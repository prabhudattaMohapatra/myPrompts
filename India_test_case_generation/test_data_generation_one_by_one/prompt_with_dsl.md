# Test Case Generation Prompt for Indian Payroll Engine (with DSL Rules) - One-by-One Employee Generation

## ROLE
You are an expert tax consultant and test engineer specializing in Indian tax law and payroll systems.

## TASK
Generate comprehensive test cases for validating the Indian Payroll Engine for assessment year 2026-27. The test cases must satisfy specific data requirements and cover all defined use cases, while ensuring full compliance with Indian tax laws and regulations. **This prompt uses an iterative one-by-one employee generation workflow.**

## TARGET USERS
- Payroll administrators
- Tax professionals
- System developers

## PURPOSE
Validate tax calculations against official Indian tax regulations and ensure the payroll engine correctly implements all tax rules, exemptions, deductions, and compliance requirements as defined in the machine-readable DSL rules. Generate employees one at a time with full verification before proceeding to the next employee.

## Context

You will be provided with the following files. **Note**: If this prompt is in a subdirectory (e.g., `test_data_generation_one_by_one/`), the required files are located in the parent directory (`India_test_case_generation/`):

- **employee_dsl.yaml**: Contains the complete input schema definition for employee data structure with all available input fields
- **mr_dsl.yaml**: Contains machine-readable DSL rules for Indian payroll and taxation - use this as a **minimum but not exhaustive** rule set for compliance
- **Data_requirements.md**: Specifies the data requirements including number of employees, input/output requirements, and necessity levels
- **Use_Cases.md**: Lists all test case scenarios that must be covered with their specific requirements

## Workflow Overview

This prompt follows an **iterative one-by-one employee generation workflow**:

1. **Step 1**: Prepare test case ID to use case mapping and create empty master CSV files with headers
2. **Step 2**: Generate one employee's annual CTC breakdown input data
3. **Step 3**: Generate monthly input data for the same employee (if required by the test case)
4. **Step 4**: Generate one employee's annual tax forecast output data
5. **Step 5**: Generate monthly output data for the same employee (if required by the test case)
6. **Step 6**: Verify all calculations in input and output data, verify use case coverage, and output verification report to a markdown file
7. **Step 7**: Append the verified employee data to the master output CSV files
8. **Step 8**: Repeat steps 2-7 for all remaining employees/test cases

## Instructions

### Phase 1: Initial Setup (Step 1)

1. **Read and understand the schema**: First, read the `employee_dsl.yaml` file to understand the complete data structure, field types, and relationships for the inputs you are going to prepare.

2. **Read and understand the tax rules DSL**: Read the `mr_dsl.yaml` file to understand the Indian payroll and taxation rules. This file contains:
   - Tax slab definitions (old regime, new regime, senior citizens, super senior citizens)
   - Surcharge rules and thresholds
   - Cess calculations
   - Rebate rules (Section 87A)
   - Deduction limits and rules (Section 80C, 80D, 80G, etc.)
   - Exemption rules for allowances (HRA, conveyance, LTA, etc.)
   - Professional tax rules
   - Other compliance rules and regulations
   
   **Important**: The `mr_dsl.yaml` file provides a **minimum rule set** but is **not exhaustive**. You must:
   - Use all rules defined in `mr_dsl.yaml` as the baseline for compliance
   - Apply additional Indian tax laws and regulations that may not be explicitly covered in the DSL
   - Ensure complete compliance even if a specific rule is not in the DSL file
   - Cross-reference DSL rules with your knowledge of Indian Income Tax Act

3. **Review requirements**: Read `Data_requirements.md` to understand:
   - **Total number of employees needed: 30** (hardcoded requirement)
   - Required input datasets (marked as "Necessary" and "Input") - note that each requirement represents a dataset, not a single field
   - Required output datasets (marked as "Necessary" and "Output") - each requirement represents a dataset with multiple fields
   - Optional datasets (marked as "Optional")
   
   **Important**: Each entry in the requirements table represents a **dataset** (a group of related fields), not a single field. For example:
   - "Annual CTC breakdown Data" is a dataset containing multiple salary component fields
   - "Monthly Payslip Data" is a dataset with multiple fields for each required month
   - "Demographic Information" is a dataset with age, parent_age, number_of_children, etc.

4. **Extract use cases**: Read `Use_Cases.md` and extract all test cases listed in the table. Each row in the table represents a test case with:
   - Test Case ID (e.g., TC-01, TC-02, etc.)
   - Persona/Scenario Description
   - Key Data Points

5. **Map datasets to schema fields**: For each dataset requirement in `Data_requirements.md`:
   - Identify which fields from `employee_dsl.yaml` belong to that dataset
   - Understand the structure of each dataset (e.g., monthly data may need multiple columns or rows)
   - Consider time-based fields (period, moment, timeless) from the schema when structuring the data
   - Map dataset requirements to actual schema fields:
     * "Annual CTC breakdown Data" → fields like basic_salary, hra_received, special_allowance, gross_salary, etc.
     * "Demographic Information" → age, parent_age, number_of_children, etc.
     * "Monthly Payslip Data" → fields needed for payslip output, structured for multiple months
     * "Monthly Bonus and Commission Data" → bonus, performance_bonus, commission fields for specific months
     * And so on for all dataset requirements

6. **Create test case ID to use case mapping**: Create a mapping document showing:
   - Which test case IDs will be covered
   - Which employees will cover which test cases
   - Plan for covering all 30 employees and all test cases from Use_Cases.md

7. **Create empty master CSV files with headers**: Create the following CSV files with **only header rows** (no data rows yet):
   - `annual_employee_input_data.csv` - with all required columns from Annual Input CSV requirements
   - `monthly_bonus_commission_april.csv` - with columns: ID, bonus, commission, performance_bonus (and other relevant monthly bonus/commission fields)
   - `monthly_bonus_commission_december.csv` - same columns as April
   - `monthly_bonus_commission_march.csv` - same columns as April
   - `ctc_revision_december.csv` - with columns: ID, revised_annual_ctc, revised_basic_salary, revised_gross_salary, and other revised salary components
   - `tax_regime_revision_december.csv` - with columns: ID, previous_tax_regime, new_tax_regime, revision_date, and other relevant fields
   - `annual_tax_forecast.csv` - with all required columns from Annual Output CSV requirements
   - `monthly_payslip_april.csv` - with all required columns from Monthly Output CSV requirements
   - `monthly_payslip_december.csv` - same columns as April
   - `monthly_payslip_march.csv` - same columns as April
   - `test_cases_master_summary.csv` - with columns: Test ID, Employee Name, Age, Tax Regime, City, Gross Income, Taxable Income, Tax Breakdown, Final Tax, Key Features, Rules Applied, Status

   **Note**: These are the master output files. You will append employee data to these files one by one as you generate each employee.

### Phase 2: Iterative Employee Generation (Steps 2-8)

For each employee (EMP001 through EMP030), follow this workflow:

#### Step 2: Generate One Employee's Annual CTC Breakdown Input Data

Generate the annual input data for **one employee** based on their assigned test case(s):
- Employee ID (e.g., EMP001)
- All demographic information (age, parent_age, number_of_children, residency, city, etc.)
- Annual CTC breakdown (basic_salary, hra_received, special_allowance, gross_salary, etc.)
- Tax information (tax_regime, employment_type, etc.)
- Investment declarations (section_80c_investments, self_family_premium, etc.)
- All other required annual input fields from the schema

**Important**: 
- Generate data that satisfies the test case requirements for this employee
- Ensure all data is compliant with Indian tax laws and mr_dsl.yaml rules
- Use realistic values appropriate for the test case scenario

#### Step 3: Generate Monthly Input Data for the Same Employee (If Required)

**Note**: Not every employee needs monthly input data. Generate monthly input data only if:
- The test case requires bonus/commission data for specific months (April, December, March)
- The employee is one of the 3 employees requiring CTC revision in December
- The employee is one of the 2 employees requiring tax regime revision in December

If monthly input data is required:
- Generate bonus/commission data for the required months (if applicable)
- Generate CTC revision data for December (if this employee is one of the 3)
- Generate tax regime revision data for December (if this employee is one of the 2)

**Remember**: 
- Monthly bonus/commission CSVs must have at least 5 non-zero values total across all employees (not per employee)
- CTC revision CSV must have exactly 3 employees total
- Tax regime revision CSV must have exactly 2 employees total

#### Step 4: Generate One Employee's Annual Tax Forecast Output Data

Generate the annual tax forecast output data for **the same employee**:
- Calculate all exemptions (HRA, conveyance, LTA, etc.) based on input data
- Calculate all deductions (80C, 80D, 80G, etc.) based on input data
- Calculate taxable income
- Calculate base tax using appropriate tax slabs from mr_dsl.yaml
- Calculate rebates (Section 87A) if applicable
- Calculate surcharge and cess
- Calculate final tax liability and monthly TDS
- Calculate net salary

**Important**:
- All calculations must be mathematically accurate
- All calculations must comply with mr_dsl.yaml rules
- Reference rule IDs from mr_dsl.yaml for each calculation
- Include step-by-step calculation breakdown

#### Step 5: Generate Monthly Output Data for the Same Employee (If Required)

**Note**: Not every employee needs monthly output data. Generate monthly payslip data for:
- April 2025
- December 2025
- March 2026

For each required month, generate:
- Monthly gross salary components
- Monthly exemptions
- Monthly deductions
- Monthly taxable income
- Monthly tax calculations (base tax, rebate, surcharge, cess, TDS)
- Monthly net salary

**Important**:
- Monthly calculations should be consistent with annual calculations
- Monthly TDS should align with annual tax forecast
- Reference rule IDs from mr_dsl.yaml for each calculation

#### Step 6: Verify All Calculations and Use Case Coverage

Before appending to master files, perform comprehensive verification:

**Create a verification markdown file** named `employee_verification_{employee_id}.md` (e.g., `employee_verification_EMP001.md`) containing:

1. **Employee Information**:
   - Employee ID
   - Assigned test case IDs
   - Test case descriptions

2. **Input Data Verification**:
   - Verify all required input fields are present
   - Verify data types are correct
   - Verify data values are realistic and appropriate for the test case
   - Verify data is internally consistent

3. **Calculation Verification**:
   - **Mathematical Accuracy**: Verify all calculations are mathematically correct
     - Gross salary = sum of all salary components
     - Taxable income = gross income - exemptions - deductions
     - Tax calculations follow progressive slab structure
     - Surcharge and cess calculations are correct
     - Final tax = base tax - rebate + surcharge + cess
   - **Rule Compliance**: Verify all calculations comply with mr_dsl.yaml rules
     - Tax slabs match DSL definitions
     - Exemption calculations follow DSL formulas
     - Deduction limits match DSL specifications
     - Rebate calculations follow DSL rules
   - **Step-by-Step Breakdown**: Document all intermediate calculations
     - Show exemption calculations with formulas
     - Show deduction calculations with limit checks
     - Show tax slab breakdown
     - Show surcharge and cess calculations
     - Reference rule IDs for each calculation

4. **Output Data Verification**:
   - Verify output data logically follows from input data
   - Verify annual and monthly data are consistent
   - Verify all required output fields are present
   - Verify calculations match expected results based on input

5. **Use Case Coverage Verification**:
   - Verify the employee data satisfies all requirements of the assigned test case(s)
   - Verify key data points from Use_Cases.md are represented
   - Verify test case scenario is accurately reflected in the data

6. **Rule ID Mapping**:
   - List all rule IDs from mr_dsl.yaml that apply to this employee
   - Verify rule conditions (when clauses) are met
   - Verify rule actions (then clauses) are correctly applied

7. **Compliance Verification**:
   - Verify all data is compliant with Indian tax laws
   - Verify all calculations comply with mr_dsl.yaml rules
   - Verify no violations of tax regulations

8. **Issues and Resolutions**:
   - Document any issues found during verification
   - Document how issues were resolved
   - Confirm all issues are resolved before proceeding

**Only proceed to Step 7 if all verifications pass.**

#### Step 7: Append to Master Output CSV Files

Once verification is complete and documented, append the verified employee data to the master CSV files:

1. **Append to `annual_employee_input_data.csv`**: Add one row with the employee's annual input data

2. **Append to monthly input CSVs** (if applicable):
   - Append to `monthly_bonus_commission_april.csv` (if employee has bonus/commission in April)
   - Append to `monthly_bonus_commission_december.csv` (if employee has bonus/commission in December)
   - Append to `monthly_bonus_commission_march.csv` (if employee has bonus/commission in March)
   - Append to `ctc_revision_december.csv` (if employee is one of the 3 requiring CTC revision)
   - Append to `tax_regime_revision_december.csv` (if employee is one of the 2 requiring tax regime revision)

3. **Append to `annual_tax_forecast.csv`**: Add one row with the employee's annual tax forecast output data

4. **Append to monthly output CSVs** (if applicable):
   - Append to `monthly_payslip_april.csv`: Add one row with April payslip data
   - Append to `monthly_payslip_december.csv`: Add one row with December payslip data
   - Append to `monthly_payslip_march.csv`: Add one row with March payslip data

5. **Append to `test_cases_master_summary.csv`**: Add one row per test case covered by this employee (if employee covers multiple test cases, add multiple rows)

**Important**: 
- Maintain consistent employee ID and order across all files
- Ensure data format matches the header row
- Do not overwrite existing data - only append

#### Step 8: Repeat for Next Employee

After successfully appending one employee's data:
- Move to the next employee (EMP002, EMP003, etc.)
- Repeat Steps 2-7 for the next employee
- Continue until all 30 employees are generated

**Progress Tracking**: 
- Keep track of which employees have been generated
- Keep track of which test cases have been covered
- Ensure all test cases from Use_Cases.md are covered by at least one employee
- Ensure all 30 employees are generated

## CSV Format Requirements

These requirements apply to all generated CSV files:

- **Header row**: Include all relevant fields from the employee schema that are needed for the test cases
  - For input CSV: Include all fields from all input datasets (map each dataset requirement to its constituent fields)
  - For output CSV: Include all fields from all output datasets
  - For time-based datasets, use appropriate column naming (e.g., `april_bonus`, `december_bonus`, `march_bonus` for monthly bonus data)
- **Data rows**: Each row represents one employee with their complete data
- **Field values**: 
  - Use appropriate data types (strings, numbers, dates, booleans)
  - Dates should be in YYYY-MM-DD format
  - Money values should be numeric (in Indian Rupees)
  - Boolean values should be true/false
  - Empty/null values should be left blank or use appropriate null representation
- **Consistency**: Ensure employee IDs and order are consistent across all CSV files

## Minimum Required Columns

### Annual Input CSV (`annual_employee_input_data.csv`)
- ID, Age, Parents' age, No. of Children, residency, city, city_type, employment_type, tax_regime, owns_house_in_work_city, joining date
- annual ctc, gross salary, basic salary
- hra received, special allowance, transport allowance, conveyance allowance, meal allowance, leave travel allowance
- children education allowance, children hostel allowance, books and periodical allowance, telephone allowance
- bonus, commission
- employee pf contribution, employer pf contribution, vpf
- nps employee contribution, nps employer contribution, nps additional contribution
- section_80c_investments, self_family_premium, parents health insurance premium
- professional tax paid, income or loss from house property, rent paid
- Additional columns from employee_dsl.yaml as needed

### Monthly Input CSVs
**Monthly Bonus and Commission** (April, December, March):
- ID, bonus, commission, performance_bonus (and other relevant monthly bonus/commission fields)

**CTC Revision** (December):
- ID, revised_annual_ctc, revised_basic_salary, revised_gross_salary, and other revised salary components

**Tax Regime Revision** (December):
- ID, previous_tax_regime, new_tax_regime, revision_date, and other relevant fields

### Annual Output CSV (`annual_tax_forecast.csv`)
- ID, Tax Regime
- Gross Salary, Basic Salary
- HRA Exemption, Conveyance Allowance exemption, LTA exemption, total tax exemptions
- 80C deduction, 80D deduction, 80CCD(1) deduction, 80CCD(2) deduction, 80CCD(1b) deduction
- 80DD deduction, 80U deduction, 80G deduction
- 24(b) deduction, 80EEA deduction, 80EEB deduction
- 80TTA deduction, 80TTB deduction
- total deductions, gross income, taxable income
- base tax, rebate, tax after rebate, surcharge, tax with surcharge
- health and education cess, total tax liability, monthly tds, net salary
- Additional columns for step-by-step calculation breakdown and rule ID references

### Monthly Output CSVs (`monthly_payslip_april.csv`, `monthly_payslip_december.csv`, `monthly_payslip_march.csv`)
- ID, Tax Regime
- Gross Salary_monthly, Basic Salary_monthly
- HRA Received_monthly, Conveyance Allowance Received_monthly
- HRA Exemption_monthly, Conveyance Allowance exemption_monthly, Total tax exemptions_monthly
- 80C deduction_monthly, 80D deduction_monthly, 80CCD(1) deduction_monthly, 80CCD(2) deduction_monthly, 80CCD(1b) deduction_monthly
- 80DD deduction_monthly, 80U deduction_monthly, 80G deduction_monthly
- 24(b) deduction_monthly, 80EEA deduction_monthly, 80EEB deduction_monthly
- 80TTA deduction_monthly, 80TTB deduction_monthly
- Total deductions_monthly, Gross Income_monthly, Taxable Income_monthly
- Base tax_monthly, Rebate_monthly, Tax after rebate_monthly, Surcharge_monthly, Tax with surcharge_monthly
- Health and education cess_monthly, tds_monthly, Net Salary_monthly
- Additional columns for step-by-step calculation breakdown and rule ID references

### Master Summary CSV (`test_cases_master_summary.csv`)
- Test ID, Employee Name, Age, Tax Regime, City, Gross Income, Taxable Income, Tax Breakdown, Final Tax, Key Features, Rules Applied, Status

## Calculation Transparency Requirements

All test cases must include comprehensive calculation documentation showing:

1. **Step-by-Step Breakdown**:
   - Document every intermediate calculation step
   - Show formulas used for each calculation
   - Display all threshold checks and conditions
   - Include all rounding and precision handling
   - Reference rule IDs from mr_dsl.yaml for each calculation

2. **Gross to Net Computation**:
   - Start with gross salary components
   - Show each exemption applied with formula and amount
   - Show each deduction applied with limit checks
   - Calculate taxable income step-by-step
   - Reference applicable rule IDs

3. **Exemption Calculations**:
   - HRA exemption: Show all three calculations (actual rent paid, 50%/40% of basic, actual HRA received) and minimum
   - Conveyance allowance: Show exemption limit application
   - LTA: Show exemption calculation and conditions
   - Other allowances: Show exemption formulas and limits
   - Reference rule IDs from mr_dsl.yaml for each exemption

4. **Deduction Itemization**:
   - Section 80C: Show all components and aggregate limit
   - Section 80D: Show self, family, and parents' premiums with limits
   - Section 80G: Show eligible donations and limits
   - Other deductions: Show each deduction with applicable limits
   - Reference rule IDs from mr_dsl.yaml for each deduction

5. **Tax Slab Breakdown**:
   - Show income falling in each tax slab (use slab definitions from mr_dsl.yaml)
   - Calculate tax for each slab separately
   - Show progressive tax calculation
   - Display cumulative tax at each slab
   - Reference tax slab rule IDs from mr_dsl.yaml

6. **Surcharge and Cess**:
   - Show surcharge calculation based on income thresholds (from mr_dsl.yaml)
   - Show health and education cess calculation (from mr_dsl.yaml)
   - Display total tax including surcharge and cess
   - Reference surcharge and cess rule IDs

7. **Final Tax Liability**:
   - Show rebates applied (e.g., Section 87A) with rule ID reference
   - Show final tax after rebates
   - Calculate monthly TDS/withholding
   - Show annual tax forecast

8. **Mathematical Verification**:
   - Verify all additions and subtractions
   - Verify percentage calculations
   - Verify rounding at each step
   - Cross-verify final tax with manual calculation
   - Verify calculations match rule outputs from mr_dsl.yaml

**Documentation Format**: Include these calculations in:
- Verification markdown file for each employee (`employee_verification_{employee_id}.md`)
- Detailed Output CSV columns with step-by-step breakdown and rule ID columns

## Validation Requirements

For each employee, perform the following validations before appending to master files:

### Rule Validation (MANDATORY - mr_dsl.yaml is available):
- **All applicable rules are triggered**: Verify that for this employee's test case(s), all relevant rules from mr_dsl.yaml are identified and applied
- **Rule conditions are met**: Verify that all "when" clauses in applicable rules are satisfied by the employee's data
- **Rule actions are applied correctly**: Verify that all "then" clauses in applicable rules are correctly implemented in the expected results
- **Rule ID mapping**: Document which rule IDs apply to this employee in the verification file
- **Rule verification**: Cross-verify that calculations match the expected outputs from mr_dsl.yaml rules

### Calculation Validation:
- **Mathematical accuracy verified**: All calculations must be mathematically correct
  - Verify addition, subtraction, multiplication, division
  - Verify percentage calculations
  - Verify rounding rules
  - Cross-check totals and subtotals
  - Verify against mr_dsl.yaml rule outputs

- **Boundary conditions tested**: If the test case requires boundary testing:
  - Values at exact thresholds (e.g., exactly ₹12L for rebate threshold)
  - Values just below thresholds
  - Values just above thresholds
  - Maximum limit cases (e.g., maximum deduction limits from mr_dsl.yaml)
  - Minimum value cases

- **Formula application verified**: 
  - HRA exemption formula correctly applied (per mr_dsl.yaml rules)
  - Tax slab calculations follow progressive structure (per mr_dsl.yaml)
  - Surcharge calculations at correct thresholds (per mr_dsl.yaml)
  - Cess calculations on correct base (per mr_dsl.yaml)

### Data Validation:
- **Input data consistency**: Verify that input data is internally consistent
- **Output data consistency**: Verify that output data logically follows from input data
- **Cross-file consistency**: Verify that data is consistent across annual and monthly files for this employee
- **Rule compliance**: Verify that all calculations comply with mr_dsl.yaml rules

### Compliance Validation:
- **Tax law compliance**: All calculations comply with Indian Income Tax Act
- **DSL rule compliance**: All calculations comply with rules in mr_dsl.yaml
- **Regulation compliance**: All deductions, exemptions, and allowances comply with current regulations
- **Limit compliance**: All amounts are within legal limits for each category (as per mr_dsl.yaml)

## Indian Tax Law and Income Rule Compliance

**CRITICAL REQUIREMENT**: All test case data must be fully compliant with Indian tax laws and income tax rules and regulations. This is a non-negotiable requirement.

### Compliance Requirements Using mr_dsl.yaml:

1. **Tax Slabs and Rates**:
   - Use tax slab definitions from `mr_dsl.yaml` for old regime, new regime, senior citizens, and super senior citizens
   - Apply progressive tax rates exactly as defined in the DSL
   - Ensure slab ranges and rates match the DSL specifications

2. **Surcharge and Cess**:
   - Apply surcharge rules and thresholds as defined in `mr_dsl.yaml`
   - Calculate cess (health and education cess) as per DSL rules
   - Ensure surcharge calculations follow the DSL specifications

3. **Rebates**:
   - Apply Section 87A rebate rules as defined in `mr_dsl.yaml`
   - Ensure rebate eligibility and amounts match DSL specifications
   - Apply rebate correctly based on income thresholds in the DSL

4. **Deductions**:
   - Use deduction limits and rules from `mr_dsl.yaml` where available
   - Section 80C, 80D, 80G, and other deductions must comply with DSL limits
   - Apply additional deduction rules from Indian Income Tax Act that may not be in the DSL
   - Investment declarations must be within legal limits

5. **Exemptions**:
   - Apply exemption rules for allowances as defined in `mr_dsl.yaml`
   - HRA exemption calculations must follow DSL rules and formulas
   - Conveyance allowance, LTA, and other allowance exemptions must comply with DSL limits
   - Apply additional exemption rules from tax laws not covered in DSL

6. **Professional Tax**:
   - Apply professional tax rules as defined in `mr_dsl.yaml`
   - Ensure state-specific rules are followed
   - Apply annual caps as specified in the DSL

7. **Special Cases**:
   - Senior citizen benefits must follow DSL slab definitions
   - NRI tax treatment must comply with residency rules (use DSL where applicable)
   - Section 89 relief calculations must be accurate
   - Apply rules for gratuity, EPF withdrawal, etc. as per DSL and tax laws

8. **Data Accuracy**:
   - Every number, calculation, and data point must be mathematically correct
   - Taxable income calculations must be accurate
   - All percentages, amounts, and thresholds must align with `mr_dsl.yaml` rules
   - Output data (tax forecasts, payslips) must be consistent with input data and DSL rules

### Using mr_dsl.yaml as Minimum Rule Set:

- **Always use rules from mr_dsl.yaml**: If a rule is defined in the DSL, you MUST use it exactly as specified
- **Supplement with additional tax laws**: The DSL is not exhaustive - apply additional Indian Income Tax Act provisions, Finance Act rules, and current tax regulations
- **Cross-reference**: Verify DSL rules against your knowledge of Indian tax laws to ensure completeness
- **Consistency**: Ensure all calculations are consistent with both DSL rules and broader tax law framework
- **Assessment Year**: Use assessment year 2026-27 for all calculations. If mr_dsl.yaml contains rules for 2026-27, use those. If it contains rules for 2025-26, adapt them appropriately for 2026-27 or use your knowledge of Indian tax laws for 2026-27

**Priority**: DSL rules take precedence for specific calculations, but you must ensure overall compliance with all Indian tax laws and regulations, even if not explicitly in the DSL.

## File Path Handling

When processing this prompt:
- **If a filepath is provided**: Use that directory as the source for input files
- **If no filepath is provided**: 
  - If this prompt is in a subdirectory (e.g., `test_data_generation_one_by_one/`), use the **parent directory** (e.g., `India_test_case_generation/`) as the source for input files
  - Otherwise, use the directory where this prompt file is located as the source for input files
- Read all four files (employee_dsl.yaml, mr_dsl.yaml, Data_requirements.md, Use_Cases.md) from the source directory
- **Create an output directory**: Generate a new folder named `output_with_dsl_{timestamp}` in the source directory where `{timestamp}` is the current timestamp in format `YYYYMMDD_HHMMSS` (e.g., `output_with_dsl_20250115_143022`)
- Generate all CSV output files and verification files in the output directory (not in the source directory)
- Ensure all file paths are handled dynamically based on the provided or default directory path

## Final Quality Assurance

After all 30 employees have been generated and appended to master files:

1. **Verify all CSV files are complete**:
   - Master Summary CSV: Should have entries for all test cases
   - Annual Input CSV: Should have exactly 30 employee rows
   - Monthly Input CSVs: Should have appropriate rows (at least 5 non-zero values in bonus/commission files, exactly 3 in CTC revision, exactly 2 in tax regime revision)
   - Annual Output CSV: Should have exactly 30 employee rows
   - Monthly Output CSVs: Should have exactly 30 employee rows each

2. **Verify all test cases are covered**: All test cases from Use_Cases.md should be covered by at least one employee

3. **Verify all employees are generated**: All 30 employees (EMP001-EMP030) should be present in all relevant CSV files

4. **Create final summary documents**:
   - `test_case_rule_mapping.md`: Comprehensive mapping of all test cases to rule IDs from mr_dsl.yaml
   - `test_case_mapping.md`: Mapping of employees to test cases
   - `final_verification_summary.md`: Summary of all verification results

5. **Verify data consistency**: 
   - Employee IDs and order are consistent across all files
   - Data types match schema definitions
   - All calculations are mathematically accurate
   - All data complies with Indian tax laws and mr_dsl.yaml rules

## Notes

- Generate employees one at a time with full verification before proceeding
- Not every employee needs monthly input/output data - only generate when required by the test case
- Ensure data consistency across months for the same employee
- Use realistic Indian names, PAN numbers, and addresses
- Ensure tax regime selections align with the test case requirements
- Include appropriate variations in income levels, deductions, and exemptions
- Consider edge cases and boundary conditions mentioned in the use cases
- **All data must be compliant with Indian tax laws and mr_dsl.yaml rules - verify every calculation and amount**
- **When in doubt between DSL rules and general tax knowledge, prioritize DSL rules but ensure overall tax law compliance**

---

**Ready to generate**: Once you have read all four files (employee_dsl.yaml, mr_dsl.yaml, Data_requirements.md, Use_Cases.md) from the provided directory (or the parent directory if this prompt is in a subdirectory, or the directory where this prompt is located if no directory is provided), proceed to:

1. **Step 1**: Create the output directory `output_with_dsl_{timestamp}` in the source directory
2. **Step 1**: Create test case ID to use case mapping document
3. **Step 1**: Create empty master CSV files with headers (all files listed above)
4. **Steps 2-8**: Generate employees one by one following the iterative workflow:
   - Step 2: Generate one employee's annual input data
   - Step 3: Generate monthly input data (if required)
   - Step 4: Generate one employee's annual output data
   - Step 5: Generate monthly output data (if required)
   - Step 6: Verify all calculations and create verification markdown file
   - Step 7: Append verified data to master CSV files
   - Step 8: Repeat for next employee
5. **Final**: Create final summary documents and perform final quality assurance

**Important**: Do NOT generate Arrears Data files (marked as "Later, not to be generated now" in Data_requirements.md)

**Note on Task Size**: Generating 30 employees one by one is a substantial task. You are free to split this work across multiple chat sessions if needed. If doing so:
- Track which employees have been completed in each session
- Ensure consistency in data format, employee IDs, and file structure across all sessions
- Continue appending to the same master CSV files across sessions
- Ensure all 30 employees are eventually generated

