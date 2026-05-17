# Exposé VI. Fibered Categories and Descent

<!-- label: VI -->

<!-- original page 145 -->

## 0. Introduction

Contrary to what had been announced in the introduction to the preceding exposé, it has turned out to be impossible to
do descent in the category of preschemes, even in particular cases, without first having developed with sufficient care
the language of descent in general categories.

The notion of “descent” supplies the general framework for all procedures of “gluing” objects, and consequently of
“gluing” categories. The most classical case of gluing is relative to the data of a topological space `X` and a covering
of `X` by open subsets `Xᵢ`. Suppose one is given, for every `i`, a fiber space, say, `Eᵢ` over `Xᵢ`, and for every pair
`(i,j)` an isomorphism `f_{ji}` from `Eᵢ|X_{ij}` to `Eⱼ|X_{ij}`, where `X_{ij} = Xᵢ ∩ Xⱼ`, satisfying the well-known
transitivity condition, written in abbreviated form `f_{kj} f_{ji} = f_{ki}`. One knows that there exists a fiber space
`E` on `X`, defined up to isomorphism by the condition that one have isomorphisms `fᵢ: E|Xᵢ ≃ Eᵢ` satisfying the
relations `f_{ji} = fⱼ fᵢ⁻¹`, with the usual abuse of notation.

Let `X′` be the sum space of the `Xᵢ`; it is therefore a fiber space over `X`, i.e. endowed with a continuous map
`X′ → X`. The data of the `Eᵢ` can be interpreted more concisely as a fiber space `E′` over `X′`, and the data of the
`f_{ji}` as an isomorphism between the two inverse images, by the two canonical projections, `E″₁` and `E″₂` of `E′` on
`X″ = X′ ×_X X′`. The gluing condition can then be written as an identity between isomorphisms of fiber spaces `E‴₁` and
`E‴₃` over the triple fiber product `X‴ = X′ ×_X X′ ×_X X′`, where `E‴ᵢ` denotes the inverse image of `E′` on `X‴` by
the canonical projection of index `i`. The construction of `E` from `E′` and `f` is a typical case of a “descent”
procedure.

<!-- original page 146 -->

Moreover, starting from a fiber space `E` on `X`, one says that `X` is “locally trivial”, with fiber `F`, if there
exists an open covering `(Xᵢ)` of `X` such that the `E|Xᵢ` are isomorphic to `F × Xᵢ`, or what amounts to the same
thing, such that the inverse image `E′` of `E` on `X′ = ∐ᵢ Xᵢ` is isomorphic to `X′ × F`.

Thus the notion of “gluing” objects, like that of “localization” of a property, is tied to the study of certain types of
“base changes” `X′ → X`. In algebraic geometry, many other types of base change, and notably faithfully flat morphisms
`X′ → X`, must be regarded as corresponding to a procedure of “localization” relative to preschemes, or other objects,
“over” `X`. This type of localization is used just as much as ordinary topological localization, of which it is moreover
a special case. The same is true, to a lesser extent, in analytic geometry.

Most of the proofs, reducing to verifications, are omitted or merely sketched. Where appropriate, we specify the less
evident diagrams that enter into a proof.

## 1. Universes, Categories, Equivalence of Categories

<!-- label: VI.1 -->

To avoid certain logical difficulties, we shall admit here the notion of a **Universe**, which is a set “large enough”
that one does not leave it under the usual operations of set theory; an “**axiom of Universes**” guarantees that every
object lies in a Universe. For details, see a book in preparation by C. Chevalley and the speaker.[^vi-1-1] Thus the
symbol `Set` denotes not the category of all sets, a notion that has no sense, but the category of sets that lie in a
given Universe, which we shall not specify in the notation. Similarly, `Cat` will denote the category of categories
lying in the Universe in question; the “morphisms” from one object `X` of `Cat` to another `Y` are, by definition, the
**functors** from `X` to `Y`.

<!-- original page 147 -->

If `𝒞` is a category, we denote by `Ob(𝒞)` **the set of objects** of `𝒞`, and by `Fl(𝒞)` **the set of arrows** of `𝒞`,
or morphisms of `𝒞`. We shall therefore write `X ∈ Ob(𝒞)`, avoiding the common abuse of notation `X ∈ 𝒞`. If `𝒞` and
`𝒞′` are two categories, a **functor** from `𝒞` to `𝒞′` will always mean what is commonly called a **covariant** functor
from `𝒞` to `𝒞′`. Its data include both the target category and the source category, `𝒞` and `𝒞′`. The functors from `𝒞`
to `𝒞′` form a set, denoted `Hom(𝒞,𝒞′)`, which is the set of objects of a category denoted `Hom̲(𝒞,𝒞′)`. By definition,
a **contravariant functor** from `𝒞` to `𝒞′` is a functor from the **opposite category** `𝒞°` of `𝒞` to `𝒞′`.

We shall admit the notions of **projective limit** and **inductive limit** of a functor `F: ℐ → 𝒞`, and in particular
the most common special cases of these notions: cartesian products and fiber products, the dual notions of direct sums
and amalgamated sums, and the usual formal properties of these operations.

For example, in the category `Cat` introduced above, projective limits, relative to categories `ℐ` lying in the chosen
Universe, exist. The set of objects, respectively the set of arrows, of the projective-limit category `𝒞` of the `𝒞ᵢ` is
obtained by taking the projective limit of the sets of objects, respectively the sets of arrows, of the categories `𝒞ᵢ`.
The best-known case is that of the product of a family of categories. We shall constantly use, in what follows, the
fiber product of two categories over a third.

For everything concerning categories and functors, pending the book in preparation already mentioned, see [VI.1], which
is necessarily quite incomplete, even as concerns the generalities sketched in the present number.

Let us take this occasion to spell out the notion of equivalence of categories, which is not presented satisfactorily in
[VI.1]. A functor `F: 𝒞 → 𝒞′` is said to be **faithful**, respectively **fully faithful**, if for every pair of objects
`S`, `T` of `𝒞`, the map `u ↦ F(u)` from `Hom(S,T)` to `Hom(F(S),F(T))` is injective, respectively bijective. One says
that `F` is an **equivalence** of categories if

<!-- original page 148 -->

`F` is fully faithful and, moreover, every object `S′` of `𝒞′` is isomorphic to an object of the form `F(S)`. One shows
that this is the same as saying that there exists a functor `G` from `𝒞′` to `𝒞` **quasi-inverse** to `F`, i.e. such
that `GF` is isomorphic to `id_𝒞` and `FG` is isomorphic to `id_𝒞′`.

When this is so, giving a functor `G: 𝒞′ → 𝒞` and an isomorphism `φ: FG → id_𝒞′` is equivalent to giving, for every
`S′ ∈ Ob(𝒞′)`, a pair `(S,u)` formed by an object `S` of `𝒞` and an isomorphism `u: F(S) → S′`, namely `(G(S′), φ(S′))`.
With this notation, there exists a unique functor `𝒞′ → 𝒞` having the given map `S′ ↦ G(S′)` as its object map, and such
that the map `S′ ↦ φ(S′)` is a homomorphism of functors `FG → id_𝒞′`.

Finally, if `G` is a functor quasi-inverse to `F`, and if one chooses isomorphisms `φ: FG ≃ id_𝒞′` and `ψ: GF ≃ id_𝒞`,
then the two compatibility conditions on `φ` and `ψ` stated in [VI.1, I.1.2] are in fact equivalent to one another; and
for every chosen isomorphism `φ`, there exists a unique isomorphism `ψ` such that those conditions are satisfied.

## 2. Categories over Another Category

<!-- label: VI.2 -->

Let `ℰ` be a category in the chosen Universe. It is therefore an object of `Cat`, and one may consider the category
`Cat_/ℰ` of “objects of `Cat` over `ℰ`”. An object of this category is therefore a functor

```text
p: ℱ → ℰ.
```

One also says that the category `ℱ`, endowed with such a functor, is a **category over** `ℰ`, or an **`ℰ`-category**.
Thus an **`ℰ`-functor** from a category `ℱ` over `ℰ` to a category `𝒢` over `ℰ` will mean a functor

```text
f: ℱ → 𝒢
```

such that

```text
qf = p,
```

where `p` and `q` are the projection functors for `ℱ` and `𝒢` respectively. The set of `ℰ`-functors `f` from `ℱ` to `𝒢`
is therefore in bijective correspondence with the set of arrows with source `ℱ` and target `𝒢` in `Cat_/ℰ`,

<!-- original page 149 -->

without this being an identity, since the data of an `f` as above does not determine `ℱ` and `𝒢` as categories over `ℰ`.
Of course, as in any other category `𝒞_/S`, we shall routinely make the abuse of language that identifies `ℰ`-functors,
in the sense just explained, with arrows in a category `Cat_/ℰ`.

We shall denote by

```text
Hom_ℰ(ℱ,𝒢)
```

the set of `ℰ`-functors from `ℱ` to `𝒢`. Of course, a composite of `ℰ`-functors is an `ℰ`-functor, the composition in
question corresponding by definition to the composition of arrows in `Cat_/ℰ`.

Now consider two `ℰ`-functors

```text
f,g: ℱ → 𝒢
```

and a homomorphism of functors

```text
u: f → g.
```

One says that `u` is an **`ℰ`-homomorphism**, or a “**homomorphism of `ℰ`-functors**”, if for every `ξ ∈ Ob(ℱ)`, one has

```text
q(u(ξ)) = id_{p(ξ)}.
```

In words: putting `S = p(ξ) = qf(ξ) = qg(ξ) ∈ Ob(ℰ)`, the morphism

```text
u(ξ): f(ξ) → g(ξ)
```

in `𝒢` is an `id_S`-morphism. In general, for every morphism `α: T → S` in `ℰ` and every category `𝒢` over `ℰ`, a
morphism `v` in `𝒢` is called an **`α`-morphism** if `q(v) = α`, where `q` denotes the projection functor `𝒢 → ℰ`. If
one has a third `ℰ`-functor `h: ℱ → 𝒢` and an `ℰ`-homomorphism `v: g → h`, then `vu` is again an `ℰ`-homomorphism.

<!-- original page 150 -->

Thus **the `ℰ`-functors from `ℱ` to `𝒢`, and the `ℰ`-homomorphisms between them, form a subcategory of the category
`Hom̲(ℱ,𝒢)` of all functors from `ℱ` to `𝒢`; it will be called the category of `ℰ`-functors from `ℱ` to `𝒢` and
denoted**

```text
Hom̲_{ℰ/-}(ℱ,𝒢).
```

It is also the kernel subcategory of the pair of functors

```text
R,S: Hom̲(ℱ,𝒢) ⇉ Hom̲(ℱ,ℰ),
```

where `R` is the constant functor defined by the object `p` of `Hom̲(ℱ,ℰ)`, and `S` is the functor `f ↦ q ∘ f` defined
by `q: 𝒢 → ℰ`.

To finish these generalities, it remains to define the natural pairings between the categories `Hom̲_{ℰ/-}(ℱ,𝒢)` by
composition of `ℰ`-functors. In other words, one wants to define a “composition functor”

```text
(i)  Hom̲_{ℰ/-}(ℱ,𝒢) × Hom̲_{ℰ/-}(𝒢,ℋ) → Hom̲_{ℰ/-}(ℱ,ℋ)
```

when `ℱ`, `𝒢`, `ℋ` are three categories over `ℰ`, in such a way that this functor induces, on objects, the composition
map `(f,g) ↦ gf` for `ℰ`-functors `f: ℱ → 𝒢` and `g: 𝒢 → ℋ`. For this, recall that one defines a canonical functor

```text
(ii) Hom̲(ℱ,𝒢) × Hom̲(𝒢,ℋ) → Hom̲(ℱ,ℋ),
```

which on objects is just the composition map `(f,g) ↦ gf` of functors, and which transforms an arrow `(u,v)`, where

```text
u: f → f′,    v: g → g′,
```

are arrows in `Hom̲(ℱ,𝒢)`, respectively in `Hom̲(𝒢,ℋ)`, into the arrow

```text
v ∗ u: gf → g′f′
```

defined by the relation

<!-- original page 151 -->

```text
(v ∗ u)(ξ) = v(f′(ξ)) · g(u(ξ)) = g′(u(ξ)) · v(f(ξ)).
```

It is well known that one indeed obtains in this way a homomorphism from `gf` to `g′f′`, and that, for variable `f`, `g`
and `u`, `v`, one obtains the functor (ii); that is, one has

```text
(I)   id_g ∗ id_f = id_{gf},
```

and

```text
(II)  (v′ ∗ u′) ∘ (v ∗ u) = (v′ ∘ v) ∗ (u′ ∘ u).
```

Recall also that one has an associativity formula for the canonical pairings (ii), expressed on the one hand by the
associativity `(hg)f = h(gf)` of the composition of functors, and on the other hand by the formula

```text
(III) (w ∗ v) ∗ u = w ∗ (v ∗ u)
```

for the composition products of homomorphisms of functors, where `u: f → f′` and `v: g → g′` are as above, and where one
supposes given in addition a homomorphism `w: h → h′` of functors `h,h′: ℋ → 𝒦`.

I now say that **when `ℱ` and `𝒢` are `ℰ`-categories, the canonical composition functor (ii) induces a functor (i)**.
Since we already know that the composite of two `ℰ`-functors is an `ℰ`-functor, this amounts to saying that **when
`u: f → f′` and `v: g → g′` are homomorphisms of `ℰ`-functors, then `v ∗ u: gf → g′f′` is also a homomorphism of
`ℰ`-functors**. This follows trivially from the definitions. Since the pairings (i) are induced by the pairings (ii),
they satisfy the same associativity property, also expressed in the formulas `(hg)f = h(gf)` and
`(w ∗ v) ∗ u = w ∗ (v ∗ u)`, for `ℰ`-functors and `ℰ`-homomorphisms of `ℰ`-functors.

To complete the formulary (I), (II), (III), recall also the formulas

```text
(IV)  v ∗ id_ℱ = v    and    id_𝒢 ∗ u = u,
```

<!-- original page 152 -->

where, for simplicity, one writes `v ∗ f` or `u ∗ g` instead of `v ∗ u` when `u`, respectively `v`, is the identity
automorphism of `f`, respectively `g`.

It follows from the definition of the pairings (i) that **`Hom̲_{ℰ/-}(ℱ,𝒢)` is a functor in `ℱ` and `𝒢`, from the
product category `Cat_/ℰ° × Cat_/ℰ` to the category `Cat`**. Indeed, if `g: 𝒢 → 𝒢₁` is an `ℰ`-functor, i.e. an object of
`Hom̲_{ℰ/-}(𝒢,𝒢₁)`, then by taking `ℋ = 𝒢₁` in (i), there corresponds to it a functor

```text
g_*: Hom̲_{ℰ/-}(ℱ,𝒢) → Hom̲_{ℰ/-}(ℱ,𝒢₁).
```

One defines analogously, for an `ℰ`-functor `f: ℱ₁ → ℱ`, a functor

```text
f^*: Hom̲_{ℰ/-}(ℱ,𝒢) → Hom̲_{ℰ/-}(ℱ₁,𝒢).
```

For short, these functors are also denoted by the symbols `f ↦ g ∘ f` and `g ↦ g ∘ f` respectively; these in fact denote
only the corresponding maps on the sets of objects. It follows from the associativity property indicated above that one
does indeed obtain in this way, as announced, a functor `Cat_/ℰ° × Cat_/ℰ → Cat`.

## 3. Base Change in Categories over ℰ

<!-- label: VI.3 -->

Since projective limits exist in `Cat`, relative to categories `ℐ` belonging to the Universe, the same is true in
`Cat_/ℰ`. In particular, cartesian products exist there; these are interpreted as fiber products in `Cat`. In accordance
with the general notation, if `ℱ` and `𝒢` are categories over `ℰ`, we denote by

```text
ℱ ×_ℰ 𝒢
```

their product in `Cat_/ℰ`, i.e. their fiber product over `ℰ` in `Cat`, regarded as a category over `ℰ`. Thus `ℱ ×_ℰ 𝒢`
is endowed with two `ℰ`-functors `pr₁` and `pr₂`, which define, for every category `ℋ` over `ℰ`, a bijection

<!-- original page 153 -->

```text
Hom_ℰ(ℋ, ℱ ×_ℰ 𝒢) ≃ Hom_ℰ(ℋ,ℱ) × Hom_ℰ(ℋ,𝒢).
```

This bijection moreover comes from an isomorphism of categories

```text
Hom̲_{ℰ/-}(ℋ, ℱ ×_ℰ 𝒢) ≃ Hom̲_{ℰ/-}(ℋ,ℱ) × Hom̲_{ℰ/-}(ℋ,𝒢),
```

by taking the sets of objects of the two sides. The displayed functor is the one whose components are the functors
`h ↦ pr₁ ∘ h` and `h ↦ pr₂ ∘ h` from the first member to the two factors of the second. We leave to the reader the
verification that one indeed obtains an isomorphism in this way; the analogous fact is true more generally whenever one
has a projective limit of categories, and not only in the case of a fiber product.

Recall moreover, as was said in VI.1, that

```text
Ob(ℱ ×_ℰ 𝒢) = Ob(ℱ) ×_{Ob(ℰ)} Ob(𝒢),
Fl(ℱ ×_ℰ 𝒢) = Fl(ℱ) ×_{Fl(ℰ)} Fl(𝒢),
```

the composition of arrows being carried out componentwise.

In what follows, we consider a functor

```text
λ: ℰ′ → ℰ,
```

and, for every category `ℱ` over `ℰ`, we regard `ℱ ×_ℰ ℰ′` as a category over `ℰ′` by means of `pr₂`. In other words, we
interpret the “fiber product” operation as an operation of **“base change”**, the functor `λ: ℰ′ → ℰ` being called the
**“base-change functor.”** In accordance with the well-known general facts, one obtains in this way a functor, called
the **base-change functor** for `λ`:

<!-- original page 154 -->

```text
λ*: Cat_/ℰ → Cat_/ℰ′.
```

It is adjoint to the “restriction of the base” functor, which sends every category `ℱ′` over `ℰ′`, with projection
functor `p′`, to `ℱ′` regarded as a category over `ℰ` by the functor `p = λp′`. As is well known for a base-change
functor in a category, the base-change functor “commutes with projective limits”, and in particular “transforms” fiber
products over `ℰ` into fiber products over `ℰ′`.

Let `ℱ` and `𝒢` be two categories over `ℰ`. We shall define a **canonical isomorphism**

```text
(i)  Hom̲_{ℰ′/-}(ℱ′,𝒢′) ≃ Hom̲_{ℰ/-}(ℱ ×_ℰ ℰ′,𝒢),
     where ℱ′ = ℱ ×_ℰ ℰ′ and 𝒢′ = 𝒢 ×_ℰ ℰ′.
```

For this, consider the functor

```text
pr₁: 𝒢′ = 𝒢 ×_ℰ ℰ′ → 𝒢,
```

and define (i) by

```text
F ↦ pr₁ ∘ F,
```

which a priori denotes a functor

```text
(ii) Hom̲(ℱ′,𝒢′) → Hom̲(ℱ′,𝒢).
```

It remains only to verify that this latter functor induces a functor on the subcategories in (i), and that this induced
functor is an isomorphism. That (ii) induces a bijection

```text
Hom_{ℰ′/-}(ℱ′,𝒢′) ≃ Hom_{ℰ/-}(ℱ ×_ℰ ℰ′,𝒢)
```

is the characteristic property of the base-change functor. It remains therefore

<!-- original page 155 -->

to prove that if `F`, `G` are `ℰ′`-functors `ℱ′ → 𝒢′`, then **the map**

```text
u ↦ pr₁ ∘ u
```

**induces a bijection**

```text
Hom_{ℰ′}(F,G) ≃ Hom_ℰ(pr₁ ∘ F, pr₁ ∘ G).
```

The verification of this fact is immediate and is left to the reader.

It follows from this isomorphism (i), and from the end of the preceding number, that

```text
Hom̲_{ℰ′/-}(ℱ ×_ℰ ℰ′, 𝒢 ×_ℰ ℰ′)
```

**may be regarded as a functor in `ℰ′`, `ℱ`, `𝒢`, from the category `Cat_/ℰ° × Cat_/ℰ° × Cat_/ℰ` to the category
`Cat`**, isomorphic to the functor defined by the expression

```text
Hom̲_{ℰ/-}(ℱ ×_ℰ ℰ′,𝒢).
```

In particular, for fixed `ℱ` and `𝒢`, one obtains a functor in `ℰ′`. Thus the `ℰ`-functor of projection `λ: ℰ′ → ℰ`
defines a morphism, i.e. a functor

```text
λ*_{ℱ,𝒢}: Hom̲_{ℰ/-}(ℱ,𝒢) → Hom̲_{ℰ′/-}(ℱ′,𝒢′),
```

which we now spell out. On the sets of objects of the two sides, it is the map

```text
f ↦ f′ = f ×_ℰ ℰ′,
```

expressing the functorial dependence of `ℱ ×_ℰ ℰ′` on the object `ℱ` over `ℰ`. On the other hand, consider two
`ℰ`-functors

```text
f,g: ℱ → 𝒢
```

and a homomorphism of `ℰ`-functors

```text
u: f → g.
```

We shall spell out the corresponding homomorphism of `ℰ′`-functors

<!-- original page 156 -->

```text
u′: f′ → g′.
```

For every

```text
ξ′ = (ξ,S′) ∈ Ob(ℱ′)
```

with

```text
ξ ∈ Ob(ℱ),    S′ ∈ Ob(ℰ′),    p(ξ) = λ(S′) = S,
```

the morphism

```text
u′(ξ′): f′(ξ′) = (f(ξ),S′) → g′(ξ′) = (g(ξ),S′)    in 𝒢′
```

is defined by the formula

```text
u′(ξ′) = (u(ξ), id_{S′}).
```

This is indeed an `S′`-morphism in `𝒢′`, since `q(u(ξ)) = λ(id_{S′}) = id_S`.

Now consider any `ℰ`-functor

```text
λ′: ℰ″ → ℰ′
```

and the corresponding functor

```text
Hom̲_{ℰ′/-}(ℱ ×_ℰ ℰ′, 𝒢 ×_ℰ ℰ′)
  → Hom̲_{ℰ″/-}(ℱ ×_ℰ ℰ″, 𝒢 ×_ℰ ℰ″).
```

I say that this functor is none other than the one obtained by the preceding process, starting from `ℱ′` and `𝒢′` over
`ℰ′` and regarding `ℰ″` as a category over `ℰ′`, taking into account the isomorphisms of **“transitivity of base
change”**

```text
ℱ′ ×_ℰ′ ℰ″ ≃ ℱ″ = ℱ ×_ℰ ℰ″,
𝒢′ ×_ℰ′ ℰ″ ≃ 𝒢″ = 𝒢 ×_ℰ ℰ″,
```

which imply a canonical isomorphism

```text
Hom̲_{ℰ″/-}(ℱ′ ×_ℰ′ ℰ″, 𝒢′ ×_ℰ′ ℰ″)
  ≃ Hom̲_{ℰ″/-}(ℱ ×_ℰ ℰ″, 𝒢 ×_ℰ ℰ″).
```

<!-- original page 157 -->

The verification of this compatibility is immediate and is left to the reader.

The functors just defined are compatible with the pairings defined in the preceding number. More precisely, if `ℱ`, `𝒢`,
`ℋ` are categories over `ℰ` and if one puts

```text
ℱ′ = ℱ ×_ℰ ℰ′,    𝒢′ = 𝒢 ×_ℰ ℰ′,    ℋ′ = ℋ ×_ℰ ℰ′,
```

one has commutativity in the following diagram of functors:

```text
Hom̲_{ℰ/-}(ℱ,𝒢) × Hom̲_{ℰ/-}(𝒢,ℋ)  →  Hom̲_{ℰ/-}(ℱ,ℋ)
        ↓ λ*_{ℱ,𝒢} × λ*_{𝒢,ℋ}              ↓ λ*_{ℱ,ℋ}
Hom̲_{ℰ′/-}(ℱ′,𝒢′) × Hom̲_{ℰ′/-}(𝒢′,ℋ′) → Hom̲_{ℰ′/-}(ℱ′,ℋ′),
```

where the horizontal arrows are the composition functors defined in the preceding number. This commutativity is
expressed by the formulas

```text
(gf)′ = g′f′
```

for `f ∈ Hom_ℰ(ℱ,𝒢)`, `g ∈ Hom_ℰ(𝒢,ℋ)`, a formula which simply expresses the functoriality of base change, and

```text
(v ∗ u)′ = v′ ∗ u′
```

when `u: f → f₁` is an arrow of `Hom̲_{ℰ/-}(ℱ,𝒢)` and `v: g → g₁` is an arrow of `Hom̲_{ℰ/-}(𝒢,ℋ)`. The verification of
this formula follows easily from the definitions.

In what follows, we shall be chiefly interested in `Hom̲_ℰ(ℱ,𝒢)`, and certain remarkable subcategories of it, when
`ℱ = ℰ`. For this reason we introduce a special notation:

```text
Γ̲(𝒢/ℰ) = Hom̲_ℰ(ℰ,𝒢),
Γ(𝒢/ℰ) = Ob(Γ̲(𝒢/ℰ)) = Hom_ℰ(ℰ,𝒢).
```

**Remarks.** When `ℰ` is a point category, i.e. `Ob(ℰ)` and `Fl(ℰ)` are reduced to a single element, which also means
that `ℰ` is a final object of the category `Cat`, then the data of a category over `ℰ` is equivalent to the data of a
category in the ordinary sense, since there will be a unique functor from `ℱ` to `ℰ`. More precisely, `Cat_/ℰ` is then
isomorphic to `Cat`. Moreover, the categories `Hom̲_{ℰ/-}(ℱ,𝒢)` are then none other than the `Hom̲(ℱ,𝒢)`.

<!-- original page 158 -->

Recall then that the fundamental formula

```text
Hom(ℋ, Hom̲(ℱ,𝒢)) ≃ Hom(ℱ × ℋ, 𝒢),
```

functorial in the three arguments appearing in it, allows `Hom̲(ℱ,𝒢)` to be interpreted axiomatically, in terms internal
to the category `Cat`. Thus the familiar formulary for `Hom̲`-categories appears as a special case of a formulary valid
in categories such as `Cat`, where “`Hom̲`-objects”, defined by the preceding formula, exist. There is an analogous
interpretation of `Hom̲_{ℰ/-}(ℱ,𝒢)`, when `ℰ` is again arbitrary, by the formula

```text
Hom(ℋ, Hom̲_{ℰ/-}(ℱ,𝒢)) ≃ Hom_ℰ(ℱ × ℋ, 𝒢),
```

functorial in the three arguments. In this way, the formal properties set out in VI.2 and VI.3 are special cases of more
general results, valid in categories where the objects `Hom̲_{ℰ/-}(ℱ,𝒢)`, for `ℱ` and `𝒢` two objects of the category
over a third object `ℰ`, exist.

## 4. Fiber Categories; Equivalence of ℰ-Categories

<!-- label: VI.4 -->

Let `ℱ` be a category over `ℰ`, and let `S ∈ Ob(ℰ)`. The **fiber category** of `ℱ` at `S` is the subcategory `ℱ_S` of
`ℱ` that is the inverse image of the point subcategory of `ℰ` defined by `S`.

<!-- original page 159 -->

Thus the objects of `ℱ_S` are the objects `ξ` of `ℱ` such that `p(ξ) = S`, and its morphisms are the morphisms `u` of
`ℱ` such that `p(u) = id_S`, i.e. the `S`-morphisms in `ℱ`. Of course, `ℱ_S` is canonically isomorphic to the fiber
product `ℱ ×_ℰ {S}`, where `{S}` denotes the point subcategory of `ℰ` defined by `S`, endowed with its inclusion functor
into `ℰ`. It follows, taking the transitivity of base change into account, that if one makes a base change `λ: ℰ′ → ℰ`,
then for every `S′ ∈ Ob(ℰ′)`, **the projection `pr₁: ℱ′ = ℱ ×_ℰ ℰ′ → ℱ` induces an isomorphism**

```text
ℱ′_{S′} → ℱ_S,    where S = λ(S′).
```

**Proposition.**

<!-- label: VI.4.1 -->

Let `f: ℱ → 𝒢` be an `ℰ`-functor. If `f` is fully faithful, then for every base change `ℰ′ → ℰ`, the corresponding
functor

```text
f′: ℱ′ = ℱ ×_ℰ ℰ′ → 𝒢′ = 𝒢 ×_ℰ ℰ′
```

is fully faithful.

The verification is immediate. More generally, one can show that every projective limit of fully faithful functors, here
`f` and the identity functors in `ℰ` and `ℰ′`, is a fully faithful functor.

One should note that the assertion analogous to 4.1, with “fully faithful” replaced by “equivalence of categories”, is
false, already for `𝒢 = ℰ`. However:

**Proposition.**

<!-- label: VI.4.2 -->

Let `f: ℱ → 𝒢` be an `ℰ`-functor. The following conditions are equivalent:

1. There exists an `ℰ`-functor `g: 𝒢 → ℱ` and `ℰ`-isomorphisms

```text
gf ≃ id_ℱ,    fg ≃ id_𝒢.
```

1. For every category `ℰ′` over `ℰ`, the functor

```text
f′ = f ×_ℰ ℰ′: ℱ′ = ℱ ×_ℰ ℰ′ → 𝒢′ = 𝒢 ×_ℰ ℰ′
```

is an equivalence of categories.

<!-- original page 160 -->

1. `f` is an equivalence of categories, and for every `S ∈ Ob(ℰ)`, the functor `f_S: ℱ_S → 𝒢_S` induced by `f` is an
    equivalence of categories.

1. `f` is fully faithful, and for every `S ∈ Ob(ℰ)` and every `η ∈ Ob(𝒢_S)`, there exist `ξ ∈ Ob(ℱ_S)` and an
    `S`-isomorphism `u: f(ξ) → η`.

**Proof.** Evidently (1) implies that `f` is an equivalence of categories, a notion defined by the same condition but
without requiring the isomorphisms of functors to be `ℰ`-morphisms. On the other hand, it follows from the
functorialities of the preceding number that condition (1) is preserved after base change `ℰ′ → ℰ`. Hence (1) ⇒ (2).
Evidently (2) ⇒ (3), since it is enough to take `ℰ′ = ℰ` and `ℰ′ = {S}`. It is still more trivial that (3) ⇒ (4). It
remains to prove (4) ⇒ (1).

For this, choose for every `η ∈ Ob(𝒢)` an object `g(η) ∈ Ob(ℱ)` and an isomorphism `u(η): f(g(η)) → η` such that
`q(u(η)) = id_S`, where `S = q(η)`. This is possible by the second condition in (4). As is known and immediate, the fact
that `f` is fully faithful implies that `g` can be regarded in a unique way as a functor from `𝒢` to `ℱ`, so that the
`u(η)` define a functorial homomorphism, hence isomorphism,

```text
u: fg ≃ id_𝒢.
```

Moreover, by construction, `g` is an `ℰ`-functor and `u` an `ℰ`-homomorphism. To the preceding data there then
corresponds a functorial isomorphism `v: gf → id_ℱ`, defined by the condition `f ∗ v = u ∗ f`, and one sees at once that
it is also an `ℰ`-morphism. This proves the assertion.

**Definition.**

<!-- label: VI.4.3 -->

If the preceding conditions are satisfied, one says that `f` is an **equivalence of categories over `ℰ`**, or an
**`ℰ`-equivalence**.

**Corollary.**

<!-- label: VI.4.4 -->

Suppose that the projection functor `p: ℱ → ℰ` is a transportable functor, i.e. that for every isomorphism `α: T → S` in
`ℰ` and every object `ξ` in `ℱ_T`, there exists an isomorphism `u` in `ℱ` with source `ξ` such that `p(u) = α`. Then
every `ℰ`-functor `f: ℱ → 𝒢` that is an equivalence of categories is an `ℰ`-equivalence.

This follows

<!-- original page 161 -->

from criterion (4).

**Corollary.**

<!-- label: VI.4.5 -->

Let `f: ℱ → 𝒢` be an `ℰ`-equivalence. Then for every category `ℋ` over `ℰ`, the corresponding functors

```text
Hom̲_{ℰ/-}(𝒢,ℋ) → Hom̲_{ℰ/-}(ℱ,ℋ),
Hom̲_{ℰ/-}(ℋ,ℱ) → Hom̲_{ℰ/-}(ℋ,𝒢)
```

are equivalences of categories.

This follows from criterion (1) by the usual argument.

## 5. Cartesian Morphisms, Inverse Images, Cartesian Functors

<!-- label: VI.5 -->

Let `ℱ` be a category over `ℰ`, with projection functor `p`.

**Definition.**

<!-- label: VI.5.1 -->

Consider a morphism

```text
α: η → ξ
```

in `ℱ`, and let

```text
S = p(ξ),    T = p(η),    f = p(α).
```

One says that `α` is a **cartesian morphism** if, for every `η′ ∈ Ob(ℱ_T)` and every `f`-morphism `u: η′ → ξ`, there
exists a unique `T`-morphism `ū: η′ → η` such that `u = α ∘ ū`.

This therefore means that, for every `η′ ∈ Ob(ℱ_T)`, the map `v ↦ α ∘ v`

```text
(i)  Hom_T(η′,η) → Hom_f(η′,ξ)
```

is bijective. It also means that the pair `(η,α)` **represents, as a functor in `η′`**, the functor `ℱ_T° → Set` given
by the second member.

If, for a given morphism `f: T → S` in `ℰ` and a given `ξ ∈ Ob(ℱ_S)`, such a pair `(η,α)` exists, i.e. a cartesian
morphism `α` in `ℱ` with target `ξ` and with `p(α) = f`, then `η` is determined in `ℱ_T` up to unique isomorphism. One
then says that **the inverse image of `ξ` by `f` exists**, and an object `η` of `ℱ_T` endowed with a cartesian
`f`-morphism `α: η → ξ` is called **an inverse image of `ξ` by `f`**.

<!-- original page 162 -->

Often, once `ℱ` is fixed, one assumes such an inverse image chosen whenever it exists. The inverse image will then be
denoted by symbols such as `f*_ℱ(ξ)`, or simply `f*(ξ)`, or `ξ ×_S T` when these notations cause no confusion. In what
follows, the canonical morphism `α: η → ξ` will then be denoted `α_f(ξ)`.

If for every `ξ ∈ Ob(ℱ_S)` the inverse image of `ξ` by `f` exists, one also says that **the inverse-image functor by `f`
in `ℱ` exists**, and `f*(ξ)` then becomes a **covariant functor in `ξ`**, from `ℱ_S` to `ℱ_T`. This comes from the fact
that the second member in (i) depends covariantly on `ξ`, or more precisely denotes a functor from `ℱ_T° × ℱ_S` to
`Set`.

This functorial dependence of `f*(ξ)` is made explicit as follows. Consider cartesian `f`-morphisms

```text
α: η → ξ,    α′: η′ → ξ′
```

and an `S`-morphism `λ: ξ → ξ′`. Then there exists a unique `T`-morphism `μ: η → η′` such that

```text
α′ μ = λ α,
```

as follows from the fact that `α′` is cartesian.

Also note the following immediate fact. Consider a commutative diagram in `ℱ`

```text
η  --α-->  ξ
|         |
μ         λ
↓         ↓
η′ --α′-> ξ′
```

<!-- original page 163 -->

where `α` and `α′` are `f`-morphisms, `λ` is an `S`-isomorphism, and `μ` is a `T`-isomorphism. **Then `α` is cartesian
if and only if `α′` is cartesian**.

**Definition.**

<!-- label: VI.5.2 -->

An `ℰ`-functor `F: ℱ → 𝒢` is called a **cartesian functor** if it transforms cartesian morphisms into cartesian
morphisms. We denote by `Hom̲_cart(ℱ,𝒢)` the full subcategory of `Hom̲_{ℰ/-}(ℱ,𝒢)` formed by the cartesian functors.

For example, regarding `ℰ` as a category over `ℰ` by means of the identity functor, every morphism of `ℰ` is cartesian.
Thus a cartesian functor from `ℰ` to `ℱ` is a section functor `F: ℰ → ℱ` that transforms every morphism of `ℰ` into a
cartesian morphism. Such a functor is called a **cartesian section** of `ℱ` over `ℰ`.

**Proposition.**

<!-- label: VI.5.3 -->

1. A functor `F: ℱ → 𝒢` that is an `ℰ`-equivalence is a cartesian functor.
1. Let `F`, `G` be two **isomorphic** `ℰ`-functors `ℱ → 𝒢`. If one is cartesian, then so is the other.
1. The composite of two cartesian functors `ℱ → 𝒢` and `𝒢 → ℋ` is a cartesian functor.

Assertion (3) is trivial from the definition; (2) follows from the remark preceding VI.5.2; (1) follows easily from the
definition and criterion VI.4.2 (3). More precisely, a morphism `α` in `ℱ` is cartesian if and only if `F(α)` is
cartesian.

**Corollary.**

<!-- label: VI.5.4 -->

Let `F: ℱ → 𝒢` be an `ℰ`-equivalence. Then for every category `ℋ` over `ℰ`, the corresponding functors `G ↦ G ∘ F` and
`G ↦ F ∘ G` induce equivalences of categories:

```text
Hom̲_cart(𝒢,ℋ) ≃ Hom̲_cart(ℱ,ℋ),
Hom̲_cart(ℋ,ℱ) ≃ Hom̲_cart(ℋ,𝒢).
```

This follows in the usual way from criterion VI.4.2 (1) and from VI.5.3 (1), (2), (3).

<!-- original page 164 -->

One can specify that **the `ℰ`-functor `G: 𝒢 → ℋ` is cartesian if and only if `G ∘ F` is cartesian**, and likewise **an
`ℰ`-functor `G: ℋ → ℱ` is cartesian if and only if `F ∘ G` is cartesian**.

It follows from VI.5.4 (3) that, if one considers the subcategory `Cat^cart_/ℰ` of `Cat_/ℰ` whose objects are the same
as those of `Cat_/ℰ` and whose morphisms are the **cartesian** functors, then, as in VI.2, one has pairings

```text
Hom̲_cart(ℱ,𝒢) × Hom̲_cart(𝒢,ℋ) → Hom̲_cart(ℱ,ℋ)
```

induced by those of VI.2. These pairings allow one to regard `Hom̲_cart(ℱ,𝒢)` as a functor in `ℱ` and `𝒢`, from the
category `(Cat^cart_/ℰ)° × Cat^cart_/ℰ` to `Cat`. We shall need this remark chiefly in the case `ℱ = 𝒢`.

**Definition.**

<!-- label: VI.5.5 -->

Let `ℱ` be a category over `ℰ`. We denote by

```text
Lim←(ℱ/ℰ)
```

the category of cartesian `ℰ`-functors `ℰ → ℱ`, i.e. the cartesian sections of `ℱ` over `ℰ`.

By what has just been said, `Lim←(ℱ/ℰ)` is a functor in `ℱ`, from the category `Cat^cart_/ℰ` to the category `Cat`.

We shall see below the relations between this operation `Lim←` and the notion of projective limit of categories, as well
as numerous examples.

## 6. Fibered Categories and Prefibered Categories. Products and Base Change in Them

<!-- label: VI.6 -->

**Definition.**

<!-- label: VI.6.1 -->

A category `ℱ` over `ℰ` is called a **fibered category**, and the functor `ℱ → ℰ` is then said to be **fibrant**, if it
satisfies the two following axioms:

**Fib I.** For every morphism `f: T → S` in `ℰ`, the inverse-image functor by `f` in `ℱ` exists.

**Fib II.** The composite of two cartesian morphisms is cartesian.

A category `ℱ` over `ℰ` satisfying condition **Fib I** is called a **prefibered category over `ℰ`**.

If `ℱ` is a fibered, respectively prefibered, category over `ℰ`, a subcategory `𝒢` of `ℱ` is called a **fibered
subcategory**, respectively a **prefibered subcategory**, if it is a fibered, respectively prefibered, category over `ℰ`
and, moreover, the inclusion functor is cartesian. If, for example, `𝒢` is a **full** subcategory of `ℱ`, one sees that
this means that, for every morphism `f: T → S` in `ℰ` and every `ξ ∈ Ob(𝒢_S)`, `f*_ℱ(ξ)` is `T`-isomorphic to an object
of `𝒢_T`.

Another interesting case is the following. Let `ℱ` be a fibered category over `ℰ`, and consider the subcategory `𝒢` of
`ℱ` with the same objects and whose morphisms are the **cartesian** morphisms of `ℱ`; in particular the morphisms of
`𝒢_S` are the isomorphisms of `ℱ_S`. One sees at once that this is indeed a fibered subcategory of `ℱ`, because in the
bijection

<!-- original page 165 -->

```text
Hom_T(η′,η) ≃ Hom_f(η′,ξ)
```

relative to a cartesian `f`-morphism `α` in `ℱ`, the `T`-isomorphisms of the first member correspond to the cartesian
morphisms of the second. By definition, the cartesian sections `ℰ → ℱ` then correspond bijectively to arbitrary
`ℰ`-functors `ℰ → 𝒢`. However, note that the natural functor

```text
Hom̲_{ℰ/-}(ℰ,𝒢) → Hom̲_cart(ℰ,ℱ) = Lim←(ℱ/ℰ)
```

is faithful, but in general is not fully faithful, i.e. is not an isomorphism.

**Remarks.** Let `ℱ` be a category over `ℰ`. The following conditions are equivalent:

1. All morphisms of `ℱ` are cartesian.
1. `ℱ` is a fibered category over `ℰ`, and the `ℱ_S` are groupoids, i.e. every morphism in `ℱ_S` is an isomorphism.

One then says that `ℱ` is a category **fibered in groupoids** over `ℰ`.

<!-- original page 166 -->

These are the ones encountered especially in “theory of moduli”. If `ℰ` is a groupoid, one shows that conditions (1) and
(2) are also equivalent to the following:

1. `ℱ` is a groupoid, and the projection functor `p: ℱ → ℰ` is transportable; cf. VI.4.4.

For example, if `ℰ` and `ℱ` are groupoids such that `Ob(ℰ)` and `Ob(ℱ)` are reduced to a point, so that `ℰ` and `ℱ` are
defined, up to isomorphism, by groups `E` and `F`, and the functor `p: ℱ → ℰ` is defined by a group homomorphism
`p: F → E`, then `ℱ` is fibered over `ℰ` if and only if `p` is surjective, i.e. if `p` defines an **extension** of the
group `E` by the group `G = Ker p`.

**Proposition.**

<!-- label: VI.6.2 -->

Let `F: ℱ → 𝒢` be an `ℰ`-equivalence. In order that `ℱ` be a fibered, respectively prefibered, category over `ℰ`, it is
necessary and sufficient that `𝒢` be so.

This follows easily from the definitions and from the remark made above that a morphism `α` in `ℱ` is cartesian if and
only if `F(α)` is.

**Proposition.**

<!-- label: VI.6.3 -->

Let `ℱ₁`, `ℱ₂` be two categories over `ℰ`, and let `α = (α₁,α₂)` be a morphism in `ℱ = ℱ₁ ×_ℰ ℱ₂`. Then `α` is cartesian
if and only if its components are cartesian.

Indeed, let `ξᵢ` be the target and `ηᵢ` the source of `αᵢ`, and let `f: T → S` be the morphism of `ℰ` such that `α₁` and
`α₂` are `f`-morphisms. For every `η′ = (η′₁,η′₂)` in `ℱ_T`, one has a commutative diagram

```text
Hom_T(η′,η)  →  Hom_f(η′,ξ)
     ↓              ↓
Hom_T(η′₁,η₁) × Hom_T(η′₂,η₂)
  → Hom_f(η′₁,ξ₁) × Hom_f(η′₂,ξ₂),
```

where the vertical arrows are bijections. Thus if one of the horizontal arrows is a bijection, the same is true of the
other. This already shows that if `α₁` and `α₂` are cartesian, hence the second horizontal arrow is bijective, then `α`
is cartesian. The converse is seen by taking, in the diagram above, `η′ᵢ = ηᵢ`, whence `Hom_T(η′ᵢ,ηᵢ) ≠ ∅`: first for
`i = 2`, which proves that `α₁` is cartesian, then for `i = 1`, which proves that `α₂` is cartesian.

**Corollary.**

<!-- label: VI.6.4 -->

<!-- original page 167 -->

Let `ℱ = ℱ₁ ×_ℰ ℱ₂`, and let `F = (F₁,F₂)` be an `ℰ`-functor `𝒢 → ℱ`. Then `F` is cartesian if and only if `F₁` and `F₂`
are cartesian. One obtains in this way an isomorphism of categories

```text
Hom̲_cart(𝒢, ℱ₁ ×_ℰ ℱ₂) ≃ Hom̲_cart(𝒢,ℱ₁) × Hom̲_cart(𝒢,ℱ₂),
```

and in particular, taking `𝒢 = ℰ`, an isomorphism of categories

```text
Lim←((ℱ₁ ×_ℰ ℱ₂)/ℰ) ≃ Lim←(ℱ₁/ℰ) × Lim←(ℱ₂/ℰ).
```

**Corollary.**

<!-- label: VI.6.5 -->

Let `ℱ₁` and `ℱ₂` be two fibered, respectively prefibered, categories over `ℰ`. Then their fiber product `ℱ = ℱ₁ ×_ℰ ℱ₂`
is a fibered, respectively prefibered, category over `ℰ`.

These results moreover extend to the case of the fiber product of an arbitrary family of categories over `ℰ`.

**Proposition.**

<!-- label: VI.6.6 -->

Let `ℱ` be a category over `ℰ`, with projection functor `p`, and let `λ: ℰ′ → ℰ` be a functor. Regard `ℱ′ = ℱ ×_ℰ ℰ′` as
a category over `ℰ′` by the projection functor `p′ = p ×_ℰ id_ℰ′`. Let `α′` be a morphism of `ℱ′`. Then `α′` is a
cartesian morphism if and only if its image `α` in `ℱ` is cartesian.

The proof is immediate and is left to the reader.

**Corollary.**

<!-- label: VI.6.7 -->

For every cartesian functor `F: ℱ → 𝒢` of categories over `ℰ`, the functor

```text
F′ = F ×_ℰ ℰ′
```

from `ℱ′ = ℱ ×_ℰ ℰ′` to `𝒢′ = 𝒢 ×_ℰ ℰ′` is cartesian.

Consequently, the functor `Hom̲_ℰ(ℱ,𝒢) → Hom̲_ℰ′(ℱ′,𝒢′)` considered in VI.3 induces a functor

```text
Hom̲_cart(ℱ,𝒢) → Hom̲_cart(ℱ′,𝒢′).
```

In other words, for fixed `ℱ` and `𝒢`, **one may regard**

```text
Hom̲_cart(ℱ ×_ℰ ℰ′, 𝒢 ×_ℰ ℰ′)
```

<!-- original page 168 -->

**as a functor in `ℰ′`, from the category `Cat_/ℰ°` to `Cat`**. If `ℱ` and `𝒢` are also allowed to vary, one finds a
functor from the category

```text
Cat_/ℰ° × (Cat^cart_/ℰ)° × Cat^cart_/ℰ
```

to `Cat`.

When one takes into account the isomorphism

```text
Hom_ℰ′(ℱ′,𝒢′) ≃ Hom_ℰ(ℱ ×_ℰ ℰ′,𝒢)
```

considered in VI.3, the cartesian `ℰ′`-functors from `ℱ′` to `𝒢′` correspond to the `ℰ`-functors `ℱ ×_ℰ ℰ′ → 𝒢` that
transform every morphism whose first projection is a cartesian morphism of `ℱ` into a cartesian morphism of `𝒢`. Taking
`ℱ = ℰ`, one finds, after a change of notation:

**Corollary.**

<!-- label: VI.6.8 -->

`Lim←(ℱ′/ℰ′)` is isomorphic to the full subcategory of `Hom̲_{ℰ/-}(ℰ′,ℱ)` formed by the `ℰ`-functors `ℰ′ → ℱ` that
transform arbitrary morphisms into cartesian morphisms. In particular, if `ℱ` is a fibered category and if `ℱ̃` is the
subcategory of `ℱ` whose morphisms are the cartesian morphisms of `ℱ`, then one has a bijection

```text
Ob Lim←(ℱ′/ℰ′) ≃ Hom_{ℰ/-}(ℰ′,ℱ̃).
```

This makes precise the way in which the expression

```text
Lim←((ℱ ×_ℰ ℰ′)/ℰ′)
```

must be regarded as a functor in `ℰ′` and `ℱ`, from the category `Cat_/ℰ° × Cat^cart_/ℰ` to the category `Cat`. Later we
shall see a more complete functorial dependence with respect to `ℰ′` when `ℱ` is required to be a fibered category.

**Corollary.**

<!-- label: VI.6.9 -->

If `ℱ` is a fibered, respectively prefibered, category over `ℰ`, then `ℱ′ = ℱ ×_ℰ ℰ′` is a fibered, respectively
prefibered, category over `ℰ′`.

**Proposition.**

<!-- label: VI.6.10 -->

Let `ℱ` and `𝒢` be prefibered categories over `ℰ`, and let `F` be a cartesian `ℰ`-functor from `ℱ` to `𝒢`. In order that
`F` be faithful, respectively fully faithful, respectively an `ℰ`-equivalence, it is necessary and sufficient that for
every `S ∈ Ob(ℰ)`, the induced functor

<!-- original page 169 -->

```text
F_S: ℱ_S → 𝒢_S
```

be faithful, respectively fully faithful, respectively an equivalence.

The proof is immediate from the definitions.

To finish this number, we give a few properties of fibered categories using axiom **Fib II**.

**Proposition.**

<!-- label: VI.6.11 -->

Let `ℱ` be a prefibered category over `ℰ`. In order that `ℱ` be fibered, it is necessary and sufficient that it satisfy
the following condition:

**Fib II′.** Let `α: η → ξ` be a cartesian morphism in `ℱ` over the morphism `f: T → S` of `ℰ`. For every morphism
`g: U → T` in `ℰ`, and every `ζ ∈ Ob(ℱ_U)`, the map `u ↦ α ∘ u`

```text
Hom_g(ζ,η) → Hom_{fg}(ζ,ξ)
```

is bijective.

In other words, in a category **fibered** over `ℰ`, cartesian diagrams are characterized by a property a priori stronger
than the one in the definition, which is recovered by taking `g = id_T` in the preceding statement.

**Corollary.**

<!-- label: VI.6.12 -->

Let `ℱ` be a category over `ℰ` and let `α` be a morphism in `ℱ`. In order that `α` be an isomorphism, it is necessary
that `p(α) = f` be an isomorphism and that `α` be cartesian. The converse is true if `ℱ` is fibered over `ℰ`.

Indeed, if `α` is an isomorphism then evidently so is `f = p(α)`. For every `η′ ∈ Ob(ℱ_T)`, the map `u ↦ α ∘ u`

```text
Hom(η′,η) → Hom(η′,ξ)
```

is bijective. Since `f` is an isomorphism, one sees at once that an element of the first member is a `T`-morphism if and
only if its image in the second is an `f`-morphism. Thus one obtains a bijection

```text
Hom_T(η′,η) → Hom_f(η′,ξ),
```

<!-- original page 170 -->

which proves the first assertion. Conversely, suppose that `f` is an isomorphism and that `α` satisfies the condition
stated in **Fib II′**, which means, when `ℱ` is fibered over `ℰ`, that `α` is cartesian. Then one sees at once that for
every `ζ ∈ Ob(ℱ)`, the map `u ↦ α ∘ u` from `Hom(ζ,η)` to `Hom(ζ,ξ)` is bijective, and hence `α` is an isomorphism.

**Corollary.**

<!-- label: VI.6.13 -->

Let `α: η → ξ` and `β: ζ → η` be two composable morphisms in the category `ℱ` fibered over `ℰ`. If `α` is cartesian,
then `β` is cartesian if and only if `αβ` is cartesian.

One uses the definition of cartesian morphisms in the strengthened form VI.6.11.

## 7. Categories Cloven over ℰ

<!-- label: VI.7 -->

**Definition.**

<!-- label: VI.7.1 -->

Let `ℱ` be a category over `ℰ`. A **cleavage** of `ℱ` over `ℰ` means a function that attaches to every `f ∈ Fl(ℰ)` an
inverse-image functor for `f` in `ℱ`, denoted `f*`. The cleavage is said to be **normalized** if `f = id_S` implies
`f* = id_{ℱ_S}`. A **cloven category**, respectively a **normalized cloven category**, means a category `ℱ` over `ℰ`
endowed with a cleavage, respectively with a normalized cleavage.

It is evident that `ℱ` admits a cleavage if and only if `ℱ` is prefibered over `ℰ`, and then `ℱ` admits a normalized
cleavage. The set of cleavages on `ℱ` is in bijective correspondence with the set of subsets `K` of `Fl(ℱ)` satisfying
the following conditions:

1. The `α ∈ K` are cartesian morphisms.
1. For every morphism `f: T → S` in `ℰ` and every `ξ ∈ Ob(ℱ_S)`, there exists a unique `f`-morphism in `K` with target
    `ξ`.

For the cleavage defined by `K` to be normalized, it is necessary and sufficient that `K` also satisfy the condition:

1. The identity morphisms in `ℱ` belong to `K`.

<!-- original page 171 -->

The morphisms that are elements of `K` may be called the **“transport morphisms”** for the cleavage in question.

The notion of isomorphism of cloven categories over `ℰ` is clear. More generally, one can define morphisms of cloven
`ℰ`-categories as functors of `ℰ`-categories `ℱ → 𝒢` that send transport morphisms to transport morphisms. These are, in
particular, cartesian functors. In this way the cloven categories over `ℰ` are the objects of a category, the **category
of cloven categories over `ℰ`**. The reader may spell out the existence of products, tied to the fact that if a category
over `ℰ` is the product of categories `ℱᵢ` over `ℰ`, each endowed with a cleavage, then `ℱ` is endowed with the
corresponding natural cleavage. We also leave to the reader the task of spelling out the notion of base change in cloven
categories.

We shall denote by `α_f(ξ)` the canonical morphism

```text
α_f(ξ): f*(ξ) → ξ.
```

As was said, it is functorial in `ξ`, i.e. one has a functorial homomorphism

```text
α_f: i_T f* → i_S,
```

where for every `S ∈ Ob(ℰ)`, `i_S` denotes the inclusion functor

```text
i_S: ℱ_S → ℱ.
```

Now consider morphisms

```text
f: T → S    and    g: U → T
```

in `ℰ`, and let `ξ ∈ Ob(ℱ_S)`. There then exists a unique `U`-morphism

```text
c_{f,g}(ξ): g*f*(ξ) → (fg)*(ξ)
```

making commutative

<!-- original page 172 -->

the diagram

```text
g*f*(ξ) --α_g(f*(ξ))--> f*(ξ)
   | c_{f,g}(ξ)           | α_f(ξ)
   ↓                      ↓
(fg)*(ξ) --α_{fg}(ξ)-->   ξ,
```

by the definition of `(fg)*(ξ)`. For variable `ξ`, this homomorphism is functorial; that is, one has a homomorphism

```text
c_{f,g}: g*f* → (fg)*
```

of functors `ℱ_S → ℱ_U`. Note at once:

**Proposition.**

<!-- label: VI.7.2 -->

In order that the cloven category `ℱ` over `ℰ` be fibered, it is necessary and sufficient that the `c_{f,g}` be
isomorphisms.

It follows, taking `f` to be an isomorphism and `g` its inverse, and considering the isomorphisms `c_{f,g}` and
`c_{g,f}`:

**Corollary.**

<!-- label: VI.7.3 -->

If `ℱ` is a **fibered** cloven category over `ℰ`, then for every isomorphism `f: T → S` in `ℰ`, `f*` is an equivalence
of categories `ℱ_S → ℱ_T`.

**Proposition.**

<!-- label: VI.7.4 -->

Let `ℱ` be a cloven category over `ℰ`. One has:

```text
A)
  c_{f,id_T}(ξ) = α_{id_T}(f*(ξ)),
  c_{id_S,f}(ξ) = f*(α_{id_S}(ξ)).
```

and

```text
B)  c_{f,gh}(ξ) · c_{g,h}(f*(ξ))
      = c_{fg,h}(ξ) · h*(c_{f,g}(ξ)).
```

In these formulas, `f`, `g`, `h` denote morphisms

```text
V → U → T → S
```

<!-- original page 173 -->

and `ξ` is an object of `ℱ_S`.

In the case of a normalized cleavage, the first and second relations take the simpler form

```text
A′) c_{f,id_T} = id_{f*},    c_{id_S,f} = id_{f*}.
```

As for the third, it is visualized by the commutativity of the diagram

```text
h*g*f*(ξ) --c_{g,h}(f*(ξ))--> (gh)*f*(ξ)
    | h*(c_{f,g}(ξ))              | c_{f,gh}(ξ)
    ↓                             ↓
h*(fg)*(ξ) --c_{fg,h}(ξ)-->    (fgh)*(ξ).
```

In the case of fibered categories, where the `c_{f,g}` are isomorphisms, this commutativity may be expressed intuitively
by saying that **the successive use of isomorphisms of the form `c_{f,g}` does not lead to “contradictory
identifications.”** One may also write this formula without the argument `ξ`, using the convolution product of
homomorphisms of functors:

```text
c_{fg,h} ∘ (h* ∗ c_{f,g}) = c_{f,gh} ∘ (c_{g,h} ∗ f*).
```

The proof of the first two formulas in VI.7.4 is trivial; let us sketch that of the third. For this, consider, in
addition to the square `(D)`, the square of homomorphisms

```text
g*f*(ξ) --α_g(f*(ξ))--> f*(ξ)
   | c_{f,g}(ξ)            | α_f(ξ)
   ↓                       ↓
(fg)*(ξ) --α_{fg}(ξ)-->    ξ,
```

<!-- original page 174 -->

which is commutative by definition of `c_{f,g}(ξ)`. Consider the diagram obtained by joining the vertices of `(D)` to
the corresponding vertices of this square by homomorphisms of the form `α`:

```text
α_h(g*f*(ξ)),       α_{gh}(f*(ξ)),
α_h((fg)*(ξ)),      α_{fgh}(ξ).
```

The four lateral faces of the cube so obtained are also commutative. For the left face, this comes from the fact that
the left column of `(D)` is obtained from the left column of the preceding square by applying `h`, and that `α_h` is a
functorial homomorphism. For the other three faces, this is nothing other than the definition of the operations `c` on
the remaining three sides of `(D)`. Thus the five faces of the cube other than the upper face are commutative. It
follows that the two `(fgh)`-morphisms `h*g*f*(ξ) → (fgh)*(ξ)` defined by `(D)` have the same composite with
`α_{fgh}(ξ): (fgh)*(ξ) → ξ`. Hence they are equal by the definition of `(fgh)*`.

Let us confine ourselves, in what follows, to **normalized** cloven categories. Such a category gives rise to the
following objects:

1. A map `S ↦ ℱ_S` from `Ob(ℰ)` to `Cat`.
1. A map `f ↦ f*`, associating to every `f ∈ Fl(ℰ)`, with source `T` and target `S`, a functor `f*: ℱ_S → ℱ_T`.
1. A map `(f,g) ↦ c_{f,g}`, associating to every pair of arrows `(f,g)` of `ℰ` a functorial homomorphism
    `c_{f,g}: g*f* → (fg)*`.

Moreover, these data satisfy the conditions expressed in formulas A′) and B) above. N.B. If one had not confined oneself
to the case of a normalized cleavage, one would have had to introduce an additional object, namely a function `S ↦ α_S`
associating to every object `S` of `ℰ` a functorial homomorphism `α_S: (id_S)* → id_{ℱ_S}`; condition A′) would then be
replaced by condition A).

<!-- original page 175 -->

We shall now show how one can reconstruct, up to unique isomorphism, the normalized cloven category `ℱ` over `ℰ` from
the preceding objects.

## 8. Cloven Category Defined by a Pseudofunctor ℰ° → Cat

<!-- label: VI.8 -->

For short, call a **pseudofunctor** from `ℰ°` to `Cat`, one should say a **normalized** pseudofunctor, a set of data a),
b), c) as above, satisfying conditions A′) and B). In the preceding number we associated to a normalized cloven category
over `ℰ` a pseudofunctor `ℰ° → Cat`. Here we indicate the inverse construction. We shall leave to the reader the
verification of most of the details, as well as of the fact that these constructions are indeed “inverse” to one
another. More precisely, one should regard the pseudofunctors `ℰ° → Cat` as the objects of a new category, and show that
our constructions provide equivalences, quasi-inverse to one another, between this latter category and the category of
cloven categories over `ℰ` defined in the preceding number.

Put

```text
ℱ° = ∐_{S∈Ob(ℰ)} Ob(ℱ(S)),
```

the sum set of the sets `Ob(ℱ(S))`. N.B. here we write `ℱ(S)`, and not `ℱ_S`, for the value at the object `S` of `ℰ` of
the given pseudofunctor, to avoid notational confusion later. We therefore have an evident map

```text
p°: ℱ° → Ob(ℰ).
```

Let

```text
ξ̄ = (S,ξ),    η̄ = (T,η),    with ξ ∈ Ob(ℱ(S)), η ∈ Ob(ℱ(T)),
```

be two elements of `ℱ°`, and let `f ∈ Hom(T,S)`. Put

```text
h_f(η̄,ξ̄) = Hom_{ℱ(T)}(η, f*(ξ)).
```

<!-- original page 176 -->

If in addition one has a morphism `g: U → T` in `ℰ` and `ζ ∈ Ob(ℱ(U))`, one defines a map, denoted `(u,v) ↦ u ∘ v`,

```text
h_f(η̄,ξ̄) × h_g(ζ̄,η̄) → h_{fg}(ζ̄,ξ̄),
```

i.e. a map

```text
Hom_{ℱ(T)}(η, f*(ξ)) × Hom_{ℱ(U)}(ζ, g*(η))
  → Hom_{ℱ(U)}(ζ, (fg)*(ξ)),
```

by the formula

```text
u ∘ v = c_{f,g}(ξ) · g*(u) · v.
```

That is, `u ∘ v` is the composite of the sequence

```text
ζ --v--> g*(η) --g*(u)--> g*f*(ξ) --c_{f,g}(ξ)--> (fg)*(ξ).
```

On the other hand, put

```text
h(η̄,ξ̄) = ∐_{f∈Hom(T,S)} h_f(η̄,ξ̄).
```

The preceding pairings define pairings

```text
h(η̄,ξ̄) × h(ζ̄,η̄) → h(ζ̄,ξ̄),
```

while the definition of the `h(η̄,ξ̄)` gives an evident map

```text
p_{η̄,ξ̄}: h(η̄,ξ̄) → Hom(T,S).
```

This being said, one verifies the following points:

1. Composition between elements of the `h(η̄,ξ̄)` is **associative**.

1. For every `ξ̄ = (S,ξ)` in `ℱ°`, consider the identity element of

<!-- original page 177 -->

```text
h_{id_S}(ξ̄,ξ̄) = Hom_{ℱ(S)}(id_S*(ξ),ξ) = Hom_{ℱ(S)}(ξ,ξ),
```

and its image in `h(ξ̄,ξ̄)`. This object is a **left and right unit** for composition between elements of the
`h(η̄,ξ̄)`.

This already shows that **one obtains a category** `ℱ` by putting

```text
Ob(ℱ) = ℱ°,
Fl(ℱ) = ∐_{ξ̄,η̄∈ℱ°} h(η̄,ξ̄).
```

N.B. one cannot simply take `Fl(ℱ)` to be the **union** of the sets `h(η̄,ξ̄)`, since these latter sets are not
necessarily disjoint. Moreover:

1. The maps `p°: Ob(ℱ) → Ob(ℰ)` and `p₁ = (p_{η̄,ξ̄}): Fl(ℱ) → Fl(ℰ)` define a **functor** `p: ℱ → ℰ`. In this way `ℱ`
    becomes a category over `ℰ`; moreover, the evident map `h_f(η̄,ξ̄) → Hom(η̄,ξ̄)` induces a **bijection**

```text
h_f(η̄,ξ̄) ≃ Hom_f(η̄,ξ̄).
```

1. The evident maps

```text
Ob(ℱ(S)) → ℱ° = Ob(ℱ),    Fl(ℱ(S)) → Fl(ℱ),
```

where the second is defined by the evident maps

```text
Hom_{ℱ(S)}(ξ,ξ′) = h_{id_S}(ξ̄,ξ̄′) → Hom(ξ̄,ξ̄′),
```

define an **isomorphism**

```text
i_S: ℱ(S) ≃ ℱ_S.
```

1. For every object `ξ̄ = (S,ξ)` of `ℱ`, and every morphism `f: T → S` of `ℰ`, consider

<!-- original page 178 -->

the element `η̄ = (T,η)` of `ℱ_T`, with `η = f*(ξ)`, and the element `α_f(ξ)` of `Hom(η̄,ξ̄)`, image of `id_{f*(ξ)}` by
the morphism

```text
Hom_{ℱ(T)}(f*(ξ),f*(ξ)) = h_f(η̄,ξ̄) → Hom_f(η̄,ξ̄).
```

**This element is cartesian, and it is the identity of `ξ̄` if `f = id_S`**. In other words, the set of the `α_f(ξ)`
defines a **normalized cleavage of `ℱ` over `ℰ`**. Moreover, by construction, one has commutativity in the diagram of
functors

```text
ℱ(S) --f*--> ℱ(T)
 | i_S        | i_T
 ↓            ↓
ℱ_S --f*_ℱ-> ℱ_T,
```

where `f*_ℱ` is the inverse-image functor by `f`, relative to the cleavage considered on `ℱ`. Finally:

1. The homomorphisms `c_{f,g}` given with the pseudofunctor are transformed, by the isomorphisms `i_S`, into the
    functorial homomorphisms `c_{f,g}` associated with the cleavage of `ℱ`.

We restrict ourselves to giving the verification of 1), which is, if anything, less trivial than the others. It suffices
to prove associativity of composition between objects of sets of the form `h_f(η̄,ξ̄)`. Thus consider in `ℰ` morphisms

```text
S ←^f T ←^g U ←^h V
```

and objects

```text
ξ, η, ζ, τ
```

in `ℱ(S)`, `ℱ(T)`, `ℱ(U)`, `ℱ(V)`, and finally elements

```text
u ∈ h_f(η̄,ξ̄) = Hom_{ℱ(T)}(η, f*(ξ)),
v ∈ h_g(ζ̄,η̄) = Hom_{ℱ(U)}(ζ, g*(η)),
w ∈ h_h(τ̄,ζ̄) = Hom_{ℱ(V)}(τ, h*(ζ)).
```

<!-- original page 179 -->

We want to prove the formula

```text
(u ∘ v) ∘ w = u ∘ (v ∘ w),
```

which is an equality in `Hom_{ℱ(V)}(τ,(fgh)*(ξ))`. By the definitions, the two members of this equality are obtained by
composition along the upper and lower contours of the diagram below:

```text
τ --w--> h*(ζ) --h*(v)--> h*g*(η) --h*g*(u)--> h*g*f*(ξ) --h*(c_{f,g}(ξ))--> h*(fg)*(ξ)
 \____________________ v∘w ____________________/       | c_{g,h}(f*(ξ))              | c_{fg,h}(ξ)
                         ↓                              ↓                             ↓
                  (gh)*(η) --(gh)*(u)-->        (gh)*f*(ξ) --c_{f,gh}(ξ)-->       (fgh)*(ξ).
```

The middle square is commutative because `c_{g,h}` is a functorial homomorphism, and the square on the right is
commutative by condition B) for a pseudofunctor. This gives the asserted result.

Of course, it remains to specify, when the pseudofunctor considered already comes from a normalized cloven category `ℱ′`
over `ℰ`, how one obtains a natural isomorphism between `ℱ′` and `ℱ`. We leave the details to the reader.

We likewise leave to the reader the interpretation, in terms of pseudofunctors, of the notion of inverse image of a
cloven category `ℱ` over `ℰ` by a base-change functor `ℰ′ → ℰ`.

## 9. Example: Cloven Category Defined by a Functor ℰ° → Cat; Split Categories over ℰ

<!-- label: VI.9 -->

Suppose one has a functor

```text
φ: ℰ° → Cat.
```

It then defines a pseudofunctor by putting

```text
ℱ(S) = φ(S),    f* = φ(f),    c_{f,g} = id_{(fg)*}.
```

<!-- original page 180 -->

Thus the construction of the preceding number gives us a category `ℱ` cloven over `ℰ`, said to be associated with the
functor `φ`. For a cloven category over `ℰ` to be isomorphic to a cloven category defined by a functor `φ: ℰ° → Cat`, it
is manifestly necessary and sufficient that it satisfy the conditions

```text
(fg)* = g*f*,    c_{f,g} = id_{(fg)*}.
```

In terms of the set `K` of transport morphisms, this also simply means that **the composite of two transport morphisms
is a transport morphism**. A cleavage of a category `ℱ` over `ℰ` satisfying the preceding condition is called a
**splitting** of `ℱ` over `ℰ`, and a category `ℱ` over `ℰ` endowed with a splitting is called a **split category over
`ℰ`**. It is therefore a special case of the notion of cloven category. The category of split categories over `ℰ` is
therefore equivalent to `Hom̲(ℰ°,Cat)`. Note that a split category over `ℰ` is a fortiori a cloven category over `ℰ`.

If `ℱ` is a fibered category over `ℰ`, there does not always exist a splitting on `ℱ`. Suppose for example that `Ob(ℰ)`
and `Ob(ℱ)` are reduced to one element, and that the set of endomorphisms of that element is a group `E`, respectively
`F`, so that the projection functor `p` is given by a group homomorphism `p: F → E`, surjective since `p` is fibrant.
One verifies at once that the set of cleavages of `ℱ` over `ℰ` is in bijective correspondence with the set of maps
`s: E → F` such that `ps = id_E`, i.e. the set of “systems of representatives” for the classes modulo the subgroup `G`
that is the kernel of the surjective homomorphism `p: F → E`. A cleavage is a splitting if and only if `s` is a group
homomorphism. To say that a splitting exists therefore means that the group extension `F` of `E` by `G` is trivial,
which is expressed, when `G` is commutative, by the vanishing of a certain cohomology class in `H²(E,G)`, where `G` is
regarded as a group on which `E` operates.

Suppose, however, that `ℱ` is a fibered category over `ℰ` such that the

<!-- original page 181 -->

`ℱ_S` are **rigid** categories, i.e. the automorphism group of every object of `ℱ_S` is reduced to the identity. It is
then easy to prove that `ℱ` admits a splitting over `ℰ`. Indeed, one first observes that the question of existence of a
splitting is not changed if `ℱ` is replaced by an `ℰ`-equivalent category. This reduces us in the present case to the
case where the `ℱ_S` are rigid **and reduced** categories, i.e. two isomorphic objects in `ℱ_S` are identical. But if
`G` is a rigid and reduced category, every isomorphism between two functors `H → G`, where `H` is any category, is an
identity. It follows that if `ℱ` is a fibered category over `ℰ` whose fiber categories are rigid and reduced, then there
exists a **unique** cleavage of `ℱ` over `ℰ`, which is necessarily a splitting. Thus `ℱ` is isomorphic to the category
defined by a functor `φ: ℰ° → Cat` such that the `φ(S)` are rigid and discrete categories, and the functor `φ` is
defined up to isomorphism.

## 10. Co-Fibered Categories, Bi-Fibered Categories

<!-- label: VI.10 -->

Consider a category `ℱ` over `ℰ`, with projection functor

```text
p: ℱ → ℰ.
```

It defines a category `ℱ°` over `ℰ°` by the projection functor

```text
p°: ℱ° → ℰ°.
```

A morphism `α: η → ξ` in `ℱ` is said to be **co-cartesian** if it is a cartesian morphism for `ℱ°` over `ℰ°`. Spelling
this out, one sees that it means that for every object `ξ′` of `ℱ_S`, the map `u ↦ u ∘ α`

```text
Hom_S(ξ,ξ′) → Hom_f(η,ξ′)
```

is bijective. One then also says that `(ξ,α)` is a **direct image** of `η` by `f`, in the category `ℱ` over `ℰ`. If it
exists for every `η` in `ℱ_T`, one says that the direct-image functor by `f` exists; once it has been chosen, this
functor is denoted

<!-- original page 182 -->

```text
f*_ℱ    or    f_*.
```

It is therefore defined by an isomorphism of bifunctors on `ℱ_T° × ℱ_S`:

```text
Hom_S(f_*(η),ξ) ≃ Hom_f(η,ξ).
```

Thus, if `f_*` exists, then for `f*` to exist it is necessary and sufficient that `f_*` admit an adjoint functor, i.e.
that there exist a functor `f*: ℱ_S → ℱ_T` and an isomorphism of bifunctors

```text
Hom_S(f_*(η),ξ) ≃ Hom_T(η,f*(ξ)).
```

Let `g: U → T` be another morphism in `ℰ`, and suppose that the inverse and direct images by `f`, `g`, and `fg` exist.
Consider then the functorial homomorphisms

```text
c^{f,g}: f_* g_* ← (fg)_*,
c_{f,g}: g* f* → (fg)*.
```

One observes that, if `f_* g_*` and `g* f*` are regarded as a pair of adjoint functors, and likewise `(fg)_*` and
`(fg)*`, then the two preceding homomorphisms are adjoint to one another. Thus one is an isomorphism if and only if the
other is. In particular:

**Proposition.**

<!-- label: VI.10.1 -->

Suppose that the category `ℱ` over `ℰ` is prefibered and co-prefibered. In order that it be fibered, it is necessary and
sufficient that it be co-fibered.

Of course, `ℱ` is said to be co-prefibered, respectively co-fibered, over `ℰ` if `ℱ°` is prefibered, respectively
fibered, over `ℰ`. We shall say that `ℱ` is **bi-fibered** over `ℰ` if it is both fibered and co-fibered over `ℰ`.

## 11. Various Examples

<!-- label: VI.11 -->

### a) Categories of Arrows of ℰ

Let `ℰ` be a category. Denote by `Δ¹` the category associated with the totally ordered set with two elements `[0,1]`. It
therefore has two objects `0` and `1`, and besides the two identity morphisms one arrow `(0,1)` with source `0` and
target `1`. Let

<!-- original page 183 -->

```text
Ar(ℰ) = Hom̲(Δ¹,ℰ).
```

This is called the **category of arrows of** `ℰ`. The object `1` of `Δ¹` defines a canonical functor, called the
**target functor**

```text
Ar(ℰ) → ℰ
```

the functor defined by the object `0` of `Δ¹` being called the **source functor**. For every object `S` of `ℰ`, the
fiber category `Ar(ℰ)_S` is canonically isomorphic to the category `ℰ_/S` of objects of `ℰ` over `S`.

Consider a morphism `f: T → S` in `ℰ`. To it there corresponds a canonical functor

```text
f_*: ℰ_/T = ℱ_T → ℰ_/S = ℱ_S
```

and a functorial isomorphism

```text
Hom_S(f_*(η),ξ) ≃ Hom_f(η,ξ),
```

which therefore makes `f_*` a direct-image functor for `f` in `ℱ`. Moreover, here

```text
(id_S)_* = id_{ℱ_S},    (fg)_* = f_* g_*,    c^{f,g} = id_{(fg)},
```

i.e. `ℱ` is endowed with a co-splitting over `ℰ`. A fortiori, `ℱ` is co-fibered over `ℰ`. Note now that the set of
morphisms in `ℱ` is in bijective correspondence with the set of commutative square diagrams in `ℰ`:

```text
Y --f′--> X
| v      | u
↓        ↓
T --f--> S.
```

<!-- original page 184 -->

By definition, the morphism in question is cartesian if the square is cartesian in `ℰ`, i.e. if it makes `Y` a fiber
product of `X` and `T` over `S`. The inverse-image functor `f*` therefore exists if and only if, for every object `X`
over `S`, the fiber product `X ×_S T` exists. It follows from VI.10.1 that if the product of two objects over a third
always exists in `ℰ`, i.e. if `ℱ` is prefibered over `ℰ`, then `ℱ` is even fibered over `ℰ`.

### b) Category of Presheaves or Sheaves on Variable Spaces

Let `ℰ = Top` be the category of topological spaces. If `T` is a topological space, we denote by `𝒰(T)` the category of
open subsets of `T`, whose morphisms are inclusion maps. If `𝒞` is a category, a functor `𝒰(T)° → 𝒞` is called a
**presheaf** on `T` with values in `𝒞`, and a **sheaf** if it satisfies a left-exactness condition that we shall not
repeat here.

The **category `𝒫(T)` of presheaves on `T` with values in `𝒞`** is, by definition, the category `Hom̲(𝒰(T)°,𝒞)`, and the
category `ℱ(T)` of sheaves on `T` with values in `𝒞` is the full subcategory whose objects are the objects of
`Hom̲(𝒰(T)°,𝒞)` that are sheaves. If `f: T → S` is a morphism in `ℰ`, i.e. a continuous map of topological spaces, then
by the increasing map `U ↦ f⁻¹(U)` there corresponds to it a functor `𝒰(S) → 𝒰(T)`, whence a functor

```text
f_*: Hom̲(𝒰(T)°,𝒞) → Hom̲(𝒰(S)°,𝒞)
```

called the **direct-image functor of presheaves by** `f`. One sees at once that the direct image of a sheaf is a sheaf.
Thus the functor `f_*: 𝒫(T) → 𝒫(S)` induces a functor, also denoted

```text
f_*: ℱ(T) → ℱ(S).
```

Moreover, one verifies trivially, by associativity of composition of functors, that for a second continuous map
`g: U → T` one has the identity

```text
(gf)_* = g_* f_*,    and likewise    (id_S)_* = id_{𝒫(S)}.
```

In this way one obtains a functor

```text
S ↦ 𝒫(S)
```

respectively

```text
S ↦ ℱ(S)
```

<!-- original page 185 -->

from `ℰ` to `Cat`. In fact, we are interested in the corresponding functor

```text
S ↦ 𝒫(S)°,    respectively    S ↦ ℱ(S)°.
```

It defines a co-fibered, indeed co-split, category over the category of topological spaces, called the **co-fibered
category of presheaves**, respectively **sheaves**, **with values in** `𝒞`, understood as on variable spaces. Spelling
out the construction of VI.8, one sees that a morphism from a presheaf `B` on `T` to a presheaf `A` on `S` is a pair
`(f,u)` formed by a continuous map from `T` to `S` and a morphism `u: A → f_*(B)` in the category `𝒫(S)`. This
description is equally valid for morphisms of sheaves, `ℱ` being a full subcategory of `𝒫`.

In the most important cases, the category `𝒫` and the category `ℱ` over `ℰ` are also fibered categories; that is, for
every continuous map, the direct-image functors `𝒫(T) → 𝒫(S)` and `ℱ(T) → ℱ(S)` have an adjoint functor, then denoted
`f*` and called the inverse-image functor of presheaves, respectively the inverse-image functor of sheaves, by the
continuous map `f`. This functor exists, for example, if `𝒞 = Set`. One can show that the functor `f*: 𝒫(S) → 𝒫(T)`
exists whenever inductive limits, relative to diagrams in the Universe under consideration, exist in `𝒞`. The question
is less easy for `ℱ`. Indeed, even in the case `𝒞 = Set`, the inverse image of a presheaf that is a sheaf is not in
general a sheaf; in other words, the inverse-image functor of sheaves is not isomorphic to the functor induced by the
inverse-image functor of presheaves, despite the common notation `f*`. Thus `ℱ` is a co-fibered subcategory of `𝒫`, but
not a fibered subcategory; i.e. **the inclusion functor `ℱ → 𝒫` is not fibrant**.

The co-fibered category `𝒫` can be deduced from a more general co-fibered, or rather fibered, category obtained as
follows. For every category `𝒰` in the fixed Universe, put

```text
𝒫(𝒰) = Hom̲(𝒰,𝒞),
```

and

<!-- original page 186 -->

note that `𝒰 ↦ 𝒫(𝒰)` is naturally a contravariant functor in `𝒰`, from the category `Cat` to `Cat`. It therefore defines
a split category over `ℰ = Cat`, which we shall denote `Cat_//𝒞`. The objects of this category are pairs `(𝒰,p)`, where
`𝒰` is a category and `p: 𝒰 → 𝒞` is a functor; a morphism from `(𝒰,p)` to `(𝒱,q)` is essentially a pair `(f,u)`, where
`f` is a functor `𝒰 → 𝒱` and `u` is a homomorphism of functors `u: p → qf`. We leave to the reader the task of spelling
out the composition of morphisms in `Cat_//𝒞`.

The projection functor

```text
ℱ = Cat_//𝒞 → ℰ = Cat
```

sends the pair `(𝒰,p)` to the object `𝒰`. The fiber category at `𝒰` is the category `Hom̲(𝒰,𝒞)`, up to isomorphism. When
inductive limits exist in `𝒞`, one shows easily that the fibered category `Cat_//𝒞` over `Cat` is also co-fibered over
`Cat`; i.e. one can define the notion of **direct image of a functor** `p: 𝒰 → 𝒞` by a functor `f: 𝒰 → 𝒱`.

The category of presheaves is deduced from the preceding fibered category by the base change

```text
Top° → Cat
```

the functor `S ↦ 𝒰(S)` defined above. This gives a fibered category over `Top°`, and by passing to the opposite category
one obtains the co-fibered category `𝒫` of presheaves over `Top`. The notion of inverse image of a functor corresponds
to that of direct image of a presheaf; the notion of direct image of a functor corresponds to that of inverse image of a
presheaf.

### c) Objects with Operators over an Object with Operators

Let `ℱ` be a category over `ℰ`, and let `S` be an object of `ℰ` on which a group `G` operates, on the left to fix ideas.
This object with operators can be interpreted as corresponding to a functor `λ: ℰ′ → ℰ` from the category `ℰ′` defined
by `G`, with a single object and `G` as its group of endomorphisms, to the category `ℰ`. It therefore defines by base
change a category `ℱ′` over `ℰ′`, which is fibered, respectively co-fibered, when `ℱ` is so over `ℰ`.

<!-- original page 187 -->

A section of `ℰ′` over `ℱ′`, necessarily cartesian, since `ℰ′` is a groupoid and every isomorphism in `ℱ′` is cartesian
by VI.6.12, can also be interpreted as an `ℰ`-functor `ℰ′ → ℱ` over `λ`, or also as an object with operators `ξ` in `ℱ`
“over” the object with operators `S`.

### d) Pairs of Quasi-Inverse Adjoint Functors; Autodualities

When the base category `ℰ` is reduced to two objects `a`, `b` and, besides the identity arrows, to two isomorphisms
`f: a → b` and `g: b → a` inverse to one another, i.e. `ℰ` is a connected rigid groupoid with two objects, a normalized
cloven category over `ℰ` is essentially the same thing as the system formed by two categories `ℱ_a` and `ℱ_b` and a
**pair of adjoint functors** `G: ℱ_a → ℱ_b` and `F: ℱ_b → ℱ_a` that are equivalences of categories, hence quasi-inverse
to one another. One takes for `ℱ_a` and `ℱ_b` the fiber categories of `ℱ`, for `F` and `G` the functors `f*` and `g*`,
and the two isomorphisms

```text
u: FG ≃ id_{ℱ_a},    v: GF ≃ id_{ℱ_b}
```

are `c_{g,f}` and `c_{f,g}`. The two usual compatibility conditions between `u` and `v` are nothing other than condition
VI.7.4 B) for the composites `fgf` and `gfg`. It is easy to show that these conditions suffice to imply that one indeed
has a pseudofunctor `ℰ° → Cat`.

An interesting case is the one in which

```text
ℱ_b = ℱ_a°,    G = F°,    v = u°.
```

An **autoduality** in a category `𝒞` means the data of a functor `D: 𝒞 → 𝒞°` and an isomorphism `u: DD° ≃ id_𝒞` such
that `u` and the isomorphism `u°: D°D ≃ id_𝒞°` make `(D,D°)` a pair of adjoint functors, necessarily quasi-inverse to
one another. This condition is written

```text
D(u(x)) = u(D(x))    for every x ∈ Ob(𝒞).
```

### e) Categories over a Discrete Category ℰ

<!-- original page 188 -->

One says that `ℰ` is a **discrete category** if every arrow in it is an identity arrow, so that `ℰ` is defined up to
unique isomorphism by knowing the set `I = Ob(ℰ)`. The data of a category `ℱ` over `ℰ` is therefore equivalent, up to
unique isomorphism, to the data of a family of categories `ℱᵢ`, `i ∈ I`, the fiber categories. Every category `ℱ` over
`ℰ` is fibered; every `ℰ`-functor `ℱ → 𝒢` is cartesian; one has a canonical isomorphism

```text
Hom̲_{ℰ/-}(ℱ,𝒢) ≃ ∏ᵢ Hom̲(ℱᵢ,𝒢ᵢ).
```

In particular, one obtains

```text
Γ̲(ℱ/ℰ) = Lim←(ℱ/ℰ) ≃ ∏ᵢ ℱᵢ.
```

### f) Suppose that ℰ Has Exactly Two Objects S and T

Suppose that, besides the identity morphisms, `ℰ` has one morphism `f: T → S`. Then a category `ℱ` over `ℰ` is defined,
up to unique `ℰ`-isomorphism, by the data of two categories `ℱ_S` and `ℱ_T` and a bifunctor `H(η,ξ)` on `ℱ_T° × ℱ_S`
with values in `Set`. Indeed, if `ℱ` is a category over `ℰ`, one associates to it the two fiber categories `ℱ_S` and
`ℱ_T` and the bifunctor `H(η,ξ) = Hom_f(η,ξ)`. We leave to the reader the task of spelling out the construction in the
opposite direction. For the category in question to be fibered, or prefibered, which comes to the same thing, it is
necessary and sufficient that the functor `H` be representable with respect to the argument `ξ`. For it to be
co-fibered, it is necessary and sufficient that `H` be representable with respect to the argument `η`.

### g)

Let `ℱ = 𝒞 × ℰ`, regarded as a category over `ℰ` by means of `pr₂`. Then `ℱ` is fibered and co-fibered over `ℰ`, and is
even endowed with a canonical splitting and co-splitting, corresponding to the constant functor on `ℰ`, respectively on
`ℰ°`, with values in `Cat` and value `𝒞`. One has

```text
Γ̲(ℱ/ℰ) ≃ Hom̲(ℰ,𝒞),
```

and

<!-- original page 189 -->

`Lim←(ℱ/ℰ)` corresponds to the full subcategory formed by the functors `F: ℰ → 𝒞` that transform arbitrary morphisms
into isomorphisms.

## 12. Functors on a Cloven Category

<!-- label: VI.12 -->

Let `ℱ` be a normalized cloven category over `ℰ`. For every object `S` of `ℰ`, denote by

```text
i_S: ℱ_S → ℱ
```

the inclusion functor. Thus one has a functorial homomorphism, for every morphism `f: T → S` in `ℰ`,

```text
α_f: i_T f* → i_S,
```

where `f*` is the base-change functor `ℱ_S → ℱ_T` for `f` defined by the cleavage. Let now

```text
F: ℱ → 𝒞
```

be a functor from `ℱ` to a category `𝒞`. Put, for every `S ∈ Ob(ℰ)`,

```text
F_S = F ∘ i_S: ℱ_S → 𝒞,
```

and for every `f: T → S` in `ℰ`,

```text
φ_f = F ∗ α_f: F_T f* → F_S.
```

Thus to every functor `F: ℱ → 𝒞` there is associated a family `(F_S)` of functors `ℱ_S → 𝒞`, and a family `(φ_f)` of
homomorphisms of functors `F_T f* → F_S`. These families satisfy the following conditions:

a) `φ_{id_S} = id_{F_S}`.

b) For two morphisms `f: T → S` and `g: U → T` in `ℰ`, one has commutativity in the square of functorial homomorphisms:

```text
F_U g* f* --F_U ∗ c_{f,g}--> F_U(fg)*
    | φ_g ∗ f*                  | φ_{fg}
    ↓                           ↓
F_T f* ------φ_f-------------> F_S.
```

<!-- original page 190 -->

The first relation is trivial, and the second relation is obtained by applying the functor `F` to the commutative
diagram

```text
g*f*(ξ) --c_{f,g}(ξ)--> (fg)*(ξ)
   | α_g(f*(ξ))             | α_{fg}(ξ)
   ↓                        ↓
f*(ξ) --α_f(ξ)----------->  ξ
```

for variable `ξ` in `ℱ_S`.

If `G` is a second functor `ℱ → 𝒞`, giving rise to functors `G_S: ℱ_S → 𝒞` and functorial homomorphisms
`ψ_f: G_T f* → G_S`, and if `u: F → G` is a functorial homomorphism, then to it there correspond the functorial
homomorphisms `u ∗ i_S`:

```text
u_S: F_S → G_S.
```

One checks at once that, for every morphism `f: T → S` in `ℰ`, one has commutativity in the squares

```text
c)  F_T f* --φ_f--> F_S
       | u_T ∗ f*      | u_S
       ↓               ↓
    G_T f* --ψ_f--> G_S.
```

**Proposition.**

<!-- label: VI.12.1 -->

Let `ℋ(ℱ,𝒞)` be the category whose objects are pairs of families `(F_S)`, `S ∈ Ob(ℰ)`, of functors `ℱ_S → 𝒞`, and of
families `(φ_f)`, `f ∈ Fl(ℰ)`, of functorial homomorphisms `F_T f* → F_S` satisfying conditions **a)** and **b)**, and
whose morphisms are the families `(u_S)`, `S ∈ Ob(ℰ)`, of homomorphisms `F_S → G_S` verifying the commutativity
condition **c)** written above; composition of morphisms is by composition of homomorphisms of functors `ℱ_S → 𝒞`. Then
the two laws just described define an **isomorphism** `K` from the category `Hom̲(ℱ,𝒞)` to the category `ℋ(ℱ,𝒞)`.

<!-- original page 191 -->

It is trivial that this is indeed a **functor** from the first category to the second. This functor is fully faithful:
for given `F`, `G`, the map `Hom(F,G) → Hom(K(F),K(G))` is trivially injective. To show that it is surjective, it
suffices to note that commutativity condition c) expresses the functoriality of the maps

```text
u(ξ) = u_S(ξ): F(ξ) = F_S(ξ) → G(ξ) = G_S(ξ)
```

for homomorphisms of the form `α_f(ξ)` in `ℱ`. On the other hand, one has functoriality on each fiber category, i.e. for
morphisms in `ℱ` that are `T`-morphisms with `T ∈ Ob(ℰ)`. Hence one has functoriality for every morphism in `ℱ`, since
an `f`-morphism, where `f: T → S` is a morphism in `ℰ`, is uniquely a composite of a morphism `α_f(ξ)` and a
`T`-morphism.

It remains therefore to prove that the functor `K` is bijective on objects. The preceding argument already shows that
`K` is injective on objects; it remains to prove that it is surjective. That is, suppose we start from a system `(F_S)`,
`(φ_f)` satisfying a) and b), and define a map `Ob(ℱ) → Ob(𝒞)` by

```text
F(ξ) = F_S(ξ)    for ξ ∈ Ob(ℱ_S) ⊂ Ob(ℱ),
```

and a map `Fl(ℱ) → Fl(𝒞)` by

```text
F(α_f(ξ)u′) = φ_f(ξ) F_T(u′),
```

for every morphism `f: T → S` in `ℰ`, every object `ξ` of `ℱ_S`, and every `T`-morphism `u′` with target `f*(ξ)`. Then
one obtains a **functor** `F` from `ℱ` to `𝒞`. Indeed, the relation `F(id_ξ) = id_{F(ξ)}` is trivial; it remains to
prove multiplicativity `F(uv) = F(u)F(v)` when one has an `f`-morphism `u: η → ξ` and a `g`-morphism `v: ζ → η`, with
`f: T → S` and `g: U → T` morphisms of `ℰ`. Putting `w = uv`, one has

```text
u = α_f(ξ)u′,    v = α_g(η)v′,    w = α_{fg}(ξ)w′
```

<!-- original page 192 -->

with

```text
w′ = c_{f,g}(ξ) g*(u′) v′        cf. VI.8.
```

With this notation, one must prove commutativity of the outer contour of the diagram below:

```text
F_U(ζ) --F_U(v′)--> F_U g*(η) --F_U g*(u′)--> F_U g*f*(ξ) --F_U(c_{f,g}(ξ))--> F_U(fg)*(ξ)
   \________________ F(v) ________________/        | φ_g(f*(ξ))                         | φ_{fg}(ξ)
                                                    ↓                                    ↓
                                      F_T(η) --F_T(u′)--> F_T f*(ξ) --φ_f(ξ)--> F_S(ξ).
```

The left triangle is commutative by definition of `F(v)`; the middle square is commutative because it is deduced from
the homomorphism `u′` by the functorial homomorphism `φ_g`; finally the right square is commutative by condition b). The
desired conclusion follows.

Suppose now that `𝒞` is also a normalized cloven category over `ℰ`, which from now on we shall call `𝒢`, and that we are
interested in `ℰ`-functors from `ℱ` to `𝒢`. If `F` is such a functor, it induces functors

```text
F_S: ℱ_S → 𝒢_S
```

on the fiber categories. On the other hand, for every morphism `f: T → S` in `ℰ` and every object `ξ` in `ℱ_S`, the
`f`-morphism `F(α_f(ξ))` factors uniquely through a `T`-morphism

```text
φ_f(ξ): F_T(f*_ℱ(ξ)) → f*_𝒢(F_S(ξ)),
```

where the subscript `ℱ` or `𝒢` indicates the cloven category in which the inverse-image functor is being taken. Hence
one obtains a functorial homomorphism of functors from `ℱ_S` to `𝒢_T`:

```text
φ_f: F_T f*_ℱ → f*_𝒢 F_S.
```

<!-- original page 193 -->

The two systems `(F_S)` and `(φ_f)` satisfy the following conditions:

a′) `φ_{id_S} = id_{F_S}`.

b′) For two morphisms `f: T → S` and `g: U → T` in `ℰ`, one has commutativity in the following diagram of functorial
homomorphisms:

```text
F_U g*_ℱ f*_ℱ --F_U ∗ c^ℱ_{f,g}--> F_U(fg)*_ℱ
       | φ_g ∗ f*_ℱ                         | φ_{fg}
       ↓                                    ↓
g*_𝒢 F_T f*_ℱ
       | g*_𝒢 ∗ φ_f
       ↓
g*_𝒢 f*_𝒢 F_S --c^𝒢_{f,g} ∗ F_S--> (fg)*_𝒢 F_S.
```

We leave to the reader the verification, as well as the statement and proof of the analogue of Proposition VI.12.1,
which implies that one obtains in this way a bijective correspondence between the set of `ℰ`-functors from `ℱ` to `𝒢`
and the set of systems `(F_S)`, `(φ_f)` satisfying conditions a′) and b′) above. Of course, in this correspondence, the
cartesian functors are characterized by the property that the homomorphisms `φ_f` are isomorphisms.

**Remark.** Of course, it is usually better to reason directly on fibered categories without using explicit cleavages.
This avoids, in particular, having to appeal, for the simple notion of ℰ-functor or cartesian ℰ-functor, to a heavy
interpretation such as the one above. It is in order to avoid unbearable heaviness, and to obtain more intrinsic
statements,

<!-- original page 194 -->

that we have had to give up starting, as in [VI.2], from the notion of cloven category, called “fibered category” in the
cited text, which now takes second place in favor of the notion of fibered category. It is moreover probable that,
contrary to the still prevailing usage, tied to old habits of thought, it will eventually prove more convenient in
universal problems not to put the emphasis on **one** solution supposed chosen once and for all, but to put all
solutions on an equal footing.

## Bibliography

<!-- label: VI.13 -->

[VI.1] A. Grothendieck, “Sur quelques points d’algèbre homologique,” Tôhoku Math. J. **9** (1957), 119–221.

[VI.2] A. Grothendieck, “Technique de descente et Théorèmes d’existence, I,” Séminaire Bourbaki 190, December 1959.

<!-- Exposé VII does not exist. -->

[^vi-1-1]: The eventual authors are C. Chevalley and P. Gabriel. The book is due out in the year 3000. Meanwhile, cf.
    also SGA 4 I.
