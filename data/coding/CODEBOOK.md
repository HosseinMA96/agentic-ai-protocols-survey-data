# Codebook: design pressures in MCP and A2A changelogs

Unit of analysis: one item as enumerated by the official changelog (MCP 2025-03-26, 2025-06-18, 2025-11-25,
2026-07-28 changelog pages) or one change enumerated in A2A "What's New in v1.0" (0.3 -> 1.0), or one feature or breaking-change entry
in A2A's CHANGELOG.md for v0.2.1-v0.3.0 (typo, bug-fix, and documentation entries excluded). Revision 2024-11-05 is
the initial release and has no changelog. Sources fetched 2026-11-05.

Each item gets exactly one primary code and at most one secondary code. Pick the pressure that best explains *why*
the change was made, as stated or implied by the item itself; do not infer from later revisions.

| Code | Pressure | Assign when the change ... |
|---|---|---|
| DP1 | Scale-out over session affinity | removes or avoids connection/session state, makes requests self-describing or routable without the body, supports caching, polling, multi-tenancy, or horizontal scaling |
| DP2 | Alignment with the OAuth ecosystem | adopts, profiles, tightens, or removes an OAuth/OIDC mechanism (RFCs and IETF drafts) |
| DP3 | Durable, asynchronous work | adds or changes support for long-running work: tasks, progress, push notifications, deferred results |
| DP4 | Humans in the loop without held-open connections | adds or reshapes mechanisms for asking the user for input or approval (elicitation, input-required states, MRTR) |
| DP5 | Smaller core, extensions, and rigor | moves features to extensions, deprecates/removes features, adds extension points, or tightens schemas, naming, errors, normative definitions |
| DP6 | Neutral stewardship and formal process | changes governance, decision process, working groups, SDK policy, or lifecycle policy |
| OTHER | none of the above | e.g. richer primitives or content types for the model/UI, security hardening outside OAuth, observability |

Plane (P1..P6) follows Section IV of the paper: P1 transport/encoding, P2 state/session, P3 description/discovery,
P4 interaction semantics, P5 identity/authorization, P6 governance/evolution.

Primary coder: first coding by the AI assistant from the changelog text, reviewed by the author.
Second coder: see `second_coder_sample.tsv` (blinded; codes removed) and `kappa.py`.
