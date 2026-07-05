# Prism

**An open lens on emerging technology — see a maker community whole, and the connections no single participant can.**

Prism maps the exhibitors and creators of a maker event, surfaces the connections between them that no one in their own booth can see, and reads each convergence for where it's heading — **Abundance, Progress, Stagnation, or Collapse**. First dataset: Open Sauce 2026.

A [Divergent Futures](https://divergentfutures.co) project, released open source so any community can use and adapt it.

## Try it

Open **`Prism-OS2026-App.html`** in any browser (just double-click it — no install, works offline). Five tabs:

- **Landscape** — every exhibitor, grouped into domains, sized by count.
- **Exhibitors** — the full searchable directory.
- **Network** — fields as nodes, convergences as threads coloured by path.
- **Opportunities** — each field mapped to adjacent industries, target companies, funding, and sponsors.
- **Convergences** — worked examples of cross-domain combinations, each read through the prism.

## What's in here

- `Prism-OS2026-App.html` — the interactive app (all data embedded; self-contained).
- `Prism-OS2026-Exhibitors.xlsx` — the exhibitor dataset: directory, category landscape, convergence examples.
- `Prism-Field-Opportunity-Map.xlsx` — each field mapped to industries, companies, funding, and in-room sponsors.
- `os2026-exhibitors-raw.tsv` — the source data table (single source of truth).

## How it works

Prism is data-driven: all data lives in one JSON block inside the HTML, generated from the source table. The idea is portable — point it at another event's exhibitor list and the same views light up.

## Use it for your own event

The data model is generic (exhibitors, fields, convergences). To adapt Prism to a different maker fair, hackathon, or conference, replace the exhibitor table with your own and regenerate. A reusable build script is on the roadmap — contributions welcome.

## Status

Proof of concept. The Open Sauce 2026 list is a partial snapshot (still growing), categories are auto-derived then hand-cleaned, and region/year layers are scaffolded but need fuller data.

## Data

Exhibitor names, makers, and descriptions are derived from the public [Open Sauce 2026 exhibits page](https://www.opensauce.com/exhibits). Open Sauce is not affiliated with this project.

## Contributing

Issues and pull requests are welcome — better categorisation, new convergences, the build script, or adapting Prism to other events.

## License

[MIT](LICENSE) © 2026 Divergent Futures. Use it, fork it, build on it.
