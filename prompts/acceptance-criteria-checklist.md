# Acceptance Criteria Checklist

Use this prompt when writing or reviewing acceptance criteria for a story, ticket, or feature. Paste it with the ticket or spec.

---

## Role

You are helping write or review acceptance criteria (AC) so that “done” is testable and unambiguous. Good AC allow both implementation and testing to succeed without extra guesswork.

## Checklist for acceptance criteria

### Completeness

- [ ] **User goal**: The user/stakeholder goal is stated (who, what, why in one sentence).
- [ ] **Scope**: In scope is clear; out of scope or “not in this ticket” is stated where it avoids confusion.
- [ ] **Done definition**: What “done” means is explicit (e.g. “User can X”, “API returns Y when Z”).

### Testability

- [ ] **Observable**: Each criterion can be verified by behaviour or output (screens, APIs, logs, data); no vague “should work” or “improve”.
- [ ] **Concrete**: Inputs and expected outcomes are specific (e.g. “When user submits with invalid email, show message M” not “handle errors well”).
- [ ] **Independent**: Criteria can be checked one by one; no single giant paragraph that mixes many conditions.

### Edge cases & errors

- [ ] **Happy path**: Main success path is covered.
- [ ] **Validation**: Invalid or missing input is addressed (what the user sees or what the API returns).
- [ ] **Errors**: Known error cases (e.g. timeout, not found, duplicate) have a stated expected behaviour.

### Dependencies & constraints

- [ ] **Dependencies**: Other systems, APIs, or data that must be available are mentioned.
- [ ] **Constraints**: Non-functional needs (e.g. performance, permissions) are stated if they affect “done”.

## Template (copy-paste)

```markdown
**Goal:** As a [role], I want [action/outcome] so that [benefit].

**In scope:** ...
**Out of scope:** ...

**Acceptance criteria:**
1. Given [precondition], when [action], then [observable result].
2. Given [precondition], when [invalid action], then [observable result].
3. ...

**Dependencies / constraints:** ...
```

## Output

If you are an AI: review the provided AC against the checklist and note pass/fail/N/A per item. Suggest rewritten or new criteria for any that are vague or untestable. If drafting from a ticket, fill the template and list any open questions.
