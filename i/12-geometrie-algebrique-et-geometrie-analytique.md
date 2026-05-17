# Exposé XII. Algebraic Geometry and Analytic Geometry

<!-- label: XII -->

<!-- original page 311 -->

Mme M. Raynaud. [Translator note: according to unpublished notes of A. Grothendieck.]

Proceeding as in [XII.10], one associates to every scheme `X` locally of finite type over the field of complex numbers
`ℂ` an analytic space `X^an`, whose underlying set is `X(ℂ)`.

<!-- label: indnot:lb -->

In nos. XII.2 and XII.3 of this exposé, we give a “dictionary” between the usual properties of `X` and of `X^an`, and
between the properties of a morphism `f: X → Y` and of the associated morphism `f^an: X^an → Y^an`.

<!-- label: indnot:lc -->

We then show that the comparison theorems between coherent sheaves on `X` and `X^an`, established in [XII.10, no. 12]
for a projective variety, are still valid when `X` is a proper scheme.

Finally, in no. XII.5 we prove the equivalence between the category of finite étale coverings of `X` and the category of
finite étale coverings of `X^an`. As a bonus for the reader, we give a new proof of the Grauert-Remmert theorem [XII.6],
using resolution of singularities [XII.8].

## 1. The Analytic Space Associated with a Scheme

<!-- label: XII.1 -->

<!-- original page 312 -->

Let `X` be a scheme locally of finite type over `ℂ`. Let `Φ` be the functor from the category of analytic spaces
\[XII.4, no. 9\] to the category of sets which associates to an analytic space `𝓧` the set of morphisms of ringed spaces
in `ℂ`-algebras `Hom_ℂ(𝓧,X)`. One has the following theorem:

**Theorem-Definition.**

<!-- label: XII.1.1 -->

The functor `Φ` is representable by an analytic space `X^an` and a morphism `φ: X^an → X`. One says that `X^an` is the
analytic space associated with `X`.

If `|X^an|` is the underlying set of `X^an`, `φ` induces a bijection from `|X^an|` to the set `X(ℂ)` of points of `X`
with values in `ℂ`. Moreover, for each point `x` of `X^an`, the morphism

```text
φ_x: 𝒪_X,φ(x) → 𝒪_X^an,x,
```

which is necessarily local, gives after passage to completions an isomorphism

```text
φ̂_x: 𝒪̂_X,φ(x) ≃ 𝒪̂_X^an,x.
```

In particular the morphism `φ` is flat.

Notice that the fact that `φ` induces a bijection from `X^an` to `X(ℂ)` follows from the universal property of `X^an`.
On the other hand, one has the following assertions:

a. If the theorem is true for a scheme `Y`, then it is also true for every subscheme `X` of `Y`. Suppose first that `X`
is an open subscheme of `Y`. If `ψ: Y^an → Y` is the canonical morphism, `ψ⁻¹(X)` is an open subset

<!-- original page 313 -->

of `Y^an`, endowed with the analytic-space structure induced by that of `Y^an`. Since every morphism from an analytic
space `𝓧` to `X` factors through `Y^an` by the universal property of the latter, and hence through `X^an`, which is the
fiber product `Y^an ×_Y X`, `X^an` is the analytic space associated with `X`. Finally, the assertion concerning the
`φ_x` is evident.

It remains only to consider the case where `X` is a closed subscheme of `Y`. Let `I` be the coherent `𝒪_Y`-ideal
defining `X`. Then `I · 𝒪_Y^an` is a coherent sheaf of ideals on `𝒪_Y^an` defining a closed analytic subspace `X^an` of
`Y^an`. As in the case of an open subscheme, one sees that `X^an` is the analytic space associated with `X`. Let
`φ: X^an → X` be the canonical morphism. For every point `x` of `X^an`, the morphism `φ_x` is none other than the
morphism

```text
𝒪_Y,ψ(x)/I_ψ(x) → 𝒪_Y^an,x / I_ψ(x) · 𝒪_Y^an,x
```

induced by `ψ_x`. Its completion

```text
𝒪̂_Y,ψ(x) / I_ψ(x) · 𝒪̂_Y,ψ(x)
  → 𝒪̂_Y^an,x / I_ψ(x) · 𝒪̂_Y^an,x
```

is an isomorphism, since `ψ̂_x` is one; this proves a.

b. If one has two `ℂ`-schemes `X₁`, `X₂`, such that `X₁^an` and `X₂^an` exist, then `(X₁ × X₂)^an` also exists. Indeed,
let `φ₁: X₁^an → X₁` and `φ₂: X₂^an → X₂` be the canonical morphisms, and let `p₁`, `p₂` be the two projections from
`X₁^an × X₂^an`. It follows formally from EGA I 1.8.1 that `X₁ × X₂` is the product of `X₁` and `X₂` in the category of
ringed spaces in local rings. Consequently the morphisms `φ₁ · p₁` and `φ₂ · p₂` define a

<!-- original page 314 -->

morphism `φ: X₁^an × X₂^an → X₁ × X₂`, and the pair `(X₁^an × X₂^an, φ)` represents the functor `𝓧 ↦ Hom_ℂ(𝓧, X₁ × X₂)`.

c. If `𝓔¹` denotes affine space of dimension 1, that is, the topological space `ℂ` endowed with the sheaf of holomorphic
functions, the functor `𝓧 ↦ Hom_ℂ(𝓧,E¹_ℂ)` is representable by `𝓔¹`, the canonical morphism `φ: 𝓔¹ → E¹_ℂ` being the
evident morphism. \[Translator note: the corrected source adds in 2003 that `E¹_ℂ` denotes the algebraic affine line
over `ℂ`.\] Indeed, to give a morphism from an analytic space `𝓧` to `E¹_ℂ` is equivalent to giving an element of
`Γ(𝓧,𝒪_𝓧)`, which is also equivalent to giving a morphism from `𝓧` to `𝓔¹`. Plainly one has a bijection `|𝓔¹| ≃ E¹(ℂ)`,
and, for each point `x ∈ 𝓔¹`, the morphism `φ̂_x` is none other than the identity morphism of a ring of formal power
series in one variable over `ℂ`.

It follows from b and c that the theorem is true for affine space `Eⁿ_ℂ`, `n ≥ 0`. Using a, one sees that it is also
true for every affine scheme `X` locally of finite type over `ℂ`. If `X` is no longer assumed affine and if `(X_i)` is a
covering of `X` by affine opens, it follows from the universal property and from a that the `X_i^an` glue and thus
define the analytic space `X^an` associated with `X`.

### 1.2.

<!-- label: XII.1.2 -->

Let `f: X → Y` be a morphism of `ℂ`-schemes locally of finite type. If `φ: X^an → X` and `ψ: Y^an → Y` are the canonical
morphisms, it follows from the universal property of `Y^an` that there exists a unique morphism `f^an: X^an → Y^an` such
that the diagram

```text
X^an → X
 |      |
f^an   f
 |      |
Y^an → Y
```

is

<!-- original page 315 -->

commutative. We have therefore defined a functor `Φ` from the category of `ℂ`-schemes locally of finite type to the
category of analytic spaces.

The functor `Φ` commutes with finite projective limits. Indeed it is enough to see that `Φ` commutes with fiber
products. But if `X`, `Y`, `Z` are schemes locally of finite type over `ℂ`, it follows from the fact that `X ×_Z Y` is
the fiber product of `X` and `Y` over `Z` in the category of ringed spaces in local rings that `X^an ×_Z^an Y^an`
satisfies the universal property characterizing `(X ×_Z Y)^an`.

### 1.3.

<!-- label: XII.1.3 -->

Let `X` be a `ℂ`-scheme locally of finite type, let `X^an` be the associated analytic space, and let `φ: X^an → X` be
the canonical morphism. If `F` is an `𝒪_X`-module, the inverse image `φ*F = F^an` is a sheaf of modules over `𝒪_X^an`.
This defines a functor from the category of `𝒪_X`-modules to the category of modules on `X^an`. This functor commutes
with inductive limits (EGA 0 4.3.2). Since the sheaf `𝒪_X^an` is coherent [XII.4, no. 18, §2, th. 2], it sends coherent
sheaves to coherent sheaves (EGA 0 5.3.11). Moreover:

**Subproposition.**

<!-- label: XII.1.3.1 -->

The functor which associates to an `𝒪_X`-module `F` its inverse image `F^an` on `X^an` is exact, faithful, and
conservative.

Exactness follows from the fact that the morphism `φ: X^an → X` is flat (XIII.1.1). Let us prove that the functor
`F ↦ F^an` is faithful. Taking exactness into account, it is enough to show that if `F^an` is zero, then `F` itself is
zero. But for every point `x` of `X^an` one then has

```text
F_φ(x) ⊗_𝒪_X,φ(x) 𝒪_X^an,x = 0.
```

Since the morphism `𝒪_X,φ(x) → 𝒪_X^an,x` is faithfully flat, one has `F_φ(x) = 0` for every closed point `φ(x)` of `X`;
and since `X` is Jacobson (EGA IV 10.4.8), this implies that `F` is zero.

The

<!-- original page 316 -->

fact that the functor `F ↦ F^an` is conservative is formal from exactness and faithfulness.

## 2. Comparison of Properties of a Scheme and of the Associated Analytic Space

<!-- label: XII.2 -->

**Proposition.**

<!-- label: XII.2.1 -->

Let `X` be a `ℂ`-scheme locally of finite type, let `X^an` be the associated analytic space, and let `n` be an integer.
Consider the property `P` of being:

```text
(i)    nonempty
(i′)   discrete
(ii)   Cohen-Macaulay
(iii)  (S_n)
(iv)   regular
(v)    (R_n)
(vi)   normal
(vii)  reduced
(viii) of dimension n.
```

Then `X` has property `P` if and only if `X^an` has property `P`.

Let `φ: X^an → X` be the canonical morphism. Assertion (i) follows from the fact that `|X^an| = X(ℂ)` (XIII.1.1) and
from the fact that `X` is Jacobson (EGA IV 10.4.8). To say that `X`, respectively `X^an`, is discrete is equivalent to
saying that `dim X = 0`, respectively `dim X^an = 0` by [XII.4, no. 19, §4, cor. 6]; hence (i′) follows from (viii).

Let `P` be one of the properties (ii) through (vii). For `X` to have property `P`, it is necessary and sufficient that
`P` hold at every closed point of `X`. Indeed, since `X` is excellent (EGA IV 7.8.6 (iii)), the set of points

<!-- original page 317 -->

where `X` satisfies `P` is open, and if this open contains all closed points, it is equal to all of `X`. Thus to say
that `X`, respectively `X^an`, has property `P` is equivalent to saying that for every point `x` of `X^an`, the local
ring `𝒪_X,φ(x)`, respectively `𝒪_X^an,x`, has property `P`. Since the fact that an excellent local ring has property `P`
can be detected after passage to the completion, the proposition follows from the isomorphisms

```text
𝒪̂_X,φ(x) ≃ 𝒪̂_X^an,x
```

in cases (ii) through (vii). The same holds in case (viii), taking into account the relations

```text
dim X = sup_x dim 𝒪_X,φ(x),     dim X^an = sup_x dim 𝒪_X^an,x,
```

where `x ∈ X^an`. This completes the proof.

**Proposition.**

<!-- label: XII.2.2 -->

Let `X` be a `ℂ`-scheme locally of finite type, let `φ: X^an → X` be the canonical morphism, and let `T` be a locally
constructible subset of `X`. Then one has the relation

```text
φ⁻¹(closure(T)) = closure(φ⁻¹(T)).
```

We may suppose that `T` is a dense open subset of `X`. Let `H` be the reduced closed subscheme of `X` whose underlying
space is `X − T`. The associated space `H^an` is a closed analytic subspace of `X^an` whose underlying space is
`X^an − φ⁻¹(T)`. We must show that every point `x` of `H^an` belongs to `closure(φ⁻¹(T))`. But at such a point `x`, the
germ of analytic space `(X^an,x)` contains the subgerm `(H^an,x)`, and this is defined by a non-nilpotent ideal of
`𝒪_X^an,x`. It then follows from the Nullstellensatz [XII.4, no. 19, §4, cor. 3] that every open neighborhood of `x`
contains points of `X^an` which do not belong to `H^an`. This proves that `x ∈ closure(φ⁻¹(T))`.

**Corollary.**

<!-- label: XII.2.3 -->

Let

<!-- original page 318 -->

`X` be a `ℂ`-scheme locally of finite type, let `φ: X^an → X` be the canonical morphism, and let `T` be a locally
constructible subset of `X`. For `T` to be an open subset, respectively a closed subset, respectively a dense subset, it
is necessary and sufficient that `φ⁻¹(T)` have the corresponding property.

The corollary follows from XII.2.2 and from the fact that, since `X` is a Jacobson scheme (EGA IV 10.4.8), two locally
constructible subsets of `X` that have the same trace on the very dense set `X(ℂ)` are equal.

**Proposition.**

<!-- label: XII.2.4 -->

Let `X` be a `ℂ`-scheme locally of finite type. For `X` to be connected, respectively irreducible, it is necessary and
sufficient that `X^an` be connected, respectively irreducible.

Suppose `X^an` is connected, respectively irreducible. The image `X(ℂ)` of `X^an` in `X` is then connected, respectively
irreducible. It follows that `X` is connected, respectively irreducible, because closed subsets of `X` and of `X(ℂ)`
correspond bijectively (EGA IV 10.1.2).

Conversely suppose `X` is connected, respectively irreducible, and let us show that the same is true of `X^an`. We may
restrict to the case where `X` is irreducible. Indeed, suppose `X` is connected. Given a point `x` of `X`, the set of
points `y ∈ X` for which there exists a finite sequence of irreducible closed subschemes `X₁, …, X_n` of `X`, with
`x ∈ X₁`, `y ∈ X_n`, and `X_i ∩ X_{i+1} ≠ ∅` for `1 ≤ i ≤ n − 1`, is both open and closed, hence equal to all of `X`.
For a sequence `X₁, …, X_n` as above, one also has `X_i^an ∩ X_{i+1}^an ≠ ∅` for `1 ≤ i ≤ n − 1`; if the `X_i^an` are
known to be connected, then `X^an` is connected as well.

From now on

<!-- original page 319 -->

suppose `X` is irreducible. We may also suppose `X` affine. Indeed, if `(U_i)_{i∈I}` is a covering of `X` by affine
opens, any two of these opens have nonempty intersection, and the same property is therefore true for the covering
`(U_i^an)_{i∈I}` of `X^an`. If the `U_i^an` are known to be irreducible, then `X^an` is irreducible as well.

We may further suppose that `X` is normal. Indeed, let `X̃` be the normalization of `X`. Since the morphism `X̃ → X` is
surjective, so is `X̃^an → X^an`, which proves that if `X̃^an` is irreducible, then `X^an` is irreducible as well.

From now on suppose `X` is affine normal. Since the local rings of `X^an` are integral domains, saying that `X^an` is
irreducible is equivalent to saying that it is connected. Indeed, if `𝓕` is a closed analytic subset of `X^an`, the set
of points `x` of `X^an` at which `codim_x(𝓕,X^an) = 0` is a closed analytic subset of `X^an` [XII.4, no. 20 A, cor. 1]
which is also open. If `X^an` is connected, this proves that, whenever `𝓕 ≠ X^an`, `𝓕` is rare; hence `X^an` is
irreducible. We are thus reduced to showing that `X^an` is connected.

Let

```text
i: X → P
```

be a compactification of `X`, where `P` is a normal projective `ℂ`-scheme and `i` is a dominant open immersion. It then
follows from [XII.10, no. 12, th. 1] that `P^an` is connected. Since `X^an` is obtained by removing from `P^an` a rare
closed analytic subset, it follows from XII.2.5 below that `X^an` is also connected.

**Lemma.**

<!-- label: XII.2.5 -->

Let

<!-- original page 320 -->

`𝓟` be a connected normal analytic space, and let `𝓨` be a rare closed analytic subset. Then `𝓧 = 𝓟 − 𝓨` is connected.

When `𝓨` has codimension `≥ 2`, the proposition follows from [XII.11, no. 3, prop. 4]. In the general case one may
suppose, after removing from `𝓟` a closed analytic subset of codimension `≥ 2`, that `𝓟` and `𝓨`, regarded as a reduced
analytic subspace of `𝓟`, are regular. By the implicit function theorem, every point `y` of `𝓨` has a neighborhood `𝓤`
isomorphic to a ball in an affine space `𝓔ⁿ`, such that `𝓤 ∩ 𝓨` is defined by the vanishing of a certain number of
coordinate functions. This proves that `𝓤 − 𝓤 ∩ 𝓨` is connected, and hence that `𝓧` is connected.

**Corollary.**

<!-- label: XII.2.6 -->

Let `X` be a `ℂ`-scheme locally of finite type. The morphism

```text
π₀(X^an) → π₀(X)
```

induced by the canonical morphism `X^an → X` is bijective.

## 3. Comparison of Properties of Morphisms

<!-- label: XII.3 -->

**Proposition.**

<!-- label: XII.3.1 -->

Let `f: X → Y` be a morphism of `ℂ`-schemes locally of finite type, and let `f^an: X^an → Y^an` be the morphism deduced
from `f` on the associated analytic spaces. Let `P` be the property of being:

```text
(i)    flat
(ii)   net, that is, unramified
(iii)  étale
(iv)   smooth
(v)    normal
(vi)   reduced
(vii)  injective
(viii) separated
(ix)   an isomorphism
(x)    a monomorphism
(xi)   an open immersion.
```

Then `f` has property `P` if and only if `f^an` has property `P`.

Let `φ: X^an → X` and `ψ: Y^an → Y` be the canonical morphisms. Let `x` be a point of `X^an`, and put `y = f^an(x)`. The
morphisms `𝒪_Y^an,y → 𝒪_X^an,x` and `𝒪_Y,ψ(y) → 𝒪_X,φ(x)` deduced from `f^an` and `f` give the same morphism after
passage to completions (XII.1.1). By [XII.2, ch. 3, §5, prop. 4], respectively EGA IV 17.4.4, it is therefore equivalent
to say that `f^an` satisfies property (i), respectively (ii), and to say that `f` satisfies (i), respectively (ii), at
every closed point of `X`. Since the set of points of `X` where (i), respectively (ii), holds is open (EGA IV 11.1.1 and
I 3.3), this proves (i) and (ii), hence also (iii).

Let `P` be property (iv), respectively (v), respectively (vi). Taking XII.2.1 ((v), (vi), (vii)) into account, it is
equivalent to say that the geometric fibers of `f^an` at the various points `y` of `Y^an` are regular, respectively
normal, respectively reduced, and to say that the same is true of the geometric fibers of `f` at the various closed
points `ψ(y)` of `Y`. Cases (iv), respectively (v), respectively (vi), then follow from (i) and from the fact that the
set of points of `Y` where the geometric fibers of `f` are regular is open (EGA IV 12.1.7).

(vii). If `f` is injective, so is `f^an`. Conversely suppose `f^an` is injective and let us show that `f` is injective.
We may suppose

<!-- original page 322 -->

`f` of finite type. Since `f^an` is injective, the fibers of `f` at closed points of `Y` are radicial. Since the set of
points of `Y` whose fiber is radicial is locally constructible (EGA IV 9.6.1), and since `Y` is a Jacobson scheme, all
fibers of `f` are radicial; hence `f` is injective.

(viii). Let `Δ: X → X ×_Y X` and `Δ^an: X^an → X^an ×_{Y^an} X^an` be the diagonal immersions, and let
`Θ: X^an ×_{Y^an} X^an → X ×_Y X` be the canonical morphism. By XII.2.3, saying that `Δ(X)` is closed in `X ×_Y X` is
equivalent to saying that `Δ^an(X^an)` is closed in `X^an ×_{Y^an} X^an`.

Since an open immersion is nothing other than an étale injective morphism (EGA IV 17.9.1 and [XII.4, no. 13, §1]), (xi)
follows from (iii) and (vii). Since an isomorphism is the same thing as a surjective open immersion, (ix) follows from
(xi) and XII.3.2 (i) below. Saying that `f` is a monomorphism is equivalent to saying that the diagonal morphism
`Δ: X → X ×_Y X` is an isomorphism, so (x) follows from (ix).

**Proposition.**

<!-- label: XII.3.2 -->

Let `X` and `Y` be two `ℂ`-schemes locally of finite type, let `f: X → Y` be a morphism of finite type, and let
`f^an: X^an → Y^an` be the morphism deduced from `f` on the associated analytic spaces. Let `P` be the property of
being:

```text
(i)   surjective
(ii)  dominant
(iii) a closed immersion
(iv)  an immersion
(v)   proper
(vi)  finite.
```

Then `f` has property `P` if and only if `f^an` has property `P`. \[Translator note: the source footnote says that a
morphism of analytic spaces is called proper if it is proper in the sense of [XII.1, ch. 1, §10, no. 1] and is
separated.\]

<!-- original page 323 -->

Let `φ: X^an → X` and `ψ: Y^an → Y` be the canonical morphisms.

(i). If `f` is surjective, then for every point `y` of `Y^an`, `f⁻¹(ψ(y))` is a nonempty closed subset of `X`; hence it
contains at least one closed point, which proves that `f^an` is surjective. Conversely, if `f^an` is surjective, `f(X)`
is a locally constructible subset of `Y` (EGA IV 1.8.4) containing all closed points of `Y`; hence `f(X) = Y`.

(ii) follows from XII.2.2.

(iii). If `f` is a closed immersion, then so is `f^an` by XII.1.1 a. Conversely, if `f^an` is a closed immersion, then
so is `f` by XII.3.1 (x) and XII.3.2 (v), since this is equivalent to saying that `f` is a proper monomorphism (EGA IV
8.11.5).

(iv). It is clear that if `f` is an immersion, then so is `f^an`. Conversely suppose `f^an` is an immersion, and let `T`
be the image of `X` in `Y`, and `T̄` the scheme-theoretic closure of `f`. There is a factorization of `f`

```text
X --i→ T̄ --j→ Y,
```

where `j` is a closed immersion and `i` is the canonical morphism; from it one deduces the following factorization of
`f^an`:

```text
X^an --i^an→ T̄^an --j^an→ Y^an.
```

Since

<!-- original page 324 -->

`T = f(X)` is a locally constructible subset of `Y` (EGA IV 1.8.4), one has, by XII.2.2, `T̄^an = closure(f^an(X^an))`.
It follows that `i^an(X^an)` is open in `T̄^an`, hence that `i(X)` is open in `T̄`. Consider the canonical factorization
of `i`

```text
X --i₁→ i(X) --i₂→ T̄.
```

The morphism `i₁^an` is a proper monomorphism, hence so is `i₁` by XII.3.2 (v) and XII.3.1 (x). This proves that `i₁`,
and hence also `f`, is an immersion.

(v). Suppose `f` is proper and let us show that `f^an` is proper. Since properness of `f^an` is local on `Y^an`, we may
suppose `Y` affine. By Chow’s lemma (EGA II 5.6.1), one can find a projective `Y`-scheme `X′` and a projective
surjective morphism

```text
g: X′ → X.
```

The morphism `(fg)^an = f^an g^an` is projective, hence proper; `g^an` is surjective; and it follows from \[XII.1, ch.
1, §10\] that `f^an` is proper.

Conversely suppose `f^an` is proper and let us show that `f` is proper. By XII.3.1 (viii), `f` is separated. It remains
to prove that `f` is universally closed, and it is even enough to show that `f` is closed. Indeed, for every `Y`-scheme
`Y′` locally of finite type, the morphism

```text
f_(Y′) = h: X ×_Y Y′ → Y′
```

will also be closed since `h^an` is proper. Let `T` be a closed subset of `X`. The set `f(T)` is locally constructible,
and one has

```text
f^an(φ⁻¹(T)) = ψ⁻¹(f(T)).
```

Since

<!-- original page 325 -->

`f^an` is proper, `ψ⁻¹(f(T))` is a closed subset of `Y^an`, and therefore it follows from XII.2.2 that

```text
ψ⁻¹(closure(f(T))) = ψ⁻¹(f(T)).
```

This implies `f(T) = closure(f(T))`, that is, `f` is closed; hence `f` is proper.

(vi). Saying that a morphism is finite is equivalent to saying that it is proper with finite fibers (EGA III 4.4.2 and
[XII.4, no. 19, §5]). Since the set of points where the fibers of `f` are finite is locally constructible (EGA IV
9.7.9), the fibers of `f` are finite if and only if the fibers of `f^an` are finite. Thus (vi) follows from (v).

**Remark.**

<!-- label: XII.3.3 -->

a. Let `f: X → Y` be a morphism of `ℂ`-schemes locally of finite type. The fact that `f^an` is a local isomorphism does
not imply that `f` is one. Indeed, if `f` is étale, `f^an` is étale and hence is a local isomorphism \[XII.4, no. 13,
§1\], but this need not be true of `f`.

b. The statement XII.3.2 is not true if `f` is not assumed of finite type. For example, `f^an` can be a closed immersion
without `f` being one. It is enough to take `X` to be the sum of `ℤ` copies of `Spec ℂ`, `Y` to be the affine line, and
`f` the morphism obtained by sending the points of `X` to distinct points of `Y` forming a discrete subset.

## 4. Cohomological Comparison Theorems and Existence Theorems

<!-- label: XII.4 -->

<!-- original page 326 -->

The purpose of this number is to reprove the results of [XII.3, no. 2, ths. 5 and 6]. These generalize to the case of a
proper scheme the theorems established in [XII.10, no. 12] when `X` is projective, and extend them to the relative case.
More general results, concerning relative proper schemes over an analytic space, are proved in [XII.7, ch. VIII, no. 3].

Recall that the Čech cohomology used in [XII.10, no. 12] coincides with the usual cohomology in the algebraic case as
well as in the analytic case (EGA III 1.4.1 and [XII.5, II 5.10]).

### 4.1.

<!-- label: XII.4.1 -->

Let `f: X → Y` be a morphism of `ℂ`-schemes locally of finite type, and consider the commutative diagram

```text
X^an --φ→ X
 |        |
f^an     f
 |        |
Y^an --ψ→ Y.
```

If `F` is an `𝒪_X`-module, then for every integer `p ≥ 0` one has morphisms

```text
Rᵖf_*F --i→ Rᵖf_*(φ_*F^an) --j→ Rᵖ(f·φ)_*F^an --k→ ψ_*(Rᵖf_*^an F^an),
```

where `i` is deduced from the canonical morphism `F → φ_*F^an`, and `j`, `k` are “edge homomorphisms” of Leray spectral
sequences. With the composite `k · j · i` there is associated a canonical morphism

<!-- label: eq:XII.4.1.1 -->

```text
(4.1.1)   θ_p: (Rᵖf_*F)^an → Rᵖf_*^an(F^an).
```

**Theorem.**

<!-- label: XII.4.2 -->

Let

<!-- original page 327 -->

`f: X → Y` be a proper morphism of `ℂ`-schemes locally of finite type, and let `F` be a coherent `𝒪_X`-module. Then, for
every integer `p ≥ 0`, the morphism (4.1.1)

```text
θ_p: (Rᵖf_*F)^an → Rᵖf_*^an(F^an)
```

is an isomorphism.

1. **The case where `f` is projective.** The proof is analogous to that of [XII.10, no. 13]. Let us recall it briefly.
    One reduces to the case where `X` is a projective space of type `ℙ^r_Y` over `Y`. Let `𝓨 = Y^an` and `𝓟 = ℙ^r_𝓨`.
    One first proves that

```text
f_*^an 𝒪_𝓟 = 𝒪_𝓨,     Rᵖf_*^an(𝒪_𝓟) = 0 for p > 0.
```

To verify the preceding relations, one may reduce to the case where `𝓨` is a ball `𝓑` in an affine space `𝓔ⁿ`. One
considers the “standard covering” `{𝓤_i}` of `𝓟` by `r + 1` open subsets isomorphic to `𝓑 × 𝓔^r`. Since these opens are
Stein, one has, for every integer `p ≥ 0`, isomorphisms

```text
Hᵖ({𝓤_i},𝒪_𝓟) ≃ Hᵖ(𝓟,𝒪_𝓟).
```

One can then express the sections of the structural sheaf `𝒪_𝓟` on the opens `𝓤_i` and on their intersections in terms
of Laurent series. An easy calculation proves that

```text
H⁰(𝓟,𝒪_𝓟) ≃ H⁰(𝓨,𝒪_𝓨),     Hᵖ(𝓟,𝒪_𝓟) = 0 for p > 0.
```

The proof is then completed by copying [XII.10, no. 12, lemma 5], with cohomology groups replaced by cohomology sheaves.

2.

<!-- original page 328 -->

**The case where `f` is proper.** One uses EGA III 3.1.2 to reduce to the projective case. Let `𝓚` be the category of
coherent `𝒪_X`-modules such that `θ_p` is an isomorphism for every `p ≥ 0`. It is enough to prove that, for every exact
sequence `0 → F′ → F → F″ → 0` whose two terms are in `𝓚`, the third is also in `𝓚`; that a direct factor of an object
of `𝓚` is in `𝓚`; and that, for every point `x` of `X`, one can find an object `F` of `𝓚` such that `F_x ≠ 0`.

The first condition follows by applying the five lemma to the following commutative diagram, whose rows are exact:

```text
… → (Rᵖf_*F′)^an → (Rᵖf_*F)^an → (Rᵖf_*F″)^an → (Rᵖ⁺¹f_*F′)^an → …
      ↓                ↓                 ↓                   ↓
… → Rᵖf_*^an F′^an → Rᵖf_*^an F^an → Rᵖf_*^an F″^an → Rᵖ⁺¹f_*^an F′^an → …
```

The second condition is verified analogously.

To verify the third condition, one may restrict to the case where `X` is an irreducible scheme with generic point `x`.
We could have supposed `Y` noetherian from the beginning. By Chow’s lemma (EGA II 5.6.1), one can find a projective
`Y`-scheme `X′` and a projective surjective morphism `g: X′ → X`. On the other hand, there exists an integer `n` such
that `Rᵖg_*(𝒪_X′(n)) = 0` for all `p > 0` and such that the canonical morphism `g*g_*(𝒪_X′(n)) → 𝒪_X′(n)` is surjective
(EGA III 2.2.1). If one puts `F = g_*(𝒪_X′(n))`, the sheaf `F` answers the question. Indeed `F_x ≠ 0`; moreover, the
Leray spectral sequence

```text
Rᵖf_*(R^qg_*(𝒪_X′(n))) ⇒ R^(p+q)(f·g)_*(𝒪_X′(n))
```

is degenerate, so one has an isomorphism

```text
Rᵖf_*F ≃ Rᵖ(f·g)_*(𝒪_X′(n)).
```

<!-- original page 329 -->

As in the algebraic case, one has a canonical isomorphism

```text
Rᵖf_*^an F^an ≃ Rᵖ(f·g)_*^an(𝒪_X′(n)^an),
```

and the diagram

```text
(Rᵖf_*F)^an  ≃  (Rᵖ(f·g)_*(𝒪_X′(n)))^an
      ↓ θ_p                ↓ ψ_p
Rᵖf_*^an F^an ≃ Rᵖ(f·g)_*^an(𝒪_X′(n)^an)
```

is commutative. By 1, `ψ_p` is an isomorphism; hence `θ_p` is also an isomorphism. This completes the proof.

**Corollary.**

<!-- label: XII.4.3 -->

Let `X` be a proper `ℂ`-scheme, and let `F` be a coherent `𝒪_X`-module. Then, for every integer `p ≥ 0`, the canonical
morphism

```text
Hᵖ(X,F) → Hᵖ(X^an,F^an)
```

is an isomorphism.

**Theorem.**

<!-- label: XII.4.4 -->

Let `X` be a proper `ℂ`-scheme. The functor which associates to every coherent `𝒪_X`-module `F` its inverse image `F^an`
on `X^an` is an equivalence of categories.

1. **The functor is fully faithful.** Indeed, let `F` and `G` be two coherent `𝒪_X`-modules. The canonical morphism

```text
Hom_𝒪_X(F,G) → Hom_𝒪_X^an(F^an,G^an)
```

identifies with the canonical morphism

```text
H⁰(X,SheafHom_𝒪_X(F,G)) → H⁰(X^an,SheafHom_𝒪_X(F,G))
```

<!-- original page 330 -->

(EGA `0_I` 6.7.6). Since `SheafHom_𝒪_X(F,G)` is coherent, it follows from XII.4.3 that this morphism is bijective.

1. **The functor is essentially surjective.** When `X` is projective, the assertion follows from \[XII.10, no. 12, th.
    3\]. The general case reduces to the preceding one by using Chow’s lemma (EGA II 5.6.1). Indeed, let `X′` be a
    projective `ℂ`-scheme, let `f: X′ → X` be a projective surjective morphism, and let `U` be a dense open subset of
    `X` such that `f` induces an isomorphism `f⁻¹(U) ≃ U`. We reason by noetherian induction on `X`; hence we may
    suppose that for every coherent sheaf `𝓖` on `X^an` for which one can find a closed subset `Y` of `X`, distinct
    from `X`, satisfying `Y^an ⊃ Supp 𝓖`, there exists a coherent sheaf `G` on `X` such that `G^an ≃ 𝓖`.

Let `𝓕` be a coherent sheaf of modules over `𝒪_X^an`, and let `𝓚` and `𝓛` be the coherent sheaves defined by requiring
the sequence

```text
0 → 𝓚 → 𝓕 → f_*^an f^an*𝓕 → 𝓛 → 0
```

to be exact. Since `X′` is projective, there exists a coherent `𝒪_X′`-module `F′` such that `F′^an ≃ f^an*𝓕`. From
XII.4.2 one then deduces an isomorphism `(f_*F′)^an ≃ f_*^an f^an*𝓕`. Since `𝓚|U^an` and `𝓛|U^an` are zero, there exist
coherent `𝒪_X`-modules `K` and `L` such that `K^an ≃ 𝓚` and `L^an ≃ 𝓛`. By 1, the morphism `f_*^an f^an*𝓕 → 𝓛` comes
from a unique morphism `f_*F′ → L`. Let `I = Ker(f_*F′ → L)`. The sheaf `𝓕` is then an extension of `I^an` by `K^an`,
and it remains only to see that this extension comes

<!-- original page 331 -->

by inverse image from an extension of `I` by `K`. It is therefore enough to prove that the canonical morphism

<!-- label: eq:XII.4.* -->

```text
(*)   Ext^q_𝒪_X(I,K)^an ≃ Ext^q_𝒪_X^an(I^an,K^an),     q = 1,
```

is bijective. \[Translator note: the source prints “`q ≠ 1`,” but the preceding sentence shows that the needed case is
`q = 1`; this is a mathematical correction rather than a change of argument.\] Now one has isomorphisms

```text
ExtSheaf^q_𝒪_X(I,K)^an ≃ ExtSheaf^q_𝒪_X^an(I^an,K^an)
```

for every integer `q ≥ 0` (EGA `0_III` 12.3.5), and a morphism of spectral sequences

```text
Hᵖ(X,ExtSheaf^q_𝒪_X(I,K))              ⇒ Ext^(p+q)_𝒪_X(I,K)
     ↓                                             ↓
Hᵖ(X^an,ExtSheaf^q_𝒪_X^an(I^an,K^an)) ⇒ Ext^(p+q)_𝒪_X^an(I^an,K^an).
```

This morphism is an isomorphism because, by XII.4.3, it is so on the `E₂^(p,q)`-terms; this proves the bijectivity of
`(*)`.

**Corollary.**

<!-- label: XII.4.5 -->

The functor which associates `X^an` to every proper `ℂ`-scheme `X` is fully faithful.

We must show that, if `X` and `Y` are two proper `ℂ`-schemes, the canonical map

```text
Hom_ℂ(X,Y) → Hom(X^an,Y^an)
```

is bijective. But to give a morphism from `X` to `Y`, respectively from `X^an` to `Y^an`, is equivalent to giving its
graph, that is, a closed subscheme `Z` of `X × Y`, respectively a closed analytic subspace `𝓩` of `X^an × Y^an`, such
that the restriction of the first projection `X × Y → X` to `Z`, respectively of `X^an × Y^an → X^an` to `𝓩`, is

<!-- original page 332 -->

an isomorphism. Since giving a closed subscheme of `X × Y`, respectively a closed analytic subspace of `X^an × Y^an`, is
equivalent to giving a coherent sheaf of ideals on `𝒪_{X×Y}`, respectively on `𝒪_{X^an×Y^an}`, the corollary follows
from XII.4.4.

**Corollary.**

<!-- label: XII.4.6 -->

Let `X` be a proper `ℂ`-scheme. The functor which associates `X′^an` to every finite, respectively finite étale, scheme
`X′` over `X` is an equivalence from the category of finite, respectively finite étale, schemes over `X` to the category
of finite, respectively finite étale, analytic spaces over `X^an`.

Indeed, to give a finite morphism `X′ → X`, respectively `X′^an → X^an`, is equivalent to giving a coherent sheaf of
algebras over `𝒪_X`, respectively over `𝒪_X^an` [XII.4, no. 19, §5, th. 2]. The corollary therefore follows from XII.4.4
in the non-respective case, and the respective case follows from it in view of XII.3.1 (iii).

## 5. Comparison Theorems for Étale Coverings

<!-- label: XII.5 -->

### 5.0.

<!-- label: XII.5.0 -->

Let us make precise the notion of a finite covering of an analytic space. If `𝓧` is an analytic space, an analytic space
`𝓧′` finite over `𝓧` is called a finite covering of `𝓧` if every irreducible component of `𝓧′` dominates an irreducible
component of `𝓧`.

**Theorem (“Riemann existence theorem”).**

<!-- label: XII.5.1 -->

Let `X` be a `ℂ`-scheme locally of finite type, and let `X^an` be the analytic space associated with `X`. The functor
`Ψ` which associates `X′^an` to every finite étale covering `X′` of `X` is an equivalence

<!-- original page 333 -->

from the category of finite étale coverings of `X` to the category of finite étale coverings of `X^an`.

1. **The functor `Ψ` is fully faithful.** Let `X′` and `X″` be two finite étale coverings of `X`, and let us prove that
    the canonical map

<!-- label: eq:XII.5.* -->

```text
(*)   Hom_X(X′,X″) → Hom_X^an(X′^an,X″^an)
```

is bijective. We may suppose `X′` connected. To give an `X`-morphism from `X′` to `X″` is equivalent to giving a
connected component `X_i` of `X′ ×_X X″` such that the morphism `X_i → X′` induced by the first projection is an
isomorphism. Since the connected components of `X′ ×_X X″` correspond bijectively to the connected components of
`X′^an ×_{X^an} X″^an` (XII.2.6), and since a morphism `X_i → X′` is an isomorphism if and only if `X_i^an → X′^an` is
one, this proves the bijectivity of `(*)`.

1. **The functor `Ψ` is essentially surjective.** Let `𝓧′` be a finite étale covering of `X^an`, and let us prove that
    there exists an étale covering `X′` of `X` such that one has an isomorphism `X′^an ≃ 𝓧′`. In view of 1, the
    question is local on `X`, so we may suppose `X` affine.

a. **Reduction to the case where `X` is normal.** We may suppose `X` reduced. Indeed, suppose the theorem proved for
`X_red`. The functor which associates to a finite étale covering `X′` of `X` the finite étale covering `X′^an_red` of
`X_red^an` is then an equivalence. Since it is obtained by composing `Ψ` with the functor `Θ` which associates to a
finite étale covering of `X^an` its inverse image on `X_red^an`, and since `Θ` is fully faithful, this shows that `Ψ` is
an equivalence of categories.

We

<!-- original page 334 -->

may suppose `X` normal. Indeed, let `X̃` be the normalization of `X`, and let `p: X̃ → X` be the canonical morphism.
Since `p` is finite, `p` is a morphism of effective descent for the category of étale coverings (IX.4.7). Supposing the
theorem proved for `X̃`, put `𝓧̃′ = 𝓧′ ×_{X^an} X̃^an`. There exists an étale covering `X̃′` of `X̃` and an isomorphism
`X̃′^an ≃ 𝓧̃′`. It then follows from 1 that the natural descent datum on `𝓧̃′` lifts to a descent datum on `X̃′`
relative to `X̃ → X`. This proves the existence of an étale covering `X′` of `X` such that one has an isomorphism

```text
i: X′^an ×_{X^an} X̃^an ≃ 𝓧̃′,
```

whose inverse images by the two projections from `X̃^an ×_{X^an} X̃^an` are the same. By IX.3.2, whose proof is valid in
the analytic case, the morphism `X̃^an → X^an` is a morphism of descent for the category of étale coverings, and
consequently `i` comes from an isomorphism `X′^an ≃ 𝓧′`.

b. **Reduction to the case where `X` is regular.** Let `U` be the open subset of regular points of `X`, and let
`i: U → X` and `i^an: U^an → X^an` be the canonical morphisms. Since `X` is normal, one has `codim(X − U, X) ≥ 2`.
Suppose that there exists an étale covering `U′` of `U` such that `U′^an ≃ 𝓧′|U^an`, and let us show that `U′` then
extends to an étale covering `X′` of `X` such that `X′^an ≃ 𝓧′`. It is enough to see that `U′` extends to an étale
covering `X′` of `X`. Indeed, one will then have an isomorphism `X′^an|U^an ≃ 𝓧′|U^an`; but if `𝓕` and `𝓖` are the
coherent sheaves of algebras on `𝒪_X^an` defining respectively `𝓧′` and `X′^an`, the fact that `X` is normal and that
`codim(X − U, X) ≥ 2` implies that the canonical morphisms

```text
𝓕 → i_*^an(𝓕|U^an),     𝓖 → i_*^an(𝓖|U^an)
```

are

<!-- original page 335 -->

isomorphisms [XII.11, no. 3, prop. 4]. It follows that `𝓕` and `𝓖`, and hence also `X′^an` and `𝓧′`, are isomorphic.

Let `φ: X^an → X` be the canonical morphism. Since the problem of extending `U′` to `X` is local on `X`, it is enough to
prove that, for every point `y` of `X^an − U^an`, the étale covering

```text
U′_φ(y) = U′ ×_X Spec 𝒪_X,φ(y)
```

of

```text
U_φ(y) = U ×_X Spec 𝒪_X,φ(y)
```

extends to `Spec 𝒪_X,φ(y)`. Let `H` be the coherent `𝒪_U`-algebra defining `U′`. The canonical morphism

```text
α: (i_*H)^an → i_*^an(H^an) = 𝓕
```

defines a morphism of sheaves of modules on `Spec 𝒪_X^an,y`:

```text
α_y: (i_*H)^an_y → 𝓕_y,
```

whose restriction to

```text
U_y = U_φ(y) ×_{Spec 𝒪_X,φ(y)} Spec 𝒪_X^an,y
```

is an isomorphism. But this proves that `H|U_y` is trivial, hence that `U′_φ(y)` extends to `Spec 𝒪_X,φ(y)`.

c. **The case where `X` is affine regular.** Let

```text
j: X → P
```

be a compactification of `X`, where `P` is a projective `ℂ`-scheme and `j` is a dominant open immersion. By the
resolution of singularities theorem [XII.8], one can find a regular scheme `R` and a projective morphism `r: R → P`,
such that `r` induces an isomorphism `r⁻¹(X) ≃ X` and such that `r⁻¹(X)` is the complement in `R` of a divisor with
normal crossings. Let

<!-- original page 336 -->

```text
k: X → R
```

be the canonical immersion. We shall show that there exists a finite normal covering `𝓡′` of `R^an`, in the sense of
XII.5.0, which extends the étale covering `X′^an`. By Proposition XII.5.3 below, such a covering is unique; the problem
of extending `X′^an` is therefore local on `R^an` near `R^an − X^an`. But each point of `R^an − X^an` has an open
neighborhood `𝓥` isomorphic to a ball in an affine space `𝓔ⁿ`, such that `𝓥 − 𝓥 ∩ X^an` is defined by the vanishing of
the first `p` coordinate functions `z₁, …, z_p`, with `0 ≤ p ≤ n`. The fundamental group of `𝓤 = 𝓥 ∩ X^an` is isomorphic
to `ℤᵖ`, and every étale covering of `𝓤` is a quotient of a covering of the form

```text
𝓤″ = 𝓤[T₁,…,T_p]/(T₁ⁿ¹ − z₁, …, T_pⁿᵖ − z_p),
```

where the `n_i` are integers `> 0`, by a subgroup `H` of the Galois group `ℤ/n₁ℤ × ⋯ × ℤ/n_pℤ` of `𝓤″`. But `𝓤″` extends
to the regular covering

```text
𝓥″ = 𝓥[T₁,…,T_p]/(T₁ⁿ¹ − z₁, …, T_pⁿᵖ − z_p)
```

of `𝓥` on which `H` acts, and the quotient of `𝓥″` by `H` is the desired extension.

The proof is then completed by XII.4.6. The covering `𝓡′` comes from a finite covering `R′` of `R`; the restriction of
`R′` to `X` is a covering `X′` of `X` such that `X′^an ≃ 𝓧′`, and by XII.3.1 (iii), `X′` is an étale covering of `X`.

**Corollary.**

<!-- label: XII.5.2 -->

Let

<!-- original page 337 -->

`X` be a connected `ℂ`-scheme locally of finite type, let `φ: X^an → X` be the canonical morphism, and let `x` be a
point of `X^an`. Let `π₁(X^an,x)` be the fundamental group of the topological space `X^an` at `x`, and let `π₁(X,φ(x))`
be the fundamental group of the scheme `X` at `φ(x)` (V.7). Then `π₁(X,φ(x))` is canonically isomorphic to the
completion of `π₁(X^an,x)` for the topology of subgroups of finite index.

Indeed, let `𝓒` be the category of finite étale coverings of `X^an`, let `F` be the functor from `𝓒` to Sets which
associates to every finite étale covering `𝓧′` of `X^an` the set of points of `𝓧′` above `x`, and let `π̂₁(X^an,x)` be
the profinite group associated with `𝓒` and `F` as in V.4. Since every finite étale covering of `X^an` is a quotient of
the universal covering by a subgroup of finite index, `π̂₁(X^an,x)` is nothing other than the completion of `π₁(X^an,x)`
for the topology of subgroups of finite index. The corollary therefore follows from XII.5.1 and V.6.10.

**Proposition.**

<!-- label: XII.5.3 -->

Let `𝓧` be a normal analytic space, and let `𝓨` be a closed analytic subset such that `𝓤 = 𝓧 − 𝓨` is dense in `𝓧`. Then
the functor which associates to every normal finite covering `𝓧′` of `𝓧`, in the sense of XII.5.0, its restriction to
`𝓤` is fully faithful.

Let `𝓧′` and `𝓧″` be two finite normal coverings of `𝓧`. We must show that the canonical map

```text
Hom_𝓧(𝓧′,𝓧″) → Hom_𝓤(𝓧′|𝓤,𝓧″|𝓤)
```

is bijective. Let `u`, `v` be two `𝓧`-morphisms from `𝓧′` to `𝓧″` whose restrictions to `𝓤` are the same, and let us
prove that `u = v`. The morphisms `u` and

<!-- original page 338 -->

`v` coincide on the dense open `𝓤 ×_𝓧 𝓧′`, hence on the underlying topological spaces. By [XII.4, no. 19, §4, cor. 5],
this proves `u = v`.

Let now `u` be a `𝓤`-morphism from `𝓧′|𝓤` to `𝓧″|𝓤`, and let us show that it extends to all of `𝓧′`. We may suppose `𝓧′`
regular. Indeed, since `𝓧′` is normal, one can find an open subset `𝓥` of `𝓧` whose complement is an analytic subset of
codimension `≥ 2`, such that `𝓧′ ×_𝓧 𝓥 = 𝓥′` is regular. Let `𝓥″ = 𝓧″ ×_𝓧 𝓥`, and suppose the proposition proved for
`𝓥`. Consider the commutative diagram

```text
𝓥′  → 𝓧′
 ↓      ↓
𝓥   → 𝓧

and similarly 𝓥″ → 𝓧″ over 𝓥 → 𝓧.
```

With `u` there is associated a morphism of `𝒪_𝓥`-algebras

```text
g″_*𝒪_𝓥″ → g′_*𝒪_𝓥′,
```

from which one deduces a morphism

```text
i_*g″_*𝒪_𝓥″ → i_*g′_*𝒪_𝓥′.
```

Taking into account the isomorphisms `i′_*𝒪_𝓥′ ≃ 𝒪_𝓧′` and `i″_*𝒪_𝓥″ ≃ 𝒪_𝓧″` [XII.11, no. 3, prop. 4], one deduces a
morphism of `𝒪_𝓧`-algebras

```text
f″_*𝒪_𝓧″ → f′_*𝒪_𝓧′,
```

hence the desired morphism `𝓧′ → 𝓧″`.

We

<!-- original page 339 -->

now suppose `𝓧′` regular. Let `𝓤′ = 𝓤 ×_𝓧 𝓧′` and `𝓨′ = 𝓧′ − 𝓤′`. We regard `𝓨′` as a reduced analytic subspace of `𝓧′`.
If `𝓨′₁` is the singular closed subset of `𝓨′`, then `dim 𝓨′₁ < dim 𝓨′` [XII.4, no. 20 D, th. 3]. Thus, by induction on
the dimension of `𝓨′`, one may suppose `𝓨′` smooth. Since it is enough to extend `u` to an open neighborhood of each
point of `𝓨′`, the implicit function theorem lets us suppose that `𝓧′` is a ball in an affine space `𝓔ⁿ` and that `𝓨′`
is the closed subset defined by the vanishing of the first `p` coordinate functions `z₁, …, z_p`, with `0 ≤ p ≤ n`.

To `u` one associates a section `s` of

```text
p: 𝓧′ ×_𝓧 𝓧″ → 𝓧′
```

above `𝓤′`. After restricting `𝓧′` if necessary, one may suppose that `p_*(𝒪_{𝓧′×_𝓧𝓧″})` is generated by elements
`x₁, …, x_q` of `Γ(𝓧′, p_*𝒪_{𝓧′×_𝓧𝓧″})`. Let `u₁, …, u_q ∈ Γ(𝓤′,𝒪_𝓧′)` be the images by `s` of `x₁|𝓤′, …, x_q|𝓤′`.
Saying that `s` extends to `𝓧′` is equivalent to saying that `u₁, …, u_q` extend to sections of `Γ(𝓧′,𝒪_𝓧′)`. But, since
`f` is finite, each `u_i` is a Laurent series in `z₁, …, z_p` with coefficients that are convergent power series in
`z_{p+1}, …, z_n`, and satisfies integral-dependence relations. It follows that `u_i` is bounded, hence is a convergent
power series in `z₁, …, z_n`, and therefore extends to `𝓧′`.

One may ask whether the functor introduced in XII.5.3 is an equivalence of categories. This question has an answer by
the theorem of Grauert-Remmert [XII.6], for which we give below a proof using resolution of singularities. One could
also have used the Grauert-Remmert theorem to prove XII.5.1; that was what was done before [XII.8] was available.

**Theorem (Grauert-Remmert theorem).**

<!-- label: XII.5.4 -->

Let

<!-- original page 340 -->

`𝓧` be a normal analytic space, and let `𝓨` be a closed analytic subset such that `𝓤 = 𝓧 − 𝓨` is dense in `𝓧`. Let `𝓤′`
be a normal finite covering of `𝓤`. Suppose that there exists a rare closed analytic subset `𝓢` of `𝓧` such that the
restriction of `𝓤′` to `𝓤 − 𝓤 ∩ 𝓢` is étale. Then there exists a normal finite covering `𝓧′` of `𝓧` extending `𝓤′`, and
`𝓧′` is unique up to isomorphism.

Uniqueness follows from XII.5.3. The problem of extending `𝓤′` is therefore local on `𝓧`. We may suppose `𝓤` regular and
`𝓤′` étale over `𝓤`. Indeed, the set of regular points of `𝓤` is a dense open subset `𝓥` of `𝓧` whose complement is an
analytic subset [XII.4, no. 20 D, th. 2], and it is enough to replace `𝓤` by the open subset `𝓥 − 𝓥 ∩ 𝓢`.

Let `y` be a point of `𝓧 − 𝓤` and let us show that one can extend `𝓤′` to a neighborhood of `y`. After restricting `𝓧`
to an open neighborhood of `y`, it follows from the resolution of singularities theorem [XII.8] that one can find a
regular analytic space `𝓧₁` and a projective morphism `f: 𝓧₁ → 𝓧` inducing by restriction to `𝓤` an isomorphism
`𝓤₁ = f⁻¹(𝓤) ≃ 𝓤`, such that `𝓤₁` is the complement in `𝓧₁` of a divisor with normal crossings. Let us show that `𝓤′`
extends to a normal finite covering of `𝓧₁`. Since the question is local on `𝓧₁`, one may suppose that `𝓧₁` is a ball in
an affine space `𝓔ⁿ` and that `𝓧₁ − 𝓤₁` is defined by the vanishing of the first `p` coordinate functions `z₁, …, z_p`,
with `0 ≤ p ≤ n`. \[Translator note: the corrected source fixes `z_q` to `z_p` in this list.\] The étale covering `𝓤′`
of `𝓤₁` is a quotient of a covering of the form

```text
𝓤₂ = 𝓤₁[T₁,…,T_p]/(T₁ⁿ¹ − z₁, …, T_pⁿᵖ − z_p)
```

by a subgroup `H` of the Galois group of `𝓤₂`. The covering `𝓤₂` extends

<!-- original page 341 -->

to the covering

```text
𝓧₂ = 𝓧₁[T₁,…,T_p]/(T₁ⁿ¹ − z₁, …, T_pⁿᵖ − z_p)
```

of `𝓧₁` on which `H` acts, and `𝓧₂/H` extends `𝓤′` to `𝓧₁`.

Let `𝓧′₁` denote the normal finite covering of `𝓧₁` extending `𝓤′`, and let `𝓕₁` be the coherent `𝒪_𝓧₁`-algebra defining
`𝓧′₁`. By the finiteness theorem of Grauert-Remmert [XII.4, no. 15, th. 1.1], `f_*𝓕₁` is a coherent `𝒪_𝓧`-algebra. It
therefore corresponds to a finite covering `𝓧′` of `𝓧`, which is normal since `𝓧′₁` is, and `𝓧′` is the desired
extension of `𝓤′`.

**Remark.**

<!-- label: XII.5.5 -->

In the statement XII.5.4, one cannot remove the hypothesis on the locus of points where the morphism `𝓤′ → 𝓤` is not
étale. For example, let `𝓧` be the unit disk in the complex plane, let `𝓤` be the complement of the origin in `𝓧`, and
let

```text
𝓤′ = 𝓤[T]/(T² − sin(1/z)),
```

where `z` is the coordinate function on `𝓧`. Then `𝓤′` is a normal finite covering of `𝓤` which does not extend to `𝓧`.
Indeed, suppose `𝓤′` extended to a finite covering `𝓧′` of `𝓧`. The locus of points of `𝓧` where the morphism `𝓧′ → 𝓧`
is not étale would then be a closed analytic subset containing all points `z` such that `sin(1/z) = 0`, which is absurd.

One can, however, remove the hypothesis on the singular locus of the morphism `𝓤′ → 𝓤` when `codim(𝓧 − 𝓤,𝓧) ≥ 2`.
Indeed, one may suppose `𝓤` regular. The locus of points of `𝓤` where `𝓤′ → 𝓤` is not étale is a divisor of `𝓤`, and it
follows from the Remmert-Stein theorem [XII.9, th. 3] that it is

<!-- original page 342 -->

the trace on `𝓤` of a divisor of `𝓧`. In this case, if `𝓐` is a coherent `𝒪_𝓤`-algebra such that `𝓤′ = Spec_an(𝓐)`, and
if `i: 𝓤 → 𝓧` is the canonical morphism, it is enough to take `𝓧′ = Spec_an(i_*𝓐)`; indeed one knows that `i_*𝓐` is
coherent [XII.11, no. 1, th. 1]. \[Translator note: the corrected source fixes the adjective “coherent” to agree with
`i_*𝓐`.\]

**Remark (M. Raynaud, added in 2003).**

<!-- label: XII.5.6 -->

There exist nontrivial finitely presented groups `G` which have no subgroups of finite index distinct from `G`, for
example G. Higman’s group; cf. J.-P. Serre, _Arbres et amalgames_, Astérisque no. 46, prop. 6, ch. I, §1. Consequently,
if such a group is realized as the topological fundamental group of a scheme `V` over `ℂ`, say smooth and projective,
the topological space `V_top` underlying `V` is not simply connected, but `V` is algebraically simply connected. At
present no such `V` is known. Let us nevertheless mention that D. Toledo constructed smooth projective schemes `V` over
`ℂ` whose topological fundamental group is not separated for the topology of subgroups of finite index; the natural
morphism `π₁(V_top) → π₁(V_alg)` is not injective. \[D. Toledo, “Projective varieties with non-residually finite
fundamental group,” Publ. Math. IHÉS 77 (1993), pp. 103-119.\]

## Bibliography

<!-- original page 343 -->

1. N. Bourbaki, _Topologie Générale_, Hermann, Paris, 1960.
1. N. Bourbaki, _Algèbre Commutative_, Hermann, Paris, 1961.
1. H. Cartan, Séminaire E.N.S., Paris, 1956-57.
1. H. Cartan, Séminaire E.N.S., Paris, 1960-61.
1. R. Godement, _Théorie des Faisceaux_, Hermann, Paris, 1958.
1. H. Grauert and R. Remmert, “Komplexe Räume,” Math. Ann. 136 (1958), pp. 245-318.
1. M. Hakim, _Schémas relatifs_, thesis, Paris, 1967.
1. H. Hironaka, “Resolution of singularities of an algebraic variety over a field of characteristic zero,” Ann. of Math.
    39 (1964), pp. 109-236.
1. R. Remmert and K. Stein, “Ueber die wesentlichen Singularitäten analytischer Mengen,” Math. Ann. 126 (1953), pp.
    263-306.
1. J.-P. Serre, “Géométrie algébrique et géométrie analytique,” Ann. Inst. Fourier (Grenoble) 6 (1956), pp. 1-42.
1. J.-P. Serre, “Prolongement de faisceaux analytiques cohérents,” Ann. Inst. Fourier (Grenoble) 16 (1966), pp. 363-374.
