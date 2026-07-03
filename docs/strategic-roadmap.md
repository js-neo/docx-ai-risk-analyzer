# Strategic Roadmap

## Product vision

`docx-ai-risk-analyzer` is a privacy-friendly tool for editorial analysis of academic DOCX documents.

The product does not claim to prove AI generation. Instead, it helps the user find linguistic, structural, and statistical markers that may require manual editing.

The long-term goal is to build a practical local-first document analysis system that helps students, editors, and authors review formal academic texts before submission.

## Strategic principles

### 1. Local-first and privacy-friendly

Uploaded documents should be processed locally by default. Long-term storage must be optional and explicit.

### 2. Explainable analysis

The tool must show why a fragment is considered risky. Numeric scores without explanations are not enough.

### 3. Editorial assistant, not AI police

The product should help improve text quality. It should not present itself as an official detector or as proof of AI usage.

### 4. Incremental development

Each stage must produce a usable product increment with tests, documentation, and CI.

### 5. Portfolio-grade engineering

The repository should demonstrate modern engineering practices:

- monorepo structure
- backend and frontend separation
- typed API contracts
- automated tests
- CI
- clear roadmap
- conventional commits
- documentation

## Stage overview

| Stage | Name | Main outcome |
| --- | --- | --- |
| Stage 1 | Local MVP | Stable local DOCX analyzer with UI, risk details, and export |
| Stage 2 | Analysis Quality | Better heuristics, configurable dictionaries, stronger tests |
| Stage 3 | Reporting Workflow | Reports, history, comparison, and document revision support |
| Stage 4 | Productization | Deployment, authentication, persistence, and user workflows |
| Stage 5 | Intelligent Editorial Assistant | Assisted rewriting suggestions and deeper document diagnostics |

## Stage 1: Local MVP

### Goal

Create a stable local tool for uploading DOCX files, analyzing risk markers, and reviewing results in the browser.

### Key capabilities

- DOCX upload
- local backend analysis
- summary metrics
- block-level risk table
- risky sentence details
- CSV/XLSX export
- stable CI
- clear documentation

### Technical focus

- FastAPI backend structure
- Next.js frontend structure
- analyzer unit tests
- typed response models
- frontend API client
- local-first operation

### Exit criteria

- user can analyze a DOCX document locally
- user can inspect risky blocks and sentences
- user can export the result
- CI is green
- documentation reflects actual project state

## Stage 2: Analysis Quality

### Goal

Improve the usefulness and accuracy of the heuristic analysis.

### Key capabilities

- marker categories
- configurable dictionaries
- improved Russian sentence splitting
- improved scoring explanation
- separate scores for clichés, abstraction, uniformity, and repetition
- false-positive reduction for academic terminology
- test corpus of sample documents

### Technical focus

- dictionary architecture
- analyzer modules by responsibility
- test fixtures
- deterministic scoring
- response schema versioning

### Possible tasks

- create `analyzer/dictionaries.py`
- create `analyzer/scoring.py`
- create `analyzer/sentences.py`
- add unit tests for each scoring component
- add sample documents to `samples/`
- add expected result snapshots
- add response field `schema_version`

### Exit criteria

- scoring logic is covered by tests
- marker explanations are more precise
- sample documents produce predictable results
- false positives are documented and reduced

## Stage 3: Reporting Workflow

### Goal

Turn analysis output into a practical editorial report workflow.

### Key capabilities

- CSV export
- XLSX export
- PDF report export
- document-level recommendations
- block-level recommendations
- before/after comparison
- analysis session history in local storage
- report metadata

### Technical focus

- report generator
- frontend report view
- client-side export
- optional backend export
- local browser storage
- UX improvements

### Possible tasks

- add export module
- add report preview page
- add downloadable CSV/XLSX
- add local history without server persistence
- add comparison between two analysis runs
- add visual risk distribution

### Exit criteria

- user can generate a readable report
- user can compare results after editing
- report can be saved and shared
- no document storage is required by default

## Stage 4: Productization

### Goal

Prepare the project for real usage beyond local development.

### Key capabilities

- production deployment
- authentication
- optional user accounts
- persistent analysis history
- file size limits
- rate limiting
- monitoring
- error tracking
- deployment documentation

### Technical focus

- Docker
- deployment topology
- backend production settings
- frontend production config
- database decision
- security hardening
- observability

### Possible tasks

- add Dockerfile for backend
- add Dockerfile for frontend
- add docker-compose for local production mode
- add deployment guide
- add persistent storage for analysis metadata
- add file upload limits
- add request logging
- add error boundary in frontend

### Exit criteria

- project can be deployed reproducibly
- secrets are managed through environment variables
- production mode is documented
- basic operational risks are covered

## Stage 5: Intelligent Editorial Assistant

### Goal

Add assisted editing features while keeping user control and transparency.

### Key capabilities

- rewrite suggestions for risky sentences
- explanation of why a sentence is risky
- tone and academic style recommendations
- section-level quality diagnostics
- document structure review
- optional LLM integration
- local-only mode remains available

### Technical focus

- suggestion pipeline
- prompt templates
- optional external provider abstraction
- privacy controls
- user confirmation flow
- version comparison

### Possible tasks

- add suggestion API
- add provider interface
- add local/manual mode
- add rewrite suggestion UI
- add accept/reject workflow
- add before/after comparison
- add privacy warnings for external processing

### Exit criteria

- user can receive editing suggestions
- suggestions are explainable
- external AI usage is optional and clearly marked
- original document is never overwritten automatically

## Long-term ideas

Potential future directions:

- browser extension
- Google Docs integration
- Microsoft Word add-in
- plagiarism-adjacent originality checks
- academic style profile presets
- per-university formatting profiles
- batch document analysis
- team workspace for editors
- offline desktop app
- local model integration

## Current strategic priority

The project should not jump directly to AI rewriting, accounts, deployment, or storage.

The next priority is to complete Stage 1:

1. frontend API client
2. risky sentence details
3. analyzer tests
4. dictionary extraction
5. CSV/XLSX export
6. upload validation
7. documentation updates

After Stage 1 is complete, the project can move into Stage 2 and focus on analysis quality.
