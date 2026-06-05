# Exposé X. Theory of Specialization of the Fundamental Group

<!-- label: X -->

<!-- original page 261 -->

In the present exposé, we restrict ourselves to the study of the fundamental group of geometric fibers in a **proper**
morphism, that is, of the fundamental group of a variable **proper** algebraic scheme. In a later exposé, we shall
generalize the technique used here to étale coverings **tamely ramified** “at infinity.” This will give, for example, a
solution of the “three point problem” in the case of Galois coverings of order prime to the characteristic, that is, a
determination of the Galois coverings of the line $\mathbb{P}^{1}_{k}$ ramified at most at three given points and tamely
ramified at those points, together with its evident variants.

## 1. The Homotopy Exact Sequence for a Proper and Separable Morphism

<!-- label: X.1 -->

**Definition.**

<!-- label: X.1.1 -->

A prescheme $X$ over a field $k$ is called **separable**, or **separable over $k$**, if for every extension $K$ of $k$,
$X \otimes_{k} K$ is reduced. If $f: X \to Y$ is a morphism of preschemes, one says that $f$ is **separable**, or that
$X$ **is separable over $Y$**, if $X$ is flat over $Y$ and if for every $y \in Y$, the fiber $X \otimes_{Y} \kappa(y)$
is separable over $\kappa(y)$.

If $X$ is a prescheme over a field $k$, to say that it is separable also means that it is **reduced**, and that the
fields $\kappa(x)$, for $x$ the generic point of an irreducible component of $X$, are separable extensions of $k$. If
$k$ is perfect, this is therefore the same as saying that $X$ is reduced.

Notice that if $X$ is separable over $Y$, then for every base change $Y' \to Y$, $X' = X \times_{Y} Y'$ is separable
over $Y'$. One can also prove, under suitable finiteness hypotheses, that the composite of two separable morphisms is

<!-- original page 262 -->

separable. We shall need this only in the following form: **if $X$ is separable over $Y$ and $X'$ is étale over $X$,
then $X'$ is separable over $Y$.** This is an immediate consequence of the definitions and I.9.2. Moreover, the
hypothesis “separable morphism” will be used through the following proposition:

**Proposition.**

<!-- label: X.1.2 -->

Let $f: X \to Y$ be a proper and separable morphism, with $Y$ locally noetherian, and consider its **Stein**
factorization $X \to Y' \to Y$, where $f'_{*}(\mathcal{O}_{X}) = \mathcal{O}_{Y'}$, with $Y'$ finite over $Y$ and
isomorphic to the spectrum of the algebra $f_{*}(\mathcal{O}_{X})$. Then $Y'$ is an **étale covering** of $Y$.

This proposition will appear in EGA III 7. [Translator note: the source footnote cites EGA III 7.8.10(i).] Let us
indicate the principle of the proof. One reduces easily to the case where $Y$ is the spectrum of a complete local ring
$A$, and, after making a suitable finite flat extension of the latter corresponding to a suitable residue extension, one
may suppose that the connected components of the fiber over the closed point $y$ are geometrically connected. This also
means that $H^{0}(X_{y}, \mathcal{O}_{X_{y}})$ decomposes as a product of fields identical with $k = \kappa(y)$.
Supposing then that $X$ is connected, as one may, one has $H^{0}(X_{y}, \mathcal{O}_{X_{y}}) = k$, hence the
homomorphism $A \to H^{0}(X_{y}, \mathcal{O}_{X_{y}})$ is **surjective**. By a general proposition of Künneth type, one
concludes that $f_{*}(\mathcal{O}_{X})$ is defined by a module $B$ over $A$ that is free over $A$, and that
$B/\mathfrak{m}B \to H^{0}(X_{y}, \mathcal{O}_{X_{y}}) = k$ is bijective. Thus in the present case $B$ is an étale
algebra over $A$, completing the proof.

**Theorem.**

<!-- label: X.1.3 -->

Let $f: X \to Y$ be a proper and separable morphism, with $Y$ locally noetherian and connected, and suppose
$f_{*}(\mathcal{O}_{X}) = \mathcal{O}_{Y}$. This implies that the fibers of $X$ over $Y$ are geometrically connected,
and conversely by X.1.2. Let $y$ be a point of $Y$, let $\kappa\bar{y}$ be an algebraic closure of $\kappa(y)$, and let
$\bar{X}_{y} = X_{y} \otimes_{\kappa(y)} \kappa\bar{y}$. Finally, let $X'$ be a **connected** étale covering of $X$, and
let $\bar{X}'_{y} = X'_{y} \otimes_{\kappa(y)} \kappa\bar{y}$. Then there exists an étale covering $Y'$ of $Y$ and an
$X$-isomorphism

<!-- original page 263 -->

```text
X′ ≃ X ×_Y Y′
```

if and only if $\bar{X}'_{y}$ admits a section over $\bar{X}_{y}$.

Putting $Y' = \operatorname{Spec}(h_{*}(\mathcal{O}_{X'}))$, where $h: X' \to Y$ is the composite $X' \to X \to Y$, it
is enough to prove that the canonical $Y$-morphism

```text
X′ → X ×_Y Y′
```

is an **isomorphism**, and that $Y'$ is étale over $Y$. We already know by X.1.2 that $Y'$ is étale over $Y$, hence $X
\times_{Y} Y'$ is étale over $X$, and therefore the morphism $X' \to X \times_{Y} Y'$ is also étale (I.4.8). Moreover,
$Y'$ is connected as the image of $X'$, which is connected; hence $X \times_{Y} Y'$ is connected, since $X$ has
connected fibers over $Y$ (IX.3.4 and V.6.9(iii)). Thus to prove that $X' \to X \times_{Y} Y'$ is an isomorphism, it is
enough to see that its projection degree at **one** point of $X \times_{Y} Y'$ is equal to 1. This follows easily from
the hypothesis that $\bar{X}'_{y}$ admits a section over $\bar{X}_{y}$, either by using IX.6.6 or more simply by noting
that it is enough to prove the existence of such a point in $X \times_{Y} Y'$ after the base change
$\operatorname{Spec}(\kappa\bar{y}) \to Y$, where this is evident. This proves X.1.3.

Taking IX.3.4 and the dictionary V.6.9 and V.6.11 into account, one can put X.1.3 in the following equivalent form:

**Corollary.**

<!-- label: X.1.4 -->

With the preceding notation for $f: X \to Y$ and $\bar{X}_{y}$, let `ā` be a geometric point of $\bar{X}_{y}$, let $a$
be its image in $X$, and let $b$ be its image in $Y$. Then the following sequence of group homomorphisms is **exact**:

```text
π₁(X̄_y,ā) → π₁(X,a) → π₁(Y,b) → e.
```

**Remarks.**

<!-- label: X.1.5 -->

Notice that the proof of X.1.3 uses X.1.2 in an essential way and hence the “first comparison theorem” in
algebraic-formal geometry. By contrast, the descent theory of Exposé IX entered only through IX.3.4, for which a direct
proof is easy in the case of a **proper** morphism $f: X \to Y$ such that $f_{*}(\mathcal{O}_{X}) = \mathcal{O}_{Y}$.

<!-- original page 264 -->

Indeed, let $Y'$ be étale over $Y$ and suppose $X' = X \times_{Y} Y'$ is the disjoint sum of two nonempty open subsets;
we prove that the same is true of $Y'$. One has $Y' = \operatorname{Spec}(\mathcal{A})$, hence $X' =
\operatorname{Spec}(\mathcal{B})$, with $\mathcal{B} = \mathcal{A} \otimes_{\mathcal{O}_{Y}} \mathcal{O}_{X}$, and the
decomposition of $X'$ as a direct sum corresponds to a decomposition of $\mathcal{B}$ as a product of two nonzero
Algebras $\mathcal{B}_{1}$ and $\mathcal{B}_{2}$. Since $f_{*}(\mathcal{O}_{X}) = \mathcal{O}_{Y}$, one easily concludes
$f_{*}(\mathcal{B}) = \mathcal{A}$, so $\mathcal{A}$ is a sum of two Algebras, also nonzero because their unit sections
are nonzero, namely $f_{*}(\mathcal{B}_{1})$ and $f_{*}(\mathcal{B}_{2})$.

### 1.6.

<!-- label: X.I.6 -->

Suppose again that $f$ is proper and separable, but no longer make any hypothesis on $f_{*}(\mathcal{O}_{X})$, which
will correspond to a well-determined étale covering $Y'$ of $Y$, pointed above $b$ by the image $b'$ of $a$. Applying
X.1.4 to the canonical morphism $X \to Y'$, and supposing $f$ surjective, the exact sequence X.1.4 is replaced by the
following, analogous to the homotopy exact sequence of fiber spaces in algebraic topology:

```text
π₁(X̄_y,ā) → π₁(X,a) → π₁(Y,b) →
π₀(X̄_y,ā) → π₀(X,a) → π₀(Y,b) → e.
```

Of course, in X.1.4 one cannot in general assert that the homomorphism $\pi_{1}(\bar{X}_{y}, \bar{a}) \to \pi_{1}(X, a)$
is injective; in algebraic topology its kernel is the image of $\pi_{2}(Y, b)$, and in algebraic geometry as well there
would be reason to introduce homotopy groups in all dimensions, and the complete homotopy exact sequence for a proper
morphism satisfying suitable hypotheses, for example being smooth. At present no result in this direction is available,
except for a reasonable, though perhaps not definitive, definition of higher homotopy groups.

**Corollary.**

<!-- label: X.1.7 -->

Let $k$ be an algebraically closed field, and let $X$ and $Y$ be two connected preschemes over $k$. Suppose $X$ proper
over $k$ and $Y$ locally

<!-- original page 265 -->

noetherian. Let $a$ be a geometric point of $X$, and let $b$ be a geometric point of $Y$ with values in the same
algebraically closed extension $K$ of $k$. Consider the geometric point $c = (a, b)$ of $X \times_{k} Y$, and the
homomorphism

```text
π₁(X ×_k Y,c) → π₁(X,a) × π₁(Y,b)
```

deduced from the homomorphisms on fundamental groups associated with the two projections $X \times_{k} Y \to X$ and $X
\times_{k} Y \to Y$. This homomorphism is an **isomorphism**.

First suppose $K = k$. Put $Z = X \times_{k} Y$, consider the projection $f: Z \to Y$ and the locality $y$ of the
geometric point $b$ of $Y$, and apply X.1.4 to this situation. Notice that, after replacing $X$ by $X_{red}$ (which does
not change the fundamental groups in question), one may assume $X$ reduced, hence separable over $k$; therefore $Z$ is
separable over $k$, and plainly has geometrically connected fibers, since $X$ is connected. The geometric fiber of $Z$
at $b$ is canonically isomorphic to $X \otimes_{k} K = X$.

On the other hand, since the composite $X \to Z \to X$ is the identity, one finds that $\pi_{1}(X, a) \to \pi_{1}(Z, c)$
is injective, and X.1.4 gives an exact sequence

```text
e → π₁(X,a) → π₁(Z,c) → π₁(Y,b) → e.
```

There is also the canonical exact sequence

```text
e → π₁(X,a) → π₁(X,a) × π₁(Y,b) → π₁(Y,b) → e,
```

where the maps written are the canonical injection and projection. Finally, the canonical homomorphism $\pi_{1}(Z, c)
\to \pi_{1}(X, a) \times \pi_{1}(Y, b)$, together with the identity maps on the two end terms, gives a homomorphism from
the first exact sequence to the second. The commutativity of the resulting diagram is immediate. Since the homomorphisms
on the end terms are isomorphisms, the same is true for the middle terms; this proves X.1.7 in this case.

When $K$ is no longer assumed equal to $k$, one obtains only an isomorphism

```text
π₁(Z,c) → π₁(X ⊗_k K,a) × π₁(Y,b),
```

<!-- original page 266 -->

and X.1.7 is then equivalent to the following special case:

**Corollary.**

<!-- label: X.1.8 -->

Let $X$ be a proper connected scheme over an algebraically closed field $k$, let $k'$ be an algebraically closed
extension of $k$, let $a'$ be a geometric point of $X \otimes_{k} k'$, and let $a$ be its image in $X$. Then the
canonical homomorphism

```text
π₁(X ⊗_k k′,a′) → π₁(X,a)
```

is an **isomorphism**.

The fact that this homomorphism is surjective is equivalent to saying that if $X'$ is a connected étale covering of $X$,
then $X' \otimes_{k} k'$ is also connected; this follows at once from the fact that $k$ is algebraically closed, and is
also a special case of IX.3.4. The properness hypothesis on $X$ has not yet been used.

It remains to say that injectivity of the homomorphism under consideration means: **every étale covering of $X
\otimes_{k} k'$ is isomorphic to the inverse image of an étale covering of $X$.** It is essentially sorital that one can
find a sub-$k$-algebra $A$ of $k'$, of finite type over $k$, and an étale covering of $X \otimes_{k} A$ whose inverse
image on $X \otimes_{k} k'$ is isomorphic to the given covering. Let $Y = \operatorname{Spec}(A)$, an integral
$k$-scheme of finite type, hence having $k$-rational points. Applying X.1.7 to the fundamental group of $X \times Y$ at
a point $(a, b)$ rational over $k$, one finds that every connected étale covering of $X \times Y$ is isomorphic to a
quotient of a covering $X' \times Y'$, where $X'$ and $Y'$ are Galois étale coverings of $X$ and $Y$ with groups $G$ and
$G'$, by a subgroup $H$ of $G \times G'$.

It follows that the inverse image of this covering of $X \times Y$ on $X \times Y'$ is isomorphic to a covering of the
form $X_{1}' \times Y'$, where $X_{1}'$ is an étale covering of $X$. If $L$ is the function field of $Y$, equal to the
fraction field of $A$ in $k'$, the étale covering of $X \otimes_{k} L$ induced by the given covering of $X \times_{k} Y$
is such that there exists a finite separable extension $L'$ of $L$ for which the inverse image of that covering on $X
\otimes_{k} L'$ is isomorphic to $X_{1}' \otimes_{k} L'$. Since $k'$ is algebraically closed, one may suppose the
extension $L'$ of $L$ is contained in $k'$. This proves that the given étale covering of $X \otimes_{k} k'$ is
isomorphic to $X_{1}' \otimes_{k} k'$.

The explicit form just mentioned for étale coverings of a product

<!-- original page 267 -->

$X \times_{k} Y$ immediately implies:

**Corollary.**

<!-- label: X.1.9 -->

Let $k$ be an algebraically closed field, let $X$ and $Y$ be two locally noetherian preschemes over $k$, let $Z = X
\times_{k} Y$ be their product, and let $Z'$ be an étale covering of $Z$. For every point $y \in Y$ rational over $k$,
let $i_{y}: \operatorname{Spec}(k) \to Y$ be the associated canonical morphism, and let $j_{y} = id_{X} \times_{k}
i_{y}$ be the corresponding morphism $X \to Z$. Finally, let $X_{y}'$ be the étale covering of $X$ obtained as inverse
image of $Z'$ by $j_{y}$. Suppose $Y$ connected, and suppose $X$ or $Y$ proper over $k$. Then the coverings $X_{y}'$ of
$X$ are all isomorphic.

Figuratively, one may say that **a family of étale coverings of $X$, parametrized by a connected prescheme $Y$, is
constant if $X$ or the parameter prescheme $Y$ is proper over $k$.**

**Remarks.**

<!-- label: X.1.10 -->

Corollaries X.1.7 to X.1.9 are due to Lang and Serre [X.2] in the case of normal algebraic schemes. Their work was the
initial motivation for the theory of the fundamental group developed in this seminar. As these authors observed, these
results become false if the properness hypothesis is dropped, at least in characteristic $p > 0$. Taking for example $X$
to be the affine line $X = \operatorname{Spec}(k[t])$, it is not difficult to see that the coverings of $X$,
parametrized by the affine line $Y = \operatorname{Spec}(k[s])$, defined by the equations

$$ x^{p} - x = st, $$

are étale and pairwise non-isomorphic. This contradicts X.1.9 and a fortiori X.1.7; similarly, if $s$ is regarded as a
transcendental element over $k$ in an algebraically closed extension $K$ of $k$, one obtains an étale covering $X'$ of
$X \otimes_{k} K$ that does not come from an étale covering of $X$.

## 2. Application of the Existence Theorem for Sheaves: Semicontinuity Theorem for Fundamental Groups of Fibers of a Proper and Separable Morphism

<!-- label: X.2 -->

<!-- original page 268 -->

**Theorem.**

<!-- label: X.2.1 -->

Let $Y$ be the spectrum of a **complete** noetherian local ring, with residue field $k$; let $X$ be a proper $Y$-scheme;
let $X_{0} = X \otimes_{A} k$; let $a_{0}$ be a geometric point of $X_{0}$; and let $a$ be the corresponding geometric
point of $X$. Then the canonical homomorphism

$$ \pi_{1}(X_{0},a_{0}) \to \pi_{1}(X,a) $$

is an **isomorphism**.

This is only a translation, into the language of the fundamental group, of the result recalled in IX.1.10. It is here
that the existence theorem for sheaves in algebraic-formal geometry enters essentially into the theory of the
fundamental group.

Now introduce an algebraic closure $\bar{k}$ of the residue field $k$, and the geometric fiber $\bar{X}_{0} = X_{0}
\otimes_{k} \bar{k}$. We have the exact sequence (IX.6.1)

```text
e → π₁(X̄₀,ā) → π₁(X₀,a₀) → π₁(k,k̄) → e.
```

On the other hand, we have the isomorphism X.2.1 and the analogous, more elementary isomorphism

$$ \pi_{1}(k,\bar{k}) \to \pi_{1}(Y,b), $$

where $b$ is the image of $a$ in $Y$. Thus one obtains:

**Corollary.**

<!-- label: X.2.2 -->

With the preceding notation, suppose $\bar{X}_{0} = X_{0} \otimes_{k} \bar{k}$ connected, and let $\bar{a}_{0}$ be a
geometric point of $\bar{X}_{0}$, let $a_{0}$ be its image in $X$, and let $b_{0}$ be its image in $Y$. Then the
following sequence of canonical homomorphisms is exact:

```text
e → π₁(X̄₀,ā) → π₁(X,a₀) → π₁(Y,b₀) → e.
```

Compare this sequence with the exact sequence X.1.4, but note that: a) no flatness or fiberwise separability hypothesis
has had to be made for $X \to Y$; b) one has the important supplement that **the morphism $\pi_{1}(\bar{X}_{0},
\bar{a}_{0}) \to \pi_{1}(X, a_{0})$ is injective.**

This last fact will allow us to compare the fundamental group of the other

<!-- original page 269 -->

geometric fibers of $X$ over $Y$ with that of $\bar{X}_{0}$. Indeed, let $y_{1}$ be any point of $Y$, let $X_{1}$ be its
fiber and $\bar{X}_{1}$ its geometric fiber relative to an algebraically closed extension of $\kappa(y_{1})$, let
$\bar{a}_{1}$ be a geometric point of $\bar{X}_{1}$, and let $a_{1}$ and $b_{1}$ be its images in $X$ and $Y$. Choose a
“path class” from $a_{1}$ to $a_{0}$, whence a path class from $b_{1}$ to $b_{0}$. This gives a commutative diagram of
homomorphisms

```text
π₁(X̄₁,ā₁) → π₁(X,a₁) → π₁(Y,b₁) → e
     ↓            ↓≃           ↓≃
e → π₁(X̄₀,ā₀) → π₁(X,a₀) → π₁(Y,b₀) → e,
```

where the two displayed vertical arrows in the middle and on the right are isomorphisms. Since the second row is exact,
one obtains a canonical homomorphism, which we shall call **the specialization homomorphism for the fundamental group**.
It depends only on the chosen path class from $a_{1}$ to $a_{0}$, and is therefore **defined modulo inner automorphism
of** $\pi_{1}(X, a_{0})$:

$$ \pi_{1}(\bar{X}_{1},\bar{a}_{1}) \to \pi_{1}(\bar{X}_{0},\bar{a}_{0}). $$

When the first row above is also exact, it follows at once that the specialization homomorphism is surjective. Thus,
taking X.1.4 into account:

**Corollary.**

<!-- label: X.2.3 -->

Under the conditions of X.2.1, suppose in addition that the morphism $f: X \to Y$ is **separable** (X.1.1) and that
$\bar{X}_{0}$ is connected. Then, by X.1.2, $f_{*}(\mathcal{O}_{X}) = \mathcal{O}_{Y}$. For every geometric fiber
$\bar{X}_{1}$ of $X$ over $Y$, endowed with a geometric point $\bar{a}_{1}$, the specialization homomorphism defined
above is **surjective**.

This is a **semicontinuity** result for the fundamental group, and it does not yet seem to have an analogue in algebraic
topology. It can also be stated under more general conditions:

**Corollary.**

<!-- label: X.2.4 -->

<!-- original page 270 -->

Let $f: X \to Y$ be a proper morphism with geometrically connected fibers, with $Y$ locally noetherian. Let $y_{0}$ and
$y_{1}$ be two points of $Y$ such that $y_{0} \in cl({y_{1}})$, let $\bar{X}_{0}$ and $\bar{X}_{1}$ be the geometric
fibers of $X$ corresponding to given algebraically closed extensions of $\kappa(y_{0})$ and $\kappa(y_{1})$, and let
$\bar{a}_{0}$, respectively $\bar{a}_{1}$, be a geometric point of $\bar{X}_{0}$, respectively $\bar{X}_{1}$. Then one
can define naturally a specialization homomorphism

$$ \pi_{1}(\bar{X}_{1},\bar{a}_{1}) \to \pi_{1}(\bar{X}_{0},\bar{a}_{0}), $$

defined up to inner automorphism, and it is **surjective** if $f$ is separable (X.1.1).

Indeed, X.1.8 first implies that X.2.4 is essentially independent of the chosen algebraically closed extensions of the
residue fields $\kappa(y_{0})$ and $\kappa(y_{1})$. This allows us to replace $Y$ by a prescheme $Y'$ over $Y$ having a
point $y_{0}'$, respectively $y_{1}'$, above $y_{0}$, respectively $y_{1}$. We then take $Y'$ to be the spectrum of the
completion of the local ring of $y_{0}$ in $Y$, and apply X.2.3.

**Remarks.**

<!-- label: X.2.5 -->

The final conclusion of X.2.4 on surjectivity of the specialization homomorphism, and a fortiori the results X.1.3 and
X.1.4 of which it is a consequence, become false if one no longer assumes $f: X \to Y$ to be separable, even for
projective schemes over an algebraically closed field of characteristic 0. We shall see examples later, both in the case
where $f$ is flat but has a nonseparable fiber (with $X$ and $Y$ nevertheless smooth over $k$), and in the case where
the fibers of $f$ are separable but $f$ is not flat, for instance with $f: X \to Y$ a birational morphism of normal
integral schemes; cf. XI.3. In these examples it can happen that the fundamental group of the generic geometric fiber is
trivial, while that of a suitable special geometric fiber is not.

On the other hand, even if $f: X \to Y$ is a proper separable morphism as in X.2.4, the specialization morphism often
fails to be an isomorphism.

<!-- original page 271 -->

For instance, it is easy to give examples where $\bar{X}_{1}$ is a nonsingular elliptic curve, so its fundamental group
is commutative and its $\ell$-primary component for a prime $\ell$ different from the characteristic is isomorphic to
$\mathbb{Z}^{2}_{\ell}$ (cf. XI), while $\bar{X}_{0}$ is formed either of two nonsingular rational curves meeting in two
points, or of two rational curves tangent at one point, or finally of a rational curve with a singularity that is a
cusp. For the complete classification of degenerate elliptic curves, see the recent work of Kodaira [X.1] and Néron. In
these cases the fundamental group of $\bar{X}_{0}$ is respectively $\hat{\mathbb{Z}}$, $e$, $e$, hence “strictly
smaller” than that of $\bar{X}_{1}$.

We shall see later, however, that when $f$ is a **smooth** morphism there is an upper bound on the kernel of the
specialization homomorphism, implying in particular that if $\kappa(y_{0})$ has **characteristic** 0, the specialization
homomorphism is an isomorphism. But even for a smooth morphism, if the characteristic of $\kappa(y_{0})$ is `> 0`, the
specialization homomorphism may fail to be an isomorphism, as one sees for example when $X$ is an abelian scheme over
$Y$ (of relative dimension 1, if desired); cf. XI.2.

A satisfactory theory of specialization of the fundamental group must take into account the “continuous component” of
the “true” fundamental group, corresponding to the classification of principal coverings with structural group an
infinitesimal group. Once this is done, one would be entitled to expect that the “true” fundamental groups of the
geometric fibers of a smooth and proper morphism $f: X \to Y$ form a nice local system on $X$, an inverse limit of
finite flat group schemes over $X$. \[Translator note: the source footnote says this very attractive conjecture is
unfortunately contradicted by an unpublished example of M. Artin, already for fibers that are algebraic curves of fixed
genus $g \geq 2$.\] We shall return later to this viewpoint; our present aim is, on the contrary, to push as far as
possible the phenomena common to the topological theory and the schematic theory of the fundamental group.

Let now $X_{0}$ be a proper, smooth, connected curve of genus $g$ over an algebraically closed field $k$. If $k$ has
characteristic zero, its fundamental group can be determined by transcendental methods as follows. One knows that
$X_{0}$ is obtained by base extension from a curve defined over an algebraically closed extension of finite
transcendence degree of the prime field $\mathbb{Q}$; taking X.1.8 into account, one may suppose $k$ itself has finite
transcendence degree over $\mathbb{Q}$. Hence one may suppose $k$ is a subfield of the complex numbers $\mathbb{C}$, and
another application of X.1.8 allows one to suppose $k = \mathbb{C}$.

It is then not difficult to verify that the fundamental group of $X$ is isomorphic to the profinite completion of the
fundamental group of the associated topological space $\tilde{X}$, a compact oriented surface of genus $g$, for the topology
defined by subgroups of finite index. \[Translator note: the source footnote says this deduction was explained in one of
the oral expos\acute{e}s that were not written up.\] Classically, the topological fundamental group is generated by `2g`
generators $s_{i}, t_{i}$, $1 \leq i \leq g$, subject to the single relation

```text
(s₁t₁s₁⁻¹t₁⁻¹)⋯(s_gt_gs_g⁻¹t_g⁻¹) = 1.
```

Thus the fundamental group of $X$ admits `2g` **topological** generators $s_{i}, t_{i}$, $1 \leq i \leq g$, bound by the
preceding single relation.

If now $k$ has characteristic $p > 0$, let $A$ be the ring of Witt vectors built from $k$, and let $K$ be an
algebraically closed extension of its fraction field. We saw in III.7.4 that there exists a scheme $X$ over $Y =
\operatorname{Spec}(A)$, proper and smooth over $Y$, reducing to $X_{0}$. Applying X.2.3 to it, one obtains a
**surjective** morphism

$$ \pi_{1}(X_{1}) \to \pi_{1}(X_{0}), $$

where $X_{1} = X \otimes_{A} K$. It is immediate (cf. EGA IV 12.2) that $X_{1}$ is smooth over $K$, connected (X.1.2),
of dimension 1, and that its genus is equal to $g$, by invariance of the Euler-Poincaré characteristic (cf. EGA III 7).
Since $K$ has characteristic 0, the preceding result applies to it. We have thus proved, by **transcendental methods**:

**Theorem.**

<!-- label: X.2.6 -->

Let $X_{0}$ be a smooth, proper, connected algebraic curve over an algebraically closed field $k$, and let $g$ be its
genus. Then $\pi_{1}(X_{0})$ admits a system of `2g` topological generators, bound by the relation written above. When
the characteristic of $k$ is 0, $\pi_{1}(X_{0})$ is even the group of galoisian type freely generated by the preceding
generators and relation.

<!-- original page 273 -->

**Remarks.**

<!-- label: X.2.7 -->

At present, to the editor’s knowledge, there is no purely algebraic proof of the preceding result, except in genera 0
and 1. To begin with, it is hardly clear how to distinguish `2g` elements in $\pi_{1}(X_{0})$ which one could then expect to
form a system of topological generators. In this respect, the situation of the rational line punctured at $n$ points,
and the study of its coverings tamely ramified at those points, is more sympathetic, since the ramification groups at
these $n$ points provide $n$ elements of the fundamental group to be studied, which one indeed shows generate it
topologically, as we shall see later. \[Translator note: the source footnote refers to Expos\acute{e} XII and notes that these
elements are really determined only up to conjugacy, so a judicious simultaneous choice of representatives is
required.\] But even in this particularly concrete case, there does not seem to be a purely algebraic proof. Such a
proof would plainly be extremely interesting. The only fact concerning the fundamental group of a curve that one knows
how to prove by purely algebraic methods, apart from the weak finiteness theorem X.2.12 below proved algebraically by
Lang and Serre [X.2], seems to be the determination of the abelianized fundamental group via the Jacobian, mentioned at
the end of IX.5.8.

### 2.8.

<!-- label: X.2.8 -->

The last assertion of X.2.6 is no longer valid in characteristic $p > 0$, as one already sees for elliptic curves. As we
have already pointed out, we do not know whether the fundamental group of $X_{0}$ is topologically finitely presented;
this seems quite improbable.

**Theorem.**

<!-- label: X.2.9 -->

Let $k$ be an algebraically closed field, and let $X$ be a proper connected scheme over $k$. Then the fundamental group
of $X$ is topologically finitely generated.

<!-- original page 274 -->

We proceed by induction on $n = \dim X$, the assertion being trivial for $n \leq 0$. Suppose $n > 0$ and the theorem
proved in dimensions $n' < n$. By Chow’s lemma (EGA II 5.6.2), there exists a projective scheme $X'$ over $k$ and a
surjective morphism $X' \to X$. One may plainly suppose $X'$ reduced, and after passing to the normalization, normal. By
descent theory, it is enough to prove that the fundamental groups of the connected components of $X'$ are topologically
finitely generated (IX.5.2). This reduces us to the case where $X$ is **projective** and **normal**. If $n = 1$, it is
enough to apply X.2.6. If $n \geq 2$, consider a projective immersion $X \to \mathbb{P}^{r}_{k}$ and a hyperplane
section $Y = X \cdot H$, endowed with the induced reduced structure, such that $Y \neq X$, that is, $H$ does not contain
$X$. Then $\dim Y < n$, and by the induction hypothesis it is enough to prove that $\pi_{1}(Y) \to \pi_{1}(X)$ is
**surjective**. More generally:

**Lemma.**

<!-- label: X.2.10 -->

Let $X$ be a prescheme proper over an algebraically closed field $k$, and let $g: X \to \mathbb{P}^{r}_{k}$ be a
morphism. Suppose $X$ irreducible and normal and $\dim g(X) \geq 2$. Let $H$ be a hyperplane of $\mathbb{P}^{r}_{k}$ and
let $Y = X \times_{\mathbb{P}^{r}} H$. Then $Y$ is connected, and the homomorphism $\pi_{1}(Y) \to \pi_{1}(X)$ is
surjective.

These assertions follow from:

**Corollary.**

<!-- label: X.2.11 -->

Under the preceding conditions, let $X'$ be a connected étale covering of $X$, and let $Y' = X' \times_{X} Y = X'
\times_{\mathbb{P}^{r}} H$ be the induced covering on $Y$. Then $Y'$ is connected.

Since $X$ is normal, $X'$ is normal; being connected, it is irreducible, and its image in $\mathbb{P}^{r}_{k}$ has
dimension $\geq 2$. A well-known lemma due to Zariski, called the **Bertini theorem**, implies that if $H_{1}'$ is the
generic hyperplane in $\mathbb{P}^{r}_{k}$, defined over an extension $K$ of $k$, then $X' \times_{\mathbb{P}^{r}}
H_{1}$ is universally irreducible, hence universally connected over $K$. Zariski’s connectedness theorem (EGA III 4)
then implies that for **every** hyperplane $H$, defined over any extension of $k$, $X' \times_{\mathbb{P}^{r}} H$ is
geometrically connected. This proves X.2.11, hence X.2.9.

**Corollary (Lang-Serre).**

<!-- label: X.2.12 -->

<!-- original page 275 -->

Under the conditions of X.2.9, for every finite group $G$, the set of isomorphism classes of principal coverings of $X$
with group $G$ is finite.

**Remark.**

<!-- label: X.2.13 -->

Under the conditions of X.2.10, when $\dim g(X) \geq 3$ we shall prove, at least when $g$ is an immersion and $X$
regular, a sharper result known in algebraic geometry as the **Lefschetz theorem**: $\pi_{1}(Y) \to \pi_{1}(X)$ **is an
isomorphism**. [Translator note: the corrected source refers to the subsequent seminar SGA 2, theorem X 3.10.] In the
classical cases there are analogous statements for homology groups and higher homotopy groups, which sooner or later
must be incorporated into abstract algebraic geometry. Even for Hodge cohomology $H^{p}(X, \Omega^{q})$, the question
does not seem to have been studied; moreover, it is hardly likely that for the latter the Lefschetz theorems remain
valid as stated in characteristic $p > 0$.

**Remark (M. Raynaud).**

<!-- label: X.2.14 -->

Let $R$ be a complete discrete valuation ring, with algebraically closed residue field $k$ of characteristic $p > 0$,
fraction field $K$, and let $Y$ be a proper, smooth, connected curve of genus $g$ over $R$. There is a surjective
specialization morphism $sp: \pi_{1}(Y_{\bar{K}}) \to \pi_{1}(Y_{k})$. We have already observed that if $K$ has
characteristic 0, `sp` is not an isomorphism as soon as $g \geq 1$. Suppose $K$ has characteristic $p$, so that $R$ is
isomorphic to the power series ring `k[[T]]`.

In equal characteristic $p > 0$, the fundamental group is not determined by the genus $g$, as one already sees for
elliptic curves, which may be ordinary or supersingular. We quote the recent result of A. Tamagawa, not yet published.
If $G$ is a profinite group, write $G^{res}$ for the profinite quotient of $G$ that is the inverse limit of the finite
solvable topological quotients of $G$.

**Theorem (A. Tamagawa).** Suppose $g \geq 2$, that the special fiber $Y_{k}$ is definable over a finite field, and that
the morphism `sp^res: π₁(Y_K̄)^res → π₁(Y_k)^res` deduced from `sp` by passage to the quotient is bijective. Then the
curve $Y$ is constant over $R$.

Notice that the Galois group of $\bar{K}/K$ is solvable. The preceding statement can also be translated as follows:
suppose that every finite étale covering $X_{K} \to Y_{K}$ of the generic fiber `Y_K`, Galois with solvable Galois
group, has potentially good reduction, that is, extends to a finite étale covering of $Y$ after possibly replacing $R$
by its normalization in a finite extension of $K$. Then $Y$ is constant over $R$.

## 3. Application of the Purity Theorem: Continuity Theorem for Fundamental Groups of Fibers of a Proper and Smooth Morphism

<!-- label: X.3 -->

Recall without proof the following theorem. [Translator note: the source refers for a proof to SGA 2 X.3.4.]

**Purity Theorem (Zariski-Nagata).**

<!-- label: X.3.1 -->

Let $f: X \to Y$ be a quasi-finite and dominant morphism of integral preschemes, with $X$ normal and $Y$ regular locally
noetherian, and let $Z$ be the set of points of $X$ at which $f$ is not étale, that is, where $f$ is ramified
(equivalently, I.9.5(ii)). If $Z \neq X$, then $Z$ has codimension 1 in $X$ at all its points; that is, for every
irreducible component $Z'$ of $Z$ with generic point $z$, the Krull dimension of $\mathcal{O}_{X, z}$ is equal to 1.

Recall that a prescheme is called **normal**, respectively **regular**, if its local rings are normal, respectively
regular, and that the relation $Z \neq X$ also means that the finite extension $R(Z)/R(X)$, where $R$ denotes the field
of rational functions, is **separable**. Placing ourselves at the generic point $z$ of a component $Z'$ of $Z$, and
localizing at the point $y$ of $Y$ below $z$, one obtains

<!-- original page 276 -->

the equivalent statement:

**Corollary.**

<!-- label: X.3.2 -->

Let $A$ be a regular noetherian local ring, and let $A \to B$ be an injective local homomorphism such that $B$ is
normal, a localization of a finite-type $A$-algebra, and **quasi-finite** over $A$. Suppose moreover that $\dim A (=
\dim B) \geq 2$, and that for every prime ideal $\mathfrak{p}$ of $B$ distinct from the maximal ideal, $B$ is étale over
$A$ at $\mathfrak{p}$, that is, $B_{\mathfrak{p}}$ is étale over $A_{\mathfrak{q}}$, where $\mathfrak{q} = A \cap
\mathfrak{p}$. Then $B$ is étale over $A$.

It is not difficult to reduce this last statement to the case where $A$ is a **complete** local ring, hence where $B$ is
**finite** over $A$. Zariski [X.5] gives a simple proof of this result, valid in the equal-characteristic case. The
general case is due to Nagata [X.3], who relies on a delicate result of Chow; the latter was not verified by any of the
participants in the seminar, and should be the subject of a later exposé.

We record here only the very simple proof in the special case $\dim A = 2$, which is enough for the most important
application we shall make of it in the present number. Since $B$ is normal, it is a $B$-module of depth (old
terminology: cohomological codimension) $\geq 2$; hence it is an $A$-module of depth $\geq 2$. Since $A$ is regular of
dimension 2, it follows that $B$ is a **free module** over $A$. [Translator note: the source refers to EGA 0_IV 17.3.4.]
It then follows from I.4.10 that the set of prime ideals $\mathfrak{q}$ of $A$ at which $B$ is ramified over $A$ is the
subset of $\operatorname{Spec}(A)$ defined by a principal ideal (generated by the discriminant of a basis of $B$ over
$A$). Thus it is empty if it is contained in the closed point of $\operatorname{Spec}(A)$, proving X.3.2 when $\dim A =
2$.

We shall mainly use X.3.1 in the following equivalent form:

**Corollary.**

<!-- label: X.3.3 -->

Let $X$ be a locally noetherian regular prescheme, and let $U$ be an open subset of $X$ whose complement is a closed
subset $Z$ of $X$ of codimension $\geq 2$. Then the functor $X' \mapsto X' \times_{X} U$ from the category of étale
coverings of $X$ to the category of étale coverings of $U$ is an equivalence

<!-- original page 277 -->

of categories. In particular, if $a$ is a geometric point of $U$, the canonical homomorphism $\pi_{1}(U, a) \to
\pi_{1}(X, a)$ is an isomorphism.

The last assertion is plainly a consequence of the first; for the first, one may plainly suppose $X$ connected, hence
irreducible. The normality of $X$ already implies that the functor $X' \mapsto X' \times_{X} U$ from the category of
locally free coverings (not necessarily étale) of $X$ to the category of coverings of $U$ is fully faithful, because the
functor $\mathcal{E} \mapsto \mathcal{E}|U$ from locally free Modules on $X$ to locally free Modules on $U$ is fully
faithful.

It remains to prove that for every **étale** covering $U'$ of $U$, there exists an étale covering $X'$ of $X$,
necessarily unique by what precedes, such that $U'$ is isomorphic to $X' \times_{X} U$. One may plainly suppose $U'$
connected, hence irreducible since $U'$ is normal ($U$ being normal). Let $K$ be the field of rational functions on $X$,
or on $U$, which is the same, and let $K'$ be that of $U'$. Then $U'$ identifies with the normalization of $U$ in $K'$
(I.10.3). Let $X'$ be the normalization of $X$ in $K'$ (EGA II 6.3); then $X' \times_{X} U \simeq U'$. Moreover $X'$ is
normal and integral, and the structural morphism $f: X' \to X$ is **finite** and dominant, since $X$ is normal and
$K'/K$ is a finite separable extension. It is étale over $U' = f^{-1}(U)$, and since $Z$ has codimension $\geq 2$ in
$X$, $f^{-1}(Z)$ has codimension $\geq 2$ in $X'$. We conclude from X.3.1 that $X'$ is étale over $X$, completing the
proof.

Now let $f: X \to Y$ be a rational map from a locally noetherian regular prescheme $X$ to a prescheme $Y$, and suppose
$f$ is defined on an open subset $U$ whose complement is a closed subset of codimension $\geq 2$. Then X.3.3 gives a
functor, defined up to isomorphism, from the category of étale coverings of $Y$ to the category of étale coverings of
$X$; hence for every geometric point $a$ of $U$, with image $b$ in $Y$, a canonical homomorphism

$$ \pi_{1}(X,a) \to \pi_{1}(Y,b), $$

<!-- original page 278 -->

deduced from the canonical homomorphism $\pi_{1}(U, a) \to \pi_{1}(Y, b)$ by means of the isomorphism $\pi_{1}(U, a)
\simeq \pi_{1}(X, a)$. When $f$ is a dominant morphism, with $X$ and $Y$ integral of function fields $K$ and $L$, so
that $K$ is an extension of $L$, and with $Y$ normal, these correspondences become more precise in terms of field
extensions: for every finite extension $L'$ of $L$ unramified over $Y$, the $K$-algebra $K' = L' \otimes_{L} K$ is
unramified over $X$.

In particular, these reflections show that the fundamental group of connected locally noetherian regular preschemes,
pointed by geometric points localized in codimension $\leq 1$, is a **functor** when as morphisms in this category one
takes dominant rational maps defined on complements of closed subsets of codimension $\geq 2$. Recalling, for example,
that a rational map from a normal scheme over a field $k$ to a proper scheme over $k$ is defined on the complement of a
set of codimension $\geq 2$, one obtains:

**Corollary. Birational Invariance of the Fundamental Group.**

<!-- label: X.3.4 -->

Let $k$ be a field, let $X$ and $Y$ be two proper regular schemes over $k$, let $f: X \to Y$ be a birational map from
$X$ to $Y$, and let $\Omega$ be an algebraically closed extension of the function field $K$ of $X$ allowing one to
define the fundamental group of $X$ and the fundamental group of $Y$. These groups are then canonically isomorphic.

This also means that for a finite extension $K'$ of $K$, if it is unramified over one nonsingular proper “model” $X$ of
$K$, it is unramified over every other nonsingular proper model.

**Remark.**

<!-- label: X.3.5 -->

For other applications of the purity theorem, see the work of Abhyankar presented in [X.4], inspired by the results of
Zariski [X.6, Chapter VIII], proved by topological methods. These latter results are far from having been assimilated by
“abstract” algebraic geometry and deserve renewed effort.

<!-- original page 279 -->

We shall need a few elementary facts from ramification theory. Let $V$ be a discrete valuation ring with fraction field
$K$ and residue field $k$; let $L$ be a Galois extension of $K$ with group $G$; let $V'$ be the normalization of $V$ in
$L$, which is a free $V$-module of rank $n = [L:K]$; let $\mathfrak{m}'$ be a maximal ideal of $V'$; let $G_{d}$ be the
subgroup of $G$ consisting of the elements that leave $\mathfrak{m}'$ invariant, so that $G_{d}$ acts on the residue
extension $k' = V'/\mathfrak{m}'$ of $k$; and let $G_{i}$ be the subgroup of elements of $G_{d}$ acting trivially.
Recall that $G_{d}$ and $G_{i}$ are called respectively the **decomposition** and **inertia** subgroups of $G$.

One says that $L$ is **tamely ramified** over $V$ if $n_{i} = [G_{i}:e]$ is of order prime to the characteristic $p$ of
$k$, a condition always satisfied if $k$ has characteristic 0. It is well known that $G_{i}$ then embeds canonically in
the group $k'*$, and is therefore isomorphic to the group of $n_{i}$-th roots of unity in $k'*$. In particular, $G_{i}$
**is cyclic**. The typical case is $L = K[t]/(t^{n} - u)$, where $u$ is a uniformizer of $V$ and $n$ is prime to $p$: if
$K$ contains the $n$-th roots of unity, $L$ is a totally ramified Galois extension of $K$, with Galois group $G = G_{i}$
isomorphic to $\mathbb{Z}/n\mathbb{Z}$.

**Lemma (Abhyankar’s Lemma).**

<!-- label: X.3.6 -->

Let $V$ be a discrete valuation ring with fraction field $K$. Let $L$ and $K'$ be two Galois extensions of $K$ **tamely
ramified** over $V$, and let $n$ and $m$ be the orders of the corresponding inertia groups. Let $L'$ be a composite
extension of $L$ and $K'$ over $K$. If $m$ is a multiple of $n$, then $L'$ is unramified over the localizations of the
normal closure $V'$ of $V$ in $K'$.

Indeed, let $W'$ be the normalization of $V'$ in $L'$, let $\mathfrak{m}'$ be a maximal ideal of $V'$, let
$\mathfrak{n}'$ be a maximal ideal of $W'$ above $\mathfrak{m}'$, and let $\mathfrak{n}$ be the maximal ideal that it
induces on the normalization $W$ of $V$ in $L$. Let $G$, $H$, $M$ be the Galois groups of $L$, $K'$, $L'$ over $K$, and
let $G_{i}$, $H_{i}$, $M_{i}$ be the inertia groups corresponding to the chosen maximal ideals. Then $M$ embeds in $G
\times H$ and $M_{i}$ in $G_{i} \times H_{i}$, in such a way that the projections $M \to G$ and $M \to H$, and $M_{i}
\to G_{i}$

<!-- original page 280 -->

and $M_{i} \to H_{i}$, are surjective (the standard intermediate-field sorites). It already follows, since $G_{i}$ and
$H_{i}$ are by hypothesis cyclic of orders $m$ and $n$ prime to $p$, that $M_{i}$ has order prime to $p$, hence is
cyclic. Since $m$ is a multiple of $n$, all elements of $G_{i} \times H_{i}$ have $m$-th power equal to the identity;
hence $M_{i}$ has order dividing $m$, and therefore order exactly $m$ because $M_{i} \to H_{i}$ is surjective. This last
homomorphism is therefore also injective. But its kernel is the inertia group of $\mathfrak{n}'$ over $\mathfrak{m}'$,
which proves that $L'$ is unramified over $K'$ at $\mathfrak{n}'$. This proves the lemma.

Place ourselves now under the conditions of X.2.4, where one has a **surjective** specialization homomorphism

$$ \pi_{1}(\bar{X}_{1},\bar{a}_{1}) \to \pi_{1}(\bar{X}_{0},\bar{a}_{0}) $$

relative to a proper and separable morphism $f: X \to Y$. We want to make its kernel more precise. Proceeding as in the
proof of X.2.4, one sees that for this question one may always suppose that $Y$ is the spectrum of a **complete discrete
valuation ring $V$ with algebraically closed residue field**, since one can always find such a ring and a morphism from
its spectrum $Y'$ into $Y$ whose image is ${y_{0}, y_{1}}$. Then $X_{0} = \bar{X}_{0}$, $\kappa(y_{0}) = k$ is the
residue field of $V$, and $\kappa(y_{1}) = K$ is the fraction field of $V$. Let $K_{s}$ be the separable closure of $K$,
$\bar{K}$ its algebraic closure, and for every subring $W$ of $\bar{K}$ containing $V$ put $X_{W} = X \otimes_{V} W$. In
particular,

```text
X_V = X,    X_K = X₁,    X_K̄ = X̄₁.
```

Moreover the canonical morphism $\bar{X}_{1} = X_{\bar{K}} \to X_{K_{s}}$ induces an isomorphism on fundamental groups
(IX.4.11). Thus, taking into account the isomorphism X.2.1, $\pi_{1}(X_{0}) \to \pi_{1}(X)$, we are reduced to studying
the surjective homomorphism

```text
π₁(X_K_s) → π₁(X)
```

associated with the canonical morphism $X_{K_{s}} \to X$.

<!-- original page 281 -->

Determining the kernel of this latter homomorphism is equivalent to solving the following problem: **given a connected
principal covering $Z_{K_{s}}$ of $X_{K_{s}}$ with group $G$** (hence associated with a homomorphism from
$\pi_{1}(X_{K_{s}})$ to $G$), **determine under what conditions it is isomorphic to the inverse image of a principal
covering $Z$ of $X$ with group $G$.**

First note that $K_{s}$ is the filtered increasing union of its finite subextensions $K'$ over $K$, and therefore
$Z_{K_{s}}$ is isomorphic to the inverse image of a principal covering $Z_{K'}$ of $X_{K'}$ for a suitable $K'$. Be
careful, however, that for fixed $K'$, $Z_{K'}$ is not uniquely determined. To say that $Z_{K_{s}}$ is isomorphic to the
inverse image of a principal covering $Z$ of $X$ means that there exists a finite subextension $K'' \supset K'$ of
$K_{s}$ such that $Z_{K''} = Z_{K'} \otimes_{K'} K''$ is isomorphic to $Z \otimes_{V} K''$.

Now, for a finite subextension $K'$ of $K_{s}$, denote by $V'$ the normalization of $V$ in $K'$. This is a complete
discrete valuation ring with residue field $k$. The canonical morphism $X_{V'} \to X_{V}$ therefore induces an
isomorphism on the fibers above the closed points of $Y = \operatorname{Spec}(V)$ and $Y' = \operatorname{Spec}(V')$;
applying X.2.1 to `X_V` and $X_{V'}$, it follows that the induced homomorphism on fundamental groups $\pi_{1}(X_{V'})
\to \pi_{1}(X_{V})$ is an isomorphism. Equivalently, every principal covering of $X_{V'}$ is the inverse image of a
principal covering of `X_V`, determined up to isomorphism. This implies:

**Lemma.**

<!-- label: X.3.7 -->

Let $Z_{K'}$ be a connected principal covering of $X_{K'}$ with group $G$, and let $Z_{K_{s}}$ be its inverse image on
$X_{K_{s}}$. Then $Z_{K_{s}}$ is isomorphic to the inverse image of a principal covering $Z$ of $X$ if and only if there
exists a finite extension $K'' \supset K'$ of $K$ in $K_{s}$ such that the principal covering $Z_{K''}$ of $X_{K''}$ is
induced by a principal covering of $X_{V''}$.

Suppose in particular that the $X_{V''}$ are normal. It is enough, for example, that $X_{0}$ be normal, and a fortiori
that $X_{0}$ be simple; cf. I.9.1.

<!-- original page 282 -->

Since they are connected, they are then irreducible. Let $L$ be the field of rational functions of $X$ and `X_K`, let
$L'$ be the field for $X_{V'}$ and $X_{K'}$, and let $L''$ be the field for $X_{V''}$ and $X_{K''}$. Under the
conditions of X.3.7, $Z_{K'}$ defines a finite separable extension $R'$ of $L'$, and $Z_{K''}$ defines the extension
$R'' = R' \otimes_{L'} L'' = R' \otimes_{K'} K''$. The condition considered in X.3.7 therefore also means that there
exists a finite separable extension $K''$ of $K'$ such that $R'' = R' \otimes_{K'} K''$ is **unramified** over the
normal scheme $X_{V''}$ with function field $L'' = L' \otimes_{K'} K''$, and not only over the open part $X_{K''}$ of
$X_{V''}$.

From now on suppose that $f: X \to Y$ is a **smooth** morphism. Then the morphisms $X_{V'} \to \operatorname{Spec}(V')$
are smooth, and therefore the schemes $X_{V'}$ are **regular**. Notice that the fiber of the closed point of
$\operatorname{Spec}(V')$ in $X_{V'}$ is irreducible and of codimension 1. Let $\mathfrak{o}'$ be its local ring; this
is a discrete valuation ring with fraction field $L'$ and residue field isomorphic to the field of rational functions of
$X_{0}$, hence with the same characteristic as $k$. Define similarly $\mathfrak{o}''$ in $L''$; it is plainly the
normalization of $\mathfrak{o}'$ in $L''$. It then follows from the purity theorem X.3.1, or X.3.3, that $R''$ is
unramified over $X_{V''}$ if and only if $R''$ is unramified over $\mathfrak{o}''$, the normalization of $\mathfrak{o}'$
in $L''$.

Now note that if $u'$ is a uniformizer of $V'$, it is also a uniformizer of $\mathfrak{o}'$. If $n$ is an integer prime
to the characteristic $p$ of $k$, and if one takes $K'' = K'[t]/(t^{n} - u')$, then $K''$ is a finite Galois extension
of $K'$ and $L''$ is isomorphic to $L'[t]/(t^{n} - u')$, hence is tamely ramified over $\mathfrak{o}'$ with inertia
group of order $n$. Suppose now that $G$ has order prime to $p$. Then $R'$ is tamely ramified over $\mathfrak{o}'$. Take
$n$ to be a multiple prime to $p$ of the order of the inertia group of $R'$ over $\mathfrak{o}'$, for example $n =
[G:e]$. Applying Abhyankar’s lemma X.3.6, one sees that the condition considered in X.3.7 is satisfied.

This proves the following theorem:

**Theorem.**

<!-- label: X.3.8 -->

Let $f: X \to Y$ be a proper and smooth morphism with geometrically connected fibers, with $Y$ locally noetherian. Let
$y_{0}$ and $y_{1}$ be two points of $Y$ such that $y_{0} \in cl({y_{1}})$, let $\bar{X}_{0}$ and $\bar{X}_{1}$ be the
corresponding geometric fibers, and consider the specialization homomorphism of X.2.4

$$ \pi_{1}(\bar{X}_{1}) \to \pi_{1}(\bar{X}_{0}). $$

This homomorphism is surjective, and every continuous homomorphism from $\pi_{1}(\bar{X}_{1})$ to a finite group $G$ of
order prime to the characteristic $p$ of $\kappa(y_{0})$ comes from a homomorphism from $\pi_{1}(\bar{X}_{0})$ to $G$.

<!-- original page 283 -->

In other words:

**Corollary.**

<!-- label: X.3.9 -->

If $\kappa(y_{0})$ has characteristic zero, then the specialization homomorphism is an isomorphism. If $\kappa(y_{0})$
has characteristic $p > 0$, then the kernel of the specialization homomorphism is contained in the intersection of the
kernels of the continuous homomorphisms from $\pi_{1}(\bar{X}_{1})$ to finite groups of order prime to $p$, or
equivalently in the closed normal subgroup generated by a $p$-Sylow subgroup of the group of galoisian type
$\pi_{1}(\bar{X}_{1})$. Thus, if $\pi_{1}(\bar{X}_{1})^{p}$ denotes the quotient group of $\pi_{1}(\bar{X}_{1})$ by the
preceding closed subgroup, and if $\pi_{1}(\bar{X}_{0})^{p}$ is defined similarly, then the specialization homomorphism
induces an **isomorphism**

$$ \pi_{1}(\bar{X}_{1})^{p} \simeq \pi_{1}(\bar{X}_{0})^{p}. $$

Notice that the proof of X.3.8 is purely algebraic. Proceeding as in X.2.6, one concludes by **transcendental methods**:

**Corollary.**

<!-- label: X.3.10 -->

Let $X_{0}$ be a proper, smooth, connected curve of genus $g$ over an algebraically closed field of characteristic $p$.
With the notation introduced in X.3.9, the group $\pi_{1}(X_{0})^{p}$ is isomorphic to $\Gamma^{p}$, where $\Gamma$ is
the group of galoisian type generated by generators $s_{i}, t_{i}$, $1 \leq i \leq g$, bound by the relation

```text
(s₁t₁s₁⁻¹t₁⁻¹)⋯(s_gt_gs_g⁻¹t_g⁻¹) = 1.
```

**Remarks.**

<!-- label: X.3.11 -->

<!-- original page 284 -->

When $\kappa(y_{0})$ has characteristic zero, the result X.3.9 is well known by transcendental methods. Notice that the
proof of X.3.10 appeals to the purity theorem in the unequal-characteristic case, but only for rings of dimension 2,
where the proof of that theorem is easy and was recalled in the text.

## Bibliography

**[X.1]** K. Kodaira, “On compact analytic surfaces,” _Annals of Mathematics_ **71** (1960), pp. 111–152.

**[X.2]** S. Lang and J.-P. Serre, “Sur les revêtements non ramifiés des variétés algébriques,” _American Journal of
Mathematics_ **79** (1957), pp. 319–330.

**[X.3]** M. Nagata, “On the purity of branch loci in regular local rings,” _Illinois Journal of Mathematics_ **3**
(1959), pp. 328–333.

**[X.4]** J.-P. Serre, _Revêtements ramifiés du plan projectif (d’après S. Abhyankar)_, Séminaire Bourbaki, May 1960.

**[X.5]** O. Zariski, “On the purity of the branch locus of algebraic functions,” _Proceedings of the National Academy
of Sciences USA_ **44** (1958), pp. 791–796.

**[X.6]** O. Zariski, _Algebraic Surfaces_, Ergebnisse, 1948; Chelsea, New York.
