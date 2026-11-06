#!/usr/bin/env python3
"""Changelog coding for Section IX (design pressures, M1 of the Nov. 2026 review).
Every item enumerated in the official MCP changelogs (2025-03-26, 2025-06-18, 2025-11-25, 2026-07-28) and every
change enumerated in A2A's "What's New in v1.0" page (0.3 -> 1.0) is assigned
  - a primary design pressure (DP1..DP6, or OTHER), an optional secondary one, and
  - the concern plane it changes (P1..P6).
Sources fetched 2026-11-05. Coding rules are in CODEBOOK.md. Writes dp_coding.tsv and prints the summary tables used in
the paper (coverage per DP, churn per plane per revision)."""
import csv, collections, os
H = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'coding')
R = []
def add(proto, rev, items):
    for i, (txt, plane, dp, dp2) in enumerate(items, 1): R.append((proto, rev, f'{rev}#{i}', txt, plane, dp, dp2))
add('MCP', '2025-03-26', [
 ('OAuth 2.1-based authorization framework', 'P5', 'DP2', ''),
 ('Streamable HTTP replaces HTTP+SSE transport', 'P1', 'DP1', ''),
 ('JSON-RPC batching added', 'P1', 'OTHER', ''),
 ('Tool annotations (read-only, destructive, ...)', 'P3', 'OTHER', 'DP4'),
 ('message field on ProgressNotification', 'P2', 'DP3', ''),
 ('Audio content type', 'P4', 'OTHER', ''),
 ('completions capability declared explicitly', 'P4', 'OTHER', ''),
])
add('MCP', '2025-06-18', [
 ('JSON-RPC batching removed', 'P1', 'DP5', ''),
 ('Structured tool output', 'P4', 'OTHER', 'DP5'),
 ('Servers classified as OAuth resource servers; protected-resource metadata', 'P5', 'DP2', ''),
 ('Clients must implement RFC 8707 resource indicators', 'P5', 'DP2', ''),
 ('Authorization security considerations and security best-practices page', 'P5', 'DP2', ''),
 ('Elicitation (server requests information from the user)', 'P4', 'DP4', ''),
 ('Resource links in tool results', 'P4', 'OTHER', ''),
 ('MCP-Protocol-Version header required on subsequent HTTP requests', 'P1', 'DP1', 'DP5'),
 ('Lifecycle operation SHOULD -> MUST', 'P2', 'DP5', ''),
 ('_meta field on more interface types', 'P6', 'DP5', ''),
 ('context field on CompletionRequest', 'P4', 'OTHER', ''),
 ('title field for human-friendly names', 'P3', 'OTHER', ''),
])
add('MCP', '2025-11-25', [
 ('OpenID Connect Discovery for authorization servers', 'P5', 'DP2', ''),
 ('Icons for tools, resources, templates, prompts', 'P3', 'OTHER', ''),
 ('Incremental scope consent via WWW-Authenticate', 'P5', 'DP2', ''),
 ('Guidance on tool names', 'P3', 'DP5', ''),
 ('Standards-based ElicitResult/EnumSchema', 'P4', 'DP4', 'DP5'),
 ('URL-mode elicitation', 'P4', 'DP4', ''),
 ('Tool calling in sampling (tools, toolChoice)', 'P4', 'OTHER', ''),
 ('Client ID Metadata Documents recommended for registration', 'P5', 'DP2', ''),
 ('Experimental tasks (durable requests, polling, deferred results)', 'P2', 'DP3', ''),
 ('stdio servers may log to stderr', 'P1', 'DP5', ''),
 ('Optional description on Implementation (aligns with registry server.json)', 'P3', 'OTHER', ''),
 ('HTTP 403 for invalid Origin headers', 'P1', 'OTHER', ''),
 ('Security best-practices guidance updated', 'P5', 'OTHER', ''),
 ('Input validation errors returned as tool execution errors', 'P4', 'DP5', ''),
 ('Polling SSE streams: servers may disconnect at will', 'P2', 'DP1', ''),
 ('Clarification of polling/resumption semantics for GET streams', 'P2', 'DP1', ''),
 ('Protected-resource metadata discovery aligned with RFC 9728', 'P5', 'DP2', ''),
 ('Default values in elicitation schemas', 'P4', 'DP4', ''),
 ('JSON Schema 2020-12 as default dialect', 'P3', 'DP5', ''),
 ('Request payloads decoupled into standalone parameter schemas', 'P4', 'DP5', ''),
 ('Formal governance structure', 'P6', 'DP6', ''),
 ('Community communication practices', 'P6', 'DP6', ''),
 ('Working groups and interest groups', 'P6', 'DP6', ''),
 ('SDK tiering system', 'P6', 'DP6', ''),
])
add('MCP', '2026-07-28', [
 ('Protocol-level sessions and Mcp-Session-Id removed', 'P2', 'DP1', ''),
 ('initialize handshake removed; per-request _meta', 'P2', 'DP1', ''),
 ('server/discover RPC', 'P3', 'DP1', ''),
 ('subscriptions/listen replaces GET endpoint and resources/subscribe', 'P2', 'DP1', ''),
 ('ping, logging/setLevel, roots/list_changed removed', 'P2', 'DP1', 'DP5'),
 ('Tasks moved to io.modelcontextprotocol/tasks extension; tasks/update', 'P2', 'DP3', 'DP5'),
 ('Multi Round-Trip Requests replace server-initiated requests', 'P4', 'DP4', 'DP1'),
 ('Required resultType (complete | input_required)', 'P4', 'DP4', ''),
 ('SSE resumability and redelivery (Last-Event-ID) removed', 'P2', 'DP1', ''),
 ('extensions field in client/server capabilities', 'P6', 'DP5', ''),
 ('OpenTelemetry trace-context propagation in _meta', 'P1', 'OTHER', ''),
 ('Deterministic tools/list order', 'P3', 'OTHER', ''),
 ('Mcp-Method and Mcp-Name headers on Streamable HTTP POST', 'P1', 'DP1', ''),
 ('ttlMs and cacheScope on list/read results', 'P3', 'DP1', ''),
 ('Resource-not-found error code changed', 'P4', 'DP5', ''),
 ('iss parameter (RFC 9207); clients must validate', 'P5', 'DP2', ''),
 ('application_type required in Dynamic Client Registration', 'P5', 'DP2', ''),
 ('Client credentials bound to issuing authorization server', 'P5', 'DP2', ''),
 ('inputSchema/outputSchema accept any JSON Schema 2020-12 keywords', 'P3', 'DP5', ''),
 ('elicitation/complete notification and elicitationId removed', 'P4', 'DP4', 'DP1'),
 ('Error-code allocation policy', 'P4', 'DP5', ''),
 ('Roots, Sampling, Logging deprecated', 'P6', 'DP5', ''),
 ('HTTP+SSE transport reclassified as Deprecated', 'P6', 'DP5', ''),
 ('includeContext values thisServer/allServers deprecated', 'P6', 'DP5', ''),
 ('Dynamic Client Registration deprecated in favor of CIMD', 'P5', 'DP2', ''),
 ('schema.json numeric types corrected', 'P4', 'DP5', ''),
 ('Feature lifecycle and 12-month deprecation policy', 'P6', 'DP6', ''),
 ('PR-based SEP workflow', 'P6', 'DP6', ''),
])
add('A2A', '0.2-0.3', [
 # CHANGELOG.md features and breaking changes, v0.2.1 (2025-05-27) to v0.3.0 (2025-07-30); typo, bug-fix, and docs entries excluded
 ('0.2.1: flag for authenticated extended Agent Cards', 'P3', 'OTHER', ''),
 ('0.2.1: referenceTaskIds for task follow-ups', 'P2', 'DP3', ''),
 ('0.2.2: resolve inconsistencies with JSON-RPC 2.0 (breaking)', 'P1', 'DP5', ''),
 ('0.2.2: gRPC and REST definitions', 'P1', 'OTHER', ''),
 ('0.2.2: protocol support for extensions', 'P6', 'DP5', ''),
 ('0.2.2: optional iconUrl on Agent Card', 'P3', 'OTHER', ''),
 ('0.2.4: multiple transport announcement in Agent Card', 'P3', 'OTHER', ''),
 ('0.2.5: required protocol version in Agent Card (breaking)', 'P6', 'DP5', ''),
 ('0.2.5: multiple push-notification configs per task (breaking)', 'P2', 'DP3', ''),
 ('0.3.0: mTLS security scheme, OAuth 2.0 metadata URL, per-skill security (breaking)', 'P5', 'DP2', 'OTHER'),
 ('0.3.0: well-known URI renamed agent.json -> agent-card.json (breaking)', 'P3', 'DP5', ''),
 ('0.3.0: method for fetching the extended Agent Card (breaking)', 'P3', 'OTHER', ''),
 ('0.3.0: signatures on the Agent Card', 'P3', 'OTHER', ''),
])
add('A2A', '1.0', [
 ('a2a.proto becomes the normative source', 'P1', 'DP5', ''),
 ('google.rpc.Status error model replaces RFC 9457', 'P4', 'DP5', ''),
 ('Three bindings formally specified with stricter adherence', 'P1', 'DP5', ''),
 ('Versioning strategy; A2A-Version header negotiation', 'P6', 'DP5', ''),
 ('Error taxonomy', 'P4', 'DP5', ''),
 ('kind discriminators removed', 'P4', 'DP5', ''),
 ('Enum values in SCREAMING_SNAKE_CASE', 'P4', 'DP5', ''),
 ('camelCase JSON and ISO 8601 timestamps', 'P1', 'DP5', ''),
 ('Optional vs. required field semantics', 'P4', 'DP5', ''),
 ('Operations renamed (SendMessage, GetTask, ...)', 'P4', 'DP5', ''),
 ('supportedInterfaces[] with per-interface protocol version', 'P3', 'DP5', ''),
 ('Extension versioning and requirements; A2A-Extensions header', 'P6', 'DP5', ''),
 ('Simplified identifiers', 'P4', 'DP5', ''),
 ('/v1 URL prefix removed', 'P1', 'DP5', ''),
 ('tenant field: one endpoint serves many agents', 'P2', 'DP1', ''),
 ('Agent Card signatures specified with JCS canonicalization and verification rules (signatures added in 0.3)', 'P3', 'OTHER', ''),
 ('OAuth device authorization grant added', 'P5', 'DP2', ''),
 ('OAuth implicit and password flows removed', 'P5', 'DP2', ''),
 ('pkce_required on authorization-code flow', 'P5', 'DP2', ''),
 ('Cursor-based pagination', 'P2', 'DP1', ''),
 ('ListTasks operation', 'P2', 'DP3', ''),
 ('Multiple concurrent streams/subscriptions per task', 'P2', 'DP1', 'DP3'),
 ('Unified Part type (text, raw, url, data)', 'P4', 'DP5', ''),
 ('Stream events wrapped; final flag removed; terminal state by stream closure', 'P2', 'DP5', 'DP3'),
 ('index field on TaskArtifactUpdateEvent', 'P2', 'DP3', ''),
 ('Push-notification config operations renamed, flattened, authentication enhanced', 'P2', 'DP3', ''),
 ('returnImmediately execution-mode control', 'P2', 'DP3', ''),
 ('Task visibility and authorization scoped to the caller', 'P5', 'OTHER', ''),
 ('extensions[] on Message and Artifact', 'P6', 'DP5', ''),
])
with open(os.path.join(H, 'dp_coding.tsv'), 'w', newline='') as f:
    w = csv.writer(f, delimiter='\t'); w.writerow(['protocol', 'revision', 'item', 'change', 'plane', 'primary_dp', 'secondary_dp'])
    w.writerows(R)
N = len(R); C = collections.Counter(r[5] for r in R)
print(f'items coded: {N} (MCP {sum(r[0]=="MCP" for r in R)}, A2A {sum(r[0]=="A2A" for r in R)})')
print('primary DP:', {k: C[k] for k in sorted(C)}, f'covered by DP1-6: {N - C["OTHER"]}/{N} = {100*(N-C["OTHER"])/N:.1f}%')
for p in ('MCP', 'A2A'):
    rs = [r for r in R if r[0] == p]; o = sum(r[5] == 'OTHER' for r in rs)
    print(f'  {p}: {len(rs)-o}/{len(rs)} = {100*(len(rs)-o)/len(rs):.1f}%')
print('OTHER items:'); [print('   ', r[2], r[3]) for r in R if r[5] == 'OTHER']
revs = ['2025-03-26', '2025-06-18', '2025-11-25', '2026-07-28', '0.2-0.3', '1.0']
print('plane x revision (item counts):')
print('plane ' + ' '.join(f'{v:>11}' for v in revs) + '  MCP-total  revisions-touched(MCP)  A2A-total')
for pl in ['P1', 'P2', 'P3', 'P4', 'P5', 'P6']:
    cnt = [sum(1 for r in R if r[1] == v and r[4] == pl) for v in revs]
    print(f'{pl:5} ' + ' '.join(f'{c:>11}' for c in cnt) + f'  {sum(cnt[:4]):>9}  {sum(1 for c in cnt[:4] if c):>5}  {sum(cnt[4:]):>9}')
print('DP x revision:')
for d in ['DP1', 'DP2', 'DP3', 'DP4', 'DP5', 'DP6', 'OTHER']:
    print(f'{d:6}' + ' '.join(f'{sum(1 for r in R if r[1]==v and r[5]==d):>11}' for v in revs))
