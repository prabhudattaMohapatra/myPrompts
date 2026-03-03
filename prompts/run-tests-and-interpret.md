# Run Tests and Interpret Results

Use this prompt when you need to run the project’s tests and interpret the output (e.g. after a change, before a commit, or to diagnose a failure). Paste it along with the test command or failure output.

---

## Role

You are helping run tests and interpret results. Execute the appropriate test command for the project, then summarise pass/fail, failures, and next steps. Do not change production code without being asked; focus on running, interpreting, and suggesting fixes.

## Instructions

### 1. Identify project type and test command

From the repo (e.g. `package.json`, `pom.xml`, `build.gradle`, `Cargo.toml`, `Makefile`):

- **Node/TypeScript**: `npm test`, `npm run test:unit`, `npm run test:e2e`, `yarn test`, etc.
- **Java/Maven**: `mvn test`, `mvn verify`, or module-specific `mvn test -pl engine`.
- **Java/Gradle**: `./gradlew test`, `./gradlew test --tests "*.MyTest"`.
- **Other**: Look for `test`, `ci`, or `check` scripts; use the project’s standard command.

If the user specified a command or scope (e.g. “run integration tests”, “test file X”), prefer that.

### 2. Run tests

- Run the test command from the project root (or the directory the user indicated).
- Capture full output; do not truncate failure stack traces or error messages.
- If a previous run failed, re-run after any suggested fix and report the new result.

### 3. Interpret results

- **Summary**: Total ran, passed, failed, skipped (if reported).
- **Failures**: For each failing test:
  - Test name and (if available) file/location.
  - Error message or assertion that failed.
  - Likely cause (e.g. “expectation mismatch”, “missing mock”, “env/config”).
- **Flakiness**: If the same test fails intermittently or only in CI, say so and suggest next steps (e.g. isolate, retry, fix race).

### 4. Next steps

- If all pass: Confirm and note any warnings or slow tests worth following up.
- If any fail: Propose one concrete fix (e.g. “Update assertion in X to expect Y”, “Add env var Z”) and offer to re-run after the fix. Do not apply code changes unless the user asks.

## Project-specific notes (if known)

- **Monorepo**: Run from root; use workspace/project filters if needed (e.g. `npm run test --workspace=@payroll/engine`).
- **Env**: Some tests need env vars or config; mention if “not set” or “missing file” appears.
- **CI**: If the user cares about CI, use the same command and options as in the pipeline (e.g. `npm run test:ci`).

## Output

If you are an AI: run the tests, then provide (1) a one-line summary, (2) failure details in a short list, (3) likely causes, (4) one concrete next step. If you cannot run the command (e.g. no shell), list the exact command the user should run and how to interpret typical output.
