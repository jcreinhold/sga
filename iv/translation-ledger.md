# Translation Ledger — SGA 4-I

This ledger records recurring translation choices for SGA 4-I. It is deliberately conservative: established English
mathematical terminology is used where it exists, while historically loaded terms are not silently modernized.

## Formatting

| Source feature                   | English convention                                        | Note                                                             |
| -------------------------------- | --------------------------------------------------------- | ---------------------------------------------------------------- |
| mathematical notation            | TeX inside `$...$` or `$$...$$`                           | Use KaTeX-friendly TeX, not Unicode mathematical glyphs.         |
| arrows                           | `\to`, `\leftarrow`, `\Rightarrow`, `\Longleftrightarrow` | Avoid Unicode arrows in mathematics.                             |
| products and sums                | `\prod`, `\coprod`, `\times`, `\times_X`                  | Use TeX operators rather than Unicode symbols.                   |
| limits                           | `\varprojlim`, `\varinjlim`, `\operatorname{colim}`       | Preserve period terms "projective" and "inductive" in prose.     |
| categories of presheaves/sheaves | `\widehat{C}`, `\widetilde{C}`                            | Use TeX instead of `C^` or `C~` when the symbol is mathematical. |
| universe notation                | `$U$`, `$V$`, `$U$-site`, `$U$-small`                     | Keep source universe notation.                                   |
| damaged diagrams                 | fenced `text` block with a translator warning             | Do not silently reconstruct an uncertain OCR diagram.            |

## Core Terminology

| French                                                            | English                                                    | Note                                                                                                         |
| ----------------------------------------------------------------- | ---------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------ |
| topos                                                             | topos; plural topoi                                        | Use `topoi` in prose. Keep `topos` in compounds such as "ringed topos".                                      |
| theorie des topos                                                 | theory of topoi                                            | Title-level phrase.                                                                                          |
| site                                                              | site                                                       | Standard SGA terminology.                                                                                    |
| prefaisceau                                                       | presheaf                                                   | Standard.                                                                                                    |
| faisceau                                                          | sheaf                                                      | Standard.                                                                                                    |
| categorie                                                         | category                                                   | Standard.                                                                                                    |
| foncteur                                                          | functor                                                    | Standard.                                                                                                    |
| foncteur fibre                                                    | fiber functor                                              | Standard; American spelling.                                                                                 |
| foncteur section                                                  | section functor                                            | Standard for the SGA IV usage.                                                                               |
| categorie des points d'un topos                                   | category of points of a topos                              | Preserve the topos-theoretic sense.                                                                          |
| point geometrique                                                 | geometric point                                            | Standard.                                                                                                    |
| morphisme de topos                                                | morphism of topoi                                          | Use plural "topoi" in the English compound.                                                                  |
| morphisme de sites                                                | morphism of sites                                          | Standard.                                                                                                    |
| topos annele                                                      | ringed topos                                               | Standard.                                                                                                    |
| topos localement annele                                           | locally ringed topos                                       | Standard.                                                                                                    |
| espace annele                                                     | ringed space                                               | Standard.                                                                                                    |
| espace topologique                                                | topological space                                          | Standard.                                                                                                    |
| espace a operateurs                                               | space with operators                                       | Historical/topological term; do not replace by "group action" unless the source does.                        |
| gros site / gros topos                                            | big site / big topos                                       | Standard English rendering.                                                                                  |
| petit                                                             | small                                                      | Size-theoretic term.                                                                                         |
| `$U$`-petit                                                       | `$U$`-small                                                | Preserve universe notation.                                                                                  |
| univers                                                           | universe                                                   | Size-theoretic term.                                                                                         |
| cardinaux inaccessibles                                           | inaccessible cardinals                                     | Standard.                                                                                                    |
| application                                                       | map                                                        | Use "function" only in elementary set-theoretic prose.                                                       |
| morphisme                                                         | morphism                                                   | Standard.                                                                                                    |
| monomorphisme                                                     | monomorphism                                               | Standard.                                                                                                    |
| epimorphisme                                                      | epimorphism                                                | Standard.                                                                                                    |
| epimorphisme effectif                                             | effective epimorphism                                      | Standard.                                                                                                    |
| epimorphisme strict                                               | strict epimorphism                                         | Historical categorical terminology; keep literal technical rendering.                                        |
| epimorphique universelle                                          | universally epimorphic                                     | For families; "universal epimorphism" for a morphism when grammar calls for it.                              |
| bicouvrant                                                        | bicovering                                                 | Technical SGA IV term.                                                                                       |
| couvrant                                                          | covering                                                   | For sieves, morphisms, and families.                                                                         |
| crible                                                            | sieve                                                      | Standard categorical topology term.                                                                          |
| topologie                                                         | topology                                                   | Grothendieck topology unless the context is ordinary topology.                                               |
| pretopologie                                                      | pretopology                                                | Standard.                                                                                                    |
| topologie canonique                                               | canonical topology                                         | Standard.                                                                                                    |
| topologie grossiere                                               | coarse topology                                            | Historical source pairs it with chaotic topology.                                                            |
| topologie chaotique                                               | chaotic topology                                           | Preserve the source's term.                                                                                  |
| recouvrement                                                      | covering                                                   | Prefer "covering" to "cover" in formal terminology.                                                          |
| raffinement                                                       | refinement                                                 | Standard.                                                                                                    |
| categorie filtrante                                               | filtered category                                          | Standard.                                                                                                    |
| categorie pseudo-filtrante                                        | pseudo-filtered category                                   | Preserve the source's term.                                                                                  |
| limite projective                                                 | projective limit                                           | Preserve period terminology in SGA IV; modern English often says "inverse limit".                            |
| limite inductive                                                  | inductive limit                                            | Preserve period terminology in SGA IV; modern English often says "direct limit".                             |
| image directe                                                     | direct image                                               | Standard for sheaves/topoi.                                                                                  |
| image inverse / image reciproque                                  | inverse image                                              | Standard.                                                                                                    |
| prolongement par zero                                             | extension by zero                                          | Standard.                                                                                                    |
| prolongement par le vide                                          | extension by the empty object                              | Preserve the distinction from extension by zero.                                                             |
| recollement                                                       | gluing                                                     | Use "gluing"; "recollement" only if the term is used technically as such.                                    |
| localisation                                                      | localization                                               | Standard.                                                                                                    |
| sous-topos                                                        | subtopos                                                   | Standard.                                                                                                    |
| sous-topos ouvert / ferme / localement ferme                      | open / closed / locally closed subtopos                    | Standard.                                                                                                    |
| plongement ouvert / ferme                                         | open / closed embedding                                    | Standard for topoi in this context.                                                                          |
| adherence / interieur / exterieur / frontiere d'un sous-topos     | closure / interior / exterior / boundary of a subtopos     | Standard topological analogy.                                                                                |
| support / cosupport                                               | support / cosupport                                        | Standard.                                                                                                    |
| etendue                                                           | spread                                                     | Historical SGA IV term for topological spreads; use a note at first substantive occurrence.                  |
| sobre                                                             | sober                                                      | Topological term.                                                                                            |
| voisinage                                                         | neighborhood                                               | American spelling.                                                                                           |
| generalisation / specialisation d'un point                        | generalization / specialization of a point                 | Standard.                                                                                                    |
| stable par descente                                               | stable under descent                                       | Standard.                                                                                                    |
| quarrable                                                         | quarrable                                                  | Preserve SGA's historical term for "has representable base changes"; define at first substantive occurrence. |
| foncteur fibrant                                                  | fibering functor                                           | SGA period terminology for a functor organized by cartesian pullbacks.                                       |
| categorie fibre                                                   | fiber category                                             | American spelling; preserve categorical sense.                                                               |
| filtration cardinale                                              | cardinal filtration                                        | Technical term of Expose I, § 9.                                                                             |
| accessible / preaccessible                                        | accessible / preaccessible                                 | Preserve the exact size-theoretic distinction.                                                               |
| grand devant un cardinal                                          | large relative to a cardinal                               | Literal size-theoretic term in the accessibility arguments.                                                  |
| foncteur ind-adjoint / pro-adjoint                                | ind-adjoint / pro-adjoint functor                          | Do not replace by modern adjoint functor terminology.                                                        |
| facteur direct                                                    | direct factor                                              | For an image of an idempotent/projector.                                                                     |
| projecteur                                                        | projector                                                  | Historical categorical/set-theoretic term for idempotent.                                                    |
| espece de structure                                               | species of structure                                       | Bourbaki terminology; do not paraphrase as "kind of structure".                                              |
| artinien                                                          | artinian                                                   | Lowercase in prose except at sentence start.                                                                 |
| collectivisante                                                   | collectivizing                                             | Bourbaki set-theoretic terminology.                                                                          |
| torseur                                                           | torsor                                                     | Standard.                                                                                                    |
| cohomologie a supports propres                                    | cohomology with proper supports                            | Standard for `$f_!$` context.                                                                                |
| descente cohomologique                                            | cohomological descent                                      | Standard.                                                                                                    |
| lissification                                                     | smoothification                                            | Historical term; avoid paraphrase unless context demands.                                                    |
| coefficients de torsion premiers aux caracteristiques residuelles | torsion coefficients prime to the residual characteristics | Preserve exact hypothesis.                                                                                   |
| corps premier                                                     | prime field                                                | Standard.                                                                                                    |
| corps fini                                                        | finite field                                               | Standard.                                                                                                    |

## Proof and Expository Movement

| French             | English               | Note                                                          |
| ------------------ | --------------------- | ------------------------------------------------------------- |
| Soit / Soient      | Let                   | Match singular/plural in English.                             |
| Supposons que      | Suppose that / Assume | Choose by register.                                           |
| On a               | We have               | Avoid repeated "one has" unless the impersonal style matters. |
| Il suffit de       | It suffices to        | Standard proof idiom.                                         |
| Il reste a montrer | It remains to show    | Standard proof idiom.                                         |
| Il en resulte que  | It follows that       | Use "hence" only in compact proof prose.                      |
| Par suite          | Consequently / hence  | Choose by rhythm.                                             |
| En effet           | Indeed                | Introduces justification.                                     |
| D'ou               | Hence                 | Use "whence" only when the register supports it.              |
| A fortiori         | A fortiori            | Keep loan phrase; already idiomatic in mathematical English.  |

## Notes Needing Review

- The cleaned source flags the synoptic diagram of the second edition as too damaged for reliable transcription. The
  English front matter preserves that warning rather than inventing a reconstruction.
- The notation index contains intentionally preserved uncertain OCR entries, such as `(Karfiness)` and `Lib` (*Women's
  Liberation*). These should be checked against the PDF if they become mathematically relevant.
