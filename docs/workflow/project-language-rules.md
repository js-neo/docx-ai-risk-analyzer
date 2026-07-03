<!-- docs/workflow/project-language-rules.md -->

# Языковые правила проекта docx-ai-risk-analyzer

## Назначение

Этот документ фиксирует единые языковые правила проекта `docx-ai-risk-analyzer` для документации, Python docstrings, TypeScript/JSDoc, комментариев, тестов, Pull Request descriptions и Codex prompt.

Цель правил — сохранить понятную русскоязычную проектную документацию и одновременно не переводить технические элементы, которые являются частью кода, машинных контрактов или инженерного workflow.

Документ является основным источником языкового стандарта проекта. Если в других документах есть более краткие формулировки, они должны пониматься через правила этого файла.

## Краткий принцип

Поясняющий текст пишется по-русски.

Английский оставляется там, где он выполняет техническую функцию:

```text
имя файла;
путь;
имя модуля;
имя функции;
имя класса;
имя типа;
переменная окружения;
string literal;
error code;
status;
API field;
JSON field;
CLI command;
CI step;
conventional commit;
branch name;
устойчивый инженерный термин.
```

Если английское слово можно естественно заменить русским без потери смысла, его нужно заменить.

## Где русский обязателен

Русский язык обязателен или предпочтителен в следующих местах:

```text
Markdown-документация в docs/**;
roadmap descriptions;
workflow documents;
architecture explanations;
runbooks;
transfer notes;
working-plan descriptions;
Python module docstrings;
Python public function/class docstrings;
Pydantic model explanations;
TypeScript JSDoc for exported components/types/helpers;
module comments;
comments explaining safety/privacy/regression reasons;
frontend user-facing UI text;
error messages shown to the user;
Codex prompt sections explaining goal, scope, constraints and acceptance criteria.
```

## Где английский обязателен или допустим

Английский сохраняется в технических элементах:

| Категория | Примеры |
| --- | --- |
| Code identifiers | `analyzeDocument`, `RiskLevel`, `AnalyzeResponse`, `extract_docx_text` |
| File paths | `apps/api/src/docx_ai_risk_api/analyzer/extraction.py` |
| Env names | `NEXT_PUBLIC_ANALYZER_API_URL` |
| API/JSON fields | `overall_risk`, `risk_score`, `status`, `blocks` |
| Machine-readable values | `low`, `medium`, `high`, `analyzed`, `invalid-file` |
| Commands | `uv run pytest`, `pnpm --filter web build` |
| CI step names | `Run pytest`, `Run ESLint`, `Build frontend` |
| Commit messages | `feat(api): validate upload size` |
| Branch names | `refactor/1.3-analyzer-api-client` |
| Stable terms | `API`, `DTO`, `runtime`, `frontend`, `backend`, `CI`, `PR`, `MVP`, `DOCX`, `FastAPI`, `Pydantic`, `Next.js` |

## Правило первого использования термина

Если английский термин важен и может быть неочевиден, при первом использовании нужно дать русское пояснение.

Примеры:

```text
quality gate (контрольный барьер качества)
runtime (контур выполнения)
schema version (версия схемы ответа)
API client (клиентский модуль для вызова API)
local-first (локальная обработка по умолчанию)
risk marker (маркер риска)
false positive (ложное срабатывание)
```

После первого пояснения термин можно использовать короче.

## Слова, которые нужно переводить в обычном пояснительном тексте

| Не использовать без необходимости | Предпочтительный вариант |
| --- | --- |
| output | результат |
| foundation | основа |
| scope | область изменений / границы задачи |
| safe | безопасный |
| safety | безопасность / защитное ограничение |
| workflow | рабочий процесс |
| test documentation | пояснения к тестам / документация тестов |
| source of truth | источник истины |
| active next candidate | следующий активный срез |
| runtime scope | область runtime-изменений / runtime-контур |
| review | проверка / review, если речь именно о GitHub review |
| checks | проверки |
| validation | проверка / валидация, если речь о валидации данных |
| report | отчёт |

Исключение: английское слово можно оставить, если оно является частью commit title, PR title, API field, string literal, статуса, error code или устойчивого термина проекта.

## Подробность документации кода

Документация кода в проекте должна быть подробной по умолчанию.

Подробная документация не означает комментарий к каждой строке. Она означает, что новый reviewer может понять назначение модуля, границы ответственности, входные данные, результат, ограничения и причины важных проверок без восстановления логики по всему проекту.

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

Каждый новый или изменённый Python source module должен начинаться с подробного module docstring на русском языке.

Хороший module docstring отвечает на вопросы:

```text
1. Что делает модуль?
2. К какому слою относится модуль?
3. Какие данные принимает?
4. Какие данные возвращает?
5. Какие ограничения и safety/privacy assumptions есть?
6. Какие ошибки или edge cases обрабатываются?
```

Пример:

```python
"""Извлечение текста из DOCX-документов.

Модуль относится к analyzer layer и не зависит от FastAPI, request/response
objects или frontend-кода. Его задача — получить бинарное содержимое DOCX,
извлечь paragraphs and tables и вернуть нормализованные текстовые блоки для
дальнейшего эвристического анализа.

Модуль не сохраняет исходный документ на диск и не должен становиться местом
HTTP-валидации. Ошибки чтения файла должны обрабатываться выше, на уровне
service или route layer, чтобы API мог вернуть безопасный user-facing response.
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

Пример подробного function docstring:

```python
def analyze_text_blocks(blocks: list[str]) -> AnalysisResult:
    """Анализирует текстовые блоки и возвращает детерминированный результат.

    Функция не работает с DOCX-файлом напрямую: извлечение текста выполняется
    отдельным модулем `extraction.py`. Такое разделение нужно, чтобы scoring
    можно было тестировать независимо от формата файла.

    Args:
        blocks: Нормализованные текстовые блоки документа. Каждый блок обычно
            соответствует группе абзацев или таблиц после DOCX extraction.

    Returns:
        AnalysisResult: Сводный результат анализа с общим уровнем риска,
        суммарным баллом и block-level детализацией.

    Ограничения:
        Результат не является доказательством AI generation. Это эвристическая
        редакционная оценка, которую пользователь должен интерпретировать вручную.
    """
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

Пример:

```python
class AnalyzeSummary(BaseModel):
    """Сводная часть результата анализа DOCX-документа.

    Модель используется во внешнем API response и должна оставаться стабильной
    для frontend. Поля отражают редакционную оценку риска, а не доказательство
    происхождения текста.
    """

    overall_risk: RiskLevel = Field(
        description="Общий уровень редакционного риска: low, medium или high."
    )
```

## TypeScript, React и JSDoc

Новые или изменённые exported components, API clients, exported types and non-trivial helpers должны иметь русскоязычный JSDoc или module-level comment.

Пример:

```ts
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

## Комментарии в тестах

Названия тестов могут оставаться на английском, если они используются как машинно-ориентированное описание поведения.

Комментарии и docstrings в тестах пишутся на русском языке, если они объясняют:

```text
какую регрессию защищает тест;
какую privacy boundary нельзя нарушить;
почему конкретное значение не должно попасть в ответ;
почему expected value важен для scoring behavior;
почему ошибка должна быть safe and user-facing.
```

Пример:

```python
def test_invalid_docx_does_not_expose_stack_trace() -> None:
    """Проверяет, что ошибка чтения DOCX не раскрывает внутренний traceback.

    Это privacy/safety regression test: пользователь должен получить понятную
    ошибку, но API не должен возвращать детали исключения, пути файлов или
    внутренние stack traces.
    """
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

Пример:

```text
API недоступен. Проверьте, что FastAPI backend запущен на localhost:8000.
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

Примеры:

```json
{
  "status": "analyzed",
  "overall_risk": "low",
  "risk_score": 3
}
```

Но user-facing interpretation этих значений во frontend должна быть на русском:

```text
low -> Низкий
medium -> Средний
high -> Высокий
```

## Documentation and roadmap

Roadmap descriptions читаются как проектная документация. Поэтому commit title можно оставить на английском, но описание результата, причин, границ и рисков должно быть на русском.

Проблемный вариант:

```text
Next recommended task: refactor(web): move analyzer request to API client.
Reason: upload component owns too much responsibility.
```

Предпочтительный вариант:

```text
Следующая рекомендуемая задача: `refactor(web): move analyzer request to API client`.
Причина: компонент загрузки сейчас отвечает одновременно за выбор файла, API-запрос,
обработку ошибок и отображение результата. Эту ответственность нужно разделить.
```

## Codex prompt language rules

Каждый Codex prompt должен содержать блок Language rules, если задача затрагивает docs, comments, docstrings, tests, UI text or roadmap.

Рекомендуемый блок:

```text
Language rules:
- Поясняющий текст в docs, Python docstrings, JSDoc, comments, roadmap descriptions and test comments пишется преимущественно на русском.
- English оставляем только для commit titles, file/module names, identifiers, literal values, API fields, statuses, error codes and stable engineering terms.
- Не смешивать обычные English words в русском пояснении, если есть естественный русский эквивалент.
- Использовать: результат, основа, область изменений, проверки, источник истины, пояснения к тестам.
- Избегать: output, foundation, scope, checks, source of truth, test documentation в обычной пояснительной прозе.
```

## Codex prompt code documentation rules

Если задача затрагивает код, Codex prompt должен содержать отдельное требование к документации кода:

```text
Code documentation rules:
- Preserve or expand detailed Russian code documentation.
- New or changed Python modules must include Russian module docstrings.
- Public Python functions, classes and Pydantic models must have Russian docstrings when they define project behavior or API contracts.
- New or changed exported frontend types, API clients and non-trivial components must have Russian JSDoc or module comments.
- Documentation must explain purpose, layer boundaries, inputs, outputs, limitations and privacy/safety assumptions where relevant.
- Do not remove or shorten existing docstrings, JSDoc or comments without explicit justification.
```

## PR body, commit message and CLI

Git commit message остаётся conventional commit на английском:

```text
feat(api): validate upload size
refactor(web): move analyzer request to API client
docs(workflow): add project language rules
```

PR title может быть английским и должен отражать commit purpose.

PR body может содержать английские технические элементы, но поясняющий текст желательно писать на русском.

CLI output, CI logs, runtime logs, event names, statuses, error codes and diagnostic codes остаются на английском.

## Мини-чеклист review языковых правил

Перед merge проверить:

```text
1. docs, docstrings, JSDoc and comments написаны преимущественно на русском;
2. английские слова являются identifiers, file paths, literal values, API fields or stable terms;
3. обычные слова output, foundation, scope, checks, source of truth не используются без необходимости;
4. сложные английские термины при первом использовании объяснены по-русски;
5. frontend user-facing text на русском;
6. machine-readable statuses, error codes and API fields на английском;
7. тестовые комментарии объясняют регрессию или safety/privacy boundary;
8. PR body не содержит случайного смешения языков в обычной пояснительной прозе;
9. новые или изменённые Python modules имеют подробные русские module docstrings;
10. public functions, Pydantic models, exported frontend types and API clients документированы достаточно подробно.
```

## Короткая версия правила

Пиши пояснения по-русски.

Английский оставляй только там, где это имя кода, путь, literal, commit title, API field, error code, machine-readable status или устойчивый engineering term.

Если английское слово можно естественно перевести без потери смысла — переводи.

Документация кода должна быть подробной по умолчанию: объясняй назначение, границы ответственности, входы, результат, ограничения и privacy/safety assumptions, но не комментируй очевидный синтаксис.
