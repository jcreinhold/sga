# Exposé II. Smooth Morphisms: Generalities, Differential Properties

<!-- label: II -->

<!-- original page 29 -->

References to Exposé I are indicated by I. Recall that rings are noetherian, and preschemes locally noetherian.

## 1. Generalities

<!-- label: II.1 -->

Let $Y$ be a prescheme, and let $t_{1},...,t_{n}$ be indeterminates. Put

```text
Y[t₁,...,t_n] = Y ⊗_ℤ ℤ[t₁,...,t_n].
```

<!-- label: eq:II.1.1 -->

Thus $Y[t_{1},...,t_{n}]$ is a $Y$-scheme, affine over $Y$, defined by the quasi-coherent sheaf of algebras
$\mathcal{O}_{Y}[t_{1},...,t_{n}]$. Giving a section of this prescheme over $Y$ is therefore equivalent to giving $n$
sections of $\mathcal{O}_{Y}$, corresponding to the images of the $t_{i}$ under the corresponding homomorphism. If $Y'$
is over $Y$, one has

```text
Y[t₁,...,t_n] ×_Y Y′ = Y′[t₁,...,t_n],
```

<!-- label: eq:II.1.2 -->

which implies that giving a $Y$-morphism from $Y'$ to $Y[t_{1},...,t_{n}]$ is equivalent to giving $n$ sections of
$\mathcal{O}_{Y'}$. On the other hand, one has

$$ (Y[t_{1},...,t_{n}])[t_{n+1},...,t_{m}] = Y[t_{1},...,t_{m}], $$

<!-- label: eq:II.1.3 -->

by the analogous formula for polynomial rings over $\mathbb{Z}$. Formula II.1.2 implies that $Y[t_{1},...,t_{n}]$ varies
functorially with $Y$.

The prescheme $Y[t_{1},...,t_{n}]$ is of finite type and flat over $Y$.

**Definition.**

<!-- label: II.1.1 -->

Let $f: X \to Y$ be a morphism, making $X$ into a $Y$-prescheme. One says that $f$ is smooth[^II-1-1] at $x \in X$, or
that $X$ is smooth over $Y$ at $x$, if there exist an integer $n \geq 0$, an open neighborhood $U$ of $x$, and an étale
$Y$-morphism from $U$ to $Y[t_{1},...,t_{n}]$. One says that $f$, respectively $X$, is smooth if it is smooth at all
points of $X$. An algebra $B$ over a ring $A$ is said to be smooth at a prime ideal $\mathfrak{p}$ of $B$ if
$\operatorname{Spec}(B)$ is smooth over $\operatorname{Spec}(A)$ at the point $\mathfrak{p}$.

<!-- original page 30 -->

The algebra $B$ is said to be smooth over $A$ if it is smooth over $A$ at every prime ideal $\mathfrak{p}$ of $B$.
Finally, a local homomorphism $A \to B$ of local rings is said to be smooth, or $B$ is said to be smooth over
$A$,[^II-1-2] if $B$ is a localization of an algebra of finite type $B_{1}$ smooth over $A$.

Note that the notion of smoothness of $X$ over $Y$ is local on $X$ and on $Y$. If $X$ is smooth over $Y$, it is locally
of finite type over $Y$.

**Proposition.**

<!-- label: prop:II.1.1 -->

The set of points $x$ of $X$ at which $f$ is smooth is open.

This is trivial from the definition.

**Corollary.**

<!-- label: II.1.2 -->

If $B$ is smooth over $A$ at $\mathfrak{p}$, then it is smooth over $A$ at every prime ideal $\mathfrak{q}$ of $B$
contained in $\mathfrak{p}$.

Proposition II.1.1 also implies that the last two definitions II.1.1 coincide on their common domain of existence.

**Proposition.**

<!-- label: II.1.3 -->

1. An étale morphism, in particular an open immersion or an identity morphism, is smooth.
1. Base extension in a smooth morphism gives a smooth morphism.
1. The composite of two smooth morphisms is smooth.

Statement (i) is trivial from the definition; more precisely, one has:

**Corollary.**

<!-- label: II.1.4 -->

étale = quasi-finite + smooth.

Statement (ii) follows immediately from the analogous fact for étale morphisms (I 4.6) and for the projections
$Y[t_{1},...,t_{n}] \to Y$; cf. II.1.2. For (iii), it follows formally from the fact that this is separately true for
“étale” (I 4.6) and for projections of the type $Y[t_{1},...,t_{n}] \to Y$, cf. II.1.3, together with the two facts
cited for (ii).

Suppose $Y$ is smooth over $Z$ and $X$ smooth over $Y$; prove that $X$ is smooth over $Z$. We may suppose $Y$ is étale
over $Z[t_{1},...,t_{n}]$ and $X$ is étale over $Y[s_{1},...,s_{m}]$. The first hypothesis therefore implies that
$Y[s_{1},...,s_{m}]$ is étale over $Z[t_{1},...,t_{n}][s_{1},...,s_{m}] = Z[t_{1},...,s_{m}]$. Hence $X$ is étale over
$Z[t_{1},...,s_{m}]$, as required.

**Remark.**

<!-- label: II.1.5 -->

The integer $n$ appearing in Definition II.1.1 is well determined, since one checks immediately

<!-- original page 31 -->

that it is the dimension of the local ring of $x$ in its fiber $f^{-1}(f(x))$. It is called the relative dimension of
$X$ over $Y$. It behaves additively under composition of morphisms.

## 2. Some Smoothness Criteria for a Morphism

<!-- label: II.2 -->

**Theorem.**

<!-- label: II.2.1 -->

Let $f: X \to Y$ be a morphism locally of finite type, let $x \in X$, and let $y = f(x)$. For $f$ to be smooth at $x$,
it is necessary and sufficient that (a) $f$ be flat at $x$, and (b) $f^{-1}(y)$ be smooth over $\kappa(y)$ at $x$.

Since the composite of two flat morphisms is flat, and $Y[t_{1},...,t_{n}] \to Y$ is flat, one sees that smooth implies
flat. Taking II.1.3(ii) into account, this proves necessity.

Suppose (a) and (b) verified. Let $V$ be an affine neighborhood of $y$ with ring $A$, and $U$ an affine neighborhood of
$x$ over $V$, with ring $B$. Taking $U$ small enough, we may suppose by (b) that there exists an étale
$\kappa(y)$-morphism

```text
g: U|f⁻¹(y) → Spec k[t₁,...,t_n],     k = κ(y),
```

defined by $n$ sections $g_{i}$ of the structural sheaf of $U|f^{-1}(y)$. One checks easily that one may suppose the
$g_{i}$, which a priori are elements of $B \otimes_{A} k = BS^{-1}$, where $S = A - \mathfrak{p}$ and $\mathfrak{p}$ is
the prime ideal of $A$ corresponding to $y$, come from sections of the structural sheaf of $U$. Thus $g$ is induced by a
morphism, still denoted $g$,

$$ g: U \to Y[t_{1},...,t_{n}], $$

after multiplying the $g_{i}$ by a common nonzero element of $k$ if necessary. Now $U$ is flat over $Y$ by (a), as is
$Y[t_{1},...,t_{n}]$; on the other hand, $g$ induces an étale morphism between the fibers over $y$. Hence $g$ is étale
at $x$ by I 5.8. This proves the assertion.

**Corollary.**

<!-- label: II.2.2 -->

Let $S$ be a prescheme, let $f: X \to Y$ be an $S$-morphism of finite type, with $Y$ of finite type and flat over $S$,
let $x \in X$, and let $s$ be the projection of $x$ to $S$. For $f$ to be smooth at $x$, it is necessary and sufficient
that $X$ be flat, or equivalently smooth, over $S$ at $x$, and that the morphism $f_{s}: X_{s} \to Y_{s}$ induced on the
fibers of $s$ be smooth at $x$.

Only sufficiency requires proof, and it follows from criterion II.2.1 together with the flatness criterion I 5.9.

<!-- original page 32 -->

To state the following result, “recall” that a morphism $f: X \to Y$ locally of finite type is said to be
equidimensional at the point $x \in X$ if, putting $y = f(x)$, one can find an open neighborhood $U$ of $x$, every
component of which dominates a component of $Y$, such that, for every $y' \in Y$, the irreducible components of
$f^{-1}(y') \cap U$ all have the same dimension independent of $y'$. In this condition it is enough, moreover, to take
$y'$ to be the generic points of the irreducible components of $Y$ passing through $y$, and the point $y$ itself.

If, for example, $X$ and $Y$ are integral and $f$ is dominant, the condition means that the components of $f^{-1}(y)$
passing through $x$ have the “right” dimension, i.e. the dimension of the generic fiber; recall that they are always at
least the dimension of the generic fiber. If $f$ is equidimensional at $x$, the dimension of its fiber at $x$ being $n$,
and if $g: U \to Y' = Y[t_{1},...,t_{n}]$ is a $Y$-morphism from a neighborhood $U$ of $x$, inducing on the fibers of
$y$ a morphism that is quasi-finite at $x$, or equivalently if $g$ is quasi-finite at $x$, then one shows that every
irreducible component of $U$ passing through $x$ dominates an irreducible component of $Y'$. Moreover, by the
“normalization lemma”, such a $g$ always exists. Conversely, if there exists a quasi-finite $Y$-morphism $g$ from an
open neighborhood $U$ of $x$ into a $Y$-scheme of the form $Y' = Y[t_{1},...,t_{n}]$, such that every component of $U$
passing through $x$ dominates a component of $Y'$, then $f$ is equidimensional at $x$. This said:

**Proposition.**

<!-- label: II.2.3 -->

Let $f: X \to Y$ be a morphism locally of finite type, let $x$ be a point of $X$, and let $y = f(x)$. Suppose
$\mathcal{O}_{y}$ is normal. For $f$ to be smooth at $x$, it is necessary and sufficient that $f$ be equidimensional at
$x$ and that $f^{-1}(y)$ be smooth over $\kappa(y)$ at $x$.

One sees immediately from the definition that a smooth morphism is equidimensional. Note that a flat morphism of finite
type is not necessarily equidimensional at $x$, even if its fiber at $x$ is irreducible. Let us prove the converse.
Since $f^{-1}(y)$ is smooth over $\kappa(y)$ at $x$, we may suppose, replacing $X$ if necessary by a suitable
neighborhood of $x$, that there exists a $Y$-morphism

```text
g: X → Y[t₁,...,t_n] = Y′
```

inducing an étale morphism on the fibers of $y$, and a fortiori quasi-finite at $x$.

<!-- original page 33 -->

Thus $g$ is unramified, and since $f$ is equidimensional at $x$, the irreducible components of $X$ passing through $x$
each dominate a component of $Y'$. A fortiori the homomorphism $\mathcal{O}_{y'} \to \mathcal{O}_{x}$ deduced from $g$,
where $y' = g(x)$, is injective. This homomorphism is moreover unramified, and $\mathcal{O}_{y'}$ is normal, since it is
a localization of the ring $\mathcal{O}_{y}[t_{1},...,t_{n}]$, which is normal because $\mathcal{O}_{y}$ is. Thus the
homomorphism $\mathcal{O}_{y'} \to \mathcal{O}_{x}$ is étale by I 9.5(ii).

**Remarks.**

<!-- label: II.2.4 -->

The preceding statement remains valid if one replaces the hypothesis that $\mathcal{O}_{y}$ is normal by the weaker
hypothesis that $Y$ is geometrically unibranch at $y$, cf. I 11, since I 9.5 is valid under this hypothesis. Let us take
the occasion to point out at the same time that if the residue field of an integral local ring $A$ is algebraically
closed, then analytically integral, i.e. `Â` is integral, implies geometrically unibranch. The converse is moreover true
in every category of “good rings”, more precisely in a category of rings stable under the usual operations and in which
the completion of a normal local ring is normal; this condition is fulfilled, by Zariski’s “analytic normality theorem”,
in the category of affine algebras and their localizations.[^II-2-1]

Finally, “recall” in the present context the following result, due to Hironaka,[^II-2-2] which sometimes makes it
possible to ensure that $f^{-1}(y)$ is a reduced scheme, i.e. that it is also what many algebraic geometers would
abusively regard as the fiber without multiplicity of $f$ over $x$, namely $f^{-1}(y)_{red}$:

**Proposition.**

<!-- label: II.2.5 -->

Let $f: X \to Y$ be a dominant morphism of finite type of reduced preschemes, and let $y$ be a point of $Y$ such that
$\mathcal{O}_{y}$ is regular. Suppose that all components of $f^{-1}(y)$ have multiplicity 1, cf. definition below, and
that $f^{-1}(y)_{red}$ is normal. Then $f^{-1}(y)$ is reduced, hence normal; $X$ is normal at all points of $f^{-1}(y)$;
and finally $X$ is flat over $Y$ at all points of $f^{-1}(y)$.

<!-- original page 34 -->

One says that a component $Z$ of $f^{-1}(y)$ has multiplicity 1 if, with $x$ denoting the generic point of $Z$, one has:
(i) $\dim \mathcal{O}_{x} = \dim \mathcal{O}_{y}$, i.e. $Z$ is not an “excess component”, in other words is not “of too
large a dimension”; (ii) the maximal ideal of $\mathcal{O}_{x}$ is generated by the maximal ideal of $\mathcal{O}_{y}$,
which a priori, by the choice of $x$, generates an ideal of definition of $\mathcal{O}_{x}$.

Taking II.2.3 or II.2.1 into account, one obtains:

**Corollary.**

<!-- label: II.2.6 -->

Let $f: X \to Y$ be a dominant morphism of finite type of reduced preschemes, and let $y$ be a point of $Y$ such that
$\mathcal{O}_{y}$ is regular. For $f$ to be smooth at the points of $X$ above $y$, it is necessary and sufficient that
the components of $f^{-1}(y)$ have multiplicity 1 and that $f^{-1}(y)_{red}$ be smooth over $\kappa(y)$.

This situation was considered especially in the past when $Y$ was the spectrum of a discrete valuation ring $A$, and was
commonly designated by phrases such as: “if the reduction of $X$ with respect to the given valuation is pretty”...
Moreover, $X$ then denoted a closed subscheme, if one may say so, of a $\mathbb{P}^{n}_{K}$, where $K$ is the field of
fractions of $A$, and for lack of an adequate language, the more intrinsic role of an object “defined over $A$”, and not
only over $K$, hardly appeared.

## 3. Permanence Properties

<!-- label: II.3 -->

**Proposition.**

<!-- label: II.3.1 -->

Let $f: X \to Y$ be a morphism, let $x \in X$, and let $y = f(x)$. Suppose $f$ is smooth at $x$. For $\mathcal{O}_{x}$
to be reduced, respectively regular, respectively normal, it is necessary and sufficient that $\mathcal{O}_{y}$ be so.

This statement is indeed known when $X$ is of the form $Y[t_{1},...,t_{n}]$, and it was proved in I, no. I.9 for an
étale morphism; the general case follows at once by Definition II.1.1.

We do not detail here the other permanence properties, which already follow from flatness alone, or from the fact that
$X$ is locally quasi-finite and flat over a $Y$-prescheme of the form $Y[t_{1},...,t_{n}]$, or, as we shall say,

<!-- original page 35 -->

that $X$ is Cohen-Macaulay over $Y$. Let us only point out that from this latter fact one obtains

```text
dim 𝒪_x = dim 𝒪_y + n − d,
depth 𝒪_x = depth 𝒪_y + n − d,
```

<!-- label: eq:II.3.1 -->

where $n$ is the dimension of the fiber of $f$ at $x$, and $d$ is the transcendence degree of $\kappa(x)$ over
$\kappa(y)$. Hence, putting `codepth = dim − depth`,[^II-3-1]

```text
codepth 𝒪_x = codepth 𝒪_y.
```

<!-- label: eq:II.3.2 -->

It follows, for example, that $\mathcal{O}_{x}$ is Cohen-Macaulay, respectively has no embedded components, if and only
if the same is true of $\mathcal{O}_{y}$.

## 4. Differential Properties of Smooth Morphisms

<!-- label: II.4 -->

For simplicity, we shall restrict ourselves essentially to differential calculus of order 1, limiting ourselves to rapid
indications for higher order, where the results are just as simple.

For the definition of the sheaf $\Omega^{1}_{X/Y}$ of 1-differentials of a $Y$-prescheme $X$, cf. I no. I.1. Suppose $X$
and $Y$ are $S$-preschemes, with structural morphism $f: X \to Y$ an $S$-morphism. Then $f$ defines a homomorphism of
modules, compatible with $f$,

$$ f*: \Omega^{1}_{Y/S} \to \Omega^{1}_{X/S}. $$

<!-- label: eq:II.4.1 -->

In other words, $\Omega^{1}_{X/S}$ is contravariant in the $S$-prescheme $X$. Moreover II.4.1 is equivalent to a
homomorphism of modules on $X$,

$$ f*(\Omega^{1}_{Y/S}) \to \Omega^{1}_{X/S}, $$

<!-- label: eq:II.4.1bis -->

also denoted $f*$ for lack of anything better, and fitting into a canonical exact sequence of module homomorphisms

$$ f*(\Omega^{1}_{Y/S}) \to \Omega^{1}_{X/S} \to \Omega^{1}_{X/Y} \to 0. $$

<!-- label: eq:II.4.2 -->

All these homomorphisms are defined by the condition of being local in nature, which reduces to the affine case, and of
commuting with the operators $d$. The exactness of II.4.2 is classical and trivial, and in the affine case it is
transcribed as the exact sequence corresponding to a homomorphism $B \to C$ of $A$-algebras:

```text
Ω¹_{B/A} ⊗_B C → Ω¹_{C/A} → Ω¹_{C/B} → 0.
```

<!-- label: eq:II.4.2bis -->

**Lemma.**

<!-- label: II.4.1 -->

<!-- original page 36 -->

Let $f: X \to Y$ be a morphism of $S$-preschemes. If $f$ is unramified, respectively étale, then

$$ f*(\Omega^{1}_{Y/S}) \to \Omega^{1}_{X/S} $$

is surjective, respectively an isomorphism. The converse is true in the unramified case, if $f$ is assumed locally of
finite type.

The unramified case follows from the exact sequence II.4.2 and from I 3.1, but can also be seen directly as in the étale
case. Consider the diagram

```text
X → X ×_Y X → X ×_S X
    ↓           ↓
    Y →       Y ×_S Y
```

in which $X \times_{Y} X$ identifies with the fiber product of $Y$ and $X \times_{S} X$ over $Y \times_{S} Y$. Since $f$
is unramified, $X \to X \times_{Y} X$ is an open immersion; hence the “conormal” sheaf of the composite immersion
$\Delta_{X/S}$ of the latter with $X \times_{Y} X \to X \times_{S} X$ is isomorphic to the inverse image on $X$ of the
conormal sheaf for the immersion $X \times_{Y} X \to X \times_{S} X$. On the other hand, since $X \to Y$ is étale, hence
flat, $X \times_{S} X \to Y \times_{S} Y$ is flat. Thus the conormal sheaf for the immersion $X \times_{Y} X \to X
\times_{S} X$ is isomorphic to the inverse image of the conormal sheaf for the immersion $Y \to Y \times_{S} Y$, i.e.
the inverse image of $\Omega^{1}_{Y/S}$. The conclusion follows.

**Lemma.**

<!-- label: II.4.2 -->

Let $X = Y[t_{1},...,t_{n}]$, with $Y$ an $S$-prescheme. Then the sequence of canonical homomorphisms

$$ 0 \to f*(\Omega^{1}_{Y/S}) \to \Omega^{1}_{X/S} \to \Omega^{1}_{X/Y} \to 0 $$

is exact, and $\Omega^{1}_{X/Y}$ is free with basis $d_{X/Y}t_{i}$.

The verification, purely affine, is immediate. Note that we already know the exactness of II.4.2.

Combining these two statements and Definition II.1.1, one finds:

**Theorem.**

<!-- label: II.4.3 -->

Let $f: X \to Y$ be a smooth morphism of $S$-preschemes. Then:

1. The sequence of canonical homomorphisms

$$ 0 \to f*(\Omega^{1}_{Y/S}) \to \Omega^{1}_{X/S} \to \Omega^{1}_{X/Y} \to 0 $$

is exact. 2. $\Omega^{1}_{X/Y}$ is locally free, and its rank $n$ at $x$ is equal to the relative dimension of $f$ at
$x$.

**Corollary.**

<!-- label: II.4.4 -->

<!-- original page 37 -->

The homomorphism

$$ f*(\Omega^{1}_{Y/S}) \to \Omega^{1}_{X/S} $$

is injective; its image in $\Omega^{1}_{X/S}$ is locally a direct factor.

Let $u: F \to G$ be a homomorphism of modules on the prescheme $X$. We say that it is **universally injective** at $x
\in X$ if the homomorphism $F_{x} \to G_{x}$ of $\mathcal{O}_{x}$-modules is injective and remains so after tensoring
with every $\mathcal{O}_{x}$-algebra, or equivalently with every $\mathcal{O}_{x}$-module. It is enough, for example,
that there exist an open neighborhood $U$ of $x$ such that $u$ induces an isomorphism from $F|U$ onto a direct factor of
$G|U$. This condition is also necessary when $F$ and $G$ are free, of finite type, in a neighborhood of $x$. More
precisely, in that case the following conditions are equivalent:

1. $u$ is injective at $x$ and `Coker u` is free at $x$.
1. There is an open neighborhood $U$ of $x$ such that $u$ induces an isomorphism from $F|U$ onto a direct factor of
   $G|U$.
1. $u$ is universally injective at $x$.
1. The induced homomorphism on the restricted fibers

```text
F_x ⊗ κ(x) → G_x ⊗ κ(x)
```

is injective. 5. The transposed homomorphism $\check{G} \to \check{F}$ is surjective at the point $x$, or equivalently
in a neighborhood of $x$.

For the circular proof, (iv) ⇒ (v) follows from Nakayama, and (v) ⇒ (i) because a locally free quotient sheaf is
necessarily a direct factor. Geometrically, the situation considered means that $u$ corresponds to an isomorphism from
the vector bundle whose sheaf of sections is $F$ onto a sub-bundle of the analogous vector bundle defined by $G$. Of
course it is not enough for this that $F \to G$ be injective.

**Corollary.**

<!-- label: II.4.5 -->

Let $f: X \to Y$ be a morphism of $S$-preschemes, locally of finite type; let $x \in X$, $y = f(x)$, and let $s$ be the
image of $x$ and $y$ in $S$. Suppose that $Y$ is smooth at $y$ over $S$. The following conditions are equivalent:

1. $f$ is smooth at $x$.
1. $X$ is smooth over $S$ at $x$, and

$$ f*(\Omega^{1}_{Y/S}) \to \Omega^{1}_{X/S} $$

is universally injective at $x$, i.e. it is an injective homomorphism at $x$ and its cokernel $\Omega^{1}_{X/Y}$ is free
at $x$.

The necessity follows from II.1.3 (iii) and II.4.3 (i), (ii). We prove the sufficiency. Since the `d g`, with $g \in
\mathcal{O}_{x}$, generate the module $\Omega^{1}_{X/Y}$ at $x$, one can find $g_{i}$, $1 \leq i \leq n$, such that the
images of the $d g_{i}$ in $(\Omega^{1}_{X/Y})_{x}$ form a basis of this module. Taking $X$ small enough, we may suppose
that the $g_{i}$ come from sections of $\mathcal{O}_{X}$, and therefore define a $Y$-morphism

```text
g: X → Y′ = Y[t₁,...,t_n].
```

Using the hypothesis and Lemma II.4.2, one easily sees that the corresponding homomorphism

$$ g*(\Omega^{1}_{Y'/S}) \to \Omega^{1}_{X/S} $$

is bijective at $x$. This reduces us to proving the following statement.

**Corollary.**

<!-- label: II.4.6 -->

Let $f: X \to Y$ be a morphism of smooth $S$-preschemes. In order that $f$ be étale at $x \in X$, it is necessary and
sufficient that

$$ f*(\Omega^{1}_{Y/S}) \to \Omega^{1}_{X/S} $$

be an isomorphism at $x$.

We know by II.4.1 that this is necessary, and the same lemma implies that this condition makes $f$ unramified at $x$. By
II.2.2, we are reduced to the case $S = \operatorname{Spec}(k)$. Since $Y$ is smooth over $k$, it is regular, hence a
fortiori normal, and by I.9.5 (ii) we are reduced to proving that $\mathcal{O}_{y} \to \mathcal{O}_{x}$ is injective, or
again that $\mathcal{O}_{y}$ and $\mathcal{O}_{x}$ have the same dimension. These dimensions are respectively the ranks
of $\Omega^{1}_{Y/k}$ and $\Omega^{1}_{X/k}$ at $y$ and $x$, hence are equal by the hypothesis.

**Remarks.**

<!-- label: II.4.7 -->

When $X$ and $Y$ are assumed smooth over $S$, the smoothness criterion II.4.5 (ii) for $f: X \to Y$ can also be stated
by saying that for every $x \in X$, the **tangent** map of $f$ at $x$, relative to the base $S$, namely the transpose of
the homomorphism of finite-dimensional $\kappa(x)$-vector spaces given by the restricted fibers of
$f*(\Omega^{1}_{Y/S})$ and $\Omega^{1}_{X/S}$ at $x$, is **surjective**. This is a very familiar hypothesis, especially
among those who work with analytic spaces. The nonsingularity hypothesis that they ordinarily impose, meaning that $X$
and $Y$ are “smooth over $\mathbb{C}$”, cf. II.5, seems due only to the fear still inspired in many geometers by
singular points of algebraic varieties or analytic spaces.

Let us point out the following special case of II.4.6.

**Corollary.**

<!-- label: II.4.8 -->

Let $X$ be an $S$-prescheme, let $g: X \to S[t_{1},...,t_{n}]$ be an $S$-morphism defined by sections $g_{i}$, $1 \leq i
\leq n$, of $\mathcal{O}_{X}$, and let $x$ be a point of $X$ such that $X$ is smooth over $S$ at $x$. In order that $g$
be étale at $x$, it is necessary and sufficient that the $d g_{i}$, $1 \leq i \leq n$, form a basis of
$\Omega^{1}_{X/S}$ at $x$; equivalently, that their images in

```text
Ω¹_{X/S}(x) = (Ω¹_{X/S})_x ⊗_{𝒪_x} κ(x)
```

<!-- original page 39 -->

form a basis of this vector space over $\kappa(x)$.

Let $X$ be a prescheme, and let $Y$ be a closed sub-prescheme of $X$ defined by a coherent sheaf $\mathcal{J}$ of
ideals. Thus $\mathcal{J}/\mathcal{J}^{2}$ may be regarded as a coherent sheaf on $Y$, the **conormal sheaf** of $Y$ in
$X$. If now $X$ is an $S$-prescheme, there is a canonical exact sequence of quasi-coherent sheaves on $Y$

```text
𝒥/𝒥² --d→ Ω¹_{X/S} ⊗_{𝒪_X} 𝒪_Y → Ω¹_{Y/S} → 0.
```

<!-- label: eq:II.4.3 -->

Its right-hand part is just II.4.2, with the roles of $X$ and $Y$ interchanged and taking into account that
$\Omega^{1}_{Y/X} = 0$, while the homomorphism $\mathcal{J}/\mathcal{J}^{2} \to \Omega^{1}_{X/S}
\otimes_{\mathcal{O}_{X}} \mathcal{O}_{Y}$ is obtained from the, in general nonlinear, homomorphism $g \mapsto d g$ by
passing to quotients. The exactness of II.4.3 is classical and in any case trivial; in the affine case it is interpreted
by the following exact sequence, corresponding to a surjective homomorphism $B \to C$ of $A$-algebras, with kernel $J$:

```text
J/J² → Ω¹_{B/A} ⊗_B C → Ω¹_{C/A} → 0,     C = B/J.
```

<!-- label: eq:II.4.3bis -->

This exact sequence had already been used implicitly in the proof of I.7.2.

**Proposition.**

<!-- label: II.4.9 -->

Let $X$ be an $S$-prescheme, let $Y$ be a closed sub-prescheme of $X$ defined by a coherent sheaf $\mathcal{J}$ of
ideals on $X$, let $x$ be a point of $X$, let $g_{i}$, $1 \leq i \leq n$, be sections of $\mathcal{O}_{X}$ defining an
$S$-morphism

```text
g: X → S[t₁,...,t_n] = X′,
```

and finally let $p$ be an integer, $0 \leq p \leq n$. Suppose that $X$ is **smooth over $S$ at $x$**. The following
conditions are equivalent:

1. There is an open neighborhood $X_{1}$ of $x$ in $X$ such that $g|X_{1}$ is **étale** and such that $Y_{1} = Y \cap
   X_{1}$, the trace of $Y$ on $X_{1}$, is the **inverse image** of the closed sub-prescheme $Y' = S[t_{p+1},...,t_{n}]$
   of $X' = S[t_{1},...,t_{n}]$; equivalently, the $g_{i}$, $1 \leq i \leq p$, generate $\mathcal{J}|X_{1}$:

$$ Y_{1} \to X_{1} \downarrow \downarrow \acute{e}tale Y' \to X' $$

1. $Y$ is **smooth over $S$ at $x$**, the $g_{i}$, $1 \leq i \leq p$, define **elements of** $\mathcal{J}_{x}$, the $d
   g_{i}(x)$, $1 \leq i \leq n$, form a **basis of** $\Omega^{1}_{X/S}(x)$ over $\kappa(x)$, and the $d g'_{i}(x)$, $p +
   1 \leq i \leq n$, form a **basis of** $\Omega^{1}_{Y/S}(x)$ over $\kappa(x)$, where the $g'_{i}$ denote the
   restrictions of the $g_{i}$ to $Y$; the differentials are taken relative to $S$.
1. The $g_{i}$, $1 \leq i \leq p$, define a **system of generators** of $\mathcal{J}_{x}$, and the $d g_{i}(x)$, $1 \leq
   i \leq n$, form a **basis of** $\Omega^{1}_{X/S}(x)$ over $\kappa(x)$.
1. $Y$ is **smooth over $S$** at $x$, the $g_{i}$, $1 \leq i \leq p$, form a **minimal system of generators of**
   $\mathcal{J}_{x}$, and the $d g'_{i}(x)$, $p + 1 \leq i \leq n$, form a **basis of** $\Omega^{1}_{Y/S}(x)$ over
   $\kappa(x)$.

Moreover, under these conditions, $\mathcal{J}/\mathcal{J}^{2}$ is a free module on $Y$ at $x$, having as **basis at
$x$** the classes of the $g_{i}$, $1 \leq i \leq p$, and the canonical homomorphism

$$ \mathcal{J}/\mathcal{J}^{2} \to \Omega^{1}_{X/S} \otimes \mathcal{O}_{Y} $$

is **universally injective at $x$**.

**Remark.** This implies that $p$ is well determined by the other conditions, either as the **rank** of the free module
$\mathcal{J}/\mathcal{J}^{2}$ on $Y$ at $x$, or again as the **minimum number of generators** of $\mathcal{J}_{x}$ on
$X$, or finally by the fact that the relative dimension of $Y$ relative to $S$ at $x$ is $n - p$.

**Proof.** Suppose first that (i) holds. Then by I.4.6 (iii), $Y_{1}$ is étale over $Y'$; hence by definition it is
smooth over $S$ at $x$, of relative dimension $n - p$, and the same is therefore true of $Y$. It then follows from
II.4.8 that the $d g_{i}$, $1 \leq i \leq n$, form a basis of $\Omega^{1}_{X/S}$ at $x$, and that the $d g'_{i}$, $p + 1
\leq i \leq n$, form a basis of $\Omega^{1}_{Y/S}$ at $x$. By the exact sequence II.4.3, it follows that the $g_{i}$, $1
\leq i \leq p$, are linearly independent in $\mathcal{J}/\mathcal{J}^{2}$, considered as a module on $Y$, at $x$. Since
the $g_{i}$, $1 \leq i \leq p$, generate $\mathcal{J}_{x}$, it follows that the $g_{i}$ modulo $\mathcal{J}^{2}_{x}$
form a **basis of** $\mathcal{J}/\mathcal{J}^{2}$ at $x$. This implies, on the one hand, that the $g_{i}$, $1 \leq i
\leq p$, form a **minimal** system of generators of $\mathcal{J}_{x}$, and, on the other hand, that the homomorphism
$\mathcal{J}/\mathcal{J}^{2} \to \Omega^{1}_{X/S} \otimes \mathcal{O}_{Y}$ in II.4.3 is universally injective at $x$,
since it sends a basis of a module free at $x$ to part of a basis of a module free at $x$; note that these are
$Y$-modules. This proves that (i) implies (ii), (iii), (iv), as well as the last assertions of Proposition I.4.9.

(iii) implies (i) by Corollary I.4.8.

<!-- original page 41 -->

(ii) implies (i). Indeed, the first hypothesis in (ii) means that, after replacing $X$ by an open neighborhood of $x$ in
$X$, $g$ induces a morphism $h: Y \to Y'$. By II.4.8, the two other hypotheses in (ii) mean that $g$ is étale at $x$ and
$h$ is étale at $x$. Let $Y''$ be the inverse image of $Y'$ by $g$. Then $Y$ is a closed sub-prescheme of $Y''$, which
is étale over $Y'$ at $x$ by I.4.6 (iii), since $g$ is étale at $x$. Thus the immersion morphism $Y \to Y''$ is itself
étale by I.4.8, hence is an open immersion by I.5.8 or I.5.2. Replacing $X$ again by a suitable open neighborhood
$X_{1}$ of $x$, we obtain (i).

The preceding establishes the equivalence of conditions (i), (ii), (iii), and the fact that they imply (iv). It remains
to prove that (iv) ⇒ (ii), which is immediate, taking into account that $\Omega^{1}_{X/S}$ is free on $X$ at $x$, once
one knows that the fact that $Y$ is smooth over $S$ at $x$ implies that $\mathcal{J}/\mathcal{J}^{2}$ is free on $Y$ at
$x$ and that the homomorphism

$$ \mathcal{J}/\mathcal{J}^{2} \to \Omega^{1}_{X/S} \otimes \mathcal{O}_{Y} $$

is universally injective at $x$. This last point is included in the following theorem.

**Theorem.**

<!-- label: II.4.10 -->

Let $X$ be a smooth $S$-prescheme, let $Y$ be a closed sub-prescheme of $X$ defined by a coherent sheaf $\mathcal{J}$ of
ideals on $X$, and let $x$ be a point of $X$. The following conditions are equivalent:

1. $Y$ is **smooth over $S$ at $x$**.
1. There is an open neighborhood $X_{1}$ of $x$ in $X$ and an **étale** $S$-morphism

```text
g: X₁ → X′ = S[t₁,...,t_n]
```

such that $Y_{1} = Y \cap X_{1}$, the trace of $Y$ on $X_{1}$, is the sub-prescheme of $X_{1}$ that is the **inverse
image** under $g$ of the closed sub-prescheme $Y' = S[t_{p+1},...,t_{n}]$ of $X' = S[t_{1},...,t_{n}]$, for a suitable
$p$. 3. There are **generators $g_{i}$, $1 \leq i \leq p$, of $\mathcal{J}_{x}$** such that the $d g_{i}$ form part of a
basis of $\Omega^{1}_{X/S}$ at $x$; equivalently, such that the $d g_{i}(x)$ in $\Omega^{1}_{X/S}$ are linearly
independent over $\kappa(x)$. 4. The sheaf $\mathcal{J}/\mathcal{J}^{2}$ is free on $Y$ at $x$, and the canonical
homomorphism

```text
d: 𝒥/𝒥² → Ω¹_{X/S} ⊗ 𝒪_Y
```

is universally injective at $x$; or again, the sequence of canonical homomorphisms

```text
0 → 𝒥/𝒥² → Ω¹_{X/S} ⊗ 𝒪_Y → Ω¹_{Y/S} → 0
```

is exact at $x$, and $\Omega^{1}_{Y/S}$ is locally free at $x$.

**Proof.** We already know from the preceding that (ii) implies (i), (iii), and (iv). We prove (i) ⇒ (ii), which will at
the same time finish the proof of I.4.9. By Theorem II.4.3 (ii), the last two terms in the exact sequence II.4.3 are
free modules on $Y$. Thus, since the images in $\Omega^{1}_{X/S} \otimes_{\mathcal{O}_{X}} \mathcal{O}_{Y}$ of the
`d g`, for $g \in \mathcal{O}_{X}$, generate this module at $x$, hence their images in $\Omega^{1}_{Y/S}$ generate the
latter at $x$, one can find $g_{i}$, $p + 1 \leq i \leq n$, in $\mathcal{O}_{X}$ such that the $d g'_{i}$ form a basis
of $\Omega^{1}_{Y/S}$. Then, by exactness of II.4.3, one can complete the system of the $d g_{i}$, $p + 1 \leq i \leq
n$, to a basis of the middle term by elements of the form $d g_{i}$, $1 \leq i \leq n$, where the $g_{i}$, $1 \leq i
\leq p$, **belong to $\mathcal{J}_{x}$**. The $g_{i}$ come from sections of $\mathcal{O}_{X}$ on a neighborhood of $x$
in $X$, which we may suppose equal to $X$. We are then under the conditions of II.4.8 (ii), and we have established that
these imply condition II.4.8 (i), whence II.4.10 (ii).

The implication (iii) ⇒ (ii) in II.4.10 follows at once from the implication (iii) ⇒ (i) in II.4.8. Thus (i), (ii),
(iii) are equivalent and imply (iv). Finally, it is trivial that (iv) implies (iii), taking into account that elements
$g_{i} \in \mathcal{J}_{x}$ whose classes form a basis of $\mathcal{J}_{x}$ modulo $\mathcal{J}^{2}_{x}$ generate
$\mathcal{J}_{x}$ by Nakayama.

Moreover, the preceding proof shows the following.

**Corollary.**

<!-- label: II.4.11 -->

Let $X$ be an $S$-prescheme, let $Y$ be a closed sub-prescheme defined by a coherent sheaf $\mathcal{J}$ of ideals on
$X$, and let $x$ be a point of $Y$. Suppose that **$X$ and $Y$ are smooth over $S$ at $x$**. Let $g_{i}$ be sections of
$\mathcal{J}$, $1 \leq i \leq p$. The following conditions are equivalent:

1. The $g_{i}$ **generate** $\mathcal{J}_{x}$ and the $d g_{i}(x)$ are **linearly independent** in $\Omega^{1}_{X/S}(x)$
   over $\kappa(x)$.
1. The $g_{i}$ modulo $\mathcal{J}^{2}$ form a basis of $\mathcal{J}/\mathcal{J}^{2}$ at $x$.
1. The $g_{i}$ form a minimal system of generators of $\mathcal{J}_{x}$.
1. One can find other sections $g_{i}$, $p + 1 \leq i \leq n$, of $\mathcal{O}_{X}$ on a neighborhood $X_{1}$ of $x$,
   defining together with the preceding ones an **étale** morphism $X_{1} \to X' = S[t_{1},...,t_{n}]$ such that $Y_{1}
   = Y \cap X_{1}$ is the **inverse image** under $g$ of the closed sub-prescheme $Y' = S[t_{p+1},...,t_{n}]$ of $X' =
   S[t_{1},...,t_{n}]$.

<!-- original page 43 -->

In particular:

**Corollary.**

<!-- label: II.4.12 -->

Let $X$ be an $S$-prescheme, let $F$ be a section of $\mathcal{O}_{X}$, let $Y$ be the sub-prescheme of the zeros of
$F$, defined by the coherent ideal $F\cdot \mathcal{O}_{X}$, and let $x$ be a point of $Y$. Suppose that $X$ is smooth
over $S$ at $x$. In order that $Y$ be smooth over $S$ at $x$, it is necessary and sufficient that either $F$ be zero in
a neighborhood of $x$, or $dF(x) \neq 0$, where $dF(x)$ denotes the image of `dF` in the vector space
$\Omega^{1}_{X/S}(x)$ over $\kappa(x)$.

This is sufficient by criterion (iii) of II.4.10. It is necessary, because since $\mathcal{J}$ is generated by one
element, it is first necessary that $\mathcal{J}/\mathcal{J}^{2}$ at the point $x$ be free of rank $\leq 1$. If this
rank is 0, i.e. if $\mathcal{J}/\mathcal{J}^{2} = 0$ at $x$, it follows that $\mathcal{J} = 0$ at $x$ by Nakayama, i.e.
$F$ is zero in a neighborhood of $x$. If this rank is 1, then $F$ forms a minimal system of generators of $\mathcal{J}$
at $x$, and one concludes by II.4.11, equivalence of (i) and (iii).

**Corollary.**

<!-- label: II.4.13 -->

Let $Y$ be an $S$-prescheme locally of finite type, let $S'$ be a **flat** $S$-prescheme, let $Y' = Y \times_{S} S'$,
let $x'$ be a point of $Y'$, and let $x$ be its canonical image in $Y$. In order that $Y$ be smooth over $S$ at $x$, it
is necessary and sufficient that $Y'$ be smooth over $S'$ at $x'$. In particular, if $S' \to S$ is flat and surjective,
$Y$ is smooth over $S$ if and only if $Y'$ is smooth over $S'$.

Only the sufficiency has to be proved; the necessity was seen in II.1.3 (ii). We may suppose, after replacing $Y$ by a
suitable neighborhood of $x$ and $Y'$ by its inverse image, that $Y$ is affine of finite type over affine $S$; hence $Y$
is isomorphic to a closed sub-prescheme of a scheme $S[t_{1},...,t_{n}]$. It follows that $Y'$ identifies with a closed
sub-prescheme of $X' = X \times_{S} S'$. Since $X$ is smooth over $S$, and hence $X'$ is smooth over $S'$, the
smoothness criteria II.4.10 may be applied. Here criterion (iv) gives the result at once.

**Remarks.**

<!-- label: II.4.14 -->

Criterion (iii) of Theorem II.4.10 deserves to be called the **Jacobian criterion for smoothness**. It makes it
possible, theoretically, to recognize whether a given $S$-prescheme $Y$ is smooth over $S$ at a point $x$ of $Y$, since
there is always a neighborhood of $Y$ isomorphic to a sub-prescheme of a smooth $S$-prescheme $X$, for instance $X =
S[t_{1},...,t_{n}]$. It is indeed for $X = S[t_{1},...,t_{n}]$, $S = \operatorname{Spec}(A)$, that the Jacobian
criterion is usually stated; of course, in the classical case considered by Zariski, $A$ was a field. We leave it to the
reader to give the statement, to which one is thus led, in terms of an ideal $J$ of $A[t_{1},...,t_{n}]$ and a prime
ideal containing it. Let us note that at present it seems, especially since Nagata succeeded in generalizing by
non-differential methods Zariski's theorem saying that the set of regular points of an algebraic scheme is open, that
the Jacobian criterion has scarcely any interest except in the form in which we give it here, i.e. using exclusively
**relative** differentials and not **absolute** differentials, i.e. differentials relative to the absolute ring of
constants $\mathbb{Z}$. As very often, considering differentials is more convenient here than considering derivations.
Finally, note that if $Y$ is smooth over $S$ at $x$, of relative dimension $m$, then there is an open neighborhood of
$x$ in $Y$ isomorphic to a sub-prescheme of $X = S[t_{1},...,t_{n}]$ with $n = m + 1$, as follows from the definition
and from I.7.6.

Let $A$ be a noetherian ring, let $x_{i}$, $1 \leq i \leq n$, be elements of $A$, and let $J$ be the ideal generated by
the $x_{i}$. We say that the $x_{i}$ form a **regular system of generators** of $J$ if the canonical surjective
homomorphism

$$ (A/J)[t_{1},...,t_{n}] \to gr^{J}(A) $$

defined by the $x_{i}$, where the second member denotes the graded ring associated with $A$ filtered by the powers of
$J$, is an **isomorphism**. This condition also means that:

1. The canonical surjective homomorphism

$$ S_{A/J}(J/J^{2}) \to gr^{J}(A), $$

where the first member denotes the symmetric algebra of the $A/J$-module $J/J^{2}$, is an isomorphism. 2. $J/J^{2}$ is
free and has as basis the classes of the $x_{i}$ modulo $J^{2}$.

In this form one sees that if $J \neq A$, the $x_{i}$ form a **minimal system of generators** of $J$, and that **every
other minimal system of generators** of $J$ **is a regular system of generators**. Here “minimal” is taken in the strict
sense: minimum number of elements, which is equivalent to minimality for inclusion only if $A$ is local. On the other
hand, if $J = A$, every system of generators of $J$ is regular.

<!-- original page 45 -->

The regularity condition for a system of generators of an ideal is stable under localization by an arbitrary
multiplicatively stable set. Moreover, one sees immediately that, in order for $(x_{i})$ to be a minimal system of
generators of $J$, it already suffices that for every **maximal ideal $\mathfrak{m}$ containing $J$**, the $x_{i}$
define a regular system of generators of $J A_{\mathfrak{m}}$ in $A_{\mathfrak{m}}$. We are therefore reduced to the
case where $A$ is a local ring with maximal ideal $\mathfrak{m}$, and where the $x_{i}$ are in $\mathfrak{m}$. **Then
the $x_{i}$ form a regular system of generators of $J$ if and only if they form an $A$-sequence in the sense of Serre**,
that is, if for every $i$ with $1 \leq i \leq n$, $x_{i}$ is not a zero-divisor in $A/(x_{1},...,x_{i-1})A$.[^ii-4-14-1]

Finally, in the case where $A$ is an algebra over a ring $B$, and where $A/J$ is isomorphic as a $B$-algebra to $B$, so
that $J$ is the kernel of a homomorphism of $B$-algebras $A \to B$, the $x_{i}$ form a regular system of generators of
$J$ if and only if the canonical homomorphism

$$ B[[t_{1},...,t_{n}]] \to \hat{A} $$

defined by the $x_{i}$, where the second member denotes the separated completion $\lim A/J^{n+1}$ of $A$ for the
topology defined by the powers of $J$, is an **isomorphism**; it is in any case **surjective**.

All these facts are well known and, no doubt with minor differences, appear in Serre's course on commutative algebra
written up by Gabriel, where one finds N other characterizations of $A$-sequences in the case where $A$ is a local ring.

Let $J$ be an ideal in a noetherian ring $A$. We shall say that $J$ is a **regular ideal** if, for every prime ideal
$\mathfrak{p}$ of $A$, $J A_{\mathfrak{p}}$ admits a regular system of generators. It is of course enough to verify this
for $\mathfrak{p} \supset J$, and one may furthermore restrict to maximal $\mathfrak{p}$. More generally, let
$\mathcal{J}$ be an ideal on a locally noetherian prescheme $X$. We say that $\mathcal{J}$ is a **regular ideal** if,
for every $x \in X$, $\mathcal{J}_{x}$ is an ideal of $\mathcal{O}_{x}$ admitting a regular system of generators. This
is equivalent to the conjunction of the following two conditions:

1. The canonical surjective homomorphism

$$ S_{\mathcal{O}_{X}/\mathcal{J}}(\mathcal{J}/\mathcal{J}^{2}) \to gr^{\mathcal{J}}(\mathcal{O}_{X}) $$

is an isomorphism. 2. The sheaf of $\mathcal{O}_{X}/\mathcal{J}$-modules $\mathcal{J}/\mathcal{J}^{2}$ is locally free.

<!-- original page 46 -->

One also then says that the sub-prescheme $Y$ of $X$ defined by $\mathcal{J}$, so that $\mathcal{O}_{Y}$ extended by 0
is isomorphic to $\mathcal{O}_{X}/\mathcal{J}$, is **regularly immersed** in $X$. In the same evident way one defines
the notion of a morphism that is a **regular immersion**, respectively **regular at a point $x$**: an immersion morphism
$Y \to X$ identifying $Y$, respectively a suitable neighborhood of $x$, with a closed sub-prescheme regularly immersed
in an open of $X$. One should not say “regular sub-prescheme”, since that would mean that the local rings of $Y$ are
regular. Finally, sections $x_{i}$ of $\mathcal{J}$ are called a **regular system of generators** if, for every $x \in
X$, the corresponding elements of $\mathcal{O}_{x}$ form a regular system of generators of $\mathcal{J}_{x}$; this
terminology is compatible with that introduced for generators of an ideal of a ring. This also means that the canonical
surjective homomorphism

$$ \mathcal{O}_{Y}[t_{1},...,t_{n}] \to gr^{\mathcal{J}}(\mathcal{O}_{X}) $$

defined by the $x_{i}$ is an isomorphism. If one knows in advance that the ideal $\mathcal{J}$ is regular, this simply
means that at every point $x$ **of $Y$**, the $x_{i}$ define a **basis** of $\mathcal{J}/\mathcal{J}^{2}$ over
$\mathcal{O}_{Y,x}$. This condition is empty if $Y$ is empty. Thus, in order that $\mathcal{J}$ admit a regular system
of generators, it is necessary and sufficient that $\mathcal{J}$ be regular and that the $\mathcal{O}_{Y}$-module
$\mathcal{J}/\mathcal{J}^{2}$ be globally free, not merely locally free; that is, that the canonical homomorphism
$S_{\mathcal{O}_{Y}}(\mathcal{J}/\mathcal{J}^{2}) \to gr^{\mathcal{J}}(\mathcal{O}_{X})$ be surjective and that the
$\mathcal{O}_{Y}$-module $\mathcal{J}/\mathcal{J}^{2}$ be globally free.

An **augmented ring is said to be regular** if the ideal of augmentation is regular. Thus, if $A$ is a local ring,
regarded as augmented into its residue field $k$, then $A$ is a regular local ring if and only if it is a regular
augmented ring.

To tell the truth, it seems that it was unnecessary to begin by making the preliminary sorites for rings; there is some
advantage in starting with sheaves at once. If one wants something in the noetherian case, it is the definition adopted
here, a priori less strict than Serre's definition by $A$-sequences, that seems preferable for the needs of differential
calculus. Of course, to do the job properly, one would also have to develop at least part of the theory of smooth
morphisms in the non-noetherian setting,[^ii-4-14-2] probably by starting from the Jacobian criterion, so as to obtain
if possible all the essential formal properties of smooth morphisms and of étale morphisms, i.e. smooth and quasi-finite
morphisms; only the converses would appeal to noetherian hypotheses.

After these long terminological preliminaries, a small theorem:

**Theorem.**

<!-- label: II.4.15 -->

Let $X$ be an $S$-prescheme locally of finite type, let $Y$ be a closed sub-prescheme of $X$ defined by a coherent sheaf
$\mathcal{J}$ of ideals on $X$, and let $x$ be a point of $X$. We now suppose **$Y$ smooth over $S$ at $x$**, and assume
nothing about $X$. Then the following conditions are equivalent:

1. $X$ is smooth over $S$ at $x$.
1. The immersion $i: Y \to X$ is regular at $x$, i.e. $\mathcal{J}_{x}$ is a regular ideal of $\mathcal{O}_{x}$.

**Corollary.**

<!-- label: II.4.16 -->

Suppose $Y$ is **smooth** over $S$. In order that $X$ be smooth over $S$ in a neighborhood of $Y$, i.e. at the points of
$Y$, it is necessary and sufficient that $Y$ be regularly embedded in $X$, i.e. that the immersion $i: Y \to X$ be
regular.

**Proof.** (i) implies (ii). Apply criterion (ii) of II.4.10. Since $g: X_{1} \to X$ is **flat**, in order to show that
the inverse image by $g$ of the sub-prescheme $Y'$ of $X'$ is regularly embedded, we are reduced to proving that $Y' =
S[t_{p+1},...,t_{n}]$ is regularly embedded in $S[t_{1},...,t_{n}]$, which is trivial: the $t_{i}$, $1 \leq i \leq p$,
form a regular system of generators of the ideal defining $Y'$ in $X'$.

(ii) implies (i). Let $g_{i}$, $1 \leq i \leq p$, be a regular system of generators of $\mathcal{J}_{x}$, and let
$g_{i}$, $p + 1 \leq i \leq n$, be elements of $\mathcal{O}_{X,x}$ such that their images $g'_{i}$ in
$\mathcal{O}_{Y,x}$ define an **étale** morphism

$$ Y_{1} \to Y' = S[t_{p+1},...,t_{n}] $$

from a neighborhood $Y_{1}$ of $x$ in $Y$. The $g_{i}$, $1 \leq i \leq n$, come from sections, denoted by the same
names, of $\mathcal{O}_{X}$ on a neighborhood $X_{1}$ of $x$, and we may suppose $X_{1} = X$ and $Y_{1} = Y$. We thereby
obtain a morphism

```text
g: X → X′ = S[t₁,...,t_n],
```

and everything comes down to showing that this morphism is **étale** at $x$. Taking $X_{1}$ small enough, we may suppose
that the $g_{i}$, $1 \leq i \leq p$, form a regular system of generators of $\mathcal{J}$ on all of $X$. In particular,
they generate $\mathcal{J}$, so the sub-prescheme $Y$ of $X$ identifies with the inverse image by $g$ of the
sub-prescheme $Y'$ of $X'$. Let $x' = g(x)$. Then the fiber of $X \to X'$ at $x'$ is identical with the fiber of $Y \to
Y'$ at $x$, hence is étale over $\kappa(x')$, and therefore $g$ is **unramified** at $x$. It remains to prove that $g$
is **flat** at $x$. The graded ring associated with $\mathcal{O}_{X',x'}$, filtered by the powers of
$\mathcal{J}'_{x'}$, is **free** over $\mathcal{O}_{Y',x'}$ in every degree; on the other hand, the graded ring
associated with $\mathcal{O}_{X,x}$, filtered by the powers of $\mathcal{J}_{x} = \mathcal{J}'_{x} \mathcal{O}_{X,x}$,
is isomorphic, under the canonical homomorphism, to the tensor product of the preceding one with $\mathcal{O}_{Y,x}$,
since both rings are polynomial rings in $n - p$ indeterminates with rings of constants $\mathcal{O}_{Y',x'}$ and
$\mathcal{O}_{Y,x}$, respectively. Finally, over $\mathcal{O}_{X',x'}/\mathcal{J}'_{x'} = \mathcal{O}_{Y',x'}$, the
quotient $\mathcal{O}_{X,x}/\mathcal{J}_{x} = \mathcal{O}_{Y,x}$ is flat.

By a general flatness criterion, valid for a local homomorphism of noetherian local rings $A' \to A$, where $A'$ is
equipped with an ideal $J' \neq A'$ whose associated graded ring is free over $A'/J'$ in every dimension, it follows
that $X$ is flat over $X'$ at $x$, as required.

**Corollary.**

<!-- label: II.4.17 -->

Let $X$ be a prescheme locally of finite type over $Y$, let $i$ be a section of $X$ over $Y$, let $y$ be a point of $Y$,
let $x = i(y)$, and let $\mathcal{J}$ be the sheaf of ideals on $X$ defined by the sub-prescheme $i(Y)$, which we
suppose closed in order to simplify the statement, a condition satisfied if $X$ is a scheme.

The following conditions are equivalent:

1. $X$ is smooth over $Y$ at $x$.
1. $i$ is a regular immersion at $y$.
1. The $\mathcal{O}_{y}$-algebra obtained by completing $\mathcal{O}_{x}$ for the topology defined by the powers of
   $\mathcal{J}_{x}$ is isomorphic to a formal power-series algebra $\mathcal{O}_{y}[[t_{1},...,t_{n}]]$.
1. There is an open neighborhood $U$ of $y$ such that the sheaf of algebras $\lim i*(\mathcal{O}_{X}/\mathcal{J}^{n+1})$
   on $\mathcal{O}_{Y}$ is isomorphic over $U$ to a sheaf of the form $\mathcal{O}_{Y}[[t_{1},...,t_{n}]]$.
1. There is an open neighborhood $U$ of $y$, an open neighborhood $V$ of $x$, and finally a $Y$-morphism $g: V \to
   U[t_{1},...,t_{n}]$, such that $g$ is étale, such that $i$ induces a section of $V$ over $U$, and such that $g$
   carries this section to the zero section of $U[t_{1},...,t_{n}]$ over $U$.

The equivalence of (i) and (ii) is a special case of Theorem II.4.15, taking $Y = S$. The equivalence of (ii) and (iii),
and morally of (ii) and (iii bis), was indicated in the “reminders”. As for the equivalence of (i) and (iv), it follows
easily from Theorem II.4.10, namely from the equivalence of conditions (i) and (ii) there.

**Corollary.**

<!-- label: II.4.18 -->

Let $X$ be a prescheme smooth over $S$. Then the diagonal morphism

```text
Δ_{X/S}: X → X ×_S X
```

is a **regular immersion**, or, as one also says, $X$ is “**differentially smooth**” over $S$.

Indeed, this is a special case of Corollary II.4.16, since $X$ and $X \times_{S} X$ are both smooth over $S$.

**Remarks.**

<!-- label: rem:II.4.18 -->

Recall from I.1 that if $X$ is a prescheme over $S$, one introduces the quasi-coherent sheaves of algebras

```text
𝒫ⁿ_{X/S} = 𝒪_{X ×_S X}/𝓘_X^{n+1}
```

on $X$, where $\mathcal{I}_{X}$ denotes the sheaf of ideals defining the diagonal in $X \times_{S} X$, regarded as a
sheaf of $\mathcal{O}_{X}$-algebras through the first projection $pr_{1}: X \times_{S} X \to X$. The
$\mathcal{P}^{n}_{X/S}$ form a projective system of algebras on $X$, whose projective limit is denoted
$\mathcal{P}^{\infty}_{X/S}$; it is nothing other than the structure sheaf of the formal completion of $X \times_{S} X$
along the diagonal, now supposing $X$ locally of finite type over $S$, hence the $\mathcal{P}^{n}_{X/S}$ coherent. To
say that $X$ is differentially smooth over $S$, i.e. that the diagonal morphism $\Delta_{X/S}$ is a regular immersion,
also means that $\mathcal{P}^{\infty}_{X/S}$ is regular as a sheaf of augmented algebras toward $\mathcal{O}_{X}$, i.e.
that $\Omega^{1}_{X/S}$ is locally free and the canonical surjective homomorphism

$$ S_{\mathcal{O}_{X}}(\Omega^{1}_{X/S}) \to gr_{*}(\mathcal{P}^{\infty}_{X/S}) $$

is an isomorphism; or finally that every point of $X$ has an open neighborhood on which the sheaf of augmented algebras
$\mathcal{P}^{\infty}_{X/S}$ is isomorphic to a sheaf $\mathcal{O}_{X}[[t_{1},...,t_{n}]]$.

Let $s$ be a section of $X$ over $S$, and let $\mathcal{J}$ be the sheaf of ideals on $X$ that it defines, supposing for
simplicity that $s(S)$ is closed. Then there are canonical isomorphisms of augmented $\mathcal{O}_{X}$-algebras:

```text
s*(𝒫ⁿ_{X/S}) = 𝒪_X/𝒥^{n+1},    s*(𝒫^∞_{X/S}) = lim_n 𝒪_X/𝒥^{n+1}.
```

<!-- label: eq:II.4.4 -->

These isomorphisms are functorial in the evident sense under base change and, taking this fact into account, again give
a characterization of the sheaves of algebras $\mathcal{P}^{n}_{X/S}$ on $S$. If, for example, $S =
\operatorname{Spec}(k)$, with $k$ a field, then giving a section $s$ of $X$ over $S$ is equivalent to giving a point $x$
of $X$ rational over $k$, and the preceding formulas mean that there is an isomorphism of $k$-algebras

$$ \mathcal{P}^{n}_{X/S}(x) = \mathcal{O}_{x}/\mathfrak{m}^{n+1}_{x}. $$

<!-- label: eq:II.4.5 -->

This justifies the name “**sheaf of principal parts of order $n$ on $X$ relative to $S$**” given to
$\mathcal{P}^{n}_{X/S}$. One sees moreover from II.4.4 that **if $X$ is differentially smooth over $S$ at every point of
$s(S)$, then $X$ is smooth over $S$ at every point of $s(S)$**, by Corollary II.4.17, **the converse also being true**,
by Corollary II.4.18. Taking II.4.13 into account, one easily concludes that if $X$ is an $S$-prescheme locally of
finite type, **$X$ is smooth over $S$ if and only if it is flat over $S$ and differentially smooth over $S$**. Note that
the flatness hypothesis is essential, as one sees by taking $X$ to be a closed sub-prescheme of $S$.

Let us also recall that one obtains a **second algebra structure** on $\mathcal{P}^{n}_{X/S}$ through the projection
$pr_{2}: X \times_{S} X \to X$; it is in fact obtained from the preceding one by means of the **canonical involution**
of the sheaf of rings $\mathcal{P}^{n}_{X/S}$, induced by the symmetry automorphism of $X \times_{S} X$. We denote by
$d^{n}_{X/S}$, or simply $d^{n}$, the homomorphism of sheaves of rings

$$ d^{n}_{X/S}: \mathcal{O}_{X} \to \mathcal{P}^{n}_{X/S} $$

<!-- label: eq:II.4.6 -->

that corresponds to this second algebra structure. Taking the isomorphism II.4.4 into account, this homomorphism
transforms a section $f$ of $\mathcal{O}_{X}$ into a section $d^{n}(f)$ of $\mathcal{P}^{n}_{X/S}$ whose inverse image
by a section $s$ of $X$ over $S$ identifies with the canonical image of $f$ in $\Gamma(X,
\mathcal{O}_{X}/\mathcal{J}^{n+1})$. This justifies the name “**system of principal parts of order $n$ of $f$**” given
to $d^{n}f$, notably in the case $S = \operatorname{Spec}(k)$ considered in formula II.4.5.

Finally, note that the homomorphism II.4.6 may be regarded as the **universal differential operator of order $\leq
n$**[^ii-4-18-1] on $\mathcal{O}_{X}$, relative to the prescheme of constants $S$, provided one agrees to call a
homomorphism of sheaves $D$ from $\mathcal{O}_{X}$ into a module $F$ a differential operator of order $\leq n$ when it
factors as

```text
D: 𝒪_X --dⁿ→ 𝒫ⁿ_{X/S} --u→ F
```

where $u$ is a homomorphism of $\mathcal{O}_{X}$-modules, necessarily uniquely determined by $D$. This definition agrees
with the intuitive recursive definition: $D$ is a differential operator of order $\leq n$ if for every section $g$ of
$\mathcal{O}_{X}$ on an open $U$ of $X$, the map $f \mapsto D(fg) - gD(f)$ is a differential operator of order $\leq n -
1$ on $U$. It follows that **if $X$ is differentially smooth over $S$, the sheaf of rings of differential operators of
all orders has the familiar simple structure** from differential calculus on differentiable manifolds, and in particular
admits locally, as an $\mathcal{O}_{X}$-module, a basis formed from the **divided powers** in commuting operators
$\delta/\delta x_{i}$, $1 \leq i \leq n$. If $S$ is a sheaf of $\mathbb{Q}$-algebras, where $\mathbb{Q}$ is the field of
rational numbers, it is enough to take the ordinary polynomials in the $\delta/\delta x_{i}$. In that case, moreover,
and very exceptionally, for $X$ to be differentially smooth over $S$ it already suffices that $\Omega^{1}_{X/S}$ be
locally free.

**Remark.**

<!-- label: II.4.19 -->

The terminology “regular immersion”, “regular ideal”, etc. introduced in this number met with rather lively and general
opposition from Chevalley and Serre. “Cohen-Macaulay ideal”, or “Macaulay ideal”, or “Macaulayan ideal” was proposed,
which would morally oblige one also to adopt “Cohen-Macaulay immersion” or “Macaulay immersion”. This terminology,
however, conflicts with another already used in future drafts of the multiplodocus, where a morphism of finite type is
said to be “Cohen-Macaulay” at a point if it is flat at that point and if the fiber passing through that point has there
a local ring that is a Cohen-Macaulay ring. Pending a satisfactory solution, we shall keep, with every reservation, the
terminology introduced in this number.[^ii-4-19-1]

## 5. Case of a Base Field

<!-- label: II.5 -->

<!-- original page 52 -->

**Proposition.**

<!-- label: II.5.1 -->

Let $k$ be a field, let $X$ be a prescheme of finite type over $k$, let $x$ be a point of $X$, let $n$ be the dimension
of $X$ at $x$, and let

```text
f: X → Spec k[t₁,...,t_n] = Y
```

be a morphism defined by elements $f_{i} \in \Gamma(X, \mathcal{O}_{X})$. The following conditions are equivalent, and
imply that $X$ is smooth over $k$ at $x$, and a fortiori regular at $x$ by II.3.1:

1. $f$ is étale at $x$.
1. The $d f_{i}$ form a basis of $\Omega^{1}_{X/k}$ at $x$.
1. The $d f_{i}$ generate $\Omega^{1}_{X/k}$ at $x$.

Since (i) implies that $X$ is smooth over $k$ at $x$, the implication (i) ⇒ (ii) is a special case of II.4.8; (ii) ⇒
(iii) is trivial. It remains to prove (iii) ⇒ (i). If (iii) holds, $f$ is unramified at $x$ by Lemma II.4.1, hence,
after replacing $X$ by an open neighborhood of $x$, quasi-finite, and therefore dominant for dimension reasons. Since
$Y$ is regular, it follows that $f$ is étale by I.9.5 (ii) or I.9.11.

**Corollary.**

<!-- label: II.5.2 -->

Under the preliminary conditions of II.5.1, suppose that $\kappa(x)$ is a **finite separable** extension of $k$, and
that the $f_{i}$, $1 \leq i \leq n$, define elements of $\mathfrak{m}_{x}$. Then the preceding conditions are equivalent
to:

1. The $f_{i}$ form a system of generators of $\mathfrak{m}_{x}$; equivalently, the $f_{i}$ modulo
   $\mathfrak{m}^{2}_{x}$ form a basis of $\mathfrak{m}_{x}/\mathfrak{m}^{2}_{x}$ over $\kappa(x)$.

Indeed, (iv) ⇒ (iii) by the exact sequence

$$ \mathfrak{m}_{x}/\mathfrak{m}^{2}_{x} \to \Omega^{1}_{\mathcal{O}_{x}/k} \to \Omega^{1}_{\kappa(x)/k} \to 0 $$

<!-- label: eq:II.5.1 -->

and the fact that $\Omega^{1}_{\kappa(x)/k} = 0$, since $\kappa(x)$ is étale over $k$. On the other hand, (ii) implies
(iv), because since $X$ and $\operatorname{Spec}(\kappa(x))$ are smooth over $k$ at $x$, one may put a 0 on the left in
the preceding exact sequence by II.4.10 (iv).

**Corollary.**

<!-- label: II.5.3 -->

Let $x$ be a point of $X$, of finite type over $k$. If $X$ is smooth over $k$ at $x$, then $\mathcal{O}_{x}$ is regular;
the converse is true if $\kappa(x)$ is a finite separable extension of $k$.

Indeed, the converse follows from II.5.2 by taking a regular system $(f_{i})$ of generators of $\mathfrak{m}_{x}$.
Instead of II.5.2 one may also invoke Theorem II.4.15. We conclude:

**Proposition.**

<!-- label: II.5.4 -->

Let $X$ be a prescheme of finite type over $k$. If $X$ is smooth over $k$, then it is regular; the converse is true if
$k$ is perfect.

For the converse, note that by II.5.3, $X$ is smooth over $k$ at every closed point, hence everywhere, since the set of
points where it is smooth is open.

**Theorem.**

<!-- label: II.5.5 -->

Let $X$ be a prescheme of finite type over $k$, let $x$ be a point of $X$, let $n$ be the dimension of $X$ at $x$, and
let $k'$ be a perfect extension of $k$. The following conditions are equivalent:

1. $X$ is smooth over $k$ at $x$.
1. $\Omega^{1}_{X/k}$ is free of rank $n$ at $x$.
1. $\Omega^{1}_{X/k}$ is generated by $n$ elements at $x$.
1. $X$ is differentially smooth over $k$ at $x$.
1. There is an open neighborhood $U$ of $x$ such that $U \otimes_{k} k'$ is regular, i.e. the local rings of its points
   are regular.

We have (i) ⇒ (ii) by II.4.3 (ii), (ii) ⇒ (ii bis) trivially, and (ii bis) ⇒ (i) by II.5.1. Since $X$ is flat over $k$,
we have (i) ⇔ (iii) by II.4.18. We have (i) ⇒ (iv) because smoothness is invariant under extension of the base and
implies regularity; and (iv) ⇒ (i), because by Proposition II.5.4 one sees that $U \otimes_{k} k'$ is smooth over $k'$,
hence $U$ is smooth over $k$ by II.4.13.

Taking $x$ to be the generic point of $X$, supposed irreducible, one obtains:

**Corollary.**

<!-- label: II.5.6 -->

Let $K$ be a local Artin ring obtained by localizing an algebra of finite type over the field $k$; for example, $K$ may
be an extension of finite type of $k$. Let $n$ be the transcendence degree over $K$ of its residue field. The following
conditions are equivalent:

1. $K$ is a finite separable extension of a purely transcendental extension $k(t_{1},...,t_{n})$ of $k$.
1. $\Omega^{1}_{K/k}$ is a free $K$-module of rank $n$.
1. $\Omega^{1}_{K/k}$ is a $K$-module admitting $n$ generators.
1. The completion $O'$ of $K \otimes_{k} K$ for the topology defined by the powers of the augmentation ideal $K
   \otimes_{k} K \to K$ is a “regular” augmented $K$-algebra, i.e. isomorphic to a formal power-series algebra over $K$.
   If $K$ is a field, this is equivalent to saying that $O'$ is a regular local ring.
1. $K$ is a separable extension of $k$.

Indeed, one may always regard $K$ as the local ring of the generic point of an irreducible scheme $X$ of finite type
over $k$, and the conditions under consideration are the conditions with the same names in II.5.5, taking in (iv) an
algebraically closed extension of $k$ for $k'$. Only the implication “$K$ separable over $k$ ⇒ $X$ smooth over $k$ at
$x$” requires a proof. By II.4.13 one is immediately reduced to the case where the base field is $k'$, hence
algebraically closed, and therefore where there exists a point $a$ of $X$ rational over $k$. But then $X$ is smooth over
$k$ at $a$ by II.5.4, and a fortiori it is smooth over $k$ at the generic point $x$.[^ii-5-6-1]

One will notice that in the case where $K$ is an extension of finite type of $k$, the equivalence of (i), (ii), (ii
bis), and (iv) is well known, but that we have not used any of these already-known equivalences. Of course Proposition
II.5.1 contains as a special case the well-known fact that a sequence of elements $x_{i}$, $1 \leq i \leq n$, is a
“separating transcendence basis” of $K$ over $k$ if and only if the $d x_{i}$ form a basis of the $K$-module
$\Omega^{1}_{K/k}$.

**Corollary.**

<!-- label: II.5.7 -->

Let $X$ be a prescheme of finite type over a field $k$. In order that $X$ be smooth over $k$, it is necessary and
sufficient that $\Omega^{1}_{X/k}$ be locally free and that the local rings at the generic points of the irreducible
components of $X$ be separable extensions of $k$. The latter condition is automatically satisfied if $k$ is perfect and
$X$ is reduced.

We may suppose $X$ connected, and let $n$ be the rank of $\Omega^{1}_{X/k}$, assumed locally free. By the hypothesis and
II.5.6, this is also the transcendence degree of the extensions of $k$ defined by the local rings at the generic points
of $X$. Hence all irreducible components of $X$ have dimension $n$. We then conclude by II.5.5.

Care must be taken that if $K$ is a finite, not necessarily separable, extension of $k$, then $\Omega^{1}_{K/k}$ is a
free $k$-module; hence, putting $X = \operatorname{Spec}(K)$, $\Omega^{1}_{X/k}$ is a locally free sheaf and $X$ is
reduced, without $X$ necessarily being smooth over $k$. Extending scalars then to the algebraic closure of $k$, one
obtains an analogous example where $k$ is algebraically closed, but $X$, in contrast, is not reduced.

**Corollary.**

<!-- label: II.5.8 -->

Let $X$ be a prescheme of finite type over the field $k$, let $x$ be a point of $X$, let $n$ be the dimension of $X$ at
$x$, and let $p$ be the dimension of $\mathcal{O}_{x}$, i.e. the codimension in $X$ of the closure $Y$ of $x$ in $X$;
thus $n - p$ is the transcendence degree of $\kappa(x)$ over $k$. Let $f_{i}$, $1 \leq i \leq n$, be elements of
$\mathcal{O}_{x}$, with $f_{i} \in \mathfrak{m}_{x}$ for $1 \leq i \leq p$. The following conditions are equivalent:

1. The germ at $x$ of the morphism

$$ X \to \operatorname{Spec}(k[t_{1},...,t_{n}]) $$

defined by the $f_{i}$ is étale at $x$. 2. The $f_{i}$, $1 \leq i \leq p$, generate $\mathfrak{m}_{x}$, i.e. form a
regular system of parameters of $\mathcal{O}_{x}$, and the classes in $\kappa(x)$ of the $f_{j}$, $p + 1 \leq j \leq n$,
form a separating transcendence basis; equivalently, the $d \bar{f}_{j}$, $p + 1 \leq j \leq n$, form a basis of
$\Omega^{1}_{\kappa(x)/k}$, or again generate $\Omega^{1}_{\kappa(x)/k}$.

Suppose (i) holds. It follows that the $d f_{i}(x)$ form a basis of $\Omega^{1}_{X/k}(x)$ by II.4.8; hence their images
$d \bar{f}_{i}(x)$ in $\Omega^{1}_{\kappa(x)/k}$ generate this vector space over $k$. Since the $\bar{f}_{i}$ for $1
\leq i \leq p$ are zero, it follows that it suffices to take the $d \bar{f}_{i}(x)$ with $p + 1 \leq i \leq n$. Since
the transcendence degree of $\kappa(x)$ over $k$ is $n - p$, Corollary II.5.6, criterion (iii), applied to $K =
\kappa(x)$, then implies that $Y$ is smooth over $k$ at its generic point $x$, and that the $d \bar{f}_{i}(x)$, $p + 1
\leq i \leq n$, form a **basis** of $\Omega^{1}_{\kappa(x)/k}$ over $\kappa(x)$. Consequently condition (ii) of II.4.9
is satisfied, hence also condition (iii), and in particular the $f_{i}$, $1 \leq i \leq p$, form a system of generators
of $\mathfrak{m}_{x}$. Since $\mathcal{O}_{x}$ has dimension $p$, they therefore form a regular system of parameters at
$x$. This proves (ii).

Suppose (ii) holds. By the exact sequence II.5.1, it follows that the $d f_{i}(x)$ generate $\Omega^{1}_{X/k}$; hence
(i) follows from Proposition II.5.1.

**Corollary.**

<!-- label: II.5.9 -->

Let $X$ be a prescheme of finite type over the field $k$, let $x$ be a point of $X$, let $n$ be the dimension of $X$ at
$x$, and let $p$ be the dimension of $\mathcal{O}_{x}$, i.e. the codimension of the closure $Y$ of $x$ in $X$; thus $n -
p$ is the transcendence degree of $\kappa(x)$ over $k$. The following conditions are equivalent:

1. $\mathcal{O}_{x}$ is regular and $\kappa(x)$ is a separable extension of $k$.
1. $X$ is smooth over $k$ at $x$, and the canonical homomorphism

```text
𝔪_x/𝔪_x² → Ω¹_{𝒪_x/k} ⊗_{𝒪_x} κ(x) = Ω¹_{X/k}(x)
```

is injective. 3. There are $f_{i} \in \mathcal{O}_{x}$, $1 \leq i \leq n$, with $f_{i} \in \mathfrak{m}_{x}$ for $1 \leq
i \leq p$, such that the germ at $x$ of the morphism from $X$ to $\operatorname{Spec}(k[t_{1},...,t_{n}])$ defined by
the $f_{i}$ is étale at $x$; equivalently, by II.5.1, such that the $d f_{i}(x)$ generate $\Omega^{1}_{X/k}(x)$. 4.
There are $f_{i} \in \mathcal{O}_{x}$, $1 \leq i \leq n$, such that the $f_{i}$, $1 \leq i \leq p$, generate
$\mathfrak{m}_{x}$ and the $d f_{j}(x)$, $p + 1 \leq j \leq n$, generate $\Omega^{1}_{\kappa(x)/k}$ over $\kappa(x)$.

The equivalence of (iii) and (iv) follows from Corollary II.5.8. By II.4.9, these conditions are also equivalent to the
fact that $X$ is smooth over $k$ at $x$ and that condition (ii) of II.4.10 is satisfied. Thus they are equivalent to the
fact that $X$ is smooth over $k$ at $x$ and that condition (iv) of II.4.10 is satisfied, hence to II.5.9 (ii). Or
equivalently, to the fact that $X$ is smooth over $k$ at $x$ and that condition (i) of II.4.10 is satisfied, which here
simply means that $\kappa(x)$ is separable over $k$. This implies II.5.9 (i). It remains to prove that II.5.9 (i)
implies it, i.e. to prove:

**Corollary.**

<!-- label: II.5.10 -->

Let $x$ be a point of a prescheme of finite type over the field $k$, such that $\kappa(x)$ is separable over $k$. In
order that $X$ be smooth over $k$ at $x$, it is necessary and sufficient that it be regular at $x$, i.e. that the local
ring $\mathcal{O}_{x}$ be regular.

Indeed, if this is so, one can evidently find $f_{i} \in \mathcal{O}_{x}$, $1 \leq i \leq n$, satisfying condition
II.5.9 (iv).

### Errata

<!-- label: II.fin.errata -->

<!-- original page 57 -->

In the present number, in the proof of II.5.6, we used the fact that a nonempty reduced scheme of finite type over an
algebraically closed field has at least one regular, hence smooth, point, a fact usually proved by differential means,
via Zariski's theorem that the set of regular points of $X$ is open. If one wants to avoid a vicious circle, one must
prove that if $K/k$ is a separable extension of finite type, and if the $f_{i} \in K$ are such that $d_{K/k} f_{i}$ form
a basis of $\Omega^{1}_{K/k}$, $1 \leq i \leq n$, then $n$ is the transcendence degree of $K$ over $k$, i.e. the $f_{i}$
are algebraically independent. The proof of this fact using Mac Lane's criterion is well known; cf. Bourbaki, Algebra,
Chapter V, paragraph 9, theorem 2. One takes a polynomial $g \in k[t_{1},...,t_{n}]$ of minimal degree such that
$g(f_{1},...,f_{n}) = 0$. We then have

```text
Σ_i (∂g/∂t_i)(f₁,...,f_n) d f_i = 0.
```

Hence, since the $d f_{i}$ form a basis of $\Omega^{1}_{K/k}$, the $\partial g/\partial t_{i}$ vanish at
$(f_{1},...,f_{n})$, and therefore are zero by the minimality of $g$. Thus if $k$ has characteristic 0, one has $g = 0$,
while if $k$ has characteristic $p \neq 0$, one has $g = h(t^{p}_{1},...,t^{p}_{n})$. Using Mac Lane's criterion, one
sees that the polynomial $h \in k[t_{1},...,t_{n}]$ also vanishes at $(f_{1},...,f_{n})$, whence again $g = 0$ by the
minimality of $g$.

<!-- end of Exposé II source block: next chapter begins at smf_doc-math_3_01.tex line 4492 -->

[^II-1-1]: Older terminology: $f$ is simple at $x$, or $x$ is a simple point for $f$. This terminology led to confusion
    in various contexts, such as simple algebras and simple groups, and had to be abandoned.

[^II-1-2]: It is better then to say, as in EGA IV 18.6.1, that $B$ is “essentially smooth” over $A$.

[^II-2-1]: Cf. EGA IV 7.8.

[^II-2-2]: Cf. EGA IV 5.12.10.

[^II-3-1]: For these formulas, cf. EGA IV 6.1 and 6.3.

[^ii-4-14-1]: We would now rather say “$A$-regular sequence”, cf. EGA 0_IV 15.1.7 and 15.1.11.

[^ii-4-14-2]: As was said in the preface, this has now been done; cf. EGA IV 17, 18.

[^ii-4-18-1]: For everything concerning the present paragraph, one may consult EGA IV 16.8 to 16.12.

[^ii-4-19-1]: This is the terminology adopted in EGA 0_IV 15.1.7.

[^ii-5-6-1]: Cf. the Errata at the end of the present Exposé II, p. 57 in the original numbering.
