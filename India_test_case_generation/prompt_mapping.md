# Employee to Test Case Mapping Prompt

## ROLE
You are a test engineer specializing in test case planning and organization for Indian payroll systems.

## TASK
Before generating the actual test case data, create a mapping document that assigns each of the 30 employees (EMP001 through EMP030) to one or more test case numbers from Use_Cases.md.

## Instructions

1. **Read Use_Cases.md**: Read the file to understand all available test cases (TC-01 through TC-38).

2. **Create the mapping**: Generate a markdown file named `employee_test_case_mapping.md` that contains:
   - A table mapping each employee ID (EMP001-EMP030) to one or more test case IDs
   - Ensure all test cases from Use_Cases.md are covered across the 30 employees
   - Some employees may cover multiple test cases (e.g., an employee can satisfy both TC-01 and TC-05)
   - The mapping should be logical and ensure comprehensive test coverage

3. **Output format**: Create a markdown file with the following structure:
   ```markdown
   # Employee to Test Case Mapping
   
   ## Assessment Year: 2026-27
   ## Total Employees: 30
   
   | Employee ID | Test Case IDs | Notes |
   | --- | --- | --- |
   | EMP001 | TC-01, TC-05 | New regime with multiple deductions |
   | EMP002 | TC-02 | New regime rebate threshold |
   | ... | ... | ... |
   | EMP030 | TC-38 | Grossing up components |
   
   ## Coverage Summary
   - Total Test Cases Covered: [count]
   - Employees with Single Test Case: [count]
   - Employees with Multiple Test Cases: [count]
   ```

4. **File location**: Save the file as `employee_test_case_mapping.md` in the same directory where this prompt is located (or in the provided directory if specified).

5. **Next step**: After generating this mapping file, use the main prompt (`prompt.md` or `prompt_with_dsl.md`) to generate the actual test case data, ensuring that each employee's data aligns with their assigned test case(s) from this mapping.

## Important Notes

- **Assessment Year**: 2026-27
- **Total Employees**: 30 (EMP001 through EMP030)
- **Coverage**: All test cases from Use_Cases.md must be covered at least once
- **Flexibility**: An employee can cover multiple test cases if the scenarios are compatible
- **Priority**: Focus on covering all test cases rather than evenly distributing employees

## Ready to Generate

Once you have read `Use_Cases.md`, proceed to:
1. Create the `employee_test_case_mapping.md` file
2. Map all 30 employees to test cases ensuring complete coverage
3. Include a coverage summary at the end

