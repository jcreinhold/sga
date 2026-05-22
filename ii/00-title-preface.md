# SGA 2: Local Cohomology of Coherent Sheaves and Local and Global Lefschetz Theorems

*Séminaire de Géométrie Algébrique du Bois-Marie*, 1962.

A seminar directed by Alexander Grothendieck (compiled by a group of auditors), augmented by an Exposé of Mme Michèle
Raynaud.

A new updated edition of volume 2 of the *Advanced Studies in Pure Mathematics*, published in 1968 by North-Holland
Publishing Company.

## Preface

<!-- label: II.preface -->

The present text is a new updated edition of the book *Cohomologie locale des faisceaux cohérents et théorèmes de
Lefschetz locaux et globaux* (SGA 2), Advanced Studies in Pure Mathematics 2, North-Holland Publishing Company,
Amsterdam, 1968, by A. Grothendieck *et al.* It is the second part of the SGA project initiated by B. Edixhoven, who
prepared a new edition of SGA 1. This version is meant to reproduce the original text, with some modifications,
including minor typographical corrections and footnotes from the editor (*N.D.E.*) explaining the current status of
questions raised in the first edition. Some additional detail has also been given for certain proofs. To avoid possible
confusion, the original footnotes are numbered using stars, while the new ones are numbered using integers. The page
numbers of the original version are written in the margin of the text.

Let me thank the mathematicians who carried out most of the initial typesetting in LATEX 2e, namely L. Bayle, N. Borne,
O. Brinon, J. Buresi, M. Chardin, F. Ducrot, P. Graftiaux, F. Han, P. Karwasz, L. Koelblen, D. Madore, S. Morel, D.
Naie, B. Osserman, J. Riou, and V. Sécherre, and also C. Sabbah for adapting this text to the SMF layout. Let me also
thank J.-B. Bost, P. Colmez, O. Gabber, W. Fulton, S. Kleiman, F. Orgogozo, M. Raynaud, and J.-P. Serre for their
comments and advice.

The editor, Yves Laszlo.

<!-- TRANSLATOR NOTE: Laszlo's own English preface in the source PDF has been adopted here with only light
copy-editing for consistency with the SGA 1 translation. The French original of the preface (also in the source PDF)
is the authoritative version; this text matches it. -->

## Table of contents

<!-- label: II.toc -->

Introduction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . . . . . . . . . . . . . 1

- **I.** Global and local cohomological invariants with respect to a closed subspace . . . . . . . . . . . . . . . . . .
  . . . 5

    1. The functors $\Gamma_{Z}$, $\Gamma Z$ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . . . . . 5
    1. The functors $H^{\bullet}_{Z}(X, F)$ and $\mathcal{H}^{\bullet}_{Z}(F)$ . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . . . . . . . . 10
    1. Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . 14

- **II.** Application to quasi-coherent sheaves on preschemes . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . . . . . . . . . 15

- **III.** Cohomological invariants and depth . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . . . . . . . . . . . 21

    1. Review . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . . . . 21
    1. Depth . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . . . 22
    1. Depth and topological properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . 26

- **IV.** Dualizing modules and dualizing functors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . . . . . . . . . 33

    1. Generalities on module functors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . 33
    1. Characterization of exact functors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . 36
    1. Study of the case where $T$ is left exact and $T(M)$ is of finite type for every $M$ . . . . . . . . . . . 37
    1. Dualizing module; dualizing functor . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . 39
    1. Consequences of the theory of dualizing modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       43

- **V.** Local duality and structure of the $H^{i}(M)$ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . . . . . . . . . . . 47

    1. Complexes of homomorphisms . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . 47
    1. The local duality theorem for a regular local ring . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . 50
    1. Application to the structure of the $H^{i}(M)$ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . 50

- **VI.** The functors $Ext^{\bullet}_{Z}(X; F, G)$ and $Ext^{\bullet}_{Z}(F, G)$ . . . . . . . . . . . . . . . . . . .
  . . . . . . . . . . . . . . . . . . 57

    1. Generalities . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . . . 57
    1. Applications to quasi-coherent sheaves on preschemes . . . . . . . . . . . . . . . . . . . . . . . . . . . . 59
    1. Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . 60

- **VII.** Vanishing criteria and coherence conditions for the sheaves $Ext^{i}_{Y}(F, G)$ . . . . . . . . . . . . . . .
  . . . . 61

    1. Study for $i < n$ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . 61
    1. Study for $i > n$ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . 64

- **VIII.** The finiteness theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . . . . . . . . . . . . . . 67

    1. A biduality spectral sequence . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . 67
    1. The finiteness theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . 70
    1. Applications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . . 76
    1. Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . . 77

- **IX.** Algebraic geometry and formal geometry . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . . . . . . . 79

    1. The comparison theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . 79
    1. The existence theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . 85

- **X.** Application to the fundamental group . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . . . . . . . . . . 89

    1. Comparison of $\hat{E}t(\hat{X})$ and $\hat{E}t(Y)$ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . . . . 89
    1. Comparison of $\hat{E}t(Y)$ and $\hat{E}t(U)$, for $U$ variable . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . 89
    1. Comparison of $\pi_{1}(X)$ and $\pi_{1}(U)$ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . 94

- **XI.** Application to the Picard group . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . . . . . . . . . . . 99

    1. Comparison of $\operatorname{Pic}(\hat{X})$ and $\operatorname{Pic}(Y)$ . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . . . . . . . . . . . . 99
    1. Comparison of $\operatorname{Pic}(X)$ and $\operatorname{Pic}(\hat{X})$ . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . . . . . . . . . . . 100
    1. Comparison of $P(X)$ and $P(U)$ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . 101

- **XII.** Applications to projective algebraic schemes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . . . . . . 109

    1. Projective duality theorem and finiteness theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       109
    1. Lefschetz theory for a projective morphism: Grauert's comparison theorem . . . . . . . . . . . 114
    1. Lefschetz theory for a projective morphism: existence theorem . . . . . . . . . . . . . . . . . . . . . 117
    1. Formal completion and normal flatness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . 122
    1. Universal finiteness conditions for a non-proper morphism . . . . . . . . . . . . . . . . . . . . . . . . 128

- **XIII.** Problems and conjectures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . . . . . . . . . . 135

    1. Relations between global and local results. Affine problems related to duality . . . . . . . . 135
    1. Problems related to $\pi_{0}$: local Bertini theorems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . 139
    1. Problems related to $\pi_{1}$ . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . 143
    1. Problems related to higher $\pi_{i}$: local and global Lefschetz theorems for complex analytic spaces . . . 144
    1. Problems related to local Picard groups . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . 148
    1. Comments . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . . 151
    1. Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . 158

- **XIV.** Depth and Lefschetz theorems in étale cohomology . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . 159

    1. Cohomological and homotopical depth . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . 159
    1. Technical lemmas . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . 177
    1. Converse of the affine Lefschetz theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . 181
    1. Main theorem and variants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . 187
    1. Geometrical depth . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . 198
    1. Open questions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . 202
    1. Bibliography . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
       . . . . . . . . . . . . 204

- Index of notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . . . . . . . . . . . . . . 205

- Terminological index . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
  . . . . . . . . . . . . 207
