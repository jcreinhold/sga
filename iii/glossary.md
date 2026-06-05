# Glossary and Translation Ledger — SGA 3

This file records the translation choices made for the SGA 3 Markdown translation. It is the authoritative reference for
the parallel translators of individual Exposés; every translator must consult it before drafting and must obey it where
it applies.

## Core terminology

| French                                       | English                                       | Note                                                                                                                     |
| -------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| préschéma                                    | prescheme                                     | Historical SGA/EGA term. Used throughout SGA 3, matching SGA 1 and SGA 2 I–XIII.                                         |
| schéma                                       | scheme                                        | Older sense: separated prescheme. The 2011 re-edition retains this.                                                      |
| $S$-préschéma                                | $S$-prescheme                                 | A prescheme over $S$. Sometimes typeset `S-préschéma`; preserve hyphen.                                                  |
| $S$-schéma en groupes                        | $S$-group scheme                              | The relative form. Title-level for the whole Séminaire.                                                                  |
| faisceau                                     | sheaf                                         | Standard.                                                                                                                |
| faisceau (quasi-)cohérent                    | (quasi-)coherent sheaf                        | Standard.                                                                                                                |
| espace annelé                                | ringed space                                  | Standard.                                                                                                                |
| application                                  | map                                           | "Function" only in elementary set-theoretic contexts.                                                                    |
| morphisme                                    | morphism                                      | Standard.                                                                                                                |
| morphisme étale / lisse / plat / propre      | étale / smooth / flat / proper morphism       | Standard; matches SGA 1 glossary.                                                                                        |
| de présentation finie                        | of finite presentation                        | SGA 3 deliberately replaces *de type fini* by *de présentation finie* (cf. Intro §6); preserve.                          |
| de type fini                                 | of finite type                                | Use only when the source uses *de type fini*.                                                                            |
| revêtement étale                             | étale covering                                | Per SGA 1 glossary.                                                                                                      |
| immersion / immersion fermée / ouverte       | immersion / closed immersion / open immersion | Standard.                                                                                                                |
| ouvert / fermé / localement fermé            | open / closed / locally closed                | Standard.                                                                                                                |
| voisinage                                    | neighborhood                                  | American spelling.                                                                                                       |
| recouvrement                                 | covering                                      | "Cover" only in casual prose.                                                                                            |
| corps                                        | field                                         | False friend: not "body".                                                                                                |
| anneau                                       | ring                                          | Commutative by SGA convention unless stated.                                                                             |
| anneau local (noethérien)                    | (noetherian) local ring                       | Standard.                                                                                                                |
| anneau local régulier                        | regular local ring                            | Standard.                                                                                                                |
| corps résiduel                               | residue field                                 | Denoted $\kappa(x)$ or $\kappa(A)$ (per SGA 1).                                                                          |
| catégorie                                    | category                                      | Standard.                                                                                                                |
| foncteur / foncteur dérivé                   | functor / derived functor                     | Standard.                                                                                                                |
| foncteur exact / exact à gauche / à droite   | exact / left exact / right exact functor      | Standard.                                                                                                                |
| sous-foncteur                                | subfunctor                                    | Standard.                                                                                                                |
| foncteur représentable                       | representable functor                         | Central to SGA 3.                                                                                                        |
| représentation (d'un groupe par un foncteur) | representation                                | Be careful: SGA 3 uses *représenter* both for representable functors and for representations of groups; pick by context. |
| catégorie abélienne                          | abelian category                              | Standard.                                                                                                                |
| limite projective / inductive                | inverse / direct limit                        | Modern English.                                                                                                          |
| fibre                                        | fiber                                         | American spelling.                                                                                                       |
| fibre géométrique                            | geometric fiber                               | Standard. (Used heavily in Tome III for reductive groups.)                                                               |
| spécialisation                               | specialization                                | American spelling.                                                                                                       |
| canonique                                    | canonical                                     | Do *not* translate as "natural" unless the source specifically appeals to naturality.                                    |
| fonctoriel                                   | functorial                                    | Standard.                                                                                                                |
| naturel                                      | natural                                       | Reserve for genuine naturality.                                                                                          |
| à isomorphisme près                          | up to isomorphism                             | Standard.                                                                                                                |
| nécessaire et suffisant                      | necessary and sufficient                      | Sometimes "if and only if" in theorem statements.                                                                        |
| si et seulement si                           | if and only if                                | "Iff" only if local idiom permits.                                                                                       |

## SGA 3 topics: foundations (Tome I)

| French                                  | English                            | Note                                                                                                              |
| --------------------------------------- | ---------------------------------- | ----------------------------------------------------------------------------------------------------------------- |
| schéma en groupes                       | group scheme                       | Title-level term.                                                                                                 |
| $S$-groupe                              | $S$-group                          | Shorthand for *$S$-schéma en groupes*. Preserve.                                                                  |
| schéma en monoïdes                      | monoid scheme                      | Standard.                                                                                                         |
| schéma en anneaux                       | ring scheme                        | Standard.                                                                                                         |
| structure algébrique                    | algebraic structure                | Per Exposé I title.                                                                                               |
| cohomologie des groupes                 | group cohomology                   | Per Exposé I title.                                                                                               |
| univers (Univers)                       | universe                           | Set-theoretic universe (Grothendieck universe).                                                                   |
| catégorie `(Ens)`                       | category of sets `(Ens)`           | Keep the source notation `(Ens)`. Gloss only at first use.                                                        |
| catégorie `(Sch)`                       | category of schemes `(Sch)`        | Keep notation. The source writes $(Sch)/S$ for $S$-schemes.                                                       |
| catégorie `(Ann)`                       | category of rings `(Ann)`          | Keep notation.                                                                                                    |
| catégorie `(Gr)`                        | category of groups `(Gr)`          | Keep notation.                                                                                                    |
| `Ĉ`                                     | `Ĉ`                                | Notation for $\operatorname{Hom}(C^{\circ}, (Ens))$. OCR may produce `Cb`; restore the hat.                       |
| $C^{\circ}$                             | $C^{\circ}$ (opposite category)    | Keep ${}^{\circ}$ Unicode; OCR may give $o$ or `0`.                                                               |
| foncteur contravariant                  | contravariant functor              | Standard.                                                                                                         |
| topologie fpqc                          | fpqc topology                      | "Faithfully flat quasi-compact." Acronym kept; spell out on first use per Exposé.                                 |
| topologie fppf                          | fppf topology                      | "Faithfully flat of finite presentation." Same convention.                                                        |
| topologie étale                         | étale topology                     | Standard.                                                                                                         |
| topologie de Zariski                    | Zariski topology                   | Standard.                                                                                                         |
| descente fidèlement plate               | faithfully flat descent            | Matches SGA 1 glossary.                                                                                           |
| catégorie fibrée                        | fibered category                   | American spelling.                                                                                                |
| faisceau (au sens d'une topologie)      | sheaf (in the sense of a topology) | Standard.                                                                                                         |
| faisceau associé                        | associated sheaf                   | Standard.                                                                                                         |
| sous-foncteur représentable             | representable subfunctor           | Standard.                                                                                                         |
| objet en groupes                        | group object                       | When the source uses *objet en groupes* rather than *schéma en groupes*.                                          |
| algèbre de Hopf                         | Hopf algebra                       | Standard.                                                                                                         |
| algèbre affine                          | affine algebra                     | Standard.                                                                                                         |
| spectre                                 | spectrum                           | Standard.                                                                                                         |
| $\operatorname{Spec}(A)$                | $\operatorname{Spec}(A)$           | Keep as-is; the source sometimes writes $\operatorname{Spec} A$ without parens.                                   |
| extension infinitésimale                | infinitesimal extension            | Per Exposé III title.                                                                                             |
| déformation infinitésimale              | infinitesimal deformation          | Standard.                                                                                                         |
| fibré tangent                           | tangent bundle                     | Per Exposé II title. Context may favor "tangent sheaf"; flag first occurrence.                                    |
| fibré normal                            | normal bundle                      | Standard.                                                                                                         |
| fibré principal                         | principal bundle                   | Standard.                                                                                                         |
| algèbre de Lie                          | Lie algebra                        | Standard. $Lie(G/S)$ notation preserved.                                                                          |
| $p$-algèbre de Lie                      | $p$-Lie algebra                    | Modern: *restricted Lie algebra*; the source's term is *$p$-algèbre de Lie*. Keep it; flag with a one-time gloss. |
| schéma en groupes radiciel de hauteur 1 | radicial group scheme of height 1  | Per Intro §1. *Radiciel* = purely inseparable.                                                                    |
| radiciel                                | radicial                           | Loanword (per EGA); not "radical".                                                                                |
| opérateur différentiel                  | differential operator              | Per Exposé VII_A title.                                                                                           |
| groupe formel                           | formal group                       | Per Exposé VII_B title.                                                                                           |
| $S$-foncteur                            | $S$-functor                        | A functor from $(Sch)^{\circ}/S$ to `(Ens)`. Preserve.                                                            |
| passage au quotient                     | passage to the quotient            | Standard.                                                                                                         |
| schéma quotient                         | quotient scheme                    | Per Exposé V title.                                                                                               |
| relation d'équivalence                  | equivalence relation               | Standard.                                                                                                         |
| groupoïde                               | groupoid                           | Standard.                                                                                                         |
| sous-groupe distingué / normal          | normal subgroup                    | Standard (English does not distinguish).                                                                          |
| centralisateur / normalisateur          | centralizer / normalizer           | American spelling.                                                                                                |
| transporteur                            | transporter                        | Standard.                                                                                                         |
| stabilisateur                           | stabilizer                         | American spelling.                                                                                                |

## SGA 3 topics: multiplicative-type and Lie-algebra material (Tome II)

| French                             | English                         | Note                                                                   |
| ---------------------------------- | ------------------------------- | ---------------------------------------------------------------------- |
| groupe diagonalisable              | diagonalizable group            | American spelling. Per Exposé VIII title.                              |
| groupe de type multiplicatif       | group of multiplicative type    | Per Exposé IX–X titles.                                                |
| caractère / cocaractère            | character / cocharacter         | Standard.                                                              |
| $D(M)$                             | $D(M)$                          | The Cartier dual of the abstract group $M$. Notation preserved.        |
| groupe constant                    | constant group                  | Standard.                                                              |
| groupe tordu                       | twisted group                   | Standard.                                                              |
| forme tordue                       | twisted form                    | Standard.                                                              |
| critère de représentabilité        | representability criterion      | Per Exposé XI title.                                                   |
| tore                               | torus                           | Standard. Plural: *tori*.                                              |
| tore maximal                       | maximal torus                   | Standard.                                                              |
| sous-tore                          | subtorus                        | Standard.                                                              |
| variété des tores maximaux         | variety of maximal tori         | Standard.                                                              |
| groupe de Weyl                     | Weyl group                      | Standard.                                                              |
| sous-groupe de Cartan              | Cartan subgroup                 | Standard.                                                              |
| centre / centre réductif           | center / reductive center       | American spelling. $Z(G)$, $rad(G)$, $rad_{u}(G)$ notations preserved. |
| élément régulier                   | regular element                 | Per Exposés XIII–XIV titles.                                           |
| élément semi-simple / unipotent    | semisimple / unipotent element  | "Semisimple" one word, no hyphen.                                      |
| polynôme caractéristique           | characteristic polynomial       | Standard.                                                              |
| sous-groupe lisse                  | smooth subgroup                 | Standard.                                                              |
| groupe (algébrique) lisse          | smooth (algebraic) group        | Standard.                                                              |
| groupe de rang unipotent nul       | group of zero unipotent rank    | Per Exposé XVI title.                                                  |
| groupe algébrique unipotent        | unipotent algebraic group       | Per Exposé XVII title.                                                 |
| extension (de groupes algébriques) | extension (of algebraic groups) | Standard.                                                              |
| loi rationnelle                    | rational law                    | Per Exposé XVIII title (Weil's theorem on rational laws).              |
| théorème de Weil                   | Weil's theorem                  | Standard.                                                              |

## SGA 3 topics: reductive groups (Tome III)

| French                               | English                                 | Note                                                                             |
| ------------------------------------ | --------------------------------------- | -------------------------------------------------------------------------------- |
| groupe réductif                      | reductive group                         | Per Tome III title and Exposés XIX–XXVI.                                         |
| groupe semi-simple                   | semisimple group                        | One word, no hyphen.                                                             |
| groupe résoluble                     | solvable group                          | American spelling.                                                               |
| groupe à rang semi-simple 1          | group of semisimple rank 1              | Per Exposé XX title.                                                             |
| déploiement / déployé                | splitting / split                       | Standard.                                                                        |
| groupe déployable                    | splittable group                        | Standard.                                                                        |
| sous-groupe parabolique              | parabolic subgroup                      | Per Exposé XXVI title.                                                           |
| sous-groupe de Borel                 | Borel subgroup                          | Standard.                                                                        |
| sous-groupe radiciel                 | root subgroup                           | The $U_{\alpha}$ of a reductive group.                                           |
| donnée radicielle                    | root datum                              | Per Exposé XXI title. Plural: *root data*.                                       |
| système de racines                   | root system                             | Standard.                                                                        |
| racine                               | root                                    | Standard. (Not "radical" — that is *radical*.)                                   |
| coracine                             | coroot                                  | Standard.                                                                        |
| poids                                | weight                                  | Standard.                                                                        |
| groupe épinglé                       | pinned group                            | Per Exposé XXIII title. *Épinglage* = *pinning*; "framed group" only in passing. |
| épinglage                            | pinning                                 | Standard (in this translation).                                                  |
| unicité des groupes épinglés         | uniqueness of pinned groups             | Per Exposé XXIII title.                                                          |
| automorphisme (d'un groupe réductif) | automorphism                            | Per Exposé XXIV title.                                                           |
| isogénie                             | isogeny                                 | Standard.                                                                        |
| groupe simplement connexe / adjoint  | simply connected / adjoint group        | Standard.                                                                        |
| théorème d'existence                 | existence theorem                       | Per Exposé XXV title.                                                            |
| théorème d'unicité                   | uniqueness theorem                      | Standard.                                                                        |
| groupes « de Tôhoku »                | "Tôhoku" groups                         | Chevalley's groups over $\mathbb{Z}$. Italics on *Tôhoku* in journal references. |
| Bible (Séminaire Chevalley 1956/58)  | the *Bible* (Chevalley Seminar 1956–58) | SGA 3 cites the Chevalley Seminar as "Bible". Render the same way.               |
| Bourbaki                             | Bourbaki                                | Standard.                                                                        |
| théorie de Borel-Chevalley           | Borel–Chevalley theory                  | Use en-dash between author names.                                                |
| théorie de Demazure                  | Demazure's theory                       | Standard.                                                                        |

## Proof movement

These follow $references/french-math-idiom.md$ of the translation skill, with SGA-specific tweaks (inherited from SGA
1/SGA 2).

| French                                | English                                         | Note                                                            |
| ------------------------------------- | ----------------------------------------------- | --------------------------------------------------------------- |
| Soit / Soient X / X et Y              | Let X / X and Y be                              | Match singular / plural.                                        |
| Supposons (que)                       | Suppose (that) / Assume                         | "Assume" if the sentence is a hypothesis register.              |
| Posons                                | Set / Put                                       | "Put" for variable assignments; "Set" for ad-hoc definitions.   |
| Notons                                | Denote / Write / Note                           | Choose by what follows; *Notons que* is "Note that".            |
| On a                                  | We have                                         | Not "one has" except for register.                              |
| On en déduit                          | We deduce                                       | "It follows" if the inference is non-trivial.                   |
| Montrons (que)                        | We show (that)                                  | "It remains to show" if it closes a reduction.                  |
| Il suffit de                          | It suffices to                                  | Standard.                                                       |
| Il reste à montrer                    | It remains to show                              | Standard.                                                       |
| Il en résulte (que) / Il résulte (de) | It follows (that) / It follows (from)           | Choose by structure; "hence" in compact proof prose.            |
| Par suite                             | Consequently / hence                            | Avoid "as a result of this".                                    |
| D'où                                  | Hence / whence                                  | "Whence" only if register supports it.                          |
| En effet                              | Indeed                                          | Standard introduces a justification.                            |
| Or                                    | Now                                             | Pivot conjunction; "but" only if the sentence really contrasts. |
| Donc                                  | Thus / hence / so                               | Choose by rhythm.                                               |
| D'une part … d'autre part             | On the one hand … on the other hand             | Keep both clauses.                                              |
| Cela achève la démonstration          | This completes the proof                        | Standard.                                                       |
| CQFD                                  | QED                                             | Or "This proves the claim."                                     |
| à savoir                              | namely                                          | Standard.                                                       |
| compte tenu de                        | taking into account / in view of                | Choose by clause weight.                                        |
| en vertu de                           | by virtue of / by                               | "By" usually suffices.                                          |
| moyennant                             | by means of / using                             | Standard.                                                       |
| quitte à                              | (possibly) by … / replacing X by Y if necessary | A standard French move.                                         |
| à condition que                       | provided that                                   | Standard.                                                       |
| dès que                               | as soon as                                      | Standard.                                                       |
| chaque fois que                       | whenever                                        | Standard.                                                       |

## Modality and certainty

Preserve modality exactly; do *not* upgrade certainty.

| French                               | English                                  |
| ------------------------------------ | ---------------------------------------- |
| il est clair que                     | it is clear that                         |
| il est évident que                   | it is evident that                       |
| manifestement / il est manifeste que | manifestly / it is manifest that         |
| il semble que                        | it seems that                            |
| on s'attend à ce que                 | one expects that                         |
| il est probable que                  | it is probable that                      |
| sans doute                           | doubtless / probably (context-dependent) |
| conjecturalement                     | conjecturally                            |
| il y a tout lieu de penser que       | there is every reason to think that      |
| on peut conjecturer                  | one may conjecture                       |
| il n'est pas exclu que               | it is not excluded that                  |
| il se peut que                       | it may be that                           |
| vraisemblablement                    | presumably                               |

## Cross-volume citations

| Source                                       | English citation form                                                                     |
| -------------------------------------------- | ----------------------------------------------------------------------------------------- |
| EGA I, II, III, IV (with chapter and number) | `EGA I, 1.2.3` / `EGA IV, 1.4`, etc. Preserve the chapter Roman numeral.                  |
| SGA 1 (with Exposé and number)               | `SGA 1, I 5.1` / `SGA 1, VIII 1.7`, etc. Match the source's spacing.                      |
| SGA n in general                             | `SGA n, X y.z` per the Introduction §7 convention.                                        |
| Bible = Séminaire Chevalley 1956/58          | *Bible* (italicised) or $S\acute{e}minaire Chevalley 1956/58$. Keep the source's wording. |
| TDTE                                         | Grothendieck's *Techniques de descente et théorèmes d'existence* (Bourbaki 1959–62).      |
| Mumford GIT                                  | Mumford, *Geometric Invariant Theory*. Italics.                                           |
| Demazure–Gabriel                             | *Groupes algébriques* (Demazure–Gabriel). Italics, en-dash between author names.          |

## Common OCR repairs

The 2011 SMF re-edition is modern LaTeX, so OCR is high quality. Most math symbols survive. These items still recur:

- **Dropped sub/superscripts on big operators.** $\Gamma$, $H^{i}$, $Ext^{i}$, $R^{i} f_{*}$, `O_X`, `Lie`, $T_{e} G$,
  $\mu_{n}$, $G_{m}$, $G_{a}$, $\alpha_{p}$, $D(M)$, $w\alpha(X)$, root operators $U_{\alpha}$, $T_{\alpha}$ may lose
  their indices. Recover from context.
- **`Cb` instead of `Ĉ`.** Hat on category symbol drops. Restore.
- **$(\ast)$ / $(\ast\ast)$ / $(\ast\ast\ast)$ for original footnote markers.** Render as
  $[{}^{<}expos\acute{e}>-<sec>-<n>]$ slugs ($[{}^{I}-1-1]$, $[{}^{I}-1-2]$, …).
- **`(N)` for N.D.E. footnote markers** (small Arabic digit in parentheses). Render as $[{}^{N}.D.E-<expos\acute{e}>-N]$
  ($[{}^{N}.D.E-I-3]$, etc.) and translate the body of the note.
- **$\ddot{\imath}$ or `ı`** (dotless i with floating diacritic) — restore to `ï`.
- **Backslash escapes** surviving from LaTeX: `\&` → `&`, `\#` → `#`.
- **Arrows.** $-\to$ → $\to$, $7\to$ → $\mapsto$, $\sim=$ (often broken across lines) → $\cong$, `\sim\n\to` (OCR
  artefact) → $\xrightarrow{\sim}$ or $\to$ annotated `~`.
- **Greek subscripts.** $\pi 1$, `H0`, `G m` etc. should be $\pi_{1}$, $H^{0}$, $G_{m}$ (with backticks).
- **`◦` for opposite category** drops to $o$ or `0`. Restore ${}^{\circ}$ or ${}^{\circ}$ (degree sign), matching local
  convention.
- **VIB, VIIA, VIIB citations.** Render as `VI_B`, $VII_{A}$, $VII_{B}$. Preserve subscript via underscore.
- **« » guillemets.** Translate to English quotes ($"\cdots"$) unless the source uses them to mark a Grothendieckian
  coinage, in which case keep them as quotation marks in the translation too.
- **Hat across line break** for formal completions: $Et( b / X)$ → $\hat{E}t(\hat{X})$. Same as SGA 2.
- **Math run-ons.** Restore displayed equations as fenced ```` ```text ```` blocks.
- **Embedded N.D.E. footnotes.** Source convention is $(N) N.D.E. : <text>$ at page bottom. Recover the whole footnote
  (which may span lines) and translate as $[{}^{N}.D.E-<expos\acute{e}>-N]$.

## Style anchors (non-negotiable for cross-volume consistency)

Inherited from SGA 1 / SGA 2. Deviate only if the SGA 1/2 corpus is itself inconsistent.

- **File naming.** `00-i-errata.md`, `00-i-avertissement-introduction.md`, `00-ii-preface.md`, `00-iii-errata.md`,
  `NN-<slug>.md` for each Exposé (using `06A`, `06B`, `07A`, `07B` for the split Exposés), `glossary.md`, `README.md`,
  `zz-i-index-notations.md`, `zz-iii-index-notations.md`, `zz-iii-index-terminologique.md`.
- **Heading hierarchy.** `# Exposé N. <English Title>` (with `_A` / `_B` suffix where applicable), then numbered
  `## 1. <Section Title>`, then sub-sections `### 1.1. <Subsection>`. The Exposé heading carries a
  `<!-- label: III.<Roman> -->` comment on the next line.
- **Statement blocks.** `**Proposition.**`, `**Lemma.**`, `**Theorem.**`, `**Corollary.**`, `**Definition.**`,
  `**Remark.**`, `**Example.**`, `**Scholie.**` on their own line. Statement numbers go inline:
  `**Proposition 3.1.2.** *Statement…*`. The label `<!-- label: III.<Roman>.X.Y -->` follows on the next line.
- **Math.** Unicode math wrapped in backticks for inline. Displayed math in fenced ```` ```text ```` blocks. Numbered
  displayed equations get `<!-- label: eq:III.<Roman>.X.Y -->`.
- **Footnotes.** Markdown $[{}^{slug}]$ syntax. Original footnotes: $[{}^{<}expos\acute{e}>-<sec>-<n>]$ (e.g.
  $[{}^{I}-1-1]$). Editor footnotes: $[{}^{N}.D.E-<expos\acute{e}>-<n>]$ (e.g. $[{}^{N}.D.E-I-3]$).
- **Page marks.** `<!-- original page N -->` at page boundaries (page numbers from the 2011 re-edition).
- **Cross-references.** Source's own convention: $(VI_{B}, 5.3)$, `(EGA III, 4.1.5)`, `(SGA 1, IV 3.8)`, `(Bible, XIV)`.
- **Bibliographies.** Each Exposé's own bibliography section is preserved as `## Bibliography`, entries as a numbered
  (or `[Key]`-keyed) list, journal titles in italics.

## Cross-Exposé additions (discovered during translation)

Each translated Exposé file ends with a fenced HTML-comment block titled `LEDGER DELTA — Exposé <N>` recording new
terminology choices that the translator encountered beyond what this glossary already covers. Those deltas are kept in
place at the foot of each Exposé rather than copied here, both to preserve the audit trail and because consolidating the
deltas (which span ~500–1,500 terms across the 26 Exposés) into a single table would make the glossary harder to scan
than the per-Exposé tables. A future cleanup pass may de-duplicate the most cross-cutting entries (e.g. *dévissage*, the
`prescheme`/`scheme` split, Demazure's *épinglage* → *pinning*, Bertin's "anti-affine" envelope) into the tables above;
until then, consult the deltas in the Exposé files for the authoritative per-Exposé terminology choices.
