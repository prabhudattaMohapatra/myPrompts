import csv
from decimal import Decimal, ROUND_HALF_UP

def parse_value(value):
    """Parse string value to Decimal, handling empty strings and booleans"""
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

def load_annual_data(filename):
    """Load annual employee data"""
    data = {}
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data[row['employee_id']] = row
    return data

def load_monthly_bonus(filename):
    """Load monthly bonus data"""
    data = {}
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data[row['employee_id']] = {
                'bonus': parse_value(row['bonus']),
                'commission': parse_value(row['commission']),
                'performance_bonus': parse_value(row['performance_bonus'])
            }
    return data

def load_ctc_revisions():
    """Load CTC revision data"""
    revisions = {}
    try:
        with open('ctc_revision_december.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                revisions[row['employee_id']] = {
                    'revised_gross_salary': parse_value(row['revised_gross_salary']),
                    'revised_basic_salary': parse_value(row['revised_basic_salary']),
                    'revised_hra_received': parse_value(row['revised_hra_received'])
                }
    except:
        pass
    return revisions

def generate_monthly_payslip(annual_data, input_data, bonus_data, month_name, ctc_revisions=None):
    """Generate monthly payslip data"""
    payslip_rows = []
    
    for emp_id, annual in annual_data.items():
        input_emp = input_data.get(emp_id, {})
        bonus_emp = bonus_data.get(emp_id, {'bonus': Decimal('0'), 'commission': Decimal('0'), 'performance_bonus': Decimal('0')})
        
        # Get base salary info
        gross_salary = parse_value(annual['gross_salary'])
        basic_salary = parse_value(annual['basic_salary'])
        tax_regime = annual['tax_regime']
        
        # Check for CTC revision (for December and March)
        if ctc_revisions and emp_id in ctc_revisions:
            revision = ctc_revisions[emp_id]
            gross_salary = revision['revised_gross_salary']
            basic_salary = revision['revised_basic_salary']
        
        # Calculate monthly salary
        monthly_gross = round_currency(gross_salary / 12)
        monthly_basic = round_currency(basic_salary / 12)
        
        # Add bonuses
        monthly_bonus = bonus_emp['bonus']
        monthly_commission = bonus_emp['commission']
        monthly_perf_bonus = bonus_emp['performance_bonus']
        
        # Total monthly gross with bonuses
        total_monthly_gross = monthly_gross + monthly_bonus + monthly_commission + monthly_perf_bonus
        
        # Calculate exemptions (monthly)
        hra_exemption_monthly = round_currency(parse_value(annual['hra_exemption']) / 12)
        conveyance_exemption_monthly = round_currency(parse_value(annual['conveyance_exemption']) / 12)
        lta_exemption_monthly = round_currency(parse_value(annual['lta_exemption']) / 12)
        transport_exemption_monthly = round_currency(parse_value(annual['transport_exemption']) / 12)
        meal_voucher_exemption_monthly = round_currency(parse_value(annual['meal_voucher_exemption']) / 12)
        
        total_exemptions_monthly = (hra_exemption_monthly + conveyance_exemption_monthly + 
                                    lta_exemption_monthly + transport_exemption_monthly + 
                                    meal_voucher_exemption_monthly)
        
        # Calculate deductions (monthly)
        standard_deduction_monthly = round_currency(parse_value(annual['standard_deduction']) / 12)
        professional_tax_monthly = round_currency(parse_value(annual['professional_tax_deduction']) / 12)
        
        c80_monthly = round_currency(parse_value(annual['80c_deduction']) / 12)
        ccd1_monthly = round_currency(parse_value(annual['80ccd1_deduction']) / 12)
        ccd2_monthly = round_currency(parse_value(annual['80ccd2_deduction']) / 12)
        ccd1b_monthly = round_currency(parse_value(annual['80ccd1b_deduction']) / 12)
        d80_monthly = round_currency(parse_value(annual['80d_total_deduction']) / 12)
        u80_monthly = round_currency(parse_value(annual['80u_deduction']) / 12)
        g80_monthly = round_currency(parse_value(annual['80g_deduction']) / 12)
        tta_monthly = round_currency(parse_value(annual['80tta_deduction']) / 12)
        ttb_monthly = round_currency(parse_value(annual['80ttb_deduction']) / 12)
        b24_monthly = round_currency(parse_value(annual['24b_deduction']) / 12)
        eea_monthly = round_currency(parse_value(annual['80eea_deduction']) / 12)
        
        total_deductions_monthly = (standard_deduction_monthly + professional_tax_monthly +
                                   c80_monthly + ccd1_monthly + ccd2_monthly + ccd1b_monthly +
                                   d80_monthly + u80_monthly + g80_monthly + tta_monthly + 
                                   ttb_monthly + b24_monthly + eea_monthly)
        
        # Calculate taxable income
        gross_income_monthly = total_monthly_gross
        taxable_income_monthly = gross_income_monthly - total_exemptions_monthly - total_deductions_monthly
        
        # Calculate tax based on regime
        if tax_regime == 'new':
            base_tax_monthly = calculate_new_regime_tax(taxable_income_monthly)
        else:
            base_tax_monthly = calculate_old_regime_tax(taxable_income_monthly)
        
        base_tax_monthly = round_currency(base_tax_monthly)
        
        # Check for rebate (Section 87A)
        rebate_monthly = Decimal('0')
        annual_taxable = taxable_income_monthly * 12  # Approximation
        if tax_regime == 'new' and annual_taxable <= 700000:
            rebate_monthly = min(base_tax_monthly, round_currency(Decimal('25000') / 12))
        elif tax_regime == 'old' and annual_taxable <= 500000:
            rebate_monthly = min(base_tax_monthly, round_currency(Decimal('12500') / 12))
        
        tax_after_rebate_monthly = base_tax_monthly - rebate_monthly
        
        # Calculate surcharge (if applicable)
        surcharge_monthly = Decimal('0')
        annual_taxable_approx = taxable_income_monthly * 12
        if annual_taxable_approx > 5000000:
            if annual_taxable_approx <= 10000000:
                surcharge_monthly = round_currency(tax_after_rebate_monthly * Decimal('0.10'))
            elif annual_taxable_approx <= 20000000:
                surcharge_monthly = round_currency(tax_after_rebate_monthly * Decimal('0.15'))
            elif annual_taxable_approx <= 50000000:
                surcharge_monthly = round_currency(tax_after_rebate_monthly * Decimal('0.25'))
            else:
                surcharge_monthly = round_currency(tax_after_rebate_monthly * Decimal('0.37'))
        
        tax_with_surcharge_monthly = tax_after_rebate_monthly + surcharge_monthly
        
        # Calculate health and education cess
        cess_monthly = round_currency(tax_with_surcharge_monthly * Decimal('0.04'))
        
        # Total TDS
        tds_monthly = tax_with_surcharge_monthly + cess_monthly
        
        # Net salary
        net_salary_monthly = total_monthly_gross - tds_monthly - professional_tax_monthly
        
        payslip_rows.append({
            'employee_id': emp_id,
            'tax_regime': tax_regime,
            'gross_salary_monthly': monthly_gross,
            'basic_salary_monthly': monthly_basic,
            'hra_exemption_monthly': hra_exemption_monthly,
            'conveyance_exemption_monthly': conveyance_exemption_monthly,
            'lta_exemption_monthly': lta_exemption_monthly,
            'transport_exemption_monthly': transport_exemption_monthly,
            'meal_voucher_exemption_monthly': meal_voucher_exemption_monthly,
            'total_exemptions_monthly': total_exemptions_monthly,
            'standard_deduction_monthly': standard_deduction_monthly,
            'professional_tax_deduction_monthly': professional_tax_monthly,
            '80c_deduction_monthly': c80_monthly,
            '80ccd1_deduction_monthly': ccd1_monthly,
            '80ccd2_deduction_monthly': ccd2_monthly,
            '80ccd1b_deduction_monthly': ccd1b_monthly,
            '80d_total_deduction_monthly': d80_monthly,
            '80u_deduction_monthly': u80_monthly,
            '80g_deduction_monthly': g80_monthly,
            '80tta_deduction_monthly': tta_monthly,
            '80ttb_deduction_monthly': ttb_monthly,
            '24b_deduction_monthly': b24_monthly,
            '80eea_deduction_monthly': eea_monthly,
            'total_deductions_monthly': total_deductions_monthly,
            'gross_income_monthly': gross_income_monthly,
            'taxable_income_monthly': taxable_income_monthly,
            'base_tax_monthly': base_tax_monthly,
            'rebate_monthly': rebate_monthly,
            'tax_after_rebate_monthly': tax_after_rebate_monthly,
            'surcharge_monthly': surcharge_monthly,
            'tax_with_surcharge_monthly': tax_with_surcharge_monthly,
            'health_education_cess_monthly': cess_monthly,
            'tds_monthly': tds_monthly,
            'net_salary_monthly': net_salary_monthly
        })
    
    return payslip_rows

def write_payslip_csv(filename, rows):
    """Write payslip data to CSV"""
    if not rows:
        return
    
    fieldnames = list(rows[0].keys())
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

# Main execution
print("Loading data files...")
annual_data = load_annual_data('annual_tax_forecast.csv')
input_data = load_annual_data('annual_employee_input_data.csv')
ctc_revisions = load_ctc_revisions()

print("\\nGenerating April payslips...")
april_bonus = load_monthly_bonus('monthly_bonus_commission_april.csv')
april_payslips = generate_monthly_payslip(annual_data, input_data, april_bonus, 'April')
write_payslip_csv('monthly_payslip_april_CORRECTED.csv', april_payslips)
print(f"✓ Generated monthly_payslip_april_CORRECTED.csv with {len(april_payslips)} employees")

print("\\nGenerating December payslips...")
december_bonus = load_monthly_bonus('monthly_bonus_commission_december.csv')
december_payslips = generate_monthly_payslip(annual_data, input_data, december_bonus, 'December', ctc_revisions)
write_payslip_csv('monthly_payslip_december_CORRECTED.csv', december_payslips)
print(f"✓ Generated monthly_payslip_december_CORRECTED.csv with {len(december_payslips)} employees")

print("\\nGenerating March payslips...")
march_bonus = load_monthly_bonus('monthly_bonus_commission_march.csv')
march_payslips = generate_monthly_payslip(annual_data, input_data, march_bonus, 'March', ctc_revisions)
write_payslip_csv('monthly_payslip_march_CORRECTED.csv', march_payslips)
print(f"✓ Generated monthly_payslip_march_CORRECTED.csv with {len(march_payslips)} employees")

print("\\n✅ All monthly payslip files have been regenerated with corrected calculations!")
