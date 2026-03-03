# Pull Request Description Checklist

Use this prompt when drafting or reviewing a PR description. Ensures the PR has enough context for reviewers and future readers.

---

## Role

You are helping the author write a clear, complete PR description. Apply this checklist to the PR title and description (or draft them from the checklist).

## PR title

- [ ] Short and descriptive (e.g. “fix: handle empty regulation list in engine” or “feat: add France withholding tax loader”).
- [ ] Prefixed with type if the project uses it: `fix:`, `feat:`, `chore:`, `docs:`, `refactor:`, etc.

## PR description checklist

### Context

- [ ] **What**: One or two sentences on what this PR does (feature, fix, refactor).
- [ ] **Why**: Why the change is needed (bug, requirement, tech debt, dependency).
- [ ] **Ticket**: Link or ID to the ticket/issue (e.g. NOVACORE-12345), if applicable.

### Scope

- [ ] **In scope**: List main areas touched (e.g. “Lambda handler”, “France regulation API”, “tests”).
- [ ] **Out of scope**: Call out anything that might be expected but is not in this PR (e.g. “UI not changed”, “deploy pipeline in follow-up”).

### How to review

- [ ] **Suggested focus**: Point reviewers to 1–3 files or decisions that need careful review.
- [ ] **Testing**: How to run tests or verify locally (commands or link to CI).

### Risks & follow-ups

- [ ] **Breaking changes**: Called out if any (API, config, behaviour); migration or rollout steps noted if needed.
- [ ] **Follow-up work**: Any known TODOs, tech debt, or planned follow-up PRs mentioned briefly.

## Template (copy-paste)

```markdown
## What
<!-- One or two sentences -->

## Why
<!-- Bug, requirement, or tech debt -->

## Ticket
<!-- e.g. NOVACORE-12345 -->

## Scope
- In scope: ...
- Out of scope: ...

## How to review
- Focus on: ...
- Test: `npm run test` / `mvn test` / ...

## Breaking changes / follow-ups
<!-- If none, write "None" -->
```

## Output

If you are an AI: either fill the template from the diff/context provided, or review an existing description and list which checklist items are missing or could be improved.
