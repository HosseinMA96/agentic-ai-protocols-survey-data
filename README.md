# Data and scripts for "Agentic AI Protocols" (survey)

Supporting data for the survey *Agentic AI Protocols: A Survey of Interoperability Standards, Their
Evolution, and Open Challenges* (H. Mohasel Arjomandi and A. GhaffarTehrani, preprint, November 2026).
Survey cutoff: October 31, 2026. Archived versions: [10.5281/zenodo.24000345](https://doi.org/10.5281/zenodo.24000345) (all versions; v1.2: [10.5281/zenodo.24072244](https://doi.org/10.5281/zenodo.24072244); v1.1: [10.5281/zenodo.24058686](https://doi.org/10.5281/zenodo.24058686))
(concept DOI for the latest version: [10.5281/zenodo.24000345](https://doi.org/10.5281/zenodo.24000345)).

This repository contains the arXiv harvest and screening sheet, the coding of every MCP and A2A
changelog change against the six design pressures, the coverage checks (competing-survey
bibliographies, title retrieval, and the OpenAlex supplementary search with its manual screening),
the reference-verification reports, and the scripts that produce them.

## Contents

| Path | What it is | Used in the paper |
|---|---|---|
| `data/harvest/harvest.json`, `screening.csv` | 847 unique arXiv records (Nov. 2024 to Oct. 2026) from six queries, with the protocol-centric flag and keyword category | §II-A, Figs. 1–2 |
| `data/harvest/learning_screen.tsv`, `learning_screen_decisions.tsv` | Learning-centric screen of the 379 protocol-centric records: 37 flagged by the keyword rule (7 already cited) and the decision, with its reason, for each of the other 30 (9 included) | §II-A, §V-C, Table II |
| `data/coding/dp_coding.tsv` | 113 changelog changes (MCP 2025-03-26 to 2026-07-28; A2A 0.2.1–0.3.0 and 0.3→1.0), each with concern plane and primary/secondary design pressure (adjudicated codes, used in Table VI) | §II-C, §IX-B, Table VI |
| `data/coding/CODEBOOK.md` | Coding rules for DP1–DP6, "other", and planes | §II-C |
| `data/coding/second_coder_sample.tsv` | Blinded 30-item sample for an independent second coder (blank form) | §II-C |
| `data/coding/second_coder_sample_filled.tsv` | The second coder's codes for the 30 items (primary pressure, plane, confidence, notes) | §II-C |
| `data/coding/dp_coding_pre_adjudication.tsv` | First codes before adjudication (the basis of the reported κ) | §II-C |
| `data/coding/kappa_output.txt` | Cohen's κ: primary pressure 0.868 (27/30), plane 0.833 (26/30); lenient agreement 28/30 | §II-C |
| `data/coding/adjudication.tsv` | The six disagreements and their resolution (four first codes changed) | §II-C |
| `data/coverage/first_run/gaps.tsv` | Works cited by competing surveys and not by us (first run, Nov. 1, 2026) | §II-E |
| `data/coverage/rerun_2026-11-05/surveys.txt`, `gaps.tsv`, `log.txt` | The 16 surveys used and the re-run of the gap list | §II-E |
| `data/coverage/rerun_2026-11-05/title_retrieval.tsv` | 341 arXiv records whose titles name MCP, A2A, or an agent protocol, with overlap flags | §II-E |
| `data/coverage/rerun_2026-11-05/openalex.tsv`, `openalex_summary.txt` | OpenAlex supplementary search (1,259 records) with arXiv-only, in-harvest, and title-rule flags | §II-B |
| `data/coverage/rerun_2026-11-05/openalex_peer256_screened.tsv` | Manual screening of all 256 peer-reviewed-type delta records into five categories | §II-B |
| `data/coverage/coverage_check_added_keys.txt` | Works added after the coverage check (bib key, arXiv id) | Table II |
| `data/verification/arxiv_id_check.tsv` | Title and first-author check of every cited arXiv identifier | References |
| `data/verification/doi_check*.tsv` | Crossref check (title, first author, venue, year) of every DOI | References |
| `data/verification/withdrawn_check.tsv` | Withdrawal check of every cited arXiv preprint | References |
| `data/verification/provenance_summary.txt` | Provenance counts of the 278 cited works | Table II |
| `data/bib/references.bib`, `cited_keys.txt`, `manual.bib` | Final bibliography, the keys cited in the paper, and hand-verified entries | — |
| `scripts/harvest.py`, `screen.py`, `arxiv.py` | arXiv harvest, title-rule screening, BibTeX from the arXiv API | §II-A |
| `scripts/learning_screen.py` | Learning-centric keyword screen of the protocol-centric pool | §II-A |
| `scripts/build_coding.py`, `kappa.py` | Changelog coding and summary tables; Cohen's κ for the second coder | §IX-B |
| `scripts/coverage_gap.py`, `title_retrieval.py`, `openalex_supplement.py` | Coverage checks and supplementary search | §II-B, §II-E |
| `scripts/provenance.py` | Table II | §II-A |
| `scripts/verify_arxiv_ids.py`, `verify_dois.py`, `check_withdrawn.py`, `cr.py`, `build_bib.py`, `fix_bib_round1.py` | Reference verification and bibliography normalization | References |

## Reproduce the numbers

Run from the repository root (Python 3, standard library only):

```bash
python3 scripts/build_coding.py            # Table VI: 113 changes, 92 explained by DP1-DP6
python3 scripts/provenance.py              # Table II: provenance of the 278 cited works
python3 scripts/learning_screen.py         # learning-centric screen: 37 flagged, 7 cited before it, 9 added
python3 scripts/verify_arxiv_ids.py data/bib/references.bib out.tsv
python3 scripts/verify_dois.py data/bib/references.bib out.tsv
python3 scripts/check_withdrawn.py data/bib/references.bib out.tsv
python3 scripts/title_retrieval.py data/harvest/screening.csv data/bib/references.bib out.tsv
python3 scripts/openalex_supplement.py data/harvest/screening.csv data/bib/references.bib out.tsv
(cd data/coding && python3 ../../scripts/kappa.py second_coder_sample_filled.tsv dp_coding_pre_adjudication.tsv)   # reported kappa
```

The harvest and network-based checks query live APIs (arXiv, Crossref, Semantic Scholar, OpenAlex),
so counts can drift slightly as these services update their records. The files in `data/` are the
outputs used in the paper.

## Sources of the changelog coding

- MCP changelogs: `https://modelcontextprotocol.io/specification/{2025-03-26,2025-06-18,2025-11-25,2026-07-28}/changelog`
- A2A: `https://github.com/a2aproject/A2A/blob/main/CHANGELOG.md` (v0.2.1–v0.3.0) and
  `https://a2a-protocol.org/latest/whats-new-v1/` (0.3 → 1.0). Fetched November 5, 2026.

## License

Scripts: MIT. Data in `data/`: CC BY 4.0. See `LICENSE`. Records derived from arXiv, Crossref, and
OpenAlex metadata keep the terms of those services (arXiv metadata and OpenAlex are CC0).

## Changes in version 1.2 (November 2026)

- Second coder for the changelog coding: the survey's second author, blinded to the first codes and without AI
  tools, coded the 30-item sample (`data/coding/second_coder_sample_filled.tsv`). Cohen's κ against the first codes
  before adjudication: primary pressure 0.868 (27/30), plane 0.833 (26/30) (`kappa_output.txt`; reproduce with the
  `kappa.py` command above).
- The six disagreements were adjudicated after κ was computed (`data/coding/adjudication.tsv`); four first codes
  changed. `dp_coding.tsv` now holds the adjudicated codes (92 of 113 changes explained by DP1–DP6, previously 90);
  the earlier codes are in `dp_coding_pre_adjudication.tsv`. `kappa.py` takes the first-coder file as an optional
  second argument.

## Changes in version 1.1 (November 2026)

- Learning-centric screen of the protocol-centric pool (`scripts/learning_screen.py`, `data/harvest/learning_screen*.tsv`):
  9 works added, so the survey now cites 278 works (Table II gains the row "added by learning-centric screen").
- Bibliography: protocol names braced in titles so that sentence-casing styles keep their capitals; compound
  surnames (Soria Parra, De Rossi, La Malfa) braced. The 9 new arXiv identifiers were added to the identifier
  and withdrawal checks in `data/verification/`.

## Citation

Please cite the survey (arXiv identifier to be added) and this repository:

H. Mohasel Arjomandi, *Data and Scripts for "Agentic AI Protocols"*, version 1.2, Zenodo, 2026.
DOI (all versions, resolves to the latest): [10.5281/zenodo.24000345](https://doi.org/10.5281/zenodo.24000345)
