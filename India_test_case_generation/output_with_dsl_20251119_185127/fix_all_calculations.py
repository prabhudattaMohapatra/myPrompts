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

def calculate_new_regime_tax(taxable_income):
    """Calculate tax based on new regime slabs"""
    taxable = taxable_income
    tax = Decimal('0')
    
    if taxable <= 300000:
        tax = Decimal('0')
    elif taxable <= 700000:
        tax = (taxable - 300000) * Decimal('0.05')
    elif taxable <= 1000000:
        tax = 20000 + (taxable - 700000) * Decimal('0.10')
    elif taxable <= 1200000:
        tax = 50000 + (taxable - 1000000) * Decimal('0.15')
    elif taxable <= 1500000:
        tax = 80000 + (taxable - 1200000) * Decimal('0.20')
    else:
        tax = 140000 + (taxable - 1500000) * Decimal('0.30')
    
    return tax

def calculate_old_regime_tax(taxable_income):
    """Calculate tax based on old regime slabs"""
    taxable = taxable_income
    tax = Decimal('0')
    
    if taxable <= 250000:
        tax = Decimal('0')
    elif taxable <= 500000:
        tax = (taxable - 250000) * Decimal('0.05')
    elif taxable <= 1000000:
        tax = 12500 + (taxable - 500000) * Decimal('0.20')
    else:
        tax = 112500 + (taxable - 1000000) * Decimal('0.30')
    
    return tax

print("=" * 80)
print("FIXING ALL CALCULATION ISSUES")
print("=" * 80)
print()

# Step 1: Fix INPUT file - correct gross salary
print("STEP 1: Fixing gross salary in input file...")
print("-" * 80)

input_data = []
with open('annual_employee_input_data.csv', 'r') as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)  # Convert to list
    for row in reader:
        # Calculate correct gross salary as sum of all components
        basic_salary = parse_value(row.get('basic_salary', 0))
        hra_received = parse_value(row.get('hra_received', 0))
        special_allowance = parse_value(row.get('special_allowance', 0))
        transport_allowance = parse_value(row.get('transport_allowance', 0))
        conveyance_allowance = parse_value(row.get('conveyance_allowance', 0))
        meal_vouchers = parse_value(row.get('meal_vouchers', 0))
        lta_received = parse_value(row.get('lta_received', 0))
        children_education_allowance = parse_value(row.get('children_education_allowance', 0))
        children_hostel_allowance = parse_value(row.get('children_hostel_allowance', 0))
        books_and_periodical_allowance = parse_value(row.get('books_and_periodical_allowance', 0))
        telephone_reimbursement = parse_value(row.get('telephone_reimbursement', 0))
        bonus = parse_value(row.get('bonus', 0))
        commission = parse_value(row.get('commission', 0))
        
        correct_gross = (basic_salary + hra_received + special_allowance + transport_allowance + 
                        conveyance_allowance + meal_vouchers + lta_received + 
                        children_education_allowance + children_hostel_allowance + 
                        books_and_periodical_allowance + telephone_reimbursement +
                        bonus + commission)
        
        old_gross = parse_value(row.get('gross_salary', 0))
        if abs(old_gross - correct_gross) > Decimal('1'):
            print(f"{row['employee_id']}: Corrected gross salary from ₹{old_gross:,.2f} to ₹{correct_gross:,.2f}")
        
        row['gross_salary'] = str(float(correct_gross))
        row['annual_ctc'] = str(float(correct_gross))
        input_data.append(row)

# Write corrected input file
with open('annual_employee_input_data_CORRECTED.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(input_data)

print(f"\n✓ Corrected input file saved as annual_employee_input_data_CORRECTED.csv")

# Step 2: Fix OUTPUT file - correct total deductions and recalculate taxes
print("\n" + "=" * 80)
print("STEP 2: Fixing total deductions and recalculating taxes in output file...")
print("-" * 80)

output_data = []
with open('annual_tax_forecast.csv', 'r') as f:
    reader = csv.DictReader(f)
    fieldnames = list(reader.fieldnames)  # Convert to list
    
    for row in reader:
        emp_id = row['employee_id']
        
        # Get the corrected gross salary from input
        input_emp = next((emp for emp in input_data if emp['employee_id'] == emp_id), None)
        if input_emp:
            corrected_gross = parse_value(input_emp['gross_salary'])
            row['gross_salary'] = str(float(corrected_gross))
            row['gross_income'] = str(float(corrected_gross))
        
        # Recalculate total deductions (80CCD1 is part of 80C, not separate)
        standard_deduction = parse_value(row.get('standard_deduction', 0))
        professional_tax = parse_value(row.get('professional_tax_deduction', 0))
        c80 = parse_value(row.get('80c_deduction', 0))
        # 80CCD1 is already included in 80C, so don't add separately
        ccd2 = parse_value(row.get('80ccd2_deduction', 0))
        ccd1b = parse_value(row.get('80ccd1b_deduction', 0))
        d80 = parse_value(row.get('80d_total_deduction', 0))
        dd80 = parse_value(row.get('80dd_deduction', 0))
        u80 = parse_value(row.get('80u_deduction', 0))
        g80 = parse_value(row.get('80g_deduction', 0))
        tta = parse_value(row.get('80tta_deduction', 0))
        ttb = parse_value(row.get('80ttb_deduction', 0))
        b24 = parse_value(row.get('24b_deduction', 0))
        eea = parse_value(row.get('80eea_deduction', 0))
        eeb = parse_value(row.get('80eeb_deduction', 0))
        ddb = parse_value(row.get('80ddb_deduction', 0))
        family_pension = parse_value(row.get('family_pension_deduction', 0))
        
        # Correct total deductions (80CCD1 is part of 80C)
        correct_total_deductions = (standard_deduction + professional_tax + c80 + 
                                   ccd2 + ccd1b + d80 + dd80 + u80 + g80 + 
                                   tta + ttb + b24 + eea + eeb + ddb + family_pension)
        
        old_total_deductions = parse_value(row.get('total_deductions', 0))
        if abs(old_total_deductions - correct_total_deductions) > Decimal('1'):
            print(f"{emp_id}: Corrected total deductions from ₹{old_total_deductions:,.2f} to ₹{correct_total_deductions:,.2f}")
        
        row['total_deductions'] = str(float(correct_total_deductions))
        
        # Recalculate taxable income
        gross_income = parse_value(row['gross_income'])
        total_exemptions = parse_value(row.get('total_exemptions', 0))
        income_after_exemptions = gross_income - total_exemptions
        row['income_after_exemptions'] = str(float(income_after_exemptions))
        
        taxable_income = gross_income - total_exemptions - correct_total_deductions
        old_taxable = parse_value(row.get('taxable_income', 0))
        if abs(old_taxable - taxable_income) > Decimal('1'):
            print(f"{emp_id}: Corrected taxable income from ₹{old_taxable:,.2f} to ₹{taxable_income:,.2f}")
        
        row['taxable_income'] = str(float(taxable_income))
        
        # Recalculate base tax
        tax_regime = row['tax_regime']
        if tax_regime == 'new':
            base_tax = calculate_new_regime_tax(taxable_income)
        else:
            base_tax = calculate_old_regime_tax(taxable_income)
        
        base_tax = round_currency(base_tax)
        old_base_tax = parse_value(row.get('base_tax', 0))
        if abs(old_base_tax - base_tax) > Decimal('1'):
            print(f"{emp_id}: Corrected base tax from ₹{old_base_tax:,.2f} to ₹{base_tax:,.2f}")
        
        row['base_tax'] = str(float(base_tax))
        
        # Recalculate rebate
        rebate = Decimal('0')
        if tax_regime == 'new' and taxable_income <= 700000 and taxable_income > 0:
            rebate = min(base_tax, Decimal('25000'))
        elif tax_regime == 'old' and taxable_income <= 500000 and taxable_income > 0:
            rebate = min(base_tax, Decimal('12500'))
        
        row['rebate_87a'] = str(float(rebate))
        
        # Tax after rebate
        tax_after_rebate = base_tax - rebate
        row['tax_after_rebate'] = str(float(tax_after_rebate))
        
        # Recalculate surcharge
        surcharge = Decimal('0')
        if taxable_income > 5000000:
            if taxable_income <= 10000000:
                surcharge = round_currency(tax_after_rebate * Decimal('0.10'))
            elif taxable_income <= 20000000:
                surcharge = round_currency(tax_after_rebate * Decimal('0.15'))
            elif taxable_income <= 50000000:
                surcharge = round_currency(tax_after_rebate * Decimal('0.25'))
            else:
                surcharge = round_currency(tax_after_rebate * Decimal('0.37'))
        
        row['surcharge'] = str(float(surcharge))
        
        # Tax with surcharge
        tax_with_surcharge = tax_after_rebate + surcharge
        row['tax_with_surcharge'] = str(float(tax_with_surcharge))
        
        # Health and education cess
        cess = round_currency(tax_with_surcharge * Decimal('0.04'))
        row['health_education_cess'] = str(float(cess))
        
        # Total tax liability
        total_tax = tax_with_surcharge + cess
        row['total_tax_liability'] = str(float(total_tax))
        
        # Monthly TDS
        monthly_tds = round_currency(total_tax / 12)
        row['monthly_tds'] = str(float(monthly_tds))
        
        # Net salary (approximation: gross - total tax)
        net_salary = gross_income - total_tax
        row['net_salary'] = str(float(net_salary))
        
        output_data.append(row)

# Write corrected output file
with open('annual_tax_forecast_CORRECTED.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
    writer.writeheader()
    writer.writerows(output_data)

print(f"\n✓ Corrected output file saved as annual_tax_forecast_CORRECTED.csv")

print("\n" + "=" * 80)
print("✅ ALL CORRECTIONS COMPLETED!")
print("=" * 80)
print("\nFiles created:")
print("1. annual_employee_input_data_CORRECTED.csv")
print("2. annual_tax_forecast_CORRECTED.csv")
print("\nNext steps:")
print("1. Review the corrected files")
print("2. Replace original files with corrected versions if satisfied")
print("3. Regenerate monthly payslip files with corrected calculations")
print("=" * 80)
