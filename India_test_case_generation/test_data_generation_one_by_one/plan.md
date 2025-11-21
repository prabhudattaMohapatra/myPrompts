# Test Data Generation Plan for 30 Employees

## Overview

Generate comprehensive test case data for Indian Payroll Engine (Assessment Year 2026-27) following the iterative one-by-one employee generation workflow. Each employee will have complete input/output data with full tax calculations and verification.

**Note**: Originally planned for 30 employees, expanded to 32, reduced to 28, expanded to 29 with EMP015, and now 30 with EMP023 added.

## Phase 1: Initial Setup

### 1.1 Read Input Files

- Read `employee_dsl.yaml` from parent directory (`India_test_case_generation/`) to understand complete data schema
- Read `mr_dsl.yaml` from parent directory to understand tax rules, slabs, deductions, exemptions
- Read `Data_requirements.md` to understand dataset requirements (30 employees, input/output requirements)
- Read `Use_Cases.md` to extract all 38 test cases (TC-01 through TC-38)

### 1.2 Create Output Directory

- Create directory: `output_with_dsl_{timestamp}` in parent directory where timestamp = `YYYYMMDD_HHMMSS`
- All generated files will be placed in this directory

### 1.3 Create Test Case Mapping

- Map 30 employees (EMP001-EMP030) to test cases from Use_Cases.md
- Ensure all 38 test cases are covered by at least one employee
- Create `test_case_mapping.md` documenting which employees cover which test cases
- Prioritize bold test cases (TC-01, TC-02, TC-04, TC-05, TC-06, TC-08, TC-09) for early employees

### 1.4 Create Empty Master CSV Files with Headers

Create the following CSV files with header rows only:

- `annual_employee_input_data_april_2025.csv` - All annual input fields from schema **(68 fields)**
- `monthly_bonus_commission_april.csv` - ID, bonus, commission, performance_bonus, month, year **(6 fields)**
- `monthly_bonus_commission_december.csv` - Same as April **(6 fields)**
- `monthly_bonus_commission_march.csv` - Same as April **(6 fields)**
- `ctc_revision_december.csv` - ID, previous_annual_ctc, revised_annual_ctc, previous_basic_salary, revised_basic_salary, previous_gross_salary, revised_gross_salary, revision_date, revision_month, revision_year **(10 fields)**
- `tax_regime_revision_december.csv` - ID, previous_tax_regime, new_tax_regime, revision_date, revision_month, revision_year, impact_on_tax_liability **(7 fields)**
- `investment_declaration_revision_february.csv` - ID, revision_date, section_80c_investments, self_family_premium, parents_premium, home_loan_interest, income_or_loss_from_house_property, charitable_donations, nps_employee_contribution, nps_additional_contribution **(10 fields)** (NEW - for mid-year investment changes)
- `annual_tax_forecast_april_2025.csv` - All annual output fields (exemptions, deductions, tax calculations) **(50 fields)**
- `monthly_payslip_april.csv` - All monthly output fields for April 2025 **(48 fields)**
- `monthly_payslip_december.csv` - All monthly output fields for December 2025 **(48 fields)**
- `monthly_payslip_march.csv` - All monthly output fields for March 2026 **(48 fields)**
- `test_cases_master_summary.csv` - test_id, employee_id, employee_name, age, tax_regime, city, gross_income, taxable_income, tax_breakdown, final_tax, key_features, rules_applied, status **(13 fields)**

**Note**: The `investment_declaration_revision_february.csv` file is used for employees who update their investment declarations mid-year (February). This demonstrates the operational scenario where employees can revise their tax-saving investments before the financial year ends, requiring TDS recalculation for remaining months.

## Phase 2: Iterative Employee Generation (EMP001-EMP032, excluding EMP022, EMP024)

For each employee, follow this 7-step workflow:

### Step 2: Generate Annual Input Data

- Generate employee ID (EMP001, EMP002, etc.)
- Generate demographic data (age, parent_age, number_of_children, residency, city, city_type)
- Generate annual CTC breakdown (basic_salary, hra_received, special_allowance, transport_allowance, conveyance_allowance, meal_allowance, LTA, etc.)
- Generate tax information (tax_regime, employment_type, joining_date)
- Generate investment declarations (section_80c_investments, self_family_premium, parents_health_insurance_premium)
- Ensure data satisfies assigned test case requirements
- Ensure compliance with Indian tax laws and mr_dsl.yaml rules

**CRITICAL: Annual CTC Breakdown Prepared in April**

The annual input data represents the CTC breakdown prepared at the **start of the financial year (April 2025)**. Therefore:

**DO NOT include variable bonuses/commissions** that will be paid later in the year:
- `bonus` field = 0 (if it's a variable bonus paid in specific months later)
- `commission` field = 0 (if it's variable commission paid in specific months later)  
- `performance_bonus` field = 0 (if it's variable performance bonus paid in specific months later)

**DO include fixed bonuses/commissions** that are part of regular monthly salary structure:
- Fixed monthly bonus paid every month → Include total annual amount
- Regular commission structure paid monthly → Include total annual amount

**How to Distinguish:**
- **Fixed**: Paid every month as part of regular salary → Include in annual input (will be divided by 12 in monthly payslips)
- **Variable**: Paid only in specific months → Set to 0 in annual input, create entries in `monthly_bonus_commission_{month}.csv`

**Examples:**
- EMP002: ₹70K commission paid only in December → `commission = 0`, `annual_ctc = 1430000` (excluding variable commission)
- EMP004: ₹3L fixed bonus (monthly) + ₹2.45L variable commission (Apr/Dec/March) → `bonus = 300000`, `commission = 0`, `annual_ctc = 6754400`
- EMP007: ₹50K performance bonus only in April → `performance_bonus = 0`, `annual_ctc = 950000` (excluding variable bonus)
- EMP008: ₹5Cr bonus + ₹3Cr commission paid monthly → `bonus = 50000000`, `commission = 30000000` (all fixed)

**Key Principle**: 
- **Annual CTC in April** = Sum of ALL regular salary components that are known/committed at the start of the year
- **Variable bonuses paid later** are NOT part of the April CTC breakdown (they're uncertain/future events)
- **Annual Tax Forecast** (also prepared in April) includes projected variable bonuses because it's a forward-looking forecast/projection

### Step 3: Generate Monthly Input Data (If Required)

Generate only if:

- Test case requires bonus/commission for April, December, or March (at least 5 non-zero values total across all employees)
- Employee is one of 3 employees requiring CTC revision in December
- Employee is one of 2 employees requiring tax regime revision in December

### Step 4: Generate Annual Tax Forecast Output

Calculate and generate:

- Exemptions (HRA, conveyance, LTA) using formulas from mr_dsl.yaml
- Deductions (80C, 80D, 80G, 80CCD, etc.) with limit checks from mr_dsl.yaml
- Taxable income = Gross Income - Exemptions - Deductions - Standard Deduction
- Base tax using progressive tax slabs from mr_dsl.yaml (old/new regime, senior citizen if applicable)
- Rebate (Section 87A) if applicable per mr_dsl.yaml
- Surcharge based on income thresholds from mr_dsl.yaml
- Cess (4% of tax + surcharge) per mr_dsl.yaml
- Final tax liability and monthly TDS
- Net salary
- Include step-by-step calculation breakdown with rule ID references

### Step 5: Generate Monthly Output Data (If Required)

Generate payslip data for:

- April 2025
- December 2025
- March 2026

For each month, calculate:

- Monthly gross salary components
- Monthly exemptions and deductions
- Monthly taxable income
- Monthly tax calculations (base tax, rebate, surcharge, cess, TDS)
- Monthly net salary
- Ensure consistency with annual calculations

**CRITICAL: Handling Fixed vs Variable Bonuses/Commissions in Monthly Payslips**

**Model Overview:**
1. Annual tax forecast is prepared in April including ALL expected annual income (fixed + variable bonuses)
2. Monthly TDS = Annual Tax / 12 (remains constant throughout the year)
3. Variable bonuses appear in specific months but don't change the TDS

**Implementation for Monthly Payslips:**

**A. For Employees with ONLY Fixed Bonuses** (e.g., EMP008):
- Annual input: bonus/commission fields have total annual amounts
- Monthly bonus CSVs: No entries
- Monthly payslips: bonus_monthly = annual_bonus / 12, commission_monthly = annual_commission / 12
- All 3 months (April, Dec, March) have same values

**B. For Employees with Variable Bonuses** (e.g., EMP002, EMP004, EMP007):
- Annual input: bonus/commission fields have total annual amounts (for tax forecast)
- Monthly bonus CSVs: Entries for specific months when variable amounts are paid
- Monthly payslips:
  * **Months WITHOUT variable bonus**: 
    - gross_salary_monthly = sum of regular salary components (excluding variable bonus/commission)
    - bonus_monthly = 0, commission_monthly = 0
  * **Months WITH variable bonus**:
    - gross_salary_monthly = regular components + variable bonus/commission received
    - bonus_monthly / commission_monthly = actual amount from monthly_bonus_commission CSV
  * **TDS in ALL months**: Same value = annual_tax / 12 (does NOT change!)

**Example: EMP002**
- Annual CTC: ₹15,00,000
- Variable commission: ₹70,000 (paid in December only)
- Regular gross (excluding variable commission): ₹14,30,000
- Monthly regular gross: ₹14,30,000 / 12 = ₹119,166
- Annual tax (calculated in April including expected ₹70K commission): ₹93,756
- Monthly TDS: ₹93,756 / 12 = ₹7,813

Monthly Payslips:
```
April:   gross=₹119,166, commission=0,      TDS=₹7,813, net=₹104,653
December: gross=₹189,166, commission=70,000, TDS=₹7,813, net=₹174,653
March:   gross=₹119,166, commission=0,      TDS=₹7,813, net=₹104,653
```

**Steps to Generate**:
1. Calculate regular monthly gross = (annual_ctc - total_variable_bonuses) / 12
2. For each month:
   - Check if employee has entry in monthly_bonus_commission_{month}.csv
   - If YES: gross_monthly = regular_gross + variable_amount, bonus/commission_monthly = variable_amount
   - If NO: gross_monthly = regular_gross, bonus/commission_monthly = 0
3. TDS same for all months = annual_tax / 12

**SPECIAL CASE: Mid-Year Investment Declaration Changes (February)**

For employees who revise their investment declarations in February (e.g., EMP032):

1. **Initial Declaration (April)**:
   - Annual input data contains original declarations
   - Tax calculated based on April declarations
   - TDS deducted Apr-Jan: annual_tax / 12

2. **Revised Declaration (February)**:
   - Create entry in `investment_declaration_revision_february.csv`:
     - ID, section_80c_investments, self_family_premium, home_loan_interest, 
       income_or_loss_from_house_property, etc.
   - Recalculate annual tax with revised declarations
   - Revised TDS for Feb-Mar: (new_annual_tax - tds_paid_apr_jan) / 2

3. **Monthly Payslips**:
   - April-January: TDS based on original declarations
   - February-March: Revised TDS based on updated declarations
   - Ensure annual TDS = recalculated annual tax

**Example**: EMP032 increases 80C from ₹1L to ₹1.5L in February
- Apr-Jan TDS: ₹8,000/month (based on ₹1L 80C)
- Feb declaration update: 80C now ₹1.5L
- Recalculated tax: ₹85K (vs original ₹96K)
- TDS paid Apr-Jan: ₹80K
- Remaining: ₹5K for Feb-Mar
- Feb-Mar TDS: ₹2,500/month

### Step 6: Verify and Document

Create `employee_verification_{employee_id}.md` with:

- Employee information and assigned test cases
- Input data verification (completeness, consistency, types)
- Calculation verification (mathematical accuracy, rule compliance, step-by-step breakdown)
- Output data verification (logical consistency, annual-monthly consistency)
- Use case coverage verification
- Rule ID mapping (all applicable rules from mr_dsl.yaml)
- Compliance verification (Indian tax laws, DSL rules)
- **CSV Field Count Verification** (see section 6.1 below)
- Issues and resolutions

Only proceed to Step 7 if all verifications pass.

#### 6.1 CSV Field Count Verification (CRITICAL)

**MUST verify field counts BEFORE appending to master CSV files to prevent data corruption.**

For each CSV file, verify:

1. **Count header fields** in the master CSV file
2. **Count fields** in the employee data row you're about to append
3. **Verify they match exactly**

**Required Field Counts** (as of current schema):
- `annual_employee_input_data_april_2025.csv`: **68 fields**
- `annual_tax_forecast_april_2025.csv`: **50 fields**
- `monthly_payslip_april.csv`: **48 fields**
- `monthly_payslip_december.csv`: **48 fields**
- `monthly_payslip_march.csv`: **48 fields**
- `test_cases_master_summary.csv`: **13 fields**
- `monthly_bonus_commission_april.csv`: **6 fields**
- `monthly_bonus_commission_december.csv`: **6 fields**
- `monthly_bonus_commission_march.csv`: **6 fields**
- `ctc_revision_december.csv`: **10 fields**
- `tax_regime_revision_december.csv`: **7 fields**
- `investment_declaration_revision_february.csv`: **10 fields**

**Verification Script** (run before appending):

```python
import csv

# Check field count for each file
files_to_check = {
    'annual_employee_input_data.csv': 68,
    'annual_tax_forecast.csv': 50,
    'monthly_payslip_april.csv': 48,
    'monthly_payslip_december.csv': 48,
    'monthly_payslip_march.csv': 48,
}

for filename, expected_fields in files_to_check.items():
    with open(filename, 'r') as f:
        header_count = len(f.readline().strip().split(','))
        
    # Count fields in your employee data string
    employee_data = "EMP012,..." # Your data
    data_count = len(employee_data.split(','))
    
    if header_count != expected_fields:
        print(f"❌ {filename}: Header has {header_count} fields, expected {expected_fields}")
    elif data_count != expected_fields:
        print(f"❌ {filename}: Data has {data_count} fields, expected {expected_fields}")
    else:
        print(f"✅ {filename}: Correct ({expected_fields} fields)")
```

**Common Issues to Avoid**:
1. **Missing fields** - Ensure all fields from the schema are included, even if empty
2. **Extra fields** - Don't add fields that aren't in the header (e.g., children_education_allowance_monthly, children_hostel_allowance_monthly are NOT in monthly payslip schema)
3. **Field order mismatch** - Follow exact header order
4. **Delimiter issues** - Use only commas, no extra delimiters
5. **Newline issues** - Ensure proper line breaks between rows

**Monthly Payslip Schema Note**:
The monthly payslip CSVs do NOT have separate fields for:
- `children_education_allowance_monthly`
- `children_hostel_allowance_monthly`
- `books_and_periodical_allowance_monthly`
- `telephone_reimbursement_monthly`

These are included in the gross salary calculation but NOT as separate columns. Only include fields that exist in the header!

### Step 7: Append to Master CSV Files

Append verified employee data to:

- `annual_employee_input_data_april_2025.csv` - One row
- Monthly input CSVs (if applicable) - One row each
- `annual_tax_forecast_april_2025.csv` - One row
- Monthly output CSVs (if applicable) - One row each
- `test_cases_master_summary.csv` - One row per test case covered

### Step 8: Repeat for Next Employee

Continue until all 30 employees (EMP001-EMP032, excluding EMP022, EMP024) are generated.

## Phase 3: Final Quality Assurance

### 3.1 Verify CSV Completeness

- Annual Input CSV: Exactly 30 rows (EMP001-EMP032, excluding EMP022, EMP024)
- Monthly Input CSVs: Appropriate rows (5+ non-zero bonus/commission values, 1 CTC revision, 1 tax regime revision, 1 investment declaration revision)
- Annual Output CSV: Exactly 30 rows
- Monthly Output CSVs: Exactly 30 rows each
- Master Summary CSV: Entries for all test cases (31 test cases)

### 3.2 Verify Test Case Coverage

- All 33 test cases covered by at least one employee (TC-22, TC-25 excluded)
- Document any gaps

### 3.3 Create Final Summary Documents

- `test_case_rule_mapping.md` - Comprehensive mapping of test cases to rule IDs from mr_dsl.yaml
- `test_case_mapping.md` - Final mapping of employees to test cases
- `final_verification_summary.md` - Summary of all verification results across 30 employees
- `README.md` - Overview of generated data, file structure, and key statistics

### 3.4 Verify Data Consistency

- Employee IDs consistent across all files
- Data types match schema definitions
- All calculations mathematically accurate
- All data complies with Indian tax laws and mr_dsl.yaml rules

## Key Requirements

### Calculation Requirements

- All calculations must be mathematically accurate
- All calculations must comply with mr_dsl.yaml rules
- Reference rule IDs from mr_dsl.yaml for each calculation
- Include step-by-step calculation breakdowns
- Use assessment year 2026-27 for all calculations

### Compliance Requirements

- Use mr_dsl.yaml as minimum rule set
- Apply additional Indian Income Tax Act provisions not in DSL
- Ensure complete compliance with Indian tax laws
- Verify all limits, thresholds, and formulas

### Data Quality Requirements

- Use realistic Indian names, PAN numbers, addresses
- Ensure data consistency across months for same employee
- Verify all boundary conditions and edge cases
- Document all calculations and rule applications

## File Locations

- Input files: `/Users/pmohapatra/repos/payroll/prabhu_aws/myPrompts/India_test_case_generation/`
- Output directory: `/Users/pmohapatra/repos/payroll/prabhu_aws/myPrompts/India_test_case_generation/output_with_dsl_{timestamp}/`