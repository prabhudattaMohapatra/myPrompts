# Bug Triage Checklist

Use this prompt when triaging a bug report or failure (from a ticket, CI, or user report). Paste it with the bug description, logs, or stack trace.

---

## Role

You are triaging a bug: classify it, confirm reproducibility, and decide next steps. You are not fixing the bug unless asked; focus on understanding and routing.

## Instructions

### 1. Summarise the bug

- **What**: One-sentence description of the observed wrong behaviour or failure.
- **Where**: Component, service, file, or flow (e.g. “Lambda X”, “API /payroll/run”, “UI step 3”).
- **When**: Trigger (e.g. “On submit”, “Every night at 00:00”, “When input is empty”).

### 2. Reproducibility

- [ ] **Steps**: Are there clear steps to reproduce? If not, list what’s missing.
- [ ] **Environment**: Is env specified (local, staging, CI, browser, version)?
- [ ] **Consistency**: Does it always happen, or only sometimes? Note if flaky or env-specific.

### 3. Impact & severity

- [ ] **Impact**: Who is affected? (e.g. all users, one tenant, only admins, CI only.)
- [ ] **Severity**: Classify as critical / major / minor / trivial (or use your team’s scale). Justify in one line.
- [ ] **Workaround**: Is there a known workaround? Mention it.

### 4. Root cause (if known)

- **Suspected cause**: From logs, stack trace, or code: what likely failed? (e.g. “Null in tax lookup when regulation list empty”.)
- **Evidence**: Quote or link the relevant log line, assertion, or code path.
- **Uncertainty**: If cause is unknown, list 1–3 hypotheses to investigate.

### 5. Next steps

- [ ] **Assignee**: Who should own it? (team, role, or “unassigned”.)
- [ ] **Duplicate**: Could this be the same as another ticket? Suggest search terms or ticket IDs.
- [ ] **Action**: Recommend: fix now, backlog, spike to reproduce, or close as duplicate/not-a-bug (with reason).

## Output format (example)

```markdown
**Summary:** ...
**Where / When:** ...

**Reproducibility:** ...
**Impact / Severity:** ...
**Workaround:** ...

**Suspected cause:** ...
**Evidence:** ...
**Next steps:** ...
```

## Output

If you are an AI: fill the sections above from the provided bug report and logs. If information is missing, list what’s needed to complete triage. Do not change code unless the user asks for a fix.
