# Exposé XXVI. Parabolic subgroups of reductive groups

<!-- label: III.XXVI -->

*by M. Demazure*

<!-- original page 281 -->

[^N.D.E-XXVI-0]

This Exposé studies the parabolic subgroups of an `S`-reductive group `G`. Its essential result is the conjugacy
theorem (5.4). The essential tool is the notion of *transversal position* of two parabolic subgroups, a notion studied
systematically in §4. Another fact plays an important role: the decomposition of the unipotent radical `rad^u(P)` of a
parabolic subgroup `P` as successive extensions of vector groups (2.1)[^N.D.E-XXVI-1].

Various schemes associated with `G` are studied in §3; §6 deals with the split subtori[^N.D.E-XXVI-2] of `G` and their
relations with parabolic subgroups.

Finally, in §7, we briefly expound how, over a semi-local base, one formulates the "relative theory" of reductive groups
as presented over fields in the article of A. Borel and J. Tits, *Groupes réductifs*, Publications Mathématiques de
l'IHÉS, no. 27. In that article, cited [BT65] in what follows, the reader will moreover find, in the case of a base
field, other results that have not been touched on here.

## 1. Recollections. Levi subgroups

<!-- label: III.XXVI.1 -->

**Definition 1.1.** *Let `S` be a scheme, `G` an `S`-reductive group, `P` a sub-`S`-group-scheme of `G`. One says that
`P` is a* parabolic subgroup *of `G` if*

*(i) `P` is smooth over `S`,*

<!-- original page 282 -->

*(ii) for each `s ∈ S`, the `s`-quotient-scheme `G_s/P_s` is proper (i.e. Bible, §6.4, Th. 4 (= [Ch05], §6.5, Th. 5),
`P_s` contains a Borel subgroup of `G_s`).*

<!-- label: III.XXVI.1.1 -->

**Proposition 1.2** (Exp. XXII, 5.8.5). *Let `S` be a scheme, `G` an `S`-reductive group, `P` a parabolic subgroup of
`G`. Then `P` is closed in `G`, with connected fibers, and*

```text
P = Norm_G(P).
```

*Moreover, the quotient sheaf `G/P` is representable by an `S`-scheme that is smooth and projective over `S`.*

<!-- label: III.XXVI.1.2 -->

**Proposition 1.3** (Exp. XXII, 5.3.9 and 5.3.11). *Let `S` be a scheme, `G` an `S`-reductive group, `P` and `P'` two
parabolic subgroups of `G`. The following conditions are equivalent:*

*(i) `P` and `P'` are conjugate in `G`, locally for the étale (resp. (fpqc)) topology.*

*(ii) For each `s ∈ S`, `P_s` and `P_s'` are conjugate by an element of `G(s)`.*

*(iii) The strict transporter `Transt_G(P, P')` of `P` into `P'` (defined by*

```text
Transt_G(P, P')(S') = { g ∈ G(S') | int(g) P_{S'} = P'_{S'} }
```

*for every `S' → S`) is a closed subscheme of `G`, smooth and of finite presentation over `S`, which is a principal
homogeneous bundle on the right under `P` and on the left under `P'`.*

<!-- label: III.XXVI.1.3 -->

**Proposition 1.4.** *Let `S` be a nonempty scheme, `(G, T, M, R)` an `S`-split reductive group, `R'` a subset of `R`.
The following conditions on `R'` are equivalent:*

<!-- original page 428 -->

*(i) `g_{R'} = t ⊕ ⨁_{α ∈ R'} g^α` is the Lie algebra of a parabolic subgroup of `G` containing `T` (necessarily unique,
Exp. XXII, 5.3.5).*

*(ii) `R'` is of type (R) (Exp. XXII, 5.4.2) and contains a system of positive roots.*

*(iii) `R'` is a closed subset of `R` and satisfies: if `α ∈ R − R'`, then `−α ∈ R'` (that is, `R = R' ∪ (−R')`).*

*(iv) There exist a system of simple roots `Δ`, and a subset `A` of `Δ` such that `R'` is the union of the set of
positive roots and the set of negative roots that are linear combinations of the elements of `A`.*

*(v) `R'` contains a system of simple roots of `R`; moreover, if `Δ ⊂ R'` is a system of simple roots of `R` and one
sets*

```text
A = (−R') ∩ Δ,
```

*then `R'` is the union of the set of positive roots and the set of negative roots that are linear combinations of the
elements of `A`.*

<!-- label: III.XXVI.1.4 -->

One has (i) ⇔ (ii) by Exp. XXII, 5.4.5 (ii) and 5.5.1. One has (iii) ⇒ (ii) by Exp. XXI, 3.3.6 and Exp. XXII, 5.4.7. One
trivially has (v) ⇒ (iv) ⇒ (iii). One has (iii) ⇒ (v) by Exp. XXI, 3.3.6 and 3.3.10.

It therefore remains to prove that (i) implies that `R'` is a closed subset of `R`. But this last assertion can be
verified on any geometric fiber; one may therefore assume that `S` is the spectrum of an algebraically closed field.

Let `P` be the parabolic subgroup of `G` containing `T` whose Lie algebra is `g_{R'}`. Since the Borel subgroups of `P`
are the Borel subgroups of `G` contained in `P`, it follows from Bible, §12.3, Th. 1, and from Exp. XXII, 5.4.5 (i),
that if one denotes by `U` the unipotent radical of `P`, then `T · U` is the subgroup of `G` containing `T` whose Lie
algebra is

```text
g_{R''} = t ⊕ ⨁_{α ∈ R''} g^α,
```

<!-- original page 429 -->

where `R''` is the intersection of the systems of positive roots of `R` contained in `R'`. In particular, it follows
that `R''` is closed and that `R'' ∩ (−R'') = ∅`. On the other hand, the group `H = P/U` is reductive, the canonical
image `T̄` of `T` is a maximal torus of it (`T → T̄` is an isomorphism), and one has an isomorphism of `T̄`-modules, i.e.
of `M`-graded vector spaces,

```text
Lie(H) ≃ t ⊕ ⨁_{α ∈ R_s} g^α,
```

where `R_s` is the complement of `R''` in `R'`. It follows that `R_s` is naturally identified with the set of roots of
`H` relative to `T̄`, and in particular satisfies `R_s = −R_s`. One immediately deduces that

```text
R'' = { α ∈ R' | −α ∉ R' },        R_s = { α ∈ R' | −α ∈ R' }.
```

Let us now show that `R'` is closed. Let `α, β ∈ R'` such that `α + β ∈ R`; let us prove that `α + β ∈ R'`. If
`α, β ∈ R''`, then `α + β ∈ R''` because `R''` is closed. If `α ∈ R_s`, `β ∈ R''`, and if `α + β ∉ R'`, then
`α + β ∈ −R''`, and one has `−α = −(α + β) + β ∈ R''` because `R''` is closed, which entails `−α ∈ R'' ∩ R_s` and
contradicts the fact that `R_s ∩ R'' = ∅`. It therefore remains to study the case where `α, β ∈ R_s`. If
`α + β ∉ R'`, then `α + β ∈ −R''`. But, as `α + β ≠ 0`, there exists a system of positive roots of the root system
`R_s` containing `α` and `β`, hence a Borel subgroup of `H = P/U` containing the canonical image of `U_α` and `U_β`.
Its inverse image in `P` is a Borel subgroup containing `U_α`, `U_β` and `U`, hence `U_α`, `U_β` and `U_{−(α+β)}`, which
is impossible.

**Corollary 1.5.** *A parabolic subgroup of a reductive group is of type (RC) (Exp. XXII, 5.11.1).*

<!-- original page 430 -->

<!-- label: III.XXVI.1.5 -->

**Proposition 1.6** (Exp. XXII, 5.11.4). *Let `S` be a scheme, `G` an `S`-reductive group, `P` a subgroup of `G` of type
(RC)*[^N.D.E-XXVI-3].

*(i) `P` possesses a largest invariant sub-group-scheme that is smooth and of finite presentation over `S`, with
connected unipotent geometric fibers. It is a characteristic subgroup of `P`, called the* unipotent radical *of `P`,
denoted `rad^u(P)`. The quotient sheaf `P/rad^u(P)` is representable by an `S`-reductive group.*

*(ii) If `T` is a maximal torus of `P`, `P` possesses a reductive subgroup `L` containing `T` such that:*

   *(a) Every reductive subgroup of `P` containing `T` is contained in `L`.*

   *(b) `P` is the semidirect product `L · rad^u(P)`, i.e. the canonical morphism `L → P/rad^u(P)` is an isomorphism.*

*Moreover, `L` is the unique subgroup (resp. reductive subgroup) of `P` containing `T` and satisfying (b) (resp. (a)).
Finally, one has*

```text
Norm_P(L) = L,        Norm_P(T) = Norm_L(T).
```

<!-- label: III.XXVI.1.6 -->

### 1.7.

<!-- label: III.XXVI.1.7 -->

A subgroup `L` of `P` satisfying condition (b) above is called a *Levi subgroup* of `P`. It is a maximal reductive
subgroup of `P`; indeed, it is reductive, since isomorphic to `P/rad^u(P)`. Let us show that it is maximal for this
property. Let `L'` be a reductive subgroup of `P` containing `L`; to prove that `L' = L`, one may reason locally for the
(fpqc) topology, and hence assume that `L` has a maximal torus `T`, and one is reduced to 1.6 (ii).

<!-- original page 431 -->

If `L` and `L'` are two Levi subgroups of `P`, then `L` and `L'` are conjugate in `P`, locally for the (fpqc) topology.
Indeed, locally for this topology, one may assume that `L` (resp. `L'`) has a maximal torus `T` (resp. `T'`); since `T`
and `T'` are conjugate in `P` locally for the (fpqc) topology, one may assume `T = T'`, and one then has `L = L'`, by
1.6 (ii). But since `P = L · rad^u(P)` and `Norm_P(L) = L`, one immediately deduces:

**Corollary 1.8.** *Let `P` be a subgroup of type (RC)[^N.D.E-XXVI-4] of the `S`-reductive group `G`. If `L` and `L'`
are two Levi subgroups of `P`, there exists a unique `u ∈ rad^u(P)(S)` such that `int(u) L = L'`.*

<!-- label: III.XXVI.1.8 -->

Let us denote by `Lev(P)` the functor of Levi subgroups of `P`: for `S' → S`, `Lev(P)(S')` is the set of Levi subgroups
of `P_{S'}`. From 1.8 one deduces:

**Corollary 1.9.** *Let `P` be a subgroup of type (RC)[^N.D.E-XXVI-4] of the `S`-reductive group `G`. Then `Lev(P)` is a
principal homogeneous bundle under the `S`-group `rad^u(P)`, and in particular is representable by an `S`-scheme that
is smooth and affine over `S`, with integral geometric fibers.*

<!-- label: III.XXVI.1.9 -->

It follows immediately from 1.6:

**Corollary 1.10.** *Let `P` be a subgroup of type (RC)[^N.D.E-XXVI-4] of the `S`-reductive group `G`. The functor
`Tor(P)` of maximal tori of `P` is representable by an `S`-scheme that is smooth and affine, the "relation `L ⊃ T`"
defines a morphism*

```text
Tor(P) ⟶ Lev(P),
```

*the fiber of which over `L ∈ Lev(P)(S)` is identified with `Tor(L)` (Exp. XXII, 5.8.3).*

<!-- label: III.XXVI.1.10 -->

The first assertion of 1.10 is a consequence of the other two and of Exp. XXII, 5.8.3.

<!-- original page 432 -->

**Definition 1.11.** *Let `S` be a nonempty scheme, `G` an `S`-reductive group, `P` a parabolic subgroup of `G`,
`E = (T, M, R, Δ, (X_α)_{α ∈ Δ})` a pinning of `G`. One says that `E` is* adapted *to `P`, or that `E` is a* pinning of
the pair `(G, P)`, *if `P ⊃ T` and if the Lie algebra of `P` is of the form `t ⊕ ⨁_{α ∈ R'} g^α`, where `R'` is a
subset of `R` containing `R^+`.*

<!-- label: III.XXVI.1.11 -->

In particular, if `T ⊂ B` is the Killing pair defined by the pinning, one has `T ⊂ B ⊂ P`.

Under the preceding conditions, one sets `Δ(P) = Δ ∩ (−R')`; then, by Exp. XXII, 5.4.3, one has:

```text
α ∈ Δ(P)  ⇔  α ∈ Δ and U_{−α} ⊂ P  ⇔  α ∈ Δ and U_{−α} ∩ P ≠ e.
```

It follows immediately from 1.4 (v) and Exp. XXII, 5.11.3 and 5.10.6:

**Proposition 1.12.** *Let `S` be a scheme, `G` an `S`-reductive group, `P` a parabolic subgroup of `G`,
`(T, M, R, Δ, (X_α)_{α ∈ Δ})` a pinning of `G` adapted to `P`, `Δ(P)` the subset of `Δ` defined above.*

*(i) The unipotent radical `rad^u(P)` of `P` is none other than*

```text
U_{R''} = ∏_{α ∈ R''} U_α,
```

*where `R''` is the set of positive roots that, in their decomposition along `Δ`, involve at least one element of
`Δ − Δ(P)`[^N.D.E-XXVI-5] with a nonzero coefficient.*

*(ii) The unique Levi subgroup `L` of `P` containing `T` is none other than*

```text
Z_{Δ(P)} = Centr_G(T_{Δ(P)}),
```

*where `T_{Δ(P)}` is the maximal torus of `⋂_{α ∈ Δ(P)} Ker(α)`; moreover, one has `T_{Δ(P)} = rad(L)`.*

<!-- label: III.XXVI.1.12 -->

**Corollary 1.13.** *Every Levi subgroup `L` of the parabolic subgroup `P` of the reductive group `G` is a* critical
subgroup *of `G`, i.e. satisfies (Exp. XXII, 5.10.4):*

```text
L = Centr_G(rad(L)).
```

<!-- original page 433 -->

<!-- label: III.XXVI.1.13 -->

This follows immediately from 1.12 and from the following lemma, which is contained in 1.4 and Exp. XXII, 5.4.1:

**Lemma 1.14.** *Locally for the étale topology, every pair `(G, P)`, where `P` is a parabolic subgroup of the reductive
group `G`, may be pinned (1.11).*

<!-- label: III.XXVI.1.14 -->

Let us note:

**Proposition 1.15.** *Let `S` be a scheme, `G` an `S`-reductive group, `P` a parabolic subgroup of `G`, `E` and `E'`
two pinnings of `G` adapted to `P`. The unique inner automorphism of `G` over `S` that transforms `E` into `E'`
(Exp. XXIV, 1.5) comes from `P`, via the morphism*

```text
P ⟶ P/Centr(P) = P/Centr(G) ⟶ G/Centr(G).
```

<!-- label: III.XXVI.1.15 -->

Indeed, it suffices to reason as in Exp. XXIV, 1.5, using:

**Lemma 1.16** (Exp. XXII, 5.3.14 and 5.2.6). *The maximal tori (resp. Borel subgroups, resp. Killing pairs) of a
parabolic subgroup `P` of the `S`-reductive group `G` are conjugate in `P`, locally for the étale topology.*

<!-- label: III.XXVI.1.16 -->

**Proposition 1.17.** *Let `S` be a scheme, `G` an `S`-reductive group, `P` and `P'` two parabolic subgroups of `G`,
`B` a Borel subgroup contained in `P` and `P'`. If `P` and `P'` are conjugate in `G` locally for the étale topology,
then `P = P'`.*

<!-- label: III.XXVI.1.17 -->

<!-- original page 434 -->

Indeed, one may assume that there exists `g ∈ G(S)` such that `int(g) P = P'`. Then `B` and `int(g)^{-1} B` are two
Borel subgroups of `P`. Possibly after extending `S`, by 1.16 one may assume that there exists `p ∈ P(S)` such that
`int(p) int(g^{-1}) B = B`. Then

```text
p g^{-1} ∈ Norm_G(B)(S) = B(S),
```

and `g ∈ B(S) · p ⊂ P(S)`, hence `P' = int(g) P = P`.

**Remark 1.18.** *If `P` and `P'` are two parabolic subgroups of `G` containing a common Borel subgroup, then `P ∩ P'`
is again a parabolic subgroup of `G`. Indeed, it is smooth along the unit section (Exp. XXII, 5.4.5), and it contains a
Borel subgroup.*

<!-- label: III.XXVI.1.18 -->

**Proposition 1.19.** *Let `S` be a scheme, `G` an `S`-reductive group, `G'` its derived group (Exp. XXII, 6.2.1).*

*(i) The maps*

```text
P ↦ P' = P ∩ G'    and    P ↦ P' · rad(G) = Norm_G(P')
```

*are mutually inverse bijections between the set of parabolic subgroups of `G` and the set of parabolic subgroups of
`G'`. One has `rad^u(P) = rad^u(P')`.*

*(ii) Let `P` be a parabolic subgroup of `G` and `P' = P ∩ G'`. The maps*

```text
L ↦ L' = L ∩ G' = L ∩ P'
L' ↦ L' · rad(G) = Centr_G(rad(L'))
```

*are mutually inverse bijections between the set of Levi subgroups of `P` and the set of Levi subgroups of `P'`.
Moreover, one has `rad(L') = (rad(L) ∩ G')^0`.*

<!-- label: III.XXVI.1.19 -->

<!-- original page 435 -->

The proof (by reduction to the split case, for example) is straightforward and is left to the reader, together with
that, immediate, of:

**Proposition 1.20.** *Let `S` be a scheme, `G` an `S`-reductive group, `P` a parabolic subgroup of `G`, `L` a Levi
subgroup of `P`. The maps*

```text
Q ↦ Q ∩ L = Q',     Q' ↦ Q' · rad^u(P)
```

*are mutually inverse bijections between the set of parabolic subgroups of `G` contained in `P` and the set of parabolic
subgroups of `L`. Moreover, the Levi subgroups of `Q'` are the Levi subgroups of `Q` contained in `L`.*

<!-- label: III.XXVI.1.20 -->

One may complete 1.6 as follows:

**Proposition 1.21.** *Let `S` be a scheme, `G` an `S`-reductive group, `P` a parabolic subgroup of `G`.*

*(i) `P` possesses a largest invariant subgroup that is smooth and of finite presentation over `S`, with connected
solvable geometric fibers. It is a characteristic subgroup of `P`, called the* radical *of `P`, and denoted `rad(P)`.
The quotient sheaf `P/rad(P)` is representable by an `S`-semisimple group.*

*(ii) If `L` is a Levi subgroup of `P`, `rad(P)` is the semidirect product of `rad^u(P)` and `rad(L)`; one has
`rad(L) = L ∩ rad(P)`, hence `L = Centr_G(L ∩ rad(P))`, and `P/rad(P) ≃ L/rad(L)`.*

<!-- label: III.XXVI.1.21 -->

Indeed, assertion (i) being local, one may assume that `G` has a Levi subgroup `L`, and one is reduced to proving that
`R = rad^u(P) · rad(L)` has the properties announced in (i), which is immediate. For (ii), it only remains to show that
`rad(L) = L ∩ rad(P)`, which follows immediately from the fact that `L ∩ rad(P)` is smooth and has connected fibers, `L`
being the centralizer of a torus[^N.D.E-XXVI-6].

<!-- original page 436 -->

## 2. Structure of the unipotent radical of a parabolic subgroup

<!-- label: III.XXVI.2 -->

**Proposition 2.1.** *Let `S` be a scheme, `G` an `S`-reductive group, `P` a parabolic subgroup of `G`, `rad^u(P)` its
unipotent radical. There exists a sequence of sub-group-schemes of `rad^u(P)`*

```text
rad^u(P) = U_0 ⊃ U_1 ⊃ U_2 ⊃ · · · ⊃ U_n ⊃ · · ·
```

*possessing the following properties:*

*(i) Each `U_i` is smooth, with connected fibers, characteristic and closed in `P`. The commutator of a section of `U_i`
and a section of `U_j` is a section of `U_{i+j+1}` (over a varying `S' → S`).*

*(ii) For each `i ⩾ 0`, there exists a locally free `O_S`-module `E_i` and an isomorphism of `S`-group sheaves*

```text
U_i / U_{i+1} ⥲ W(E_i).
```

*Moreover, the automorphisms of `P` (over a varying `S' → S`) act linearly on `W(E_i)`.*

*(iii) For every `s ∈ S`, one has `U_{n,s} = e` for `n > dim(rad^u(P)_s)`.*

<!-- label: III.XXVI.2.1 -->

### 2.1.1.

<!-- label: III.XXVI.2.1.1 -->

Suppose first that the pair `(G, P)` is pinnable. Let `(T, M, R, Δ, …)` be a pinning of `G` adapted to `P`; let `Δ(P)`
be the part of `Δ` defined by `P`. Let `α_1, …, α_p` be

<!-- original page 437 -->

the elements of `Δ(P)`, and `β_1, …, β_q` the elements of `Δ − Δ(P)`. Every root `γ ∈ R` is written uniquely as

```text
γ = a_1 α_1 + · · · + a_p α_p + b_1 β_1 + · · · + b_q β_q.
```

Set

```text
a(γ) = b_1 + · · · + b_q. [^N.D.E-XXVI-7]
```

It follows immediately from the definitions that the following properties hold (cf. 1.12):

(i) `U_γ ⊂ P ⇔ a(γ) ⩾ 0`.

(ii) `U_γ ⊂ rad^u(P) ⇔ a(γ) > 0`.

(iii) `a(n γ + m γ') = n a(γ) + m a(γ')` for all `n, m ∈ ℤ`.

For `i > 0`, let `R_i` be the set of roots `γ ∈ R` such that `a(γ) > i`. Each `R_i` is a closed set of roots satisfying
`R_i ∩ (−R_i) = ∅`. Consider (Exp. XXII, 5.6.5) the `S`-group

```text
U_i = U_{R_i} = ∏_{γ ∈ R_i} U_γ.
```

It is a closed sub-group-scheme of `G`, smooth over `S`, with connected fibers.

Let `α, β ∈ R`; consider the commutation relation of Exp. XXII, 5.5.2

```text
p_α(x) p_β(y) p_α(−x) = p_β(y) ∏_{n, m ∈ ℕ^*} p_{n α + m β}(C_{n, m, α, β} x^n y^m),
```

<!-- original page 438 -->

where each `p_γ` is an isomorphism of vector groups `G_{a, S} ⥲ U_γ`. Let us first remark that if `a(α) > i` and
`a(β) > j`, one has

```text
a(n α + m β) = n a(α) + m a(β) ⩾ n(i + 1) + m(j + 1) > i + j + 1
```

when `n` and `m` are `> 0`. It follows that the commutator of a section of `U_α` and a section of `U_β` is a section of
`U_{i+j+1}` (over a varying `S' → S`), which indeed entails `(U_i, U_j) ⊂ U_{i+j+1}`. For each `i ⩾ 0`, the quotient
`U_i / U_{i+1}` is therefore commutative; it is naturally identified with

```text
U_i / U_{i+1} ≃ ∏_{a(γ) = i+1} U_γ ≃ W(E_i),
```

where `E_i` is the direct sum of the `g^γ` for `a(γ) = i + 1`.

Let us return to the above commutation formula, and suppose `a(α) ⩾ 0`, `a(β) > i`. If `n, m ∈ ℕ^*`,

– either `a(n α + m β) > i + 1`,

– or `a(n α + m β) = i + 1`, in which case one necessarily has `m = 1`.

This proves first that `int(p_α(x))` respects `U_i` (hence also `U_{i+1}`), and then that, in the expression of
`int(p_α(x)) p_β(y)`, only terms of the form `p_{n α + β}(C_{n, 1, α, β} x^n y)` occur modulo `U_{i+1}`, which are
therefore linear in `y`. It follows that the inner automorphisms defined by sections of `U_α` act linearly on the
quotient `U_i / U_{i+1}` identified with `W(E_i)`. As this is also trivially true for the inner automorphisms defined by
sections of `T`, and as `P` is generated by `T` and the `U_α`, `a(α) ⩾ 0`, one deduces that:

(i) each `U_i` is invariant in `P`,

(ii) the inner automorphisms defined by sections of `P` act linearly on `U_i / U_{i+1} ≃ W(E_i)`.

### 2.1.2.

<!-- label: III.XXVI.2.1.2 -->

Now let `(T', M', R', Δ', …)` be a new pinning of `G` adapted to `P`.

<!-- original page 439 -->

By 1.15, there exists an inner automorphism of `G` coming from `P` that transforms the old pinning into the new one.
Possibly after extending `S`, one may assume that this inner automorphism is of the form `int(p)`, `p ∈ P(S)`. If one
takes up the preceding constructions using the new pinning, it is clear that the groups `U'_i` and the isomorphisms
`U'_i / U'_{i+1} ≃ W(E'_i)` obtained are deduced from `U_i` and `U_i / U_{i+1} ≃ W(E_i)` by transport of structure via
`int(p)`. It follows from remarks (i) and (ii) above that one therefore has `U'_i = U_i`, and that the two vector
structures constructed on `U_i / U_{i+1} = U'_i / U'_{i+1}` coincide.

This shows that the groups `U_i` and the vector structures on the quotients `U_i / U_{i+1}` are independent of the
pinning considered (and in particular invariant under every automorphism of `P`, as one sees easily).

We have therefore proved the proposition when the pair `(G, P)` is pinnable (part (iii) is trivial, since by
Exp. XXI 3.1.2, the set `{ a(γ) | γ ∈ R }` is an interval of `ℤ`, hence one cannot have
`dim(U_{i, s}) = dim(U_{i+1, s})` unless `U_{i, s} = e`).

### 2.1.3.

<!-- label: III.XXVI.2.1.3 -->

In the general case, there exists a covering family for the (fpqc) topology `{ S_j → S }` such that each pair
`(G_{S_j}, P_{S_j})` is pinnable (1.14). By the preceding, one has descent data on the `rad^u(P_{S_j})_i`, compatible
with the vector structures of the quotients, and one concludes by descent of closed subschemes (resp. locally free
modules)[^N.D.E-XXVI-8].

**Corollary 2.2.** *Let `S` be an affine scheme, `G` an `S`-reductive group, `P` a parabolic subgroup of `G`. One has*

```text
H^1(S, rad^u(P)) = 0,
```

*i.e. every principal homogeneous bundle under `rad^u(P)` is trivial.*

<!-- label: III.XXVI.2.2 -->

Indeed, `S` decomposes as a sum of subschemes on each of which `rad^u(P)` is of constant relative dimension. One may
<!-- original page 440 -->
therefore, by (iii), assume that there exists `n` such that `U_n = e`. Since `H^1(S, U_i / U_{i+1}) = H^1(S, W(E_i)) = 0`
by TDTE I, B, 1.1 (or SGA 1, XI 5.1), one concludes at once.

**Corollary 2.3.** *Under the preceding conditions, `P` possesses a Levi subgroup `L`. If `L` is a Levi subgroup of `P`,
the canonical map*

```text
H^1(S, L) ⟶ H^1(S, P)
```

*is bijective (cf. the introduction of Exp. XXIV for the definition of `H^1(S, −)`).*

<!-- label: III.XXVI.2.3 -->

The first assertion follows from 2.2 and 1.9. The canonical map `H^1(S, L) → H^1(S, P)` is surjective, because `P` is
the semidirect product `L · rad^u(P)`. To prove that it is injective, it suffices to see that for every principal
homogeneous bundle `Q` under `L`, one has `H^1(S, rad^u(P)_Q) = 0`, where the subscript `Q` denotes twisting by the
`L`-bundle `Q`. This can be proved in two ways: one may take up the proof of 2.2, using the fact that the vector
structures on the `U_i / U_{i+1}` are invariant under `L`; one may also remark that `rad^u(P)_Q` is identified with the
unipotent radical of the parabolic subgroup `P_Q` of `G_Q`, and apply 2.2 to `P_Q`.

**Corollary 2.4.** *Let `S` be a semi-local scheme, `G` an `S`-reductive group, `P` a parabolic subgroup of `G`. There
exists a maximal torus `T` of `G` contained in `P`.*

<!-- label: III.XXVI.2.4 -->

Indeed, in view of 2.3, `P` has a Levi subgroup `L`, and it suffices to prove that `L` has a maximal torus, which
follows from Exp. XIV, 3.20.

<!-- original page 441 -->

**Corollary 2.5.** *Let `S` be an affine scheme, `G` an `S`-reductive group, `P` a parabolic subgroup of `G`. There
exists a locally free `O_S`-module `E` such that `rad^u(P)` is isomorphic as an `S`-scheme to `W(E)`.*

<!-- label: III.XXVI.2.5 -->

Indeed, let us prove by induction on `i` that one has an isomorphism of `S`-schemes

```text
rad^u(P) / U_i ≃ W(E_0 ⊕ E_1 ⊕ · · · ⊕ E_{i−1}).
```

This is clear for `i = 0`. Assume `i > 0`; then `rad^u(P) / U_i` is a principal homogeneous bundle with base
`rad^u(P) / U_{i−1}`, under the group

```text
(U_{i−1} / U_i)_{rad^u(P) / U_{i−1}} ≃ W(E_{i−1} ⊗ O_{rad^u(P) / U_{i−1}}).
```

Now the base is affine (e.g. by the induction hypothesis), so this bundle is trivial (TDTE I or SGA 1 XI, *loc. cit.*),
and there exists an isomorphism of `S`-schemes
`rad^u(P) / U_i ≃ (rad^u(P) / U_{i−1}) ×_S (U_{i−1} / U_i)`, which completes the proof.

**Corollary 2.6.** *Let `S` be a semi-local scheme, `{s_i}` the set of its closed points, `G` an `S`-reductive group,
`P` a parabolic subgroup of `G`. The canonical map*

```text
rad^u(P)(S) ⟶ ∏_i rad^u(P)(Spec κ(s_i))
```

*is surjective.*

<!-- label: III.XXVI.2.6 -->

Indeed, if `S = Spec(A)`, `κ(s_i) = A/p_i`, and if `E` is given by the projective (hence flat) module `E`, we must prove
that the map

```text
E ⟶ ∏_i E ⊗_A A/p_i
```

is surjective. It suffices to do this when `E = A`, in which case it is well known (cf. Bourbaki, *Alg. Comm.* Chap. II,
§1, no. 2, Proposition 5).

<!-- original page 442 -->

**Corollary 2.7.** *Let `k` be an infinite field, `G` a `k`-reductive group, `P` a parabolic subgroup of `G`; then
`rad^u(P)(k)` is dense in `rad^u(P)`.*

<!-- label: III.XXVI.2.7 -->

**Corollary 2.8.** *Let `S` be a semi-local scheme, `{s_i}` the set of its closed points, `G` an `S`-reductive group,
`P` a parabolic subgroup of `G`, and `L_i` a Levi subgroup of `P_{s_i}` for each `i`. There exists a Levi subgroup `L`
of `P` inducing `L_i` for each `i`.*

<!-- label: III.XXVI.2.8 -->

Indeed, let `L_0` be a Levi subgroup of `P` (2.3). For each `i`, let `u_i ∈ rad^u(P)(Spec(κ(s_i)))` be such that
`int(u_i) L_{0, s_i} = L_i` (1.8); if `u ∈ rad^u(P)(S)` induces `u_i` for each `i` (2.6), then `L = int(u) L_0` answers
the question.

**Corollary 2.9.** *In the situation of 2.1, let moreover `H` be a sub-group-scheme of `G`, smooth and of finite
presentation over `S`, with connected fibers, such that `P ∩ H` contains locally for the (fpqc) topology a maximal
torus of `G`. Then for each `i ⩾ 0`, there exists a locally direct factor submodule `F_i` of `E_i` such that the
isomorphism `U_i / U_{i+1} ⥲ W(E_i)` induces an isomorphism of groups*

```text
(U_i ∩ H) / (U_{i+1} ∩ H) ⥲ W(F_i).
```

<!-- label: III.XXVI.2.9 -->

Indeed, `H` is a subgroup of type (R) of `G` (Exp. XXII, 5.2.1). On the other hand, the assertion to be proved is local
for the (fpqc) topology, and one may assume `G` split relative to a maximal torus of `P ∩ H`; one may even reduce to the
situation of 2.1.1, with `H` defined by a subset `R'` of `R`. Taking up the notation of *loc. cit.*, one sees by
Exp. XXII, 5.6.7 (ii) that `U_i ∩ H = ∏_{α ∈ R_i ∩ R'} U_α`, hence that `(U_i ∩ H) / (U_{i+1} ∩ H)` is identified with
`∏_{α ∈ R', a(α) = i+1} U_α`, which yields the result.

**Corollary 2.10.** *In the situation of 2.9, the conclusions of 2.2, 2.5, 2.6, 2.7 are also valid when `rad^u(P)` is
replaced by `rad^u(P) ∩ H`.*

<!-- original page 443 -->

<!-- label: III.XXVI.2.10 -->

**Corollary 2.11.**[^N.D.E-XXVI-9] *Let `G` be an `S`-reductive group, `P` a parabolic subgroup, `H` a subgroup of type
(RC) of `P` such that `rad^u(H) = rad^u(P) ∩ H`. Then statements 2.2 to 2.8 are also valid when `P` is replaced by `H`.*

<!-- label: III.XXVI.2.11 -->

## 3. Scheme of parabolic subgroups of a reductive group

<!-- label: III.XXVI.3 -->

### 3.1.

<!-- label: III.XXVI.3.1 -->

Let `E` be a finite twisted constant `S`-scheme (Exp. X, 5.1). Consider the `S`-functor `Of(E)`, where `Of(E)(S')` is
the set of open and closed subschemes of `E_{S'}` (or, equivalently, the set of open and closed subsets of `E_{S'}`);
then `Of(E)` is representable by a finite twisted constant `S`-scheme. Indeed, if `E = A_S`, where `A` is a finite set,
one has immediately `Of(E) ≃ P(A)_S` (where `P(A)` denotes the power set of `A`), and one concludes by descent of open
and closed subschemes. One trivially has:

```text
Of(E_{S'}) = Of(E)_{S'},        Of(E ×_S E') = Of(E) ×_S Of(E').
```

### 3.2.

<!-- label: III.XXVI.3.2 -->

Let `S` be a scheme, `G` an `S`-reductive group. The functor `Par(G)` of parabolic subgroups of `G` is defined by

```text
Par(G)(S') = the set of parabolic subgroups of G_{S'}.
```

In particular, `G ∈ Par(G)(S)`, `Bor(G) ⊂ Par(G)`. We propose to define a morphism

```text
t : Par(G) ⟶ Of(Dyn(G))
```

possessing the following properties:

(i) `t` is functorial in `G` (with respect to isomorphisms) and commutes with base change.

<!-- original page 444 -->

(ii) If `(T, M, R, Δ, …)` is a pinning of `G` adapted to the parabolic subgroup `P` (1.11), the canonical isomorphism
`Dyn(G) ≃ Δ_S` (Exp. XXIV, 3.4 (iii)) transforms `t(P)` into `Δ(P)_S` (notations of 1.11, 1.12).

Let first `P` be a parabolic subgroup of `G` and `(T, M, R, Δ, …)` a pinning of `G` adapted to `P`. One defines `t(P)`
by (ii); the subscheme `t(P)` of `Dyn(G)` thus constructed is independent of the pinning chosen. Indeed, if
`(T', M', R', Δ', …)` is another pinning of `G` adapted to `P`, the unique inner automorphism of `G` transforming the
first pinning into the second comes from `P` (1.15); the canonical isomorphism `Δ ⥲ Δ'` therefore transforms `Δ(P)`
into `Δ'(P)`, which entails the announced result.

If now one no longer assumes `(G, P)` to be pinnable, it follows immediately from 1.14 and the definition of `Dyn(G)`
(Exp. XXIV, 3.3) that one may define by descent an open and closed subscheme `t(P)` of `Dyn(G)`, unique, such that for
every `S' → S` for which `(G, P)_{S'}` is pinnable, one has `t(P)_{S'} = t(P_{S'})`.

**Theorem 3.3.** *Let `S` be a scheme, `G` an `S`-reductive group,*

```text
t : Par(G) ⟶ Of(Dyn(G))
```

*the morphism defined above.*

*(i) For two parabolic subgroups `P` and `P'` of `G` to be conjugate locally for the (fpqc) topology (cf. 1.3), it is
necessary and sufficient that `t(P) = t(P')`.*

*(ii) `Par(G)` is representable, and the morphism `t` is smooth, projective, with integral geometric fibers.*

<!-- label: III.XXVI.3.3 -->

By 3.2 (i), and the fact that inner automorphisms of `G` act trivially on `Dyn(G)` (Exp. XXIV, 3.4 (iv)), one indeed has
`t(P) = t(P')` when `P` and `P'` are conjugate. Conversely, let `P` and `P'` be two parabolic subgroups of `G` such that
`t(P) = t(P')`; let us prove that `P` and `P'` are conjugate in `G`, locally for the (fpqc) topology; one may first
<!-- original page 445 -->
assume that the pairs `(G, P)` and `(G, P')` are pinnable (1.14); by conjugacy of pinnings in `G` (Exp. XXIV, 1.5), one
may assume that there exists a pinning `(T, M, R, Δ)` of `G` adapted to `P` and `P'`. Then `t(P) = t(P')` implies
`Δ(P) = Δ(P')`, hence `P = P'` (cf. 1.4 (v)). We have therefore proved (i). To demonstrate (ii), let us take up the
notation of Exp. XXII, 5.11.5[^N.D.E-XXVI-10].

We have a canonical morphism `Par(G) → H_c`, and it is clear (e.g. by reduction to the pinned case) that it fits into a
cartesian square (where the vertical arrows are monomorphisms)

```text
Par(G) ────────t──────→ Of(Dyn(G))
   │                          │
   │                          │
   ▼                          ▼
   H_c ────────cℓ─────→ Cℓ_c.
```

Now (*loc. cit.*) `H_c` is representable and the morphism `cℓ` is smooth, quasi-projective, of finite presentation, with
integral geometric fibers, hence the same holds for `t`.

It remains to prove that `t` is proper; but this is now a local assertion for the (fpqc) topology, and one may reduce
to the pinned case `G = (G, T, M, R, Δ, …)`. One then has `Dyn(G) ≃ Δ_S`, and it suffices to prove that for every subset
`Δ_1` of `Δ`, the `S`-scheme `t^{-1}((Δ_1)_S)` is proper over `S`. Now if `P_1` is the parabolic subgroup of `G`
containing `T` such that `Δ(P_1) = Δ_1`, it follows from (i) that the morphism `G → Par(G)` defined set-theoretically by
`g ↦ int(g) P_1` induces an isomorphism of `G / Norm_G(P_1)` onto `t^{-1}((Δ_1)_S)`. Now, by 1.2, `G / Norm_G(P_1) =
G / P_1` is projective over `S`.

**Definition 3.4.** *`Of(Dyn(G))` is called the* scheme of types of parabolics *of `G`; `t(P)` is called the* type *of
`P`.*

<!-- label: III.XXVI.3.4 -->

**Corollary 3.5.** *The `S`-functor `Par(G)` is representable by an `S`-scheme that is smooth and projective over `S`.
The decomposition*

```text
Par(G) ⟶ Of(Dyn(G)) ⟶ S
```

*is the Stein factorization (EGA III, 4.3.3) of the structural morphism `Par(G) → S`.*

<!-- original page 446 -->

<!-- label: III.XXVI.3.5 -->

**Corollary 3.6.** *For each `t ∈ Of(Dyn(G))(S)`, the `S`-scheme*

```text
Par_t(G) = t^{-1}(t)
```

*of parabolic subgroups of `G` of type `t` is smooth and projective over `S`, homogeneous under `G`. If `P` is a
parabolic subgroup of `G`, one has a canonical isomorphism `G/P ⥲ Par_{t(P)}(G)`. One has `Par_∅(G) = Bor(G)`,
`Par_{Dyn(G)}(G) ⥲ S`.*

<!-- label: III.XXVI.3.6 -->

**Remark 3.7.** *The `S`-scheme `Of(Dyn(G))` is equipped with a natural order structure (the relation of domination,
here set-theoretic inclusion, between subschemes). This order structure is a lattice; in particular, the infimum of two
open and closed subschemes of `Dyn(G)_{S'}` is obviously their intersection. Let us moreover remark that if `B` is a
Borel subgroup of `G`, one may define the functor `X` of parabolic subgroups of `G` containing `B`. The morphism
`X → Of(Dyn(G))` induced by `t` is an isomorphism (for the structure of "ordered scheme"), by virtue of the assertion
`P ⊂ Q ⇒ t(P) ⊂ t(Q)` and of:*

<!-- label: III.XXVI.3.7 -->

**Lemma 3.8.** *Let `S` be a scheme, `G` an `S`-reductive group, `P` a parabolic subgroup of `G`, `t'` a section of
`Of(Dyn(G))` over `S`, such that `t(P) ⊂ t'`. There exists a unique parabolic subgroup `P'` of `G`, containing `P`, and
such that `t(P') = t'`.*

<!-- label: III.XXVI.3.8 -->

Possibly after extending the base, one may assume that `P` contains a Borel subgroup `B` of `G`. The uniqueness of `P'`
then follows from 1.17. To demonstrate existence, one may place oneself in the split case, in which case the assertion
is evident, cf. §1.

<!-- original page 447 -->

**Remarks 3.8.1.** *(i) The assertion analogous to 3.8 obtained by reversing the inclusions is obviously false. It
would, for instance, entail that every group of type `A_1` has a Borel subgroup, which is not the case, cf. Exp. XX,
§5.*

*(ii) It follows immediately from the preceding that `t(P) ⊂ t(Q)` means that locally for (fpqc) or (ét), `P` is
conjugate to a subgroup of `Q` (it suffices moreover to verify the assertion on geometric fibers). Moreover, one shall
see in §5 that the étale topology may be replaced by the Zariski topology.*

<!-- label: III.XXVI.3.8.1 -->

### 3.9.

<!-- label: III.XXVI.3.9 -->

The preceding discussions may be taken up in the case of critical subgroups. Let us recall (Exp. XXII, 5.10.4 and
5.10.5) that a reductive subgroup `H` of the reductive group `G` is *critical* if `H = Centr_G(rad(H))`, that a subtorus
`Q` of `G` is a *C-critical torus* if `Q = rad(Centr_G(Q))`, and that critical subgroups and C-critical
tori[^N.D.E-XXVI-11] are in bijective correspondence (via `H ↦ rad(H)` and `Q ↦ Centr_G(Q)`).

If `(G, T, M, R)` is a split `S`-group, the subgroup of `G` containing `T` corresponding to the part `R'` of `R`
(Exp. XXII, 5.4.2) is critical if and only if `R'` is "vectorial" (that is, the intersection of `R` with a vector
subspace of `M ⊗ ℚ`), cf. Exp. XXII, 5.10.6.

If `G` is an arbitrary `S`-reductive group, one defines, as in Exp. XXII, 5.11.5, an étale finite `S`-scheme
`Cℓ_{crit}`, which in the split case will be the constant scheme associated with the set of vectorial parts of `R`
modulo the action of the Weyl group. If `Crit(G)` denotes the "functor of critical subgroups" of `G`, one has a
canonical morphism `Crit(G) ⟶ Cℓ_{crit}`, which fits into a cartesian diagram[^N.D.E-XXVI-12]

```text
Crit(G) ────cℓ───→ Cℓ_{crit}
   │                   │
   │                   │
   ▼                   ▼
   H_c ────cℓ─────→ Cℓ_c.
```

<!-- original page 448 -->

**Proposition 3.10.** *Let `S` be a scheme, `G` an `S`-reductive group, `Crit(G)` the functor of its critical subgroups,
`Cℓ_{crit}` and `cℓ : Crit(G) → Cℓ_{crit}` the étale finite `S`-scheme and the morphism defined above.*

*(i) For critical subgroups `H` and `H'` of `G` to be conjugate (locally for the (fpqc) topology), it is necessary and
sufficient that `cℓ(H) = cℓ(H')`.*

*(ii) `Crit(G)` is representable and the morphism `cℓ` is smooth, affine, with integral geometric fibers.*

<!-- label: III.XXVI.3.10 -->

This is proved as 3.3, with the exception of the assertion "`cℓ` is affine". It suffices to prove that `Crit(G)` is
affine over `S`. Now `Crit(G)` is naturally identified with the `S`-functor of critical tori of `G`, and one therefore
has a canonical monomorphism

```text
Crit(G) ⟶ M
```

where `M` is the scheme of subgroups of multiplicative type of `G` (Exp. XI, 4.1). To prove that `Crit(G)` is affine
over `S`, it suffices, by Exp. XII 5.3, to show that this morphism is an open and closed immersion, or equivalently, by
making the base change `M → S`, to prove the following assertion: if `Q` is a subgroup of multiplicative type of the
reductive group `G`, the `S' → S` such that `Q_{S'}` is a critical torus of `G_{S'}` are those that factor through a
certain open and closed subscheme of `S`. Now to say that `Q` is a critical torus is to say:

(1) that `Q` is a torus,

(2) `Q` being a torus, that `rad(Centr_G(Q))`, which is also a torus, is of the same relative dimension as `Q`.

These two conditions are indeed of the type envisaged.

**Corollary 3.11.** *The `S`-functor `Crit(G)` is representable by an `S`-scheme that is smooth and affine over `S`.*

<!-- original page 449 -->

<!-- label: III.XXVI.3.11 -->

**Corollary 3.12.** *Let `H` be a critical subgroup of the `S`-reductive group `G`. Then `G / Norm_G(H)` and `G / H` are
representable by `S`-schemes that are affine and smooth over `S`.*

<!-- label: III.XXVI.3.12 -->

The first assertion follows from 3.11, the second from the first and from Exp. XXII, 5.10.2.

**Corollary 3.13.** *Let `Q` be a subtorus of the `S`-reductive group `G`. Then `G / Centr_G(Q)` is representable by an
`S`-scheme that is smooth and affine over `S`. The same holds for `G / Norm_G(Q)` if `Q` is a critical subtorus of
`G`.*

<!-- label: III.XXVI.3.13 -->

Indeed, `H = Centr_G(Q)` is critical (Exp. XXII, 5.10.5), and one has `Norm_G(H) = Norm_G(Q)` if `Q` is critical
(*loc. cit.* 5.10.8).

### 3.14.

<!-- label: III.XXVI.3.14 -->

By the conjugacy of Levi subgroups of parabolic subgroups of `G`, there exists a unique morphism

```text
u : Of(Dyn(G)) ⟶ Cℓ_{crit}
```

such that for every parabolic subgroup `P` of `G`, and every Levi subgroup `L` of `P`, one has `cℓ(L) = u(t(P))`, and
such that this holds after every base change.

### 3.15.

<!-- label: III.XXVI.3.15 -->

Let `S` be a scheme, `G` an `S`-reductive group. Consider the `S`-functors[^N.D.E-XXVI-13]:

```text
PL(S')  = { pairs P ⊃ L, P parabolic of G_{S'}, L Levi subgroup of P };
PT(S')  = { pairs P ⊃ T, P parabolic of G_{S'}, T maximal torus of P };
CT(S')  = { pairs C ⊃ T, C critical subgroup of G_{S'}, T maximal torus of C };
PLT(S') = { triples P ⊃ L ⊃ T, (P, T) ∈ PT(S'), L Levi subgroup of P }.
```

One has evident morphisms between these functors and the functors `Par(G)`, `Crit(G)`,

<!-- original page 450 -->

`Tor(G)` already introduced, and one has a commutative diagram in the form of a truncated cube (see the following
figure):

```text
                        g (ét.)
            CT  ←─────────────  PLT
           ╱   ╲                  ╲
        a╱       ╲b                ╲ (aff.)
        ╱          ╲                ╲
       ╱             ╲                ╲
      ╱  (aff.)    (ét.) k             ╲
     ╱       f (ét.)                    ╲
 Crit(G) ←─────────  PL                  PT     (e isom.)
     │                │                  │
     │ cℓ (aff.)      │                  │
     ▼                ▼                  ▼
  Cℓ_{crit}        Tor(G) ←──── h (ét.) ─ PT
         ╲          │                    ╱
       q ╲   (ét.)   │    d (aff.)      ╱
           ╲          │                ╱
       u ╲    │ r (aff.)             ╱  c (aff.)
              ▼                    ╱
       u (ét.) S                  ╱
           ╲                    ╱
              ╲ p (ét.)        ╱
                              ╱
                     t (proj.)
            Of(Dyn(G)) ────── Par(G)
```

*Figure 3.15.1.*

<!-- TRANSLATOR NOTE: The cube diagram in the source has many visual lines/arrows that are difficult to render in plain text; the labels and key adjacencies are preserved above. -->

<!-- original page 451 -->

**Theorem 3.16.** *(cf. Figure 3.15.1).*

*(i) All the morphisms of the diagram are smooth, surjective, and of finite presentation.*

*(ii) All the morphisms of the diagram, with the exception of `t`, are affine; the morphism `t` is projective.*

*(iii) All the morphisms of the diagram are either étale finite or with integral geometric fibers: the morphisms `f`,
`g`, `h`, `k`, `p`, `q` and `u` are étale finite, the morphisms `a`, `b`, `c`, `d`, `r` and `cℓ` are with integral
geometric fibers, the morphism `e` is an isomorphism.*

*(iv) The square `(a, b, f, g)` is cartesian.*

<!-- label: III.XXVI.3.16 -->

*Proof.* It is first clear that `e` is an isomorphism, by 1.6 (ii). On the other hand, (iv) is evident.

The morphism `a` is smooth, affine, with integral geometric fibers: indeed, by base change `Crit(G) → S`, it suffices to
verify that the morphism `Tor(L_0) → S`, where `L_0` is the universal critical subgroup, has these properties; but
`L_0` is reductive (by definition), and one is reduced to Exp. XXII, 5.8.3. The morphism `b` therefore has the same
properties, by virtue of (iv).

<!-- original page 452 -->

The morphism `d` is also smooth, affine, with integral geometric fibers, by 1.9; the same therefore holds for
`c = d b e^{-1}`. The morphism `r` has these same properties (Exp. XXII, 5.8.3), as does the morphism `cℓ` (3.10).

On the other hand, we have already proved that the morphisms `p` and `q` are étale finite surjective (3.1 and 3.9). If
we prove that `f` and `k` are étale finite surjective, the same properties will hold for `g` (by (iv)) and for `h`
(since `h = k g e^{-1}`); as the properties stated for `t` were established in 3.3 (ii), it therefore only remains to
prove that `f` (resp. `k`) is étale finite surjective; let us give the proof for `k`, that for `f` being analogous.

It suffices to prove that if `T` is a maximal torus of `G`, the functor `C` of critical subgroups of `G` containing `T`
is representable by an étale finite `S`-scheme with non-empty fibers; one may assume `G` split with respect to `T`; let
then `E` be the set of vectorial parts of `R` (root system of the splitting); `C` is representable by `E_S` (3.9), which
completes the proof.

**Corollary 3.17.** *All the functors of the preceding diagram are representable by `S`-schemes that are smooth over
`S`, and they are all affine over `S`, with the exception of `Par(G)`.*

<!-- label: III.XXVI.3.17 -->

**Remark 3.18.** *(i) The fact that the morphism `f : PL → Crit(G)` is étale surjective implies that a subgroup of `G`
is critical if and only if it is, locally for the étale topology, a Levi subgroup of a parabolic subgroup of `G`.*

*On the other hand, one should not believe that in general the map `f(S) : PL(S) → Crit(G)(S)` is surjective: it may
very well happen that a critical subgroup `C` of `G` does not come on `S` from a parabolic subgroup of `G`; for example,
a maximal torus is not always contained in a Borel subgroup (example: a non-split form of `SL_2`, cf. Exp. XX, §5).*

*(ii) Similarly, it may happen that the morphism `u : Of(Dyn(G)) → Cℓ_{crit}` is not an isomorphism: two parabolic
subgroups of distinct types may have Levi subgroups of the same type; for example: in a group of type `A_2`, there are
two types of parabolic subgroups whose Levi subgroups are of semisimple rank 1 (corresponding to the two vertices of
the diagram), whereas there is only one type of critical subgroup of rank 1.*

*The analogous example with a group of type `A_3` shows that, even over an algebraically closed field, non-isomorphic
parabolic subgroups may have Levi subgroups of the same type.*[^N.D.E-XXVI-14]

<!-- label: III.XXVI.3.18 -->

Let us close this section with an application to the theory of principal bundles.

<!-- original page 453 -->

**Lemma 3.20.**[^N.D.E-XXVI-15] *Let `S` be a scheme, `G` an `S`-reductive group, `F` a principal homogeneous bundle
under `G`, `G_F` the corresponding twisted form of `G`. Identify `Dyn(G)` and `Dyn(G_F)` (Exp. XXIV, 3.5). Let `P` be a
parabolic subgroup of `G`. One has a canonical isomorphism*

```text
F/P ⥲ Par_{t(P)}(G_F).
```

*In particular, for the structural group of `F` to reduce to `P`, it is necessary and sufficient that `G_F` have a
parabolic subgroup of type `t(P)`.*

<!-- label: III.XXVI.3.20 -->

The proof goes exactly as in Exp. XXIV, 4.2.1.

### 3.21.

<!-- label: III.XXVI.3.21 -->

If `S` is a scheme, `G` an `S`-reductive group, and if `t ∈ Of(Dyn(G))(S)`, one denotes by `H^1_t(S, G)` the subset of
`H^1(S, G)` formed of classes of principal bundles `F` under `G` such that the associated group `G_F` has a parabolic
subgroup of type `t`. If `G` itself has a parabolic subgroup `P` of type `t`, `H^1_t(S, G)` is none other than the
image of `H^1(S, P)` in `H^1(S, G)`, an image which therefore does not depend on the `P` chosen.

## 4. Relative position of two parabolic subgroups

<!-- label: III.XXVI.4 -->

### 4.1. A preliminary result

<!-- label: III.XXVI.4.1 -->

**Lemma 4.1.1.** *Let `k` be a field, `G` a `k`-reductive group, `P` and `P'` two parabolic subgroups of `G`.*

*(i) Then `P ∩ P'` is smooth, of the same reductive rank as `G`, and contains a maximal torus `T` of `G`.*

*(ii) The set `R'` of roots of `P ∩ P'` with respect to `T` is a closed subset of the set `R` of roots of `G` with
respect to `T`.*[^N.D.E-XXVI-16]

<!-- label: III.XXVI.4.1.1 -->

Suppose first `k` algebraically closed. Let `B` (resp. `B'`) be a Borel subgroup
<!-- original page 454 -->
of `P` (resp. `P'`). One knows that there exists `g ∈ G(k)` such that `int(g) B = B'`. On the other hand, if `T_0` is a
maximal torus of `B` and one sets `N = Norm_G(T_0)`, one knows (Bruhat's theorem, Bible, §13.4, Cor. 1 to Th. 3) that
`G(k) = B(k) N(k) B(k)`. One therefore sees that there exist `b, b_1 ∈ B(k)` and `n ∈ N(k)` such that `g = b n b_1`,
hence `int(b) int(n) B = B'`. One then has

```text
P ∩ P' ⊃ B ∩ B' = int(b)(B ∩ int(n) B') ⊃ int(b) T_0.
```

Now suppose `k` arbitrary. Applying the preceding result, one sees that `P_{k̄} ∩ P'_{k̄}` contains a maximal torus of
`G_{k̄}`; by Exp. XXII, 5.4.5, one deduces that `(P ∩ P')_{k̄}` is smooth "along the unit section", hence smooth since
one is over a field (Exp. VI_A 1.3.1), hence `P ∩ P'` is smooth. By Exp. VI_A 2.3.1, the neutral component `(P ∩ P')^0`
of `P ∩ P'` is therefore an open subgroup of `P ∩ P'`, smooth over `S`. One may then apply Exp. XIV, 1.1 to it, whence
(i).

Finally, the set `R_P` (resp. `R_{P'}`) of roots of `P` (resp. `P'`) with respect to `T` is closed and one has
`R' = R_P ∩ R_{P'}`, whence (ii).

**Remark 4.1.2.** *One may prove ([BT65], 4.5) that `P ∩ P'` is connected;[^N.D.E-XXVI-17] this will be used in 4.5.1.*

<!-- label: III.XXVI.4.1.2 -->

**Remark 4.1.3.** *The preceding lemma is not true over an arbitrary scheme. Indeed, let `G` be, for example, a
reductive group over an algebraically closed field `k`, and let `B` be a Borel subgroup of `G`. Take `S = X` as base
and consider the Borel subgroups `B_1` and `B_2` of `G_X`, where `B_1 = B_X` and `B_2 = int(g_0) B_1`, `g_0` being the
canonical (diagonal) section of `G_X`. For each `g ∈ X(k)`, the fiber of `B_1 ∩ B_2` at `g` is none other than
`B ∩ int(g) B`. If one assumes `B ≠ G`, the dimension of this fiber varies with `g`, hence `B_1 ∩ B_2` cannot be smooth
over `X`.*

<!-- label: III.XXVI.4.1.3 -->

### 4.2. Transversal position

<!-- label: III.XXVI.4.2 -->

**Theorem 4.2.1.** *Let `S` be a scheme, `G` an `S`-reductive group, `P` and `Q` two parabolic subgroups of `G`. The
following conditions on the pair `(P, Q)` are equivalent:*

*(i) `Lie(P/S) + Lie(Q/S) = Lie(G/S)`.*

<!-- original page 455 -->

*(ii) The canonical morphism `P ×_S Q → G` is smooth.*

*(ii') The canonical morphism `P → G/Q` is smooth.*

*(iii) The canonical morphism `P ×_S Q → G` is open.*

*(iii') The canonical morphism `P → G/Q` is open.*

*(iv) The canonical morphism `P ×_S Q → G` is fiberwise dominant.*

*(iv') The canonical morphism `P → G/Q` is fiberwise dominant.*

*(v) For every `s ∈ S`, "`P_s ∩ Q_s` is of minimum dimension", i.e. one has*

```text
dim(P_s ∩ Q_s) = dim P_s + dim Q_s − dim G_s.
```

*(vi) There exists a covering family for the étale topology `{ S_i → S }`, and for each `i` a Borel subgroup `B_i` of
`P_{S_i}` and a Borel subgroup `B'_i` of `Q_{S_i}`, such that `B_i ∩ B'_i` is a maximal torus of `G_{S_i}`.*

*(vii) There exists a covering family for the étale topology `{ S_i → S }`, and for each `i` a splitting
`(T_i, …, R_i)` of `G_{S_i}` and a system of positive roots `R_i^+` of `R_i`, such that `P_{S_i}` (resp. `Q_{S_i}`) is
the subgroup of type (R) of `G_{S_i}` containing `T_i` and defined by a subset `R_i^{(1)}` (resp. `R_i^{(2)}`) of `R`
containing `R_i^+` (resp. `−R_i^+`) (see Exp. XXII, 5.4.2 and 5.2.1 for the definitions).*

<!-- label: III.XXVI.4.2.1 -->

*Proof.* We shall prove the theorem following the logical diagram

```text
(i) ⇔ (vii) ⇔ (vi)
                  ╲
                   ╲
(ii') ⇒ (iii') ⇒ (iv') ⇒ (v)
                  ╱
                 ╱
(ii)  ⇒ (iii)  ⇒ (iv)
```

<!-- original page 456 -->

One trivially has (ii) ⇒ (iii) and (ii') ⇒ (iii'). If (iii) holds, the set-theoretic image of the morphism
`P ×_S Q → G` is an open set of `G` containing the unit section; since the fibers of `G` are connected, this image is
dense on each fiber, which proves (iv). One similarly has (iii') ⇒ (iv').

One has (ii') ⇒ (ii), by the cartesian diagram

```text
P ×_S Q ─────→ G
   │           │
 pr_1│         │
   ▼           ▼
   P ───────→ G/Q.
```

On the other hand (iv) or (iv') implies (v), by the theory of dimension (cf. EGA IV₂, 5.6.6). One notes that one may
indeed assume `S = Spec(k)`, `k` an algebraically closed field, and that every non-empty fiber of the morphism (iv),
resp. (iv'), at a point of `G(k)`, resp. of `(G/Q)(k)`, is isomorphic to `P ∩ Q` (as an immediate computation shows).

One has (vi) ⇒ (vii), by Exp. XXII, 5.5.1 (iv) and 5.9.2.

One has (vii) ⇒ (i), because to verify that `Lie(P) + Lie(Q) = Lie(G)`, one may reason locally for (fpqc); thus if (vii)
is satisfied one may assume `G` split, `P ⊃ B_{R^+}` and `Q ⊃ B_{−R^+}` (usual notations), in which case one already
has

```text
Lie(B_{R^+}) + Lie(B_{−R^+}) = Lie(G).
```

Let us prove that (i) implies (ii').

Let `u : P → G/Q` be the canonical morphism; to prove that `u` is smooth, it suffices to do so on the geometric fibers
of `u`, since `P` and `G/Q` are smooth over `S`, and one may therefore assume that `S` is the spectrum of an
algebraically closed field. As the morphism `u` is compatible with the obvious action of `P` (one has `u(p p') = p
u(p')`) it suffices, by a translation argument (cf. the proof of VI_B 1.3), to verify that `u` is smooth at
`e ∈ P(k)`, i.e. (SGA 1, II 4.7) that the tangent map to `u` at `e` is surjective; but the latter is naturally
<!-- original page 457 -->
identified with the canonical map `Lie(P) → Lie(G)/Lie(Q)`, which is surjective if (i) is satisfied.

It therefore only remains to verify the last assertion, namely (v) ⇒ (vi). Suppose first that `S` is the spectrum of an
algebraically closed field. By 4.1.1, there exists a maximal torus `T` contained in `P` and `Q`; let `R` (resp. `R_1`,
resp. `R_2`) be the set of roots of `G` (resp. `P`, resp. `Q`) relative to `T`.

One has:

```text
dim(G) = dim(T) + Card(R),         dim(P) = dim(T) + Card(R_1),
dim(Q) = dim(T) + Card(R_2),       dim(P ∩ Q) = dim(T) + Card(R_1 ∩ R_2),
```

by Exp. XXII, 5.4.4 and 5.4.5 for example. The condition of (v) is therefore equivalent to

```text
Card(R_1 ∩ R_2) = Card(R_1) + Card(R_2) − Card(R),
```

that is `R_1 ∪ R_2 = R`. To demonstrate (vi), it suffices, by Exp. XXII, 5.9.2 and 5.4.5, to prove that `R_1 ∩ −R_2`
contains a system of positive roots of `R`. We are therefore reduced to proving:

**Lemma 4.2.2.** *Let `R` be a "root system" (e.g. the set of roots of a root datum in the sense of Exposé XXI). Let
`R_1` and `R_2` be two closed subsets of `R` each containing a system of positive roots. If `R_1 ∪ R_2 = R`, then
`R_1 ∩ −R_2` contains a system of positive roots.*

<!-- label: III.XXVI.4.2.2 -->

Indeed, since `R_1 ∩ −R_2 = R_3` is evidently closed, and by Exp. XXI, 3.3.6, it suffices to show that
`R_3 ∪ −R_3 = R`. Now one knows that `R_1 ∪ −R_1 = R = R_2 ∪ −R_2`, and one concludes thanks to the following
elementary fact: if `A, A', B, B'` are four subsets of a set `E`, and if `A ∪ A' = B ∪ B' = A ∪ B = A' ∪ B' = E`, then
`(A ∩ B') ∪ (A' ∩ B) = E`.

This completes the proof of (v) ⇒ (vi) in the case where the base is the spectrum of an algebraically closed field. Let
<!-- original page 458 -->
us now return to the general case and assume (v) is satisfied. Let `s ∈ S`; by the preceding, one may find a Borel
subgroup `B̄` (resp. `B̄'`) of `P_s` (resp. `Q_s`) such that `B̄ ∩ B̄'` is a maximal torus of `G_s`.

Since the `S`-scheme `Bor(P) ≃ Bor(P/rad^u(P))` of Borel subgroups of `P` is smooth, one may, applying "Hensel's lemma"
(cf. Exp. XI 1.10) and reasoning locally for the étale topology (i.e. replacing `S` by an `S' → S` that is étale and
covering `s`, and `s` by a point of its fiber in `S'`), assume that there exists a Borel subgroup `B` of `P` projecting
onto `B̄`; one may similarly assume that there exists a Borel subgroup `B'` of `Q` projecting onto `B̄'`. Since
`B_s ∩ B'_s` is a maximal torus of `G_s`, there exists an open neighborhood `U` of `s` in `S` such that
`B_U ∩ B'_U` is a maximal torus of `G_U` (Exp. XXII, 5.9.4), which proves (vi). QED.

**Definition 4.2.3.** *A pair `(P, Q)` satisfying the equivalent conditions (i) to (vii) of Theorem 4.2.1 is said to be
in* transversal position. *One also says that `P` is in transversal position relative to `Q`, or, by abuse of language,
that `P` and `Q` are in (mutual) transversal position.*

<!-- label: III.XXVI.4.2.3 -->

In view of (vi), this definition coincides in the case of Borel subgroups with that of Exp. XXII, 5.9.1.

**Corollary 4.2.4.** *Let `S` be a scheme, `G` an `S`-reductive group, `P` and `Q` two parabolic subgroups of `G`.*

*(i) For `(P, Q)` to be in transversal position, it is necessary and sufficient that for each point `s` of `S`, the pair
`(P_s, Q_s)` be in transversal position; if `S' → S` is a surjective morphism, and if `(P_{S'}, Q_{S'})` is in
transversal position, then `(P, Q)` is in transversal position.*

<!-- original page 459 -->

*(ii) There exists an open subscheme `U` of `S` having the following property: for a morphism `S' → S` to factor
through `U`, it is necessary and sufficient that `(P_{S'}, Q_{S'})` be in transversal position.*

*(iii) Consider the subfunctors*

```text
Gen(G)   ⊂ Par(G) ×_S Par(G),
Gen(/Q)  ⊂ Par(G),
Gen(P/Q) ⊂ G
```

*defined as follows: for `S' → S`, `Gen(G)(S')` is the set of pairs of parabolic subgroups of `G_{S'}` in transversal
position, `Gen(/Q)(S')` is the set of parabolic subgroups of `G_{S'}` in transversal position relative to `Q_{S'}`,
`Gen(P/Q)(S')` is the set of `g ∈ G(S')` such that `int(g) P_{S'}` is in transversal position relative to `Q_{S'}`.*

*Each of these functors is representable by a universally schematically dense open subscheme over `S`[^N.D.E-XXVI-18]
(cf. Exp. XVIII §1) of the corresponding `S`-scheme `Par(G) ×_S Par(G)`, resp. `Par(G)`, resp. `G`.*

<!-- label: III.XXVI.4.2.4 -->

Assertions (i) follow at once from the description 4.2.1 (i) of the term "transversal position". To demonstrate (ii),
one takes `U = S − Supp(Coker u)` where `u` is the canonical morphism
`Lie(P) ⊕ Lie(Q) → Lie(G)`.

Since one has cartesian diagrams

```text
G ──f──→ Par(G)        Par(G) ──f'──→ Par(G) ×_S Par(G)
↑          ↑              ↑                  ↑
│          │              │                  │
Gen(P/Q) → Gen(/Q)       Gen(/Q) ─────→ Gen(G)
```

(where `f(g) = int(g) P` and `f'(R) = (R, Q)`), it suffices to verify (iii) in the case of `Gen(G)`.

<!-- original page 460 -->

Let then `P_0` be the canonical parabolic subgroup of `G_{Par(G)}`; set

```text
X = Par(G) ×_S Par(G),     P = pr_1^*(P_0),     Q = pr_2^*(P_0);
```

applying assertion (ii) to the parabolic subgroups `P` and `Q` of `G_X`, one constructs an open subscheme `U` of `X`,
which, as one verifies at once, is indeed identified with `Gen(G)`. It remains to verify the density assertion, which
can be done on geometric fibers[^N.D.E-XXVI-19]; one may therefore assume `S = Spec(k)`, `k` an algebraically closed
field. As `Par(G)` is smooth, it suffices to verify that `Gen(G)` meets each irreducible component of
`Par(G) ×_S Par(G)`; in other words, by 3.3, it suffices to see that if `t, t' ∈ Of(Dyn(G))(S)`, there exists a pair
`(P, P')` in transversal position with `t(P) = t`, `t(P') = t'`. Now this is immediate: one chooses a pair `(B, B')` of
Borel subgroups of `G` such that `B ∩ B'` is a maximal torus (one splits `G` and applies Exp. XXII, 5.9.2) then one
applies 3.8 to construct `P ⊃ B` and `P' ⊃ B'`, with `t(P) = t`, `t(P') = t'`; `P` and `P'` are of the desired types
and are in transversal position by 4.2.1 (vi).

**Corollary 4.2.5.** *Let `S` be a scheme, `G` an `S`-reductive group, `P` and `Q` two parabolic subgroups of `G`, the
pair `(P, Q)` being in transversal position.*

*(i) Let `P'` and `Q'` be two parabolic subgroups of `G`, of the same type as `P` and `Q` respectively. For the pair
`(P', Q')` to be in transversal position, it is necessary and sufficient that it be conjugate to the pair `(P, Q)`,
locally for the étale topology. (N. B. One shall see in §5 that the étale topology can be replaced by the Zariski
topology.)*

*(ii) The canonical morphism `P ×_S Q → G` induces a smooth and surjective morphism `P ×_S Q → Gen(Q/P)`, and an
isomorphism*

```text
(P ×_S Q) / (P ∩ Q) ≃ Gen(Q/P)
```

*(where `P ∩ Q = R` operates on `P ×_S Q` by `(p, q) r = (p r, r^{-1} q)`).*

*(iii) The canonical morphism `P → Par_{t(Q)}(G)` (defined set-theoretically by `p ↦ int(p) Q`) induces a smooth and
surjective morphism `P → Gen(/P) ∩ Par_{t(Q)}(G)`, and an*

<!-- original page 461 -->

*isomorphism*

```text
P / (P ∩ Q) ≃ Gen(/P) ∩ Par_{t(Q)}(G).
```

*(iv) The canonical morphism `G → Par_{t(P)}(G) ×_S Par_{t(Q)}(G)` (defined set-theoretically by
`g ↦ (int(g) P, int(g) Q)`) induces a smooth and surjective morphism
`G → Gen(G) ∩ (Par_{t(P)}(G) ×_S Par_{t(Q)}(G))` and an isomorphism*

```text
G / (P ∩ Q) ≃ Gen(G) ∩ (Par_{t(P)}(G) ×_S Par_{t(Q)}(G)).
```

<!-- label: III.XXVI.4.2.5 -->

Let us demonstrate (i). It is clear that the condition is sufficient; let us prove that it is necessary. Let then
`(P', Q')` be in transversal position. Since `P` and `P'` are conjugate locally for the étale topology, we may assume
`P = P'`, and it suffices to prove that if `Q` and `Q'` are two parabolic subgroups of `G`, in transversal position
relative to `P`, and of the same type, then they are conjugate, locally for the étale topology, by a section of `P`.
Using 4.2.1 (vi), one may assume that there exist Borel subgroups `B, B', B_1, B'_1` of `P, P, Q, Q'` respectively,
such that `B ∩ B_1 = T` and `B' ∩ B'_1 = T'` are maximal tori of `G`. Now the Killing pairs `(B, T)` and `(B', T')` of
`P` are conjugate locally in `P` for the étale topology (1.16), and one may assume `B = B'`, `T = T'`, in which case
one has `B_1 = B'_1` by Exp. XXII, 5.9.2, hence `Q = Q'` by 3.8.

Assertions (ii), (iii) and (iv) are proved in a parallel fashion. Let us demonstrate, for instance, (ii); let
`g ∈ Gen(Q/P)(S)`, i.e. let `g ∈ G(S)` be such that `int(g) Q` is in transversal position relative to `P`. By the
preceding proof, `Q` and `int(g) Q` are conjugate locally for the étale topology, by a section of `P`. Reasoning
<!-- original page 462 -->
locally for this topology, one may assume that there exists `p ∈ P(S)` such that `int(g) Q = int(p) Q`, hence
`p^{-1} g ∈ Norm_G(Q)(S) = Q(S)`; which proves the existence of `q ∈ Q(S)` such that `g = p q`. We have therefore proved
that the morphism considered in (ii) is covering for the étale topology. Comparing with 4.2.1 (ii), one deduces that it
is smooth and surjective. On the other hand, an immediate reasoning shows that the equivalence relation defined on
`P ×_S Q` by the morphism `P ×_S Q → G` is the equivalence relation associated with the action of the group
`R = P ∩ Q` (operating by `(p, q) r = (p r, r^{-1} q)`), which demonstrates the last assertion of (ii) (since a smooth
surjective morphism is an effective epimorphism, for example).

**Remark 4.2.6.** *If `P` and `Q` are in transversal position, one will often denote by `P · Q` the open subset
`Gen(Q/P)` of `G`, a notation justified by 4.2.5 (ii).*

<!-- label: III.XXVI.4.2.6 -->

**Proposition 4.2.7.** *Let `S` be a scheme, `G` an `S`-reductive group, `P` and `Q` two parabolic subgroups of `G`,
the pair `(P, Q)` being in transversal position.*

*(i) The group `P ∩ Q` is smooth over `S` (and in fact has connected fibers by 4.1.2); introducing then `(P ∩ Q)^0`
(cf. Exp. VI_B 3.10), this is a subgroup of type (RC) of `G` (Exp. XXII, 5.11.1), whose unipotent radical (loc. cit.
5.11.4) decomposes as a direct product*

```text
rad^u((P ∩ Q)^0) = (rad^u(P) ∩ Q) ×_S (P ∩ rad^u(Q)).
```

*(ii) If `S` is affine, `H^1(S, rad^u((P ∩ Q)^0)) = 0`. If `S` is semi-local, `P ∩ Q` contains a maximal torus of `G`.*

<!-- label: III.XXVI.4.2.7 -->

Indeed, `P ∩ Q` is smooth by 4.2.1 (ii) and the cartesian diagram

```text
P ×_S Q ─────→ G
   ↑           ↑
   │           │
   P ∩ Q ─────→ S.
```

<!-- original page 463 -->

To verify the announced assertions on `(P ∩ Q)^0`, one may reason locally for the étale topology, hence by 4.2.1 (vii)
assume to have chosen a splitting `(G, T, M, R)` of `G`, such that `P` and `Q` contain `T` and are defined respectively
by subsets `R_1` and `R_2` of `R`, `R_1` containing a system of positive roots `R^+`, and `R_2` containing the opposite
system `R^−`. Let `Δ` be the set of simple roots of `R^+`; denote

```text
A_1 = Δ ∩ −R_1,        A_2 = Δ ∩ R_2,        A = A_1 ∩ A_2.
```

By 1.4 (v) and 1.12, one has

```text
R_1 = R^+ ∪ (R^− ∩ −ℕA_1),         R_2 = (R^+ ∩ ℕA_2) ∪ R^−,
rad^u(P) = ∏_{α ∈ R_1, α ∉ −R_1} U_α,    rad^u(Q) = ∏_{α ∈ R_2, α ∉ −R_2} U_α.
```

By Exp. XXII, 5.6.7, one therefore has

```text
rad^u(P) ∩ Q = ∏_{α ∈ R_1 ∩ R_2, α ∉ −R_1} U_α = ∏_{α ∈ K_2} U_α,
rad^u(Q) ∩ P = ∏_{α ∈ R_1 ∩ R_2, α ∉ −R_2} U_α = ∏_{α ∈ K_1} U_α,
```

where `K_2` is the set of positive roots that are linear combinations of the elements of `A_2`, but not linear
combinations of the elements of `A`, and `K_1` the set of negative roots that are linear combinations of the elements
of `A_1`, but not linear combinations of the elements of `A`. It is clear that if `α ∈ K_2`, `β ∈ K_1`, `α + β` is
never a root, nor zero, which entails that the two groups above commute.

On the other hand, one knows by Exp. XXII, 5.4.5, that `H = (P ∩ Q)^0` is defined by the set of roots `R_1 ∩ R_2`,
namely

<!-- original page 464 -->

```text
R_1 ∩ R_2 = (R^+ ∩ ℕA_2) ∪ (R^− ∩ −ℕA_1).
```

Since `R_1 ∩ R_2` is closed, `H` is of type (RC) by definition (Exp. XXII 5.11.1), and by *loc. cit.* 5.11.3 and
5.11.4, one has

```text
rad^u(H) = ∏_{α ∈ K} U_α,
```

where `K` is the set of `α ∈ R_1 ∩ R_2` such that `α ∉ −(R_1 ∩ R_2)`. As the symmetric part of `R_1 ∩ R_2` is evidently
`R ∩ ℤA`, one sees at once that `K = K_1 ∪ K_2`, which completes the proof of (i).

The first assertion of (ii) then follows from (i) and 2.10; let us demonstrate the second. Since
`(P ∩ Q)^0 / rad^u((P ∩ Q)^0)` is reductive, it has a maximal torus `T̄` if the base is semi-local. The inverse image
of `T̄` in `(P ∩ Q)^0` is a subgroup `N` of type (R) of `G` with solvable fibers, and one has
`N^u = rad^u((P ∩ Q)^0)` (Exp. XXII, 5.6.9). The scheme of maximal tori of `N` is a principal homogeneous bundle under
`N^u` (*loc. cit.* 5.6.13), hence has a section, since `H^1(S, N^u) = 0`.

### 4.3. Opposite parabolic subgroups

<!-- label: III.XXVI.4.3 -->

### 4.3.1.

<!-- label: III.XXVI.4.3.1 -->

If `G` is an `S`-reductive group, one has defined in Exp. XXIV, 3.16.6, a canonical "outer automorphism" `s_G` of order
`⩽ 2`[^N.D.E-XXVI-20] of `G`, hence a canonical automorphism of order `⩽ 2` of `Dyn(G)`, hence also an automorphism of
order `⩽ 2` of `Of(Dyn(G))`, which we shall also denote `s_G` or simply `s`. Two types of parabolic subgroups
`t, t' ∈ Of(Dyn(G))(S)` will be said to be *opposite* when `t = s_G(t')`.

**Theorem 4.3.2.** *Let `S` be a scheme, `G` an `S`-reductive group, `P` a parabolic subgroup of `G`.*

*(a) If `L` is a Levi subgroup of `P`, there exists a unique parabolic subgroup `P'` of `G` such that `P ∩ P' = L`.*

<!-- original page 465 -->

*(b) For every parabolic subgroup `Q` of `G`, the following conditions are equivalent:*

*(i) For every `s ∈ S`, `((P ∩ Q)_s)^0` (which is smooth by 4.1.1) is reductive.*

*(ii) `P ∩ Q` is a Levi subgroup of `P` and of `Q`.*

*(iii) `P` and `Q` are of opposite types, and the pair `(P, Q)` is in transversal position (cf. 4.2.3).*

*(iv) `P` and `Q` are of opposite types and `rad^u(P) ∩ Q = e`.*

*(v) `rad^u(P) ∩ Q = rad^u(Q) ∩ P = e`.*

*(vi) The canonical morphism `rad^u(P) ×_S Q → G` is an open immersion.*

*(vi') The canonical morphism `rad^u(P) → G/Q` is an open immersion.*

*(vii) There exists a covering family for the étale topology `{ S_i → S }`, and for each `i` a splitting
`(T_i, M_i, R_i)` of `G_{S_i}`, and a subset `R_i^{(1)}` of `R_i` such that `P_{S_i}` (resp. `Q_{S_i}`) is the subgroup
of type (R) of `G_{S_i}` containing `T_i` and defined by `R_i^{(1)}` (resp. by `R_i^{(2)} = −R_i^{(1)}`).*

<!-- label: III.XXVI.4.3.2 -->

*Proof.* Let us first demonstrate the second part of the theorem; one sees first that (iii) ⇔ (vii) by 4.2.1 (vii) and
the definition of `s_G` in the split case (Exp. XXII, 3.16.2 (iv)); one trivially has (ii) ⇒ (i); one has (vi') ⇒ (vi)
by base change `G → G/Q`.

<!-- original page 466 -->

Now suppose (vii) holds, and let us prove all the other conditions; as they are local for the étale topology, one may
assume `G = (G, T, M, R)` split, `P` defined by the part `R'` of `R` and `Q` by the part `−R'`. If `L` is the subgroup
of type (R) of `G` containing `T` defined by `R' ∩ −R'`, it is clear by Exp. XXII, 5.11.3 that `L` is a Levi subgroup
common to `P` and `Q`. But `P = L · rad^u(P)`, `Q = L · rad^u(Q)`, and by Exp. XXII, 5.6.7, `rad^u(P) ∩ Q =
Q ∩ rad^u(P) = e`; hence `P ∩ Q = L`, and we have proved (ii) and (v). Since `P` and `Q` are in transversal position,
the canonical morphism `P → G/Q` induces an open immersion `P / P ∩ Q → G/Q` (4.2.1); but the canonical morphism
`rad^u(P) → P / P ∩ Q = P / L` is an isomorphism, so we have proved (vi'). In view of what was already seen, all
assertions are therefore consequences of (vii).

It now suffices to prove that any one of the assertions (i), (iv), (v), (vi) implies (vii); as we have already proved
the equivalence of (ii) and (iii), it suffices to give the proof on geometric fibers, and one may assume that `S` is
the spectrum of an algebraically closed field. By 4.1.1, there exists a maximal torus `T` of `G` contained in `P ∩ Q`.
Let `R` (resp. `R_1`, resp. `R_2`) be the set of roots of `G` (resp. `P`, resp. `Q`) relative to `T`.

Let `R_1^a` be the asymmetric part of `R_1` (i.e. `R_1^a = { α ∈ R_1 | −α ∉ R_1 }`). Introduce `R_2^a` similarly. We
must prove that `R_1 = −R_2`.

– Condition (i) entails that `R_1 ∩ R_2` is symmetric; let `α ∈ R_1`; if `α ∉ R_2`, then `α ∈ −R_2`, and if
`α ∈ R_2`, then `α ∈ R_1 ∩ R_2 = −(R_1 ∩ R_2) ⊂ −R_2`; one therefore has `R_1 ⊂ −R_2`, hence by symmetry
`R_1 = −R_2`.

– Condition (iv) entails `Card(R_1) = Card(R_2)` and `R_1^a ∩ R_2 = ∅`; the second condition is equivalent to
`R_2 ⊂ −R_1`; the first then gives `R_2 = −R_1`.

– Condition (v) entails `R_1^a ∩ R_2 = R_2^a ∩ R_1 = ∅`, hence `R_2 ⊂ −R_1` and `R_1 ⊂ −R_2`, which again gives
`R_2 = −R_1`.

– Condition (vi) entails `Lie(rad^u(P)) ⊕ Lie(Q) = Lie(G)`, which entails that `R` is the disjoint union of `R_2` and
<!-- original page 467 -->
`R_1^a`, hence that `R_2 = −R_1`.

This completes the proof of the second part of the theorem. Let us prove the first; let us first remark that, by virtue
of (vii) ⇒ (ii), we have already proved the existence locally for the étale topology of the sought group `P'`; it
therefore remains to prove its uniqueness, and this can also be done locally for the étale topology. One may therefore
assume `G` split relative to a maximal torus `T` of `L`, and `P` (resp. `P'`) defined by a part `R_1` (resp. `R'_1`) of
the root system `R`.

By hypothesis `R_1 ∩ R'_1` is symmetric; reasoning as above, one derives `R'_1 = −R_1`, which proves that `P'` is
determined by `P` and `L` and completes the proof.

**Definition 4.3.3.** *Two parabolic subgroups of `G` satisfying the equivalent conditions (i) to (vii) of 4.3.2 are
said to be* opposite. *If `P` is a parabolic subgroup of `G`, and if `L` is a Levi subgroup of `P` (resp. and if `T` is
a maximal torus of `P`), one calls* parabolic subgroup opposite to `P` relative to `L` (resp. `T`) *the unique parabolic
subgroup `Q` of `G` such that `P ∩ Q = L` (resp. such that `P ∩ Q` is the unique Levi subgroup of `P` containing `T`,
cf. 1.6, or, equivalently, such that `P ∩ Q` contains `T` and that `P` and `Q` are opposite).*

<!-- label: III.XXVI.4.3.3 -->

By 4.3.2 (iii), one derives from 4.2.4 and 4.2.5 parallel results; let us give one sample.

**Corollary 4.3.4.** *Let `S` be a scheme, `G` an `S`-reductive group, `P` and `Q` two parabolic subgroups of `G`.*

<!-- original page 468 -->

*(i) For `P` and `Q` to be opposite, it is necessary and sufficient that for every point `s ∈ S`, `P_s` and `Q_s` be
opposite. If `S' → S` is a surjective morphism, and if `P_{S'}` and `Q_{S'}` are opposite, then `P` and `Q` are
opposite.*

*(ii) The functor `Opp(G)`, such that for `S' → S`, `Opp(G)(S')` is the set of pairs of opposite parabolic subgroups of
`G_{S'}`, is representable by an open subscheme of `Par(G)^2`. The functor `Opp(/P)` such that for `S' → S`,
`Opp(/P)(S')` is the set of parabolic subgroups of `G_{S'}` opposite to `P_{S'}`, is representable by a universally
schematically dense open subscheme over `S`[^N.D.E-XXVI-21] of `Par_{s(t(P))}(G)`.*

*(iii) Suppose `P` and `Q` are opposite; let `P'` and `Q'` be two parabolic subgroups of `G`, `P'` being of the same
type as `P`. For `P'` and `Q'` to be opposite, it is necessary and sufficient that locally for the étale topology, the
pair `(P', Q')` be conjugate to the pair `(P, Q)`. (N. B. One shall see in §5 that the étale topology can be replaced
by the Zariski topology.)*

<!-- label: III.XXVI.4.3.4 -->

**Corollary 4.3.5.** *Let `S` be a scheme, `G` an `S`-reductive group, `P` a parabolic subgroup of `G`.*

<!-- original page 469 -->

*(i) The morphism `Opp(/P) → Lev(P)` (cf. 1.9) defined set-theoretically by `Q ↦ P ∩ Q`, is an isomorphism; `Opp(/P)`
is a principal homogeneous bundle under `rad^u(P)` (`rad^u(P)` operating by inner automorphisms). If `S` is affine,
there exists a parabolic subgroup of `G` opposite to `P`.*

*(ii) Suppose `S` semi-local; let `{s_i}` be the set of its closed points; for each `i`, let `Q_i` be a parabolic
subgroup of `G_{s_i}`, opposite to `P_{s_i}`. There exists a parabolic subgroup `Q` of `G`, opposite to `P`, and such
that `Q_{s_i} = Q_i` for each `i`.*

*(iii) The morphism `Opp(G) → PL` (cf. 3.15) defined set-theoretically by `(P, Q) ↦ (P, P ∩ Q)` is an isomorphism.*

<!-- label: III.XXVI.4.3.5 -->

All this follows from the first part of the theorem and from 1.9, 2.3 and 2.8.

**Remark 4.3.6.** *Let `P` and `Q` be two opposite parabolic subgroups of `G`, and let `P · Q` be the open subscheme of
`G`, sheaf-theoretic image of `P ×_S Q`, introduced in 4.2.6. The "product morphism" `G ×_S G → G` induces
isomorphisms:*

```text
rad^u(P) ×_S Q ⥲ P · Q ⥲ P ×_S rad^u(Q).
```

<!-- label: III.XXVI.4.3.6 -->

This follows indeed from 4.3.2 (or 4.2.5 (ii)) and from the fact that `P ∩ Q` is a Levi subgroup of `P` and of `Q`,
hence that `P = rad^u(P) · (P ∩ Q)` and `Q = rad^u(Q) · (P ∩ Q)`.

<!-- original page 470 -->

One has similarly a commutative diagram

```text
rad^u(P) ─────→ G/Q
   ≀               ≀
Opp(/P) ──────→ Par_{t(Q)}(G),
```

where the vertical arrows are induced by `g ↦ int(g) Q`.

### 4.4. Osculating position

<!-- label: III.XXVI.4.4 -->

**Proposition 4.4.1.** *Let `S` be a scheme, `G` an `S`-reductive group, `P` and `Q` two parabolic subgroups of `G`. The
following conditions are equivalent:*

*(i) `P ∩ Q` is a parabolic subgroup of `G`.*

*(ii) `P ∩ Q` contains locally for the étale topology a Borel subgroup of `G`.*

*(iii) `P ∩ Q` contains locally for the étale topology a maximal torus of `G`, and, for every `S' → S` and every
maximal torus `T` of `G_{S'}` contained in `P_{S'}` and `Q_{S'}`, the opposite of `P_{S'}` relative to `T` is in
transversal position relative to `Q_{S'}`.*

*(iv) There exists a covering family for the étale topology `{ S_i → S }`, and for each `i` a maximal torus `T_i` of
`G_{S_i}` contained in `P_{S_i}` and `Q_{S_i}`, and such that the opposite of `P_{S_i}` relative to `T_i` is in
transversal position relative to `Q_{S_i}`.*

<!-- original page 471 -->

*(v) There exists a covering family for the étale topology `{ S_i → S }`, and for each `i` a splitting
`(T_i, M_i, R_i)` of `G_{S_i}` such that `P_{S_i}` (resp. `Q_{S_i}`) is the subgroup of type (R) of `G_{S_i}`
containing `T_i` and defined by a set of roots `R_i^{(1)}` (resp. `R_i^{(2)}`), `R_i^{(1)} ∩ R_i^{(2)}` containing a
system of positive roots of `R`.*

*Moreover, if these conditions are satisfied, one has `t(P ∩ Q) = t(P) ∩ t(Q)` (with the notations of 3.2).*

<!-- label: III.XXVI.4.4.1 -->

One has (v) ⇒ (ii) and (iii) ⇒ (iv) trivially. On the other hand, (ii) ⇒ (i) by 1.18. One has (iv) ⇒ (v): indeed, one
may assume `G` split, `P` (resp. `Q`) defined by the set of roots `R_1` (resp. `R_2`); the opposite of `P` is then
defined by `−R_1`, and one is reduced to Lemma 4.2.2. One proves (i) ⇒ (iii) by splitting, in the same way. Finally,
the last assertion of the theorem can be proved locally for the étale topology; one may assume that `P ∩ Q` contains
a Borel subgroup `B` of `G`, and one is reduced to 3.7.

**Definition 4.4.2.** *Two parabolic subgroups of `G` satisfying conditions (i) to (v) of 4.4.1 are said to be in*
osculating position.

<!-- label: III.XXVI.4.4.2 -->

**Corollary 4.4.3.** *Let `P` and `Q` be two parabolic subgroups in osculating position, and let `P'` and `Q'` be two
parabolic subgroups of `G`, of the same type as `P` and `Q` respectively. For `P'` and `Q'` to be in osculating
position, it is necessary and sufficient that the pair `(P', Q')` be conjugate to the pair `(P, Q)`, locally for the
étale topology.*

<!-- original page 472 -->

<!-- label: III.XXVI.4.4.3 -->

It suffices to prove that if `P` and `P'` are in osculating position with respect to `Q`, they are conjugate, locally
for (ét), by a section of `Q`. Now `P ∩ Q` and `P' ∩ Q` are two parabolic subgroups of the same type contained in `Q`,
hence are conjugate locally for (ét) by a section of `Q`, by part (ii) of the lemma below. One may therefore assume
`P ∩ Q = P' ∩ Q`; one then has `P = P'`, by part (i) of the same lemma:

**Lemma 4.4.4.** *Let `P, P'` and `Q` be three parabolic subgroups of the `S`-reductive group `G`.*

*(i) For `P = P'`, it is necessary and sufficient that `P` and `P'` be in osculating position and of the same type.*

*(ii) If `P ⊂ Q`, `P' ⊂ Q`, and if `g ∈ G(S)` is such that `int(g) P` and `P'` are in osculating position, then
`g ∈ Q(S)`.*

<!-- label: III.XXVI.4.4.4 -->

Part (i) follows trivially from the last assertion of 4.4.1. Let us demonstrate (ii): `Q` and `int(g) Q` contain
`P' ∩ int(g) P`, hence are in osculating position; they coincide by (i), hence `g ∈ Norm_G(Q)(S) = Q(S)`.

Let us remark that assertions (iii) and (iv) of the theorem immediately yield:

<!-- original page 473 -->

**Corollary 4.4.5.** *Let `P, P'` and `Q` be three parabolic subgroups of the `S`-reductive group `G`, containing the
same maximal torus `T` of `G`. Suppose `P` and `P'` opposite relative to `T`. For `Q` to be in osculating position
relative to `P`, it is necessary and sufficient that it be in transversal position relative to `P'`. Under these
conditions `P ∩ Q` is also in transversal position relative to `P'`.*

<!-- label: III.XXVI.4.4.5 -->

**Corollary 4.4.6.** *Let `P` and `Q` be two parabolic subgroups of `G` containing the same maximal torus `T`. For `P`
and `Q` to be in transversal position, it is necessary and sufficient that there exist two parabolic subgroups
`P' ⊂ P` and `Q' ⊂ Q` of `G`, opposite relative to `T`; one may even choose `t(P') = t(P) ∩ s(t(Q))`.*[^N.D.E-XXVI-22]

<!-- label: III.XXVI.4.4.6 -->

The condition is evidently sufficient (4.2.1 (i) and 4.3.2 (iii)). Let us show that it is necessary; let `P^−`
(resp. `Q^−`) be the opposite of `P` (resp. `Q`) relative to `T`. By 4.4.5, `P^− ∩ Q` is in transversal position
relative to `P` and `Q^−`, hence also relative to `P ∩ Q^−` by a further application of 4.4.5; moreover

```text
t(P^− ∩ Q) = t(P^−) ∩ t(Q) = s(t(P)) ∩ s(t(Q^−)) = s(t(P) ∩ t(Q^−)) = s(t(P ∩ Q^−)),
```

<!-- original page 474 -->

hence `P^− ∩ Q = P'` and `P ∩ Q^− = Q'` are opposite (4.3.2 (iii)); but `P' ∩ Q' ⊃ T`, hence they are indeed opposite
relative to `T`.

### 4.5. Standard position

<!-- label: III.XXVI.4.5 -->

In this section, we briefly indicate how some of the preceding results generalize.

**Proposition 4.5.1.** *If `P_1` and `P_2` are two parabolic subgroups of the `S`-reductive group `G`, the following
conditions are equivalent:*[^N.D.E-XXVI-23]

*(i) `P_1 ∩ P_2` is smooth.*

*(ii) `P_1 ∩ P_2` is a subgroup of type (R) (or of type (RC)) of `G`.*

*(iii) `P_1 ∩ P_2` contains locally for the (fpqc) topology a maximal torus of `G`.*

*(iv) `P_1 ∩ P_2` contains locally for the Zariski topology a maximal torus of `G`.*

*When `S` is semi-local, these conditions are moreover equivalent to:*

*(v) `P_1 ∩ P_2` contains a maximal torus of `G`.*

<!-- label: III.XXVI.4.5.1 -->

*Proof.*[^N.D.E-XXVI-23] Evidently, (iv) ⇒ (iii) (and (v) ⇒ (iv) when `S` is semi-local), and (ii) ⇒ (i) according to
Exp. XXII, Def. 5.2.1. We shall show (i) ⇒ (ii) ⇒ (iii), then that (iii) entails (i) and (iv) (and also (v) when `S` is
semi-local). Set `K = P_1 ∩ P_2`. By 4.1.1 and [BT65], 4.5, each geometric fiber `K_s` contains a maximal torus `T_s`
of `G_s` and is connected, and the set of roots of `K_s` with respect to `T_s` is a closed subset of the set of roots
of `G_s` with respect to `T_s`. Hence, if `K` is smooth over `S`, then it is a subgroup of type (RC) (hence a fortiori
of type (R)), cf. Exp. XXII 5.2.1 and 5.11.1. We therefore have (i) ⇔ (ii).

If `K` is a subgroup of type (R), it contains locally for the étale topology a maximal torus of `G`, by Exp. XXII 2.2
and Exp. XIX 6.1. So (ii) ⇒ (iii).

Suppose (iii) holds and let us show that `K` is smooth. By (fpqc) descent, one may assume that `G = (G, T, M, R)` is
split, where `T` is a maximal torus contained in `P ∩ Q`, and that there exist two closed subsets `R_1` and `R_2` of
`R` such that `P = H_{R_1}` and `Q = H_{R_2}`.

<!-- original page 311 source / page 475 -->

Since `K` has connected fibers, it follows from Exp. XXII 5.4.5 that `K` equals `H_{R_1 ∩ R_2}`, hence is smooth over
`S` and of type (RC).

Let `R_1^s` be the symmetric part of `R_1` and `R_1^a = R_1 − R_1^s`; then `rad^u(P_1) = H_{R_1^a}`. As noted in the
proof of [BT65], 4.4, `R' = (R_1^s ∩ R_2) ∪ R_1^a` is a closed subset of `R` such that `R' ∪ (−R') = R`; hence, by
Exp. XXI 3.3.6, `R'` contains a system of positive roots of `R`. Moreover, the symmetric part of `R'` is
`R_1^s ∩ R_2^s`, which is contained in `R_1 ∩ R_2`.

It follows from the preceding that `P' = K · rad^u(P)` is a parabolic subgroup of `G`, and that `K` is a subgroup of
type (RC) of `P'` such that `rad^u(K) = K ∩ rad^u(P')`. Hence, by 2.11, `K` has a Levi subgroup `L`. It then follows
from Exp. XIV 3.20 and 3.21 that `K` satisfies assertion (iv), as well as assertion (v) when `S` is semi-local. This
proves 4.5.1.

**Definition 4.5.1.1.**[^N.D.E-XXVI-24] *When the preceding conditions are satisfied, one says that `P` and `Q` are in*
mutual standard position; *this is, for instance, the case if `P` and `Q` are in transversal position, or in osculating
position, or if the base is the spectrum of a field. It is a notion stable under base extension and local for the
(fpqc) topology.*

<!-- label: III.XXVI.4.5.1.1 -->

### 4.5.2.

<!-- label: III.XXVI.4.5.2 -->

Let `(P, Q)` and `(P', Q')` be two pairs of parabolic subgroups of `G`, in standard position, and let `H` be the
subfunctor of `G` defined as follows: `H(S')` is the set of `g ∈ G(S')` such that `int(g) P = P'` and `int(g) Q = Q'`.
It is a closed subscheme of `G`, smooth over `S` and formally principal homogeneous under `P ∩ Q`. One deduces that the
following conditions are equivalent:

(i) `(P, Q)` and `(P', Q')` are conjugate locally for the (fpqc) topology,

(ii) `(P, Q)` and `(P', Q')` are conjugate locally for the étale topology.

(iii) `(P, Q)` and `(P', Q')` are conjugate on each geometric fiber.

One then says that the pairs `(P, Q)` and `(P', Q')` have the same *type of mutual position*. This is a notion stable
under base change and local for the (fpqc) topology.

### 4.5.3.

<!-- label: III.XXVI.4.5.3 -->

Let `Stand(G)` be the subfunctor of `Par(G) ×_S Par(G)` "formed of pairs in mutual standard position". Then `Stand(G)`
is representable, there exists an étale finite `S`-scheme `TypeStand` ("scheme of types of mutual standard position"),
and a morphism, smooth, of finite presentation, with irreducible geometric fibers (and hence in particular faithfully
flat)

```text
t_2 : Stand(G) ⟶ TypeStand
```

<!-- original page 476 -->

which is a quotient of `Stand(G)` by the action of `G`: two sections of `Stand(G)` (over an arbitrary `S' → S`) have the
same type of mutual position if and only if they have the same image under `t_2`. One has a commutative diagram

```text
Stand(G) ────────t_2────→ TypeStand
   │                          │
   │                          │ q
   ▼                          ▼
Par(G) ×_S Par(G) ─t × t─→ Of(Dyn(G)) ×_S Of(Dyn(G)),
```

where the morphism `q` may be described by descent as follows: if `(P, Q)` is a pair of parabolic subgroups of `G` in
mutual standard position, and if `T` is a maximal torus of `P ∩ Q`, then the morphism `Norm_G(T) → Stand(G)` defined
set-theoretically by `n ↦ (P, int(n) Q)` induces an isomorphism

```text
W_P(T) \ W_G(T) / W_Q(T) ≃ q^{−1}(t(P), t(Q)).
```

(The left-hand side denotes the sheaf of double cosets …). These assertions are proved without difficulty (remark in
particular that `t_2^{−1}(t_2(P, Q)) ≃ G / (P ∩ Q)`).

### 4.5.4.

<!-- label: III.XXVI.4.5.4 -->

Now let `P` be a fixed parabolic subgroup of `G`, and let `Par(G; P)` be the functor of parabolic subgroups of `G` in
standard position relative to `P`. For each `t ∈ Of(Dyn(G))(S)`, set similarly
`Par_t(G; P) = Par(G; P) ∩ Par_t(G)`. One sees at once that the two preceding functors are obtained from `Stand(G)` by
<!-- original page 477 -->
fibered products, and are therefore representable by `S`-schemes that are smooth and of finite presentation over `S`,
with non-empty fibers. One has a canonical morphism `t_P` induced by `t_2` (i.e. `t_P(Q) = t_2(P, Q)`)

```text
t_P : Par_t(G; P) ⟶ q^{−1}(t(P), t)
```

which is smooth and of finite presentation, with irreducible geometric fibers. The canonical morphism
`Par_t(G; P) → Par_t(G)` is a surjective monomorphism, and may therefore be considered as a *cellular decomposition* of
`Par_t(G)` (indexed by the set of connected components of `q^{−1}(t(P), t)`).

### 4.5.5.

<!-- label: III.XXVI.4.5.5 -->

Suppose now that the type `t` is of the form `t(Q)`, where `Q` is a parabolic subgroup of `G` in standard position
relative to `P`, and that `P ∩ Q` contains a maximal torus `T`.

Then `Par_t(G) ≃ G/Q` and `q^{−1}(t(P), t) ≃ W_P(T) \ W_G(T) / W_Q(T)`, which gives a diagram

```text
Par_{t(Q)}(G; P) ──f──→ W_P(T) \ W_G(T) / W_Q(T)
   │
 i │
   ▼
Par_{t(Q)}(G) ─────────⥲────→ G/Q
```

where `i` is a surjective monomorphism, and where `f` is smooth and of finite presentation, with irreducible geometric
fibers. Moreover, if `Q_1` and `Q_2` are two sections of `Par_{t(Q)}(G; P)` (over an `S' → S`), i.e. two parabolic
<!-- original page 478 -->
subgroups of `G_{S'}` conjugate (locally for (fpqc)) to `Q`, and in standard position relative to `P_{S'}`, then `Q_1`
and `Q_2` are conjugate by a section of `P` (locally for (fpqc)) if and only if `f(Q_1) = f(Q_2)`. If `S` is the
spectrum of an algebraically closed field `k`, one thereby finds the relation

```text
P(k) \ G(k) / Q(k) ≃ W_P(T)(k) \ W_G(T)(k) / W_Q(T)(k).
```

More generally, if one assumes that the scheme `W_P(T) \ W_G(T) / W_Q(T)` is constant and of the form `E_S` (which
happens, for instance, when `G` is split relative to `T` and `S` is connected), the `f^{−1}(e)`, `e ∈ E`, form a
decomposition of `Par_{t(Q)}(G; P)` into open and closed subschemes, which are homogeneous spaces under `P`, smooth and
of finite presentation over `S`, with irreducible geometric fibers.

### 4.5.6.

<!-- label: III.XXVI.4.5.6 -->

Let us return to the general situation of 4.5.4. The scheme `q^{−1}(t(P), t)`[^N.D.E-XXVI-25] always has two
distinguished sections, corresponding respectively to the types "transversal position" and "osculating position". The
inverse image of the first section is a relatively dense open subscheme of `Par_t(G; P)`, as one has seen above; it is
the cell of maximum relative dimension of the decomposition.

The inverse image of the second section is presumably a closed subscheme of `Par_t(G; P)`; it is the cell of minimum
relative dimension of the decomposition.

## 5. Conjugacy theorem

<!-- label: III.XXVI.5 -->

<!-- original page 479 -->

**Theorem 5.1.** *Let `S` be a semi-local scheme, `G` an `S`-reductive group, `P` and `P'` two opposite parabolic
subgroups (4.3.3) of `G`. Then*

```text
rad^u(P)(S) · P' · P = G,
```

*i.e. the union of the open subsets `u P' · P` (4.3.6), for `u` running through `rad^u(P)(S)`, is all of `G`.*

<!-- label: III.XXVI.5.1 -->

The proof is carried out in several steps:

### 5.1.1.

<!-- label: III.XXVI.5.1.1 -->

It suffices to give the proof in the case where `S` is the spectrum of a field `k`; this follows at once from 2.6.

### 5.1.2.

<!-- label: III.XXVI.5.1.2 -->

Let `L = P ∩ P'`. Suppose `L` has a Borel subgroup `B_L`; let `T` be a maximal torus of `B_L` (Exp. XXII, 5.9.7); one
verifies at once that `B = B_L · rad^u(P)` is a Borel subgroup of `P`; let `B'` be the Borel subgroup of `G` opposite to
`B` relative to `T` (i.e. such that `B ∩ B' = T`). One has `B' ⊂ P'` as one verifies at once by splitting `G` relative
to `T`. Let us prove that

```text
(x)    B^u(S) · B' · B ⊂ rad^u(P)(S) · P' · P.
```

Since one has `B^u(S) ⊂ P(S) = rad^u(P)(S) · L(S) ⊂ rad^u(P)(S) · P'(S)`, it suffices to prove that
`B' · B ⊂ P' · P`, which is evident. It follows from (x) that it suffices to prove 5.1
<!-- original page 480 -->
for the pair `(B, B')`.

### 5.1.3.

<!-- label: III.XXVI.5.1.3 -->

The theorem is true if `k` is algebraically closed; indeed, the condition of 5.1.2 is satisfied, and one concludes by
Exp. XXII, 5.7.10.

### 5.1.4.

<!-- label: III.XXVI.5.1.4 -->

The theorem is true when `k` is an infinite field. Indeed, `rad^u(P)(k)` is dense in `rad^u(P)(k̄)` by 2.7, and the
theorem is true for `k̄`.

### 5.1.5.

<!-- label: III.XXVI.5.1.5 -->

We are therefore reduced to the case where `k` is a finite field. Now `Bor(L)` is a smooth homogeneous space of `L`; it
follows from Lang's theorem (Am. J. of Maths., 78, 1956[^N.D.E-XXVI-26]) that `L` has a Borel subgroup `B_L`. By 5.1.2,
one may therefore assume that `P = B` and `P' = B'` are Borel subgroups. One writes `T = B ∩ B'`.

### 5.1.6.

<!-- label: III.XXVI.5.1.6 -->

Let `K` be the algebraic closure of `k`; choose a pinning of the triple `(G_K, B_K, T_K)`, let `R^+` (resp. `Δ`) be the
set of positive roots (resp. simple). By Exp. XXII, 5.7.2, it suffices to prove that for every `α ∈ Δ`, one has

```text
(1)    u_α B'^u(K) ⊂ B^u(k) · B'^u(K) · B(K).
```

Let `α_i` be the various roots conjugate to `α` over `k` (these are elements of `Δ`, since `B` is "defined over `k`"),
and let `R'` be the set of roots that are linear combinations of the `α_i`. Set `R'^− = R^− ∩ R'`. As "`R'` is defined
<!-- original page 481 -->
over `k`", there exists a subtorus `Q` of `T` such that `Q_K` is the maximal torus of the common kernel of the `α_i`.

Set `Z = Centr_G(Q)`, `B_Z = B ∩ Z`, `B'_Z = B' ∩ Z` (cf. Exp. XXII, 5.10.2). Let us show that it suffices to verify
the sought assertion in `Z`, that is

```text
(2)    u_α · B'^u_Z(K) ⊂ B^u_Z(k) · B'^u_Z(K) · B_Z(K).
```

One has `(B'^u_Z)_K = ∏_{α ∈ R'^−} U_α`; let `R''` be the complement of `R'` in `R`, and set

```text
V = ∏_{α ∈ R'' ∩ R^−} U_α.
```

One immediately has `(B'^u)_K = (B'^u_Z)_K · V`, and `(B_Z)_K` normalizes `V` (Exp. XXII, 5.6.7). One therefore derives
from (2) successively

```text
u_α · B'^u(K) = u_α · B'^u_Z(K) V(K) ⊂ B^u_Z(k) B'^u_Z(K) B_Z(K) V(K)
                                     ⊂ B^u_Z(k) B'^u_Z(K) V(K) B_Z(K),
```

which yields (1) at once.

We are therefore reduced to the case where `G = Z`, that is, where the Galois group of `K` over `k` acts transitively
on the simple roots.

### 5.1.7.

<!-- label: III.XXVI.5.1.7 -->

<!-- original page 482 -->

The assertion to be proved is equivalent to the fact that `G/B` is the union of the translates by `B^u(k)` of the open
image of `B'^u`, an assertion that does not change if one replaces `G` by its adjoint group (or by any group yielding
the same adjoint group). One may therefore assume `G` adjoint.

### 5.1.8.

<!-- label: III.XXVI.5.1.8 -->

Consider then the Dynkin diagram of `G_K`. The Galois group acts transitively on this Dynkin diagram. But this Galois
group has only cyclic quotients, and the Dynkin diagram has no cycles. It follows immediately that this diagram is of
type `n A_1`, `n ⩾ 0`, or `m A_2`, `m ⩾ 0`. Using the canonical decomposition of Exp. XXIV, 5.9, one may write

```text
G = ∏_{D/K} G_0,
```

where `D` is a finite `K`-scheme and `G_0` is either a torus, of type `A_1`, or of type `A_2`.

By Exp. XXIV, 5.12, `B` comes from a Borel subgroup `B_0` of `G_0`, `T` from a maximal torus `T_0` of `G_0`; `B'` comes
from the Borel subgroup `B'_0` of `G_0` opposite to `B_0` relative to `T_0`. One has

```text
B'^u(k) = B^u_0(D),
B'^u · T · B^u = ∏_{D/k} B'^u_0 · T_0 · B^u_0,
```

and it suffices to prove the sought assertion for the triple `(G_0, B_0, T_0)`.

### 5.1.9.

<!-- label: III.XXVI.5.1.9 -->

<!-- original page 483 -->

One may therefore assume that `G` is of type `∅`, `A_1`, or `A_2`. Since `G` has a Borel subgroup `B`, `G` is
quasi-splittable relative to `B` (Exp. XXIV, 3.9.1), hence splittable if it is of type `∅` or `A_1`. Since the theorem
has already been proved in the split case (Exp. XXII 5.7.10), only the case `A_2` remains to be treated. By
Exp. XXIV, 3.11 there exists a morphism `E → Spec(k)`, principal Galois bundle under the group `ℤ/2ℤ` of automorphisms
of the Dynkin diagram of type `A_2`, such that `G = Q-Ép_{E/Spec(k)}(A_2)`. If `E` has a section, `G` is splittable and
the theorem is proved. Otherwise, one necessarily has `E = Spec(k')`, where `k'` is a quadratic extension of `k`.
Finally, as one saw in 5.1.7, one may assume `G` simply connected (i.e. that `G` is a form of `SL_{3, k}`).

### 5.1.10.

<!-- label: III.XXVI.5.1.10 -->

One is therefore in the following situation: one has a finite field `k`, a quadratic extension `k'` of `k`. The group
`SL_{3, k'}` of `3 × 3` matrices of determinant 1 is pinned as follows: the maximal torus is the group of diagonal
matrices, the Borel subgroup is the group of upper triangular matrices, the "pins" are the elements:

```text
u_α = ( 1 1 0 )       u_β = ( 1 0 0 )
      ( 0 1 0 )             ( 0 1 1 )
      ( 0 0 1 )             ( 0 0 1 ).
```

One sees at once that the big cell `Ω` is defined by

```text
( a b c )
( d e f ) ∈ Ω(S) ⇔ a and ae − bd are invertible,
( g h i )
```

<!-- original page 484 -->

and that

```text
B^u(k) = { ( 1 x z )                                            }
         { ( 0 1 x̄ ) :  x, z ∈ k',  z + z̄ = x x̄ }
         { ( 0 0 1 )                                            }.
```

We must prove inclusion (1) of 5.1.6, that is to say, show that for all `a, b, c ∈ K` (algebraic closure of `k`), there
exist `x, z ∈ k'` such that `z + z̄ = x x̄` and

```text
(1)    ( 1 x z ) ( 1 1 0 ) ( 1 0 0 )
       ( 0 1 x̄ ) ( 0 1 0 ) ( a 1 0 )  ⊂ Ω(K).
       ( 0 0 1 ) ( 0 0 1 ) ( b c 1 )
```

– If `a ≠ −1`, one takes `x = z = 0`.

– If `a = −1`, the conditions to be realized are written

```text
{ z + z̄ = x x̄,
{ b z − x ≠ 0,
{ (b + c) z + b x − 1 ≠ 0.
```

Let `q` be the number of elements of `k` (`q ⩾ 2`). One knows that for every `m ∈ k`, the equation `z + z̄ = m`, with
`z ∈ k'`, has `q` solutions.

– If `b = 0`, take `x = 1`; one must solve `z + z̄ = 1`, `c z ≠ 1`, which is always possible by the preceding remark.

– If `b ≠ 0`, take `x = 0`; one must solve

```text
z + z̄ = 0,    z ≠ 0,    (b + c) z ≠ 1.
```

This is always possible if `q ⩾ 3`. If `k = 𝔽_2`, it is possible if `b + c ≠ 1`; one may take `z = 1`.

<!-- original page 485 -->

– It remains to treat the case `k = 𝔽_2`, `b + c = 1`, `b ≠ 0`. The system is then written

```text
z + z̄ = x x̄,    b z ≠ x,    z + b x ≠ 1.
```

If `b = 1` (resp. `b ∉ k'`), let us take `x = 1`; then the last two conditions are written `z ≠ b^{−1}`, `1 − b`, and
they are consequences of `z + z̄ = 1`, which has solutions. Finally, if `b ∈ k' − k`, one may take `x = b`, `z = b̄`.
QED.

**Corollary 5.2.** *Let `S` be a semi-local scheme, `G` an `S`-reductive group, `P` and `P'` two opposite parabolic
subgroups of `G`. The canonical map*

```text
rad^u(P)(S) · rad^u(P')(S) ⟶ (G/P)(S)
```

*is surjective (in particular, one has `(G/P)(S) = G(S) / P(S)`). Every parabolic subgroup `Q` of `G`, of the same type
as `P`, is of the form `int(u u') P` with `u ∈ rad^u(P)(S)` and `u' ∈ rad^u(P')(S)`.*

<!-- label: III.XXVI.5.2 -->

The second assertion is evidently equivalent to the first; let us demonstrate the latter. Let `s_i` be the closed points
of `S`, let `V` be the open subscheme of `G/P` image of `P'` (and isomorphic to `rad^u(P')`, cf. 4.3.6), and let
`x ∈ (G/P)(S)`. By 5.1, there exists for each `i` a section `u_i ∈ rad^u(P)(κ(s_i))` such that `u_i x_{s_i}` is a
section of `V_{s_i}`. If `u ∈ rad^u(P)(S)` lifts the `u_i` (2.6), `u x` is a section of `V`, since such an assertion is
verified on the closed fibers. But `rad^u(P')(S) ⥲ V(S)` is bijective, and one concludes at once.

<!-- original page 486 -->

**Corollary 5.3.** *Let `S` be a semi-local scheme, `G` an `S`-reductive group, `P, P'` and `Q` three parabolic subgroups
of `G`. There exists `g ∈ G(S)` such that `int(g) Q` is in transversal position relative to `P` and `P'`.*

<!-- label: III.XXVI.5.3 -->

With the notation of 4.2.4 (ii), one must verify that the universally schematically dense open subscheme over
`S`[^N.D.E-XXVI-27] `Gen(Q/P) ∩ Gen(Q/P')` of `G` has a section over `S`. Let us in fact choose a parabolic subgroup of
`G` opposite to `Q` (4.3.5 (i)), say `Q_1`, and set `U = rad^u(Q)`, `U' = rad^u(Q_1)`. We shall show that there exists
`g ∈ U(S) U'(S)` answering the question; in this form, it follows from 4.2.4 (i) and 2.6 that it suffices to verify the
assertion on the fibers at the closed points of `S`, and one may therefore assume that `S` is the spectrum of a field
`k`.

If `k` is algebraically closed, there exists `g ∈ G(k)` answering the question; now `g` is written `u u' q` with
`u ∈ U(k)`, `u' ∈ U'(k)`, `q ∈ Q(k)` (5.2), and one has `int(u u') Q = int(g) Q`.

If `k` is infinite, consider the open subset `V` of `U ×_k U'` defined by the cartesian diagram

```text
U ×_k U' ─────→ G
   ↑               ↑
   │               │
   V ─────→ Gen(Q/P) ∩ Gen(Q/P');
```

since `V(k̄) ≠ ∅` by what was just seen, `V` is dense in `U ×_k U'`, hence has a section by 2.7.

If `k` is finite, `P` (resp. `P'`) has a Borel subgroup `B` (resp. `B'`), by virtue of
<!-- original page 487 -->
Lang's theorem (cf. 5.1.5), since the schemes `Bor(P) ≃ Bor(P/rad^u(P))` and `Bor(Q) ≃ Bor(Q/rad^u(Q))` are smooth. If
`B_1` is a Borel subgroup opposite to `B` (4.3.5 (i)), there exist `a ∈ B^u(k)` and `a_1 ∈ B_1^u(k)` such that
`int(a a_1) B = B'` (5.2); then `B_0 = int(a a_1) B_1 = int(a) B_1` is opposite to `B'` and to `B`; if `Q_0` is the
unique parabolic subgroup of `G` containing `B_0` and of the same type as `Q` (3.8), `Q_0` is in transversal position
relative to `P` and `P'` (4.2.1 (vi)). On the other hand, by 5.2, `Q_0` is written `int(u u') Q` with `u' ∈ U'(k)`,
`u ∈ U(k)`, which is what was to be demonstrated.

**Corollary 5.4.** *Let `S` be a semi-local scheme, `G` an `S`-reductive group, `P` and `Q` two parabolic subgroups of
`G`. There exists `g ∈ G(S)` such that `int(g) P` is in osculating position relative to `Q`, i.e. (4.4.2) that
`int(g) P ∩ Q` is a parabolic subgroup of `G`.*

<!-- label: III.XXVI.5.4 -->

Indeed, by 4.3.5 (i), there exists a parabolic subgroup `P'` of `G` opposite to `P`. By 5.3, there exists a parabolic
subgroup `P'_1` of `G` of the same type as `P'`, in transversal position relative to `P` and `Q`. If `T` is a maximal
torus of `P'_1 ∩ Q` (4.2.7 (ii)), and if `P_1` is the opposite of `P'_1` relative to `T`, then `P_1` and `Q` are in
osculating position, by 4.4.5. On the other hand, `P` and `P_1` being opposite to `P'_1`, there exists
`g ∈ rad^u(P'_1)(S)` such that `int(g) P = P_1` (4.3.5 (i)). QED.

<!-- original page 488 -->

Let us remark, moreover, that for the same reason there exists `u ∈ rad^u(P)(S)` such that `int(u) P' = P'_1`, hence
`g` is written `int(u) u'` with `u' ∈ rad^u(P')(S)`, which gives `P_1 = int(u u' u^{−1}) P = int(u u') P` and
re-proves 5.2 in passing.

Statements 5.3 and 5.4 are the essential results of this section. Let us first state some consequences of 5.4.

**Corollary 5.5.** *Let `S` be a semi-local scheme, `G` an `S`-reductive group.*

*(i) If `P` and `Q` are two parabolic subgroups of `G` and if `t(P) ⊂ t(Q)` (cf. 3.3), there exists `g ∈ G(S)` such that
`int(g) P ⊂ Q`.*

*(ii) Let*

```text
P_1 ⊃ P_2 ⊃ · · · · · · ⊃ P_n    and    P'_1 ⊃ P'_2 ⊃ · · · · · · ⊃ P'_n
```

*be two chains of parabolic subgroups of `G` such that `t(P_i) = t(P'_i)`. There exists `g ∈ G(S)` such that
`int(g) P_i = P'_i` for each `i`.*

*(iii) Let `P, Q, P', Q'` be four parabolic subgroups of `G` such that `t(P) = t(P')` and `t(Q) = t(Q')`. If the pairs
`(P, P')` and `(Q, Q')` are in transversal (resp. osculating) position, there exists `g ∈ G(S)` such that
`int(g) P = P'` and `int(g) Q = Q'`.*

<!-- original page 489 -->

*(iv) Let `P` and `P'` be two parabolic subgroups of the same type, `L` (resp. `L'`) a Levi subgroup of `P` (resp.
`P'`). There exists `g ∈ G(S)` such that `int(g) P = P'` and `int(g) L = L'`.*

<!-- label: III.XXVI.5.5 -->

*Proof:* (i) follows at once from 5.4; (ii) is proved by induction on `n`, the case `n = 0` being trivial; one may
therefore assume `P_i = P'_i` for `i = 1, …, n − 1`; by 5.2 there exists `g ∈ G(S)` such that `int(g) P_n = P'_n`; but
then `P_n` and `int(g) P_n` are contained in `P_{n−1} = P'_{n−1}`, hence `g ∈ P_{n−1}(S)` (4.4.4 (ii)) and
`int(g) P_i = P'_i` for `i = 1, …, n`.

On the other hand, (iv) follows at once from 5.2 and 1.8. Let us demonstrate (iii) in the case of "transversal
position"; the assertion is a consequence of (iv) when the types of `P` and `Q` are opposite (4.3.3 (iii)); in the
general case, by 4.2.7 (iii) and 4.4.6, one may find parabolic subgroups `P_1, P'_1, Q_1, Q'_1` of `P, P', Q, Q'`
respectively, such that `P_1` and `P'_1` are opposite, as are `Q_1` and `Q'_1`, and such that `t(P_1) = t(P'_1)`;
there therefore exists `g ∈ G(S)` such that `int(g) P_1 = P'_1`, `int(g) Q_1 = Q'_1`, and one may assume `P_1 = P'_1`
and `Q_1 = Q'_1`; but then `P` and `P'` are in osculating position and of the same type, hence `P = P'` (4.4.4 (i));
for the same reason `Q = Q'`.

It remains to demonstrate assertion (iii) in the case of "osculating position". By the conjugacy theorem (5.2), one
may assume `P = P'`; by the same theorem, one may find `g ∈ G(S)` such that `int(g) Q = Q'`; but then `g ∈ P(S)` by
4.4.4 (ii) and one has `int(g) P = P = P'`.

<!-- original page 490 -->

**Definition 5.6.** *Let `S` be a scheme, `G` an `S`-reductive group, `P` a parabolic subgroup of `G`. One says that
`P` is* minimal *if whenever `Q` is a parabolic subgroup of `G` contained in `P`, one has `Q = P`.*

<!-- label: III.XXVI.5.6 -->

One should note that this is not in general a notion stable under passage to fibers.

**Corollary 5.7.** *Let `S` be a semi-local scheme, `G` an `S`-reductive group.*

*(i) Let `t, t' ∈ Of(Dyn(G))(S)`. If there exist in `G` a parabolic subgroup of type `t` and a parabolic subgroup of
type `t'`, there exists a parabolic subgroup of type `t ∩ t'`. In particular, there exists a smallest element `t_{min}`
in the set of `t(P)`, `P` running through the set of parabolic subgroups of `G`.*

*(ii) Every parabolic subgroup of `G` contains a minimal parabolic subgroup. For a parabolic subgroup of `G` to be
minimal, it is necessary and sufficient that it be of type `t_{min}`. Two minimal parabolic subgroups of `G` are
conjugate by an element of `G(S)`.*

<!-- label: III.XXVI.5.7 -->

This follows at once from 5.4 and 5.5 (i).

**Remark 5.8.** *A parabolic subgroup opposite to a minimal parabolic subgroup is also minimal; this entails
`s(t_{min}) = t_{min}`.*

<!-- label: III.XXVI.5.8 -->

<!-- original page 491 -->

**Corollary 5.9.** *Let `S` be a scheme, `G` an `S`-reductive group, `P` a parabolic subgroup of `G`. The canonical
morphism*

```text
G ⟶ G/P = X
```

*makes `G` an `X`-bundle locally trivial (in the sense of Zariski) with group `P_X`. If `L` is a Levi subgroup of `P`,
the canonical morphism (cf. 3.12)*

```text
G ⟶ G/L = Y
```

*makes `G` a `Y`-bundle locally trivial (in the sense of Zariski) with group `L_Y`.*

<!-- label: III.XXVI.5.9 -->

It suffices to prove that if one has a morphism `S' → S`, where `S'` is local and a morphism `S' → X` (resp. `S' → Y`),
it lifts to a morphism `S' → G`. In other words, one may assume `S` local, and one must show that the map
`G(S) → X(S)` (resp. `G(S) → Y(S)`) is surjective.

The first assertion was demonstrated in 5.2; let us demonstrate the second. Let `y ∈ Y(S)`; its canonical image in
`X(S)` comes from a `g ∈ G(S)`; the projection `y'` of `g` in `Y(S)` therefore has the same projection as `y` in
`X(S)`. There exists therefore a unique `u ∈ rad^u(P)(S)` such that `y' u = y`, and the projection of `g u` in `Y(S)`
is indeed `y`.

<!-- original page 492 -->

**Corollary 5.10.** *Let `S` be a semi-local scheme, `G` an `S`-reductive group.*

*(i) Let `P` be a parabolic subgroup of `G`, `L` a Levi subgroup of `P`. The canonical maps (cf. 3.21) induce
bijections*

```text
H^1(S, L) ⥲ H^1(S, P) ⥲ H^1_{t(P)}(S, G).
```

*(ii) Let `t, t' ∈ Of(Dyn(G))(S)`; one has (cf. 3.21)*

```text
H^1_t(S, G) ∩ H^1_{t'}(S, G) = H^1_{t ∩ t'}(S, G).
```

*(iii) If `P` and `Q` are two parabolic subgroups of `G` in osculating position, the following canonical diagram is
cartesian and composed of injections:*

```text
H^1(S, P) ─────→ H^1(S, G)
   ↑                  ↑
   │                  │
H^1(S, P ∩ Q) ──→ H^1(S, Q).
```

<!-- label: III.XXVI.5.10 -->

Let us demonstrate (i). The map `H^1(S, L) → H^1(S, P)` is bijective by 2.3; the map `H^1(S, P) → H^1_{t(P)}(S, G)` is
surjective (3.21); let us show that it is injective, i.e. that the canonical map `H^1(S, P) → H^1(S, G)` is injective.
Let `Q` be a principal bundle under `P`, `Q_1` the associated principal bundle under `G`, `P'` and `G'` the
corresponding twisted forms of `P` and `G`. It is clear that `G'` is an `S`-reductive group and that `P'` is a
parabolic
<!-- original page 493 -->
subgroup of it. The set of elements of `H^1(S, P)` that have the same image as the class of `Q` in `H^1(S, G)` is
naturally identified with the kernel of the canonical map `H^1(S, P') → H^1(S, G')`, and this, by the exact sequence
of cohomology, with the set of orbits of `G'(S)` in `(G'/P')(S)` (for these arguments of non-abelian cohomology, see
Giraud's thesis[^N.D.E-XXVI-28]). But `G'(S)` acts transitively on `(G'/P')(S)` by 5.2.

Let us demonstrate (ii): let `Q` be a principal homogeneous bundle under `G` and `G_Q` the corresponding twisted form
of `G`. By definition (3.21), we must prove that `G_Q` has a parabolic subgroup of type `t ∩ t'` if and only if it has
parabolic subgroups of type `t` and `t'`, which is none other than the conjunction of 3.8 and 5.7 (i). Finally, (iii)
follows at once from (i) and (ii).

Let us now state a consequence of 5.3.

**Corollary 5.11.** *Let `S` be a semi-local scheme, `G` an `S`-reductive group, `P` a parabolic subgroup of `G`. If
`P ≠ G`, there exist at least three distinct parabolic subgroups of `G` of the same type as `P`; in other words,
`P ≠ G` entails `(G(S) : P(S)) ⩾ 3`.*

<!-- label: III.XXVI.5.11 -->

Indeed, let `P'` be a parabolic subgroup of `G` opposite to `P` (4.3.5 (i)). Since `P ≠ G`, one has `rad^u(P') ≠ e` (by
4.3.2 for example). By 2.1, `rad^u(P')(S) ≠ e`; let then `u ∈ rad^u(P')(S)`, `u ≠ e`. Then `int(u) P ≠ P`, and by 5.3,
there exists a `P_1`, of the same type as `P`, and opposite to `P` and `int(u) P`; then `P_1`, `P` and `int(u) P` are
three distinct parabolic subgroups of `G`, of the same type as `P`.

## 6. Parabolic subgroups and split tori

<!-- label: III.XXVI.6 -->

<!-- original page 494 -->

**Proposition 6.1.** *Let `S` be a scheme, `G` an `S`-reductive group, `g = Lie(G/S)`, and `Q` a split subtorus of `G`.
Write `Q = D_S(M)` and let*

```text
g = ⨁_{α ∈ M} g^α
```

*be the decomposition of `g` under the action of `Q`. Let `M_1` be a subset of `M` such that `0 ∈ M_1` and that
`α, β ∈ M_1 ⇒ α + β ∈ M_1`.*

*(i) There exists a unique smooth subgroup `H_{M_1}` of `G`, with connected fibers, containing `Centr_G(Q)`, and whose
Lie algebra is `⨁_{α ∈ M_1} g^α`.*

*(ii) One has the following implications:*

```text
M_1 = {0}              ⟹  H_{M_1} = Centr_G(Q),
M_1 = −M_1             ⟹  H_{M_1} is reductive,
M_1 ∪ (−M_1) = M       ⟹  H_{M_1} and H_{−M_1} are parabolic subgroups of G,
                          opposite, with common Levi subgroup H_{M_1 ∩ −M_1}.
```

<!-- label: III.XXVI.6.1 -->

To demonstrate (i) and (ii), which are local for the (fpqc) topology, one may assume that `Q` is contained in a maximal
<!-- original page 495 -->
torus `T` of `G`; one may furthermore split `G` relative to `T`. Assertion (i) then follows at once from Exp. XXII,
5.3.5, 5.4.5 and 5.4.7; the assertions of (ii) follow from Exp. XXII, 5.3.5, 5.10.1, 5.11.3 and, in this Exposé, 1.4
and 4.3.2.

**Corollary 6.2.** *Let `S` be a scheme, `G` an `S`-reductive group, `Q` a split subtorus of `G`. There exists a
parabolic subgroup of `G` of which `Centr_G(Q)` is a Levi subgroup.*

<!-- label: III.XXVI.6.2 -->

Indeed, writing `Q = D_S(M)`, one chooses a total order structure on the group `M`, one calls `M_1` the set of positive
elements of `M`; the group `H_{M_1}` answers the question.

**Corollary 6.3.** *If the `S`-reductive group `G` has a non-central split subtorus, it has a proper parabolic subgroup
(i.e. `≠ G`).*

<!-- label: III.XXVI.6.3 -->

By 5.9 and 5.10, one derives from 6.2:

**Corollary 6.4.** *Let `S` be a scheme, `G` an `S`-reductive group, `Q` a split subtorus of `G`. The canonical
morphism `G → G / Centr_G(Q)` is a locally trivial fibration.*

*If `S` is semi-local, the map `G(S) → (G / Centr_G(Q))(S)` is surjective, and the map
`H^1(S, Centr_G(Q)) → H^1(S, G)` is injective.*

<!-- label: III.XXVI.6.4 -->

### 6.5.

<!-- label: III.XXVI.6.5 -->

Suppose `S` connected. If `T` is an `S`-torus and `T'` and `T''` are two split subtori of `T`, their product
`T' · T''`[^N.D.E-XXVI-29] is also a split subtorus of `T`. Indeed,
<!-- original page 496 -->
it is identified with the quotient of `T' ×_S T''` by `T' ∩ T''`, a quotient that is split by Exp. IX, 2.11. It follows
that `T` has a largest split subtorus; one denotes it `T_{spl}`.

**Lemma 6.6.** *Let `S` be a connected scheme, `T` an isotrivial `S`-torus, `T_{spl}` its largest split subtorus. The
following conditions are equivalent:*

*(i) There exists a homomorphism `T → G_{m, S}` distinct from `e`.*

*(ii) `T_{spl} ≠ e`.*

<!-- label: III.XXVI.6.6 -->

Since `T` is assumed isotrivial, there exist a finite group `Γ`, a connected principal Galois covering `S' → S` of
group `Γ`, and an isomorphism `T_{S'} ≃ D_{S'}(M)`; `M` is then endowed with a structure of `Γ`-module, and one has a
natural isomorphism `Hom_S(T, G_{m, S}) = H^0(Γ, M)`.

On the other hand, let `V` be the vector subspace of `M ⊗ ℚ` generated by elements of the form `g(m) − m`, `g ∈ Γ`,
`m ∈ M`. One verifies at once that `(T_{spl})_{S'}` is identified with `D_{S'}(M / M ∩ V)`. Assertion (i) is therefore
equivalent to `H^0(Γ, M) ≠ 0`, or equivalently to `H^0(Γ, M ⊗ ℚ) ≠ 0`, whereas assertion (ii) is equivalent to
`M ≠ M ∩ V`, or equivalently to `M ⊗ ℚ ≠ V`. Now one has `M ⊗ ℚ = H^0(Γ, M ⊗ ℚ) ⊕ V`, as one verifies at once
(consider the projector `M ⊗ ℚ → H^0(Γ, M ⊗ ℚ)` that sends `x` to the average of the transforms of `x` by `Γ`).

<!-- original page 497 -->

**Lemma 6.7.** *Let `S` be a scheme, `G` an `S`-reductive group, `P` a parabolic subgroup of `G` such that `P ≠ G`, `L`
a Levi subgroup of `P`, `Q` its radical. There exists a homomorphism `Q → G_{m, S}` distinct from `e`.*

<!-- label: III.XXVI.6.7 -->

Consider the unipotent radical `U` of `P`; it is invariant under `int(P)`, hence under `int(Q)`. Consider the
invertible `O_S`-module `det(Lie(U))`, the "maximum exterior power" of the locally free `O_S`-module `Lie(U)`. The
adjoint representation defines a homomorphism of groups

```text
f : Q ⟶ Aut(det(Lie(U))) = G_{m, S}.
```

If `P ≠ G`, then `U ≠ e`. Let us choose `s ∈ S` such that `U_s ≠ e`. Splitting `G_s` relative to a maximal torus
containing `Q_s`, one sees at once that `f_s ≠ e`.

**Proposition 6.8.** *Let `S` be a connected semi-local scheme, `G` an `S`-reductive group, `P` a parabolic subgroup of
`G`, `L` a Levi subgroup of `P`, `Q` its radical, `Q_{spl}` the largest split subtorus of `Q` (i.e. the largest central
split subtorus of `L`). Then*

```text
L = Centr_G(Q_{spl}).
```

<!-- label: III.XXVI.6.8 -->

Set `L' = Centr_G(Q_{spl})`; this is a reductive subgroup of `G` containing `L`; moreover, `P' = P ∩ L'` is a parabolic
subgroup of `L'`, of Levi subgroup `L` (1.20). If `L' ≠ L`, then `L' ⊄ P` (since `L` is a maximal reductive subgroup of
<!-- original page 498 -->
`P`, cf. 1.7), hence `P' ≠ L'`.

Let `G_1` be the derived group of `G`, and `P_1 = P' ∩ G_1`. By 1.19, `P_1` is a parabolic subgroup of the semisimple
group `G_1`, `L_1 = L ∩ G_1` is a Levi subgroup of it, and

```text
Q_1 = rad(L_1) = (rad(L) ∩ G_1)^0 = (Q ∩ G_1)^0.
```

Since `L_1` has a maximal torus `T_1` (Exp. XIV, 3.20), and the latter is isotrivial (Exp. XXIV, 4.1.5), `Q_1`, being a
subtorus of `T_1`, is also isotrivial (Exp. IX, 2.11); since `P_1 ≠ G_1`, one may apply 6.7 and 6.6, and one therefore
has `(Q_1)_{spl} ≠ e`, whence `(Q_{spl} ∩ G_1)^0 ≠ e`, hence `Q_{spl} ⊄ rad(L')` (since `rad(L') ∩ G_1` is finite),
which is contradictory with the definition of `L'`.

**Corollary 6.9.** *Let `S` be a connected semi-local scheme, `G` an `S`-reductive group, `Q` a critical subtorus of
`G` (i.e. such that `rad(Centr_G(Q)) = Q`). For `Centr_G(Q)` to be a Levi subgroup of a parabolic subgroup of `G`, it
is necessary and sufficient that `Centr_G(Q) = Centr_G(Q_{spl})`, that is, `Lie(G)^Q = Lie(G)^{Q_{spl}}`.*

<!-- label: III.XXVI.6.9 -->

This follows from 6.2 and 6.8.

**Corollary 6.10.** *Let `S` be a connected semi-local scheme, `G` an `S`-reductive group, `L` a subgroup of `G`. The
following conditions are equivalent:*

*(i) There exists a parabolic subgroup of `G` of which `L` is a Levi subgroup.*

*(ii) There exists a split subtorus of `G` of which `L` is the centralizer.*

*(iii) There exists a homomorphism `G_{m, S} → G` of which `L` is the centralizer.*

<!-- label: III.XXVI.6.10 -->

<!-- original page 499 -->

Indeed, one has (i) ⇒ (ii) by 6.8, and (iii) ⇒ (i) by 6.1; it remains to prove (ii) ⇒ (iii). Suppose then
`L = Centr_G(Q)`, with `Q = D_S(M)`; write `g = Lie(G/S)` and

```text
g = ⨁_{α ∈ M} g^α,
```

and let `R` be the set of `α ∈ M − {0}` such that `g^α ≠ 0`.

Since `R` is finite and does not contain `0`, there exists a homomorphism `u : M → ℤ` such that `u(α) ≠ 0` for each
`α ∈ R`. By duality, `u` gives a homomorphism `G_{m, S} → Q`, hence a homomorphism `f : G_{m, S} → G`. One has
`Centr_G(f) ⊃ Centr_G(Q)`; these are two smooth subgroups of `G`, with connected fibers; their Lie algebras coincide
(since both are equal to `g^0`); they therefore coincide, by a customary argument.

**Corollary 6.11.** *Let `S` be a connected semi-local scheme, `G` an `S`-reductive group. The maps*

```text
L ↦ rad(L)_{spl},        Q ↦ Centr_G(Q)
```

*are mutually inverse bijections, which reverse the natural order structures, between the set of subgroups `L` of `G`
that are Levi subgroups of parabolic subgroups of `G` and the set of split subtori `Q` of `G` such that
`rad(Centr_G(Q))_{spl} = Q`.*

<!-- label: III.XXVI.6.11 -->

**Corollary 6.12.** *Let `S` be a connected semi-local scheme, `G` an `S`-reductive group. Consider the following
assertions:*

<!-- original page 500 -->

*(i) There exists a parabolic subgroup of `G` distinct from `G`.*

*(ii) `G` has a non-central split subtorus.*

*(ii bis) `G` has a non-central split subtorus of relative dimension 1.*

*(iii) There exists a homomorphism of groups `G_{a, S} → G` that is a closed immersion.*

*Then one has (i) ⇔ (ii) ⇔ (ii bis) ⇒ (iii).*

<!-- label: III.XXVI.6.12 -->

The only new assertion is (i) ⇒ (iii). Let then `P` be a parabolic subgroup of `G`, distinct from `G`. Then
`U = rad^u(P) ≠ e`. Consider the last non-trivial subgroup `U_n` of the composition series of `U` (2.1). One has an
isomorphism `U_n ≃ W(E_n)`, where `E_n` is a locally free `O_S`-module, hence free[^N.D.E-XXVI-30]. Since `E_n ≠ 0`,
there exists a locally direct-factor monomorphism `O_S → E_n`, hence a closed immersion
`G_{a, S} = W(O_S) ↪ W(E_n) ≃ U_n`, which yields (iii) at once.

**Remark 6.12.1.** *When `S` is the spectrum of a field of characteristic 0, it follows from the Jacobson–Morozov
theorem that (iii) ⇒ (ii bis). The preceding four conditions are then equivalent ("Godement's criterion",
cf. [BT65], 8.5).[^XXVI-1]*

<!-- label: III.XXVI.6.12.1 -->

<!-- original page 501 -->

**Definition 6.13.** *Let `S` be a connected semi-local scheme, `G` an `S`-reductive group. One says that `G` is*
anisotropic *if `G` contains no split subtorus not reduced to `e`.*

<!-- label: III.XXVI.6.13 -->

**Corollary 6.14.** *Let `S` be a connected semi-local scheme. For the `S`-reductive group `G` to be anisotropic, it
is necessary and sufficient that it have no parabolic subgroup `P ≠ G`, and that its radical be anisotropic.*

<!-- label: III.XXVI.6.14 -->

Using now 6.6, Exp. XXIV, 4.1.5, and Exp. XXII, 6.2, one deduces:

**Corollary 6.15.** *Let `S` be a connected semi-local scheme, `G` an isotrivial `S`-reductive group (e.g. `G`
semisimple, or `S` normal (Exp. X 5.16)). For `G` to be anisotropic, it is necessary and sufficient that `G` have no
parabolic subgroup `P ≠ G`, and that `Hom_{S-gr.}(G, G_{m, S}) = e`.*

<!-- label: III.XXVI.6.15 -->

**Proposition 6.16.** *Let `S` be a connected semi-local scheme, `G` an `S`-reductive group. The maximal split subtori
of `G` are the largest central split subtori of the Levi subgroups of the minimal parabolic subgroups of `G`. Two such
tori are conjugate by an element of `G(S)`.*

<!-- label: III.XXVI.6.16 -->

Let `Q` be a maximal split subtorus of `G`.[^N.D.E-XXVI-32] Then, by 6.2, `L = Centr_G(Q)` is a Levi subgroup of a
parabolic subgroup `P` of `G`, and since `Q ⊂ rad(Centr_G(Q))_{spl}`, the maximality of `Q` entails
`Q = rad(Centr_G(Q))_{spl}`. By 6.11, `L` is a minimal element of the set of Levi subgroups of parabolic
<!-- original page 502 -->
subgroups of `G`, hence `P` is a minimal parabolic subgroup of `G` by 1.20. It then follows from 5.7 and 5.5 (iv) that
two subtori such as `Q` are conjugate by a section of `G(S)`. The conjugacy of the `Q` and of the pairs `(P, L)` then
entails the first assertion of 6.16.

**Corollary 6.17.** *Let `S` be a connected semi-local scheme, `P` and `P'` two minimal parabolic subgroups in
standard position (4.5.1.1). Then `P ∩ P'` contains a common Levi subgroup of `P` and `P'`.*

<!-- label: III.XXVI.6.17 -->

Indeed, `P ∩ P'` contains a maximal torus `T` of `G`, by 4.5.1 (v); let `L` be the unique Levi subgroup of `P`
containing `T`. One has

```text
rad(P) ∩ T = rad(P) ∩ L = rad(L)
```

by 1.21, hence `rad(P) ∩ T` contains `rad(L)_{spl}`, which is a maximal split subtorus of `G`, hence is necessarily
equal to `T_{spl}`. One therefore has `L = Centr_G(T_{spl})`, and by symmetry `L` is also a Levi subgroup of `P'`.

**Remark 6.18.** *It follows from 1.21 that the parabolic subgroup `P` of `G` is minimal if and only if `rad(P)`
contains a maximal split subtorus of `G`; then, by the proof of 6.17, if `T` is a maximal torus of `P`, `T_{spl}` is a
maximal split torus of `G` and of `rad(P)`, and `Centr_G(T_{spl})` is a Levi subgroup of `P`. Moreover, every Levi
subgroup of `P` is obtained in this way.*

<!-- label: III.XXVI.6.18 -->

## 7. Relative root datum

<!-- label: III.XXVI.7 -->

<!-- original page 503 -->

In this section, `S` will denote a non-empty connected semi-local scheme, `G` an `S`-reductive group, `Q` a maximal
split subtorus of `G`, and `L` the centralizer of `Q` in `G`, i.e. `L = Centr_G(Q)`.

### 7.1.

<!-- label: III.XXVI.7.1 -->

Since `Q` is the largest central split subtorus of `L`, every section of `G(S)` that normalizes `L` also normalizes `Q`.
One therefore has (cf. 7.1.1)

```text
Norm_G(L)(S) = Norm_G(Q)(S).
```

On the other hand, one saw in 6.4 that the map `G(S) → (G/L)(S)` is surjective. It follows that one has a canonical
identification

```text
W_G(Q)(S) = (Norm_G(Q) / Centr_G(Q))(S) ≃ Norm_G(L)(S) / L(S).
```

One will denote by `M` the group `Hom_{S-gr.}(Q, G_{m, S})`, so that one has a canonical isomorphism `Q ≃ D_S(M)`. One
will denote by `W` the group of automorphisms of `M` defined by `W_G(Q)(S)`. One therefore has isomorphisms

```text
W ≃ W_G(Q)(S) ≃ Norm_G(L)(S) / L(S).
```

### 7.1.1.

<!-- label: III.XXVI.7.1.1 -->

One does not in general have `Norm_G(L) = Norm_G(Q)`. Take, for example, for `S` the spectrum of a field `k`, having a
quadratic extension `k'`, for `G` the unitary group `Q-Ép_{k'/k}(A_2)` (cf. Exp. XXIV, 3.11.2).

<!-- original page 504 -->

Since the minimal parabolic subgroups of `G` are its Borel subgroups, their Levi subgroups are maximal tori, and one has
`(Norm_G(L)/L)(k) = S_3`.

On the other hand, since `G` is not split, the maximal split tori of `G` are of dimension `⩽ 1`, hence isomorphic to
`G_{m, k}`. Since `Norm_G(Q)/L` acts faithfully on `Q`, one has `(Norm_G(Q)/Q)(k) = ℤ/2ℤ`.

### 7.2.

<!-- label: III.XXVI.7.2 -->

If `P` is a parabolic subgroup of `G` with Levi group `L` (one exists by 6.2), `P` is necessarily minimal (cf. 6.18). By
the conjugacy of minimal parabolic subgroups of `G` (5.7), of that of Levi subgroups of a parabolic subgroup (1.8), and
of the equalities `P = Norm_G(P)` and `Norm_G(L) ∩ P = L` (1.6), one obtains: the set of (minimal) parabolic subgroups
of `G` with Levi group `L` is principal homogeneous under the group `W`.

### 7.3.

<!-- label: III.XXVI.7.3 -->

The Lie algebra of `G` decomposes under the action of `Q` as

```text
Lie(G) = Lie(L) ⊕ ⨁_{α ∈ R} Lie(G)^α,
```

where `R` is the set of non-zero characters of `Q` such that `Lie(G)^α ≠ 0` (roots of `G` relative to `Q`).

Let us denote by `M^*` the group `Hom_{S-gr.}(G_{m, S}, Q)`, which is in duality with `M` and on which `W` acts
naturally by transport of structure.

<!-- original page 505 -->

**Theorem 7.4.** *With the notations of 7.3, there exists a unique map `α ↦ α^*` from `R` to `M^*` that defines on
`(M, M^*)` a root datum (Exp. XXI, 1.1) whose Weyl group is `W`.*

*Moreover, the parabolic subgroups `P` of `G` with Levi group `L` and the systems of positive roots `R^+` of `R`
correspond bijectively via the relation*

```text
Lie(P) = Lie(L) ⊕ ⨁_{α ∈ R^+} Lie(G)^α.
```

<!-- label: III.XXVI.7.4 -->

### 7.4.1.

<!-- label: III.XXVI.7.4.1 -->

Suppose first that the existence of the map `α ↦ α^*` sought has been proved. By Exp. XXI, 3.4.10, `s_α` is the unique
element of `W` such that for every `m ∈ M`, `s_α(m) − m` is a rational multiple of `α`, which shows that `s_α` is
determined by `α`; as one then has[^N.D.E-XXVI-33] `α^*(m) α = m − s_α(m)`, one sees that `α^*` is determined by `α`,
which proves the uniqueness of the map `α ↦ α^*`.

### 7.4.2.

<!-- label: III.XXVI.7.4.2 -->

Let `α ∈ R` and let `L_α` (resp. `H_α`, resp. `H_{−α}`) be the unique smooth subgroup of `G` with connected fibers
containing `L` and such that (cf. 6.1 (i))

```text
Lie(L_α)   = Lie(L) ⊕ ⨁_{γ ∈ ℤα ∩ R} Lie(G)^γ,
Lie(H_α)   = Lie(L) ⊕ ⨁_{γ ∈ ℕα ∩ R} Lie(G)^γ,
Lie(H_{−α}) = Lie(L) ⊕ ⨁_{γ ∈ −ℕα ∩ R} Lie(G)^γ.
```

<!-- original page 506 -->

`L_α` is a reductive subgroup of `G`, `H_α` and `H_{−α}` are parabolic subgroups of it with Levi subgroup `L`, and
`H_α` and `H_{−α}` are opposite relative to `L` (cf. 6.1 (ii)).

By 7.2, there therefore exists `s_α ∈ Norm_{L_α}(Q)(S) / L(S) ⊂ W` such that `s_α(H_α) = H_{−α}`. One has
`s_α(α) = −α` (because `α` (resp. `−α`) is the common divisor of the elements of `R` occurring in `H_α` (resp.
`H_{−α}`)), and one has `s_α^2 = id` (since `s_α^2(H_α)` and `H_α` are both opposite to `H_{−α}` relative to `L`). One
has therefore constructed an `s_α ∈ W` satisfying the following properties:

```text
(x)     s_α(α) = −α,    s_α^2 = id;
(xx)    s_α can be represented by an element of L_α(S).
```

Let us moreover remark that `s_α` is constructed canonically from `α`, and in particular that

```text
(xxx)    for every w ∈ W, one has w s_α w^{−1} = s_{w(α)}.
```

### 7.4.3.

<!-- label: III.XXVI.7.4.3 -->

We now propose to prove the assertion:

```text
(xxxx)    for every m ∈ M, s_α(m) − m ∈ ℤα.
```

Since `S` is connected, this assertion is local for the (fpqc) topology. One may therefore assume that `L_α = G_1` is
splittable relative to a maximal torus `T_1` of `L`. Let then `(G_1, T_1, M_1, R_1)` be such a splitting. The
monomorphism `Q → T_1` identifies `M` with a quotient of `M_1`; let `p : M_1 → M` be the canonical map.

The image of `R_1` under `p` consists, possibly with the inclusion of zero, of the roots of `G_1` with respect to `Q`
<!-- original page 507 -->
(hence of the elements of `R` that are integer multiples of `α`); one therefore has `p(R_1) ⊂ ℤα`. By (xx), there
exists an element of `Norm_{G_1}(L)(S)` that induces `s_α` on `Q`. By Exp. XXII, 5.10.10, there therefore exists a
section `w ∈ (W_1)_S(S)` that induces `s_α` on `Q` (one denotes by `W_1` the Weyl group of the root datum
`(M_1, R_1, …)`). Possibly after restricting `S`, one may therefore assume that there exists `w ∈ W_1` inducing `s_α`
on `Q`, hence satisfying `p(w(m_1)) = s_α(p(m_1))` for every `m_1 ∈ M_1`. But, by definition of `W_1`, `w` is a product
of reflections with respect to elements of `R_1`, hence `w(m_1) − m_1` is a linear combination with integer
coefficients of elements of `R_1`. It follows that `s_α(p(m_1)) − p(m_1)` is a linear combination with integer
coefficients of the elements of `p(R_1) ⊂ ℤα`, hence an integer multiple of `α`, as was to be proved.

### 7.4.4.

<!-- label: III.XXVI.7.4.4 -->

One may therefore define an element `α^* ∈ M^*` by[^N.D.E-XXVI-34]

```text
α^*(m) α = m − s_α(m).
```

By (x), one has `(α^*, α) = 2`; on the other hand, it follows from (xxx) that for every pair `(α, α') ∈ R × R`, one
has `s_α(α') ∈ R` and `s_α(α'^*) = s_α(α')^*`, which proves (cf. Exp. XXI, 1.1) that the constructed map `α ↦ α^*`
indeed defines a root datum on `(M, M^*)`.

### 7.4.5.

<!-- label: III.XXVI.7.4.5 -->

Let `W'` be the Weyl group of this root datum (the group of transformations of `M` generated by the `s_α`); one has
`W' ⊂ W`.

Let on the other hand `⩾` be a total order relation on the free abelian group `M`; set
`R^+ = { α ∈ R | α ⩾ 0 }`. One knows that `R^+` is a system of positive roots of `R`. Let `w ∈ W`, represented by an
`n ∈ Norm_G(L)(S) = Norm_G(Q)(S)`. Set `P = H_{R^+}`
<!-- original page 508 -->
(notation of 6.1); by *loc. cit.*, `P` is a parabolic subgroup of `G` with Levi subgroup `L`. One obviously has
`int(n) P = H_{w(R^+)}`. It then follows from 7.3 that `w(R^+) = R^+` entails `w = e`. As the group `W'` acts
transitively on the systems of positive roots of `R` (Exp. XXI, 3.3.7) and the stabilizer in `W` of `R^+` is the
identity, one concludes immediately that `W = W'`. One also concludes that `W = W'` acts in a simply transitive way
both on the set of systems of positive roots of `R` and on the set of parabolic subgroups of `G` with Levi group `L`,
which entails the last assertion of 7.4. QED.

### 7.5.

<!-- label: III.XXVI.7.5 -->

If `P` and `P_1` are two minimal parabolic subgroups of `G`, with Levi subgroups `L` and `L_1`, and if one denotes by
`Q` and `Q_1` the maximal central split tori of `L` and `L_1`, then the pairs `(P, Q)` and `(P_1, Q_1)` are conjugate:
there exists `g ∈ G(S)` such that `int(g) P = P_1` and `int(g) Q = Q_1`.

Indeed, `P` and `P_1` are conjugate (5.7) and one may therefore assume `P = P_1`; then `L` and `L_1` are conjugate by a
section of `P(S)` (1.8). Moreover, if `g` and `g'` are two sections of `G` conjugating the pairs `(P, Q)` and
`(P_1, Q_1)`, then `g'^{−1} g` normalizes `P` and `Q`, hence `P` and `L`; but

```text
Norm_G(P) ∩ Norm_G(L) = P ∩ Norm_G(L) = L = Centr_G(Q).
```

<!-- original page 509 -->

The isomorphism `Q ⥲ Q_1` induced by `int(g)` is therefore independent of `g`.

Let `R` and `R_1` be the root data defined thanks to 7.4 in `Hom_{S-gr.}(Q, G_{m, S})` and
`Hom_{S-gr.}(Q_1, G_{m, S})`, and let `R^+` and `R_1^+` be the systems of positive roots corresponding to `P` and
`P_1`. The canonical isomorphism `Q ⥲ Q_1` defined above transforms `(R, R^+)` into `(R_1, R_1^+)`. One immediately
deduces that one may define the *pinned relative root datum*[^N.D.E-XXVI-35] of `G` over `S`, by identifying the
various `(R, R^+)` by means of the transitive system of isomorphisms described above.

From now on, we shall denote `(M, M^*, R, R^*, R^+) = R(G/S)` this pinned root datum; for each pair `P ⊃ Q` as above,
one therefore has a canonical isomorphism `M ⥲ Hom_{S-gr.}(Q, G_{m, S})` transforming `R` (resp. `R^+`) into the set of
roots of `G` (resp. of `P`) relative to `Q`, and `W(R)` into `W_G(Q)(S)`.

### 7.6.

<!-- label: III.XXVI.7.6 -->

Let still `Q` be a maximal split torus of `G`, `P` a (minimal) parabolic subgroup of `G` with Levi group
`Centr_G(Q)`, `(M, M^*, R, R^*, R^+)` the corresponding pinned root datum (7.4), and `Δ` the set of simple roots of
`R^+`. For every `A ⊂ Δ`, let `R_A ⊂ R` be the set

```text
R_A = R^+ ∪ (ℤA ∩ R^−)
```

consisting of positive roots and negative roots that are linear combinations of elements of `A`. It is a closed set
(Exp. XXI, 3.1.4) of roots, and every closed set containing `R^+` is uniquely of this form (Exp. XXI, 3.3.10). By 6.1,
<!-- original page 510 -->
there exists a unique subgroup `P_A` of `G`, smooth and with connected fibers, containing `Centr_G(Q)` and such that

```text
Lie(P_A) = Lie(G)^0 ⊕ ⨁_{α ∈ R_A} Lie(G)^α.
```

It then follows at once from 6.1, from the conjugacy of minimal parabolics, and from the fact that the set of roots of
a parabolic subgroup of `G` containing `Q` is closed (which is deduced at once from 1.4 by splitting), that:

**Proposition 7.7.** *(i) The map `A ↦ P_A` is a bijection of the set of subsets of `Δ` onto the set of parabolic
subgroups of `G` containing `P`. This bijection preserves the natural order relations of inclusion.*

*(ii) Every parabolic subgroup of `G` is conjugate by a section of `G(S)` to a unique `P_A`.*

<!-- label: III.XXVI.7.7 -->

### 7.8.

<!-- label: III.XXVI.7.8 -->

Let `P ⊃ Q` be as above. Consider the relative root datum (7.5) of `G` over `S` and the canonical isomorphism

```text
f : (M, M^*, R, R^*, R^+) ⥲ (M, M^*, R, R^*, R^+).
```

<!-- TRANSLATOR NOTE: The source writes f as an automorphism of (M, M^*, R, R^*, R^+) with itself; presumably the identifications are over different bases or models. -->

The set `Δ` of simple roots of `R^+` is transformed into the set `Δ` of simple roots of `R^+`, hence every subset `A`
of `Δ` into a subset `f(A) ⊂ Δ`.

**Definition 7.9.0.**[^N.D.E-XXVI-36] *Let `H` be an arbitrary parabolic subgroup of `G`. By 7.7 (ii), it is conjugate
to a unique `P_A`. Let us denote `t_r(H) = f(A) ⊂ Δ`. One verifies at once using the conjugacy theorems that `t_r(H)`
is independent of the choice of the pair `P ⊃ Q`. One says that it is the* relative type *of `H`.*

<!-- original page 511 -->

<!-- label: III.XXVI.7.9.0 -->

**Proposition 7.9.** *(i) The map `H ↦ t_r(H)` induces a bijection between the set of conjugacy classes (under `G(S)`)
of parabolic subgroups of `G`, and the set of subsets of `Δ`.*

*(ii) Let `H` be a parabolic subgroup of `G`, `P` a minimal parabolic subgroup contained in `H`, `Q` the maximal central
split torus of a Levi subgroup of `P`, `Δ` the set of simple roots of `P` relative to `Q`, and `f : Δ ⥲ Δ` the
canonical isomorphism. Then, for every `α ∈ Δ`, one has the equivalence:*

```text
f(α) ∈ t_r(H)  ⇔  Lie(H)^{−α} ≠ 0
```

*and one has `H = P_A`, where `A = f^{−1}(t_r(H))`.*

*(iii) If `H` and `H'` are two parabolic subgroups of `G` containing `P`, then (see 3.8.1 (ii) and 5.5 (i) for other
equivalent conditions):*

```text
t_r(H) ⊂ t_r(H')  ⇔  t(H) ⊂ t(H')
```

<!-- label: III.XXVI.7.9 -->

### 7.10.

<!-- label: III.XXVI.7.10 -->

One can study the relative positions of two minimal parabolic subgroups; the results are as follows (one refers to
<!-- original page 512 -->
4.5.2 for the notation `t_2(P, P_1)`):

(1) If `P, P_1, P', P'_1` are four minimal parabolic subgroups of `G`, then `t_2(P, P_1) = t_2(P', P'_1)` (i.e.
`(P, P_1)` and `(P', P'_1)` are conjugate locally for (fpqc)) if and only if there exists `g ∈ G(S)` such that
`int(g) P = P'` and `int(g) P_1 = P'_1`.

(2) Let us fix in particular a minimal parabolic subgroup `P` of `G` of Levi subgroup `L`, and let `T` be a maximal
torus of `L`. Consider the scheme `Par_{t_{min}}(G; P)` of minimal parabolic subgroups of `G` in standard position
relative to `P`. One has a morphism (cf. 4.5.5)

```text
f : Par_{t_{min}}(G; P) ⟶ W_P(T) \ W_G(T) / W_P(T)
```

whose fibers are "the orbits of `P` in `Par_{t_{min}}(G; P)`". By (1), `f` therefore induces a monomorphism

```text
P(S) \ Par_{t_{min}}(G; P)(S) ↪ (W_P(T) \ W_G(T) / W_P(T))(S).
```

The image of this morphism is identified with `W`; this is the Bruhat theorem: each orbit of `P(S)` in
`Par_{t_{min}}(G; P)(S)` contains one and only one parabolic subgroup of `G` with Levi group `L` (that is, of the form
`int(n) P`, where `n ∈ Norm_G(L)`).

(3) In other words, let `E(S)` be the set of `g ∈ G(S)` such that `int(g) P` and `P` are in mutual standard position.
Then `E(S)` has a partition into double cosets modulo `P(S)` indexed by `W`:

```text
E(S) = P(S) · W · P(S)
```

<!-- original page 513 -->

(obvious notation). Setting `U = rad^u(P)(S)`, one may also write

```text
E(S) = U(S) · Norm_G(L)(S) · U(S),
```

thereby exhibiting a partition of `E(S)` into double cosets modulo `U(S)`, indexed by `Norm_G(L)(S)`.

(4) If `S` is the spectrum of a field, then `E(S) = G(S)`, and one recovers [BT65], 5.15.

**Counterexamples 7.11.** *Let `S = Spec(ℤ/4ℤ)`, `G = SL_{2, S}`. Let `B` be the standard Borel subgroup formed of
matrices `(a b; c d)` with `c = 0`. Let `g = ( 1; −2 1)` ∈ G(S)` [scil.: `g = (1, 1; −2, 1)`]; set
`B' = int(g) B`. Then `B(S) = B'(S)`, and `B ∩ B'` does not contain a maximal torus[^N.D.E-XXVI-37]. This shows on the
one hand that two distinct minimal parabolic subgroups may have the same group of sections, and on the other hand that
there exists no general criterion allowing one to recognize whether two minimal parabolic subgroups `P` and `P'` are in
standard position, using only the groups `P(S)` and `P'(S)`. In particular, the part `E(S)` of `G(S)` does not seem to
be definable using only the situation `{G(S), P(S), Norm_G(L)(S)}` (in the preceding case, this part is defined by
`c ≠ 2`[^N.D.E-XXVI-38]).*

<!-- label: III.XXVI.7.11 -->

### 7.12.

<!-- label: III.XXVI.7.12 -->

<!-- original page 514 -->

One now proposes to study the variation of `R(G/S)` with `S`. Let then `S'` be an `S`-scheme, also semi-local connected
and non-empty. Let `Q` be a maximal split torus of `G`; then `Q_{S'}` is a split torus of `G_{S'}`; let `Q'` be a
maximal split torus of `G_{S'}` containing `Q_{S'}`. Set

```text
M  = Hom_{S-gr.}(Q, G_{m, S}) ≃ Hom_{S'-gr.}(Q_{S'}, G_{m, S'}),
M' = Hom_{S'-gr.}(Q', G_{m, S'}).
```

The monomorphism `Q_{S'} → Q'` induces an epimorphism `u : M' → M`. Denote

```text
L  = Centr_G(Q),         L' = Centr_{G_{S'}}(Q'),
```

one has `L' ⊂ L_{S'}`.

If `H` is a subgroup of `G` containing `L`, then `H_{S'}` contains `L'`, and one has

```text
Lie(H) = Lie(L) ⊕ ⨁_{α ∈ R_H} Lie(H)^α,
Lie(H_{S'}) = Lie(L') ⊕ ⨁_{α' ∈ R'_{H_{S'}}} Lie(H_{S'})^{α'},
```

where `R_H` (resp. `R'_{H_{S'}}`) denotes the set of roots of `H` (resp. `H_{S'}`) relative to `Q` (resp. `Q'`). One
immediately derives that

```text
R_H ⊂ u(R'_{H_{S'}}) ⊂ R_H ∪ {0}.
```

Taking `H = G`, one sees first that `R ⊂ u(R') ⊂ R ∪ {0}`; taking then for `H` a minimal parabolic subgroup `P` of
Levi subgroup `L`, one sees that `R'_{H_{S'}}` contains a system of positive roots of `R'`, hence (7.4) that there
exists a minimal parabolic subgroup `P'` of `G_{S'}` of Levi subgroup `L'` contained in `P_{S'}`. One has therefore
constructed a diagram

```text
Q_{S'}   ⊂   L_{S'}   ⊂   P_{S'}
   ∩            ∪            ∪
   Q'    ⊂   L'      ⊂   P'.
```

If `R^+` (resp. `Δ`) is the system of positive roots (resp. simple) of `R` defined by `P`,
<!-- original page 515 -->
and if one defines similarly `R'^+` and `Δ'`, one easily verifies that

```text
R^+ ⊂ u(R'^+) ⊂ R^+ ∪ {0},        Δ ⊂ u(Δ') ⊂ Δ ∪ {0}.
```

Let now `w ∈ W ≃ Norm_G(Q)(S) / Centr_G(Q)(S)`, and `n ∈ Norm_G(Q)(S)` a representative of `w`. One has
`int(n) Q = Q` hence `int(n) L = L`, hence `int(n) L_{S'} = L_{S'}`. Then `Q'` and `int(n) Q'` are two maximal split
tori of `L_{S'}`, hence are conjugate by a section `x ∈ L(S')`, and one has `int(n x) Q' = Q'`, hence
`n x ∈ Norm_{G_{S'}}(Q')(S')`. Let `w'` be the image of `n' = n x` in `W' ≃ Norm_{G_{S'}}(Q')(S') /
Centr_{G_{S'}}(Q')(S')`. It is clear that the operation of `w'` on `M'` is compatible with the projection
`u : M' → M` and that the induced operation on `M` coincides with that defined by `w`.

Using now the definition of relative root data and the conjugacy theorems, one proves without difficulty:

**Theorem 7.13.** *Let `S` and `S'` be two non-empty connected semi-local schemes, `S' → S` a morphism of `S`-schemes,
`G` an `S`-reductive group,*

```text
R(G/S) = (M, M^*, R, R^*, R^+),      R(G_{S'}/S') = (M', M'^*, R', R'^*, R'^+)
```

*the pinned relative root data. There exists a canonical homomorphism*

```text
u : M' ⟶ M
```

<!-- original page 516 -->

*satisfying the following conditions:*

*(i) `u` is surjective.*

*(ii) For every `w ∈ W`, there exists an element `w'` of `W'` compatible with `u` and which induces `w` on `M`.*

*(iii) For every subset `X` of `M`, denote `X^∧ = X ∩ (M − {0})`. Then*

```text
u(R'^+)^∧ = R^+,        u(Δ')^∧ = Δ.
```

*(iv) For every parabolic subgroup `H`, consider `t_r(H) ⊂ Δ` and `t_r(H_{S'}) ⊂ Δ'`. Then*

```text
t_r(H_{S'}) = (u^{−1}(t_r(H) ∪ {0})) ∩ Δ' = { α' ∈ Δ' | u(α') ∈ t_r(H) or u(α') = 0 }.
```

<!-- label: III.XXVI.7.13 -->

**Remark 7.14.** *If `G` is splittable over `S`, its maximal split tori are maximal tori, and the relative notions
introduced here then coincide with the absolute notions already introduced. The preceding theorem therefore gives a
description of the relative root datum `R(G/S)` and of the relative type `t_r`, via the absolute root datum and the
absolute type of the group `G_{S'}`, `S'` being chosen in such a way that `G_{S'}` is splittable
(cf. Exp. XXIV, 4.4.1). We refer to [BT65], 6.12 et seq. for this description.*

<!-- label: III.XXVI.7.14 -->

### 7.15.

<!-- label: III.XXVI.7.15 -->

<!-- original page 517 -->

Let `S` be a Henselian local scheme, `s_0` its closed point, `S_0` the spectrum of the residue field of `s_0`,
identified with a closed subscheme of `S`; for every object `X` above `S`, let us denote by `X_0` the object above
`S_0` deduced from `X` by base change. Let finally `G` be an `S`-reductive group. For every parabolic subgroup `P̄` of
`G`, `P̄_0` is a parabolic subgroup of `G_0`; conversely, for every parabolic subgroup `P` of `G_0`, there exists a
parabolic subgroup `P̄` of `G` such that `P̄_0 = P` (this follows from Hensel's lemma and from the fact that `Par(G)` is
a smooth `S`-scheme); in particular (cf. 5.7), a parabolic subgroup `P̄` of `G` is minimal if and only if `P̄_0` is
minimal. Such a subgroup `P̄` of `G` being chosen, an analogous reasoning shows that the maximal split subtori of `P̄_0`
are of the form `T_0`, where `T` is a maximal split subtorus of `P̄`. It follows without difficulty that the relative
root data of `G` over `S` and of `G_0` over `S_0` are canonically isomorphic, so that the theory of parabolic subgroups
of `G` reduces to that of parabolic subgroups of `G_0`.

Let us remark, moreover, that every `S_0`-reductive group is of the form `G_0` (Exp. XXIV, Prop. 1.21), which
conversely allows one to reduce the study of parabolic subgroups of an `S_0`-reductive group to the corresponding study
over `S`.

## Bibliography

[BT65] A. Borel, J. Tits, *Groupes réductifs*, Publ. Math. I.H.É.S. **27** (1965), 55–150.[^N.D.E-XXVI-39]

[BT71] A. Borel, J. Tits, *Éléments unipotents et sous-groupes paraboliques de groupes réductifs. I*, Invent. Math.
**12** (1971), 95–104.

[Ch05] C. Chevalley, *Classification des groupes algébriques semi-simples* (with the collaboration of P. Cartier,
A. Grothendieck, M. Lazard), Collected Works, vol. 3, Springer, 2005.

[DG70] M. Demazure, P. Gabriel, *Groupes algébriques*, Masson & North-Holland, 1970.

[Gi71] J. Giraud, *Cohomologie non abélienne*, Springer-Verlag, 1971.

## Footnotes

[^XXVI-1]: This is more generally true when `S` is the spectrum of a perfect field (Tits).[^N.D.E-XXVI-31]

[^N.D.E-XXVI-0]: *N.D.E.* Version of 13/10/2024.

[^N.D.E-XXVI-1]: *N.D.E.* Since the Levi subgroups of `P` form a torsor under `rad^u(P)` (1.9), this entails, when `S`
    is semi-local, that `P` has a Levi subgroup and hence a maximal torus (2.4).

[^N.D.E-XXVI-2]: *N.D.E.* The terminology "trivial torus" has been replaced by that of "split torus".

[^N.D.E-XXVI-3]: *N.D.E.* "Parabolic subgroup" has been replaced by "subgroup of type (RC)", as in Exp. XXII, 5.11.4,
    because it will be useful later on (4.5.1, 6.17) to be able to apply this statement to `P ∩ P'`, when `P, P'` are
    two parabolic subgroups such that `P ∩ P'` is of type (RC).

[^N.D.E-XXVI-4]: *N.D.E.* cf. N.D.E. (3).

[^N.D.E-XXVI-5]: *N.D.E.* `Δ(P)` has been corrected to `Δ − Δ(P)`.

[^N.D.E-XXVI-6]: *N.D.E.* cf. XIX 1.4.

[^N.D.E-XXVI-7]: *N.D.E.* `a_1 + · · · + a_p` has been corrected to `b_1 + · · · + b_q`.

[^N.D.E-XXVI-8]: *N.D.E.* cf. SGA 1, VIII 1.3, 1.9 and 1.10.

[^N.D.E-XXVI-9]: *N.D.E.* Corollary 2.11 has been added; it will be used in 4.5.1 and 6.17.

[^N.D.E-XXVI-10]: *N.D.E.* One recalls (cf. *loc. cit.*) that `H_c = H_c(G)` denotes the functor of subgroups of `G` of
    type (RC), `Cℓ_c = Cℓ_c(G)` the functor of "conjugacy classes" of such subgroups, and that `cℓ : H_c → Cℓ_c` is the
    canonical projection.

[^N.D.E-XXVI-11]: *N.D.E.* "Critical torus" has been replaced here by "C-critical torus", cf. *loc. cit.*. In the
    sequel, we shall simply write "critical torus" instead of "C-critical torus".

[^N.D.E-XXVI-12]: *N.D.E.* cf. 3.3, N.D.E. (10) for the notations `H_c` and `Cℓ_c`.

[^N.D.E-XXVI-13]: *N.D.E.* `LT` has been changed to `CT`.

[^N.D.E-XXVI-14]: *N.D.E.* i.e. the parabolic subgroups
    `P = ((* * * *), (0 * * *), (0 0 * *), (0 0 0 *))` and
    `P' = ((* * * *), (0 * * *), (0 * * *), (0 0 0 *))` of `GL_4` are not isomorphic (because
    `rad^u(P) ≄ rad^u(P')`), but their Levi subgroups
    `L = ((* * 0 0), (* * 0 0), (0 0 * 0), (0 0 0 *))` and
    `L' = ((* 0 0 0), (0 * * 0), (0 * * 0), (0 0 0 *))` are conjugate by the element `((0 0 1 0), (0 1 0 0),
    (1 0 0 0), (0 0 0 1))`.

[^N.D.E-XXVI-15]: *N.D.E.* The numbering of the original has been preserved: there is no §3.19.

[^N.D.E-XXVI-16]: *N.D.E.* Point (ii) has been added; it will be useful in 4.5.1.

[^N.D.E-XXVI-17]: *N.D.E.* In view of the details added in 4.5.1, the original has been modified here (which stated "we
    shall not use this fact").

[^N.D.E-XXVI-18]: *N.D.E.* "Relatively dense" has been replaced by "universally schematically dense over `S`", cf. EGA
    IV₃, Def. 11.10.8.

[^N.D.E-XXVI-19]: *N.D.E.* cf. EGA IV₃, 11.10.10.

[^N.D.E-XXVI-20]: *N.D.E.* "Of order 2" has been replaced by "of order `⩽ 2`" because `s_G` may be trivial (for
    example, if `G` is of type `A_1`, `B_n`, `C_n`, …).

[^N.D.E-XXVI-21]: *N.D.E.* "Relatively dense" has been replaced by "universally schematically dense over `S`", cf. EGA
    IV₃, Def. 11.10.8.

[^N.D.E-XXVI-22]: *N.D.E.* Recall that the involution `s` was defined in 4.3.1.

[^N.D.E-XXVI-23]: *N.D.E.* The proof of the equivalence of these conditions has been added (as well as condition (v),
    used implicitly in 6.17 of the original); consequently, §4.5.1 has been transformed into Proposition 4.5.1 plus
    Definition 4.5.1.1.

[^N.D.E-XXVI-24]: *N.D.E.* see N.D.E. (23). Moreover, for an example of parabolic subgroups `P, Q` that are not in
    standard position, see 7.11 below.

[^N.D.E-XXVI-25]: *N.D.E.* `t^{−1}(t(P), t)` has been corrected to `q^{−1}(t(P), t)` and, lower down, `Par_t(G)` to
    `Par_t(G; P)` (twice).

[^N.D.E-XXVI-26]: *N.D.E.* See also [DG70], §III.5, 7.4.

[^N.D.E-XXVI-27]: *N.D.E.* "Relatively dense" has been replaced by "universally schematically dense over `S`", cf. EGA
    IV₃, Def. 11.10.8.

[^N.D.E-XXVI-28]: *N.D.E.* See [Gi71], §III.3.

[^N.D.E-XXVI-29]: *N.D.E.* Multiplicative notation has been adopted, i.e. "their sum `T' + T''`" has been replaced by
    "their product `T' · T''`".

[^N.D.E-XXVI-30]: *N.D.E.* Since `S` is assumed semi-local and connected.

[^N.D.E-XXVI-31]: *N.D.E.* This is Corollary 3.7 of the article [BT71].

[^N.D.E-XXVI-32]: *N.D.E.* The following sentence has been spelled out.

[^N.D.E-XXVI-33]: *N.D.E.* `α^*(m)` has been corrected to `α^*(m) α`.

[^N.D.E-XXVI-34]: *N.D.E.* `α^*(m)` has been corrected to `α^*(m) α`.

[^N.D.E-XXVI-35]: *N.D.E.* Recall (Exp. XXIII 1.5) that a pinned root datum is a root datum endowed with the choice of
    a system of positive roots (or of simple roots).

[^N.D.E-XXVI-36]: *N.D.E.* The numbering 7.9.0 has been added to highlight the definition of "relative type".

[^N.D.E-XXVI-37]: *N.D.E.* Indeed, `B'` is the subgroup of `G` defined by the equation `c = 2(a + b)`; then `B ∩ B'` is
    not flat over `S`, hence does not contain a maximal torus, by 4.5.1.

[^N.D.E-XXVI-38]: *N.D.E.* More generally, for every `S`-scheme `S'`, `E(S')` is defined by the condition: "`c` is
    zero or invertible".

[^N.D.E-XXVI-39]: *N.D.E.* The references that follow have been added to this reference, which appears in the
    original.

<!-- LEDGER DELTA — Exposé XXVI — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| sous-groupe parabolique | parabolic subgroup | Title-level (already in glossary). |
| sous-groupe de Levi | Levi subgroup | Already in glossary. |
| partie de Levi | Levi part | Used in the editor's introduction; renders as "Levi part". |
| radical unipotent | unipotent radical | Already in glossary. Symbolic form `rad^u(P)`. |
| position transversale | transversal position | Section 4.2 term. |
| position osculatrice | osculating position | Section 4.4 term. |
| position standard / position mutuelle standard | standard position / mutual standard position | Section 4.5 term. |
| sous-groupe critique | critical subgroup | Already used in Exp. XXII glossary. |
| tore (C-)critique | (C-)critical torus | NDE 11 changes terminology to "critical torus" in the sequel. |
| sous-tore déployé | split subtorus | NDE 2 changes "trivial torus" to "split torus". |
| tore déployé maximal | maximal split torus | Section 6 / 7 term. |
| tore central déployé maximal | maximal central split torus | Section 6.8. |
| sous-groupe parabolique minimal | minimal parabolic subgroup | Definition 5.6. |
| type de parabolique | type of a parabolic | Definition 3.4. |
| schéma des types de paraboliques | scheme of types of parabolics | Definition 3.4. |
| type relatif | relative type | Definition 7.9.0. |
| donnée radicielle relative épinglée | pinned relative root datum | Section 7.5 terminology. |
| grosse cellule | big cell | Section 5.1.10 (`Ω`). |
| anisotrope | anisotropic | Definition 6.13. |
| isotrivial | isotrivial | Lemma 6.6 / Cor. 6.15. |
| déployable / quasi-déployable | splittable / quasi-splittable | 5.1.9. |
| schéma constant tordu fini | finite twisted constant scheme | 3.1. |
| Of(E) | Of(E) | Set of open-and-closed subschemes; kept verbatim. |
| Par(G) | Par(G) | Functor of parabolic subgroups; kept verbatim. |
| Crit(G), Cℓ_crit | Crit(G), Cℓ_crit | Functor of critical subgroups and class scheme; kept verbatim. |
| Dyn(G) | Dyn(G) | Dynkin scheme; kept verbatim. |
| Tor(G), Lev(P), PL, PT, CT, PLT | Tor(G), Lev(P), PL, PT, CT, PLT | Auxiliary functor names; kept verbatim. |
| Gen, Gen(/Q), Gen(P/Q) | Gen, Gen(/Q), Gen(P/Q) | Open subscheme/functor names; kept verbatim. |
| Opp(G), Opp(/P) | Opp(G), Opp(/P) | Opposite-parabolic functors; kept verbatim. |
| Stand(G), TypeStand | Stand(G), TypeStand | Functor of standard-position pairs and its type scheme. |
| Q-Ép_{k'/k}(A_2) | Q-Ép_{k'/k}(A_2) | "Quasi-pinning" / outer-form notation from Exp. XXIV; kept verbatim. |
| Tdép | T_{spl} | "Largest split subtorus"; English suffix "spl" used in this translation. |
| transporteur strict | strict transporter | 1.3 (iii). |
| schéma ordonné | ordered scheme | 3.7. |
| fibration localement triviale | locally trivial fibration | 6.4 / 5.9. |
| critère de Godement | Godement's criterion | Remark 6.12.1. |
-->




