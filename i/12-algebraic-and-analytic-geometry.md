# Exposé XII. Algebraic Geometry and Analytic Geometry

<!-- label: XII -->

<!-- original page 311 -->

Mme M. Raynaud. [Translator note: according to unpublished notes of A. Grothendieck.]

Proceeding as in [XII.10], one associates to every scheme $X$ locally of finite type over the field of complex numbers
$\mathbb{C}$ an analytic space $X^{an}$, whose underlying set is $X(\mathbb{C})$.

<!-- label: indnot:lb -->

In nos. XII.2 and XII.3 of this exposé, we give a “dictionary” between the usual properties of $X$ and of $X^{an}$, and
between the properties of a morphism $f: X \to Y$ and of the associated morphism $f^{an}: X^{an} \to Y^{an}$.

<!-- label: indnot:lc -->

We then show that the comparison theorems between coherent sheaves on $X$ and $X^{an}$, established in [XII.10, no. 12]
for a projective variety, are still valid when $X$ is a proper scheme.

Finally, in no. XII.5 we prove the equivalence between the category of finite étale coverings of $X$ and the category of
finite étale coverings of $X^{an}$. As a bonus for the reader, we give a new proof of the Grauert-Remmert theorem
[XII.6], using resolution of singularities [XII.8].

## 1. The Analytic Space Associated with a Scheme

<!-- label: XII.1 -->

<!-- original page 312 -->

Let $X$ be a scheme locally of finite type over $\mathbb{C}$. Let $\Phi$ be the functor from the category of analytic
spaces \[XII.4, no. 9\] to the category of sets which associates to an analytic space $\mathcal{X}$ the set of morphisms
of ringed spaces in $\mathbb{C}$-algebras $\operatorname{Hom}_{\mathbb{C}}(\mathcal{X},X)$. One has the following
theorem:

**Theorem-Definition.**

<!-- label: XII.1.1 -->

The functor $\Phi$ is representable by an analytic space $X^{an}$ and a morphism $\phi: X^{an} \to X$. One says that
$X^{an}$ is the analytic space associated with $X$.

If $|X^{an}|$ is the underlying set of $X^{an}$, $\phi$ induces a bijection from $|X^{an}|$ to the set $X(\mathbb{C})$
of points of $X$ with values in $\mathbb{C}$. Moreover, for each point $x$ of $X^{an}$, the morphism

$$ \phi_{x}: \mathcal{O}_{X},\phi(x) \to \mathcal{O}^{an}_{X},x, $$

which is necessarily local, gives after passage to completions an isomorphism

$$ \hat{\phi}_{x}: \hat{\mathcal{O}}_{X},\phi(x) \simeq \hat{\mathcal{O}}^{an}_{X},x. $$

In particular the morphism $\phi$ is flat.

Notice that the fact that $\phi$ induces a bijection from $X^{an}$ to $X(\mathbb{C})$ follows from the universal
property of $X^{an}$. On the other hand, one has the following assertions:

a. If the theorem is true for a scheme $Y$, then it is also true for every subscheme $X$ of $Y$. Suppose first that $X$
is an open subscheme of $Y$. If $\psi: Y^{an} \to Y$ is the canonical morphism, $\psi^{-1}(X)$ is an open subset

<!-- original page 313 -->

of $Y^{an}$, endowed with the analytic-space structure induced by that of $Y^{an}$. Since every morphism from an
analytic space $\mathcal{X}$ to $X$ factors through $Y^{an}$ by the universal property of the latter, and hence through
$X^{an}$, which is the fiber product $Y^{an} \times_{Y} X$, $X^{an}$ is the analytic space associated with $X$. Finally,
the assertion concerning the $\phi_{x}$ is evident.

It remains only to consider the case where $X$ is a closed subscheme of $Y$. Let $I$ be the coherent
$\mathcal{O}_{Y}$-ideal defining $X$. Then $I \cdot \mathcal{O}^{an}_{Y}$ is a coherent sheaf of ideals on
$\mathcal{O}^{an}_{Y}$ defining a closed analytic subspace $X^{an}$ of $Y^{an}$. As in the case of an open subscheme,
one sees that $X^{an}$ is the analytic space associated with $X$. Let $\phi: X^{an} \to X$ be the canonical morphism.
For every point $x$ of $X^{an}$, the morphism $\phi_{x}$ is none other than the morphism

```text
𝒪_Y,ψ(x)/I_ψ(x) → 𝒪_Y^an,x / I_ψ(x) · 𝒪_Y^an,x
```

induced by $\psi_{x}$. Its completion

$$ \hat{\mathcal{O}}_{Y},\psi(x) / I_{\psi}(x) \cdot \hat{\mathcal{O}}_{Y},\psi(x) \to \hat{\mathcal{O}}^{an}_{Y},x /
I_{\psi}(x) \cdot \hat{\mathcal{O}}^{an}_{Y},x $$

is an isomorphism, since $\hat{\psi}_{x}$ is one; this proves a.

b. If one has two $\mathbb{C}$-schemes $X_{1}$, $X_{2}$, such that $X^{an}_{1}$ and $X^{an}_{2}$ exist, then $(X_{1}
\times X_{2})^{an}$ also exists. Indeed, let $\phi_{1}: X^{an}_{1} \to X_{1}$ and $\phi_{2}: X^{an}_{2} \to X_{2}$ be
the canonical morphisms, and let $p_{1}$, $p_{2}$ be the two projections from $X^{an}_{1} \times X^{an}_{2}$. It follows
formally from EGA I 1.8.1 that $X_{1} \times X_{2}$ is the product of $X_{1}$ and $X_{2}$ in the category of ringed
spaces in local rings. Consequently the morphisms $\phi_{1} \cdot p_{1}$ and $\phi_{2} \cdot p_{2}$ define a

<!-- original page 314 -->

morphism $\phi: X^{an}_{1} \times X^{an}_{2} \to X_{1} \times X_{2}$, and the pair $(X^{an}_{1} \times X^{an}_{2},
\phi)$ represents the functor $\mathcal{X} \mapsto \operatorname{Hom}_{\mathbb{C}}(\mathcal{X}, X_{1} \times X_{2})$.

c. If $\mathcal{E}^{1}$ denotes affine space of dimension 1, that is, the topological space $\mathbb{C}$ endowed with the sheaf of holomorphic
functions, the functor $\mathcal{X} \mapsto \operatorname{Hom}_{\mathbb{C}}(\mathcal{X},E^{1}_{\mathbb{C}})$ is representable by $\mathcal{E}^{1}$, the canonical morphism $\phi: \mathcal{E}^{1} \to E^{1}_{\mathbb{C}}$ being the
evident morphism. \[Translator note: the corrected source adds in 2003 that $E^{1}_{\mathbb{C}}$ denotes the algebraic affine line
over $\mathbb{C}$.\] Indeed, to give a morphism from an analytic space $\mathcal{X}$ to $E^{1}_{\mathbb{C}}$ is equivalent to giving an element of
$\Gamma(\mathcal{X},\mathcal{O}_{\mathcal{X}})$, which is also equivalent to giving a morphism from $\mathcal{X}$ to $\mathcal{E}^{1}$. Plainly one has a bijection $|\mathcal{E}^{1}| \simeq E^{1}(\mathbb{C})$,
and, for each point $x \in \mathcal{E}^{1}$, the morphism $\hat{\phi}_{x}$ is none other than the identity morphism of a ring of formal power
series in one variable over $\mathbb{C}$.

It follows from b and c that the theorem is true for affine space $E^{n}_{\mathbb{C}}$, $n \geq 0$. Using a, one sees
that it is also true for every affine scheme $X$ locally of finite type over $\mathbb{C}$. If $X$ is no longer assumed
affine and if $(X_{i})$ is a covering of $X$ by affine opens, it follows from the universal property and from a that the
$X^{an}_{i}$ glue and thus define the analytic space $X^{an}$ associated with $X$.

### 1.2

<!-- label: XII.1.2 -->

Let $f: X \to Y$ be a morphism of $\mathbb{C}$-schemes locally of finite type. If $\phi: X^{an} \to X$ and $\psi: Y^{an}
\to Y$ are the canonical morphisms, it follows from the universal property of $Y^{an}$ that there exists a unique
morphism $f^{an}: X^{an} \to Y^{an}$ such that the diagram

```text
X^an → X
 |      |
f^an   f
 |      |
Y^an → Y
```

is

<!-- original page 315 -->

commutative. We have therefore defined a functor $\Phi$ from the category of $\mathbb{C}$-schemes locally of finite type
to the category of analytic spaces.

The functor $\Phi$ commutes with finite projective limits. Indeed it is enough to see that $\Phi$ commutes with fiber
products. But if $X$, $Y$, $Z$ are schemes locally of finite type over $\mathbb{C}$, it follows from the fact that $X
\times_{Z} Y$ is the fiber product of $X$ and $Y$ over $Z$ in the category of ringed spaces in local rings that $X^{an}
\times^{an}_{Z} Y^{an}$ satisfies the universal property characterizing $(X \times_{Z} Y)^{an}$.

### 1.3

<!-- label: XII.1.3 -->

Let $X$ be a $\mathbb{C}$-scheme locally of finite type, let $X^{an}$ be the associated analytic space, and let $\phi:
X^{an} \to X$ be the canonical morphism. If $F$ is an $\mathcal{O}_{X}$-module, the inverse image $\phi*F = F^{an}$ is a
sheaf of modules over $\mathcal{O}^{an}_{X}$. This defines a functor from the category of $\mathcal{O}_{X}$-modules to
the category of modules on $X^{an}$. This functor commutes with inductive limits (EGA 0 4.3.2). Since the sheaf
$\mathcal{O}^{an}_{X}$ is coherent [XII.4, no. 18, §2, th. 2], it sends coherent sheaves to coherent sheaves (EGA 0
5.3.11). Moreover:

**Subproposition.**

<!-- label: XII.1.3.1 -->

The functor which associates to an $\mathcal{O}_{X}$-module $F$ its inverse image $F^{an}$ on $X^{an}$ is exact,
faithful, and conservative.

Exactness follows from the fact that the morphism $\phi: X^{an} \to X$ is flat (XIII.1.1). Let us prove that the functor
$F \mapsto F^{an}$ is faithful. Taking exactness into account, it is enough to show that if $F^{an}$ is zero, then $F$
itself is zero. But for every point $x$ of $X^{an}$ one then has

```text
F_φ(x) ⊗_𝒪_X,φ(x) 𝒪_X^an,x = 0.
```

Since the morphism $\mathcal{O}_{X},\phi(x) \to \mathcal{O}^{an}_{X},x$ is faithfully flat, one has $F_{\phi}(x) = 0$
for every closed point $\phi(x)$ of $X$; and since $X$ is Jacobson (EGA IV 10.4.8), this implies that $F$ is zero.

The

<!-- original page 316 -->

fact that the functor $F \mapsto F^{an}$ is conservative is formal from exactness and faithfulness.

## 2. Comparison of Properties of a Scheme and of the Associated Analytic Space

<!-- label: XII.2 -->

**Proposition.**

<!-- label: XII.2.1 -->

Let $X$ be a $\mathbb{C}$-scheme locally of finite type, let $X^{an}$ be the associated analytic space, and let $n$ be
an integer. Consider the property $P$ of being:

```text
(i)    nonempty
(i′)   discrete
(ii)   Cohen-Macaulay
(iii)  (S_n)
(iv)   regular
(v)    (R_n)
(vi)   normal
(vii)  reduced
(viii) of dimension n.
```

Then $X$ has property $P$ if and only if $X^{an}$ has property $P$.

Let $\phi: X^{an} \to X$ be the canonical morphism. Assertion (i) follows from the fact that $|X^{an}| = X(\mathbb{C})$
(XIII.1.1) and from the fact that $X$ is Jacobson (EGA IV 10.4.8). To say that $X$, respectively $X^{an}$, is discrete
is equivalent to saying that $\dim X = 0$, respectively $\dim X^{an} = 0$ by [XII.4, no. 19, §4, cor. 6]; hence (i′)
follows from (viii).

Let $P$ be one of the properties (ii) through (vii). For $X$ to have property $P$, it is necessary and sufficient that
$P$ hold at every closed point of $X$. Indeed, since $X$ is excellent (EGA IV 7.8.6 (iii)), the set of points

<!-- original page 317 -->

where $X$ satisfies $P$ is open, and if this open contains all closed points, it is equal to all of $X$. Thus to say
that $X$, respectively $X^{an}$, has property $P$ is equivalent to saying that for every point $x$ of $X^{an}$, the
local ring $\mathcal{O}_{X},\phi(x)$, respectively $\mathcal{O}^{an}_{X},x$, has property $P$. Since the fact that an
excellent local ring has property $P$ can be detected after passage to the completion, the proposition follows from the
isomorphisms

$$ \hat{\mathcal{O}}_{X},\phi(x) \simeq \hat{\mathcal{O}}^{an}_{X},x $$

in cases (ii) through (vii). The same holds in case (viii), taking into account the relations

```text
dim X = sup_x dim 𝒪_X,φ(x),     dim X^an = sup_x dim 𝒪_X^an,x,
```

where $x \in X^{an}$. This completes the proof.

**Proposition.**

<!-- label: XII.2.2 -->

Let $X$ be a $\mathbb{C}$-scheme locally of finite type, let $\phi: X^{an} \to X$ be the canonical morphism, and let $T$
be a locally constructible subset of $X$. Then one has the relation

$$ \phi^{-1}(closure(T)) = closure(\phi^{-1}(T)). $$

We may suppose that $T$ is a dense open subset of $X$. Let $H$ be the reduced closed subscheme of $X$ whose underlying
space is $X - T$. The associated space $H^{an}$ is a closed analytic subspace of $X^{an}$ whose underlying space is
$X^{an} - \phi^{-1}(T)$. We must show that every point $x$ of $H^{an}$ belongs to $closure(\phi^{-1}(T))$. But at such a
point $x$, the germ of analytic space $(X^{an},x)$ contains the subgerm $(H^{an},x)$, and this is defined by a
non-nilpotent ideal of $\mathcal{O}^{an}_{X},x$. It then follows from the Nullstellensatz [XII.4, no. 19, §4, cor. 3]
that every open neighborhood of $x$ contains points of $X^{an}$ which do not belong to $H^{an}$. This proves that $x \in
closure(\phi^{-1}(T))$.

**Corollary.**

<!-- label: XII.2.3 -->

Let

<!-- original page 318 -->

$X$ be a $\mathbb{C}$-scheme locally of finite type, let $\phi: X^{an} \to X$ be the canonical morphism, and let $T$ be
a locally constructible subset of $X$. For $T$ to be an open subset, respectively a closed subset, respectively a dense
subset, it is necessary and sufficient that $\phi^{-1}(T)$ have the corresponding property.

The corollary follows from XII.2.2 and from the fact that, since $X$ is a Jacobson scheme (EGA IV 10.4.8), two locally
constructible subsets of $X$ that have the same trace on the very dense set $X(\mathbb{C})$ are equal.

**Proposition.**

<!-- label: XII.2.4 -->

Let $X$ be a $\mathbb{C}$-scheme locally of finite type. For $X$ to be connected, respectively irreducible, it is
necessary and sufficient that $X^{an}$ be connected, respectively irreducible.

Suppose $X^{an}$ is connected, respectively irreducible. The image $X(\mathbb{C})$ of $X^{an}$ in $X$ is then connected,
respectively irreducible. It follows that $X$ is connected, respectively irreducible, because closed subsets of $X$ and
of $X(\mathbb{C})$ correspond bijectively (EGA IV 10.1.2).

Conversely suppose $X$ is connected, respectively irreducible, and let us show that the same is true of $X^{an}$. We may
restrict to the case where $X$ is irreducible. Indeed, suppose $X$ is connected. Given a point $x$ of $X$, the set of
points $y \in X$ for which there exists a finite sequence of irreducible closed subschemes $X_{1}, \cdots, X_{n}$ of
$X$, with $x \in X_{1}$, $y \in X_{n}$, and $X_{i} \cap X_{i+1} \neq \emptyset$ for $1 \leq i \leq n - 1$, is both open
and closed, hence equal to all of $X$. For a sequence $X_{1}, \cdots, X_{n}$ as above, one also has $X^{an}_{i} \cap
X^{an}_{i+1} \neq \emptyset$ for $1 \leq i \leq n - 1$; if the $X^{an}_{i}$ are known to be connected, then $X^{an}$ is
connected as well.

From now on

<!-- original page 319 -->

suppose $X$ is irreducible. We may also suppose $X$ affine. Indeed, if $(U_{i})_{i\in I}$ is a covering of $X$ by affine
opens, any two of these opens have nonempty intersection, and the same property is therefore true for the covering
$(U^{an}_{i})_{i\in I}$ of $X^{an}$. If the $U^{an}_{i}$ are known to be irreducible, then $X^{an}$ is irreducible as
well.

We may further suppose that $X$ is normal. Indeed, let $\tilde{X}$ be the normalization of $X$. Since the morphism
$\tilde{X} \to X$ is surjective, so is $\tilde{X}^{an} \to X^{an}$, which proves that if $\tilde{X}^{an}$ is
irreducible, then $X^{an}$ is irreducible as well.

From now on suppose $X$ is affine normal. Since the local rings of $X^{an}$ are integral domains, saying that $X^{an}$
is irreducible is equivalent to saying that it is connected. Indeed, if $\mathcal{F}$ is a closed analytic subset of
$X^{an}$, the set of points $x$ of $X^{an}$ at which $codim_{x}(\mathcal{F},X^{an}) = 0$ is a closed analytic subset of
$X^{an}$ [XII.4, no. 20 A, cor. 1] which is also open. If $X^{an}$ is connected, this proves that, whenever $\mathcal{F}
\neq X^{an}$, $\mathcal{F}$ is rare; hence $X^{an}$ is irreducible. We are thus reduced to showing that $X^{an}$ is
connected.

Let

$$ i: X \to P $$

be a compactification of $X$, where $P$ is a normal projective $\mathbb{C}$-scheme and $i$ is a dominant open immersion.
It then follows from [XII.10, no. 12, th. 1] that $P^{an}$ is connected. Since $X^{an}$ is obtained by removing from
$P^{an}$ a rare closed analytic subset, it follows from XII.2.5 below that $X^{an}$ is also connected.

**Lemma.**

<!-- label: XII.2.5 -->

Let

<!-- original page 320 -->

$\mathcal{P}$ be a connected normal analytic space, and let $\mathcal{Y}$ be a rare closed analytic subset. Then
$\mathcal{X} = \mathcal{P} - \mathcal{Y}$ is connected.

When $\mathcal{Y}$ has codimension $\geq 2$, the proposition follows from [XII.11, no. 3, prop. 4]. In the general case
one may suppose, after removing from $\mathcal{P}$ a closed analytic subset of codimension $\geq 2$, that $\mathcal{P}$
and $\mathcal{Y}$, regarded as a reduced analytic subspace of $\mathcal{P}$, are regular. By the implicit function
theorem, every point $y$ of $\mathcal{Y}$ has a neighborhood $\mathcal{U}$ isomorphic to a ball in an affine space
$\mathcal{E}^{n}$, such that $\mathcal{U} \cap \mathcal{Y}$ is defined by the vanishing of a certain number of
coordinate functions. This proves that $\mathcal{U} - \mathcal{U} \cap \mathcal{Y}$ is connected, and hence that
$\mathcal{X}$ is connected.

**Corollary.**

<!-- label: XII.2.6 -->

Let $X$ be a $\mathbb{C}$-scheme locally of finite type. The morphism

$$ \pi_{0}(X^{an}) \to \pi_{0}(X) $$

induced by the canonical morphism $X^{an} \to X$ is bijective.

## 3. Comparison of Properties of Morphisms

<!-- label: XII.3 -->

**Proposition.**

<!-- label: XII.3.1 -->

Let $f: X \to Y$ be a morphism of $\mathbb{C}$-schemes locally of finite type, and let $f^{an}: X^{an} \to Y^{an}$ be
the morphism deduced from $f$ on the associated analytic spaces. Let $P$ be the property of being:

```text
(i)    flat
(ii)   net, that is, unramified
(iii)  étale
(iv)   smooth
(v)    normal
(vi)   reduced
(vii)  injective
(viii) separated
(ix)   an isomorphism
(x)    a monomorphism
(xi)   an open immersion.
```

Then $f$ has property $P$ if and only if $f^{an}$ has property $P$.

Let $\phi: X^{an} \to X$ and $\psi: Y^{an} \to Y$ be the canonical morphisms. Let $x$ be a point of $X^{an}$, and put $y
= f^{an}(x)$. The morphisms $\mathcal{O}^{an}_{Y},y \to \mathcal{O}^{an}_{X},x$ and $\mathcal{O}_{Y},\psi(y) \to
\mathcal{O}_{X},\phi(x)$ deduced from $f^{an}$ and $f$ give the same morphism after passage to completions (XII.1.1). By
[XII.2, ch. 3, §5, prop. 4], respectively EGA IV 17.4.4, it is therefore equivalent to say that $f^{an}$ satisfies
property (i), respectively (ii), and to say that $f$ satisfies (i), respectively (ii), at every closed point of $X$.
Since the set of points of $X$ where (i), respectively (ii), holds is open (EGA IV 11.1.1 and I 3.3), this proves (i)
and (ii), hence also (iii).

Let $P$ be property (iv), respectively (v), respectively (vi). Taking XII.2.1 ((v), (vi), (vii)) into account, it is
equivalent to say that the geometric fibers of $f^{an}$ at the various points $y$ of $Y^{an}$ are regular, respectively
normal, respectively reduced, and to say that the same is true of the geometric fibers of $f$ at the various closed
points $\psi(y)$ of $Y$. Cases (iv), respectively (v), respectively (vi), then follow from (i) and from the fact that
the set of points of $Y$ where the geometric fibers of $f$ are regular is open (EGA IV 12.1.7).

(vii). If $f$ is injective, so is $f^{an}$. Conversely suppose $f^{an}$ is injective and let us show that $f$ is
injective. We may suppose

<!-- original page 322 -->

$f$ of finite type. Since $f^{an}$ is injective, the fibers of $f$ at closed points of $Y$ are radicial. Since the set
of points of $Y$ whose fiber is radicial is locally constructible (EGA IV 9.6.1), and since $Y$ is a Jacobson scheme,
all fibers of $f$ are radicial; hence $f$ is injective.

(viii). Let $\Delta: X \to X \times_{Y} X$ and $\Delta^{an}: X^{an} \to X^{an} \times_{Y^{an}} X^{an}$ be the diagonal
immersions, and let $\Theta: X^{an} \times_{Y^{an}} X^{an} \to X \times_{Y} X$ be the canonical morphism. By XII.2.3,
saying that $\Delta(X)$ is closed in $X \times_{Y} X$ is equivalent to saying that $\Delta^{an}(X^{an})$ is closed in
$X^{an} \times_{Y^{an}} X^{an}$.

Since an open immersion is nothing other than an étale injective morphism (EGA IV 17.9.1 and [XII.4, no. 13, §1]), (xi)
follows from (iii) and (vii). Since an isomorphism is the same thing as a surjective open immersion, (ix) follows from
(xi) and XII.3.2 (i) below. Saying that $f$ is a monomorphism is equivalent to saying that the diagonal morphism
$\Delta: X \to X \times_{Y} X$ is an isomorphism, so (x) follows from (ix).

**Proposition.**

<!-- label: XII.3.2 -->

Let $X$ and $Y$ be two $\mathbb{C}$-schemes locally of finite type, let $f: X \to Y$ be a morphism of finite type, and
let $f^{an}: X^{an} \to Y^{an}$ be the morphism deduced from $f$ on the associated analytic spaces. Let $P$ be the
property of being:

```text
(i)   surjective
(ii)  dominant
(iii) a closed immersion
(iv)  an immersion
(v)   proper
(vi)  finite.
```

Then $f$ has property $P$ if and only if $f^{an}$ has property $P$. \[Translator note: the source footnote says that a
morphism of analytic spaces is called proper if it is proper in the sense of [XII.1, ch. 1, §10, no. 1] and is
separated.\]

<!-- original page 323 -->

Let $\phi: X^{an} \to X$ and $\psi: Y^{an} \to Y$ be the canonical morphisms.

(i). If $f$ is surjective, then for every point $y$ of $Y^{an}$, $f^{-1}(\psi(y))$ is a nonempty closed subset of $X$;
hence it contains at least one closed point, which proves that $f^{an}$ is surjective. Conversely, if $f^{an}$ is
surjective, $f(X)$ is a locally constructible subset of $Y$ (EGA IV 1.8.4) containing all closed points of $Y$; hence
$f(X) = Y$.

(ii) follows from XII.2.2.

(iii). If $f$ is a closed immersion, then so is $f^{an}$ by XII.1.1 a. Conversely, if $f^{an}$ is a closed immersion,
then so is $f$ by XII.3.1 (x) and XII.3.2 (v), since this is equivalent to saying that $f$ is a proper monomorphism (EGA
IV 8.11.5).

(iv). It is clear that if $f$ is an immersion, then so is $f^{an}$. Conversely suppose $f^{an}$ is an immersion, and let
$T$ be the image of $X$ in $Y$, and $\bar{T}$ the scheme-theoretic closure of $f$. There is a factorization of $f$

```text
X --i→ T̄ --j→ Y,
```

where $j$ is a closed immersion and $i$ is the canonical morphism; from it one deduces the following factorization of
$f^{an}$:

```text
X^an --i^an→ T̄^an --j^an→ Y^an.
```

Since

<!-- original page 324 -->

$T = f(X)$ is a locally constructible subset of $Y$ (EGA IV 1.8.4), one has, by XII.2.2, $\bar{T}^{an} =
closure(f^{an}(X^{an}))$. It follows that $i^{an}(X^{an})$ is open in $\bar{T}^{an}$, hence that $i(X)$ is open in
$\bar{T}$. Consider the canonical factorization of $i$

```text
X --i₁→ i(X) --i₂→ T̄.
```

The morphism $i^{an}_{1}$ is a proper monomorphism, hence so is $i_{1}$ by XII.3.2 (v) and XII.3.1 (x). This proves that
$i_{1}$, and hence also $f$, is an immersion.

(v). Suppose $f$ is proper and let us show that $f^{an}$ is proper. Since properness of $f^{an}$ is local on $Y^{an}$,
we may suppose $Y$ affine. By Chow’s lemma (EGA II 5.6.1), one can find a projective $Y$-scheme $X'$ and a projective
surjective morphism

$$ g: X' \to X. $$

The morphism $(fg)^{an} = f^{an} g^{an}$ is projective, hence proper; $g^{an}$ is surjective; and it follows from \[XII.1, ch.
1, §10\] that $f^{an}$ is proper.

Conversely suppose $f^{an}$ is proper and let us show that $f$ is proper. By XII.3.1 (viii), $f$ is separated. It
remains to prove that $f$ is universally closed, and it is even enough to show that $f$ is closed. Indeed, for every
$Y$-scheme $Y'$ locally of finite type, the morphism

```text
f_(Y′) = h: X ×_Y Y′ → Y′
```

will also be closed since $h^{an}$ is proper. Let $T$ be a closed subset of $X$. The set $f(T)$ is locally
constructible, and one has

$$ f^{an}(\phi^{-1}(T)) = \psi^{-1}(f(T)). $$

Since

<!-- original page 325 -->

$f^{an}$ is proper, $\psi^{-1}(f(T))$ is a closed subset of $Y^{an}$, and therefore it follows from XII.2.2 that

$$ \psi^{-1}(closure(f(T))) = \psi^{-1}(f(T)). $$

This implies $f(T) = closure(f(T))$, that is, $f$ is closed; hence $f$ is proper.

(vi). Saying that a morphism is finite is equivalent to saying that it is proper with finite fibers (EGA III 4.4.2 and
[XII.4, no. 19, §5]). Since the set of points where the fibers of $f$ are finite is locally constructible (EGA IV
9.7.9), the fibers of $f$ are finite if and only if the fibers of $f^{an}$ are finite. Thus (vi) follows from (v).

**Remark.**

<!-- label: XII.3.3 -->

a. Let $f: X \to Y$ be a morphism of $\mathbb{C}$-schemes locally of finite type. The fact that $f^{an}$ is a local isomorphism does
not imply that $f$ is one. Indeed, if $f$ is étale, $f^{an}$ is étale and hence is a local isomorphism \[XII.4, no. 13,
§1\], but this need not be true of $f$.

b. The statement XII.3.2 is not true if $f$ is not assumed of finite type. For example, $f^{an}$ can be a closed
immersion without $f$ being one. It is enough to take $X$ to be the sum of $\mathbb{Z}$ copies of $\operatorname{Spec}
\mathbb{C}$, $Y$ to be the affine line, and $f$ the morphism obtained by sending the points of $X$ to distinct points of
$Y$ forming a discrete subset.

## 4. Cohomological Comparison Theorems and Existence Theorems

<!-- label: XII.4 -->

<!-- original page 326 -->

The purpose of this number is to reprove the results of [XII.3, no. 2, ths. 5 and 6]. These generalize to the case of a
proper scheme the theorems established in [XII.10, no. 12] when $X$ is projective, and extend them to the relative case.
More general results, concerning relative proper schemes over an analytic space, are proved in [XII.7, ch. VIII, no. 3].

Recall that the Čech cohomology used in [XII.10, no. 12] coincides with the usual cohomology in the algebraic case as
well as in the analytic case (EGA III 1.4.1 and [XII.5, II 5.10]).

### 4.1

<!-- label: XII.4.1 -->

Let $f: X \to Y$ be a morphism of $\mathbb{C}$-schemes locally of finite type, and consider the commutative diagram

```text
X^an --φ→ X
 |        |
f^an     f
 |        |
Y^an --ψ→ Y.
```

If $F$ is an $\mathcal{O}_{X}$-module, then for every integer $p \geq 0$ one has morphisms

```text
Rᵖf_*F --i→ Rᵖf_*(φ_*F^an) --j→ Rᵖ(f·φ)_*F^an --k→ ψ_*(Rᵖf_*^an F^an),
```

where $i$ is deduced from the canonical morphism $F \to \phi_{*}F^{an}$, and $j$, $k$ are “edge homomorphisms” of Leray
spectral sequences. With the composite $k \cdot j \cdot i$ there is associated a canonical morphism

<!-- label: eq:XII.4.1.1 -->

$$ (4.1.1) \theta_{p}: (R^{p}f_{*}F)^{an} \to R^{p}f^{an}_{*}(F^{an}). $$

**Theorem.**

<!-- label: XII.4.2 -->

Let

<!-- original page 327 -->

$f: X \to Y$ be a proper morphism of $\mathbb{C}$-schemes locally of finite type, and let $F$ be a coherent
$\mathcal{O}_{X}$-module. Then, for every integer $p \geq 0$, the morphism (4.1.1)

$$ \theta_{p}: (R^{p}f_{*}F)^{an} \to R^{p}f^{an}_{*}(F^{an}) $$

is an isomorphism.

1. **The case where $f$ is projective.** The proof is analogous to that of [XII.10, no. 13]. Let us recall it briefly.
   One reduces to the case where $X$ is a projective space of type $\mathbb{P}^{r}_{Y}$ over $Y$. Let $\mathcal{Y} =
   Y^{an}$ and $\mathcal{P} = \mathbb{P}^{r}_{\mathcal{Y}}$. One first proves that

```text
f_*^an 𝒪_𝓟 = 𝒪_𝓨,     Rᵖf_*^an(𝒪_𝓟) = 0 for p > 0.
```

To verify the preceding relations, one may reduce to the case where $\mathcal{Y}$ is a ball $\mathcal{B}$ in an affine
space $\mathcal{E}^{n}$. One considers the “standard covering” ${\mathcal{U}_{i}}$ of $\mathcal{P}$ by $r + 1$ open
subsets isomorphic to $\mathcal{B} \times \mathcal{E}^{r}$. Since these opens are Stein, one has, for every integer $p
\geq 0$, isomorphisms

$$ H^{p}({\mathcal{U}_{i}},\mathcal{O}_{\mathcal{P}}) \simeq H^{p}(\mathcal{P},\mathcal{O}_{\mathcal{P}}). $$

One can then express the sections of the structural sheaf $\mathcal{O}_{\mathcal{P}}$ on the opens $\mathcal{U}_{i}$ and
on their intersections in terms of Laurent series. An easy calculation proves that

```text
H⁰(𝓟,𝒪_𝓟) ≃ H⁰(𝓨,𝒪_𝓨),     Hᵖ(𝓟,𝒪_𝓟) = 0 for p > 0.
```

The proof is then completed by copying [XII.10, no. 12, lemma 5], with cohomology groups replaced by cohomology sheaves.

2.

<!-- original page 328 -->

**The case where $f$ is proper.** One uses EGA III 3.1.2 to reduce to the projective case. Let $\mathcal{K}$ be the
category of coherent $\mathcal{O}_{X}$-modules such that $\theta_{p}$ is an isomorphism for every $p \geq 0$. It is
enough to prove that, for every exact sequence $0 \to F' \to F \to F'' \to 0$ whose two terms are in $\mathcal{K}$, the
third is also in $\mathcal{K}$; that a direct factor of an object of $\mathcal{K}$ is in $\mathcal{K}$; and that, for
every point $x$ of $X$, one can find an object $F$ of $\mathcal{K}$ such that $F_{x} \neq 0$.

The first condition follows by applying the five lemma to the following commutative diagram, whose rows are exact:

```text
… → (Rᵖf_*F′)^an → (Rᵖf_*F)^an → (Rᵖf_*F″)^an → (Rᵖ⁺¹f_*F′)^an → …
      ↓                ↓                 ↓                   ↓
… → Rᵖf_*^an F′^an → Rᵖf_*^an F^an → Rᵖf_*^an F″^an → Rᵖ⁺¹f_*^an F′^an → …
```

The second condition is verified analogously.

To verify the third condition, one may restrict to the case where $X$ is an irreducible scheme with generic point $x$.
We could have supposed $Y$ noetherian from the beginning. By Chow’s lemma (EGA II 5.6.1), one can find a projective
$Y$-scheme $X'$ and a projective surjective morphism $g: X' \to X$. On the other hand, there exists an integer $n$ such
that $R^{p}g_{*}(\mathcal{O}_{X}'(n)) = 0$ for all $p > 0$ and such that the canonical morphism
$g*g_{*}(\mathcal{O}_{X}'(n)) \to \mathcal{O}_{X}'(n)$ is surjective (EGA III 2.2.1). If one puts $F =
g_{*}(\mathcal{O}_{X}'(n))$, the sheaf $F$ answers the question. Indeed $F_{x} \neq 0$; moreover, the Leray spectral
sequence

$$ R^{p}f_{*}(R^{qg}_{*}(\mathcal{O}_{X}'(n))) \Rightarrow R^{p+q}(f\cdot g)_{*}(\mathcal{O}_{X}'(n)) $$

is degenerate, so one has an isomorphism

$$ R^{p}f_{*}F \simeq R^{p}(f\cdot g)_{*}(\mathcal{O}_{X}'(n)). $$

<!-- original page 329 -->

As in the algebraic case, one has a canonical isomorphism

$$ R^{p}f^{an}_{*} F^{an} \simeq R^{p}(f\cdot g)^{an}_{*}(\mathcal{O}_{X}'(n)^{an}), $$

and the diagram

$$ (R^{p}f_{*}F)^{an} \simeq (R^{p}(f\cdot g)_{*}(\mathcal{O}_{X}'(n)))^{an} \downarrow \theta_{p} \downarrow \psi_{p}
R^{p}f^{an}_{*} F^{an} \simeq R^{p}(f\cdot g)^{an}_{*}(\mathcal{O}_{X}'(n)^{an}) $$

is commutative. By 1, $\psi_{p}$ is an isomorphism; hence $\theta_{p}$ is also an isomorphism. This completes the proof.

**Corollary.**

<!-- label: XII.4.3 -->

Let $X$ be a proper $\mathbb{C}$-scheme, and let $F$ be a coherent $\mathcal{O}_{X}$-module. Then, for every integer $p
\geq 0$, the canonical morphism

$$ H^{p}(X,F) \to H^{p}(X^{an},F^{an}) $$

is an isomorphism.

**Theorem.**

<!-- label: XII.4.4 -->

Let $X$ be a proper $\mathbb{C}$-scheme. The functor which associates to every coherent $\mathcal{O}_{X}$-module $F$ its
inverse image $F^{an}$ on $X^{an}$ is an equivalence of categories.

1. **The functor is fully faithful.** Indeed, let $F$ and $G$ be two coherent $\mathcal{O}_{X}$-modules. The canonical
   morphism

```text
Hom_𝒪_X(F,G) → Hom_𝒪_X^an(F^an,G^an)
```

identifies with the canonical morphism

```text
H⁰(X,SheafHom_𝒪_X(F,G)) → H⁰(X^an,SheafHom_𝒪_X(F,G))
```

<!-- original page 330 -->

(EGA `0_I` 6.7.6). Since `SheafHom_𝒪_X(F,G)` is coherent, it follows from XII.4.3 that this morphism is bijective.

1. **The functor is essentially surjective.** When $X$ is projective, the assertion follows from \[XII.10, no. 12, th.
   3\]. The general case reduces to the preceding one by using Chow’s lemma (EGA II 5.6.1). Indeed, let $X'$ be a
   projective $\mathbb{C}$-scheme, let $f: X' \to X$ be a projective surjective morphism, and let $U$ be a dense open
   subset of $X$ such that $f$ induces an isomorphism $f^{-1}(U) \simeq U$. We reason by noetherian induction on $X$;
   hence we may suppose that for every coherent sheaf $\mathcal{G}$ on $X^{an}$ for which one can find a closed subset
   $Y$ of $X$, distinct from $X$, satisfying $Y^{an} \supset Supp \mathcal{G}$, there exists a coherent sheaf $G$ on $X$
   such that $G^{an} \simeq \mathcal{G}$.

Let $\mathcal{F}$ be a coherent sheaf of modules over $\mathcal{O}^{an}_{X}$, and let $\mathcal{K}$ and $\mathcal{L}$ be
the coherent sheaves defined by requiring the sequence

```text
0 → 𝓚 → 𝓕 → f_*^an f^an*𝓕 → 𝓛 → 0
```

to be exact. Since $X'$ is projective, there exists a coherent $\mathcal{O}_{X}'$-module $F'$ such that $F'^{an} \simeq
f^{an}*\mathcal{F}$. From XII.4.2 one then deduces an isomorphism $(f_{*}F')^{an} \simeq f^{an}_{*} f^{an}*\mathcal{F}$.
Since $\mathcal{K}|U^{an}$ and $\mathcal{L}|U^{an}$ are zero, there exist coherent $\mathcal{O}_{X}$-modules $K$ and $L$
such that $K^{an} \simeq \mathcal{K}$ and $L^{an} \simeq \mathcal{L}$. By 1, the morphism $f^{an}_{*} f^{an}*\mathcal{F}
\to \mathcal{L}$ comes from a unique morphism $f_{*}F' \to L$. Let $I = Ker(f_{*}F' \to L)$. The sheaf $\mathcal{F}$ is
then an extension of $I^{an}$ by $K^{an}$, and it remains only to see that this extension comes

<!-- original page 331 -->

by inverse image from an extension of $I$ by $K$. It is therefore enough to prove that the canonical morphism

<!-- label: eq:XII.4.* -->

```text
(*)   Ext^q_𝒪_X(I,K)^an ≃ Ext^q_𝒪_X^an(I^an,K^an),     q = 1,
```

is bijective. \[Translator note: the source prints “$q \neq 1$,” but the preceding sentence shows that the needed case is
$q = 1$; this is a mathematical correction rather than a change of argument.\] Now one has isomorphisms

```text
ExtSheaf^q_𝒪_X(I,K)^an ≃ ExtSheaf^q_𝒪_X^an(I^an,K^an)
```

for every integer $q \geq 0$ (EGA $0_{III}$ 12.3.5), and a morphism of spectral sequences

```text
Hᵖ(X,ExtSheaf^q_𝒪_X(I,K))              ⇒ Ext^(p+q)_𝒪_X(I,K)
     ↓                                             ↓
Hᵖ(X^an,ExtSheaf^q_𝒪_X^an(I^an,K^an)) ⇒ Ext^(p+q)_𝒪_X^an(I^an,K^an).
```

This morphism is an isomorphism because, by XII.4.3, it is so on the $E^{p,q}_{2}$-terms; this proves the bijectivity of
`(*)`.

**Corollary.**

<!-- label: XII.4.5 -->

The functor which associates $X^{an}$ to every proper $\mathbb{C}$-scheme $X$ is fully faithful.

We must show that, if $X$ and $Y$ are two proper $\mathbb{C}$-schemes, the canonical map

$$ \operatorname{Hom}_{\mathbb{C}}(X,Y) \to \operatorname{Hom}(X^{an},Y^{an}) $$

is bijective. But to give a morphism from $X$ to $Y$, respectively from $X^{an}$ to $Y^{an}$, is equivalent to giving
its graph, that is, a closed subscheme $Z$ of $X \times Y$, respectively a closed analytic subspace $\mathcal{Z}$ of
$X^{an} \times Y^{an}$, such that the restriction of the first projection $X \times Y \to X$ to $Z$, respectively of
$X^{an} \times Y^{an} \to X^{an}$ to $\mathcal{Z}$, is

<!-- original page 332 -->

an isomorphism. Since giving a closed subscheme of $X \times Y$, respectively a closed analytic subspace of $X^{an}
\times Y^{an}$, is equivalent to giving a coherent sheaf of ideals on $\mathcal{O}_{X\times Y}$, respectively on
$\mathcal{O}_{X^{an}\times Y^{an}}$, the corollary follows from XII.4.4.

**Corollary.**

<!-- label: XII.4.6 -->

Let $X$ be a proper $\mathbb{C}$-scheme. The functor which associates $X'^{an}$ to every finite, respectively finite
étale, scheme $X'$ over $X$ is an equivalence from the category of finite, respectively finite étale, schemes over $X$
to the category of finite, respectively finite étale, analytic spaces over $X^{an}$.

Indeed, to give a finite morphism $X' \to X$, respectively $X'^{an} \to X^{an}$, is equivalent to giving a coherent
sheaf of algebras over $\mathcal{O}_{X}$, respectively over $\mathcal{O}^{an}_{X}$ [XII.4, no. 19, §5, th. 2]. The
corollary therefore follows from XII.4.4 in the non-respective case, and the respective case follows from it in view of
XII.3.1 (iii).

## 5. Comparison Theorems for Étale Coverings

<!-- label: XII.5 -->

### 5.0

<!-- label: XII.5.0 -->

Let us make precise the notion of a finite covering of an analytic space. If $\mathcal{X}$ is an analytic space, an
analytic space $\mathcal{X}'$ finite over $\mathcal{X}$ is called a finite covering of $\mathcal{X}$ if every
irreducible component of $\mathcal{X}'$ dominates an irreducible component of $\mathcal{X}$.

**Theorem (“Riemann existence theorem”).**

<!-- label: XII.5.1 -->

Let $X$ be a $\mathbb{C}$-scheme locally of finite type, and let $X^{an}$ be the analytic space associated with $X$. The
functor $\Psi$ which associates $X'^{an}$ to every finite étale covering $X'$ of $X$ is an equivalence

<!-- original page 333 -->

from the category of finite étale coverings of $X$ to the category of finite étale coverings of $X^{an}$.

1. **The functor $\Psi$ is fully faithful.** Let $X'$ and $X''$ be two finite étale coverings of $X$, and let us prove
   that the canonical map

<!-- label: eq:XII.5.* -->

$$ (*) \operatorname{Hom}_{X}(X',X'') \to \operatorname{Hom}^{an}_{X}(X'^{an},X''^{an}) $$

is bijective. We may suppose $X'$ connected. To give an $X$-morphism from $X'$ to $X''$ is equivalent to giving a
connected component $X_{i}$ of $X' \times_{X} X''$ such that the morphism $X_{i} \to X'$ induced by the first projection
is an isomorphism. Since the connected components of $X' \times_{X} X''$ correspond bijectively to the connected
components of $X'^{an} \times_{X^{an}} X''^{an}$ (XII.2.6), and since a morphism $X_{i} \to X'$ is an isomorphism if and
only if $X^{an}_{i} \to X'^{an}$ is one, this proves the bijectivity of `(*)`.

1. **The functor $\Psi$ is essentially surjective.** Let $\mathcal{X}'$ be a finite étale covering of $X^{an}$, and let
   us prove that there exists an étale covering $X'$ of $X$ such that one has an isomorphism $X'^{an} \simeq
   \mathcal{X}'$. In view of 1, the question is local on $X$, so we may suppose $X$ affine.

a. **Reduction to the case where $X$ is normal.** We may suppose $X$ reduced. Indeed, suppose the theorem proved for
$X_{red}$. The functor which associates to a finite étale covering $X'$ of $X$ the finite étale covering $X'^{an}_{red}$
of $X^{an}_{red}$ is then an equivalence. Since it is obtained by composing $\Psi$ with the functor $\Theta$ which
associates to a finite étale covering of $X^{an}$ its inverse image on $X^{an}_{red}$, and since $\Theta$ is fully
faithful, this shows that $\Psi$ is an equivalence of categories.

We

<!-- original page 334 -->

may suppose $X$ normal. Indeed, let $\tilde{X}$ be the normalization of $X$, and let $p: \tilde{X} \to X$ be the
canonical morphism. Since $p$ is finite, $p$ is a morphism of effective descent for the category of étale coverings
(IX.4.7). Supposing the theorem proved for $\tilde{X}$, put $\tilde{\mathcal{X}}' = \mathcal{X}' \times_{X^{an}}
\tilde{X}^{an}$. There exists an étale covering $\tilde{X}'$ of $\tilde{X}$ and an isomorphism $\tilde{X}'^{an} \simeq
\tilde{\mathcal{X}}'$. It then follows from 1 that the natural descent datum on $\tilde{\mathcal{X}}'$ lifts to a
descent datum on $\tilde{X}'$ relative to $\tilde{X} \to X$. This proves the existence of an étale covering $X'$ of $X$
such that one has an isomorphism

```text
i: X′^an ×_{X^an} X̃^an ≃ 𝓧̃′,
```

whose inverse images by the two projections from $\tilde{X}^{an} \times_{X^{an}} \tilde{X}^{an}$ are the same. By
IX.3.2, whose proof is valid in the analytic case, the morphism $\tilde{X}^{an} \to X^{an}$ is a morphism of descent for
the category of étale coverings, and consequently $i$ comes from an isomorphism $X'^{an} \simeq \mathcal{X}'$.

b. **Reduction to the case where $X$ is regular.** Let $U$ be the open subset of regular points of $X$, and let
$i: U \to X$ and $i^{an}: U^{an} \to X^{an}$ be the canonical morphisms. Since $X$ is normal, one has
$codim(X - U, X) \geq 2$. Suppose that there exists an étale covering $U'$ of $U$ such that
$U'^{an} \simeq \mathcal{X}'|U^{an}$, and let us show that $U'$ then extends to an étale covering $X'$ of $X$ such that
$X'^{an} \simeq \mathcal{X}'$. It is enough to see that $U'$ extends to an étale covering $X'$ of $X$. Indeed, one will
then have an isomorphism $X'^{an}|U^{an} \simeq \mathcal{X}'|U^{an}$; but if $\mathcal{F}$ and $\mathcal{G}$ are the
coherent sheaves of algebras on $\mathcal{O}^{an}_{X}$ defining respectively $\mathcal{X}'$ and $X'^{an}$, the fact that
$X$ is normal and that $codim(X - U, X) \geq 2$ implies that the canonical morphisms

```text
𝓕 → i_*^an(𝓕|U^an),     𝓖 → i_*^an(𝓖|U^an)
```

are

<!-- original page 335 -->

isomorphisms [XII.11, no. 3, prop. 4]. It follows that $\mathcal{F}$ and $\mathcal{G}$, and hence also $X'^{an}$ and
$\mathcal{X}'$, are isomorphic.

Let $\phi: X^{an} \to X$ be the canonical morphism. Since the problem of extending $U'$ to $X$ is local on $X$, it is
enough to prove that, for every point $y$ of $X^{an} - U^{an}$, the étale covering

```text
U′_φ(y) = U′ ×_X Spec 𝒪_X,φ(y)
```

of

```text
U_φ(y) = U ×_X Spec 𝒪_X,φ(y)
```

extends to $\operatorname{Spec} \mathcal{O}_{X},\phi(y)$. Let $H$ be the coherent $\mathcal{O}_{U}$-algebra defining
$U'$. The canonical morphism

```text
α: (i_*H)^an → i_*^an(H^an) = 𝓕
```

defines a morphism of sheaves of modules on $\operatorname{Spec} \mathcal{O}^{an}_{X},y$:

$$ \alpha_{y}: (i_{*}H)^{an}_{y} \to \mathcal{F}_{y}, $$

whose restriction to

```text
U_y = U_φ(y) ×_{Spec 𝒪_X,φ(y)} Spec 𝒪_X^an,y
```

is an isomorphism. But this proves that $H|U_{y}$ is trivial, hence that $U'_{\phi}(y)$ extends to $\operatorname{Spec}
\mathcal{O}_{X},\phi(y)$.

c. **The case where $X$ is affine regular.** Let

$$ j: X \to P $$

be a compactification of $X$, where $P$ is a projective $\mathbb{C}$-scheme and $j$ is a dominant open immersion. By the
resolution of singularities theorem [XII.8], one can find a regular scheme $R$ and a projective morphism $r: R \to P$,
such that $r$ induces an isomorphism $r^{-1}(X) \simeq X$ and such that $r^{-1}(X)$ is the complement in $R$ of a
divisor with normal crossings. Let

<!-- original page 336 -->

$$ k: X \to R $$

be the canonical immersion. We shall show that there exists a finite normal covering $\mathcal{R}'$ of $R^{an}$, in the
sense of XII.5.0, which extends the étale covering $X'^{an}$. By Proposition XII.5.3 below, such a covering is unique;
the problem of extending $X'^{an}$ is therefore local on $R^{an}$ near $R^{an} - X^{an}$. But each point of $R^{an} -
X^{an}$ has an open neighborhood $\mathcal{V}$ isomorphic to a ball in an affine space $\mathcal{E}^{n}$, such that
$\mathcal{V} - \mathcal{V} \cap X^{an}$ is defined by the vanishing of the first $p$ coordinate functions $z_{1},
\cdots, z_{p}$, with $0 \leq p \leq n$. The fundamental group of $\mathcal{U} = \mathcal{V} \cap X^{an}$ is isomorphic
to $\mathbb{Z}^{p}$, and every étale covering of $\mathcal{U}$ is a quotient of a covering of the form

```text
𝓤″ = 𝓤[T₁,…,T_p]/(T₁ⁿ¹ − z₁, …, T_pⁿᵖ − z_p),
```

where the $n_{i}$ are integers `> 0`, by a subgroup $H$ of the Galois group $\mathbb{Z}/n_{1}\mathbb{Z} \times \cdots
\times \mathbb{Z}/n_{p}\mathbb{Z}$ of $\mathcal{U}''$. But $\mathcal{U}''$ extends to the regular covering

```text
𝓥″ = 𝓥[T₁,…,T_p]/(T₁ⁿ¹ − z₁, …, T_pⁿᵖ − z_p)
```

of $\mathcal{V}$ on which $H$ acts, and the quotient of $\mathcal{V}''$ by $H$ is the desired extension.

The proof is then completed by XII.4.6. The covering $\mathcal{R}'$ comes from a finite covering $R'$ of $R$; the
restriction of $R'$ to $X$ is a covering $X'$ of $X$ such that $X'^{an} \simeq \mathcal{X}'$, and by XII.3.1 (iii), $X'$
is an étale covering of $X$.

**Corollary.**

<!-- label: XII.5.2 -->

Let

<!-- original page 337 -->

$X$ be a connected $\mathbb{C}$-scheme locally of finite type, let $\phi: X^{an} \to X$ be the canonical morphism, and
let $x$ be a point of $X^{an}$. Let $\pi_{1}(X^{an},x)$ be the fundamental group of the topological space $X^{an}$ at
$x$, and let $\pi_{1}(X,\phi(x))$ be the fundamental group of the scheme $X$ at $\phi(x)$ (V.7). Then
$\pi_{1}(X,\phi(x))$ is canonically isomorphic to the completion of $\pi_{1}(X^{an},x)$ for the topology of subgroups of
finite index.

Indeed, let $\mathcal{C}$ be the category of finite étale coverings of $X^{an}$, let $F$ be the functor from
$\mathcal{C}$ to Sets which associates to every finite étale covering $\mathcal{X}'$ of $X^{an}$ the set of points of
$\mathcal{X}'$ above $x$, and let $\hat{\pi}_{1}(X^{an},x)$ be the profinite group associated with $\mathcal{C}$ and $F$
as in V.4. Since every finite étale covering of $X^{an}$ is a quotient of the universal covering by a subgroup of finite
index, $\hat{\pi}_{1}(X^{an},x)$ is nothing other than the completion of $\pi_{1}(X^{an},x)$ for the topology of
subgroups of finite index. The corollary therefore follows from XII.5.1 and V.6.10.

**Proposition.**

<!-- label: XII.5.3 -->

Let $\mathcal{X}$ be a normal analytic space, and let $\mathcal{Y}$ be a closed analytic subset such that $\mathcal{U} =
\mathcal{X} - \mathcal{Y}$ is dense in $\mathcal{X}$. Then the functor which associates to every normal finite covering
$\mathcal{X}'$ of $\mathcal{X}$, in the sense of XII.5.0, its restriction to $\mathcal{U}$ is fully faithful.

Let $\mathcal{X}'$ and $\mathcal{X}''$ be two finite normal coverings of $\mathcal{X}$. We must show that the canonical
map

$$ \operatorname{Hom}_{\mathcal{X}}(\mathcal{X}',\mathcal{X}'') \to
\operatorname{Hom}_{\mathcal{U}}(\mathcal{X}'|\mathcal{U},\mathcal{X}''|\mathcal{U}) $$

is bijective. Let $u$, $v$ be two $\mathcal{X}$-morphisms from $\mathcal{X}'$ to $\mathcal{X}''$ whose restrictions to
$\mathcal{U}$ are the same, and let us prove that $u = v$. The morphisms $u$ and

<!-- original page 338 -->

$v$ coincide on the dense open $\mathcal{U} \times_{\mathcal{X}} \mathcal{X}'$, hence on the underlying topological
spaces. By [XII.4, no. 19, §4, cor. 5], this proves $u = v$.

Let now $u$ be a $\mathcal{U}$-morphism from $\mathcal{X}'|\mathcal{U}$ to $\mathcal{X}''|\mathcal{U}$, and let us show
that it extends to all of $\mathcal{X}'$. We may suppose $\mathcal{X}'$ regular. Indeed, since $\mathcal{X}'$ is normal,
one can find an open subset $\mathcal{V}$ of $\mathcal{X}$ whose complement is an analytic subset of codimension $\geq
2$, such that $\mathcal{X}' \times_{\mathcal{X}} \mathcal{V} = \mathcal{V}'$ is regular. Let $\mathcal{V}'' =
\mathcal{X}'' \times_{\mathcal{X}} \mathcal{V}$, and suppose the proposition proved for $\mathcal{V}$. Consider the
commutative diagram

```text
𝓥′  → 𝓧′
 ↓      ↓
𝓥   → 𝓧

and similarly 𝓥″ → 𝓧″ over 𝓥 → 𝓧.
```

With $u$ there is associated a morphism of $\mathcal{O}_{\mathcal{V}}$-algebras

$$ g''_{*}\mathcal{O}_{\mathcal{V}}'' \to g'_{*}\mathcal{O}_{\mathcal{V}}', $$

from which one deduces a morphism

$$ i_{*}g''_{*}\mathcal{O}_{\mathcal{V}}'' \to i_{*}g'_{*}\mathcal{O}_{\mathcal{V}}'. $$

Taking into account the isomorphisms $i'_{*}\mathcal{O}_{\mathcal{V}}' \simeq \mathcal{O}_{\mathcal{X}}'$ and
$i''_{*}\mathcal{O}_{\mathcal{V}}'' \simeq \mathcal{O}_{\mathcal{X}}''$ [XII.11, no. 3, prop. 4], one deduces a morphism
of $\mathcal{O}_{\mathcal{X}}$-algebras

$$ f''_{*}\mathcal{O}_{\mathcal{X}}'' \to f'_{*}\mathcal{O}_{\mathcal{X}}', $$

hence the desired morphism $\mathcal{X}' \to \mathcal{X}''$.

We

<!-- original page 339 -->

now suppose $\mathcal{X}'$ regular. Let $\mathcal{U}' = \mathcal{U} \times_{\mathcal{X}} \mathcal{X}'$ and $\mathcal{Y}'
= \mathcal{X}' - \mathcal{U}'$. We regard $\mathcal{Y}'$ as a reduced analytic subspace of $\mathcal{X}'$. If
$\mathcal{Y}'_{1}$ is the singular closed subset of $\mathcal{Y}'$, then $\dim \mathcal{Y}'_{1} < \dim \mathcal{Y}'$
[XII.4, no. 20 D, th. 3]. Thus, by induction on the dimension of $\mathcal{Y}'$, one may suppose $\mathcal{Y}'$ smooth.
Since it is enough to extend $u$ to an open neighborhood of each point of $\mathcal{Y}'$, the implicit function theorem
lets us suppose that $\mathcal{X}'$ is a ball in an affine space $\mathcal{E}^{n}$ and that $\mathcal{Y}'$ is the closed
subset defined by the vanishing of the first $p$ coordinate functions $z_{1}, \cdots, z_{p}$, with $0 \leq p \leq n$.

To $u$ one associates a section $s$ of

```text
p: 𝓧′ ×_𝓧 𝓧″ → 𝓧′
```

above $\mathcal{U}'$. After restricting $\mathcal{X}'$ if necessary, one may suppose that
$p_{*}(\mathcal{O}_{\mathcal{X}'\times_{\mathcal{XX}}''})$ is generated by elements $x_{1}, \cdots, x_{q}$ of
$\Gamma(\mathcal{X}', p_{*}\mathcal{O}_{\mathcal{X}'\times_{\mathcal{XX}}''})$. Let $u_{1}, \cdots, u_{q} \in
\Gamma(\mathcal{U}',\mathcal{O}_{\mathcal{X}}')$ be the images by $s$ of $x_{1}|\mathcal{U}', \cdots,
x_{q}|\mathcal{U}'$. Saying that $s$ extends to $\mathcal{X}'$ is equivalent to saying that $u_{1}, \cdots, u_{q}$
extend to sections of $\Gamma(\mathcal{X}',\mathcal{O}_{\mathcal{X}}')$. But, since $f$ is finite, each $u_{i}$ is a
Laurent series in $z_{1}, \cdots, z_{p}$ with coefficients that are convergent power series in $z_{p+1}, \cdots, z_{n}$,
and satisfies integral-dependence relations. It follows that $u_{i}$ is bounded, hence is a convergent power series in
$z_{1}, \cdots, z_{n}$, and therefore extends to $\mathcal{X}'$.

One may ask whether the functor introduced in XII.5.3 is an equivalence of categories. This question has an answer by
the theorem of Grauert-Remmert [XII.6], for which we give below a proof using resolution of singularities. One could
also have used the Grauert-Remmert theorem to prove XII.5.1; that was what was done before [XII.8] was available.

**Theorem (Grauert-Remmert theorem).**

<!-- label: XII.5.4 -->

Let

<!-- original page 340 -->

$\mathcal{X}$ be a normal analytic space, and let $\mathcal{Y}$ be a closed analytic subset such that $\mathcal{U} =
\mathcal{X} - \mathcal{Y}$ is dense in $\mathcal{X}$. Let $\mathcal{U}'$ be a normal finite covering of $\mathcal{U}$.
Suppose that there exists a rare closed analytic subset $\mathcal{S}$ of $\mathcal{X}$ such that the restriction of
$\mathcal{U}'$ to $\mathcal{U} - \mathcal{U} \cap \mathcal{S}$ is étale. Then there exists a normal finite covering
$\mathcal{X}'$ of $\mathcal{X}$ extending $\mathcal{U}'$, and $\mathcal{X}'$ is unique up to isomorphism.

Uniqueness follows from XII.5.3. The problem of extending $\mathcal{U}'$ is therefore local on $\mathcal{X}$. We may
suppose $\mathcal{U}$ regular and $\mathcal{U}'$ étale over $\mathcal{U}$. Indeed, the set of regular points of
$\mathcal{U}$ is a dense open subset $\mathcal{V}$ of $\mathcal{X}$ whose complement is an analytic subset [XII.4, no.
20 D, th. 2], and it is enough to replace $\mathcal{U}$ by the open subset $\mathcal{V} - \mathcal{V} \cap \mathcal{S}$.

Let $y$ be a point of $\mathcal{X} - \mathcal{U}$ and let us show that one can extend $\mathcal{U}'$ to a neighborhood
of $y$. After restricting $\mathcal{X}$ to an open neighborhood of $y$, it follows from the resolution of singularities
theorem [XII.8] that one can find a regular analytic space $\mathcal{X}_{1}$ and a projective morphism $f:
\mathcal{X}_{1} \to \mathcal{X}$ inducing by restriction to $\mathcal{U}$ an isomorphism $\mathcal{U}_{1} =
f^{-1}(\mathcal{U}) \simeq \mathcal{U}$, such that $\mathcal{U}_{1}$ is the complement in $\mathcal{X}_{1}$ of a divisor
with normal crossings. Let us show that $\mathcal{U}'$ extends to a normal finite covering of $\mathcal{X}_{1}$. Since
the question is local on $\mathcal{X}_{1}$, one may suppose that $\mathcal{X}_{1}$ is a ball in an affine space
$\mathcal{E}^{n}$ and that $\mathcal{X}_{1} - \mathcal{U}_{1}$ is defined by the vanishing of the first $p$ coordinate
functions $z_{1}, \cdots, z_{p}$, with $0 \leq p \leq n$.
\[Translator note: the corrected source fixes $z_{q}$ to $z_{p}$ in this list.\] The étale covering $\mathcal{U}'$ of
$\mathcal{U}_{1}$ is a quotient of a covering of the form

```text
𝓤₂ = 𝓤₁[T₁,…,T_p]/(T₁ⁿ¹ − z₁, …, T_pⁿᵖ − z_p)
```

by a subgroup $H$ of the Galois group of $\mathcal{U}_{2}$. The covering $\mathcal{U}_{2}$ extends

<!-- original page 341 -->

to the covering

```text
𝓧₂ = 𝓧₁[T₁,…,T_p]/(T₁ⁿ¹ − z₁, …, T_pⁿᵖ − z_p)
```

of $\mathcal{X}_{1}$ on which $H$ acts, and $\mathcal{X}_{2}/H$ extends $\mathcal{U}'$ to $\mathcal{X}_{1}$.

Let $\mathcal{X}'_{1}$ denote the normal finite covering of $\mathcal{X}_{1}$ extending $\mathcal{U}'$, and let
$\mathcal{F}_{1}$ be the coherent `𝒪_𝓧₁`-algebra defining $\mathcal{X}'_{1}$. By the finiteness theorem of
Grauert-Remmert [XII.4, no. 15, th. 1.1], $f_{*}\mathcal{F}_{1}$ is a coherent $\mathcal{O}_{\mathcal{X}}$-algebra. It
therefore corresponds to a finite covering $\mathcal{X}'$ of $\mathcal{X}$, which is normal since $\mathcal{X}'_{1}$ is,
and $\mathcal{X}'$ is the desired extension of $\mathcal{U}'$.

**Remark.**

<!-- label: XII.5.5 -->

In the statement XII.5.4, one cannot remove the hypothesis on the locus of points where the morphism $\mathcal{U}' \to
\mathcal{U}$ is not étale. For example, let $\mathcal{X}$ be the unit disk in the complex plane, let $\mathcal{U}$ be
the complement of the origin in $\mathcal{X}$, and let

$$ \mathcal{U}' = \mathcal{U}[T]/(T^{2} - \sin(1/z)), $$

where $z$ is the coordinate function on $\mathcal{X}$. Then $\mathcal{U}'$ is a normal finite covering of $\mathcal{U}$
which does not extend to $\mathcal{X}$. Indeed, suppose $\mathcal{U}'$ extended to a finite covering $\mathcal{X}'$ of
$\mathcal{X}$. The locus of points of $\mathcal{X}$ where the morphism $\mathcal{X}' \to \mathcal{X}$ is not étale would
then be a closed analytic subset containing all points $z$ such that $\sin(1/z) = 0$, which is absurd.

One can, however, remove the hypothesis on the singular locus of the morphism $\mathcal{U}' \to \mathcal{U}$ when
$codim(\mathcal{X} - \mathcal{U},\mathcal{X}) \geq 2$. Indeed, one may suppose $\mathcal{U}$ regular. The locus of
points of $\mathcal{U}$ where $\mathcal{U}' \to \mathcal{U}$ is not étale is a divisor of $\mathcal{U}$, and it follows
from the Remmert-Stein theorem [XII.9, th. 3] that it is

<!-- original page 342 -->

the trace on $\mathcal{U}$ of a divisor of $\mathcal{X}$. In this case, if $\mathcal{A}$ is a coherent $\mathcal{O}_{\mathcal{U}}$-algebra such that $\mathcal{U}' = \operatorname{Spec}_{an}(\mathcal{A})$, and
if $i: \mathcal{U} \to \mathcal{X}$ is the canonical morphism, it is enough to take $\mathcal{X}' = \operatorname{Spec}_{an}(i_{*}\mathcal{A})$; indeed one knows that $i_{*}\mathcal{A}$ is
coherent [XII.11, no. 1, th. 1]. \[Translator note: the corrected source fixes the adjective “coherent” to agree with
`i_*𝓐`.\]

**Remark (M. Raynaud, added in 2003).**

<!-- label: XII.5.6 -->

There exist nontrivial finitely presented groups $G$ which have no subgroups of finite index distinct from $G$, for
example G. Higman’s group; cf. J.-P. Serre, _Arbres et amalgames_, Astérisque no. 46, prop. 6, ch. I, §1. Consequently,
if such a group is realized as the topological fundamental group of a scheme $V$ over $\mathbb{C}$, say smooth and projective,
the topological space $V_{top}$ underlying $V$ is not simply connected, but $V$ is algebraically simply connected. At
present no such $V$ is known. Let us nevertheless mention that D. Toledo constructed smooth projective schemes $V$ over
$\mathbb{C}$ whose topological fundamental group is not separated for the topology of subgroups of finite index; the natural
morphism $\pi_{1}(V_{top}) \to \pi_{1}(V_{alg})$ is not injective. \[D. Toledo, “Projective varieties with non-residually finite
fundamental group,” Publ. Math. IHÉS 77 (1993), pp. 103-119.\]

## Bibliography

<!-- original page 343 -->

1. N. Bourbaki, _Topologie Générale_, Hermann, Paris, 1960.
1. N. Bourbaki, _Algèbre Commutative_, Hermann, Paris, 1961.
1. H. Cartan, Séminaire E.N.S., Paris, 1956-57.
1. H. Cartan, Séminaire E.N.S., Paris, 1960-61.
1. R. Godement, _Théorie des Faisceaux_, Hermann, Paris, 1958.
1. H. Grauert and R. Remmert, “Komplexe Räume,” Math. Ann. 136 (1958), pp. 245-318.
1. M. Hakim, _Schémas relatifs_, thesis, Paris, 1967.
1. H. Hironaka, “Resolution of singularities of an algebraic variety over a field of characteristic zero,” Ann. of Math.
   39 (1964), pp. 109-236.
1. R. Remmert and K. Stein, “Ueber die wesentlichen Singularitäten analytischer Mengen,” Math. Ann. 126 (1953), pp.
   263-306.
1. J.-P. Serre, “Géométrie algébrique et géométrie analytique,” Ann. Inst. Fourier (Grenoble) 6 (1956), pp. 1-42.
1. J.-P. Serre, “Prolongement de faisceaux analytiques cohérents,” Ann. Inst. Fourier (Grenoble) 16 (1966), pp. 363-374.
