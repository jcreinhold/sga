# Exposé II. Smooth Morphisms: Generalities, Differential Properties

<!-- label: II -->

<!-- original page 29 -->

References to Exposé I are indicated by I. Recall that rings are noetherian, and preschemes locally noetherian.

## 1. Generalities

<!-- label: II.1 -->

Let `Y` be a prescheme, and let `t₁,...,t_n` be indeterminates. Put

```text
Y[t₁,...,t_n] = Y ⊗_ℤ ℤ[t₁,...,t_n].
```

<!-- label: eq:II.1.1 -->

Thus `Y[t₁,...,t_n]` is a `Y`-scheme, affine over `Y`, defined by the quasi-coherent sheaf of algebras
`𝒪_Y[t₁,...,t_n]`. Giving a section of this prescheme over `Y` is therefore equivalent to giving `n` sections of `𝒪_Y`,
corresponding to the images of the `t_i` under the corresponding homomorphism. If `Y′` is over `Y`, one has

```text
Y[t₁,...,t_n] ×_Y Y′ = Y′[t₁,...,t_n],
```

<!-- label: eq:II.1.2 -->

which implies that giving a `Y`-morphism from `Y′` to `Y[t₁,...,t_n]` is equivalent to giving `n` sections of `𝒪_{Y′}`.
On the other hand, one has

```text
(Y[t₁,...,t_n])[t_{n+1},...,t_m] = Y[t₁,...,t_m],
```

<!-- label: eq:II.1.3 -->

by the analogous formula for polynomial rings over `ℤ`. Formula II.1.2 implies that `Y[t₁,...,t_n]` varies functorially
with `Y`.

The prescheme `Y[t₁,...,t_n]` is of finite type and flat over `Y`.

**Definition.**

<!-- label: II.1.1 -->

Let `f: X → Y` be a morphism, making `X` into a `Y`-prescheme. One says that `f` is smooth[^II-1-1] at `x ∈ X`, or that
`X` is smooth over `Y` at `x`, if there exist an integer `n ≥ 0`, an open neighborhood `U` of `x`, and an étale
`Y`-morphism from `U` to `Y[t₁,...,t_n]`. One says that `f`, respectively `X`, is smooth if it is smooth at all points
of `X`. An algebra `B` over a ring `A` is said to be smooth at a prime ideal `𝔭` of `B` if `Spec(B)` is smooth over
`Spec(A)` at the point `𝔭`.

<!-- original page 30 -->

The algebra `B` is said to be smooth over `A` if it is smooth over `A` at every prime ideal `𝔭` of `B`. Finally, a local
homomorphism `A → B` of local rings is said to be smooth, or `B` is said to be smooth over `A`,[^II-1-2] if `B` is a
localization of an algebra of finite type `B₁` smooth over `A`.

Note that the notion of smoothness of `X` over `Y` is local on `X` and on `Y`. If `X` is smooth over `Y`, it is locally
of finite type over `Y`.

**Proposition.**

<!-- label: prop:II.1.1 -->

The set of points `x` of `X` at which `f` is smooth is open.

This is trivial from the definition.

**Corollary.**

<!-- label: II.1.2 -->

If `B` is smooth over `A` at `𝔭`, then it is smooth over `A` at every prime ideal `𝔮` of `B` contained in `𝔭`.

Proposition II.1.1 also implies that the last two definitions II.1.1 coincide on their common domain of existence.

**Proposition.**

<!-- label: II.1.3 -->

1. An étale morphism, in particular an open immersion or an identity morphism, is smooth.
1. Base extension in a smooth morphism gives a smooth morphism.
1. The composite of two smooth morphisms is smooth.

Statement (i) is trivial from the definition; more precisely, one has:

**Corollary.**

<!-- label: II.1.4 -->

étale = quasi-finite + smooth.

Statement (ii) follows immediately from the analogous fact for étale morphisms (I 4.6) and for the projections
`Y[t₁,...,t_n] → Y`; cf. II.1.2. For (iii), it follows formally from the fact that this is separately true for “étale”
(I 4.6) and for projections of the type `Y[t₁,...,t_n] → Y`, cf. II.1.3, together with the two facts cited for (ii).

Suppose `Y` is smooth over `Z` and `X` smooth over `Y`; prove that `X` is smooth over `Z`. We may suppose `Y` is étale
over `Z[t₁,...,t_n]` and `X` is étale over `Y[s₁,...,s_m]`. The first hypothesis therefore implies that `Y[s₁,...,s_m]`
is étale over `Z[t₁,...,t_n][s₁,...,s_m] = Z[t₁,...,s_m]`. Hence `X` is étale over `Z[t₁,...,s_m]`, as required.

**Remark.**

<!-- label: II.1.5 -->

The integer `n` appearing in Definition II.1.1 is well determined, since one checks immediately

<!-- original page 31 -->

that it is the dimension of the local ring of `x` in its fiber `f⁻¹(f(x))`. It is called the relative dimension of `X`
over `Y`. It behaves additively under composition of morphisms.

## 2. Some Smoothness Criteria for a Morphism

<!-- label: II.2 -->

**Theorem.**

<!-- label: II.2.1 -->

Let `f: X → Y` be a morphism locally of finite type, let `x ∈ X`, and let `y = f(x)`. For `f` to be smooth at `x`, it is
necessary and sufficient that (a) `f` be flat at `x`, and (b) `f⁻¹(y)` be smooth over `κ(y)` at `x`.

Since the composite of two flat morphisms is flat, and `Y[t₁,...,t_n] → Y` is flat, one sees that smooth implies flat.
Taking II.1.3(ii) into account, this proves necessity.

Suppose (a) and (b) verified. Let `V` be an affine neighborhood of `y` with ring `A`, and `U` an affine neighborhood of
`x` over `V`, with ring `B`. Taking `U` small enough, we may suppose by (b) that there exists an étale `κ(y)`-morphism

```text
g: U|f⁻¹(y) → Spec k[t₁,...,t_n],     k = κ(y),
```

defined by `n` sections `g_i` of the structural sheaf of `U|f⁻¹(y)`. One checks easily that one may suppose the `g_i`,
which a priori are elements of `B ⊗_A k = BS⁻¹`, where `S = A − 𝔭` and `𝔭` is the prime ideal of `A` corresponding to
`y`, come from sections of the structural sheaf of `U`. Thus `g` is induced by a morphism, still denoted `g`,

```text
g: U → Y[t₁,...,t_n],
```

after multiplying the `g_i` by a common nonzero element of `k` if necessary. Now `U` is flat over `Y` by (a), as is
`Y[t₁,...,t_n]`; on the other hand, `g` induces an étale morphism between the fibers over `y`. Hence `g` is étale at `x`
by I 5.8. This proves the assertion.

**Corollary.**

<!-- label: II.2.2 -->

Let `S` be a prescheme, let `f: X → Y` be an `S`-morphism of finite type, with `Y` of finite type and flat over `S`, let
`x ∈ X`, and let `s` be the projection of `x` to `S`. For `f` to be smooth at `x`, it is necessary and sufficient that
`X` be flat, or equivalently smooth, over `S` at `x`, and that the morphism `f_s: X_s → Y_s` induced on the fibers of
`s` be smooth at `x`.

Only sufficiency requires proof, and it follows from criterion II.2.1 together with the flatness criterion I 5.9.

<!-- original page 32 -->

To state the following result, “recall” that a morphism `f: X → Y` locally of finite type is said to be equidimensional
at the point `x ∈ X` if, putting `y = f(x)`, one can find an open neighborhood `U` of `x`, every component of which
dominates a component of `Y`, such that, for every `y′ ∈ Y`, the irreducible components of `f⁻¹(y′) ∩ U` all have the
same dimension independent of `y′`. In this condition it is enough, moreover, to take `y′` to be the generic points of
the irreducible components of `Y` passing through `y`, and the point `y` itself.

If, for example, `X` and `Y` are integral and `f` is dominant, the condition means that the components of `f⁻¹(y)`
passing through `x` have the “right” dimension, i.e. the dimension of the generic fiber; recall that they are always at
least the dimension of the generic fiber. If `f` is equidimensional at `x`, the dimension of its fiber at `x` being `n`,
and if `g: U → Y′ = Y[t₁,...,t_n]` is a `Y`-morphism from a neighborhood `U` of `x`, inducing on the fibers of `y` a
morphism that is quasi-finite at `x`, or equivalently if `g` is quasi-finite at `x`, then one shows that every
irreducible component of `U` passing through `x` dominates an irreducible component of `Y′`. Moreover, by the
“normalization lemma”, such a `g` always exists. Conversely, if there exists a quasi-finite `Y`-morphism `g` from an
open neighborhood `U` of `x` into a `Y`-scheme of the form `Y′ = Y[t₁,...,t_n]`, such that every component of `U`
passing through `x` dominates a component of `Y′`, then `f` is equidimensional at `x`. This said:

**Proposition.**

<!-- label: II.2.3 -->

Let `f: X → Y` be a morphism locally of finite type, let `x` be a point of `X`, and let `y = f(x)`. Suppose `𝒪_y` is
normal. For `f` to be smooth at `x`, it is necessary and sufficient that `f` be equidimensional at `x` and that `f⁻¹(y)`
be smooth over `κ(y)` at `x`.

One sees immediately from the definition that a smooth morphism is equidimensional. Note that a flat morphism of finite
type is not necessarily equidimensional at `x`, even if its fiber at `x` is irreducible. Let us prove the converse.
Since `f⁻¹(y)` is smooth over `κ(y)` at `x`, we may suppose, replacing `X` if necessary by a suitable neighborhood of
`x`, that there exists a `Y`-morphism

```text
g: X → Y[t₁,...,t_n] = Y′
```

inducing an étale morphism on the fibers of `y`, and a fortiori quasi-finite at `x`.

<!-- original page 33 -->

Thus `g` is unramified, and since `f` is equidimensional at `x`, the irreducible components of `X` passing through `x`
each dominate a component of `Y′`. A fortiori the homomorphism `𝒪_{y′} → 𝒪_x` deduced from `g`, where `y′ = g(x)`, is
injective. This homomorphism is moreover unramified, and `𝒪_{y′}` is normal, since it is a localization of the ring
`𝒪_y[t₁,...,t_n]`, which is normal because `𝒪_y` is. Thus the homomorphism `𝒪_{y′} → 𝒪_x` is étale by I 9.5(ii).

**Remarks.**

<!-- label: II.2.4 -->

The preceding statement remains valid if one replaces the hypothesis that `𝒪_y` is normal by the weaker hypothesis that
`Y` is geometrically unibranch at `y`, cf. I 11, since I 9.5 is valid under this hypothesis. Let us take the occasion to
point out at the same time that if the residue field of an integral local ring `A` is algebraically closed, then
analytically integral, i.e. `Â` is integral, implies geometrically unibranch. The converse is moreover true in every
category of “good rings”, more precisely in a category of rings stable under the usual operations and in which the
completion of a normal local ring is normal; this condition is fulfilled, by Zariski’s “analytic normality theorem”, in
the category of affine algebras and their localizations.[^II-2-1]

Finally, “recall” in the present context the following result, due to Hironaka,[^II-2-2] which sometimes makes it
possible to ensure that `f⁻¹(y)` is a reduced scheme, i.e. that it is also what many algebraic geometers would abusively
regard as the fiber without multiplicity of `f` over `x`, namely `f⁻¹(y)_red`:

**Proposition.**

<!-- label: II.2.5 -->

Let `f: X → Y` be a dominant morphism of finite type of reduced preschemes, and let `y` be a point of `Y` such that
`𝒪_y` is regular. Suppose that all components of `f⁻¹(y)` have multiplicity 1, cf. definition below, and that
`f⁻¹(y)_red` is normal. Then `f⁻¹(y)` is reduced, hence normal; `X` is normal at all points of `f⁻¹(y)`; and finally `X`
is flat over `Y` at all points of `f⁻¹(y)`.

<!-- original page 34 -->

One says that a component `Z` of `f⁻¹(y)` has multiplicity 1 if, with `x` denoting the generic point of `Z`, one has:
(i) `dim 𝒪_x = dim 𝒪_y`, i.e. `Z` is not an “excess component”, in other words is not “of too large a dimension”; (ii)
the maximal ideal of `𝒪_x` is generated by the maximal ideal of `𝒪_y`, which a priori, by the choice of `x`, generates
an ideal of definition of `𝒪_x`.

Taking II.2.3 or II.2.1 into account, one obtains:

**Corollary.**

<!-- label: II.2.6 -->

Let `f: X → Y` be a dominant morphism of finite type of reduced preschemes, and let `y` be a point of `Y` such that
`𝒪_y` is regular. For `f` to be smooth at the points of `X` above `y`, it is necessary and sufficient that the
components of `f⁻¹(y)` have multiplicity 1 and that `f⁻¹(y)_red` be smooth over `κ(y)`.

This situation was considered especially in the past when `Y` was the spectrum of a discrete valuation ring `A`, and was
commonly designated by phrases such as: “if the reduction of `X` with respect to the given valuation is pretty”...
Moreover, `X` then denoted a closed subscheme, if one may say so, of a `ℙⁿ_K`, where `K` is the field of fractions of
`A`, and for lack of an adequate language, the more intrinsic role of an object “defined over `A`”, and not only over
`K`, hardly appeared.

## 3. Permanence Properties

<!-- label: II.3 -->

**Proposition.**

<!-- label: II.3.1 -->

Let `f: X → Y` be a morphism, let `x ∈ X`, and let `y = f(x)`. Suppose `f` is smooth at `x`. For `𝒪_x` to be reduced,
respectively regular, respectively normal, it is necessary and sufficient that `𝒪_y` be so.

This statement is indeed known when `X` is of the form `Y[t₁,...,t_n]`, and it was proved in I, no. I.9 for an étale
morphism; the general case follows at once by Definition II.1.1.

We do not detail here the other permanence properties, which already follow from flatness alone, or from the fact that
`X` is locally quasi-finite and flat over a `Y`-prescheme of the form `Y[t₁,...,t_n]`, or, as we shall say,

<!-- original page 35 -->

that `X` is Cohen-Macaulay over `Y`. Let us only point out that from this latter fact one obtains

```text
dim 𝒪_x = dim 𝒪_y + n − d,
depth 𝒪_x = depth 𝒪_y + n − d,
```

<!-- label: eq:II.3.1 -->

where `n` is the dimension of the fiber of `f` at `x`, and `d` is the transcendence degree of `κ(x)` over `κ(y)`. Hence,
putting `codepth = dim − depth`,[^II-3-1]

```text
codepth 𝒪_x = codepth 𝒪_y.
```

<!-- label: eq:II.3.2 -->

It follows, for example, that `𝒪_x` is Cohen-Macaulay, respectively has no embedded components, if and only if the same
is true of `𝒪_y`.

## 4. Differential Properties of Smooth Morphisms

<!-- label: II.4 -->

For simplicity, we shall restrict ourselves essentially to differential calculus of order 1, limiting ourselves to rapid
indications for higher order, where the results are just as simple.

For the definition of the sheaf `Ω¹_{X/Y}` of 1-differentials of a `Y`-prescheme `X`, cf. I no. I.1. Suppose `X` and `Y`
are `S`-preschemes, with structural morphism `f: X → Y` an `S`-morphism. Then `f` defines a homomorphism of modules,
compatible with `f`,

```text
f*: Ω¹_{Y/S} → Ω¹_{X/S}.
```

<!-- label: eq:II.4.1 -->

In other words, `Ω¹_{X/S}` is contravariant in the `S`-prescheme `X`. Moreover II.4.1 is equivalent to a homomorphism of
modules on `X`,

```text
f*(Ω¹_{Y/S}) → Ω¹_{X/S},
```

<!-- label: eq:II.4.1bis -->

also denoted `f*` for lack of anything better, and fitting into a canonical exact sequence of module homomorphisms

```text
f*(Ω¹_{Y/S}) → Ω¹_{X/S} → Ω¹_{X/Y} → 0.
```

<!-- label: eq:II.4.2 -->

All these homomorphisms are defined by the condition of being local in nature, which reduces to the affine case, and of
commuting with the operators `d`. The exactness of II.4.2 is classical and trivial, and in the affine case it is
transcribed as the exact sequence corresponding to a homomorphism `B → C` of `A`-algebras:

```text
Ω¹_{B/A} ⊗_B C → Ω¹_{C/A} → Ω¹_{C/B} → 0.
```

<!-- label: eq:II.4.2bis -->

**Lemma.**

<!-- label: II.4.1 -->

<!-- original page 36 -->

Let `f: X → Y` be a morphism of `S`-preschemes. If `f` is unramified, respectively étale, then

```text
f*(Ω¹_{Y/S}) → Ω¹_{X/S}
```

is surjective, respectively an isomorphism. The converse is true in the unramified case, if `f` is assumed locally of
finite type.

The unramified case follows from the exact sequence II.4.2 and from I 3.1, but can also be seen directly as in the étale
case. Consider the diagram

```text
X → X ×_Y X → X ×_S X
    ↓           ↓
    Y →       Y ×_S Y
```

in which `X ×_Y X` identifies with the fiber product of `Y` and `X ×_S X` over `Y ×_S Y`. Since `f` is unramified,
`X → X ×_Y X` is an open immersion; hence the “conormal” sheaf of the composite immersion `Δ_{X/S}` of the latter with
`X ×_Y X → X ×_S X` is isomorphic to the inverse image on `X` of the conormal sheaf for the immersion
`X ×_Y X → X ×_S X`. On the other hand, since `X → Y` is étale, hence flat, `X ×_S X → Y ×_S Y` is flat. Thus the
conormal sheaf for the immersion `X ×_Y X → X ×_S X` is isomorphic to the inverse image of the conormal sheaf for the
immersion `Y → Y ×_S Y`, i.e. the inverse image of `Ω¹_{Y/S}`. The conclusion follows.

**Lemma.**

<!-- label: II.4.2 -->

Let `X = Y[t₁,...,t_n]`, with `Y` an `S`-prescheme. Then the sequence of canonical homomorphisms

```text
0 → f*(Ω¹_{Y/S}) → Ω¹_{X/S} → Ω¹_{X/Y} → 0
```

is exact, and `Ω¹_{X/Y}` is free with basis `d_{X/Y}t_i`.

The verification, purely affine, is immediate. Note that we already know the exactness of II.4.2.

Combining these two statements and Definition II.1.1, one finds:

**Theorem.**

<!-- label: II.4.3 -->

Let `f: X → Y` be a smooth morphism of `S`-preschemes. Then:

1. The sequence of canonical homomorphisms

```text
0 → f*(Ω¹_{Y/S}) → Ω¹_{X/S} → Ω¹_{X/Y} → 0
```

is exact. 2. `Ω¹_{X/Y}` is locally free, and its rank `n` at `x` is equal to the relative dimension of `f` at `x`.

**Corollary.**

<!-- label: II.4.4 -->

<!-- original page 37 -->

The homomorphism

```text
f*(Ω¹_{Y/S}) → Ω¹_{X/S}
```

is injective; its image in `Ω¹_{X/S}` is locally a direct factor.

Let `u: F → G` be a homomorphism of modules on the prescheme `X`. We say that it is **universally injective** at `x ∈ X`
if the homomorphism `F_x → G_x` of `𝒪_x`-modules is injective and remains so after tensoring with every `𝒪_x`-algebra,
or equivalently with every `𝒪_x`-module. It is enough, for example, that there exist an open neighborhood `U` of `x`
such that `u` induces an isomorphism from `F|U` onto a direct factor of `G|U`. This condition is also necessary when `F`
and `G` are free, of finite type, in a neighborhood of `x`. More precisely, in that case the following conditions are
equivalent:

1. `u` is injective at `x` and `Coker u` is free at `x`.
1. There is an open neighborhood `U` of `x` such that `u` induces an isomorphism from `F|U` onto a direct factor of
    `G|U`.
1. `u` is universally injective at `x`.
1. The induced homomorphism on the restricted fibers

```text
F_x ⊗ κ(x) → G_x ⊗ κ(x)
```

is injective. 5. The transposed homomorphism `Ǧ → F̌` is surjective at the point `x`, or equivalently in a neighborhood
of `x`.

For the circular proof, (iv) ⇒ (v) follows from Nakayama, and (v) ⇒ (i) because a locally free quotient sheaf is
necessarily a direct factor. Geometrically, the situation considered means that `u` corresponds to an isomorphism from
the vector bundle whose sheaf of sections is `F` onto a sub-bundle of the analogous vector bundle defined by `G`. Of
course it is not enough for this that `F → G` be injective.

**Corollary.**

<!-- label: II.4.5 -->

Let `f: X → Y` be a morphism of `S`-preschemes, locally of finite type; let `x ∈ X`, `y = f(x)`, and let `s` be the
image of `x` and `y` in `S`. Suppose that `Y` is smooth at `y` over `S`. The following conditions are equivalent:

1. `f` is smooth at `x`.
1. `X` is smooth over `S` at `x`, and

```text
f*(Ω¹_{Y/S}) → Ω¹_{X/S}
```

is universally injective at `x`, i.e. it is an injective homomorphism at `x` and its cokernel `Ω¹_{X/Y}` is free at `x`.

The necessity follows from II.1.3 (iii) and II.4.3 (i), (ii). We prove the sufficiency. Since the `d g`, with `g ∈ 𝒪_x`,
generate the module `Ω¹_{X/Y}` at `x`, one can find `g_i`, `1 ≤ i ≤ n`, such that the images of the `d g_i` in
`(Ω¹_{X/Y})_x` form a basis of this module. Taking `X` small enough, we may suppose that the `g_i` come from sections of
`𝒪_X`, and therefore define a `Y`-morphism

```text
g: X → Y′ = Y[t₁,...,t_n].
```

Using the hypothesis and Lemma II.4.2, one easily sees that the corresponding homomorphism

```text
g*(Ω¹_{Y′/S}) → Ω¹_{X/S}
```

is bijective at `x`. This reduces us to proving the following statement.

**Corollary.**

<!-- label: II.4.6 -->

Let `f: X → Y` be a morphism of smooth `S`-preschemes. In order that `f` be étale at `x ∈ X`, it is necessary and
sufficient that

```text
f*(Ω¹_{Y/S}) → Ω¹_{X/S}
```

be an isomorphism at `x`.

We know by II.4.1 that this is necessary, and the same lemma implies that this condition makes `f` unramified at `x`. By
II.2.2, we are reduced to the case `S = Spec(k)`. Since `Y` is smooth over `k`, it is regular, hence a fortiori normal,
and by I.9.5 (ii) we are reduced to proving that `𝒪_y → 𝒪_x` is injective, or again that `𝒪_y` and `𝒪_x` have the same
dimension. These dimensions are respectively the ranks of `Ω¹_{Y/k}` and `Ω¹_{X/k}` at `y` and `x`, hence are equal by
the hypothesis.

**Remarks.**

<!-- label: II.4.7 -->

When `X` and `Y` are assumed smooth over `S`, the smoothness criterion II.4.5 (ii) for `f: X → Y` can also be stated by
saying that for every `x ∈ X`, the **tangent** map of `f` at `x`, relative to the base `S`, namely the transpose of the
homomorphism of finite-dimensional `κ(x)`-vector spaces given by the restricted fibers of `f*(Ω¹_{Y/S})` and `Ω¹_{X/S}`
at `x`, is **surjective**. This is a very familiar hypothesis, especially among those who work with analytic spaces. The
nonsingularity hypothesis that they ordinarily impose, meaning that `X` and `Y` are “smooth over `ℂ`”, cf. II.5, seems
due only to the fear still inspired in many geometers by singular points of algebraic varieties or analytic spaces.

Let us point out the following special case of II.4.6.

**Corollary.**

<!-- label: II.4.8 -->

Let `X` be an `S`-prescheme, let `g: X → S[t₁,...,t_n]` be an `S`-morphism defined by sections `g_i`, `1 ≤ i ≤ n`, of
`𝒪_X`, and let `x` be a point of `X` such that `X` is smooth over `S` at `x`. In order that `g` be étale at `x`, it is
necessary and sufficient that the `d g_i`, `1 ≤ i ≤ n`, form a basis of `Ω¹_{X/S}` at `x`; equivalently, that their
images in

```text
Ω¹_{X/S}(x) = (Ω¹_{X/S})_x ⊗_{𝒪_x} κ(x)
```

<!-- original page 39 -->

form a basis of this vector space over `κ(x)`.

Let `X` be a prescheme, and let `Y` be a closed sub-prescheme of `X` defined by a coherent sheaf `𝒥` of ideals. Thus
`𝒥/𝒥²` may be regarded as a coherent sheaf on `Y`, the **conormal sheaf** of `Y` in `X`. If now `X` is an `S`-prescheme,
there is a canonical exact sequence of quasi-coherent sheaves on `Y`

```text
𝒥/𝒥² --d→ Ω¹_{X/S} ⊗_{𝒪_X} 𝒪_Y → Ω¹_{Y/S} → 0.
```

<!-- label: eq:II.4.3 -->

Its right-hand part is just II.4.2, with the roles of `X` and `Y` interchanged and taking into account that
`Ω¹_{Y/X} = 0`, while the homomorphism `𝒥/𝒥² → Ω¹_{X/S} ⊗_{𝒪_X} 𝒪_Y` is obtained from the, in general nonlinear,
homomorphism `g ↦ d g` by passing to quotients. The exactness of II.4.3 is classical and in any case trivial; in the
affine case it is interpreted by the following exact sequence, corresponding to a surjective homomorphism `B → C` of
`A`-algebras, with kernel `J`:

```text
J/J² → Ω¹_{B/A} ⊗_B C → Ω¹_{C/A} → 0,     C = B/J.
```

<!-- label: eq:II.4.3bis -->

This exact sequence had already been used implicitly in the proof of I.7.2.

**Proposition.**

<!-- label: II.4.9 -->

Let `X` be an `S`-prescheme, let `Y` be a closed sub-prescheme of `X` defined by a coherent sheaf `𝒥` of ideals on `X`,
let `x` be a point of `X`, let `g_i`, `1 ≤ i ≤ n`, be sections of `𝒪_X` defining an `S`-morphism

```text
g: X → S[t₁,...,t_n] = X′,
```

and finally let `p` be an integer, `0 ≤ p ≤ n`. Suppose that `X` is **smooth over `S` at `x`**. The following conditions
are equivalent:

1. There is an open neighborhood `X₁` of `x` in `X` such that `g|X₁` is **étale** and such that `Y₁ = Y ∩ X₁`, the trace
    of `Y` on `X₁`, is the **inverse image** of the closed sub-prescheme `Y′ = S[t_{p+1},...,t_n]` of
    `X′ = S[t₁,...,t_n]`; equivalently, the `g_i`, `1 ≤ i ≤ p`, generate `𝒥|X₁`:

```text
Y₁  →  X₁
↓       ↓ étale
Y′  →  X′
```

1. `Y` is **smooth over `S` at `x`**, the `g_i`, `1 ≤ i ≤ p`, define **elements of** `𝒥_x`, the `d g_i(x)`, `1 ≤ i ≤ n`,
    form a **basis of** `Ω¹_{X/S}(x)` over `κ(x)`, and the `d g′_i(x)`, `p + 1 ≤ i ≤ n`, form a **basis of**
    `Ω¹_{Y/S}(x)` over `κ(x)`, where the `g′_i` denote the restrictions of the `g_i` to `Y`; the differentials are
    taken relative to `S`.
1. The `g_i`, `1 ≤ i ≤ p`, define a **system of generators** of `𝒥_x`, and the `d g_i(x)`, `1 ≤ i ≤ n`, form a **basis
    of** `Ω¹_{X/S}(x)` over `κ(x)`.
1. `Y` is **smooth over `S`** at `x`, the `g_i`, `1 ≤ i ≤ p`, form a **minimal system of generators of** `𝒥_x`, and the
    `d g′_i(x)`, `p + 1 ≤ i ≤ n`, form a **basis of** `Ω¹_{Y/S}(x)` over `κ(x)`.

Moreover, under these conditions, `𝒥/𝒥²` is a free module on `Y` at `x`, having as **basis at `x`** the classes of the
`g_i`, `1 ≤ i ≤ p`, and the canonical homomorphism

```text
𝒥/𝒥² → Ω¹_{X/S} ⊗ 𝒪_Y
```

is **universally injective at `x`**.

**Remark.** This implies that `p` is well determined by the other conditions, either as the **rank** of the free module
`𝒥/𝒥²` on `Y` at `x`, or again as the **minimum number of generators** of `𝒥_x` on `X`, or finally by the fact that the
relative dimension of `Y` relative to `S` at `x` is `n − p`.

**Proof.** Suppose first that (i) holds. Then by I.4.6 (iii), `Y₁` is étale over `Y′`; hence by definition it is smooth
over `S` at `x`, of relative dimension `n − p`, and the same is therefore true of `Y`. It then follows from II.4.8 that
the `d g_i`, `1 ≤ i ≤ n`, form a basis of `Ω¹_{X/S}` at `x`, and that the `d g′_i`, `p + 1 ≤ i ≤ n`, form a basis of
`Ω¹_{Y/S}` at `x`. By the exact sequence II.4.3, it follows that the `g_i`, `1 ≤ i ≤ p`, are linearly independent in
`𝒥/𝒥²`, considered as a module on `Y`, at `x`. Since the `g_i`, `1 ≤ i ≤ p`, generate `𝒥_x`, it follows that the `g_i`
modulo `𝒥_x²` form a **basis of** `𝒥/𝒥²` at `x`. This implies, on the one hand, that the `g_i`, `1 ≤ i ≤ p`, form a
**minimal** system of generators of `𝒥_x`, and, on the other hand, that the homomorphism `𝒥/𝒥² → Ω¹_{X/S} ⊗ 𝒪_Y` in
II.4.3 is universally injective at `x`, since it sends a basis of a module free at `x` to part of a basis of a module
free at `x`; note that these are `Y`-modules. This proves that (i) implies (ii), (iii), (iv), as well as the last
assertions of Proposition I.4.9.

(iii) implies (i) by Corollary I.4.8.

<!-- original page 41 -->

(ii) implies (i). Indeed, the first hypothesis in (ii) means that, after replacing `X` by an open neighborhood of `x` in
`X`, `g` induces a morphism `h: Y → Y′`. By II.4.8, the two other hypotheses in (ii) mean that `g` is étale at `x` and
`h` is étale at `x`. Let `Y″` be the inverse image of `Y′` by `g`. Then `Y` is a closed sub-prescheme of `Y″`, which is
étale over `Y′` at `x` by I.4.6 (iii), since `g` is étale at `x`. Thus the immersion morphism `Y → Y″` is itself étale
by I.4.8, hence is an open immersion by I.5.8 or I.5.2. Replacing `X` again by a suitable open neighborhood `X₁` of `x`,
we obtain (i).

The preceding establishes the equivalence of conditions (i), (ii), (iii), and the fact that they imply (iv). It remains
to prove that (iv) ⇒ (ii), which is immediate, taking into account that `Ω¹_{X/S}` is free on `X` at `x`, once one knows
that the fact that `Y` is smooth over `S` at `x` implies that `𝒥/𝒥²` is free on `Y` at `x` and that the homomorphism

```text
𝒥/𝒥² → Ω¹_{X/S} ⊗ 𝒪_Y
```

is universally injective at `x`. This last point is included in the following theorem.

**Theorem.**

<!-- label: II.4.10 -->

Let `X` be a smooth `S`-prescheme, let `Y` be a closed sub-prescheme of `X` defined by a coherent sheaf `𝒥` of ideals on
`X`, and let `x` be a point of `X`. The following conditions are equivalent:

1. `Y` is **smooth over `S` at `x`**.
1. There is an open neighborhood `X₁` of `x` in `X` and an **étale** `S`-morphism

```text
g: X₁ → X′ = S[t₁,...,t_n]
```

such that `Y₁ = Y ∩ X₁`, the trace of `Y` on `X₁`, is the sub-prescheme of `X₁` that is the **inverse image** under `g`
of the closed sub-prescheme `Y′ = S[t_{p+1},...,t_n]` of `X′ = S[t₁,...,t_n]`, for a suitable `p`. 3. There are
**generators `g_i`, `1 ≤ i ≤ p`, of `𝒥_x`** such that the `d g_i` form part of a basis of `Ω¹_{X/S}` at `x`;
equivalently, such that the `d g_i(x)` in `Ω¹_{X/S}` are linearly independent over `κ(x)`. 4. The sheaf `𝒥/𝒥²` is free
on `Y` at `x`, and the canonical homomorphism

```text
d: 𝒥/𝒥² → Ω¹_{X/S} ⊗ 𝒪_Y
```

is universally injective at `x`; or again, the sequence of canonical homomorphisms

```text
0 → 𝒥/𝒥² → Ω¹_{X/S} ⊗ 𝒪_Y → Ω¹_{Y/S} → 0
```

is exact at `x`, and `Ω¹_{Y/S}` is locally free at `x`.

**Proof.** We already know from the preceding that (ii) implies (i), (iii), and (iv). We prove (i) ⇒ (ii), which will at
the same time finish the proof of I.4.9. By Theorem II.4.3 (ii), the last two terms in the exact sequence II.4.3 are
free modules on `Y`. Thus, since the images in `Ω¹_{X/S} ⊗_{𝒪_X} 𝒪_Y` of the `d g`, for `g ∈ 𝒪_X`, generate this module
at `x`, hence their images in `Ω¹_{Y/S}` generate the latter at `x`, one can find `g_i`, `p + 1 ≤ i ≤ n`, in `𝒪_X` such
that the `d g′_i` form a basis of `Ω¹_{Y/S}`. Then, by exactness of II.4.3, one can complete the system of the `d g_i`,
`p + 1 ≤ i ≤ n`, to a basis of the middle term by elements of the form `d g_i`, `1 ≤ i ≤ n`, where the `g_i`,
`1 ≤ i ≤ p`, **belong to `𝒥_x`**. The `g_i` come from sections of `𝒪_X` on a neighborhood of `x` in `X`, which we may
suppose equal to `X`. We are then under the conditions of II.4.8 (ii), and we have established that these imply
condition II.4.8 (i), whence II.4.10 (ii).

The implication (iii) ⇒ (ii) in II.4.10 follows at once from the implication (iii) ⇒ (i) in II.4.8. Thus (i), (ii),
(iii) are equivalent and imply (iv). Finally, it is trivial that (iv) implies (iii), taking into account that elements
`g_i ∈ 𝒥_x` whose classes form a basis of `𝒥_x` modulo `𝒥_x²` generate `𝒥_x` by Nakayama.

Moreover, the preceding proof shows the following.

**Corollary.**

<!-- label: II.4.11 -->

Let `X` be an `S`-prescheme, let `Y` be a closed sub-prescheme defined by a coherent sheaf `𝒥` of ideals on `X`, and let
`x` be a point of `Y`. Suppose that **`X` and `Y` are smooth over `S` at `x`**. Let `g_i` be sections of `𝒥`,
`1 ≤ i ≤ p`. The following conditions are equivalent:

1. The `g_i` **generate** `𝒥_x` and the `d g_i(x)` are **linearly independent** in `Ω¹_{X/S}(x)` over `κ(x)`.
1. The `g_i` modulo `𝒥²` form a basis of `𝒥/𝒥²` at `x`.
1. The `g_i` form a minimal system of generators of `𝒥_x`.
1. One can find other sections `g_i`, `p + 1 ≤ i ≤ n`, of `𝒪_X` on a neighborhood `X₁` of `x`, defining together with
    the preceding ones an **étale** morphism `X₁ → X′ = S[t₁,...,t_n]` such that `Y₁ = Y ∩ X₁` is the **inverse image**
    under `g` of the closed sub-prescheme `Y′ = S[t_{p+1},...,t_n]` of `X′ = S[t₁,...,t_n]`.

<!-- original page 43 -->

In particular:

**Corollary.**

<!-- label: II.4.12 -->

Let `X` be an `S`-prescheme, let `F` be a section of `𝒪_X`, let `Y` be the sub-prescheme of the zeros of `F`, defined by
the coherent ideal `F·𝒪_X`, and let `x` be a point of `Y`. Suppose that `X` is smooth over `S` at `x`. In order that `Y`
be smooth over `S` at `x`, it is necessary and sufficient that either `F` be zero in a neighborhood of `x`, or
`dF(x) ≠ 0`, where `dF(x)` denotes the image of `dF` in the vector space `Ω¹_{X/S}(x)` over `κ(x)`.

This is sufficient by criterion (iii) of II.4.10. It is necessary, because since `𝒥` is generated by one element, it is
first necessary that `𝒥/𝒥²` at the point `x` be free of rank `≤ 1`. If this rank is 0, i.e. if `𝒥/𝒥² = 0` at `x`, it
follows that `𝒥 = 0` at `x` by Nakayama, i.e. `F` is zero in a neighborhood of `x`. If this rank is 1, then `F` forms a
minimal system of generators of `𝒥` at `x`, and one concludes by II.4.11, equivalence of (i) and (iii).

**Corollary.**

<!-- label: II.4.13 -->

Let `Y` be an `S`-prescheme locally of finite type, let `S′` be a **flat** `S`-prescheme, let `Y′ = Y ×_S S′`, let `x′`
be a point of `Y′`, and let `x` be its canonical image in `Y`. In order that `Y` be smooth over `S` at `x`, it is
necessary and sufficient that `Y′` be smooth over `S′` at `x′`. In particular, if `S′ → S` is flat and surjective, `Y`
is smooth over `S` if and only if `Y′` is smooth over `S′`.

Only the sufficiency has to be proved; the necessity was seen in II.1.3 (ii). We may suppose, after replacing `Y` by a
suitable neighborhood of `x` and `Y′` by its inverse image, that `Y` is affine of finite type over affine `S`; hence `Y`
is isomorphic to a closed sub-prescheme of a scheme `S[t₁,...,t_n]`. It follows that `Y′` identifies with a closed
sub-prescheme of `X′ = X ×_S S′`. Since `X` is smooth over `S`, and hence `X′` is smooth over `S′`, the smoothness
criteria II.4.10 may be applied. Here criterion (iv) gives the result at once.

**Remarks.**

<!-- label: II.4.14 -->

Criterion (iii) of Theorem II.4.10 deserves to be called the **Jacobian criterion for smoothness**. It makes it
possible, theoretically, to recognize whether a given `S`-prescheme `Y` is smooth over `S` at a point `x` of `Y`, since
there is always a neighborhood of `Y` isomorphic to a sub-prescheme of a smooth `S`-prescheme `X`, for instance
`X = S[t₁,...,t_n]`. It is indeed for `X = S[t₁,...,t_n]`, `S = Spec(A)`, that the Jacobian criterion is usually stated;
of course, in the classical case considered by Zariski, `A` was a field. We leave it to the reader to give the
statement, to which one is thus led, in terms of an ideal `J` of `A[t₁,...,t_n]` and a prime ideal containing it. Let us
note that at present it seems, especially since Nagata succeeded in generalizing by non-differential methods Zariski's
theorem saying that the set of regular points of an algebraic scheme is open, that the Jacobian criterion has scarcely
any interest except in the form in which we give it here, i.e. using exclusively **relative** differentials and not
**absolute** differentials, i.e. differentials relative to the absolute ring of constants `ℤ`. As very often,
considering differentials is more convenient here than considering derivations. Finally, note that if `Y` is smooth over
`S` at `x`, of relative dimension `m`, then there is an open neighborhood of `x` in `Y` isomorphic to a sub-prescheme of
`X = S[t₁,...,t_n]` with `n = m + 1`, as follows from the definition and from I.7.6.

Let `A` be a noetherian ring, let `x_i`, `1 ≤ i ≤ n`, be elements of `A`, and let `J` be the ideal generated by the
`x_i`. We say that the `x_i` form a **regular system of generators** of `J` if the canonical surjective homomorphism

```text
(A/J)[t₁,...,t_n] → gr^J(A)
```

defined by the `x_i`, where the second member denotes the graded ring associated with `A` filtered by the powers of `J`,
is an **isomorphism**. This condition also means that:

1. The canonical surjective homomorphism

```text
S_{A/J}(J/J²) → gr^J(A),
```

where the first member denotes the symmetric algebra of the `A/J`-module `J/J²`, is an isomorphism. 2. `J/J²` is free
and has as basis the classes of the `x_i` modulo `J²`.

In this form one sees that if `J ≠ A`, the `x_i` form a **minimal system of generators** of `J`, and that **every other
minimal system of generators** of `J` **is a regular system of generators**. Here “minimal” is taken in the strict
sense: minimum number of elements, which is equivalent to minimality for inclusion only if `A` is local. On the other
hand, if `J = A`, every system of generators of `J` is regular.

<!-- original page 45 -->

The regularity condition for a system of generators of an ideal is stable under localization by an arbitrary
multiplicatively stable set. Moreover, one sees immediately that, in order for `(x_i)` to be a minimal system of
generators of `J`, it already suffices that for every **maximal ideal `𝔪` containing `J`**, the `x_i` define a regular
system of generators of `J A_𝔪` in `A_𝔪`. We are therefore reduced to the case where `A` is a local ring with maximal
ideal `𝔪`, and where the `x_i` are in `𝔪`. **Then the `x_i` form a regular system of generators of `J` if and only if
they form an `A`-sequence in the sense of Serre**, that is, if for every `i` with `1 ≤ i ≤ n`, `x_i` is not a
zero-divisor in `A/(x₁,...,x_{i−1})A`.[^ii-4-14-1]

Finally, in the case where `A` is an algebra over a ring `B`, and where `A/J` is isomorphic as a `B`-algebra to `B`, so
that `J` is the kernel of a homomorphism of `B`-algebras `A → B`, the `x_i` form a regular system of generators of `J`
if and only if the canonical homomorphism

```text
B[[t₁,...,t_n]] → Â
```

defined by the `x_i`, where the second member denotes the separated completion `lim A/J^{n+1}` of `A` for the topology
defined by the powers of `J`, is an **isomorphism**; it is in any case **surjective**.

All these facts are well known and, no doubt with minor differences, appear in Serre's course on commutative algebra
written up by Gabriel, where one finds N other characterizations of `A`-sequences in the case where `A` is a local ring.

Let `J` be an ideal in a noetherian ring `A`. We shall say that `J` is a **regular ideal** if, for every prime ideal `𝔭`
of `A`, `J A_𝔭` admits a regular system of generators. It is of course enough to verify this for `𝔭 ⊃ J`, and one may
furthermore restrict to maximal `𝔭`. More generally, let `𝒥` be an ideal on a locally noetherian prescheme `X`. We say
that `𝒥` is a **regular ideal** if, for every `x ∈ X`, `𝒥_x` is an ideal of `𝒪_x` admitting a regular system of
generators. This is equivalent to the conjunction of the following two conditions:

1. The canonical surjective homomorphism

```text
S_{𝒪_X/𝒥}(𝒥/𝒥²) → gr^𝒥(𝒪_X)
```

is an isomorphism. 2. The sheaf of `𝒪_X/𝒥`-modules `𝒥/𝒥²` is locally free.

<!-- original page 46 -->

One also then says that the sub-prescheme `Y` of `X` defined by `𝒥`, so that `𝒪_Y` extended by 0 is isomorphic to
`𝒪_X/𝒥`, is **regularly immersed** in `X`. In the same evident way one defines the notion of a morphism that is a
**regular immersion**, respectively **regular at a point `x`**: an immersion morphism `Y → X` identifying `Y`,
respectively a suitable neighborhood of `x`, with a closed sub-prescheme regularly immersed in an open of `X`. One
should not say “regular sub-prescheme”, since that would mean that the local rings of `Y` are regular. Finally, sections
`x_i` of `𝒥` are called a **regular system of generators** if, for every `x ∈ X`, the corresponding elements of `𝒪_x`
form a regular system of generators of `𝒥_x`; this terminology is compatible with that introduced for generators of an
ideal of a ring. This also means that the canonical surjective homomorphism

```text
𝒪_Y[t₁,...,t_n] → gr^𝒥(𝒪_X)
```

defined by the `x_i` is an isomorphism. If one knows in advance that the ideal `𝒥` is regular, this simply means that at
every point `x` **of `Y`**, the `x_i` define a **basis** of `𝒥/𝒥²` over `𝒪_{Y,x}`. This condition is empty if `Y` is
empty. Thus, in order that `𝒥` admit a regular system of generators, it is necessary and sufficient that `𝒥` be regular
and that the `𝒪_Y`-module `𝒥/𝒥²` be globally free, not merely locally free; that is, that the canonical homomorphism
`S_{𝒪_Y}(𝒥/𝒥²) → gr^𝒥(𝒪_X)` be surjective and that the `𝒪_Y`-module `𝒥/𝒥²` be globally free.

An **augmented ring is said to be regular** if the ideal of augmentation is regular. Thus, if `A` is a local ring,
regarded as augmented into its residue field `k`, then `A` is a regular local ring if and only if it is a regular
augmented ring.

To tell the truth, it seems that it was unnecessary to begin by making the preliminary sorites for rings; there is some
advantage in starting with sheaves at once. If one wants something in the noetherian case, it is the definition adopted
here, a priori less strict than Serre's definition by `A`-sequences, that seems preferable for the needs of differential
calculus. Of course, to do the job properly, one would also have to develop at least part of the theory of smooth
morphisms in the non-noetherian setting,[^ii-4-14-2] probably by starting from the Jacobian criterion, so as to obtain
if possible all the essential formal properties of smooth morphisms and of étale morphisms, i.e. smooth and quasi-finite
morphisms; only the converses would appeal to noetherian hypotheses.

After these long terminological preliminaries, a small theorem:

**Theorem.**

<!-- label: II.4.15 -->

Let `X` be an `S`-prescheme locally of finite type, let `Y` be a closed sub-prescheme of `X` defined by a coherent sheaf
`𝒥` of ideals on `X`, and let `x` be a point of `X`. We now suppose **`Y` smooth over `S` at `x`**, and assume nothing
about `X`. Then the following conditions are equivalent:

1. `X` is smooth over `S` at `x`.
1. The immersion `i: Y → X` is regular at `x`, i.e. `𝒥_x` is a regular ideal of `𝒪_x`.

**Corollary.**

<!-- label: II.4.16 -->

Suppose `Y` is **smooth** over `S`. In order that `X` be smooth over `S` in a neighborhood of `Y`, i.e. at the points of
`Y`, it is necessary and sufficient that `Y` be regularly embedded in `X`, i.e. that the immersion `i: Y → X` be
regular.

**Proof.** (i) implies (ii). Apply criterion (ii) of II.4.10. Since `g: X₁ → X` is **flat**, in order to show that the
inverse image by `g` of the sub-prescheme `Y′` of `X′` is regularly embedded, we are reduced to proving that
`Y′ = S[t_{p+1},...,t_n]` is regularly embedded in `S[t₁,...,t_n]`, which is trivial: the `t_i`, `1 ≤ i ≤ p`, form a
regular system of generators of the ideal defining `Y′` in `X′`.

(ii) implies (i). Let `g_i`, `1 ≤ i ≤ p`, be a regular system of generators of `𝒥_x`, and let `g_i`, `p + 1 ≤ i ≤ n`, be
elements of `𝒪_{X,x}` such that their images `g′_i` in `𝒪_{Y,x}` define an **étale** morphism

```text
Y₁ → Y′ = S[t_{p+1},...,t_n]
```

from a neighborhood `Y₁` of `x` in `Y`. The `g_i`, `1 ≤ i ≤ n`, come from sections, denoted by the same names, of `𝒪_X`
on a neighborhood `X₁` of `x`, and we may suppose `X₁ = X` and `Y₁ = Y`. We thereby obtain a morphism

```text
g: X → X′ = S[t₁,...,t_n],
```

and everything comes down to showing that this morphism is **étale** at `x`. Taking `X₁` small enough, we may suppose
that the `g_i`, `1 ≤ i ≤ p`, form a regular system of generators of `𝒥` on all of `X`. In particular, they generate `𝒥`,
so the sub-prescheme `Y` of `X` identifies with the inverse image by `g` of the sub-prescheme `Y′` of `X′`. Let
`x′ = g(x)`. Then the fiber of `X → X′` at `x′` is identical with the fiber of `Y → Y′` at `x`, hence is étale over
`κ(x′)`, and therefore `g` is **unramified** at `x`. It remains to prove that `g` is **flat** at `x`. The graded ring
associated with `𝒪_{X′,x′}`, filtered by the powers of `𝒥′_{x′}`, is **free** over `𝒪_{Y′,x′}` in every degree; on the
other hand, the graded ring associated with `𝒪_{X,x}`, filtered by the powers of `𝒥_x = 𝒥′_x 𝒪_{X,x}`, is isomorphic,
under the canonical homomorphism, to the tensor product of the preceding one with `𝒪_{Y,x}`, since both rings are
polynomial rings in `n − p` indeterminates with rings of constants `𝒪_{Y′,x′}` and `𝒪_{Y,x}`, respectively. Finally,
over `𝒪_{X′,x′}/𝒥′_{x′} = 𝒪_{Y′,x′}`, the quotient `𝒪_{X,x}/𝒥_x = 𝒪_{Y,x}` is flat.

By a general flatness criterion, valid for a local homomorphism of noetherian local rings `A′ → A`, where `A′` is
equipped with an ideal `J′ ≠ A′` whose associated graded ring is free over `A′/J′` in every dimension, it follows that
`X` is flat over `X′` at `x`, as required.

**Corollary.**

<!-- label: II.4.17 -->

Let `X` be a prescheme locally of finite type over `Y`, let `i` be a section of `X` over `Y`, let `y` be a point of `Y`,
let `x = i(y)`, and let `𝒥` be the sheaf of ideals on `X` defined by the sub-prescheme `i(Y)`, which we suppose closed
in order to simplify the statement, a condition satisfied if `X` is a scheme.

The following conditions are equivalent:

1. `X` is smooth over `Y` at `x`.
1. `i` is a regular immersion at `y`.
1. The `𝒪_y`-algebra obtained by completing `𝒪_x` for the topology defined by the powers of `𝒥_x` is isomorphic to a
    formal power-series algebra `𝒪_y[[t₁,...,t_n]]`.
1. There is an open neighborhood `U` of `y` such that the sheaf of algebras `lim i*(𝒪_X/𝒥^{n+1})` on `𝒪_Y` is isomorphic
    over `U` to a sheaf of the form `𝒪_Y[[t₁,...,t_n]]`.
1. There is an open neighborhood `U` of `y`, an open neighborhood `V` of `x`, and finally a `Y`-morphism
    `g: V → U[t₁,...,t_n]`, such that `g` is étale, such that `i` induces a section of `V` over `U`, and such that `g`
    carries this section to the zero section of `U[t₁,...,t_n]` over `U`.

The equivalence of (i) and (ii) is a special case of Theorem II.4.15, taking `Y = S`. The equivalence of (ii) and (iii),
and morally of (ii) and (iii bis), was indicated in the “reminders”. As for the equivalence of (i) and (iv), it follows
easily from Theorem II.4.10, namely from the equivalence of conditions (i) and (ii) there.

**Corollary.**

<!-- label: II.4.18 -->

Let `X` be a prescheme smooth over `S`. Then the diagonal morphism

```text
Δ_{X/S}: X → X ×_S X
```

is a **regular immersion**, or, as one also says, `X` is “**differentially smooth**” over `S`.

Indeed, this is a special case of Corollary II.4.16, since `X` and `X ×_S X` are both smooth over `S`.

**Remarks.**

<!-- label: rem:II.4.18 -->

Recall from I.1 that if `X` is a prescheme over `S`, one introduces the quasi-coherent sheaves of algebras

```text
𝒫ⁿ_{X/S} = 𝒪_{X ×_S X}/𝓘_X^{n+1}
```

on `X`, where `𝓘_X` denotes the sheaf of ideals defining the diagonal in `X ×_S X`, regarded as a sheaf of
`𝒪_X`-algebras through the first projection `pr₁: X ×_S X → X`. The `𝒫ⁿ_{X/S}` form a projective system of algebras on
`X`, whose projective limit is denoted `𝒫^∞_{X/S}`; it is nothing other than the structure sheaf of the formal
completion of `X ×_S X` along the diagonal, now supposing `X` locally of finite type over `S`, hence the `𝒫ⁿ_{X/S}`
coherent. To say that `X` is differentially smooth over `S`, i.e. that the diagonal morphism `Δ_{X/S}` is a regular
immersion, also means that `𝒫^∞_{X/S}` is regular as a sheaf of augmented algebras toward `𝒪_X`, i.e. that `Ω¹_{X/S}` is
locally free and the canonical surjective homomorphism

```text
S_{𝒪_X}(Ω¹_{X/S}) → gr_*(𝒫^∞_{X/S})
```

is an isomorphism; or finally that every point of `X` has an open neighborhood on which the sheaf of augmented algebras
`𝒫^∞_{X/S}` is isomorphic to a sheaf `𝒪_X[[t₁,...,t_n]]`.

Let `s` be a section of `X` over `S`, and let `𝒥` be the sheaf of ideals on `X` that it defines, supposing for
simplicity that `s(S)` is closed. Then there are canonical isomorphisms of augmented `𝒪_X`-algebras:

```text
s*(𝒫ⁿ_{X/S}) = 𝒪_X/𝒥^{n+1},    s*(𝒫^∞_{X/S}) = lim_n 𝒪_X/𝒥^{n+1}.
```

<!-- label: eq:II.4.4 -->

These isomorphisms are functorial in the evident sense under base change and, taking this fact into account, again give
a characterization of the sheaves of algebras `𝒫ⁿ_{X/S}` on `S`. If, for example, `S = Spec(k)`, with `k` a field, then
giving a section `s` of `X` over `S` is equivalent to giving a point `x` of `X` rational over `k`, and the preceding
formulas mean that there is an isomorphism of `k`-algebras

```text
𝒫ⁿ_{X/S}(x) = 𝒪_x/𝔪_x^{n+1}.
```

<!-- label: eq:II.4.5 -->

This justifies the name “**sheaf of principal parts of order `n` on `X` relative to `S`**” given to `𝒫ⁿ_{X/S}`. One sees
moreover from II.4.4 that **if `X` is differentially smooth over `S` at every point of `s(S)`, then `X` is smooth over
`S` at every point of `s(S)`**, by Corollary II.4.17, **the converse also being true**, by Corollary II.4.18. Taking
II.4.13 into account, one easily concludes that if `X` is an `S`-prescheme locally of finite type, **`X` is smooth over
`S` if and only if it is flat over `S` and differentially smooth over `S`**. Note that the flatness hypothesis is
essential, as one sees by taking `X` to be a closed sub-prescheme of `S`.

Let us also recall that one obtains a **second algebra structure** on `𝒫ⁿ_{X/S}` through the projection
`pr₂: X ×_S X → X`; it is in fact obtained from the preceding one by means of the **canonical involution** of the sheaf
of rings `𝒫ⁿ_{X/S}`, induced by the symmetry automorphism of `X ×_S X`. We denote by `dⁿ_{X/S}`, or simply `dⁿ`, the
homomorphism of sheaves of rings

```text
dⁿ_{X/S}: 𝒪_X → 𝒫ⁿ_{X/S}
```

<!-- label: eq:II.4.6 -->

that corresponds to this second algebra structure. Taking the isomorphism II.4.4 into account, this homomorphism
transforms a section `f` of `𝒪_X` into a section `dⁿ(f)` of `𝒫ⁿ_{X/S}` whose inverse image by a section `s` of `X` over
`S` identifies with the canonical image of `f` in `Γ(X, 𝒪_X/𝒥^{n+1})`. This justifies the name “**system of principal
parts of order `n` of `f`**” given to `dⁿf`, notably in the case `S = Spec(k)` considered in formula II.4.5.

Finally, note that the homomorphism II.4.6 may be regarded as the **universal differential operator of order
`≤ n`**[^ii-4-18-1] on `𝒪_X`, relative to the prescheme of constants `S`, provided one agrees to call a homomorphism of
sheaves `D` from `𝒪_X` into a module `F` a differential operator of order `≤ n` when it factors as

```text
D: 𝒪_X --dⁿ→ 𝒫ⁿ_{X/S} --u→ F
```

where `u` is a homomorphism of `𝒪_X`-modules, necessarily uniquely determined by `D`. This definition agrees with the
intuitive recursive definition: `D` is a differential operator of order `≤ n` if for every section `g` of `𝒪_X` on an
open `U` of `X`, the map `f ↦ D(fg) − gD(f)` is a differential operator of order `≤ n − 1` on `U`. It follows that **if
`X` is differentially smooth over `S`, the sheaf of rings of differential operators of all orders has the familiar
simple structure** from differential calculus on differentiable manifolds, and in particular admits locally, as an
`𝒪_X`-module, a basis formed from the **divided powers** in commuting operators `δ/δx_i`, `1 ≤ i ≤ n`. If `S` is a sheaf
of `ℚ`-algebras, where `ℚ` is the field of rational numbers, it is enough to take the ordinary polynomials in the
`δ/δx_i`. In that case, moreover, and very exceptionally, for `X` to be differentially smooth over `S` it already
suffices that `Ω¹_{X/S}` be locally free.

**Remark.**

<!-- label: II.4.19 -->

The terminology “regular immersion”, “regular ideal”, etc. introduced in this number met with rather lively and general
opposition from Chevalley and Serre. “Cohen-Macaulay ideal”, or “Macaulay ideal”, or “Macaulayan ideal” was proposed,
which would morally oblige one also to adopt “Cohen-Macaulay immersion” or “Macaulay immersion”. This terminology,
however, conflicts with another already used in future drafts of the multiplodocus, where a morphism of finite type is
said to be “Cohen-Macaulay” at a point if it is flat at that point and if the fiber passing through that point has there
a local ring that is a Cohen-Macaulay ring. Pending a satisfactory solution, we shall keep, with every reservation, the
terminology introduced in this number.[^ii-4-19-1]

## 5. Case of a Base Field

<!-- label: II.5 -->

<!-- original page 52 -->

**Proposition.**

<!-- label: II.5.1 -->

Let `k` be a field, let `X` be a prescheme of finite type over `k`, let `x` be a point of `X`, let `n` be the dimension
of `X` at `x`, and let

```text
f: X → Spec k[t₁,...,t_n] = Y
```

be a morphism defined by elements `f_i ∈ Γ(X, 𝒪_X)`. The following conditions are equivalent, and imply that `X` is
smooth over `k` at `x`, and a fortiori regular at `x` by II.3.1:

1. `f` is étale at `x`.
1. The `d f_i` form a basis of `Ω¹_{X/k}` at `x`.
1. The `d f_i` generate `Ω¹_{X/k}` at `x`.

Since (i) implies that `X` is smooth over `k` at `x`, the implication (i) ⇒ (ii) is a special case of II.4.8; (ii) ⇒
(iii) is trivial. It remains to prove (iii) ⇒ (i). If (iii) holds, `f` is unramified at `x` by Lemma II.4.1, hence,
after replacing `X` by an open neighborhood of `x`, quasi-finite, and therefore dominant for dimension reasons. Since
`Y` is regular, it follows that `f` is étale by I.9.5 (ii) or I.9.11.

**Corollary.**

<!-- label: II.5.2 -->

Under the preliminary conditions of II.5.1, suppose that `κ(x)` is a **finite separable** extension of `k`, and that the
`f_i`, `1 ≤ i ≤ n`, define elements of `𝔪_x`. Then the preceding conditions are equivalent to:

1. The `f_i` form a system of generators of `𝔪_x`; equivalently, the `f_i` modulo `𝔪_x²` form a basis of `𝔪_x/𝔪_x²` over
    `κ(x)`.

Indeed, (iv) ⇒ (iii) by the exact sequence

```text
𝔪_x/𝔪_x² → Ω¹_{𝒪_x/k} → Ω¹_{κ(x)/k} → 0
```

<!-- label: eq:II.5.1 -->

and the fact that `Ω¹_{κ(x)/k} = 0`, since `κ(x)` is étale over `k`. On the other hand, (ii) implies (iv), because since
`X` and `Spec(κ(x))` are smooth over `k` at `x`, one may put a 0 on the left in the preceding exact sequence by II.4.10
(iv).

**Corollary.**

<!-- label: II.5.3 -->

Let `x` be a point of `X`, of finite type over `k`. If `X` is smooth over `k` at `x`, then `𝒪_x` is regular; the
converse is true if `κ(x)` is a finite separable extension of `k`.

Indeed, the converse follows from II.5.2 by taking a regular system `(f_i)` of generators of `𝔪_x`. Instead of II.5.2
one may also invoke Theorem II.4.15. We conclude:

**Proposition.**

<!-- label: II.5.4 -->

Let `X` be a prescheme of finite type over `k`. If `X` is smooth over `k`, then it is regular; the converse is true if
`k` is perfect.

For the converse, note that by II.5.3, `X` is smooth over `k` at every closed point, hence everywhere, since the set of
points where it is smooth is open.

**Theorem.**

<!-- label: II.5.5 -->

Let `X` be a prescheme of finite type over `k`, let `x` be a point of `X`, let `n` be the dimension of `X` at `x`, and
let `k′` be a perfect extension of `k`. The following conditions are equivalent:

1. `X` is smooth over `k` at `x`.
1. `Ω¹_{X/k}` is free of rank `n` at `x`.
1. `Ω¹_{X/k}` is generated by `n` elements at `x`.
1. `X` is differentially smooth over `k` at `x`.
1. There is an open neighborhood `U` of `x` such that `U ⊗_k k′` is regular, i.e. the local rings of its points are
    regular.

We have (i) ⇒ (ii) by II.4.3 (ii), (ii) ⇒ (ii bis) trivially, and (ii bis) ⇒ (i) by II.5.1. Since `X` is flat over `k`,
we have (i) ⇔ (iii) by II.4.18. We have (i) ⇒ (iv) because smoothness is invariant under extension of the base and
implies regularity; and (iv) ⇒ (i), because by Proposition II.5.4 one sees that `U ⊗_k k′` is smooth over `k′`, hence
`U` is smooth over `k` by II.4.13.

Taking `x` to be the generic point of `X`, supposed irreducible, one obtains:

**Corollary.**

<!-- label: II.5.6 -->

Let `K` be a local Artin ring obtained by localizing an algebra of finite type over the field `k`; for example, `K` may
be an extension of finite type of `k`. Let `n` be the transcendence degree over `K` of its residue field. The following
conditions are equivalent:

1. `K` is a finite separable extension of a purely transcendental extension `k(t₁,...,t_n)` of `k`.
1. `Ω¹_{K/k}` is a free `K`-module of rank `n`.
1. `Ω¹_{K/k}` is a `K`-module admitting `n` generators.
1. The completion `O′` of `K ⊗_k K` for the topology defined by the powers of the augmentation ideal `K ⊗_k K → K` is a
    “regular” augmented `K`-algebra, i.e. isomorphic to a formal power-series algebra over `K`. If `K` is a field, this
    is equivalent to saying that `O′` is a regular local ring.
1. `K` is a separable extension of `k`.

Indeed, one may always regard `K` as the local ring of the generic point of an irreducible scheme `X` of finite type
over `k`, and the conditions under consideration are the conditions with the same names in II.5.5, taking in (iv) an
algebraically closed extension of `k` for `k′`. Only the implication “`K` separable over `k` ⇒ `X` smooth over `k` at
`x`” requires a proof. By II.4.13 one is immediately reduced to the case where the base field is `k′`, hence
algebraically closed, and therefore where there exists a point `a` of `X` rational over `k`. But then `X` is smooth over
`k` at `a` by II.5.4, and a fortiori it is smooth over `k` at the generic point `x`.[^ii-5-6-1]

One will notice that in the case where `K` is an extension of finite type of `k`, the equivalence of (i), (ii), (ii
bis), and (iv) is well known, but that we have not used any of these already-known equivalences. Of course Proposition
II.5.1 contains as a special case the well-known fact that a sequence of elements `x_i`, `1 ≤ i ≤ n`, is a “separating
transcendence basis” of `K` over `k` if and only if the `d x_i` form a basis of the `K`-module `Ω¹_{K/k}`.

**Corollary.**

<!-- label: II.5.7 -->

Let `X` be a prescheme of finite type over a field `k`. In order that `X` be smooth over `k`, it is necessary and
sufficient that `Ω¹_{X/k}` be locally free and that the local rings at the generic points of the irreducible components
of `X` be separable extensions of `k`. The latter condition is automatically satisfied if `k` is perfect and `X` is
reduced.

We may suppose `X` connected, and let `n` be the rank of `Ω¹_{X/k}`, assumed locally free. By the hypothesis and II.5.6,
this is also the transcendence degree of the extensions of `k` defined by the local rings at the generic points of `X`.
Hence all irreducible components of `X` have dimension `n`. We then conclude by II.5.5.

Care must be taken that if `K` is a finite, not necessarily separable, extension of `k`, then `Ω¹_{K/k}` is a free
`k`-module; hence, putting `X = Spec(K)`, `Ω¹_{X/k}` is a locally free sheaf and `X` is reduced, without `X` necessarily
being smooth over `k`. Extending scalars then to the algebraic closure of `k`, one obtains an analogous example where
`k` is algebraically closed, but `X`, in contrast, is not reduced.

**Corollary.**

<!-- label: II.5.8 -->

Let `X` be a prescheme of finite type over the field `k`, let `x` be a point of `X`, let `n` be the dimension of `X` at
`x`, and let `p` be the dimension of `𝒪_x`, i.e. the codimension in `X` of the closure `Y` of `x` in `X`; thus `n − p`
is the transcendence degree of `κ(x)` over `k`. Let `f_i`, `1 ≤ i ≤ n`, be elements of `𝒪_x`, with `f_i ∈ 𝔪_x` for
`1 ≤ i ≤ p`. The following conditions are equivalent:

1. The germ at `x` of the morphism

```text
X → Spec(k[t₁,...,t_n])
```

defined by the `f_i` is étale at `x`. 2. The `f_i`, `1 ≤ i ≤ p`, generate `𝔪_x`, i.e. form a regular system of
parameters of `𝒪_x`, and the classes in `κ(x)` of the `f_j`, `p + 1 ≤ j ≤ n`, form a separating transcendence basis;
equivalently, the `d f̄_j`, `p + 1 ≤ j ≤ n`, form a basis of `Ω¹_{κ(x)/k}`, or again generate `Ω¹_{κ(x)/k}`.

Suppose (i) holds. It follows that the `d f_i(x)` form a basis of `Ω¹_{X/k}(x)` by II.4.8; hence their images
`d f̄_i(x)` in `Ω¹_{κ(x)/k}` generate this vector space over `k`. Since the `f̄_i` for `1 ≤ i ≤ p` are zero, it follows
that it suffices to take the `d f̄_i(x)` with `p + 1 ≤ i ≤ n`. Since the transcendence degree of `κ(x)` over `k` is
`n − p`, Corollary II.5.6, criterion (iii), applied to `K = κ(x)`, then implies that `Y` is smooth over `k` at its
generic point `x`, and that the `d f̄_i(x)`, `p + 1 ≤ i ≤ n`, form a **basis** of `Ω¹_{κ(x)/k}` over `κ(x)`.
Consequently condition (ii) of II.4.9 is satisfied, hence also condition (iii), and in particular the `f_i`,
`1 ≤ i ≤ p`, form a system of generators of `𝔪_x`. Since `𝒪_x` has dimension `p`, they therefore form a regular system
of parameters at `x`. This proves (ii).

Suppose (ii) holds. By the exact sequence II.5.1, it follows that the `d f_i(x)` generate `Ω¹_{X/k}`; hence (i) follows
from Proposition II.5.1.

**Corollary.**

<!-- label: II.5.9 -->

Let `X` be a prescheme of finite type over the field `k`, let `x` be a point of `X`, let `n` be the dimension of `X` at
`x`, and let `p` be the dimension of `𝒪_x`, i.e. the codimension of the closure `Y` of `x` in `X`; thus `n − p` is the
transcendence degree of `κ(x)` over `k`. The following conditions are equivalent:

1. `𝒪_x` is regular and `κ(x)` is a separable extension of `k`.
1. `X` is smooth over `k` at `x`, and the canonical homomorphism

```text
𝔪_x/𝔪_x² → Ω¹_{𝒪_x/k} ⊗_{𝒪_x} κ(x) = Ω¹_{X/k}(x)
```

is injective. 3. There are `f_i ∈ 𝒪_x`, `1 ≤ i ≤ n`, with `f_i ∈ 𝔪_x` for `1 ≤ i ≤ p`, such that the germ at `x` of the
morphism from `X` to `Spec(k[t₁,...,t_n])` defined by the `f_i` is étale at `x`; equivalently, by II.5.1, such that the
`d f_i(x)` generate `Ω¹_{X/k}(x)`. 4. There are `f_i ∈ 𝒪_x`, `1 ≤ i ≤ n`, such that the `f_i`, `1 ≤ i ≤ p`, generate
`𝔪_x` and the `d f_j(x)`, `p + 1 ≤ j ≤ n`, generate `Ω¹_{κ(x)/k}` over `κ(x)`.

The equivalence of (iii) and (iv) follows from Corollary II.5.8. By II.4.9, these conditions are also equivalent to the
fact that `X` is smooth over `k` at `x` and that condition (ii) of II.4.10 is satisfied. Thus they are equivalent to the
fact that `X` is smooth over `k` at `x` and that condition (iv) of II.4.10 is satisfied, hence to II.5.9 (ii). Or
equivalently, to the fact that `X` is smooth over `k` at `x` and that condition (i) of II.4.10 is satisfied, which here
simply means that `κ(x)` is separable over `k`. This implies II.5.9 (i). It remains to prove that II.5.9 (i) implies it,
i.e. to prove:

**Corollary.**

<!-- label: II.5.10 -->

Let `x` be a point of a prescheme of finite type over the field `k`, such that `κ(x)` is separable over `k`. In order
that `X` be smooth over `k` at `x`, it is necessary and sufficient that it be regular at `x`, i.e. that the local ring
`𝒪_x` be regular.

Indeed, if this is so, one can evidently find `f_i ∈ 𝒪_x`, `1 ≤ i ≤ n`, satisfying condition II.5.9 (iv).

### Errata

<!-- label: II.fin.errata -->

<!-- original page 57 -->

In the present number, in the proof of II.5.6, we used the fact that a nonempty reduced scheme of finite type over an
algebraically closed field has at least one regular, hence smooth, point, a fact usually proved by differential means,
via Zariski's theorem that the set of regular points of `X` is open. If one wants to avoid a vicious circle, one must
prove that if `K/k` is a separable extension of finite type, and if the `f_i ∈ K` are such that `d_{K/k} f_i` form a
basis of `Ω¹_{K/k}`, `1 ≤ i ≤ n`, then `n` is the transcendence degree of `K` over `k`, i.e. the `f_i` are algebraically
independent. The proof of this fact using Mac Lane's criterion is well known; cf. Bourbaki, Algebra, Chapter V,
paragraph 9, theorem 2. One takes a polynomial `g ∈ k[t₁,...,t_n]` of minimal degree such that `g(f₁,...,f_n) = 0`. We
then have

```text
Σ_i (∂g/∂t_i)(f₁,...,f_n) d f_i = 0.
```

Hence, since the `d f_i` form a basis of `Ω¹_{K/k}`, the `∂g/∂t_i` vanish at `(f₁,...,f_n)`, and therefore are zero by
the minimality of `g`. Thus if `k` has characteristic 0, one has `g = 0`, while if `k` has characteristic `p ≠ 0`, one
has `g = h(t₁ᵖ,...,t_nᵖ)`. Using Mac Lane's criterion, one sees that the polynomial `h ∈ k[t₁,...,t_n]` also vanishes at
`(f₁,...,f_n)`, whence again `g = 0` by the minimality of `g`.

<!-- end of Exposé II source block: next chapter begins at smf_doc-math_3_01.tex line 4492 -->

[^II-1-1]: Older terminology: `f` is simple at `x`, or `x` is a simple point for `f`. This terminology led to confusion
    in various contexts, such as simple algebras and simple groups, and had to be abandoned.

[^II-1-2]: It is better then to say, as in EGA IV 18.6.1, that `B` is “essentially smooth” over `A`.

[^II-2-1]: Cf. EGA IV 7.8.

[^II-2-2]: Cf. EGA IV 5.12.10.

[^II-3-1]: For these formulas, cf. EGA IV 6.1 and 6.3.

[^ii-4-14-1]: We would now rather say “`A`-regular sequence”, cf. EGA 0_IV 15.1.7 and 15.1.11.

[^ii-4-14-2]: As was said in the preface, this has now been done; cf. EGA IV 17, 18.

[^ii-4-18-1]: For everything concerning the present paragraph, one may consult EGA IV 16.8 to 16.12.

[^ii-4-19-1]: This is the terminology adopted in EGA 0_IV 15.1.7.

[^ii-5-6-1]: Cf. the Errata at the end of the present Exposé II, p. 57 in the original numbering.
