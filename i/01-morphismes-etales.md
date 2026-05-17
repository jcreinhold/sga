# Exposé I. Étale Morphisms

<!-- label: I -->

<!-- original page 1 -->

To simplify the exposition, we assume that all preschemes under consideration are locally noetherian, at least after no.
I.2.

## 1. Notions of Differential Calculus

<!-- label: I.1 -->

Let `X` be a prescheme over `Y`, and let `Δ_{X/Y}`, or simply `Δ`, denote the diagonal morphism `X → X ×_Y X`. It is an
immersion, hence a closed immersion of `X` into an open subset `V` of `X ×_Y X`. Let `𝓘_X` be the ideal of the closed
subprescheme corresponding to the diagonal in `V`. Note that if one wants to do things intrinsically, without assuming
`X` separated over `Y`, a hypothesis that would be farcical here, one should consider the set-theoretic inverse image of
`𝒪_{X×X}` in `X`, and designate by `𝓘_X` the augmentation ideal in the latter.

The sheaf `𝓘_X/𝓘_X²` may be regarded as a quasi-coherent sheaf on `X`; it is denoted `Ω¹_{X/Y}`. It is of finite type if
`X → Y` is of finite type. It behaves well with respect to an extension of the base `Y′ → Y`.

One also introduces the sheaves

```text
𝒪_{X×_Y X}/𝓘_Xⁿ⁺¹ = 𝓟ⁿ_{X/Y}.
```

These are sheaves of rings on `X`, making `X` into a prescheme that may be denoted `Δⁿ_{X/Y}` and called the n-th
infinitesimal neighborhood of `X/Y`. The sorites for this are of total triviality, although rather long;[^I-1-1] it
would be prudent to speak of them only when one has something useful to say about them, namely with smooth morphisms.

## 2. Quasi-Finite Morphisms

<!-- label: I.2 -->

**Proposition.**

<!-- label: I.2.1 -->

Let `A → B` be a local homomorphism; from now on the rings are noetherian. Let `𝔪` be the maximal ideal of `A`. The
following conditions are equivalent:

1. `B/𝔪B` is finite-dimensional over `k = A/𝔪`.
1. `𝔪B` is an ideal of definition, and `B/𝔯(B) = κ(B)` is an extension of `k = κ(A)`.
1. The completion `B̂` is finite over the completion `Â` of `A`.

One then says that `B` is quasi-finite over `A`.

<!-- original page 2 -->

A morphism `f: X → Y` is said to be quasi-finite at `x`, or the `Y`-prescheme `f` is said to be quasi-finite at `x`, if
`𝒪_x` is quasi-finite over `𝒪_{f(x)}`. This is also equivalent to saying that `x` is isolated in its fiber `f⁻¹(f(x))`.
A morphism is said to be quasi-finite if it is so at every point.[^I-2-1]

**Corollary.**

<!-- label: I.2.2 -->

If `A` is complete, quasi-finite is equivalent to finite.

One could give the usual sorites (i), (ii), (iii), (iv), (v) for quasi-finite morphisms, but that does not seem
indispensable here.

## 3. Unramified or Net Morphisms

<!-- label: I.3 -->

**Proposition.**

<!-- label: I.3.1 -->

Let `f: X → Y` be a morphism of finite type, let `x ∈ X`, and let `y = f(x)`. The following conditions are equivalent:

1. `𝒪_x/𝔪_y𝒪_x` is a finite separable extension of `κ(y)`.
1. `Ω¹_{X/Y}` vanishes at `x`.
1. The diagonal morphism `Δ_{X/Y}` is an open immersion in a neighborhood of `x`.

For the implication (i) ⇒ (ii), Nakayama immediately reduces us to the case `Y = Spec(k)`, `X = Spec(k′)`, where this is
well known and, moreover, trivial from the definition of separability. The implication (ii) ⇒ (iii) follows from a
pleasant and easy characterization of open immersions, using Krull. For (iii) ⇒ (i), one is again reduced to the case
where `Y = Spec(k)` and where the diagonal morphism is everywhere an open immersion. One must then prove that `X` is
finite with separable coordinate ring over `k`; for this, one reduces to the case where `k` is algebraically closed. But
then every closed point of `X` is isolated, since it is identical with the inverse image of the diagonal by the morphism
`X → X ×_k X` defined by `x`; hence `X` is finite. We may then suppose that `X` is reduced to a point, with ring `A`, so
that `A ⊗_k A → A` is an isomorphism, whence `A = k`, as required.

**Definition.**

<!-- label: I.3.2 -->

1. One then says that `f` is net, or also unramified, at `x`, or that `X` is net, or unramified, at `x` over `Y`.
1. Let `A → B` be a local homomorphism. One says that it is net, or unramified, or that `B` is a local algebra net, or
    unramified, over `A`, if `B/𝔯(A)B` is a finite separable extension of `A/𝔯(A)`, i.e. if `𝔯(A)B = 𝔯(B)`, and `κ(B)`
    is a separable extension of `κ(A)`.[^I-3-1]

**Remark.**

<!-- original page 3 -->

The fact that `B` is net over `A` can already be recognized on the completions of `A` and `B`. Net implies quasi-finite.

**Corollary.**

<!-- label: I.3.3 -->

The set of points where `f` is net is open.

**Corollary.**

<!-- label: I.3.4 -->

Let `X′` and `X` be two preschemes of finite type over `Y`, and let `g: X′ → X` be a `Y`-morphism. If `X` is net over
`Y`, the graph morphism `Γ_g: X′ → X ×_Y X` is an open immersion.

Indeed, it is the inverse image of the diagonal morphism `X → X ×_Y X` by

```text
g ×_Y id_{X′}: X′ ×_Y X → X ×_Y X.
```

One may also introduce the annihilator ideal `𝔡_{X/Y}` of `Ω¹_{X/Y}`, called the different ideal of `X/Y`; it defines a
closed subprescheme of `X` which, set-theoretically, is the set of points where `X/Y` is ramified, i.e. not net.

**Proposition.**

<!-- label: I.3.5 -->

1. An immersion is net.
1. The composite of two net morphisms is net.
1. A base extension of a net morphism is again net.

This is seen indifferently from (ii) or (iii), the second seeming to me more amusing. One can of course also be more
precise by giving pointwise statements; this is only apparently more general, except in the setting of definition b),
and tedious. As usual, one obtains the following corollaries.

**Corollaries.**

<!-- label: I.3.6 -->

1. The cartesian product of two net morphisms is again net.
1. If `gf` is net, then `f` is net.
1. If `f` is net, then `f_red` is net.

**Proposition.**

<!-- label: I.3.7 -->

Let `A → B` be a local homomorphism, and suppose that the residue extension `κ(B)/κ(A)` is trivial, or that `κ(A)` is
algebraically closed. For `B/A` to be net, it is necessary and sufficient that `B̂` be, as an `Â`-algebra, a quotient of
`Â`.

**Remarks.**

- In the case where the residue extension is not assumed trivial, one can reduce to that case by making a suitable
    finite flat extension over `A` that kills the given extension.
- Give the example where `A` is the local ring of an ordinary double point of a curve, and `B` that of a point of the
    normalization: then `A ⊂ B`, `B` is net over `A` with trivial residue extension, and `Â → B̂` is surjective but not
    injective.

<!-- original page 4 -->

We shall therefore strengthen the notion of netness.

## 4. Étale Morphisms. Étale Coverings

<!-- label: I.4 -->

We shall admit everything that will be necessary for us concerning flat morphisms; these facts will be proved later, if
needed.[^I-4-1]

**Definition.**

<!-- label: I.4.1 -->

1. Let `f: X → Y` be a morphism of finite type. One says that `f` is étale at `x` if `f` is flat at `x` and net at `x`.
    One says that `f` is étale if it is so at all points. One says that `X` is étale at `x` over `Y`, or that it is a
    `Y`-prescheme étale at `x`, etc.
1. Let `f: A → B` be a local homomorphism. One says that `f` is étale, or that `B` is étale over `A`, if `B` is flat and
    unramified over `A`.[^I-4-2]

**Proposition.**

<!-- label: I.4.2 -->

For `B/A` to be étale, it is necessary and sufficient that `B̂/Â` be étale.

Indeed, this is true separately for "net" and for "flat".

<!-- original page 5 -->

**Corollary.**

<!-- label: I.4.3 -->

Let `f: X → Y` be of finite type, and let `x ∈ X`. The fact that `f` is étale at `x` depends only on the local
homomorphism `𝒪_{f(x)} → 𝒪_x`, and even only on the corresponding homomorphism for completions.

**Corollary.**

<!-- label: I.4.4 -->

Suppose that the residue extension `κ(A) → κ(B)` is trivial, or that `κ(A)` is algebraically closed. Then `B/A` is étale
if and only if `Â → B̂` is an isomorphism.

One combines flatness with I.3.7.

**Proposition.**

<!-- label: I.4.5 -->

Let `f: X → Y` be a morphism of finite type. Then the set of points where it is étale is open.

Indeed, this is true separately for "net" and for "flat".

This proposition shows that in the study of morphisms of finite type that are étale somewhere, one may drop the
"pointwise" statements.

**Proposition.**

<!-- label: I.4.6 -->

1. An open immersion is étale.
1. The composite of two étale morphisms is étale.
1. Base extension.

Indeed, (i) is trivial, and for (ii) and (iii) it suffices to note that this is true for "net" and for "flat". To tell
the truth, there are also corresponding statements for local homomorphisms, without finiteness conditions, which in any
case should appear in the multiplodocus, beginning with the net case.

**Corollary.**

<!-- label: I.4.7 -->

A cartesian product of two étale morphisms is likewise étale.

**Corollary.**

<!-- label: I.4.8 -->

Let `X` and `X′` be of finite type over `Y`, and let `g: X → X′` be a `Y`-morphism. If `X′` is unramified over `Y` and
`X` is étale over `Y`, then `g` is étale.

Indeed, `g` is the composite of the graph morphism `Γ_g: X → X ×_Y X′`, which is an open immersion by I.3.4, and the
projection morphism, which is étale because it is deduced from the étale morphism `X → Y` by the base change `X′ → Y`.

**Definition.**

<!-- label: I.4.9 -->

An étale covering, respectively a net covering, of `Y` is a `Y`-scheme `X` that is finite over `Y` and étale,
respectively net, over `Y`.

The first condition means that `X` is defined by a coherent sheaf `𝓑` of algebras on `Y`. The second then means that `𝓑`
is locally free over `Y`, respectively says nothing at all, and that moreover, for every `y ∈ Y`, the fiber
`𝓑(y) = 𝓑_y ⊗_{𝒪_y} κ(y)` is a separable algebra, that is, a finite product of finite separable extensions, over `κ(y)`.

**Proposition.**

<!-- label: I.4.10 -->

Let `X` be a flat covering of `Y` of degree `n`, defined by a coherent locally free sheaf `𝓑` of algebras. One defines,
in the well-known way, the trace homomorphism `𝓑 → 𝓐`, which is a homomorphism of `𝓐`-modules, where `𝓐 = 𝒪_Y`. For `X`
to be étale, it is necessary and sufficient that the corresponding bilinear form `tr_{𝓑/𝓐}(xy)` define an isomorphism
from `𝓑` to its dual, or equivalently that the discriminant section

```text
d_{X/Y} = d_{𝓑/𝓐} ∈ Γ(Y, ∧ⁿ𝓑̌ ⊗_𝓐 ∧ⁿ𝓑̌)
```

be invertible, or finally that the discriminant ideal defined by this section be the unit ideal.

Indeed, one is reduced to the case `Y = Spec(k)`, and then this is a well-known separability criterion, and trivial
after passage to the algebraic closure of `k`.

**Remark.**

<!-- original page 6 -->

We shall have a less trivial statement below, when one does not suppose a priori that `X` is flat over `Y` but makes a
normality hypothesis.

## 5. The Fundamental Property of Étale Morphisms

<!-- label: I.5 -->

**Theorem.**

<!-- label: I.5.1 -->

Let `f: X → Y` be a morphism of finite type. For `f` to be an open immersion, it is necessary and sufficient that it be
an étale and radicial morphism.

Recall that radicial means: injective, with radicial residue extensions; one may also recall that this means that the
morphism remains injective after every base extension. Necessity is trivial; sufficiency remains. We shall give two
different proofs, the first shorter, the second more elementary.

1. A flat morphism is open, so we may suppose, replacing `Y` by `f(X)`, that `f` is a homeomorphism onto `Y`. After any
    base extension, it remains true that `f` is flat, radicial, and surjective, hence a homeomorphism, a fortiori
    closed. Thus `f` is proper. Therefore `f` is finite, by Chevalley's theorem, and is defined by a coherent sheaf `𝓑`
    of algebras. The sheaf `𝓑` is locally free; moreover, by the hypothesis, it has rank 1 everywhere. Thus `X = Y`, as
    required.

1. One may suppose `Y` and `X` affine. Moreover, one easily reduces to proving the following: if `Y = Spec(A)`, with `A`
    local, and if `f⁻¹(y)` is nonempty, where `y` is the closed point of `Y`, then `X = Y`. Indeed, this will imply
    that every `y ∈ f(X)` has an open neighborhood `U` such that `X|U = U`. We have `X = Spec(B)`, and we want to prove
    `A = B`. For this, one is reduced to proving the analogous assertion after replacing `A` by `Â` and `B` by
    `B ⊗_A Â`, taking into account that `Â` is faithfully flat over `A`. We may therefore suppose `A` complete. Let `x`
    be the point over `y`. By Corollary I.2.2, `𝒪_x` is finite over `A`, hence, being flat and radicial over `A`, is
    identical with `A`. Thus `X = Y ⨿ X′`, a disjoint sum. Since `X` is radicial over `Y`, `X′` is empty. This
    completes the proof.

**Corollary.**

<!-- label: I.5.2 -->

Let `f: X → Y` be a closed immersion and étale. If `X` is connected, `f` is an isomorphism from `X` onto a connected
component of `Y`.

Indeed, `f` is also an open immersion. We deduce:

**Corollary.**

<!-- label: I.5.3 -->

<!-- original page 7 -->

Let `X` be a net `Y`-scheme, with `Y` connected. Then every section of `X` over `Y` is an isomorphism from `Y` onto a
connected component of `X`. Thus there is a one-to-one correspondence between the set of these sections and the set of
connected components `X_i` of `X` such that the projection `X_i → Y` is an isomorphism, or equivalently, by I.5.1, is
surjective and radicial. In particular, a section is known once its value at one point is known.

Only the first assertion requires proof. By I.5.2, it is enough to observe that a section is a closed immersion, since
`X` is separated over `Y`, and is étale by I.4.8.

**Corollary.**

<!-- label: I.5.4 -->

Let `X` and `Y` be two preschemes over `S`, with `X` net and separated over `S` and `Y` connected. Let `f` and `g` be
two `S`-morphisms from `Y` to `X`, and let `y` be a point of `Y`. Suppose `f(y) = g(y) = x` and that the residue
homomorphisms `κ(x) → κ(y)` defined by `f` and `g` are identical, that is, `f` and `g` coincide geometrically at `y`.
Then `f` and `g` are identical.

This follows from I.5.3 by reducing to the case `Y = S`, replacing `X` by `X ×_S Y`.

Here is a particularly important variant of I.5.3.

**Theorem.**

<!-- label: I.5.5 -->

Let `S` be a prescheme, `X` and `Y` two `S`-preschemes, `S₀` a closed subprescheme of `S` having the same underlying
space as `S`, and let `X₀ = X ×_S S₀` and `Y₀ = Y ×_S S₀` be the "restrictions" of `X` and `Y` to `S₀`. Suppose `X` is
étale over `S`. Then the natural map

```text
Hom_S(Y, X) → Hom_{S₀}(Y₀, X₀)
```

is bijective.

One is again reduced to the case `Y = S`, and then this follows from the "topological" description of sections of `X/Y`
given in I.5.3.

**Scholium.** This result includes both a uniqueness assertion and an existence assertion for morphisms. It may also be
expressed, when `X` and `Y` are both taken étale over `S`, by saying that the functor `X ↦ X₀` from the category of
étale `S`-schemes to the category of étale `S₀`-schemes is fully faithful, i.e. establishes an equivalence of the first
category with a full subcategory of the second. We shall see below that it is even an equivalence between the first and
the second; this will be an existence theorem for étale `S`-schemes.

<!-- original page 8 -->

The following form, apparently more general, of I.5.5 is often convenient.

**Corollary ("Extension theorem for liftings").**

<!-- label: I.5.6 -->

Consider a commutative diagram

```text
Y₀ → X
↓    ↓
Y  → S
```

of morphisms, where `X → S` is étale and `Y₀ → Y` is a bijective closed immersion. Then one can find a unique morphism
`Y → X` making the two corresponding triangles commute.

Indeed, replacing `S` by `Y` and `X` by `X ×_S Y`, one is reduced to the case `Y = S`, and then this is the special case
of I.5.5 for `Y = S`.

Let us also record the following immediate consequence of I.5.1, which we did not give as Corollary 1 so as not to
interrupt the line of ideas developed after I.5.1.

**Proposition.**

<!-- label: I.5.7 -->

Let `X` and `X′` be two preschemes of finite type and flat over `Y`, and let `g: X → X′` be a `Y`-morphism. For `g` to
be an open immersion, respectively an isomorphism, it is necessary and sufficient that for every `y ∈ Y`, the induced
morphism on fibers

```text
g ⊗_Y κ(y): X ⊗_Y κ(y) → X′ ⊗_Y κ(y)
```

be an open immersion, respectively an isomorphism.

It suffices to prove sufficiency; since this is true for the notion of surjection, one is reduced to the case of an open
immersion. By I.5.1, one must verify that `g` is radicial, which is trivial, and that it is étale, which follows from
Corollary I.5.9 below.

**Corollary.**

<!-- label: I.5.8 -->

(This should go in no. I.3.) Let `X` and `X′` be two `Y`-preschemes, let `g: X → X′` be a `Y`-morphism, let `x` be a
point of `X`, and let `y` be its projection to `Y`. For `g` to be quasi-finite, respectively net, at `x`, it is
necessary and sufficient that the same be true of `g ⊗_Y κ(y)`.

Indeed, the two algebras over `k(g(x))` that must be considered to ensure that one has a quasi-finite, respectively net,
morphism at `x` are the same for `g` and for `g ⊗_Y κ(y)`.

**Corollary.**

<!-- label: I.5.9 -->

<!-- original page 9 -->

With the notation of I.5.8, suppose `X` and `X′` are flat and of finite type over `Y`. For `g` to be flat, respectively
étale, at `x`, it is necessary and sufficient that `g ⊗_Y κ(y)` be so.

For "flat" the statement is included only as a reminder; it is one of the fundamental criteria for flatness.[^I-5-1] For
"étale", it follows from this, taking I.5.8 into account.

## 6. Application to Étale Extensions of Complete Local Rings

<!-- label: I.6 -->

This number is a special case of results on formal preschemes that should appear in the multiplodocus. Nevertheless,
here one gets by at less cost, i.e. without the explicit local determination of étale morphisms in no. I.7, which uses
the Main Theorem. That may be a sufficient reason to keep the present number, even in the multiplodocus, in this place.

**Theorem.**

<!-- label: I.6.1 -->

Let `A` be a complete local ring, noetherian of course, with residue field `k`. For every `A`-algebra `B`, let
`R(B) = B ⊗_A k`, considered as a `k`-algebra; it thus depends functorially on `B`. Then `R` defines an equivalence from
the category of `A`-algebras finite and étale over `A` to the category of finite-rank separable algebras over `k`.

First of all, the functor in question is fully faithful, as follows from the more general fact:

**Corollary.**

<!-- label: I.6.2 -->

Let `B` and `B′` be two `A`-algebras finite over `A`. If `B` is étale over `A`, then the canonical map

```text
Hom_{A-alg}(B, B′) → Hom_{k-alg}(R(B), R(B′))
```

is bijective.

One is reduced to the case where `A` is artinian, replacing `A` by `A/𝔪ⁿ`, and then this is a special case of I.5.5.

It remains to prove that for every finite separable `k`-algebra, why not say étale, since it is shorter, `L`, there
exists `B` étale over `A` such that `R(B)` is isomorphic to `L`. We may suppose that `L` is a separable extension of
`k`; as such it admits a generator `x`, i.e. is isomorphic to an algebra `k[t]/Fk[t]`, where `F ∈ k[t]` is a monic
polynomial. Lift `F` to a monic polynomial `F₁` in `A[t]`, and take `B = A[t]/F₁A[t]`.

## 7. Local Construction of Unramified and Étale Morphisms

<!-- label: I.7 -->

<!-- original page 10 -->

**Proposition.**

<!-- label: I.7.1 -->

Let `A` be a noetherian ring, `B` a finite algebra over `A`, `u` a generator of `B` over `A`, `F ∈ A[t]` such that
`F(u) = 0`, where `F` is not assumed monic, `u′ = F′(u)`, where `F′` is the derived polynomial, `𝔮` a prime ideal of `B`
not containing `u′`, and `𝔭` its trace on `A`. Then `B_𝔮` is net over `A_𝔭`.

In other words, putting `Y = Spec(A)`, `X = Spec(B)`, and `X_{u′} = Spec(B_{u′})`, `X_{u′}` is unramified over `Y`. The
statement follows from the following more precise one.

**Corollary.**

<!-- label: I.7.2 -->

The different ideal of `B/A` contains `u′B`, and is equal to it if the natural homomorphism `A[t]/FA[t] → B`, sending
`t` to `u`, is an isomorphism.

Let `J` be the kernel of the homomorphism `C = A[t] → B`. This kernel contains `FA[t]`, and is equal to it in the second
case considered in I.7.2. Since the homomorphism is surjective, `Ω¹_{B/A}` identifies with the quotient of `Ω¹_{C/A}` by
the submodule generated by `JΩ¹_{C/A}` and `d(J)`; one should have made explicit in no. I.1 the definition of the
homomorphism `d` and the computation of `Ω¹` for a polynomial algebra. Identifying `Ω¹_{C/A}` with `C` by means of the
basis `dt`, one finds `B/B·J′`, so the different is generated by the set `J′` of images in `B` of the derivatives of
`G ∈ J`, and it suffices to take `G` running through generators of `J`.

Since `F ∈ J`, respectively since `F` is a generator of `J`, we are done. Note that I.7.2 should be made the proposition
and I.7.1 the corollary. We find:

**Corollary.**

<!-- label: I.7.3 -->

Under the conditions of I.7.1, suppose `F` is monic and that `A[t]/FA[t] → B` is an isomorphism. For `B_𝔮` to be étale
over `A_𝔭`, it is necessary and sufficient that `𝔮` not contain `u′`.

Indeed, since `B` is flat over `A`, étale is equivalent to net, and one may apply I.7.2.

**Corollary.**

<!-- label: I.7.4 -->

Under the conditions of I.7.3, for `B` to be étale over `A`, it is necessary and sufficient that `u′` be invertible, or
again that the ideal generated by `F` and `F′` in `A[t]` be the unit ideal.

The last criterion follows from the first and from Nakayama, in `B`.

<!-- original page 11 -->

A monic polynomial `F ∈ A[t]` having the property stated in Corollary I.7.4 is called a separable polynomial. If `F` is
not monic, one would at least have to require that the coefficient of its leading term be invertible; in the case where
`A` is a field, one recovers the usual definition.

**Corollary.**

<!-- label: I.7.5 -->

Let `B` be a finite algebra over the local ring `A`. Suppose that `K(A)` is infinite or that `B` is local. Let `n` be
the rank of `L = B ⊗_A K(A)` over `K(A) = k`. For `B` to be net, respectively étale, over `A`, it is necessary and
sufficient that `B` be isomorphic to a quotient of, respectively isomorphic to, `A[t]/FA[t]`, where `F` is a monic
separable polynomial, which one may suppose, respectively which is necessarily, of degree `n`.

Only necessity has to be proved. Suppose `B` is net over `A`, hence `L` is separable over `k`. It then follows from the
hypothesis made that `L/k` admits a generator `ξ`, so the `ξⁱ`, with `0 ≤ i < n`, form a basis of `L` over `k`. Let
`u ∈ B` lift `ξ`. Then, by Nakayama, the `uⁱ`, with `0 ≤ i < n`, generate the `A`-module `B`, respectively form a basis
of it. In particular, one can find a monic polynomial `F ∈ A[t]` such that `F(u) = 0`, and `B` will be isomorphic to a
quotient of, respectively isomorphic to, `A[t]/FA[t]`. Finally, by I.7.4 applied to `L/k`, `F` and `F′` generate `A[t]`
modulo `𝔪A[t]`, hence by Nakayama in `A[t]/FA[t]`, `F` and `F′` generate `A[t]`. This completes the proof.

**Theorem.**

<!-- label: I.7.6 -->

Let `A` be a local ring, and let `A → 𝒪` be a local homomorphism such that `𝒪` is isomorphic to a localized algebra of
an algebra of finite type over `A`. Suppose `𝒪` is net over `A`. Then one can find an `A`-algebra `B`, integral over
`A`, a maximal ideal `𝔫` of `B`, a generator `u` of `B` over `A`, and a monic polynomial `F ∈ A[t]`, such that `𝔫` does
not contain `F′(u)` and `𝒪` is isomorphic, as an `A`-algebra, to `B_𝔫`. If `𝒪` is étale over `A`, one can take
`B = A[t]/FA[t]`.

Of course, these are also sufficient conditions.

Let us first record the pleasant corollaries.

**Corollary.**

<!-- label: I.7.7 -->

For `𝒪` to be net over `A`, it is necessary and sufficient that `𝒪` be isomorphic to the quotient of an analogous
algebra that is étale over `A`.

Indeed, take `𝒪′ = B′_{𝔫′}`, where `B′ = A[t]/FA[t]` and where `𝔫′` is the inverse image of `𝔫` in `B′`.

**Corollary.**

<!-- label: I.7.8 -->

<!-- original page 12 -->

Let `f: X → Y` be a morphism of finite type, and let `x ∈ X`. For `f` to be net at `x`, it is necessary and sufficient
that there exist an open neighborhood `U` of `x` such that `f|U` factors as `U → X′ → Y`, where the first arrow is a
closed immersion and the second is an étale morphism.

This is a simple translation of I.7.7.

Let us show how the jargon of I.7.6 follows from the principal statement: indeed, by I.7.7 there exists an epimorphism
`𝒪′ → 𝒪`, where `𝒪` has the required properties; but since `𝒪′` and `𝒪` are étale over `A`, the morphism `𝒪′ → 𝒪` is
étale by I.4.8, hence an isomorphism.

### Proof of I.7.6

This repeats a proof from Chevalley's seminar. By the Main Theorem, one will have `𝒪 = B_𝔫`, where `B` is a finite
algebra over `A` and `𝔫` is a maximal ideal of `B`. Then `B/𝔫 = K(𝒪)` is a separable, hence monogenic, extension of `k`.
If `𝔫_i`, `1 ≤ i ≤ r`, are the maximal ideals of `B` distinct from `𝔫`, there therefore exists an element `u` of `B`
that belongs to all the `𝔫_i` and whose image in `B/𝔫` is a generator. But `B/𝔫 = B_𝔫/𝔫B_𝔫 = B_𝔫/𝔪B_𝔫`, where `𝔪` is the
maximal ideal of `A`. Let us admit for a moment the following lemma.

**Lemma.**

<!-- label: I.7.9 -->

Let `A` be a local ring, `B` a finite algebra over `A`, `𝔫` a maximal ideal of `B`, and `u` an element of `B` whose
image in `B_𝔫/𝔪B_𝔫` generates it as an algebra over `k = A/𝔪`, and which lies in every maximal ideal of `B` distinct
from `𝔫`. Let `B′ = B[u]` and `𝔫′ = 𝔫B′`. Then the canonical homomorphism `B′_{𝔫′} → B_𝔫` is an isomorphism.

**Lemma.**

<!-- label: I.7.10 -->

(This should have appeared as a corollary to I.7.1, before I.7.5, which it implies.) Let `B` be a finite algebra over
`A` generated by an element `u`, and let `𝔫` be a maximal ideal of `B` such that `B_𝔫` is unramified over `A`. Then
there exists a monic polynomial `F ∈ A[t]` such that `F(u) = 0` and `F′(u) ∉ 𝔫`.

Indeed, let `n` be the rank of the `k`-algebra `L = B ⊗_A k`. By Nakayama, there exists a monic polynomial of degree `n`
in `A[t]` such that `F(u) = 0`. Let `f` be the polynomial deduced from `F` by reduction mod `𝔪`. Then `L` is
`k`-isomorphic to `k[t]/fk[t]`, hence by I.7.3, `f′(ξ)` is not contained in the maximal ideal of `L` corresponding to
`𝔫`, where `ξ` denotes the image of `t` in `L`, i.e. the image of `u` in `L`. Since `f′(ξ)` is the image of `F′(u)`, we
are done.

<!-- original page 13 -->

Theorem I.7.6 now follows by combining I.7.9 and I.7.10. It remains to prove I.7.9. Put `S′ = B′ − 𝔫′`, so
`B′S′⁻¹ = B′_{𝔫′}`. Similarly let `S = B − 𝔫`, so `BS⁻¹ = B_𝔫`. We therefore have a natural homomorphism
`B S′⁻¹ → BS⁻¹ = B_𝔫`. Let us prove that it is an isomorphism, i.e. that the elements of `S` are invertible in `B S′⁻¹`,
i.e. that every maximal ideal `𝔭` of the latter does not meet `S`, i.e. induces `𝔫` on `B`.

Indeed, since `B S′⁻¹` is finite over `B′S′⁻¹ = B′_{𝔫′}`, `𝔭` induces the unique maximal ideal `𝔫′B′_{𝔫′}` of `B′_{𝔫′}`,
hence induces the maximal ideal `𝔫′` of `B′`. Since `B` is finite over `B′`, the ideal `𝔮` of `B` induced by `𝔭`, lying
over `𝔫′`, is necessarily maximal and does not contain `u`, hence is identical with `𝔫`. Here we have just used that `u`
belongs to every maximal ideal of `B` distinct from `𝔫`.

Let us now prove that `B S′⁻¹` equals `B′S′⁻¹`. Since it is finite over the latter, Nakayama reduces us to proving
equality modulo `𝔫′B S′⁻¹`, and a fortiori it suffices to prove equality modulo `𝔪B S′⁻¹`. But

```text
B S′⁻¹ / 𝔪B S′⁻¹ = B_𝔫 / 𝔪B_𝔫
```

is generated over `k` by `u`, using here the other property of `u`. Thus the image of `B′`, and a fortiori of `B′S′⁻¹`,
in it is everything, as a subring containing `k` and the image of `u`.

**Remark.** One should be able to state Theorem I.7.6 for a ring `𝒪` that is only semilocal, so as also to cover I.7.5:
one would make the hypothesis that `𝒪/𝔪𝒪` is a monogenic `k`-algebra. One could then find `u ∈ B` whose image in `B/𝔪B`
is a generator and which belongs to all maximal ideals of `B` not coming from `𝒪`. Lemmas I.7.9 and I.7.10 should adapt
without difficulty. More generally, ...

## 8. Infinitesimal Lifting of Étale Schemes. Application to Formal Schemes

<!-- label: I.8 -->

**Proposition.**

<!-- label: I.8.1 -->

Let `Y` be a prescheme, `Y₀` a subprescheme, `X₀` an étale `Y₀`-scheme, and `x` a point of `X₀`. Then there exists an
étale `Y`-scheme `X`, a neighborhood `U₀` of `x` in `X₀`, and a `Y₀`-isomorphism `U₀ ≅ X ×_Y Y₀`.

Indeed, let `y` be the projection of `x` in `Y₀`. Applying I.7.6 to the étale local homomorphism `A₀ → B₀` of the local
rings of `y` and `x` in `Y₀` and `X₀`, one finds an isomorphism

```text
B₀ = (C₀)_{𝔫₀},     C₀ = A₀[t]/F₀A₀[t],
```

where `F₀` is a monic polynomial and `𝔫₀` is a maximal ideal of `C₀` not containing the class of `F′₀(t)` in `C₀`. Let
`A` be the local ring of `y` in `Y`, let `F` be a monic polynomial in `A[t]` giving `F₀` under the surjective
homomorphism `A → A₀`, by lifting the coefficients of `F₀`, and finally let `C = A[t]/FA[t]`, and let `𝔫` be the maximal
ideal of `C` which is the inverse image of `𝔫₀` under the natural epimorphism `C → C ⊗_A A₀ = C₀`. Put `B = C_𝔫`. It is
immediate by construction and I.7.1 that `B` is étale over `A`, and that one has an isomorphism `B ⊗_A A₀ = A₀`.

One knows, from EGA Chapter I as indicated in the introduction, that there exists a `Y`-scheme of finite type `X` and a
point `z` of `X` over `y` such that `𝒪_z` is `A`-isomorphic to `C`. Since the latter is étale over `A = 𝒪_y`, one may,
by taking `X` small enough, suppose that `X` is étale over `Y`. Let `X′₀ = X ×_Y Y₀`. Then the local ring of `z` in
`X′₀` identifies with `𝒪_z ⊗_A A₀ = B ⊗_A A₀`, hence is isomorphic to `B₀`. This isomorphism is defined by an
isomorphism from a neighborhood `U₀` of `x` in `X₀` onto a neighborhood of `z` in `X′₀`, and by taking `X` small enough
one may suppose this neighborhood identical with `X′₀`. We are done.

**Corollary.**

<!-- label: I.8.2 -->

There is an analogous statement for étale coverings, assuming the residue field `κ(y)` infinite.

The proof is the same, with I.7.5 replacing I.7.6.

**Theorem.**

<!-- label: I.8.3 -->

The functor considered in I.5.5 is an equivalence of categories.

By Theorem I.5.5, it remains to show that every étale `S₀`-scheme `X₀` is isomorphic to an `S₀`-scheme `X ×_S S₀`, where
`X` is an étale `S`-scheme. The underlying topological space of `X` must necessarily be identical with that of `X₀`,
with `X₀` furthermore identifying with a closed subprescheme of `X`.

The problem is therefore equivalent to the following one: find on the underlying topological space `|X₀|` of `X₀` a
sheaf of algebras `𝒪_X` over `f₀⁎(𝒪_S)`, where `f₀` is the projection `X₀ → S₀`, here regarded as a continuous map of
underlying spaces, making `|X₀|` into an étale `S`-prescheme `X`, together with a homomorphism of algebras
`𝒪_X → 𝒪_{X₀}`, compatible with the homomorphism `f₀⁎(𝒪_S) → f₀⁎(𝒪_{S₀})` on the sheaves of scalars, and inducing an
isomorphism

```text
𝒪_X ⊗_{f₀⁎(𝒪_S)} f₀⁎(𝒪_{S₀}) ≅ 𝒪_{X₀}.
```

Then `X` will be an étale `S`-prescheme reducing to `X₀`.

<!-- original page 15 -->

Thus `X` will be separated over `S`, since `X₀` is separated over `S₀`, and `X` answers the question. Moreover, if
`(U_i)` is a covering of `X₀` by open subsets, and if one has found a solution of the problem in each `U_i`, then it
follows from the uniqueness theorem I.5.5 that these solutions glue, i.e. that the sheaves of algebras defining them,
equipped with their augmentation homomorphisms, glue; one immediately checks that the locally ringed space thereby
constructed over `S` is an étale `S`-prescheme `X` equipped with an isomorphism `X ×_S S₀ ≅ X₀`. It therefore suffices
to find a solution locally, which is assured by I.8.1.

**Corollary.**

<!-- label: I.8.4 -->

Let `S` be a locally noetherian formal prescheme, equipped with an ideal of definition `J`, and let `S₀ = (|S|, 𝒪_S/J)`
be the corresponding ordinary prescheme. Then the functor `𝔛 ↦ 𝔛 ×_S S₀` from the category of étale coverings of `S` to
the category of étale coverings of `S₀` is an equivalence of categories.

Of course, by an étale covering of a formal prescheme `S` we mean a covering of `S`, i.e. a formal prescheme over `S`
defined by a coherent sheaf `𝓑` of algebras, such that `𝓑` is locally free and such that the residue fibers
`𝓑_s ⊗_{𝒪_s} κ(s)` of `𝓑` are separable algebras over `κ(s)`. If `S_n` denotes the ordinary prescheme `(|S|, 𝒪_S/Jⁿ⁺¹)`,
the data of a coherent sheaf of algebras `𝓑` on `S` is equivalent to the data of a sequence of coherent sheaves of
algebras `𝓑_n` on the `S_n`, equipped with a transitive system of homomorphisms `𝓑_m → 𝓑_n`, for `m ≥ n`, defining
isomorphisms

```text
𝓑_m ⊗_{𝒪_{S_m}} 𝒪_{S_n} ≅ 𝓑_n.
```

It is immediate that `𝓑` is locally free if and only if the `𝓑_n` on the `S_n` are locally free, and that the
separability condition is satisfied if and only if it is satisfied for `𝓑₀`, or equivalently for all the `𝓑_n`. Thus `𝓑`
is étale over `S` if and only if the `𝓑_n` over the `S_n` are étale. Taking this into account, I.8.4 follows at once
from I.8.3.

**Remark.** It was not necessary in I.8.4 to restrict to the case of coverings. It is, however, the only case used for
the moment.

## 9. Permanence Properties

<!-- label: I.9 -->

Let `A → B` be a local and étale homomorphism. We examine here a few cases where a certain property of `A` implies the
same property for `B`, or conversely.

<!-- original page 16 -->

A certain number of such propositions are already consequences of the simple fact that `B` is quasi-finite and flat over
`A`, and we shall limit ourselves to "recalling" a few of them: `A` and `B` have the same Krull dimension and the same
depth, "cohomological codimension" in Serre's still-current terminology. It follows, for example, that `A` is
Cohen-Macaulay if and only if `B` is Cohen-Macaulay.

Moreover, for every prime ideal `𝔮` of `B` inducing `𝔭` on `A`, `B_𝔮` will again be quasi-finite and flat over `A_𝔭`,
provided `B` is assumed to be a localization of an algebra of finite type over `A`; this follows from the fact that the
set of points where a morphism of finite type is quasi-finite, respectively flat, is open. And moreover every prime
ideal `𝔭` of `A` is induced by a prime ideal `𝔮` of `B`, because `B` is faithfully flat over `A`. It follows for example
that `𝔭` and `𝔮` have the same rank, and also that `A` has no embedded prime ideal if and only if `B` has none.

We shall therefore restrict ourselves to propositions more special to the case of étale morphisms.

**Proposition.**

<!-- label: I.9.1 -->

Let `A → B` be a local étale homomorphism. For `A` to be regular, it is necessary and sufficient that `B` be regular.

Indeed, let `k` be the residue field of `A`, and `L` that of `B`. Since `B` is flat over `A` and `L = B ⊗_A k`, i.e.
`𝔫 = 𝔪B`, where `𝔪` and `𝔫` are the maximal ideals of `A` and `B`, the `𝔪`-adic filtration on `B` is identical with its
`𝔫`-adic filtration, and one will have

```text
gr*(B) = gr*(A) ⊗_k L.
```

It follows that `gr*(B)` is a polynomial algebra over `L` if and only if `gr*(A)` is a polynomial algebra over `k`. This
proves the assertion. Note that we did not use the fact that `L/k` is separable.

**Corollary.**

<!-- label: I.9.2 -->

Let `f: X → Y` be an étale morphism. If `Y` is regular, then `X` is regular; the converse is true if `f` is surjective.

**Proposition.**

<!-- label: prop:I.9.2 -->

Let `f: X → Y` be an étale morphism. If `Y` is reduced, then so is `X`; the converse is true if `f` is surjective.

This is equivalent to:

**Corollary.**

<!-- label: I.9.3 -->

<!-- original page 17 -->

Let `f: A → B` be a local étale homomorphism, with `B` isomorphic to a localized `A`-algebra of an `A`-algebra of finite
type. For `A` to be reduced, it is necessary and sufficient that `B` be reduced.

Necessity is trivial, since `A → B` is injective, `B` being faithfully flat over `A`. For sufficiency, let `𝔭_i` be the
minimal prime ideals of `A`. By hypothesis the natural map `A → ∏_i A/𝔭_i` is injective; tensoring with the flat
`A`-module `B`, one finds that `B → ∏_i B/𝔭_iB` is injective, and one is reduced to proving that the `B/𝔭_iB` are
reduced. Since `B/𝔭_iB` is étale over `A/𝔭_i`, one is reduced to the case where `A` is integral.

Let `K` be its field of fractions. Since `A → K` is injective, the same is true, `B` being `A`-flat, of `B → B ⊗_A K`;
we are reduced to proving that this latter ring is reduced. But `B`, being a localization of an `A`-algebra of finite
type over `A`, is the local ring of a point `x` of a scheme `X = Spec(C)` of finite type and étale over `Y = Spec(A)`.
Thus `B ⊗_A K` is a localized ring, with respect to a suitable multiplicatively stable set, of the ring `C ⊗_A K` of
`X ⊗_A K`. Since `X ⊗_A K` is étale over `K`, its ring is a finite product of fields, separable extensions of `K`, and
the same is therefore true of `B ⊗_A K`. This proves the assertion.

**Corollary.**

<!-- label: I.9.4 -->

Let `f: A → B` be a local étale homomorphism, and suppose `A` analytically reduced, i.e. the completion `Â` of `A` has
no nilpotent elements. Then `B` is analytically reduced, and a fortiori reduced.

Indeed, `B̂` is finite and étale over `Â`, and one applies I.9.3.

**Theorem.**

<!-- label: I.9.5 -->

Let `f: A → B` be a local homomorphism, with `B` isomorphic to a localized algebra of an `A`-algebra of finite type.
Then:

1. If `f` is étale, `A` is normal if and only if `B` is normal.
1. If `A` is normal, `f` is étale if and only if `f` is injective and net; then `B` is normal by (i).

We shall give two different proofs of (i). The first uses some properties of quasi-finite flat morphisms, recalled at
the beginning of this number, without using I.7.6, and hence without using the Main Theorem; for the second proof the
reverse is true. Finally, for (ii), it seems that one needs the Main Theorem in any case.

### First Proof

We use the following necessary and sufficient condition for normality of a noetherian local ring `A` of nonzero
dimension.

<!-- original page 18 -->

**Serre's Criterion.** (i) For every prime ideal `𝔭` of `A` of rank 1, `A_𝔭` is normal, or equivalently regular. (ii)
For every prime ideal `𝔭` of `A` of rank `≥ 2`, `depth A_𝔭 ≥ 2`.[^I-9-1]

We shall admit this criterion here; it is supposed to appear in the paragraph on flat morphisms. Its principal advantage
is that it does not suppose a priori that `A` is reduced, nor a fortiori integral. Here, we may already suppose
`dim A = dim B ≠ 0`.

By the reminders at the beginning of this number, the prime ideals `𝔭` of `A` of rank 1, respectively of rank `≥ 2`, are
exactly the traces on `A` of the prime ideals `𝔮` of `B` of rank 1, respectively of rank `≥ 2`. Finally, if `𝔭` and `𝔮`
correspond, `B_𝔮` is étale over `A_𝔭`, hence has the same depth as `A_𝔭`, and is regular if and only if `A_𝔭` is
regular, by I.9.1. Applying Serre's criterion, one finds that `A` is normal if and only if `B` is.

### Second Proof

Suppose `B` normal, let `L` be its field of fractions, and `K` that of `A`; `A` is integral since `B` is. We saw in the
proof of I.9.3 that `B ⊗_A K` is a finite product of fields. Since it is contained in `L`, it is a field, and since it
contains `B`, it is `L`. An element of `K` integral over `A` is integral over `B`, hence lies in `B` since `B` is
normal, and therefore lies in `A` because `B ∩ K = A`, as follows from the fact that `B` is faithfully flat over `A`.

Now suppose `A` normal, and prove that `B` is normal. By I.7.6 one has `B = B′_𝔫`, where `B′ = A[t]/FA[t]`, with `F` and
`𝔫` as in I.7.6. Thus `L = B ⊗_A K` will be a localization of `B′ ⊗_A K = K[t]/FK[t]`, and a product of fields, finite
separable extensions of `K`. This latter product, as happens whenever one localizes an artinian ring, here `B′_K` with
respect to a multiplicatively stable set, is a direct factor of `B′_K`, hence corresponds to a decomposition `F = F₁F₂`
in `K[t]`, with the generator of `L` corresponding to `t` already annihilated by `F₁`.

But since `A` is normal, the `F_i` lie in `A[t]`, assuming them monic. Observing that `B → L = B ⊗_A K` is injective,
since `A → K` is injective and `B` is flat over `A`, it follows that one already has `F₁(u) = 0`, with `u` the class of
`t` in `L`. If `F` has been chosen of minimal degree, it follows that `F₂ = 1`. Note that
`F′(u) = F′₁(u)F₂(u) + F₁(u)F′₂(u) = F′₁(u)F₂(u)`, since `F₁(u) = 0`; hence `F′₁(u) ≠ 0` since `F′(u) ≠ 0`.

<!-- original page 19 -->

Thus one has

```text
(*)  L = B ⊗_A K = K[t]/FK[t],
```

and `F` is consequently a separable polynomial in `K[t]`, though evidently not necessarily in `A[t]`. Note that for the
moment, one has only shown, essentially, that in I.7.6 one can choose `F` and `𝔫` in such a way that, with the notation
used here, `B′ → B′_𝔫 = B` is injective. We used the normality of `A` for this; I do not know whether it remains true
without the normality hypothesis.

Recall now the well-known lemma, extracted from Serre's course of last year.

**Lemma.**

<!-- label: I.9.6 -->

Let `K` be a ring, `F ∈ K[t]` a monic separable polynomial, `L = K[t]/FK[t]`, and `u` the class of `t` in `L`, so that
`F′(u)` is an invertible element of `L`. Then one has the following formulas, where `n = deg F`:

```text
tr_{L/K}(uⁱ/F′(u)) = 0    if 0 ≤ i < n − 1,
tr_{L/K}(uⁿ⁻¹/F′(u)) = 1.
```

**Corollary.**

<!-- label: I.9.7 -->

The determinant of the matrix

```text
(uʲ · uⁱ/F′(u))_{0≤i,j≤n−1}
```

is equal to `(-1)ⁿ⁽ⁿ⁻¹⁾/²`, hence is invertible in every subring `A` of `K`.

**Corollary.**

<!-- label: I.9.8 -->

Let `A` be a subring of `K`, let `V` be the `A`-module generated by the `uⁱ`, `0 ≤ i ≤ n − 1`, in `L`, and let `V′` be
the sub-`A`-module of `L` formed by the `x ∈ L` such that `tr_{L/K}(xy) ∈ A` for every `y ∈ V`, i.e. for `y` of the form
`uⁱ`, `0 ≤ i ≤ n − 1`. Then `V′` is the `A`-module having as basis the `uⁱ/F′(u)`, `0 ≤ i ≤ n − 1`.

**Corollary.**

<!-- label: I.9.9 -->

Suppose `K` is the field of fractions of a normal integral ring `A`, and that `F` has its coefficients in `A`. Then,
with the notation of I.9.8, `V′` contains the normal closure `A′` of `A` in `L`, which is therefore contained in
`A[u]/F′(u)`, and a fortiori in `A[u][F′(u)⁻¹]`.

Apply this last corollary to the situation obtained in the proof: since `F′(u)` is invertible in `B`, which contains
`A[u]`, `B` contains `A′`. By the Main Theorem, or from the fact that `B = A[u]_𝔫`, `B` is a localized algebra of `A′`.
Since `A′` is normal, so is `B`.

### Proof of (ii)

<!-- original page 20 -->

Proceed as in the preceding proof to show that in I.7.6 one can choose `F` in such a way that `(*)` still holds. The
only a priori obstacle is that, `B` no longer being assumed flat over `A`, one can no longer assert that `B → L` is
injective, so the reasoning applies a priori only to the image `B₁` of `B` under that homomorphism. It follows at once
that `B₁` is flat over `A`, as a localization of a free algebra over `A`. By I.4.8 the morphism `B → B₁` is étale, hence
an isomorphism, which completes the proof.

From the editorial point of view, the last two proofs should be interchanged, and the formal computations of the lemma
and its corollaries should be put in a separate number.

**Corollary.**

<!-- label: I.9.10 -->

Let `f: X → Y` be an étale morphism. If `Y` is normal, then `X` is normal; the converse is true if `f` is surjective.

**Corollary.**

<!-- label: I.9.11 -->

Let `f: X → Y` be a dominant morphism, with `Y` normal and `X` connected. If `f` is net, then `f` is étale; hence `X` is
normal and therefore, being connected, irreducible.

Let `U` be the set of points where `f` is étale. It is open, and it suffices to show that it is also closed and
nonempty. The set `U` contains the inverse image of the generic point of `Y`, since for an algebra over a field,
unramified equals étale; hence, since `X` dominates `Y`, `U` is nonempty. If `x` belongs to the closure of `U`, then it
belongs to the closure of an irreducible component `U_i` of `U`, hence to an irreducible component `X_i := closure(U_i)`
of `X` that meets `U`, and therefore dominates `Y`, since every component of `U`, being flat over `Y`, dominates `Y`.
Consequently, if `y` is the projection of `x` to `Y`, `𝒪_y → 𝒪_x` is injective, taking into account that `𝒪_y` is
integral. Since `𝒪_y` is normal and `𝒪_y → 𝒪_x` is net, one concludes using I.9.5(ii).

**Corollary.**

<!-- label: I.9.12 -->

Let `f: X → Y` be a dominant morphism of finite type, with `Y` normal and `X` irreducible. Then the set of points where
`f` is étale is identical with the complement of the support of `Ω¹_{X/Y}`, i.e. with the complement of the subprescheme
of `X` defined by the different ideal `𝔡_{X/Y}`.

<!-- original page 21 -->

This is the "less trivial" statement alluded to in the remark in no. I.4.

**Remark.** One should be careful not to believe that a connected étale covering of an irreducible scheme is itself
irreducible, when the base is not assumed normal. This question will be studied in no. I.11.

## 10. Étale Coverings of a Normal Scheme

<!-- label: I.10 -->

**Proposition.**

<!-- label: I.10.1 -->

Let `X` be a prescheme étale and separated over a connected normal `Y` with field `K`. Then the connected components
`X_i` of `X` are integral, their fields `K_i` are finite separable extensions of `K`, and `X_i` identifies with a
nonempty open part of the normalization of `Y` in `K_i`; hence `X` identifies with a dense open part of the
normalization of `Y` in `R(X) = L = ∏ K_i`.

By I.9.10, `X` is normal; a fortiori its local rings are integral, so the connected components of `X` are irreducible.
Since `X_i` is normal, and finite and dominant over `Y`, it follows from a special case, almost trivial moreover, of the
Main Theorem that `X_i` is an open subset of the normalization of `Y` in the field `K_i` of `X`.

**Corollary.**

<!-- label: I.10.2 -->

Under the conditions of I.10.1, `X` is finite over `Y`, i.e. an étale covering of `Y`, if and only if `X` is isomorphic
to the normalization `Y′` of `Y` in `L = R(X)`, the ring of rational functions on `X`.

Indeed, one knows that this normalization is finite over `Y`, since `Y` is normal and `R/K` is separable. Conversely, if
`X` is finite over `Y`, it is finite over `Y′`, so its image in `Y′` is closed; on the other hand it is dense.

An algebra `L` of finite rank over `K` will be said to be unramified over `X`, or simply unramified over `K` if `X` is
understood, if `L` is a separable algebra over `K`, i.e. a direct product of separable extensions `K_i`, and if the
normalization `Y′` of `Y` in `L`, the disjoint sum of the normalizations of `Y` in the `K_i`, is unramified, hence étale
by I.9.11, over `Y`. Thus:

**Corollary.**

<!-- label: I.10.3 -->

For every `X` finite over `Y` and such that every irreducible component dominates `Y`, let `R(X)` be the ring of
rational functions on `X`, the product of the local rings of the generic points of the irreducible components of `X`.

<!-- original page 22 -->

Thus `X ↦ R(X)` is a functor, with values in algebras of finite rank over `K = R(Y)`. This functor establishes an
equivalence from the category of connected étale coverings of `Y` to the category of extensions `L` of `K` unramified
over `Y`.

The inverse functor is the normalization functor.

Suppose `Y` affine, hence defined by a normal ring `A` with field of fractions `K`. Let `L` be a finite extension of `K`
that is a direct product of fields. Then, by definition, the normalization `Y′` of `Y` in `L` is isomorphic to
`Spec(A′)`, where `A′` is the normalization of `A` in `L`. Saying that `L` is unramified over `Y` means that `A′` is
unramified, or equivalently étale, over `A`. If `A` is local, this is equivalent to saying that the local rings `A′_𝔫`,
where `𝔫` runs through the finite set of maximal ideals of `A′`, i.e. of its prime ideals inducing the maximal ideal `𝔪`
of `A`, are unramified, hence étale, over the local ring `A`.

Finally, note also that the discriminant criterion I.4.10 can also be applied in this situation. More generally, a
variant of that criterion should be stated as follows, without a preliminary flatness condition when `X` dominates `Y`,
though `Y` is still assumed locally integral: `A → B` and `B → B ⊗_A K = L` are injective, so `tr_{L/K}` is defined, and
`tr_{L/K}(xy)` induces a fundamental bilinear form `B × B → A`, i.e. there exist `x_i ∈ B`, `1 ≤ i ≤ n`, with `n` the
rank of `L` over `K`, such that `tr(x_ix_j) ∈ A` for all `i, j`, and `det(tr(x_ix_j))` is invertible in `A`.

The sorites I.4.6 immediately imply the sorites of unramifiedness in the classical setting.

**Proposition.**

<!-- label: I.10.4 -->

Let `Y` be a normal integral prescheme, with field `K`.

1. `K` is unramified over `Y`.
1. If `L` is an extension of `K` unramified over `Y`, if `Y′` is a normal prescheme with field `L` and dominating `Y`,
    for example the normalization of `Y` in `L`, and if `M` is an extension of `L` unramified over `Y′`, then `M/K` is
    unramified over `Y`. This is the transitivity of unramifiedness.
1. Let `Y′` be a normal integral prescheme dominating `Y`, with field `K′/K`. If `L` is an extension of `K` unramified
    over `Y`, then `L ⊗_K K′` is an extension of `K′` unramified over `Y′`. This is the translation property.

<!-- original page 23 -->

Moreover:

**Corollary.**

<!-- label: I.10.5 -->

Under the conditions of (iii), if `Y = Spec(A)` and `Y′ = Spec(A′)`, then the normalization `Ā′` of `Y′` in
`L′ = L ⊗_K K′` identifies with `Ā ⊗_A A′`, where `Ā` is the normalization of `A` in `L`.

Usually, people, who are reluctant to consider nonintegral rings, even when they are direct products of fields, state
the translation property in the following weaker form:

**Corollary.**

<!-- label: I.10.6 -->

Under the conditions of (iii), let `L₁` be a compositum of `L/K`, unramified over `Y`, and `K′/K`. Then `L₁/K′` is
unramified over `Y′`. In the case where `Y = Spec(A)`, `Y′ = Spec(A′)`, one furthermore has

```text
Ā′ = A[Ā, A′],
```

i.e. the normalized ring `Ā′` of `A′` in `L₁` is the `A`-algebra generated by `A′` and the normalization `Ā` of `A` in
`L`.

This last fact is false without the unramifiedness hypothesis, even in the case of composita of number fields.

To finish this number, we shall give the interpretation of the notion of étale covering corresponding to the intuitive
image of that notion: there should be the "maximum number" of points over the point under consideration `y ∈ Y`, and in
particular there should not be "several points merged together" over `y`. To prove the results in this direction with
all desirable generality, we shall admit here Proposition I.10.7 below, whose proof will be in the multiplodocus,
Chapter IV, paragraph 15, and uses Chevalley's technique of constructible sets and a little descent theory.

A morphism of finite type `f: X → Y` is said to be universally open if for every base extension `Y′ → Y`, with `Y′`
locally noetherian, the morphism `f′: X′ = X ×_Y Y′ → Y′` is open, i.e. sends open sets to open sets. One may moreover
restrict to the case where `Y′` is of finite type over `Y`, and even where `Y′` is of the form `Y[t₁,...,t_r]`, with the
`t_i` indeterminates.

A universally open morphism is a fortiori open, the converse being false. On the other hand, if `f` is open, with `X`
and `Y` irreducible, then all components of all fibers of `f` have the same dimension, namely the dimension of the
generic fiber

<!-- original page 24 -->

`f⁻¹(z)`, where `z` is the generic point of `Y`. Finally, if `Y` is normal, this latter condition already implies that
`f` is universally open, by Chevalley's theorem. It follows, for example, that if `f: X → Y` is a quasi-finite morphism,
with `Y` normal and irreducible, then `f` is universally open, or simply open, if and only if every irreducible
component of `X` dominates `Y`. Recall also that a flat morphism of finite type, being open, is also universally open.
With these preliminaries in place, "recall":

**Proposition.**

<!-- label: I.10.7 -->

Let `f: X → Y` be a quasi-finite, separated, universally open morphism. For every `y ∈ Y`, let `n(y)` be the "geometric
number of points of the fiber `f⁻¹(y)`", equal to the sum of the separable degrees of the residue extensions
`κ(x)/κ(y)`, for `x ∈ f⁻¹(y)`. Then the function `y ↦ n(y)` on `Y` is upper semicontinuous. For it to be constant in a
neighborhood of the point `y`, i.e. for `n(y) = n(z_i)`, where the `z_i` are the generic points of the irreducible
components of `Y` containing `y`, it is necessary that there exist a neighborhood `U` of `y` such that `X|U` is finite
over `U`.[^I-10-1]

**Corollary.**

<!-- label: I.10.8 -->

If `y ↦ n(y)` is constant and `Y` is geometrically unibranch,[^I-10-2] then the irreducible components of `X` are
disjoint.

**Proposition.**

<!-- label: I.10.9 -->

Let `f: X → Y` be an étale separated morphism. With the notation of I.10.7, the function `y ↦ n(y)` is upper
semicontinuous. For it to be constant in a neighborhood of the point `y`, i.e. for `n(y) = n(z_i)`, where the `z_i` are
the generic points of the irreducible components of `Y` containing `y`, it is necessary and sufficient that there exist
an open neighborhood `U` of `y` such that `X|U` is finite over `U`, i.e. is an étale covering of `U`.

**Corollary.**

<!-- label: I.10.10 -->

For an étale separated morphism `f: X → Y`, with `Y` connected, to be finite, i.e. to make `X` an étale covering of `Y`,
it is necessary and sufficient that all fibers of `f` have the same geometric number of points.

In I.10.7 and its corollary, there was no normality hypothesis on `Y`. If one makes such a hypothesis, one finds the
stronger statement, most often taken as the definition of unramifiedness of a covering:

**Theorem.**

<!-- label: I.10.11 -->

<!-- original page 25 -->

Let `f: X → Y` be a quasi-finite separated morphism. Suppose that `Y` is irreducible, that every component of `X`
dominates `Y`, and that `X` is reduced, i.e. that `𝒪_X` has no nilpotent elements. Let `n` be the degree of `X` over
`Y`, the sum of the degrees over the field `K` of `Y` of the fields `K_i` of the irreducible components `X_i` of `X`.
Let `y` be a normal point of `Y`. Then the geometric number `n(y)` of points of `X` over `y` is `≤ n`, and equality
holds if and only if there exists an open neighborhood `U` of `y` such that `X|U` is an étale covering of `U`.

The "only if" being trivial, let us prove the "if". Let `z` be the generic point of `Y`. We have `n(z) =` the sum of the
separable degrees of the `K_i/K`, hence `n(z) ≤ n`; and by I.10.7 one has `n(y) ≤ n(z) ≤ n`, with equality implying that
`X|U` is finite over `U` for a suitable neighborhood `U` of `y`. One may therefore suppose `X` finite over `Y` and the
function `n(y′)` on `Y` constant. Finally, by I.10.8, `X` is then the disjoint union of its irreducible components, and
to prove that it is unramified at `y`, one is reduced to the case where `X` is irreducible, hence integral. Finally, one
may suppose `Y = Spec(𝒪_y)`. The theorem is then reduced to the following classical statement:

**Corollary.**

<!-- label: I.10.12 -->

Let `A` be a normal local ring, noetherian as always, with field `K`; let `L` be a finite extension of `K` of degree
`n`, with separable degree `n_s`; let `B` be a subring of `L` finite over `A`, with field of fractions `L`; let `𝔪` be
the maximal ideal of `A`, and let `n′` be the separable degree of `B/𝔪B` over `A/𝔪A = k`, i.e. the sum of the separable
degrees of the residue extensions of this ring. One has `n′ ≤ n_s` and a fortiori `n′ ≤ n`. This last inequality is an
equality if and only if `B` is unramified, hence étale, over `A`.

It remains only to show that `n′ = n` implies that `B` is étale over `A`. Recall the proof when `k` is infinite: one
need only show that `R = B/𝔪B` is separable over `k`. If this were not the case, it would follow, by a known lemma, that
there exists an element `a` of `R` whose minimal polynomial over `k` has degree `> n′`. This element comes from an
element `x` of `B`, whose minimal polynomial over `K`, as an element of `L`, has degree `≤ n`. On the other hand, this
latter polynomial has its coefficients in `A` since `A` is normal, and therefore gives by reduction mod `𝔪` a monic
polynomial `F ∈ k[t]`, of degree `≤ n = n′`, such that `F(a) = 0`, a contradiction.

<!-- original page 26 -->

In the general case, where `k` may be finite, returning to geometric language, consider `Y′ = Spec(A[t])`, which is
faithfully flat over `Y`, and the generic point `y′` of the fiber `Spec(k[t])` of `Y′` over `y`. Then `X` is net over
`Y` at `y` if and only if `X′ = X ×_Y Y′ = Spec(B[t])` is net at `y′` over `Y′`, as one checks immediately. On the other
hand, by the choice of `y′`, its residue field is `k(t)`, hence infinite. Since `y′` is a normal point of `Y′`, one is
reduced to the preceding case.

## 11. Some Complements

<!-- label: I.11 -->

We have already said that a connected étale covering of an integral scheme is not necessarily integral. Here are two
examples of this fact.

**a)** Let `C` be an algebraic curve with an ordinary double point `x`, let `C′` be its normalization, and let `a` and
`b` be the two points of `C′` above `x`. Let `C′_i`, for `i = 1, 2`, be two copies of `C′`, and let `a_i` and `b_i` be
the points of `C′_i` corresponding to `a` and `b` respectively. In the sum curve `C′₁ ⨿ C′₂`, identify `a₁` with `b₂` on
the one hand, and `a₂` with `b₁` on the other. We leave to the reader the task of making this identification process
precise; it will be explained in Chapter VI of the multiplodocus, but in the case of curves over an algebraically closed
field it is treated in Serre's book on algebraic curves.

One obtains a connected and reducible curve `C″`, which is an étale covering of degree 2 of `C`. The reader will verify
that, in general, the connected "Galois" étale coverings `C″` of `C` whose inverse image `C″ ×_C C′` is a trivial
covering of `C′`, i.e. isomorphic to the sum of a certain number of copies of `C′`, are "cyclic" of degree `n`; and for
every integer `n > 0`, one can construct a connected cyclic étale covering of degree `n`. In the language of the
fundamental group to be developed later, this means that the quotient of `π₁(C)` by the closed normal subgroup generated
by the image of `π₁(C′) → π₁(C)`, the homomorphism induced by the projection, is isomorphic to the profinite completion
of `ℤ`. More precisely, one should be able to show that the fundamental group of `C` is isomorphic to the topological
free product of the fundamental group of `C′` with the profinite completion of `ℤ`. Note that questions of this kind
gave rise to descent theory for schemes.

**b)** Let `A` be a complete integral local ring. One knows that its normalization `A′` is finite over `A`, by Nagata;
hence it is a complete semilocal ring, and therefore local since it is integral. Suppose that the residue extension
`L/k` it defines is not radicial. Otherwise, one will say that `A` is geometrically unibranch; cf. below. This will be
the case, for example, for the ring

```text
ℝ[[s,t]]/(s²+t²)ℝ[[s,t]],
```

where `ℝ` is the field of real numbers.

Let `k′` be a finite Galois extension of `k` such that `L ⊗_k k′` decomposes, and let `B` be a finite étale algebra over
`A` corresponding to the residue extension `k′`; recall that `B` is essentially unique. Then `B′ = A′ ⊗_A B` over `B`
has residue algebra `L ⊗_k k′`, which is not local; hence `B′` is not a local ring, and therefore, being complete, has
zero divisors.

<!-- original page 27 -->

Since `B′` is contained in the total ring of fractions of `B`, because it is free over `A′`, hence torsion-free over
`A′`, hence torsion-free over `A`, and therefore contained in

```text
B′ ⊗_A K = B′_(K) = A′_(K) ⊗_K B_(K) = B_(K),
```

since `A′_(K) = K`, it follows that `B` is not integral. In the case of the ring `ℝ[[s,t]]/(s²+t²)ℝ[[s,t]]`, taking
`k′/k = ℂ/ℝ`, one obtains for `B` the local ring of two intersecting lines in the plane at their point of intersection.

Note moreover that if there exists a connected étale covering `X` of an integral `Y` that is not irreducible, then every
irreducible component of `X` gives an example of an unramified covering `X′` of `Y`, dominating `Y`, that is not étale
over `Y`. In the case of example a), one obtains in this way that `C′` is unramified over `C` without being étale at the
two points `a` and `b`. This is also seen directly by inspecting the completions of the local rings of `x` and `a`: from
the "formal" point of view, `C′` at the point `a` identifies with a closed subscheme of `C` at the point `x`, namely one
of the two "branches" of `C` passing through `x`.

In a) and b), one sees that the failure of the conclusions of I.9.5(i) and (ii) is directly linked to the fact that a
point of `Y` "bursts" into distinct points of the normalization. In b), the fact that the residue extension is not
radicial must be interpreted geometrically in this way.

More precisely, we shall say that an integral local ring `A` is geometrically unibranch if its normalization has only
one maximal ideal, the corresponding residue extension being radicial. A point `y` of an integral prescheme is said to
be geometrically unibranch if its local ring is. Examples: a normal point, an ordinary cusp of a curve, etc.

<!-- original page 28 -->

It seems that if `Y` has a point that is not unibranch, there always exists a connected nonirreducible étale covering of
`Y`; at least this is what we showed in case b), when `Y` is the spectrum of a complete local ring. By contrast, one can
show that if all points of `Y` are geometrically unibranch, then every connected unramified `Y`-prescheme dominating `Y`
is étale and irreducible. The proof repeats that of I.9.5, using the following generalization of Theorem I.8.3, which
will be proved later using descent theory:[^I-11-1]

Let `Y′ → Y` be a finite, radicial, surjective morphism, i.e. what one might call a "universal homeomorphism". Consider
the functor `X ↦ X ×_Y Y′ = X′` from `Y`-preschemes to `Y′`-preschemes. This functor induces an equivalence from the
category of étale `Y`-schemes to the category of étale `Y′`-schemes.

One may apply this result, for example, in the case where `Y′` is the normalization of `Y`, with `Y` assumed unibranch
and `Y′` finite over `Y`, which is true in all cases one encounters in practice; or in the case of a `Y″` "sandwiched"
between `Y` and its normalization, which no longer needs to be finite over `Y`.

<!-- end of Exposé I source block: next chapter begins at smf_doc-math_3_01.tex line 2519 -->

[^I-1-1]: Cf. EGA IV 16.3.

[^I-2-1]: In EGA II 6.2.3 one assumes in addition that `f` is of finite type.

[^I-3-1]: Cf. remorse in III 1.2.

[^I-4-1]: Cf. Exposé IV.

[^I-4-2]: Cf. remorse in III 1.2.

[^I-5-1]: Cf. IV 5.9.

[^I-9-1]: Cf. EGA IV 5.8.6.

[^I-10-1]: Cf. EGA IV 15.5.1.

[^I-10-2]: For the definition, cf. below no. I.11.

[^I-11-1]: Cf. IX 4.10. For a more direct proof, cf. EGA IV 18.10.3, using a variant of I.9.5 for geometrically
    unibranch local rings.
