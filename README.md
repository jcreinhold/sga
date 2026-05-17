# SGA — English translation

An idiomatic English translation, in Markdown with Unicode mathematics, of the Grothendieck-era *Séminaires de Géométrie
Algébrique du Bois-Marie*.

> **Note.** This translation was produced with substantial assistance from large language models, then curated and
> edited by the maintainer. It has not been audited line-by-line by a working algebraic geometer. Treat it as a
> reading aid: verify against the French source for anything that matters mathematically.

## Volumes

- [`i/`](i) — SGA 1: Étale Coverings and the Fundamental Group (Grothendieck, with Raynaud)
- [`ii/`](ii) — SGA 2: Cohomologie locale des faisceaux cohérents et théorèmes de Lefschetz locaux et globaux
- [`iii/`](iii) — SGA 3: Schémas en Groupes (Demazure–Grothendieck)

Each volume directory has its own `README.md` with status, exposé index, and translation notes.

## Translation principles

- Preserve original numbering of Exposés, sections, and statements.
- Keep technical terms close to community-standard English (étale, scheme, descent); inline a brief definition the first
    time a term appears in an exposé.
- Mark original page transitions inline as HTML comments where helpful.
- Revise prose for English mathematical idiom while preserving the seminar voice of the originals.

## Sources

The French source text was drawn from the Grothendieck Circle's archive of Grothendieck's published writings:
<https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/pubtexts.php>. LaTeX community editions (where they
exist) were cross-referenced for technical accuracy.

## Related projects

- The French LaTeX re-typesettings of the SGA volumes — most notably Bas Edixhoven's volunteer SGA 1 LaTeX project, the
    2005 SMF *Documents Mathématiques* edition of SGA 2 edited by Y. Laszlo et al., and the 2011 SMF re-edition of
    SGA 3 edited by M. Demazure — were cross-referenced as authoritative French source text.
- [The Stacks Project](https://stacks.math.columbia.edu/) — an open-source modernized algebraic geometry reference that
    covers much of the SGA material (étale cohomology, descent, fundamental groups, group schemes) in contemporary
    language, with permanently linkable tags.
