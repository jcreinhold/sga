# Exposé XI. Examples and Complements

<!-- label: XI -->

<!-- original page 285 -->

## 1. Projective Spaces, Unirational Varieties

<!-- label: XI.1 -->

**Proposition.**

<!-- label: XI.1.1 -->

Let `k` be an algebraically closed field, and let `X = ℙ^r_k` be projective space of dimension `r` over `k`. Then `X` is
**simply connected**, that is, `π₁(X) = 0`.

For `r = 0` this is trivial. If `r = 1`, one must show that if `X′` is a nonempty connected étale covering of
`X = ℙ¹_k`, then `X′ ≃ X`. The genus formula gives, if `g` and `g′` are the genera of `X` and `X′`,

```text
1 − g′ = d(1 − g),
```

where `d` is the degree of `X′` over `X`. Since `g = 0`, we have `1 − g′ = d`, which forces `d = 1` because `g′ ≥ 0`;
this proves `X′ ≃ X`.

When `r ≥ 2`, one proceeds by induction on `r`, assuming `ℙ^r′` simply connected for `r′ < r`. Applying this to a
hyperplane of `ℙ^r` and using X.2.10, it follows that `ℙ^r` is simply connected. Another proof: by X.1.7 one has

```text
π₁(ℙ¹ × ⋯ × ℙ¹) = π₁(ℙ¹) × ⋯ × π₁(ℙ¹),
```

so `(ℙ¹)^r` is simply connected because `ℙ¹` is. Hence `ℙ^r` is simply connected by birational invariance of the
fundamental group (X.3.4). This proof shows more generally:

**Corollary.**

<!-- label: XI.1.2 -->

Let `X` be a proper normal scheme over an algebraically closed field `k`. If `X` is a rational variety, that is,
integral and with function field a purely transcendental extension of `k`, then `X` is simply connected.

This result applies in particular to Grassmann varieties and, more generally,

<!-- original page 286 -->

to varieties `G/H`, where `G` is a connected linear group over `k` and `H` is an algebraic subgroup containing a Borel
subgroup of `G`.

Recall that a variety **unirational over `k`** means a proper integral scheme over `k` whose function field `K` is
contained in a purely transcendental extension `K′` of `k`, finite over `K` (that is, with the same transcendence degree
over `k` as `K`), or equivalently, for which there exists a dominant rational map `f: ℙ^r_k → X` with `r = dim X`. If
`X` is normal, the reflections preceding X.3.4 show that for every connected étale covering `X′` of `X`, with function
field `L/K`, the `K′`-algebra `L ⊗_K K′` is unramified over the model `ℙ^r`, hence completely decomposed by XI.1.1. This
shows that `L` is `K`-isomorphic to a subextension of `K′/K`. Taking V.8.2 into account, this proves:

**Corollary.**

<!-- label: XI.1.3 -->

The fundamental group of a normal unirational variety over an algebraically closed field is finite.

Notice that in the definition of “unirational,” one did not need `K′/K` to be finite.

**Remarks.**

<!-- label: XI.1.4 -->

The results of this number are, of course, well known. Moreover, J.-P. Serre showed [XI.10] that when `X` is a smooth
projective unirational variety over an algebraically closed field of **characteristic zero**, `X` is simply connected.
His proof is transcendental, using Hodge symmetry.

[M. Raynaud, added in 2003.] Restrict to the case of an algebraically closed field `k` of characteristic `p ≥ 0`. In
characteristic `p > 0`, the definition of a unirational `k`-variety given above is that of a weakly unirational
`k`-variety, as opposed to a strongly unirational `k`-variety, where one also assumes that `K′` is a separable extension
of `K`.

In dimension 2, there exist smooth projective weakly unirational surfaces with nontrivial fundamental group (finite by
XI.1.3), and hence nonrational surfaces; see T. Shioda, “On unirationality of supersingular surfaces,” _Mathematische
Annalen_ **225** (1977), pp. 155–159. By contrast, a strongly unirational surface is rational: this follows from
Castelnuovo’s rationality criterion, extended to characteristic `p > 0` by O. Zariski; cf. J.-P. Serre, Séminaire
Bourbaki no. 146, 1957, and _Œuvres/Collected Papers_, vol. 1, p. 467.

Over the field `ℂ` of complex numbers, examples are known of smooth projective varieties of dimension `≥ 3` that are
unirational and nonrational; cf. P. Deligne, “Variétés unirationnelles non rationnelles (d’après M. Artin et D.
Mumford),” Séminaire Bourbaki no. 402, 1971-72, Lecture Notes vol. 317. A smooth cubic hypersurface in projective
4-space is one such example. Some of these examples extend to characteristic `> 0` to give strongly unirational
nonrational varieties; cf. J.-P. Murre, “Reduction of the proof of the non-rationality of a non singular cubic threefold
to a result of Mumford,” _Compositio Mathematica_ **27** (1973), pp. 63–82.

Let `V` be a normal integral projective `k`-variety. One says that `V` is rationally connected if there exist an
integral finite-type `k`-scheme `T` and a `k`-morphism `F: T × ℙ¹ → V` such that the morphism

```text
T × ℙ¹ × ℙ¹ → V × V,
(t,u,u′) ↦ (F(t,u), F(t,u′))
```

is dominant. In particular, through two sufficiently general rational points of `V` there passes a rational curve. The
terminology is justified by the fact that if `V` is rationally connected, two rational points can be joined by a finite
chain of rational curves. If `k` has characteristic `p > 0`, one strengthens the preceding definition by requiring that
the displayed map be generically smooth. This gives the notion of separably rationally connected variety. Thus
unirational varieties are rationally connected, and in characteristic `p > 0` strongly unirational varieties are
separably rationally connected. J. Kollár showed that separably rationally connected varieties have trivial algebraic
fundamental group; cf. O. Debarre, “Variétés rationnellement connexes (d’après T. Graber, J. Harris, J. Starr et A. J.
de Jong),” Séminaire Bourbaki no. 906, 2001-2002.

## 2. Abelian Varieties

<!-- label: XI.2 -->

Let `k` be an algebraically closed field, let `A` be an abelian variety over `k`, that is, a group scheme over `k`,
proper, smooth, and connected over `k`, and finally let `G` be a commutative group scheme of finite type over `k`.
Denote by `Ext(A,G)` the group of classes of commutative extensions of `A` by `G`, and by `H¹(A,G)` the group of classes
of principal bundles on `A` with group `G` (compare no. XI.4 below). Consider the canonical homomorphism

```text
Ext(A,G) → H¹(A,G).
```

<!-- original page 287 -->

An argument of Serre [XI.5, Chapter VII, Theorem 5] shows that this is an injective homomorphism, whose image is the set
of “primitive elements” of `H¹(A,G)`, that is, the elements `ξ` for which

```text
π*(ξ) = pr₁*(ξ) + pr₂*(ξ),
```

where `pr_i` are the two projections from `A × A` to `A`, and `π: A × A → A` is the composition law of `A`. Serre states
his theorem only for `G` linear and connected, and of course smooth over `k`, but by simplifying the first part of his
argument one sees that these restrictions are unnecessary. It is enough to note that every morphism from `A` to a group
scheme `E` of finite type over `k` that sends the identity to the identity is a group homomorphism, and to apply this to
sections over `A` of an extension `E` of `A` by `G`.

We shall apply this result when `G` is a finite separable group over `k`, that is, an ordinary finite group, assumed
commutative. Using `π₁(A × A) ≃ π₁(A) × π₁(A)` (X.1.7), and interpreting `H¹(X,G)` as `Hom(π₁(X),G)` for every algebraic
scheme `X`, in particular for `X = A` or `X = A × A`, one sees that every class in `H¹(A,G)` is primitive. Thus one has
an isomorphism

```text
Ext(A,G) ≃ H¹(A,G).
```

In other words, **every principal covering of `A` with commutative structural group `G`, pointed above the origin of
`A`, is endowed in a unique way with a structure of algebraic group having the marked point as origin, and such that
`A′ → A` is a homomorphism of algebraic groups.** In particular, if `A′` is connected, it is also an abelian variety,
isogenous to `A`.

On the other hand, since the functor `X ↦ π₁(X)` from pointed algebraic schemes `X` to groups commutes with products
(IX.1.7), it sends a group in the first category to a group in the category of groups, that is, to a **commutative**
group. Hence **if `A` is an abelian variety, `π₁(A)`**

<!-- original page 288 -->

**is a commutative group.** Thus, to know `π₁(A)`, it is enough to know the functor

```text
G ↦ H¹(A,G) = Hom(π₁(A),G)
```

as `G` varies through finite **commutative** groups. Finally, recall that for every integer `n > 0`, the
multiplication-by-`n` homomorphism in `A`,

```text
A --n→ A,
```

is surjective, hence has finite kernel, that is, it is an isogeny; it follows that every isogeny `A′ → A` is a quotient
of an isogeny of the preceding type. From this, and from standard arguments (cf. for example [XI.6]), one obtains:

**Theorem (Serre-Lang).**

<!-- label: XI.2.1 -->

Let `A` be an abelian variety over an algebraically closed field `k`. For every integer `n > 0`, let `K_n` be the
ordinary finite group underlying the kernel `_nA` of multiplication by `n` in `A`, and put, for every prime number `ℓ`,

```text
T_ℓ(A) = lim_r K_ℓʳ
```

and

```text
T_·(A) = ∏_ℓ T_ℓ(A) = lim_n K_n,
```

where, for `m` a multiple of `n`, `m = ns`, one sends `K_m` to `K_n` by multiplication by `s`. Then `π₁(A)` is
canonically isomorphic to `T_·(A)`. Hence for every prime number `ℓ`, the `ℓ`-primary component of `π₁(A)` is
canonically isomorphic to `T_ℓ(A)`.

Notice that these isomorphisms are functorial in `A`. The module `T_ℓ(A)` is called the **`ℓ`-adic Tate module** of the
abelian variety `A`. It is an additive functor in `A`; in particular it gives rise to a representation of the ring
`Hom(A,A)` of endomorphisms of `A` in `T_ℓ(A)`, called the **`ℓ`-adic Weil representation**, which plays an important
role in the theory of abelian varieties (cf. for example [XI.4, Chapter VII]). Theorem XI.2.1 gives an interpretation of
it in terms of the natural representation in the **`ℓ`-adic homology group** of `A`,

```text
H₁(A,ℤ_ℓ) = π₁(A)_ℓ,
```

<!-- original page 289 -->

which is plainly more satisfactory a priori, especially from the point of view of the Lefschetz formula \[XI.4, Chapter
V\]. Recall Weil’s results on the structure of `T_ℓ(A)`:

a) If `n` is prime to `char(k)`, then `K_n` is a free module of rank `2 dim A` over `ℤ/nℤ`. Hence if `ℓ` is a prime
number different from `char(k)`, `T_ℓ(A)` is a free module of rank `2 dim A` over the ring `ℤ_ℓ` of `ℓ`-adic integers.

b) If `n` is a power of `char(k) = p`, then `K_n` is a free module of rank `ν ≤ dim A` over `ℤ/nℤ`, with `ν` independent
of `n`. Hence `T_p(A)` is a free module of rank `ν ≤ dim A` over the ring `ℤ_p` of `p`-adic integers.

This shows that in the theory of the fundamental group developed here, the fundamental group of a variable abelian
variety does not vary regularly with the parameter: its `p`-primary component may suddenly drop for values of the
parameter `t` corresponding to residual characteristic `p`. The best-known case of this phenomenon is that of elliptic
curves.

Notice, however, that for every `n`, whether or not `n` is prime to the characteristic, the true kernel `_nA` in `A` of
multiplication by `n` is a finite group scheme over `k` of degree `n²ᵍ`, where `g = dim A`; it is nonseparable over `k`
if `n` is a multiple of `p = char(k)`. Moreover, when `A` varies in a family of abelian varieties, that is, when one has
an abelian scheme `A` over a base scheme `S`, one shows more generally that `_nA` is a finite flat group scheme over
`S`, of degree `n²ᵍ` over `S`. In other words, provided that the infinitesimal parts of the kernels `_nA` are taken into
account, they behave regularly for every `n`.

This suggests that the “true” fundamental group of an abelian variety `A` is the pro-algebraic group (formal inverse
limit of finite groups over `k`)

```text
lim_n _nA,
```

where by the “true fundamental group” of an algebraic scheme `X` one should mean the pro-group that classifies principal
coverings of `X` with structural group an arbitrary finite group scheme `G` over `k`, not necessarily separable over
`k`. In this way, for example, from the representations of `Hom(A,A)` in the `p`-primary component of the true
fundamental group of `A`, one recovers the Weil characteristic polynomial defined by the latter using the `ℓ ≠ p`, in a
more natural way than Serre’s construction [XI.8].

## 3. Projective Cones, Zariski’s Example

<!-- label: XI.3 -->

<!-- original page 290 -->

For simplicity, keep `k` algebraically closed, and let `V` be a connected projective `k`-scheme, a closed subscheme of
`ℙ^r_k`, which one may assume nonsingular if desired. Let `Y = Ĉ` be the projective cone over `V`, let `y₀` be its
vertex, let `X = Ĉ_V` be the usual projective closure of the vector bundle `C_V = V(𝒪_V(1))` associated with `𝒪_V(1)`,
and finally let

```text
f: X → Y
```

be the canonical morphism contracting the zero section `X₀` of `C_V` on `X` to a point (EGA II 8.6.4). Since `X` is a
locally trivial bundle over `V` with fibers `ℙ¹`, hence with simply connected fibers, the morphism `p: X → V` induces,
by X.1.4, an isomorphism

```text
π₁(X) ≃ π₁(V).
```

Since `p` induces an isomorphism `X₀ → V`, it follows that **an étale covering of `X` is completely decomposed if and
only if its restriction to `X₀` is so**. But for every étale covering `Y′` of `Y`, the inverse image `X′ = X ×_Y Y′` is
an étale covering of `X` completely decomposed over the fiber `X₀`, hence trivial. Since the homomorphism
`π₁(X) → π₁(Y)` is surjective (IX.3.4), it follows that

```text
π₁(Y) = (e).
```

In other words, **every projective cone is simply connected.** In characteristic 0, the same result remains true with
`Y` taken to be the affine cone.

Now suppose `V` regular, that is, smooth over `k`. Then `X` is regular, and for a suitable projective embedding of `V`
one obtains a **normal** projective cone `Y`. If `V` is not simply connected, hence `X` is not simply connected, let
`X′` be a nontrivial connected étale covering of `X`. Since the fibers of `X` over the points `y ∈ Y` distinct from `y₀`
are reduced to a point, the restriction of `X′` to its fibers, in particular to the

<!-- original page 291 -->

generic fiber, is trivial. Nevertheless `X′` does not come by inverse image from an étale covering of `Y`, since `Y` is
simply connected and `X′` would then be completely decomposed. This shows that X.1.3 and X.1.4 become false if the
hypothesis that `f` is separable is replaced by the weaker hypothesis that its fibers are separable algebraic schemes,
or even smooth schemes, over the `κ(s)`. Similarly, the fundamental groups of the geometric fibers `X̄_y` for `y ≠ y₀`
are plainly reduced to `(e)`, since these fibers are reduced to a point, while `π₁(X₀) ≠ e`; hence the semicontinuity
theorem X.2.4 also fails for `f`.

Finally let us indicate the example, pointed out by Zariski, that makes the same theorems fail when the hypothesis that
`f` is separable is replaced by the hypothesis that `f` is flat. Let `f: X → Y` be a morphism from a nonsingular
projective surface to the rational line `Y = ℙ¹`, such that `K = k(X)` is a “regular” extension, that is, primary and
separable, of `k(f)` (equivalently, the geometric generic fiber is connected and separable), and such that the divisor
`(f) = X₀ − X_∞` is an `n`-th multiple of a divisor, where `n` is an integer prime to the characteristic. Such examples
can be constructed in every characteristic.

Let `X′` be the normalization of `X` in `K(f^(1/n))`, where `K = k(X)` is the function field of `X`. The hypothesis on
`(f)` implies that `X′` is étale over `X`. Let `Y′` be the normalization of `Y` in `k(t)(t^(1/n))`; it is ramified over
`Y` exactly at `t = 0` and `t = ∞`, and the restriction `X′|f⁻¹(U)` is isomorphic to the inverse image of `Y′|U`. In
particular, the restriction of `X′` to the **geometric** generic fiber of `X` over `Y` decomposes completely.
Nevertheless `X′` is not isomorphic to the inverse image of an étale covering of `Y`, since one sees immediately that
the latter would necessarily be `Y′`, which is absurd because `Y′` is ramified over `Y`. \[Translator note: the source
footnote observes that, from the viewpoint of the étale topology (SGA 4 VII), in this example `R¹(f_et)_*(ℤ/nℤ)` is
“non-separated” over `S`.\]

Here is a simple way, due to Serre, to realize the conditions of this example, inspired by [XI.5, no. 20]. Take `n` to
be a prime number `≥ 5`, distinct from the characteristic, and let `G = ℤ/nℤ` act on affine 4-space `k⁴` by multiplying
the coordinates by four distinct characters of `G`, which is possible since `n ≥ 5`. \[M. Raynaud, added in 2003: `k⁴`
denotes affine 4-space over `k`.\] Then `G` acts on projective space `ℙ³_k`, and the only fixed points under `G` are the
four points corresponding to the coordinate axes. The surface `X′` with equation

```text
xⁿ + yⁿ + zⁿ + tⁿ = 0
```

is smooth over

<!-- original page 292 -->

`k` by the Jacobian criterion, and contains none of the fixed points. Since `G` has prime order, it acts on `X′`
“without fixed points,” that is, `X′` is a principal covering of `X = X′/G` with group `G`.

Let `g = x/y` in `k(X′) = K′`. This is a Kummer generator of `K′` over `K = k(X)` if the chosen characters were `χ^i`,
`i = 0,1,2,3`, with `χ` a primitive character. Let `f` be its `n`-th power, which is an element of `K`. One sees at once
that `K′` is a regular extension of `k(g)`. This follows from the fact that the plane curve with homogeneous equation in
`U,T,Z`

```text
Tⁿ + Zⁿ + (1 + gⁿ)Uⁿ = 0
```

is smooth over `k(g)`, by the Jacobian criterion, and from the fact that every plane curve is connected. On the other
hand, `k(f) = K ∩ k(g)`, since the right-hand side is an extension of `k(f)` contained in the prime-degree extension
`k(g)`, and distinct from `k(g)` because `g ∉ K`. This implies that `K` is a regular extension of `k(f)`.

Finally, the divisor of `f` on `X` is an `n`-th multiple of a divisor, since its inverse image on `X′` is the divisor of
`gⁿ`, hence an `n`-th multiple, and one can descend because `X′` is étale over `X`. We would be done if the rational map
`f: X → ℙ¹` were a morphism, that is, if the divisors of zeros and poles of `f` did not meet. In fact, one verifies
easily, again by looking on `X′`, that the two divisors in question are the products by `n` of two smooth curves over
`k` meeting transversely at one point `a`. Replacing `X` by the scheme obtained by blowing up `a`, the preceding
conditions (`div(f)` divisible by `n`, and `k(X₁) = k(X)` a regular extension of `k(f)`) remain satisfied, but moreover
`f` is a **morphism** `X₁ → ℙ¹`. Thus we are in the desired situation.

## 4. The Cohomology Exact Sequence

<!-- label: XI.4 -->

Let `S` be a prescheme, so that the category `Sch_/S` of preschemes over `S` is determined, and hence also the notion of
a group in it; such a group will also be called a **group prescheme over `S`**, or simply an **`S`-group**. To simplify
the exposition and fix ideas, in what follows we shall most often restrict to groups that are **affine** and **flat**
over `S`. \[Translator note: the source footnote says that quasi-affineness instead of affineness would suffice for what
follows; cf. the footnote referred to as note 296 in the source.\] This will be enough for the applications we have in
view. Of course, there are many cases where neither hypothesis is satisfied.

<!-- original page 293 -->

Let `G` be such an `S`-group, and let `P` be a prescheme over `S` on which `G` acts on the right; in particular this
gives a morphism

```text
π: P ×_S G → P
```

in the category `Sch_/S`, satisfying the familiar axioms. We say that `P` is **formally principal homogeneous under**
`G` if the morphism

```text
P ×_S G → P ×_S P
```

with components `pr₁` and `π` is an isomorphism. Equivalently, for every object `S′` of `Sch_/S`, the set
`P(S′) = Hom_S(S′,P)`, regarded as a set with operator group `G(S′) = Hom_S(S′,G)`, is either empty or principal
homogeneous, that is, empty or isomorphic to `G(S′)` with `G(S′)` acting by right translations.

We say that `P` is **trivial** if `P` is isomorphic to `G`, with `G` acting on itself by right translations, or
equivalently if each of the operator sets `P(S′)` under `G(S′)` is trivial. One verifies, for example by the patented
procedure of passing to the set-theoretic case, that `P` **is trivial if and only if it is formally principal
homogeneous and admits a section over `S`**. This last fact can be phrased categorically by saying that `P` has a
section over the final object `e = S` of `Sch_/S`, that is, that there exists a morphism from `e` to `P`.

To define the notion of a principal homogeneous bundle `P` under `G`, stronger than that of a formally principal
homogeneous bundle, one must first specify in `Sch_/S` a class of morphisms to be used for “descent,” and which will
play the role of “localization morphisms” for “trivializing” bundles. The most suitable choice varies with context; no
one choice contains all the others. [Translator note: the source refers here to SGA 3 IV, especially §4.] Here it is
convenient to adopt the following definition:

**Definition.**

<!-- label: XI.4.1 -->

Let `G` be an `S`-group. A **principal homogeneous bundle** (on the right) under `G` is an `S`-prescheme `P` with a
right action of the `S`-group `G`, such that there exists a covering of `S` by open subsets `U_i`, and for each `i` a
faithfully flat and quasi-compact base-change morphism `S′_i → U_i`, such that `P′ = P ×_S S′` is a trivial operator
prescheme under `G′ = G ×_S S′`, where `S′` is the `S`-prescheme that is the disjoint sum of the `S′_i`.

<!-- original page 294 -->

The base-change functor `X ↦ X′ = X ×_S S′`, being left exact, sends groups to groups and objects with operator group to
objects with operator group. Notice that XI.4.1 is **stable under base change**. Also:

**Proposition.**

<!-- label: XI.4.2 -->

Let `G` be an `S`-group, flat and quasi-compact over `S`, and let `P` be an `S`-prescheme on which `G` acts on the
right. The following conditions are equivalent:

1. `P` is a principal homogeneous bundle under `G`.
1. `P` is formally principal homogeneous under `G`, and the structural morphism `P → S` is faithfully flat and
    quasi-compact.

If `P` is principal homogeneous under `G`, then with the notation of XI.4.1, `P′` is faithfully flat and quasi-compact
over `S′`, since `G′` is so and `P′` is `S′`-isomorphic to it. Hence `P` has the same properties over `S` (for
“surjective” and “quasi-compact,” cf. VIII.3.1; for “flat,” this is an omission in the sorites of Exposé VIII).
Conversely, if 2 holds, take the base change `S′ = P`, which is indeed faithfully flat and quasi-compact over `S`. Then
`P′` is formally principal homogeneous over `S′` because `P` is so over `S` and base change is left exact. Moreover `P′`
has a section over `S′`, namely the diagonal section, hence it is a trivial principal bundle. This proves the assertion.

**Corollary.**

<!-- label: XI.4.3 -->

If `G` is affine and flat over `S`, every principal homogeneous bundle `P` under `G` is affine and flat over `S`.

Indeed, it becomes so after a faithfully flat and quasi-compact base extension, and one applies VIII.5.6.

The usefulness of Definition XI.4.1 for `S`-groups **flat** and **affine** over `S` rests on VIII.2.1, that is, on the
fact that the morphisms `S′ → S` considered in XI.4.1 are morphisms of effective descent for the category of preschemes
affine over other preschemes. Thanks to this fact, the verification of the facts sketched below is essentially
“categorical.” [Translator note: the source refers again to the footnote cited above.]

Let `E` be an `S`-prescheme on which the `S`-group `G` acts on the left, and let `P` be a principal homogeneous bundle
on the right under `G`. We want to define an associated bundle `E^(P)`, “locally” isomorphic to `E`. To do this, make
`G` act on the right on `P ×_S E` by the law

```text
(x,y) ↦ (xg,g⁻¹y),
```

<!-- original page 295 -->

which describes such actions in the set-theoretic context and extends to categories by the patented procedure. We put,
subject to existence,

```text
E^(P) = (P ×_S E)/G.
```

With this convention, `P ×_S E` will be a prescheme over `T = E^(P)`, with right operator group `G_T = G ×_S T`; one
would like, for comfort, `P ×_S E` to be a principal homogeneous bundle over `T` with group `G_T`.

To verify the existence of `E^(P)` and the preceding property, take the `S′` from Definition XI.4.1 and look at the
inverse-image situation over `S′`. Since `P′` is trivial, that is, isomorphic to `G′_d`, one sees at once that `E′^(P′)`
exists and has the desired exactness property. In fact, `E′ ×_S′ P′` is `G′`-isomorphic to the product `E′ ×_S′ G′`, and
therefore `E′^(P′)` is isomorphic to `E′`. Moreover, the formation of the “associated bundle” in the case of a trivial
operator space commutes with every base extension. Taking here the various base extensions `S″ ⇉ S′` and `S‴ ⇉⇉ S′`,
where `S″` and `S‴` are the double and triple fiber products of `S′` over `S`, one sees that `E′^(P′)` **is endowed with
a descent datum relative to `S′ → S`, and `E^(P)` exists with the required properties if and only if this descent datum
is effective**. Of course `E^(P)` is then precisely the descended object. Use here the fact that `S′ → S` is a descent
morphism in the category of `S`-preschemes; cf. VIII.5.2. It follows that **the associated bundle exists if `E` is
affine over `S`**.

We shall apply this construction in the case where one has a homomorphism of `S`-groups `G → H`, and where `E` is the
`S`-prescheme `H` endowed with the left actions of `G` on `H` arising from the given morphism. Since `H` acts on itself
on the right in a way that commutes with the actions of `G` on `H`, and since (subject to existence over `S`) the
formation of the associated bundle commutes with base extension, one easily sees that `H` acts on the right on `P^(H)`.
Thus `P^(H)` is a principal homogeneous bundle under `H` in the sense of XI.4.1, and

<!-- original page 296 -->

more precisely it is trivialized by the same morphism `S′ → S` as `P`. In particular, **to every principal homogeneous
bundle `P` under `G` and every homomorphism of `S`-groups `G → H`, with `H` affine over `S`, there is associated a
principal homogeneous bundle with group `H`**, functorially in `(G → H)`, and compatibly with arbitrary base changes
`T → S`.

**Definition.**

<!-- label: XI.4.4 -->

Let `G` be an `S`-prescheme. We write `H⁰(S,G)` for the set of sections of `G` over `S`, considered as a group when `G`
is an `S`-group. In that case, we write `H¹(S,G)` for the set of isomorphism classes of principal homogeneous bundles
over `S` with group `G`, regarding `H¹(S,G)` as endowed with the “marked point” corresponding to the trivial bundles.
\[Translator note: the source footnote says this notation is consistent with the general cohomological notation (SGA 4
V) only when one has effectivity criteria for descent, which are scarcely ensured except when `G` is affine, or merely
quasi-affine; cf. VIII.7.9.\]

Thus `H⁰(S,G)` is a functor in the `S`-prescheme `G`, with values in sets. This functor is left exact, and a fortiori
commutes with finite products; indeed this implies that it sends groups to groups and commutative groups to commutative
groups. Similarly, `H¹(S,G)` is a functor in the **affine** `S`-group `G`, with values in sets, by formation of
associated bundles; one checks easily that this functor commutes with finite products. In particular it sends groups in
the category of affine `S`-groups, that is, **commutative affine** `S`-groups, to groups, and indeed to commutative
groups. Thus, **if `G` is a commutative affine `S`-group, `H¹(S,G)` is a commutative group**, and a homomorphism `G → H`
of commutative affine `S`-groups gives rise to a group homomorphism `H¹(S,G) → H¹(S,H)`.

For simplicity, from now on we restrict to **affine and commutative** `S`-groups. Let

```text
0 → G′ → G → G″ → 0
```

be a sequence of morphisms of such groups. **We say that this sequence is exact if the composite `G′ → G → G″` is zero**
(which allows `G` to be regarded as a prescheme over `G″` with right operator group `G′_G″`)

<!-- original page 297 -->

**and if `G` is a principal homogeneous bundle over `G″` with group `G′_G″ = G′ ×_S G″`**. This implies in particular
that `u: G′ → G` is a kernel of `v: G → G″`, and a fortiori it implies exactness of

```text
0 → H⁰(S,G′) → H⁰(S,G) → H⁰(S,G″).
```

It also makes it possible to define a map

```text
∂: H⁰(S,G″) → H¹(S,G′),
```

by associating to every section of `G″` over `S`, that is, to every `S`-morphism `f: S → G″`, the principal homogeneous
bundle `P_f` with group `G′ ≃ f*(G′_G″)` over `S`, inverse image of the principal homogeneous bundle `G` over `G″`. From
the viewpoint of `S`-preschemes, this is simply the inverse image by `v: G → G″` of the subprescheme image of `S` by the
immersion `f`; the operations of `G′` on `P_f` are induced by the right operations of `G′` on `G`.

We also leave to the reader the verification of the following proposition, which presents no difficulties other than
those of writing it out:

**Proposition.**

<!-- label: XI.4.5 -->

The map `∂: H⁰(S,G″) → H¹(S,G′)` is a group homomorphism. The following sequence of homomorphisms is exact:

```text
0 → H⁰(S,G′) → H⁰(S,G) → H⁰(S,G″) → H¹(S,G′) → H¹(S,G) → H¹(S,G″),
```

where all homomorphisms other than `∂` come from the functoriality of `H⁰`, respectively `H¹`.

**Remarks.**

<!-- label: XI.4.6 -->

The point of view set out here for the study of principal homogeneous bundles is visibly inspired by Serre [XI.7], which
the reader would do well to consult. When one wants a formalism that also applies to structural `S`-groups
quasi-projective over `S`, in order to include projective abelian schemes in particular, it is useful to modify XI.4.1
by requiring `S′` to be a sum of preschemes `S′_i` finite and locally free over open subsets `S_i` covering `S`. The
preceding developments are then valid, including in particular XI.4.5, after replacing the affine hypothesis everywhere
by the quasi-projective hypothesis, and interpreting accordingly the definition given above of an exact sequence of
`S`-groups. It is enough to replace the reference to VIII.2.1

<!-- original page 298 -->

by VIII.7.7: the morphisms `S′ → S` used are morphisms of effective descent for the fibered category of preschemes
quasi-projective over other preschemes. Be careful, however, that this second notion of principal homogeneous bundle is
more restrictive than the first, XI.4.1.

### 4.7.

<!-- label: XI.4.7 -->

One obtains an even more restrictive notion of principal homogeneous bundle by requiring `S` to be covered by open
subsets `S_i` such that for every `i`, `P|S_i` is a trivial operator bundle under `G|S_i`; in this case one says that
`P` is a **locally trivial** principal homogeneous bundle. The classes of these bundles, for fixed `G`, form a subset of
`H¹(X,G)`, in one-to-one correspondence with `H¹(X,𝒪_X(G))`, where `𝒪_X(G)` is the ordinary sheaf of sections of `G`
over `S`; cf. [XI.2]. For these `H¹` to again give rise to a cohomology exact sequence XI.4.5, one must plainly assume
that the sequence `0 → G′ → G → G″ → 0` is exact in the reasonable sense for this new context, that is, that `G` is a
locally trivial bundle over `G″` with group `G′_G″`. This also means that `u: G′ → G` is a kernel of `v: G → G″`, and
that `G` admits local sections over `G″`.

### 4.8.

<!-- label: XI.4.8 -->

It is plainly very desirable to continue the exact sequence XI.4.5 by introducing the higher cohomology groups
`H^i(X,G)`. This is possible in the framework of “Weil cohomology”: one considers the category `𝓑` of quasi-compact
preschemes over `S`, endowed with the class `𝓜` of faithfully flat and quasi-compact morphisms, called localizing
morphisms. An abelian “Weil sheaf” on `S`, or better, on `(𝓑,𝓜)`, is a contravariant functor `𝓕` from `𝓑` to abelian
groups, sending sums to products and every sequence `T″ = T′ ×_T T′ ⇉ T′ → T`, with `T′ → T` in `𝓜`, to an **exact**
diagram of sets

```text
𝓕(T) → 𝓕(T′) ⇉ 𝓕(T″).
```

The Weil sheaves form an abelian category with exact filtered colimits and a generator, hence with enough injective
objects [XI.1]. The right derived functors of `Γ(𝓕) = 𝓕(S)` are denoted `H^i(S,𝓕)`. On the other hand, every commutative
`S`-group plainly defines a Weil sheaf (VIII.5.2), whose `H⁰` and `H¹` are just `H⁰(S,G)` and `H¹(S,G)`. This gives a
reasonable definition of the other `H^i(S,G)`.

<!-- original page 299 -->

Moreover, one shows that an exact sequence of `S`-groups defines an exact sequence of Weil sheaves, allowing one to
recover and extend the exact sequence XI.4.5. \[Translator note: the source footnote refers, for a systematic study of
this point of view, to SGA 4 I-IX.\]

### 4.9.

<!-- label: XI.4.9 -->

It would be appropriate to develop the noncommutative variants of XI.4.5 as in [XI.2]. For a systematic development, in
the proper framework, of the various cohomological notions sketched in the present number, we refer to work in
preparation by J. Giraud. \[Translator note: the corrected source identifies this as J. Giraud, *Cohomologie non
abélienne*, Springer-Verlag, 1971.\]

## 5. Special Cases of Principal Bundles

<!-- label: XI.5 -->

Suppose now that `S` is connected and endowed with a geometric point `a`, hence with a fundamental group `π₁(S,a)`
classifying the étale coverings of `S`: the category of étale coverings of `S` is equivalent to the category of finite
sets on which `π₁` acts continuously. It follows that a finite étale group scheme `G` over `S` is determined,
essentially, by an ordinary finite group `𝒢` on which `π₁` acts continuously by group automorphisms. An étale covering
`P` of `S` on which `G` acts on the right is determined, essentially, by a finite set `𝒫` on which `π₁` acts
continuously on the left, and on which `𝒢` acts on the right in a way compatible with the operations of `π₁`:

```text
s(p · g) = (sp) · (sg),     for s ∈ π₁, p ∈ 𝒫, g ∈ 𝒢.
```

One verifies that `P` is a principal homogeneous bundle in the sense of XI.4.1 if and only if `𝒫` is a principal
homogeneous set under `𝒢`; for example, use the criterion XI.4.2. In other words, **the category of principal
homogeneous bundles over `S` with group `G` is equivalent to the category of principal homogeneous bundles with group
`G` in the category of finite sets on which `π₁` acts continuously**. In particular one deduces a canonical bijection,
functorial in `G`:

<!-- label: eq:XI.5.etoile -->

```text
(*)   H¹(S,G) ≃ H¹(π₁,𝒢),
```

where

<!-- original page 300 -->

the second member denotes the set of classes, up to isomorphism, of principal homogeneous bundles under `𝒢` in the
category of finite sets on which `π₁` acts; it is in fact needless to specify “continuously.” This set is made explicit
in the familiar way as the quotient of the set `Z¹(π₁,G)` of 1-cocycles `φ: π₁ → 𝒢`, satisfying

```text
φ(1) = 1,     φ(st) = φ(s)(s · φ(t)),
```

by the natural action of the group `𝒢`.

<!-- label: page-300 -->

An important case is the one where `π₁` acts trivially on `𝒢`, that is, where `G` is a completely decomposed covering of
`S`, isomorphic to the sum of `𝒢` copies of `S`. One then also writes `H¹(S,𝒢)` instead of `H¹(S,G)`, and this set is in
one-to-one correspondence, by (\*), with `H¹(π₁,𝒢) = Hom(π₁,𝒢)` modulo inner automorphisms of `𝒢`. Notice, moreover,
that in this case a principal homogeneous bundle over `S` with group `G` is nothing other than a **principal covering**
of `S` with group `𝒢` (V.2.7), and the preceding one-to-one correspondence is the one deduced from the correspondence
between principal coverings of `S` with group `𝒢`, **pointed** above `a`, and continuous homomorphisms from `π₁(S,a)` to
`𝒢` (V, end of no. V.5).

The interest of relating the theory of étale coverings with that of principal bundles, already implicit in A. Weil,
_Généralisation des Fonctions Abéliennes_, and made explicit by S. Lang in his geometric theory of class fields, cf.
Serre [XI.5], comes from the following fact. Every `S`-group that is finite and étale over `S` can be embedded in an
`S`-group `H`, affine and smooth over `S`, with connected fibers, and commutative when `G` is. Therefore, by the exact
sequence XI.4.5, and possibly its noncommutative variants, the “discrete” classification of principal coverings with
group `G` can be studied by means of the “continuous” classification of principal bundles with group `H`, and conversely
as well. For the idea of the general construction of the immersion of `G` into `H`, apparently rather little used in
practice, see [XI.5, VI 2.8]. We shall content ourselves in the following number with developing two important special
cases, classical ones at that. We shall need the following auxiliary result.

**Proposition.**

<!-- label: XI.5.1 -->

Let

<!-- original page 301 -->

`S` be a prescheme, and let `G` be an `S`-group isomorphic to `GL(n)_S`, for example `𝔾_m,S`, or to `𝔾_a,S`. Then every
principal homogeneous bundle under `G` is locally trivial.

Here `GL(n)_S`, for an integer `n ≥ 0`, denotes the `S`-group representing the contravariant functor

```text
T ↦ GL(n, Γ(T,𝒪_T))
```

on the `S`-prescheme `T`. In particular `𝔾_m,S`, the “multiplicative group over `S`,” represents the contravariant
functor

```text
T ↦ Γ(T,𝒪_T^*),
```

and therefore, as a prescheme over `S`, is isomorphic to `Spec 𝒪_S[t,t⁻¹]`, where `t` is an indeterminate. Similarly
`𝔾_a,S` represents the contravariant functor

```text
T ↦ Γ(T,𝒪_T),
```

and hence is isomorphic as an `S`-prescheme to `Spec(𝒪_S[t])`, where `t` is an indeterminate. Notice that, by dévissage,
XI.5.1 recovers Rosenlicht’s local-triviality result for the case where `G` admits a “composition series” whose
successive factors are groups of the type considered here. For a finer study of questions of local triviality of
principal homogeneous bundles, cf. [XI.7] and [XI.3].

The first assertion is proved by observing that `G(T) = Aut(𝒪_T^n)`, and that the morphisms `S′ → S` occurring in
XI.4.1, that is, those which are faithfully flat and quasi-compact, are morphisms of effective descent for the fibered
category of modules locally isomorphic to `𝒪_T^n`, that is, locally free of rank `n` (VIII.1.12). The second is proved
in an analogous way, noting that in this case `G(T) = Aut(𝓔_T)`, where `𝓔_T` is the trivial **extension** of `𝒪_T` by
`𝒪_T`, and where the automorphisms must of course respect the extension structure. The morphisms `S′ → S` occurring in
XI.4.1 are morphisms of effective descent for the fibered category of extensions of `𝒪_T` by `𝒪_T`, as follows easily
from VIII.1.1, and such extensions are automatically locally trivial.

**Remark.**

<!-- label: XI.5.2 -->

Notice that the same type of proof applies to the symplectic group `Symp(2n)_S`, since an alternating form on a module
locally isomorphic to `𝒪_S^(2n)`, which is “nondegenerate,” that is, defines an isomorphism from this module to its
dual, is locally isomorphic to the standard form. The corresponding result for the orthogonal group is false, however,
already when `S` is the spectrum of a field, since there may be quadratic forms over a field that are not isomorphic to
the standard form.

<!-- original page 302 -->

Moreover, it is shown essentially in [XI.3] that the groups `GL`, `Symp`, `𝔾_a`, and those which can be dévissés into
such groups, are, up to small qualifications, the only ones for which one has a local-triviality result of the type
considered here.

**Corollary.**

<!-- label: XI.5.3 -->

There are canonical bijections

```text
H¹(S,GL(n)_S) ≃ H¹(S,GL(n,𝒪_S)),
```

in particular

```text
H¹(S,𝔾_m,S) ≃ H¹(S,𝒪_S^*),
```

and

```text
H¹(S,𝔾_a,S) ≃ H¹(S,𝒪_S),
```

where the second members denote cohomology groups of the topological space `S` with coefficients in ordinary sheaves.

In particular, `H¹(S,GL(n)_S)` identifies with the set of isomorphism classes of modules locally free of rank `n` on
`S`, and `H¹(S,𝔾_a,S)` identifies with the set of classes of extensions of the module `𝒪_S` by itself.

## 6. Application to Principal Coverings: Kummer and Artin-Schreier Theories

<!-- label: XI.6 -->

**Proposition.**

<!-- label: XI.6.1 -->

Let `S` be a prescheme, let `n` be an integer `> 0`, let

```text
u_n: 𝔾_m,S → 𝔾_m,S
```

be the `n`-th power homomorphism, and let `μ_n,S` be its kernel. Then `μ_n,S` is finite and locally free of rank `n`
over `S`, and it is étale over `S` if and only if for every `s ∈ S`, the characteristic of `s` is prime to `n`. The
sequence of homomorphisms

```text
0 → μ_n,S → 𝔾_m,S --u_n→ 𝔾_m,S → 0
```

is exact in the sense of no. XI.4. It will be called the **Kummer exact sequence** over `S`, relative to the integer
`n`.

One has

<!-- original page 303 -->

```text
𝔾_m = Spec 𝒪_S[t,t⁻¹],
```

and `u_n` corresponds to the homomorphism `u_n` on affine `𝒪_S`-algebras given by

```text
u_n(t) = tⁿ.
```

On the other hand, the unit section of `𝔾_m,S` corresponds to the augmentation homomorphism of `𝒪_S`-algebras given by

```text
ε(t) = 1,
```

whose kernel is therefore the principal ideal `(t − 1)`. The image of this ideal by `u_n` is thus the principal ideal
`(1 − tⁿ)`, and one finds

```text
μ_n,S = Spec 𝒪_S[t]/(1 − tⁿ).
```

This shows in particular that `μ_n,S` is finite over `S`, and is defined by an algebra over `S` that is free of rank
`n`, with basis formed by the `tⁱ` for `0 ≤ i ≤ n − 1`. For it to be étale at `s ∈ S`, it is necessary and sufficient
that the reduced algebra `k[t]/(1 − tⁿ)`, where `k = κ(s)`, obtained by formally adjoining the `n`-th roots of unity to
`k`, be separable over `k`; that is, that the roots of `1 − tⁿ` in an algebraic closure of `k` all be distinct. This is
equivalent to `n` being prime to the characteristic. Finally, to show that the sequence of homomorphisms in XI.6.1 is
exact, the criterion XI.4.2 reduces us to proving that `u_n` is faithfully flat. \[Translator note: the corrected source
replaces an erroneous “v” here by `u_n`.\] We may plainly suppose that `S` is affine with ring `A`, hence that `𝔾_m,S`
is affine with ring `B = A[t,t⁻¹]`. It is enough to verify that `u_n` makes `B` a free module of rank `n` over `B`;
equivalently, that `u_n` is injective and that `A[t,t⁻¹]` is a free module of rank `n` over `A[tⁿ,t⁻ⁿ]`. Indeed, one
checks easily that the `tⁱ` for `0 ≤ i ≤ n − 1` form a basis of the former over the latter, which completes the proof.

**Definition.**

<!-- label: XI.6.2 -->

<!-- original page 304 -->

The group `μ_n,S` is called the **Kummer group of rank `n` over `S`**, and a **Kummer principal covering of rank `n`
over `S`** is a principal homogeneous bundle over `S` whose group is the Kummer group of rank `n`. \[Translator note:
the corrected source reads “rank `n` over `S`,” correcting the old text’s malformed “n S.”\]

The set of these coverings is a group, denoted `H¹(S,μ_n,S)`, or simply `H¹(S,μ_n)`. Notice that the formation of the
Kummer group of rank `n` over `S` is compatible with extension of the base, so that `μ_n,S` comes by base extension from
the **absolute Kummer group `μ_n`** over `Spec(ℤ)`.

Let `(ℤ/nℤ)_S` denote the `S`-group defined by the ordinary finite group `ℤ/nℤ`. If `G` is any `S`-group, the
homomorphisms of `S`-groups `u` from `(ℤ/nℤ)_S` to `G` are in one-to-one correspondence, compatibly with base change,
with the sections of `G` over `S` whose `n`-th power is the unit section: to `u` one associates the image by `u` of the
section of `(ℤ/nℤ)_S` over `S` defined by the generator `1 mod nℤ` of `ℤ/nℤ`. With this understood:

**Corollary.**

<!-- label: XI.6.3 -->

If `μ_n,S` is étale over `S`, one thereby obtains a one-to-one correspondence between isomorphisms of `S`-groups

```text
(ℤ/nℤ)_S ≃ μ_n,S
```

and sections of `𝒪_S` that are of exact order `n` on each connected component of `S`; such a section will be called a
“primitive `n`-th root of unity over `S`.” Therefore, for `μ_n,S` to be isomorphic as an `S`-group to `(ℤ/nℤ)_S`, it is
necessary and sufficient that it be étale over `S`, that is, that the residual characteristics of `S` be prime to `n`,
and that there exist a primitive `n`-th root of unity over `S`.

This explains the role played in classical Kummer theory by the hypothesis that the base field, playing the role of `S`,
have characteristic prime to `n` and contain the `n`-th roots of unity, and by the choice of a primitive `n`-th root of
unity. Once the language of schemes is available, there is no longer any reason to burden oneself with these hypotheses;
one should reason directly with `μ_n` instead of `ℤ/nℤ`. Thus the conjunction of XI.6.1, XI.4.5, and XI.5.3 gives the
following general relation between the theory of Kummer principal coverings and that of Picard groups.

**Proposition.**

<!-- label: XI.6.4 -->

Let

<!-- original page 305 -->

`S` be a prescheme. There is a canonical exact sequence

```text
0 → H⁰(S,μ_n) → H⁰(S,𝒪_S^*) → H⁰(S,𝒪_S^*) → H¹(S,μ_n)
  → H¹(S,𝒪_S^*) → H¹(S,𝒪_S^*),
```

hence, putting `H¹(S,𝒪_S^*) = Pic(S)`, and denoting for every abelian group `A` by `_nA` and `A_n` the kernel and
cokernel of multiplication by `n` in `A`, the exact sequence

```text
0 → H⁰(S,𝒪_S)^*_n → H¹(S,μ_n) → _nPic(S) → 0.
```

\[Translator note: the corrected source fixes the definition of `Pic(S)` here from `H¹(S,𝒪_S)` to `H¹(S,𝒪_S^*)`.\]

We shall spell out two important cases, where one or the other extreme term of this exact sequence is zero.

**Corollary.**

<!-- label: XI.6.5 -->

Suppose `_nPic(S) = 0`, for example that `S` is the spectrum of a local ring or of a factorial ring, and let `A` be the
ring `H⁰(S,𝒪_S)`. Then there is a canonical isomorphism

```text
H¹(S,μ_n) ≃ A^*/(A^*)ⁿ.
```

This is essentially the classical statement of Kummer theory when `S` is the spectrum of a field.

**Corollary.**

<!-- label: XI.6.6 -->

Suppose that every element of `H⁰(S,𝒪_S)` is an `n`-th power, for example that `H⁰(S,𝒪_S)` is a composite of
algebraically closed fields, or that `S` is reduced and proper over an algebraically closed field `k`. Then there is a
canonical isomorphism

```text
H¹(S,μ_n) ≃ _nPic(S).
```

In particular, when `S` is proper and connected over an algebraically closed field `k`, this relates the fundamental
group of `S` with the points of finite order of the Picard scheme `P` of `S` over `k`. Thus one has an isomorphism

```text
Hom(π₁(S),ℤ/nℤ) ≃ _nP(k)
```

for `n` prime to the characteristic, a relation often used in algebraic

<!-- original page 306 -->

geometry. As an application, when the connected component `P⁰` of `P` is a complete group scheme of dimension `g`, one
sees, using the results recalled in no. XI.2 and the finiteness of the Néron-Severi torsion group, that for every prime
number `ℓ` prime to the characteristic, the `ℓ`-primary component of the abelianized fundamental group `π₁(S)` is a
module of finite type and rank `2g` over the ring `ℤ_ℓ` of `ℓ`-adic integers; indeed it is free except for at most
finitely many values of `ℓ`. As Serre observed, this allows one to prove under certain conditions that when `X` is a
flat and projective scheme over connected `S`, the Picard schemes of the fibers of `X` all have the same dimension, by
applying the semicontinuity theorem (X.2.3). Serre’s argument applies as soon as the Picard scheme of `X` over `S`
exists and the connected Picards of the fibers of `X` over `S` are proper group schemes; for example when the geometric
fibers of `X` over `S` are normal, with `X` still flat and projective over `S`, and in particular if `X` is smooth and
projective over `S`.

Now let `p` be a prime number, and suppose that `S` is a prescheme of characteristic `p`, that is, `p · 𝒪_S = 0`. Then
the `p`-th power homomorphism in `𝒪_S` is additive, and the corresponding morphism, obtained by replacing `S` by a
variable `T` over `S`,

```text
F: 𝔾_a,S → 𝔾_a,S
```

is therefore a homomorphism of `S`-groups, called the **Frobenius homomorphism**. Note that such a morphism is defined
for every `S`-prescheme `G` which comes by base extension from a prescheme `G₀` over the prime field `ℤ/pℤ`, and that
this morphism is a group homomorphism if `G₀` is a group prescheme. We put

```text
wp = id − F: 𝔾_a,S → 𝔾_a,S.
```

On the other hand, consider the `S`-group `(ℤ/pℤ)_S` defined by the ordinary finite group `ℤ/pℤ`. We said that for every
`S`-group `G`, the homomorphisms of `S`-groups from `(ℤ/pℤ)_S` to `G` are in one-to-one correspondence with the sections
of `G` over `S` whose `p`-th power is the unit section. When `G = 𝔾_a,S`, they therefore correspond

<!-- original page 307 -->

to arbitrary sections of `G` over `S`. Taking in particular the section of `𝔾_a,S` over `S` corresponding to the unit
section of the sheaf of rings `𝒪_S`, one obtains a homomorphism of `S`-groups

```text
i: (ℤ/pℤ)_S → 𝔾_a,S.
```

**Proposition.**

<!-- label: XI.6.7 -->

The sequence of homomorphisms of `S`-groups

```text
0 → (ℤ/pℤ)_S → 𝔾_a,S → 𝔾_a,S → 0
```

is exact in the sense of no. XI.4. It is called the **Artin-Schreier exact sequence** over `S`. \[Translator note: the
corrected source fixes the last group symbol in the displayed sequence.\]

It is enough to prove this over the prime field `k = ℤ/pℤ`. It is enough to observe that the homomorphism
`wp*: k[t] → k[t]` defined by `wp*(t) = t − tᵖ` makes `k[t]` a free module of rank `p` over `k[t]`; more precisely,
`k[t]` is a free module over `k[s]`, where `s = t − tᵖ`, with basis formed by the `tⁱ` for `0 ≤ i ≤ p − 1`.

Using XI.4.5 and XI.5.3, we conclude:

**Proposition.**

<!-- label: XI.6.8 -->

There is a canonical exact sequence

```text
0 → H⁰(S,ℤ/pℤ) → H⁰(S,𝒪_S) → H⁰(S,𝒪_S) → H¹(S,ℤ/pℤ)
  → H¹(S,𝒪_S) → H¹(S,𝒪_S),
```

hence an exact sequence

```text
0 → H⁰(S,𝒪_S)/wp H⁰(S,𝒪_S) → H¹(S,ℤ/pℤ) → H¹(S,𝒪_S)^F → 0,
```

where the exponent `F` in the last term denotes the subgroup of invariants under the endomorphism `F`, equal to the
kernel of `wp = id − F`.

Let us spell out two extreme cases:

**Corollary.**

<!-- label: XI.6.9 -->

Suppose `H¹(S,𝒪_S)^F = 0`, for example that `S` is an affine scheme. Then, putting `A = H⁰(S,𝒪_S)`, there is a canonical
isomorphism

```text
H¹(S,ℤ/pℤ) ≃ A/wp A.
```

This is **Artin-Schreier theory** in its classical form, at least when `A` is the spectrum of a field. \[Translator
note: the source says “when `A` is the spectrum of a field”; mathematically one expects “when `S` is the spectrum of a
field,” or “when `A` is a field.”\]

**Corollary.**

<!-- label: XI.6.10 -->

Suppose

<!-- original page 308 -->

`wp H⁰(S,𝒪_S) = H⁰(S,𝒪_S)`, for example that `H⁰(S,𝒪_S)` is a composite of algebraically closed fields, or that `S` is
proper over an algebraically closed field. Then there is a canonical isomorphism

```text
H¹(S,ℤ/pℤ) ≃ H¹(S,𝒪_S)^F.
```

**Remarks.**

<!-- label: XI.6.11 -->

The last statement is due to J.-P. Serre [XI.9]. It is also possible to develop an analogous theory for the structural
group `ℤ/pⁿℤ` for arbitrary `n`, using in place of `𝔾_a` the Witt group scheme `W_n`; cf. loc. cit. Notice that in
characteristic `p > 0`, Kummer theory no longer gives information on principal coverings of order `p`, since `μ_p` is
then an “infinitesimal” group, that is, radicial over the base, and hence has no direct relation with `ℤ/pℤ`. Thus at
first sight, the theory of these coverings no longer falls, when `S` is a proper scheme over an algebraically closed
field for definiteness, under the theory of the Picard scheme as in XI.6.6. Nevertheless, if one recalls that the
Zariski tangent space at the origin in `Pic_S/K` \[Translator note: the source footnote refers for the definition of
`Pic_S/K` to A. Grothendieck, Séminaire Bourbaki no. 232, February 1962.\] identifies with `H¹(S,𝒪_S)`, one sees that
**knowledge of the group scheme `_pPic_S/k`, the kernel of multiplication by `p` in `Pic_S/k`, implies knowledge of
`H¹(S,ℤ/pℤ)` as well as of `H¹(S,μ_p)`; notice that it also implies knowledge of `H¹(S,α_p)`**, where `α_p` denotes the
infinitesimal group scheme over the prime field, the kernel of `F: 𝔾_a → 𝔾_a`, which can also be described as the
spectrum of the restricted enveloping algebra of the trivial one-dimensional `p`-Lie algebra. Indeed, the exact sequence
XI.4.5 gives here

```text
H¹(S,α_p) ≃ Ker(F: H¹(S,𝒪_S) → H¹(S,𝒪_S)),
```

and more generally, denoting by `α_pⁿ` the kernel in `𝔾_a` of the `n`-th iterate of `F`, one has

```text
H¹(S,α_pⁿ) ≃ Ker(Fⁿ: H¹(S,𝒪_S) → H¹(S,𝒪_S)).
```

In fact, knowledge of `_pPic_S/k` is equivalent to knowledge of `H¹(S,G)` for every finite commutative algebraic

<!-- original page 309 -->

group annihilated by `p`; more generally, knowledge of `_pⁿPic_S/k` is equivalent to knowledge of `H¹(S,G)` for every
finite commutative algebraic group `G` annihilated by `pⁿ`, by virtue of the following theorem, which in the case under
consideration includes both Kummer theory and Artin-Schreier theory:

Let `G` be a finite algebraic group over `k`, and let `D(G) = SheafHom_k-groups(G,𝔾_m)` be its **Cartier dual**; the
affine algebra of `D(G)` is carried by the vector space dual to the affine algebra of `G`, that is, by the hyperalgebra
of `G` in the sense of Dieudonné-Cartier. Then there is a canonical isomorphism:

<!-- label: eqXI.6.11 -->

```text
(*)   H¹(S,G) ≃ Hom_k-groups(D(G),Pic_S/k).
```

Here `S` is a proper scheme over algebraically closed `k` such that `H⁰(S,𝒪_S) = k`. This formula may also be expressed
by saying that the “true fundamental group” of `S` alluded to in no. XI.2, after abelianization, is isomorphic to the
projective limit of the `D(P_i)`, where `P_i` ranges over the **finite** algebraic subgroups of `Pic_S/k`; we shall
denote it by `T•(Pic_X/k)`. When `S` is an abelian variety, we saw in XI.2.1 that this group is also isomorphic to the
“true” Tate module `T_•(S) = lim _nS`, and the isomorphism (\*) is then written in the more striking form

```text
Ext¹(A,G) ≃ Hom(D(G),B),
```

where `A` is an abelian variety, `B` its dual, and `G` a finite algebraic group over `k`. The results just indicated can
moreover be generalized to the case where `k` is replaced by an arbitrary base prescheme, and to coefficient groups `G`
other than finite groups.

## Bibliography

<!-- original page 310 -->

1. A. Grothendieck, “Sur quelques points d’algèbre homologique,” Tôhoku Math. J. 9 (1957), pp. 119-221.
1. A. Grothendieck, “A general theory of fibre spaces with structure sheaf,” University of Kansas, 1955.
1. A. Grothendieck, “Torsion homologique et sections rationnelles,” Séminaire Chevalley, 16 June 1958.
1. S. Lang, _Abelian Varieties_, Interscience Tracts in Pure and Applied Mathematics, no. 7, New York.
1. J.-P. Serre, _Groupes algébriques et corps de classes_, Actualités Scientifiques et Industrielles no. 1264, Hermann,
    Paris, 1959.
1. J.-P. Serre, “Groupes proalgébriques,” Publications Mathématiques de l’IHÉS 7 (1960), pp. 1-67.
1. J.-P. Serre, “Espaces fibrés algébriques,” Séminaire Chevalley, 21 April 1958.
1. J.-P. Serre, “Quelques propriétés des variétés abéliennes en caractéristique p,” Amer. J. Math. 80 (1958), pp.
    715-739.
1. J.-P. Serre, “Sur la topologie des variétés algébriques en caractéristique p,” Symposium Internacional de Topologia
    Algebraica, 1958.
1. J.-P. Serre, “On the fundamental group of a unirational variety,” J. London Math. Soc. 34 (1959), pp. 481-484.
