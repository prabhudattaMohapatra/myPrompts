# Test Case Generation Prompt for Indian Payroll Engine (with DSL Rules)

You are tasked with generating comprehensive test case data in CSV format for the Indian Payroll Engine. The test cases must satisfy specific data requirements and cover all defined use cases, while ensuring full compliance with Indian tax laws and regulations.

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

7. **Generate CSV files**: Create multiple CSV files with test case data:
   - **Input CSV**: Contains all fields from input datasets - all employee data that serves as input to the payroll system
   - **Output CSV**: Contains all fields from output datasets - all expected output data from the payroll system (e.g., tax forecasts, payslips)
   - **Combined CSV**: Contains both input and output fields in a single file for comprehensive reference
   
   **Dataset representation in CSV**:
   - Each dataset requirement must be fully represented with all its constituent fields
   - For time-based datasets (e.g., monthly data), use appropriate column naming (e.g., `april_bonus`, `december_bonus`, `march_bonus`) or create separate columns for each time period
   - Ensure all fields from a dataset are included when that dataset is required
   - Handle period-based, moment-based, and timeless fields appropriately based on the schema
   
   All CSV files should:
   - Contain the exact number of employees specified in Data_requirements.md
   - Cover all test cases extracted from Use_Cases.md (some employees may cover multiple use cases)
   - Satisfy all necessary dataset requirements extracted from Data_requirements.md (with all their constituent fields)
   - Include optional dataset requirements where applicable (with all their constituent fields)
   - Use valid field names from the employee_dsl.yaml schema
   - Contain realistic data values appropriate for each test case scenario
   - Properly structure datasets that span multiple time periods (e.g., monthly data for April, December, March)
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

Generate a minimum of three CSV files:

### 1. Input CSV File
- **Filename**: `indian_payroll_test_cases_input.csv` (or similar descriptive name)
- **Content**: All fields from input datasets extracted from Data_requirements.md (marked as "Input")
  - Each input dataset requirement must be fully represented with all its constituent fields from employee_dsl.yaml
  - For time-based datasets (e.g., monthly bonus data), include columns for each required time period
- **Purpose**: Contains all employee input data required for payroll processing
- **Rows**: The exact number of employee rows as specified in Data_requirements.md (plus header row)

### 2. Output CSV File
- **Filename**: `indian_payroll_test_cases_output.csv` (or similar descriptive name)
- **Content**: All fields from output datasets extracted from Data_requirements.md (marked as "Output")
  - Each output dataset requirement must be fully represented with all its constituent fields
  - For time-based datasets (e.g., monthly payslip data), include columns for each required time period
- **Purpose**: Contains all expected output data from the payroll system
- **Rows**: The exact number of employee rows as specified in Data_requirements.md (plus header row)
- **Note**: Output data should correspond to the same employees in the same order as the input CSV

### 3. Combined CSV File
- **Filename**: `indian_payroll_test_cases_combined.csv` (or similar descriptive name)
- **Content**: Both input and output fields from all datasets in a single file
  - All fields from all input datasets
  - All fields from all output datasets
- **Purpose**: Comprehensive reference file with all data together
- **Rows**: The exact number of employee rows as specified in Data_requirements.md (plus header row)

### Additional Files (if needed)
- Generate additional CSV files if the data structure requires separation (e.g., monthly data files, separate files for different data types)
- Use descriptive filenames that clearly indicate the content and purpose

### Mapping Document
- Create a separate mapping document (e.g., `test_case_mapping.md` or include as comments) indicating:
  - Which employees correspond to which test cases (using Test Case IDs from Use_Cases.md)
  - Which employees cover multiple test cases
  - Any special notes about specific test scenarios

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
6. Generate the following CSV files in the output directory:
   - `/path/to/India_test_case_generation/output_with_dsl_20250115_143022/indian_payroll_test_cases_input.csv`
   - `/path/to/India_test_case_generation/output_with_dsl_20250115_143022/indian_payroll_test_cases_output.csv`
   - `/path/to/India_test_case_generation/output_with_dsl_20250115_143022/indian_payroll_test_cases_combined.csv`
   - Additional files as needed (e.g., mapping document)

**Scenario 2: No filepath provided**
If no filepath is provided, use the directory where this prompt file is located.

For example, if the prompt is at: `/path/to/India_test_case_generation/prompt_with_dsl.md`

You should:
1. Read `/path/to/India_test_case_generation/employee_dsl.yaml`
2. Read `/path/to/India_test_case_generation/mr_dsl.yaml`
3. Read `/path/to/India_test_case_generation/Data_requirements.md`
4. Read `/path/to/India_test_case_generation/Use_Cases.md`
5. Create output directory: `/path/to/India_test_case_generation/output_with_dsl_20250115_143022/` (with current timestamp)
6. Generate the following CSV files in the output directory:
   - `/path/to/India_test_case_generation/output_with_dsl_20250115_143022/indian_payroll_test_cases_input.csv`
   - `/path/to/India_test_case_generation/output_with_dsl_20250115_143022/indian_payroll_test_cases_output.csv`
   - `/path/to/India_test_case_generation/output_with_dsl_20250115_143022/indian_payroll_test_cases_combined.csv`
   - Additional files as needed (e.g., mapping document)

## Quality Assurance

Before finalizing the CSV files:
- Verify all three CSV files (input, output, combined) are generated
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
2. Generate the comprehensive CSV test case files (input, output, and combined) in the output directory following all the requirements above, ensuring full compliance with mr_dsl.yaml rules and Indian tax laws

