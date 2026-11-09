<!-- Released copy of the instructions given to the second coder (the survey's second author), with the first
author's name replaced by "the first author". The coder also received the workbook (blank form:
second_coder_sample.tsv; Codebook tab = CODEBOOK.md) and coded from the official changelog pages. -->

# Second Coding Task: Instructions

**Design pressures in the MCP and A2A changelogs** · 30 items · about 60–90 minutes

You need two files, both in this folder:

- `INSTRUCTIONS.pdf` (this document; the same text is in `INSTRUCTIONS.md`)
- `second_coding_task.xlsx` (the workbook you fill in and send back)

Please read Sections 1–6 before you start (about 15 minutes). Sections 7–9 are for reference while you work.

---

## 1. What this is about

A survey paper on *agentic AI protocols* studies how two protocols changed over time:

- **MCP (Model Context Protocol)** connects LLM applications to tools and data sources.
- **A2A (Agent2Agent)** lets AI agents delegate work to, and communicate with, other agents.

Both projects publish an official changelog for each version. The survey argues that a small set of recurring
**design pressures** explain *why* most of these changes were made. To test that argument, every changelog entry was
assigned a code.

One person's codes can reflect that person's habits. A standard check is to have a second person code a random
sample **independently**, using the same codebook, and then measure how often the two agree (Cohen's kappa). That
second person is you. The paper reports the agreement, whatever it turns out to be. There are no "right answers" you
are expected to reproduce: your honest reading of the codebook is exactly what is needed.

## 2. What you do, in one paragraph

The workbook lists 30 changes. For each one, open the official changelog, read the entry, and choose:

1. **Primary pressure:** the one design pressure (DP1–DP6, or OTHER) that best explains **why** the change was made.
2. **Plane:** the one part of the protocol (P1–P6) that the change **modifies**.
3. **Confidence:** high, medium, or low.
4. **Notes** (optional, but please use them when your confidence is not high).

Then save the workbook and send it back.

## 3. Rules that keep the coding independent

These rules matter more than anything else in this document. If you break one by accident, say so in the Notes of
the first row. That is fine; it just has to be reported.

1. **Work alone.** Don't discuss specific items with the author or anyone else until you have sent the workbook back.
2. **Don't read the survey or its data repository** (on GitHub or Zenodo) before you finish. Both contain the
   original codes.
3. **Don't use AI tools** (ChatGPT, Claude, Gemini, Copilot, etc.) for any part of this task, including to explain an
   entry. The original coding was AI-assisted, so what we need now is an independent *human* judgment. Ordinary web
   searches for unfamiliar terms are fine, and Section 9 has a short glossary.
4. **Code each entry by what it says or implies at the time.** Don't use what you know about later versions of the
   protocols.
5. **Don't edit the gray cells, and don't delete, add, or reorder rows.** The workbook is scored automatically.
6. **If a rule in the codebook seems unclear, don't ask.** Write down how you read it in Notes and carry on. Asking
   about wording could reveal how the original coder read it.

## 4. The workbook

Open `second_coding_task.xlsx` in Excel, LibreOffice Calc, or Google Sheets. If you use Google Sheets, return it with
*File → Download → Microsoft Excel (.xlsx)*.

| Tab | What it holds |
|---|---|
| **Read me** | A one-page summary of this document |
| **Codebook** | The code definitions (the same as Section 5) |
| **Coding** | The 30 items. You fill in the **yellow** cells: *Primary pressure*, *Plane*, *Confidence* (dropdowns) and *Notes* (free text). The gray row at the top, marked **EX**, is a worked example and is not scored. "Coded so far" counts your progress. |

The columns *Item ID*, *Protocol*, *Revision / source* and *Change (short label)* tell you which entry to find. The
**Source link** ("open") goes to the official page that contains it. The short label is only a pointer; the entry on
the page is what you code.

## 5. The codes

### 5.1 Design pressures (choose exactly one per item)

The codebook's rule: *Pick the pressure that best explains **why** the change was made, as stated or implied by the
item itself; do not infer from later revisions.*

| Code | Pressure | Assign when the change … |
|---|---|---|
| **DP1** | Scale-out over session affinity | removes or avoids connection/session state, makes requests self-describing or routable without the body, supports caching, polling, multi-tenancy, or horizontal scaling |
| **DP2** | Alignment with the OAuth ecosystem | adopts, profiles, tightens, or removes an OAuth/OIDC mechanism (RFCs and IETF drafts) |
| **DP3** | Durable, asynchronous work | adds or changes support for long-running work: tasks, progress, push notifications, deferred results |
| **DP4** | Humans in the loop without held-open connections | adds or reshapes mechanisms for asking the user for input or approval (elicitation, input-required states, MRTR) |
| **DP5** | Smaller core, extensions, and rigor | moves features to extensions, deprecates/removes features, adds extension points, or tightens schemas, naming, errors, normative definitions |
| **DP6** | Neutral stewardship and formal process | changes governance, decision process, working groups, SDK policy, or lifecycle policy |
| **OTHER** | None of the above | e.g. richer primitives or content types for the model/UI, security hardening outside OAuth, observability |

### 5.2 Concern planes (choose exactly one per item)

The plane is **what** the change modifies, chosen separately from the pressure.

| Code | Plane | Covers |
|---|---|---|
| **P1** | Transport and encoding | the wire format and carriage, for example JSON-RPC 2.0, HTTP, Server-Sent Events, gRPC, or standard input/output |
| **P2** | State and session | whether interactions are stateful, how long-running work is tracked, and how streaming, resumption, and cancellation work |
| **P3** | Capability description and discovery | how a party advertises what it offers (tool schemas, Agent Cards, product catalogs) and how others find it, for example through well-known URIs or registries |
| **P4** | Interaction semantics | the primitives and their lifecycle, for example tools, resources, and prompts in MCP; tasks, messages, and artifacts in A2A |
| **P5** | Identity, authorization, and trust | who the parties are and what they may do, for example OAuth profiles, signed metadata, decentralized identifiers, and verifiable credentials |
| **P6** | Governance and evolution | versioning, extension mechanisms, deprecation policy, and stewardship |

## 6. How to code one item

**Step A: Find the entry.** Click "open" and use Ctrl+F (Cmd+F on a Mac) with a distinctive word from the label.

| Revision / source | Page | Where the entries are |
|---|---|---|
| MCP revision 2025-03-26, 2025-06-18, 2025-11-25, 2026-07-28 | MCP specification changelog for that revision | Bulleted lists under headings such as *Major changes*, *Minor changes*, *Other schema changes* and *Governance and process updates*. Ignore the *Full changelog* link at the bottom. |
| A2A changelog 0.2.1–0.3.0 | `CHANGELOG.md` in the A2A GitHub repository | The newest versions are at the top. **Scroll down to the headings for versions 0.2.1 to 0.3.0.** The label starts with the version, e.g. "0.2.4: …". Entries are under *Features* or *⚠ BREAKING CHANGES*. |
| A2A What's New in v1.0 | A2A "What's New in v1.0" page | Changes from version 0.3 to 1.0, grouped by theme, with later sections that detail the breaking changes. The same change can appear in a summary list and again in a detailed section; read both. |

The number after `#` in the Item ID is an internal running number. Use the label to find the entry, not the number.

**Step B: Read the entry.** Read the entry itself and any text directly attached to it on the same page. If the entry
is too terse to tell what actually changed, you may open the pull request or proposal (PR / SEP) that it links to. If
you do, write "read PR" in Notes. Don't go looking for the reasons in other places (blogs, news, later versions).

**Step C: Choose the primary pressure.** Ask: *why was this change made?*

1. Read the "Assign when the change …" column for DP1 to DP6.
2. If exactly one fits, choose it.
3. If more than one fits, choose the one that best explains **why** the change was made, judging by the entry's own
   wording. Note the runner-up in Notes (e.g. "runner-up DP3").
4. If none of DP1–DP6 fits, choose **OTHER**. OTHER is a real category ("none of the six"). Don't use it as a
   "not sure" option; use the Confidence column for that.

**Step D: Choose the plane.** Ask: *which part of the protocol does this change touch?* If it touches several, choose
the one it changes most directly. Choose the plane on its own merits. A given pressure does not imply a particular
plane, or the other way round.

**Step E: Set the confidence.**

- **high:** one code clearly fits.
- **medium:** two codes are plausible and you picked the better one (give the runner-up in Notes).
- **low:** the entry is unclear to you, or no code fits well (say why in Notes).

**Step F: Notes (optional).** Useful notes are short, e.g. "runner-up DP5", "plane could also be P3", "entry not
found, coded from label", "read PR". Please put each note in its own row's Notes cell.

## 7. Worked examples

These six entries are **not** in your sample. They show the format and how the codebook is applied. The first one is
also the gray **EX** row in the workbook.

| Entry | Pressure | Plane | Why |
|---|---|---|---|
| MCP 2025-03-26: *OAuth 2.1-based authorization framework* | DP2 | P5 | Adopts an OAuth mechanism. It changes who may do what, so the plane is identity and authorization. |
| MCP 2025-03-26: *Replaced the previous HTTP+SSE transport with a more flexible Streamable HTTP transport* | DP1 | P1 | The old transport kept a long-lived connection per client; the replacement avoids that connection state (DP1: "removes or avoids connection/session state"). What it modifies is the transport. |
| MCP 2025-11-25: *Experimental tasks (durable requests with polling and deferred result retrieval)* | DP3 | P2 | Adds support for long-running work with deferred results. It changes how long-running work is tracked. |
| A2A 0.3 → 1.0: *Enum values changed from kebab-case to SCREAMING_SNAKE_CASE for compliance with the Protocol Buffers style* | DP5 | P4 | Tightens naming for consistency with a standard. What it changes is how the values of the primitives (e.g. task states) are written. |
| MCP 2025-11-25: *Establish SDK tiering system with clear requirements for feature support* | DP6 | P6 | Changes SDK policy, which is part of how the protocol is stewarded. |
| MCP 2025-03-26: *Audio content type* | OTHER | P4 | A richer content type for the model. None of DP1–DP6 applies. The plane is the primitives' content. |

## 8. Common questions

**I can't find the entry.** Try another distinctive word from the label. On A2A's `CHANGELOG.md`, make sure you are
under the 0.2.1–0.3.0 headings. If you still can't find it, code from the label, set Confidence to *low*, and write
"entry not found".

**The entry covers several changes.** Code the part that the short label describes.

**The label and the entry seem to say different things.** Follow the entry, and say so in Notes.

**I recognize a change and know why it was really made (for example from a later version or a talk).** Code only from
the entry (Rule 4). If your background knowledge pulls you strongly toward another code, mention it in Notes.

**Can I go back and change an answer?** Yes, any time before you send the workbook.

**How long should one item take?** Two to three minutes. Don't spend more than five on a single item; choose, set the
confidence, and add a note.

**I have a question about the codebook.** See Rule 6: write your interpretation in Notes rather than asking.

## 9. Glossary

These are neutral descriptions of terms that appear in the entries.

| Term | Meaning |
|---|---|
| JSON-RPC 2.0 | A simple format for remote procedure calls encoded in JSON. MCP and A2A messages use it. |
| HTTP, SSE | The web's request/response protocol; Server-Sent Events let a server stream messages to a client over HTTP. |
| gRPC, Protocol Buffers (`.proto`) | Google's RPC framework and the schema language it uses to define messages. |
| stdio | Standard input/output: a client runs a server as a local process and talks to it through pipes. |
| Session | State kept by a server across several requests from the same client. |
| OAuth 2.0 / 2.1 | The standard framework for granting an application limited access on a user's behalf. *Flows* (or *grants*) are its variants, e.g. authorization code, device code, implicit, password. |
| PKCE | An OAuth extension that protects the authorization-code flow against interception. |
| OIDC (OpenID Connect) | An identity layer on top of OAuth 2.0. |
| RFC, IETF | Request for Comments: a numbered standards document of the Internet Engineering Task Force. |
| SEP | Specification Enhancement Proposal: MCP's process for proposing changes to the specification. |
| Capability | A feature a client or server declares that it supports, so the other side knows it can be used. |
| Elicitation | An MCP mechanism by which a server asks the user, through the client, for information. |
| MRTR | Multi Round-Trip Requests (MCP). |
| Extension | An optional add-on to a protocol, defined outside the core specification. |
| Agent Card | A2A's JSON document in which an agent describes itself: identity, skills, endpoints, authentication. |
| Well-known URI | A fixed path on a web server (under `/.well-known/`) where a document such as an Agent Card is published. |
| Tenant | One customer or agent among several served by the same endpoint. |
| `_meta` | An MCP field for attaching metadata to messages. |
| Breaking change | A change that makes older implementations incompatible. |

## 10. When you're done

1. Check that "Coded so far" shows **30 of 30**.
2. Save the workbook as `second_coding_task_<your name>.xlsx` and send it back to the first author.
3. In the same message, say:
   - roughly how long it took;
   - whether you followed all the rules in Section 3 (or which one you didn't, and how);
   - whether you would like to be **named in the acknowledgments** of the paper or remain anonymous.

**How your answers are used:** The first author computes the agreement between your codes and the original ones. After that,
the first author may ask you to discuss the items you disagreed on; that discussion never changes the agreement score. The paper
reports the agreement statistics. Your codes (without your name unless you agree) will be released in the survey's
public data repository under the CC BY 4.0 license.

Thank you!
