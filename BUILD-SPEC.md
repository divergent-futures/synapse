# Build Spec — Synapse (Open Sauce 2026 Enhancement)

*Prepared for: Grok Build / Cowork · Date: 2026-07-07*
*Goal: evolve the working Synapse app into a significantly better version using the requirements below. **Do not patch the built single-file HTML directly** — use and improve the build system (`src/build.py`), which is the proper development workflow.*

> Workflow note (already set up in this repo): source lives in `src/` (`build.py`, `app.head.js`, `app.tail.js`, `app.css`, `brand.svg`) plus `os2026-exhibitors-raw.tsv`. Run `python src/build.py` to regenerate `Synapse-OS2026-App.html`. The richer data model and Helm interchange referenced below are defined in `synapse-interchange-v0.2.json`.

## 1. Project overview

Synapse is a public, standalone, MIT-licensed, offline-first web app that helps people at maker events (Open Sauce and future Sauceathons) discover connections between exhibitors, their projects, industry, funding, and potential collaborators. It must serve two audiences at once:

- **Casual users on the floor** (visitors, exhibitors) — human, visual, actionable.
- **Analytical / institutional users** (universities, grant programs, sponsors, contractors) — strong data views, filtering, ecosystem insights.

The app stays self-contained (single HTML file for distribution) while being generated cleanly from a build process.

## 2. Current state (starting point)

- 5 working tabs: Landscape, Exhibitors, Network, Opportunities, Convergences.
- Embedded JSON with ~225 exhibitors from Open Sauce 2026.
- Basic analytical functionality; currently category-heavy rather than people-focused.
- Space/aero makers exist but lack rich descriptions and public links.

**Non-negotiable:** all original functionality must remain fully working. No regressions.

## 3. Key requirements

**A. People-centric experience (new layer).** Make individual makers and projects feel human and prominent. Prominent public links (Instagram profile, website, YouTube, GitHub, business) in detail panels and cards. Clear "Who you should meet" / complementary-project recommendations. Visual hierarchy that highlights real people and inventions, not just categories.

**B. Personalization / user-type support.** Optional onboarding on open: persona (Visitor one-day, Exhibitor, Industry/Sponsor, Just exploring) + interests (multi-select from existing categories). Generate a "Recommended for you" section from selections; influence chips/filters and surface relevant makers + convergences. Full analytical tabs remain accessible at all times.

**C. Richer data model.** Multi-year history per maker (previous appearances, what they showed, progress over time). Location / state data (regional grants, clusters, local talent). Affiliations (university, school, lab, student-project links — key for young makers). Entrepreneurship signals and work/affiliation data. Stable identity across years via `id` + `external_ids`.

**D. Helm integration.** Continue the Helm↔Synapse interchange format (v0.1 defined; evolve to **v0.2** with the richer fields above — see `synapse-interchange-v0.2.json`). Synapse pushes public maker signals; Helm responds with contextual knowledge (universities, state grants, companies by geo + field) via enrichment requests. Private individuals remain **projects**, not tracked person entities, unless they are genuine public figures.

**E. Dual-audience balance.** Casual users get quick, relevant recommendations without overwhelm; analytical users retain and gain powerful filtering, network views, opportunity mapping, and historical analysis.

## 4. Technical constraints & approach

- **Do not edit the built single-file HTML directly** (this has caused repeated breakage). Use/improve `src/build.py` as the single source of truth.
- Output must remain a single self-contained HTML file for easy event distribution.
- Keep the data-driven architecture (embedded JSON + vanilla JS, no dependencies).
- Respect all existing guardrails: public links only, **no Instagram photo embedding**, attribution, the four Divergent Futures themes (Abundance/Progress/Stagnation/Collapse) used **only as the channel lens**, never as a per-maker rating.

**Recommended development flow:** (1) restore a clean working base from the current build + enriched space data; (2) improve `src/build.py` to generate the enhanced app; (3) add personalization + richer data model through the build; (4) keep all original tabs fully functional.

## 5. Success criteria

- All 5 original tabs work without regression.
- Makers feel like real people with visible projects and easy-to-reach public links.
- Users can quickly personalize their view and get relevant recommendations.
- The app supports future multi-year data and richer signals (location, university links, entrepreneurship).
- The Helm interchange is updated to v0.2 with the new fields.
- `src/build.py` is improved so future changes are safe and maintainable.

## 6. Deliverables

- Updated `src/build.py` that generates the enhanced app cleanly.
- A `Synapse-OS2026-App.html` that is clearly better than the current version in the areas above.
- `synapse-interchange-v0.2.json` (or clear evolution of the format).
- Supporting docs / README updates explaining the new structure.

---

*Instructions for the builder: start from the current working app + this document. Restore/keep full functionality first, then layer on the people-centric experience and personalization through improvements to `src/build.py`. Do not regress any existing tab or feature. The end result should feel like a natural evolution serving both casual floor makers and analytical users, and be ready for multi-year data and Helm integration.*
