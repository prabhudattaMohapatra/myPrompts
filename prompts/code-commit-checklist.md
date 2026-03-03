# Code Commit Checklist

Use this prompt before committing (or opening a PR) to ensure changes are ready. Paste it and run through the list with your current changes in mind.

---

## Role

You are helping the developer verify that their working tree is ready to commit. Work through each item; if something fails, fix it or document why it’s skipped before committing.

## Pre-commit checklist

### Build & tests

- [ ] **Build**: Project builds successfully (`mvn compile`, `npm run build`, `cargo build`, or project equivalent).
- [ ] **Unit tests**: All relevant unit tests pass.
- [ ] **Lint**: Linter and formatter are run and issues are fixed or explicitly ignored with a reason (e.g. `// eslint-disable-next-line` with a comment).

### What’s in the commit

- [ ] **Scope**: Only files related to the change are staged; no stray edits, debug code, or commented-out blocks.
- [ ] **Secrets**: No credentials, API keys, or secrets in staged files.
- [ ] **Generated files**: Generated or build artifacts are not committed unless they are intended to be in the repo (e.g. lockfiles, checked-in bundles).

### Message & traceability

- [ ] **Message**: Commit message is clear and describes *what* and *why* (and ticket ID if your process requires it).
- [ ] **Atomicity**: One logical change per commit; if you have multiple unrelated changes, split into separate commits.

### Optional (recommended)

- [ ] **Documentation**: User-facing behaviour or config changes are reflected in docs or README if needed.
- [ ] **Changelog**: If the project keeps a CHANGELOG, add an entry for user-visible changes.

## Example commit message

```
<type>: short summary (e.g. fix: handle null in tax lookup)

- Detail 1
- Detail 2

Refs: TICKET-123
```

## Output

If you are an AI: list which items pass, which fail, and one concrete next step for the first failure. If all pass, confirm and suggest a one-line commit message.
