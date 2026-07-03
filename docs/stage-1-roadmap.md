# Stage 1 Roadmap: Local DOCX AI-Risk Analyzer MVP

## Stage goal

Stage 1 focuses on turning the current prototype into a stable local MVP for analyzing academic DOCX documents by editorial AI-risk markers.

The product must remain privacy-friendly: documents are uploaded to the local backend, analyzed locally, and are not stored permanently.

## Current baseline

The project already includes:

- FastAPI backend
- DOCX upload endpoint
- text extraction from paragraphs and tables
- heuristic analysis pipeline
- block-level risk scoring
- Next.js frontend
- DOCX upload UI
- summary cards and block table
- environment-based API URL configuration
- backend smoke tests
- GitHub Actions CI for backend and frontend checks

## Stage 1 success criteria

Stage 1 is complete when the system can be used as a reliable local tool for checking DOCX documents and reviewing risk markers.

Required completion criteria:

| Area | Completion criterion |
| --- | --- |
| Backend | API returns stable typed analysis response |
| Frontend | User can upload DOCX and inspect summary, blocks, and risk markers |
| Analysis | Risky sentences and marker details are visible to the user |
| Export | User can export analysis results to CSV or XLSX |
| Reliability | Backend and frontend checks pass in CI |
| Documentation | README, stage roadmap, and strategic roadmap describe current state and next steps |

## Stage 1 scope

### 1. Backend stabilization

Purpose: make the analysis API more maintainable and explicit.

Tasks:

- move API response assembly from `routes/analyze.py` into a service layer
- keep route handlers thin
- add dedicated analyzer unit tests
- add tests for DOCX extraction
- add tests for scoring rules
- add typed error responses for invalid files
- validate oversized files with a clear error message

Expected result:

- backend logic is easier to test
- route layer only handles HTTP concerns
- analyzer layer can evolve independently

Suggested commits:

- `refactor(api): move analysis orchestration to service layer`
- `test(api): add analyzer unit tests`
- `test(api): add DOCX extraction tests`
- `feat(api): validate upload size`

### 2. Frontend API client

Purpose: remove direct fetch logic from the UI component and prepare the frontend for growth.

Tasks:

- create `apps/web/src/lib/api/analyzer.ts`
- move `fetch` logic from `analyzer-upload-form.tsx` into the API client
- create frontend TypeScript types for API response
- handle API errors consistently
- keep UI component focused on state and rendering

Expected result:

- upload form becomes smaller
- API interaction is reusable
- future components can use the same client

Suggested commits:

- `refactor(web): move analyzer request to API client`
- `refactor(web): add analyzer response types`

### 3. Risky sentence details in UI

Purpose: show not only block-level risk, but also concrete text fragments that triggered markers.

Tasks:

- add expandable block rows
- show risky sentences inside each block
- display markers found in each sentence
- show empty state when a block has no risky sentences
- keep table readable on narrow screens

Expected result:

- user can understand why a block received its score
- analysis becomes actionable instead of only numerical

Suggested commits:

- `feat(web): show risky sentence details`
- `style(web): improve block table responsiveness`

### 4. Export results

Purpose: allow the user to save analysis results outside the browser.

Tasks:

- add CSV export for summary and block table
- add XLSX export if practical in Stage 1
- include filename, total stats, block scores, marker counts
- keep export client-side if possible
- avoid storing uploaded documents

Expected result:

- user can download a report after checking a document
- exported file can be attached to academic editing workflow

Suggested commits:

- `feat(web): add CSV export for analysis results`
- `feat(web): add XLSX export for analysis results`

### 5. Analyzer dictionaries

Purpose: make heuristic lists easier to maintain.

Tasks:

- move clichés and abstract words from code constants to separate dictionary module
- split dictionaries by category
- add comments explaining each marker category
- prepare future support for editable dictionaries

Expected result:

- marker lists can grow without making analyzer logic messy
- future UI dictionary editor becomes possible

Suggested commits:

- `refactor(api): extract heuristic dictionaries`
- `test(api): cover dictionary marker matching`

### 6. Documentation

Purpose: keep project understandable as it grows.

Tasks:

- maintain README after every major feature
- document API response structure
- document local development workflow
- document current limitations
- document roadmap updates

Expected result:

- repository remains understandable for future development and portfolio review

Suggested commits:

- `docs(api): describe analysis response fields`
- `docs(roadmap): update stage 1 progress`

## Stage 1 non-goals

The following items are intentionally outside Stage 1:

- user accounts
- cloud deployment
- database persistence
- document history
- paid plans
- team workspace
- official AI-generated text detection claims
- ML-based detector training
- browser extension
- Google Docs integration

These can be considered in later stages after the local MVP is stable.

## Stage 1 implementation order

Recommended order:

1. move frontend fetch logic into API client
2. add frontend response types
3. show risky sentence details in UI
4. add analyzer unit tests
5. extract heuristic dictionaries
6. add CSV export
7. add upload size validation
8. update README and roadmap progress

## Quality gates

Before each merge or push to `main`:

- backend checks must pass:
  - `uv run ruff check src tests`
  - `uv run mypy src`
  - `uv run pytest`
- frontend checks must pass:
  - `pnpm --filter web lint`
  - `pnpm --filter web exec tsc --noEmit`
  - `pnpm --filter web build`
- GitHub Actions CI must be green
- remote repository state must be reviewed after push

## Current priority

Next recommended task:

`refactor(web): move analyzer request to API client`

Reason:

The current UI works, but the upload component owns too much responsibility: file selection, request creation, API call, error handling, and rendering. Moving API logic into a dedicated client will make the frontend easier to extend before adding risky sentence details and export.
