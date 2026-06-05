# Exposé XI. Examples and Complements

<!-- label: XI -->

<!-- original page 285 -->

## 1. Projective Spaces, Unirational Varieties

<!-- label: XI.1 -->

**Proposition.**

<!-- label: XI.1.1 -->

Let $k$ be an algebraically closed field, and let $X = \mathbb{P}^{r}_{k}$ be projective space of dimension $r$ over
$k$. Then $X$ is **simply connected**, that is, $\pi_{1}(X) = 0$.

For $r = 0$ this is trivial. If $r = 1$, one must show that if $X'$ is a nonempty connected étale covering of $X =
\mathbb{P}^{1}_{k}$, then $X' \simeq X$. The genus formula gives, if $g$ and $g'$ are the genera of $X$ and $X'$,

$$ 1 - g' = d(1 - g), $$

where $d$ is the degree of $X'$ over $X$. Since $g = 0$, we have $1 - g' = d$, which forces $d = 1$ because $g' \geq 0$;
this proves $X' \simeq X$.

When $r \geq 2$, one proceeds by induction on $r$, assuming ${\mathbb{P}^{r}}'$ simply connected for $r' < r$. Applying
this to a hyperplane of $\mathbb{P}^{r}$ and using X.2.10, it follows that $\mathbb{P}^{r}$ is simply connected. Another
proof: by X.1.7 one has

```text
π₁(ℙ¹ × ⋯ × ℙ¹) = π₁(ℙ¹) × ⋯ × π₁(ℙ¹),
```

so $(\mathbb{P}^{1})^{r}$ is simply connected because $\mathbb{P}^{1}$ is. Hence $\mathbb{P}^{r}$ is simply connected by
birational invariance of the fundamental group (X.3.4). This proof shows more generally:

**Corollary.**

<!-- label: XI.1.2 -->

Let $X$ be a proper normal scheme over an algebraically closed field $k$. If $X$ is a rational variety, that is,
integral and with function field a purely transcendental extension of $k$, then $X$ is simply connected.

This result applies in particular to Grassmann varieties and, more generally,

<!-- original page 286 -->

to varieties $G/H$, where $G$ is a connected linear group over $k$ and $H$ is an algebraic subgroup containing a Borel
subgroup of $G$.

Recall that a variety **unirational over $k$** means a proper integral scheme over $k$ whose function field $K$ is
contained in a purely transcendental extension $K'$ of $k$, finite over $K$ (that is, with the same transcendence degree
over $k$ as $K$), or equivalently, for which there exists a dominant rational map $f: \mathbb{P}^{r}_{k} \to X$ with $r
= \dim X$. If $X$ is normal, the reflections preceding X.3.4 show that for every connected étale covering $X'$ of $X$,
with function field $L/K$, the $K'$-algebra $L \otimes_{K} K'$ is unramified over the model $\mathbb{P}^{r}$, hence
completely decomposed by XI.1.1. This shows that $L$ is $K$-isomorphic to a subextension of $K'/K$. Taking V.8.2 into
account, this proves:

**Corollary.**

<!-- label: XI.1.3 -->

The fundamental group of a normal unirational variety over an algebraically closed field is finite.

Notice that in the definition of “unirational,” one did not need $K'/K$ to be finite.

**Remarks.**

<!-- label: XI.1.4 -->

The results of this number are, of course, well known. Moreover, J.-P. Serre showed [XI.10] that when $X$ is a smooth
projective unirational variety over an algebraically closed field of **characteristic zero**, $X$ is simply connected.
His proof is transcendental, using Hodge symmetry.

[M. Raynaud, added in 2003.] Restrict to the case of an algebraically closed field $k$ of characteristic $p \geq 0$. In
characteristic $p > 0$, the definition of a unirational $k$-variety given above is that of a weakly unirational
$k$-variety, as opposed to a strongly unirational $k$-variety, where one also assumes that $K'$ is a separable extension
of $K$.

In dimension 2, there exist smooth projective weakly unirational surfaces with nontrivial fundamental group (finite by
XI.1.3), and hence nonrational surfaces; see T. Shioda, “On unirationality of supersingular surfaces,” _Mathematische
Annalen_ **225** (1977), pp. 155–159. By contrast, a strongly unirational surface is rational: this follows from
Castelnuovo’s rationality criterion, extended to characteristic $p > 0$ by O. Zariski; cf. J.-P. Serre, Séminaire
Bourbaki no. 146, 1957, and _Œuvres/Collected Papers_, vol. 1, p. 467.

Over the field $\mathbb{C}$ of complex numbers, examples are known of smooth projective varieties of dimension $\geq 3$
that are unirational and nonrational; cf. P. Deligne, “Variétés unirationnelles non rationnelles (d’après M. Artin et D.
Mumford),” Séminaire Bourbaki no. 402, 1971-72, Lecture Notes vol. 317. A smooth cubic hypersurface in projective
4-space is one such example. Some of these examples extend to characteristic `> 0` to give strongly unirational
nonrational varieties; cf. J.-P. Murre, “Reduction of the proof of the non-rationality of a non singular cubic threefold
to a result of Mumford,” _Compositio Mathematica_ **27** (1973), pp. 63–82.

Let $V$ be a normal integral projective $k$-variety. One says that $V$ is rationally connected if there exist an
integral finite-type $k$-scheme $T$ and a $k$-morphism $F: T \times \mathbb{P}^{1} \to V$ such that the morphism

```text
T × ℙ¹ × ℙ¹ → V × V,
(t,u,u′) ↦ (F(t,u), F(t,u′))
```

is dominant. In particular, through two sufficiently general rational points of $V$ there passes a rational curve. The
terminology is justified by the fact that if $V$ is rationally connected, two rational points can be joined by a finite
chain of rational curves. If $k$ has characteristic $p > 0$, one strengthens the preceding definition by requiring that
the displayed map be generically smooth. This gives the notion of separably rationally connected variety. Thus
unirational varieties are rationally connected, and in characteristic $p > 0$ strongly unirational varieties are
separably rationally connected. J. Kollár showed that separably rationally connected varieties have trivial algebraic
fundamental group; cf. O. Debarre, “Variétés rationnellement connexes (d’après T. Graber, J. Harris, J. Starr et A. J.
de Jong),” Séminaire Bourbaki no. 906, 2001-2002.

## 2. Abelian Varieties

<!-- label: XI.2 -->

Let $k$ be an algebraically closed field, let $A$ be an abelian variety over $k$, that is, a group scheme over $k$,
proper, smooth, and connected over $k$, and finally let $G$ be a commutative group scheme of finite type over $k$.
Denote by $Ext(A,G)$ the group of classes of commutative extensions of $A$ by $G$, and by $H^{1}(A,G)$ the group of
classes of principal bundles on $A$ with group $G$ (compare no. XI.4 below). Consider the canonical homomorphism

$$ Ext(A,G) \to H^{1}(A,G). $$

<!-- original page 287 -->

An argument of Serre [XI.5, Chapter VII, Theorem 5] shows that this is an injective homomorphism, whose image is the set
of “primitive elements” of $H^{1}(A,G)$, that is, the elements $\xi$ for which

$$ \pi*(\xi) = pr_{1}*(\xi) + pr_{2}*(\xi), $$

where $pr_{i}$ are the two projections from $A \times A$ to $A$, and $\pi: A \times A \to A$ is the composition law of
$A$. Serre states his theorem only for $G$ linear and connected, and of course smooth over $k$, but by simplifying the
first part of his argument one sees that these restrictions are unnecessary. It is enough to note that every morphism
from $A$ to a group scheme $E$ of finite type over $k$ that sends the identity to the identity is a group homomorphism,
and to apply this to sections over $A$ of an extension $E$ of $A$ by $G$.

We shall apply this result when $G$ is a finite separable group over $k$, that is, an ordinary finite group, assumed
commutative. Using $\pi_{1}(A \times A) \simeq \pi_{1}(A) \times \pi_{1}(A)$ (X.1.7), and interpreting $H^{1}(X,G)$ as
$\operatorname{Hom}(\pi_{1}(X),G)$ for every algebraic scheme $X$, in particular for $X = A$ or $X = A \times A$, one
sees that every class in $H^{1}(A,G)$ is primitive. Thus one has an isomorphism

$$ Ext(A,G) \simeq H^{1}(A,G). $$

In other words, **every principal covering of $A$ with commutative structural group $G$, pointed above the origin of
$A$, is endowed in a unique way with a structure of algebraic group having the marked point as origin, and such that $A'
\to A$ is a homomorphism of algebraic groups.** In particular, if $A'$ is connected, it is also an abelian variety,
isogenous to $A$.

On the other hand, since the functor $X \mapsto \pi_{1}(X)$ from pointed algebraic schemes $X$ to groups commutes with
products (IX.1.7), it sends a group in the first category to a group in the category of groups, that is, to a
**commutative** group. Hence **if $A$ is an abelian variety, $\pi_{1}(A)$**

<!-- original page 288 -->

**is a commutative group.** Thus, to know $\pi_{1}(A)$, it is enough to know the functor

$$ G \mapsto H^{1}(A,G) = \operatorname{Hom}(\pi_{1}(A),G) $$

as $G$ varies through finite **commutative** groups. Finally, recall that for every integer $n > 0$, the
multiplication-by-$n$ homomorphism in $A$,

$$ A --n\to A, $$

is surjective, hence has finite kernel, that is, it is an isogeny; it follows that every isogeny $A' \to A$ is a
quotient of an isogeny of the preceding type. From this, and from standard arguments (cf. for example [XI.6]), one
obtains:

**Theorem (Serre-Lang).**

<!-- label: XI.2.1 -->

Let $A$ be an abelian variety over an algebraically closed field $k$. For every integer $n > 0$, let $K_{n}$ be the
ordinary finite group underlying the kernel ${}_{nA}$ of multiplication by $n$ in $A$, and put, for every prime number
$\ell$,

$$ T_{\ell}(A) = \lim_{r} K^{r}_{\ell} $$

and

```text
T_·(A) = ∏_ℓ T_ℓ(A) = lim_n K_n,
```

where, for $m$ a multiple of $n$, $m = ns$, one sends $K_{m}$ to $K_{n}$ by multiplication by $s$. Then $\pi_{1}(A)$ is
canonically isomorphic to $T_{\cdot}(A)$. Hence for every prime number $\ell$, the $\ell$-primary component of
$\pi_{1}(A)$ is canonically isomorphic to $T_{\ell}(A)$.

Notice that these isomorphisms are functorial in $A$. The module $T_{\ell}(A)$ is called the **$\ell$-adic Tate module**
of the abelian variety $A$. It is an additive functor in $A$; in particular it gives rise to a representation of the
ring $\operatorname{Hom}(A,A)$ of endomorphisms of $A$ in $T_{\ell}(A)$, called the **$\ell$-adic Weil representation**,
which plays an important role in the theory of abelian varieties (cf. for example [XI.4, Chapter VII]). Theorem XI.2.1
gives an interpretation of it in terms of the natural representation in the **$\ell$-adic homology group** of $A$,

$$ H_{1}(A,\mathbb{Z}_{\ell}) = \pi_{1}(A)_{\ell}, $$

<!-- original page 289 -->

which is plainly more satisfactory a priori, especially from the point of view of the Lefschetz formula \[XI.4, Chapter
V\]. Recall Weil’s results on the structure of $T_{\ell}(A)$:

a) If $n$ is prime to $char(k)$, then $K_{n}$ is a free module of rank $2 \dim A$ over $\mathbb{Z}/n\mathbb{Z}$. Hence
if $\ell$ is a prime number different from $char(k)$, $T_{\ell}(A)$ is a free module of rank $2 \dim A$ over the ring
$\mathbb{Z}_{\ell}$ of $\ell$-adic integers.

b) If $n$ is a power of $char(k) = p$, then $K_{n}$ is a free module of rank $\nu \leq \dim A$ over
$\mathbb{Z}/n\mathbb{Z}$, with $\nu$ independent of $n$. Hence $T_{p}(A)$ is a free module of rank $\nu \leq \dim A$
over the ring $\mathbb{Z}_{p}$ of $p$-adic integers.

This shows that in the theory of the fundamental group developed here, the fundamental group of a variable abelian
variety does not vary regularly with the parameter: its $p$-primary component may suddenly drop for values of the
parameter $t$ corresponding to residual characteristic $p$. The best-known case of this phenomenon is that of elliptic
curves.

Notice, however, that for every $n$, whether or not $n$ is prime to the characteristic, the true kernel ${}_{nA}$ in $A$
of multiplication by $n$ is a finite group scheme over $k$ of degree $n^{2g}$, where $g = \dim A$; it is nonseparable
over $k$ if $n$ is a multiple of $p = char(k)$. Moreover, when $A$ varies in a family of abelian varieties, that is,
when one has an abelian scheme $A$ over a base scheme $S$, one shows more generally that ${}_{nA}$ is a finite flat
group scheme over $S$, of degree $n^{2g}$ over $S$. In other words, provided that the infinitesimal parts of the kernels
${}_{nA}$ are taken into account, they behave regularly for every $n$.

This suggests that the “true” fundamental group of an abelian variety $A$ is the pro-algebraic group (formal inverse
limit of finite groups over $k$)

$$ \lim_{n} {}_{nA}, $$

where by the “true fundamental group” of an algebraic scheme $X$ one should mean the pro-group that classifies principal
coverings of $X$ with structural group an arbitrary finite group scheme $G$ over $k$, not necessarily separable over
$k$. In this way, for example, from the representations of $\operatorname{Hom}(A,A)$ in the $p$-primary component of the
true fundamental group of $A$, one recovers the Weil characteristic polynomial defined by the latter using the $\ell
\neq p$, in a more natural way than Serre’s construction [XI.8].

## 3. Projective Cones, Zariski’s Example

<!-- label: XI.3 -->

<!-- original page 290 -->

For simplicity, keep $k$ algebraically closed, and let $V$ be a connected projective $k$-scheme, a closed subscheme of
$\mathbb{P}^{r}_{k}$, which one may assume nonsingular if desired. Let $Y = \hat{C}$ be the projective cone over $V$,
let $y_{0}$ be its vertex, let $X = \hat{C}_{V}$ be the usual projective closure of the vector bundle $C_{V} =
V(\mathcal{O}_{V}(1))$ associated with $\mathcal{O}_{V}(1)$, and finally let

$$ f: X \to Y $$

be the canonical morphism contracting the zero section $X_{0}$ of `C_V` on $X$ to a point (EGA II 8.6.4). Since $X$ is a
locally trivial bundle over $V$ with fibers $\mathbb{P}^{1}$, hence with simply connected fibers, the morphism $p: X \to
V$ induces, by X.1.4, an isomorphism

$$ \pi_{1}(X) \simeq \pi_{1}(V). $$

Since $p$ induces an isomorphism $X_{0} \to V$, it follows that **an étale covering of $X$ is completely decomposed if
and only if its restriction to $X_{0}$ is so**. But for every étale covering $Y'$ of $Y$, the inverse image $X' = X
\times_{Y} Y'$ is an étale covering of $X$ completely decomposed over the fiber $X_{0}$, hence trivial. Since the
homomorphism $\pi_{1}(X) \to \pi_{1}(Y)$ is surjective (IX.3.4), it follows that

$$ \pi_{1}(Y) = (e). $$

In other words, **every projective cone is simply connected.** In characteristic 0, the same result remains true with
$Y$ taken to be the affine cone.

Now suppose $V$ regular, that is, smooth over $k$. Then $X$ is regular, and for a suitable projective embedding of $V$
one obtains a **normal** projective cone $Y$. If $V$ is not simply connected, hence $X$ is not simply connected, let
$X'$ be a nontrivial connected étale covering of $X$. Since the fibers of $X$ over the points $y \in Y$ distinct from
$y_{0}$ are reduced to a point, the restriction of $X'$ to its fibers, in particular to the

<!-- original page 291 -->

generic fiber, is trivial. Nevertheless $X'$ does not come by inverse image from an étale covering of $Y$, since $Y$ is
simply connected and $X'$ would then be completely decomposed. This shows that X.1.3 and X.1.4 become false if the
hypothesis that $f$ is separable is replaced by the weaker hypothesis that its fibers are separable algebraic schemes,
or even smooth schemes, over the $\kappa(s)$. Similarly, the fundamental groups of the geometric fibers $\bar{X}_{y}$
for $y \neq y_{0}$ are plainly reduced to `(e)`, since these fibers are reduced to a point, while $\pi_{1}(X_{0}) \neq
e$; hence the semicontinuity theorem X.2.4 also fails for $f$.

Finally let us indicate the example, pointed out by Zariski, that makes the same theorems fail when the hypothesis that
$f$ is separable is replaced by the hypothesis that $f$ is flat. Let $f: X \to Y$ be a morphism from a nonsingular
projective surface to the rational line $Y = \mathbb{P}^{1}$, such that $K = k(X)$ is a “regular” extension, that is,
primary and separable, of $k(f)$ (equivalently, the geometric generic fiber is connected and separable), and such that
the divisor $(f) = X_{0} - X_{\infty}$ is an $n$-th multiple of a divisor, where $n$ is an integer prime to the
characteristic. Such examples can be constructed in every characteristic.

Let $X'$ be the normalization of $X$ in $K(f^{1/n})$, where $K = k(X)$ is the function field of $X$. The hypothesis on
`(f)` implies that $X'$ is étale over $X$. Let $Y'$ be the normalization of $Y$ in $k(t)(t^{1/n})$; it is ramified over
$Y$ exactly at $t = 0$ and $t = \infty$, and the restriction $X'|f^{-1}(U)$ is isomorphic to the inverse image of $Y'|U$. In
particular, the restriction of $X'$ to the **geometric** generic fiber of $X$ over $Y$ decomposes completely.
Nevertheless $X'$ is not isomorphic to the inverse image of an étale covering of $Y$, since one sees immediately that
the latter would necessarily be $Y'$, which is absurd because $Y'$ is ramified over $Y$. \[Translator note: the source
footnote observes that, from the viewpoint of the étale topology (SGA 4 VII), in this example $R^{1}(f_{et})_{*}(\mathbb{Z}/n\mathbb{Z})$ is
“non-separated” over $S$.\]

Here is a simple way, due to Serre, to realize the conditions of this example, inspired by [XI.5, no. 20]. Take $n$ to
be a prime number $\geq 5$, distinct from the characteristic, and let $G = \mathbb{Z}/n\mathbb{Z}$ act on affine 4-space $k^{4}$ by multiplying
the coordinates by four distinct characters of $G$, which is possible since $n \geq 5$. \[M. Raynaud, added in 2003: $k^{4}$
denotes affine 4-space over $k$.\] Then $G$ acts on projective space $\mathbb{P}^{3}_{k}$, and the only fixed points under $G$ are the
four points corresponding to the coordinate axes. The surface $X'$ with equation

```text
xⁿ + yⁿ + zⁿ + tⁿ = 0
```

is smooth over

<!-- original page 292 -->

$k$ by the Jacobian criterion, and contains none of the fixed points. Since $G$ has prime order, it acts on $X'$
“without fixed points,” that is, $X'$ is a principal covering of $X = X'/G$ with group $G$.

Let $g = x/y$ in $k(X') = K'$. This is a Kummer generator of $K'$ over $K = k(X)$ if the chosen characters were
$\chi^{i}$, $i = 0,1,2,3$, with $\chi$ a primitive character. Let $f$ be its $n$-th power, which is an element of $K$.
One sees at once that $K'$ is a regular extension of $k(g)$. This follows from the fact that the plane curve with
homogeneous equation in `U,T,Z`

$$ T^{n} + Z^{n} + (1 + g^{n})U^{n} = 0 $$

is smooth over $k(g)$, by the Jacobian criterion, and from the fact that every plane curve is connected. On the other
hand, $k(f) = K \cap k(g)$, since the right-hand side is an extension of $k(f)$ contained in the prime-degree extension
$k(g)$, and distinct from $k(g)$ because $g \notin K$. This implies that $K$ is a regular extension of $k(f)$.

Finally, the divisor of $f$ on $X$ is an $n$-th multiple of a divisor, since its inverse image on $X'$ is the divisor of
$g^{n}$, hence an $n$-th multiple, and one can descend because $X'$ is étale over $X$. We would be done if the rational
map $f: X \to \mathbb{P}^{1}$ were a morphism, that is, if the divisors of zeros and poles of $f$ did not meet. In fact,
one verifies easily, again by looking on $X'$, that the two divisors in question are the products by $n$ of two smooth
curves over $k$ meeting transversely at one point $a$. Replacing $X$ by the scheme obtained by blowing up $a$, the
preceding conditions ($div(f)$ divisible by $n$, and $k(X_{1}) = k(X)$ a regular extension of $k(f)$) remain satisfied,
but moreover $f$ is a **morphism** $X_{1} \to \mathbb{P}^{1}$. Thus we are in the desired situation.

## 4. The Cohomology Exact Sequence

<!-- label: XI.4 -->

Let $S$ be a prescheme, so that the category $Sch_{/}S$ of preschemes over $S$ is determined, and hence also the notion of
a group in it; such a group will also be called a **group prescheme over $S$**, or simply an **$S$-group**. To simplify
the exposition and fix ideas, in what follows we shall most often restrict to groups that are **affine** and **flat**
over $S$. \[Translator note: the source footnote says that quasi-affineness instead of affineness would suffice for what
follows; cf. the footnote referred to as note 296 in the source.\] This will be enough for the applications we have in
view. Of course, there are many cases where neither hypothesis is satisfied.

<!-- original page 293 -->

Let $G$ be such an $S$-group, and let $P$ be a prescheme over $S$ on which $G$ acts on the right; in particular this
gives a morphism

```text
π: P ×_S G → P
```

in the category $Sch_{/}S$, satisfying the familiar axioms. We say that $P$ is **formally principal homogeneous under**
$G$ if the morphism

```text
P ×_S G → P ×_S P
```

with components $pr_{1}$ and $\pi$ is an isomorphism. Equivalently, for every object $S'$ of $Sch_{/}S$, the set $P(S')
= \operatorname{Hom}_{S}(S',P)$, regarded as a set with operator group $G(S') = \operatorname{Hom}_{S}(S',G)$, is either
empty or principal homogeneous, that is, empty or isomorphic to $G(S')$ with $G(S')$ acting by right translations.

We say that $P$ is **trivial** if $P$ is isomorphic to $G$, with $G$ acting on itself by right translations, or
equivalently if each of the operator sets $P(S')$ under $G(S')$ is trivial. One verifies, for example by the patented
procedure of passing to the set-theoretic case, that $P$ **is trivial if and only if it is formally principal
homogeneous and admits a section over $S$**. This last fact can be phrased categorically by saying that $P$ has a
section over the final object $e = S$ of $Sch_{/}S$, that is, that there exists a morphism from $e$ to $P$.

To define the notion of a principal homogeneous bundle $P$ under $G$, stronger than that of a formally principal
homogeneous bundle, one must first specify in $Sch_{/}S$ a class of morphisms to be used for “descent,” and which will
play the role of “localization morphisms” for “trivializing” bundles. The most suitable choice varies with context; no
one choice contains all the others. [Translator note: the source refers here to SGA 3 IV, especially §4.] Here it is
convenient to adopt the following definition:

**Definition.**

<!-- label: XI.4.1 -->

Let $G$ be an $S$-group. A **principal homogeneous bundle** (on the right) under $G$ is an $S$-prescheme $P$ with a
right action of the $S$-group $G$, such that there exists a covering of $S$ by open subsets $U_{i}$, and for each $i$ a
faithfully flat and quasi-compact base-change morphism $S'_{i} \to U_{i}$, such that $P' = P \times_{S} S'$ is a trivial
operator prescheme under $G' = G \times_{S} S'$, where $S'$ is the $S$-prescheme that is the disjoint sum of the
$S'_{i}$.

<!-- original page 294 -->

The base-change functor $X \mapsto X' = X \times_{S} S'$, being left exact, sends groups to groups and objects with
operator group to objects with operator group. Notice that XI.4.1 is **stable under base change**. Also:

**Proposition.**

<!-- label: XI.4.2 -->

Let $G$ be an $S$-group, flat and quasi-compact over $S$, and let $P$ be an $S$-prescheme on which $G$ acts on the
right. The following conditions are equivalent:

1. $P$ is a principal homogeneous bundle under $G$.
1. $P$ is formally principal homogeneous under $G$, and the structural morphism $P \to S$ is faithfully flat and
   quasi-compact.

If $P$ is principal homogeneous under $G$, then with the notation of XI.4.1, $P'$ is faithfully flat and quasi-compact
over $S'$, since $G'$ is so and $P'$ is $S'$-isomorphic to it. Hence $P$ has the same properties over $S$ (for
“surjective” and “quasi-compact,” cf. VIII.3.1; for “flat,” this is an omission in the sorites of Exposé VIII).
Conversely, if 2 holds, take the base change $S' = P$, which is indeed faithfully flat and quasi-compact over $S$. Then
$P'$ is formally principal homogeneous over $S'$ because $P$ is so over $S$ and base change is left exact. Moreover $P'$
has a section over $S'$, namely the diagonal section, hence it is a trivial principal bundle. This proves the assertion.

**Corollary.**

<!-- label: XI.4.3 -->

If $G$ is affine and flat over $S$, every principal homogeneous bundle $P$ under $G$ is affine and flat over $S$.

Indeed, it becomes so after a faithfully flat and quasi-compact base extension, and one applies VIII.5.6.

The usefulness of Definition XI.4.1 for $S$-groups **flat** and **affine** over $S$ rests on VIII.2.1, that is, on the
fact that the morphisms $S' \to S$ considered in XI.4.1 are morphisms of effective descent for the category of
preschemes affine over other preschemes. Thanks to this fact, the verification of the facts sketched below is
essentially “categorical.” [Translator note: the source refers again to the footnote cited above.]

Let $E$ be an $S$-prescheme on which the $S$-group $G$ acts on the left, and let $P$ be a principal homogeneous bundle
on the right under $G$. We want to define an associated bundle $E^{P}$, “locally” isomorphic to $E$. To do this, make
$G$ act on the right on $P \times_{S} E$ by the law

$$ (x,y) \mapsto (xg,g^{-1}y), $$

<!-- original page 295 -->

which describes such actions in the set-theoretic context and extends to categories by the patented procedure. We put,
subject to existence,

```text
E^(P) = (P ×_S E)/G.
```

With this convention, $P \times_{S} E$ will be a prescheme over $T = E^{P}$, with right operator group $G_{T} = G
\times_{S} T$; one would like, for comfort, $P \times_{S} E$ to be a principal homogeneous bundle over $T$ with group
`G_T`.

To verify the existence of $E^{P}$ and the preceding property, take the $S'$ from Definition XI.4.1 and look at the
inverse-image situation over $S'$. Since $P'$ is trivial, that is, isomorphic to $G'_{d}$, one sees at once that
$E'^{P'}$ exists and has the desired exactness property. In fact, $E' \times_{S}' P'$ is $G'$-isomorphic to the product
$E' \times_{S}' G'$, and therefore $E'^{P'}$ is isomorphic to $E'$. Moreover, the formation of the “associated bundle”
in the case of a trivial operator space commutes with every base extension. Taking here the various base extensions
`S″ ⇉ S′` and `S‴ ⇉⇉ S′`, where $S''$ and $S'''$ are the double and triple fiber products of $S'$ over $S$, one sees
that $E'^{P'}$ **is endowed with a descent datum relative to $S' \to S$, and $E^{P}$ exists with the required properties
if and only if this descent datum is effective**. Of course $E^{P}$ is then precisely the descended object. Use here the
fact that $S' \to S$ is a descent morphism in the category of $S$-preschemes; cf. VIII.5.2. It follows that **the
associated bundle exists if $E$ is affine over $S$**.

We shall apply this construction in the case where one has a homomorphism of $S$-groups $G \to H$, and where $E$ is the
$S$-prescheme $H$ endowed with the left actions of $G$ on $H$ arising from the given morphism. Since $H$ acts on itself
on the right in a way that commutes with the actions of $G$ on $H$, and since (subject to existence over $S$) the
formation of the associated bundle commutes with base extension, one easily sees that $H$ acts on the right on $P^{H}$.
Thus $P^{H}$ is a principal homogeneous bundle under $H$ in the sense of XI.4.1, and

<!-- original page 296 -->

more precisely it is trivialized by the same morphism $S' \to S$ as $P$. In particular, **to every principal homogeneous
bundle $P$ under $G$ and every homomorphism of $S$-groups $G \to H$, with $H$ affine over $S$, there is associated a
principal homogeneous bundle with group $H$**, functorially in $(G \to H)$, and compatibly with arbitrary base changes
$T \to S$.

**Definition.**

<!-- label: XI.4.4 -->

Let $G$ be an $S$-prescheme. We write $H^{0}(S,G)$ for the set of sections of $G$ over $S$, considered as a group when $G$
is an $S$-group. In that case, we write $H^{1}(S,G)$ for the set of isomorphism classes of principal homogeneous bundles
over $S$ with group $G$, regarding $H^{1}(S,G)$ as endowed with the “marked point” corresponding to the trivial bundles.
\[Translator note: the source footnote says this notation is consistent with the general cohomological notation (SGA 4
V) only when one has effectivity criteria for descent, which are scarcely ensured except when $G$ is affine, or merely
quasi-affine; cf. VIII.7.9.\]

Thus $H^{0}(S,G)$ is a functor in the $S$-prescheme $G$, with values in sets. This functor is left exact, and a fortiori
commutes with finite products; indeed this implies that it sends groups to groups and commutative groups to commutative
groups. Similarly, $H^{1}(S,G)$ is a functor in the **affine** $S$-group $G$, with values in sets, by formation of
associated bundles; one checks easily that this functor commutes with finite products. In particular it sends groups in
the category of affine $S$-groups, that is, **commutative affine** $S$-groups, to groups, and indeed to commutative
groups. Thus, **if $G$ is a commutative affine $S$-group, $H^{1}(S,G)$ is a commutative group**, and a homomorphism $G
\to H$ of commutative affine $S$-groups gives rise to a group homomorphism $H^{1}(S,G) \to H^{1}(S,H)$.

For simplicity, from now on we restrict to **affine and commutative** $S$-groups. Let

$$ 0 \to G' \to G \to G'' \to 0 $$

be a sequence of morphisms of such groups. **We say that this sequence is exact if the composite $G' \to G \to G''$ is
zero** (which allows $G$ to be regarded as a prescheme over $G''$ with right operator group ${G'_{G}}''$)

<!-- original page 297 -->

**and if $G$ is a principal homogeneous bundle over $G''$ with group ${G'_{G}}'' = G' \times_{S} G''$**. This implies in
particular that $u: G' \to G$ is a kernel of $v: G \to G''$, and a fortiori it implies exactness of

$$ 0 \to H^{0}(S,G') \to H^{0}(S,G) \to H^{0}(S,G''). $$

It also makes it possible to define a map

$$ \partial: H^{0}(S,G'') \to H^{1}(S,G'), $$

by associating to every section of $G''$ over $S$, that is, to every $S$-morphism $f: S \to G''$, the principal
homogeneous bundle $P_{f}$ with group $G' \simeq f*({G'_{G}}'')$ over $S$, inverse image of the principal homogeneous
bundle $G$ over $G''$. From the viewpoint of $S$-preschemes, this is simply the inverse image by $v: G \to G''$ of the
subprescheme image of $S$ by the immersion $f$; the operations of $G'$ on $P_{f}$ are induced by the right operations of
$G'$ on $G$.

We also leave to the reader the verification of the following proposition, which presents no difficulties other than
those of writing it out:

**Proposition.**

<!-- label: XI.4.5 -->

The map $\partial: H^{0}(S,G'') \to H^{1}(S,G')$ is a group homomorphism. The following sequence of homomorphisms is
exact:

```text
0 → H⁰(S,G′) → H⁰(S,G) → H⁰(S,G″) → H¹(S,G′) → H¹(S,G) → H¹(S,G″),
```

where all homomorphisms other than $\partial$ come from the functoriality of $H^{0}$, respectively $H^{1}$.

**Remarks.**

<!-- label: XI.4.6 -->

The point of view set out here for the study of principal homogeneous bundles is visibly inspired by Serre [XI.7], which
the reader would do well to consult. When one wants a formalism that also applies to structural $S$-groups
quasi-projective over $S$, in order to include projective abelian schemes in particular, it is useful to modify XI.4.1
by requiring $S'$ to be a sum of preschemes $S'_{i}$ finite and locally free over open subsets $S_{i}$ covering $S$. The
preceding developments are then valid, including in particular XI.4.5, after replacing the affine hypothesis everywhere
by the quasi-projective hypothesis, and interpreting accordingly the definition given above of an exact sequence of
$S$-groups. It is enough to replace the reference to VIII.2.1

<!-- original page 298 -->

by VIII.7.7: the morphisms $S' \to S$ used are morphisms of effective descent for the fibered category of preschemes
quasi-projective over other preschemes. Be careful, however, that this second notion of principal homogeneous bundle is
more restrictive than the first, XI.4.1.

### 4.7.

<!-- label: XI.4.7 -->

One obtains an even more restrictive notion of principal homogeneous bundle by requiring $S$ to be covered by open
subsets $S_{i}$ such that for every $i$, $P|S_{i}$ is a trivial operator bundle under $G|S_{i}$; in this case one says
that $P$ is a **locally trivial** principal homogeneous bundle. The classes of these bundles, for fixed $G$, form a
subset of $H^{1}(X,G)$, in one-to-one correspondence with $H^{1}(X,\mathcal{O}_{X}(G))$, where $\mathcal{O}_{X}(G)$ is
the ordinary sheaf of sections of $G$ over $S$; cf. [XI.2]. For these $H^{1}$ to again give rise to a cohomology exact
sequence XI.4.5, one must plainly assume that the sequence $0 \to G' \to G \to G'' \to 0$ is exact in the reasonable
sense for this new context, that is, that $G$ is a locally trivial bundle over $G''$ with group ${G'_{G}}''$. This also
means that $u: G' \to G$ is a kernel of $v: G \to G''$, and that $G$ admits local sections over $G''$.

### 4.8.

<!-- label: XI.4.8 -->

It is plainly very desirable to continue the exact sequence XI.4.5 by introducing the higher cohomology groups
$H^{i}(X,G)$. This is possible in the framework of “Weil cohomology”: one considers the category $\mathcal{B}$ of
quasi-compact preschemes over $S$, endowed with the class $\mathcal{M}$ of faithfully flat and quasi-compact morphisms,
called localizing morphisms. An abelian “Weil sheaf” on $S$, or better, on $(\mathcal{B},\mathcal{M})$, is a
contravariant functor $\mathcal{F}$ from $\mathcal{B}$ to abelian groups, sending sums to products and every sequence
`T″ = T′ ×_T T′ ⇉ T′ → T`, with $T' \to T$ in $\mathcal{M}$, to an **exact** diagram of sets

```text
𝓕(T) → 𝓕(T′) ⇉ 𝓕(T″).
```

The Weil sheaves form an abelian category with exact filtered colimits and a generator, hence with enough injective
objects [XI.1]. The right derived functors of $\Gamma(\mathcal{F}) = \mathcal{F}(S)$ are denoted $H^{i}(S,\mathcal{F})$.
On the other hand, every commutative $S$-group plainly defines a Weil sheaf (VIII.5.2), whose $H^{0}$ and $H^{1}$ are
just $H^{0}(S,G)$ and $H^{1}(S,G)$. This gives a reasonable definition of the other $H^{i}(S,G)$.

<!-- original page 299 -->

Moreover, one shows that an exact sequence of $S$-groups defines an exact sequence of Weil sheaves, allowing one to
recover and extend the exact sequence XI.4.5. \[Translator note: the source footnote refers, for a systematic study of
this point of view, to SGA 4 I-IX.\]

### 4.9.

<!-- label: XI.4.9 -->

It would be appropriate to develop the noncommutative variants of XI.4.5 as in [XI.2]. For a systematic development, in
the proper framework, of the various cohomological notions sketched in the present number, we refer to work in
preparation by J. Giraud. \[Translator note: the corrected source identifies this as J. Giraud, *Cohomologie non
ab\acute{e}lienne*, Springer-Verlag, 1971.\]

## 5. Special Cases of Principal Bundles

<!-- label: XI.5 -->

Suppose now that $S$ is connected and endowed with a geometric point $a$, hence with a fundamental group $\pi_{1}(S,a)$
classifying the étale coverings of $S$: the category of étale coverings of $S$ is equivalent to the category of finite
sets on which $\pi_{1}$ acts continuously. It follows that a finite étale group scheme $G$ over $S$ is determined,
essentially, by an ordinary finite group $\mathcal{G}$ on which $\pi_{1}$ acts continuously by group automorphisms. An
étale covering $P$ of $S$ on which $G$ acts on the right is determined, essentially, by a finite set $\mathcal{P}$ on
which $\pi_{1}$ acts continuously on the left, and on which $\mathcal{G}$ acts on the right in a way compatible with the
operations of $\pi_{1}$:

```text
s(p · g) = (sp) · (sg),     for s ∈ π₁, p ∈ 𝒫, g ∈ 𝒢.
```

One verifies that $P$ is a principal homogeneous bundle in the sense of XI.4.1 if and only if $\mathcal{P}$ is a
principal homogeneous set under $\mathcal{G}$; for example, use the criterion XI.4.2. In other words, **the category of
principal homogeneous bundles over $S$ with group $G$ is equivalent to the category of principal homogeneous bundles
with group $G$ in the category of finite sets on which $\pi_{1}$ acts continuously**. In particular one deduces a
canonical bijection, functorial in $G$:

<!-- label: eq:XI.5.etoile -->

$$ (*) H^{1}(S,G) \simeq H^{1}(\pi_{1},\mathcal{G}), $$

where

<!-- original page 300 -->

the second member denotes the set of classes, up to isomorphism, of principal homogeneous bundles under $\mathcal{G}$ in
the category of finite sets on which $\pi_{1}$ acts; it is in fact needless to specify “continuously.” This set is made
explicit in the familiar way as the quotient of the set $Z^{1}(\pi_{1},G)$ of 1-cocycles $\phi: \pi_{1} \to
\mathcal{G}$, satisfying

```text
φ(1) = 1,     φ(st) = φ(s)(s · φ(t)),
```

by the natural action of the group $\mathcal{G}$.

<!-- label: page-300 -->

An important case is the one where $\pi_{1}$ acts trivially on $\mathcal{G}$, that is, where $G$ is a completely
decomposed covering of $S$, isomorphic to the sum of $\mathcal{G}$ copies of $S$. One then also writes
$H^{1}(S,\mathcal{G})$ instead of $H^{1}(S,G)$, and this set is in one-to-one correspondence, by (\*), with
$H^{1}(\pi_{1},\mathcal{G}) = \operatorname{Hom}(\pi_{1},\mathcal{G})$ modulo inner automorphisms of $\mathcal{G}$.
Notice, moreover, that in this case a principal homogeneous bundle over $S$ with group $G$ is nothing other than a
**principal covering** of $S$ with group $\mathcal{G}$ (V.2.7), and the preceding one-to-one correspondence is the one
deduced from the correspondence between principal coverings of $S$ with group $\mathcal{G}$, **pointed** above $a$, and
continuous homomorphisms from $\pi_{1}(S,a)$ to $\mathcal{G}$ (V, end of no. V.5).

The interest of relating the theory of étale coverings with that of principal bundles, already implicit in A. Weil,
_Généralisation des Fonctions Abéliennes_, and made explicit by S. Lang in his geometric theory of class fields, cf.
Serre [XI.5], comes from the following fact. Every $S$-group that is finite and étale over $S$ can be embedded in an
$S$-group $H$, affine and smooth over $S$, with connected fibers, and commutative when $G$ is. Therefore, by the exact
sequence XI.4.5, and possibly its noncommutative variants, the “discrete” classification of principal coverings with
group $G$ can be studied by means of the “continuous” classification of principal bundles with group $H$, and conversely
as well. For the idea of the general construction of the immersion of $G$ into $H$, apparently rather little used in
practice, see [XI.5, VI 2.8]. We shall content ourselves in the following number with developing two important special
cases, classical ones at that. We shall need the following auxiliary result.

**Proposition.**

<!-- label: XI.5.1 -->

Let

<!-- original page 301 -->

$S$ be a prescheme, and let $G$ be an $S$-group isomorphic to $GL(n)_{S}$, for example $\mathbb{G}_{m},S$, or to
$\mathbb{G}_{a},S$. Then every principal homogeneous bundle under $G$ is locally trivial.

Here $GL(n)_{S}$, for an integer $n \geq 0$, denotes the $S$-group representing the contravariant functor

$$ T \mapsto GL(n, \Gamma(T,\mathcal{O}_{T})) $$

on the $S$-prescheme $T$. In particular $\mathbb{G}_{m},S$, the “multiplicative group over $S$,” represents the
contravariant functor

$$ T \mapsto \Gamma(T,\mathcal{O}^{*}_{T}), $$

and therefore, as a prescheme over $S$, is isomorphic to $\operatorname{Spec} \mathcal{O}_{S}[t,t^{-1}]$, where $t$ is
an indeterminate. Similarly $\mathbb{G}_{a},S$ represents the contravariant functor

$$ T \mapsto \Gamma(T,\mathcal{O}_{T}), $$

and hence is isomorphic as an $S$-prescheme to $\operatorname{Spec}(\mathcal{O}_{S}[t])$, where $t$ is an indeterminate.
Notice that, by dévissage, XI.5.1 recovers Rosenlicht’s local-triviality result for the case where $G$ admits a
“composition series” whose successive factors are groups of the type considered here. For a finer study of questions of
local triviality of principal homogeneous bundles, cf. [XI.7] and [XI.3].

The first assertion is proved by observing that $G(T) = \operatorname{Aut}(\mathcal{O}^{n}_{T})$, and that the morphisms
$S' \to S$ occurring in XI.4.1, that is, those which are faithfully flat and quasi-compact, are morphisms of effective
descent for the fibered category of modules locally isomorphic to $\mathcal{O}^{n}_{T}$, that is, locally free of rank
$n$ (VIII.1.12). The second is proved in an analogous way, noting that in this case $G(T) =
\operatorname{Aut}(\mathcal{E}_{T})$, where $\mathcal{E}_{T}$ is the trivial **extension** of $\mathcal{O}_{T}$ by
$\mathcal{O}_{T}$, and where the automorphisms must of course respect the extension structure. The morphisms $S' \to S$
occurring in XI.4.1 are morphisms of effective descent for the fibered category of extensions of $\mathcal{O}_{T}$ by
$\mathcal{O}_{T}$, as follows easily from VIII.1.1, and such extensions are automatically locally trivial.

**Remark.**

<!-- label: XI.5.2 -->

Notice that the same type of proof applies to the symplectic group $Symp(2n)_{S}$, since an alternating form on a module
locally isomorphic to $\mathcal{O}^{2n}_{S}$, which is “nondegenerate,” that is, defines an isomorphism from this module
to its dual, is locally isomorphic to the standard form. The corresponding result for the orthogonal group is false,
however, already when $S$ is the spectrum of a field, since there may be quadratic forms over a field that are not
isomorphic to the standard form.

<!-- original page 302 -->

Moreover, it is shown essentially in [XI.3] that the groups `GL`, `Symp`, $\mathbb{G}_{a}$, and those which can be
dévissés into such groups, are, up to small qualifications, the only ones for which one has a local-triviality result of
the type considered here.

**Corollary.**

<!-- label: XI.5.3 -->

There are canonical bijections

$$ H^{1}(S,GL(n)_{S}) \simeq H^{1}(S,GL(n,\mathcal{O}_{S})), $$

in particular

$$ H^{1}(S,\mathbb{G}_{m},S) \simeq H^{1}(S,\mathcal{O}^{*}_{S}), $$

and

$$ H^{1}(S,\mathbb{G}_{a},S) \simeq H^{1}(S,\mathcal{O}_{S}), $$

where the second members denote cohomology groups of the topological space $S$ with coefficients in ordinary sheaves.

In particular, $H^{1}(S,GL(n)_{S})$ identifies with the set of isomorphism classes of modules locally free of rank $n$
on $S$, and $H^{1}(S,\mathbb{G}_{a},S)$ identifies with the set of classes of extensions of the module $\mathcal{O}_{S}$
by itself.

## 6. Application to Principal Coverings: Kummer and Artin-Schreier Theories

<!-- label: XI.6 -->

**Proposition.**

<!-- label: XI.6.1 -->

Let $S$ be a prescheme, let $n$ be an integer `> 0`, let

$$ u_{n}: \mathbb{G}_{m},S \to \mathbb{G}_{m},S $$

be the $n$-th power homomorphism, and let $\mu_{n},S$ be its kernel. Then $\mu_{n},S$ is finite and locally free of rank
$n$ over $S$, and it is étale over $S$ if and only if for every $s \in S$, the characteristic of $s$ is prime to $n$.
The sequence of homomorphisms

```text
0 → μ_n,S → 𝔾_m,S --u_n→ 𝔾_m,S → 0
```

is exact in the sense of no. XI.4. It will be called the **Kummer exact sequence** over $S$, relative to the integer
$n$.

One has

<!-- original page 303 -->

$$ \mathbb{G}_{m} = \operatorname{Spec} \mathcal{O}_{S}[t,t^{-1}], $$

and $u_{n}$ corresponds to the homomorphism $u_{n}$ on affine $\mathcal{O}_{S}$-algebras given by

$$ u_{n}(t) = t^{n}. $$

On the other hand, the unit section of $\mathbb{G}_{m},S$ corresponds to the augmentation homomorphism of
$\mathcal{O}_{S}$-algebras given by

$$ \epsilon(t) = 1, $$

whose kernel is therefore the principal ideal $(t - 1)$. The image of this ideal by $u_{n}$ is thus the principal ideal
$(1 - t^{n})$, and one finds

```text
μ_n,S = Spec 𝒪_S[t]/(1 − tⁿ).
```

This shows in particular that $\mu_{n},S$ is finite over $S$, and is defined by an algebra over $S$ that is free of rank
$n$, with basis formed by the $t^{i}$ for $0 \leq i \leq n - 1$. For it to be étale at $s \in S$, it is necessary and sufficient
that the reduced algebra $k[t]/(1 - t^{n})$, where $k = \kappa(s)$, obtained by formally adjoining the $n$-th roots of unity to
$k$, be separable over $k$; that is, that the roots of $1 - t^{n}$ in an algebraic closure of $k$ all be distinct. This is
equivalent to $n$ being prime to the characteristic. Finally, to show that the sequence of homomorphisms in XI.6.1 is
exact, the criterion XI.4.2 reduces us to proving that $u_{n}$ is faithfully flat. \[Translator note: the corrected source
replaces an erroneous “v” here by $u_{n}$.\] We may plainly suppose that $S$ is affine with ring $A$, hence that $\mathbb{G}_{m},S$
is affine with ring $B = A[t,t^{-1}]$. It is enough to verify that $u_{n}$ makes $B$ a free module of rank $n$ over $B$;
equivalently, that $u_{n}$ is injective and that $A[t,t^{-1}]$ is a free module of rank $n$ over $A[t^{n},t^{-n}]$. Indeed, one
checks easily that the $t^{i}$ for $0 \leq i \leq n - 1$ form a basis of the former over the latter, which completes the proof.

**Definition.**

<!-- label: XI.6.2 -->

<!-- original page 304 -->

The group $\mu_{n},S$ is called the **Kummer group of rank $n$ over $S$**, and a **Kummer principal covering of rank $n$
over $S$** is a principal homogeneous bundle over $S$ whose group is the Kummer group of rank $n$. \[Translator note:
the corrected source reads “rank $n$ over $S$,” correcting the old text’s malformed “n S.”\]

The set of these coverings is a group, denoted $H^{1}(S,\mu_{n},S)$, or simply $H^{1}(S,\mu_{n})$. Notice that the
formation of the Kummer group of rank $n$ over $S$ is compatible with extension of the base, so that $\mu_{n},S$ comes
by base extension from the **absolute Kummer group $\mu_{n}$** over $\operatorname{Spec}(\mathbb{Z})$.

Let $(\mathbb{Z}/n\mathbb{Z})_{S}$ denote the $S$-group defined by the ordinary finite group $\mathbb{Z}/n\mathbb{Z}$.
If $G$ is any $S$-group, the homomorphisms of $S$-groups $u$ from $(\mathbb{Z}/n\mathbb{Z})_{S}$ to $G$ are in
one-to-one correspondence, compatibly with base change, with the sections of $G$ over $S$ whose $n$-th power is the unit
section: to $u$ one associates the image by $u$ of the section of $(\mathbb{Z}/n\mathbb{Z})_{S}$ over $S$ defined by the
generator $1 mod n\mathbb{Z}$ of $\mathbb{Z}/n\mathbb{Z}$. With this understood:

**Corollary.**

<!-- label: XI.6.3 -->

If $\mu_{n},S$ is étale over $S$, one thereby obtains a one-to-one correspondence between isomorphisms of $S$-groups

$$ (\mathbb{Z}/n\mathbb{Z})_{S} \simeq \mu_{n},S $$

and sections of $\mathcal{O}_{S}$ that are of exact order $n$ on each connected component of $S$; such a section will be
called a “primitive $n$-th root of unity over $S$.” Therefore, for $\mu_{n},S$ to be isomorphic as an $S$-group to
$(\mathbb{Z}/n\mathbb{Z})_{S}$, it is necessary and sufficient that it be étale over $S$, that is, that the residual
characteristics of $S$ be prime to $n$, and that there exist a primitive $n$-th root of unity over $S$.

This explains the role played in classical Kummer theory by the hypothesis that the base field, playing the role of $S$,
have characteristic prime to $n$ and contain the $n$-th roots of unity, and by the choice of a primitive $n$-th root of
unity. Once the language of schemes is available, there is no longer any reason to burden oneself with these hypotheses;
one should reason directly with $\mu_{n}$ instead of $\mathbb{Z}/n\mathbb{Z}$. Thus the conjunction of XI.6.1, XI.4.5,
and XI.5.3 gives the following general relation between the theory of Kummer principal coverings and that of Picard
groups.

**Proposition.**

<!-- label: XI.6.4 -->

Let

<!-- original page 305 -->

$S$ be a prescheme. There is a canonical exact sequence

```text
0 → H⁰(S,μ_n) → H⁰(S,𝒪_S^*) → H⁰(S,𝒪_S^*) → H¹(S,μ_n)
  → H¹(S,𝒪_S^*) → H¹(S,𝒪_S^*),
```

hence, putting $H^{1}(S,\mathcal{O}^{*}_{S}) = \operatorname{Pic}(S)$, and denoting for every abelian group $A$ by
${}_{nA}$ and $A_{n}$ the kernel and cokernel of multiplication by $n$ in $A$, the exact sequence

$$ 0 \to H^{0}(S,\mathcal{O}_{S})^{*}_{n} \to H^{1}(S,\mu_{n}) \to {}_{nPic}(S) \to 0. $$

\[Translator note: the corrected source fixes the definition of $\operatorname{Pic}(S)$ here from $H^{1}(S,\mathcal{O}_{S})$ to $H^{1}(S,\mathcal{O}^{*}_{S})$.\]

We shall spell out two important cases, where one or the other extreme term of this exact sequence is zero.

**Corollary.**

<!-- label: XI.6.5 -->

Suppose ${}_{nPic}(S) = 0$, for example that $S$ is the spectrum of a local ring or of a factorial ring, and let $A$ be
the ring $H^{0}(S,\mathcal{O}_{S})$. Then there is a canonical isomorphism

$$ H^{1}(S,\mu_{n}) \simeq A^{*}/(A^{*})^{n}. $$

This is essentially the classical statement of Kummer theory when $S$ is the spectrum of a field.

**Corollary.**

<!-- label: XI.6.6 -->

Suppose that every element of $H^{0}(S,\mathcal{O}_{S})$ is an $n$-th power, for example that $H^{0}(S,\mathcal{O}_{S})$
is a composite of algebraically closed fields, or that $S$ is reduced and proper over an algebraically closed field $k$.
Then there is a canonical isomorphism

$$ H^{1}(S,\mu_{n}) \simeq {}_{nPic}(S). $$

In particular, when $S$ is proper and connected over an algebraically closed field $k$, this relates the fundamental
group of $S$ with the points of finite order of the Picard scheme $P$ of $S$ over $k$. Thus one has an isomorphism

$$ \operatorname{Hom}(\pi_{1}(S),\mathbb{Z}/n\mathbb{Z}) \simeq {}_{nP}(k) $$

for $n$ prime to the characteristic, a relation often used in algebraic

<!-- original page 306 -->

geometry. As an application, when the connected component $P^{0}$ of $P$ is a complete group scheme of dimension $g$,
one sees, using the results recalled in no. XI.2 and the finiteness of the Néron-Severi torsion group, that for every
prime number $\ell$ prime to the characteristic, the $\ell$-primary component of the abelianized fundamental group
$\pi_{1}(S)$ is a module of finite type and rank `2g` over the ring $\mathbb{Z}_{\ell}$ of $\ell$-adic integers; indeed
it is free except for at most finitely many values of $\ell$. As Serre observed, this allows one to prove under certain
conditions that when $X$ is a flat and projective scheme over connected $S$, the Picard schemes of the fibers of $X$ all
have the same dimension, by applying the semicontinuity theorem (X.2.3). Serre’s argument applies as soon as the Picard
scheme of $X$ over $S$ exists and the connected Picards of the fibers of $X$ over $S$ are proper group schemes; for
example when the geometric fibers of $X$ over $S$ are normal, with $X$ still flat and projective over $S$, and in
particular if $X$ is smooth and projective over $S$.

Now let $p$ be a prime number, and suppose that $S$ is a prescheme of characteristic $p$, that is, $p \cdot
\mathcal{O}_{S} = 0$. Then the $p$-th power homomorphism in $\mathcal{O}_{S}$ is additive, and the corresponding
morphism, obtained by replacing $S$ by a variable $T$ over $S$,

$$ F: \mathbb{G}_{a},S \to \mathbb{G}_{a},S $$

is therefore a homomorphism of $S$-groups, called the **Frobenius homomorphism**. Note that such a morphism is defined
for every $S$-prescheme $G$ which comes by base extension from a prescheme $G_{0}$ over the prime field
$\mathbb{Z}/p\mathbb{Z}$, and that this morphism is a group homomorphism if $G_{0}$ is a group prescheme. We put

```text
wp = id − F: 𝔾_a,S → 𝔾_a,S.
```

On the other hand, consider the $S$-group $(\mathbb{Z}/p\mathbb{Z})_{S}$ defined by the ordinary finite group
$\mathbb{Z}/p\mathbb{Z}$. We said that for every $S$-group $G$, the homomorphisms of $S$-groups from
$(\mathbb{Z}/p\mathbb{Z})_{S}$ to $G$ are in one-to-one correspondence with the sections of $G$ over $S$ whose $p$-th
power is the unit section. When $G = \mathbb{G}_{a},S$, they therefore correspond

<!-- original page 307 -->

to arbitrary sections of $G$ over $S$. Taking in particular the section of $\mathbb{G}_{a},S$ over $S$ corresponding to
the unit section of the sheaf of rings $\mathcal{O}_{S}$, one obtains a homomorphism of $S$-groups

$$ i: (\mathbb{Z}/p\mathbb{Z})_{S} \to \mathbb{G}_{a},S. $$

**Proposition.**

<!-- label: XI.6.7 -->

The sequence of homomorphisms of $S$-groups

$$ 0 \to (\mathbb{Z}/p\mathbb{Z})_{S} \to \mathbb{G}_{a},S \to \mathbb{G}_{a},S \to 0 $$

is exact in the sense of no. XI.4. It is called the **Artin-Schreier exact sequence** over $S$. \[Translator note: the
corrected source fixes the last group symbol in the displayed sequence.\]

It is enough to prove this over the prime field $k = \mathbb{Z}/p\mathbb{Z}$. It is enough to observe that the
homomorphism $wp*: k[t] \to k[t]$ defined by $wp*(t) = t - t^{p}$ makes `k[t]` a free module of rank $p$ over `k[t]`;
more precisely, `k[t]` is a free module over `k[s]`, where $s = t - t^{p}$, with basis formed by the $t^{i}$ for $0 \leq
i \leq p - 1$.

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

where the exponent $F$ in the last term denotes the subgroup of invariants under the endomorphism $F$, equal to the
kernel of $wp = id - F$.

Let us spell out two extreme cases:

**Corollary.**

<!-- label: XI.6.9 -->

Suppose $H^{1}(S,\mathcal{O}_{S})^{F} = 0$, for example that $S$ is an affine scheme. Then, putting $A =
H^{0}(S,\mathcal{O}_{S})$, there is a canonical isomorphism

$$ H^{1}(S,\mathbb{Z}/p\mathbb{Z}) \simeq A/wp A. $$

This is **Artin-Schreier theory** in its classical form, at least when $A$ is the spectrum of a field. \[Translator
note: the source says “when $A$ is the spectrum of a field”; mathematically one expects “when $S$ is the spectrum of a
field,” or “when $A$ is a field.”\]

**Corollary.**

<!-- label: XI.6.10 -->

Suppose

<!-- original page 308 -->

$wp H^{0}(S,\mathcal{O}_{S}) = H^{0}(S,\mathcal{O}_{S})$, for example that $H^{0}(S,\mathcal{O}_{S})$ is a composite of
algebraically closed fields, or that $S$ is proper over an algebraically closed field. Then there is a canonical
isomorphism

$$ H^{1}(S,\mathbb{Z}/p\mathbb{Z}) \simeq H^{1}(S,\mathcal{O}_{S})^{F}. $$

**Remarks.**

<!-- label: XI.6.11 -->

The last statement is due to J.-P. Serre [XI.9]. It is also possible to develop an analogous theory for the structural
group $\mathbb{Z}/p^{n}\mathbb{Z}$ for arbitrary $n$, using in place of $\mathbb{G}_{a}$ the Witt group scheme $W_{n}$; cf. loc. cit. Notice that in
characteristic $p > 0$, Kummer theory no longer gives information on principal coverings of order $p$, since $\mu_{p}$ is
then an “infinitesimal” group, that is, radicial over the base, and hence has no direct relation with $\mathbb{Z}/p\mathbb{Z}$. Thus at
first sight, the theory of these coverings no longer falls, when $S$ is a proper scheme over an algebraically closed
field for definiteness, under the theory of the Picard scheme as in XI.6.6. Nevertheless, if one recalls that the
Zariski tangent space at the origin in $\operatorname{Pic}_{S}/K$ \[Translator note: the source footnote refers for the definition of
$\operatorname{Pic}_{S}/K$ to A. Grothendieck, Séminaire Bourbaki no. 232, February 1962.\] identifies with $H^{1}(S,\mathcal{O}_{S})$, one sees that
**knowledge of the group scheme `_pPic_S/k`, the kernel of multiplication by $p$ in $\operatorname{Pic}_{S}/k$, implies knowledge of
$H^{1}(S,\mathbb{Z}/p\mathbb{Z})$ as well as of $H^{1}(S,\mu_{p})$; notice that it also implies knowledge of $H^{1}(S,\alpha_{p})$**, where $\alpha_{p}$ denotes the
infinitesimal group scheme over the prime field, the kernel of $F: \mathbb{G}_{a} \to \mathbb{G}_{a}$, which can also be described as the
spectrum of the restricted enveloping algebra of the trivial one-dimensional $p$-Lie algebra. Indeed, the exact sequence
XI.4.5 gives here

```text
H¹(S,α_p) ≃ Ker(F: H¹(S,𝒪_S) → H¹(S,𝒪_S)),
```

and more generally, denoting by $\alpha^{n}_{p}$ the kernel in $\mathbb{G}_{a}$ of the $n$-th iterate of $F$, one has

```text
H¹(S,α_pⁿ) ≃ Ker(Fⁿ: H¹(S,𝒪_S) → H¹(S,𝒪_S)).
```

In fact, knowledge of `_pPic_S/k` is equivalent to knowledge of $H^{1}(S,G)$ for every finite commutative algebraic

<!-- original page 309 -->

group annihilated by $p$; more generally, knowledge of ${}^{n}_{p}\operatorname{Pic}_{S}/k$ is equivalent to knowledge
of $H^{1}(S,G)$ for every finite commutative algebraic group $G$ annihilated by $p^{n}$, by virtue of the following
theorem, which in the case under consideration includes both Kummer theory and Artin-Schreier theory:

Let $G$ be a finite algebraic group over $k$, and let $D(G) = SheafHom_{k}-groups(G,\mathbb{G}_{m})$ be its **Cartier
dual**; the affine algebra of $D(G)$ is carried by the vector space dual to the affine algebra of $G$, that is, by the
hyperalgebra of $G$ in the sense of Dieudonné-Cartier. Then there is a canonical isomorphism:

<!-- label: eqXI.6.11 -->

```text
(*)   H¹(S,G) ≃ Hom_k-groups(D(G),Pic_S/k).
```

Here $S$ is a proper scheme over algebraically closed $k$ such that $H^{0}(S,\mathcal{O}_{S}) = k$. This formula may
also be expressed by saying that the “true fundamental group” of $S$ alluded to in no. XI.2, after abelianization, is
isomorphic to the projective limit of the $D(P_{i})$, where $P_{i}$ ranges over the **finite** algebraic subgroups of
$\operatorname{Pic}_{S}/k$; we shall denote it by $T\bullet(\operatorname{Pic}_{X}/k)$. When $S$ is an abelian variety,
we saw in XI.2.1 that this group is also isomorphic to the “true” Tate module $T_{\bullet}(S) = \lim {}_{nS}$, and the
isomorphism (\*) is then written in the more striking form

$$ Ext^{1}(A,G) \simeq \operatorname{Hom}(D(G),B), $$

where $A$ is an abelian variety, $B$ its dual, and $G$ a finite algebraic group over $k$. The results just indicated can
moreover be generalized to the case where $k$ is replaced by an arbitrary base prescheme, and to coefficient groups $G$
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
