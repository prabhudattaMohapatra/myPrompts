# Code Review Checklist

Use this prompt when asking an AI or a reviewer to perform a structured code review. Paste it with the files or PR you want reviewed.

---

## Role

You are an experienced engineer performing a thorough code review. Apply this checklist systematically and report pass/fail or N/A with brief notes for each item.

## Scope

Review the provided code changes (diff, files, or PR) against the following. Focus on the changed/added code; mention existing code only when it affects correctness or safety of the new changes.

## Checklist

### Correctness & logic

- [ ] **Intent**: The code does what the ticket/PR description says; no unintended behaviour.
- [ ] **Edge cases**: Null/empty, boundary values, and error paths are handled.
- [ ] **Data flow**: Inputs are validated or sanitized where needed; outputs are consistent with contracts (API, types, schema).
- [ ] **Concurrency**: No obvious race conditions, deadlocks, or shared mutable state issues (if applicable).

### Design & structure

- [ ] **Single responsibility**: Functions/classes have a clear, focused purpose.
- [ ] **Dependencies**: New dependencies are justified; no unnecessary coupling.
- [ ] **Reuse**: Existing utilities/patterns are used where appropriate; no duplicated logic that should be shared.
- [ ] **Naming**: Names are clear and consistent with the rest of the codebase.

### Security & safety

- [ ] **Inputs**: User/external input is not trusted blindly; validation/sanitization or parameterization is used where relevant.
- [ ] **Secrets**: No secrets, API keys, or credentials in code or logs.
- [ ] **Sensitive data**: PII/sensitive data is not logged or exposed in error messages.

### Testing & maintainability

- [ ] **Tests**: New or changed behaviour is covered by tests (unit/integration as appropriate).
- [ ] **Readability**: Logic is readable without excessive comments; complex logic has a short explanation.
- [ ] **Documentation**: Public APIs, config, or non-obvious behaviour are documented where needed.

### Project standards

- [ ] **Style**: Code follows project style (lint/format) and conventions.
- [ ] **Build/CI**: Changes do not break build or existing tests; new warnings are addressed or explicitly accepted.

## Output

Provide a short summary (overall assessment, main risks, and top 1–3 suggestions), then go through the checklist with a one-line note per item (e.g. “Pass”, “Fail: …”, “N/A: …”).
