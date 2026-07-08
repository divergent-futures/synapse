# Synapse — Handoff & Expansion Brief

*For the cohort table picking this up. Everything you need to understand it, run it, and expand it. — Divergent Futures*

---

## The idea in one breath

At a maker event, everyone is stuck in their own silo. 800 exhibitors, one busy weekend, and the collaborators who should meet never do. **Synapse is the brain that wires those silos together** — it maps everyone, then surfaces the connections no single booth can see: maker-to-maker, maker-to-industry, and maker-to-funding. The name is the mission: a synapse is the link that carries a signal between otherwise-isolated cells.

It's a [Divergent Futures](https://divergentfutures.co) project, released open source (MIT) so any community can use and extend it. First dataset: **Open Sauce 2026** (~225 exhibitors, a partial snapshot).

## What it does today

A single, self-contained HTML app (no install, works offline). Five tabs:

- **Landscape** — the whole room by domain; click a bar to drill into that section's exhibitors.
- **Exhibitors** — searchable directory; click anyone for a detail panel.
- **Network** — fields as nodes, convergences as threads; multi-select nodes to isolate connections.
- **Opportunities** — each field mapped to adjacent industries, target companies, funding, and the Open Sauce sponsors already in the room.
- **Convergences** — worked cross-domain combinations (what X + Y makes possible) with a real commercial/funding pathway.

Multi-select works across every tab (chips at top, or click bars/nodes/cards; click again to deselect).

**The one honest gap:** exhibitor detail panels don't have real bios/links yet — they show a placeholder plus a "search the web" link. Filling that in is the obvious first expansion (see below).

## How it's built (so you can change it)

Synapse is **data-driven and dependency-free**. All data is baked into one JSON block inside the HTML, generated from source files by a small Python script. No frameworks, no build tools beyond Python 3.

Repo layout:

- `Synapse-OS2026-App.html` — the built app (what you ship / open).
- `os2026-exhibitors-raw.tsv` — the exhibitor data (name, maker, category). **Single source of truth for exhibitors.**
- `src/build.py` — the generator. Also holds the `FIELDS` (opportunity map) and `CONV` (convergences) data inline — edit those lists here.
- `src/app.head.js` + `src/app.tail.js` — the app's UI logic (split in two halves for a tooling quirk; they're just concatenated).
- `src/app.css` — styles. `src/brand.svg` — the logo mark.
- `Synapse-OS2026-Exhibitors.xlsx`, `Synapse-Field-Opportunity-Map.xlsx` — the same data as spreadsheets, for reference/editing.

**To rebuild:** edit the data or any `src/` file, then run:

```
python src/build.py
```

It reads the `.tsv` + the `src/` pieces + the `FIELDS`/`CONV` lists and rewrites `Synapse-OS2026-App.html`. Refresh the browser. That's the whole loop.

## Where to take it (expansion menu, roughly in priority order)

1. **Exhibitor enrichment.** Scrape each Open Sauce exhibit page (`opensauce.com/exhibits/<slug>`) for the full description and any links the maker published (website, YouTube, socials). Populate `desc` and a `links` array per exhibitor — the detail panel already renders them. *Biggest single value-add.*
2. **Location / region layer.** Add each exhibitor's state to the data. Then build a regional view — "what would a Sauceathon in Ohio look like." (Divergent Futures cares a lot about this for regional expansion.)
3. **Year-over-year layer.** Add a `year` field and load multiple events, so you can watch domains and convergences shift over time. The data model already anticipates this.
4. **AI-assisted convergences.** Auto-suggest maker↔maker and maker↔industry combinations from the category tags, with a human curating. Right now the convergences are hand-written examples.
5. **Real matchmaking.** Go past field-level: per-exhibitor "who you should meet" and specific company/grant matches.
6. **Sharper categories.** The categories are auto-derived then hand-cleaned; refine them, or allow multi-tagging.
7. **A real back end.** When it needs to be multi-user or live, promote the JSON model to a database (e.g. SQLite/Supabase) + a hosted app with an editing UI. The data shape is designed to move cleanly.
8. **Mobile + Network polish.** It'll get shown on phones at events; make it responsive. Curved/bundled edges and node tooltips would make the Network tab sing.

## Guardrails (please keep these)

- **The four themes — Abundance / Progress / Stagnation / Collapse — are the Divergent Futures channel lens, not a rating for individual makers.** They describe the quality of *humanity's* decisions and where they lead. Don't stamp them on individual exhibitors or convergences (an earlier version did, and a backyard rocket is not "Collapse").
- **Don't scrape or embed Instagram photos.** It's against their terms, technically blocked, and raises rights questions. Link out to profiles instead. YouTube and website links are fine to collect.
- **Attribution.** Exhibitor data is from the public Open Sauce exhibits page; Open Sauce is not affiliated with this project. Keep the note in the README.
- **Stay open.** MIT licensed — build on it, fork it, but keep the spirit: hand makers the map, don't gatekeep it.

## Links

- Repo: `github.com/divergent-futures/prism` *(may be renamed to `synapse`)*
- Divergent Futures: divergentfutures.co

*Have fun with it — the whole point is connecting the room. Make it connect more of it.*
