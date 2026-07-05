# Стратегический roadmap

## Видение продукта

`docx-ai-risk-analyzer` — privacy-friendly инструмент для редакционного анализа академических DOCX-документов.

Продукт не должен утверждать, что он доказывает AI generation. Его задача — находить языковые, структурные и статистические маркеры, которые могут требовать ручной редакторской проверки.

Долгосрочная цель проекта — создать практичную local-first систему анализа документов, которая помогает студентам, редакторам и авторам проверять формальные академические тексты перед сдачей, доработкой или публикацией.

## Стратегические принципы

### 1. Local-first и privacy-friendly обработка

Загруженные документы должны обрабатываться локально по умолчанию. Долгосрочное хранение, синхронизация или cloud-processing могут появляться только как отдельные явно включаемые режимы.

Исходный документ не должен сохраняться постоянно без явного согласия пользователя.

### 2. Explainable analysis

Система должна объяснять, почему конкретный фрагмент считается рискованным.

Одного числового score недостаточно. Пользователь должен видеть:

- какой маркер найден;
- в каком фрагменте он найден;
- почему этот маркер может создавать ощущение машинной шаблонности;
- какое редакционное действие может снизить риск.

### 3. Editorial assistant, not AI police

Продукт должен помогать улучшать качество текста. Он не должен позиционироваться как официальный AI detector или как доказательство использования нейросети.

Правильная продуктовая формулировка:

```text
Инструмент выявляет редакционные признаки AI-risk и помогает вручную улучшить текст.
```

Неправильная продуктовая формулировка:

```text
Инструмент доказывает, что текст написан ИИ.
```

### 4. Редакционное снижение шаблонности, а не обход проверок

Будущие функции по переработке текста должны быть описаны как повышение качества академического изложения.

Цель не в том, чтобы обмануть AI-detector. Цель — убрать чрезмерную универсальность, одинаковый ритм, отсутствие конкретики, слабую аргументацию и недостаток авторской логики.

### 5. Incremental development

Каждый этап должен давать рабочий product increment с тестами, документацией и CI.

Нельзя перепрыгивать сразу к AI rewriting, cloud deployment или user accounts, пока локальный анализатор не стал стабильным и объяснимым.

### 6. Portfolio-grade engineering

Репозиторий должен демонстрировать современные engineering practices:

- monorepo structure;
- backend/frontend separation;
- typed API contracts;
- automated tests;
- CI;
- clear roadmap;
- conventional commits;
- detailed documentation;
- privacy and security constraints.

## Обзор этапов

| Stage | Название | Основной результат |
| --- | --- | --- |
| Stage 1 | Local MVP | Стабильный локальный DOCX-анализатор с UI, risk details и export |
| Stage 2 | Analysis Quality | Более точные эвристики, категории маркеров, словари и тесты |
| Stage 3 | Reporting Workflow | Отчёты, история, сравнение версий и report export |
| Stage 4 | Productization | Deployment, authentication, persistence and production workflows |
| Stage 5 | Intelligent Editorial Assistant | Редакторские рекомендации, anti-template analysis and assisted rewriting |

## Stage 1: Local MVP

### Цель

Создать стабильный локальный инструмент для загрузки DOCX-файлов, анализа risk markers и просмотра результатов в браузере.

### Ключевые возможности

- DOCX upload;
- local backend analysis;
- summary metrics;
- block-level risk table;
- risky sentence details;
- CSV/XLSX export;
- stable CI;
- clear documentation.

### Технический фокус

- FastAPI backend structure;
- Next.js frontend structure;
- analyzer unit tests;
- typed response models;
- frontend API client;
- local-first operation.

### Критерии выхода

- пользователь может локально проанализировать DOCX-документ;
- пользователь может увидеть риск по блокам и предложениям;
- пользователь может экспортировать результат;
- CI остаётся green;
- documentation отражает фактическое состояние проекта.

## Stage 2: Analysis Quality

### Цель

Повысить полезность и точность эвристического анализа.

На этом этапе система должна лучше отличать обычный академический стиль от машинной шаблонности. Важно снижать false positives, потому что формальные учебные тексты сами по себе часто содержат повторы, клише, таблицы и нейтральные формулировки.

### Ключевые возможности

- marker categories;
- configurable dictionaries;
- improved Russian sentence splitting;
- improved scoring explanation;
- separate scores for clichés, abstraction, uniformity and repetition;
- false-positive reduction for academic terminology;
- test corpus of sample documents;
- paragraph and sentence rhythm metrics.

### Технический фокус

- dictionary architecture;
- analyzer modules by responsibility;
- test fixtures;
- deterministic scoring;
- response schema versioning;
- text rhythm statistics;
- paragraph distribution analysis.

### Возможные задачи

- create `analyzer/dictionaries.py`;
- create `analyzer/scoring.py`;
- create `analyzer/sentences.py`;
- create `analyzer/rhythm.py`;
- add unit tests for each scoring component;
- add sample documents to `samples/`;
- add expected result snapshots;
- add response field `schema_version`;
- add paragraph length distribution to analysis result;
- add sentence length variance to analysis result.

### Критерии выхода

- scoring logic покрыт тестами;
- marker explanations стали точнее;
- sample documents дают предсказуемые результаты;
- false positives задокументированы и снижены;
- система умеет фиксировать не только отдельные клише, но и чрезмерную равномерность структуры текста.

## Stage 3: Reporting Workflow

### Цель

Превратить результат анализа в практический редакционный report workflow.

Пользователь должен не только увидеть общий риск, но и получить понятный отчёт: какие признаки найдены, где они находятся, насколько они выражены и что можно исправить вручную.

### Ключевые возможности

- CSV export;
- XLSX export;
- PDF report export;
- document-level recommendations;
- block-level recommendations;
- before/after comparison;
- analysis session history in local storage;
- report metadata;
- grouped marker summary.

### Технический фокус

- report generator;
- frontend report view;
- client-side export;
- optional backend export;
- local browser storage;
- UX improvements;
- before/after diff view.

### Возможные задачи

- add export module;
- add report preview page;
- add downloadable CSV/XLSX;
- add local history without server persistence;
- add comparison between two analysis runs;
- add visual risk distribution;
- add recommendation summary by marker category.

### Критерии выхода

- пользователь может сформировать читаемый отчёт;
- пользователь может сравнить результат до и после ручной правки;
- отчёт можно сохранить и передать;
- хранение исходного документа на сервере не требуется по умолчанию.

## Stage 4: Productization

### Цель

Подготовить проект к реальному использованию за пределами локальной разработки.

Этот этап не должен начинаться до стабилизации local MVP and analysis quality.

### Ключевые возможности

- production deployment;
- authentication;
- optional user accounts;
- persistent analysis history;
- file size limits;
- rate limiting;
- monitoring;
- error tracking;
- deployment documentation.

### Технический фокус

- Docker;
- deployment topology;
- backend production settings;
- frontend production config;
- database decision;
- security hardening;
- observability;
- privacy controls.

### Возможные задачи

- add Dockerfile for backend;
- add Dockerfile for frontend;
- add docker-compose for local production mode;
- add deployment guide;
- add persistent storage for analysis metadata;
- add file upload limits;
- add request logging;
- add error boundary in frontend.

### Критерии выхода

- project can be deployed reproducibly;
- secrets are managed through environment variables;
- production mode is documented;
- basic operational risks are covered;
- privacy assumptions are explicit.

## Stage 5: Intelligent Editorial Assistant

### Цель

Добавить функции редакторской помощи при сохранении user control and transparency.

Stage 5 должен развивать систему от пассивной диагностики к практической редакторской поддержке. При этом оригинальный документ не должен автоматически перезаписываться, а любые внешние AI/LLM-вызовы должны быть опциональными и явно отмеченными.

### Ключевые возможности

- rewrite suggestions for risky sentences;
- explanation of why a sentence is risky;
- tone and academic style recommendations;
- section-level quality diagnostics;
- document structure review;
- anti-template editorial assistance;
- paragraph and sentence rhythm analysis;
- before/after re-analysis;
- optional LLM integration;
- local-only mode remains available.

### Снижение машинной шаблонности академического текста

Система должна помогать пользователю снижать признаки машинной шаблонности без искажения смысла документа.

Функция не должна описываться как обход AI-detectors. Корректная цель — улучшение академического текста за счёт конкретики, авторской логики, неоднородного синтаксиса, практических примеров, расчётной части и явных ограничений метода.

Планируемые возможности:

- выявление чрезмерно гладкой академической структуры;
- выявление универсальных формулировок без привязки к предметной области;
- анализ повторяемости ключевых слов и однотипных конструкций;
- анализ равномерности абзацев и синтаксиса;
- проверка наличия ограничений, допущений и критической позиции;
- проверка таблиц на шаблонность и отсутствие интерпретации;
- проверка наличия расчётной или практической части;
- анализ прикладной конкретности выводов;
- формирование редакционных рекомендаций по каждому найденному признаку;
- повторная проверка документа после ручной переработки.

### Анализ ритма абзацев и предложений

Система должна учитывать не только клише, абстрактные слова и повторяющиеся формулы, но и ритм текста: длину абзацев, длину предложений и повторяемость композиции разделов.

Эмпирически выявленный признак машинной шаблонности: разделы часто строятся слишком равномерно. Например, в разделе может быть ровно два абзаца, каждый примерно по 6–8 строк. Если в разделе есть таблица, структура часто принимает вид:

```text
абзац перед таблицей
таблица
абзац после таблицы
```

Такая структура не всегда ошибочна, но при многократном повторении она создаёт ощущение автоматически собранного учебного текста.

Планируемая функциональность:

- анализировать распределение длины абзацев;
- выявлять соседние разделы, где абзацы имеют почти одинаковый объём;
- выявлять повторяющийся шаблон `paragraph -> table -> paragraph`;
- анализировать среднюю длину предложений;
- анализировать разброс длины предложений;
- отмечать фрагменты, где почти все предложения имеют близкую длину;
- рекомендовать смешивать короткие и сложные предложения;
- рекомендовать использовать абзацы разной длины: короткие переходные абзацы из одного предложения, средние пояснительные абзацы и развёрнутые аналитические абзацы;
- предупреждать, если несколько разделов имеют одинаковую композицию;
- предлагать ручную переработку структуры раздела, а не механическую замену слов.

В реализации нельзя жёстко привязываться к количеству строк в Word, потому что оно зависит от шрифта, полей, масштаба и ширины страницы. Надёжнее анализировать:

```text
количество слов в абзаце;
количество предложений в абзаце;
среднюю длину предложения;
стандартное отклонение длины предложений;
повторяемость количества абзацев по разделам;
наличие одинакового структурного паттерна paragraph/table/paragraph.
```

### Предметная конкретика и практическая проверяемость

Будущий редакторский assistant должен искать места, где текст звучит универсально и может подойти почти к любой теме.

Признаки:

- мало конкретных допущений;
- мало предметных деталей;
- нет примеров последствий;
- нет расчётов;
- таблицы выглядят как универсальные учебные блоки;
- выводы фиксируют общую правильность, но не прикладной результат.

Рекомендации должны предлагать пользователю:

- добавить 2–4 предметные детали;
- указать практические последствия ошибки прогноза, расчёта или решения;
- добавить короткий расчётный пример;
- пояснить происхождение диапазонов в таблицах;
- добавить интерпретацию перед таблицей или после неё;
- сделать вывод более прикладным;
- добавить ограничения модели, метода или исходных данных.

### Ограничения и критическая позиция

Система должна отдельно проверять, есть ли в тексте ограничения, допущения и критическая позиция автора.

Признаки риска:

- метод описан слишком уверенно;
- нет условий применимости;
- нет слабых мест исходных данных;
- нет оговорки о малом объёме наблюдений;
- нет сравнения с простой базовой моделью;
- нет описания ситуации, когда предложенное решение может не сработать.

Рекомендации должны помогать добавить:

- ограничения данных;
- условия применимости метода;
- риск переобучения модели;
- необходимость проверки на отложенном периоде;
- влияние внешних факторов;
- необходимость ручной интерпретации результата.

### Технический фокус

- suggestion pipeline;
- prompt templates;
- optional external provider abstraction;
- privacy controls;
- user confirmation flow;
- version comparison;
- paragraph rhythm analyzer;
- sentence length variance analyzer;
- section structure analyzer;
- table context analyzer;
- recommendation templates by marker category.

### Возможные задачи

- add suggestion API;
- add provider interface;
- add local/manual mode;
- add rewrite suggestion UI;
- add accept/reject workflow;
- add before/after comparison;
- add privacy warnings for external processing;
- add paragraph rhythm metrics;
- add sentence rhythm metrics;
- add table-context diagnostics;
- add anti-template recommendation categories;
- add recommendation templates for specificity, limitations, calculations and conclusion rewriting.

### Критерии выхода

- пользователь может получить редакторские рекомендации;
- рекомендации объяснимы;
- рекомендации не утверждают, что текст точно написан ИИ;
- пользователь может вручную принять или отклонить правки;
- external AI usage is optional and clearly marked;
- original document is never overwritten automatically;
- local-only mode remains available;
- before/after analysis показывает, какие признаки снижены после ручной переработки.

## Long-term ideas

Potential future directions:

- browser extension;
- Google Docs integration;
- Microsoft Word add-in;
- plagiarism-adjacent originality checks;
- academic style profile presets;
- per-university formatting profiles;
- batch document analysis;
- team workspace for editors;
- offline desktop app;
- local model integration;
- Word add-in with paragraph rhythm highlights;
- editable anti-template recommendation profiles.

## Текущий стратегический приоритет

Проект не должен сразу переходить к AI rewriting, user accounts, deployment или storage.

Ближайший приоритет — завершить Stage 1:

1. frontend API client;
2. risky sentence details;
3. analyzer tests;
4. dictionary extraction;
5. CSV/XLSX export;
6. upload validation;
7. documentation updates.

После завершения Stage 1 проект может перейти к Stage 2 и сосредоточиться на качестве анализа.
