# References and verification scope

**STATUS: RIEMANN HYPOTHESIS OPEN**

This publication credits **@ykbballer91** for the project record. The authors of cited mathematical works retain their scholarly attribution. A citation is evidence for a particular statement under particular assumptions; it is not an endorsement of every claim in a paper.

The [machine-readable reference uses](../data/references.json) preserve 108 statement-level records from six historical ledgers and add three uses from the dated cyclicity notes. The same work can appear more than once when a theorem, a conditional criterion and a heuristic discussion have different dependencies. Later prose citations also have an external-link discovery index with source locations. That index is not a list of verified theorems, and this is not an exhaustive bibliography.

## How to read a verification status

- **Publication status** concerns the journal, preprint or reference source. It does not state that this project has verified the proof.
- **Primary text checked** means the indicated statement or passage was read. It does not mean every lemma in the paper was reconstructed.
- **Scoped independent check** describes a separate internal AI-agent derivation, audit or computation of a specified claim. It is not external peer review and does not certify unrelated claims.
- **Conditional / RH-dependent** is attached to the statement used, not flattened into a judgment about a whole paper. A valid conditional theorem remains conditional when applied here.
- **NO**, **PARTIAL**, booleans and longer scope notes are retained in their original types and wording under `verification_as_recorded`. Missing fields remain missing or null. Text is never converted to a Boolean on the basis of whether it is nonempty.

The inherited bibliography includes bounded audits of proof claims and exploratory analogies. Such entries are historical context, not accepted RH inputs. The track reports state what survived each audit. No source was newly promoted to “independently verified” during publication editing.

## Selected mathematical entry points

| Topic | Primary or official source | Exact use and boundary |
|---|---|---|
| Weil criterion and explicit formula | [Weil, 1952](https://cds.cern.ch/record/471308); [Connes, trace formula](https://arxiv.org/pdf/math/9811068v1) | Positivity criterion and arithmetic trace framework; the global positivity hypothesis must still be supplied. |
| Arithmetic quotient and Frobenius comparison | [Connes–Consani–Marcolli, math/0703392v1](https://arxiv.org/pdf/math/0703392v1); [Deligne, Weil I](https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf) | Exact domains, traces and multiplicities; finite-field purity is not automatically a number-field theorem. |
| Polarization and heights | [Gillet–Soulé](https://www.numdam.org/item/10.1007/BF02699132.pdf); [Milne, Abelian Varieties](https://www.jmilne.org/math/CourseNotes/AV.pdf) | The positive structures are used only on their stated geometric spaces. No identity with the full zeta-zero space is inferred. |
| Heat deformation | [Rodgers–Tao, 1801.05914v5](https://arxiv.org/pdf/1801.05914v5) | Nonnegativity of the de Bruijn–Newman constant; this does not prove the missing upper bound at time zero. |
| Localized Weil form and arithmetic radical | [Connes–Consani, Spectral triples and ζ-cycles](https://ems.press/journals/lem/articles/11033001) | The known arithmetic radical is explicitly attributed; it does not by itself select a unique finite ground state. |
| Real-zero theorem and prolate proxy | [Connes–van Suijlekom, 2511.23257v1](https://arxiv.org/html/2511.23257v1); [Connes–Consani–Moscovici, 2511.22755v1](https://arxiv.org/html/2511.22755v1) | Conditional ground-state hypotheses, known proxy convergence, and the missing normalized comparison are separate in the local-to-global theorem stack. |
| Sonin spaces | [Burnol, math/0203120v6](https://arxiv.org/pdf/math/0203120v6) | Completion and minimality results in their stated spaces; the hierarchy audit does not substitute this chain for the actual projected Weil energy. |
| Moment density | [de Jeu, math/0111019v2](https://arxiv.org/pdf/math/0111019v2), Theorem 2.3, p.5 | Carleman implies polynomial L² density for the finite positive measure used in cyclicity. Theorem 5.1's Stieltjes statement is kept distinct. |
| Exponential decay of Xi | [DLMF 5.11.9](https://dlmf.nist.gov/5.11#E9), [25.9.3](https://dlmf.nist.gov/25.9#E3), [25.4.4](https://dlmf.nist.gov/25.4#E4) | Standard Gamma decay, an unconditional zeta estimate and completion conventions. No RH input. |
| Supplementary moments | [Simonič–Starichkova, 2105.06821v3](https://arxiv.org/html/2105.06821v3) | A mean-square error estimate used for a moment asymptotic; the cyclicity theorem does not depend on that refinement. |

## Where the exact statement-level records live

- [Initial theorem and computation ledger](../archive/literature/literature/sources.json).
- [Weil frontier source notes](../archive/literature/literature/notes/weil-sources.json).
- [Structural heuristic source uses](../archive/literature/research/structural_sources.json).
- [Generator and boundary sources](../archive/literature/research/phase2_sources.json).
- [Frobenius comparison sources](../archive/literature/research/phase3_sources.json).
- [Polarization and intersection sources](../archive/literature/research/phase4/sources.json).

For later tracks, the canonical report and its supporting note provide theorem numbers, hypotheses, versions and failed applicability checks. Particularly relevant are [the local-to-global stack](../archive/reports/research/local_global_theorem_stack.md), [the Sonin audit](../archive/reports/research/sonine_filtration_audit.md) and [the cyclicity source note](../archive/reports/research/full_ground_capture/notes/moment_problem_sources.md).

## Rights and retrieval

Only project commentary and bibliographic metadata are reproduced here. Third-party full texts, cached PDFs/HTML/TeX and ancillary software are excluded. External links point to the relevant publisher, repository or official reference; their content and rights are outside this publication. Source retrieval dates and versions are preserved where the research recorded them. No unrecorded access date, peer-review outcome or new author identity is supplied.
