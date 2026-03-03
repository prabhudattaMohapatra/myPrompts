# myPrompts

Local prompts and checklists for development and review. Use them in Cursor (e.g. by @-mentioning the file or pasting the content) or share with the team.

## Prompts in `prompts/`

### Code & review

| Prompt | Use when |
|--------|----------|
| [code-review-checklist.md](prompts/code-review-checklist.md) | Reviewing a PR or diff: correctness, design, security, tests, standards |
| [code-commit-checklist.md](prompts/code-commit-checklist.md) | Before committing: build, tests, lint, scope, message, traceability |
| [pr-description-checklist.md](prompts/pr-description-checklist.md) | Writing or reviewing a PR description: context, scope, how to review |
| [refactor-checklist.md](prompts/refactor-checklist.md) | Planning or validating a refactor: tests, small steps, no behaviour change |
| [documentation-review-checklist.md](prompts/documentation-review-checklist.md) | Reviewing docs: purpose, audience, accuracy, structure, safety |

### Analysis & requirements

| Prompt | Use when |
|--------|----------|
| [analysis-document-checklist.md](prompts/analysis-document-checklist.md) | Writing or reviewing analysis docs: feasibility, options, impact, conclusions |
| [acceptance-criteria-checklist.md](prompts/acceptance-criteria-checklist.md) | Writing or reviewing acceptance criteria: testable, concrete, complete |
| [user-journeys-discovery.md](prompts/user-journeys-discovery.md) | Finding and documenting user journeys: actors, steps, triggers, alternatives |

### Testing & quality

| Prompt | Use when |
|--------|----------|
| [generate-test-cases.md](prompts/generate-test-cases.md) | Generating test cases from requirements, spec, API, or code |
| [run-tests-and-interpret.md](prompts/run-tests-and-interpret.md) | Running tests and interpreting results: pass/fail, failures, next steps |
| [check-github-pipeline-errors.md](prompts/check-github-pipeline-errors.md) | Checking GitHub Actions failures with `gh`: list runs, view logs, interpret errors |
| [bug-triage-checklist.md](prompts/bug-triage-checklist.md) | Triage: reproducibility, impact, severity, next steps |

## Other content

- **India_test_case_generation/** — Test case generation and verification prompts for the Indian payroll engine.
