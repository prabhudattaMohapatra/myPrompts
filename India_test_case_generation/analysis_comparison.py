#!/usr/bin/env python3
import csv
from typing import Dict, List

def calculate_new_regime_tax(taxable_income: float) -> float:
    """Calculate base tax for New Regime 2025-26"""
    if taxable_income <= 400000:
        return 0
    elif taxable_income <= 800000:
        return (taxable_income - 400000) * 0.05
    elif taxable_income <= 1200000:
        return 20000 + (taxable_income - 800000) * 0.10
    elif taxable_income <= 1600000:
        return 60000 + (taxable_income - 1200000) * 0.15
    elif taxable_income <= 2000000:
        return 120000 + (taxable_income - 1600000) * 0.20
    else:
        return 200000 + (taxable_income - 2000000) * 0.30

def calculate_old_regime_tax(taxable_income: float) -> float:
    """Calculate base tax for Old Regime"""
    if taxable_income <= 300000:
        return 0
    elif taxable_income <= 600000:
        return (taxable_income - 300000) * 0.05
    elif taxable_income <= 900000:
        return 15000 + (taxable_income - 600000) * 0.20
    elif taxable_income <= 1200000:
        return 75000 + (taxable_income - 900000) * 0.20
    elif taxable_income <= 1500000:
        return 135000 + (taxable_income - 1200000) * 0.30
    else:
        return 225000 + (taxable_income - 1500000) * 0.30

def read_csv_rows(filepath: str, limit: int = 6) -> List[Dict]:
    """Read CSV file and return rows as list of dicts"""
    rows = []
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if i >= limit:
                break
            rows.append(row)
    return rows

print("=" * 100)
print("CALCULATION ACCURACY ANALYSIS")
print("=" * 100)

# Analyze Output 185127
print("\n1. OUTPUT 185127 - Annual Tax Forecast Validation (First 5 Employees)")
print("-" * 100)

rows_185127 = read_csv_rows('output_with_dsl_20251119_185127/annual_tax_forecast.csv', 6)
errors_185127 = 0

for row in rows_185127:
    emp_id = row['employee_id']
    regime = row['tax_regime']
    taxable_income = float(row['taxable_income']) if row['taxable_income'] else 0
    reported_base_tax = float(row['base_tax']) if row['base_tax'] else 0
    
    # Calculate expected tax
    if regime == 'new':
        expected_base_tax = calculate_new_regime_tax(taxable_income)
    else:
        expected_base_tax = calculate_old_regime_tax(taxable_income)
    
    # Check accuracy
    diff = abs(expected_base_tax - reported_base_tax)
    is_accurate = diff < 100  # Allow small rounding differences
    
    if not is_accurate:
        errors_185127 += 1
        status = "✗ ERROR"
    else:
        status = "✓ OK"
    
    print(f"{status:10} | {emp_id:8} | {regime:5} | Taxable: ₹{taxable_income:13,.2f} | "
          f"Reported: ₹{reported_base_tax:10,.2f} | Expected: ₹{expected_base_tax:10,.2f} | "
          f"Diff: ₹{diff:8,.2f}")

print(f"\nErrors found in 185127: {errors_185127}/5")

# Analyze Output 192056
print("\n2. OUTPUT 192056 - Annual Tax Forecast Validation (First 5 Employees)")
print("-" * 100)

rows_192056 = read_csv_rows('output_with_dsl_20251119_192056/annual_tax_forecast.csv', 6)
errors_192056 = 0

for row in rows_192056:
    emp_id = row['ID']
    regime = row['tax_regime']
    taxable_income = float(row['taxable_income']) if row['taxable_income'] else 0
    reported_base_tax = float(row['base_tax_before_rebate']) if row['base_tax_before_rebate'] else 0
    
    # Calculate expected tax
    if regime == 'new':
        expected_base_tax = calculate_new_regime_tax(taxable_income)
    else:
        expected_base_tax = calculate_old_regime_tax(taxable_income)
    
    # Check accuracy
    diff = abs(expected_base_tax - reported_base_tax)
    is_accurate = diff < 100
    
    if not is_accurate:
        errors_192056 += 1
        status = "✗ ERROR"
    else:
        status = "✓ OK"
    
    print(f"{status:10} | {emp_id:8} | {regime:5} | Taxable: ₹{taxable_income:13,.2f} | "
          f"Reported: ₹{reported_base_tax:10,.2f} | Expected: ₹{expected_base_tax:10,.2f} | "
          f"Diff: ₹{diff:8,.2f}")

print(f"\nErrors found in 192056: {errors_192056}/5")

print("\n" + "=" * 100)
print("SUMMARY")
print("=" * 100)
print(f"Output 185127: {errors_185127}/5 calculation errors")
print(f"Output 192056: {errors_192056}/5 calculation errors")

if errors_185127 < errors_192056:
    print("\n✓ Output 185127 has BETTER accuracy")
elif errors_185127 > errors_192056:
    print("\n✓ Output 192056 has BETTER accuracy")
else:
    print("\n✓ Both outputs have EQUAL accuracy")

