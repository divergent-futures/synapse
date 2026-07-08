# BUILD-GUARDRAILS — Synapse

Hard rules. Breaking any of these is a regression.

## Build integrity
- **Never edit `Synapse-OS2026-App.html` directly.** Edit `src/` (or the `.tsv`) and run `python src/build.py`.
- Every change ends with `python src/build.py` printing `-> PASS`. FAIL = do not continue, do not ship.
- Keep the app **single-file, offline, dependency-free** (vanilla JS + embedded JSON). No frameworks, no CDNs, no build tools beyond Python 3 + optional Node for the verify.
- If a write leaves the app blank, suspect trailing NUL bytes — re-run the build and read the VERIFY line.

## No regressions
- All 5 tabs keep working: Landscape, Exhibitors, Network, Opportunities, Convergences.
- Multi-select (chips + bars + network nodes; click again to deselect; "All" clears) keeps working across tabs.
- Landscape bar → drills into that section's exhibitors. Exhibitor row → detail panel. Keep both.

## Brand & content
- The four themes — **Abundance / Progress / Stagnation / Collapse** — are the Divergent Futures *channel lens* (quality of humanity's decisions → trajectory). **Never** stamp them as a rating on an individual maker or convergence.
- Convergence `p` values (green/purple/orange/red) are colour keys only, not judgments.

## Privacy, rights, attribution
- Public profile/website links only. **Never scrape or embed Instagram photos** (ToS + rights + they block it). Link to the profile instead. YouTube/website/GitHub links are fine.
- Private individuals are represented as **projects**, not tracked person-entities, unless they are genuine public figures (`is_public_figure`).
- Keep the attribution: data derived from the public Open Sauce exhibits page; Open Sauce is not affiliated.
- Licence stays MIT.

## Token discipline
- Don't read the built HTML. Work in `src/`. Let `python src/build.py` be the test.
- 2–3 failed attempts → emit a `COWORK HANDOFF` block (see `CLAUDE.md`) and stop.
