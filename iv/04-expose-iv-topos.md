# SGA 4-I -- Expose IV: Topoi

> Cleaned from best-effort OCR of the image-only SGA 4-I scan. Page markers refer to the PDF pages. Mathematical
> notation should still be checked against the scan, especially in dense formulas and diagrams.

[PDF p. 313]

# Expose IV -- Topoi

By A. Grothendieck and J.-L. Verdier.

## 0. Introduction

**0.1.** In II we saw various exactness properties of categories of the form $\widetilde{C}$ = category of sheaves of
sets on $C$, where $C$ is a small site, properties that can be expressed by saying that in many respects these
categories (which we shall call topoi) inherit the familiar properties of the category $(\mathrm{Ens})$ of (small) sets.
On the other hand, experience has taught that many situations in mathematics should be considered above all as a
technical means for constructing the corresponding categories of sheaves (of sets), i.e. the corresponding "topoi". It
appears that all genuinely important notions attached to a site (for example its cohomological invariants, studied in V,
various other "topological" invariants, such as its homotopy invariants recently studied by M. Artin and B. Mazur [1],
and the notions studied in J. Giraud's book on noncommutative cohomology) are in fact expressed directly in terms of the
associated topos. From this point of view, two sites should be regarded as essentially equivalent when the associated
topoi are equivalent categories, and the datum of a site (at least in the practically most important case where its
topology is less fine than its canonical topology) amounts to that of a topos $E$ (namely the associated topos, formed
by the sheaves of sets on the site), and of a generating family of elements of $E$

[PDF p. 314]

(cf. II 4.9 and 1.2.1 below). This point of view is analogous to associating a group to any system of generators and any
system of relations among these generators, and attaching one's interest rather to the structure of this group than to
the system of generators and relations which served to generate it (regarded as auxiliary data of the situation).
Moreover, the "comparison lemma" III 5.1 supplies many examples of pairs of sites $C$, $C'$ which are not isomorphic,
and not even equivalent as categories, and which give rise to equivalent topoi, so that $C$ and $C'$ should be regarded
as essentially equivalent.

**0.2.** In the present expose, we give a characterization of topoi by simple exactness properties (due to J. Giraud),
we study the natural notion of morphism of topoi, inspired by the notion of a continuous map from one topological space
to another, and we develop, in the framework of topoi, certain familiar constructions from ordinary sheaf theory
(internal Hom sheaves, tensor product sheaves, supports). Finally, following M. Artin, we show how one can reconstruct a
topos from an "open" of it, from the complementary "closed" part, and from a certain left exact functor relating them,
which, up to very little, can moreover be chosen arbitrarily.

**0.3.** This gives a gluing procedure for topoi which, when applied to topoi coming from ordinary topological spaces,
will in general give a topos no longer of the same type. This is a first indication of the remarkable stability of the
notion of topos under various natural constructions, a stability lacking in the notion of topological space (from which
the notion

[PDF p. 315]

of topos is inspired). For a second remarkable example, let us also mention that of the classifying topos relative to a
group of a topos (cf. [1] or 5.9 below), inspired by the classical notion of classifying space of a topological group,
and the notion of "modular topos" associated to various "moduli problems" in algebraic geometry or analytic geometry
[10] [13].

Other topoi, such as the etale topos of a scheme (studied systematically in the present Seminar starting from Exp. VII)
or the crystalline topos of a relative scheme [6], arise naturally when one wants to develop usable cohomology theories
for abstract algebraic varieties (and more generally schemes), replacing the classical Betti cohomology of algebraic
varieties over the field of complex numbers.

**0.4.** One may therefore say that the notion of topos, a natural derivative of the sheaf-theoretic point of view in
topology, in turn constitutes a substantial enlargement of the notion of topological space (cf. [9], or 4.1 and 4.2
below, for the precise relations between the notion of topos and that of topological space), encompassing a large number
of situations which formerly were not considered as belonging to topological intuition. The characteristic feature of
such situations is that one has in them a notion of "localization", a notion formalized precisely by the notion of site
and, in the last analysis, by that of topos (via the topos associated to the site). Since the term "topos" itself is
intended precisely to suggest this, it seems reasonable and legitimate to the authors of the present Seminar to consider
that the object of topology is the study of topoi (and not of topological spaces alone).

**0.5.** It seemed useful to us to include in this general expose on topoi a fairly large number of examples, many of
which have only remote

[PDF p. 316]

relations with the initial aim of this seminar (namely the study of etale cohomology). The hurried reader, interested
exclusively in etale cohomology, may of course omit without inconvenience the reading of these examples, as also most of
the present expose, to which it will suffice to refer as needed.

## 1. Definition and Characterization of Topoi

**Definition 1.1.** A $U$-topos, or simply a topos if no confusion is to be feared, is a category $E$ such that there
exists a site $C\in U$ such that $E$ is equivalent to the category $\widetilde{C}$ of $U$-sheaves of sets on $C$.

**1.1.1.** Let $E$ be a $U$-topos. We always regard $E$ as endowed with its canonical topology (II 2.5), which therefore
makes it a site, and even, by virtue of 1.1.2 d) below, a $U$-site (II 3.0.2). Unless explicitly stated otherwise, we
shall consider no topology on $E$ other than the one just specified.

**1.1.2.** We saw in II 4.8, 4.11 that a $U$-topos $E$ is a $U$-category (I 1.1) satisfying the following conditions:

1. Finite projective limits are representable in $E$.
2. Direct sums indexed by an element of $U$ are representable in $E$. They are disjoint and universal (II 4.5).
3. Equivalence relations in $E$ are universally effective (I 10.6).
4. $E$ admits a generating family (II 4.9) indexed by an element of $U$.

[PDF p. 317]

In fact, we shall see that these intrinsic properties characterize $U$-topoi:

**Theorem 1.2** (J. Giraud). Let $E$ be a $U$-category. The following properties are equivalent:

1. $E$ is a $U$-topos (1.1).
2. $E$ satisfies conditions a), b), c), and d) of 1.1.2.
3. The $U$-sheaves on $E$ for the canonical topology are representable, and $E$ possesses a small generating family
   (condition 1.1.2 d)).
4. There exist a category $C\in U$ and a fully faithful functor $i : E\to\widehat{C}$ (where $\widehat{C}$ denotes the
   category of $U$-presheaves on $C$) admitting a left adjoint $a$ which is left exact.
5. There exists a site $C\in U$, such that projective limits are representable in $C$ and the topology of $C$ is less
   fine than its canonical topology (II 2.5), such that $E$ is equivalent to the category $\widetilde{C}$ of $U$-sheaves
   of sets on $C$.

Moreover:

**Corollary 1.2.1.** Let $E$ be a $U$-topos, and let $C$ be a full subcategory of $E$, endowed with the topology induced
(III 3.1) by that of $E$ (1.1.1). Consider the functor

```text
E -> C~
```

which associates to every $X\in\operatorname{ob}E$ the restriction to $C$ of the functor represented by $X$. This
functor is an equivalence of categories if and only if $\operatorname{ob}C$ is a generating family of $E$.

[PDF p. 318]

The equivalence i) $\Longleftrightarrow$ iv) follows immediately from II 5.5, and we have already recalled above that i)
$\Rightarrow$ ii). Since i') $\Rightarrow$ i) trivially, it remains to prove ii) $\Rightarrow$ iii) and iii)
$\Rightarrow$ i'), which will be done in 1.2.4 and 1.2.3 below. The corollary is then obtained by observing that the
functor under consideration factors as $E\to\widetilde{E}\to\widetilde{C}$, so that, since $E\to\widetilde{E}$ is an
equivalence by virtue of (iii), the question reduces to determining when $\widetilde{E}\to\widetilde{C}$ is an
equivalence. One then concludes by the "comparison lemma" III 4.1, cf. proof 1.2.3 below.

**1.2.3. Proof of iii) $\Rightarrow$ i').** Let $\mathfrak{X}=(X_i)_{i\in I}$, $I\in U$, be a small generating family of
$E$. Since $E$ is a $U$-category, the set of isomorphism classes of finite diagrams in $E$ whose objects are elements
$X_i$ is $U$-small. Consequently the smallest set $\mathfrak{X}'$ of objects of $E$, containing the finite projective
limits of objects of $\mathfrak{X}$, is a countable union of small sets and is therefore small (*). Setting
$\mathfrak{X}^{(n+1)}=\mathfrak{X}^{(n)}(1)$, and $\mathfrak{X}=\bigcup_n\mathfrak{X}^{(n)}$, one sees that, after
enlarging the family of generators if necessary, one may suppose that $\mathfrak{X}$ is stable under finite projective
limits. Let $V$ be a universe containing $U$ such that $E$ is $V$-small. For every object $H$ of $E$, denote by $I(H)$
the set $\coprod_{i\in I}\operatorname{Hom}(X_i,H)$. Let $H$ be an object of $E$ and let $H'\subset H$ be the subsheaf
of $H$, for the canonical topology, which is the "union" of the images of the morphisms $u : X_i\to H$, $(u,i)\in I(H)$
(II 4.1). Since $H'$ is a subsheaf of a $U$-sheaf, $H'$ is a $U$-sheaf. It is therefore representable. Since the family
$\mathfrak{X}$ is generating and, for every $i\in I$, the map $\operatorname{Hom}(X_i,H')\to\operatorname{Hom}(X_i,H)$
is bijective, the morphism $H'\subset H$ is an isomorphism (II 4.9). Consequently (II 6.1) the family $(u : X_i\to H)$,
$(u,i)\in I(H)$, is covering for the canonical topology of $E$.

(*) We reason here on classes of objects of $E$ up to isomorphism.

[PDF p. 319]

Thus every object of $E$ can be covered, for the canonical topology of $E$, by objects of $\mathfrak{X}$. Let $C$ be the
full subcategory of $E$ defined by the objects of $\mathfrak{X}$, and let $u : C\to E$ be the inclusion functor. The
topology $\mathfrak{T}$ induced on $C$ by the canonical topology of $E$ is less fine than the canonical topology of $C$,
and when $U$ has an element of infinite cardinality, finite projective limits are representable in $C$. It follows from
III 5.1 that the functor $F\mapsto F\circ u$ is an equivalence from $E$ onto the category of $U$-sheaves on $C$ for the
topology $\mathfrak{T}$, Q.E.D.

**1.2.4. Proof of ii) $\Rightarrow$ iii).** The proof has four steps.

Let $V$ be a universe containing $U$, such that $E$ is an element of $V$. Let $\widetilde{E}$ be the category of
$V$-sheaves on $E$ for the canonical topology, and let $J_E : E\to\widetilde{E}$ be the canonical functor.

**1.2.4.1.** Let $(g_i : G_i\to H)$, $i\in I\in U$, be an epimorphic family in $\widetilde{E}$. If the $G_i$ and the
fiber products $G_i\times_H G_j$ are representable, then the sheaf $H$ is representable.

Indeed, the direct sum $\coprod_{i\in I}G_i$ is representable in $\widetilde{E}$ (II 4.1) by a representable sheaf $G$
(property b) and II 4.6). The same is true for the direct sum

```text
K = coproduct_{(i, j) in I x I} G_i x_H G_j.
```

Moreover, the diagram $K\rightrightarrows G\to H$ is exact and $K$ is the fiber square of $G$ over $H$. This last
property is true in the category of presheaves, hence true in the category of sheaves (II 4.1). One deduces from c) and
II 4.7 that the sheaf $H$ is representable.

**1.2.4.2.** Let $X_\alpha$, $\alpha\in A\in U$, be a family of generators of $E$. For every sheaf $H$, denote by $I(H)$
the set $\coprod_{\alpha\in A}\operatorname{Hom}_E(X_\alpha,H)$. The family

[PDF p. 320]

$(u : X_\alpha\to H,\ (u,\alpha)\in I(H))$ is epimorphic in $\widetilde{E}$. When $H$ is a $U$-sheaf, $I(H)$ is an
element of $U$.

Indeed, since every sheaf $H$ is the target of an epimorphic family of morphisms whose sources are representable sheaves
(I 3.4 and II 4.1), it suffices to prove the first assertion when the sheaf $H$ is representable. Let $G$ then be the
image of the family $(u : X_\alpha\to H,\ (u,\alpha)\in I(H))$. The morphism $G\to H$ is a monomorphism. Consequently we
are in the situation of the first step, because $X_\alpha\times_G X_\beta$ is isomorphic to $X_\alpha\times_H X_\beta$,
which is representable, and moreover $I(H)$ is an element of $U$. It follows that $G$ is representable. But since the
$X_\alpha$ are a generating family, $G\to H$ is an isomorphism. The last assertion is trivial by definition of
$U$-sheaves.

**1.2.4.3.** Every subsheaf of a representable sheaf is representable.

Indeed, let $G\to H$ be a subsheaf of a representable sheaf. Then $G$ is a $U$-sheaf. The family
$(u : X_\alpha\to G,\ (u,\alpha)\in I(G))$ is therefore epimorphic in $\widetilde{E}$ and indexed by an element of $U$.
Moreover, the fiber products $X_\alpha\times_G X_\beta$ are isomorphic to the fiber products $X_\alpha\times_H X_\beta$,
which are representable. Consequently we are in the situation of the first step and $G$ is representable.

**1.2.4.4.** Every $U$-sheaf is representable.

Indeed, by virtue of the first and second steps, it suffices to show that the fiber products $X_\alpha\times_H X_\beta$
are representable. But these fiber products are subobjects of the products $X_\alpha\times X_\beta$. We therefore
conclude by the third step. This completes the proof of Theorem 1.2.

[PDF p. 321]

**Remark 1.3.** Of course, for a given $U$-topos $E$, there is in general no privileged way to represent it, up to
equivalence, in the form $\widetilde{C}$, with $C$ a small site; or, what amounts essentially to the same thing by
virtue of 1.2.1 when one restricts to those $C$ whose topology is less fine than the canonical topology, there is no
privileged small generating family in $E$. When one stops imposing on $C$ the condition that $C$ be small, however, by
virtue of 1.2 iii) there is a completely canonical choice of a $U$-site $C$ such that $E$ is equivalent to
$\widetilde{C}$, namely $E$ itself! This is one of the technical reasons why it is not convenient in practice to work
only with small sites: in fact, the most important sites of all, namely the $U$-topoi, are not small! Moreover, the
topos-generating sites which arise in many questions in algebraic geometry (indeed in topology, cf. 2.5) are not small
either; example: the etale site of a scheme (VIII 1).

**Proposition 1.4.** Let $E$ be a $U$-topos, let $E'$ be a category (not necessarily a $U$-category), and let $F$ be a
presheaf on $E$ with values in $E'$. For $F$ to be a sheaf with values in $E'$ (II 6.1), it is necessary and sufficient
that $F$ transform $U$-inductive limits in $E$ into projective limits in $E'$.

Let $V$ be a universe containing $U$ and such that $E'$ is a $V$-category. By composing $F$ with the functors
$\operatorname{Hom}(X',-) : E'\to V\text{-}\mathrm{Ens}$ defined by the objects $X'$ of $E'$, one is reduced to the case
where $E'=V\text{-}\mathrm{Ens}$, where $V$ is a universe.

Suppose that $F$ transforms $U$-inductive limits into projective limits; then it follows immediately from the
definitions that $F$ is a sheaf, since a covering

[PDF p. 322]

family $X_i\to X$ in $E$, by definition of the canonical topology of $E$, makes it possible to regard $X$ as an
inductive limit of the diagram $(X_i\times_X X_j\rightrightarrows X_i)$. Suppose that $F$ is a sheaf, and let us prove
that it transforms $U$-inductive limits into projective limits. If $V\subset U$, one may suppose $V=U$ and it suffices
to apply criterion 1.2 iii). To treat the general case, a little more work is needed.

Let $C$ be a full subcategory of $E$ generated by a generating family indexed by an element of $U$, and let $u : C\to E$
be the inclusion functor. Endow $C$ with the topology induced by the canonical topology of $E$ (III 4.5). Let
$\widetilde{C}_U$, $\widetilde{C}_V$ denote the categories of sheaves on $C$, and let $\widetilde{E}_V$ denote the
category of $V$-sheaves on $E$ for the canonical topology; let $J_E : E\to\widetilde{E}_V$ be the canonical functor, and
let $i_{U,V} : \widetilde{C}_U\to\widetilde{C}_V$ be the inclusion functor. The diagram

```text
C~_U  --i_{U,V}-->  C~_V
  ^                  ^
  |                  |
  E   ----J_E----->  E~_V
```

where the vertical arrows are induced by the functor $F\mapsto F\circ u$, is commutative. It follows from the explicit
construction of the associated sheaf functor (II 3) and from II 4.1 that the functor $i_{U,V}$ commutes with
$U$-inductive limits. Moreover, it follows from III 5.1 and 1.5 that the vertical arrows in (*) are equivalences of
categories. Consequently $J_E : E\to\widetilde{E}_V$ commutes with $U$-inductive limits. For every object $X$ of $E$,
one has:

```text
F(X) ~= Hom_{E~_V}(J_E(X), F).
```

[PDF p. 323]

Therefore $F$ transforms $U$-inductive limits of $E$ into projective limits.

**Corollary 1.5.** Let $E$ be a $U$-topos, let $E'$ be a $U$-category, and let $f : E\to E'$ be a functor. For $f$ to
admit a right adjoint, it is necessary and sufficient that $f$ commute with $U$-inductive limits.

This is an immediate consequence of 1.4 for the case $E'=U\text{-}\mathrm{Ens}$.

**Corollary 1.6.** Let $E$, $E'$ be two $U$-topoi, and let $f : E\to E'$ be a functor. The following conditions are
equivalent:

1. $f$ commutes with $U$-inductive limits.
2. $f$ admits a right adjoint.
3. $f$ is continuous (III 1.1).

The equivalence i) $\Longleftrightarrow$ ii) was seen in 1.5. To prove i) $\Longleftrightarrow$ iii), apply the
definition of continuous functors, choosing a universe $V$ such that $U\in V$ (so $E$, $E'$ are $V$-small sites). One
must express that for every $V$-sheaf $F$ on $E'$, the composite $F\circ f$ is a sheaf on $E$, i.e. (1.4) that it
transforms $U$-inductive limits into projective limits. It is sufficient for this that i) hold, since by virtue of 1.4
$F$ itself transforms $U$-inductive limits into projective limits; it is also necessary, as one sees by taking $F$ to be
a representable functor.

**Corollary 1.7.** With the notation of 1.6, for $f$ to be the inverse image functor $u^*$ for a morphism of topoi (3.1)
$u : E'\to E$, it is necessary and sufficient that $f$ be left exact and transform epimorphic families into epimorphic
families.

[PDF p. 324]

Necessity is trivial by definition (NB every right exact functor transforms epimorphisms into epimorphisms). Sufficiency
follows from III 2.6, which implies that $f$ is continuous under the indicated conditions, hence commutes with
$U$-inductive limits by virtue of 1.6.

**Remark 1.8.** With the notation of 1.5, one can show that $f$ admits a left adjoint if and only if it commutes with
$U$-projective limits. In other words, a covariant functor $E\to(U\text{-}\mathrm{Ens})$ is representable if and only if
it commutes with $U$-projective limits. A more general statement is found in I 8.12.8, 8.12.9; the sketch of proof in a)
to c) corresponds to the proof given in loc. cit. We indicate only the principle of the proof:

1. Standard arguments [5, No. 195, § 3] show that if $F$ commutes with projective limits, it is pro-representable by a
   strict projective system $(T_i)_{i\in I}$, where $I$ is a filtered ordered set, not necessarily small. One may
   suppose that if $i>j$, then $T_i\to T_j$ is not an isomorphism, and under this hypothesis $F$ is representable if and
   only if $I$ is small (which in fact implies that the projective system is essentially constant).
2. To prove that $I$ is small, knowing that for every object $X$ of $E$ the set
   $F(X)=\varprojlim_i\operatorname{Hom}(T_i,X)$ is small, it suffices to have a small cogenerating family
   $(X_j)_{j\in J}$ (i.e. one which is generating for the opposite category $E^\circ$). But one shows that in a
   $U$-topos $E$ there always exists a small cogenerating family.
3. To prove this last point, one notes by standard arguments [Toh] that every object $X$ of $E$ admits a monomorphism
   into an "injective" object; then, for any generating family $(L_\alpha)$ of $E$,

[PDF p. 325]

if one embeds each $L_\alpha$ in this way into an injective object $I_\alpha$, the family $(I_\alpha)$ is cogenerating.

## 2. Examples of Topoi

**2.0.** We have collected in this number a fairly large number of typical examples of topoi, which the reader will
already have had occasion to meet elsewhere, and which are intended to make access to the "yoga" of topoi easier. For
other examples (drawn from algebraic geometry) of topologies on sites, giving rise to as many topoi, the reader may
consult SGA 3 IV 6 and (for the etale topos) Expose VII of the present seminar. Since in what follows we shall refer to
the present number hardly at all except for questions of notation or terminology, we leave to the reader, as an
exercise, the verification of the statements with which we have accompanied these examples for general instruction. All
the examples of the present number will be made precise in 4, where their functorial dependence on the data will be
examined, and in the following numbers as illustrations of the general notions relative to topoi.

### 2.1. Topos Associated to a Topological Space

Let $X$ be a small topological space, and let $\operatorname{Ouv}(X)$ be the category of open subsets of $X$, endowed
with the canonical topology (III 2.9.1). We shall denote by $\operatorname{Top}(X)$ the topos of $U$-sheaves on
$\operatorname{Ouv}(X)$. This topos is equivalent to the category of etale topological spaces over $X$, by associating
to every such space $X'$ over $X$ the sheaf $U\mapsto\Gamma(X'/U)=\operatorname{Hom}_X(U,X')$ on $\operatorname{Ouv}(X)$
[TF]. We shall not be able to keep ourselves from sometimes denoting, by abuse

[PDF p. 326]

of language, by the same letter $X$ the topos $\operatorname{Top}(X)$ defined by the topological space $X$.

It is of course the preceding example which served principally as guide and intuitive support for the development of the
theory of topoi. One should be careful, however, that the topoi deduced from topological spaces are of a very special
nature, due in particular to the fact that they have been described by sites $C=\operatorname{Ouv}(X)$ in which all
morphisms are monomorphisms (hence whose underlying category reduces to a preordered set). It follows in particular that
the sheaves represented by the objects of $C$ are subsheaves of the final sheaf, and consequently that the subsheaves of
the final sheaf form a generating family of the topos under consideration. This property is not shared by most of the
topoi which arise naturally in algebraic geometry or algebra, cf. examples below. It is, up to very little,
characteristic of topoi of the form $\operatorname{Top}(X)$ (cf. 7.1.9 below).

One verifies easily that the map $\operatorname{Ouv}(X)\to\operatorname{Top}(X)$, which associates to every open subset
of $X$ the sheaf it represents, is a bijection from $\operatorname{Ouv}(X)$ onto the set of subobjects of the final
object of $\operatorname{Top}(X)$, this bijection even being an isomorphism for the natural order structures, i.e.
inducing an isomorphism of the corresponding categories. This suggests that it should be possible to reconstruct, up to
homeomorphism, the topological space $X$, when one knows $\operatorname{Top}(X)$ up to equivalence. We shall see below
(4.2) that this is indeed so, subject to a slight restriction on $X$.

[PDF p. 327]

### 2.2. Punctual or Final Topos, and Empty or Initial Topos

When $X$ is a topological space reduced to a single point, the functor

```text
F |-> F(X) : Top(X) -> U-Ens
```

is an equivalence of categories. This shows in particular that the category $U\text{-}\mathrm{Ens}$ is a $U$-topos. We
saw in examples in Exp. II that this $U$-topos is typical from the point of view of exactness properties, in that the
verification of many properties (notably exactness properties) of general topoi reduces to this particular topos. The
interpretation we give here in terms of the punctual topological space justifies the abuse of language consisting in
calling a topos equivalent to the category $U\text{-}\mathrm{Ens}$ a punctual topos (although, as a category, it is not
at all equivalent to the punctual category $1$). This is the terminology corresponding to the correct geometric
intuition of the role played by these topoi. Sometimes, also by abuse of language, a punctual topos is called a final
topos, cf. 4.3; we shall say "the final topos" for the topos $(U\text{-}\mathrm{Ens})$.

When $X$ is reduced to the empty topological space, and hence $\operatorname{Ouv}(X)$ to the punctual category, then a
presheaf $F$ on $\operatorname{Ouv}(X)$ is a sheaf if and only if its value at the unique object $\emptyset$ of
$\operatorname{Ouv}(X)$ is a one-point set. It follows that $\operatorname{Top}(\emptyset)$ is isomorphic to the
category of one-point $U$-sets, a category equivalent to the punctual category. From this one concludes in particular
that the punctual category (as well as every $U$-category equivalent to it) is a $U$-topos. It is sometimes called, by
abuse

[PDF p. 328]

of language, the empty topos or initial topos (cf. 4.4); one should take care that it is not equivalent to the empty
category.

### 2.3. Topos Associated to a Space with Operators

Let $X$ be a topological space, and let $G$ be a discrete group acting on $X$ by homeomorphisms. In [Toh. 5.1] one then
defined the category of $G$-sheaves on $X$, or, as we shall also say, of sheaves on $(X,G)$; these are the sheaves (of
sets) on $X$, equipped with operations of $G$ compatible with those of $G$ on $X$. One immediately sees, using Giraud's
criterion 1.2 iii), that this category is a topos (NB $U$ is understood throughout here), which we shall simply denote
by $\operatorname{Top}(X,G)$.

When $G$ is reduced to the unit group, one recovers Example 2.1; when $X$ is reduced to the punctual space, one finds
the topos of sets on which $G$ acts on the left (or $G$-sets), also called the classifying topos of the discrete group
$G$, and denoted $B_G$. One verifies easily that the only subobject of the final object $e$ of the topos $B_G$ is $e$ or
the empty sheaf $\emptyset$; in particular, if $G$ is not reduced to the unit group, the subobjects of the final object
of the classifying topos $B_G$ do not form a generating family of $B_G$. Thus $B_G$ is then not equivalent to a topos of
the type $\operatorname{Top}(X)$ considered in 2.1.

The notion of $G$-sheaf was introduced in loc. cit. to develop the cohomological theory of abelian $G$-sheaves.
Interpreting these as the abelian sheaves of the topos $(X,G)$, that theory is included in Exp. V, developed in the
framework of general topoi.

[PDF p. 329]

More generally, one may try to attach an appropriate topos to a topological space $X$, equipped with a topological group
$G$ (not necessarily discrete) of automorphisms, which would give rise to an adequate cohomological theory. Similarly in
the context of differentiable varieties, or real or complex analytic varieties, or schemes. This is indeed possible, cf.
2.5 below.

### 2.4. Classifying Topos of a Group

Let $E$ be a topos, and let $G$ be a group of $E$. Let $(E,G)$ be the category of objects of $E$ on which $G$ acts. By
Giraud's criterion, one immediately sees that it is a topos. It is called the classifying topos of the group $G$, and is
denoted $B_G$. When $E$ is the punctual topos (2.2), i.e. when $G$ is an ordinary group, one recovers the classifying
topos of 2.3.

The terminology adopted here is justified by the fact that the topos $B_G$ plays a universal role for the classification
of "torsors" (or homogeneous principal bundles) under $G$, or more generally under the $G_{E'}=f^*(G)$, where $E'$ is a
topos "over $E$", i.e. equipped with a morphism $f : E'\to E$ (cf. 3.1 below). This role, made explicit in [3, Chap. V]
or in 5.9 below, shows that $B_G$ plays, in the context of topoi, the same role as the classical classifying spaces of
topological groups in the homotopy theory of topological spaces. The latter may be regarded (cf. 2.5) as a weakened
version of the former, obtained by retaining from the classifying topos only the "homotopy type" of that topos, in a
suitable sense that need not be specified here.

[PDF p. 330]

### 2.5. "Big Site" and "Big Topos" of a Topological Space. Classifying Topos of a Topological Group (*)

Let $U\text{-}\mathrm{Esp}$, or simply $(\mathrm{Esp})$, be the category of topological spaces $\in U$. We know that in
$(\mathrm{Esp})$ finite projective limits are representable. Consider on $(\mathrm{Esp})$ the pretopology (I 1.3) for
which $\operatorname{Cov}(X)$ is the set of surjective families of open immersions $u_i : X_i\to X$. We shall regard
$(\mathrm{Esp})$ as a site by means of the topology generated by the preceding pretopology. For every object $X$ of
$(\mathrm{Esp})$, consider the category

```text
(Esp)/X
```

of objects of $(\mathrm{Esp})$ over $X$, i.e. of topological spaces over $X$, as a site, by means of the topology induced
by that of $(\mathrm{Esp})$ via the forgetful functor $(\mathrm{Esp})/X\to(\mathrm{Esp})$ (III 5.2 4)). This site is
called the big site associated to $X$. One should be careful that it is not $\in U$; it is not a $U$-site in the sense of
II 3.0.2 either, so precautions are necessary in order to apply the usual results to it. To remedy this inconvenience,
one may choose a universe $V$ such that $U\in V$, so that $(\mathrm{Esp})/X$ becomes a $V$-site, and one may work with
the associated $V$-topos $((\mathrm{Esp})/X)^\sim$, which may be denoted $\operatorname{TOP}(X)$ and will be called the
big topos of $X$. If one is reluctant to enlarge $U$, one may choose a cardinal $c$ bounding the cardinals of $X$ and of
all the topological spaces one expects to involve in the arguments (most often, $\operatorname{Sup}(\operatorname{card}
X,\operatorname{card} R)$ will suffice!), and replace $(\mathrm{Esp})/X$ by the subcategory $(\mathrm{Esp})'/X$ formed
by the $X'$ over $X$ such that $\operatorname{card}X'\leq c$, endowed with the induced topology, and denote by
$\operatorname{TOP}(X)$ the topos of sheaves on

[PDF p. 331]

this site. To fix ideas, suppose that the first definition has been adopted.

(*) The introduction of these sites and topoi is due to M. Giraud, who also brought to light their advantages over the
traditional "small" site.

The advantage of the big topos of $X$ over the small one is that the site defining it contains $(\mathrm{Esp})/X$ as a
full subcategory; since the topology of this site is manifestly less fine than the canonical topology, one sees that the
canonical functor from $(\mathrm{Esp})/X$ to $\operatorname{TOP}(X)$, associating to every space $X'$ over $X$ the sheaf
it represents, is fully faithful. Consequently, a space $X'$ over $X$ is known up to $X$-isomorphism when one knows the
sheaf ($\in\operatorname{TOP}(X)$) it defines; thus the notion of sheaf on (the big site of) $X$ may be regarded as a
generalization of the notion of topological space over $X$, by means of which all constructions of sheaf theory take on
a meaning for topological spaces over $X$.

Thus, when $G$ is a group object of the category $(\mathrm{Esp})/X$ of topological spaces over $X$, one can associate to
it the classifying topos $B_G$ (2.4), hence classifying cohomology groups, classifying homotopy groups, etc. (defined as
the corresponding invariants of the $V$-topos $B_G$). In particular, when $X$ is a punctual space, $G$ is identified
with an ordinary topological group. One can verify, subject to the usual local conditions ensuring that the singular
cohomology of the cartesian products $G^n$ coincides with sheaf cohomology (for constant coefficients, say), for example
if $G$ is locally contractible, that the cohomology of the classifying topos of $G$ is canonically isomorphic to that of
the classifying space of $G$ in the sense of topologists.

[PDF p. 332]

The introduction of classifying topoi (via the "big sites") has the advantage over classifying spaces of providing a
richer theory, since in particular they provide useful cohomological invariants for coefficients more general than
constant or locally constant coefficients. Moreover, the definition considered here adapts in an evident way to the
other usual contexts: differentiable varieties, real or complex analytic varieties or spaces, schemes. This point of
view makes it possible in particular to connect the study of characteristic classes from the traditional point of view
and from the "arithmetic" point of view, by considering the "classical groups" as coming from schemes defined over the
ring of integers; cf. [7] for indications in this direction. Similarly, J. Giraud's general results [3] on the
classification of extensions of groups, developed in the very general and very flexible framework of topoi, can, thanks
to the "big topoi", be specialized to results on the classification of extensions of topological groups, or of real or
complex Lie groups, which seem to have been hardly known to topologists except in the case of extensions with abelian
kernel [11].

### 2.6. Topoi of the Form $\widehat{C}$

Let $C$ be a small category. Then the category $\widehat{C}$ of $U$-presheaves on $C$ is evidently a $U$-topos, since it
is of the form $C^\wedge$, where $C$ is endowed with the chaotic topology. We shall give below a few details on the
relations between $C$ and $\widehat{C}$. Let us only note here that a topos $E$ equivalent to a topos of the form
$\widehat{C}$ is of a rather special nature, because it admits a small generating family $(X_i)$ formed of connected
projective objects, i.e. objects $X$ such that the functor

[PDF p. 333]

```text
Y |-> Hom(X, Y)
```

transforms epimorphisms into epimorphisms and sums into sums: indeed it suffices to take in $\widehat{C}$ the generating
family formed by the functors represented by the $X\in\operatorname{ob}C$. Note moreover that if in a topos $E$ one has
a covering family $X_i\to X$, with the $X_i$ projective and connected, then every other covering family of $X$ is
majorized (I 4.3.2, 4.3.3) by the preceding one. Consequently, in a topos $E$ of the form $\widehat{C}$ every object $X$
admits a covering family majorizing all the others. A topos of the form $\operatorname{Top}(X)$ (2.1), with $X$ a
topological space whose points are closed, has the preceding property only if $X$ is discrete.

When the category $C$ has a single object, $C$ is identified with a monoid $G$. A presheaf on $C$ is then identified
with a set on which $G$ acts on the right (since it is a functor $G^\circ\to(\mathrm{Ens})$), and $\widehat{C}$ is the
topos of sets with a monoid of right operators, which may also be denoted $B_{G^\circ}$. Taking 2.3 into account: this
is the topos of sets with monoid of operators $G^\circ$ (the monoid opposite to $G$). When $G$ is a group, using the
isomorphism $g\mapsto g^{-1}$ from $G$ onto $G^\circ$, one recovers the classifying topos $B_G$ of 2.3.

### 2.7. Classifying Topos of a Pro-Group

**2.7.1.** Let $G=(G_i)_{i\in I}$ be a projective system of groups, with $G_i\in U$. Suppose the projective system is
strict, i.e. the transition morphisms $G_j\to G_i$ are surjective. If $E$ is a set, an operation of $G$ on $E$ (on the
left, say) means the following structure:

1. a family $(E_i)_{i\in I}$ of subsets of $E$, with union $E$;
2. for every $i\in I$, an action of the group $G_i$ on the set $E_i$.

These data are moreover supposed subject

[PDF p. 334]

to the following condition: for $j\geq i$, $E_i$ is the subset of $E_j$ formed by the elements fixed under the kernel
group of $G_j\to G_i$. We also say that $G$ acts on $E$ (on the left) if an action of $G$ on $E$ (on the left) has been
given. The sets $\in U$ equipped with an action of $G$ form a category in the evident way. By Giraud's criterion, one
immediately sees that this category is a $U$-topos. It is denoted $B_G$, and is called the classifying topos of $G$.
When $I$ admits an initial object $i_0$, setting $G=G_{i_0}$, one recovers the classifying topos of 2.3.

**2.7.2.** Another important example is the one where the groups $G_i$ are finite, so that

```text
G = lim<-_i G_i
```

is a compact totally disconnected topological group, or profinite group. An action of $G$ on $E$ then amounts to an
action of $G$ on $E$ which is continuous, or equivalently, such that the stabilizer of every point of $E$ is an open
subgroup of $G$. The classifying topos of the topological group $G$ will also be denoted $B_G$, where, of course, $G$
must be regarded as endowed with its profinite topology.

**2.7.3.** It is easy to verify, using the remarks of 2.6, that the topos $B_G$ defined by a strict projective system
$G=(G_i)_{i\in I}$ of groups is equivalent to a topos of the form $\widehat{C}$ only if this projective system is
essentially constant; in the case of a profinite group, this means that this group is in fact finite.

**2.7.4.** The following geometric interpretation of the classifying topos $B_G$ of a discrete group $G$ is useful for
giving correct geometric intuition about these topoi. (Cf. also, in the same direction, 4.5, 5.8, 5.9, and 7.2 below.)
Let $X$ be a connected, locally connected

[PDF p. 335]

and locally simply connected topological space, let $x$ be a point of $X$, and let $G$ be its fundamental group at $x$.
(NB it is known that, up to isomorphism, every discrete group $G$ can be obtained in this way.) Then Galois theory of
covering spaces of $X$ gives an equivalence between the category $B_G$ of $G$-sets and the category of etale coverings
of $X$, i.e. of spaces $X'$ over $X$ which are locally $X$-isomorphic to $X$-spaces of the form $X\times I$, where $I$
is a discrete space. (Compare SGA 1 V 4.5.) This latter category may moreover be interpreted as the category of locally
constant sheaves on $X$, i.e. the category of locally constant objects (IX 2.0) of the topos $\operatorname{Top}(X)$.

When $G$ is a profinite group, there is an analogous geometric interpretation of $B_G$ as the category of $X$-schemes
which are sums of finite etale coverings of a connected scheme $X$, equipped with a geometric point $x$ and with an
isomorphism $G\simeq\pi_1(X,x)$. It is again known that every profinite group can be obtained as the fundamental group
of a suitable connected scheme (the spectrum of a field, if desired). Finally, one also encounters pro-groups (not
necessarily profinite nor essentially constant) for the classification of coverings of connected and locally connected
spaces which are not locally simply connected, or the classification of etale coverings, not necessarily finite or
ind-finite, of nonnormal connected schemes. For this last case, cf. SGA 3 X 6.

**Exercise 2.7.5.** Define for a topos $E$ the notions of connectedness, local connectedness (*), simple connectedness,
and local simple connectedness. Define the notion of a constant object and of a locally constant object of $E$ (cf. IX
2.0). Let

[PDF p. 336]

$f : E'\to E$ be a morphism of topoi (3.1), with $E'$ simply connected (for example $E'$ the punctual topos (2.2)), and
$E$ connected and locally connected. Define a strict pro-group $\pi_1(E,f)=(G_i)_{i\in I}=G$ (called the fundamental
pro-group of $E$ at $f$) and an equivalence of categories from $B_G$ to the category of locally constant objects of $E$.
(*) Show that when $E$ is locally simply connected, $\pi_1(E,f)$ is essentially constant and is therefore identified
with an ordinary discrete group $\pi_1(E,f)$, called the fundamental group of $E$ at $f$. Show that every strict
pro-group $G$ is isomorphic (as a pro-group) to the fundamental pro-group of a suitable connected and locally connected
topos at a suitable $f$, with $E'$ the punctual topos (take $E=B_G$, and $f : E'\to E$ defined by the forgetful functor
$f^* : E\to E'=(\mathrm{Ens})$). When $G$ is essentially constant, i.e. isomorphic (as a pro-group) to an ordinary
discrete group, prove that one can take $E$ above to be locally simply connected (again take $E=B_G$).

(*) One may draw inspiration from SGA 3 X 6.

### 2.8. Example of a False Topos

Let $G=(G_i)_{i\in I}$ be a strict pro-group, where $I$ is filtered ordered and where $i>j$ implies that $G_i\to G_j$ is
not an isomorphism. Suppose that $\operatorname{card}(I)\notin U$. Consider the category of sets $E\in U$ on which $G$
acts on the left (2.7.1). It is a $U$-category, and one sees as in 2.7.1 that this category satisfies conditions a), b),
c) of 1.1.2. However it is not a $U$-topos, because one sees that it admits no generating family which is $U$-small.
Similarly one sees that it is not a $V$-topos for any universe $V$.

[PDF p. 337]

## 3. Morphisms of Topoi

**Definition 3.1.** Let $E$ and $E'$ be two $U$-topoi. A morphism from $E$ to $E'$, or sometimes (by abuse of language)
a continuous map from $E$ to $E'$, is a triple $u=(u_*,u^*,\varphi)$, formed by functors

```text
u_* : E -> E',        u^* : E' -> E
```

and by an "adjunction" isomorphism $\varphi$ of bifunctors in $X'\in\operatorname{Ob}E'$, $Y\in\operatorname{Ob}E$:

```text
phi : Hom_E(u^*(X'), Y) ~= Hom_{E'}(X', u_*(Y)),
```

the functor $u^*$ being moreover subject to the condition of being left exact, i.e. of commuting with finite projective
limits. The functor $u_*$ is called the direct image functor for the morphism of topoi $u$, the functor $u^*$ is called
the inverse image functor for the morphism of topoi $u$, and the isomorphism $\varphi$ is called the adjunction
isomorphism for $u$.

**3.1.1.** Unless explicitly stated otherwise, for a morphism of topoi $u : E\to E'$ we shall subsequently denote by
$u_*$ and $u^*$ the corresponding direct image and inverse image functors (*). Note that, since $u_*$ is right adjoint
to $u^*$ and $u^*$ is left adjoint to $u_*$ by the adjunction isomorphism $\varphi$, each of the two functors $u_*$,
$u^*$ determines the other up to unique isomorphism, by the well-known sorites of adjoint functors [14]. In practice,
depending on the case, it may be more convenient to define a morphism of topoi $u : E\to E'$ either by giving
$u^* : E'\to E$, or by giving $u_* : E\to E'$; in the first case, one must simply verify that the given functor $u^*$

[PDF p. 338]

admits a right adjoint and is left exact. In the second, that the given functor $u_*$ admits a left adjoint which is
left exact. In either case, from the partial datum, by choosing an adjoint functor and an adjunction isomorphism, one
deduces a morphism of topoi $u : E\to E'$, and this latter will be "unique up to unique isomorphism" in terms of the
datum $u^*$ resp. $u_*$, in a fairly clear sense, which will moreover be made entirely explicit below (3.2.1).

(*) Sometimes one should also write $u^{-1}$ instead of $u^*$.

**3.1.2.** If $u : E\to E'$ is a morphism of topoi, it follows from the properties of adjoint functors (I 2.11) that the
direct image functor $u_* : E\to E'$ commutes with projective limits, and the functor $u^* : E'\to E$ commutes with
inductive limits (+). Since this latter is moreover supposed to be left exact, i.e. to commute with finite projective
limits, one sees in particular that $u^*$ is exact. Thus one may say that it is the inverse image functor $u^*$, in the
pair $(u_*,u^*)$, which has the most remarkable exactness properties. These properties ensure that for every species of
algebraic structure $\Sigma$ whose data can be described in terms of data of arrows between the base sets and sets
deduced from these by repeated application of operations of finite projective limits and arbitrary inductive limits, and
for every "object of $E'$ equipped with a structure of species $\Sigma$" (a notion which makes sense thanks to the
internal exactness properties of the topos $E'$ (II 4.1)), its image by $u^*$ is equipped with the same structures.
Rather than undertaking the unappealing task of giving a precise meaning to this statement and

[PDF p. 339]

justifying it formally, we advise the reader to make it explicit and convince himself of its validity for species of
structure such as that of group, ring, module over a ring, comodule over a ring, bialgebra over a ring, torsor under a
group. (In these examples, the first three species of structure are defined exclusively in terms of finite projective
limits, while the other notions implicitly involve constructions also appealing to inductive limits.) Moreover, the
functor $u^*$ "commutes" with all the usual functorial operations made in terms of such structures, more precisely with
all operations that can be expressed in terms of $\varinjlim$ and finite $\varprojlim$: constructions of free objects
(free groups or modules, for example) generated by an object, tensor products (cf. § 12 below), etc.

(+) Moreover (1.5 and 1.6), for a given functor $u_* : E\to E'$ resp. $u^* : E'\to E$, this functor admits a left
adjoint (resp. right adjoint) if and only if it commutes with $U$-projective limits (resp. $U$-inductive limits).

As for the direct image functor $u_* : E\to E'$, which commutes with projective limits, it consequently "respects" every
algebraic structure on an object (or a family of objects) of $E$ definable exclusively in terms of projective limits
(such as structures of group, ring, or module over a ring, among the preceding examples). On the other hand, the functor
$u_*$ is in general not right exact, i.e. it does not in general commute with finite inductive limits, and it does not
even in general transform epimorphisms into epimorphisms (indeed this lack of exactness of the functor $u_*$ is the
source of its cohomological properties, which will be studied (from the point of view of commutative homological
algebra) in the following expose). Consequently, it does not extend, in general, to a functor on objects of the type
comodule, or bialgebra, or torsor under a group, and it does not in general commute with operations such as "free
generated module", tensor product of modules, etc.

[PDF p. 340]

**3.1.3.** In practice, when one has a functor $f : E\to F$ from one $U$-topos to another, one should make explicit all
its exactness properties, including the possible existence of left or right adjoint functors (cf. footnote 26), in order
to arrive at an understanding of the "geometric nature" of $f$, an understanding that will generally be an indispensable
guide for correct geometric intuition about the situation. Thus, if it turns out that $f$ commutes with arbitrary
inductive limits and finite projective limits, one should write $f$ in the form

```text
f = u^*,
```

where

```text
u : F -> E
```

is a morphism of topoi, i.e. interpret $f$ as an "inverse image" functor by a "continuous map" of topoi. When $f$
commutes with arbitrary projective limits, hence admits a left adjoint, and if this latter (which a priori commutes with
arbitrary inductive limits) moreover commutes with finite projective limits, one should write $f$ in the form

```text
f = v_*,
```

where

```text
v : E -> F
```

is a morphism of topoi. In some cases, it may happen that $f$

[PDF p. 341]

satisfies both of the two properties considered (cf. 4.10 for an example). In this case one should introduce
simultaneously the morphisms of topoi

```text
u : F -> E      and      v : E -> F,
```

which give rise to a sequence of three adjoint functors (I 5.3):

```text
v^*,  v_* = u^* = f,  u_*.
```

One should then carefully distinguish between the morphisms of topoi $u$ and $v$, under penalty of losing the geometric
intuition of the situation.

In this connection, note that when between two topoi $E$, $F$ one has a sequence of three adjoint functors

```text
e, f, g      (e, g : F -> E,  f : E -> F),
```

then $f$ commutes with arbitrary inductive and projective limits, so it can always be put in the form $u^*$, where
$u : F\to E$ is a morphism of topoi. Then $g$ is therefore written $g=u_*$. On the other hand, of course, $e$ can be
written in the form $v^*$ (and then $f$ in the form $v_*$) only if it moreover commutes with finite projective limits.
This will obviously be the case if it is itself the right adjoint of a fourth functor $d$. Without a condition of this
nature, one often writes:

```text
e = u_!
```

for the left adjoint of an inverse image functor $f=u^*$, when such a left adjoint exists, this notation being suggested
by the example of an open immersion $u : X\to Y$ of topological spaces. Similarly, if $e$ is of the form $v^*$, i.e. $f$
of the form $v_*$, one sometimes writes $g=v^!$ for the right adjoint of a direct image functor $v_*$, when this adjoint
exists (*).

(*) Cf. below, in the case of abelian sheaves.

[PDF p. 342]

**3.2.** Let $E$, $E'$ be two $U$-topoi, and let

```text
u = (u_*, u^*, phi),      v = (v_*, v^*, psi) : E => E'
```

be two morphisms of topoi from $E$ to $E'$. A morphism from $u$ to $v$ means any morphism from $u_*$ to $v_*$ (in the
sense of the category $\operatorname{Hom}(E,E')$ of functors from $E$ to $E'$). Morphisms of morphisms of topoi compose
in the evident way, and one thus defines a category, which is in fact a $U$-category (I 7.8), denoted

```text
Homtop(E, E'),
```

called the category of morphisms (or continuous maps) from $E$ to $E'$. One then defines in the evident way a functor

```text
u |-> u_* : Homtop(E, E') -> Hom(E, E'),
```

a functor which is fully faithful by definition of the arrows in the source (but is not injective on objects).

**3.2.1.** One should be careful that, if $u$ and $v$ are given as above, the theory of adjoint functors supplies a
canonical bijection

```text
Hom(u_*, v_*) ~= Hom(v^*, u^*) ;
```

in particular, one obtains a contrafunctor on $\operatorname{Homtop}(E,E')$:

```text
u |-> u^* : Homtop(E, E')^circ -> Hom(E', E).
```

In accordance with the geometric intuition according to which the direct image functor $u_*$ "goes in the same
direction" as the continuous map giving rise to it, one should therefore define the direction of arrows for morphisms
between morphisms of topoi in terms of direct image functors, and not in terms of inverse image functors (although it is
the latter which, as we have seen, possess the exactness properties characteristic of the notion of morphism of topoi).

[PDF p. 343]

**3.2.2.** Having defined the category $\operatorname{Homtop}(E,E')$ of morphisms from the topos $E$ to the topos $E'$,
the notion of isomorphism between two morphisms $u$, $v$ from $E$ to $E'$ is also defined. In practice, there is no need
to distinguish essentially between two isomorphic morphisms of topoi, at least when one has a canonical isomorphism
between the two (just as there is often no need to distinguish between two elements of a category when one is given a
canonical isomorphism between them).

Let us point out in this connection that most often, when one treats diagrams of morphisms of topoi and questions of
commutativity of such diagrams (a notion which makes sense thanks to (3.3.)), what is meant is only commutativity up to
("canonical") isomorphism; by abuse of language, one then treats these diagrams as actually commutative diagrams.

One might think of justifying this abuse of language by introducing the set
$\operatorname{Homtop}(E,E')/\operatorname{Isom}$ of morphisms from $E$ to $E'$ up to isomorphism, and calling such an
isomorphism class a morphism, instead of following Definition 3.2. But this runs into the very serious drawbacks that
arise every time one tries to identify two isomorphic objects of a category without having a canonical isomorphism
between them. Experience proves that such a point of view is impracticable, and that one must keep the "fine" notion 3.1
and the notion of morphism between morphisms of topoi, even if one is sometimes forced to fight with compatibilities
among canonical isomorphisms (*).

(*) For examples of such battles (victorious, it seems), we refer the reader to Mme M. Hakim's book on relative schemes
[9].

[PDF p. 344]

**3.3.1.** Let $E$, $E'$, $E''$ be three $U$-topoi, and consider morphisms of topoi

```text
u : E -> E',      v : E' -> E''.
```

The theory of adjoint functors then gives us an adjunction isomorphism between the composite functors $v_*u_*$ and
$u^*v^*$, in terms of the adjunction isomorphisms for the pairs $(u_*,u^*)$ and $(v_*,v^*)$. On the other hand, the
functor $u^*v^*$ is left exact, as a composite of two left exact functors. Consequently, one obtains a morphism from $E$
to $E''$, called the composite of the morphisms $u$ and $v$, and denoted $vu$:

```text
vu : E -> E''.
```

One then verifies trivially that composition of morphisms is associative, and that for every $U$-topos $E$ there is a
morphism from $E$ to itself which is a two-sided unit for composition: it is the morphism
$(\operatorname{id}_E,\operatorname{id}_E,\varphi)$, where $\varphi$ is the evident adjunction isomorphism of
$\operatorname{id}_E$ with itself. Let $V$ be a universe such that $U\in V$. One defines a category

```text
(V-U-Top),
```

whose objects are the $U$-topoi which are $\in V$, whose arrows are the morphisms between such $U$-topoi, and whose
composition of arrows is the one just made explicit.

**3.3.2.** In fact, the composition map

```text
Homtop(E, E') x Homtop(E', E'') -> Homtop(E, E'')
```

is the map induced on objects by a "composition of morphisms" functor:

[PDF p. 345]

```text
Homtop(E, E') x Homtop(E', E'') -> Homtop(E, E''),
```

whose effect on arrows is the usual "convolution product" operation for morphisms between functors (here direct image
functors). These composition functors satisfy a (strict) associativity property, for four topoi $E$, $E'$, $E''$,
$E'''$, making precise the associativity of composition of morphisms of topoi. One may also say, in language that is
beginning to become familiar [2] [9], that the $U$-topoi are the objects (or $0$-arrows) of a 2-category, whose
$1$-arrows are morphisms of topoi and whose $2$-arrows are morphisms of morphisms of topoi.

The fact that the $U$-topoi (elements of a universe $V$) form a 2-category, and no longer merely an ordinary category
like ordinary topological spaces, is from the technical point of view the most important difference between the theory
of topoi and that of topological spaces. This fact is the source of certain technical complications to which we have
already alluded, but also of facts essentially new in relation to traditional topology.

**3.4.** The fact that the $U$-topoi (elements of a universe $V$) form a 2-category (3.3.2) makes it possible in
particular to define the notion of equivalence of two $U$-topoi $E$, $E'$: we shall say that $E$ and $E'$ are equivalent
if there exist morphisms of topoi $u : E\to E'$ and $v : E'\to E$ such that the composites $uv$ and $vu$ are isomorphic,
respectively, to the identity morphism of $E$ and of $E'$; one then says that the morphisms $u$ and $v$ are

[PDF p. 346]

quasi-inverse equivalences of one another.

One immediately sees that for the morphism of topoi $u : E\to E'$ to be an equivalence, it is necessary and sufficient
that $u_*$ be an equivalence, or equivalently, that $u^*$ be an equivalence. (Use the fact that a functor $f : E\to E'$
between two topoi which is an equivalence is both of the form $u_*$ and of the form $v^*$, with $u$ and $v$ morphisms of
topoi); and for $E$ and $E'$ to be equivalent in the sense of the preceding paragraph, it is necessary and sufficient
that they be equivalent as categories (i.e. as objects of the 2-category $(V\text{-}\mathrm{Cat})$). As expected, this
shows that the notions of equivalence introduced do not depend on the choice of the universe $V$ in 3.3.1.

**3.4.1.** In practice, there is usually no need to distinguish essentially between equivalent $U$-topoi, just as there
is often no need to distinguish essentially between two equivalent categories, provided however that one has an explicit
equivalence from one to the other, or at least an equivalence defined up to unique isomorphism. It is the notion of
equivalence of topoi which replaces here the traditional notion of homeomorphism between two topological spaces. See
Example 4.2 below for the precise relations between these two notions.

## 4. Examples of Morphisms of Topoi

We return here to the examples of 2, using the notion of morphism of topoi. The comments of 2.0 apply equally to the
present number. The universe $U$ will generally be understood.

[PDF p. 347]

### 4.1. The Topos $\operatorname{Top}(X)$ for a Variable Topological Space $X$

**4.1.1.** Let

```text
f : X -> Y
```

be a continuous map of topological spaces. We shall associate to it canonically a morphism of topoi

```text
Top(f) or f : Top(X) -> Top(Y),
```

with the notation of 2.1. When one defines $\operatorname{Top}(X)$ as $\operatorname{Ouv}(X)^\sim$, the most convenient
description of $\operatorname{Top}(f)$ is by the direct image functor of sheaves

```text
f_* : Top(X) -> Top(Y),
```

defined by the formula

```text
f_*(F) = F circ f^{-1},
```

where

```text
f^{-1} : Ouv(Y) -> Ouv(X)
```

is the evident functor $U\mapsto f^{-1}(U)$. We already noted that this functor is continuous and left exact, hence
indeed defines a functor $f_*$ above, admitting a right adjoint $f^*$ which is left exact (III 1.9.1). Of course, in all
strictness, the morphism of topoi $\operatorname{Top}(f)$ depends on the choice of the right adjoint $f^*$ of $f_*$, and
is therefore defined only up to canonical isomorphism. We shall henceforth dispense with explicitly mentioning phenomena
of this kind.

When one adopts the point of view of "etale spaces" to define $\operatorname{Top}(X)$, it is the inverse image functor

```text
f^* : Top(Y) -> Top(X)
```

[PDF p. 348]

which is the most convenient one for defining the morphism of topoi $\operatorname{Top}(f)$, by simply setting

```text
f^*(Y') = X x_Y Y'
```

for every etale space $Y'$ over $Y$; it is evident that the fiber product is indeed an etale space over $X$, and that
the functor $f^*$ thus obtained is left exact and commutes with arbitrary $\varinjlim$, and consequently defines a
morphism of topoi $\operatorname{Top}(f)$. For the compatibility of the two definitions obtained, we refer to [TF].

When one has two composable continuous maps

```text
X --f--> Y --g--> Z,
```

one finds a canonical isomorphism

```text
Top(gf) ~= Top(g) Top(f)
```

of morphisms of topoi. These transitivity isomorphisms, for three composable continuous maps $f$, $g$, $h$, satisfy a
compatibility relation which we shall not write here, and which is precisely the one considered in SGA 1 VI 7.4 B) (for
$C=(\mathrm{Esp})^\circ$). This may be expressed by saying that, for variable $X$ in the category $(\mathrm{Esp})$,

```text
X |-> Top(X)
```

is a "pseudo-functor"

```text
(4.1.1.1)    (U-esp) -> (V-U-top) ;
```

or also, in the terminology of 2-categories, that one has a non-strict functor of 2-categories [9]. In practice, we
shall most often allow ourselves the abuse of language consisting in identifying $\operatorname{Top}(gf)$ and
$\operatorname{Top}(g)\operatorname{Top}(f)$, i.e. in reasoning as if (4.1.1.1) were a true functor of

[PDF p. 349]

ordinary categories. We shall allow ourselves analogous abuses of language in the other examples treated below.

**4.1.2.** The preceding considerations extend immediately to the case of topoi associated to topological spaces with
groups of operators (2.3). If $f=(f^{\mathrm{es}},f^{\mathrm{gr}})$,

```text
f : (X, G) -> (Y, H)
```

is a morphism of spaces with operators (where

```text
f^{es} : X -> Y      and      f^{gr} : G -> H
```

are respectively continuous maps and group morphisms, compatible in the evident sense), one associates to it a morphism
of topoi

```text
Top(f) or f : Top(X, G) -> Top(Y, H),
```

whose definition is left to the reader. When the groups $G$ and $H$ are the unit groups, one recovers the definition of
4.1.1; when, on the other hand, it is the spaces $X$ and $Y$ which are reduced to a point, one finds as inverse image
functor $f^*$ the functor "restriction of the group of operators"

```text
f^* : B_H -> B_G,
```

associating to every $H$-set the $G$-set it defines by means of $f : G\to H$. We shall encounter this example again in
other forms in 4.5 and 4.6.1.

**4.1.3.** Given a continuous map $f : X\to Y$ of topological spaces, one also associates to it a morphism on the
corresponding "big topoi" (2.5)

[PDF p. 350]

```text
TOP(f) or f : TOP(X) -> TOP(Y),
```

defined most conveniently by the inverse image functor

```text
f^* : TOP(Y) -> TOP(X),
```

which is none other than the restriction functor. This morphism $\operatorname{TOP}(f)$ is a particular case of the
so-called "inclusion" morphism for an induced topos, which will be studied in 5. Thus one sees that, subject to the same
reservations as in 4.1.1, the topos $\operatorname{TOP}(X)$ may be regarded as a functor in $X$, for $X$ variable in
$(\mathrm{Esp})$.

### 4.2. Faithfulness Properties of $X\mapsto\operatorname{Top}(X)$

We propose to make precise to what extent a topological space $X$ can be reconstructed in terms of the topos
$\operatorname{Top}(X)$, and for this purpose it is appropriate to describe, for two spaces $X$ and $Y$, the category of
morphisms from $\operatorname{Top}(X)$ to $\operatorname{Top}(Y)$ (3.2), in order to make precise the faithfulness
properties of the "functor" $X\mapsto\operatorname{Top}(X)$. We restrict ourselves to stating the results one obtains,
referring the reader to [9] for details. The reader who wants to carry out the verification exercise himself may consult
Exerc. 7.8.

**4.2.1.** Recall that a topological space $X$ is called sober if every irreducible closed subset of $X$ has exactly one
generic point. Let us point out that almost all spaces used in practice are sober; this holds in particular for a
separated space, more generally for a space all of whose points are closed, or for the underlying space of a scheme. If
$X$ is a topological space, one associates to it (loc. cit. or EGA $0_{\mathrm{I}}$, re-edition) a sober topological
space $X_{\mathrm{sob}}$ and a continuous map

[PDF p. 351]

```text
(4.2.1.1)    phi : X -> X_sob
```

which is universal for continuous maps from $X$ to sober spaces; in other words, one constructs a left adjoint functor
$X\mapsto X_{\mathrm{sob}}$ to the inclusion functor $(\mathrm{Esp}_{\mathrm{sob}})\to(\mathrm{Esp})$ from the category
of sober spaces into that of "arbitrary" topological spaces (the quotation marks recalling that there is a universe!).
The explicit construction is made by taking as points of $X_{\mathrm{sob}}$ the irreducible closed subsets of $X$, and
as open sets the sets of the form $U'$, where $U$ is an open subset of $X$ and $U'\subset X_{\mathrm{sob}}$ denotes the
set of irreducible closed subsets of $X$ which meet $U$. The map (4.2.1.1) is obtained by associating to every $x\in X$
the closure of $\{x\}$. The space $X$ is sober if and only if the preceding map is bijective, hence a homeomorphism.

One observes that the functor

```text
phi^{-1} : Ouv(X_sob) -> Ouv(X)
```

induced by $\varphi$ is an isomorphism, which implies that the morphism of topoi

```text
Top(phi) : Top(X) -> Top(X_sob)
```

defined by $\varphi$ is also an isomorphism. This explains a priori why $X_{\mathrm{sob}}$ must necessarily enter the
question of reconstructing $X$ from $\operatorname{Top}(X)$: since the latter depends only on $X_{\mathrm{sob}}$ up to
isomorphism, the question can have an affirmative answer only if $X$ is sober. We shall make precise below (7.1) how
$X_{\mathrm{sob}}$ can effectively

[PDF p. 352]

be reconstructed in terms of $\operatorname{Top}(X)$, by interpreting its points as "points" of the topos
$\operatorname{Top}(X)$ (or again as fiber functors).

**4.2.2.** On every topological space one should introduce the order relation $\leq$ for which

```text
x <= y  <=>  closure({x}) subset closure({y}),    i.e. x in closure({y})
```

(which is also expressed by saying that $x$ is a specialization of $y$, or that $y$ is a generalization of $x$). For a
space of the form $X_{\mathrm{sob}}$, this is simply the inclusion relation between irreducible closed subsets of $X$.

This being said, one should introduce on the set of maps from a space $X$ to another space $Y$ the order relation called
"specialization", deduced from that of $Y$, namely

```text
f <= g  <=>  f(x) <= g(x) for every x in X.
```

With these conventions, one has the following result:

**4.2.3.** Let $X$, $Y$ be two topological spaces, with $Y$ sober, and let $f$ and $g$ be two continuous maps from $X$
to $Y$. Then there is at most one morphism from $\operatorname{Top}(f)$ to $\operatorname{Top}(g)$, and for there to be
one, it is necessary and sufficient that $g$ be a specialization of $f$. Finally, every morphism of topoi
$\operatorname{Top}(X)\to\operatorname{Top}(Y)$ is isomorphic to a morphism of the form $\operatorname{Top}(f)$, where
$f : X\to Y$ is a continuous map (uniquely determined by the first assertion).

[PDF p. 353]

If one defines the category $\operatorname{cat}(I)$ associated to an ordered set $I$ by declaring that for $i\geq j$
there is exactly one arrow from $i$ to $j$, the preceding result may be summarized by saying that there is a canonical
equivalence of categories

```text
cat(Hom_{(Esp)}(X, Y)) ~= Homtop(Top(X), Top(Y))
```

(where the second member is defined in 3.2).

These results formally imply:

**Corollary 4.2.4.**

1. Let $f : X\to Y$ be a continuous map. Then $\operatorname{Top}(f) : \operatorname{Top}(X)\to\operatorname{Top}(Y)$ is
   an equivalence of topoi if and only if $f_{\mathrm{sob}} : X_{\mathrm{sob}}\to Y_{\mathrm{sob}}$ is a homeomorphism
   (hence, when $X$ and $Y$ are sober, if and only if $f$ is a homeomorphism).
2. Let $X$ and $Y$ be topological spaces. For $\operatorname{Top}(X)$ and $\operatorname{Top}(Y)$ to be equivalent, it
   is necessary and sufficient that $X_{\mathrm{sob}}$ and $Y_{\mathrm{sob}}$ be homeomorphic (hence, if $X$ and $Y$ are
   sober, it is necessary and sufficient that $X$ and $Y$ be homeomorphic).

### 4.3. Morphisms into the Final Topos: Constant Objects of a Topos, Section Functors

Denote by $P$ (initial of "point") the standard final topos, i.e. $P=(\mathrm{Ens})$ (2.2). Let $E$ be any topos; we
shall see that, up to unique isomorphism, there exists a unique morphism of topoi

```text
f : E -> P.
```

More precisely, the category $\operatorname{Homtop}(E,P)$ is equivalent to the punctual category: for two objects of
this category, there therefore exists

[PDF p. 354]

a unique arrow from one to the other, and it is an isomorphism. This justifies to some extent the name "final topos".

For this, recall (3.2.1) that $\operatorname{Homtop}(E,P)$ is equivalent to the full subcategory of
$\operatorname{Hom}(P,E)^\circ$ formed by the functors

```text
f* : P = (Ens) -> E
```

which commute with inductive limits and are left exact. Let $e$ be a one-point set; then every set $X$ is written
canonically as the "sum of $X$ copies of $e$", whence it follows that the category of functors $g : (\mathrm{Ens})\to E$
which commute with inductive limits is equivalent to the category $E$, by associating to every $g$ the object $g(e)$ of
$E$. One reconstructs $g$ in terms of $T=g(e)$, up to unique isomorphism, by $g(I)=T\times I$, where one sets

```text
T x I = coproduct_{i in I} T_i,    with T_i = T for every i in I.
```

That the functor in $I$ thus defined by $T$ indeed commutes with inductive limits follows from the fact that it is
manifestly right adjoint to the functor $X\mapsto\operatorname{Hom}(T,X)$ from $E$ to $(\mathrm{Ens})$. This being said,
for $g$ to be left exact, it is evidently necessary that $g(e)=T$ be a final object of $E$ (since $e$ is a final object
of $(\mathrm{Ens})$), and it follows easily from the fact that in $E$ "sums are universal" (1.1.2 b)) that this
condition is also sufficient. Thus one finds that the category of inverse image functors $f^*$ is equivalent to the
category of final objects of $E$, which is obviously itself equivalent to the final category.

From what precedes, one sees that the choice of a morphism (4.3.1) is essentially equivalent to that of a final object
of $E$, say $e_E$. In terms of this, one then has canonical isomorphisms of functors

[PDF p. 355]

```text
(4.3.2)    f*(I) ~= e_E x I = sum of I copies of e_E,    for I in ob(Ens),
```

and

```text
(4.3.3)    f_*(X) = Hom(e_E, X)                           for X in Ob E.
```

**4.3.4.** The two preceding functors will play an important role later. For a set $I$, the object $f^*(I)=e_E\times I$
of (4.3.2) is called the constant object of value $I$ in $E$ (or, when $E$ is realized as a category $\widetilde{C}$ in
terms of a site $C$, the constant sheaf of value $I$ on $C$). It will also often be denoted $I_E$, or $I_C$ when $E$ is
defined by the site $C$.

The fact that $I\mapsto I_E$ is the inverse image functor of a morphism of topoi makes precise its exactness properties,
which imply in particular that this functor respects all the usual species of algebraic structures, transforming a group
into a group object of $E$, etc. (3.1.2). When, for example, one has a group $G$ of $E$, one says that it is a constant
group (or, if appropriate, a constant sheaf of groups) if it is isomorphic to a group of the form $G_{0E}$, where $G_0$
is an ordinary group. The same terminology applies for every other "algebraic" species of structure, in the sense made
precise (more or less) in 3.1.2.

**4.3.5.** One should be careful that the functor $I\mapsto I_E$ is not necessarily fully faithful (nor even faithful:
take for $E$ the "empty topos" (2.2)), so a constant object of $E$ does not in general determine, up to unique
isomorphism, the set $I$ which gives rise to it. One says that $E$ is $0$-acyclic, or connected-nonempty, if the functor
$I\mapsto I_E$ is fully faithful. By the general properties of adjoint functors, this is equivalent to saying that the
adjunction morphism

[PDF p. 356]

```text
I -> f_*(f*(I)) = f_*(I_E) = Hom(e_E, I_E)
```

is an isomorphism (so that the functor (4.3.3) makes it possible to recover the "value" of a constant object of $E$).
One verifies easily that for this it is necessary and sufficient that $e_E$ not be the initial object $\emptyset_E$ of
$E$, i.e. that $E$ not be an "empty topos" (which expresses the faithfulness of the functor $I\mapsto I_E$ (*)), and
that $e_E$ be a connected object of $E$, i.e. not be the sum of two objects of $E$ which are not "empty" (i.e. which are
not initial objects of $E$).

**4.3.6.** The functor (4.3.3) is also often called the sections functor and denoted $\Gamma_E$, or $\Gamma(E,-)$, or
simply $\Gamma$:

```text
(4.3.6.1)    Hom(e_E, X) = Gamma_E(X) = Gamma(E, X) = Gamma(X).
```

It is a functor commuting with arbitrary projective limits, but not right exact in general; its derived functors (on
abelian group objects) will be studied in the next expose.

(*) Or also the fact that this functor is conservative (I 6.3).

### 4.4. Morphisms from the "Empty Topos"

Let $\emptyset_{\mathrm{top}}$ be an empty topos, which therefore corresponds to a category of sheaves $\Phi$ equivalent
to the final category (2.2). Let $E$ be a topos. The category of functors from $E$ to $\Phi$ is evidently equivalent to
the punctual category, and every such functor commutes with inductive and projective limits (with no merit, moreover),
so can be regarded as an inverse image functor $f^*$ for a morphism of topoi $\emptyset_{\mathrm{top}}\to E$. It follows
that the category $\operatorname{Homtop}(\emptyset_{\mathrm{top}},E)$ is equivalent to the punctual category, and in
particular that, up to

[PDF p. 357]

unique isomorphism, there exists one and only one morphism of topoi

```text
(4.4.1)    empty_top -> E.
```

This justifies to some extent the terminology "initial topos" introduced in 2.2.

One can also determine the morphisms of topoi

```text
(4.4.2)    E -> empty_top ;
```

one immediately verifies that such a morphism exists if and only if the initial object of $E$ is also a final object,
i.e. if and only if $E$ itself is an "empty topos", and that in this case the category
$\operatorname{Homtop}(E,\emptyset_{\mathrm{top}})$ is again equivalent to the punctual category. The unique morphism
(4.4.2) (modulo isomorphism) is then an equivalence of topoi.

### 4.5. The Classifying Topos $B_G$ for Variable Group $G$

**4.5.1.** Let $E$ be a topos, and let

```text
f : G -> H
```

be a morphism of groups in $E$. One deduces from it the functor "restriction of the group of operators"

```text
f* : B_H -> B_G,
```

where the notation is that of 2.4. It is trivial that this functor commutes with inductive limits and projective limits;
a fortiori it can be interpreted as an inverse image functor associated to a morphism of topoi

```text
B_f, or f : B_G -> B_H.
```

[PDF p. 358]

One easily makes explicit the corresponding direct image functor

```text
f_* : B_G -> B_H
```

by the formula

```text
f_*(X) = Hom_G(H_s, X),
```

where $X$ is an object of $E$ with $G$ acting on the left, where $H_s$ is $H$ regarded as equipped with the left actions
by $G$ deduced from $f$, and where $\operatorname{Hom}_G$ denotes the expected subobject of the object
$\operatorname{Hom}$ defined below (10.); one makes $H$ act on the left on $\operatorname{Hom}_G(H_s,X)$ by means of the
right actions of $H$ on $H_s$, by right translations.

Since the inverse image functor $f^*$ commutes with arbitrary limits (and not only with finite limits), it is itself the
left adjoint of a functor

```text
f_! : B_G -> B_H,
```

so that one has a sequence of three adjoint functors as in 3.1.3:

```text
f_!,  f*,  f_*.
```

One easily makes $f_!$ explicit by the formula

```text
f_!(X) = H x^G X,
```

where the second member denotes the "contracted product", deduced from the actions of $G$ on $X$ (on the left) and on
$H$ (on the right via right translations and $f$), defined as the quotient of $H\times X$ by $G$ acting by the formula

```text
g . (h, x) = (h g^{-1}, gx).
```

The functor $f_!$, being a left adjoint, evidently commutes with inductive limits, but it is not in general left exact
(i.e.

[PDF p. 359]

it cannot in turn be regarded as an inverse image functor by a morphism of topoi $B_H\to B_G$). In fact, one verifies
easily that it can be left exact only if $f : G\to H$ is an isomorphism. Similarly, the functor $f_*$, which commutes
with projective limits, is not in general right exact, and a fortiori does not in general admit a right adjoint. At
least when $E$ is the punctual topos, i.e. when $G$ and $H$ are ordinary groups, $f_*$ is right exact only if $f$ is an
isomorphism.

When one has a second morphism of groups $g : H\to K$, one finds, as in 4.1.1, a transitivity up to canonical
isomorphism, so that, subject to the usual reservation, one may regard the classifying topos $B_G$ as depending
functorially on the group $G$. We leave to the reader the task of generalizing this functorial behavior to the case
where $G$ and the topos $E$ are varied simultaneously.

**4.5.2. The topos $B_G$ for a variable pro-group $G$.**

We leave to the reader the task of making precise the covariant character of the topos $B_G$ (2.7) with respect to $G$,
by modeling the exposition we gave in 4.5.1. One should be careful, however, that in the case of a morphism $f : G\to H$
of pro-groups which are not essentially constant, the corresponding morphism of topoi $B_G\to B_H$ does not in general
allow the definition of a functor $f_!$ (whose right adjoint would be the functor $f^*$ of restriction of the pro-group
of operators). Supposing, to simplify the statement, that $G$ and $H$ are defined by profinite groups $G$ and $H$, one
sees easily that $f_!$ exists if and only if the image of the morphism under consideration $f : G\to H$ has finite index
in $H$, and

[PDF p. 360]

in this case $f_!$ is given by the same formula as in 4.5.

### 4.6. The Topos $\widehat{C}$ for Variable Category $C$

**4.6.1.** Let

```text
f : C -> C'
```

be a functor from a category $C\in U$ to another $C'$, giving a functor

```text
f* : C'^ -> C^,    f*(F) = F circ f.
```

It is trivial that this functor commutes with projective limits and inductive limits; a fortiori it can be regarded as
the inverse image functor for a morphism of topoi

```text
f^ or f : C^ -> C'^.
```

The corresponding direct image functor

```text
f_* : C^ -> C'^
```

is none other than the functor also denoted $f_*$ in I 5.1. Moreover (as was to be expected from the fact that $f^*$
also commutes with arbitrary limits), $f^*$ also admits a left adjoint

```text
f_! : C^ -> C'^,
```

(which was also denoted $f_!$ in I 5.1). One thus obtains a sequence of three adjoint functors

```text
f_!,  f*,  f_*,
```

the first moreover being an extension of $f : C\to C'$ to the categories of presheaves (for the usual embedding of $C$,
$C'$ in the categories $\widehat{C}$, $\widehat{C}'$). One should be careful that the functor $f_!$ is not in general
left exact, nor $f_*$ right exact, which therefore removes any ambiguity about the

[PDF p. 361]

direction of variance of the topos $\widehat{C}$ associated to the variable category $C$: this topos is a covariant
functor in $C$, subject to the usual reservation coming from transitivity isomorphisms (cf. 4.1.1). When the sets of
objects of $C$ and $C'$ are reduced to one element, so that $C$ and $C'$ are identified with monoids $G$, $G'$, the
corresponding topoi are the classifying topoi $B_{G^\circ}$ and $B_{G'^\circ}$, and one recovers the variance of these
for variable $G$ already encountered from other points of view in 4.1.2 and 4.5 (where the restriction to groups rather
than monoids was not essential).

**4.6.2.** One can make precise the 2-functorial dependence of the topos $\widehat{C}$ with respect to $C$, by
introducing for two categories $C$, $C'\in U$ a canonical functor

```text
(4.6.2.1)    Hom(C, C') -> Homtop(C^, C'^).
```

It remains to define this functor on arrows, and for this one notes that $f\mapsto f^*$ makes it possible to identify
(up to equivalence of categories) the second member with a full subcategory of
$\operatorname{Hom}(\widehat{C}',\widehat{C})^\circ$ (3.2.1). Now, if $f,g : C\to C'$ are two functors, every morphism
$u : f\to g$ of functors defines a morphism $F\circ g\to F\circ f$ of functors in $F\in\operatorname{ob}\widehat{C}'$
($F$ being a contrafunctor), hence a morphism $g^*\to f^*$, and consequently defines a morphism
$\widehat{f}\to\widehat{g}$ as

announced.

When $C$ is the punctual category, $\widehat{C}$ is the punctual topos (2.2), denoted $P$, and (4.6.2.1) is interpreted
as a natural functor

```text
(4.6.2.2)    C' -> Homtop(P, C'^) = Points(C'^)
```

from $C'$ to the "category of points" of $\widehat{C}'$, which will be studied in 6.

[PDF p. 362]

This functor is not necessarily an equivalence of categories (7.3.3); a fortiori (4.6.2.1) is not necessarily an
equivalence of categories. On the other hand, the functor (4.6.2.1) is always fully faithful.

To see this, note that if $f,g : E\to E'$ are two morphisms of topoi such that $f_!$ and $g_!$ are defined (3.1.3), it
follows from the theory of adjoint functors that one has canonical isomorphisms

```text
Hom(f_!, g_!) ~= Hom(g*, f*) ~= Hom(f_*, g_*)  def= Hom(f, g).
```

Applying this to functors of the form $\widehat{f}$, $\widehat{g}$ associated to $f,g : C\to C'$, one finds the
announced result, taking into account that the natural extension map

```text
Hom(f, g) -> Hom(f_!, g_!)
```

is bijective (I 7.8).

**4.6.3.** One may ask when the functor (4.6.2.1) is an equivalence of categories, i.e. when it is essentially
surjective, which is a particular case of the question of determining all morphisms of topoi
$\widehat{C}\to\widehat{C}'$. More generally, if $C$ is a category $\in U$ and $E$ a topos, one may seek to determine
the morphisms of topoi

```text
f : C^ -> E.
```

The category of these morphisms is equivalent to the opposite category of that of functors

```text
f* : E -> C^
```

commuting with arbitrary inductive limits and finite projective limits. Interpreting functors $E\to\widehat{C}$ as
functors $E\times C^\circ\to(U\text{-}\mathrm{Ens})=(\mathrm{Ens})$, or again as functors
$F : C^\circ\to\operatorname{Hom}(E,(\mathrm{Ens}))$, the exactness property under consideration is expressed by the
condition that for every object $X$ of $C$, the functor $F(X) : E\to(\mathrm{Ens})$ commute with arbitrary inductive
limits and finite projective limits (or, as we shall say in 6, that $F(X)$ is a

[PDF p. 363]

"fiber functor" on $E$). This is equivalent to saying that $F(X)$ is the inverse image functor for a morphism of topoi
$P\to E$, so that one finally obtains a canonical equivalence of categories

```text
(4.6.3.1)    Homtop(C^, E) ~= Hom(C, Points(E)),
```

where, for short, we denote by

```text
Points(E) = Homtop(P, E)
```

the category of points of the topos $E$.

When $E$ is of the form $\widehat{C}'$, one sees immediately from the definitions that the composite of (4.6.2.1) and
the preceding equivalence (4.6.3.1) is the functor

```text
(4.6.3.2)    Hom(C, C') -> Hom(C, Points(C'^))
```

defined by $F\mapsto i\circ F$, where $i : C'\to\operatorname{Points}(\widehat{C}')$ is the canonical embedding
(4.6.2.2). It follows immediately that for (4.6.2.1) to be an equivalence, it is necessary and sufficient that $C$ be
empty or that (4.6.2.2) be essentially surjective (hence an equivalence of categories). This last condition on $C'$ is
satisfied in certain interesting cases, notably when $C'$ is the category with one object defined by a group $G$
(7.2.5).

**Remark 4.6.4.** The fact of having associated a topos $\widehat{C}$ to an arbitrary category $C$ suggests that a
category $C$ admits invariants of topological nature (cohomology groups, homotopy groups, etc.), just like a topos. The
cohomology groups of $\widehat{C}$ with coefficients in an abelian group object $F$ (in the general sense studied in V)
are none other than the values of the derived functors $\varprojlim^n$ of the functor $\varprojlim$, already familiar to
topologists.

[PDF p. 364]

J. L. Verdier and (independently) D. G. Quillen have verified that when one restricts to constant coefficients, or more
generally locally constant coefficients, these cohomology groups are identified with the cohomology groups of the
semisimplicial set $\operatorname{Nerf}(C)$ canonically associated to $C$ (ref. [5], No. 212, Prop. 4.1), and that
moreover, up to isomorphism in the "homotopy category" of [2], every semisimplicial set can be obtained by means of a
category $C$.

By means of a suitable notion of homotopy type for topoi, which we do not make precise here, one can say that the
semisimplicial homotopy types of topologists are none other than the homotopy types of topoi of the special form
$\widehat{C}$, more generally of topoi $E$ in which every object admits a covering refining all others (2.6) (*). In the
absence of this condition on $E$, one can at best express its homotopy type by a suitable projective system of
semisimplicial sets [1].

(*) And, more generally still, of topoi which are "locally $\infty$-connected", in an evident sense which we leave to
the reader to make precise.

### 4.7. The Topos $\widetilde{C}$ for a Variable Site $C$ (Cocontinuous Functors)

Let

```text
f : C -> C'
```

be a cocontinuous functor (III 2.1) between sites $\in U$, i.e. a functor such that the functor $f_*$, or
$\widehat{f}_* : F\mapsto F\circ f$, from $\widehat{C}$ to $\widehat{C}'$ (4.6.1), carries $\widetilde{C}$ into
$\widetilde{C}'$, that is, induces a functor

```text
(4.7.1)    f~_* : C~ -> C'~
```

making the diagram of functors

[PDF p. 365]

```text
(4.7.2)
        f~_*
  C~ --------> C'~
  |            |
i |            | i'
  v            v
  C^ ---------> C'^
        f^_*
```

commutative, where $i$, $i'$ are the inclusion functors. We then saw (III 2.3) that the functor $\widetilde{f}_*$ admits
a left adjoint $\widetilde{f}^*$, and that the latter is left exact. In other words, $\widetilde{f}_*$ is the direct
image functor associated to a morphism of topoi

```text
f~ or f : C~ -> C'~,
```

the corresponding inverse image functor being of course $\widetilde{f}^*$. Taking left adjoints of the functors in
question, the commutative diagram (4.7.2) moreover gives a diagram commutative up to isomorphism

```text
(4.7.3)
        f~*
  C~ <-------- C'~
  ^            ^
a |            | a'
  |            |
  C^ <--------- C'^
        f^*
```

where $a$ and $a'$ are the "associated sheaf" functors, a diagram which immediately recovers the formula (III 2.3)

```text
f~* = a f^* i'.
```

The transitivity property for the morphisms of topoi $\widehat{f} : \widehat{C}\to\widehat{C}'$ implies the same
property for the morphisms of topoi $\widetilde{f} : \widetilde{C}\to\widetilde{C}'$ associated to cocontinuous
functors, so that one can say that the topos $\widetilde{C}$ varies functorially in $C$, covariantly, when one takes
cocontinuous functors as "morphisms" of sites.

[PDF p. 366]

In all cases encountered up to now, the cocontinuous functor $f$ used is also continuous, i.e. (III 1.1) "extends" to a
functor

```text
f~_! : C~ -> C'~
```

commuting with inductive limits, and which is left adjoint to $\widetilde{f}^*$, so that one has a sequence of three
adjoint functors

```text
f~_!,  f~*,  f~_*.
```

One should be careful that the functor $\widetilde{f}_!$ is not in general left exact, nor $\widetilde{f}_*$ right
exact, which removes any ambiguity about the direction of variance of the topos $\widetilde{C}$, for $C$ variable by
functors which are supposed only to be cocontinuous, or even continuous and cocontinuous.

**Remark 4.7.4.** Given a morphism of topoi

```text
F : E -> E',
```

for there to exist a functor $F_!$, left adjoint to $F^*$, it is necessary and sufficient that one be able to "realize"
(up to equivalence) $E$ and $E'$ in the form $\widetilde{C}$ and $\widetilde{C}'$, for two sites $C$, $C'\in U$, and be
able to find a continuous and cocontinuous functor $f : C\to C'$ such that $F$ is identified with $\widetilde{f}$. This
is evidently sufficient, and for necessity it suffices to take for $C$ and $C'$ small full generating subcategories of
$E$ and $E'$ respectively, such that

```text
F_!(ob C) subset ob C',
```

endowed with the topologies induced by those of $E$ and $E'$, and to take for $f$ the functor induced by $F_!$ (cf.
1.2.1). Recall (1.8) that the existence of $F_!$ also means that $F^*$ commutes with projective limits,

[PDF p. 367]

or, what is the same here since this functor is left exact, that it commutes with products.

**4.7.5.** If one asks which morphisms of topoi $F : E\to E'$ can be realized by a cocontinuous (not necessarily
continuous) functor of sites, one sees similarly that the answer is the following: the set of objects $X$ of $E$ such
that the functor

```text
X' |-> Hom(X, F*(X'))
```

from $E'$ to $(\mathrm{Ens})$ commutes with projective limits (or, equivalently, with products) must be a generating
family of $E$.

### 4.8. The Morphism of Topoi $\widetilde{C}\to\widehat{C}$ for a Site $C$

Let $C$ be a small site, to which are therefore associated the two topoi $\widetilde{C}$ and $\widehat{C}$ (the second
not depending on the topology put on $C$). In II 3.4 we defined the "associated sheaf" functor

```text
a : C^ -> C~
```

and established that it is left exact and commutes with inductive limits. It is therefore the inverse image functor
associated to a morphism of topoi

```text
p : C~ -> C^,    p* = a,
```

the corresponding direct image functor being the canonical inclusion

```text
i = p_* : C~ -> C^.
```

It is well known that this latter functor is not in general right exact (its derived functors on abelian objects give
rise to the cohomology presheaves $R^r i(F)$ of V 2), and that $a$ does not in general commute with arbitrary limits,
which removes any ambiguity about the direction of the "natural" morphism of topoi between $\widehat{C}$ and
$\widetilde{C}$.

When one has a cocontinuous functor

```text
f : C -> C'
```

[PDF p. 368]

of sites, one deduces a diagram of morphisms of topoi

```text
        f~
  C~ -------> C'~
  |           |
p |           | p'
  v           v
  C^ --------> C'^
        f^
```

which is commutative up to canonical isomorphism: this is indeed what is expressed by the commutativity of the diagram
of functors (4.7.2). Thus one can say that the morphism of topoi $p : \widetilde{C}\to\widehat{C}$ is functorial in $C$,
when $C$ is varied by cocontinuous functors between sites.

### 4.9. Effect of a Continuous Functor of Sites. Morphisms of Sites

**4.9.1.** If

```text
f : C -> C'
```

is a continuous functor from $C$ to $C'$, i.e. such that the functor

```text
f^* : C'^ -> C^
```

carries $\widetilde{C}'$ into $\widetilde{C}$, hence induces a functor

```text
f_s : C'~ -> C~,
```

we saw (III 1.2) that this latter admits a left adjoint

```text
f^s : C~ -> C'~,
```

which moreover "extends" $f$ in an evident sense. One should be careful that in general $f^s$ is not right exact (even
if $f$ is also cocontinuous), nor does $f_s$ commute with inductive limits, so that the datum of $f$ does not, without
further hypothesis, describe a morphism of topoi in either direction between $\widetilde{C}$ and $\widetilde{C}'$. The
case where $f$ is cocontinuous, i.e. where $f_s$ commutes with inductive limits and

[PDF p. 369]

can therefore be regarded as an inverse image functor for a morphism of topoi $\widetilde{f} : \widetilde{C}\to
\widetilde{C}'$, was examined in 4.7. We shall examine the case where the functor $f^s$ is left exact, and can therefore
be regarded as an inverse image functor for a morphism of topoi in the opposite direction:

```text
(4.9.1.1)    Top(f) = g : C'~ -> C~.
```

One should be careful that we have taken care not to denote this morphism by the letter $\widetilde{f}$ or $f$, to avoid
confusions with the situation of 4.7, in accordance with the general recommendations of 3.1.3. One sometimes says that
the functor $f : C\to C'$ is a morphism of sites from $C'$ to $C$ (attention, not from $C$ to $C'$) if it is continuous
and if the functor $f^s$ is left exact, in other words if there exists a morphism of topoi (4.9.1.1) such that the
corresponding inverse image functor

```text
g* : C~ -> C'~
```

extends the functor $f$, i.e. makes the diagram of functors

```text
        f
  C --------> C'
  |           |
eps |         | eps'
  v           v
  C~ -------> C'~
        g*
```

commute up to isomorphism, where $\varepsilon$, $\varepsilon'$ are the canonical functors of II 4.4.0.

**4.9.2.** In practice, one recognizes that a continuous functor $f : C\to C'$ is a morphism of sites from $C'$ to $C$,
by the fact that finite projective limits are representable in $C$, and that $f$ commutes with them (III 1.3.5).

[PDF p. 370]

Subject to the indicated condition on $C$ (almost always verified in practice), and supposing moreover that the topology
of $C'$ is less fine than the canonical topology (also almost always verified), the preceding sufficient condition ($f$
left exact) for $f$ to be a morphism of sites from $C'$ to $C$ is moreover also necessary.

**4.9.3.** In the spirit of what precedes, if $C$ and $C'$ are two $U$-sites, one should define the category of
morphisms of sites $\operatorname{Morsite}(C',C)$ from $C$ to $C'$ as the full subcategory of the opposite category
$\operatorname{Hom}(C,C')^\circ$ of the category of functors from $C$ to $C'$, formed by those functors which are
willing to be morphisms of sites (from $C'$ to $C$). In this way one obtains a canonical functor (defined up to unique
isomorphism)

```text
Morsite(C', C) -> Homtop(C'~, C~).
```

**Proposition 4.9.4.** Let $E$ be a $U$-topos and let $C$ be a $U$-site. Then the functor

```text
f |-> f*|_C = f* circ eps_C
```

associating to every morphism of topoi $f : E\to\widetilde{C}$ the "restriction" to $C$ of the associated inverse image
functor $f^* : \widetilde{C}\to E$, induces an equivalence of categories

```text
Homtop(E, C~) ~= Morsite(E, C) (subset Hom(C, E)^circ).
```

When finite limits are representable in $C$, the corresponding fully faithful functor

```text
Homtop(E, C~) -> Hom(C, E)^circ
```

has as essential image the set of functors $g : C\to E$ which are left exact and continuous, or equivalently left exact
and transform covering families into covering families.

[PDF p. 371]

The last assertion follows from the first by means of 4.9.2. On the other hand, one deduces from III 1.2 iv) and IV 1.2
iii) that the functor

```text
G |-> G circ eps
```

induces an equivalence between the category of continuous functors from $\widetilde{C}$ to $E$ and the category of
continuous functors from $C$ to $E$, a quasi-inverse functor being obtained by $g\mapsto g^s$ in the notation of loc.
cit. On the other hand, by the very definition, $g$ is a morphism of sites if and only if $g^s$ is the inverse image
functor associated to a morphism of topoi $E\to\widetilde{C}$, whence the conclusion by 3.2.1; the "or equivalently"
comes from III 1.6.

One should retain above all from 4.9.4 that (when finite limits are representable in $C$) "it amounts to the same thing"
to give a morphism of topoi $f : E\to\widetilde{C}$ or a functor $g : C\to E$ which is left exact and transforms
covering families into covering families.

**4.9.5.** Using the developments of 4.9.1 and 4.9.3, one sees as usual that for a variable $U$-site $C$, via the notion
of morphism of sites and of morphism of morphisms of sites just made explicit, the topos $\widetilde{C}$ depends
functorially (or more exactly, 2-functorially) on the site $C$. Note that thanks to the terminology introduced,
$\widetilde{C}$ depends covariantly on the site $C$.

**4.9.6.** It is immediate that (unlike what happens for the notion of cocontinuous functor, cf. 4.7.4) every morphism
of topoi $F : E\to E'$ can be realized by means of a morphism of sites $f : C\to C'$ (i.e. a continuous functor
$f : C'\to C$ such that...): it suffices to choose in $E$ and $E'$ small full generating subcategories

[PDF p. 372]

$C$ and $C'$ respectively, endowed with the topologies induced by those of $E$ and $E'$, such that one has

```text
F*(ob C') subset ob C,
```

and to take for $f$ the functor induced by $F^*$. This explains why most morphisms of topoi encountered in practice are
indeed described by means of morphisms of sites (rather than by means of cocontinuous functors as in 4.7).

### 4.10. Relations Between the Small and Big Topoi Associated to a Topological Space $X$

We return to the notation of 2.5. In particular, $V$ is a universe such that $U\in V$. We depart from the convention of
2.1, denoting by $\operatorname{Top}(X)$ the topos of $V$-sheaves (and not $U$-sheaves) on $X$. Thus we shall reason
with $V$-topoi and not $U$-topoi. (NB: it would be possible to keep the $U$-topoi, by adopting the appropriate
convention for the definition of $\operatorname{TOP}(X)$, so that the latter is a $U$-topos; cf. 2.5.)

This being said, we shall define two morphisms of topoi

```text
(4.10.1)    f : Top(X) -> TOP(X)
            g : TOP(X) -> Top(X),    g f ~= id_{Top(X)},
```

giving rise to a sequence of three adjoint functors

```text
(4.10.1.1)    g* = f_!,    g_* = f*,    g^! = f_*,
```

the notation being that of 3.1.3. We shall successively define

[PDF p. 373]

the first two functors of this sequence, the third then being defined as the right adjoint of the second.

**4.10.2.** The functor

```text
g_* = f* : TOP(X) -> Top(X)
```

is defined simply as the restriction functor from $(\mathrm{Esp})/X$ to the site $\operatorname{Ouv}(X)$ of open subsets
of $X$, which indeed transforms sheaves into sheaves, as follows immediately from the definition. Denoting sheaves on
the big site of $X$ by underlined letters, for such a sheaf $F$ we denote by $F_X$ its restriction to the site
$\operatorname{Ouv}(X)$, whence a functor

```text
(4.10.2.1)    Restr : F |-> F_X : TOP(X) -> Top(X).
```

It is evident that this functor commutes with $V$-projective limits, since these are computed argument by argument (one
could also invoke the existence of the left adjoint, constructed in 4.10.4 below). I claim that it also commutes with
$V$-inductive limits. To be convinced of this, we shall give a very convenient interpretation of "big" sheaves on $X$,
i.e. of objects of $\operatorname{TOP}(X)$, in terms of ordinary sheaves (NB: $V$-sheaves are meant) on topological
spaces $X'$ over $X$.

**4.10.3.** For a big sheaf $F$ on $X$, and for every space $X'$ over $X$ (understood: $X'\in U$), define in the evident
way, as in 4.10.2, the "small" sheaf $F_{X'}$, restriction of $F$ to $X'$. If

```text
u : X'' -> X'
```

[PDF p. 374]

is a morphism of $(\mathrm{Esp})/X$, one then defines in the evident way a morphism $u^*(F_{X'})\to F_{X''}$, or
equivalently, a "transition morphism"

```text
(4.10.3.1)    phi_u : u*(F_{X'}) -> F_{X''}.
```

These morphisms, for variable $u$, satisfy an evident transitivity condition for a composite

```text
X''' --v--> X'' --u--> X'
```

of morphisms in $(\mathrm{Esp})/X$, which we leave to the reader to make explicit. In this way one obtains a natural
functor from the category $\operatorname{TOP}(X)$ of big sheaves on $X$ to the category of systems

```text
(F_{X'})_{X' in ob (Esp)/X},    (phi_u)_{u in Fl (Esp)/X},
```

satisfying the transitivity condition under consideration, and such moreover that for every morphism $u : X''\to X'$
which is an open immersion (or, more generally, an etale space), the transition morphism $\varphi_u$ is an isomorphism.

Since the functors $u^* : \operatorname{Top}(X')\to\operatorname{Top}(X'')$ used for the description of the $\varphi_u$
commute with $V$-inductive limits, it follows immediately that, in the preceding description of objects of
$\operatorname{TOP}(X)$ in terms of "small" sheaves $F_{X'}$, $V$-inductive limits are computed argument by argument,
i.e. the functors of the form $F\mapsto F_{X'}$ commute with $V$-inductive limits.

In particular, this holds for the functor $F\mapsto F_X$ considered in 4.10.2. It therefore indeed admits a right
adjoint (1.5). It remains to construct a left adjoint for it (whose existence follows a priori from 1.8), and to verify
that the latter is left exact.

[PDF p. 375]

This will complete the definition of the announced morphisms of topoi (4.10.1) in terms of the functors (4.10.1.1).

**4.10.4.** The functor

```text
g* = f_! : Top(X) -> TOP(X)
```

is obtained by associating to every small sheaf $F$ on $X$ the system of its inverse images $(F_{X'})$,
$X'\in\operatorname{ob}(\mathrm{Esp})/X$, by the structural morphisms $X'\to X$, the transition morphism $\varphi_u$,
for $u : X''\to X'$, being the transitivity isomorphism for inverse images of sheaves (4.1.1). One immediately sees that
one thus obtains a functor

```text
Prol : Top(X) -> TOP(X)
```

which is fully faithful, and whose essential image is formed by the big sheaves $F$ on $X$ for which all the transition
morphisms $\varphi_u$ of 4.10.3 are isomorphisms. We leave to the reader the task of defining an adjunction isomorphism
between this canonical prolongation functor and the restriction functor of 4.10.2, proving that the latter is right
adjoint to the former. This is immediate in terms of the description 4.10.3 of the category $\operatorname{TOP}(X)$.

**Remarks 4.10.5.**

**a)** The construction 4.10.4 shows at the same time that $g^*=f_!$ is fully faithful (or, equivalently, that $g_*=f^*$
is a functor of passage to a category of fractions, or finally that $g^!=f_*$ is fully faithful). The big sheaves on $X$
which belong to the essential image of the functor $g^*=f_!=\operatorname{Prol}$ deserve the name of etale big sheaves
on $X$, since they form a category equivalent to that of ordinary sheaves on $X$, or again to that of etale spaces

[PDF p. 376]

over $X$. One also sees easily that if $X'$ is a topological space over $X$, then the big sheaf on $X$ represented by it
is etale in the preceding sense if and only if $X'$ is an etale space over $X$.

**b)** One may also express the full faithfulness of $f_!$ by saying that the adjunction morphism
$f^*f_!\to\operatorname{id}_{\operatorname{Top}(X)}$ is an isomorphism, i.e. that $g_*g^*\simeq\operatorname{id}$, i.e.
that $gf\simeq\operatorname{id}$. Thus $g$ makes $\operatorname{TOP}(X)$ a topos over $\operatorname{Top}(X)$, admitting
a "section" $f$ over $\operatorname{Top}(X)$.

**c)** The fact that the functor $g^*=f_!$ is fully faithful, exact, and commutes with $V$-inductive limits partially
justifies the very convenient point of view (due to J. Giraud) according to which, in practically all questions of sheaf
theory on $X$, it is harmless to replace usual sheaves, or "small" sheaves, by the associated "big" sheaves. This is so
in particular for cohomological questions, since $g_*$ is exact, the functors $R^i g_*$ vanish for $i>0$, and therefore
for every big sheaf $F$ on $X$ one has canonical isomorphisms

```text
H^i(TOP(X), F) ~= H^i(Top(X), F_X) = H^i(X, F_X).
```

Applying this to a sheaf of the form $\operatorname{Prol}(F)$, where $F$ is a small sheaf on $X$, one concludes (since
$\operatorname{Prol}(F)_X\simeq F$ canonically) a canonical isomorphism:

```text
H^i(X, F) = H^i(TOP(X), Prol(F)).
```

Thus the cohomological invariants of $X$, computed via the small or the big topos of $X$, are essentially identical. The
same result is moreover valid in noncommutative cohomology.

[PDF p. 377]

**Exercise 4.10.6.** Let $S$ be a $U$-site whose topology is less fine than the canonical topology, and let $M$ be a
subset of $\operatorname{Fl}S$ satisfying the following conditions:

**a)** The morphisms of $M$ are quarrable (I 10.3), and $M$ is stable under base change.

**b)** $M$ contains the identity arrows and is stable under composition.

**c)** An arrow $u : X\to Y$ such that there exists a covering family $Y_i\to Y$, with the morphisms
$X\times_Y Y_i\to Y_i$ in $M$, is itself an element of $M$.

**d)** For every $X\in\operatorname{ob}S$, every covering family of $X$ is refined by a covering family
$(f_i : X_i\to X)$, with the $f_i\in M$.

For every $X\in\operatorname{ob}S$, consider the site $S(X)$ ("small site of $X$") whose underlying category is the full
subcategory of $S/X$ formed by the objects whose structural morphism is in $M$, endowed with the topology induced (III
3.1) by that of $S$.

**1°)** For every arrow $u : X\to Y$ of $S$, show that base change by $u$ from $S(Y)$ to $S(X)$ is a continuous functor,
hence gives a functor commuting with inductive limits (III)

```text
S(u)^* : S(Y)~ -> S(X)~.
```

**2°)** Define an equivalence between the topos $\widetilde{S}$ and the category of systems

```text
(F_X)_{X in ob S},    (phi_u)_{u in Fl S}
```

[PDF p. 378]

formed by objects $F_X\in\operatorname{ob}\widetilde{S(X)}$, and, for every arrow $u : X\to Y$ in $S$, by a morphism

```text
phi_u : S(u)^*(F_Y) -> F_X,
```

these systems being subject to a transitivity condition for a composite $v\circ u$ of arrows of $S$, and to the
condition that $u\in M$ implies that $\varphi_u$ is an isomorphism.

**3°)** Define "restriction" and "prolongation" functors

```text
Res_X : (S/X)~ -> S(X)~,
Prol_X : S(X)~ -> (S/X)~.
```

Show that $\operatorname{Res}_X$ commutes with small inductive and projective limits and that $\operatorname{Prol}_X$ is
fully faithful, its essential image being formed by the sheaves $F$ such that $\varphi_u$ is an isomorphism for every
arrow $u$ of $S/X$.

**4°)** Define an adjunction morphism making $\operatorname{Res}_X$ right adjoint to $\operatorname{Prol}_X$. Conclude
that there exists a morphism of topoi

```text
f : S(X)~ -> (S/X)~
```

making $\widetilde{S(X)}$ a subtopos of $\widetilde{(S/X)}$ and such that

```text
f_! = Prol_X,
f* = Res_X.
```

Show that $\operatorname{Prol}_X$ transforms abelian sheaves into abelian sheaves.

**5°)** Show that if $S(X)$ admits fiber products, $\operatorname{Prol}_X$ is exact. Deduce that there then exists a
morphism of topoi $g : \widetilde{(S/X)}\to\widetilde{S(X)}$ which is a left retraction of $f$, i.e. such that

[PDF p. 379]

```text
g* = Prol_X,
g_* = Res_X.
```

(For an example where $S(X)$ does not admit fiber products, take for $S$ the category of schemes endowed with the etale
topology, for $M$ the smooth morphisms, and for $X$ a noetherian scheme of dimension $>0$.)

**6°)** Show that for every abelian sheaf $F$ of $\widetilde{(S/X)}$, one has an isomorphism

```text
H^q(X, F) ~= H^q(X, Res_X F)        for all q.
```

Show, using for example hypercoverings, that for every abelian sheaf $G$ of $\widetilde{S(X)}$, one has an isomorphism

```text
H^q(X, G) ~= H^q(X, Prol_X G)       for all q.
```

**7°)** Buy a chocolate medal for the editor.

```text
```

### 5. Induced Topos

**5.1.** Let $E$ be a topos and let $X$ be an object of $E$. Then the category $E/X$ of objects of $E$ over $X$ is a
topos, as follows for example immediately from Giraud's criterion 1.2 ii). One can also, thanks to 1.2.1, realize $E$ as
a category of sheaves $\widetilde{C}$, where $C$ is a

[PDF p. 380]

generating subcategory of $E$ which can be chosen so that $X\in\operatorname{ob}C$; then one knows that
$E/X=\widetilde{C}/X$ is equivalent to $\widetilde{(C/X)}$ (III 5.4), hence it is a topos.

The topos $E/X$ is called the **topos induced** on the object $X$ of $E$.

**5.2.** We shall define a canonical morphism of topoi

```text
(5.2.1)    j_X : E/X -> E,
```

called the **inclusion morphism** of the induced topos $E/X$ into the ambient topos $E$, or better (cf. 5.7), the
**localization morphism** of $E$ at $X$. This morphism corresponds to a sequence of three adjoint functors (cf. 3.1.3)

```text
(5.2.2)    j_{X!},    j_X^*,    j_{X*},
```

which can be made explicit as follows:

**a)** The functor

```text
j_{X!} : E/X -> E
```

is the "forget the structural arrow" functor from $E/X$ to $E$.

**b)** The functor

```text
j_X^* : E -> E/X
```

is defined by

```text
j_X^*(Z) = (X x Z, pr_1),
```

where $\operatorname{pr}_1 : X\times Z\to X$ is the first projection. It may also be interpreted as the base change
functor relative to the morphism

```text
X -> e_E,
```

where $e_E$ is the final object of $E$. It is trivial, by definition of the base change functor, that $j_X^*$ is indeed
right adjoint to $j_{X!}$. In particular it commutes with projective limits. It also commutes with

[PDF p. 381]

inductive limits, by virtue of the special exactness properties of topoi (II 4).

**c)** From this last fact it follows (1.6) that $j_X^*$ admits a right adjoint

```text
j_{X*} : E/X -> E.
```

For an object $X'$ over $X$, the object $j_{X*}(X')$ is also sometimes denoted by one of the symbols

```text
prod_{X/e_E}(X'/X),    Hom_{X/e_E}(X, X'),    Res_{X/e_E}(X'/X)
```

("Weil restriction"), one or another of which is no doubt already familiar to the learned reader of our modest work.

**5.3.** One should be careful that the functor $j_{X!}$ commutes with fiber products and transforms monomorphisms into
monomorphisms, but it is not in general left exact for all that. It is left exact only if $X$ is a final object of $E$
(because $X=j_{X!}(X,\operatorname{id}_X)$, and $(X,\operatorname{id}_X)$ is a final object of $E/X$), that is, if and
only if $j_X$ is in fact an equivalence of topoi (hence if all the functors (5.2.2) are equivalences). (*)

Similarly, the functor $j_{X*}$ is not in general right exact, and does not necessarily transform epimorphisms into
epimorphisms.

One concludes from these observations that the direction of the morphism of topoi relating $E/X$ to $E$, for an object
$X$ of the topos $E$, is determined without possible ambiguity.

**5.4.** The functor $j_X^*$ is often called the localization functor or restriction functor. This latter terminology is
justified by identifying objects of $E$ resp. on $E/X$ with sheaves on $E$ resp. on $E/X$ (1.2 iii)), and by noting that
with this identification, the adjunction formula between $j_{X!}$ (forgetful functor) and $j_X^*$ is interpreted as
saying that $j_X^*(F)$

> (*) For a property of commutation of $j_{X!}$ with change of topos, cf. XVII 5.1.2.

[PDF p. 382]

is the sheaf restriction to $E/X$ of the sheaf $F$ on $E$ (taking "restriction" in the generalized sense: composite with
the "inclusion" functor $j_{X!} : E/X\to E$). In accordance with familiar notation in other contexts, we shall also
often write, indifferently:

```text
(5.4.1)    j_X^*(F) = F|X = F_X = restriction of F to X.
```

Similarly, when $E$ is of the form $\widetilde{C}$, where $C$ is a (small) site, and $X$ is of the form $\varepsilon(S)$
with $S\in\operatorname{ob}C$, so that one has the equivalence of categories recalled in 5.1

```text
E/X = C~/epsilon(S) ~= (C/S)~
```

($C/S$ being endowed with the topology induced by that of $C$), the functor $j_X^*$ is identified simply with the
"restriction" functor of a variable sheaf $F$ on $C$ to the category $C/S$.

These reflections moreover make it possible to anticipate the important role that induced topoi and localization
morphisms (5.2.1) will play in all questions where one is led to reason by "localization on $E$" (cf. 8), that is,
practically in all questions involving sites or topoi.

**5.5.** Let

```text
f : X -> Y
```

be an arrow of $E$, which therefore makes it possible to interpret $X$ (or more correctly, $(X,f)$) as an object of
$E/Y$. It is evident that one has a canonical isomorphism

```text
(5.5.1)    (E/Y)/X ~= E/X
```

(transitivity of induced topoi). Applying the construction of 5.1 to $E/Y$ instead of $E$, one therefore finds a
canonical morphism of topoi

[PDF p. 383]

```text
(5.5.2)    loc(f) or f : E/X -> E/Y,
```

also called the **localization morphism** (associated to $f$). When $Y$ is the final object of $E$, one essentially
recovers (5.2.1). The localization morphism for $f$ is associated to a sequence of three adjoint functors

```text
(5.5.3)    f_!,    f^*,    f_*,
```

which may be interpreted respectively as a forgetful functor, as a restriction functor, and as a functor denoted, at
will ($X'$ being the argument),

```text
prod_{X/Y}(X'/X),    Hom_{X/Y}(X, X'),    Res_{X/Y}(X'/X).
```

**5.6.** The transitivity of forgetful functors implies that for two composable morphisms

```text
X --f--> Y --g--> Z
```

of $E$, one has a canonical isomorphism of morphisms of topoi

```text
loc(gf) ~= loc(g) loc(f) : E/X -> E/Y -> E/Z.
```

Moreover, for three composable morphisms, one has the usual compatibility relation for the preceding transitivity
isomorphisms. Subject to the usual abuse of language, this therefore makes it possible to regard

```text
X |-> E/X
```

as a covariant functor from $E$ to the category $(V\text{-}U\text{-}\mathrm{top})$ (3.3.1). More precisely, one finds a
2-functor (not strict in general) from $E$ to the 2-category $(V\text{-}U\text{-}\mathrm{top})$.

Before continuing the generalities on induced topoi (5.10), let us give a few instructive examples.

**5.7.** Let $X$ be a topological space, hence a topos $\operatorname{Top}(X)$ (2.1). Let $X'$ be an object of
$\operatorname{Top}(X)$, which it will be convenient to interpret as an etale space over $X$, $p : X'\to X$. The
category $\operatorname{Top}(X)/X'$ is then identified with the category of etale spaces $X''$ over $X$, equipped with
an $X$-morphism $X''\to X'$. One knows that such a morphism makes $X''$ an etale space over $X'$, and in this way one
finds a canonical equivalence of topoi

```text
Top(X)/X' ~= Top(X').
```

The localization morphism is therefore identified with a morphism of topoi
$\operatorname{Top}(X')\to\operatorname{Top}(X)$, and one immediately observes that the latter is none other than the
morphism

```text
Top(p) : Top(X') -> Top(X)
```

associated to the structural continuous map $p : X'\to X$. Intuitively, the localization morphism is therefore simply
the translation, in topos language, of the etale morphism $p : X'\to X$. This both explains the appropriateness of the
terminology "localization morphism" and encourages caution in the use of the term "inclusion morphism", which seems
especially appropriate in the case where $p$ is an open immersion. It will therefore be prudent in 5.1 to reserve the
term "inclusion morphism" for the case where the morphism $X\to e_E$ is a monomorphism, i.e. where $X$ is identified
with a subobject of the final object of $E$.

**5.8.** Let $E$ be a topos, let $G$ be a group of $E$, let $H$ be a subgroup of $G$,

```text
X = G/H
```

the quotient homogeneous space, regarded as an object of $E$ with left group of operators $G$, i.e. as an object of the
classifying topos $B_G$ (2.4).

[PDF p. 385]

We shall determine the induced topos

```text
(B_G)/X        (X = G/H),
```

by defining an equivalence of topoi

```text
(5.8.1)    c : B_H ~= (B_G)/X,
```

such that one has commutativity up to canonical isomorphism in the diagram

```text
(5.8.2)        c          j_X
          B_H ---> (B_G)/X ---> B_G
           \_____________________/
                    B_i
```

where $j_X$ is the localization morphism in $B_G$, and where

```text
B_i : B_H -> B_G
```

is the morphism deduced from the inclusion $i : H\to G$ (4.5).

To define (5.8.1), we shall simply indicate the description of the inverse image functor $c^*$ and direct image functor
$c_*$, leaving to the reader the task of verifying that these are indeed quasi-inverse equivalences of one another,
giving rise to the commutative diagram (5.8.2) of morphisms of topoi. Let $e$ be the subobject of $E$ underlying $X$,
image of the section of $X$ (over a chosen final object $e_E$ of $E$) deduced from the unit section of $G$. If $X'$ is
an object of $B_G$ over $G$, then $c^*(X')$ denotes the inverse image of $e$ in $X'$,

```text
c*(X') = X' x_X e,
```

which is stable under the left action of $H$ on $X'$, the restriction of the given action of $G$ on $X'$. This indeed
defines a functor

[PDF p. 386]

```text
c* : (B_G)/X -> B_H.
```

On the other hand, if $X'$ is an object of $B_H$, then the morphism from $X'$ to the final object $e_H$ of $B_H$ (i.e.
the final object $e_E$ of $E$ with trivial action of $H$) gives, by applying the functor $i_!$ (4.5), a morphism of
$B_G$

```text
i_!(X') -> i_!(e_H) ~= X,
```

which makes it possible to interpret $i_!(X')$ as an object of $(B_G)/X$, whence the desired functor

```text
c_* : X' |-> (i_!(X') -> X) : B_H -> (B_G)/X.
```

**5.8.3.** Thus one sees, thanks to (5.8.2), that if $G$ is a group of a topos and $H$ a subgroup, the functor
"restriction of operators from $G$ to $H$" can be interpreted as a localization functor. In particular, taking for $H$
the unit subgroup, one sees that the functor "forget the actions of $G$" is interpreted as a localization functor. More
generally, one concludes that if $(X,G)$ is an object of $E$ with an action of $G$ (i.e. an object of the classifying
topos $B_G$), then the functor "forget the actions of $G$",

```text
E' = (B_G)/(X, G) -> E/X
```

can be interpreted as a localization functor, relative to a suitable object $E_{G,(X,G)}$ of $E'$ covering the final
object. It suffices to take

```text
E_{G,(X, G)} = E_G x (X, G),
```

whence the cartesian diagram (where $E_G=G_s=G$ with action of $G$ by left translation)

[PDF p. 387]

```text
(5.8.3.1)
        E_G  <-----  E_{G,(X, G)} = Z
         |              |
         v              v
        e_G  <-----  (X, G).
```

and to note that, by transitivity of induced topoi, the induced topos

```text
E' / Z = ((B_G)/(X, G))/Z
```

is equivalent to the topos $((B_G)/E_G)/Z$. Since $(B_G)/E_G$ is equivalent to $E$ by the functor $c^*$ of (5.8.1) (with
$H=e$), it suffices to verify that this equivalence transforms $Z$ into the object $X$ of $E$ (which is trivial) to
deduce the desired equivalence of categories

```text
E'/Z ~= E/X.
```

We leave to the reader the task of verifying that the composite of this equivalence with the localization functor

```text
E' = (B_G)/(X, G) -> E'/Z
```

is the functor "forget the actions of $G$". Thus one sees that the cartesian diagram above gives, by passage to induced
topoi, a diagram, commutative up to canonical isomorphism (5.6), of morphisms of topoi:

```text
(5.8.3.2)
        (B_G)/E_G ~= E  <----  (B_G)/Z ~= E'/Z ~= E/X
             |                         |
             v                         v
            B_G        <----       (B_G)/(X, G) = E',
```

where the inverse image functors associated to the vertical arrows $j$, $j'$ are the functors "forget the actions of
$G$", and where the inverse image functor $i^*$ is identified with the localization functor $E\to E/X$. This

[PDF p. 388]

diagram is moreover "2-cartesian" in the sense of 5.11 below.

**5.8.4.** We leave to the reader the task of extending the preceding reflections to the case of a pro-group $G=(G_i)$,
in the particular case where $H$ is defined as the "kernel" of $G\to G_i$. (In the case of profinite groups, this means
that one restricts to subgroups $H$ of $G$ which are open, i.e. closed and of finite index.)

**Exercise 5.9.** Let $E$ be a topos, let $G$ be a group of $E$, let $B_G$ be the classifying topos of $G$ (2.4),

```text
pi : B_G -> E
```

the morphism of topoi deduced from the homomorphism from $G$ to the unit group $e$ of $E$ (taking into account that
$B_e\simeq E$).

**a)** Let

```text
E_G = G_s
```

be the object of $B_G$ whose underlying $E$-object is $G$, the actions of $G$ being defined by left translation.
Consider $\pi^*(G)$ as a group of $B_G$ (it is the group $G$ of $E$ with the trivial actions of $G$ on it). Show that
the morphism of $E$

```text
G_s x G -> G_s
```

defined by the right translations of $G$ on $G_s$ is compatible with the actions of $G$ on $G_s$ and on $G=\pi^*(G)$,
and defines a morphism in $B_G$

```text
E_G x pi*(G) -> E_G.
```

Show that this morphism makes $E_G$ an object of $B_G$ with a right action of the $B_G$-group $\pi^*(G)$, and that this
latter makes $E_G$ a torsor

[PDF p. 389]

under $\pi^*(G)$ (i.e. the final object of $B_G$ can be covered by objects $X_i$ such that, for every $i$, the
restriction of $E_G$ to $X_i$ is isomorphic to the trivial bundle with operators $(\pi^*(G)_{X_i})_d$).

**b)** Let

```text
q : E' -> E
```

be a topos over $E$. For every topos $B$ over $E$, define the category $\operatorname{Homtop}_E(E',B)$ of morphisms of
topoi from $E'$ to $B$ compatible with the structural morphisms $E'\to E$ and $B\to E$ up to a given isomorphism. Taking
$B=B_G$, define by the formula $f\mapsto f^*(E_G)$ an equivalence of categories

```text
Homtop_E(E', B_G) -> Tors(E', q*(G)),
```

where the second member denotes the category of $q^*(G)$-torsors (on the right) on $E'$.

**c)** Let $H$ be a subgroup of $G$, so that $\pi^*(H)$ is a subgroup of $\pi^*(G)$, and therefore acts on $E_G$ by
restriction of the group of operators, whence a quotient object

```text
X = E_G / pi*(H),
```

which is none other than the object $G/H$ equipped with the usual left action of $G$. Let $e_G$ be the final object of
$B_G$ (i.e. the final object $e_E$ of $E$ with trivial action, there is no choice, of $G$), and consider in $B_G$ the
diagram of morphisms

```text
        E_G
        |  \
        v   v
        e_G <- X = E_G / pi*(H)
```

[PDF p. 390]

whence, by passing to the topoi induced by $B_G$ on these objects, a diagram of morphisms of topoi, commutative up to
canonical isomorphism (5.6). Show that this diagram is equivalent to the diagram

```text
        E = B_e
        |   \
        v    v
        B_G <- B_H,
```

whose three arrows are the arrows associated by 4.5 to the group morphisms $e\to H\to G$ of $E$. (Thus the classifying
topos $B_H$ is interpreted intuitively as a homogeneous space over $B_G$, with group $\pi^*(G)$, associated to the
universal torsor (= homogeneous principal bundle) $E_G$ on $B_G$.)

**d)** Revisit Example 5.7 in the case where $X'$ is an etale covering (locally trivial, cf. 2.7.4) of $X$, interpreting
it in terms of the considerations of the present exercise.

```text
```

### 5.10. Inverse Images of Induced Topoi

Let

```text
f : E' -> E
```

be a morphism of $U$-topoi, let $X$ be an object of $E$, and let $X'=f^*(X)$ be its inverse image in $E'$. We shall then
define a diagram of morphisms of topoi

```text
(5.10.1)
        E/X  <-----  E'/X'
         |              |
       j_X            j_X'
         v              v
         E   <-----     E'
              f
```

[PDF p. 391]

where $j_X$ and $j_{X'}$ are the localization morphisms (5.2), and where $f/X$ is defined below, a diagram which will be
commutative up to canonical isomorphism. We shall define here $f/X$ by means of the inverse image functor

```text
(5.10.2)    (f/X)* : E/X -> E'/X',
```

for which we simply take the functor "induced" by $f^*$, in the evident sense. Since the inclusion functors
$j_{X!} : E/X\to E$ and $j_{X'!} : E'/X'\to E'$ commute with $U$-inductive limits and with fiber products, and since
they are conservative, it follows immediately that the functor $(f/X)^*$ commutes with $U$-inductive limits and with
fiber products just as the functor $f^*$ inducing it does; since moreover $(f/X)^*$ obviously transforms the final
object $X$ into the final object $X'$, it is left exact, and is therefore associated to a morphism of topoi

```text
(5.10.3)    f/X : E'/X' -> E/X,
```

defined up to unique isomorphism (1.1.1). On the other hand, the diagram deduced from (5.10.1) by passing to inverse
image functors is commutative (up to canonical isomorphism) by construction and because $f^*$ commutes with products
$X\times Y$; hence (5.10.1) itself is commutative, up to a unique isomorphism inducing the canonical isomorphism on the
inverse image functors of the two composites $f\circ j_{X'}$ and $j_X\circ f/X$ (3.2.1).

**5.10.4.** When $f : E'\to E$ is associated to a continuous map $Y'\to Y$ of topological spaces (4.1), so that $X$ is
identified with an etale space over $Y$, and $X'$ with the fiber product $X\times_Y Y'$, then, identifying the induced
topoi $\operatorname{Top}(Y)/X$ and $\operatorname{Top}(Y')/X'$ with $\operatorname{Top}(X)$ and
$\operatorname{Top}(X')$ respectively (5.7), one observes that the morphism $f/X$ just

[PDF p. 392]

constructed is (up to unique isomorphism) the morphism $\operatorname{Top}(X')\to\operatorname{Top}(X)$ deduced from the
canonical continuous map $X'\to X$. Thus, in light of this example, one may say that the topos $E'/X'$ plays the role of
a fiber product of $E/X$ and $E'$ over $E$. This intuition is made precise by the following result:

```text
```

**Proposition 5.11.** With the notation of 5.10, the diagram (5.10.1), equipped with the compatibility isomorphism

```text
alpha : f circ j_X' -> j_X circ f/X,
```

is "2-cartesian"; more precisely, for every $U$-topos $F$, if to every morphism of topoi $g : F\to E'/X'$ one associates
the triple

```text
((f/X) circ g, j_X' circ g, alpha * g) = (g_1, g_2, beta),
```

where $g_1 : F\to E/X$ and $g_2 : F\to E'$ are morphisms of topoi, and $\beta : j_X\circ g_1\to f\circ g_2$ is an
isomorphism of morphisms of topoi from $F$ to $E$, one obtains an equivalence of categories from
$\operatorname{Homtop}(F,E'/X')$ to the category

```text
Homtop(F, E/X) x^2_{Homtop(F, E)} Homtop(F, E')
```

of all triples $(g_1,g_2,\beta)$ as above.

(NB. We have placed a $2$ over the cartesian product sign to recall that this is not an ordinary fiber product of
categories, but a "2-fiber product", in the sense made explicit in the statement.)

To prove 5.11, one makes the morphisms of topoi explicit by means of the associated inverse image functors. For this we
shall need auxiliary results, given in 5.11.1 to 5.12 below.

**5.11.1.** Consider generally the situation where one is given two categories $E$, $E'$, an object $X$ of $E$ which is
supposed quarrable, i.e. such that the functor

```text
j : A |-> A x X : E -> E/X
```

[PDF p. 393]

is defined, and finally a left exact functor

```text
(*)    phi : E/X -> E'.
```

Since $E/X$ has a final object, namely $(X,\operatorname{id}_X)=X$, the same is therefore true of $E'$, which admits the
final object

```text
e' ~= phi(X).
```

Supposing that the final object $e'$ of $E'$ has been chosen, we shall associate to every $\varphi$ as above a pair

```text
(**)    (psi, u),    with psi = phi circ j : E -> E', and u in Hom(e', psi(X)).
```

To define $u$, note that

```text
psi(X) = phi(X x X)
```

has a canonical section $\delta_X$ over the final object $X$ of $E/X$, namely the diagonal section, and define

```text
u = phi(delta_X) : phi(X) = e' -> phi(X x X) = psi(X).
```

I claim that knowledge of the pair (**) makes it possible to reconstruct the functor $\varphi$ of (*) up to unique
isomorphism. For this, for every object

```text
p : X' -> X
```

of $E/X$, consider the following cartesian diagram in $E/X$:

```text
        X'  ------>  j(X') = X' x X
        |              |
        v              v j(p)
        X   --delta_X-->   j(X) = X x X,
```

where the first horizontal arrow is the graph morphism $\Gamma_p=(\operatorname{id}_{X'},p)$. Applying the left exact
functor $\varphi$ to this diagram, and using the definition of $\psi$ as $\varphi\circ j$, one finds a cartesian diagram

[PDF p. 394]

```text
        phi(X', p)  ------>  psi(X')
           |                |
           v                v psi(p)
          e'  ------u---->  psi(X),
```

in other words one obtains a canonical isomorphism

```text
(5.11.1.1)    phi(X', p) ~= psi(X') x_{psi(X)} e'.
```

One immediately observes that it is functorial in the object $(X',p)$ of $E/X$, which makes explicit how one
reconstructs, up to isomorphism, the functor $\varphi : E/X\to E'$ by means of the pair $(\psi,u)$ of (**). Note
moreover that the functor $\psi$ is left exact; more generally, $\varphi$ commutes with every type of projective limits
with which $\psi$ commutes, because $j$ commutes with projective limits.

Conversely, suppose now that finite projective limits are representable in $E$ and $E'$, and start from a pair

```text
(psi, u),    psi : E -> E',    u in Hom(e', psi(X)),
```

where the functor $\psi$ is left exact. Define by formula (5.11.1.1) a functor $\varphi : E/X\to E'$. One immediately
verifies that this functor is left exact; more generally, that it commutes with every type of projective limits
representable in $E$ with which $\psi$ commutes. This follows immediately from the cartesian diagram

```text
        lim_I X'_i  <-----  lim_I E/X_i'
            |                   |
            v                   v
        lim_I X     <---delta---    X
```

[PDF p. 395]

relating the projective limits computed in $E$ or in $E/X$ (where $\delta$ denotes the diagonal morphism into the
projective limit of the constant functor with value $X$), by applying the functor $\psi$ to it, whence a cartesian
diagram in $E'$, and by composing this latter with the cartesian square deduced from $\psi(X)\leftarrow e'$, producing a
composite cartesian square which expresses the compatibility of $\varphi$ with the projective limit under consideration.

One reconstructs the pair $(\psi,u)$ up to isomorphism by means of $\varphi$, noting that one has a canonical
isomorphism

```text
(5.11.1.2)    psi(X') = phi(j(X')),
```

deduced from (5.11.1.1) by replacing $(X',p)$ there by $j(X')=(X'\times X,\operatorname{pr}_2)$, and noting that
$\psi(X'\times X)\simeq\psi(X')\times\psi(X)$. The preceding isomorphism is manifestly functorial in $X'$, i.e. it gives
an isomorphism

```text
psi ~= phi circ j,
```

and one verifies similarly that, by means of this isomorphism, $u : e'\to\psi(X)$ is identified with
$\varphi(\delta_X)$. We have thus obtained the substance of the

```text
```

**Lemma 5.11.2.** Let $E$ and $E'$ be two categories in which finite projective limits are representable, let $X$ be an
object of $E$, let $\operatorname{Sex}(E,E')$ be the category of left exact functors $\psi$ from $E$ to $E'$, and let
$\operatorname{Sex}(E/X,E')$ be the analogous category of left exact functors $\varphi$ from $E/X$ to $E'$. There is
then an equivalence between the category $\operatorname{Sex}(E/X,E')$ and the category $\operatorname{Sex}(E,E')/\Gamma$
of pairs $(\psi,u)$, with $\psi\in\operatorname{ob}\operatorname{Sex}(E,E')$ and $u : e'\to\psi(X)$ (where $e'$ is the
final object of $E'$), whose definition is made explicit in 5.11.1, as is that of a quasi-inverse functor. If $\varphi$
and $(\psi,u)$ correspond, then $\varphi$ commutes with a determined type of projective limits

[PDF p. 396]

if and only if $\psi$ does. If in $E$ and $E'$ base change functors commute with a determined type of inductive limits,
then for $\varphi$ to commute with inductive limits of that type, it is necessary and sufficient that $\psi$ do so.

We leave to the reader the task of making explicit the category structure $\operatorname{Sex}(E,E')/\Gamma$
corresponding to the pairs $(\psi,u)$. Defining the functor

```text
Gamma : Sex(E, E') -> (Ens),    Gamma(psi) = Hom(e', psi(X)),
```

one may interpret $u$ in the pair $(\psi,u)$ as an element of $\Gamma(\psi)$, i.e. a homomorphism $\psi\to\Gamma$ in the
category of presheaves on $\operatorname{Sex}(E,E')^\circ$, which justifies the notation $/\Gamma$ used in the statement
of 5.11.1. To prove 5.11.2, it remains to make explicit in 5.11.1 the functorial character of the constructions
considered for variable $\varphi$ resp. $(\psi,u)$, which is essentially trivial and left to the reader, and finally to
verify the assertion concerning commutation with inductive limits, which is also trivial by means of the explicit
formulas (5.11.1.1) and (5.11.1.2) relating these functors.

One finds in particular, when $E$ and $E'$ are $U$-topoi, and interpreting morphisms of topoi by means of the associated
inverse image functors:

**Proposition 5.12.** Let $E$ and $E'$ be two $U$-topoi, let $X$ be an object of $E$, and consider on
$\operatorname{Homtop}(E',E)$ the contravariant functor

```text
Upsilon : f |-> Gamma(E', f*(X)) = Hom(e', f*(X)) : Homtop(E', E)^circ -> (Ens).
```

There is then an equivalence of categories

```text
(5.12.1)    Homtop(E', E/X) ~= Homtop(E', E)/Upsilon,
```

[PDF p. 397]

where the second member is the full subcategory of $\operatorname{Homtop}(E',E)/\Upsilon$ formed by the pairs $(f,u)$,
with $f\in\operatorname{Homtop}(E',E)$ and $u\in\Upsilon(f)$, i.e. $u\in\Gamma(E',f^*(X))$. This functor is obtained by
associating to every morphism of topoi $h : E'\to E/X$ the pair $(f,u)$ formed by the composite

```text
f = j_X circ h : E' -> E/X -> E,
```

and by the morphism

```text
u : e' = h*(X, id_X) -> f*(X) = h*(j_X^*(X)) = h*(X x X),
```

deduced from the diagonal morphism $\delta_X : X\to X\times X$ by applying $h^*$ to it.

**5.12.2.** Using 5.12, the proof of 5.11 becomes almost evident, and reduces essentially to this (which will serve as a
"formal" proof that would not be more instructive): giving a morphism of topoi $g : F\to E'/X'$ "amounts to the same
thing" as giving a morphism of topoi $g_2 : F\to E'$ and a section $u$ of $g_2^*(X')$; but
$g_2^*(X')=g_2^*(f^*(X))=(fg_2)^*(X)$, so the datum of $u$ is also equivalent to the datum of a lift of the morphism of
topoi $fg_2 : F\to E$ to a morphism of topoi $g_1 : F\to E/X$. This indeed expresses that the datum of a morphism of
topoi $g : F\to E'/X'$ is essentially equivalent to the datum of a triple $(g_1,g_2,\alpha)$ as in 5.11.

```text
```

**Remark 5.13.** We shall see (§ 15) that for every diagram of topoi, there exists a 2-fiber product in the sense of the
2-category $(V\text{-}U\text{-}\mathrm{Top})$ of $U$-topoi $\in V$ (not depending, up to equivalence, on the choice of a
universe $V$ such that $U\in V$). For other natural examples besides 5.11 of "fiber products of topoi", see the last
chapter of Giraud's book [3].

**Exercise 5.14.**

**a)** Let $F$, $G$ be two topoi over a topos $E$. Define the category $\operatorname{Homtop}_E(F,G)$ of pairs
$(f,\alpha)$, where $f : F\to G$ is a morphism of topoi and $\alpha : p\to qf$ is an isomorphism of morphisms of topoi
from $F$ to $E$ ($p : F\to E$ and $q : G\to E$ being the structural morphisms of topoi). Define pairing functors

```text
Homtop_E(F, G) x Homtop_E(G, H) -> Homtop_E(F, H),
```

and associativity isomorphisms.

**b)** Let $X$ and $Y$ be two objects of a topos $E$. Define a natural functor from the discrete category defined by the
set $\operatorname{Hom}(X,Y)$ to the category $\operatorname{Homtop}_E(E/X,E/Y)$. Compatibility with compositions of
morphisms in $E$ and the pairings considered in a).

**c)** Prove that the functor considered in b) is an equivalence of categories. In particular, an object $X$ of a topos
$E$ is reconstructed up to unique isomorphism when one knows "up to $E$-equivalence" the induced topos $E/X$, as a topos
over $E$.

```text
```

### 6. Points of a Topos and Fiber Functors

**6.0.** Let $P$ be the standard punctual $U$-topos (2.2)

```text
P = (U-Ens).
```

Given the rather different intuition attached on the one hand to the

> (*) Result due to P. Deligne. The case where $E$ is the punctual topos had previously been treated by Mme Hakim.

[PDF p. 399]

symbol $P$, representing a geometric object in the nature of a point, and on the other hand to
$(U\text{-}\mathrm{Ens})$, representing a "large category", which will be interpreted as "the category of sheaves on
$P$", one should, according to context, use one or the other symbol exclusively, although, from the strict logical point
of view, they designate one and the same object.

**Definition 6.1.** Let $E$ be a $U$-topos. A **point** of $E$ means any morphism of topoi $P\to E$ from the punctual
topos $P$ (6.0) to $E$. The **category of points** of $E$, denoted $\operatorname{Point}(E)$ or $\operatorname{Pt}(E)$,
is the category $\operatorname{Homtop}(P,E)$ (3.2). If $p : P\to E$ is a point of $E$, associated to the inverse image
functor

```text
p* : E -> (U-Ens),
```

and if $F$ is an object of $E$, the set $p^*(F)$ is called the **fiber** of $F$ at $p$, and is denoted $F_p$.

**6.1.1.** Of course, when $F$ is a group object (resp. ring object, resp. ...) of $E$, its fiber $F_p$ at $p$ is a
group (resp. a ring, resp. ...) (3.1.2).

**6.1.2.** By virtue of 3.2.1, the category of points of $E$ is equivalent, via the functor $p\mapsto p^*$, to the
category opposite to that of the functors

```text
phi : E -> (U-Ens)
```

which commute with $U$-inductive limits and are left exact. Thus, essentially, giving a point of $E$ amounts to the same
thing as giving such a functor $\varphi$.

**Definition 6.2.** A **fiber functor** of the $U$-topos $E$ means any functor

```text
phi : E -> (U-Ens)
```

which commutes with $U$-inductive limits and is left exact. The **category of fiber functors** on $E$, denoted

[PDF p. 400]

$\operatorname{Fib}(E)$, is the full subcategory of $\operatorname{Hom}(E,(U\text{-}\mathrm{Ens}))$ formed by the fiber
functors on $E$.

**6.2.1.** By virtue of 6.1.2, the category $\operatorname{Fib}(E)$ of fiber functors on $E$ is therefore equivalent to
the opposite of the category $\operatorname{Point}(E)$ of points of $E$, via the functor $p\mapsto p^*$ from the latter
to the former:

```text
(6.2.1.1)    Point(E)^circ ~= Fib(E).
```

For a functor

```text
phi : E -> (U-Ens)
```

to be a fiber functor, it is necessary and sufficient that it be the fiber functor $F\mapsto F_p$ associated to a point
$p$ of $E$ (6.1). In other words, the functor (6.2.1.1) is surjective. Let us also point out that a functor $\varphi$ is
a fiber functor if and only if it is left exact and transforms covering families into surjective families (1.7). This
last condition is also expressed by saying that $\varphi$ commutes with $U$-sums and transforms epimorphisms into
epimorphisms.

```text
```

**6.3.** Let $C\in U$ be a site. A **point of the site** $C$ means a point of the topos $\widetilde{C}$, and the
**category of points** of the site $C$ is the category

```text
Point(C) = Point(C~).
```

On the other hand, consider the functor

```text
(6.3.1)    phi |-> phi|C : Fib(C~) -> Hom(C, (U-Ens)),
```

which is fully faithful and whose essential image is the full subcategory
$\operatorname{Morsite}((U\text{-}\mathrm{Ens}),C)^\circ$ (4.9.4), which we shall also denote by
$\operatorname{Fib}(C)$. A functor

```text
psi : C -> (U-Ens)
```

[PDF p. 401]

is called a **fiber functor on the site** $C$ if it lies in the essential image of (6.3.1), just made explicit. Such a
functor is therefore continuous (a fortiori (III 1.6), it transforms covering families into covering families, i.e. into
surjective families), and is left exact. When finite projective limits are representable in $C$ (a condition verified in
almost all cases encountered in practice), the preceding properties characterize fiber functors on $C$, which are then
the functors $\psi : C\to(U\text{-}\mathrm{Ens})$ which are left exact and transform covering families into surjective
families (4.9.4).

One should retain that the functor $\varphi\mapsto\varphi|C$ is an equivalence of categories

```text
Fib(C~) ~= Fib(C),
```

so that giving a fiber functor on the topos $\widetilde{C}$ (or again a point of this topos) amounts essentially to the
same thing as giving a fiber functor on the site $C$. Given a fiber functor $\psi$ on $C$, which therefore comes up to
isomorphism from a fiber functor $\varphi$ on $\widetilde{C}$, one reconstructs the latter from $\psi$, up to canonical
isomorphism, by the formula

```text
(6.3.2)    phi(F) = colim_{X in C/F} psi(X),
```

where $C/F$ is the category of objects $X$ of $C$ equipped with a morphism $X\to F$ (in $\widetilde{C}$, i.e. with an
element of $F(X)$). Formula (6.3.2) is an immediate consequence of the fact that $\varphi$ commutes with inductive
limits and that one has a canonical isomorphism, functorial in $F$ (II 4.1.1):

[PDF p. 402]

```text
F ~= colim_{X in C/F} epsilon(X).
```

More generally, when $G$ is a presheaf on $C$, one has a canonical isomorphism, functorial in $G$:

```text
(6.3.3)    phi(aG) ~= colim_{X in C/G} psi(X),
```

where $aG$ is the sheaf associated to $G$ (II 4.1.1). Indeed, one knows that one has the formula

```text
aG ~= colim_{X in C/G} epsilon(X).
```

**6.4.0.** We refer to I 6.1 for the notion of conservative family of functors

```text
phi_i : E -> E_i    (i in I).
```

Note that when $E$ and the $E_i$ are $U$-topoi, and the functors $\varphi_i$ are inverse image functors $f_i^*$
associated to morphisms of topoi

```text
f_i : E_i -> E,
```

then all the exactness properties postulated in I 6.2, I 6.3, and I 6.4 are verified, provided that in I 6.2 (v), $D$ is
assumed finite. It is then equivalent for $(f_i^*)_{i\in I}$ to be conservative, or conservative for monomorphisms (I
6.1), or conservative for epimorphisms, or finally faithful.

[PDF p. 403]

When the family of functors $f_i^*$ is conservative, we shall also sometimes say that the family of morphisms of topoi
$(f_i)_{i\in I}$ is conservative. In particular:

**Definition 6.4.1.** Let $E$ be a $U$-topos, and let $(p_i : P\to E)_{i\in I}$ be a family of points of $E$. We say
that this family of points is **conservative** if the family of associated fiber functors $F\mapsto F_{p_i}$, from $E$
to $(U\text{-}\mathrm{Ens})$, is conservative (6.4.0). We say that the topos $E$ has **enough points** if it admits a
conservative family of points (i.e. if the family of all points of the topos is conservative).

**6.4.2.** Let us point out that all $U$-topoi used up to now have enough points. However, one can, "on purpose",
construct topoi which do not have enough points (7.2.6 e) and 7.4); note that such a topos is necessarily not "empty" in
the geometric sense of 2.2. A topos admitting enough points admits a conservative family of points indexed by an
$I\in U$ (6.5). Note, however, in this connection, that if $E$ is a $U$-topos, the set of isomorphism classes of points
of $E$ is not necessarily $U$-small (7.3). It is so, however, in many cases encountered in practice. Finally, for an
interesting existence theorem (due to P. Deligne) of enough points, covering all cases encountered in algebraic
geometry.

**6.4.3.** When $(p_i)_{i\in I}$ is a conservative family of points of the topos $E$, one can apply the remarks of I
6.2, which imply in particular that two arrows $u,v : F\to G$ of $E$ are equal if and only if for every $i\in I$, the
induced arrows on fibers

```text
u_{p_i}, v_{p_i} : F_{p_i} -> G_{p_i}
```

[PDF p. 404]

are equal; that an arrow $u : F\to G$ of $E$ is a monomorphism (resp. an epimorphism) if and only if for every $i\in I$
the same is true of the map $F_{p_i}\to G_{p_i}$; that an object $F$ of $E$ is initial (resp. final) if and only if for
every $i\in I$, $F_{p_i}$ is empty (resp. reduced to one point); that an object $F$ is a subobject of the final object
$e$ if and only if for every $i\in I$, $F_{p_i}$ has at most one point.

**Proposition 6.5.**

**a)** Let $C$ be a $U$-site, and let $(\varphi_i)_{i\in I}$ be a family of fiber functors on $C$ (6.3). For the
corresponding family $(p_i)_{i\in I}$ of points of the topos $E=\widetilde{C}$ to be conservative, it is necessary and
sufficient that for every family $(X_j\to X)_{j\in J}$ in $C$ such that, for every $i\in I$, the corresponding family

```text
(phi_i(X_j) -> phi_i(X))_{j in J}
```

is surjective, the given family $(X_j\to X)_{j\in J}$ be covering.

**b)** Let $E$ be a $U$-topos. If $E$ admits enough points (6.4.1), then $E$ admits a conservative family of points
which is $U$-small.

Assertion b) is a particular case of I 7.7. To prove a), apply I 7.7 to the generating family in $E$ formed by the
$\varepsilon(X)$ ($X\in\operatorname{ob}C$). Recall (II 4.4) that the family $X_j\to X$ is covering if and only if the
family $\varepsilon(X_j)\to\varepsilon(X)$ is epimorphic. If the family of points $(p_i)_{i\in I}$ is conservative, it
is equivalent (6.4.3) to say that for every $i\in I$, the family of the $X_{j,p_i}\to X_{p_i}$ is surjective, i.e. that
the family of the $\varphi_i(X_j)\to\varphi_i(X)$ is surjective. This proves the "only if" in a). For the "if", one
applies criterion I 7.7, which reduces us to verifying that every monomorphism

[PDF p. 405]

$F\to\varepsilon(X)$ such that $F_{p_i}\to\varepsilon(X)_{p_i}$ is an isomorphism for every $i\in I$ is an isomorphism,
or equivalently, an epimorphism. But one can find a covering family of morphisms $\varepsilon(X_j)\to F$, and after
refining further if necessary, one may suppose that the morphisms $\varepsilon(X_j)\to\varepsilon(X)$ are induced by
morphisms $X_j\to X$. By hypothesis, for every $i\in I$, the composite morphisms

```text
phi_i(X_j) -> F_{p_i} -> epsilon(X)_{p_i}
```

form a surjective family (as a composite of two surjective families), i.e. the family of the
$\varphi_i(X_j)\to\varphi_i(X)$ is surjective. It follows by hypothesis that the family $X_j\to X$ is covering, hence
that the family of the $\varepsilon(X_j)\to\varepsilon(X)$ is epimorphic, and a fortiori that $F\to\varepsilon(X)$ is
epimorphic.

**Corollary 6.5.1.** Let $C$ be a category. A topology on $C$ making $C$ a $U$-site admitting enough fiber functors
(i.e. such that the associated topos admits enough points) is entirely known when one knows the full subcategory $\Phi$
of $\operatorname{Hom}(C,\mathrm{Ens})$ formed by the fiber functors on $C$.

Indeed, by virtue of 6.5 a), one then knows how to describe covering families in terms of the family of fiber functors.

In fact, we shall see below (6.8.3) that the subcategory $\Phi$ is contained in the category of pro-representable
functors on $C$, so $\Phi^\circ=\operatorname{Point}(\widetilde{C})$ is identified, up to equivalence, with a full
subcategory of $\operatorname{Pro}\text{-}C$.

Compare 6.5.1 with Giraud's theorem II 5.5, which establishes a one-to-one correspondence between the set of topologies
on $C$ and a certain set of full subcategories of $\operatorname{Hom}(C^\circ,\mathrm{Ens})$.

[PDF p. 406]

**Exercise 6.5.2.** Let $C$ be a category equivalent to a category $\in U$, and let $P$ be a subcategory of
$\operatorname{Pro}(C)$. For every $p\in P$, denote by $X\mapsto X_p$ the functor pro-represented by $p$. A family
$(X_i\to X)_{i\in I}$ in $C$ is called **$P$-covering** if for every $p\in P$, the family $(X_{i,p}\to X_p)_{i\in I}$ is
surjective.

Show that there exists a topology $T_P$ on $C$ for which the covering families are exactly the $P$-covering families,
and that $T_P$ is the finest topology on $C$ for which the functors $X\mapsto X_p$ ($p\in P$) are fiber functors. Show
that the topology $T_P$ makes $C$ a site having enough fiber functors. Show that for every topology $T$ on $C$, among
the topologies $T'$ finer than $T$ which have enough fiber functors, there is a least fine one: it is the topology
$T_P$, where $P$ is the strictly full subcategory of $\operatorname{Pro}(C)$, equivalent to $\operatorname{Point}
(\widetilde{C})$, described in 6.8.3 below.

**Problem 6.5.3.** Characterize the subcategories (strictly full, stable under $U$-filtered projective limits, ...) $P$
of $\operatorname{Pro}(C)$ which can be deduced from a topology on $C$ as the essential image of
$\operatorname{Point}(\widetilde{C})$ (6.8.5).

**6.6.** Let

```text
f : E -> E'
```

be a morphism of $U$-topoi; one deduces from it a canonical functor

```text
Point(f) = (p |-> f circ p) : Point(E) -> Point(E').
```

When one has two composable morphisms of topoi

```text
E --f--> E' --g--> E'',
```

one verifies trivially that one has

[PDF p. 407]

```text
Point(gf) = Point(g) circ Point(f) : Point(E) -> Point(E') -> Point(E'').
```

This therefore makes precise the functorial dependence (without abuse of language for once) of $\operatorname{Point}(E)$
with respect to the topos $E$: if $V$ is a universe such that $U\in V$, one obtains a genuine functor

```text
Point : (V-U-top) -> (V-cat)
```

from the category of $U$-topoi which are elements of $V$ to the category of categories which are elements of $V$.

**6.7.** Let $E$ be a $U$-topos. Then every object $F$ of $E$ defines a contrafunctor

```text
p |-> F_p = p^*(F) : Point(E)^circ -> (U-Ens),
```

whence, for variable $F$, a canonical functor

```text
(6.7.1)    E -> Point(E)^ = Hom(Point(E)^circ, (U-Ens)),
```

which by definition (6.5) is faithful if and only if $E$ has enough points. The functor (6.7.1) has a certain formal
analogy with a Fourier transform.

Let $X$ be an object of $E$, which therefore defines a presheaf $X$ on $C=\operatorname{Point}(E)$. We can therefore
define the category

```text
C_{/X} = Point(E)_{/X}
```

of morphisms $p\to X$ in the category $\widehat{C}$ of presheaves on $C$, i.e. the category of pairs $(p,\xi)$, where
$p$ is a point of $E$ and $\xi$ an element of $X(p)=X_p$, the fiber of $X$ at $p$. This being said, I claim that one has
a canonical equivalence of categories

[PDF p. 408]

```text
(6.7.2)    C' = Point(E_{/X}) ~= C_{/X},    where C = Point(E),
```

whose composite with the inclusion functor $C_{/X}\to C$ is none other than the functor

```text
Point(j_X) : C' = Point(E_{/X}) -> C = Point(E)
```

deduced by functoriality (6.6) from the localization morphism (5.2.1)

```text
j_X : E_{/X} -> E.
```

This is simply the particular case of 5.12 obtained by taking $E'=P$.

**Corollary 6.7.3.** Let $E$ be a topos. If $E$ has enough points, then so does every induced topos $E_{/X}$
($X\in\operatorname{ob}E$). Conversely, if $(X_i)_{i\in I}$ is a family of objects of $E$ covering the final object, and
if for every $i\in I$, $E_{/X_i}$ has enough points, then $E$ has enough points.

For the first assertion, let $f : X'\to X''$ be a morphism in $E_{/X}$ which is not an isomorphism; let us prove that
there exists a point $q$ of $E_{/X}$ such that $f_q$ is not an isomorphism. Since $E$ has enough points, there exists a
point $p$ of $E$ such that $f_p : X'_p\to X''_p$ is not an isomorphism. This implies that there exists a $q\in X_p$ such
that the morphism induced by $f_p$ for the fibers of $X'$ and $X''$ over $X_p$ at $q$ is not an isomorphism. But by
virtue of the equivalence 6.7.2, $q$ can be identified with a point of $E_{/X}$, and the map just considered is none
other than the map on fibers at $q$ induced by $f : X'\to X''$, whence the conclusion.

Conversely, suppose that the $X_i$ cover the final object of $E$, and that the $E_{/X_i}$ have enough points; let us
prove that the same is true of $E$.

[PDF p. 409]

Let $f : X'\to X''$ be a morphism in $E$ which is not an isomorphism. There therefore exists $i\in I$ such that
$f_i : X'_i\to X''_i$ is not an isomorphism, where the index $i$ indicates restriction to $X_i$. There therefore exists
a point $p_i$ of $E_{/X_i}$ such that $f_{i,p_i} : X'_{i,p_i}\to X''_{i,p_i}$ is not an isomorphism. Denoting by $p$ the
image of $p_i$ in $E$ by the localization morphism $E_{/X_i}\to E$, this means that $f_p : X'_p\to X''_p$ is not an
isomorphism, which proves that $E$ has enough points.

**Remark 6.7.4.** The preceding argument shows that if $(p_i)_{i\in I}$ is a conservative family of points of $E$, then
the family of points of $E_{/X}$ which lie over one of the $p_i$ (a family indexed by the sum set of the $X_{p_i}$) is
conservative. Similarly, if the $X_i$ cover the final object of $E$, and if for every $i\in I$, $P_i$ is a conservative
set of points of $E_{/X_i}$, then the set of points of $E$ which are images of the $p\in P_i$ for the localization
morphisms $E_{/X_i}\to E$ (with $i$ and $p$ variable) is conservative.

**6.8.** Let $E$ be a topos, and let $p$ be a point of $E$. A **neighborhood of the point $p$ of the topos $E$** means a
pair $(X,u)$, where $X\in\operatorname{ob}E$ and $u\in X_p$. By virtue of (6.7.2), one may also interpret $u$ as a lift
of $p$ to a point of the induced topos $E_{/X}$.

Introducing the fiber functor $\varphi_p$ associated to the point $p$, one may also interpret a neighborhood of the
point $p$ as an object of the category $E_{/\varphi_p}$ (the full subcategory of $(E^\circ)_{/\varphi_p}^\circ$ formed
by the objects whose source lies in $E\subset\widehat{E}$). This latter category, i.e. the category of pairs $(X,u)$ as
above, will naturally be called the **category of neighborhoods of the point $p$ of the topos $E$**; it is also denoted
$\operatorname{Vois}(p)$.

[PDF p. 410]

Since $\varphi_p$ is left exact and finite projective limits are representable in $E$, finite projective limits are
representable in the category $\operatorname{Vois}(p)$, and the canonical functor $\operatorname{Vois}(p)\to E$ commutes
with them (I 3.4). A fortiori, the opposite category $\operatorname{Vois}(p)^\circ$ is filtered.

Moreover, it is clear (I 3.4) that one has a canonical isomorphism, functorial in $F\in\operatorname{ob}E$:

```text
(6.8.1)    phi_p(F) = F_p ~= colim_{Vois(p)^circ} F(X).
```

In other words, the functor $\varphi_p$, "fiber at the point $p$", is isomorphic to the filtered inductive limit of the
functors represented in the topos $E$ by the neighborhoods of the point $p$ of $E$. One even sees that the fiber functor
is ind-representable (I 8), which also means that it is representable by a pro-object $(X_i)_{i\in I}$ of $E$, where $I$
is a filtered ordered set such that $I\in U$. Indeed, by virtue of loc. cit., this is equivalent to saying that the
category $\operatorname{Vois}(p)$ admits a small cofinal full subcategory.

Now let $C$ be a small full generating subcategory of $E$. I claim that the full subcategory $C_{/\varphi_p}$ of
$\operatorname{Vois}(p)=E_{/\varphi_p}$, formed by the neighborhoods $(X,u)$ of $p$ such that $X\in\operatorname{ob}C$
(a category which is evidently small), is cofinal in $\operatorname{Vois}(p)$. Indeed, let $(X,u)$ be a neighborhood of
$p$; one must find a neighborhood $(X',u')$ of $p$ over $(X,u)$, with $X'\in\operatorname{ob}C$. But there exists a
covering family $X'_i\to X$, with the $X'_i$ in $C$, whence it follows that the $X'_{i,p}$ cover $X_p$, so there exists
an $X'=X'_{i_0}$ and a $u'\in X'_p$ such that $(X',u')$ lies over $(X,u)$, as claimed.

[PDF p. 411]

**6.8.2.** Let $C$ be a $U$-site, and let $p$ be a point of $C$, i.e. a point of the topos $\widetilde{C}$. By abuse of
notation, denote again by $\varphi_p$ the "restriction" of the fiber functor $\varphi_p$ to $C$, i.e. the composite
$\varphi_p\circ\varepsilon$; we shall also often write, for an object $X$ of $C$,

```text
X_p = phi_p(X) = epsilon(X)_p.
```

A **neighborhood of the point $p$ in the site $C$** means a pair $(X,u)$, where $X\in\operatorname{ob}C$ and
$u\in X_p=\varphi_p(X)$. These neighborhoods again form a category $C_{/\varphi_p}$, which may be denoted
$\operatorname{Vois}_C(p)$. We show that the category $\operatorname{Vois}_C(p)^\circ$ is still filtered, that it admits
a $U$-small cofinal full subcategory, and that one has an isomorphism, functorial in the sheaf $F$ on $C$:

```text
(6.8.3)    F_p ~= colim_{Vois_C(p)^circ} F(X).
```

First note, repeating the argument of 6.8.1, that if $C'$ is a full subcategory of $C$ which is topologically generating
(II 3.0.1), then $\operatorname{Vois}_{C'}(p)^\circ$ is cofinal in $\operatorname{Vois}_C(p)^\circ$. Taking $C'$
$U$-small, we are therefore reduced, for the assertion, to the case where $C\in U$. In this case $\widehat{C}$ is a
$U$-topos, and one has an associated sheaf functor $a : \widehat{C}\to\widetilde{C}$, which makes it possible to
construct on $\widehat{C}$ the composite fiber functor $\varphi_p\circ a$. Applying 6.8.1 to the topos $\widehat{C}$ and
to the full generating subcategory $C$ of it, one finds that the category $C_{/\varphi_p a}^\circ$, which is manifestly
isomorphic to $\operatorname{Vois}_C(p)^\circ$, is filtered, and that one has an isomorphism, functorial in the presheaf
$P$ on $C$:

```text
phi_p(a(P)) ~= colim_{Vois_C(p)^circ} P(X).
```

If $F$ is a sheaf on $C$, then $F=aF$, and applying the preceding isomorphism to $F$ regarded as a presheaf, one obtains
(6.8.3). At the same time, this argument establishes the more general formula

[PDF p. 412]

```text
(6.8.4)    (aP)_p ~= colim_{Vois_C(p)^circ} P(X),
```

an isomorphism functorial in the arbitrary presheaf $P$ on $C$, at least when $C$ is small. The general case follows by
introducing a universe $V$ such that $C\in V$, by considering $\varphi_p$ on $\widetilde{C}$ as a fiber functor with
values in $(V\text{-}\mathrm{Ens})$, and by using the compatibility of the formation of the associated presheaf with
enlargement of universes (II 3.6).

**6.8.5.** To every point $p$ of the topos $\widetilde{C}$ we have associated a pro-object of the $U$-site $C$, defined
by the canonical functor $\operatorname{Vois}_C(p)\to C$, taking into account the fact that the category of
neighborhoods of $p$ in $C$ is cofiltered and admits a small cofinal full subcategory. One immediately verifies that for
variable $p$, one obtains a functor

```text
(6.8.5.1)    Point(C~) -> Pro(C).
```

This functor is fully faithful. Indeed, via the associated fiber functors, it is interpreted as a functor
$\operatorname{Fib}(C)\to\operatorname{Fib}(\widetilde{C})\to\operatorname{Pro}(C)^\circ$. The first functor is an
equivalence by virtue of 4.9.4 (recalled for fiber functors in 6.3), and the second is fully faithful by the general
sorites (I 8) of pro-objects.

**6.8.6.** Take the particular case where $C$ is $U$-small and endowed with the chaotic topology, so that
$\widetilde{C}=\widehat{C}$. I claim that in this case the preceding functor is even an equivalence of categories

```text
(6.8.6.1)    Point(C^) ~= Pro(C).
```

[PDF p. 413]

Indeed, it remains to prove that this functor is essentially surjective, which follows from the fact that the functors
of the form $F\mapsto F(X)$ on $\widehat{C}$ are fiber functors, and from the evident fact that every filtered inductive
limit of fiber functors on a topos is again a fiber functor.

Identifying $C$ with a full subcategory of $\operatorname{Pro}(C)$ (I 8), the functor

```text
C -> Point(C^)
```

induced by a quasi-inverse of (6.8.6.1) is manifestly isomorphic to the canonical functor already considered in
(4.6.2.2), whose quasi-inverse under consideration can be regarded as the canonical extension (I 8), taking into account
the fact that $\operatorname{Point}(\widehat{C})$ is stable under small projective limits.

**6.8.7.** Let $(X_i)_{i\in I}$ generally be a pro-object of the $U$-site $C$, giving on $\widetilde{C}$ a functor

```text
(6.8.7.1)    phi(F) = colim_i F(X_i).
```

In view of (6.8.5), it is natural to ask when this functor is a fiber functor. One finds that the following conditions
are equivalent:

**(i)** The preceding functor $\varphi$ is a fiber functor on $\widetilde{C}$.

**(ii)** The "restriction" of $\varphi$ to $C$ is a fiber functor on the site $C$ (6.3).

**(iii)** For every covering family $Y_\alpha\to Y$ of an object $Y$ of $C$, every $i_0\in I$, and every morphism
$X_{i_0}\to Y$, there exist $i\geq i_0$, an $\alpha$, and a morphism $X_i\to Y_\alpha$ making the diagram

```text
X_i  ------>  Y_alpha
 |            |
 v            v
X_{i_0} -->   Y.
```

[PDF p. 414]

commutative.

In fact, condition (iii) simply expresses the fact that $\varphi|_C$ transforms covering families into covering
families. The implications (i) $\Rightarrow$ (ii) $\Rightarrow$ (iii) are trivial, and it remains to prove (iii)
$\Rightarrow$ (i).

Since the functor $\varphi$ is manifestly left exact, it remains to prove (4.9.4) that it transforms covering families
$F_\alpha\to F$ in $\widetilde{C}$ into covering families, i.e. that for every $i_0$ and every $x_0\in F(X_{i_0})$,
there exist $i\geq i_0$, an $\alpha$, and a $y\in F_\alpha(X_i)$, such that $x_0$ and $y$ have the same image in
$F(X_i)$. But, since $F_\alpha\to F$ is covering, there exists a covering family $Z_\lambda\to X_{i_0}$ of $X_{i_0}$,
such that for every $\lambda$ the inverse image of $x_0$ in $F(Z_\lambda)$ lifts to an element of some
$F_\alpha(Z_\lambda)$. By hypothesis (iii), there exist $i\geq i_0$ and an $X_{i_0}$-morphism $X_i\to Z_\lambda$. Then
the image of $x_0$ in $F(X_i)$ therefore lifts to an element $y$ of some $F_\alpha(X_i)$, Q.E.D.

**Exercise 6.9.** Let $C$ be a site $\in U$, let $\varphi$ be a fiber functor on $C$, pro-represented by an object
$(X_i)_{i\in I}$ of $\operatorname{Pro}(C)$. For every index $i\in I$, every object $Y$ of $C$, every morphism
$u : X_i\to Y$, and every covering sieve $R$ of $Y$, choose an index $j\geq i$ such that the composite $X_j\to X_i\to Y$
factors through $R$.

For fixed $i$, let $J(i)$ be the set formed by $i$ and by the $j$ obtained for variable $Y,u,R$; for a subset $I'$ of
$I$, similarly let $J(I')$ be the union of the $J(i)$ for $i\in I'$. On the other hand, if $I'$ is a finite subset of
$I$, let $m(I')\in I$ be an upper bound of $I'$, and for an arbitrary subset $I'$ of $I$, let $M(I')$ be the union of
the $m(I'')$, where $I''$ runs through the set of finite subsets of $I'$.

[PDF p. 415]

Suppose that the function $I'\mapsto m(I')$ is chosen so that for $I'$ reduced to one element $i$, one has $m(I')=i$,
which implies that for every subset $I'$ of $I$, one has $I'\subset M(I')$. Consider the iterates $(MJ)^n$ of the map
$MJ$ from the set of subsets of $I$ to itself, and let, for every subset $I'$ of $I$, $P(I')$ be the union of the
$(MJ)^n(I')$.

**a)** Show that for every subset $I'$ of $I$, $P(I')$ is a filtered subset of $I$ for the induced order, and that $I$
is the increasing filtered union of the $P(I')$, when $I'$ runs through the set of finite subsets of $I$.

**b)** Show that there exists a cardinal $c\in U$, depending only on the cardinal
$\operatorname{card}\operatorname{fl}(C)=a$, such that for every finite subset $I'$ of $I$, one has
$\operatorname{card}(P(I'))\leq c$. If $a$ is infinite, one may take $c=2^a$.

**c)** Show, using 6.8.7, that for every subset $I'$ of $I$ of the form $P(I_0)$, the functor $\varphi_{I'}$ on $C$
pro-represented by the pro-object $(X_i)_{i\in I'}$ is a fiber functor on $C$, and that the fiber functor $\varphi$ is
the filtered inductive limit of the functors $\varphi_{P(I_0)}$, when $I_0$ runs through the set of finite subsets of
$I$.

**d)** Conclude that there exists a small full subcategory $\Phi$ of
$\operatorname{Fib}(C)\simeq\operatorname{Fib}(\widetilde{C})$, such that every object of $\operatorname{Fib}(C)$ is a
filtered inductive limit of objects of $\Phi$. If $a$ is infinite, one may take $\Phi$ of cardinal $\leq 2^a$; if $a$ is
finite, one may of course take $\Phi=C$.

**Exercise 6.10.** Let $C$ be a $U$-site, let $D$ be a $U$-category in which small filtered inductive limits are
representable, and let $\operatorname{Fais}(C,D)$ be the category of sheaves on $C$ with values in $D$ (II 6.1). Define,
by extending (6.8.3), a "fiber functor"

```text
(6.10.1)    F |-> F_p : Fais(C, D) -> D.
```

If finite projective limits are representable in $D$, and commute with filtered inductive limits, then the preceding
functor is left exact.

[PDF p. 416]

## 7. Examples of Fiber Functors and Points of Topoi

### 7.1. Case of $\operatorname{Top}(X)$ for a Topological Space $X$

Let $x$ be a point of $X$. Regard the one-point set $\{x\}$ as a topological space, and consider the inclusion

```text
i_x : {x} -> X.
```

By virtue of 4.1.1, it defines a morphism of topoi (defined up to unique isomorphism)

```text
(7.1.1)    Top(i_x) : Top({x}) -> Top(X).
```

On the other hand, one can identify $P$ with $\operatorname{Top}(\{x\})$ (2.2), and in this way one finds a point $P_x$
of $\operatorname{Top}(X)$:

```text
(7.1.2)    P_x : P -> Top(X),
```

defined by $x$ up to unique isomorphism. The associated fiber functor is given by the well-known formula [TF], which
moreover follows immediately from I 5.1:

```text
(7.1.3)    p_x^*(F) = F_x = F_{P_x} = colim_{U containing x} F(U),
```

the limit being taken over the open neighborhoods $U$ of $x$ in $X$.

Since we know that $\operatorname{Top}(X)$ is isomorphic to $\operatorname{Top}(X_{\mathrm{sob}})$ (4.2.1), one sees
more generally that every point of $X_{\mathrm{sob}}$, i.e. every irreducible closed subset $Z$ of $X$, defines a point
of $\operatorname{Top}(X)$, or again a fiber functor on $\operatorname{Top}(X)$, which we shall still denote
$F\mapsto F_Z$. Returning to its definition by formula (7.1.3) on $X_{\mathrm{sob}}$, one finds

```text
(7.1.4)    F_Z = colim_{U meets Z} F(U),
```

[PDF p. 417]

the inductive limit being taken over the open subsets $U$ of $X$ which meet $Z$.

**7.1.5.** It is well known that the fiber functors $F\mapsto F_x$ ($x\in X$) already form a conservative family. This
is especially evident from the interpretation of sheaves on $X$ in terms of etale spaces, the fiber of $F$ at $x$ then
being none other than its fiber in the sense of spaces fibered over $X$. Note that the index set of the conservative
family of fiber functors under consideration is $X$, hence is $U$-small.

**7.1.6.** By virtue of 4.2.3, the category $\operatorname{Point}(\operatorname{Top}(X))$ is equivalent to the category
associated to the set $X_{\mathrm{sob}}$, ordered by the specialization relation. In other words: every fiber functor on
$\operatorname{Top}(X)$ is isomorphic to a fiber functor $F\mapsto F_Z$, where $Z$ is a uniquely determined element of
$X_{\mathrm{sob}}$, i.e. a uniquely determined irreducible closed subset of $X$; on the other hand, if
$Z,Z'\in X_{\mathrm{sob}}$, then the set $\operatorname{Hom}(F_Z,F_{Z'})$ is empty or reduced to one point, the latter
case occurring if and only if $Z$ is a specialization of $Z'$ in $X_{\mathrm{sob}}$, i.e. if and only if $Z\subset Z'$
as a subset of $X$. When $X$ itself is sober, one may replace $X_{\mathrm{sob}}$ by $X$ itself in these statements.

Note that the group of automorphisms of a fiber functor of $\operatorname{Top}(X)$ (opposite to the group of
automorphisms of the corresponding point of $\operatorname{Top}(X)$) is always reduced to the unit group. More
generally, 4.2.3 tells us the same thing for the automorphism group of every morphism of topoi associated to topological
spaces. This is a phenomenon very special to the particular case considered: see Example 7.2,

[PDF p. 418]

as well as VIII 7. In the case of topoi associated to "moduli problems" (cf. for example [10]), the automorphism groups
of fiber functors moreover have a remarkable interpretation, as the automorphism groups of the algebraic structures
(over algebraically closed fields) which one proposes to classify.

**7.1.7.** We have just seen how one can reconstruct a sober space $X$ (or the sober space $X_{\mathrm{sob}}$ associated
to an arbitrary topological space), at least as a set ordered by the specialization relation, from the topos
$\operatorname{Top}(X)$ (which it even suffices to know up to equivalence), as the set of isomorphism classes of points
of $\operatorname{Top}(X)$.

From what was said in 2.1, one also reconstructs the topology of $X$, i.e. the family of its open sets, as follows: for
every subobject $U$ of the final object $e$ of $E$, let $\operatorname{Pt}(U)$ be the set of $x\in X$ such that
$U_x\neq\emptyset$ (which is moreover identified, by virtue of (6.7.2), with the set of isomorphism classes of points of
the induced topos $E_{/U}$). Then $U\mapsto\operatorname{Pt}(U)$ is an isomorphism of ordered sets from the set of
subobjects of $e$ onto the set of open subsets of $X$.

**7.1.8.** The determination 7.1.6 of the category of points of the topos $\operatorname{Top}(X)$ defined by a
topological space $X$ leads one to adopt the following terminology for points $p,p'$ of an arbitrary topos $E$: one says
that $p$ is a **specialization** of $p'$, or that $p'$ is a **generalization** of $p$, when there exists a morphism from
$p'$ to $p$ (in the sense of the category $\operatorname{Point}(E)$ of 6.1). These relations are still transitive, but
using 6.8.6 one easily finds examples where $p$ and $p'$ are each a specialization

[PDF p. 419]

of the other, without $p$ and $p'$ being isomorphic (nor a fortiori equal). The category of generalizations of a point
$p$ of the topos $E$, by which one means the category $\operatorname{Point}(E)_{/p}$, plays in certain respects a role
analogous to that of passing to the localization of a scheme at a point. This role will be made precise in Chap. VI with
the construction of the topos localized of $E$ at the point $p$, whose category of points is canonically equivalent to
the category of generalizations of $p$.

**Exercise 7.1.9.** Let $E$ be a $U$-topos. Prove that $E$ is equivalent to a topos of the form $\operatorname{Top}(X)$,
where $X$ is a topological space $\in U$, if and only if it satisfies the following two conditions:

**a)** The family of subobjects of the final object $e$ is generating for the topos $E$.

**b)** $E$ has enough points (6.5). This condition is not superfluous: cf. 7.4.

Compare with 7.8 c).

**Exercise 7.1.10.** Let $X$ be a topological space equipped with a group of operators $G$ ($X,G\in U$), and let
$E=\operatorname{Top}(X,G)$ (2.5).

**a)** Show that for every object $(X',G)$ of $E$, the induced topos $E_{/(X',G)}$ is canonically equivalent to the
topos $\operatorname{Top}(X',G)$ (compare 5.7).

**b)** When $G$ acts properly and freely on $X'$ (Bourbaki, Top. Gen. Chap. III, § 4), show that the morphism of spaces
with operators

```text
(X', G) -> (X'/G, e)
```

induces (4.1.2) an equivalence of topoi.

[PDF p. 420]

**c)** Conclude from b) that there exists an object $Z$ of $E$ such that the induced topos $E_{/Z}$ is equivalent to
$\operatorname{Top}(X)$, the localization functor $E\to E_{/Z}$ being isomorphic to the functor "forget the actions of
$G$". Model the reasoning on 5.8.3.

**d)** Conclude from c) that every fiber functor on $E$ is induced, via the functor "forget the actions of $G$", by a
fiber functor on $\operatorname{Top}(X)$, hence definable by a point of $X_{\mathrm{sob}}$.

**e)** Determine the structure of the category $\operatorname{Point}(E)$ (up to equivalence) in terms of the space with
operators $(X_{\mathrm{sob}},G)$. In particular, conclude that two points of $X_{\mathrm{sob}}$ define isomorphic fiber
functors on $E$ if and only if they are conjugate under the action of $G$.

**Exercise 7.1.11.** Let $X\in U$ be a topological space. Prove that the $V$-topos $\operatorname{TOP}(X)$ (2.5) has
enough points. More precisely, for every object $X'$ of $\operatorname{TOP}(X)$ and every $x'\in X'$, define a fiber
functor $F\mapsto F_{X',x'}$ on $\operatorname{TOP}(X)$, depending only on the "germ" of the space $(X',x')$ over $X$,
and prove that this family of fiber functors is conservative (and indexed by a $V$-small index set). Show, using a
suitable filtered projective system $(X'_i,x'_i)_{i\in I}$, with $I$ not $U$-small, that one does not obtain in this way
all fiber functors of the $V$-topos $\operatorname{TOP}(X)$. Show that the set of isomorphism classes of such fiber
functors is not of cardinal $\in V$.

[PDF p. 421]

### 7.2. Points of a Classifying Topos $B_G$

Let $E$ be a $U$-topos, and let $G$ be a group of $E$, whence a classifying topos $B_G$ (2.4). If $e$ is the punctual
group, the morphisms $e\to G\to e$ define (4.5) morphisms of topoi (taking into account that $B_e\simeq E$)

```text
(7.2.1)    E -> B_G -> E,
```

whose composite is isomorphic to $\operatorname{id}_E$, whence, by passing to categories of points, functors

```text
(7.2.2)    Point(E) -> Point(B_G) -> Point(E),
```

whose composite is isomorphic to the identity.

Use the fact that the first morphism of topoi (7.2.1) is identified with a localization morphism relative to the object
$E_G=G$ of $B_G$ (5.8). It follows, by virtue of 6.7.2, that the first functor (7.2.2) is identified with the natural
"inclusion" functor

```text
(7.2.3)    Point(B_G)_{/Ehat_G} -> Point(B_G),
```

where $\widehat{E}_G$ denotes the presheaf $p'\mapsto(E_G)_{p'}$ on $\operatorname{Point}(B_G)$. Since $E_G$ evidently
covers the final object of $B_G$, its fibers $(E_G)_p$ are nonempty; it follows that (7.2.3) is essentially surjective.
This means that every fiber functor on $B_G$ is induced (up to isomorphism) by a fiber functor of $E$, via the functor
"forget the actions of $G$" $B_G\to E$. In particular, one concludes that if $E$ has enough points (resp. a small
conservative family of points), then the same is true of $B_G$.

**Remark 7.2.4.** One can go further and determine (up to equivalence) the structure of the category
$C'=\operatorname{Point}(B_G)$ in terms of the category $C=\operatorname{Point}(E)$ and of the presheaf in groups.

[PDF p. 422]

```text
Ghat : p |-> G_p : C^circ -> (Groups)
```

on it. Indeed, define a new category $C_1$, having the same objects as $C$, and such that for two objects $p,q$ of $C$,
one has

```text
Hom_{C_1}(p, q) = Hom_C(p, q) x Ghat(p),
```

composition of arrows in $C_1$ being induced by that of $C$ and by the group law of the presheaf $\widehat{G}$. Giving a
functor $\varphi_1 : C_1\to D$ to any category $D$ is then equivalent to giving a functor $\varphi : C\to D$, equipped
with an action of the presheaf $\widehat{G}$ on it (i.e. to giving, for every $p\in\operatorname{ob}C$, an action of
$\widehat{G}(p)$ on $\varphi(p)$, satisfying an evident functoriality condition for variable $p$).

Using this observation, one defines a canonical functor

```text
(7.2.4.1)    phi_1 : C_1 -> C',
```

corresponding to the functor $\varphi : C\to C'$ of (7.2.2), associating to every point $p$ of $E$ the point
$\varphi(p)$ induced on $B_G$, with the natural actions of $\widehat{G}(p)=G_p$ on the latter, coming from the actions
of $G_p$ on the $X_p$ as $X$ runs through $B_G$. We leave to the reader the task of proving that (7.2.4.1) is an
equivalence of categories, using the structure (7.2.3) of the first functor of (7.2.2), and noting that the natural
inclusion functor $C\to C_1$ admits an analogous structure, relative to the inverse image $P_1$ of the presheaf
$P'=\widehat{E}_G$ on $C'$.

[PDF p. 423]

**7.2.5.** In particular, one concludes that the isomorphism classes of points of $B_G$ correspond exactly to the
isomorphism classes of points of $E$: every point of the classifying topos $B_G$ is induced, up to nonunique
isomorphism, by a point of $E$.

In particular, when $E$ is the punctual topos $P$, so that $G$ is an ordinary group, the category
$\operatorname{Point}(B_G)$ is a connected groupoid with fundamental group $G$: every fiber functor on $B_G$ is
isomorphic (noncanonically) to the functor $\omega$ "forget the actions of $G$", and the monoid of endomorphisms of this
functor is the group $G$ (so every endomorphism of $\omega$ is an automorphism).

**Exercise 7.2.6.** a) Let $(\mathrm{Tors})$ be the category of pairs $(T,P)\in U$, with $T$ a group and $P$ a right
torsor under $T$. The functor $(T,P)\mapsto T$

```text
(7.2.6.1)    (Tors) -> (Groups)
```

is a cofibring functor. With the notation of 7.2.4, consider the functor

```text
Ghat : C^circ -> (Groups),
```

and let $D'$ be the category cofibered over $C^\circ$ inverse image of the cofibered category (7.2.6.1), and let $D$ be
the corresponding fibered category over $C$, with the same fiber categories as $D'$, so that for
$p\in\operatorname{ob}C$ one has

```text
D_p = category of right G_p-torsors.
```

Construct canonical functors

```text
(7.2.6.2)    D -> C' = Point(B_G),    C' -> D,
```

quasi-inverse to one another. In particular, conclude that the category of points of $B_G$ over a given point $p$ of $E$
is canonically equivalent to the category of right torsors under the group $G_p$.

[PDF p. 424]

b) Let $G=(G_i)_{i\in I}$ be a strict projective system of groups of the $U$-topos $E$ ($I\in U$ a filtered preordered
set), whence a classifying topos $B_G$, by modeling the definition on 2.7.1. Determine the category of points of $B_G$,
by modeling a). (NB. Replace the categories $(\mathrm{Tors})$ and $(\mathrm{Groups})$ by the categories of projective
systems indexed by $I$ of these categories.) Conclude that if $I$ admits a countable cofinal set, then every fiber
functor on $B_G$ is isomorphic to a functor induced by a fiber functor of $E$ (via the functor "forget the actions of
$G$"), the latter being determined up to nonunique isomorphism.

c) Taking $E$ to be the punctual topos, so that $G$ is an ordinary pro-group, show that the conclusion of b) is also
valid if $I$ is arbitrary, but $G$ is profinite (i.e. the $G_i$ are finite): every fiber functor is isomorphic to the
functor "forget the actions of $G$".

d) Still taking the case where $E$ is the punctual topos, give an example of a fiber functor on $B_G$, for a suitable
projective system $G=(G_i)_{i\in I}$, which is not isomorphic to the functor "forget the actions of $G$".

e) Regard $G=(G_i)$ as a group of the topos $\widehat{I}$, and let $T$ be a gerbe on $I$ with band $G$ [3]. Show how one
can "twist" the classifying topos $B_G$ by means of the gerbe $T$, to obtain a topos $B_G^T$, an inductive limit of
subcategories $B^T(i)$ equivalent (noncanonically) to the classifying topoi $B_{G_i}$. Show that the topos $B_G^T$
admits a fiber functor if and only if the gerbe $T$ is "neutral", by establishing

[PDF p. 425]

an equivalence of categories between the category of fiber functors of $B_G^T$ and the category of sections of $T$ over
$I$. Conclude, if the $G_i$ are commutative, so that gerbes on $I$ with band $G$ are classified by
$\varprojlim_I^2 G_i=H^2(I,G)$ (loc. cit.), an example of a topos (not "empty" (2.29)) of the form $B_G^T$ which has no
points. (Take an example where $\varprojlim_I^2 G_i\neq 0$.)

### 7.3. Points of the Topoi $\widehat{C}$; Examples of $U$-Topoi $\widehat{C}$ Whose Category of Points Is Not
Equivalent to a Small Category

Let $E$ be a $U$-topos, and let $(\varphi_i)_{i\in I}$ be a filtered family of fiber functors on $E$. It follows from
the exactness properties of the functors $\varinjlim$ (and of the $\varphi_i$) that the functor
$\varphi=\varinjlim\varphi_i$ is again a fiber functor: every filtered inductive limit of fiber functors is a fiber
functor. Consequently, the category $\operatorname{Fib}(E)$ admits $U$-filtered inductive limits (and the inclusion
functor $\operatorname{Fib}(E)\to\operatorname{Hom}(E,(U\text{-}\mathrm{Ens}))$ commutes with them); in other words, the
category $\operatorname{Point}(E)$ admits $U$-filtered projective limits. This fact was already used in Exercise 7.1.10
to give an example of "large" categories of fiber functors.

One can construct much simpler examples, with topoi of the form $E=\widehat{C}$, $C\in U$, using (6.8.6.4). This at once
gives examples where $\operatorname{Fib}(\widehat{C})$ is not equivalent to a category $\in U$ (i.e. where the cardinal
of the set of isomorphism classes of objects of this $U$-category is not $\in U$). This means that the category
$\operatorname{Pro}(C)$ is not equivalent to a category $\in U$. For example, it suffices to take for $D=C^\circ$ the
category of finite sets of the form $[0,n]$, where $n\geq 0$ is an

[PDF p. 426]

integer; then $\operatorname{Ind}(D)\simeq\operatorname{Pro}(C)^\circ$ is equivalent to the category of nonempty sets.
The topos $E$ is in this case the well-known category of cosimplicial sets. One could also take for $C$ the category of
nonempty finite sets; one finds that the category of points on the topos $\widehat{C}$ of simplicial sets is equivalent
to the category of profinite sets, or again to the category of compact totally disconnected spaces.

### 7.4. Nonempty Topoi Without Points

The following example is due to P. Deligne. (For another example, cf. 7.2.6 d).) Take a compact space $K$ equipped with
a measure $\mu$, and the ordered set $U$ of measurable subsets of $K$ modulo sets of measure zero. Make $U$ into a
category such that $\operatorname{ob}U=U$, the morphisms of $U$ being the "inclusion morphisms" between elements of $U$.
Make $U$ into a site by taking the pretopology for which $\operatorname{Cov}(E)$ (for $E\in U$) is formed by the
countable families of elements $E_i$ of $U$, bounded above by $E$, such that $E$ is the union of the $E_i$ modulo a set
of measure zero. One deduces a topos $\operatorname{Top}(\mu)=\widetilde{U}$, admitting the set of subobjects of the
final object as a generating family (a topos which seems to have escaped the attention of probabilists).

This topos is an "empty topos" (2.2) if and only if $\mu=0$. On the other hand, the category of points of this topos is
equivalent to the discrete category defined by the set of points $x\in K$ such that $\mu(\{x\})\neq 0$ (proof left to
the reader). It is therefore empty if $K$ admits no such points, for example if $K$ is the unit interval of the line,
with the measure induced by Lebesgue measure.

[PDF p. 427]

**Exercise 7.5 (Karoubian categories and morphisms of topoi).** (*) a) Let $C$ be a category, let $X$ be an object of
$C$, and let $p$ be an endomorphism of $X$. One says that $p$ is a **projector** if $p^2=p$. Prove that if $p$ is a
projector, then for $\operatorname{Ker}(\operatorname{id}_X,p)$ to be representable, it is necessary and sufficient that
$\operatorname{Coker}(\operatorname{id}_X,p)$ be representable, and that the two objects of $C$ thus obtained are
canonically isomorphic.

One then says that the projector $p$ **admits an image**, and
$\operatorname{Ker}(\operatorname{id}_X,p)\simeq\operatorname{Coker}(\operatorname{id}_X,p)$ is called the image of the
projector $p$; according to context, it is identified with a subobject or with a quotient object of $C$. An object
isomorphic to an $\operatorname{Im}p$, for a suitable projector $p$ in $X$, is called a direct factor of the object $X$
of $C$.

One says that $C$ is a **category with direct factors**, or a **Karoubian category**, if every projector in an object of
$C$ admits an image. If $F : C\to C'$ is a functor which commutes with kernels or cokernels, then $F$ transforms a
projector admitting an image into a projector admitting an image.

b) Show that for every category $C$, one can find a functor $\varphi : C\to\operatorname{kar}(C)$ from $C$ to a
Karoubian category (determined up to equivalence), such that for every Karoubian category $C'$, the functor

```text
f |-> f phi : Hom(kar(C), C') -> Hom(C, C')
```

is an equivalence of categories; $\operatorname{kar}(C)$ will be called the Karoubi envelope of the category $C$. (Hint:
take for $\operatorname{ob}\operatorname{kar}(C)$ the set of pairs $(X,p)$, with $X\in\operatorname{ob}C$ and $p$ a
projector in $X$, and for $\operatorname{Hom}((X,p),(Y,q))$ the subset of $\operatorname{Hom}(X,Y)$ formed by the
$f : X\to Y$ such that $f=qfp$.) Show that $\varphi$ is fully faithful.

c) Let $F : E\to E'$ be a functor from one category to another. Show that if $F$ commutes with a certain type of
inductive or projective limits, then the same is true of every direct factor of $F$. In particular, if $E$ and $E'$ are
$U$-topoi and if $F$ is an inverse image functor for a morphism of topoi $E'\to E$, then the same is true of every
direct factor of $F$; consequently, the category $\operatorname{Homtop}(E',E)$ is Karoubian, and in particular the
category $\operatorname{Point}(E)$ is Karoubian.

(*) Compare I 8.7.8.

[PDF p. 428]

d) Show that for every $U$-category $C$, the category $\operatorname{Ind}(C)$ is Karoubian (where
$\operatorname{Ind}(C)$ is formed with inductive systems of $C$ indexed by a filtered preordered set $I\in U$). (If
$C\in U$, use for example the fact (7.3) that $\operatorname{Ind}(C)$ is equivalent to the category
$\operatorname{Fib}((C^\circ)^\wedge)=\operatorname{Point}((C^\circ)^\wedge)^\circ$.) Conclude another construction of
$\operatorname{kar}(C)$ as the full subcategory of $\operatorname{Ind}(C)$ formed by the images in
$\operatorname{Ind}(C)$ of projectors of objects $X$ of $C$.

**Exercise 7.6 (essential morphisms of topoi, essential points).** a) Let $f : E\to E'$ be a morphism of topoi. Show
that the following conditions are equivalent:

1. $f_!$ exists, i.e. $f^*$ admits a left adjoint;
2. $f^*$ commutes with $U$-projective limits;
3. $f^*$ commutes with $U$-products.

One then says that $f$ is an **essential morphism** from the topos $E$ to the topos $E'$.

Show that if $f$ satisfies these conditions, then so does every direct factor of $f$. (Use 1.8 and 7.5 c).)

b) Let $E$ be a topos. An **essential point of the topos $E$** means any point $p : P\to E$ of $E$ such that $p_!$
exists. Show that if $E=\operatorname{Top}(X)$, $X$ a topological space, and if $p$ is the point of $E$ defined by an
$x\in X$, then $p$ is

[PDF p. 429]

essential if and only if $x$ admits a smallest open neighborhood $U$ (which means, if the points of $X$ are closed, that
$x$ is an isolated point of $X$). For a morphism of topoi $f : E\to F$ to be essential (a)), it is necessary that $f$
transform essential points into essential points, and this condition is also sufficient when $E$ admits enough essential
points (i.e. if the family of these points is conservative) (cf. d)).

c) For a point $p$ of the topos $E$ to be essential, it is necessary and sufficient that the associated fiber functor be
representable by an object $X$ of $E$.

For the covariant functor $\varphi : E\to(\mathrm{Ens})$ represented by a given object $X$ of $E$ to be a fiber functor
(i.e. to define a point, necessarily essential, of $E$), it is necessary and sufficient that $X$ be connected nonempty
(4.3.5), and projective (1.6: that the functor $\varphi$ transform epimorphisms into epimorphisms). (Hint: first show
that for $\varphi$ to commute with sums, it is necessary and sufficient that $X$ be connected nonempty, then use
criterion 4.9.4.)

Conclude an equivalence between the category $\operatorname{Point}_{\mathrm{ess}}(E)$ and the full subcategory $P$ of
$E$ formed by the connected nonempty projective objects.

d) Show that the topology of $P$ induced by that of $E$ is the chaotic topology. Conclude the equivalence of the
following conditions on $E$ (due to J. E. Roos [12 c), Prop. 1]):

1. the family of essential points of $E$ is conservative;
2. the full subcategory $P$ of $E$ formed by the connected nonempty projective objects is generating;
3. $E$ is equivalent to a topos of the form $\widehat{C}$, where $C$ is a category equivalent to a category $\in U$ (or,
   if preferred, $C\in U$).

(Use c) and the fact that if $P$ is generating, the natural functor $E\to\widehat{P}$ is an equivalence

[PDF p. 430]

of categories.)

e) The category of essential points of a topos $E$ is Karoubian (cf. 7.5 c)). Let $C$ be a category equivalent to a
category $\in U$. Prove that the canonical fully faithful functor (4.6.2)

```text
C -> Point(C^)
```

factors through a functor

```text
C -> Point_ess(C^)
```

which makes $\operatorname{Point}_{\mathrm{ess}}(\widehat{C})$ a Karoubi envelope (7.5 b)) of $C$. In particular, this
functor is an equivalence of categories if and only if the category $C$ is Karoubian. (Hint: using c), prove that every
isolated point of $\widehat{C}$ is isomorphic to a direct factor of some $X\in\operatorname{ob}C$.)

f) Let $C$ and $C'$ be two categories equivalent to categories $\in U$. Prove that the canonical fully faithful functor
(4.6.2)

```text
Hom(C, C') -> Homtop(C^, C'^)
```

takes its values in the full subcategory $\operatorname{Homtop}_{\mathrm{ess}}(\widehat{C},\widehat{C}')$ of essential
morphisms of topoi (a)), and that the induced functor

```text
Hom(C, C') -> Homtop_ess(C^, C'^)
```

is an equivalence of categories if and only if $C$ is empty or $C'$ is Karoubian. (Use g) below.)

g) Let $C$ be a category equivalent to a category $\in U$, and let $E$ be a topos. Define an equivalence between the
category $\operatorname{Homtop}_{\mathrm{ess}}(\widehat{C},E)$ of essential morphisms of topoi $\widehat{C}\to E$, and
the category $\operatorname{Hom}(C,\operatorname{Point}_{\mathrm{ess}}(E))$.

[PDF p. 431]

(Use e) and the fact that $\widehat{C}$ has enough essential points.)

h) Let $C$ be a finite category. Prove that every point of $\widehat{C}$ is essential, and that
$\operatorname{Point}(\widehat{C})$ is equivalent to a finite category. (Note that the Karoubi envelope of $C$ is
finite, and, using 6.8.6.1, reduce to proving that if $C$ is a finite Karoubian category, then the canonical functor
$C\to\operatorname{Pro}(C)$ is an equivalence of categories.) Using b), conclude that every morphism of topoi
$\widehat{C}\to\widehat{C}'$ is essential, and that
$\operatorname{Hom}(C,C')\to\operatorname{Homtop}(\widehat{C},\widehat{C}')$ is an equivalence if and only if $C$ is
empty or $C'$ is Karoubian.

i) Let $X$ be a topological space, and let $f : \operatorname{Top}(X)\to P$ be the morphism of topoi deduced from the
continuous map from $X$ to the punctual space. Show that $f$ is essential if and only if the space $X$ is locally
connected, i.e. satisfies the following condition: for every $x\in X$ and every open neighborhood $U$ of $x$, the
connected component of $x$ in $U$ is a neighborhood of $x$, or equivalently: for every open subset $U$ of $X$, the
connected components of $U$ are open. (Cf. 8.7 b) for a generalization.)

**Exercise 7.7 (unusual points of a classifying topos).** (*) a) Let $G$ be a monoid. For $G$ to contain an element $g$
such that $g\neq e$, $g^2=g$, it is necessary and sufficient that the classifying topos $B_G$ admit an essential point
which is not isomorphic to the banal point (corresponding to the fiber functor "forget the actions of $G$"). (Use 7.6
e).)

b) Let $G$ be the additive monoid of integers $\geq 0$. Show that every essential point of the classifying topos $B_G$
is isomorphic to the banal point. Construct a point of $B_G$ which is not isomorphic to the banal point. Show that the
category $\operatorname{Point}(B_G)$ is not equivalent to a category $\in U$.

(*) Cf. also 7.2.6 d).

**Exercise 7.8 (topology on $\operatorname{Point}(E)$, and topoi associated to ordered sets).** a) Let $E$ be a topos.
Denote by $\operatorname{Point}'(E)$ the set of classes, up to isomorphism, of points of $E$. For every open $U$ of $E$,
let $U'$

[PDF p. 432]

be the set of classes of points $p$ of $E$ such that $U_p\neq\emptyset$. Show that $U\mapsto U'$ is an increasing map
from the ordered set $\operatorname{Ouv}(E)$ of opens of $E$ to the set of subsets of $X=\operatorname{Point}'(E)$, and
that this map commutes with finite infima and arbitrary suprema. Conclude that the set of subsets of $X$ of the form
$U'$ defines a topology on $X$ (called the canonical topology on the set of classes of points of the topos $E$). Show
that if $E$ has enough points, the map $U\mapsto U'$ is an isomorphism from the ordered set $\operatorname{Ouv}(E)$ to
the ordered set $\operatorname{Ouv}(X)$.

b) Let $O\in U$ be an ordered set admitting finite infima and arbitrary suprema, which therefore defines a category
$\operatorname{cat}(O)$ having finite products and arbitrary sums. We shall say that a family of morphisms $U_i\to U$
with common target $U$ is covering if $U$ is the supremum of the $U_i$. Assuming that in $\operatorname{cat}(O)$ sums
are universal, i.e. that in $O$ arbitrary suprema commute with infima, this defines on $\operatorname{cat}(O)$ a
topology making it a site, whence a topos $\widetilde{\operatorname{cat}(O)}$, also denoted simply $\widetilde{O}$. Show
that $O$ is canonically isomorphic to $\operatorname{Ouv}(\widetilde{O})$.

Show that the category $\operatorname{Homtop}(E,\widetilde{O})$ is equivalent to the category associated to the ordered
set of morphisms of ordered sets $O\to\operatorname{Ouv}(E)$ which commute with finite infima and arbitrary suprema.
(Use criterion 4.9.4.) If $O'$ is an ordered set satisfying the same conditions as $O$, conclude that
$\operatorname{Homtop}(\widetilde{O},\widetilde{O}')$ is equivalent to the category associated to the ordered set of all
morphisms of ordered sets $O\to O'$ which commute with finite infima and arbitrary suprema.

[PDF p. 433]

c) Show that for the topos $E$ to be equivalent to a topos of the form $\widetilde{O}$ with $O$ as in b), it is
necessary and sufficient that the family of opens of $E$ be generating in $E$. For it to be equivalent to a
$\operatorname{Top}(X)$ for $X\in U$, it is necessary and sufficient that it satisfy the preceding condition and have
enough points. Assuming the first condition is realized, express the second in terms of the structure of the ordered set
$O=\operatorname{Ouv}(E)$, using the last assertion of b).

d) Define a canonical morphism of topoi

```text
E -> Ouv(E)~
```

which is universal (up to equivalence) for morphisms from $E$ to topoi generated by their opens (cf. c)).

e) Let $X'$ be a small subset of $X=\operatorname{Point}'(E)$, endowed with the topology induced by that of $X$. Define
a canonical morphism of topoi

```text
Ouv(E)~ -> Top(X'),
```

which is an equivalence when the family $X'$ of points of $E$ is conservative. Then conclude a canonical morphism of
topoi

```text
E -> Top(X').
```

Give a universal characterization (up to equivalence) of this morphism of topoi for morphisms from the topos $E$ to
topoi of the form $\operatorname{Top}(Y)$. (Note in this connection that, up to equivalence, $\operatorname{Top}(X')$
does not depend on the small conservative family of fiber functors chosen, or equivalently (4.2), that
$X'_{\mathrm{sob}}$ does not depend up to homeomorphism on the choice of such a family.)

[PDF p. 434]

f) Suppose that the category $\operatorname{Point}(E)$ is not equivalent to a small category (cf. 7.3), and that $E$
admits a small conservative family of fiber functors. Show that if such a family is taken large enough, the subset $X'$
of $\operatorname{Point}(E)$ that it defines is not a sober topological space for the induced topology.

g) For the relations with Exercise 7.6, cf. 8.

## 8. Localization. Opens of a Topos

### 8.1. Stability Under Base Change

Let $C$ be a category, and let $T(X)$ be a relation involving an object $X$ of $C$. The relation $T(X)$ is said to be
stable under base change (in $X$) if for every morphism $X'\to X$ of $C$, the relation $T(X)$ implies $T(X')$. This is
equivalent to saying that the full subcategory $R$ of $C$ formed by the objects $X$ of $C$ such that $T(X)$ holds is a
sieve (I 4.1).

**Remark 8.1.1.** Suppose that $C$ is a $U$-category (I 1.1), so that $C$ can be identified with a full subcategory of
$\widehat{C}$ (I 1.4). It is sometimes convenient to extend the definition of the relation $T$ on $\operatorname{ob}C$
to a relation $\widehat{T}$ concerning an object $F$ of $\widehat{C}$, by letting $\widehat{T}(F)$ denote the relation:
for every arrow $X\to F$ in $\widehat{C}$, with $X\in\operatorname{ob}C$, one has $T(X)$. The relation $\widehat{T}(F)$
is evidently still stable under base change in $F$. Still denoting by $R$ the subobject of the final object $e$ of
$\widehat{C}$ defined by the sieve $R$ of $C$ (I 4.2.1), the relation $\widehat{T}(F)$ can also be expressed by
$\operatorname{Hom}_{\widehat{C}}(F,R)\neq\emptyset$, i.e. it means that the unique morphism $F\to e$ factors through
the subobject $R$ of $e$.

### 8.2. Relations of Local Nature

Now suppose that $C$ is a site. A relation $T(X)$ in one argument $X\in\operatorname{ob}C$ is said to be stable under
descent if for every

[PDF p. 435]

covering family $(X_i\to X)_{i\in I}$ of an object $X$ of $C$, the relation "$T(X_i)$ for every $i\in I$" implies the
relation $T(X)$. The relation $T$ is called a relation of local nature if it is stable under base change (8.1) and
stable under descent.

When $C$ is a $U$-category, and $T$ is already assumed stable under base change, i.e. is definable by a sieve $R$ of
$C$, which will be identified with a subpresheaf of the final presheaf on $C$, one immediately sees that $T$ is of local
nature if and only if $R$ is a sheaf. Thus, relations of local nature in one argument $X\in\operatorname{ob}C$
correspond exactly to subsheaves of the final sheaf of $C$, i.e. to subobjects of the final object of the topos
$\widetilde{C}$. They therefore depend essentially only on the topos $\widetilde{C}$ defined by the site $C$ (like all
important notions associated to a site!). In terms of the subsheaf $R$ of the final sheaf, the relation $T(X)$ is
expressed as $\operatorname{Hom}(\varepsilon(X),R)\neq\emptyset$. It extends canonically to the relation
$T(F) : \operatorname{Hom}(F,R)\neq\emptyset$ on the topos $\widetilde{C}$.

**Remark 8.2.1.** With the notation introduced in 6.1.1, for a presheaf $F$ on $C$, since
$\operatorname{Hom}(F,R)=\operatorname{Hom}(a(F),R)$, the relation $T(F)$ is equivalent to the relation $T(a(F))$.

**Definition 8.3.** An open of a $U$-topos $E$ means any subobject of the final object $e_E$ of $E$; if $X$ is an object
of $E$, one sometimes calls an open of $X$ any open of the induced topos $E_{/X}$, i.e. any subobject of $X$. An open of
a $U$-site $C$ means an open of the associated $U$-topos $\widetilde{C}$.

Note that, since final objects of $E$ are canonically isomorphic, the ambiguity introduced in 8.3 by the choice of $e_E$
is harmless;

[PDF p. 436]

one can also, more intrinsically but less manageably in practice, define the opens of $E$ as the full subcategories $R$
of $E$ such that the relation $F\in\operatorname{ob}R$ for an object $F$ of $E$ is a relation of local nature.
Similarly, the opens of a $U$-site $C$ correspond bijectively to the full subcategories of $C$ such that the relation
$F\in\operatorname{ob}R$ for an object of $C$ is of local nature; this notion is therefore essentially independent of
the chosen universe $U$. Finally, by virtue of what was said in 8.2, a relation of local nature on a topos (or on a
site) is essentially the same thing as an open of that topos (or site).

### 8.4. Examples of Opens

**8.4.1.** Let $X$ be a topological space, and interpret $\operatorname{Top}(X)$ (2.1) as the category of etale spaces
over $X$. Since it is clear that monomorphisms in $\operatorname{Top}(X)$ are injective maps, it follows that the opens
of the topos $\operatorname{Top}(X)$ are identified with the open subsets of the space $X$. More generally, the opens of
a topos $\operatorname{Top}(X,G)$ (2.4) are identified with the open subsets of $X$ invariant under the action of $G$.

**8.4.2.** The opens of a $U$-topos $E$ form a $U$-small set (I 7.4), ordered by inclusion, admitting arbitrary suprema
and finite infima. It admits the initial object (or "empty object") $\emptyset$ as smallest element, and the final
object $e_E$ of $E$ as greatest element. These two elements are identical only if $E$ is an "empty topos" (2.2).

**8.4.3.** Let $G$ be a monoid in $E$, whence a topos $B_G$ (2.4), the category of objects of $E$ on which $G$ acts on
the left. The final object $e_{B_G}$ of $B_G$ is

[PDF p. 437]

the final object $e_E$ of $E$ with trivial action of $G$. One therefore sees that the ordered set of opens of $B_G$ is
canonically isomorphic to the category of opens of $E$. In particular, if $E$ is the punctual topos, so $G$ is an
ordinary monoid, the set of opens of $B_G$ is exactly formed by two elements, namely $\emptyset$ and $e$.

**8.4.4.** If $E$ is a topos of the form $\widehat{C}$, where $C$ is a $U$-category, then (8.1) the ordered set of opens
of $E$ is isomorphic to the ordered set of sieves of $C$.

**8.4.5.** Let $X$ be a sober nondiscrete topological space. Show that $\operatorname{TOP}(X)$ (2.5) has opens which do
not come from opens of $X$, i.e. from opens of $\operatorname{Top}(X)$, by inverse image by means of the canonical
morphism (4.10.1)

```text
TOP(X) -> Top(X).
```

### 8.5. Examples of Relations of Local Nature

For every object $X$ of the topos $E$, denote by $F\mapsto F_X$ the localization functor $j_X^* : E\to E_{/X}$ (5.2).

**8.5.1.** Let $u : F\to G$ be a morphism of $E$. The relation in the argument $X\in\operatorname{ob}E$,

```text
u_X : F_X -> G_X is a monomorphism
  (resp. an epimorphism, resp. an isomorphism),
```

is a relation of local nature. In particular, if $G$ is a group of $E$, the relation "$G_X$ is the unit group over $X$"
is of local nature; the open of $E$ corresponding to it is called the cosupport of the group $G$.

[PDF p. 438]

**8.5.2.** Let $u,v : F\to G$ be two morphisms of $E$. The relation in the argument $X\in\operatorname{ob}E$,

```text
u_X = v_X,
```

is a relation of local nature. In particular, if $G$ is a group of $E$, and $u$ a section of $G$ (4.3.6), the relation
in $X$

```text
the section u_X of the group G_X of E_{/X} is zero
```

is of local nature; the open of $E$ corresponding to it is called the cosupport of the section $u$ of the group $G$.

**Remark 8.5.3.** When $E=\operatorname{Top}(X)$, the cosupport of a sheaf of groups $G$, resp. of a section of such a
sheaf $G$, is none other than the open subset of $X$ complementary to the support of $G$, resp. the support of $u$, in
the classical terminology [TF].

**8.5.4.** Let $P(f)$ be a relation in the argument $f\in\operatorname{Fl}(C)$, where $C$ is a site. When fiber products
are representable in $C$, the relation $P(f)$ is said to be stable under base change (resp. stable under descent, resp.
of local nature) on the target (or on the base, or "below") if for every morphism $f : X\to Y$ of $C$, the relation in
the argument $Y'\in\operatorname{ob}C_{/Y}$,

```text
the morphism f' : X' = X x_Y Y' -> Y'
deduced from f by base change by the structural morphism Y' -> Y
satisfies P(f')
```

is stable under base change, resp. stable under descent, resp. is of local nature.

When the topology of $C$ is defined by means of a pretopology, the relation $P(f)$ is said to be of local nature on the
source (or "above") if for every morphism $f : X\to Y$ of $C$ and every family

[PDF p. 439]

$(g_i : X_i\to X)_{i\in I}\in\operatorname{Cov}(X)$, the relation $P(f)$ is equivalent to the relation "$P(fg_i)$ for
every $i\in I$". When $\operatorname{Cov}(X)$ is formed by all covering families of $C$, this condition therefore also
means that the relation in the object $X'$ of the induced site $C_{/X}$,

```text
P(fg), where g : X' -> X is the structural morphism,
```

is of local nature. Note that if the relation $P(f)$ is of local nature above, it is a fortiori of local nature below.

**8.5.5.** Take for example $C=(\mathrm{Sch})$, category of schemes $\in U$, with the faithfully flat quasi-compact
topology (SGA 3 IV 6.3) or a less fine topology. Then each of the following properties of a morphism is of local nature
below:

- surjective;
- radicial;
- universally open;
- universally closed;
- proper;
- quasi-compact;
- quasi-compact and dominant;
- universal homeomorphism;
- separated;
- quasi-separated;
- locally of finite type;
- locally of finite presentation;
- of finite type;
- of finite presentation;
- an isomorphism;
- a monomorphism;
- an open immersion;
- a closed immersion;
- a quasi-compact immersion;
- affine;
- quasi-affine;
- finite;
- quasi-finite;
- integral;
- flat;
- faithfully flat;
- unramified;
- smooth;
- etale.

(EGA IV 2.6.4, 2.7.1 and EGA IV 17.7.1). On the other hand, endow $(\mathrm{Sch})$ with the pretopology for which, for
every scheme $X\in U$, $\operatorname{Cov}(X)$ is formed by the families of morphisms $(f_i : X_i\to X)_{i\in I}$ which
are surjective and such that the $f_i$ are flat and locally of finite presentation. Then each of the following
properties is of local nature above:

- locally of finite type;
- locally of finite presentation;
- of finite type;
- flat;
- unramified;
- smooth;
- etale.

(EGA IV 17.7.5, 17.7.7).

**Exercise 8.6.** Let $f : E\to F$ be a morphism of $U$-topoi. Consider the relation in the argument
$X\in\operatorname{ob}F$: the induced morphism $E_{/f^*(X)}\to F_{/X}$ is an equivalence of topoi. Prove that this
relation is of local nature.

**Exercise 8.7 (partitions of a topos, sum of topoi).** Let $E$ be a $U$-topos. A family $(e_i)_{i\in I}$ of opens of
$E$, i.e. of subobjects of the final object $e$ of $E$, is called a partition of $e$ (or also of the topos $E$) if the
canonical morphism $\coprod_{i\in I}e_i\to e$ is an isomorphism, i.e. (II 4.6.2) if $e$ is the supremum of the $e_i$,
and if $i\neq j$ implies $e_i\cap e_j=\emptyset$.

a) Show that for the family $(e_i)_{i\in I}$ of objects of $E$ to be a partition of $E$, it is necessary and sufficient
that the functor

```text
(8.7.1)    E -> product_{i in I} E_{/e_i}
```

defined by the localization functors $E\to E_{/e_i}$ be an equivalence of categories.

b) Conversely, let $(E_i)_{i\in I}$ be a family of $U$-topoi, with $I\in U$. Prove that $E=\prod_{i\in I}E_i$ is a
$U$-topos (which will be called the sum topos of the family of topoi $(E_i)_{i\in I}$). Define a partition
$(e_i)_{i\in I}$ of $E$ and equivalences of categories $E_{/e_i}\simeq E_i$, in such a way that the projection functors
$E\to E_i$ are identified with the localization functors $E\to E_{/e_i}$.

c) Let $E$ be the sum topos of the family of topoi $(E_i)_{i\in I}$. Show that for every $i\in I$ the projection functor
$E\to E_i$ is of the form $u_i^*$, where

```text
(8.7.2)    u_i : E_i -> E
```

[PDF p. 441]

is a morphism of topoi. Prove that for every $U$-topos $F$, the functor

```text
(8.7.3)    Homtop(E, F) -> product_{i in I} Homtop(E_i, F)
```

is an equivalence of categories.

d) Let $(e_i)_{i\in I}$ be a partition of the topos $E$. For every morphism of topoi $g : F\to E$, the family
$(g^*(e_i))_{i\in I}$ is a partition of $F$, and the induced morphisms $g_i : F_{/g^*(e_i)}\to E_{/e_i}$ make it
possible to reconstruct $g$ (up to unique isomorphism), the functor $g^*$ being identified with the cartesian product of
the functors $g_i^*$ (taking into account the equivalences of type (8.7.1)). Conclude a complete description of the
category $\operatorname{Homtop}(F,E)$ in terms of the categories of the form $\operatorname{Homtop}(F',E_i)$, where $F'$
is a topos of the form $F_{/e'}$ ($e'$ a direct summand of the final object of $F$) and $E_i=E_{/e_i}$.

e) In particular, if $F$ is connected nonempty (cf. 4.3.5), i.e. if for every partition $(f_i)_{i\in I}$ of $F$ there
exists one and only one $i\in I$ such that $f_i\neq\emptyset$, prove that the canonical functor

```text
(8.7.4)    coproduct_{i in I} Homtop(F, E_i) -> Homtop(F, E)
```

deduced from the morphisms of topoi (8.7.2) is an equivalence of categories. More particularly, the family of morphisms
of topoi (8.7.2) induces an equivalence of categories

```text
coproduct_{i in I} Point(E_i) -> Point(E).
```

[PDF p. 442]

f) A subset $I$ of the set of opens of $E$ is called a reduced partition of $E$ if the identical family $(e)_{e\in I}$
indexed by $I$ is a partition, and if the $e$ are $\neq\emptyset$. Show that the refinement relation (I 4.3.2) between
reduced partitions makes the set $P$ of reduced partitions into a $U$-small ordered set, such that the supremum of two
elements of $P$ exists. One thus obtains a strict projective system of sets, which will be considered as a pro-set and
denoted $\pi_0(E)$. It is called the pro-$\pi_0$ of the topos $E$.

g) Prove that $\pi_0(E)$ pro-represents the functor

```text
Gamma_E(T) = Gamma(E, T) : (U-Ens) -> (U-Ens)
```

associated to the canonical morphism $f : E\to P$ from $E$ to the punctual topos $P$ (4.3). In particular, for this
functor to be representable, it is necessary and sufficient that $\pi_0(E)$ be essentially constant, i.e. isomorphic (as
a pro-set) to an "ordinary" set, which will still be denoted $\pi_0(E)$. For $\pi_0(E)$ to be reduced to one point, it
is necessary and sufficient that $E$ be "connected nonempty". For $\pi_0(E)$ to be empty, it is necessary and sufficient
that $E$ be the "empty topos" (2.2).

h) Suppose $E$ quasi-compact, i.e. that every covering of its final object $e$ admits a finite subcovering. Show that
then $\pi_0(E)$ is a profinite set, and may consequently be identified (by means of the well-known equivalence of
categories between pro-objects of the category of finite sets and compact totally disconnected spaces) with a compact
totally disconnected space, which will also be denoted $\pi_0(E)$.

i) Let $X$ be a topological space, and let $\pi_0(X)$ be the set of connected components of $X$, regarded as a constant
pro-set. Define a

[PDF p. 443]

canonical morphism of pro-sets

```text
(8.7.5)    pi_0(X) -> pi_0(Top(X)),
```

or equivalently, a canonical map

```text
(8.7.6)    pi_0(X) -> lim pi_0(Top(X)).
```

Show that the first morphism is an isomorphism if and only if $X$ is homeomorphic to a sum space of connected spaces
(which is the case in particular if $X$ is locally connected).

j) Suppose that $X$ is a quasi-compact scheme. Prove that (8.7.5) is then bijective.

k) Establish the "functorial character" in $X$ of the morphisms (8.7.5) and (8.7.6), first making precise the meaning of
this expression.

l) (Compare 7.6 i).) Show that the following two conditions on the $U$-topos $E$ are equivalent:

1. The canonical morphism from $E$ to the punctual topos is "essential" (Exercise 7.6 a)), i.e. the functor
   $T\mapsto\Gamma(E,T)$, from $(U\text{-}\mathrm{Ens})$ to itself, commutes with products indexed by sets $\in U$.
2. For every object $X$ of $E$, the induced topos $E_{/X}$ has a $\pi_0$ which is an ordinary set, i.e. $X$ is
   isomorphic to the sum of a family of connected objects of $E$.

One then says that $E$ is a locally connected topos (compare 8.7.5).

**Exercise 8.8 (dominant morphisms of topoi).** a) Let $f : E'\to E$ be a morphism of topoi. Show the equivalence of the
following conditions:

1. $f^*(\emptyset_E)=\emptyset_{E'}$. The $\emptyset$ denote the initial objects of $E$, $E'$.

[PDF p. 444]

2. For every object $X$ of $E$ which is "nonempty", i.e. not isomorphic to $\emptyset$, $f^*(X)$ is a nonempty object of
   $E'$.
3. As in 2, with $X$ a subobject of the final object $e$ of $E$, i.e. $X$ an open of the topos $E$.

The morphism $f$ of topoi is then called dominant.

b) Let $f : X'\to X$ be a continuous map of topological spaces, whence a morphism of topoi
$\operatorname{Top}(f) : \operatorname{Top}(X')\to\operatorname{Top}(X)$ (4.1). Show that $\operatorname{Top}(f)$ is
dominant if and only if $f$ is dominant, i.e. $f(X')$ is dense in $X$.

c) Show that if $f : E'\to E$ is a "conservative" morphism of topoi (6.4.0), i.e. such that $f^*$ is faithful, then $f$
is dominant. Show that the converse is not necessarily true, even for a localization morphism $E_{/U}\to E$, where $U$
is an open of the topos $E$. (Show that in this case $f$ is conservative only if $U$ is the final object of $E$ (hence
if $f$ is an equivalence of topoi), and use Example b).)

d) Let $f : X'\to X$ be an arrow in a topos $E$. We say that $f$ is a dominant morphism in the topos $E$ if the
corresponding morphism of induced topoi $E_{/X'}\to E_{/X}$ (5.5.2) is dominant. Show that this property depends only on
the image $f(X')$ of $X'$ in $X$, as an element of the ordered set $\operatorname{Ouv}(X)$ of subobjects of $X$. Show
that the morphism $E_{/X'}\to E_{/X}$ is conservative if and only if $f$ is covering.

[PDF p. 445]

## 9. Subtopoi and Embeddings

### 9.1. Embeddings and Subtopoi

**Definition 9.1.1.**

a) A morphism of topoi $f : F\to E$ is called an embedding if the functor $f_* : F\to E$ is fully faithful (i.e. if the
adjunction morphism $\operatorname{id}_F\to f^*f_*$ is an isomorphism).

b) A subtopos of a topos $E$ means a strictly full subcategory $E'$ of $E$ such that the inclusion functor $a : E'\to E$
is of the form $i_*$, where $i : E'\to E$ is a morphism of topoi (i.e. (3.1.1) $a$ admits a left adjoint $i^*$ which is
left exact). The morphism $i$ is called the inclusion morphism of the subtopos $E'$ into $E$.

**Remark 9.1.2.**

a) It is clear that the inclusion morphism of a subtopos is an embedding, and that a subcategory $E'$ of the topos $E$
is a subtopos if and only if it is the essential image of a direct image functor $g_*$ associated to a morphism of topoi
$g : F\to E$ which is an embedding.

b) It follows immediately from the definitions that a morphism of topoi $f : F\to E$ is an embedding if and only if it
is isomorphic to a composite morphism

```text
F --g--> E' --i--> E,
```

where $g$ is an equivalence of topoi and $i$ is the inclusion morphism of a subtopos $E'$ of $E$. This latter is
uniquely determined by the preceding conditions, as the essential image of $f_*$, and the preceding factorization is
also unique up to unique isomorphism. Of course, in practice one should identify, by means of $g$, $F$ with the subtopos
$E'$ of $E$ (compare IV 3.4.1).

c) An equivalence of topoi (3.4) $u : E\simeq E_1$ defines in the evident way a bijection between the set of subtopoi of
$E$ and the set of subtopoi of $E_1$. Indeed, since $u_*$ is an equivalence of

[PDF p. 446]

categories, it establishes a bijection between the set of strictly full subcategories of $E$ and the set of strictly
full subcategories of $E_1$ (to $E'\subset E$ corresponding the essential image $E'_1$ of $u_*(E')$), and one
immediately checks that $E'$ is a subtopos of $E$ if and only if $E'_1$ is a subtopos of $E_1$.

Thus, for the study of subtopoi, one may reduce to the case where $E$ is of the form $\widetilde{C}$, with $C$ a small
site. In this case, it follows from II 5.5 that a strictly full subcategory $E'$ of $E$ is a subtopos if and only if the
inclusion functor $a : E'\to E$ admits a left adjoint which is left exact (this therefore already implies that $E'$ is a
topos), and that the set of these subtopoi is in bijective correspondence with the set of topologies $T'$ on $C$ which
are finer than the given topology $T$ of $C$, by associating to any such $T'$ the strictly full subcategory
$(C,T')^\sim$ of $\widetilde{C}$, formed by the sheaves for the topology $T'$.

This shows at the same time, for any $U$-topos $E$: a strictly full subcategory $E'$ of $E$ is a subtopos if and only if
the inclusion functor $a : E'\to E$ admits a left adjoint which is left exact; the ordered set $S(E)$ of subtopoi of $E$
is $U$-small, and every subset of $S(E)$ admits a supremum and an infimum.

d) If $E'$ and $E''$ are two subtopoi of the topos $E$, their intersection is a subtopos of $E$. Indeed, since this
intersection is strictly full, we are reduced to the case where $E$ is of the form $\widetilde{C}$. With the notation of
b), $E'$ and $E''$ then correspond to two topologies $T'$, $T''$ on $C$ finer than $T$, and it suffices to see that
$E'\cap E''$ is then the category of sheaves for the topology $T'''$ which is the supremum of $T'$ and $T''$.

Let us indicate the proof of this fact (which should have appeared as a corollary after II 4.4 or II 5.5.1). Let $E'''$
be the category of sheaves for $T'''$, evidently contained in $E'$ and $E''$, hence in $E'\cap E''$. For every full
subcategory $D$ of $E$, let $t(D)$ be the finest topology among those for which the elements of $D$ are sheaves (II
2.2). The inclusions $E'''\subset E'\cap E''\subset E',E''$ evidently imply

[PDF p. 447]

$t(E'), t(E'') < t(E'\cap E'') < t(E''')$; on the other hand (II 4.4.1) we have $t(E') = T'$, $t(E'') = T''$,
$t(E''') = T'''$, so that the preceding inequalities and the definition of $T'''$ as supremum imply that
$T''' = t(E'\cap E'')$, hence $E'\cap E''\subset E'''$, q.e.d.

More generally, this argument shows that if $T'$ is a topology which is the supremum of an arbitrary family of
topologies $(T_i)$, the category $E'$ of sheaves for $T'$ is the intersection of the categories $E_i$ of sheaves for the
$T_i$. We conclude in particular:

**Proposition 9.1.3.** Let $E$ be a topos. Then for every family of subtopoi $(E_i)_{i\in I}$ of $E$, the intersection
$\bigcap_i E_i$ is a subtopos of $E$.

**Proposition 9.1.4.** Let $i : E'\to E$ be an embedding of topoi, and let $F$ be a topos. The functor

```text
(9.1.4.1)    f |-> i f : Homtop(F, E') -> Homtop(F, E)
```

is fully faithful, and its essential image is formed by the morphisms of topoi $g : F\to E$ such that the essential
image of $g_*$ is contained in that of $i_*$.

Indeed, consider the evident commutative diagram

```text
Homtop(F, E') -> Homtop(F, E)
     |              |
     v              v
Hom(F, E')   ->    Hom(F, E),
```

where the vertical arrows are the functors $h\mapsto h_*$, which are fully faithful by the definition of $\operatorname
{Homtop}$ (IV 3.2). On the other hand the second horizontal arrow $G\mapsto i_*G$ is fully faithful, since $i_*$ is, and
therefore the first horizontal arrow is fully faithful as well.

It remains to prove the characterization of the essential image of (9.1.4.1). The necessity of the condition is evident
from the formula $(if)_* = i_*f_*$, and it remains to prove that if the essential image of $g_*$ is contained in that of
$i_*$, i.e. if one can write $g_* = i_*f_*$, with $f_* : F\to E'$ a functor, then $g$ lies in the essential image of
(9.1.4.1). This is equivalent to saying that $f_*$ admits a left adjoint which is left exact.

[PDF p. 448]

But it is clear that $f_*$ admits $g^*i_*$ as left adjoint, and this functor is left exact, as a composite of the left
exact functors $g^*$ and $i_*$, q.e.d.

For a converse of 9.1.4, see Exercise 9.1.6.

Taking $F$ to be the punctual topos (IV 2.2), we deduce in particular from 9.1.4:

**Corollary 9.1.5.** If $f : E'\to E$ is an embedding morphism of topoi, the corresponding functor

```text
(9.1.5.1)    Point(f) : Point(E') -> Point(E)
```

is fully faithful.

**Exercise 9.1.6 (embeddings of topoi and 2-monomorphisms).** Let $i : E'\to E$ be a morphism of topoi.

a) If $F$ and $G$ are two topoi over $E'$, define (with the notation of 5.14 a)) a canonical functor

```text
(9.1.6.1)    i o - : Homtop_{E'}(F, G) -> Homtop_E(F, G).
```

b) Suppose that $i$, as a 1-arrow of the 2-category of $V$-$U$-topoi (3.3.2), is a 2-monomorphism, i.e. such that for
every $U$-topos $F$ which is an element of $V$, the functor (9.1.4.1) is fully faithful. Show that for every pair of
$U$-topoi $F$, $G$ (not necessarily $\in V$) the functor (9.1.6.1) is fully faithful.

c) Show that $i$ is an embedding if and only if $i$ is a 2-monomorphism. (For sufficiency, apply b) to induced topoi
$E'_{/Y'}$ and $E_{/Y}$, and use 5.14 c).)

d) Let $g : F\to E$ be a morphism of topoi, and suppose that the 2-fiber product (5.11) $F' = F\times_E E'$ exists (a
condition always satisfied, as P. Deligne has shown). Let $j : F'\to F$ be the projection morphism. Prove that if $i$ is
an embedding, then so is $j$. (Use c), and note that the stability of the notion of 2-monomorphism under 2-base change
is formal.)

In the case where $E'$ is a subtopos of $E$ and $i : E'\to E$ is the canonical inclusion morphism, the essential image
of $F'$ by $j_*$ (which is a subtopos of $F$ and which

[PDF p. 449]

does not depend on the indeterminacy in the construction of a 2-fiber product) is called the subtopos of $F$ inverse
image by $g : F\to E$ of the subtopos $E'$ of $E$.

e) With the notation at the end of d), choose as 2-fiber product the subtopos of $F$ inverse image of the subtopos $E'$
of $E$. Let $X$ be an object of $F$. Show that in order for $X$ to belong to $F'$, it is necessary that it satisfy the
following condition: for every object $U$ of $F$, denoting by $g_U : F_{/U}\to E$ the morphism of topoi induced by $g$,
we have $g_{U*}(X|U)\in \operatorname{ob} E'$, where $X|U = (X\times U\to U)$ is the "restriction of $X$ to $U$". (NB:
one may note that if $i_U : F_{/U}\to F$ is the canonical inclusion, then $g_U = g i_U$, whence
$g_{U*}(X|U) = g_* i_{U*}(X|U) = g_*(\operatorname{Hom}(U,X))$, where $\operatorname{Hom}(U,X)$ is the object defined in
10.1 below.)

**Problem.** Conversely, is the preceding condition on $X$ sufficient for $X$ to belong to $F'$? This is equivalent to
asking whether the strictly full subcategory of $F$ formed by these objects $X$ is a subtopos of $F$.

f) Let $X$ be an object of $E$, let $X' = i^*(X)$, and let $i_{/X} : E'_{/X'}\to E_{/X}$ be the morphism of topoi
induced by $i$ (5.10.1). Show that if $i$ is an embedding, then so is $i_{/X}$. (Use d) and 5.11.) Conversely, if
$(X_\alpha)$ is a family of objects covering the final object, and if for every $\alpha$, $i_{/X_\alpha}$ is an
embedding, then so is $i$.

**Exercise 9.1.7 (subtopoi and multiplicative sets of arrows).** a) Let $i : E'\to E$ be a morphism of topoi, let $S$ be
the set of arrows $u$ of $E$ such that $i^*(u)$ is an isomorphism, and consider the canonical functor induced by $i^*$
(cf. [2, Chap. I] or VI):

```text
(9.1.7.1)    phi : E[S^{-1}] -> E'.
```

Show that $i$ is an embedding if and only if the preceding functor $\phi$ is an equivalence of categories, and in this
case $S$ admits both a left calculus of fractions and a right calculus of fractions. (Use [2, Chap. I 1.3].) In this
case, the essential image of $i_*$ is recovered from $S$ as formed by the $X\in \operatorname{ob} E$ such that for

[PDF p. 450]

every $u : Y\to Y'$ in $S$, $\operatorname{Hom}(u,X) : \operatorname{Hom}(Y',X)\to \operatorname{Hom}(Y,X)$ is
bijective.

b) We now suppose that $i$ is an embedding. Show that for every topos $F$, the functor

```text
r^* |-> r^* i^* : Hom(E', F) -> Hom(E, F)
```

induces an equivalence between the category of the $r^*$ coming from morphisms of topoi $r : F\to E'$ (i.e. left exact
and admitting a right adjoint) and the category of functors $g^* : E\to F$ coming from morphisms of topoi $g : F\to E$,
and such that $g^*$ transforms objects of $S$ into isomorphisms.

c) Let $S$ be a subset of $\operatorname{Fl} E$, where $E$ is a $U$-topos. Show that $S$ is associated with a subtopos
$E'$ of $E$ by the procedure of a) if and only if $S$ satisfies the following conditions:

**ST 1)** $S$ contains the invertible arrows, and is stable under composition and base change.

**ST 2)** If a composite $vu$ is in $S$, then $u\in S$ if and only if $v\in S$.

**ST 3)** If $u : X\to Y$ is such that there exists a covering family $(Y_i\to Y)_{i\in I}$ for which
$u_i : X_i = X\times_Y Y_i\to Y_i$ is in $S$ for every $i\in I$, then $u\in S$.

Show that one obtains in this way a bijective correspondence between the set of subtopoi $E'$ of $E$ and the set of
subsets $S$ of $\operatorname{Fl} E$ satisfying conditions ST 1), ST 2), and ST 3). (Given $S$, associate to it a
$U$-topology $T'$, finer than the canonical topology $T$ of $E$, whose covering families $(X_i\to X)_{i\in I}$ are those
for which the inclusion $X'\to X$ of the image of the $X_i$ belongs to $S$. Show that the category of sheaves for $T'$
is equivalent to a subtopos $E'$ of $E$, and use II 4.4 to prove that this subtopos gives back $S$.)

d) Show that $S$ is known once one knows the part $S_0$ of $S$ formed by the monomorphisms. Show that the map
$S\mapsto S_0$ establishes a bijection between the set of subsets $S$ of $\operatorname{Fl} E$ satisfying conditions
ST 1) to ST 3) of c), and the set of subsets of $\operatorname{Fl} E$ formed by

[PDF p. 451]

monomorphisms and satisfying the same conditions ST 1) to ST 3).

e) Let $(E_j)_{j\in J}$ be a family of subtopoi of $E$, and let $(S_j)_{j\in J}$ be the corresponding family of subsets
of $\operatorname{Fl} E$. Show that $\bigcap_j S_j$ satisfies conditions ST 1) to ST 3) of c), hence corresponds to a
subtopos $E'$ of $E$, and that this subtopos is the subtopos generated by the $E_j$, i.e. the supremum (cf. 9.1.2 c)) of
the subtopoi $E_j$.

f) Let $A$ be a subset of $\operatorname{Fl} E$. Show that there exists a smallest subset $S$ of $\operatorname{Fl} E$
among those containing $A$ and satisfying conditions ST 1) to ST 3), and that $S$ corresponds to the largest subtopos
$E'$ of $E$ such that the corresponding multiplicative subset of $\operatorname{Fl} E$ contains $A$. Show that $S$ is
equal to the union of the subsets $A_n$ ($n\geq 0$) of $\operatorname{Fl} E$, constructed recursively as follows:
$A_0 = A$, and $A_{n+1}$ is formed by the arrows $u : X\to Y$ which are of one of the following four types:

1. $u$ is invertible, or the composite of two arrows of $A_n$, or obtained by base change from an arrow of $A_n$.
2. $u$ is one of the factors of a composite arrow whose other factor and whose composite are in $A_n$.
3. $u$ is a sum of a small family of arrows $\in A_n$.
4. There exists an epimorphism $Y'\to Y$ such that $u' : X' = X\times_Y Y'\to Y'$ obtained from $u$ by base change is in
   $A_n$.

g) With the notation of e), let $A$ be the union of the $S_j$, let $S$ be the subset of $\operatorname{Fl} E$ deduced
from $A$ by the procedure of f), and let $E'$ be the corresponding subtopos of $E$. Show that $E'$ is the intersection
(= infimum) of the subtopoi $E_j$.

**Exercise 9.1.7.2 (canonical factorization of a morphism of topoi).**

a) Let $f : F\to E$ be a morphism of topoi. Show that one can find a factorization of $f$, up to isomorphism, as

```text
(9.1.7.3)    F --f'--> E' --i--> E,
```

where $f'$ is conservative (i.e. (6.1.0) $f'^*$ is conservative, or equivalently

[PDF p. 452]

faithful) and where $i$ is an embedding, and that this factorization is unique up to equivalence (cf. 9.1.4). For this,
introduce the set $S_f\subset \operatorname{Fl} E$ of arrows $u$ of $E$ such that $f^*(u)$ is an isomorphism, prove that
$S_f$ satisfies the conditions of 9.1.7 c), take for $E'$ the corresponding subtopos of $E$, and define $f'^*$ by
(9.1.7.1), which corresponds to a morphism of topoi $f'$ thanks to 9.1.7 b).

b) The subtopos of $E$ defined by the embedding $i$ is called the subtopos of $E$ image of the morphism of topoi $f$.
Show that it is the smallest of the subtopoi $E_1$ of $E$ such that $f$ factors, up to isomorphism, through $E_1$, i.e.
(9.1.4) the smallest of the subtopoi of $E$ containing the image of $f_*$ (or equivalently, the essential image of
$f_*$). In order that $f$ be an embedding, it is necessary and sufficient that $f$ induce an equivalence $f'$ of $F$
with its image; in order that $f$ be conservative, it is necessary and sufficient that its image be equal to all of $E$.

c) Suppose that $f = Top(f_0)$ is associated with a continuous map of sober topological spaces $f_0 : Y\to X$. Consider
the canonical factorization of $f_0$ as

```text
Y -> X' = f_0(Y) -> X,
```

where the second morphism is the inclusion. Show that the canonical factorization of $f$ is then identified with the
corresponding factorization.

Let $Z$ be the smallest sober subspace of $X$ containing $X' = f_0(Y)$, i.e. the set of points $x$ of $X$ such that
$\{x\}\cap X'$ is dense in $\{x\}$. (Note that $Z = X'$ if the points of $X$ are closed, or if $X'$ is a constructible
subset of $X$ assumed locally noetherian.) Then $f$ is conservative, i.e. the subtopos of $E = Top(X)$ image of
$F = Top(Y)$ by $f = Top(f_0)$ is equal to $E$ itself, if and only if $Z = X$, i.e. if and only if $f_0(Y)$ is very
dense (EGA IV 10.13) in $X$. This makes precise the extent to which it is legitimate to regard the notion of
conservative morphism of topoi as the natural generalization of the notion of surjective continuous map of topological
spaces.

[PDF p. 453]

d) Let a cartesian diagram of topological spaces be given. If $Y$ and $X'$ are discrete spaces, hence $Y'$ is discrete,
then the corresponding diagram of topoi is 2-cartesian (5.11). (NB. For a counterexample when $Y$, $X'$ are no longer
assumed discrete, with $Y$, $X'$ subspaces of the separated space $X$, cf. 9.1.10 c).)

Deduce an example of a 2-cartesian diagram of topoi

```text
F' -> F
|    |
v    v
E' -> E
```

such that $f$ is conservative, but $f'$ is not conservative, more precisely $F$ = punctual topos, $F'$ = empty topos
(2.2). (Take $Y$ such that the image of $Y$ in $X$ is very dense and $\ne X$, and take $X'$ reduced to a point not lying
in the image.)

e) Let $(E_i)_{i\in I}$ be a family of subtopoi of a topos $E$. Prove that $E$ is the supremum of the $E_i$ if and only
if the family of embedding morphisms $E_i\to E$ is conservative (6.4.0).

**Exercise 9.1.8 (subtopoi and points of $E$; case of topological spaces).** Let $E$ be a topos.

a) Let $Z$ be a full subcategory of $\operatorname{Point}(E)$ (or, what amounts to the same thing, a subset of
$\operatorname{Ob}\operatorname{Point}(E)$). Show that the set $S(Z)$ of arrows of $E$ which are transformed into
bijections by the fiber functors corresponding to the $z\in \operatorname{Ob} Z$ satisfies the conditions of 9.1.7 c),
and therefore defines a subtopos $E_Z$ of $E$. Show that this subtopos admits enough points, and that $Z$ is equivalent
to a full subcategory of $\operatorname{Point}(E_Z)$.

Show that one can obtain by the preceding procedure every subtopos $E'$ of $E$ which admits enough points. (Take for $Z$
the essential image of the functor (9.1.5.1).)

[PDF p. 454]

Show that one obtains a bijection between the set of subtopoi $E'$ of $E$ admitting enough points, and a subset of the
set of strictly full subcategories $Z$ of $\operatorname{Point}(E)$ which are stable under direct factors (I 10) and
under small filtered projective limits (cf. 7.5). (Problem: which subcategories of $\operatorname{Point}(E)$ are found
in this way? This is essentially, in another form, the problem already raised in 6.5.3, taking account of the dictionary
9.1.3 c). Note that besides the necessary conditions just indicated, there are also more subtle conditions on the
topological nature of $\operatorname{Point}(E)$, of the sobriety kind, cf. c).)

b) Let $(Z_j)_{j\in J}$ be a family of full subcategories of $\operatorname{Point}(E)$, and let $Z$ be the full
subcategory which is the union of the $Z_j$. Show that the corresponding subtopos $E_Z$, defined in a), is the subtopos
of $E$ generated by the $E_{Z_j}$. (Use 9.1.7 e).) Conclude that the subtopos of $E$ generated by a family of subtopoi
having enough points also has enough points.

c) Let $f : E'\to E$ be an embedding of topoi. Show that the map

```text
(9.1.8.1)    Ouv(E) -> Ouv(E'),    U |-> f^*(U),
```

is surjective, and conclude that the map induced by $f$ on isomorphism classes of points induces a homeomorphism of
$\operatorname{Point}(E')$ onto a subspace of $\operatorname{Point}(E)$, for the topologies defined in 7.8 a). (For
injectivity, use 9.1.5.)

d) Let $f : X'\to X$ be a continuous map, hence a morphism of topoi (4.1)

```text
Top(f) : Top(X') -> Top(X).
```

Prove that the latter is an embedding if and only if the topology of $X'$ is the inverse image by $f$ of that of $X$
(i.e. when $X'$ is a Kolmogoroff space, for example a sober space, if and only if $f$ induces a homeomorphism of $X'$
onto a subspace of $X$). (For necessity, use c); for sufficiency, 9.1.7.2 c).)

[PDF p. 455]

e) Let $X$ be a sober topological space, and let $E = Top(X)$. Using a) and d), establish an isomorphism of ordered sets
$X'\mapsto E_{X'}$ between the set of sober subspaces $X'$ of $X$ (i.e., when $X$ is separated, between the set of all
subsets of $X$) and the set of subtopoi of $E$ having enough points. Show that $E_{X'}$ is equivalent to $Top(X')$.

If $(X_j)_{j\in J}$ is a family of sober subspaces of $X$, prove that there exists a smallest sober subspace $X'$ of $X$
containing the $X_j$, equal to the union of the $X_j$ if $J$ is finite or $X$ is separated, and that $E_{X'}$ is the
subtopos of $E$ generated by the $E_{X_j}$. (Use b).)

f) Give an example of a topos $E$ of the form $Top(X)$, and of a subtopos $E'$ which does not have enough points, and
even which is nonempty (2.2) without points. (Take $E$ of the form $\widetilde{U}$, $E' = \widetilde{U'}$, where $U$ is
the ordered set defined in 7.4. Or better, take the example of 9.1.10 b), which shows that one may take for $X$ any
nonempty separated space without isolated points.)

**Exercise 9.1.9 (case of topoi defined by an ordered set).** a) We use the yoga of 7.8 b) and c), giving a dictionary
between, on the one hand, topoi generated by their opens and morphisms of such topoi, and on the other hand ordered sets
having arbitrary suprema, finite infima, and in which the infimum of two elements is distributive with respect to
arbitrary suprema, the morphisms between such ordered sets being the increasing maps commuting with finite infima and
arbitrary suprema.

b) Let $E$ be a topos, and let $f : E'\to E$ be an embedding of topoi. Show that for every generating family
$(X_i)_{i\in I}$ in $E$, the family $(f^*(X_i))_{i\in I}$ is generating. Deduce that if $E$ is generated by its opens,
then so is $E'$. (Use 9.1.8 c).)

c) Let $f : E'\to E$ be a morphism of topoi generated by their opens, associated with a morphism $g : O\to O'$ on the
corresponding ordered sets. Show that $f$ is an embedding if and only if $g$

[PDF p. 456]

is surjective, and if $g$ is surjective on the graphs of the order relations, i.e. the order of $O'$ is the quotient of
that of $O$.

d) Let $E$ be a topos of the form $\widetilde{O}$ as in a). Deduce from b) and c) a one-to-one correspondence between
the set of subtopoi of $E$ and the set of equivalence relations $R$ in $O$ having the following properties, analogous to
conditions ST 1) to ST 3) of 9.1.7 c):

**QO 1)** The relation $R$ is compatible with finite infima, or equivalently: if $U,U'$ are equivalent by $R$, then so
are $U\cap V$ and $U'\cap V$ for every $V\in O$.

**QO 2)** The relation $R$ is compatible with arbitrary suprema, or equivalently: if $U_i$ is equivalent to $U'_i$ for
every $i\in I$, then $\operatorname{Sup} U_i$ is equivalent to $\operatorname{Sup} U'_i$.

Show that if subtopoi $E_i$ of $E$ correspond to equivalence relations $R_i$, then the subtopos generated by the $E_i$
corresponds to the intersection relation of the $R_i$.

**Exercise 9.1.10 (intersection of subspaces; new topoi without points; nonexistence of the complement of a subtopos).**
Let $X$ be a topological space, $E = Top(X) = \widetilde{\operatorname{Ouv}(X)}$ (2.1).

a) Let $R$ be the following relation on $\operatorname{Ouv}(X)$:

```text
(U, U') in R  <=>  U cap U' is dense in U and in U'.
```

Show that $R$ is an equivalence relation satisfying conditions QO 1) and QO 2) of 9.1.9 d), and therefore defines a
subtopos $E'$ of $E$. Show that, for a point $x\in X$, the corresponding point is in the essential image of
$\operatorname{Point}(E')$ if and only if $x$ is thick, i.e. belongs to the closure of the interior of $\{x\}$. Show
that $E'$ is the empty topos (2.2) if and only if $X$ is empty.

b) If $X$ is sober, show that the category $\operatorname{Point}(E')$ is equivalent to the category defined by the
ordered subset of $X$ (for the specialization relation) defined by the thick points of $X$. Show that if the points of
$X$ are closed (resp. if $X$ is noetherian), then the thick points of $X$ are the isolated points of $X$, i.e. those
such that $\{x\}$ is open (resp. are the maximal points of $X$).

[PDF p. 457]

Conclude that, if $X$ is a nonempty separated topological space without isolated points, then the subtopos $E'$ of
$E = Top(X)$ is a non-"empty" topos which has no points.

c) Let $X'$ be a subset of $X$, and let $E_{X'}$ be the subtopos of $E$ associated with $X'$ by the procedure 9.1.8 a).
Show that, if $X'$ is dense, then $E_{X'}$ contains $E'$. Show that, if $X$ is sober and if $X'$ and $X''$ are two sober
subsets of $X$, their intersection $X'\cap X''$ is sober and

```text
E_{X' cap X''} subset E_{X'} cap E_{X''},
```

and that the inclusion may be strict (*). (Take a nonempty separated space $X$ admitting two disjoint dense subsets
$X'$, $X''$.) Show that the preceding inclusion is an equality if and only if the subtopos $E_{X'}\cap E_{X''}$ has
enough points. Show that this is so if $X'$ or $X''$ is a locally closed subset of $X$.

(*) See however 9.1.11 f) below for the case where $X$ is locally noetherian.

d) Let $X'$ be a subset of $X$, and let $X''$ be the complement of $X'$. A subtopos $F$ of $E$ contains the $E_x$, for
$x\in X''$, if and only if it contains $E_{X''}$ (cf. 9.1.8 b)). Conclude that if $X''$ is a union of locally closed
subsets of $X$ (for example if the points of $X''$ are closed), then the set of subtopoi $F$ of $E$ whose intersection
with $E_{X'}$ is the empty subtopos $Top(\emptyset)$ contains a greatest element (which then deserves the name weak
complementary subtopos of $E$ to $E_{X'}$, cf. 9.1.13) only if $E_{X'}\cap E_{X''}$ is the empty subtopos.

This condition is not satisfied if $X\ne\emptyset$ and if $X'$ and $X''$ are both dense in $X$, with $X$, $X'$, and
$X''$ sober, cf. c). Show that, when this condition fails, then in the ordered set of subtopoi of $E$, the $\operatorname
{Inf}$ of two elements is not distributive with respect to arbitrary $\operatorname{Sup}$'s. (The editor does not know
whether it is distributive with respect to finite $\operatorname{Sup}$'s; cf. however 9.1.11 f) and 9.1.12 a).)

**Exercise 9.1.11 (subtopoi of locally noetherian topoi; case of noetherian spaces).**

a) Let $f : E'\to E$ be an embedding of topoi. Show that if $X$ is a prenoetherian object of $E$ (i.e. (VI 1), every
increasing sequence of subobjects of $X$ is stationary), then $X' = f^*(X)$ is a prenoetherian object of $E'$.

[PDF p. 458]

Introducing the induced topoi $E_{/X}$ and $E'_{/X'}$ and using 9.1.6 c), first reduce to the case where $X$ is the
final object $e$ of $E$, hence $X'$ is the final object $e'$ of $E'$. Then note that every increasing sequence of
subobjects of $e'$ defines, by applying $f_*$, an increasing sequence of subobjects of $f_*(e') = e$.

Conclude that if $E$ admits a generating family formed by prenoetherian objects (resp. if $E$ is a noetherian topos,
resp. locally noetherian (VI 2)), then $E'$ satisfies the same condition. (Use 9.1.9 b).)

b) Let $E$ be a locally noetherian topos (VI 2). Show that every subtopos of $E$ is of the form $E_Z$ (9.1.8 a)), for a
suitable full subcategory $Z$ of $\operatorname{Point}(E)$. (Use a) and Deligne's theorem that every locally noetherian
topos admits enough points.)

Conclude that, if $E$ is of the form $Top(X)$, where $X$ is a sober locally noetherian topological space, then
$Z\mapsto E_Z$ is an isomorphism from the ordered set of sober subspaces of $X$ to the ordered set of subtopoi of $E$.
(Use 9.1.8 e).) The intersection of sober subspaces $Z_i$ (is necessarily sober and) defines the intersection of the
subtopoi $E_{Z_i}$ (contrary to what can happen in the general case (9.1.10 c)).

c) Let $X$ be a sober locally noetherian space, let $X'$ be a subset of $X$, and let $X''$ be its complement. Show that
the following conditions are equivalent:

(i) $X'$ is constructible.

(ii) $X'$ and $X''$ are sober.

(iii) $X'$ is sober, and the subtopos $E_{X'}\simeq Top(X')$ of $E = Top(X)$ admits a "complementary" subtopos (cf.
9.1.13 e).

(iv) The intersection of the subtopoi $E_{X'}\simeq Top(X')$ and $E_{X''}\simeq Top(X'')$ in $Top(X)$ is the "empty"
subtopos of $E$.

Show that if $E'$ and $E''$ are two subtopoi of $E$, they are weak complements if and only if they are complements
(9.1.13).

[PDF p. 459]

d) Let $X$ be a sober noetherian space. Show the equivalence of the following conditions:

(i) Every sober subspace $X'$ of $X$ is constructible, i.e. its complement is sober (cf. c)).

(i bis) For every maximal point $x$ of $X$, $X-\{x\}$ is sober, i.e. $\{x\}$ is constructible.

(iii) Every subtopos of $Top(X)$ admits a complementary subtopos (cf. 9.1.13).

(iv) In the ordered set of subtopoi of $Top(X)$, the $\operatorname{Inf}$ of two elements is distributive with respect
to arbitrary $\operatorname{Sup}$'s.

(Use the argument of 9.1.10 d), thanks to the intersection formula.)

e) Let $X$ be a locally noetherian space. Show that, in the ordered set of subtopoi of $Top(X)$, the
$\operatorname{Inf}$ of two elements is distributive with respect to finite $\operatorname{Sup}$'s. (Reduce to the case
where $X$ is sober, and use b).)

f) For every sober subspace $Z$ of the sober locally noetherian space $X$, let $T_Z$ be the topology on the category
$\operatorname{Ouv}(X)$ of opens of $X$ for which a family of inclusions $U_i\to U$ is covering if and only if one has

```text
U cap Z = union_i (U_i cap Z).
```

Show that $Z\mapsto T_Z$ establishes a bijection (reversing inclusion relations) between the set of sober subspaces $Z$
of $X$, and the set of topologies on $\operatorname{Ouv}(X)$ finer than the canonical topology $T_X$. (Use b) and 9.1.2
e).)

g) Let $X$ be a sober topological space. A subset $X'$ of $X$ is sober if and only if its complement is a union of
locally closed subsets; if $X$ is locally noetherian, this also means that $X'$ is "proconstructible" (EGA IV 1.9.4).
Show that there exists on $X$ a topology $T_{\mathrm{cons}}$, in such a way that the closed subsets of
$X_{\mathrm{cons}} = (X,T_{\mathrm{cons}})$ are the sober subsets of $X$. From now on suppose $X$ locally noetherian;
$X_{\mathrm{cons}}$ is therefore none other than the space

[PDF p. 460]

$X_{\mathrm{cons}}$ of EGA IV 9.1.13. Deduce then from b) and c) that the ordered set $\Sigma$ of subtopoi of $Top(X)$
is isomorphic to the ordered set of closed subsets of $X_{\mathrm{cons}}$, and that, under this correspondence, the
subtopoi admitting a complement correspond to the subsets both open and closed of $X_{\mathrm{cons}}$. Show that
$X_{\mathrm{cons}}$ is locally compact, and that it is compact if and only if $X$ is noetherian, i.e. the topos $Top(X)$
is noetherian.

h) Let $E$ be a locally noetherian topos. Suppose that it has the property considered in 9.1.14 b) (a condition perhaps
always fulfilled...). Show that the essential images of the canonical functors

```text
Point(E') -> Point(E),
```

where $E'$ runs through the set $\Sigma$ of subtopoi of $E$, define in the set $X = \operatorname{Point}(E)$ of
isomorphism classes of points of $E$ a set of subsets which is the set of closed subsets for a topology $T_{\mathrm
{cons}}$ on $X$, and that in this way one obtains an isomorphism of ordered sets between the set $\Sigma$ of subtopoi of
$E$ and the set of closed subsets of $X_{\mathrm{cons}}$. Conclude that in $\Sigma$, the $\operatorname{Sup}$ of two
elements is distributive with respect to arbitrary $\operatorname{Inf}$'s. Show that $X_{\mathrm{cons}}$, which is not
necessarily $U$-small, has an associated sober space (4.2.1) which is $U$-small.

**Exercise 9.1.12 (finite topoi).** A topos $E$ is called **finite** if it is equivalent to a topos of the form
$\widehat{C}$, with $C$ a finite category.

**a) (Dictionary).** Let $V$ be a universe such that $U\in V$. Let $(\mathrm{Karfiness})$ be the 2-category defined as
the full 2-subcategory of the category $(\mathrm{Cat})_V$, formed by the categories which are elements of $V$, are
Karoubian, and are equivalent to a finite category; and let $(\mathrm{Topfin})$ be the 2-category defined as the full
2-subcategory of $(V\text{-}U\text{-}\mathrm{Top})$ (3.3.1) formed

[PDF p. 461]

by the finite $U$-topoi which are elements of $V$. Show that one has 2-equivalences quasi-inverse to one another:

```text
(9.1.12.1)  C |-> Chat : (Karfiness) -> (Topfin),
(9.1.12.2)  E |-> Point(E) : (Topfin) -> (Karfiness).
```

(Use 7.6 h), e).)

**b)** Show that a finite topos is noetherian (VI 2).

**c)** Show that every subtopos of a finite topos $E$ is a finite topos. More precisely, if $E$ is equivalent to
$\widehat{C}$, where $C$ is a finite Karoubian category (or, more generally, equivalent to a finite category), show that
one obtains an ordered isomorphism between the set of subtopoi $E'$ of $E$ and the set of strictly full subcategories
$C'$ of $C$ which are Karoubian (or, what amounts to the same thing, stable in $C$ under direct factors), by associating
to every $C'$ the essential image of

```text
f_* : Chat' -> Chat,
```

where $f' : C'\to C$ is the inclusion functor. (Use 5.6 to ensure that $f_*$ is fully faithful, and b) and 9.1.11 b) for
the fact that every subtopos $E'$ of $E$ is obtained as indicated.)

**d)** Let $E$ be a finite topos. Construct on the finite set $X = \operatorname{Point}(E)$ of isomorphism classes of
points of $E$ a topology making it into a sober topological space, and such that the ordered set of subtopoi of $E$ is
canonically isomorphic to the set of closed subsets of $X$. (Take the "constructible topology" $T_{\mathrm{cons}}$
defined via the order relation

```text
x <= y  <=>  x is a direct factor of y,
```

for which the closure of a point $x$ is formed by the $y$ such that $y\leq x$.) In particular, the set $\Sigma$ of
subtopoi of $E$ is finite, and $\operatorname{Inf}$ there is distributive with respect to arbitrary
$\operatorname{Sup}$'s.

**e)** Let $C$ be a category equivalent to a finite category. Show that for every full subcategory $C'$ of $C$, there
exists on $C$ a topology $T_{C'}$ for which a family $(X_i\to X)_{i\in I}$ is covering if and only if, for every
$Y\in \operatorname{Ob} C'$, the family of maps

```text
Hom(Y, X_i) -> Hom(Y, X)        (i in I)
```

is surjective. Show that the category of sheaves on $(C,T_{C'})$ is equivalent to $\widehat{C'}$, and that
$C'\mapsto T_{C'}$ is a bijection (reversing the order relations) between the set of strictly full subcategories $C'$ of
$C$ which are Karoubian (or, what amounts to the same thing, stable in $C$ under direct factors), and the set of
topologies (II 1.1) on the category $C$. (Use c) and

[PDF p. 462]

9.1.2 c).) In particular, if $C$ is a site whose underlying category is equivalent to a finite category, then the topos
$\widetilde{C}$ is a finite topos.

**f)** Let $f : C'\to C$ be a functor of $U$-categories, with $C$ equivalent to a finite category. Show that the
morphism of topoi

```text
f~ : C'~ -> C~                         (4.6)
```

is conservative if and only if every object of $C$ is isomorphic to a direct factor of an object in the image of $f$.
(Reduce to the case where $f$ is an inclusion $f : C'\hookrightarrow C$, with $C'$ as in c).)

**g)** Let $C$ be the category having two objects $e$ (the final object) and $a$, and, besides the identity arrows,
three arrows

```text
f : a -> e,    alpha : e -> a,    p = alpha f       (hence p^2 = p).
```

Show that $E = \widehat{C}$ has, besides the subtopoi $E$ and $Top(\emptyset)$, exactly one subtopos $E'$, namely
$E' = \widehat{\{e\}}$. Consequently, for every subtopos $E''$ of $E$, if $E''\ne Top(\emptyset)$, then
$E'\cap E''\ne Top(\emptyset)$.

**Exercise 9.1.13 (complementary subtopoi of a topos).** Let $E$ be a topos, and let $E'$ and $E''$ be two subtopoi. We
say that $E'$ and $E''$ are **complementary** to one another if

```text
E' cap E'' = Top(emptyset),        E' vee E'' = E,
```

where the sign $\vee$ denotes the $\operatorname{Sup}$ in the ordered set of subtopoi of $E$. We suppose that in the set
$\Sigma$ of subtopoi of $E$, the $\operatorname{Inf}$ of two elements is distributive with respect to finite
$\operatorname{Sup}$.

**a)** If $E'$ and $E''$ are complementary, $E''$ is the greatest among the subtopoi $E_1$ of $E$ such that
$E'\cap E_1 = Top(\emptyset)$ (i.e. $E''$ is a weak complement of $E'$, in the terminology of 9.1.10 d)).

**b)** Show that the following conditions on $E$ are equivalent:

**(i)** If $E'$ and $E''$ are two subtopoi of $E$ such that $E''$ is a weak complement of $E'$, then $E''$ is a
complement of $E'$.

**(ii)** For every subtopos $E'$ of $E$ such that $E'\ne E$, there exists a subtopos $E''$ of $E$ such that
$E''\ne Top(\emptyset)$ and $E'\cap E'' = Top(\emptyset)$.

**(i bis)** If $E'$ and $E''$ are two subtopoi of $E$ such that $E''$ is maximal in the set of subtopoi $E_1$ such that
$E'\cap E_1 = Top(\emptyset)$, then $E''$ is a complement of $E'$.

Show that even if $E$ is a finite topos (9.1.12),

[PDF p. 463]

these conditions are not necessarily verified (9.1.12 g)). They are nevertheless verified if $E$ is of the form
$Top(X)$, where $X$ is a locally noetherian space. (Use 9.1.11 b).)

**c)** A subtopos $E'$ of $E$ is called **complemented** if it admits a complement (compare 9.1.12 c)). Prove that the
set of complemented subtopoi is stable under finite $\operatorname{Inf}$ and $\operatorname{Sup}$, and under
complementation, and that complementation transforms $\operatorname{Inf}$ into $\operatorname{Sup}$, and
$\operatorname{Sup}$ into $\operatorname{Inf}$.

**d)** State the duals of observations a), b), c) (which were in fact trivial general statements about an abstract
ordered set $\Sigma$; note that the hypothesis made on $\Sigma$ is in fact self-dual).

**9.1.14. Open questions.** Let $E$ be a topos.

**a)** In the set of subtopoi of $E$, is the $\operatorname{Inf}$ of two elements distributive with respect to finite
$\operatorname{Sup}$'s?

**b)** Let $E'$, $E''$ be two subtopoi of $E$ such that $E = E'\vee E''$. Is it then true that every point of $E$ is
isomorphic to the image of a point of $E'$ or of a point of $E''$?

Note that if the answer to b) is affirmative for $E$ and all its subtopoi, then the answer to a) is affirmative, at
least for the case of subtopoi having enough points (hence for all subtopoi, if $E$ is locally noetherian (9.1.11 b)).
The answer to a) (and, a fortiori, to b)) is nevertheless not known for all noetherian topoi. However the answer to a)
and b) is affirmative if $E$ is of the form $Top(X)$, with $X$ a locally noetherian space (9.1.11), or if $E$ is a
finite topos (9.1.12).

Note that a) can be reformulated in the following form, applied to all subtopoi $F$ of $E$:

**a')** If $E'$ and $E''$ are two subtopoi of a topos $F$, such that the canonical morphism (cf. 8.7 b))

```text
(9.1.14.1)    E' coproduct E'' -> F
```

is conservative (which also means $F = E'\vee E''$ (9.1.7.2 e)), then the same is true for the morphism deduced by
2-base change

[PDF p. 464]

$F_1\to F$, where $F_1$ is a subtopos of $F$.

There is an analogous reformulation b') of b), by taking a base change $F_1\to F$ by a punctual topos $F_1$ (2.2). Thus
one sees that an affirmative answer to a), b) would follow from an affirmative answer to the following question (where
one takes for $F$ any subtopos of $E$):

**c)** If $E'$ and $E''$ are two subtopoi of the topos $F$, whose $\operatorname{Sup}$ is $F$, i.e. such that the
morphism of topoi (9.1.14.1) is conservative, is this morphism even universally conservative, i.e. does it remain
conservative after every 2-base change $F_1\to F$?

This statement makes sense, thanks to Deligne's result asserting the existence of 2-fiber products of topoi. See however
the example 9.1.7.2 d).

On the other hand, one sees by 9.1.11 h) that an affirmative answer to b) would give, in the locally noetherian case, an
affirmative answer to the following question:

**d)** In the ordered set $\Sigma$ of subtopoi of $E$, is the $\operatorname{Sup}$ of two elements distributive with
respect to arbitrary $\operatorname{Inf}$'s (not necessarily finite)?

This also means that $\Sigma$ is interpreted as the ordered set of "closed subtopoi" of a suitable topos $E_{\mathrm
{cons}}$ (namely $(\Sigma^{\mathrm{op}})^\sim$, where the opposite ordered set $\Sigma^{\mathrm{op}}$ of $\Sigma$,
regarded as a category, is endowed with its canonical topology, cf. 7.8 b)), which is generated by the subobjects of the
final object, hence is very close to an ordinary topological space. It would remain to study this topos $E_{\mathrm
{cons}}$, taking inspiration from Examples 9.1.11 g) and 9.1.12 d), and in particular to determine whether it is
noetherian if $E$ is, which amounts to the following question for the subtopoi $F$ of $E$, which makes sense
independently of d):

**e)** Let $F$ be a noetherian topos and let $(E_i)_{i\in I}$ be a family of subtopoi of $F$ whose intersection is
$Top(\emptyset)$. Does there then exist a finite subfamily having the same property?

In a rather different direction, let us also recall the question raised in 9.1.6 e), which deserves clarification.

**9.2. Case of Open Subtopoi.**

**9.2.1.** Let $U$ be an open of a topos $E$, i.e. a subobject of the final object $e$ of $E$ (8.3). Consider the
localization morphism (5.2)

```text
j : E/U -> E.
```

Since $U\to e$ is here a monomorphism, the functor $j_*$ (which is interpreted as the forgetful functor) is fully
faithful, hence its biadjoint $j_!$ is also fully faithful (1.5.7 a)). In other words, the localization morphism $j$
(9.2.2) associated with an open $U$ of the topos $E$ is an embedding of topoi (9.1.1 a)).

An embedding of topoi $F\to E$ is called an **open embedding** if it is isomorphic to the embedding of topoi defined by
an open $U$ of $E$. A subtopos $E'$ (9.1.1 b)) of $E$ is called an **open subtopos** if it is defined by means of an
open of $E$, i.e. if the canonical inclusion morphism $E'\to E$ is an open embedding. Note that the open $U$ of $E$
associated with an open embedding of topoi $j : E'\to E$ is uniquely determined as being equal to the subobject
$j_*(e')$ of $e$, where $e'$ denotes the final object of $E'$. Consequently, one obtains a one-to-one correspondence
between the opens $U$ of $E$ and the open subtopoi of $E$.

**Remark 9.2.3.** In accordance with the preceding definitions, the open subtopos of $E$ associated with the open $U$ of
$E$ is the strictly full subcategory of $E$ which is the essential image of the direct image functor $j_*$.

One must be careful not to confuse this subcategory of $E$ with the strictly full subcategory, the essential image of
$j_!$, formed by the objects $X$ of $E$ such that the structural morphism $X\to e$ factors through $U$. It is clear,
however, that these two subcategories determine one another, and that they are canonically equivalent. This is why some
authors have been tempted to call (or indeed have called) "open subtopos defined by $U$" the strictly full subcategory
which is the essential image of $j_!$, whose description in terms of $U$ is simpler than

[PDF p. 466]

that of the essential image of $j_*$. This terminology presents no drawback so long as one does not intend to study
other kinds of subtopoi than open subtopoi. Since this is not our case, we shall not follow the aforementioned authors
here.

For the reader's convenience, we shall summarize the most important special properties of open embeddings.

**Proposition 9.2.4.** Let

```text
j : E' -> E
```

be an open embedding of topoi (9.2.1). Then the functor $j_!$ left adjoint to $j^*$ exists, so that one has a sequence
of three adjoint functors

```text
j_! adj j^* adj j_*.
```

Moreover:

**a)** The functor $j_!$ and the functor $j_*$ are fully faithful.

**b)** The functor $j_!$ commutes with fiber products, products indexed by small sets $I\ne\emptyset$, and projective
limits relative to small cofiltered index categories (1.2.7).

**c)** For every object $X$ of $E$, the adjunction morphism

```text
j_! j^*(X) -> X
```

is a monomorphism.

**Proof.** We may suppose that $j$ is the localization morphism defined by an open $U$ of $E$. Then a) is recorded for
reference, b) comes from the interpretation of $j_!$ as a forgetful functor and from the fact that $U\to e$ is a
monomorphism. Finally c) is immediate on noting that the morphism in question is none other than the morphism deduced
from the inclusion $U\to e$ by the base change $X\to e$, taking account of the fact that a monomorphism is transformed
into a monomorphism by base change.

**Remark 9.2.4.1.** One can find embeddings of topoi $j : E'\to E$ such that $j_!$ exists, but $j_!$ does not commute
with products of two objects, nor with cofiltered projective limits (Exercise 9.5.9 c)).

[PDF p. 467]

**9.2.5.** Now let

```text
g : E' -> E
```

be an arbitrary morphism of topoi, and let $U' = g^*(U)$ be the inverse image of the open $U$ of $E$. We saw in 5.11
that the corresponding diagram of topoi is 2-cartesian. We conclude in particular that the inverse image by $g$ of an
open subtopos of $E$ (cf. 9.1.6 d)) is an open subtopos of $E'$, or what amounts to the same thing, that the notion of
open embedding of topoi (9.2.1) is stable under 2-base changes in the 2-category of $U$-topoi (which are elements of a
given universe $V$).

Also note that in order for the morphism of topoi $g : E'\to E$ to factor, up to isomorphism, through $j : E/U\to E$, it
is evidently necessary and sufficient that $j' : E'/U'\to E'$ be an equivalence of categories, which also means that the
inclusion $U'\to e'$ (the final object of $E'$) is an isomorphism. This therefore refines 9.1.4, by characterizing in a
simple way the essential image of the functor considered in loc. cit.

**9.2.6.** Apply 9.2.5 to the case where $E'$ is of the form $E/V$, where $V$ is an open of $E$, with $g$ the
localization morphism. Then $U' = U\cap V$, and one finds that the 2-cartesian product of $E/U$ and $E/V$ over $E$ is
identified with $E/(U\cap V)$. We conclude that a finite intersection of open subtopoi of $E$ is an open subtopos of
$E$, more precisely that the map

```text
(9.2.6.1)    U |-> subtopos of E defined by U
```

commutes with finite intersections.

**Exercise 9.2.7.** Prove that the map (9.2.6.1) also commutes with arbitrary $\operatorname{Sup}$'s. (Use 9.1.7.2 e).)

**9.3. Construction of the Closed Subtopos Complementary to an Open Subtopos.**

**9.3.1.** Let $T$ be a topological space, and let $U$ be an open subset of $T$, so that $Top(U)$ is identified with an
open subtopos of $Top(T)$ (notation of 2.1). Let $Y$ be the closed topological subspace of $T$ complementary to $U$. One
may then, up to equivalence, regard $Top(Y)$ as a subtopos of $Top(T)$, namely the subtopos formed by the objects $F$ of
$Top(T)$ whose restriction to $U$ is the final topos of $U$. This description of a subcategory of $E = Top(T)$ makes
sense whenever one has a topos and an open $U$ of it, and we shall see that it always gives a subtopos of $E$. Moreover,
in the particular case first considered (and with the terminology introduced in Exercise 9.1.13), it is immediate that
$Top(Y)$ and $Top(U)$ are complementary subtopoi of one another (use 9.2.5 and 9.1.7.2 e)). The same will still be true
in the general case, and we shall see that this property uniquely characterizes the subtopos under consideration. It
therefore deserves, in every respect, the name closed subtopos complementary to the open under consideration or to the
open subtopos defined by $U$. The details of the construction of this topos $F$, and of the inverse image functor
$i^* : E\to F$, will be given in the present section, while Section 9.4 will develop its first properties.

**9.3.2.** Thus let, as in 9.2.1, $E$ be a topos, let $U$ be an open of $E$, and consider the localization morphism

```text
(9.3.2.1)    j : E/U -> E,
```

which is an open embedding. For every object $X$ of $E$, put

```text
(9.3.2.2)    X_{C U} = U coproduct_{U times X} X,
```

where the amalgamation is taken for the canonical projections

```text
pr_1 : U times X -> U,        pr_2 : U times X -> X.
```

Thus one has a cocartesian diagram (I 10) in $E$, depending functorially on $X$:

[PDF p. 469]

```text
(9.3.2.3)        U times X  --pr_2-->  X
                  |                    |
                pr_1                   v
                  |                  X_{C U}
                  v                    ^
                  U  -----------------/
```

Note that in the example considered in 9.3.1, $X_{C U}$ is canonically isomorphic to $i_*i^*(X)$ (where $i : Y\to T$ is
the inclusion), and $X\to X_{C U}$ to the adjunction morphism.

**Proposition 9.3.3.** With the preceding notation, one has the following:

**a)** For every object $X$ of $E$, the following conditions are equivalent:

**(i)** There exists an object $Y$ of $E$ and an isomorphism $X\simeq Y_{C U}$.

**(ii)** The canonical morphism $X\to X_{C U}$ is an isomorphism.

**(iii)** The canonical morphism $\operatorname{pr}_2 : X\times U\to U$ is an isomorphism (i.e. $j^*(X)$ is a final
object of $E/U$).

**b)** For every morphism

```text
m : X -> X'
```

in $E$, the following conditions are equivalent:

**(i')** The diagram

```text
X      ->   X'
|           |
v           v
X_{C U} ->  X'_{C U}
```

is cartesian.

**(ii')** The morphism $m\times \operatorname{id}_U : X\times U\to X'\times U$ is an isomorphism, i.e. $j^*(m)$ is an
isomorphism.

**c)** The functor

```text
X |-> X_{C U}
```

from $E$ to $E$ is left exact, transforms epimorphic families into epimorphic families, commutes with filtered inductive
limits

[PDF p. 470]

and with amalgamated sums.

**Proof.** We first prove the proposition in the case where $E$ is of the form $\widehat{C}$, where $C$ is a small
category, and for this one is reduced by I 3.1 to the case where $E$ is the "punctual" topos $(\mathrm{Ens})$, where the
proposition is evident. One passes from there to the general case by the standard procedures of II 4, using the
"associated sheaf" functor.

**Proposition 9.3.4.** With the notation of 9.3.2, the strictly full subcategory $F$ of $E$ defined by the objects $X$
of $E$ such that $j^*(X)$ is a final object of $E/U$ (cf. 9.3.3 a)) is a subtopos of $E$, i.e. (9.1.1) it is a topos,
and the inclusion functor $i_* : F\to E$ is the direct image functor of a morphism of topoi $i : F\to E$, whose inverse
image functor is the functor

```text
i^*(X) = X_{C U}.
```

The adjunction morphism $X\to i_*i^*(X)$ is the canonical morphism $X\to X_{C U}$ of (9.3.2.3).

**Proof.** For every object $X$ of $E$, denote by $u(X)$ the canonical morphism $X\to X_{C U}$. The morphism $u(X)$ is
functorial in $X$ and, for every object $X$, $u(X_{C U})$ is an isomorphism. It then follows formally and trivially from
these two properties that the functor $i^*$ is left adjoint to the functor $i_*$, and that the adjunction morphism is
$u(X)$. Since the functor $X\mapsto X_{C U}$ is left exact, the functor $i^*$ is left exact. It then follows from II 5.5
that $F$ is a topos, and from Definition 3.1 that the pair $(i^*,i_*)$ is a morphism of topoi.

**9.3.5.** The subtopos $F$ of $E$ described in 9.3.4 is called the **closed subtopos** of $E$ complementary to the open
$U$ of $E$, or, equivalently, to the open subtopos of $E$ corresponding to $U$. In accordance with 9.1.1 b), the
morphism $i : F\to E$ constructed in 9.3.4 is called the inclusion morphism. A full subcategory $F$ of $E$ is called a
**closed subtopos** of $E$ if there exists an open $U$ of $E$ such that $F$ is the closed subtopos complementary to $U$.
Note that this $U$ is uniquely determined as $i_*(0_F)$, where $0_F$ is the initial object of $F$, equal to $i^*(0_E)$;
it is also called the open of $E$ complementary to the closed subtopos $F$.

[PDF p. 471]

The subtopos of $E$ defined by $U$ is also called the open subtopos of $E$ complementary to $F$. Finally, an embedding
of topoi $i : F\to E$ (9.1.1 a)) is called a **closed embedding** if the corresponding subtopos of $E$ is closed.

If $G$ is a group on $E$, $s\in \operatorname{Hom}(e,G)$, the **support** of $G$ (resp. of $s$) means the closed
subtopos of $E$ complementary to the open cosupport of $G$ (resp. $s$) (8.5.1, 8.5.2).

**9.3.6.** With the notation of 9.3.2 and 9.3.4, we therefore find two morphisms of topoi

```text
(9.3.6.1)    E/U --j--> E <--i-- F,
```

defining five functors forming two sequences of adjoint functors

```text
j_! adj j^* adj j_*,        i^* adj i_*.
```

The functor

```text
(9.3.6.3)    p = i^* j_* : E/U -> F
```

is called the **gluing functor** relative to the open $U$ of $E$. More generally, if $U$ and $F$ are two arbitrary
topoi, a functor $p : U\to F$ is called a gluing functor if it is left exact and accessible (I 9.2), or what amounts to
the same thing (I 8), if it admits a pro-adjoint. The reasons for this terminology will appear in 9.4.1 d) and 9.5.4
below.

## 9.4. First Properties of the Closed Subtopos $F$ and of $i^*$

**Proposition 9.4.1.** The notation is that of 9.3.2 and 9.3.4.

a) The functor $i^* : E\to F$ transforms epimorphic families into epimorphic families. It commutes with the formation of
amalgamated sums and filtered inductive limits.

b) For every object $X$ of $E$ such that the projection morphism $U\times X\to U$ is an epimorphism, the adjunction
morphism

```text
X -> i_* i^*(X)
```

is an epimorphism.

[PDF p. 472]

c) The pair of functors $(i^*,j^*)$ from $E$ to $F$ and $E/U$ respectively is conservative (I 6.1), i.e. a morphism $m$
of $E$ is an isomorphism if and only if $i^*(m)$ and $j^*(m)$ are isomorphisms. This is equivalent to saying that the
pair of functors $(i^*,j^*)$ is faithful (6.4.0).

d) The gluing functor $p = i^*j_* : E/U\to F$ is a left exact and accessible functor (I 9.2), or what amounts to the
same thing (I 8), it admits a pro-adjoint

```text
e : Pro(F) -> Pro(E/U).
```

**Proof.** a) follows from 9.3.3 c). To prove b), it suffices to refer to the definition (9.3.2.2) of $X_{C U}$, taking
account of the fact that $i_*i^*(X) = X_{C U}$ (9.3.4). Assertion c) follows from 9.3.3 b). The functors $i^*$ and $j_*$
are left exact, and consequently $p$ is left exact. The functor $j_*$ is a direct image functor of a morphism of topoi,
and consequently it is accessible (I 9.5; note that a topos is an accessible category (I 9.11.3)). Since the functor
$i^*$ commutes with inductive limits (it is an inverse image functor), the functor $p$, as the composite of two
accessible functors, is accessible.

**Proposition 9.4.2.** Let $E'$ be a topos. Then the functor

```text
Homtop(E', F) -> Homtop(E', E)
```

is fully faithful, and its essential image is formed by the morphisms of topoi $g : E'\to E$ such that $g^*(U)$ is an
initial object $0_{E'}$ of $E'$.

By 9.1.4, we know that the functor in question is fully faithful and that $g$ is in its essential image if and only if,
for every object $X'$ of $E'$, the object $g_*(X')$ of $E$ belongs to $F$, i.e. one has

```text
(*)    g_*(X') ~= (g_*(X'))_{C U}       for every X' in Ob E'.
```

Now put $U' = g^*(U)$, and consider the diagram of topoi

```text
E'/U' --j'--> E'
  |           |
  v           v g
E/U  --j-->   E.
```

[PDF p. 473]

It is clear that one has a canonical isomorphism

```text
j^* g_*(X') ~= g'_* j'^*(X'),
```

and on the other hand it is also immediate that the functor $j'^*$ is essentially surjective, so condition (*) is
equivalent to the condition

```text
(**)    g'_*(Y') is a final object of E/U,       for every Y' in Ob(E'/U').
```

Using the adjunction property of $g'^*$ and $g'_*$, one immediately sees that this means that $g'^*(Y)$ is an initial
object of $E'/U'$ for every object $Y$ of $E/U$, or equivalently (using the fact that the initial object of $E'/U'$ is
strict (II 4.5)) that this is so for $Y = e_U$, the final object of $E/U$. But this also means that the final object
$U'$ of $E'/U'$ is initial, or, what is manifestly the same thing, if and only if $U'$ is an initial object $0_{E'}$ of
$E'$, q.e.d.

**Corollary 9.4.3.** Let $g : E'\to E$ be a morphism of topoi, let $U' = g^*(U)$, let $F'$ be the closed subtopos of
$E'$ complementary to the open $U'$, and finally let $i'$ be the inclusion morphism. Then the morphism of topoi
$g i' : F'\to E$ factors up to isomorphism through a morphism of topoi

```text
g_F : F' -> F,
```

and the corresponding diagram of topoi

```text
(9.4.3.2)        F'  --g_F-->  F
                  |            |
                 i'            i
                  |            |
                  v            v
                  E' --g-->    E
```

is 2-cartesian (cf. 5.11).

This follows formally from 9.4.2 and the definitions.

With the terminology introduced in 9.1.6 d), one may therefore say, in particular, that the inverse image by a morphism
of topoi $g : E'\to E$ of a closed subtopos $F$ of $E$ is a closed subtopos $F'$ of $E'$, namely the closed subtopos
complementary to the open $U' = g^*(U)$, where $U$ is the open of $E$ complementary to $F$.

**Corollary 9.4.4.** Let $E$ be a topos, let $U$ be an open subtopos of $E$, and let $F$ be its complementary closed
subtopos.

[PDF p. 474]

**a)** One has

```text
U cap F ~= Top(emptyset),        U vee F = E,
```

where the sign $\vee$ denotes the $\operatorname{Sup}$ in the set of all subtopoi of $E$ (9.1.2 e)). With the
terminology introduced in 9.1.13, $U$ and $F$ are complementary subtopoi of $E$.

**b)** $U$ (resp. $F$) is the greatest among the subtopoi $E'$ of $E$ such that one has $E'\cap F\simeq Top(\emptyset)$
(resp. $U\cap E'\simeq Top(\emptyset)$).

**Proof.** a) The first relation amounts to saying that if $E'$ is a topos and $g : E'\to E$ is a morphism of topoi
which factors up to isomorphism through $U$ and through $F$, then $E'\simeq Top(\emptyset)$; but by virtue of 9.2.5 and
9.4.2, the hypothesis means that $g^*(U)$ is both an initial object and a final object of $E'$, whence the conclusion.
For the second relation, note that by 9.1.7.2 e) it is equivalent to 9.4.1 c).

b) Suppose that $E'\cap F\simeq Top(\emptyset)$; by virtue of 9.4.3, $E'\cap F$ is equivalent to the subtopos of $E'$
complementary to $g^*(U)$, where $g : E'\to E$ is the inclusion morphism, and therefore the condition considered means
that $U' = g^*(U)$ is a final object of $E'$, i.e. (9.2.5) that $E'\subset U$. Suppose that
$U\cap E'\simeq Top(\emptyset)$; by virtue of 5.11, $U\cap E'$ is equivalent to $E'/U'$, and therefore the condition
considered means that $U'$ is an initial object of $E'$, i.e. (9.4.2) that $E'\subset F$.

**Corollary 9.4.5.** Let $(F_i)_{i\in I}$ be a family of closed subtopoi of the topos $E$, and for every $i\in I$, let
$U_i$ be the open of $E$ complementary to $F_i$. Then the subtopos of $E$ which is the intersection of the $F_i$ (9.1.3)
is a closed subtopos, whose complementary open is

```text
U = Sup_i U_i.
```

This follows formally from the universal property of the intersection as 2-product and from 9.4.2, taking account of the
fact that for a morphism

```text
h : E' -> E,
```

one has $h^*(U) = \operatorname{Sup}_i h^*(U_i)$.

**Corollary 9.4.6.** With the notation of 9.4.5, suppose $I$ finite. Then

[PDF p. 475]

the subtopos of $E$ which is the supremum of the $F_i$ (9.1.2 c)) is a closed subtopos of $E$, whose complementary open
is equal to $\operatorname{Inf}_i U_i$.

**Exercise 9.4.7 (gluing of subtopoi).** Let $E$ be a topos.

a) Let $E'$ be a subtopos of $E$, let $(S_i)_{i\in I}$ be a family of objects of $E$ covering the final object, and for
every $i\in I$, let $S'_i$ be the inverse image of $S_i$ in $E'$; let $E'_i\subset E_i$ be the subtopos of $E_i = E/S_i$
inverse image by the localization morphism $E_i\to E$ of the subtopos $E'$ of $E$ (9.1.6 d) and 5.11). Show that for an
object $X$ of $E$, $X$ belongs to $E'$ if and only if, for every $i\in I$, the inverse image $X|S_i$ of $X$ in $E_i$
belongs to $E'_i$.

b) Suppose that $E$ is of the form $\widetilde{C}$, where $C$ is a $U$-site. Show that the presheaf on $C$

```text
X |-> set of subtopoi of the topos (C/X)~
```

is a sheaf. With $E$ again arbitrary, conclude that there exists an object of $E$ which represents the functor

```text
S |-> set of subtopoi of the topos E/S.
```

c) With the notation of a), show that, in order for the subtopos $E'$ of $E$ to be an open subtopos (resp. a closed
subtopos), it is necessary and sufficient that, for every $i\in I$, the same be true of the induced subtopos $E'_i$ of
$E_i$.

**Exercise 9.4.8 (interior, exterior, closure, and boundary of a subtopos).** Let $E$ be a topos, let $E'$ be a
subtopos, and let $i : E'\to E$ be the inclusion morphism.

**a)** Show that $i_*(0_{E'})$ is the greatest open $U$ of $E$ such that one has $E'\cap U\simeq Top(\emptyset)$, where
$U$ is the open subtopos of $E$ defined by $U$. We shall call this $U$, or $U_{E'}$, the **exterior** of the subtopos
$E'$ of $E$, and the closed subtopos of $E$ complementary to $U$ the **closure** of $E'$.

**b)** Show that there exists a greatest open $V$ of $E$ such that the corresponding open subtopos $V$ of $E$ is
contained in $E'$. (Use 9.2.7.) We shall call this $V$, or $V_{E'}$, the **interior** of the subtopos $E'$ of $E$. The
opens $U$ and $V$ of $E$ are disjoint ($U\cap V = \emptyset$); the closed subtopos of $E$ complementary to
$\operatorname{Sup}(U,V) = U\cup V$

[PDF p. 476]

is called the **boundary** of the subtopos $E'$ of $E$.

**c)** In order for $E'$ to be an open (resp. closed) subtopos of $E$, it is necessary and sufficient that it be equal
to its interior (resp. to its closure). In order for the boundary of $E'$ to be empty, it is necessary and sufficient
that $E'$ be an open and closed subtopos of $E$; or equivalently, that it be the open subtopos of $E$ defined by an open
$V$ of $E$ which is a direct factor of the final object $e$, i.e. such that there exists a subobject $U$ of $e$ with
$e\simeq U\amalg V$. In order for the exterior of $E'$ to be "empty", i.e. for the closure to be equal to $E$, it is
necessary and sufficient that $i : E'\to E$ be dominant (8.8).

**d)** Let $S$ be an object of $E$, let $F = E/S$ be the induced topos, and let $F'$ be the subtopos of $F$ induced by
the subtopos $E'$ of $E$. Show that the exterior (resp. the closure, resp. the interior, resp. the boundary) of $F'$ is
induced by the exterior (resp. ...) of $E'$.

**Exercise 9.4.9 (locally closed subtopoi of a topos).** A subtopos $F$ of a topos $E$ is called a **locally closed
subtopos** of $E$ if it is an intersection of an open subtopos and a closed subtopos.

**a)** Prove that the intersection of a finite family of locally closed subtopoi of $E$ is locally closed. If
$g : E'\to E$ is a morphism of topoi, prove that the inverse image (9.1.6 d)) of a locally closed subtopos of $E$ is a
locally closed subtopos of $E'$.

**b)** Let $X$ be a topological space, and let $E = Top(X)$. For every subset $X'$ of $X$, consider the subtopos $T(X')$
of $E$ which is the essential image of $Top(X')$ in $Top(X)$. Show that if $X'$ is a locally closed subset, $T(X')$ is a
locally closed subtopos of $E$, the converse being true if one further assumes $X$ and $X'$ sober. Prove that
$X'\mapsto T(X')$ establishes an isomorphism of ordered sets between the set of locally closed subsets $X'$ of $X$ and
the set of locally closed subtopoi of $E$.

**c)** Let $F$ be a subtopos of $E$. Show that every open subtopos of

[PDF p. 477]

$F$ is induced by an open subtopos of $E$ (use 9.1.8 e)). Show that $F$ is a locally closed subtopos of $E$ if and only
if it is an open subtopos of its closure (9.4.8 a)). Conclude, using 9.4.8 d), that the property for $F$ of being a
locally closed subtopos of $E$ is local on $E$.

**d)** Let $F$ be a locally closed subtopos of $E$. Show that among all ways of writing $F$ as an intersection of an
open subtopos $U$ and a closed subtopos $G$ of $E$, there is one with $G$ as small as possible, and $U$ as large as
possible. (Take $G =$ closure of $F$, and $U =$ the largest open subtopos inducing $F$ on $G$.) Compatibility of the
formation of $U$, $G$ with localization on $E$.

**Exercise 9.4.10.** Develop the notion of constructible, locally constructible, quasi-constructible, and locally
quasi-constructible subtopos, on the model of the familiar notions in the case of topological spaces (EGA 0_III 9.1, EGA
IV 10.1). In the case of a topos of the form $Top(X)$, one will recover a bijection between the set of constructible
(resp. ...) subsets of $X$, and the set of constructible (resp. ...) subtopoi of $Top(X)$.

**9.5. The Gluing Theorem.**

**9.5.1.** Let $f : A\to B$ be a functor between two categories. Denote by $(B,A,f)$ the following category: the objects
of $(B,A,f)$ are the triples

```text
(X, Y, u)
```

where $X$ is an object of $B$, $Y$ an object of $A$, and $u$ a morphism from $X$ to $f(Y)$; the morphisms between two
objects $(X,Y,u)$ and $(X',Y',u')$ are the pairs $(m,m')$, where $m$ is a morphism from $X$ to $X'$ and $m'$ a morphism
from $Y$ to $Y'$, such that the following diagram is commutative:

```text
X   --u-->    f(Y)
|             |
m             f(m')
|             |
v             v
X'  --u'-->   f(Y').
```

[PDF p. 478]

The composition of morphisms is defined in the evident way.

**9.5.2.** Remark that the category $(B,A,f)$ depends functorially on the system of data $A$, $B$, $f$, in a sense which
we leave to the reader to make precise. In particular, if $f'$ is a second functor from $A$ to $B$, then every morphism
of functors

```text
f -> f'
```

defines a functor $(B,A,f)\to (B,A,f')$, which is an isomorphism if $f\to f'$ is one.

**9.5.3.** Return to the situation of 9.3, and consider the category

```text
(F, E/U, p)
```

defined in 9.5.1. To every object $X$ of $E$ corresponds an object

```text
(i^*X, j^*X, eta(X) : i^*X -> p j^*X)
```

of $(F,E/U,p)$, where $\eta(X)$ is obtained by applying the functor $i^*$ to the adjunction morphism

```text
X -> j_* j^*(X)
```

(one has $p = i^*j_*$ (9.3.6)). Thus we have defined a functor

```text
(9.5.3.1)    phi : E -> (F, E/U, p).
```

**Theorem 9.5.4.**

**a)** Let $E$ be a topos, $E/U$ an open subtopos of $E$, and $F$ the complementary closed subtopos. The functor

```text
p = i^* j_* : E/U -> F
```

is left exact and accessible, and the functor $\phi$ (9.5.3.1) is an equivalence of categories.

**b)** Conversely, let $U$ and $F$ be two topoi and let $p : U\to F$ be a gluing functor (9.3.6), i.e. accessible (I
9.2) and left exact. The category

```text
E = (F, U, p)
```

is a topos. Let $0_F$ be an initial object of $F$, let $e_U$ be a final object of $U$, and let

```text
calU = (0_F, e_U, 0_F -> p(e_U)) in Ob E.
```

The functor

```text
X |-> (0_F, X, 0_F -> p(X))
```

induces an equivalence of $U$ onto $E/\mathcal{U}$, hence with the open subtopos $U$ of $E$ defined by $\mathcal{U}$.
The functor

```text
Y |-> (Y, e_U, Y -> p(e_U))
```

is a closed embedding (9.3.5), i.e. induces an equivalence of $F$ with a closed subtopos $F'$ of $E$. The subtopoi $U$
and

[PDF p. 479]

$F'$ are complementary. Let $p' : U\to F'$ be the gluing functor. The functors $p$ and $p'$ are compatible with the
equivalences displayed above.

**Definition 9.5.5.** Let $U$ and $F$ be two topoi and let $p : U\to F$ be a gluing functor (9.3.6). The topos $(F,U,p)$
is called the **topos constructed from $U$ and $F$ by gluing with the aid of the functor $p$**.

**9.5.6. Proof of 9.5.4 a).** (*) The first assertion is just a reminder of 9.4.1 d). The pair of functors $(i^*,j^*)$
is conservative, or equivalently faithful (9.4.1 c)). A fortiori the functor $\phi$ is faithful.

Let us show that it is fully faithful. It follows from 9.3.3 b) that, for every object $X$ of $E$, the following diagram
is cartesian:

```text
(x)        X  ---------->  j_* j^* X
           |                |
           v                v
       i_* i^* X  ---->  i_* i^* j_* j^* X.
```

Let $X$ and $Y$ be two objects of $E$, and let

```text
(m, m') : phi(X) -> phi(Y)
```

be a morphism between $\phi(X)$ and $\phi(Y)$. Using the functoriality of the cartesian product and the diagrams $(x)$,
one obtains a morphism

```text
w : X -> Y
```

which makes the following diagrams commutative:

```text
X --w--> Y                         X --w--> Y
|                                  |
v                                  v
j_*j^*X --j_*m'--> j_*j^*Y         i_*i^*X --i_*m--> i_*i^*Y.
```

(*) For a gluing statement more general than 9.5.4, cf. Exercise.

[PDF p. 480]

Applying respectively the functors $j^*$ and $i^*$, one obtains:

```text
j^*(w) = m',        i^*(w) = m.
```

Let us now show that the functor $\phi$ is essentially surjective. Let

```text
(Y, X, u : Y -> p(X))
```

be an object of $(F,E/U,p)$, where $p = i^*j_*$. We deduce a diagram:

```text
j_*X
  |
  v
i_*i^*j_*X  <--i_*u--  i_*Y.
```

Hence, by taking the fiber product, a cartesian diagram:

```text
(xx)       W  ---------->  j_*X
           |                |
           v                v
         i_*Y --i_*u-->  i_*i^*j_*X.
```

We leave it to the reader to show that $\phi(W)$ is isomorphic to $(Y,X,u : Y\to p(X))$, and that the diagram $(xx)$ is
isomorphic to the diagram $(x)$ relative to $W$.

**9.5.7. Proof of 9.5.4 b).** We shall confine ourselves to showing that $(F,U,p)$ is a topos. The proof of the other
assertions is left to the reader. Let us verify properties a), b), c), d) of 1.1.2.

a) Finite projective limits are representable: this is clear because the categories $U$ and $F$ are topoi, and $p$
commutes with finite projective limits.

b) Direct sums are representable, disjoint, and universal. Let

```text
(Y_i -> p(X_i))_{i in I}
```

be a family of objects of $(F,U,p)$. By the definition of inductive limits, one has a canonical morphism

[PDF p. 481]

```text
coproduct_i Y_i -> p(coproduct_i X_i),
```

hence, by composing with the morphism $\coprod_i u_i$, a morphism which makes the corresponding object the direct sum of
the family under consideration. One immediately verifies that this direct sum is disjoint and universal.

c) Equivalence relations are effective and universal. Let an equivalence relation on the object $Y\to p(X)$ be given. It
induces an equivalence relation on $Y$ in $F$ and an equivalence relation on $X$ in $U$. The quotients $Y/R_Y$,
$p(X)/p(R_X)$, $X/R_X$ are representable in $F$ and $U$, because these categories are topoi. Moreover, by definition of
inductive limits, the canonical morphism $p(X)\to p(X/R_X)$ factors through $p(X)/p(R_X)$. We deduce, by functoriality
of inductive limits, a canonical morphism

```text
Y/R_Y -> p(X/R_X).
```

One verifies that this latter object is the quotient of $Y\to p(X)$ by the equivalence relation considered, that this
quotient is effective (I 10), and that all these properties are preserved by base change.

d) $(F,U,p)$ admits a small generating family. This property follows from I 9.2.5, taking account of the fact that $p$
is accessible, by taking $B = (0_F\to p(e_U))$, $E_0 = F$, $E_1 = U$, and the functor $p : E_1\to E_0$, whence
$\operatorname{Hom}_E(B,E) = (F,U,p)$.

One can also avoid recourse to I 9.2.5 (whose proof given there was rather painful!) and use the hypothesis on $p$ in
the form that $p$ admits a pro-adjoint.

[PDF p. 482]

(This interpretation (I 8) rests on I 8, whose proof is much more comprehensible.) It then suffices to note that if $C'$
(resp. $C''$) is a generating subcategory of $F$ (resp. $U$), and if, for every $X''\in \operatorname{Ob} C''$, one
represents the pro-adjoint pro-object by a small filtered projective system, then the family of objects of $(F,U,p)$
which are either of the form coming from $C'$, or of the form coming from these systems associated with the objects of
$C''$, is a generating family (evidently small) if $C'$, $C''$ are chosen small. Verification of this fact is indeed
immediate, and is left to the reader.

**9.5.8.** Use the notation of 9.5.7 b), and let us show how one can make explicit, up to canonical isomorphisms of
functors, the system of functors (9.3.6.2), where $E = (F,U,p)$. The details of the verifications of the assertions
below (essentially mechanical with the aid of 9.5.4) are left to the reader.

**9.5.8.1.** The functor

```text
j^* : (F, U, p) -> U
```

is given by

```text
j^*(Y, X, u : Y -> p(X)) = X.
```

**9.5.8.2.** The functor

```text
j_! : U -> (F, U, p)
```

is given by

```text
j_!(X) = (0_F, X, 0_F -> p(X)),
```

where $0_F$ is the initial object of $F$.

**9.5.8.3.** The adjunction morphism

```text
j_!j^* -> id
```

is isomorphic to the functorial morphism

```text
(0_F, X, 0_F -> p(X)) -> (Y, X, u),
```

given by the unique morphism $0_F\to Y$ and the identity of $X$.

[PDF p. 483]

**9.5.8.4.** The functor

```text
i^* : (F, U, p) -> F
```

is given by

```text
i^*(Y, X, u : Y -> p(X)) = Y.
```

**9.5.8.5.** The functor

```text
i_* : F -> (F, U, p)
```

is given by

```text
i_*(Y) = (Y, e_U, Y -> p(e_U)),
```

where $e_U$ is the final object of $U$; since $p$ is left exact, $p(e_U)$ is final in $F$.

**9.5.8.6.** The functor

```text
j_* : U -> (F, U, p)
```

is given by

```text
j_*(X) = (p(X), X, id_{p(X)}).
```

**9.5.8.7.** The adjunction morphism

```text
id -> i_*i^*
```

is isomorphic to the functorial morphism

```text
(Y, X, u) -> (Y, e_U, Y -> p(e_U)),
```

given by the identity of $Y$ and the structural morphism $X\to e_U$.

**9.5.8.8.** The adjunction morphism

```text
id -> j_*j^*
```

is isomorphic to the functorial morphism

```text
(Y, X, u) -> (p(X), X, id_{p(X)}),
```

given by $u : Y\to p(X)$ and the identity of $X$.

**Exercise 9.5.9 (exactness properties of a glued topos).** Let $U$, $F$ be two topoi, let $p : U\to F$ be a gluing
functor, let $E = (F,U,p)$ be the glued topos, and let $j : U\to E$ and $i : F\to E$ be the canonical morphisms of
topoi, so that $p = i^*j_*$.

a) Prove that $i_*$ commutes with small products, i.e. (I 8 or 2.8) the functor $i^*$ admits a left adjoint $i_!$, if
and only if the same is true of $p$, i.e. (loc. cit.) if and only if $p$ admits a left adjoint

[PDF p. 484]

```text
q : F -> U
```

(or equivalently if and only if the pro-adjoint of $p$ restricted to $F$ (9.3.6) factors up to isomorphism through $U$).
One then has $q = j^*i_!$. Thus the gluing functors $p$ having this property correspond up to isomorphism to the
functors $q : F\to U$ which have a right adjoint, i.e. (I 6) which commute with $U$-inductive limits, or equivalently
which are continuous. When $F$ is equivalent to a topos $\widetilde{C}$, where $C$ is a $U$-site, these functors
therefore correspond up to isomorphism to continuous functors $C\to U$ (III 1.2 and 1.7).

b) Suppose that the functor $i_!$ is defined. Show that, in order for $i_!$ to commute with a specified type of small
projective limits, it is necessary and sufficient that $q : F\to U$ commute with them. (For necessity, use the fact that
$j^*$ commutes with small projective limits; for sufficiency, use the equivalent description of $E$ in terms of $q$ as
formed by triples $(Y,X,u)$ with $Y\in \operatorname{Ob} F$, $X\in \operatorname{Ob} U$, $u : q(Y)\to X$.)

c) Deduce from a) and b) an example of a closed embedding of topoi $i : F\to E$ such that $i_!$ exists, but commutes
neither with fiber products nor with filtered projective limits. (It suffices to find a continuous functor between two
topoi which has neither of these two exactness properties.)

**Exercise 9.5.10 (gluing of topoi of the form $\widehat{C}$).** Let $C$ be a small category, and let $E = \widehat{C}$,
which is a $U$-topos.

**a)** Recall that the opens $U$ of $E$ correspond to sieves $C'$ of $C$ (1.4.1, 4.2), $E/U$ then being equivalent to
$\widehat{C'}$, the functor

```text
j^* : E -> E/U
```

being identified with the restriction functor (1.5.11), i.e. the inclusion morphism $j : E/U\to E$ being
$\widetilde{f} : \widehat{C'}\to \widehat{C}$ (4.6.1), where $f : C'\to C$ is the inclusion. Let $C''$ be the full
subcategory of $C$ complementary to $C'$ (i.e. $\operatorname{Ob} C''$ is the complement of $\operatorname{Ob} C'$ in
$\operatorname{Ob} C$), and let $g : C''\to C$ be the inclusion. Then the closed subtopos $F$ of $E = \widehat{C}$,
complementary to the open subtopos defined by $C'$, is canonically equivalent to $\widehat{C''}$, and the inclusion
morphism $i : F\to E$ is identified with $\widetilde{g} : \widehat{C''}\to \widehat{C}$.

[PDF p. 485]

**b)** Consider the functor

```text
(9.5.10.1)    h : (C')^op times C'' -> (Ens),        h(X', X'') = Hom_C(X', X''),
```

and note that $C$ is reconstructed up to isomorphism, with its full subcategory $C'$, from the knowledge of the
categories $C'$, $C''$ and the bifunctor $h$ (the latter being allowed to be chosen arbitrarily). (Compare 9.7.1 below.)
The datum of $h$ is equivalent to that of a functor

```text
C'' -> Chat' = Hom((C')^op, (Ens));
```

or again (III 1.2 and 1.7) to that of a continuous functor, i.e. (I 6) commuting with small inductive limits, or
equivalently admitting a right adjoint,

```text
(9.5.10.3)    Chat'' -> Chat'.
```

Show that the latter is none other than the gluing functor associated with the open subtopos $\widehat{C'}$ of
$E = \widehat{C}$.

**c)** Deduce from a) and b) that if one is given a gluing functor (9.5.10.3) between two categories of presheaves,
hence a glued topos $E$, the following conditions are equivalent:

**(i)** $E$ is equivalent to a topos of the form $\widehat{C}$.

**(ii)** The functor $p$ commutes with small products, or equivalently it admits a left adjoint (9.5.10.2).

**(iii)** The inclusion morphism $i : \widehat{C''}\to E$ is "essential", i.e. $i^*$ commutes with products, or
equivalently $i^*$ admits a left adjoint.

When this is so, make explicit a category $C$ such that $E\simeq \widehat{C}$, using the bifunctor (9.5.10.1) defined by
the restriction of (9.5.10.2).

**d)** Show that a topos obtained by gluing two punctual topoi is not necessarily equivalent to a topos of the form
$\widehat{C}$.

**Exercise 9.5.11 (morphism from a glued topos into a topos).**

a) Let $p : U\to F$ be a functor between two categories,

[PDF p. 486]

let $E = (F,U,p)$ be the "glued" category of 9.5.1, and let $G$ be an arbitrary category. Consider the functor induced
by $p$

```text
Hom(G, U) -> Hom(G, F),
```

and define an equivalence of categories

```text
Hom(G, E) ~= (Hom(G, F), Hom(G, U), p_*).
```

b) Let $f : G\to E$ be a functor, and consider its composites with the canonical functors $j^* : E\to U$ and
$i^* : E\to F$. Show that $f$ commutes with a specified type of inductive limits (assumed representable in $U$ and $F$,
hence in $E$) if and only if $j^*f$ and $i^*f$ commute with them. Show that if $f$ commutes with a specified type of
projective limits (which is therefore representable in $E$), then $f$ commutes with them if and only if the same is true
of $j^*f$ and $i^*f$.

c) Now suppose that $U$ and $F$ are topoi, and that $p$ is a gluing functor. Let $G$ be a topos, and let $f : G\to E$ be
a functor. Conclude from b) that $f$ is an inverse image functor associated with a morphism of topoi $E\to G$ if and
only if the same is true of the functors $j^*f : G\to U$ and $i^*f : G\to F$.

Conclude from this and from a) that one has an equivalence between the category $\operatorname{Homtop}(E,G)$ and the
category of triples $(f',f'',u)$, where $f'$ (resp. $f''$) is an object of $\operatorname{Homtop}(U,G)$ (resp.
$\operatorname{Homtop}(F,G)$), and where $u$ is a homomorphism of functors compatible with the gluing. If $f$ is an
object of $\operatorname{Homtop}(E,G)$, and $(f',f'',u)$ the corresponding triple, then

```text
f' = f o j,        f'' = f o i.
```

d) Specify in what sense one may say that c) gives a characterization up to equivalence (in a 2-category of topoi) of
the topos $E$ in terms of the triple $(U,F,p)$.

**Exercise 9.5.12 (gluing of two topological spaces).**

a) Let $X$ be a topological space,

```text
p : Top(X) -> (Ens) = Top(pt)
```

a gluing functor, i.e. (I 8) a prorepresentable functor, let $A\in \operatorname{Ob}\operatorname{Pro}(Top(X))$ be the
object which prorepresents it, and let $E$ be the topos deduced from $p$ by gluing. Show that $E$ is equivalent to a
topos of the form $Top(Y)$ if and only if $A$ is isomorphic to an object of $\operatorname{Pro}(\operatorname{Ouv}(X))$.

[PDF p. 487]

Conclude that if $X$ is not empty, one can find $p$ such that $E$ is not equivalent to a topos of the form $Top(Y)$.

b) More generally, consider a gluing functor

```text
p : Top(X) -> Top(Y),
```

with $X$, $Y$ two topological spaces. Deduce from it a map

```text
phi : X -> Ob Pro(Top(Y)),
```

composed of $X\to \operatorname{Ob}\operatorname{Point}(Top(X))\to \operatorname{Ob}\operatorname{Pro}(Top(X))$ (6.8.5)
and the pro-adjoint of $p$. (N.B. for $x\in X$, $\phi(x)$ is identified with the fiber at $x$ of the gluing sheaf
(9.6.4) defined by $p$.) Show that if $E$ is equivalent to a topos of the form $Top(Z)$, then $\phi$ takes its values in
the essential image of $\operatorname{Pro}(\operatorname{Ouv}(Y))$.

Problem: is there a converse?

**9.6. Gluing Sheaf.** We saw in 9.5.4 that the datum of a topos $E$ endowed with an open $U$ essentially amounts to the
datum of two topoi $U$ and $F$, and of a gluing functor

```text
(9.6.1)    p : U -> F,
```

i.e. of a functor admitting a pro-adjoint

```text
(9.6.2)    q : Pro(F) -> Pro(U).
```

By the sorites on pro-adjoint functors (I 8), the functor $p$ is known up to unique isomorphism (and consequently the
glued topos $E = (F,U,p)$ is known up to equivalence of topoi) once one knows the functor $q$, or equivalently the
functor induced by $q$

```text
(9.6.3)    F -> Pro(U).
```

The functor $q$ is determined, up to unique isomorphism, by the property of commuting with small filtered projective
limits and of extending the functor (9.6.3). On the other hand, in order for a given functor (9.6.3) to be isomorphic to
a pro-adjoint, it is evidently necessary and sufficient that, for every object $X$ of $U$, the contravariant functor

[PDF p. 488]

```text
Y |-> Hom_{Pro(U)}(X, q(Y))
```

on $F$ be representable, or equivalently be a sheaf on $F$ for the canonical topology (1.1.2 (iii)). One immediately
sees that this also means that the opposite functor

```text
(9.6.4)    q^o : F^o -> Pro(U)^o
```

is a sheaf on $F$ with values in $\operatorname{Pro}(U)^o$ (II 6.1). Thus the datum of a gluing functor (9.6.1) is also
equivalent, up to isomorphism, to that of a sheaf on $F$ with values in $\operatorname{Pro}(U)^o$. The sheaf thus
associated with a gluing functor (or with a situation $(E,U,F)$ as in 9.3) is called the **gluing sheaf** associated
with the gluing functor under consideration $p$ (resp. with the open $U$ of the topos $E$).

**Exercise 9.6.5.** Refine 9.5.4 into a statement of 2-equivalence of categories, between the 2-category formed by pairs
$(E,U)$ consisting of a topos $E$ and an open $U$ of it, and the 2-category formed by triples $(U,F,p)$ consisting of
topoi $U$, $F$ and a gluing functor $p : U\to F$ (the explicit description of the 2-categories in question being left to
the reader). Give a variant of this statement involving the 2-category of triples $(U,F,Q)$, where $Q$ is now a sheaf on
$F$ with values in $\operatorname{Pro}(U)^o$.

## 9.7. Points of a Glued Topos

**9.7.1.** Let $C$ be a category, and let

```text
u : D' -> C,        v : D'' -> C
```

be two fully faithful functors. Denote by $C'$, $C''$ their essential images, and suppose that

```text
Ob C' cap Ob C'' = emptyset,        Ob C' union Ob C'' = Ob C.
```

Suppose moreover that

```text
X' in Ob C', X'' in Ob C''  =>  Hom(X'', X') = emptyset,
```

or, what amounts to the same thing, that

```text
Hom(v(A''), u(A')) = emptyset        for A' in Ob D', A'' in Ob D''.
```

It is then immediate that the category $C$ is reconstructed, up to canonical isomorphism, from the knowledge of the
categories $C'$ and $C''$ and of the functor

[PDF p. 489]

```text
(X', X'') |-> Hom(X', X'') : (C')^o times C'' -> (Ens).
```

Similarly, $C$ is reconstructed up to equivalence, the latter being defined up to unique isomorphism, from the knowledge
of $D'$, $D''$ and of the functor

```text
(A', A'') |-> Hom(u(A'), v(A'')) : (D')^o times D'' -> (Ens).
```

This remark applies in particular to the situation described in the following proposition. It shows that the category
$\operatorname{Point}(E)$ is determined, up to equivalence, by the knowledge of the categories $\operatorname{Point}(U)$
and $\operatorname{Point}(F)$ and of a certain functor

```text
Point(U)^o times Point(F) -> (Ens)
```

deduced from the gluing functor $p : U\to F$.

**Proposition 9.7.2.** Let $E$ be a topos, let $U$ be an open of $E$, and let $F = E-U$ be the complementary closed
subtopos of $U$. Consider the functors induced by the inclusion morphisms

```text
(9.7.2.1)    u : Point(U) -> Point(E),        v : Point(F) -> Point(E).
```

Then:

**a)** The functors $u$ and $v$ are fully faithful, and every point of $E$ belongs to the essential image of one of the
two functors $u$ and $v$, exclusively.

**b)** Let $p$ and $a$ be two points of $E$, such that $p$ belongs to the essential image of $u$ and $a$ to the
essential image of $v$. Then

```text
(9.7.2.2)    Hom(a, p) = emptyset.
```

**c)** Let $x$ be a point of $U$ and $a$ a point of $F$. One has an isomorphism, functorial in $(a,x)$:

```text
(9.7.2.3)    Hom(u(x), v(a))
              ~= Hom_{Pro(F)}(Pro(p)(x), a)
              ~= Hom_{Pro(U)}(x, q(a)),
```

where

```text
q : Pro(F) -> Pro(U)
```

is the functor (9.6.2) pro-adjoint to the gluing functor $p : U\to F$, and where one has identified, up to equivalence,
the categories $\operatorname{Point}(U)$ and $\operatorname{Point}(F)$ with full subcategories of
$\operatorname{Pro}(U)$ and $\operatorname{Pro}(F)$ respectively (6.8.5).

**Proof.** For a), the full faithfulness of $u$ and $v$ is known (9.1.4). The assertion about their essential images
follows from the criteria 9.2.5 and 9.2.4 for a point $P\to E$ to factor, up to isomorphism, through $U$ resp. through
$F$, taking account of the fact that the punctual topos $P$ has only two opens, namely the initial object and the final
object of $P$.

For b), taking a) into account, the assertion means that if the point $p : P\to E$ factors through $U$, then so does
every point $p' : P'\to E$ such that $\operatorname{Hom}(p',p)\ne\emptyset$. But a morphism $p'\to p$ induces
$p^*(U)\to p'^*(U)$, and then $p^*(U) = e_P$ implies $p'^*(U) = e_{P'}$, as was to be shown.

For c), thanks to Lemma 9.7.2.4 below, applied to the inclusions $j : U\to E$ and $i : F\to E$, one has a diagram of
functors commutative up to canonical isomorphisms:

```text
Point(U)  ->  Point(E)  <-  Point(F)
   |             |             |
   v             v             v
Pro(U)    ->    Pro(E)   <-    Pro(F),
```

where the vertical arrows denote the canonical fully faithful functors (6.8.5). On the other hand, since $i^*$ admits a
left adjoint, $\operatorname{Pro}(i_*)$ admits a left adjoint $\operatorname{Pro}(i^*)$ (I 8), and one finally obtains
functorial isomorphisms

```text
Hom(u(x), v(a))
  ~= Hom_{Pro(E)}(Pro(j_*)(x), Pro(i_*)(a))
  ~= Hom_{Pro(F)}(Pro(i^*)Pro(j_*)(x), a).
```

This is none other than the first formula (9.7.2.3), the second then being trivial by definition of $q$ as pro-adjoint
to the gluing functor. This proves 9.7.2, modulo the following lemma.

**Lemma 9.7.2.4.** Let $f : F\to E$ be a morphism of topoi. Then the diagram of functors

```text
(9.7.2.4.1)    Point(F)  ->  Point(E)
                    |           |
                    v           v
                Pro(F)    ->   Pro(E)
```

is commutative up to canonical isomorphism, the vertical arrows denoting the fully faithful functors (6.8.5).

[PDF p. 491]

The verification is immediate from the definitions and is left to the reader.

**Corollary 9.7.3.** Let $E$ be a topos admitting enough points. Then the same is true for every closed subtopos $F$ of
$E$. More precisely, if $(P_i)_{i\in I}$ is a conservative family of points of $E$, then the family of points of $F$
defined by the subfamily $(P_i)_{i\in J}$ formed by those $P_i$ which come from points of $F$, is conservative. (Compare
6.7.3 and 6.7.4.)

Indeed, let $f : X\to Y$ be an arrow of $F$ transformed into an isomorphism by the fiber functors associated with the
points under consideration of $F$. Since $i^*i_*\simeq \operatorname{id}_F$, one sees that $i_*(f) : i_*(X)\to i_*(Y)$
is transformed into an isomorphism by the fiber functors associated with the $P_i$ with $i\in J$. The same is true for
the $P_i$ with $i\in I-J$, that is, those coming from points of $U$, since $j^*i_*$ is the constant functor with value
the final object. Thus $i_*(f)$ is an isomorphism, and therefore so is $f\simeq i^*i_*(f)$, as was to be shown.

**Remark 9.7.4.** If $E$ is a topos having enough points, it is clear that an open $U$ of $E$ is determined once one
knows the full subcategory of $\operatorname{Point}(E)$ which is the essential image of $\operatorname{Point}(U)$. In
fact, if $C$ is a full subcategory of $\operatorname{Point}(E)$ defining a conservative family of points of $E$, it even
suffices to know the subcategory $C_U$ of the elements of $C$ belonging to the essential image of $\operatorname
{Point}(U)$.

From this and from 9.7.2 a), it follows that a closed subtopos $F$ of $E$ is determined once one knows the essential
image of $\operatorname{Point}(F)$ in $\operatorname{Point}(E)$, or even only its intersection with $C$.

**Exercise 9.7.5.** Let $E$ be a topos. For every subtopos $F$ of $E$, let $P(F)$ be the subset of $\operatorname
{Point}(E)$ formed by the isomorphism classes of points of $E$ which factor through $F$. Thus, $P(F)$ is homeomorphic to
$\operatorname{Point}(F)$ (9.1.8 c)). Show that if $F$ is an open (resp. closed, resp. locally closed (9.4.9)) subtopos
of $E$, then $P(F)$ is a

[PDF p. 492]

open (resp. closed, resp. locally closed) subset of $\operatorname{Point}(E)$.

Show that, when $E$ has enough points, the same is true for every locally closed subtopos of $E$, and that the map
$F\mapsto P(F)$ induces a bijection between the set of open (resp. closed, resp. locally closed) subtopoi of $E$, and
the set of open (resp. closed, resp. locally closed) subsets of $\operatorname{Point}(E)$.

Generalize the preceding considerations to the case where $\operatorname{Point}(E)$ is replaced by any subspace $X$ of
$\operatorname{Point}(E)$ corresponding to a conservative family of points of $E$.

## 9.8. Complements on Certain Topoi Related to Topological Spaces

In this section we indicate a few complements, which will be given in the form of exercises. The reader is advised to go
through them, to become accustomed to the viewpoint of topoi in various situations of classical type.

**Exercise 9.8.1 (descent of sheaves on a topological space).** Let $f : X\to Y$ be a continuous map of topological
spaces $\in U$, hence a functor

```text
f^* : Top(Y) -> Top(X).
```

**a)** The following conditions are equivalent:

**(i)** $f^*$ is faithful.

**(ii)** $f^*$ is conservative.

**(iii)** $f(X)$ is a very dense subset (EGA IV 10.1.3) of $Y$.

It suffices for this that $f$ or $f_{\mathrm{sob}}$ be surjective. Give an example where $f^*$ is faithful and where
$f = f_{\mathrm{sob}}$ is not surjective (take $X$ discrete, $f$ injective, $f(X)$ the set of closed points of $Y$, $Y$
a non-discrete noetherian topological space). Give an example where $f_{\mathrm{sob}}$ is surjective but not $f$, and
another where $f$ is surjective but not $f_{\mathrm{sob}}$.

**b)** Suppose $f(X)$ very dense in $Y$, and its topology the quotient topology of that of $X$. Prove that the arrow $f$
of $(\mathrm{Esp})$ is a descent morphism for the fibered category of sheaves of sets on variable spaces, i.e. that the
functor $f^*$ induces a fully

[PDF p. 493]

faithful functor from the category $Top(Y)$ to the category of objects of $Top(X)$ endowed with descent data relative to
$f : X\to Y$. Reduce to the case where $f$ is surjective, and imitate the reasoning of VIII 9.1 given in the context of
the etale topologies of schemes. Give a converse.

**c)** Suppose that $f(X)$ is very dense in $Y$, that its topology is the quotient topology of that of $X$, and that the
fibers of $f$ are connected. Prove that the functor $f^*$ is fully faithful. (Imitate the reasoning of SGA 1 IX 3.4.)
Give a converse, at least if the points of $Y$ are closed.

**d)** Suppose that $Y$ is a union of opens $Y_i$ over which $X$ admits sections. Prove that then $f$ is an effective
descent morphism for the fibered category of sheaves of sets on variable topological spaces, i.e. that the functor
considered in c) is even an equivalence of categories.

**Exercise 9.8.2 (quotient topoi of topological spaces. Topological spreads).**

**a)** Let

```text
(9.8.2.1)        X_2 => X_1 => X_0
                         p_1,p_2
```

be a semi-simplicial object truncated at order 2 of the category $(\mathrm{Esp})$ of topological spaces $\in U$, hence,
by the inverse image functors, a diagram of categories of sheaves

```text
Top(X_0) => Top(X_1) => Top(X_2).
```

More precisely, one has a cofibered category over the category of standard simplices $\Delta_n$, $0\leq n\leq 2$. Show
that the category $\operatorname{Lim}$ of this diagram, i.e. the category of sheaves of sets on $X_0$ endowed with
descent data relative to the diagram (9.8.2.1), i.e. with an isomorphism $p_1^*(F)\simeq p_2^*(F)$ such that ..., is a
$U$-topos $T$. (For a more general statement of stability of topoi under $\lim$ operations, cf. VI.) Define a morphism
of topoi $a : Top(X_0)\to T$, and prove that, for every

[PDF p. 494]

$U$-topos $E$, $\operatorname{Homtop}(T,E)$ is equivalent, via $a^*$, to the category $\operatorname{Lim}$ of the
following diagram of categories, deduced from (9.8.2.1):

```text
Homtop(Top(X_0), E) => Homtop(Top(X_1), E) => Homtop(Top(X_2), E).
```

**b)** In particular, let $R$ be an equivalence relation in an object $X$ of $(\mathrm{Esp})$, i.e. (I 10) a subobject
$R$ of $X\times X$ (N.B. the inclusion $R\hookrightarrow X\times X$ is continuous, but the topology of $R$ is not
necessarily induced by that of $X\times X$), such that, for every object $Y$ of $(\mathrm{Esp})$, $\operatorname{Hom}
(Y,R)$ is the graph of an equivalence relation in $\operatorname{Hom}(Y,X)$. We deduce a diagram of the form (9.8.2.1),
with

```text
X_0 = X,
X_1 = R,
X_2 = (R, p_2) times_X (R, p_1),
```

where $p_1$, $p_2$ are the two projections from $R$ to $X$, hence a topos, which we denote by $Top(X)/R$, or even
$Top(X/R)$, or also $X/R$, by abuse of notation, and which plays the role of a quotient of $X$ by $R$, in the sense made
precise by a). Suppose that the topology of $R$ is induced by that of $X\times X$, and that, denoting by $X/R$ the
ordinary quotient topological space, $X$ locally admits sections over $X/R$; prove that then $T$ is equivalent to
$Top(X/R)$. (Use 9.8.1 d).)

**c)** Let $H\to X$ be an injective morphism of topological groups, i.e. a monomorphism of group objects in
$(\mathrm{Esp})$, and let $R$ be the equivalence relation which it defines in $X$, i.e. $R = H\times X$, with
$p_1 = \operatorname{pr}_2$ and $p_2$ defined by the action of $H$ on $X$ via left translations. Show that, in order for
the topology of $R$ to be induced by that of $X\times X$, it is necessary and sufficient that the topology of $H$ be
induced by that of $X$. Give examples where this condition is not fulfilled, and where the ordinary quotient topology of
$X/H$ is the coarse topology, with:

```text
a) H = Z times Z, X = R,
b) H = R,         X = T times T, with T = R/Z,
```

("geodesics of the torus"). Prove that the two topoi obtained are equivalent and are not equivalent to $Top(X/H)$

(which is a final topos (2.2)), nor to any topos of the form $Top(Y)$.

**d)** Let $G$ be a topological group acting on a topological space $X$, hence, in the well-known way, a semi-simplicial
object

[PDF p. 495]

```text
... G times G times X => G times X => X.
```

Show that the topos $T$ deduced from it by virtue of a) is identified with the category of spaces $X'$ with group of
operators $G$ over $X$, such that $X'\to X$ is an etale space (compatible with the action of $G$). In particular, when
$G$ is discrete, one recovers the topos $Top(X,G)$ of 2.3.

The preceding considerations justify the notation $Top(X)/G$, or even $Top(X/G)$, or simply $X/G$, for the preceding
topos $T$. Be careful, however, that when $G$ is a discrete group (to fix ideas) acting properly on $X$, so that the
ordinary quotient space $X/G$ has reasonably good properties, the natural morphism of topoi $T\to Top(X/G)$, deduced
from the universal characterization a) of $T$, is an equivalence of topoi only if $G$ acts freely, i.e. without fixed
points, i.e. when $G\times X\to X\times X$ is a monomorphism. Thus, in the case of a "pre-equivalence relation" (or
"groupoid" in the sense of SGA 3 V 1) which is not an equivalence relation, the notion of passing to the quotient in the
sense of topoi (or "fine passage to the quotient") does not in general correspond, via the correspondence
$X\mapsto Top(X)$, to the usual passage to the topological quotient.

**e)** Let $T$ be a $U$-topos. Show that the following conditions are equivalent:

**(i)** There exists a family $(S_i)_{i\in I}$ of objects of $T$ covering the final object of $T$, such that, for every
$i\in I$, the induced topos $T/S_i$ is equivalent to a topos of the form $Top(X)$, with $X\in(\mathrm{Esp})$.

**(i')** There exists an $S\in \operatorname{Ob}(T)$ covering the final object such that the induced topos $T/S$ is
equivalent to a topos of the form $Top(X)$.

**(ii)** There exists a topological space $X$, and a pre-equivalence relation $R$ in $X$ (in the sense of the category
$(\mathrm{Esp})$) which is etale, i.e. such that $p_1 : R\to X$ is an etale space, such that $T$ is equivalent to
$Top(X/R)$, where the notation is that of b).

[PDF p. 496]

We shall then say that the topos $T$ is locally a topological space, or also that $T$ is a topological spread (or simply
a spread, if no confusion is to be feared).

**f)** Show that the topos $T$ constructed in a) has enough points, and more precisely, that it admits a conservative
family of points parametrized by the (small) set $X_0$. In particular, every spread has a small conservative family of
points, hence has enough points. When a spread $T$ is realized in the form $Top(X/R)$ as in e) ii), prove that every
point of $T$ is isomorphic to the image of a point of $Top(X)$, hence is defined by an ordinary point of $X_{\mathrm
{sob}}$ (or of $X$, when $X$ is sober).

**g)** Show that the topos $Top(X/G)$ of 2.3 is a spread. (Use its description d) or 7.1.10 c).) Show that, for every
$x\in X$, the monoid of endomorphisms of the point of $Top(X,G) = Top(X)/G$ defined by $x$ is canonically isomorphic to
the stabilizer group $G_x$ of $x$. In particular, the points of a spread may have nontrivial automorphism groups.
Determine $\operatorname{Point}(T)$ for the spread $T$ defined by an etale pre-equivalence relation in a space $X$, and
show that every endomorphism of a point of $T$ is an automorphism.

**h)** Let $T$ be a topos. Show that the following conditions are equivalent:

**(i)** For every point $p$ of $T$, every endomorphism of $p$ (resp. every automorphism of $p$) is the identity.

**(ii)** For every topos $S$ having enough points, and every morphism of topoi $f : S\to T$, every endomorphism of $f$
(resp. every automorphism of $f$) is the identity.

Show similarly that the following conditions are equivalent:

**(i')** For two points $p,q$ of $T$, there exists at most one morphism from $p$ to $q$.

**(ii')** For two morphisms $f,g : S\to T$ from a topos $S$ having enough

[PDF p. 497]

points into $T$, there exists at most one morphism from $f$ to $g$.

When these latter conditions are verified, one says that the topos $T$ is pointwise rigid, or simply rigid. Show that,
if $X$ is a topological space endowed with an etale pre-equivalence relation $R$, the quotient spread $T = Top(X)/R$ is
rigid if and only if $R$ is an equivalence relation.

**i)** Let $(X,G)$ be a topological space with a discrete group of operators, let $H$ be a normal subgroup of $G$ such
that the induced operation of $H$ on $X$ is proper and free, and let $X' = X/H$, $G' = G/H$, so that $G'$ acts on $X'$
in the evident way. Prove that the morphism of topoi

```text
Top(X, G) -> Top(X', G')
```

induced by the canonical morphism $(X,G)\to (X',G')$ of spaces with operators (4.12) is an equivalence of topoi.

Show that the set of opens of the topos $Top(X/G)$ is identified with the set of opens of $X$ stable under the action of
$G$, or equivalently with the set of opens of the topological quotient space $X/G$. Conclude that $Top(X/G)$ is
connected if and only if every subset of $X$ both open and closed and stable under the action of $G$ is empty or equal
to $X$. When the connected components of $X$ are open, $Top(X,G)$ is connected if and only if $G$ acts transitively on
the set $\pi_0(X)$ of connected components of $X$; more generally, $\pi_0(Top(X))$ (8.7 e)) is an essentially constant
pro-set isomorphic to the quotient set $\pi_0(X)/G$.

Show that, when $X$ is locally connected and locally simply connected, and $T = Top(X,G)$ is connected, i.e. $G$
transitive on $\pi_0(X)$, then among all ways of realizing $T$ by means of a space with operators $(X',G')$ (cf. above
for some such ways), there is one, unique up to non-unique isomorphism, for which $X'$ is connected and simply
connected. Show that the choice of such an $(X',G')$ amounts to the choice of a "universal covering" of the final object
of $T$, and that $G'$ is isomorphic to the group $\pi_1(T)$ relative to this universal covering (cf. 2.7.5).

[PDF p. 498]

Hint: show that the datum of an equivalence of $T$ with a $Top(X,G)$ amounts to the datum of a $G_T$-torsor $P$ in $T$,
and that, if $(X,G)$ and $P$ correspond to one another, one has a canonical equivalence $Top(X)\simeq T/P$.

Conclude from this a trivial proof of the last assertion of c). Characterize the topoi $T$ equivalent to $Top(X,G)$,
where $G$ is a discrete group acting on a locally connected and locally simply connected topological space by permuting
the connected components transitively, as being the connected, locally connected, and locally simply connected spreads
whose universal covering $P$ of the final object $e_T$ of $T$ is such that the induced topos $T/P$ is equivalent to a
topos of the form $Top(X)$ (or, as we shall simply say by abuse of language, $T/P$ "is" a topological space).

Give an example of a spread, locally isomorphic to $\mathbf{R}$, which is connected and simply connected but is not a
topological space. (Take the universal covering of the line $\mathbf{R}$ with doubled origin.)

**j)** A ringed topos $(T,O_T)$ (cf. III) is called a differentiable spread (resp. a real analytic spread, resp. a
complex analytic spread) if there exist objects $S_i$ of $T$ covering the final object, such that the induced ringed
topos $(T/S_i,O_T/S_i)$ is equivalent to the ringed topos defined by a differentiable manifold with its sheaf of real
functions $C^\infty$ (resp. to the ringed topos defined by a real analytic space, resp. to the ringed topos defined by a
complex analytic space). Give a constructive description of these ringed topoi, of the type of e) ii) (where one takes
for $X$ respectively a differentiable manifold, a complex analytic space, or a real analytic space). Give examples of
such ringed topoi which are not equivalent to ringed topoi associated with topological spaces, by returning to the
examples considered in c).

[PDF p. 499]

**Exercise 9.8.3 (topoi associated with local equivalence relations and foliations)** (*).

Let $X$ be a topological space.

**a)** For every open $U$ of $X$, let $\operatorname{Quot}(U)$ be the set of equivalence relations in $U$, and, for an
open $V\subset U$, consider the natural map $\operatorname{Quot}(U)\to \operatorname{Quot}(V)$, hence a presheaf
$\operatorname{Quot}_X$ on $X$. Let $Q_X$, or simply $Q$, be the associated sheaf, and let $r$ be a section of $Q$
("local equivalence relation on $X$"). From the order relation on the set $\operatorname{Quot}(U)$ of equivalence
relations on an open $U$ of $X$, deduce on the presheaf $\operatorname{Quot}$, and on the associated sheaf $Q$, an order
structure, i.e. a structure of presheaf, resp. of sheaf, with values in the category of ordered sets.

**b)** For every equivalence relation $R$ on $X$, consider the section $\operatorname{loc}(R)$ of $Q$ that it defines.
Let $E(r)$ be the set of equivalence relations on $X$ such that $\operatorname{loc}(R)$ is less fine than $r$, and let
$\operatorname{glob}(r)$ be the equivalence relation which is the supremum of $E(r)$, whose graph is the intersection of
the graphs of the $R\in E(r)$.

Let $(U_x)_{x\in X}$ be a family of open neighborhoods of the $x\in X$, and, for every $x\in X$, let $R_x$ be an
equivalence relation in $U_x$ whose germ at $x$ is $r_x$. For every family $V$ of opens $V_x$ ($x\in X$,
$x\in V_x\subset U_x$), let $R_V$ be the equivalence relation in $X$ generated by the family of relations $R_x|V_x$.
Show that, if $V' < V$ (in an evident sense), one has $R_{V'}\geq R_V$, and that $\operatorname{glob}(r)$ is the
supremum of the filtered increasing family of equivalence relations $R_V$. Give an example where $\operatorname{glob}
(r)$ is not in $E(r)$, i.e. where there exists an $a\in X$ such that,

(*) This exercise is given under full reserve, having been drafted hastily and insufficiently checked. Mr. N. Saavedra
has checked parts a) to e). The reader is asked to communicate any observations.

[PDF p. 500]

for every open neighborhood $W\subset U_a$ of $a$, there exist a $V = (V_x)$ and two points $y,z$ of $W$ which are
equivalent for $R_a$, but which are not equivalent for $R_V$. Show that, for every $R\in \operatorname{Quot}(X)$, one
has $\operatorname{glob}(\operatorname{loc}(R))\geq R$.

**c)** One says that $r$ is a **precoherent** (resp. **coherent**) local equivalence relation if $\operatorname{glob}
(r)\in E(r)$, i.e. $\operatorname{loc}(\operatorname{glob}(r))\leq r$ (resp. if, for every open $U$ of $X$, the
restriction of $r$ to $U$ is precoherent). One says that $r$ is **globally coherent** if it is coherent and if,
moreover, $r = \operatorname{loc}(\operatorname{glob}(r))$.

One says that an equivalence relation $R$ on $X$ is **locally coherent** if $r = \operatorname{loc}(R)$ is coherent, and
**coherent** if moreover $R = \operatorname{glob}(r)$, i.e. $R = \operatorname{glob}(\operatorname{loc}(R))$. Show that
globally coherent equivalence relations on $X$ correspond bijectively to coherent equivalence relations on $X$, by

```text
r |-> glob(r),        R |-> loc(R).
```

**d)** Show that, in order for $r$ to be coherent, it suffices that, for every $a\in X$ and every open neighborhood
$W'\subset U_a$ of $a$, there exists an open neighborhood $W\subset W'$ of $a$ such that every equivalence class of
$R_a|W$ is contained in a connected component of an equivalence class of $R_a$. A fortiori, it suffices that there exist
a fundamental family of open neighborhoods $W\subset U_a$ of $a$ such that the fibers of the induced equivalence
relation $R_a|W$ are connected.

(Hint: reduce to establishing precoherence in the case where $r$ is defined by an $R\in \operatorname{Quot}(X)$, and
note in that case that the fibers of the equivalence relations $R_V$ are relatively open subsets, hence also relatively
closed subsets, of the fibers of $R$.)

Show that, in order for a global equivalence relation $R$ to be coherent, it suffices that it be locally coherent and
that its fibers be connected; prove that this condition is necessary if the fibers are closed. Give an example of an
equivalence relation with connected and locally connected fibers, and which is not locally coherent.

[PDF p. 501]

**e)** Let $f : X'\to X$ be a continuous map. Define a natural homomorphism of presheaves

```text
f^{-1}(Quot_X) -> Quot_{X'},
```

inducing a homomorphism of sheaves $f^*(Q_X)\to Q_{X'}$. If $r$ is a local equivalence relation on $X$, we say that $f$
is a **fibered map** for the local equivalence relation $r$ on $X$ if the inverse image of $r$ is the coarse local
equivalence relation on $X'$. For every topological space $X'$, let $\operatorname{Hom}_{\mathrm{fib}}(X',X)$ be the set
of continuous maps from $X'$ to $X$ which are fibered maps relative to $r$. Show that, as $X'$ varies, one obtains a
contrafunctor in $X'$.

**f)** Suppose $r$ coherent. Show that the preceding functor is representable by a topological space $X^r$ over $X$.
Show that the universal fibered map $\phi : X^r\to X$ is bijective, and that every $x\in X^r$ admits an open
neighborhood $U$ such that the map $U\to X$ induced by $\phi$ is a homeomorphism of $U$ onto its image. Show that the
connected components of $X^r$ are open and correspond under the bijection $\phi$ to the fibers of the equivalence
relation $R = \operatorname{glob}(r)$. Give an example where the restriction of $\phi$ to the connected components of
$X^r$ does not induce homeomorphisms from these spaces to their images.

**g)** The local equivalence relation $r$ is said to be **open** if it is a section of the subsheaf $Q_{\mathrm{ouv}}$
of $Q$ coming from the subpresheaf $\operatorname{Quot}_{\mathrm{ouv}}$ of $\operatorname{Quot}_X$ whose value on every
open $U$ of $X$ is the set of open equivalence relations of $U$. We say that the local equivalence relation $r$ is
**strictly open** if it is coherent and open, or, what amounts to the same thing, if it is coherent and if, for every
open $U$ of $X$, $\operatorname{glob}(r|U)$ is an open equivalence relation in $U$. We say that the equivalence relation
$R$ in $X$ is **strictly open** if it is coherent and if $\operatorname{loc}(R)$ is a strictly open local equivalence
relation. Prove that, in order for $r$ assumed open to be strictly open, it suffices that it satisfy the condition
considered in d); if $r$ is locally defined by an $R$ with closed fibers, then this condition is also necessary.

[PDF p. 502]

**h)** Let $F$ be a sheaf of sets on $X$. For every open $U$ of $X$, let $\operatorname{Quot}(U,F)$ be the set of pairs
formed by an equivalence relation $R_U$ in $U$ and an equivalence relation $R_{F|U}$ in $F|U$ ($F$ being interpreted as
an etale space over $X$) such that the structural morphism $p : F|U\to U$ is compatible with the equivalence relations
$R_U$, $R_{F|U}$, and such that the corresponding diagram of topological spaces

```text
F|U --------------> (F|U)/R_{F|U}
 | p                       | q
 v                         v
 U ---------------->       U/R_U
```

is cartesian with $q$ an etale space, so that $F|U$ is identified with the inverse image of the sheaf $(F|U)/R_{F|U}$ on
$U/R_U$.

Show that the $\operatorname{Quot}(U,F)$, for variable $U$, define a presheaf on $X$, whose associated sheaf will be
denoted $Q(F/X)$. Define a homomorphism of sheaves $Q(F/X)\to Q_X$. For a given section $r$ of $Q_X$, an $r$-structure
on the sheaf $F$ means any section of $Q(F/X)$ over the given section $r$ of $Q_X$. Define the category $Top(X/r)$ of
$r$-sheaves on $X$, and define a conservative and faithful functor "forget the $r$-structure"

```text
Top(X/r) -> Top(X).
```

Prove that in $Top(X/r)$, finite projective limits and finite inductive limits are representable, and that the preceding
functor commutes with those limits. Conclude that, in $Top(X/r)$, finite sums are disjoint and universal and equivalence
relations are effective universal. Prove that $Top(X/r)$ admits a small generating family. Give an example with $r$
coherent where $Top(X/r)$ does not admit infinite direct sums (?), hence is not a topos.

**i)** Let $f : X\to Y$ be a continuous map compatible with $R = \operatorname{glob}(r)$. Define a functor

[PDF p. 503]

```text
f_r^* : Top(Y) -> Top(X/r)
```

whose composite with the forgetful functor $Top(X/r)\to Top(X)$ is $f^*$. Show that, if $r$ is globally coherent and
strictly open, i.e. if $R$ is strictly open and $r = \operatorname{loc}(R)$, and if $f$ is the canonical map

```text
X -> Y = X/R,
```

then $f_r^*$ is an equivalence of categories. Therefore $Top(X/r)$ is a $U$-topos, and $Top(X/r)\to Top(X)$ is the
inverse image functor of a morphism of topoi.

**j)** Conclude from i) that, if $r$ is strictly open, then $Top(X/r)$ is a topos, and the forgetful functor

$Top(X/r)\to Top(X)$ is the inverse image functor associated with a morphism of topoi

```text
p : Top(X) -> Top(X/r).
```

**k)** Define a functorial law for the topos $Top(X/r)$ and the preceding morphism of topoi $p$, with respect to the
pair $(X,r)$ of a topological space $X$ endowed with a strictly open local equivalence relation. Show that if $X'\to X$
is an etale space and if $r'$ is the inverse image of $r$ in $X'$, then the induced morphism

```text
Top(X'/r') -> Top(X/r)
```

is equivalent to a localization morphism

```text
Top(X/r)/E -> Top(X/r),
```

where $E$ is an object of $Top(X/r)$, determined up to unique isomorphism. In order for $E$ to cover the final object of
$Top(X/r)$, it is necessary and sufficient that the saturation under $R = \operatorname{glob}(r)$ of the image of $X'$
in $X$ be equal to $X$.

**l)** Deduce from k) that $Top(X/r)$ is a rigid spread (9.8.2 h)). Show that, if $X$ is sober, the set of isomorphism
classes of points of $Top(X/r)$ is homeomorphic, for its canonical topology, to the topological quotient space
$X/\operatorname{glob}(r)$, and that, for two points of $Top(X/r)$ coming from points $x$ and $x'$ of $X$, there exists
at most one morphism from one to the other; there is indeed one if and only if $x$ and $x'$ are equivalent modulo
$\operatorname{glob}(r)$ to points $x_1$ and $x'_1$ such that $x_1$ generalizes $x'_1$.

**m)** Study the canonical morphism of topoi

```text
Top(X) -> Top(X/r),
```

[PDF p. 504]

noting that, for every object $U$ of $Top(X/r)$ such that the topos induced on $U$ "is" an ordinary topological space,
the induced morphism

```text
Top(X) times_{Top(X/r)} (Top(X/r)/U) -> Top(X/r)/U
```

"is" a continuous map of ordinary topological spaces $X_U\to U$. Show that the fibers of the map $X_U\to U$ are
homeomorphic to connected components of the space $X^r$ of f).

**n)** Let $X$ be a differentiable manifold endowed with a foliation, i.e. with a subsheaf $F$ locally a direct factor
of the tangent sheaf of $X$, stable under brackets. Define on $X$ a strictly open local equivalence relation associated
with the foliation, and define on the quotient topos $T = Top(X/r)$ a ring making it into a differentiable spread (9.8.2
j)).

Define an equivalence between the category of locally free modules on the differentiable spread $T$ (also called
differentiable vector bundles on $T$) and the category of locally free modules on $X$ endowed with a connection relative
to the given subbundle $F$ of the tangent bundle. Give variants in the real analytic and complex analytic cases.

[PDF p. 505]

## 10. Sheaves of Morphisms

**Proposition 10.1.** Let $E$ be a topos, and let $X$ and $Y$ be two objects of $E$; the functor

```text
Z |-> Hom_E(Z times X, Y) ~= Hom_{E/Z}(X_Z, Y_Z)
```

is representable.

Indeed, inductive limits are universal in $E$ (II 4.3). The functor $Z\mapsto Z\times X$ therefore commutes with
inductive limits. Consequently, the functor $Z\mapsto \operatorname{Hom}_E(Z\times X,Y)$ transforms inductive limits in
the argument $Z$ into projective limits. It is therefore representable (IV 1.4 and 1.2).

**10.2.** The object representing the functor $Z\mapsto \operatorname{Hom}_E(Z\times X,Y)$ is denoted

```text
Hom_E(X, Y)
```

or more simply $\operatorname{Hom}(X,Y)$, and is called the **sheaf of morphisms from $X$ to $Y$**. It is a bifunctor in
$X$ and $Y$. Thus one has a trifunctorial isomorphism

```text
(10.2.1)  Hom_E(Z, Hom_E(X, Y)) ~= Hom_E(Z times X, Y).
```

It then follows from formula (10.2.1) that the bifunctor $(X,Y)\mapsto \operatorname{Hom}(X,Y)$ transforms inductive
limits in the argument $X$ (resp. projective limits in the argument $Y$) into projective limits in $E$.

**Proposition 10.3.** Let $v : E\to E'$ be a morphism of topoi. For a variable object $X$ of $E$ and a variable object
$Y$ of $E'$, one has a bifunctorial isomorphism

```text
(10.3.1)  v_* Hom_E(v^*Y, X) ~= Hom_{E'}(Y, v_*X).
```

**Proof.** For every object $Z$ of $E'$, one has a sequence of isomorphisms, functorial in all arguments:

```text
Hom_{E'}(Z, v_* Hom_E(v^*Y, X))
  ~= Hom_E(v^*Z, Hom_E(v^*Y, X))                  (adjunction)
  ~= Hom_E(v^*Z times v^*Y, X)                    (10.2.1)
  ~= Hom_E(v^*(Z times Y), X)                     (v^* left exact)
  ~= Hom_{E'}(Z times Y, v_*X)                    (adjunction)
  ~= Hom_{E'}(Z, Hom_{E'}(Y, v_*X))               (10.2.1).
```

The two sides of (10.3.1) therefore represent isomorphic functors, q.e.d.

[PDF p. 506]

**Corollary 10.4.** Let $C$ be a $U$-site, let $X$ be a $U$-presheaf on $C$, let $Y$ be a $U$-sheaf on $C$, and let $V$
be a universe containing $U$ such that $C$ is $V$-small. Let $C_V$ be the topos of $V$-presheaves on $C$, and let
$\widetilde{C}$ be the topos of $U$-sheaves on $C$. The presheaf $\operatorname{Hom}(X,Y)$ is a $U$-sheaf.

Let $X\to aX$ be the canonical morphism from $X$ to its associated sheaf. The corresponding morphism

```text
Hom(aX, Y) -> Hom(X, Y)
```

is an isomorphism. In particular one has a canonical isomorphism

```text
Hom(aX, Y) ~= Hom(X, Y).
```

**10.4.1.** First suppose that $C$ is a small site and that $V = U$. One then has a morphism of topoi
$\widetilde{C}\to C_V$ (IV 4.8), whence the assertions in this case by (10.3.1). To pass from there to the general case,
first remark that the "associated sheaf" functor does not depend on the universe (II 3.6), and that the topos of
$V$-sheaves on $C$ is equivalent to the topos of $V$-sheaves on $\widetilde{C}$ (III 4 and IV 1). It therefore suffices
to prove the following lemma.

**Lemma 10.4.2.** Let $E$ be a $U$-topos, let $V$ be a universe containing $U$, let $E_V$ be the topos of $V$-sheaves on
$E$, and let $X$, $Y$ be two objects of $E$. There exists a canonical isomorphism

```text
Hom_E(X, Y) ~= Hom_{E_V}(X, Y).
```

**10.4.3.** The functor $\varepsilon : E\to E_V$ is fully faithful and left exact. Consequently, for every object $Z$ of
$E$, one has an isomorphism

```text
Hom_{E_V}(epsilon Z, epsilon Hom_E(X, Y)) ~= Hom_E(Z times X, Y).
```

But every object of $E_V$ is an inductive limit of objects coming from $E$; hence the assertion by (10.2.1).

**10.5.** Let $v : E\to E'$ be a morphism of topoi. We propose to define four bifunctorial morphisms:

```text
(10.5.a)  v^* Hom_{E'}(X, Y) -> Hom_E(v^*X, v^*Y),        X, Y in Ob E',
(10.5.b)  v_* Hom_E(X, Y) -> Hom_{E'}(v_*X, v_*Y),         X, Y in Ob E,
(10.5.c)  Hom_{E'}(v_!X, Y) -> v_* Hom_E(X, v^*Y),         X in Ob E, Y in Ob E',
(10.5.d)  v_!(X times v^*Y) -> v_!X times Y,               X in Ob E, Y in Ob E',
```

where, to define the morphisms (10.5.c) and (10.5.d), we suppose that the inverse image functor $v^*$ admits a left
adjoint $v_!$.

[PDF p. 507]

**10.5.1. Definition of (10.5.b).** Let $X$ be an object of $E$. One has an adjunction morphism

```text
v^*v_*X -> X.
```

Hence, for every object $Z$ of $E'$, a bifunctorial morphism

```text
v^*Z times v^*v_*X -> v^*Z times X.
```

Thus, for every object $Y$ of $E$, one has a trifunctorial morphism

```text
Hom_E(v^*Z times X, Y) -> Hom_E(v^*(Z times v_*X), Y).
```

We deduce, by adjunction, a trifunctorial morphism

```text
Hom_{E'}(Z, v_* Hom_E(X, Y)) -> Hom_{E'}(Z, Hom_{E'}(v_*X, v_*Y)),
```

whence the morphism (10.5.b).

**10.5.2. Definition of (10.5.d).** For every object $X$ of $E$, one has an adjunction morphism

```text
X -> v^*v_!X.
```

Hence, for every object $Y$ of $E'$, a bifunctorial morphism

```text
X times v^*Y -> v^*v_!X times v^*Y ~= v^*(v_!X times Y).
```

By adjunction, one obtains the morphism (10.5.d).

**10.5.3. Definition of (10.5.c).** Let $X$ be an object of $E$, and let $Z$, $Y$ be two objects of $E'$. The morphism
(10.5.d)

```text
v_!(X times v^*Z) -> v_!X times Z
```

gives a trifunctorial morphism

```text
Hom_{E'}(v_!X times Z, Y) -> Hom_{E'}(v_!(X times v^*Z), Y),
```

then, by adjunction, a trifunctorial morphism

```text
Hom_{E'}(Z, Hom_{E'}(v_!X, Y)) -> Hom_{E'}(Z, v_* Hom_E(X, v^*Y)),
```

whence the morphism (10.5.c).

**10.5.4. Definition of (10.5.a).** The trifunctorial morphism of (10.5.3)

```text
Hom_{E'}(v_!(Z times v^*X), Y) -> Hom_{E'}(v_!Z times X, Y),
```

where $Z$ is an object of $E$ and $X$, $Y$ are objects of $E'$, makes it possible to obtain, by adjunction, a
trifunctorial morphism

```text
Hom_{E'}(Z, v^* Hom_{E'}(X, Y)) -> Hom_E(Z, Hom_E(v^*X, v^*Y)),
```

whence the morphism (10.5.a).

There is a second way to define (10.5.a). Let $X$, $Y$, $Z$ be three objects of $E'$. The functor $v^*$ gives a
trifunctorial morphism

```text
Hom_{E'}(Z times X, Y) -> Hom_E(v^*Z times v^*X, v^*Y).
```

By adjunction, one obtains a trifunctorial morphism

[PDF p. 508]

```text
Hom_{E'}(Z, Hom_{E'}(X, Y)) -> Hom_{E'}(Z, v_* Hom_E(v^*X, v^*Y)).
```

Thus one has a bifunctorial morphism

```text
Hom_{E'}(X, Y) -> v_* Hom_E(v^*X, v^*Y),
```

whence, by adjunction, a morphism (10.5.a). We leave to the reader the verification that it is indeed the morphism
defined above.

**Proposition 10.6.** Let $v : E\to E'$ be a morphism of topoi.

**1)** The morphism (10.5.b) is an isomorphism, for every object $Y$ of $E$, if and only if the adjunction morphism

```text
v^*v_*X -> X
```

is an isomorphism. In particular, the morphism (10.5.b) is an isomorphism for every pair of objects $(X,Y)$ if and only
if the functor $v_* : E\to E'$ is fully faithful, i.e. if $v$ is an embedding of topoi.

**2)** The following conditions are equivalent:

**(i)** For every pair $(X,Y)$ of objects of $E'$, the morphism (10.5.a) is an isomorphism.

**(ii)** The functor $v^*$ admits a left adjoint $v_!$, and, for every object $X$ of $E$ and every object $Y$ of $E'$,
the morphism (10.5.c) is an isomorphism.

**(iii)** The functor $v^*$ admits a left adjoint $v_!$, and, for every object $X$ of $E$ and every object $Y$ of $E'$,
the morphism (10.5.d) is an isomorphism.

**10.6.1.** The first assertion follows immediately from (10.5.1). It also follows immediately from (10.5.2), (10.5.3),
(10.5.4) that $(iii)\Rightarrow (ii)\Rightarrow (i)$ and that the functor $v^*$ admits a left adjoint $v_!$.

It remains to show that (i) implies that $v^*$ admits a left adjoint, i.e. (IV 1.8) that (i) implies that $v^*$ commutes
with small products. Let $e'$ be the final object of $E'$ and let $I$ be a small set. Since $v^*$ is left exact,
$v^*(e')$ is a final object of $E$; and since $v^*$ commutes with inductive limits,
$v^*(\coprod_I e')\simeq \coprod_I v^*(e')$. For every object $Y$ of $E'$, one has

```text
Hom_{E'}(coproduct_I e', Y) ~= Hom_{E'}(e', Y)^I
```

and

[PDF p. 509]

```text
Hom_E(v^*(coproduct_I e'), v^*Y) ~= Hom_E(coproduct_I v^*(e'), v^*Y).
```

The functorial morphism (10.5.a) therefore induces an isomorphism

```text
v^*(product_I Y) ~= product_I v^*Y,
```

which one verifies is the canonical isomorphism. This proves the assertion.

**Corollary 10.7.** Let $E$ be a topos, let $Z$ be an object of $E$,

```text
j_Z : E/Z -> E
```

the localization morphism (IV 5.2), and let $X,Y$ be two objects of $E$.

**1)** There exists a bifunctorial isomorphism

```text
j_Z^* Hom_E(X, Y) ~= Hom_{E/Z}(j_Z^*X, j_Z^*Y).
```

**2)** Let $X'$ be an object of $E/Z$. There exists a bifunctorial isomorphism

```text
Hom_E(j_{Z!}X', Y) ~= j_{Z*} Hom_{E/Z}(X', j_Z^*Y).
```

**3)** Let $Y'$ be an object of $E/Z$. When $Z$ is an open of $E$, there exists a bifunctorial isomorphism

```text
j_{Z*} Hom_{E/Z}(X', Y') ~= Hom_E(j_{Z!}X', j_{Z*}Y').
```

Assertions **1)** and **2)** are proved by remarking that the morphism $\Lambda_{j_Z}$ is an isomorphism. For assertion
**3)**, it suffices to remark that $j_{Z*}$ is fully faithful, because $j_{Z!}$ is fully faithful (I 5.7. a)).

**Corollary 10.8.** Let $E$ be a topos, let $X$, $Y$ and $Z$ be three objects of $E$, and let

```text
j_Z : E/Z -> E
```

be the localization morphism.

**1)** One has a canonical isomorphism:

```text
j_{Z*}j_Z^*Y ~= Hom(Z, Y).
```

**2)** One has a canonical isomorphism

```text
Hom_E(Z, Hom(X, Y)) ~= Hom_{E/Z}(j_Z^*X, j_Z^*Y).
```

Let $e_Z$ be the final object of $E/Z$ (i.e. the object $\operatorname{id}_Z : Z\to Z$). It follows from (10.2.1) that
one has a canonical isomorphism

```text
Hom_{E/Z}(e_Z, j_Z^*Y) ~= j_Z^*Y ;
```

whence, by (10.7.2), an isomorphism

```text
j_{Z*}j_Z^*Y ~= Hom(j_{Z!}e_Z, Y).
```

Since $j_{Z!}e_Z = Z$, we have proved **1)**. Let us prove **2)**. From (10.7), one derives

[PDF p. 510]

a canonical isomorphism

```text
Hom_{E/Z}(e_Z, j_Z^*Hom(X, Y)) ~= Hom_{E/Z}(j_Z^*X, j_Z^*Y) ;
```

whence, by adjunction on the first member,

```text
Hom_E(Z, Hom(X, Y)) ~= Hom_{E/Z}(j_Z^*X, j_Z^*Y).
```

## 11. Ringed Topoi, Localization in Ringed Topoi

**11.1.1.** Let $U$ be a universe. A $U$-ringed topos means a pair $(E,A)$, where $E$ is a $U$-topos and $A$ is an
object endowed with a ring structure. A $U$-ringed site means a pair $(C,A)$, where $C$ is a $U$-site and $A$ is a
$U$-sheaf of rings on $C$. We do not mention the universe when the context is not ambiguous.

To a ringed site $(C,A)$ is associated the ringed topos $(\widetilde{C},A)$. To a ringed topos $(E,A)$ is associated the
ringed site constituted by the site $E$ and the sheaf of rings represented by $A$.

**11.1.2.** Let $(E,A)$ be a ringed topos. We denote by $A\text{-}E$ (resp. $E\text{-}A$) the category of sheaves of
unitary left (resp. right) $A$-modules. The category $A\text{-}E$ (resp. $E\text{-}A$) is an abelian category (II 6.7).
Let $M$ and $N$ be two sheaves of left (resp. right) $A$-modules. The commutative group of morphisms of $A$-modules from
$M$ to $N$ is denoted $\operatorname{Hom}_A(M,N)$.

**11.1.3.** Let $A$, $B$ and $C$ be three rings of a topos $E$, let $M$ be a sheaf of $A$-$B$-bimodules, and let $N$ be
a sheaf of left $A$-$C$-bimodules. Let $e$ be a final object of $E$ and put $\operatorname{Hom}(e,B)=\Gamma(B)$,
$\operatorname{Hom}(e,C)=\Gamma(C)$.

The $A$-$B$-bimodule structure of $M$ gives a homomorphism of rings from $\Gamma(B)^o$ to the ring of endomorphisms of
the $A$-module $M$; similarly, the $A$-$C$-bimodule structure of $N$ gives a homomorphism of rings from $\Gamma(C)$ to
the ring of endomorphisms of the $A$-module $N$. We deduce, by functoriality, a $\Gamma(B)$-$\Gamma(C)$-bimodule
structure on the commutative group $\operatorname{Hom}_A(M,N)$. In particular, when $A$ is a sheaf of commutative rings,
the group $\operatorname{Hom}_A(M,N)$ is canonically endowed with a $\Gamma(A)$-module structure.

[PDF p. 511]

**11.1.4.** Let $E$ be a topos, let $A$ and $B$ be two rings of $E$, let $u : A\to B$ be a morphism of sheaves of rings,
and let $M$ be a $B$-module, on the left to fix ideas. The sheaf $M$ may be regarded as a sheaf of $A$-modules via $u$:
for every object $X$ of $E$, $M(X)$ is endowed with the $A(X)$-module structure deduced from its $B(X)$-module structure
and from the homomorphism $u(X) : A(X)\to B(X)$, by restriction of scalars. One obtains in this way a restriction of
scalars functor by $u$

```text
Res(u) : B-E -> A-E.
```

**11.1.5.** In particular, when $A = \mathbf{Z}$ (the constant sheaf $\mathbf{Z}$, i.e. the sheaf associated with the
constant presheaf $\mathbf{Z}$) and when $u : \mathbf{Z}\to B$ is the unique canonical morphism, one obtains a functor
from $B\text{-}E$ to the category $E_{\mathrm{ab}}$, which is none other than the category of abelian sheaves. This
functor is called the **underlying abelian sheaf** functor.

**Proposition 11.1.6.** The restriction of scalars functor by $u$ commutes with inductive and projective limits. It is
conservative.

The proposition is true for the restriction of scalars functor for ordinary modules, i.e. when $E$ is the punctual
topos. It is therefore true when $E$ is the topos of presheaves on a small site. It then follows from the determination
of inductive and projective limits with the aid of the associated sheaf functor (II 6.4) that the proposition is true in
the general case.

**11.2.1.** Let $(E,A)$ be a ringed topos, let $X$ be an object of $E$, and let

```text
j_X : E/X -> E
```

be the localization morphism (IV 8). By III 1.7 or IV 3.1.2, the sheaf $j_X^*A$ is canonically endowed with a ring
structure. The sheaf of rings $j_X^*A$ is most often denoted $A|X$, or also, abusively, $A$. Unless otherwise mentioned,
the topos $E/X$ will be ringed by $A|X$.

The sheaf $j_{X*}(A|X)$ is canonically endowed with a ring structure. The adjunction morphism

```text
A -> j_{X*}(A|X)
```

is a morphism of sheaves of rings.

[PDF p. 512]

**11.2.2.** Let moreover $M$ be an $A$-module, on the left to fix ideas. The sheaf $j_X^*M$ is an $A|X$-module (III 1.7
or IV 3.1.2), hence a functor

```text
j_X^* : A-E -> (A|X)-(E/X),
```

called the restriction functor to $E/X$, or also the restriction functor to $X$. The functor $j_X^*$ commutes with
inductive and projective limits (loc. cit.); in particular it is exact.

Now let $N$ be an $A|X$-module. The sheaf $j_{X*}N$ is a sheaf of $j_{X*}(A|X)$-modules (III 1.7 or IV 3.1.2). By
restriction of scalars through the adjunction morphism $A\to j_{X*}(A|X)$ (11.2.1), it is therefore an $A$-module, still
denoted $j_{X*}N$. Thus we have defined a functor

```text
j_{X*} : (A|X)-(E/X) -> A-E,
```

which commutes with projective limits (11.1.6 and III 1.7).

For every $A$-module $M$, the adjunction morphism

```text
M -> j_{X*}j_X^*M
```

is a morphism of $A$-modules. For every $A|X$-module $N$ and every $A$-module $M$, the adjunction morphism
$M\to j_{X*}j_X^*M$ defines a bifunctorial morphism in $M$ and $N$

```text
(11.2.2.1)  Hom_{A|X}(j_X^*M, N) -> Hom_A(M, j_{X*}N).
```

This latter morphism is an isomorphism, i.e. the functors $j_X^*$ and $j_{X*}$, for $A$-modules, are adjoint (III 1.7).

**11.2.3.** The functors $j_X^*$ and $j_{X*}$, for modules, commute with the "underlying set" functor (III 1.7 d)). They
therefore commute with restriction of scalars functors and, in particular, with the underlying abelian sheaf functor.

**Proposition 11.3.1.** Let $(E,A)$ be a ringed topos and let $X$ be an object of $E$. The functor

```text
j_X^* : A-E -> (A|X)-(E/X)
```

admits a left adjoint, denoted

```text
j_{X!} : (A|X)-(E/X) -> A-E,
```

and called **extension by zero**. The extension by zero functor is exact and faithful and commutes with inductive
limits. The functors $j_{X!}$, for modules, commute with restriction of scalars functors and, in particular, they
commute with the underlying abelian sheaf functor.

[PDF p. 513]

The existence of the functor $j_{X!}$ follows from III 1.7. Since $j_{X!}$ is a left adjoint, it commutes with inductive
limits (I 2). To prove the other assertions, suppose first that $E$ is the topos of presheaves of sets on a small
category $C$ containing the object $X$. We then know that $E/X$ is equivalent to the category of presheaves on $C/X$ and
that, modulo this equivalence, the functor

```text
j_X^* : E -> E/X
```

is none other than composition with the forgetful functor $C/X\to C$ (I 5.15). It then follows immediately from the
explicit construction of $j_{X!}$ (I 5.1) that, for every $A|X$-module $N$ and every object $Y$ of $C$, one has

```text
j_{X!}N(Y) = direct_sum_{u in Hom_C(Y, X)} N(u),
```

whence the exactness of $j_{X!}$ and the fact that extension by zero commutes with restriction of scalars functors in
this case.

In the general case, one may suppose that $E$ is the topos of sheaves on a small site $C$ and that $X$ comes from an
object of $C$ (IV 1). The topos $E/X$ is then equivalent to the topos of sheaves on $C/X$ endowed with the induced
topology (III 5.4), and the morphism of topoi $j_X : E/X\to E$ comes from the forgetful functor $C/X\to C$, which is
continuous and cocontinuous (III 5.2). It then follows from III 1.7 that extension by zero for sheaves is obtained by
composing extension by zero for presheaves with the associated sheaf functor; whence the assertion of exactness and the
commutation with restrictions of scalars.

To prove faithfulness, it amounts to the same thing to show that, for every $A|X$-module $N$, the adjunction morphism

```text
ad_N : N -> j_X^*j_{X!}N
```

is a monomorphism. Now, denoting by $j'_{X!}$ the extension by zero functor for presheaves and by $a$ the "associated
sheaf" functor, one has a commutative diagram

[PDF p. 514]

```text
                 ad_N
N  -------------------------------->  j_X^* a j'_{X!}N
 \                                      ^
  \ ad'_N                               |
   \                                    |
    -> a j'_X{}^* j'_{X!}N  ------------
```

where $ad'_N$ is the adjunction morphism for presheaves. The morphism $ad'_N$ is a monomorphism by what precedes, hence
$a(ad'_N)$ is a monomorphism. Moreover, since the forgetful functor $C/X\to C$ is continuous and cocontinuous, the
canonical morphism $a j'_X{}^*\to j_X^* a$ is an isomorphism (III 2.5). Consequently $ad_N$ is a monomorphism.

**Remark 11.3.2.** Let $N$ be an $A|X$-module. The underlying sheaf of sets of $j_{X!}N$ is not, in general, isomorphic
to the sheaf obtained by extension by the empty set (III 5.3 and IV 5.2) of the underlying sheaf of sets of $N$. One
should therefore be careful not to confuse the extension by zero functor denoted

```text
j_{X!} : (A|X)-(E/X) -> A-E
```

in 11.3.1, and the extension by the empty set functor again denoted

```text
j_{X!} : E/X -> E
```

in III 5.3 and IV 5.2. In most cases encountered in practice, the abuse of notation just indicated does not cause
confusion. When confusion is nevertheless possible, we shall use the notations $j_{X!}^{\mathrm{mod}}$ and
$j_{X!}^{\mathrm{ens}}$ to denote respectively the functors extension by zero and extension by the empty set.

**Proposition 11.3.3.** Let $(E,A)$ be a ringed topos and let $X$ be an object of $E$. The $A$-module $j_{X!}(A|X)$,
most often denoted $A_X$ or $A_{X,E}$, is the free $A$-module generated by $X$ (II 6.5), i.e. for every $A$-module $M$,
one has a canonical isomorphism, functorial in $M$:

```text
Hom_E(X, M) ~= Hom_A(A_X, M).
```

Let $(X_i)_{i\in I}$ be a topologically generating family of $E$ (II 3.0.1). The family $(A_{X_i})_{i\in I}$ is a
generating family of the category of $A$-modules.

Let $e_X$ be the final object of the topos $E/X$ ($e_X = X\to X$). One has an isomorphism

```text
Hom_{A|X}(A|X, j_X^*M) ~= Hom_{E/X}(e_X, j_X^*M),
```

[PDF p. 515]

deduced from the unit section $e_X\to A|X$; whence, by adjunction, an isomorphism

```text
Hom_A(j_{X!}^{mod}(A|X), M) ~= Hom_E(j_{X!}^{ens}(e_X), M).
```

Since $j_{X!}^{\mathrm{ens}}(e_X) = X$, one obtains the announced isomorphism. The last assertion follows from II 6.6.

**Remark 11.3.4.** Let $A$ and $B$ be two sheaves of rings on a topos $E$, let $X$ be an object of $E$, and let $N$ be
an $A|X$-$B|X$-bimodule. The abelian sheaf obtained by extending $N$ by zero is canonically endowed with an
$A$-$B$-bimodule structure, as follows immediately from its explicit description (11.3.1). In particular, the generated
free $A$-module $A_X$ is an $A$-bimodule.

**Exercise 11.3.5.** Let $E$ be a topos, let $X$ be an object of $E$, let $x : P\to E$ be a point of $E$ (IV 6.1), and
let $(x_i)_{i\in I}$ be the family of points of $E/X$ over $x$ (in bijective correspondence with the fiber $X_x$, IV
6.7.2). Show that, for every abelian sheaf $M$ on $E/X$, the fiber $(j_{X!}M)_x$ is canonically isomorphic to

```text
direct_sum_{i in I} M_{x_i}.
```

## 12. Operations on Modules

**Proposition 12.1.** Let $(E,A)$ be a ringed topos, and let $M$ and $N$ be two left (resp. right) $A$-modules. The
functor on $E$ which, to every object $X$ of $E$, associates the commutative group

```text
Hom_A(M, Hom_E(X, N))
```

is representable by an abelian sheaf denoted $\mathcal{H}om_A(M,N)$ (or sometimes $\mathcal{H}om(M,N)$ when no confusion
can result). For every object $X$ of $E$, one has a canonical isomorphism

```text
(12.1.1)  Hom_A(M, N)(X) ~= Hom_{A|X}(j_X^*M, j_X^*N).
```

One has a canonical isomorphism $\operatorname{Hom}_E(X,N)\simeq j_{X*}j_X^*N$ (10.8), and consequently
$\operatorname{Hom}_E(X,N)$ is functorially endowed in $X$ with a left (resp. right) $A$-module structure. The functor
$X\mapsto \operatorname{Hom}_E(X,N)$ transforms inductive limits in the argument $X$ into projective limits of
$A$-modules (10.2 and 11.2.3) and, consequently, the functor

```text
X |-> Hom_A(M, Hom_E(X, N))
```

transforms inductive limits in the argument $X$ into projective limits of commutative groups, hence into projective
limits of the underlying sets. It is therefore representable (IV 1.4 and 1.2), and the object representing it is endowed
with the structure of an abelian sheaf.

[PDF p. 516]

By definition, for every object $X$ of $E$, one has a canonical isomorphism

```text
(12.1.2)  Hom_A(M, N)(X) = Hom_E(X, Hom_A(M, N)) ~= Hom_A(M, Hom_E(X, N)),
```

and the isomorphism (12.1.1) follows from (12.1.2), from the isomorphism

```text
Hom_E(X, N) ~= j_{X*}j_X^*N
```

(10.8), and from the adjunction formulas of 10.

**12.2.** The abelian sheaf $\mathcal{H}om_A(M,N)$ is called the **sheaf of morphisms of $A$-modules** from $M$ to $N$.
It is a bifunctor in $M$ and $N$. It follows from its definition and from (10.2) that it transforms projective limits in
the argument $N$ (resp. inductive limits in $M$) into projective limits of abelian sheaves. In particular, it is left
exact in its two arguments.

**Proposition 12.3.** Let $(E,A)$ be a ringed topos, let $M$ and $N$ be two right (resp. left) $A$-modules, and let $X$
be an object of $E$.

**a)** One has canonical isomorphisms:

```text
Hom_A(M, N)(X)
  ~= Hom_A(M, j_{X*}j_X^*N)
  ~= Hom_{A|X}(j_X^*M, j_X^*N)
  ~= Hom_A(j_{X!}j_X^*M, N).
```

**b)** One has a canonical isomorphism:

```text
phi_X : j_X^* Hom_A(M, N) ~= Hom_{A|X}(j_X^*M, j_X^*N).
```

Let moreover $P$ be a right (resp. left) $A|X$-module.

**c)** One has a canonical isomorphism:

```text
j_{X*} Hom_{A|X}(j_X^*M, P) ~= Hom_A(M, j_{X*}P).
```

**d)** One has a canonical isomorphism:

```text
j_{X*} Hom_{A|X}(P, j_X^*N) ~= Hom_A(j_{X!}P, N).
```

The isomorphisms of **a)** follow from (12.1.2), from the isomorphism $\operatorname{Hom}_E(X,N)\simeq j_{X*}j_X^*N$
(10.8), and from the adjunction formulas of 10.

Let us prove **b)**. For every object $Y$ of $E/X$, one has the sequence of isomorphisms:

```text
Hom(Y, j_X^*Hom_A(M, N))
  ~= Hom(j_{X!}Y, Hom_A(M, N))
  ~= Hom_A(M, Hom_E(j_{X!}Y, N))
  ~= Hom_A(M, j_{X*}Hom_{E/X}(Y, j_X^*N))
  ~= Hom_{A|X}(j_X^*M, Hom_{E/X}(Y, j_X^*N))
  ~= Hom(Y, Hom_{A|X}(j_X^*M, j_X^*N)).
```

[PDF p. 517]

Let us prove **c)**. For every object $Y$ of $E$, one has the sequence of isomorphisms:

```text
Hom(Y, j_{X*}Hom_{A|X}(j_X^*M, P))
  ~= Hom(j_X^*Y, Hom_{A|X}(j_X^*M, P))
  ~= Hom_{A|X}(j_X^*M, Hom_{E/X}(j_X^*Y, P))
  ~= Hom_A(M, j_{X*}Hom_{E/X}(j_X^*Y, P))
  ~= Hom_A(M, Hom_E(Y, j_{X*}P))
  ~= Hom(Y, Hom_A(M, j_{X*}P)).
```

Let us prove **d)**. For every object $Y$ of $E$, one has the sequence of isomorphisms:

```text
Hom(Y, Hom_A(j_{X!}P, N))
  ~= Hom_A(j_{X!}P, Hom_E(Y, N))
  ~= Hom_{A|X}(P, j_X^*Hom_E(Y, N))
  ~= Hom_{A|X}(P, Hom_{E/X}(j_X^*Y, j_X^*N))
  ~= Hom(j_X^*Y, Hom_{A|X}(P, j_X^*N))
  ~= Hom(Y, j_{X*}Hom_{A|X}(P, j_X^*N)).
```

**Corollary 12.4.** Let $C$ be a $U$-site, let $A'$ be a $U$-presheaf of rings on $C$, let $M$ be a $U$-presheaf of
$A'$-modules, on the left to fix ideas, and let $N$ be a $U$-sheaf of left $A'$-modules. Denote by $A$ the sheaf
associated with $A'$, so that the sheaves $N$ and $aM$ (the sheaf associated with $M$) are $A$-modules. The presheaf

```text
X |-> Hom_{A'|X}(j_X^*M, j_X^*N)
```

is a $U$-abelian sheaf canonically isomorphic to $\mathcal{H}om_A(aM,N)$. Indeed, it follows from III 5.5 and III 2.3
that the localization functor to $C/X$ commutes with associated sheaf functors (for $C$ and $C/X$). Consequently, one
has functorial isomorphisms in the variable object $X$ of $C$:

```text
Hom_{A'|X}(j_X^*M, j_X^*N)
  ~= Hom_{A|X}(a j_X^*M, j_X^*N)
  ~= Hom_{A|X}(j_X^*aM, j_X^*N)
  ~= Hom_A(aM, N)(X).
```

[PDF p. 518]

**Corollary 12.5.** Let $E$ be a topos, let $A$, $B$, $C$ be three sheaves of rings on $E$, let $M$ be an
$A$-$B$-bimodule, and let $N$ be an $A$-$C$-bimodule. The abelian sheaf $\mathcal{H}om_A(M,N)$ is canonically endowed
with a $B$-$C$-bimodule structure. In particular, when $A$ is a sheaf of commutative rings and when $M$ and $N$ are
$A$-modules, $\mathcal{H}om_A(M,N)$ is canonically endowed with an $A$-module structure. The canonical isomorphisms
**b)**, **c)**, **d)** of 12.3 are isomorphisms of bimodules.

We shall confine ourselves to giving indications. For every object $X$ of $E$, one has

```text
Hom_A(M, N)(X) ~= Hom_{A|X}(j_X^*M, j_X^*N)
```

(12.3). Consequently, the commutative group $\operatorname{Hom}_A(M,N)(X)$ is canonically endowed with a
$B(X)$-$C(X)$-bimodule structure (11.1.3), which one verifies is functorial in $X$. The other assertions are left to the
reader.

**Corollary 12.6.** Let $(E,A)$ be a ringed topos, let $X$ be an object of $E$, and let $N$ be an $A$-module, on the
left to fix ideas. One has canonical isomorphisms of $A$-modules:

```text
Hom_E(X, N) ~= j_{X*}j_X^*N ~= Hom_A(A_X, N),
```

the $A$-module structure on $\operatorname{Hom}_A(A_X,N)$ coming from the bimodule structure on $A_X$ (11.3.4).

The first isomorphism follows from 10.7, the second from the isomorphism of $A$-modules
$N\simeq \operatorname{Hom}_A(A,N)$ and from 12.3.

**Proposition 12.7.** Let $(E,A)$ be a ringed topos, let $M$ be a right $A$-module, and let $N$ be a left $A$-module.
The functor which, to every abelian sheaf $P$, associates the commutative group

```text
Hom_A(M, Hom(N, P))
```

is representable by an abelian sheaf denoted $M\otimes_A N$ and called the **tensor product over $A$** of $M$ and $N$.

One has a canonical injection of $\operatorname{Hom}_A(M,\operatorname{Hom}(N,P))$ into the set

```text
Hom(M, Hom(N, P)) ~= Hom(M times N, P).
```

Returning to the definitions, a morphism $f : M\times N\to P$ of sheaves of sets comes from an element of
$\operatorname{Hom}_A(M,\operatorname{Hom}(N,P))$ if and only if, for every object $X$ of $E$,

```text
f(X) : M(X) times N(X) -> P(X)
```

[PDF p. 519]

is an $A(X)$-bilinear map. Call a morphism of sheaves of sets $M\times N\to P$ having this property an **$A$-bilinear
morphism**. Thus it is a matter of representing the functor of $A$-bilinear morphisms from $M\times N$ to $P$.

For this we proceed as in the ordinary case, i.e. as in the case where $E$ is the punctual topos. Consider the eight
morphisms

```text
(i) : M times M times N -> M times N,    1 <= i <= 3,
(i) : M times N times N -> M times N,    4 <= i <= 6,
(i) : M times A times N -> M times N,    7 <= i <= 8,
```

defined by the formulas:

```text
(1) (m_1, m_2, n) |-> (m_1 + m_2, n)
(2) (m_1, m_2, n) |-> (m_1, n)
(3) (m_1, m_2, n) |-> (m_2, n)
(4) (m, n_1, n_2) |-> (m, n_1 + n_2)
(5) (m, n_1, n_2) |-> (m, n_1)
(6) (m, n_1, n_2) |-> (m, n_2)
(7) (m, a, n) |-> (ma, n)
(8) (m, a, n) |-> (m, an),
```

where formula $(i)$ describes the map $(i)(X)$ for variable objects $X$ of $E$. If $L$ denotes the functor "free abelian
sheaf generated by", the greatest quotient of $L(M\times N)$ which equalizes $L(1)$ with $L(2)+L(3)$, $L(4)$ with
$L(5)+L(6)$, and $L(7)$ with $L(8)$ represents the functor of $A$-bilinear morphisms from $M\times N$ to $P$.

**12.8.** One observes that the functor

```text
P |-> Hom_A(N, Hom(M, P))
```

is also canonically isomorphic to the functor of $A$-bilinear maps from $M\times N$ to $P$. Consequently, the tensor
product $M\otimes_A N$ also represents this functor. Thus one has isomorphisms, functorial in all arguments,

```text
(12.8.1)  Hom(M tensor_A N, P) ~= Hom_A(M, Hom(N, P)),
(12.8.2)  Hom(M tensor_A N, P) ~= Hom_A(N, Hom(M, P)).
```

[PDF p. 520]

**12.9.** It follows from (12.8.1), or from (12.8.2) and 12.2, that the functor $\otimes_A$ commutes with inductive
limits in its two arguments.

**Proposition 12.10.** Let $C$ be a $U$-site, let $A'$ be a presheaf of rings on $C$, let $M'$ (resp. $N'$) be a right
(resp. left) $A'$-module, and let $A$, $M$, $N$ be the sheaves associated respectively with $A'$, $M'$, $N'$. The sheaf
associated with the presheaf

```text
X |-> M'(X) tensor_{A'(X)} N'(X)      (X in ob C)
```

is canonically isomorphic to the sheaf $M\otimes_A N$.

The presheaf $X\mapsto M'(X)\otimes_{A'(X)}N'(X)$ is constructed from the presheaves $M'$, $N'$ and $A'$ by the
operations indicated in the proof of 12.7. Since the "associated sheaf" functor commutes with finite projective and
inductive limits and with the functor "free abelian object generated by", formation of the tensor product commutes with
the "associated sheaf" functor.

**Proposition 12.11.** Let $(E,A)$ be a ringed topos, let $M$ be a right $A$-module, let $N$ be a left $A$-module, and
let $X$ be an object of $E$.

**a)** One has a canonical isomorphism

```text
j_X^*(M tensor_A N) ~= j_X^*M tensor_{A|X} j_X^*N.
```

Let moreover $P$ be a right $A|X$-module and $Q$ a left $A|X$-module.

**b)** One has canonical isomorphisms, the **projection formulas**:

```text
j_{X!}(P tensor_{A|X} j_X^*N) ~= j_{X!}P tensor_A N,
j_{X!}(j_X^*M tensor_{A|X} Q) ~= M tensor_A j_{X!}Q.
```

Let us prove **a)**. For every abelian sheaf $R$ on $E/X$, one has the sequence of isomorphisms functorial in $R$:

```text
Hom(j_X^*(M tensor_A N), R)
  ~= Hom(M tensor_A N, j_{X*}R)
  ~= Hom_A(M, Hom(N, j_{X*}R))
  ~= Hom_A(M, j_{X*}Hom(j_X^*N, R))
  ~= Hom_{A|X}(j_X^*M, Hom(j_X^*N, R))
  ~= Hom(j_X^*M tensor_{A|X} j_X^*N, R).
```

[PDF p. 521]

Let us exhibit the first isomorphism of **b)**. For every abelian sheaf $R$, one has a sequence of isomorphisms
functorial in $R$:

```text
Hom(j_{X!}(P tensor_{A|X} j_X^*N), R)
  ~= Hom(P tensor_{A|X} j_X^*N, j_X^*R)
  ~= Hom_{A|X}(P, Hom(j_X^*N, j_X^*R))
  ~= Hom_{A|X}(P, j_X^*Hom(N, R))
  ~= Hom(j_{X!}P, Hom(N, R))
  ~= Hom(j_{X!}P tensor_A N, R).
```

The second isomorphism is obtained analogously with the aid of (12.8.2).

**Corollary 12.12.** Let $E$ be a topos, let $A$, $B$, $C$ be three sheaves of rings on $E$, let $M$ be a
$B$-$A$-bimodule, and let $N$ be an $A$-$C$-bimodule. The abelian sheaf $M\otimes_A N$ is canonically endowed with a
$B$-$C$-bimodule structure. In particular, when $A$ is a sheaf of commutative rings and when $M$ and $N$ are
$A$-modules, $M\otimes_A N$ is canonically endowed with an $A$-module structure. The isomorphisms of 12.11 are
isomorphisms of bimodules.

For every object $X$ of $E$, $j_X^*M$ is a right $A|X$-module on which the ring $B(X)$ acts on the left. Similarly,
$j_X^*N$ is a left $A|X$-module on which $C(X)$ acts on the right. By functoriality, the abelian sheaf

```text
j_X^*M tensor_{A|X} j_X^*N = j_X^*(M tensor_A N)
```

is endowed with a $B(X)$-$C(X)$-object structure, a structure which varies functorially in $X$. Consequently
$M\otimes_A N$ is endowed with a $B$-$C$-bimodule structure. This structure is reflected in the evident way on the
"$A$-bilinear morphism" functor. One then observes that, when $A$ is commutative and when $M$ and $N$ are $A$-modules,
the right and left $A$-module structures obtained are equal; consequently $M\otimes_A N$ is in this case an $A$-module.
The last assertion is left to the reader.

[PDF p. 522]

**Corollary 12.13.** Let $(E,A)$ be a ringed topos, let $M$ be a left (resp. right) $A$-module, and let $X$ be an object
of $E$. With the notation $A_X$ of 11.3.3, one has a canonical isomorphism

```text
A_X tensor_A M ~= j_{X!}j_X^*M
```

resp.

```text
M tensor_A A_X ~= j_{X!}j_X^*M.
```

This follows from the projection formulas (12.11).

**Proposition 12.14.** Let $E$ be a topos, let $A$ and $B$ be two sheaves of rings on $E$, let $M$ be a right
$A$-module, let $N$ be an $A$-$B$-bimodule, and let $P$ be a right $B$-module. One has a canonical isomorphism

```text
Hom_B(M tensor_A N, P) ~= Hom_A(M, Hom_B(N, P)).
```

From (12.8.1) one obtains a canonical $A$-bilinear morphism

```text
Hom_B(N, P) times N -> P.
```

Restricting to $\operatorname{Hom}_B(N,P)\times N$, which is a subsheaf of the corresponding sheaf of maps, one obtains
an $A$-bilinear morphism $\operatorname{Hom}_B(N,P)\times N\to P$, which one immediately verifies is $B$-linear on the
second factor. Thus one has a canonical morphism of $B$-modules

```text
Hom_B(N, P) tensor_A N -> P,
```

whence a canonical map, functorial in $M$,

```text
(12.14.1)  Hom_A(M, Hom_B(N, P)) -> Hom_B(M tensor_A N, P).
```

Let us show that this morphism of functors is an isomorphism. Since the two members transform inductive limits of $M$
into projective limits, it suffices to show that (12.14.1) is an isomorphism when $M$ runs through a generating family
of the category of $A$-modules. It therefore suffices to show it when $M = A_X$, where $X$ is an object of $E$. The
verification is then immediate.

## 13. Morphisms of Ringed Topoi

**Definition 13.1.** Let $(E,A)$ and $(E',A')$ be two ringed topoi. A **morphism of ringed topoi**

```text
u : (E, A) -> (E', A')
```

is a pair $(m,\theta)$, where $m : E\to E'$ is a morphism of topoi (IV 3.1) and

```text
theta : m^*A' -> A
```

is a morphism of rings.

**13.1.1.** Since the functor $m^* : E'\to E$ is left adjoint to the functor $m_* : E\to E'$, to give a morphism of
ringed topoi $(m,\theta) : (E,A)\to (E',A')$ amounts to giving a morphism of topoi $m : E\to E'$ and a morphism of
sheaves of rings

```text
theta' : A' -> m_*A.
```

[PDF p. 523]

**13.2.** To a morphism of ringed topoi $u = (m,\theta) : (E,A)\to (E',A')$, one associates two remarkable functors
between the categories of modules.

**13.2.1. The direct image functor for modules.** Let $M$ be a left (resp. right) $A$-module. The object $m_*M$ is
canonically endowed with an $m_*A$-module structure. By restriction of scalars through the canonical morphism
$\theta' : A'\to m_*A$, one obtains an $A'$-module, denoted $u_*M$ and called the **direct image** of $M$ by the
morphism $u$.

**13.2.2. The inverse image functor for modules.** Let $N$ be a left (resp. right) $A'$-module. The object $m^*N$ of $E$
is canonically endowed with a left (resp. right) $m^*A'$-module structure. The $A$-module

```text
A tensor_{m^*A'} m^*N
```

resp.

```text
m^*N tensor_{m^*A'} A
```

where $A$ is endowed with the $m^*A'$-module structure defined by $\theta : m^*A'\to A$, is denoted $u^*N$ and called
the **inverse image** of the module $N$ by the morphism of ringed topoi $u$.

**13.2.3.** For every $A$-module $M$, the sheaf of sets and the abelian sheaf underlying $u_*M$ are the sheaf $m_*M$.
Thus one most often uses the notation $u_*$ to denote the functor $m_*$, direct image for sheaves of sets.

On the other hand, for an $A'$-module $N$, the sheaf of sets or the abelian sheaf underlying $u^*N$ is in general
neither equal nor isomorphic to $m^*N$, except however when $\theta$ is an isomorphism. Thus one must distinguish the
inverse image for modules and the inverse image for sheaves of sets or abelian sheaves. One most often uses the notation

```text
m^* : E' -> E
```

to denote the inverse image functor for sheaves of sets. This functor is called the "set-theoretic" inverse image
functor by the morphism of ringed topoi $u$, by opposition with the inverse image "in the sense of modules" $u^*$.

**Definition 13.3.** Let $(C,A)$ and $(C',A')$ be two $U$-ringed sites. A morphism of ringed sites

```text
u : (C, A) -> (C', A')
```

is a pair $(m,\theta)$, where $m$ is a morphism from the site $C$ to the site $C'$ (IV 4.9) and

[PDF p. 524]

```text
theta : m^*A' -> A
```

is a morphism of rings.

**13.3.1.** A morphism of ringed topoi is a morphism of $U$-ringed sites. A morphism of ringed sites gives rise to a
morphism between the corresponding ringed topoi (11.1.1 and IV 4.9.1).

**Proposition 13.4.** Let $u : (E,A)\to (E',A')$ be a morphism of ringed topoi.

**a)** For a variable left (resp. right) $A$-module $M$, and for a variable left (resp. right) $A'$-module $N$, one has
canonical bifunctorial isomorphisms, called **adjunction isomorphisms**:

```text
(13.4.1)  Hom_A(u^*N, M) ~= Hom_{A'}(N, u_*M),
(13.4.2)  u_* Hom_A(u^*N, M) ~= Hom_{A'}(N, u_*M).
```

**b)** For a variable object $X$ of $E'$, one has a canonical isomorphism, functorial in $X$:

```text
(13.4.3)  u^*A'_X ~= A_{u^{-1}(X)},
```

where $A'_X$ and $A_{u^{-1}(X)}$ denote the generated free modules (11.3.3).

**c)** When $A'$ is commutative and when the canonical morphism $u^{-1}A'\to A$ is central (resp. when the canonical
morphism $u^{-1}A'\to A$ is an isomorphism), one has, for a variable right $A'$-module $M$ and a variable left
$A'$-module $N$, a canonical bifunctorial isomorphism:

```text
(13.4.4)  u^*M tensor_A u^*N ~= u^*(M tensor_{A'} N)
```

resp.

```text
(13.4.5)  u^*M tensor_A u^*N ~= u^{-1}(M tensor_{A'} N).
```

First one has a canonical isomorphism

```text
Hom_A(u^*N, M) ~= Hom_{u^{-1}A'}(u^{-1}N, M)
```

(12.12), then an isomorphism

```text
Hom_{u^{-1}A'}(u^{-1}N, M) ~= Hom_{A'}(N, u_*M)
```

(III 1.7), whence (13.4.1). Let us exhibit the isomorphism (13.4.2). For every object $X$ of $E'$, one has the sequence
of functorial isomorphisms:

```text
Hom_{E'}(X, u_*Hom_A(u^*N, M))
  ~= Hom_E(u^{-1}X, Hom_A(u^*N, M))
  ~= Hom_A(u^*N, Hom_E(u^{-1}X, M))
  ~= Hom_{A'}(N, u_*Hom_E(u^{-1}X, M))
  ~= Hom_{A'}(N, Hom_{E'}(X, u_*M))
  ~= Hom_{E'}(X, Hom_{A'}(N, u_*M)).
```

[PDF p. 525]

Formula (13.4.5) is then obtained from formula (13.4.2) by adjunction, i.e. by the definition of the tensor product
(12.7). Formula (13.4.4) is deduced from (13.4.5) by using the commutativity of the tensor product when the base ring is
commutative (12.8).

Finally, to prove (13.4.3), consider the sequence of isomorphisms

```text
Hom_A(u^*A'_X, M)
  ~= Hom_{A'}(A'_X, u_*M)
  ~= Hom_{E'}(X, u_*M)
  ~= Hom_E(u^{-1}X, M)
  ~= Hom_A(A_{u^{-1}X}, M).
```

**Corollary 13.5.** Let $(E,A)$ be a ringed topos, let $x : P\to E$ be a point of $E$, and let $F\mapsto F_x$ be the
associated fiber functor (IV 6.1). The fiber functor at $x$ transforms the tensor product of $A$-modules into the
ordinary tensor product of $A_x$-modules.

The tensor product in $P$ is the ordinary tensor product of modules ($P$, the punctual topos, is the category of sets).
The assertion therefore follows from (13.4.4).

**Corollary 13.6.** Let $u : (E,A)\to (E',A')$ be a morphism of ringed topoi. The functor $u_*$, direct image for right
or left modules, commutes with projective limits and, in particular, is left exact. The functor $u^*$, inverse image for
right or left modules, commutes with inductive limits and, in particular, is right exact.

This follows from formula (13.4.1) (I 2.11).

**13.7.** Note that the functor $u^*$, inverse image for modules, is not exact in general, whereas the functor $u^{-1}$,
set-theoretic inverse image, is exact. One can nevertheless assert the exactness of $u^*$ when the canonical morphism

```text
u^{-1}A' -> A
```

is flat, on the right or on the left (V 1.8). This is in particular the case when this canonical morphism is an
isomorphism.

[PDF p. 526]

**13.8.** Let $C$ be a $U$-site, let $A'$ be a presheaf of rings on $C$, and denote by $A$ the associated sheaf. The
category of presheaves of $A'$-modules which are sheaves is equivalent to the category of $A$-modules. One sometimes
uses the notation $\operatorname{Hom}_{A'}(M,N)$ to denote the group $\operatorname{Hom}_A(M,N)$ (11.1.2). Similarly,
and abusively, one uses the notations $\operatorname{Hom}_{A'}(M,N)$ and $M\otimes_{A'}N$ to denote the sheaves
$\mathcal{H}om_A(M,N)$ and $M\otimes_A N$. When $A' = k_E$ is the constant presheaf, defined by an ordinary ring $k$,
one also writes $\operatorname{Hom}_k$, $\otimes_k$ instead of $\operatorname{Hom}_{k_E}$, $\otimes_{k_E}$.

**Exercise 13.9. Locally ringed topoi.** Cf. [9] for more information in the direction that follows.

Let $(E,O_E)$ be a commutatively ringed topos. For $X\in \operatorname{ob} E$ and $f\in O_E(X)$, let $X_f$ be the
largest subobject of $X$ on which $f$ is invertible.

**a)** Show that, for $X'\in \operatorname{ob}(E/X)$, the restriction $f|_{X'}$ is invertible if and only if the
structural morphism $X'\to X$ factors through $X_f$, and that, for $f,g\in O_E(X)$, one has

```text
X_{fg} = X_f cap X_g.
```

**b)** Show that the following conditions are equivalent:

**(i)** For $X\in \operatorname{ob} E$ and $f,g\in O_E(X)$, one has

```text
X_{f+g} <= Sup(X_f, X_g).
```

**(ii)** For $X\in \operatorname{ob} E$ and $f,g\in O_E(X)$ such that $f+g$ is invertible, one has

```text
X = Sup(X_f, X_g).
```

**(iii)** For $X\in \operatorname{ob} E$ and $f\in O_E(X)$, one has

```text
X = Sup(X_f, X_{1-f}).
```

Show that these conditions imply the following condition, and that they are equivalent to it if $E$ has enough points:

[PDF p. 527]

**(iv)** For every point $p$ of $E$, the fiber ring $O_{E,p}$ is a local ring.

When the equivalent conditions **(i)** to **(iii)** are satisfied, one says that $(E,O_E)$ is a **locally ringed
topos**. Similarly, a ringed site is called a **locally ringed site** if the corresponding ringed topos is a locally
ringed topos.

**c)** Let $(E,O_E)$ and $(E',O_{E'})$ be two locally ringed topoi, and let $f$ be a morphism of ringed topoi from the
first to the second. Show that the following condition **(i)** implies condition **(ii)**, and is equivalent to it if
$E$ has enough points:

**(i)** For every $X\in \operatorname{ob} E'$ and $s\in O_{E'}(X)$, putting $Y = f^{-1}X$, one has

```text
Y_{f^*s} = f^{-1}(X_s).
```

**(ii)** For every point $p$ of $E$, putting $p' = f(p)$, the natural homomorphism on the fibers

```text
O_{E',p'} -> O_{E,p}
```

is a local homomorphism of local rings.

When condition **(i)** is satisfied, one says that $f$ is a **morphism of locally ringed topoi**, or also an
**admissible** morphism of locally ringed topoi if confusion is to be feared. We denote by $\operatorname{Homtoplocan}
(E,E')$ the full subcategory of the category $\operatorname{Homtopan}(E,E')$ of all morphisms of ringed topoi from $E$
to $E'$, defined by the admissible morphisms from $E$ to $E'$.

**d)** Suppose that $(E,O_E)$ is the ringed topos associated with a ringed topological space $(X,O_X)$ (IV 2.1). Show
that $(E,O_E)$ is locally ringed if and only if $(X,O_X)$ is locally ringed, i.e. if and only if for every $x\in X$, the
fiber $O_{X,x}$ is a local ring. Note that, in criterion **(iv)** of **b)**, it suffices to take the points in a
conservative family of points of $E$.

[PDF p. 528]

Let $f : (X,O_X)\to (X',O_{X'})$ be a morphism of ringed spaces, where $O_X$ and $O_{X'}$ are sheaves of local rings.
Show that the corresponding morphism of ringed topoi

```text
Top(X, O_X) -> Top(X', O_{X'})
```

is admissible if and only if the same is true for the morphism $f$, i.e. if and only if, for every $x\in X$, the natural
homomorphism

```text
O_{X',f(x)} -> O_{X,x}
```

is a local homomorphism of local rings.

**e)** Let $(E,O_E)$ and $(E',O_{E'})$ be two locally ringed topoi, such that $E$ has enough points and $(E',O_{E'})$ is
equivalent to the ringed topos defined by a scheme $(X',O_{X'})$. Prove that the category
$\operatorname{Homtoplocan}(E,E')$ is equivalent to a discrete category, i.e. that it is a rigid groupoid: every
morphism is an isomorphism and the automorphism groups of the objects are the unit groups.

Indication: reduce to the case where $(E,O_E)$ is the punctual topos ringed by a field. Recall that, by contrast,
$\operatorname{Homtop}(E,E')$ is not in general equivalent to a discrete category, even if $E$ and $E'$ are topoi
defined by schemes, and even if $E$ is the punctual topos; cf. 4.2.3.

**f)** Let $E$ be a locally ringed topos and let $P$ be the ringed topos defined by the ringed space $\operatorname{Spec}
(k)$, where $k$ is a field. Show that the admissible morphisms of locally ringed topoi $P\to E$ correspond to pairs
$(p,u)$, where $p$ is a point of $E$ and $u : k(p)\to k$ is an injection of fields, $k(p)$ being the residue field of the
local ring $O_{E,p}$. Generalize to a statement exhibiting the admissible morphisms from a punctual locally ringed topos
to $E$, generalizing EGA I 2.4.4.

A **geometric point** of a locally ringed topos $E$ means any admissible morphism into $E$ from the locally ringed topos
defined by a ringed space of the form $\operatorname{Spec}(k)$, where $k$ is an algebraically closed field. Define the
category of geometric points of $E$, understood to correspond to fields $k\in U$, denoted $\operatorname{Ptgeom}(E)$,
and a canonical functor

```text
Ptgeom(E) -> Point(E).
```

Show that this functor is faithful if and only if $E$ has no point, i.e. if $\operatorname{Point}(E)$ is the empty
category.

[PDF p. 529]

**g)** Let $E$ be a $U$-topos and let $V$ be a universe such that $U\in V$. Define a 2-category
$(V\text{-}U\text{-}\mathrm{Top})/E$ in terms of the object $E$ of the 2-category $(V\text{-}U\text{-}\mathrm{Top})$
(3.3.1), taking inspiration from 5.14 a). When $E$ is ringed by a ring $A$, similarly define a 2-category
$(V\text{-}U\text{-}\mathrm{Topan})/E$; and when $E$ is locally ringed, using the notion of admissible morphism (cf.
**c)**), define a 2-category $(V\text{-}U\text{-}\mathrm{Topanloc})/E$, admitting $\operatorname{Ptgeom}(E)$ (cf.
**f)**) as a full subcategory.

## 14. Modules on a Topos Defined by Gluing

**14.1.** Let $(E,A)$ be a ringed topos, let $U$ be an open subtopos of $E$, let $F$ be the complementary closed
subtopos, and let

```text
j : U -> E,    i : F -> E
```

be the canonical morphisms (9.3). The topos $U$ is ringed by $j^*A$ (11.2.2). In this section, the topos $F$ will be
ringed by the sheaf $i^*A$, denoted $A|F$. The morphisms $j$ and $i$, completed in the evident way, are then morphisms
of ringed topoi.

**14.2.** Thus one has two morphisms of ringed topoi

```text
j : (U, A|U) -> (E, A),    i : (F, A|F) -> (E, A),
```

and five functors between the corresponding categories of modules, on the left to fix ideas:

```text
        j_!
A|U-Mod ---> A-Mod
         <---
        j^*
         --->
        j_*

        i^*
A-Mod   ---> A|F-Mod
         <---
        i_*
```

Each functor of the diagram (14.2.1) is left adjoint to the one lying below it.

[PDF p. 530]

**14.3.** We know that the functor

```text
X |-> (j^*X, i^*X, i^*X -> i^*j_*j^*X)
```

is an equivalence of $E$ with the topos $(U,F,i^*j_*)$ (9.5.4). This equivalence induces an equivalence between the
corresponding categories of modules. Consequently the functor

```text
P |-> (j^*P, i^*P, i^*P -> i^*j_*j^*P)
```

is an equivalence, denoted $\Phi$, from the category of $A$-modules to the category of triples

```text
(M, N, u : N -> i^*j_*M).
```

The functors of (14.2.1), composed with $\Phi$ or $\Phi^{-1}$, are then the functors:

```text
Phi o j_* :
M |-> (M, i^*j_*M ; i^*j_*M --id--> i^*j_*M),

j^* o Phi^{-1} :
(M, N ; N --u--> i^*j_*M) |-> M,

Phi o j_! :
M |-> (M, 0 ; 0 -> i^*j_*M),

Phi o i_* :
N |-> (0, N ; N -> 0),

i^* o Phi^{-1} :
(M, N ; N --u--> i^*j_*M) |-> N.
```

The reader may, as an exercise, make explicit the various adjunction morphisms.

**14.4.** Denote by

```text
i^! : A-E -> (A|F)-F
```

the functor defined, under the equivalence of 14.3, by the formula

```text
i^!(M, N, u : N -> i^*j_*M) = Ker(u).
```

**Proposition 14.5.** The functor $i^!$ is right adjoint to the functor $i_*$. The adjunction morphism $i_*i^!\to
\operatorname{id}$ is a monomorphism. The functors $i^!$, for variable rings, commute with restriction of scalars
functors.

It is clear that every morphism

```text
(0, N ; 0) -> (M, N ; N --u--> i^*j_*M)
```

factors uniquely through $(0,\operatorname{Ker}(u);0)$, which proves the adjunction property. The other assertions are
trivial.

[PDF p. 531]

**Proposition 14.6.** For every $A$-module $P$, one has exact sequences functorial in $P$:

```text
(14.6.1)  0 -> j_!j^*P -> P -> i_*i^*P -> 0,
(14.6.2)  0 -> i_*i^!P -> P -> j_*j^*P,
```

where the nontrivial arrows are the adjunction arrows.

First remark that a sequence

```text
(M', N', u') -> (M, N, u) -> (M'', N'', u'')
```

in the category of triples is exact if and only if the corresponding sequences

```text
M' -> M -> M'',    N' -> N -> N''
```

are exact. The sequences (14.6.1) and (14.6.2) are transformed by the equivalence $\Phi$ into sequences of the type

```text
0 -> (M, 0, 0) -> (M, N, u) -> (0, N, 0) -> 0,
0 -> (0, Ker(u), 0) -> (M, N, u) -> (M, i^*j_*M, id).
```

Verification of the exactness of these sequences is trivial.

**14.7.** The exact sequence (14.6.2) makes it possible to obtain a new interpretation of the functor $i_*i^!$. Let $X$
be an object of $E$. From (14.6.2) one obtains the exact sequence of commutative groups

```text
0 -> Hom_E(X, i_*i^!P) -> Hom_E(X, P) -> Hom_E(X, j_*j^*P).
```

Again denote by $U$ the open of $E$, the final object of the open subtopos $U$. It follows from the adjunction
properties of the functors $j_!$, $j^*$ and $j_*$ that the group $\operatorname{Hom}_E(X,j_*j^*P)$ is canonically
isomorphic to $\operatorname{Hom}_E(X\times U,P)$, and that the morphism
$\operatorname{Hom}_E(X,P)\to \operatorname{Hom}_E(X,j_*j^*P)$ is none other than the morphism defined by the
monomorphism $X\times U\to X$ (IV 5). In other words (8.5.2):

[PDF p. 532]

**Proposition 14.8.** The sections of $i_*i^!P$ on $E/X$ are the sections of $P$ on $E/X$ whose support (9.3.5) is
contained in $F$ (notation of 5.9.1). In other words, $i_*i^!P$ is the largest subsheaf of $P$ with support contained in
$F$.

**14.9.** By abuse of language, one sometimes says that $i_*i^!P$ is the submodule of $P$ defined by the sections of $P$
with support in $F$. It follows from 8.5.3 that this terminology merely extends to general topoi a terminology used for
topoi of sheaves on topological spaces.

**Proposition 14.10.**

1. The functor $P\mapsto i_*i^*P$ is isomorphic to the functor

   ```text
   P |-> i_*i^*A tensor_A P.
   ```

2. The functor $P\mapsto i_*i^!P$ is isomorphic to the functor

   ```text
   P |-> Hom_A(i_*i^*A, P).
   ```

The exact sequence (14.6.1) is written, in the particular case where $P$ is the $A$-module $A$, as

```text
(14.10.1)  0 -> A_U -> A -> i_*i^*A -> 0,
```

where $A_U$ is the free $A$-module generated by the open $U$ corresponding to the open subtopos $U$ (9 and 11.3.3). For
every $A$-module $P$, the $A$-modules $j_!j^*P$ and $j_*j^*P$ are canonically isomorphic respectively to
$A_U\otimes_A P$ and to $\operatorname{Hom}_A(A_U,P)$ (12.3 and 12.6). Moreover, the canonical morphisms $j_!j^*P\to P$
and $P\to j_*j^*P$ come, modulo these isomorphisms, from the monomorphism $A_U\to A$. From the exact sequence (14.10.1)
one therefore derives two exact sequences (12.2 and 12.11); the announced isomorphisms follow by comparison with
(14.6.1) and (14.6.2).

[PDF p. 533]

## Bibliography

[1] M. Artin and B. Mazur, *Homotopy of varieties in the etale topology*, in *Proceedings of a Conference on Local
Fields*, Driebergen 1966, Springer.

[2] P. Gabriel and G. Zisman, *Calculus of fractions and homotopy theory*, Ergebnisse der Mathematik, Bd. 35.

[3] A. Giraud, *Algebre homologique non commutative*, Grundlehren, Springer, 1971.

[4] A. Grothendieck, *Sur quelques points d'algebre homologique*, Tohoku Math. Journal, cited [Toh].

[5] A. Grothendieck, *Fondements de la Geometrie Algebrique* (collection of Bourbaki talks 1957/62), Secretariat
mathematique, 11 rue P. Curie, Paris.

[6] A. Grothendieck, *Crystals and the De Rham cohomology of schemes*, notes by I. Coates and O. Jussila, in *Dix
exposes sur la cohomologie des schemas*, North-Holland, 1969.

[7] A. Grothendieck, *Classes de Chern des representations lineaires des groupes discrets*, in *Dix exposes sur la
cohomologie des schemas*, North-Holland, 1969.

[8] R. Godement, *Theorie des faisceaux*, Act. Scient. Ind. no. 1252, Hermann, Paris, 1958, cited [TF].

[9] M. Hakim, *Topos anneles et schemas relatifs*, mimeographed thesis, Orsay, 1967.

[10] D. Mumford, *Picard groups of moduli problems*, in *Arithmetic Algebraic Geometry*, Harper's Series in Modern
Mathematics.

[11] Nguyen Dinh Ngoc, thesis in Mathematical Sciences, Paris, 1963, no. 4995.

[12] J. E. Roos, *Distributivite des lim par rapport aux lim des topos*, C. R. Acad. Sci. Paris, t. 259, p. 969-972, p.
1160, p. 1801-1804, August and September 1964.

[13] P. Deligne and D. Mumford, *The irreducibility of the space of curves of given genus*, Publ. Math. IHES no. 36,
1969.

[14] B. Mitchell, *Theory of categories*, Academic Press, 1965.
