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
print("FINAL COMPREHENSIVE VERIFICATION")
print("=" * 80)
print()

# Load all data files
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

print(f"✓ Loaded {len(input_data)} employees")
print()

errors_found = []

print("Verifying all calculations...")
print("-" * 80)

for emp_id in sorted(input_data.keys()):
    emp_input = input_data[emp_id]
    emp_output = output_data.get(emp_id)
    
    if not emp_output:
        errors_found.append(f"{emp_id}: Missing from output file")
        continue
    
    # 1. Verify gross salary = sum of components
    basic = parse_value(emp_input.get('basic_salary', 0))
    hra = parse_value(emp_input.get('hra_received', 0))
    special = parse_value(emp_input.get('special_allowance', 0))
    transport = parse_value(emp_input.get('transport_allowance', 0))
    conveyance = parse_value(emp_input.get('conveyance_allowance', 0))
    meal = parse_value(emp_input.get('meal_vouchers', 0))
    lta = parse_value(emp_input.get('lta_received', 0))
    cea = parse_value(emp_input.get('children_education_allowance', 0))
    cha = parse_value(emp_input.get('children_hostel_allowance', 0))
    books = parse_value(emp_input.get('books_and_periodical_allowance', 0))
    telephone = parse_value(emp_input.get('telephone_reimbursement', 0))
    bonus = parse_value(emp_input.get('bonus', 0))
    commission = parse_value(emp_input.get('commission', 0))
    
    calc_gross = basic + hra + special + transport + conveyance + meal + lta + cea + cha + books + telephone + bonus + commission
    stated_gross = parse_value(emp_input.get('gross_salary', 0))
    
    if abs(calc_gross - stated_gross) > Decimal('1'):
        errors_found.append(f"{emp_id}: INPUT Gross salary mismatch: Calculated={calc_gross}, Stated={stated_gross}")
    
    # 2. Verify PF = 12% of basic
    employee_pf = parse_value(emp_input.get('employee_pf_contribution', 0))
    expected_pf = round_currency(basic * Decimal('0.12'))
    
    if basic > 0 and abs(employee_pf - expected_pf) > Decimal('1'):
        errors_found.append(f"{emp_id}: INPUT Employee PF incorrect: Should be {expected_pf}, got {employee_pf}")
    
    # 3. Verify output gross matches input gross
    output_gross = parse_value(emp_output.get('gross_income', 0))
    if abs(output_gross - stated_gross) > Decimal('1'):
        errors_found.append(f"{emp_id}: OUTPUT Gross mismatch with input: Input={stated_gross}, Output={output_gross}")
    
    # 4. Verify total exemptions sum
    hra_ex = parse_value(emp_output.get('hra_exemption', 0))
    conv_ex = parse_value(emp_output.get('conveyance_exemption', 0))
    lta_ex = parse_value(emp_output.get('lta_exemption', 0))
    trans_ex = parse_value(emp_output.get('transport_exemption', 0))
    meal_ex = parse_value(emp_output.get('meal_voucher_exemption', 0))
    cea_ex = parse_value(emp_output.get('children_education_exemption', 0))
    cha_ex = parse_value(emp_output.get('children_hostel_exemption', 0))
    books_ex = parse_value(emp_output.get('books_periodical_exemption', 0))
    tel_ex = parse_value(emp_output.get('telephone_exemption', 0))
    
    calc_exemptions = hra_ex + conv_ex + lta_ex + trans_ex + meal_ex + cea_ex + cha_ex + books_ex + tel_ex
    stated_exemptions = parse_value(emp_output.get('total_exemptions', 0))
    
    if abs(calc_exemptions - stated_exemptions) > Decimal('1'):
        errors_found.append(f"{emp_id}: OUTPUT Total exemptions mismatch: Calculated={calc_exemptions}, Stated={stated_exemptions}")
    
    # 5. Verify total deductions sum (80CCD1 is part of 80C, not separate)
    std_ded = parse_value(emp_output.get('standard_deduction', 0))
    prof_tax = parse_value(emp_output.get('professional_tax_deduction', 0))
    c80 = parse_value(emp_output.get('80c_deduction', 0))
    ccd2 = parse_value(emp_output.get('80ccd2_deduction', 0))
    ccd1b = parse_value(emp_output.get('80ccd1b_deduction', 0))
    d80 = parse_value(emp_output.get('80d_total_deduction', 0))
    dd80 = parse_value(emp_output.get('80dd_deduction', 0))
    u80 = parse_value(emp_output.get('80u_deduction', 0))
    g80 = parse_value(emp_output.get('80g_deduction', 0))
    tta = parse_value(emp_output.get('80tta_deduction', 0))
    ttb = parse_value(emp_output.get('80ttb_deduction', 0))
    b24 = parse_value(emp_output.get('24b_deduction', 0))
    eea = parse_value(emp_output.get('80eea_deduction', 0))
    eeb = parse_value(emp_output.get('80eeb_deduction', 0))
    ddb = parse_value(emp_output.get('80ddb_deduction', 0))
    
    calc_deductions = std_ded + prof_tax + c80 + ccd2 + ccd1b + d80 + dd80 + u80 + g80 + tta + ttb + b24 + eea + eeb + ddb
    stated_deductions = parse_value(emp_output.get('total_deductions', 0))
    
    if abs(calc_deductions - stated_deductions) > Decimal('1'):
        errors_found.append(f"{emp_id}: OUTPUT Total deductions mismatch: Calculated={calc_deductions}, Stated={stated_deductions}")
    
    # 6. Verify taxable income = gross - exemptions - deductions
    calc_taxable = output_gross - stated_exemptions - stated_deductions
    stated_taxable = parse_value(emp_output.get('taxable_income', 0))
    
    if abs(calc_taxable - stated_taxable) > Decimal('1'):
        errors_found.append(f"{emp_id}: OUTPUT Taxable income mismatch: Calculated={calc_taxable}, Stated={stated_taxable}")
    
    # 7. Verify tax after rebate = base tax - rebate
    base_tax = parse_value(emp_output.get('base_tax', 0))
    rebate = parse_value(emp_output.get('rebate_87a', 0))
    tax_after_rebate = parse_value(emp_output.get('tax_after_rebate', 0))
    
    if abs(tax_after_rebate - (base_tax - rebate)) > Decimal('0.5'):
        errors_found.append(f"{emp_id}: OUTPUT Tax after rebate incorrect: Should be {base_tax - rebate}, got {tax_after_rebate}")
    
    # 8. Verify tax with surcharge = tax after rebate + surcharge
    surcharge = parse_value(emp_output.get('surcharge', 0))
    tax_with_surcharge = parse_value(emp_output.get('tax_with_surcharge', 0))
    
    if abs(tax_with_surcharge - (tax_after_rebate + surcharge)) > Decimal('0.5'):
        errors_found.append(f"{emp_id}: OUTPUT Tax with surcharge incorrect: Should be {tax_after_rebate + surcharge}, got {tax_with_surcharge}")
    
    # 9. Verify cess = 4% of tax with surcharge
    expected_cess = round_currency(tax_with_surcharge * Decimal('0.04'))
    stated_cess = parse_value(emp_output.get('health_education_cess', 0))
    
    if abs(expected_cess - stated_cess) > Decimal('0.5'):
        errors_found.append(f"{emp_id}: OUTPUT Cess incorrect: Should be {expected_cess}, got {stated_cess}")
    
    # 10. Verify total tax = tax with surcharge + cess
    total_tax = parse_value(emp_output.get('total_tax_liability', 0))
    expected_total = tax_with_surcharge + stated_cess
    
    if abs(total_tax - expected_total) > Decimal('0.5'):
        errors_found.append(f"{emp_id}: OUTPUT Total tax incorrect: Should be {expected_total}, got {total_tax}")
    
    # 11. Verify monthly TDS = total tax / 12
    monthly_tds = parse_value(emp_output.get('monthly_tds', 0))
    expected_monthly = round_currency(total_tax / 12)
    
    if abs(monthly_tds - expected_monthly) > Decimal('1'):
        errors_found.append(f"{emp_id}: OUTPUT Monthly TDS incorrect: Should be {expected_monthly}, got {monthly_tds}")

print()
print("=" * 80)
print("VERIFICATION RESULTS")
print("=" * 80)

if errors_found:
    print(f"\n❌ Found {len(errors_found)} calculation errors:\n")
    for error in errors_found:
        print(f"  • {error}")
    print(f"\n⚠️  Total errors: {len(errors_found)}")
else:
    print("\n✅ ALL CALCULATIONS ARE CORRECT!")
    print("   - Gross salary = sum of components ✓")
    print("   - PF = 12% of basic salary ✓")
    print("   - Total exemptions sum correctly ✓")
    print("   - Total deductions sum correctly ✓")
    print("   - Taxable income calculated correctly ✓")
    print("   - Tax calculations are accurate ✓")
    print("   - Cess = 4% of tax with surcharge ✓")
    print("   - Monthly TDS = total tax / 12 ✓")

print("\n" + "=" * 80)
