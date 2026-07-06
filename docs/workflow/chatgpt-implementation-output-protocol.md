<!-- docs/workflow/chatgpt-implementation-output-protocol.md -->

# ChatGPT implementation output protocol

## Purpose

This document defines how ChatGPT must present implementation work while the project is developed through chat-based manual commits.

It is not a Codex protocol and not a Codex prompt template.

This protocol exists because the current development mode is:

~~~text
ChatGPT analyzes the repository and prepares an atomic commit.
ChatGPT outputs changed modules in chat.
The developer manually applies files locally.
The developer runs checks, commits and pushes.
ChatGPT can then review the remote state.
~~~

When Codex is connected later, Codex-specific instructions must live in separate documents:

~~~text
docs/workflow/github-pr-orchestration.md
docs/workflow/codex-implementation-protocol.md
docs/workflow/codex-prompt-template.md
~~~

## Audience

This document is agent-facing operational workflow text. Therefore it is English-first.

User-facing explanations in chat may be Russian, because the project owner is Russian-speaking.

## Scope

This protocol applies when ChatGPT writes implementation instructions directly in chat.

It covers:

1. Commit description format.
2. Current project point analysis.
3. Changed module list.
4. Full module output format.
5. Rules for targeted replacements.
6. Module size reduction explanations.
7. Check commands.
8. Git add and commit commands.
9. PowerShell/Bash command safety.
10. Out-of-scope boundaries.

## Required reading before implementation

Before preparing any implementation commit, ChatGPT must read or verify the relevant current repository context:

~~~text
AGENTS.md
docs/README.md
docs/stage-1-roadmap.md
docs/strategic-roadmap.md
docs/workflow/project-language-rules.md
docs/workflow/project-development-rules.md
relevant source modules
relevant tests
relevant package/config/workflow files
~~~

For docs-only changes, read the relevant docs and documentation index.

For backend changes, read the affected backend modules, schemas and tests.

For frontend changes, read the affected components, frontend API clients, shared types and package scripts.

Do not rely on old chat memory if it conflicts with repository state.

## Required response structure

Every implementation response must start with the commit title:

~~~text
Коммит N.M — type(scope): message
~~~

Example:

~~~text
Коммит 1.4 — docs(workflow): add development and ChatGPT output protocols
~~~

After the title, ChatGPT must provide a short current-point analysis:

~~~text
Короткий анализ текущей точки проекта:
- какие модули найдены;
- какие boundaries затрагиваются;
- какие DDD boundaries затрагиваются;
- какие existing helpers/contracts/scripts можно переиспользовать;
- почему commit scope должен быть ограничен;
- какие non-regression risks нужно учитывать.
~~~

For docs-only tasks, the analysis may focus on documentation ownership, active/planned docs, update policy and scope boundaries.

## Changed module list format

After the analysis, ChatGPT must list all changed modules.

Required format:

~~~text
Коммит включает N позиций:

1. path/to/file — новый модуль — назначение
2. path/to/file — изменить — назначение
3. path/to/file — удалить — назначение, если удаление явно approved
~~~

Use exact repository paths.

Do not hide package/config/docs changes.

If a file is only partially changed, mark it as `изменить` and describe the exact purpose.

## Commit purpose section

After the module list, ChatGPT must include:

~~~text
Назначение коммита:
<плотное описание, что меняется и зачем>
~~~

The purpose must explain:

1. What the commit changes.
2. Why the change is needed now.
3. What is intentionally out of scope.
4. Whether existing behavior or documentation is preserved.

## Module output format

For each new source module, output the full module.

Python module format:

~~~~text
1/N — Новый модуль: apps/api/path/to/module.py

~~~python
# apps/api/path/to/module.py
"""Русский module docstring."""

...
~~~
~~~~

TypeScript/TSX module format:

~~~~text
2/N — Новый модуль: apps/web/src/path/to/module.tsx

~~~tsx
// apps/web/src/path/to/module.tsx
'use client';

...
~~~
~~~~

Markdown module format:

~~~~text
3/N — Новый модуль: docs/path/to/file.md

~~~~md
<!-- docs/path/to/file.md -->

# Title

...
~~~~
~~~~

Use tilde fences for Markdown files or any answer that contains nested fenced blocks. This avoids accidental ChatGPT-generated service attributes in triple-backtick fences.

## Targeted replacement format

Do not rewrite large existing files without need.

If a small section changes inside a large existing module, prefer a targeted replacement.

Required format:

~~~text
X/N — Изменённый модуль: path/to/file

Точечно замени только раздел:
<heading or unique anchor>

Было:
<old block>

Станет:
<new block>
~~~

Use targeted replacement for:

1. `AGENTS.md` section edits.
2. `docs/README.md` index updates.
3. `package.json` script additions when full file output is unnecessary.
4. Large source files where a small change is safer.

If the user explicitly asks for the full final module, output the full module, but first verify that no existing content is accidentally removed.

## Module size reduction rule

If a changed module becomes smaller, ChatGPT must explicitly add a section:

~~~text
Почему модуль стал меньше
~~~

That section must explain:

1. What was removed or extracted.
2. Where the removed/extracted content moved.
3. Why this is not functional degradation.
4. Why documentation/docstrings/JSDoc were not lost.
5. Which check or diff confirms safety.

If ChatGPT cannot verify safety, it must not claim that the reduction is safe. It must ask for the current module or diff.

This rule applies to code and documentation.

Wrong:

~~~text
В коммите нет сокращения существующих модулей.
~~~

when a changed file actually became smaller.

Correct:

~~~text
AGENTS.md changes only the Required documents section. No broad replacement is allowed.
If local diff shows a large deletion, stop and restore AGENTS.md before committing.
~~~

## Markdown fence rule

For Markdown modules and nested code examples, use tilde fences:

~~~~text
~~~~md
# Markdown file

~~~text
nested block
~~~
~~~~
~~~~

Do not use triple-backtick fenced blocks for large Markdown files in ChatGPT output, because the chat renderer can add service metadata to the fence and pollute copied files.

## Language requirements in output

ChatGPT's explanatory response to the owner should be Russian.

Technical identifiers remain English:

~~~text
file paths;
function names;
type names;
API fields;
machine-readable statuses;
error codes;
CI commands;
commit messages.
~~~

Code documentation must follow project language rules:

1. Python docstrings — Russian-first.
2. TypeScript/JSDoc — Russian-first.
3. Frontend user-facing text — Russian.
4. Agent-facing workflow rules — English-first.
5. Owner-facing roadmap explanations — Russian-first.

## PowerShell and Bash command rules

The project owner may use PowerShell or Git Bash.

ChatGPT must not mix command syntax silently.

For PowerShell, do not use Bash line continuation `\`.

Correct PowerShell one-line command:

~~~powershell
git add docs/README.md AGENTS.md
~~~

Correct PowerShell multiline command:

~~~powershell
git add `
  docs/README.md `
  AGENTS.md
~~~

Correct Bash multiline command:

~~~bash
git add \
  docs/README.md \
  AGENTS.md
~~~

If the user is currently in PowerShell, prefer one-line commands unless multiline is necessary.

## Required final sections

Every implementation response must end with:

~~~text
Проверки
Git add
Коммит
~~~

For backend changes:

~~~bash
cd apps/api
uv run ruff check src tests
uv run mypy src
uv run pytest
~~~

For frontend changes:

~~~bash
pnpm --filter web lint
pnpm --filter web exec tsc --noEmit
pnpm --filter web build
~~~

For docs-only changes:

~~~powershell
git status --short
git --no-pager diff --stat
git --no-pager diff -- <changed-files>
~~~

Git add section must match the user's shell.

PowerShell example:

~~~powershell
git add docs/workflow/project-development-rules.md docs/workflow/chatgpt-implementation-output-protocol.md docs/README.md AGENTS.md
~~~

Commit section:

~~~powershell
git commit -m "docs(workflow): add development and ChatGPT output protocols"
git push
git status
~~~

## Out-of-scope rule

Do not implement tasks from the next stage inside the current commit.

If analysis shows that a separate architecture preparation is needed, ChatGPT must propose a future commit instead of implementing it inside the current scope.

Examples:

1. Do not add Codex prompt template inside ChatGPT output protocol commit.
2. Do not add runtime analyzer features inside docs workflow commits.
3. Do not add external AI integration without approved architecture scope.
4. Do not refactor frontend code inside documentation commits.
5. Do not change API contracts inside docs-only commits.

## Post-push review expectation

After the user pushes, ChatGPT should help verify:

1. Commit hash and message.
2. Remote branch state.
3. `git status` clean output.
4. Whether the diff matches the intended scope.
5. Whether any documentation index or roadmap should be updated next.

If a mistake is found before commit, fix it locally.

If a mistake is found after push, decide whether to add a corrective follow-up commit or revert, depending on severity.