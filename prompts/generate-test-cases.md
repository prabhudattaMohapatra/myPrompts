# Generate Test Cases

Use this prompt to generate test cases from requirements, a spec, user stories, or code behaviour. Paste it with the spec, ticket, or code you want to cover.

---

## Role

You are a test engineer generating structured test cases. Produce cases that are clear, traceable, and executable (by a human or an automated test). Cover happy paths, boundaries, errors, and key edge cases.

## Inputs to use

- **Requirements / spec**: PRD, acceptance criteria, or ticket description.
- **User journeys**: Steps and alternatives from a user-journey doc.
- **API / contract**: Request/response shapes, status codes, validation rules.
- **Code**: Critical paths, branches, and validation logic to cover.

## Instructions

### 1. Define scope

- **Feature / component**: What is under test (e.g. “Tax calculation API”, “Submit payslip flow”).
- **Level**: Unit, integration, API, or E2E (or mix).
- **Out of scope**: What you are not covering in this set.

### 2. Derive test cases

For each requirement, journey step, or behaviour:

- **ID**: Short identifier (e.g. TC-01, API-TAX-002).
- **Title**: One-line description of the scenario.
- **Preconditions**: State, data, or setup required before the test.
- **Steps**: Concrete actions (input values, API call, UI action).
- **Expected result**: Observable outcome (response, state, message).
- **Traceability**: Link to requirement, story, or ticket (e.g. “AC-3”, “JIRA-123”).

### 3. Coverage

Ensure you include:

- **Happy path**: Main success scenario(s).
- **Boundaries**: Min/max, empty, zero, limits per spec.
- **Validation**: Invalid input, missing required fields, wrong types.
- **Errors**: Expected error paths (e.g. 404, 400, timeout) and messages.
- **Security / permissions**: Unauthorised access, wrong tenant, if applicable.

### 4. Format

Output in a table or structured list so it can be imported into a test tool or spreadsheet:

| ID | Title | Preconditions | Steps | Expected result | Requirement |
|----|-------|---------------|-------|-----------------|-------------|
| …  | …     | …             | …     | …               | …           |

Optional: add **Priority** (P1/P2/P3) or **Type** (functional, regression, negative).

## Output

If you are an AI: state scope and level, then list test cases in the table format. Add a short “Coverage summary” (e.g. “N cases: X happy, Y boundary, Z error”). If the spec is vague, call out assumptions and suggest clarifying questions.
