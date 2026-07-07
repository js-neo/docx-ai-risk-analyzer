<!-- docs/workflow/pr-body-and-extended-description-contract.md -->

# PR body and Extended description contract

## Назначение

Этот документ фиксирует workflow contract для подготовки финального GitHub-facing `PR body` и `Extended description` в проекте `docx-ai-risk-analyzer`.

Контракт нужен, чтобы разделить три разных слоя:

1. `Codex report` — factual implementation report по diff и проверкам.
2. ChatGPT / human owner review — русскоязычное owner-facing объяснение, planning, review verdict и risk analysis в чате.
3. GitHub-facing `PR body` и `Extended description` — English-first review artifacts, которые вручную вставляются в GitHub после review.

Главное правило:

~~~text
ChatGPT owner-facing review/planning -> Russian-first.
GitHub-facing PR body and Extended description -> English-first.
Codex prompt/control-plane blocks -> English-first.
Repository explanatory documentation -> Russian-first.
Code and machine-readable contracts -> English.
User-facing product text -> Russian.
~~~

Этот документ не заменяет `AGENTS.md`, `docs/README.md`, `docs/workflow/project-language-rules.md`, `docs/workflow/project-development-rules.md` или `docs/workflow/github-pr-orchestration.md`. Он уточняет только ответственность за финальные GitHub-facing PR artifacts.

## Почему PR body и Extended description пишутся English-first

`PR body` и `Extended description` не являются обычной русскоязычной проектной документацией.

Это долговечные GitHub review artifacts рядом с:

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

Поэтому финальный GitHub-facing `PR body` и `Extended description` в этом проекте пишутся English-first.

При этом ChatGPT review, commit planning, request-changes rationale, approve rationale, scope discussion и owner-facing объяснения в чате остаются Russian-first.

## Разделение ролей

### Codex

Codex не владеет финальным GitHub-facing `PR body` по умолчанию.

Codex должен возвращать factual implementation report:

~~~text
1. Changed files.
2. New files.
3. Deleted files.
4. Rationale.
5. Diff summary.
6. Exact validation commands and results.
7. Test accounting.
8. Non-regression report.
9. Module size impact.
10. Known risks and limitations.
11. Follow-up recommendations outside scope.
12. Suggested conventional commit message.
13. PR body responsibility checklist.
~~~

Codex не должен:

~~~text
write the final GitHub-facing PR body by default;
write the final Extended description by default;
mark a PR as Ready without required gates;
claim checks passed without exact output;
include private DOCX content, personal data, stack traces or raw local paths;
expand scope to improve PR wording.
~~~

Исключение возможно только если owner явно просит Codex подготовить draft text для дальнейшего human review.

### ChatGPT

ChatGPT используется как reviewer, planning assistant and owner-facing explanation layer.

ChatGPT может:

~~~text
review PR metadata, diff, changed files, CI status and comments;
explain risks in Russian;
prepare request-changes or approve rationale in Russian;
prepare final GitHub-facing PR body in English;
prepare final Extended description in English;
prepare optional merge/review comment in English if it will be pasted into GitHub;
explain Module size impact based on actual diff, not intention.
~~~

ChatGPT не должен:

~~~text
claim that checks passed without evidence;
invent files, tests, CI status or runtime behavior;
include citations inside copyable PR body or Extended description;
include private document text or sensitive data;
treat old chat memory as more reliable than repository state.
~~~

### Owner

Owner остаётся final owner проекта.

Owner:

~~~text
reviews Codex report;
reviews ChatGPT explanation;
checks final PR body and Extended description;
manually inserts final GitHub-facing text into GitHub;
decides whether PR can be marked Ready, merged, split, closed or sent back for changes;
owns secrets, production operations, review resolution and final merge decision.
~~~

## Общие правила подготовки GitHub-facing PR artifacts

Финальный `PR body` и `Extended description` должны быть factual and grounded in actual diff/checks.

Запрещено включать:

~~~text
real uploaded document text;
private academic documents;
personal data from documents;
real API keys;
tokens;
private URLs;
local paths from stack traces;
raw exception details;
private screenshots;
citations inside copyable GitHub text;
unverified claims about checks, CI or behavior.
~~~

Разрешено включать:

~~~text
repository file paths;
commit hashes;
PR numbers;
branch names;
CI check names;
sanitized error summaries;
synthetic examples;
high-level privacy-safe summaries;
exact local command results provided by owner or Codex.
~~~

Если checks не запускались, это нужно писать явно:

~~~text
Not run — docs-only change; runtime checks were not required.
Not run — local environment unavailable; GitHub Actions must cover this.
Failed — exact failure reason...
Skipped — exact reason...
~~~

Нельзя заменять actual validation общими словами вроде `standard checks passed`.

## PR body structure

Canonical GitHub-facing `PR body` использует English headings:

~~~markdown
### Motivation

### Description

### Testing

### Runtime impact

### Non-regression

### Module size impact

### Known limitations
~~~

Эти headings не переводятся.

### Motivation

`Motivation` объясняет, зачем PR нужен сейчас.

Он должен отвечать на вопросы:

~~~text
why this PR exists;
which roadmap/workflow/stage gap it closes;
why the change belongs in one atomic PR;
what risk or missing capability it addresses.
~~~

Пример:

~~~~markdown
### Motivation

- Add the missing PR body ownership contract before introducing Codex implementation prompts.
- Align the project workflow with the strict route-cost model: Codex returns factual reports, while the owner prepares final GitHub-facing PR artifacts.
- Prevent future PR descriptions from mixing owner-facing Russian review text with GitHub-facing English review artifacts.
~~~~

### Description

`Description` описывает actual changed files/modules, grouped by purpose.

Пример:

~~~~markdown
### Description

- Added `docs/workflow/pr-body-and-extended-description-contract.md`.
  - Defines the responsibility split between Codex reports, ChatGPT review and final GitHub-facing PR artifacts.
  - Documents English-first PR body and Extended description requirements.
  - Adds DOCX analyzer-specific non-regression and privacy checks.

- Updated `docs/README.md`.
  - Added the new workflow contract to existing workflow documents.
  - Added recommended reading for PR body and Extended description preparation tasks.

- Updated `AGENTS.md`.
  - Added the contract as required reading for PR body, Extended description and GitHub-facing merge/review comment tasks.
~~~~

### Testing

`Testing` фиксирует exact commands and results.

Docs-only пример:

~~~~markdown
### Testing

- `git status --short` — passed; working tree contained only the intended docs changes before commit.
- `git --no-pager diff --stat` — passed; reviewed changed-file summary.
- `git --no-pager diff -- docs/workflow/pr-body-and-extended-description-contract.md docs/README.md AGENTS.md` — passed; reviewed intended docs-only diff.
- Runtime checks — not run; this PR changes documentation only.
- Test accounting: added 0 tests, modified 0 tests, removed 0 tests.
~~~~

Если backend менялся:

~~~~markdown
### Testing

- `cd apps/api && uv run ruff check src tests` — passed.
- `cd apps/api && uv run mypy src` — passed.
- `cd apps/api && uv run pytest` — passed: <N> passed, 0 failed.
- Test accounting: added <N> tests, modified <N> tests, removed <N> tests.
~~~~

Если frontend менялся:

~~~~markdown
### Testing

- `pnpm --filter web lint` — passed.
- `pnpm --filter web exec tsc --noEmit` — passed.
- `pnpm --filter web build` — passed.
- Test accounting: added <N> tests, modified <N> tests, removed <N> tests.
~~~~

### Runtime impact

`Runtime impact` явно фиксирует, влияет ли PR на runtime.

Docs-only пример:

~~~~markdown
### Runtime impact

No runtime impact.

- Backend source files were not changed.
- Frontend source files were not changed.
- API contracts were not changed.
- Analyzer scoring behavior was not changed.
- DOCX extraction behavior was not changed.
- CI workflows, package files, dependencies and environment variables were not changed.
- User document handling and privacy behavior were not changed.
~~~~

Runtime PR должен перечислять affected areas:

~~~text
Backend API: affected/not affected
Analyzer domain logic: affected/not affected
DOCX extraction: affected/not affected
Risk scoring: affected/not affected
Frontend upload UI: affected/not affected
Frontend API client: affected/not affected
Export/reporting: affected/not affected
Privacy/user document handling: affected/not affected
CI/workflows: affected/not affected
Dependencies/env: affected/not affected
~~~

### Non-regression

`Non-regression` должен быть checklist-style.

Минимальный checklist для `docx-ai-risk-analyzer`:

~~~~markdown
### Non-regression

- Docs changed: yes — <explanation>.
- Runtime code changed: no/yes — <explanation>.
- Backend API changed: no/yes — <explanation>.
- Analyzer domain logic changed: no/yes — <explanation>.
- DOCX extraction changed: no/yes — <explanation>.
- Risk scoring changed: no/yes — <explanation>.
- Frontend upload UI changed: no/yes — <explanation>.
- Frontend API client changed: no/yes — <explanation>.
- Export/reporting behavior changed: no/yes — <explanation>.
- API contracts changed: no/yes — <explanation>.
- User-facing text changed: no/yes — <explanation>.
- Privacy/user document handling changed: no/yes — <explanation>.
- Dependencies changed: no/yes — <explanation>.
- Workflows/env files changed: no/yes — <explanation>.
- Tests changed: no/yes — <explanation>.
- Tests removed or weakened: no/yes — <explanation>.
- Files deleted: no/yes — <explanation>.
- Exported symbols removed: no/yes — <explanation>.
- Python docstrings / JSDoc / module comments removed or shortened: no/yes — <explanation>.
- Fallback / validation / error-handling branches removed: no/yes — <explanation>.
- Sensitive data added: no/yes — <explanation>.
- Intentionally changed behaviors: <list or none>.
- Preserved behaviors: <task-specific list>.
~~~~

### Module size impact

`Module size impact` обязателен даже для docs-only PR.

Если сокращений нет:

~~~~markdown
### Module size impact

No existing source, test or documentation module was shortened.

The PR adds a new workflow document and only updates documentation indexes / required-reading sections.
~~~~

Если файл стал меньше:

~~~~markdown
### Module size impact

`docs/README.md` became smaller because the repeated planned-document entry was moved into a dedicated source-of-truth document:

- Moved from: `docs/README.md`
- Moved to: `docs/workflow/pr-body-and-extended-description-contract.md`
- Reason: `docs/README.md` is an index, not the canonical contract body.
- Documentation was not lost; the detailed contract now lives in the dedicated workflow document.
- Runtime behavior was not affected.
~~~~

Если безопасность сокращения нельзя подтвердить, нельзя писать, что всё безопасно.

### Known limitations

`Known limitations` фиксирует intentionally out-of-scope items.

Пример:

~~~~markdown
### Known limitations

- Does not add the Codex implementation protocol.
- Does not add the Codex prompt template.
- Does not change runtime backend/frontend behavior.
- Does not change analyzer scoring, DOCX extraction or export behavior.
- Does not run backend/frontend checks because the PR is docs-only.
~~~~

## Extended description structure

`Extended description` — это concise narrative summary for GitHub/review context.

Он пишется English-first.

Он должен включать:

~~~text
what the PR adds or changes;
why the change matters now;
how it preserves workflow/runtime/privacy boundaries;
which future workflow step it prepares;
what remains out of scope.
~~~

Он не должен включать:

~~~text
long checklists;
full file-by-file diff;
citations;
secrets;
private document content;
raw local paths;
unverified CI claims;
owner-facing Russian review rationale.
~~~

Пример:

~~~~markdown
This PR adds the missing PR body and Extended description contract before enabling broader Codex-assisted implementation.

It preserves the owner-managed workflow used in route-cost: Codex returns factual implementation reports, ChatGPT/human review prepares the final English-first GitHub-facing PR artifacts, and the owner remains responsible for manually inserting final PR text and making the merge decision.

The change is documentation-only and does not affect backend runtime, frontend runtime, DOCX extraction, analyzer scoring, API contracts, CI workflows, dependencies or user document handling.
~~~~

## Formatting contract

Когда owner просит:

~~~text
PR body и Extended description выведи отдельными блоками в markdown
~~~

ChatGPT должен вывести два отдельных raw Markdown blocks:

~~~text
PR body
<raw markdown block>

Extended description
<raw markdown block>
~~~

Внутри copyable GitHub text не должно быть citations.

Citations допустимы только outside copyable blocks, в owner-facing review answer.

## Language contract

### GitHub-facing artifacts

GitHub-facing artifacts пишутся English-first:

~~~text
PR body;
Extended description;
PR title;
branch name;
conventional commit message;
merge/review comment intended to be pasted into GitHub.
~~~

### Owner-facing chat

Owner-facing chat остаётся Russian-first:

~~~text
commit planning;
scope discussion;
review verdict;
request-changes explanation;
approve rationale;
risk explanation;
manual local command guidance;
post-push review explanation.
~~~

### Repository docs

Explanatory repository documentation пишется Russian-first:

~~~text
Markdown docs;
roadmap notes;
transfer notes;
runbooks;
architecture explanations;
workflow explanations;
JSDoc/module comments;
explanatory test comments;
project governance docs.
~~~

### Control-plane blocks

Control-plane blocks пишутся English-first:

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

### Code and machine-readable contracts

Code-adjacent and machine-readable entities remain English:

~~~text
code identifiers;
type names;
function names;
variable names;
file paths;
branch names;
env names;
CLI commands;
CI step names;
API/DTO fields;
statuses;
error codes;
diagnostic codes;
runtime log events;
JSON keys;
conventional commit messages.
~~~

### User-facing product text

User-facing product text для русскоязычного продукта пишется на русском:

~~~text
frontend labels;
button text;
form hints;
validation messages;
empty states;
error explanations shown to the user;
support instructions.
~~~

Machine-readable error code remains English, visible message remains Russian:

~~~~json
{
  "code": "INVALID_DOCX_FILE",
  "message": "Загрузите корректный DOCX-файл."
}
~~~~

## PR body responsibility checklist

Every Codex report must include:

~~~text
- PR Body / Extended description updated by Codex: no
- Manual PR Body and Extended description update required by owner: yes
- ChatGPT/human owner will prepare final English-first PR Body, Extended description and optional GitHub-facing review/merge comment from the Codex report.
- Owner will paste the final GitHub-facing text into GitHub manually and remains final merge owner.
~~~

If owner explicitly asks Codex to draft PR text, the report must say:

~~~text
- PR Body / Extended description drafted by Codex for owner review: yes
- Final owner review required before GitHub insertion: yes
~~~

## Review checklist

When reviewing PR body or Extended description, check:

~~~text
- GitHub-facing PR body is English-first.
- Extended description is English-first.
- ChatGPT owner-facing review remains Russian-first outside copyable GitHub blocks.
- No citations are inside copyable GitHub text.
- No private DOCX content is included.
- No personal data from uploaded documents is included.
- No raw stack traces or local paths are included.
- Testing section contains exact commands and exact results.
- Runtime impact is explicit.
- Non-regression report is task-specific, not generic.
- Module size impact is explicit.
- Known limitations do not promise future runtime features.
- PR body does not claim checks passed unless output confirms it.
- Docs-only PR clearly states no runtime impact.
- Runtime PR lists affected backend/frontend/analyzer/privacy areas.
~~~

## Relationship to Codex implementation protocol

`docs/workflow/codex-implementation-protocol.md` must reference this document.

Codex implementation protocol should explain:

~~~text
Codex returns factual implementation report.
Codex does not own final GitHub-facing PR body by default.
ChatGPT/human owner prepares final English-first PR body and Extended description.
Owner manually inserts final text into GitHub and remains final merge owner.
~~~

## Relationship to Codex prompt template

`docs/workflow/codex-prompt-template.md` must include the PR body responsibility checklist.

The prompt template should not duplicate this document completely. It should link to this contract and include the minimal required checklist.

## Definition of done

PR body / Extended description preparation is complete only when:

1. The final `PR body` is English-first.
2. The final `Extended description` is English-first.
3. Both are based on actual diff and actual check results.
4. Testing results are exact or explicitly marked as not run / skipped / failed.
5. Runtime impact is explicit.
6. Non-regression report is task-specific.
7. Module size impact is explicit.
8. Known limitations are honest and scoped.
9. No private user document content or sensitive data is included.
10. Owner has reviewed and accepted the final GitHub-facing text.
