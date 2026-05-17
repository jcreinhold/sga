# Exposé V. Construction of quotient schemes

<!-- label: III.V -->

*by P. Gabriel*

<!-- original page 251 -->

The aim of this Exposé is to prove the theorems stated in TDTE III.[^N.D.E-V-1] If `X` and `T` are two objects of a
category `C`, we write `X(T)` instead of `Hom_C(T, X)`. Similarly, if `φ : Y → X` is an arrow (resp. an object `T`) of
`C`, then `φ(T)` denotes the map `g ↦ φ ∘ g` from `Y(T)` to `X(T)`:

```text
        T
       / \
      g   φ ∘ g
     /     \
    Y ─ φ → X,
```

and `T(φ)` denotes the map `g ↦ g ∘ φ` from `T(X)` to `T(Y)`:

```text
    Y ─ φ → X
     \     /
      g ∘ φ   g
       \   /
        T.
```

Finally, if `P` is a scheme, we write `P` for the underlying set of `P`.

Exceptionally, in the present Exposé we do not follow the convention stated in IV 4.6.15 on the notation for quotients
(loc. cit., top of page 227 of the original), since we wish to give here a construction of quotients which also applies
to "pre-equivalence relations"[^N.D.E-V-2] that are not equivalence relations.

<!-- original page 252 -->

## 1. `C`-groupoids

<!-- label: III.V.1 -->

**a)** Let `C` be a category in which products and fiber products exist. Recall first that a diagram

```text
        d₁       p
   X₁ ⇉ X₀ → Y
        d₀
```

in `C` is said to be *exact* if `p d₀ = p d₁` and if, for every `T ∈ C`, `T(p)` is a bijection of `T(Y)` onto the subset
of `T(X₀)` consisting of arrows `f : X₀ → T` such that `f d₀ = f d₁`. One also says that `(Y, p)` is the *cokernel* of
`(d₀, d₁)` and writes

```text
(Y, p) = Coker(d₀, d₁).
```

**b)** Let, for example, `C` be the category `(Esp.An)` of ringed spaces. In this case, there always exists a cokernel
`(Y, p)`, which can be described as follows: the underlying topological space of `Y` is obtained from `X₀` by
identifying the points `d₀(x)` and `d₁(x)` and endowing `Y` with the quotient topology. The canonical map `π : X₀ → Y`
together with `d₀, d₁` then induces a double arrow of sheaves of rings on `Y`:

```text
                       δ₀
    π_∗(O₀) ⇉ π_∗(d_{0∗} O₁) = π_∗(d_{1∗} O₁),
                       δ₁
```

where `O_i` is the structure sheaf of `X_i`. We choose for the sheaf of rings on `Y` the subsheaf of `π_∗(O₀)` whose
sections `s` satisfy `δ₀(s) = δ₁(s)`. The arrow `p` is defined in the evident way.

Let[^N.D.E-V-3] `X₁ ⇉ X₀` be a diagram (with arrows `d₀, d₁`) in `(Esp.An)` and let `(Y, p)` be its cokernel. We say
that an open set `U` of `X₀` is *saturated* if `d₀⁻¹(U) = d₁⁻¹(U)`, which is equivalent to saying that `U = p⁻¹(p(U))`.
In this case, since `Y` is endowed with the quotient topology, `p(U)` is an open subset of `Y`.

**Lemma 1.1.** *Let `U` be a saturated open set of `X` and `V = p(U)`. If we denote by `U₁` the open set
`d₀⁻¹(U) = d₁⁻¹(U)` of `X₁`, and by `d̃₀`, `d̃₁`, and `p̃` the restrictions of `d₀, d₁` to `U₁`, and of `p` to `U`, then
`(V, p̃)` is a cokernel in `(Esp.An)` of:*[^N.D.E-V-4]

<!-- label: III.V.1.1 -->

```text
         d̃₁      p̃
   U₁ ⇉ U → V.
         d̃₀
```

The verification is straightforward.

**Lemma 1.2.** *Let `X₁ ⇉ X₀` be a diagram in `(Sch)` (with arrows `d₀, d₁`) and let `(Y, p)` be its cokernel in
`(Esp.An)`.*

<!-- label: III.V.1.2 -->

*(i) If `Y` is a scheme and `p` a morphism of schemes, then `(Y, p)` is a cokernel of `(d₀, d₁)` in `(Sch)`.*

*(ii) Suppose that every point of `X₀` possesses a saturated open neighborhood `U` such that, denoting by `d̃₀` and
`d̃₁` the restrictions of `d₀` and `d₁` to `d₀⁻¹(U) = d₁⁻¹(U)`, and by `(Q, q)` the cokernel of `(d̃₀, d̃₁)` in
`(Esp.An)`, the space `Q` is a scheme and `q` a morphism of schemes. Then `(Y, p)` is a cokernel of `(d₀, d₁)` in
`(Sch)`.*

(i) is proved in § 4.c); since the proof is short, let us repeat it here. Let `f : X₀ → Z` be a morphism of schemes such
that `f d₀ = f d₁`. By hypothesis, there is a unique morphism of ringed spaces `r : Y → Z` such that `f = r p`. It
remains to show that, for every `y ∈ Y`, the homomorphism `O_{r(y)} → O_y` induced by `r` is local. This follows from
the fact that `p` is surjective, so that `y` is of the form `p(x)`, and from the fact that the homomorphism
`O_{f(x)} → O_x` induced by `f` is local.

(ii) follows from (i) and the preceding lemma.

<!-- original page 253 -->

**c)** In this Exposé we study the existence of `Coker(d₀, d₁)` when the double arrow `(d₀, d₁)` is inserted in a richer
context; more precisely, let `X₂ = X₁ ×_{d₁, d₀} X₁` denote the fiber product of the diagram

```text
                X₁
                ↓ d₁
(∗)             X₀
                ↑ d₀
                X₁,
```

and let `d′₀` and `d′₂` be the two canonical projections of `X₂` onto `X₁`; one then has by definition a Cartesian
square

```text
                  d′₀
            X₂ ─────→ X₁
            │          │
        d′₂ │          │ d₁
            ↓          ↓
            X₁ ─────→ X₀.
                  d₀
(0)
```

Moreover, let us give ourselves a third arrow `d′₁ : X₂ → X₁`; we say that `(d₀, d₁ : X₁ ⇉ X₀, d′₁)` is a `C`-*groupoid*
if for every object `T` of `C`, `X₁(T)` is the set of arrows of a groupoid `X∗(T)` whose set of objects is `X₀(T)`, with
source map `d₁(T)`, target map `d₀(T)`, and composition map `d′₁(T)` (one identifies, as usual, `(X₁ ×_{d₁, d₀} X₁)(T)`
with `X₁(T) ×_{d₁(T), d₀(T)} X₁(T)`; we also recall that a groupoid is a category in which every arrow is
invertible).[^N.D.E-V-5]

If `φ` is an arrow of the groupoid `X∗(T)`, the map `f ↦ φ ∘ f` is a bijection from the set of arrows `f` whose target
coincides with the source of `φ` onto the set of arrows having the same target as `φ`. One sees easily that this fact
can be translated by saying that the square

```text
                  d′₁
            X₂ ─────→ X₁
            │          │
        d′₀ │          │ d₀
            ↓          ↓
            X₁ ─────→ X₀
                  d₀
(1)
```

is Cartesian.

Similarly, the map `g ↦ g ∘ φ` is a bijection from the set of arrows `g` of `X∗(T)` having source equal to the target of
`φ` onto the set of arrows having the same source as `φ`. This fact can again be translated by saying that the square

```text
                  d′₁
            X₂ ─────→ X₁
            │          │
        d′₂ │          │ d₁
            ↓          ↓
            X₁ ─────→ X₀
                  d₁
(2)
```

is Cartesian.

<!-- original page 254 -->

On the other hand, let `s : X₀ → X₁` be the unique arrow of `C` such that, for every `T`, `s(T) : X₀(T) → X₁(T)`
associates to every object of `X∗(T)` the identity arrow of that object.[^N.D.E-V-6] The arrow `s` satisfies the
equalities

```text
(3)        d₁ s = id_{X₀},
(3 bis)    d₀ s = id_{X₀}.
```

Finally, the associativity of the composition maps `d′₁(T)` translates into the commutativity of the diagram

```text
                              d′₁ × X₁
   X₁ ×_{d₁, d₀} X₁ ×_{d₁, d₀} X₁ ─────────→ X₁ ×_{d₁, d₀} X₁
            │                                       │
   X₁ × d′₁ │                                       │ d′₁
            ↓                                       ↓
   X₁ ×_{d₁, d₀} X₁ ──────────d′₁──────────────→ X₁.
(4)
```

Conversely, the conditions (1), (2), and (4) together with the existence of an arrow `s` satisfying (3) imply that
`(X₁ ⇉ X₀, d′₁)` is a `C`-groupoid. The condition (3) is harmless; it merely ensures that the map
`d₁(T) : X₁(T) → X₀(T)` is surjective for every `T ∈ C`. In what follows we shall mostly make use of the Cartesian
squares (0), (1) and (2), which we summarize in the diagram

```text
                  d′₁              d₀
            X₂  ────→  X₁  ──────→  X₀
                  d′₀
        d′₂ │           │ d₁
            ↓           ↓
            X₁  ────→  X₀
                  d₀
(0,1,2)
```

In this diagram the two left-hand squares (i.e. the squares (0) and (2)) are Cartesian; the first row is exact, and `X₂`
is identified with the fiber product `X₁ ×_{d₀, d₀} X₁`.

We use associativity only indirectly, for instance to ensure the existence of an arrow `s` satisfying (3) and (3 bis),
or else to ensure the existence of an arrow

```text
(†)   σ : X₁ → X₁    such that    d₀ σ = d₁    and    d₁ σ = d₀
```

(one chooses `σ` so that `σ(T) : X₁(T) → X₁(T)` sends every arrow of `X∗(T)` to its inverse).[^N.D.E-V-7]

By abuse of language, we shall sometimes call a `C`-*groupoid* a diagram

```text
        d′₀, d′₁, d′₂      d₀, d₁
   X₂ ⇶ X₁ ⇉ X₀
```

such that (0), (1) and (2) are Cartesian, (4) is commutative, and there exists `s` satisfying (3). The object `X₂` will
therefore be allowed to be "a" fiber product of (∗) without being "the" fiber product of (∗).[^N.D.E-V-8]

**Terminology.** Instead of `C`-groupoid `X∗`, we shall also speak of the *groupoid `X∗` with base `X₀`*, or of the
*pre-equivalence relation `X∗` in `X₀`*.

<!-- original page 255 -->

## 2. Examples of `C`-groupoids

<!-- label: III.V.2 -->

**a)** Let `X` be an object of `C` and `G` a `C`-group acting on the left on `X`. We denote by `d₀ : G × X → X` the
arrow defining the action of `G` on `X`, by `d₁ : G × X → X` the projection of the product onto the second factor, by
`μ : G × G → G` the arrow defining the `C`-group structure of `G`, and finally by `pr_{2,3}` the projection of
`G × G × X = G × (G × X)` onto the second factor. Then

```text
                  pr_{2,3}              d₁
   G × G × X      ⇉      G × X         ⇉   X
                  μ × X                 d₀
                  G × d₀
```

<!-- original page 256 -->

is a `C`-groupoid.

**b)** Let `d₀, d₁ : X₁ → X₀` be an *equivalence pair*, i.e., if `d₀ ⊠ d₁ : X₁ → X₀ × X₀` is the arrow with components
`d₀` and `d₁`, we suppose that `(d₀ ⊠ d₁)(T)` is, for every object `T` of `C`, a bijection of `X₁(T)` onto the graph of
an equivalence relation on `X₀(T)`. The set `X₁(T)` therefore identifies with the set of pairs `(x, y)` of elements of
`X₀(T)` such that `x ∼ y`; similarly, the set `X₂(T) = (X₁ ×_{d₁, d₀} X₁)(T)` identifies with the set of triples
`(x, y, z)` of elements of `X₀(T)` such that `x ∼ y` and `y ∼ z`. There is therefore one and only one arrow
`d′₁ : X₂ → X₁` making the squares (1) and (2) commute: `d′₁(T)` must send `(x, y, z) ∈ X₂(T)` to `(x, z) ∈ X₁(T)`. For
this choice of `d′₁`, `(d₀, d₁ : X₁ ⇉ X₀, d′₁)` is a `C`-groupoid.

Conversely, consider a `C`-groupoid `X∗` such that `d₀ ⊠ d₁ : X₁ → X₀ × X₀` is a monomorphism. Then `(d₀, d₁)` is an
equivalence pair and `X∗` can be reconstructed from `(d₀, d₁)` as explained a few lines above.[^N.D.E-V-9]

**c)** If `p : X → Y` is any arrow of `C` and if `pr₁` and `pr₂` are the two projections of `X ×_{p, p} X` onto `X`,
then `(pr₁, pr₂) : X ×_{p, p} X ⇉ X` is an equivalence pair. One says that `p` is an *effective epimorphism* if the
diagram

```text
                  pr₁           p
   X ×_{p, p} X  ⇉  X  ────→  Y
                  pr₂
```

is exact, that is, if `(Y, p) = Coker(pr₁, pr₂)`.

Let, for example, `S` be a Noetherian scheme and let `C` be the category of schemes finite over `S`. Let us show that an
epimorphism in `C` is not necessarily effective: take `S` equal to `Spec k[T³, T⁵]`, where `k` is a commutative field,
`Y` equal to `S`, and `X` equal to `Spec k[T]`. If `i` is the inclusion of `B = k[T³, T⁵]` into `A = k[T]`, take `p`
equal to `Spec i`. In this case `X ×_{p, p} X` identifies with `Spec(A ⊗_B A)` and `Coker(pr₁, pr₂)` with `Spec B′`,
where `B′` is the subring of `A` consisting of `a` such that `a ⊗_B 1 = 1 ⊗_B a`. Now

<!-- original page 257 -->

```text
T⁷ ⊗_B 1 = (T² T⁵) ⊗_B 1 = T² ⊗_B T⁵ = T² ⊗_B (T³ T²) = T⁵ ⊗_B T² = 1 ⊗_B T⁷.
```

So `T⁷` belongs to `B′`, does not belong to `B`, and `Spec B′` is distinct from `Spec B`, which yields the
counterexample.[^N.D.E-V-10]

## 3. Some sorites on `C`-groupoids

<!-- label: III.V.3 -->

Here, in no particular order, are some remarks used in what follows:

**a)** Let

```text
        d′₀, d′₁, d′₂      d₀, d₁
   X₂ ⇶ X₁ ⇉ X₀
```

be a `C`-groupoid and `f₀ : Y₀ → X₀` an arrow of `C`. We shall define a `C`-groupoid with base `Y₀`

```text
        e′₀, e′₁, e′₂      e₀, e₁
   Y₂ ⇶ Y₁ ⇉ Y₀
```

which we shall call *induced by `X∗` and `f₀`*. One also says that `Y∗` is the *inverse image of `X∗` under the base
change `f₀`*.

We choose for `Y₁` the fiber product of the diagram

```text
                 f₁
   Y₁ ─────────→ X₁
   │              │
   │              │ d₀ ⊠ d₁
   ↓              ↓
   Y₀ × Y₀ ────→ X₀ × X₀,
        f₀ × f₀
```

and for `e₀` and `e₁` the arrows obtained by composing the canonical arrow `Y₁ → Y₀ × Y₀` with the first and second
projections of `Y₀ × Y₀`. The morphism `Y₁ → Y₀ × Y₀` is then `e₀ ⊠ e₁`, and one has `f₀ ∘ e_i = d_i ∘ f₁` for
`i = 0, 1`, where we have written `f₁` for the projection of `Y₁` onto `X₁`.

<!-- original page 258 -->

We set `Y₂ = Y₁ ×_{e₀, e₁} Y₁`, cf. 1.c). One can say that the pair `(e₀, e₁)` is defined in such a way that, for every
`T ∈ C` and every pair `(y, x)` of elements of `Y₀(T)`, there is a certain one-to-one correspondence `ψ ↦ _y ψ_x`
between the arrows `ψ` of `X∗(T)` with source `f₀(x)` and target `f₀(y)` and the arrows `_y ψ_x` of `Y∗(T)` with source
`x` and target `y`. One therefore determines `e′₁ : Y₂ → Y₁` by defining, for every `T ∈ C`, the composition of arrows
of `Y∗(T)` by the formula

```text
   _z ψ_y ∘ _y φ_x = _z (ψ ∘ φ)_x.
```

It is clear that this definition makes each `Y∗(T)` into a groupoid.

**b)** Knowing the `C`-groupoid `X∗` and the base change `f₀ : Y₀ → X₀`, one can reconstruct the pair
`(e₀, e₁) : Y₁ ⇉ Y₀` in another way:[^N.D.E-V-11] construct `Y₀ ×_{X₀} X₁`, `pr₁` and `pr₂` so that the square

```text
                       pr₂
   Y₀ ×_{X₀} X₁ ─────→ X₁
        │              │
    pr₁ │              │ d₀
        ↓              ↓
        Y₀ ──────────→ X₀
                  f₀
```

is Cartesian. One then verifies without difficulty, by reduction to the set-theoretic case, that one has the Cartesian
square

```text
              e₀ ⊠ f₁
   Y₁ ─────────────→ Y₀ ×_{X₀} X₁
   │                       │
e₁ │                       │ d₁ ∘ pr₂
   ↓                       ↓
   Y₀ ────────────────→ X₀,
              f₀
```

where `f₁` denotes the canonical projection of `Y₁ = (Y₀ × Y₀) ×_{(X₀ × X₀)} X₁` onto `X₁`.

<!-- original page 259 -->

**c)** We shall give two examples of inverse images of a `C`-groupoid. Take `Y₀` equal to `X₁`, `f₀` equal to `d₀`. For
every object `T` of `C`, `Y₁(T)` then identifies with the set of diagrams of the form

```text
        φ
   b ────→ d
   ↑        ↑
   f        g
   │        │
   a        c
```

of `X∗(T)`. The source of such a diagram is the arrow `f`, the target is the arrow `g`. These diagrams compose in the
evident way.

Now put `Y′₀ = X₁`, `f′₀ = d₁` (we add the primes[^N.D.E-V-12] to avoid any confusion with the preceding example). In
this case, `Y′₁(T)` identifies, for every `T ∈ C`, with the set of diagrams of the form

```text
   b        d
   ↑        ↑
   f        g
   │   ψ   │
   a ────→ c
```

of the groupoid `X∗(T)`. The source of such a diagram is `f`, the target is `g`; the composition of these diagrams is
evident.

This being so, it is clear that the identity map of `Y₀(T)` and the map

```text
        φ                       
   b ────→ d           b        d
   ↑        ↑          ↑        ↑
   f        g    ↦     f        g
   │        │          │  g⁻¹φf │
   a        c          a ─────→ c
```

from `Y₁(T)` to `Y′₁(T)` define an isomorphism of the groupoid `Y∗(T)` onto `Y′∗(T)`. Moreover, this isomorphism depends
functorially on `T`, so that the `C`-groupoids `Y∗` and `Y′∗` are isomorphic.[^N.D.E-V-13]

<!-- original page 260 -->

**d)**

**Proposition 3.1.** *We keep the notations of a) and assume that `f₀` is an effective and universal epimorphism. Then
`Coker(d₀, d₁)` exists if and only if `Coker(e₀, e₁)` exists.*[^N.D.E-V-14] *Moreover, in that case, `f₀` induces an
isomorphism*

<!-- label: III.V.3.1 -->

```text
   Coker(d₀, d₁) ⥲ Coker(e₀, e₁).
```

Let us first recall that an epimorphism `f₀ : Y₀ → X₀` is said to be *universal* if, for every Cartesian square

```text
   Y′ ─────→ Y₀
   │         │
f′ │         │ f₀
   ↓         ↓
   X′ ─────→ X₀,
```

`f′` is an epimorphism. This being so, let us denote by `C(d₀, d₁)` the covariant functor from `C` to sets which
associates to every `T ∈ C` the kernel of the pair `T(d₀), T(d₁) : T(X₀) ⇉ T(X₁)`. We define `C(e₀, e₁)` similarly. For
every `T ∈ C`, one therefore has a commutative diagram

```text
                           T(d₁)
   C(d₀, d₁)(T) ────→ T(X₀) ⇉ T(X₁)
                           T(d₀)
        │                  │           │
   T(f) │           T(f₀) │           │ T(f₁)
        ↓                  ↓           ↓
                           T(e₁)
   C(e₀, e₁)(T) ────→ T(Y₀) ⇉ T(Y₁),
                           T(e₀)
```

where `T(f)` is the injection induced by the injection `T(f₀)`. If we show that `T(f)` is a surjection for every `T`, we
shall have a functorial isomorphism `f : C(d₀, d₁) ⥲ C(e₀, e₁)`, so that the representability of one of these functors
will be equivalent to that of the other; this will prove our proposition.

To prove the surjectivity of `T(f)`, consider the diagram

```text
                          f₁
              Y₁ ─────────────→ X₁
            ↗  
        Δ ↗  e₀ │ e₁          d₀ │ d₁
         ↗      ↓                ↓
   Y₀ ×_{X₀} Y₀ ─────→ Y₀ ─────→ X₀,
                   pr₂      f₀
              pr₁
```

<!-- original page 261 -->

where `Δ` is the section of `Y₁ → Y₀ × Y₀` defined by the morphism `s ∘ f₀ ∘ pr₁ : Y₀ × Y₀ → X₁`, with `s : X₀ → X₁` the
arrow satisfying equalities (3) and (3 bis) of section 1.

If the arrow `g : Y₀ → T` is such that `g ∘ e₀ = g ∘ e₁`, then `g ∘ e₀ ∘ Δ = g ∘ e₁ ∘ Δ`, so `g ∘ pr₁ = g ∘ pr₂`. Since
`f₀` is an effective epimorphism, `g` factors through `f₀` and an arrow `h : X₀ → T`, that is to say `g = T(f₀)(h)`. It
remains to show that `h` belongs to `C(d₀, d₁)(T)`, i.e. satisfies `h d₀ = h d₁`; now one has

```text
   h d₀ f₁ = h f₀ e₀ = g e₀ = g e₁ = h f₀ e₁ = h d₁ f₁,
```

whence the desired equality, since `f₁` is an epimorphism (because `f₀` is a universal epimorphism).

**e)** Consider now a scheme `S` and choose `C` equal to `(Sch/S)`. The data of a `C`-groupoid

```text
        d′₀, d′₁, d′₂      d₀, d₁
   X₂ ⇶ X₁ ⇉ X₀
```

allows one to define an equivalence relation on the set `X₀` underlying the scheme `X₀`: if `x, y ∈ X₀`, one writes
`x ∼ y` when there exists `z ∈ X₁` such that `x = d₁ z` and `y = d₀ z`. The reflexivity and symmetry of this relation
are evident;[^N.D.E-V-15] let us prove transitivity: if `x ∼ y` and `y ∼ z`, there exist `u, v ∈ X₁` with `x = d₁ u`,
`y = d₀ u`, `y = d₁ v`, `z = d₀ v`. It follows that `(v, u)` belongs to the set-theoretic fiber product
`X₁ ×_{d₁, d₀} X₁`. Since the canonical map

<!-- original page 262 -->

```text
   X₁ ×_{d₁, d₀} X₁ ⟶ X₁ ×_{d₁, d₀} X₁
```

from the set underlying the fiber product into the fiber product of the underlying sets is surjective, `(v, u)` is the
image of some `w ∈ X₂`. One then has `x = d₁ d′₁ w` and `z = d₀ d′₁ w`, whence `x ∼ z`.

**f)** We keep the notations of a) and b), `C` still being `(Sch/S)`. If `x, y` are points of `Y₀`, we shall see that
one has `x ∼ y` if and only if `f₀(x) ∼ f₀(y)` (the inverse image of the equivalence relation defined by a groupoid is
the equivalence relation defined by the inverse image of the groupoid).

Indeed, suppose `x ∼ y`. There exists therefore `z ∈ Y₁` such that `x = e₁(z)` and `y = e₀(z)`. Since
`f₀ ∘ e_i = d_i ∘ f₁` for `i = 0, 1`, one then has `f₀(x) = d₁ f₁(z)` and `f₀(y) = d₀ f₁(z)`, whence `f₀(x) ∼ f₀(y)`.

Conversely, suppose `f₀(x) ∼ f₀(y)` and let `z ∈ X₁` be such that `f₀(y) = d₁(z)` and `f₀(x) = d₀(z)`. Using the
construction and notations of b), there is then a point `t` of `Y₀ ×_{X₀} X₁` such that `pr₁(t) = x` and `pr₂(t) = z`.
Similarly, since `f₀(y) = d₁ pr₂(t)`, there is `s ∈ Y₁` such that `y = e₁(s)` and `(e₀ ⊠ f₁)(s) = t`. One then has
`e₀(s) = pr₁(e₀ ⊠ f₁)(s) = pr₁(t) = x`. Whence `x ∼ y`.

<!-- original page 261 -->

## 4. Passage to the quotient by a finite and flat groupoid (proof of a particular case)

<!-- label: III.V.4 -->

**Theorem 4.1.** *Consider a `(Sch/S)`-groupoid*

<!-- label: III.V.4.1 -->

```text
        d′₀, d′₁, d′₂      d₀, d₁
   X₂ ⇶ X₁ ⇉ X₀.
```

*Suppose the following conditions are satisfied:*[^N.D.E-V-16]

<!-- original page 263 -->

*a) `d₁` is finite locally free;*

*b) for every `x ∈ X₀`, the set `d₀ d₁⁻¹(x)` is contained in an affine open of `X₀`.*[^N.D.E-V-17]

*Then:*

*(i) There exists a cokernel `(Y, p)` of `(d₀, d₁)` in `(Sch/S)`; moreover, such a `(Y, p)` is a cokernel of `(d₀, d₁)`
in the category of all ringed spaces.*

*(ii) `p` is integral and open, and `Y` is affine if `X₀` is affine.*[^N.D.E-V-18]

*(iii) The morphism `X₁ → X₀ ×_Y X₀` with components `d₀` and `d₁` is surjective.*

*(iv) If `(d₀, d₁)` is an equivalence pair, then `X₁ → X₀ ×_Y X₀` is an isomorphism*[^N.D.E-V-19] *and `p : X₀ → Y` is
finite locally free.*[^N.D.E-V-20] *Moreover, `(Y, p)` is a cokernel of `(d₀, d₁)` in the category of sheaves for the
(fppf) topology and, for every base change `Y′ → Y`, `Y′` is the cokernel of the groupoid `X∗ ×_Y Y′` obtained from `X∗`
by the base change `X₀ ×_Y Y′ → X₀`.*

*In particular, for every base change `S′ → S`, `Y′ = Y ×_S S′` is the cokernel of the `S′`-groupoid `X′∗ = X∗ ×_S S′`.
So, in this case, "the formation of the quotient commutes with base change".*

It evidently follows from (i) that the topological space underlying `Y` is the quotient of the topological space
underlying `X₀` by the equivalence relation defined by the `(Sch/S)`-groupoid `X∗`.

We shall first prove this theorem when `X₀` is affine and `d₁` is locally free of constant rank `n`. We shall see next
how to reduce to this particular case.

<!-- original page 262 -->

In the case in which we have placed ourselves, `X₀`, `X₁` and `X₂` are affine. We can therefore suppose that

```text
   X_i = Spec A_i,   d_j = Spec δ_j,   d′_k = Spec δ′_k,
```

the `A_i` being commutative rings and the `δ_j`, `δ′_k` ring homomorphisms. One can then replace the diagram (0, 1, 2)
by the following

```text
                    δ′₁
            A₂ ⇇ A₁ ⇇ A₀
                    δ′₀         δ₀
   (0,1,2)∗   δ′₂        δ₁
                    δ₁
            A₁ ⇇ A₀,
                    δ₀
```

where the two left-hand squares are cocartesian.

Let `B` denote the subring of `A₀` consisting of those `a ∈ A₀` such that `δ₀(a) = δ₁(a)`.

<!-- original page 264 -->

**a)** Let us show that `A₀` is integral over `B`. If `a` belongs to `A₀`, let

```text
   P_{δ₁}(T, δ₀(a)) = Tⁿ − σ₁ T^{n−1} + ⋯ + (−1)ⁿ σ_n
```

be the characteristic polynomial of `δ₀(a)` when `A₁` is regarded as an algebra over `A₀` via the homomorphism `δ₁` (cf.
Bourbaki, Alg. VIII, § 12 and Alg. comm. II, § 5, exercise 9). Since the left-hand squares of `(0,1,2)∗` are
cocartesian, one has

```text
   δ₀(P_{δ₁}(T, δ₀(a))) = P_{δ′₂}(T, δ′₀ δ₀(a))
```

and

```text
   δ₁(P_{δ₁}(T, δ₀(a))) = P_{δ′₂}(T, δ′₁ δ₀(a)).
```

Since `δ′₀ δ₀ = δ′₁ δ₀`, one has

```text
   δ₀(P_{δ₁}(T, δ₀(a))) = δ₁(P_{δ₁}(T, δ₀(a))),
```

that is, `δ₀(σ_i) = δ₁(σ_i)` for every `i`. Hamilton–Cayley moreover tells us that

```text
   δ₀(a)ⁿ − δ₁(σ₁) δ₀(a)^{n−1} + ⋯ + (−1)ⁿ δ₁(σ_n) = 0.
```

Since `δ₁(σ_i) = δ₀(σ_i)`, one also has

```text
   δ₀(a)ⁿ − δ₀(σ₁) δ₀(a)^{n−1} + ⋯ + (−1)ⁿ δ₀(σ_n) = 0,
```

whence

```text
   aⁿ − σ₁ a^{n−1} + ⋯ + (−1)ⁿ σ_n = 0,
```

<!-- original page 265 -->

since there exists a homomorphism `τ : A₁ → A₀` such that `τ δ₀ = id_{A₀}`, hence `δ₀` is injective. It follows that
`A₀` is integral over `B`.

**b)** Consider now two prime ideals `x` and `y` of `A₀`. We shall show that the equality `x ∩ B = y ∩ B` entails the
existence of a prime ideal `z` of `A₁` such that `x = d₀(z)` and `y = d₁(z)`.

Indeed, if the assertion were not true, `x` would be distinct from `δ₀⁻¹(t)` for every prime ideal `t` of `A₁` such that
`δ₁⁻¹(t) = y`. For such a `t` one would have `δ₀⁻¹(t) ∩ B = δ₁⁻¹(t) ∩ B = y ∩ B = x ∩ B`, whence by Cohen–Seidenberg
(cf. Bourbaki, Alg. comm. V, § 2, cor. 1 of prop. 1) `x` would be contained in no `δ₀⁻¹(t)`.[^N.D.E-V-21] Now there are
at most `n` prime ideals `t` of `A₁` such that `δ₁⁻¹(t) = y` (cf. loc. cit., prop. 3), so, by the "Prime Avoidance
Lemma" (loc. cit., II, § 1, prop. 3), there would exist `a ∈ x` belonging to no `δ₀⁻¹(t)`. Consequently, `δ₀(a)` would
belong to none of these ideals `t`, and so, by the lemma below, the norm `N_{δ₁}(δ₀(a))` would not belong to `y` (one
computes this norm by regarding `A₁` as an algebra over `A₀` via the homomorphism `δ₁`; one has `N_{δ₁}(δ₀(a)) = σ_n`
with the notations of a)). But, since `(−1)^{n−1} σ_n = aⁿ + ∑_{i=1}^{n−1} (−1)^i σ_i a^{n−i}`, this norm belongs to
`B ∩ x = B ∩ y`, whence the contradiction.

**Lemma 4.1.1.** *Let `A → A′` be a morphism of commutative rings making `A′` into a projective `A`-module of rank `n`.
Let `p ∈ Spec(A)`, `q₁, …, q_r` the elements of `Spec(A′)` above `p`, and `a ∈ A′`. Then `a` belongs to `q₁ ∪ ⋯ ∪ q_r`
if and only if its norm `N(a)` belongs to `p`.*

<!-- label: III.V.4.1.1 -->

Indeed, replacing `A` and `A′` by the localizations `A_p` and `A′_p`, we reduce to the case where `(A, p)` is local and
`A′` is semilocal, with `Spec(A′) = {q₁, …, q_r}`. In this case, `A′` is a free `A`-module of rank `n` (cf. Bourbaki,
Alg. comm. II, § 3.2, cor. 2 of prop. 5), and `N(a)` is the determinant of the endomorphism `ℓ_a : a′ ↦ a a′` of `A′`,
so one has the equivalences

```text
   N(a) ∉ p ⟺ N(a) invertible ⟺ ℓ_a invertible ⟺ a ∉ q₁ ∪ ⋯ ∪ q_r.
```

**c)** Proof of (i):

Set `Y = Spec B` and `p = Spec i`, where `i` is the inclusion of `B` into `A₀`. By a), the morphism `p : X₀ → Y` is
surjective. Let us first show that `(Y, p)` is a cokernel of `(d₀, d₁)` in the category of all ringed spaces: it follows
indeed from b) that the set underlying `Spec B` is obtained from the set underlying `X₀` by identifying the points `x`
and `y` such that there exists `z ∈ X₁` with `d₁ z = y`, `d₀ z = x`. Moreover, since `i` is integral, `p = Spec i` is
closed, so `Y` is endowed with the quotient topology of that of `X₀`. It follows that `p` is open. Indeed, let `U′` be
any open of `X₀`; since `d₁` is surjective and finite locally free, hence faithfully flat and of finite presentation,
and therefore open, the saturation `U = d₁(d₀⁻¹(U′))` of `U′` for the equivalence relation defined by `X∗` is open. Then
`p(U′) = p(U)` is open, since `Y` is endowed with the quotient topology.

It follows finally from the choice of `B` and from the fact that `p`, `d₀` and `d₁` are affine that the canonical
sequence of sheaves of rings

<!-- original page 266 -->

```text
                       p_∗(δ₁)
   O_Y ────→ p_∗(O_{X₀}) ⇉ p_∗(d_{0∗}(O_{X₁})) = p_∗(d_{1∗}(O_{X₁}))
                       p_∗(δ₀)
```

is exact.

It remains to show that `(Y, p)` is also the cokernel of `(d₀, d₁)` in the category of schemes (more generally, in the
category of ringed spaces in local rings). Let then `q : X₀ → Z` be a morphism of schemes such that `q d₀ = q d₁`. By
what precedes, there is a unique morphism of ringed spaces `r : Y → Z` such that `q = r p`. It remains to show that, for
every `y ∈ Y`, the homomorphism `O_{r(y)} → O_y` induced by `r` is local. This follows from the fact that `p` is
surjective, so that `y` is of the form `p(x)`, and from the fact that the homomorphism `O_{q(x)} → O_x` induced by `q`
is local.

**d)** Proof of (ii): Follows from a) and c).

**e)** Proof of (iii):

Recall that one denotes by `P` the set underlying a scheme `P`, and by `d : P → Q` the map induced by a morphism
`d : P → Q`.

**Lemma 4.1.2.**[^N.D.E-V-22] *Let `(A, m)` be a local ring, `k` its residue field, and `K` an extension of the field
`k`. Then there exists a local and flat `A`-algebra `B` such that `B/mB` is `k`-isomorphic to `K`; moreover, one can
choose `B` finite and free over `A` if `K` is of finite degree over `k`.*

<!-- label: III.V.4.1.2 -->

This is proved in EGA 0_III, 10.3.1, where it is moreover shown that one can choose `B` Noetherian if `A` is. For the
reader's convenience, let us indicate the proof.

Put `A′ = A[T]`, where `T` is an indeterminate. If `K = k(T)`, let `p = m A′` and `B = A′_p`. Then
`B/mB ≅ k[T]_{(0)} = k(T)`, and `B` is flat over `A′`, which is a free `A`-module, so `B` is flat over `A`.

If `K = k(t) = k[t]`, where `t` is algebraic over `k`, set `B = A′/(F)`, where `F ∈ A′` is a monic polynomial whose
image in `k[T]` is the minimal polynomial `f` of `t` over `k`. Then `B` is a free `A`-module of finite rank
`deg(F) = deg(f)`. In particular, `B` is integral over `A`, hence every maximal ideal of `B` contains `m`. Since
`B/mB ≅ k[T]/(f) ≅ K`, it follows that `B` is local, with maximal ideal `mB`. This already shows that if `[K : k] < ∞`,
one can choose `B` finite and free over `A`.

In the general case, let `(t_i)_{i ∈ I}` be a system of generators of `K` over `k`, and endow `I` with a well-ordering
(i.e., a total order `⩽` such that every non-empty subset of `I` has a least element). For every `i ∈ I`, let `k_i`
(resp. `k_{<i}`) denote the subfield of `K` generated by the `t_j` for `j ⩽ i` (resp. `j < i`). Adding one element if
necessary, we may suppose that `I` has a greatest element `ξ`, so that `K = k_ξ`. Consider the subset `J` of `I`
consisting of indices `i` such that there exists an inductive system `(A_j)_{j ⩽ i}` of local and flat `A`-algebras such
that `A_j/m A_j ≅ k_j` and `A_j` is flat over `A_ℓ` for every `ℓ < j`. Suppose `I − J` non-empty; let `i` be its least
element and let `A′ = lim_{j < i} A_j`. Since tensor product commutes with direct limits, `A′` is flat over `A` and over
each `A_j` for `j < i`, and one has `A′/m A′ ≅ A′ ⊗_A (A/m) ≅ k_{<i}`. Moreover, `A′` is local, with maximal ideal
`m A′`. Indeed, if `x = f_j(x_j)` is non-invertible, then `x_j` is not invertible, hence belongs to the maximal ideal
`m A_j` of `A_j`, whence `x ∈ m A′`. It then follows from the monogenic case treated above that there exists a local and
flat `A′`-algebra `A_i` such that `A_i/m A_i ≅ k_{<i}(t_i) = k_i`; then `A_i` is flat over each `A_j` for `j < i`, and
so `i ∈ J`, contrary to hypothesis. This contradiction shows that `J = I`, and so `A_ξ` answers the question. Lemma
4.1.2 is proved.

<!-- original page 265 -->

Let us now prove 4.1 (iii). Recall that one denotes by `P` the set underlying a scheme `P`, and by `d : P → Q` the map
induced by a morphism `d : P → Q`. One can then translate b) by saying that the map

```text
   d₀ ⊠ d₁ : X₁ ⟶ X₀ ×_Y X₀
```

with components `d₀` and `d₁` is surjective; now this map factors as follows

```text
   X₁ ──d₀⊠d₁──→ X₀ × X₀ ──q──→ X₀ ×_Y X₀,
                       (set-theoretic Y-product)
```

`q` being the canonical map; the image of `d₀ ⊠ d₁` therefore contains all points `v` of `X₀ ×_Y X₀` such that
`{v} = q⁻¹(q(v))`. This last condition[^N.D.E-V-23] will be realized in particular if `v` is rational over `Y`, that is
to say, if the residue field `κ(v)` of `v` identifies with the residue field `κ(w)` of the image `w` of `v` in `Y`.

<!-- original page 267 -->

If `v ∈ X₀ ×_Y X₀` is not rational over `Y`, let `w` again be the image of `v` in `Y`. By lemma 4.1.2, there exists a
local ring `C` of radical `m` and a local and flat homomorphism `f : O_w → C` such that `C/m` is isomorphic to `κ(v)` as
a `κ(w)`-algebra. If one sets `Y′ = Spec C` and if `π : Y′ → Y` is the morphism induced by `f`, it is clear that the
canonical projection of `(X₀ ×_Y X₀) ×_Y Y′` to `X₀ ×_Y X₀` sends to `v` a point `v′` of `(X₀ ×_Y X₀) ×_Y Y′` which is
rational over `Y′`. Since

```text
   (X₀ ×_Y X₀) ×_Y Y′ ≅ (X₀ ×_Y Y′) ×_{Y′} (X₀ ×_Y Y′),
```

and since the hypotheses of theorem 4.1 and the previous results, in particular point b), remain valid after the base
change `π : Y′ → Y`, then `v′` is the image of an element `u′ ∈ X₁ ×_Y Y′` by the morphism deduced from `d₀ ⊠ d₁` by
base change. If `u` is the image of `u′` in `X₁`, one indeed has `v = (d₀ ⊠ d₁)(u)`.

**f)** Proof of (iv):[^N.D.E-V-24]

**Lemma 4.1.3.** *If a monomorphism of schemes `f : T → Z` is a finite morphism, it is a closed immersion.*

<!-- label: III.V.4.1.3 -->

Indeed, covering `Z` by affine opens `Z_i` and replacing `f` by the induced morphisms `f⁻¹(Z_i) → Z_i`, we reduce (`f`
being finite, hence affine) to the case where `Z = Spec B` and `T = Spec A`. Since `f` is a monomorphism, the diagonal
morphism `T → T ×_Z T` is an isomorphism (EGA I, 5.3.8), i.e., `A ⊗_B A → A` is an isomorphism. Consequently, for every
maximal ideal `m` of `B`, one has an isomorphism

```text
   (A/mA) ⊗_k (A/mA) ≅ (A/mA),
```

<!-- original page 266 -->

where we have set `k = B/m`. Since `A` is finite over `B`, `A/mA` is a `k`-vector space of finite dimension `d`, and the
above isomorphism entails `d = 0` or `1`, so that the morphism `k = B/m → A/mA` is surjective. Hence, by Nakayama's
lemma (`A` being finite over `B`), the morphism `B_m → A_m` is surjective. It follows that the morphism of `B`-modules
`B → A` is surjective (since its cokernel `C` satisfies `C_m = 0` for every `m`, so is zero). This proves the lemma.

Let us now prove (iv). By hypothesis, `X₀ = Spec A₀`, `X₁ = Spec A₁`, and, for `i = 0, 1`, the morphism `δ_i : A₀ → A₁`
makes `A₁` a finitely generated `A₀`-module; thus, a fortiori, the morphism `A₀ ⊗_B A₀ → A₁` is finite.

One assumes in addition that `d = d₀ ⊠ d₁ : X₁ → X₀ ×_Y X₀` is a monomorphism; hence, by the preceding lemma, the
morphism `A₀ ⊗_B A₀ → A₁` is surjective.

We shall show that it is an isomorphism (we shall prove along the way that `p : X₀ → Y` is finite and locally free). It
suffices to show that, for every prime ideal `p` of `B`, the homomorphism `(A₀)_p ⊗_{B_p} (A₀)_p → (A₁)_p` with
components `δ_{0p}` and `δ_{1p}` is bijective. In other words, one may suppose `B` local. It then follows from b) that
`(A₀)_p` is semilocal; indeed, if `m` is a maximal ideal of `(A₀)_p`, the other maximal ideals are of the form
`δ_0⁻¹(n)`, where `n` runs over the prime ideals of `A₁` such that `δ_1⁻¹(n) = m`; the assertion follows from the fact
that there are at most `n = [A₁ : A₀]` such prime ideals `n`. Possibly performing a faithfully flat base
change,[^N.D.E-V-25] one can also suppose that the residue field of `B` is infinite, so that one can use the following
lemma:

**Lemma 4.2.** *Let `B` be a local ring with infinite residue field, `A` a semilocal ring, and `i : B → A` a
homomorphism sending the maximal ideal `n` of `B` into the radical `r` of `A`. Let `M` be a free `A`-module of rank `n`
and `N` a `B`-submodule of `M` that generates `M` as an `A`-module. Then `N` contains a basis of `M` over `A`.*

<!-- label: III.V.4.2 -->

<!-- original page 268 -->

Recall indeed that a sequence `m₁, …, m_n` of elements of `M` is an `A`-basis of `M` if and only if the canonical images
of `m₁, …, m_n` in `M/rM` form a basis of `M/rM` over `A/r`. One can therefore replace `M` by `M/rM`, `N` by
`N/(N ∩ rM)`, `A` by `A/r` and `B` by `B/n`. In this case the lemma is easy (if `A` is a product of fields
`K₁ × ⋯ × K_r`, one can identify `M` with the module `K₁ⁿ × ⋯ × K_rⁿ`; if `x_j` is then an element of `N` whose `j`-th
component in `K₁ⁿ × ⋯ × K_rⁿ` is non-zero, show that a certain linear combination `x` of the `x_j` with coefficients in
`B` has all components non-zero; then replace `M` by `M/Ax` and proceed by induction on `n`).

We apply the preceding lemma in the following situation: `B = B`, `A = A₀`, `i` is the inclusion of `B` in `A₀`,
`M = A₁` regarded as an `A₀`-module via the homomorphism `δ₁`, `N = δ₀(A₀)`. Indeed, since `d₀ ⊠ d₁ : X₁ → X₀ ×_Y X₀` is
a closed immersion, the homomorphism `A₀ ⊗_B A₀ → A₁` with components `δ₀` and `δ₁` is surjective; this means precisely
that `δ₀(A₀)` generates the `A₀`-module `A₁`.

Let then `a₁, …, a_n` be elements of `A₀` such that `δ₀(a₁), …, δ₀(a_n)` form a basis of `A₁` over `A₀`. If we show that
`a₁, …, a_n` is a basis of `A₀` over `B`, it will follow that the homomorphism `A₀ ⊗_B A₀ → A₁` sends the basis
`(1 ⊗ a_i)_{1 ⩽ i ⩽ n}` to the basis `(δ₀(a_i))_{1 ⩽ i ⩽ n}`, hence is bijective. Consequently, if `ε : ℤⁿ → A₀` is the
morphism of abelian groups sending the natural basis of `ℤⁿ` to `a₁, …, a_n`, it suffices to prove that the map
`B ⊗_ℤ ℤⁿ → A₀` with components `i` and `ε` is bijective.

<!-- original page 269 -->

Now the diagram `(0, 1, 2)∗` considered at the beginning of this proof induces the following commutative diagram:

```text
                    δ′₁                       δ₀
            A₂ ⇇ A₁ ⇇ A₀
                    δ′₀
            │       │ ≅           │
         u₂ │    u₁ │           u₀│
            ↓       ↓             ↓
                    δ₁ ⊗ ℤⁿ      i ⊗ ℤⁿ
            A₁ ⊗_ℤ ℤⁿ ⇇ A₀ ⊗_ℤ ℤⁿ ⇇ B ⊗_ℤ ℤⁿ,
                    δ₀ ⊗ ℤⁿ
```

where `u₀`, `u₁` and `u₂` have respectively as components `i` and `ε`, `δ₁` and `δ₀ ε`, `δ′₂` and `δ′₀ δ₀ ε`. We know
that `u₁` is an isomorphism. Since the two left-hand squares of `(0, 1, 2)∗` are cocartesian, `u₂` is bijective. But the
two horizontal rows of our diagram are exact, so `u₀` is bijective.[^N.D.E-V-26] This shows that `A₀` is a `B`-module
locally free of rank `n`, and, by the previous reductions, this entails that `δ₀ ⊗ δ₁ : A₀ ⊗_B A₀ → A₁` is an
isomorphism. This completes the proof of theorem 4.1 in the particular case considered (`X₀` affine and `d₁` locally
free of constant rank `n`).

## 5. Passage to the quotient by a finite and flat groupoid (general case)

<!-- label: III.V.5 -->

**a)** Let `U^{(n)}` be the largest open subset of `X₀` above which `d₁` is finite locally free of rank `n`. One knows
that `X₀` is the direct sum of the `U^{(n)}`. It follows on the other hand from the two Cartesian squares

```text
              d′₀                              d′₁
   X₂ ────→ X₁          and       X₂ ────→ X₁
   │         │                     │         │
d′₂│         │ d₁                d′₂│         │ d₁
   ↓         ↓                     ↓         ↓
   X₁ ────→ X₀                     X₁ ────→ X₀
        d₀                                d₁
```

that the inverse images of `U^{(n)}` under `d₀` and `d₁` both coincide with the largest open subset of `X₁` above which
`d′₂` is locally free of rank `n`;[^N.D.E-V-27] one therefore has `d₀⁻¹(U^{(n)}) = d₁⁻¹(U^{(n)})`, so that the groupoid
`X∗` is the direct sum of the groupoids `X∗^{(n)}` induced by `X∗` on the open-and-closed subsets `U^{(n)}`.
Consequently, as one sees easily, it suffices to prove theorem 4.1 for each of the `X∗^{(n)}`: one is reduced to the
case where `d₁` is finite locally free of rank `n`.

**b)** We are now in a position to prove our theorem in the general case.

<!-- original page 270 -->

By a) one may suppose `d₁` locally free of rank `n`. Let then `(Y, p)` be a cokernel of `(d₀, d₁)` in the category of
all ringed spaces. The argument at the end of paragraph 4.c) shows that to prove 4.1 (i) it suffices to prove that `Y`
is a scheme and `p : X₀ → Y` a morphism of schemes. By lemma 1.2, the question is local on `Y`: let `y ∈ Y` and let
`x ∈ X₀` with `p(x) = y`; if `x` possesses a saturated affine open neighborhood `U`, then `p(U)` will be an affine open
of `Y` by § 4, and `p|U` will be a morphism of schemes. It therefore suffices to prove that every `x ∈ X₀` possesses a
saturated affine open neighborhood `U`. Here is how one proceeds (the proof is taken from SGA 1, VIII, cor. 7.6).

```text
   d₁(d₀⁻¹(x)) ⊂ U = (V_f)′ ⊂ V_f ⊂ V′ ⊂ V ⊂ X₀

      ↑                ↑           ↑
   affine open    special       affine
   special of V   affine open   open
                  of V
                      ↑           ↑
                  largest     largest
                  saturated   saturated
                  open in V_f open in V
```

By condition b) of 4.1, there exists an affine open `V` of `X₀` containing `d₁(d₀⁻¹(x))`;[^N.D.E-V-28] if `F = X₀ − V`,
then `d₁(d₀⁻¹(F))` is closed since `d₁` is integral, and `V′ = X₀ − d₁(d₀⁻¹(F))` is the largest saturated open contained
in `V`. Since `V′` is a neighborhood of the finite set `d₁(d₀⁻¹(x))`, there exists a section `f` of the structure sheaf
of `V` vanishing on `V − V′` and such that `d₁(d₀⁻¹(x))` is contained in the open `V_f` of `V` consisting of points
where `f` does not vanish. We shall show that the largest saturated open `(V_f)′` of `V_f` is affine, and therefore
answers the question.

Indeed, let `Z(f) = V′ − V_f`. Then `d₀⁻¹(Z(f))` is the set of points of `d₀⁻¹(V′) = d₁⁻¹(V′)` where the image
`d_0^∗(f)` of `f` under the map induced by `d₀` vanishes. On the other hand, since `d₁` induces a locally free morphism
of rank `n` from `d₀⁻¹(V′) = d₁⁻¹(V′)` onto `V′`,[^N.D.E-V-29] then, by lemma 4.1.1, `d₁(d₀⁻¹(Z(f)))` is the set of
points where the norm `N` of `d_0^∗(f)` for the morphism `d₁` vanishes. It follows that `(V_f)′ = V′ − d₁(d₀⁻¹(Z(f)))`
is the set of points of `V_f` where `N` does not vanish; consequently, `(V_f)′` is affine.

<!-- original page 271 -->

This proves 4.1 (i); assertions (ii), (iii), and the first part of (iv) are then clear. Let us finally show the
consequences indicated at the end of point (iv) (cf. [Ray67a], th. 1 (iii)).

By hypothesis, the groupoid `X∗` comes from an equivalence relation `i : R → X₀ × X₀` (`i` being therefore an immersion,
cf. N.D.E. 19), and one has established that `R` is effective (cf. Exp. IV, 3.3.2) and that `p : X₀ → Y = X₀/R` is a
surjective and finite locally free morphism, hence in particular faithfully flat and of finite presentation.

Consequently, denoting by `(M)` the family of faithfully flat morphisms locally of finite presentation, `R` is
`(M)`-effective. Therefore, by Exp. IV, 6.3.3, `(Y, p)` represents the quotient sheaf of `X₀` by `R` for the (fppf)
topology, and the assertions concerning base change follow from IV, 3.4.3.1.

**Remark 5.1.**[^N.D.E-V-30] *We keep the hypotheses and notations of 4.1, and suppose in addition that `S` is locally
Noetherian and `π₀ : X₀ → S` is quasi-projective. Let us then show that `π : Y → S` is quasi-projective.*

<!-- label: III.V.5.1 -->

The above hypotheses imply that `Y → S` is of finite type, see the proof of 6.1 (ii). Let `A` be an invertible
`O_{X₀}`-module that is ample for `π₀`. By EGA II, 6.1.12, `p_∗(A)` is an invertible `p_∗(O_{X₀})`-module. There
therefore exists a covering `(V_i)_{i ∈ I}` of `Y` by affine opens such that `A` is trivial above each of the saturated
affine opens `U_i = p⁻¹(V_i)`.

For each index `i`, write `A_{i,0} = O_{X₀}(U_i)`, `A_{i,1}` the ring of the affine open `d₀⁻¹(U_i) = d₁⁻¹(U_i)` of
`X₁`, `δ_{i,0}` (resp. `δ_{i,1}`) the morphism `A_{i,0} → A_{i,1}` induced by `d₀` (resp. `d₁`), and
`B_i = O_Y(V_i) = {b ∈ A_{i,0} | δ_{i,0}(b) = δ_{i,1}(b)}`.

Following EGA II, § 6.5, consider the invertible `O_{X₀}`-module `N_{d₁}(d_0^∗(A))`, the norm relative to the finite
locally free morphism `d₁ : X₁ → X₀` of the invertible `O_{X₁}`-module `d_0^∗(A)`. If `A` is given, relative to the
covering `(U_i)_{i ∈ I}`, by transition functions `c_{ij} ∈ O_{X₀}(U_i ∩ U_j)^×`, then `N_{δ₁}(d_0^∗(A))` is given by
the transition functions `N_{d₁}(δ_0(c_{ij})) ∈ O_{X₀}(U_i ∩ U_j)^×`; since, by paragraph 4.a), these elements belong to
`O_Y(V_i ∩ V_j)^×`, they define an invertible `O_Y`-module `L`, such that `p^∗(L) = N_{d₁}(d_0^∗(A))`. Moreover, note
that for every `n ∈ ℕ^∗`, one has `p^∗(L^n) = N_{d₁}(d_0^∗(A^n))`, cf. loc. cit., (6.5.2.1).

Let us show that `L` is ample for the morphism `π : Y → S`. For this, replacing `S` by an affine open, we may suppose
`S` affine. Let then `y ∈ Y`, `x ∈ X₀` with `p(x) = y`, `V` an affine open of `Y` containing `y`, and `U = p⁻¹(V)`.
Since `A` is `π₀`-ample, there exists `n ∈ ℕ^∗` and a section `s ∈ Γ(X₀, A^n)` such that the open `(X₀)_s` satisfies
`x ∈ (X₀)_s ⊂ U`. With the preceding notations, `s` is given by sections `a_i ∈ A_{i,0} = O_{X₀}(U_i)` such that
`a_i = c_{ij} a_j` on `U_i ∩ U_j`, and `(X₀)_s` is the union of the opens `U′_i = {p ∈ Spec(A_{i,0}) | a_i ∉ p}`.

For each index `i`, put `N(a_i) = N_{δ₁}(δ_0(a_i)) ∈ B_i`. By 4.1 (i) and lemma 4.1.1, one has:

```text
   p(U′_i) = p d₁(d₀⁻¹(U′_i)) = p d₁({q ∈ Spec(A_{i,1}) | δ_{i,0}(a_i) ∉ q})
```

and `d₁({q ∈ Spec(A_{i,1}) | δ_{i,0}(a_i) ∉ q}) = {p ∈ Spec(A_{i,0}) | N_{δ₁}(δ_{i,0}(a_i)) ∉ p}`, whence

```text
   p(U′_i) = {p ∈ Spec(B_i) | N(a_i) ∉ p}.
```

It follows that `p((X₀)_s)` equals `Y_{N(s)}`, where we have written `N(s)` for the section of `L^n` over `Y` defined by
the sections `N(a_i) ∈ O_Y(V_i)`. One thus has

```text
(∗)   y ∈ p((X₀)_s) = Y_{N(s)} ⊂ p(U) = V.
```

This shows that `L` is ample for `π : Y → S`, which finishes showing that `π : Y → S` is quasi-projective.

<!-- original page 270 -->

## 6. Passage to the quotient when a quasi-section exists

<!-- label: III.V.6 -->

We shall now prove a lemma of technical character which will be useful in the proof of the two theorems we have in view.
Let `S` be a scheme and

```text
        d′₀, d′₁, d′₂      d₀, d₁
   X₂ ⇶ X₁ ⇉ X₀
```

a `(Sch/S)`-groupoid. We shall call a *quasi-section* of the groupoid `X∗` any subscheme `U` of `X₀` such that (1) and
(2) hold:

(1) The restriction `v` of `d₁` to `d₀⁻¹(U)` is a finite, locally free, and surjective morphism from `d₀⁻¹(U)` onto
`X₀`.

(2) Every subset `E` of `U` consisting of points pairwise equivalent for the equivalence relation defined by `X∗` (§
3.e)) is contained in an affine open of `U`.[^N.D.E-V-31]

If `U` is a quasi-section of `X∗`, the `(Sch/S)`-groupoid

```text
        u′₀, u′₁, u′₂      u₀, u₁
   U₂ ⇶ U₁ ⇉ U
```

<!-- original page 272 -->

induced by `X∗` and the inclusion of `U` into `X₀` (cf. § 3.a)) satisfies the hypotheses of theorem 4.1. Set indeed
`V = d₀⁻¹(U)` and let `u` and `v` be the morphisms with source `V` induced respectively by `d₀` and `d₁`:

```text
   X₀ ←─v── V ──u──→ U.
```

By paragraph 3.b), one has a Cartesian square

```text
                  
   U₁ ──────→ V
   │           │
u₁ │           │ v
   ↓           ↓
   U ─inclusion─→ X₀,
```

so `u₁` is surjective and finite locally free by (1). With (2), condition (1) therefore ensures that the groupoid `U∗`
satisfies the hypotheses of theorem 4.1. In particular `Coker(u₀, u₁)` exists in `(Sch/S)`. Moreover, `d₀` has a
section, so that `u` is a universal effective epimorphism (cf. III 1.12); it follows, by proposition 3.1, that
`Coker(u₀, u₁)` coincides with the cokernel `Coker(v₀, v₁)` of the groupoid `V∗`:

```text
        v′₀, v′₁, v′₂      v₀, v₁
   V₂ ⇶ V₁ ⇉ V,
```

inverse image of `U∗` under the base change `u : V → U`, that is also the inverse image of `X∗` under the base change:

```text
   V ──inclusion──→ X₁ ──d₀──→ X₀.
```

By paragraph 3.c), `V∗` is isomorphic to the groupoid `V′∗`, the inverse image of `X∗` under the base change:

```text
   v :  V ──inclusion──→ X₁ ──d₁──→ X₀,
```

and so `V′∗` admits a cokernel in `(Sch/S)`. Now, being flat, surjective and finite, `v : V → X₀` is faithfully flat and
quasi-compact, hence a universal effective epimorphism by III 6.3.2. Consequently, by proposition 3.1, the groupoid `X∗`
admits a cokernel `Coker(d₀, d₁)` in `(Sch/S)`. We have thus proved the first assertion of point (i) of the following
lemma:[^N.D.E-V-32]

<!-- original page 273 -->

**Lemma 6.1.** *Suppose that the `(Sch/S)`-groupoid `X∗` possesses a quasi-section. Then:*

<!-- label: III.V.6.1 -->

*(i) There exists a cokernel `(Y, p)` of `(d₀, d₁)` in `(Sch/S)`; moreover, such a `(Y, p)` is a cokernel of `(d₀, d₁)`
in the category of all ringed spaces.*

*(i′) `p` is surjective, and is open (resp. universally closed) if `d₀` is.*

*(ii) Suppose `S` locally Noetherian and `X₀` locally of finite type (resp. of finite type) over `S`. Then `p` and
`Y → S` are locally of finite presentation (resp. of finite presentation).*

*(iii) The morphism `X₁ → X₀ ×_Y X₀` with components `d₀` and `d₁` is surjective.*

*(iv) If `(d₀, d₁)` is an equivalence pair, then `X₁ → X₀ ×_Y X₀` is an isomorphism. Moreover, if `d₀ : X₁ → X₀` is
flat, `p` is faithfully flat.*

Before proving the second assertion of (i), we shall demonstrate (i′), (ii) and (iii).

**a)** Proof of (i′) and (ii):

We have just seen that `(Y, p)` identifies with `Coker(v₀, v₁)` and `Coker(u₀, u₁)`. Let then `q` and `r` be the
canonical epimorphisms from `U` and `V` into `Y`:

```text
   X₀ ←─v── V ──u──→ U
        ↘        ↙
         r     q
          ↘ ↙
           Y.
```

By hypothesis, `v` is surjective and finite locally free, hence open. On the other hand, if `d₀ : X₁ → X₀` is open
(resp. universally closed), then `u`, which is obtained from it by base change, is also.

<!-- original page 274 -->

Since, by theorem 4.1, `q` is surjective, integral, and open, it follows that `r` is surjective, and open (resp.
universally closed) if `d₀` is. The same therefore holds for `p`, since `v` is surjective. This proves (i′).

Suppose now `S` locally Noetherian and `X₀` locally of finite type over `S`, so that `X₀` is locally Noetherian.

Let us show that `Y` is locally of finite presentation over `S`. Let `S′ = Spec R` be an affine open of `S`,
`Y′ = Spec B` an affine open of `Y` projecting into `S′`, and `U′ = Spec A` the inverse image of `Y′` in `U`. Since `R`
is Noetherian, it suffices to show that `B` is a finitely generated `R`-algebra; but, by paragraphs 4 and 5, `B` is
contained in `A`, which is a finitely generated `R`-algebra; the assertion therefore follows from the fact that `R` is
Noetherian and `A` is integral over `B`.

Finally, since `X₀ → S` is locally of finite type, so is `p` (EGA I, 6.6.6), hence `p` is locally of finite presentation
since `Y` is locally Noetherian.

It remains to show the last assertion of (ii). Suppose in addition `X₀` of finite type over `S`. Then, since `p` is
surjective, `Y` is also quasi-compact over `S`, hence of finite type over `S`. Since `S` is locally Noetherian, then
`X₀ → S` and `Y → S` are of finite presentation, and so `p : X₀ → Y` is also (EGA IV_1, 1.6.2 (v)).

**b)** Proof of (iii):

Since the groupoid `V∗` with base `V` is isomorphic both to the inverse image of `U∗` under the base change `u` and to
the inverse image of `X∗` under the base change `v`, one has a double Cartesian square

```text
   X₁ ←──── V₁ ─────→ U₁
   │         │          │
d₀⊠d₁│     v₀⊠v₁│    u₀⊠u₁
   ↓         ↓          ↓
   X₀ ×_Y X₀ ←─── V ×_Y V ───→ U ×_Y U.
              v × v        u × u
```

Since `u₀ ⊠ u₁` is surjective, so is `v₀ ⊠ v₁`. Since `v × v` is surjective, so is the composite morphism
`V₁ → X₀ ×_Y X₀`, and therefore so is `d₀ ⊠ d₁`.

<!-- original page 275 -->

**c)** Proof of (i):

It remains to prove that `(Y, p)` is a cokernel of `(d₀, d₁)` in the category of all ringed spaces. We first show that
`Y` is obtained from `X₀` by identifying the points `x` and `y` such that there exists `z ∈ X₁` with `d₀(z) = x` and
`d₁(z) = y`. Indeed, `p` is surjective and one has `p d₀ = p d₁`; moreover, if `p(x) = p(y)`, there is a point `z′` of
`X₀ ×_Y X₀` whose first projection is `x` and second projection is `y`. If `z` is a point of `X₁` such that
`(d₀ ⊠ d₁)(z) = z′`, one indeed has `d₀(z) = x` and `d₁(z) = y`.

On the other hand, if `W` is a saturated open of `X₀`, then `W ∩ U` is a saturated open of `U`; by 4.1, `q(W ∩ U)` is an
open of `Y`. Since `q(W ∩ U)` is none other than `p(W)`, one sees that `Y` is endowed with the quotient topology of that
of `X₀`.

It remains to show that the canonical sequence of sheaves of rings

```text
   O_Y → p_∗(O_{X₀}) ⇉ p_∗ d_{0∗}(O_{X₁}) = p_∗ d_{1∗}(O_{X₁})
```

is exact.

Let then `Y′` be an open of `Y` and put `U′ = q⁻¹(Y′)`, `X′₀ = p⁻¹(Y′)`, etc.[^N.D.E-V-33] Then `U′` is an open of `U`
saturated for the equivalence relation defined by the groupoid `U∗`, and it follows from lemmas 1.1 and 1.2 that `Y′` is
the cokernel, in `(Sch/S)` and in `(Esp.An)`, of the groupoid induced by `U∗` on `U′`. Similarly, `X′₀` is an open of
`X₀` saturated for the equivalence relation defined by `X∗`, and one has the following commutative diagram, where the
two squares are Cartesian:

```text
              d̃₁                              d̃₀
   X′₀ ←─── V′ = d₀⁻¹(U′) ────→ U′
   │              │                  │
   │              │                  │
   ↓              ↓                  ↓
   X₀ ←──── V = d₀⁻¹(U) ────→ U′.
              d₁                       d₀
```

Then `d̃₁` is surjective, and finite locally free. On the other hand, let `x ∈ U′`. Since `U` is a quasi-section, the
set `E := d₀ d₁⁻¹(x) ∩ U` is finite and contained in an affine open `W` of `U`. Then `E′ = E ∩ U′` is a finite set,
contained in the quasi-affine open `W ∩ U′`. Consequently, there exists an affine open `W′` of `W ∩ U′` containing `E′`.
This shows that `U′` is a quasi-section of the groupoid `X′∗` induced by `X∗` on `X′₀`. The first assertion of (i),
applied to `X′∗` and `U′`, then shows that `Y′` is the cokernel in `(Sch/S)` of `X′∗`.

In particular, for every `S`-scheme `T`, one has the exact sequence

```text
                  T(p|_{X′₀})              T(d₁|_{X′₁})
   T(Y′) ────────→ T(X′₀) ⇉ T(X′₁).
                                      T(d₀|_{X′₁})
```

<!-- original page 276 -->

Now, if `T` is the "affine line" `G_{a,S}` (I 4.3), this sequence identifies with the sequence

```text
                                          δ₁
   Γ(Y′, O_Y) → Γ(p⁻¹(Y′), O_{X₀}) ⇉ Γ(d₀⁻¹ p⁻¹(Y′), O_{X₁}) = Γ(d₁⁻¹ p⁻¹(Y′), O_{X₁})
                                          δ₀
```

which is therefore exact for every open `Y′`. This completes the proof of 6.1 (i).

**d)** Proof of (iv):

If `(d₀, d₁)` is an equivalence pair, the same holds for `(u₀, u₁)`. It follows that `u₀ ⊠ u₁ : U₁ → U ×_Y U` is an
isomorphism (theorem 4.1), hence so is `v₀ ⊠ v₁` (confer the Cartesian squares of b)); since `v × v` is faithfully flat
and quasi-compact, `d₀ ⊠ d₁` is an isomorphism (SGA 1, VIII 5.4).

Moreover, if `d₀` is flat, so is `u`. Now `q` is flat, by theorem 4.1, so `r` also is. Since `v` is faithfully flat,
then `p` is flat, and therefore faithfully flat since surjective.

## 7. Quotient by a proper and flat groupoid

<!-- label: III.V.7 -->

**Theorem 7.1.**[^N.D.E-V-34] *Let `S` be a locally Noetherian scheme and*

<!-- label: III.V.7.1 -->

```text
        d′₀, d′₁, d′₂      d₀, d₁
   X₂ ⇶ X₁ ⇉ X₀
```

*a `(Sch/S)`-groupoid such that `d₁` is proper and flat, `X₀` is quasi-projective over `S`,*[^N.D.E-V-35] *and the
morphism `d : X₁ → X₀ ×_S X₀` with components `d₀` and `d₁` is quasi-finite. Then:*

*(i) There exists a cokernel `(Y, p)` of `(d₀, d₁)` in `(Sch/S)`; moreover, such a `(Y, p)` is a cokernel of `(d₀, d₁)`
in the category of all ringed spaces.*

<!-- original page 277 -->

*(ii) `p` is surjective, open, proper, of finite presentation, and `Y → S` is of finite presentation and
separated.*[^N.D.E-V-36]

*(iii) The morphism `X₁ → X₀ ×_Y X₀` with components `d₀` and `d₁` is surjective.*

*(iv) If `(d₀, d₁)` is an equivalence pair, then `X₁ → X₀ ×_Y X₀` is an isomorphism and `p` is faithfully
flat.*[^N.D.E-V-37] *Moreover, `(Y, p)` is a cokernel of `(d₀, d₁)` in the category of sheaves for the (fppf) topology
and, for every base change `Y′ → Y`, `Y′` is the cokernel of the groupoid `X∗ ×_Y Y′` obtained from `X∗` by the base
change `X₀ ×_Y Y′ → X₀`.*

*In particular, for every base change `S′ → S`, `Y′ = Y ×_S S′` is the cokernel of the `S′`-groupoid `X′∗ = X∗ ×_S S′`.
So, in this case, "the formation of the quotient commutes with base change".*

Let `(Y, p)` be the cokernel of `(d₀, d₁)` in the category of all ringed spaces. Lemma 1.2 shows that, to prove (i), it
suffices to show that every point `z` of `X₀` possesses a saturated open neighborhood `U_z` such that, denoting by `d̃₀`
and `d̃₁` the restrictions of `d₀` and `d₁` to `d₀⁻¹(U_z) = d₁⁻¹(U_z)`, and by `(Q, q)` the cokernel of `(d̃₀, d̃₁)` in
`(Esp.An)`, `Q` is a scheme and `q` a morphism of schemes.

By lemma 6.1 (i), it therefore suffices to show that every point `z` of `X₀` possesses a saturated open neighborhood
`U_z` such that the groupoid induced on `U_z` by `X∗` possesses a quasi-section. One can even suppose that `z` is closed
in its fiber over `S` (we shall say that `z` is *closed relative to `S`*).[^N.D.E-V-38] The existence of `U_z` then
follows from the lemmas below:

<!-- original page 275 -->

**Lemma 7.2.** *Let `T` be an affine Noetherian scheme, `X`, `Y`, and `Z` `T`-schemes of finite type, with `X`
quasi-projective over `T`, and*

<!-- label: III.V.7.2 -->

```text
   Y ──u──→ X
   │         ⋮
v  │         ⋮
   ↓         ↓
   Z ⋯⋯⋯⋯→ T
```

*a diagram in `(Sch/T)`. Let `z` be a point of `v(Y)` that is closed relative to `T` and such that `v` is flat at the
points of `v⁻¹(z)`. Then there exists a closed subscheme `F` of `X` such that `u(u⁻¹(F) ∩ v⁻¹(z))` is finite and
non-empty, and such that the restriction of `v` to `u⁻¹(F)` is flat at the points of `v⁻¹(z)`.*

Let `T = Spec A`. One may suppose `X` of the form `Proj S`, where `S` is the symmetric algebra of a finitely generated
`A`-module `E`.

If `u(v⁻¹(z))` is finite, one can choose `F` equal to `X`. Otherwise, we denote by `y₁, …, y_n`

<!-- original page 278 -->

the points of the fiber `v⁻¹(z)` associated with the structure sheaf `O_{v⁻¹(z)}` of `v⁻¹(z)` (the `y_i` are such that,
if `O_i` denotes the local ring of `v⁻¹(z)` at `y_i`, the maximal ideal of `O_i` consists of zero divisors). If `t` is
the image of `z` in `T`, `u(v⁻¹(z))` is an infinite constructible subset of the fiber of `t` in `X`. There therefore
exists a point `x` closed in this fiber, belonging to `u(v⁻¹ z)` and distinct from `u(y₁), …, u(y_n)`. Then `X − {x}` is
an open neighborhood of `u(y₁), …, u(y_n)`, hence contains an open neighborhood of the form `D_+(f)`, where `f` is a
homogeneous element of degree `d` of `S` (the notations are those of EGA II, § 2.3).

Consequently, the closed subscheme `X₁ = V_+(f)` defined by `f` contains `x` and avoids the points `u(y₁), …, u(y_n)`.
It follows of course that the inverse image `Y₁ = u⁻¹(V_+(f))` of this subscheme is distinct from `Y` and meets
`v⁻¹(z)`. We shall further show that the restriction `v₁` of `v` to `Y₁` is flat at the points of `v⁻¹(z)`; if
`u(v₁⁻¹(z))` is finite, we shall therefore only need to choose `F` equal to `X₁`; otherwise, we shall repeat the
argument we have just developed, replacing `Y` by `Y₁`, `v` by `v₁`, `u` by the morphism `u₁` induced on `Y₁` by `u`; in
this way we shall obtain a decreasing sequence `X, X₁, …` of closed subschemes of `X`; since such a sequence terminates,
`u(u⁻¹(X_n) ∩ v⁻¹(z))` will be finite and non-empty for some `n`, and one will choose `F` equal to `X_n`.

It remains then to show that `v₁` is flat at the points of `v⁻¹(z)`; let `y` be a point of `Y₁` above `z`, `O_y` the
local ring of `y` in `Y`, `O̅_y` the local ring of `y` in `v⁻¹(z)`, `O_{v(y)}` the local ring of `v(y)` in `Z`. If
`g ∈ S_1` is such that `D_+(g)` is a neighborhood of `u(y)` in `X`, let `φ` be the image of `f/g^d` in `O_y` and `φ̅`
the image of `f/g^d` in `O̅_y`. It then follows from the construction of `f` that `φ̅` is not a zero divisor in `O̅_y`;
since

<!-- original page 276 -->

`O_y` is flat over `O_z`, `φ` is not a zero divisor in `O_y` and `O_y/O_y φ` is flat over `O_z` (SGA 1, IV 5.7). But
`O_y/O_y φ` is precisely the local ring of `y` in `Y₁`.

<!-- original page 279 -->

**Lemma 7.3.** *We keep the notations and hypotheses of 7.1. Every point `z` of `X₀` closed relative to `S` therefore
possesses a saturated open neighborhood `U_z` such that the groupoid induced by `X∗` on `U_z` possesses a
quasi-section.*

<!-- label: III.V.7.3 -->

The statement being local on `S`, one may suppose `S` affine Noetherian and apply the previous lemma to the diagram

```text
   X₁ ──d₀──→ X₀
   │           ⋮
d₁ │           ⋮
   ↓           ↓
   X₀ ⋯⋯⋯⋯→ S
```

of `(Sch/S)`. Let then `F` be a closed subscheme of `X₀` such that `d₀(d₀⁻¹(F) ∩ d₁⁻¹(z))` is finite and non-empty, and
such that the restriction of `d₁` to `d₀⁻¹(F)` is flat at the points of `d₁⁻¹(z)`.[^N.D.E-V-39]

Denote by `F₁` and `F₂` the inverse images of `F` under `d₀` and under `d₀ d′₀ = d₀ d′₁`, and denote by `d̃₀`, `d̃₁`,
etc., the morphisms induced by `d₀`, `d₁`, etc. One thus has a commutative diagram

```text
                d̃′₁              d̃₀
        F₂ ─────→ F₁ ─────→ F
                d̃′₀                ⋮ q̃
    d̃′₂│         │ d̃₁              ⋮
        ↓         ↓                 ↓
        X₁ ─────→ X₀ ⋯⋯⋯⋯→ S,
                d₁          q
                d₀
```

where the two left-hand squares are Cartesian and the first row is exact (confer (0,1,2), § 1), and where `q` and `q̃`
denote the structure morphisms.

Let us first show that there are only finitely many points of `F₁` above `z`.[^N.D.E-V-39] Indeed, let `s` be the image
of `z` in `S`; since `F` is of finite type over `S`, the fiber `q̃⁻¹(s)` is a Noetherian scheme. On the other hand,
since `d̃₀` is proper, `d̃₀(d̃₁⁻¹(z))` is a closed subscheme of `q̃⁻¹(s)`, consisting of finitely many points.
Consequently (cf. EGA I, 6.2.2), the points of this set are closed in `q̃⁻¹(s)`, and also (since `F` is closed in `X₀`)
in the fiber `q⁻¹(s)` of `s` in `X₀`. Let `y` be one of these points; since the fiber `q⁻¹(s)` is of finite type over
`κ(s)`, it contains affine open neighborhoods `Spec B` and `Spec C` of `y` and `z`, respectively, where `B` and `C` are
finitely generated `κ(s)`-algebras. Then `y` and `z` correspond to maximal ideals `p ⊂ B` and `q ⊂ C`, the fields `B/p`
and `C/q` are of finite degree over `κ(s)`, and so `(B/p) ⊗_{κ(s)} (C/q)` is a `κ(s)`-algebra of finite dimension, whose
maximal ideals correspond exactly to the points of `X₀ ×_S X₀` whose second (resp. first) projection is `z` (resp. `y`).
There are therefore only finitely many points `u` of `X₀ ×_S X₀` whose

<!-- original page 280 -->

second projection is `z` and whose first projection belongs to `d̃₀(d̃₁⁻¹(z))`. Finally, since `X₁ → X₀ ×_S X₀` has
finite fibers, such a point `u` comes from finitely many points of `X₁`, whence the desired assertion.

The morphism `d̃₁` is therefore quasi-finite and flat at the points of `F₁` above `z`. Since `d̃₁` is of finite type, it
follows from SGA 1, IV 6.10 and EGA III, 4.4.10,[^N.D.E-V-40] that the set `Φ` of points of `F₁` where `d̃₁` is not
simultaneously flat and quasi-finite is closed in `F₁`, hence in `X₁` (since `F₁` is closed in `X₁`). Since `d₁` is
proper, `d̃₁(Φ)` is closed, and does not contain `z` by what precedes. Put `W = d̃₁(F₁) − d̃₁(Φ)`. Then the restriction
of `d̃₁` to `d̃₁⁻¹(W)` is[^N.D.E-V-41] of finite presentation (in view of the Noetherian hypotheses), flat, proper and
quasi-finite, hence finite, locally free, and open, by EGA III, 4.4.2, and EGA IV_2, 2.1.12 and 2.4.6. Consequently,
`d̃₁(F₁)` is a neighborhood of `z`, and `W` is the largest open of `X₀` contained in `d̃₁(F₁)` above which `d̃₁` is
simultaneously flat and quasi-finite.

We shall see in lemma 7.4 that the inverse images of `Φ` by `d̃′₁` and `d̃′₀` both identify with the set of points of
`F₂` where `d̃′₂` is not simultaneously flat and quasi-finite. It follows that `d₀⁻¹(W) = d̃′₂(F₂) − d̃′₂(d̃′₀ Φ)`
coincides with `d₁⁻¹(W) = d̃′₂(F₂) − d̃′₂(d̃′₁ Φ)`, that is, `W` is saturated. Consequently, setting `W₁ = d̃₁⁻¹(W)`,
the equality `d₀⁻¹(W) = d₁⁻¹(W)` entails `d̃′₂ d̃′₀⁻¹(W) = d̃′₂ d̃′₁⁻¹(W)`, that is, `d̃′₀⁻¹(W₁) = d̃′₁⁻¹(W₁)`. Since
`d̃₀` is faithfully flat and quasi-compact (because `d₀` is, like `d₁`, surjective, proper and flat), and the square

```text
              d̃′₁
       F₂ ─────→ F₁
       │          │
   d̃′₀│          │ d̃₀
       ↓          ↓
       F₁ ─────→ F
              d̃₀
```

is Cartesian, it follows that `W₁` is of the form `d̃₀⁻¹(U)`, where `U` is an open of `F`

<!-- original page 281 -->

(SGA 1, VIII 4.4). This open `U` of `F` is a quasi-section for the groupoid with base `W` induced by `X∗`. One can
therefore choose `U_z` equal to `W`.

It remains for us therefore to state lemma 7.4, whose proof is classical:

**Lemma 7.4.** *Consider a Cartesian square of schemes*

<!-- label: III.V.7.4 -->

```text
   F₂ ──v──→ F₁
   │           │
d′ │           │ d
   ↓           ↓
   X₁ ──u──→ X₀
```

*and let `x` be a point of `F₂`.*

*(i) If `u` is flat, `d′` is flat at `x` if and only if `d` is flat at `v(x)`.*

*(ii) If `d` is locally of finite type, `d′` is quasi-finite at `x` if and only if `d` is quasi-finite at
`v(x)`.*[^N.D.E-V-42]

We have thus proved that there exists a covering of `X₀` by saturated opens `W` such that the groupoid `W∗` induced by
`X∗` on `W` possesses a quasi-section.[^N.D.E-V-43]

By lemma 6.1 and the reductions stated after theorem 7.1, this implies assertions (i) and (iii) of theorem 7.1, and the
fact that `p` is surjective and open, and that `p` and `Y → S` are locally of finite presentation. Moreover, since
`X₀ → S` is quasi-projective, hence separated and of finite type, then `p` is separated, and the proof of point (ii) of
lemma 6.1 shows that `p` and `Y → S` are of finite presentation.

To show that `p` is proper, it remains therefore to show that it is universally closed. As the assertion is local on
`Y`, one may place oneself on a saturated open `W` such that the groupoid `W∗` induced by `X∗` on `W` possesses a
quasi-section `U` (since `X₀` is covered by such opens). Taking up the notations of 6.a), one has a commutative diagram

```text
   W ←─v── V ──u──→ U
       ↘        ↙
        r     q
         ↘ ↙
          Z,
```

where `Z` is an open of `Y`, all the arrows are surjective, and `q` is integral. Moreover, by hypothesis, `d₀ : X₁ → X₀`
is proper, so `u`, obtained from it by base change, is also. Consequently, `r` is universally closed, and so is `p`,
since `v` is surjective.

Finally, `p` being surjective and universally closed, and `X₀` quasi-projective hence separated, the diagonal
`Δ_{Y/S}(Y)` is closed in `Y ×_S Y`, being the image under `p × p` of the diagonal `Δ_{X₀/S}(X₀)`. So `Y` is separated
over `S`. This completes the proof of 7.1 (ii).

The assertions to prove in 7.1 (iv) are local on `Y`; since `X₀` is covered by the saturated opens `U_z`, it suffices to
verify these assertions by replacing `X` and `Y` by `U_z` and `V = p(U_z)`. As one has already seen at the beginning of
the proof of 7.1, it follows from lemmas 1.1, 1.2, and 6.1 (i), that `(V_z, p|_{U_z})` is the cokernel in `(Sch)` and in
`(Esp.An)` of the groupoid induced by `X∗` on `U_z`. Now the hypothesis that

<!-- original page 282 -->

`d = (d₀, d₁)` is a monomorphism is preserved by the base change `U_z → X₀`. Consequently, the first two assertions of
7.1 (iv) follow from 6.1 (iv).

Let us finally show the consequences indicated at the end of point (iv) (cf. [Ray67a], th. 1 (iii)). By hypothesis, the
groupoid `X∗` comes from an equivalence relation `R → X₀ × X₀`, and one has established that `R` is effective (cf. Exp.
IV, 3.3.2) and that `p : X₀ → Y = X₀/R` is faithfully flat and of finite presentation. Consequently, denoting by `(M)`
the family of faithfully flat morphisms locally of finite presentation, `R` is `(M)`-effective. Therefore, by Exp. IV,
6.3.3, `(Y, p)` represents the quotient sheaf of `X₀` by `R` for the (fppf) topology, and the assertions concerning base
change follow from IV, 3.4.3.1.

## 8. Passage to the quotient by a flat, not necessarily proper, groupoid

<!-- label: III.V.8 -->

**Theorem 8.1.**[^N.D.E-V-44] *Let `S` be a Noetherian scheme and*

<!-- label: III.V.8.1 -->

```text
        d′₀, d′₁, d′₂      d₀, d₁
   X₂ ⇶ X₁ ⇉ X₀
```

*a `(Sch/S)`-groupoid such that `d₁` is flat and of finite type, `X₀` is of finite type over `S`, and the morphism
`X₁ → X₀ ×_S X₀` with components `d₀` and `d₁` is quasi-finite.*

<!-- original page 282 -->

*There then exists an open `W` of `X₀` which is dense, saturated, and satisfies the following properties:*

*(i) If `W₂ ⇶ W₁ ⇉ W` (with arrows `w′_i, w_j`) is the groupoid induced by `X∗` on `W`, then `(w₀, w₁)` admits a
cokernel `(V, p)` in `(Sch/S)`; moreover, `(V, p)` is a cokernel of `(w₀, w₁)` in the category of all ringed spaces.*

*(ii) `p` is surjective and open.*

*(ii′) `p` and `V → S` are of finite presentation.*

*(iii) The morphism `W₁ → W ×_V W` with components `w₀` and `w₁` is surjective.*

*(iv) If `(d₀, d₁)` is an equivalence pair, `W₁ → W ×_V W` is an isomorphism and `p` is faithfully flat.*

<!-- original page 280 -->

We shall show that one can choose `W` in such a way that the `(Sch/S)`-groupoid `W∗` induced by `X∗` possesses a
quasi-section (confer § 7). Theorem 8.1 will then follow from lemma 6.1.

Suppose provisionally that, for every point `z ∈ X₀` closed relative to `S` (confer § 7), there exists a saturated open
`W_z` which possesses a quasi-section and meets all the irreducible components of `X₀` passing through `z`. Then the
exterior `X₀ − W_z` of `W_z` in `X₀` is saturated (since the saturation `d₁(d₀⁻¹(X₀ − W_z))` of this exterior is open
and does not meet `W_z`). If this exterior is non-empty, one can choose in it a point `z′` closed relative to `S` and
associate to `z′` an open `W_{z′}` as above; one may moreover suppose `W_{z′}` contained in `X₀ − W_z`; then `W_z` and
`W_{z′}` are disjoint and the groupoid induced by `X∗` on `W_z ∪ W_{z′}` possesses a quasi-section. The process must
stop, because `X₀` has only finitely many irreducible components. It therefore remains to construct `W_z`.

For this, one may suppose `S` affine; in this case, let `y` be a point of `X₁`

<!-- original page 283 -->

such that `d₁(y) = z`, `X` an affine open of `X₀` containing `d₀(y)`, `Y` the inverse image of `X` in `X₁` under `d₀`,
and finally `u : Y → X` and `v : Y → X₀` the morphisms induced by `d₀` and `d₁`. Since `X` is affine, hence
quasi-projective, one can apply lemma 7.2: there is therefore a closed subscheme `F` of `X₀` such that
`d₀⁻¹(F) ∩ d₁⁻¹(z)` is non-empty, `d₀(d₀⁻¹(F) ∩ d₁⁻¹(z))` is finite, and the restriction of `d₁` to `d₀⁻¹(F)` is flat at
the points of `v⁻¹(z)`. This allows us to take up the notations of lemma 7.3, denoting by `F₁` and `F₂` the inverse
images of `F` in `X₁` and `X₂`, etc.

```text
                d̃′₁              d̃₀
        F₂ ─────→ F₁ ─────→ F
                d̃′₀
    d̃′₂│         │ d̃₁
        ↓         ↓
        X₁ ─────→ X₀.
                d₁
                d₀
```

One then shows as in 7.3 that `d̃₁` is quasi-finite at the points of `d̃₁⁻¹(z)`, so that it is natural to consider the
open `F′₁` of `F₁` consisting of points where `d̃₁` is simultaneously flat and quasi-finite. By 7.4, the two inverse
images of `F′₁` under `d̃′₁` and `d̃′₀` consist of the points of `F₂` where `d̃′₂` is flat and quasi-finite, so these
two inverse images coincide, and `F′₁` is of the form `d̃₀⁻¹(F′)`, where `F′` is an open of `F`

(SGA 1, VIII 4.4). Possibly replacing `F` by `F′`, one may therefore suppose that `d̃₁` is quasi-finite and flat. In
this case, we denote by `W_z` the largest open of `d̃₁(F₁)` above which `d̃₁` is finite and flat.

This open `W_z` does not necessarily contain `z`, but it contains the generic points of the irreducible components of
`X₀` passing through `z`.[^N.D.E-V-45] Since `d₀` (resp. `d₁`) is faithfully flat and of finite presentation (hence
open), it then follows from SGA 1, VIII 5.7, that `d₀⁻¹(W_z)` and `d₁⁻¹(W_z)` both coincide with the largest open of
`d̃′₂(F₂)` above which `d̃′₂` is finite and flat. One sees consequently as in 7.3 that the two inverse images of
`d̃₁⁻¹(W_z)` under `d̃′₀` and `d̃′₁` coincide, so that `d̃₁⁻¹(W_z)` is of the form `d̃₀⁻¹(U)` where `U` is an open of
`F` which is a quasi-section for the groupoid induced by `X∗` on `W_z`.

## 9. Elimination of the Noetherian hypotheses in theorem 7.1

<!-- label: III.V.9 -->

<!-- original page 284 -->

**a)** We take up the notations and hypotheses of lemma 6.1 and let `π : S′ → S` be an arbitrary base change. Denote by
`f′ : X′ → Y′` the morphism of `S′`-schemes deduced by extension via `π` of the base from a morphism of `S`-schemes
`f : X → Y`. With this convention, `p′ : X′₀ → Y′` is surjective, as is the morphism `X′₁ → X′₀ ×_{Y′} X′₀` with
components `d′₀` and `d′₁`. The set underlying `Y′` therefore identifies with the quotient of the set underlying `X′₀`
by the equivalence relation defined in `X′₀` by the `S′`-groupoid `X′∗`. Moreover, `q′ : U′ → Y′` is integral and
surjective, so that the topology of `Y′` is the quotient topology of that of `U′`, hence also of that of `X′₀` (confer
the proof in § 6.c).

On the other hand, it is clear that `U′` is a quasi-section of the `S′`-groupoid `X′∗`, to which one can therefore apply
lemma 6.1. In particular, `X′∗` possesses a cokernel `(Y_1, p_1)` and the topological space underlying `Y_1` is obtained
from the topological space underlying `X′₀` by identifying the points equivalent under the relation defined by `X′∗`. It
follows that the canonical morphism `Y_1 → Y′` is a homeomorphism; I claim that `Y_1 → Y′` is even a universal
homeomorphism: indeed, if `S′′` is above `S′`, let `Y_2` be the cokernel of `(d₀ ×_S S′′, d₁ ×_S S′′)`. By what
precedes, applied to the base changes `S′′ → S′` and `S′′ → S`,

```text
   Y_2 ──→ Y_1 ×_{S′} S′′    and    Y_2 ──→ Y ×_S S′′ ≃ Y′ ×_{S′} S′′
```

are homeomorphisms, so the same holds for `Y_1 ×_{S′} S′′ → Y′ ×_{S′} S′′`.

**b)** Analogous remarks evidently apply to the case where the groupoid `X∗` "locally" possesses quasi-sections (confer
the proof of theorem 7.1).[^N.D.E-V-46] For example, one has the following theorem:

<!-- original page 285 -->

**Theorem 9.0.** *Let `S` be an arbitrary scheme and `X₂ ⇶ X₁ ⇉ X₀` a `(Sch/S)`-groupoid (with arrows `d′_i` and `d_j`)
such that: `X₀` is of finite presentation and quasi-projective over `S`, `d₁` is of finite presentation, proper and
flat, the morphism `d₀ ⊠ d₁ : X₁ → X₀ ×_S X₀` is quasi-finite. Then:*

<!-- label: III.V.9.0 -->

*(1) Every point `x` of `X₀` has an open neighborhood `W` that is saturated and such that the groupoid induced by `X∗`
on `W` possesses a quasi-section.*

*(2) Let `(Y, p)` be the cokernel of `(d₀, d₁)` in the category of all ringed spaces. Then `Y` is a scheme, `p` a
morphism of schemes, and `(Y, p)` is a cokernel of `(d₀, d₁)` in `(Sch/S)`.*

*(3) `p` is surjective, open and universally closed.*

*(4) The morphism `d : X₁ → X₀ ×_Y X₀` with components `d₀` and `d₁` is surjective.*

*(5) If `(d₀, d₁)` is an equivalence pair, then:*

*(a) `d : X₁ → X₀ ×_Y X₀` is an isomorphism and `p` is faithfully flat.*

*(b) `p` and `Y → S` are of finite presentation, and `(Y, p)` is a cokernel of `(d₀, d₁)` in the category of sheaves for
the (fppf) topology.*

*Proof.* For (1), the question is local on `S`, so one may suppose `S = Spec B` affine. There then exists a ring `A` of
finite type over `ℤ`, a morphism `S → T = Spec A` and a `(Sch/T)`-groupoid `Z∗` such that `X∗` identifies with
`Z∗ ×_T S` (cf. EGA IV_3, 8.8.3, applied to `S₀ = Spec ℤ` and `S_i = Spec A_i`, with the `A_i` running over the finitely
generated `ℤ`-subalgebras of `B`). Moreover, one may suppose that `Z∗` satisfies the hypotheses of theorem 7.1 (cf. EGA
IV_3, 8.10.5). Consequently, `Z∗` "locally" possesses quasi-sections.

The same therefore holds for `X∗`, by a), and assertions (2), (3), (4) and (5) (a) follow from 6.1, as in the proof of
7.1.

**c)** Let us show that `Y → S` is of finite presentation.[^N.D.E-V-47] By hypothesis, `(d_0^{X∗}, d_1^{X∗})` is an
equivalence pair, that is, `d^{X∗} : X₁ → X₀ ×_S X₀` is a monomorphism. By EGA IV_3, 8.10.5, one may suppose, possibly
enlarging `A`, that `d^{Z∗} : Z₁ → Z₀ ×_T Z₀` is a monomorphism. Since `T = Spec A`, with `A` Noetherian, it then
follows from theorem 7.1 that the groupoid `Z∗` possesses a cokernel `(Q, q)` in `(Sch/T)`, that `q` and `Q → T` are of
finite presentation, and moreover that `q : Z₀ → Q` is faithfully flat and that `d^{Z∗}` induces an isomorphism
`Z₁ ⥲ Z₀ ×_Q Z₀`. Put `Q_S = Q ×_T S`.

Since `X_i ≅ Z_i ×_T S`, one therefore obtains an isomorphism:

```text
   d^{Z∗} ×_T S : X₁ ⥲ X₀ ×_{Q_S} X₀.
```

Denote its inverse by `φ`, and let `π` be the canonical morphism

```text
   X₀ ×_Y X₀ ⟶ X₀ ×_{Q_S} X₀.
```

<!-- original page 283 -->

Then `φ ∘ π` is the inverse of `d₀ ⊠ d₁ : X₁ ⥲ X₀ ×_Y X₀`. It follows that the equivalence relation defined by `X∗`,
that is, the monomorphism

```text
   X₁ ──d₀⊠d₁ (≅)──→ X₀ ×_Y X₀ ──→ X₀ ×_S X₀,
```

identifies with the equivalence relation `R(q_S)` defined by the morphism `q_S : X₀ → Q_S`. Since the latter is
faithfully flat and of finite presentation, hence a universal effective epimorphism, `R(q_S)` has quotient `Q_S` (cf. IV
3.3.2). Consequently, `Y ≅ Q ×_T S`, so `Y → S` and `p` are of finite presentation. Moreover, by IV 6.3.3, `(Y, p)` is
also a cokernel of `(d₀, d₁)` in the category of sheaves for the (fppf) topology.

**Proposition 9.1.** *Consider morphisms of schemes*

<!-- label: III.V.9.1 -->

```text
   X₀ ──p──→ Y ──q──→ S
```

*such that `qp` is of finite type (resp. of finite presentation) and `p` is faithfully flat of finite presentation. Then
`q` is of finite type (resp. of finite presentation)[^V-9-1].*

Since `p` is surjective and `qp` quasi-compact, `q` is quasi-compact. So one may suppose `S`, `Y` and `X₀` affine, with
rings `A`, `B`, `C`. One has `B = lim B_i`, where the `B_i` run over the finitely generated `A`-subalgebras of `B`.
Since `C` is of finite presentation over `B`, there exists an index `i₀`, a `B_{i₀}`-algebra of finite presentation
`C_{i₀}`, and an isomorphism `C ≃ C_{i₀} ⊗_{B_{i₀}} B`; if we put `C_i = C_{i₀} ⊗_{B_{i₀}} B_i` for `i ⩾ i₀`, we
therefore have `C ≃ C_i ⊗_{B_i} B`.

```text
        B ────→ C
        ↑       ↑
        B_i ──→ C_i
        ↑
        A
```

Since `C` is faithfully flat over `B`, one extracts from EGA IV_3, 11.2.6 and 8.10.5 (vi) the existence of an `i_1 ⩾ i₀`
such that `C_{i_1}` is faithfully flat over `B_{i_1}`; consequently `C_i` is faithfully flat over `B_i` for `i ⩾ i_1`.
For `i ⩾ i_1`, the canonical map `C_i → C` is then injective, since deduced from `B_i → B` by faithfully flat extension
of the base.

<!-- original page 286 -->

If `C` is of finite type over `A`, it follows that there exists an index `j ⩾ i_1` such that `C_j = C`, whence
`B_j = B`, since `C_j` is faithfully flat over `B_j`. Consequently, `B` is of finite type over `A`.

Suppose now `C` of finite presentation over `A`. By what precedes, `B` is of finite type over `A`, hence of the form
`B̅/I` where `B̅` is a polynomial algebra over `A` in a finite number of indeterminates, and `I` an ideal of `B̅`. Then
`I` is the union of its finitely generated subideals `I_α`; whence the equality `B = lim B_α` with `B_α = B̅/I_α`.
Proceeding as above, there exists an index `α₀`, a `B_{α₀}`-algebra of finite presentation `C_{α₀}`, and an isomorphism
`C ≃ C_{α₀} ⊗_{B_{α₀}} B`. For `α ⩾ α₀`, one again sets `C_α = C_{α₀} ⊗_{B_{α₀}} B_α` so that one has
`C ≃ C_α ⊗_{B_α} B` for `α ⩾ α₀`. Again by EGA IV_3, 11.2.6 and 8.10.5 (vi), one concludes as above that `C_α` is
faithfully flat over `B_α` for `α` large enough. In this case, the kernel of the map `C_α → C` (resp. `C_α → C_β` for
`β ⩾ α`) identifies with `C_α ⊗_{B_α} (I/I_α)` (resp. with `C_α ⊗_{B_α} (I_β/I_α)`).

Since `C_α` and `C` are of finite presentation over `A` and `C_α → C` is surjective, `C_α ⊗_{B_α} (I/I_α)` is a finitely
generated ideal[^N.D.E-V-48] and is the union of the ideals `C_α ⊗_{B_α} (I_β/I_α)`. One therefore has
`C_α ⊗_{B_α} (I_β/I_α) = C_α ⊗_{B_α} (I/I_α)` for `β` large enough, whence also `I_β = I` (since `C_α` is faithfully
flat over `B_α`); so `B` is of finite presentation over `A`.

## 10. Complement: quotients by a group scheme

<!-- label: III.V.10 -->

The following §§ 10.2–10.4, written following indications of M. Raynaud, aim to apply the preceding theorems to the case
of an action of a group scheme. For the reader's convenience, we have begun by reproducing, in § 10.1, statements 2.1 to
2.3 of Exp. XVI.

### 10.1. Representability theorems for quotients.

<!-- label: III.V.10.1 -->

"Recall" first the following result:

**Theorem 10.1.1.** *Let `S` be a scheme, `X` and `Y` two `S`-schemes, `f : X → Y` an `S`-morphism. Suppose that one is
in one of the following two cases:*

<!-- label: III.V.10.1.1 -->

*α) The morphism `f` is locally of finite presentation.*

*β) The scheme `S` is locally Noetherian and `X` is locally of finite type over `S`.*

*Then the following conditions are equivalent:*

*(i) There exists an `S`-scheme `X′` and a factorization of `f`:*

```text
   f : X ──f′──→ X′ ──f′′──→ Y,
```

*where `f′` is a faithfully flat `S`-morphism locally of finite presentation and `f′′` is a monomorphism.*

*(ii) The (first) projection:*

```text
   p_1 : X ×_Y X ⟶ X
```

*is a flat morphism.*

*Moreover, if the preceding conditions are realized, `(X′, f′)` is a quotient of `X` by the equivalence relation defined
by `f` (for the (fppf) topology), so that the factorization `f = f′′ ∘ f′` of i) is unique up to isomorphism.*

The case `Y` locally Noetherian, `X` of finite type over `Y`, is treated in [Mur65], cor. 2 of th. 2. We shall see that
one can reduce to this case.

Let us first make a few remarks:

<!-- original page 285 -->

**a)** The implication (i) ⇒ (ii) is trivial. Indeed, the first projection

```text
   p′_1 : X ×_{X′} X ⟶ X
```

factors through `X ×_Y X`:

```text
   p′_1 : X ×_{X′} X ──u──→ X ×_Y X ──p_1──→ X.
```

The morphism `u` is an isomorphism, since `f′′` is a monomorphism, and `p′_1` is flat, since `f′` is flat, so `p_1` is
flat.

**b)** The assertions of 10.1.1 are local on `Y` (hence local on `S`); they are also local on `X`, as follows easily
from the fact that a flat morphism locally of finite presentation is open (EGA IV_3, 11.3.1).

**c)** Under the hypotheses of 10.1.1 α), in view of what precedes, we are reduced to the case where `X` and `Y` are
affine and `f` of finite presentation. Possibly replacing `S` by `Y`, one may suppose `X` and `Y` of finite presentation
over `S`. One then reduces to the case `S` Noetherian thanks to EGA IV_3, 11.2.6.

**d)** Under the hypotheses of 10.1.1 β), one may suppose `S`, `X`, `Y` affine, `S` Noetherian and `X` of finite type
over `S`. Consider `Y` as filtered inverse limit of affine schemes `Y_i` of finite type over `S`. The schemes
`X ×_{Y_i} X` form a filtered decreasing family of closed subschemes of `X ×_S X`, whose inverse limit is `X ×_Y X`.
Since `X ×_S X` is Noetherian, one has `X ×_{Y_i} X = X ×_Y X` for `i` large enough, so that `f_i : X → Y → Y_i`
satisfies the hypotheses of 10.1.1 ii) if `f` does. Since the equivalence relation defined by `f` on `X` coincides with
that defined by `f_i`, it is clear that it suffices to prove ii) ⇒ i) for `f_i`, which reduces us to the case where `Y`
is of finite type over `S`.

*Application to group schemes.* Let `S` be a scheme, `G` an `S`-group scheme locally of finite presentation over `S`,
acting (on the left) on an `S`-scheme `X`. If `X → S` possesses a section `ξ`, recall that the stabilizer `Stab_G(ξ)` is
representable by a subgroup scheme of `G` (cf. I, 2.3.3).

**Theorem 10.1.2.** *Let `S` be a scheme, `G` an `S`-group scheme locally of finite presentation over `S`, acting on an
`S`-scheme `X`.*

<!-- label: III.V.10.1.2 -->

*One assumes that `X → S` possesses a section `ξ`, such that the stabilizer `H` of `ξ` in `G` is flat over `S`. If one
of the following hypotheses is satisfied:*

*a) `X` is locally of finite type over `S`,*

*b) `S` is locally Noetherian,*

*then the quotient (fppf) sheaf `G/H` is representable by an `S`-scheme, locally of finite presentation over `S`, and
the `S`-morphism:*

```text
   f : G ⟶ X,   g ↦ g · ξ
```

<!-- original page 286 -->

*factors as:*

```text
        G
        │  ↘ f
      p │    ↘
        ↓      ↘
       G/H ──i──→ X,
```

*where `p` is the canonical projection, which is a faithfully flat morphism locally of finite presentation, and `i` is a
monomorphism.*

*Proof.* The morphism `f` makes `G` an `X`-scheme. By definition of the stabilizer of `ξ`, the morphism:

```text
   G ×_S H ⟶ G ×_X G,   (g, h) ↦ (g, gh)
```

is an isomorphism. Since `H` is flat over `S`, `G ×_S H` is flat over `G`, so the first projection `p_1 : G ×_S G → G`
is a flat morphism. Moreover, if `X` is locally of finite type over `S`, `f` is locally of finite presentation (EGA
IV_1, 1.4.3 (v)), and otherwise `S` is assumed locally Noetherian. It then suffices to apply 10.1.1 to the morphism `f`.
It remains to see that `G/H` is locally of finite presentation over `S`, but this follows immediately from 9.1.

**Corollary 10.1.3.** *Let `S` be a scheme, `u : G → H` a morphism of `S`-group schemes. Suppose `G` locally of finite
presentation over `S` and that either `H` is locally of finite type over `S`, or `S` is locally Noetherian.*

<!-- label: III.V.10.1.3 -->

*Then, if `K = Ker(u)` is flat over `S`, the quotient group `G/K` is representable by an `S`-group scheme locally of
finite presentation over `S`, and `u` factors as:*

```text
        G ──u──→ H
        │       ↗
      p │      ↗
        ↓     ↗ i
       G/K
```

*where `p` is the canonical projection and `i` a monomorphism.*

*Proof.* One applies 10.1.2 taking `X = H` and for `ξ` the unit section of `H`.

### 10.2. Stabilizer of the diagonal.

<!-- label: III.V.10.2 -->

Let `S` be a Noetherian scheme, `X` an `S`-scheme of finite type, and `G` a flat `S`-group scheme of finite type acting
on the left on `X`, i.e., one has an `S`-action `d₀ : G ×_S X → X`. Denote by `d₁ : G ×_S X → X` the projection onto the
second factor. Following § 2.a), one has the groupoid

```text
                  pr_{2,3}              d₁
   G ×_S G ×_S X      ⇉      G ×_S X         ⇉   X
                  μ × X                       d₀
                  G × d₀
```

whose cokernel, if it exists, is denoted `G\X`.

<!-- original page 287 -->

**Definition 10.2.1.** *We denote by `F ⊂ G ×_S X` the* stabilizer of the diagonal section, *i.e. the `X`-scheme defined
by the Cartesian product*

<!-- label: III.V.10.2.1 -->

```text
   F ─────→ X
   │         │ Δ
   ↓         ↓
   G ×_S X ──(d₀, d₁)──→ X ×_S X.
```

*Then `F` is an `X`-subgroup scheme of `G ×_S X`. Since `G ×_S X` is of finite type over `S` Noetherian, hence
Noetherian, `F` is of finite type over `S` and over `X` (EGA I, 6.3.5 and 6.3.6). Moreover, if `X → S` is separated, `F`
is a closed `X`-subgroup scheme of `G ×_S X`.*

Recall that one says that `G` *acts freely* on `X` if the morphism

```text
   G ×_S X ──(d₀, d₁)──→ X ×_S X
```

is a monomorphism (cf. Exp. III, 3.2.1). This amounts to saying that `F` is the trivial group scheme with base `X`.

### 10.3. Case where `F` is quasi-finite over `X`.

<!-- label: III.V.10.3 -->

Since `F` is of finite type over `X`, it is quasi-finite over `X` if and only if the fixators of the geometric points of
`X` are finite.

**Theorem 10.3.1.**[^N.D.E-V-49] *Under the hypotheses of 10.2, suppose that `F` is quasi-finite over `X`. Then there
exists an open `U` of `X`, dense and `G`-saturated, satisfying the following properties:*

<!-- label: III.V.10.3.1 -->

*(i) In `(Sch/S)`, the cokernel `V = G\U` exists; moreover, the scheme `V` is a quotient in the category of ringed
spaces.*

*(ii) `p : U → V` is surjective, open, and of finite presentation.*

*(iii) `V` is of finite presentation over `S`.*

*(iv) The morphism `G ×_S U → U ×_V U`, `(g, x) ↦ (gx, x)`, is surjective.*

*(v) Suppose in addition that `G` acts freely on `X`. Then `U → V` is a (left) `G`-torsor locally trivial for the (fppf)
topology. In particular, `U → V` is faithfully flat.*[^N.D.E-V-50]

*Proof.* It is assumed that the morphism `G ×_S X → X ×_S X`, `(g, x) ↦ (gx, x)`, is quasi-finite. Theorem 8.1 therefore
applies to the groupoid defined by `(X, G)`. Thus there exists a dense saturated open `U ⊂ X` such that the quotient
`G\U` exists; it satisfies properties (i), (ii), (iii).

<!-- original page 288 -->

To establish (iv), recall that `G` acts freely on `X` if and only if `(d₀, d₁)` is an equivalence pair (III 3.2.1). In
this case, theorem 8.1 (iv) shows that the morphism `G ×_S U → U ×_V U` is an isomorphism and that `p` is faithfully
flat and of finite presentation. Thus `U` is a `G`-torsor with base `V`, locally trivial for the (fppf) topology.

### 10.4. Case where `F` is flat over `X`.

<!-- label: III.V.10.4 -->

We denote

```text
   d = (d₀, d₁) : G ×_S X ⟶ X ×_S X
```

the morphism `d(g, x) = (gx, x)`. Recall that the sheaf-theoretic graph `Γ̃` of the equivalence relation associated with
`(X, G)` is the (fppf) `S`-subsheaf of `X ×_S X` image of `(d₀, d₁)`. It is the (fppf) sheaf associated to the graph
functor:

```text
   T ↦ Γ(T) = {(x₀, x₁) ∈ X(T) × X(T) | x₀ ∈ G(T) x₁}.
```

Set `G_X = G ×_S X`. For every `S`-scheme `T`, one has a surjective map

```text
   G_X(T) ⟶ Γ(T),   (g, x) ↦ (gx, x),
```

which induces a bijective map

```text
   φ(T) : G_X(T)/F(T) ⥲ Γ(T);
```

indeed, if `(g, x), (g′, x′) ∈ G_X(T)` satisfy `(gx, x) = (g′ x′, x′)`, then `x′ = x` and `g⁻¹ g′ x = x`, so
`(g⁻¹ g′ x, x) ∈ F(T)` and `(g, x)` and `(g′, x)` have the same image in `G_X(T)/F_X(T)`.

By definition (cf. IV, 4.4.1 (ii) or proof of 5.2.1), the quotient sheaf `G_X/F` is the (fppf) sheaf associated to the
presheaf

```text
   T ↦ G_X(T)/F(T) ≅ Γ(T).
```

One therefore has an isomorphism of sheaves `φ : G_X/F → Γ̃`.

**Theorem 10.4.1.**[^N.D.E-V-51] *Under the hypotheses of 10.2, one has:*

<!-- label: III.V.10.4.1 -->

*a) `Γ̃` is representable if and only if `F` is flat over `X`.*

*b) Suppose `F` flat over `X`. Then the morphisms induced by `d₁` and `d₀`:*

```text
   G_X/F   ⇉   X
        d₀ ↓↑ d₁
```

*are faithfully flat and of finite presentation.*

<!-- original page 289 -->

*Proof of a):* Suppose the (fppf) sheaf `G_X/F` representable by an `X`-scheme `Y`. Then, by IV 6.3.3, `p : G_X → Y` is
faithfully flat and locally of finite presentation, and the second square of the diagram below is Cartesian:

```text
   F ────→ F ×_X G_X ────→ G_X
   │                            │ p
   ↓                            ↓
   X ──e_X──→ G_X ──────────→ Y,
```

the first square being obtained by base change along the unit section `e_X : X → G_X`. Since `p` is faithfully flat and
locally of finite presentation, so is `F → X`.

Conversely, suppose `F` flat over `X`. Put `X_2 = X ×_S X`. The morphism `d : G_X → X_2` allows one to form the fiber
product:

```text
   G_X ×_{X_2} G_X ────→ G_X
        │                 │
        ↓                 ↓
       G_X ────────────→ X_2.
```

Then the morphism `G_X ×_{X_2} G_X → X_2` is an `F ×_X X_2`-torsor over `X_2`, and is therefore flat and of finite type
(since `F` is). By theorem 10.1.1, the morphism `d` factors uniquely:

```text
   G_X ──ψ──→ Y ──τ──→ X ×_S X,
```

where `ψ` is faithfully flat (of finite type) and `τ` is a monomorphism of schemes.

Consequently, the morphism of sheaves `ψ : G_X → Y` is therefore `F`-invariant, and there comes a morphism of sheaves
`ψ̄ : G_X/F → Y`. Moreover, since `ψ` is faithfully flat (of finite type), the monomorphism of sheaves `τ` factors
through the sheaf image of `d`, that is `Γ̃`. The isomorphism of sheaves `G_X/F ≅ Γ̃` therefore factors through the
monomorphism `Y → Γ̃`. One concludes that `Y` represents `G_X/F`.

*Proof of b):* Suppose `F` flat over `X`. Then, by a) and its proof, `G_X/F` is representable, and the morphism
`p : G_X → G_X/F` is faithfully flat and of finite presentation. On the other hand, the morphisms `d_i : G_X → X`
(`i = 0, 1`) are faithfully flat and of finite presentation by hypothesis. Since `d_i = d̄_i ∘ p`, it follows from EGA
IV_2, 2.2.13 (iii) and EGA IV_3, 11.3.16, that `d̄_i` is faithfully flat and of finite presentation.

**Theorem 10.4.2.**[^N.D.E-V-52] *Under the hypotheses of 10.2, suppose `F` flat over `X`. Then there exists a dense
saturated open `U` of `X` such that the (fppf) quotient `V = G\U` is an `S`-scheme of finite type and `U → V` is
faithfully flat and of finite presentation.*

<!-- label: III.V.10.4.2 -->

<!-- original page 290 -->

*Proof.* Theorem 10.4.1 shows that `G_X/F ≅ Γ̃` is representable. Then the (fppf) sheaf `G\X` identifies with the
quotient sheaf of

```text
                  d̄₁
   G_X/F     ⇉    X.
                  d̄₀
```

By what precedes, `d̄_i : G_X/F → X` is faithfully flat and of finite presentation (`i = 0, 1`), and the morphism

```text
   G_X/F ──≅──→ Γ̃ ────→ X ×_S X
```

is a monomorphism, that is, `(d̄₀, d̄₁)` is an equivalence pair. Consequently, theorem 8.1 applies. There therefore
exists an open `U` of `X`, dense and saturated, such that the (fppf) quotient `V = G\U` is an `S`-scheme of finite type,
and `U → V` is faithfully flat and of finite presentation.

Taking into account the generic flatness theorem (EGA IV_2, 6.9.3), one obtains the

**Corollary 10.4.3.** *Under the hypotheses of 10.2, suppose `X` reduced. Then there exists a dense saturated open `U`
of `X` such that the (fppf) quotient `G\U` is an `S`-scheme of finite type and `U → G\U` is faithfully flat and of
finite presentation.*

<!-- label: III.V.10.4.3 -->

## Bibliography

[^N.D.E-V-53]

[AK80] A. B. Altman, S. L. Kleiman, *Compactifying the Picard Scheme*, Adv. Math. **35** (1980), 50–112.

[An73] S. Anantharaman, *Schémas en groupes, espaces homogènes et espaces algébriques sur une base de dimension 1*, Mém.
Soc. Math. France **33** (1973), 5–79.

[BLR90] S. Bosch, W. Lütkebohmert, M. Raynaud, *Néron models*, Springer-Verlag, 1990.

[CTS79] J.-L. Colliot-Thélène, J.-J. Sansuc, *Fibrés quadratiques et composantes connexes réelles*, Math. Ann. **244**
(1979), 105–134.

[DG70] M. Demazure, P. Gabriel, *Groupes algébriques*, Masson & North-Holland, 1970.

[DR81] J. Dixmier, M. Raynaud, *Sur le quotient d'une variété algébrique par un groupe algébrique*, pp. 327–344 in:
*Mathematical Analysis and Applications* (L. Schwartz 65th birthday, ed. L. Nachbin), Adv. Math. Suppl. Stud., Vol. 7A,
1981\.

[Fe03] D. Ferrand, *Conducteur, descente et pincement*, Bull. Soc. Math. France **131** (2003), no. 4, 553–585.

[Hi62] H. Hironaka, *An example of a non-Kählerian complex analytic deformation of Kählerian complex structures*, Ann.
of Math. **75** (1962), no. 1, 190–208.

<!-- original page 291 -->

[KM97] S. Keel, S. Mori, *Quotient by groupoids*, Ann. of Math. **145** (1997), no. 1, 193–213.

[Ko97] J. Kollár, *Quotient spaces modulo algebraic groups*, Ann. of Math. **145** (1997), no. 1, 33–79.

[Ko08] J. Kollár, *Quotients by finite equivalence relations*, arXiv: 0812.3608.

[Mum65] D. Mumford, *Geometric invariant theory*, Springer-Verlag, 1965; 2nd (resp. 3rd) ed. with J. Fogarty (resp. and
F. Kirwan), 1982 (resp. 1994).

[Mur65] J. P. Murre, *Representation of unramified functors. Applications* (according to unpublished results of A.
Grothendieck), Sém. Bourbaki, Vol. 9, Exp. 294 (1965), Soc. Math. France, 1995.

[Ray67a] M. Raynaud, *Passage au quotient par une relation d'équivalence plate*, pp. 78–85 in: *Proc. Conf. Local Fields
(Driebergen)* (ed. T. A. Springer), Springer-Verlag, 1967.

[Ray67b] M. Raynaud, *Sur le passage au quotient par un groupoïde plat*, C. R. Acad. Sci. Paris (Sér. A) **265** (1967),
384–387.

<!-- LEDGER DELTA — Exposé V — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| pré-relation d'équivalence | pre-equivalence relation | Gabriel's coinage; preserve hyphen and the term, since the Exposé constructs quotients for these. |
| couple d'équivalence | equivalence pair | A pair `(d₀, d₁) : X₁ → X₀` whose `d₀ ⊠ d₁` is, on `T`-points, the graph of an equivalence relation on `X₀(T)`. |
| conoyau | cokernel | Standard categorical sense (coequalizer of the double arrow). |
| diagramme exact | exact diagram | For a coequalizer diagram in the sense of §1.a). |
| flèche | arrow | Reserved for category-theoretic morphisms in §1; "morphism" used when the source is a scheme morphism. |
| espace annelé | ringed space | Standard. The category is written `(Esp.An)`. |
| `(Esp.An)` | `(Esp.An)` | Source notation preserved (category of ringed spaces). |
| saturé | saturated | Of an open set, for a given groupoid/equivalence relation. |
| quasi-section | quasi-section | Gabriel's technical term; do not translate. |
| fini localement libre | finite locally free | Of a morphism of schemes. |
| fidèlement plat et quasi-compact | faithfully flat and quasi-compact | Standard. |
| épimorphisme effectif (universel) | (universal) effective epimorphism | Standard. |
| changement de base | base change | Standard. |
| produit fibré | fiber product | American spelling. |
| application source / but / composition | source / target / composition map | Standard groupoid terminology. |
| flèche identique | identity arrow | Standard. |
| relation d'équivalence effective | effective equivalence relation | As in Exp. IV 3.3.2. |
| schéma quasi-projectif | quasi-projective scheme | Standard. |
| morphisme entier | integral morphism | Standard. |
| polynôme caractéristique | characteristic polynomial | Standard. |
| Hamilton-Cayley | Hamilton–Cayley | En-dash between author names. |
| Cohen-Seidenberg | Cohen–Seidenberg | En-dash between author names. |
| Lemme d'évitement des idéaux premiers | Prime Avoidance Lemma | Standard English phrase. |
| « la formation du quotient commute au changement de base » | "the formation of the quotient commutes with base change" | Translate guillemets to quotation marks. |
| fermé relativement à `S` | closed relative to `S` | Gabriel's standing phrase for "closed in its fiber over `S`". |
| anneau semi-local | semilocal ring | One word, American. |
| anneau local artinien | Artinian local ring | Standard. |
| stabilisateur de la section diagonale | stabilizer of the diagonal section | Standard. |
| graphe faisceautique | sheaf-theoretic graph | Per IV. |
| schéma en groupes réductifs | reductive group scheme | Standard. |
| `G`-torseur | `G`-torsor | Standard. |
| linéarisable | linearizable | Standard. |
| théorème de platitude générique | generic flatness theorem | Standard (EGA IV_2 6.9.3). |
| schéma fini | finite scheme | Standard. |
| schéma noethérien | Noetherian scheme | Capital N. |
| « accents » | "accents" | Translator's note on Gabriel's use of primes vs. accents. |
| « pré-relations d'équivalence » | "pre-equivalence relations" | Guillemets in source → English quotation marks; coinage preserved. |
-->

[^N.D.E-V-1]: N.D.E.: namely, theorems 5.1, 5.3, 6.1, 6.2 and 7.2 of TDTE III. The first two (resp. the next two)
    correspond to theorem 4.1 (resp. theorems 7.1 and 8.1) of this Exposé. Theorem 7.2 of TDTE III is proved
    in Exp. VI_A, 3.2 and 3.3.

[^N.D.E-V-2]: N.D.E.: that is, groupoids with base `X`, cf. the terminology at the end of section 1. When `C` is the
    category of schemes, the quotient `p : X → Y` of a groupoid `X∗` with base `X` exists under certain
    hypotheses (cf. 4.1, 6.1, 7.1); if, moreover, `X∗` is an equivalence relation, then `p` is, under the same
    hypotheses, faithfully flat and quasi-compact, hence a universal epimorphism, cf. loc. cit.

[^N.D.E-V-3]: N.D.E.: Lemmas 1.1 and 1.2 have been added; they are used several times in sections 5 to 9.

[^N.D.E-V-4]: N.D.E.: This is not the case in the category of schemes. Take, for example, `S = Spec(C)`,
    `X₀ = A²_S = Spec(C[x₁, x₂])`, let `d₁ : G_{m,S} ×_S A²_S → A²_S` be the action of `G_{m,S}` by
    homotheties on `A²_S`, let `d₀` be the projection onto the second factor, and `U = A²_S − {m}`, where `m`
    is the point `(0, 0)`. Then projective space `P¹_S` is the cokernel of `(d̃₀, d̃₁)` in `(Esp. An)` and in
    `(Sch)`, and the cokernel `Y` of `(d₀, d₁)` in `(Esp. An)` is the union of `P¹_S` and the point
    `y₀ = {p(m)}`; the only open set containing `y₀` is `Y`, and one has `Γ(Y, O_Y) = C`. If `f : A²_S → T` is
    a morphism of `S`-schemes such that `f d₀ = f d₁` and if `V = Spec(A)` is an affine open of `T` containing
    the point `t₀ = f(y₀)`, then `f⁻¹(V) = A²` and the ring morphism `A → C[x₁, x₂]` factors through `C`; this
    shows that `S = Spec(C)` is the cokernel of `(d₀, d₁)` in the category `(Sch/S)`.

[^N.D.E-V-5]: N.D.E.: Hence, in this case, `X₂(T)` is the set of pairs `(f₂, f₁)` of composable arrows, that is, such
    that `d₀(f₁) = d₁(f₂)`, and `d′₀`, `d′₁`, `d′₂` send `(f₂, f₁)` to `f₂`, `f₂ ∘ f₁`, `f₁` respectively.

[^N.D.E-V-6]: N.D.E.: `T ↦ s(T)` defines an element of `Hom(h_{X₀}, h_{X₁})`, and the latter equals `Hom(X₀, X₁)` by the
    Yoneda lemma.

[^N.D.E-V-7]: N.D.E.: It follows from the Yoneda lemma that `σ` is an involutive automorphism of `X₁`; this will be
    used, for example, in 3.e) and in theorem 4.1.

[^N.D.E-V-8]: N.D.E.: see example 2.a) below.

[^N.D.E-V-9]: N.D.E.: In particular, if `G` is a `C`-group acting on the left on an object `X` of `C` and if `X∗` is the
    `C`-groupoid defined in a), then `(d₀, d₁)` is an equivalence pair if and only if `G` acts freely on `X`,
    cf. Exp. III, 3.2.1.

[^N.D.E-V-10]: N.D.E.: The same argument applies for `B = k[T³, T⁴]` and `T⁵ ⊗_B 1`; more generally, for
    `B = k[Tⁿ, T^{n+r}]` and the element `T^{n+2r} ⊗_B 1`, provided that `n` does not divide `2r`.

[^N.D.E-V-11]: N.D.E.: this second viewpoint will be used in 3.f) and in the proof of 6.1.

[^N.D.E-V-12]: N.D.E.: "accents" in the original.

[^N.D.E-V-13]: N.D.E.: This will play a crucial role in the proof of lemma 6.1.

[^N.D.E-V-14]: N.D.E.: The original has been modified to make explicit the isomorphism below.

[^N.D.E-V-15]: N.D.E.: Reflexivity follows from the existence of `s : X₀ → X₁` which is a section of both `d₀` and `d₁`;
    symmetry follows from the existence of the involution `σ` of `X₁` which "exchanges `d₀` and `d₁`", that
    is, satisfies `d₀ σ = d₁` and `d₁ σ = d₀`, cf. § 1, (3), (3 bis) and (†).

[^N.D.E-V-16]: N.D.E.: Since `d₀ = d₁ σ`, where `σ` is an involutive automorphism of `X₁`, these two conditions are
    symmetric in `d₁` and `d₀`; moreover, one has `d₀ d₁⁻¹(x) = d₁ d₀⁻¹(x)`.

[^N.D.E-V-17]: N.D.E.: One cannot omit hypothesis b). Indeed, H. Hironaka has given an example of an action of the
    finite group `G = ℤ/2ℤ` on a proper `C`-variety `X₀` such that the quotient `X₀/G` is an algebraic space
    which is not a scheme ([Hi62], see also [Mum65], Chap. 4, § 3).

[^N.D.E-V-18]: N.D.E.: We have added that `p` is open, by taking up the analogous proof given in 6.1.

[^N.D.E-V-19]: N.D.E.: Note that, in this case, `X₁ → X₀ ×_S X₀` is therefore an immersion (EGA I, 5.3.10); see also
    VI_B, 9.2.1. On the other hand, for the existence of the quotient (in the category of schemes or that of
    algebraic spaces) under the weaker hypothesis that `d₀` and `d₁` are finite (but not necessarily flat),
    see [An73], § 1.1, [Fe03], [Ko08]…

[^N.D.E-V-20]: N.D.E.: We have made explicit the consequences which follow; see [Ray67a], th. 1 (iii) and the proof
    given further on, at the end of section 5.

[^N.D.E-V-21]: N.D.E.: We have expanded on the original in what follows; in particular, we have added lemma 4.1.1, taken
    from [DG70], III, § 2.4, Lemma 4.3.

[^N.D.E-V-22]: N.D.E.: We have inserted this lemma, which is used several times in this Exposé and in subsequent Exposés
    (VI_A, VI_B). It appeared as Lemma VI_B, 4.5.1 in the original 1965 edition of SGAD.

[^N.D.E-V-23]: N.D.E.: Note the permutation of pages in Lecture Notes 151; the real order is
    265-266-268-269-267-270-271.

[^N.D.E-V-24]: N.D.E.: We have added the following lemma, taken from [DG70], I, § 5, Prop. 1.5 (see also the proof of
    EGA IV_3, 8.11.5), used implicitly in the original, and explicitly in [DG70], III, § 2, 4.6. It is
    moreover useful in th. 7.1 further on.

[^N.D.E-V-25]: N.D.E.: cf. Lemma 4.1.2.

[^N.D.E-V-26]: N.D.E.: We have added what follows.

[^N.D.E-V-27]: N.D.E.: indeed, since `d₀` (resp. `d₁`) is surjective, flat and finite, hence faithfully flat and affine,
    then `d′₂` is of rank `n` above a neighborhood of a point `x` of `X₁` if and only if `d₁` is of rank `n`
    above a neighborhood of `d₀(x)` (resp. `d₁(x)`).

[^N.D.E-V-28]: N.D.E.: one has `d₁(d₀⁻¹(x)) = d₀(d₁⁻¹(x))`, cf. N.D.E. 16 in theorem 4.1.

[^N.D.E-V-29]: N.D.E.: We have added the reference to lemma 4.1.1, cf. [DG70], III, § 5.2, p. 313.

[^N.D.E-V-30]: N.D.E.: We have added this paragraph.

[^N.D.E-V-31]: N.D.E.: If `x, y ∈ E`, there exists `z ∈ X₁` such that `d₁(x) = x` and `d₀(z) = y`, that is, `z` belongs
    to the set `v⁻¹(x)`, which is finite by (1). Hence `E` is contained in the finite set
    `d₀(v⁻¹(x)) = d₀ d₁⁻¹(x) ∩ U`.

[^N.D.E-V-32]: N.D.E.: We have slightly modified what follows; in particular, in lemma 6.1, the additional hypothesis
    that `d₀` be flat has been moved to (iv), and (ii) has been separated into (i′) + (ii), and the second
    assertion of (i′) added.

[^N.D.E-V-33]: N.D.E.: We have expanded what follows, in particular the fact that `U′` is a quasi-section of the
    groupoid induced on `X′₀`.

[^N.D.E-V-34]: N.D.E.: Let us mention here the article of S. Keel and S. Mori ([KM97]), where the following theorem is
    established. Let `X` be an algebraic space of finite type over a locally Noetherian base `S`, and
    `j : R → X ×_S X` a flat groupoid whose stabilizer `j⁻¹(Δ_X)` is finite over `X`; there then exists an
    algebraic space which is a geometric quotient of `X` by `R` and a uniform categorical quotient; moreover,
    if `j` is separated, this quotient is separated. In particular, if a flat `S`-group scheme `G` acts
    properly on `X`, with finite stabilizer (i.e., the morphism `G ×_S X → X ×_S X`, `(g, x) ↦ (x, g · x)`,
    is proper and the stabilizer of the diagonal is finite over `X`), then there exists a geometric quotient
    `X → X/G`. In the case of a reductive `S`-group scheme `G`, this is a result of J. Kollár ([Ko97]).

[^N.D.E-V-35]: N.D.E.: This hypothesis on `X₀` is necessary, cf. N.D.E. 17 in Th. 4.1.

[^N.D.E-V-36]: N.D.E.: In TDTE III, Th. 6.1, it is indicated that `Y → S` is quasi-projective if `S` is Noetherian. The
    editors have not seen how to deduce this from the local existence of quasi-sections.

[^N.D.E-V-37]: N.D.E.: We have made explicit the consequences which follow; see [Ray67a], th. 1 (iii) and the end of the
    proof of the theorem. Let us also mention that another proof of th. 7.1 in the case of an equivalence
    relation, based on the existence of Hilbert schemes, is given in [AK80], Th. 2.9, see also [BLR90], §
    8.2, Th. 12; it is moreover shown there, in this case, that `Y → S` is quasi-projective.

[^N.D.E-V-38]: N.D.E.: Indeed, if one has constructed such an open neighborhood `U_z` for every point `z` closed
    relative to `S`, then the union of these `U_z` covers `X₀`, since each fiber over `S` of the closed
    complement is a Noetherian scheme without closed points, hence empty.

[^N.D.E-V-39]: N.D.E.: We have added details, and made explicit the role of the hypothesis that `d₀` and `d₁` are proper
    in theorem 7.1. (One can compare with the statement and proof of theorem 8.1, where this properness
    hypothesis is omitted.)

[^N.D.E-V-40]: N.D.E.: If `f : X → Y` is a morphism locally of finite type, the set of `x ∈ X` isolated in their fiber
    `f⁻¹(f(x))` is open in `X`: in EGA III, 4.4.10, this is deduced, for `Y` locally Noetherian, from
    Zariski's "Main Theorem"; on the other hand, for arbitrary `Y`, this follows from Chevalley's
    semi-continuity theorem (EGA IV_3, 13.1.3 and 13.1.4). Consequently, `f` is quasi-finite at `x` if and
    only if `f` is of finite type at `x` and `x` is isolated in `f⁻¹(f(x))`; this will be used further on,
    cf. N.D.E. 42.

[^N.D.E-V-41]: N.D.E.: We have expanded on the original in what follows.

[^N.D.E-V-42]: N.D.E.: The conditions are sufficient, by base change (cf. EGA II, 6.2.4 (iii) and EGA IV_2, 2.1.4).
    Conversely, put `y = d′(x)` and `z = u(y) = d(v(x))`, and suppose `d′` flat at `x` and `u` (hence also
    `v`) flat. Then `O_{v(x)} → O_x` is faithfully flat, as is `O_z → O_y → O_x`. Consequently,
    `O_z → O_{v(x)}` is faithfully flat (cf. EGA IV_2, 2.2.11 (iv)). Finally, suppose `d` locally of finite
    type and `d′` quasi-finite at `x`. Then `v(x)` is isolated in its fiber `d⁻¹(z)`, since `x` is in its
    fiber `d′⁻¹(y) = d⁻¹(z) ⊗_{κ(z)} κ(y)`. Hence, by Chevalley's semi-continuity theorem, there exists an
    open neighborhood of `v(x)` every point of which is isolated in its fiber (EGA IV_3, 13.1.3 and 13.1.4),
    so that `d` is quasi-finite at `v(x)`.

[^N.D.E-V-43]: N.D.E.: We have modified the sequel, taking advantage of the additions made in lemma 6.1.

[^N.D.E-V-44]: N.D.E.: There exists a largest open `W` of `X₀` satisfying the conclusions of the theorem. Indeed, let
    `W` be an open as in the theorem and `W^♯` a dense saturated open contained in `W`. Since `p` is open,
    `V^♯ = p(W^♯)` is an open of `V`, and `W^♯ = p⁻¹(V^♯)`, since `W^♯` is saturated. By lemma 1.1, `V^♯` is
    a cokernel for the groupoid induced on `W^♯`. Thus one can glue along their intersection `W^♯` two opens
    `W` and `W′` satisfying the conclusions of the theorem, and the conditions (i), (ii), (iii), (iv), as
    well as the fact that `p` and `V → S` are locally of finite presentation, are preserved. The conclusion
    (ii′) follows, as in the proof of 6.1 (ii), from the hypothesis that `X₀` is of finite type over `S`
    Noetherian. Moreover, lemmas 1.1 and 1.2 also show that the union of all saturated opens `U` of `X₀` such
    that the open `p(U)` of `Y` is a scheme and `p|_U : U → p(U)` is a morphism of schemes is the largest
    saturated open `Ω` of `X₀` satisfying condition (i) of 8.1. Theorem 8.1 shows that `Ω` contains a dense
    open `W`, but it is not immediate that `Ω` satisfies properties (ii) to (iv). On this subject, the reader
    may consult [Ray67a], [Ray67b], and Appendix I of [An73], which give more precise results, and study the
    question of the representability of the quotient `S`-sheaf (fppf) `X̃/R` (where one has denoted by `R`
    the groupoid `X∗` with base `X = X₀`), all this under weaker hypotheses (`S` an arbitrary scheme, `X` a
    scheme locally of finite type over `S`, and `R` an `S`-groupoid with base `X` such that `d₀` (and
    therefore `d₁`) is flat and of finite presentation). Let us mention in particular the following results.
    If `X̃/R` is representable by an `S`-scheme `Y`, then `Y` is also the cokernel in the category
    `(Esp. An)`. The converse is in general false (cf. example 0.4 of [Mum65], Chap. 0, § 3, cited in
    [Ray67a], Rem. 1), but is true if `d = (d₀, d₁)` is an immersion. Under this hypothesis, the morphism
    `p : Ω → Z := Ω/R_Ω` is faithfully flat and of finite presentation; if moreover `S` is locally
    Noetherian, then a point `x` of codimension 1 in `X` belongs to `Ω` if and only if the graph of the
    groupoid induced on `Spec(O_{X,x})` is closed. For all this, see [Ray67a], Prop. 1, [Ray67b], Prop. 1 and
    Theorems 2, 1 and 4, and [An73], Theorems 5 and 6 pages 66–67, and Prop. 3.3.1 page 49. (See also, in the
    case of an action of an algebraic group on an algebraically closed field `k`, the article [DR81].)

[^N.D.E-V-45]: N.D.E.: Indeed, let `η` be such a generic point. The hypotheses imply that `O_{X₀, η}` is an Artinian
    local ring, and `O_{F₁, η}` a finitely generated `O_{X₀, η}`-module. Therefore, by SGA 1, VIII 6.5, there
    exists an open neighborhood of `η` above which `d̃₁` is finite.

[^N.D.E-V-46]: N.D.E.: We have expanded what follows, to highlight theorem 9.0 below.

[^N.D.E-V-47]: N.D.E.: The original states that this follows from proposition 9.1 below. We were not able to reconstruct
    that argument. The proof that follows was indicated to us by O. Gabber.

[^V-9-1]: Cf. EGA IV_4, 17.7.5 for a more general result.

[^N.D.E-V-48]: N.D.E.: cf. EGA IV_1, 1.4.4.

[^N.D.E-V-49]: N.D.E.: Here too, there exists a largest open `U` of `X` satisfying the conclusions of the theorem, cf.
    N.D.E. 44.

[^N.D.E-V-50]: N.D.E.: If one assumes in addition that `G` is a reductive `S`-group scheme and that the (free) action of
    `G` on `X` is linearizable, then it is known that `G\X` is representable and that `X → G\X` is a (left)
    `G`-torsor. This follows from results of Raynaud and Seshadri and is found in the article [CTS79]
    (proposition 6.11).

[^N.D.E-V-51]: N.D.E.: This is point (2) of theorem 3 of [Ray67b]. In this Note another proof of th. 10.1.1 is sketched.

[^N.D.E-V-52]: N.D.E.: Here too, there exists a largest open `U` of `X` satisfying the conclusions of the theorem;
    moreover, a point `x ∈ X` of codimension 1 in `X` belongs to `U` if and only if the morphism
    `(G_X/F) ×_X Spec(O_{X,x}) → Spec(O_{X,x}) ×_S Spec(O_{X,x})` is a closed immersion, cf. N.D.E. 44.

[^N.D.E-V-53]: N.D.E.: additional references cited in this Exposé.
