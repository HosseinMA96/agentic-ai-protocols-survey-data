# Update search, 2026-11-17

The main harvest (`../../harvest.json`, arXiv window 2024-11-01..2026-10-31) is frozen. This folder holds the update search
reported in §II-F of the paper (label `sec:method-update`).

- `../../../scripts/update_search.py ../../harvest/harvest.json ../../bib/references.bib . 20261117` reproduces
  `update_search_arxiv.tsv` (records returned by the six queries Q1-Q6 or the title retrieval T over 2024-11-01..2026-11-17
  that are not in the frozen harvest), `update_search_not_returned.tsv` (frozen records the re-run no longer returns), and
  `update_search_openalex.tsv` (OpenAlex, publication dates 2026-11-01..2026-11-17). arXiv/OpenAlex results change over time.
- `update_decisions.tsv`: screening decision for each title-rule record (arXiv), each peer-reviewed-type OpenAlex record in a
  named venue, and the two pool taxonomies added to Table I after a final survey search.
- Counts in the paper: 48 abstract-query records (11 late-indexed in the original window, 37 later) + 4 title-only (later)
  = 52; 24 pass the title rule; 14 added. OpenAlex: 209 unique, 179 non-arXiv-only, 74 title-rule, 16 peer-reviewed type in a
  named venue, 5 protocol research, 2 added + 1 peer-reviewed version.
- Specification check (same day): no new MCP revision (2026-07-28 current; next planned 2027-03-30, blog of 2026-11-11), A2A tag
  v1.1.0-rc (2026-10-29, no release), AP2 v0.2.0 / UCP 2026-08-25 / ACP-Commerce unchanged, CIMD draft -03 (2026-11-02).
