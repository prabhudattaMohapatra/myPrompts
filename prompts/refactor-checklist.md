# Refactor Checklist

Use this prompt before or during a refactor to keep behaviour intact and avoid regressions. Paste it and reference the code you are refactoring.

---

## Role

You are an engineer performing or reviewing a refactor. The goal is to improve structure, readability, or maintainability **without changing observable behaviour**. Apply this checklist to plan or validate the refactor.

## Before refactoring

- [ ] **Tests**: Existing tests pass and cover the behaviour you are refactoring. Add tests for unclear or critical paths if missing.
- [ ] **Scope**: You have a clear boundary (file, module, or feature) and a small, incremental plan (avoid one giant refactor).
- [ ] **Baseline**: You know the current inputs, outputs, and side effects of the code you will change.

## During refactoring

- [ ] **One step at a time**: Each step keeps tests green; commit or checkpoint after each logical step.
- [ ] **No behaviour change**: No change to public API, return values, or side effects unless that is an explicit follow-up task.
- [ ] **Naming**: New names are clearer; avoid renaming and logic changes in the same step if possible.

## After refactoring

- [ ] **Tests**: All tests still pass; no tests removed or disabled without a documented reason.
- [ ] **Lint/build**: Lint and build succeed; no new warnings introduced (or they are acknowledged).
- [ ] **Documentation**: Comments and docs reflect the new structure; no stale references to old names or flow.

## Red flags (stop and reassess)

- [ ] **Tests deleted or skipped** to make the refactor “easier”.
- [ ] **Large diff** with both refactor and feature/fix mixed; split into separate commits/PRs.
- [ ] **Unclear behaviour**: If you are unsure whether the old code handled an edge case, add a test first, then refactor.

## Output

If you are an AI: given a refactor plan or diff, report which checklist items are satisfied and which are missing or risky. Suggest one concrete improvement (e.g. “Add a test for X before extracting this function”).
