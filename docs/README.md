<!-- docs/README.md -->

# docx-ai-risk-analyzer documentation map

## Назначение

Этот файл является navigation map по документации проекта `docx-ai-risk-analyzer`.

Он нужен, чтобы будущие ChatGPT/Codex-сессии, ревью и ручная разработка быстро понимали:

- какие документы уже есть в проекте;
- какой документ является active source of truth для конкретной задачи;
- какие документы являются roadmap, workflow protocol, language rules или historical context;
- какие документы ещё только запланированы;
- когда и какой документ нужно обновлять.

`docs/README.md` не заменяет `AGENTS.md`, roadmaps, workflow protocols или source modules. Перед реализацией задачи агент всё равно обязан читать `AGENTS.md`, этот documentation map и релевантные документы текущего scope.

## Current active entry points

Для любой задачи по проекту сначала читать:

~~~text
AGENTS.md
docs/README.md
docs/stage-1-roadmap.md
docs/strategic-roadmap.md
docs/workflow/project-language-rules.md
~~~

Назначение каждого active entry point:

| Документ | Статус | Назначение |
| --- | --- | --- |
| `AGENTS.md` | active agent instructions | Durable instructions для ChatGPT, Codex и других coding agents |
| `docs/README.md` | active documentation map | Карта документации, active entry points, directory roles и update policy |
| `docs/stage-1-roadmap.md` | active stage roadmap | План Stage 1: Local MVP, scope, order, quality gates and non-goals |
| `docs/strategic-roadmap.md` | active strategic baseline v1.1 | Стратегическое развитие продукта, этапы, long-term direction and version history |
| `docs/workflow/project-language-rules.md` | active workflow standard | Языковые правила проекта и audience consistency rules |

## Current development baseline

~~~text
Current commit: 38ade62 — docs(roadmap): add strategic roadmap version metadata
Current stage: Stage 1 — Local MVP
Strategic roadmap version: v1.1
Current implementation priority: refactor(web): move analyzer request to API client
~~~

Stage 1 сейчас должен оставаться сфокусированным на local MVP: frontend API client, risky sentence details, analyzer tests, dictionary extraction, CSV/XLSX export, upload validation and documentation updates.

## Existing documentation

### Root-level project documents

| Документ | Назначение | Когда обновлять |
| --- | --- | --- |
| `AGENTS.md` | Главные durable instructions для coding agents | При изменении обязательных документов, architecture rules, checks, workflow или agent protocol |
| `README.md` | Основное описание проекта и локального запуска | После значимых изменений продукта, setup, scripts, API или UI |

### Roadmaps

| Документ | Назначение | Когда обновлять |
| --- | --- | --- |
| `docs/stage-1-roadmap.md` | Подробный roadmap Stage 1 Local MVP | При изменении Stage 1 scope, order, quality gates или current priority |
| `docs/strategic-roadmap.md` | Стратегический roadmap продукта | При изменении product vision, strategic stages, long-term direction или roadmap version metadata |

### Workflow documents

| Документ | Назначение | Когда обновлять |
| --- | --- | --- |
| `docs/workflow/project-language-rules.md` | Языковой стандарт проекта | При изменении правил языка, audience rules, code documentation language или workflow wording rules |

## Planned workflow documents

Эти документы ещё не созданы, но уже запланированы как развитие workflow layer.

| Документ | Планируемое назначение |
| --- | --- |
| `docs/workflow/project-development-rules.md` | Общие правила разработки проекта: DDD-inspired architecture, boundaries, safety, non-regression, checks |
| `docs/workflow/chatgpt-implementation-output-protocol.md` | Формат текущей разработки через ChatGPT: как выводить коммит, список модулей, полный код, проверки, git add и commit |
| `docs/workflow/github-pr-orchestration.md` | Правила GitHub PR workflow, review ownership, CI, comments and merge decision boundaries |
| `docs/workflow/codex-implementation-protocol.md` | Правила работы Codex после подключения: branch/PR flow, validation, review and reporting |
| `docs/workflow/codex-prompt-template.md` | Шаблон prompt для Codex-задач после появления отдельного Codex protocol |

Важно: `docs/workflow/codex-prompt-template.md` не должен появляться как смешанный ChatGPT/Codex prompt. До подключения Codex правила текущего chat-based development должны жить отдельно в `chatgpt-implementation-output-protocol.md`.

## Directory roles

Текущие и будущие роли директорий:

| Директория | Назначение |
| --- | --- |
| `docs/workflow` | Development workflow, language rules, agent protocols, ChatGPT/Codex output rules, PR orchestration |
| `docs/roadmaps` | Будущие stage-specific и theme-specific roadmaps, если root-level roadmap станет слишком крупным |
| `docs/architecture` | Будущие architecture notes, DDD boundaries, analyzer pipeline diagrams and module ownership |
| `docs/api` | Будущие API contracts, response schema explanations and endpoint documentation |
| `docs/transfer` | Будущие handoff snapshots между этапами или чатами |
| `docs/operations` | Будущие runbooks, smoke checks and local/production operations notes |
| root `docs/*.md` | Активные high-level roadmaps и документы раннего этапа проекта |

Пока проект находится на Stage 1, допустимо держать `docs/stage-1-roadmap.md` и `docs/strategic-roadmap.md` в корне `docs`. Если количество roadmaps вырастет, новые roadmaps лучше складывать в `docs/roadmaps`.

## Documentation update policy

### `AGENTS.md`

Обновлять, если меняются:

- обязательные документы для чтения;
- architecture rules;
- DDD boundaries;
- required checks;
- security/privacy rules;
- agent output expectations;
- GitHub PR or Codex workflow.

Не использовать `AGENTS.md` как место для длинных roadmap-описаний. Он должен оставаться entrypoint-документом для агентов.

### `docs/README.md`

Обновлять, если:

- добавлен новый документ в `docs/**`;
- изменился active roadmap;
- появился новый workflow protocol;
- появился historical snapshot;
- изменилась directory role;
- изменился recommended reading order.

### `docs/stage-1-roadmap.md`

Обновлять, если:

- меняется Stage 1 scope;
- меняется implementation order;
- закрывается крупный Stage 1 task;
- меняется current priority;
- появляются новые Stage 1 non-goals или quality gates.

### `docs/strategic-roadmap.md`

Обновлять, если:

- меняется стратегическое направление продукта;
- меняется roadmap version;
- добавляется крупный future stage;
- меняется long-term product boundary;
- появляется новый strategic product line.

Мелкие correction notes, metadata и ссылки допускаются как patch-level updates. Если меняется стратегический смысл этапов, нужно повышать minor version.

### `docs/workflow/project-language-rules.md`

Обновлять, если:

- меняется language convention;
- обнаружен повторяемый language/audience defect;
- меняется правило для owner-facing, user-facing или agent-facing текста;
- нужно уточнить допустимое использование English stable engineering terms.

## Historical snapshots policy

Historical snapshots нельзя молча переписывать под текущую baseline.

Если в будущем появятся документы в `docs/transfer/**` или historical roadmaps, они должны сохранять context на момент создания. Их можно дополнять correction notes, но нельзя broad-rewrite без отдельного approved scope.

Правило:

~~~text
Active docs можно обновлять под текущую baseline.
Historical docs сохраняют traceability решений.
~~~

## Recommended reading by task type

### Docs-only workflow task

Читать:

~~~text
AGENTS.md
docs/README.md
docs/workflow/project-language-rules.md
релевантный docs/** файл
~~~

### Roadmap update

Читать:

~~~text
AGENTS.md
docs/README.md
docs/stage-1-roadmap.md
docs/strategic-roadmap.md
docs/workflow/project-language-rules.md
~~~

### Backend implementation task

Читать:

~~~text
AGENTS.md
docs/README.md
docs/stage-1-roadmap.md
docs/strategic-roadmap.md
docs/workflow/project-language-rules.md
apps/api/pyproject.toml
apps/api/src/docx_ai_risk_api/**
apps/api/tests/**
~~~

### Frontend implementation task

Читать:

~~~text
AGENTS.md
docs/README.md
docs/stage-1-roadmap.md
docs/strategic-roadmap.md
docs/workflow/project-language-rules.md
package.json
pnpm-workspace.yaml
apps/web/src/**
~~~

### Current ChatGPT chat-based implementation

До подключения Codex ChatGPT должен:

~~~text
1. анализировать актуальный код и docs;
2. предлагать atomic commit;
3. выводить список новых и изменённых модулей;
4. выводить полный код модулей или точечную замену, если это безопаснее;
5. явно объяснять уменьшение модулей, если оно есть;
6. завершать ответ разделами Проверки, Git add и Коммит.
~~~

Подробный protocol для этого режима должен быть вынесен в будущий документ:

~~~text
docs/workflow/chatgpt-implementation-output-protocol.md
~~~

### Future Codex implementation

Codex не должен подключаться к полноценной реализации до появления отдельных workflow-документов:

~~~text
docs/workflow/github-pr-orchestration.md
docs/workflow/codex-implementation-protocol.md
docs/workflow/codex-prompt-template.md
~~~

Первый Codex-task должен быть low-risk и хорошо проверяемым: docs consistency, tests, module headers/docstrings или frontend API client extraction после явного approval.

## Current known documentation debt

Текущие известные задачи по documentation/workflow layer:

~~~text
1. docs/stage-1-roadmap.md остаётся English-first legacy roadmap и позже должен быть приведён к Russian-first owner-facing style.
2. docs/workflow/project-development-rules.md ещё не создан.
3. docs/workflow/chatgpt-implementation-output-protocol.md ещё не создан.
4. docs/workflow/github-pr-orchestration.md ещё не создан.
5. docs/workflow/codex-implementation-protocol.md ещё не создан.
6. docs/workflow/codex-prompt-template.md ещё не создан.
7. Backend and frontend source modules всё ещё требуют постепенного выравнивания с path comment/docstring/JSDoc rules.
~~~

Эти пункты не нужно исправлять в одном коммите. Они фиксируют дальнейшую последовательность и предотвращают смешение scope.

## Ближайшая рекомендуемая последовательность docs/workflow-коммитов

~~~text
1.4 — docs(workflow): add development and ChatGPT output protocols
1.5 — docs(workflow): add GitHub PR orchestration protocol
1.6 — docs(workflow): add Codex implementation protocol
1.7 — docs(workflow): add Codex prompt template
~~~

После этого можно подключать Codex в пилотном режиме для небольших проверяемых задач.

## Что не делать в этом documentation layer

~~~text
1. Не смешивать ChatGPT output protocol и Codex prompt template в одном документе.
2. Не превращать docs/README.md в roadmap.
3. Не дублировать полностью AGENTS.md в каждом workflow-документе.
4. Не переписывать historical snapshots без отдельного scope.
5. Не добавлять runtime-задачи внутрь docs-only коммита.
6. Не подключать external AI/LLM provider без отдельного architecture approval.
~~~