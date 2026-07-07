<!-- docs/workflow/github-pr-orchestration.md -->

# GitHub PR orchestration protocol

## Purpose

This document defines how GitHub pull requests must be used as the durable coordination layer for agent-assisted development in `docx-ai-risk-analyzer`.

It is not a Codex implementation protocol and not a Codex prompt template.

This protocol describes:

1. Who owns each decision.
2. What must be stored in GitHub PRs.
3. How PR scope is fixed.
4. How CI and review results are interpreted.
5. How ChatGPT, Codex and the developer coordinate through GitHub.
6. What must not be placed into PR descriptions, comments, logs or screenshots.

Codex-specific task execution rules must be documented separately in:

~~~text
docs/workflow/codex-implementation-protocol.md
docs/workflow/codex-prompt-template.md
~~~

## Audience

This document is agent-facing operational workflow text. Therefore it is English-first.

Owner-facing explanations in chat may be Russian, because the project owner is Russian-speaking.

## Core principle

GitHub PR is the durable exchange point for implementation work.

Chat history can help with analysis, planning and explanation, but it must not replace repository state.

Source of truth order:

~~~text
1. Repository files.
2. Commit history.
3. Pull request diff.
4. Pull request description.
5. CI status and logs.
6. Review comments.
7. Roadmap and workflow documents.
8. Chat discussion as auxiliary context.
~~~

If chat memory conflicts with repository state, repository state wins.

## Roles and responsibilities

### Developer

The developer is the final owner of the project.

The developer decides:

1. Whether a task should be implemented.
2. Whether a branch or PR should be created.
3. Whether scope is acceptable.
4. Whether review comments are blocking.
5. Whether a PR can be merged.
6. Whether a follow-up commit, revert or new task is needed.

No agent may merge or make final architecture decisions without developer approval.

### ChatGPT

ChatGPT may:

1. Analyze the current repository state.
2. Propose an atomic task.
3. Prepare the commit/PR scope.
4. Review a PR diff.
5. Review CI logs and comments.
6. Explain risks and non-regression concerns.
7. Recommend whether a PR needs changes before merge.
8. Prepare follow-up tasks.

ChatGPT must not:

1. Treat old chat memory as more reliable than repository files.
2. Approve its own assumptions without checking the current diff.
3. Ignore deleted documentation, docstrings or JSDoc.
4. Expand PR scope silently.
5. Make the final merge decision.

### Codex

Codex may be used only after Codex-specific workflow documents exist and are approved.

Codex may eventually:

1. Implement a task in a branch.
2. Open a PR.
3. Run or report checks.
4. Respond to review comments.
5. Propose a conventional commit message.
6. Summarize implementation and non-regression status.

Codex must not:

1. Merge PRs.
2. Make final architecture decisions.
3. Add external AI/LLM integration without approved architecture scope.
4. Commit user documents or private data.
5. Hide scope expansion inside implementation details.

### GitHub PR

A PR must store the durable implementation state:

1. Branch name.
2. PR title.
3. PR description.
4. Changed files.
5. Diff.
6. CI status.
7. Review comments.
8. Follow-up notes.
9. Final merge decision context.

## Branch naming

Branch names should be short, English and scope-specific.

Recommended format:

~~~text
docs/github-pr-orchestration
docs/codex-implementation-protocol
refactor/web-analyzer-api-client
test/api-analyzer-scoring
feat/web-risky-sentence-details
~~~

Avoid vague branch names:

~~~text
fix
update
changes
new-docs
big-refactor
~~~

## PR title

PR titles should use conventional commit style when practical:

~~~text
docs(workflow): add GitHub PR orchestration protocol
refactor(web): move analyzer request to API client
test(api): add analyzer scoring regression tests
feat(web): show risky sentence details
~~~

The PR title may match the final squash/merge commit message if the repository uses squash merging.

## PR description requirements

Every implementation PR should include:

~~~text
## Summary

## Scope

## Changed files

## Validation

## Non-regression notes

## Documentation impact

## Known risks

## Out of scope
~~~

### Summary

Explain what the PR changes in 2–5 concise bullets.

### Scope

State the approved scope.

If the PR includes anything outside the approved scope, it must be explicitly marked as follow-up or removed.

### Changed files

List changed files by path and role:

~~~text
docs/workflow/github-pr-orchestration.md
→ new workflow protocol for PR-based development

AGENTS.md
→ updates required reading for PR orchestration tasks
~~~

### Validation

List checks that were run.

For docs-only PRs:

~~~bash
git status --short
git --no-pager diff --stat
git --no-pager diff -- <changed-files>
~~~

For backend PRs:

~~~bash
cd apps/api
uv run ruff check src tests
uv run mypy src
uv run pytest
~~~

For frontend PRs:

~~~bash
pnpm --filter web lint
pnpm --filter web exec tsc --noEmit
pnpm --filter web build
~~~

If a check was not run, state why.

### Non-regression notes

Every PR must explicitly state whether it:

1. Deletes files.
2. Removes exported symbols.
3. Removes or shortens Python docstrings, JSDoc or module comments.
4. Removes fallback, validation or error-handling branches.
5. Weakens or removes tests.
6. Changes API contracts.
7. Changes user-facing text.
8. Makes any module significantly smaller.
9. Touches privacy/security behavior.

If a module becomes smaller, the PR must explain:

1. What moved.
2. Where it moved.
3. Why behavior is preserved.
4. Why documentation was not lost.
5. Which diff/check confirms safety.

### Documentation impact

State whether documentation was added, updated or intentionally left unchanged.

If a new document is added to `docs/**`, update `docs/README.md` unless there is a clear reason not to.

### Known risks

List risks that remain after the PR.

Examples:

~~~text
- Docs-only PR, no runtime checks were run.
- Frontend build not run locally; must rely on GitHub Actions.
- Analyzer behavior unchanged; no new regression fixtures added.
~~~

### Out of scope

State what the PR intentionally does not do.

Examples:

~~~text
- Does not add Codex implementation protocol.
- Does not add Codex prompt template.
- Does not change runtime backend/frontend code.
- Does not add external AI/LLM integration.
~~~

## PR comments

PR comments should be durable and actionable.

Good comments:

~~~text
This change moves request construction from the component to the API client.
The component still owns UI state, while apps/web/src/lib/api owns fetch behavior.
~~~

Bad comments:

~~~text
fixed
done
updated
looks good
~~~

A review comment should explain:

1. What is wrong or risky.
2. Which file or behavior is affected.
3. Whether the issue is blocking.
4. What change is expected.

## Review decision levels

Use three practical decision levels:

~~~text
blocking
non-blocking
follow-up
~~~

### Blocking

A blocking issue must be fixed before merge.

Examples:

1. Scope expansion.
2. Deleted functionality.
3. Weakened privacy boundary.
4. Removed docstrings/JSDoc without justification.
5. Broken CI.
6. Public API contract change without approval.
7. Stack trace or private data exposure.
8. External AI/LLM integration without approved scope.

### Non-blocking

A non-blocking issue can be merged if the developer accepts the risk.

Examples:

1. Minor wording issue.
2. Small formatting inconsistency.
3. Non-critical documentation improvement.
4. Test naming improvement.

### Follow-up

A follow-up should become a separate task or issue.

Examples:

1. Refactor outside current scope.
2. Additional test coverage not required for this PR.
3. Roadmap expansion.
4. Future UI improvement.
5. Codex-specific automation.

## CI policy

CI must be treated as necessary but not sufficient.

A green CI result means the automated checks passed. It does not prove that:

1. Scope is correct.
2. Architecture boundaries are preserved.
3. Documentation is complete.
4. Privacy assumptions are safe.
5. Product wording is correct.
6. The developer understands and accepts the diff.

A red CI result is blocking unless the failure is clearly unrelated and the developer explicitly accepts the exception.

## Docs-only PR policy

Docs-only PRs do not require backend/frontend runtime checks by default.

Required local checks:

~~~bash
git status --short
git --no-pager diff --stat
git --no-pager diff -- <changed-files>
~~~

Docs-only PRs must still be reviewed for:

1. Scope control.
2. Broken links or outdated references.
3. Incorrect source-of-truth hierarchy.
4. Language convention violations.
5. Accidental deletion of existing workflow rules.
6. Incorrect claims about current implementation.

## Backend PR policy

Backend PRs must preserve backend boundaries:

1. Analyzer modules must not depend on FastAPI, Starlette or frontend code.
2. Routes must remain thin.
3. Application orchestration should live in services.
4. Pydantic schemas remain explicit API contracts.
5. DOCX extraction and scoring behavior must be covered by tests when changed.
6. Safe error mapping must not expose stack traces or local paths.

Required checks:

~~~bash
cd apps/api
uv run ruff check src tests
uv run mypy src
uv run pytest
~~~

## Frontend PR policy

Frontend PRs must preserve frontend boundaries:

1. UI components own rendering and interaction state.
2. Reusable API request logic belongs in `apps/web/src/lib/api`.
3. User-facing text must be Russian.
4. Machine-readable API values must be mapped to user-facing labels.
5. Error and empty states must remain understandable.

Required checks:

~~~bash
pnpm --filter web lint
pnpm --filter web exec tsc --noEmit
pnpm --filter web build
~~~

## Privacy and security in PRs

Never place the following in PR descriptions, comments, screenshots, fixtures or logs:

~~~text
real uploaded document text;
real personal data;
real API keys;
tokens;
private URLs;
local paths from stack traces;
raw exception details;
private academic documents;
screenshots containing private document content.
~~~

Safe to include:

~~~text
file paths from the repository;
env variable names without values;
synthetic examples;
sanitized error messages;
high-level analysis summaries without private document text.
~~~

## Merge decision

The developer makes the final merge decision.

Before merge, the developer should know:

1. What changed.
2. Why it changed.
3. Which files changed.
4. Which checks passed.
5. Which risks remain.
6. Whether any behavior changed.
7. Whether documentation was preserved or updated.
8. Whether any follow-up task is needed.

No agent should present a PR as merge-ready if blocking review comments or failed required checks remain unresolved.

## Revert and corrective follow-up policy

If a mistake is found before merge, fix it in the PR.

If a mistake is found after merge or push to `main`, choose one of two paths:

~~~text
corrective follow-up commit
→ use when the mistake is limited and safe to repair directly.

revert
→ use when the merged change is unsafe, broad, misleading or difficult to repair without risk.
~~~

Do not silently rewrite history on `main` unless the developer explicitly chooses that strategy.

## Relationship to future Codex workflow

This document defines PR orchestration.

It does not define exactly how Codex must implement code. That belongs in:

~~~text
docs/workflow/codex-implementation-protocol.md
~~~

It does not define the reusable prompt template for Codex. That belongs in:

~~~text
docs/workflow/codex-prompt-template.md
~~~

Before Codex is used for full implementation, the project must have:

~~~text
docs/workflow/github-pr-orchestration.md
docs/workflow/codex-implementation-protocol.md
docs/workflow/codex-prompt-template.md
~~~

## Definition of done for PR orchestration

A PR workflow is complete only when:

1. Scope is clear.
2. Changed files are visible.
3. Validation status is known.
4. Non-regression notes are explicit.
5. Documentation impact is stated.
6. Privacy/security risks are reviewed.
7. Blocking comments are resolved.
8. Follow-up items are separated from current scope.
9. The developer makes the final merge decision.