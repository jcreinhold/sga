# Exposé XV. Complements on sub-tori of a group scheme. Application to smooth groups

<!-- label: III.XV -->

*by M. Raynaud* [^XV-0-1]

## 0. Introduction

<!-- label: III.XV.0 -->

<!-- original page 349 -->

This Exposé complements and partially recasts Exposés XI and XII; the contents of Exposés XIII and XIV are not
indispensable. Continuing the effort undertaken in XII, we shall work with `S`-preschemes in groups that are not
necessarily affine and not necessarily separated over `S`.

Sections 1, 2, 3, 4 are devoted to the study of sub-tori of a group prescheme. We obtain theorems of infinitesimal
lifting (§ 2) and global lifting (§ 4), in which an essential role is played by points of finite order (§ 1).

Sections 5, 6 and 7 are independent of the preceding ones. The consideration of infinitesimal neighborhoods leads to the
representability of the functor of smooth subgroups equal to their connected normalizer (§ 5). In §§ 6 and 7, we turn
more specifically to Cartan subgroups.

Finally, in § 8 we give a necessary and sufficient condition for the functor of sub-tori of a smooth group, or that of
maximal tori, to be representable.

## 1. Lifting of finite subgroups

<!-- label: III.XV.1 -->

<!-- original page 350 -->

### 1.1. Finite, smooth and central subgroups of multiplicative type

<!-- label: III.XV.1.1 -->

**Proposition 1.1.** *Let `S` be an affine scheme, `S₀` a closed subscheme of `S` defined by an ideal of square zero,
`G` an `S`-prescheme in groups, `H₀` a subgroup scheme of `G₀ = G ×_S S₀` which is smooth over `S₀`, of finite type, and
of multiplicative type. Then, in order that there exist a subgroup scheme of `G`, of multiplicative type, which lifts
`H₀`, it is necessary and sufficient that there exist a subscheme `H′` of `G`, flat over `S`, which lifts `H₀`.*

<!-- label: III.XV.1.1.statement -->

The necessity of the condition is clear; let us prove sufficiency. The group `H₀` of multiplicative type is
quasi-isotrivial (X 4.5); by Exp. X 2.1, there exist an `S`-group `H` of multiplicative type and an `S₀`-isomorphism of
groups:

```text
u₀ : H ×_S S₀ ⥲ H₀.
```

Since `H′` is flat over `S` and `H′ ×_S S₀` is of finite presentation over `S₀` (Exp. IX 2.1 b)), `H′` is of finite
presentation over `S`; moreover, its fibers are smooth, so `H′` is smooth over `S` (EGA IV 17.5.1). Since `S` is affine,
`u₀` therefore lifts to an `S`-morphism of preschemes:

```text
u : H ⟶ H′.
```

It then follows from Exp. III 2.1 and Exp. IX 3.1 that the composed morphism `v₀ : H ×_{S₀} S ⥲ H₀ → G₀`

<!-- original page 351 -->

also lifts to an `S`-morphism of groups:

```text
v : H ⟶ G.
```

Since `v₀` is an immersion, so is `v`. The image of `H` by `v` is therefore a subgroup scheme of `G`, of multiplicative
type, which lifts `H₀`.

**Proposition 1.2.** *Let `S` be a prescheme, `S₀` a subprescheme of `S` defined by a locally nilpotent sheaf of ideals,
`G` an `S`-prescheme in groups, flat and of finite presentation over `S`, and `H₀` a subgroup scheme of `G₀ = G ×_S S₀`
which is smooth, finite over `S₀`, of multiplicative type and central. Then there exists a unique subgroup scheme `H` of
`G`, of multiplicative type, which lifts `H₀`. Moreover `H` is central. (See XVII App. III, 1).*

<!-- label: III.XV.1.2 -->

**Proposition 1.2 bis.** *Let `S`, `G`, `S₀`, `G₀` be as above, `H` an `S`-group scheme of multiplicative type, smooth
and finite over `S`, and `u₀ : H₀ = H ×_S S₀ → G₀` a central homomorphism. Then `u₀` lifts uniquely to a homomorphism
`u : H → G`. Moreover `u` is central.*

<!-- label: III.XV.1.2bis -->

The existence of the lifting `u` in 1.2 bis is easily deduced from 1.2 by considering the graph of `u₀`. The lifting `u`
is unique and central by Exp. IX 3.4 and Exp. IX 5.1.

*Proof of 1.2.* The uniqueness of `H` and the fact that `H` is central follow from Exp. IX 5.6 b) and Exp. IX 3.4 bis.
Given uniqueness, in order to prove the existence

<!-- original page 352 -->

of `H` we may assume `S` affine and `S₀` defined by an ideal of square zero, and it suffices (1.1) to find a subscheme
of `G`, flat over `S`, which lifts `H₀`.

Since `H₀` is smooth and finite over `S₀`, we may assume — possibly after restricting `S` — that there exists an integer
`n > 0`, invertible on `S`, such that `H₀ = ₙH₀`. Consider the `n`-th power morphism in `G`:

```text
u : G ⟶ G,    x ↦ xⁿ.
```

We still denote by `ₙG` the "kernel of `u`", that is, the inverse image under `u` of the unit section of `G` (N.B. `u`
is not in general a group morphism). Granting for a moment the following lemma:

**Lemma 1.3.** *Let `k` be a field, `G` a group scheme locally of finite type over `k`, `n` an integer prime to the
characteristic of `k`, `u` the `n`-th power morphism in `G`. Then `u` is étale at every point `x` of `G` belonging to
the center of `G`.*

<!-- label: III.XV.1.3 -->

Since `G` is flat and of finite presentation over `S`, it follows from the preceding lemma and from EGA IV 17.8.2 that
if `x` is a point of `G` projecting to `s` in `S` and belonging to the center of `Gₛ`, the morphism `u` is étale at `x`.
If moreover `x` is a point of `ₙG`, then `ₙG` is étale over `S` at `x`. By hypothesis, the group `H₀` is central and
contained in `ₙG₀`, so it is in fact contained in the largest open subset `V` of `ₙG` which is étale over `S`. Since
`H₀` and `V ×_S S₀ = V₀` are étale over `S₀`, `H₀` is an open subset of `V₀` (EGA IV 17.8.7 and 17.9.1).

<!-- original page 353 -->

But then the open subprescheme of `V` having the same underlying space as `H₀` is a subscheme of `G`, flat over `S`,
which lifts `H₀`.

It remains to prove Lemma 1.3. For this, note that the largest open subset of `G` on which `u` is étale is invariant
under base field extension (EGA IV 17.8.2); this allows us to reduce to the case where `x` is rational over `k`. Let
`tₓ` denote translation by `x`, which is a `k`-automorphism of the scheme `G`. Since `x` is in the center of `G`, we
have the commutative diagram:

```text
G ──u──→ G
│        │
tₓ       tₓⁿ
│        │
▼        ▼
G ──u──→ G.
```

It therefore suffices to show that `u` is étale at the origin, but this was seen in VII_A 8.4.

### 1.2. Global lifting of finite groups

<!-- label: III.XV.1.2-global -->

**Lemma 1.4.** *Let `A` be a local ring, separated and complete for the topology defined by its maximal ideal `𝔪`, let
`S = Spec(A)`, `Sₙ = Spec(A/𝔪ⁿ)`. Then for every prescheme `X` (resp. every `S`-prescheme `X`), the canonical map*

```text
(*)    Hom(S, X) ⟶ lim_{←n} Hom(Sₙ, X)
```

*(resp.*

```text
(**)   Γ(X/S) ⟶ lim_{←n} Γ(Xₙ/Sₙ),    where Xₙ = X ×_S Sₙ)
```

*is bijective.*

<!-- label: III.XV.1.4 -->

Statement (\*\*) is an easy consequence of (*). Let us prove (*).

<!-- original page 354 -->

Let `uₙ : Sₙ → X` (`n ∈ ℕ`) be a coherent system of morphisms. The image `y` of the closed point of `Sₙ` is therefore
independent of `n`, and `uₙ` factors through `Spec(𝒪_y)`. The morphisms `uₙ` define, by passage to the projective limit,
a ring morphism

```text
ũ : 𝒪_y ⟶ lim_{←n} (A/𝔪ⁿ) = A.
```

This shows that (\*) is surjective; it is injective as soon as `A` is separated for the `𝔪`-adic topology.

**Corollary 1.5.** *Let `A` be a complete noetherian local ring, `𝔪` its maximal ideal, `S = Spec(A)`,
`Sₙ = Spec(A/𝔪ⁿ)`, `X` a finite scheme over `S` and `Y` an `S`-prescheme. Then the canonical map*

```text
Hom_S(X, Y) ⟶ lim_{←n} Hom_{Sₙ}(Xₙ, Yₙ)
```

*(where `Xₙ = X ×_S Sₙ` and similarly `Yₙ = ⋯`) is bijective.*

<!-- label: III.XV.1.5 -->

Indeed, it follows from EGA II 6.2.5 that `X` is a finite sum of local `S`-schemes finite over `S`. This reduces us to
the case where `X` itself is the spectrum of a complete noetherian local ring. But `Hom_S(X, Y) = Γ(Z/X)` where `Z` is
the `X`-prescheme `Y ×_S X`, and we apply the preceding proposition.

**Proposition 1.6.** *Let `A`, `S`, `Sₙ` be as above, and let `G` and `M` be two `S`-preschemes in groups, with `M`
finite over `S`. Then:*

*a) The canonical map*

```text
Hom_{S-gr}(M, G) ⟶ lim_{←n} Hom_{Sₙ-gr}(Mₙ, Gₙ)
```

*is bijective.* <!-- original page 355 -->

*b) If `M` is of multiplicative type and `G` is smooth over `S`, the canonical map*

```text
φ : Hom_{S-gr}(M, G) ⟶ Hom_{S₀-gr}(M₀, G₀)
```

*is surjective. Moreover, if `φ(u) = φ(u′) = u₀`, then `u` and `u′` are conjugate by an element of `G(S)` reducing to
the unit element of `G(S₀)`.*

*c) If `M` is of multiplicative type and smooth over `S`, if `G` is flat of finite type over `S`, and if `u₀ : M₀ → G₀`
is a central homomorphism, then `u₀` lifts uniquely to a homomorphism*

```text
u : M ⟶ G.
```

*Moreover `u` is central if `G` has connected fibers.*

<!-- label: III.XV.1.6 -->

*Proof.* a) Follows from 1.5, from the fact that `M ×_S M` is finite over `S`, and from the characterization of group
morphisms as those rendering commutative the well-known diagram:

```text
M ×_S M ──u×u──→ G ×_S G
   │                │
   │                │
   ▼                ▼
   M  ────u───────→ G.
```

b) By Exp. IX 3.6, one can construct a coherent system of homomorphisms `uₙ : Mₙ → Gₙ` lifting a homomorphism
`u₀ : M₀ → G₀`. Hence the first assertion of b), in view of a).

If now `u` and `u′` are two liftings of `u₀`, then `uₙ` and `u′ₙ` are conjugate

<!-- original page 356 -->

by an element `gₙ` of `G(Sₙ)` lifting the unit element of `G(S₀)` (Exp. IX 3.6); *loc. cit.* also implies that one may
choose the `gₙ` in a coherent way, and hence (1.4) coming from a section `g` of `G(S)`. The morphisms `u` and
`int(g)·u′` then coincide modulo `𝔪ⁿ` for every `n`, so they coincide (1.5).

c) The existence and uniqueness of `u` follow from a) and 1.2 bis. If `G` has connected fibers, `u` is central by Exp.
IX 5.6 a).

## 2. Infinitesimal lifting of sub-tori

<!-- label: III.XV.2 -->

<!-- original page 357 -->

### 2.1. Statement of the theorem

<!-- label: III.XV.2.statement -->

We shall give a theorem of infinitesimal lifting of sub-tori of a group prescheme which does not appeal to smoothness
hypotheses (in contrast to Exp. IX 3.6 bis) and which moreover answers a very natural question[^N.D.E-XV-1]: does it
suffice to be able to lift "enough" points of finite order of a sub-torus `T₀` in order to be assured of being able to
lift `T₀` (infinitesimally, of course)?

**Theorem 2.1.** *Let `S` be a noetherian affine scheme, `S₀` a closed subscheme of `S` defined by an ideal `J` of
square zero, `G` an `S`-prescheme in groups of finite type, `G₀ = G ×_S S₀`, `T₀` a sub-torus of `G₀`, `q` an integer
`> 0` invertible on `S`. Suppose that for every integer `n` equal to a power of `q`, there exists a subscheme `Mₙ` of
`G`, flat over `S`, such that `Mₙ ×_S S₀ = ₙT₀`. Then there exists a sub-torus `T` of `G` such that `T ×_S S₀ = T₀`.*

<!-- label: III.XV.2.1 -->

Theorem 2.1 will be useful to us through the following two corollaries:

**Corollary 2.2.** *Let `S` be a locally noetherian prescheme, `S₀` a closed subprescheme of `S` defined by a locally
nilpotent sheaf of ideals, `G` an `S`-prescheme in groups of finite type, `T₀` a sub-torus of `G₀ = G ×_S S₀`, `q` an
integer `> 0` invertible on `S`; finally, with the integer `n` ranging over powers of `q`, let `(Mₙ)` be a coherent
system*

<!-- original page 358 -->

*of `S`-subgroup schemes of `G`, of multiplicative type, which lifts the `ₙT₀` (N.B. The system of subgroups of
multiplicative type `(Mₙ)` is said to be coherent if `M_m = _m(Mₙ)` whenever the integer `m` divides `n`.) Then there
exists one and only one sub-torus `T` of `G` such that `T ×_S S₀ = T₀` and `ₙT = Mₙ` for every `n`.*

<!-- label: III.XV.2.2 -->

**Corollary 2.3.** *Let `G` be an `S`-prescheme in groups, flat and of finite presentation over `S`, `S₀` a closed
subprescheme of `S` defined by a sheaf of ideals of finite type and locally nilpotent, `T₀` a central torus of
`G₀ = G ×_S S₀`. Then there exists one and only one sub-torus `T` of `G` lifting `T₀`. Moreover `T` is central.*

<!-- label: III.XV.2.3 -->

**Remark 2.4.** We leave to the reader the task of formulating the analogue of statements 2.1, 2.2, 2.3 in which,
instead of lifting a sub-torus of `G₀`, one is given a torus `T` over `S` and one proposes to lift a morphism

```text
u₀ : T₀ ⟶ G₀
```

(one reduces to the preceding cases by considering the graph of `u₀`).

<!-- label: III.XV.2.4 -->

Let us show how Corollaries 2.2 and 2.3 are deduced from 2.1.

*Proof of Corollary 2.2.* The uniqueness of `T` follows from Exp. IX 4.8 b) and Exp. IX 4.10. To prove the existence of
`T`, we may therefore reduce to the case where `S` is affine, hence noetherian, and where `S₀` is defined by an ideal of
square zero.

<!-- original page 359 -->

**Lemma 2.5.** *Let `G` be an `S`-prescheme in groups, of finite presentation, and `H` a subgroup scheme of `G`, of
multiplicative type, smooth over `S`. Then `Centr_G(H)` is representable by a subgroup prescheme of `G`, of finite
presentation.*

<!-- label: III.XV.2.5 -->

The lemma follows from Exp. VIII 6.5 e), without smoothness hypothesis on `H`, when `G` is separated over `S`. In the
present case, one notes that the assertion to be proved is local for the fpqc topology, which allows us to assume `H`
diagonalizable, hence of the form `D_S(M)`. We may also assume `S` affine, then `S` noetherian thanks to EGA IV 8. Since
`H` is smooth over `S` and of finite type, the order `q` of the torsion subgroup of `M` is invertible on `S` (Exp. VIII
2.1 e)). It is then immediate (cf. Exp. IX 4.10) that the subgroups `ₙH`, where `n` ranges over powers of `q`, are
schematically dense in `H` (Exp. IX 4.1). But `ₙH` is a completely decomposed covering of `S` (i.e. is isomorphic to a
finite direct sum of copies of `S`), so `Centr_G(ₙH) = Zₙ` is representable as the intersection of the centralizers in
`G` of the sections of `ₙH` over `S`. It then suffices to apply the lemma:

**Lemma 2.5 bis.** *Let `S` be a noetherian prescheme, `G` an `S`-prescheme in groups of finite type, `H` a subgroup of
`G` of multiplicative type, `(Hᵢ)` an increasing filtered family of subgroups of `G` of multiplicative type, and suppose
that `Zᵢ = Centr_G(Hᵢ)` is representable by a subgroup prescheme of `G`. Then the family of `Zᵢ` is stationary.*

<!-- original page 360 -->

*If moreover the `Hᵢ` are schematically dense in `H`, one has `Zᵢ = Centr_G(H)` for `i` large enough.*

<!-- label: III.XV.2.5bis -->

To see that the family of `Zᵢ` is stationary, it suffices to show that the family of underlying sets `ens(Zᵢ)` is
stationary. Indeed, the stationary value will then be a closed subset of an open subset `U` of `G`; and, possibly
replacing `G` by `U`, we are reduced to studying a decreasing filtered family of closed subpreschemes of a noetherian
prescheme. An easy constructibility argument reduces us to the case where `S` is integral. We must then show that the
family of `ens(Zᵢ)` is stationary above some non-empty open subset of `S`. Now the generic fiber of `G` is separated
(Exp. VI_A 0.3), so, possibly restricting `S`, we may assume `G` separated over `S` (EGA IV 8). But then `Zᵢ` is closed
in `G` (Exp. VIII 6.5 e)).

To establish the last assertion of the lemma, denote by `Z` the stationary value of the family `Zᵢ`. It is clear that
`Centr_G(H)` is a subfunctor of `Z`; let us show that `Z` centralizes `H`. Let `E` be the subprescheme of `H ×_S Z`
which is the kernel of the pair of morphisms:

```text
H ×_S Z ⇒ G
(h, c) ↦ c
(h, c) ↦ hch⁻¹.
```

The prescheme `E` majorizes `Hᵢ ×_S Z` for every `i`. On the other hand, the `Hᵢ` are flat over `S`, so (EGA IV 11.10.9)
for every point `s` of `S`, the `(Hᵢ)ₛ` are schematically dense in `Hₛ` and the `Hᵢ ×_S Z` are schematically dense in
`H ×_S Z`. Since `Gₛ` is separated, `Eₛ` is closed in `(H ×_s Z)ₛ` and therefore equal to it. But then `E` is closed in

<!-- original page 361 -->

`H ×_S Z`, so equals `H ×_S Z`. This says that `Z` centralizes `H`.

Let us return to the proof of 2.2. By 2.5, `Zₙ = Centr_G(Mₙ)` is representable, and by 2.5 bis the decreasing family of
subpreschemes `Zₙ` is stationary; let `Z` be its stationary value. The group `Z` majorizes `T₀` and the `Mₙ`. Possibly
replacing `G` by `Z`, we may therefore assume the `Mₙ` central.

We are then in the conditions of application of Theorem 2.1, and there exists a sub-torus `T` of `G` lifting `T₀`. The
groups `ₙT` and `Mₙ` are then two liftings of `ₙT₀`, hence are conjugate (Exp. IX 3.2 bis) and consequently coincide,
`Mₙ` being central. The torus `T` answers the question.

*Proof of Corollary 2.3.* The uniqueness of `T` follows from Exp. IX 5.1 bis, and the fact that `T` is central follows
from IX 5.6 b). This remark allows us, by the usual procedure, to reduce to the case where `S` is affine (so `S₀` is
defined by a nilpotent ideal of finite type), then to the case where `S` is noetherian. Possibly restricting `S`, we may
assume that there exists an integer `q` invertible on `S`. Corollary 2.3 is then a consequence of 2.2 and of 1.2.

**Remark 2.6.** One easily shows that Corollary 2.3 remains true if one replaces the torus `T₀` by a smooth central
subgroup of multiplicative type of `G₀`.

<!-- label: III.XV.2.6 -->

### 2.2. Proof of 2.1

<!-- label: III.XV.2.proof -->

<!-- original page 362 -->

**a) Reduction to the case `T₀ = G_{m, S₀}`.**

Thanks to 1.1, we may assume that `Mₙ` is a subgroup of multiplicative type. Using Exp. IX 3.2 bis, we may assume that
the family of the `Mₙ` is coherent (2.2). The centralizer `Zₙ` of `Mₙ` in `G` is representable (2.5), and the filtered
family of `Zₙ` is stationary (2.5 bis). Possibly replacing `G` by `Zₙ` for `n` large enough, we may therefore assume
`T₀` and the `Mₙ` central. The uniqueness of the lifting of `T₀` is then assured (Exp. IX 5.1 bis).

Proceeding as in the proof of 1.1, we may assume that there exist an `S`-torus `T` and an `S₀`-isomorphism

```text
u₀ : T ×_S S₀ ⥲ T₀,
```

and it is equivalent to lift `u₀` or to lift `T₀`. In view of uniqueness, it suffices to prove the existence of a
lifting of `u₀` after performing a faithfully flat affine extension `S′ → S` of finite type (fpqc descent), which allows
us to assume `T = G^r_{m, S}` (Exp. X 4.5). If the restriction of `u₀` to each factor `G_m` lifts to an `S`-morphism —
necessarily central — one immediately deduces a lifting of `u₀`. In short, we may assume `T₀ = G_{m, S₀}`.

**b) Definition of the obstruction to the existence of a lifting of `T₀`.**

To prove 2.1, it suffices by 1.1 to find a subscheme of `G`, flat over `S`, which lifts `T₀`. We shall see that one can
define the obstruction to the existence of such a lifting as an element of a certain `Ext¹(·, ·)` of sheaves of modules.

<!-- original page 363 -->

Let `U` be an open subset of `G` such that `T₀` is closed in `U`, and let us still denote by `U` (resp. `U₀`) the open
subscheme of `G` (resp. `G₀`) having `U` as underlying space. The sheaf `𝒪_{T₀}`, viewed as a sheaf on `U`, is therefore
a quotient of `𝒪_{U₀}`. Let `h` be the canonical epimorphism:

```text
h : 𝒪_{U₀} ⟶ 𝒪_{T₀}.
```

**Lemma 2.7.** *The canonical map*

```text
h̃ = id_J ⊗ h : J ⊗_{S₀} 𝒪_{U₀} ⟶ J ⊗_{S₀} 𝒪_{T₀}
```

*factors (evidently uniquely) as `i ∘ j_U`, where `j_U` is the canonical epimorphism*

```text
J ⊗_{S₀} 𝒪_{U₀} ⟶ J𝒪_U ≃ J𝒪_{U₀}.
```

<!-- label: III.XV.2.7 -->

We must show that `h̃(K) = 0`, where `K` is the kernel of `j_U`. Now for every integer `n` equal to a power of `q`, we
have an epimorphism

```text
hₙ : 𝒪_{T₀} ⟶ 𝒪_{ₙT₀}
```

and since `ₙT₀` lifts to a scheme `Mₙ` flat over `S`, the canonical morphism

```text
jₙ : J ⊗_{S₀} 𝒪_{ₙT₀} ⟶ J𝒪_{Mₙ}
```

is an isomorphism.

<!-- original page 364 -->

The commutative diagram below:

```text
K ──→ J ⊗_{S₀} 𝒪_{U₀} ──j_U──→ J𝒪_U ⊂ 𝒪_U
            │             ⤡
            │ h̃           i
            ▼            ↗
       J ⊗_{S₀} 𝒪_{T₀}
            │
            │ h̃ₙ
            ▼            ≅
      J ⊗_{S₀} 𝒪_{ₙT₀} ──jₙ──→ J𝒪_{Mₙ} ⊂ 𝒪_{Mₙ}
```

shows that `h̃(K)` is contained in `Ker h̃ₙ` for every `n`, hence is contained in `⋂ₙ Ker h̃ₙ`, and it suffices to show
that this last intersection is zero. Now the sheaf `𝒪_{T₀}` is equal to the sheaf `𝒪_{S₀}[ℤ]`, the algebra of the group
`ℤ` with coefficients in `𝒪_{S₀}`, while `𝒪_{ₙT₀}` is the quotient algebra `𝒪_{S₀}[ℤ/nℤ]`.

Let `a = Σ_{m ∈ ℤ} aₘ ⊗ m` be an element of `J ⊗_{S₀} 𝒪_{T₀}`. The `aₘ` are then sections of `J`, almost all zero. Take
`n` large enough that the indices `m` for which `aₘ` is non-zero have distinct images in `ℤ/nℤ`. Then if `a ∈ Ker h̃ₙ`,
one necessarily has `a = 0`. This proves that `⋂ₙ Ker h̃ₙ = 0`, and proves 2.7.

Let then `K₀` be the kernel of `h`; consider the following diagram:

```text
                          0
                          │
                          ▼
       J𝒪_U              K₀
        ≅│                │
         ▼                ▼
   0 → J𝒪_{U₀} ────→ 𝒪_U ────→ 𝒪_{U₀} → 0
         │ i               h    │
         ▼                      ▼
  J ⊗_{S₀} 𝒪_{T₀}            𝒪_{T₀}
                                │
                                ▼
                                0.
```

The sheaf `𝒪_U` defines an element `Φ` of the group `Ext¹_{𝒪_U}(𝒪_{U₀}, J𝒪_{U₀})`. Let `Ψ` be the element of

<!-- original page 365 -->

`Ext¹_{𝒪_U}(K₀, J ⊗_{S₀} 𝒪_{T₀})` deduced from `Φ` by bifunctoriality of `Ext¹(·, ·)` through the morphisms
`K₀ → 𝒪_{U₀}` and `i : J𝒪_{U₀} → J ⊗_{S₀} 𝒪_{T₀}`. It follows from Exp. III 4.1 and from the infinitesimal flatness
criterion (cf. Exp. III 4.3) that there exists a subscheme of `U`, flat over `S`, which lifts `T₀`, if and only if `Ψ`
is zero.

But note that `T₀` is affine, so it suffices (Exp. III 4.5 and 4.6) to show that there locally on `U` exists a subscheme
flat over `S` lifting `T₀`. In short, it suffices to show that the image of `Ψ` in the sheaf

```text
ℰ = Ext¹_{𝒪_U}(K₀, J ⊗_{S₀} 𝒪_{T₀})
```

is zero. We shall still denote by `Ψ` this element of `Γ(U, ℰ)`.

**c) Reduction to the case `S` local artinian with algebraically closed residue field.**

Since `K₀` and `J ⊗_{S₀} 𝒪_{T₀}` are coherent sheaves, so is the sheaf `ℰ`; moreover `ℰ` has its support in `T₀`, since
this is the case for `J ⊗_{S₀} 𝒪_{T₀}`. To show that the section `Ψ` of `ℰ` is zero, it suffices to see that for every
point `u` of `T₀`, the image of

<!-- original page 366 -->

`Ψ` in the fiber of `ℰ` at the point `u` is zero. But the formation of the `Ext^i(·, ·)` of coherent sheaves commutes
with flat extensions of the base[^N.D.E-XV-2], so we are reduced to proving the existence of a lifting of
`T₀ ∩ Spec 𝒪_u` flat over `S`. Let `s` be the projection of `u` on `S`; we may then replace `S` by `Spec 𝒪_s` and `G` by
`G ×_S Spec 𝒪_s`.

Possibly again making a faithfully flat extension, we may assume that `𝒪_s` has an algebraically closed residue field
(EGA 0_III, 10.3.1).

Let `𝔪` be the maximal ideal of `𝒪_s` and `Sₙ = Spec 𝒪_s/𝔪ⁿ`. Suppose we have shown that for every `n > 0` the
obstruction to lifting `T₀ ×_S Sₙ = (T₀)ₙ` to a subscheme of `Gₙ = G ×_S Sₙ`, flat over `Sₙ`, is zero, and let `Tₙ` be
the unique flat lifting of `(T₀)ₙ` over `Sₙ` which is a sub-torus of `Gₙ`. It is clear that if `n > n′`, one has

```text
(Tₙ) ×_{Sₙ} Sₙ′ = Tₙ′.
```

If then `u` is a point of `T₀` projecting onto `s`, it follows from the lemma below, applied to the coherent system of
liftings `(Tₙ ∩ Spec 𝒪_u)` of `(T₀)ₙ ∩ Spec 𝒪_u`, that there indeed exists a lifting of `T₀ ∩ Spec 𝒪_u` flat over `𝒪_s`.
We are therefore reduced to proving that `Ψ` is zero when `S = Sₙ` is the spectrum of an artinian local ring with
algebraically closed residue field, and to proving:

**Lemma 2.8.** *Let `A → B` be a local homomorphism of noetherian local rings, `𝔪` the maximal ideal of `A`, `J` an
ideal of square zero of `A`, `M` a `B`-module of finite type, `A₀ = A/J`, `B₀ = B/JB`, `M₀ = M/JM`, `N₀` a quotient
`B₀`-module of `M₀` which is flat over `A₀`. For every integer `n > 0`, let `Aₙ`, `A₀,ₙ`, etc., be the objects obtained
by base extension*

<!-- original page 367 -->

*`A → A/𝔪ⁿ = Aₙ`, and let `Jₙ` be the image of `J` in `Aₙ`. For every integer `n > 0`, let `Nₙ` be a quotient
`Bₙ`-module of `Mₙ`, flat over `Aₙ`, lifting `N₀,ₙ`, and suppose that for `n ⩾ n′`, `Nₙ′` is obtained from `Nₙ` by base
extension `Aₙ → Aₙ′`. Then there exists a `B`-module `N`, quotient of `M`, flat over `A`, lifting `N₀`.*

<!-- label: III.XV.2.8 -->

*Proof of 2.8.* Let `P₀` be the kernel of the epimorphism `M₀ → N₀`. For every `n > 0`, we have the following
commutative diagram in which the horizontal rows are exact:

```text
                                       0
                                       │
                                       ▼
                                     P₀,ₙ
                                       │
                                       ▼
   0 ──→ Jₙ Mₙ ──→ Mₙ ──→ M₀,ₙ ──→ 0
            ↗
        Jₙ ⊗_{A₀,ₙ} M₀,ₙ
            ↘
                         ▼      ▼       ▼
   0 ──→ Jₙ ⊗_{A₀,ₙ} N₀,ₙ ──→ Nₙ ──→ N₀,ₙ ──→ 0
                                       ▼     ▼
                                       0     0
```

\*(*ₙ*)

Moreover, by hypothesis, the diagram `(*)_{n+1}` reduces modulo `𝔪ⁿ` to `(*)ₙ`.

The Artin–Rees lemma (Bourbaki, *Algèbre commutative*, Chap. 3 § 3 cor. 1) shows that the filtration defined on `JM`
(resp. `J ⊗_{A₀} M₀` and `J ⊗_{A₀} N₀`) by the kernels of the morphisms

<!-- original page 368 -->

```text
JM ⟶ Jₙ Mₙ,   (resp.   J ⊗_{A₀} M₀ ⟶ Jₙ ⊗_{A₀,ₙ} M₀,ₙ   and   J ⊗_{A₀} N₀ ⟶ Jₙ ⊗_{A₀,ₙ} N₀,ₙ)
```

is `𝔪B`-good, so that, passing to the projective limit on the diagrams `(*)ₙ` and denoting by `Q̂` the separated
completion of a `B`-module `Q` for the `𝔪B`-adic topology, one obtains the following commutative diagram, where the two
horizontal rows are still exact:

```text
                                       0
                                       │
                                       ▼
                                      P̂₀
                                       │
                                       ▼
   0 ──→ ĴM ──→ M̂ ──→ M̂₀ ──→ 0
           ↗
        Ĵ ⊗_{A₀} M₀
           ↘
   0 ──→ Ĵ ⊗_{A₀} N₀ ──→ lim_{←n} Nₙ ──→ N̂₀ ──→ 0
                                       ▼      ▼
                                       0      0
```

(*ˆ*)

Now `(B, 𝔪B)` is a Zariski ring and `J ⊗_{A₀} N₀` is of finite type over `B`, so it is separated for the `𝔪B`-adic
topology. The diagram `(*̂)` then shows that the morphism

```text
J ⊗_{A₀} M₀ ⟶ J ⊗_{A₀} N₀
```

deduced from the epimorphism `M₀ → N₀` factors through `JM`:

```text
J ⊗_{A₀} M₀ ──can.──→ JM
       ↘            ↙
        J ⊗_{A₀} N₀.
```

Under these conditions, it follows from Exp. III 4.1 and Exp. III 4.3 that there exists a `B`-module quotient `N` of
`M`, flat over `A`, lifting `N₀`, if and only if a certain element `g` of `E = Ext¹_B(P₀, J ⊗_{A₀} N₀)` is zero. More
precisely, the exact sequence

```text
0 ⟶ JM ⟶ M ⟶ M₀ ⟶ 0
```

defines an element `f` of `F`, where `F` is the `B`-module `Ext¹_B(M₀, JM)`, and `g` is the image of `f`

<!-- original page 369 -->

under the natural morphism `F → E` arising by bifunctoriality from the morphisms

```text
P₀ ⟶ M₀    and    JM ⟶ J ⊗_{A₀} N₀.
```

It follows from the diagram `(*̂)` and from Exp. III 4.1 that the image of `g` in `Ê`, canonically identified with
`Ext¹_{B̂}(P̂₀, Ĵ ⊗_{A₀} N₀)`, is zero. But `E` is of finite type over `B`,

<!-- original page 370 -->

so is separated for the `𝔪B`-adic topology, and consequently `g` is indeed equal to `0`, which completes the proof of
2.8.

**d) Study of `ℰ`.** We therefore suppose that `S` is the spectrum of a local artinian ring `A` with algebraically
closed residue field `k`. Let `A₀` be the ring of `S₀`, `𝔪₀` the maximal ideal of `A₀`. Since `S₀` is artinian, `T₀` is
closed in `G` (Exp. VI_B 1.4.2); we may therefore take the open subset `U` equal to `G`, so that

```text
ℰ = Ext¹_{𝒪_G}(K₀, J ⊗_{S₀} 𝒪_{T₀}).
```

Let `B₀` be the ring of the affine `S₀`-scheme `T₀ = G_{m, S₀}`, and `B′₀` the ring of the special fiber
`T₀ ×_{S₀} Spec(k) = G_{m, k}` of `T₀`. The sheaf `ℰ` is a coherent `𝒪_{T₀}`-module, so is defined by a `B₀`-module of
finite type which we shall denote `E`.

Consider the graded module associated to `E` and to the `𝔪₀ B₀`-adic filtration:

```text
Eᵣ = 𝔪₀ʳ E / 𝔪₀^{r+1} E.
```

Each `Eᵣ` is therefore a `B′₀`-module of finite type, and `Eᵣ = 0` for `r` large enough, since `S₀` is artinian.

Let then `g` be a section of `G` above `S` which on `S₀` induces a section `g₀` of `T₀`. Translation (on the left, to
fix ideas) by the element `g` defines an "automorphism of the situation" from the viewpoint of the obstruction problem
under consideration. In particular, to `g` corresponds an `S₀`-automorphism of the sheaf `ℰ` leaving the obstruction `Ψ`
fixed. More precisely, `g` defines a semi-linear automorphism of the `B₀`-module `E` (relative to the `A₀`-automorphism
of `B₀` defined by translation by `g₀` in the group `T₀`). By reduction modulo `𝔪₀^{r+1}`, `g` then defines a
semi-linear automorphism of `Eᵣ` (relative to the `k`-automorphism of `B′₀` defined by translation by
`g₀ ×_{S₀} Spec(k)` in `T₀ ×_{S₀} Spec(k)`).

**Lemma 2.9.** *For every integer `r ⩾ 0`, `Eᵣ` is a locally free `B′₀`-module.*

<!-- label: III.XV.2.9 -->

Let `x` be a point of `T₀`, `κ(x)` its residue field, `(Eᵣ)ₓ` "the fiber" of `Eᵣ` at `x`, equal to `Eᵣ ⊗_{B′₀} κ(x)`,
`ℓ(x)` the rank of `(Eᵣ)ₓ` over `κ(x)`, `ℓ` the maximum value of `ℓ(x)` as `x` ranges over the points of `T₀`. Let `L`
be the largest closed subscheme of `Spec B′₀ = G_{m, k}` above which `Eᵣ` is locally free of rank `ℓ` (TDTE IV Lemma
3.6). Let `β` be a point of `L(k)` (there is one, `L` being of finite type over `k` algebraically closed) and let `α` be
a point of `G_{m, k}(k)` of order equal to a power `n` of `q`. The point `α` is therefore rational

<!-- original page 371 -->

over `k`, and since by hypothesis `ₙT₀` lifts to a subscheme `Mₙ` étale over `S`, there exists a section `a` of `G`
above `S` which lifts `α` and which, above `S₀`, is a section of `T₀`. The remarks made above then show that the fibers
of `Eᵣ` are `k`-isomorphic at the points `β` and `αβ` of `G_{m, k}(k)`. But the points of order a power of `q` are dense
in `G_{m, k}`, and similarly their translates by `β`. Since `L` is closed in `G_{m, k}` and `G_{m, k}` is reduced, `L`
equals `G_{m, k}` and `Eᵣ` is locally free over `B′₀` of rank `ℓ`.

**e) End of the proof of Theorem 2.1.**

Let `K₀(n)` be the sheaf of ideals of `𝒪_{G₀}` defining the closed subscheme `ₙT₀`. The sheaf `K₀`[^N.D.E-XV-3] is
therefore a subsheaf of `K₀(n)`. Set, for simplicity,

```text
R = J ⊗_{S₀} 𝒪_{T₀}    and    R(n) = J ⊗_{S₀} 𝒪_{ₙT₀}.
```

The sheaf `R(n)` is therefore a quotient of `R`, and one has the diagram of morphisms:

```text
                K₀
                │
                ▼
              K₀(n)
                │
                ▼
0 ──→ J𝒪_G ──→ 𝒪_G ──→ 𝒪_{G₀} ──→ 0
        │
        ▼
        R
        │
        ▼
      R(n)
```

Using then the bifunctoriality of `Ext¹_{𝒪_G}(·, ·)`, one obtains the following commutative diagram:

```text
Ext¹_{𝒪_G}(𝒪_{G₀}, J𝒪_G)
        ↘
         Ext¹_{𝒪_G}(K₀(n), R) ──→ Ext¹_{𝒪_G}(K₀, R) = ℰ
               │                          │
               ▼                          ▼
         Ext¹_{𝒪_G}(K₀(n), R(n)) ──→ Ext¹_{𝒪_G}(K₀, R(n)).
```

Let us again denote by `Φ` the element of `Ext¹_{𝒪_G}(𝒪_{G₀}, J𝒪_G)` defined by the exact sequence

<!-- original page 372 -->

```text
0 ⟶ J𝒪_G ⟶ 𝒪_G ⟶ 𝒪_{G₀} ⟶ 0,
```

so that `Ψ` is the image of `Φ` in `ℰ`. Since `ₙT₀` lifts to a subscheme `Mₙ` of `G`, flat over `S`, the image of `Φ` in
the sheaf `Ext¹_{𝒪_G}(K₀(n), R(n))` is zero (Exp. III 4.1); *a fortiori*, the image of `Φ` in `Ext¹_{𝒪_G}(K₀, R(n))`,
which is also the image of `Ψ`, is zero.

**Lemma 2.10.** *The canonical morphism*

```text
Ext¹_{𝒪_G}(K₀, R) ⊗_{B₀} 𝒪_{ₙT₀} ⟶ Ext¹_{𝒪_G}(K₀, R(n))
```

*is injective for every integer `n`.*

<!-- label: III.XV.2.10 -->

Indeed, the affine scheme `T₀ = G_{m, S₀}` has ring

```text
B₀ = A₀[T, T⁻¹].
```

The subscheme `ₙT₀` is defined by the vanishing of the following section of `B₀`:

```text
h(n) = Tⁿ − 1,
```

which is regular (EGA 0_IV 15.2.2) and remains regular after any base change `S′₀ → S₀`. We therefore have an exact
sequence of sheaves:

```text
0 ⟶ 𝒪_{T₀} ──h(n)──→ 𝒪_{T₀} ⟶ 𝒪_{ₙT₀} ⟶ 0.
```

<!-- original page 373 -->

Since `ₙT₀` is flat over `S`, one obtains, by tensoring with `J` over `𝒪_{S₀}`, the exact sequence

```text
0 ⟶ R ──h(n)──→ R ⟶ R(n) ⟶ 0,
```

then the exact sequence of `Ext`:

```text
⋯ ⟶ Ext¹_{𝒪_G}(K₀, R) ──h(n)──→ Ext¹_{𝒪_G}(K₀, R) ⟶ Ext¹_{𝒪_G}(K₀, R(n)),
```

which completes the proof of the lemma.

The foregoing shows that for every integer `n` equal to a power of `q`, the image of `Ψ` in `ℰ/h(n)ℰ` is zero. To show
that `Ψ` is zero, it suffices to see that if `Ψ ∈ 𝔪₀ʳ ℰ`, then `Ψ ∈ 𝔪₀^{r+1} ℰ`. Let `Ψ̄` be the image of `Ψ` in `Eᵣ`.
There exists an element `Ψ(n)` of `ℰ` such that one has

```text
Ψ = Ψ(n) · h(n)    (n equal to a power of q).
```

We noted that the image `h̄(n)` of `h(n)` in `B′₀` is again `B′₀`-regular. Since `Eₛ` is locally free over `B′₀` for
every `s` (2.9), multiplication by `h̄(n)` in `Eᵣ` is injective. One deduces immediately that `Ψ(n)` is in `𝔪₀ʳ ℰ`. Let
`Ψ̄(n)` be its image in `Eᵣ`, so that one has the relation

```text
Ψ̄ = h̄(n) Ψ̄(n)    (n equal to a power of q).
```

This shows that the set `F` of points of `G_{m, k}` at which `Ψ̄` takes the value `0` contains the dense set of points
of order a power of `q`. Moreover `F` is a closed set (since `Eᵣ` is locally free over `B′₀`) and `G_{m, k}` is reduced,
so `Ψ̄` is zero.

This completes the proof of Theorem 2.1.

## 3. Characterization of a sub-torus by its underlying set

<!-- label: III.XV.3 -->

<!-- original page 374 -->

### 3.1. Statement of the theorem

<!-- label: III.XV.3.statement -->

**Notation.** If `X` is a prescheme, `ens(X)` denotes the underlying set of `X`. If `X` and `S′` are two `S`-preschemes,
`X_{S′} = X ×_S S′`, `u : X_{S′} → X` the canonical morphism, `E` a subset of `ens(X)`, one denotes by `E_{S′}` (or
`E ×_S S′`) the subset of `ens(X_{S′})` equal to `u⁻¹(E)`.

**Theorem 3.1.** *Let `S` be a locally noetherian prescheme, `G` an `S`-prescheme in groups of finite type, `q` an
integer `> 0` invertible on `S`, `E` a subset of `ens(G)`. Consider the following assertions concerning `E`:*

- *(i) The set `E` is the underlying set of a sub-torus `T` of `G`.*
- *(ii) a) For every point `s` of `S`, there exists a sub-torus `Tₛ` of `Gₛ` such that `E ∩ ens(Gₛ) = Eₛ` is the
    underlying set of `Tₛ`.*
- - b) As the integer `n` ranges over powers of `q`, there exists a coherent family (cf. 2.2) `Mₙ` of subgroup schemes
    of `G`, of multiplicative type, such that for every point `s` of `S` one has\*

```text
(Mₙ)ₛ = ₙ Tₛ.
```

- *(iii) a) As in (ii) a).*
- - b) The set `E` is locally closed in `ens(G)`, and the dimension of the fibers of `E` over `S` is locally constant.\*
- *(iv) a) As in (ii) a).*
- - b) For every `S`-scheme `S′` which is the spectrum of a complete discrete valuation ring with algebraically closed
    residue field, `E_{S′}` is the underlying set of a sub-torus of `G_{S′}`.\*

*Then one has the following implications:*

- *A) (i) ⇔ (ii) ⇒ (iii) ⇒ (iv).*
- *B) If `G` is separated over `S`, one has (iii) ⇔ (iv), and moreover `E` is closed.*
- *C) Conditions (i), (ii), (iii) (and also (iv) if `G` is separated over `S`) are equivalent in the following two
    cases:*
- - 1st case: a) The prescheme `S` is reduced, or `G` is flat over `S`, and\*
- - ```
    b) For every point `s` of `S`, `Tₛ` is a central torus of `Gₛ`.*
    ```
    ```
    - - 2nd case: `S` is normal.\*
    ```

<!-- original page 375 -->

*Moreover, in the two cases above, the torus `T` with underlying set `E` is unique.*

<!-- label: III.XV.3.1 -->

**Remarks 3.2.** a) When `S` is reduced, it is unnecessary in (ii) to assume that the family `Mₙ` is coherent, this
condition being entailed by the other hypotheses. Indeed, if the integer `m` divides `n`, the subgroups `ₘMₙ` and `M_m`
are étale over `S`, hence reduced, and have the same underlying space, so they coincide.

<!-- original page 376 -->

b) If `S` is not assumed normal, it is no longer true in general that (iii) ⇒ (i), even when `S` is reduced,
geometrically unibranched and `G` is a smooth group scheme over `S`. Indeed, consider the Borel subgroup of `SL_{2, S}`
formed by matrices of the form

```text
( t   u )
( 0  t⁻¹ ),
```

where `S` is the affine curve over a field `k` with ring

```text
k[x, y]/(y² − x³).
```

Consider then the set `E` obtained as follows: above the "cusp of `S`" (`x = y = 0`) we take the diagonal torus
(`u = 0`). Above the complementary open subset (`x ≠ 0`) we take the torus deduced from the diagonal torus by
conjugation by the element

```text
( 1  y/x )
( 0   1  ).
```

The set `E` so obtained satisfies (iii) a); on the other hand it is closed in `G`, and the reduced subscheme having `E`
as underlying set has equations

```text
xu + y(t − t⁻¹) = 0
u² − x(t − t⁻¹)² = 0.
```

<!-- original page 377 -->

This is therefore not a sub-torus of `G`, since the fiber above the cusp is not reduced.

<!-- label: III.XV.3.2 -->

**Plan of the proof of 3.1.** In a first part we shall establish the following "easy" implications:

```text
                  (ii)
              ↗        ↘
         (i)              (iv)
              ↘        ↗
                  (iii)
```

and `[(iv) ⇒ (iii) and E closed if G is separated over S]`.

The proof of the more delicate implications will be carried out in three stages:

- I) Reduction of the implication (iii) ⇒ (i) (under the hypotheses of C), 1st case) to the case where `S` is normal.
- II) (iii) ⇒ (ii) when `S` is normal.
- III) (ii) ⇒ (i).

### 3.2. Proof of the "easy" assertions contained in 3.1

<!-- label: III.XV.3.easy -->

(i) ⇒ (ii) and (iii) is trivial.

(iii) ⇒ (iv). Possibly replacing `S` by `S′`, we may assume that `S` is the spectrum of a discrete valuation ring. Let
`t` be the generic point of `S` and `s` the closed point.

Since `E` is locally closed, there exists a subprescheme of `G` which is reduced and whose underlying space is `E`; we
shall denote it `E`. The generic fiber `E_t` of `E` is therefore equal to the sub-torus `T_t` of rank `r` of `G_t` (by
(iii) a)). Let `E′` be the schematic closure of `E_t` in `E`. The prescheme

<!-- original page 378 -->

`E′` is irreducible, and its closed fiber `E′ₛ` is non-empty (it contains the unit section of `Gₛ`), so `E′ₛ` is of
dimension `r` (EGA IV 14.3.10). But then `E′ₛ` is a closed subscheme of `Eₛ`, and the latter is of dimension `r` (by
(iii) b)) and irreducible (since it has the same underlying space as `Tₛ`), so `E′ₛ` has the same underlying space as
`Eₛ`, and consequently `E′ = E`, which proves that `E` is flat over `S`.

Let now `E″` be the schematic closure of `E_t` in `G`. Then `E″` is a subprescheme in groups of `G`, flat over `S` (Exp.
VIII 7.1), which majorizes `E′`, hence `E`. The closed

<!-- original page 379 -->

fiber `E″ₛ` is an algebraic subgroup of `Gₛ` of dimension `r` (*loc. cit.*). Since `Tₛ` is a closed irreducible subset
of `Gₛ` of dimension `r`, `Eₛ` has the same underlying set as the connected component `(E″ₛ)⁰` of `E″ₛ`. Let `(E″)⁰` be
the "connected component" of `E″`, i.e. the open subgroup of `E″` complementary to the union of the irreducible
components of `E″ₛ` not containing the origin. One then has

```text
E = ens[(E″)⁰].
```

Since `E` and `E″` are reduced, one has even `E = (E″)⁰`. Finally `E` is a subgroup prescheme of `G`, flat and of finite
type over `S`, with connected fibers, hence separated (Exp. VI_B 5.2), whose generic fiber is a torus `T_t`, and whose
reduced closed fiber is a torus `Tₛ`; but then `E` is a torus (Exp. X 8.8).

(ii) ⇒ (iv). One may again assume that `S` is the spectrum of a discrete valuation ring, and we keep the notation
introduced above. The schematic closure in `G` of `T_t` is a subgroup prescheme `T` of `G`, flat over `S`, which
majorizes `Mₙ` for every integer `n` equal to a power of `q`. Consequently the closed fiber of `T` is a closed subscheme
of `Gₛ` majorizing `(Mₙ)ₛ` for every `n`, hence majorizing `Tₛ`. For dimension reasons, the "connected component" `T⁰`
of `T` has `E` as underlying set, and one concludes as above that `T⁰` is a sub-torus of `G`.

(iv) ⇒ \[(iii) and `E` closed\], if `G` is separated over `S`. Let us show that `E` is closed.[^N.D.E-XV-4] First let us
prove the lemma:

**Lemma 3.3.** *If the conditions stated in 3.1 (iv) are satisfied, `E` is a locally constructible part of `ens(G)`.*

<!-- label: III.XV.3.3 -->

By the usual method, we are reduced to studying the case where `S` is noetherian, integral, with generic point `η`.
Possibly restricting `S`, we may assume (Exp. VI_B 10.10) that there exists a subgroup scheme `H` of `G`, flat over `S`,
with connected fibers, whose generic fiber `H_η` is equal to `T_η`. To prove 3.3 it then suffices to show that
`ens(H) = E`. Now if `s` is a point of `S`, there exists, by EGA II 7.1.9, an `S`-scheme `S′`, the spectrum of a
discrete valuation ring, that one may assume complete with algebraically closed residue field, whose generic point `t′`
projects onto `η` and whose closed point `s′` projects onto `s`. By (iv) b), there exists a sub-torus `T_{S′}` of
`G_{S′}` having `E_{S′}` as underlying space. The two subprescheme in groups `T_{S′}` and `H_{S′} = H ×_S S′` of
`G_{S′}` are flat over `S′`, have connected fibers, and the same generic fiber `T_{t′}`, so they coincide with the
connected component of the schematic closure

<!-- original page 380 -->

of `T_{t′}` in `G_{S′}`. Consequently `ens(Hₛ) = Eₛ`, so `ens(H) = E`, which proves the lemma.

This being so, knowing that `E` is locally constructible, in order to see that `E` is closed it suffices to show that
every specialization in `G` of a point of `E` is a point of `E`. By the usual technique we are reduced to the case where
`S` is the spectrum of a complete discrete valuation ring with algebraically closed residue field. But then the
sub-torus of `G` of underlying space `E` ((iv) b)) is closed in `G` since `G` is separated (Exp. VIII 7.12).

### 3.3. Continuation of the proof of 3.1

<!-- label: III.XV.3.cont -->

**I) Reduction of (iii) ⇒ (i) (C, 1st case) to the case where `S` is normal.**

**a) Reduction to the case `S` affine reduced.** We therefore assume that for every point `s` of `S`, `Eₛ` is the
underlying space of a central sub-torus of `Gₛ`. The uniqueness of `T` then follows from Exp. IX 5.1 bis, and moreover
`T` will necessarily be central (*loc. cit.*). In view of uniqueness, to prove the existence of `T` we may assume `S`
noetherian, affine of ring `A`. If `S` is not reduced, by hypothesis `G` is flat over `S`. By 2.3 it then suffices to
solve the problem for `S_{red}` and `G ×_S S_{red}`. We may therefore assume in addition that `S` is reduced.

**b) Reduction to the case where the ring `A` is of finite type over `ℤ`.** Let us first prove two lemmas:

<!-- original page 381 -->

**Lemma 3.4.** *Let `k` be a field, `G` a `k`-algebraic group, `E` a subset of `G`, `k′` an extension of `k`, `T_{k′}` a
sub-torus of `G_{k′}` having `E_{k′}` as underlying space. Then, if `T_{k′}` is central or if `k` is perfect, `E` is the
underlying set of a sub-torus of `G_k`.*

<!-- label: III.XV.3.4 -->

Indeed, by fpqc descent it suffices to show that the two inverse images of `T_{k′}` in `G_{k″}`, where `k″ = k′ ⊗_k k′`,
coincide. Now they have the same underlying space, namely the inverse image of `E`. If `T_{k′}` is central, the lemma is
a consequence of Exp. IX 5.1 bis. If `k` is perfect, `k″` is reduced and the two inverse images of `T_{k′}`, being
smooth over `k″`, are reduced, hence coincide.

**Remark 3.5.** It follows from the preceding lemma that in the statement of 3.1 (iv), property (iv) a) is a consequence
of (iv) b) in the two following cases:

1. One assumes that the residue fields of the points of `S` are perfect.
1. For every `S′` as in (iv) b), one assumes that the torus with underlying space `E_{S′}` is central in `G_{S′}`.

<!-- label: III.XV.3.5 -->

**Lemma 3.6.** *Let `S` be a prescheme projective limit of affine schemes `Sᵢ` (cf. EGA IV 8), `H` an `S`-group scheme
of multiplicative type and of finite type. Then there exist an index `i`, an `Sᵢ`-group scheme `Hᵢ` of multiplicative
type and of finite type, and an `S`-isomorphism*

```text
Hᵢ ×_{Sᵢ} S ⥲ H.
```

*If moreover `H` is isotrivial, one may assume `Hᵢ` isotrivial.*

<!-- label: III.XV.3.6 -->

<!-- original page 382 -->

Since `H` is of finite type over `S`, `H` is in fact of finite presentation over `S` (Exp. IX 2.1 b)); there therefore
exist an index `ℓ` and an `S_ℓ`-group scheme `H_ℓ` such that `H_ℓ ×_{S_ℓ} S` is isomorphic to `H` (Exp. VI_B 10).
Setting `Hᵢ = H_ℓ ×_{S_ℓ} Sᵢ`, one therefore has `H ≅ Hᵢ ×_{Sᵢ} S` for every `i ⩾ ℓ`.

Since `H` is of finite type over `S`, `H` is quasi-isotrivial (Exp. X 4.5), hence trivialized by an étale surjective
morphism `S′ → S`. Using the quasi-compactness of `S`, one easily sees that there exist a covering of `S` by a finite
number of affine open subsets `S_α`, and for every `α` an étale, surjective and finitely presented morphism `S′_α → S_α`
trivializing `H|S_α`. This covering `(S_α)` of `S` then comes from a covering `(S_{i, α})` of `Sᵢ` for `i` large enough
(EGA IV 8). Possibly replacing `Sᵢ` by `S_{i, α}` and `S` by `S_α`, we may therefore assume that `H` is trivialized by
an étale surjective morphism `S′ → S` of finite presentation. For `i` large enough, there then exist a prescheme `S′ᵢ`,
an étale surjective morphism `S′ᵢ → Sᵢ` of finite presentation, and an `S`-isomorphism `S′ᵢ ×_{Sᵢ} S → S′` (EGA IV
17.16). Set then for `j` large enough:

```text
S′_j = S′ᵢ ×_{Sᵢ} S_j,    H′_j = H_j ×_{S_j} S′_j,    H′ = H ×_S S′.
```

Given the choice of `S′`, there exist a finitely generated abelian group `M` and an `S′`-isomorphism of group schemes
`D_{S′}(M) ⥲ H′`. Since the `S′ᵢ` are quasi-compact and `S′ = lim S′ᵢ`, it follows from Exp. VI_B 10 that there exist an
index `j` and an `S′_j`-isomorphism of group schemes

```text
D_{S′_j}(M) ⥲ H′_j.
```

But this says that `H_j` is a quasi-isotrivial group of multiplicative type.

<!-- original page 383 -->

When `H` is isotrivial, one proceeds analogously, using a trivialization of `H` by a finite étale morphism `S′ → S`.

This being so, we can carry out the announced reduction b). The ring `A` of `S` is a filtered inductive limit of its
subrings `Aᵢ` of finite type over `ℤ`. Let `Sᵢ = Spec Aᵢ`, `u_j : S → S_j` and `u_{jk} : S_k → S_j` (`k ⩾ j`) the
transition morphisms. Since `S` is noetherian and `G` is of finite presentation over `S`, there exist an index `i` and
an `Sᵢ`-prescheme in groups `Gᵢ`, of finite type over `Sᵢ`, such that `G` is `S`-isomorphic to `Gᵢ ×_{Sᵢ} S`. Similarly,
since `E` is locally closed in `G`, we may assume that there exists a locally closed subset `Eᵢ` of `Gᵢ` such that
`E = Eᵢ ×_{Sᵢ} S` (EGA IV 8.3.11). For every `j > i`, let `G_j = Gᵢ ×_{Sᵢ} S_j` and `E_j = Eᵢ ×_{Sᵢ} S_j`, and let `Q_j`
be the set of points `s` of `S_j` such that `(E_j)ₛ` is the underlying set of a central sub-torus of `(G_j)ₛ`.

It follows from 3.4 that `Q_k = u_{jk}⁻¹(Q_j)` for `k ⩾ j`, and by hypothesis `ens(S) = u_j⁻¹(Q_j)` for `j ⩾ i`.
Moreover, I claim that `Q_j` is ind-constructible (EGA IV 1.9.4). Indeed, since `S_j` is noetherian, it suffices (EGA IV
1.9.10) to see that if `S` is a noetherian integral scheme with generic point `η`, and if `E_η` is the underlying set of
a central sub-torus `T_η` of `G_η`, there exists a neighborhood `U` of `η` such that for every point `s` of `U`, `Eₛ`
has the same property. Now, possibly restricting `S`, we may assume that the

<!-- original page 384 -->

center `Z` of `G` is representable and that there exists a subgroup scheme `T` of `G` whose generic fiber is `T_η` (VI_B
§ 10). But then `ens(T)` and `E` are two locally closed subsets of `ens(G)` which coincide on the generic fiber; one may
therefore find a neighborhood `U` of `η` such that, above `U`, `ens(T) = E` (EGA IV 8.3.11). For the same reasons, one
may assume that above `U`, `T` is central, since `T` is a torus (3.6).

Knowing now that `Q_j` is ind-constructible, it follows from EGA IV 8.3.4 that `Q_j = ens(S_j)` for `j` large enough. We
may then replace `S`, `G`, `E` by `S_j`, `G_j`, `E_j`, which reduces us to the case where `S` is an affine reduced
scheme of finite type over `ℤ`.

**c) Reduction to the case where `S` is the spectrum of a complete reduced noetherian local ring.** Owing to the
uniqueness of the torus of underlying set `E`, the usual technique (EGA IV 8) and Lemma 3.6 allow us to replace `S` by
the spectrum of the local ring `A` of a point of `S`. Let `Ŝ` be the spectrum of the completion `Â` of `A` for the
topology defined by the maximal ideal. Since `A` is the localization of a finitely generated algebra over `ℤ`, `Ŝ` is
still

<!-- original page 385 -->

reduced (EGA IV 7.6.5). I claim that it suffices to solve the problem after the base change `Ŝ → S`. Indeed if `T̂` is
the sub-torus of `G_{Ŝ}` with underlying space `E_{Ŝ}`, its two inverse images in `G_{Ŝ} ×_S Ŝ` are two central sub-tori
with the same underlying space, so they coincide (Exp. IX 5.1 bis), and by fpqc descent, `T̂` comes from a torus `T` of
`G` which answers the question (cf. 3.4).

**d) A descent lemma.** Let us recall the following properties of finite morphisms which were noted in TDTE I: Let `S`
and `S′` be two preschemes and `u : S′ → S` a finite morphism. Then:

1. The morphism `u` is an epimorphism if and only if the canonical morphism of sheaves `𝒪_S ⟶ u_*(𝒪_{S′})` is injective.
1. The morphism `u` is an effective epimorphism (Exp. IV 1.3) if and only if the canonical diagram
    `0 ⟶ 𝒪_S ⟶ u_*(𝒪_{S′}) ⇒ u_*(𝒪_{S′}) ⊗_{𝒪_S} u_*(𝒪_{S′})` is exact.
1. If moreover `S` is noetherian and if `u` is an epimorphism, `u` is the composite of a finite sequence of effective
    finite epimorphisms.

We are then in a position to prove the following lemma, whose proof uses a technique of non-flat descent:

**Lemma 3.7.** *Let `S` be a locally noetherian prescheme, `G` an `S`-prescheme in groups of finite type, `S′` a
prescheme and `u : S′ → S` a finite morphism. For every `S`-prescheme `T`, let `M(T)` denote the set of subgroups of
multiplicative type of `G_T`*

<!-- original page 386 -->

*(resp. the set of central subgroups of multiplicative type of `G_T`), so that `M` is in a natural way a contravariant
functor defined on `Sch/S`. Then, if `u` is an effective epimorphism (resp. an epimorphism), the diagram of sets*

```text
(*)    M(S) ⟶ M(S′) ⇒ M(S′ ×_S S′)
```

*is exact.*

<!-- label: III.XV.3.7 -->

*Proof.* i) **Reduction to the case where `u` is an effective epimorphism.** We are then interested in the functor of
central subgroups of multiplicative type of `G`. The injectivity of `M(S) → M(S′)` is a local question on `S`, and, this
injectivity being granted, the exactness of (\*) becomes a local problem on `S`. We may therefore assume `S` affine
noetherian.

Let us study the case where `u : S′ → S` is the composite of two finite epimorphisms:

```text
S′ ──v──→ S″ ──w──→ S.
```

I claim that if the two diagrams

```text
(*)′    M(S″) ⟶ M(S′) ⇒ M(S′ ×_{S″} S′)
(*)″    M(S) ⟶ M(S″) ⇒ M(S″ ×_S S″)
```

are exact, then so is (\*).

Indeed the injectivity of `M(S) → M(S′)` is clear. If now `T′` is an element of `Ker M(S′) ⇒ M(S′ ×_S S′)`, *a fortiori*
`T′` belongs to `Ker M(S′) ⇒ M(S′ ×_{S″} S′)`, so by exactness of (\*)′ comes from a unique element `T″` of `M(S″)`. It
suffices

<!-- original page 387 -->

to show that `T″` belongs to `Ker M(S″) ⇒ M(S″ ×_S S″)`, since, by exactness of (\*)″, `T″` will descend to `S`. Let
`T″₁` and `T″₂` be the two inverse images of `T″` in `M(S″ ×_S S″)`. Since these are two central subgroups of
multiplicative type of `G_{S″ ×_S S″}`, to show that `T″₁ = T″₂` it suffices to see that they have the same fibers (Exp.
IX 5.1 bis). Consider the commutative diagram

```text
S′ ←──── S′ ×_S S′
│          │
v          v × v
▼          ▼
S″ ←──── S″ ×_S S″.
```

The morphism `v` is a finite epimorphism, hence is dominant (property (a) above) and closed, hence is surjective, and
the same is true of `v × v`. Let `x″` be a point of `S″ ×_S S″` and `x′` a point of `S′ ×_S S′` above `x″`. It follows
from commutativity of the diagram above that the two inverse images of `(T″₁)_{x″}` and `(T″₂)_{x″}` in `G_{x′}`
coincide, so `(T″₁)_{x″} = (T″₂)_{x″}` (EGA IV 2.2.15).

What precedes, and an immediate induction on the number of factors of a factorization of `u : S′ → S` into effective
epimorphisms (property (c) recalled above), show that to prove the exactness of (\*) in the case of central subgroups of
multiplicative type, we may restrict to the case where `u` is an effective epimorphism. Finally, using once again Exp.
IX 5.1 bis, one sees that it suffices to prove 3.7 when `M` is the functor of subgroups of multiplicative type of `G`
and `u` an effective epimorphism.

ii) **Injectivity of `M(S) → M(S′)`.** Since `u : S′ → S` is an epimorphism, the canonical

<!-- original page 388 -->

morphism `𝒪_S ⟶ u_*(𝒪_{S′})` is injective; moreover an `S`-group of multiplicative type is flat over `S`; the
injectivity of `M(S) → M(S′)` is therefore a consequence of the more general following lemma:

**Lemma 3.8.** *Let `f : X → S` and `g : S′ → S` be two morphisms of preschemes, `ℱ` a quasi-coherent `𝒪_X`-module,
`X′ = X ×_S S′`, `ℱ′ = ℱ ⊗_{𝒪_S} 𝒪_{S′}`, `Q(ℱ)` the set of quotient `𝒪_X`-modules `𝒢` of `ℱ` which are quasi-coherent
and flat over `S`, `Q(ℱ′)` the analogue relative to `ℱ′`, `X′` and `S′`. Suppose `g` is quasi-compact and
`𝒪_S → g_*(𝒪_{S′})` injective; then the canonical map*

```text
Q(ℱ) ⟶ Q(ℱ′)
𝒢 ↦ 𝒢 ⊗_{𝒪_S} 𝒪_{S′}
```

*is injective.*

<!-- label: III.XV.3.8 -->

Indeed, one may assume `S` affine, then `X` affine. The morphism `g` being quasi-compact, `S′` is then a union of a
finite number of affine open subsets `S′ᵢ`. Possibly replacing `S′` by `∐ S′ᵢ` (an operation which preserves the
injectivity of `𝒪_S → g_*(𝒪_{S′})`), one may assume `S′` affine. One is then reduced to proving the following lemma,
whose proof is immediate:

<!-- original page 389 -->

**Lemma 3.9.** *Let `A → A′` be an injective homomorphism of rings, `M` an `A`-module, `N = M/P` a quotient `A`-module
flat over `A`, `M′ = M ⊗_A A′`, `N′ = N ⊗_A A′ = M′/P′`. Then `P` is the inverse image of `P′` under the canonical
homomorphism `M → M′` (so `N` and `P` are known when one knows `N′` and `P′`).*

<!-- label: III.XV.3.9 -->

iii) **Exactness of 3.7 (\*) at `M(S′)`.** Let `T′` be an element of `Ker M(S′) ⇒ M(S′ ×_S S′)`. Suppose we have proved
iii) when `S` is the spectrum of a noetherian local ring. For every point `s` of `S`, there then exists a subgroup of
multiplicative type `Tₛ` of `G ×_S Spec(𝒪_{S, s})` which comes by descent from `T′ ×_{S′} u⁻¹ Spec(𝒪_{S, s})`. By (Exp.
VI_B § 10 and 3.6), there exist a neighborhood `U` of `s` in `S` and a subgroup scheme `T` of `G` above `U` which is of
multiplicative type and which extends `Tₛ`. Let `U′` be the inverse image of `U` in `S′`. One then knows two subschemes
of `G′|U′`: `T′|U′` and `T ×_U U′`, which coincide on `u⁻¹(Spec(𝒪_{S, s}))`. If one regards `u⁻¹(Spec(𝒪_{S, s}))` as the
projective limit of the schemes `u⁻¹(V)` where `V` ranges over the open neighborhoods of `s` in `U`, it follows from EGA
IV 8 that there exists an open neighborhood `V` of `s` in `U` such that `T ×_U U′` and `T′` coincide above `u⁻¹(V)`. So
with the hypotheses made, `T′` descends locally on `S`; but, owing to the uniqueness proved in ii), `T′` then descends
globally on `S`. In short, it suffices to prove iii) when `S` is the spectrum of a noetherian local ring.

<!-- original page 390 -->

Let then `Ŝ` denote the spectrum of the completion of the ring of `S`, and let `S″ = S′ ×_S S′`, `Ŝ′ = Ŝ ×_S S′`,
`Ŝ″ = Ŝ ×_S S″ = Ŝ′ ×_{Ŝ} Ŝ′`. I claim it suffices to show that the diagram

```text
(*)    M(Ŝ) ⟶ M(Ŝ′) ⇒ M(Ŝ″)
```

is exact at `M(Ŝ′)`. This follows from the commutative diagram below, in which the second row is exact at `M(Ŝ′)` by
hypothesis, the first two columns are exact (fpqc descent), and the map `f` is injective as follows from ii) applied to
the finite epimorphism

```text
Ŝ′ ×_{Ŝ} Ŝ′ ⟶ Ŝ ×_S Ŝ
```

deduced from `S′ → S` by the flat base change `Ŝ ×_S Ŝ → S`:

```text
M(S) ────→ M(S′) ───⇒───→ M(S″)
  │            │             │
  ▼            ▼             ▼
M(Ŝ) ────→ M(Ŝ′) ───⇒───→ M(Ŝ″)
  │ ▼          │ ▼
M(Ŝ ×_S Ŝ) ──f──→ M(Ŝ′ ×_{S′} Ŝ′)
```

(the diagram-chase is left to the reader). It follows from the characterization (b) of effective finite epimorphisms
that the morphism `Ŝ′ → Ŝ`, deduced from `S′ → S` by the flat base change `Ŝ → S`, is again an effective finite
epimorphism. We are therefore reduced to the case where furthermore `S` is the spectrum of a complete noetherian local
ring.

<!-- original page 391 -->

Let `S₀` denote the reduced subscheme of `S` whose underlying space is the closed point of `S`. Let `T′` be an element
of `Ker M(S′) ⇒ M(S″)`, `T′₀` its image in `M(S′₀)`. Since `S″₀ = S′₀ ×_{S₀} S′₀` is faithfully flat over `S₀`, there
exists an `S`-subgroup of multiplicative type `T′_{S₀}` of `G_{S₀}` whose inverse image in `G_{S″₀}` is `T′_{S′₀}` (fpqc
descent). But `S` is local complete noetherian, so there exist an `S`-group of multiplicative type `T` and an
`S₀`-morphism `u₀ : T ×_S S₀ → T′_{S₀}` (Exp. X 3.3). The inverse image `u′₀` of `u₀` above `S′₀` extends uniquely to an
`S′`-isomorphism `u′ : T_{S′} → T′`, still by Exp. X 3.3 (note that `S′`, being finite over `S` local complete, is the
sum of a finite number of complete local schemes). The two inverse images of `u′` above `S″` are two morphisms of
`T_{S″}` into `T″` which coincide on `S₀ ×_S S″`, so they coincide (*loc. cit.*). Since `T` is flat over `S` and
`S′ → S` is a finite effective epimorphism, it follows from TDTE I page 8 that the diagram

```text
Hom_S(T, G) ⟶ Hom_{S′}(T_{S′}, G_{S′}) ⇒ Hom_{S″}(T_{S″}, G_{S″})
```

is exact. So `u′` comes from a morphism of preschemes `u : T → G`. Similarly `T ×_S T` is flat over `S`, and
consequently the map

```text
Hom_S(T ×_S T, G) ⟶ Hom_{S′}(T_{S′} ×_{S′} T_{S′}, G_{S′})
```

is injective. One deduces immediately that `u` is a morphism of groups, since this is so of `u′`. Moreover `u` is a
monomorphism. Indeed, note first that `Ker u` is flat over `S`, since to establish this fact one may assume `S` artinian
local (EGA 0_III 10.2.2), hence `G` separated (Exp. VI_A 0.3); but then `Ker u` is of multiplicative type (Exp. IX 6.8),
hence is flat over `S`. Since `Ker(u) ×_S S′ = Ker(u′) = 0`, one has `Ker(u) = 0` (3.8). But `u` being a monomorphism is
an immersion (Exp. VIII, remarks 7.13), and the image group `u(T)` is indeed an element of `M(S)` whose image in `M(S′)`
is `T′`. This completes the proof of 3.7.

**e) End of the proof of I).**

<!-- original page 392 -->

We are reduced by reduction c) to the case where `S` is the spectrum of a complete reduced noetherian local ring `A`.
Let `S′` be the spectrum of the normalization `A′` of `A`, which is finite over `A` by Nagata (EGA 0_IV 23.1.5);
`S′ → S` is an epimorphism since `A` embeds injectively into `A′`. Suppose then that there exists a torus `T′` of
`G_{S′}` having `E_{S′}` as underlying space. The two inverse images of `T′` in `G_{S′ ×_S S′}` are two central sub-tori
with the same underlying space, so they coincide (Exp. IX 5 bis); hence, by 3.7, `T′` comes from a central sub-torus `T`
of `G_S` which evidently has `E` as underlying space. It therefore suffices to prove the existence of `T′`, which
reduces us to the case where `S` is normal and completes the proof of I).

**II) Proof of (iii) ⇒ (ii) when `S` is normal.**

We may restrict to the case where `S` is integral; let `t` be its generic point. For every integer `n` equal to a power
of `q`, let `ₙG` be the subprescheme of `G` "kernel" of the `n`-th power morphism in `G`. Since `E` is locally closed in
`G` (by (iii) b)), the intersection of `ens(ₙG)` with `E` is locally closed in `ens(G)`; let us then denote by `E(n)`
the reduced subprescheme of `G` having `ens(ₙG) ∩ E` as underlying space.

Let us show that the structural morphism `E(n) → S` is separated and universally open. For these two properties we have
a valuative criterion (EGA II 7.2.3 and

<!-- original page 393 -->

EGA IV 14.5.8). Let then `S′` be an `S`-scheme which is the spectrum of a complete discrete valuation ring with
algebraically closed residue field. We have shown that 3.1 (iii) ⇒ 3.1 (iv), so there exists a sub-torus `T′` of
`G_{S′}` having `E_{S′}` as underlying space. Now `ₙT′` is finite and étale over `S′`, hence separated and universally
open over `S′`, and the same is true of `E(n) ×_S S′`, which has the same underlying space as `ₙT′`.

Moreover, the fibers of `E(n)` have the same number of geometric points, namely `rⁿ` if `r` is the rank of the torus
`T_t`. Finally, the generic fiber `E(n)_t`, being reduced, is equal to `ₙT_t`, hence is étale over `Spec(t)`. Since `S`
is normal, it then follows from SGA I 10.11 that `E(n)` is an étale covering of `S`.

If `s` is a point of `S`, `E(n)_s` is étale over `Spec κ(s)`, hence reduced, and consequently coincides with the group
of multiplicative type `ₙTₛ`. Let us show that `E(n)` is a subgroup prescheme of `G`. Indeed, let `m` be the morphism

```text
E(n) ×_S E(n) ⟶ G
```

induced by the multiplication in `G`. The underlying map `ens(m)` factors through `E(n)`, so `m` factors through the
prescheme `E(n)`, since its source `E(n) ×_S E(n)` is étale over `S`, hence reduced. It then follows from Exp. X 4.8 a)
that `E(n)` is a subgroup of multiplicative type. As already noted (3.2 a)), the family of subgroups `E(n)` is
necessarily coherent. We have therefore proved that (iii) ⇒ (ii) when `S` is normal.

<!-- original page 394 -->

**III) Proof of (ii) ⇒ (i).**

In fact we shall show that there exists a unique sub-torus `T` of `G` with underlying space equal to `E` and such that
`ₙT = Mₙ` for every `n` equal to a power of `q`. The uniqueness of `T` follows simply from Exp. IX 4.8 b). To establish
the existence of `T`, in view of uniqueness, we may successively assume:

a) `S` is noetherian.

b) The `Mₙ` are central subgroups. Indeed, it suffices to replace `G` by `Zₙ = Centr_G(Mₙ)` for `n` large enough (2.5
and 2.5 bis).

c) `S` is the spectrum of a local ring. Suppose indeed the problem solved after every base change `Spec(𝒪_{S, s}) → S`
where `s` ranges over the points of `S`. Let `Tₛ` be the sub-torus of `G ×_S Spec(𝒪_{S, s})` thus obtained. For every
`s` there then exist an open neighborhood `U` of `s` and a sub-torus `T` of `G|U` extending `Tₛ` (Exp. VI_B § 10 and
3.6). We have shown that 3.1 (ii) ⇒ 3.1 (iv); since `S` is noetherian, `E` is therefore constructible (3.3).
Consequently, possibly restricting `U`, we may assume that `ens(T) = E ×_S U` (EGA IV 9.5.2). But then, for every
integer `n` equal to a power of `q`, `ₙT` and `Mₙ ×_S U` are two subgroups of multiplicative type of `G|U` with the same
fibers, hence which coincide, `Mₙ` being central (Exp. IX 5.3 bis). In short, with the hypotheses made, there exists a
solution locally on `S`, hence by uniqueness, there exists a global solution.

<!-- original page 395 -->

d) `S` is the spectrum of a complete noetherian local ring, and if `s` is the closed point, `Tₛ` is trivial. This
follows from EGA 0_III 10.3.1 and from fpqc descent.

e) `S` is reduced. One applies 2.2.

f) `S` is normal. One applies Nagata's finiteness theorem (EGA 0_IV 23.1.5) and Lemma 3.7 in the case of central
sub-tori.

These reductions being made, since `Tₛ` is trivial, `(Mₙ)ₛ` is trivial, so `Mₙ` is trivial (Exp. X 3.3). If `t` is a
point of `S`, the subgroups `ₙT_t` of `T_t` are therefore trivial for every `n` equal to a power of `q`, and it follows
easily from Exp. X 1.4 that `T_t` itself is trivial. It then suffices to prove the lemma:

**Lemma 3.10.** *Under the hypotheses of 3.1 (ii), suppose in addition that `S` is noetherian and normal and that for
every point `s` of `S`, `Tₛ` is a trivial torus. Then there exists a unique sub-torus `T` of `G` with underlying space
equal to `E`, such that `ₙT = Mₙ` for every `n` equal to a power of `q`. Moreover `T` is trivial.*

<!-- label: III.XV.3.10 -->

The uniqueness of `T` follows from the fact that `T`, being smooth over `S`, is reduced. To prove the existence, we may
assume `S` irreducible with generic point `η`. Let `r` be the rank of `T_η`, `T⁰ = G^r_{m, S}`, `u_η` an isomorphism of
`T⁰_η` onto `T_η`, `ₙu_η` the restriction of `u_η` to `ₙT⁰_η`. Since `ₙT⁰` and `Mₙ` are trivial, there exists a unique
extension `ₙu` of `ₙu_η` to an `S`-isomorphism of `ₙT⁰` onto `Mₙ`. I claim that for every point `s` of `S` there exists
a group isomorphism, necessarily unique:

```text
uₛ : T⁰ₛ ⥲ Tₛ
```

extending `ₙuₛ` for every `n` equal to a power of `q`. Indeed, let `S₁` be an `S`-scheme,

<!-- original page 396 -->

spectrum of a complete discrete valuation ring with algebraically closed residue field, whose generic point `t₁`
projects onto `η` and whose closed point `s₁` projects onto `s` (EGA II 7.1.9). It follows from the proof of 3.1 (ii) ⇒
3.1 (iv) that there exists a sub-torus `T₁` of `G_{S₁}` such that `(Mₙ)_{S₁} = ₙT₁` for every `n` equal to a power of
`q`. Since `S₁` is normal, `T₁` is isotrivial (Exp. X 5.16), and it follows from the classification of isotrivial tori
(Exp. X 1.2) and from SGA 1 V 8.2 that `T₁`, having trivial generic fiber, is trivial. One may therefore extend the
isomorphism `u_η ×_η t₁` to an `S₁`-isomorphism of group schemes

```text
u₁ : T⁰ ×_S S₁ ⥲ T₁.
```

The restriction of `u₁` to `ₙT⁰ ×_S S₁` on the one hand, and `ₙu ×_S S₁` on the other, coincide on the generic fiber by
construction, hence coincide. The restriction `u_{1, s₁}` of `u₁` to the closed fiber thus realizes the desired
extension after the residue field extension `κ(s) → κ(s₁)`. It then follows from Exp. IX 4.8 a) and from fpqc descent
that `u_{1, s₁}` descends to `κ(s)` to a group isomorphism `uₛ : T⁰ₛ ⥲ Tₛ` answering the question.

Moreover, `T⁰` is smooth over `S` which is normal, hence is normal. It then follows from an easy extension criterion for
rational maps (EGA IV4 20.4.6) that for the existence of an `S`-morphism `u : T⁰ → G` whose restriction to `T⁰ₛ`, for
every point `s` of `S`, is the composite morphism

```text
T⁰ₛ ──uₛ──→ Tₛ ⟶ Gₛ,
```

it is necessary and sufficient that this be the case after every base change `S₁ → S` where `S₁` is the spectrum

<!-- original page 397 -->

of a complete discrete valuation ring with algebraically closed residue field.

Now in the present case, a reasoning analogous to the one just made shows that the extension condition is indeed
satisfied. Let `u` denote the `S`-morphism `T⁰ → G` thus obtained.

Let us show that `u` is indeed a morphism of groups. Let `m_{T⁰}` (resp. `m_G`) be the morphism defining the
multiplication in `T⁰` (resp. `G`). We must verify that `m_G ∘ (u ×_S u) = u ∘ m_{T⁰}`. Now the subprescheme of
coincidences of these two morphisms is a subprescheme of `T⁰ ×_S T⁰`, which majorizes the fibers (since `uₛ` is a group
morphism), so has the same underlying space as `T⁰ ×_S T⁰`, hence is equal to it, since `T⁰ ×_S T⁰` is smooth over `S`,
hence reduced.

Finally, note that `u` is a monomorphism (since this is so on the fibers), hence is an immersion (Exp. VIII 7.9). The
image of `T⁰` by `u` is then a sub-torus of `G` having `E` as underlying set.

This completes the proof of Theorem 3.1.

## 4. Characterization of a sub-torus `T` by the subgroups `ₙT`

<!-- label: III.XV.4 -->

<!-- original page 398 -->

### 4.1. Statement of the main theorem

<!-- label: III.XV.4.statement -->

**Theorem 4.1.** *Let `S` be a locally noetherian connected prescheme, `G` an `S`-prescheme in groups of finite type
over `S`, `q` an integer `> 1` invertible on `S`, `r` a positive integer. For every integer `n` equal to a power of `q`,
let `M(n)` be a subgroup scheme of `G`, of multiplicative type and of type `(ℤ/nℤ)ʳ`. Suppose:*

- *a) The family of subgroups `M(n)` is coherent, that is, if the integer `m` divides `n`, one has*

```text
ₘM(n) = M(m).
```

- *b) There exists a point `s` of `S` and a sub-torus `Tₛ` of `Gₛ` such that*

```text
M(n)ₛ = ₙTₛ    for every n.
```

- *c) For every point `t` of `S`, there exists a closed affine subscheme `F_t` of `G_t` majorizing `M(n)_t` for every
    `n`.*

*Then there exists one and only one sub-torus `T` of `G` such that `ₙT = M(n)` for every `n` equal to a power of `q`.*

<!-- label: III.XV.4.1 -->

One has an analogous theorem concerning the lifting of morphisms:

**Theorem 4.1 bis.** *Let `S`, `G` and `q` be as above, `T` an `S`-torus, and for every integer `n` equal to a power of
`q`, let `u(n)` be an `S`-group morphism `ₙT → G`. Suppose:*

- *a) The family of morphisms `u(n)` is coherent, i.e., if `m` divides `n`, one has*

<!-- original page 399 -->

```text
u(m) = u(n)|_{ₘT}.
```

- *b) There exists a point `s` of `S` and a group morphism `uₛ : Tₛ → Gₛ` such that `uₛ|_{ₙTₛ} = u(n)ₛ` for every `n`
    equal to a power of `q`.*
- *c) For every point `t` of `S`, there exists a closed affine subscheme `F_t` of `G_t` majorizing `u(n)_t(ₙT_t)` for
    every `n`.*

*Then there exists a unique group morphism `u : T → G` such that for every `n` equal to a power of `q`, the restriction
of `u` to `ₙT` is equal to `u(n)`.*

<!-- label: III.XV.4.1bis -->

**Remark 4.2.** Using the lower semicontinuity of the abelian rank of a flat group prescheme of finite type over the
spectrum of a discrete valuation ring (cf. Exp. X 8.7), one can, in the statements of 4.1 and 4.1 bis, weaken condition
c) by simply requiring that the required closed affine subscheme `F_t` exists for every maximal point `t` of `S`.

<!-- label: III.XV.4.2 -->

Let us show how 4.1 bis follows from 4.1. Let `G′ = G ×_S T`. For every integer `n` equal to a power of `q`, consider
the group morphism

```text
v(n) : ₙT ⟶ G′
```

whose projections to `G` and `T` are respectively `u(n)` and the canonical immersion `ₙT → T`. The morphism `v(n)` is
therefore an immersion; let `M(n)` be the image subgroup. It is clear that the family of subgroups `M(n)` is coherent in
the sense of 4.1, that the group `M(n)ₛ` is equal to

<!-- original page 400 -->

`ₙT′ₛ`, where `T′ₛ` is the sub-torus of `G′ₛ` which is the graph of `uₛ`, and that for every point `t` of `S`, the
closed affine subscheme `F_t ×_t T_t` of `G′_t` majorizes the subgroups `M(n)_t` for every `n`. By 4.1, there therefore
exists a sub-torus `T′` of `G′` such that `ₙT′ = M(n)` for every `n` equal to a power of `q`. Let `f` be the restriction
to `T′` of the projection of `G′` to `T`, and `f(n)` the restriction of `f` to `M(n)`. One has

```text
f(n) ∘ v(n) = id_{ₙT}.
```

The fiber at `s` of `T′` is the torus already denoted `T′ₛ`, equal to the graph of `uₛ` (this follows from Exp. IX 4.8
b)), so `fₛ` is an isomorphism. But `Ker f` and `Coker f` are groups of multiplicative type (Exp. IX 2.7) of constant
type, `S` being connected, hence reduced to the unit group, and `f` is an isomorphism. Let `v` be the inverse
isomorphism of `f`. One has

```text
v|_{ₙT} = v(n).
```

Consequently, the composite of `v` and the projection of `G′` onto `G` is a morphism `u : T → G` answering the question.
The foregoing proves the existence of the morphism `u`; as for uniqueness, it follows in any case from Exp. IX 4.8 a).

### 4.2. Application

<!-- label: III.XV.4.app -->

We propose to generalize Theorem 7.1 of Exp. IX.

Let `A` be a complete noetherian local ring, `I` its maximal ideal,

<!-- original page 401 -->

`S = Spec A`, `S_m = Spec(A/I^m)`. For every prescheme `X`, set `X_m = X ×_S S_m`.

Let then `G` be an `S`-prescheme in groups of finite type, `T` an `S`-torus, `q` an integer invertible on `S`, and
`u_m : T_m → G_m` (`m ∈ ℕ`) a coherent family of group morphisms. With `n` ranging over the powers of `q`, denote by
`u_m(n)` the restriction of `u_m` to `ₙT_m`, and by `u(n)` the unique group morphism

```text
u(n) : ₙT ⟶ G
```

extending the morphisms `u_m(n)` for every `m` (1.6 a)). We shall say that the family `(u_m)`, `m ∈ ℕ`, is *admissible*
if for every point `t` of `S` there exists a closed affine subprescheme `F_t` of `G_t` majorizing `u(n)_t(ₙT_t)` for
every `n` equal to a power of `q` (this property is independent of `q`, as we shall see).

**Proposition 4.3.** *With the notation above, the canonical map*

```text
Hom_{S-gr}(T, G) ⟶ lim_{←m} Hom_{S_m-gr}(T_m, G_m)
```

*induces an isomorphism of the source onto the subset of the target consisting of "admissible" coherent families.*

<!-- label: III.XV.4.3 -->

Indeed, it suffices to apply 4.1 bis, taking for `s` the closed point of `S`.

**Corollary 4.4.** *With the notation above, suppose in addition that `G` has affine fibers; then the canonical map*

```text
Hom_{S-gr}(T, G) ⟶ lim_{←m} Hom_{S_m-gr}(T_m, G_m)
```

*is an isomorphism.* <!-- original page 402 -->

<!-- label: III.XV.4.4 -->

Indeed, if `G` has affine fibers, every coherent family is "admissible".

**Remark 4.5.** When `G` is separated, one may in 4.3 replace the ring `A` by an `I`-adic noetherian ring; one may
indeed use EGA III 5.4.1 instead of 1.6 a).

<!-- label: III.XV.4.5 -->

### 4.3. Proof of 4.1

<!-- label: III.XV.4.proof -->

**Lemma 4.6.** *Let `k` be a field, `G` a `k`-algebraic group, `q` an integer prime to the residue characteristic of
`k`, `r` an integer `> 0`, `M(n)` (`n` ranging over the powers of `q`) a coherent family of subgroups of `G`, of
multiplicative type and of type `(ℤ/nℤ)ʳ`. Then there exists a smallest closed subscheme `H` of `G` majorizing the
`M(n)` for every `n`. Moreover, `H` is a smooth, connected and commutative algebraic subgroup of `G` "whose formation is
compatible with base field extension".*

<!-- label: III.XV.4.6 -->

Let `M` be the subset of `ens(G)` which is the union of the underlying sets of the subgroups `M(n)` for every `n`, and
`H` the reduced closed subscheme of `G` having the closure of `M` as underlying space. Since `M(n)` is étale over `k`
hence reduced, `M(n)` is contained in `H`, and consequently `H` is the smallest closed subscheme of `G` majorizing
`M(n)` for every `n`. Now let `k̄` be an algebraically closed extension of `k`. By

<!-- original page 403 -->

construction the subschemes `M(n)` are schematically dense in `H` (Exp. IX 4.1); the `M(n)_{k̄}` are therefore
schematically dense in `H_{k̄}` (Exp. IX 4.5); moreover `M(n)_{k̄}` is reduced, and it follows that `H_{k̄}` is
necessarily equal to the closed reduced subscheme of `G_{k̄}` having as underlying space the closure of `M_{k̄}`. This
proves that `H` is geometrically reduced (EGA IV 4.6.1). The family `M(n)` being coherent, `M` is stable under the group
law; moreover `M ×_k M` is dense in `ens(H ×_k H)` and `H ×_k H` is reduced (EGA IV 4.6.5); one immediately deduces that
`H` is an algebraic subgroup of `G`. Moreover `H` is smooth over `S`, since it is geometrically reduced (Exp. VI_A
1.3.1), and `H` is commutative since the `M(n)` are commutative. It remains to see that `H` is connected. Let `H⁰` be
the connected component of `H`, `m` the number of geometric points of `H/H⁰`, `q^s` the exponent of `q` in the
decomposition of `m` into prime factors. For every integer `n` equal to a power of `q`, `_{q^s} M(n)` is then contained
in `H⁰`. But the family `M(n)` is coherent and `M(n)` is of type `(ℤ/nℤ)ʳ`, so `_{q^s} M(nq^s) = M(n)`. Hence `H⁰`
majorizes `M(n)` for every `n` and consequently equals `H`.

This being so, we shall make condition c) of 4.1 more precise. Indeed, by what precedes, we may consider the smallest
closed subscheme `H_t` of `G_t` majorizing `M(n)_t` for every `n`. The formation of `H_t` commuting with base field
extension (4.6), `H_t ⊗_t t̄` is contained in the affine closed subset `F_t`, hence is affine. In short, `H_t` is
affine. On the other hand, we know (4.6) that `H_t` is a smooth, connected, commutative algebraic group. It then follows
from the structure of smooth, commutative, connected affine algebraic groups over an algebraically closed field (*Bible*
4 Th. 4),

<!-- original page 404 -->

that `H_t` is a direct product of a torus `T_t` and a unipotent group `U_t`. But then `M(n)_t` is necessarily contained
in `T_t`, so `H_t = T_t`, and consequently `H_t` is a torus.

We can now begin the proof of 4.1.

a) **Uniqueness of the solution:** it suffices to apply Exp. IX 4.8 b).

b) **Case where `S` is the spectrum of a complete discrete valuation ring `A` with algebraically closed residue field
`k`.** Denote by `K` the field of fractions of `A`, `s` the closed point of `S`, `t` the generic point, `J` the maximal
ideal of `A`, `S_m = Spec(A/J^m)`, `X_m = X ×_S S_m`.

Let us distinguish two cases:

**1st case: The point `s` of 4.1 b) is the generic point `t` of `S`.** Let then `T′` be the schematic closure in `G` of
the torus `T_t`. The closed fiber `T′ₛ` is therefore an algebraic subgroup of `Gₛ`, of dimension `r`, majorizing `M(n)ₛ`
for every `n`, hence `T′ₛ` majorizes `Hₛ`. But `Hₛ` is a torus containing `M(n)ₛ`, so `Hₛ` has rank at least `r`.
Consequently `Hₛ` has the same underlying space as the connected component of `T′ₛ`. The "connected component" `(T′)⁰`
of `T′` is then a subgroup prescheme of `G`, flat, separated (VI_B 5.2), whose generic fiber `T_t` is a torus and whose
reduced closed fiber `Hₛ` is a torus. But then `(T′)⁰` is a torus (Exp. X 8.8) which we denote by `T`. The groups `ₙT`
and `M_n` are smooth over `S`, hence reduced, and since they have the same underlying space, they coincide. So the torus
`T` is the solution of the problem.

**2nd case: The point `s` of 4.1 b) is the closed point `s` of `S`.** Possibly replacing `G` by

<!-- original page 405 -->

the schematic closure in `G` of the smallest algebraic subgroup `H_t` majorizing the family `M(n)_t` (4.6), we may
assume `G_t` affine.

For every integer `m ⩾ 0`, it follows from 2.2 that there exists a unique sub-torus `T_m` of `G_m` lifting `Tₛ` and such
that for every integer `n` equal to a power of `q`, one has `ₙT_m = M(n)_m`. Moreover, let `T⁰ = G^r_{m, S}`. Since `k`
is algebraically closed, `Tₛ` is trivial, and there exists a `k`-isomorphism `uₛ : T⁰ₛ ⥲ Tₛ`. The morphism `uₛ` lifts
uniquely to an `S_m`-isomorphism `u_m : T⁰_m → T_m` (Exp. IX 3.3). The family of morphisms `u_m`, `m ∈ ℕ`, defines in
the limit a morphism `û` of formal completions `T̂⁰` and `Ĝ` of `T⁰` and `G` along their closed fibers:

```text
T̂⁰ ──û──→ Ĝ
│            │
i            j
▼            ▼
T⁰           G,
```

where `i` and `j` denote the canonical morphisms.

We shall show that the morphism `û` is algebraizable. For this we shall reduce to the case where the group `G` is
affine.

**Lemma 4.7.** *Let `S` be the spectrum of a discrete valuation ring `A`, `X` and `Y` two `S`-preschemes, quasi-compact,
quasi-separated and flat over `S`. Then the canonical map*

```text
Γ(X, 𝒪_X) ⊗_A Γ(Y, 𝒪_Y) ⟶ Γ(X ×_S Y, 𝒪_{X ×_S Y})
```

*is an isomorphism.*

<!-- label: III.XV.4.7 -->

Let `f : X → S` (resp. `g : Y → S`) be the structural morphism. Since `X` (resp. `Y`)

<!-- original page 406 -->

is quasi-compact and quasi-separated, it follows from EGA I 9.2.2 and from EGA IV 1.7.4 that `f_*(𝒪_X)` (resp.
`g_*(𝒪_Y)`) is a quasi-coherent `𝒪_S`-algebra, which therefore corresponds to an affine `S`-scheme `X̃` (resp. `Ỹ`). By
hypothesis `Y` is flat over `S`; it then follows from EGA III 1.4.15, in view of EGA IV 1.7.21, that the canonical map
(deduced from the canonical morphism `X → X̃`)

```text
Γ(X̃ ×_S Y, 𝒪_{X̃ ×_S Y}) ⟶ Γ(X ×_S Y, 𝒪_{X ×_S Y})
```

is an isomorphism. But `X` being flat over `S`, `X̃` is flat over `S` (since flat over `A` is equivalent to
torsion-free). Applying once again EGA III 1.4.15 with the roles of `X` and `Y` exchanged, one obtains an isomorphism

```text
Γ(X̃, 𝒪_{X̃}) ⊗_A Γ(Ỹ, 𝒪_{Ỹ}) ≃ Γ(X̃ ×_S Ỹ, 𝒪_{X̃ ×_S Ỹ}) ⥲ Γ(X̃ ×_S Y, 𝒪_{X̃ ×_S Y}),
```

whence the lemma.

In the present case, the `S`-group `G` is flat over `S` and of finite type, hence quasi-compact and quasi-separated. One
may therefore apply the lemma to `G ×_S G`:

```text
Γ(G, 𝒪_G) ⊗_A Γ(G, 𝒪_G) ⥲ Γ(G ×_S G, 𝒪_{G ×_S G}).
```

To the morphism `m_G : G ×_S G → G` defining the multiplication in `G` there corresponds therefore a morphism

```text
Γ(G, 𝒪_G) ⟶ Γ(G ×_S G, 𝒪_{G ×_S G}) ⥲ Γ(G, 𝒪_G) ⊗_A Γ(G, 𝒪_G),
```

hence an `S`-morphism

```text
m_{G̃} : G̃ ×_S G̃ ⟶ G̃,
```

<!-- original page 407 -->

where `G̃` denotes the affine `S`-scheme having `Γ(G, 𝒪_G)` as `A`-algebra. It is formal, from there, to verify that
`m_{G̃}` endows `G̃` with a structure of `S`-group scheme such that the canonical morphism `v : G → G̃` is an `S`-group
morphism.

**Remark 4.8.** `G̃` plays the role of a largest "affine quotient" of `G`; moreover one can show that `G̃` is indeed a
quotient of `G` for fpqc, hence is of finite type over `S` (XVII App. III, 2).

<!-- label: III.XV.4.8 -->

In the case at hand, the generic fiber `G_t` of `G` is affine; it then follows from EGA I 9.3.3 that `v_t` is an
isomorphism. Since `G̃` is affine, the coherent family of morphisms

```text
w_m = v_m u_m : T⁰_m ⟶ G̃_m    (m ∈ ℕ)
```

comes from a unique `S`-group morphism (Exp. IX 7.1)

```text
w : T⁰ ⟶ G̃.
```

Let `T_t` be the sub-torus of `G_t` equal to `v_t⁻¹ w_t(T⁰_t)`. The torus `T_t` is therefore of rank at most `r` (as the
image of a torus of rank `r`). Let us show that `T_t` majorizes `M(n)_t` for every `n`. Indeed, let `u(n)_m` be the
`S_m`-isomorphism `(ₙT⁰)_m ⥲ M(n)_m` obtained by restriction of `u_m` to `(ₙT⁰)_m`. The coherent family of morphisms
`u(n)_m` comes from a unique `S`-isomorphism `u(n) : ₙT⁰ ⥲ M(n)` (since `M(n)` is finite over `S`). For every integer
`m ⩾ 0`, one then has the equalities

```text
w_m|_{(ₙT⁰)_m} = (v_m u_m)|_{(ₙT⁰)_m} = (v ∘ u(n))_m.
```

Consequently, `w|_{ₙT⁰} = v ∘ u(n)` (1.6 a)). In particular, one has `w_t|_{(ₙT⁰)_t} = v_t ∘ u(n)_t`, so
`v_t⁻¹ w_t (ₙT⁰)_t = u(n)_t (ₙT⁰)_t = M(n)_t`.

This indeed proves that `T_t` majorizes `M(n)_t`, and entails that `T_t` is of rank `r`. One concludes

<!-- original page 408 -->

as in the first case already studied, by considering the schematic closure in `G` of `T_t`, namely `T″`. Since `T_t`
majorizes `M(n)_t`, `T″ₛ` majorizes `M(n)ₛ`, hence majorizes `Tₛ` (density theorem). On the other hand `T″` is flat over
`S` and `T_t` is of dimension `r`, so `T″ₛ` is of dimension `r` (Exp. VI_B 4). In short, `Tₛ` has the same underlying
space as the connected component of `T″ₛ`, and one concludes as in the first case that the connected component of `T″`
is a sub-torus of `G` answering the question.

c) **End of the proof of 4.1.**

To prove the existence of the sub-torus `T`, we may assume `S` reduced (2.2). In view of 3.1 (ii) ⇒ (i), it then
suffices to prove that the set `U` of points `x` of `S` such that there exists a sub-torus `T_x` of `G_x` with
`ₙT_x = M(n)_x` for every `n` equal to a power of `q`, is equal to `ens(S)`. The torus `T_x` in question is necessarily
unique, and by fpqc descent, it suffices to prove its existence after extension of the residue field of `x` (Exp. IX 4.8
b)).

This being so, since `S` is locally noetherian and connected and since `U` is non-empty (it contains the point `s` of
4.1 b)), one is reduced, by an immediate argument, to proving that if `x` and `x′` are two points of `S`, with `x` a
specialization of `x′`, and if one of the two points belongs to `U`, then both points are in `U`. By the usual technique
(EGA II 7.1.9) one reduces to the case where `S` is the spectrum of a complete discrete valuation ring with
algebraically closed residue field, a case which has been treated in b).

This completes the proof of Theorem 4.1.

## 5. Representability of the functor of smooth subgroups identical to their connected normalizer

<!-- label: III.XV.5 -->

<!-- original page 409 -->

**Proposition 5.1.** *Let `S` be a prescheme, `G` an `S`-prescheme in groups of finite presentation, `H` a subgroup
prescheme of `G`, smooth with connected fibers. Then:*

- *a) The normalizer `N` of `H` in `G` is representable by a closed subprescheme of `G` of finite presentation over
    `S`.*
- *b) The following conditions are equivalent:*
    - *i) The canonical immersion `H → N` is an open immersion.*
    - *ii) The group `N` is smooth along the unit section, and its connected component, which is then representable (Exp.
        VI_B 3.10), is equal to `H`.*
    - *iii) For every point `s` of `S`, one has `Hₛ = (Nₛ)⁰`.*

<!-- label: III.XV.5.1 -->

*Proof.* The group prescheme `H` is locally of finite presentation over `S` (`H` is smooth over `S`) and has connected
fibers, hence is of finite presentation over `S` (Exp. VI_B 5.3.3). Assertion a) is then a consequence of Exp. XI 6.11.
The equivalence of the conditions appearing in b) is included here for the record and was proved in VI_B 6.5.1.

This being so, we can state the main theorem of this section:

<!-- original page 410 -->

**Theorem 5.2.** *Let `S` be a prescheme, `G` an `S`-prescheme in groups of finite presentation over `S`, `ℒ_G` (or
simply `ℒ` if there is no ambiguity) the `S`-functor such that for every `S`-prescheme `S′` one has:*

> *`ℒ_G(S′)` = set of subgroup preschemes of `G_{S′}`, smooth over `S′`, with connected fibers, which are identical to
> their connected normalizer.*

*Then the functor `ℒ` is representable by an `S`-prescheme, a union of an increasing family `(Uᵢ)_{i ∈ ℕ}` of open
subpreschemes, quasi-projective and of finite presentation over `S`, hence a fortiori separated over `S`.*

<!-- label: III.XV.5.2 -->

**Initial reductions.**

For every integer `r ⩾ 0`, let `ℒ^r` be the subfunctor of `ℒ` such that for every `S`-prescheme `S′` one has:

> *`ℒ^r(S′)` = set of subgroup preschemes of `G_{S′}`, smooth, with connected fibers, identical to their connected
> normalizer and of relative dimension `r`.*

Since the dimension of the fibers of a smooth group is a locally constant function, the canonical monomorphism `ℒ^r → ℒ`
is representable by an immersion both open and closed. It therefore suffices to show that for every `r`, `ℒ^r` is
representable by an `S`-prescheme having the properties stated above, since `ℒ` will then be representable by the
`S`-prescheme sum `∐_{r ∈ ℕ} ℒ^r`.

<!-- original page 411 -->

For every integer `n ⩾ 0`, every `S`-prescheme `S′` and every subgroup prescheme `H` of `G_{S′}`, we denote by `H^{(n)}`
the `n`-th normal invariant of the unit section `S′ → H` of `H` (EGA IV 16.1.2), so that `H^{(n)}` is a sheaf of
`𝒪_{S′}`-modules of finite type corresponding to the `n`-th infinitesimal neighborhood of the unit section of `H`. If
`H` is smooth over `S′` of relative dimension `r`, `H^{(n)}` is a locally free `𝒪_S`-module whose rank `φ(n, r)` depends
only on `n` and `r`. Moreover, since `H` is a subprescheme of `G_{S′}`, one has a canonical epimorphism, compatible with
base extension:

```text
G^{(n)} ⊗_{𝒪_S} 𝒪_{S′} ≃ G_{S′}^{(n)} → H^{(n)}.
```

Introduce then the projective `S`-scheme

```text
P_{φ(n, r)} = Grass_{φ(n, r)}(G^{(n)})
```

(EGA I 2nd ed. 9.7; cf. also Séminaire Cartan 1960/61, Exp. N° 14 by A. Grothendieck). It then follows from the
preceding remarks that the map

```text
H ↦ H^{(n)}
```

defines a canonical morphism

```text
u_{n, r} : ℒ^r ⟶ P_{φ(n, r)}.
```

The group `G` acts in a natural way on `G^{(n)}`, hence on `P_{φ(n, r)}`, by means of the representation

```text
int : G ⟶ Aut_{S-gr}(G),    g ↦ int(g).
```

Moreover, if `S′` is a quasi-compact `S`-prescheme and `H` an element of `ℒ^r(S′)`, one knows

<!-- original page 412 -->

(Exp. XI 6.11) that for `n` large enough,

```text
N = Norm_{G_{S′}}(H) = Norm_{G_{S′}}(H^{(n)}).
```

For each integer `n ⩾ 0`, introduce the subfunctor `ℒ^r_n` of `ℒ^r` such that for every `S`-prescheme `S′` one has:

> *`ℒ^r_n(S′)` = set of subgroups `H` of `G_{S′}` belonging to `ℒ^r(S′)` such that
> `Norm_{G_{S′}}(H) = Norm_{G_{S′}}(H^{(n)})`.*

**Representability of `ℒ^r_n`.**

Since the integer `r` is fixed until the end of the proof of 5.2, we shall not repeat it in the notation. Thus we shall
write `ℒ`, `ℒ_n`, `P_n`, `u_n` instead of `ℒ^r`, `ℒ^r_n`, `P_{φ(n, r)}`, `u_{n, r}`.

Let `v_n` be the restriction of `u_n` to the subfunctor `ℒ_n` of `ℒ`. It follows from the definition of `ℒ_n` and from
5.1 b) ii) that `v_n` is a monomorphism. In fact one has the following lemma:

**Lemma 5.3.** *The morphism `v_n` is an immersion of finite presentation. A fortiori, `ℒ_n` is representable by an
`S`-prescheme, quasi-projective and of finite presentation over `S`.*

<!-- label: III.XV.5.3 -->

Possibly replacing `S` by `P_n`, we are reduced by the usual technique to proving the following assertion: Let
`Q ∈ P_n(S)` and consider the subfunctor `F` of the functor `h_S` represented by the final object `S` of `Sch/S`, such
that for every `S`-prescheme `S′` one has:

<!-- original page 413 -->

- *`F(S′) = h_S(S′)` (set with one element) if there exists `H ∈ ℒ_n(S′)` such that `H^{(n)} = Q_{S′}`,*
- *`F(S′) = ∅` otherwise.*

Then the canonical monomorphism `F → S` is an immersion of finite presentation.

Let us first transform the definition of the functor `F`. For this, note that the normalizer of `Q` in `G` is
representable by a subgroup prescheme `N` of finite presentation over `S` (namely the inverse image of the point `Q` of
`P_n(S)` under the morphism `G → P_n`, `g ↦ g · Q`). I claim that the functor `F` coincides with the following
subfunctor of `h_S`:

> *`F(S′) = h_S(S′)` if:*
>
> - *(a) `N_{S′}` is smooth along the unit section and of relative dimension `r`,*
> - *(b) `(N_{S′})^{(n)}` (which is then canonically an element of `P_n(S′)`) is equal to `Q_{S′}`.*
>
> *`F(S′) = ∅` otherwise.*

Indeed, denote temporarily by `F_1` the functor `F` in the first formulation, and `F_2` the functor `F` in the second
formulation. Then:

i) `F_1(S′) = h_S(S′) ⇒ F_2(S′) = h_S(S′)`.

<!-- original page 414 -->

Indeed, let `H ∈ ℒ_n(S′)` be the subgroup of `G_{S′}` such that `H^{(n)} = Q_{S′}`. Then

```text
Norm_{G_{S′}}(H) = Norm_{G_{S′}}(H^{(n)}) = Norm_{G_{S′}}(Q_{S′}) = N_{S′}.
```

So by 5.1 b) ii), `N_{S′}` is smooth along the unit section and its connected component is `H`. Consequently `N_{S′}` is
of relative dimension `r`; and since `H` is open in `N_{S′}` (by 5.1 b) i)), one has
`(N_{S′})^{(n)} = H^{(n)} = Q_{S′}`. In short, `F_2(S′) = h_S(S′)`.

ii) `F_2(S′) = h_S(S′) ⇒ F_1(S′) = h_S(S′)`.

By hypothesis, `N_{S′}` is smooth along the unit section, of relative dimension `r`; its connected component is then
representable (Exp. VI_B 3.10) by a subgroup prescheme `H`, smooth over `S′`, with connected fibers of dimension `r`.
Since `H` is invariant in `N_{S′}` and open in `N_{S′}`, one has the following inclusions:

```text
N_{S′} ⊂ Norm_{G_{S′}}(H) ⊂ Norm_{G_{S′}}(H^{(n)}) = Norm_{G_{S′}}((N_{S′})^{(n)}) = Norm_{G_{S′}}(Q_{S′}) = N_{S′}.
```

These inclusions are therefore equalities. The first inclusion then shows that `H` is equal to its connected normalizer,
and the second shows that `H` is an element of `ℒ_n(S′)`. This says that `F_1(S′) = h_S(S′)`.

Implications i) and ii) entail `F_1 = F_2`. We keep the second definition of the functor `F`, and we shall first
"represent condition a)" by an immersion of finite presentation. For this it suffices to apply the:

**Lemma 5.4.** *Let `S` be a prescheme, `X` an `S`-prescheme locally of finite presentation over `S`, `σ : S → X` a
section of `X`, `r` an integer `⩾ 0`, and `L : (Sch/S)° → (Ens)` the subfunctor of `S` defined as follows:*

<!-- original page 415 -->

- *`L(S′) = h_S(S′)` if `X_{S′}` is smooth along the section `σ_{S′}` and of relative dimension `r` at the points of
    `σ_{S′}(S′)`.*
- *`L(S′) = ∅` otherwise.*

*Then:*

- *a) The monomorphism `L → S` is an immersion of finite presentation.*
- *b) Let `𝒥` be the conormal sheaf relative to the immersion `S → X` (EGA IV 16.1.2); assume that for every point `s`
    of `S`, `𝒥 ⊗_{𝒪_{S, s}} κ(s)` is of rank at most `r`. Then the immersion `L → S` is a closed immersion.*

<!-- label: III.XV.5.4 -->

*Proof.* The functor `L` is of local nature on `S`, which reduces us to the case where `S` is affine. Possibly replacing
`X` by a neighborhood of `σ(S)`, we may assume `X` of finite presentation over `S`, then (EGA IV 8.9) `S` noetherian
(noting, in case b), that the formation of the conormal sheaf commutes with base extension (EGA IV 16.6.4) and that the
rank of the fibers of `𝒥` is a constructible function on `S`). This being so, for every `S`-prescheme `S′`, denote
`𝒥_0 = 𝒥_{S′}` the conormal sheaf relative to the section `σ_{S′}`, `S_•(𝒥_0)` (canonically isomorphic to `S_•(𝒥)_{S′}`)
the symmetric algebra of `𝒥_0` over `𝒪_{S′}`, `Gr_•(σ_{S′})` the sheaf of graded `𝒪_{S′}`-algebras associated to
`σ_{S′}` (EGA IV 16), and for every integer `n ⩾ 0` let `σ_{n, S′} : S_n(𝒥_0) → Gr_n(σ_{S′})` be the canonical
epimorphism.

It follows from EGA IV 17.12.3 and from EGA 0_IV 19.5.4 that, for `X_{S′}` to be smooth along the section `σ_{S′}` and
of relative dimension `r` at the points of `σ_{S′}(S′)`,

<!-- original page 416 -->

it is necessary and sufficient that:

- i) `𝒥_0` be a locally free `𝒪_{S′}`-sheaf of rank `r`.
- ii) For every integer `n ⩾ 1`, `σ_{n, S′}` be an isomorphism.

Now it follows from TDTE IV, Lemma 3.6, that "the functor that makes `𝒥` locally free of rank `r`" is representable by a
subprescheme `S_1`, closed in `S` in case b). Replacing `S` by `S_1`, we are reduced to the case where `𝒥` is locally
free of rank `r`. Let us then proceed by induction on the integer `n`. Suppose that we have represented by a closed
subprescheme `S_{n-1}` of `S` the "functor that makes the morphisms `σ_{q, S′}` injective for every integer
`q ⩽ n − 1`", and let us show that the "subfunctor[^N.D.E-XV-5] that makes `σ_{n, S′}` injective" is representable by a
closed subprescheme `S_n` of `S_{n-1}`. Replacing `S` by `S_{n-1}`, we may assume that `σ_{q, S}` is bijective for
`q ⩽ n − 1`. But then the `(n − 1)`-st normal invariant `X^{(n-1)}` relative to the section `σ_s` admits a composition
series `X^{(0)}, …, X^{(n-1)}` whose successive quotients `Gr_0(σ_s), …, Gr_{n-1}(σ_s)` are locally free over `𝒪_{S′}`,
hence flat; so `X^{(n-1)}` is flat over `𝒪_S`. Since the formation of `X^{(i)}` commutes with base extension (EGA IV
16), one has, for every `S`-prescheme `S′`:

```text
Gr_n(σ_{S′}) = Ker(X_{S′}^{(n)} → X_{S′}^{(n-1)}) = (Gr_n(σ))_{S′}    and    σ_{n, S′} = (σ_{n, S})_{S′}.
```

So the functor that interests us is "the one that makes the morphism `σ_{n, S}` injective".

<!-- original page 417 -->

This functor is of local nature on `S`, which allows us to assume `S` affine and `S_n(𝒥)` free over `𝒪_S`. But then it
is clear that the functor in question is representable by the closed subscheme of `S` defined by the ideal generated by
the coordinates of `Ker σ_{n, S}` with respect to a basis of `S_n(𝒥)`.

Since `S` is noetherian, the decreasing sequence `{S_n}` of closed subpreschemes of `S_1` is stationary, and the
stationary value represents the functor `L`, which completes the proof of 5.4.

Let us return to the question of representability of `ℒ_n`. Replacing `S` by a suitable subprescheme `S_1`, we may
therefore assume `N` smooth along the unit section and of relative dimension `r`. The functor `ℒ_n` is then the "functor
of coincidences" of two sections of `P_n` above `S`, `h` and `g`, corresponding to the sheaves `Q` and `N^{(n)}`
(condition b) appearing in the definition of the functor `F_2` above). It is therefore representable by the closed
subprescheme of `S`, inverse image of the diagonal of `P_n ×_S P_n` by the morphism of finite presentation `h ×_S g`.
This completes the proof of 5.3.

**Study of the transition morphisms `ℒ_n → ℒ_m`.**

If a subgroup `H` of `G_{S′}` belongs to `ℒ_n(S′)`, it belongs *a fortiori* to `ℒ_m(S′)` for every `m ⩾ n`, whence
natural monomorphisms

```text
u^m_n : ℒ_n ⟶ ℒ_m    for m ⩾ n.
```

**Lemma 5.5.** *The morphism `u^m_n` is an open immersion.*

<!-- label: III.XV.5.5 -->

Possibly changing `S`, we are reduced to the following problem: Let `H ∈ ℒ_m(S)`,

```text
N = Norm_G(H) = Norm_G(H^{(m)}),    N′ = Norm_G(H^{(n)}),
```

and let `D : (Sch/S)° → (Ens)` be the functor of coincidences of `N` and `N′`, defined by `D(S′) = h_S(S′)` if
`N_{S′} = N′_{S′}`, and `D(S′) = ∅` otherwise. We must show that `D → S`

<!-- original page 418 -->

is an open immersion. Now I claim that `D` is also the subfunctor of `S` which "makes the immersion `H → N′` open".
Indeed, if `N_{S′} = N′_{S′}`, then `H_{S′} → N′_{S′}` is indeed an open immersion since this is so for
`H_{S′} → N_{S′}` (Prop. 5.1). Conversely, if `H_{S′} → N′_{S′}` is an open immersion, `H` having connected fibers,
`H_{S′}` is the connected component of `N′_{S′}` (Exp. VI_B 3.10) and consequently is invariant in `N′_{S′}`, so
`N′_{S′} ⊂ N_{S′}`. Since in any case `N′` majorizes `N`, one has `N_{S′} = N′_{S′}`. The group preschemes `H` and `N′`
are of finite presentation over `S` and `H` is flat over `S`; the fact that `D → S` is an open immersion then follows
from Exp. VI_B 2.6.

**End of the proof of 5.2.**

The functors `ℒ_n` being representable and the transition morphisms `u^m_n` being compatible with one another and
representable by open immersions, there exists an `S`-prescheme `X`, union of an increasing sequence of open subsets
`(Xᵢ)_{i ∈ ℕ}`, such that `Xᵢ` represents the functor `ℒ_i`, and such that if one identifies `ℒ_i` with `Xᵢ`, the
inclusion `Xᵢ → X_j` (`j ⩾ i`) is identified with `u^j_i`. To conclude that `X` represents the functor `ℒ`, it then
suffices to remark that in the category of sheaves on `Sch/S` equipped with the Zariski topology (Exp. IV 6.1) one has

<!-- original page 419 -->

```text
X = lim_{→} Xᵢ    and    ℒ = lim_{→} ℒ_i.
```

**Remark 5.6.** With the preceding notation, suppose in addition that `S` has all residue characteristics zero. Then,
for every integer `r ⩾ 0`, the functor `ℒ^r` is equal to `ℒ^r_1`, hence is representable by an `S`-prescheme of finite
presentation and quasi-projective over `S`. Indeed, it suffices to show that if `H ∈ ℒ^r(S′)`, the canonical immersion

```text
H ⟶ N = Norm_{G_{S′}}(H^{(1)})
```

is an open immersion (since this entails `N = Norm_{G_{S′}}(H)`, hence `H ∈ ℒ^r_1(S′)`). Since `H` is flat over `S`, and
`H` and `N` are of finite presentation over `S`, it suffices (Exp. VI_B 2.6) to show that for every point `s` of `S`,
`Hₛ → Nₛ` is an open immersion. Now it follows easily[^N.D.E-XV-6] from Cartier's theorem (Exp. VI_B 1.6) that if `G` is
an algebraic group over a field of characteristic 0 and `H` is a connected algebraic subgroup, one has

```text
Norm_G(H) = Norm_G(Lie H) = Norm_G(H^{(1)}).
```

On the other hand, if `S` has non-zero residue characteristics, the subfunctors `ℒ^r_n` of `ℒ^r` may form a strictly
increasing sequence (even when `S` is quasi-compact) and in this case `ℒ^r` is not representable by an `S`-prescheme
quasi-compact over `S`. Take for example the algebraic group `G`, defined over a field `k` of characteristic `p > 0`,
equal to the semidirect product of the torus `T = G_m × G_m` by the unipotent group `U = G_a × G_a`, the action of `T`
on `U` being defined by `(t, t′, u, u′) → (tu, t′u′)`. For every integer `n > 0`, consider the smooth connected subgroup
`U_n` of `U` of equation `u′ = u^{pⁿ}`, and the sub-torus `T_n` of `T` of equation `t′ = t^{pⁿ}`. It is immediate to
verify that `T_n` acts on `U_n` and that the subgroup `G_n` of `G`, equal to `T_n · U_n`, is smooth, connected and equal
to its normalizer in `G`. Now all the groups `G_n`, for `n ⩾ m`, are distinct but have the same infinitesimal
neighborhood of order `pᵐ`.

<!-- label: III.XV.5.6 -->

**Remark 5.7.** There exists on `ℒ` a canonical invertible sheaf `L`,

<!-- original page 420 -->

whose restriction to every open subset `U` of `ℒ` quasi-compact over `S` is `S`-ample. Indeed, consider the subgroup
prescheme `H` of `G_ℒ` smooth over `ℒ`, with connected fibers, equal to its connected normalizer and universal for these
properties. I claim that one may take for `L` the sheaf `(det(Lie H))⁻¹` (recall that if `ℱ` is a sheaf of `𝒪_S`-modules
on a prescheme `S` that is locally free of finite rank, `det(ℱ)` denotes the invertible `𝒪_S`-module whose restriction
to the open-closed subprescheme `S_r` of `S` (`r ⩾ 0`) where `ℱ` is of rank `r` is equal to `⋀^r(ℱ)`). We keep the
notation from the proof of 5.2. To prove the assertion made on `L`, we may restrict to the functor `ℒ^r_n` and prove
that `L|_{ℒ^r_n}` is `S`-ample. Consider the canonical immersion `v_n : ℒ^r_n → P_n`, and let `Q` be the locally free
sheaf on `P_n` universal for the Grassmannian `P_n`. By construction, one has `v_n^*(Q) = H^{(n)}` (where now `H`
denotes the subgroup prescheme of `G_{ℒ^r_n}` universal for the functor `ℒ^r_n`). Now `det(Q)` is the canonical ample
sheaf on `P_n` (EGA I 2nd ed. 9.7), so `det H^{(n)}` is ample relative to `ℒ^r_n` (EGA II 4.6.13 i) bis). Let `𝒥` still
denote the conormal sheaf, equal to `H^{(1)}`, and `S^q(𝒥)` the homogeneous part of degree `q` of the symmetric algebra
of `𝒥` over `𝒪_{ℒ^r_n}`. Since `H` is smooth over `ℒ^r_n`, it is immediate that one has a canonical isomorphism:

```text
det H^{(n)} ≃ ∏_{1 ⩽ q ⩽ n} det S^q(𝒥).
```

On the other hand, one proves that for every locally free sheaf `𝒥` of rank `r` and for every integer `q > 0`, there
exists a canonical isomorphism:

<!-- original page 421 -->

```text
det S^q(𝒥) ≃ (det 𝒥)^{⊗ s},
```

where `s > 0` is an integer depending only on `r` and `q`. Finally, one obtains `det H^{(n)} ≃ (det 𝒥)^{⊗ s}` for a
suitable integer `s > 0`, hence (EGA II 4.5.6), `det 𝒥 = (det Lie H)⁻¹` is indeed `S`-ample.

<!-- label: III.XV.5.7 -->

**Remark 5.8.** Let `S` be a prescheme, `G` and `H` two `S`-preschemes in groups of finite presentation over `S`,
`i : H → G` an `S`-homomorphism of groups which is a monomorphism. If `H` is smooth over `S` with connected fibers, one
knows (Exp. XI 6.11) that `N = Norm_G(H)` is representable by a closed subgroup prescheme of `G`, of finite presentation
over `S`. Suppose in addition that `N` is smooth along the unit section and has the same relative dimension over `S` as
`H`. The connected component `N⁰` of `N` is then representable by an open subgroup prescheme of `N`, smooth over `S`
(Exp. VI_B 3.10). The monomorphism `i` evidently factors through `N⁰`. In fact one has `H = N⁰`. Indeed, for every point
`s` of `S`, one has `Hₛ = (N⁰)ₛ`, these two algebraic groups being connected, smooth, of the same dimension. Since `H`
is flat over `S`, one deduces that `H → N⁰` is an isomorphism (EGA IV 17.9.5). Finally `H` is a subgroup prescheme of
`G`. We have therefore shown that the functor `ℒ` introduced in this section is identical to the functor of subgroups
`H` of `G`, smooth over `S`, with connected fibers and equal to their connected normalizer.

<!-- label: III.XV.5.8 -->

## 6. Functor of Cartan subgroups and functor of parabolic subgroups

<!-- label: III.XV.6 -->

<!-- original page 422 -->

When `G` is a smooth, connected algebraic group defined over an algebraically closed field `k`, one has defined the
sub-tori of `G`, the maximal sub-tori, the Cartan subgroups (Exp. XII 1), the Borel subgroups (Exp. XIV 4.1), the
parabolic subgroups (Exp. XIV 4.8 bis). We extend these notions to the case of a group prescheme over an arbitrary base,
as follows:

**Definition 6.1.** *Let `S` be a prescheme, `G` an `S`-prescheme in groups of finite presentation over `S`, `H` an
`S`-prescheme in groups, `i : H → G` an `S`-monomorphism making `H` a subgroup of `G`. We say that `H` is a sub-torus of
`G` (resp. a maximal sub-torus of `G`, a Cartan subgroup, a Borel subgroup, a parabolic subgroup) if:*

- *i) `H` is smooth over `S`.*
- *ii) For every geometric point `s` above `S`, `Hₛ` is a sub-torus of `(Gₛ)⁰_{red}` (resp. a maximal sub-torus, a
    Cartan subgroup, a Borel subgroup, a parabolic subgroup).*

<!-- label: III.XV.6.1 -->

**Remarks 6.1 bis.**

a) If the `S`-group `H` is a sub-torus of `G` (resp. ...), its fibers are connected, and consequently `H` is of finite
presentation over `S` (Exp. VI_B 5.3.3).

<!-- original page 423 -->

b) If `H` is a sub-torus of `G`, then `H` is a torus in the sense of Exp. IX, as follows immediately from Exp. X 8.1.
Moreover the monomorphism `i : H → G` is an immersion (cf. 8.3 below).

c) If `G` is smooth over `S` with connected fibers and if `H` is a Cartan subgroup of `G` (resp. a Borel subgroup, a
parabolic subgroup), the monomorphism `i : H → G` is an immersion, so that our definitions coincide with those
introduced in Exp. XII and Exp. XIV. Indeed, `H` is then identical to its connected normalizer (by XII 6.6 c), XIV 4.8
and 4.8 bis), and it suffices to apply 5.8.

<!-- label: III.XV.6.1bis -->

**Definition 6.1 ter.** *Let `S` be a prescheme, `G` an `S`-prescheme in groups locally of finite type, `s` a point of
`S`. The **nilpotent rank** of `G` at the point `s`, denoted `ρ_n(s)`, is the dimension of the Cartan subgroups of
`(Gₛ)⁰_{red}`. One similarly defines the reductive rank `ρ_r(s)`, the unipotent rank `ρ_u(s)`, the abelian rank
`ρ_{ab}(s)` (cf. Exp. X 8.7).*

<!-- label: III.XV.6.1ter -->

If now `G` is a smooth connected algebraic group defined over an algebraically closed field `k`, recall that the
**radical** of `G`, denoted `rad(G)`, is the largest invariant, smooth, connected, solvable algebraic subgroup of `G`;
`G/rad(G)` is then semisimple (use Exp. XII 6.1 to reduce to the affine case). If `G` is moreover affine, one defines
the **unipotent radical** `rad_u(G)` of `G` as the largest invariant, smooth, connected, unipotent algebraic subgroup of
`G`; `G/rad_u(G)` is then reductive.

<!-- original page 424 -->

**Proposition 6.2.** *Let `S` be a prescheme, `G` and `H` two `S`-preschemes in groups of finite presentation over `S`,
`i : H → G` an `S`-monomorphism making `H` a subgroup of `G`, and let `P(s)` be one of the following properties
concerning the point `s` of `S`:*

- *i) `(Gₛ)⁰_{red}` is an abelian variety (resp. is affine, is a torus, is unipotent).*
- *ii) `(Hₛ)⁰_{red}` is a maximal torus of `Gₛ`.*
- *iii) `(Hₛ)⁰_{red}` is the centralizer in `(Gₛ)⁰_{red}` of a torus of `Gₛ` (resp. is a Cartan subgroup of `Gₛ`).*
- *iv) `(Hₛ)⁰_{red}` is a Borel subgroup (resp. a parabolic subgroup) of `Gₛ`.*
- *v) `(Hₛ)⁰_{red}` is the radical of `Gₛ` (resp. `(Gₛ)⁰_{red}` is semisimple).*
- *vi) `Gₛ` is affine and `(Hₛ)⁰_{red}` is the unipotent radical of `Gₛ` (resp. `(Gₛ)⁰_{red}` is reductive).*

*Then the set `E` of points `s` of `S` for which `P(s)` is true is locally constructible (EGA 0_III 9.1.11).*

<!-- label: III.XV.6.2 -->

**Remark 6.2.1.** This proposition complements Exp. VI_B § 10. Moreover, one can further specify the structure of `E` by
using semi-continuity theorems (cf. Exp. X 8.7); we shall see an example a little later.

<!-- label: III.XV.6.2.1 -->

*Proof of 6.2.* <!-- original page 425 --> Note that if `S` is the spectrum of a field, `E` is invariant under extension
of that field. A standard reduction (EGA IV 9) then allows us to reduce to the case where `S` is noetherian, integral,
with generic point `η`. One must show that `E` or `ens(S) \ E` contains a neighborhood of `η` (EGA IV 9.2.1). One may
assume `S` affine of ring `A` and field of fractions `K`. If `L` is a finite extension of `K`, it is immediate that
there exists an `A`-subalgebra `B` of `L`, finite over `A`, having `L` as field of fractions. The canonical morphism
`S′ → S`, where `S′ = Spec B`, is dominant, of finite presentation, so the image of a non-empty open subset of `S′`
contains a non-empty open subset of `S` (EGA IV 1.8.4). From the viewpoint that interests us, we may therefore replace
`S` by `S′`, hence replace `K` by a finite extension `L`. Thus we may choose `L` so that `(G_L)_{red}` and `(H_L)_{red}`
are smooth over `L` (EGA IV 4.6.6). Possibly restricting `S′`, we may assume that `G_{red}` and `H_{red}` are group
preschemes smooth over `S` (Exp. VI_B § 10 and EGA IV 17). In view of the properties to be proved, we may replace `G`
and `H` by their reduced connected components (Exp. VI_B 10.9), hence assume `G` and `H` smooth over `S` with connected
fibers. Finally we may assume `H` is a closed subgroup prescheme of `G` (Exp. VI_B 10.4).

*Proof of i).* Possibly after a finite extension of `K`, we may assume that `G_η` admits a "Chevalley decomposition",
i.e. is an extension of an abelian variety `D_η` by a smooth connected linear algebraic group `F_η` (Séminaire Bourbaki
1956/57 N° 145). By Exp. VI_B 10.16, there exists an open neighborhood `U` of `η`

<!-- original page 426 -->

such that this generic extension comes from an extension `1 → F → G|_U → D → 1`. One may further assume `F` and `D`
smooth over `U` with connected fibers, `F` affine over `U` and `D` proper over `U` (EGA IV 8, 9 and 17). For every point
`s` of `U`, `(Dₛ, Fₛ)` is then the "Chevalley decomposition" of `Gₛ`. Consequently, `Gₛ` is an abelian variety (resp. is
affine) if and only if `Fₛ` (resp. `Dₛ`) is the unit group, which is a constructible property (EGA IV 9.2.6.1).

To establish the last two assertions of i), we may, by the preceding, assume `G` affine over `S`. Let `q` be a prime
number invertible on `S` and `_qG` the "kernel" of the `q`-th power morphism in `G`. It follows easily from the
structure of affine algebraic groups that `Gₛ` is a torus (resp. is unipotent) if and only if a) `_qGₛ` is quasi-finite,
which is a constructible property (EGA IV 9.3.2), and b) `_qGₛ` has `r^q` geometric points, where `r` denotes the
relative dimension of `G` over `S` (resp. `_qGₛ` has a single point). Now the function
`s ↦ (number of geometric points of _qGₛ)` is constructible (EGA IV 9.7.9). This completes the proof of (i).

*Proof of iii).* a) **Case of a centralizer of a torus.** Suppose `H_η = Centr_{G_η}(T_η)`, where `T_η` is a torus of
`G_η`, and let us show that `Hₛ` is the centralizer of a sub-torus of `Gₛ` for `s` in a neighborhood of `η`. By i),
possibly restricting `S`,

<!-- original page 427 -->

we may assume that `T_η` comes from a sub-torus `T` of `G`. But then `Z = Centr_G(T)` is representable (Exp. XI 6.11) by
a subgroup prescheme of `G`. Since `H` and `Z` coincide generically, they coincide over a neighborhood of `η`. This
proves to us that the set `E` of points `s` of `S` such that `Hₛ` is the centralizer in `Gₛ` of a sub-torus of `Gₛ` is
ind-constructible (EGA IV 1), and this result will suffice for us to establish, in Lemma 6.6 below, that `E` is an open
part of `S`; *a fortiori*, `E` will indeed be a locally constructible part of `S`.

iii) b) **Case of a Cartan subgroup.** Suppose `H_η` is a Cartan subgroup of `G_η`, and let us show that `Hₛ` is a
Cartan subgroup of `Gₛ` for every point `s` of a neighborhood of `η`. The group `H_η` is the centralizer in `G_η` of a
torus of `G_η` and is nilpotent (Exp. XII 6.6). By a) and Exp. VI_B 8.4, `Hₛ` has the same properties for every point
`s` of a neighborhood `U` of `η`. For every point `s` of `U`, the group `Hₛ` thus has the same reductive rank as `Gₛ`,
and its unique maximal torus is central (Exp. XII 6.7); it is therefore the centralizer of a maximal torus of `Gₛ`, i.e.
a Cartan group of `Gₛ`.

Suppose now that `H` is not a Cartan subgroup of `G`, and let us show that `Hₛ` is not a Cartan subgroup of `Gₛ` for `s`
in a neighborhood `U` of `η`. In view of the assertion provisionally admitted in (a) above, we may restrict to the case
where `H` is the centralizer in `G` of a sub-torus `T`. But then `H_η` contains a Cartan subgroup `C_η` of `H_η`. We
have just seen that, possibly restricting `S`, `C_η` extends to a Cartan subgroup `C` of `G`, which one may assume
contained in `H`. By hypothesis `H_η` strictly majorizes `C_η`, so `Hₛ` strictly majorizes `Cₛ` for `s` in a
neighborhood `U` of `η` (EGA IV 9.5.2); *a fortiori*, `Hₛ` is not

<!-- original page 428 -->

a Cartan subgroup of `Gₛ` for `s` in `U`.

*Proof of ii).* Suppose `H_η` is a maximal torus of `G_η` and let `C_η` be its centralizer in `G_η`. By i) and iii), `H`
is a torus over a neighborhood `U` of `η` and `C = Centr_{G|U}(H|U)` is a Cartan subgroup of `G|U`. To prove that `H` is
a maximal torus of `G` over a neighborhood of `η`, we may then replace `G` by `C`, then by the linear component `F` of a
Chevalley decomposition of `C` (cf. i)). Let `q` be an integer invertible on `S`, `_qF` the kernel of the `q`-th power
morphism in `F`. Since `Fₛ` is affine, nilpotent, smooth and connected, `Fₛ` is the direct product of its maximal torus
`Tₛ` by a unipotent group (*Bible* 6-04), so `_qFₛ = _qTₛ`. Since `H_η` is a maximal torus, `_qH_η = _qF_η`, and
consequently `_qH = _qF` over a neighborhood `V` of `η`. For every point `s` of `V`, `_qHₛ = _qTₛ`, so `Hₛ = Tₛ` is a
maximal torus.

Suppose now that `H_η` is not a maximal torus of `G_η`. By i), we may restrict to the case where `H_η` is a torus, then
assume that it is contained in a strictly larger torus `T_η`. The latter extends to a torus `T` strictly majorizing `H`
over a neighborhood `U` of `η`. *A fortiori*, `Hₛ` is not a maximal torus for `s ∈ U`.

*Proof of iv).* Possibly restricting `S`, we may assume that the center `Z` of `G` is representable (Exp. VI_B 10.11)
and flat over `S`, as well as the quotient `G/Z` (*loc. cit.*). The property "`Hₛ` majorizes `Zₛ`" is constructible (EGA
IV 9.5.2) and every parabolic subgroup of `Gₛ` contains `Zₛ` (Exp. XIV 4.9 a)); this allows us to replace `G` by `G/Z`,
hence assume `G` affine over `S` (Exp. XII 6.1 and i)). We may further

<!-- original page 429 -->

assume that `G/H` is representable, but then `Hₛ` is a parabolic subgroup of `Gₛ` if and only if `(G/H)ₛ` is proper
(*Bible* 6 Th. 4 b)), which is an ind-constructible property (EGA IV 9.3.5). So `E` is ind-constructible, and this will
suffice for us to prove that `E` is open (Lemma 6.6), hence locally constructible.

Let us now examine the case of Borel subgroups. If `H_η` is a Borel subgroup of `G_η`, i.e. a solvable parabolic
subgroup of `G_η`, what precedes and Exp. VI_B 8.4 entail that these properties remain true at every point `s` of a
neighborhood of `η`. If now `H_η` is not a Borel subgroup of `G_η`, to prove that the same holds at points `s` of a
neighborhood of `η`, we may restrict (in view of what precedes) to the case where `H_η` is a parabolic subgroup, then
assume that `H_η` contains a Borel subgroup `B_η`. We have just shown that the latter extends to a Borel subgroup `B` of
`G` over a neighborhood `U` of `η`. Since `H_η` strictly majorizes `B_η`, `Hₛ` strictly majorizes `Bₛ` at every point of
an open subset `V`, and `Hₛ` is not a Borel subgroup of `Gₛ` for `s ∈ V`.

*Proof of v).* Suppose `H_η` is the radical of `G_η`. The group `H_η` is then invariant in `G_η`, solvable (smooth and
connected); the same is therefore true for `Hₛ` for `s` belonging to a neighborhood `U` of `η` (Exp. VI_B 8 and 10), so
for `s ∈ U`, `Hₛ` is contained in the radical of `Gₛ`. Replacing `G` by `G/H` (Exp. VI_B 10), we must

<!-- original page 430 -->

prove that if `G_η` is semisimple, then `Gₛ` is semisimple at every point of a neighborhood `V` of `η`. Using i) and
ii), one may assume that `G` is affine over `S` and possesses a maximal torus `T`. Let `W` be the Weyl group of `T`
(Exp. XII 2), which is quasi-finite and étale over `S`, hence finite and étale over an open subset `V`. It then follows
from the elementary properties of roots (Exp. XIX 1.12) that `G` is semisimple over `V`.

Suppose now that `H_η` is not the radical of `G_η`. Possibly replacing `K` by a finite extension `L`, we may assume that
`G_η` admits a radical `R_η`. By what precedes, `R_η` extends to a subgroup prescheme `R` of `G|_U` such that for every
`s ∈ U`, `Rₛ` is the radical of `Gₛ`. By hypothesis, `R_η ≠ H_η`. So `Rₛ ≠ Hₛ` for `s ∈ V`. It remains to prove that if
`G_η` is not semisimple, neither is `Gₛ` at neighboring points, but this is a particular case of what precedes (take `H`
= unit group).

*Proof of vi).* The proof is entirely analogous to that of v), in view of i), and is left to the care of the reader.

**Corollary 6.3.** *Let `S₀` be a quasi-compact prescheme, `(Sᵢ)_{i ∈ L}` a projective system of `S₀`-preschemes, affine
over `S₀`, `S = lim Sᵢ` (EGA IV 8.2), `G₀` a group prescheme of finite presentation over `S₀`, `Gᵢ = G₀ ×_{S₀} Sᵢ`,
`G = G₀ ×_{S₀} S`, `H` a subgroup of `G`. Then, if `H` is a sub-torus of `G` (resp. a maximal sub-torus, a Cartan
subgroup, a Borel subgroup, a parabolic subgroup), there exists an index `i ∈ L` and a subgroup `Hᵢ` of `Gᵢ` such that
`H = Hᵢ ×_{Sᵢ} S` and `Hᵢ` is a sub-torus of `Gᵢ` (resp. ...).*

<!-- label: III.XV.6.3 -->

<!-- original page 431 -->

Indeed, `H` is smooth with connected fibers, hence of finite presentation over `S` (Exp. VI_B 5.3.3). By Exp. VI_B § 10,
there exist `i ∈ L` and a subgroup `Hᵢ` of `Gᵢ`, smooth over `S`, such that `H = Hᵢ ×_{Sᵢ} S`. Corollary 6.3 then
follows from Definition 6.1, from 6.2, and from EGA IV 9.3.3.

**Corollary 6.3 bis.** *Let `S` be a prescheme, `G` an `S`-prescheme in groups of finite presentation over `S`. Then the
functions `ρ_n`, `ρ_r`, `ρ_u`, `ρ_{ab}` (cf. 6.1 ter) are locally constructible functions on `S`.*

<!-- label: III.XV.6.3bis -->

It suffices to show (EGA IV 9.) that if `S` is a noetherian integral scheme with generic point `η`, the functions in
question are constant on a neighborhood of `η`. Possibly replacing `S` by a scheme `S′` finite over `S` and dominating
`S`, we may assume that `G_η` admits a Cartan subgroup `C_η` with a Chevalley decomposition `1 → L_η → C_η → A_η → 1`.
The argument made in 6.2 i) proves that this decomposition extends to a Chevalley decomposition over a neighborhood of
`η`:

```text
1 ⟶ L ⟶ C ⟶ A ⟶ 1.
```

Moreover, one may assume that `C` is a Cartan subgroup of `G` (6.3) and that the maximal torus `T_η` of `L_η` extends to
a maximal torus `T` of `L` (6.3). The corollary follows immediately from this and from the definitions.

**6.4.0.** Let then `S` be a prescheme, `G` an `S`-prescheme in groups of finite presentation over `S`, `ℒ` the functor
of subgroups of `G`, smooth, with connected fibers and equal to their connected normalizer (cf. § 5); `ℒ` is
representable (5.2 and 5.8). The remainder of this

<!-- original page 432 -->

section is devoted to the study of certain subfunctors of `ℒ`. More precisely, we introduce the subfunctors of `ℒ`,
denoted `ℒ_C` (resp. `𝒞𝒯`, resp. `𝒫`), defined as follows: for every `S`-prescheme `S′`, `ℒ_C(S′)` (resp. `𝒞𝒯(S′)`,
resp. `𝒫(S′)`) is the set of subgroups `H` of `G_{S′}`, smooth over `S′`, with connected fibers, equal to their
connected normalizer, and such that for every point `s′` of `S′`, `Hₛ′` contains a Cartan subgroup (6.1) of `Gₛ′` (resp.
is the centralizer in `(Gₛ′)⁰_{red}` of a sub-torus of `Gₛ′`, resp. is a parabolic subgroup (6.1) of `Gₛ′`).

<!-- label: III.XV.6.4.0 -->

**Theorem 6.4.** *Let `S` be a prescheme, `G` an `S`-prescheme in groups of finite presentation over `S`. Then the
`S`-functors `ℒ_C`, `𝒞𝒯`, `𝒫` above (6.4.0) are representable by `S`-preschemes of finite presentation over `S`,
quasi-projective over `S`.*

<!-- label: III.XV.6.4 -->

**Remark 6.5.** If `G` has smooth fibers, for example if `G` is smooth over `S`, or if the residue characteristics of
`S` are zero (Exp. VI_B 1.6.1), every subgroup `H` of `G`, smooth over `S` with connected fibers, such that for every
point `s` of `S`, `Hₛ` contains a Cartan subgroup of `(Gₛ)⁰`, is necessarily equal to its connected normalizer (and
consequently is an element of `ℒ_C(S)`). Indeed, using 5.1 iii), one may assume that `S` is the spectrum of a field, in
which case the property was noted at the end of the statement of Exp. XIII 2.1.

<!-- label: III.XV.6.5 -->

Note that one has natural monomorphisms

```text
𝒞𝒯 ↘
       ℒ_C ──→ ℒ.
𝒫  ↗
```

<!-- original page 433 -->

Let us show that these monomorphisms are open immersions of finite presentation (which will already prove, in view of
5.2, that `ℒ_C`, `𝒞𝒯`, `𝒫` are representable by `S`-preschemes, union of an increasing sequence of open subpreschemes,
quasi-projective and of finite presentation over `S`). Now this will follow, by the usual technique, from the following
lemma:

**Lemma 6.6.** *Let `S` be a prescheme, `G` an `S`-prescheme in groups of finite presentation, `H` a subgroup of `G`,
smooth with connected fibers. Then the set of points `s` of `S` such that `Hₛ` contains a Cartan subgroup of `Gₛ` (resp.
is equal to the centralizer in `(Gₛ)⁰_{red}` of a torus of `Gₛ`) is an open subset of `S`. If moreover `H` is equal to
its connected normalizer*[^XV-6-1]*, the set of points `s` of `S` such that `Hₛ` is a parabolic subgroup of `Gₛ` is also
an open subset of `S`.*

<!-- label: III.XV.6.6 -->

The assertion to be proved is local on `S`, which allows us to assume `S` affine, then, by EGA IV 8.1 and 6.3, `S`
noetherian. Denote by `E` the set of points of `S` having the property in question. It then follows from the assertions
effectively proved in 6.2 that `E` is ind-constructible. But `S` is noetherian, so to prove that `E` is open, it
suffices to show that `E` is stable under generizations (EGA IV 1.10.1). Using EGA II 7.1.9, we are finally led to prove
that if `S` is the spectrum of a discrete valuation ring, and if the closed point `s` belongs to `E`, then so does the
generic point `t`.

<!-- original page 434 -->

We shall need the following lemma:

**Lemma 6.7.** *Let `A` be a complete noetherian local ring, `S = Spec A`, `s` the closed point of `S`, `H` an
`S`-prescheme in groups, smooth with connected fibers, `Tₛ` a sub-torus of `Hₛ`. Then:*

- *i) There exists a closed subgroup prescheme `C` of `H`, smooth, with connected fibers, such that
    `Cₛ = Centr_{Hₛ}(Tₛ)`.*
- *ii) For every point `t` of `S`, `C_t` is the centralizer in `H_t` of a sub-torus `T_t` of `H_t`.*

<!-- label: III.XV.6.7 -->

*Proof of 6.7.* Let `T⁰` be an `S`-torus such that there exists an isomorphism `u₀ : T⁰ₛ ⥲ Tₛ` (Exp. X 4.6). Let `𝔪` be
the maximal ideal of `A`, `A_n = A/𝔪ⁿ`, `S_n = Spec A_n`, `H_n = H ×_S S_n`, etc. Since `H` is smooth over `S`, for
every integer `n > 0` there exists an `S_n`-group morphism `u_n : T⁰_n → H_n` lifting `u₀` (Exp. IX 3.6), and one may
assume by induction on `n` that `u_n` lifts `u_{n−1}`. Moreover, let `q` be a prime number invertible on `S`; for every
integer `ℓ` equal to a power of `q`, denote by `_ℓu_n` the restriction of `u_n` to the subgroup `_ℓT⁰_n`. For fixed `ℓ`
and variable `n`, the morphisms `_ℓu_n` form a projective system, hence come from a unique `S`-group morphism
`_ℓu : _ℓT⁰ → H` (1.6 a)). Since `H` is separated (Exp. VI_B 5.2) and `u₀` is a monomorphism, `_ℓu` is a monomorphism
(Exp. IX 6.8), and even a closed immersion since it is finite, `_ℓT⁰` being finite over `S`. Denote by `M(ℓ)` the image
group. It is clear that the family of subgroups of multiplicative type `M(ℓ)` is coherent in the sense of 4.1. Let
`C_ℓ = Centr_H(M(ℓ))`, which is representable by a subgroup prescheme (2.5), closed (`H` is separated),

<!-- original page 435 -->

smooth over `S` (Exp. XI 2.4). The `C_ℓ` form a filtered decreasing family of closed subschemes, hence stationary, `H`
being noetherian. The stationary value is a smooth closed subgroup `C` such that `Cₛ = Centr_{Hₛ}(Tₛ)` by the density
theorem (Exp. IX 4.7). It remains to show that for every point `t` of `S`, `C_t` is the centralizer in `H_t` of a
sub-torus `T_t` (which will entail that `C_t` is connected). But this will follow from the more precise lemma below,
applied to the family `M(ℓ)_t` of subgroups of `H_t`:

**Lemma 6.8.** *Let `G` be a connected algebraic group defined over a field `k`, `r` an integer `> 0`, `q` an integer
prime to the characteristic*[^N.D.E-XV-7] *of `k`, `M(ℓ)` (`ℓ` ranging over the powers of `q`) a coherent family of
subgroups of `G`, of multiplicative type and of type `(ℤ/ℓℤ)ʳ` (cf. 4.6), `M` the algebraic subgroup of `G` generated by
the `M(ℓ)` (*loc. cit.*), `T` the unique maximal torus of `M` (cf. 3.4). Then*

```text
Centr_G(T) = Centr_G(M) = Centr_G(M(ℓ))    for ℓ large enough.
```

<!-- label: III.XV.6.8 -->

The last equality is clear. To prove the first, introduce the center `Z` of `G`, `G′ = G/Z`, `M′` (resp. `T′`) the image
of `M` (resp. `T`) in `G′`, `K` the inverse image of `T′` in `G` (i.e. the algebraic subgroup of `G` generated by `T`
and `Z`). It evidently suffices to prove that `K ⊃ M`, hence that `T′ = M′`. Now, `M` is smooth and connected (4.6) and
`G′` is affine (Exp. XII 6.1), so `M′` is a direct product of its maximal torus

<!-- original page 436 -->

`T′` (Exp. XII 6.6 d)) and a unipotent group (*Bible* 4 Th. 4) (one may assume `k` algebraically closed). The image of
`M(ℓ)` in `M′` is therefore necessarily contained in `T′`. So the inverse image of `T′` in `M` majorizes `M(ℓ)` for
every `ℓ`, hence equals `M`. Consequently `M′ = T′`. This proves 6.8 and hence 6.7.

This being so, let us prove 6.6. We have reduced to the case where `S` is the spectrum of a discrete valuation ring `A`,
which one may further assume complete with algebraically closed residue field. Possibly replacing `A` by its
normalization in a finite extension of its field of fractions, one may assume that `(G_t)_{red}` is smooth[^N.D.E-XV-8].
It is clear that to prove 6.6 one may replace `G` by the connected component of the schematic closure in `G` of
`(G_t)⁰_{red}`, hence assume `G` flat over `S` with connected fibers, and `G_t` smooth.

a) Suppose `Hₛ` is the centralizer in `(Gₛ)_{red}` of a torus `Tₛ`, and let us show that `H_t` is then the centralizer
in `G_t` of a sub-torus of `G_t`. By Lemma 6.7, there exists a subgroup scheme `C` of `H`, smooth over `S`, whose closed
fiber is `Hₛ` and such that `C_t = Centr_{H_t}(T_t)`, where `T_t` is a sub-torus of `H_t`. Since `H` is smooth over `S`
with connected fibers, one concludes for dimension reasons that `C = H`. Keeping the notation of 6.7, one has
`H = C = C_ℓ` for `ℓ` large. Consider similarly `C′_ℓ = Centr_G(M(ℓ))` (2.5), and let `C′` be the stationary value of
`C′_ℓ` for `ℓ` large (2.5 bis). The group scheme `C′` majorizes `H` and is such that `C′_t = Centr_{G_t}(T_t)` (6.8) and
`C′ₛ = Centr_{Gₛ}(Tₛ)`. The hypothesis made on `Hₛ` implies `dim Hₛ = dim C′ₛ`. Moreover, `dim Hₛ = dim H_t` (since `H`
is smooth over `S`) and `dim C′_t ⩽ dim C′ₛ` (Exp. VI_B 4.1),

<!-- original page 437 -->

so `dim H_t = dim C′_t`. But `G_t` being smooth and connected, `C′_t = Centr_{G_t}(T_t)` is smooth and connected, so
finally `H_t = C′_t = Centr_{G_t}(T_t)`.

b) Suppose `Hₛ` contains a Cartan subgroup `Cₛ` of `Gₛ`, i.e. the centralizer in `(Gₛ)_{red}` of a maximal torus `Tₛ` of
`Gₛ`. By 6.7, there exists a subgroup scheme `C` of `H`, smooth over `S`, with connected fibers, lifting `Cₛ`. It
evidently suffices to prove that `C_t` contains a Cartan subgroup of `G_t`. Now by a) applied with `H = C`, `C_t` is the
centralizer in `G_t` of a sub-torus of `G_t`, hence contains a Cartan subgroup of `G_t`.

c) Suppose `Hₛ` is a parabolic subgroup of `Gₛ`. Let `N = Norm_G(H)`. By hypothesis, `H` is equal to its connected
normalizer, so `Nₛ` is smooth, and consequently equals `Norm_{(Gₛ)_{red}}(Hₛ) = Hₛ` (Exp. XII 8 bis). But then `N` is
flat over `S`. We shall see in Exp. XVI that, under these conditions, `G/N` is representable. Since `Hₛ = Nₛ` is a
parabolic subgroup of `G`, `(G/N)ₛ` is proper. Since `(G/N)` has connected fibers and is flat over `S`, it follows from
EGA III 5.5.1 that `(G/N)` is proper over `S`. So `(G/N)_t = G_t/N_t` is proper over `t`, and the same is true of
`G_t/H_t`, since `N_t/H_t` is finite. It then suffices to apply the following lemma:

**Lemma 6.9.** \*Let `k` be a field, `G` a `k`-algebraic group, `H` a smooth connected algebraic subgroup of `G`,

<!-- original page 438 -->

`N = Norm_G H`; then if `dim H = dim N` and if `G/H` is proper, `H` is a parabolic subgroup of `G`.\*

<!-- label: III.XV.6.9 -->

Indeed, one may assume `k` algebraically closed and `G` smooth and connected. The center `Z` of `G` is contained in `N`,
and the hypothesis `dim H = dim N` entails that `Z⁰ = (Z)⁰_{red}` is contained in `H`, so `G′ = G/Z⁰` is affine (Exp.
XII 6.1). Replacing `G` by `G′` and `H` by its image in `G′`, one is reduced to the case where `G` is affine (Exp. XIV
4.9), and Lemma 6.9 then follows from *Bible* 6 Th. 4. We have therefore proved Lemma 6.6.

To complete the proof of 6.4, we must prove that the `S`-preschemes representing `ℒ_C` (resp. `𝒞𝒯`, resp. `𝒫`) are of
finite presentation over `S`. This assertion is local on `S`, which allows us to assume `S` affine, then, `G` being of
finite presentation, `S` noetherian (EGA IV 8.9). We have just seen that the natural inclusions `𝒞𝒯 → ℒ` (resp. `𝒫 → ℒ`)
are immersions, so the same is true of the inclusions `𝒞𝒯 → ℒ_C` (resp. `𝒫 → ℒ_C`), and consequently it suffices to
prove that `ℒ_C` is representable by an `S`-prescheme of finite presentation.

Let us resume the notation introduced in 5.2. For every integer `n ⩾ 0`, let `ℒ_n` be the subfunctor of `ℒ` such that

```text
ℒ_n(S′) = {H ∈ ℒ(S′) such that Norm_{G_{S′}}(H) = Norm_{G_{S′}}(H^{(n)})}.
```

The `S`-functor `ℒ_n` is therefore representable by an open subprescheme of `ℒ`, sum of the `ℒ^r_n`. Each `ℒ^r_n` is of
finite presentation over `S` (5.3) and is empty for `r > sup_{s ∈ S} dim Gₛ` (which is a finite number, `S` being
quasi-compact), so `ℒ_n` is

<!-- original page 439 -->

of finite presentation over `S`. It suffices to prove that `ℒ_C` is contained in `ℒ_n` for `n` large enough.

For every point `s` of `S`, let `d(s)` be the smallest integer `n` (finite or infinite) such that
`ℒ_{C, Gₛ} ⊂ ℒ_{n, Gₛ}`. It suffices to show that the function `d` is bounded on `S`, since if `M` is an upper bound,
`ℒ_C` will be set-theoretically contained in `ℒ_M`, so `ℒ_C` will be contained in `ℒ_M`, since the latter is an open
subset of `ℒ`. An immediate constructibility argument reduces us to proving that if `S` is noetherian integral with
generic point `t`, then `d` is bounded on a neighborhood of `t`.

a) **Reduction to the case where `G` is smooth over `S`.** Proceeding as in 6.2, one sees that, possibly changing `S`,
one may assume that `(G)_{red}` is a group prescheme smooth over `S`, which we shall denote `G′`. Set `X = ℒ_{C, G}`,
`X′ = ℒ_{C, G′}` and let `H` (resp. `H′`) be the subgroup prescheme of `G_X` (resp. `G′_{X′}`) universal for the functor
`ℒ_{C, G}` (resp. `ℒ_{C, G′}`). Since `H` is smooth over `X`, `H ×_X X_{red}` is reduced, hence contained in
`G′_{X_{red}}`, and is an element of `ℒ_{C, G′}(X_{red})`, whence a canonical morphism `p : X_{red} → X′`. It is clear
that `p` is a monomorphism; let us show that `p` is even an immersion. Let `N′` be the normalizer of `H′` in `G_{X′}`.
The set of points `s` of `X′` such that the immersion `H′ₛ → N′ₛ` is an open immersion is an open subset `U`, and
`H′|_U → N|_U` is an open immersion (Exp. VI_B 2.5 and EGA IV 17.9.5). It follows from 5.1 iii) that `U` is the largest
open subset of `X′` above which `H′` is equal to its connected normalizer in `G_{X′}`, so `H′|_U ∈ ℒ_{C, G}(U)`. One
immediately deduces that `p` is an isomorphism of `X_{red}` onto `U_{red}`. If one shows that `ℒ_{C, G}` is of finite
type when `G` is smooth, `X′` will be of finite type over `S`,

<!-- original page 440 -->

so `X_{red}` will be of finite type (`S` is noetherian) and consequently will be contained in `ℒ^M_G` for `M` large
enough, and the same will hold of `X`.

b) **Case where `S` is the spectrum of an algebraically closed field `k` of characteristic `p > 0` and `G` is a smooth
algebraic group over `k`.** Instead of using the infinitesimal neighborhoods `H^{(n)}` of a subgroup prescheme `H` of
`G`, we shall use the radicial subgroups `F_n(H)`, kernels of the iterates of the Frobenius morphism in `H` (Exp. VII_A
4), which is legitimate here, since `F_n(H)` is contained in the infinitesimal neighborhood of order `pⁿ` of the unit
section of `H`. If `T` is a sub-torus of `G`, `F_n(T) = _{pⁿ}(T)`, and it is immediate by duality that
`Centr_G(_{pⁿ}(T))` is equal to `Centr_G(T)` for `n` large enough. One then has the following more precise proposition:

**Proposition 6.10.** *Let `k` be a field of characteristic `p > 0`, `G` a smooth `k`-algebraic group, `T` a maximal
torus of `G_{k̄}`, `m` the smallest integer such that*

```text
Centr_G(_{pᵐ}(T))⁰ = Centr_G(T)⁰.
```

*Then, for every `k`-prescheme `S` and every `H ∈ ℒ_C(S)`, one has*

```text
Norm_{G_S}(H) = Norm_{G_S}(F_m(H)).
```

*A fortiori, `ℒ_C` is contained in `ℒ^{pᵐ}`.*

<!-- label: III.XV.6.10 -->

Since `H` is smooth over `S`, of finite presentation over `S` and has a constant nilpotent rank (namely that of `G`), we
shall see in the following section (7.3) that the functor `𝒞_H`

<!-- original page 441 -->

of Cartan subgroups of `H` is representable by an `S`-prescheme, smooth over `S` (the reader will verify that the proof
given of this property does not use the fact that `ℒ_{C, H}` is of finite type over `S`). It then follows from Exp. XIII
3.1 that one may consider the open subset `U` of regular points of `H`.

Let `S′` be an `S`-prescheme, `g` an element of `G(S′)` normalizing `F_m(H)_{S′}`. To prove that `g` normalizes
`H_{S′}`, it suffices to prove that `int(g)U_{S′}` is contained in `H_{S′}`; indeed, `H_{S′} ∩ int(g)H_{S′}` will then
contain an open subgroup of `int(g)H`, hence will be equal to

<!-- original page 442 -->

`int(g)H`, since the latter has connected fibers. Possibly replacing `S′` by a suitable `S″`, then `S″` by `S`, we are
reduced to proving that if `g ∈ G(S)` normalizes `F_m(H)` and if `u ∈ U(S)`, then `int(g)u ∈ H(S)`.

Now let `C` be the unique Cartan subgroup of `H_S` "containing" `u` (Exp. XIII 3.2). It suffices to show that
`C′ = int(g)C ⊂ H`. Since `H ∈ ℒ_{C, G}(S)`, `C` is also a Cartan subgroup of `G`; but the latter admits maximal tori,
so (Exp. XII 7.1 (a)) `C` is the centralizer in `G⁰_S` of its unique maximal torus `T`. It follows from the definition
of `m` (and from the fact that any two maximal tori of `G` are locally conjugate for fpqc (Exp. XII 7.1)) that

```text
C = (Centr_G(T))⁰ = Centr_G(_{pᵐ}(T))⁰,
```

whence by conjugation by `g`:

```text
C′ = Centr_G(int(g)(_{pᵐ}(T)))⁰.
```

But `int(g)(_{pᵐ}(T))` is a subgroup of multiplicative type of `int(g)(F_m(H)) = F_m(H)` (`g` normalizes `F_m(H)`),
hence is contained in `H`. It then follows from Exp. XIII 2.1 (which is proved when the base is a field, but extends
immediately to the case of an arbitrary base) that for `C′` to be contained in `H` it suffices that

```text
Lie C′ ⊂ Lie H.
```

Now `Lie C′ = int(g)(Lie C) ⊂ int(g)(Lie H)`.

On the other hand, if `m ⩾ 1`, which it is permissible to assume, one has (using Exp. VII_A 4.1.2):

```text
Lie H = Lie(F_m(H)) = Lie(int(g)(F_m(H))) = int(g)(Lie H).
```

So `Lie C′ ⊂ Lie H`, which completes the proof of 6.10.

We shall need another definition of the integer `m` introduced in 6.10.

**Lemma 6.11.** *Let `G` be a smooth algebraic group defined over an algebraically closed field `k` of characteristic
`p > 0`, `T` a maximal torus of `G`, `𝔤 = Lie G`, and `R` the family of non-zero characters of `T` appearing in the
representation of `T` in `𝔤` induced by the adjoint representation of `G`. For every element `r ∈ R`, denote by `e_r`
the largest integer `n` such that `pⁿ` divides `r` in the group of characters of `T`. Then `m = sup_{r ∈ R}(e_r + 1)` if
`R ≠ ∅`, and `m = 0` otherwise.*

<!-- label: III.XV.6.11 -->

Indeed, `Centr_G(T)` is smooth and contained in `Centr_G(_{pᵐ}(T))`, so

```text
(Centr_G T)⁰ = (Centr_G(_{pᵐ}(T)))⁰ ⇔ Lie(Centr_G T) = Lie(Centr_G(F_m(T)))
                                    ⇔ 𝔤^T = 𝔤^{_{pᵐ}(T)}    (Exp. II 5.2.3).
```

<!-- original page 443 -->

Now with the usual notation,

```text
𝔤 = 𝔤_0 ⊕ ∐_{r ∈ R} 𝔤_r.
```

So `𝔤^T = 𝔤_0` and `𝔤^{_{pᵐ}(T)} = 𝔤_0 + ∐_{r ∈ R_0} 𝔤_r`, where `R_0` is the subset of `R` consisting of characters of
`T` whose restriction to `_{pᵐ}(T)` is zero. But a non-zero character `r` of `T` has trivial restriction to `_{pᵐ}(T)`
if and only if `m ⩽ e_r`, whence the lemma.

c) **Return to the proof of 6.4.** We have reduced (by point a) and the section preceding it) to the case where `S` is a
noetherian integral scheme and `G` is smooth over `S`. We must show that the function `d` is bounded on a neighborhood
of the generic point `t` of `S`. Possibly changing `S`, we may assume that `G` admits a trivial maximal torus (6.2)
`T = D_S(M)`. Let then `𝔤 = ∐_{λ ∈ M} 𝔤_λ` be the decomposition of the Lie algebra of `G` according to the characters of
`T`, and let `R` be the finite set of non-zero characters of `M` such that `𝔤_λ ≠ 0`. Let us distinguish two cases:

**1st case: the point `t`, and hence all points of `S`, have residue characteristic `p > 0`.** It is clear, from what
precedes, that the function `d` is then bounded by `pᵐ`, where `m` is defined as in 6.11.

**2nd case: the point `t` has residue characteristic zero.** For every `λ ∈ R`, let `n_λ` be the largest integer
dividing `λ` in the group `M`, and set `n = ∏ n_λ`, `λ ∈ R`. For every prime number `q` dividing `n`, denote by `S_q`
the closed subset of `S` consisting of points of `S` whose residue characteristic equals `q`, and let `U` be the
non-empty open subset (it contains `t`) complementary in `S` to the union of the `S_q`. If now `s` is a point of `U`,
either `s`

<!-- original page 444 -->

has residue characteristic zero, in which case `d(s) = 1` (5.6), or `s` has residue characteristic `p > 0` not dividing
`n`, so the integer `m` relative to the group `Gₛ`, defined in 6.11, is at most one. Moreover, it follows from Exp.
VII[^N.D.E-XV-9] that

```text
Norm_{G_{S′}}(F_1(H)) = Norm_{G_{S′}}(Lie H) = Norm_{G_{S′}}(H^{(1)}).
```

Finally, it follows from 6.10 that if `H ∈ ℒ_{C, Gₛ}(S′)`, one has `Norm_{G_{S′}}(H) = Norm_{G_{S′}}(H^{(1)})`, and
consequently `d(s) ⩽ 1`, so `d` is bounded by `1` on `U`.

This completes the proof of 6.4.

**Corollary 6.12.** *Let `S` be a prescheme and `G` an `S`-prescheme in groups of finite presentation. Suppose that the
nilpotent rank (resp. the dimension of the Borel subgroups) of the fibers of `G` is a locally constant function on `S`.
Then the functor `𝒞` of Cartan subgroups of `G` (resp. the functor `ℬ` of Borel subgroups of `G`) is representable by an
`S`-prescheme of finite presentation over `S`.*

<!-- label: III.XV.6.12 -->

Indeed, possibly restricting `S`, we may assume that the nilpotent rank `ν` of the fibers is constant. But then it is
clear that `𝒞` is represented by the open-closed subprescheme of the prescheme `X` representing `ℒ_C` (6.4) above which
the universal subgroup of `G_X` relative to the functor `ℒ_C` is of relative dimension `ν`. The proof is analogous for
the functor `ℬ`, in view of the representability of the functor `𝒫`.

## 7. Cartan subgroups of a smooth group

<!-- label: III.XV.7 -->

<!-- original page 445 -->

**Proposition 7.1.** *Let `S` be a prescheme, `G` an `S`-prescheme in groups of finite presentation, smooth over `S`,
with connected fibers.*

- *i) Let `𝒞𝒯` be the `S`-functor `(Sch/S)° → Ens` such that for every `S`-prescheme `S′`:*
    > *`𝒞𝒯(S′)` = set of subgroup preschemes `H` of `G_{S′}`, smooth over `S′`, such that for every point `s′` of `S′`,
    > `Hₛ′` is the centralizer in `Gₛ′` of a sub-torus of `Gₛ′`.*
- *Then `𝒞𝒯` is representable by an `S`-prescheme of finite presentation over `S`, smooth and quasi-projective over
    `S`.*
- *ii) If `S` is artinian and `H ∈ 𝒞𝒯(S)`, then `H` is the centralizer in `G` of a sub-torus of `G`. If `S` is the
    spectrum of a Henselian local ring and `H ∈ 𝒞𝒯(S)`, then `H` is the centralizer in `G` of a subgroup of
    multiplicative type of `G`, étale over `S`.*
- *iii) If `L` is an `S`-prescheme in groups, smooth and of finite presentation over `S`, `i : L → G` an `S`-group
    monomorphism, and `H` an element of `𝒞𝒯(S)`, then `Transp_G(H, L)` and `Transp^{str}_G(H, L)` (cf. Exp. VIII 6.5 e))
    are representable by closed subpreschemes of `G`, smooth over `S`.*
- *iv) If `H ∈ 𝒞𝒯(S)`, `H` is closed in `G`, `N = Norm_G(H)` is representable by a closed subgroup prescheme of `G`,
    smooth over `S`;*

<!-- original page 446 -->

*`N/H` is representable by an `S`-prescheme in groups, separated over `S`, étale and of finite type over `S`; `G/N` is
representable by an `S`-prescheme smooth and quasi-projective over `S`.*

- *v) Let `G′` be an `S`-prescheme in groups of finite presentation over `S` and `u : G → G′` a faithfully flat
    `S`-group morphism, so that `G′` satisfies the same hypotheses as `G` (Exp. VI_B 9). Then if `H ∈ 𝒞𝒯_G(S)`, the
    image of `H` by `u` is representable by a subgroup prescheme `H′` of `G′` which is an element of `𝒞𝒯_{G′}(S)`.
    Moreover, `H → H′` is faithfully flat, and if `H` is the centralizer in `G` of a torus `T`, `H′` is the centralizer
    in `G′` of the torus `T′ = u(T)`.*
- *vi) Under the conditions of v), consider the `S`-morphism*

```text
ũ : 𝒞𝒯_G ⟶ 𝒞𝒯_{G′},    H ↦ H′ = u(H).
```

- *Then `ũ` is a quasi-compact faithfully flat morphism; if moreover `Ker u` is central, `ũ` is an isomorphism, the
    inverse isomorphism being `H′ ↦ u⁻¹(H′)`.*

<!-- label: III.XV.7.1 -->

*Proof of ii).* For the first assertion, we may assume `S` local artinian with closed point `s`. Let `H ∈ 𝒞𝒯(S)` and let
`Tₛ` be the maximal central torus of `Hₛ`, which is already defined over `κ(s)` (cf. 3.4). Since `Hₛ ∈ 𝒞𝒯(s)`, one has
`Hₛ = Centr_{Gₛ} Tₛ`. The group `H` is smooth, so `Tₛ` lifts uniquely to a sub-torus `T` of `H`, central

<!-- original page 447 -->

in `H` (Exp. IX 3.6 bis and Exp. IX 5.6). But then `H′ = Centr_G T` majorizes `H` and has the same fiber as `H`; since
`H` is flat over `S`, one has `H = H′` (Exp. VI_B 2.5).

Suppose now that `S` is the spectrum of a Henselian local ring, which one may assume noetherian by the usual reductions.
Denote by `s` the closed point of `S`, `Tₛ` the maximal central torus of `Hₛ`, `q` an integer invertible on `S`, `ℓ` a
power of `q`, `T` an `S`-torus having a closed fiber isomorphic to `Tₛ` (Exp. X 4.6). Moreover, let `_ℓH` be the
"kernel" of the `ℓ`-th power morphism in `H`, and let `U_ℓ` be the largest open subset of `_ℓH` étale over `S`. It then
follows from 1.3 and from the fact that `H` is flat over `S` that `U_ℓ` majorizes `_ℓTₛ`. Since `S` is Henselian, there
exists a unique `S`-morphism

```text
u_ℓ : _ℓT ⟶ U_ℓ
```

which, on the closed fiber, induces the canonical immersion `_ℓTₛ → (U_ℓ)ₛ`. By uniqueness, one easily sees that `u_ℓ`
is an `S`-group morphism, central (Exp. IX 5.6 a)). Proceeding then as in 6.6 and 6.7, one shows that `u_ℓ` is an
immersion, and that if `M_ℓ` is the image group `u_ℓ(_ℓT)`, then `Centr_G(M_ℓ)` is equal to `H` for `ℓ` large enough
(this is where the noetherian hypothesis on `S` is used).

*Proof of i).* The group `G` is smooth over `S` with connected fibers, so if `H ∈ 𝒞𝒯(S)`, `H` has connected fibers (Exp.
XII 6.6 b)) and is equal to its connected normalizer (6.5), so that the functor `𝒞𝒯` defined in 7.1 i) coincides with
the functor also denoted `𝒞𝒯` defined in 6.4.0. So, by Theorem 6.4, `𝒞𝒯` is representable by an `S`-prescheme of finite
presentation and quasi-projective over `S`. It remains to show that this prescheme is smooth over `S`. One first reduces
by EGA IV 8

<!-- original page 448 -->

to the case where `S` is affine noetherian. Thanks to Exp. XI 1.5, it then suffices to prove that if `S` is the spectrum
of a local artinian ring, `S₀` a subscheme defined by a nilpotent ideal, `H₀` an element of `𝒞𝒯(S₀)`, then `H₀` lifts to
a subgroup prescheme `H` of `G`, smooth over `S`. Now by ii), `H₀ = Centr_{G₀} T₀`, where `T₀` is a sub-torus of `G₀`.
Since `G` is smooth, `T₀` lifts to a sub-torus `T` of `G` (Exp. IX 3.6 bis), and it suffices to take `H = Centr_G(T)`,
which is indeed smooth over `S` (Exp. XI 2.4 and Lemma 2.5).

*Proof of iii).* Since `H` is smooth with connected fibers, by Exp. XI 6.11, `Transp_G(H, L)` is representable by a
closed subprescheme of `G` of finite presentation over `S`. To show that this transporter is smooth, one reduces, as
above, to proving that if `S` is local artinian, `S₀` a closed subprescheme of `S`, `g₀ ∈ G(S₀)` such that
`int(g₀)H₀ ⊂ L₀`, then `g₀` lifts to `g ∈ G(S)` such that `int(g)H ⊂ L`. The group `G` being smooth over `S`, there
exists a section `g₁` of `G` lifting `g₀`; let `H′ = int(g₁)H`. So this is an element of `𝒞𝒯(S)` such that `H′₀ ⊂ L₀`.
By ii), `H′` is the centralizer in `G` of a torus `T′` of `G`. Since `L` is smooth, the torus `T′₀` of `L₀` lifts to a
torus `T″₀` of `L` (Exp. XI 3.6 bis). The group `Centr_L T″₀` is contained in `Centr_G T″₀`, has the same fiber as the
latter (namely `H′₀`) and is smooth, so equals `Centr_G T″₀ = H′₀`. The sub-tori `T′` and `T″₀` of `G` are two liftings
of `T′₀`, so are conjugate by an element `h` of `G(S)` reducing to the unit section of `G₀` (Exp. IX 3.3 bis); the same
is therefore true of their centralizers `H′` and `H″₀` in `G`. The section `g = h g₁` lifts `g₀` and one has
`int(g)H ⊂ L`.

<!-- original page 449 -->

If now `g ∈ Transp_G(H, L)(S)`, for `int(g)H = L` it is necessary and sufficient that for every `s ∈ S`,
`dim Hₛ = dim Lₛ`. It follows that if `U` denotes the open-closed subprescheme of `S` above which the fibers of `H` have
the same dimension as those of `L`, the strict transporter of `H` in `L`, `Transp^{str}_G(H, L)`, is representable by
the `S`-prescheme

```text
U ×_S Transp_G(H, L).
```

*Proof of iv).* To see that if `H ∈ 𝒞𝒯(S)`, `H` is closed in `G`, one may assume `S` affine noetherian, then `S`
spectrum of a complete local ring (EGA IV 8); but then `H` is the centralizer in `G` of a subgroup of multiplicative
type (by ii)), hence is closed since `G` is separated over `S` (Exp. VI_B 5.2).

By iii), `N = Norm_G(H) = Transp^{str}_G(H, H)` is representable by a subgroup prescheme smooth over `S` and closed in
`G`. Consider the `S`-morphism

```text
G ⟶ 𝒞𝒯,    g ↦ int(g)H.
```

It follows from iii) that this morphism is smooth, so its image is an open subset `U` of `𝒞𝒯`. One then proves as in
Exp. XI 5.3 that `G/N` is representable by `U`, hence in particular is quasi-projective.

Let us now study the quotient `N/H`. Thanks to EGA IV 8, to prove that `N/H` is representable, one may assume `S` affine
noetherian, then `S` the spectrum of a local ring `A`, of finite (Krull[^N.D.E-XV-10]) dimension.

<!-- original page 450 -->

We shall proceed by increasing induction on the dimension of `S`. If `dim S = 0`, the property follows from Exp. VI_A §
4\. Note now that if `N/H` is representable, it is separated over `S` (since `H` is closed in `N` by iv)), of finite type
and étale over `S` (since `N` is smooth over `S`, of finite type and `H` is open in `N`), so `N/H` is necessarily
quasi-affine over `S` (SGA 1 VIII.6.2). By effective descent of quasi-affine schemes (*loc. cit.* 7.9), one may replace
`A` by its completion, hence assume `S` spectrum of a complete noetherian local ring. Let `s` be its closed point and
`U = S \ s`. By induction hypothesis, `(N|_U)/(H|_U)` is representable by a `U`-group `K`. Let then `Tₛ` be the maximal
central torus of `Hₛ`, `q` an integer invertible on `S`, `ℓ` a power of `q`, `M_ℓ` the unique central subgroup of
multiplicative type of `H` lifting `_ℓTₛ` (cf. ii)). Choose `ℓ` large enough that `Centr_G(M_ℓ) = H`, and let
`N′ = Norm_G(M_ℓ)`. Since `Centr_G(M_ℓ) = H`, one has `N′ ⊂ Norm_G(H)`. Moreover, one immediately verifies that `Tₛ` (so
also `(M_ℓ)ₛ`) is a characteristic subgroup of `Hₛ` (i.e. stable under `Aut_{gr}(Hₛ)`), so `Nₛ` normalizes `(M_ℓ)ₛ` and
consequently `Nₛ = N′ₛ`. The proof of Exp. XI 5.9 then shows that the quotient `N′/H = Norm_G(M_ℓ)/Centr_G(M_ℓ)` is
representable by an `S`-group `K′`. Since `N′` is smooth over `S` and `N′ₛ = Nₛ`, `N′` is an open subgroup of `N` (Exp.
VI_B 2.5) containing `H`, so the image of `N′|_U` in `K` is an open subgroup, isomorphic to `K′|_U`. Let `L` be the
`S`-prescheme obtained by gluing `K` and `K′` along the previous isomorphism, and let `p` be the `S`-morphism `N → L`
obtained by gluing the canonical projections `N|_U → K` and `N′ → K′`.

<!-- original page 451 -->

It is clear that `(L, p)` represents the quotient `N/H`.

*Proof of v).* Suppose first that `S` is the spectrum of a field `k`. The image `H′` of `H` is then a smooth subgroup of
`G′`. We must show that `H′ ∈ 𝒞𝒯_{G′}(S)`, which will follow from the following more precise lemma:

**Lemma 7.2.** *Let `u : G → G′` be an epimorphism of smooth connected `k`-algebraic groups, `T` a torus of `G`, `T′`
its image in `G′`. Then*

```text
u(Centr_G T) = Centr_{G′} T′.
```

<!-- label: III.XV.7.2 -->

Denote `H = Centr_G T`, `H′ = Centr_{G′} T′`, `H″ = u(H)`. One has `H″ ⊂ H′`. To prove that `H′ = H″`, one may assume
the base field algebraically closed, and it suffices to prove that every Cartan subgroup of `H′` is contained in `H″`.
Indeed, `H″` will then contain the open subset of regular points of `H′`, so `H″` will be an open subgroup of `H′` and
consequently will be equal to `H′` since the latter has connected fibers. So let `C′` be a Cartan subgroup of `H′`; `C′`
is also a Cartan subgroup of `G′`, since `H′` is the centralizer of a torus `T′`, hence has the same reductive rank and
the same nilpotent rank as `G′`. Set `K = (u⁻¹(C′))⁰_{red}`. Since `T′` is in the center of `H′`, `C′` contains `T′`, so
`K` contains `T`. Let then `C` be a Cartan subgroup of `K` containing `T`. The torus `T` is contained in the unique
maximal torus of `C`, which is central in `C` (Exp. XII 6.6 c)), so `C` is contained in `H = Centr_G T`. Using now the
fact that any two Cartan subgroups of `G` are conjugate and that the image of a Cartan subgroup of `G` is a Cartan
subgroup of `G′` (Exp. XII 6.6), one

<!-- original page 452 -->

deduces that `C` is also a Cartan subgroup of `G`; its image is therefore a Cartan subgroup of `G′`; as it is contained
in `C′`, one has `u(C) = C′`, so `C′` is indeed contained in `H″`.

We have therefore established v) when `S` is the spectrum of a field `k`. Let us now study the general case. Since `G`,
`H` and `G′` are of finite presentation over `S`, to prove that `u(H)` is representable and is an element of
`𝒞𝒯_{G′}(S)`, one reduces by the usual technique to the case where `S` is affine noetherian, then to the case where `S`
is the spectrum of a local ring. By fpqc descent of subpreschemes of `G′`, one may even assume that `S` is the spectrum
of a complete noetherian local ring `A`.

Let us resume the notation of ii), namely: let `Tₛ` be the maximal central torus of `Hₛ` (`s` is the closed point of
`S`), `M_ℓ` a subgroup of multiplicative type of `H` lifting `_ℓTₛ` such that `H = Centr_G M_ℓ`. Let `T′ₛ` be the image
of `Tₛ` in `G′ₛ`. Since `G′` is separated over `S` (Exp. VI_B 5.2), the image of `M_ℓ` by `u` is a subgroup of
multiplicative type `M′_ℓ` of `G′` (Exp. IX 6.8). Set then `H′ = Centr_{G′} M′_ℓ`, which is a smooth subgroup prescheme
of `G′`. For every integer `ℓ′` equal to a power of `q`, there exists `ℓ` such that `(M′_ℓ)ₛ` majorizes `_{ℓ′}T′ₛ`, so
we may assume `ℓ` chosen large enough that `H′ₛ = Centr_{G′ₛ} T′ₛ = uₛ(Hₛ)`, where the last equality follows from 7.2.
The restriction of `u` to `H`, namely `v`, evidently factors through `H′`. Let us prove that `v : H → H′` is a flat
morphism. Since `H` and `H′` are flat over `S` and `Hₛ → H′ₛ` is flat, `v` is flat on a neighborhood of `Hₛ` (EGA IV
11.3.10 and 11.3.1). The morphism `v` is therefore flat on an open subgroup of `H` (Exp. VI_B 2.2), so `v` is flat, `H`
having connected fibers.

<!-- original page 453 -->

The set-theoretic image of `H` is therefore an open subset of `H′` (necessarily equal to `(H′)⁰`) which, equipped with
its induced structure, represents the image sheaf `u(H)` (for the fpqc topology). The fact that `u(H)` is an element of
`𝒞𝒯_{G′}(S)` then follows from 7.2.

Suppose now that `H` is the centralizer in `G` of a torus `T`, and let `T′` be the image of `T` by `u`, which is a
sub-torus of `G′` (Exp. IX 6.8). The image of `H` by `u` is contained in `Centr_{G′}(T′)`, coincides fiber by fiber with
the latter (7.2), and is smooth over `S`, so `u(H) = Centr_{G′}(T′)`.

*Proof of vi).* To show that `ũ` is a faithfully flat `S`-morphism, knowing that `𝒞𝒯_G` and `𝒞𝒯_{G′}` are smooth over
`S` (by i)), it suffices to verify it on the geometric fibers. We are therefore reduced to the case where `S` is the
spectrum of an algebraically closed field `k`. Let `H′ ∈ 𝒞𝒯_{G′}(k)`, `T′` its maximal central torus, `T` a sub-torus of
`G` whose image is `T′`, `H = Centr_G(T)`, so that `H′ = u(H)` (7.2), `N = Norm_G(H)`, `N′ = Norm_{G′}(H′)`. We have
shown in iv) that `G/N` (resp. `G′/N′`) canonically identifies with open neighborhoods of `H` in `𝒞𝒯_G`

<!-- original page 454 -->

(resp. of `H′` in `𝒞𝒯_{G′}`). Under these identifications, the restriction of `ũ` to `G/N` coincides with the natural
morphism

```text
w : G/N ⟶ G′/N′
```

deduced from `u` by passage to the quotient. Now `w` is an epimorphism of homogeneous spaces under `G`, hence is
faithfully flat. This proves that `ũ` is a flat morphism such that `ũ(𝒞𝒯_G)`, which is therefore an open subset of
`𝒞𝒯_{G′}`, contains every point of `𝒞𝒯_{G′}(k)`. Since `𝒞𝒯_{G′}` is of finite type over `k`, one deduces that `ũ` is
surjective, hence faithfully flat.

The complementary assertions contained in vi) in the case where `Ker u` is central follow from Exp. XII 7.12.

The following theorem generalizes Theorem 7.1 of Exp. XII:

**Theorem 7.3.** *Let `S` be a prescheme, `G` an `S`-prescheme in groups of finite presentation over `S`, smooth, with
connected fibers, and consider the `S`-functor `𝒞 : (Sch/S)° → Ens` such that:*

> *`𝒞(S′)` = set of Cartan subgroups of `G_{S′}`.*

- *i) The following conditions are equivalent:*
    - *a) The functor `𝒞` is representable.*
    - *b) The functor `𝒞` is representable by an `S`-prescheme, smooth, quasi-projective, of finite presentation over `S`,
        with affine fibers.*
    - *c) The group `G` admits locally for the étale topology a Cartan subgroup.*
    - *d) The group `G` admits locally for the faithfully flat topology a Cartan subgroup.*
    - *e) The nilpotent rank of the fibers of `G` is a locally constant function on `S`.*
- *ii) If the preceding conditions hold, any two Cartan subgroups of `G` are locally conjugate for the étale topology.*

<!-- original page 455 -->

*The set of regular points of the fibers of `G` (Exp. XIII 2.7) is an open subset `G_{reg}`, of finite presentation over
`S`, and every section of `G_{reg}` over `S` is contained in a unique Cartan subgroup of `G`.*

- *iii) Let `G′` be an `S`-prescheme in groups of finite presentation over `S` and `u : G → G′` a faithfully flat
    `S`-group morphism, so that `G′` is smooth over `S` with connected fibers. Then if `C` is a Cartan subgroup of `G`,
    `u(C) = C′` is representable by a Cartan subgroup of `G′`, and `C → C′` is faithfully flat.*
- *iv) Under the conditions of i) and iii) the morphism*

```text
ũ : 𝒞_G ⟶ 𝒞_{G′},    C ↦ u(C) = C′
```

*is faithfully flat. If moreover `Ker(u)` is central, `ũ` is an isomorphism.*

- *v) For any complementary information concerning the transporters, or the relations with maximal tori, one may consult
    7.1 and Exp. XII 7.1.*

<!-- label: III.XV.7.3 -->

*Proof.* i) We shall show that b) ⇒ c) ⇒ d) ⇒ e) ⇒ b) ⇒ a) ⇒ d).

b) ⇒ c). Let `s` be a point of `S`. Since `Cₛ` is smooth over `κ(s)`, there exist points of `Cₛ` whose residue field is
a finite separable extension of `κ(s)`. Applying Exp. XI 1.10, one sees that there exist an open neighborhood `U` of `s`
and an étale surjective morphism

<!-- original page 456 -->

`U′ → U` such that `G_{U′}` admits a Cartan subgroup.

c) ⇒ d) is clear.

d) ⇒ e). Let `s ∈ S`. By hypothesis, there exists an `S`-prescheme `S′`, flat over `S`, whose image contains `s`, such
that `G_{S′}` admits a Cartan subgroup. Let `s′` be a point of `S′` above `s`. The nilpotent rank of the fibers of
`G_{S′}` is therefore constant on `Spec 𝒪_{S′, s′}`, and consequently the nilpotent rank of the fibers of `G` is
constant on `Spec 𝒪_{S, s}` which is the image of `Spec 𝒪_{S′, s′}` (EGA IV 2.3.4 ii)). Let `r` be its value. It follows
from 6.3 bis that the set `E_r` of points `x` of `S` such that the nilpotent rank of `G_x` equals `r` is an
ind-constructible part of `S`, hence contains a neighborhood of `s` (EGA IV 1.10.1).

e) ⇒ b). The assertion is local on `S`, so one may assume that the nilpotent rank of the fibers of `G` is constant and
equal to `r`. For every `S`-prescheme `S′` there is then identity between the Cartan subgroups of `G_{S′}` and the
subgroup preschemes of `G_{S′}` smooth over `S′` of relative dimension `r`, whose geometric fibers are centralizers of a
torus. Since `𝒞𝒯` is representable by 7.1, `𝒞` is representable by the open-closed subprescheme of `𝒞𝒯` representing the
subfunctor of `𝒞𝒯` consisting of groups of relative dimension `r`. The other assertions in b) are contained in 7.1 i),
except for the fact that the fibers of `𝒞` are affine, which itself follows from Exp. XII 7.1 d).

It is clear that b) ⇒ a). Let us show that a) ⇒ d). It follows from 6.2 iii) that the functor `𝒞`

<!-- original page 457 -->

commutes with filtered inductive limits of rings, so if `𝒞` is representable, it is necessarily representable by an
`S`-prescheme locally of finite presentation (EGA IV 8.14.2). To prove that `𝒞` is smooth over `S`, one is reduced to
showing that if `S` is affine and if `S₀` is the closed subscheme defined by a nilpotent ideal `J`, then every Cartan
subgroup `C₀` of `G₀ = G ×_S S₀` lifts to a Cartan subgroup `C` of `G`. But the existence of `C₀` entails that condition
e) is satisfied for `S₀`, hence for `S` which has the same underlying space, and one concludes from the fact that d) ⇒
b). Since `𝒞` is smooth over `S` and `𝒞 → S` is surjective, one sees that a) ⇒ d).

ii) Let `C` and `C′` be two Cartan subgroups of `G`. Then `Transp_G(C, C′)` is representable by a prescheme smooth over
`S` (7.1 iii)) with non-empty fibers (cf. Exp. XII 6.6 a) and c)). The fact that `C` and `C′` are locally conjugate for
the étale topology is then a consequence of Hensel's lemma (Exp. XI 1.10).

The other assertions of ii) are consequences of XIII 3.1 and XIII 3.2, in view of i).

iii) Let `C` be a Cartan subgroup of `G`. One knows (7.1 v)) that `u(C)` is representable by a smooth subgroup `C′` of
`G′`. Since the fibers of `C′` are Cartan subgroups of the fibers of `G′` (Exp. XII 6.6 d)), `C′` is a Cartan subgroup
of `G′`.

iv) To prove that the morphism `ũ` is faithfully flat, one proceeds as in 7.1 vi).

If now `Ker u` is central and `C′` is a Cartan subgroup of `G′`,

<!-- original page 458 -->

`u⁻¹(C′) = C` is smooth, with connected fibers (7.1 vi)) and its fibers are Cartan subgroups (Exp. XII 6.6 f)), so `C`
is a Cartan subgroup of `G`, which completes the proof of iv), in view of 7.1 vi).

## 8. Representability criterion for the functor of sub-tori of a smooth group

<!-- label: III.XV.8 -->

<!-- original page 459 -->

**8.0.** In this section, if `S` is a prescheme and `G` an `S`-prescheme in groups, `𝒯_G` (or simply `𝒯` if there is no
ambiguity) denotes the `S`-functor `(Sch/S)° → Ens` such that, for every `S`-prescheme `S′`, one has

> *`𝒯(S′)` = set of sub-tori of `G_{S′}`.*

One similarly defines `𝒯_C` as the functor of central sub-tori of `G`.

**Proposition 8.1.** *Let `S` be a locally noetherian prescheme and `G` an `S`-prescheme in groups of finite type. Then
the following conditions are equivalent:*

- *i) The functor `𝒯_G` "commutes with adic limits of local artinian rings", i.e. for every `S`-prescheme of the form
    `Spec(A) = S′`, where `A` is a complete noetherian local ring for the topology defined by its maximal ideal `𝔪`, the
    canonical map*

```text
𝒯(S′) ⟶ lim_{←n} 𝒯(S′_n)    (where S′_n = Spec(A/𝔪ⁿ))
```

*is bijective.*

- *ii) As in i) but restricted to the case where `A` is a complete discrete valuation ring with algebraically closed
    residue field.*
- *iii) As in ii), but one restricts to the subfunctor `𝒯^{(1)}` of `𝒯` relative to sub-tori of `G` of relative
    dimension `1`.*

<!-- original page 460 -->

- *i bis) For every `S`-prescheme `S′` as in i) and every `S′`-torus `T`, the canonical map*

```text
Hom_{S′-gr}(T, G_{S′}) ⟶ lim_{←n} Hom_{S′_n-gr}(T_{S′_n}, G_{S′_n})
```

*is bijective.*

- *ii bis) As i bis), but one restricts to the case where `A` is a complete discrete valuation ring with algebraically
    closed residue field.*
- *iii bis) As ii bis), but one restricts to the case where `T` is the multiplicative group `G_m`.*

<!-- label: III.XV.8.1 -->

**Remark 8.2.** One has an analogous proposition restricting to central sub-tori of `G` and to central homomorphisms of
a torus into `G`.

<!-- label: III.XV.8.2 -->

*Proof.* We shall use the following lemma:

**Lemma 8.3.** *Let `S` be a prescheme, `G` an `S`-prescheme in groups, `T` an `S`-torus, `u : T → G` an `S`-group
morphism. Assume in addition that `G` is of finite presentation over `S`, or else that `S` is locally noetherian and `G`
locally of finite type. Then:*

- *a) `Ker u` is a subgroup of multiplicative type of `T`.*
- *b) The quotient `T′ = T/Ker u` is a torus.*
- *c) The canonical monomorphism `T′ → G` deduced from `u` by passage to the quotient is an immersion.*

<!-- label: III.XV.8.3 -->

<!-- original page 461 -->

This lemma is a consequence of Exp. IX 6.8 when `G` is separated over `S`. In the general case, one reduces as usual to
the case where `S` is noetherian. Let us first show that `K = Ker u` is flat. We may assume that `S` is the spectrum of
a local artinian ring (EGA 0_III 10.2.6), in which case `G` is separated (Exp. VI_B 5.2), so `K` is of multiplicative
type (Exp. IX 6.8) and *a fortiori* flat over `S`. Let us now prove that `Ker u` is closed in `T`, which reduces us to
the case where `S` is the spectrum of a discrete valuation ring (EGA II 7.2.1). Since `T` is flat with connected fibers,
`u` factors through the connected component of the schematic closure in `G` of the generic fiber of `G`. We may
therefore assume `G` flat with connected fibers, but then `G` is separated (Exp. VI_B 5.2), so `K` is closed. This being
so, it follows from Exp. X 4.8 b) that `K` is a subgroup of multiplicative type of `T`. The quotient `T′ = T/K` is then
representable and `T′` is a group of multiplicative type (Exp. IX 2.7) whose fibers are tori, so it is a torus. The fact
that the monomorphism `T′ → G` is an immersion then follows from Exp. VIII 7.9.

*Proof of 8.1.* i) ⇒ i bis). Set `T_n = T_{S′_n}`, `G_n = G_{S′_n}`, and let `(u_n)_{n ∈ ℕ}` be an element of
`lim_{←n} Hom_{S′_n-gr}(T_n, G_n)`. For every integer `n`, `u_n(T_n)` is therefore a sub-torus `T′_n` of `G_n` (Lemma
8.3). By hypothesis, there exists a unique sub-torus `T′` of `G` lifting `T′_n` for every `n`. Since `T′` has affine
fibers, one concludes thanks to 4.4.

i bis) ⇒ i). Let `(T_n)_{n ∈ ℕ}` be an element of `lim_{←n} 𝒯(S_n)`. By Exp. X 4.6,

<!-- original page 462 -->

there exist an `S′`-torus `T⁰` and an `S′_0`-isomorphism `u_0 : T⁰_0 ⥲ T_0`. Since `T_n` is smooth over `S′_n`, `u_0`
lifts to an `S′_n`-morphism `u_n : T⁰_n → T_n` (Exp. IX 3.6), and one may assume the family `(u_n)_{n ∈ ℕ}` coherent,
hence coming from a morphism `u : T⁰ → G`. The image of `T⁰` by `u` is then a sub-torus of `G` (Lemma 8.3) lifting `T_n`
for every `n`.

The implications i) ⇒ ii) ⇒ iii) on the one hand, and i bis) ⇒ ii bis) ⇒ iii bis) on the other, are evident. The
implication iii) ⇒ iii bis) is proved as i) ⇒ i bis). It therefore suffices to prove: iii bis) ⇒ ii bis) ⇒ i bis).

ii bis) ⇒ i bis). With the terminology introduced in 4.3, assertion i bis) is true if and only if every element
`(u_n)_{n ∈ ℕ}` of `lim_{←n} Hom_{S_n-gr}(T_n, G_n)` is "admissible". For every point `t` of `S′` distinct from the
closed point `s` of `S′`, there exists an `S`-scheme `S″`, spectrum of a complete discrete valuation ring with
algebraically closed residue field, whose generic point projects to `t` and whose closed point projects to `s` (EGA II
7.1.9). One immediately deduces a valuative criterion for a family of morphisms to be admissible. This says that ii bis)
⇒ i bis).

iii bis) ⇒ ii bis). Let `T` be an `S`-torus, where `S` is the spectrum of a complete discrete valuation ring with
algebraically closed residue field. The torus `T` is then trivial (Exp. X 4.6), i.e. isomorphic to `(G_{m, S})ʳ` for a
suitable integer `r`. Let `(u_n)_{n ∈ ℕ}` be an element of `lim_{←n} Hom_{S_n-gr}((G_m)ʳ_{S_n}, G_n)`. By hypothesis,
the restrictions of `u_n` to each

<!-- original page 463 -->

factor of `(G_m)ʳ_S` come from a group morphism `G_{m, S} → G`. Whence a product morphism `(G_m)ʳ_S → Gʳ` which,
composed with the morphism `Gʳ → G` defined by the composition law in `G`, gives a morphism

```text
v : (G_m)ʳ_S ⟶ G.
```

Given the existence of the group morphism `u_n`, it is clear that `u_n = v_n`. It remains to see that `v` is a group
morphism, which translates into the fact that two obvious morphisms `f, g : X = (G_m)ʳ_S ×_S (G_m)ʳ_S → G` coincide. Let
`Z` be the subscheme of coincidences of `f` and `g`. Since `(G_m)ʳ_S` has connected fibers and `v((G_m)ʳ_S)` contains
the unit section, one sees as in 8.3 that `v` factors through the connected component of `G`, which allows us to assume
`G` separated (Exp. VI_B 5.2), so `Z` is closed. On the other hand, since `v_n` is a group morphism, one has `f_n = g_n`
for every `n`, so `Z` contains a neighborhood of the closed fiber of `X` (EGA I 10.9.4), hence is schematically dense in
`X`, `X` having smooth and irreducible fibers (Exp. IX 4.6), and consequently `Z = X`, so `f = g`.

**Definition 8.4.** *Let `S` be a locally noetherian prescheme, `G` an `S`-prescheme in groups of finite type, and `𝒮`
the set of `S`-schemes `S′`, spectrum of a complete discrete valuation ring with algebraically closed residue field, of
closed point `s`, of generic point `t`,*

<!-- original page 464 -->

*such that `(G_t)⁰_{red}` is smooth and admits a Chevalley decomposition, i.e. is an extension of an abelian variety by
a smooth, connected linear algebraic subgroup `L_t` (this decomposition is then unique). If `S′ ∈ 𝒮`, denote by `G′`
(resp. `L`) the schematic closure in `G_{S′}` of `G_t` (resp. `L_t`).*

*Under these conditions, we shall say that*

> *"the abelian part of `G` does not degenerate into a toric part", or more briefly that `G` satisfies property AT,*

*if for every `S′ ∈ 𝒮`, `Lₛ` has the same reductive rank as `G′ₛ`. (Intuitively, suppose that the quotient `A = G′/L` is
representable, in which case `A` is a flat group prescheme such that `(A_t)⁰_{red}` is an abelian variety. The condition
"AT" then means that `Aₛ` has reductive rank zero, hence `(Aₛ)⁰_{red}` is an extension of an abelian variety by a
unipotent group.)*

*Similarly, assuming in addition `G` has connected fibers, we shall say that*

> *`G` satisfies property ATC*

*if for every `S′ ∈ 𝒮`, the schematic closure `Z` of the center `Z_t` of `G_t` satisfies AT.*

<!-- label: III.XV.8.4 -->

These technical definitions are justified by the following proposition:

**Proposition 8.5.** *Let `S` be a locally noetherian prescheme, `G` an `S`-prescheme in groups of finite type. Then:*

- *a) For the functor `𝒯` of sub-tori of `G` to "commute with adic limits of local artinian rings" (cf. 8.1), it is
    necessary and sufficient that `G` satisfy property AT (8.4).*
- *b) If `G` has connected fibers, for the functor `𝒯_C` of central sub-tori of `G` to commute with adic limits of local
    artinian rings,*

<!-- original page 465 -->

*it is necessary and sufficient that `G` satisfy property ATC (8.4).*

<!-- label: III.XV.8.5 -->

We shall need the following technical lemma:

**Lemma 8.6.** *Let `S` be the spectrum of a discrete valuation ring, `s` the closed point of `S`, `G` an `S`-prescheme
in groups, flat and of finite type, `Tₛ` a sub-torus of `Gₛ`. Then there exists an `S`-scheme `S′`, spectrum of a
discrete valuation ring faithfully flat over `S`, with closed point `s′`, and a subgroup scheme `C` of `G_{S′}`, flat
over `S′`, commutative, with connected fibers, such that `Cₛ′` majorizes `Tₛ ×_s s′`.*

<!-- label: III.XV.8.6 -->

Possibly replacing `S` by `S′`, spectrum of a discrete valuation ring faithfully flat over `S`, we may assume that `Tₛ`
is equal to `(G_m)ʳₛ` and that the transcendence degree of `κ(s)` over the prime field is `⩾ r` (EGA 0_III 10.3.1 and
EGA II 7.1.9). There then exists an element `x` of `Tₛ(s)` such that every algebraic subgroup of `Gₛ` "containing" `x`
majorizes `Tₛ` (cf. Exp. XIII proof of 2.1 (ii) ⇒ (vii)). Since `G` is flat over `S`, a quasi-section passes through `x`
(EGA IV 14.5.8), and consequently, possibly replacing `S` by the spectrum of a discrete valuation ring faithfully flat
over `S`, one may assume that there exists a section `x̃` of `G` above `S` lifting `x`. Let `C_t` be the commutative
algebraic subgroup of `G_t` generated by `x̃_t` (Exp. VI_B 7), and let `C` be the schematic closure of `C_t` in `G`. It
is clear that `Cₛ` contains `x`, hence majorizes `Tₛ`, and consequently, the "connected component" of `C` will be a flat
and commutative group scheme answering the question.

*Proof of 8.5 a).* <!-- original page 466 --> Suppose the functor `𝒯` commutes with adic limits of artinian rings and
let us show that `G` satisfies property AT. Let then `S′ ∈ 𝒮`, and let `Tₛ` be a maximal torus of `G′ₛ`. We must prove
that `Tₛ` is contained in `Lₛ`. The formation of `L` and `G′` evidently commutes with faithfully flat extensions
`S″ → S′` of discrete valuation rings. Possibly changing `S′`, we may therefore, by Lemma 8.6, assume that there exists
a subgroup scheme `C` of `G′_{S′}`, flat and commutative, such that `Cₛ` majorizes `Tₛ`. But then `Tₛ` is a central
sub-torus of `Cₛ`, and consequently lifts infinitesimally to a central sub-torus (Cor. 2.3). Given the hypothesis made
on `G`, `Tₛ` lifts to a sub-torus `T` of `G`. Evidently `T_t` is contained in the linear component `L_t` of `G_t`, so
`T` is contained in `L`.

Suppose now that `G` satisfies property AT, and let us show that condition 8.1 iii bis) is verified. Let then `S` be the
spectrum of a complete discrete valuation ring `A` with algebraically closed residue field, `𝔪` the maximal ideal of
`A`, `S_n = Spec(A/𝔪ⁿ)`, `u_n`, `n ∈ ℕ`, a coherent system of group morphisms `u_n : (G_{m, S})_n → G_n = G ×_S S_n`.
Let `q` be a prime number invertible on `S`. The integer `ℓ` ranging over the powers of `q`, there exists a unique
`S`-group morphism

```text
_ℓu : _ℓ G_{m, S} ⟶ G
```

lifting `u_n|_{_ℓ(G_{m, S})_n}` for every `n` (Prop. 1.6 a)). Consequently, if there exists an `S`-group morphism
`u : G_{m, S} → T` lifting `u_n` for every `n`, its restriction to `_ℓ G_{m, S}` is uniquely determined. By the density
theorem (Exp. IX 4.8 (a)), this proves

<!-- original page 467 -->

the uniqueness of `u` and the fact that to prove the existence of `u`, we may allow a faithfully flat extension of the
base. Now `(G_t)⁰_{red}` admits a Chevalley decomposition, and this is already defined over a finite extension `L` of
the field of fractions `K` of `A`. Possibly replacing `S` by the normalization of `S` in `L`, we may therefore assume
`S ∈ 𝒮`. The morphism `_ℓu_t` factors through `(G_t)_{red}`, so `_ℓu` factors through the schematic closure `G″` of
`(G_t)_{red}` in `G′`. Still by the density theorem, one deduces that `u_n` factors through `G″_n` for every `n`. Since
`G` has property AT, every sub-torus of `G′ₛ`, and *a fortiori* of `G″ₛ`, is contained in `Lₛ`, so `uₛ` factors through
`Lₛ`. I claim that for every `n`, `u_n` factors through `L_n`. Indeed, since `L_t` is invariant in `(G″)_t`, `L` is
invariant in `G″`; on the other hand, `L` is flat over `S`, so for every integer `n`, the quotient `H_n = G″_n/L_n` is
representable (Exp. VI_A § 4). The image of `(G_{m, S})_n` in `H_n` is a sub-torus of `H_n` (Exp. IX 6.8) whose closed
fiber is zero, so this image is zero and consequently `u_n` factors through `L_n`. But since `L_t` is affine, one
deduces that the family `u_n` is admissible (Prop. 4.3), which completes the proof.

The proof of 8.5 b) is entirely analogous to that of 8.5 a), in view of 8.2 and Exp. IX 5.6 a).

**Proposition 8.7.** *Let `S` be a locally noetherian prescheme, `G` an `S`-prescheme in groups of finite type. Then:*

<!-- original page 468 -->

- *i) If `G` has connected fibers and satisfies AT, it satisfies ATC.*
- *ii) If `G` satisfies AT, every subgroup prescheme of `G` satisfies AT.*
- *iii) If `G` is flat over `S` and the abelian rank of the fibers of `G` is a locally constant function on `S`, then
    `G` satisfies AT.*

<!-- label: III.XV.8.7 -->

i) follows immediately from 8.5 and Exp. IX 5.6 a).

ii) Let `H` be a subgroup prescheme of `G`. To prove that `H` satisfies property AT, we may assume that `S` is the
spectrum of a complete discrete valuation ring and we must show that every coherent family of `S_n`-group morphisms

```text
u_n : (G_{m, S})_n ⟶ H_n
```

is admissible (8.5 and 8.1 iii bis)). Now by hypothesis, `G` satisfies property AT, so there exists an `S`-group
morphism

```text
u : (G_m)_S ⟶ G
```

lifting `u_n` for every `n`. Proceeding as in the proof of 8.5, one sees that `u|_{_ℓ G_{m, S}}` (where `ℓ` ranges over
the powers of a prime `q` invertible on `S`) factors through `H`. By density, one deduces that on the generic fiber,
`u_t` factors through `H_t`. Since `(G_m)_S` is reduced, it indeed follows that `u` factors through `H`.

iii) Let `S′ ∈ 𝒮` (notation of 8.4). <!-- original page 469 --> The group `L` is flat over `S`, its generic fiber `L_t`
is affine; under these conditions, one can show that `Lₛ` is necessarily affine (XVII App. III, 2). Since `G` and `L`
are flat, one has `G = G′` and the dimension of the fibers of `G` and `L` is constant on `S` (Exp. VI_B 4), so that one
has the inequalities:

```text
abelian rank Gₛ ⩽ dim Gₛ − dim Lₛ = dim G_t − dim L_t = abelian rank G_t.
```

The hypothesis entails that these inequalities are equalities. It follows that `(Gₛ/Lₛ)⁰_{red}` is an abelian variety,
hence has reductive rank zero, and consequently `Lₛ` has the same reductive rank as `Gₛ`.

We are now in a position to prove the main theorems of this section:

**Theorem 8.8.** *Let `G` be a group prescheme of finite type over a locally noetherian prescheme `S`. Suppose `G` flat
over `S` with connected fibers. Then:*

- *a) For the functor `𝒯_C` of central sub-tori of `G` to be representable, it is necessary and sufficient that `G` have
    property ATC (8.4). Moreover, in this case, `𝒯_C` is representable by an `S`-prescheme étale and separated over
    `S`.*
- *b) Under the conditions of a), for every `S`-torus `T`, the functor `Hom^{cent}_{S-gr}(T, G)` of central
    homomorphisms of `T` into `G` is representable by an `S`-prescheme étale and separated over `S`.*

<!-- label: III.XV.8.8 -->

**Theorem 8.9.** *Let `S` be a locally noetherian prescheme and `G` an `S`-prescheme in groups of finite type, smooth
over `S`.*

- *a) For the functor `𝒯` of sub-tori of `G` to be representable, it is necessary and sufficient*

<!-- original page 470 -->

*that `G` have property AT (8.4). Moreover, in this case, `𝒯` is representable by an `S`-prescheme smooth and separated
over `S`; more precisely, the structural morphism `𝒯 → S` admits a canonical factorization*

```text
𝒯 ──u──→ Y ──v──→ S,
```

*where `v` is a smooth and quasi-projective morphism (hence of finite type) and `u` is an étale separated morphism.*

- *b) Under the conditions of a), for every `S`-torus `T`, the functor `Hom_{S-gr}(T, G)` of homomorphisms of `T` into
    `G` is representable by an `S`-prescheme smooth and separated over `S`.*

<!-- label: III.XV.8.9 -->

*Proof of 8.8 a).* If the functor `𝒯_C` is representable, it commutes with adic limits of artinian rings, and
consequently (8.2 and 8.5 b)) `G` has property ATC. To establish the converse, we shall use the following result, which
will be proved in EGA VI, and is also found in Murre's exposé: Sém. Bourbaki, May 1965, N° 294, Theorem 1, corollary 2.

**Lemma 8.10.** *Let `S` be a locally noetherian prescheme and `F` a contravariant functor defined on `Sch/S` with
values in the category of sets. For `F` to be representable by an étale separated `S`-prescheme, it is (necessary and)
sufficient that `F` satisfy the following five properties:*

- *i) `F` is a sheaf for the fpqc topology (Exp. IV).*

<!-- original page 471 -->

- *ii) `F` commutes with inductive limits of rings (Exp. XI 3.2).*
- *iii) `F` commutes with adic limits of local artinian rings (8.1 i)).*
- *iv) `F` satisfies the "valuative criterion of separation", i.e. for every `S`-scheme `S′` which is the spectrum of a
    discrete valuation ring with generic point `t`, the canonical map `F(S′) → F(t)` is injective.*
- *v) `F` is infinitesimally étale (Exp. XI 1.8).*

<!-- label: III.XV.8.10 -->

Let us show that the functor `𝒯_C` of 8.8 satisfies the five conditions of 8.10.

i) The functor `𝒯` (resp. `𝒯_C`) is a sheaf for the fpqc topology as soon as `G` is of finite presentation over `S`.
Indeed, every monomorphism of a torus into `G` is then an immersion (Exp. VIII 7.9), and the property follows from fpqc
descent of subpreschemes.

ii) Corollary 6.3 proves that the functor `𝒯` commutes with inductive limits of rings if `G` is of finite presentation
over `S`; one immediately deduces that the same is true of `𝒯_C`.

iii) By 8.5, condition iii) is precisely equivalent to property ATC.

iv) follows simply from the fact that if `S` is the spectrum of a discrete valuation ring, two sub-tori of `G` having
the same generic fiber coincide

<!-- original page 472 -->

and more precisely coincide with the connected component of the schematic closure in `G` of their generic fiber.

v) follows from 2.3 since `G` is flat over `S`.

*Proof of 8.8 b).* Proceeding as in Exp. XI 4.2, one sees that it suffices to prove that the product group `T ×_S G`
again satisfies property ATC, which is immediate from the definition.

*Proof of 8.9 a).* Possibly replacing `G` by its connected component (Exp. VI_B 3.10), we may assume `G` has connected
fibers. If `T` is a sub-torus of `G`, its centralizer `Centr_G(T)` is then representable (Exp. XI 6.11) by a subgroup
prescheme of `G`, smooth over `S` (Exp. XI 2.4), with connected fibers (Exp. XII 6.6 b)), hence is an element of
`𝒞𝒯(S)`, where `𝒞𝒯` is the functor defined in 7.1 i). It is clear that the map

```text
T ↦ Centr_G(T)
```

defines an `S`-morphism

```text
u : 𝒯 ⟶ 𝒞𝒯.
```

Since `𝒞𝒯` is representable by an `S`-prescheme smooth and quasi-projective over `S` (7.1 i)), it suffices to prove that
the morphism `u` is representable by a separated and étale morphism.

After a suitable base change `S′ → S` (with `S′ = 𝒞𝒯`, hence `S′` locally noetherian),

<!-- original page 473 -->

we are reduced to the following problem: let `S` be a locally noetherian prescheme, `G` an `S`-prescheme in groups,
smooth and of finite type over `S`, with connected fibers, `H` a subgroup of `G`, smooth over `S` with connected fibers.
Consider the subfunctor `X` of `𝒯_{C, H}` such that, for every `S`-prescheme `S′`, `X(S′)` is the set of central
sub-tori `T` of `H_{S′}` such that `Centr_{G_{S′}}(T) = H_{S′}`. We shall show that `X` is representable by an
`S`-prescheme étale and separated over `S`.

Indeed, by hypothesis, `G` satisfies property AT, hence so does `H` (8.7 ii)); and since `H` has connected fibers, `H`
also satisfies property ATC (8.7 i)). On the other hand `H` is smooth over `S`, hence flat. By 8.8 a), `𝒯_{C, H}` is
representable by an `S`-prescheme étale and separated over `S`. It then suffices to show that the canonical monomorphism
`X → 𝒯_{C, H}` is representable by an open immersion.

Set `S′ = 𝒯_{C, H}` and let `K` be the centralizer in `G_{S′}` of the "universal" central torus of `H_{S′}`. The group
`K` is a smooth group scheme over `S′` with connected fibers, majorizing `H_{S′}`. By definition,
`X = ∏_{K/S′} H_{S′}/K`, which is indeed representable by the open-closed subprescheme of `S′` above which `H_{S′}` and
`K` have the same relative dimension.

One proves 8.9 b) analogously to 8.8 b).

**Corollary 8.11.** *Let `S` be a prescheme, `G` an `S`-prescheme in groups smooth over `S` and of finite presentation.
Then, if the abelian rank of the fibers of `G` is a locally constant function on `S` (in particular if the fibers of `G`
are affine), the functor*

<!-- original page 474 -->

*of sub-tori of `G` is representable by an `S`-prescheme, smooth and separated over `S`, and the same is true of the
functor `Hom_{S-gr}(T, G)` for every `S`-torus `T`.*

<!-- label: III.XV.8.11 -->

Indeed, the assertion is local on `S`, so we may assume `S` affine and the abelian rank of the fibers of `G` constant.
One may then find (Exp. VI_B § 10) a noetherian affine scheme `S₀` and an `S₀`-prescheme in groups `G₀`, smooth and of
finite type over `S₀`, such that `G` is `S`-isomorphic to `G₀ ×_{S₀} S`. Moreover, the abelian rank of the fibers of an
`S`-prescheme in groups of finite presentation over `S` is an ind-constructible function (6.3 bis). By a standard
argument (EGA IV 8), one concludes that in the present case, one may assume the abelian rank of the fibers of `G₀`
constant on `S₀`. But then `G₀` has property AT (8.7 iii)), and consequently (8.10) the functor of sub-tori of `G₀` is
representable by an `S₀`-prescheme smooth and separated over `S₀`, whence the announced property for `G`. As for the
functor `Hom_{S-gr}(T, G)`, one proceeds analogously.

**Generalization of 8.9.**

The functor `𝒯` of sub-tori of a smooth group `G` not being necessarily representable, we shall state sufficient
conditions for a subfunctor of `𝒯` to be representable.

**Proposition 8.12.** *Let `S` be a locally noetherian prescheme, `G` an `S`-prescheme in groups, smooth over `S`, with
connected fibers, and `F` an `S`-subfunctor of the functor `𝒯` of*

<!-- original page 475 -->

*sub-tori of `G`, satisfying the following properties:*

- *i) `F` is a sheaf for the fpqc topology (Exp. IV).*
- *ii) `F` commutes with inductive limits of rings (Exp. XI 3.2).*
- *iii) `F` commutes with adic limits of local artinian rings (Exp. XI 3.3).*
- *iv) `F` is infinitesimally smooth over `S` (Exp. XI 1.8).*
- *v) `F` is stable under inner automorphisms of `G`, i.e. for every `S`-prescheme `S′`, one has:*

```text
T ∈ F(S′) and g ∈ G(S′) ⇒ int(g)T ∈ F(S′).
```

*Then `F` is representable by an `S`-prescheme, smooth and separated over `S`.*

<!-- label: III.XV.8.12 -->

**Proposition 8.12 bis.** *Let `S` and `G` be as above, `T` an `S`-torus, and `F` a subfunctor of `Hom_{S-gr}(T, G)`,
satisfying the following properties:*

- *i), ii), iii), iv) as above.*
- *v) `F` is stable under inner automorphisms of `G`, i.e. for every `S`-prescheme `S′`, one has:*

```text
u ∈ F(S′) and g ∈ G(S′) ⇒ int(g) u ∈ F(S′).
```

*Then `F` is representable by an `S`-prescheme smooth and separated over `S`.*

<!-- label: III.XV.8.12bis -->

*Proof of 8.12.* (The proof of 8.12 bis is entirely analogous and is left to the care of the reader.)

<!-- original page 476 -->

Let `u : F → 𝒞𝒯` (7.1 i)) be the `S`-morphism which to every element `T` of `F(S′)` associates the element
`Centr_{G_{S′}}(T)` of `𝒞𝒯(S′)`. Since `𝒞𝒯` is representable by an `S`-prescheme smooth and quasi-projective (7.1 i)),
we are reduced to proving the representability of `u`. After base change `𝒞𝒯 → S`, we are reduced to the following
problem: given `S` and `G` as above, `H` a smooth subgroup of `G` with connected fibers, we must represent the functor
`F_H` such that `F_H(S′)` = set of elements `T ∈ F(S′)` such that

```text
H_{S′} = Centr_{G_{S′}}(T).
```

We shall show that `F_H` is étale and separated over `S`. To do this, it suffices to verify the five conditions of 8.10.

Conditions i), ii) and iii) of 8.10 follow easily from 8.12 i), ii) and iii). One has already remarked that `𝒯_{C, H}`
is a separated and infinitesimally étale functor, so `F_H`, which is a subfunctor of `𝒯_{C, H}`, is separated and
infinitesimally unramified (Exp. XI 1.8). It therefore suffices to show that `F_H` is infinitesimally smooth (*loc.
cit.*). Let `S` be the spectrum of a local artinian ring, `S₀` a subscheme of `S` defined by a nilpotent ideal, `T₀` an
element of `F_H(S₀)`; let us prove that `T₀` lifts to an element `T` of `F_H(S)`. By hypothesis (8.12 iv)), `T₀` lifts
to an element `T'` of `F(S)`. On the other hand, `H` being smooth, `T₀` lifts to a sub-torus `T″` of `H_S` (Exp. IX 3.6
bis), which is conjugate to `T'` by an element `g ∈ G(S)` (*loc. cit.*), so `T″ ∈ F(S)` (8.12 v)). Since
`Centr_{G_S}(T″)` is smooth over `S` and coincides with `H_{S₀}` above `S₀`, `T″` lies in the

<!-- original page 477 -->

center of `H_S` (Exp. IX 5.6 a)) and its centralizer in `G` is equal to `H_S`; in short, `T″ ∈ F_H(S)`, and one takes
`T = T″`.

**Corollary 8.13.** *Let `S` be a prescheme, `G` an `S`-prescheme in groups smooth and of finite presentation over `S`,
with connected fibers, and let `𝒯_D` be the subfunctor of `𝒯` whose set of points with values in an `S`-prescheme `S′`
is the set of sub-tori `T` of `G_{S′}` such that for every point `s′` of `S′`, `Tₛ′` is contained in the derived
subgroup (Exp. VI_B 7) of `Gₛ′`. Then `𝒯_D` is representable by an `S`-prescheme smooth and separated over `S`.*

<!-- label: III.XV.8.13 -->

**Corollary 8.13 bis.** *Let `S` and `G` be as above, `T` an `S`-torus, and let `Hom^{der}_{S-gr}(T, G)` be the
subfunctor of `Hom_{S-gr}(T, G)` whose set of points with values in `S′` is the set of `S′`-morphisms
`u : T_{S′} → G_{S′}` such that for every point `s′` of `S′`, `uₛ′` factors through the derived group of `Gₛ′`. Then
this functor is representable by an `S`-prescheme smooth and separated over `S`.*

<!-- label: III.XV.8.13bis -->

Corollary 8.13 and Corollary 8.13 bis are proved analogously; let us prove 8.13 bis for example. By the usual procedure,
we reduce to the case where `S` is noetherian. Let us verify that the five conditions of 8.12 bis are satisfied:

Conditions i) and iv) follow immediately from the corresponding properties of the functor `Hom_{S-gr}(T, G)`. Condition
v) is satisfied since the derived group of an algebraic group is invariant (Exp. VI_B § 7). To establish ii), we are
reduced by a standard reduction (EGA IV 8) to proving that if `S` is a noetherian integral scheme with generic point `η`
and `u : T → G` is an `S`-group morphism which on the generic fiber

<!-- original page 478 -->

factors through the derived group of `G_η`, then there exists a neighborhood `U` of `η` such that, for every point `s`
of `U`, `uₛ` factors through the derived group of `Gₛ`. But this follows immediately from Exp. VI_B 10.12. To establish
iii), let us resume the notation of 4.3. To show that an element `(u_m)_{m ∈ ℕ}` of
`lim_{←m} Hom^{der}_{S_m-gr}(T_m, G_m)` is "admissible", in the sense of 4.3, and comes from an element of
`Hom^{der}_{S-gr}(T, G)`, one reduces immediately to the case where `S` is the spectrum of a complete discrete valuation
ring (cf. 8.1). Let `t` be the generic point and `s` the closed point of `S`, `D` the schematic closure in `G` of the
derived group `D_t` of `G_t`.

a) `Dₛ` contains the derived group of `Gₛ`. Indeed, since `D_t` is invariant in `G_t` and `G` is flat over `S`, `D` is
invariant in `G`. Moreover the morphism

```text
G ×_S G ⟶ G,    (x, y) ↦ x y x⁻¹ y⁻¹
```

factors through `D_t` on the generic fiber, hence factors through `D`. Consequently the algebraic group `Gₛ/Dₛ` is
commutative, whence assertion a).

b) If `u_m ∈ Hom^{der}_{S_m-gr}(T_m, G_m)`, then `u_m` factors through `D_m`. Indeed, by hypothesis, `uₛ` factors
through the derived group of `Gₛ`, hence *a fortiori* factors through `Dₛ` by a). Since `D_m` is flat over `S_m` and
invariant in `G_m`, the quotient group `H_m = G_m/D_m` is representable (Exp. VI_A § 4). Since the image of `T_m` in
`H_m` is a torus (Exp. IX 6.8) whose closed fiber is zero, the image of `T_m` is zero; this says that `u_m` factors
through `D_m`.

c) The family `(u_m)_{m ∈ ℕ}` is "admissible" and lifts to a morphism `T → G` belonging to `Hom^{der}_{S-gr}(T, G)`.

<!-- original page 479 -->

By what precedes and 4.1 bis, it suffices to prove that `D_t` is an affine algebraic group, which follows from the
following lemma:

**Lemma 8.14.** *Let `G` be a smooth connected algebraic group defined over a field `k`. Then the derived group `D` of
`G` is affine.*

<!-- label: III.XV.8.14 -->

Since the formation of `D` commutes with base field extension (Exp. VI_B 7), one may assume `k` algebraically closed.
But then `G` is an extension of an abelian variety `A` by a linear group `L`. Since `A` is commutative, `D` is
necessarily contained in `L`, hence is affine.

**Maximal tori.**

**Theorem 8.15.** *Let `S` be a locally noetherian prescheme and `G` an `S`-prescheme in groups, smooth and of finite
type over `S`. Then the following conditions are equivalent:*

- *i) The `S`-functor `𝒯_M`, whose set of points with values in an `S`-prescheme `S′` is the set of maximal tori of
    `G_{S′}` (Exp. XII 1.3), is representable.*
- *ii) The preceding functor `𝒯_M` is representable by an `S`-prescheme smooth and quasi-projective over `S` with affine
    fibers.*
- *iii) The group `G` admits locally for the étale topology a maximal torus.*

<!-- original page 480 -->

- *iv) The group `G` admits locally for the faithfully flat topology a maximal torus.*
- *v) The group `G` has property AT (8.4), and the reductive rank of its fibers is a locally constant function on `S`.*

<!-- label: III.XV.8.15 -->

*Proof.* ii) ⇒ i) is clear.

i) ⇒ iii). Indeed, since `G` is of finite presentation over `S`, it follows from 6.3 that `𝒯_M` commutes with inductive
limits of rings, hence is locally of finite presentation if it is representable (EGA IV 8.14). Moreover `𝒯_M` is
formally smooth (Exp. XI 2.1 bis). So if it is representable, it is representable by a prescheme smooth over `S`, and
iii) then follows from Hensel's lemma (Exp. XI 1.10).

iii) ⇒ iv) is clear.

iv) ⇒ v). Let `s` be a point of `S`. By hypothesis, there exists an `S`-prescheme `S′`, flat over `S`, whose image
contains `s`, such that `G_{S′}` admits a maximal torus `T′`. Let `s′` be a point of `S′` above `s`. The reductive rank
of the fibers of `G_{S′}` is therefore constant on `Spec 𝒪_{S′, s′}`, and consequently the reductive rank of the fibers
of `G` is constant on the image of `Spec 𝒪_{S′, s′}`, which is `Spec 𝒪_{S, s}` (EGA IV 2.3.4 ii)). Now the reductive
rank of the fibers of `G` is a locally constructible function on `S` (6.3 bis), so this rank is constant on a
neighborhood of `s` (EGA IV 1.10.1).

To see that `G` has property AT, consider an `S`-scheme `S₁`, spectrum of a discrete valuation ring, with closed point
`s₁` projecting to the point `s`

<!-- original page 481 -->

above. The prescheme `S′₁ = S₁ ×_S S′` is faithfully flat over `S₁`, and `G_{S′₁}` admits a maximal torus. Let `A`
(resp. `A′`) be the ring of `S₁` (resp. `S′₁`). Regarding `A′` as an inductive limit of its finitely generated
`A`-subalgebras, it follows from 6.3 that there exists an `S₁`-scheme `S″₁` such that `G_{S″₁}` admits a maximal torus
and the structural morphism `S″₁ → S₁` is of finite type and surjective. Using now EGA II 7.1.9, we may assume that
`S′₁` is the spectrum of a discrete valuation ring. But then it is clear that `G_{S′₁}`, hence also `G_{S₁}`, has
property AT. Since this is true for every `S`-prescheme `S₁` spectrum of a discrete valuation ring, `G` has property AT.

v) ⇒ i). Indeed, by 8.9, the functor `𝒯` of sub-tori of `G` is representable, and it is clear that `𝒯_M` is
representable by the open-closed subprescheme of `𝒯` representing the subfunctor of tori of rank `r`, where `r` denotes
the reductive rank of `G` (which one may assume constant).

iii) ⇒ ii). Indeed, if condition iii) is realized, we may use the results of Exp. XII 7.1. The functor `𝒯_M` is
therefore canonically isomorphic to the functor of Cartan subgroups of `G`, and it suffices to apply 7.3 i).

**Remark 8.16.** One can show that the prescheme `𝒯_M` of maximal tori of `G` is affine over `S`[^XV-8-1], which
generalizes Exp. XII 5.4.

<!-- label: III.XV.8.16 -->

**Corollary 8.17.** *Let `S` be a prescheme, `G` an `S`-prescheme in groups,*

<!-- original page 482 -->

*smooth and of finite presentation over `S`. Suppose that the abelian rank and the reductive rank of the fibers of `G`
are locally constant functions on `S`; then `G` satisfies the (equivalent) properties i) to iv) of 8.15.*

<!-- label: III.XV.8.17 -->

We may assume that the abelian rank and the reductive rank of the fibers of `G` are constant. Proceeding as in 8.11, and
in view of 6.3 bis, we reduce to the case where `S` is noetherian. But then `G` has property AT (8.7), and one concludes
by 8.15 v).

**Corollary 8.18.** *Let `S` be a prescheme, `G` an `S`-prescheme in groups, smooth over `S`. Then the following
conditions are equivalent:*

- *a) The unipotent rank `ρ_u` and the abelian rank `ρ_{ab}` (6.1 ter) of the fibers of `G` are locally constant
    functions on `S`.*
- *b) The unipotent rank `ρ_u` is locally constant and `G` admits locally for the fpqc topology maximal tori.*
- *c) The reductive rank `ρ_r` (6.1 ter) and the abelian rank `ρ_{ab}` of the fibers of `G` are locally constant
    functions on `S`.*

<!-- label: III.XV.8.18 -->

**Remarks 8.19.** Under the hypotheses of 8.18, a more refined argument, using the lower semicontinuity of the abelian
rank (announced in Exp. X 8.7), shows that if two of the three ranks `ρ_u`, `ρ_r`, `ρ_{ab}` are locally constant, then
so is the third.

<!-- label: III.XV.8.19 -->

*Proof of 8.18.* Possibly replacing `G` by its connected component, we may assume `G` of finite presentation over `S`
(Exp. VI_B 5.3.3).

<!-- original page 483 -->

a) ⇒ c). Let `s` be a point of `S`. Since `ρ_{ab}` is locally constant, it follows from 8.11 that, possibly after an
étale extension covering `S`, we may assume that there exists a sub-torus `T` of `G` whose fiber `Tₛ` is a maximal torus
of `Gₛ`. Let `C = Centr_G(T)`, which is a subgroup prescheme of `G`, smooth over `S` with connected fibers. For every
point `t` of `S`, `C_t` evidently contains a Cartan subgroup `C′_t` of `G_t`. Possibly restricting `S`, we may assume
`ρ_u`, `ρ_{ab}`, and the relative dimension of `C` over `S` are constant. One then has the inequalities

```text
dim Cₛ = dim C_t ⩾ dim C′_t ⩾ ρ_u(t) + ρ_{ab}(t) + dim T_t
                            = ρ_u(s) + ρ_{ab}(s) + dim Tₛ = ρ_ν(s) = dim Cₛ.
```

One deduces that `C_t = C′_t`, hence that `T` is a maximal torus of `G`, and *a fortiori* `ρ_r(t) = ρ_r(s)`.

c) ⇒ b) by 8.17.

b) ⇒ a). Indeed, since `G` admits locally for the fpqc topology maximal tori, it admits locally for the fpqc topology
Cartan subgroups, and consequently (Exp. XII 7.3) the nilpotent rank `ρ_ν = ρ_u + ρ_r + ρ_{ab}` is locally constant.
Since `ρ_r` and `ρ_{ab}` are locally constant, `ρ_u` is locally constant.

<!-- LEDGER DELTA — Exposé XV — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| relèvement | lifting | Standard. |
| relever | to lift | Standard. |
| relevable | liftable | Standard. |
| sous-tore | sub-torus | Hyphenated; plural "sub-tori". |
| sous-tore maximal | maximal sub-torus | Standard. |
| tore maximal | maximal torus | Standard. |
| variété des tores maximaux | functor `𝒯_M` of maximal tori | Per 8.15. |
| schéma des tores maximaux | scheme of maximal tori | Per 1.10 of XII. |
| sous-groupe parabolique | parabolic subgroup | Standard. |
| sous-groupe de Borel | Borel subgroup | Standard. |
| sous-groupe de Cartan | Cartan subgroup | Standard. |
| normalisateur connexe | connected normalizer | Per 5.1. |
| transporteur | transporter | Standard. |
| transporteur strict | strict transporter | Notation `Transp^{str}`. |
| voisinage infinitésimal | infinitesimal neighborhood | Standard. |
| invariant normal | normal invariant | Per EGA IV 16.1.2. |
| rang nilpotent | nilpotent rank | `ρ_n`. |
| rang réductif | reductive rank | `ρ_r`. |
| rang unipotent | unipotent rank | `ρ_u`. |
| rang abélien | abelian rank | `ρ_{ab}`. |
| décomposition de Chevalley | Chevalley decomposition | Standard. |
| adhérence schématique | schematic closure | Standard. |
| relèvement infinitésimal | infinitesimal lifting | Standard. |
| relèvement global | global lifting | Standard. |
| de type multiplicatif | of multiplicative type | Standard. |
| central | central | Standard. |
| densément schématique | schematically dense | Per Exp. IX 4.1. |
| revêtement complètement décomposé | completely decomposed covering | Per 2.5. |
| limite adique | adic limit | Per 8.1. |
| propriété AT / ATC | property AT / ATC | Coined in 8.4; preserve as labels. |
| dégénère en une partie torique | degenerate into a toric part | Per 8.4 (quoted phrase). |
| groupe formel / complété formel | formal completion | Per 4.6. |
| algébrisable | algebraizable | Per 4.6. |
| critère valuatif | valuative criterion | Standard. |
| ind-constructible | ind-constructible | Standard. |
| localement constructible | locally constructible | Standard. |
| caractéristique résiduelle | residue characteristic | Standard. |
| Bible | *Bible* | Italicised; the Chevalley Seminar 1956/58. |
| schéma en sous-groupes | subgroup scheme | Standard. |
| sous-préschéma en groupes | subgroup prescheme | Standard. |
| « noyau » de l'élévation à la puissance nième | "kernel" of the n-th power morphism | Preserve quotes around "kernel" since the n-th power map is not a homomorphism. |
| Hom centraux | central homomorphisms | Per 8.8. |
| Hom dérivés | derived homomorphisms | Per 8.13. |
-->

[^XV-0-1]: This Exposé and the two following ones (Exp. XVI and XVII) do not correspond to oral lectures of the seminar.
    They develop, with some additional material, the substance of (succinct) manuscript notes of A. Grothendieck,
    written in 1964 on the occasion of the present seminar.

[^N.D.E-XV-1]: The idea of approximating a torus by its finite subgroups appears in Grothendieck's proof of the
    connectedness of the centralizers of tori; see § 4.6 of *Bible*.

[^N.D.E-XV-2]: cf. EGA 0_III, 12.3.5.

[^N.D.E-XV-3]: introduced after Lemma 2.7.

[^N.D.E-XV-4]: The fact that (iv) ⇒ (iii) will appear in the course of the proof.

[^N.D.E-XV-5]: We have replaced "functor" by "subfunctor". Should one rather write "which makes `σ_{q, S′}` injective
    for `q ⩽ n`"?

[^N.D.E-XV-6]: One may apply, for example, Proposition II.6.1 of the book by M. Demazure and P. Gabriel, *Groupes
    algébriques* I, Masson & North Holland (1970).

[^XV-6-1]: hypothesis in fact superfluous, cf. XVII App. III 3.

[^N.D.E-XV-7]: we have removed the word "residue".

[^N.D.E-XV-8]: details or references to be given here…

[^N.D.E-XV-9]: argument to be made explicit…

[^N.D.E-XV-10]: (Krull's)

[^XV-8-1]: cf. M. Raynaud, *Faisceaux amples sur les schémas en groupes et les espaces homogènes* (thesis, to
    appear)(N.D.E.: see Lecture Notes Math. 119 (1970), Springer), in particular IX 2.9.
