<!-- docs/workflow/project-development-rules.md -->

# Project development rules

## Purpose

This document defines durable development rules for `docx-ai-risk-analyzer`.

It is not a one-time prompt and not a Codex-specific instruction. These rules apply to ChatGPT, Codex and any future coding agent working on the project.

The goal is to keep development consistent as the project grows: DDD-inspired boundaries, privacy constraints, code documentation, non-regression discipline, check commands and scope control must remain stable across chat-based and PR-based development.

## Audience

This document is agent-facing operational workflow text. Therefore it is English-first.

Russian is still required or preferred inside code documentation, frontend user-facing text, owner-facing explanations and manual smoke-check explanations.

## Product context

`docx-ai-risk-analyzer` is a local-first monorepo application for editorial analysis of academic `.docx` documents by AI-risk markers.

The product does not prove AI generation and must not position itself as an official detector. It identifies linguistic, structural and statistical markers that may require manual editorial review.

Core stack:

~~~text
Backend: Python, FastAPI, Pydantic, python-docx, pytest, Ruff, mypy, uv
Frontend: Next.js, React, TypeScript, Tailwind CSS, pnpm
CI: GitHub Actions
Repository model: monorepo
~~~

## Product invariants

The following rules must not be weakened by feature work, refactoring, tests or documentation updates:

1. The tool must not claim that it proves AI generation.
2. Analysis result is an editorial risk assessment, not an official detector verdict.
3. Local-first behavior must remain the default.
4. Uploaded documents are user data.
5. Uploaded documents must not be committed, logged, copied into PR descriptions, screenshots or fixtures without explicit approval.
6. Analysis output must be explainable through visible markers, statistics or structural signals.
7. Frontend user-facing text must be Russian.
8. Machine-readable statuses, error codes, diagnostic codes and API fields must remain English.
9. API responses must not expose stack traces, internal paths or raw exception details.
10. External AI/LLM provider integration is forbidden without a separate approved architecture scope.

## DDD-inspired architecture

The project must evolve according to DDD-inspired architecture.

DDD here does not mean creating folders mechanically. It means preserving responsibility boundaries so that the analyzer can grow without mixing domain rules, HTTP details, UI rendering and infrastructure adapters.

Expected conceptual layers:

~~~text
domain / analyzer core
→ text analysis rules, DOCX blocks, markers, dictionaries, scoring, rhythm metrics,
  risk categories and recommendation reasons.

application / services
→ use cases, orchestration, coordination of extraction/scoring/recommendation assembly,
  API response preparation and workflow-level decisions.

infrastructure
→ adapters for DOCX libraries, file parsing, export generation, optional persistence,
  optional external providers and other IO details.

presentation / API
→ FastAPI routes, upload handling, request validation, safe error mapping and HTTP contracts.

frontend presentation
→ pages, UI components, local UI state and user-facing rendering.

frontend infrastructure / client
→ typed API clients, response mapping and reusable browser-side helpers.
~~~

## Backend boundaries

Backend lives in `apps/api`.

Expected module ownership:

~~~text
apps/api/src/docx_ai_risk_api/analyzer
→ domain/analyzer core: extraction normalization assumptions, segmentation,
  dictionaries, scoring, marker matching, rhythm analysis and recommendation reasons.

apps/api/src/docx_ai_risk_api/services
→ application orchestration: analysis use cases, response assembly and coordination.

apps/api/src/docx_ai_risk_api/routes
→ FastAPI HTTP layer: upload handling, request validation and safe error mapping.

apps/api/src/docx_ai_risk_api/schemas.py
→ Pydantic API contracts.

apps/api/tests
→ API smoke tests, analyzer unit tests, extraction tests and scoring regression tests.
~~~

Backend rules:

1. Analyzer modules must not import FastAPI, Starlette, request objects, response objects, React, Next.js or frontend code.
2. Domain/analyzer logic must remain testable without network, browser, server runtime or external services.
3. Routes must remain thin.
4. If route logic grows, orchestration must move to `apps/api/src/docx_ai_risk_api/services`.
5. Pydantic models are API contracts and must be documented.
6. Scoring behavior must be deterministic and covered by regression tests.
7. DOCX extraction must preserve support for paragraphs and tables.
8. DOCX read errors must be mapped to safe API errors without stack traces.
9. Business/domain decisions must not be hidden inside HTTP route handlers.
10. New analyzer capabilities must be designed around explicit marker categories, deterministic scoring rules, documented risk reasons and regression tests.

## Frontend boundaries

Frontend lives in `apps/web`.

Expected module ownership:

~~~text
apps/web/src/app
→ Next.js routes and layout.

apps/web/src/components
→ UI components and presentation state.

apps/web/src/lib
→ frontend API clients, helpers and shared frontend utilities.
~~~

Frontend rules:

1. UI components must not own reusable low-level API request logic if it can live in `apps/web/src/lib/api`.
2. Machine-readable API values must be mapped to Russian user-facing text.
3. Error states, empty states, hints, labels and user-facing explanations must be Russian.
4. Export helpers must document output format and limitations.
5. UI components should focus on rendering, interaction state and user flow.
6. API clients should own request construction, response validation/mapping and reusable browser-side API behavior.
7. Business/domain decisions must not be hidden inside React components.

## Source module conventions

Every new or changed source module must start with a path comment.

Python source module example:

~~~python
# apps/api/src/docx_ai_risk_api/analyzer/extraction.py
"""Извлечение текста из DOCX-документов.

Модуль относится к analyzer layer и не зависит от FastAPI или frontend-кода.
Он извлекает paragraphs and tables и возвращает нормализованные текстовые блоки
для дальнейшего эвристического анализа.
"""
~~~

TypeScript / TSX source module example:

~~~ts
// apps/web/src/components/analyzer-upload-form.tsx
'use client';

import { useState } from 'react';
~~~

Rules:

1. For Python, the path comment must be the first line, followed by a Russian module docstring.
2. For TS/TSX, the path comment must be the first line.
3. If a TSX file is a client component, `'use client'` must go immediately after the path comment.
4. JSDoc, module comments and Python docstrings are part of the implementation and must be preserved or expanded.
5. Public contracts must remain explicit and documented.
6. Runtime safety, privacy and regression assumptions must be documented near the code that depends on them.
7. Do not add dependencies unless the task explicitly requires them.
8. Do not perform formatting-only changes outside the requested scope.

## Code documentation rules

Code documentation must be detailed by default.

Detailed documentation does not mean commenting every line. It means that a reviewer can understand module purpose, layer ownership, inputs, outputs, limitations and safety/privacy assumptions without reconstructing the whole project from scattered files.

Document in detail:

~~~text
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
~~~

Do not remove or shorten existing docstrings, JSDoc or comments without explicit justification.

## Language rules summary

Follow `docs/workflow/project-language-rules.md` as the source of truth.

Short summary:

~~~text
Agent-facing operational instructions -> English-first.
Code documentation and owner-facing explanations -> Russian-first.
Machine-readable and code-adjacent entities -> English.
~~~

Examples:

1. Python docstrings should be Russian-first.
2. TypeScript/JSDoc should be Russian-first.
3. Frontend user-facing text should be Russian.
4. API fields, statuses, error codes and diagnostic codes should be English.
5. Conventional commit messages should be English.
6. CLI commands, CI/runtime logs and GitHub Actions step names should be English.
7. Stable engineering terms may remain English when they name concrete technical concepts.

Before writing or editing any section, determine the audience of that section. Do not mix owner-facing Russian explanations with adjacent English operational instructions inside one rule block unless the audience switch is explicit.

## Security and privacy rules

Secrets and sensitive values must never be written to chat, documentation, Git commits, logs, issue comments, screenshots or PR descriptions.

Sensitive values include:

~~~text
real API keys;
tokens;
private URLs;
uploaded document content;
personal data from documents;
real emails, phone numbers or addresses;
stack traces with local paths or private context.
~~~

Allowed:

~~~text
Documenting env variable names without values.
Documenting safe placeholder values that cannot be confused with real secrets.
Documenting privacy assumptions and data-flow boundaries.
~~~

Forbidden:

~~~text
Logging uploaded document text.
Adding real uploaded documents to fixtures without explicit approval.
Copying private document fragments into PR body or screenshots.
Using real secret values as examples.
Exposing raw exception details to frontend users.
Adding external AI/LLM calls without approved architecture scope.
~~~

## Non-regression rules

1. Do not remove existing functionality.
2. Do not remove or shorten Python docstrings, JSDoc or module comments.
3. Do not remove exported functions, classes, types, interfaces, constants, hooks or components unless the task explicitly requires it.
4. Do not remove fallback branches, validation branches, error-handling branches or edge-case handling.
5. Do not replace specific behavior with a simplified placeholder.
6. Do not weaken tests or rewrite expected values without explaining the product reason.
7. Do not change public API contracts unless the task explicitly requires it.
8. Do not perform broad refactoring inside bug-fix, docs-only or test-only commits.
9. If behavior is intentionally removed, stop and request explicit approval before finalizing the change.

## Module size reduction rule

If a module becomes smaller, explicitly explain:

1. What was extracted from the module.
2. Where the extracted logic/documentation moved.
3. Why this is not functional degradation.
4. Why documentation, docstrings or JSDoc were not lost.
5. Which checks or diffs confirm that behavior is preserved.

If it is impossible to verify that a reduction is safe, do not claim that it is safe. Ask for the current module or diff first.

This rule applies to source code and workflow documentation. A documentation index may become shorter only when information is intentionally moved into a dedicated document and the index links to that new source of truth.

## Commit scope rules

Each commit must be atomic.

A commit should have one primary purpose:

~~~text
docs-only workflow update;
backend refactor;
frontend refactor;
API contract update;
analyzer scoring change;
test coverage update;
export feature;
UI feature;
CI/workflow change.
~~~

Do not mix unrelated concerns.

Examples:

~~~text
Good:
docs(workflow): add development rules
refactor(web): move analyzer request to API client
test(api): add analyzer scoring regression tests

Bad:
feat(web): add export and rewrite backend scoring and update roadmap
docs: update everything
fix: improve project
~~~

## Required checks

Backend changes:

~~~bash
cd apps/api
uv run ruff check src tests
uv run mypy src
uv run pytest
~~~

Frontend changes:

~~~bash
pnpm --filter web lint
pnpm --filter web exec tsc --noEmit
pnpm --filter web build
~~~

Docs-only changes:

~~~bash
git status --short
git --no-pager diff --stat
git --no-pager diff -- <changed-files>
~~~

Workflow, dependency, build or CI changes require the relevant full check set and GitHub Actions confirmation.

Docs-only changes do not require runtime smoke checks, but `git diff` and `git status` are required.

## Current development mode

Current development mode is ChatGPT chat-based implementation.

That means ChatGPT prepares atomic commits, outputs full modules or safe targeted replacements, and the developer manually applies changes locally.

Codex must not be used for full implementation until the following documents exist and are approved:

~~~text
docs/workflow/github-pr-orchestration.md
docs/workflow/codex-implementation-protocol.md
docs/workflow/codex-prompt-template.md
~~~

The first Codex task should be low-risk and strongly checkable, such as docs consistency, test fixtures, module headers/docstrings or frontend API client extraction after explicit approval.