# Test Case Verification Prompt for Indian Payroll Engine (with DSL Rules)

## ROLE
You are an expert tax consultant and test engineer specializing in Indian tax law and payroll systems, with expertise in mathematical verification and tax rule compliance.

## TASK
Perform comprehensive verification of all generated test case data for the Indian Payroll Engine for assessment year 2026-27. **Verify calculations one by one for each employee** by:
1. **INDEPENDENTLY RECALCULATING** every value from scratch using input data
2. **SHOWING STEP-BY-STEP ARITHMETIC** with explicit numbers and operations  
3. **COMPARING** your calculated values with output CSV values
4. **DOCUMENTING** any discrepancies and explaining them
5. Validating rule coverage and generating detailed validation reports

**CRITICAL**: You must CALCULATE and VERIFY, not just compare values. Show your work!

## TARGET USERS
- Payroll administrators
- Tax professionals
- System developers
- Quality assurance teams

## PURPOSE
Validate the accuracy and compliance of all generated test case data by:
- Verifying mathematical accuracy of all calculations for each employee
- Validating rule coverage and compliance with mr_dsl.yaml rules
- Generating detailed validation reports for each employee
- Identifying any errors, inconsistencies, or compliance issues
- Ensuring all test cases meet quality standards

## Context

You will be provided with the following files. **Note**: If this prompt is in a subdirectory (e.g., `test_data_generation_one_by_one/`), the required files are located in the parent directory (`India_test_case_generation/`) or in output subdirectories:

- **employee_dsl.yaml**: Contains the complete input schema definition for employee data structure
- **mr_dsl.yaml**: Contains machine-readable DSL rules for Indian payroll and taxation - use this as the reference for rule compliance
- **Data_requirements.md**: Specifies the data requirements including number of employees, input/output requirements
- **Use_Cases.md**: Lists all test case scenarios that must be covered
- **Generated CSV files**: All master output CSV files containing employee data (typically in `output_with_dsl_{timestamp}/` subdirectories)
- **Verification files** (if any): Previous verification markdown files created during generation

## Workflow Overview

This verification prompt follows a **systematic one-by-one employee verification workflow**:

1. **Step 1**: Read all generated CSV files and understand the data structure
2. **Step 2**: For each employee (EMP001 through EMP030):
   - Extract employee data from all relevant CSV files
   - Verify mathematical accuracy of all calculations
   - Verify rule coverage and compliance with mr_dsl.yaml
   - Generate detailed validation report
3. **Step 3**: Create comprehensive summary reports
4. **Step 4**: Document all issues and provide recommendations

## Instructions

### Phase 1: Initial Setup (Step 1)

1. **Read and understand the schema**: Read the `employee_dsl.yaml` file to understand the complete data structure, field types, and relationships.

2. **Read and understand the tax rules DSL**: Read the `mr_dsl.yaml` file to understand all Indian payroll and taxation rules. Extract:
   - Tax slab definitions (old regime, new regime, senior citizens, super senior citizens)
   - Surcharge rules and thresholds
   - Cess calculations
   - Rebate rules (Section 87A)
   - Deduction limits and rules (Section 80C, 80D, 80G, etc.)
   - Exemption rules for allowances (HRA, conveyance, LTA, etc.)
   - Professional tax rules
   - All rule IDs and their conditions (when clauses) and actions (then clauses)

3. **Read requirements**: Read `Data_requirements.md` to understand:
   - Total number of employees expected (30)
   - Required input and output datasets
   - Optional datasets

4. **Read use cases**: Read `Use_Cases.md` to understand all test case scenarios that should be covered.

5. **Read generated CSV files**: Read all generated master CSV files:
   - `annual_employee_input_data.csv`
   - `monthly_bonus_commission_april.csv`
   - `monthly_bonus_commission_december.csv`
   - `monthly_bonus_commission_march.csv`
   - `ctc_revision_december.csv`
   - `tax_regime_revision_december.csv`
   - `annual_tax_forecast.csv`
   - `monthly_payslip_april.csv`
   - `monthly_payslip_december.csv`
   - `monthly_payslip_march.csv`
   - `test_cases_master_summary.csv`

6. **Create output directory**: Create a verification output directory named `verification_{timestamp}` where `{timestamp}` is the current timestamp in format `YYYYMMDD_HHMMSS` (e.g., `verification_20250115_143022`)

### Phase 2: One-by-One Employee Verification (Step 2)

For each employee (EMP001 through EMP030), perform comprehensive verification:

#### 2.1 Extract Employee Data

Extract all data for the current employee from all relevant CSV files:
- Annual input data from `annual_employee_input_data.csv`
- Monthly input data (if present) from monthly bonus/commission files, CTC revision, tax regime revision
- Annual output data from `annual_tax_forecast.csv`
- Monthly output data (if present) from monthly payslip files
- Test case mapping from `test_cases_master_summary.csv`

#### 2.1.5 Input File Content Validation

**CRITICAL FIRST STEP**: Before using input data for calculations, validate the contents and internal consistency of the input files themselves. This ensures data integrity before proceeding with tax calculations.

**A. Annual Input File (`annual_employee_input_data.csv`) Validation**:

For each employee, validate the following:

1. **Gross Salary Component Verification**:
   - **Calculate sum of components**: basic_salary + hra + special_allowance + transport_allowance + conveyance_allowance + meal_allowance + lta + other_allowances = ₹Calculated_Total
   - **Compare with gross_salary field**: 
     - Show: "Component Sum: ₹X, CSV gross_salary: ₹Y, Difference: ₹Z"
     - If difference > ₹1, flag as ERROR (rounding differences up to ₹1 are acceptable)
     - Document which components were included in the sum
   - **Verify all components are non-negative**: Check that no salary component has negative values (unless explicitly allowed by business rules)

2. **Employee PF Contribution Validation**:
   - **Calculate expected PF**: basic_salary × 0.12 = ₹Expected_PF
   - **Compare with employee_pf_contribution field**:
     - Show: "Expected (12% of basic ₹X): ₹Y, CSV shows: ₹Z, Difference: ₹W"
     - **Acceptable range**: Employee PF should be within 12% of basic (allow ±₹1 for rounding)
     - If employee_pf_contribution > basic_salary × 0.12, flag as ERROR
     - If employee_pf_contribution < 0, flag as ERROR
   - **Note**: Some employees may have opted out of PF or have different rates, but 12% is the standard - document any exceptions

3. **Employer PF Contribution Validation**:
   - **Calculate expected Employer PF**: basic_salary × 0.12 = ₹Expected_Employer_PF (or 0.13/0.14 in some states)
   - **Compare with employer_pf_contribution field**
   - **Verify**: Employer PF should typically equal or exceed employee PF (unless different rates apply)
   - Document any discrepancies

4. **Annual CTC Validation**:
   - **Calculate expected CTC**: gross_salary + employer_pf_contribution + employer_nps_contribution + employer_esi_contribution + other_employer_contributions = ₹Calculated_CTC
   - **Compare with annual_ctc field**:
     - Show: "Calculated CTC: ₹X, CSV annual_ctc: ₹Y, Difference: ₹Z"
     - Flag discrepancies > ₹100 as WARNING (minor differences may be due to rounding or other components)
   - **Verify**: CTC should be ≥ gross_salary (employer contributions add to CTC)

5. **Basic Salary Validation**:
   - **Verify**: basic_salary should be > 0
   - **Verify**: basic_salary should typically be 40-60% of gross_salary (document exceptions)
   - **Check**: basic_salary ≤ gross_salary

6. **HRA Validation**:
   - **Verify**: hra ≥ 0
   - **Verify**: If hra > 0, then rent_paid_per_month should be > 0 (or document exception)
   - **Verify**: If hra > 0, then city_type should be specified (metro/non-metro)

7. **Investment and Deduction Declarations Validation**:
   - **Section 80C**: Sum all 80C components (employee_pf, ppf, elss, life_insurance_premium, etc.)
     - Verify: Total 80C investments ≤ ₹150,000 (per mr_dsl.yaml)
     - Flag if total exceeds limit
   - **Section 80D**: 
     - Verify: self_family_health_insurance_premium ≤ ₹25,000 or ₹50,000 (based on age)
     - Verify: parents_health_insurance_premium ≤ ₹25,000 or ₹50,000 (based on parents' age)
   - **Section 80G**: Verify donation amounts are reasonable and within limits
   - **Home Loan Interest (24(b))**: 
     - Verify: home_loan_interest_paid ≤ home_loan_principal_paid (interest typically higher than principal in early years)
     - Verify: home_loan_interest_paid ≤ ₹200,000 (limit per mr_dsl.yaml)

8. **Tax Regime Validation**:
   - **Verify**: tax_regime is either "old" or "new" (case-insensitive)
   - **Verify**: If tax_regime is "old", then deductions should be present
   - **Verify**: If tax_regime is "new", then standard deduction should be ₹75,000 (not ₹50,000)

9. **Date and Format Validation**:
   - **Verify date formats**: All date fields (date_of_birth, date_of_joining, etc.) are in YYYY-MM-DD format
   - **Verify dates are valid**: Check that dates are not in the future (except for certain fields)
   - **Verify age calculation**: Calculate age from date_of_birth and verify it matches age field (if present)
   - **Verify**: date_of_joining should be before assessment year end

10. **Residence and Location Validation**:
    - **Verify**: residential_status is one of: "resident", "non_resident", "resident_but_not_ordinarily_resident"
    - **Verify**: If city_type is specified, it should be "metro" or "non_metro"
    - **Verify**: state should be a valid Indian state name

11. **Numeric Field Validation**:
    - **Verify**: All numeric fields are valid numbers (not text, not empty)
    - **Verify**: All amounts are non-negative (unless explicitly negative for losses)
    - **Verify**: Percentages are between 0 and 100 (where applicable)

12. **Cross-Field Consistency Checks**:
    - **Verify**: If employee has home_loan, then home_loan_principal_paid and home_loan_interest_paid should be > 0
    - **Verify**: If employee has nps_contribution, then employer_nps_contribution should typically be present
    - **Verify**: If employee is senior_citizen (age ≥ 60), tax slabs should reflect senior citizen rates
    - **Verify**: If employee is super_senior_citizen (age ≥ 80), tax slabs should reflect super senior citizen rates

**B. Monthly Input Files Validation**:

For each monthly input file (bonus/commission, CTC revision, tax regime revision), validate:

1. **Employee ID Consistency**:
   - Verify employee_id exists in annual input file
   - Verify employee_id format is consistent (EMP001, EMP002, etc.)

2. **Month Validation**:
   - Verify month field is valid (January, February, ..., December or 1-12)
   - Verify month matches the file name (e.g., `monthly_bonus_commission_december.csv` should have month = December)

3. **Amount Validation**:
   - **Bonus/Commission**: Verify amounts are non-negative
   - **CTC Revision**: Verify new_ctc > 0 and document the change from previous CTC
   - **Tax Regime Revision**: Verify new_regime is "old" or "new"

4. **Date Validation**:
   - Verify revision dates are within the assessment year (2026-27)
   - Verify dates are in YYYY-MM-DD format

**C. Input File Summary for Each Employee**:

After validating all input files for an employee, create a summary:
- **Total Issues Found**: Count of errors, warnings, and information items
- **Critical Errors**: List any errors that would prevent accurate tax calculation
- **Warnings**: List any inconsistencies that should be reviewed
- **Data Quality Score**: Overall assessment of input data quality for this employee

**Documentation Format**:
```
### Input File Validation for {employee_id}

#### Annual Input File Validation:
- ✅/❌ Gross Salary Components: Calculated ₹X, CSV shows ₹Y, Status: PASS/FAIL
- ✅/❌ Employee PF (12% of basic): Expected ₹X, CSV shows ₹Y, Status: PASS/FAIL
- ✅/❌ Annual CTC: Calculated ₹X, CSV shows ₹Y, Status: PASS/FAIL
- ✅/❌ Investment Declarations: All within limits / Issues found: [list]
- ✅/❌ Tax Regime: Valid / Invalid: [reason]
- ✅/❌ Date Formats: All valid / Issues: [list]
- ✅/❌ Cross-Field Consistency: All consistent / Issues: [list]

#### Monthly Input Files Validation:
- ✅/❌ Bonus/Commission Files: [status]
- ✅/❌ CTC Revision: [status]
- ✅/❌ Tax Regime Revision: [status]

#### Summary:
- Total Errors: X
- Total Warnings: Y
- Data Quality: Excellent/Good/Fair/Poor
- Ready for Tax Calculation: Yes/No (if No, explain why)
```

**IMPORTANT**: If critical errors are found in input files, document them clearly and proceed with calculations using the input data as-is, but flag that results may be inaccurate due to input data issues.

#### 2.2 Mathematical Accuracy Verification

**IMPORTANT**: For ALL calculations below, you MUST:
1. **Independently recalculate** the value from scratch using input data
2. **Show step-by-step arithmetic** with explicit numbers and operations
3. **Compare** your calculated value with the value in the output CSV
4. **Document any discrepancies** (even minor rounding differences)
5. **Explain** why values match or differ
6. **DO NOT** just state "Expected: X, Actual: X, PASS" without showing the calculation steps

Verify all calculations are mathematically correct:

**A. Input Data Verification**:
- **Gross Salary**: Add all salary components from input CSV
  - Example: basic (₹X) + HRA (₹Y) + special (₹Z) + ... = ₹Total
  - Compare with gross_salary field in input CSV
  - Document: "Calculated: ₹X, CSV shows: ₹Y, Difference: ₹Z"
- **Annual CTC**: Calculate gross_salary + employer_pf + employer_nps + other employer contributions
  - Show: ₹A + ₹B + ₹C = ₹Total
  - Compare with annual_ctc field
- Verify all input data is internally consistent
- Verify data types are correct (numbers, dates, booleans)
- Verify date formats are correct (YYYY-MM-DD)

**B. Exemption Calculations Verification**:
- **HRA Exemption** (MUST show all three components): 
  - **Component 1**: Actual HRA received = ₹X
  - **Component 2**: Rent paid - 10% of basic = ₹A - (₹B × 0.10) = ₹A - ₹C = ₹D
  - **Component 3**: 50% of basic (metro) OR 40% of basic (non-metro) = ₹B × 0.5/0.4 = ₹E
  - **Calculation**: min(₹X, ₹D, ₹E) = ₹F
  - **Compare**: Your calculation (₹F) vs CSV value (₹G)
  - **Identify limiting factor**: Which of the 3 components is the minimum?
  - Verify the formula matches mr_dsl.yaml rules
- **Conveyance Allowance Exemption**:
  - Calculate: min(conveyance_allowance_received, limit_from_dsl)
  - Show: min(₹X, ₹24,000) = ₹Y
  - Compare with CSV value
- **LTA Exemption**:
  - Calculate per mr_dsl.yaml rules (typically fully exempt if conditions met)
  - Show calculation and compare
- **Other Allowance Exemptions** (CEA, CHA, Meal, Books, etc.):
  - For each: Show input amount, apply exemption limit/formula, calculate exempt amount
  - Example CEA: min(received, ₹100 × children × 12) = min(₹X, ₹Y) = ₹Z
  - Compare each with CSV value

**C. Deduction Calculations Verification**:
- **Section 80C** (MUST show component breakdown):
  - List all 80C components: Employee PF (₹A), PPF (₹B), ELSS (₹C), 80C investments (₹D), etc.
  - **Sum**: ₹A + ₹B + ₹C + ₹D = ₹Total
  - **Limit**: ₹150,000 (from mr_dsl.yaml)
  - **Deduction**: min(₹Total, ₹150,000) = ₹X
  - **Compare**: Your ₹X vs CSV value ₹Y
  - If different, explain why
- **Section 80D** (MUST show self and parents separately):
  - **Self/Family**: Premium paid (₹A), limit based on age (₹25K or ₹50K), deduction = min(₹A, limit)
  - **Parents**: Premium paid (₹B), limit based on parents' age (₹25K or ₹50K), deduction = min(₹B, limit)
  - **Total 80D**: Self deduction + Parents deduction = ₹C + ₹D = ₹E
  - Compare ₹E with CSV value
- **Section 80G**:
  - **50% donations**: ₹A × 0.50 = ₹B
  - **100% donations**: ₹C × 1.00 = ₹C
  - **Total 80G**: ₹B + ₹C = ₹D
  - Compare with CSV
- **Other Deductions** (80CCD1, 80CCD2, 80CCD1B, 80DD, 80U, 24(b), 80EEA, 80EEB, 80TTA, 80TTB):
  - For EACH deduction:
    - Show input amount
    - Show limit from mr_dsl.yaml
    - Calculate: min(input, limit) = result
    - Compare with CSV
  - **Example 80CCD(2)**: Employer NPS (₹X), limit 10%/14% of salary (₹Y), deduction = min(₹X, ₹Y)

**D. Taxable Income Calculation Verification**:
- **Step-by-step calculation** (MUST show each step):
  - **Step 1**: Gross Income = ₹X (from input or adjusted for house property)
  - **Step 2**: Total Exemptions = ₹Y (sum all exemptions calculated above)
  - **Step 3**: Income after exemptions = ₹X - ₹Y = ₹Z
  - **Step 4**: Standard Deduction = ₹A (₹75,000 new regime or ₹50,000 old regime per mr_dsl.yaml)
  - **Step 5**: Chapter VI-A Deductions = ₹B (sum of 80C, 80D, 80G, etc. calculated above)
  - **Step 6**: Professional Tax = ₹C (if deductible from taxable income per regime)
  - **Step 7**: Total Deductions = ₹A + ₹B + ₹C = ₹D
  - **Step 8**: Taxable Income = ₹Z - ₹D = ₹E
- **Compare**: Your calculated ₹E vs CSV taxable_income value
- **Verify**: Standard deduction amount is correct for the regime
- **Document**: Any adjustments for house property loss, agricultural income, etc.

**E. Tax Calculation Verification**:
- **Identify Tax Regime**: Verify correct regime (old/new) is used
- **Apply Tax Slabs** (MUST show slab-by-slab breakdown): 
  - Extract tax slab definitions from mr_dsl.yaml for the applicable regime
  - **For EACH slab**, calculate tax:
    - **Slab 1** (₹0 - ₹A): Income in this slab (₹X) × Rate (Y%) = ₹Z
    - **Slab 2** (₹A - ₹B): Income in this slab (₹P) × Rate (Q%) = ₹R
    - **Continue for all applicable slabs**
  - **Example**: Taxable income ₹7,50,000 in old regime:
    - Slab 1: ₹2,50,000 × 0% = ₹0
    - Slab 2: ₹2,50,000 × 5% = ₹12,500
    - Slab 3: ₹2,50,000 × 20% = ₹50,000
    - **Total Base Tax** = ₹0 + ₹12,500 + ₹50,000 = ₹62,500
  - **Compare**: Your calculated base tax vs CSV base_tax value
  - **Document**: Which slabs were used and why
- **Rebate Calculation** (Section 87A):
  - **Check eligibility**: Taxable income ≤ threshold? (₹5L old, ₹12L new 2026-27)
  - **If eligible**: Rebate = min(base_tax, rebate_limit from mr_dsl.yaml)
  - **Calculate**: min(₹X, ₹12,500 or ₹60,000) = ₹Y
  - **Compare**: ₹Y vs CSV rebate_87a value
- **Surcharge Calculation**:
  - **Identify threshold**: Check income against surcharge slabs in mr_dsl.yaml
  - **Calculate**: Base tax × surcharge rate = ₹A × R% = ₹B
  - **Compare**: ₹B vs CSV surcharge value
  - **Document**: Which surcharge bracket applies (10%, 15%, 25%, 30%)
- **Cess Calculation**:
  - **Calculate**: (Base Tax - Rebate + Surcharge) × 4% = (₹A - ₹B + ₹C) × 0.04 = ₹D
  - **Compare**: ₹D vs CSV health_education_cess value
- **Final Tax**:
  - **Calculate**: Base Tax - Rebate + Surcharge + Cess = ₹A - ₹B + ₹C + ₹D = ₹E
  - **Compare**: ₹E vs CSV total_tax_liability value
  - **Monthly TDS**: ₹E / 12 = ₹F (compare with monthly_tds)
  - **Net Salary**: Gross - PF - PT - TDS = ₹G - ₹H - ₹I - ₹E = ₹J
  - **Compare all** with CSV values

**F. Monthly Data Verification** (if applicable):
- Verify monthly gross salary components sum correctly
- Verify monthly exemptions are calculated correctly
- Verify monthly deductions are calculated correctly
- Verify monthly taxable income calculation
- Verify monthly tax calculations (base tax, rebate, surcharge, cess, TDS)
- Verify monthly net salary calculation
- Verify monthly data is consistent with annual data (monthly × 12 ≈ annual, accounting for variations)

**G. Cross-File Consistency Verification**:
- Verify employee ID is consistent across all files
- Verify tax regime is consistent across all files
- Verify annual and monthly data are consistent
- Verify input and output data are logically connected

#### 2.3 Rule Coverage and Compliance Verification

Verify rule coverage and compliance with mr_dsl.yaml:

**A. Rule Identification**:
- Identify all rules from mr_dsl.yaml that should apply to this employee based on:
  - Tax regime (old/new)
  - Income level
  - Age (senior citizen, super senior citizen)
  - Residency status (resident/NRI)
  - Specific deductions/exemptions claimed
  - Other relevant factors

**B. Rule Condition Verification**:
- For each applicable rule, verify the "when" clause conditions are met:
  - Check if income thresholds are met
  - Check if age requirements are met
  - Check if regime requirements are met
  - Check if other conditions are satisfied
- Document which rule conditions are met and which are not

**C. Rule Action Verification**:
- For each applicable rule, verify the "then" clause actions are correctly applied:
  - Verify tax slabs are applied correctly
  - Verify exemptions are calculated per rule formulas
  - Verify deductions are applied per rule limits
  - Verify rebates are applied per rule conditions
  - Verify surcharge and cess are calculated per rule formulas
- Document which rule actions are correctly applied and which are not

**D. Rule ID Mapping Verification**:
- Verify all applicable rule IDs are documented
- Verify rule IDs referenced in output data match actual applicable rules
- Identify any missing rule references
- Identify any incorrect rule references

**E. Rule Coverage Assessment**:
- Assess whether all applicable rules are covered by this employee's test case
- Identify any rules that should apply but are not covered
- Document rule coverage completeness

#### 2.4 Use Case Coverage Verification

Verify the employee data satisfies the assigned test case requirements:

- Extract test case ID(s) assigned to this employee
- Read test case description and key data points from Use_Cases.md
- Verify the employee data satisfies all requirements:
  - Tax regime matches test case requirement
  - Income level matches test case requirement
  - Specific deductions/exemptions match test case requirement
  - Other key data points match test case requirement
- Document whether test case requirements are satisfied

#### 2.5 Compliance Verification

Verify compliance with Indian tax laws and regulations:

- Verify all calculations comply with Indian Income Tax Act
- Verify all calculations comply with mr_dsl.yaml rules
- Verify all deductions, exemptions, and allowances comply with current regulations
- Verify all amounts are within legal limits
- Verify no violations of tax regulations
- Document any compliance issues

#### 2.6 Generate Validation Report

Create a detailed validation report for this employee named `validation_report_{employee_id}.md` (e.g., `validation_report_EMP001.md`) containing:

**Report Structure**:

```markdown
# Validation Report for {Employee ID}

## Employee Information
- Employee ID: {employee_id}
- Employee Name: {name}
- Assigned Test Case IDs: {test_case_ids}
- Tax Regime: {old/new}
- Age: {age}
- City: {city}

## Executive Summary
- Overall Status: ✅ PASS / ⚠️ WARNINGS / ❌ FAIL
- Critical Issues: {count}
- Warnings: {count}
- Passed Checks: {count}

## 1. Mathematical Accuracy Verification

### 1.1 Input Data Verification
- ✅/❌ Gross Salary Calculation: {status}
  - Calculated: {value}
  - Expected: {value}
  - Difference: {value}
  - Formula: {formula}
  
- ✅/❌ Annual CTC Calculation: {status}
  - {details}

### 1.2 Exemption Calculations
- ✅/❌ HRA Exemption: {status}
  - Calculated: {value}
  - Expected: {value}
  - Formula: min(rent - 10% basic, 50%/40% basic, HRA received)
  - Components:
    - Actual rent paid - 10% basic: {value}
    - 50%/40% of basic: {value}
    - Actual HRA received: {value}
    - Minimum: {value}
  - Rule ID: {rule_id from mr_dsl.yaml}
  
- ✅/❌ Conveyance Allowance Exemption: {status}
  - {details}
  
- ✅/❌ LTA Exemption: {status}
  - {details}

### 1.3 Deduction Calculations
- ✅/❌ Section 80C: {status}
  - Calculated: {value}
  - Expected: {value}
  - Components: {list}
  - Limit: {limit from mr_dsl.yaml}
  - Rule ID: {rule_id}
  
- ✅/❌ Section 80D: {status}
  - {details}
  
- ✅/❌ Other Deductions: {status}
  - {details}

### 1.4 Taxable Income Calculation
- ✅/❌ Taxable Income: {status}
  - Gross Income: {value}
  - Total Exemptions: {value}
  - Total Deductions: {value}
  - Standard Deduction: {value}
  - Calculated Taxable Income: {value}
  - Expected Taxable Income: {value}
  - Difference: {value}

### 1.5 Tax Calculation
- ✅/❌ Base Tax: {status}
  - Tax Regime: {old/new}
  - Taxable Income: {value}
  - Slab Breakdown:
    - Slab 1 (0-{threshold}): {income_in_slab} × {rate}% = {tax}
    - Slab 2 ({threshold1}-{threshold2}): {income_in_slab} × {rate}% = {tax}
    - ... (continue for all slabs)
  - Total Base Tax: {calculated_value}
  - Expected Base Tax: {value}
  - Rule ID: {rule_id from mr_dsl.yaml}
  
- ✅/❌ Rebate (Section 87A): {status}
  - Eligibility: {yes/no}
  - Calculated Rebate: {value}
  - Expected Rebate: {value}
  - Rule ID: {rule_id}
  
- ✅/❌ Surcharge: {status}
  - Income Threshold: {threshold from mr_dsl.yaml}
  - Applicable Rate: {rate from mr_dsl.yaml}
  - Calculated Surcharge: {value}
  - Expected Surcharge: {value}
  - Rule ID: {rule_id}
  
- ✅/❌ Cess: {status}
  - Base (Tax + Surcharge): {value}
  - Rate: 4% (from mr_dsl.yaml)
  - Calculated Cess: {value}
  - Expected Cess: {value}
  - Rule ID: {rule_id}
  
- ✅/❌ Final Tax: {status}
  - Base Tax: {value}
  - Rebate: {value}
  - Surcharge: {value}
  - Cess: {value}
  - Calculated Final Tax: {value}
  - Expected Final Tax: {value}
  - Difference: {value}
  
- ✅/❌ Monthly TDS: {status}
  - Calculated: {value}
  - Expected: {value}
  
- ✅/❌ Net Salary: {status}
  - Calculated: {value}
  - Expected: {value}

### 1.6 Monthly Data Verification (if applicable)
- ✅/❌ April 2025: {status}
  - {monthly calculations breakdown}
  
- ✅/❌ December 2025: {status}
  - {monthly calculations breakdown}
  
- ✅/❌ March 2026: {status}
  - {monthly calculations breakdown}

### 1.7 Cross-File Consistency
- ✅/❌ Employee ID Consistency: {status}
- ✅/❌ Tax Regime Consistency: {status}
- ✅/❌ Annual-Monthly Consistency: {status}
- ✅/❌ Input-Output Consistency: {status}

## 2. Rule Coverage and Compliance Verification

### 2.1 Applicable Rules Identified
List of all rules from mr_dsl.yaml that should apply:
- {Rule ID}: {Rule Description} - ✅ Applicable / ❌ Not Applicable
- {Rule ID}: {Rule Description} - ✅ Applicable / ❌ Not Applicable
- ... (list all applicable rules)

### 2.2 Rule Condition Verification
For each applicable rule:
- **{Rule ID}**: {Rule Name}
  - Condition: {when clause from mr_dsl.yaml}
  - Status: ✅ Met / ❌ Not Met
  - Details: {explanation}
  
### 2.3 Rule Action Verification
For each applicable rule:
- **{Rule ID}**: {Rule Name}
  - Action: {then clause from mr_dsl.yaml}
  - Status: ✅ Correctly Applied / ❌ Incorrectly Applied
  - Expected Result: {expected value}
  - Actual Result: {actual value}
  - Difference: {difference}
  
### 2.4 Rule ID Mapping
- ✅/❌ All applicable rules are referenced: {status}
- Missing Rule References: {list}
- Incorrect Rule References: {list}

### 2.5 Rule Coverage Assessment
- Total Applicable Rules: {count}
- Rules Correctly Applied: {count}
- Rules Incorrectly Applied: {count}
- Rules Not Applied: {count}
- Coverage Percentage: {percentage}

## 3. Use Case Coverage Verification

### 3.1 Assigned Test Cases
- Test Case ID: {TC-XX}
  - Description: {description from Use_Cases.md}
  - Key Data Points: {key points}
  
### 3.2 Test Case Requirement Verification
For each assigned test case:
- ✅/❌ Tax Regime Requirement: {status}
  - Required: {value}
  - Actual: {value}
  
- ✅/❌ Income Level Requirement: {status}
  - Required: {value}
  - Actual: {value}
  
- ✅/❌ Specific Deductions/Exemptions: {status}
  - Required: {list}
  - Actual: {list}
  
- ✅/❌ Other Key Data Points: {status}
  - {details}

### 3.3 Test Case Coverage Assessment
- Test Cases Assigned: {count}
- Test Cases Satisfied: {count}
- Test Cases Not Satisfied: {count}
- Coverage Status: ✅ Complete / ⚠️ Partial / ❌ Incomplete

## 4. Compliance Verification

### 4.1 Indian Tax Law Compliance
- ✅/❌ All calculations comply with Indian Income Tax Act: {status}
- Issues: {list}

### 4.2 DSL Rule Compliance
- ✅/❌ All calculations comply with mr_dsl.yaml rules: {status}
- Issues: {list}

### 4.3 Regulation Compliance
- ✅/❌ All deductions, exemptions, and allowances comply with current regulations: {status}
- Issues: {list}

### 4.4 Limit Compliance
- ✅/❌ All amounts are within legal limits: {status}
- Issues: {list}

## 5. Issues and Recommendations

### 5.1 Critical Issues
1. {Issue description}
   - Impact: {high/medium/low}
   - Recommendation: {recommendation}
   
### 5.2 Warnings
1. {Warning description}
   - Impact: {high/medium/low}
   - Recommendation: {recommendation}

### 5.3 Recommendations
1. {Recommendation}

## 6. Summary Statistics

- Total Checks Performed: {count}
- Passed: {count} ({percentage}%)
- Warnings: {count} ({percentage}%)
- Failed: {count} ({percentage}%)
- Overall Status: ✅ PASS / ⚠️ WARNINGS / ❌ FAIL

## 7. Verification Metadata

- Verification Date: {date}
- Verification Time: {time}
- Assessment Year: 2026-27
- DSL Version: {version from mr_dsl.yaml}
```

**Important**: 
- Mark each check as ✅ (pass), ⚠️ (warning), or ❌ (fail)
- Provide detailed calculations and formulas for all verifications
- Reference rule IDs from mr_dsl.yaml for all applicable rules
- Document all discrepancies with expected values
- Provide clear recommendations for any issues found

### Phase 3: Comprehensive Summary Reports (Step 3)

After verifying all 30 employees, create comprehensive summary reports:

#### 3.1 Overall Validation Summary

Create `overall_validation_summary.md` containing:
- Total employees verified: 30
- Overall pass rate: {percentage}
- Total critical issues: {count}
- Total warnings: {count}
- Summary statistics by category:
  - Mathematical accuracy: {pass rate}
  - Rule compliance: {pass rate}
  - Use case coverage: {pass rate}
  - Compliance: {pass rate}
- List of employees with critical issues
- List of employees with warnings
- List of employees that passed all checks

#### 3.2 Rule Coverage Summary

Create `rule_coverage_summary.md` containing:
- Total rules in mr_dsl.yaml: {count}
- Rules covered by test cases: {count}
- Rules not covered: {list}
- Rule coverage percentage: {percentage}
- Mapping of rules to employees/test cases
- Rules with most coverage
- Rules with least coverage

#### 3.3 Test Case Coverage Summary

Create `test_case_coverage_summary.md` containing:
- Total test cases from Use_Cases.md: {count}
- Test cases covered: {count}
- Test cases not covered: {list}
- Test case coverage percentage: {percentage}
- Mapping of test cases to employees
- Employees covering multiple test cases

#### 3.4 Issue Summary

Create `issue_summary.md` containing:
- Critical issues by category:
  - Mathematical errors: {count}
  - Rule compliance errors: {count}
  - Use case coverage issues: {count}
  - Compliance violations: {count}
- Warnings by category: {similar breakdown}
- Recommendations for fixes
- Priority ranking of issues

### Phase 4: Final Report (Step 4)

Create `final_verification_report.md` containing:
- Executive summary
- Overall assessment
- Key findings
- Critical issues requiring immediate attention
- Recommendations for improvement
- Next steps

## File Path Handling

When processing this prompt:
- **If a filepath is provided**: Use that directory as the source for input files
- **If no filepath is provided**: 
  - If this prompt is in a subdirectory (e.g., `test_data_generation_one_by_one/`), use the **parent directory** (e.g., `India_test_case_generation/`) as the source for input files
  - Otherwise, use the directory where this prompt file is located as the source for input files
- Read all required files from the source directory:
  - **Schema and rule files**: employee_dsl.yaml, mr_dsl.yaml, Data_requirements.md, Use_Cases.md (from the source directory)
  - **Generated CSV files**: All master output CSV files (typically in `output_with_dsl_{timestamp}/` subdirectories within the source directory)
- **Create verification output directory**: Generate a new folder named `verification_{timestamp}` in the source directory where `{timestamp}` is the current timestamp in format `YYYYMMDD_HHMMSS` (e.g., `verification_20250115_143022`)
- Generate all validation reports in the verification output directory

## Quality Standards

All verification must meet these quality standards:

1. **Completeness**: All 30 employees must be verified
2. **Accuracy**: All calculations must be verified with detailed breakdowns
3. **Rule Compliance**: All applicable rules must be identified and verified
4. **Documentation**: All findings must be clearly documented
5. **Actionability**: All issues must have clear recommendations

## Notes

- Verify employees one by one systematically
- Do not skip any verification steps
- Document all findings, even if they pass
- Provide detailed calculations for all verifications
- Reference rule IDs from mr_dsl.yaml for all applicable rules
- Be thorough and accurate in all verifications
- Flag any discrepancies, no matter how small

---

**Ready to verify**: Once you have read all required files (employee_dsl.yaml, mr_dsl.yaml, Data_requirements.md, Use_Cases.md, and all generated CSV files) from the provided directory (or the parent directory if this prompt is in a subdirectory, or the directory where this prompt is located if no directory is provided), proceed to:

1. **Step 1**: Create verification output directory and read all files
2. **Step 2**: Verify each employee one by one (EMP001 through EMP030):
   - Extract employee data
   - Verify mathematical accuracy
   - Verify rule coverage and compliance
   - Verify use case coverage
   - Verify compliance
   - Generate validation report for each employee
3. **Step 3**: Create comprehensive summary reports
4. **Step 4**: Create final verification report

**Important**: This verification should be performed after all employee generation is complete. Verify all 30 employees systematically and thoroughly.

