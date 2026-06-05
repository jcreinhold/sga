# Exposé I. Étale Morphisms

<!-- label: I -->

<!-- original page 1 -->

To simplify the exposition, we assume that all preschemes under consideration are locally noetherian, at least after no.
I.2.

## 1. Notions of Differential Calculus

<!-- label: I.1 -->

Let $X$ be a prescheme over $Y$, and let $\Delta_{X/Y}$, or simply $\Delta$, denote the diagonal morphism $X \to X
\times_{Y} X$. It is an immersion, hence a closed immersion of $X$ into an open subset $V$ of $X \times_{Y} X$. Let
$\mathcal{I}_{X}$ be the ideal of the closed subprescheme corresponding to the diagonal in $V$. Note that if one wants
to do things intrinsically, without assuming $X$ separated over $Y$, a hypothesis that would be farcical here, one
should consider the set-theoretic inverse image of $\mathcal{O}_{X\times X}$ in $X$, and designate by $\mathcal{I}_{X}$
the augmentation ideal in the latter.

The sheaf $\mathcal{I}_{X}/\mathcal{I}^{2}_{X}$ may be regarded as a quasi-coherent sheaf on $X$; it is denoted
$\Omega^{1}_{X/Y}$. It is of finite type if $X \to Y$ is of finite type. It behaves well with respect to an extension of
the base $Y' \to Y$.

One also introduces the sheaves

$$ \mathcal{O}_{X\times_{Y} X}/\mathcal{I}^{n+1}_{X} = \mathcal{P}^{n}_{X/Y}. $$

These are sheaves of rings on $X$, making $X$ into a prescheme that may be denoted $\Delta^{n}_{X/Y}$ and called the
n-th infinitesimal neighborhood of $X/Y$. The sorites for this are of total triviality, although rather long;[^I-1-1] it
would be prudent to speak of them only when one has something useful to say about them, namely with smooth morphisms.

## 2. Quasi-Finite Morphisms

<!-- label: I.2 -->

**Proposition.**

<!-- label: I.2.1 -->

Let $A \to B$ be a local homomorphism; from now on the rings are noetherian. Let $\mathfrak{m}$ be the maximal ideal of
$A$. The following conditions are equivalent:

1. $B/\mathfrak{m}B$ is finite-dimensional over $k = A/\mathfrak{m}$.
1. $\mathfrak{m}B$ is an ideal of definition, and $B/\mathfrak{r}(B) = \kappa(B)$ is an extension of $k = \kappa(A)$.
1. The completion $\hat{B}$ is finite over the completion `Â` of $A$.

One then says that $B$ is quasi-finite over $A$.

<!-- original page 2 -->

A morphism $f: X \to Y$ is said to be quasi-finite at $x$, or the $Y$-prescheme $f$ is said to be quasi-finite at $x$,
if $\mathcal{O}_{x}$ is quasi-finite over $\mathcal{O}_{f(x)}$. This is also equivalent to saying that $x$ is isolated
in its fiber $f^{-1}(f(x))$. A morphism is said to be quasi-finite if it is so at every point.[^I-2-1]

**Corollary.**

<!-- label: I.2.2 -->

If $A$ is complete, quasi-finite is equivalent to finite.

One could give the usual sorites (i), (ii), (iii), (iv), (v) for quasi-finite morphisms, but that does not seem
indispensable here.

## 3. Unramified or Net Morphisms

<!-- label: I.3 -->

**Proposition.**

<!-- label: I.3.1 -->

Let $f: X \to Y$ be a morphism of finite type, let $x \in X$, and let $y = f(x)$. The following conditions are
equivalent:

1. $\mathcal{O}_{x}/\mathfrak{m}_{y}\mathcal{O}_{x}$ is a finite separable extension of $\kappa(y)$.
1. $\Omega^{1}_{X/Y}$ vanishes at $x$.
1. The diagonal morphism $\Delta_{X/Y}$ is an open immersion in a neighborhood of $x$.

For the implication (i) ⇒ (ii), Nakayama immediately reduces us to the case $Y = \operatorname{Spec}(k)$, $X =
\operatorname{Spec}(k')$, where this is well known and, moreover, trivial from the definition of separability. The
implication (ii) ⇒ (iii) follows from a pleasant and easy characterization of open immersions, using Krull. For (iii) ⇒
(i), one is again reduced to the case where $Y = \operatorname{Spec}(k)$ and where the diagonal morphism is everywhere
an open immersion. One must then prove that $X$ is finite with separable coordinate ring over $k$; for this, one reduces
to the case where $k$ is algebraically closed. But then every closed point of $X$ is isolated, since it is identical
with the inverse image of the diagonal by the morphism $X \to X \times_{k} X$ defined by $x$; hence $X$ is finite. We
may then suppose that $X$ is reduced to a point, with ring $A$, so that $A \otimes_{k} A \to A$ is an isomorphism,
whence $A = k$, as required.

**Definition.**

<!-- label: I.3.2 -->

1. One then says that $f$ is net, or also unramified, at $x$, or that $X$ is net, or unramified, at $x$ over $Y$.
1. Let $A \to B$ be a local homomorphism. One says that it is net, or unramified, or that $B$ is a local algebra net, or
   unramified, over $A$, if $B/\mathfrak{r}(A)B$ is a finite separable extension of $A/\mathfrak{r}(A)$, i.e. if
   $\mathfrak{r}(A)B = \mathfrak{r}(B)$, and $\kappa(B)$ is a separable extension of $\kappa(A)$.[^I-3-1]

**Remark.**

<!-- original page 3 -->

The fact that $B$ is net over $A$ can already be recognized on the completions of $A$ and $B$. Net implies quasi-finite.

**Corollary.**

<!-- label: I.3.3 -->

The set of points where $f$ is net is open.

**Corollary.**

<!-- label: I.3.4 -->

Let $X'$ and $X$ be two preschemes of finite type over $Y$, and let $g: X' \to X$ be a $Y$-morphism. If $X$ is net over
$Y$, the graph morphism $\Gamma_{g}: X' \to X \times_{Y} X$ is an open immersion.

Indeed, it is the inverse image of the diagonal morphism $X \to X \times_{Y} X$ by

```text
g ×_Y id_{X′}: X′ ×_Y X → X ×_Y X.
```

One may also introduce the annihilator ideal $\mathfrak{d}_{X/Y}$ of $\Omega^{1}_{X/Y}$, called the different ideal of
$X/Y$; it defines a closed subprescheme of $X$ which, set-theoretically, is the set of points where $X/Y$ is ramified,
i.e. not net.

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
1. If `gf` is net, then $f$ is net.
1. If $f$ is net, then $f_{red}$ is net.

**Proposition.**

<!-- label: I.3.7 -->

Let $A \to B$ be a local homomorphism, and suppose that the residue extension $\kappa(B)/\kappa(A)$ is trivial, or that
$\kappa(A)$ is algebraically closed. For $B/A$ to be net, it is necessary and sufficient that $\hat{B}$ be, as an
`Â`-algebra, a quotient of `Â`.

**Remarks.**

- In the case where the residue extension is not assumed trivial, one can reduce to that case by making a suitable
  finite flat extension over $A$ that kills the given extension.
- Give the example where $A$ is the local ring of an ordinary double point of a curve, and $B$ that of a point of the
  normalization: then $A \subset B$, $B$ is net over $A$ with trivial residue extension, and $\hat{A} \to \hat{B}$ is
  surjective but not injective.

<!-- original page 4 -->

We shall therefore strengthen the notion of netness.

## 4. Étale Morphisms. Étale Coverings

<!-- label: I.4 -->

We shall admit everything that will be necessary for us concerning flat morphisms; these facts will be proved later, if
needed.[^I-4-1]

**Definition.**

<!-- label: I.4.1 -->

1. Let $f: X \to Y$ be a morphism of finite type. One says that $f$ is étale at $x$ if $f$ is flat at $x$ and net at
   $x$. One says that $f$ is étale if it is so at all points. One says that $X$ is étale at $x$ over $Y$, or that it is
   a $Y$-prescheme étale at $x$, etc.
1. Let $f: A \to B$ be a local homomorphism. One says that $f$ is étale, or that $B$ is étale over $A$, if $B$ is flat
   and unramified over $A$.[^I-4-2]

**Proposition.**

<!-- label: I.4.2 -->

For $B/A$ to be étale, it is necessary and sufficient that $\hat{B}/\hat{A}$ be étale.

Indeed, this is true separately for "net" and for "flat".

<!-- original page 5 -->

**Corollary.**

<!-- label: I.4.3 -->

Let $f: X \to Y$ be of finite type, and let $x \in X$. The fact that $f$ is étale at $x$ depends only on the local
homomorphism $\mathcal{O}_{f(x)} \to \mathcal{O}_{x}$, and even only on the corresponding homomorphism for completions.

**Corollary.**

<!-- label: I.4.4 -->

Suppose that the residue extension $\kappa(A) \to \kappa(B)$ is trivial, or that $\kappa(A)$ is algebraically closed.
Then $B/A$ is étale if and only if $\hat{A} \to \hat{B}$ is an isomorphism.

One combines flatness with I.3.7.

**Proposition.**

<!-- label: I.4.5 -->

Let $f: X \to Y$ be a morphism of finite type. Then the set of points where it is étale is open.

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

Let $X$ and $X'$ be of finite type over $Y$, and let $g: X \to X'$ be a $Y$-morphism. If $X'$ is unramified over $Y$ and
$X$ is étale over $Y$, then $g$ is étale.

Indeed, $g$ is the composite of the graph morphism $\Gamma_{g}: X \to X \times_{Y} X'$, which is an open immersion by
I.3.4, and the projection morphism, which is étale because it is deduced from the étale morphism $X \to Y$ by the base
change $X' \to Y$.

**Definition.**

<!-- label: I.4.9 -->

An étale covering, respectively a net covering, of $Y$ is a $Y$-scheme $X$ that is finite over $Y$ and étale,
respectively net, over $Y$.

The first condition means that $X$ is defined by a coherent sheaf $\mathcal{B}$ of algebras on $Y$. The second then
means that $\mathcal{B}$ is locally free over $Y$, respectively says nothing at all, and that moreover, for every $y \in
Y$, the fiber $\mathcal{B}(y) = \mathcal{B}_{y} \otimes_{\mathcal{O}_{y}} \kappa(y)$ is a separable algebra, that is, a
finite product of finite separable extensions, over $\kappa(y)$.

**Proposition.**

<!-- label: I.4.10 -->

Let $X$ be a flat covering of $Y$ of degree $n$, defined by a coherent locally free sheaf $\mathcal{B}$ of algebras. One
defines, in the well-known way, the trace homomorphism $\mathcal{B} \to \mathcal{A}$, which is a homomorphism of
$\mathcal{A}$-modules, where $\mathcal{A} = \mathcal{O}_{Y}$. For $X$ to be étale, it is necessary and sufficient that
the corresponding bilinear form $tr_{\mathcal{B}/\mathcal{A}}(xy)$ define an isomorphism from $\mathcal{B}$ to its dual,
or equivalently that the discriminant section

```text
d_{X/Y} = d_{𝓑/𝓐} ∈ Γ(Y, ∧ⁿ𝓑̌ ⊗_𝓐 ∧ⁿ𝓑̌)
```

be invertible, or finally that the discriminant ideal defined by this section be the unit ideal.

Indeed, one is reduced to the case $Y = \operatorname{Spec}(k)$, and then this is a well-known separability criterion,
and trivial after passage to the algebraic closure of $k$.

**Remark.**

<!-- original page 6 -->

We shall have a less trivial statement below, when one does not suppose a priori that $X$ is flat over $Y$ but makes a
normality hypothesis.

## 5. The Fundamental Property of Étale Morphisms

<!-- label: I.5 -->

**Theorem.**

<!-- label: I.5.1 -->

Let $f: X \to Y$ be a morphism of finite type. For $f$ to be an open immersion, it is necessary and sufficient that it
be an étale and radicial morphism.

Recall that radicial means: injective, with radicial residue extensions; one may also recall that this means that the
morphism remains injective after every base extension. Necessity is trivial; sufficiency remains. We shall give two
different proofs, the first shorter, the second more elementary.

1. A flat morphism is open, so we may suppose, replacing $Y$ by $f(X)$, that $f$ is a homeomorphism onto $Y$. After any
   base extension, it remains true that $f$ is flat, radicial, and surjective, hence a homeomorphism, a fortiori closed.
   Thus $f$ is proper. Therefore $f$ is finite, by Chevalley's theorem, and is defined by a coherent sheaf $\mathcal{B}$
   of algebras. The sheaf $\mathcal{B}$ is locally free; moreover, by the hypothesis, it has rank 1 everywhere. Thus $X
   = Y$, as required.

1. One may suppose $Y$ and $X$ affine. Moreover, one easily reduces to proving the following: if $Y =
   \operatorname{Spec}(A)$, with $A$ local, and if $f^{-1}(y)$ is nonempty, where $y$ is the closed point of $Y$, then
   $X = Y$. Indeed, this will imply that every $y \in f(X)$ has an open neighborhood $U$ such that $X|U = U$. We have $X
   = \operatorname{Spec}(B)$, and we want to prove $A = B$. For this, one is reduced to proving the analogous assertion
   after replacing $A$ by `Â` and $B$ by $B \otimes_{A} \hat{A}$, taking into account that `Â` is faithfully flat over
   $A$. We may therefore suppose $A$ complete. Let $x$ be the point over $y$. By Corollary I.2.2, $\mathcal{O}_{x}$ is
   finite over $A$, hence, being flat and radicial over $A$, is identical with $A$. Thus $X = Y \amalg X'$, a disjoint
   sum. Since $X$ is radicial over $Y$, $X'$ is empty. This completes the proof.

**Corollary.**

<!-- label: I.5.2 -->

Let $f: X \to Y$ be a closed immersion and étale. If $X$ is connected, $f$ is an isomorphism from $X$ onto a connected
component of $Y$.

Indeed, $f$ is also an open immersion. We deduce:

**Corollary.**

<!-- label: I.5.3 -->

<!-- original page 7 -->

Let $X$ be a net $Y$-scheme, with $Y$ connected. Then every section of $X$ over $Y$ is an isomorphism from $Y$ onto a
connected component of $X$. Thus there is a one-to-one correspondence between the set of these sections and the set of
connected components $X_{i}$ of $X$ such that the projection $X_{i} \to Y$ is an isomorphism, or equivalently, by I.5.1,
is surjective and radicial. In particular, a section is known once its value at one point is known.

Only the first assertion requires proof. By I.5.2, it is enough to observe that a section is a closed immersion, since
$X$ is separated over $Y$, and is étale by I.4.8.

**Corollary.**

<!-- label: I.5.4 -->

Let $X$ and $Y$ be two preschemes over $S$, with $X$ net and separated over $S$ and $Y$ connected. Let $f$ and $g$ be
two $S$-morphisms from $Y$ to $X$, and let $y$ be a point of $Y$. Suppose $f(y) = g(y) = x$ and that the residue
homomorphisms $\kappa(x) \to \kappa(y)$ defined by $f$ and $g$ are identical, that is, $f$ and $g$ coincide
geometrically at $y$. Then $f$ and $g$ are identical.

This follows from I.5.3 by reducing to the case $Y = S$, replacing $X$ by $X \times_{S} Y$.

Here is a particularly important variant of I.5.3.

**Theorem.**

<!-- label: I.5.5 -->

Let $S$ be a prescheme, $X$ and $Y$ two $S$-preschemes, $S_{0}$ a closed subprescheme of $S$ having the same underlying
space as $S$, and let $X_{0} = X \times_{S} S_{0}$ and $Y_{0} = Y \times_{S} S_{0}$ be the "restrictions" of $X$ and $Y$
to $S_{0}$. Suppose $X$ is étale over $S$. Then the natural map

```text
Hom_S(Y, X) → Hom_{S₀}(Y₀, X₀)
```

is bijective.

One is again reduced to the case $Y = S$, and then this follows from the "topological" description of sections of $X/Y$
given in I.5.3.

**Scholium.** This result includes both a uniqueness assertion and an existence assertion for morphisms. It may also be
expressed, when $X$ and $Y$ are both taken étale over $S$, by saying that the functor $X \mapsto X_{0}$ from the
category of étale $S$-schemes to the category of étale $S_{0}$-schemes is fully faithful, i.e. establishes an
equivalence of the first category with a full subcategory of the second. We shall see below that it is even an
equivalence between the first and the second; this will be an existence theorem for étale $S$-schemes.

<!-- original page 8 -->

The following form, apparently more general, of I.5.5 is often convenient.

**Corollary ("Extension theorem for liftings").**

<!-- label: I.5.6 -->

Consider a commutative diagram

$$ Y_{0} \to X \downarrow \downarrow Y \to S $$

of morphisms, where $X \to S$ is étale and $Y_{0} \to Y$ is a bijective closed immersion. Then one can find a unique
morphism $Y \to X$ making the two corresponding triangles commute.

Indeed, replacing $S$ by $Y$ and $X$ by $X \times_{S} Y$, one is reduced to the case $Y = S$, and then this is the
special case of I.5.5 for $Y = S$.

Let us also record the following immediate consequence of I.5.1, which we did not give as Corollary 1 so as not to
interrupt the line of ideas developed after I.5.1.

**Proposition.**

<!-- label: I.5.7 -->

Let $X$ and $X'$ be two preschemes of finite type and flat over $Y$, and let $g: X \to X'$ be a $Y$-morphism. For $g$ to
be an open immersion, respectively an isomorphism, it is necessary and sufficient that for every $y \in Y$, the induced
morphism on fibers

```text
g ⊗_Y κ(y): X ⊗_Y κ(y) → X′ ⊗_Y κ(y)
```

be an open immersion, respectively an isomorphism.

It suffices to prove sufficiency; since this is true for the notion of surjection, one is reduced to the case of an open
immersion. By I.5.1, one must verify that $g$ is radicial, which is trivial, and that it is étale, which follows from
Corollary I.5.9 below.

**Corollary.**

<!-- label: I.5.8 -->

(This should go in no. I.3.) Let $X$ and $X'$ be two $Y$-preschemes, let $g: X \to X'$ be a $Y$-morphism, let $x$ be a
point of $X$, and let $y$ be its projection to $Y$. For $g$ to be quasi-finite, respectively net, at $x$, it is
necessary and sufficient that the same be true of $g \otimes_{Y} \kappa(y)$.

Indeed, the two algebras over $k(g(x))$ that must be considered to ensure that one has a quasi-finite, respectively net,
morphism at $x$ are the same for $g$ and for $g \otimes_{Y} \kappa(y)$.

**Corollary.**

<!-- label: I.5.9 -->

<!-- original page 9 -->

With the notation of I.5.8, suppose $X$ and $X'$ are flat and of finite type over $Y$. For $g$ to be flat, respectively
étale, at $x$, it is necessary and sufficient that $g \otimes_{Y} \kappa(y)$ be so.

For "flat" the statement is included only as a reminder; it is one of the fundamental criteria for flatness.[^I-5-1] For
"étale", it follows from this, taking I.5.8 into account.

## 6. Application to Étale Extensions of Complete Local Rings

<!-- label: I.6 -->

This number is a special case of results on formal preschemes that should appear in the multiplodocus. Nevertheless,
here one gets by at less cost, i.e. without the explicit local determination of étale morphisms in no. I.7, which uses
the Main Theorem. That may be a sufficient reason to keep the present number, even in the multiplodocus, in this place.

**Theorem.**

<!-- label: I.6.1 -->

Let $A$ be a complete local ring, noetherian of course, with residue field $k$. For every $A$-algebra $B$, let $R(B) = B
\otimes_{A} k$, considered as a $k$-algebra; it thus depends functorially on $B$. Then $R$ defines an equivalence from
the category of $A$-algebras finite and étale over $A$ to the category of finite-rank separable algebras over $k$.

First of all, the functor in question is fully faithful, as follows from the more general fact:

**Corollary.**

<!-- label: I.6.2 -->

Let $B$ and $B'$ be two $A$-algebras finite over $A$. If $B$ is étale over $A$, then the canonical map

```text
Hom_{A-alg}(B, B′) → Hom_{k-alg}(R(B), R(B′))
```

is bijective.

One is reduced to the case where $A$ is artinian, replacing $A$ by $A/\mathfrak{m}^{n}$, and then this is a special case
of I.5.5.

It remains to prove that for every finite separable $k$-algebra, why not say étale, since it is shorter, $L$, there
exists $B$ étale over $A$ such that $R(B)$ is isomorphic to $L$. We may suppose that $L$ is a separable extension of
$k$; as such it admits a generator $x$, i.e. is isomorphic to an algebra $k[t]/Fk[t]$, where $F \in k[t]$ is a monic
polynomial. Lift $F$ to a monic polynomial $F_{1}$ in `A[t]`, and take $B = A[t]/F_{1}A[t]$.

## 7. Local Construction of Unramified and Étale Morphisms

<!-- label: I.7 -->

<!-- original page 10 -->

**Proposition.**

<!-- label: I.7.1 -->

Let $A$ be a noetherian ring, $B$ a finite algebra over $A$, $u$ a generator of $B$ over $A$, $F \in A[t]$ such that
$F(u) = 0$, where $F$ is not assumed monic, $u' = F'(u)$, where $F'$ is the derived polynomial, $\mathfrak{q}$ a prime
ideal of $B$ not containing $u'$, and $\mathfrak{p}$ its trace on $A$. Then $B_{\mathfrak{q}}$ is net over
$A_{\mathfrak{p}}$.

In other words, putting $Y = \operatorname{Spec}(A)$, $X = \operatorname{Spec}(B)$, and $X_{u'} =
\operatorname{Spec}(B_{u'})$, $X_{u'}$ is unramified over $Y$. The statement follows from the following more precise
one.

**Corollary.**

<!-- label: I.7.2 -->

The different ideal of $B/A$ contains $u'B$, and is equal to it if the natural homomorphism $A[t]/FA[t] \to B$, sending
$t$ to $u$, is an isomorphism.

Let $J$ be the kernel of the homomorphism $C = A[t] \to B$. This kernel contains `FA[t]`, and is equal to it in the
second case considered in I.7.2. Since the homomorphism is surjective, $\Omega^{1}_{B/A}$ identifies with the quotient
of $\Omega^{1}_{C/A}$ by the submodule generated by $J\Omega^{1}_{C/A}$ and $d(J)$; one should have made explicit in no.
I.1 the definition of the homomorphism $d$ and the computation of $\Omega^{1}$ for a polynomial algebra. Identifying
$\Omega^{1}_{C/A}$ with $C$ by means of the basis `dt`, one finds $B/B\cdot J'$, so the different is generated by the
set $J'$ of images in $B$ of the derivatives of $G \in J$, and it suffices to take $G$ running through generators of
$J$.

Since $F \in J$, respectively since $F$ is a generator of $J$, we are done. Note that I.7.2 should be made the
proposition and I.7.1 the corollary. We find:

**Corollary.**

<!-- label: I.7.3 -->

Under the conditions of I.7.1, suppose $F$ is monic and that $A[t]/FA[t] \to B$ is an isomorphism. For
$B_{\mathfrak{q}}$ to be étale over $A_{\mathfrak{p}}$, it is necessary and sufficient that $\mathfrak{q}$ not contain
$u'$.

Indeed, since $B$ is flat over $A$, étale is equivalent to net, and one may apply I.7.2.

**Corollary.**

<!-- label: I.7.4 -->

Under the conditions of I.7.3, for $B$ to be étale over $A$, it is necessary and sufficient that $u'$ be invertible, or
again that the ideal generated by $F$ and $F'$ in `A[t]` be the unit ideal.

The last criterion follows from the first and from Nakayama, in $B$.

<!-- original page 11 -->

A monic polynomial $F \in A[t]$ having the property stated in Corollary I.7.4 is called a separable polynomial. If $F$
is not monic, one would at least have to require that the coefficient of its leading term be invertible; in the case
where $A$ is a field, one recovers the usual definition.

**Corollary.**

<!-- label: I.7.5 -->

Let $B$ be a finite algebra over the local ring $A$. Suppose that $K(A)$ is infinite or that $B$ is local. Let $n$ be
the rank of $L = B \otimes_{A} K(A)$ over $K(A) = k$. For $B$ to be net, respectively étale, over $A$, it is necessary
and sufficient that $B$ be isomorphic to a quotient of, respectively isomorphic to, $A[t]/FA[t]$, where $F$ is a monic
separable polynomial, which one may suppose, respectively which is necessarily, of degree $n$.

Only necessity has to be proved. Suppose $B$ is net over $A$, hence $L$ is separable over $k$. It then follows from the
hypothesis made that $L/k$ admits a generator $\xi$, so the $\xi^{i}$, with $0 \leq i < n$, form a basis of $L$ over
$k$. Let $u \in B$ lift $\xi$. Then, by Nakayama, the $u^{i}$, with $0 \leq i < n$, generate the $A$-module $B$,
respectively form a basis of it. In particular, one can find a monic polynomial $F \in A[t]$ such that $F(u) = 0$, and
$B$ will be isomorphic to a quotient of, respectively isomorphic to, $A[t]/FA[t]$. Finally, by I.7.4 applied to $L/k$,
$F$ and $F'$ generate `A[t]` modulo $\mathfrak{m}A[t]$, hence by Nakayama in $A[t]/FA[t]$, $F$ and $F'$ generate `A[t]`.
This completes the proof.

**Theorem.**

<!-- label: I.7.6 -->

Let $A$ be a local ring, and let $A \to \mathcal{O}$ be a local homomorphism such that $\mathcal{O}$ is isomorphic to a
localized algebra of an algebra of finite type over $A$. Suppose $\mathcal{O}$ is net over $A$. Then one can find an
$A$-algebra $B$, integral over $A$, a maximal ideal $\mathfrak{n}$ of $B$, a generator $u$ of $B$ over $A$, and a monic
polynomial $F \in A[t]$, such that $\mathfrak{n}$ does not contain $F'(u)$ and $\mathcal{O}$ is isomorphic, as an
$A$-algebra, to $B_{\mathfrak{n}}$. If $\mathcal{O}$ is étale over $A$, one can take $B = A[t]/FA[t]$.

Of course, these are also sufficient conditions.

Let us first record the pleasant corollaries.

**Corollary.**

<!-- label: I.7.7 -->

For $\mathcal{O}$ to be net over $A$, it is necessary and sufficient that $\mathcal{O}$ be isomorphic to the quotient of
an analogous algebra that is étale over $A$.

Indeed, take $\mathcal{O}' = {{B'_{\mathfrak{n}}}'}$, where $B' = A[t]/FA[t]$ and where $\mathfrak{n}'$ is the inverse
image of $\mathfrak{n}$ in $B'$.

**Corollary.**

<!-- label: I.7.8 -->

<!-- original page 12 -->

Let $f: X \to Y$ be a morphism of finite type, and let $x \in X$. For $f$ to be net at $x$, it is necessary and
sufficient that there exist an open neighborhood $U$ of $x$ such that $f|U$ factors as $U \to X' \to Y$, where the first
arrow is a closed immersion and the second is an étale morphism.

This is a simple translation of I.7.7.

Let us show how the jargon of I.7.6 follows from the principal statement: indeed, by I.7.7 there exists an epimorphism
$\mathcal{O}' \to \mathcal{O}$, where $\mathcal{O}$ has the required properties; but since $\mathcal{O}'$ and
$\mathcal{O}$ are étale over $A$, the morphism $\mathcal{O}' \to \mathcal{O}$ is étale by I.4.8, hence an isomorphism.

### Proof of I.7.6

This repeats a proof from Chevalley's seminar. By the Main Theorem, one will have $\mathcal{O} = B_{\mathfrak{n}}$,
where $B$ is a finite algebra over $A$ and $\mathfrak{n}$ is a maximal ideal of $B$. Then $B/\mathfrak{n} =
K(\mathcal{O})$ is a separable, hence monogenic, extension of $k$. If $\mathfrak{n}_{i}$, $1 \leq i \leq r$, are the
maximal ideals of $B$ distinct from $\mathfrak{n}$, there therefore exists an element $u$ of $B$ that belongs to all the
$\mathfrak{n}_{i}$ and whose image in $B/\mathfrak{n}$ is a generator. But $B/\mathfrak{n} =
B_{\mathfrak{n}}/\mathfrak{n}B_{\mathfrak{n}} = B_{\mathfrak{n}}/\mathfrak{m}B_{\mathfrak{n}}$, where $\mathfrak{m}$ is
the maximal ideal of $A$. Let us admit for a moment the following lemma.

**Lemma.**

<!-- label: I.7.9 -->

Let $A$ be a local ring, $B$ a finite algebra over $A$, $\mathfrak{n}$ a maximal ideal of $B$, and $u$ an element of $B$
whose image in $B_{\mathfrak{n}}/\mathfrak{m}B_{\mathfrak{n}}$ generates it as an algebra over $k = A/\mathfrak{m}$, and
which lies in every maximal ideal of $B$ distinct from $\mathfrak{n}$. Let $B' = B[u]$ and $\mathfrak{n}' =
\mathfrak{n}B'$. Then the canonical homomorphism ${{B'_{\mathfrak{n}}}'} \to B_{\mathfrak{n}}$ is an isomorphism.

**Lemma.**

<!-- label: I.7.10 -->

(This should have appeared as a corollary to I.7.1, before I.7.5, which it implies.) Let $B$ be a finite algebra over
$A$ generated by an element $u$, and let $\mathfrak{n}$ be a maximal ideal of $B$ such that $B_{\mathfrak{n}}$ is
unramified over $A$. Then there exists a monic polynomial $F \in A[t]$ such that $F(u) = 0$ and $F'(u) \notin
\mathfrak{n}$.

Indeed, let $n$ be the rank of the $k$-algebra $L = B \otimes_{A} k$. By Nakayama, there exists a monic polynomial of
degree $n$ in `A[t]` such that $F(u) = 0$. Let $f$ be the polynomial deduced from $F$ by reduction mod $\mathfrak{m}$.
Then $L$ is $k$-isomorphic to $k[t]/fk[t]$, hence by I.7.3, $f'(\xi)$ is not contained in the maximal ideal of $L$
corresponding to $\mathfrak{n}$, where $\xi$ denotes the image of $t$ in $L$, i.e. the image of $u$ in $L$. Since
$f'(\xi)$ is the image of $F'(u)$, we are done.

<!-- original page 13 -->

Theorem I.7.6 now follows by combining I.7.9 and I.7.10. It remains to prove I.7.9. Put $S' = B' - \mathfrak{n}'$, so
$B'S'^{-1} = {{B'_{\mathfrak{n}}}'}$. Similarly let $S = B - \mathfrak{n}$, so $BS^{-1} = B_{\mathfrak{n}}$. We
therefore have a natural homomorphism $B S'^{-1} \to BS^{-1} = B_{\mathfrak{n}}$. Let us prove that it is an
isomorphism, i.e. that the elements of $S$ are invertible in $B S'^{-1}$, i.e. that every maximal ideal $\mathfrak{p}$
of the latter does not meet $S$, i.e. induces $\mathfrak{n}$ on $B$.

Indeed, since $B S'^{-1}$ is finite over $B'S'^{-1} = {{B'_{\mathfrak{n}}}'}$, $\mathfrak{p}$ induces the unique maximal
ideal $\mathfrak{n}'{{B'_{\mathfrak{n}}}'}$ of ${{B'_{\mathfrak{n}}}'}$, hence induces the maximal ideal $\mathfrak{n}'$
of $B'$. Since $B$ is finite over $B'$, the ideal $\mathfrak{q}$ of $B$ induced by $\mathfrak{p}$, lying over
$\mathfrak{n}'$, is necessarily maximal and does not contain $u$, hence is identical with $\mathfrak{n}$. Here we have
just used that $u$ belongs to every maximal ideal of $B$ distinct from $\mathfrak{n}$.

Let us now prove that $B S'^{-1}$ equals $B'S'^{-1}$. Since it is finite over the latter, Nakayama reduces us to proving
equality modulo $\mathfrak{n}'B S'^{-1}$, and a fortiori it suffices to prove equality modulo $\mathfrak{m}B S'^{-1}$.
But

```text
B S′⁻¹ / 𝔪B S′⁻¹ = B_𝔫 / 𝔪B_𝔫
```

is generated over $k$ by $u$, using here the other property of $u$. Thus the image of $B'$, and a fortiori of
$B'S'^{-1}$, in it is everything, as a subring containing $k$ and the image of $u$.

**Remark.** One should be able to state Theorem I.7.6 for a ring $\mathcal{O}$ that is only semilocal, so as also to
cover I.7.5: one would make the hypothesis that $\mathcal{O}/\mathfrak{m}\mathcal{O}$ is a monogenic $k$-algebra. One
could then find $u \in B$ whose image in $B/\mathfrak{m}B$ is a generator and which belongs to all maximal ideals of $B$
not coming from $\mathcal{O}$. Lemmas I.7.9 and I.7.10 should adapt without difficulty. More generally, ...

## 8. Infinitesimal Lifting of Étale Schemes. Application to Formal Schemes

<!-- label: I.8 -->

**Proposition.**

<!-- label: I.8.1 -->

Let $Y$ be a prescheme, $Y_{0}$ a subprescheme, $X_{0}$ an étale $Y_{0}$-scheme, and $x$ a point of $X_{0}$. Then there
exists an étale $Y$-scheme $X$, a neighborhood $U_{0}$ of $x$ in $X_{0}$, and a $Y_{0}$-isomorphism $U_{0} \cong X
\times_{Y} Y_{0}$.

Indeed, let $y$ be the projection of $x$ in $Y_{0}$. Applying I.7.6 to the étale local homomorphism $A_{0} \to B_{0}$ of
the local rings of $y$ and $x$ in $Y_{0}$ and $X_{0}$, one finds an isomorphism

```text
B₀ = (C₀)_{𝔫₀},     C₀ = A₀[t]/F₀A₀[t],
```

where $F_{0}$ is a monic polynomial and $\mathfrak{n}_{0}$ is a maximal ideal of $C_{0}$ not containing the class of
$F'_{0}(t)$ in $C_{0}$. Let $A$ be the local ring of $y$ in $Y$, let $F$ be a monic polynomial in `A[t]` giving $F_{0}$
under the surjective homomorphism $A \to A_{0}$, by lifting the coefficients of $F_{0}$, and finally let $C =
A[t]/FA[t]$, and let $\mathfrak{n}$ be the maximal ideal of $C$ which is the inverse image of $\mathfrak{n}_{0}$ under
the natural epimorphism $C \to C \otimes_{A} A_{0} = C_{0}$. Put $B = C_{\mathfrak{n}}$. It is immediate by construction
and I.7.1 that $B$ is étale over $A$, and that one has an isomorphism $B \otimes_{A} A_{0} = A_{0}$.

One knows, from EGA Chapter I as indicated in the introduction, that there exists a $Y$-scheme of finite type $X$ and a
point $z$ of $X$ over $y$ such that $\mathcal{O}_{z}$ is $A$-isomorphic to $C$. Since the latter is étale over $A =
\mathcal{O}_{y}$, one may, by taking $X$ small enough, suppose that $X$ is étale over $Y$. Let $X'_{0} = X \times_{Y}
Y_{0}$. Then the local ring of $z$ in $X'_{0}$ identifies with $\mathcal{O}_{z} \otimes_{A} A_{0} = B \otimes_{A}
A_{0}$, hence is isomorphic to $B_{0}$. This isomorphism is defined by an isomorphism from a neighborhood $U_{0}$ of $x$
in $X_{0}$ onto a neighborhood of $z$ in $X'_{0}$, and by taking $X$ small enough one may suppose this neighborhood
identical with $X'_{0}$. We are done.

**Corollary.**

<!-- label: I.8.2 -->

There is an analogous statement for étale coverings, assuming the residue field $\kappa(y)$ infinite.

The proof is the same, with I.7.5 replacing I.7.6.

**Theorem.**

<!-- label: I.8.3 -->

The functor considered in I.5.5 is an equivalence of categories.

By Theorem I.5.5, it remains to show that every étale $S_{0}$-scheme $X_{0}$ is isomorphic to an $S_{0}$-scheme $X
\times_{S} S_{0}$, where $X$ is an étale $S$-scheme. The underlying topological space of $X$ must necessarily be
identical with that of $X_{0}$, with $X_{0}$ furthermore identifying with a closed subprescheme of $X$.

The problem is therefore equivalent to the following one: find on the underlying topological space $|X_{0}|$ of $X_{0}$
a sheaf of algebras $\mathcal{O}_{X}$ over `f₀⁎(𝒪_S)`, where $f_{0}$ is the projection $X_{0} \to S_{0}$, here regarded
as a continuous map of underlying spaces, making $|X_{0}|$ into an étale $S$-prescheme $X$, together with a homomorphism
of algebras $\mathcal{O}_{X} \to \mathcal{O}_{X_{0}}$, compatible with the homomorphism `f₀⁎(𝒪_S) → f₀⁎(𝒪_{S₀})` on the
sheaves of scalars, and inducing an isomorphism

```text
𝒪_X ⊗_{f₀⁎(𝒪_S)} f₀⁎(𝒪_{S₀}) ≅ 𝒪_{X₀}.
```

Then $X$ will be an étale $S$-prescheme reducing to $X_{0}$.

<!-- original page 15 -->

Thus $X$ will be separated over $S$, since $X_{0}$ is separated over $S_{0}$, and $X$ answers the question. Moreover, if
$(U_{i})$ is a covering of $X_{0}$ by open subsets, and if one has found a solution of the problem in each $U_{i}$, then
it follows from the uniqueness theorem I.5.5 that these solutions glue, i.e. that the sheaves of algebras defining them,
equipped with their augmentation homomorphisms, glue; one immediately checks that the locally ringed space thereby
constructed over $S$ is an étale $S$-prescheme $X$ equipped with an isomorphism $X \times_{S} S_{0} \cong X_{0}$. It
therefore suffices to find a solution locally, which is assured by I.8.1.

**Corollary.**

<!-- label: I.8.4 -->

Let $S$ be a locally noetherian formal prescheme, equipped with an ideal of definition $J$, and let $S_{0} = (|S|,
\mathcal{O}_{S}/J)$ be the corresponding ordinary prescheme. Then the functor $\mathfrak{X} \mapsto \mathfrak{X}
\times_{S} S_{0}$ from the category of étale coverings of $S$ to the category of étale coverings of $S_{0}$ is an
equivalence of categories.

Of course, by an étale covering of a formal prescheme $S$ we mean a covering of $S$, i.e. a formal prescheme over $S$
defined by a coherent sheaf $\mathcal{B}$ of algebras, such that $\mathcal{B}$ is locally free and such that the residue
fibers $\mathcal{B}_{s} \otimes_{\mathcal{O}_{s}} \kappa(s)$ of $\mathcal{B}$ are separable algebras over $\kappa(s)$.
If $S_{n}$ denotes the ordinary prescheme $(|S|, \mathcal{O}_{S}/J^{n+1})$, the data of a coherent sheaf of algebras
$\mathcal{B}$ on $S$ is equivalent to the data of a sequence of coherent sheaves of algebras $\mathcal{B}_{n}$ on the
$S_{n}$, equipped with a transitive system of homomorphisms $\mathcal{B}_{m} \to \mathcal{B}_{n}$, for $m \geq n$,
defining isomorphisms

```text
𝓑_m ⊗_{𝒪_{S_m}} 𝒪_{S_n} ≅ 𝓑_n.
```

It is immediate that $\mathcal{B}$ is locally free if and only if the $\mathcal{B}_{n}$ on the $S_{n}$ are locally free,
and that the separability condition is satisfied if and only if it is satisfied for $\mathcal{B}_{0}$, or equivalently
for all the $\mathcal{B}_{n}$. Thus $\mathcal{B}$ is étale over $S$ if and only if the $\mathcal{B}_{n}$ over the
$S_{n}$ are étale. Taking this into account, I.8.4 follows at once from I.8.3.

**Remark.** It was not necessary in I.8.4 to restrict to the case of coverings. It is, however, the only case used for
the moment.

## 9. Permanence Properties

<!-- label: I.9 -->

Let $A \to B$ be a local and étale homomorphism. We examine here a few cases where a certain property of $A$ implies the
same property for $B$, or conversely.

<!-- original page 16 -->

A certain number of such propositions are already consequences of the simple fact that $B$ is quasi-finite and flat over
$A$, and we shall limit ourselves to "recalling" a few of them: $A$ and $B$ have the same Krull dimension and the same
depth, "cohomological codimension" in Serre's still-current terminology. It follows, for example, that $A$ is
Cohen-Macaulay if and only if $B$ is Cohen-Macaulay.

Moreover, for every prime ideal $\mathfrak{q}$ of $B$ inducing $\mathfrak{p}$ on $A$, $B_{\mathfrak{q}}$ will again be
quasi-finite and flat over $A_{\mathfrak{p}}$, provided $B$ is assumed to be a localization of an algebra of finite type
over $A$; this follows from the fact that the set of points where a morphism of finite type is quasi-finite,
respectively flat, is open. And moreover every prime ideal $\mathfrak{p}$ of $A$ is induced by a prime ideal
$\mathfrak{q}$ of $B$, because $B$ is faithfully flat over $A$. It follows for example that $\mathfrak{p}$ and
$\mathfrak{q}$ have the same rank, and also that $A$ has no embedded prime ideal if and only if $B$ has none.

We shall therefore restrict ourselves to propositions more special to the case of étale morphisms.

**Proposition.**

<!-- label: I.9.1 -->

Let $A \to B$ be a local étale homomorphism. For $A$ to be regular, it is necessary and sufficient that $B$ be regular.

Indeed, let $k$ be the residue field of $A$, and $L$ that of $B$. Since $B$ is flat over $A$ and $L = B \otimes_{A} k$,
i.e. $\mathfrak{n} = \mathfrak{m}B$, where $\mathfrak{m}$ and $\mathfrak{n}$ are the maximal ideals of $A$ and $B$, the
$\mathfrak{m}$-adic filtration on $B$ is identical with its $\mathfrak{n}$-adic filtration, and one will have

```text
gr*(B) = gr*(A) ⊗_k L.
```

It follows that $gr*(B)$ is a polynomial algebra over $L$ if and only if $gr*(A)$ is a polynomial algebra over $k$. This
proves the assertion. Note that we did not use the fact that $L/k$ is separable.

**Corollary.**

<!-- label: I.9.2 -->

Let $f: X \to Y$ be an étale morphism. If $Y$ is regular, then $X$ is regular; the converse is true if $f$ is
surjective.

**Proposition.**

<!-- label: prop:I.9.2 -->

Let $f: X \to Y$ be an étale morphism. If $Y$ is reduced, then so is $X$; the converse is true if $f$ is surjective.

This is equivalent to:

**Corollary.**

<!-- label: I.9.3 -->

<!-- original page 17 -->

Let $f: A \to B$ be a local étale homomorphism, with $B$ isomorphic to a localized $A$-algebra of an $A$-algebra of
finite type. For $A$ to be reduced, it is necessary and sufficient that $B$ be reduced.

Necessity is trivial, since $A \to B$ is injective, $B$ being faithfully flat over $A$. For sufficiency, let
$\mathfrak{p}_{i}$ be the minimal prime ideals of $A$. By hypothesis the natural map $A \to \prod_{i}
A/\mathfrak{p}_{i}$ is injective; tensoring with the flat $A$-module $B$, one finds that $B \to \prod_{i}
B/\mathfrak{p}_{iB}$ is injective, and one is reduced to proving that the $B/\mathfrak{p}_{iB}$ are reduced. Since
$B/\mathfrak{p}_{iB}$ is étale over $A/\mathfrak{p}_{i}$, one is reduced to the case where $A$ is integral.

Let $K$ be its field of fractions. Since $A \to K$ is injective, the same is true, $B$ being $A$-flat, of $B \to B
\otimes_{A} K$; we are reduced to proving that this latter ring is reduced. But $B$, being a localization of an
$A$-algebra of finite type over $A$, is the local ring of a point $x$ of a scheme $X = \operatorname{Spec}(C)$ of finite
type and étale over $Y = \operatorname{Spec}(A)$. Thus $B \otimes_{A} K$ is a localized ring, with respect to a suitable
multiplicatively stable set, of the ring $C \otimes_{A} K$ of $X \otimes_{A} K$. Since $X \otimes_{A} K$ is étale over
$K$, its ring is a finite product of fields, separable extensions of $K$, and the same is therefore true of $B
\otimes_{A} K$. This proves the assertion.

**Corollary.**

<!-- label: I.9.4 -->

Let $f: A \to B$ be a local étale homomorphism, and suppose $A$ analytically reduced, i.e. the completion `Â` of $A$ has
no nilpotent elements. Then $B$ is analytically reduced, and a fortiori reduced.

Indeed, $\hat{B}$ is finite and étale over `Â`, and one applies I.9.3.

**Theorem.**

<!-- label: I.9.5 -->

Let $f: A \to B$ be a local homomorphism, with $B$ isomorphic to a localized algebra of an $A$-algebra of finite type.
Then:

1. If $f$ is étale, $A$ is normal if and only if $B$ is normal.
1. If $A$ is normal, $f$ is étale if and only if $f$ is injective and net; then $B$ is normal by (i).

We shall give two different proofs of (i). The first uses some properties of quasi-finite flat morphisms, recalled at
the beginning of this number, without using I.7.6, and hence without using the Main Theorem; for the second proof the
reverse is true. Finally, for (ii), it seems that one needs the Main Theorem in any case.

### First Proof

We use the following necessary and sufficient condition for normality of a noetherian local ring $A$ of nonzero
dimension.

<!-- original page 18 -->

**Serre's Criterion.** (i) For every prime ideal $\mathfrak{p}$ of $A$ of rank 1, $A_{\mathfrak{p}}$ is normal, or
equivalently regular. (ii) For every prime ideal $\mathfrak{p}$ of $A$ of rank $\geq 2$, $depth A_{\mathfrak{p}} \geq
2$.[^I-9-1]

We shall admit this criterion here; it is supposed to appear in the paragraph on flat morphisms. Its principal advantage
is that it does not suppose a priori that $A$ is reduced, nor a fortiori integral. Here, we may already suppose $\dim A
= \dim B \neq 0$.

By the reminders at the beginning of this number, the prime ideals $\mathfrak{p}$ of $A$ of rank 1, respectively of rank
$\geq 2$, are exactly the traces on $A$ of the prime ideals $\mathfrak{q}$ of $B$ of rank 1, respectively of rank $\geq
2$. Finally, if $\mathfrak{p}$ and $\mathfrak{q}$ correspond, $B_{\mathfrak{q}}$ is étale over $A_{\mathfrak{p}}$, hence
has the same depth as $A_{\mathfrak{p}}$, and is regular if and only if $A_{\mathfrak{p}}$ is regular, by I.9.1.
Applying Serre's criterion, one finds that $A$ is normal if and only if $B$ is.

### Second Proof

Suppose $B$ normal, let $L$ be its field of fractions, and $K$ that of $A$; $A$ is integral since $B$ is. We saw in the
proof of I.9.3 that $B \otimes_{A} K$ is a finite product of fields. Since it is contained in $L$, it is a field, and
since it contains $B$, it is $L$. An element of $K$ integral over $A$ is integral over $B$, hence lies in $B$ since $B$
is normal, and therefore lies in $A$ because $B \cap K = A$, as follows from the fact that $B$ is faithfully flat over
$A$.

Now suppose $A$ normal, and prove that $B$ is normal. By I.7.6 one has $B = B'_{\mathfrak{n}}$, where $B' = A[t]/FA[t]$,
with $F$ and $\mathfrak{n}$ as in I.7.6. Thus $L = B \otimes_{A} K$ will be a localization of $B' \otimes_{A} K =
K[t]/FK[t]$, and a product of fields, finite separable extensions of $K$. This latter product, as happens whenever one
localizes an artinian ring, here $B'_{K}$ with respect to a multiplicatively stable set, is a direct factor of $B'_{K}$,
hence corresponds to a decomposition $F = F_{1}F_{2}$ in `K[t]`, with the generator of $L$ corresponding to $t$ already
annihilated by $F_{1}$.

But since $A$ is normal, the $F_{i}$ lie in `A[t]`, assuming them monic. Observing that $B \to L = B \otimes_{A} K$ is
injective, since $A \to K$ is injective and $B$ is flat over $A$, it follows that one already has $F_{1}(u) = 0$, with
$u$ the class of $t$ in $L$. If $F$ has been chosen of minimal degree, it follows that $F_{2} = 1$. Note that $F'(u) =
F'_{1}(u)F_{2}(u) + F_{1}(u)F'_{2}(u) = F'_{1}(u)F_{2}(u)$, since $F_{1}(u) = 0$; hence $F'_{1}(u) \neq 0$ since $F'(u)
\neq 0$.

<!-- original page 19 -->

Thus one has

```text
(*)  L = B ⊗_A K = K[t]/FK[t],
```

and $F$ is consequently a separable polynomial in `K[t]`, though evidently not necessarily in `A[t]`. Note that for the
moment, one has only shown, essentially, that in I.7.6 one can choose $F$ and $\mathfrak{n}$ in such a way that, with
the notation used here, $B' \to B'_{\mathfrak{n}} = B$ is injective. We used the normality of $A$ for this; I do not
know whether it remains true without the normality hypothesis.

Recall now the well-known lemma, extracted from Serre's course of last year.

**Lemma.**

<!-- label: I.9.6 -->

Let $K$ be a ring, $F \in K[t]$ a monic separable polynomial, $L = K[t]/FK[t]$, and $u$ the class of $t$ in $L$, so that
$F'(u)$ is an invertible element of $L$. Then one has the following formulas, where $n = deg F$:

```text
tr_{L/K}(uⁱ/F′(u)) = 0    if 0 ≤ i < n − 1,
tr_{L/K}(uⁿ⁻¹/F′(u)) = 1.
```

**Corollary.**

<!-- label: I.9.7 -->

The determinant of the matrix

$$ (u^{j} \cdot u^{i}/F'(u))_{0\leq i,j\leq n-1} $$

is equal to $(-1)^{n(n-1)}/^{2}$, hence is invertible in every subring $A$ of $K$.

**Corollary.**

<!-- label: I.9.8 -->

Let $A$ be a subring of $K$, let $V$ be the $A$-module generated by the $u^{i}$, $0 \leq i \leq n - 1$, in $L$, and let
$V'$ be the sub-$A$-module of $L$ formed by the $x \in L$ such that $tr_{L/K}(xy) \in A$ for every $y \in V$, i.e. for
$y$ of the form $u^{i}$, $0 \leq i \leq n - 1$. Then $V'$ is the $A$-module having as basis the $u^{i}/F'(u)$, $0 \leq i
\leq n - 1$.

**Corollary.**

<!-- label: I.9.9 -->

Suppose $K$ is the field of fractions of a normal integral ring $A$, and that $F$ has its coefficients in $A$. Then,
with the notation of I.9.8, $V'$ contains the normal closure $A'$ of $A$ in $L$, which is therefore contained in
$A[u]/F'(u)$, and a fortiori in $A[u][F'(u)^{-1}]$.

Apply this last corollary to the situation obtained in the proof: since $F'(u)$ is invertible in $B$, which contains
`A[u]`, $B$ contains $A'$. By the Main Theorem, or from the fact that $B = A[u]_{\mathfrak{n}}$, $B$ is a localized
algebra of $A'$. Since $A'$ is normal, so is $B$.

### Proof of (ii)

<!-- original page 20 -->

Proceed as in the preceding proof to show that in I.7.6 one can choose $F$ in such a way that `(*)` still holds. The
only a priori obstacle is that, $B$ no longer being assumed flat over $A$, one can no longer assert that $B \to L$ is
injective, so the reasoning applies a priori only to the image $B_{1}$ of $B$ under that homomorphism. It follows at
once that $B_{1}$ is flat over $A$, as a localization of a free algebra over $A$. By I.4.8 the morphism $B \to B_{1}$ is
étale, hence an isomorphism, which completes the proof.

From the editorial point of view, the last two proofs should be interchanged, and the formal computations of the lemma
and its corollaries should be put in a separate number.

**Corollary.**

<!-- label: I.9.10 -->

Let $f: X \to Y$ be an étale morphism. If $Y$ is normal, then $X$ is normal; the converse is true if $f$ is surjective.

**Corollary.**

<!-- label: I.9.11 -->

Let $f: X \to Y$ be a dominant morphism, with $Y$ normal and $X$ connected. If $f$ is net, then $f$ is étale; hence $X$
is normal and therefore, being connected, irreducible.

Let $U$ be the set of points where $f$ is étale. It is open, and it suffices to show that it is also closed and
nonempty. The set $U$ contains the inverse image of the generic point of $Y$, since for an algebra over a field,
unramified equals étale; hence, since $X$ dominates $Y$, $U$ is nonempty. If $x$ belongs to the closure of $U$, then it
belongs to the closure of an irreducible component $U_{i}$ of $U$, hence to an irreducible component $X_{i} :=
closure(U_{i})$ of $X$ that meets $U$, and therefore dominates $Y$, since every component of $U$, being flat over $Y$,
dominates $Y$. Consequently, if $y$ is the projection of $x$ to $Y$, $\mathcal{O}_{y} \to \mathcal{O}_{x}$ is injective,
taking into account that $\mathcal{O}_{y}$ is integral. Since $\mathcal{O}_{y}$ is normal and $\mathcal{O}_{y} \to
\mathcal{O}_{x}$ is net, one concludes using I.9.5(ii).

**Corollary.**

<!-- label: I.9.12 -->

Let $f: X \to Y$ be a dominant morphism of finite type, with $Y$ normal and $X$ irreducible. Then the set of points
where $f$ is étale is identical with the complement of the support of $\Omega^{1}_{X/Y}$, i.e. with the complement of
the subprescheme of $X$ defined by the different ideal $\mathfrak{d}_{X/Y}$.

<!-- original page 21 -->

This is the "less trivial" statement alluded to in the remark in no. I.4.

**Remark.** One should be careful not to believe that a connected étale covering of an irreducible scheme is itself
irreducible, when the base is not assumed normal. This question will be studied in no. I.11.

## 10. Étale Coverings of a Normal Scheme

<!-- label: I.10 -->

**Proposition.**

<!-- label: I.10.1 -->

Let $X$ be a prescheme étale and separated over a connected normal $Y$ with field $K$. Then the connected components
$X_{i}$ of $X$ are integral, their fields $K_{i}$ are finite separable extensions of $K$, and $X_{i}$ identifies with a
nonempty open part of the normalization of $Y$ in $K_{i}$; hence $X$ identifies with a dense open part of the
normalization of $Y$ in $R(X) = L = \prod K_{i}$.

By I.9.10, $X$ is normal; a fortiori its local rings are integral, so the connected components of $X$ are irreducible.
Since $X_{i}$ is normal, and finite and dominant over $Y$, it follows from a special case, almost trivial moreover, of
the Main Theorem that $X_{i}$ is an open subset of the normalization of $Y$ in the field $K_{i}$ of $X$.

**Corollary.**

<!-- label: I.10.2 -->

Under the conditions of I.10.1, $X$ is finite over $Y$, i.e. an étale covering of $Y$, if and only if $X$ is isomorphic
to the normalization $Y'$ of $Y$ in $L = R(X)$, the ring of rational functions on $X$.

Indeed, one knows that this normalization is finite over $Y$, since $Y$ is normal and $R/K$ is separable. Conversely, if
$X$ is finite over $Y$, it is finite over $Y'$, so its image in $Y'$ is closed; on the other hand it is dense.

An algebra $L$ of finite rank over $K$ will be said to be unramified over $X$, or simply unramified over $K$ if $X$ is
understood, if $L$ is a separable algebra over $K$, i.e. a direct product of separable extensions $K_{i}$, and if the
normalization $Y'$ of $Y$ in $L$, the disjoint sum of the normalizations of $Y$ in the $K_{i}$, is unramified, hence
étale by I.9.11, over $Y$. Thus:

**Corollary.**

<!-- label: I.10.3 -->

For every $X$ finite over $Y$ and such that every irreducible component dominates $Y$, let $R(X)$ be the ring of
rational functions on $X$, the product of the local rings of the generic points of the irreducible components of $X$.

<!-- original page 22 -->

Thus $X \mapsto R(X)$ is a functor, with values in algebras of finite rank over $K = R(Y)$. This functor establishes an
equivalence from the category of connected étale coverings of $Y$ to the category of extensions $L$ of $K$ unramified
over $Y$.

The inverse functor is the normalization functor.

Suppose $Y$ affine, hence defined by a normal ring $A$ with field of fractions $K$. Let $L$ be a finite extension of $K$
that is a direct product of fields. Then, by definition, the normalization $Y'$ of $Y$ in $L$ is isomorphic to
$\operatorname{Spec}(A')$, where $A'$ is the normalization of $A$ in $L$. Saying that $L$ is unramified over $Y$ means
that $A'$ is unramified, or equivalently étale, over $A$. If $A$ is local, this is equivalent to saying that the local
rings $A'_{\mathfrak{n}}$, where $\mathfrak{n}$ runs through the finite set of maximal ideals of $A'$, i.e. of its prime
ideals inducing the maximal ideal $\mathfrak{m}$ of $A$, are unramified, hence étale, over the local ring $A$.

Finally, note also that the discriminant criterion I.4.10 can also be applied in this situation. More generally, a
variant of that criterion should be stated as follows, without a preliminary flatness condition when $X$ dominates $Y$,
though $Y$ is still assumed locally integral: $A \to B$ and $B \to B \otimes_{A} K = L$ are injective, so $tr_{L/K}$ is
defined, and $tr_{L/K}(xy)$ induces a fundamental bilinear form $B \times B \to A$, i.e. there exist $x_{i} \in B$, $1
\leq i \leq n$, with $n$ the rank of $L$ over $K$, such that `tr(x_ix_j) ∈ A` for all `i, j`, and `det(tr(x_ix_j))` is
invertible in $A$.

The sorites I.4.6 immediately imply the sorites of unramifiedness in the classical setting.

**Proposition.**

<!-- label: I.10.4 -->

Let $Y$ be a normal integral prescheme, with field $K$.

1. $K$ is unramified over $Y$.
1. If $L$ is an extension of $K$ unramified over $Y$, if $Y'$ is a normal prescheme with field $L$ and dominating $Y$,
   for example the normalization of $Y$ in $L$, and if $M$ is an extension of $L$ unramified over $Y'$, then $M/K$ is
   unramified over $Y$. This is the transitivity of unramifiedness.
1. Let $Y'$ be a normal integral prescheme dominating $Y$, with field $K'/K$. If $L$ is an extension of $K$ unramified
   over $Y$, then $L \otimes_{K} K'$ is an extension of $K'$ unramified over $Y'$. This is the translation property.

<!-- original page 23 -->

Moreover:

**Corollary.**

<!-- label: I.10.5 -->

Under the conditions of (iii), if $Y = \operatorname{Spec}(A)$ and $Y' = \operatorname{Spec}(A')$, then the
normalization $\bar{A}'$ of $Y'$ in $L' = L \otimes_{K} K'$ identifies with $\bar{A} \otimes_{A} A'$, where `Ā` is the
normalization of $A$ in $L$.

Usually, people, who are reluctant to consider nonintegral rings, even when they are direct products of fields, state
the translation property in the following weaker form:

**Corollary.**

<!-- label: I.10.6 -->

Under the conditions of (iii), let $L_{1}$ be a compositum of $L/K$, unramified over $Y$, and $K'/K$. Then $L_{1}/K'$ is
unramified over $Y'$. In the case where $Y = \operatorname{Spec}(A)$, $Y' = \operatorname{Spec}(A')$, one furthermore
has

$$ \bar{A}' = A[\bar{A}, A'], $$

i.e. the normalized ring $\bar{A}'$ of $A'$ in $L_{1}$ is the $A$-algebra generated by $A'$ and the normalization `Ā` of
$A$ in $L$.

This last fact is false without the unramifiedness hypothesis, even in the case of composita of number fields.

To finish this number, we shall give the interpretation of the notion of étale covering corresponding to the intuitive
image of that notion: there should be the "maximum number" of points over the point under consideration $y \in Y$, and
in particular there should not be "several points merged together" over $y$. To prove the results in this direction with
all desirable generality, we shall admit here Proposition I.10.7 below, whose proof will be in the multiplodocus,
Chapter IV, paragraph 15, and uses Chevalley's technique of constructible sets and a little descent theory.

A morphism of finite type $f: X \to Y$ is said to be universally open if for every base extension $Y' \to Y$, with $Y'$
locally noetherian, the morphism $f': X' = X \times_{Y} Y' \to Y'$ is open, i.e. sends open sets to open sets. One may
moreover restrict to the case where $Y'$ is of finite type over $Y$, and even where $Y'$ is of the form
$Y[t_{1},...,t_{r}]$, with the $t_{i}$ indeterminates.

A universally open morphism is a fortiori open, the converse being false. On the other hand, if $f$ is open, with $X$
and $Y$ irreducible, then all components of all fibers of $f$ have the same dimension, namely the dimension of the
generic fiber

<!-- original page 24 -->

$f^{-1}(z)$, where $z$ is the generic point of $Y$. Finally, if $Y$ is normal, this latter condition already implies
that $f$ is universally open, by Chevalley's theorem. It follows, for example, that if $f: X \to Y$ is a quasi-finite
morphism, with $Y$ normal and irreducible, then $f$ is universally open, or simply open, if and only if every
irreducible component of $X$ dominates $Y$. Recall also that a flat morphism of finite type, being open, is also
universally open. With these preliminaries in place, "recall":

**Proposition.**

<!-- label: I.10.7 -->

Let $f: X \to Y$ be a quasi-finite, separated, universally open morphism. For every $y \in Y$, let $n(y)$ be the
"geometric number of points of the fiber $f^{-1}(y)$", equal to the sum of the separable degrees of the residue
extensions $\kappa(x)/\kappa(y)$, for $x \in f^{-1}(y)$. Then the function $y \mapsto n(y)$ on $Y$ is upper
semicontinuous. For it to be constant in a neighborhood of the point $y$, i.e. for $n(y) = n(z_{i})$, where the $z_{i}$
are the generic points of the irreducible components of $Y$ containing $y$, it is necessary that there exist a
neighborhood $U$ of $y$ such that $X|U$ is finite over $U$.[^I-10-1]

**Corollary.**

<!-- label: I.10.8 -->

If $y \mapsto n(y)$ is constant and $Y$ is geometrically unibranch,[^I-10-2] then the irreducible components of $X$ are
disjoint.

**Proposition.**

<!-- label: I.10.9 -->

Let $f: X \to Y$ be an étale separated morphism. With the notation of I.10.7, the function $y \mapsto n(y)$ is upper
semicontinuous. For it to be constant in a neighborhood of the point $y$, i.e. for $n(y) = n(z_{i})$, where the $z_{i}$
are the generic points of the irreducible components of $Y$ containing $y$, it is necessary and sufficient that there
exist an open neighborhood $U$ of $y$ such that $X|U$ is finite over $U$, i.e. is an étale covering of $U$.

**Corollary.**

<!-- label: I.10.10 -->

For an étale separated morphism $f: X \to Y$, with $Y$ connected, to be finite, i.e. to make $X$ an étale covering of
$Y$, it is necessary and sufficient that all fibers of $f$ have the same geometric number of points.

In I.10.7 and its corollary, there was no normality hypothesis on $Y$. If one makes such a hypothesis, one finds the
stronger statement, most often taken as the definition of unramifiedness of a covering:

**Theorem.**

<!-- label: I.10.11 -->

<!-- original page 25 -->

Let $f: X \to Y$ be a quasi-finite separated morphism. Suppose that $Y$ is irreducible, that every component of $X$
dominates $Y$, and that $X$ is reduced, i.e. that $\mathcal{O}_{X}$ has no nilpotent elements. Let $n$ be the degree of
$X$ over $Y$, the sum of the degrees over the field $K$ of $Y$ of the fields $K_{i}$ of the irreducible components
$X_{i}$ of $X$. Let $y$ be a normal point of $Y$. Then the geometric number $n(y)$ of points of $X$ over $y$ is $\leq
n$, and equality holds if and only if there exists an open neighborhood $U$ of $y$ such that $X|U$ is an étale covering
of $U$.

The "only if" being trivial, let us prove the "if". Let $z$ be the generic point of $Y$. We have $n(z) =$ the sum of the
separable degrees of the $K_{i}/K$, hence $n(z) \leq n$; and by I.10.7 one has $n(y) \leq n(z) \leq n$, with equality
implying that $X|U$ is finite over $U$ for a suitable neighborhood $U$ of $y$. One may therefore suppose $X$ finite over
$Y$ and the function $n(y')$ on $Y$ constant. Finally, by I.10.8, $X$ is then the disjoint union of its irreducible
components, and to prove that it is unramified at $y$, one is reduced to the case where $X$ is irreducible, hence
integral. Finally, one may suppose $Y = \operatorname{Spec}(\mathcal{O}_{y})$. The theorem is then reduced to the
following classical statement:

**Corollary.**

<!-- label: I.10.12 -->

Let $A$ be a normal local ring, noetherian as always, with field $K$; let $L$ be a finite extension of $K$ of degree
$n$, with separable degree $n_{s}$; let $B$ be a subring of $L$ finite over $A$, with field of fractions $L$; let
$\mathfrak{m}$ be the maximal ideal of $A$, and let $n'$ be the separable degree of $B/\mathfrak{m}B$ over
$A/\mathfrak{m}A = k$, i.e. the sum of the separable degrees of the residue extensions of this ring. One has $n' \leq
n_{s}$ and a fortiori $n' \leq n$. This last inequality is an equality if and only if $B$ is unramified, hence étale,
over $A$.

It remains only to show that $n' = n$ implies that $B$ is étale over $A$. Recall the proof when $k$ is infinite: one
need only show that $R = B/\mathfrak{m}B$ is separable over $k$. If this were not the case, it would follow, by a known
lemma, that there exists an element $a$ of $R$ whose minimal polynomial over $k$ has degree $> n'$. This element comes
from an element $x$ of $B$, whose minimal polynomial over $K$, as an element of $L$, has degree $\leq n$. On the other
hand, this latter polynomial has its coefficients in $A$ since $A$ is normal, and therefore gives by reduction mod
$\mathfrak{m}$ a monic polynomial $F \in k[t]$, of degree $\leq n = n'$, such that $F(a) = 0$, a contradiction.

<!-- original page 26 -->

In the general case, where $k$ may be finite, returning to geometric language, consider $Y' =
\operatorname{Spec}(A[t])$, which is faithfully flat over $Y$, and the generic point $y'$ of the fiber
$\operatorname{Spec}(k[t])$ of $Y'$ over $y$. Then $X$ is net over $Y$ at $y$ if and only if $X' = X \times_{Y} Y' =
\operatorname{Spec}(B[t])$ is net at $y'$ over $Y'$, as one checks immediately. On the other hand, by the choice of
$y'$, its residue field is $k(t)$, hence infinite. Since $y'$ is a normal point of $Y'$, one is reduced to the preceding
case.

## 11. Some Complements

<!-- label: I.11 -->

We have already said that a connected étale covering of an integral scheme is not necessarily integral. Here are two
examples of this fact.

**a)** Let $C$ be an algebraic curve with an ordinary double point $x$, let $C'$ be its normalization, and let $a$ and
$b$ be the two points of $C'$ above $x$. Let $C'_{i}$, for $i = 1, 2$, be two copies of $C'$, and let $a_{i}$ and
$b_{i}$ be the points of $C'_{i}$ corresponding to $a$ and $b$ respectively. In the sum curve $C'_{1} \amalg C'_{2}$,
identify $a_{1}$ with $b_{2}$ on the one hand, and $a_{2}$ with $b_{1}$ on the other. We leave to the reader the task of
making this identification process precise; it will be explained in Chapter VI of the multiplodocus, but in the case of
curves over an algebraically closed field it is treated in Serre's book on algebraic curves.

One obtains a connected and reducible curve $C''$, which is an étale covering of degree 2 of $C$. The reader will verify
that, in general, the connected "Galois" étale coverings $C''$ of $C$ whose inverse image $C'' \times_{C} C'$ is a
trivial covering of $C'$, i.e. isomorphic to the sum of a certain number of copies of $C'$, are "cyclic" of degree $n$;
and for every integer $n > 0$, one can construct a connected cyclic étale covering of degree $n$. In the language of the
fundamental group to be developed later, this means that the quotient of $\pi_{1}(C)$ by the closed normal subgroup
generated by the image of $\pi_{1}(C') \to \pi_{1}(C)$, the homomorphism induced by the projection, is isomorphic to the
profinite completion of $\mathbb{Z}$. More precisely, one should be able to show that the fundamental group of $C$ is
isomorphic to the topological free product of the fundamental group of $C'$ with the profinite completion of
$\mathbb{Z}$. Note that questions of this kind gave rise to descent theory for schemes.

**b)** Let $A$ be a complete integral local ring. One knows that its normalization $A'$ is finite over $A$, by Nagata;
hence it is a complete semilocal ring, and therefore local since it is integral. Suppose that the residue extension
$L/k$ it defines is not radicial. Otherwise, one will say that $A$ is geometrically unibranch; cf. below. This will be
the case, for example, for the ring

$$ \mathbb{R}[[s,t]]/(s^{2}+t^{2})\mathbb{R}[[s,t]], $$

where $\mathbb{R}$ is the field of real numbers.

Let $k'$ be a finite Galois extension of $k$ such that $L \otimes_{k} k'$ decomposes, and let $B$ be a finite étale
algebra over $A$ corresponding to the residue extension $k'$; recall that $B$ is essentially unique. Then $B' = A'
\otimes_{A} B$ over $B$ has residue algebra $L \otimes_{k} k'$, which is not local; hence $B'$ is not a local ring, and
therefore, being complete, has zero divisors.

<!-- original page 27 -->

Since $B'$ is contained in the total ring of fractions of $B$, because it is free over $A'$, hence torsion-free over
$A'$, hence torsion-free over $A$, and therefore contained in

```text
B′ ⊗_A K = B′_(K) = A′_(K) ⊗_K B_(K) = B_(K),
```

since $A'_{K} = K$, it follows that $B$ is not integral. In the case of the ring
$\mathbb{R}[[s,t]]/(s^{2}+t^{2})\mathbb{R}[[s,t]]$, taking $k'/k = \mathbb{C}/\mathbb{R}$, one obtains for $B$ the local
ring of two intersecting lines in the plane at their point of intersection.

Note moreover that if there exists a connected étale covering $X$ of an integral $Y$ that is not irreducible, then every
irreducible component of $X$ gives an example of an unramified covering $X'$ of $Y$, dominating $Y$, that is not étale
over $Y$. In the case of example a), one obtains in this way that $C'$ is unramified over $C$ without being étale at the
two points $a$ and $b$. This is also seen directly by inspecting the completions of the local rings of $x$ and $a$: from
the "formal" point of view, $C'$ at the point $a$ identifies with a closed subscheme of $C$ at the point $x$, namely one
of the two "branches" of $C$ passing through $x$.

In a) and b), one sees that the failure of the conclusions of I.9.5(i) and (ii) is directly linked to the fact that a
point of $Y$ "bursts" into distinct points of the normalization. In b), the fact that the residue extension is not
radicial must be interpreted geometrically in this way.

More precisely, we shall say that an integral local ring $A$ is geometrically unibranch if its normalization has only
one maximal ideal, the corresponding residue extension being radicial. A point $y$ of an integral prescheme is said to
be geometrically unibranch if its local ring is. Examples: a normal point, an ordinary cusp of a curve, etc.

<!-- original page 28 -->

It seems that if $Y$ has a point that is not unibranch, there always exists a connected nonirreducible étale covering of
$Y$; at least this is what we showed in case b), when $Y$ is the spectrum of a complete local ring. By contrast, one can
show that if all points of $Y$ are geometrically unibranch, then every connected unramified $Y$-prescheme dominating $Y$
is étale and irreducible. The proof repeats that of I.9.5, using the following generalization of Theorem I.8.3, which
will be proved later using descent theory:[^I-11-1]

Let $Y' \to Y$ be a finite, radicial, surjective morphism, i.e. what one might call a "universal homeomorphism".
Consider the functor $X \mapsto X \times_{Y} Y' = X'$ from $Y$-preschemes to $Y'$-preschemes. This functor induces an
equivalence from the category of étale $Y$-schemes to the category of étale $Y'$-schemes.

One may apply this result, for example, in the case where $Y'$ is the normalization of $Y$, with $Y$ assumed unibranch
and $Y'$ finite over $Y$, which is true in all cases one encounters in practice; or in the case of a $Y''$ "sandwiched"
between $Y$ and its normalization, which no longer needs to be finite over $Y$.

<!-- end of Exposé I source block: next chapter begins at smf_doc-math_3_01.tex line 2519 -->

[^I-1-1]: Cf. EGA IV 16.3.

[^I-2-1]: In EGA II 6.2.3 one assumes in addition that $f$ is of finite type.

[^I-3-1]: Cf. remorse in III 1.2.

[^I-4-1]: Cf. Exposé IV.

[^I-4-2]: Cf. remorse in III 1.2.

[^I-5-1]: Cf. IV 5.9.

[^I-9-1]: Cf. EGA IV 5.8.6.

[^I-10-1]: Cf. EGA IV 15.5.1.

[^I-10-2]: For the definition, cf. below no. I.11.

[^I-11-1]: Cf. IX 4.10. For a more direct proof, cf. EGA IV 18.10.3, using a variant of I.9.5 for geometrically
    unibranch local rings.
