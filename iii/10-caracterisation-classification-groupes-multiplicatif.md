# Exposé X. Characterization and classification of groups of multiplicative type

<!-- label: III.X -->

*by A. Grothendieck*

> Version xy of 6 November 2009: Addenda placed in Section 9, reviewed through 8.8.[^X-0-0]

## 1. Classification of isotrivial groups. Case of a base field

<!-- original page 77 -->

Recall (IX 1.1) that the group of multiplicative type `H` over the prescheme `S` is said to be *isotrivial* if there
exists an étale, finite, surjective morphism `S′ → S` such that `H′ = H ×_S S′` is diagonalizable. When `S` is
connected, `S′` decomposes as a finite sum of connected components `S′_i`, and one can therefore (possibly by replacing
`S′` by one of the `S′_i`) assume `S′` connected. Finally, one knows that `S′` can be dominated by an `S′_1` finite,
étale and connected, which is Galois, i.e. a principal homogeneous bundle over `S` with group `Γ_S`, where `Γ` is an
ordinary finite group (cf. SGA 1, V N°s 7 & 3 when `S` is locally noetherian, and EGA IV₄, 18.2.9 in the general
case).[^N.D.E-X-1] We assume `S′` chosen in this way, and we propose to determine the groups of multiplicative type `H`
over `S` which are "trivialized" by `S′`, i.e. such that `H′ = H ×_S S′` is diagonalizable.[^N.D.E-X-2] By descent
theory (cf. SGA 1, VIII 5.4), the category of these `H` is equivalent to the category of diagonalizable groups `H′` over
`S′`, equipped with operations of `Γ` on `H′` compatible with the operations of `Γ` on `S′`. (N.B. As the groups under
consideration are affine over the base, the question of effectivity of a descent datum is answered in the affirmative,
cf. SGA 1, VIII 2.1.) Now `S′` being connected, the contravariant functor

```text
M ↦ D_{S′}(M)
```

is an anti-equivalence of the category of ordinary commutative groups with the category <!-- original page 78 --> of
diagonalizable groups over `S′` (cf. VIII 1.6), a quasi-inverse functor being
`H ↦ Hom_{S′-gr.}(H, G_{m,S′})`.[^N.D.E-X-3]

**Proposition 1.1.** *Let `S` be a connected prescheme, `S′` a connected principal cover of `S` with group `Γ` (finite).
Then the category of groups of multiplicative type over `S` split[^N.D.E-X-4] by `S′` is anti-equivalent to the category
of `Γ`-modules, i.e. of ordinary commutative groups `M` equipped with a homomorphism `Γ → Aut_{gr.}(M)`.*

<!-- label: III.X.1.1 -->

One concludes from this in a standard manner:

**Corollary 1.2.** *Let `S` be a connected prescheme, `ξ : Spec(Ω) → S` a "geometric point" of `S`, i.e. a homomorphism
into `S` of the spectrum of an algebraically closed field `Ω`; consider the fundamental group of `S` at `ξ` (cf. SGA 1
V, N° 7):*

<!-- label: III.X.1.2 -->

```text
π = π₁(S, ξ).
```

*Then the category of isotrivial groups of multiplicative type `H` over `S` is anti-equivalent to the category of
"Galois modules" under `π`, i.e. of `π`-modules `M` such that the stabilizer in `π` of every point of `M` is an open
subgroup.*

*In this correspondence, to the isotrivial group of multiplicative type `H` is associated the group
`M = Hom_{Ω-gr.}(H_ξ, G_{m,Ω})`, where `H_ξ` is the fiber of `H` at `ξ`; this group is naturally equipped with
operations of `π₁(S, ξ)`.*

**Remark 1.3.** We shall see below (cf. 5.16) that if `S` is normal, or more generally geometrically unibranch, then
every group of multiplicative type and of finite type over `S` is necessarily isotrivial, so that the classification
principle 1.2 is applicable to groups of multiplicative type and of finite type over `S`, which correspond to <!--
original page 79 --> Galois `π`-modules that are of finite type over `ℤ`. For the moment, let us confine ourselves to
the following result:

<!-- label: III.X.1.3 -->

**Proposition 1.4.** *Let `k` be a field, `H` a group of multiplicative type and of finite type over `k`; then `H` is
isotrivial, i.e. there exists a finite separable extension `k′` of `k` which splits `H`.*

<!-- label: III.X.1.4 -->

*Consequently, by 1.2, if `π` is the topological Galois group of an algebraic closure `Ω` of `k`, the category of groups
of multiplicative type and of finite type `H` over `k` is anti-equivalent to the category of Galois modules `M` under
`π` that are of finite type as `ℤ`-modules.*

It follows first from the fact that `H` is of finite type over `k` and from the "principle of the finite extension" (cf.
EGA IV₃, 9.1.4) that there exists a finite extension `k′` of `k` which splits `H`. Let us recall the principle of the
proof: by hypothesis there exist a diagonalizable group of finite type `G` over `k`, a faithfully flat `S′` over
`S = Spec(k)`, and an isomorphism of `S′`-groups `H_{S′} ≃ G_{S′}`. Possibly replacing `S′` by the residue field of a
point of `S′`, we may suppose that `S′` is the spectrum of an extension `K` of `k`. The latter is the inductive limit of
its finitely generated subalgebras `A_i`, from which it readily follows (cf. EGA IV₃, 8.8.2.4) that `u` comes from an
`A_i`-isomorphism `u_i : H_{A_i} ≃ G_{A_i}` for `i` large enough. By the Nullstellensatz, there exists a quotient ring
`k′` of `A_i` which is a finite extension of `k`. The latter therefore splits `H`.

<!-- original page 65 -->

Then `k′` is a radicial extension of a separable extension `k′_s` of `k`. By IX 5.4, the isomorphism
`u′ : H_{k′} ≃ G_{k′}` comes from an isomorphism `H_{k′_s} ≃ G_{k′_s}`, which proves that `k′_s` splits `H` and
establishes 1.4.

**Remark 1.5.** Statement 1.2 yields in particular a characterization of isotrivial tori over `S` of relative dimension
`n`: setting `π = π₁(S, ξ)`, they correspond to classes (up to "equivalence") of representations `π → GL(n, ℤ)` with
kernel an open subgroup of `π`.

<!-- label: III.X.1.5 -->

**1.6.** Even when `S` is an algebraic curve, there can exist over `S` tori (of relative dimension `2`) that are not
locally isotrivial (and *a fortiori* not isotrivial); <!-- original page 80 --> there can also exist locally trivial
tori that are not isotrivial. (Note however that such phenomena can present themselves only if `S` is not normal, as
already signalled in 1.3.) Let for example `S` be an irreducible algebraic curve (over an algebraically closed field to
fix ideas) having an ordinary double point `a`, let `S′` be its normalization, and `b` and `c` the two points of `S′`
above `a`. One then constructs a principal homogeneous bundle `P` over `S`, with structural group `ℤ`, connected, by
attaching together an infinity of copies of `S′` along the diagram

<!-- label: III.X.1.6 -->

```text
······         b            b           b            b   ······
                       c            c           c
```

(N.B. This is a principal bundle in the sense of the étale topology.) Now one has a homomorphism

```text
                                     ⎛ 1  n ⎞
φ : ℤ ⟶ GL(2, ℤ),       φ(n) =       ⎝ 0  1 ⎠,
```

which permits the construction of a torus `T` over `S`, of relative dimension `2`, from the trivial torus `G_m²` over
`P` and from the descent datum on the latter deduced from `φ`. (N.B. one will note that the projection `P → S` is
covering for the étale topology and *a fortiori* for the canonical topology of `(Sch)`, and that the descent datum under
consideration is necessarily effective, since `G²_{m,P}` is affine over `P`.) It is not difficult to prove that `T` is
not isotrivial in a neighborhood of `a`[^N.D.E-X-5] (it is however trivial on `S − {a}`).

One finds a variant of this construction by taking for `S` a curve having two irreducible components `S_1` and `S_2`
intersecting in two points `a′` and `a″`, which permits the construction of a principal homogeneous bundle `P` over `S`
with group `ℤ_S`, connected and locally trivial, hence an associated torus `T` which is locally trivial, but not
isotrivial.

## 2. Infinitesimal variations of structure

<!-- original page 81 -->

[^N.D.E-X-6] Let us begin by recalling the following result (cf. SGA 1, I 8.3 in the case `S` locally noetherian, EGA
IV₄, 18.1.2 in general):

<!-- original page 66 -->

**Recall 2.0.** *Let `S` be a prescheme, `S_0` a sub-prescheme having the same underlying set. Then the functor*

<!-- label: III.X.2.0 -->

```text
X ↦ X_0 = X ×_S S_0
```

*is an equivalence between the category of étale preschemes over `S` and the analogous category over `S_0`.*

**Proposition 2.1.** *Let `S` be a prescheme, `S_0` a sub-prescheme having the same underlying set (i.e. defined by a
nilideal `I`). Then the functor*

<!-- label: III.X.2.1 -->

```text
H ↦ H_0 = H ×_S S_0
```

*from the category of preschemes in groups of multiplicative type over `S` to the analogous category over `S_0`, is
fully faithful.*

*Moreover, it induces an equivalence between the category of quasi-isotrivial groups of multiplicative type over `S` and
the analogous category over `S_0`.*

Let us first prove the full faithfulness, i.e. that if `H`, `G` over `S` are of multiplicative type, then

```text
Hom_{S-gr.}(H, G) ⟶ Hom_{S_0-gr.}(H_0, G_0)
```

is bijective. The question being local on `S`, we may suppose `S` affine; there then exists a faithfully flat
quasi-compact morphism `S′ → S` which splits `H` and `G`. Let `S″ = S′ ×_S S′`; denote by `H′, G′` resp. `H″, G″` the
groups deduced from `H, G` by the base change `S′ → S` resp. `S″ → S`; define `S′_0` and `S″_0` similarly, the latter
being also isomorphic to `S′_0 ×_{S_0} S′_0`. One then finds a commutative diagram with exact rows:

```text
Hom_{S-gr.}(H, G)      ⟶  Hom_{S′-gr.}(H′, G′)      ⇉  Hom_{S″-gr.}(H″, G″)
        ↓ u                       ↓ u′                       ↓ u″
Hom_{S_0-gr.}(H_0, G_0) ⟶ Hom_{S′_0-gr.}(H′_0, G′_0) ⇉  Hom_{S″_0-gr.}(H″_0, G″_0),
```

so to prove that `u` is bijective, it suffices to prove that `u′` and `u″` are, which reduces us to the case where `H`
and `G` are diagonalizable, hence of the form `D_S(M)` and <!-- original page 82 --> `D_S(N)`, where `M` and `N` are
ordinary commutative groups. One will therefore have likewise `H_0 = D_{S_0}(M)`, `G_0 = D_{S_0}(N)`. One then has a
commutative diagram[^N.D.E-X-7]

```text
Hom_{S-gr.}(N_S, M_S)       ⥲  Hom_{S-gr.}(D_S(M), D_S(N))
        ↓                                  ↓
Hom_{S_0-gr.}(N_{S_0}, M_{S_0}) ⥲ Hom_{S_0-gr.}(D_{S_0}(M), D_{S_0}(N)),
```

<!-- original page 67 -->

where the horizontal arrows are isomorphisms by VIII 1.4, so we are reduced to proving that the homomorphism

```text
(×)     Hom_{S-gr.}(N_S, M_S) ⟶ Hom_{S_0-gr.}(N_{S_0}, M_{S_0})
```

is bijective, i.e. to proving that the functor `M_S ↦ M_{S_0}`, from preschemes in constant commutative groups over `S`
to preschemes in constant commutative groups over `S_0`, is fully faithful. Now `(×)` identifies also with the natural
map

```text
Hom_{gr.}(N, Γ(M_S)) ⟶ Hom_{gr.}(N, Γ(M_{S_0}))
```

deduced from `Γ(M_S) → Γ(M_{S_0})`; this latter map is obviously bijective (since `Γ(M_S)` = set of locally constant
maps from `S` to `M`, depends only on the topological space underlying `S`), whence the desired conclusion.

To prove the second assertion of 2.1, it remains to see that every group `H_0` of multiplicative type over `S_0` which
is quasi-isotrivial comes from a quasi-isotrivial group of multiplicative type `H` over `S`. To see this, let
`S′_0 → S_0` be an étale surjective morphism which splits `H_0`.

One knows (cf. 2.0) that there exists an étale morphism `S′ → S` and an `S_0`-isomorphism `S′ ×_S S_0 ≃ S′_0`, so that
one may suppose that `S′_0` comes from `S′` by reduction. Since <!-- original page 83 --> `H′_0` is diagonalizable, one
sees at once that it is isomorphic to the group deduced by base change `S′_0 → S′` from a diagonalizable group `H′` over
`S′` (N.B. if `H′_0 = D_{S′_0}(M)`, one takes `H′ = D_{S′}(M)`). Set as usual `S″ = S′ ×_S S′`, `S‴ = S′ ×_S S′ ×_S S′`,
and define `S″_0`, `S‴_0` similarly, deduced from the preceding by the base change `S_0 → S` and isomorphic also to the
fibered square resp. cube of `S′_0` over `S_0`. Using the full faithfulness already proved, in the cases `(S″, S″_0)`
and `(S‴, S‴_0)`, one sees that the natural descent datum on `H′_0` relative to `S′_0 → S_0` (cf. IV 2.1) comes from a
well-determined descent datum on `H′` relative to `S′ → S`. This descent datum is effective since `H′` is affine over
`S′` (SGA 1, VIII 2.1), so there exists an `S`-group `H` such that `H ×_S S′ = H′ = D_{S′}(M)`, and `H` is therefore of
quasi-isotrivial multiplicative type.

One then verifies easily, using now the full-faithfulness result for `(S′, S′_0)`, that the given isomorphism between
`H′_0` and `H′ ×_{S′} S′_0` comes from an isomorphism between `H_0` and `H ×_S S_0`. (For a more formal exposition of
results of this kind, see Giraud's article in preparation[^X-2-1] on descent theory.)

**Corollary 2.2.** *Let `H` be an `S`-group of multiplicative type, and `H_0 = H ×_S S_0`. For `H` to be
quasi-isotrivial (resp. locally isotrivial, resp. isotrivial, resp. locally trivial, resp. trivial), it is necessary and
sufficient that `H_0` be so.*

<!-- label: III.X.2.2 -->

The "only if" is trivial; the "if" has already been seen in the quasi-isotrivial case, since thanks to the full
faithfulness, it suffices to know that every quasi-isotrivial group over `S_0` lifts to a quasi-isotrivial group over
`S`. The same argument works for "trivial". For the case "isotrivial", one takes up the reasoning establishing the
second assertion of 2.1, but taking `S′_0 → S_0` étale surjective and finite. The cases "locally isotrivial" and
"locally trivial" follow at once from the cases "isotrivial" and "trivial".

One can generalize 2.2 somewhat when `I` is nilpotent, without supposing *a priori* `H` of multiplicative
type:[^N.D.E-X-8]

<!-- original page 84 -->

<!-- original page 68 -->

**Corollary 2.3.** *Suppose the ideal `I` defining `S_0` locally nilpotent. Let `H` be a prescheme in groups over `S`,
flat over `S`, and `H_0 = H ×_S S_0`. For `H` to be of quasi-isotrivial multiplicative type, it is necessary and
sufficient that `H_0` be so.*

<!-- label: III.X.2.3 -->

Indeed, suppose `H_0` is of quasi-isotrivial multiplicative type; let us prove that `H` is so. The question being local
for the étale topology, and the category of étale preschemes over `S` being equivalent to the category of étale
preschemes over `S_0` by the functor `S′ ↦ S′ ×_S S_0` (cf. 2.0), one is at once reduced to the case where `H_0` is
diagonalizable, hence isomorphic to a group `D_{S_0}(M)`. Let `G = D_S(M)`; one then has an isomorphism
`u_0 : H_0 ⥲ G_0`; I claim it comes from a unique homomorphism `u : H → G`, which will therefore be an isomorphism since
`u_0` is one (`H` and `G` being flat over `S`, and `I` locally nilpotent[^N.D.E-X-9]); this will establish 2.3. Now one
has (cf. VIII 1 (xxx))

```text
Hom_{S-gr.}(H, G) ≃ Hom_{S-gr.}(M_S, Hom_{S-gr.}(H, G_{m,S})),
```

and the second member identifies also with

```text
Hom_{gr.}(M, Hom_{S-gr.}(H, G_{m,S})),
```

so the homomorphism

```text
(×)     Hom_{S-gr.}(H, G) ⟶ Hom_{S_0-gr.}(H_0, G_0)
```

is isomorphic to the homomorphism

```text
Hom_{gr.}(M, Hom_{S-gr.}(H, G_{m,S})) ⟶ Hom_{gr.}(M, Hom_{S_0-gr.}(H_0, G_{m,S_0}))
```

deduced from the restriction homomorphism

```text
(××)    Hom_{S-gr.}(H, G_{m,S}) ⟶ Hom_{S_0-gr.}(H_0, G_{m,S_0});
```

<!-- original page 85 -->

so to prove that `(×)` is bijective, it suffices to prove that `(××)` is. The question is local on `S`; we may therefore
suppose `S` affine. Now `G_{m,S}` being commutative and smooth over `S`, the situation is governed by IX 3.6, which
completes the proof.

**Corollary 2.4.** *Let `A` be an artinian local ring with residue field `k`, `S = Spec(A)`, `S_0 = Spec(k)`.*

<!-- label: III.X.2.4 -->

*(i)[^N.D.E-X-10] Let `H` be an `S`-prescheme in groups, flat and locally of finite type, such that `H_0 = H ×_S S_0` is
of multiplicative type. Then `H` is of multiplicative type, of finite type and isotrivial. In particular, every
`S`-prescheme in groups `H` of multiplicative type and of finite type is isotrivial.*

*(ii) The functor `H ↦ H_0` is an equivalence between the category of groups of multiplicative type of finite type over
`A` and the analogous category over `k`.*

Indeed, let `H` be as in (i). Then `H_0` is of multiplicative type and locally of finite type, hence of finite type,
hence isotrivial by 1.4. Therefore, by 2.3 and 2.2, `H` is of multiplicative type (hence of finite type) and isotrivial.
Assertion (ii) then follows from 2.1.

**Corollary 2.5.** *Let `S′ → S` be a faithfully flat and radicial morphism.*

<!-- label: III.X.2.5 -->

*(i) The functor `H ↦ H′ = H ×_S S′`, from the category of groups of multiplicative type over `S` to the analogous
category over `S′`, is fully faithful.*

*Moreover, it induces an equivalence between the subcategories formed by the quasi-isotrivial groups of multiplicative
type.*

*(ii) If `H` is of multiplicative type, for it to be quasi-isotrivial (resp. locally isotrivial, resp. isotrivial, resp.
locally trivial, resp. trivial) it is necessary and sufficient that `H′` be so.*

Indeed, let `S″ = S′ ×_S S′` and `S‴ = S′ ×_S S′ ×_S S′`; then the hypothesis that `S′ → S` is radicial implies that the
diagonal immersions `S′ → S″` and `S′ → S‴` are surjective, so the base change by either of these immersions is governed
by 2.1 and 2.2. Taking into account that `S′ → S` is a morphism of effective descent for the fibered category of groups
of multiplicative type over preschemes (since it is faithfully flat and quasi-compact[^N.D.E-X-11]), our assertion
follows formally from 2.1 and 2.2 (cf. for a formal argument the already-cited Giraud article).

## 3. Finite variations of structure: complete base ring

<!-- original page 86 -->

**Lemma 3.1.** *Let `A` be a noetherian ring, equipped with an ideal `I` such that `A` is separated and complete for the
`I`-adic topology, `S = Spec(A)`, `S_0 = Spec(A/I)`, `G` and `H` two `S`-group schemes, with `G` of multiplicative type
and isotrivial, `H` affine over `S`, flat over `S` at the points of `H_0 = H ×_S S_0`, `H_0` of quasi-isotrivial
multiplicative type. Then the natural map*

<!-- label: III.X.3.1 -->

```text
Hom_{S-gr.}(G, H) ⟶ Hom_{S_0-gr.}(G_0, H_0)
```

*is bijective.*

For every integer `n ⩾ 0`, let `S_n = Spec(A/I^{n+1})`, and let `G_n`, `H_n` be the groups deduced from `G`, `H` by the
base change `S_n → S`. Since `G/S` is of isotrivial multiplicative type and `H` affine over `S`, then, by IX 7.1, the
natural homomorphism

```text
Hom_{S-gr.}(G, H) ⟶ lim_n Hom_{S_n-gr.}(G_n, H_n)
```

is bijective. On the other hand, by 2.3, the `H_n` are of quasi-isotrivial multiplicative type, and by 2.1, the
transition homomorphisms in the projective system `(Hom_{S_n-gr.}(G_n, H_n))_n` are isomorphisms, whence 3.1 at once.

**Theorem 3.2.** *Let `A` be a noetherian ring equipped with an ideal `I` such that `A` is separated and complete for
the `I`-adic topology, `S = Spec(A)`, `S_0 = Spec(A/I)`. Then:*

<!-- label: III.X.3.2 -->

<!-- original page 70 -->

*(i) The functor*

```text
H ↦ H_0 = H ×_S S_0
```

*is an equivalence between the category of isotrivial groups of multiplicative type over `S` and the analogous category
over `S_0`.*

<!-- original page 87 -->

*(ii) Let `H` be an `S`-group of multiplicative type and of finite type; for `H` to be isotrivial, it is necessary and
sufficient that `H_0` be so.*

*Proof.* For (i) one can either take up the proof of 2.1, or use 1.2, in either case using the fact that the functor

```text
S′ ↦ S′_0 = S′ ×_S S_0
```

from the category of finite étale schemes over `S` to the category of finite étale schemes over `S_0` is an equivalence
(SGA 1, I 8.4), which one can also state (reducing to the case `S` connected, i.e. `S_0` connected), by choosing a
geometric point `ξ` of `S_0`, by saying that the canonical homomorphism

```text
π₁(S_0, ξ) ⟶ π₁(S, ξ)
```

is an isomorphism.

Let us prove (ii), i.e. that if `H_0` is isotrivial, then `H` is so. By (i), there exists an isotrivial group of
multiplicative type `G` over `S` and an `S_0`-isomorphism

```text
u_0 : G_0 ⥲ H_0.
```

[^N.D.E-X-12] Since `H` is of finite type, so are `H_0` and `G_0`; therefore, by IX 2.1 b), the type of `G` at each
point of `S` is an abelian group of finite type, and so `G` is of finite type over `S`. On the other hand, by 3.1, `u_0`
comes from a homomorphism of `S`-groups

```text
u : G ⟶ H.
```

Finally, since `G`, `H` are of multiplicative type and of finite type over `S`, and since `u_0` is an isomorphism, then,
by IX 2.9, `u` is an isomorphism (taking into account that every neighborhood of `S_0` in `S` equals `S`).

**Corollary 3.3.** *Let `A` be a complete noetherian local ring with residue field `k`.*

<!-- label: III.X.3.3 -->

<!-- original page 88 -->

*(i) Every group of multiplicative type and of finite type over `A` is isotrivial.*

*(ii) The functor `H ↦ H ⊗_A k = H_0` is an equivalence between the categories of groups of multiplicative type and of
finite type over `A` and over `k`.*

[^N.D.E-X-12] First, (i) follows from 3.2 (ii) and 1.4; then (ii) follows from 3.2 (i), taking into account the fact
that `H` is of finite type if and only if `H_0` is (cf. the proof of 3.2 (ii)).

**Remark 3.3.1.** One will note that 3.3 yields, by 1.4, a complete classification of groups of multiplicative type and
of finite type over `A` in terms of the topological Galois group of an algebraic closure `Ω` of `k`.

<!-- label: III.X.3.3.1 -->

**Remarks 3.4.** Under the hypotheses of 3.2 (i.e. `A` noetherian, separated and complete for the `I`-adic topology, but
without further hypothesis on `A/I`), it will follow from N° 5 that the functor `H ↦ H_0`, from the category of groups
of multiplicative type and of finite type over `S` to the analogous category over `S_0`, is again fully faithful
(without hypotheses of isotriviality).[^N.D.E-X-13]

<!-- label: III.X.3.4 -->

However, it is not in general essentially surjective; in fact, there can exist an `S_0`-group `H_0` of multiplicative
type and of finite type, locally trivial if one wishes (but not isotrivial), which does not come by reduction from a
group of multiplicative type `H` over `S`.

To see this, let us take up either of the examples 1.6 of a non-isotrivial group of multiplicative type over a
non-normal curve. One may obviously take this curve affine, say `S_0`, and assume that it is embedded in the affine
space of dimension 2, hence defined by an ideal `J` in `k[X, Y]`. We shall take for `A` the completion of this ring for
the `J`-preadic topology, so that `A` is a regular ring of dimension 2, *a fortiori* normal. We shall see in 5.16 that
it follows that every group of multiplicative type and of finite type over `S = Spec(A)` is isotrivial; therefore `H_0`,
which is of finite type and not isotrivial, does not come from a group of multiplicative type `H` over `S` (since `H`
would necessarily be of finite type, hence isotrivial).

**Lemma 3.5.**[^X-3-1] *Let `S` be a prescheme, `u : G → H` a homomorphism of `S`-preschemes in groups, locally of
finite presentation and flat over `S`, `U` the set of `s ∈ S` such that the induced homomorphism on fibers
`u_s : G_s → H_s` is flat (resp. smooth, resp. unramified, resp. étale, resp. quasi-finite).*

<!-- label: III.X.3.5 -->

<!-- original page 89 -->

*Then `U` is open, and the restriction `u|U : G|U → H|U` is a flat (resp. smooth, resp. unramified, resp. étale, resp.
quasi-finite) morphism.*

Indeed, let `V` be the set of points at which `u` is flat (resp. …). One knows that `V` is open (cf. SGA 1, I to IV in
the locally noetherian case, EGA IV in general[^N.D.E-X-14]), and that for `x ∈ G` above `s ∈ S`, one has `x ∈ V` if and
only if `u_s : G_s → H_s` is flat (resp. …) at `x` (same reference; in the flat, smooth, étale cases, one uses here the
flatness of `G` and `H` over `S`). Since `u_s` is a homomorphism of locally algebraic groups, this also means that `u_s`
is flat (resp. …) everywhere (Exp. VI_B, 1.3), i.e. `s ∈ U`. Therefore `U` is the inverse image of the open set `V` by
the unit section of `G`, hence open, and `V = G|U`, so `G|U → H|U` is flat (resp. …), which completes the proof. (N.B.
In the "unramified" or "quasi-finite" case, the flatness hypothesis on `G` and `H` is unnecessary.)

**Lemma 3.6.** *Let `H` be a commutative algebraic group over a field `k`, admitting an open subgroup `G` of
multiplicative type. Then the family of subschemes `_n H` (`n > 0`) of `H` is schematically dense; in particular, if one
has `_n H = _n G` for every `n > 0`, then `H = G`.*

<!-- label: III.X.3.6 -->

Here `_n H` denotes the kernel of `n · id_H`.[^N.D.E-X-15] Let `k̄` be an algebraic closure of `k`; it suffices to show
that the family `(_n H_{k̄})_{n > 0}` is schematically dense in `H_{k̄}`, for then the family `(_n H)_{n > 0}` will be
so in `H` (cf. IX 4.5). Thus, one may suppose `k` algebraically closed, hence `G` of the form `D_k(M)`, `M` a finitely
generated ordinary commutative group.

<!-- original page 72 -->

Let `M_0 = M/Torsion(M)`; then `T = D_k(M_0)` is the largest torus contained in `G`, and `H/T` is finite, so `H(k)/T(k)`
is annihilated by an integer `ν > 0`. One can find a finite number of elements `g_i ∈ H(k)` such that

```text
H = ∐_i g_i · G,
```

and one will have `g_i^ν ∈ T(k)`. Since `k` is algebraically closed, `ν · id_T` is surjective on `T(k) ≃ k^{∗d}`, so up
to replacing the `g_i` by `g_i t_i^{−1}`, where `t_i ∈ T(k)` is such that `t_i^ν = g_i^ν`, <!-- original page 90 --> one
may suppose that `g_i^ν = 1`. If then `n` is a multiple of `ν`, one will have

```text
_n H ⊇ g_i · _n G,
```

and since (for `n > 0` variable) the family of `_n G` is schematically dense in `G` by IX 4.7, conclusion 3.6 follows.

**Theorem 3.7.** *Let `A` be a noetherian ring equipped with an ideal `I` such that `A` is separated and complete for
the `I`-adic topology, `S = Spec(A)`, `S_0 = Spec(A/I)`, and let `H` be an affine `S`-group scheme of finite type, flat
over `S` at the points of `H_0`, such that `H_0 = H ×_S S_0` is of multiplicative type and isotrivial.*

<!-- label: III.X.3.7 -->

*Then there exists an open and closed subgroup `G` of `H`, of isotrivial multiplicative type (and of finite type), such
that `G_0 = H_0`.*

By 3.2 (i), there exists an isotrivial group of multiplicative type `G` over `S` and an isomorphism

```text
u_0 : G_0 ⥲ H_0.
```

By 3.1, `u_0` comes from a unique homomorphism of `S`-groups

```text
u : G ⟶ H.
```

Using IX 6.6, one sees that `u` is a monomorphism (since if `U` is the set of `s ∈ S` such that `u_s : G_s → H_s` is a
monomorphism, then `U` is an open neighborhood of `S_0` hence identical to `S`, and `G|U → H|U` is a monomorphism). By
IX 2.5, `u` is even a closed immersion.

[^N.D.E-X-16] Therefore `G` is of finite type, hence of finite presentation over `S`. Then, by lemma 3.5 in the "étale"
case, one sees that there exists an open set `U` neighborhood of `S_0`, hence identical to `S`, such that `G|U → H|U` is
étale, so `u` is étale, hence an open immersion (since it is an étale monomorphism[^N.D.E-X-17]), which completes the
proof.

**Corollary 3.8.** *Let `A` be a noetherian ring equipped with an ideal `I` such that `A` is separated and complete for
the `I`-adic topology, `S = Spec(A)`, `S_0 = Spec(A/I)`, and let `H` be an `S`-prescheme in groups of finite type,
affine and flat over `S`.*

<!-- label: III.X.3.8 -->

<!-- original page 91 -->

*For `H` to be of multiplicative type and isotrivial, it is necessary and sufficient that `H_0` be so, and that `H`
satisfy one of the following conditions a) and b) (which are therefore equivalent given the preceding conditions):*

*a) The fibers of `H` are of multiplicative type, and of constant type on each connected component of `S`.*

*b) `H` is commutative and the `_n H` (`n > 0`) are finite over `S`.*

*These last conditions are also implied by the following:*

*c) The fibers of `H` are connected.*

Of course, if `H` is of multiplicative type (and isotrivial), conditions a) and b) are verified by IX 1.4.1 a) and 2.1
c), so only the "if" requires proof. We shall use the subgroup `G` indicated in 3.7. When condition c) is satisfied, one
obviously has `G = H` and we are done.

In case b), one notes that the immersion `u : G → H` induces an open immersion

```text
_n u : _n G ⟶ _n H
```

which induces an isomorphism `(_n G)_0 ⥲ (_n H)_0`; since `_n H` is finite over `S`, this implies at once that `_n u` is
an isomorphism (the complement of its image is finite over `S` and reduces to `∅`). By 3.6 it follows that the morphisms
induced on fibers `u_s : G_s → H_s` are isomorphisms, so `u` is surjective, hence an isomorphism.

Finally, in case a), one may assume `S` connected,[^N.D.E-X-18] and it follows that for every `s ∈ S`, `u_s : G_s → H_s`
is a monomorphism of algebraic groups of multiplicative type and of the same type over `κ(s)`.[^N.D.E-X-19] I claim that
such a homomorphism is necessarily an isomorphism (which will again complete the proof[^N.D.E-X-20]). Indeed, one may
suppose, possibly extending the base field, that the two groups over `κ(s)` are diagonalizable, and then this follows
from VIII 3.2 b) and from the fact that a surjective homomorphism of isomorphic finitely generated `ℤ`-modules `M → N`
is necessarily bijective.

**Corollary 3.9.** *Let `A` be a noetherian ring equipped with an ideal `I` such that `A` is separated and complete for
the `I`-adic topology, and let `H` be an `S`-prescheme in groups of finite type, affine and flat over `S`, with
connected fibers.*

<!-- label: III.X.3.9 -->

<!-- original page 92 -->

*For `H` to be an isotrivial torus, it is necessary and sufficient that `H_0` be so.*

## 4. Case of an arbitrary base. Quasi-isotriviality theorem

Let `A` be a local ring. Recall that one says, after Nagata, that `A` is *henselian* if every algebra `B` finite over
`A` is a product of local algebras `B_i` finite over `A`.

**Recall 4.0.**[^N.D.E-X-21] *Let `A` be a henselian local ring, `k` its residue field, `S = Spec(A)`, `S_0 = Spec(k)`,
and `ξ` a geometric point of `S_0`. Then, the functor*

<!-- label: III.X.4.0 -->

```text
X ↦ X_0 = X ×_S S_0
```

*is an equivalence between the category of étale covers of `S` and the analogous category over `S_0` (cf. EGA IV₄, §
18.5). Consequently (cf. SGA 1, V), one has `π₁(S_0, ξ) = π₁(S, ξ)`.*

Suppose moreover `A` noetherian and denote by `A′` its completion, `S′ = Spec(A′)`. Then `A′` is a complete noetherian
local ring, hence henselian (loc. cit., 18.5.14), and the functor

```text
X ↦ X′ = X ×_S S′,
```

from the category of étale covers of `S` to the analogous category over `S′`, fits into a commutative diagram

```text
                Rev.ét.(S)  ⟶  Rev.ét.(S′)
                       ↘        ↙
                      ≃   ↘   ↙  ≃
                            Rev.ét.(S_0)
```

so is also an equivalence of categories, whence `π₁(S_0, ξ) = π₁(S′, ξ)`.

**Remark 4.0.1.** Since `S` is connected (`A` being local), it follows from 1.2 that the category of isotrivial groups
of multiplicative type over `S` is equivalent to the analogous category over `S_0` (and also over `S′` if moreover `A`
is noetherian).

<!-- label: III.X.4.0.1 -->

**Lemma 4.1.** *Let `A` be a henselian local ring with residue field `k`, `S = Spec(A)`, `S_0 = Spec(k)`.*

<!-- label: III.X.4.1 -->

*(i) The functor*

```text
H ↦ H_0 = H ×_S S_0
```

*is an equivalence between the category of finite groups of multiplicative type over `S` and* <!-- original page 93 -->
*the analogous category over `S_0`.*

*(ii) If moreover `A` is noetherian, denoting by `A′` its completion and `S′ = Spec(A′)`, the functor*

```text
H ↦ H′ = H ×_S S′
```

*is an equivalence between the category of finite groups of multiplicative type over `S` and the analogous category over
`S′`.*

As in 4.0, the second assertion is a consequence of the first; let us prove the latter. One already knows that the
functor under consideration is essentially surjective, since every group of multiplicative type `H_0` over
`S_0 = Spec(k)`, finite hence of finite type over `k`, is isotrivial by 1.4, hence comes from an isotrivial group of
multiplicative type over `S` by 4.0.1.

It remains to prove full faithfulness, i.e. that for two finite groups `G`, `H` of multiplicative type over `S`, the map
below is bijective:

```text
Hom_{S-gr.}(G, H) ⟶ Hom_{S_0-gr.}(G_0, H_0),
```

i.e.,[^N.D.E-X-22] denoting by `F` the `S`-functor `Hom_{S-gr.}(G, H)`, that the natural map

```text
Hom_S(S, F) ⟶ Hom_{S_0}(S_0, F_0)
```

induced by the base change `S_0 → S` is bijective. For this, given recall 4.0, it suffices to prove:

**Lemma 4.2.** *Let `G`, `H` be two finite groups of multiplicative type over a prescheme `S`. Then
`F = Hom_{S-gr.}(G, H)` is representable by a finite étale scheme over `S`.*

<!-- label: III.X.4.2 -->

[^N.D.E-X-23] Let `f : S′ → S` be a faithfully flat quasi-compact morphism such that `G′` and `H′` are diagonalizable.
It suffices to show that `F_{S′}` is representable by a preschem `X′` étale and finite (hence affine) over `S′`, since
the descent datum on `X′` relative to `f` (cf. VIII 1.7.2) will then be effective (by SGA 1 VIII, 2.1), whence the
existence of an `S`-prescheme `X` such that `X ×_S S′ = X′`, which represents `F`, and is étale and finite over `S` (cf.
SGA 1, V 5.7 and EGA IV₄, 17.7.3 (ii)).

One may therefore suppose that `G = D_S(M)` and `H = D_S(N)`, where `M` and `N` are finite commutative groups (cf. VIII
2.1 c)). Then, <!-- original page 94 --> `K = Hom_{gr.}(N, M)` is a finite abelian group and, by VIII 1.5, one has an
isomorphism

```text
Hom_{S-gr.}(G, H) ≃ K_S,
```

which completes the proof of 4.2 and hence of 4.1.

**Proposition 4.3.0.**[^N.D.E-X-24] *Let `S` be a henselian local scheme, `s` its closed point, `g : X → S` a morphism
locally of finite type, `x` an isolated point of the fiber `X_s`.*

<!-- label: III.X.4.3.0 -->

*(i) Then `O_{X,x}` is finite over `O_{S,s}`. (In particular, if the residue extension `κ(x)/κ(s)` is trivial, then
`O_{S,s} → O_{X,x}` is surjective, by Nakayama's lemma.)*

*(ii) If moreover `g` is separated, then `X′ = Spec(O_{X,x})` is an open and closed subscheme of `X`, i.e. one has a
decomposition as a disjoint sum `X = X′ ⊔ X″`.*

*Proof.* By the local form of Zariski's main theorem given in [Pes66], or [Ray70, Ch. IV, Th. 1], `x` has an affine open
neighborhood `U = Spec(B)` of finite type and quasi-finite over `A = O_{S,s}`, and there exists an open immersion
`U ↪ Y = Spec(C)`, where `C` is a finite `A`-algebra. (N.B. to reach this conclusion, one may also use Chevalley's
semi-continuity theorem (EGA IV₃, 13.1.4), then the form of Zariski's main theorem given in loc. cit., 8.12.8.)

Since `A` is henselian, `Y` is the disjoint sum of local schemes `Y_1, …, Y_n`, each finite over `S`, and the points of
`Y` above `s` are the closed points `y_1, …, y_n`. Therefore `x = y_i` for some `i`, and `O_{X,x} = O_{U,x} = C_i` is
finite over `A`. Moreover, `X′ = C_i` is an open subscheme of `U` hence of `X`.

Suppose moreover `g` separated. Then, since the morphism `X′ → S` is finite (`C_i` being finite over `A`), so is the
immersion `X′ → X` (cf. EGA II, 6.1.5 (v)), so `X′` is also closed in `X`.

**Lemma 4.3.** *Let `A` be a noetherian henselian local ring, `A′` its completion, `S = Spec(A)`, `S′ = Spec(A′)`, `s`
the closed point of `S`, `G` and `H` two `S`-preschemes in groups, with `G` of multiplicative type and of finite type
over `S`, `H` locally of finite type and separated over `S`, `H_s` of multiplicative type, and `H` flat over `S` at the
points of `H_s`.*

<!-- label: III.X.4.3 -->

*Let `G′`, `H′` be deduced from `G`, `H` by the base change `S′ → S`. Then the natural map below is bijective:*

```text
Hom_{S-gr.}(G, H) ⥲ Hom_{S′-gr.}(G′, H′).
```

Since `S′` is faithfully flat and quasi-compact over `S`, one knows by SGA 1, VIII 5.2 that this map is a bijection of
the first member onto the part of the second formed by the `u′ : G′ → H′` such that the two inverse images `u″_1`,
`u″_2 : G″ → H″` of `u′` on `S″ = S′ ×_S S′` (by the projections `pr_1`, `pr_2` of `S″` onto `S′`) are equal.

Therefore everything reduces to proving that for every homomorphism of `S′`-groups `u′ : G′ → H′`, one has
`u″_1 = u″_2`. By the density theorem IX 4.8 it suffices to prove that `u″_1` and `u″_2` coincide on `_n G″` for every
integer `n > 0`. (N.B. one needs here in an essential way the density theorem in a case where the base prescheme, here
`S″`, is not locally noetherian.)

This reduces us, replacing `G` by `_n G`, to the case where there exists an integer `n > 0` such that `n · id_G = 0`,
hence where `G` is finite over `S`. Let likewise `_n H` be the kernel of the `n`-th power morphism `φ_n` in `H`. (N.B.
we have not assumed `H` commutative, so `φ_n` (resp. `_n H`) is not necessarily a homomorphism of groups (resp. a
subgroup of `H`).) Since `_n H` is defined as the fibered product of `φ_n : H → H` <!-- original page 95 --> and the
unit section `ε : S → H`, its formation commutes with every base change `T → S`, i.e. one has `(_n H)_T = _n (H_T)`.

[^N.D.E-X-25] We denote by an index `m` on the right the reductions modulo `m^{m+1}`, where `m` is the maximal ideal of
`A`. Then `H_m` is flat over `S_m` (since `H` is so over `S` at the points of `H_0`); therefore, by 2.4, since `H_0` is
of multiplicative type and of finite type, so is `H_m`. Therefore each `(_n H)_m = _n (H_m)` is a subgroup of `H_m`, of
multiplicative type, finite and flat over `S_m`.

In particular, `(_n H)_0 = _n (H_0)` is finite over `S_0`; since `S` is henselian local and `_n H` is (like `H`) locally
of finite type and separated over `S`, then, by 4.3.0, <!-- original page 77 --> the local rings of `_n H` at the points
of `(_n H)_0` are finite over `S` and one has a decomposition as a disjoint sum of open sets

```text
(∗)    _n H = _n H⁺ ⊔ _n H⁻,
```

where `Z = _n H⁺` is finite over `S`, and `_n H⁻` lies above `S − {s}`.

Note that, for every finite `S`-scheme `Y` (such as `G`), every `S`-morphism `Y → _n H` factors through `Z`, and that
the formation of the decomposition `(∗)` commutes with the base change `S′ → S` (where `S′ = Spec(A′)`, `A′` the
completion of `A`).

Then `Z′ = Z ×_S S′` is a finite scheme over `S′`, as is `P′ = Z′ ×_{S′} Z′`. Denote by `ν` the restriction to `P′` of
the multiplication of `H′` and by `σ` the automorphism of `P′` which exchanges the two factors. Since `P′` is finite
over `S′` and `H′` separated and locally of finite type over `S′`, then, by EGA II 5.4.3 and IV₁ 1.1.3, `Y = ν(P′)` is a
closed subscheme of `H′`, universally closed and quasi-compact, hence of finite type, hence proper over `S′`. Moreover,
`Y → S′` has finite fibers (since `P′ → S′` does). Therefore, since `S′` is noetherian, the morphism `Y → S′` is finite
(cf. EGA III, 4.4.2). Since `Z′ ⊆ Y` and `Z′_m = Y′_m` for every `m`, then `Z′ = Y`, by lemma IX 5.0, so `Z′` is a
subgroup of `H′`. Likewise, the kernel `K = Ker(ν, ν ∘ σ)` is a closed subscheme of `P′`, such that `K_m = P′_m` for
every `m` (since `Z′_m = _n H_m` is commutative), so `K = P′`, i.e. `Z′` is a commutative subgroup of `H′`.

On the other hand, since each reduction `Z′_m = _n H_m` is flat over `S_m`, then, by the "local criterion of flatness"
(cf. EGA 0_III, 10.2.2 or [BAC], III § 5, Example 1 and Th. 1), `Z′` is flat over `S′`. Since moreover `Z′_0 = _n H_0`
is a finite group of multiplicative type over `S_0`, hence isotrivial by 1.4, then `Z′` is of multiplicative type (and
isotrivial) over `S′`, by 3.8 b). Since `S′ → S` is faithfully flat and quasi-compact, one deduces that the
multiplication `Z ×_S Z → H` factors through `Z` and makes `Z` a subgroup of `H`, finite over `S` and of multiplicative
type (since `Z′` is).

Finally, by the remarks made above on decomposition `(∗)`, `Z′` is the "finite part" of `_n H′`, and so the morphism
`u′ : G′ → _n H′` takes its values in `Z′`. Since `Z` is of multiplicative type and finite over `S`, as is `G = _n G`,
then, by 4.1, `u′` comes from a `u : G → Z`, and therefore `u″_1 = u″_2`. This completes the proof of 4.3.

**Lemma 4.4.0.**[^N.D.E-X-26] *Let `A` be a ring, `S = Spec(A)`, `H` an `S`-group scheme of multiplicative type and of
finite type, quasi-isotrivial (resp. isotrivial), `(A_i)` a filtered family of subrings of `A` of which `A` is the
inductive limit, `S_i = Spec(A_i)`.*

<!-- label: III.X.4.4.0 -->

*Then there exist an index `i` and an `S_i`-group scheme `H_i` of multiplicative type and of finite type,
quasi-isotrivial (resp. isotrivial), such that `H = H_i ×_{S_i} S`.*

**Theorem 4.4.** *Let `S` be a prescheme, `H` an `S`-prescheme in groups affine and of finite presentation over `S`, and
`s ∈ S`. Assume:*

<!-- label: III.X.4.4 -->

*α) `H` is flat over `S` at the points of `H_s`.*

*β) `H_s` is of multiplicative type.*

*Then there exist an étale morphism `S′ → S`, a point `s′` of `S′` above `s` such that the extension `κ(s′)/κ(s)` is
trivial, and an open and closed subgroup `G′` of `H′ = H ×_S S′`,* <!-- original page 96 --> *of multiplicative type and
of finite type, isotrivial, such that `G′_{s′} = H′_{s′}`.*

[^N.D.E-X-27] **a)** Let us provisionally denote `T = Spec(O_{S,s})` and show that, by "descent of conclusions", one can
reduce to the case where `S = T`. Indeed, suppose we have found an étale morphism `g : T′ → T`, a point `s′ ∈ T′` and a
subgroup `G′` of `H′ = H_{T′}` satisfying the conditions of the statement; replacing `T′` by an affine open neighborhood
of `s′`, one may suppose `T′` of finite presentation over `T`.

Since `G′` is isotrivial, there exists an étale finite surjective morphism `f : T̃ → T′` such that `G̃ = G′ ×_{T′} T̃`
is isomorphic to `D_{T̃}(M)`, where `M` is a finitely generated abelian group. Since `T′`, `H`, and `T̃`, `G′` are of
finite presentation over `T = Spec(O_{S,s})`, and `O_{S,s}` is the inductive limit of the subalgebras `A_i = O_S(S_i)`,
where `S_i` runs through the affine open neighborhoods of `s` in `S`, then, by EGA IV₃, 8.8.2 (and Exp. VI_B, 10.2 and
10.3), there exist an index `i`, `S_i`-preschemes (resp. an `S_i`-prescheme in groups) of finite presentation `S′_i` and
`T̃_i` (resp. `G′_i`), and morphisms `g_i : S′_i → S_i` and `f_i : T̃_i → S′_i` (resp. a morphism of `S_i`-preschemes in
groups `u_i : G′_i → H ×_S S′_i`), from which `f` and `g` (resp. `u : G′ → H′`) come by the base change `T′ → S_i`.
Moreover, taking `i` large enough, `g_i` will be étale, `f_i` étale finite surjective, and `u_i` an open and closed
immersion (cf. EGA IV, 8.10.5 and 17.7.8).

Then, `G̃` comes from the groups `G̃_i = G_i ×_{S_i} T̃_i` and `D_{T̃_i}(M)`; therefore, by EGA IV₃, 8.8.2 (i) (and
VI_B, 10.2), there exists an index `j ⩾ i` such that `G̃_j ≃ D_{T̃_j}(M)`, so `G_j` is of isotrivial multiplicative
type. Denote by `s′_j` the image of `s′` in `S′_j`. Then the étale morphism `S′_j → S_j ↪ S`, the point `s′_j` and the
open and closed subgroup `G′_j` of `H ×_S S′_j`, verify the conditions of the statement. This shows that one may suppose
`S = Spec(A)` local, with closed point `s`.

**b)** Then, `A` is the inductive limit of local rings `A_i` which are localizations of `ℤ`-algebras of finite type;
denote `S_i = Spec(A_i)`. Let us show that the hypotheses α) and β) "descend" to some `A_i`. Since `H → S` is of finite
presentation, the set of `x ∈ H` such that `H` is flat over `S` at `x` is an open set `W`, which contains `H_s` by
hypothesis, hence contains a quasi-compact open set `V` containing `H_s` (since `H_s` being affine, one can cover it by
a finite number of affine open sets contained in `W`). Then the open immersion `τ : V ↪ H` is of finite presentation, so
`V → S` is too.

Therefore, by EGA IV₃, 8.8.2 (and Exp. VI_B, 10.2 and 10.3), there exist an index `i`, an `S_i`-prescheme `V_i` (resp.
an `S_i`-prescheme in groups `H_i`) of finite presentation over `S_i`, and an `S_i`-morphism `τ_i : V_i → H_i` from
which `V`, `H` and `τ` come by base change `S → S_i`; moreover, taking `i` large enough, `τ_i` will be an open immersion
and `V_i` will be flat over `S_i`, by EGA IV₃, 8.10.5 and 11.2.6. Denote by `s_i` the image of `s` in `S_i`; since the
open immersion `(V_i)_{s_i} ↪ (H_i)_{s_i}` gives, by the base change `κ(s_i) → κ(s)`, the equality `V_s = H_s`, one
already has `(V_i)_{s_i} = (H_i)_{s_i}`, i.e. `(H_i)_{s_i} ⊆ V_i`, so `H_i` is flat over `S_i` at the points of
`(H_i)_{s_i}`. Finally, `(H_i)_{s_i}` is of multiplicative type, since `H_s = (H_i)_{s_i} ⊗_{κ(s_i)} κ(s)` is. Therefore
the triple `(S_i, H_i, s_i)` verifies the hypotheses of 4.4, and if the desired assertion is verified for this triple,
it will also be verified, by base change, for `(S, H, s)`. This reduces us to the case where `A` is local and
noetherian. Let us now distinguish two cases.

**1°)** `A` *is local noetherian and henselian.* <!-- original page 79 --> Let `Â` be its completion, `Ŝ = Spec(Â)`, and
`Ĥ = H ×_S Ŝ`. Applying theorem 3.7, one finds an `Ŝ`-group `Ĝ` of multiplicative type, isotrivial and of finite type,
and a homomorphism of `Ŝ`-groups

```text
û : Ĝ ⟶ Ĥ
```

which is an open immersion and a closed immersion, such that `û` induces an isomorphism `û_0 : Ĝ_0 ⥲ Ĥ_0`.

By remark 4.0.1, the base change functor by `Ŝ → S` induces an equivalence between the category of isotrivial groups of
multiplicative type over `S`, and over `Ŝ`; in particular `Ĝ` "comes from" an `S`-group of multiplicative type `G`,
isotrivial and of finite type. By 4.3, `û` comes from a homomorphism

```text
u : G ⟶ H;
```

moreover `u` is an open and closed immersion and induces an isomorphism `u_0 : G_0 → H_0`, since this is so after the
faithfully flat quasi-compact base change `Ŝ → S`. This therefore proves 4.4 in this case (taking of course, in the
conclusion of 4.4, `S′ = S` and `s′ = s`).

**2°)** `A` *is local noetherian.* The reduction to case 1°) is immediate, by applying 1°) to the "henselized" ring
`A^h` of `A`. More precisely, one sees easily (using SGA 1, I § 5[^X-4-1]) that the local rings `O_{S′,s′}` of the
`S`-preschemes étale `S′` equipped with a point `s′` above `s` such that `κ(s′)/κ(s)` is trivial, form a filtered
inductive system, whose inductive limit is a noetherian henselian local ring `A^h` (called the "henselized" ring of
`A`); for details of this construction (due to Nagata in the normal case), cf. SGA 4, VIII § 4[^X-4-1]. The sorites of
EGA IV₃ § 8 then allow, <!-- original page 97 --> as in part a) of the proof, to deduce from a known result on the
inductive limit `A^h` of the `O_{S′,s′}`, an analogous result on one of the `(S′, s′)`, which proves 4.4.

**Corollary 4.5.** *Let `S` be a prescheme, `H` an `S`-prescheme in groups of multiplicative type and of finite type.
Then `H` is quasi-isotrivial, i.e. is split by an étale surjective morphism `S′ → S`.*

<!-- label: III.X.4.5 -->

Indeed, let `s ∈ S`. By 4.4, there exist an étale morphism `S′ → S`, an `s′ ∈ S′` above `s` such that `κ(s) = κ(s′)`,
and a subgroup `G′` of `H′`, of isotrivial multiplicative type and of finite type, such that `G′_{s′} = H′_{s′}`. Since
`G′` and `H′` are of multiplicative type and of finite type, then, by IX 2.9, there exists an open neighborhood `U′` of
`s′` such that `G′|U′ = H′|U′`.

[^N.D.E-X-28] Suppose moreover `S` local henselian, with closed point `s`; then, by EGA IV₄, 18.5.11 b), there exists a
section `σ` of `S′ → S` such that `σ(s) = s′`. (N.B. one can see directly that `B = O_{S′,s′}` equals `A = O_{S,s}` as
follows: by 4.3.0 (i), one has `B ≃ A/I`, and since `B` is a finitely presented and flat `A`-algebra, `I` is a finitely
generated ideal <!-- original page 80 --> (cf. EGA IV₁, 1.4.7), and `I = I m` (where `m` is the maximal ideal of `A`),
whence `I = 0`.) Therefore `H` is already isotrivial. One thus obtains:

**Corollary 4.6.** *Let `A` be a henselian local ring, `k` its residue field, and `π` the topological Galois group of an
algebraic closure of `k`.*

<!-- label: III.X.4.6 -->

*(i) Every group of multiplicative type and of finite type over `S = Spec(A)` is isotrivial.*

*(ii) The category of these groups over `S` is equivalent (via the functor `H ↦ H ⊗_A k`) to the analogous category over
`S_0 = Spec(k)`; it is therefore anti-equivalent, by 1.4, to the category of Galois modules under `π` which are of
finite type as `ℤ`-modules.*

**Corollary 4.7.** *Under the conditions of 4.4 suppose moreover that one of the following conditions is verified:*

<!-- label: III.X.4.7 -->

*a) For every generization `t` of `s`, `H_t` is of multiplicative type and of the same type as `H_s`.*

*b) `H` is commutative and the `_n H` (`n > 0`) are finite over `S` in a neighborhood of `s`.*

*c) For every generization `t` of `s`, the fiber `H_t` is connected.*

*Then there exists an open neighborhood `U` of `s` such that `H|U` is of multiplicative type.*

<!-- original page 98 -->

Taking into account that an étale morphism is open, one is reduced to proving that there exists (with the notations of
the conclusion of 4.4) an open neighborhood `U′` of `s′` such that `G′|U′ = H′|U′`. Set `S″ = Spec(O_{S′,s′})`; since
`G′` and `H′` are of finite presentation over `S′`, it suffices to show, by EGA IV₃, 8.8.2, that `G″ = H″`. We may
therefore suppose `S = S″`, and then hypotheses (a), (b), (c) become those of the lemma below, whose proof is the same
as that of 3.8:

**Lemma 4.7.1.** *Let `S` be a local scheme, `s` its closed point, `H` an `S`-group scheme of finite type, `G` an open
and closed subgroup of `H`, of multiplicative type, such that `G_s = H_s`. Suppose moreover one of the following
conditions verified:*

<!-- label: III.X.4.7.1 -->

*a) The fibers of `H` are of multiplicative type and of the same type as `H_s`.*

*b) `H` is commutative and the `_n H` (`n > 0`) are finite over `S`.*

*c) The fibers of `H` are connected.*

*Then `G = H`.*

**Corollary 4.8.** *Let `S` be a prescheme, `H` an `S`-prescheme in groups affine, flat and of finite presentation over
`S`, with fibers of multiplicative type.*

<!-- label: III.X.4.8 -->

*For `H` to be of multiplicative type, it is necessary and sufficient that it satisfy one of the two following
conditions (equivalent given the preceding conditions):*

*a) The type of `H_s` (cf. IX 1.4) is a locally constant function of `s ∈ S`.*

*b) `H` is commutative, and the `_n H` (`n > 0`) are finite over `S`.*

*Moreover, these conditions a), b) are implied by the following:*

*c) The fibers of `H` are connected.*

In particular, one finds:

**Corollary 4.9.** *Let `S` be a prescheme, `H` an `S`-prescheme in groups flat and of finite presentation over `S`.
Suppose moreover `H` affine over `S` and with connected fibers.[^N.D.E-X-29] If `s ∈ S` is such that `H_s` is a torus,
there exists an open neighborhood `U` of `s` such that `H|U` is a torus.*

<!-- label: III.X.4.9 -->

<!-- original page 81 -->

*In particular, if all the fibers of `H` are tori, `H` is a torus.*

## 5. Scheme of homomorphisms from one group of multiplicative type to another. Twisted constant groups and groups of multiplicative type

**Definition 5.1.** *a) Let `S` be a prescheme, `R` a prescheme in groups over `S`. One says that `R` is a* twisted
constant group *over `S` if it is locally isomorphic, in the sense of the faithfully flat quasi-compact topology, to a
constant group scheme, i.e. of the form `M_S` with `M` an ordinary group.*

<!-- label: III.X.5.1 -->

<!-- original page 99 -->

*b) One says that the twisted constant group `R` over `S` is* quasi-isotrivial, resp. isotrivial, resp. locally
isotrivial, resp. locally trivial, resp. trivial, *if in the definition above one can replace the faithfully flat
quasi-compact topology by the étale topology, resp. the global finite étale topology, resp. the finite étale topology,
resp. the Zariski topology, resp. the coarsest (or "chaotic") topology, cf. IX 1.1 and 1.2, and IV 6.6.*

*To say that `R` is quasi-isotrivial (resp. isotrivial) thus means that there exists an étale surjective (resp. and
finite) morphism `S′ → S` such that `R′ = R ×_S S′` is a constant group over `S`; to say that it is trivial means that
`R` is a constant group.*

*c) One defines as in VIII 1.4 the* type *of a twisted constant group `R` over `S` at an `s ∈ S`; it is a class of
ordinary groups up to isomorphism, which for variable `s` is a locally constant function of `s`, hence constant if `S`
is connected. One will also say that `R` is "of type `M`" if all the fibers of `R` are of type `M`.*

*Beware that `R` is quasi-compact over `S` only if it is finite over `S`, i.e. if its type at every `s ∈ S` is a finite
group.*[^N.D.E-X-30]

*d) The case most interesting for us is that where `R` is commutative. We shall then say that `R` is "*finitely
generated*" if its type at each point `s ∈ S` is given by a finitely generated `ℤ`-module, a notion which should not be
confused with the schematic notion "`R` of finite type over `S`" (cf. above).*

**Remark 5.2.** We shall also have to consider `S`-preschemes `X` which are locally isomorphic (for the faithfully flat
quasi-compact topology) to constant preschemes, independently of any group structure. We shall then say that `X` is a
*twisted constant bundle* over `S`, and we extend to these preschemes the terminology introduced in 5.1. Of course one
will note that when `X` is endowed with an `S`-group structure, the meaning of the expressions "twisted constant",
"isotrivial" etc. changes, depending on whether one takes into account or not the group structure over `S`. The same
holds if one considers <!-- original page 100 --> on `X` any other species of algebraic structure (for example that of
Galois principal bundle that will be considered in the following number).

<!-- label: III.X.5.2 -->

**Proposition 5.3.** *Let `R` be a commutative twisted constant group over `S`.*

<!-- label: III.X.5.3 -->

*(i) The functor `H = D_S(R)` (cf. VIII 1) is representable and is a group of multiplicative type over `S`.*

*(ii) For every `s ∈ S`, the type of `R` at `s` equals that of `H` at `s`.*

*(iii) For `R` to be quasi-isotrivial (resp. isotrivial, resp. trivial, resp. locally isotrivial, resp. locally
trivial), it is necessary and sufficient that `H` be so.*

**Remark 5.3.1.**[^N.D.E-X-31] One may worry about seeing in 5.3 the term "type" used in two different senses depending
on whether we speak of `R` or `H`; fortunately, when an `S`-prescheme in groups `G` is at the same time a twisted
constant group and of multiplicative type, its type in either sense is the same, thanks to the fact that a finite
ordinary commutative group is isomorphic to its dual!

<!-- label: III.X.5.3.1 -->

*Proof.* Since the families covering for the faithfully flat quasi-compact topology are families of effective descent
for the fibered category of affine preschemes in groups over variable base preschemes (SGA 1, VIII 2.1), one sees that
`H` is representable (and is affine over `S`), since it is so "locally"[^N.D.E-X-32] (because it is so when `R` is
constant, and then `H` is a diagonalizable group).

The fact that `H` is of multiplicative type is then evident by definition, as is the fact that the type of `R` and `H`
at `s ∈ S` is the same. Finally, since `H_{S′} = D_{S′}(R_{S′})`, the last assertion is reduced to the "trivial" case,
i.e. to verifying that `R` is trivial if and only if `H` is, which follows at once from the biduality theorem VIII 1.2.

To finish making precise the correspondence between twisted constant groups and groups of multiplicative type, one must
start from a group of multiplicative type `H`, and study `R = D_S(H)`. If the latter is representable, it is obviously a
twisted constant group, and one will have `H ≃ D_S(R)`. In other words:

**Scholie 5.4.0.** *The functor `R ↦ D_S(R)` is an anti-equivalence[^N.D.E-X-33] between the category of twisted
constant groups over `S` and that of groups of multiplicative type `H` over `S` such that `D_S(H)` is representable.*

<!-- label: III.X.5.4.0 -->

<!-- original page 101 -->

I do not know whether this condition on `H` is always satisfied; we shall see however that it is satisfied when `H` is
quasi-isotrivial, in particular when `H` is of finite type.

**Lemma 5.4.** *Let `S′ → S` be a faithfully flat morphism locally of finite presentation, `X′` an `S′`-prescheme
separated, locally of finite presentation and locally quasi-finite over `S′`.*

<!-- label: III.X.5.4 -->

*Then every descent datum on `X′` relative to `S′ → S` is effective, i.e. there exists an `S`-prescheme `X`, and an
`S′`-isomorphism `X ×_S S′ ≃ X′` compatible with the descent datum.*

We have already noted that the hypothesis on `S′ → S` implies that it is a morphism covering for the faithfully flat
quasi-compact topology (IV 6.3.1 (iv)), *a fortiori* a morphism of effective descent.

When `X′ → S′` is quasi-compact, hence of finite presentation and quasi-finite, then it is a quasi-affine morphism (cf.
SGA 1, VIII 6.2[^N.D.E-X-34]), and effectivity follows in this case from SGA 1, VIII 7.9. In the general case, one
reduces at once to the case where `S` and `S′` are affine. One covers `X′` by affine open sets `U′_i`; let `V′_i` be the
saturation of `U′_i` for the equivalence relation in `X′` defined by the descent datum, i.e.
`V′_i = q_2(q_1^{−1}(U′_i))`, where `q_1`, `q_2` are the two projections of `X″_1 = X′ ×_{S′} (S″, p_1)` onto `X′`
(`q_1 = pr_1`, and `q_2` is deduced from the first projection of `X″_2 = X′ ×_{S′} (S″, p_2)` thanks to the given
descent isomorphism `X″_1 ≃ X″_2`). Since `S′ → S` is faithfully flat quasi-compact locally of finite presentation, the
same holds for `p_1 : S″ = S′ ×_S S′ → S′`, hence also for `q_1` and `q_2`, which are consequently open morphisms (SGA 1
IV 6.6[^N.D.E-X-35]). Consequently, `V′_i` is an open and quasi-compact part of `X′`. By what we have already seen, the
descent data induced on the `V′_i` are effective, whence it follows that the descent datum on `X′` is so (SGA 1, VIII
7.2).

**Corollary 5.5.** *A faithfully flat morphism of finite presentation `S′ → S` is a morphism of effective descent for
the fibered category of twisted constant groups (over variable base preschemes).*

<!-- label: III.X.5.5 -->

<!-- original page 102 -->

Indeed, this amounts to asserting the effectivity of a descent datum under the conditions of 5.4, when `X′` is a
constant `S′`-prescheme.

**Theorem 5.6.** *Let `S` be a prescheme, `G` and `H` two `S`-preschemes in groups of quasi-isotrivial multiplicative
type, with `G`[^N.D.E-X-36] of finite type.*

<!-- label: III.X.5.6 -->

*Then `Hom_{S-gr.}(H, G)` is representable by, and is a quasi-isotrivial twisted constant group over `S`;*[^N.D.E-X-37]
*for every `s ∈ S`, if the type at `s` of `G` (resp. `H`) is `M` (resp. `N`), that of `Hom_{S-gr.}(H, G)` is
`Hom_{gr.}(M, N)`.*

One proceeds as in 4.2, using the fact that the assertion is established (VIII 1.5) when `G` and `H` are trivial. The
necessary effectivity criterion is furnished by 5.5 (in the case of an étale surjective morphism `S′ → S`).

In particular, taking `G = G_{m,S}`, one finds:

**Corollary 5.7.** *(i) Let `H` be a quasi-isotrivial `S`-group of multiplicative type; then the `S`-group `D_S(H)` is
representable and is a quasi-isotrivial twisted constant group over `S`.*

<!-- label: III.X.5.7 -->

*(ii) The functors `R ↦ D_S(R)` and `H ↦ D_S(H)` are anti-equivalences, quasi-inverse to one another, between the
category of quasi-isotrivial twisted constant `S`-groups and that of quasi-isotrivial `S`-groups of multiplicative
type.*

*(iii) These functors induce anti-equivalences between the subcategories formed by the isotrivial, resp. locally
isotrivial, resp. locally trivial, resp. trivial groups.*

The last assertion is included only for the record, being already contained in 5.3.

Moreover, since every `S`-group of multiplicative type and of finite type is quasi-isotrivial by 4.5, one deduces from
5.6:

**Corollary 5.8.** *Let `S` be a prescheme, `G` and `H` two `S`-preschemes in groups of multiplicative type and of
finite type. Then `Hom_{S-gr.}(H, G)` is representable and is a finitely generated quasi-isotrivial twisted constant
`S`-group.*

<!-- label: III.X.5.8 -->

Let us note also that in 5.3, `R` is finitely generated if and only if `H = D_S(R)` is of finite type (IX 2.1 b)). By
4.5, `H` is then quasi-isotrivial, hence `R` is quasi-isotrivial. One thus finds:

<!-- original page 103 -->

**Corollary 5.9.** *The functors of 5.7 induce anti-equivalences quasi-inverse to one another between the category of
`S`-groups `H` of multiplicative type of finite type, and that of finitely generated twisted constant `S`-groups `R`;
moreover, every such group `R` is quasi-isotrivial.*

<!-- label: III.X.5.9 -->

**Corollary 5.10.** *Let `H`, `G` be two `S`-preschemes in groups of multiplicative type and of finite type.*

<!-- label: III.X.5.10 -->

*(i) Then `Isom_{S-gr.}(H, G)` is representable by an open and closed subprescheme of `Hom_{S-gr.}(H, G)`, and it is a
twisted constant `S`-prescheme.*

*(ii) In particular, `Aut_{S-gr.}(H)` is representable and is a twisted constant `S`-group (in general
non-commutative).*

This follows from 5.8 and from VIII 1.6.[^N.D.E-X-38]

**Recall 5.11.0.**[^N.D.E-X-39] Recall that if `X` is a locally noetherian prescheme, its connected components (which
are always closed) are open. Indeed, let `C` be a connected component of `X`, `x ∈ C` and `U` a noetherian open
neighborhood of `x`; then `U` has only a finite number of connected components, hence the connected component `U_x` of
`x` in `U` is open in `U` hence in `X`; since `U_x ⊆ C`, this shows that `C` is open in `X`.

<!-- label: III.X.5.11.0 -->

**Proposition 5.11.** *Let `S` be a prescheme, `R` a commutative twisted constant group over `S`, `H = D_S(R)` the group
of multiplicative type that it defines. Consider the following conditions:*

<!-- label: III.X.5.11 -->

*(i) `H` is isotrivial (i.e. `R` is isotrivial).*

*(ii) `R` is the union of subpreschemes both open and closed `R_i`, which are quasi-compact over `S` (and then
necessarily finite over `S`).*

*(iii) The connected components of `R` are finite over `S`.*

*a) Then (i) ⇒ (ii) ⇒ (iii).*[^N.D.E-X-40]

*b) One has (i) ⇔ (ii) ⇔ (iii) if `S` is locally noetherian.*

*c) Finally, (i) ⇔ (ii) if `R` is finitely generated (i.e. if `H` is of finite type over `S`), at least if `S` is
quasi-compact or if its connected components are open.*

Decomposing first `S` into a prescheme sum of preschemes `S_i` on each of which `H` is of constant type (cf. IX 1.4.1),
we are reduced to the case where `H` hence `R` is of constant type `M`. We shall need:

**Lemma 5.12.** *Let `S` be a prescheme, `R` a twisted constant prescheme over `S`. Then every closed subprescheme `Z`
of `R` which is quasi-compact over `S` is finite over `S`.*

<!-- label: III.X.5.12 -->

Indeed, one reduces to the case where `R` is constant, hence of the form `I_S`, where `I` is a set, <!-- original page
104 --> hence the filtered increasing union of the `J_S`, where `J` runs through the finite subsets of `I`. One may
moreover suppose `S` affine; then `Z` is quasi-compact, hence contained in one of the `J_S`. Since `J_S` is finite over
`S`, the same holds for `Z`.

Lemma 5.12 already establishes the parenthesized assertion in 5.11 (ii).[^N.D.E-X-41] The implication (ii) ⇒ (iii) is
then clear, since the connected components of `R` are closed; by 5.11.0 they are open and closed if `S` is locally
noetherian (`R` being étale, hence locally of finite type over `S`), whence (iii) ⇒ (ii) in this case.

Let us prove that (i) ⇒ (ii). For this, let `S′ → S` be an étale finite surjective morphism splitting `H` hence `R` (cf.
5.3), so that `R′` is isomorphic to `M_{S′} = ∐_{m ∈ M} R′_m`, where the `R′_m` are disjoint open sets of `R′`,
`S′`-isomorphic to `S′`. Let `g : R′ → R` be the projection, which is a finite étale surjective morphism, hence an open
and closed morphism; then the `R_m = g(R′_m)` are open and closed parts of `R`, and obviously quasi-compact over `S`
since the `R′_m` are so.

Finally, suppose `H` of finite type over `S`, and let us prove (ii) ⇒ (i). The case where the connected components of
`S` are open reduces at once to the case where `S` is connected, so we may suppose `S` quasi-compact or connected. Since
`M` is finitely generated, one can write `M = ℤ^r × N`, where `r` is an integer `⩾ 0` and `N` a finite abelian group.
Let `G = D_S(M)`; consider the preschemes

```text
P = Isom_{S-gr.}(H, G) ⊂ Hom_{S-gr.}(H, G) = Q
```

(cf. 5.8 and 5.10). One has isomorphisms

```text
Q ≃ Hom_{S-gr.}(M_S, R) ≃ Hom_{S-gr.}(ℤ^r_S, R) × Hom_{S-gr.}(N_S, R) ≃ R^r × E,
```

where `E = Hom_{S-gr.}(N_S, R)` is finite over `S`[^N.D.E-X-42]. It follows that `Q` is the union of subpreschemes both
open and closed `Q_i` finite over `S`. Therefore `P` is the union of the subpreschemes both open and closed
`P_i = P ∩ Q_i`, finite over `S`. Since they are étale over `S`, their images in `S` are parts `S_i` both open and
closed, and they cover `S`. If `S` is connected or quasi-compact, there therefore exists a finite set <!-- original
page 105 --> of indices `i` such that the `S_i` cover `S`; let `S′` be the union of the corresponding `P_i`. Then
`S′ → S` is finite étale surjective, and setting `P′ = P ×_S S′ = Isom_{S′-gr.}(H′, G′)`, one sees that `P′` has a
section over `S′`, hence there exists an isomorphism of `S′`-groups

```text
H′ = H ×_S S′ ⥲ G′ = G ×_S S′ = D_{S′}(M),
```

which proves that `S′` splits `H`. This completes the proof of 5.11.[^N.D.E-X-43]

**Remark 5.11 bis.** Let us note moreover that one can, when `H` is of finite type over `S` and of constant type, give
the following isotriviality criterion (in which it is no longer necessary to make any restriction on `S`): `H = D_S(R)`
is isotrivial if and only if `R` is the union of a sequence of parts both open and closed finite over `S`.[^N.D.E-X-44]

<!-- label: III.X.5.11bis -->

**Lemma 5.13.** *Let `S` be a locally noetherian and connected prescheme, `P` a quasi-isotrivial twisted constant
`S`-prescheme, `Z` a part both open and closed of `P`, such that there exists an `s ∈ S` with `Z_s` finite. Then `Z` is
finite over `S`.*

<!-- label: III.X.5.13 -->

Let us first not suppose `S` connected: let `U` be the set of `s ∈ S` such that `Z_s` is finite; we shall prove that `U`
is both open and closed, and that `Z|U` is finite over `U`. This is a statement essentially equivalent to 5.13 but has
the advantage of being "of local nature" on `S` for the étale topology (say), which reduces us to the case where `P` is
constant, i.e. of the form `I_S`, where `I` is a set. (N.B. the locally noetherian hypothesis is not lost by an étale
base change; this is where we use the quasi-isotriviality of `P` over `S`.)

One may moreover suppose `S` connected, since its connected components are open (`S` being locally noetherian). But then
one necessarily has `Z = J_S`, where `J` is a part of `I`, and one therefore has `U = ∅` or `U = S`, depending on
whether `J` is infinite or finite, which gives the desired conclusion.

**Recalls 5.14.0.**[^N.D.E-X-45] Let `S` be a locally noetherian prescheme, and let `S̃` be the normalization of
`S_{red}` (cf. EGA II, 6.3.8). Recall that `S` is said to be *geometrically unibranch* (cf. EGA 0_IV, § 23.2 and IV₂, §
6.15) if the canonical morphism `S̃ → S` is radicial (and hence a universal homeomorphism); in particular, the connected
components of `S` are irreducible.

<!-- label: III.X.5.14.0 -->

Suppose then `S` connected, hence irreducible, let `η` be its generic point and let `f : P → S` be a flat and locally
quasi-finite morphism. Let `P_i` be the irreducible components of `P`, and `ξ_i` the generic point of `P_i`. Since `P`
is flat over `S`, each `ξ_i` <!-- original page 106 --> lies above `η` (cf. EGA IV₂, 2.3.4), and so
`(P_i)_η = P_i ∩ P_η` is the closure of `ξ_i` in `P_η`. Since the fiber `P_η` is discrete, one therefore has
`(P_i)_η = {ξ_i}`. This applies in particular when `f` is étale; in this case, `P` is also locally noetherian and
geometrically unibranch (cf. EGA IV₄, 17.5.7), so its irreducible components are its connected components and are open
(and closed).

**Corollary 5.14.** *Let `S` be a locally noetherian and geometrically unibranch prescheme, `P` a quasi-isotrivial
twisted constant `S`-prescheme. Then the connected components of `P` are finite over `S`.*

<!-- label: III.X.5.14 -->

One may obviously suppose `S` connected hence irreducible, and let `η` be its generic point. By what precedes, each
connected component `P_i` of `P` is open and closed, and meets the fiber `P_η` at a single point. Therefore 5.13 applies
and shows that each `P_i` is finite over `S`.

**Theorem 5.16.**[^N.D.E-X-46] *Let `S` be a locally noetherian and geometrically unibranch prescheme. Then every
`S`-group of multiplicative type and of finite type is isotrivial.*

<!-- label: III.X.5.16 -->

One may indeed suppose `S` connected, hence `H` of constant type `M`. It suffices to apply 5.14 to
`P = Isom_{S-gr.}(H, G)`, where `G = D_S(M)`, then to argue as in the proof of 5.11 (ii) ⇒ (i). One may also apply 5.14
to `P = R = D_S(H)` (cf. 5.9), then use 5.11.

## 6. Infinite Galois principal covers and the enlarged fundamental group

(The results of the present N° and of the following will no longer be used in the sequel of this Seminar.)

Let `S` be a prescheme; we propose to determine the principal homogeneous bundles `P` over `S` with structural group of
the form `G_S`, the constant `S`-group defined by an ordinary group `G` (not necessarily finite), which we shall also
call *Galois principal bundles over `S` with group `G`*. <!-- original page 107 --> We take "principal bundle" in the
sense of the faithfully flat quasi-compact topology (cf. Exp. IV, Def. 5.1.5), but we shall note that for such a `P`,
the structural morphism `P → S` is necessarily étale and surjective, hence covering for the étale topology; consequently
`P` is also locally trivial for the étale topology (cf. IV, Prop. 5.1.6).[^N.D.E-X-47]

We shall assume that `S` is a sum of connected preschemes, i.e. that its connected components are open, which reduces us
at once to the case where `S` is connected. We shall then choose a "geometric point" `ξ` of `S`, i.e. an `S`-scheme `ξ`
which is the spectrum of an algebraically closed field `Ω = κ(ξ)`. Then for every Galois principal bundle `P` over `S`
with group `G`, `P_ξ` is a Galois principal bundle over the algebraically closed field `κ(ξ)`, hence is trivial. We
shall therefore make the initial problem precise by proposing to determine the category of Galois principal bundles over
`S` *pointed* above `ξ`, i.e. endowed with an `S`-homomorphism `ξ → P`, i.e. with a trivialization of `P_ξ`. For fixed
`G`, the set of classes of such bundles, up to an isomorphism respecting the base point, will be denoted by
`π̄¹(S, ξ; G)`. Then the set `π̄¹(S; G)` of isomorphism classes of Galois principal bundles over `S` with group `G`
(without a specified base point) is isomorphic to the set of orbits of `G` in `π̄¹(S, ξ; G)` (taking into account the
natural operations of `G` on this set, corresponding to translation by `G` of the marked point in a pointed Galois
principal bundle `P`):

```text
π̄¹(S; G) = π̄¹(S, ξ; G)/G.
```

For every morphism `S′ → S` which is a morphism of universal effective descent for the fibered category of twisted
constant preschemes over a variable base (for example `S′ → S` faithfully flat and locally of finite presentation, cf.
5.4; for other examples cf. SGA 1 IX), we propose to determine the subsets of the preceding sets, denoted
`π̄¹(S′/S, ξ; G)` and <!-- original page 108 --> `π̄¹(S′/S; G)`, formed by the Galois principal bundles over `S` which
become trivial on `S′` (or, as one says, are "split" by `S′`). One will in fact determine the category of Galois
principal bundles `P` over `S` which are split by `S′`. Of course, one will then have

```text
π̄¹(S, ξ; G) = lim_{S′} π̄¹(S′/S, ξ; G),
```

where in the second member, `S′` runs over a cofinal system in the set of `S′/S` covering for the étale topology (for
example, when `S` is quasi-compact, the set of `S′` over `S` which are quasi-compact and with étale and surjective
structural morphism). Likewise, the category of Galois principal bundles over `S` will be the inductive limit of the
subcategories defined by the `S′` (formed of the bundles which are split over `S′`).

Thanks to the hypothesis made on `S′/S`, the category of Galois principal bundles over `S` split by `S′` is equivalent
to the category of trivial Galois principal bundles over `S′` (hence of the form `G_{S′}`, where `G` acts by right
translations), endowed with a descent datum relative to `S′ → S`. The datum of a base point on a Galois principal bundle
`P` over `S` split by `S′` amounts, in terms of the corresponding trivial bundle `P′` over `S′` and its descent datum,
to the datum of a trivialization of `P′ ×_{S′} S′_ξ` compatible with the induced descent datum, relative to `S′_ξ → ξ`
(N.B. we have set `S′_ξ = S′ ×_S ξ`), i.e. a section `σ` of `P′_ξ` over `S′_ξ` compatible with the descent datum. There
is then advantage, for an arbitrary `S`-prescheme `S′` (for which one no longer supposes that `S′ → S` is a morphism of
universal effective descent for the fibered category of twisted constant bundles…), in defining `π̄¹(S′/S; G)` and
`π̄¹(S′/S, ξ; G)` as the set of classes, up to isomorphism, of the structures with descent data just specified. One then
obtains, for these functors in `G`, a very simple simplicial description, in terms of the fibered square and cube `S″`
and `S‴` of `S′` over `S`, which we shall sketch below (cf. 6.3).

<!-- original page 109 -->

The important conclusion to retain will be the following:

**Proposition 6.1.** *Suppose that the connected components of `S′` and `S″` are open, and, for example, that the
quotient set of `π_0(S′)` by the equivalence relation induced by the two projections `π_0(S″) → π_0(S′)` is a single
point.*[^N.D.E-X-48]

<!-- label: III.X.6.1 -->

*(i) The functor `G ↦ π̄¹(S′/S, ξ; G)`, from the category of groups to the category of sets, is representable by a
group, denoted `π_1(S′/S, ξ)` and called the* fundamental group of `S` at `ξ` relative to `S′ → S`. *One thus has a
functorial bijection:*

```text
π̄¹(S′/S, ξ; G) ≃ Hom_{gr.}(π_1(S′/S, ξ), G).
```

*(ii) This group has a set of generators in bijection with `π_0(S″)`, and is described in terms of these generators by
relations in bijection with the elements of `π_0(S‴)`.[^N.D.E-X-49] In particular, `π_1(S′/S, ξ)` is finitely generated
(resp. of finite presentation) if `π_0(S″)` (resp. as well as `π_0(S‴)`) is finite.*

*(iii) The category of Galois principal bundles over `S` split by `S′`, with base point above `ξ`, is equivalent to the
category of ordinary groups `G`, endowed with a homomorphism of `π_1(S′/S, ξ)` into `G`.*

The proof is given below, cf. ….

**6.2.** When `S` is a connected locally noetherian prescheme, which implies that every étale prescheme `S′` over `S` is
locally noetherian hence has its connected components open, one concludes from what precedes[^N.D.E-X-50] that the
functor `G ↦ π̄¹(S, ξ; G)`, from the category of ordinary groups to the category of sets, is strictly pro-representable
(cf. *Séminaire Bourbaki*, February 1960, N° 195, §§ A.2 and A.3), i.e. there exists a projective system

<!-- label: III.X.6.2 -->

```text
Π = Π_1(S; ξ) = (π_i)_{i ∈ I}
```

of ordinary groups over a filtered increasing index set `I`, which is "strict" <!-- original page 110 --> (i.e. with
surjective transition morphisms `π_j → π_i`), and an isomorphism of functors in `G`

```text
π̄¹(S, ξ; G) ≃ lim_i Hom_{gr.}(π_i, G).
```

The second member is also simply denoted `Hom_{pro-gr.}(Π, G)` (cf. loc. cit.).

In the case where the projective limit `π = lim π_i` is "sufficiently large", more precisely when the canonical
homomorphisms `Π → Π_i` are surjective, it is appropriate to endow `Π` with the projective limit topology of the
discrete topologies of the `Π_i`, and the preceding isomorphism is also written:

```text
π̄¹(S, ξ; G) ≃ Hom_{gr. top.}(π, G),
```

where the second member denotes the set of homomorphisms of topological groups, it being understood that `G` is endowed
with the discrete topology.

The hypothesis just formulated on the projective system `Π` is verified, as is well known, when the `π_i` are finite
groups (cf. [BEns], III § 7.4, Th. 1). This last condition obviously also means that every Galois principal bundle over
`S` is isotrivial, i.e. is split by an étale surjective finite morphism. This is the case when `S` is geometrically
unibranch (for example normal), as follows at once from 5.14.[^N.D.E-X-51] In the case where the `π_i` are finite, the
group `π` coincides also with the fundamental group `π_1(S, ξ)` introduced in SGA 1, V.

Also, in the favorable case (`π → π_i` surjective) one could call `π` the *enlarged fundamental group of `S` at `ξ`*.
Outside of this favorable case, `π` itself is hardly of interest, and the role of the usual fundamental group is played
by the projective system `Π` itself, which one will call the *enlarged fundamental pro-group of `S` at `ξ`*. (Any
terminological suggestion better than "enlarged" is welcome![^N.D.E-X-52]). One will note that knowledge of this
pro-group is more precise than that of the usual fundamental group `π_1(S, ξ)` of SGA 1 V; more precisely, the latter is
the projective limit of the projective system formed by the finite quotients of the `π_i`.

**6.3.** Let us indicate rapidly the "computation" of `π_1(S′/S, ξ)`. Let `S_i` be the `(i + 1)`-th fibered power of
`S′` over `S` (i.e. `S_0 = S′`, `S_1 = S″`, etc.). One has between the `S_i` obvious simplicial operations, which make
`(S_i)_{i ∈ ℕ}` a simplicial object of `(Sch)/S`.

<!-- label: III.X.6.3 -->

<!-- original page 111 -->

Transforming this simplicial object by the functor "set of connected components"

```text
π_0 : (Sch)/S ⟶ (Ens),
```

one finds a simplicial set `K_• = (K_i)_{i ∈ ℕ}`, with `K_i = π_0(S_i)`.

Likewise, the `S_{i,ξ}` (= `(i + 1)`-th fibered power of `S′_ξ` over `ξ`) form a simplicial object of `(Sch)/ξ` hence of
`(Sch)/S`, moreover endowed with a natural homomorphism of simplicial objects into `(S_i)_{i ∈ ℕ}`, whence a simplicial
set `k_•` (with `k_i = π_0(S_{i,ξ})`) and a canonical homomorphism

```text
k_• ⟶ K_•.
```

We can form a new simplicial set by taking the cone of this morphism (cf. 9.5.1):

```text
K̃_• = Cone(k_• ⟶ K_•).
```

[^N.D.E-X-53] In this way, one obtains a "pointed simplicial set" `K̃_•` (i.e. a simplicial set endowed with a
homomorphism `ξ̃ : ẽ_• → K̃_•`, where `ẽ_•` is the final simplicial set). We can construct its well-known combinatorial
invariants `π_0(K̃_•, ξ̃)` and `π_1(K̃_•, ξ̃)`, whose construction involves only the components of degree `⩽ 1` resp. of
degree `⩽ 2`. These invariants are defined without restriction on `S` or `S′`. One then verifies without difficulty,
when the connected components of `S_0` and `S_1` are open and `K̃_•` is connected,[^N.D.E-X-54] that `π_1(K̃_•, ξ̃)`
represents the functor `G ↦ π̄¹(S′/S, ξ; G)`, i.e. one has:

```text
π_1(S′/S; ξ) ≃ π_1(K̃_•, ξ̃).
```

Let us also signal that when the morphism `S′ → S` is "universally submersive" (cf. SGA 1, IV 2.1), and the connected
components of `S′` are open, then[^N.D.E-X-55] <!-- original page 112 --> the simplicial set `K_•`, hence also `K̃_•`,
is connected.

**Examples 6.4.** It remains to give examples of enlarged fundamental groups. Let us take up the examples of 1.6, i.e.
let `k` be an algebraically closed field, `C_1` a complete rational curve over `k`, having exactly one singular point,
this point being an ordinary double point, and `C_2` a curve which is the union of two irreducible components,
isomorphic to `P¹_k` and meeting at exactly two points, which are ordinary double points of `C_2`. In either case, the
enlarged fundamental group of the curve is isomorphic to `ℤ`.[^N.D.E-X-56]

<!-- label: III.X.6.4 -->

In general, there would be reason to take up (simplifying and rectifying them) the results of SGA 1 IX 5, in the
framework of the enlarged fundamental group. The examples of loc. cit., 5.5 would give as many examples of enlarged
fundamental pro-groups which are not profinite. Thus, if instead of an ordinary double point, one took in the first
example a double point with `n` distinct branches,[^N.D.E-X-57] one would find as enlarged fundamental group the free
(discrete!) group on `n − 1` generators.

## 7. Classification of twisted constant preschemes and of groups of multiplicative type of finite type in terms of the enlarged fundamental group

**7.0.** Let `S` be a prescheme, which we still assume locally noetherian, to ensure that `S` and certain preschemes
over `S` that we shall consider <!-- original page 113 --> (notably those étale over `S`, more generally those locally
of finite type over `S`) are locally connected.

**Proposition 7.0.1.** *Every twisted constant prescheme `X` over `S` which is locally trivial for the (fppf) topology
(i.e. which is split by a faithfully flat morphism locally of finite presentation `S′ → S`) is quasi-isotrivial (i.e.
one can even choose `S′ → S` étale surjective).*

<!-- label: III.X.7.0.1 -->

Indeed, one may suppose `S` connected, hence `X` of type `I`, where `I` is a fixed set. Therefore `X′ = X ×_S S′` is
isomorphic to `I_{S′}`, hence `I_{S′}` is endowed with a descent datum relative to `S′ → S`, i.e. one has an isomorphism
`I_{S″} ⥲ I_{S″}` satisfying the usual transitivity condition. Now, `S″ = S′ ×_S S′` is locally noetherian hence locally
connected, whence it follows that the automorphisms of `I_{S″}` correspond to the sections of `G_{S″}`, where
`G = Aut(I)` is the group of permutations of `I`.

In this way, one obtains a descent datum on `G_{S′}` (considered as a trivial Galois principal bundle) relative to
`S′ → S`. By 5.4 this descent datum is effective, whence a Galois principal bundle `P` over `S`, with group `G`. By
construction, it represents the functor `Isom_S(I_S, X)` in the category of preschemes over `S` which are locally
noetherian. Consequently, the étale surjective base change `P → S` splits `X`, so `X` is indeed quasi-isotrivial.

**Remark 7.0.2.** Beware that even if `S` is the spectrum of a field, it is not true in general that every twisted
constant bundle over `S` is quasi-isotrivial. It suffices for example to take for `X` the scheme sum of a sequence of
schemes of the form `Spec(k_i)`, where the `k_i` are separable extensions of `k` of strictly increasing degrees.

<!-- label: III.X.7.0.2 -->

The proof given above shows at the same time that the classification of twisted constant bundles `X` over `S`,
quasi-isotrivial and of type `I`, is equivalent to that of Galois principal bundles over `S` with group `G = Aut(I)`. It
is even an equivalence of categories.

It can be put in a more convenient form as in SGA 1 V. For this, <!-- original page 114 --> suppose `S` connected and
equipped with a geometric point `ξ`. Consequently the enlarged fundamental pro-group `Π = Π_1(S, ξ)` is defined.
Moreover, for every quasi-isotrivial twisted constant bundle `X` over `S`, let `I = X(ξ)` be its set-theoretic fiber at
`ξ`. Therefore `X` is of type `I`, and consequently associated as we have just said with a Galois principal bundle
`P = Isom_S(I_S, X)` over `S`, with group `G = Aut(I)`.

By the definition of `Π`, one therefore obtains a canonical homomorphism of `Π` into `G`, i.e. of one of the `Π_i` into
`G`. Since `G` is the group of permutations of `I = X(ξ)`, this means that `Π` "acts continuously on `I = X(ξ)`", it
being understood that the `π_i` (`i` large) act on `I`, in a way compatible with the transition morphisms.

We leave to the reader the verification that every `S`-morphism `X → Y` between quasi-isotrivial twisted constant
bundles over `S` induces a map `X(ξ) → Y(ξ)` compatible with the operations of `Π`, and that the functor thus obtained
is an equivalence of categories:

**Proposition 7.0.3.** *Let `S` be a locally noetherian connected prescheme, `ξ` a geometric point of `S`,
`Π = Π_1(S, ξ)` the enlarged fundamental pro-group of `S` at `ξ`. Then the functor*

<!-- label: III.X.7.0.3 -->

```text
X ↦ X(ξ)
```

*is an equivalence between the category of quasi-isotrivial twisted constant bundles over `S` and the category of sets
on which `Π` acts continuously.*

This functor is compatible with the operations of finite sums and finite inverse limits. It follows for example that the
twisted constant groups (or rings etc.) quasi-isotrivial over `S` correspond to the ordinary groups (resp. rings etc.)
on which the pro-group `Π` acts continuously. In particular:

**Corollary 7.0.4.** *The category of commutative twisted constant groups quasi-isotrivial over `S` is equivalent to the
category of "`Π`-modules", i.e. of commutative groups `M` on which `Π` acts continuously.*

<!-- label: III.X.7.0.4 -->

Using now 5.7 one concludes the:

**Theorem 7.1.** *Let `S` be a locally noetherian connected prescheme, `ξ` a geometric point of `S`, `Π = Π_1(S, ξ)` the
enlarged fundamental pro-group of `S` at `ξ`. Then the functor*

<!-- label: III.X.7.1 -->

```text
G ↦ Hom_{κ(ξ)-gr.}(G_ξ, G_{m,ξ})
```

*induces an anti-equivalence of the category of quasi-isotrivial groups of multiplicative type over `S`* <!-- original
page 115 --> *with the category of `Π`-modules.*

Using 4.5 one concludes:

**Corollary 7.2.** *The preceding functor induces an anti-equivalence of the category of groups of multiplicative type
and of finite type over `S` with the category of `Π`-modules which are of finite type over `ℤ`.*

<!-- label: III.X.7.2 -->

**Example 7.3.** Take for example for `S` a complete rational curve over an algebraically closed field, having exactly
one multiple point with `n + 1` distinct branches. By 6.4, the enlarged fundamental group `Π(S, ξ)` is a free group on
`n` generators. Therefore, by 7.2, the classification of tori of relative dimension `m` over `S` is equivalent to the
classification of systems of `n` endomorphisms `A_1, …, A_n` of the `ℤ`-module `ℤ^m`, up to automorphism of `ℤ^m`.
Except for `n ⩽ 1` or `m ⩽ 1`, an explicit classification of such systems seems hopeless. One can at least define a
multitude of non-trivial invariants for such a system, such as the characteristic polynomials of the `A_i`.[^N.D.E-X-58]

<!-- label: III.X.7.3 -->

**Remark 7.4.** If one makes no hypothesis on `S`, it remains true that for a given ordinary commutative group `M` of
finite type over `ℤ`, the category of groups of multiplicative type of type `M` over `S` is anti-equivalent to the
category of Galois principal bundles over `S` with group `G = Aut_{gr.}(M)`. This follows easily from 5.9 and 5.10.

<!-- label: III.X.7.4 -->

**Remark 7.5.** The theory of the fundamental pro-group that we have sketched in the present two numbers will be written
more advantageously in the framework of general sites. In this form, it applies equally well, for example, to ordinary
topological spaces, and gives a satisfactory theory at least for a locally connected topological space (not necessarily
locally simply connected). In this case too it seems that one cannot be content with defining a fundamental group, and
that a pro-group is needed. Finally, let us note that, once one has available the language of topologies and descent
(which is really at the bottom of these questions), the exposition sketched here is also technically simpler than that
of SGA 1 V, and should therefore in principle replace it.

<!-- label: III.X.7.5 -->

## 8. Appendix: Elimination of certain affineness hypotheses

<!-- original page 116 -->

Our aim is to prove the following generalization of 4.9.

**Theorem 8.1.** *Let `S` be a prescheme, `H` an `S`-prescheme in groups flat and of finite presentation, with connected
and affine fibers.[^N.D.E-X-59] Let `s ∈ S`; suppose that `H_s` is a torus. Then there exists an open neighborhood `U`
of `s` such that `H|U` is a torus.*

<!-- label: III.X.8.1 -->

One concludes immediately:

**Corollary 8.2.** *Let `H` be an `S`-prescheme in groups, flat and of finite presentation over `S`. For `H` to be a
torus, it is necessary and sufficient that its fibers be tori.*

<!-- label: III.X.8.2 -->

**Remark 8.3.** Even when `S` is the spectrum of a discrete valuation ring, one cannot abandon in 8.1 the hypothesis
that the fibers of `H` (here the generic fiber) be affine, since there are examples of smooth groups over `S` whose
generic fiber is an elliptic curve, and whose special fiber is `G_m`.

<!-- label: III.X.8.3 -->

*Proof of 8.1.* One may obviously suppose `S = Spec(A)` affine, which reduces us by the standard procedure (cf. EGA IV₂,
8.8.2) to the case where `S` is moreover noetherian. We begin by proving 8.2 in this case.

By 4.9 we are reduced to proving that `H` is affine over `S`. We may therefore suppose[^N.D.E-X-60] `A` noetherian
local, and since the completion `Â` is faithfully flat over `A`, we are reduced by descent to the case where `A` is a
complete noetherian local ring. Let `S′` be the normalization of `S_{red}`; one knows by Nagata that it is finite over
`S` (EGA 0_IV, 23.1.5); moreover `S′ → S` is surjective, so `H′ = H ×_S S′ → H` is finite and surjective, so to prove
that `H` is affine, it suffices to show that `H′` is so (EGA II, 6.7.1).

<!-- original page 95 -->

[^N.D.E-X-61] Replacing `S` by a connected component of `S′`, this reduces us to the case where `A` is a noetherian
(semi-local) normal and integral ring. Moreover, possibly replacing `A` by its normalization in a finite separable
extension of its field of fractions, <!-- original page 117 --> one may suppose that the generic fiber `H_η` of `H` is
diagonalizable, i.e. that one has an isomorphism

```text
u_η : H_η ⥲ T_η,
```

where `T = G^r_{m,S}`. Now we have:

**Lemma 8.4.** *Let `S` be a locally noetherian normal and irreducible prescheme, with generic point `η`, `H` a
prescheme in groups over `S` smooth and with connected fibers, `T` a prescheme in groups of multiplicative type and of
finite type over `S`, `u_η : H_η → T_η` a homomorphism of algebraic groups over `κ(η)`.*

<!-- label: III.X.8.4 -->

*Then `u_η` extends to a homomorphism of groups `u : H → T`.*

Possibly replacing `S` by its normalization in a finite separable extension of its function field, one may suppose `T`
diagonalizable (which is moreover the case in the application we have in view). Then `T` is a closed subgroup of a group
of the form `G^r_{m,S}`, which reduces us to the case where `T = G_{m,S}`.

It all amounts to proving that `u_η`, considered as a rational map of `H` into `T = G_{m,S}`, is everywhere defined
(since the morphism `u : H → T` extending it is then necessarily a homomorphism of groups). One may consider `u_η` as an
invertible section `f` of the structural sheaf of `H_η`, and one must show that it extends to an invertible section of
the structural sheaf of `H`. Now `H`, being smooth over the normal `S`, is normal (SGA 1, II 3.1), so it suffices to
find a closed part `Z` of `H` of codimension `⩾ 2` such that `f` extends to an invertible section of the structural
sheaf of `H − Z`. This reduces us at once to the case where `S` is the spectrum of a discrete valuation ring `A` (by
localizing at points of codimension 1 of `S`).

Let `t` be a uniformizer of `A`, `t′` the section of `O_H` that it defines, so that the special fiber `H_0` is equal to
`V(t′)`. By hypothesis `H_0` is smooth over the residue field `k`, and connected. Then `f` is a rational function on `H`
which has neither zeros nor poles in `H − H_0`; since `H_0 = V(t′)` is an irreducible divisor, there exists an integer
`n ∈ ℤ` such that `t′^n f = t^n f` has neither zeros nor poles, i.e. is an invertible section of `O_H`. <!-- original
page 118 --> It therefore defines a morphism `v : H → G_{m,S}`, and since `v_η = t′^n u_η` and `u_η` is a homomorphism
of groups, `v` transforms the unit section of `H` into a section of `G_{m,S}` whose value at the generic point of `S` is
`t^n`; since it is a question of a section of `G_{m,S}`, `t^n` must be a unit, i.e. `n = 0`, so `v` extends `u_η`, which
completes the proof of 8.4.

Applying this lemma to the present case, one finds a homomorphism of groups

```text
u : H ⟶ T = G^r_{m,S}
```

which induces on the generic fibers an isomorphism. Let us prove that `u` is an isomorphism.

**Lemma 8.5.** *For every integer `n > 0` prime to the residual characteristic of `A`, `_n H = Ker(n · id_H)` is finite
over `S`.*

<!-- label: III.X.8.5 -->

If `n` is prime to the residual characteristic of `A`, it is prime to all the residual characteristics of points of `S`.
Therefore `n · id_H` induces on every fiber of `H` an étale morphism; consequently `n · id_H` is étale (SGA 1, I 5.9),
so its kernel `_n H` is étale over `S`. On the other hand, `_n H` is separated over `S` since `H` is.[^X-8-1]
[^N.D.E-X-62] Moreover, all its fibers have the same rank `n^r`, since the fibers of `H` are tori, all of the same
dimension `r` (`H` being smooth over `S`). One concludes that `_n H` is finite over `S` (SGA 1, I 10.9 or EGA IV₄,
18.2.9).

Therefore, by the preceding lemma, `u(_n H)` is a closed part of `T`. Since on the generic fiber `T_η`, this part is
identical to `_n(T_η)`, it follows that it contains the closure of this part, namely `_n T`. Now for every `s ∈ S`, the
`_n(T_s)` are dense in `T_s`; since `u_s(H_s)` is a closed part (VI_B 1.4.2) containing them, one sees that
`u_s(H_s) = T_s`, so `u` is surjective. Since a surjective homomorphism of tori of the same dimension over a field is
flat,[^N.D.E-X-63] it follows that `u` induces on each fiber a flat morphism, so `u` is flat (SGA 1 I 5.9).
Consequently, `K = Ker(u)` is flat over `S`,[^N.D.E-X-64] hence equal to the closure of its generic fiber `K_η`. Now
`K_η` is the unit group by construction, and since `K` is separated over `S` (since `H` is), its unit section is closed,
whence it follows that `K` is the unit group. <!-- original page 119 --> Therefore `u` is a monomorphism; since we have
seen that it is faithfully flat, it is therefore an isomorphism (cf. SGA 1, I 5.1 or EGA IV₄, 17.9.1). This proves that
`H` is a torus, hence completes the proof of 8.2.[^N.D.E-X-65]

**Remark 8.5.1.** Instead of invoking 8.5 one can also invoke Zariski's "Main Theorem", which directly implies that `u`
is an open immersion, hence an isomorphism.[^N.D.E-X-66]

<!-- label: III.X.8.5.1 -->

To prove 8.1, we are reduced, thanks to the quasi-isotriviality theorem, to the case where `S` is local, `s` its closed
point,[^N.D.E-X-67] and to proving that, with the hypotheses made elsewhere, `H` is then a torus. By 8.2 already proved,
we are reduced to proving that the fibers of `H` are tori. One may suppose `S` the spectrum of a complete noetherian
local ring `A`. By 3.3 there exists for every `n > 0` a group of multiplicative type `T_n` finite over `S`, and an
isomorphism `(T_n)_s ≃ _n(H_s)`, where `s` is the closed point of `S`. Proceeding as in 3.1 and using the fact that
`T_n` is finite over `S`,[^N.D.E-X-68] one sees that the preceding isomorphism comes from a homomorphism
`u_n : T_n → H`, moreover uniquely determined. (Pass to the limit over the artinian quotients of `A`.)

Moreover, by uniqueness properties, `u_n : T_n → H` is deduced from `u_m : T_m → H` by restriction to `_n(T_m) ≃ T_n`
when `m` is a multiple of `n`. It follows from IX 6.6 that the `u_n` are monomorphisms, so the `T_n` are subgroups of
`H`, and for `m` a multiple of `n`, one has `T_n = _n(T_m)`.

Therefore for every `t ∈ S`, the `(T_n)_t` are subgroups of `H_t`, of type `(ℤ/nℤ)^r` (where `r = dim H_s = dim H_t`),
such that for `m` a multiple of `n`, one has `(T_n)_t = _n(T_m)_t`. The fact that `H_t` is a torus now follows from:

**Lemma 8.6.** *Let `H` be a smooth affine algebraic group over an algebraically closed field `k`, `(T_n)_{n > 0}` a
family of subgroups of multiplicative type of `H`, such that for every integer `n > 0`, `T_n` is of type `(ℤ/nℤ)^r`, and
for every multiple `m` of `n`, one has `T_n = _n(T_m)`.*

<!-- label: III.X.8.6 -->

*Under these conditions, `H` contains a torus of dimension `⩾ r` containing the `T_n`,* <!-- original page 120 --> *so
if `H` is connected of dimension `⩽ r`, `H` is a torus of dimension `r`.*

This is an exercise on affine algebraic groups, which we shall treat by reference to *Bible*. We confine ourselves to
considering the `T_n` for `n` prime to the characteristic. Let `K` be the closure of the union of the `T_n` in `H`,
endowed with the induced reduced structure; then standard arguments show that `K` is a commutative algebraic subgroup of
`H`. By *Bible*, § 4.5, Th. 4, `K` is therefore isomorphic to a product `K_u × K_s`, with `K_u` "unipotent" and `K_s`
diagonalizable. Every diagonalizable subgroup of `K` is contained in `K_s`, so the `T_n` are subgroups of `K_s`, hence
`K = K_s`. Write `K = D(M)`, with `M` an ordinary commutative group of finite type over `ℤ`; then `T_n ⊆ K` means that
`M` admits a quotient group isomorphic to `(ℤ/nℤ)^r`. Since this is true for every integer `n` prime to the
characteristic of `k` (it would suffice for powers of a fixed prime number), it follows that `M` is of rank `⩾ r`, so
`K` contains a torus of dimension `r`, say `T`. When `H` is connected of dimension `r`, it follows that `T = H`, which
completes the proof of 8.6. Thus 8.1 is proved.

**Remarks 8.7.** Using 8.1, it should not be difficult to give analogous generalizations of 4.7 and 4.8. A more
interesting study would be that of the situation in 8.1 where one abandons the hypothesis that the fibers of `H` be
affine. One can show that there then exists an open neighborhood `U` of `s` such that `H|U` is commutative and that for
every `t ∈ U`, the geometric fiber `H_t` is an extension of an abelian variety by a torus.[^N.D.E-X-69] Of course, in
questions of this kind, one may restrict oneself to the case where `S` is the spectrum of a discrete valuation ring, `s`
its closed point, `t` its generic point.

<!-- label: III.X.8.7 -->

One can generalize this result as follows. For every algebraic group `G` connected smooth over an algebraically closed
field `k`, a well-known theorem of Chevalley <!-- original page 121 --> tells us that `G` is (in a unique way) an
extension of an abelian variety `A` by a smooth connected affine group `V`. Let us denote by *abelian rank* (resp.
*reductive rank*, resp. *nilpotent rank*, resp. *semisimple dimension*) of `G`, and denote by `ρ_{ab}(G)` (resp.
`ρ_r(G)`, resp. `ρ_n(G)`, resp. `d_s(G)`), the dimension of `A`, resp. the dimension of the maximal tori of `G`, resp.
the dimension of the Cartan subgroups[^N.D.E-X-70] of `G`, resp. the dimension of the quotient of `G` (or also of `V`)
by its radical (cf. *Bible* for all these notions). Let us also introduce the *unipotent rank*
`ρ_u(G) = ρ_u(V) = ρ_n(G) − ρ_r(G) − ρ_{ab}(G)`. When `G` is not over an algebraically closed field, we still denote by
the same names and the same notations the corresponding invariants for `G_{k̄}`, where `k̄` is the algebraic closure of
`k`.

This being so, let `G` be a smooth group scheme over the spectrum `S` of a discrete valuation ring; let `ρ_{ab}` etc.
(resp. `ρ′_{ab}` etc.) be the invariants associated with the special fiber (resp. with the generic fiber); then one has
the inequalities:

```text
⎧ ρ_{ab} ⩽ ρ′_{ab}             ⎧ ρ_n ⩾ ρ′_n
⎨ ρ_r + ρ_{ab} ⩽ ρ′_r + ρ′_{ab}⎨
⎩ d_s ⩽ d′_s                   ⎩ ρ_u ⩾ ρ′_u.
```

It amounts to the same to say that if `G` is smooth of finite type over an arbitrary base `S`, the functions
`s ↦ ρ_{ab}(s)`, `ρ_{ab}(s) + ρ_r(s)`, `d_s(s)` are lower semi-continuous, and the functions `s ↦ ρ_n(s)`, `ρ_u(s)` are
upper semi-continuous.[^N.D.E-X-71]

The same results probably remain valid without supposing `G` smooth over `S`, but simply flat of finite presentation
over `S`, by agreeing to denote, for an algebraic group `G` over an algebraically closed field `k`, by `ρ_{ab}(G)` etc.
the corresponding invariants of `G^0_{red}`.

In this Seminar, we present some results of this kind for `G` affine over `S`, or more generally with affine fibers:

<!-- original page 122 --> in this case, we shall verify the semi-continuity properties for `ρ_r`, `ρ_n` hence for

`ρ_u = ρ_n − ρ_r`, and the continuity of `ρ_s` in a neighborhood of a point `s` whose fiber is a reductive
group.[^N.D.E-X-71]

One can generalize 8.2 when one supposes already `G` commutative, as follows:

**Theorem 8.8.**[^N.D.E-X-72] *Let `G` be an `S`-prescheme in commutative groups which is flat and of finite
presentation over `S`, with affine connected fibers. Let `s ∈ S`, and suppose that*

<!-- label: III.X.8.8 -->

*a) if `k̄` denotes an algebraic closure of `κ(s)`, `(G_{k̄})_{red}` is a torus.*

*b) There exists a generization `t` of `s` such that `G_t` is smooth over `κ(t)`.*

*Under these conditions, there exists an open neighborhood `U` of `s` such that `G|U` is a torus.*

*(Note moreover that if one supposes only that for every generization `t` of `s`, `G_t` is affine resp. connected, one
easily derives that the same conclusion is valid for `t` in an open neighborhood of `s`).*

*Proof of 8.8.* It suffices to prove that `G_s` is smooth over `κ(s)`. Indeed, since `G` is flat of finite presentation
over `S`, it then follows that `G` is smooth over `S` above a neighborhood of `s` (cf. 3.5), but then one is under the
conditions of 8.1.

To prove that `G_s` is smooth over `κ(s)`, the usual procedure reduces us to the case where `S` is affine noetherian.
Choosing a homomorphism `S′ → S` from a spectrum of a discrete valuation ring `S′` into `S`, sending the closed point to
`s` and the generic point `η` to `t`, we are reduced to the case where `S` is itself the spectrum of a discrete
valuation ring, which may be assumed moreover complete with algebraically closed residue field, and where `s` and
`t = η` are respectively the closed point and the generic point of `S`.

Therefore `G` is flat, separated, of finite type over `S`, the generic fiber `G_η` is smooth and connected, <!--
original page 123 --> and the special fiber `G_0` is such that `T_0 = (G_0)_{red}` is a torus. Let `m` be an integer
`> 0` prime to the residual characteristic at `s`, hence also to that at `η`; one knows then that `m · id_G` is a
fiber-by-fiber étale morphism (VII_A 8.4), hence an étale morphism since `G` is flat over `S` (SGA 1 I 5.9), so its
kernel `_m G` is étale over `S`, and since `G` is separated[^X-8-2] [^N.D.E-X-73] of finite type over `S`, so is `_m G`.
Since `(_m G)_0 = _m(T_0)`, its degree is `m^r`, where `r = dim T_0 = dim G_0 = dim G`. It follows that the rank of
`(_m G)_η = _m(G_η)` is `⩾ m^r`, which proves already (using 8.6) that `G_η` is a torus of dimension `r`, since the two
fibers of `_m G` have the same rank, hence as in 8.5 that `_m G` is finite over `S`.[^N.D.E-X-74]

Note that since `S` is complete with algebraically closed residue field, the finite étale cover `_m G` decomposes
completely, so through every point of `_m G_0` passes a section of `G` over `S`; in particular, the set of points of
`G_0` through which passes a section of `G` over `S` is everywhere dense. Now we have this:

**Lemma 8.9.** *Let `S` be a locally noetherian regular prescheme of dimension 1, `G` an `S`-prescheme in groups flat
and locally of finite type, such that `G_η` is smooth over `κ(η)` for every maximal point `η` of `S` (which implies that
`G` is reduced). Suppose that the normalized scheme `X` of `G` is finite over `G` (this is the case, by Nagata, if `S`
is the spectrum of a complete discrete valuation ring, cf. EGA IV₂, 7.7.4), and let `G′` be the open set of `X` formed
by the points at which `X` is smooth over `S`. With these notations:*

<!-- label: III.X.8.9 -->

*a) If the projection `G′ → S` is surjective, then there exists on `G′` a unique structure of `S`-prescheme in groups
such that the canonical morphism `G′ → G` is a homomorphism of groups.*

*b) Suppose that for every closed point `s` of `S`, the set of points of `G^0_s` through which passes an étale
quasi-section is dense in `G^0_s` for the Zariski topology. Then `X` is regular, one is under the conditions of a), and
the map `Γ(G′/S) → Γ(G/S)` is bijective.*

<!-- original page 124 -->

In the case of interest to us, this lemma applies and gives us a homomorphism of groups `u : G′ → G`, where `G′` is
smooth over `S`, and `u_η` is an isomorphism `G′_η ⥲ G_η`. Possibly replacing `G′` by an open subgroup, one may suppose
that `G′_0` is connected, and since `u_0 : G′_0 → G_0` induces a surjective morphism `G′_0 → T_0`, where `T_0` is a
torus of the same dimension as `G′_0`, one easily concludes that `G′_0` is a torus (for example using 8.6, or by
referring to *Bible*, § 7.3, Th. 3 a)). Consequently, by 8.2 `G′` is a torus, but then by IX 6.8, `Ker u` is a subgroup
of multiplicative type of `G′`, and since its generic fiber is reduced to the unit group, it is the unit group, hence
`u` is a monomorphism. Using now VIII 7.9 it follows that `u` is an immersion. Being surjective, and `G` being reduced,
it follows that `u` is an isomorphism, which completes the proof of 8.8.

It remains to prove 8.9. To prove a), note that the uniqueness of the group law on `G′` making `u : G′ → G` a
homomorphism of groups is clear, since one knows the group law of `G′` on the generic fiber (supposing `S` irreducible,
which is permissible). For existence, one reduces easily to the case where `S` is local, the spectrum of a discrete
valuation ring `A`, and thanks to uniqueness, and to the fact that the operation of integral closure commutes with an
étale base extension, one can make étale base extensions on `S`, which reduces us to the case where `A` is "strictly
local" i.e. henselian with separably closed residue field. The same reduction applies for b), but under the hypothesis
made in b), one can now replace "étale quasi-section" by "section".

Note that `G′` being smooth over `S` and `X` normal, `G′ ×_S X` is normal (since smooth over `X` which is normal), so
the composite morphism `G′ ×_S X → G ×_S G → G` factors as

```text
p : G′ ×_S X ⟶ X.
```

<!-- original page 125 -->

Let us prove that this last morphism induces on the open set `G′ ×_S G′` of `G′ ×_S X` a morphism

```text
G′ ×_S G′ ⟶ G′.
```

One must therefore show that `G′_0 ×_k G′_0` is mapped into the open set `G′_0` of `X_0`; it suffices to see that for
every point `g′_0` of `G′_0` with values in `k`, the morphism

```text
(×)    h′_0 ↦ p_0(g′_0, h′_0)
```

from `G′_0` into `X_0` takes its values in `G′_0`. Now since `G′` is smooth over `S` and `S` is henselian, every `g′_0`
as above is induced by a section `g′` of `G′` over `S`, and one sees at once that the morphism `(×)` above is then
induced by the morphism `h′ ↦ p(g′, h′)` of `G′` into `X`, itself deduced by transport of structure from the
automorphism `h ↦ g · h` of `G`, left translation by the section `g` of `G` image of `g′`. So `h′ ↦ p(g′, h′)` is itself
an automorphism of `X`, hence maps `G′` into `G′`, which proves our assertion.

It remains to prove that the composition law thus obtained on `G′` is a group law. Associativity follows at once from
the associativity of the generic fiber (isomorphic to that of `G`). On the other hand, the symmetry automorphism of the
`S`-prescheme `G` induces an automorphism of `X`, which therefore leaves `G′` stable and induces an automorphism `σ` of
`G′`. One then verifies that the latter has the properties of an inverse for the composition law on `G′`, since this
again reduces to verifying the commutativity of certain diagrams involving fibered powers of `G′` over `S`, and the
latter being smooth over `S`, it suffices to verify the commutativity on the generic fiber, which is clear. This proves
part a) of 8.9.

Let us prove b). Let `Z′` be the set of `x ∈ X` such that `O_{X,x}` is non-regular; it is a closed part by a theorem of
Nagata (EGA IV₂, 6.12.6), <!-- original page 126 --> obviously contained in `X_0`; let `Z` be its image in `G`, which is
therefore a closed part of `G_0`. Then `Z` is a rare part of `G_0`, i.e. contains no maximal point `y` of `G_0`. Indeed,
since `G_0` is defined in `G` by an equation `t = 0` (where `t` is a uniformizer of the discrete valuation ring `A`),
`O_{G,y}` is of dimension 1 by the Hauptidealsatz, so for every `x` of `X` above `y`, `O_{X,x}` is of dimension 1, hence
a discrete valuation ring since `X` is normal hence regular in codimension 1. On the other hand, it is evident that for
every section `g` of `G` over `S`, `Z′` is stable under the automorphism of `X` defined by transport of structure from
the left translation by `g` in `G`, so `Z` is stable under the left translation in `G_0` defined by `g_0`. Now by
hypothesis the set of such `g_0` is dense in `G^0_0`. Since `Z` is stable under translation by these `g_0`, and is a
rare closed set, it follows at once that `Z = ∅`, whence `Z′ = ∅`, so `X` is regular. Consequently, `X` is smooth over
`S` at every point through which passes a section. Now every section of `G` over `S` lifts in a unique way to a section
of `X` over `S` hence of `G′` over `S`. This is so in particular for the unit section, which proves that the image of
`G′` in `S` is `S`, i.e. that one is under the conditions of (a). This completes the proof of 8.9 and hence of 8.8.

## 9. Addenda

[^N.D.E-X-75]

### 9.1. Simplicial sets, topoi, groupoids, and topological spaces

**Notations 9.1.1.**[^X-9-1] *Let `E` be a simplicial set. One can associate with it the following objects:*

<!-- label: III.X.9.1.1 -->

*(2) a topos `T = E^∼`, obtained from the topoi naturally associated with the sets `E_i`, by the procedure described in
[Del74], 6.3.1 (see also [Ill72], VI.5.2 and SGA 4 VI.7);*

*(3) a groupoid `G = Π(E)`, whose objects are the elements of `E_0` (the "vertices"), and whose arrows are defined in
[GZ67], II.7;*

*(4) a topological space `X = |E|` (a cellular complex), called the "geometric realization" (or "topological") (cf. loc.
cit., III.1).*

Let us note that a sheaf on `T` is nothing other than a simplicial set over `E`.

<!-- original page 102 -->

### 9.2. Locally constant sheaves; descent data

**Definitions 9.2.1.** *One calls a* locally constant sheaf *on:*

<!-- label: III.X.9.2.1 -->

*(1) a simplicial set `E`, every morphism of simplicial sets `E′ → E` such that for every `i ∈ ℕ` and every `e ∈ E_i`,
the face operators `d` induce isomorphisms `E′_e ⥲ E′_{d(e)}` between the fibers (cf. [AM69], § 10);*

*(2) a topos `T`, every object `F` of `T` such that there exists an epimorphism `U → 1` and an isomorphism
`F × U ≃ f^∗ I × U`, where `I` is a set and `f : T → Ens` is the final morphism (cf. SGA 4, IX.2);*

*(3) a groupoid `G`, every presheaf on `G`, that is, every contravariant functor from `G` into the category of sets (cf.
[GZ67], append. I.1.2);*

*(4) a topological space `X`, every sheaf of sets on `X`, locally constant in the usual sense.*

*Finally:*

*(5) one calls a* descent datum *on a simplicial set `E` the datum of a sheaf `F` on `E^∼_0` (that is, a set-valued
function on `E_0`) and of an isomorphism `α : p_1^∗ F ⥲ p_2^∗ F`, where `p_1, p_2 : E^∼_1 → E^∼_0` are the morphisms
(deduced from the) faces, satisfying the usual cocycle relation (cf. Exp. IV, 2.1 (1) and infra).*

The morphisms between these five types of objects, as well as the associated inverse-image functors, are defined in an
obvious manner.

### 9.3. Some equivalences of categories

Let `E` be a simplicial set and let `T`, `G` and `X` be the associated topos, groupoid and topological space.

**Proposition 9.3.1.** *The categories of locally constant sheaves on `E`, `T`, `G`, `X` as well as the category of
descent data on `E` are equivalent.*

<!-- label: III.X.9.3.1 -->

*Sketch of proof.* Let us denote by (1) through (5) the categories of objects defined in the preceding paragraph.

– (1) ⇔ (5). This is a particular case of [AM69], 10.6 (see also [GZ67], append. I.2.3, [Fri82], ?.5.6, or [Ill72],
VI.8.1.6). An equivalence of categories is given by the functor associating with the object `(E′ → E)` the pair
`(E′_0, α)` where `E′_0` is considered as a sheaf on `E_0` and where `α` is the unique isomorphism
`p_1^∗ E′_0 ⥲ p_2^∗ E′_0` whose fiber at each `y ∈ E_1` — with images denoted `x_1` and `x_2` by the two projections —
is given by the isomorphisms `(E′_0)_{x_1} ← (E′_1)_y → (E′_0)_{x_2}`.

– (5) ⇔ (3). Evident: one of the two relations defining the morphisms in the groupoid `G` associated with `E` is a
cocycle relation.

– (1) ⇔ (4). Cf. [GZ67], append. I.3.2.1.

– (1) ⇔ (2). One must show that an object over `E` is a locally constant sheaf in the simplicial sense if and only if it
is so as a sheaf on `T = E^∼`. This follows from the fact that the locally constant sheaves `F_•` on `T` are nothing
other than the cartesian sheaves, that is, those for which the arrows `([n] → [m])^∗ F_m → F_n` are isomorphisms. This
last point is a particular case of a general fact on simplicial topoi <!-- original page 103 --> together with the fact
that every sheaf on `E^∼_0` is locally constant. (See also [Ill72], VI.8.1.6.) QED.

For every group `H`, the equivalences of categories above induce equivalences between the categories of `H`-torsors,
these being locally constant sheaves equipped with an action of `H`, with fibers isomorphic to `H` acting on itself by
translation.

### 9.4. Fundamental groups and groupoids

It follows from the preceding equivalences of categories that for every group `H` and every simplicial set `E`, the sets
of isomorphism classes of `H`-torsors `H^1(E, H)`, `H^1(E^∼, H)`, `π_0(Hom(Π(E), BH))` and `H^1(|E|, H)` are naturally
in bijection. Recall that one denotes by `BH` the punctual groupoid associated with `H` and by `π_0` the functor
associating with a category the set of isomorphism classes of its objects.

Likewise, if `e` is a point of `E`, the preceding equivalences induce bijections between the sets of isomorphism classes
of `H`-torsors trivialized over `e`, denoted respectively `H^1(E rel e, H)`, `H^1(E^∼ rel e^∼, H)`,
`Hom(π_1(Π(E), e), H)` and `H^1(|E| rel |e|, H)`. Recall that one denotes by `π_1(Π(E), e)` the group
`Isom_{Π(E)}(e, e)`. For variable `H`, these functors are represented, in the connected case, by a group which one
denotes by `π_1(E, e)`. The group `π_1(E, e)` is isomorphic to `π_1(Π(E), e)` and `π_1(|E|, |e|)`, hence also to the
fundamental group of a simplicial set as defined by Kan (cf. e.g. [May67], 16.1 or [Ill72], I.2.1.1). (Recall that the
set `H^1(E, H)` is in turn isomorphic to the set `H^1(π_1(E, e), H)` of morphisms to `H` modulo conjugation, also
denoted `Hom ext(π_1(E, e), H)`.)

### 9.5. Cones

**Definitions 9.5.1.** *(1) Let `f : E′ → E` be a morphism of simplicial sets. Recall (cf. for example [Del74], 6.3.1)
that one denotes by `C(f)` the pointed simplicial set whose underlying set in degree `n ⩾ 0` is*

<!-- label: III.X.9.5.1 -->

```text
E_n ∐ (∐_{i < n} E′_i) ∐ ⋆,
```

*where `⋆` is a singleton. We leave to the reader the task of defining the simplicial maps, the definition of the faces
in rank less than or equal to two being recalled below. (See also [GZ67], VI.2 for a pointed variant.) The category of
locally constant sheaves on `C(f)` is equivalent to the category of locally constant sheaves on `E` equipped with a
trivialization of the inverse image on `E′`. The simplicial set `C(f)` is naturally pointed by `⋆ → C(f)`.*

*(2) Let `f : T′ → T` be a morphism of topoi. Denote by `C(f)` the topos whose objects are quintuples*
`(F, F′, A, α : f^∗ F → F′, β : A → Γ(T′, F′))`, *where `F` (resp. `F′`) is an object of `T` (resp. `T′`), `A` is a set,
and `α` (resp. `β`) is a morphism in `T′` (resp. Ens). (See also [Del80], 4.3.4 and [Ill72], III.4 for a variant of this
construction.) The category of locally constant sheaves on `C(f)` is equivalent to the category of locally constant
sheaves on `T` equipped with a trivialization of* <!-- original page 104 --> *the inverse image on `T′`. The topos
`C(f)` is naturally pointed by the fiber functor sending the quintuple `(F, F′, A, α : f^∗ F → F′, β : A → Γ(T′, F′))`
to the set `A`.*

*(3) Let `f : G′ → G` be a morphism of groupoids. Denote by `C(f)` the colimit of the diagram*

```text
G ← G′ → B_1
```

*where `B_1` is the punctual category (one object, one arrow). The category of locally constant sheaves on `C(f)` is
equivalent to the category of locally constant sheaves on `G` equipped with a trivialization of the inverse image on
`G′`.*

*(4) Let `f : X′ → X` be a morphism of topological spaces. Denote by `C(f)` the colimit of the diagram*

```text
⋆ ← X′ × {0} → X′ × [0, 1] ← X′ × {1} → X.
```

*The category of locally constant sheaves on `C(f)` is equivalent to the category of locally constant sheaves on `X`
equipped with a trivialization of the inverse image on `X′`. The topological space `C(f)` is naturally pointed by
`⋆ → C(f)`.*

#### 9.5.2. Descent data on the cone of a simplicial map

Let `f : E′ → E` be a morphism of simplicial sets and `C(f)` its cone (cf. supra, (1)). Let us use the letter `p` (resp.
`q`, `r`) to denote the face maps of `E′` (resp. `E`, `C(f)`). Before stating the proposition below, let us explicit the
faces `r` in degree less than or equal to two in terms of `p` and `q`. By convention, `p_{ij}` (resp. `p_i`) is the face
map `E′_2 = E′_{\{1,2,3\}} → E′_1 = E′_{\{1,2\}}` (resp. `E′_1 = E′_{\{1,2\}} → E′_0 = E′_{\{1\}}`) corresponding to the
increasing map `\{1, 2\} → \{1, 2, 3\}` (resp. `\{1\} → \{1, 2\}`) of image `\{i, j\}` (resp. `\{i\}`)[^X-9-2]. The same
convention is adopted for the faces of `E` and `C(f)`.

The morphism

```text
r_1 : C(f)_1 = E_1 ∐ E′_0 ∐ ⋆ → C(f)_0 = E_0 ∐ ⋆
```

(resp. `r_2`) is:

– `q_1 : E_1 → E_0` (resp. `q_2 : E_1 → E_0`) on `E_1`;

– `E′_0 → ⋆` (resp. `f_0 : E′_0 → E_0`) on `E′_0`;

– `⋆ → ⋆` on `⋆`.

Likewise the morphism

```text
r_{21} : C(f)_2 = E_2 ∐ E′_1 ∐ E′_0 ∐ ⋆ → C(f)_1 = E_1 ∐ E′_0 ∐ ⋆
```

(resp. `r_{32}`, `r_{31}`) is:

– `q_{21} : E_2 → E_1` (resp. `q_{32}`, `q_{31}`) on `E_2`;

– `p_1 : E′_1 → E′_0` (resp. `f_1 : E′_1 → E_1`, `p_2 : E′_1 → E′_0`) on `E′_1`;

– `E′_0 → ⋆` (resp. `Id : E′_0 → E′_0`, `Id : E′_0 → E′_0`) on `E′_0`.

Let `H` be a descent datum on `C(f)`, that is, a sheaf `H_0` on `C(f)_0 = E_0 ∐ ⋆` equipped with an isomorphism
`γ : r_1^∗ H_0 ⥲ r_2^∗ H_0` between its inverse images on `C(f)_1 = E_1 ∐ E′_0 ∐ ⋆` satisfying the cocycle relation
`r_{31}^∗ γ = r_{32}^∗ γ ∘ r_{21}^∗ γ`.

<!-- original page 105 -->

The restriction of the isomorphism `γ` to `E_1` (resp. `E′_0`) is a descent datum `β : q_1^∗ G_0 ⥲ q_2^∗ G_0` where
`G_0` is the restriction of `H_0` to `E_0` (resp. a trivialization `t : H_0(⋆) ⥲ f^∗ G_0 =: F_0` where `H_0(⋆)` is the
constant sheaf with stalk `H_0(⋆)`). The restriction of the cocycle relation satisfied by `γ` to `E_2` (resp. `E′_1`) is
the cocycle relation for `β` (resp. `p_2^∗(t) = f_1^∗(β) ∘ p_1^∗(t)`). This latter relation means that the
trivialization `t` is compatible with the descent datum `f_1^∗(β)` induced by `β` on `F_0`. From this it follows:

**Proposition 9.5.3.** *Let `f : E′ → E` be a morphism of simplicial sets and `C(f)` its cone, pointed by `⋆`. The
category of descent data on `C(f)` trivialized over `⋆` is equivalent to the category of descent data on `E` equipped
with a trivialization of the descent datum induced on `E′`.*

<!-- label: III.X.9.5.3 -->

### 9.6. Representability of the functor π̄¹(S′/S, ξ; −)

The notations are those of page 90 and from now on we suppose the connected components of `S_0 = S′` and
`S_1 = S′ ×_S S′` open. Under this hypothesis, one has the following explicit combinatorial description, which follows
immediately from the recalls above.

**Proposition 9.6.1.** *For every group `G`, the set `π̄¹(S′/S, ξ; G)` of isomorphism classes of descent data equipped
with a trivialization above `ξ` is in natural bijection with the relative non-abelian cohomology set*

<!-- label: III.X.9.6.1 -->

```text
H^1(K rel k, G) := H^1(K̃ rel ⋆, G).
```

It follows that this functor is representable by a group, denoted `π_1(K, k)` (the "*relative fundamental group*"), as
soon as the simplicial set `K̃ = C(k → K)` is connected. One verifies immediately that this is so if and only if the map
`π_0(k) → π_0(K)` is surjective. It suffices in particular that the simplicial set `K` be connected. As indicated in the
text, this is the case if the scheme `S` is connected and the morphism `S′ → S` is universally submersive.

### 9.7. Contractibility of k, counter-example to the injectivity of k\_• → K\_•

The two following propositions make the N.D.E. (53) more precise.

**Proposition 9.7.1.** *Let `κ` be an algebraically closed field, and `X` a connected `κ`-scheme. For every integer
`i ⩾ 0`, denote by `X_i` the `(i + 1)`-th fibered power of `X` over `κ`. For every integer `i ⩾ 0`, the canonical map*

<!-- label: III.X.9.7.1 -->

```text
π_0(X_i) → π_0(X)^{i+1}
```

*is a bijection. In particular, the simplicial set `π_0(X_•)` is contractible.*

It suffices to prove the following lemma, which follows by passage to the limit from the Künneth formula. [Spell out?]

**Lemma 9.7.2.** *Let `κ` be an algebraically closed field and `X`, `Y` two connected `κ`-schemes. Then the fibered
product `X ×_κ Y` is connected.*

<!-- label: III.X.9.7.2 -->

**Proposition 9.7.3.** *Let `X` be a connected scheme, `X′ → X` a finite étale morphism, and `x` a geometric point of
`X` localized at a point `x`. The canonical morphism `π_0(X′_x) → π_0(X′)` is surjective.*

<!-- label: III.X.9.7.3 -->

<!-- original page 106 -->

Indeed, every connected component of `X′` has image an open-closed of `X` hence meets the fiber `X′_x`. The morphism
`π_0(X′_x) → π_0(X′)` is therefore surjective, as is the morphism `π_0(X^′_x) → π_0(X′_x)`.

## Bibliography

[^X-biblio]

- **[BAC]** N. Bourbaki, *Algèbre commutative*, Chap. I–IV, Hermann, 1961, Masson, 1985, Springer-Verlag, 2006.
- **[BEns]** N. Bourbaki, *Théorie des ensembles*, Chap. I–IV, Hermann, 1970.
- **[Pes66]** C. Peskine, *Une généralisation du « Main Theorem » de Zariski*, Bull. Sci. Math. **90** (1966), 119–127.
- **[PY06]** G. Prasad, J.-K. Yu, *On quasi-reductive group schemes*, J. Alg. Geom. **15** (2006), 507–549.
- **[Ray70]** M. Raynaud, *Anneaux locaux henséliens*, Lect. Notes Maths. **169**, Springer-Verlag, 1970.
- **[AM69]** M. Artin & B. Mazur, *Etale homotopy*, Lect. Notes Maths **100**, Springer, 1969.
- **[Del74]** P. Deligne, *Théorie de Hodge III*, Publ. Math. IHÉS **44** (1974), 5–77.
- **[Del80]** P. Deligne, *La conjecture de Weil II*, Publ. Math. IHÉS **52** (1980), 137–252.
- **[Fri82]** E. M. Friedlander, *Etale homotopy of simplicial schemes*, Princeton Univ. Press, 1982.
- **[GZ67]** P. Gabriel & M. Zisman, *Calculus of fractions and homotopy theory*, Springer, 1967.
- **[Ill72]** L. Illusie, *Complexe cotangent et déformations I & II*, Lect. Notes Maths **239** & **283**, Springer,
    1971 & 1972.
- **[Kan58]** D. Kan, *A combinatorial definition of homotopy groups*, Ann. of Math. **67** (1958), 282–312.
- **[May67]** J. P. May, *Simplicial objects in algebraic topology*, Univ. of Chicago Press, 1967.

<!-- LEDGER DELTA — Exposé X — for consolidation in Phase 3

| French                                     | English                                          | Note                                                                                                                                                                  |
| ------------------------------------------ | ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| revêtement principal                       | principal cover                                  | When `Γ`-Galois cover of a connected base; matches SGA 1, V.                                                                                                          |
| déployé / déploie                          | split / splits                                   | Per N.D.E. (4), the editors replaced "splitté" with "déployé"; we render uniformly as "split".                                                                        |
| à engendrement fini                        | finitely generated                               | Used for a twisted constant commutative group whose type at every point is a finitely generated `ℤ`-module. Not the same as the schematic "of finite type".           |
| fibré principal galoisien                  | Galois principal bundle                          | Principal homogeneous bundle with constant `G_S` structural group.                                                                                                    |
| groupe fondamental élargi                  | enlarged fundamental group                       | Grothendieck's term for the group attached to the full pro-system, not just its finite quotients.                                                                     |
| pro-groupe fondamental élargi              | enlarged fundamental pro-group                   | The projective system `Π = (π_i)_{i ∈ I}` itself.                                                                                                                     |
| anneau hensélisé                           | henselized ring                                  | `A^h`, the inductive limit of étale local neighborhoods of `s` with trivial residue extension.                                                                        |
| critère local de platitude                 | local criterion of flatness                      | Standard EGA terminology.                                                                                                                                             |
| point géométrique                          | geometric point                                  | Spectrum of an algebraically closed field, with a chosen map into `S`.                                                                                                |
| rang abélien / réductif / nilpotent / unipotent | abelian / reductive / nilpotent / unipotent rank | The four numerical invariants of a smooth algebraic group introduced in 8.7.                                                                                          |
| dimension semi-simple                      | semisimple dimension                             | The dimension of `G / radical`, denoted `d_s(G)`.                                                                                                                     |
| théorème principal de Zariski              | Zariski's main theorem                           | Standard. Also rendered "Main Theorem" when the original used English quotes.                                                                                         |
| théorème de quasi-isotrivialité            | quasi-isotriviality theorem                      | The principal theorem of §4 (Theorem 4.4 and Corollary 4.5).                                                                                                          |
| ensemble simplicial pointé                 | pointed simplicial set                           | Per §9.1–9.5.                                                                                                                                                         |
| topos simplicial                           | simplicial topos                                 | Per §9.1.                                                                                                                                                             |
| réalisation géométrique                    | geometric realization                            | Standard.                                                                                                                                                             |
| groupoïde ponctuel                         | punctual groupoid                                | A groupoid with one object and one automorphism group `H`; `BH` notation.                                                                                             |
| cocycle                                    | cocycle                                          | In descent data.                                                                                                                                                      |
| données de descente                        | descent data                                     | Standard.                                                                                                                                                             |
| morphisme universellement submersif         | universally submersive morphism                  | Per SGA 1, IV 2.1.                                                                                                                                                    |
| données de descente effective              | effective descent datum                          | Standard.                                                                                                                                                             |
| « partie finie »                            | "finite part"                                    | Per the decomposition `(∗)` in the proof of 4.3.                                                                                                                      |
| caractérisation                            | characterization                                 | Per Exposé title.                                                                                                                                                     |
| classification                             | classification                                   | Per Exposé title.                                                                                                                                                     |
-->

[^X-0-0]: Version xy of 6 November 2009: Addenda placed in Section 9, reviewed through 8.8.

[^N.D.E-X-1]: *N.D.E.* More precisely, this follows from the "axiomatic conditions of a Galois theory", cf. SGA 1, V N°
    4 g); when `S` is locally noetherian, the verification of the axioms is done in *loc. cit.*, N°s 7 & 3, in
    particular 3.7, which rests on SGA 1, I 10.9. This last result is proved, without noetherian hypotheses,
    in EGA IV₄, 18.2.9.

[^N.D.E-X-2]: *N.D.E.* In the sequel, one will say that an `S`-group of multiplicative type is "split" if it is
    "trivial" in the sense of IX 1.2, i.e., if it is a diagonalizable `S`-group.

[^N.D.E-X-3]: *N.D.E.* One has corrected `S` to `S′`.

[^N.D.E-X-4]: *N.D.E.* One has replaced, here and in the sequel, "splittés" by "déployés", "splitte" by "déploie", etc.
    (In English: "split".)

[^N.D.E-X-5]: *N.D.E.* See 7.3 below.

[^N.D.E-X-6]: *N.D.E.* One has added this "recall", for later references.

[^N.D.E-X-7]: *N.D.E.* One has corrected the original by exchanging `M` and `N` in the right-hand terms.

[^X-2-1]: Cf. J. Giraud, *Méthode de la descente*, Bull. Soc. Math. France, Mémoire 2 (1964).

[^N.D.E-X-8]: *N.D.E.* One recalls that 2.3 is used to prove Theorem IX 3.6 bis.

[^N.D.E-X-9]: *N.D.E.* Since `u_0` is an isomorphism, it suffices to see that for every `h ∈ H`, the morphism
    `φ : O_{G,u(h)} → O_{H,h}` is bijective. It is so by reduction modulo `I = I_s` (where `s` is the image of
    `h` in `S`), so its cokernel `C` verifies `C = IC`, whence `C = 0` since `I` is nilpotent. Then, since
    `O_{H,h}` is flat over `O_{S,s}`, the kernel `K` of `φ` also verifies `K = IK`, whence `K = 0`.

[^N.D.E-X-10]: *N.D.E.* One has rewritten the statement keeping only the non-trivial implication, to bring it into
    focus.

[^N.D.E-X-11]: *N.D.E.* Spell out this point ….

[^N.D.E-X-12]: *N.D.E.* One has spelled out the original in what follows.

[^N.D.E-X-13]: *N.D.E.* Specify this reference, possibly adding a corollary in N° 5 ….

[^X-3-1]: Cf. also VI_B 2.5 for more systematic developments of this nature.

[^N.D.E-X-14]: *N.D.E.* Specify these references: Since `G`, `H` are locally of finite presentation, `u` is locally of
    finite presentation (IV₁, 1.4.3 (v)); next one applies IV₃, 11.3.10 and 13.1.4 for flat and quasi-finite,
    IV₄, 17.4.1, 17.5.1 and 17.6.1 for unramified, smooth and étale; compare with VI_B 2.5.

[^N.D.E-X-15]: *N.D.E.* One has added the following sentence.

[^N.D.E-X-16]: *N.D.E.* One has added the following sentence.

[^N.D.E-X-17]: *N.D.E.* Cf. EGA IV₄, 17.9.1.

[^N.D.E-X-18]: *N.D.E.* The original indicated: "i.e. `S_0` connected". Note that, since `A` is separated for the
    `I`-adic topology, `S_0` meets every connected component of `S` (and since `A` is complete, the connected
    components of `S_0` and `S` are in bijection).

[^N.D.E-X-19]: *N.D.E.* since `G_s` and `H_s` are of the same type for every `s ∈ S_0`, hence for every `s`.

[^N.D.E-X-20]: *N.D.E.* because `u` will once again be a surjective open immersion.

[^N.D.E-X-21]: *N.D.E.* One has spelled out this recall, and added remark 4.0.1.

[^N.D.E-X-22]: *N.D.E.* One has added what follows.

[^N.D.E-X-23]: *N.D.E.* One has spelled out the original in what follows.

[^N.D.E-X-24]: *N.D.E.* One has added this recall, used in the proof of 4.3 (the reference to EGA IV₄ 18.5.11 not being
    fully satisfactory).

[^N.D.E-X-25]: *N.D.E.* One has spelled out the original in what follows, on the basis of indications by M. Raynaud.

[^N.D.E-X-26]: *N.D.E.* One has added this lemma, used several times in the sequel.

[^N.D.E-X-27]: *N.D.E.* One has spelled out the reductions that follow (the original indicated: "One reduces at once to
    the case where `S` is the spectrum of a noetherian local ring `A`, and where `s` is the closed point of
    `S`.").

[^X-4-1]: Or EGA IV₄, § 18.6.

[^N.D.E-X-28]: *N.D.E.* One has spelled out the original in what precedes and what follows.

[^N.D.E-X-29]: *N.D.E.* This result is generalized in 8.1: it suffices in fact to suppose that the fibers of `H` are
    affine and connected.

[^N.D.E-X-30]: *N.D.E.* See lemma 5.12 below.

[^N.D.E-X-31]: *N.D.E.* One has moved this remark here, appearing in the original after the proof.

[^N.D.E-X-32]: *N.D.E.* cf. VIII § 1.7.

[^N.D.E-X-33]: *N.D.E.* One has corrected "equivalence" to "anti-equivalence".

[^N.D.E-X-34]: *N.D.E.* (when `S′` is locally noetherian, and EGA IV₃, 8.11.2 in general).

[^N.D.E-X-35]: *N.D.E.* (when `S′` is locally noetherian, and EGA IV₂, 2.4.6 in general).

[^N.D.E-X-36]: *N.D.E.* One has corrected `H` to `G`.

[^N.D.E-X-37]: *N.D.E.* One has added what follows.

[^N.D.E-X-38]: *N.D.E.* Correct this reference by treating the case of the functor `Isom_{S-gr.}(H, G)` in an addition
    1.5.1 in VIII ….

[^N.D.E-X-39]: *N.D.E.* One has added this recall, used several times in the sequel. (See also EGA I, 6.1.9; note
    however that the proof of *loc. cit.* seems unnecessarily complicated.)

[^N.D.E-X-40]: *N.D.E.* Compare with the examples of 1.6 ….

[^N.D.E-X-41]: *N.D.E.* One has spelled out the original in what follows.

[^N.D.E-X-42]: *N.D.E.* because it is a twisted constant group of type `End_{gr.}(N)` (cf. 5.6 and 5.8).

[^N.D.E-X-43]: *N.D.E.* modulo the verification that (ii) ⇒ (i) when `S` is locally noetherian and `R` is not finitely
    generated ….

[^N.D.E-X-44]: *N.D.E.* Spell out this point: `M` being a finitely generated `ℤ`-module, it is countable, and the proof
    of 5.11 (i) ⇒ (ii) shows that `R` is the union of a countable family of open and closed parts, finite
    over `S`. One would need to see the converse ….

[^N.D.E-X-45]: *N.D.E.* The original treated in 5.14 the case where `S` is locally noetherian and normal, and signalled
    in Remark 5.15 that the reasoning applies, more generally, if one supposes only `S` geometrically
    unibranch instead of normal. One has modified the statement of 5.14 (and also 5.16) accordingly, and one
    has added these "recalls", drawn from EGA IV₄, 18.10.6 and 18.10.7, which show that the proof of 5.14
    applies verbatim to the geometrically unibranch case.

[^N.D.E-X-46]: *N.D.E.* One has removed remark 5.15, rendered obsolete by the addition of 5.14.0 (cf. the preceding
    N.D.E.), and in 5.16 one has replaced "normal" by "geometrically unibranch".

[^N.D.E-X-47]: *N.D.E.* Note that `P` is supposed to be a prescheme — in the *a priori* more general case of a sheaf
    (fpqc) `P` which is a `G_S`-torsor, is `P` necessarily representable?

[^N.D.E-X-48]: *N.D.E.* One has added the hypothesis that the connected components of `S′` be open, as well as the
    second hypothesis. This latter means that the simplicial set `K_• = π_0(S_•)` defined in 6.3 is
    connected; in fact a weaker hypothesis suffices, namely that the cone `K̃_•` of a certain morphism of
    simplicial sets `k_• → K_•` be connected (cf. *loc. cit.*).

[^N.D.E-X-49]: *N.D.E.* One has suppressed the superfluous hypothesis that the connected components of `S‴` be open. On
    the other hand, the description given later (cf. …) gives as the natural set of generators the set
    `π_0(S″) ∐ π_0(S′_ξ)`; one then reduces to `π_0(S″)` by means of the relations between these generators
    arising from the 2-cells. See for example [Kan58], § 19 for a finer description.

[^N.D.E-X-50]: *N.D.E.* One could spell out this deduction; `I` is in bijection with a cofinal set of morphisms `S′ → S`
    covering for the étale topology ….

[^N.D.E-X-51]: *N.D.E.* One has corrected 5.13 to 5.14.

[^N.D.E-X-52]: *N.D.E.* Some authors speak of the "true" fundamental group.

[^N.D.E-X-53]: *N.D.E.* One has corrected the original, which considers `K̃_• = K_•/k_•` whereas on the one hand `k_•`
    is already contractible (cf. 9.7.1) and on the other hand the morphism `k_• → K_•` is not in general
    injective. It is an epimorphism if `S′/S` is étale finite (cf. 9.7.3).

[^N.D.E-X-54]: *N.D.E.* One has added the hypothesis that `K̃_•` be connected; for the proof, see the addendum below
    (Section 9).

[^N.D.E-X-55]: *N.D.E.* One has modified the sequel, taking into account the correction made above, cf. N.D.E. (53).
    (The original was: "`π_0(K̃_•, ξ̃)` is also canonically isomorphic to the set `π_0(S, ξ)` of connected
    components of `S`, pointed by the connected component of `ξ` in `S`".)

[^N.D.E-X-56]: *N.D.E.* One could spell this out: first, taking into account 5.14, the enlarged fundamental group of the
    projective line `P¹_k` is zero, i.e. `P¹_k` is "truly" simply connected. Next, one would have to extend
    to the case of the enlarged fundamental group and the category of principal bundles (not necessarily
    finite), Corollary 5.4 of SGA 1 IX and the discussion that follows. (Let `Γ_1` and `Γ_2` be two copies of
    `P¹_k`, `a_i`, `b_i` two distinct points of `Γ_i`, `C″_2` the disjoint union of `Γ_1` and `Γ_2`, `C′_2`
    the curve obtained by identifying `a_1` with `a_2`; then `C_2` is obtained from `C′_2` by additionally
    identifying `b_1` with `b_2`. The discussion following *loc. cit.*, extended to the enlarged case, then
    shows that the enlarged fundamental group of `C′_2` (resp. `C_2`) is zero (resp. `ℤ`).

[^N.D.E-X-57]: *N.D.E.* This is an `n`-fold point with `n` distinct tangents, for example the curve
    `X^n − Y^n = X^{n+1}`.

[^N.D.E-X-58]: *N.D.E.* In particular, this shows that the tori of relative dimension 2 considered in 1.6 are not
    isotrivial.

[^N.D.E-X-59]: *N.D.E.* Note that the hypotheses entail that `H` is separated over `S`, by VI_B, Th. 5.3 or Cor. 5.5.

[^N.D.E-X-60]: *N.D.E.* by EGA IV₂, 8.8.2 again.

[^N.D.E-X-61]: *N.D.E.* One has spelled out the original in what follows.

[^X-8-1]: By Raynaud's theorem VI_B 5.3.

[^N.D.E-X-62]: *N.D.E.* Spell out this point, in connection with the modifications in VI_B § 5.

[^N.D.E-X-63]: *N.D.E.* This follows, for example, from VIII 3.2 a); more generally, if `f : G → H` is a surjective
    morphism of algebraic groups over a field `k` and if `H` is reduced, then `f` is flat (cf. VI_B 1.3).

[^N.D.E-X-64]: *N.D.E.* One has spelled out the original in what follows.

[^N.D.E-X-65]: *N.D.E.* At least in the case envisaged so far, namely `S` locally noetherian.

[^N.D.E-X-66]: *N.D.E.* The editors did not understand this remark, not understanding why `u` would *a priori* have
    finite fibers and be surjective ….

[^N.D.E-X-67]: *N.D.E.* Spell out this reduction ….

[^N.D.E-X-68]: *N.D.E.* Spell out this point ….

[^N.D.E-X-69]: *N.D.E.* Give a reference here?

[^N.D.E-X-70]: *N.D.E.* Recall the definition of "Cartan subgroup" ….

[^N.D.E-X-71]: *N.D.E.* Give a reference for these results?

[^N.D.E-X-72]: *N.D.E.* G. Prasad and J.-K. Yu have generalized (subject to some additional hypotheses) this result
    without supposing `G` commutative and replacing in hypothesis a) and the conclusion "torus" by "reductive
    group", cf. [PY06], Th. 6.2.

[^X-8-2]: By Raynaud's theorem VI_B 5.3.

[^N.D.E-X-73]: *N.D.E.* cf. N.D.E. (62) in 8.5.

[^N.D.E-X-74]: *N.D.E.* revise the preceding sentence ….

[^N.D.E-X-75]: *N.D.E.* This additional section was written by Fabrice Orgogozo (following indications by Ofer Gabber).

[^X-9-1]: PP: I have replaced "FGA, *Technique de descente* I, 1.6" by "Exp. IV, 2.1".

[^X-9-2]: This convention departs from the current simplicial norm but is closer to the notations used by Grothendieck
    in his theory of descent.

[^X-biblio]: *N.D.E.* additional references cited in this Exposé; the references [AM69] and following concern the
    Addenda.
