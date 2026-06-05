# Exposé VI. Fibered Categories and Descent

<!-- label: VI -->

<!-- original page 145 -->

## 0. Introduction

Contrary to what had been announced in the introduction to the preceding exposé, it has turned out to be impossible to
do descent in the category of preschemes, even in particular cases, without first having developed with sufficient care
the language of descent in general categories.

The notion of “descent” supplies the general framework for all procedures of “gluing” objects, and consequently of
“gluing” categories. The most classical case of gluing is relative to the data of a topological space $X$ and a covering
of $X$ by open subsets `Xᵢ`. Suppose one is given, for every $i$, a fiber space, say, `Eᵢ` over `Xᵢ`, and for every pair
$(i,j)$ an isomorphism $f_{ji}$ from $E_{i}|X_{ij}$ to $E_{j}|X_{ij}$, where $X_{ij} = X_{i} \cap X_{j}$, satisfying the
well-known transitivity condition, written in abbreviated form $f_{kj} f_{ji} = f_{ki}$. One knows that there exists a
fiber space $E$ on $X$, defined up to isomorphism by the condition that one have isomorphisms $f_{i}: E|X_{i} \simeq
E_{i}$ satisfying the relations $f_{ji} = f_{j} f^{-1}_{i}$, with the usual abuse of notation.

Let $X'$ be the sum space of the `Xᵢ`; it is therefore a fiber space over $X$, i.e. endowed with a continuous map $X'
\to X$. The data of the `Eᵢ` can be interpreted more concisely as a fiber space $E'$ over $X'$, and the data of the
$f_{ji}$ as an isomorphism between the two inverse images, by the two canonical projections, $E''_{1}$ and $E''_{2}$ of
$E'$ on $X'' = X' \times_{X} X'$. The gluing condition can then be written as an identity between isomorphisms of fiber
spaces $E'''_{1}$ and $E'''_{3}$ over the triple fiber product $X''' = X' \times_{X} X' \times_{X} X'$, where $E'''_{i}$
denotes the inverse image of $E'$ on $X'''$ by the canonical projection of index $i$. The construction of $E$ from $E'$
and $f$ is a typical case of a “descent” procedure.

<!-- original page 146 -->

Moreover, starting from a fiber space $E$ on $X$, one says that $X$ is “locally trivial”, with fiber $F$, if there
exists an open covering $(X_{i})$ of $X$ such that the $E|X_{i}$ are isomorphic to $F \times X_{i}$, or what amounts to
the same thing, such that the inverse image $E'$ of $E$ on $X' = \coprod_{i} X_{i}$ is isomorphic to $X' \times F$.

Thus the notion of “gluing” objects, like that of “localization” of a property, is tied to the study of certain types of
“base changes” $X' \to X$. In algebraic geometry, many other types of base change, and notably faithfully flat morphisms
$X' \to X$, must be regarded as corresponding to a procedure of “localization” relative to preschemes, or other objects,
“over” $X$. This type of localization is used just as much as ordinary topological localization, of which it is moreover
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
lying in the Universe in question; the “morphisms” from one object $X$ of `Cat` to another $Y$ are, by definition, the
**functors** from $X$ to $Y$.

<!-- original page 147 -->

If $\mathcal{C}$ is a category, we denote by $Ob(\mathcal{C})$ **the set of objects** of $\mathcal{C}$, and by
$Fl(\mathcal{C})$ **the set of arrows** of $\mathcal{C}$, or morphisms of $\mathcal{C}$. We shall therefore write $X \in
Ob(\mathcal{C})$, avoiding the common abuse of notation $X \in \mathcal{C}$. If $\mathcal{C}$ and $\mathcal{C}'$ are two
categories, a **functor** from $\mathcal{C}$ to $\mathcal{C}'$ will always mean what is commonly called a **covariant**
functor from $\mathcal{C}$ to $\mathcal{C}'$. Its data include both the target category and the source category,
$\mathcal{C}$ and $\mathcal{C}'$. The functors from $\mathcal{C}$ to $\mathcal{C}'$ form a set, denoted
$\operatorname{Hom}(\mathcal{C},\mathcal{C}')$, which is the set of objects of a category denoted `Hom̲(𝒞,𝒞′)`. By
definition, a **contravariant functor** from $\mathcal{C}$ to $\mathcal{C}'$ is a functor from the **opposite category**
$\mathcal{C}^{\circ}$ of $\mathcal{C}$ to $\mathcal{C}'$.

We shall admit the notions of **projective limit** and **inductive limit** of a functor $F: \mathcal{I} \to
\mathcal{C}$, and in particular the most common special cases of these notions: cartesian products and fiber products,
the dual notions of direct sums and amalgamated sums, and the usual formal properties of these operations.

For example, in the category `Cat` introduced above, projective limits, relative to categories $\mathcal{I}$ lying in
the chosen Universe, exist. The set of objects, respectively the set of arrows, of the projective-limit category
$\mathcal{C}$ of the $\mathcal{C}_{i}$ is obtained by taking the projective limit of the sets of objects, respectively
the sets of arrows, of the categories $\mathcal{C}_{i}$. The best-known case is that of the product of a family of
categories. We shall constantly use, in what follows, the fiber product of two categories over a third.

For everything concerning categories and functors, pending the book in preparation already mentioned, see [VI.1], which
is necessarily quite incomplete, even as concerns the generalities sketched in the present number.

Let us take this occasion to spell out the notion of equivalence of categories, which is not presented satisfactorily in
[VI.1]. A functor $F: \mathcal{C} \to \mathcal{C}'$ is said to be **faithful**, respectively **fully faithful**, if for
every pair of objects $S$, $T$ of $\mathcal{C}$, the map $u \mapsto F(u)$ from $\operatorname{Hom}(S,T)$ to
$\operatorname{Hom}(F(S),F(T))$ is injective, respectively bijective. One says that $F$ is an **equivalence** of
categories if

<!-- original page 148 -->

$F$ is fully faithful and, moreover, every object $S'$ of $\mathcal{C}'$ is isomorphic to an object of the form $F(S)$.
One shows that this is the same as saying that there exists a functor $G$ from $\mathcal{C}'$ to $\mathcal{C}$
**quasi-inverse** to $F$, i.e. such that `GF` is isomorphic to $id_{\mathcal{C}}$ and `FG` is isomorphic to
$id_{\mathcal{C}}'$.

When this is so, giving a functor $G: \mathcal{C}' \to \mathcal{C}$ and an isomorphism $\phi: FG \to id_{\mathcal{C}}'$
is equivalent to giving, for every $S' \in Ob(\mathcal{C}')$, a pair $(S,u)$ formed by an object $S$ of $\mathcal{C}$
and an isomorphism $u: F(S) \to S'$, namely $(G(S'), \phi(S'))$. With this notation, there exists a unique functor
$\mathcal{C}' \to \mathcal{C}$ having the given map $S' \mapsto G(S')$ as its object map, and such that the map $S'
\mapsto \phi(S')$ is a homomorphism of functors $FG \to id_{\mathcal{C}}'$.

Finally, if $G$ is a functor quasi-inverse to $F$, and if one chooses isomorphisms $\phi: FG \simeq id_{\mathcal{C}}'$
and $\psi: GF \simeq id_{\mathcal{C}}$, then the two compatibility conditions on $\phi$ and $\psi$ stated in [VI.1,
I.1.2] are in fact equivalent to one another; and for every chosen isomorphism $\phi$, there exists a unique isomorphism
$\psi$ such that those conditions are satisfied.

## 2. Categories over Another Category

<!-- label: VI.2 -->

Let $\mathcal{E}$ be a category in the chosen Universe. It is therefore an object of `Cat`, and one may consider the
category $Cat_{/}\mathcal{E}$ of “objects of `Cat` over $\mathcal{E}$”. An object of this category is therefore a
functor

$$ p: \mathcal{F} \to \mathcal{E}. $$

One also says that the category $\mathcal{F}$, endowed with such a functor, is a **category over** $\mathcal{E}$, or an
**$\mathcal{E}$-category**. Thus an **$\mathcal{E}$-functor** from a category $\mathcal{F}$ over $\mathcal{E}$ to a
category $\mathcal{G}$ over $\mathcal{E}$ will mean a functor

$$ f: \mathcal{F} \to \mathcal{G} $$

such that

```text
qf = p,
```

where $p$ and $q$ are the projection functors for $\mathcal{F}$ and $\mathcal{G}$ respectively. The set of
$\mathcal{E}$-functors $f$ from $\mathcal{F}$ to $\mathcal{G}$ is therefore in bijective correspondence with the set of
arrows with source $\mathcal{F}$ and target $\mathcal{G}$ in $Cat_{/}\mathcal{E}$,

<!-- original page 149 -->

without this being an identity, since the data of an $f$ as above does not determine $\mathcal{F}$ and $\mathcal{G}$ as
categories over $\mathcal{E}$. Of course, as in any other category $\mathcal{C}_{/}S$, we shall routinely make the abuse
of language that identifies $\mathcal{E}$-functors, in the sense just explained, with arrows in a category
$Cat_{/}\mathcal{E}$.

We shall denote by

$$ \operatorname{Hom}_{\mathcal{E}}(\mathcal{F},\mathcal{G}) $$

the set of $\mathcal{E}$-functors from $\mathcal{F}$ to $\mathcal{G}$. Of course, a composite of $\mathcal{E}$-functors
is an $\mathcal{E}$-functor, the composition in question corresponding by definition to the composition of arrows in
$Cat_{/}\mathcal{E}$.

Now consider two $\mathcal{E}$-functors

$$ f,g: \mathcal{F} \to \mathcal{G} $$

and a homomorphism of functors

$$ u: f \to g. $$

One says that $u$ is an **$\mathcal{E}$-homomorphism**, or a “**homomorphism of $\mathcal{E}$-functors**”, if for every
$\xi \in Ob(\mathcal{F})$, one has

$$ q(u(\xi)) = id_{p(\xi)}. $$

In words: putting $S = p(\xi) = qf(\xi) = qg(\xi) \in Ob(\mathcal{E})$, the morphism

$$ u(\xi): f(\xi) \to g(\xi) $$

in $\mathcal{G}$ is an $id_{S}$-morphism. In general, for every morphism $\alpha: T \to S$ in $\mathcal{E}$ and every
category $\mathcal{G}$ over $\mathcal{E}$, a morphism $v$ in $\mathcal{G}$ is called an **$\alpha$-morphism** if $q(v) =
\alpha$, where $q$ denotes the projection functor $\mathcal{G} \to \mathcal{E}$. If one has a third
$\mathcal{E}$-functor $h: \mathcal{F} \to \mathcal{G}$ and an $\mathcal{E}$-homomorphism $v: g \to h$, then `vu` is
again an $\mathcal{E}$-homomorphism.

<!-- original page 150 -->

Thus **the $\mathcal{E}$-functors from $\mathcal{F}$ to $\mathcal{G}$, and the $\mathcal{E}$-homomorphisms between them,
form a subcategory of the category `Hom̲(ℱ,𝒢)` of all functors from $\mathcal{F}$ to $\mathcal{G}$; it will be called the
category of $\mathcal{E}$-functors from $\mathcal{F}$ to $\mathcal{G}$ and denoted**

```text
Hom̲_{ℰ/-}(ℱ,𝒢).
```

It is also the kernel subcategory of the pair of functors

```text
R,S: Hom̲(ℱ,𝒢) ⇉ Hom̲(ℱ,ℰ),
```

where $R$ is the constant functor defined by the object $p$ of `Hom̲(ℱ,ℰ)`, and $S$ is the functor $f \mapsto q \circ f$
defined by $q: \mathcal{G} \to \mathcal{E}$.

To finish these generalities, it remains to define the natural pairings between the categories `Hom̲_{ℰ/-}(ℱ,𝒢)` by
composition of $\mathcal{E}$-functors. In other words, one wants to define a “composition functor”

```text
(i)  Hom̲_{ℰ/-}(ℱ,𝒢) × Hom̲_{ℰ/-}(𝒢,ℋ) → Hom̲_{ℰ/-}(ℱ,ℋ)
```

when $\mathcal{F}$, $\mathcal{G}$, $\mathcal{H}$ are three categories over $\mathcal{E}$, in such a way that this
functor induces, on objects, the composition map $(f,g) \mapsto gf$ for $\mathcal{E}$-functors $f: \mathcal{F} \to
\mathcal{G}$ and $g: \mathcal{G} \to \mathcal{H}$. For this, recall that one defines a canonical functor

```text
(ii) Hom̲(ℱ,𝒢) × Hom̲(𝒢,ℋ) → Hom̲(ℱ,ℋ),
```

which on objects is just the composition map $(f,g) \mapsto gf$ of functors, and which transforms an arrow $(u,v)$,
where

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

It is well known that one indeed obtains in this way a homomorphism from `gf` to $g'f'$, and that, for variable $f$, $g$
and $u$, $v$, one obtains the functor (ii); that is, one has

```text
(I)   id_g ∗ id_f = id_{gf},
```

and

```text
(II)  (v′ ∗ u′) ∘ (v ∗ u) = (v′ ∘ v) ∗ (u′ ∘ u).
```

Recall also that one has an associativity formula for the canonical pairings (ii), expressed on the one hand by the
associativity $(hg)f = h(gf)$ of the composition of functors, and on the other hand by the formula

```text
(III) (w ∗ v) ∗ u = w ∗ (v ∗ u)
```

for the composition products of homomorphisms of functors, where $u: f \to f'$ and $v: g \to g'$ are as above, and where
one supposes given in addition a homomorphism $w: h \to h'$ of functors $h,h': \mathcal{H} \to \mathcal{K}$.

I now say that **when $\mathcal{F}$ and $\mathcal{G}$ are $\mathcal{E}$-categories, the canonical composition functor
(ii) induces a functor (i)**. Since we already know that the composite of two $\mathcal{E}$-functors is an
$\mathcal{E}$-functor, this amounts to saying that **when $u: f \to f'$ and $v: g \to g'$ are homomorphisms of
$\mathcal{E}$-functors, then $v \ast u: gf \to g'f'$ is also a homomorphism of $\mathcal{E}$-functors**. This follows
trivially from the definitions. Since the pairings (i) are induced by the pairings (ii), they satisfy the same
associativity property, also expressed in the formulas $(hg)f = h(gf)$ and $(w \ast v) \ast u = w \ast (v \ast u)$, for
$\mathcal{E}$-functors and $\mathcal{E}$-homomorphisms of $\mathcal{E}$-functors.

To complete the formulary (I), (II), (III), recall also the formulas

```text
(IV)  v ∗ id_ℱ = v    and    id_𝒢 ∗ u = u,
```

<!-- original page 152 -->

where, for simplicity, one writes $v \ast f$ or $u \ast g$ instead of $v \ast u$ when $u$, respectively $v$, is the
identity automorphism of $f$, respectively $g$.

It follows from the definition of the pairings (i) that **`Hom̲_{ℰ/-}(ℱ,𝒢)` is a functor in $\mathcal{F}$ and
$\mathcal{G}$, from the product category $Cat_{/}\mathcal{E}^{\circ} \times Cat_{/}\mathcal{E}$ to the category `Cat`**.
Indeed, if $g: \mathcal{G} \to \mathcal{G}_{1}$ is an $\mathcal{E}$-functor, i.e. an object of `Hom̲_{ℰ/-}(𝒢,𝒢₁)`, then
by taking $\mathcal{H} = \mathcal{G}_{1}$ in (i), there corresponds to it a functor

```text
g_*: Hom̲_{ℰ/-}(ℱ,𝒢) → Hom̲_{ℰ/-}(ℱ,𝒢₁).
```

One defines analogously, for an $\mathcal{E}$-functor $f: \mathcal{F}_{1} \to \mathcal{F}$, a functor

```text
f^*: Hom̲_{ℰ/-}(ℱ,𝒢) → Hom̲_{ℰ/-}(ℱ₁,𝒢).
```

For short, these functors are also denoted by the symbols $f \mapsto g \circ f$ and $g \mapsto g \circ f$ respectively;
these in fact denote only the corresponding maps on the sets of objects. It follows from the associativity property
indicated above that one does indeed obtain in this way, as announced, a functor `Cat_/ℰ° × Cat_/ℰ → Cat`.

## 3. Base Change in Categories over ℰ

<!-- label: VI.3 -->

Since projective limits exist in `Cat`, relative to categories $\mathcal{I}$ belonging to the Universe, the same is true
in $Cat_{/}\mathcal{E}$. In particular, cartesian products exist there; these are interpreted as fiber products in
`Cat`. In accordance with the general notation, if $\mathcal{F}$ and $\mathcal{G}$ are categories over $\mathcal{E}$, we
denote by

$$ \mathcal{F} \times_{\mathcal{E}} \mathcal{G} $$

their product in $Cat_{/}\mathcal{E}$, i.e. their fiber product over $\mathcal{E}$ in `Cat`, regarded as a category over
$\mathcal{E}$. Thus $\mathcal{F} \times_{\mathcal{E}} \mathcal{G}$ is endowed with two $\mathcal{E}$-functors $pr_{1}$
and $pr_{2}$, which define, for every category $\mathcal{H}$ over $\mathcal{E}$, a bijection

<!-- original page 153 -->

```text
Hom_ℰ(ℋ, ℱ ×_ℰ 𝒢) ≃ Hom_ℰ(ℋ,ℱ) × Hom_ℰ(ℋ,𝒢).
```

This bijection moreover comes from an isomorphism of categories

```text
Hom̲_{ℰ/-}(ℋ, ℱ ×_ℰ 𝒢) ≃ Hom̲_{ℰ/-}(ℋ,ℱ) × Hom̲_{ℰ/-}(ℋ,𝒢),
```

by taking the sets of objects of the two sides. The displayed functor is the one whose components are the functors $h
\mapsto pr_{1} \circ h$ and $h \mapsto pr_{2} \circ h$ from the first member to the two factors of the second. We leave
to the reader the verification that one indeed obtains an isomorphism in this way; the analogous fact is true more
generally whenever one has a projective limit of categories, and not only in the case of a fiber product.

Recall moreover, as was said in VI.1, that

```text
Ob(ℱ ×_ℰ 𝒢) = Ob(ℱ) ×_{Ob(ℰ)} Ob(𝒢),
Fl(ℱ ×_ℰ 𝒢) = Fl(ℱ) ×_{Fl(ℰ)} Fl(𝒢),
```

the composition of arrows being carried out componentwise.

In what follows, we consider a functor

$$ \lambda: \mathcal{E}' \to \mathcal{E}, $$

and, for every category $\mathcal{F}$ over $\mathcal{E}$, we regard $\mathcal{F} \times_{\mathcal{E}} \mathcal{E}'$ as a
category over $\mathcal{E}'$ by means of $pr_{2}$. In other words, we interpret the “fiber product” operation as an
operation of **“base change”**, the functor $\lambda: \mathcal{E}' \to \mathcal{E}$ being called the **“base-change
functor.”** In accordance with the well-known general facts, one obtains in this way a functor, called the **base-change
functor** for $\lambda$:

<!-- original page 154 -->

$$ \lambda*: Cat_{/}\mathcal{E} \to Cat_{/}\mathcal{E}'. $$

It is adjoint to the “restriction of the base” functor, which sends every category $\mathcal{F}'$ over $\mathcal{E}'$,
with projection functor $p'$, to $\mathcal{F}'$ regarded as a category over $\mathcal{E}$ by the functor $p = \lambda
p'$. As is well known for a base-change functor in a category, the base-change functor “commutes with projective
limits”, and in particular “transforms” fiber products over $\mathcal{E}$ into fiber products over $\mathcal{E}'$.

Let $\mathcal{F}$ and $\mathcal{G}$ be two categories over $\mathcal{E}$. We shall define a **canonical isomorphism**

```text
(i)  Hom̲_{ℰ′/-}(ℱ′,𝒢′) ≃ Hom̲_{ℰ/-}(ℱ ×_ℰ ℰ′,𝒢),
     where ℱ′ = ℱ ×_ℰ ℰ′ and 𝒢′ = 𝒢 ×_ℰ ℰ′.
```

For this, consider the functor

```text
pr₁: 𝒢′ = 𝒢 ×_ℰ ℰ′ → 𝒢,
```

and define (i) by

$$ F \mapsto pr_{1} \circ F, $$

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

to prove that if $F$, $G$ are $\mathcal{E}'$-functors $\mathcal{F}' \to \mathcal{G}'$, then **the map**

$$ u \mapsto pr_{1} \circ u $$

**induces a bijection**

```text
Hom_{ℰ′}(F,G) ≃ Hom_ℰ(pr₁ ∘ F, pr₁ ∘ G).
```

The verification of this fact is immediate and is left to the reader.

It follows from this isomorphism (i), and from the end of the preceding number, that

```text
Hom̲_{ℰ′/-}(ℱ ×_ℰ ℰ′, 𝒢 ×_ℰ ℰ′)
```

**may be regarded as a functor in $\mathcal{E}'$, $\mathcal{F}$, $\mathcal{G}$, from the category
`Cat_/ℰ° × Cat_/ℰ° × Cat_/ℰ` to the category `Cat`**, isomorphic to the functor defined by the expression

```text
Hom̲_{ℰ/-}(ℱ ×_ℰ ℰ′,𝒢).
```

In particular, for fixed $\mathcal{F}$ and $\mathcal{G}$, one obtains a functor in $\mathcal{E}'$. Thus the
$\mathcal{E}$-functor of projection $\lambda: \mathcal{E}' \to \mathcal{E}$ defines a morphism, i.e. a functor

```text
λ*_{ℱ,𝒢}: Hom̲_{ℰ/-}(ℱ,𝒢) → Hom̲_{ℰ′/-}(ℱ′,𝒢′),
```

which we now spell out. On the sets of objects of the two sides, it is the map

```text
f ↦ f′ = f ×_ℰ ℰ′,
```

expressing the functorial dependence of $\mathcal{F} \times_{\mathcal{E}} \mathcal{E}'$ on the object $\mathcal{F}$ over
$\mathcal{E}$. On the other hand, consider two $\mathcal{E}$-functors

$$ f,g: \mathcal{F} \to \mathcal{G} $$

and a homomorphism of $\mathcal{E}$-functors

$$ u: f \to g. $$

We shall spell out the corresponding homomorphism of $\mathcal{E}'$-functors

<!-- original page 156 -->

$$ u': f' \to g'. $$

For every

$$ \xi' = (\xi,S') \in Ob(\mathcal{F}') $$

with

```text
ξ ∈ Ob(ℱ),    S′ ∈ Ob(ℰ′),    p(ξ) = λ(S′) = S,
```

the morphism

```text
u′(ξ′): f′(ξ′) = (f(ξ),S′) → g′(ξ′) = (g(ξ),S′)    in 𝒢′
```

is defined by the formula

$$ u'(\xi') = (u(\xi), id_{S'}). $$

This is indeed an $S'$-morphism in $\mathcal{G}'$, since $q(u(\xi)) = \lambda(id_{S'}) = id_{S}$.

Now consider any $\mathcal{E}$-functor

$$ \lambda': \mathcal{E}'' \to \mathcal{E}' $$

and the corresponding functor

```text
Hom̲_{ℰ′/-}(ℱ ×_ℰ ℰ′, 𝒢 ×_ℰ ℰ′)
  → Hom̲_{ℰ″/-}(ℱ ×_ℰ ℰ″, 𝒢 ×_ℰ ℰ″).
```

I say that this functor is none other than the one obtained by the preceding process, starting from $\mathcal{F}'$ and
$\mathcal{G}'$ over $\mathcal{E}'$ and regarding $\mathcal{E}''$ as a category over $\mathcal{E}'$, taking into account
the isomorphisms of **“transitivity of base change”**

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

The functors just defined are compatible with the pairings defined in the preceding number. More precisely, if
$\mathcal{F}$, $\mathcal{G}$, $\mathcal{H}$ are categories over $\mathcal{E}$ and if one puts

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

$$ (gf)' = g'f' $$

for $f \in \operatorname{Hom}_{\mathcal{E}}(\mathcal{F},\mathcal{G})$, $g \in
\operatorname{Hom}_{\mathcal{E}}(\mathcal{G},\mathcal{H})$, a formula which simply expresses the functoriality of base
change, and

```text
(v ∗ u)′ = v′ ∗ u′
```

when $u: f \to f_{1}$ is an arrow of `Hom̲_{ℰ/-}(ℱ,𝒢)` and $v: g \to g_{1}$ is an arrow of `Hom̲_{ℰ/-}(𝒢,ℋ)`. The
verification of this formula follows easily from the definitions.

In what follows, we shall be chiefly interested in `Hom̲_ℰ(ℱ,𝒢)`, and certain remarkable subcategories of it, when
$\mathcal{F} = \mathcal{E}$. For this reason we introduce a special notation:

```text
Γ̲(𝒢/ℰ) = Hom̲_ℰ(ℰ,𝒢),
Γ(𝒢/ℰ) = Ob(Γ̲(𝒢/ℰ)) = Hom_ℰ(ℰ,𝒢).
```

**Remarks.** When $\mathcal{E}$ is a point category, i.e. $Ob(\mathcal{E})$ and $Fl(\mathcal{E})$ are reduced to a
single element, which also means that $\mathcal{E}$ is a final object of the category `Cat`, then the data of a category
over $\mathcal{E}$ is equivalent to the data of a category in the ordinary sense, since there will be a unique functor
from $\mathcal{F}$ to $\mathcal{E}$. More precisely, $Cat_{/}\mathcal{E}$ is then isomorphic to `Cat`. Moreover, the
categories `Hom̲_{ℰ/-}(ℱ,𝒢)` are then none other than the `Hom̲(ℱ,𝒢)`.

<!-- original page 158 -->

Recall then that the fundamental formula

```text
Hom(ℋ, Hom̲(ℱ,𝒢)) ≃ Hom(ℱ × ℋ, 𝒢),
```

functorial in the three arguments appearing in it, allows `Hom̲(ℱ,𝒢)` to be interpreted axiomatically, in terms internal
to the category `Cat`. Thus the familiar formulary for `Hom̲`-categories appears as a special case of a formulary valid
in categories such as `Cat`, where “`Hom̲`-objects”, defined by the preceding formula, exist. There is an analogous
interpretation of `Hom̲_{ℰ/-}(ℱ,𝒢)`, when $\mathcal{E}$ is again arbitrary, by the formula

```text
Hom(ℋ, Hom̲_{ℰ/-}(ℱ,𝒢)) ≃ Hom_ℰ(ℱ × ℋ, 𝒢),
```

functorial in the three arguments. In this way, the formal properties set out in VI.2 and VI.3 are special cases of more
general results, valid in categories where the objects `Hom̲_{ℰ/-}(ℱ,𝒢)`, for $\mathcal{F}$ and $\mathcal{G}$ two objects
of the category over a third object $\mathcal{E}$, exist.

## 4. Fiber Categories; Equivalence of ℰ-Categories

<!-- label: VI.4 -->

Let $\mathcal{F}$ be a category over $\mathcal{E}$, and let $S \in Ob(\mathcal{E})$. The **fiber category** of
$\mathcal{F}$ at $S$ is the subcategory $\mathcal{F}_{S}$ of $\mathcal{F}$ that is the inverse image of the point
subcategory of $\mathcal{E}$ defined by $S$.

<!-- original page 159 -->

Thus the objects of $\mathcal{F}_{S}$ are the objects $\xi$ of $\mathcal{F}$ such that $p(\xi) = S$, and its morphisms
are the morphisms $u$ of $\mathcal{F}$ such that $p(u) = id_{S}$, i.e. the $S$-morphisms in $\mathcal{F}$. Of course,
$\mathcal{F}_{S}$ is canonically isomorphic to the fiber product $\mathcal{F} \times_{\mathcal{E}} {S}$, where ${S}$
denotes the point subcategory of $\mathcal{E}$ defined by $S$, endowed with its inclusion functor into $\mathcal{E}$. It
follows, taking the transitivity of base change into account, that if one makes a base change $\lambda: \mathcal{E}' \to
\mathcal{E}$, then for every $S' \in Ob(\mathcal{E}')$, **the projection $pr_{1}: \mathcal{F}' = \mathcal{F}
\times_{\mathcal{E}} \mathcal{E}' \to \mathcal{F}$ induces an isomorphism**

```text
ℱ′_{S′} → ℱ_S,    where S = λ(S′).
```

**Proposition.**

<!-- label: VI.4.1 -->

Let $f: \mathcal{F} \to \mathcal{G}$ be an $\mathcal{E}$-functor. If $f$ is fully faithful, then for every base change
$\mathcal{E}' \to \mathcal{E}$, the corresponding functor

```text
f′: ℱ′ = ℱ ×_ℰ ℰ′ → 𝒢′ = 𝒢 ×_ℰ ℰ′
```

is fully faithful.

The verification is immediate. More generally, one can show that every projective limit of fully faithful functors, here
$f$ and the identity functors in $\mathcal{E}$ and $\mathcal{E}'$, is a fully faithful functor.

One should note that the assertion analogous to 4.1, with “fully faithful” replaced by “equivalence of categories”, is
false, already for $\mathcal{G} = \mathcal{E}$. However:

**Proposition.**

<!-- label: VI.4.2 -->

Let $f: \mathcal{F} \to \mathcal{G}$ be an $\mathcal{E}$-functor. The following conditions are equivalent:

1. There exists an $\mathcal{E}$-functor $g: \mathcal{G} \to \mathcal{F}$ and $\mathcal{E}$-isomorphisms

```text
gf ≃ id_ℱ,    fg ≃ id_𝒢.
```

1. For every category $\mathcal{E}'$ over $\mathcal{E}$, the functor

```text
f′ = f ×_ℰ ℰ′: ℱ′ = ℱ ×_ℰ ℰ′ → 𝒢′ = 𝒢 ×_ℰ ℰ′
```

is an equivalence of categories.

<!-- original page 160 -->

1. $f$ is an equivalence of categories, and for every $S \in Ob(\mathcal{E})$, the functor $f_{S}: \mathcal{F}_{S} \to
   \mathcal{G}_{S}$ induced by $f$ is an equivalence of categories.

1. $f$ is fully faithful, and for every $S \in Ob(\mathcal{E})$ and every $\eta \in Ob(\mathcal{G}_{S})$, there exist
   $\xi \in Ob(\mathcal{F}_{S})$ and an $S$-isomorphism $u: f(\xi) \to \eta$.

**Proof.** Evidently (1) implies that $f$ is an equivalence of categories, a notion defined by the same condition but
without requiring the isomorphisms of functors to be $\mathcal{E}$-morphisms. On the other hand, it follows from the
functorialities of the preceding number that condition (1) is preserved after base change $\mathcal{E}' \to
\mathcal{E}$. Hence (1) ⇒ (2). Evidently (2) ⇒ (3), since it is enough to take $\mathcal{E}' = \mathcal{E}$ and
$\mathcal{E}' = {S}$. It is still more trivial that (3) ⇒ (4). It remains to prove (4) ⇒ (1).

For this, choose for every $\eta \in Ob(\mathcal{G})$ an object $g(\eta) \in Ob(\mathcal{F})$ and an isomorphism
$u(\eta): f(g(\eta)) \to \eta$ such that $q(u(\eta)) = id_{S}$, where $S = q(\eta)$. This is possible by the second
condition in (4). As is known and immediate, the fact that $f$ is fully faithful implies that $g$ can be regarded in a
unique way as a functor from $\mathcal{G}$ to $\mathcal{F}$, so that the $u(\eta)$ define a functorial homomorphism,
hence isomorphism,

$$ u: fg \simeq id_{\mathcal{G}}. $$

Moreover, by construction, $g$ is an $\mathcal{E}$-functor and $u$ an $\mathcal{E}$-homomorphism. To the preceding data
there then corresponds a functorial isomorphism $v: gf \to id_{\mathcal{F}}$, defined by the condition $f \ast v = u
\ast f$, and one sees at once that it is also an $\mathcal{E}$-morphism. This proves the assertion.

**Definition.**

<!-- label: VI.4.3 -->

If the preceding conditions are satisfied, one says that $f$ is an **equivalence of categories over $\mathcal{E}$**, or
an **$\mathcal{E}$-equivalence**.

**Corollary.**

<!-- label: VI.4.4 -->

Suppose that the projection functor $p: \mathcal{F} \to \mathcal{E}$ is a transportable functor, i.e. that for every
isomorphism $\alpha: T \to S$ in $\mathcal{E}$ and every object $\xi$ in $\mathcal{F}_{T}$, there exists an isomorphism
$u$ in $\mathcal{F}$ with source $\xi$ such that $p(u) = \alpha$. Then every $\mathcal{E}$-functor $f: \mathcal{F} \to
\mathcal{G}$ that is an equivalence of categories is an $\mathcal{E}$-equivalence.

This follows

<!-- original page 161 -->

from criterion (4).

**Corollary.**

<!-- label: VI.4.5 -->

Let $f: \mathcal{F} \to \mathcal{G}$ be an $\mathcal{E}$-equivalence. Then for every category $\mathcal{H}$ over
$\mathcal{E}$, the corresponding functors

```text
Hom̲_{ℰ/-}(𝒢,ℋ) → Hom̲_{ℰ/-}(ℱ,ℋ),
Hom̲_{ℰ/-}(ℋ,ℱ) → Hom̲_{ℰ/-}(ℋ,𝒢)
```

are equivalences of categories.

This follows from criterion (1) by the usual argument.

## 5. Cartesian Morphisms, Inverse Images, Cartesian Functors

<!-- label: VI.5 -->

Let $\mathcal{F}$ be a category over $\mathcal{E}$, with projection functor $p$.

**Definition.**

<!-- label: VI.5.1 -->

Consider a morphism

$$ \alpha: \eta \to \xi $$

in $\mathcal{F}$, and let

```text
S = p(ξ),    T = p(η),    f = p(α).
```

One says that $\alpha$ is a **cartesian morphism** if, for every $\eta' \in Ob(\mathcal{F}_{T})$ and every $f$-morphism
$u: \eta' \to \xi$, there exists a unique $T$-morphism $\bar{u}: \eta' \to \eta$ such that $u = \alpha \circ \bar{u}$.

This therefore means that, for every $\eta' \in Ob(\mathcal{F}_{T})$, the map $v \mapsto \alpha \circ v$

$$ (i) \operatorname{Hom}_{T}(\eta',\eta) \to \operatorname{Hom}_{f}(\eta',\xi) $$

is bijective. It also means that the pair $(\eta,\alpha)$ **represents, as a functor in $\eta'$**, the functor
$\mathcal{F}^{\circ}_{T} \to Set$ given by the second member.

If, for a given morphism $f: T \to S$ in $\mathcal{E}$ and a given $\xi \in Ob(\mathcal{F}_{S})$, such a pair
$(\eta,\alpha)$ exists, i.e. a cartesian morphism $\alpha$ in $\mathcal{F}$ with target $\xi$ and with $p(\alpha) = f$,
then $\eta$ is determined in $\mathcal{F}_{T}$ up to unique isomorphism. One then says that **the inverse image of $\xi$
by $f$ exists**, and an object $\eta$ of $\mathcal{F}_{T}$ endowed with a cartesian $f$-morphism $\alpha: \eta \to \xi$
is called **an inverse image of $\xi$ by $f$**.

<!-- original page 162 -->

Often, once $\mathcal{F}$ is fixed, one assumes such an inverse image chosen whenever it exists. The inverse image will
then be denoted by symbols such as $f*_{\mathcal{F}}(\xi)$, or simply $f*(\xi)$, or $\xi \times_{S} T$ when these
notations cause no confusion. In what follows, the canonical morphism $\alpha: \eta \to \xi$ will then be denoted
$\alpha_{f}(\xi)$.

If for every $\xi \in Ob(\mathcal{F}_{S})$ the inverse image of $\xi$ by $f$ exists, one also says that **the
inverse-image functor by $f$ in $\mathcal{F}$ exists**, and $f*(\xi)$ then becomes a **covariant functor in $\xi$**,
from $\mathcal{F}_{S}$ to $\mathcal{F}_{T}$. This comes from the fact that the second member in (i) depends covariantly
on $\xi$, or more precisely denotes a functor from $\mathcal{F}^{\circ}_{T} \times \mathcal{F}_{S}$ to `Set`.

This functorial dependence of $f*(\xi)$ is made explicit as follows. Consider cartesian $f$-morphisms

```text
α: η → ξ,    α′: η′ → ξ′
```

and an $S$-morphism $\lambda: \xi \to \xi'$. Then there exists a unique $T$-morphism $\mu: \eta \to \eta'$ such that

```text
α′ μ = λ α,
```

as follows from the fact that $\alpha'$ is cartesian.

Also note the following immediate fact. Consider a commutative diagram in $\mathcal{F}$

```text
η  --α-->  ξ
|         |
μ         λ
↓         ↓
η′ --α′-> ξ′
```

<!-- original page 163 -->

where $\alpha$ and $\alpha'$ are $f$-morphisms, $\lambda$ is an $S$-isomorphism, and $\mu$ is a $T$-isomorphism. **Then
$\alpha$ is cartesian if and only if $\alpha'$ is cartesian**.

**Definition.**

<!-- label: VI.5.2 -->

An $\mathcal{E}$-functor $F: \mathcal{F} \to \mathcal{G}$ is called a **cartesian functor** if it transforms cartesian
morphisms into cartesian morphisms. We denote by `Hom̲_cart(ℱ,𝒢)` the full subcategory of `Hom̲_{ℰ/-}(ℱ,𝒢)` formed by the
cartesian functors.

For example, regarding $\mathcal{E}$ as a category over $\mathcal{E}$ by means of the identity functor, every morphism
of $\mathcal{E}$ is cartesian. Thus a cartesian functor from $\mathcal{E}$ to $\mathcal{F}$ is a section functor $F:
\mathcal{E} \to \mathcal{F}$ that transforms every morphism of $\mathcal{E}$ into a cartesian morphism. Such a functor
is called a **cartesian section** of $\mathcal{F}$ over $\mathcal{E}$.

**Proposition.**

<!-- label: VI.5.3 -->

1. A functor $F: \mathcal{F} \to \mathcal{G}$ that is an $\mathcal{E}$-equivalence is a cartesian functor.
1. Let $F$, $G$ be two **isomorphic** $\mathcal{E}$-functors $\mathcal{F} \to \mathcal{G}$. If one is cartesian, then so
   is the other.
1. The composite of two cartesian functors $\mathcal{F} \to \mathcal{G}$ and $\mathcal{G} \to \mathcal{H}$ is a
   cartesian functor.

Assertion (3) is trivial from the definition; (2) follows from the remark preceding VI.5.2; (1) follows easily from the
definition and criterion VI.4.2 (3). More precisely, a morphism $\alpha$ in $\mathcal{F}$ is cartesian if and only if
$F(\alpha)$ is cartesian.

**Corollary.**

<!-- label: VI.5.4 -->

Let $F: \mathcal{F} \to \mathcal{G}$ be an $\mathcal{E}$-equivalence. Then for every category $\mathcal{H}$ over
$\mathcal{E}$, the corresponding functors $G \mapsto G \circ F$ and $G \mapsto F \circ G$ induce equivalences of
categories:

```text
Hom̲_cart(𝒢,ℋ) ≃ Hom̲_cart(ℱ,ℋ),
Hom̲_cart(ℋ,ℱ) ≃ Hom̲_cart(ℋ,𝒢).
```

This follows in the usual way from criterion VI.4.2 (1) and from VI.5.3 (1), (2), (3).

<!-- original page 164 -->

One can specify that **the $\mathcal{E}$-functor $G: \mathcal{G} \to \mathcal{H}$ is cartesian if and only if $G \circ
F$ is cartesian**, and likewise **an $\mathcal{E}$-functor $G: \mathcal{H} \to \mathcal{F}$ is cartesian if and only if
$F \circ G$ is cartesian**.

It follows from VI.5.4 (3) that, if one considers the subcategory $Cat^{cart}_{/}\mathcal{E}$ of $Cat_{/}\mathcal{E}$
whose objects are the same as those of $Cat_{/}\mathcal{E}$ and whose morphisms are the **cartesian** functors, then, as
in VI.2, one has pairings

```text
Hom̲_cart(ℱ,𝒢) × Hom̲_cart(𝒢,ℋ) → Hom̲_cart(ℱ,ℋ)
```

induced by those of VI.2. These pairings allow one to regard `Hom̲_cart(ℱ,𝒢)` as a functor in $\mathcal{F}$ and
$\mathcal{G}$, from the category `(Cat^cart_/ℰ)° × Cat^cart_/ℰ` to `Cat`. We shall need this remark chiefly in the case
$\mathcal{F} = \mathcal{G}$.

**Definition.**

<!-- label: VI.5.5 -->

Let $\mathcal{F}$ be a category over $\mathcal{E}$. We denote by

$$ Lim\leftarrow(\mathcal{F}/\mathcal{E}) $$

the category of cartesian $\mathcal{E}$-functors $\mathcal{E} \to \mathcal{F}$, i.e. the cartesian sections of
$\mathcal{F}$ over $\mathcal{E}$.

By what has just been said, $Lim\leftarrow(\mathcal{F}/\mathcal{E})$ is a functor in $\mathcal{F}$, from the category
$Cat^{cart}_{/}\mathcal{E}$ to the category `Cat`.

We shall see below the relations between this operation $Lim\leftarrow$ and the notion of projective limit of
categories, as well as numerous examples.

## 6. Fibered Categories and Prefibered Categories. Products and Base Change in Them

<!-- label: VI.6 -->

**Definition.**

<!-- label: VI.6.1 -->

A category $\mathcal{F}$ over $\mathcal{E}$ is called a **fibered category**, and the functor $\mathcal{F} \to
\mathcal{E}$ is then said to be **fibrant**, if it satisfies the two following axioms:

**Fib I.** For every morphism $f: T \to S$ in $\mathcal{E}$, the inverse-image functor by $f$ in $\mathcal{F}$ exists.

**Fib II.** The composite of two cartesian morphisms is cartesian.

A category $\mathcal{F}$ over $\mathcal{E}$ satisfying condition **Fib I** is called a **prefibered category over
$\mathcal{E}$**.

If $\mathcal{F}$ is a fibered, respectively prefibered, category over $\mathcal{E}$, a subcategory $\mathcal{G}$ of
$\mathcal{F}$ is called a **fibered subcategory**, respectively a **prefibered subcategory**, if it is a fibered,
respectively prefibered, category over $\mathcal{E}$ and, moreover, the inclusion functor is cartesian. If, for example,
$\mathcal{G}$ is a **full** subcategory of $\mathcal{F}$, one sees that this means that, for every morphism $f: T \to S$
in $\mathcal{E}$ and every $\xi \in Ob(\mathcal{G}_{S})$, $f*_{\mathcal{F}}(\xi)$ is $T$-isomorphic to an object of
$\mathcal{G}_{T}$.

Another interesting case is the following. Let $\mathcal{F}$ be a fibered category over $\mathcal{E}$, and consider the
subcategory $\mathcal{G}$ of $\mathcal{F}$ with the same objects and whose morphisms are the **cartesian** morphisms of
$\mathcal{F}$; in particular the morphisms of $\mathcal{G}_{S}$ are the isomorphisms of $\mathcal{F}_{S}$. One sees at
once that this is indeed a fibered subcategory of $\mathcal{F}$, because in the bijection

<!-- original page 165 -->

$$ \operatorname{Hom}_{T}(\eta',\eta) \simeq \operatorname{Hom}_{f}(\eta',\xi) $$

relative to a cartesian $f$-morphism $\alpha$ in $\mathcal{F}$, the $T$-isomorphisms of the first member correspond to
the cartesian morphisms of the second. By definition, the cartesian sections $\mathcal{E} \to \mathcal{F}$ then
correspond bijectively to arbitrary $\mathcal{E}$-functors $\mathcal{E} \to \mathcal{G}$. However, note that the natural
functor

```text
Hom̲_{ℰ/-}(ℰ,𝒢) → Hom̲_cart(ℰ,ℱ) = Lim←(ℱ/ℰ)
```

is faithful, but in general is not fully faithful, i.e. is not an isomorphism.

**Remarks.** Let $\mathcal{F}$ be a category over $\mathcal{E}$. The following conditions are equivalent:

1. All morphisms of $\mathcal{F}$ are cartesian.
1. $\mathcal{F}$ is a fibered category over $\mathcal{E}$, and the $\mathcal{F}_{S}$ are groupoids, i.e. every morphism
   in $\mathcal{F}_{S}$ is an isomorphism.

One then says that $\mathcal{F}$ is a category **fibered in groupoids** over $\mathcal{E}$.

<!-- original page 166 -->

These are the ones encountered especially in “theory of moduli”. If $\mathcal{E}$ is a groupoid, one shows that
conditions (1) and (2) are also equivalent to the following:

1. $\mathcal{F}$ is a groupoid, and the projection functor $p: \mathcal{F} \to \mathcal{E}$ is transportable; cf.
   VI.4.4.

For example, if $\mathcal{E}$ and $\mathcal{F}$ are groupoids such that $Ob(\mathcal{E})$ and $Ob(\mathcal{F})$ are
reduced to a point, so that $\mathcal{E}$ and $\mathcal{F}$ are defined, up to isomorphism, by groups $E$ and $F$, and
the functor $p: \mathcal{F} \to \mathcal{E}$ is defined by a group homomorphism $p: F \to E$, then $\mathcal{F}$ is
fibered over $\mathcal{E}$ if and only if $p$ is surjective, i.e. if $p$ defines an **extension** of the group $E$ by
the group $G = Ker p$.

**Proposition.**

<!-- label: VI.6.2 -->

Let $F: \mathcal{F} \to \mathcal{G}$ be an $\mathcal{E}$-equivalence. In order that $\mathcal{F}$ be a fibered,
respectively prefibered, category over $\mathcal{E}$, it is necessary and sufficient that $\mathcal{G}$ be so.

This follows easily from the definitions and from the remark made above that a morphism $\alpha$ in $\mathcal{F}$ is
cartesian if and only if $F(\alpha)$ is.

**Proposition.**

<!-- label: VI.6.3 -->

Let $\mathcal{F}_{1}$, $\mathcal{F}_{2}$ be two categories over $\mathcal{E}$, and let $\alpha =
(\alpha_{1},\alpha_{2})$ be a morphism in $\mathcal{F} = \mathcal{F}_{1} \times_{\mathcal{E}} \mathcal{F}_{2}$. Then
$\alpha$ is cartesian if and only if its components are cartesian.

Indeed, let $\xi_{i}$ be the target and $\eta_{i}$ the source of $\alpha_{i}$, and let $f: T \to S$ be the morphism of
$\mathcal{E}$ such that $\alpha_{1}$ and $\alpha_{2}$ are $f$-morphisms. For every $\eta' = (\eta'_{1},\eta'_{2})$ in
$\mathcal{F}_{T}$, one has a commutative diagram

$$ \operatorname{Hom}_{T}(\eta',\eta) \to \operatorname{Hom}_{f}(\eta',\xi) \downarrow \downarrow
\operatorname{Hom}_{T}(\eta'_{1},\eta_{1}) \times \operatorname{Hom}_{T}(\eta'_{2},\eta_{2}) \to
\operatorname{Hom}_{f}(\eta'_{1},\xi_{1}) \times \operatorname{Hom}_{f}(\eta'_{2},\xi_{2}), $$

where the vertical arrows are bijections. Thus if one of the horizontal arrows is a bijection, the same is true of the
other. This already shows that if $\alpha_{1}$ and $\alpha_{2}$ are cartesian, hence the second horizontal arrow is
bijective, then $\alpha$ is cartesian. The converse is seen by taking, in the diagram above, $\eta'_{i} = \eta_{i}$,
whence $\operatorname{Hom}_{T}(\eta'_{i},\eta_{i}) \neq \emptyset$: first for $i = 2$, which proves that $\alpha_{1}$ is
cartesian, then for $i = 1$, which proves that $\alpha_{2}$ is cartesian.

**Corollary.**

<!-- label: VI.6.4 -->

<!-- original page 167 -->

Let $\mathcal{F} = \mathcal{F}_{1} \times_{\mathcal{E}} \mathcal{F}_{2}$, and let $F = (F_{1},F_{2})$ be an
$\mathcal{E}$-functor $\mathcal{G} \to \mathcal{F}$. Then $F$ is cartesian if and only if $F_{1}$ and $F_{2}$ are
cartesian. One obtains in this way an isomorphism of categories

```text
Hom̲_cart(𝒢, ℱ₁ ×_ℰ ℱ₂) ≃ Hom̲_cart(𝒢,ℱ₁) × Hom̲_cart(𝒢,ℱ₂),
```

and in particular, taking $\mathcal{G} = \mathcal{E}$, an isomorphism of categories

```text
Lim←((ℱ₁ ×_ℰ ℱ₂)/ℰ) ≃ Lim←(ℱ₁/ℰ) × Lim←(ℱ₂/ℰ).
```

**Corollary.**

<!-- label: VI.6.5 -->

Let $\mathcal{F}_{1}$ and $\mathcal{F}_{2}$ be two fibered, respectively prefibered, categories over $\mathcal{E}$. Then
their fiber product $\mathcal{F} = \mathcal{F}_{1} \times_{\mathcal{E}} \mathcal{F}_{2}$ is a fibered, respectively
prefibered, category over $\mathcal{E}$.

These results moreover extend to the case of the fiber product of an arbitrary family of categories over $\mathcal{E}$.

**Proposition.**

<!-- label: VI.6.6 -->

Let $\mathcal{F}$ be a category over $\mathcal{E}$, with projection functor $p$, and let $\lambda: \mathcal{E}' \to
\mathcal{E}$ be a functor. Regard $\mathcal{F}' = \mathcal{F} \times_{\mathcal{E}} \mathcal{E}'$ as a category over
$\mathcal{E}'$ by the projection functor $p' = p \times_{\mathcal{E}} id_{\mathcal{E}}'$. Let $\alpha'$ be a morphism of
$\mathcal{F}'$. Then $\alpha'$ is a cartesian morphism if and only if its image $\alpha$ in $\mathcal{F}$ is cartesian.

The proof is immediate and is left to the reader.

**Corollary.**

<!-- label: VI.6.7 -->

For every cartesian functor $F: \mathcal{F} \to \mathcal{G}$ of categories over $\mathcal{E}$, the functor

```text
F′ = F ×_ℰ ℰ′
```

from $\mathcal{F}' = \mathcal{F} \times_{\mathcal{E}} \mathcal{E}'$ to $\mathcal{G}' = \mathcal{G} \times_{\mathcal{E}}
\mathcal{E}'$ is cartesian.

Consequently, the functor `Hom̲_ℰ(ℱ,𝒢) → Hom̲_ℰ′(ℱ′,𝒢′)` considered in VI.3 induces a functor

```text
Hom̲_cart(ℱ,𝒢) → Hom̲_cart(ℱ′,𝒢′).
```

In other words, for fixed $\mathcal{F}$ and $\mathcal{G}$, **one may regard**

```text
Hom̲_cart(ℱ ×_ℰ ℰ′, 𝒢 ×_ℰ ℰ′)
```

<!-- original page 168 -->

**as a functor in $\mathcal{E}'$, from the category $Cat_{/}\mathcal{E}^{\circ}$ to `Cat`**. If $\mathcal{F}$ and
$\mathcal{G}$ are also allowed to vary, one finds a functor from the category

```text
Cat_/ℰ° × (Cat^cart_/ℰ)° × Cat^cart_/ℰ
```

to `Cat`.

When one takes into account the isomorphism

```text
Hom_ℰ′(ℱ′,𝒢′) ≃ Hom_ℰ(ℱ ×_ℰ ℰ′,𝒢)
```

considered in VI.3, the cartesian $\mathcal{E}'$-functors from $\mathcal{F}'$ to $\mathcal{G}'$ correspond to the
$\mathcal{E}$-functors $\mathcal{F} \times_{\mathcal{E}} \mathcal{E}' \to \mathcal{G}$ that transform every morphism
whose first projection is a cartesian morphism of $\mathcal{F}$ into a cartesian morphism of $\mathcal{G}$. Taking
$\mathcal{F} = \mathcal{E}$, one finds, after a change of notation:

**Corollary.**

<!-- label: VI.6.8 -->

$Lim\leftarrow(\mathcal{F}'/\mathcal{E}')$ is isomorphic to the full subcategory of `Hom̲_{ℰ/-}(ℰ′,ℱ)` formed by the
$\mathcal{E}$-functors $\mathcal{E}' \to \mathcal{F}$ that transform arbitrary morphisms into cartesian morphisms. In
particular, if $\mathcal{F}$ is a fibered category and if $\tilde{\mathcal{F}}$ is the subcategory of $\mathcal{F}$
whose morphisms are the cartesian morphisms of $\mathcal{F}$, then one has a bijection

$$ Ob Lim\leftarrow(\mathcal{F}'/\mathcal{E}') \simeq
\operatorname{Hom}_{\mathcal{E}/-}(\mathcal{E}',\tilde{\mathcal{F}}). $$

This makes precise the way in which the expression

$$ Lim\leftarrow((\mathcal{F} \times_{\mathcal{E}} \mathcal{E}')/\mathcal{E}') $$

must be regarded as a functor in $\mathcal{E}'$ and $\mathcal{F}$, from the category `Cat_/ℰ° × Cat^cart_/ℰ` to the
category `Cat`. Later we shall see a more complete functorial dependence with respect to $\mathcal{E}'$ when
$\mathcal{F}$ is required to be a fibered category.

**Corollary.**

<!-- label: VI.6.9 -->

If $\mathcal{F}$ is a fibered, respectively prefibered, category over $\mathcal{E}$, then $\mathcal{F}' = \mathcal{F}
\times_{\mathcal{E}} \mathcal{E}'$ is a fibered, respectively prefibered, category over $\mathcal{E}'$.

**Proposition.**

<!-- label: VI.6.10 -->

Let $\mathcal{F}$ and $\mathcal{G}$ be prefibered categories over $\mathcal{E}$, and let $F$ be a cartesian
$\mathcal{E}$-functor from $\mathcal{F}$ to $\mathcal{G}$. In order that $F$ be faithful, respectively fully faithful,
respectively an $\mathcal{E}$-equivalence, it is necessary and sufficient that for every $S \in Ob(\mathcal{E})$, the
induced functor

<!-- original page 169 -->

$$ F_{S}: \mathcal{F}_{S} \to \mathcal{G}_{S} $$

be faithful, respectively fully faithful, respectively an equivalence.

The proof is immediate from the definitions.

To finish this number, we give a few properties of fibered categories using axiom **Fib II**.

**Proposition.**

<!-- label: VI.6.11 -->

Let $\mathcal{F}$ be a prefibered category over $\mathcal{E}$. In order that $\mathcal{F}$ be fibered, it is necessary
and sufficient that it satisfy the following condition:

**Fib II′.** Let $\alpha: \eta \to \xi$ be a cartesian morphism in $\mathcal{F}$ over the morphism $f: T \to S$ of
$\mathcal{E}$. For every morphism $g: U \to T$ in $\mathcal{E}$, and every $\zeta \in Ob(\mathcal{F}_{U})$, the map $u
\mapsto \alpha \circ u$

$$ \operatorname{Hom}_{g}(\zeta,\eta) \to \operatorname{Hom}_{fg}(\zeta,\xi) $$

is bijective.

In other words, in a category **fibered** over $\mathcal{E}$, cartesian diagrams are characterized by a property a
priori stronger than the one in the definition, which is recovered by taking $g = id_{T}$ in the preceding statement.

**Corollary.**

<!-- label: VI.6.12 -->

Let $\mathcal{F}$ be a category over $\mathcal{E}$ and let $\alpha$ be a morphism in $\mathcal{F}$. In order that
$\alpha$ be an isomorphism, it is necessary that $p(\alpha) = f$ be an isomorphism and that $\alpha$ be cartesian. The
converse is true if $\mathcal{F}$ is fibered over $\mathcal{E}$.

Indeed, if $\alpha$ is an isomorphism then evidently so is $f = p(\alpha)$. For every $\eta' \in Ob(\mathcal{F}_{T})$,
the map $u \mapsto \alpha \circ u$

$$ \operatorname{Hom}(\eta',\eta) \to \operatorname{Hom}(\eta',\xi) $$

is bijective. Since $f$ is an isomorphism, one sees at once that an element of the first member is a $T$-morphism if and
only if its image in the second is an $f$-morphism. Thus one obtains a bijection

$$ \operatorname{Hom}_{T}(\eta',\eta) \to \operatorname{Hom}_{f}(\eta',\xi), $$

<!-- original page 170 -->

which proves the first assertion. Conversely, suppose that $f$ is an isomorphism and that $\alpha$ satisfies the
condition stated in **Fib II′**, which means, when $\mathcal{F}$ is fibered over $\mathcal{E}$, that $\alpha$ is
cartesian. Then one sees at once that for every $\zeta \in Ob(\mathcal{F})$, the map $u \mapsto \alpha \circ u$ from
$\operatorname{Hom}(\zeta,\eta)$ to $\operatorname{Hom}(\zeta,\xi)$ is bijective, and hence $\alpha$ is an isomorphism.

**Corollary.**

<!-- label: VI.6.13 -->

Let $\alpha: \eta \to \xi$ and $\beta: \zeta \to \eta$ be two composable morphisms in the category $\mathcal{F}$ fibered
over $\mathcal{E}$. If $\alpha$ is cartesian, then $\beta$ is cartesian if and only if $\alpha \beta$ is cartesian.

One uses the definition of cartesian morphisms in the strengthened form VI.6.11.

## 7. Categories Cloven over ℰ

<!-- label: VI.7 -->

**Definition.**

<!-- label: VI.7.1 -->

Let $\mathcal{F}$ be a category over $\mathcal{E}$. A **cleavage** of $\mathcal{F}$ over $\mathcal{E}$ means a function
that attaches to every $f \in Fl(\mathcal{E})$ an inverse-image functor for $f$ in $\mathcal{F}$, denoted $f*$. The
cleavage is said to be **normalized** if $f = id_{S}$ implies $f* = id_{\mathcal{F}_{S}}$. A **cloven category**,
respectively a **normalized cloven category**, means a category $\mathcal{F}$ over $\mathcal{E}$ endowed with a
cleavage, respectively with a normalized cleavage.

It is evident that $\mathcal{F}$ admits a cleavage if and only if $\mathcal{F}$ is prefibered over $\mathcal{E}$, and
then $\mathcal{F}$ admits a normalized cleavage. The set of cleavages on $\mathcal{F}$ is in bijective correspondence
with the set of subsets $K$ of $Fl(\mathcal{F})$ satisfying the following conditions:

1. The $\alpha \in K$ are cartesian morphisms.
1. For every morphism $f: T \to S$ in $\mathcal{E}$ and every $\xi \in Ob(\mathcal{F}_{S})$, there exists a unique
   $f$-morphism in $K$ with target $\xi$.

For the cleavage defined by $K$ to be normalized, it is necessary and sufficient that $K$ also satisfy the condition:

1. The identity morphisms in $\mathcal{F}$ belong to $K$.

<!-- original page 171 -->

The morphisms that are elements of $K$ may be called the **“transport morphisms”** for the cleavage in question.

The notion of isomorphism of cloven categories over $\mathcal{E}$ is clear. More generally, one can define morphisms of
cloven $\mathcal{E}$-categories as functors of $\mathcal{E}$-categories $\mathcal{F} \to \mathcal{G}$ that send
transport morphisms to transport morphisms. These are, in particular, cartesian functors. In this way the cloven
categories over $\mathcal{E}$ are the objects of a category, the **category of cloven categories over $\mathcal{E}$**.
The reader may spell out the existence of products, tied to the fact that if a category over $\mathcal{E}$ is the
product of categories $\mathcal{F}_{i}$ over $\mathcal{E}$, each endowed with a cleavage, then $\mathcal{F}$ is endowed
with the corresponding natural cleavage. We also leave to the reader the task of spelling out the notion of base change
in cloven categories.

We shall denote by $\alpha_{f}(\xi)$ the canonical morphism

$$ \alpha_{f}(\xi): f*(\xi) \to \xi. $$

As was said, it is functorial in $\xi$, i.e. one has a functorial homomorphism

```text
α_f: i_T f* → i_S,
```

where for every $S \in Ob(\mathcal{E})$, $i_{S}$ denotes the inclusion functor

$$ i_{S}: \mathcal{F}_{S} \to \mathcal{F}. $$

Now consider morphisms

```text
f: T → S    and    g: U → T
```

in $\mathcal{E}$, and let $\xi \in Ob(\mathcal{F}_{S})$. There then exists a unique $U$-morphism

$$ c_{f,g}(\xi): g*f*(\xi) \to (fg)*(\xi) $$

making commutative

<!-- original page 172 -->

the diagram

$$ g*f*(\xi) --\alpha_{g}(f*(\xi))--> f*(\xi) | c_{f,g}(\xi) | \alpha_{f}(\xi) \downarrow \downarrow (fg)*(\xi)
--\alpha_{fg}(\xi)--> \xi, $$

by the definition of $(fg)*(\xi)$. For variable $\xi$, this homomorphism is functorial; that is, one has a homomorphism

$$ c_{f,g}: g*f* \to (fg)* $$

of functors $\mathcal{F}_{S} \to \mathcal{F}_{U}$. Note at once:

**Proposition.**

<!-- label: VI.7.2 -->

In order that the cloven category $\mathcal{F}$ over $\mathcal{E}$ be fibered, it is necessary and sufficient that the
$c_{f,g}$ be isomorphisms.

It follows, taking $f$ to be an isomorphism and $g$ its inverse, and considering the isomorphisms $c_{f,g}$ and
$c_{g,f}$:

**Corollary.**

<!-- label: VI.7.3 -->

If $\mathcal{F}$ is a **fibered** cloven category over $\mathcal{E}$, then for every isomorphism $f: T \to S$ in
$\mathcal{E}$, $f*$ is an equivalence of categories $\mathcal{F}_{S} \to \mathcal{F}_{T}$.

**Proposition.**

<!-- label: VI.7.4 -->

Let $\mathcal{F}$ be a cloven category over $\mathcal{E}$. One has:

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

In these formulas, $f$, $g$, $h$ denote morphisms

```text
V → U → T → S
```

<!-- original page 173 -->

and $\xi$ is an object of $\mathcal{F}_{S}$.

In the case of a normalized cleavage, the first and second relations take the simpler form

```text
A′) c_{f,id_T} = id_{f*},    c_{id_S,f} = id_{f*}.
```

As for the third, it is visualized by the commutativity of the diagram

$$ h*g*f*(\xi) --c_{g,h}(f*(\xi))--> (gh)*f*(\xi) | h*(c_{f,g}(\xi)) | c_{f,gh}(\xi) \downarrow \downarrow h*(fg)*(\xi)
--c_{fg,h}(\xi)--> (fgh)*(\xi). $$

In the case of fibered categories, where the $c_{f,g}$ are isomorphisms, this commutativity may be expressed intuitively
by saying that **the successive use of isomorphisms of the form $c_{f,g}$ does not lead to “contradictory
identifications.”** One may also write this formula without the argument $\xi$, using the convolution product of
homomorphisms of functors:

```text
c_{fg,h} ∘ (h* ∗ c_{f,g}) = c_{f,gh} ∘ (c_{g,h} ∗ f*).
```

The proof of the first two formulas in VI.7.4 is trivial; let us sketch that of the third. For this, consider, in
addition to the square `(D)`, the square of homomorphisms

$$ g*f*(\xi) --\alpha_{g}(f*(\xi))--> f*(\xi) | c_{f,g}(\xi) | \alpha_{f}(\xi) \downarrow \downarrow (fg)*(\xi)
--\alpha_{fg}(\xi)--> \xi, $$

<!-- original page 174 -->

which is commutative by definition of $c_{f,g}(\xi)$. Consider the diagram obtained by joining the vertices of `(D)` to
the corresponding vertices of this square by homomorphisms of the form $\alpha$:

$$ \alpha_{h}(g*f*(\xi)), \alpha_{gh}(f*(\xi)), \alpha_{h}((fg)*(\xi)), \alpha_{fgh}(\xi). $$

The four lateral faces of the cube so obtained are also commutative. For the left face, this comes from the fact that
the left column of `(D)` is obtained from the left column of the preceding square by applying $h$, and that $\alpha_{h}$
is a functorial homomorphism. For the other three faces, this is nothing other than the definition of the operations $c$
on the remaining three sides of `(D)`. Thus the five faces of the cube other than the upper face are commutative. It
follows that the two `(fgh)`-morphisms $h*g*f*(\xi) \to (fgh)*(\xi)$ defined by `(D)` have the same composite with
$\alpha_{fgh}(\xi): (fgh)*(\xi) \to \xi$. Hence they are equal by the definition of $(fgh)*$.

Let us confine ourselves, in what follows, to **normalized** cloven categories. Such a category gives rise to the
following objects:

1. A map $S \mapsto \mathcal{F}_{S}$ from $Ob(\mathcal{E})$ to `Cat`.
1. A map $f \mapsto f*$, associating to every $f \in Fl(\mathcal{E})$, with source $T$ and target $S$, a functor $f*:
   \mathcal{F}_{S} \to \mathcal{F}_{T}$.
1. A map $(f,g) \mapsto c_{f,g}$, associating to every pair of arrows $(f,g)$ of $\mathcal{E}$ a functorial homomorphism
   $c_{f,g}: g*f* \to (fg)*$.

Moreover, these data satisfy the conditions expressed in formulas A′) and B) above. N.B. If one had not confined oneself
to the case of a normalized cleavage, one would have had to introduce an additional object, namely a function $S \mapsto
\alpha_{S}$ associating to every object $S$ of $\mathcal{E}$ a functorial homomorphism $\alpha_{S}: (id_{S})* \to
id_{\mathcal{F}_{S}}$; condition A′) would then be replaced by condition A).

<!-- original page 175 -->

We shall now show how one can reconstruct, up to unique isomorphism, the normalized cloven category $\mathcal{F}$ over
$\mathcal{E}$ from the preceding objects.

## 8. Cloven Category Defined by a Pseudofunctor ℰ° → Cat

<!-- label: VI.8 -->

For short, call a **pseudofunctor** from $\mathcal{E}^{\circ}$ to `Cat`, one should say a **normalized** pseudofunctor,
a set of data a), b), c) as above, satisfying conditions A′) and B). In the preceding number we associated to a
normalized cloven category over $\mathcal{E}$ a pseudofunctor $\mathcal{E}^{\circ} \to Cat$. Here we indicate the
inverse construction. We shall leave to the reader the verification of most of the details, as well as of the fact that
these constructions are indeed “inverse” to one another. More precisely, one should regard the pseudofunctors
$\mathcal{E}^{\circ} \to Cat$ as the objects of a new category, and show that our constructions provide equivalences,
quasi-inverse to one another, between this latter category and the category of cloven categories over $\mathcal{E}$
defined in the preceding number.

Put

$$ \mathcal{F}^{\circ} = \coprod_{S\in Ob(\mathcal{E})} Ob(\mathcal{F}(S)), $$

the sum set of the sets $Ob(\mathcal{F}(S))$. N.B. here we write $\mathcal{F}(S)$, and not $\mathcal{F}_{S}$, for the
value at the object $S$ of $\mathcal{E}$ of the given pseudofunctor, to avoid notational confusion later. We therefore
have an evident map

$$ p^{\circ}: \mathcal{F}^{\circ} \to Ob(\mathcal{E}). $$

Let

```text
ξ̄ = (S,ξ),    η̄ = (T,η),    with ξ ∈ Ob(ℱ(S)), η ∈ Ob(ℱ(T)),
```

be two elements of $\mathcal{F}^{\circ}$, and let $f \in \operatorname{Hom}(T,S)$. Put

$$ h_{f}(\bar{\eta},\bar{\xi}) = \operatorname{Hom}_{\mathcal{F}(T)}(\eta, f*(\xi)). $$

<!-- original page 176 -->

If in addition one has a morphism $g: U \to T$ in $\mathcal{E}$ and $\zeta \in Ob(\mathcal{F}(U))$, one defines a map,
denoted $(u,v) \mapsto u \circ v$,

$$ h_{f}(\bar{\eta},\bar{\xi}) \times h_{g}(\bar{\zeta},\bar{\eta}) \to h_{fg}(\bar{\zeta},\bar{\xi}), $$

i.e. a map

```text
Hom_{ℱ(T)}(η, f*(ξ)) × Hom_{ℱ(U)}(ζ, g*(η))
  → Hom_{ℱ(U)}(ζ, (fg)*(ξ)),
```

by the formula

```text
u ∘ v = c_{f,g}(ξ) · g*(u) · v.
```

That is, $u \circ v$ is the composite of the sequence

```text
ζ --v--> g*(η) --g*(u)--> g*f*(ξ) --c_{f,g}(ξ)--> (fg)*(ξ).
```

On the other hand, put

$$ h(\bar{\eta},\bar{\xi}) = \coprod_{f\in \operatorname{Hom}(T,S)} h_{f}(\bar{\eta},\bar{\xi}). $$

The preceding pairings define pairings

$$ h(\bar{\eta},\bar{\xi}) \times h(\bar{\zeta},\bar{\eta}) \to h(\bar{\zeta},\bar{\xi}), $$

while the definition of the $h(\bar{\eta},\bar{\xi})$ gives an evident map

$$ p_{\bar{\eta},\bar{\xi}}: h(\bar{\eta},\bar{\xi}) \to \operatorname{Hom}(T,S). $$

This being said, one verifies the following points:

1. Composition between elements of the $h(\bar{\eta},\bar{\xi})$ is **associative**.

1. For every $\bar{\xi} = (S,\xi)$ in $\mathcal{F}^{\circ}$, consider the identity element of

<!-- original page 177 -->

$$ h_{id_{S}}(\bar{\xi},\bar{\xi}) = \operatorname{Hom}_{\mathcal{F}(S)}(id_{S}*(\xi),\xi) =
\operatorname{Hom}_{\mathcal{F}(S)}(\xi,\xi), $$

and its image in $h(\bar{\xi},\bar{\xi})$. This object is a **left and right unit** for composition between elements of
the $h(\bar{\eta},\bar{\xi})$.

This already shows that **one obtains a category** $\mathcal{F}$ by putting

$$ Ob(\mathcal{F}) = \mathcal{F}^{\circ}, Fl(\mathcal{F}) = \coprod_{\bar{\xi},\bar{\eta}\in \mathcal{F}^{\circ}}
h(\bar{\eta},\bar{\xi}). $$

N.B. one cannot simply take $Fl(\mathcal{F})$ to be the **union** of the sets $h(\bar{\eta},\bar{\xi})$, since these
latter sets are not necessarily disjoint. Moreover:

1. The maps $p^{\circ}: Ob(\mathcal{F}) \to Ob(\mathcal{E})$ and $p_{1} = (p_{\bar{\eta},\bar{\xi}}): Fl(\mathcal{F})
   \to Fl(\mathcal{E})$ define a **functor** $p: \mathcal{F} \to \mathcal{E}$. In this way $\mathcal{F}$ becomes a
   category over $\mathcal{E}$; moreover, the evident map $h_{f}(\bar{\eta},\bar{\xi}) \to
   \operatorname{Hom}(\bar{\eta},\bar{\xi})$ induces a **bijection**

$$ h_{f}(\bar{\eta},\bar{\xi}) \simeq \operatorname{Hom}_{f}(\bar{\eta},\bar{\xi}). $$

1. The evident maps

```text
Ob(ℱ(S)) → ℱ° = Ob(ℱ),    Fl(ℱ(S)) → Fl(ℱ),
```

where the second is defined by the evident maps

$$ \operatorname{Hom}_{\mathcal{F}(S)}(\xi,\xi') = h_{id_{S}}(\bar{\xi},\bar{\xi}') \to
\operatorname{Hom}(\bar{\xi},\bar{\xi}'), $$

define an **isomorphism**

$$ i_{S}: \mathcal{F}(S) \simeq \mathcal{F}_{S}. $$

1. For every object $\bar{\xi} = (S,\xi)$ of $\mathcal{F}$, and every morphism $f: T \to S$ of $\mathcal{E}$, consider

<!-- original page 178 -->

the element $\bar{\eta} = (T,\eta)$ of $\mathcal{F}_{T}$, with $\eta = f*(\xi)$, and the element $\alpha_{f}(\xi)$ of
$\operatorname{Hom}(\bar{\eta},\bar{\xi})$, image of $id_{f*(\xi)}$ by the morphism

$$ \operatorname{Hom}_{\mathcal{F}(T)}(f*(\xi),f*(\xi)) = h_{f}(\bar{\eta},\bar{\xi}) \to
\operatorname{Hom}_{f}(\bar{\eta},\bar{\xi}). $$

**This element is cartesian, and it is the identity of $\bar{\xi}$ if $f = id_{S}$**. In other words, the set of the
$\alpha_{f}(\xi)$ defines a **normalized cleavage of $\mathcal{F}$ over $\mathcal{E}$**. Moreover, by construction, one
has commutativity in the diagram of functors

$$ \mathcal{F}(S) --f*--> \mathcal{F}(T) | i_{S} | i_{T} \downarrow \downarrow \mathcal{F}_{S} --f*_{\mathcal{F}}->
\mathcal{F}_{T}, $$

where $f*_{\mathcal{F}}$ is the inverse-image functor by $f$, relative to the cleavage considered on $\mathcal{F}$.
Finally:

1. The homomorphisms $c_{f,g}$ given with the pseudofunctor are transformed, by the isomorphisms $i_{S}$, into the
   functorial homomorphisms $c_{f,g}$ associated with the cleavage of $\mathcal{F}$.

We restrict ourselves to giving the verification of 1), which is, if anything, less trivial than the others. It suffices
to prove associativity of composition between objects of sets of the form $h_{f}(\bar{\eta},\bar{\xi})$. Thus consider
in $\mathcal{E}$ morphisms

```text
S ←^f T ←^g U ←^h V
```

and objects

```text
ξ, η, ζ, τ
```

in $\mathcal{F}(S)$, $\mathcal{F}(T)$, $\mathcal{F}(U)$, $\mathcal{F}(V)$, and finally elements

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

which is an equality in $\operatorname{Hom}_{\mathcal{F}(V)}(\tau,(fgh)*(\xi))$. By the definitions, the two members of
this equality are obtained by composition along the upper and lower contours of the diagram below:

```text
τ --w--> h*(ζ) --h*(v)--> h*g*(η) --h*g*(u)--> h*g*f*(ξ) --h*(c_{f,g}(ξ))--> h*(fg)*(ξ)
 \____________________ v∘w ____________________/       | c_{g,h}(f*(ξ))              | c_{fg,h}(ξ)
                         ↓                              ↓                             ↓
                  (gh)*(η) --(gh)*(u)-->        (gh)*f*(ξ) --c_{f,gh}(ξ)-->       (fgh)*(ξ).
```

The middle square is commutative because $c_{g,h}$ is a functorial homomorphism, and the square on the right is
commutative by condition B) for a pseudofunctor. This gives the asserted result.

Of course, it remains to specify, when the pseudofunctor considered already comes from a normalized cloven category
$\mathcal{F}'$ over $\mathcal{E}$, how one obtains a natural isomorphism between $\mathcal{F}'$ and $\mathcal{F}$. We
leave the details to the reader.

We likewise leave to the reader the interpretation, in terms of pseudofunctors, of the notion of inverse image of a
cloven category $\mathcal{F}$ over $\mathcal{E}$ by a base-change functor $\mathcal{E}' \to \mathcal{E}$.

## 9. Example: Cloven Category Defined by a Functor ℰ° → Cat; Split Categories over ℰ

<!-- label: VI.9 -->

Suppose one has a functor

$$ \phi: \mathcal{E}^{\circ} \to Cat. $$

It then defines a pseudofunctor by putting

```text
ℱ(S) = φ(S),    f* = φ(f),    c_{f,g} = id_{(fg)*}.
```

<!-- original page 180 -->

Thus the construction of the preceding number gives us a category $\mathcal{F}$ cloven over $\mathcal{E}$, said to be
associated with the functor $\phi$. For a cloven category over $\mathcal{E}$ to be isomorphic to a cloven category
defined by a functor $\phi: \mathcal{E}^{\circ} \to Cat$, it is manifestly necessary and sufficient that it satisfy the
conditions

```text
(fg)* = g*f*,    c_{f,g} = id_{(fg)*}.
```

In terms of the set $K$ of transport morphisms, this also simply means that **the composite of two transport morphisms
is a transport morphism**. A cleavage of a category $\mathcal{F}$ over $\mathcal{E}$ satisfying the preceding condition
is called a **splitting** of $\mathcal{F}$ over $\mathcal{E}$, and a category $\mathcal{F}$ over $\mathcal{E}$ endowed
with a splitting is called a **split category over $\mathcal{E}$**. It is therefore a special case of the notion of
cloven category. The category of split categories over $\mathcal{E}$ is therefore equivalent to `Hom̲(ℰ°,Cat)`. Note that
a split category over $\mathcal{E}$ is a fortiori a cloven category over $\mathcal{E}$.

If $\mathcal{F}$ is a fibered category over $\mathcal{E}$, there does not always exist a splitting on $\mathcal{F}$.
Suppose for example that $Ob(\mathcal{E})$ and $Ob(\mathcal{F})$ are reduced to one element, and that the set of
endomorphisms of that element is a group $E$, respectively $F$, so that the projection functor $p$ is given by a group
homomorphism $p: F \to E$, surjective since $p$ is fibrant. One verifies at once that the set of cleavages of
$\mathcal{F}$ over $\mathcal{E}$ is in bijective correspondence with the set of maps $s: E \to F$ such that $ps =
id_{E}$, i.e. the set of “systems of representatives” for the classes modulo the subgroup $G$ that is the kernel of the
surjective homomorphism $p: F \to E$. A cleavage is a splitting if and only if $s$ is a group homomorphism. To say that
a splitting exists therefore means that the group extension $F$ of $E$ by $G$ is trivial, which is expressed, when $G$
is commutative, by the vanishing of a certain cohomology class in $H^{2}(E,G)$, where $G$ is regarded as a group on
which $E$ operates.

Suppose, however, that $\mathcal{F}$ is a fibered category over $\mathcal{E}$ such that the

<!-- original page 181 -->

$\mathcal{F}_{S}$ are **rigid** categories, i.e. the automorphism group of every object of $\mathcal{F}_{S}$ is reduced
to the identity. It is then easy to prove that $\mathcal{F}$ admits a splitting over $\mathcal{E}$. Indeed, one first
observes that the question of existence of a splitting is not changed if $\mathcal{F}$ is replaced by an
$\mathcal{E}$-equivalent category. This reduces us in the present case to the case where the $\mathcal{F}_{S}$ are rigid
**and reduced** categories, i.e. two isomorphic objects in $\mathcal{F}_{S}$ are identical. But if $G$ is a rigid and
reduced category, every isomorphism between two functors $H \to G$, where $H$ is any category, is an identity. It
follows that if $\mathcal{F}$ is a fibered category over $\mathcal{E}$ whose fiber categories are rigid and reduced,
then there exists a **unique** cleavage of $\mathcal{F}$ over $\mathcal{E}$, which is necessarily a splitting. Thus
$\mathcal{F}$ is isomorphic to the category defined by a functor $\phi: \mathcal{E}^{\circ} \to Cat$ such that the
$\phi(S)$ are rigid and discrete categories, and the functor $\phi$ is defined up to isomorphism.

## 10. Co-Fibered Categories, Bi-Fibered Categories

<!-- label: VI.10 -->

Consider a category $\mathcal{F}$ over $\mathcal{E}$, with projection functor

$$ p: \mathcal{F} \to \mathcal{E}. $$

It defines a category $\mathcal{F}^{\circ}$ over $\mathcal{E}^{\circ}$ by the projection functor

$$ p^{\circ}: \mathcal{F}^{\circ} \to \mathcal{E}^{\circ}. $$

A morphism $\alpha: \eta \to \xi$ in $\mathcal{F}$ is said to be **co-cartesian** if it is a cartesian morphism for
$\mathcal{F}^{\circ}$ over $\mathcal{E}^{\circ}$. Spelling this out, one sees that it means that for every object $\xi'$
of $\mathcal{F}_{S}$, the map $u \mapsto u \circ \alpha$

$$ \operatorname{Hom}_{S}(\xi,\xi') \to \operatorname{Hom}_{f}(\eta,\xi') $$

is bijective. One then also says that $(\xi,\alpha)$ is a **direct image** of $\eta$ by $f$, in the category
$\mathcal{F}$ over $\mathcal{E}$. If it exists for every $\eta$ in $\mathcal{F}_{T}$, one says that the direct-image
functor by $f$ exists; once it has been chosen, this functor is denoted

<!-- original page 182 -->

$$ f*_{\mathcal{F}} or f_{*}. $$

It is therefore defined by an isomorphism of bifunctors on $\mathcal{F}^{\circ}_{T} \times \mathcal{F}_{S}$:

$$ \operatorname{Hom}_{S}(f_{*}(\eta),\xi) \simeq \operatorname{Hom}_{f}(\eta,\xi). $$

Thus, if $f_{*}$ exists, then for $f*$ to exist it is necessary and sufficient that $f_{*}$ admit an adjoint functor,
i.e. that there exist a functor $f*: \mathcal{F}_{S} \to \mathcal{F}_{T}$ and an isomorphism of bifunctors

$$ \operatorname{Hom}_{S}(f_{*}(\eta),\xi) \simeq \operatorname{Hom}_{T}(\eta,f*(\xi)). $$

Let $g: U \to T$ be another morphism in $\mathcal{E}$, and suppose that the inverse and direct images by $f$, $g$, and
`fg` exist. Consider then the functorial homomorphisms

```text
c^{f,g}: f_* g_* ← (fg)_*,
c_{f,g}: g* f* → (fg)*.
```

One observes that, if $f_{*} g_{*}$ and $g* f*$ are regarded as a pair of adjoint functors, and likewise $(fg)_{*}$ and
$(fg)*$, then the two preceding homomorphisms are adjoint to one another. Thus one is an isomorphism if and only if the
other is. In particular:

**Proposition.**

<!-- label: VI.10.1 -->

Suppose that the category $\mathcal{F}$ over $\mathcal{E}$ is prefibered and co-prefibered. In order that it be fibered,
it is necessary and sufficient that it be co-fibered.

Of course, $\mathcal{F}$ is said to be co-prefibered, respectively co-fibered, over $\mathcal{E}$ if
$\mathcal{F}^{\circ}$ is prefibered, respectively fibered, over $\mathcal{E}$. We shall say that $\mathcal{F}$ is
**bi-fibered** over $\mathcal{E}$ if it is both fibered and co-fibered over $\mathcal{E}$.

## 11. Various Examples

<!-- label: VI.11 -->

### a) Categories of Arrows of ℰ

Let $\mathcal{E}$ be a category. Denote by $\Delta^{1}$ the category associated with the totally ordered set with two
elements `[0,1]`. It therefore has two objects `0` and `1`, and besides the two identity morphisms one arrow `(0,1)`
with source `0` and target `1`. Let

<!-- original page 183 -->

```text
Ar(ℰ) = Hom̲(Δ¹,ℰ).
```

This is called the **category of arrows of** $\mathcal{E}$. The object `1` of $\Delta^{1}$ defines a canonical functor,
called the **target functor**

$$ Ar(\mathcal{E}) \to \mathcal{E} $$

the functor defined by the object `0` of $\Delta^{1}$ being called the **source functor**. For every object $S$ of
$\mathcal{E}$, the fiber category $Ar(\mathcal{E})_{S}$ is canonically isomorphic to the category $\mathcal{E}_{/}S$ of
objects of $\mathcal{E}$ over $S$.

Consider a morphism $f: T \to S$ in $\mathcal{E}$. To it there corresponds a canonical functor

```text
f_*: ℰ_/T = ℱ_T → ℰ_/S = ℱ_S
```

and a functorial isomorphism

$$ \operatorname{Hom}_{S}(f_{*}(\eta),\xi) \simeq \operatorname{Hom}_{f}(\eta,\xi), $$

which therefore makes $f_{*}$ a direct-image functor for $f$ in $\mathcal{F}$. Moreover, here

```text
(id_S)_* = id_{ℱ_S},    (fg)_* = f_* g_*,    c^{f,g} = id_{(fg)},
```

i.e. $\mathcal{F}$ is endowed with a co-splitting over $\mathcal{E}$. A fortiori, $\mathcal{F}$ is co-fibered over
$\mathcal{E}$. Note now that the set of morphisms in $\mathcal{F}$ is in bijective correspondence with the set of
commutative square diagrams in $\mathcal{E}$:

```text
Y --f′--> X
| v      | u
↓        ↓
T --f--> S.
```

<!-- original page 184 -->

By definition, the morphism in question is cartesian if the square is cartesian in $\mathcal{E}$, i.e. if it makes $Y$ a
fiber product of $X$ and $T$ over $S$. The inverse-image functor $f*$ therefore exists if and only if, for every object
$X$ over $S$, the fiber product $X \times_{S} T$ exists. It follows from VI.10.1 that if the product of two objects over
a third always exists in $\mathcal{E}$, i.e. if $\mathcal{F}$ is prefibered over $\mathcal{E}$, then $\mathcal{F}$ is
even fibered over $\mathcal{E}$.

### b) Category of Presheaves or Sheaves on Variable Spaces

Let $\mathcal{E} = Top$ be the category of topological spaces. If $T$ is a topological space, we denote by
$\mathcal{U}(T)$ the category of open subsets of $T$, whose morphisms are inclusion maps. If $\mathcal{C}$ is a
category, a functor $\mathcal{U}(T)^{\circ} \to \mathcal{C}$ is called a **presheaf** on $T$ with values in
$\mathcal{C}$, and a **sheaf** if it satisfies a left-exactness condition that we shall not repeat here.

The **category $\mathcal{P}(T)$ of presheaves on $T$ with values in $\mathcal{C}$** is, by definition, the category
`Hom̲(𝒰(T)°,𝒞)`, and the category $\mathcal{F}(T)$ of sheaves on $T$ with values in $\mathcal{C}$ is the full subcategory
whose objects are the objects of `Hom̲(𝒰(T)°,𝒞)` that are sheaves. If $f: T \to S$ is a morphism in $\mathcal{E}$, i.e. a
continuous map of topological spaces, then by the increasing map $U \mapsto f^{-1}(U)$ there corresponds to it a functor
$\mathcal{U}(S) \to \mathcal{U}(T)$, whence a functor

```text
f_*: Hom̲(𝒰(T)°,𝒞) → Hom̲(𝒰(S)°,𝒞)
```

called the **direct-image functor of presheaves by** $f$. One sees at once that the direct image of a sheaf is a sheaf.
Thus the functor $f_{*}: \mathcal{P}(T) \to \mathcal{P}(S)$ induces a functor, also denoted

$$ f_{*}: \mathcal{F}(T) \to \mathcal{F}(S). $$

Moreover, one verifies trivially, by associativity of composition of functors, that for a second continuous map $g: U
\to T$ one has the identity

```text
(gf)_* = g_* f_*,    and likewise    (id_S)_* = id_{𝒫(S)}.
```

In this way one obtains a functor

$$ S \mapsto \mathcal{P}(S) $$

respectively

$$ S \mapsto \mathcal{F}(S) $$

<!-- original page 185 -->

from $\mathcal{E}$ to `Cat`. In fact, we are interested in the corresponding functor

```text
S ↦ 𝒫(S)°,    respectively    S ↦ ℱ(S)°.
```

It defines a co-fibered, indeed co-split, category over the category of topological spaces, called the **co-fibered
category of presheaves**, respectively **sheaves**, **with values in** $\mathcal{C}$, understood as on variable spaces.
Spelling out the construction of VI.8, one sees that a morphism from a presheaf $B$ on $T$ to a presheaf $A$ on $S$ is a
pair $(f,u)$ formed by a continuous map from $T$ to $S$ and a morphism $u: A \to f_{*}(B)$ in the category
$\mathcal{P}(S)$. This description is equally valid for morphisms of sheaves, $\mathcal{F}$ being a full subcategory of
$\mathcal{P}$.

In the most important cases, the category $\mathcal{P}$ and the category $\mathcal{F}$ over $\mathcal{E}$ are also
fibered categories; that is, for every continuous map, the direct-image functors $\mathcal{P}(T) \to \mathcal{P}(S)$ and
$\mathcal{F}(T) \to \mathcal{F}(S)$ have an adjoint functor, then denoted $f*$ and called the inverse-image functor of
presheaves, respectively the inverse-image functor of sheaves, by the continuous map $f$. This functor exists, for
example, if $\mathcal{C} = Set$. One can show that the functor $f*: \mathcal{P}(S) \to \mathcal{P}(T)$ exists whenever
inductive limits, relative to diagrams in the Universe under consideration, exist in $\mathcal{C}$. The question is less
easy for $\mathcal{F}$. Indeed, even in the case $\mathcal{C} = Set$, the inverse image of a presheaf that is a sheaf is
not in general a sheaf; in other words, the inverse-image functor of sheaves is not isomorphic to the functor induced by
the inverse-image functor of presheaves, despite the common notation $f*$. Thus $\mathcal{F}$ is a co-fibered
subcategory of $\mathcal{P}$, but not a fibered subcategory; i.e. **the inclusion functor $\mathcal{F} \to \mathcal{P}$
is not fibrant**.

The co-fibered category $\mathcal{P}$ can be deduced from a more general co-fibered, or rather fibered, category
obtained as follows. For every category $\mathcal{U}$ in the fixed Universe, put

```text
𝒫(𝒰) = Hom̲(𝒰,𝒞),
```

and

<!-- original page 186 -->

note that $\mathcal{U} \mapsto \mathcal{P}(\mathcal{U})$ is naturally a contravariant functor in $\mathcal{U}$, from the
category `Cat` to `Cat`. It therefore defines a split category over $\mathcal{E} = Cat$, which we shall denote
$Cat_{/}/\mathcal{C}$. The objects of this category are pairs $(\mathcal{U},p)$, where $\mathcal{U}$ is a category and
$p: \mathcal{U} \to \mathcal{C}$ is a functor; a morphism from $(\mathcal{U},p)$ to $(\mathcal{V},q)$ is essentially a
pair $(f,u)$, where $f$ is a functor $\mathcal{U} \to \mathcal{V}$ and $u$ is a homomorphism of functors $u: p \to qf$.
We leave to the reader the task of spelling out the composition of morphisms in $Cat_{/}/\mathcal{C}$.

The projection functor

```text
ℱ = Cat_//𝒞 → ℰ = Cat
```

sends the pair $(\mathcal{U},p)$ to the object $\mathcal{U}$. The fiber category at $\mathcal{U}$ is the category
`Hom̲(𝒰,𝒞)`, up to isomorphism. When inductive limits exist in $\mathcal{C}$, one shows easily that the fibered category
$Cat_{/}/\mathcal{C}$ over `Cat` is also co-fibered over `Cat`; i.e. one can define the notion of **direct image of a
functor** $p: \mathcal{U} \to \mathcal{C}$ by a functor $f: \mathcal{U} \to \mathcal{V}$.

The category of presheaves is deduced from the preceding fibered category by the base change

$$ Top^{\circ} \to Cat $$

the functor $S \mapsto \mathcal{U}(S)$ defined above. This gives a fibered category over $Top^{\circ}$, and by passing
to the opposite category one obtains the co-fibered category $\mathcal{P}$ of presheaves over `Top`. The notion of
inverse image of a functor corresponds to that of direct image of a presheaf; the notion of direct image of a functor
corresponds to that of inverse image of a presheaf.

### c) Objects with Operators over an Object with Operators

Let $\mathcal{F}$ be a category over $\mathcal{E}$, and let $S$ be an object of $\mathcal{E}$ on which a group $G$
operates, on the left to fix ideas. This object with operators can be interpreted as corresponding to a functor
$\lambda: \mathcal{E}' \to \mathcal{E}$ from the category $\mathcal{E}'$ defined by $G$, with a single object and $G$ as
its group of endomorphisms, to the category $\mathcal{E}$. It therefore defines by base change a category $\mathcal{F}'$
over $\mathcal{E}'$, which is fibered, respectively co-fibered, when $\mathcal{F}$ is so over $\mathcal{E}$.

<!-- original page 187 -->

A section of $\mathcal{E}'$ over $\mathcal{F}'$, necessarily cartesian, since $\mathcal{E}'$ is a groupoid and every
isomorphism in $\mathcal{F}'$ is cartesian by VI.6.12, can also be interpreted as an $\mathcal{E}$-functor $\mathcal{E}'
\to \mathcal{F}$ over $\lambda$, or also as an object with operators $\xi$ in $\mathcal{F}$ “over” the object with
operators $S$.

### d) Pairs of Quasi-Inverse Adjoint Functors; Autodualities

When the base category $\mathcal{E}$ is reduced to two objects $a$, $b$ and, besides the identity arrows, to two
isomorphisms $f: a \to b$ and $g: b \to a$ inverse to one another, i.e. $\mathcal{E}$ is a connected rigid groupoid with
two objects, a normalized cloven category over $\mathcal{E}$ is essentially the same thing as the system formed by two
categories $\mathcal{F}_{a}$ and $\mathcal{F}_{b}$ and a **pair of adjoint functors** $G: \mathcal{F}_{a} \to
\mathcal{F}_{b}$ and $F: \mathcal{F}_{b} \to \mathcal{F}_{a}$ that are equivalences of categories, hence quasi-inverse
to one another. One takes for $\mathcal{F}_{a}$ and $\mathcal{F}_{b}$ the fiber categories of $\mathcal{F}$, for $F$ and
$G$ the functors $f*$ and $g*$, and the two isomorphisms

```text
u: FG ≃ id_{ℱ_a},    v: GF ≃ id_{ℱ_b}
```

are $c_{g,f}$ and $c_{f,g}$. The two usual compatibility conditions between $u$ and $v$ are nothing other than condition
VI.7.4 B) for the composites `fgf` and `gfg`. It is easy to show that these conditions suffice to imply that one indeed
has a pseudofunctor $\mathcal{E}^{\circ} \to Cat$.

An interesting case is the one in which

```text
ℱ_b = ℱ_a°,    G = F°,    v = u°.
```

An **autoduality** in a category $\mathcal{C}$ means the data of a functor $D: \mathcal{C} \to \mathcal{C}^{\circ}$ and
an isomorphism $u: DD^{\circ} \simeq id_{\mathcal{C}}$ such that $u$ and the isomorphism $u^{\circ}: D^{\circ}D \simeq
id^{\circ}_{\mathcal{C}}$ make $(D,D^{\circ})$ a pair of adjoint functors, necessarily quasi-inverse to one another.
This condition is written

```text
D(u(x)) = u(D(x))    for every x ∈ Ob(𝒞).
```

### e) Categories over a Discrete Category ℰ

<!-- original page 188 -->

One says that $\mathcal{E}$ is a **discrete category** if every arrow in it is an identity arrow, so that $\mathcal{E}$
is defined up to unique isomorphism by knowing the set $I = Ob(\mathcal{E})$. The data of a category $\mathcal{F}$ over
$\mathcal{E}$ is therefore equivalent, up to unique isomorphism, to the data of a family of categories
$\mathcal{F}_{i}$, $i \in I$, the fiber categories. Every category $\mathcal{F}$ over $\mathcal{E}$ is fibered; every
$\mathcal{E}$-functor $\mathcal{F} \to \mathcal{G}$ is cartesian; one has a canonical isomorphism

```text
Hom̲_{ℰ/-}(ℱ,𝒢) ≃ ∏ᵢ Hom̲(ℱᵢ,𝒢ᵢ).
```

In particular, one obtains

```text
Γ̲(ℱ/ℰ) = Lim←(ℱ/ℰ) ≃ ∏ᵢ ℱᵢ.
```

### f) Suppose that ℰ Has Exactly Two Objects S and T

Suppose that, besides the identity morphisms, $\mathcal{E}$ has one morphism $f: T \to S$. Then a category $\mathcal{F}$
over $\mathcal{E}$ is defined, up to unique $\mathcal{E}$-isomorphism, by the data of two categories $\mathcal{F}_{S}$
and $\mathcal{F}_{T}$ and a bifunctor $H(\eta,\xi)$ on $\mathcal{F}^{\circ}_{T} \times \mathcal{F}_{S}$ with values in
`Set`. Indeed, if $\mathcal{F}$ is a category over $\mathcal{E}$, one associates to it the two fiber categories
$\mathcal{F}_{S}$ and $\mathcal{F}_{T}$ and the bifunctor $H(\eta,\xi) = \operatorname{Hom}_{f}(\eta,\xi)$. We leave to
the reader the task of spelling out the construction in the opposite direction. For the category in question to be
fibered, or prefibered, which comes to the same thing, it is necessary and sufficient that the functor $H$ be
representable with respect to the argument $\xi$. For it to be co-fibered, it is necessary and sufficient that $H$ be
representable with respect to the argument $\eta$.

### g)

Let $\mathcal{F} = \mathcal{C} \times \mathcal{E}$, regarded as a category over $\mathcal{E}$ by means of $pr_{2}$. Then
$\mathcal{F}$ is fibered and co-fibered over $\mathcal{E}$, and is even endowed with a canonical splitting and
co-splitting, corresponding to the constant functor on $\mathcal{E}$, respectively on $\mathcal{E}^{\circ}$, with values
in `Cat` and value $\mathcal{C}$. One has

```text
Γ̲(ℱ/ℰ) ≃ Hom̲(ℰ,𝒞),
```

and

<!-- original page 189 -->

$Lim\leftarrow(\mathcal{F}/\mathcal{E})$ corresponds to the full subcategory formed by the functors $F: \mathcal{E} \to
\mathcal{C}$ that transform arbitrary morphisms into isomorphisms.

## 12. Functors on a Cloven Category

<!-- label: VI.12 -->

Let $\mathcal{F}$ be a normalized cloven category over $\mathcal{E}$. For every object $S$ of $\mathcal{E}$, denote by

$$ i_{S}: \mathcal{F}_{S} \to \mathcal{F} $$

the inclusion functor. Thus one has a functorial homomorphism, for every morphism $f: T \to S$ in $\mathcal{E}$,

```text
α_f: i_T f* → i_S,
```

where $f*$ is the base-change functor $\mathcal{F}_{S} \to \mathcal{F}_{T}$ for $f$ defined by the cleavage. Let now

$$ F: \mathcal{F} \to \mathcal{C} $$

be a functor from $\mathcal{F}$ to a category $\mathcal{C}$. Put, for every $S \in Ob(\mathcal{E})$,

```text
F_S = F ∘ i_S: ℱ_S → 𝒞,
```

and for every $f: T \to S$ in $\mathcal{E}$,

```text
φ_f = F ∗ α_f: F_T f* → F_S.
```

Thus to every functor $F: \mathcal{F} \to \mathcal{C}$ there is associated a family `(F_S)` of functors $\mathcal{F}_{S}
\to \mathcal{C}$, and a family $(\phi_{f})$ of homomorphisms of functors $F_{T} f* \to F_{S}$. These families satisfy
the following conditions:

a) $\phi_{id_{S}} = id_{F_{S}}$.

b) For two morphisms $f: T \to S$ and $g: U \to T$ in $\mathcal{E}$, one has commutativity in the square of functorial
homomorphisms:

```text
F_U g* f* --F_U ∗ c_{f,g}--> F_U(fg)*
    | φ_g ∗ f*                  | φ_{fg}
    ↓                           ↓
F_T f* ------φ_f-------------> F_S.
```

<!-- original page 190 -->

The first relation is trivial, and the second relation is obtained by applying the functor $F$ to the commutative
diagram

```text
g*f*(ξ) --c_{f,g}(ξ)--> (fg)*(ξ)
   | α_g(f*(ξ))             | α_{fg}(ξ)
   ↓                        ↓
f*(ξ) --α_f(ξ)----------->  ξ
```

for variable $\xi$ in $\mathcal{F}_{S}$.

If $G$ is a second functor $\mathcal{F} \to \mathcal{C}$, giving rise to functors $G_{S}: \mathcal{F}_{S} \to
\mathcal{C}$ and functorial homomorphisms $\psi_{f}: G_{T} f* \to G_{S}$, and if $u: F \to G$ is a functorial
homomorphism, then to it there correspond the functorial homomorphisms $u \ast i_{S}$:

$$ u_{S}: F_{S} \to G_{S}. $$

One checks at once that, for every morphism $f: T \to S$ in $\mathcal{E}$, one has commutativity in the squares

```text
c)  F_T f* --φ_f--> F_S
       | u_T ∗ f*      | u_S
       ↓               ↓
    G_T f* --ψ_f--> G_S.
```

**Proposition.**

<!-- label: VI.12.1 -->

Let $\mathcal{H}(\mathcal{F},\mathcal{C})$ be the category whose objects are pairs of families `(F_S)`, $S \in
Ob(\mathcal{E})$, of functors $\mathcal{F}_{S} \to \mathcal{C}$, and of families $(\phi_{f})$, $f \in Fl(\mathcal{E})$,
of functorial homomorphisms $F_{T} f* \to F_{S}$ satisfying conditions **a)** and **b)**, and whose morphisms are the
families $(u_{S})$, $S \in Ob(\mathcal{E})$, of homomorphisms $F_{S} \to G_{S}$ verifying the commutativity condition
**c)** written above; composition of morphisms is by composition of homomorphisms of functors $\mathcal{F}_{S} \to
\mathcal{C}$. Then the two laws just described define an **isomorphism** $K$ from the category `Hom̲(ℱ,𝒞)` to the
category $\mathcal{H}(\mathcal{F},\mathcal{C})$.

<!-- original page 191 -->

It is trivial that this is indeed a **functor** from the first category to the second. This functor is fully faithful:
for given $F$, $G$, the map $\operatorname{Hom}(F,G) \to \operatorname{Hom}(K(F),K(G))$ is trivially injective. To show
that it is surjective, it suffices to note that commutativity condition c) expresses the functoriality of the maps

```text
u(ξ) = u_S(ξ): F(ξ) = F_S(ξ) → G(ξ) = G_S(ξ)
```

for homomorphisms of the form $\alpha_{f}(\xi)$ in $\mathcal{F}$. On the other hand, one has functoriality on each fiber
category, i.e. for morphisms in $\mathcal{F}$ that are $T$-morphisms with $T \in Ob(\mathcal{E})$. Hence one has
functoriality for every morphism in $\mathcal{F}$, since an $f$-morphism, where $f: T \to S$ is a morphism in
$\mathcal{E}$, is uniquely a composite of a morphism $\alpha_{f}(\xi)$ and a $T$-morphism.

It remains therefore to prove that the functor $K$ is bijective on objects. The preceding argument already shows that
$K$ is injective on objects; it remains to prove that it is surjective. That is, suppose we start from a system `(F_S)`,
$(\phi_{f})$ satisfying a) and b), and define a map $Ob(\mathcal{F}) \to Ob(\mathcal{C})$ by

```text
F(ξ) = F_S(ξ)    for ξ ∈ Ob(ℱ_S) ⊂ Ob(ℱ),
```

and a map $Fl(\mathcal{F}) \to Fl(\mathcal{C})$ by

$$ F(\alpha_{f}(\xi)u') = \phi_{f}(\xi) F_{T}(u'), $$

for every morphism $f: T \to S$ in $\mathcal{E}$, every object $\xi$ of $\mathcal{F}_{S}$, and every $T$-morphism $u'$
with target $f*(\xi)$. Then one obtains a **functor** $F$ from $\mathcal{F}$ to $\mathcal{C}$. Indeed, the relation
$F(id_{\xi}) = id_{F(\xi)}$ is trivial; it remains to prove multiplicativity $F(uv) = F(u)F(v)$ when one has an
$f$-morphism $u: \eta \to \xi$ and a $g$-morphism $v: \zeta \to \eta$, with $f: T \to S$ and $g: U \to T$ morphisms of
$\mathcal{E}$. Putting $w = uv$, one has

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

The left triangle is commutative by definition of $F(v)$; the middle square is commutative because it is deduced from
the homomorphism $u'$ by the functorial homomorphism $\phi_{g}$; finally the right square is commutative by condition
b). The desired conclusion follows.

Suppose now that $\mathcal{C}$ is also a normalized cloven category over $\mathcal{E}$, which from now on we shall call
$\mathcal{G}$, and that we are interested in $\mathcal{E}$-functors from $\mathcal{F}$ to $\mathcal{G}$. If $F$ is such
a functor, it induces functors

$$ F_{S}: \mathcal{F}_{S} \to \mathcal{G}_{S} $$

on the fiber categories. On the other hand, for every morphism $f: T \to S$ in $\mathcal{E}$ and every object $\xi$ in
$\mathcal{F}_{S}$, the $f$-morphism $F(\alpha_{f}(\xi))$ factors uniquely through a $T$-morphism

$$ \phi_{f}(\xi): F_{T}(f*_{\mathcal{F}}(\xi)) \to f*_{\mathcal{G}}(F_{S}(\xi)), $$

where the subscript $\mathcal{F}$ or $\mathcal{G}$ indicates the cloven category in which the inverse-image functor is
being taken. Hence one obtains a functorial homomorphism of functors from $\mathcal{F}_{S}$ to $\mathcal{G}_{T}$:

```text
φ_f: F_T f*_ℱ → f*_𝒢 F_S.
```

<!-- original page 193 -->

The two systems `(F_S)` and $(\phi_{f})$ satisfy the following conditions:

a′) $\phi_{id_{S}} = id_{F_{S}}$.

b′) For two morphisms $f: T \to S$ and $g: U \to T$ in $\mathcal{E}$, one has commutativity in the following diagram of
functorial homomorphisms:

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
which implies that one obtains in this way a bijective correspondence between the set of $\mathcal{E}$-functors from
$\mathcal{F}$ to $\mathcal{G}$ and the set of systems `(F_S)`, $(\phi_{f})$ satisfying conditions a′) and b′) above. Of
course, in this correspondence, the cartesian functors are characterized by the property that the homomorphisms
$\phi_{f}$ are isomorphisms.

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
