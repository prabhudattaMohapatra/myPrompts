# Test Case Generation Prompt for Indian Payroll Engine

## ROLE
You are an expert tax consultant and test engineer specializing in Indian tax law and payroll systems.

## TASK
Generate comprehensive test cases for validating the Indian Payroll Engine for assessment year 2025-26. The test cases must satisfy specific data requirements and cover all defined use cases.

## TARGET USERS
- Payroll administrators
- Tax professionals
- System developers

## PURPOSE
Validate tax calculations against official Indian tax regulations and ensure the payroll engine correctly implements all tax rules, exemptions, deductions, and compliance requirements.

## Context

You will be provided with the following files in the same directory:
- **employee_dsl.yaml**: Contains the complete input schema definition for employee data structure with all available input fields
- **Data_requirements.md**: Specifies the data requirements including number of employees, input/output requirements, and necessity levels
- **Use_Cases.md**: Lists all test case scenarios that must be covered with their specific requirements

## Instructions

1. **Read and understand the schema**: First, read the `employee_dsl.yaml` file to understand the complete data structure, field types, and relationships for the inputs you are going to prepare.

2. **Review requirements**: Read `Data_requirements.md` to understand:
   - **Total number of employees needed: 50** (hardcoded requirement)
   - Required input datasets (marked as "Necessary" and "Input") - note that each requirement represents a dataset, not a single field
   - Required output datasets (marked as "Necessary" and "Output") - each requirement represents a dataset with multiple fields
   - Optional datasets (marked as "Optional")
   
   **Note**: Generating 50 employees with all required data is a substantial task. You are free to split this work across multiple tries if it's too much. For example:
   - First try: Generate a subset of employees (covering a portion of the test cases)
   - Subsequent tries: Generate the remaining employees (covering the remaining test cases)
   - Ensure consistency in data format, employee IDs, and file structure across all sessions
   
   **Important**: Each entry in the requirements table represents a **dataset** (a group of related fields), not a single field. For example:
   - "Annual CTC breakdown Data" is a dataset containing multiple salary component fields
   - "Monthly Payslip Data" is a dataset with multiple fields for each required month
   - "Demographic Information" is a dataset with age, parent_age, number_of_children, etc. 

3. **Extract use cases**: Read `Use_Cases.md` and extract all test cases listed in the table. Each row in the table represents a test case with:
   - Test Case ID (e.g., TC-01, TC-02, etc.)
   - Persona/Scenario Description
   - Key Data Points
   
   Map each extracted test case to specific employee records, ensuring all scenarios are covered.

4. **Map datasets to schema fields**: For each dataset requirement in `Data_requirements.md`:
   - Identify which fields from `employee_dsl.yaml` belong to that dataset
   - Understand the structure of each dataset (e.g., monthly data may need multiple columns or rows)
   - Consider time-based fields (period, moment, timeless) from the schema when structuring the data
   - Map dataset requirements to actual schema fields:
     * "Annual CTC breakdown Data" → fields like basic_salary, hra_received, special_allowance, gross_salary, etc.
     * "Demographic Information" → age, parent_age, number_of_children, etc.
     * "Monthly Payslip Data" → fields needed for payslip output, structured for multiple months
     * "Monthly Bonus and Commission Data" → bonus, performance_bonus, commission fields for specific months
     * And so on for all dataset requirements
   
   Create a mapping document showing which schema fields correspond to each dataset requirement.

5. **Separate input and output datasets**: Based on the requirements extracted from Data_requirements.md:
   - **Input datasets**: All datasets marked as "Input" (both Necessary and Optional)
   - **Output datasets**: All datasets marked as "Output"
   
   For each dataset, identify all the individual fields from employee_dsl.yaml that belong to it.

6. **Map test cases to rule IDs** (if mr_dsl.yaml is available): For each test case:
   - Identify which rules from mr_dsl.yaml apply to the test case scenario
   - Extract rule IDs (e.g., "IN-IT-SLAB-OLD-NORMAL-001", "IN-IT-SURCHARGE-001")
   - Verify rule conditions (when clauses) are met by the test case data
   - Verify rule actions (then clauses) are correctly applied in expected results
   - Document the mapping of test cases to rule IDs
   - Create a rule coverage matrix showing which rules are validated by which test cases
   
   **Note**: If mr_dsl.yaml is not available, use your knowledge of Indian tax laws to ensure compliance.

7. **Generate test case files**: Create test case files in CSV format:
   - **Input CSV**: Contains all fields from input datasets - all employee data that serves as input to the payroll system
   - **Output CSV**: Contains all fields from output datasets - all expected output data from the payroll system (e.g., tax forecasts, payslips)
   - **Combined CSV**: Contains both input and output fields in a single file for comprehensive reference
   
   **Dataset representation in CSV**:
   - Each dataset requirement must be fully represented with all its constituent fields
   - For time-based datasets (e.g., monthly data), use appropriate column naming (e.g., `april_bonus`, `december_bonus`, `march_bonus`) or create separate columns for each time period
   - Ensure all fields from a dataset are included when that dataset is required
   - Handle period-based, moment-based, and timeless fields appropriately based on the schema
   
   All test case files (CSV) should:
   - Contain exactly 50 employees (hardcoded requirement)
   - Cover all test cases extracted from Use_Cases.md (some employees may cover multiple use cases)
   - **Note**: The LLM is free to generate in multiple tries if it's too much, but ensure the total across all sessions equals 50 employees
   - Satisfy all necessary dataset requirements extracted from Data_requirements.md (with all their constituent fields)
   - Include optional dataset requirements where applicable (with all their constituent fields)
   - Use valid field names from the employee_dsl.yaml schema
   - Contain realistic data values appropriate for each test case scenario
   - Properly structure datasets that span multiple time periods (e.g., monthly data for April, December, March)
   - Include step-by-step calculation documentation showing all intermediate steps
   - Reference specific rule IDs where applicable

## CSV Format Requirements

These requirements apply to all generated CSV files (input, output, and combined):

- **Header row**: Include all relevant fields from the employee schema that are needed for the test cases
  - For input CSV: Include all fields from all input datasets (map each dataset requirement to its constituent fields)
  - For output CSV: Include all fields from all output datasets
  - For combined CSV: Include all fields from both input and output datasets
  - For time-based datasets, use appropriate column naming (e.g., `april_bonus`, `december_bonus`, `march_bonus` for monthly bonus data)
- **Data rows**: Each row represents one employee with their complete data
- **Field values**: 
  - Use appropriate data types (strings, numbers, dates, booleans)
  - Dates should be in YYYY-MM-DD format
  - Money values should be numeric (in Indian Rupees)
  - Boolean values should be true/false
  - Empty/null values should be left blank or use appropriate null representation
- **Consistency**: Ensure employee IDs and order are consistent across all CSV files

## Test Case Coverage

**Extract from Use_Cases.md**: Read the `Use_Cases.md` file and identify all test cases listed in the table format. Each test case includes:
- Test Case ID (column 1)
- Persona/Scenario Description (column 2)
- Key Data Points (column 3)

Ensure all test cases extracted from `Use_Cases.md` are represented in your employee records. Some employees may satisfy multiple test cases, which is acceptable and encouraged for efficiency.

## Data Requirements Checklist

**Extract from Data_requirements.md**: Read the `Data_requirements.md` file and extract the requirements table. For each requirement row:
- Identify the dataset requirement description (column 1) - remember each is a dataset, not a single field
- Note whether it's Input or Output (column 2)
- Note whether it's Necessary or Optional (column 3)
- Map the dataset to its constituent fields from employee_dsl.yaml

Create a comprehensive checklist from the extracted dataset requirements and ensure:
- All dataset requirements marked as "Necessary" are included for all employees (with ALL their constituent fields)
- All dataset requirements marked as "Optional" are included for at least some employees (as specified in the requirements, with ALL their constituent fields)
- The total number of employees is exactly 50 (hardcoded requirement)
- Each dataset is fully represented with all its fields (e.g., "Monthly Payslip Data" includes all payslip-related fields for the required months)
- **Note**: If generating in multiple chat sessions, coordinate to ensure exactly 50 employees total across all sessions

## Output Format

Generate test case files in CSV format:

### CSV Files

Generate the following CSV files as specified in Data_requirements.md:

#### 1. Master Summary CSV
- **Filename**: `test_cases_master_summary.csv`
- **Columns**: Test ID, Employee Name, Age, Tax Regime, City, Gross Income, Taxable Income, Tax Breakdown, Final Tax, Key Features, Rules Applied, Status
- **Purpose**: High-level overview of all test cases for quick reference
- **Rows**: One row per test case (plus header row)

#### 2. Annual Input CSV (One CSV)
- **Filename**: `annual_employee_input_data.csv` (or similar descriptive name)
- **Content**: Annual CTC breakdown Data, demographics data, tax information and investment declaration of employees
- **Minimum Required Columns** (must include, but list is not exhaustive - some employees may not have values for all columns):
  - ID, Age, Parents' age, No. of Children, residency, city, city_type, employment_type, tax_regime, owns_house_in_work_city, joining date
  - annual ctc, gross salary, basic salary
  - hra received, special allowance, transport allowance, conveyance allowance, meal allowance, leave travel allowance
  - children education allowance, children hostel allowance, books and periodical allowance, telephone allowance
  - bonus, commission
  - employee pf contribution, employer pf contribution, vpf
  - nps employee contribution, nps employer contribution, nps additional contribution
  - section_80c_investments, self_family_premium, parents health insurance premium
  - professional tax paid, income or loss from house property, rent paid
- **Purpose**: Contains all annual employee input data required for payroll processing
- **Rows**: Exactly 50 employee rows (plus header row)
- **Note**: Include all columns listed above. Additional columns from employee_dsl.yaml may be included as needed.

#### 3. Monthly Input CSVs
Generate separate CSV files for monthly input data:

**a) Monthly Bonus and Commission Data (3 months)**
- **Filenames**: 
  - `monthly_bonus_commission_april.csv` (for April 2025)
  - `monthly_bonus_commission_december.csv` (for December 2025)
  - `monthly_bonus_commission_march.csv` (for March 2026)
- **Content**: Monthly bonus and commission data for April 2025, December 2025, and March 2026
- **Columns**: ID, bonus, commission, performance_bonus (and other relevant monthly bonus/commission fields)
- **Rows**: Exactly 50 employee rows (plus header row) for each month
- **Requirement**: Each CSV must have **at least 5 non-zero values** (i.e., at least 5 employees must have bonus or commission in each month)

**b) CTC Revision Data (December 2025)**
- **Filename**: `ctc_revision_december.csv`
- **Content**: CTC revision data for December 2025 month
- **Columns**: ID, revised_annual_ctc, revised_basic_salary, revised_gross_salary, and other revised salary components
- **Rows**: Exactly 3 employee rows (plus header row) - **for exactly 3 employees** as specified in Data_requirements.md

**c) Tax Regime Revision Data (December 2025)**
- **Filename**: `tax_regime_revision_december.csv`
- **Content**: Tax regime revision data for December 2025 month
- **Columns**: ID, previous_tax_regime, new_tax_regime, revision_date, and other relevant fields
- **Rows**: Exactly 2 employee rows (plus header row) - **for exactly 2 employees** as specified in Data_requirements.md

**Note**: Arrears Data is marked as "Later, not to be generated now" - DO NOT generate arrears data files.

#### 4. Annual Output CSV (One CSV)
- **Filename**: `annual_tax_forecast.csv` (or similar descriptive name)
- **Content**: Annual Tax Forecast
- **Minimum Required Columns** (must include, but list is not exhaustive - some employees may not have values for all columns):
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
- **Purpose**: Contains annual tax forecast with detailed calculations
- **Rows**: Exactly 50 employee rows (plus header row)
- **Note**: Include all columns listed above. Output data should correspond to the same employees in the same order as the Annual Input CSV.

#### 5. Monthly Output CSVs (Payslip Data)
Generate separate CSV files for monthly payslip data for 3 months:

- **Filenames**: 
  - `monthly_payslip_april.csv` (for April 2025)
  - `monthly_payslip_december.csv` (for December 2025)
  - `monthly_payslip_march.csv` (for March 2026)

- **Content**: Payslip Data for April 2025, December 2025, and March 2026
- **Minimum Required Columns** for each month (must include, but list is not exhaustive - some employees may not have values for all columns):
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
- **Purpose**: Contains monthly payslip data with detailed calculations for each month
- **Rows**: Exactly 50 employee rows (plus header row) for each month
- **Note**: Each month's payslip should correspond to the same employees in the same order. Include step-by-step calculation breakdown in the columns.

### Additional Files

#### Rule-to-Test-Case Mapping Document
- **Filename**: `test_case_rule_mapping.md` or `test_case_rule_mapping.csv`
- **Content**: 
  - Mapping of test cases to rule IDs from mr_dsl.yaml (if available)
  - Which rules apply to each test case
  - Rule coverage matrix showing which rules are validated by which test cases
  - Missing rule coverage identification

#### Test Case Mapping Document
- **Filename**: `test_case_mapping.md`
- **Content**:
  - Which employees correspond to which test cases (using Test Case IDs from Use_Cases.md)
  - Which employees cover multiple test cases
  - Any special notes about specific test scenarios
  - Cross-reference to CSV rows

## File Path Handling

When processing this prompt:
- **If a filepath is provided**: Use that directory as the source for input files
- **If no filepath is provided**: Use the directory where this prompt file is located as the source for input files
- Read all three files (employee_dsl.yaml, Data_requirements.md, Use_Cases.md) from the source directory
- **Create an output directory**: Generate a new folder named `output_{timestamp}` where `{timestamp}` is the current timestamp in format `YYYYMMDD_HHMMSS` (e.g., `output_20250115_143022`)
- Generate all CSV output files in the output directory (not in the source directory)
- Ensure all file paths are handled dynamically based on the provided or default directory path

## Example Command Usage

**Scenario 1: Filepath provided**
If the user provides a filepath like: `/path/to/India_test_case_generation/`

You should:
1. Read `/path/to/India_test_case_generation/employee_dsl.yaml`
2. Read `/path/to/India_test_case_generation/Data_requirements.md`
3. Read `/path/to/India_test_case_generation/Use_Cases.md`
4. Create output directory: `/path/to/India_test_case_generation/output_20250115_143022/` (with current timestamp)
5. Generate the following files in the output directory:
   - Master Summary CSV: `test_cases_master_summary.csv`
   - Annual Input CSV: `annual_employee_input_data.csv`
   - Monthly Input CSVs: `monthly_bonus_commission_april.csv`, `monthly_bonus_commission_december.csv`, `monthly_bonus_commission_march.csv`, `ctc_revision_december.csv`, `tax_regime_revision_december.csv`
   - Annual Output CSV: `annual_tax_forecast.csv`
   - Monthly Output CSVs: `monthly_payslip_april.csv`, `monthly_payslip_december.csv`, `monthly_payslip_march.csv`
   - Rule-to-Test-Case Mapping: `test_case_rule_mapping.md` or `.csv` (if mr_dsl.yaml is available)
   - Test Case Mapping: `test_case_mapping.md`

**Scenario 2: No filepath provided**
If no filepath is provided, use the directory where this prompt file is located.

For example, if the prompt is at: `/path/to/India_test_case_generation/prompt.md`

You should:
1. Read `/path/to/India_test_case_generation/employee_dsl.yaml`
2. Read `/path/to/India_test_case_generation/Data_requirements.md`
3. Read `/path/to/India_test_case_generation/Use_Cases.md`
4. Create output directory: `/path/to/India_test_case_generation/output_20250115_143022/` (with current timestamp)
5. Generate the following files in the output directory:
   - Master Summary CSV: `test_cases_master_summary.csv`
   - Annual Input CSV: `annual_employee_input_data.csv`
   - Monthly Input CSVs: `monthly_bonus_commission_april.csv`, `monthly_bonus_commission_december.csv`, `monthly_bonus_commission_march.csv`, `ctc_revision_december.csv`, `tax_regime_revision_december.csv`
   - Annual Output CSV: `annual_tax_forecast.csv`
   - Monthly Output CSVs: `monthly_payslip_april.csv`, `monthly_payslip_december.csv`, `monthly_payslip_march.csv`
   - Rule-to-Test-Case Mapping: `test_case_rule_mapping.md` or `.csv` (if mr_dsl.yaml is available)
   - Test Case Mapping: `test_case_mapping.md`

## Calculation Transparency Requirements

All test cases must include comprehensive calculation documentation showing:

1. **Step-by-Step Breakdown**:
   - Document every intermediate calculation step
   - Show formulas used for each calculation
   - Display all threshold checks and conditions
   - Include all rounding and precision handling

2. **Gross to Net Computation**:
   - Start with gross salary components
   - Show each exemption applied with formula and amount
   - Show each deduction applied with limit checks
   - Calculate taxable income step-by-step

3. **Exemption Calculations**:
   - HRA exemption: Show all three calculations (actual rent paid, 50%/40% of basic, actual HRA received) and minimum
   - Conveyance allowance: Show exemption limit application
   - LTA: Show exemption calculation and conditions
   - Other allowances: Show exemption formulas and limits

4. **Deduction Itemization**:
   - Section 80C: Show all components and aggregate limit
   - Section 80D: Show self, family, and parents' premiums with limits
   - Section 80G: Show eligible donations and limits
   - Other deductions: Show each deduction with applicable limits

5. **Tax Slab Breakdown**:
   - Show income falling in each tax slab
   - Calculate tax for each slab separately
   - Show progressive tax calculation
   - Display cumulative tax at each slab

6. **Surcharge and Cess**:
   - Show surcharge calculation based on income thresholds
   - Show health and education cess calculation
   - Display total tax including surcharge and cess

7. **Final Tax Liability**:
   - Show rebates applied (e.g., Section 87A)
   - Show final tax after rebates
   - Calculate monthly TDS/withholding
   - Show annual tax forecast

8. **Mathematical Verification**:
   - Verify all additions and subtractions
   - Verify percentage calculations
   - Verify rounding at each step
   - Cross-verify final tax with manual calculation

**Documentation Format**: Include these calculations in:
- Detailed Output CSV columns (with step-by-step breakdown columns)
- Separate calculation documentation file (if needed)

## Validation Requirements

Before finalizing all test case files, perform the following validations:

### Rule Validation (if mr_dsl.yaml is available):
- **All applicable rules are triggered**: Verify that for each test case, all relevant rules from mr_dsl.yaml are identified and applied
- **Rule conditions are met**: Verify that all "when" clauses in applicable rules are satisfied by the test case data
- **Rule actions are applied correctly**: Verify that all "then" clauses in applicable rules are correctly implemented in the expected results
- **Rule ID mapping**: Document which rule IDs apply to each test case in the rule-to-test-case mapping document
- **Rule coverage**: Ensure comprehensive coverage of rules - identify any rules that are not covered by any test case

### Calculation Validation:
- **Mathematical accuracy verified**: All calculations must be mathematically correct
  - Verify addition, subtraction, multiplication, division
  - Verify percentage calculations
  - Verify rounding rules
  - Cross-check totals and subtotals

- **Boundary conditions tested**: Test cases must include:
  - Values at exact thresholds (e.g., exactly ₹12L for rebate threshold)
  - Values just below thresholds
  - Values just above thresholds
  - Maximum limit cases (e.g., maximum deduction limits)
  - Minimum value cases

- **Formula application verified**: 
  - HRA exemption formula correctly applied
  - Tax slab calculations follow progressive structure
  - Surcharge calculations at correct thresholds
  - Cess calculations on correct base

### Data Validation:
- **Input data consistency**: Verify that input data is internally consistent
- **Output data consistency**: Verify that output data logically follows from input data
- **Cross-file consistency**: Verify that data is consistent across CSV files and mapping documents

### Compliance Validation:
- **Tax law compliance**: All calculations comply with Indian Income Tax Act
- **Regulation compliance**: All deductions, exemptions, and allowances comply with current regulations
- **Limit compliance**: All amounts are within legal limits for each category

## Quality Assurance

Before finalizing all test case files (CSV):
- Verify all CSV files are generated:
  - Master Summary CSV
  - Annual Input CSV (with all minimum required columns)
  - Monthly Input CSVs (3 bonus/commission files with at least 5 non-zero values each + 1 CTC revision file for 3 employees + 1 tax regime revision file for 2 employees)
  - Annual Output CSV (with all minimum required columns)
  - Monthly Output CSVs (3 payslip files with all minimum required columns)
- Verify Arrears Data is NOT generated (marked as "Later, not to be generated now")
- Verify exactly 50 employees are included in all files (or coordinate across multiple chat sessions to total 50)
- Verify all test cases extracted from Use_Cases.md are covered
- Verify all necessary dataset requirements extracted from Data_requirements.md are met (with ALL their constituent fields)
- Verify each dataset requirement is fully represented with all its fields from employee_dsl.yaml
- Verify time-based datasets (e.g., monthly data) are properly structured with columns for each required time period
- Verify input CSV contains only fields from input datasets (no output dataset fields)
- Verify output CSV contains only fields from output datasets (no input dataset fields)
- Verify combined CSV contains fields from both input and output datasets
- Verify employee order and IDs are consistent across all CSV files
- Verify data types match the schema definitions
- Verify realistic data values for each scenario
- Verify date ranges are appropriate (FY 2025-26)
- **Verify all tax calculations are compliant with Indian Income Tax Act and current tax rules**
- **Verify all deductions, exemptions, and allowances comply with Indian tax regulations**
- **Verify all amounts, percentages, and thresholds align with current Indian tax laws**
- **Verify tax slabs, surcharges, and cess are accurate for the assessment year**
- Verify output data logically corresponds to input data for each employee
- **Verify mathematical accuracy of all calculations**
- **Verify step-by-step calculation documentation is included in Detailed Output CSV**
- **Verify rule IDs are referenced where applicable**
- **Verify rule-to-test-case mapping document is created**
- **Verify boundary conditions are tested**
- **Verify all applicable rules are triggered and validated**

## Indian Tax Law and Income Rule Compliance

**CRITICAL REQUIREMENT**: All test case data must be fully compliant with Indian tax laws and income tax rules and regulations. This is a non-negotiable requirement.

### Compliance Requirements:

1. **Tax Calculations**: 
   - All tax calculations must follow current Indian Income Tax Act provisions
   - Tax slabs, rates, surcharges, and cess must be accurate for the assessment year
   - Rebates (e.g., Section 87A) must be calculated correctly based on income thresholds
   - Marginal relief calculations must be accurate where applicable

2. **Deductions and Exemptions**:
   - Section 80C, 80D, 80G, HRA, LTA, and all other deductions must comply with current limits and rules
   - Exemption calculations (HRA, conveyance, etc.) must follow the correct formulas and limits
   - Investment declarations must be within legal limits for each section

3. **Allowances**:
   - All allowances must comply with Indian tax exemption rules
   - Conveyance allowance exemption limits must be respected
   - Children education allowance, hostel allowance limits must be correct
   - Other allowances must follow current exemption rules

4. **Income Components**:
   - Salary structure must be realistic and compliant
   - Bonus, commission, and other income components must follow tax treatment rules
   - Arrears and advance salary must be handled per Indian tax rules

5. **Special Cases**:
   - Senior citizen benefits and deductions must be correctly applied
   - NRI tax treatment must follow residency rules
   - Professional tax must comply with state-specific rules
   - Section 89 relief calculations must be accurate

6. **Data Accuracy**:
   - Every number, calculation, and data point must be mathematically correct
   - Taxable income calculations must be accurate
   - All percentages, amounts, and thresholds must align with current Indian tax laws
   - Output data (tax forecasts, payslips) must be consistent with input data and tax rules

**Use your knowledge of Indian Income Tax Act, Finance Act provisions, and current tax rules to ensure complete compliance. If uncertain about any rule or calculation, research or use conservative estimates that align with Indian tax regulations.**

## Notes

- Some employees may satisfy multiple test cases
- Ensure data consistency across months for the same employee
- Use realistic Indian names, PAN numbers, and addresses
- Ensure tax regime selections align with the test case requirements
- Include appropriate variations in income levels, deductions, and exemptions
- Consider edge cases and boundary conditions mentioned in the use cases
- **All data must be compliant with Indian tax laws - verify every calculation and amount**

---

**Ready to generate**: Once you have read all three files from the provided directory (or the directory where this prompt is located if no directory is provided), proceed to:
1. Create the output directory `output_{timestamp}` in the source directory
2. Generate the comprehensive CSV test case files for **exactly 50 employees**:
   - Master Summary CSV
   - Annual Input CSV (with all minimum required columns from Data_requirements.md)
   - Monthly Input CSVs (bonus/commission for April 2025, December 2025, March 2026 with at least 5 non-zero values per CSV + CTC revision for December 2025 for 3 employees + tax regime revision for December 2025 for 2 employees)
   - Note: Monthly bonus/commission CSVs must have at least 5 non-zero values each. CTC revision CSV must have exactly 3 employees. Tax regime revision CSV must have exactly 2 employees.
   - Annual Output CSV (Annual Tax Forecast with all minimum required columns from Data_requirements.md)
   - Monthly Output CSVs (payslip data for April 2025, December 2025, March 2026 with all minimum required columns from Data_requirements.md)
4. Create rule-to-test-case mapping document (if mr_dsl.yaml is available)
5. Create test case mapping document
6. Follow all the requirements above including calculation transparency and validation requirements
7. **Important**: Do NOT generate Arrears Data files (marked as "Later, not to be generated now" in Data_requirements.md)

**Note on Task Size**: Generating 50 employees with all required data is substantial. You are free to split this work across multiple tries if it's too much. If doing so:
- First try: Generate a subset of employees covering a portion of the test cases
- Subsequent tries: Generate the remaining employees covering the remaining test cases
- Ensure consistency in data format, employee IDs (e.g., EMP001-EMP025 in first try, EMP026-EMP050 in subsequent tries), and file structure across all sessions
- All sessions should generate all required CSV files, but with their respective employee subsets

