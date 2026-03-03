# Check GitHub Pipeline Errors with `gh`

Use this prompt when a GitHub Actions workflow failed and you need to inspect the failure using the `gh` CLI. Paste it from the repo root or with the run URL/ID. Requires `gh` to be installed and authenticated (`gh auth status`).

---

## Role

You are helping diagnose GitHub Actions pipeline failures. Use the `gh` CLI to list runs, view failed runs, and fetch logs. Summarise what failed, where, and why; suggest concrete next steps. Do not change code unless the user asks; focus on inspection and interpretation.

## Prerequisites

- **`gh` installed**: `gh --version`
- **Authenticated**: `gh auth status` (must be logged in and have repo access)
- **In repo or specify repo**: Run from the repo root, or use `--repo owner/name` with commands below

## Instructions

### 1. List recent workflow runs

- **All recent runs:**
  ```bash
  gh run list --limit 20
  ```
- **Only failed runs:**
  ```bash
  gh run list --limit 20 --status failure
  ```
- **Runs for a specific workflow** (e.g. `main-build.yaml`):
  ```bash
  gh run list --limit 20 --workflow "main-build.yaml"
  ```
- **Runs for a branch or PR:**
  ```bash
  gh run list --limit 20 --branch <branch-name>
  gh run list --limit 20 --branch <branch-name> --status failure
  ```

Note the **run ID** (numeric) or **run URL** of the failed run to inspect.

### 2. View run summary

- **Summary of a specific run** (replace `RUN_ID` with ID from step 1):
  ```bash
  gh run view RUN_ID
  ```
  This shows: workflow name, status, trigger, branch, commit, jobs and their status (success/failure/cancelled).

- **Which job failed:**
  ```bash
  gh run view RUN_ID --json jobs --jq '.jobs[] | select(.conclusion == "failure") | {name: .name, conclusion: .conclusion}'
  ```

### 3. Get logs for the failed run

- **Full log** (can be long):
  ```bash
  gh run view RUN_ID --log
  ```
- **Only failed job logs** (recommended first):
  ```bash
  gh run view RUN_ID --log-failed
  ```
  Saves or streams the log of the job(s) that failed so you can see the failing step and error.

### 4. Interpret the failure

From the run summary and logs, extract:

- **Workflow and job**: Which workflow (e.g. `main-build`) and which job (e.g. `build`, `test`) failed.
- **Step**: Which step inside the job failed (name or number).
- **Error message**: The actual error from the log (e.g. test failure, compile error, exit code 1, permission denied).
- **Likely cause**: Build failure, test failure, lint, missing env/secret, timeout, or dependency issue.

### 5. Report and next steps

Provide:

1. **One-line summary**: e.g. “Workflow X, job Y failed at step Z: <error>.”
2. **Relevant log snippet**: 5–15 lines around the failure (command and error output).
3. **Likely cause**: Short explanation.
4. **Next steps**: One or two concrete actions (e.g. “Fix the failing test in …”, “Add secret X to the repo”, “Re-run with `gh run rerun RUN_ID`”).

If the user asked to fix the failure, only then suggest or apply code/config changes.

## Useful `gh` reference

| Goal | Command |
|------|---------|
| List failed runs | `gh run list --status failure --limit 10` |
| View run | `gh run view RUN_ID` |
| Logs (failed jobs only) | `gh run view RUN_ID --log-failed` |
| Full logs | `gh run view RUN_ID --log` |
| List workflows | `gh workflow list` |
| Re-run a failed run | `gh run rerun RUN_ID` |
| Re-run only failed jobs | `gh run rerun RUN_ID --failed` |
| Repo elsewhere | Add `--repo owner/repo` to any command |

## Output

If you are an AI: run the appropriate `gh` commands (from repo root or with `--repo`), then output (1) summary, (2) log snippet, (3) likely cause, (4) next steps. If `gh` is not available or auth fails, say so and give the exact commands for the user to run locally.
