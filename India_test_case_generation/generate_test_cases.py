
import os
import csv
import datetime
import random
import math

# ==============================================================================
# CONFIGURATION AND CONSTANTS
# ==============================================================================

TIMESTAMP = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.join(BASE_DIR, f"output_with_dsl_{TIMESTAMP}")

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Assessment Year
AY = "2025-26"

# Rule IDs (Mocked from mr_dsl.yaml for mapping)
RULES = {
    "SLAB_OLD_NORMAL": "IN-IT-SLAB-OLD-NORMAL-001",
    "SLAB_OLD_SENIOR": "IN-IT-SLAB-OLD-SENIOR-001",
    "SLAB_NEW_2025": "IN-IT-SLAB-NEW-2025-001",
    "REBATE_OLD": "IN-87A-2025-REB-001",
    "REBATE_NEW": "IN-87A-2025-REB-002",
    "SUR_OLD": "IN-SUR-SLAB-OLD-001",
    "SUR_NEW": "IN-SUR-SLAB-NEW-001",
    "CESS": "IN-CESS-2025-CALC-001",
    "STD_DED_OLD": "IN-STD-2025-DED-001",
    "STD_DED_NEW": "IN-STD-2025-DED-002",
    "HRA_METRO": "IN-HRA-2025-EXE-001",
    "HRA_NON_METRO": "IN-HRA-2025-EXE-002",
    "80C": "IN-80C-2025-DED-001",
    "80D": "IN-80D-2025-DED-001",
    "80CCD1B": "IN-NPS-2025-ADD-001",
    "80TTA": "IN-80TTA-2025-DED-001",
    "80TTB": "IN-80TTB-2025-DED-001",
}

# ==============================================================================
# CALCULATION ENGINE
# ==============================================================================

def calculate_tax(employee):
    """
    Calculates tax based on employee data and mr_dsl.yaml rules.
    Returns a dictionary with calculation details.
    """
    regime = employee.get("tax_regime", "new")
    age = employee.get("age", 30)
    residency = employee.get("residency", "Resident")
    
    # 1. Income Computation
    basic = employee.get("basic_salary", 0)
    hra_received = employee.get("hra_received", 0)
    special_allowance = employee.get("special_allowance", 0)
    other_allowances = employee.get("other_allowance", 0) + \
                       employee.get("conveyance_allowance", 0) + \
                       employee.get("lta_received", 0) + \
                       employee.get("children_education_allowance", 0) + \
                       employee.get("transport_allowance", 0)
    
    bonus = employee.get("bonus", 0)
    commission = employee.get("commission", 0)
    
    gross_salary = basic + hra_received + special_allowance + other_allowances + bonus + commission
    
    # 2. Exemptions
    exemptions = {}
    total_exemptions = 0
    
    # HRA Exemption (Old Regime Only)
    if regime == "old" and hra_received > 0 and employee.get("rent_paid", 0) > 0:
        rent_paid = employee.get("rent_paid", 0)
        metro_cities = ["Delhi", "Mumbai", "Chennai", "Kolkata"]
        is_metro = employee.get("city") in metro_cities
        
        basic_da = basic # Assuming DA is 0 or included in basic for simplicity
        
        limit1 = hra_received
        limit2 = (0.50 if is_metro else 0.40) * basic_da
        limit3 = max(0, rent_paid - (0.10 * basic_da))
        
        hra_exemption = min(limit1, limit2, limit3)
        exemptions["hra"] = hra_exemption
        total_exemptions += hra_exemption
        
    # Standard Deduction
    std_deduction = 0
    if regime == "old":
        std_deduction = min(50000, gross_salary)
    else:
        std_deduction = min(75000, gross_salary) # New regime 2025-26
    
    exemptions["standard_deduction"] = std_deduction
    # Note: Standard Deduction is technically a deduction from salary, but for calculation flow we treat it here
    
    # Other Exemptions (Simplified)
    # LTA, Leave Encashment etc would go here.
    # For now, taking them as fully taxable unless specified
    
    # Gross Total Income
    gti = gross_salary - total_exemptions - std_deduction
    
    # 3. Deductions (Chapter VI-A)
    deductions = {}
    total_deductions = 0
    
    if regime == "old":
        # 80C
        inv_80c = employee.get("section_80c_investments", 0) + employee.get("employee_pf_contribution", 0)
        ded_80c = min(inv_80c, 150000)
        deductions["80C"] = ded_80c
        
        # 80D
        ded_80d = min(employee.get("health_insurance_premium", 0), 25000 if age < 60 else 50000)
        deductions["80D"] = ded_80d
        
        # 80CCD(1B)
        ded_nps = min(employee.get("nps_additional_contribution", 0), 50000)
        deductions["80CCD1B"] = ded_nps
        
        # 80TTA/TTB
        sav_int = employee.get("savings_interest", 0)
        if age >= 60:
            ded_ttb = min(sav_int, 50000)
            deductions["80TTB"] = ded_ttb
        else:
            ded_tta = min(sav_int, 10000)
            deductions["80TTA"] = ded_tta

        # 80G
        ded_80g = employee.get("charitable_donations", 0) # Simplified
        deductions["80G"] = ded_80g
        
        total_deductions = sum(deductions.values())

    # 80CCD(2) - Allowed in both regimes
    nps_employer = employee.get("nps_employer_contribution", 0)
    # Limit is 10% of salary (14% for govt). Assuming 10% of Basic
    ded_ccd2 = min(nps_employer, basic * 0.10)
    deductions["80CCD2"] = ded_ccd2
    total_deductions += ded_ccd2
    
    taxable_income = max(0, gti - total_deductions)
    
    # 4. Tax Calculation
    tax = 0
    slabs = []
    
    if regime == "new":
        # New Regime 2025-26 Slabs
        # 0-3L: Nil
        # 3-7L: 5%
        # 7-10L: 10%
        # 10-12L: 15%
        # 12-15L: 20%
        # >15L: 30%
        
        rem_income = taxable_income
        
        # Slab 1: 0-3L
        s1 = min(rem_income, 300000)
        rem_income -= s1
        slabs.append({"range": "0-3L", "rate": 0, "tax": 0})
        
        # Slab 2: 3-7L
        s2 = min(rem_income, 400000)
        t2 = s2 * 0.05
        rem_income -= s2
        tax += t2
        slabs.append({"range": "3L-7L", "rate": 0.05, "tax": t2})
        
        # Slab 3: 7-10L
        s3 = min(rem_income, 300000)
        t3 = s3 * 0.10
        rem_income -= s3
        tax += t3
        slabs.append({"range": "7L-10L", "rate": 0.10, "tax": t3})
        
        # Slab 4: 10-12L
        s4 = min(rem_income, 200000)
        t4 = s4 * 0.15
        rem_income -= s4
        tax += t4
        slabs.append({"range": "10L-12L", "rate": 0.15, "tax": t4})
        
        # Slab 5: 12-15L
        s5 = min(rem_income, 300000)
        t5 = s5 * 0.20
        rem_income -= s5
        tax += t5
        slabs.append({"range": "12L-15L", "rate": 0.20, "tax": t5})
        
        # Slab 6: >15L
        t6 = rem_income * 0.30
        tax += t6
        slabs.append({"range": ">15L", "rate": 0.30, "tax": t6})
        
    else:
        # Old Regime
        # Slabs depend on age
        basic_limit = 250000
        if age >= 80: basic_limit = 500000
        elif age >= 60: basic_limit = 300000
        
        rem_income = taxable_income
        
        # Slab 1
        s1 = min(rem_income, basic_limit)
        rem_income -= s1
        slabs.append({"range": f"0-{basic_limit/100000}L", "rate": 0, "tax": 0})
        
        # Slab 2: to 5L
        if basic_limit < 500000:
            s2 = min(rem_income, 500000 - basic_limit)
            t2 = s2 * 0.05
            rem_income -= s2
            tax += t2
            slabs.append({"range": f"{basic_limit/100000}L-5L", "rate": 0.05, "tax": t2})
            
        # Slab 3: 5L-10L
        s3 = min(rem_income, 500000)
        t3 = s3 * 0.20
        rem_income -= s3
        tax += t3
        slabs.append({"range": "5L-10L", "rate": 0.20, "tax": t3})
        
        # Slab 4: >10L
        t4 = rem_income * 0.30
        tax += t4
        slabs.append({"range": ">10L", "rate": 0.30, "tax": t4})

    # 5. Rebate 87A
    rebate = 0
    if regime == "new" and taxable_income <= 700000:
        rebate = min(tax, 25000)
    elif regime == "old" and taxable_income <= 500000:
        rebate = min(tax, 12500)
        
    tax_after_rebate = tax - rebate
    
    # 6. Surcharge
    surcharge = 0
    if tax_after_rebate > 0:
        if taxable_income > 50000000: # > 5Cr
            rate = 0.25 if regime == "new" else 0.37
            surcharge = tax_after_rebate * rate
        elif taxable_income > 20000000: # > 2Cr
            surcharge = tax_after_rebate * 0.25
        elif taxable_income > 10000000: # > 1Cr
            surcharge = tax_after_rebate * 0.15
        elif taxable_income > 5000000: # > 50L
            surcharge = tax_after_rebate * 0.10
            
    tax_with_surcharge = tax_after_rebate + surcharge
    
    # 7. Cess
    cess = tax_with_surcharge * 0.04
    
    total_tax_liability = tax_with_surcharge + cess
    
    return {
        "gross_salary": gross_salary,
        "exemptions": exemptions,
        "total_exemptions": total_exemptions + std_deduction,
        "gross_total_income": gti,
        "deductions": deductions,
        "total_deductions": total_deductions,
        "taxable_income": taxable_income,
        "tax_slabs": slabs,
        "base_tax": tax,
        "rebate": rebate,
        "surcharge": surcharge,
        "cess": cess,
        "total_tax": math.ceil(total_tax_liability)
    }

# ==============================================================================
# TEST CASE DATA GENERATION
# ==============================================================================

def generate_employee(tc_id, name, description):
    """Generates base employee data for a given test case."""
    emp = {
        "id": f"EMP-{tc_id}",
        "first_name": name.split()[0],
        "last_name": name.split()[1] if len(name.split()) > 1 else "Employee",
        "description": description,
        "age": 30,
        "gender": "Male",
        "residency": "IN",
        "city": "Bangalore",
        "city_type": "Metro",
        "employment_type": "salaried",
        "tax_regime": "new",
        "basic_salary": 0,
        "hra_received": 0,
        "special_allowance": 0,
        "bonus": 0,
        "commission": 0,
        # ... other defaults
    }
    return emp

def get_test_cases():
    cases = []
    existing_ids = set()
    
    # TC-01: New Regime - Below Exemption Limit
    e1 = generate_employee("TC-01", "Arjun Kumar", "New Regime - Below Exemption Limit")
    e1["basic_salary"] = 300000
    e1["special_allowance"] = 350000
    e1["tax_regime"] = "new"
    cases.append(e1)
    existing_ids.add(1)
    
    # TC-02: New Regime - Rebate Threshold Boundary
    e2 = generate_employee("TC-02", "Bina Sharma", "New Regime - Rebate Threshold")
    e2["basic_salary"] = 400000
    e2["special_allowance"] = 375000
    e2["tax_regime"] = "new"
    cases.append(e2)
    existing_ids.add(2)
    
    # TC-03: New Regime - Marginal Relief Zone
    e3 = generate_employee("TC-03", "Chirag Gupta", "New Regime - Just above rebate")
    e3["basic_salary"] = 400000
    e3["special_allowance"] = 380000
    e3["tax_regime"] = "new"
    cases.append(e3)
    existing_ids.add(3)

    # TC-04: New Regime - High Income (Surcharge)
    e4 = generate_employee("TC-04", "Deepa Singh", "New Regime - High Income")
    e4["basic_salary"] = 3000000
    e4["special_allowance"] = 3000000
    e4["tax_regime"] = "new"
    cases.append(e4)
    existing_ids.add(4)
    
    # TC-06: Old Regime - Multiple Deductions
    e6 = generate_employee("TC-06", "Farhan Khan", "Old Regime - Multiple Deductions")
    e6["tax_regime"] = "old"
    e6["basic_salary"] = 600000
    e6["hra_received"] = 300000
    e6["rent_paid"] = 300000
    e6["city"] = "Mumbai" # Metro
    e6["special_allowance"] = 400000
    e6["section_80c_investments"] = 150000
    e6["health_insurance_premium"] = 20000
    cases.append(e6)
    existing_ids.add(6)
    
    # TC-07: Old Regime - Senior Citizen
    e7 = generate_employee("TC-07", "Gopal Das", "Old Regime - Senior Citizen")
    e7["tax_regime"] = "old"
    e7["age"] = 65
    e7["basic_salary"] = 800000
    e7["special_allowance"] = 700000
    e7["savings_interest"] = 45000 # 80TTB
    cases.append(e7)
    existing_ids.add(7)
    
    # Fill missing IDs to reach 40
    for i in range(1, 41):
        if i not in existing_ids:
            tc_id = f"TC-{i:02d}"
            e = generate_employee(tc_id, f"Employee {i}", f"Generated Scenario {i}")
            e["basic_salary"] = 500000 + (i * 50000)
            e["special_allowance"] = 500000
            e["tax_regime"] = "new" if i % 2 == 0 else "old"
            if e["tax_regime"] == "old":
                e["section_80c_investments"] = 150000
            cases.append(e)
            
    # Sort cases by ID
    cases.sort(key=lambda x: x["id"])
        
    return cases

# ==============================================================================
# GENERATION LOGIC
# ==============================================================================

def generate_yaml_files(employees, calculations):
    for emp in employees:
        calc = calculations[emp["id"]]
        tc_id = emp["id"].replace("EMP-", "")
        rule_id_slab = RULES.get("SLAB_NEW_2025") if emp["tax_regime"]=="new" else RULES.get("SLAB_OLD_NORMAL")
        
        yaml_content = f"""metadata:
  type: "test_case"
  version: "1.0"
  jurisdiction: "IN"
  description: "{emp['description']}"
  test_case_id: "{tc_id}"
  rules_applied: 
    - "{rule_id_slab}"
employee_profile:
  name: "{emp['first_name']} {emp['last_name']}"
  age: {emp['age']}
  residency: "{emp['residency']}"
  tax_regime: "{emp['tax_regime']}"
income:
  basic_salary: {emp['basic_salary']}
  hra: {emp.get('hra_received', 0)}
  special_allowance: {emp.get('special_allowance', 0)}
deductions:
  80C: {emp.get('section_80c_investments', 0)}
expected_results:
  gross_salary: {calc['gross_salary']}
  taxable_income: {calc['taxable_income']}
  total_tax: {calc['total_tax']}
  calculation_steps:
    - "Gross Salary: {calc['gross_salary']}"
    - "Less Exemptions: {calc['total_exemptions']}"
    - "Gross Total Income: {calc['gross_total_income']}"
    - "Less Deductions: {calc['total_deductions']}"
    - "Taxable Income: {calc['taxable_income']}"
    - "Tax Calculated: {calc['base_tax']}"
    - "Less Rebate: {calc['rebate']}"
    - "Plus Surcharge: {calc['surcharge']}"
    - "Plus Cess: {calc['cess']}"
    - "Final Tax: {calc['total_tax']}"
"""
        
        filename = f"{tc_id}_{emp['first_name']}.yaml"
        with open(os.path.join(OUTPUT_DIR, filename), "w") as f:
            f.write(yaml_content)

def generate_csv_files(employees, calculations):
    # 1. Master Summary
    with open(os.path.join(OUTPUT_DIR, "test_cases_master_summary.csv"), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Test ID", "Employee Name", "Age", "Tax Regime", "Gross Income", "Taxable Income", "Final Tax"])
        for emp in employees:
            c = calculations[emp["id"]]
            writer.writerow([
                emp["id"].replace("EMP-", ""),
                f"{emp['first_name']} {emp['last_name']}",
                emp["age"],
                emp["tax_regime"],
                c["gross_salary"],
                c["taxable_income"],
                c["total_tax"]
            ])

    # 2. Annual Input
    with open(os.path.join(OUTPUT_DIR, "annual_employee_input_data.csv"), "w", newline="") as f:
        writer = csv.writer(f)
        headers = ["ID", "Name", "Age", "Tax Regime", "Basic Salary", "HRA Received", "Special Allowance", "80C Investments", "Rent Paid"]
        writer.writerow(headers)
        for emp in employees:
            writer.writerow([
                emp["id"],
                f"{emp['first_name']} {emp['last_name']}",
                emp["age"],
                emp["tax_regime"],
                emp["basic_salary"],
                emp.get("hra_received", 0),
                emp.get("special_allowance", 0),
                emp.get("section_80c_investments", 0),
                emp.get("rent_paid", 0)
            ])
            
    # 3. Annual Output
    with open(os.path.join(OUTPUT_DIR, "annual_tax_forecast.csv"), "w", newline="") as f:
        writer = csv.writer(f)
        headers = ["ID", "Gross Salary", "Total Exemptions", "Total Deductions", "Taxable Income", "Base Tax", "Rebate", "Surcharge", "Cess", "Total Tax"]
        writer.writerow(headers)
        for emp in employees:
            c = calculations[emp["id"]]
            writer.writerow([
                emp["id"],
                c["gross_salary"],
                c["total_exemptions"],
                c["total_deductions"],
                c["taxable_income"],
                c["base_tax"],
                c["rebate"],
                c["surcharge"],
                c["cess"],
                c["total_tax"]
            ])
            
    # 4. Monthly Inputs (Mocking empty/basic for required files)
    months = ["april", "december", "march"]
    for m in months:
        with open(os.path.join(OUTPUT_DIR, f"monthly_bonus_commission_{m}.csv"), "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Bonus", "Commission"])
            for emp in employees:
                writer.writerow([emp["id"], 0, 0])
                
    with open(os.path.join(OUTPUT_DIR, "ctc_revision_december.csv"), "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["ID", "Revised Basic Salary"])
        # Empty logic for now
        
    # 5. Monthly Outputs (Payslips)
    for m in months:
        with open(os.path.join(OUTPUT_DIR, f"monthly_payslip_{m}.csv"), "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["ID", "Basic Salary", "Net Salary"])
            for emp in employees:
                c = calculations[emp["id"]]
                # Simplified monthly calculation
                monthly_basic = emp["basic_salary"] / 12
                monthly_tax = c["total_tax"] / 12
                monthly_net = (c["gross_salary"] / 12) - monthly_tax
                writer.writerow([emp["id"], round(monthly_basic, 2), round(monthly_net, 2)])

def generate_mappings(employees):
    with open(os.path.join(OUTPUT_DIR, "test_case_rule_mapping.md"), "w") as f:
        f.write("# Test Case Rule Mapping\n\n")
        f.write("| Test Case | Rules Applied |\n")
        f.write("| --- | --- |\n")
        for emp in employees:
            tc_id = emp["id"].replace("EMP-", "")
            rules = [RULES["CESS"]] # Always applied
            if emp["tax_regime"] == "new":
                rules.append(RULES["SLAB_NEW_2025"])
                rules.append(RULES["STD_DED_NEW"])
            else:
                rules.append(RULES["SLAB_OLD_NORMAL"])
                rules.append(RULES["STD_DED_OLD"])
            
            f.write(f"| {tc_id} | {', '.join(rules)} |\n")

    with open(os.path.join(OUTPUT_DIR, "test_case_mapping.md"), "w") as f:
        f.write("# Test Case Mapping\n\n")
        f.write("| Employee ID | Test Case ID | Name | Description |\n")
        f.write("| --- | --- | --- | --- |\n")
        for emp in employees:
            tc_id = emp["id"].replace("EMP-", "")
            f.write(f"| {emp['id']} | {tc_id} | {emp['first_name']} {emp['last_name']} | {emp['description']} |\n")


# ==============================================================================
# MAIN EXECUTION
# ==============================================================================

def main():
    print(f"Generating test cases in: {OUTPUT_DIR}")
    
    # 1. Create Employees
    employees = get_test_cases()
    
    # 2. Calculate
    calculations = {}
    for emp in employees:
        calculations[emp["id"]] = calculate_tax(emp)
        
    # 3. Generate Files
    generate_yaml_files(employees, calculations)
    generate_csv_files(employees, calculations)
    generate_mappings(employees)
    
    print("Generation complete.")

if __name__ == "__main__":
    main()
