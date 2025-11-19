# Test Case Generation Prompt for Indian Payroll Engine (with DSL Rules)

## ROLE
You are an expert tax consultant and test engineer specializing in Indian tax law and payroll systems.

## TASK
Generate comprehensive test cases for validating the Indian Payroll Engine for assessment year 2025-26. The test cases must satisfy specific data requirements and cover all defined use cases, while ensuring full compliance with Indian tax laws and regulations.

## TARGET USERS
- Payroll administrators
- Tax professionals
- System developers

## PURPOSE
Validate tax calculations against official Indian tax regulations and ensure the payroll engine correctly implements all tax rules, exemptions, deductions, and compliance requirements as defined in the machine-readable DSL rules.

## Context

You will be provided with the following files in the same directory:
- **employee_dsl.yaml**: Contains the complete input schema definition for employee data structure with all available input fields
- **mr_dsl.yaml**: Contains machine-readable DSL rules for Indian payroll and taxation - use this as a **minimum but not exhaustive** rule set for compliance
- **Data_requirements.md**: Specifies the data requirements including number of employees, input/output requirements, and necessity levels
- **Use_Cases.md**: Lists all test case scenarios that must be covered with their specific requirements

## Instructions

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
   - Total number of employees needed (extract from the file)
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
   
   Map each extracted test case to specific employee records, ensuring all scenarios are covered.

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
   
   Create a mapping document showing which schema fields correspond to each dataset requirement.

6. **Separate input and output datasets**: Based on the requirements extracted from Data_requirements.md:
   - **Input datasets**: All datasets marked as "Input" (both Necessary and Optional)
   - **Output datasets**: All datasets marked as "Output"
   
   For each dataset, identify all the individual fields from employee_dsl.yaml that belong to it.

7. **Map test cases to rule IDs**: For each test case, you MUST:
   - Identify which rules from `mr_dsl.yaml` apply to the test case scenario
   - Extract rule IDs (e.g., "IN-IT-SLAB-OLD-NORMAL-001", "IN-IT-SURCHARGE-001")
   - Verify rule conditions (when clauses) are met by the test case data
   - Verify rule actions (then clauses) are correctly applied in expected results
   - Document the mapping of test cases to rule IDs
   - Create a rule coverage matrix showing which rules are validated by which test cases
   - Ensure comprehensive coverage of rules - identify any rules that are not covered by any test case

8. **Generate test case files**: Create test case files in both YAML and CSV formats:
   - **Input CSV**: Contains all fields from input datasets - all employee data that serves as input to the payroll system
   - **Output CSV**: Contains all fields from output datasets - all expected output data from the payroll system (e.g., tax forecasts, payslips)
   - **Combined CSV**: Contains both input and output fields in a single file for comprehensive reference
   
   **Dataset representation in CSV**:
   - Each dataset requirement must be fully represented with all its constituent fields
   - For time-based datasets (e.g., monthly data), use appropriate column naming (e.g., `april_bonus`, `december_bonus`, `march_bonus`) or create separate columns for each time period
   - Ensure all fields from a dataset are included when that dataset is required
   - Handle period-based, moment-based, and timeless fields appropriately based on the schema
   
   All test case files (YAML and CSV) should:
   - Contain the exact number of employees specified in Data_requirements.md
   - Cover all test cases extracted from Use_Cases.md (some employees may cover multiple use cases)
   - Satisfy all necessary dataset requirements extracted from Data_requirements.md (with all their constituent fields)
   - Include optional dataset requirements where applicable (with all their constituent fields)
   - Use valid field names from the employee_dsl.yaml schema
   - Contain realistic data values appropriate for each test case scenario
   - Properly structure datasets that span multiple time periods (e.g., monthly data for April, December, March)
   - Include step-by-step calculation documentation showing all intermediate steps
   - Reference specific rule IDs from mr_dsl.yaml
   - **Be fully compliant with rules in mr_dsl.yaml and additional Indian tax laws**

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
- The total number of employees matches the number specified in Data_requirements.md
- Each dataset is fully represented with all its fields (e.g., "Monthly Payslip Data" includes all payslip-related fields for the required months)

## Output Format

Generate test case files in both YAML and CSV formats:

### YAML Test Case Files

Generate individual YAML test case files for each test case scenario:

- **Naming Convention**: `TC-##_ScenarioDescription.yaml` (e.g., `TC-01_NewRegimeBelowExemption.yaml`, `TC-02_OldRegimeMultipleDeductions.yaml`)
- **Count**: One YAML file per test case from Use_Cases.md
- **Structure**: Each YAML file must include:
  
  **a) Metadata Section:**
  - Type, version, jurisdiction, effective date, description
  - Test Case ID and scenario name
  - Rules applied (list of rule IDs from mr_dsl.yaml - MANDATORY)
  
  **b) Employee Profile:**
  - Personal details (name, age, PAN/tax ID, DOB, gender)
  - Location (state, city, residency status)
  - Employment details (type, status, employer type, service years)
  - Tax regime selection
  
  **c) Income Components:**
  - Salary breakdown (basic, HRA/housing, allowances, bonuses)
  - Other income sources (rental, interest, capital gains)
  - Investment details
  - Deduction claims
  
  **d) Expected Results (in comments):**
  - Step-by-step calculation breakdown
  - Gross to net computation
  - All exemptions applied (with formulas)
  - All deductions itemized
  - Tax slab breakdown
  - Surcharge and cess calculations (if applicable)
  - Final tax liability derivation
  - Monthly TDS/withholding
  - Rule IDs referenced for each calculation step

### CSV Files

Generate the following CSV files:

#### 1. Master Summary CSV
- **Filename**: `test_cases_master_summary.csv`
- **Columns**: Test ID, Employee Name, Age, Tax Regime, City, Gross Income, Taxable Income, Tax Breakdown, Final Tax, Key Features, Rules Applied, Status
- **Purpose**: High-level overview of all test cases for quick reference
- **Rows**: One row per test case (plus header row)

#### 2. Detailed Input CSV
- **Filename**: `indian_payroll_test_cases_input.csv` (or similar descriptive name)
- **Content**: All fields from input datasets extracted from Data_requirements.md (marked as "Input")
  - Each input dataset requirement must be fully represented with all its constituent fields from employee_dsl.yaml
  - For time-based datasets (e.g., monthly bonus data), include columns for each required time period
  - Should contain 30-40 columns covering all employee attributes, salary components, investments, deductions
- **Purpose**: Contains all employee input data required for payroll processing
- **Rows**: The exact number of employee rows as specified in Data_requirements.md (plus header row)

#### 3. Detailed Output CSV
- **Filename**: `indian_payroll_test_cases_output.csv` (or similar descriptive name)
- **Content**: All fields from output datasets extracted from Data_requirements.md (marked as "Output")
  - Each output dataset requirement must be fully represented with all its constituent fields
  - For time-based datasets (e.g., monthly payslip data), include columns for each required time period
  - Should contain 40+ columns with step-by-step calculation breakdown:
    - Gross income components
    - Exemptions applied (with amounts)
    - Deductions itemized
    - Taxable income calculation
    - Tax slab-wise breakdown
    - Surcharge and cess
    - Final tax liability
    - Monthly TDS/withholding
    - Rule IDs applied at each step
- **Purpose**: Contains all expected output data from the payroll system with detailed calculations
- **Rows**: The exact number of employee rows as specified in Data_requirements.md (plus header row)
- **Note**: Output data should correspond to the same employees in the same order as the input CSV

#### 4. Combined CSV File
- **Filename**: `indian_payroll_test_cases_combined.csv` (or similar descriptive name)
- **Content**: Both input and output fields from all datasets in a single file
  - All fields from all input datasets
  - All fields from all output datasets
- **Purpose**: Comprehensive reference file with all data together
- **Rows**: The exact number of employee rows as specified in Data_requirements.md (plus header row)

### Additional Files

#### Rule-to-Test-Case Mapping Document (MANDATORY)
- **Filename**: `test_case_rule_mapping.md` or `test_case_rule_mapping.csv`
- **Content**: 
  - Mapping of test cases to rule IDs from mr_dsl.yaml (MANDATORY - all applicable rules must be mapped)
  - Which rules apply to each test case
  - Rule coverage matrix showing which rules are validated by which test cases
  - Missing rule coverage identification
  - Verification that rule conditions (when clauses) are met
  - Verification that rule actions (then clauses) are applied

#### Test Case Mapping Document
- **Filename**: `test_case_mapping.md`
- **Content**:
  - Which employees correspond to which test cases (using Test Case IDs from Use_Cases.md)
  - Which employees cover multiple test cases
  - Any special notes about specific test scenarios
  - Cross-reference to YAML files and CSV rows

## File Path Handling

When processing this prompt:
- **If a filepath is provided**: Use that directory as the source for input files
- **If no filepath is provided**: Use the directory where this prompt file is located as the source for input files
- Read all four files (employee_dsl.yaml, mr_dsl.yaml, Data_requirements.md, Use_Cases.md) from the source directory
- **Create an output directory**: Generate a new folder named `output_with_dsl_{timestamp}` where `{timestamp}` is the current timestamp in format `YYYYMMDD_HHMMSS` (e.g., `output_with_dsl_20250115_143022`)
- Generate all CSV output files in the output directory (not in the source directory)
- Ensure all file paths are handled dynamically based on the provided or default directory path

## Example Command Usage

**Scenario 1: Filepath provided**
If the user provides a filepath like: `/path/to/India_test_case_generation/`

You should:
1. Read `/path/to/India_test_case_generation/employee_dsl.yaml`
2. Read `/path/to/India_test_case_generation/mr_dsl.yaml`
3. Read `/path/to/India_test_case_generation/Data_requirements.md`
4. Read `/path/to/India_test_case_generation/Use_Cases.md`
5. Create output directory: `/path/to/India_test_case_generation/output_with_dsl_20250115_143022/` (with current timestamp)
6. Generate the following files in the output directory:
   - YAML test case files: `TC-01_*.yaml`, `TC-02_*.yaml`, etc. (one per test case from Use_Cases.md)
   - Master Summary CSV: `test_cases_master_summary.csv`
   - Detailed Input CSV: `indian_payroll_test_cases_input.csv`
   - Detailed Output CSV: `indian_payroll_test_cases_output.csv`
   - Combined CSV: `indian_payroll_test_cases_combined.csv`
   - Rule-to-Test-Case Mapping: `test_case_rule_mapping.md` or `.csv` (MANDATORY)
   - Test Case Mapping: `test_case_mapping.md`

**Scenario 2: No filepath provided**
If no filepath is provided, use the directory where this prompt file is located.

For example, if the prompt is at: `/path/to/India_test_case_generation/prompt_with_dsl.md`

You should:
1. Read `/path/to/India_test_case_generation/employee_dsl.yaml`
2. Read `/path/to/India_test_case_generation/mr_dsl.yaml`
3. Read `/path/to/India_test_case_generation/Data_requirements.md`
4. Read `/path/to/India_test_case_generation/Use_Cases.md`
5. Create output directory: `/path/to/India_test_case_generation/output_with_dsl_20250115_143022/` (with current timestamp)
6. Generate the following files in the output directory:
   - YAML test case files: `TC-01_*.yaml`, `TC-02_*.yaml`, etc. (one per test case from Use_Cases.md)
   - Master Summary CSV: `test_cases_master_summary.csv`
   - Detailed Input CSV: `indian_payroll_test_cases_input.csv`
   - Detailed Output CSV: `indian_payroll_test_cases_output.csv`
   - Combined CSV: `indian_payroll_test_cases_combined.csv`
   - Rule-to-Test-Case Mapping: `test_case_rule_mapping.md` or `.csv` (MANDATORY)
   - Test Case Mapping: `test_case_mapping.md`

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
- YAML file comments (Expected Results section) with rule ID references
- Detailed Output CSV columns with rule ID columns
- Separate calculation documentation file (if needed)

## Validation Requirements

Before finalizing all test case files, perform the following validations:

### Rule Validation (MANDATORY - mr_dsl.yaml is available):
- **All applicable rules are triggered**: Verify that for each test case, all relevant rules from mr_dsl.yaml are identified and applied
- **Rule conditions are met**: Verify that all "when" clauses in applicable rules are satisfied by the test case data
- **Rule actions are applied correctly**: Verify that all "then" clauses in applicable rules are correctly implemented in the expected results
- **Rule ID mapping**: Document which rule IDs apply to each test case in the rule-to-test-case mapping document (MANDATORY)
- **Rule coverage**: Ensure comprehensive coverage of rules - identify any rules that are not covered by any test case
- **Rule verification**: Cross-verify that calculations match the expected outputs from mr_dsl.yaml rules

### Calculation Validation:
- **Mathematical accuracy verified**: All calculations must be mathematically correct
  - Verify addition, subtraction, multiplication, division
  - Verify percentage calculations
  - Verify rounding rules
  - Cross-check totals and subtotals
  - Verify against mr_dsl.yaml rule outputs

- **Boundary conditions tested**: Test cases must include:
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
- **Cross-file consistency**: Verify that data is consistent across YAML files, CSV files, and mapping documents
- **Rule compliance**: Verify that all calculations comply with mr_dsl.yaml rules

### Compliance Validation:
- **Tax law compliance**: All calculations comply with Indian Income Tax Act
- **DSL rule compliance**: All calculations comply with rules in mr_dsl.yaml
- **Regulation compliance**: All deductions, exemptions, and allowances comply with current regulations
- **Limit compliance**: All amounts are within legal limits for each category (as per mr_dsl.yaml)

## Quality Assurance

Before finalizing all test case files (YAML and CSV):
- Verify all YAML test case files are generated (one per test case from Use_Cases.md)
- Verify all CSV files (Master Summary, Detailed Input, Detailed Output, Combined) are generated
- Verify the exact number of employees specified in Data_requirements.md are included in all files
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
- **Verify all tax calculations comply with rules defined in mr_dsl.yaml**
- **Verify all tax calculations are compliant with Indian Income Tax Act and current tax rules**
- **Verify all deductions, exemptions, and allowances comply with Indian tax regulations and mr_dsl.yaml rules**
- **Verify all amounts, percentages, and thresholds align with current Indian tax laws and mr_dsl.yaml**
- **Verify tax slabs, surcharges, and cess match the definitions in mr_dsl.yaml**
- **Verify rebate calculations (Section 87A) follow rules in mr_dsl.yaml**
- **Verify allowance exemptions follow rules defined in mr_dsl.yaml**
- **Verify deduction limits match those specified in mr_dsl.yaml**
- Verify output data logically corresponds to input data for each employee
- **Verify mathematical accuracy of all calculations**
- **Verify step-by-step calculation documentation is included in YAML files and Detailed Output CSV**
- **Verify rule IDs are referenced in all YAML files and mapping documents (MANDATORY)**
- **Verify rule-to-test-case mapping document is created and comprehensive (MANDATORY)**
- **Verify boundary conditions are tested**
- **Verify all applicable rules from mr_dsl.yaml are triggered and validated**
- **Cross-verify calculations against both mr_dsl.yaml rules and additional Indian tax laws**

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
- **Assessment Year**: Use the effective date and version from mr_dsl.yaml metadata (2025-26) for all calculations

**Priority**: DSL rules take precedence for specific calculations, but you must ensure overall compliance with all Indian tax laws and regulations, even if not explicitly in the DSL.

## Notes

- Some employees may satisfy multiple test cases
- Ensure data consistency across months for the same employee
- Use realistic Indian names, PAN numbers, and addresses
- Ensure tax regime selections align with the test case requirements
- Include appropriate variations in income levels, deductions, and exemptions
- Consider edge cases and boundary conditions mentioned in the use cases
- **All data must be compliant with Indian tax laws and mr_dsl.yaml rules - verify every calculation and amount**
- **When in doubt between DSL rules and general tax knowledge, prioritize DSL rules but ensure overall tax law compliance**

---

**Ready to generate**: Once you have read all four files (employee_dsl.yaml, mr_dsl.yaml, Data_requirements.md, Use_Cases.md) from the provided directory (or the directory where this prompt is located if no directory is provided), proceed to:
1. Create the output directory `output_with_dsl_{timestamp}` in the source directory
2. Generate YAML test case files (one per test case from Use_Cases.md) with comprehensive calculation documentation and rule ID references
3. Generate the comprehensive CSV test case files (Master Summary, Detailed Input, Detailed Output, and Combined) in the output directory
4. Create rule-to-test-case mapping document (MANDATORY - must map all applicable rules from mr_dsl.yaml)
5. Create test case mapping document
6. Follow all the requirements above including calculation transparency, validation requirements, and full compliance with mr_dsl.yaml rules and Indian tax laws

