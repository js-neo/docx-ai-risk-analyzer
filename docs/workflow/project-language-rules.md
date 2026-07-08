<!-- docs/workflow/project-language-rules.md -->

# Языковые правила проекта docx-ai-risk-analyzer

## Назначение

Этот документ фиксирует языковую модель проекта `docx-ai-risk-analyzer` для repository documentation, workflow-документов, ChatGPT/Codex workflow, GitHub-facing PR artifacts, Python docstrings, TypeScript/JSDoc, frontend user-facing text, API contracts, CI, runtime logs и machine-readable contracts.

Правило приведено к strict route-cost aligned модели: язык выбирается не только по адресату, а по функции текста.

Главная формула:

~~~text
Объясняем на русском.
Управляем инструментами на английском.
GitHub-facing PR artifacts пишем на английском.
Пользователю показываем русский.
Коду и машинам отдаём английский.
~~~

## Базовый принцип

Проект использует functional language split: язык текста определяется его ролью в workflow.

~~~text
Russian-first explanatory documentation
+ English control-plane blocks
+ English GitHub-facing PR artifacts
+ English code/machine-readable contracts
+ Russian user-facing product text
~~~

Это заменяет прежнее грубое правило `Agent-facing operational instructions -> English-first`.

Такое прежнее деление было недостаточно точным, потому что `AGENTS.md`, workflow protocols, roadmap notes, transfer notes и runbooks одновременно являются:

1. инструкциями для ChatGPT/Codex;
2. governance-документами владельца проекта;
3. handoff-контекстом для будущих сессий;
4. source of truth для review;
5. документацией, которую владелец проекта читает и редактирует вручную.

Поэтому объясняющий слой таких документов должен быть Russian-first, а повторяемые технические control-plane blocks должны оставаться English-first.

## Языковая матрица

| Тип текста | Основной язык | Правило |
| --- | --- | --- |
| Project overview | Russian-first | Объяснять на русском, технические имена не переводить |
| Architecture docs | Russian-first | Русская рамка + stable engineering terms на английском |
| Roadmap notes | Russian-first | Dated notes писать на русском |
| Transfer/handoff notes | Russian-first | Это owner-facing durable context |
| Runbooks | Russian-first | Объяснения на русском, команды на английском |
| `AGENTS.md` | Russian-first narrative + English control blocks | Не делать полностью English-first |
| Workflow docs narrative | Russian-first | Назначение, роли, риски, review policy и process explanations писать на русском |
| Codex implementation protocol | Russian-first narrative + English control blocks | Объяснение на русском, reusable contracts на английском |
| Codex prompt template | Russian-first wrapper + English prompt body | Описание на русском, сам prompt contract English-first |
| Concrete Codex prompt `.txt` | English-first | Execution contract для Codex |
| GitHub-facing PR body | English-first | Durable GitHub review artifact |
| GitHub-facing Extended description | English-first | Durable GitHub review artifact |
| ChatGPT review/planning в чате | Russian-first | Owner-facing discussion |
| PR title | English | Conventional technical title |
| Conventional commit | English | Всегда English |
| Branch names | English | Не переводить |
| CLI commands | English | Не переводить |
| CI step names/logs | English | Не переводить |
| Env variables | English uppercase | Не переводить |
| API/DTO fields | English | Не переводить |
| Status/error/diagnostic codes | English | Machine-readable values |
| Runtime logs | English | Machine-readable diagnostics |
| Code identifiers | English | Functions, classes, variables, types |
| Python docstrings | Russian-first | Русское объяснение, code names English |
| TypeScript/JSDoc | Russian-first | Русское объяснение, identifiers English |
| Module comments | Russian-first | Русское объяснение архитектурного смысла |
| Explanatory test comments | Russian-first | Regression/privacy/business rationale |
| Test names | English or existing project style | Сохранять стиль тестового фреймворка |
| Frontend user-facing text | Russian | Для русскоязычного продукта |
| Validation messages shown to user | Russian | Machine-readable code remains English |

## Explanatory documentation

Explanatory documentation — это текст, который объясняет человеку смысл решения, процесса, ограничения или архитектурного выбора.

Писать Russian-first:

~~~text
назначение документа;
бизнес-смысл slice;
архитектурная роль изменения;
почему commit идёт именно сейчас;
какие boundaries фиксирует изменение;
что сознательно не входит в scope;
roadmap notes;
transfer notes;
runbook explanations;
review rationale;
non-regression explanation;
module size impact explanation;
security/privacy rationale;
manual smoke-check instructions;
owner-facing workflow rules.
~~~

Пример:

~~~md
## Назначение

Этот документ фиксирует порядок работы с Codex в проекте. Codex используется как implementation agent, но архитектурное решение, scope, review и merge остаются ответственностью владельца проекта.
~~~

## Control-plane blocks

Control-plane block — это структурированный блок, который управляет работой агента, GitHub, CI, review или machine-readable процесса.

Оставлять English-first:

~~~text
Project / repository:
Current point:
Target slice:
Suggested branch:
Suggested commit message:
Suggested PR title:
Purpose:
Why this is needed:
Affected runtime:
Files to inspect first:
Required implementation:
Out of scope:
Acceptance criteria:
Required checks:
Final report must include:
Non-regression report:
Module size impact:
Ready/Merge gates:
PR body responsibility checklist:
~~~

Причина: такие блоки являются reusable prompt / review / CI contract. Их перевод ухудшает точность и совместимость с Codex/GitHub workflow.

## GitHub-facing PR artifacts

GitHub-facing `PR body` и `Extended description` пишутся English-first.

Это не обычная repository documentation и не owner-facing chat explanation. Это долговечные GitHub review artifacts рядом с:

~~~text
PR title;
conventional commit message;
branch name;
commit history;
CI checks;
review comments;
merge decision context;
GitHub Actions status.
~~~

Canonical PR body headings:

~~~markdown
### Motivation
### Description
### Testing
### Runtime impact
### Non-regression
### Module size impact
### Known limitations
~~~

ChatGPT может объяснять review verdict, request-changes rationale, approve rationale и planning в чате на русском, но copyable GitHub-facing `PR body`, `Extended description` и merge/review comment пишутся English-first.

## ChatGPT owner-facing discussion

ChatGPT review, planning, commit planning, request-changes rationale, approve rationale, scope discussion, risk analysis и manual local command guidance в чате пишутся Russian-first.

Пример:

~~~text
Вердикт: request changes. Пока approve нельзя.

Blocking issue один: новая roadmap note написана почти полностью на английском, а roadmap notes должны быть Russian-first как owner-facing durable project context.
~~~

Если ChatGPT готовит текст, который будет вставлен в GitHub, этот copyable text должен быть English-first и не должен содержать citations внутри copyable блока.

## `AGENTS.md`

`AGENTS.md` является agent-facing документом, но также является durable governance document владельца проекта.

Рекомендуемая модель:

~~~text
AGENTS.md = Russian-first narrative + English control-plane blocks.
~~~

В `AGENTS.md` на русском пишутся:

~~~text
назначение документа;
проектный контекст;
продуктовые инварианты;
архитектурные правила;
non-regression rationale;
privacy/safety explanations;
роль ChatGPT/Codex/developer;
owner-managed workflow explanation.
~~~

На английском остаются:

~~~text
file paths;
commands;
required checks blocks;
Final report must include;
Definition of done;
field names;
code identifiers;
machine-readable contracts.
~~~

## Codex prompt language

Конкретный prompt, который передаётся Codex, лучше делать English-first, потому что это execution contract.

Внутри prompt нужно явно указывать языковые требования к создаваемым и изменяемым файлам:

~~~text
Language rules:
- Markdown docs, roadmap notes, transfer notes, architecture explanations, runbooks, JSDoc/module comments and explanatory test comments must be Russian-first.
- User-facing UI/business copy must be Russian unless the task explicitly targets an English-facing surface.
- Codex prompt control-plane blocks, GitHub-facing PR body, Extended description, PR title, conventional commit message, branch names, CLI commands, CI step names, file paths, code identifiers, env names, API/DTO fields, statuses, error codes, diagnostic codes and runtime logs must remain English.
- Stable engineering terms may remain English inside Russian documentation when they name concrete code-adjacent concepts.
- Do not translate identifiers, file paths, commands, env names, API fields, error codes or diagnostic codes.
- Do not introduce English-first roadmap notes or owner-facing explanatory docs unless the target document explicitly requires English.
~~~

## Code and machine-readable text

Писать на английском:

~~~text
code identifiers;
type names;
function names;
variable names;
class names;
file names;
directory names;
package names;
branch names;
conventional commit messages;
PR titles;
env variables;
CLI commands;
CI job names;
CI step names;
API endpoint paths;
API/DTO fields;
database field names;
queue names;
event names;
runtime log event names;
diagnostic codes;
error codes;
machine-readable statuses;
JSON keys;
test command names;
script names.
~~~

Примеры:

~~~text
analyzeDocxRisk
RiskLevelSummary
NEXT_PUBLIC_ANALYZER_API_URL
INVALID_DOCX_FILE
/api/analyze
pnpm --filter web build
uv run pytest
docs(workflow): align project language rules with route-cost strict model
~~~

## User-facing product text

User-facing text — всё, что видит конечный пользователь продукта в интерфейсе или сообщениях.

Для `docx-ai-risk-analyzer` пользовательский текст пишется на русском:

~~~text
UI labels;
button text;
form hints;
validation messages;
empty states;
error explanations for user;
support instructions;
analysis explanations shown to the user.
~~~

Пример:

~~~json
{
  "code": "INVALID_DOCX_FILE",
  "message": "Загрузите корректный DOCX-файл."
}
~~~

Machine-readable `code` остаётся английским, user-facing `message` остаётся русским.

## Python docstrings

Каждый новый или изменённый Python source module должен начинаться с path comment и подробного module docstring на русском языке.

Пример:

~~~python
# apps/api/src/docx_ai_risk_api/analyzer/extraction.py
"""Извлечение текста из DOCX-документов.

Модуль относится к analyzer layer и не зависит от FastAPI или frontend-кода.
Он извлекает paragraphs and tables и возвращает нормализованные текстовые блоки
для дальнейшего эвристического анализа.
"""
~~~

Public functions, classes, exceptions, Pydantic models and non-obvious scoring rules должны иметь русскоязычные docstrings.

Docstring должен объяснять:

~~~text
назначение;
входные данные;
результат;
ограничения;
privacy или safety assumptions, если они есть;
причину важного архитектурного разделения, если она неочевидна.
~~~

## TypeScript/JSDoc and module comments

TypeScript JSDoc, module comments и explanatory comments пишутся Russian-first.

Пример:

~~~ts
/**
 * Клиентский helper для отправки DOCX-файла в analyzer API.
 *
 * UI-компонент не должен знать детали HTTP-запроса: он передаёт файл,
 * а API client отвечает за request construction, safe error mapping и
 * возврат typed response.
 */
~~~

Code identifiers не переводятся.

## Test comments

Explanatory test comments пишутся Russian-first, если они объясняют business rule, privacy boundary, regression rationale или safety invariant.

Пример:

~~~ts
// Проверяем, что frontend не показывает machine-readable diagnostic code
// вместо понятного русскоязычного сообщения для пользователя.
~~~

Test names могут оставаться English, если таков стиль test framework или проекта.

## Stable English terms

Не нужно насильно переводить устойчивые engineering terms. Это ухудшит точность.

Допустимо оставлять внутри русскоязычной документации:

~~~text
runtime;
scope;
PR;
PR body;
Extended description;
Codex;
ChatGPT;
coding agent;
control-plane;
route handler;
use case;
DTO;
API;
CI;
cache;
fallback;
local-first;
false positive;
source of truth;
quality gate;
read model;
risk scoring;
DOCX extraction;
editorial risk assessment.
~~~

При первом важном употреблении можно дать русское пояснение.

Пример:

~~~md
`control-plane block` — это повторяемый структурированный блок, который управляет работой Codex, GitHub PR или CI и поэтому остаётся English-first.
~~~

## Existing legacy workflow docs

Некоторые workflow-документы были созданы до принятия strict route-cost aligned модели и могут оставаться преимущественно English-first.

Это считается documentation debt, а не новым стандартом.

Новые workflow-документы и новые существенные изменения existing workflow docs должны следовать текущей модели:

~~~text
Russian-first explanatory narrative;
English-first control-plane blocks;
English-first GitHub-facing PR artifacts;
English code/machine-readable contracts;
Russian user-facing product text.
~~~

Если в будущем workflow-документ переписывается существенно, его narrative нужно постепенно переводить к Russian-first route-cost style без изменения технических identifiers и control-plane blocks.

## Антипаттерны

### Полностью English-first workflow docs

Плохо:

~~~md
## Purpose

This document defines how pull requests must be used as the durable coordination layer.
~~~

Лучше:

~~~md
## Назначение

Этот документ фиксирует, как GitHub PR используется как durable coordination layer между ChatGPT, Codex, CI и владельцем проекта.
~~~

### Полный перевод control-plane blocks

Плохо:

~~~text
Проект / репозиторий:
Целевой срез:
Предлагаемая ветка:
Сообщение коммита:
~~~

Лучше:

~~~text
Project / repository:
Target slice:
Suggested branch:
Suggested commit message:
~~~

### Перевод identifiers

Плохо:

~~~text
проанализироватьДокумент
НЕКОРРЕКТНЫЙ_DOCX_ФАЙЛ
~~~

Лучше:

~~~text
analyzeDocument
INVALID_DOCX_FILE
~~~

### Английские roadmap notes без необходимости

Плохо:

~~~md
- 2026-07-07 — documentation workflow updated...
~~~

Лучше:

~~~md
- 07.07.2026 — обновлён documentation workflow: добавлен PR body contract и уточнено разделение GitHub-facing artifacts / owner-facing chat review.
~~~

## Review checklist

При review PR проверять:

~~~text
- Markdown docs changed: are explanatory sections Russian-first?
- Roadmap notes changed: are dated notes Russian-first?
- Transfer notes changed: are they Russian-first?
- Runbooks changed: are explanations Russian-first and commands English?
- AGENTS/workflow docs changed: is narrative Russian-first and control-plane English?
- Codex prompt blocks changed: are control-plane field names English?
- GitHub-facing PR body / Extended description prepared: are they English-first?
- ChatGPT review/planning in chat: is owner-facing explanation Russian-first?
- User-facing copy changed: is visible text Russian?
- API/DTO fields changed: are field names English?
- Error/status codes changed: are machine-readable codes English?
- Runtime logs changed: are log event names English?
- JSDoc/module comments changed: are explanatory comments Russian-first?
- Test comments changed: are business/privacy/regression explanations Russian-first?
- Conventional commit / PR title: English?
- Any unnecessary full-English roadmap/doc paragraph introduced?
- Any unnecessary Russian translation of code identifiers introduced?
~~~

## Итоговое правило

Проект использует functional language split: язык выбирается по функции текста.

Explanatory repository documentation пишется Russian-first. К ней относятся Markdown docs, roadmap notes, transfer notes, runbooks, architecture explanations, workflow explanations, JSDoc/module comments, explanatory test comments and project governance docs.

GitHub-facing PR artifacts пишутся English-first. К ним относятся финальные `PR body` и `Extended description`, которые вставляются в GitHub после review. Они должны совпадать по стилю с PR title, conventional commits, branch names, CI checks, commit history и merge decision context.

ChatGPT owner-facing review and planning пишутся Russian-first. К ним относятся PR review verdicts, request-changes rationale, approve rationale, commit planning, объяснение назначения slice, risk analysis, scope discussion and owner guidance в чате.

Control-plane blocks пишутся English-first. К ним относятся reusable Codex/ChatGPT prompt blocks, PR/checklist field names, required checks, final report contracts, non-regression templates, module size impact templates and Ready/Merge gates.

Code-adjacent and machine-readable contracts пишутся на английском. К ним относятся code identifiers, type names, function names, variable names, file paths, branch names, conventional commit messages, PR titles, env names, CLI commands, CI step names, API/DTO fields, statuses, error codes, diagnostic codes, runtime log events and JSON keys.

User-facing product text пишется на языке пользователя продукта. Для `docx-ai-risk-analyzer` UI copy, validation messages, analysis explanations and support instructions пишутся на русском.

Stable engineering terms may remain English inside Russian documentation when they name exact technical concepts. Do not translate identifiers, commands, file paths, env names, API fields, statuses, error codes or diagnostic codes.
