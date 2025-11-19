import csv
from decimal import Decimal, ROUND_HALF_UP

def parse_value(value):
    """Parse string value to Decimal"""
    if value in ('', 'true', 'false', None):
        return Decimal('0')
    try:
        return Decimal(str(value))
    except:
        return Decimal('0')

def round_currency(value):
    """Round to 2 decimal places"""
    return value.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

print("=" * 80)
print("CORRECTED CALCULATION VERIFICATION REPORT")
print("=" * 80)
print()

# Load data
print("Loading data files...")
input_data = {}
with open('annual_employee_input_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        input_data[row['employee_id']] = row

output_data = {}
with open('annual_tax_forecast.csv', 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        output_data[row['employee_id']] = row

print(f"✓ Loaded {len(input_data)} employees from input file")
print(f"✓ Loaded {len(output_data)} employees from output file")
print()

# Verification counters
total_employees = len(input_data)
input_issues = 0
output_issues = 0

print("=" * 80)
print("PART 1: INPUT DATA VERIFICATION (CORRECTED PF CALCULATION)")
print("=" * 80)
print()

for emp_id, emp in input_data.items():
    issues_found = []
    
    # Verify PF contributions (should be 12% of basic salary - NO CAP)
    basic_salary = parse_value(emp.get('basic_salary', 0))
    employee_pf = parse_value(emp.get('employee_pf_contribution', 0))
    employer_pf = parse_value(emp.get('employer_pf_contribution', 0))
    
    if basic_salary > 0:
        expected_pf = round_currency(basic_salary * Decimal('0.12'))
        
        if abs(employee_pf - expected_pf) > Decimal('1'):
            issues_found.append(f"Employee PF incorrect: Stated={employee_pf}, Expected={expected_pf} (12% of {basic_salary})")
        
        if abs(employer_pf - expected_pf) > Decimal('1'):
            issues_found.append(f"Employer PF incorrect: Stated={employer_pf}, Expected={expected_pf} (12% of {basic_salary})")
    
    # Verify gross salary matches sum of components (including bonuses)
    gross_salary = parse_value(emp.get('gross_salary', 0))
    hra_received = parse_value(emp.get('hra_received', 0))
    special_allowance = parse_value(emp.get('special_allowance', 0))
    transport_allowance = parse_value(emp.get('transport_allowance', 0))
    conveyance_allowance = parse_value(emp.get('conveyance_allowance', 0))
    meal_vouchers = parse_value(emp.get('meal_vouchers', 0))
    lta_received = parse_value(emp.get('lta_received', 0))
    bonus = parse_value(emp.get('bonus', 0))
    commission = parse_value(emp.get('commission', 0))
    
    # Note: Gross salary typically does NOT include bonus/commission if they're variable
    # Calculate expected gross (without bonus/commission as they're typically variable)
    calculated_gross = (basic_salary + hra_received + special_allowance + 
                       transport_allowance + conveyance_allowance + meal_vouchers + lta_received)
    
    if abs(gross_salary - calculated_gross) > Decimal('1'):
        # Check if it includes bonus/commission
        calculated_gross_with_bonus = calculated_gross + bonus + commission
        if abs(gross_salary - calculated_gross_with_bonus) > Decimal('1'):
            issues_found.append(f"Gross salary mismatch: Stated={gross_salary}, Calculated (excl bonus/comm)={calculated_gross}, Calculated (incl bonus/comm)={calculated_gross_with_bonus}")
    
    # Verify CTC = gross + employer contributions (typically)
    annual_ctc = parse_value(emp.get('annual_ctc', 0))
    nps_employer = parse_value(emp.get('nps_employer_contribution', 0))
    
    # CTC can be defined differently by companies, so this is just a check
    calculated_ctc = gross_salary + employer_pf + nps_employer
    if abs(annual_ctc - calculated_ctc) > Decimal('1') and abs(annual_ctc - gross_salary) > Decimal('1'):
        issues_found.append(f"CTC check: Stated={annual_ctc}, Calculated (Gross+Employer contributions)={calculated_ctc}, Gross alone={gross_salary}")
    
    if issues_found:
        input_issues += 1
        print(f"\n{emp_id} - INPUT ISSUES:")
        for issue in issues_found:
            print(f"  ⚠️  {issue}")

if input_issues == 0:
    print("✅ All input data calculations are correct!")
else:
    print(f"\n⚠️  Found potential input issues in {input_issues} out of {total_employees} employees")

print()
print("=" * 80)
print("PART 2: OUTPUT DATA VERIFICATION")
print("=" * 80)
print()

for emp_id, output in output_data.items():
    issues_found = []
    input_emp = input_data.get(emp_id, {})
    
    # Verify total exemptions
    hra_exemption = parse_value(output.get('hra_exemption', 0))
    conveyance_exemption = parse_value(output.get('conveyance_exemption', 0))
    lta_exemption = parse_value(output.get('lta_exemption', 0))
    transport_exemption = parse_value(output.get('transport_exemption', 0))
    meal_voucher_exemption = parse_value(output.get('meal_voucher_exemption', 0))
    children_education_exemption = parse_value(output.get('children_education_exemption', 0))
    children_hostel_exemption = parse_value(output.get('children_hostel_exemption', 0))
    books_periodical_exemption = parse_value(output.get('books_periodical_exemption', 0))
    telephone_exemption = parse_value(output.get('telephone_exemption', 0))
    insurance_exemption = parse_value(output.get('insurance_exemption', 0))
    motor_car_exemption = parse_value(output.get('motor_car_exemption', 0))
    other_exemptions = parse_value(output.get('other_exemptions', 0))
    
    total_exemptions = parse_value(output.get('total_exemptions', 0))
    calculated_exemptions = (hra_exemption + conveyance_exemption + lta_exemption + 
                            transport_exemption + meal_voucher_exemption + 
                            children_education_exemption + children_hostel_exemption + 
                            books_periodical_exemption + telephone_exemption +
                            insurance_exemption + motor_car_exemption + other_exemptions)
    
    if abs(total_exemptions - calculated_exemptions) > Decimal('1'):
        issues_found.append(f"Total exemptions: Stated={total_exemptions}, Calculated={calculated_exemptions}, Difference={total_exemptions - calculated_exemptions}")
    
    # Verify total deductions
    standard_deduction = parse_value(output.get('standard_deduction', 0))
    professional_tax = parse_value(output.get('professional_tax_deduction', 0))
    c80 = parse_value(output.get('80c_deduction', 0))
    ccd1 = parse_value(output.get('80ccd1_deduction', 0))
    ccd2 = parse_value(output.get('80ccd2_deduction', 0))
    ccd1b = parse_value(output.get('80ccd1b_deduction', 0))
    d80_self = parse_value(output.get('80d_self_deduction', 0))
    d80_parents = parse_value(output.get('80d_parents_deduction', 0))
    d80_total = parse_value(output.get('80d_total_deduction', 0))
    dd80 = parse_value(output.get('80dd_deduction', 0))
    u80 = parse_value(output.get('80u_deduction', 0))
    g80 = parse_value(output.get('80g_deduction', 0))
    tta = parse_value(output.get('80tta_deduction', 0))
    ttb = parse_value(output.get('80ttb_deduction', 0))
    b24 = parse_value(output.get('24b_deduction', 0))
    eea = parse_value(output.get('80eea_deduction', 0))
    eeb = parse_value(output.get('80eeb_deduction', 0))
    ddb = parse_value(output.get('80ddb_deduction', 0))
    family_pension = parse_value(output.get('family_pension_deduction', 0))
    
    total_deductions = parse_value(output.get('total_deductions', 0))
    
    # Use the total 80D deduction if available, otherwise sum self + parents
    d80_to_use = d80_total if d80_total > 0 else (d80_self + d80_parents)
    
    calculated_deductions = (standard_deduction + professional_tax + c80 + ccd1 + ccd2 + 
                            ccd1b + d80_to_use + dd80 + u80 + g80 + tta + ttb + b24 + eea + eeb + ddb + family_pension)
    
    if abs(total_deductions - calculated_deductions) > Decimal('1'):
        issues_found.append(f"Total deductions: Stated={total_deductions}, Calculated={calculated_deductions}, Difference={total_deductions - calculated_deductions}")
    
    # Verify taxable income = gross - exemptions - deductions
    gross_income = parse_value(output.get('gross_income', 0))
    income_after_exemptions = parse_value(output.get('income_after_exemptions', 0))
    taxable_income = parse_value(output.get('taxable_income', 0))
    
    calculated_income_after_exemptions = gross_income - total_exemptions
    if abs(income_after_exemptions - calculated_income_after_exemptions) > Decimal('1'):
        issues_found.append(f"Income after exemptions: Stated={income_after_exemptions}, Calculated={calculated_income_after_exemptions}")
    
    calculated_taxable = gross_income - total_exemptions - total_deductions
    if abs(taxable_income - calculated_taxable) > Decimal('1'):
        issues_found.append(f"Taxable income: Stated={taxable_income}, Calculated={calculated_taxable}")
    
    # Verify tax calculation components
    base_tax = parse_value(output.get('base_tax', 0))
    rebate = parse_value(output.get('rebate_87a', 0))
    tax_after_rebate = parse_value(output.get('tax_after_rebate', 0))
    
    if abs(tax_after_rebate - (base_tax - rebate)) > Decimal('0.1'):
        issues_found.append(f"Tax after rebate: Should be {base_tax - rebate}, got {tax_after_rebate}")
    
    surcharge = parse_value(output.get('surcharge', 0))
    tax_with_surcharge = parse_value(output.get('tax_with_surcharge', 0))
    
    if abs(tax_with_surcharge - (tax_after_rebate + surcharge)) > Decimal('0.1'):
        issues_found.append(f"Tax with surcharge: Should be {tax_after_rebate + surcharge}, got {tax_with_surcharge}")
    
    cess = parse_value(output.get('health_education_cess', 0))
    expected_cess = round_currency(tax_with_surcharge * Decimal('0.04'))
    
    if abs(cess - expected_cess) > Decimal('0.1'):
        issues_found.append(f"Cess: Should be {expected_cess}, got {cess}")
    
    total_tax = parse_value(output.get('total_tax_liability', 0))
    calculated_total_tax = tax_with_surcharge + cess
    
    if abs(total_tax - calculated_total_tax) > Decimal('0.1'):
        issues_found.append(f"Total tax liability: Should be {calculated_total_tax}, got {total_tax}")
    
    if issues_found:
        output_issues += 1
        print(f"\n{emp_id} - OUTPUT CALCULATION ISSUES:")
        for issue in issues_found:
            print(f"  ❌ {issue}")

if output_issues == 0:
    print("✅ All output calculations are correct!")
else:
    print(f"\n⚠️  Found output calculation issues in {output_issues} out of {total_employees} employees")

print()
print("=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"Total Employees Verified: {total_employees}")
print(f"Input Data Issues: {input_issues}")
print(f"Output Calculation Issues: {output_issues}")
print()

if input_issues == 0 and output_issues == 0:
    print("🎉 ALL VERIFICATIONS PASSED! All calculations are correct!")
else:
    total_issues = input_issues + output_issues
    print(f"⚠️  Total Issues Found: {total_issues}")
    print("   Review the issues above for any necessary corrections.")

print("=" * 80)
