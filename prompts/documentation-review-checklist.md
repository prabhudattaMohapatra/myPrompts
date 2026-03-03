# Documentation Review Checklist

Use this prompt when writing or reviewing docs (README, API docs, runbooks, or ADRs). Paste it with the doc or link.

---

## Role

You are reviewing documentation for clarity, completeness, and accuracy. Apply this checklist to the provided doc (README, Confluence page, ADR, API spec, etc.).

## Checklist

### Purpose & audience

- [ ] **Purpose**: It’s clear what the doc is for (e.g. “how to run the engine locally”, “API contract for regulation loader”).
- [ ] **Audience**: The intended reader is obvious (e.g. new devs, ops, API consumers); tone and depth match that audience.

### Content

- [ ] **Up to date**: Commands, versions, and config examples work with the current codebase; no references to removed or renamed components.
- [ ] **Complete**: Prerequisites, setup, and steps are listed in order; nothing critical is assumed without being stated.
- [ ] **Accurate**: Technical details (APIs, env vars, file paths) match the code or repo; no copy-paste errors or placeholders left in.

### Structure & readability

- [ ] **Structure**: Headings and sections are logical; a new reader can scan and find what they need quickly.
- [ ] **Formatting**: Code blocks, lists, and links are formatted correctly; diagrams (e.g. Mermaid) render if used.
- [ ] **Jargon**: Acronyms and domain terms are explained on first use or linked to a glossary.

### Safety & ops (if applicable)

- [ ] **Sensitive data**: No real secrets, credentials, or PII in examples; use placeholders like `REDACTED` or `your-api-key`.
- [ ] **Runbooks**: If it’s a runbook, failure modes and rollback steps are mentioned where relevant.

## Output

If you are an AI: go through the checklist and note pass/fail/N/A per item with a one-line comment. End with a short summary: what’s good and the top 1–3 improvements to make.
