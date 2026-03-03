# Find and Document User Journeys

Use this prompt to discover, list, or document user journeys for a feature, product area, or system. Paste it with the spec, UI flows, or codebase context.

---

## Role

You are analysing a feature or system to identify and document user journeys. A user journey is an end-to-end path a user (human or system) takes to achieve a goal, including steps, entry points, outcomes, and possible failures.

## Inputs to use

- **Spec or PRD**: Requirements, user stories, or acceptance criteria.
- **UI / API**: Screens, flows, or API contracts that describe how users interact.
- **Code**: Entry points (handlers, controllers, jobs) and main flows.
- **Existing docs**: Runbooks, FAQs, or process docs.

## Instructions

### 1. Identify actors

- List who uses the system (roles: end user, admin, integrator, batch job, etc.).
- For each actor, note their main goals in one line.

### 2. Find journeys

For each actor and goal:

- **Trigger**: What starts the journey? (e.g. “User clicks Submit”, “Cron at 00:00”, “API call from client”.)
- **Steps**: Main steps in order; include system actions, not only UI.
- **Happy path**: The success path from trigger to desired outcome.
- **Alternatives**: Branching (e.g. “If validation fails…”, “If user cancels…”).
- **Exit**: How the journey ends (success, partial success, error, abandon).
- **Post-conditions**: What must be true after (data state, side effects, notifications).

### 3. Document

Produce a short document that includes:

- **Journey name** and actor.
- **Goal** in one sentence.
- **Trigger → Steps → Exit** (bullet list or numbered).
- **Alternatives / error paths** (brief).
- **Dependencies** (other systems, data, permissions).
- **Open questions** (e.g. “What happens if X times out?”).

### 4. Gaps and edge cases

- Note journeys that are implied but not clearly specified.
- Note edge cases (timeouts, duplicates, partial failure) that lack a defined path.

## Output format (example)

```markdown
## Journey: [Name]
**Actor:** [Role]
**Goal:** [One sentence]

**Trigger:** ...
**Steps:**
1. ...
2. ...
**Exit:** ...

**Alternatives:** ...
**Dependencies:** ...
**Open questions:** ...
```

## Output

If you are an AI: list the actors, then for each major goal produce a journey in the format above. End with a short “Gaps and edge cases” section. If the provided context is thin, say what’s missing and what would clarify the journeys.
