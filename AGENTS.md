<!-- AGENTS.md -->

# docx-ai-risk-analyzer agent instructions

## Назначение

`AGENTS.md` фиксирует постоянный контекст для ChatGPT, Codex и других coding agents, работающих с репозиторием `docx-ai-risk-analyzer`.

GitHub repository, pull requests, CI logs, review comments, roadmap documents and commit history являются источником истины. История чата используется только как вспомогательный канал анализа и не должна заменять актуальное состояние репозитория.

Перед началом любой задачи агент обязан прочитать этот файл, актуальные workflow-документы, roadmap текущего этапа и релевантные модули из текущей ветки.

## Обязательные документы

Перед implementation task, review task или planning task нужно прочитать:

```text
AGENTS.md
docs/stage-1-roadmap.md
docs/strategic-roadmap.md
docs/workflow/project-language-rules.md
```

После добавления docs navigation, PR orchestration и Codex protocol к обязательным документам также будут относиться:

```text
docs/README.md
docs/workflow/github-pr-orchestration.md
docs/workflow/codex-implementation-protocol.md
docs/workflow/codex-prompt-template.md
```

Если задача относится к конкретному этапу, агент также обязан прочитать актуальный roadmap, transfer snapshot или stage handoff document, если такие документы уже есть в `docs/**`.

## Project context

`docx-ai-risk-analyzer` — local-first приложение для анализа академических `.docx` документов по редакционным признакам AI-risk.

Проект не доказывает AI generation. Он помогает найти языковые, структурные и статистические маркеры, которые могут требовать ручной редакторской проверки.

Текущий стек:

```text
Backend: Python, FastAPI, Pydantic, python-docx, pytest, Ruff, mypy, uv
Frontend: Next.js, React, TypeScript, Tailwind CSS, pnpm
CI: GitHub Actions
Repository model: monorepo
```

## Главные продуктовые инварианты

- Инструмент не должен утверждать, что он доказывает генерацию текста нейросетью.
- Результат анализа является редакционной оценкой риска, а не официальным detector verdict.
- Local-first behavior должен сохраняться по умолчанию: документ анализируется локальным backend и не сохраняется постоянно.
- Uploaded documents являются пользовательскими данными и не должны попадать в Git, logs, screenshots, PR descriptions или test fixtures без явного разрешения.
- Analysis result должен быть объяснимым: риск должен связываться с видимыми маркерами, статистикой или структурными признаками.
- User-facing frontend text пишется на русском языке.
- Machine-readable statuses, error codes and API fields остаются на английском языке.
- API responses не должны раскрывать stack traces, internal paths или raw exception details.
- External AI provider integration запрещён без отдельного approved architecture scope.

## Языковые правила

Основной источник языкового стандарта:

```text
docs/workflow/project-language-rules.md
```

Краткое правило:

```text
Поясняющий текст пишется по-русски.
Английский оставляется для identifiers, file paths, env names, API fields, statuses,
error codes, commands, CI steps, conventional commits, branch names and stable engineering terms.
```

Документация, Python docstrings, TypeScript/JSDoc, module comments, test comments, roadmap descriptions and Codex prompt explanations должны быть преимущественно на русском.

Git commit messages остаются conventional commits на английском:

```text
feat(api): validate upload size
refactor(web): move analyzer request to API client
docs(workflow): add agent instructions
```

## Правило path comment в source modules

Каждый новый или изменённый source module должен начинаться с комментария с путём файла.

### Python

```python
# apps/api/src/docx_ai_risk_api/analyzer/extraction.py
"""Подробный module docstring на русском языке.

Документирует назначение модуля, слой, входные данные, результат,
ограничения и privacy/safety assumptions.
"""
```

### TypeScript / TSX

```ts
// apps/web/src/components/analyzer-upload-form.tsx
'use client';

import { useState } from 'react';
```

Если файл является client component, `'use client'` должен идти сразу после path comment.

## Подробная документация кода

Документация кода является частью реализации.

Новые и изменённые source modules должны документироваться достаточно подробно, чтобы reviewer мог понять назначение модуля, границы ответственности, входные данные, результат, ограничения и причины важных проверок без восстановления логики по всему проекту.

Подробно документируются:

```text
назначение backend/frontend модуля;
место модуля в архитектуре;
public functions, classes, Pydantic models, exported types and components;
scoring rules и причины начисления risk score;
DOCX extraction assumptions;
privacy assumptions;
validation and error handling branches;
API response contracts;
frontend API client behavior;
export behavior;
тесты, которые защищают важные регрессии.
```

Не нужно комментировать очевидный синтаксис. Нужно документировать смысл, границы, ограничения, причины проверок и non-regression assumptions.

## Backend architecture boundaries

Backend находится в `apps/api`.

Ожидаемые границы:

```text
apps/api/src/docx_ai_risk_api/analyzer
→ чистая логика анализа: extraction, segmentation, dictionaries, scoring, marker matching.

apps/api/src/docx_ai_risk_api/services
→ application orchestration: analysis use cases, response assembly, coordination.

apps/api/src/docx_ai_risk_api/routes
→ FastAPI HTTP layer: upload handling, request validation, error mapping.

apps/api/src/docx_ai_risk_api/schemas.py
→ Pydantic request/response contracts.

apps/api/tests
→ API smoke tests, analyzer unit tests, extraction tests, scoring regression tests.
```

Правила:

- Analyzer modules не должны импортировать FastAPI, Starlette, request objects, response objects или frontend code.
- Route handlers должны оставаться тонкими. Если route logic растёт, orchestration переносится в `services`.
- Pydantic models являются API contract и должны документироваться подробно.
- Scoring behavior должен быть детерминированным и покрываться regression tests.
- DOCX extraction должна сохранять поддержку paragraphs and tables.
- Ошибки чтения DOCX должны возвращаться как безопасные API errors без stack traces.

## Frontend architecture boundaries

Frontend находится в `apps/web`.

Ожидаемые границы:

```text
apps/web/src/app
→ Next.js routes and layout.

apps/web/src/components
→ UI components and presentation state.

apps/web/src/lib
→ frontend API clients, helpers and shared frontend utilities.
```

Правила:

- UI components не должны содержать reusable low-level API request logic, если её можно вынести в `apps/web/src/lib/api`.
- Machine-readable API values должны маппиться в русскоязычный user-facing text.
- Error states, empty states, hints and labels пишутся на русском языке.
- Export helpers должны явно документировать формат результата и ограничения.

## Non-regression rules

- Не удалять существующую функциональность.
- Не удалять и не сокращать Python docstrings, JSDoc или module comments без явного обоснования.
- Не удалять exported functions, classes, types, interfaces, constants, hooks or components без явного scope.
- Не удалять fallback branches, validation branches, error handling branches or edge-case handling.
- Не заменять конкретное поведение упрощённым placeholder.
- Не ослаблять tests и не переписывать expected values без объяснения продуктовой причины.
- Не менять public API contracts без явного scope.
- Не выполнять broad refactoring внутри bug-fix или test-only commit.
- Если модуль стал меньше, объяснить, что было extracted, куда перенесено и почему behavior/documentation preserved.
- Если поведение intentionally removed, остановиться и запросить explicit approval.

## Security and privacy

Secrets and sensitive values must never be written to chat, documentation, Git commits, logs, issue comments, screenshots or PR descriptions.

Sensitive values include:

```text
реальные API keys;
tokens;
private URLs;
uploaded document content;
личные данные из документов;
реальные email/телефоны/адреса;
stack traces с локальными путями или private context.
```

Разрешено документировать env variable names, если они не раскрывают значения:

```text
NEXT_PUBLIC_ANALYZER_API_URL
```

Запрещено использовать secret names как фактические credential values в runtime/CI configuration.

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

Для docs-only changes runtime smoke checks не требуются, но `git diff` и `git status` обязательны.

## GitHub PR orchestration

GitHub PR является центральной точкой обмена для agent-assisted development.

Ожидаемый процесс:

```text
ChatGPT -> prepares an atomic task
Codex -> implements in a branch and opens a PR
GitHub PR -> stores diff, comments, CI and review decisions
Codex review -> checks regression, documentation and scope risks
ChatGPT -> reviews PR/diff/CI/comments
Developer -> makes the final merge decision
```

Developer остаётся final owner. Codex не принимает архитектурные решения самостоятельно и не выполняет merge.

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

Non-regression report must explicitly state:

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
