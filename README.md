# Supplementary materials for "When Agents Delegate"

These are the supplementary materials for the article "When Agents Delegate: Accountability Chains in Multi-Agent AI Systems" by Ornella Bahidika (Independent Researcher, Seattle, WA, USA), published in the International Journal of Advanced Computer Science and Applications (IJACSA).

Section VI of the article audits five widely used agent protocols and frameworks (the Model Context Protocol, the Agent2Agent protocol, LangGraph, AutoGen, and the OpenAI Agents SDK) against five accountability conditions. That gives 25 verdicts in total. The files here show the evidence behind every one of those verdicts.

## The files

**S1-audit-working-notes.md** holds the working notes of the audit. For each verdict it gives the exact wording quoted from the official specification or documentation, the address of the source page, and the reasoning that led to the verdict. The version of each specification and the date of the audit are recorded as well.

**S2-audit-evidence.json** holds the same 25 assessments as structured data. Each record names the artifact, the condition, the verdict, the supporting quotations, the source addresses, and the rationale. Use this file if you want to load the results into your own code.


**reliability/** holds the blind second-coding study reported in the article's Limitations section: `blind_recode_verdicts.json` (the second coder's verdicts for all twenty-five cells, coded blind from the primary sources in randomized order), `blind_recode_notes.md` (method notes), `compute_agreement.py` (the agreement script), and `agreement-results.json` (raw agreement 19/25, Cohen's kappa 0.42, and the six disagreeing cells).

## How to cite

Bahidika, O., "When Agents Delegate: Accountability Chains in Multi-Agent AI Systems," International Journal of Advanced Computer Science and Applications (IJACSA), 2026.

## License

CC BY 4.0. You may share and adapt these materials with attribution.
