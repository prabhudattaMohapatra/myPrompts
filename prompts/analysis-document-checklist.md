# Analysis Document Checklist

Use this prompt when writing or reviewing an analysis document (feasibility, options analysis, impact analysis, design analysis, or technical spec). Paste it with the doc or outline.

---

## Role

You are reviewing (or helping draft) an analysis document. The doc should support a clear decision or next step. Apply this checklist so the analysis is complete, traceable, and actionable.

## Checklist

### Purpose & scope

- [ ] **Objective**: The goal of the analysis is stated (e.g. “choose approach for X”, “assess impact of Y”, “validate feasibility of Z”).
- [ ] **Scope**: In-scope and out-of-scope are clear; boundaries (system, timeline, constraints) are explicit.
- [ ] **Audience**: Intended readers are identified (e.g. architects, product, ops); level of detail matches them.

### Context & inputs

- [ ] **Problem statement**: The problem or opportunity is described; drivers and constraints are listed.
- [ ] **Sources**: Requirements, tickets, or prior docs are referenced; assumptions are called out.
- [ ] **Baseline**: Current state (as-is) is summarised where relevant to the analysis.

### Analysis content

- [ ] **Options / approach**: Options or approaches are listed and compared on agreed criteria (e.g. cost, risk, effort, maintainability).
- [ ] **Evidence**: Claims are backed by data, code references, or links; gaps and uncertainties are noted.
- [ ] **Risks & dependencies**: Key risks and dependencies are identified; mitigation or follow-up is suggested where needed.

### Conclusions & next steps

- [ ] **Conclusion**: A clear conclusion or recommendation is stated, with brief rationale.
- [ ] **Next steps**: Concrete next steps or decisions are listed (e.g. “Implement option A”, “Spike on X”, “Update ADR”).
- [ ] **Open questions**: Open questions or follow-up analyses are recorded so they are not lost.

### Quality

- [ ] **Structure**: Sections flow logically; a reader can find summary, detail, and recommendation quickly.
- [ ] **Traceability**: Key decisions or numbers can be traced back to source (ticket, doc, or assumption).
- [ ] **Accuracy**: Technical details (APIs, versions, metrics) are accurate and consistent with the codebase or docs.

## Output

If you are an AI: go through the checklist and note pass/fail/N/A per item with a one-line comment. Summarise: what’s strong, what’s missing, and the top 1–3 improvements. If drafting, propose an outline or fill missing sections.
