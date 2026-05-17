# Exposé III. Smooth Morphisms: Extension Properties

<!-- label: III -->

<!-- original page 58 -->

## 1. Formally Smooth Homomorphisms

<!-- label: III.1 -->

In II, we limited ourselves to homomorphisms of finite type and, consequently, in local homomorphisms `A → B` of local
rings, to the case where B is isomorphic to a localization of an A-algebra of finite type. This case is insufficient for
various applications, notably in formal geometry or analytic geometry. For example, the formal power-series ring
`B = A[[t₁,...,t_n]]` has, from the point of view of formal geometry, the properties of a smooth algebra over A. In
analytic geometry, the same is true of the local ring of a point (y,z) of a product `Y × ℂⁿ`, regarded as an algebra
over the local ring of y; moreover, the completion of this algebra is isomorphic to the algebra of formal power series
in n indeterminates over the completion of the base ring `𝒪_x`. This leads to the following definition.

**Definition.**

<!-- label: III.1.1 -->

Let `u: A → B` be a local homomorphism of local rings, noetherian as recalled. Suppose that `κ(B)` is finite over
`κ(A)`. We say that u is a **formally smooth homomorphism**, or that the algebra B is **formally smooth over** A, if
there exists a local finite `Ā`-algebra `A′`, free over `Ā`, such that the local components of the semi-local ring
`B̄ ⊗_{Ā} A′ = B′` are `A′`-isomorphic to algebras of formal power series over `A′`.[^iii-1-1-1]

Here `Ā` and `B̄` denote the completions of A and B. Since `B′` is finite and free over `B̄`, it is indeed a semi-local
ring, a direct sum of complete local rings, each of which is still a free module over `B̄`, hence has the same dimension
as `B̄`, and therefore as B. It follows that the number of variables `t_i` in the formal power-series rings considered
in III.1.1 is equal to `dim B̄ − dim Ā = dim B − dim A`, and in particular is independent of the local component
chosen. One sees at once that it is also the dimension of the ring `B ⊗ k = B/𝔪B`, where `k = A/𝔪` is the residue field
of A; we shall call it the **relative dimension of** B **with respect to** A.

<!-- original page 59 -->

**Remarks.**

<!-- label: III.1.2 -->

It is clear that Definition III.1.1 depends only on the homomorphism on completions `Ā → B̄` deduced from `A → B`,
which justifies the terminology to some extent. We repent here of Definitions I.3.2 b) and I.4.1 b), which risk being
misleading, and prefer to say “formally unramified” and “formally étale” in the cases considered in those definitions,
reserving the terminology “unramified” and “étale” for the case where B is a localization of an A-algebra of finite
type.[^iii-1-2-1] The reader will immediately verify that “formally étale” is equivalent to “formally smooth and
quasi-finite”. Finally, let us point out that there is a reasonable definition of “formally smooth” without any prior
hypothesis on the residual extension `κ(B)/κ(A)`, supposed finite here, encompassing among others the local
homomorphisms `A → B` such that B is **flat** over A and `B/𝔪B` is a **separable extension** of `A/𝔪 = k`, not
necessarily of finite type. For example, a Cohen p-ring is formally smooth over the ring of p-adic integers. It is the
lifting property for homomorphisms, compare III.2.1, that should become the definition in this general case. For the
applications we have in view, the case treated in Definition III.1.1 will suffice; in what follows, in “formally smooth”
we shall understand “with finite residual extension”.

**Lemma.**

<!-- label: III.1.3 -->

If B is formally smooth over A, then B is flat over A.

Since flatness is invariant under completion, we may suppose A and B complete. Since flatness is invariant under a local
flat, hence faithfully flat, extension of the base ring, Definition III.1.1 reduces us to the case where B is a formal
power-series algebra over A. But then, as an A-module, B is isomorphic to a product of A-modules isomorphic to A; hence,
since the base ring A is noetherian, B is A-flat as a product of flat A-modules.

Let us place ourselves under the conditions of III.1.1. Since the residual extensions of the local components of `B′`
over `A′` are trivial, it follows that `L ⊗_k k′` is an artinian `k′`-algebra whose local components have trivial
residual extensions, where L, k, `k′` are the residue fields of A, B, and `A′`. This necessary condition for the finite
free extension `A′` to satisfy the condition stated in III.1.1 is also sufficient, as follows at once from III.1.4 (i)
and III.1.5 below.

<!-- original page 60 -->

**Proposition.**

<!-- label: III.1.4 -->

Let `A → B` be a local homomorphism of local rings with finite residual extension, and let `A′` be a finite local
A-algebra over A, so that `B′ = B ⊗_A A′` is finite over B and hence is a semi-local ring, also noetherian.

1. If B is formally smooth over A, then the localizations of `B′` at its maximal ideals are formally smooth over `A′`.
1. The converse is true if `A′` is free over A.

We are immediately reduced to the case where A and B are complete.

For (i), let `A″` be a finite free local extension of A such that the local components of `B″ = B ⊗_A A″` are formal
power-series algebras over `A″`. Extending scalars `A″ → A″ ⊗_A A′ → A‴`, where `A‴` is a local component of
`A″ ⊗_A A′`, one sees that the local components of `B″ ⊗_{A″} A‴ = B ⊗_A A‴` are formal power-series algebras over `A‴`.
But we also have

```text
B ⊗_A A‴ = (B ⊗_A A′) ⊗_{A′} A‴ = B′ ⊗_{A′} A‴.
```

Moreover, since `A″` is free over A, `A″ ⊗_A A′` is free over `A′`, and consequently so is `A‴`, which is a direct
factor of it. This proves that `B′` is formally smooth over `A′`.

For (ii), let `A″` be a finite free local `A′`-algebra such that the local components of `B′ ⊗_{A′} A″ = B ⊗_A A″` are
formal power-series algebras over `A″`. Since `A′` is free over A, so is `A″`; hence B is formally **smooth** over A.

**Proposition.**

<!-- label: III.1.5 -->

Let `A → B` be a local homomorphism of local rings with **trivial** residual extension. In order that B be formally
smooth over A, it is necessary and sufficient that `B̄` be isomorphic to a formal power-series algebra over `Ā`.

Only the necessity has to be proved, and we may suppose A and B complete. Let `𝔪` and `𝔫` be the maximal ideals of A and
B, respectively, and let `t₁,...,t_n` be elements of `𝔫` defining a basis of the vector space

```text
(𝔫/𝔫²)/Im(𝔪/𝔪²) = 𝔫/(𝔫² + 𝔪B).
```

These elements therefore define a homomorphism of local A-algebras

```text
B₁ = A[[t₁,...,t_n]] → B.
```

We prove that it is an isomorphism. It suffices to prove that for every power `𝔪^q` of `𝔪`, one obtains an isomorphism
after reducing modulo `𝔪^q`, since `B₁` and B are the projective limits of the corresponding rings reduced modulo `𝔪^q`,
with q variable. Since B and `B₁` are flat A-modules, the graded rings associated with the `𝔪`-adic filtration are
obtained by tensoring over `k = A/𝔪` with `gr(A)` the rings `B₁/𝔪B₁` and `B/𝔪B`, respectively. We are thus reduced to
showing that `B₁/𝔪B₁ → B/𝔪B` is an isomorphism. Taking III.1.3 into account, we are thereby reduced to the case where A
is a **field** k. On the other hand, if `A′` is a finite free local A-algebra such that `B ⊗_A A′` is a formal
power-series algebra over `A′`, note that this algebra is local since the residual extension of B over A is trivial. To
prove that `B₁ → B` is an isomorphism, it suffices to prove that `B₁ ⊗_A A′ → B ⊗_A A′` is one. This reduces us to the
case where B is already a formal power-series algebra; this reduction should have been made first, before reducing to
the case of a base field. But then B is a regular local ring with coefficient field k, and it is well known, and
immediate by considering the graded rings associated with the `𝔫₁`-adic and `𝔫`-adic filtrations on `B₁` and B, that
`B₁ → B` is an isomorphism. This completes the proof.

**Corollary.**

<!-- label: III.1.6 -->

If B is formally smooth over A, then there exists a finite local A-algebra `A′` such that the local components of

```text
B̄ ⊗_{Ā} A′̄ = completion of (B ⊗_A A′)
```

are isomorphic to formal power-series algebras over `A′̄`.

Indeed, if L/k is the residual extension of B/A, consider an extension `k′/k` such that the residual extensions in the
`k′`-algebra `L ⊗_k k′` are trivial. Let `A′` be an algebra finite and free over A such that `A′/𝔪A′ = k′`; one knows
that such an algebra exists, for example by reducing step by step to the case where `k′/k` is monogenic, and then
lifting to A the coefficients of the minimal polynomial of a generator of `k′` over k. It is local. Then `B ⊗_A A′` has,
at its maximal ideals, trivial residual extensions over that `k′` of `A′`, and the conclusion follows with the help of
III.1.5.

**Corollary.**

<!-- label: III.1.7 -->

Let `A → B` be a local homomorphism of local rings. In order that B be formally smooth over A, it is necessary and
sufficient that B be flat over A and that `B/𝔪B` be formally smooth over `k = A/𝔪`.

Making a suitable finite free local extension `A′` of A and using III.1.4 (ii), we are reduced to the case where the
residual extension of B/A is trivial. We know moreover by III.1.4 (i) and III.1.3 that the stated conditions are
necessary. For the sufficiency, it suffices to observe that the proof of III.1.5 proves, under the hypotheses made here,
that B is a formal power-series algebra over A, supposing A and B complete, which is permissible.

<!-- original page 62 -->

**Remark.**

<!-- label: III.1.8 -->

It would not be difficult to develop, for formally smooth homomorphisms, the analogue of all the properties of smooth
morphisms studied in II. For the differential properties, however, this requires a modification of the usual definition
of Kähler differentials, cf. I.1, with completed tensor products replacing ordinary tensor products. We shall content
ourselves with evoking these abysses here, what precedes being sufficient for our purpose.

It remains to make the link between formal smoothness and the notion of smoothness developed in II, which we have not
yet used at all.

**Proposition.**

<!-- label: III.1.9 -->

Let `A → B` be a local homomorphism, with B a localization of an A-algebra of finite type. In order that B be smooth
over A, it is necessary and sufficient that it be formally smooth over A.

Using III.1.7 and II.2.1, we are reduced to the case where A is a field.

Using III.1.4 (ii) and II.4.13, a suitable extension `k′` of k reduces us to the case where the residual extension for
B/k is trivial. By III.1.5, respectively II.5.2, B is smooth over k, respectively formally **smooth over** k, if and
only if B is a regular local ring, respectively its completion is a formal power-series algebra over k. But it is well
known that these two conditions are equivalent when the residual extension is trivial.

## 2. The Lifting Property Characteristic of Formally Smooth Homomorphisms

<!-- label: III.2 -->

**Theorem.**

<!-- label: III.2.1 -->

Let `A → B` be a local homomorphism of local rings defining a finite residual extension. The following conditions are
equivalent:

1. B is formally smooth over A.
1. For every local homomorphism `A → C`, where C is a **complete** local ring, every ideal J of C contained in the
    radical `𝔯(C)`, and every local A-homomorphism `B → C/J`, there exists an A-homomorphism, necessarily local,
    `B → C` lifting it.
1. For every A-algebra C, not necessarily noetherian, every nilpotent ideal J of C, and every continuous A-homomorphism
    `B → C/J`, i.e. one vanishing on a power of `𝔯(B)`, there exists an A-homomorphism `B → C`, necessarily continuous
    as well, lifting it.
1. The same statement as (ii) and (iii), but with C a local artinian ring finite over A.
1. As in (iv), but with J moreover square-zero.

**Remark.** For the rest of this exposé, we shall use only the implication (iv) ⇒ (i), or (iv bis) ⇒ (i). The direct
implication (i) ⇒ (ii) will be proved by another method in the next number when B is a localization of an algebra of
finite type over A. Recall that in the “good” theory of Cohen theorems,[^iii-2-1-1] property (ii) or (iii) becomes the
definition of formally smooth homomorphisms, while III.1.1 becomes a characteristic property valid only in the case of a
finite residual extension. Care should be taken that neither of properties (ii) and (iii) is more general than the
other. One could give an equivalent property covering both by introducing a linearly topologized ring C, **separated**
and **complete**, a **closed topologically nilpotent** ideal of C, and a continuous homomorphism `A → C`, thus making C
a topological A-algebra; we leave this modification to the reader.

**Proof of III.2.1.** We shall prove (i) ⇒ (iii) ⇒ (ii), then (iv) ⇒ (i). Since (ii) ⇒ (iv) is trivial, and the
equivalence of (iv) and (iv bis) is seen by an immediate induction on the integer n such that `Jⁿ = 0`, this will finish
the proof.

(i) ⇒ (iii). An immediate induction reduces us to the case J² = 0. Since C is finite over A, some power `𝔪^q` of the
maximal ideal of A annihilates C. Dividing by `𝔪^q`, and noting that `B/𝔪^qB` is still formally smooth over `A/𝔪^q` by
III.1.4 (i), we may suppose A artinian. Since B is flat over A by III.1.3, B **is free over** A because A is artinian.
Thus there exists an **A-module homomorphism**

```text
w: B → C
```

lifting the given homomorphism `u: B → C/J`. Put

```text
f(x,y) = w(xy) − w(x)w(y),     x,y ∈ B.
```

Then f(x,y) ∈ J, and f is therefore an A-bilinear map from `B × B` to J. For there to exist a lift `v: B → C` of u that
is an algebra homomorphism, it is necessary and sufficient that there exist an A-linear map `g: B → J` such that
`v = w + g` is an algebra homomorphism, which is written

```text
g(1) = 1 − w(1),
g(xy) − u(x)g(y) − u(y)g(x) = −f(x,y),     x,y ∈ B.
```

This is a system of **linear** equations in `Hom_A(B,J)`, with right-hand sides in J. Hence it has a solution if and
only if the corresponding system in `Hom_A(B,J) ⊗_A A′`, with right-hand sides in `J′ = J ⊗_A A′`, has a solution, where
`A′` denotes a faithfully flat algebra over A. Let `A′` be an algebra finite and free over A, local, such that
`B′ = B ⊗_A A′` is a formal power-series algebra over `A′`. In our proof we may suppose A and B complete, as is
immediately checked. Since `A′` is free of finite type over A, we have

```text
Hom_A(B,J) ⊗_A A′ = Hom_{A′}(B′,J′),
```

and one verifies that the system of equations obtained in `Hom_{A′}(B′,J′)` is the one that determines the homomorphisms
of `A′`-algebras `B′ → C′ = C ⊗_A A′` lifting the homomorphism `u′: B′ → C′/J′` deduced from u by extension of scalars,
by “correcting” by an `A′`-module homomorphism `g′: B′ → J′` the `A′`-module homomorphism `w′: B′ → C′` deduced from w
by extension of scalars. Note that B generates `B′` as an `A′`-module. We are thereby reduced to proving (iii) when B is
a **formal power-series algebra** over A, `B = A[[t₁,...,t_n]]`. Lift arbitrarily the images in C/J of the `t_i` to
elements `z_i` of C. Since the `z_i` modulo J are nilpotent, `u: B → C/J` being continuous, the `z_i` themselves are
nilpotent, since J is nilpotent. Thus the `z_i` define a continuous homomorphism of topological A-algebras from B to the
discrete ring C, evidently lifting u, as required.

(iii) ⇒ (ii). Let `𝔫` be the maximal ideal of C, and for every integer q > 0 put

```text
C_q = C/𝔫^q,    J_q = (J + 𝔫^q)/𝔫^q.
```

Thus `C_q/J_q` identifies with a quotient algebra of C/J. On the other hand, the composite homomorphism
`u_q: B → C/J → C_q/J_q` is continuous from B to the discrete ring `C_q/J_q`, and `J_q` is a nilpotent ideal in `C_q`.
We then construct, step by step, A-homomorphisms

```text
v_q: B → C_q
```

such that (a) `v_q` lifts `u_q` and (b) `v_q` lifts `v_{q−1}`. The possibility of the induction is checked easily: since

```text
u_q: B → C/(J + 𝔫^q)     and     v_{q−1}: B → C/𝔫^{q−1}
```

define the same homomorphism

```text
B → C/((J + 𝔫^q) + 𝔫^{q−1}) = C/(J + 𝔫^{q−1}) = C_{q−1}/J_{q−1},
```

namely `u_{q−1}`, they define a homomorphism

```text
B → C/J′_q,    where J′_q = (J + 𝔫^q) ∩ 𝔫^{q−1} ⊃ 𝔫^q,
```

from which both arise by reduction. We are therefore reduced to lifting a homomorphism `B → C/J′_q` from B into a
quotient of `C_q` by an ideal `J′_q/𝔫^q` contained in `J_q`, hence nilpotent; this is possible by hypothesis (iii).

This done, the `v_q` define a homomorphism from B into the projective limit C of the `C_q`. Since J is closed, J is the
projective limit of the `J_q`; hence v lifts u, as required.

(iv) ⇒ (i). First one observes at once that if (iv) holds, then (iv) remains true for the local components of `B ⊗_A A′`
over `A′`, if `A′` is a finite local algebra over A. Taking `A′` free over A and such that the residual extensions of
`B′` over `A′` are trivial, we are reduced, by III.1.4 (ii), to the case where the residual extension of B over A is
trivial. We shall then prove the slightly more precise result:

**Corollary.**

<!-- label: III.2.2 -->

Under the conditions of III.2.1, suppose moreover that the residual extension of B over A is trivial. Then the
equivalent conditions of III.2.1 are also equivalent to the following two conditions, supposing in (v) that A and B are
complete:

1. As in (iv), but with the local artinian ring C finite over A restricted to have trivial residual extension; and
    moreover, if one wants, with the ideal J square-zero.
1. There exists a local A-homomorphism, where `n = dim 𝔫/(𝔫² + 𝔪B)`,

```text
u: B → B₁ = A[[t₁,...,t_n]]
```

inducing an **isomorphism**

```text
𝔫/(𝔫² + 𝔪B) → 𝔫₁/(𝔫₁² + 𝔪B₁),
```

where `𝔫` and `𝔫₁` are the maximal ideals of B and `B₁`, respectively, and `𝔪` is that of A.

**Proof.** Since (iv bis) evidently implies (iv ter), setting aside the square-zero-ideal joke, it will suffice to prove
(iv ter) ⇒ `(v) ⇒ (i)`.

For (iv ter) ⇒ (v), choose a basis `a₁,...,a_n` of `𝔫/(𝔫² + 𝔪B)`. This therefore defines a local homomorphism of
A-algebras

```text
B → B₁/(𝔫₁² + 𝔪B₁) = k[t₁,...,t_n]/(t₁,...,t_n)²,
```

which can be lifted step by step, by (iv ter), to homomorphisms of A-algebras from B into `B₁/𝔫₁²`, `B₁/𝔫₁³`, and so on;
passing to the projective limit gives the homomorphism `B → B₁` with the desired property.

For `(v) ⇒ (i)`, in the commutative diagram

```text
𝔪/𝔪² → 𝔫/𝔫² → 𝔫/(𝔫² + 𝔪B) → 0
↓       ↓       ↓
𝔪/𝔪² → 𝔫₁/𝔫₁² → 𝔫₁/(𝔫₁² + 𝔪B₁) → 0
```

the two rows are exact, and the extreme vertical arrows are surjective; the middle arrow is therefore surjective, and it
follows, since B is complete, that `B → B₁` is **surjective**. Let `x_i`, `1 ≤ i ≤ n`, be elements of B lifting the
`t_i`. They define a homomorphism of A-algebras `B₁ → B`, which is surjective for the same reason as u, and whose
composite with u is the identity by construction. Thus `B₁ → B` is also injective, and consequently is an isomorphism.
We obtain:

**Corollary.**

<!-- label: III.2.3 -->

Under the conditions of III.2.2 (v), u is necessarily an isomorphism.

This finishes the proof that B is formally smooth over A. At the same time we have recovered III.1.5, though there is
little merit in that.

## 3. Local Infinitesimal Extension of Morphisms into a Smooth S-Scheme

<!-- label: III.3 -->

**Theorem.**

<!-- label: III.3.1 -->

Let `f: X → Y` be a morphism locally of finite type. The following conditions are equivalent:

1. f is smooth.
1. For every prescheme `Y′` over Y, every closed sub-prescheme `Y′₀` of `Y′` having the same underlying space as `Y′`,
    every Y-morphism `g₀: Y′₀ → X`, and every `z ∈ Y′₀`, there exists an open neighborhood U of z in `Y′` and an
    extension g of `g₀|_{Y′₀ ∩ U}` to a Y-morphism `U → X`.
1. For `Y′`, `Y′₀`, and z as in (ii), putting `X′ = X ×_Y Y′` and `X′₀ = X ×_Y Y′₀`, every section of `X′₀` over `Y′₀`
    extends to a section of `X′` over an open neighborhood U of z.
1. For every Y-scheme `Y′` that is the spectrum of a local artinian ring finite over some `𝒪_y`, with `y ∈ Y`, every
    nonempty closed sub-prescheme `Y′₀` of `Y′`, and every Y-morphism `g₀: Y′₀ → X`, there exists a Y-morphism
    `g: Y′ → X` extending `g₀`.
1. For every `Y′` and `Y′₀` as in (iii), putting `X′ = X ×_Y Y′` and `X′₀ = X ×_Y Y′₀`, every section of `X′₀` over
    `Y′₀` extends to a section of `X′` over `Y′`.

**Proof.** The equivalence of (ii) and (ii bis), on the one hand, and of (iii) and (iii bis), on the other, is trivial,
as is the implication (ii) ⇒ (iii). It remains to prove (i) ⇒ (ii) and (iii) ⇒ (i).

(i) ⇒ (ii). Let `x = g₀(z)`. Replacing X by a suitable open neighborhood of x, and `Y′` by the prescheme induced on the
open inverse image of the latter under `g₀`, we may suppose that X is étale over `Y[t₁,...,t_n]`. Consider the composite
Y-morphism `Y′₀ → X → Y[t₁,...,t_n]`; it is defined by n sections of the sheaf `𝒪_{Y′₀}`, which can therefore be
extended in a neighborhood of z to sections of `𝒪_{Y′}`. Thus we may suppose that the morphism in question has been
extended to a Y-morphism `Y′ → Y[t₁,...,t_n]`. By I.5.6, there is then a unique Y-morphism `g: Y′ → X` lifting the
preceding one and at the same time extending `g₀`.

<!-- original page 68 -->

(iii) ⇒ (i). Since the set of points where f is smooth is open, it suffices to prove that it contains every `x ∈ X` that
is **closed** in its fiber. Let y = f(x). Then `𝒪_x` is an algebra over `𝒪_y`, a localization of an algebra of finite
type, with finite residual extension. On the other hand, hypothesis (iii) implies that every homomorphism from `𝒪_x`
into an algebra A/J, where A is a local artinian algebra finite over `𝒪_y` and J is an ideal contained in its radical,
lifts to a homomorphism from `𝒪_x` into the algebra A, taking into account that a morphism from `Spec(B)`, with B local,
into X is determined bijectively by a local homomorphism from some `𝒪_x`, `x ∈ X`, into B. By III.2.1 it follows that
`𝒪_x` is formally smooth over `𝒪_y`, hence smooth over `𝒪_y` by III.1.9.

**Corollary.**

<!-- label: III.3.2 -->

Let `f: X → Y` be as in III.3.1. The following conditions are equivalent:

1. f is étale.
1. Condition (ii) of III.3.1 holds with **uniqueness** of the extension g of `g₀` to U.
1. Condition (iii) of III.3.1 holds with **uniqueness** of g.

It suffices to note, in the proof of (i) ⇒ (ii) above, that one can have uniqueness, when `Y′₀` is not identical to `Y′`
in a neighborhood of z, only if `n = 0`, a condition that is known to be sufficient.

**Corollary.**

<!-- label: III.3.3 -->

Let X be a prescheme locally of finite type over a **complete** local ring A, let y be the closed point of
`Y = Spec(A)`, and let x be a point of `f⁻¹(y)` **rational** over `κ(y)`. If X is **smooth over A at x**, then there
exists a section s of X over Y “passing through x”, i.e. such that s(y) = x.

In particular, if X is smooth over A, then the natural map

```text
Γ(X/Y) → Γ(X ⊗_A k / k)
```

from sections of X over Y to the set of points of the fiber `f⁻¹(y) = X ⊗_A k` rational over k is surjective. This fact
was especially well known and used when A is a discrete valuation ring and X is proper over A, in fact projective over
A. In that case the sections of X over Y, i.e. the “points of X with values in A”, also identify with the rational
sections, i.e. with the points of `X ⊗_A K = X_K`, which is a proper smooth scheme over K, with values in K, the field
of fractions of A; in other words, with the points of X rational over K.

## 4. Local Infinitesimal Extension of Smooth S-Schemes

<!-- label: III.4 -->

**Theorem.**

<!-- label: III.4.1 -->

Let Y be a locally noetherian prescheme, let `Y₀` be a closed sub-prescheme with the same underlying space, let `X₀` be
a smooth `Y₀`-prescheme, and let x be a point of `X₀`. Then there exist an open neighborhood `U₀` of x, a prescheme X
smooth over Y, and a `Y₀`-isomorphism

```text
h: U₀ → X ×_Y Y₀.
```

Moreover, if `(U′₀`, `X′`, `h′)` is another solution of this problem, then “it is isomorphic to the first in a
neighborhood of x”.

We leave it to the reader to make precise what is meant by this. One may note that, for `U₀` given, a solution of the
stated problem amounts to giving on `U₀` a sheaf of algebras `ℬ` over `f₀⁻¹(𝒪_Y)`, where `f₀` is the continuous map
underlying the structural morphism `U₀ → Y₀`, together with a homomorphism of rings `ℬ → 𝒪_{U₀}` compatible with the
homomorphism `f⁻¹(𝒪_Y) → f⁻¹(𝒪_{Y₀})`, such that:

1. This homomorphism induces an isomorphism

```text
ℬ ⊗_{f⁻¹(𝒪_Y)} f⁻¹(𝒪_{Y₀}) → 𝒪_{Y₀}.
```

1. `U₀` equipped with `ℬ` becomes a smooth Y-prescheme.

In this way the precise meaning of the assertion of local uniqueness becomes particularly evident.

**Proof.** We may already suppose that `X₀` is étale over some `Y₀[t₁,...,t_n] = Y′₀`. But the latter may be regarded as
a closed sub-prescheme of `Y′ = Y[t₁,...,t_n]` having the same underlying space. By I.8.3, there exists an X étale over
`Y′` and a `Y′₀`-isomorphism `X ×_{Y′} Y′₀ → X′`. We have won existence. For uniqueness, use property III.3.1 (ii) of
smooth morphisms, taking into account the following lemma.

<!-- original page 70 -->

**Lemma.**

<!-- label: III.4.2 -->

Let Y be a prescheme, let `Y₀` be a closed sub-prescheme defined by a locally nilpotent sheaf of ideals `𝒥`, let X and
`X′` be Y-preschemes, and let `u: X → X′` be a Y-morphism. Suppose X is flat over Y. In order that u be an isomorphism,
it is necessary and sufficient that

```text
u₀: X ×_Y Y₀ → X′ ×_Y Y₀
```

be an isomorphism.

The proof is easy, by passing to the affine case and looking at associated graded rings. One should note moreover that
the analogous statement obtained by replacing “isomorphism” by “closed immersion” is also valid, and without the
flatness hypothesis.

**Remark.**

<!-- label: III.4.3 -->

It is essential to note that the local extension X obtained in III.4.1 **is not canonical**; in other words, the local
isomorphism between two solutions is not unique, i.e. in general there exist nontrivial Y-automorphisms of X inducing
the identity on the closed sub-prescheme `X₀ = X ×_Y Y₀`. This is why, for the construction of **global** infinitesimal
extensions of smooth preschemes, one must expect the existence of an obstruction of cohomological nature, which will be
made precise below in III.6.

## 5. Global Infinitesimal Extension of Morphisms

<!-- label: III.5 -->

Let T be a topological space, let `𝒢` be a sheaf of groups on X, and let `𝒫` be a sheaf of sets on T on which `𝒢` acts,
on the right to fix ideas. We say that `𝒫` is **formally principal homogeneous** under `𝒢` if the familiar homomorphism

```text
𝒢 × 𝒫 → 𝒫 × 𝒫
```

of sheaves of sets, deduced from the operations of `𝒢` on `𝒫`, is an **isomorphism**. This is equivalent to saying that
for every `x ∈ T`, `𝒫_x` is **empty or a principal homogeneous space** under the ordinary group `𝒢_x`; or also that for
every open U of T, `𝒫(U)` is empty or a principal homogeneous space under the ordinary group `𝒢(U)`. We say that `𝒫` is
a **principal homogeneous sheaf** under `𝒢` if it is so formally and if, in addition, the `𝒫_x` are nonempty; in other
words, if **all** the `𝒫_x` are principal homogeneous spaces, hence nonempty, under the `𝒢_x`.[^iii-5-0-1] Recall that
the set of classes, up to isomorphism, of principal homogeneous sheaves under `𝒢` identifies with the cohomology set
`H¹(T,𝒢)`, which is also the usual cohomology group of T with coefficients in `𝒢` when `𝒢` is commutative. Thus, for
every principal homogeneous `𝒫`, there is a characteristic class `c(𝒫) ∈ H¹(T,𝒢)`, whose triviality is necessary and
sufficient for `𝒫` to be trivial, i.e. isomorphic to `𝒢`, on which `𝒢` acts by right translations, or equivalently for
`𝒫` to have a section.

**Proposition.**

<!-- label: III.5.1 -->

Let S be a prescheme, let X and Y be preschemes over S, and let `Y₀` be a closed sub-prescheme of Y defined by an ideal
`𝒥` on Y **of square zero**. Let `g₀` be an S-morphism from `Y₀` to X, and let `𝒫(g₀)` be the sheaf on Y whose sections
on an open U are the extensions `g: U → X` of `g₀|_{U ∩ Y₀}` to an S-morphism g. Then `𝒫(g₀)` is, naturally, a
**formally principal homogeneous** sheaf under the commutative sheaf of groups

```text
𝒢 = Hom_{𝒪_{Y₀}}(g₀*(Ω¹_{X/S}), 𝒥).
```

Put `𝒫 = 𝒫(g₀)`. For every open U of Y we must define a map

```text
𝒫(U) × 𝒢(U) → 𝒫(U)
```

so that: for fixed `g ∈ 𝒫(U)`, the map s ↦ gs from `𝒢(U)` to `𝒫(U)` is bijective; `𝒫(U)` becomes a set with group of
operators `𝒢(U)`; and these maps are compatible with restriction operators for an open `V ⊂ U`. The verification of the
last point is trivial, so for simplicity we may suppose `U = Y`. The verification of the second point, which is local if
one wants, is left to the reader. We shall limit ourselves, for a given `g ∈ 𝒫(Y)`, to defining a natural bijection from
`𝒢(Y)` onto `𝒫(Y)`. Thus suppose already given an S-morphism `g: Y → X`, and seek a canonical bijection

```text
Hom_{𝒪_{Y₀}}(g₀*(Ω¹_{X/S}), 𝒥) → 𝒫(Y),
```

<!-- label: eq:III.5.1.* -->

where `𝒫(Y)` is the set of S-morphisms `g′` from Y to X inducing the same morphism `g₀: Y₀ → X` as g. Giving such a `g′`
is equivalent to giving an S-morphism `h: Y → X ×_S X` such that `pr₁ ∘ h = g` and `h ∘ i = (g₀,g₀)`, where
`pr₁: X ×_S X → X` is the first projection, `i: Y₀ → Y` is the canonical immersion, and `(g₀,g₀): Y₀ → X ×_S X` is the
morphism `Δ_{X/S} g₀` with components `g₀,g₀:`

```text
Y₀ --h₀=(g₀,g₀)--> X ×_S X
|                         |
i                         pr₁
v                         v
Y  --------g----------->  X
```

Since `h₀` factors through the diagonal immersion `Δ_{X/S}`, and since Y is in the first-order infinitesimal
neighborhood of `Y₀`, i.e. `𝒥² = 0`, the desired h necessarily factor, uniquely, through the first-order infinitesimal
neighborhood of the diagonal. This neighborhood identifies, as an X-prescheme via `pr₁`, with the spectrum `X′` of the
sheaf of algebras `𝒪_X + Ω¹_{X/S}`, where the second term is regarded as a square-zero ideal; the diagonal morphism
`X → X′` corresponds to the canonical augmentation of this sheaf of algebras. Put `Y′ = X′ ×_X Y` and
`Y′₀ = Y′ ×_Y Y₀ = X′ ×_X Y₀`. The desired h are then in bijective correspondence with sections u of `Y′` over Y
extending a given section `u₀` of `Y′₀` over `Y₀`. We may moreover identify `Y′` with the spectrum of the sheaf of
algebras on Y

```text
𝒜 = g*(𝒪_X + Ω¹_{X/S}) = 𝒪_Y + g*(Ω¹_{X/S}),
```

and `Y′₀` with the sheaf of algebras

```text
𝒜₀ = 𝒜 ⊗_{𝒪_Y} 𝒪_{Y₀} = 𝒪_{Y₀} + g₀*(Ω¹_{X/S}).
```

Then `u₀` is the section defined by the canonical augmentation of `𝒜₀` into `𝒪_{Y₀}`. Thus `𝒫(Y)` identifies with the
set of algebra homomorphisms `𝒜 → 𝒪_Y` inducing the canonical augmentation `𝒜₀ → 𝒪_{Y₀}`. But the algebra homomorphisms
`𝒜 → 𝒪_Y` correspond bijectively to module homomorphisms `𝓜 → 𝒪_Y`, putting for simplicity `𝓜 = g*(Ω¹_{X/S})`, and we
are interested in those inducing the **zero** homomorphism `𝓜₀ → 𝒪_{Y₀}`, where `𝓜₀ = 𝓜 ⊗_{𝒪_Y} 𝒪_{Y₀}`; that is, those
sending `𝓜` into the augmentation ideal `𝒥`. We therefore find the set

```text
Hom_{𝒪_Y}(𝓜,𝒥) = Hom_{𝒪_{Y₀}}(𝓜₀,𝒥),
```

since `𝒥` is annihilated by `𝒥`. This is the desired canonical bijection `III.5.1.*`.

Taking into account the implication (i) ⇒ (iii) in III.3.1, one obtains:

**Corollary.**

<!-- label: III.5.2 -->

<!-- original page 73 -->

If X is smooth over S, at least at the points of `g₀(Y₀)`, then `𝒫` is even a **principal homogeneous sheaf** under the
commutative sheaf of groups `𝒢`, which in this case may also be written

```text
𝒢 = g₀*(𝔤_{X/S}) ⊗_{𝒪_{Y₀}} 𝒥,
```

where `𝔤_{X/S}` is the sheaf on X dual to `Ω¹_{X/S}`, i.e. the **tangent sheaf**, or **sheaf of derivations**, of X
relative to S. This last formula comes from the fact that `Ω¹_{X/S}` is then free of finite type.

In particular, this principal homogeneous sheaf determines a cohomology class in `H¹(Y₀,𝒢)`, whose vanishing is
necessary and sufficient for the existence of an S-morphism g extending `g₀`. And if such an extension exists, the set
of all possible extensions is a homogeneous space under the group `H⁰(Y₀,𝒢)`.

In applying the methods of formal geometry, the situation is most often the following. We are given two S-preschemes X
and Y, and a coherent ideal `𝓘` on S. Let `S_n` denote the closed sub-prescheme of S defined by `𝓘^{n+1}`, and put

```text
X_n = X ×_S S_n,    Y_n = Y ×_S S_n.
```

Suppose we have an `S_n`-morphism

```text
g_n: Y_n → X_n
```

or, what amounts to the same thing, an S-morphism `Y_n → X`, or again an `S_{n+1}`-morphism `Y_n → X_{n+1}`, since such
a morphism necessarily induces `Y_n → X_n`. We seek to extend it to an `S_{n+1}`-morphism

```text
g_{n+1}: Y_{n+1} → X_{n+1}.
```

If this can be continued indefinitely, one obtains a morphism `Ŷ → X̂` for the formal preschemes obtained by completing
Y and X for the ideals `𝓘𝒪_Y` and `𝓘𝒪_X`. We may apply III.5.1 with `(S,X,Y,Y₀,g₀)` replaced by `(S_{n+1}`, `X_{n+1}`,
`Y_{n+1}`, `Y_n`, `g_n)`. The sheaf `𝒢` here becomes the sheaf of module homomorphisms from `g_n*(Ω¹_{X_{n+1}/S_{n+1}})`
into

```text
𝒥 = 𝓘^{n+1}𝒪_Y / 𝓘^{n+2}𝒪_Y.
```

Since `𝒥` is annihilated by `𝓘𝒪_Y`, we may then replace `g_n*(Ω¹_{X_{n+1}/S_{n+1}})` by the sheaf it induces on `Y₀`,
namely `h₀*(Ω¹_{X/S})`, where `h₀` is the composite `Y₀ → Y_n → X_{n+1}`, or again the composite `Y₀ → X₀ → X_{n+1}`,
where `g₀: Y₀ → X₀` is induced by `g_n`. Since the inverse image of `Ω¹_{X_{n+1}/S_{n+1}}` on
`X₀ = X_{n+1} ×_{S_{n+1}} S₀` is `Ω¹_{X₀/S₀}`, one sees that one also has

```text
𝒢 = Hom_{𝒪_{Y₀}}(g₀*(Ω¹_{X₀/S₀}), 𝓘^{n+1}𝒪_Y / 𝓘^{n+2}𝒪_Y).
```

Thus we obtain:

**Corollary.**

<!-- label: III.5.3 -->

Let S, X, Y, `𝓘`, and `g_n` be as above, and let `𝒫(g_n)` be the sheaf on Y whose sections on an open U are the
extensions `g_{n+1}` of `g_n` to an `S_{n+1}`-morphism `Y_{n+1} → X_{n+1}`. Then `𝒫(g_n)` is a formally principal
homogeneous sheaf under the sheaf of groups

```text
𝒢 = Hom_{𝒪_{Y₀}}(g₀*(Ω¹_{X₀/S₀}), gr^{n+1}_{𝓘𝒪_Y}(𝒪_Y)).
```

In particular:

**Corollary.**

<!-- label: III.5.4 -->

If moreover X is smooth over S, at least at the points of `g₀(Y₀)`, then `𝒫(g_n)` is even a principal homogeneous sheaf.
In particular, it defines an obstruction class in `H¹(Y₀,𝒢)`, whose vanishing is necessary and sufficient for the
existence of a global extension `g_{n+1}` of `g_n`. And if such an extension exists, the set of all global extensions is
a principal homogeneous space under `H⁰(Y₀,𝒢)`. Finally, in the case considered, the sheaf `𝒢` may also be written

```text
𝒢 = g₀*(𝔤_{X₀/S₀}) ⊗_{𝒪_{Y₀}} gr^{n+1}_{𝓘𝒪_Y}(𝒪_Y).
```

Proceeding step by step, one sees therefore that if all the `H¹(Y₀,𝒢_n)` vanish, where

```text
𝒢_n = g₀*(𝔤_{X₀/S₀}) ⊗ gr^n_{𝓘𝒪_Y}(𝒪_Y),
```

then, starting with an arbitrary `g_k`, one can extend it successively to `g_{k+1}`, and so on. In particular, if `𝓘` is
nilpotent, one will be able to find an extension g of `g_k` to Y. The vanishing condition for the H¹ is satisfied in
particular if `Y₀` is affine. Thus one obtains:

**Corollary.**

<!-- label: III.5.5 -->

<!-- original page 75 -->

In the statement of Theorem III.3.1, one obtains a necessary and sufficient condition equivalent to the others by
supposing that the `Y′` occurring in (ii), or (ii bis), is affine, and by requiring the existence of a **global
extension** g of `g₀` to all of `Y′`.

Note that the proof of III.3.1 could not have given this result directly.

An important case is that where Y is **flat** over S. Then one has

```text
gr^n(𝒪_Y) = gr^n(𝒪_S) ⊗_{𝒪_{S₀}} 𝒪_{Y₀},
```

and when, moreover, the `gr^n(𝒪_S)` are **locally free on** S, one finds

```text
𝒢_n = Hom_{𝒪_{Y₀}}(g₀*(Ω¹_{X₀/S₀}), 𝒪_{Y₀}) ⊗_{𝒪_{S₀}} gr^n(𝒪_S),
```

or again, if `Ω¹_{X₀/S₀}` is itself locally free, for example if X is smooth over S,

```text
𝒢_n = g₀*(𝔤_{X₀/S₀}) ⊗_{𝒪_{S₀}} gr^n(𝒪_S).
```

If, for example, S is affine with affine ring A, and `𝓘` is defined by an ideal I of A, one finds

```text
H^i(Y₀,𝒢_n) = H^i(Y₀,𝒢₀) ⊗_A gr_I^n(A)
```

for every i; indeed, the question is local on `S₀`, and one is reduced to the case where one tensors by a free module.
**In this case, the vanishing of `H¹(Y₀,𝒢₀)` implies that all obstructions to the successive extensions of `g_n`
vanish.** Thus one obtains:

**Corollary.**

<!-- label: III.5.6 -->

Let `(S,X,Y,𝓘,g_n)` be as above. Suppose moreover that X is smooth over S and Y is flat over S, and finally that S is
affine and the

```text
gr^n(𝒪_S) = 𝓘^n/𝓘^{n+1}
```

are locally free. Then the obstruction to constructing `g_{n+1}` lies in

```text
H¹(Y₀,𝒢₀) ⊗_A gr_I^{n+1}(A),
```

where A is the ring of S and I the ideal of A defining `𝓘`, with

```text
𝒢₀ = g₀*(𝔤_{X₀/S₀}).
```

If `H¹(Y₀,𝒢₀) = 0`, then `g_n` can be extended to an `Ŝ`-morphism ĝ: `Ŷ → X̂`.

Of course, this result would remain valid exactly as stated if, instead of starting with ordinary S-preschemes X and Y,
one started with formal `𝓘̂`-adic `Ŝ`-preschemes `𝔛` and `𝔜`. It allows one to prove, for example, that certain formal
schemes proper over a complete local ring are in fact algebraic. Indeed, proceeding as in Lemma III.4.2, one finds:

<!-- original page 76 -->

**Corollary.**

<!-- label: III.5.7 -->

Under the conditions of III.5.6, if `g₀` is an isomorphism, then so is ĝ.

The same result holds for closed immersions.

Thus one obtains:

**Proposition.**

<!-- label: III.5.8 -->

Let A be a complete local ring with maximal ideal `𝔪` and residue field k. Let `𝔛` and `𝔜` be two `𝔪`-adic formal
preschemes over A, flat over A, meaning that for every n, `X_n` and `Y_n` are flat over `A_n = A/𝔪^{n+1}`. Suppose
`X₀ = 𝔛 ⊗_A k` is smooth over k and `H¹(X₀,𝔤_{X₀/k}) = 0`. Then every k-isomorphism from `Y₀` onto `X₀` extends to an
A-isomorphism from `𝔜` onto `𝔛`; this extension is unique if moreover `H⁰(X₀,𝔤_{X₀/k}) = 0`.

This gives in particular a result on the **uniqueness** of a smooth formal prescheme over A reducing to a given
prescheme `X₀`, provided `H¹(X₀,𝔤_{X₀/k}) = 0`. Moreover, if `𝔛` and `𝔜` come from ordinary proper schemes over A, say X
and Y, then by the existence theorem for sheaves in formal geometry, cf. the Bourbaki seminar exposé no.
182,[^iii-5-8-1] there is a bijective correspondence between the A-isomorphisms `Y → X` and the A-isomorphisms of the
formal completions. Hence:

**Corollary.**

<!-- label: III.5.9 -->

The preceding statement III.5.8 remains valid when `𝔛` and `𝔜` are replaced by ordinary A-schemes X and Y, **proper**
over A.

Finally, when `𝔛` is a formal scheme proper over A, and `𝔜` is of the form `Ŷ` where Y is an ordinary proper scheme over
A, Proposition III.5.8 gives sufficient conditions for finding an isomorphism of `𝔛` with `Ŷ`, and hence for the formal
scheme `𝔛` to be in fact “algebraic”, i.e. isomorphic to an `X̂`, with X an ordinary proper scheme over A, which will
then be canonically determined. This happens notably if `X₀ = ℙ^r_k`, or more generally if `X₀` is a Severi-Brauer
scheme, i.e. becomes isomorphic to the standard projective space over the algebraic closure of k: every formal scheme
proper and flat over A, with fiber `ℙ^r_k`, is algebraizable, and more precisely is isomorphic to the `𝔪`-adic formal
completion of `ℙ^r_A`. In particular, thanks to the “existence theorem”, every ordinary proper scheme over A with fiber
`ℙ^r_k` is isomorphic to `ℙ^r_A`, where A is a complete local ring. Using descent theory, one can prove that if A is not
complete, X becomes isomorphic to `ℙ^r` after making a finite étale extension `A → A′` of the base; in this form, the
result remains valid for a fiber that is a Severi-Brauer scheme.

## 6. Global Infinitesimal Extension of Smooth S-Schemes

<!-- label: III.6 -->

Under the conditions of Theorem III.4.1, we propose to seek whether there exists a prescheme X smooth over Y such that
`X ×_Y Y₀` is `Y₀`-isomorphic to `X₀`, knowing that such a scheme “exists locally on `X₀`”. Taking up again the
step-by-step construction method, we are led to replace Y by the letter S, to suppose given a closed sub-prescheme `S₀`
of S defined by a sheaf of ideals `𝓘`, which it is no longer necessary to suppose locally nilpotent, to introduce the
closed sub-preschemes `S_n` of S defined by the `𝓘^{n+1}`, and to suppose given a sub-prescheme `X_n` smooth over `S_n`.
We propose to find an `S_{n+1}`-prescheme `X_{n+1}` “reducing to `X_n`”, i.e. equipped with an isomorphism

```text
X_n → X_{n+1} ×_{S_{n+1}} S_n
```

that is **smooth** over `S_{n+1}`, or equivalently by II.2.1, **flat** over `S_{n+1}`. As we noted in III.4, such data
amount to giving a sheaf of algebras `ℬ` over `f⁻¹(𝒪_{S_{n+1}})`, where f is the continuous map underlying the
structural morphism `X_n → S_n`, equipped with an augmentation `ℬ → 𝒪_{X_n}` compatible with the augmentation
`f⁻¹(𝒪_{S_{n+1}}) → f⁻¹(𝒪_{S_n})`, and satisfying two conditions (a) and (b) that we shall not rewrite, merely noting
that they are **local in nature** on the topological space underlying `X_n`. By III.4.1, a solution exists locally. It
is moreover unique up to nonunique isomorphism, at least locally. Let us begin by making this point precise.

<!-- original page 78 -->

**Proposition.**

<!-- label: III.6.1 -->

Let `X_{n+1}` over `S_{n+1}` reduce to `X_n` over `S_n`. Then the sheaf, on the topological space underlying `X_n`, or
equivalently `X₀`, of `S_{n+1}`-automorphisms of `X_{n+1}` inducing the identity on `X_n` is canonically isomorphic to

```text
𝒢 = 𝔤_{X₀/S₀} ⊗_{𝒪_{S₀}} gr^{n+1}_𝓘(𝒪_S)
```

as a sheaf of groups.

Indeed, by III.5.4 and III.4.2 this sheaf is a principal homogeneous sheaf under `𝒢`. Since it has a distinguished
section, the identity automorphism of `X_{n+1}`, it identifies as a sheaf of sets with `𝒢`. One must verify that this
identification is compatible with the group structures. This is easy, and is moreover a special case of a more general
result on the compatibility of the principal-bundle structures in III.5.1 and III.5.3 with composition of morphisms, a
result that we do not state here but that ought to appear in the hyperplodocus.

In particular, the sheaf on `X₀` of germs of automorphisms of `X_{n+1}`, with the structures just made explicit, is
**commutative**. It follows that if `X′_{n+1}` is another solution of the problem, isomorphic to `X_{n+1}` over the open
U of `X₀`, then the isomorphism from `Aut(X_{n+1})|U` to `Aut(X′_{n+1})|U` deduced by transport of structure from an
isomorphism `X_{n+1}|U → X′_{n+1}|U` **does not depend** on the choice of the latter. It is in fact nothing but the
identity isomorphism of `𝒢`, when both automorphism sheaves are identified with `𝒢` by III.6.1.

From III.6.1 one deduces:

**Corollary.**

<!-- label: III.6.2 -->

Let `X_{n+1}` and `X′_{n+1}` be smooth over `S_{n+1}` and “reduce to `X_n`”. Then the sheaf, on the space underlying
`X₀`, of `S_{n+1}`-isomorphisms from `X_{n+1}` to `X′_{n+1}` inducing the identity on `X_n` is naturally a principal
homogeneous sheaf under `𝒢`.

This expresses indeed that `X_{n+1}` and `X′_{n+1}` are locally isomorphic, and that the sheaf of germs of automorphisms
of the first is `𝒢`.

Now note that by III.4.1 one can always find a covering `(U_i)` of `X_n` by opens, which may be supposed affine, and for
each i a smooth scheme `X^i` over `S_{n+1}` reducing to `U_i`. Suppose for simplicity that `X_n` is **separated**, so
the `U_{ij} = U_i ∩ U_j` are still **affine** opens of `X_n`. Since H¹ of such an open with values in the quasi-coherent
sheaf `𝒢` is zero, Corollary III.6.2 implies that `X^i|U_{ij}` is isomorphic to `X^j|U_{ij}`; let

```text
f_{ji}: X^i|U_{ij} → X^j|U_{ij}
```

be such an isomorphism. It is determined up to a section of `𝒢` on `U_{ij}`. For every triple of indices put

```text
f_{ji}^{(k)} = f_{ji}|U_{ijk},    where U_{ijk} = U_i ∩ U_j ∩ U_k.
```

If one had

```text
f_{kj}^{(i)} f_{ji}^{(k)} = f_{ki}^{(j)},
```

<!-- label: eq:III.6.1 -->

it would follow that the `X^i` glue by the `f_{ji}`, and hence define a solution `X = X_{n+1}` of the desired problem.
Such a solution exists more generally if one can modify the `f_{ji}` into `f′_{ji}:`

```text
f′_{ji} = f_{ji} g_{ji},    g_{ji} ∈ Γ(U_{ij},𝒢),
```

<!-- label: eq:III.6.2 -->

so that the `f′_{ji}` satisfy the preceding transitivity condition. This sufficient condition for the existence of a
solution is also necessary, as one sees by recalling that such a solution X must, on each `U_i`, be isomorphic to `X^i`;
this allows one to choose isomorphisms

```text
f_i: X|U_i → X^i
```

and to define

```text
f′_{ji} = (f_j|U_{ij})(f_i|U_{ij})^{-1}: X^i|U_{ij} → X^j|U_{ij},
```

satisfying the gluing condition.

Now put

```text
f_{ijk} = (f_{ki}^{(j)})^{-1} f_{kj}^{(i)} f_{ji}^{(k)}.
```

<!-- label: eq:III.6.3 -->

This is an automorphism of `X^i|U_{ijk}`, which we identify with a section of `𝒢` by III.6.1. One checks, by a small
formal calculation left to the reader, that it is a **2-cocycle** f of the open covering `𝒰 = (U_i)`, with coefficients
in `𝒢`. The same calculation shows that, under III.6.2, the gluing condition III.6.1 **for the** `f′_{ij}` is equivalent
to the formula

```text
f = dg,
```

<!-- label: eq:III.6.4 -->

where `g = (g_{ij})` is regarded as a 1-cochain of `𝒰` with coefficients in `𝒢`. Thus **the necessary and sufficient
condition for the existence of a solution of the problem is that the cohomology class in `H²(𝒰,𝒢)` defined by the
cocycle III.6.3 be zero**. Moreover, since `𝒰 = (U_i)` is an affine covering of `X₀`, which is a **scheme**, `H²(𝒰,𝒢)`
identifies with `H²(X₀,𝒢)`. It is immediate that the cohomology class thus obtained in `H²(X₀,𝒢)` does not depend on the
affine covering considered. We shall call it the **obstruction class to extending `X_n` to a scheme `X_{n+1}` smooth
over `S_{n+1}`**.

Suppose this obstruction is zero. Then the argument sketched above shows that every solution `X = X_{n+1}` is isomorphic
to a solution obtained by gluing from isomorphisms `f′_{ji}`, which may be supposed of the form III.6.2, the gluing
condition being just III.6.3. The set of admissible g is therefore a principal homogeneous space under the group
`Z¹(𝒰,𝒢)` of 1-cocycles of `𝒰` with coefficients in `𝒢`. Moreover, one sees at once that **two cochains g and `g′`**,
with dg = `dg′ = f`, **define isomorphic solutions if and only if the cocycle `g − g′` is of the form dh**, with
`h = (h_i) ∈ C⁰(𝒰,𝒢)`. Thus one obtains:

**Theorem.**

<!-- label: III.6.3 -->

Let `(S,𝓘,X_n)` be as above, with `X_n` assumed separated.[^iii-6-3-1] Then one can define canonically an obstruction
class in `H²(X₀,𝒢)`, where `𝒢` is defined in III.6.1, whose vanishing is necessary and sufficient for the existence of a
scheme `X_{n+1}`, smooth over `S_{n+1}`, reducing to `X_n`. If this obstruction is zero, then the set of isomorphism
classes, with isomorphisms inducing the identity on `X_n`, of `S_{n+1}`-preschemes `X_{n+1}` reducing to `X_n` is
naturally a principal homogeneous space under `H¹(X₀,𝒢)`.

**Remarks.**

<!-- label: III.6.4 -->

Starting from III.6.1, the arguments made here are purely formal, and are advantageously transcribed in the setting of
local categories, or even of general fibered categories. The obstruction class to the existence of a “global” object of
a category, where one can find an object “locally”, any two objects are always “locally isomorphic”, and the
automorphism group of any object is commutative, obtained in this general context, contains as a special case the
“second boundary homomorphism” in an exact sequence of sheaves of not necessarily commutative groups, studied for
example by Grothendieck in Kansas or Tôhoku. The silly cocycle calculation made here should therefore be regarded as a
makeshift, due to the absence of a satisfactory reference text.

### 6.5

<!-- label: III.6.5 -->

Note that in III.6.3 there is in general no distinguished element in the principal homogeneous space under `H¹(X₀,𝒢)`
under consideration. This is reflected in particular by the fact that, after localizing on S, one obtains a principal
homogeneous sheaf on `S₀` with structural group `R¹f_*(𝒢)`, which is not necessarily trivial, i.e. which defines a
cohomology class in `H¹(S₀,R¹f_*(𝒢))` that is not necessarily zero. This is when one supposes that the class d ∈
`H²(X₀,𝒢)` is not zero, but is zero “locally over S”, i.e. defines a zero section of `R²f_*(𝒢)`, equivalently a zero
element in `H⁰(S₀,R²f_*(𝒢))`.

### 6.6

<!-- label: III.6.6 -->

For the moment we know almost nothing about the general algebraic mechanism of the cohomology classes introduced in this
number and their relations with the preceding number, and we have nothing precise to say about them in the simplest
particular cases, such as the case of abelian schemes over artinian rings.[^iii-6-6-1] One hopes that people will be
found to work the question out thoroughly; it seems particularly interesting. It is intimately linked, in particular, to
the “module theory” of algebraic structures.

**Corollary.**

<!-- label: III.6.7 -->

Suppose `H²(X₀,𝒢) = 0`. Then an `X_{n+1}` exists, and it is unique up to isomorphism if moreover `H¹(X₀,𝒢) = 0`.

In particular, proceeding step by step, and observing that an affine scheme is acyclic for a quasi-coherent sheaf, one
concludes:

**Corollary.**

<!-- label: III.6.8 -->

<!-- original page 82 -->

Under the conditions of Theorem III.4.1, if `X₀` is affine, then there exists an X smooth over Y reducing to `X₀`, and
this X is unique up to nonunique isomorphism.

Note that the direct proof of Theorem III.4.1 could not have given this result.

**Corollary.**

<!-- label: III.6.9 -->

Under the conditions of III.6.3, suppose S is affine with ring A, `𝓘` is defined by an ideal I of A, and finally the

```text
gr^n_𝓘(𝒪_S) = 𝓘^n/𝓘^{n+1}
```

are locally free. Then `H^i(X₀,𝒢)` identifies with

```text
H^i(X₀,𝒢₀) ⊗_A gr_I^{n+1}(A),
```

where

```text
𝒢₀ = 𝔤_{X₀/S₀}.
```

Thus the obstruction class to extending `X_n` lies in `H²(X₀,𝒢₀) ⊗_A gr_I^{n+1}(A)`, and, if it is zero, the set of
isomorphism classes of solutions is a principal homogeneous space under `H¹(X₀,𝒢₀) ⊗_A gr_I^{n+1}(A)`.

In particular:

**Corollary.**

<!-- label: III.6.10 -->

Under the conditions of III.6.9, suppose

```text
H²(X₀,𝔤_{X₀/S₀}) = 0.
```

Then there exists an `𝓘̂`-adic formal scheme `𝔛` over the `𝓘`-adic formal completion `Ŝ` of S, “smooth over S”, i.e.
such that the `𝔛_p` are smooth over the `S_p`, and reducing to `X_n`, i.e. equipped with an isomorphism

```text
X_n → 𝔛 ×_S S_n.
```

If moreover `H¹(X₀,𝔤_{X₀/S₀}) = 0`, then such a `𝔛` is unique up to isomorphism.

Indeed, one constructs `X_{n+1}`, `X_{n+2}`, and so on step by step, whence `𝔛` by passing to the inductive limit of the
`X_i`. The uniqueness assertion already appears in the preceding number.

## 7. Application to the Construction of Formal Schemes and Ordinary Smooth Schemes over a Complete Local Ring A

<!-- label: III.7 -->

The results of the preceding number sometimes make it possible to prove the existence of an `𝔪`-adic formal scheme over
such a ring, reducing to a given smooth scheme `X₀` over k. Distinguish two cases.

1. **A is “of equal characteristics”.** This is the case in particular if k has characteristic 0. Then one knows that
    there exists a **coefficient subfield of** A, i.e. a subfield `k′` such that `A → k` induces an isomorphism
    `k′ → k`. **Then there even exists an ordinary smooth scheme over A reducing to `X₀`**, namely `X = X₀ ⊗_k A`, with
    A regarded as an algebra over k by the homomorphism `k → k′ → A` defined by `k′`. It should be noted, however, that
    this construction is not “natural”. It is easy to convince oneself, already in the case where A = k[t]/(t²), the
    algebra of dual numbers, that another lifting homomorphism `k → A`, in this case defined by an absolute derivation
    of k into itself, defines an `X′` over A that in general **is not isomorphic to X**, if `H¹(X₀,𝔤_{X₀/k}) ≠ 0`. It
    would moreover be interesting to study, for k of characteristic 0, or imperfect of characteristic p > 0, which X
    smooth over A are obtained in this way, and under what condition two homomorphisms `k → A` define isomorphic
    A-schemes. Nevertheless, the existence of `k′` is enough to imply that the first obstruction to lifting `X₀`, which
    lies in `H²(X₀,𝔤_{X₀/k}) ⊗_k 𝔪/𝔪²`, is necessarily zero. Of course, once `X₀` has then been lifted to `X₁` smooth
    over `A/𝔪²`, the new obstruction to constructing `X₂` will in general not be zero: it will depend on a variable
    element in a certain principal homogeneous space under `H¹(X₀,𝒢₀) ⊗ 𝔪/𝔪²` and lies in `H²(X₀,𝒢₀) ⊗ 𝔪²/𝔪³`. The
    situation ought to be studied in detail.[^iii-7-a-1]

2) **A is of unequal characteristics.** In this case we know nothing, except if by luck `H²(X₀,𝔤_{X₀/k}) = 0`, in which
    case one can construct an `𝔪`-adic formal smooth scheme over A reducing to k. Even if `A = ℤ/p²ℤ` and `X₀` is an
    “abelian” scheme of dimension 2, one does not know whether it can be lifted to an `X = X₁` smooth over
    A;[^iii-7-b-1] on the other hand, we have no example of an `X₀` that has been proved not to come from an ordinary
    scheme X smooth over A. I have the impression that such examples should exist, with `X₀` a projective
    surface.[^iii-7-b-2] Let us simply point out that by Cohen's theorem, there exists a Cohen p-ring B with residue
    field k and a homomorphism `B → A` inducing the identity isomorphism on residue fields. Consequently, the
    “strongest” lifting result would be obtained by taking A to be a Cohen p-ring: if there is an ordinary or formal
    solution over such a ring, there is one over every complete local ring with residue field k. In particular, since
    for a Cohen p-ring `𝔪/𝔪²` identifies canonically with k, one sees that **for every smooth scheme `X₀` over a field
    k of characteristic p > 0, there exists a cohomology class in `H²(X₀,𝔤_{X₀/k})`**, the first obstruction to lifting
    `X₀` to a smooth scheme over a Cohen p-ring. We do not know whether it can be nonzero.[^iii-7-b-3]

Even if one succeeds step by step in constructing the `X_n` reducing to `X₀`, this generally gives only a **formal**
scheme `𝔛` smooth over A, reducing to `X₀`. When `X₀` is proper over A, there remains the question whether `𝔛` is in
fact algebraizable, in order to obtain an **ordinary** proper scheme over A, smooth over A, reducing to `X₀`. The only
known criterion, noted in the Bourbaki seminar and appearing in the Éléments, Chapter III, 4.7.1, is the following: if
`𝔛` is proper over A, and if `ℒ` is an invertible sheaf on `𝔛` such that the induced sheaf `ℒ₀` on `X₀` is ample, i.e.
some tensor power `ℒ₀^{⊗ n}`, n > 0, comes from a projective immersion of `X₀`, then there exists a scheme X projective
over A, and an ample invertible sheaf on X, such that `(𝔛,ℒ)` is obtained from it by `𝔪`-adic completion. This leads us,
given a locally free sheaf `𝓔₀` on `X₀`, which we shall choose invertible and ample for our purpose, to extend it to a
locally free sheaf `𝓔` on `𝔛`. For this, one is reduced to constructing step by step locally free sheaves `𝓔_n` on the
`X_n`. The discussion is entirely analogous to that of III.6, cf. Remark III.6.4; the essential role is played by the
**sheaf of automorphisms** of an `𝓔_{n+1}` inducing the identity on `𝓔_n`. One shows at once that this sheaf identifies
with

```text
𝒢 = Hom_{𝒪_{X₀}}(𝓔₀, 𝓔₀ ⊗ gr^{n+1}_𝓘(𝒪_X))
  = Hom_{𝒪_{X₀}}(𝓔₀,𝓔₀) ⊗ gr^{n+1}_𝓘(𝒪_X),
```

which is again a sheaf of commutative groups. One obtains:

<!-- original page 85 -->

**Proposition.**

<!-- label: III.7.1 -->

Let S be a prescheme equipped with a quasi-coherent sheaf of ideals `𝓘`, let X be a prescheme over S, let `S_n` be the
sub-prescheme of S defined by `𝓘^{n+1}`, and let `X_n = X ×_S S_n` for every integer n. Let `𝓔_n` be a locally free
sheaf on `X_n`, and seek to extend it to a locally free sheaf `𝓔_{n+1}` on `X_{n+1}`. Then `𝓔_n` defines a canonical
obstruction class in `H²(X₀,𝒢)`, where `𝒢` is the quasi-coherent sheaf given by the formula above. The vanishing of this
class is necessary and sufficient for the existence of an `𝓔_{n+1}` extending `𝓔_n`. If this class is zero, then the set
of isomorphism classes, with isomorphisms inducing the identity on `𝓔_n`, of solutions `𝓔_{n+1}` is a principal
homogeneous space under `H¹(X₀,𝒢)`.

This proposition gives rise to the usual corollaries. Let us only point out that if X is **flat** over S, then one may
write

```text
𝒢 = Hom_{𝒪_{X₀}}(𝓔₀,𝓔₀) ⊗_{𝒪_{S₀}} gr^{n+1}_𝓘(𝒪_S),
```

whence, if S is affine with ring A and the `𝓘^n/𝓘^{n+1}` are locally free, the sufficient condition

```text
H²(X₀,𝒢₀) = 0,    with    𝒢₀ = Hom_{𝒪_{X₀}}(𝓔₀,𝓔₀),
```

for the existence of an `𝓔_{n+1}`, and hence, step by step, for the existence of successive extensions `𝓔_m`, `m = n`,
`n + 1`, etc.

Returning to the initial situation, we therefore find:

**Proposition.**

<!-- label: III.7.2 -->

Let A be a complete local ring, and let `𝔛` be a formal scheme proper and flat over A, such that `X₀` is projective and
`H²(X₀,𝒪_{X₀}) = 0`. Then there exists a scheme X projective over A whose `𝔪`-adic formal completion is isomorphic to
`𝔛`.

Combining this with III.6.10, one finds:

**Theorem.**

<!-- label: III.7.3 -->

Let A be a complete local ring with residue field k, and let `X₀` be a projective smooth scheme over k such that

```text
H²(X₀,𝔤_{X₀/k}) = H²(X₀,𝒪_{X₀}) = 0.
```

Then there exists a smooth and projective scheme X over A reducing to `X₀`.

More generally, if one is given an `X_n` smooth over `A_n = A/𝔪^{n+1}` reducing to `X₀`, then there exists an X smooth
and proper over A and an isomorphism `X ⊗_A A_n = X_n`.

**Corollary.**

<!-- label: III.7.4 -->

Every smooth proper curve over k is obtained by reduction from a smooth proper curve over A.

This result will be the essential tool, together with the existence theorem for sheaves in formal geometry, for studying
the fundamental group of `X₀` by transcendental means.

<!-- original page 86 -->

<!-- end of Exposé III source block: next chapter begins at smf_doc-math_3_01.tex line 6269 -->

[^iii-1-1-1]: For a more general and more conceptual definition, motivated by III.2.1 below, cf. EGA 0_IV 19.3.1.

[^iii-1-2-1]: Or better, “essentially unramified”, respectively “essentially étale”; compare EGA IV 18.6.1.

[^iii-2-1-1]: Cf. EGA 0_IV 19.3, 19.8.

[^iii-5-0-1]: It seems preferable to adopt the shorter and more expressive term “torsor under `𝒢`”, introduced in J.
    Giraud's thesis.

[^iii-5-8-1]: Cf. EGA III 5.4.1 for the proof.

[^iii-6-3-1]: This condition is in fact unnecessary, and one can avoid the cocycle calculations above. Cf. J. Giraud,
    _Cohomologie Non Abélienne_, forthcoming from Springer Verlag, 1971. Compare Remarks III.6.4.

[^iii-6-6-1]: It is now known that this obstruction is always zero in this case \[added in 2003 by MR: cf. F. Oort,
    “Finite group schemes, local moduli for abelian varieties and lifting problems”, *Algebraic Geometry Oslo
    1970*, Wolters-Noordhoff, 1972, pp. 223-254\].

[^iii-7-a-1]: It is probably described by the Kodaira-Spencer bracket operation; cf. Séminaire Cartan, 1960/61, Exposé
    4\.

[^iii-7-b-1]: This is now proved; cf. note III.6.6, page 81 in the original numbering.

[^iii-7-b-2]: Such an example was later constructed by J.-P. Serre, _Proc. Nat. Acad. Sci. USA_ **47** (1961), no. 1,
    pp. 108-109, at least in certain dimensions. D. Mumford gave an unpublished example with an algebraic
    **surface**.

[^iii-7-b-3]: It can be nonzero, as indicated in note iii-7-b-2.
