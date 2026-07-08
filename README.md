# Synapse

**An open lens on emerging technology — see a maker community whole, and the connections no single participant can.**

Synapse maps the exhibitors and creators of a maker event, surfaces the connections between them that no one in their own booth can see, and reads each convergence for where it's heading — **Abundance, Progress, Stagnation, or Collapse**. First dataset: Open Sauce 2026.

A [Divergent Futures](https://divergentfutures.co) project, released open source so any community can use and adapt it.

## Try it

Open **`Synapse-OS2026-App.html`** in any browser (just double-click it — no install, works offline). Six tabs:

- **For You** — optional personalization. Tell Synapse who you are (Visitor / Exhibitor / Industry-Sponsor / Just exploring) and which fields you care about, and it builds a shortlist of makers to meet and convergences to watch, and pre-selects your fields across every other tab. Stored in `localStorage`; skip it and nothing changes.
- **Landscape** — every exhibitor, grouped into domains, sized by count.
- **Exhibitors** — the full searchable directory. Each maker opens a detail panel with their project, public links, tags, affiliations, location, history, and a **Who you should meet** block of complementary makers in adjacent/convergent fields.
- **Network** — fields as nodes, convergences as threads coloured by path.
- **Opportunities** — each field mapped to adjacent industries, target companies, funding, and sponsors.
- **Convergences** — worked examples of cross-domain combinations, each read through the prism.

## What's in here

- `Synapse-OS2026-App.html` — the interactive app (all data embedded; self-contained). **Generated — never edit by hand.**
- `os2026-exhibitors-raw.tsv` — the source exhibitor table (name, maker, category).
- `src/` — the build system (see below).
- `synapse-interchange-v0.2.json` — the richer data model + the Helm↔Synapse enrichment interchange.
- `Synapse-*.xlsx` — the same data as spreadsheets, for reference.

## How it works

Synapse is data-driven and built from source, never hand-edited. All data lives in one JSON block inside the HTML, produced by `python src/build.py`. The build:

- reads the exhibitor table (`os2026-exhibitors-raw.tsv`),
- widens each maker to the **v0.2 record** (`src/build.py` + `src/enrich.py`),
- concatenates the app logic (`src/app.head.js` + `src/app.tail.js`), styles (`src/app.css`) and mark (`src/brand.svg`) into the single HTML file,
- and self-verifies (no stray NUL bytes, JS parses, all tabs present), printing `-> PASS` / `-> FAIL`.

The idea is portable — point it at another event's exhibitor list and the same views light up.

## Data model (v0.2)

Every exhibitor is emitted with compact base keys (`n` name, `m` maker, `c` category) plus an `id`, plus any **optional** v0.2 fields that have been enriched for that maker — `project`, `description`, `tags[]`, `location{}`, `affiliations[]`, `links[]` (kind-tagged), `entrepreneurship_signals{}`, `history[]`, `external_ids{}`, `is_public_figure`. Empty optionals are dropped, so the app renders only what exists and the long tail stays tiny. The canonical shape and the Helm enrichment interchange are documented in `synapse-interchange-v0.2.json`.

Enrichment lives in `src/enrich.py`, keyed by exact exhibitor name — the place to add real descriptions, affiliations and **public** links. Links are public profile/website URLs only; Instagram is stored as a profile URL and never scraped or photo-embedded.

## Use it for your own event

The data model is generic (exhibitors, fields, convergences). To adapt Synapse to a different maker fair, hackathon, or conference, replace the exhibitor table with your own and regenerate. Rebuild after edits with `python src/build.py` (needs Python 3, no dependencies). Contributions welcome.

## Status

Proof of concept. The Open Sauce 2026 list is a partial snapshot (still growing), categories are auto-derived then hand-cleaned, and region/year layers are scaffolded but need fuller data.

## Data

Exhibitor names, makers, and descriptions are derived from the public [Open Sauce 2026 exhibits page](https://www.opensauce.com/exhibits). Open Sauce is not affiliated with this project.

## Contributing

Issues and pull requests are welcome — better categorisation, new convergences, the build script, or adapting Synapse to other events.

## License

[MIT](LICENSE) © 2026 Divergent Futures. Use it, fork it, build on it.
