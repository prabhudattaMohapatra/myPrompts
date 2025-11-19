#!/usr/bin/env python3
import csv

def read_csv_row(filepath: str, row_num: int = 0):
    """Read specific row from CSV"""
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if i == row_num:
                return row
    return None

# Investigate EMP001 from both outputs
print("=" * 100)
print("DETAILED CALCULATION INVESTIGATION - EMP001")
print("=" * 100)

print("\n185127 - EMP001 Annual Tax Forecast:")
row1 = read_csv_row('output_with_dsl_20251119_185127/annual_tax_forecast.csv', 0)
if row1:
    print(f"  Employee ID: {row1['employee_id']}")
    print(f"  Tax Regime: {row1['tax_regime']}")
    print(f"  Gross Salary: ₹{float(row1['gross_salary']):,.0f}")
    print(f"  Total Exemptions: ₹{float(row1['total_exemptions']):,.0f}")
    print(f"  Total Deductions: ₹{float(row1['total_deductions']):,.0f}")
    print(f"  Gross Income: ₹{float(row1['gross_income']):,.0f}")
    print(f"  Taxable Income: ₹{float(row1['taxable_income']):,.0f}")
    print(f"  Base Tax (Reported): ₹{float(row1['base_tax']):,.0f}")
    print(f"  Rebate 87A: ₹{float(row1['rebate_87a']):,.0f}")
    
    # Manual calculation for New Regime
    taxable = float(row1['taxable_income'])
    if taxable <= 400000:
        expected_tax = 0
    elif taxable <= 800000:
        expected_tax = (taxable - 400000) * 0.05
    else:
        print(f"\n  ERROR: Taxable income {taxable:,.0f} should have tax > 0")
    
    expected_tax = (492600 - 400000) * 0.05
    print(f"  Expected Base Tax: ₹{expected_tax:,.0f}")
    print(f"  Difference: ₹{float(row1['base_tax']) - expected_tax:,.0f}")

print("\n192056 - EMP001 Annual Tax Forecast:")
row2 = read_csv_row('output_with_dsl_20251119_192056/annual_tax_forecast.csv', 0)
if row2:
    print(f"  Employee ID: {row2['ID']}")
    print(f"  Tax Regime: {row2['tax_regime']}")
    print(f"  Gross Salary: ₹{float(row2['gross_salary']):,.0f}")
    print(f"  Total Exemptions: ₹{float(row2['total_tax_exemptions']):,.0f}")
    print(f"  Total Deductions: ₹{float(row2['total_deductions']):,.0f}")
    print(f"  Gross Income: ₹{float(row2['gross_income']):,.0f}")
    print(f"  Taxable Income: ₹{float(row2['taxable_income']):,.0f}")
    print(f"  Base Tax (Reported): ₹{float(row2['base_tax_before_rebate']):,.0f}")
    print(f"  Rebate 87A: ₹{float(row2['rebate_87a']):,.0f}")
    
    # Manual calculation
    taxable = float(row2['taxable_income'])
    expected_tax = (483400 - 400000) * 0.05
    print(f"  Expected Base Tax: ₹{expected_tax:,.0f}")
    print(f"  Difference: ₹{float(row2['base_tax_before_rebate']) - expected_tax:,.0f}")

# Check if the difference is professional tax related
print("\n" + "=" * 100)
print("HYPOTHESIS: The ₹5,000 difference might be related to:")
print("  1. Professional Tax (₹2,400 annually)")
print("  2. Some other systematic adjustment")
print("  3. Incorrect tax slab calculation")
print("\nBOTH outputs show the SAME ₹5,000 error pattern, suggesting a systematic issue")
print("in the calculation logic used to generate both datasets.")
print("=" * 100)

