# SGA 4-I — Expose I: Presheaves

> Translated from the cleaned OCR transcription of the image-only SGA 4-I scan. The file has been normalized for
> readability. Diagrams and dense formulas remain in fenced text blocks where faithful Markdown transcription is
> uncertain. Consult the PDF for mathematical fidelity.

[PDF p. 17]

# Expose I — Presheaves

By A. Grothendieck and J.-L. Verdier, with an appendix by N. Bourbaki.

In sections 0 to 5 of this expose, we present the elementary, and most often well-known, properties of categories of
presheaves (*). These properties are used constantly in the sequel of the Seminar, and knowing them is essential for
understanding the following exposes. The proofs are immediate; they are most often omitted.

In sections 6 to 9 we touch on a few themes used several times later. The reader in a hurry may omit them on first
reading. Section 10 fixes the terminology used. Appendix 11 is due to N. Bourbaki.

(*) The reader may also consult SGA 3 I, §§ 1 to 3.

## 0. Universes

A universe is a nonempty set $U$ having the following properties:

- (U1) If $x \in U$ and if $y \in x$, then $y \in U$.
- (U2) If $x,y \in U$, then $\{x,y\} \in U$.
- (U3) If $x \in U$, then $\mathcal{P}(x) \in U$.
- (U4) If $(x_i)_{i \in I}$ is a family of elements of $U$ and if $I \in U$, then $\bigcup_{i \in I} x_i \in U$.

[PDF p. 18]

From the preceding axioms one easily deduces the following properties:

- If $x \in U$, the set $\{x\}$ belongs to $U$.
- If $x$ is a subset of $y \in U$, then $x \in U$.
- If $x,y \in U$, the ordered pair $(x,y)=\{\{x,y\},\{x\}\}$ (Kuratowski's definition) is an element of $U$.
- If $x,y \in U$, the union $x \cup y$ and the product $x \times y$ are elements of $U$.
- If $(x_i)_{i \in I}$ is a family of elements of $U$ and if $I \in U$, the product $\prod_{i \in I} x_i$ is an element
  of $U$.
- If $x \in U$, then $\operatorname{card}(\mathcal{P}(x)) < \operatorname{card}(U)$, strictly. In particular the
  relation $U \in U$ does not hold.

Thus one can perform all the usual operations of set theory starting from the elements of a universe without the final
result thereby ceasing to be an element of the universe.

The first use of the notion of universe is to provide a definition of the usual categories: the category of sets
belonging to the universe $U$, denoted $U\text{-}\mathbf{Ens}$; the category of topological spaces belonging to $U$; the
category of commutative groups belonging to $U$, denoted $U\text{-}\mathbf{Ab}$; the category of categories belonging to
$U$; and so on.

However, the only known universe is the set of symbols of the form $\emptyset$, $\{\emptyset\}$,
$\{\{\emptyset\},\emptyset\}$, and so on. All elements of this universe are finite sets, and this universe is countable.
In particular, no universe is known which contains an element of infinite cardinality. One is therefore led to add to
the axioms of set theory the axiom:

$(\mathrm{UA})$ For every set $x$, there exists a universe $U$ such that $x \in U$.

[PDF p. 19]

Since the intersection of a family of universes is a universe, it follows immediately that every set is an element of a
smallest universe. One can show that axiom (UA) is independent of the axioms of set theory.

We shall also add the axiom:

$(\mathrm{UB})$ Let $R(x)$ be a relation and let $U$ be a universe. If there exists an element $y \in U$ such that
$R(y)$, then there exists $x \in U$ such that $R(x)$.

The non-contradiction of the axioms (UA) and (UB), relative to the other axioms of set theory, has not been proved and,
it seems, is not provable.

Let $U$ be a universe and let $c(U)$ be the least upper bound of the cardinals of the elements of $U$, so that
$c(U)=\operatorname{card}(U)$. The cardinal $c(U)$ has the following properties:

- (FI) If $a<c(U)$, then $2^a<c(U)$.
- (FII) If $(a_i)_{i \in I}$ is a family of cardinals strictly smaller than $c(U)$, and if $\operatorname{card}(I)$ is
  strictly smaller than $c(U)$, then $\sum_{i \in I} a_i < c(U)$.

Cardinals which possess properties (FI) and (FII) are called strongly inaccessible cardinals. The cardinal $0$ and the
countably infinite cardinal are strongly inaccessible.

Axiom (UA) implies:

$(\mathrm{UA}')$ Every cardinal is strictly bounded above by a strongly inaccessible cardinal.

Conversely, one can show that the non-contradiction of $(\mathrm{UA}')$ implies the non-contradiction of (UA), and that
the non-contradiction of these axioms entails that of axiom (UB).

[PDF p. 20]

Call a set $E$ artinian if there is no infinite family $(x_n)_{n \in \mathbf{N}}$ such that $x_{n+1} \in x_n \in E$. One
can then show that there is a one-to-one correspondence between strongly inaccessible cardinals and artinian universes:
to every strongly inaccessible cardinal $c$ one associates the unique artinian universe $U$ such that
$\operatorname{card}(U)=c$.

Let $c<c'$ be two strongly inaccessible cardinals. Then $U_c \in U_{c'}$. In particular, the artinian universes of
cardinals smaller than a given cardinal form a well-ordered set for the membership relation.

Axiom $(\mathrm{UA}')$ is equivalent to the axiom:

$(\mathrm{UA}'')$ Every artinian set is an element of an artinian universe.

Note that all usual sets, such as $\mathbf{Z}$, $\mathbf{Q}$, and so on, are artinian sets.

## 1. $U$-Categories. Presheaves of Sets

**1.0.** In the sequel of the Seminar, and unless expressly stated otherwise, the universes considered will contain an
element of infinite cardinality. Let $U$ be a universe. A set is said to be $U$-small, or simply small when this causes
no confusion, if it is isomorphic to an element of $U$. We also use the terminology: small group, small ring, small
category, and so on. We shall often suppose, without explicit mention, that the schemes, topological spaces, and index
sets with which we work are elements of $U$,

[PDF p. 21]

or at least have cardinality in $U$. However, many categories with which we shall work will not be elements of $U$.

**Definition 1.1.** Let $U$ be a universe and let $C$ be a category. We say that $C$ is a $U$-category if, for every
pair $(x,y)$ of objects of $C$, the set $\operatorname{Hom}_C(x,y)$ is $U$-small.

**1.1.1.** Let $C$ and $D$ be two categories, and let $\operatorname{Fonct}(C,D)$ be the category of functors from $C$
to $D$. The following assertions are checked immediately:

a) If $C$ and $D$ are elements of a universe $U$, respectively $U$-small, then the category $\operatorname{Fonct}(C,D)$
is an element of $U$, respectively is $U$-small.

b) If $C$ is $U$-small and if $D$ is a $U$-category, then $\operatorname{Fonct}(C,D)$ is a $U$-category.

**Remark 1.1.2.** Let $D$ be a category having the following properties:

- (C1) The set $\operatorname{ob}(D)$ is contained in the universe $U$.
- (C2) For every pair $(x,y)$ of objects of $D$, the set $\operatorname{Hom}_D(x,y)$ is an element of $U$.

The usual categories constructed from a universe $U$ have these two properties: $U\text{-}\mathbf{Ens}$,
$U\text{-}\mathbf{Ab}$, and so on. Let $C$ be a category belonging to $U$. Then the category $\operatorname{Fonct}(C,D)$
does not in general have properties (C1) and (C2). For example the category
$\operatorname{Fonct}(C,U\text{-}\mathbf{Ens})$ has neither property (C1) nor property (C2). This justifies the adopted
definition of $U$-category, in preference to the more restrictive notion given by conditions (C1) and (C2).

[PDF p. 22]

**Definition 1.2.** Let $C$ be a category. The category of presheaves of sets on $C$ relative to the universe $U$, or
simply the category of presheaves on $C$ when no confusion can result, is the category of contravariant functors on $C$
with values in the category of $U$-sets.

We denote by $\widehat{C}$ the category of presheaves of sets on $C$ relative to the universe $U$. The objects of
$\widehat{C}$ are called $U$-presheaves, or more simply presheaves, on $C$. When $C$ is $U$-small, the category
$\widehat{C}$ is a $U$-category. When $C$ is a $U$-category, $\widehat{C}$ is not necessarily a $U$-category.

**Construction-Definition 1.3.** Let $x$ be an object of a $U$-category $C$. The $U$-functor represented by $x$ is the
functor $h_U(x) : C^\circ \to U\text{-}\mathbf{Ens}$ whose construction follows (*). Let $y$ be an object of $C$.

a) If $\operatorname{Hom}_C(y,x)$ is an element of $U$, then $h_U(x)(y)=\operatorname{Hom}_C(y,x)$.

b) Suppose that $\operatorname{Hom}_C(y,x)$ is not an element of $U$. Let $R(Z,x,y)$ be the relation: "$Z$ is the target
of an isomorphism $\operatorname{Hom}_C(y,x) \to Z$." We then put

$$ h_U(x)(y)=\tau Z\,R(Z,x,y). $$

By axiom (UB), $h_U(x)(y)$ is an element of $U$. Let $R'(u,x,y)$ be the relation: "$u$ is a bijection
$\operatorname{Hom}_C(y,x) \to h_U(x)(y)$." We then put

$$ \alpha(y,x)=\tau u\,R'(u,x,y). $$

(*) $C^\circ$ will always denote the category opposite to $C$.

[PDF p. 23]

Observe that in cases (a) and (b) one has a canonical isomorphism

$$ \alpha(y,x) : \operatorname{Hom}_C(y,x) \to h_U(x)(y). $$

In case (a), $\alpha(y,x)$ is the identity.

Let $u : y \to y'$ be an arrow of $C$. By composition of morphisms, the morphism $u$ defines a map

$$ \operatorname{Hom}_C(y',x) \to \operatorname{Hom}_C(y,x). $$

We put

$$ h_U(x)(u)=\alpha(y,x) \circ \operatorname{Hom}_C(u,x) \circ \alpha(y',x)^{-1}. $$

It is checked immediately that $h_U(x)$, so defined, is a functor $C^\circ \to U\text{-}\mathbf{Ens}$.

**1.3.1.** Similarly, using the isomorphisms $\alpha$, for every morphism $\gamma : x \to x'$ one defines a morphism of
functors

$$ h_U(\gamma) : h_U(x) \to h_U(x'), $$

and it is checked immediately that this defines a functor

$$ h_U : C \to \widehat{C}. $$

**1.3.2.** Now let $V$ be a universe such that $U \in V$. Then there is a canonical fully faithful functor

$$ U\text{-}\mathbf{Ens} \to V\text{-}\mathbf{Ens}, $$

hence a fully faithful functor

[PDF p. 24]

$$ \widehat{C}_U \to \widehat{C}_V, $$

and the diagram

```text
C -> C^_U
|    |
v    v
C -> C^_V
```

is commutative up to canonical isomorphism. When $C$ is an element of $U$, this canonical isomorphism is the identity.

**1.3.3.** In practice, the universe $U$ is fixed once and for all and is not mentioned. We then use the notation
$\widehat{C}$ for the category of $U$-presheaves of sets, and

$$ h : C \to \widehat{C}. $$

For every object $x$ of $C$, the presheaf $h(x)$ is called the presheaf represented by $x$, and we shall always identify
the value at $y \in \operatorname{ob}(C)$ of the presheaf $h(x)$ with $\operatorname{Hom}_C(y,x)$.

**Proposition 1.4.** Let $C$ be a $U$-category, let $F$ be a presheaf on $C$, and let $X$ be an object of $C$. There is
an isomorphism, functorial in $X$ and in $F$:

$$ \operatorname{Hom}_{\widehat{C}}(h(X),F) \simeq F(X). $$

When $F$ is of the form $h(Y)$, this isomorphism is precisely the map

$$ \operatorname{Hom}_C(X,Y) \to \operatorname{Hom}_{\widehat{C}}(h(X),h(Y)). $$

In particular the functor $h$ is fully faithful.

**1.4.1.** This proposition justifies the usual abuses of language identifying an object of $C$ and the corresponding
contravariant functor.

[PDF p. 25]

A presheaf isomorphic to an object in the image of $h$, or, using the abuse of language just mentioned, isomorphic to an
object of $C$, is called a representable presheaf.

**1.4.2.** Let $V$ be a universe containing a universe $U$. The category of $U$-presheaves is a full subcategory of the
category of $V$-presheaves. Consequently a $U$-presheaf is representable if and only if its image in the category of
$V$-presheaves is a representable $V$-presheaf.

## 2. Projective and Inductive Limits

Let $C$ be a $U$-category and let $I$ be a small category. Denote by $\operatorname{Fonct}(I,C)$ the category of
functors from $I$ to $C$. The category $\operatorname{Fonct}(I,C)$ is a $U$-category.

To every object $X$ of $C$, associate the subcategory $X$ of $C$ having as its only object the object $X$ and as its
only arrow the identity of $X$. Let $i_X : X \to C$ denote the inclusion functor. There is one and only one functor
$e_X : I \to X$, and we shall denote by

$$ k_X : I \to C $$

the functor $i_X \circ e_X$. We shall say that $k_X$ is the constant functor with value $X$. The correspondence
$X \mapsto k_X$ is visibly functorial in $X$, which allows us to define, for every functor $G : I \to C$, the presheaf

$$ X \mapsto \operatorname{Hom}_{\operatorname{Fonct}(I,C)}(k_X,G). $$

**Definition 2.1.** The **projective limit** of $G$, denoted $\varprojlim_I G$, is the presheaf

$$ X \mapsto \operatorname{Hom}_{\operatorname{Fonct}(I,C)}(k_X,G). $$

If this presheaf is representable, we again denote by $\varprojlim_I G$

[PDF p. 26]

an object of $C$ which represents it. The object $\varprojlim_I G$ is therefore defined only up to isomorphism. When no
confusion can result, we use the abbreviated notation $\varprojlim G$.

For variable $G$, $\varprojlim_I G$ is a functor from the category $\operatorname{Fonct}(I,C)$ with values in
$\widehat{C}$.

**2.1.1.** Similarly, by symmetry, reversing the direction of the arrows in $C$, one defines the **inductive limit** of
a functor: it is a covariant functor on $C$, with values in the category of $U$-sets. We shall use the notations
$\varinjlim_I G$ or $\varinjlim G$.

We note that products, fiber products, and kernels are projective limits. Similarly, sums, amalgamated sums, and
cokernels are inductive limits.

**Definition 2.2.** Let $I$ and $C$ be two categories, and let $G : I \to C$ be a functor. We say that the projective
limit of $G$ is **representable** if there exists a universe $U$ such that:

1. The category $I$ is $U$-small.
2. The category $C$ is a $U$-category.
3. The presheaf $\varprojlim_I G$, with values in the category of $U$-sets, is representable.

It follows from no. 1 that the object $\varprojlim_I G$ representing the presheaf $\varprojlim_I G$ does not depend, up
to isomorphism, on the universe $U$. Note also that there exists a smallest universe $U'$ having properties 1 and 2, and
that the presheaf $\varprojlim_I G$ necessarily has values in the category of $U'$-sets.

[PDF p. 27]

**2.2.1.** Let $I$ and $C$ be two categories. We say that the $I$-projective limits in $C$ are representable if, for
every functor $G : I \to C$, the projective limit of $G$ is representable.

Finally, let $C$ be a category and let $U$ be a universe. We say that the $U$-projective limits in $C$ are representable
if, for every $U$-small category $I$ and every functor $G : I \to C$, the projective limit of $G$ is representable.

**Proposition 2.3.** Let $C$ be a category and let $U$ be a nonempty universe. The following assertions are equivalent:

1. The $U$-projective limits in $C$ are representable.
2. Products indexed by a small set are representable, and kernels of pairs of arrows are representable.
3. Products indexed by a small set are representable, and fiber products are representable.

**Proof.** It suffices to observe that there is an isomorphism functorial in $G$,

$$
\varprojlim_I G \simeq
\operatorname{Ker}\left(
\prod_{i \in \operatorname{ob}(I)} G(i)
\rightrightarrows
\prod_{u \in \operatorname{Fl}(I)} G(\operatorname{target}(u))
\right),
$$

the pair of arrows being defined by the morphisms

$$
\prod_{i \in \operatorname{ob}(I)} G(i)
\xrightarrow{\operatorname{pr}_{\operatorname{target}(u)}}
G(\operatorname{target}(u)),
$$

$$
\prod_{i \in \operatorname{ob}(I)} G(i)
\xrightarrow{\operatorname{pr}_{\operatorname{source}(u)}}
G(\operatorname{source}(u))
\xrightarrow{G(u)}
G(\operatorname{target}(u)).
$$

Moreover it is clear that $\operatorname{Ker}(X \rightrightarrows Y)=X \times_{Y \times Y} Y$, the two morphisms from
$X$ to $Y \times Y$ being $\operatorname{id}_X \times u$ and $\operatorname{id}_X \times v$.

**2.3.1.** There are of course analogous definitions and assertions for inductive limits; we shall not spell them out.
Similarly for finite projective and inductive limits, that is, those relative to a finite category $I$.

[PDF p. 28]

**Corollary 2.3.2.** Let $U\text{-}\mathbf{Ens}$ denote the category of $U$-sets and $U\text{-}\mathbf{Ab}$ the category
of abelian groups in $U\text{-}\mathbf{Ens}$. The $U$-projective and inductive limits in $U\text{-}\mathbf{Ens}$ and in
$U\text{-}\mathbf{Ab}$ are representable.

**Proposition 2.3.3.** Let $I$ be a small category, let $F : I \to U\text{-}\mathbf{Ens}$ be a functor, and let
$G \subset \operatorname{ob}(I)$ be a small set of objects of $I$ such that, for every object $X$ of $I$, there exists
an object $Y \in G$ and a morphism $Y \to X$ (resp. $X \to Y$). Then $\varprojlim_I F$ (resp. $\varinjlim_I F$) is
representable and one has

$$
\operatorname{card}(\varprojlim_I F) \leq
\operatorname{card}\left(\prod_{Y \in G} F(Y)\right),
$$

respectively

$$
\operatorname{card}(\varinjlim_I F) \leq
\sum_{Y \in G} \operatorname{card}(F(Y)).
$$

**Proof.** It is checked immediately that $\varprojlim_I F$ (resp. $\varinjlim_I F$) is isomorphic to a subobject (resp.
a quotient) of $\prod_{Y \in G} F(Y)$ (resp. of $\coprod_{Y \in G} F(Y)$), whence the proposition.

**Definition 2.4.1.** Let $C$ be a category in which finite projective (resp. inductive) limits are representable, and
let $u : C \to C'$ be a functor. We say that $u$ is **left exact** (resp. **right exact**) if it commutes with finite
projective (resp. inductive) limits. A functor which is both left and right exact is called an **exact** functor.

**2.4.2.** It follows from 2.3 that, for a functor to be left exact, it is necessary and sufficient that it transform
the final object, that is, the empty product, into the final object, the product of two objects into the product of
their two image objects, and the kernel of pairs of two arrows into the kernel of the image pairs. Equivalently, it is
necessary and sufficient that it transform the final object into the final object and fiber products into fiber
products, assuming that in $C$ finite limits are representable.

[PDF p. 29]

**2.5.0.** Let $I$, $J$, and $C$ be three categories, and let $G : I \times J \to C$ be a functor, that is, a functor
from $I$ with values in the category of functors from $J$ to $C$. Suppose that the projective limits of the functors

$$ G_i : J \to C,\qquad j \mapsto G(i,j) \qquad (i \in \operatorname{ob} I) $$

are representable, and that the functor

$$ i \mapsto \varprojlim_J G_i $$

admits a representable projective limit. It is clear that the functor $G$ then admits a representable projective limit
and that one has a canonical isomorphism

$$ \varprojlim_{I \times J} G \simeq \varprojlim_I \varprojlim_J G_i. $$

One deduces a canonical isomorphism

$$ \varprojlim_I \varprojlim_J G_i \simeq \varprojlim_J \varprojlim_I G^j. $$

In the sequel, more briefly, we shall say that projective limits commute with projective limits. Similarly, inductive
limits commute with inductive limits. But it is not true in general that inductive limits commute with projective
limits.

**Definition 2.5.** Let $C$ be a category with representable fiber products, let $I$ be a category, let $G : I \to C$ be
a functor, let $g : G \to X$ be a morphism from $G$ to an object of $C$, that is, a morphism from $G$ to the constant
functor associated with $X$, and let $m : Y \to X$ be a morphism of $C$.

[PDF p. 30]

Let $G \times_X Y : I \to C$ be the functor obtained by base change. We say that the inductive limit of $G$ is
**universal** if, for every object $X$, every morphism $g : G \to X$, and every morphism $m : Y \to X$:

1. the inductive limit of the functor $G \times_X Y$ is representable;
2. the canonical morphism

   $$ \varinjlim_I(G \times_X Y) \to (\varinjlim_I G) \times_X Y $$

   is an isomorphism.

**Proposition 2.6.** Let $U$ be a universe. Inductive limits in $U\text{-}\mathbf{Ens}$ which are representable, in
particular $U$-inductive limits (2.2.1) in $U\text{-}\mathbf{Ens}$, are universal.

We shall also use another commutation result between projective and inductive limits, which we now present.

**Definition 2.7.** A category $I$ is **pseudo-filtering** when it has the following properties:

**PS 1)** Every finite diagram of two objects can be completed by an object receiving them both; in other words, for two
objects $i,j$, there exists an object $k$ and morphisms $i \to k$, $j \to k$.

**PS 2)** For every pair of parallel arrows

$$ u,v : i \rightrightarrows j, $$

there exists an arrow $w : j \to k$ such that

[PDF p. 31]

$$ w u = w v. $$

A category $I$ is called **filtering** if it is pseudo-filtering, nonempty, and connected, that is, if any two objects
of $I$ can be joined by a sequence of arrows, with no condition on the direction of the arrows. In the presence of PS 2,
this also means that $I$ is nonempty and that, for two objects $a,b$ of $I$, there always exists an object $c$ of $I$
and arrows $a \to c$, $b \to c$. One also says that a category $I$ is **cofiltering** if $I^\circ$ is filtering.

**Example 2.7.1.** If, in $I$, amalgamated sums (resp. sums of two objects) and cokernels of double arrows are
representable, then $I$ is pseudo-filtering (resp. filtering).

**Proposition 2.8.** Let $U$ be a universe. Filtering $U$-inductive limits in $U\text{-}\mathbf{Ens}$ commute with
finite projective limits.

One is immediately reduced to proving that filtering $U$-limits commute with fiber products. The proof is left to the
reader. One may use the description of the limit given by the following lemma.

**Lemma 2.8.1.** Let $I$ be a small filtering category and let $i \mapsto X_i$ be a functor from $I$ to
$U\text{-}\mathbf{Ens}$. On the sum set $\coprod_{i \in \operatorname{ob} I} X_i$, let $R$ be the following relation:

**(R)** Two elements $x_i \in X_i$ and $x_j \in X_j$ are related if there exists an object $k \in \operatorname{ob} I$
and two morphisms $u : i \to k$, $v : j \to k$ such that the images of $x_i$ and $x_j$ by the transition maps $u$ and
$v$, respectively, are equal.

[PDF p. 32]

Then:

1. $R$ is an equivalence relation.
2. The quotient $(\coprod_{i \in \operatorname{ob} I} X_i)/R$ is canonically isomorphic to $\varinjlim_I X_i$.
3. Two equivalent elements are respectively equivalent to two elements of a same $X_i$.
4. For every $i \in \operatorname{ob} I$, two elements $\alpha$ and $\beta$ of $X_i$ are equivalent under $R$ if and
   only if there exists a morphism $u : i \to j$ such that $u(\alpha)=u(\beta)$.

Assertion 1 follows from PS 1 (2.7). To prove 2, one checks that $(\coprod X_i)/R$ has the universal property of the
inductive limit; only PS 1 is used. Assertion 3 follows from the fact that $I$ is connected. Assertion 4 follows from PS
2.

**Corollary 2.9.** Let $Y$ be a species of algebraic structure "defined by finite projective limits." The reader is
asked to give a mathematical meaning to this phrase; let us merely note that structures of groups, abelian groups,
rings, modules, and so on are such structures. Denote by $U\text{-}Y$ the category of $Y$-objects in
$U\text{-}\mathbf{Ens}$. The functor which associates to each object of $U\text{-}Y$ its underlying set commutes with
filtering $U$-limits. Consequently, filtering $U$-limits in $U\text{-}Y$ commute with finite projective limits.

**Corollary 2.10.** Pseudo-filtering $U$-limits in $U\text{-}\mathbf{Ab}$ commute with finite projective limits.

One reduces to filtering limits by decomposing the index category into connected components.

**Proposition 2.11.** Let $C$ and $C'$ be two $U$-categories, and let $u : C \to C'$, $v : C' \to C$ be two functors,
with $u$ left adjoint to $v$. Recall that this means that there is an isomorphism of bifunctors with values in
$U\text{-}\mathbf{Ens}$

$$ \operatorname{Hom}_{C'}(u(X),X') \simeq \operatorname{Hom}_C(X,v(X')). $$

The functor $u$ commutes with representable inductive limits; the functor $v$ commutes with representable projective
limits. This assertion means that, for every category $I$ and every functor $G : I \to C'$ such that the projective
limit of $G$ is representable, the functor $vG$ admits a representable projective limit and one has a canonical
isomorphism

$$ v(\varprojlim_I G) \simeq \varprojlim_I(vG). $$

The reader will spell out for himself the assertion concerning the functor $u$.

**Proposition 2.12.** Let $I$ and $C$ be two categories, and let $V$ be a universe. Assume that the $V$-projective
limits in $C$ are representable and that there exists in $I$ a family of objects $(i_\alpha)_{\alpha \in A}$, with
$A \in V$, such that:

1. the products $i_\alpha \times i_\beta$ are representable for every pair $(\alpha,\beta) \in A \times A$;
2. every object of $I$ maps to at least one of the $i_\alpha$.

Then, for every contravariant functor $F : I^\circ \to C$, the projective limit of $F$ exists and there is an
isomorphism functorial in $F$:

[PDF p. 34]

$$
\varprojlim F \simeq
\operatorname{Ker}\left(
\prod_{\alpha \in A} F(i_\alpha)
\rightrightarrows
\prod_{(\alpha,\beta) \in A \times A} F(i_\alpha \times i_\beta)
\right),
$$

the two arrows being defined by the projections of the products $i_\alpha \times i_\beta$ onto the factors.

## 3. Exactness Properties of the Category of Presheaves

Let $C$ be a $U$-category and let $\widehat{C}$ be the category of presheaves on $C$. The exactness properties of
$\widehat{C}$ all follow from the following proposition.

**Proposition 3.1.** The $U$-projective and inductive limits in $\widehat{C}$ are representable. For every object $X$ of
$C$, the functor on $\widehat{C}$

$$ F \mapsto F(X) $$

commutes with inductive and projective limits. In other words, inductive and projective limits in $\widehat{C}$ are
computed argument by argument.

Let us state a few corollaries.

**Corollary 3.2.** Let $Y$ be an algebraic structure defined by finite projective limits. The category of contravariant
functors with values in $U\text{-}Y$ is equivalent to the category of $Y$-objects of $\widehat{C}$.

**Corollary 3.3.** A morphism of $\widehat{C}$ which is both a monomorphism and an epimorphism is an isomorphism. A
morphism of $\widehat{C}$ factors uniquely as an epimorphism followed by a monomorphism. Inductive limits in
$\widehat{C}$ which are representable are universal. Filtering $U$-inductive limits in $\widehat{C}$ commute with finite
projective limits. The canonical functor

$$ C \to \widehat{C} $$

commutes with representable projective limits.

[PDF p. 35]

More generally, one can say that the category $\widehat{C}$ inherits all the properties of the category of $U$-sets
which involve inductive and projective limits.

**3.4.0.** Let $F$ be an object of $\widehat{C}$. We denote by $C/F$ the following category. The objects of $C/F$ are
pairs formed by an object $X$ of $C$ and a morphism $u : X \to F$. Let $(X,u)$ and $(Y,v)$ be two objects. A morphism
from $(X,u)$ to $(Y,v)$ is a morphism $g : X \to Y$ such that the diagram

```text
X --g--> Y
 \       |
  u      v
   \     |
      F
```

is commutative.

**Proposition 3.4.** With the notation of 3.4.0, the source functor

$$ C/F \to \widehat{C} $$

admits a representable inductive limit in $\widehat{C}$. The canonical morphism

$$ \varinjlim_{C/F} \operatorname{source}(-) \to F $$

is an isomorphism.

**Corollary 3.5.** Let $F$ and $H$ be two objects of $\widehat{C}$. There is a canonical isomorphism

$$ \operatorname{Hom}(F,H) \simeq \varprojlim_{(X,u) \in C/F} H(X). $$

**Proof.** The corollary follows immediately from 3.4 and 1.2.

[PDF p. 36]

**Proposition 3.6.** Let $C$ be a $U$-category, let $V$ be a universe containing $U$, and let

$$ i : \widehat{C}_U \to \widehat{C}_V $$

be the natural injection functor of the corresponding categories of presheaves (1.3). The functor $i$ commutes with
inductive and projective limits. Moreover, for every object $F$ of $\widehat{C}_U$, every subobject of $i(F)$ is
isomorphic to the image under $i$ of a unique subobject of $F$; thus one obtains a bijection between the set of
subobjects of $F$ and the set of subobjects of $i(F)$.

## 4. Sieves

**Definition 4.1.** Let $C$ be a category. A **sieve** of the category $C$ is a full subcategory $D$ of $C$ having the
following property: every object of $C$ for which there exists a morphism from this object to an object of $D$ lies in
$D$. Let $X$ be an object of $C$; by abuse of language, the **sieves of $X$** are the sieves of the category $C/X$.

Let $U$ be a universe such that $C$ is a $U$-category. Let $\widehat{C}$ be the corresponding category of presheaves. To
every sieve of $X$, one associates a subobject of $X$ in $\widehat{C}$ as follows: to every object $Y$ of $C$, one
assigns the set of morphisms $f : Y \to X$ such that the object $(Y,f)$ belongs to the sieve.

**Proposition 4.2.** The map defined above establishes a bijection between the set of sieves of $X$ and the set of
subobjects of $X$ in $\widehat{C}$.

**Proof.** We show only that it is the inverse map. To every subfunctor $R$ of $X$, one associates the category $C/R$ of
objects of $C$ over $R$ (3.4). It is checked immediately that $C/R$ is a sieve of $X$.

[PDF p. 37]

**Remark 4.2.1.** Similarly, one sees that the sieves of $C$ are in canonical one-to-one correspondence with the set of
subfunctors of the final functor on $C$, the final object of $\widehat{C}$.

**4.3.** Let $C$ be a $U$-category. By abuse of language, we shall also call sieves of $X$ the subobjects of $X$ in the
category $\widehat{C}$. This abuse of language makes it possible, for every presheaf $F$ and every sieve $R$ of $X$, to
define $\operatorname{Hom}(R,F)$ as the set of morphisms from the functor $R$ to $F$. Moreover, there is a canonical
isomorphism, functorial in $F$,

$$ \operatorname{Hom}(R,F) \simeq \varprojlim_{(Y \to X) \in C/R} F(Y), $$

which gives a direct definition. Similarly, Proposition 4.2 allows us to transpose to sieves the usual operations on
functors. Let us cite:

**4.3.1. Base change.** Let $R$ be a sieve of $X$ and let $f : Y \to X$ be a morphism of objects of $C$. The fiber
product $R \times_X Y$ is a sieve of $Y$, called the sieve deduced from $R$ by base change. The corresponding
subcategory of $C/Y$ is the inverse image of the subcategory of $C/X$ defined by $R$, under the canonical functor
$C/Y \to C/X$ defined by $f$.

**4.3.2. Order relation; intersection, union.** The inclusion relation on subfunctors of $X$ is an order relation. One
can define the union and the intersection of a family of sieves indexed by an arbitrary set as the least upper bound and
the greatest lower bound of the family of corresponding subpresheaves.

[PDF p. 38]

**4.3.3. Image, generated sieve.** Let $(F_\alpha)_{\alpha \in A}$ be a family of presheaves and, for each
$\alpha \in A$, let $f_\alpha : F_\alpha \to X$ be a morphism, where $X$ is an object of $C$. The image of this family
of morphisms is the union of the images of the $f_\alpha$. The image of this family is therefore a sieve of $X$. In
particular, if all the $F_\alpha$ are objects of $C$, the image sieve will be called the sieve generated by the
morphisms $f_\alpha$. The category $C/R$ is the full subcategory of $C/X$ formed by the objects $X' \to X$ over $X$ such
that there exists an $X$-morphism from $X'$ to one of the $F_\alpha$.

As an exercise, the reader may translate the relations and operations defined here on subfunctors into terms of the
categories $C/R$. He will then find that these relations and operations do not depend on the universe $U$ for which $C$
is a $U$-category, and hence that they are defined for every category without being obliged to specify the universe to
which the sets of morphisms belong; this could in any case be foreseen a priori from 3.6.

## 5. Functoriality of Categories of Presheaves

**5.0.** Let $C$, $C'$, and $D$ be three categories and let $u : C \to C'$ be a functor. We shall denote by $u^*$ the
functor

$$
u^* : \operatorname{Hom}((C')^\circ,D) \to \operatorname{Hom}(C^\circ,D),
\qquad G \mapsto G \circ u,
$$

obtained by composing with the functor $u$. The functor $u^*$ commutes with inductive and projective limits.

[PDF p. 39]

**Proposition 5.1.** Suppose that $C$ is small and that, in $D$, the $U$-inductive (resp. projective) limits are
representable. The functor $u^*$ admits a left adjoint $u_!$ (resp. a right adjoint $u_*$). Thus one has isomorphisms

$$ \operatorname{Hom}(u_!F,G) \simeq \operatorname{Hom}(F,u^*G), $$

and, respectively,

$$ \operatorname{Hom}(u^*G,F) \simeq \operatorname{Hom}(G,u_*F). $$

**Proof.** We shall indicate only the proof of the existence of the left adjoint functor. The "respectively" part of the
proposition then follows formally from the isomorphisms

$$
\operatorname{Hom}(C^\circ,D)
\simeq
\operatorname{Hom}(C,D^\circ)^\circ
\simeq
\operatorname{Hom}((C^\circ)^\circ,D^\circ)^\circ.
$$

Let $Y$ be an object of $C'$. Denote by $I_Y$ the following category. The objects of $I_Y$ are the pairs $(X,m)$, where
$X$ is an object of $C$ and $m : Y \to u(X)$ is a morphism. A morphism from $(X,m)$ to $(X',m')$ is a morphism
$s : X \to X'$ such that $m'=u(s)m$. Composition of morphisms is defined in the evident way.

Let $f : Y \to Y'$ be a morphism of $C'$. By composition, the morphism $f$ defines a functor $I_{Y'} \to I_Y$. Moreover
there is a functor $\operatorname{Pr}_Y : I_Y \to C$ which associates to the object $(X,m)$ the object $X$. The
corresponding diagram is commutative.

[PDF p. 40]

Now let $F$ be a presheaf on $C$ and put

$$ (u_!F)(Y)=\varinjlim_{I_Y} F \circ \operatorname{Pr}_Y. \tag{5.1.2} $$

The commutativity of the preceding diagram and the functoriality of the inductive limit make $u_!F$ a presheaf on $C'$.
Let us show that the functor $u_!$ is left adjoint to the functor $u^*$. For this, it suffices to show that, for every
presheaf $G$ on $C'$, there is a functorial isomorphism

$$ \operatorname{Hom}(u_!F,G) \simeq \operatorname{Hom}(F,u^*G). $$

Let $\xi : u_!F \to G$. For every object $X$ of $C$, the pair $(X,\operatorname{id}_{u(X)})$ is an object of $I_{u(X)}$
and, by definition of the inductive limit, one has a canonical morphism

$$ F(X) \to (u_!F)(u(X)). $$

One deduces, for every object $X$ of $C$, a morphism

$$ F(X) \to G(u(X)), $$

visibly functorial in $X$, hence a morphism $F \to u^*G$.

Conversely, let $\eta : F \to u^*G$. For every object $Y$ of $C'$, the morphisms

$$ F(X) \to G(u(X)) \to G(Y), $$

associated with the objects $(X,m : Y \to u(X))$ of $I_Y$, define a morphism from the functor
$F \circ \operatorname{Pr}_Y$ to the constant functor with value $G(Y)$. Thus one obtains a morphism

$$ (u_!F)(Y) \to G(Y), $$

functorial in $Y$, and consequently a morphism $u_!F \to G$.

[PDF p. 41]

The reader will check that the two maps thus defined are inverse to one another, thereby completing the proof.

**Proposition 5.2.** Suppose that, in $D$, the $U$-inductive limits are representable, finite projective limits are
representable, and filtering $U$-inductive limits commute with finite projective limits. Suppose moreover that, in $C$,
finite projective limits are representable and that the functor $u$ is left exact (2.3.2). Then finite projective limits
are representable in $\operatorname{Hom}(C^\circ,D)$ and in $\operatorname{Hom}((C')^\circ,D)$, and the functor $u_!$ is
left exact.

**Proof.** The first assertion is trivial. Let us prove the second. From the proof of 5.1, for every presheaf $F$ on $C$
and every object $Y$ of $C'$, one has

$$ (u_!F)(Y)=\varinjlim_{I_Y} F \circ \operatorname{Pr}_Y. $$

It therefore suffices to show that the category $I_Y$ satisfies axioms (PS 1) and (PS 2) (2.7) and that this category is
connected. The verification is left to the reader.

**5.3.** Specializing these results to the case where $D$ is the category of $U$-sets, one obtains a sequence of three
functors

$$ u_!,\quad u^*,\quad u_*, $$

which is a "sequence of adjoint functors," in the sense that, for two consecutive functors in the sequence, the one on
the right is right adjoint to the other.

[PDF p. 42]

Their essential properties are summarized in the following proposition.

**Proposition 5.4.** Let $C$ be a small category, let $C'$ be a $U$-category, and let $u : C \to C'$ be a functor.

1. The functor $u^* : \widehat{C'} \to \widehat{C}$ commutes with inductive and projective limits.
2. The functor $u_* : \widehat{C} \to \widehat{C'}$ commutes with projective limits. For every presheaf $F$ on $C$ and
   every object $Y$ of $C'$, one has

   $$ (u_*F)(Y) \simeq \operatorname{Hom}_{\widehat{C}}(u^*Y,F). $$

3. The functor $u_! : \widehat{C} \to \widehat{C'}$ commutes with inductive limits. The functor $u_!$ is defined only up
   to isomorphism, but it can always be chosen so that the diagram

   ```text
   C  --u-->  C'
   |         |
   h         h'
   v         v
   C^ --u_!--> (C')^
   ```

   is commutative, where $h$ and $h'$ are the canonical inclusion functors. For every presheaf $F$ on $C$, one has

   $$ u_!F \simeq \varinjlim_{(X \to F) \in C/F} h'(u(X)). $$

4. If finite projective limits are representable in $C$ and if $u$ is left exact (2.3.2), the functor $u_!$ is left
   exact.

**Proof.** Assertion (1) is trivial. Assertion (2) follows from the fact that $u_*$ is a right adjoint functor, by
(2.11) and (I.4). The same holds for assertion (3), but one applies (3.4) in addition. Finally, assertion (4) is exactly
5.2, which can be applied thanks to (2.7).

[PDF p. 43]

**Proposition 5.5.** Let $C$ and $C'$ be two small categories and

```text
C  --u-->  C'
C' --v-->  C
```

a pair of functors, where $v$ is left adjoint to $u$. Then there are isomorphisms, compatible with the adjunction
isomorphisms:

$$ v^* \simeq u_!, \qquad v_* \simeq u^*. $$

**Proof.** It suffices to exhibit an isomorphism $v^* \simeq u_!$; the other isomorphism follows from it by adjunction.
Let $F$ be a presheaf on $C$ and let $Y$ be an object of $C'$. Then

$$ v^*F(Y) \simeq \operatorname{Hom}(v(Y),F). $$

Then, using (3.4),

$$ \operatorname{Hom}(v(Y),F) \simeq \varinjlim_{C/F} \operatorname{Hom}(v(Y),-). $$

But $v$ is left adjoint to $u$, and therefore

$$
\varinjlim_{C/F} \operatorname{Hom}(v(Y),-)
\simeq
\varinjlim_{C/F} \operatorname{Hom}(Y,u(-)).
$$

Using 5.4 3), it follows that

$$
\varinjlim_{C/F} \operatorname{Hom}(Y,u(-))
\simeq
\operatorname{Hom}(Y,u_!F)
\simeq
u_!F(Y).
$$

Thus, for every object $Y$ of $C'$, we have determined an isomorphism $v^*F(Y) \simeq u_!F(Y)$, visibly functorial in
$Y$ and in $F$.

**Corollary 5.5.1.** Let $u : C \to C'$ be a functor which admits a left adjoint. The functor
$u_! : \widehat{C} \to \widehat{C'}$ commutes with projective limits; recall that it commutes with inductive limits by
(5.4, 3).

[PDF p. 44]

**Remark 5.5.2.** Thus one finds a "sequence of four adjoint functors" (cf. 5.3),

$$ v_!,\quad v^*=u_!,\quad v_*=u^*,\quad u_*, $$

of which the first three (resp. last three) therefore commute with inductive (resp. projective) limits.

**Proposition 5.6.** The hypotheses are those of 5.4. The following conditions are equivalent:

1. The functor $u$ is fully faithful.
2. The functor $u_!$ is fully faithful.
3. The adjunction morphism $\operatorname{id} \to u^*u_!$ is an isomorphism.
4. The functor $u_*$ is fully faithful.
5. The adjunction morphism $u^*u_* \to \operatorname{id}$ is an isomorphism.

**Proof.** It is clear that (2) is equivalent to (3) and that (4) is equivalent to (5), by the general properties of
adjoint functors, and that (2) implies (1) by 5.4 3). Let us show that (1) implies (3). The functors
$\operatorname{id}$, $u^*$, and $u_!$ commute with inductive limits. By (3.4), it therefore suffices to prove that
$H \to u^*u_!H$ is an isomorphism when $H$ is representable, which is evident.

Let us show that (3) is equivalent to (5). For every object $H$ of $\widehat{C}$ (resp. $K$ of $\widehat{C'}$), denote
by $\varphi(H) : H \to u^*u_!H$ (resp. by $\psi(K) : u^*u_*K \to K$) the adjunction morphism. Then one has a commutative
diagram:

```text
Hom_{C^}(H, u*u_*K) --Hom(H, psi(K))--> Hom_{C^}(H, K)
        |                                      ^
        ~=                                     |
        v                                      Hom(phi(H), K)
Hom_{(C')^}(u_!H, u_*K) -------------> Hom_{C^}(u*u_!H, K).
```

It follows that $\varphi(H)$ is an isomorphism for every $H$ if and only if $\psi(K)$ is an isomorphism for every $K$.

[PDF p. 45]

**Remark 5.7.**

1. The equivalences $(2) \Longleftrightarrow (3)$ and $(4) \Longleftrightarrow (5)$ are general results on adjoint
   functors.
2. The explicit form of $u_!$ and $u_*$, given in the proof of 5.1, shows at once that, under the general hypotheses of
   5.1, if $u$ is fully faithful, then the adjunction morphism $\operatorname{id} \to u^*u_!$ (resp.
   $u^*u_* \to \operatorname{id}$) is an isomorphism, that is, $u_!$ (resp. $u_*$) is fully faithful.

**5.8.0.** Let $Y$ be a species of algebraic structure defined by finite projective limits, and let
$U\text{-}Y\text{-}\mathbf{Ens}$ be the category of $Y$-objects of $U\text{-}\mathbf{Ens}$. Denote by

$$ \operatorname{ens} : U\text{-}Y\text{-}\mathbf{Ens} \to U\text{-}\mathbf{Ens} $$

the "underlying set" functor. For simplicity, we suppose that the species of structure under consideration has a single
underlying set. Composition with $\operatorname{ens}$ provides a functor, denoted

$$
\operatorname{ens}^C :
\operatorname{Hom}(C^\circ,U\text{-}Y\text{-}\mathbf{Ens}) \to \widehat{C}.
$$

Since, in $\widehat{C}$, projective limits are computed argument by argument, the functor $\operatorname{ens}^C$ factors
through an equivalence

$$ \operatorname{Hom}(C^\circ,U\text{-}Y\text{-}\mathbf{Ens}) \simeq (\widehat{C})Y, \tag{5.8.1} $$

where $(\widehat{C})Y$ denotes the category of $Y$-objects of $\widehat{C}$, and then through a functor still denoted

$$ \operatorname{ens}^C : (\widehat{C})Y \to \widehat{C}, $$

called the "underlying presheaf of sets" functor.

[PDF p. 46]

**5.8.2.** Suppose that the functor $\operatorname{ens} : U\text{-}Y\text{-}\mathbf{Ens} \to U\text{-}\mathbf{Ens}$
admits a left adjoint

$$ \operatorname{Lib} : U\text{-}\mathbf{Ens} \to U\text{-}Y\text{-}\mathbf{Ens}. $$

In fact one can show that this condition is always satisfied. Composition with $\operatorname{Lib}$ provides a functor

$$ \operatorname{Lib}^C : \widehat{C} \to \operatorname{Hom}(C^\circ,U\text{-}Y\text{-}\mathbf{Ens}), $$

and, composing with the equivalence (5.8.1), a functor still denoted

$$ \operatorname{Lib}^C : \widehat{C} \to (\widehat{C})Y, $$

called the "presheaf of free $Y$-objects generated by" functor. The functor $\operatorname{Lib}^C$ is left adjoint to
the functor $\operatorname{ens}^C$.

**Proposition 5.8.3.** Let $Y$ be a species of algebraic structure defined by finite projective limits such that, in the
category of $Y$-objects of $U\text{-}\mathbf{Ens}$, the $U$-inductive limits are representable; let $C$ be a category
belonging to $U$, let $C'$ be a $U$-category, and let $u : C \to C'$ be a functor. Denote by $(\widehat{C})Y$ (resp.
$(\widehat{C'})Y$) the category of $Y$-objects of $\widehat{C}$ (resp. of $\widehat{C'}$), and by $u^*Y$ the functor on
$Y$-objects deduced from the functor $u^*$. It follows from 5.1 and the equivalence (5.8.1) that there exists a functor
left adjoint (resp. right adjoint) to the functor $u^*Y$. This functor is denoted $u_!Y$ (resp. $u_*Y$).

1. The functor $u^*Y$ commutes with inductive and projective limits. The diagram

   ```text
   ((C')^)Y --u*Y--> (C^)Y
      |                |
    ens              ens
      v                v
    (C')^  --u*-->    C^
   ```

   is commutative, where the vertical functors are the "underlying set" functors.

2. The functor $u_*Y$ commutes with projective limits. The diagram

   ```text
   (C^)Y --u_*Y--> ((C')^)Y
     |                |
   ens              ens
     v                v
    C^  --u_*-->    (C')^
   ```

   is commutative up to isomorphism.

[PDF p. 47]

3. The functor $u_!Y$ commutes with inductive limits. Suppose that $\operatorname{ens}^C$ (resp.
$\operatorname{ens}^{C'}$) admits a left adjoint $\operatorname{Lib}^C$ (resp. $\operatorname{Lib}^{C'}$) as in 5.8.2.
The diagram

   ```text
   C^ --u_!--> (C')^
   |             |
   Lib^C       Lib^{C'}
   v             v
   (C^)Y --u_!Y--> ((C')^)Y
   ```

   is commutative up to isomorphism.

Finally suppose that $u_!$ commutes with finite projective limits (5.4 4 and 5.6). Then the diagram

```text
(C^)Y --u_!Y--> ((C')^)Y
  |                |
ens              ens
  v                v
 C^  --u_!-->    (C')^
```

is commutative up to isomorphism, and $u_!Y$ commutes with finite projective limits.

**Proof.** Assertion (1) is evident. Assertion (2) is also evident, since $u_*Y$ is a right adjoint and therefore
commutes with projective limits by (2.11), in particular with finite projective limits; whence the commutativity of the
corresponding diagram. The commutativity of the diagram in (3) follows from uniqueness, up to isomorphism, of the left
adjoint functor. Finally, the commutativity of the last diagram follows immediately from the fact that $u_!$ commutes
with finite projective limits.

[PDF p. 48]

**Notation 5.9.** By abuse of notation, the functors $u^*Y$ and $u_*Y$ will often be denoted $u^*$ and $u_*$, which
cannot cause confusion in view of the commutativity of the first two diagrams above. On the other hand, when $u_!$ does
not commute with finite projective limits, the last diagram is not commutative up to isomorphism, and the notations
$u_!$ and $u_!Y$ must be distinguished to avoid any confusion.

**5.10.** Let $C$ be a small category. For every object $X$ of $\widehat{C}$, denote by $C/X$ the category of arrows
with target $X$ and source an object of $C$. The source functor defines a functor

$$ j_X : C/X \to C. $$

Let $m : Y \to X$ be a morphism of $\widehat{C}$. Composition of morphisms defines a functor

$$ j_m : C/Y \to C/X, $$

and the evident diagram with the source functors is commutative. It follows from 5.1 that, for every object $F$ of
$(C/X)^\wedge$ and every object $Y$ of $C$, one has

$$ (j_{X*}F)(Y)=\prod_{u \in \operatorname{Hom}_{\widehat{C}}(Y,X)} F(u). \tag{5.10.1} $$

Formula (5.10.1) makes it possible to define $j_{X*}$ when $C$ is a $U$-category, and one checks that the functor thus
defined is always right adjoint to the functor

$$ j_X^* : \widehat{C} \to (C/X)^\wedge. $$

[PDF p. 49]

**Proposition 5.11.** Let $C$ be a $U$-category and let $X$ be a presheaf on $C$.

1. The functor

   $$ e_X : (C/X)^\wedge \to \widehat{C} $$

   factors through the category $\widehat{C}/X$:

   $$ (C/X)^\wedge \xrightarrow{e_X} \widehat{C}/X \to \widehat{C}. $$

   The functor $e_X : (C/X)^\wedge \to \widehat{C}/X$ is an equivalence of categories.

2. The functor $e_X \circ j_X^* : \widehat{C} \to \widehat{C}/X$ is canonically isomorphic to the functor

   $$ H \mapsto (H \times X \to X). $$

**Proof.** For (1), let $\varepsilon$ be the final object of $(C/X)^\wedge$. There is a canonical isomorphism

$$ \varepsilon \simeq \varinjlim_{(Y \to X) \in C/X} Y, $$

and hence $e_X(\varepsilon) \simeq \varinjlim e_X(Y)$. But $e_X(\varepsilon)=X$, whence the factorization. To show that
$e_X$ is an equivalence, it suffices to exhibit a quasi-inverse: to every object $H \to X$ of $\widehat{C}/X$ one
associates the presheaf on $C/X$

$$ (Y \to X) \mapsto \operatorname{Hom}_{\widehat{C}/X}((Y \to X),(H \to X)). $$

2. The functor $e_X \circ j_X^*$ is right adjoint to the forgetful functor, and consequently it is canonically
isomorphic to the functor $H \mapsto (H \times X \to X)$.

**5.12.** Let $m : Y \to X$ be a morphism of $\widehat{C}$. By 5.11, the morphism $m$ is canonically isomorphic to the
image under $e_X$ of an object of $(C/X)^\wedge$, which we shall denote $[m]$. The functor $e_X$ defines, by restriction
to subcategories, an equivalence

$$ (C/X)/[m] \simeq C/Y. $$

[PDF p. 50]

The evident diagram is commutative up to canonical isomorphism.

**5.13.** Let us record a result which will be useful in Expose VI. Let $u : C \to C'$ be a functor between small
categories. For every object $H$ of $\widehat{C}$, denote by

$$ u/H : C/H \to C'/u_!H $$

the functor which associates to every morphism $m : X \to H$ the morphism $u_!X \to u_!H$. We know by 5.4 that one can
always put $u_!X=uX$. One obtains a commutative diagram

```text
C/H --u/H--> C'/u_!H
 |             |
 j_H           j_{u_!H}
 v             v
 C  --u-->     C'.                         (5.13.1)
```

Thus one has a diagram commutative up to isomorphism

```text
(C/H)^ ----> (C'/u_!H)^
  |              |
 j_{H*}        j_{u_!H,*}
  v              v
 C^ --u_*-->   (C')^.                      (5.13.2)
```

Since $(u/H)_!$ transforms the final object of $(C/H)^\wedge$ into the final object of $(C'/u_!H)^\wedge$, the diagram

[PDF p. 51]

```text
(C/H)^ ----> (C'/u_!H)^
  |              |
 e_H          e_{u_!H}
  v              v
 C^/H ----> (C')^/u_!H                    (5.13.3)
```

is commutative up to isomorphism.

**Proposition 5.14.** Let $u : C \to C'$ be a functor between small categories. Assume that $u$ has the following
property:

**(PPF)** For every object $X$ of $C$, the functor

$$ u/X : C/X \to C'/uX $$

is fully faithful.

Then:

1. Let $\varepsilon$ be the final object of $\widehat{C}$. The functor $u$ factors as

   $$ C \simeq C/\varepsilon \xrightarrow{u/\varepsilon} C'/u_!\varepsilon \to C'. $$

   The functor $u/\varepsilon$ is fully faithful.

2. The functor $u_! : \widehat{C} \to \widehat{C'}$ factors as

   $$
   \widehat{C}
   \simeq (C/\varepsilon)^\wedge
   \xrightarrow{(u/\varepsilon)_!}
   (C'/u_!\varepsilon)^\wedge
   \xrightarrow{e_{u_!\varepsilon}}
   \widehat{C'}/u_!\varepsilon
   \to \widehat{C'},
   $$

   where the functor $(u/\varepsilon)_!$ is fully faithful, the functor $e_{u_!\varepsilon}$ is an equivalence, and the
   last functor is the forgetful functor.

3. In particular, the functor $u_!$ is faithful; consequently the adjunction morphism

   $$ \operatorname{id} \to u^*u_! $$

   is a monomorphism. Moreover, for every morphism $\alpha : H \to K$ of $\widehat{C}$, the square

   ```text
   H      ->  u*u_!H
   |          |
   alpha      u*u_!(alpha)
   v          v
   K      ->  u*u_!K
   ```

   is cartesian.

[PDF p. 52]

**Proof.** 1. The factorization comes from diagram (5.13.1). The functor $u$ is faithful; hence $u/\varepsilon$ is
faithful. Let us show that it is fully faithful. Let $X$ and $Y$ be two objects of $C$, let
$\operatorname{can}_X : uX \to u_!\varepsilon$ and $\operatorname{can}_Y : uY \to u_!\varepsilon$ be the canonical
morphisms, and let $m : uX \to uY$ be a morphism of $C'/u_!\varepsilon$. One has

$$ u_!\varepsilon=\varinjlim_{Z \in C} uZ. $$

By definition of the inductive limit, saying that $\operatorname{can}_Y m=\operatorname{can}_X$ is equivalent to saying
that there exists a finite sequence of objects $X_i$ of $C$, with $X_0=X$ and $X_n=Y$, and, for every pair $(i,i+1)$, a
morphism $X_i \to X_{i+1}$ or a morphism $X_{i+1} \to X_i$, so that the corresponding diagrams are commutative. One then
proves immediately, by induction on $i$ and using property (PPF), that $m$ is of the form $u(p)$. In particular
$u/\varepsilon$ is fully faithful.

[PDF p. 53]

2. The factorization is immediate. The functor $(u/\varepsilon)_!$ is fully faithful by 5.6. The other assertions follow
from 5.11.

3. The functor $u_!$ is the composite of the forgetful functor, which is faithful, and fully faithful functors; it is
therefore faithful. It follows, from the general properties of adjoint functors, that the adjunction morphism
$\operatorname{id} \to u^*u_!$ is a monomorphism. By (2), the functor $u_!$ appears as the composite of a fully faithful
functor $v : \widehat{C} \to \widehat{C'}/u_!\varepsilon$ and the forgetful functor. The functor $u^*$, right adjoint to
$u_!$, is therefore the composite of the "product by $u_!\varepsilon$" functor, right adjoint to the forgetful functor,
and of a functor $w$ right adjoint to $v$. Moreover, since $v$ is fully faithful, the adjunction morphism
$\operatorname{id} \to wv$ is an isomorphism. The last assertion follows easily.

[PDF p. 54]

## 6. Faithful Functors and Conservative Functors

**Definition 6.1.** Let $E$ be a category and let $(\varphi_i : E \to F_i)_{i \in I}$ be a family of functors. We say
that the family $(\varphi_i)$ is **faithful** if, for every pair of objects $X,Y$ of $E$ and every pair of arrows
$u,v : X \to Y$, the relation $\varphi_i(u)=\varphi_i(v)$ for every $i \in I$ implies $u=v$. In other words, the map

$$
\operatorname{Hom}_E(X,Y) \to
\prod_{i \in I} \operatorname{Hom}_{F_i}(\varphi_iX,\varphi_iY)
$$

defined by the $\varphi_i$ is injective.

We say that the family $(\varphi_i)$ is **conservative** if every arrow $u$ of $E$ such that $\varphi_i(u)$ is an
isomorphism for every $i \in I$ is an isomorphism. We say that $(\varphi_i)$ is conservative for monomorphisms (resp.
for epimorphisms, etc.) if the preceding condition is verified whenever $u$ is a monomorphism (resp. an epimorphism,
etc.).

**6.1.1.** If one introduces the unique functor

$$ \varphi : E \to F=\prod_{i \in I} F_i $$

defined by the family $(\varphi_i)$, it is clear that this family is faithful (resp. conservative, resp. conservative
for monomorphisms, etc.) if and only if the functor $\varphi$ is faithful (resp. conservative, resp. etc.). Thus,
without serious inconvenience, we could restrict ourselves below to the case of a family reduced to a single functor.
For convenience in later references, nevertheless, we shall give the following statements for families.

[PDF p. 55]

The notions of 6.1 are especially useful when the $\varphi_i$ satisfy suitable exactness properties; in that case, they
tend to coincide.

**Proposition 6.2.** The notation is that of 6.1.

1. If kernels of double arrows, or cokernels of double arrows, are representable in $E$, and if the $\varphi_i$ commute
   with them, then one has the implication

   $$ (\varphi_i)\text{ conservative } \Longrightarrow (\varphi_i)\text{ faithful}. $$

2. Suppose that fiber products (resp. amalgamated sums) are representable in $E$, and that the $\varphi_i$ commute with
   them. Suppose that $(\varphi_i)$ is faithful or conservative. Then, for every arrow $u$ of $E$, $u$ is a monomorphism
   (resp. an epimorphism) if and only if $\varphi_i(u)$ is so for every $i \in I$.

3. Suppose that, in $E$, fiber products and amalgamated sums are representable, that the $\varphi_i$ commute with them,
   and that every arrow of $E$ which is a bimorphism is an isomorphism. Then one has the implication

   $$ (\varphi_i)\text{ faithful } \Longrightarrow (\varphi_i)\text{ conservative}. $$

4. Suppose that, in $E$, fiber products (resp. amalgamated sums) are representable, and that the $\varphi_i$ commute
   with them. If $(\varphi_i)$ is conservative for monomorphisms (resp. for epimorphisms), then $(\varphi_i)$ is
   conservative.

5. Let $D$ be a type of diagram, let $F : D \to E$ be a diagram of type $D$ in $E$, let $X$ be an object of $E$, and let
   $u=(u_d)_{d \in D}$ be a family of arrows

   $$ X \to F(d) \qquad (\text{resp. } F(d) \to X). $$

[PDF p. 56]

   Suppose that $(\varphi_i)$ is conservative, that projective (resp. inductive) limits of type $D$ are representable in
   $E$, and that the $\varphi_i$ commute with them. Then, for $u$ to make $X$ a projective (resp. inductive) limit of
   $F$ in $E$, it is necessary and sufficient that, for every $i \in I$, $\varphi_i(u)$ make $\varphi_i(X)$ a projective
   (resp. inductive) limit of $\varphi_i \circ F$ in $F_i$.

**Proof.** For (1), in the non-dual statement, for a given double arrow $u,v : X \rightrightarrows Y$, it suffices to
express the equality $u=v$ by the condition that the inclusion $\operatorname{Ker}(u,v) \to X$ be an isomorphism. Here
and below, we omit repeating the dual argument.

For (2), if $(\varphi_i)$ is faithful, one expresses the condition that $u : X \to Y$ be a monomorphism by the equality
of the two projections in the fiber product $X \times_Y X$. If $(\varphi_i)$ is conservative, one expresses it by the
condition that the diagonal morphism $\delta : X \to X \times_Y X$ be an isomorphism.

For (4), as in this last argument, the morphism $\delta$ is a monomorphism, so one sees that it would in fact have
sufficed to suppose $(\varphi_i)$ conservative for monomorphisms. But this then implies that $(\varphi_i)$ is
conservative outright. Indeed, if $u$ is an arrow of $E$ such that the $\varphi_i(u)$ are isomorphisms, one first
concludes that $u$ is a monomorphism by what precedes, and then an isomorphism by the hypothesis on $(\varphi_i)$.

Assertion (3) is a trivial consequence of (2), and (5) is a trivial consequence of the definitions.

Let us note the following consequence of (1), (2), and (4).

[PDF p. 57]

**Corollary 6.3.** Suppose that, in $E$, fiber products and amalgamated sums are representable and that the $\varphi_i$
commute with them; suppose furthermore that kernels of double arrows or cokernels of double arrows are representable and
that the $\varphi_i$ commute with them. It suffices, for example, that finite projective limits and finite inductive
limits be representable in $E$, and that the $\varphi_i$ be exact functors. Then the following conditions are
equivalent:

1. $(\varphi_i)$ is faithful.
2. $(\varphi_i)$ is conservative.
3. $(\varphi_i)$ is conservative for monomorphisms.
4. $(\varphi_i)$ is conservative for epimorphisms.

Let us also record for reference:

**Proposition 6.4.** Let $\varphi : E \to F$ be a functor admitting a right adjoint $\psi$, so that

$$ \operatorname{Hom}_F(\varphi(X),Y) \simeq \operatorname{Hom}_E(X,\psi(Y)). $$

For $\varphi$ (resp. $\psi$) to be faithful, it is necessary and sufficient that, for every object $X$ of $E$ (resp.
every object $Y$ of $F$), the adjunction morphism $X \to \psi\varphi(X)$ (resp. $\varphi\psi(Y) \to Y$) be a
monomorphism. For $\varphi$ (resp. $\psi$) to be fully faithful, it is necessary and sufficient that the corresponding
adjunction morphism be an isomorphism.

Indeed, if $X'$ and $X$ are two objects of $E$, the map

$$ \operatorname{Hom}_E(X',X) \to \operatorname{Hom}_F(\varphi(X'),\varphi(X)) $$

is identified with the map deduced from the adjunction morphism

$$ X \to \psi\varphi(X) $$

by applying the functor $\operatorname{Hom}_E(X',-)$. Thus, for this map to be a monomorphism (resp. an isomorphism) for
every $X'$, with $X$ fixed, it is necessary and sufficient that the adjunction morphism be a monomorphism (resp. an
isomorphism).

[PDF p. 58]

**Proposition 6.5.** Let $p : E' \to E$ be a functor. The following conditions are equivalent:

1. $p$ is faithful, conservative, and fibering (SGA 1 VI 6.1).
2. $p$ is a fibering functor with fibers discrete categories.
3. For every $X' \in \operatorname{ob}(E')$, the functor on arrow categories induced by $p$

   $$ E'/X' \to E/p(X') $$

   is an equivalence of categories, surjective on objects.
4. When $E$ is a $U$-category, there exists a presheaf $F \in \operatorname{ob}(\widehat{E})$ and an equivalence of
   categories over $E$

   $$ E' \simeq E/F, $$

   where $E/F$ is the full subcategory of $\widehat{E}/F$ formed by the arrows $X \to F$ whose source is in $E$.

**6.5.1.** Recall that a category $C$ is called **discrete** if it is a groupoid, that is, if every arrow in it is
invertible, and if it is rigid, that is, if the automorphism group of every object is reduced to the unit group. This is
equivalent to saying that the category is equivalent to the category defined by a set, with only identity arrows. When
one already assumes that $C$ is a groupoid, saying that $C$ is discrete amounts to saying that, for two objects $X,Y$ of
$C$, there exists at most one arrow from $X$ to $Y$.

[PDF p. 59]

The equivalence of conditions (1) and (2) of 6.5 is an immediate consequence of the preceding reminders and of the
following lemma.

**Lemma 6.5.2.** Let $p : E' \to E$ be a fibering functor. Then:

1. For $p$ to be conservative, it is necessary and sufficient that its fiber categories be groupoids.
2. For $p$ to be faithful, it is necessary and sufficient that its fiber categories be ordered categories.

**Proof.** First suppose that $p$ is conservative. For every arrow $u$ of a fiber $E'_X$, $p(u)=\operatorname{id}_X$ is
an isomorphism, hence $u$ is an isomorphism in $E'$, and therefore also in $E'_X$. Thus $E'_X$ is a groupoid.
Conversely, suppose that the $E'_X$ are groupoids, and let $u'$ be an arrow of $E'$ such that $p(u')$ is an isomorphism.
Write $X=p(X')$ and $u=p(u')$. Since $p$ is fibering, one can factor $u' : X' \to Y'$ as a composite

$$ X' \to u^*(Y') \to Y', $$

where the first arrow is an $X$-morphism and the second is a cartesian morphism over $u$. The first arrow is an
isomorphism because $E'_X$ is a groupoid, and the second is one because a cartesian morphism of a fibered category is
obviously an isomorphism as soon as its projection is.

For (2), suppose that $p$ is faithful. If $X'$ and $Y'$ are two objects of a fiber category $E'_X$, then two arrows from
$X'$ to $Y'$ lie over the same arrow $\operatorname{id}_X$ of $E$, hence are identical; thus $E'_X$ is ordered.

[PDF p. 60]

Conversely, suppose that the fiber categories are ordered. Let $u',v' : X' \to Y'$ be two arrows of $E'$ over a same
arrow $u : X \to Y$ of $E$. They then factor as

$$ X' \to u^*(Y') \to Y', $$

where the two first arrows $X' \to u^*(Y')$ are arrows of $E'_X$ with the same source and the same target. These are
therefore equal, and consequently $u'=v'$.

We return to the proof of 6.5. We have proved the equivalence of (1) and (2). On the other hand, (2) implies (4).
Indeed, first, the category $E/F$ is fibered over $E$ with fiber categories the discrete categories defined by the sets
$F(X)$, as follows at once from the definitions. Secondly, if $p$ is as in (2), then, by the sorites of SGA 1 VI 8, the
fibered category $E'$ over $E$ is $E$-equivalent to the split category over $E$ defined by the functor
$F : E^\circ \to \mathbf{Ens}$ which associates to every $X \in \operatorname{ob}(E)$ the set of isomorphism classes of
objects of $E'_X$. This split category is $E$-isomorphic to the category $E/F$. Since (4) clearly implies (3), and (3)
implies (2), the proof is complete.

## 7. Generating and Cogenerating Subcategories

**Definition 7.1.** Let $E$ be a category and let $C$ be a full subcategory of $E$. We say that $C$ is a subcategory of
$E$ **generating by strict epimorphisms** (resp. **by epimorphisms**) if, for every object $X$ of $E$, the family of
arrows of $E$ with target $X$ and source $X' \in \operatorname{ob}(C)$ is strictly epimorphic (resp. epimorphic) (1.3).

We say that $C$ is a **generating** subcategory of $E$ (resp. **generating for monomorphisms**, resp. **generating for
strict monomorphisms**) if, for every arrow $u : Y \to X$ (resp. every monomorphism of $E$, resp. every strict
monomorphism of $E$ (10.5)) such that, for every $X' \in \operatorname{ob}(C)$, the corresponding map

$$ \operatorname{Hom}(X',Y) \to \operatorname{Hom}(X',X) $$

is bijective, $u$ is an isomorphism. Finally, we say that a family $(X_i)$ of objects of $E$ generates by strict
epimorphisms (resp. etc.) if the full subcategory of $E$ generated by this family has the corresponding property.

**7.1.1.** In terms of the family $(h_{X'})_{X' \in \operatorname{ob}(C)}$ of functors

$$ h_{X'} : E \to \mathbf{Ens}, \qquad X \mapsto \operatorname{Hom}(X',X), $$

represented by the $X' \in \operatorname{ob}(C)$, the condition that $C$ be generating (resp. generating for
monomorphisms, resp. generating for strict monomorphisms) is equivalent to saying that the family $(h_{X'})$ is
conservative (resp. conservative for monomorphisms, resp. conservative for strict monomorphisms) in the sense of 6.1.

[PDF p. 62]

It also follows immediately from the definitions that $C$ generates by epimorphisms if and only if the family
$(h_{X'})_{X' \in \operatorname{ob}(C)}$ is faithful (6.1). Below (7.2 (1)) we shall also give an analogous
interpretation of the condition that $C$ generate by strict epimorphisms.

**7.1.2.** As with the notions introduced in 6.1, the notions of 7.1 are especially useful when $E$ has suitable
exactness properties; in that case, the various notions introduced have a marked tendency to be all equivalent (7.3).
For this reason the question of which of these notions should be considered the most important scarcely arises: in the
most important cases, they coincide, and the term "generating subcategory" may be interpreted indifferently as referring
to any of the properties considered in 7.1, for example to the first, which is the strongest of all, as we shall now see
(7.2 (ii)).

**7.1.3.** Suppose that $E$ is a $U$-category, and consider the canonical functor

$$
\varphi : E \to \widehat{C}=\operatorname{Hom}(C^\circ,U\text{-}\mathbf{Ens}), \tag{7.1.3.1}
$$

the composite of the functors $E \to \widehat{E} \to \widehat{C}$, where the first is the canonical functor (1.3.3) and
the second is restriction to $C$. It is evident that saying that the functor $\varphi$ is conservative (resp. faithful)
is equivalent to saying that the family of functors

$$ h_{X'} : X \mapsto \operatorname{Hom}(X',X)=\varphi(X)(X'), \qquad X' \in \operatorname{ob}(C), $$

is conservative (resp. faithful), that is also, that $C$ is generating (resp. generating by epimorphisms). Similarly,
$\varphi$ is conservative for monomorphisms (resp. for strict monomorphisms) if and only if the family of the $h_{X'}$
is conservative for monomorphisms (resp. for strict monomorphisms), that is, if and only if $C$ is generating for
monomorphisms (resp. for strict monomorphisms).

[PDF p. 63]

**Proposition 7.2.** Let $E$ be a $U$-category and let $C$ be a full subcategory.

1. The following conditions are equivalent:

   a. $C$ is a subcategory generating by strict epimorphisms.

   b. For every $X \in \operatorname{ob}(E)$, denote by $C/X$ the full subcategory of $E/X$ formed by the arrows
      $X' \to X$ with source $X' \in \operatorname{ob}(C)$. Then the natural arrow from the inclusion functor
      $j : C/X \to E$ to the constant functor on $C/X$ with value $X$ makes $X$ an inductive limit of $j$:

      $$ X \simeq \varinjlim_{C/X} X'. $$

   c. The canonical functor $\varphi$ of (7.1.3.1) is fully faithful.

2. Among the notions of 7.1 one has the following implications:

   ```text
   (1) C generating by strict epimorphisms
       (phi fully faithful)
          => (2) C generating by epimorphisms
             (phi faithful)
          => (3) C generating
             (phi conservative)
          => (4) C generating for monomorphisms
             (phi conservative for monomorphisms)
          => (5) C generating for strict monomorphisms
             (phi conservative for strict monomorphisms).
   ```

[PDF p. 64]

3. One has the following conditional implications:

   a. If, in $E$, epimorphic families of arrows are strictly epimorphic, then (2) implies (1). If, in $E$, monomorphisms
      are strict, then (5) implies (4).

   b. If, in $E$, kernels of pairs of arrows (resp. fiber products) are representable, then (3) implies (2) (resp. (4)
      implies (3)).

   c. If, in $E$, every family of morphisms $X_i \to X$ with common target $X$ factors as a strictly epimorphic (resp.
      epimorphic) family $X_i \to Y$ followed by a monomorphism (resp. by a strict monomorphism) $Y \to X$, then (4)
      implies (1) (resp. (5) implies (2)).

Let us record at once the following corollary.

**Corollary 7.3.** All the notions considered in 7.1 and repeated in the implication diagram of 7.2 (2) are equivalent
in each of the following two cases:

1. In $E$, kernels of double arrows and fiber products are representable, monomorphisms are strict, and epimorphic
   families of arrows are strictly epimorphic.

2. In $E$, every family $(X_i \to X)_{i \in I}$ of arrows with common target $X$ factors as an epimorphic family
   $X_i \to Y$ followed by a monomorphism $Y \to X$, every monomorphism of $E$ is strict, and every epimorphic family of
   arrows of $E$ is strict.

[PDF p. 65]

Indeed, in case (1), one has $(4) \Rightarrow (3)$ and $(3) \Rightarrow (2)$ by 7.2 (3b), and $(5) \Rightarrow (4)$ and
$(2) \Rightarrow (1)$ by 7.2 (3a). In case (2), by 7.2 (3c), one has the implications $(4) \Rightarrow (1)$ and
$(5) \Rightarrow (2)$. We then conclude by the implication diagram 7.2 (2).

**Proof of 7.2.** For (1), the implication b $\Rightarrow$ a follows at once from the definitions. Let us prove a
$\Rightarrow$ b. Under hypothesis a, one must prove that, for all $X,Y \in \operatorname{ob}(E)$, every system of arrows

$$ u_{X'} : X' \to Y, $$

indexed by the $X' \in \operatorname{ob}(C/X)$, such that $u_{X'}=u_{X''} \circ f$ for every arrow $f : X' \to X''$ in
$C/X$, factors through an arrow, necessarily unique by hypothesis a, $X \to Y$. By hypothesis a, it suffices to check
that, for every object $Z$ of $E/X$ and every pair of morphisms $v' : Z \to X'$, $v'' : Z \to X''$ in $E/X$, with $X'$
and $X''$ in $C/X$, one has

$$ u_{X'}v'=u_{X''}v''. $$

But, by hypothesis a, the family of arrows $W \to Z$, with $W \in \operatorname{ob}(C)$, is strictly epimorphic; it
therefore suffices to check this equality after composition by every such arrow $w : W \to Z$. It then reads

$$ u_{X'}(v'w)=u_{X''}(v''w), $$

and follows at once from the hypothesis made on the family of the $u_{X'}$.

Let us now prove the equivalence of conditions b and c. For every $X \in \operatorname{ob}(E)$, the object $\varphi(X)$
of $\widehat{C}$ is the inductive limit in $\widehat{C}$ of the canonical functor $C/\varphi(X) \to \widehat{C}$ (3.4).
But $C/\varphi(X)$ is canonically isomorphic to $C/X$, so that in $\widehat{C}$ one has

$$ \varphi(X) \simeq \varinjlim_{C/X} X', $$

where the object $X'$ of $C$ is identified with the functor it represents.

[PDF p. 66]

Consequently, for a second object $Y$ of $E$, one has a canonical isomorphism

$$
\operatorname{Hom}_{\widehat{C}}(\varphi(X),\varphi(Y))
\simeq
\varprojlim_{C/X} \operatorname{Hom}_{\widehat{C}}(X',\varphi(Y))
\simeq
\varprojlim_{C/X} \operatorname{Hom}_E(X',Y). \tag{*}
$$

This said, the map

$$ \operatorname{Hom}_E(X,Y) \to \operatorname{Hom}_{\widehat{C}}(\varphi(X),\varphi(Y)) $$

defined by $\varphi$ is none other, via the isomorphism between the extreme terms of (*), than the map deduced from the
inductive system of arrows $X' \to X$ indexed by $C/X$ considered in 7.2 (1b). Thus this map is bijective for every $Y$,
with $X$ fixed, if and only if $X$ is an inductive limit of the inclusion functor $j : C/X \to E$, which proves the
equivalence of b and c.

For (2), the implications $(1) \Rightarrow (2)$ and $(3) \Rightarrow (4) \Rightarrow (5)$ are trivial by the
definitions. The implication $(1) \Rightarrow (3)$ is obtained by interpreting (1) as the full faithfulness of $\varphi$
by (1), and observing that a fully faithful functor is conservative. We have already observed in 7.1.3 that (3) means
that $\varphi$ is conservative.

[PDF p. 67]

For (3), assertion a is a tautology. Assertion b follows from 6.2 (1) (resp. 6.2 (4)) applied to the functor $\varphi$,
taking into account that the latter is left exact. Finally let us prove c. Consider, for an object $X$ of $E$, the
family of all morphisms $X_i \to X$, with $X_i \in \operatorname{ob}(C)$. By the hypothesis on $E$, it factors as a
strictly epimorphic (resp. epimorphic) family $X_i \to Y$ followed by a monomorphism (resp. by a strict monomorphism)
$Y \to X$. Then hypothesis (4) (resp. (5)) implies that $Y \to X$ is an isomorphism; hence the family considered is
strictly epimorphic (resp. epimorphic).

**Proposition 7.4.** Let $E$ be a category, let $C$ be a full subcategory of $E$, and let $X$ be an object of $E$.
Assume that $C$ is generating in $E$ (resp. that $C$ is generating for monomorphisms, and that the fiber product of two
subobjects of $X$ over $X$ is representable in $E$). Then a strict subobject (10.11) (resp. a subobject) $X'$ of $X$ is
known as soon as one knows, for every $T \in \operatorname{ob}(C)$, the subset of $\operatorname{Hom}(T,X)$ which is the
image of $\operatorname{Hom}(T,X')$. Consequently, the cardinal of the set of strict subobjects (resp. subobjects) of
$X$ is bounded above by

$$ \prod_{T \in \operatorname{ob}(C)} 2^{\operatorname{card}\operatorname{Hom}(T,X)}. $$

**Proof.** First prove the "resp." assertion. Let $X'$ and $X''$ be two subobjects of $X$ such that, for every
$T \in \operatorname{ob}(C)$, the images of $\operatorname{Hom}(T,X')$ and $\operatorname{Hom}(T,X'')$ in
$\operatorname{Hom}(T,X)$ are equal. They are therefore also equal to the image of $\operatorname{Hom}(T,X''')$, where
$X'''$ is the fiber product of $X'$ and $X''$ over $X$. Since $C$ is generating for monomorphisms, it follows that the
monomorphisms $X''' \to X'$ and $X''' \to X''$ are isomorphisms. Thus $X'$ and $X''$ are equal, both being equal to the
subobject $X'''$ of $X$.

[PDF p. 68]

Let us prove the non-"resp." assertion. By definition of the notion of strict subobject, it suffices to check that
knowing, for every $T \in \operatorname{ob}(C)$, the subset $\operatorname{Hom}(T,X')$ of $\operatorname{Hom}(T,X)$
implies knowing the double arrows

$$ u,v : X \rightrightarrows T $$

such that $ui=vi$, where $i : X' \to X$ is the canonical injection. Since $C$ is generating, the relation $ui=vi$ is
equivalent to the relation $(ui)f=(vi)f$ for every $f : T' \to X'$, with $T' \in \operatorname{ob}(C)$. In other words,
it is equivalent to $ug=vg$ for every $g \in \operatorname{Hom}(T',X)$ coming from $\operatorname{Hom}(T',X')$, that is,
of the form $if$. This proves the assertion.

**Corollary 7.5.** Let $E$ be a category, let $C$ be a full generating subcategory, and let $X$ be an object of $C$.
Then a strict quotient (10.8) $X'$ of $X$ is known when one knows, for every $T \in \operatorname{ob}(C)$, the subset of
$\operatorname{Hom}(T,X)^2$ formed by the pairs $(u,v)$ such that $qu=qv$, where $q : X \to X'$ is the canonical
morphism. Thus the cardinal of the set of strict quotients of $X$ is bounded above by

$$ \prod_{T \in \operatorname{ob}(C)} 2^{\operatorname{card}\operatorname{Hom}(T,X)^2}. $$

Indeed, by definition, a strict quotient $X'$ of $X$ is known when one knows, for every object $Y$ of $E$, the subset of
$\operatorname{Hom}(Y,X)^2$ formed by the pairs $(u,v)$ such that $qu=qv$. But the relation $qu=qv$ is equivalent to the
relation $(qu)f=(qv)f$ for every morphism $f : T \to Y$ with source $T$ in $C$, since $C$ is generating. This relation
may also be written $q(uf)=q(vf)$, which proves the first assertion of 7.5. The second follows at once.

[PDF p. 69]

**7.5.1.** One can generalize 7.5 by introducing, for a family of objects $(X_i)_{i \in I}$ of $E$, the notion of a
strict quotient in $E$ of the family. By this one means a strictly epimorphic family

$$ p_i : X_i \to X' \qquad (i \in I) $$

of morphisms of $E$, with the understanding, as for ordinary quotients, that two such families $(p_i : X_i \to X')$ and
$(q_i : X_i \to X'')$ are identified if there exists an isomorphism $v : X' \to X''$, necessarily unique, such that
$vp_i=q_i$ for every $i \in I$. With this terminology, the proof of 7.5 applies mutatis mutandis to give the following
variant.

**Variant 7.5.2.** Let $E$ and $C$ be as in 7.5, and let $(X_i)_{i \in I}$ be a family of objects of $E$. Then a strict
quotient $X'$ of the $X_i$ in $E$ (7.5.1) is known when one knows, for every $T \in \operatorname{ob}(C)$ and every pair
$(i,j) \in I \times I$, the subset of $\operatorname{Hom}(T,X_i) \times \operatorname{Hom}(T,X_j)$ formed by the pairs
$(u,v)$ such that $p_i u=p_j v$, where, for every $i \in I$, $p_i : X_i \to X'$ denotes the canonical morphism.
Consequently, the cardinal of the set of strict quotients of the $X_i$ in $E$ is bounded above by

$$
\prod_{T \in \operatorname{ob}(C)}
\prod_{i,j \in I}
2^{\operatorname{card}\operatorname{Hom}(T,X_i)\cdot
\operatorname{card}\operatorname{Hom}(T,X_j)}.
$$

**7.5.3.** The analogous conclusion remains true if one only assumes that $C$ is generating for strict monomorphisms,
provided that the products $X_i \times X_j$ are representable and that one restricts to effective quotients of the
family $(X_i)_{i \in I}$, that is, to strict quotients $X'$ such that the fiber products $X_i \times_{X'} X_j$ are
representable in $E$. This is not a restriction if $E$ is stable under fiber products.

[PDF p. 70]

**Proposition 7.6.** Let $E$ be a category, let $C$ be a full subcategory of $E$ generating by epimorphisms (7.1), and
let $\tau$ be an infinite cardinal bounding above the cardinal of the set of arrows of $C$. Let $\kappa$ be a cardinal
chosen sufficiently large relative to $\tau$. Let $X$ be an object of $E$ and let

$$ (u_i : X_i \to X)_{i \in I} $$

be a universal epimorphic family (10.3) in $E$, formed by quarrable morphisms (10.7), with sources
$X_i \in \operatorname{ob}(C)$, and such that $\operatorname{card}(I)<\tau$. Then the cardinal of the set of arrows of
$C/X$ is bounded above by $\kappa$.

It suffices to show that, for every $T \in \operatorname{ob}(C)$, one has

$$ \operatorname{card}\operatorname{Hom}(T,X)<\kappa. \tag{7.6.1} $$

Indeed, one deduces the corresponding bounds for the objects and arrows of $C/X$, since, for two objects $S,T$ of $C/X$,
one has

$$ \operatorname{card}\operatorname{Hom}_{C/X}(S,T) \leq \operatorname{card}\operatorname{Hom}_C(S,T) \leq \tau. $$

To prove (7.6.1), first note the following lemma.

**Lemma 7.6.2.** Let $J$ be a set such that $\operatorname{card}(J)=\tau$. For every object $T$ of $C$ and every
morphism $f : T \to X$, there exists an epimorphic family

$$ (v_j : S_j \to T)_{j \in J} $$

with sources $S_j \in \operatorname{ob}(C)$, and, for every $j \in J$, an index $i(j) \in I$ and a morphism
$g_j : S_j \to X_{i(j)}$ such that

$$ u_{i(j)}g_j=fv_j. $$

Indeed, the family of the $X_i \times_X T \to T$ is epimorphic by hypothesis. On the other hand, since $C$ generates by
epimorphisms, for every $i$, the family of arrows $S \to X_i \times_X T$ with source $S \in \operatorname{ob}(C)$ is
epimorphic. By transitivity, the family of arrows $v : S \to T$, with source in $C$, which factor through one of the
$X_i \times_X T$, is epimorphic.

[PDF p. 71]

But these are precisely the arrows $v : S \to T$ with source in $C$ for which there exists an $i \in I$ and a morphism
$g : S \to X_i$ such that $u_i g=fv$. The set of these arrows is contained in the set of arrows of $C$, hence has
cardinal $<\tau$; one can therefore index it by $J$, which proves the lemma.

A morphism $f : T \to X$ is known when one knows the composites $fv_j$, themselves known as soon as one knows the $g_j$.
Thus $\operatorname{card}\operatorname{Hom}(T,X)$ is bounded above by the cardinal of the set of families
$(i(j),g_j,v_j)_{j \in J}$. By the choice of the bounding cardinal $\kappa$, this cardinal is $<\kappa$; this gives
(7.6.1) and completes the proof of 7.6.

**Proposition 7.7.** Let $E$ be a category in which fiber products are representable, let $(X_a)_{a \in A}$ be a
generating family of objects of $E$, and let $(\varphi_i : E \to E_i)_{i \in I}$ be a family of functors commuting with
fiber products. For $(\varphi_i)$ to be conservative (6.1), it is necessary and sufficient that, for every $a \in A$ and
every subobject $X'$ of $X_a$ distinct from $X_a$, there exists an $i \in I$ such that

$$ \varphi_i(X') \to \varphi_i(X_a) $$

is not an isomorphism. In this case, if $E$ is a $U$-category and if $A$ is $U$-small, there exists a $U$-small subset
$J$ of $I$ such that $(\varphi_j)_{j \in J}$ is already a conservative family of functors.

The necessity of the condition is evident. Let us prove its sufficiency. By 6.2 (4), it suffices to prove that
$(\varphi_i)$ is conservative for monomorphisms.

[PDF p. 72]

Let $u : Y' \to Y$ be a monomorphism in $E$ which is not an isomorphism. One must prove that there exists $i \in I$ such
that $\varphi_i(u)$ is not an isomorphism. By the hypothesis on the family $(X_a)$, there exists an $a \in A$ and a
morphism $X_a \to Y$ which does not factor through $Y'$. In other words, the inverse image $X'$ of $Y'$ in $X_a$ is a
subobject of $X_a$ distinct from $X_a$. By hypothesis, there exists an $i \in I$ such that
$\varphi_i(X') \to \varphi_i(X_a)$ is not an isomorphism. Since $\varphi_i(X')$ is the fiber product of $\varphi_i(Y')$
with $\varphi_i(X_a)$ over $\varphi_i(Y)$, it follows that $\varphi_i(Y') \to \varphi_i(Y)$ is not an isomorphism.

The second assertion of 7.7 follows at once from the first, taking 7.4 into account.

**Corollary 7.7.1.** Let $E$ be a $U$-category in which fiber products are representable and which admits a $U$-small
generating family of objects. Then, for every generating family $(Y_i)_{i \in I}$ of objects of $E$, there exists a
$U$-small generating subfamily $(Y_j)_{j \in J}$.

It suffices to apply 7.7 to a $U$-small generating family $(X_a)_{a \in A}$ of $E$ and to the family of functors
represented by the $Y_i$.

**Proposition 7.8.** Let $E$ be a category, let $C$ be a full subcategory generating by strict epimorphisms, let $D$ be
a category, and let $\operatorname{Hom}'(E,D)$ be the full subcategory of $\operatorname{Hom}(E,D)$ formed by the
functors which commute with inductive limits of type $C/X$, where $X$ runs through the objects of $E$. Then the
restriction functor induces a fully faithful functor

$$ \operatorname{Hom}'(E,D) \to \operatorname{Hom}(C,D). $$

[PDF p. 73]

Consequently, if $\operatorname{Hom}(C,D)$ is a $U$-category, for example if $C$ is $U$-small and $D$ is a $U$-category,
then $\operatorname{Hom}'(E,D)$ is also a $U$-category.

Let $F,G : E \to D$ be two functors in $\operatorname{Hom}'(E,D)$, and let $u : F \to G$ be a morphism. If
$X=\varinjlim_{C/X} X'$ in $E$ and if $F$ and $G$ commute with this inductive limit, then $u(X) : F(X) \to G(X)$ is
identified with the limit of the morphisms $u(X') : F(X') \to G(X')$. It is therefore known as soon as one knows the
$u(X')$. This shows that the functor considered is faithful, taking into account the implication a $\Rightarrow$ b in
7.2 (1).

Conversely, let $v : F|_C \to G|_C$ be a morphism. Let us show that it comes from a morphism $u : F \to G$. For every
$X \in \operatorname{ob}(E)$, define

$$
u(X) : F(X)=\varinjlim_{C/X} F(X')
\to
G(X)=\varinjlim_{C/X} G(X')
$$

as the inductive limit of the $v(X')$. It is immediate that one thus obtains a morphism functorial in $X$, hence a
morphism $u : F \to G$, and that the morphism induced by $u$ from $F|_C$ to $G|_C$ is $v$. This completes the proof.

**7.9. Families and cogenerating subcategories.** Let $E$ be a category and let $D$ be a full subcategory of $E$. We say
that $D$ is cogenerating by strict monomorphisms (resp. cogenerating by monomorphisms, resp. cogenerating, resp.
cogenerating for epimorphisms, resp. cogenerating for strict epimorphisms) if the full subcategory $D^\circ$ of
$E^\circ$ is generating by strict epimorphisms (resp. by epimorphisms, resp. generating, resp. generating for
monomorphisms, resp. generating for strict monomorphisms). The terminology for families is analogous.

[PDF p. 74]

All the results of the present section concerning the notion of generating subcategory and its variants (7.1) therefore
give, by duality, corresponding results for the dual notions, which we leave to the reader to formulate for his personal
satisfaction.

**Proposition 7.10.** Let $E$ be a category, let $C$ be a full generating subcategory (7.1), and let $D$ be a full
subcategory of $E$. For $D$ to be cogenerating (7.9), it is necessary and sufficient that, for every double arrow

$$ u,v : T \rightrightarrows X $$

in $E$, with source $T \in \operatorname{ob}(C)$, and with $u \neq v$, there exists an arrow $w : X \to I$ with target
$I \in \operatorname{ob}(D)$ such that $wu \neq wv$.

By definition, saying that $D$ is cogenerating means that, for every double arrow $u,v : Y \rightrightarrows X$ in $E$
such that $u \neq v$, there exists an arrow $w : X \to I$, with $I \in \operatorname{ob}(D)$, such that $wu \neq wv$.
Proposition 7.10 simply says that it suffices to test this property when $Y \in \operatorname{ob}(C)$. Since $C$ is
generating, the hypothesis $u \neq v$ implies that there exists $f : T \to Y$, with $T \in \operatorname{ob}(C)$, such
that $uf \neq vf$. By hypothesis, there then exists $w : X \to I$, with target $I \in \operatorname{ob}(D)$, such that
$wuf \neq wvf$, whence $wu \neq wv$.

**Corollary 7.11.** With the notation of 7.10, suppose that the objects $I$ of $D$ are injective objects of $E$, that
is, such that, for every monomorphism $X \to Y$ in $E$, the corresponding map

$$ \operatorname{Hom}(Y,I) \to \operatorname{Hom}(X,I) $$

is surjective. Suppose moreover that every double arrow $T \rightrightarrows X$ in $E$ factors as an epimorphic (resp.
effective epimorphic) double arrow $T \rightrightarrows X'$ followed by a monomorphism $i : X' \to X$. Then, in the
criterion 7.10 for $D$ to be cogenerating, one may restrict to double arrows $(u,v)$ which are epimorphic (resp.
effective epimorphic).

[PDF p. 75]

We conclude:

**Corollary 7.12.** Let $E$ be a $U$-category admitting a small generating subcategory $C$, and such that every object
of $E$ is the source of a monomorphism into an injective object of $E$. Suppose moreover that, for all
$T,T' \in \operatorname{ob}(C)$, the sum $T \amalg T'$ in $E$ is representable, and that every morphism with source
$T \amalg T'$ factors as an effective epimorphism followed by a monomorphism. Then $E$ admits a small full cogenerating
subcategory. More precisely, one may take $D$ such that

$$
\operatorname{card}\operatorname{ob}(D) <
\prod_{T,T' \in \operatorname{ob}(C)}
2^{\operatorname{card}\operatorname{Hom}(T \amalg T',T \amalg T')}.
$$

Indeed, by 7.11, it suffices, for all $T,T' \in \operatorname{ob}(C)$ and for every effective quotient $X$ of
$T \amalg T'$, to choose an embedding of $X$ into an injective object $I$ of $E$, and to take for $D$ the full
subcategory of $E$ generated by these $I$. The conclusion then follows from 7.5.

**Examples 7.13.** To construct small cogenerating subcategories in terms of small generating subcategories, one is thus
led to seek conditions for a $U$-category $E$ to admit "enough injectives," that is, for every object to embed in an
injective object by a monomorphism. It is well known [Tohoku] that this condition is satisfied in a $U$-abelian category
with exact small filtering inductive limits (axiom AB 5 of loc. cit.) admitting a small generating family.

The construction of loc. cit. is not, moreover, essentially tied to abelian categories, and also works in the category
of sheaves of $U$-sets on a topological space $X \in U$. We shall not state here the exactness properties which make the
construction in question work, and we shall restrict ourselves to noting that,

[PDF p. 76]

in the particular case of the category of sheaves of sets on $X$, one reduces immediately to the case of loc. cit. as
follows. If $O_X$ is a ring on $X$, then every injective object $I$ of the category of $O_X$-modules is also injective
as an object of the category of sheaves of sets. Indeed, if $F$ is a sheaf of sets, and if $O_X[F]$ denotes the free
$O_X$-module generated by $F$, by definition one has a homomorphism of sheaves of sets

$$ F \to O_X[F] \tag{*} $$

giving rise to an isomorphism, functorial in $F$,

$$ \operatorname{Hom}_{O_X}(O_X[F],I) \simeq \operatorname{Hom}(F,I). $$

Since the functor $F \mapsto O_X[F]$ manifestly transforms monomorphisms into monomorphisms, it follows at once that, if
$I$ is an injective $O_X$-module, it is also an injective sheaf of sets. It follows that, if the morphism (*) is a
monomorphism, which is the case if one takes for $O_X$ a constant ring with value a ring $A \neq 0$, then an embedding
of $O_X[F]$ into an injective $O_X$-module $I$ gives an embedding of $F$ into the sheaf of sets underlying the injective
sheaf $I$.

The same argument applies, without change, to the category of sheaves of $U$-sets on a $U$-site, which will be
introduced in the following expose.

The interest of the existence of a small cogenerating subcategory lies mainly in the representability criterion 8.12.7
below.

[PDF p. 77]

# 8. Ind-Objects and Pro-Objects

## 8.1. Cofinal Functors and Cofinal Subcategories

Let

$$ \varphi : I \to I' \tag{8.1.1.1} $$

be a functor. We say that $\varphi$ is a **cofinal functor** if, for every category $C$ and every functor
$u : I' \to C$, regarding $\varinjlim u$ and $\varinjlim(u \circ \varphi)$ as objects of
$\operatorname{Hom}(C^\circ,V\text{-}\mathbf{Ens})^\circ$ (2.1, 2.3.1), where $V$ is a universe such that $I$, $I'$
belong to $V$ and $C$ is a $V$-category, the canonical morphism

$$ \varinjlim_I (u \circ \varphi) \to \varinjlim_{I'} u \tag{8.1.1.2} $$

is an isomorphism. When $\varphi$ is the inclusion functor of a subcategory of $I'$, we say that $I$ is a cofinal
subcategory if $\varphi$ is cofinal.

**8.1.2.** For given $\varphi$ and $u$, the bijectivity of (8.1.1.2) does not depend on the choice of the universe $V$.
Returning to the definition of the terms occurring in (8.1.1.2) (2.1, 2.3.1), one sees that saying that $\varphi$ is
cofinal also means that, for every universe $V$ such that $I$ and $I'$ are $V$-small, and every functor

$$ v : (I')^\circ \to V\text{-}\mathbf{Ens}, $$

the canonical homomorphism

$$ \varinjlim_{I'} v \to \varinjlim_I (v \circ \varphi) \tag{8.1.2.1} $$

is an isomorphism, that is, a bijection. To see that this condition is necessary, one observes, putting $u=v^\circ$,
that it means that the condition of Definition 8.1.1 is fulfilled when one takes $C=(V\text{-}\mathbf{Ens})^\circ$,
which implies that the inductive limits considered in (8.1.1.2) are representable in $C$.

[PDF p. 78]

**8.1.2.2.** It is immediate from the definition that the composite of two cofinal functors is cofinal.

**Proposition 8.1.3.** Let $\varphi : I \to I'$ be a functor.

1. For $\varphi$ to be cofinal, it is necessary that $\varphi$ satisfy the condition:

   **F 1)** For every object $i'$ of $I'$, there exists an object $i$ of $I$ such that $\varphi(i)$ majorizes $i'$, that
   is, such that $\operatorname{Hom}(i',\varphi(i)) \neq \emptyset$.

2. Suppose $I$ is filtering. For $\varphi$ to be cofinal, it is necessary and sufficient that $\varphi$ satisfy
   condition F 1) and the following condition:

   **F 2)** For every object $i$ of $I$ and every double arrow $f',g' : i' \rightrightarrows \varphi(i)$ in $I'$, there
   exists an arrow $h : i \to j$ in $I$ such that $\varphi(h)f'=\varphi(h)g'$. Moreover, if $\varphi$ is cofinal, then
   $I'$ is filtering.

3. Suppose $I'$ is filtering and $\varphi$ is fully faithful. For $\varphi$ to be cofinal, it is necessary and
   sufficient that it satisfy condition F 1) of (1). This implies that $I$ is filtering.

**Proof.** For necessity in (1) and (2), one uses Definition 8.1.1 only in the case where $u$ is the canonical inclusion
functor (1.3.3), after choosing a universe $U$ such that $I$ and $I'$ are $U$-small. One may then interpret (8.1.1.2) as
an arrow of $\widehat{I'}$ (3.1), whose target is the final functor on $I'$ (3.4).

[PDF p. 79]

One sees immediately that condition F 1) expresses that this arrow is an epimorphism of $\widehat{I'}$, that is, that it
is surjective on each argument, taking into account that inductive limits in $\widehat{I'}$ are computed argument by
argument. This proves (1).

Now suppose $I$ is filtering and $\varphi$ cofinal. Then $I'$ is filtering. Indeed, the condition that two objects of
$I'$ be majorized by a third follows at once from the same condition for $I$ and from F 1). It remains only to prove
condition (PS 2) of 2.7: for every double arrow $f',g' : i' \rightrightarrows j'$ in $I'$, there exists an arrow
$h' : j' \to k'$ of $I'$ such that $h'f'=h'g'$. By F 1), one may suppose $k'$ is of the form $\varphi(i)$. But, by the
hypothesis that $\varphi$ is cofinal, for every object $i'$ of $I'$,

$$ \varinjlim_{i \in I} \operatorname{Hom}(i',\varphi(i)) $$

is reduced to one element. It then follows from the standard description of filtering inductive limits in $\mathbf{Ens}$
(2.8.1) that there exists an arrow $h : i \to j$ in $I$ such that $\varphi(h)f'=\varphi(h)g'$. This completes the proof
that $I'$ is filtering and at the same time proves condition F 2).

To prove that the conditions stated in (2) are sufficient for $\varphi$ to be cofinal, use form 8.1.2 of the definition.
Condition F 1) implies that (8.1.2.1) is a monomorphism, that is, injective on each argument, while condition F 2),
together with F 1), ensures that it is bijective, taking into account the calculation of projective limits argument by
argument. This proves (2).

[PDF p. 80]

Finally, if $I'$ is filtering and $\varphi$ is fully faithful, it is immediate that condition F 1) implies that $I$ is
filtering and implies condition F 2). Thus (3) follows from (1) and (2).

**8.1.4.** When $I'$ is a filtering category and $I$ a full subcategory of $I'$, it follows from 8.1.3 (3) that the
condition that $I$ be cofinal in $I'$ depends only on the subset $\operatorname{ob}(I)$ of the preordered set
$\operatorname{ob}(I')$, for the preorder relation

$$ x \leq y \quad \Longleftrightarrow \quad \operatorname{Hom}(x,y) \neq \emptyset. $$

If $J'$ is a preordered set and $J$ a subset of $J'$, we shall sometimes say that $J$ is a cofinal subset of $J'$ when
every element of $J'$ is majorized by an element of $J$. When $J'$ is filtering, this therefore means that the inclusion
functor $J \to J'$, for the associated categories, is cofinal.

**8.1.5.** In the sequel, we shall use the notion of cofinal functor only in the cases where the categories $I$ and $I'$
are filtering. Classically, one restricted even further to categories associated with preordered sets, that is, to
categories in which there is at most one arrow with given source and target. It appears, however, that this restriction
is awkward in applications, since the "natural" filtering categories introduced in many applications are not ordered
categories. The following result, due to P. Deligne, shows nevertheless that there is no essential difference between
the two points of view.

[PDF p. 81]

**Proposition 8.1.6.** Let $I$ be a small filtering category. Then there exists a small ordered set $E$ and a cofinal
functor $\varphi : E \to I$, where $E$ denotes the category associated with the ordered set $E$.

First suppose that the preordered set $\operatorname{ob}(I)$ has no greatest element. Call a **subdiagram** of $I$ a
pair $D=(O,F)$, formed by a subset $F$ of $\operatorname{Fl}(I)$ and a subset $O$ of $\operatorname{ob}(I)$, such that,
for every arrow $f \in F$, the source and target of $f$ belong to $O$. An element $e$ of $O$ is called a final object of
the subdiagram $D$ if, for every $x \in O$, the set of arrows of $D$ with source $x$ and target $e$ has exactly one
element $f_x$, if for every arrow $g : x \to y$ of $D$ one has $f_x=f_y g$, and if $f_e=\operatorname{id}_e$.

Let $E$ be the set of finite subdiagrams $D$ of $I$ having a unique final object, denoted $\varphi(D)$, and order $E$ by
inclusion. If $D \subset D'$, there exists a unique arrow $\varphi(D',D)$ of $D'$, with source $\varphi(D)$ and target
$\varphi(D')$; if one has inclusions $D \subset D' \subset D''$, one evidently has
$\varphi(D'',D)=\varphi(D'',D')\varphi(D',D)$, and $\varphi(D,D)=\operatorname{id}_{\varphi(D)}$. Thus one obtains a
functor $\varphi : E \to I$. It remains to prove that $E$ is filtering and that $\varphi$ is cofinal. Taking 8.1.3 (3)
into account, three verifications are needed.

1. Condition F 1) of 8.1.3: for every $i \in I$, take for $D$ the subdiagram of $I$ reduced to the object $i$ and its
   identity arrow; then $\varphi(D)=i$. This condition at the same time shows that $E \neq \emptyset$.

2. Condition F 2): for every $i \in \operatorname{ob}(I)$, every $D \in E$, and every double arrow
   $i \rightrightarrows \varphi(D)$, find a diagram $D' \in E$, containing $D$, such that
   $\varphi(D',D) : \varphi(D) \to \varphi(D')$ equalizes the double arrow. Since $I$ is filtering,

[PDF p. 82]

   there exists an object $j$ of $I$ and an arrow $f : \varphi(D) \to j$ which equalizes the double arrow. Since $I$ has
   no greatest element, one may suppose that $j$ is a strict majorant of $\varphi(D)$, which implies that it is distinct
   from all the other objects of $D$. Let $D'$ be the subdiagram of $I$ whose set of objects is $O \cup \{j\}$ and whose
   set of arrows is formed by the arrows of $D$, the composites $x \to \varphi(D) \to j$, where $x$ is an object of $D$,
   and $\operatorname{id}_j$. It is clear that $D'$ is a finite subdiagram of $I$, that it admits $j$ as unique final
   object, hence $D' \in E$, and that $D'$ satisfies the required condition.

3. Two subdiagrams $D,D' \in E$ are contained in a same $D'' \in E$. Indeed, one can find a strict majorant $j$ of
   $\varphi(D)$ and $\varphi(D')$, and one takes for $D''$ the subdiagram whose set of objects is the union of the
   objects of $D$, of $D'$, and of $\{j\}$, and whose set of arrows is the union of the arrows of $D$, of the arrows of
   $D'$, of the composites $x \to \varphi(D) \to j$ for $x \in D$, of the composites $x' \to \varphi(D') \to j$ for
   $x' \in D'$, and of $\operatorname{id}_j$. One thus indeed obtains a finite subdiagram of $I$.

[PDF p. 83]

It remains to show that, after replacing $j$, $f$, $f'$ by $j'$, $gf$, $gf'$ with suitable $g : j \to j'$, one can make
$j$ a final object of $D''$. This amounts to saying that, for every $x$ which is at the same time an object of $D$ and
of $D'$, one has $ff_x=f'f'_x$. Thus one has to equalize a finite set of double arrows by a morphism $g : j \to j'$,
which is possible since $I$ is filtering.

This completes the proof in the case considered. The general case is reduced to this one by introducing the filtering
category $N$ associated with the ordered set of natural integers, and observing that the category $N \times I$ is
filtering, that it has no greatest element, and that the projection $N \times I \to I$ is a cofinal functor.

**Corollary 8.1.7.** Let $I$ be a $U$-category. For there to exist a small filtering ordered set $E$ and a cofinal
functor $E \to I$, it is necessary and sufficient that $I$ be filtering and that $\operatorname{ob}(I)$ admit a small
cofinal subset (8.1.4).

This is necessary by 8.1.3 (1), and sufficient by 8.1.6 applied to the full subcategory of $I$ defined by this small
cofinal subset.

**Definition 8.1.8.** Let $I$ be a filtering category. We say that $I$ is **essentially small** if $I$ is a $U$-category
and if it satisfies the equivalent conditions of 8.1.7.

## 8.2. Ind-Objects and Ind-Representable Functors

**8.2.1.** In the sequel we fix a $U$-category $C$, which we always regard as embedded in the category $\widehat{C}$ of
$U$-presheaves by means of the canonical functor (1.3.1)

$$ h : C \to \widehat{C}. \tag{8.2.1.1} $$

We shall call an **ind-object** of $C$, or an **inductive system** of $C$, any functor

[PDF p. 84]

$$ \varphi : I \to C, \tag{8.2.1.2} $$

where $I$ is a filtering category (2.7), called the index category of the ind-object. The category $I$ is otherwise
arbitrary; in particular, we do not require it to be a $U$-category.

It will often be convenient to denote an ind-object $\varphi$ by the indexed notation
$(X_i)_{i \in \operatorname{ob}(I)}$, or even, by a further abuse of notation, by $(X_i)_{i \in I}$ or $(X_i)$, where
$X_i=\varphi(i)$ for $i \in \operatorname{ob}(I)$. This notation is no more and no less abusive than the classical
notation for inductive systems indexed by filtering ordered sets, where the transition morphisms are likewise not
mentioned. The $X_i$ are called the component objects of the ind-object $X$.

It should be noted that, in the general case considered here, the "transition morphisms" of the inductive system are
indexed by the set $\operatorname{Fl}(I)$ of arrows of $I$, which is not generally identified with a subset of
$\operatorname{ob}(I) \times \operatorname{ob}(I)$. In other words, for given $i$ and $j$, with $j$ majorizing $i$,
there may exist more than one transition morphism from $X_i$ to $X_j$.

**8.2.2.** The most useful ind-objects $X=(X_i)_{i \in I}$ of $C$ are those for which the index category $I$ is
essentially small (8.1.8); such an ind-object is called **essentially small**. If $X=(X_i)_{i \in I}$ is such, then,
using the fact that in $\widehat{C}$ small inductive limits are representable (3.1), one may consider

$$ L(X)=\varinjlim_I h(X_i) \in \operatorname{ob}(\widehat{C}). \tag{8.2.2.1} $$

The limit is taken in $\widehat{C}$. Thus $L(X)$ is the presheaf

[PDF p. 85]

$$ L(X) : Y \mapsto \varinjlim_I \operatorname{Hom}(Y,X_i). \tag{8.2.2.2} $$

We say that this presheaf is **ind-represented** by the ind-object $X=(X_i)_{i \in I}$ of $C$. A presheaf $F$ on $C$ is
called **ind-representable** if it is isomorphic to a presheaf $L(X)$ ind-represented by an essentially small
ind-object. It follows moreover from 8.1.6 that, in this definition, one may suppose that $I$ is a small category, and
even that $I$ is associated with an ordered set belonging to $U$.

**8.2.3.** Consider an ind-object $X=(X_i)_{i \in I}$ given by a functor $\varphi : I \to C$, and let

$$ u : I' \to I $$

be a functor, where $I'$ is a second filtering category. Then the functor $\varphi \circ u$ is an ind-object $X'$ of
$C$, with index category $I'$, which in indexed notation is written $(X_{u(i')})_{i' \in I'}$. It is called the
ind-object of $C$ deduced from $X$ by change of index categories by means of the functor $u$.

If $I$ and $I'$, that is, $X$ and $X'$, are essentially small, one obtains a canonical morphism

$$ L(X') \to L(X) \tag{8.2.3.1} $$

between the presheaves ind-represented by $X'$ and $X$. When $u$ is a cofinal functor (8.1.1), then $X$ is essentially
small if and only if $X'$ is (8.1.7), and the preceding morphism is an isomorphism

$$ L(X') \simeq L(X). \tag{8.2.3.2} $$

[PDF p. 86]

**8.2.4.** Let

$$ X=(X_i)_{i \in I},\qquad Y=(Y_j)_{j \in J} \tag{8.2.4.1} $$

be two essentially small ind-objects of $C$, indexed by essentially small filtering categories $I$ and $J$. A
**morphism** from the ind-object $X$ to the ind-object $Y$ is a morphism

$$ L(X) \to L(Y) \tag{8.2.4.2} $$

between the presheaves which they ind-represent. We put

$$ \operatorname{Hom}_{\operatorname{ind\text{-}ob}}(X,Y)=\operatorname{Hom}_{\widehat{C}}(L(X),L(Y)). \tag{8.2.4.3} $$

We omit the subscript $\operatorname{ind\text{-}ob}$ from $\operatorname{Hom}$ if no confusion is to be feared. The
composition of morphisms between ind-objects of $C$ is defined as the composition of morphisms of the presheaves which
they ind-represent.

If $V \supset U$ is a universe containing $U$, and if one restricts to essentially small ind-objects which belong to
$V$, these therefore form the set of objects of a category. Its set of arrows is formed by triples $(X,Y,u)$, where $X$
and $Y$ are essentially small ind-objects belonging to $V$ and where $u : X \to Y$ is a morphism of ind-objects, that
is, a morphism $L(X) \to L(Y)$. The category thus obtained is denoted

$$ \operatorname{Ind}_V(C,U). \tag{8.2.4.4} $$

When $V=U$, it is denoted simply

$$ \operatorname{Ind}_U(C)\quad \text{or}\quad \operatorname{Ind}(C), \tag{8.2.4.5} $$

and is called the **category of ind-objects of $C$ relative to $U$**, with the mention of $U$ suppressed when no
confusion is to be feared.

[PDF p. 87]

Evidently, if $V \subset V'$ are two universes containing $U$, then $\operatorname{Ind}_V(C,U)$ is a full subcategory of
$\operatorname{Ind}_{V'}(C,U)$; it follows from 8.2.3 that the inclusion functor is an equivalence of categories:

$$ \operatorname{Ind}_V(C,U) \to \operatorname{Ind}_{V'}(C,U). \tag{8.2.4.6} $$

This shows in particular that every essentially small ind-object of $C$ defines an object of $\operatorname{Ind}(C)$, up
to unique isomorphism. This observation justifies the abuse of language, quite common in practice, which consists in
identifying every essentially small ind-object of $C$ with an object of $\operatorname{Ind}(C)$.

It follows at once from the definitions that, for every universe $V \supset U$, we have a canonical functor

$$ L : \operatorname{Ind}_V(C,U) \to \widehat{C} \tag{8.2.4.7} $$

which is fully faithful. These functors are evidently known up to unique isomorphism by (8.2.4.6). When one knows one of
them, and in particular when one knows the canonical functor

$$ L : \operatorname{Ind}(C) \to \widehat{C}, \tag{8.2.4.8} $$

since this functor is fully faithful, it is frequently used to identify an object of the first member with the functor
it ind-represents, or even to identify $\operatorname{Ind}(C)$ with its essential image in $\widehat{C}$, formed by the
ind-representable presheaves. One should note, however, that this identification has distinctly more drawbacks than the
analogous identification of $C$ with a full subcategory of $\widehat{C}$ by the functor $h$ (8.2.1.1), because, unlike
the latter, the functor (8.2.4.8) is not generally injective on objects.

[PDF p. 88]

**8.2.5.** Let us spell out definition (8.2.4.3) in terms of the indexed expressions (8.2.4.1) of the ind-objects
considered. Taking definition (8.2.2.1) into account, one finds a canonical bijection

$$
\operatorname{Hom}((X_i)_{i \in I},(Y_j)_{j \in J})
=
\varprojlim_{i \in I}\varinjlim_{j \in J}\operatorname{Hom}_C(X_i,Y_j). \tag{8.2.5.1}
$$

We leave to the reader the task of spelling out the composition of morphisms of ind-objects by means of this formula.
Note that it follows at once from this formula that the set $\operatorname{Hom}(X,Y)$ of homomorphisms of ind-objects is
$U$-small, that is, that the categories (8.2.4.4) are $U$-categories. Equivalently, by (8.2.4.6), the category
$\operatorname{Ind}(C)$ is a $U$-category: the second member of (8.2.5.1) is small when $I,J \in U$, which follows at
once from the fact that $C$ is a $U$-category, hence that the $\operatorname{Hom}_C(X_i,Y_j)$ are small.

**8.2.6.** Let $I$ be an essentially small filtering category. Then one sees from (8.2.5.1), or from the functoriality
of the inductive limit of a functor $I \to \widehat{C}$ with respect to that functor, that one has a canonical functor

$$ \operatorname{Hom}(I,C) \to \operatorname{Ind}(C). \tag{8.2.6.1} $$

One should note that this functor is not generally fully faithful, or even faithful.

[PDF p. 89]

**Remark 8.2.7.** The definitions of 8.2.4 make clear the notion of isomorphism of two essentially small ind-objects: it
also means the isomorphism of the presheaves which they ind-represent. One should note that this is a very weak notion
of isomorphism compared with the notion of isomorphism in categories of the form $\operatorname{Hom}(I,C)$. Thus a large
number of fairly natural relations one can impose on an ind-object, such as having its components in a given strictly
full subcategory, or being strict (8.12 below), are not stable under isomorphism.

Therefore, if one wants to work with notions stable under isomorphism of ind-objects, one must "saturate" the notions in
question by passing to the strictly full subcategory of $\operatorname{Ind}(C)$ generated by the subcategory of
$\operatorname{Ind}(C)$ formed by the objects satisfying the condition in question. See, for example, the notion of
essentially constant ind-object introduced below (8.4).

**Exercise 8.2.8.** Let $U \subset V$ be two universes and let $C$ be a $U$-category which belongs to $V$. Denote by
$\operatorname{SysInd}(C)$ the following category.

1. The objects of $\operatorname{SysInd}(C)$ are the functors $\varphi : I \to C$, where $I$ is a filtering, essentially
   $U$-small category belonging to $V$.

2. Let $(I,\varphi)$ and $(J,\psi)$ be two objects of $\operatorname{SysInd}(C)$. A morphism of
   $\operatorname{SysInd}(C)$ from $(I,\varphi)$ to $(J,\psi)$ is a pair $(m,u)$, where $m : I \to J$ is a functor and
   $u : \varphi \to \psi \circ m$ is a morphism of functors. Composition of morphisms in $\operatorname{SysInd}(C)$ is
   defined in the evident way.

[PDF p. 90]

Let $S$ denote the set of morphisms $(m,u):(I,\varphi) \to (J,\psi)$ of $\operatorname{SysInd}(C)$ such that $m$ is
cofinal and $u$ is an isomorphism. Let $(I,\varphi)$ be an object of $\operatorname{SysInd}(C)$. The category
$\operatorname{Fl}(I)$ of arrows of $I$ maps by two natural functors to $I$: source and target. Moreover, these two
functors are related by the canonical morphism of functors

$$ v : \operatorname{source} \to \operatorname{target}. $$

Hence there are two morphisms in $\operatorname{SysInd}(C)$ from
$(\operatorname{Fl}(I),\varphi \circ \operatorname{source})$ to $(I,\varphi)$:

$$
p_1(I,\varphi)=(\operatorname{source},\operatorname{id}),
\qquad
p_2(I,\varphi)=(\operatorname{target},\varphi(v):\varphi \circ \operatorname{source}\to
\varphi \circ \operatorname{target}).
$$

Let $p : \operatorname{SysInd}(C) \to \operatorname{Ind}(C)$ be the evident functor. Let $B$ be a category. Show that
the functor

$$ p^* : \operatorname{Hom}(\operatorname{Ind}(C),B) \to \operatorname{Hom}(\operatorname{SysInd}(C),B) $$

is fully faithful, and that a functor $G : \operatorname{SysInd}(C) \to B$ belongs to its essential image if and only if
it has the following two properties:

1. For every $s \in S$, $G(s)$ is an isomorphism of $B$.
2. For every object $(I,\varphi)$ of $\operatorname{SysInd}(C)$, $G(p_1(I,\varphi))=G(p_2(I,\varphi))$.

# 8.3. Characterization of Ind-Representable Functors

**Proposition 8.3.1.** Let $F$ be an ind-representable presheaf on $C$. Then $F$ is left exact, that is (2.3.2), for
every finite category $J$ and every functor $\varphi : J \to C$ such that $\varprojlim \varphi$ is representable (that
is, such that $\varprojlim \varphi^\circ$ is representable), the canonical map

$$ F(\varprojlim \varphi) \to \varprojlim F \circ \varphi $$

is bijective.

[PDF p. 91]

Indeed, since representable presheaves are evidently left exact, it follows at once from 2.8 that the same is true of
every filtering inductive limit of such functors.

**8.3.2.** Given a presheaf $F$ on $C$, we shall often have to work with the category

$$ C/F \subset \widehat{C}/F, \tag{8.3.2.1} $$

which denotes the full subcategory of the second member formed by the arrows $X \to F$ with source in $C$. It follows
from 1.4 that the objects of this category are identified with pairs $(X,u)$, where $X$ is an object of $C$ and
$u \in F(X)$. A morphism from $(X,u)$ to $(X',u')$ is then interpreted as an arrow $f : X \to X'$ in $C$ such that
$F(f)(u')=u$. The "forget the target" functor from $\widehat{C}/F$ to $\widehat{C}$ induces a functor, called canonical,

$$ C/F \to C, \tag{8.3.2.2} $$

already considered in 3.4, where it is proved that the inductive limit of this functor exists in $\widehat{C}$ (with no
smallness condition on $C/F$) and is canonically isomorphic to $F$.

**8.3.2.3.** Note that, if finite inductive limits are representable in $C$, and if $F$ is left exact (that is,
transforms them into finite projective limits of $\mathbf{Ens}$), then the same is true in $C/F$; a fortiori (2.7.1),
$C/F$ is filtering. More generally, if sums of two objects and cokernels of double arrows are representable in $C$, and
if $F$ transforms them respectively into products and kernels,

[PDF p. 92]

then $C/F$ is stable under the same types of finite inductive limits. Thus it is filtering if and only if it is
nonempty, that is, if and only if the functor $F$ is not the constant functor with value $\emptyset$.

**Theorem 8.3.3.** Let $C$ be a $U$-category, and let $F \in \operatorname{ob}(\widehat{C})$, in other words let
$F : C^\circ \to U\text{-}\mathbf{Ens}$ be a $U$-presheaf on $C$. The following conditions are equivalent:

1. $F$ is ind-representable (8.2.2).
2. The category $C/F$ (8.3.2) is filtering and essentially small.
3. If finite inductive limits are representable in $C$, the functor $F$ is left exact, and $\operatorname{ob}(C/F)$
   admits a small cofinal subset (8.1.4).
4. If sums of two objects and cokernels of double arrows are representable in $C$, the functor $F$ transforms sums of
   two objects of $C$ into products and cokernels of double arrows of $C$ into kernels; the category $C/F$ is nonempty,
   that is, $F$ is not the constant functor with value $\emptyset$; finally, there exists a small family of objects
   $(X_i)$ of $C/F$ such that every object $X$ of $C/F$ is majorized by an object $X_i$, that is, admits an $F$-morphism
   $X_i \to X$.
5. If the category $C$ is equivalent to a small category, the category $C/F$ is filtering.
6. If the category $C$ is equivalent to a small category and if filtering inductive limits are representable in it, the
   functor $F$ is left exact.

[PDF p. 93]

**Proof.** $(1) \Rightarrow (2)$. Suppose $F$ is ind-represented by $(X_i)_{i \in I}$, with $I$ small. Let us prove that
$C/F$ is filtering. Let $X,X'$ be two objects of $C/F$, that is, objects of $C$ equipped with morphisms $X \to F$ and
$X' \to F$. These morphisms come from morphisms $X \to X_i$ and $X' \to X_{i'}$; after replacing $i$ and $i'$ by a
common majorant in $\operatorname{ob}(I)$, one may suppose $i=i'$, and one takes as common majorant of $X$ and $X'$ the
object $X_i$, equipped with the canonical morphism $X_i \to F$.

Now let $X \rightrightarrows X' \to F$ be a double arrow in $C/F$. Let us prove that it is equalized by an arrow
$X' \to X''$ of $C/F$. The morphism $h : X' \to F$ is given by a morphism $h_i : X' \to X_i$, and the condition $hf=hg$
means that there exists an arrow $\alpha : i \to j$ in $I$ such that $\alpha h_i f=\alpha h_i g$. Thus, after replacing
$h_i$ by $\alpha h_i$, one equalizes $f$ and $g$. This proves that $C/F$ is filtering. It is then immediate that it is
essentially small, since the objects $X_i \to F$, for $i \in \operatorname{ob}(I)$, form a small cofinal family in
$\operatorname{ob}(C/F)$.

$(2) \Rightarrow (1)$. Put $I=C/F$ and consider the canonical functor (8.3.2.2)

$$ C/F \to C. $$

We know that the presheaf represented by this ind-object of $C$ is $F$ (3.4). Thus $F$ is ind-representable by
definition (8.2.2).

$(2) \Longleftrightarrow (3)$. Indeed, $(2) \Rightarrow (3)$ because an ind-representable functor is left exact (8.3.1),
and $(3) \Rightarrow (2)$ because we observed in 8.3.2.3 that $F$ left exact implies that $C/F$ is filtering,

[PDF p. 94]

and one applies Definition 8.1.8 to conclude that this category is essentially small.

The equivalence $(2) \Longleftrightarrow (4)$ is proved in the same way as $(2) \Longleftrightarrow (3)$. The
equivalences $(2) \Longleftrightarrow (5)$ and $(3) \Longleftrightarrow (6)$ are trivial, since, for $C$ equivalent to a
small category, $C/F$ is evidently also equivalent to a small category and, a fortiori, is automatically essentially
small as soon as it is filtering. This completes the proof of 8.3.3.

**Remark 8.3.4.** Let $F : C' \to C''$ be a functor between $U$-categories. It appears that the notion of left exactness
(2.3.2) is of little practical interest unless finite projective limits are representable in $C'$. In the case where
$C''=U\text{-}\mathbf{Ens}$ and $C'$ is $U$-small, writing $C'$ in the form $C^\circ$, one should regard the "right
notion" which replaces, in the general case, that of left exactness as the ind-representability of $F$, considered as a
presheaf on $C$, that is, as the pro-representability of $F$, considered as a functor on $C'$ (cf. 8.10). This notion
does coincide with that of left exactness when finite projective limits are representable in $C'$, that is, when finite
inductive limits are representable in $C$ (8.3.3).

When one no longer assumes $C'$ to be $U$-small, or at least equivalent to a $U$-small category, the two notions, for a
functor $F$, of left exactness and pro-representability need no longer coincide, even if finite projective limits are
representable in $C'$ (cf. 8.12.9). In fact, in this case, it seems that left exact functors which are not
ind-representable should be regarded as pathological in nature, the "good" objects remaining the ind-representable
functors; compare 8.13.3. For the case of functors $F : C' \to C''$, with $C'$ and $C''$ again arbitrary $U$-categories,
we shall develop below (8.11.5) a more general notion improving that of left exactness, namely that of a functor
admitting a pro-adjoint functor.

# 8.4. Constant and Essentially Constant Ind-Objects

Choose a final category $e$, that is, one for which $\operatorname{ob}(e)$ and $\operatorname{Fl}(e)$ are each reduced
to one element. For example, one may take for $e$ the full subcategory of $\mathbf{Ens}$ formed by the empty set, if one
wants a canonical choice. This is evidently a small filtering category. If $X$ is an object of $C$, one associates to it
the constant ind-object indexed by $e$, with value $X$, namely $c(X)$. It is clear that, for variable $X$, this gives a
fully faithful functor

$$ c : C \to \operatorname{Ind}(C), \tag{8.4.1} $$

which is moreover injective on objects, and by which we shall identify $C$ with a full subcategory of
$\operatorname{Ind}(C)$. Note that the composite functor

$$ C \to \operatorname{Ind}(C) \to \widehat{C} \tag{8.4.2} $$

is the canonical functor $h$ (8.2.1.1).

[PDF p. 96]

**8.4.3.** More generally, let $I$ be a filtering category. The constant functor on $I$ with value an object $X$ of $C$
is also called the constant ind-object of value $X$ indexed by $I$. It is clear, if $I$ is essentially small, that this
ind-object ind-represents the functor $h(X)$ represented by $X$; hence this ind-object is isomorphic to $c(X)$.

**8.4.4.** An ind-object $X$ of $C$ is said to be **essentially constant** if it is isomorphic, in a category
$\operatorname{Ind}_V(C,U)$ for suitable universes $V,U$, to an ind-object of the form $c(X_0)$, with
$X_0 \in \operatorname{ob}(C)$. The object $X_0$, then determined up to canonical isomorphism, is called the value of
the essentially constant ind-object in question. Thus, by definition, the functor $c$ of (8.4.1) induces an equivalence
of $C$ with the full subcategory of $\operatorname{Ind}(C)$ formed by the essentially constant ind-objects, this
subcategory being the essential image of the functor $c$.

Evidently, a constant ind-object is essentially constant. The converse is true only in the trivial case where $C$ is
empty or a punctual category.

# 8.5. Filtering Inductive Limits in $\operatorname{Ind}(C)$

**Proposition 8.5.1.** Let $C$ be a $U$-category. In $\operatorname{Ind}(C)$, small filtering inductive limits are
representable, and the canonical functor (8.2.4.8)

$$ L : \operatorname{Ind}(C) \to \widehat{C} $$

commutes with these limits.

[PDF p. 97]

Taking into account the fact that $L$ is fully faithful, the assertions of the proposition are equivalent to the
following one.

**Corollary 8.5.2.** Every small filtering inductive limit, in $\widehat{C}$, of ind-representable presheaves is
ind-representable.

This follows easily from criterion 8.3.3 (2). The details of the verification are left to the reader.

**8.5.3.** The "tautological" case of filtering inductive limits in $\operatorname{Ind}(C)$ is the one where one starts
from an essentially small ind-object $X=(X_i)_{i \in I}$ of $C$. Then, in $\widehat{C}$, hence also in
$\operatorname{Ind}(C)$, one has:

$$ X=\varinjlim_{i \in I} X_i. \tag{8.5.3.1} $$

When writing this formula, one should note that this is not an inductive limit in $C$, and that, even when the latter
exists, it is not isomorphic in $\operatorname{Ind}(C)$ to $X$. Indeed, the canonical functor (8.4.1)
$c : C \to \operatorname{Ind}(C)$ does not generally commute with filtering inductive limits (cf. 8.5.5 below).

To avoid this possible confusion in writing (8.5.3.1), "certain authors" (= P. Deligne) prefer to write it

$$ X=\text{``}\varinjlim\text{''}_{i \in I} X_i, \tag{8.5.3.2} $$

the role of the quotation marks being to indicate that the inductive limit is taken in a category of ind-objects
$\operatorname{Ind}(C)$. By extension, one would then have to denote by $\text{``}\varinjlim\text{''}$ every inductive
limit operation in $\operatorname{Ind}(C)$, without the components of the inductive system considered in
$\operatorname{Ind}(C)$ necessarily being in the image, or the essential image, of $c : C \to \operatorname{Ind}(C)$.

[PDF p. 98]

**8.5.4.** To compute the inductive or projective limit of a functor

$$ \varphi : J \to \operatorname{Ind}(C), \tag{8.5.4.1} $$

where $J$ is now an arbitrary category, it is often convenient to spell out $\varphi$ by means of a functor

$$ \Phi : J \times I \to C, \tag{8.5.4.2} $$

where $I$ is an essentially small, or preferably small, filtering category. Such a $\Phi$ indeed defines a functor

$$ j \mapsto (i \mapsto \Phi(j,i)) : J \to \operatorname{Hom}(I,C), $$

hence, composing with the canonical arrow (8.2.6.1) $\operatorname{Hom}(I,C) \to \operatorname{Ind}(C)$, a functor

$$ j \mapsto (i \mapsto \Phi(j,i)) : J \to \operatorname{Ind}(C). \tag{8.5.4.3} $$

We may say that $\Phi$ is an **indexed expression** of $\varphi$, indexed by the filtering category $I$, if the
corresponding functor (8.5.4.3) is isomorphic to $\varphi$. Below (8.8) we shall study general conditions for the
existence of an indexed expression for a given functor $\varphi$. Here we simply start from a functor $\varphi$ given in
indexed form (8.5.4.3), in the case where $J$ is a small filtering category, to indicate the computation of
$\text{``}\varinjlim\text{''}_J\varphi=\text{``}\varinjlim\text{''}_j\varphi(j)$.

Formula (8.5.3.2) and the associativity formula for inductive limits (2.5.0) then immediately give the "tautological
calculation" of $\text{``}\varinjlim\text{''}\varphi$:

$$
\text{``}\varinjlim\text{''}_{j \in J}\varphi
=
\text{``}\varinjlim\text{''}_{(j,i) \in J \times I}\Phi, \tag{8.5.4.4}
$$

[PDF p. 99]

that is,

$$
\text{``}\varinjlim\text{''}_{j \in J}(i \mapsto \Phi(j,i))
=
\text{``}\varinjlim\text{''}_{(j,i) \in J \times I}\Phi(j,i). \tag{8.5.4.5}
$$

Thus the desired inductive system is none other than $\Phi$ itself, the index category being $J \times I$, which is
indeed filtering since $J$ and $I$ are.

**Exercise 8.5.5.** Let $C$ be a $U$-category.

1. Prove that the following conditions are equivalent:

   1. In $C$, small inductive limits are representable, and the functor $c : C \to \operatorname{Ind}(C)$ commutes with
      them.
   2. In $C$, small inductive limits are representable, and, for every $X \in \operatorname{ob}(C)$, the functor
      $Y \mapsto \operatorname{Hom}(X,Y)$ commutes with said limits.
   3. The functor $c$ is an equivalence of categories.
   4. Small filtering inductive limits are representable in $C$, and the functor
      $\varinjlim c : \operatorname{Ind}(C) \to C$ (cf. 8.7.1.5) is fully faithful, or equivalently an equivalence.

2. If $C$ is a finite category, prove that the preceding conditions are equivalent to the following one: for every
   projector in $C$ (10.6), the image is representable in $C$.

# 8.6. Extension of a Functor to Ind-Objects

**8.6.1.** Let

$$ f : C \to C' \tag{8.6.1.1} $$

be a functor between $U$-categories. For every ind-object

$$ \varphi : I \to C $$

of $C$, where $I$ is a filtering category, the composite functor $f \circ \varphi$ is an ind-object of $C'$, also
denoted $\operatorname{Ind}(f)(\varphi)$. In indexed notation, if $\varphi$ is written in the form $X=(X_i)_{i \in I}$,
one obtains

[PDF p. 100]

$$ \operatorname{Ind}(f)((X_i)_{i \in I})=(f(X_i))_{i \in I}. \tag{8.6.1.2} $$

Let $Y=(Y_j)_{j \in J}$ be a second inductive system of $C$. One then obtains an evident map, also denoted
$u \mapsto \operatorname{Ind}(f)(u)$:

$$
\operatorname{Hom}(X,Y)
=
\varprojlim_i \varinjlim_j \operatorname{Hom}_C(X_i,Y_j)
\to
\operatorname{Hom}(\operatorname{Ind}(f)(X),\operatorname{Ind}(f)(Y))
\simeq
\varprojlim_i \varinjlim_j \operatorname{Hom}_{C'}(f(X_i),f(Y_j)). \tag{8.6.1.3}
$$

One immediately observes that these maps are compatible with composition of morphisms of ind-objects, by referring to
the unwritten formula for the composition of morphisms of ind-objects (8.2.5). Thus one has obtained, for every universe
$V$, a functor

$$ \operatorname{Ind}(f) : \operatorname{Ind}_V(C,U) \to \operatorname{Ind}_V(C',U), \tag{8.6.1.4} $$

with the notation of (8.2.4.5), and in particular a functor

$$ \operatorname{Ind}(f) : \operatorname{Ind}(C) \to \operatorname{Ind}(C'). \tag{8.6.1.5} $$

If one has a second functor

$$ g : C' \to C'', $$

one evidently has an identity of functors between $\operatorname{Ind}$ categories, or $\operatorname{Ind}_V$ categories
as desired:

$$ \operatorname{Ind}(gf)=\operatorname{Ind}(g) \circ \operatorname{Ind}(f), \tag{8.6.1.6} $$

[PDF p. 101]

and, for $C'=C$, the formula

$$ \operatorname{Ind}(\operatorname{id}_C)=\operatorname{id}_{\operatorname{Ind}(C)}. \tag{8.6.1.7} $$

Pictorially, one may therefore say that the category $\operatorname{Ind}(C)$ depends functorially on $C$, covariantly.
We leave to the reader the task of spelling out even a 2-functorial dependence, by defining, for every pair of
$U$-categories $C,C'$, a canonical functor

$$ \operatorname{Ind}(f) : \operatorname{Hom}(C,C') \to \operatorname{Hom}(\operatorname{Ind}(C),\operatorname{Ind}(C')),
\tag{8.6.1.8}
$$

and by specifying the functorial nature of the identical isomorphisms (8.6.1.6) and (8.6.1.7).

**8.6.2.** Take up again the functor (8.6.1.1), and consider the corresponding functor (5.1)

$$ f_! : \widehat{C} \to \widehat{C'}, \tag{8.6.2.1} $$

and the diagram of functors

```text
Ind(C)  --Ind(f)-->  Ind(C')
  | L_C                | L_{C'}
  v                    v
 C^      --f_!-->     C'^ .                     (8.6.2.2)
```

where the vertical arrows denote the canonical functors $L$ of (8.2.4.8). Since the functor $f_!$ "extends $f$" and
commutes with inductive limits (5.4.3), and since the functors $L_C$ and $L_{C'}$ commute with small filtering inductive
limits (8.5.1), it follows from (8.5.3.2) that, for every ind-object $(X_i)_{i \in I}$ of $C$, one has in $\widehat{C'}$
a canonical isomorphism

[PDF p. 102]

$$
\begin{aligned}
f_!(L_C((X_i)_{i \in I}))
&\simeq \varinjlim_i f_!L_C(X_i) \\
&\simeq \varinjlim_i L_{C'}f(X_i) \\
&= L_{C'}((f(X_i))_{i \in I}),
\end{aligned}
$$

that is, a canonical isomorphism

$$ f_!L_C(X) \simeq L_{C'}(\operatorname{Ind}(f)(X)). $$

We leave to the reader the task of checking that the latter is functorial, that is, that it corresponds to a canonical
isomorphism

$$ f_!L_C \simeq L_{C'} \circ \operatorname{Ind}(f). \tag{8.6.2.3} $$

In other words, square (8.6.2.2) is commutative up to canonical isomorphism. Taking into account the fact that $f_!$
commutes with small inductive limits, and 8.5.1, we conclude from this.

**Proposition 8.6.3.** Let $f : C \to C'$ be a functor between $U$-categories. Then the functor

$$ \operatorname{Ind}(f) : \operatorname{Ind}(C) \to \operatorname{Ind}(C') $$

commutes with filtering inductive limits. Moreover, it makes the following diagram commutative:

```text
C       --f-->      C'
| c_C              | c_{C'}
v                  v
Ind(C) --Ind(f)--> Ind(C'),
```

where the vertical arrows $c_C$, $c_{C'}$ are the canonical functors (8.4.1).

The last assertion is trivial from the definitions, and has been included for convenient reference. Note moreover that
the properties stated in 8.6.3 characterize the functor $\operatorname{Ind}(f)$ up to unique isomorphism, as being
induced by the functor $f_!$ (8.6.2.1), as follows from the proof just given of (8.6.2.3).

[PDF p. 103]

**Proposition 8.6.4.** The notation is that of 8.6.3.

1. For $\operatorname{Ind}(f)$ to be faithful, respectively fully faithful, it is necessary and sufficient that $f$ be
   so.
2. For $\operatorname{Ind}(f)$ to be an equivalence of categories, it is necessary and sufficient that $f$ be fully
   faithful and that every object of $C'$ be isomorphic to a direct factor (10.6) of an object in the image of $f$.

**Proof.** For (1), necessity follows evidently from the fact that $f$ is induced by $\operatorname{Ind}(f)$. For
sufficiency, it suffices to use the form (8.6.1.3) of $\operatorname{Ind}(f)$ on the sets $\operatorname{Hom}(X,Y)$,
remembering that filtering inductive limits of sets, and arbitrary projective limits, transform monomorphisms into
monomorphisms and isomorphisms into isomorphisms.

For (2), one may suppose already that $f$, hence $\operatorname{Ind}(f)$, is fully faithful. Since every object of
$\operatorname{Ind}(C')$ is a small filtering inductive limit of objects of $C'$, full faithfulness of
$\operatorname{Ind}(f)$ implies that, for this functor to be essentially surjective, it is equivalent that every object
$X'$ of $C'$ lie in the essential image. But if one has an isomorphism

$$ X' \simeq \text{``}\varinjlim\text{''} f(X_i), $$

this isomorphism factors through one of the $f(X_i)$, which shows that $X'$ is a direct factor of $f(X_i)$, proving
necessity in (2). Sufficiency follows at once from full faithfulness of $\operatorname{Ind}(f)$ and from stability of
ind-objects under images of projectors, made explicit in the following corollary.

[PDF p. 104]

**Corollary 8.6.5.** In $\operatorname{Ind}(C)$, images of projectors (10.6) are representable, and the functor
$\operatorname{Ind}(f) : \operatorname{Ind}(C) \to \operatorname{Ind}(C')$ commutes with the formation of these images.

Indeed, this follows from the fact that, in $\operatorname{Ind}(C)$, small filtering inductive limits are representable
(8.5.1) and that $\operatorname{Ind}(f)$ commutes with them (8.6.3), taking into account that the image of a projector
$p : X \to X$ is interpreted as the inductive limit of a filtering inductive system indexed by $N$

$$ X \xrightarrow{p} X \xrightarrow{p} X \to \cdots $$

or, alternatively, as the inductive limit of the evident functor on the filtering category $P$ having one object and one
nonidentity arrow $\pi$ such that $\pi^2=\pi$.

# 8.7. The Functor $\varinjlim_C : \operatorname{Ind}(C) \to C$. Universal Characterizations of the Category
$\operatorname{Ind}(C)$

**8.7.1.** Take up again a $U$-category $C$, and the canonical functor

$$ c : C \to \operatorname{Ind}(C). \tag{8.7.1.1} $$

Let $X=(X_i)_{i \in I}$ be an object of $\operatorname{Ind}(C)$. It follows immediately from the definition of
representable inductive limits (2.1, 2.1.1) that $\varinjlim_i X_i$ is representable in $C$ if and only if the left
adjoint of $c$ is defined at $X$, and that, in this case, $\varinjlim_i X_i$, computed in $C$, is precisely the value at
$X$ of said left adjoint:

$$
\operatorname{Hom}_C(\varinjlim_i X_i,Y)
\simeq
\operatorname{Hom}_{\operatorname{Ind}(C)}((X_i)_{i \in I},c(Y)). \tag{8.7.1.2}
$$

[PDF p. 105]

If one denotes by

$$ \operatorname{Ind}(C)' \subset \operatorname{Ind}(C) \tag{8.7.1.3} $$

the full subcategory of $\operatorname{Ind}(C)$ formed by the ind-objects of $C$ which admit an inductive limit in $C$,
it follows from the preceding observation that this subcategory is strictly full, and that one has a canonical functor

$$ \varinjlim_C : \operatorname{Ind}(C)' \to C, \tag{8.7.1.4} $$

whose value at each object $(X_i)_{i \in I}$ of $\operatorname{Ind}(C)'$ is its inductive limit in $C$. In the special
case where, in $C$, small filtering inductive limits are representable, one therefore obtains a natural functor

$$ \varinjlim_C : \operatorname{Ind}(C) \to C. \tag{8.7.1.5} $$

**8.7.1.6.** Of course, the preceding functors can also be defined on categories of the type
$\operatorname{Ind}_V(C,U)'$ and $\operatorname{Ind}_V(C,U)$, but, taking (8.2.4.6) into account, they are already
determined, up to unique isomorphism, by knowing the preceding functors corresponding to the case $V=U$.

**8.7.1.7.** From the preceding construction of $\varinjlim_C$ as a left adjoint functor, it follows immediately that
this functor commutes with arbitrary inductive limits, and in particular with small filtering inductive limits, the
latter being representable in $\operatorname{Ind}(C)$ (8.5.1). Note also that $\operatorname{Ind}(C)'$ always contains
the essential image of $c$, formed by the essentially constant ind-objects, and that one has a canonical isomorphism
functorial in $X \in \operatorname{ob}\operatorname{Ind}(C)'$:

[PDF p. 106]

$$ \varinjlim_C c(X) \simeq X. \tag{8.7.1.8} $$

In the favorable case where $C$ is stable under small inductive limits, one therefore has a canonical isomorphism

$$ \varinjlim_C \circ c \simeq \operatorname{id}_C. \tag{8.7.1.9} $$

**8.7.2.** Now consider a functor

$$ f : C \to E, \tag{8.7.2.1} $$

where $E$ is a $U$-category in which small inductive limits are representable, so that one has a functor

$$ \varinjlim_E : \operatorname{Ind}(E) \to E. $$

Since we have also defined (8.6)

$$ \operatorname{Ind}(f) : \operatorname{Ind}(C) \to \operatorname{Ind}(E), $$

we may consider the composite

$$ \overline{f}=\varinjlim_E \circ \operatorname{Ind}(f) : \operatorname{Ind}(C) \to E, \tag{8.7.2.2} $$

which is sometimes called the **canonical extension** of $f$ to ind-objects, but which one should not confuse with
$\operatorname{Ind}(f)$. As a composite of two functors commuting with small filtering inductive limits (8.6.3,
8.7.1.7), this functor itself commutes with small filtering inductive limits. Moreover, it follows from isomorphism
(8.7.1.9) applied to $E$, and from (8.6.2.3), that $\overline{f}$ extends $f$ up to isomorphism, that is, one has a
canonical isomorphism

$$ \overline{f} \circ c_C \simeq f. \tag{8.7.2.3} $$

[PDF p. 107]

It is moreover fairly clear, taking into account the fact that every object of $\operatorname{Ind}(C)$ is a small
filtering inductive limit of objects of $C$, that the two preceding properties still characterize $\overline{f}$, up to
unique isomorphism. One can make this precise and at the same time obtain a universal characterization, up to
equivalence, of $\operatorname{Ind}(C)$ among the $U$-categories $E$ in which small filtering inductive limits are
representable. If $E$ and $F$ are two such $U$-categories, denote by

$$ \operatorname{Hom}(E,F)' \subset \operatorname{Hom}(E,F) \tag{8.7.2.4} $$

the full subcategory of $\operatorname{Hom}(E,F)$ formed by the functors which commute with small filtering inductive
limits. Then:

**Proposition 8.7.3.** Let $C$ be a $U$-category, and use the notation above (8.7.2.4). Then the canonical functor

$$ c_C : C \to \operatorname{Ind}(C) $$

is 2-universal among functors with source $C$ and target a $U$-category with representable small filtering inductive
limits. In other words, $\operatorname{Ind}(C)$ is such a category (8.2.5, 8.5.1), and, if $E$ is such a category, the
functor

$$ g \mapsto g \circ c_C : \operatorname{Hom}(\operatorname{Ind}(C),E)' \to \operatorname{Hom}(C,E) \tag{8.7.3.1} $$

is an equivalence of categories.

To prove this last point, it suffices to verify that the map $f \mapsto \overline{f}$ defined by (8.7.2.2) can be
specified as a functor

[PDF p. 108]

$$
f \mapsto \overline{f}=\varinjlim_E \circ \operatorname{Ind}(f) :
\operatorname{Hom}(C,E) \to \operatorname{Hom}(\operatorname{Ind}(C),E)', \tag{8.7.3.2}
$$

and that this functor is quasi-inverse to (8.7.3.1). The details of the verification, essentially trivial, are left to
the reader. One may also invoke 7.8 to conclude first that (8.7.3.1) is fully faithful, and (8.7.2.3) to conclude that
it is essentially surjective.

**8.7.4.** Take up again a functor between $U$-categories

$$ f : C \to E, \tag{8.7.4.1} $$

where $E$ is a $U$-category in which small filtering inductive limits are representable, hence a functor

$$
\overline{f} : (X_i)_{i \in I} \mapsto \varinjlim_i f(X_i) :
\operatorname{Ind}(C) \to E. \tag{8.7.4.2}
$$

We propose to study conditions on $f$ which ensure that $\overline{f}$ is fully faithful, respectively an equivalence of
categories. Since $f$ is isomorphic to the composite $\overline{f} \circ c_C$, and since
$c_C : C \to \operatorname{Ind}(C)$ is fully faithful, one sees that, for $\overline{f}$ to be fully faithful, it is
necessary that $f$ be so. After replacing $C$ by its essential image in $E$, one therefore sees that essentially no
generality is lost in assuming that $f$ is the inclusion functor of a subcategory $C$ of $E$, which we shall assume
below to simplify notation.

**Proposition 8.7.5.** The notation is that of 8.7.4.

1. For the functor $\overline{f}$ to be fully faithful, it is necessary and sufficient that one have:

   **(i)** Every object $X$ of $C$ satisfies the following condition.

   **(PF)** For every small filtering inductive system $(Y_i)_{i \in I}$ in $C$, with inductive limit
   $\varinjlim_i Y_i$ in $E$, the canonical map

   [PDF p. 109]

   $$ \varinjlim_i \operatorname{Hom}(X,Y_i) \to \operatorname{Hom}(X,\varinjlim_i Y_i) \tag{8.7.5.1} $$

   is bijective.

2. For the functor $\overline{f}$ to be an equivalence of categories, it is necessary and sufficient that $C$ satisfy
   condition (i), as well as the following two conditions:

   **(ii)** $C$ is a subcategory of $E$ generating by strict epimorphisms (7.1).

   **(iii)** For every object $X$ of $E$, the full subcategory $C/X$ of $E/X$, formed by the objects $X'$ over $X$ with
   source in $\operatorname{ob}(C)$, is filtering and essentially small.

Condition (iii) is verified in particular if $C$ is equivalent to a small category, and if finite inductive limits in
$C$ are representable and the inclusion functor $f : C \to E$ commutes with them, that is, if, for every finite category
$J$ and every functor $\varphi : J \to C$, the inductive limit of $f\varphi$ is representable and is isomorphic in $E$
to an object of $C$.

**Proof.** For (1), with the notation of condition (i), if $Y$ denotes the ind-object $(Y_i)$, and $X$ the constant
ind-object defined by $X$, then (8.7.5.1) is precisely the canonical map

$$ \operatorname{Hom}(X,Y) \to \operatorname{Hom}(\overline{f}(X),\overline{f}(Y)). $$

Thus, if $\overline{f}$ is fully faithful, this map is indeed bijective. Conversely, if $X=(X_j)_{j \in J}$ and
$Y=(Y_i)_{i \in I}$ are two arbitrary ind-objects of $E$, then the map

$$ u : \operatorname{Hom}(X,Y) \to \operatorname{Hom}(\overline{f}(X),\overline{f}(Y)) $$

[PDF p. 110]

is the projective limit over $j$ of the maps

$$ u_j : \operatorname{Hom}(X_j,Y) \to \operatorname{Hom}(\overline{f}(X_j),\overline{f}(Y)), $$

where $X_j$ is the constant ind-object with value $X_j$. Thus $u$ is bijective if the $u_j$ are, and (i) therefore
implies that $\overline{f}$ is fully faithful.

For (2), suppose (i), (ii), and (iii) are verified, and prove that $\overline{f}$ is an equivalence. It remains to prove
that it is essentially surjective, hence that every $X \in \operatorname{ob}(E)$ is in the essential image. But
hypothesis (ii) means that

$$ \varinjlim_{C/X} Z \to X $$

is an isomorphism, and (iii) says that the category $C/X$ is filtering and essentially small. Thus $X$ is the image of
the ind-object of $E$ defined by the natural functor $C/X \to E$.

Conversely, suppose that $\overline{f}$ is an equivalence. By (1), it remains to verify (ii) and (iii). One may suppose
that $E=\operatorname{Ind}(C)$, with $C$ identified with the subcategory $c(C)$ of $E$. But we know (8.3.3 (ii)) that,
for every $X \in \operatorname{Ind}(C)$, identified if desired with the functor $F$ on $C^\circ$ which it
ind-represents, $C/X=C/F$ is a filtering essentially small category, which proves (iii), and that the inductive limit in
$\widehat{C}$ of the functor $C/F \to \widehat{C}$ is $F$. A fortiori, this is so in the full subcategory $E$ of
$\widehat{C}$, since $F=X$ is in $E$, which proves (ii). It remains to prove the last assertion of (2). But the
hypothesis made on $C$ evidently implies that, in the category $C/X$, finite inductive limits are representable; a
fortiori, the category $C/X$ is filtering.

[PDF p. 111]

**Remark 8.7.5.2.** The argument just given shows more generally that, when condition (i) is verified, the essential
image of the fully faithful functor $\overline{f}$ (8.7.4.2) is formed by those $X \in \operatorname{ob}(E)$ such that
the category $C/X$ is filtering and essentially small, a condition automatically satisfied if $C$ satisfies the
conditions stated at the end of (2), and such that the inductive limit of the canonical functor $C/X \to E$ is $X$.

**Corollary 8.7.6.** Let $E_{PF}$ be the full subcategory of $E$ formed by the objects satisfying condition (PF) of
8.7.5 (1). Then, for every functor $J \to E_{PF}$, where $J$ is a finite category, which admits an inductive limit $X$
in $E$, one has $X \in \operatorname{ob}(E_{PF})$. The canonical functor

$$ \overline{g} : \operatorname{Ind}(E_{PF}) \to E \tag{8.7.6.1} $$

deduced from the inclusion $g : E_{PF} \to E$ is fully faithful. If finite inductive limits are representable in $E$ and
if $E_{PF}$ is equivalent to a small category, then the essential image of the functor $\overline{g}$ is formed by the
objects $X$ of $E$ such that the canonical morphism

$$ \varinjlim_{(E_{PF})/X} Y \to X $$

is an isomorphism. If one further assumes that the subcategory $E_{PF}$ of $E$ generates by strict epimorphisms (7.1),
then the functor (8.7.6.1) is an equivalence of categories.

All the facts are evident, in the order in which they are given, taking 8.7.5 into account and using 2.8 for the first
assertion.

**Corollary 8.7.7.** Suppose that finite inductive limits are representable in $E$. Let $C$ be a full subcategory of
$E$, equivalent to a small category, and consider the functor

$$
(X_i)_{i \in I} \mapsto \varinjlim_i^E X_i :
\overline{f} : \operatorname{Ind}(C) \to E. \tag{8.7.7.1}
$$

Let $E_{PF}$ be as in 8.7.6. The following conditions are equivalent:

**(i)** The functor $\overline{f} : \operatorname{Ind}(C) \to E$ is an equivalence.

**(ii)** The category $C$, in $E$, generates by strict epimorphisms, is contained in $E_{PF}$, and every object of
$E_{PF}$ is isomorphic in $E$ (or in $E_{PF}$, which amounts to the same by 8.7.6) to a direct factor of an object of
$C$.

When the subcategory $C$ of $E$ is stable under direct factors (10.6), the preceding conditions are also equivalent to
the following:

**(ii bis)** $C=E_{PF}$, and $C$ generates in $E$ by strict epimorphisms.

**(iii)** The subcategory $C$ of $E$ generates by strict epimorphisms, is contained in $E_{PF}$, and finite inductive
limits are representable in it.

When, moreover, finite inductive limits are representable in $E$, these conditions are also equivalent to:

**(iii bis)** The subcategory $C$ of $E$ generates by strict epimorphisms, is contained in $E_{PF}$, and is stable in
$E$ under finite inductive limits, or equivalently, under finite sums and cokernels of double arrows.

[PDF p. 113]

We already know (8.7.5) that condition (i) implies that $C \subset E_{PF}$, and that $C$ generates by strict
epimorphisms. Let us also prove that, then, every object $X$ of $E_{PF}$ is isomorphic to a direct factor of an object
of $C$. Indeed, we know that $X$ is a filtering inductive limit $\varinjlim_i X_i$ in $E$ of objects of $C$, and, by the
definition of $E_{PF}$, one sees that, for suitable $i$, the canonical homomorphism $X_i \to X$ admits a left inverse.
Thus $X$ is indeed a direct factor of the object $X_i$ of $C$. This proves that (i) implies (ii), with no hypothesis on
$C$ or $E$, moreover.

Let us prove that (ii) implies (i). Since $C$ is equivalent to a small category and every object of $E_{PF}$ is a direct
factor of an object of $C$, one sees that $E_{PF}$ is also equivalent to a small category. Thus, by 8.7.6, the functor
(8.7.6.1) is an equivalence of categories, and one concludes by 8.6.4 (b), applied to the inclusion $C \subset E_{PF}$.

When every direct factor in $E$ of an object of $C$ lies in $C$, it is clear that (ii) is equivalent to (ii bis). On the
other hand, (ii bis) implies (iii), respectively (iii bis), by 8.7.6. Finally, (iii), and a fortiori (iii bis), implies
(i) by 8.7.5. This completes the proof.

**Exercise 8.7.8 (Karoubi Envelopes).** Let $C$ be a $U$-category, let $E=\operatorname{Ind}(C)$, and let
$E_{PF} \supset C$ be the full subcategory of $E$ defined in 8.7.6.

1. Prove that, in $E_{PF}$, images of projectors are representable, and that every object of $E_{PF}$ is a direct factor
   of an object of $C$.

2. Call a category $F$ **Karoubian** if images of projectors are representable in it. Let

   $$ \varphi : C \to K $$

   [PDF p. 114]

   be a fully faithful functor such that $K$ is Karoubian and every object of $K$ is a direct factor of an object in the
   image of $C$. Prove that $\varphi$ is 2-universal among functors from $C$ to Karoubian categories; more precisely, for
   every Karoubian category $F$, the functor

   $$ g \mapsto g \circ \varphi : \operatorname{Hom}(K,F) \to \operatorname{Hom}(C,F) $$

   is an equivalence of categories. Use the fact that every functor commutes with images of projectors. The category
   $K$, equipped with $\varphi$, determined up to equivalence (itself determined up to unique isomorphism) by the
   preceding properties, is called the Karoubi envelope $\widetilde{C}$ of $C$. Compare also IV 7.5.

3. Deduce from (1) and (2) that $\operatorname{Ind}(C)_{PF}$, equipped with the functor

   $$ C \to \operatorname{Ind}(C)_{PF} $$

   induced by $c : C \to \operatorname{Ind}(C)$, makes $\operatorname{Ind}(C)_{PF}$ a Karoubi envelope of $C$.

4. Show that every functor $f : C \to C'$ extends in an essentially unique way to a functor
   $\widetilde{f} : \widetilde{C} \to \widetilde{C'}$ of Karoubi envelopes, and that, if one takes these Karoubi
   envelopes as in (3), $\widetilde{f}$ is the functor induced by
   $\operatorname{Ind}(f) : \operatorname{Ind}(C) \to \operatorname{Ind}(C')$. Show that the conditions of 8.5.4 (b) are
   also equivalent to the following one: $\widetilde{f}$ is an equivalence of categories.

**Exercise 8.7.9.** Let $E$ be a $U$-category.

1. Show that the following conditions are equivalent:

   **(i)** $E$ is equivalent to a category of the form $\operatorname{Ind}(C)$, with $C$ a $U$-category.

   [PDF p. 115]

   **(i bis)** As in (i), with $C$ moreover Karoubian (8.7.8 (b)).

   **(ii)** The subcategory $E_{PF}$ of $E$ (8.7.6) generates by strict epimorphisms and, for every object $X$ of $E$,
   $(E_{PF})/X$ is a filtering essentially small category.

   Show that, if $C$ is a Karoubian $U$-category such that $E$ is equivalent to $\operatorname{Ind}(C)$, then $C$ is
   equivalent to $E_{PF}$, by an equivalence determined up to unique isomorphism. Establish a 2-equivalence between the
   2-category formed by the categories $E$ satisfying the preceding conditions and the functors between them commuting
   with small filtering inductive limits, and the 2-category formed by Karoubian $U$-categories and arbitrary functors
   between them.

2. Show that the following conditions are equivalent:

   **(i)** $E$ is equivalent to a category of the form $\operatorname{Ind}(C)$, where $C$ is a $U$-category in which
   finite inductive limits are representable.

   **(i bis)** As in (i), but with $C$ moreover Karoubian.

   **(ii)** Finite inductive limits in $E$ are representable, the subcategory $E_{PF}$ of $E$ generates by strict
   epimorphisms, and, for every object $X$ of $E$, there exists a small subset $I$ of $\operatorname{Ob}(E_{PF}/X)$ such
   that every object of $E_{PF}/X$ is majorized by an object of $I$. Use 8.9.5 (b).

[PDF p. 116]

### 8.8. Indexed Representation of a Functor $J \to \operatorname{Ind}(C)$

**8.8.1.** Let

$$ \varphi : J \to \operatorname{Ind}(C), \qquad \text{i.e. } \varphi \in \operatorname{ob}\operatorname{Hom}(J,\operatorname{Ind}(C)), $$

be a functor, where $C$ is a $U$-category. Recall (8.5.4) that an **indexed representation** of $\varphi$ is, by
definition, an ind-object of $\operatorname{Hom}(J,C)$,

$$ \psi : I \to \operatorname{Hom}(J,C), $$

where $I$ is an essentially small filtering category, whose inductive limit in
$\operatorname{Hom}(J,\operatorname{Ind}(C))$ is isomorphic to $\varphi$ by a given isomorphism. Thus $\varphi$ admits
an indexed representation if and only if it is isomorphic to an essentially small filtering inductive limit, in
$\operatorname{Hom}(J,\operatorname{Ind}(C))$, of objects of the full subcategory $\operatorname{Hom}(J,C)$. We shall
say that the category $J$ is **admissible for $C$** if every functor $\varphi : J \to \operatorname{Ind}(C)$ admits an
indexed representation.

Since small filtering inductive limits are representable in $\operatorname{Ind}(C)$ (8.5.1), the same is true in
$\operatorname{Hom}(J,\operatorname{Ind}(C))$, and they are computed "argument by argument." Consequently, the inclusion
functor

$$ \operatorname{Hom}(J,C) \to \operatorname{Hom}(J,\operatorname{Ind}(C)) \tag{8.8.1.1} $$

extends canonically to a functor

$$ \operatorname{Ind}(\operatorname{Hom}(J,C)) \to \operatorname{Hom}(J,\operatorname{Ind}(C)) \tag{8.8.1.2} $$

(8.7.2). The elements of the essential image of this functor are precisely the $\varphi$ admitting an indexed
representation. Thus saying that $J$ is admissible for $C$ also means that the functor (8.8.1.2) is essentially
surjective. In this connection, let us record:

[PDF p. 117]

**Proposition 8.8.2.** If the category $J$ is equivalent to a finite category, the canonical functor (8.8.1.2) is fully
faithful. Thus $J$ is admissible for $C$ if and only if it is an equivalence of categories.

By 8.7.5 (a), everything amounts to proving that, for every small filtering inductive system $(\varphi_i)_{i \in I}$ in
$\operatorname{Hom}(J,C)$ and every object $\varphi$ of $\operatorname{Hom}(J,C)$, the canonical map

$$ \varinjlim_i \operatorname{Hom}(\varphi,\varphi_i) \to \operatorname{Hom}(\varphi,\varinjlim_i \varphi_i) \tag{8.8.2.1} $$

is bijective, where $\varinjlim_i\varphi_i$ denotes the inductive limit taken in
$\operatorname{Hom}(J,\operatorname{Ind}(C))$. But, if $\varphi,\psi$ are two functors $J \to C$, one has an exact
diagram of sets, functorial in $\varphi$ and $\psi$:

$$
\operatorname{Hom}(\varphi,\psi)
\to
\prod_{X \in \operatorname{ob}J} \operatorname{Hom}(\varphi(X),\psi(X))
\rightrightarrows
\prod_{\substack{f \in \operatorname{Fl}J\\ f : X \to Y}}
\operatorname{Hom}(\varphi(X),\psi(Y)).
$$

Since filtering inductive limits commute with kernels of double arrows and finite products, the bijectivity of (8.8.2.1)
follows when $J$ is finite. The case where $J$ is equivalent to a finite category reduces at once to the preceding case.

**Proposition 8.8.3.** Let $\varphi : J \to \operatorname{Ind}(C)$ be a functor, with $J$ equivalent to a small
category. For $\varphi$ to admit an indexed representation, it suffices that it satisfy the following two conditions;
these are also necessary when $J$ is equivalent to a finite category.

1. The category $\operatorname{Hom}(J,C)/\varphi$, formed by the arrows of $\operatorname{Hom}(J,\operatorname{Ind}(C))$
   with target $\varphi$ and source in $\operatorname{Hom}(J,C)$, is filtering.

   [PDF p. 118]

2. For every object $j$ of $J$, the functor

   $$ \psi \mapsto \psi(j) : \operatorname{Hom}(J,C)/\varphi \to C/\varphi(j) \tag{8.8.3.1} $$

   is cofinal, that is, satisfies conditions F 1) and F 2) of 8.1.3.

**Proof.** Suppose (1) and (2) are verified, and prove that $\varphi$ admits an indexed representation. We may evidently
suppose $J$ small. Let

$$ I=\operatorname{Hom}(J,C)/\varphi, \tag{8.8.3.2} $$

which is a filtering category by hypothesis. First suppose $I$ is essentially small, so that the "inclusion" of $I$ into
$\operatorname{Hom}(J,C)$ defines an ind-object of $\operatorname{Hom}(J,C)$, denoted $i \mapsto \psi_i$. Moreover,
there is a canonical homomorphism

$$ \varinjlim_i \psi_i \to \varphi, \tag{8.8.3.3} $$

given argument by argument by the homomorphism

$$ \varinjlim_I \psi_i(j) \to \varphi(j)=\varinjlim_{C/\varphi(j)} X, $$

deduced from the functor (8.8.3.1). Since the latter is cofinal, one concludes that (8.8.3.3) is an isomorphism, whence
the conclusion.

In the case where $I$ is not assumed essentially small, it suffices to construct a full essentially small subcategory
$I'$ such that (8.8.3.3) remains an isomorphism when $\varinjlim_{I'}$ is taken instead of $\varinjlim_I$. For this, it
suffices that the composite functors

$$ I' \to I \to C/\varphi(j) $$

induced by the functors (8.8.3.1) all be cofinal. One then concludes by the following lemma, whose proof is immediate
from criterion (8.1.3 (b)), and is left to the reader.

[PDF p. 119]

**Lemma 8.8.3.4.** Let $I$ be a filtering $U$-category, and let

$$ f_j : I \to I_j \qquad (j \in J) $$

be a small family of cofinal functors from $I$ to essentially small filtering categories. Then there exists a full
subcategory $I'$ of $I$ which is filtering and essentially small, and such that the functors induced by the $f_j$ are
cofinal.

Finally let us prove necessity in 8.8.3 when $J$ is assumed equivalent to a finite category. An indexed representation
of $\varphi$ using an essentially small filtering index category $I$ defines a functor $\psi$,

```text
             psi
I ------------------> Hom(J, C)/phi
 \                         |
  \ psi_j                  |
   \                       v
    --------------------> C/phi(j),               (8.8.3.5)
```

and it suffices to prove that $\psi$ and each of the functors $\psi_j$ deduced from it are cofinal. By 8.1.3 (b), it
will follow that $\operatorname{Hom}(J,C)/\varphi$ is filtering, and, by Definition 8.1.1, that the vertical arrow of
(8.8.3.5) is also cofinal. By 8.8.2, one may identify $\varphi$ with an object of $\operatorname{Ind}(E)$, where
$E=\operatorname{Hom}(J,C)$, and the fact that the functor

[PDF p. 120]

$$ \psi : I \to E/\varphi $$

deduced from the ind-object $\varphi$ of $E$ indexed by $I$ is cofinal is a general fact, which is checked immediately
using criteria F 1) and F 2) of 8.1.3. The same reason, with $E,\varphi$ replaced by $C,\varphi(j)$, shows that $\psi_j$
is cofinal, which completes the proof.

**Remarks 8.8.4.**

1. In the case where $J$ is equivalent to a finite category, if $\varphi$ admits an indexed representation, we have seen
   that (8.8.3.5) is a cofinal functor, which implies that the category $\operatorname{Hom}(J,C)/\varphi$ is itself
   essentially small.

2. Suppose that finite inductive limits are representable in $C$. Then the same is true in $E=\operatorname{Hom}(J,C)$,
   and these are computed argument by argument; they are also inductive limits in $\operatorname{Hom}(J,C)$ and a
   fortiori in $\operatorname{Hom}(J,\operatorname{Ind}(C))$. It follows at once that condition (1) of 8.8.3 is then
   automatically satisfied, and everything amounts to looking at condition (2). I do not know whether it is
   automatically satisfied when, moreover, $J$ is assumed small.

We now come to the main result of the present section.

**Proposition 8.8.5.** Let $J$ be a category equivalent to a finite category, and suppose moreover that $J$ is rigid,
that is, that, for every $j \in \operatorname{ob}(J)$, every endomorphism of $j$ is the identity. Then $J$ is admissible
for $C$, whatever the $U$-category $C$ may be, that is, every functor $J \to \operatorname{Ind}(C)$ admits an indexed
representation.

[PDF p. 121]

After replacing $J$ by an equivalent category, we may suppose $J$ is reduced, that is, that two isomorphic objects of
$J$ are identical. Then $J$ is even finite. We proceed by induction on $\operatorname{card}\operatorname{ob}(J)$, the
case where this number is $\leq 0$ being trivial; we shall therefore suppose it $\geq 1$.

Let $j_0$ be a maximal object of $J$, that is, one such that, for every arrow $j_0 \to j$, there exists an arrow
$j \to j_0$. Taking into account the fact that $J$ is rigid, this implies that $j_0 \to j$ is an isomorphism, and since
$J$ is reduced, this implies $j_0=j$. Let $J'$ be the full subcategory deduced from $J$ by removing the object $j_0$,
and let $J''$ be the full subcategory reduced to the object $j_0$. The proposition then follows from the following
lemma.

**Lemma 8.8.5.1.** Let $J$ be a finite category, and let $J'$ and $J''$ be two full subcategories such that
$\operatorname{ob}(J)=\operatorname{ob}(J') \cup \operatorname{ob}(J'')$, and such that, for every
$j' \in \operatorname{ob}(J')$ and $j'' \in \operatorname{ob}(J'')$, one has $\operatorname{Hom}(j'',j')=\emptyset$. If
$J'$ and $J''$ are admissible for $C$, then so is $J$.

Everything amounts to proving criteria (1) and (2) of 8.8.3. This amounts to making six elementary verifications: the
last two conditions for the categories to be filtering for $\operatorname{Hom}(J,C)/\varphi$, and conditions F 1) and F
2) for the functors (8.8.3.1), successively in the cases $j \in \operatorname{ob}(J')$ and
$j \in \operatorname{ob}(J'')$. These latter conditions moreover imply that $\operatorname{Hom}(J,C)/\varphi$ is
nonempty. The verification, rather tedious, presents no difficulty and is left to the reader. The writer tried in vain
to find an elegant proof that would bypass these unpleasant verifications.

[PDF p. 122]

**Exercise 8.8.6.**

1. Let $J,J'$ be two categories admissible for $C$, one of them finite. Prove that $J \times J'$ is admissible for $C$.
   Use 8.8.2.

2. Prove that a small discrete category is admissible for every category $C$.

3. Let $J$ be a category satisfying the following conditions:

   **(i)** $J$ is rigid.

   **(ii)** $\operatorname{ob}(J)$ is countable.

   **(iii)** For any two objects $j,j'$ of $J$, $\operatorname{Hom}(j,j')$ is finite.

   **(iv)** For every object $j$ of $J$, the set of objects of $J$ majorized by $j$, that is, sources of an arrow with
   target $j$, is finite.

   Show that $J$ is admissible for every $U$-category $C$. First show that $J$ can be written as a filtering union of
   finite full subcategories $J_n$, such that every object of $J$ majorized by an object of $J_n$ lies in $J_n$. Then
   verify criteria (1) and (2) of 8.8.3.

**Exercise 8.8.7.** In the notation, we identify an ordered set and the category it defines.

1. Let $C$ be an ordered set. Let $\widetilde{C}$ be the set of subsets $A$ of $C$ which are filtering and such that
   $x \in A$ and $y \leq x$ imply $y \in A$. Let

   $$ L_o : C \to \widetilde{C} $$

   be the map which associates to every $x \in C$ the set $L_o(x)$ of $y \in C$ such that $y \leq x$. Show that $L_o$ is
   an injective map and that the order of $C$ is induced by that of $\widetilde{C}$.

   For every $A \in \widetilde{C}$, consider the inclusion

   $$ f(A) : A \to C. $$

   This is an ind-object of $C$. For every ind-object $\varphi : I \to C$ of $C$, let
   $g(\varphi) \in \widetilde{C}$ be the subset of $C$ formed by the elements of $C$ majorized by an element of the form
   $\varphi(i)$.

   [PDF p. 123]

   Show that one thus obtains two quasi-inverse equivalences

   $$ \operatorname{Ind}(C) \rightleftarrows \widetilde{C} $$

   transforming the functor $L_o$ into the canonical functor $L : C \to \operatorname{Ind}(C)$.

2. Suppose that, for every $x \in C$, the set of elements majorizing, respectively minorizing, $x$ is finite. Show that
   every ind-object, respectively pro-object, of $C$ is essentially constant; and even that, for every such
   $\varphi : I \to C$, respectively $\varphi : I^\circ \to C$, there exists an $i_0 \in \operatorname{ob}(I)$ such that
   the functor induced on $I/i_0$ is constant, that is, transforms every arrow into an isomorphism.

3. Take $C \subset N^\circ \times N$, formed by the pairs of natural integers $(j,i)$ such that $i \geq j$. Show that
   $\widetilde{N}$ is isomorphic to the ordered set deduced from $N$, identified with an ordered subset of
   $\widetilde{N}$ as in (1), by adding a greatest element $\infty$. Show that $\widetilde{C}$ is isomorphic to
   $N^\circ \times \widetilde{N}$. Consider the functor

   $$ \varphi : N^\circ \to \widetilde{C}, \qquad \varphi(j)=(j,\infty). $$

   Show that:

   **(i)** The projective limit of $\varphi$ is not representable in $\widetilde{C}$, although filtering projective
   limits in $C$ are representable, and are essentially constant by (2).

   **(ii)** For every functor $\psi : N^\circ \to C$, one has $\operatorname{Hom}(\psi,\varphi)=\emptyset$, and a
   fortiori the functor $\varphi$ admits no representation in indexed form.

[PDF p. 124]

**Exercise 8.8.8.** Let $X=N \amalg N$ be the sum set of two copies of $N$, let $s$ be the symmetry of $X$, and, for
every $i \in N$, let $X_i$ be the subset $\Delta_{i+1} \amalg \Delta_i$ of $N \amalg N$, where $\Delta_i$ denotes the
subset of $N$ formed by the $j$ such that $j \leq i$.

Let $C$ be the subcategory of the category of subsets of $X$ whose objects are the $X_i$, and whose arrows are the maps
between $X_i$ induced by the identity of $X$ or by its symmetry $s$. Let $\widetilde{C}$ be the category defined
analogously, but where the object $X$ is also allowed.

1. Show that $\operatorname{Ind}(C)$ is equivalent to $\widetilde{C}$, the canonical functor
$C \to \operatorname{Ind}(C)$ corresponding to the inclusion $C \to \widetilde{C}$. Show that there is no pair $(Y,f)$,
formed by an object $Y$ of $C$ and an endomorphism $f$ of $Y$, together with a morphism of objects with endomorphism of
$\operatorname{Ind}(C)$ from $(Y,f)$ to $(X,s)$.

2. Conclude that, if $J$ is the category having one object and, in addition to the identity arrow, a single arrow of
order $2$, then the functor $J \to \operatorname{Ind}(C)$ defined by $(X,s)$ admits no indexed representation.

### 8.9. Exactness Properties of $\operatorname{Ind}(C)$

**Proposition 8.9.1.** Let $C$ be a $U$-category.

1. The canonical functors $L$ (8.2.4.8) and $c$ (8.4.1),

   $$ C \xrightarrow{c} \operatorname{Ind}(C) \xrightarrow{L} \widehat{C}, $$

   commute with projective limits.

2. Suppose that finite inductive limits are representable in $C$, and that $C$ is equivalent to a small category. Then,
   in $\operatorname{Ind}(C)$, small projective limits are representable.

[PDF p. 125]

3. If, in $C$, small projective limits, respectively finite projective limits, are representable, then the same is true
   in $\operatorname{Ind}(C)$. Let $J$ be a category which is finite and rigid, or discrete; if projective limits of
   type $J$ are representable in $C$, this same type of projective limits is representable in $\operatorname{Ind}(C)$.

4. Filtering inductive limits in $\operatorname{Ind}(C)$, representable by 8.5.1, are left exact, that is, commute with
   finite projective limits.

**Proof.**

1. The fact that $L$ commutes with projective limits follows from the fact that it is fully faithful and from the
   calculation of projective limits in $\widehat{C}$ "argument by argument." Indeed, to check that a projective system
   of morphisms $F \to F_i$, $i \in I$, in $\widehat{C}$ makes $F$ a projective limit of the $F_i$, it suffices to check
   that the analogous assertion is true for the projective systems of set-theoretic maps

   $$ \operatorname{Hom}(X,F) \to \operatorname{Hom}(X,F_i), $$

   for every $X \in \operatorname{ob}(C)$. But $C \subset \operatorname{Ind}(C)$.

   The fact that $c$ commutes with projective limits follows formally from the fact that $L$ commutes with them, as does
   the composite $L \circ c : C \to \widehat{C}$.

2. Taking (1) into account, the assertion amounts to saying that every projective limit of ind-representable presheaves
   is ind-representable. This follows at once from criterion 8.3.3 (v), taking into account that a projective limit of
   left exact functors is left exact, which follows from the fact that "projective limits commute with projective
   limits" (2.5.0).

[PDF p. 126]

3. This follows formally from the analogous property of $\widehat{C}$ (3.3), and from the fact that $L$ is conservative,
   being fully faithful, and commutes with the limits of the type considered, by (1) and 8.5.1.

4. It is well known (cf. 2.3) that representability of finite projective limits is equivalent to representability of
   projective limits of the types

   ```text
   empty,  *,  * => *,
   ```

   corresponding to particular finite ordered sets; and that small projective limits amount to products and finite
   projective limits. Thus the second assertion made in (3) implies the first.

Suppose first that $J$ is finite. Using result 8.8.5 on the representability of functors
$\varphi : J \to \operatorname{Ind}(C)$ in indexed form (8.5.4), the existence of the $\varprojlim_J\varphi$ is
therefore a special case of the following more precise and more general result.

**Corollary 8.9.2.** Consider a functor $\varphi : J \to \operatorname{Ind}(C)$ given in indexed form

$$ \Phi : J \times I \to C, \tag{8.9.1.1} $$

where $J$ is a finite category. If, for every $i \in \operatorname{ob}(I)$, the partial functor $j \mapsto \Phi(j,i)$
has a projective, respectively inductive, limit representable in $C$, then $\varphi$ has a projective, respectively
inductive, limit representable in $\operatorname{Ind}(C)$, and one has a canonical isomorphism

$$
\varprojlim_J \varphi
\simeq
\text{``}\varinjlim\text{''}_i \varprojlim_J \Phi(j,i), \tag{8.9.2.1}
$$

[PDF p. 127]

respectively

$$
\varinjlim_J \varphi
\simeq
\text{``}\varinjlim\text{''}_i \varinjlim_J \Phi(j,i), \tag{8.9.2.2}
$$

where $\varprojlim_J$, respectively $\varinjlim_J$, is computed in $C$.

For the first formula, one simply uses that, in $\operatorname{Ind}(C)$, filtering inductive limits commute with
$\varprojlim_J$, and that $c$ commutes with $\varprojlim_J$ by 8.9.1 (4) and (1):

$$
\varprojlim_J \varphi
=
\varprojlim_J \text{``}\varinjlim\text{''}_i \Phi(j,i)
\simeq
\text{``}\varinjlim\text{''}_i \varprojlim_J^{\operatorname{Ind}(C)} \Phi(j,i)
\simeq
\text{``}\varinjlim\text{''}_i \varprojlim_J^C \Phi(j,i).
$$

The second is proved in the same way, using the commutation of inductive limits of type $I$ with inductive limits of
type $J$ (2.5.0) and the fact that $c$ commutes with inductive limits of type $J$, proved in 8.9.4 (a) below.

Discrete case for $J$. This case is contained in the following more precise assertion:

**Corollary 8.9.3.** Let $I_\alpha$ be essentially small filtering categories indexed by a small set $A$, and, for every
$\alpha \in A$, let

$$ X(\alpha)=(X(\alpha)_{i_\alpha})_{i_\alpha \in I_\alpha} $$

be an ind-object of $C$ indexed by $I_\alpha$. Let $I$ be the product category of the $I_\alpha$, and suppose that, for
every $i=(i_\alpha)_{\alpha \in A} \in I$, the product

$$ \prod_{\alpha \in A} X(\alpha)_{i_\alpha} $$

is representable in $C$. Then the product $\prod_{\alpha \in A} X(\alpha)$ is representable in $\operatorname{Ind}(C)$,
and it is canonically isomorphic to the ind-object indexed by $I$ given by the formula

$$
\prod_{\alpha \in A}\text{``}\varinjlim\text{''}_{i_\alpha \in I_\alpha} X(\alpha)_{i_\alpha}
\simeq
\text{``}\varinjlim\text{''}_{i=(i_\alpha) \in I}
\left(\prod_{\alpha \in A} X(\alpha)_{i_\alpha}\right). \tag{8.9.3.1}
$$

[PDF p. 128]

where the product in the second member is the product computed in $C$. Note that $I$ is filtering and essentially small,
since the $I_\alpha$ are.

Indeed, it is well known, and immediate by reduction to the case where one works in the category of sets, that the
formula considered is valid when one computes the limits in $\widehat{C}$. The conclusion then follows from the fact
that $L$ commutes with the limits considered, by 8.9.1 (2) and 8.5.1.

**Remarks 8.9.4.** The proof given of 8.9.2 and 8.9.3 shows more generally that, if for every
$i \in \operatorname{ob}(I)$, $\varprojlim_J\Phi(j,i)$, respectively $\varinjlim_J\Phi(j,i)$, computed in
$\operatorname{Ind}(C)$, is representable, then the same is true of $\varprojlim_J\varphi$, respectively of
$\varinjlim_J\varphi$.

This and the argument of (3) show that, for a given category $J$ coming from a finite or discrete ordered set, or more
generally one which is $C$-admissible (8.3.1), projective, respectively inductive, limits of type $J$ are representable
in $\operatorname{Ind}(C)$ if and only if, for every functor $\varphi : J \to C$, the projective, respectively
inductive, limit of $\varphi$ computed in $\operatorname{Ind}(C)$ is representable. In the projective case, this also
means, by (1), that every projective limit of type $J$ of representable presheaves on $C$ is ind-representable.

**Proposition 8.9.5.** Let $C$ be a $U$-category.

1. The canonical functor

   $$ c : C \to \operatorname{Ind}(C) $$

   is right exact, hence exact taking 8.9.1 (1) into account.

2. If finite inductive limits, respectively finite sums, are representable in $C$, then small inductive limits,
   respectively small sums, are representable in $\operatorname{Ind}(C)$. Let $J$ be a finite or discrete preordered
   set; if inductive limits of type $J$ are representable in $C$, then the same is true in $\operatorname{Ind}(C)$.

[PDF p. 129]

**Proof.**

1. Suppose that in $C$ one has $X \simeq \varinjlim_J X_j$, where $J$ is a finite category, $X$ and the $X_j$ lying in
   $C$. Then, for every ind-object $Y=(Y_i)_{i \in I}$ of $C$, one has:

   $$
   \begin{aligned}
   \operatorname{Hom}(X,Y)
   &\simeq \varinjlim_i \operatorname{Hom}(X,Y_i) \\
   &\simeq \varinjlim_i \varprojlim_j \operatorname{Hom}(X_j,Y_i) \\
   &\simeq \varprojlim_j \varinjlim_i \operatorname{Hom}(X_j,Y_i) \\
   &\simeq \varprojlim_j \operatorname{Hom}(X_j,Y).
   \end{aligned}
   $$

   The desired conclusion follows by comparing the extreme terms.

2. We already noted in 8.8.4 that the assertions made follow from (1) and 8.9.2, at least for finite inductive limits.
   To prove the conclusions made in the infinite cases, one is reduced to the case of sums, which may be interpreted as
   a filtering inductive limit of finite sums, and one therefore concludes by 8.5.1.

**Remark 8.9.6.** We have already observed that the functor $c$ does not in general commute with filtering inductive
limits, hence not with infinite sums either, contrary to what happens for $L : \operatorname{Ind}(C) \to \widehat{C}$.
On the other hand, except for commutation with filtering inductive limits (8.5.1), $L$ practically never has commutation
properties with any other type of inductive limits: initial object, sum of two objects, cokernels of double arrows.

Thus, if $C$ admits an initial object $\emptyset_C$, which is therefore an initial object of $\operatorname{Ind}(C)$ by
(1), $\emptyset_C$ is never an initial object of $\widehat{C}$, that is, identical to the constant presheaf with value
$\emptyset$, since $\operatorname{Hom}(\emptyset_C,\emptyset_C) \neq \emptyset$.

[PDF p. 130]

**Proposition 8.9.7.** Let

$$ f : C \to C' $$

be a functor between $U$-categories, and let $J$ be a finite rigid category (8.8.5). If inductive, respectively
projective, limits of type $J$ are representable in $C$ and if $f$ commutes with them, then
$\operatorname{Ind}(f) : \operatorname{Ind}(C) \to \operatorname{Ind}(C')$ also commutes with this type of limits.

This follows at once from 8.8.5 and from calculation 8.9.2 of finite limits in a category of ind-objects, for a functor
represented in indexed form.

**Corollary 8.9.8.** If finite inductive, respectively projective, limits are representable in $C$, and if $f$ is right
exact, respectively left exact, then the same is true of $\operatorname{Ind}(f)$. In the non-parenthesized case,
$\operatorname{Ind}(f)$ even commutes with arbitrary small inductive limits.

The first assertion follows from 8.9.7. The second follows from the first, taking into account that
$\operatorname{Ind}(f)$ commutes with filtering inductive limits (8.6.3).

**Exercise 8.9.9.** Let $C$ be a $U$-category.

1. Suppose that finite sums are representable in $C$. Show that, if finite sums in $C$ are disjoint, respectively
   universal (cf. II 4.5), then small sums in $\operatorname{Ind}(C)$ are disjoint, respectively universal.

2. Suppose that, in $C$, every morphism factors as an epimorphism followed by a monomorphism, respectively as an
   effective epimorphism

[PDF p. 131]

   followed by a monomorphism, respectively as an epimorphism followed by an effective monomorphism, respectively as an
   effective epimorphism followed by an effective monomorphism. Show that $\operatorname{Ind}(C)$ satisfies the same
   property.

   In the last case, conclude that every epimorphism of $\operatorname{Ind}(C)$ is effective, every monomorphism of
   $\operatorname{Ind}(C)$ is effective, and every bimorphism of $\operatorname{Ind}(C)$ is an isomorphism. Show that,
   in this case, every epimorphism, respectively monomorphism, of $\operatorname{Ind}(C)$ can be represented by an
   inductive system of epimorphisms, respectively monomorphisms, of $C$. If one further assumes that, in $C$, every
   epimorphism, respectively every monomorphism, is universal, the same property is true in $\operatorname{Ind}(C)$.

3. Suppose $C$ is additive, respectively abelian. Then $\operatorname{Ind}(C)$ is so as well.

4. Let $X=\text{``}\varinjlim\text{''}_I X_i$ be an ind-object of $C$, and let $R \rightrightarrows X$ be an equivalence
   relation in $X$. For every $i \in \operatorname{ob}(I)$, let $R_i \rightrightarrows X_i$ be the equivalence relation
   in $X_i$, considered as an object of $\operatorname{Ind}(C)$, induced by $R$ via $X_i \to X$. We suppose that the
   fiber product

   $$ R_i=R \times_{X \times X} (X_i \times X_i) $$

   in $\operatorname{Ind}(C)$ is representable by an object of $\operatorname{Ind}(C)$, which is the case if finite
   projective limits are representable in $C$. Show that, for $R$ to be effective, it suffices that the $R_i$ be so.

5. Let $X$ be an object of $C$, and let $R$ be an equivalence relation in $c(X)$, that is, in $X$ considered as an
   object of $\operatorname{Ind}(C)$. Suppose that fiber products are representable in $C$. For $R$ to be effective, it
   is necessary that $R$ be of the form $\text{``}\varinjlim\text{''}_i R_i$, where the $R_i$ are equivalence relations
   in $X$, regarded as an object of $C$, and this condition

[PDF p. 132]

   is sufficient if one supposes that equivalence relations are effective in $C$.

6. Suppose that, in $C$, every morphism factors as an effective epimorphism followed by an effective monomorphism, and
   that finite projective limits are representable. Let $X$ be an object of $C$, and let $R$ be a subobject of
   $X \times X$, regarded as an element of $\operatorname{Ind}(C)$. Write $R$ in the form
   $\text{``}\varinjlim\text{''}_i Z_i$, where $(Z_i)_{i \in I}$ is a filtering increasing family of subobjects of
   $X \times X$ in $C$, which is possible by (2). Show that, for $R$ to be an equivalence relation in $X$, it is
   necessary and sufficient that, for every $i \in \operatorname{ob}(I)$, there exists a $j \in \operatorname{ob}(I)$
   which contains $s(Z_i)$ and $Z_i \circ Z_i$, where $s$ is the symmetry of $X \times X$.

7. Suppose that finite projective limits as well as finite sums are representable in $C$, that every equivalence
   relation is effective there, and that every morphism factors there as an effective epimorphism followed by an
   effective monomorphism. Show that, in $\operatorname{Ind}(C)$, equivalence relations are universal if and only if $C$
   satisfies the following condition.

   **ST)** For every object $X$ of $C$ and every subobject $Z$ of $X \times X$ in $C$, if one defines recursively the
   sequence of subobjects $Z_n$, $n \geq 0$, of $X \times X$ in $C$ by

   $$
   Z_0=Z,\qquad
   Z_{n+1}=\operatorname{Sup}(Z_n,s(Z_n),Z_n \circ Z_n),
   $$

   the $\operatorname{Sup}$ being taken in the set of subobjects of $X \times X$, which exists by the hypotheses made on
   $C$, then the sequence $(Z_n)_{n \geq 0}$ is stationary.

8. Show that, in $\operatorname{Ind}(\mathbf{Ens})$, equivalence relations are not necessarily effective.

*NB.* For criteria for $\operatorname{Ind}(C)$ to be a topos, cf. VI 8.9.9.

[PDF p. 133]

**Exercise 8.9.10.** Let $C$ be a $U$-category. Put $\operatorname{Pro}(C)=(\operatorname{Ind}(C^\circ))^\circ$ (cf.
8.11).

1. Suppose that finite sums, respectively small sums, are representable in $C$. Show that, if they are disjoint (cf. II
   4.5), then $\operatorname{Pro}(C)$ satisfies the same condition.

2. Let $J$ be a small set such that sums indexed by $J$ are representable in $C$, hence also in $\operatorname{Pro}(C)$.
   Let $(X(\alpha))_{\alpha \in J}$ be a family of elements of $\operatorname{Pro}(C)$, with

   $$ X(\alpha)=\text{``}\varprojlim\text{''}_{I_\alpha} X_{i_\alpha}. $$

   Show that, for the sum of the $X(\alpha)$ in $\operatorname{Pro}(C)$ to be universal, it suffices that the same be
   true for each of the families

   $$ \varprojlim_J X_{i_\alpha}, $$

   where $(i_\alpha)_{\alpha \in J} \in \prod_{\alpha \in J} I_\alpha$. Conclude that, if sums of type $J$ are universal
   in $C$, then for the same to be true in $\operatorname{Pro}(C)$, it is necessary and sufficient that, for every
   family $(X(\alpha))$ as above, with $I_\alpha=I$ for every $\alpha \in J$, the canonical homomorphism in
   $\operatorname{Pro}(C)$

   $$
   \text{``}\varprojlim\text{''}_I \left(\coprod_\alpha X(\alpha)_i\right)
   \leftarrow
   \text{``}\varprojlim\text{''}_{I^J}
   \left(\coprod_{\alpha \in J} X(\alpha)_{i_\alpha}\right)
   $$

   is an isomorphism. Conclude that, in $\operatorname{Pro}(\mathbf{Ens})$, sums of type $J$ are universal if and only if
   $J$ is finite.

**Exercise 8.9.11.** Let $C$ be a $U$-category.

1. Let $(X_i \to X)_{i \in I}$ be a family of morphisms in $C$. Show that, for it to be epimorphic in
   $\operatorname{Ind}(C)$, it suffices that there exist a finite subfamily which is epimorphic in $C$. Prove that this
   condition is also necessary when one assumes that, in $C$, every finite family of morphisms with target $X$ factors
   as an epimorphic family

[PDF p. 134]

   followed by an effective monomorphism (10.5). For this last assertion, let $P_f(I)$ be the set of finite subsets of
   $I$, ordered by inclusion, and let $X'=(X'_J)_{J \in P_f(I)}$ be the ind-object formed by the images of the finite
   subfamilies of the given family. Finally let

   $$ X''=X \amalg_{X'} X=\text{``}\varinjlim\text{''}_J (X \amalg_{X'_J} X). $$

   Show that the two canonical morphisms $X \rightrightarrows X''$ are distinct, but coincide on the $X_i$.

2. Suppose that, in $C$, every finite family of morphisms with common target factors as an epimorphic family followed by
   an effective monomorphism. Prove that $\operatorname{Ind}(C)$ admits a small subcategory generating by epimorphisms
   (7.1) if and only if $C$ admits a small subcategory $C'$ such that every object of $C$ is the target of a finite
   epimorphic family with source in $C'$.

   When one supposes that $C$ admits a small generating subcategory (7.1), then $\operatorname{Ind}(C)$ admits a small
   subcategory generating by epimorphisms if and only if $C$ is equivalent to a small category. For this last statement,
   use 7.5.2.

3. $\operatorname{Ind}(\mathbf{Ens})$ admits no small generating subcategory.

**Exercise 8.9.12.** Let $C$ be a $U$-category, and consider $\operatorname{Pro}(C)=\operatorname{Ind}(C^\circ)^\circ$.

1. Show that, if $\operatorname{Pro}(C)$ admits a small subcategory $P'$ generating by epimorphisms (7.1), then there
   exists a small subcategory $C'$ of $C$ which generates by epimorphisms in $\operatorname{Pro}(C)$. Take the category
   of components of the objects of $P'$.

[PDF p. 135]

2. Show that the category $\operatorname{Pro}(\mathbf{Ens})$ has no small subcategory generating by epimorphisms. If
   $C'$ is as in (1), choose a set $X$ whose cardinal strictly bounds above the cardinals of the elements of $C'$, and
   consider the pro-set $X$ formed by the complements in $X$ of the subsets of cardinal $<\operatorname{card}(X)$. Show
   that, for every nonempty set $Y$ of cardinal $<\operatorname{card}(X)$, one has $\operatorname{Hom}(Y,X)=\emptyset$,
   but that $X$ is not isomorphic to the constant pro-set $\emptyset$.

### 8.10. Dual Notions: Pro-Objects, Pro-Representable Functors

Let $C$ be a $U$-category. A **pro-object** of $C$ is a functor

$$ \varphi : I^\circ \to C, \tag{8.10.1} $$

where $I$ is an essentially small filtering category, called the index category, and where, as usual, $I^\circ$ denotes
the opposite category. Let $V$ be a universe such that $V \supset U$. One should note that the pro-objects of $C$
indexed by $I \in V$ are in one-to-one correspondence with the ind-objects of $C^\circ$ indexed by $I \in V$, by
associating to every such ind-object $\psi : I \to C^\circ$ the pro-object $\varphi=\psi^\circ : I^\circ \to C$.

Inspired by this correspondence, one defines "by transport of structure and reversal of arrows" the notion of morphism
between pro-objects of $C$ from the analogous notion (8.2.4.2), (8.2.5.1) for ind-objects. Consequently one defines the
category of pro-objects of $C$ indexed by $I \in V$, and a canonical isomorphism:

$$ \operatorname{Pro}_V(C,U) \simeq \operatorname{Ind}_V(C^\circ,U)^\circ. \tag{8.10.2} $$

[PDF p. 136]

For $V=U$, one simply speaks of the category of pro-objects of $C$, denoted $\operatorname{Pro}_U(C)$ or simply
$\operatorname{Pro}(C)$, which is therefore defined by

$$ \operatorname{Pro}(C)=\operatorname{Pro}_U(C,U) \simeq \operatorname{Ind}(C^\circ)^\circ. \tag{8.10.3} $$

If two pro-objects are given in indexed form

$$ X=(X_i)_{i \in I},\qquad Y=(Y_j)_{j \in J}, \tag{8.10.4} $$

formula (8.2.5.1) here takes the form

$$ \operatorname{Hom}(X,Y) \simeq \varprojlim_j \varinjlim_i \operatorname{Hom}(X_i,Y_j). \tag{8.10.5} $$

The functor (8.4.1) applied to $C^\circ$ gives, by passing to opposite categories, a canonical functor, denoted by the
same letter $c$ if there is no risk of confusion, allowing us to identify $C$ with a full subcategory of
$\operatorname{Pro}(C)$:

$$ c : C \to \operatorname{Pro}(C). \tag{8.10.6} $$

It is in order to have such a functor, and not $C \to \operatorname{Pro}(C)^\circ$, that we have "reversed the arrows"
in the definition of morphisms of pro-objects from the analogous definition for ind-objects. The pro-objects in the
essential image of (8.10.6) are again called **essentially constant pro-objects**.

Put

$$ \check{C}=(C^\circ)^\wedge=\operatorname{Hom}(C,\mathbf{Ens}). \tag{8.10.7} $$

Then the functor (8.2.4.7) may be considered as a canonical fully faithful functor

[PDF p. 137]

$$ L : \operatorname{Pro}_V(C,U) \to \check{C}^\circ, \tag{8.10.8} $$

and one obtains in particular

$$ L : \operatorname{Pro}(C) \to \check{C}^\circ. \tag{8.10.9} $$

We leave to the reader the task of translating, as needed, the results of the preceding sections and of those which
follow from the language of ind-objects into that of pro-objects. Depending on the mathematical context, one or the
other language is more useful, not counting the cases where both notions appear simultaneously, for example when one
must consider complex categories such as $\operatorname{Pro}(\operatorname{Ind}(C))$ or
$\operatorname{Ind}(\operatorname{Pro}(C))$. We content ourselves with giving a few further indications, to fix
terminology and notation and to make the "yoga" precise.

**8.10.10.** A covariant functor $F : C \to \mathbf{Ens}$ is said to be **pro-representable** if it lies in the
essential image of (8.10.9), or of (8.10.8), which amounts to the same thing. The full subcategory of $\check{C}$ formed
by these functors is therefore equivalent to $\operatorname{Pro}(C)^\circ$. One will generally prefer to work in the
opposite category, the essential image as a subcategory of (8.10.9), which is therefore equivalent to
$\operatorname{Pro}(C)$ itself.

In accordance with this usage, it is often preferable to regard covariant functors

$$ F : C \to \mathbf{Ens} $$

as objects of $\operatorname{Hom}(C,\mathbf{Ens})^\circ=\check{C}^\circ$, and consequently to write the category of
homomorphisms

[PDF p. 138]

$$ X \to F $$

in $\check{C}^\circ$, that is, of pairs $(X,u)$ consisting of an object $X$ of $C$ and an element $u \in F(X)$, as

$$ F\backslash C. \tag{8.10.11} $$

With this convention, one therefore obtains a covariant functor, the source functor,

$$ F\backslash C \to C, \tag{8.10.12} $$

and 3.4 is rewritten in the form

$$ F \simeq \text{``}\varprojlim\text{''}_{(F\backslash C)^\circ} X. \tag{8.10.13} $$

**8.10.14.** Criterion 8.3.3 applied to $C^\circ$ becomes a pro-representability criterion for $F$: it is necessary and
sufficient that $(F\backslash C)^\circ$ be filtering and essentially small, the latter condition being superfluous if
$C$ is equivalent to a small category. If, moreover, finite projective limits are representable in $C$, it amounts to
the same thing to say that $F$ commutes with them, that is, is left exact.

**8.10.15.** In $\operatorname{Pro}(C)$, small filtering projective limits are representable and the functor (8.10.9)
commutes with them. In other words, this functor transforms projective limits in $\operatorname{Pro}(C)$ into inductive
limits of $\check{C}=\operatorname{Hom}(C,\mathbf{Ens})$, just like its composite $C \to \check{C}^\circ$ with (8.10.6),
which shares with it the unfortunate property of being contravariant when considered with values in $\check{C}$. One
should note that the pro-representable functors from $C$ to $\mathbf{Ens}$ are the functors which are small filtering
inductive limits of representable functors, and not projective limits, as the terminology might possibly suggest.

### 8.11. Ind-Adjoints and Pro-Adjoints

**8.11.1.** Let

$$ f : C \to C' \tag{8.11.1.1} $$

be a functor between $U$-categories, hence a functor $F \mapsto F \circ f$,

$$ f^* : \widehat{C'} \to \widehat{C}. \tag{8.11.1.2} $$

We say that $f$ **admits an ind-adjoint** if the preceding functor transforms ind-representable functors into
ind-representable functors. Since $f^*$ commutes with inductive limits, and the full subcategory of $\widehat{C'}$
formed by the ind-representable functors is stable under small filtering inductive limits, saying that $f$ admits an
ind-adjoint amounts to saying that $f^*$ maps the objects of $C'$, identified with a full subcategory of $\widehat{C'}$,
to ind-representable functors on $C$, that is, that

$$ X \mapsto \operatorname{Hom}(f(X),Y') $$

is ind-representable for every $Y' \in \operatorname{Ob} C'$. Another way of expressing the condition that $f$ admit an
ind-adjoint is to say that there exists a functor

$$ g : \operatorname{Ind}(C') \to \operatorname{Ind}(C) \tag{8.11.1.4} $$

which is essentially induced by $f^*$, that is, such that one has an isomorphism of bifunctors

[PDF p. 140]

$$
\operatorname{Hom}_{\operatorname{Ind}(C)}(X,g(Y'))
\simeq
\operatorname{Hom}_{\operatorname{Ind}(C')}(f(X),Y'), \tag{8.11.1.5}
$$

where $X \in \operatorname{Ob} C$ and $Y' \in \operatorname{Ob}\operatorname{Ind}(C')$. In fact, it even suffices to
have a functor

$$ g_0 : C' \to \operatorname{Ind}(C) \tag{8.11.1.6} $$

and an isomorphism of bifunctors

$$
\operatorname{Hom}_{\operatorname{Ind}(C)}(X,g_0(Y'))
\simeq
\operatorname{Hom}_{C'}(f(X),Y') \tag{8.11.1.7}
$$

in $X \in \operatorname{Ob} C$, $Y' \in \operatorname{Ob} C'$. The functor $g$, respectively $g_0$, is evidently
determined up to unique isomorphism by $f$, and conversely $f$ is reconstructed, up to canonical isomorphism, from
knowing this $g$, respectively $g_0$.

It is clear from (8.11.1.5) that the functor $g$ commutes with inductive limits, and that it "extends" the functor
$g_0$. Thus it is determined up to unique isomorphism in terms of $g_0$ (8.7.2). The functor $g$, and sometimes also the
functor $g_0$ which it extends, is called the **ind-adjoint functor** of $f$. It is unnecessary here to specify "on the
right," since the other one, if it exists, will be called the pro-adjoint (8.11.5 below).

Of course, when $f$ admits a right adjoint

$$ f^{\operatorname{ad}} : C' \to C, $$

it admits an ind-adjoint $g$, and this is canonically isomorphic to the canonical extension of $f^{\operatorname{ad}}$
to ind-objects:

$$ g \simeq \operatorname{Ind}(f^{\operatorname{ad}}). \tag{8.11.1.8} $$

The notion of ind-adjoint is therefore a natural generalization of the notion of right adjoint.

[PDF p. 141]

Now consider the canonical extension

$$ \operatorname{Ind}(f) : \operatorname{Ind}(C) \to \operatorname{Ind}(C'). \tag{8.11.1.9} $$

Then:

**Proposition 8.11.2.** For the functor $f : C \to C'$ to admit an ind-adjoint, it is necessary and sufficient that the
functor $\operatorname{Ind}(f)$ (8.11.1.9) admit a right adjoint. The latter is canonically isomorphic to the
ind-adjoint (8.11.1.4).

Sufficiency and the last assertion are trivial from the ind-adjunction formula (8.11.1.5). For necessity, note that, by
passing to the projective limit over this formula applied to $X_i$, one deduces an adjunction isomorphism in the
ind-objects $X=(X_i)_{i \in I}$ and $Y'$:

$$
\operatorname{Hom}_{\operatorname{Ind}(C)}(X,g(Y'))
\simeq
\operatorname{Hom}_{\operatorname{Ind}(C')}(\operatorname{Ind}(f)(X),Y'). \tag{8.11.2.1}
$$

QED.

**Corollary 8.11.3.** If $f$ admits an ind-adjoint, then $\operatorname{Ind}(f)$ commutes with inductive limits, and the
ind-adjoint $g$ commutes with projective limits.

**Proposition 8.11.4.** For the functor $f : C \to C'$ to admit an ind-adjoint, it is necessary that $f$ be left exact,
and this condition is sufficient when $C$ is equivalent to a small category.

This follows from criterion (8.11.1.3), and from 8.3.1 and 8.3.3 (iv). For another criterion in terms of the notion of
accessible functor, cf. 8.13.3.

[PDF p. 142]

**8.11.5.** Now consider the functor $F \mapsto F \circ f$

$$ f^{\circ *} : \check{C'} \to \check{C} \tag{8.11.5.1} $$

induced by $f$. We shall say that $f$ **admits a pro-adjoint** if the preceding functor maps pro-representable functors
to pro-representable functors, that is, if there exists a functor, called the **pro-adjoint functor** of $f$,

$$ g : \operatorname{Pro}(C') \to \operatorname{Pro}(C), \tag{8.11.5.2} $$

and an isomorphism of bifunctors

$$
\operatorname{Hom}_{\operatorname{Pro}(C)}(g(Y'),X)
\simeq
\operatorname{Hom}_{\operatorname{Pro}(C')}(Y',f(X)). \tag{8.11.5.3}
$$

Of course, saying that $f$ admits a pro-adjoint means that $f^\circ$ admits an ind-adjoint, so that the notions and
results for ind-adjoints translate trivially in terms of pro-adjoints.

Let us merely point out that $f$ admits a pro-adjoint if and only if
$\operatorname{Pro}(f) : \operatorname{Pro}(C) \to \operatorname{Pro}(C')$ admits a right adjoint, and that in this case
the preceding functor $g$ is such a right adjoint of $\operatorname{Pro}(f)$. For this, $f$ must be left exact; this
condition is also sufficient when $C$ is equivalent to a small category. In that case, $f$ is therefore exact if and
only if it admits both an ind-adjoint and a pro-adjoint.

**Example 8.11.6.** Consider the case of a functor

$$ f : C \to \mathbf{Ens}. $$

If this functor admits a pro-adjoint, it is pro-representable, and the converse is true if and only if the full
subcategory of $\check{C}$ formed by the pro-representable functors is stable under small products;

[PDF p. 143]

this is the case in particular if $C$ is equivalent to a small category (8.10.14), or if small products are
representable in $C$ (8.9.5 b) applied to $C^\circ$). Up to minor qualifications, one may therefore say that, for a
functor $f : C \to C'$, the notion of existence of a pro-adjoint is the natural generalization of the notion of
pro-representability of $f$, which is defined when $C'=\mathbf{Ens}$.

### 8.12. Strict Ind-Objects and Pro-Objects. Application to a Representability Criterion

**8.12.1.** Let

$$ X=(X_i)_{i \in I} $$

be an ind-object of the $U$-category $C$, and let $F$ be the presheaf which it ind-represents. One then sees at once
that saying that the canonical morphisms

$$ X_i \to F=\text{``}\varinjlim\text{''}_i X_i $$

are monomorphisms of $\operatorname{Ind}(C)$, or equivalently of $\widehat{C}$, that is, monomorphisms of functors
argument by argument, is equivalent to saying that, for every arrow $i \to j$ of $I$, the corresponding transition arrow

$$ X_i \to X_j $$

is a monomorphism. When these conditions are fulfilled, and if moreover $I$ is an ordered category, we say that $X$ is a
**strict ind-object**.

[PDF p. 144]

Note that this condition is not invariant under isomorphism of ind-objects; an ind-object will be called **essentially
strict** if it is isomorphic to a strict ind-object. A presheaf will be called **strictly ind-representable** if it is
ind-representable by a strict ind-object. Thus $F=\text{``}\varinjlim\text{''}X_i$ is strictly ind-representable if and
only if $X=(X_i)_{i \in I}$ is essentially strict.

**8.12.1.1.** Let $F$ be a presheaf on $C$, and consider the full subcategory of $C/F$ formed by the arrows $X \to F$,
with source in $C$, which are monomorphisms. We shall call it the **category of representable subfunctors of $F$**; it
is the category associated with the ordered set of representable subfunctors of $F$, ordered by the order induced from
that of the set of subobjects of $F$. It follows at once from the definitions:

**Proposition 8.12.2.** For the presheaf $F$ on $C$ to be strictly ind-representable, it is necessary and sufficient
that the ordered category $I$ of representable subfunctors of $F$ be filtering and essentially small, and that one have

$$ \text{``}\varinjlim\text{''}_I X_i \simeq F. \tag{8.12.2.1} $$

When, for every object $X$ of $C$, the set of subobjects of $X$ in $C$ is small, for example if $C$ admits a small
generating subcategory (7.4), this implies that the category of representable subfunctors is even small.

[PDF p. 145]

**8.12.2.2.** If $F$ is strictly ind-representable, there is therefore a preferred way of ind-representing it by an
ind-object, and the latter is even a strict ind-object: take the representation (8.12.2.1). A strict ind-object $Y$ is
called **saturated** if it is isomorphic to an ind-object of the form $(X_i)$ occurring in (8.12.2.1), for suitable $F$.
Thus, up to unique isomorphism, there exists only one saturated strict ind-object isomorphic to a given strict
ind-object, namely the one considered in 8.12.2, taking $F=\text{``}\varinjlim\text{''}Y$, the limit in $\widehat{C}$.

**8.12.2.3.** Suppose one already knows that a small cofinal subset can be found in the set $\operatorname{Ob}(C/F)$,
which is the case in particular if $F$ is ind-representable. Then it follows that the same condition is verified in the
full subcategory $I$ considered in 8.12.2; hence, in criterion 8.12.2, one may omit the condition that $I$ be
essentially small.

**8.12.3.** Let $F$ be a presheaf on $C$, and consider an object

$$ u : X \to F $$

of $C/F$.

We say that $u$, or the pair $(X,u)$, is **minimal** if, for every factorization of $u$ as

$$ X \xrightarrow{p} X' \xrightarrow{u'} F, \tag{8.12.3.1} $$

with $p$ a strict epimorphism (10.2), $p$ is an isomorphism. Considering $u$ as an object of $F(X)$ (1.4), saying that
$u$ is minimal therefore means

[PDF p. 146]

that every strict epimorphism $p : X \to X'$ such that $u \in \operatorname{Im}(F(p):F(X')\to F(X))$ is an isomorphism.
This notion is clarified by part a) of the following lemma.

**Lemma 8.12.4.** Let $F$ be a presheaf on $C$.

1. Suppose that $F$ transforms cokernels into kernels and consider a morphism

   $$ u : X \to F, $$

   with $X \in \operatorname{Ob} C$. For $u$ to be a monomorphism, it suffices, when cokernels of double arrows are
   representable in $C$, that $u$ be minimal; this condition is also necessary if fiber products are representable in
   $C$.

2. Suppose that finite limits are representable in $C$. For the subcategory of representable subfunctors of $F$
   (8.12.1.1) to be filtering, not necessarily small, and to have inductive limit $F$, it suffices that $F$ be left
   exact and that every morphism $u : X \to F$, with $X \in \operatorname{Ob} C$, factor as

   $$ X \to X' \xrightarrow{u'} F, $$

   with $u'$ minimal; this condition is also necessary if fiber products are representable in $C$.

3. Suppose that $C$ admits a small generating subcategory (7.1), and that $I$, the category of representable subfunctors
   of $F$, is filtering. Then $I$ is small.

[PDF p. 147]

**Proof.** 1. Suppose $u$ is minimal. Prove that $u$ is a monomorphism, that is, that for every double arrow
$v,v' : Y \rightrightarrows X$ such that $uv=uv'$, one has $v=v'$. Indeed, if $X'=\operatorname{Coker}(v,v')$, then $u$
factors as

$$ X \xrightarrow{p} X' \xrightarrow{u'} F $$

because $F$ transforms cokernels into kernels. Since $p$ is a strict epimorphism by construction, it follows that $p$ is
an isomorphism, that is, $v=v'$.

Conversely, suppose that $u$ is a monomorphism and prove that it is minimal. Consider a factorization (8.12.3.1). Since
$p$ is a strict epimorphism, it is the cokernel of the canonical double arrow
$v,v' : X \times_{X'} X \rightrightarrows X$. Since $(u'p)v=(u'p)v'$ and $u'p=u$ is a monomorphism, one has $v=v'$, so
$p$ is an isomorphism.

2. Sufficiency: since $F$ is left exact, $C/F$ is filtering. Since one knows that $F=\varinjlim_{C/F} X$, 8.1.3 c)
reduces us to proving that the full subcategory $I$ of $C/F$ of subobjects of $F$ is cofinal in $C/F$. By the "it
suffices" part of 1, this is exactly what is ensured by the hypothesis that every object of $C/F$ is majorized by a
minimal object.

Necessity: since every filtering inductive limit of right exact functors is again right exact, the first condition is
trivially necessary. The second then follows from the "it is necessary" part of 1.

3. A representable subfunctor $X \hookrightarrow F$ of $F$ is known when one knows the full subcategory $C'/X$ of $C'/F$,
where $C'$ is a fixed small generating subcategory of $C$. Use here the hypothesis that $I$ is filtering. Since $C'/F$
is small, the set of its full subcategories is small, whence the conclusion.

[PDF p. 148]

**Proposition 8.12.5.** Let $C$ be a $U$-category in which finite inductive limits are representable, and admitting a
small generating subcategory (7.1). Let $F$ be a presheaf on $C$. For $F$ to be strictly ind-representable, it suffices
that it satisfy the following two conditions; these are also necessary if fiber products are representable in $C$:

1. $F$ is left exact.
2. Every pair $(X,u)$, with $X \in \operatorname{Ob} C$ and $u \in F(X)$, is majorized in $C/F$ by a minimal pair
   (8.12.3), that is, there exists a minimal pair $(X',u')$, with $X' \in \operatorname{Ob} C$ and $u' \in F(X')$, and a
   morphism $f : X \to X'$ such that $u=F(f)(u')$.

Sufficiency follows from 8.12.2 and 8.12.4 b), c), and necessity from 8.3.1 and 8.12.4 a).

**Remark 8.12.6.** When $F$ transforms amalgamated sums of $C$ into fiber products, one sees at once that, for a given
pair $(X,u)$ as in b), the set of strict quotients $X'$ of $X$ such that $u \in \operatorname{Im}(F(X')\to F(X))$ is
filtering decreasing. This implies that, if the set of strict quotients of $X$ is artinian, then condition b) of 8.12.5
is automatically satisfied.

Thus, if the preceding condition on $X$ is satisfied for every object $X$ of $C$ - one also sometimes says then that the
objects of $C^\circ$ are artinian - it follows from 8.12.5 that $F$ is strictly ind-representable if and only if $F$ is
left exact. In this case, $F$ is therefore strictly ind-representable as soon as it is ind-representable (8.3.1).

[PDF p. 149]

**Corollary 8.12.7.** Let $C$ be a $U$-category in which small projective limits are representable, and admitting a
small cogenerating subcategory (7.9, 7.13). Then a functor $F : C \to \mathbf{Ens}$ is representable if and only if $F$
commutes with small projective limits.

Necessity is clear. For sufficiency, apply 8.12.5 to the opposite category $C^\circ$. To prove first that $F$ is
strictly pro-representable, one is reduced to proving that every pair $(X,u)$, with $X \in \operatorname{Ob} C$ and
$u \in F(X)$, is majorized by a minimal pair. But the family $(X_i)_{i \in I}$ of strict subobjects of $X$ such that
$u \in \operatorname{Im}(F(X_i)\to F(X))$ is small (7.5 in dual form). By the fact that $F$ is left exact, it is
cofiltering (8.12.6), and by the fact that $F$ commutes with small projective limits, one sees that

$$ X'=\varprojlim_i X_i $$

is a smallest object of this family. Use here the fact that, since $F$ is left exact, it transforms monomorphisms into
monomorphisms. If $u' \in F(X')$ is the unique element whose image in $F(X)$ is $u$, then one sees that $(X',u')$ is a
minimal pair majorizing $(X,u)$. This proves that $F$ is pro-representable, and the conclusion then follows from the
following lemma.

**Lemma 8.12.8.1.** Let $F : C \to \mathbf{Ens}$ be a functor, where $C$ is a $U$-category in which small projective
limits are representable. For $F$ to be representable, it is necessary and sufficient that it be pro-representable and
commute with small projective limits.

[PDF p. 150]

Necessity is clear; let us prove sufficiency. Saying that $F$ is representable evidently means that $F\backslash C$
admits an initial element. In fact, the initial objects of $F\backslash C$ are precisely the isomorphisms $F \to X$,
that is, the representation data for $F$. But since $F$ is pro-representable, $(F\backslash C)^\circ$ is filtering and
equivalent to a small category, hence

$$ X=\varprojlim_{(F\backslash C)^\circ} X $$

is representable in $C$. Since $F$ commutes with the limit considered, it follows that $X$ is an initial object of
$F\backslash C$, QED.

**Corollary 8.12.8.** With the hypotheses on $C$ as in 8.12.7, let $f : C \to C'$ be a functor from $C$ to a
$U$-category $C'$. For $f$ to admit a left adjoint, it is necessary and sufficient that $f$ commute with small
projective limits.

This reduces trivially to 8.12.7, by applying that statement to the composite functors of the form
$X \mapsto \operatorname{Hom}(Y',f(X))$.

**Examples 8.12.9.** As noted in 7.13, the hypotheses on $C$ in 8.12.7 and 8.12.8 are verified if $C$ is the category of
$U$-sheaves of sets on a topological space $X \in U$, or more generally on a $U$-site (II 3.0.2). Let us give an
instructive example (*) showing that the hypothesis that there exist a small cogenerating subcategory $D$ of $C$ is not
superfluous in 8.12.7.

Take for $C$ the category of groups which are elements of $U$. Let $J$ be the set of isomorphism classes of simple
groups of $C$. For every $j \in J$, choose a simple group $G_j$ in the class $j$, and let $I$ be the filtering ordered
set of $U$-small subsets of $J$. For $i \in I$, let

$$ X_i=\prod_{j \in i} G_j. $$

The $X_i$ then form a projective system $(X_i)_{i \in I}$ in $C$, whose transition morphisms are epimorphisms, and the
corresponding functor

(*) due to H. Bass.

[PDF p. 151]

$$ F(X)=\text{``}\varinjlim\text{''}_i \operatorname{Hom}(X_i,X) $$

takes its values in $U\text{-}\mathbf{Ens}$, although the index set $I$ evidently does not have a cardinal in $U$. More
precisely, let us show that for every small full subcategory $C_0$ of $C$, there exists an $i_0 \in I$ such that the
restriction of $F$ to $C_0$ is represented by $X_{i_0}$; this will prove both that $F$ takes values in
$U\text{-}\mathbf{Ens}$ and that it commutes with small projective limits.

To prove our assertion, it suffices to note that, for every $X \in \operatorname{Ob} C_0$, the cardinal of the set
$J(X)$ of $j \in J$ such that there exists a nontrivial homomorphism from $G_j$ into $X$ is necessarily small, since
such a morphism is necessarily a monomorphism, $G_j$ being simple. Consequently, if $i_0$ is the subset of $J$ which is
the union of the $J(X)$ for $X \in \operatorname{Ob} C_0$, then $i_0$ is small, that is, $i_0 \in I$, and it does the
job.

On the other hand, it is clear that $F$ is not representable, since $\operatorname{card} I \notin U$. From this and
8.12.7 one concludes that the category $C$ of groups belonging to $U$ does not admit a small full cogenerating
subcategory. Since the object $\mathbf{Z}$ of $C$ is, on the other hand, a generator, it then follows from the proof of
7.12 that there exists a group $G$ with two generators which does not embed in an injective object of the category $C$
of groups of $U$. It moreover seems plausible that $C$ admits no injective objects other than the unit groups.

[PDF p. 152]

### 8.13. Pro-Representable Functors and Accessible Functors

**8.13.1.** In the present section, we use a few notions and results from the following paragraph, and in particular
9.11 and 9.13, to obtain a pro-representability criterion which we shall use incidentally in IV 9.16. In what follows,
$C$ denotes a $U$-category satisfying condition $L$ of 9.1 b), this condition being fulfilled for example if small
filtering inductive limits are representable in $C$.

**Proposition 8.13.2.** Let $C$ be as above, and let

$$ f : C \to \mathbf{Ens} $$

be a functor.

1. Suppose that each object of $C$ is accessible (9.3). If $f$ is pro-representable, then $f$ is accessible (9.2) and
   left exact.

2. Suppose that finite projective limits are representable in $C$, and that $C$ admits a cardinal filtration (9.12). If
   $f$ is accessible and left exact, then $f$ is pro-representable.

**Proof.** 1. The hypothesis on $C$ means that the covariant representable functors from $C$ to $\mathbf{Ens}$ are
accessible. Hence the same is true of every small inductive limit of such functors (9.6 (i)), and therefore also of
every pro-representable functor.

2. By 8.3.3 (iii), it remains to prove that in $(f\backslash C)^\circ$ there is a small cofinal subcategory. By
hypothesis, there exists a cardinal $\pi$ such that $f$ is $\pi$-accessible. Let

[PDF p. 153]

$(X,u)$, with $u \in f(X)$, be an object of $f\backslash C$. With the notation of 9.12 c), one then has

$$ X=\varinjlim_i X_i, $$

with $I$ filtering, large relative to $\pi$, and the $X_i$ in $C'=\operatorname{Filt}^\pi(C)$, whence
$f(X) \simeq \varinjlim_i f(X_i)$. This shows that the small subcategory $(f\backslash C')^\circ$ is cofinal in
$(f\backslash C)^\circ$, and completes the proof.

**Corollary 8.13.3.** Let $C$ be a $U$-category satisfying the following conditions:

1. Finite projective limits are representable in $C$.
2. Small filtering inductive limits are representable in $C$.
3. The functor $\operatorname{Ker}$ on the category of double arrows of $C$ is accessible, for example if it commutes
   with small filtering inductive limits.
4. Every strict epimorphism of $C$ is strict universal (10.2).
5. There exists a small subcategory of $C$ generating by strict epimorphisms (7.1).

Under these conditions, a functor $f : C \to \mathbf{Ens}$ is pro-representable if and only if it is left exact and
accessible (9.2).

Indeed, the conditions of 8.13.2 a) and b) on $C$ are verified by 9.11 and 9.13 respectively.

**Corollary 8.13.4.** Let $f : C \to C'$ be a functor between $U$-categories satisfying conditions a) to e) of 8.13.3.
For $f$ to admit a pro-adjoint, it is necessary and sufficient that $f$ be left exact and accessible.

[PDF p. 154]

Since the representable functors

$$ h_{Y'} : X' \mapsto \operatorname{Hom}(Y',X') : C' \to \mathbf{Ens} $$

are left exact and accessible (9.11), if $f$ has these same properties, the same is true of their composites with $f$,
which are therefore pro-representable by 8.13.3; that is, $f$ admits a pro-adjoint.

Conversely, suppose that $f$ admits a pro-adjoint, and let $C'_1$ be a small generating subcategory of $C'$ and $\pi$ a
cardinal such that the $Y' \in \operatorname{Ob} C'_1$ are $\pi$-accessible. To prove that $f$ is $\pi$-accessible, it
therefore suffices to prove that the same is true of its composites with the $h_{Y'}$, $Y' \in \operatorname{Ob} C'_1$.
But, by hypothesis, these composites are pro-representable, hence accessible (8.13.3), hence $\pi$-accessible provided
one takes $\pi$ large enough. QED.

## 9. Accessible Functors, Cardinal Filtrations, and Construction of Small Generating Subcategories

The present paragraph, more technical in nature than the other paragraphs of this expose, will be used in this seminar
only in IV 9 and in VI 4, which are not used elsewhere in the Seminar. It is therefore advisable to skip reading the
present paragraph, at least on first reading!

**9.0.** All categories considered in the present section are assumed to be $U$-categories. Except for the small index
categories $I$, $J$, ... which we shall have to use, the developments below will apply mainly to "large" categories $E$,
$F$, ... which are stable under small filtering inductive limits. It will, however, most often suffice

[PDF p. 155]

that a slightly weaker condition be verified, condition $L$ in 9.1 below. All cardinals considered in the present
section are assumed to belong to $U$.

Following a suggestion of P. Deligne, we shall study, for a functor $f : E \to F$ between large categories, a condition
of commutation of $f$ with certain types of filtering inductive limits, a remarkably stable condition, and one which
will be verified for the most important functors encountered in nature. The applications we have in view, for our
seminar, are 9.13.3, 9.13.4, used in VI 4, and especially 9.25, which gives, in a nontrivial case, the existence of a
small generating family in a category of sections of a fibered category; this result will be used in IV 9.16.

**Definition 9.1.**

1. Let $I$ be a preordered set and let $\pi$ be a cardinal. We say that $I$ is **large relative to $\pi$** if $I$ is
   filtering, and if every subset of $I$ of cardinal $\leq \pi$ admits a majorant in $I$.

2. Let $E$ be a category. If $\pi$ is a cardinal, we say that $E$ satisfies condition $L_\pi$ if, for every small
   ordered set $I$ large relative to $\pi$, $E$ is stable under inductive limits of type $I$. We say that $E$ satisfies
   condition $L$ if there exists a cardinal $\pi \in U$ such that $E$ satisfies condition $L_\pi$.

**9.1.1.** When, in 9.1 a), one has $\pi \geq 2$, the second stated condition already implies that $I$ is filtering; and
if $\pi$ is finite, $I$ large relative to $\pi$ simply means that $I$ is filtering. In what follows we shall scarcely be
interested except in the case where $\pi$ is infinite. Note that if $\pi,\pi'$ are two cardinals such that
$\pi' \geq \pi$, then $I$ large relative to $\pi'$ evidently implies $I$ large relative to $\pi$.

[PDF p. 156]

**9.1.2.** As announced in 9.0, the conditions $L_\pi$, $L$ should be considered as technical variants of the stronger
condition of stability under small filtering inductive limits. It is clear that if $\pi,\pi'$ are cardinals such that
$\pi' \geq \pi$, then condition $L_\pi$ implies condition $L_{\pi'}$.

**Definition 9.2.** Let $f : E \to F$ be a functor. If $\pi$ is a cardinal, we say that $f$ is **$\pi$-preaccessible**,
respectively **$\pi$-accessible**, if $E$ satisfies $L_\pi$ (9.1) and if, for every ordered set $I \in U$ large relative
to $\pi$, and every inductive system $(X_i)_{i \in I}$ in $E$ of type $I$, the canonical morphism

$$ \text{``}\varinjlim\text{''}_i f(X_i) \to f(\text{``}\varinjlim\text{''}_i X_i) $$

is a monomorphism, respectively an isomorphism. We say that $f$ is **preaccessible**, respectively **accessible**,
relative to the universe $U$, if there exists a cardinal $\pi \in U$ such that $f$ is $\pi$-preaccessible, respectively
$\pi$-accessible.

The category of $\pi$-accessible, respectively accessible, functors from $E$ to $F$ will be denoted
$\operatorname{Hom}(E,F)_\pi$, respectively $\operatorname{Hom}(E,F)_{\operatorname{acc}}$.

**9.2.1.** Evidently, a functor commuting with small filtering inductive limits, for example a functor admitting a right
adjoint, is $\pi$-accessible for every cardinal $\pi \geq 2$.

**Definition 9.3.** Let $E$ be a category, let $X$ be an object of $E$,

$$ h_X^\circ : E \to U\text{-}\mathbf{Ens} $$

the covariant functor it represents, and let $\pi \in U$ be a cardinal. We say that $X$ is a $\pi$-preaccessible,
respectively $\pi$-accessible, object of $E$ if the functor

[PDF p. 157]

$h_X^\circ$ is $\pi$-preaccessible, respectively $\pi$-accessible. We say that $X$ is **preaccessible**, respectively
**accessible**, if there exists a cardinal $\pi \in U$ such that $X$ is a $\pi$-preaccessible, respectively
$\pi$-accessible, object of $E$.

**9.3.1.** We denote by $E_\pi$ the full subcategory of $E$ formed by the $\pi$-accessible objects of $E$.

When Definition 9.3 is applied to a category of the form $\operatorname{Hom}(C,F)$, the terminology introduced has a
priori an ambiguity with the analogous terminology introduced in 9.2, when one interprets the objects of
$\operatorname{Hom}(C,F)$ as functors; it does not seem, however, that there is any serious risk of confusion.

**Definition 9.4.** Let $E$ be a category and let $\pi \in U$ be a cardinal. We say that $E$ is a $\pi$-preaccessible,
respectively $\pi$-accessible, category if there exists in $E$ a small full subcategory $C$ which is generating (7.1)
and whose objects are $\pi$-preaccessible, respectively $\pi$-accessible (9.3). We say that $E$ is a preaccessible,
respectively accessible, category if there exists a cardinal $\pi \in U$ such that $E$ is $\pi$-preaccessible,
respectively $\pi$-accessible.

For important examples, cf. 9.11.3 below.

**Proposition 9.5.** Let $f : E \to F$ be a functor between categories such that $F$ is accessible and every object of
$E$ is accessible. Then, if $f$ admits a left adjoint, $f$ is accessible.

[PDF p. 158]

Indeed, by hypothesis, $F$ admits a small conservative family of accessible representable functors
$F \to U\text{-}\mathbf{Ens}$. One is therefore immediately reduced to showing that the composite of $f$ with each of
the preceding functors is accessible. But, since $f$ admits a left adjoint, these composites are representable functors
$E \to U\text{-}\mathbf{Ens}$, hence accessible by the hypothesis on $E$.

**Proposition 9.6.** Let $E$ and $F$ be two categories, let $\pi \in U$ be a cardinal, and consider the full subcategory
$\operatorname{Hom}(E,F)_\pi$ of $\operatorname{Hom}(E,F)$ formed by the $\pi$-accessible functors (9.2) from $E$ to
$F$.

1. This subcategory is stable under every type of inductive limit representable in $F$.
2. Suppose $F$ is $\pi$-accessible (9.4), and let $J$ be a category such that
   $\operatorname{card}\operatorname{Fl}(J) \leq \pi$ and projective limits of type $J$ are representable in $F$, hence
   projective limits of type $J$ are representable in $\operatorname{Hom}(E,F)$. Then the subcategory
   $\operatorname{Hom}(E,F)_\pi$ is stable under projective limits of type $J$.

**Corollary 9.7.** Let $E$ and $F$ be two categories, with $F$ accessible (9.4). Then the full subcategory
$\operatorname{Hom}(E,F)_{\operatorname{acc}}$ of $\operatorname{Hom}(E,F)$ formed by the accessible functors is stable
under every type of inductive or projective limit, relative to a small index category $J$, which is representable in $F$
(hence in $\operatorname{Hom}(E,F)$).

**Proof of 9.6.** Assertion (i) follows trivially from the commutation of the functor $\varinjlim$ with arbitrary
inductive limits. For (ii), let $(f_j)_{j \in J}$ be a projective system of $\pi$-accessible functors $E \to F$.

[PDF p. 159]

Let $f=\varprojlim_j f_j$ be its projective limit, which is computed "argument by argument." Prove that $f$ is
$\pi$-accessible, that is, that for every ordered set $I \in U$ large relative to $\pi$ and every inductive system
$(X_i)_{i \in I}$ in $E$, the canonical morphism

$$
\varinjlim_i ((\varprojlim_j f_j)(X_i))
\to
(\varprojlim_j f_j)(\varinjlim_i X_i)
$$

is an isomorphism. But the "argument by argument" computation of the functor $\varprojlim_j f_j$ identifies the
preceding canonical morphism with the canonical morphism

$$ \varinjlim_i \varprojlim_j f_j(X_i) \to \varprojlim_j \varinjlim_i f_j(X_i), $$

associated with the bifunctor $(i,j)\mapsto f_j(X_i)$ from $I \times J$ to $F$. Thus 9.6 is a consequence of the more
general assertion below.

**Corollary 9.8.** Let $F$ be a $\pi$-accessible category, let $I$ be an ordered set large relative to $\pi$, let $J$ be
a small category such that $\operatorname{card}\operatorname{Fl}(J)\leq \pi$ and such that projective limits of type $J$
are representable in $F$, and let $h : I \times J \to F$ be a functor. Then the canonical morphism

$$ \varinjlim_i \varprojlim_j h(i,j) \to \varprojlim_j \varinjlim_i h(i,j) \tag{9.8.1} $$

is an isomorphism. In other words, the functor

$$ \varinjlim_i : \operatorname{Hom}(I,F) \to F \tag{9.8.2} $$

commutes with projective limits of type $J$, for every small category $J$

[PDF p. 160]

such that $\operatorname{card}\operatorname{Fl}(J)\leq \pi$ and such that projective limits of type $J$ are
representable in $F$. Or again, for every $J$ as above, the functor

$$ \varprojlim_j : \operatorname{Hom}(J,F) \to F \tag{9.8.3} $$

is $\pi$-accessible.

Since, by hypothesis, $F$ admits a conservative family of covariant representable $\pi$-accessible functors
$g : F \to U\text{-}\mathbf{Ens}$, one sees at once that one is reduced to proving 9.8 in the case
$F=U\text{-}\mathbf{Ens}$. We shall then prove the assertion in the form that (9.8.2) commutes with projective limits of
type $J$, with $\operatorname{card}\operatorname{Fl}(J)\leq \pi$. Since $I$ is filtering, we know that (9.8.2) commutes
with finite projective limits (2.8). Therefore, by a standard argument (cf. 2.3), one is reduced to proving that it
commutes with products indexed by a set $J$ such that $\operatorname{card}J\leq \pi$. This reduces us to proving the
bijectivity of (9.8.1) when $J$ is discrete.

Prove injectivity. Consider two elements $a,b$ of the first member; they therefore come from $\prod_j h(i_0,j)$ for
suitable $i_0 \in I$. Suppose that the elements of the second member which they define are equal, that is, for every
$j \in J$, there exists $i(j)\geq i_0$ such that $a(i_0,j)$ and $b(i_0,j)$ have the same image in $h(i(j),j)$. Since $I$
is large relative to $\operatorname{card}J$, there exists a common majorant $i_1 \in I$ of all the $i(j)$, which implies
that the two elements considered in $\prod_j h(i_0,j)$ have the same image in $\prod_j h(i_1,j)$, and hence define the
same element of the first member of (9.8.1). This proves injectivity.

[PDF p. 161]

For surjectivity, let $\prod_j a(\infty,j)$ be an element of the second member. For every $j \in J$, the element
$a(\infty,j)$ comes from an element of $h(i(j),j)$, for suitable $i(j)\in I$. As before, one can find a common majorant
$i \in I$ of the $i(j)$. Thus $\prod_j a(\infty,j)$ comes from an element $\prod_j a(i,j)$ of $\prod_j h(i,j)$, and so
lies in the image of (9.8.1). This completes the proof.

**Corollary 9.9.** Let $F$ be a $\pi$-accessible, respectively accessible, category. Then, for every category $J$ such
that $\operatorname{card}\operatorname{Fl}(J)\leq \pi$, respectively every small category $J$, and for every functor
$(X_j)_{j \in J} : J \to F$ whose inductive limit in $F$ is representable, if the $X_j$ are $\pi$-accessible,
respectively accessible, then the same is true of $\varinjlim_J X_j$.

Indeed, the functor $F \to U\text{-}\mathbf{Ens}$ represented by $\varinjlim_J X_j$ is the projective limit of the
functors represented by the $X_j$, and one applies 9.6 (ii) to the projective system formed by these functors.

**Remark 9.10.** In statements 9.6, 9.7, 9.8, and 9.9, one may everywhere replace the words "$\pi$-accessible,"
"accessible" by "$\pi$-preaccessible," "preaccessible." The proof given indeed also proves this variant of the preceding
statements.

**Proposition 9.11.** Let $E$ be a category satisfying condition $L$ (9.1), and let $C$ be a small full generating
subcategory (7.1). Assume the condition:

1. $E$ is stable under kernels of double arrows, and the functor $\operatorname{Ker}$, on the category of double arrows
   of $E$, is accessible (for example, it commutes with small filtering inductive limits).

[PDF p. 162]

Then every object of $E$ is preaccessible (9.3); a fortiori $E$ is preaccessible.

Suppose $C$ even generates by strict epimorphisms (7.1), and assume that $E$ satisfies the conditions:

2. $E$ is stable under fiber products.
3. Every small strict epimorphic family in $E$ is strict universal epimorphic (10.3); or else, in $E$, small direct sums
   are representable, and every strict epimorphism of $E$ is a strict universal epimorphism.

Then every object of $E$ is accessible; a fortiori $E$ is accessible.

The fact that, assuming 1., every object of $E$ is preaccessible follows from the fact that, for every object $X$ of
$E$, the set of strict subobjects of $X$ is small (7.4), and from the following lemma.

**Lemma 9.11.1.** Under conditions 9.11 1., let $X \in \operatorname{Ob}(E)$ and let $\pi$ be a cardinal such that $E$
satisfies $L_\pi$ (9.1), the functor $\operatorname{Ker}$ in 9.11 1. is $\pi$-accessible, and the set of strict
subobjects of $X$ has cardinal bounded above by $\pi$. Then $X$ is $\pi$-preaccessible.

Indeed, let $I$ be a set large relative to $\pi$, let $(Y_i)_{i \in I}$ be an inductive system in $E$ with inductive
limit $Y$, and let

$$ u_i,v_i : X \rightrightarrows Y_i $$

be a double arrow such that the composite double arrow

$$ u,v : X \rightrightarrows Y $$

satisfies $u=v$. Prove that there exists $j \geq i$ in $I$ such that $u_j=v_j$. For

[PDF p. 163]

this, consider the inductive system of double arrows

$$ u_j,v_j : X \rightrightarrows Y_j \qquad (j \geq i), $$

whose inductive limit is $(u,v)$. By hypothesis, one has

$$ X=\operatorname{Ker}(u,v)=\varinjlim_j \operatorname{Ker}(u_j,v_j)=\varinjlim_j X_j, $$

where $X_j=\operatorname{Ker}(u_j,v_j)$. But the $X_j$ are strict subobjects of $X$, so there exists a subset $I'$ of
$I$ formed by indices $j \geq i$, such that $\operatorname{card}I'\leq \pi$ and every $X_j$ is equal to one of the
$X_{j'}$ ($j' \in I'$). Since $I$ is large relative to $\pi$, there exists a majorant $j$ of $I'$ in $I$. Then $X_j$
contains all the $X_{j'}$, for $j' \geq i$, hence $X_j \to X$ is an epimorphism, since the family of the $X_{j'} \to X$
is epimorphic; it is therefore an isomorphism, since it is a strict monomorphism. Thus one has $u_j=v_j$, which proves
9.11.1.

The second assertion of 9.11 follows from the first and from the following lemma.

**Lemma 9.11.2.** Under conditions 9.11 1., 2., 3., let $X$ be an object of $E$, and let $\pi$ be an infinite cardinal
such that $E$ satisfies $L_\pi$ (9.1), $\operatorname{card}\operatorname{Ob}(C_/X)\leq \pi$, for two objects $X' \to X$
and $X'' \to X$ of $C_/X$, the fiber product $X' \times_X X''$ is $\pi$-preaccessible, and finally $X$ is
$\pi$-preadmissible. Then $X$ is $\pi$-accessible.

With the notation of the proof of 9.11.1, it suffices to prove that every morphism $u : X \to Y$ comes from a morphism

$$ u_i : X \to Y_i. $$

Now consider the family of morphisms $Y_i \to Y$, which is strictly epimorphic. Thanks to 2. and 3., the family of the
$Y_i \times_Y X \to X$ is also strictly epimorphic. On the other hand, for every $i$, since $C$ generates by strict
epimorphisms, the family of arrows

[PDF p. 164]

$$ T \to Y_i \times_Y X $$

with source in $C$ is strictly epimorphic. In the second alternative considered in 3., one can find such a strictly
epimorphic arrow with source a small sum of objects of $C$. By transitivity of the notion of strict universal epimorphic
family (II 2.5), it follows that the family of arrows

$$ f_\alpha : T_\alpha \to X $$

with source in $C$, which factor through one of the $Y_i \times_Y X$, is strictly epimorphic. Let $J$ be the index set
of this family, which has cardinal bounded by $\operatorname{card}\operatorname{Ob}(C_/X)\leq \pi$. For every
$\alpha \in J$, choose an $i=i(\alpha)\in I$ and an $X$-morphism $T_\alpha \to Y_i \times_Y X$, or equivalently a
$v_\alpha : T_\alpha \to Y_i$ such that $p_i v_\alpha=uf_\alpha$, where $p_i : Y_i \to Y$ is the canonical morphism.
Since $I$ is large relative to $\pi$, one can choose $i(\alpha)$ independent of $\alpha$, say $i$.

For every pair of indices $\alpha,\beta \in J$, consider the composites

$$ \operatorname{pr}_1 v_\alpha,\operatorname{pr}_2 v_\beta : T_\alpha \times_X T_\beta \rightrightarrows Y_i. $$

Their composites with $Y_i \to Y$ are equal. Since $T_\alpha \times_X T_\beta$ is $\pi$-preaccessible by hypothesis,
there exists an index $i'=i(\alpha,\beta)\geq i$ such that the composites of the arrows considered with $Y_i \to Y_{i'}$
are equal. Since the set of pairs $\alpha,\beta$ has cardinal $\leq \pi^2=\pi$ ($\pi$ being infinite), it follows again
that $i'$ may be chosen independently of $\alpha,\beta$. One may evidently suppose $i'=i$.

But then, since the family $(f_\alpha : T_\alpha \to X)$ is strictly epimorphic, one can find a morphism
$u_i : X \to Y_i$ such that $u_i f_\alpha=v_\alpha$. Then $p_i u_i=u$, because for every $\alpha$, one has

$$ (p_i u_i)f_\alpha=p_i(u_i f_\alpha)=p_i v_\alpha=uf_\alpha, $$

and the family of the $f_\alpha$ is epimorphic. This completes the proof of 9.11.2.

[PDF p. 165]

**Remark 9.11.3.** As a special case of 9.11, one sees that in the category $E$ every object is accessible, in each of
the following two cases:

1. $E$ is a $U$-abelian category with exact filtering inductive limits and admitting a small generating subcategory.
   Here, it is the second alternative of 9.11 3. which applies.
2. $E$ is the category of sheaves of sets on a topological space $X \in U$. More generally, it suffices that $E$ be the
   category of sheaves of sets on a $U$-site (II 2.1), or again that $E$ be a $U$-topos (IV 1.1).

**Definition 9.12.** Let $E$ be a category. A **cardinal filtration** of $E$ is an increasing filtration
$(\operatorname{Filt}^\pi(E))_{\pi \geq \pi_0}$ of $E$ by strictly full subcategories $\operatorname{Filt}^\pi(E)$,
indexed by the cardinals $\pi \in U$ such that $\pi \geq \pi_0$, where $\pi_0$ is a fixed infinite cardinal depending on
the cardinal filtration considered, and satisfying the following conditions:

1. For every $\pi \geq \pi_0$, $\operatorname{Filt}^\pi(E)$ is equivalent to a small category.

2. $E$ satisfies $L_{\pi_0}$ (9.1), and, for every $\pi \geq \pi_0$, $\operatorname{Filt}^\pi(E)$ is stable in $E$ under
   filtering inductive limits indexed by ordered sets $I$ large relative to $\pi_0$, such that $\operatorname{card}I\leq
   \pi$.

3. For every $\pi \geq \pi_0$ and every $X \in \operatorname{Ob}(E)$, one can find an isomorphism

$$ X \simeq \varinjlim_I X_i, $$

where $(X_i)_{i \in I}$ is an inductive system in $E$, indexed by an ordered set

[PDF p. 166]

$I$ large relative to $\pi$ (9.1), and where the $X_i$ lie in $\operatorname{Filt}^\pi(E)$. Moreover, if
$X \in \operatorname{Ob}(\operatorname{Filt}^{\pi'}(E))$, $\pi' \geq \pi$, then one may take $I$ such that
$\operatorname{card} I \leq (\pi')^\pi$.

**9.12.1.** Note that it follows from 2. and 3. that every $X \in \operatorname{Ob}(E)$ belongs to a
$\operatorname{Filt}^\pi(E)$, for $\pi$ sufficiently large.

**Example 9.12.2.** Take $E=U\text{-}\mathbf{Ens}$, $\pi_0=\aleph_0$, and $\operatorname{Filt}^\pi(E)$ the full
subcategory of $E$ formed by the sets $X$ such that $\operatorname{card}X\leq \pi$. More generally:

**Proposition 9.13.** Let $E$ be a $U$-category. Assume that $E$ is stable under small filtering inductive limits, under
sums of two objects and cokernels of double arrows, that $E$ is stable under fiber products, and that epimorphic
morphisms in $E$ are strict universal epimorphisms.

Let $C$ be a small full subcategory of $E$ generating by strict epimorphisms. Let $\pi_0$ be an infinite cardinal
$\geq \operatorname{card}\operatorname{Fl}(C)$. For every cardinal $\pi \geq \pi_0$, let $\operatorname{Filt}^\pi(E)$ be
the strictly full subcategory of $E$ formed by the objects $X$ of $E$ such that there exists a strict epimorphic family
$(X_i \to X)_{i \in I}$ with target $X$, such that $\operatorname{card} I\leq \pi$ and $X_i \in \operatorname{Ob}(C)$
for every $i \in I$. Then $(\operatorname{Filt}^\pi(E))_{\pi \geq \pi_0}$ is a cardinal filtration of $E$.

Moreover, for every $X \in \operatorname{Ob}(\operatorname{Filt}^\pi(E))$, the cardinal of the set of arrows of $C_/X$,
and a fortiori of the set of objects of $C_/X$, is bounded above by $\pi^{\pi_0}$.

This last assertion is exactly 7.6. To show that one has a cardinal filtration, one must prove conditions 1., 2., and 3.
of 9.12. Condition 1. follows at once from 7.5.2. For 2., suppose one has

$$ X=\varinjlim_I X_i, $$

with $\operatorname{card}I\leq \pi$ and

[PDF p. 167]

the $X_i \in \operatorname{Ob}(\operatorname{Filt}^\pi(E))$. Thus the family of canonical morphisms $X_i \to X$ is
strictly epimorphic. By the hypothesis on the $X_i$, for every $i \in I$ there exists a strict epimorphic family
$(X_{ij} \to X_i)_{j \in J_i}$, with $\operatorname{card}J_i\leq \pi$. Passing to the sums $\coprod_i X_i$ and
$\coprod_{i,j} X_{ij}$, one sees, by transitivity of strict universal epimorphisms (II 2.5), that the family of
composites

$$ X_{ij} \to X_i \to X $$

indexed by the sum set of the $J_i$, for $i \in I$, is strictly epimorphic. But one has $\operatorname{card}J\leq
\pi^2=\pi$, whence the conclusion. Note that we used only the fact that $\varinjlim_I X_i$ exists, and not the fact that
$I$ is large relative to $\pi_0$, or even filtering.

Finally prove 3. For every $X \in \operatorname{Ob}(E)$, the family of arrows $X_i \to X$ with source in
$\operatorname{Ob}(C)$ is strictly epimorphic, since $C$ generates by strict epimorphisms, and is evidently small; hence
there exists a cardinal $\pi \geq \pi_0$ such that $X \in \operatorname{Ob}(\operatorname{Filt}^\pi(E))$. It remains to
prove that, if one has cardinals $\pi'\geq \pi \geq \pi_0$ and if $X \in
\operatorname{Ob}(\operatorname{Filt}^{\pi'}(E))$, then one has an isomorphism

$$ X \simeq \varinjlim_I X_i, $$

with $I$ large relative to $\pi$, $\operatorname{card}I\leq(\pi')^\pi$, and the $X_i$ in
$\operatorname{Ob}(\operatorname{Filt}^\pi(E))$. But, since $C$ generates by strict epimorphisms, one has

$$ X \simeq \varinjlim_{C_/X} T. \tag{*} $$

Note also that, by successively adding to $C$ sums and cokernels of double arrows of $C$, and likewise for the category
thus obtained, and so on, one reduces to the case where $C$ is stable under sums of two objects in $E$ and under
cokernels of double arrows in $E$, without destroying the hypothesis
$\pi_0 \geq \operatorname{card}\operatorname{Fl}(C)$. One may further suppose that, if $E$ contains

[PDF p. 168]

a fixed initial object $\emptyset_E$, then $\emptyset_E \in \operatorname{Ob}(C)$. This implies that the category $C_/X$
is stable under sums of two objects and cokernels of double arrows. It is then filtering. It is nonempty, because if it
were empty, relation $(*)$ would show that $X$ is an initial object, hence $C_/X$ would contain the arrow
$\emptyset_E \to X$, a contradiction.

Let $I$ be the set, ordered by inclusion, of full subcategories $i$ of $C_/X$ which are filtering and such that
$\operatorname{card}\operatorname{Ob}(i)\leq \pi$. For every $i \in I$, let $X_i \in \operatorname{Ob}(E)$ be the
inductive limit of the composite functor $i \to C_/X \to E$, which exists by hypothesis. Then one evidently has

$$ \varinjlim_I X_i \simeq \varinjlim_{C_/X} T \simeq X. $$

On the other hand, we have already noted that $\operatorname{card}\operatorname{Ob}(C_/X)\leq(\pi')^{\pi_0}$. It follows
that $I$ is large relative to $\pi$, and that

$$ \operatorname{card}I\leq ((\pi')^{\pi_0})^\pi=(\pi')^{\pi\pi_0}=(\pi')^\pi, $$

by the following lemma, whose proof is left to the reader, where one takes $J=C_/X$ and $c=(\pi')^{\pi_0}$.

**Lemma 9.13.1.** Let $J$ be a filtering category, and let $c$ and $\pi$ be two cardinals such that
$c\geq \operatorname{Sup}(\operatorname{card}\operatorname{Fl}(J),\pi)$, and such that
$\operatorname{card}\operatorname{Hom}(j,j')\leq \pi_0$ for every pair of objects $j,j'$ of $J$. Let $I$ be the set of
full filtering subcategories $i$ of $J$ such that $\operatorname{card}\operatorname{Ob}(i)\leq \pi$. Then, ordered by
inclusion, $I$ is large relative to $\pi$, and one has $\operatorname{card}I\leq c^\pi$.

This completes the proof of 9.13.

[PDF p. 169]

**Remark 9.13.2.** A slight additional effort should make it possible to replace in 9.13 the hypothesis that $E$ is
stable under small filtering inductive limits by the hypothesis that $E$ satisfies $L$ (9.1), if one supposes $E$ stable
under small sums, or that every epimorphic family in $E$ is universal epimorphic. Then, in the proof of 9.13 3., one
must choose $\pi_0$ such that $E$ satisfies $L_{\pi_0}$, and restrict to the full subcategories $i$ of $C_/X$ which are
not only filtering, but such that the preordered set $\operatorname{Ob}(i)$ is large relative to $\pi_0$. Using 8. and
the hypothesis that $E$ satisfies $L_{\pi_0}$, one then finds that the $X_i$ exist, and one should conclude by a
suitable variant of 9.13.1, which the writer has not checked.

**Proposition 9.14.** Let $f : E \to F$ be an accessible functor (9.2) between two categories equipped with cardinal
filtrations $(\operatorname{Filt}^\pi(E))_{\pi \geq \pi_0}$ and $(\operatorname{Filt}^\pi(F))_{\pi \geq \pi'_0}$. Then
there exists a cardinal $\pi_1 \geq \operatorname{Sup}(\pi_0,\pi'_0)$ such that, for every cardinal $\pi \geq \pi_1$,
one has

$$ f(\operatorname{Filt}^\pi(E)) \subset \operatorname{Filt}^{\pi^{\pi_1}}(F). \tag{9.14.1} $$

In particular, if one has $\pi=2^c$ with $c\geq \pi_1$, whence $\pi^{\pi_1}=2^{c\pi_1}=2^c=\pi$, one has

$$ f(\operatorname{Filt}^\pi(E)) \subset \operatorname{Filt}^\pi(F). \tag{9.14.2} $$

Let us record at once the following corollary.

[PDF p. 170]

**Corollary 9.15.** Let $E$ be a category equipped with two cardinal filtrations
$(\operatorname{Filt}^\pi(E))_{\pi \geq \pi_0}$ and $(\operatorname{Filt}'^\pi(E))_{\pi \geq \pi'_0}$. Then there exists
a cardinal $\pi_1 \geq \operatorname{Sup}(\pi_0,\pi'_0)$ such that, for every cardinal $c \geq \pi_1$, putting
$\pi=2^c$, one has

$$ \operatorname{Filt}^\pi(E)=\operatorname{Filt}'^\pi(E). $$

**Proof of 9.14.** Let $c$ be a cardinal such that $c\geq \operatorname{Sup}(\pi_0,\pi'_0)$ and such that $f$ is
$c$-admissible. Let moreover $\pi_1\geq c$ be such that one has

$$ f(\operatorname{Filt}^c(E)) \subset \operatorname{Filt}^{\pi_1}(F). \tag{*} $$

Such a $\pi_1$ exists because $\operatorname{Filt}^c(E)$ is equivalent to a small category (9.12 1.). Hence
$f(\operatorname{Filt}^c(E))$ is too, so that one may apply 9.12.1 to the objects of the latter to find a
$\operatorname{Filt}^{\pi_1}(F)$ containing them all, taking into account that the $\operatorname{Filt}^\pi(F)$ are full
subcategories.

Let then $\pi \geq \pi_1$, and let $X \in \operatorname{Ob}(\operatorname{Filt}^\pi(E))$. Prove that
$f(X) \in \operatorname{Filt}^{\pi^{\pi_1}}(F)$. Indeed, write

$$ X=\varinjlim_I X_i, $$

with the $X_i \in \operatorname{Ob}(\operatorname{Filt}^c(E))$, $I$ large relative to $c$, and
$\operatorname{card}I\leq \pi^c\leq \pi^{\pi_1}$ (9.12 3.). Since $f$ is $c$-admissible and $I$ is large relative to
$c$, one has

$$ f(X) \simeq \varinjlim_I f(X_i). $$

And since $\operatorname{card}I\leq \pi^{\pi_1}$ and $f(X_i)\in \operatorname{Ob}(\operatorname{Filt}^{\pi_1}(F))\subset
\operatorname{Ob}(\operatorname{Filt}^{\pi^{\pi_1}}(F))$ by $(*)$, one has
$f(X)\in \operatorname{Filt}^{\pi^{\pi_1}}(F)$ by 9.12 2., QED.

**9.15.1.** The notion of cardinal filtration 9.12 has little interest except when the objects of $E$ are accessible.
Let us point out that it follows from 9.11 that this condition is satisfied when, in addition to the hypotheses

[PDF p. 171]

of 9.13, one assumes that the functor $\operatorname{Ker}$ on the category of double arrows of $E$ is accessible. Let us
also record:

**Proposition 9.16.** Let $E$ be a category equipped with a cardinal filtration
$(\operatorname{Filt}^\pi(E))_{\pi \geq \pi_0}$. Suppose that the elements of $\operatorname{Filt}^{\pi_0}(E)$ are
accessible objects of $E$. Then there exists a cardinal $\pi_1 \geq \pi_0$ in $U$ such that the objects of
$\operatorname{Filt}^{\pi_0}(E)$ are $\pi_1$-accessible. If $\pi_1$ is so chosen, then, for every cardinal
$\pi \geq \pi_1$, one has, with the notation of 9.3.1:

$$ E_\pi \subset \operatorname{Filt}^\pi(E) \subset E_{\pi^{\pi_0}}. \tag{9.16.1} $$

The existence of $\pi_1$ follows immediately from the fact that $\operatorname{Filt}^{\pi_0}(E)$ is equivalent to a
small category (9.12 1.). Let then $\pi \geq \pi_1$.

If $X$ is in $\operatorname{Filt}^\pi(E)$, write

$$ X \simeq \varinjlim_I X_i, $$

with $\operatorname{card}I\leq \pi^{\pi_0}$ and $X_i \in \operatorname{Ob}(\operatorname{Filt}^{\pi_0}(E))$ for every
$i$ (9.12 3.). Then it follows from 9.9 that $X$ is $\pi^{\pi_0}$-accessible, whence the second inclusion (9.16.1).

Suppose that $X$ is $\pi$-accessible, and write

$$ X \simeq \varinjlim_I X_i, $$

with $I$ large relative to $\pi$ and the $X_i \in \operatorname{Ob}(\operatorname{Filt}^\pi(E))$ (9.12 3.). By the
hypothesis on $X$, the given isomorphism $X \simeq \varinjlim_I X_i$ factors through one of the $X_i$, so $X$ is
isomorphic to a direct factor of this $X_i$. One concludes that $X \in \operatorname{Ob}(\operatorname{Filt}^\pi(E))$,
hence the first inclusion (9.16.1), by the following lemma.

**Lemma 9.16.2.** Every object of $E$ which is a direct factor of an object of $\operatorname{Filt}^\pi(E)$ lies in
$\operatorname{Filt}^\pi(E)$.

Indeed, if $X$ is the image of a projector $p$ in the object $Y$ of $E$, that is, of an endomorphism $p$ such that
$p^2=p$, and if $I$ is a filtering ordered set,

[PDF p. 172]

$X$ is the inductive limit of the filtering inductive system $(Y_i)_{i \in I}$ defined by $Y_i=Y$ for every $i$, with
$p : Y_i \to Y_j$ if $i<j$. Taking $I$ large relative to $\pi_0$ and $\operatorname{card}I\leq \pi$, one sees that if
$Y \in \operatorname{Filt}^\pi(E)$, then the same is true of $X$ by 9.12 2.

**Corollary 9.17.** Under the conditions of 9.16, for every cardinal $c \geq \pi_1$, putting $\pi=2^c$,
$\operatorname{Filt}^\pi(E)$ is identical to the strictly full subcategory $E_\pi$ of $E$ formed by the $\pi$-accessible
objects.

**Corollary 9.18.** Let $E$ be a category satisfying condition $L_\pi$ (9.1), where $\pi$ is a cardinal, and let $C$ be
a full subcategory of $E$. Denote by $\operatorname{Ind}(C)_\pi$ the full subcategory of the category
$\operatorname{Ind}(C)$ of ind-objects of $C$ (8.2), formed by the ind-objects of the form $(X_i)_{i \in I}$, where $I$
is an ordered set large relative to $\pi$. Consider the canonical functor

$$ (X_i)_{i \in I} \mapsto \varinjlim_I X_i : \operatorname{Ind}(C)_\pi \to E. \tag{9.18.1} $$

1. For this functor to be fully faithful, it is necessary and sufficient that every object $X$ of $C$ be a
   $\pi$-accessible object (9.3) of $E$.
2. Place ourselves under the conditions of 9.17, in particular $\pi=2^c$, and take $C=\operatorname{Filt}^\pi(E)$. Then
   the functor (9.18.1) is an equivalence of categories.

Assertion 1. is an immediate generalization of 8.7.5 a), and is proved in the same way. Then 2. follows from 9.17 and
from condition 9.12 3. of cardinal filtrations, which implies that the functor considered is essentially surjective.

[PDF p. 173]

**Corollary 9.19.** Under the conditions of 9.17, let $C=\operatorname{Filt}^\pi(E)$ and let $F$ be a $U$-category.
Consider the functor

$$ \operatorname{Hom}(E,F)_\pi \to \operatorname{Hom}(C,F), \tag{9.19.1} $$

induced by the "restriction to $C$" functor, $f \mapsto f|C$, where the source of (9.19.1) is the category of
$\pi$-accessible functors from $E$ to $F$ (9.2). The preceding functor is fully faithful. If $F$ satisfies condition
$L_\pi$ (9.1), then the functor (9.19.1) is an equivalence of categories.

The first assertion is proved like 7.8, using 9.18 2. The second is obtained by constructing a quasi-inverse to
(9.19.1), associating to every functor $f : C \to F$ the functor

$$ (X_i)_{i \in I} \mapsto \varinjlim_I f(X_i) $$

from $\operatorname{Ind}(E_\pi)$ to $F$, and using 9.18 2. to deduce from it a functor $\overline{f} : E \to F$.
Everything amounts to showing that the latter is $\pi$-accessible. This is proved like the analogous assertion 8.7.3.

**Corollary 9.20.** Let $E$ be a category admitting a cardinal filtration and such that every object of $E$ is
accessible (cf. 9.16), and let $F$ be a category. Then:

1. The category $\operatorname{Hom}(E,F)_{\operatorname{acc}}$ of accessible functors from $E$ to $F$ (9.2) is a
   $U$-category. Recall (9.0) that the given categories $E,F$ are assumed to be $U$-categories.
2. Suppose that $F$ is stable under small filtering inductive limits. For every full subcategory $C$ of $E$ equivalent
   to a small category, with inclusion functor $i : C \to E$, consider the corresponding functor

[PDF p. 174]

$$ i_! : \operatorname{Hom}(C,F) \to \operatorname{Hom}(E,F) \qquad (5.1) $$

For a functor $f : E \to F$ to be accessible, it is necessary and sufficient that there exist a small subcategory $C$ of
$E$ such that $f$ lies in the essential image of the preceding functor $i_!$.

**Proof.** 1. It suffices to prove that, for every cardinal $\pi$ such that $E$ satisfies $L_\pi$, the full subcategory
$\operatorname{Hom}(E,F)_\pi$ of $\operatorname{Hom}(E,F)_{\operatorname{acc}}$ is a $U$-category. It evidently suffices
to check this for cardinals of the form $2^c$, with $c$ sufficiently large. But then this follows from 9.19, since, with
$C=\operatorname{Filt}^\pi(E)$ essentially small, $\operatorname{Hom}(C,F)$ is evidently a $U$-category.

2. By transitivity of the formation of the functors $i_!$, in the statement one may restrict to subcategories $C$ of the
form $\operatorname{Filt}^\pi(E)$, where $\pi$ is as in 9.17. One then sees easily that the composite functor

$$
\operatorname{Hom}(\operatorname{Filt}^\pi(E),F)
\to
\operatorname{Hom}(E,F)_\pi
\to
\operatorname{Hom}(E,F),
$$

where the first arrow is quasi-inverse to (9.19.1), and the second is the inclusion, is none other than the functor
$i_!$, up to isomorphism. Thus assertion 2. follows from 9.19.

**Exercise 9.20.1.** The present exercise uses the notions of site and topos, developed in Exposes II and IV. Let $E$ be
a $U$-topos, let $V$ be a universe such that $U \in V$, let $C$ be a small full generating subcategory of the $U$-topos
$E$, and let $\pi_0 \in U$ be an infinite cardinal such that $\pi_0 \geq \operatorname{card}\operatorname{Fl}(C)$. For
every cardinal $\pi \geq \pi_0$, $\pi \in U$, let $\operatorname{Filt}^\pi(E)$ be the strictly full subcategory of $E$
formed by the objects $X$ such that there exists a strict epimorphic family $(X_i \to X)_{i \in I}$ with target $X$,
such that $\operatorname{card}I\leq \pi$ and $X_i \in \operatorname{Ob}(C)$ for every $i \in I$.

[PDF p. 175]

1. Show that $(\operatorname{Filt}^\pi(E))_{\pi \geq \pi_0}$ is a cardinal filtration of the $U$-category $E$, and that
   one can choose $\pi_0$ such that, for every $\pi \geq \pi_0$, one has the inclusions

$$ E_\pi \subset \operatorname{Filt}^\pi(E) \subset E_{\pi^{\pi_0}}, $$

where, for every cardinal $c$, $E_c$ denotes the strictly full subcategory of $E$ formed by the $c$-accessible objects.

2. Choose a cardinal $\pi \geq \pi_0$ such that $\pi=\pi^{\pi_0}$, for example $\pi=2^c$ with $c>\pi_0$, and put
   $C=\operatorname{Filt}^\pi(E)$. Show that one has an equivalence of categories

$$ \operatorname{Ind}(C)_\pi \simeq E, $$

with the notation $\operatorname{Ind}(C)_\pi$ of 9.18.

3. Keep the notation of 2. Let $V$ be a universe such that $U \subset V$, and let $\widetilde{E}_V$ be the $V$-topos of
   $V$-sheaves on the site $E$ equipped with its canonical topology. Denote by $\operatorname{Ind}(C,V)_\pi$ the
   category of $V$-Ind-objects of $C$, indexed by preordered index sets large relative to $\pi$. Show that one has an
   equivalence of categories

$$ \operatorname{Ind}(C,V)_\pi \simeq \widetilde{E}_V. $$

4. Let $c \in V$ be a cardinal, and let $\operatorname{Ind}(E,V)'_c$ be the full subcategory of
   $\operatorname{Ind}(E,V)$ formed by the $V$-ind-objects of $E$ indexed by a preordered set which is large relative to
   every cardinal $<c$. By taking $c=\operatorname{card}U$,

[PDF p. 176]

   show that one has an equivalence of categories

$$ \operatorname{Ind}(E,V)'_c \simeq \widetilde{E}_V. $$

**9.21.** The present section 9.21 develops technical preliminaries for the proof of Theorem 9.22 below, which is the
main result of the present paragraph 9. Let

$$ p : E \to B \tag{9.21.1} $$

be a fibering functor, where $B$ is a small category, and where the inverse image functors

$$ f^* : E_\beta \to E_\alpha $$

associated with arrows $f : \alpha \to \beta$ of $B$ are accessible (9.2). In particular, the fiber categories
$E_\alpha$ ($\alpha \in \operatorname{Ob}(B)$) satisfy condition $L$ (9.1). Since $B$ is small, there exists a cardinal
$\pi'_0 \in U$ such that all the categories $E_\alpha$ satisfy condition $L_{\pi'_0}$. Let $\pi_0 \in U$ be an infinite
cardinal $>\pi'_0$, so that one has

$$ \pi_0>\pi'_0,\quad \text{and } E_\alpha \text{ satisfies } L_{\pi'_0} \text{ for all } \alpha\in\operatorname{Ob}(B).
\tag{9.21.2}
$$

Moreover, the hypotheses made imply at once the existence of a cardinal $c \in U$ satisfying the following conditions:

```text
a) c is infinite,
b) c >= card Fl(B),
c) for every arrow f : alpha -> beta in B, the functor
   f* : E_beta -> E_alpha is c-accessible.       (9.21.3)
```

[PDF p. 177]

Suppose in addition that one can find, for each $\alpha \in \operatorname{Ob}(B)$, a full subcategory $C_\alpha$ of
$E_\alpha$, satisfying the following conditions:

```text
a) For every X in Ob(C_alpha), X is c-accessible in E_alpha (9.3).
b) For every X in Ob(E_alpha), one can find an isomorphism
   X ~= colim_I X_i in E_alpha,
   where the X_i are in C_alpha and where I is an ordered set
   large relative to c.                          (9.21.4)
```

Let $\pi$ be a cardinal such that one has

$$ \pi \geq \pi_0,\quad \text{hence } \pi>\pi'_0. \tag{9.21.5} $$

For every $\alpha \in \operatorname{Ob}(B)$, let

$$ C^\pi_\alpha \subset E_\alpha \tag{9.21.6} $$

be the full subcategory formed by the objects which can be represented in the form $\varinjlim_I X_i$, where $I$ is an
ordered set large relative to $\pi'_0$, such that $\operatorname{card}I\leq \pi$, and where the $X_i$ lie in $C_\alpha$.
It is then clear, thanks to 7.5.2, that $C^\pi_\alpha$ is essentially small, that is, equivalent to a small category.

Let

$$ F=\operatorname{Hom}_B(B,E) \tag{9.21.7} $$

be the category of sections of $E$ over $B$, and let

$$ F^\pi \subset F \tag{9.21.8} $$

be the strictly full subcategory of $F$ formed by the sections $X : \alpha \mapsto X(\alpha)$ such that, for every
$\alpha \in \operatorname{Ob}(B)$, one has

[PDF p. 178]

$$ X(\alpha) \in C^\pi_\alpha. $$

It is clear, since the $C^\pi_\alpha$ are essentially small, that the category $F^\pi$ is so as well. We shall show that
this category is generating, and more precisely:

**Lemma 9.21.9.** Under the preceding conditions and with the preceding notation, one has the following:

1. Every object of $F$ is accessible (9.3). If $d$ is a cardinal $\geq \pi'_0$, and if $\alpha \mapsto X(\alpha)$ is an
   element of $F$ such that for every $\alpha$, $X(\alpha)$ is a $d$-accessible object of $E_\alpha$, then $X$ is
   $d$-accessible in $F$.
2. Suppose $\pi \leq c$, or that $\pi'_0$ is finite, that is, the $E_\alpha$ are stable under small filtering inductive
   limits. Then every object $X$ of $F$ is isomorphic to an object of the form $\varinjlim_I X_i$, where the $X_i$ lie
   in $F^\pi$ and where $I$ is large relative to $\pi$.

To prove 1., note that by (9.21.4) and 9.9, every object of $E_\alpha$ is accessible. On the other hand, $F$ satisfies
condition $L_{\pi'_0}$, by the following lemma.

**Lemma 9.21.10.** Let $p : E \to B$ be a fibering functor, let $F=\operatorname{Hom}_B(B,E)$, let $I$ be a category,
and let $i \mapsto X_i$ be a functor from $I$ to $F$. For $\varinjlim_I X_i$ to be representable in $F$, it suffices
that, for every $\alpha \in \operatorname{Ob}(B)$, $\varinjlim_I X_i(\alpha)$ be representable in the fiber category
$E_\alpha$. When this is so, $\varinjlim_I X_i$ is computed "argument by argument." In particular, if the fiber
categories satisfy condition $L_{\pi'_0}$, where $\pi'_0$ is a given cardinal, the same is true of $F$.

[PDF p. 179]

We leave the details of the easy proof of 9.21.10 to the reader, merely observing that it is convenient to use the
following result, whose proof is immediate.

**Corollary 9.21.10.1.** With the hypotheses and notation of 9.21.10 for $p : E \to B$ and for $I$, for every
$\alpha \in \operatorname{Ob}(B)$, the inclusion functor

$$ E_\alpha \to E $$

commutes with inductive limits of type $I$.

Returning to the general conditions of 9.21.9, let $X$ be an object of $F$. Since, for every
$\alpha \in \operatorname{Ob}(B)$, $X(\alpha)$ is accessible in $E_\alpha$, there exists a cardinal $d \in U$ such that,
for every $\alpha$, $X(\alpha)$ is $d$-accessible in $E_\alpha$. One may choose $d \geq \pi'_0$, so that $F$ satisfies
$L_d$ by 9.21.10. Again using 9.21.10 for the computation of inductive limits $\varinjlim_I Y_i$ in $F$, with $I$ large
relative to $d$, one sees at once that $X$ is $d$-accessible. This proves 1.

We shall now prove 9.21.9 2. in several steps, from 9.21.11 to 9.21.16. Let $X$ be an object of $F$. By 9.21.4 b), for
every $\alpha \in \operatorname{Ob}(B)$, one can find an ordered set $I_\alpha$ large relative to $c$, and an
isomorphism

$$ X(\alpha) \simeq \varinjlim_{i \in I_\alpha} X(\alpha)_i $$

where $i \mapsto X(\alpha)_i$ is an inductive system of type $I_\alpha$ in $E_\alpha$, with the $X(\alpha)_i$ in
$C_\alpha$. Consider the product ordered set

$$ I=\prod_{\alpha \in \operatorname{Ob}(B)} I_\alpha. $$

It is clear that it is large relative to $c$, and that the preceding systems

[PDF p. 180]

give rise to inductive systems in the $E_\alpha$,

$$ i \mapsto X(\alpha)_i \in \operatorname{Ob}(C_\alpha), \qquad i \in \operatorname{Ob}(I), \tag{9.21.11} $$

indexed by the same ordered set $I$, and to isomorphisms

$$ X(\alpha) \simeq \varinjlim_I X(\alpha)_i \quad \text{in } E_\alpha, \tag{9.21.12} $$

for every $\alpha \in \operatorname{Ob}(B)$. In what follows, the data (9.21.11) and (9.21.12) are assumed fixed.

**Lemma 9.21.13.** Under the preceding conditions, one can find a map $\varphi : I \to I$ such that $\varphi(i)\geq i$
for every $i \in I$, and a map $(i,f)\mapsto \lambda(i,f)$ from $I \times \operatorname{Fl}(B)$ to
$\operatorname{Fl}(E)$, satisfying the following conditions.

1. For $i \in I$ and $(f : \alpha \to \beta) \in \operatorname{Fl}(B)$, $\lambda(i,f)$ is an $f$-morphism from
   $X(\alpha)_i$ to $X(\beta)_{\varphi(i)}$, making the diagram

```text
X(alpha)  --X(f)-->  X(beta)
  ^                  ^
  |                  |
X(alpha)_i --lambda(i,f)-> X(beta)_{phi(i)}

alpha --f--> beta,
```

commutative, where the vertical arrows are the canonical morphisms deduced from (9.21.12).

[PDF p. 181]

2. For every $i \in I$ and $(f : \alpha \to \beta) \in \operatorname{Fl}(B)$, one has commutativity in the diagram

```text
X(alpha)_{phi(i)}  --lambda(phi(i), f)-->  X(beta)_{phi^2(i)}
      ^                                          ^
      |                                          |
X(alpha)_i       --lambda(i, f)------>  X(beta)_{phi(i)}

alpha --f--> beta.
```

3. For every pair of consecutive arrows $\alpha \xrightarrow{f} \beta \xrightarrow{g} \gamma$ of $B$, one has
   commutativity in the following diagram:

```text
X(alpha) --X(f)--> X(beta) --X(g)--> X(gamma)
  ^                  ^                  ^
  |                  |                  |
X(alpha)_i --lambda(i, f)-> X(beta)_{phi(i)}
   \                                      \
    \--lambda(i, gf)--> X(gamma)_{phi(i)} --> X(gamma)_{phi^2(i)}
                       ^
                       |
               lambda(phi(i), g)

alpha --f--> beta --g--> gamma,
```

where the vertical arrows are those deduced from (9.21.12).

[PDF p. 182]

Moreover, note that the commutativity of the two upper trapezoids in 2. is already contained in 1., so that 2. in fact
asserts commutativity of the lower triangle of the diagram considered.

Let us prove 9.21.13. Let $i \in I$ and let $f : \alpha \to \beta$ be an arrow in $B$. Consider the composite

$$ X(\alpha)_i \to X(\alpha) \xrightarrow{X(f)} X(\beta) \simeq \varinjlim_j X(\beta)_j. $$

It defines a morphism in $E$:

$$
X(\alpha)_i \to f^*(X(\beta)) \simeq f^*(\varinjlim_j X(\beta)_j) \simeq \varinjlim_j f^*(X(\beta)_j),
$$

where the last equality comes from the fact that $f^*$ is $c$-accessible (9.21.3 c) and that $I$ is large relative to
$c$. By (9.21.4 a), since $X(\alpha)_i \in \operatorname{Ob}(C_\alpha)$, the morphism considered factors through an
$f^*(X(\beta)_j)$, where $j$ depends a priori on $i$ and on $f \in \operatorname{Fl}(B)$. But by (9.21.3 b), and since
$I$ is large relative to $c$, one can choose $j$ independently of $f$, say $j=\varphi(i)$. Since $I$ is filtering, one
may suppose $\varphi(i)\geq i$. Thus, for $i \in I$ and $f \in \operatorname{Fl}(B)$, one obtains a morphism

$$ X(\alpha)_i \to f^*(X(\beta)_{\varphi(i)}), $$

or equivalently an $f$-morphism

$$ \lambda(i,f) : X(\alpha)_i \to X(\beta)_{\varphi(i)}, $$

which, by construction, makes diagram $D(f)$ of 1. commutative.

[PDF p. 183]

Now consider, for given $i,f,g$, the lower triangle of the diagram considered in 9.21.13 3. It is not clear that it is
commutative, but the two composites

$$ X(\alpha)_i \rightrightarrows X(\beta)_{\varphi^2(i)} $$

become equal after composition with $X(\beta)_{\varphi^2(i)}\to X(\beta)$, as follows from the commutativity of the two
upper trapezoids and of the global boundary trapezoid, which are diagrams $D(f)$, $D(g)$, and $D(gf)$ respectively.
Thus, since $X(\alpha)_{\varphi^2(i)}$ is $c$-accessible (9.21.4 a) and

$$ X(\alpha) \simeq \varinjlim_{j \in I} X(\alpha)_j $$

with $I$ large relative to $c$, it follows that one can find an element $j \geq \varphi^2(i)$ of $I$ such that the two
arrows considered become equal after composition with $X(\beta)_{\varphi^2(i)}\to X(\beta)_j$. A priori, $j$ depends on
$i,f,g$. But, for fixed $i$, the set of possible pairs $f,g$ has cardinal $\leq c^2=c$, by (9.21.3 a) and b). Since $I$
is large relative to $c$, one may choose $j$ independently of $f$ and $g$, say
$j=\varphi'(i)\geq \varphi^2(i)\geq \varphi(i)$.

Let then, for every $i \in I$ and $f : \alpha \to \beta$, $\lambda'(i,f)$ be the composite $f$-morphism

$$ X(\alpha)_i \to X(\beta)_{\varphi(i)} \to X(\beta)_{\varphi'(i)}, $$

where the second arrow is the transition morphism. It is then immediate, by construction, that $(\varphi',\lambda')$
satisfies conditions 9.21.13 1. and 3., for $(\varphi,\lambda)$. Proceeding similarly for condition 2., one sees that
$\varphi'$ can be chosen so that this condition too is satisfied for $(\varphi',\lambda')$. This completes the proof of
9.21.13.

[PDF p. 184]

**9.21.14.** Let now $J \subset I$ be a subset of $I$ satisfying the following conditions:

1. $J$ is filtering.
2. For every $j \in J$, one has $\varphi(j)\in J$.
3. For every $\alpha \in \operatorname{Ob}(B)$,

$$ X_J(\alpha)=\varinjlim_{i \in J} X(\alpha)_i $$

is representable in $E_\alpha$.

Conditions 1. and 3. are satisfied in particular if $J$ is large relative to $\pi'_0$ (9.21.2). It then follows from
9.21.10.1 that, for every $\alpha \in \operatorname{Ob}(B)$, $X_J(\alpha)$ is the inductive limit
$\varinjlim_{i \in J}X(\alpha)_i$ in $E$.

Now, for an arrow $f : \alpha \to \beta$ of $B$, the arrows $\lambda(i,f)$, for variable $i$ in $J$, define, thanks to
9.21.13 2., a morphism of ind-objects from $(X(\alpha)_i)_{i \in J}$ to $(X(\beta)_i)_{i \in J}$. Passing to inductive
limits, one deduces a homomorphism

$$ X_J(f) : X_J(\alpha) \to X_J(\beta), $$

which is manifestly an $f$-homomorphism. Using 9.21.13 3., one obtains the transitivity relations

$$ X_J(gf)=X_J(g)X_J(f), $$

so that one has defined a section $X_J \in \operatorname{Ob}(F)$ of $E$ over $B$. Finally, 9.21.13 1. shows that the
canonical homomorphisms

$$ X_J(\alpha)\to X(\alpha),\qquad \alpha \in \operatorname{Ob}(B), $$

are functorial in $\alpha$, so that one has a canonical homomorphism

$$ u_J : X_J \to X. $$

[PDF p. 185]

On the other hand, if $J'\supset J$ is another subset of $I$ satisfying conditions 1., 2., 3. above, one obtains a
canonical homomorphism

$$ u_{J',J} : X_J \to X_{J'}, $$

so that the $X_J$ form an inductive system in $F$, parametrized by the set, ordered by inclusion, of subsets $J$ of $I$
satisfying the conditions considered. Finally, the homomorphisms $u_J$ define a homomorphism from this inductive system
to the constant inductive system defined by $X$.

**9.21.15.** Now let $K$ be a set of subsets $J$ of $I$, satisfying conditions 1., 2., 3. considered in 9.21.14, and
suppose that $K$ is filtering and has union $I$. Then it is clear that one has

$$ \varinjlim_{J \in K} X_J \simeq X, $$

using 9.21.10.1, which reduces us to checking that one has an isomorphism argument by argument.

Take for example for $K$ the set of all subsets $J$ of $I$ which are large relative to $\pi'_0$, stable under $\varphi$,
and such that $\operatorname{card}J\leq \pi$. Then, by definition (9.21.6) of $C^\pi_\alpha$, for every
$\alpha \in \operatorname{Ob}(B)$, one has $X_J(\alpha) \in \operatorname{Ob}(C^\pi_\alpha)$, hence
$X_J \in \operatorname{Ob}(F^\pi)$. Consequently, 9.21.9 2. will be proved if we establish that $K$ is large relative to
$\pi$, hence filtering, and has union $I$. For this it will evidently suffice to prove that every subset $S$ of $I$ such
that $\operatorname{card}S\leq \pi$ is contained in a $J \in K$. This

[PDF p. 186]

will follow from the preliminary hypothesis stated in 9.21.9 2. and from the following lemma.

**Lemma 9.21.16.** Let $I$ be an ordered set, let $\pi$ be an infinite cardinal, and let $\varphi : I \to I$ be a map.

1. Suppose $I$ is filtering. Then, for every subset $S$ of $I$ such that $\operatorname{card}S\leq \pi$, there exists a
   filtering subset $J \supset S$ of $I$, such that $\varphi(J)\subset J$ and $\operatorname{card}J\leq \pi$.
2. Let $\pi'_0$ be a cardinal $<\pi$, and suppose $I$ is large relative to $\pi$. Then, for every subset $S$ of $I$ such
   that $\operatorname{card}S\leq \pi$, there exists a subset $J \supset S$ of $I$ large relative to $\pi'_0$, such that
   $\varphi(J)\subset J$ and $\operatorname{card}J\leq \pi$.

Prove 2., for example, the proof of 1. being analogous and simpler. Let $P$ be the set of subsets of $I$ of cardinal
$\leq \pi$, and let $T \mapsto i_T : P \to I$ be a map such that, for $T \in P$, $i_T$ is a majorant of $T$ in $I$. The
existence of this map simply expresses the hypothesis that $I$ is large relative to $\pi$.

Let $A$ be a well-ordered set such that $\operatorname{card}A=\pi$, and such that, for every $a \in A$, the set of
$a'\leq a$ has cardinal $<\pi$. It follows in particular, since $\pi'_0<\pi$, that $A$ is large relative to $\pi'_0$.
Define by transfinite recursion maps

$$ S \mapsto S_a : P \to P \qquad (a \in A) $$

by the following formulas:

$$
S_0=S,\qquad
S_{a+1}=S_a \cup \varphi(S_a) \cup \{i_{S_a}\},\qquad
S_a=\bigcup_{a'<a}S_{a'} \quad \text{if } a \text{ is a limit ordinal}.
$$

[PDF p. 187]

Put, for $S \in P$,

$$ J(S)=\bigcup_{a \in A}S_a. $$

It is then clear that $J(S)\supset S$, that $J(S)$ is stable under $\varphi$, that $\operatorname{card}J(S)\leq \pi$
since $\operatorname{card}A=\pi$, and finally that $J(S)$ is large relative to $\pi'_0$, using the fact that $A$ is
large relative to $\pi'_0$.

This proves 9.21.16 and completes the proof of 9.21.9.

Let us also record a variant of 9.21.9.

**Lemma 9.21.17.** The notation is that of 9.21.9. Denote by $F'$ the full subcategory $\operatorname{Homcart}_B(B,E)$
of $F=\operatorname{Hom}_B(B,E)$ formed by the cartesian sections of $E$ over $B$. Then:

1. Every object of $F'$ is accessible. More precisely, let $\alpha \mapsto X(\alpha)$ be an element of $F'$, and let $d$
   be a cardinal such that $d\geq \pi'_0$, $d\geq c$, and such that for every $\alpha \in \operatorname{ob}B$,
   $X(\alpha)$ is a $d$-accessible object of $E_\alpha$. Then $X$ is a $d$-accessible object of $F'$.
2. Suppose $\pi \leq c$ and the functors $f^* : E_\beta \to E_\alpha$ are $\pi'_0$-accessible, or that the categories
   $E_\alpha$ are stable under small filtering inductive limits and the functors $f^* : E_\beta \to E_\alpha$ commute
   with said inductive limits. Then every object $X$ of $F'$ is isomorphic to an object of the form $\varinjlim_I X_i$,
   where for every $i \in I$, $X_i$ is an object of the full subcategory $F'^\pi=F'\cap F^\pi$ of $F'$, and where $I$ is
   large relative to $\pi$.

[PDF p. 188]

The proof being entirely analogous to that of 9.21.9, we merely indicate the points where a modification of the latter
is necessary. First note:

**Lemma 9.21.18.** Statement 9.21.10 remains valid when one replaces $F=\operatorname{Hom}_B(B,E)$ by
$F'=\operatorname{Homcart}_B(B,E)$, provided one assumes that the inverse image functors $f^* : E_\beta \to E_\alpha$
commute with inductive limits of type $I$.

Thus, under the conditions of 9.21.17, if $d$ is a cardinal such that $d\geq c$ and $d\geq \pi'_0$, it follows from what
precedes and from hypothesis (9.21.3 c)) that for every ordered set $I$ large relative to $d$, inductive limits of type
$I$ are representable in $F'$ and are computed argument by argument, whence conclusion 9.21.17 (i) by an immediate
argument. To prove (ii), one needs the following supplement to 9.21.13:

**Lemma 9.21.19.** Under the conditions of 9.21.13, suppose that $X \in \operatorname{ob}F'$, i.e. that $X$ is a
cartesian section of $E$ over $B$. Then the conclusion can be strengthened by the assertion that there exists a function
$\mu$ which, to every $i \in I$ and every arrow $f : \alpha \to \beta$ of $B$, associates a morphism

$$ \mu(i,f) : f^*X(\beta)_i \to X(\alpha)_{\varphi(i)} $$

in $E_\alpha$, in such a way that:

d) For every $i \in I$ and every arrow $f : \alpha \to \beta$ of $B$, the two following diagrams are commutative.

[PDF p. 189]

```text
X(alpha)_{phi(i)}  --lambda(phi(i), f)-->  f*X(beta)_{phi^2(i)}
      ^                                          ^
      | mu(i, f)                                 |
      |                                          |
f*X(beta)_i --------------------------------------

X(alpha)_i  ------------------>  f*X(beta)_{phi(i)}
  | lambda(i, f)                         ^ mu(phi(i), f)
  v                                      |
X(alpha)_{phi(i)} <-----------------------
```

To prove it, proceed as in 9.21.3, considering the composite morphism

$$ f^*(X(\beta)_i) \to f^*(X(\beta)) \xrightarrow{X(f)^{-1}} X(\alpha), $$

where, as already in the writing of condition d), an $f$-morphism $R\to S$ of $E$ is identified in the notation with the
corresponding morphism $R\to f^*(S)$ of $E_\alpha$. Since $X(\alpha)=\varinjlim_j X(\alpha)_j$, and $I$ is large
relative to $c$, one can factor the preceding morphism through one of the $X(\alpha)_j$, where $j$ depends a priori on
$i$ and on $f$, but may be chosen independently of $f$; call this choice $\psi(i)$. After enlarging the function
$\varphi$ of 9.21.13, one may suppose $\psi=\varphi$. Proceeding as for conditions b) and c) of 9.21.13, one sees that,
after enlarging the map $\varphi$ again, one may suppose that the two diagrams of 9.21.19 d) are commutative.

**9.21.20.** With $\varphi$ chosen as in 9.21.19, take up again the argument of 9.21.14, where one must however suppose
that $J$ satisfies, in addition to conditions a), b), c), the condition:

d) For every arrow $f : \alpha \to \beta$ in $B$, the functor $f^* : E_\beta \to E_\alpha$ commutes with inductive
limits of type $J$.

[PDF p. 190]

I claim that, with this additional condition, the section $X_J$ of $E$ over $B$ is cartesian, i.e. for every arrow
$f : \alpha \to \beta$ of $B$, the morphism

$$ (*)\qquad X_J(\alpha) \to f^*X_J(\beta) $$

is an isomorphism. Indeed, by condition d) above, the target of the morphism considered is identified with
$\varinjlim_{i \in J} f^*(X(\beta)_i)$, and the morphism is obtained by passing to $\varinjlim_J$ from the morphism of
ind-objects in $E_\alpha$

$$ (X(\alpha)_i)_{i \in J} \to (f^*(X(\beta)_i))_{i \in J}, $$

deduced from the morphisms $\lambda(i,f) : X(\alpha)_i \to f^*(X(\beta)_{\varphi(i)})$, for $i \in J$. But the
conditions stated in 9.21.19 ensure that the preceding homomorphism of ind-objects is in fact an isomorphism, an inverse
being obtained from the homomorphism deduced from the system of the $\mu(i,f)$, for $i \in J$. This proves our assertion
that $(*)$ is an isomorphism, hence that $X \in \operatorname{ob}F'$.

**9.21.21.** We shall now suppose that the functors $f^* : E_\beta \to E_\alpha$ are $\pi'_0$-accessible. Then the
conditions on $J$ considered in 9.21.20 are satisfied if $J$ is large relative to $\pi'_0$, stable under $\varphi$, and
such that $\operatorname{card}J\leq \pi$, and the proof of 9.21.17 is completed as in 9.21.15.

[PDF p. 191]

**Theorem 9.22.** Let $p : E \to B$ be a fibering functor, where $B$ is a category essentially equivalent to a small
category, and where for every arrow $f : \alpha \to \beta$ in $B$, the inverse image functor
$f^* : E_\beta \to E_\alpha$ is accessible (9.2). Suppose moreover that for every $\alpha \in \operatorname{ob}B$, the
fiber category $E_\alpha$ admits a cardinal filtration (9.12) and every object of $E_\alpha$ is accessible (9.3). Then
each of the categories $F=\operatorname{Hom}_B(B,E)$ and $F'=\operatorname{Homcart}_B(B,E)$ admits a small full
subcategory generating by strict epimorphisms (7.1), and each of its objects is accessible.

It is immediate that the statement is not essentially changed when $B$ is replaced by a full subcategory $B_0$ such that
the inclusion functor $B_0 \to B$ is an equivalence, and $E$ is replaced by $E_0=E\times_B B_0$. This allows us to
suppose that $B$ is a small category.

For every $\alpha \in \operatorname{ob}B$, let $(\operatorname{Filt}^\pi(E_\alpha))_{\pi \in U}$ be a cardinal
filtration of $E_\alpha$. Let $c_0 \in U$ be a cardinal satisfying the following conditions:

```text
             c_0 >= Sup_{alpha in ob B} pi_alpha,     c_0 >= card Fl B ;
(9.22.1)     for every arrow f : alpha -> beta of B, f* : E_beta -> E_alpha is c_0-accessible ;
             for every alpha in ob B, the objects of Filt^{pi_alpha}(E_alpha) are c_0-accessible.
```

Put

$$ c=2^{c_0}, $$

so that $c>c_0$, and for every $\alpha \in \operatorname{ob}B$, let

$$ C_\alpha=\operatorname{Filt}^c(E_\alpha). $$

[PDF p. 192]

I claim that the preliminary conditions for 9.21.9 and 9.21.17 are verified, taking $\pi=\pi'_0=c$. This is clear for
(9.21.2) and (9.21.3). For (9.21.4 a)), it follows from 9.17, and (9.21.4 b)) follows from condition 9.12 c) for a
cardinal filtration. Note moreover that condition 9.12 b) of cardinal filtrations implies that for every
$\alpha \in \operatorname{ob}B$, one has $C^\pi_\alpha=C_\alpha=\operatorname{Filt}^c(E_\alpha)$, where $C^\pi_\alpha$
is defined in (9.21.6). Thus 9.22 follows from 9.21.9 and 9.21.17, and more precisely, we have proved the following
corollary.

**Corollary 9.23.** Under the conditions of 9.22, if $c_0 \in U$ is a cardinal satisfying conditions (9.22.1), and if
$c=2^{c_0}$, then the subcategory $F^c$ of $F$ (resp. $F'^c$ of $F'$) formed by the $X$ such that
$X(\alpha)\in \operatorname{ob}\operatorname{Filt}^c(E_\alpha)$ for every $\alpha \in \operatorname{ob}B$ is essentially
small and generating by strict epimorphisms; more precisely, every object $X$ of $F$ (resp. $F'$) is isomorphic to an
object of the form $\varinjlim_I X_i$, where the $X_i$ lie in $F^c$ (resp. in $F'^c$), and where $I$ is an ordered set
large relative to $c$.

Under slightly stronger hypotheses in 9.22, one can moreover make 9.22 and 9.23 considerably more precise:

**Corollary 9.24.** Under the conditions of 9.22, suppose that each of the categories $E_\alpha$
($\alpha \in \operatorname{ob}B$) is stable under small filtering inductive limits, and that for every
$\pi \geq \pi_\alpha$, $\operatorname{Filt}^\pi(E_\alpha)$ is stable under filtering inductive limits indexed by
filtering ordered sets $I$ such that $\operatorname{card}I\leq \pi$ (which slightly strengthens condition 9.12 b) of
cardinal filtrations). In the case where $F'$ is considered, suppose moreover that for every arrow
$f : \alpha \to \beta$ of $B$, the functor $f^* : E_\beta \to E_\alpha$ commutes with small filtering inductive limits.
Finally let $c_0 \in U$ be a cardinal satisfying conditions (9.22.1), and consider, for every cardinal
$\pi \geq c=2^{c_0}$, the strictly full subcategory $F^\pi$ (resp. $F'^\pi$) of $F$ (resp. of $F'$) formed by the $X$
such that $X(\alpha)\in \operatorname{Filt}^\pi(E_\alpha)$ for every $\alpha \in \operatorname{ob}B$. Then the
subcategories considered define a cardinal filtration (9.12) of $F$ (resp. of $F'$).

[PDF p. 193]

One must verify conditions a), b), c) of 9.12. Conditions a) and b) follow from the analogous conditions for the given
cardinal filtrations of the $E_\alpha$, and from 9.21.10 (resp. 9.21.18, taking the second of conditions (9.22.1) into
account). It remains to prove c), whose first part follows at once from 9.21.9 (resp. 9.21.17), taking $\pi'_0=0$,
$\pi_0=c$.

It remains to prove that if one has two cardinals $\pi' \geq \pi \geq c$, then for every $X$ in $F^{\pi'}$ (resp.
$F'^{\pi'}$) one has

$$ X \simeq \varinjlim_{i \in K} X_i, $$

with the $X_i$ in $F^\pi$ (resp. $F'^\pi$), $K$ large relative to $\pi$, and $\operatorname{card}K\leq \pi'^\pi$. For
this, take up again the proofs of 9.21.9 (ii) and 9.21.17 (ii). One may suppose that each $I_\alpha$ has cardinal
$\leq \pi'$ by condition 9.12 c) on the cardinal filtration of $E_\alpha$, hence one will have:

$$ \operatorname{card}I\leq (\pi'^\pi)^{\operatorname{card}\operatorname{ob}B}\leq(\pi'^\pi)^c=\pi'^{\pi c}=\pi'^\pi. $$

The index set $K$ used in 9.21.15 resp. 9.21.21 is the set of subsets $J$ of $I$ which are filtering (i.e. large
relative to $\pi'_0=0$), stable under $\varphi$, and such that $\operatorname{card}J\leq \pi$. It is then immediate that
one has

[PDF p. 194]

$$ \operatorname{card}K\leq(\operatorname{card}I)^\pi\leq(\pi'^\pi)^\pi=\pi'^{\pi^2}=\pi'^\pi, $$

which completes the proof of 9.24.

Finally, it is appropriate to give a statement freed from the somewhat technical hypotheses of 9.22, replacing them by
the conjunction, for the $E_\alpha$, of the hypotheses occurring in 9.11 (which ensure accessibility of the objects of
$E_\alpha$) and in 9.13 (which ensure the existence of a cardinal filtration in $E_\alpha$):

**Corollary 9.25.** Let $p : E \to B$ be a fibering functor, where $B$ is a category equivalent to a small category, and
where for every arrow $f : \alpha \to \beta$ of $B$, the functor $f^* : E_\beta \to E_\alpha$ is accessible (9.2).
Suppose moreover that, for every $\alpha \in \operatorname{ob}B$, the fiber category $E_\alpha$ satisfies the following
conditions:

a) $E_\alpha$ admits a small full subcategory generating by strict epimorphisms (7.1).

b) $E_\alpha$ is stable under fiber products, under kernels of double arrows, under sums of two objects and cokernels of
double arrows, and finally under small filtering inductive limits (*).

c) The functor $\operatorname{Ker}(u,v)$ on the category of double arrows of $E_\alpha$ is accessible (for example,
commutes with small filtering inductive limits).

d) Every strict epimorphism of $E_\alpha$ (10.2) is a strict universal epimorphism.

Under these conditions, each of the categories $F=\operatorname{Hom}_B(B,E)$ and $F'=\operatorname{Homcart}_B(B,E)$
admits a small subcategory generating by strict epimorphisms, and all its objects are accessible (9.3).

(*) This last condition is probably unnecessary, cf. 9.13.2.

[PDF p. 195]

Moreover, 9.24 gives us:

**Corollary 9.26.** Under the conditions of 9.25, and in the case where one considers
$F'=\operatorname{Homcart}_B(B,E)$, suppose that the functors $f^* : E_\beta \to E_\alpha$ commute with small filtering
inductive limits. Then $F$ (resp. $F'$) admits a cardinal filtration, which can be made explicit by the procedure of
9.24.

## 10. Glossary

For the reader's convenience, we collect here the definitions of several terms used in the preceding sections. We denote
by $C$ a category.

**10.1. Cartesian, cocartesian.** A diagram of $C$

```text
A ----> B
|      |
v      v
C ----> D
```

is called cartesian if it is commutative and if the canonical morphism from $A$ to the fiber product $C \times_D B$ is
an isomorphism. It is called cocartesian if the corresponding diagram in the category opposite to $C$ is cartesian.

[PDF p. 196]

**10.2. Epimorphism, strict epimorphism, etc.** Cf. 10.3.

**10.3. Epimorphic family, strict epimorphic family, etc.** A family

```text
f_i : A_i -> B,    i in I,
```

of arrows with the same target in $C$ is called an epimorphic family if, for every object $C$ of $C$, the map induced by
the $f_i$

```text
(10.3.1)    Hom_C(B, C) -> prod_i Hom_C(A_i, C)
```

is injective.

The family under consideration is called a strict epimorphic family if the image of the map (10.3.1) is formed by the
families $(g_i)$ such that, for every object $R$ of $C$, every pair of indices $i,j\in I$, and every pair of arrows
$u : R\to A_i$, $v : R\to A_j$, with $f_i u=f_j v$, one also has $g_i u=g_j v$.

When the fiber products $A_i\times_B A_j$ are representable for $i,j\in I$, this is equivalent to saying that the
essential image of (10.3.1) is formed by the $(g_i)$ such that, for every pair of indices $i,j\in I$, one has
$g_i\operatorname{pr}_1=g_j\operatorname{pr}_2$, where $\operatorname{pr}_1$, $\operatorname{pr}_2$ are the two
projections from $A_i\times_B A_j$.

The family $(f_i)_{i\in I}$ is called an effective epimorphic family if the preceding condition is satisfied, i.e. if it
is a strict epimorphic family, and if the fiber products $A_i\times_B A_j$ are representable.

The family $(f_i)_{i\in I}$ is called a universally epimorphic family (resp. a universally effective epimorphic family)
if the morphisms $f_i$ are quarrable (10.7), and if for every arrow $B'\to B$, the family of arrows
$f'_i : A'_i=A_i\times_B B'\to B'$, $i\in I$, deduced from the family $(f_i)_{i\in I}$ by the base change $B'\to B$, is
epimorphic (resp. effective epimorphic).

[PDF p. 197]

The notion of a strict universally epimorphic family will be defined in (II 2.5, 2.6). Note that when the morphisms
$f_i$ are quarrable (for example if fiber products are representable in $C$), this notion coincides with that of a
universally effective epimorphic family (use II 2.4). In the general case, among the six variants of the notion of
epimorphicity considered above, one has the logical implications:

```text
                 universally effective epimorphic
                    /                            \
                   v                              v
      effective epimorphic          strict universally epimorphic
                   |                    /                      \
                   v                   v                        v
             epimorphic        strict epimorphic       universally epimorphic
                                      \                       /
                                       v                     v
                                    epimorphic
```

A morphism $f : A\to B$ of $C$ is called an epimorphism (resp. a strict epimorphism, resp. an effective epimorphism,
resp. a universal epimorphism, resp. a universal effective epimorphism, resp. a strict universal epimorphism) if the
family of morphisms reduced to the single element $f$ is epimorphic (resp. ...).

**10.4. Monomorphic family, strict monomorphic family, etc.** A family of arrows $f_i : A_i\to B$ of $C$ is called
monomorphic (resp. strict monomorphic, ...) if, as a family of arrows in the opposite category $C^\circ$, it is
epimorphic (resp. strict epimorphic, ...). An arrow $f : A\to B$ of $C$ is called a monomorphism (resp. a strict
monomorphism, ...) if the family reduced to $f$ is monomorphic

[PDF p. 198]

(resp. strict monomorphic, ...), i.e. if $f$, as an arrow of the opposite category $C^\circ$, is an epimorphism (resp. a
strict epimorphism, ...).

**10.5. Monomorphism, strict monomorphism, etc.** Cf. 10.4.

**10.6. Projector, image of a projector, direct factor of an object.** Let $f : X\to X$ be an endomorphism of an object
of $C$. We say that $f$ is a projector if $f^2=f$. Then the pair $(f,\operatorname{id}_X)$ admits a representable
cokernel $X'$ if and only if it admits a representable kernel $X''$, and when this is so, there exists a unique
isomorphism $u : X'\to X''$ in $C$ such that $i u p=f$, where $p : X\to X'$ and $i : X''\to X$ are the canonical
morphisms. One then generally identifies $X'$ and $X''$, and calls it the image of the projector $f$; one says that the
projector $f$ admits an image if $\operatorname{Ker}(f,\operatorname{id}_X)$ is representable, i.e. if
$\operatorname{Coker}(f,\operatorname{id}_X)$ is representable.

A subobject (resp. a quotient) $Y$ of $X$ is called a direct factor of $X$ if one can find a projector $f$ in $X$ which
factors through $Y$, and which admits $Y$ as image as a subobject (resp. as a quotient) of $X$. Sometimes, by abuse of
language, one says that an object of $C$ is a direct factor of $X$ if it is isomorphic to the image of a projector in
$X$.

**10.7. Quarrable.** An arrow $f : A\to B$ of $C$ is called quarrable if, for every arrow $B'\to B$ of $C$, the fiber
product $A\times_B B'$ is representable in $C$.

[PDF p. 199]

**10.8. Quotient, strict quotient, etc.** Let $A$ be an object of $C$. Two epimorphisms $f : A\to B$, $f' : A\to B'$
with source $A$ are called equivalent if there exists an isomorphism $u : B\to B'$ such that $u f=f'$. In this way one
obtains an equivalence relation on the set of epimorphisms with source $A$, whose classes are called quotients, or
quotient objects, of $A$. For every quotient of $A$, one generally supposes that an element of this class has been
chosen, say $f : A\to B$, and one often speaks, by abuse of language, of the quotient $B$ of $A$ (or of the quotient
$f : A\to B$ of $A$). One says that $B$ is a strict quotient (resp. an effective quotient, resp. a universal quotient,
...) if the morphism $f : A\to B$ is a strict epimorphism (resp. an effective epimorphism, resp. a universal
epimorphism, ...) (10.3).

**10.9. Equivalence relations.** Let $F,G$ be two presheaves of sets on $C$. A diagram $p_1,p_2 : F\rightrightarrows G$
is called an equivalence relation on $G$ if, for every object $A$ of $C$, the map

```text
(p_1(A), p_2(A)) : F(A) -> G(A) x G(A)
```

induces a bijection from $F(A)$ onto the graph of an equivalence relation on the set $G(A)$.

A diagram $p_1,p_2 : B\rightrightarrows C$ in $C$ is called an equivalence relation on $C$ if the corresponding diagram
of presheaves is an equivalence relation. When finite products and fiber products are representable in $C$, a functor
$\xi : C\to C'$ commuting with finite products and fiber products transforms equivalence relations on $C$ into
equivalence relations on $\xi(C)$.

[PDF p. 200]

Let $\pi : C\to D$ be a morphism of $C$ such that the fiber product $C\times_D C$ is representable. Then the diagram
$\operatorname{pr}_1,\operatorname{pr}_2 : C\times_D C\rightrightarrows C$ is an equivalence relation on $C$.

**10.10. Effective, universally effective equivalence relation.** An equivalence relation
$p_1,p_2 : R\rightrightarrows A$ on an object $A$ of $C$ is called an effective equivalence relation if there exists a
morphism $\pi : A\to B$ such that the square

```text
R --p_2--> A
|         |
p_1       pi
v         v
A --pi--> B
```

is cartesian and cocartesian. The morphism $\pi$ is the cokernel of the pair $(p_1,p_2)$, and is therefore determined up
to unique isomorphism. The morphism $\pi$ is then an effective epimorphism; if it is a universal effective epimorphism
(10.3), the equivalence relation is called universally effective.

**10.11. Subobject, strict subobject, etc.** These are the notions dual to quotient, strict quotient, etc. (10.8).

## Bibliography

B. Mitchell, _Theory of Categories_, Academic Press (1965).

[PDF p. 201]

## II. Appendix: Universes

By N. Bourbaki. (*)

### 1. Definition and First Properties of Universes

**Definition 1.** A set $U$ is called a universe if it satisfies the following conditions:

- (U.I) if $x\in U$ and if $y\in x$, then $y\in U$;
- (U.II) if $x,y\in U$, then $\{x,y\}\in U$;
- (U.III) if $x\in U$, then $P(x)\in U$;
- (U.IV) if $(x_\alpha)_{\alpha\in I}$ is a family of elements of $U$, and if $I\in U$, then the union
  $\bigcup_{\alpha\in I}x_\alpha$ belongs to $U$;
- (U.?) if $x,y\in U$, then the pair $(x,y)\in U$.

N.B. Since it has, I believe, been decided for the next editions that the ordered pair is to be defined in Kuratowski's
way by $(x,y)=\{\{x,y\},\{x\}\}$, condition (U.?) is useless, because it follows from (U.III).

**Examples.**

1. The empty set is a universe, denoted $U_0$.
2. Consider the nonempty finite words formed with the four symbols `"{"`, `"}"`, `","`, and `"\emptyset"` (cf. Alg. I).
   Define, by induction on the length $n$ of such a word, the notion of a meaningful word:

(*) We reproduce here, with his permission, secret papers of N. Bourbaki. The references in this text refer to his
learned work.

[PDF p. 202]

a) For $n=1$, the only meaningful word is $\emptyset$.

b) For a word $A$ of length $n$ to be meaningful, it is necessary and sufficient that there exist $p$ distinct
meaningful words $A_1,\ldots,A_p$ ($p\geq 1$) of lengths $<n$ such that

```text
A = {A_1, A_2, ..., A_p}.
```

For example $\emptyset$, $\{\emptyset\}$, $\{\{\emptyset\},\{\{\emptyset\}\}\}$, $\{\emptyset,\{\emptyset\}\}$ are
meaningful words.

It is clear, by induction on length, that every meaningful word denotes a term of set theory. For example, if
$A=\{A_1,A_2,\ldots,A_p\}$, $A$ denotes the set whose elements are $A_1,A_2,\ldots,A_p$; these terms are of course
finite sets.

Let $U_1$ be the set of sets thus obtained. One verifies easily that $U_1$ satisfies conditions (U.I), (U.II), (U.III),
and (U.IV) of Definition 1, but not that idiotic (U.?), which is not serious if one is willing to decanulate the ordered
pair. Thus $U_1$ is a universe. Note that the elements of $U_1$ are finite, and that $U_1$ is countable.

In the statements that follow, $U$ denotes a universe.

**Proposition 1.** If $x\in U$ and if $y\subset x$, then $y\in U$.

Indeed, one has $P(x)\in U$ by (U.III), whence $y\in P(x)$ and $y\in U$ by (U.I).

**Corollary.** If $x\in U$, every quotient set $y$ of $x$ is an element of $U$.

Indeed, $y$ is a subset of $P(x)$. Hence $y\in U$ by (U.III) and Proposition 1.

[PDF p. 203]

**Proposition 2.** If $x\in U$, one has $\{x\}\in U$.

This follows from (U.II) applied with $y=x$.

**Proposition 3.** Every pair, every triple, and every quadruple of elements of $U$ is an element of $U$.

This is true for pairs by the N.B. or by (U.?). The case of triples follows, because $(x,y,z)=((x,y),z)$, and then the
case of quadruples follows, because $(x,y,z,t)=((x,y,z),t)$.

**Proposition 4.** If $X,Y\in U$, then $X\times Y\in U$.

Indeed, for $x\in X$, $\{x\}\times Y$ is the union of the family $(\{(x,y)\})_{y\in Y}$; since $\{(x,y)\}\in U$ by
(U.I), (U.II), and Proposition 3, one has $\{x\}\times Y\in U$ by (U.IV). Finally $X\times Y$ is the union of the family
$(\{x\}\times Y)_{x\in X}$; it is therefore an element of $U$ by (U.IV) again.

**Corollary 1.** If $X,Y,Z,\ldots$ are elements of $U$, all the sets of the scale constructed on $X,Y,Z,\ldots$ are
elements of $U$ (cf. chap. IV).

This follows from successive applications of Proposition 4 and (U.III).

**Corollary 2.** If $(x_\alpha)_{\alpha\in I}$ is a family of elements of $U$ and if $I\in U$, the sum set
$\Sigma_{\alpha\in I}x_\alpha$ is an element of $U$.

Indeed, this sum set is a subset of the product $(\bigcup_{\alpha\in I}x_\alpha)\times I$ (chap. II), a product whose
two factors are elements of $U$ (by (U.IV) and the hypothesis). One then applies Propositions 4 and 1.

[PDF p. 204]

**Proposition 5.** If $X$ and $Y$ are elements of $U$, every correspondence between $X$ and $Y$ (in particular every map
from $X$ to $Y$) is an element of $U$.

Indeed, such a correspondence $C$ is a triple $(X,Y,\Gamma)$, where $\Gamma$ is a subset of $X\times Y$, the graph of
$C$ (chap. II). One has $\Gamma\in U$ by Propositions 4 and 1. Hence $C\in U$ by Proposition 3.

**Proposition 6.** If $X,Y\in U$, every set $Z$ of correspondences between $X$ and $Y$ (in particular of maps from $X$
to $Y$) is an element of $U$.

Indeed, $Z$ is a subset of $\{X\}\times\{Y\}\times P(X\times Y)$. But this product is an element of $U$ by Proposition 2
and the corollary to Proposition 4. Thus $Z\in U$ by Proposition 1.

**Corollary.** If $(x_\alpha)_{\alpha\in I}$ is a family of elements of $U$, and if $I\in U$, one has
$\prod_{\alpha\in I}x_\alpha\in U$.

Indeed, this product is a set of maps from $I$ to $\bigcup_{\alpha\in I}x_\alpha$, and this union is an element of $U$
by (U.IV).

**Proposition 7.** If $X$ is a subset of $U$ whose cardinal is at most that of an element of $U$, then $X$ is an element
of $U$.

Let $I$ be an element of $U$ such that $\operatorname{card}(X)\leq\operatorname{card}(I)$. There is a surjection
$i\mapsto x_i$ from a subset $I'$ of $I$ onto $X$. Then $X$ is the union of the family $(\{x_i\})_{i\in I'}$; this union
is an element of $U$ by Proposition 1, Proposition 2, and (U.IV).

[PDF p. 205]

**Corollary.** If $U$ is nonempty, every finite subset of $U$ is an element of $U$, and $U$ has elements of arbitrary
finite cardinality. On the other hand, if $U=\emptyset$, $\emptyset$ is a finite subset of $\emptyset$, but not an
element of $\emptyset$.

Indeed, if $U$ is nonempty, Proposition 2 shows that a one-element set $x_0$ belongs to $U$. By induction on $n$, set
$x_{n+1}=P(x_n)$. One has $x_n\in U$ by (U.III), and $\operatorname{card}(x_{n+1})=2^{\operatorname{card}(x_n)}$, so
that $U$ has elements of arbitrarily large finite cardinality.

**Remark.** It follows from Proposition 2 and the corollary to Proposition 7 that every nonempty universe $U$ contains
the universe $U_1$ of Example 2; indeed one has $\emptyset\in U$ by Proposition 1. Thus $U_1$ is the intersection of all
nonempty universes. More generally:

**Proposition 8.** If $(U_\lambda)_{\lambda\in L}$ is a nonempty family of universes, then

```text
U = intersection_{lambda in L} U_lambda
```

is a universe.

This follows immediately from Definition 1.

### 2. Universes and Species of Structures

Let $E$ be a species of structure; suppose, to fix ideas and lighten the exposition, that each structure of species $E$
is defined on a base set. Let $(X,S)$ be a structure of species $E$, where $X$ is the base set and $S$ is the structure,
and let $U$ be a universe. If $X\in U$, then all the constituent objects of the structure $S$ on $X$ are elements of $U$
(by Corollary 1 of Proposition 4, No. 1, and by (U.I)), so that the structure $(X,S)$ is an element of $U$.

[PDF p. 206]

Suppose now that $E$ is a species of structure with morphisms. If $X$ and $X'$ are elements of $U$ equipped with
structures of species $E$, then the set of morphisms from $X$ to $X'$ is again an element of $U$ (No. 1, Proposition 6).

Now consider the category $(U - E)$ defined in § 1, No. 2, ex. c). Since the objects and arrows of $(U - E)$ are
elements of $U$, $(U - E)$ is a pair of subsets of $U$, equipped with a quadruple of maps; in general it is not an
element of $U$. The notation $X\in(U - E)$ will mean that $X$ is an element of $U$ equipped with a structure of species
$E$.

The category $(U - E)$ is stable under many operations:

a) If $X\in(U - E)$, and if $X'$ is a subset of $X$ which admits an induced structure, then $X'\in(U - E)$. This follows
from Proposition 1, No. 1.

b) If $X\in(U - E)$, and if $X''$ is a quotient set of $X$ which admits a quotient structure, then $X''\in(U - E)$
(corollary to Proposition 1, No. 1).

c) If $X,Y\in(U - E)$, and if $X\times Y$ admits a product structure, then $X\times Y\in(U - E)$ (Proposition 4, No. 1).
More generally, if $(X_i)_{i\in I}$ is a family of elements of $(U - E)$, if $I\in U$, and if $\prod_{i\in I}X_i$ admits
a product structure, then $\prod_{i\in I}X_i\in(U - E)$ (corollary to Proposition 6). Analogous assertions hold for sum
structures (Corollary 2 to Proposition 4).

d) Let $I$ be a preordered set, and let $(X_i,f_{ij})_{i,j\in I}$ be a projective (resp. inductive) system of sets
equipped with structures of species $E$ and with morphisms; let $L$ be the limit of this system, in the sense of chap.
III. If $X_i\in U$ for every $i$, if $I\in U$, and if $L$ admits a projective (resp. inductive) limit structure, then
one has $L\in(U - E)$: indeed $L$ is

[PDF p. 207]

a subset of $\prod_{i\in I}X_i$ (resp. a quotient set of $\Sigma_{i\in I}X_i$), and is therefore an element of $U$ by
No. 1.

Let us give a few more particular examples:

1. Let $X,Y\in(U - \mathrm{Top})$ be two locally compact spaces. Then the set $\mathcal{C}(X,Y)$ of continuous maps from
   $X$ to $Y$, equipped with the topology of compact convergence (Top. Gen. X), is an element of $(U - \mathrm{Top})$.
   Indeed, one has $\mathcal{C}(X,Y)\in U$ by Proposition 6 of No. 1.
2. Let $X,Y\in(U - \mathrm{Ab})$. Then the group $\operatorname{Hom}_{\mathbf{Z}}(X,Y)$ is an element of
   $(U - \mathrm{Ab})$ by Proposition 6 of No. 1. If one further supposes that $\mathbf{Z}\in U$, the tensor product
   $X\otimes_{\mathbf{Z}}Y$ is an element of $(U - \mathrm{Ab})$; indeed, this tensor product is a quotient of
   $\mathbf{Z}^{(X\times Y)}$, which is a subset of $\mathbf{Z}^{X\times Y}$, itself an element of $U$ by Propositions 4
   and 6 of No. 1.
3. Let $X\in(U - \mathrm{Unif})$ be a uniform space. Then its completion $\widehat{X}$ is an element of
   $(U - \mathrm{Unif})$. Indeed, $\widehat{X}$ is a set of equivalence classes of Cauchy filters on $X$; a filter on
   $X$ is an element of $P(P(X))$, hence an equivalence class of filters is an element of $P(P(P(X)))$, so that
   $\widehat{X}$ is an element of $P(P(P(P(X))))$, hence an element of $U$ by (U.III) and (U.I).

N.B. Moral: Bourbaki will have to take care to "canonify" his constructions. For example, in those where one adjoins an
element $\infty$ (Alexandroff compactification, projective field), it will be best to take

[PDF p. 208]

$\infty=\emptyset$ (because $\emptyset$ is an element of every nonempty universe) and to form the sum set of
$\{\emptyset\}$ and of the given set. Of course, one would also have to "canonify" the two-element set used to construct
sum sets; thus $\{\emptyset,\{\emptyset\}\}$ seems to me a good candidate, because it belongs to every nonempty
universe.

### 3. Universes and Categories

Let $U$ be a universe and $C$ a category. We write $C\in U$ if $\operatorname{Ob}(C)\in U$ and
$\operatorname{Fl}(C)\in U$. This notation is justified by the fact that $C$ is the sextuple formed by
$\operatorname{Ob}(C)$, by $\operatorname{Fl}(C)$, and by the four structural maps; hence if $\operatorname{Ob}(C)\in U$
and $\operatorname{Fl}(C)\in U$, these four maps are elements of $U$ (No. 1, Corollary 1 to Proposition 4), hence so is
the sextuple $C$ (No. 1, Proposition 3, cum grano salis). This is moreover a particular case of No. 2, if one considers
the species of structure "cat" of category. With the notation of No. 2, the relation $C\in U$ is also written
$C\in(U - \mathrm{cat})$.

Note that a category such as $(U - \mathrm{Ens})$, $(U - \mathrm{Ord})$, $(U - \mathrm{Top})$, or $(U - \mathrm{Gr})$ is
not, in general, an element of $U$.

Let $C,D$ be two categories and $U$ a universe such that $C,D\in U$. If $C'$ is a subcategory of $C$, one has $C'\in U$;
the product category $C\times D$, the sum category of $C$ and $D$, and the opposite categories $C^\circ$ and $D^\circ$
are also elements of $U$ (cf. No. 2). The category of functors $E=\operatorname{Hom}(C,D)$ is also an element of $U$:
indeed $\operatorname{Ob}(E)$ is a set of pairs of maps $\operatorname{Ob}(C)\to\operatorname{Ob}(D)$,
$\operatorname{Fl}(C)\to\operatorname{Fl}(D)$, hence $\operatorname{Ob}(E)\in U$ by

[PDF p. 209]

No. 1; as for $\operatorname{Fl}(E)$, it is a set of functorial morphisms, that is, of maps
$\operatorname{Ob}(C)\to\operatorname{Fl}(D)$, whence $\operatorname{Fl}(E)\in U$ by Proposition 6 of No. 1.

**Proposition 9.** Let $E$ be a species of structure with morphisms, and let $U,U'$ be two universes such that
$U'\subset U$. Then $(U' - E)$ is a full subcategory of $(U - E)$.

Indeed, if $x$ and $y$ are objects of $(U' - E)$, they are by definition objects of $(U - E)$. As for
$\operatorname{Hom}(x,y)$, it is the same set in the two categories (cf. § 1, No. 2, ex. c)).

N.B. Note that the hypothesis that $U$ and $U'$ are universes is useless, so that Proposition 9 would advantageously go
back to § 1, No. 4. But the Tribe asked that it be here.

**Remark.** It can happen that the axioms of the species of structure $E$ imply that the cardinals of the sets equipped
with structures of species $E$ are bounded by a fixed cardinal, say $c$ (for example the species of structure of finite
group, of finitely generated group, of finitely generated module over a fixed ring $A$, or of finitely generated algebra
over $A$). Suppose then that there exists an element $z$ of $U'$ such that $c\leq\operatorname{card}(z)$. Then, for
every set $x$ equipped with a structure of species $E$, there exists an element $x'$ of $U'$ equipotent to $x$, for
example a subset of $z$; equip $x'$ with the structure deduced from that of $x$ by transport of structure; one obtains
in this way an element of $(U' - E)$. It follows that the inclusion functor from $(U' - E)$ into $(U - E)$ is then
essentially surjective (§ 4, No. 2, Def. 2), and is therefore an equivalence of categories (§ 4, No. 3, Th. 1).

[PDF p. 210]

### 4. The Axiom of Universes

The very pleasant stability results of No. 2 are of interest only if they can be applied to something other than the two
small universes $U_0$ and $U_1$ described in No. 1. We shall therefore add the following axiom to the axioms of set
theory:

**(A.6)** For every set $x$, there exists a universe $U$ such that $x\in U$.

This axiom implies that, if $(x_\alpha)_{\alpha\in I}$ is a family of sets, there exists a universe $U$ such that
$x_\alpha\in U$ for every $\alpha\in I$: indeed, it suffices to apply (A.6) to $x=\bigcup_{\alpha\in I}x_\alpha$ and to
apply Prop. 1 of No. 1.

In particular, given a category $C$, there exists a universe $U$ such that $C\in U$ in the sense of No. 3: apply the
preceding assertion to the family $(\operatorname{Ob}(C),\operatorname{Fl}(C))$. This applies to categories of the form
$(V - E)$, where $E$ is a species of structure with morphisms and $V$ is a set, a universe for example; in general one
has $V\notin U$.

For example, if $V$ is a universe, one has $\operatorname{Ob}(V - \mathrm{Ens})=V$ and
$\operatorname{Fl}(V - \mathrm{Ens})\subset V$ (No. 1, Prop. 5). The universes $U$ such that $(V - \mathrm{Ens})\in U$
are therefore those such that $V\in U$. But the relation $V\in V$ is impossible for a universe: indeed, for every subset
$A$ of $V$, one would have $A\in V$ (No. 1, Prop. 1), whence $\operatorname{card}(P(V))\leq\operatorname{card}(V)$,
which is impossible.

[PDF p. 211]

### 5. Universes and Strongly Inaccessible Cardinals

Let $U$ be a universe. By condition (U.I) of Def. 1, every element $x$ of $U$ is a subset of $U$; hence
$\operatorname{card}(x)\leq\operatorname{card}(U)$. Since the cardinals of subsets of $U$ form a well-ordered set, the
cardinal

```text
(1)  c(U) = sup_{x in U} card(x)
```

exists. Note that, for every cardinal $c<c(U)$, there exists an element $x$ of $U$ such that $\operatorname{card}(x)=c$;
indeed, by definition there exists $y\in U$ such that $c\leq\operatorname{card}(y)\leq c(U)$, and one takes for $x$ a
suitable subset of $y$. Conversely, if $x\in U$, one has $\operatorname{card}(x)<c(U)$; indeed $P(x)\in U$ by (U.III),
whence $2^{\operatorname{card}(x)}\leq c(U)$. The cardinal $c(U)$ therefore has the following properties:

1. If $c$ is a cardinal $<c(U)$, one has $2^c<c(U)$; indeed, if $x$ is an element of $U$ of cardinal $c$, then
   $P(x)\in U$ by applying (U.III), whence $2^c<c(U)$.

2. If $(c_\lambda)_{\lambda\in I}$ is a family of cardinals such that $c_\lambda<c(U)$ for every $\lambda\in I$ and
   $\operatorname{card}(I)<c(U)$, then the sum cardinal $\Sigma_{\lambda\in I}c_\lambda$ is $<c(U)$. Indeed, let
   $x_\lambda\in U$ be such that $\operatorname{card}(x_\lambda)=c_\lambda$; replacing $I$, if necessary, by an
   equipotent index set, one may suppose that $I\in U$; then the sum set of the $x_\lambda$ is an element of $U$ (Cor. 2
   to Prop. 4 of No. 1), which proves our assertion.

We make the following definition:

[PDF p. 212]

**Definition 2.** A cardinal $d$ is called **strongly inaccessible** if:

**(FI.1)** If $c$ is a cardinal such that $c<d$, then $2^c<d$.

**(FI.2)** If $(c_\lambda)_{\lambda\in I}$ is a family of cardinals such that $c_\lambda<d$ for every $\lambda\in I$ and
if $\operatorname{card}(I)<d$, then $\Sigma_{\lambda\in I}c_\lambda<d$.

**Examples.** The cardinal $0$ and the countably infinite cardinal are strongly inaccessible. No nonzero finite cardinal
is strongly inaccessible.

Thus we have just proved that axiom (A.6) of universes implies the relation:

**(A'.6)** Every cardinal is strictly smaller than a strongly inaccessible cardinal.

Conversely:

**Theorem 1.** Relation (A'.6) implies axiom (A.6) of universes.

Indeed, let $A$ be a set. We must construct a universe $U$ of which $A$ is an element. Define by induction a sequence
$(A_n)_{n\geq 0}$ of sets by means of:

```text
(2)  A_0 = A,   A_{n+1} = union of the elements of A_n
                  = set of the elements of A_n.
```

Set $B=\bigcup_{n=0}^{\infty}A_n$. Let, by (A'.6), $c$ be a strongly inaccessible cardinal such that
$\operatorname{card}(B)<c$.

There exists a well-ordered set $I$ such that $\operatorname{card}(I)=c$. Replacing $I$, if necessary, by its smallest
segment of cardinal $c$, one may suppose that every segment of $I$ distinct from $I$ has cardinal $<c$.

[PDF p. 213]

We shall denote by $\varepsilon$ the smallest element of $I$. It follows from the hypothesis on segments that $I$ has no
largest element (otherwise one would remove it), and hence that every element of $I$ has a successor; for $\alpha\in I$,
we shall denote by $s(\alpha)$ the successor of $\alpha$.

This being so, define, by transfinite induction, a family $(B_\alpha)_{\alpha\in I}$ of sets by means of:

```text
     B_epsilon = B
(3)  B_{s(alpha)} = B_alpha union P(B_alpha)
     B_alpha = union_{beta < alpha} B_beta     if alpha has no predecessor.
```

Set $U=\bigcup_{\alpha\in I}B_\alpha$. We shall show that $U$ is the required universe. First one has $A\in U$, because
$A=A_0$ is a subset of $B=B_\varepsilon$, hence an element of $P(B_\varepsilon)\subset B_{s(\varepsilon)}$.

Next note that, for every $\alpha\in I$, one has:

```text
(4)  card(B_alpha) < c.
```

Indeed, we proceed by transfinite induction on $\alpha$. This is true for $\alpha=\varepsilon$ by hypothesis. From (4)
one deduces
$\operatorname{card}(B_{s(\alpha)})\leq\operatorname{card}(B_\alpha)+2^{\operatorname{card}(B_\alpha)}<c+c=c$ (by
(FI.1), since $c$ is infinite). Finally, if $\alpha$ has no predecessor, the set $I'$ of $\beta<\alpha$ has cardinal
$<c$ by construction; hence, if $\operatorname{card}(B_\beta)<c$ for every $\beta<\alpha$,

```text
card(B_alpha) = card(union_{beta in I'} B_beta) <= Sigma_{beta in I'} card(B_beta) < c
```

by (FI.2). This proves (4).

[PDF p. 214]

We now show that one has:

```text
(5)  card(x) < c for every x in U.
```

Indeed, it suffices to show that, for every $\alpha\in I$, one has "$\operatorname{card}(x)<c$ for every
$x\in B_\alpha$". We again proceed by transfinite induction on $\alpha$. This is true for $\alpha=\varepsilon$, because,
if $x\in B_\varepsilon=B$, there exists $n\geq 0$ such that $x\in A_n$, whence $x\subset A_{n+1}$ by (2), $x\subset B$,
and $\operatorname{card}(x)\leq\operatorname{card}(B)<c$. The case where $\alpha$ has no predecessor is obvious.
Finally, if $x\in B_{s(\alpha)}$, either $x\in B_\alpha$ and the assertion "$\operatorname{card}(x)<c$" is true by
induction, or $x\in P(B_\alpha)$, whence $x\subset B_\alpha$ and the assertion "$\operatorname{card}(x)<c$" is true by
(4).

We are now in a position to prove that $U$ is indeed a universe:

**(U.I)** Let $x\in U$ and $y\in x$. We must show that $y\in U$. In other words, we must show that, for every
$\alpha\in I$, one has the relation:

```text
x in B_alpha and y in x  =>  y in B_alpha.
```

We again proceed by transfinite induction on $\alpha$. This is true for $\alpha=\varepsilon$, because
$x\in B_\varepsilon=B$ implies $x\in A_n$ for some $n$; hence, if $y\in x$, then $y\in A_{n+1}$, whence
$y\in B=B_\varepsilon$. The passage to an element $\alpha$ without predecessor is obvious. Finally pass from $\alpha$ to
$s(\alpha)$: if $x\in B_{s(\alpha)}$ and if $y\in x$, then either $x\in B_\alpha$, whence
$y\in B_\alpha\subset B_{s(\alpha)}$ by induction, or $x\in P(B_\alpha)$, whence again
$y\in B_\alpha\subset B_{s(\alpha)}$.

**(U.II)** Let $x,y\in U$. Since the family $(B_\alpha)_{\alpha\in I}$ is increasing by (3), there exists $\alpha\in I$
such that $x,y\in B_\alpha$. Then $\{x,y\}\in P(B_\alpha)\subset B_{s(\alpha)}\subset U$.

[PDF p. 215]

**(U.III)** Let $x\in U$. Then there exists $\alpha\in I$ such that $x\in B_\alpha$. It therefore suffices to show that,
for every $\alpha\in I$, one has the relation:

```text
x in B_alpha  =>  P(x) in B_{s(s(alpha))}.
```

We again proceed by transfinite induction on $\alpha$. If $\alpha=\varepsilon$, one has $x\in A_n$ for some $n$, whence
$y\subset A_{n+1}\subset B=B_\varepsilon$ for every subset $y$ of $x$; thus one has
$y\in P(B_\varepsilon)\subset B_{s(\varepsilon)}$ for every $y\in P(x)$, whence $P(x)\subset B_{s(\varepsilon)}$ and
$P(x)\in P(B_{s(\varepsilon)})\subset B_{s(s(\varepsilon))}$, so that our assertion is true for $\alpha=\varepsilon$.
The passage to an element $\alpha$ without predecessor is immediate, because $\beta<\alpha$ then implies
$s(s(\beta))<\alpha$. Finally pass from $\alpha$ to $s(\alpha)$; let $x\in B_{s(\alpha)}$. If $x\in B_\alpha$, one has
$P(x)\in B_{s(s(\alpha))}\subset B_{s(s(s(\alpha)))}$ by induction; if $x\in P(B_\alpha)$, one has $x\subset B_\alpha$,
whence $P(x)\subset P(B_\alpha)$ and $P(x)\in P(P(B_\alpha))\subset B_{s(s(s(\alpha)))}$.

**(U.IV)** Let $(x_\lambda)_{\lambda\in K}$ be a family of elements of $U$ such that $K\in U$. We must show that the
union $x=\bigcup_{\lambda\in K}x_\lambda$ is an element of $U$. For every $\lambda\in K$, choose $\alpha(\lambda)\in I$
such that $x_\lambda\in B_{\alpha(\lambda)}$. We show that the set $\alpha(K)$ of the $\alpha(\lambda)$ is bounded above
in $I$: indeed, if it were not, one would have:

```text
I = union_{lambda in K} [epsilon, alpha(lambda)],
```

which would contradict (FI.2), because $\operatorname{card}(K)<c$ and
$\operatorname{card}([\varepsilon,\alpha(\lambda)])<c$ for every $\lambda\in K$. Let therefore $\beta$ be an upper bound
for $\alpha(K)$; one has $x_\lambda\in B_\beta$ for every $\lambda\in K$, because the family $(B_\alpha)_{\alpha\in I}$
is increasing. Thus $x_\lambda\subset B_\beta$ by what we saw in the proof of (U.I), whence
$x=\bigcup_{\lambda\in K}x_\lambda\subset B_\beta$. By (3) it follows that $x\in B_{s(\beta)}$, whence $x\in U$. Q.E.D.

[PDF p. 216]

**Definition 3.** Let $x$, $y$ be two sets and let $n$ be an integer $\geq 0$. We say that $y$ is a **component of order
$n$** of $x$ if there exists a sequence $(x_j)_{j=0,\ldots,n}$ such that $x_0=x$, $x_n=y$, and $x_{j+1}\in x_j$ for
$j=0,\ldots,n-1$.

Thus $x$ is the only component of order $0$ of $x$. The components of order $1$ (resp. $2$) of $x$ are the elements of
$x$ (resp. the elements of the elements of $x$). We say that $y$ is a **component** of $x$ if there exists $n\geq 0$
such that $y$ is a component of order $n$ of $x$. The relation "$y$ is a component of $x$" is a preorder relation. By
the selection-union scheme (chap. II, ...), the relation "$y$ is a component of $x$" is collectivizing with respect to
$y$, so that the components of $x$ form a set.

**Definition 4.** Let $c$ be a cardinal. A set $x$ is said to be **of type $c$** (resp. **of strict type $c$**, **of
finite type**) if all the components of $x$ have cardinals $\leq c$ (resp. $<c$, finite).

**Examples.** The elements of the universe $U_1$ (No. 1, ex. 2) are all of finite type. If $c$ is a cardinal, and if $x$
is of type $c$ (resp. of strict type $c$, of finite type), then every component of $x$ and every subset of $x$ is of
type $c$ (resp. of strict type $c$, of finite type); likewise $P(x)$ is of type $2^c$ (resp. of strict type $2^c$, of
finite type). If $x$ is of type $c$ and if $c\leq c'$, then $x$ is of type $c'$.

[PDF p. 217]

**Lemma.** Let $c$ be a noncountable strongly inaccessible cardinal, and let $X$ be a set of strict type $c$. Then there
exists a cardinal $d<c$ such that $X$ is of type $d$.

Indeed, for every integer $n$, denote by $d_n$ the cardinal of the set $X_n$ of components of order $n$ of $X$. One has
$d_0=1$, $d_1=\operatorname{card}(X)<c$, and, since $X_n=\bigcup_{Y\in X_{n-1}}Y$, it follows, by induction on $n$ and
use of (FI.2), that $d_n<c$ for every $n$. Then the $d_n$ are bounded above by the cardinal $d=\Sigma_{j\geq 0}d_j$,
which is $<c$ by (FI.2) and the hypothesis that $c$ is noncountable. Thus, if $Y$ is a component of order $n$ of $X$,
one has $\operatorname{card}(Y)\leq\operatorname{card}(X_{n+1})\leq d$. Q.E.D.

**Proposition 10.** Let $U$ be a universe and $c$ a strongly inaccessible cardinal. Then the set $U'$ of the $x\in U$
which are of strict type $c$ is a universe.

Indeed, if $x,y\in U'$ and if $z\in x$, then obviously $z\in U'$ and $\{x,y\}\in U'$. If $x\in U'$, one has
$\operatorname{card}(x)<c$, whence $\operatorname{card}(P(x))<c$ by (FI.1); since a component of $P(x)$ is either
$P(x)$, or a subset of $x$, or a component of $x$, one has $P(x)\in U'$. Finally, if $(x_\alpha)_{\alpha\in I}$ is a
family of elements of $U'$ such that $I\in U'$, then $\operatorname{card}(\bigcup_\alpha x_\alpha)<c$ by (FI.2); since
every component of order $>0$ of $\bigcup_\alpha x_\alpha$ is a component of some $x_\alpha$, one indeed has
$\bigcup_\alpha x_\alpha\in U'$. Q.E.D.

**Remark on the cardinal $c(U)$.** Let $U$ be a universe and let $c(U)$ be the cardinal defined by (1), i.e.

```text
c(U) = sup_{x in U} card(x).
```

[PDF p. 218]

One obviously has $c(U)\leq\operatorname{card}(U)$, because, recall, $x\in U$ implies $x\subset U$. But the equality
$c(U)=\operatorname{card}(U)$ is not always true. For example, let $(x_\alpha)_{\alpha\in I}$ be a noncountable family
of symbols with the axioms:

```text
"x_alpha = {x_alpha} for every alpha in I",   "x_alpha != x_beta if alpha != beta"
```

(in other words $x_\alpha$ is a one-element set, namely itself). Form, as in ex. 2 of No. 1, the "meaningful words"
formed with the symbols $\emptyset$, $x_\alpha$, `{`, `}`, and `,`. Each denotes a finite set.

Let $U$ be the set of these. One verifies easily that the conditions of Def. 1 are satisfied, so that $U$ is a universe.
Since the meaningful words are finite sequences of elements of a set of cardinal $\operatorname{card}(I)+4
=\operatorname{card}(I)$, one has $\operatorname{card}(U)=\operatorname{card}(I)$ (chap. III; in fact
$\operatorname{card}(U)\geq\operatorname{card}(I)$ suffices, and this is obvious). On the other hand, $c(U)$ is the
countable cardinal, whence $c(U)<\operatorname{card}(U)$.

The strict inequality $c(U)<\operatorname{card}(U)$ is due to the fact that we introduced here sets $x_\alpha$ such that
$x_\alpha\in x_\alpha$. If one forbids horrors of this kind, one obtains $\operatorname{card}(U)=c(U)$ for every
universe $U$, as well as other very pretty results "which can serve no purpose". This is what we shall do in the next
number.

### 6. Artinian Sets and Universes

**Definition 5.** A set $x$ is called **artinian** if there is no infinite sequence $(x_n)_{n\geq 0}$ such that $x_0=x$
and $x_{n+1}\in x_n$ for every $n\geq 0$.

**Examples.** The sets $\emptyset$, $\{\emptyset\}$, $\{\emptyset,\{\emptyset\}\}$, and more generally the elements of
the universe $U_1$ of No. 1, are artinian.

[PDF p. 219]

In pictorial terms, if $x$ is artinian, and if one takes an element $x_1$ of $x$, then an element $x_2$ of $x_1$, etc.,
the process must stop, and one arrives at a component $x_n$ of $x$ which is empty. In other words, artinian sets are
"built from $\emptyset$"; this will be made precise later (cf. `(*)` in the proof of Th. 2).

Artinian sets plainly have the following properties:

**(AR.I)** If $x$ is artinian, every subset of $x$ and every component of $x$ is artinian. For $x$ to be artinian, it is
necessary and sufficient that every element of $x$ be artinian.

**(AR.II)** If $x$ and $y$ are artinian, then $\{x,y\}$ is artinian.

**(AR.III)** If $x$ is artinian, $P(x)$ is artinian.

**(AR.IV)** Every union of artinian sets is an artinian set.

These properties immediately show:

**Proposition 11.** If $U$ is a universe, the set of artinian elements of $U$ is a universe, necessarily artinian.

**Corollary.** If $x$ is an artinian set, there exists an artinian universe $U$ such that $x\in U$.

Indeed, by axiom (A.6), $x$ is an element of a universe $V$; take for $U$ the set of artinian elements of $V$.

The following proposition is even less useful than the rest of the number:

[PDF p. 220]

**Proposition 12.** Let $A$ be an artinian set. Then:

a) For every $x\in A$, one has $x\notin x$.

b) If $x,y\in A$, one cannot have both $x\in y$ and $y\in x$.

c) For every $x\in A$, the relation "$y$ is a component of $z$" between components $y,z$ of $x$ is an order relation.

d) For every nonempty element $x$ of $A$, there exists $y\in x$ such that $x\cap y=\emptyset$.

Indeed, the negation of a) (resp. of b)) entails the existence of an infinite sequence $(x_n)_{n\geq 0}$ contradicting
Def. 5, namely $(x,x,x,\ldots)$ (resp. $(x,y,x,y,x,y,\ldots)$). The negation of c) means that there exist $x\in A$,
distinct components $y,z$ of $x$, and membership sequences

```text
y in y_1 in ... in y_q in z,    z in z_1 in ... in z_r in y ;
```

whence, as in b), an infinite sequence $(x_n)_{n\geq 0}$ contradicting Def. 5.

Finally, if d) is false, there exists a nonempty element $x$ of $A$ such that $x\cap y\neq\emptyset$ for every $y\in x$;
set $x_0=x$, and take for $x_1$ an element of $x$; since $x\cap x_1\neq\emptyset$, take for $x_2$ an element of
$x\cap x_1$, etc.; more formally, define by induction an infinite sequence $(x_n)_{n\geq 1}$ of elements of $x$ by means
of $x_1\in x$, $x_{n+1}\in x_n\cap x$ for $n\geq 1$; then the sequence $(x_n)_{n\geq 0}$ contradicts Def. 5.

**Remark.** Let $B$ be a set. For $B$ to be artinian, it is necessary and sufficient that every set $A$ of sets of
components of $B$ satisfy condition d) of Prop. 12. Indeed, necessity follows from (AR.I)

[PDF p. 221]

and Prop. 12. Conversely, if $B$ is not artinian, there exists an infinite sequence $(x_n)_{n\geq 0}$ with $x_0=B$ and
$x_{n+1}\in x_n$ for every $n\geq 0$; take for $A$ the subset reduced to the set $X$ of the $x_n$; then $A$ contains a
nonempty element $X$ such that, for every element $y$ of $X$, one has $y\cap X\neq\emptyset$ (indeed $y$ is of the form
$x_n$, and one has $x_{n+1}\in y\cap X$).

**Theorem 2.** Let $c$ be an infinite cardinal. Then:

a) The relation "$x$ is an artinian set of type $c$ (resp. of strict type $c$)" is collectivizing with respect to $x$;
the set $A_c$ of artinian sets of type $c$ has cardinal $2^c$.

b) If $c$ is strongly inaccessible, the set $U_c$ of artinian sets of strict type $c$ is a universe of cardinal $c$; the
cardinal $c(U_c)=\sup_{x\in U_c}\operatorname{card}(x)$ is $c$.

c) If a universe $U$ admits an element of cardinal $c$, every artinian set of type $c$ belongs to $U$ (in other words
$A_c\subset U$).

c') If a universe $U$ is nonempty, every artinian set of finite type is an element of $U$.

Before proving Th. 2, let us deduce from it some illuminating corollaries:

**Corollary 1.** If a universe $U$ is artinian, then $\operatorname{card}(U)$ is strongly inaccessible, and $U$ is the
set of artinian sets of strict type $\operatorname{card}(U)$.

[PDF p. 222]

Indeed set $c(U)=\sup_{x\in U}\operatorname{card}(x)$. This is a strongly inaccessible cardinal (beginning of No. 5).
First suppose it is noncountable; then, for every infinite cardinal $c<c(U)$, every artinian set of type $c$ is an
element of

`U` by c); hence every artinian set of strict type $c(U)$ is an element of $U$ by the lemma of No. 5. This last
assertion remains valid if $c(U)$ is countable by c'). Conversely, by (U.I), every set in $U$ is of strict type $c(U)$.
Thus $U$ is the universe $U_{c(U)}$ of b), whence $c(U)=\operatorname{card}(U)$ by b).

It follows from Cor. 1 that an artinian universe is determined uniquely by its cardinal (which is moreover strongly
inaccessible). Thus there is a "one-to-one correspondence" between artinian universes and strongly inaccessible
cardinals. In particular:

**Corollary 2.** The inclusion relation $U\subset U'$ between artinian universes is a well-ordering relation.

Indeed, the relation $c\leq c'$ between cardinals is a well-ordering relation (chap. III), and, with the notation of b)
of Th. 2, the relations $c\leq c'$ and $U_c\subset U_{c'}$ are equivalent.

Note that Th. 2, b) gives a second proof of Th. 1 (No. 5).

[PDF p. 222]

We now pass to the proof of Th. 2. Given a set $A$, we shall call a **chain** of $A$ any finite sequence
$(x_j)_{j=0,\ldots,n}$ such that $x_0=A$ and $x_{j+1}\in x_j$ for $j=0,\ldots,n-1$. The chains of $A$ form

[PDF p. 223]

a set, by the selection-union scheme; denote it by $G(A)$. Given a chain $X=(x_j)_{j=0,\ldots,n}$, the chains of the
form $(x_j)_{j=0,\ldots,q}$ with $q\leq n$ will be called smaller than $X$; in this way one obtains, on $G(A)$, the
structure of an ordered set. For $A$ to be artinian, it is necessary and sufficient that $G(A)$ be a "Noetherian"
ordered set (i.e. satisfy the equivalent conditions of chap. III, § 6, No. 5).

We shall show that:

`(*)` If $A$ is artinian, it is determined uniquely by the isomorphism class of the ordered set $G(A)$.

Indeed, given an ordered set $G$ and an element $g\in G$, we shall denote by $S(g)$ the set of $g'\in G$ such that
$g<g'$ and $g\leq h\leq g'$ implies $h=g$ or $h=g'$ (in other words, the set of "immediate successors" of $g$). Consider
the map $\theta$ which, to every chain $X=(x_0,\ldots,x_n)$ of $G(A)$, associates the set $x_n$; then, for every
$X\in G(A)$, one has:

```text
theta(X) = { theta(X') | X' in S(X) }.
```

Since $A$ is the image under $\theta$ of the smallest element $X_0=(A)$ of $G(A)$, it will suffice to show that $\theta$
is uniquely determined by the isomorphism class of the ordered set $G(A)$. This follows from the following lemma:

[PDF p. 224]

**Lemma 1.** Let $G$ be a Noetherian ordered set and let $\varphi$ be a map from $G$ such that, for every $g\in G$, one
has:

```text
(1)  phi(g) = { phi(g') | g' in S(g) }.
```

Then $\varphi$ is uniquely determined. Moreover, if $U$ is a universe containing an element equipotent to $G$, then
$\varphi$ takes its values in $U$.

The hypothesis implies that $\varphi(g)=\emptyset$ if $g$ is a maximal element of $G$.

Indeed, let $\varphi$ and $\varphi'$ be two maps such that (1) is true; if $\varphi\neq\varphi'$, the set of $g\in G$
such that $\varphi(g)\neq\varphi'(g)$ is nonempty, and hence admits a maximal element $h$ because $G$ is Noetherian; one
then has $\varphi(g)=\varphi'(g)$ for every $g>h$, in particular for every "successor" $g'\in S(h)$; whence
$\varphi(h)=\varphi'(h)$ by (1), which is a contradiction; therefore indeed $\varphi=\varphi'$.

Now let $U$ be a universe containing an element $x$ equipotent to $G$; we show that $\varphi$ takes its values in $U$;
otherwise let $h$ be a maximal element among the $g\in G$ such that $\varphi(g)\notin U$; one has $\varphi(g')\in U$ for
every $g'\in S(h)$, so that

```text
phi(h) = { phi(g') | g' in S(h) }
```

is a subset of $U$; but, since its cardinal is smaller than $\operatorname{card}(G)$, hence than the cardinal of an
element of $U$, one has $\varphi(h)\in U$ (No. 1, Prop. 7); this contradiction shows that $\varphi$ takes its values in
$U$.

[PDF p. 225]

This being so, let us prove part a) of Th. 2. It is enough to consider the non-"resp." assertion, because the other one
follows immediately. Let $c$ be an infinite cardinal. If $A$ is a set of type $c$, one has:

```text
(2)  card(G(A)) <= c.
```

Indeed, if $A_n$ denotes the set of components of order $n$ of $A$, one has $\operatorname{card}(A_1)\leq c$ and
$\operatorname{card}(A_{n+1})\leq c\cdot\operatorname{card}(A_n)$, whence $\operatorname{card}(A_n)\leq c^n$ by
induction; but $c^n=c$ because $c$ is infinite (chap. III); hence
$\operatorname{card}(\bigcup_{n=0}^{\infty}A_n)\leq\operatorname{card}(\mathbf{N})\cdot c=c$ (chap. III); and $G(A)$ is
a set of finite sequences of elements of $\bigcup_n A_n$, so one indeed has inequality (2) (chap. III).

This being so, if $E$ is a set of cardinal $c$, giving an order structure on a subset $E'$ of $E$ is equivalent to
giving the subset of $E\times E$ formed by the $(x,y)$ such that $x\in E'$, $y\in E'$, and $x\leq y$. Thus, by virtue of
(2), the isomorphism classes of the ordered sets $G(A)$ (where $A$ is of type $c$) form a set $\mathfrak{G}_c$, and one
has $\operatorname{card}(\mathfrak{G}_c)\leq\operatorname{card}(P(E\times E))=2^c$. Let $\mathfrak{G}'_c$ be the subset
of $\mathfrak{G}_c$ formed by the classes of Noetherian ordered sets having a smallest element; if, to every
$G\in\mathfrak{G}'_c$, one associates the value at the smallest element of $G$ of the function $\varphi$ of Lemma 1, one
obtains a map $\theta$ from $\mathfrak{G}'_c$ whose image contains all artinian sets of type $c$. These therefore indeed
form a set $A_c$, and one has

```text
card(A_c) <= card(mathfrak{G}'_c) <= card(mathfrak{G}_c) <= 2^c.
```

[PDF p. 226]

It remains to see that $\operatorname{card}(A_c)=2^c$. For this it suffices to see that there exists an artinian set $B$
of type $c$ and of cardinal $c$, because the subsets of $B$ will then be elements of $A_c$. This existence follows from
the following lemma:

**Lemma 2.** For every cardinal $c$, there exists an artinian set $B$ of type $c$ and of cardinal $c$.

We proceed by transfinite induction on $c$. For $c=0$ there is no choice, and we take $B=\emptyset$. If $c$ has a
predecessor $c'$, let $B'$ be an artinian set of type $c'$ and of cardinal $c'$; then one has $c\leq 2^{c'}$, so that
there exists a subset $B$ of $P(B')$ of cardinal $c$; the elements of $B$ are subsets of $B'$ and therefore have
cardinals $\leq c'\leq c$; the components of higher order of $B$ are components of $B'$, and therefore also have
cardinals $\leq c'\leq c$.

Finally, if $c$ has no predecessor, choose, for every cardinal $c_\lambda<c$, an artinian set $B_\lambda$ of type
$c_\lambda$ and of cardinal $c_\lambda$; then $B=\bigcup_\lambda B_\lambda$ answers the question. This proves Lemma 2,
and completes the proof of part a).

We turn to b). Let $c$ be a strongly inaccessible cardinal. We already know, by a), that the artinian sets of strict
type $c$ form a set $U_c$. The fact that $U_c$ is a universe follows immediately from properties (AR.I) to (AR.IV) of
artinian sets (beginning of this number),

[PDF p. 227]

and from cardinal estimates analogous to those of Prop. 10 of No. 5. The relation
$\sup_{x\in U_c}\operatorname{card}(x)=c$ follows from Lemma 2, applied to the cardinals $<c$.

Finally, to show that $\operatorname{card}(U_c)=c$, first suppose that $c$ is noncountable; by the lemma of No. 5, $U_c$
is the union $\bigcup_{d<c}A_d$, where $A_d$ denotes the set of artinian sets of type $d$; but one has
$\operatorname{card}(A_d)=2^d<c$ (by a)); on the other hand the set of cardinals $d<c$ has cardinal $<c$ (chap. III);
hence $\operatorname{card}(U_c)\leq c\cdot c=c$, and also $\operatorname{card}(U_c)\geq c$ because
$\operatorname{card}(U_c)\geq\operatorname{card}(A_d)=2^d$ for every $d<c$.

The case $c=0$ being trivial, there remains the case where $c$ is the countably infinite cardinal. In this case $U_c$ is
the set of artinian sets of finite type (i.e. finite, as are all their components), and we use a pretty result of
combinatorial nature.

[PDF p. 227]

**Lemma 3** (D. Konig?). Consider two infinite sequences $(E_n)_{n\geq 1}$, $(f_n)_{n\geq 1}$ of finite sets $E_n$ and
maps $f_n : E_{n+1}\to E_n$. If there exists no infinite sequence $(x_n)_{n\geq 1}$ such that $x_n\in E_n$ and
$f_n(x_{n+1})=x_n$ for every $n$, then $E_n$ is empty for all sufficiently large $n$.

In other words, if all sequences $(x_n)$ such that $f_n(x_{n+1})=x_n$ are finite, their lengths are bounded. This can be
expressed in terms of projective limits: a projective limit of nonempty finite sets is nonempty (cf. Top. Gen., Chap. I,
2nd ed., § 9, No. 6, Prop. 8, 2°).

[PDF p. 228]

Indeed, argue by contradiction. If there exist nonempty $E_n$ for arbitrarily large $n$, then no $E_n$ is empty (because
$E_n=\emptyset$ entails $E_{n+1}=\emptyset$ by the existence of $f_n : E_{n+1}\to E_n$). Call "coherent" the finite
sequences $(x_j)_{1\leq j\leq n}$ such that $f_j(x_{j+1})=x_j$ for $j=1,\ldots,n-1$. We prove, by induction on $n$, the
existence of a coherent sequence $(a_1,\ldots,a_n)$ ($a_i\in E_i$) which, for every $q\geq n$, can be extended to a
coherent sequence $(a_1,\ldots,a_n,x_{n+1},\ldots,x_q)$ of length $q$. This is obvious for $n=0$, because no $E_n$ is
empty.

Pass from $n$ to $n+1$. If, for every $x\in f_n^{-1}(\{a_n\})\subset E_{n+1}$, all coherent sequences extending
$(a_1,\ldots,a_n,x)$ had lengths bounded by an integer $q(x)$, then all coherent sequences extending $(a_1,\ldots,a_n)$
would have bounded lengths (by $\sup_x q(x)$) because $E_{n+1}$ is finite; there therefore exists
$a_{n+1}\in f_n^{-1}(\{a_n\})$ such that the coherent sequence $(a_1,\ldots,a_n,a_{n+1})$ admits extensions of arbitrary
length. This being so, one obtains an infinite sequence $(a_n)_{n\geq 1}$ which contradicts the hypothesis.

It follows from Lemma 3 that if $A$ is an artinian set of finite type, then the ordered set $G(A)$ of its chains is
finite: indeed, take for $E_n$ the set of chains $(x_n\in x_{n-1}\in\cdots\in x_1\in A)$ with $n+1$ terms (which is
finite because the components of $A$ of order $\leq n+1$ are finite in number and are all finite), and take for $f_n$
the map

```text
(x_{n+1} in x_n in x_{n-1} in ...)  |->  (x_n in x_{n-1} in ...).
```

[PDF p. 229]

But the set of isomorphism classes of finite ordered sets is countable: indeed, giving an order structure on a finite
subset of $\mathbf{N}$ is equivalent to giving its graph, which is a finite subset of $\mathbf{N}\times\mathbf{N}$; on
the other hand the set of finite subsets of a countable set is countable (chap. III). It follows from `(*)` and Lemma 1
that the set $G$ of artinian sets of finite type is countable. It is infinite by Lemma 2 (or, more simply, by use of the
sequence $(z_n)_{n\geq 0}$ defined by $z_0=\emptyset$, $z_{n+1}=\{z_n\}$). This completes the proof of b).

**Remark.** We have just proved that, if $A$ is an artinian set of finite type, it has only finitely many components.
There therefore exists an integer $n$ such that $A$ is of type $n$.

We turn to the proof of c). Let $c$ be an infinite cardinal, let $U$ be a universe admitting an element of cardinal $c$,
and let $A$ be an artinian set of type $c$. Then the ordered set $G(A)$ has cardinal $\leq c$ (formula (2) above). The
second assertion of Lemma 1, applied to $G(A)$, shows that the map $(x_0,\ldots,x_n)\mapsto x_n$ from $G(A)$ takes its
values in $U$. In other words, all components of $A$ are elements of $U$. This proves c).

The proof of c') is analogous: if $A$ is an artinian set of finite type, we have just seen that $G(A)$ is finite; since
$U$ is nonempty, it contains an element equipotent to $G(A)$ by the corollary to Prop. 7 (No. 1). Q.E.D.

[PDF p. 230]

### 7. Vague Metamathematical Remarks

a) The axiom "every set is artinian" is harmless. Indeed, if one has a model $M$ of set theory, the set $M'$ of artinian
elements of $M$ is also a model (cf. Prop. 11).

b) Axiom (A.6) of universes (and the equivalent axiom (A'.6) of strongly inaccessible cardinals) is independent of the
rest of set theory. Indeed let $c$ be the first noncountable strongly inaccessible cardinal. The universe $U_c$ of
artinian sets of strict type $c$ (Th. 2, b)) is a model of set theory without (A.6): one calls "sets" the elements of
$U_c$, the "membership relation" is the restriction to $U_c$ of the ordinary one, etc. The "universes" of the model are
therefore the ordinary universes which are elements of $U_c$. But we have seen that the only universes which are
elements of $U_c$ are the two small ones $U_0=\emptyset$ and $U_1$. Thus $U_1$ is a "set" which is an element of no
"universe". We have therefore a model of set theory in which (A.6) is false.

c) Bourbaki was too cautious in being content to "presume" that the axiom of infinity (A.5) is independent of the
preceding axioms and schemes. It is in fact independent, because the countable universe $U_1$ of artinian sets of finite
type is a model in which (A.5) is false, and in which the preceding axioms and schemes are true.

d) It would be very interesting to prove that axiom (A.6) of universes is harmless. That seems difficult and is even
unprovable, says Paul Cohen.

[PDF p. 231]

The adjective "vague" in the title means that, in constructing models, we have not taken the trouble to canulate the
symbol $\tau$ so that it does not leave them. The key to this, if one considers a model $M$, is to replace the ordinary
$\tau_x(R(x))$ by:

```text
tau_x(R(x) and x in M).
```

One still has to verify that this really transforms the ordinary quantifiers into the quantifiers formerly called
"typical":

```text
(for all x in M) and (there exists x in M).
```

### Exercises

1) Let $n$ be an integer $\geq 1$. Show that the set of artinian sets of type $n$ is infinite (the sets
$z_0=\emptyset$, $z_1=\{\emptyset\}$, $z_{q+1}=\{z_q\}$ are of type $1$).

2) Call the **height** of a set $A$ the least upper bound (finite or infinite) of the integers $n$ such that there exists
a sequence $x_n\in x_{n-1}\in\cdots\in x_0=A$. Show that the sets of height $\leq n$ are finite and form a finite set,
whose cardinal $p_n$ is computed by means of $p_0=1$, $p_{n+1}=2^{p_n}$ (proceed by induction on $n$, noting that the
elements of a set $A$ of height $\leq n$ are sets of height $\leq n-1$).

3) Let $G$ be a Noetherian ordered set admitting a smallest element $g_0$, and such that for every $h\in G$, the set of
$g\leq h$ is finite and totally ordered.

[PDF p. 232]

a) Show that every element $h\neq g_0$ of $G$ has one and only one predecessor.

b) Let $\omega$ be the map from $G$ defined in Lemma 1 (i.e. $\omega(g)$ is the set of the $\omega(g')$ where $g'$ runs
through the set of successors of $g$). Set $A=\omega(g_0)$. Show that $A$ is an artinian set. For $g\in G$, let
$g_0<g_1<\cdots<g_n=g$ be the sequence of elements $\leq g$; set

```text
f(g) = (omega(g_0), omega(g_1), ..., omega(g_n)).
```

Show that $f$ is an increasing and surjective map from $G$ onto the ordered set $G(A)$ of the text. Show that, if $f$ is
injective, it is an isomorphism from $G$ onto $G(A)$.

c) For $g\in G$, let $M_g$ be the set of upper bounds of $g$. Suppose that, for every pair of distinct elements $g,g'$
having the same predecessor $p$, the ordered sets $M_g$ and $M_{g'}$ are not isomorphic. Show that the map $f$ of b) is
then an isomorphism from $G$ onto $G(A)$.

Hint: if $f(g)=f(g')$ with $g\neq g'$, and if $g_0<g_1<\cdots<g_n=g$ and $g'_0<g'_1<\cdots<g'_{n'}=g'$ are the sequence
of the elements $\leq g$ and that of the elements $\leq g'$, show that $n=n'$, and that one may suppose that $g$ and
$g'$ have the same predecessor $p$. Then consider the set of $p\in G$ such that there exist two distinct successors
$g,g'$ of $p$ such that $f(g)=f(g')$, a maximal element $q$ of this set, and two distinct successors $h,h'$ of $q$ such
that $f(h)=f(h')$. Note that the restrictions of $f$ to $M_h$ and to $M_{h'}$ are injective, hence (by b)) are
isomorphisms from $M_h$ onto $G(\omega(h))$ and from $M_{h'}$ onto $G(\omega(h'))$. Deduce from the hypothesis that
$M_h$ and $M_{h'}$ are not isomorphic that $\omega(h)\neq\omega(h')$, which contradicts $f(h)=f(h')$.

[PDF p. 233]

**N.B.** Exercise 3) gives very precise information on the way in which artinian sets are "made". We already knew that
such a set $A$ is determined by the isomorphism class of the ordered set $G(A)$ (Lemma 1). We now know how to
characterize the ordered sets $G$ isomorphic to some $G(A)$:

a) $G$ is Noetherian and admits a smallest element;

b) for every $g\in G$, the set of $h\leq g$ is totally ordered and finite (whence the existence and uniqueness of the
predecessor of $g$);

c) if $g,g'$ are distinct elements having the same predecessor, the set $M_g$ of upper bounds of $g$ and the set
$M_{g'}$ of upper bounds of $g'$ are not isomorphic.

4) Let $(A_n)_{n\geq 0}$ be the sequence of finite ordinals, defined by $A_0=\emptyset$,
$A_{n+1}=A_n\cup\{A_n\}$. Show that the ordered set $G(A_n)$ has $2^n$ elements, and that the number of its elements of
height $q$ (in the sense of Exerc. 2)) is $\binom{n}{q}$.

### Bibliography

[1] B. Mitchell, *Theory of categories*, Academic Press (1965).
