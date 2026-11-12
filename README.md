# Data and scripts for "Agentic AI Protocols" (survey)

Supporting data for the survey *Agentic AI Protocols: A Survey of Interoperability Standards, Their
Evolution, and Open Challenges* (H. Mohasel Arjomandi and A. GhaffarTehrani, preprint, November 2026).
Survey cutoff: October 31, 2026. Archived versions: [10.5281/zenodo.24000345](https://doi.org/10.5281/zenodo.24000345) (all versions; v1.6: [10.5281/zenodo.24151561](https://doi.org/10.5281/zenodo.24151561); v1.5: [10.5281/zenodo.24096592](https://doi.org/10.5281/zenodo.24096592); v1.4: [10.5281/zenodo.24096244](https://doi.org/10.5281/zenodo.24096244); v1.3: [10.5281/zenodo.24074354](https://doi.org/10.5281/zenodo.24074354); v1.2: [10.5281/zenodo.24072244](https://doi.org/10.5281/zenodo.24072244); v1.1: [10.5281/zenodo.24058686](https://doi.org/10.5281/zenodo.24058686))
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
| `data/coding/second_coder_sample_filled.tsv` | The second coder's codes for the 30 items (round 1: primary pressure, plane, confidence, notes) | §II-C |
| `data/coding/second_coder_part2_filled.tsv` | The second coder's codes for the other 77 items (round 2; all items except the 30 and the six worked examples) | §II-C |
| `data/coding/second_coder_all_filled.tsv` | Both rounds joined: 107 double-coded items | §II-C |
| `data/coding/dp_coding_pre_adjudication.tsv` | First codes before any adjudication (the basis of every reported κ) | §II-C |
| `data/coding/kappa_output.txt` | Round 1, Cohen's κ: primary pressure 0.868 (27/30), plane 0.833 (26/30); lenient agreement 28/30 | §II-C |
| `data/coding/kappa_output_part2.txt` | Round 2: primary 0.834 (67/77), plane 0.780 (63/77); all 107 items: primary 0.844 (94/107), plane 0.797 (89/107); lenient 70/77, 98/107 | §II-C |
| `data/coding/adjudication.tsv` | Round 1: the six disagreements and their resolution (four first codes changed) | §II-C |
| `data/coding/adjudication_part2.tsv` | Round 2: the 19 disagreements, their resolution, and the changelog text behind each (15 first codes changed) | §II-C |
| `scripts/adjudication_direction.py` | Direction of adjudication: for each disagreeing code, whether the second coder's code, the first code, or a third code was adopted (23 / 8 / 0 of 31) | Appendix A |
| `data/coding/adjudication_check_instructions.md` | Instructions for the second author's blind check of the adjudication (each disagreeing code shown as two unlabeled options, resolution hidden) | Appendix A |
| `data/coding/adjudication_check_key.tsv` | Key of the check: for each of the 31 rows, which option is the first / second code and the adjudicated code | Appendix A |
| `data/coding/adjudication_check_scored.tsv` | The second author's choice, confidence, and reason for each of the 31 codes, scored against the adjudication (20 of 31 agree) | Appendix A |
| `scripts/adjudication_check_summary.py` | Summary of the check: 20 / 31 agree with the adjudication (17 / 23 resolved to the second code, 3 / 8 first codes kept); 22 / 31 equal the second author's earlier code | Appendix A |
| `data/coding/second_coder_instructions.md` | Instructions given to the second coder: rules, codebook, procedure, six worked examples outside the sample, FAQ | §II-C |
| `data/coverage/first_run/gaps.tsv` | Works cited by competing surveys and not by us (first run, Nov. 1, 2026) | §II-E |
| `data/coverage/rerun_2026-11-05/surveys.txt`, `gaps.tsv`, `log.txt` | The 16 surveys used and the re-run of the gap list | §II-E |
| `data/coverage/rerun_2026-11-05/title_retrieval.tsv` | 341 arXiv records whose titles name MCP, A2A, or an agent protocol, with overlap flags | §II-E |
| `data/coverage/uncited_flagged_pool.tsv` | The 143 protocol-centric pool records flagged by the title retrieval that the survey does not cite, with keyword category (one withdrawn by its authors) | §II-E |
| `data/coverage/rerun_2026-11-05/openalex.tsv`, `openalex_summary.txt` | OpenAlex supplementary search (1,259 records) with arXiv-only, in-harvest, and title-rule flags | §II-B |
| `data/coverage/rerun_2026-11-05/openalex_peer256_screened.tsv` | Manual screening of all 256 peer-reviewed-type delta records into five categories | §II-B |
| `data/coverage/coverage_check_added_keys.txt` | Works added after the coverage check (bib key, arXiv id) | Table II |
| `data/verification/arxiv_id_check.tsv` | Title and first-author check of every cited arXiv identifier | References |
| `data/verification/doi_check*.tsv` | Crossref check (title, first author, venue, year) of every DOI | References |
| `data/verification/withdrawn_check.tsv` | Withdrawal check of every cited arXiv preprint | References |
| `data/verification/provenance_summary.txt` | Provenance counts of the 280 cited works | Table II |
| `data/bib/references.bib`, `cited_keys.txt`, `manual.bib` | Final bibliography, the keys cited in the paper, and hand-verified entries | — |
| `scripts/harvest.py`, `screen.py`, `arxiv.py` | arXiv harvest, title-rule screening, BibTeX from the arXiv API | §II-A |
| `scripts/learning_screen.py` | Learning-centric keyword screen of the protocol-centric pool | §II-A |
| `scripts/build_coding.py`, `kappa.py` | Changelog coding and summary tables; Cohen's κ for the second coder | §IX-B |
| `scripts/coverage_gap.py`, `title_retrieval.py`, `openalex_supplement.py`, `uncited_flagged.py` | Coverage checks and supplementary search | §II-B, §II-E |
| `scripts/provenance.py` | Table II | §II-A |
| `scripts/verify_arxiv_ids.py`, `verify_dois.py`, `check_withdrawn.py`, `cr.py`, `build_bib.py`, `fix_bib_round1.py` | Reference verification and bibliography normalization | References |

## Reproduce the numbers

Run from the repository root (Python 3, standard library only):

```bash
python3 scripts/build_coding.py            # Table VI: 113 changes, 91 explained by DP1-DP6
python3 scripts/provenance.py              # Table II: provenance of the 280 cited works
python3 scripts/learning_screen.py         # learning-centric screen: 37 flagged, 7 cited before it, 9 added
python3 scripts/verify_arxiv_ids.py data/bib/references.bib out.tsv
python3 scripts/verify_dois.py data/bib/references.bib out.tsv
python3 scripts/check_withdrawn.py data/bib/references.bib out.tsv
python3 scripts/title_retrieval.py data/harvest/screening.csv data/bib/references.bib out.tsv
python3 scripts/openalex_supplement.py data/harvest/screening.csv data/bib/references.bib out.tsv
(cd data/coding && python3 ../../scripts/kappa.py second_coder_sample_filled.tsv dp_coding_pre_adjudication.tsv)   # kappa, round 1
(cd data/coding && python3 ../../scripts/kappa.py second_coder_part2_filled.tsv dp_coding_pre_adjudication.tsv)    # kappa, round 2
(cd data/coding && python3 ../../scripts/kappa.py second_coder_all_filled.tsv dp_coding_pre_adjudication.tsv)      # kappa, all 107 items
python3 scripts/adjudication_direction.py   # Appendix A: adjudication outcome per disagreeing code
python3 scripts/adjudication_check_summary.py   # Appendix A: second author's blind check of the adjudication
```

The harvest and network-based checks query live APIs (arXiv, Crossref, Semantic Scholar, OpenAlex),
so counts can drift slightly as these services update their records. The files in `data/` are the
outputs used in the paper.

## Sources of the changelog coding

- MCP changelogs: `https://modelcontextprotocol.io/specification/{2025-03-26,2025-06-18,2025-11-25,2026-07-28}/changelog`
- A2A: `https://github.com/a2aproject/A2A/blob/main/CHANGELOG.md` (v0.2.1–v0.3.0) and
  `https://a2a-protocol.org/latest/whats-new-v1/` (0.3 → 1.0). Fetched November 5, 2026.
- Item IDs: `<revision>#<n>` is the n-th change in the order the source lists it (MCP: the listed items of each
  changelog page in page order, numbering continuing across its sections; A2A 0.2–0.3: the feature and breaking-change entries of v0.2.1–v0.3.0 in `CHANGELOG.md`, oldest first;
  A2A 1.0: the changes in the migration guide in page order). `scripts/build_coding.py` holds the item list.

## License

Scripts: MIT. Data in `data/`: CC BY 4.0. See `LICENSE`. Records derived from arXiv, Crossref, and
OpenAlex metadata keep the terms of those services (arXiv metadata and OpenAlex are CC0).

## Changes in version 1.6 (November 2026)

- Blind check of the adjudication by the survey's second author (Appendix A): each of the 31 disagreeing codes was
  shown as two unlabeled options in random order, with the changelog entry and without the resolution
  (`adjudication_check_instructions.md`, `adjudication_check_key.tsv`). The second author's choice, confidence, and
  reason for each code are in `adjudication_check_scored.tsv`; `scripts/adjudication_check_summary.py` summarizes
  them: 20 of 31 choices equal the adjudicated code (17 of the 23 codes resolved to the second coder's code, 3 of the
  8 first codes kept), and 22 of 31 equal the second coder's earlier code. The adjudicated codes were not changed.
  The second author confirmed not having seen the adjudication files or the survey's description of the recodes
  before the check.

## Changes in version 1.5 (November 2026)

- `scripts/adjudication_direction.py`: the direction of adjudication reported in the survey's Appendix A
  (of 31 disagreeing codes, 23 resolved to the second coder's code, 8 kept the first code, none to a third code;
  no code on which the coders agreed was changed).

## Changes in version 1.4 (November 2026)

- Second round of the changelog coding: the survey's second author, blinded to the first codes and without AI
  tools, coded the items in two rounds: the 30-item sample (`second_coder_sample_filled.tsv`; κ primary 0.868, plane
  0.833) and the other 77 items except the six worked examples shown in the instructions
  (`second_coder_part2_filled.tsv`; κ primary 0.834, plane 0.780). Before round 2 the coder confirmed not having seen
  the first codes of any of its items. Over all 107 items: κ primary 0.844, plane 0.797. Agreement is lowest for DP3.
- Disagreements were adjudicated by the first author, supported by an AI assistant, after κ was computed for the
  round (`adjudication.tsv`: four first codes changed; `adjudication_part2.tsv`: 15 changed). `dp_coding.tsv` holds
  the adjudicated codes (91 of 113 changes explained by DP1–DP6; 90 before round 1, 92 before round 2);
  the original first codes are in `dp_coding_pre_adjudication.tsv`. `kappa.py` takes the first-coder file as an
  optional second argument. `scripts/build_coding.py` writes `data/coding/dp_coding.tsv`.
- `README.md` and `CODEBOOK.md` describe both rounds; Table VI counts per protocol, period, pressure, and plane change
  with the round-2 adjudication (§II-C, §IV, §IX-B of the survey).

## Changes in version 1.3 (November 2026)

- Bibliography: the extensions-framework proposal SEP-2133 is cited (grey literature), so the survey now cites 280 works
  (`provenance_summary.txt`: grey literature 42); the MCP Bridge entry notes that the cited results are in arXiv
  version 2 (January 2026).
- New `data/coverage/uncited_flagged_pool.tsv` and `scripts/uncited_flagged.py`: the 143 protocol-centric pool records
  that the title retrieval flagged but the survey does not cite, with keyword category (one withdrawn by its authors).
  The script runs from the repository root and reproduces the file.

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

H. Mohasel Arjomandi and A. GhaffarTehrani, *Data and Scripts for "Agentic AI Protocols"*, version 1.5, Zenodo, 2026.
DOI (all versions, resolves to the latest): [10.5281/zenodo.24000345](https://doi.org/10.5281/zenodo.24000345)
