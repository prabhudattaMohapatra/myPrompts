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
print("COMPREHENSIVE CALCULATION VERIFICATION REPORT")
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
consistency_issues = 0

print("=" * 80)
print("PART 1: INPUT DATA VERIFICATION")
print("=" * 80)
print()

for emp_id, emp in input_data.items():
    issues_found = []
    
    # Verify gross salary = sum of components
    gross_salary = parse_value(emp.get('gross_salary', 0))
    basic_salary = parse_value(emp.get('basic_salary', 0))
    hra_received = parse_value(emp.get('hra_received', 0))
    special_allowance = parse_value(emp.get('special_allowance', 0))
    transport_allowance = parse_value(emp.get('transport_allowance', 0))
    conveyance_allowance = parse_value(emp.get('conveyance_allowance', 0))
    meal_vouchers = parse_value(emp.get('meal_vouchers', 0))
    lta_received = parse_value(emp.get('lta_received', 0))
    bonus = parse_value(emp.get('bonus', 0))
    commission = parse_value(emp.get('commission', 0))
    
    # Calculate expected gross
    calculated_gross = (basic_salary + hra_received + special_allowance + 
                       transport_allowance + conveyance_allowance + meal_vouchers + 
                       lta_received + bonus + commission)
    
    if abs(gross_salary - calculated_gross) > Decimal('1'):
        issues_found.append(f"Gross salary mismatch: Stated={gross_salary}, Calculated={calculated_gross}")
    
    # Verify CTC = gross + employer contributions
    annual_ctc = parse_value(emp.get('annual_ctc', 0))
    employer_pf = parse_value(emp.get('employer_pf_contribution', 0))
    nps_employer = parse_value(emp.get('nps_employer_contribution', 0))
    
    calculated_ctc = gross_salary + employer_pf + nps_employer
    if abs(annual_ctc - calculated_ctc) > Decimal('1'):
        issues_found.append(f"CTC mismatch: Stated={annual_ctc}, Expected={calculated_ctc}")
    
    # Verify PF contributions (should be 12% of basic, capped at 15,000/month)
    employee_pf = parse_value(emp.get('employee_pf_contribution', 0))
    expected_pf_base = min(basic_salary, Decimal('180000'))  # 15,000 * 12
    expected_pf = round_currency(expected_pf_base * Decimal('0.12'))
    
    if basic_salary > 0 and abs(employee_pf - expected_pf) > Decimal('1'):
        issues_found.append(f"Employee PF incorrect: Stated={employee_pf}, Expected={expected_pf}")
    
    if basic_salary > 0 and abs(employer_pf - expected_pf) > Decimal('1'):
        issues_found.append(f"Employer PF incorrect: Stated={employer_pf}, Expected={expected_pf}")
    
    if issues_found:
        input_issues += 1
        print(f"\n{emp_id} - INPUT ISSUES FOUND:")
        for issue in issues_found:
            print(f"  ❌ {issue}")

if input_issues == 0:
    print("✅ All input data calculations are correct!")
else:
    print(f"\n⚠️  Found input issues in {input_issues} out of {total_employees} employees")

print()
print("=" * 80)
print("PART 2: OUTPUT DATA VERIFICATION")
print("=" * 80)
print()

for emp_id, output in output_data.items():
    issues_found = []
    input_emp = input_data.get(emp_id, {})
    
    # Get regime
    tax_regime = output.get('tax_regime')
    
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
    
    total_exemptions = parse_value(output.get('total_exemptions', 0))
    calculated_exemptions = (hra_exemption + conveyance_exemption + lta_exemption + 
                            transport_exemption + meal_voucher_exemption + 
                            children_education_exemption + children_hostel_exemption + 
                            books_periodical_exemption + telephone_exemption)
    
    if abs(total_exemptions - calculated_exemptions) > Decimal('1'):
        issues_found.append(f"Total exemptions mismatch: Stated={total_exemptions}, Calculated={calculated_exemptions}")
    
    # Verify total deductions
    standard_deduction = parse_value(output.get('standard_deduction', 0))
    professional_tax = parse_value(output.get('professional_tax_deduction', 0))
    c80 = parse_value(output.get('80c_deduction', 0))
    ccd1 = parse_value(output.get('80ccd1_deduction', 0))
    ccd2 = parse_value(output.get('80ccd2_deduction', 0))
    ccd1b = parse_value(output.get('80ccd1b_deduction', 0))
    d80 = parse_value(output.get('80d_total_deduction', 0))
    dd80 = parse_value(output.get('80dd_deduction', 0))
    u80 = parse_value(output.get('80u_deduction', 0))
    g80 = parse_value(output.get('80g_deduction', 0))
    tta = parse_value(output.get('80tta_deduction', 0))
    ttb = parse_value(output.get('80ttb_deduction', 0))
    b24 = parse_value(output.get('24b_deduction', 0))
    eea = parse_value(output.get('80eea_deduction', 0))
    eeb = parse_value(output.get('80eeb_deduction', 0))
    ddb = parse_value(output.get('80ddb_deduction', 0))
    
    total_deductions = parse_value(output.get('total_deductions', 0))
    calculated_deductions = (standard_deduction + professional_tax + c80 + ccd1 + ccd2 + 
                            ccd1b + d80 + dd80 + u80 + g80 + tta + ttb + b24 + eea + eeb + ddb)
    
    if abs(total_deductions - calculated_deductions) > Decimal('1'):
        issues_found.append(f"Total deductions mismatch: Stated={total_deductions}, Calculated={calculated_deductions}")
    
    # Verify taxable income
    gross_income = parse_value(output.get('gross_income', 0))
    taxable_income = parse_value(output.get('taxable_income', 0))
    calculated_taxable = gross_income - total_exemptions - total_deductions
    
    if abs(taxable_income - calculated_taxable) > Decimal('1'):
        issues_found.append(f"Taxable income mismatch: Stated={taxable_income}, Calculated={calculated_taxable}")
    
    # Verify tax calculation
    base_tax = parse_value(output.get('base_tax', 0))
    rebate = parse_value(output.get('rebate_87a', 0))
    tax_after_rebate = parse_value(output.get('tax_after_rebate', 0))
    
    if abs(tax_after_rebate - (base_tax - rebate)) > Decimal('0.1'):
        issues_found.append(f"Tax after rebate incorrect: Should be {base_tax - rebate}, got {tax_after_rebate}")
    
    # Verify surcharge and cess
    surcharge = parse_value(output.get('surcharge', 0))
    tax_with_surcharge = parse_value(output.get('tax_with_surcharge', 0))
    
    if abs(tax_with_surcharge - (tax_after_rebate + surcharge)) > Decimal('0.1'):
        issues_found.append(f"Tax with surcharge incorrect: Should be {tax_after_rebate + surcharge}, got {tax_with_surcharge}")
    
    cess = parse_value(output.get('health_education_cess', 0))
    expected_cess = round_currency(tax_with_surcharge * Decimal('0.04'))
    
    if abs(cess - expected_cess) > Decimal('0.1'):
        issues_found.append(f"Cess incorrect: Should be {expected_cess}, got {cess}")
    
    # Verify total tax liability
    total_tax = parse_value(output.get('total_tax_liability', 0))
    calculated_total_tax = tax_with_surcharge + cess
    
    if abs(total_tax - calculated_total_tax) > Decimal('0.1'):
        issues_found.append(f"Total tax liability incorrect: Should be {calculated_total_tax}, got {total_tax}")
    
    # Verify monthly TDS
    monthly_tds = parse_value(output.get('monthly_tds', 0))
    expected_monthly_tds = round_currency(total_tax / 12)
    
    if abs(monthly_tds - expected_monthly_tds) > Decimal('0.5'):
        issues_found.append(f"Monthly TDS incorrect: Should be {expected_monthly_tds}, got {monthly_tds}")
    
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
print("PART 3: CROSS-FILE CONSISTENCY VERIFICATION")
print("=" * 80)
print()

for emp_id in input_data.keys():
    if emp_id not in output_data:
        print(f"❌ {emp_id}: Present in input but missing in output")
        consistency_issues += 1
        continue
    
    input_emp = input_data[emp_id]
    output_emp = output_data[emp_id]
    
    issues_found = []
    
    # Verify gross salary matches
    input_gross = parse_value(input_emp.get('gross_salary', 0))
    output_gross = parse_value(output_emp.get('gross_salary', 0))
    
    if abs(input_gross - output_gross) > Decimal('1'):
        issues_found.append(f"Gross salary mismatch: Input={input_gross}, Output={output_gross}")
    
    # Verify basic salary matches
    input_basic = parse_value(input_emp.get('basic_salary', 0))
    output_basic = parse_value(output_emp.get('basic_salary', 0))
    
    if abs(input_basic - output_basic) > Decimal('1'):
        issues_found.append(f"Basic salary mismatch: Input={input_basic}, Output={output_basic}")
    
    # Verify tax regime matches
    input_regime = input_emp.get('tax_regime', '')
    output_regime = output_emp.get('tax_regime', '')
    
    if input_regime != output_regime:
        issues_found.append(f"Tax regime mismatch: Input={input_regime}, Output={output_regime}")
    
    if issues_found:
        consistency_issues += 1
        print(f"\n{emp_id} - CONSISTENCY ISSUES:")
        for issue in issues_found:
            print(f"  ❌ {issue}")

if consistency_issues == 0:
    print("✅ All cross-file data is consistent!")
else:
    print(f"\n⚠️  Found consistency issues in {consistency_issues} out of {total_employees} employees")

print()
print("=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"Total Employees Verified: {total_employees}")
print(f"Input Data Issues: {input_issues}")
print(f"Output Calculation Issues: {output_issues}")
print(f"Cross-File Consistency Issues: {consistency_issues}")
print()

if input_issues == 0 and output_issues == 0 and consistency_issues == 0:
    print("🎉 ALL VERIFICATIONS PASSED! All calculations are correct!")
else:
    print(f"⚠️  Total Issues Found: {input_issues + output_issues + consistency_issues}")
    print("   Please review the issues above and make necessary corrections.")

print("=" * 80)
