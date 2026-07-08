# START HERE — Claude Code

You're enhancing **Synapse**. Everything you need is in this repo. Build through `src/build.py` only (see `CLAUDE.md`).

## Read in this order
1. `CLAUDE.md` — the working agreement + the golden rule (build via `src/`, never edit the HTML).
2. `BUILD-SPEC.md` — the requirements (what to build and why).
3. `synapse-interchange-v0.2.json` — the data model / schema to build toward.
4. `BUILD-GUARDRAILS.md` — hard do/don'ts.
5. `HANDOFF.md` — background/context (optional).

## Repo map
- `Synapse-OS2026-App.html` — generated output (do not edit).
- `src/build.py` — generator; holds `FIELDS` (opportunity map) + `CONV` (convergences) inline; self-verifies on run.
- `src/app.head.js` + `src/app.tail.js` — app logic. `src/app.css`, `src/brand.svg` — style + mark.
- `os2026-exhibitors-raw.tsv` — exhibitor rows (name, maker, category).
- `Synapse-*.xlsx` — same data as spreadsheets (reference).

## Run & verify (one command)
```
python src/build.py
```
Look for the final line: `VERIFY nul=0 js_parses=yes 5tabs=ok -> PASS`. Only PASS is shippable. No dependencies, no API keys needed for the core build.

## Build order (phased — verify PASS after each phase, confirm all 5 tabs still work)

**Phase 0 — baseline.** Run `python src/build.py`, confirm PASS. Open the HTML once to see the 5 tabs. Don't change anything yet.

**Phase 1 — data model.** In `src/build.py`, widen each exhibitor record to the v0.2 shape (id, external_ids, tags, description, location, affiliations, links[], entrepreneurship_signals, history[], is_public_figure) — all optional, default empty. Update `src/app.*.js` so the detail panel renders these **when present** and ignores them when absent. No visible change with empty data = no regression.

**Phase 2 — people-centric UI.** Make exhibitor cards and the detail panel feel human: prominent public links (website, YouTube, GitHub, Instagram *profile*, business), the project up front, and a "Who you should meet" block (complementary makers in adjacent/convergent fields).

**Phase 3 — personalization.** Optional onboarding on open: persona (Visitor / Exhibitor / Industry-Sponsor / Just exploring) + interests (multi-select of existing categories), stored in `localStorage`. Add a "Recommended for you" section that surfaces relevant makers + convergences and pre-seeds the field selection. Analytical tabs stay fully accessible.

**Phase 4 — data enrichment (separate data task).** Populate `description` + `links[]` per exhibitor from their public Open Sauce exhibit page. Respect the Instagram guardrail (link, never scrape photos). This fills the structure built in Phase 1.

## Definition of done
- `python src/build.py` prints `-> PASS`.
- All 5 original tabs work; no feature removed.
- Makers show as real people with reachable public links.
- A user can personalize and get relevant recommendations.
- Data model supports multi-year, location, affiliations, entrepreneurship (even if some fields are still empty).
- `synapse-interchange-v0.2.json` reflects any field changes you make.
