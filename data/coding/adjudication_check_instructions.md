# Adjudication Check: Instructions

**Time:** about 30–45 minutes. **Return:** the filled spreadsheet `adjudication_check.xlsx`.

## Why we are asking

In the two coding rounds you coded 107 changelog changes. On 31 codes (13 primary pressures and 18 planes,
spread over 25 changes) your code and the first coder's code differed. The first author then resolved each
disagreement against the codebook. The first coder's codes were prepared with the help of an AI assistant, so a
reviewer may ask whether the resolution leaned toward those codes.

To answer that, we ask you to resolve the same 31 disagreements **yourself, without seeing our resolution**. The
paper will report how often your choice and ours agree. Disagreement is a useful result too, so please judge each
case on its merits.

## What you see

Each row of the **Check** tab is one disagreeing code for one change:

- **Decide:** whether the row is about the *primary pressure* (DP1–DP6 or OTHER) or the *plane* (P1–P6).
- **Already settled:** the other dimension of the same change. If both coders agreed on it, it is shown for context.
  If it is also in dispute, the row number where you decide it is shown instead.
- **Option A** and **Option B:** the two codes that were given. One is yours from the coding rounds and the other is
  the first coder's. **The order is random, and we do not say which is which.** Please do not try to recall which
  one was yours. Judge only the changelog entry against the codebook.

## Steps for each row

1. Open the **Source link** and find the entry (the *Change* column gives a short label; the item number is its
   position in the source's list, as in the coding rounds).
2. Read the codebook rows for both options (the **Codebook** tab: "Assign when the change …").
3. In **Your choice**, pick **A** or **B**: the code the codebook supports more closely, even if the case is close.
   Pick **Neither** only if a third code is clearly right, and write that code in the next column.
4. In **Reason**, write one short line, quoting the entry where it decides the case
   (e.g. *"entry says Streamable HTTP 'replaces' the HTTP+SSE transport → P1"*; this change is not in the check).
5. Set **Confidence** (high / medium / low).

## Rules

- Work alone and **without AI tools**, as in the coding rounds.
- Do **not** look at the paper's Section II-C or Appendix A, the released data repository (it contains the
  adjudication files), your earlier spreadsheets, or earlier emails about the coding while you do this task.
- If you have already seen the adjudication files or Appendix A before starting, that is fine. Just say so in the
  question at the top of the Check tab, so that we can report it honestly.

## Codebook summary

The full codebook is in the **Codebook** tab, the same one you used before. In short: a primary pressure explains
*why* the change was made (DP1 scale-out over session affinity; DP2 alignment with OAuth; DP3 durable,
asynchronous work; DP4 humans in the loop; DP5 smaller core, extensions, rigor; DP6 stewardship and process;
OTHER if none of the six). The plane is *what part of the protocol* the change touches (P1 transport and encoding;
P2 state and session; P3 description and discovery; P4 interaction semantics; P5 identity and authorization;
P6 governance and evolution).

Thank you!
