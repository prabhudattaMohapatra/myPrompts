#!/usr/bin/env python3
"""
Comprehensive Analysis: Comparing two outputs from the Indian Payroll Test Case Generation prompt
Output 1: output_with_dsl_20251119_185127
Output 2: output_with_dsl_20251119_192056
"""

import csv
import os
from typing import Dict, List, Tuple
from collections import Counter

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

def read_csv_rows(filepath: str, limit: int = None) -> List[Dict]:
    """Read CSV file and return rows as list of dicts"""
    rows = []
    with open(filepath, 'r') as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if limit and i >= limit:
                break
            rows.append(row)
    return rows

def count_csv_rows(filepath: str) -> int:
    """Count rows in CSV file"""
    with open(filepath, 'r') as f:
        return sum(1 for line in f) - 1  # Subtract header

def analyze_accuracy(rows: List[Dict], emp_id_field: str, base_tax_field: str) -> Tuple[int, int, List[Dict]]:
    """Analyze tax calculation accuracy"""
    total = 0
    accurate = 0
    errors = []
    
    for row in rows:
        if not row.get('taxable_income'):
            continue
            
        emp_id = row[emp_id_field]
        regime = row['tax_regime']
        taxable_income = float(row['taxable_income']) if row['taxable_income'] else 0
        reported_base_tax = float(row[base_tax_field]) if row[base_tax_field] else 0
        
        # Calculate expected tax
        if regime == 'new':
            expected_base_tax = calculate_new_regime_tax(taxable_income)
        else:
            expected_base_tax = calculate_old_regime_tax(taxable_income)
        
        total += 1
        diff = abs(expected_base_tax - reported_base_tax)
        
        if diff < 100:  # Allow small rounding differences
            accurate += 1
        else:
            errors.append({
                'emp_id': emp_id,
                'regime': regime,
                'taxable_income': taxable_income,
                'reported': reported_base_tax,
                'expected': expected_base_tax,
                'diff': diff
            })
    
    return total, accurate, errors

def analyze_coverage(summary_rows: List[Dict]) -> Dict:
    """Analyze test case coverage"""
    coverage = {
        'total_test_cases': len(summary_rows),
        'tax_regimes': Counter(),
        'features': [],
        'rules_applied': set()
    }
    
    for row in summary_rows:
        regime = row.get('tax_regime') or row.get('Tax Regime')
        if regime:
            coverage['tax_regimes'][regime] += 1
        
        features = row.get('key_features') or row.get('Key Features')
        if features:
            coverage['features'].append(features)
        
        rules = row.get('rules_applied') or row.get('Rules Applied')
        if rules:
            for rule in rules.split('|'):
                coverage['rules_applied'].add(rule.strip())
    
    return coverage

def analyze_completeness(dir_path: str) -> Dict:
    """Analyze data completeness"""
    required_files = [
        'annual_employee_input_data.csv',
        'annual_tax_forecast.csv',
        'monthly_payslip_april.csv',
        'monthly_payslip_december.csv',
        'monthly_payslip_march.csv',
        'monthly_bonus_commission_april.csv',
        'monthly_bonus_commission_december.csv',
        'monthly_bonus_commission_march.csv',
        'ctc_revision_december.csv',
        'tax_regime_revision_december.csv',
        'test_cases_master_summary.csv'
    ]
    
    completeness = {
        'required_files': 0,
        'missing_files': [],
        'file_row_counts': {}
    }
    
    for file in required_files:
        file_path = os.path.join(dir_path, file)
        if os.path.exists(file_path):
            completeness['required_files'] += 1
            completeness['file_row_counts'][file] = count_csv_rows(file_path)
        else:
            completeness['missing_files'].append(file)
    
    return completeness

print("=" * 120)
print("COMPREHENSIVE ANALYSIS: Indian Payroll Test Case Generation Outputs")
print("=" * 120)

# Paths
output1 = 'output_with_dsl_20251119_185127'
output2 = 'output_with_dsl_20251119_192056'

# 1. COMPLETENESS ANALYSIS
print("\n1. DATA COMPLETENESS")
print("-" * 120)

comp1 = analyze_completeness(output1)
comp2 = analyze_completeness(output2)

print(f"\nOutput 185127:")
print(f"  Required files present: {comp1['required_files']}/11")
print(f"  Missing files: {comp1['missing_files'] if comp1['missing_files'] else 'None'}")
print(f"  Total employees (annual): {comp1['file_row_counts'].get('annual_employee_input_data.csv', 'N/A')}")
print(f"  Test cases: {comp1['file_row_counts'].get('test_cases_master_summary.csv', 'N/A')}")

print(f"\nOutput 192056:")
print(f"  Required files present: {comp2['required_files']}/11")
print(f"  Missing files: {comp2['missing_files'] if comp2['missing_files'] else 'None'}")
print(f"  Total employees (annual): {comp2['file_row_counts'].get('annual_employee_input_data.csv', 'N/A')}")
print(f"  Test cases: {comp2['file_row_counts'].get('test_cases_master_summary.csv', 'N/A')}")

# 2. CALCULATION ACCURACY ANALYSIS
print("\n2. CALCULATION ACCURACY (All Records)")
print("-" * 120)

# Analyze Output 1
rows1 = read_csv_rows(f'{output1}/annual_tax_forecast.csv')
total1, accurate1, errors1 = analyze_accuracy(rows1, 'employee_id', 'base_tax')

print(f"\nOutput 185127:")
print(f"  Total records analyzed: {total1}")
print(f"  Accurate calculations: {accurate1} ({accurate1/total1*100:.1f}%)")
print(f"  Calculation errors: {len(errors1)} ({len(errors1)/total1*100:.1f}%)")

if errors1[:3]:
    print(f"  Sample errors:")
    for err in errors1[:3]:
        print(f"    - {err['emp_id']}: Expected ₹{err['expected']:,.0f}, Got ₹{err['reported']:,.0f}, Diff ₹{err['diff']:,.0f}")

# Analyze Output 2
rows2 = read_csv_rows(f'{output2}/annual_tax_forecast.csv')
total2, accurate2, errors2 = analyze_accuracy(rows2, 'ID', 'base_tax_before_rebate')

print(f"\nOutput 192056:")
print(f"  Total records analyzed: {total2}")
print(f"  Accurate calculations: {accurate2} ({accurate2/total2*100:.1f}%)")
print(f"  Calculation errors: {len(errors2)} ({len(errors2)/total2*100:.1f}%)")

if errors2[:3]:
    print(f"  Sample errors:")
    for err in errors2[:3]:
        print(f"    - {err['emp_id']}: Expected ₹{err['expected']:,.0f}, Got ₹{err['reported']:,.0f}, Diff ₹{err['diff']:,.0f}")

# 3. TEST CASE COVERAGE ANALYSIS
print("\n3. TEST CASE COVERAGE")
print("-" * 120)

summary1 = read_csv_rows(f'{output1}/test_cases_master_summary.csv')
coverage1 = analyze_coverage(summary1)

summary2 = read_csv_rows(f'{output2}/test_cases_master_summary.csv')
coverage2 = analyze_coverage(summary2)

print(f"\nOutput 185127:")
print(f"  Total test cases: {coverage1['total_test_cases']}")
print(f"  Tax regime distribution: {dict(coverage1['tax_regimes'])}")
print(f"  Unique rules covered: {len(coverage1['rules_applied'])}")
print(f"  Sample rules: {list(coverage1['rules_applied'])[:5]}")

print(f"\nOutput 192056:")
print(f"  Total test cases: {coverage2['total_test_cases']}")
print(f"  Tax regime distribution: {dict(coverage2['tax_regimes'])}")
print(f"  Unique rules covered: {len(coverage2['rules_applied'])}")
print(f"  Sample rules: {list(coverage2['rules_applied'])[:5]}")

# 4. DATA RICHNESS ANALYSIS
print("\n4. DATA RICHNESS & DIVERSITY")
print("-" * 120)

input1 = read_csv_rows(f'{output1}/annual_employee_input_data.csv')
input2 = read_csv_rows(f'{output2}/annual_employee_input_data.csv')

# Count non-zero/non-empty fields
def count_populated_fields(rows: List[Dict]) -> Dict:
    field_counts = {}
    for row in rows:
        for key, value in row.items():
            if value and value not in ['0', '0.0', '', 'false', 'False', 'none', 'None']:
                field_counts[key] = field_counts.get(key, 0) + 1
    return field_counts

fields1 = count_populated_fields(input1)
fields2 = count_populated_fields(input2)

print(f"\nOutput 185127:")
print(f"  Total fields in schema: {len(input1[0].keys()) if input1 else 0}")
print(f"  Fields with data: {len([k for k, v in fields1.items() if v > 0])}")
print(f"  Average populated fields per employee: {sum(fields1.values()) / len(input1) if input1 else 0:.1f}")

print(f"\nOutput 192056:")
print(f"  Total fields in schema: {len(input2[0].keys()) if input2 else 0}")
print(f"  Fields with data: {len([k for k, v in fields2.items() if v > 0])}")
print(f"  Average populated fields per employee: {sum(fields2.values()) / len(input2) if input2 else 0:.1f}")

# 5. FINAL VERDICT
print("\n" + "=" * 120)
print("FINAL VERDICT")
print("=" * 120)

score1 = 0
score2 = 0

print("\nScoring Criteria:")

# Criterion 1: Calculation Accuracy
accuracy_pct1 = (accurate1 / total1 * 100) if total1 > 0 else 0
accuracy_pct2 = (accurate2 / total2 * 100) if total2 > 0 else 0
print(f"\n1. Calculation Accuracy:")
print(f"   Output 185127: {accuracy_pct1:.1f}% accurate")
print(f"   Output 192056: {accuracy_pct2:.1f}% accurate")
if accuracy_pct1 > accuracy_pct2:
    score1 += 3
    print(f"   Winner: 185127 (+3 points)")
elif accuracy_pct2 > accuracy_pct1:
    score2 += 3
    print(f"   Winner: 192056 (+3 points)")
else:
    print(f"   Tie (0 points each)")

# Criterion 2: Test Case Coverage
print(f"\n2. Test Case Coverage:")
print(f"   Output 185127: {coverage1['total_test_cases']} test cases, {len(coverage1['rules_applied'])} rules")
print(f"   Output 192056: {coverage2['total_test_cases']} test cases, {len(coverage2['rules_applied'])} rules")
if coverage2['total_test_cases'] > coverage1['total_test_cases']:
    score2 += 2
    print(f"   Winner: 192056 (+2 points for more test cases)")
elif coverage1['total_test_cases'] > coverage2['total_test_cases']:
    score1 += 2
    print(f"   Winner: 185127 (+2 points for more test cases)")

if len(coverage2['rules_applied']) > len(coverage1['rules_applied']):
    score2 += 2
    print(f"   Winner: 192056 (+2 points for more rules)")
elif len(coverage1['rules_applied']) > len(coverage2['rules_applied']):
    score1 += 2
    print(f"   Winner: 185127 (+2 points for more rules)")

# Criterion 3: Completeness
print(f"\n3. Data Completeness:")
print(f"   Output 185127: {comp1['required_files']}/11 files, {comp1['file_row_counts'].get('annual_employee_input_data.csv', 0)} employees")
print(f"   Output 192056: {comp2['required_files']}/11 files, {comp2['file_row_counts'].get('annual_employee_input_data.csv', 0)} employees")
if comp1['required_files'] > comp2['required_files']:
    score1 += 1
    print(f"   Winner: 185127 (+1 point)")
elif comp2['required_files'] > comp1['required_files']:
    score2 += 1
    print(f"   Winner: 192056 (+1 point)")

# Criterion 4: Data Richness
avg_fields1 = sum(fields1.values()) / len(input1) if input1 else 0
avg_fields2 = sum(fields2.values()) / len(input2) if input2 else 0
print(f"\n4. Data Richness:")
print(f"   Output 185127: {avg_fields1:.1f} avg populated fields per employee")
print(f"   Output 192056: {avg_fields2:.1f} avg populated fields per employee")
if avg_fields1 > avg_fields2:
    score1 += 1
    print(f"   Winner: 185127 (+1 point)")
elif avg_fields2 > avg_fields1:
    score2 += 1
    print(f"   Winner: 192056 (+1 point)")

print(f"\n" + "=" * 120)
print(f"FINAL SCORES:")
print(f"  Output 185127: {score1} points")
print(f"  Output 192056: {score2} points")
print("=" * 120)

if score1 > score2:
    print(f"\n🏆 WINNER: Output 185127 (output_with_dsl_20251119_185127)")
    print(f"   Better performance in: {'Accuracy, ' if accuracy_pct1 > accuracy_pct2 else ''}{'Coverage, ' if coverage1['total_test_cases'] > coverage2['total_test_cases'] else ''}{'Completeness, ' if comp1['required_files'] > comp2['required_files'] else ''}{'Richness' if avg_fields1 > avg_fields2 else ''}")
elif score2 > score1:
    print(f"\n🏆 WINNER: Output 192056 (output_with_dsl_20251119_192056)")
    print(f"   Better performance in: {'Accuracy, ' if accuracy_pct2 > accuracy_pct1 else ''}{'Coverage, ' if coverage2['total_test_cases'] > coverage1['total_test_cases'] else ''}{'Completeness, ' if comp2['required_files'] > comp1['required_files'] else ''}{'Richness' if avg_fields2 > avg_fields1 else ''}")
else:
    print(f"\n🤝 TIE: Both outputs are equally good overall")

print("\n" + "=" * 120)

