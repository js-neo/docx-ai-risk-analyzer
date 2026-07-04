<!-- docs/workflow/project-language-rules.md -->

# Языковые правила проекта docx-ai-risk-analyzer

## Назначение

Этот документ фиксирует языковой стандарт проекта `docx-ai-risk-analyzer` для `AGENTS.md`, workflow-документов, Python docstrings, TypeScript/JSDoc, комментариев, тестов, frontend user-facing text, Codex prompt и Pull Request workflow.

Главное уточнение: agent-facing operational instructions могут и должны быть English-first. Это относится к `AGENTS.md`, Codex protocol, PR orchestration, non-regression rules, required checks, Codex output requirements and Definition of done.

Русский язык остаётся обязательным или предпочтительным для code documentation, user-facing текста и owner-facing пояснений.

## Краткий принцип

Не существует одного языка для всей документации. Нужно различать audience и функцию текста.

```text
Agent-facing operational instructions -> English-first.
Code documentation and owner-facing explanations -> Russian-first.
Machine-readable and code-adjacent entities -> English.
```

Иными словами:

```text
AGENTS.md и Codex operational rules — преимущественно английские.
Python docstrings, TypeScript/JSDoc, module comments and test comments — преимущественно русские.
Frontend user-facing text — русский.
CLI, CI, runtime logs, API fields, statuses, error codes and commit messages — английские.
```

## English-first exception для AGENTS.md и workflow protocols

`AGENTS.md` не обязан быть преимущественно русским. Для этого файла корректнее использовать English-first style, потому что он работает как постоянная инструкция для Codex, ChatGPT and other coding agents.

English-first sections допустимы и предпочтительны для:

```text
Purpose;
Project context;
Architecture rules;
Required module conventions;
Non-regression rules;
Security and privacy;
GitHub PR orchestration;
Required checks;
Codex output requirements;
Definition of done;
branching / PR / CI workflow instructions.
```

Русский язык в `AGENTS.md` допустим для owner-facing context, user-facing copy rules and short explanations. Но hard constraints для Codex лучше формулировать на английском, коротко и однозначно.

## Где русский обязателен или предпочтителен

Русский язык обязателен или предпочтителен в следующих местах:

```text
Python module docstrings;
Python public function/class docstrings;
Pydantic model explanations;
TypeScript JSDoc for exported components/types/helpers;
module comments;
path-adjacent explanatory comments;
comments explaining safety/privacy/regression reasons;
frontend user-facing UI text;
error messages shown to the user;
roadmap explanations intended for the Russian-speaking owner;
transfer notes and owner-facing handoff documents;
manual smoke-check explanations intended for the Russian-speaking owner.
```

## Где английский обязателен или предпочтителен

Английский язык обязателен или предпочтителен в следующих местах:

```text
AGENTS.md operational instructions;
Codex implementation protocol;
GitHub PR orchestration protocol;
PR template field names;
Codex output requirements;
non-regression report template;
Definition of done;
code identifiers;
type names;
function names;
variable names;
file paths;
env variable names;
API/JSON fields;
machine-readable values;
statuses;
error codes;
diagnostic codes;
CLI commands;
CI logs;
runtime logs;
GitHub Actions step names;
branch names;
conventional commit messages.
```

## Правило первого использования термина

Если английский термин важен и неочевиден для русскоязычного reviewer, при первом использовании нужно дать русское пояснение в скобках.

Примеры:

```text
runtime (контур выполнения)
quality gate (контрольный барьер качества)
source of truth (источник истины)
API client (клиентский модуль для вызова API)
false positive (ложное срабатывание)
local-first (локальная обработка по умолчанию)
```

После первого пояснения термин можно использовать короче.

## Подробность документации кода

Документация кода в проекте должна быть подробной по умолчанию.

Подробная документация не означает комментарий к каждой строке. Она означает, что reviewer может понять назначение модуля, границы ответственности, входные данные, результат, ограничения и причины важных проверок без восстановления логики по всему проекту.

Подробно документируются:

```text
назначение backend/frontend модуля;
место модуля в архитектуре;
публичные функции, классы, Pydantic models, exported types and components;
scoring rules и причины начисления risk score;
DOCX extraction assumptions;
privacy assumptions;
validation and error handling branches;
API response contracts;
frontend API client behavior;
export behavior;
тесты, которые защищают важные регрессии.
```

Не нужно комментировать очевидные строки, например простое присваивание, импорт или стандартный `return`, если в них нет архитектурного смысла.

## Python docstrings

Каждый новый или изменённый Python source module должен начинаться с path comment и подробного module docstring на русском языке.

Пример:

```python
# apps/api/src/docx_ai_risk_api/analyzer/extraction.py
"""Извлечение текста из DOCX-документов.

Модуль относится к analyzer layer и не зависит от FastAPI или frontend-кода.
Он извлекает paragraphs and tables и возвращает нормализованные текстовые блоки
для дальнейшего эвристического анализа.
"""
```

Public functions, classes, exceptions, Pydantic models and non-obvious scoring rules должны иметь русскоязычные docstrings.

Docstring должен объяснять:

```text
назначение;
входные данные;
результат;
ограничения;
privacy или safety assumptions, если они есть;
причину важного архитектурного разделения, если она неочевидна.
```

Не нужно писать очевидные docstrings для маленьких внутренних функций, если они не являются публичным контрактом и не содержат важной логики.

## Pydantic models

Pydantic models являются API contract, поэтому их нужно документировать особенно внимательно.

Рекомендуется использовать:

```text
docstring у модели;
понятные имена полей;
Field(description=...) для публичных response fields, если описание не очевидно;
стабильные machine-readable значения;
отсутствие stack traces и raw exception details в user-facing ответах.
```

## TypeScript, React и JSDoc

Новые или изменённые exported components, API clients, exported types and non-trivial helpers должны иметь русскоязычный JSDoc или module-level comment.

Пример:

```ts
// apps/web/src/lib/api/analyzer.ts

/**
 * Отправляет DOCX-файл в backend API и возвращает результат анализа.
 *
 * API client изолирует HTTP-детали от React-компонентов. Компоненты не должны
 * самостоятельно собирать URL, разбирать raw response или дублировать обработку
 * ошибок, если эта логика нужна повторно.
 */
export async function analyzeDocument(file: File): Promise<AnalyzeResponse> {
  // ...
}
```

User-facing text должен оставаться на русском языке.

Machine-readable statuses and API fields не переводятся.

## Правило path comment

Каждый новый или изменённый source module должен начинаться с path comment.

TypeScript / TSX:

```ts
// apps/web/src/components/analyzer-upload-form.tsx
'use client';

import { useState } from 'react';
```

Python:

```python
# apps/api/src/docx_ai_risk_api/schemas.py
"""Pydantic-контракты API анализа DOCX-документов."""
```

Если TSX-файл является client component, `'use client'` должен идти сразу после path comment.

## Комментарии в тестах

Названия тестов могут оставаться на английском, если они используются как machine-oriented behavior description.

Комментарии и docstrings в тестах пишутся на русском языке, если они объясняют:

```text
какую регрессию защищает тест;
какую privacy boundary нельзя нарушить;
почему конкретное значение не должно попасть в ответ;
почему expected value важен для scoring behavior;
почему ошибка должна быть safe and user-facing.
```

Не использовать реальные документы, ФИО, телефоны, email, точные адреса, private file content, tokens or provider payloads в fixtures.

## Frontend user-facing text

Все тексты, которые видит пользователь, должны быть на русском языке:

```text
кнопки;
подсказки;
ошибки;
empty states;
summary labels;
limitations;
export labels;
описания риска;
пояснения к маркерам.
```

Machine-readable values остаются английскими:

```text
low
medium
high
analyzed
invalid-file
```

## API responses and error contracts

JSON fields, statuses and error codes пишутся на английском языке.

Пример:

```json
{
  "status": "analyzed",
  "overall_risk": "low",
  "risk_score": 3
}
```

User-facing interpretation этих значений во frontend должна быть на русском:

```text
low -> Низкий
medium -> Средний
high -> Высокий
```

## Codex prompt language rules

Codex prompt может быть English-first, особенно если это implementation task.

Если задача затрагивает UI text, Python docstrings, JSDoc, comments, tests, roadmap или transfer notes, prompt должен явно указать языковые требования.

Рекомендуемый блок:

```text
Language rules:
- Agent-facing implementation instructions may be English-first.
- User-facing UI text must be Russian.
- Python docstrings, TypeScript/JSDoc, module comments and test comments must be Russian unless they are identifiers, commands, statuses, API fields or stable engineering terms.
- Preserve or expand detailed code documentation.
- Do not remove or shorten existing documentation without explicit justification.
```

## PR body, commit message and CLI

Git commit message остаётся conventional commit на английском:

```text
feat(api): validate upload size
refactor(web): move analyzer request to API client
docs(workflow): align agent instructions language with route-cost standard
```

PR title может быть английским и должен отражать commit purpose.

PR body may be English-first if it is agent-facing workflow text.

Review comments for the Russian-speaking owner may be Russian.

CLI output, CI logs, runtime logs, event names, statuses, error codes and diagnostic codes остаются на английском.

## Мини-чеклист review языковых правил

Перед merge проверить:

```text
1. AGENTS.md and Codex operational sections are clear, English-first and unambiguous.
2. Russian is preserved for user-facing UI text and owner-facing explanations.
3. Python docstrings, TypeScript/JSDoc and module comments are Russian unless a technical term must remain English.
4. Commands, paths, identifiers, env names, statuses, API fields, error codes and commit messages remain English.
5. Complex English terms have Russian explanations on first use when needed.
6. No existing documentation was removed or shortened without explicit justification.
7. No runtime behavior, tests or CI were changed inside language-only commits.
```

## Короткая версия правила

Agent-facing operational instructions — English-first.

Code documentation and user-facing explanations — Russian-first.

Machine-readable and code-adjacent entities — English.

This is the route-cost-compatible language standard for `docx-ai-risk-analyzer`.
