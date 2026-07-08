<!-- AGENTS.md -->

# docx-ai-risk-analyzer agent instructions

## Purpose

`AGENTS.md` defines durable instructions for ChatGPT, Codex and other coding agents working in the `docx-ai-risk-analyzer` repository.

GitHub repository state, pull requests, CI logs, review comments, roadmap documents and commit history are the source of truth. Chat history is an auxiliary analysis channel and must not replace repository state.

Before starting any task, the agent must read this file, the current workflow documents, the relevant roadmap or handoff document, and the source modules affected by the task.

## Required documents

For every implementation, review or planning task, read:

~~~text
AGENTS.md
docs/README.md
docs/stage-1-roadmap.md
docs/strategic-roadmap.md
docs/workflow/project-language-rules.md
docs/workflow/project-development-rules.md
~~~

`docs/README.md` is the documentation navigation map. It explains active entry points, directory roles, update policy, planned workflow documents and known documentation debt.

For ChatGPT chat-based implementation tasks, also read:

~~~text
docs/workflow/chatgpt-implementation-output-protocol.md
~~~

For GitHub PR orchestration, PR review or CI review tasks, also read:

~~~text
docs/workflow/github-pr-orchestration.md
~~~

For GitHub-facing PR body, Extended description or merge/review comment preparation tasks, also read:

~~~text
docs/workflow/pr-body-and-extended-description-contract.md
~~~

When the following workflow documents are added, read them for the matching task type:

~~~text
docs/workflow/codex-implementation-protocol.md
docs/workflow/codex-prompt-template.md
~~~

If a task belongs to a specific stage, also read the active roadmap, transfer snapshot or handoff document for that stage if it exists in `docs/**`.

## Project context

`docx-ai-risk-analyzer` is a local-first application for analyzing academic `.docx` documents by editorial AI-risk markers.

The project does not prove AI generation. It identifies language, structure and statistical markers that may require manual editorial review.

Current stack:

```text
Backend: Python, FastAPI, Pydantic, python-docx, pytest, Ruff, mypy, uv
Frontend: Next.js, React, TypeScript, Tailwind CSS, pnpm
CI: GitHub Actions
Repository model: monorepo
```

## Language convention

The project uses functional language split: language is selected by the function of the text, not only by whether the text is read by an agent or a user.

Core model:

~~~text
Russian-first explanatory documentation
+ English control-plane blocks
+ English GitHub-facing PR artifacts
+ English code/machine-readable contracts
+ Russian user-facing product text
~~~

Explanatory repository documentation is Russian-first. This includes Markdown docs, roadmap notes, transfer notes, runbooks, architecture explanations, workflow explanations, JSDoc/module comments, explanatory test comments and project governance docs.

Control-plane blocks are English-first. This includes reusable Codex/ChatGPT prompt blocks, PR/checklist field names, required checks, final report contracts, non-regression templates, module size impact templates and Ready/Merge gates.

GitHub-facing PR artifacts are English-first. This includes final PR body, Extended description, PR title, branch name, conventional commit message and merge/review comments intended to be pasted into GitHub.

ChatGPT owner-facing review, planning, request-changes rationale, approve rationale, commit planning, risk analysis and manual guidance in chat are Russian-first.

User-facing product text is Russian. This includes frontend labels, button text, form hints, validation messages, empty states, error explanations shown to the user, support instructions and analysis explanations displayed to the user.

Code-adjacent and machine-readable entities remain English:

~~~text
code identifiers;
type names;
function names;
variable names;
file paths;
branch names;
conventional commit messages;
PR titles;
env variable names;
CLI commands;
CI step names;
runtime log event names;
machine-readable statuses;
error codes;
diagnostic codes;
API/DTO fields;
JSON keys.
~~~

Python docstrings, TypeScript/JSDoc, module comments and explanatory test comments are Russian-first. Code names and stable engineering terms may remain English inside Russian documentation when they name exact technical concepts.

Do not translate identifiers, commands, file paths, env names, API fields, statuses, error codes or diagnostic codes.

Functional consistency rule:

- Determine the function of each section or rule block before choosing the language.
- Explanatory workflow documentation must be Russian-first, even when future coding agents will read it.
- Control-plane blocks must be English-first from heading to adjacent bullets and examples.
- GitHub-facing PR artifacts must be English-first.
- Owner-facing chat explanations must be Russian-first, with stable engineering terms allowed in English when useful.
- Do not mix Russian explanatory prose with adjacent English control-plane instructions inside the same rule block unless the function switch is explicit.
- When fixing language issues, fix both the concrete wording and the underlying rule if the defect can repeat.

## Product invariants

- The tool must not claim that it proves AI generation.
- Analysis result is an editorial risk assessment, not an official detector verdict.
- Local-first behavior must remain the default: uploaded documents are analyzed by the local backend and are not stored permanently.
- Uploaded documents are user data and must not be committed, logged, copied into PR descriptions, screenshots or fixtures without explicit approval.
- Analysis output must be explainable through visible markers, statistics or structural signals.
- Frontend user-facing text must be Russian.
- Machine-readable statuses, error codes and API fields must remain English.
- API responses must not expose stack traces, internal paths or raw exception details.
- External AI provider integration is forbidden without a separate approved architecture scope.

## Required module conventions

Every new or changed source module must start with a path comment.

Python example:

```python
# apps/api/src/docx_ai_risk_api/analyzer/extraction.py
"""Извлечение текста из DOCX-документов.

Модуль относится к analyzer layer и не зависит от FastAPI или frontend-кода.
Он извлекает paragraphs and tables и возвращает нормализованные текстовые блоки
для дальнейшего эвристического анализа.
"""
```

TypeScript / TSX example:

```ts
// apps/web/src/components/analyzer-upload-form.tsx
'use client';

import { useState } from 'react';
```

If a TSX file is a client component, `'use client'` must go immediately after the path comment.

JSDoc, module comments and Python docstrings are part of the implementation and must be preserved or expanded.

Public contracts must remain explicit and documented.

Runtime safety, privacy and regression assumptions must be documented near the code that depends on them.

Do not add dependencies unless the task explicitly requires them.

Do not perform formatting-only changes outside the requested scope.

## Code documentation rules

Code documentation must be detailed by default.

Detailed documentation does not mean commenting every line. It means that a reviewer can understand module purpose, layer ownership, inputs, outputs, limitations and safety/privacy assumptions without reconstructing the whole project from scattered files.

Document in detail:

```text
backend/frontend module purpose;
layer boundaries;
public functions, classes and Pydantic models;
exported frontend types, API clients and non-trivial components;
scoring rules and risk-score reasons;
DOCX extraction assumptions;
privacy assumptions;
validation and error-handling branches;
API response contracts;
frontend API client behavior;
export behavior;
tests that protect important regressions.
```

Do not remove or shorten existing docstrings, JSDoc or comments without explicit justification.

## Backend architecture rules

Backend lives in `apps/api`.

Expected boundaries:

```text
apps/api/src/docx_ai_risk_api/analyzer
→ pure analysis logic: extraction, segmentation, dictionaries, scoring and marker matching.

apps/api/src/docx_ai_risk_api/services
→ application orchestration: analysis use cases, response assembly and coordination.

apps/api/src/docx_ai_risk_api/routes
→ FastAPI HTTP layer: upload handling, request validation and error mapping.

apps/api/src/docx_ai_risk_api/schemas.py
→ Pydantic request/response contracts.

apps/api/tests
→ API smoke tests, analyzer unit tests, extraction tests and scoring regression tests.
```

Rules:

- Analyzer modules must not import FastAPI, Starlette, request objects, response objects or frontend code.
- Route handlers must remain thin. If route logic grows, orchestration must move to `services`.
- Pydantic models are API contracts and must be documented.
- Scoring behavior must be deterministic and covered by regression tests.
- DOCX extraction must preserve support for paragraphs and tables.
- DOCX read errors must be mapped to safe API errors without stack traces.

## Frontend architecture rules

Frontend lives in `apps/web`.

Expected boundaries:

```text
apps/web/src/app
→ Next.js routes and layout.

apps/web/src/components
→ UI components and presentation state.

apps/web/src/lib
→ frontend API clients, helpers and shared frontend utilities.
```

Rules:

- UI components must not own reusable low-level API request logic if it can live in `apps/web/src/lib/api`.
- Machine-readable API values must be mapped to Russian user-facing text.
- Error states, empty states, hints and labels must be Russian.
- Export helpers must document output format and limitations.

## Non-regression rules

- Do not remove existing functionality.
- Do not remove or shorten Python docstrings, JSDoc or module comments.
- Do not remove exported functions, classes, types, interfaces, constants, hooks or components unless the task explicitly requires it.
- Do not remove fallback branches, validation branches, error-handling branches or edge-case handling.
- Do not replace specific behavior with a simplified placeholder.
- Do not weaken tests or rewrite expected values without explaining the product reason.
- Do not change public API contracts unless the task explicitly requires it.
- Do not perform broad refactoring inside bug-fix, docs-only or test-only commits.
- If a module becomes smaller, explain what was extracted, where it moved and why behavior and documentation are preserved.
- If behavior is intentionally removed, stop and request explicit approval before finalizing the change.

## Security and privacy

Secrets and sensitive values must never be written to chat, documentation, Git commits, logs, issue comments, screenshots or PR descriptions.

Sensitive values include:

```text
real API keys;
tokens;
private URLs;
uploaded document content;
personal data from documents;
real emails, phone numbers or addresses;
stack traces with local paths or private context.
```

Allowed to document env variable names when values are not exposed:

```text
NEXT_PUBLIC_ANALYZER_API_URL
```

Secret names must not be used as dummy credential values in runtime or CI configuration.

## Required checks

Backend checks:

```bash
cd apps/api
uv run ruff check src tests
uv run mypy src
uv run pytest
```

Frontend checks:

```bash
pnpm --filter web lint
pnpm --filter web exec tsc --noEmit
pnpm --filter web build
```

Workflow, dependency, build or CI changes require the relevant full check set and GitHub Actions confirmation.

Docs-only changes do not require runtime smoke checks, but `git diff` and `git status` are required.

## GitHub PR orchestration

GitHub PR is the central exchange point for agent-assisted development.

Expected flow:

```text
ChatGPT -> prepares an atomic task
Codex -> implements in a branch and opens a PR
GitHub PR -> stores diff, comments, CI and review decisions
Codex review -> checks regression, documentation and scope risks
ChatGPT -> reviews PR/diff/CI/comments
Developer -> makes the final merge decision
```

Issues, branches, PR comments, CI logs, review comments, roadmap documents, `AGENTS.md` and commit history are the durable shared state.

The developer remains the final owner. Codex must not make final architecture decisions or merge decisions.

## Codex output requirements

Every Codex implementation result must include:

```text
1. Changed files.
2. Root cause or implementation rationale.
3. Summary of changes.
4. Validation commands and results.
5. Non-regression report.
6. Documentation/docstring impact.
7. Known risks and limitations.
8. Follow-up recommendations that are out of scope.
9. Suggested conventional commit message.
```

The non-regression report must explicitly state:

```text
- whether any files were deleted;
- whether any exported symbols were removed;
- whether any Python docstrings, JSDoc blocks or module comments were removed or shortened;
- whether any fallback, validation or error-handling branches were removed;
- whether any tests were removed or weakened;
- whether any module became significantly smaller and why this is safe;
- which behaviors changed intentionally;
- which behaviors were preserved.
```

## Definition of done

A task is complete only when:

```text
1. The goal and scope were fixed before implementation.
2. The diff stays inside the approved scope.
3. Backend/frontend boundaries are preserved.
4. Documentation, Python docstrings and JSDoc are preserved or expanded.
5. Functional behavior is preserved unless explicitly changed.
6. Regression coverage is added or updated for behavior changes.
7. Required checks pass locally when practical.
8. CI passes on the PR or latest pushed commit.
9. Codex review or human review has no unresolved blocking comments.
10. The developer understands and accepts the diff.
```

Passing lint, type-check or tests is necessary but not sufficient. Final acceptance requires architectural review and developer approval.
