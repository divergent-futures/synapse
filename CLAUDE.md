# CLAUDE.md — Synapse working agreement (read first)

Synapse is a single-file, offline, dependency-free web app (vanilla JS + embedded JSON) that maps maker-event exhibitors and the connections between them. You are enhancing it per `BUILD-SPEC.md`.

## THE GOLDEN RULE

**Never edit `Synapse-OS2026-App.html` directly.** It is a generated artifact. Editing it by hand is what broke every previous attempt.

Edit only:
- `src/app.head.js`, `src/app.tail.js` — the app logic (two halves, concatenated).
- `src/app.css` — styles. `src/brand.svg` — logo mark.
- `os2026-exhibitors-raw.tsv` — exhibitor data.
- `src/build.py` — the generator; also holds the `FIELDS` and `CONV` data inline.

Then regenerate + self-verify with ONE command:

```
python src/build.py
```

It prints a line ending in `-> PASS` or `-> FAIL`. **If it says FAIL, stop and fix before doing anything else.** FAIL means null bytes crept in or the JS doesn't parse — the app will be blank in a browser.

## Token discipline

- Do **not** read `Synapse-OS2026-App.html` (it's ~44KB minified — wastes tokens). Work in `src/`.
- Make targeted edits to the small `src/` files. Re-run `python src/build.py` to check — don't eyeball the built file.
- The build command is your test. Trust the `PASS/FAIL` line; don't re-verify by reading the output.

## Known environment gotcha

Writes in this environment occasionally append trailing NUL (`\x00`) bytes that silently break the HTML. `build.py` strips NULs from its inputs, and the verify step catches any that reach the output. If a change ever makes the app blank, the cause is almost always this — re-run the build and read the VERIFY line.

## Guardrails (full list in BUILD-GUARDRAILS.md)

- All 5 tabs (Landscape, Exhibitors, Network, Opportunities, Convergences) must keep working. No regressions.
- The four themes (Abundance/Progress/Stagnation/Collapse) are the Divergent Futures **channel lens only** — never a per-maker rating.
- Public profile links only. **Never scrape or embed Instagram photos** — link to profiles.
- Keep the app single-file, offline, dependency-free.

## Escalation — don't flail

If a problem isn't solved in 2–3 attempts, STOP and emit a `COWORK HANDOFF` block instead of burning tokens:

```
COWORK HANDOFF
Goal: <what you were doing>
Tried: <approaches>
Error: <exact message + file:line>
Question: <what you need decided>
```

TJ pastes that back into Cowork to diagnose against the real files.

Work in **Accept edits** mode. Data model / schema is `synapse-interchange-v0.2.json`.
