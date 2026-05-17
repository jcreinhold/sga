# SGA 2: Local Cohomology of Coherent Sheaves and Local and Global Lefschetz Theorems

*Séminaire de Géométrie Algébrique du Bois-Marie*, 1962.

A. Grothendieck (with collaborators I. Giorgiutti, J. Giraud, M. Hakim *née* Jaffe, A. Laudal). Augmented by Exposé XIV
of Mme Michèle Raynaud (1967). Revised reprint, IHÉS, Bures-sur-Yvette, April 1968. Modern LaTeX edition by Yves Laszlo
*et al.* (2005).

## Abstract

This volume develops the theory of local cohomology of coherent sheaves on noetherian schemes and applies it to prove
local and global theorems of Lefschetz type — for the fundamental group, the Picard group, and projective algebraic
schemes — through a systematic interplay between local results and global ones. Exposés I–II set up the formalism of
cohomology with supports `H^i_Y(X, F)`; III relates it to the classical notion of depth; IV–V develop local duality
and dualizing modules in the style later subsumed by Hartshorne's *Residues and Duality*; VI–VIII prove the central
finiteness theorem for `H^i_Y(F)`; IX uses it to obtain comparison and existence theorems in formal geometry, parallel
to those of EGA III for proper morphisms; X–XII apply these to Lefschetz-type theorems for `π₁`, `Pic`, and projective
schemes; XIII surveys open problems; and Raynaud's XIV recasts the Lefschetz theorems in étale cohomology, drawing on
SGA 4 and SGA 5.

## Reading order

Files are numbered so alphanumeric order matches reading order.

- [Title page, preface (Laszlo), and table of contents](00-title-preface.md)
- [Introduction (Grothendieck, 1968)](00-introduction.md)
- [Exposé I — Global and local cohomological invariants with respect to a closed subspace](01-invariants-cohomologiques.md)
- [Exposé II — Application to quasi-coherent sheaves on preschemes](02-faisceaux-quasi-coherents.md)
- [Exposé III — Cohomological invariants and depth](03-invariants-cohomologiques-et-profondeur.md)
- [Exposé IV — Dualizing modules and dualizing functors](04-modules-et-foncteurs-dualisants.md)
- [Exposé V — Local duality and the structure of the `H^i(M)`](05-dualite-locale-et-structure-des-Hi.md)
- [Exposé VI — The functors `Ext^•_Z(X; F, G)` and `Ext^•_Z(F, G)`](06-foncteurs-Ext.md)
- [Exposé VII — Vanishing criteria and coherence conditions for the sheaves `Ext^i_Y(F, G)`](07-criteres-de-nullite-coherence.md)
- [Exposé VIII — The finiteness theorem](08-theoreme-de-finitude.md)
- [Exposé IX — Algebraic geometry and formal geometry](09-geometrie-algebrique-et-formelle.md)
- [Exposé X — Application to the fundamental group](10-application-au-groupe-fondamental.md)
- [Exposé XI — Application to the Picard group](11-application-au-groupe-de-picard.md)
- [Exposé XII — Applications to projective algebraic schemes](12-schemas-algebriques-projectifs.md)
- [Exposé XIII — Problems and conjectures](13-problemes-et-conjectures.md)
- [Exposé XIV — Depth and Lefschetz theorems in étale cohomology (Raynaud)](14-profondeur-lefschetz-cohomologie-etale.md)
- [Index of notation](zz-index-notations.md)
- [Terminological index](zz-index-terminologique.md)
- [Translation glossary](glossary.md)

## Reference convention

Following the source, SGA 2 is cited as `(Exp. N, M.K)` where `N` is the Exposé Roman numeral and `M.K` is the decimal
numbering inside that Exposé — for example `(VIII, 2.3)` for Théorème 2.3 of Exposé VIII. The 1968 revised reprint
introduced a uniform decimal numbering across Exposés III–VIII; the original 1962 numbering is occasionally preserved
with the adverb *bis* where collisions occurred. Cross-references to other SGA volumes follow the same source
conventions (e.g. `SGA 4 IV 3.8`).

## Editorial conventions

- **Terminology**. Exposés I–XIII keep the historical SGA/EGA distinction between *prescheme* (`préschéma`) and
    *scheme* (`schéma`, in the older sense of separated prescheme). Exposé XIV, added in 1967 by Raynaud, explicitly
    adopts the modern usage in which *scheme* means what was previously called *prescheme*, and *separated scheme*
    means what was previously called *scheme*; her opening footnote announces this. The translation honors that
    per-Exposé split; a translator note at the head of Exposé XIV recalls it.

- **Editor footnotes (N.D.E.)**. The 2005 LaTeX edition by Yves Laszlo *et al.* added footnotes (*Notes de l'éditeur*,
    abbreviated *N.D.E.*) recording corrections, updates, and the current status of questions raised in the original.
    In this translation, original Grothendieck-era footnotes use slugs like `[^I-3-1]`, while editor footnotes use
    `[^N.D.E-IV-2]` so the two are visibly distinct.

- **Page marks**. HTML comments `<!-- original page N -->` mark the start of page `N` in the 1968 IHÉS edition, whose
    pagination is preserved in the margin of the modern LaTeX edition.

- **Mathematics**. Mathematics is written with Unicode and wrapped in backticks where formatter mangling is a risk.
    Displayed equations use fenced ```` ```text ```` blocks, optionally pinned with `<!-- label: eq:N.X.Y -->`.

- **The `ΓZ` / `Γ_Z` distinction**. SGA 2 systematically uses an underlined `ΓZ` for the *sheafified* version of the
    sections-with-support functor and a non-underlined `Γ_Z` for the global-section version. The translation preserves
    this; where the source OCR has lost the underline, the surrounding French reveals which functor is meant. A small
    typographic note at first use in each Exposé fixes the convention there.

## Provenance

This is a translation, not a critical edition. The authoritative text remains the French 2005 LaTeX edition
(`~/Code/papers/books/sga/ii/`, derived from the IHÉS/North-Holland 1968 reprint as recomposed by Y. Laszlo). For any
claim that matters mathematically, consult the source: this English version exists to make the volume readable, not to
replace it.
