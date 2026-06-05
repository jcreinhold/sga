# Glossary and Translation Ledger — SGA 2

This file records the translation choices made for the SGA 2 Markdown translation. It is the authoritative reference for
the parallel translators of individual Exposés; every translator must consult it before drafting and must obey it where
it applies.

## Core terminology

| French                                     | English                                       | Note                                                                                                                                              |
| ------------------------------------------ | --------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| préschéma                                  | prescheme                                     | Historical SGA/EGA term. Used through Exposés I–XIII. *Not* silently modernized.                                                                  |
| schéma                                     | scheme                                        | In Exposés I–XIII, denotes a separated prescheme. In Exposé XIV, the modern meaning (= prescheme of Exp. I–XIII), per Raynaud's opening footnote. |
| schéma séparé (Exp. XIV)                   | separated scheme                              | Raynaud's modern terminology in Exposé XIV.                                                                                                       |
| faisceau                                   | sheaf                                         | Standard.                                                                                                                                         |
| faisceau (quasi-)cohérent                  | (quasi-)coherent sheaf                        | Standard.                                                                                                                                         |
| espace annelé                              | ringed space                                  | Standard.                                                                                                                                         |
| espace topologique                         | topological space                             | Standard.                                                                                                                                         |
| application                                | map                                           | "Function" only in elementary set-theoretic contexts.                                                                                             |
| morphisme                                  | morphism                                      | Standard.                                                                                                                                         |
| morphisme étale / lisse / plat / propre    | étale / smooth / flat / proper morphism       | Standard; matches SGA 1 glossary.                                                                                                                 |
| revêtement étale                           | étale covering                                | Per SGA 1 glossary.                                                                                                                               |
| immersion / immersion fermée / ouverte     | immersion / closed immersion / open immersion | Standard.                                                                                                                                         |
| ouvert / fermé / localement fermé          | open / closed / locally closed                | Standard.                                                                                                                                         |
| voisinage                                  | neighborhood                                  | American spelling.                                                                                                                                |
| recouvrement                               | covering                                      | "Cover" only in casual prose.                                                                                                                     |
| corps                                      | field                                         | False friend: not "body".                                                                                                                         |
| anneau                                     | ring                                          | Commutative by SGA convention unless stated.                                                                                                      |
| anneau local (noethérien)                  | (noetherian) local ring                       | Standard.                                                                                                                                         |
| anneau local régulier                      | regular local ring                            | Standard.                                                                                                                                         |
| corps résiduel                             | residue field                                 | Denoted $\kappa(x)$ or $\kappa(A)$ (per SGA 1).                                                                                                   |
| module de type fini                        | finitely generated module                     | "Of finite type" if matching adjacent SGA 1 prose.                                                                                                |
| de type fini (morphisme, présentation)     | of finite type                                | Morphism-level terminology, EGA-standard.                                                                                                         |
| catégorie                                  | category                                      | Standard.                                                                                                                                         |
| foncteur / foncteur dérivé                 | functor / derived functor                     | Standard.                                                                                                                                         |
| foncteur exact / exact à gauche / à droite | exact / left exact / right exact functor      | Standard.                                                                                                                                         |
| sous-foncteur                              | subfunctor                                    | Standard.                                                                                                                                         |
| catégorie dérivée $D^{+}(X)$               | derived category $D^{+}(X)$                   | Used principally in Exposé XIV.                                                                                                                   |
| catégorie abélienne                        | abelian category                              | Standard.                                                                                                                                         |
| limite projective / inductive              | inverse / direct limit                        | Modern English. Flag the SGA-era usage in a translator note on first occurrence per Exposé.                                                       |
| fibre                                      | fiber                                         | American spelling.                                                                                                                                |
| spécialisation                             | specialization                                | American spelling.                                                                                                                                |
| canonique                                  | canonical                                     | Do *not* translate as "natural" unless the source specifically appeals to naturality.                                                             |
| fonctoriel                                 | functorial                                    | Standard.                                                                                                                                         |
| naturel                                    | natural                                       | Reserve for genuine naturality.                                                                                                                   |
| à isomorphisme près                        | up to isomorphism                             | Standard.                                                                                                                                         |
| nécessaire et suffisant                    | necessary and sufficient                      | Sometimes "if and only if" in theorem statements.                                                                                                 |
| si et seulement si                         | if and only if                                | "Iff" only if local idiom permits.                                                                                                                |

## SGA 2 topics

| French                                                      | English                                                                                                                    | Note                                                                                                                                                 |
| ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| cohomologie locale                                          | local cohomology                                                                                                           | Title-level. Not "cohomology locally".                                                                                                               |
| cohomologie à support dans Y                                | cohomology with supports in Y                                                                                              | Match the SGA 1 phrasing.                                                                                                                            |
| $H^{i}_{Y}(X, F)$ (sections with support)                   | $H^{i}_{Y}(X, F)$                                                                                                          | Global, non-underlined.                                                                                                                              |
| $\mathcal{H}^{i}_{Y}(F)$ (sheafified, underlined in source) | $\mathcal{H}^{i}_{Y}(F)$                                                                                                   | Use the script-H Unicode $\mathcal{H}$ to mark the sheafified functor. Where OCR drops the underline, the surrounding French reveals which is meant. |
| $\Gamma_{Z}$ (global sections with support in $Z$)          | $\Gamma_{Z}$                                                                                                               | Global, non-underlined functor.                                                                                                                      |
| $\Gamma Z$ underlined (sheafified)                          | $\Gamma_{Z}$ (sheafified) — render as $\Gamma Z$ or $\Gamma_{Z}$ with a one-line typographic note at first use per Exposé. | The translator should pin the convention at first use in each Exposé.                                                                                |
| sorite                                                      | sorites                                                                                                                    | Loanword, kept (per SGA 1).                                                                                                                          |
| dévissage                                                   | dévissage                                                                                                                  | Loanword, kept.                                                                                                                                      |
| Hartogs (phénomène de —)                                    | Hartogs phenomenon                                                                                                         | Standard.                                                                                                                                            |
| profondeur                                                  | depth                                                                                                                      | Standard.                                                                                                                                            |
| profondeur cohomologique                                    | cohomological depth                                                                                                        | Per source index.                                                                                                                                    |
| profondeur étale                                            | étale depth                                                                                                                | Per source index.                                                                                                                                    |
| profondeur homotopique                                      | homotopical depth                                                                                                          | Per source index.                                                                                                                                    |
| profondeur homotopique rectifiée                            | rectified homotopical depth                                                                                                | Per source index.                                                                                                                                    |
| profondeur géométrique                                      | geometrical depth                                                                                                          | Per source index. ("Geometrical" with -ical, as the index uses it.)                                                                                  |
| $M$-régulier                                                | $M$-regular                                                                                                                | For sequences regular on $M$.                                                                                                                        |
| anneau de Cohen-Macaulay                                    | Cohen-Macaulay ring                                                                                                        | Standard.                                                                                                                                            |
| théorème de comparaison                                     | comparison theorem                                                                                                         | Per source index.                                                                                                                                    |
| théorème d'existence                                        | existence theorem                                                                                                          | Per source index.                                                                                                                                    |
| théorème de finitude                                        | finiteness theorem                                                                                                         | Per source index.                                                                                                                                    |
| théorème de dualité (locale / projective)                   | (local / projective) duality theorem                                                                                       | Per source index.                                                                                                                                    |
| théorème d'excision                                         | excision theorem                                                                                                           | Per source index.                                                                                                                                    |
| module dualisant / foncteur dualisant                       | dualizing module / dualizing functor                                                                                       | Per source index.                                                                                                                                    |
| enveloppe injective                                         | injective envelope                                                                                                         | Per source index.                                                                                                                                    |
| extension essentielle                                       | essential extension                                                                                                        | Per source index.                                                                                                                                    |
| forme résidu                                                | residue form                                                                                                               | Per source index.                                                                                                                                    |
| résolution injective / projective                           | injective / projective resolution                                                                                          | Standard.                                                                                                                                            |
| résolution flasque                                          | flasque (flabby) resolution                                                                                                | Use "flasque" (the SGA term) inline; "flabby" only if the local prose already uses it.                                                               |
| faisceau flasque                                            | flasque sheaf                                                                                                              | Per SGA usage.                                                                                                                                       |
| faisceau mou / fin                                          | soft / fine sheaf                                                                                                          | Less common in SGA 2; if encountered, use these renderings.                                                                                          |
| suite spectrale                                             | spectral sequence                                                                                                          | Standard.                                                                                                                                            |
| terme initial / aboutissement                               | initial term / abutment                                                                                                    | Standard.                                                                                                                                            |
| homomorphisme de Gysin                                      | Gysin homomorphism                                                                                                         | Per source index.                                                                                                                                    |
| théorème de pureté de Zariski-Nagata                        | Zariski-Nagata purity theorem                                                                                              | Per source index.                                                                                                                                    |
| théorème de pureté cohomologique                            | cohomological purity theorem                                                                                               | Per source index.                                                                                                                                    |
| théorème de semi-pureté cohomologique                       | cohomological semi-purity theorem                                                                                          | Per source index.                                                                                                                                    |
| couple parafactoriel de préschémas                          | parafactorial pair of preschemes                                                                                           | Per source index. ("Pair" preserves the *couple* sense.)                                                                                             |
| anneau local parafactoriel                                  | parafactorial local ring                                                                                                   | Per source index.                                                                                                                                    |
| anneau local pur                                            | pure local ring                                                                                                            | Per source index.                                                                                                                                    |
| couple pur de préschémas                                    | pure pair of preschemes                                                                                                    | Per source index.                                                                                                                                    |
| géométriquement factoriel / parafactoriel                   | geometrically factorial / parafactorial                                                                                    | Per source index.                                                                                                                                    |
| anneau strictement local                                    | strictly local ring                                                                                                        | Per source index.                                                                                                                                    |
| condition de Lefschetz                                      | Lefschetz condition                                                                                                        | Per source index.                                                                                                                                    |
| condition de Lefschetz effective                            | effective Lefschetz condition                                                                                              | Per source index.                                                                                                                                    |
| théorème de Lefschetz affine                                | affine Lefschetz theorem                                                                                                   | Per source index.                                                                                                                                    |
| théorèmes de Lefschetz (du type —)                          | Lefschetz-type theorems / Lefschetz theorems                                                                               | Either rendering, depending on rhythm.                                                                                                               |
| groupes d'homotopie locale                                  | local homotopy groups                                                                                                      | Per source index.                                                                                                                                    |
| platitude normale                                           | normal flatness                                                                                                            | Standard.                                                                                                                                            |
| complétion formelle                                         | formal completion                                                                                                          | Standard.                                                                                                                                            |
| complété formel (de $X$ le long de $Y$)                     | formal completion (of $X$ along $Y$)                                                                                       | Standard; the hat $\hat{X}$ notation is preserved.                                                                                                   |
| section hyperplane                                          | hyperplane section                                                                                                         | Standard.                                                                                                                                            |
| schéma algébrique projectif                                 | projective algebraic scheme                                                                                                | Title-level for Exposé XII.                                                                                                                          |
| théorème de représentabilité de Brown                       | Brown's representability theorem                                                                                           | If cited in N.D.E. footnotes.                                                                                                                        |
| Tôhoku                                                      | *Tôhoku*                                                                                                                   | Cite as the journal/article; italicize.                                                                                                              |

## Proof movement

These follow $references/french-math-idiom.md$ of the translation skill, with SGA-specific tweaks.

| French                                | English                                         | Note                                                                           |
| ------------------------------------- | ----------------------------------------------- | ------------------------------------------------------------------------------ |
| Soit / Soient X / X et Y              | Let X / X and Y be                              | Match singular / plural.                                                       |
| Supposons (que)                       | Suppose (that) / Assume                         | "Assume" if the sentence is a hypothesis register.                             |
| Posons                                | Set / Put                                       | "Put" for variable assignments; "Set" for ad-hoc definitions.                  |
| Notons                                | Denote / Write / Note                           | Choose by what follows; *Notons que* is "Note that".                           |
| On a                                  | We have                                         | Not "one has" except for register.                                             |
| On en déduit                          | We deduce                                       | "It follows" if the inference is non-trivial.                                  |
| Montrons (que)                        | We show (that)                                  | "It remains to show" if it closes a reduction.                                 |
| Il suffit de                          | It suffices to                                  | Standard.                                                                      |
| Il reste à montrer                    | It remains to show                              | Standard.                                                                      |
| Il en résulte (que) / Il résulte (de) | It follows (that) / It follows (from)           | Choose by structure; "hence" in compact proof prose.                           |
| Par suite                             | Consequently / hence                            | Avoid "as a result of this".                                                   |
| D'où                                  | Hence / whence                                  | "Whence" only if register supports it.                                         |
| En effet                              | Indeed                                          | Standard introduces a justification.                                           |
| Or                                    | Now                                             | Pivot conjunction; "but" only if the sentence really contrasts.                |
| Donc                                  | Thus / hence / so                               | Choose by rhythm.                                                              |
| D'une part … d'autre part             | On the one hand … on the other hand             | Keep both clauses.                                                             |
| Cela achève la démonstration          | This completes the proof                        | Standard.                                                                      |
| CQFD                                  | QED                                             | Or "This proves the claim."                                                    |
| à savoir                              | namely                                          | Standard.                                                                      |
| compte tenu de                        | taking into account / in view of                | Choose by clause weight.                                                       |
| en vertu de                           | by virtue of / by                               | "By" usually suffices.                                                         |
| moyennant                             | by means of / using                             | Standard.                                                                      |
| quitte à                              | (possibly) by … / replacing X by Y if necessary | A standard French move; "replacing X by Y if necessary" reads best in English. |
| à condition que                       | provided that                                   | Standard.                                                                      |
| dès que                               | as soon as                                      | Standard.                                                                      |
| chaque fois que                       | whenever                                        | Standard.                                                                      |

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

## Common OCR repairs

These recur across the source files. Apply them locally as the translator reads each block; do not silently "correct"
the mathematics — only repair what the OCR clearly mangled, and flag anything genuinely ambiguous with a
`<!-- TRANSLATOR NOTE: ... -->` comment.

- **Dropped sub/superscripts on big operators.** $\Gamma$, $H^{i}$, $Ext^{i}$, $R^{i} f_{*}$, `O_X`, $H^{\bullet}$,
  $H_{\bullet}$ routinely lose their indices. The surrounding French sentence almost always names them ("la cohomologie
  locale de F le long de Y", "les $H^{i}$ de F", etc.); recover from context.
- **Underline loss on sheafified functors.** SGA 2 distinguishes $\Gamma Z$ (the global section functor —
  non-underlined) from $\Gamma Z$ (the sheafified functor — underlined). The OCR routinely loses the underline. In the
  translation, render the sheafified functor with a script-H $\mathcal{H}$ for the cohomology version
  ($\mathcal{H}^{i}_{Y}(F)$) and keep an explicit $\Gamma Z$ for the underlined section functor, pinning the convention
  at first use per Exposé with a small note.
- **Hat across line break.** Formal-completion hats break across lines: $Et( b / X)$ is $\hat{E}t(\hat{X})$. `X b` after
  a closing paren is $\hat{X}$. Repair as needed.
- **OCR substitutions for arrows.**
    - $7\to$ is $\mapsto$.
    - $-\to$ is $\to$.
    - $\sim=$ (often broken across lines) is $\cong$.
    - `\sim\n\to` (OCR artefact, with literal newline) is $\xrightarrow{\sim}$ or $\to$ annotated with `~`; pick the
      rendering that matches what is being claimed.
- **OCR substitutions for accents.**
    - $Et(X)$ should be $\hat{E}t(X)$ (the étale site / category of étale objects).
    - `etale` should be `étale`.
    - `Tohoku` should be *Tôhoku*.
- **Greek subscripts.** $\pi 1$, $\pi 0$, `H1`, `H0` etc. should be $\pi_{1}$, $\pi_{0}$, $H^{1}$, $H^{0}$ etc.
  (Unicode), inside backticks.
- **Math run-ons.** When a displayed equation has been broken into prose by the OCR, restore it as a fenced
  ```` ```text ```` block. - **Embedded N.D.E. footnotes.** Source convention is `(N) N.D.E. : <text>` at the bottom of
  a page. Recover the whole footnote (which may span lines) and render it as `[^N.D.E-N]` (or
  `[^N.D.E-<expose>-<n>]` if multiple Exposés might collide) with its English translation in the footnote body. -
  **Dash lead-ins.** Statement bodies preceded by `—` in the source (after `Proposition X.Y.`, $Th\acute{e}or\grave{e}me
  X.Y.$, etc.) are rendered SGA 1-style: bold keyword on its own line, then a paragraph break, then the body.

## Cross-Exposé additions (discovered during translation)

Consolidated from the per-Exposé ledger deltas appended at the foot of each translation file. Refer to that file for the
original context. New cross-cutting terms encountered during translation:

| French                                            | English                                                 | Note                                                                      |
| ------------------------------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------------- |
| sous-faisceau                                     | subsheaf                                                | Standard.                                                                 |
| extension par 0 (en dehors de Z)                  | extension by 0 (outside Z)                              | Standard for $j_{!}$ constructions.                                       |
| famille de supports (au sens de Cartan)           | family of supports (in Cartan's sense)                  | Kept verbatim from the source.                                            |
| à support dans Z                                  | with support in Z                                       | Standard.                                                                 |
| faisceautiser                                     | "sheafify"                                              | In quotes when the source treats it as a coinage.                         |
| par abus de langage                               | by abuse of language                                    | Standard.                                                                 |
| à valeurs dans                                    | with values in                                          | Standard.                                                                 |
| aboutissement                                     | abutment                                                | Of a spectral sequence.                                                   |
| terme initial                                     | initial term                                            | Of a spectral sequence.                                                   |
| immersion canonique                               | canonical immersion                                     | Standard.                                                                 |
| partie localement fermée                          | locally closed subset                                   | Standard.                                                                 |
| suite exacte de cohomologie relative              | exact sequence of relative cohomology                   | Standard.                                                                 |
| $\partial$-foncteur / $\delta$-foncteur           | $\partial$-functor / $\delta$-functor                   | Preserve Grothendieck's distinction.                                      |
| foncteur cohomologique universel                  | universal cohomological functor                         | Standard.                                                                 |
| système projectif essentiellement nul             | essentially zero projective system                      | Standard SGA terminology.                                                 |
| opérateur bord                                    | boundary operator                                       | Standard.                                                                 |
| cohomologie de Koszul / complexe de Koszul        | Koszul cohomology / Koszul complex                      | Standard.                                                                 |
| `Module`, `Idéal`, `Algèbre` (capitalised)        | `Module`, `Ideal`, `Algebra` (capitalised)              | Per SGA convention for sheaves of modules/ideals/algebras. Preserve case. |
| annulateur                                        | annihilator                                             | Standard.                                                                 |
| assassin de M                                     | "assassin of $M$"                                       | Bourbaki idiom; kept in quotes with explanatory gloss.                    |
| racine de $a$                                     | radical of $a$                                          | Symbol $r(a)$ preserved.                                                  |
| $M$-régulier (élément, suite)                     | $M$-regular (element, sequence)                         | Per glossary; matches the depth taxonomy.                                 |
| homothétie de rapport $a$                         | multiplication by $a$                                   | "Homothety of ratio" is unidiomatic in module-theoretic prose.            |
| suite régulière                                   | regular sequence                                        | Standard.                                                                 |
| anneau semi-local                                 | semi-local ring                                         | Standard.                                                                 |
| codimension homologique ($codh_{A} M$)            | homological codimension ($codh_{A} M$)                  | Older terminology for depth; symbol preserved.                            |
| platitude / fidèlement plat                       | flatness / faithfully flat                              | Standard.                                                                 |
| antifiltre                                        | antifilter                                              | Order-theoretic loanword.                                                 |
| chaîne (condition des chaînes)                    | chain (chain condition)                                 | Standard.                                                                 |
| connexe en codimension $d - 1$                    | connected in codimension $d - 1$                        | Standard.                                                                 |
| ensemblistement                                   | set-theoretically                                       | Standard.                                                                 |
| intersection complète (absolue)                   | (absolute) complete intersection                        | Standard.                                                                 |
| image directe supérieure                          | higher direct image                                     | $R^{i} f_{*}$ notation preserved.                                         |
| Module gradué                                     | graded Module                                           | Capital preserved per SGA convention.                                     |
| modules gradués                                   | graded modules                                          | Lowercase when context is module-level, not sheaf-of-modules.             |
| résolution injective                              | injective resolution                                    | Standard.                                                                 |
| augmentation canonique                            | canonical augmentation                                  | Standard.                                                                 |
| homotopes à zéro                                  | homotopic to zero                                       | Standard.                                                                 |
| accouplement                                      | pairing                                                 | Standard.                                                                 |
| théorème des syzygies                             | syzygy theorem                                          | Hilbert's syzygy theorem.                                                 |
| théorème de Cohen                                 | Cohen's theorem                                         | Structure theorem for complete local rings.                               |
| dimension homologique globale                     | global homological dimension                            | Standard.                                                                 |
| système de paramètres                             | system of parameters                                    | Standard.                                                                 |
| composantes irréductibles                         | irreducible components                                  | Standard.                                                                 |
| point générique                                   | generic point                                           | Standard.                                                                 |
| morphisme déduit de $f$ par passage aux complétés | morphism deduced from $f$ by passing to the completions | Standard SGA proof movement.                                              |
| idéal de définition                               | ideal of definition                                     | Standard.                                                                 |
| $I'$-bonne (filtration)                           | $I'$-good (filtration)                                  | EGA terminology for "good filtration".                                    |
| morphisme adique                                  | adic morphism                                           | Standard EGA term.                                                        |
| condition de Mittag-Leffler uniforme              | uniform Mittag-Leffler condition                        | Standard.                                                                 |
| préschéma formel                                  | formal prescheme                                        | Standard.                                                                 |
| anneau noethérien adique                          | noetherian adic ring                                    | Standard.                                                                 |
| séparé et complet pour la topologie $I$-adique    | separated and complete for the $I$-adic topology        | Standard.                                                                 |
| anneau gradué associé $gr_{I}$                    | associated graded ring $gr_{I}$                         | Standard.                                                                 |
| Module inversible                                 | invertible Module                                       | Capital preserved per source.                                             |
| pleinement fidèle                                 | fully faithful                                          | Standard.                                                                 |
| factoriel / factoriel en codimension $\geq k$     | factorial / factorial in codimension $\geq k$           | Standard (unique factorization).                                          |
| critère de normalité de Serre                     | Serre's criterion of normality                          | Standard.                                                                 |
| diviseur principal / localement principal         | principal / locally principal divisor                   | Standard.                                                                 |
| diviseur de Cartier                               | Cartier divisor                                         | Standard.                                                                 |
| anneau de valuation discrète                      | discrete valuation ring                                 | Standard.                                                                 |
| résolution libre finie                            | finite free resolution                                  | Standard.                                                                 |
| dimension cohomologique                           | cohomological dimension                                 | Standard.                                                                 |
| dimension projective (`dp`)                       | projective dimension (`dp`)                             | Auslander–Buchsbaum formula context.                                      |
| base de filtre                                    | filter base                                             | "Decreasing filtered family" per N.D.E.                                   |
| algébrisable                                      | algebraizable                                           | Standard formal-geometry term.                                            |
| Hauptidealsatz                                    | Hauptidealsatz                                          | Krull's principal-ideal theorem; kept untranslated.                       |
| canularesque (Grothendieck slang)                 | farcical / a farce                                      | From `canular` (hoax). Preserves the joking register.                     |
| Je dis que                                        | I claim that                                            | Preserves the first-person move.                                          |
| "point-base"                                      | "base-point"                                            | In quotation marks.                                                       |

## Style anchors (style is non-negotiable for cross-volume consistency)

These are inherited from SGA 1's translation; deviate only if SGA 1 itself is inconsistent.

- **File naming.** `00-title-preface.md`, `00-introduction.md`, `NN-<slug>.md` for Exposés, `glossary.md`,
  `zz-index-*.md` for indexes.
- **Heading hierarchy.** `# Exposé N. <English Title>`, then `## 1. <Section Title>`, then `### <Subsection>` if needed.
  The Exposé heading carries a `<!-- label: N -->` comment on the next line.
- **Statement blocks.** `**Proposition.**`, `**Lemma.**`, `**Theorem.**`, `**Corollary.**`, `**Definition.**`,
  `**Remark.**`, `**Example.**` on their own line. The label `<!-- label: N.X.Y -->` follows on the next line (after a
  blank line). The body begins after another blank line.
- **Math.** Unicode math wrapped in backticks for inline. Displayed math in fenced ```` ```text ```` blocks. Numbered
  displayed equations get a `<!-- label: eq:N.X.Y -->` comment immediately after the closing fence.
- **Footnotes.** Markdown `[^slug]` syntax. The footnote body goes at the end of the section (or end of file). Original
  Grothendieck-era footnotes: `[^<exposenum>-<sec>-<n>]` slugs (e.g. `[^I-1-1]`). Editor footnotes:
  `[^N.D.E-<expose>-<n>]` (e.g. `[^N.D.E-IV-2]`).
- **Page marks.** `<!-- original page N -->` on its own line at page boundaries.
- **Cross-references.** Use the source's own convention: `(VIII 2.3)`, `(EGA III 4.1.5)`, `(SGA 4 IV 3.8)`.
- **Bibliographies.** Each Exposé's own bibliography section, at its end, is preserved as a `## Bibliography` section
  with entries as a numbered list, journal titles in italics, with the original keys (e.g. `[1]`, `[2]`) preserved as
  leading bracketed labels.
