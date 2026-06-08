# Exposé III. Smooth Morphisms: Extension Properties

<!-- label: III -->

<!-- original page 58 -->

## 1. Formally Smooth Homomorphisms

<!-- label: III.1 -->

In II, we limited ourselves to homomorphisms of finite type and, consequently, in local homomorphisms $A \to B$ of local
rings, to the case where B is isomorphic to a localization of an A-algebra of finite type. This case is insufficient for
various applications, notably in formal geometry or analytic geometry. For example, the formal power-series ring $B =
A[[t_{1},...,t_{n}]]$ has, from the point of view of formal geometry, the properties of a smooth algebra over A. In
analytic geometry, the same is true of the local ring of a point (y,z) of a product $Y \times \mathbb{C}^{n}$, regarded
as an algebra over the local ring of y; moreover, the completion of this algebra is isomorphic to the algebra of formal
power series in n indeterminates over the completion of the base ring $\mathcal{O}_{x}$. This leads to the following
definition.

**Definition.**

<!-- label: III.1.1 -->

Let $u: A \to B$ be a local homomorphism of local rings, noetherian as recalled. Suppose that $\kappa(B)$ is finite over
$\kappa(A)$. We say that u is a **formally smooth homomorphism**, or that the algebra B is **formally smooth over** A,
if there exists a local finite $\bar{A}$-algebra $A'$, free over $\bar{A}$, such that the local components of the
semi-local ring $\bar{B} \otimes_{\bar{A}} A' = B'$ are $A'$-isomorphic to algebras of formal power series over
$A'$.[^iii-1-1-1]

Here $\bar{A}$ and $\bar{B}$ denote the completions of A and B. Since $B'$ is finite and free over $\bar{B}$, it is
indeed a semi-local ring, a direct sum of complete local rings, each of which is still a free module over $\bar{B}$,
hence has the same dimension as $\bar{B}$, and therefore as B. It follows that the number of variables $t_{i}$ in the
formal power-series rings considered in III.1.1 is equal to `dim B̄ − dim Ā = dim B − dim A`, and in particular is
independent of the local component chosen. One sees at once that it is also the dimension of the ring $B \otimes k =
B/\mathfrak{m}B$, where $k = A/\mathfrak{m}$ is the residue field of A; we shall call it the **relative dimension of** B
**with respect to** A.

<!-- original page 59 -->

**Remarks.**

<!-- label: III.1.2 -->

It is clear that Definition III.1.1 depends only on the homomorphism on completions $\bar{A} \to \bar{B}$ deduced from
$A \to B$, which justifies the terminology to some extent. We repent here of Definitions I.3.2 b) and I.4.1 b), which
risk being misleading, and prefer to say “formally unramified” and “formally étale” in the cases considered in those
definitions, reserving the terminology “unramified” and “étale” for the case where B is a localization of an A-algebra
of finite type.[^iii-1-2-1] The reader will immediately verify that “formally étale” is equivalent to “formally smooth
and quasi-finite”. Finally, let us point out that there is a reasonable definition of “formally smooth” without any
prior hypothesis on the residual extension $\kappa(B)/\kappa(A)$, supposed finite here, encompassing among others the
local homomorphisms $A \to B$ such that B is **flat** over A and $B/\mathfrak{m}B$ is a **separable extension** of
$A/\mathfrak{m} = k$, not necessarily of finite type. For example, a Cohen p-ring is formally smooth over the ring of
p-adic integers. It is the lifting property for homomorphisms, compare III.2.1, that should become the definition in
this general case. For the applications we have in view, the case treated in Definition III.1.1 will suffice; in what
follows, in “formally smooth” we shall understand “with finite residual extension”.

**Lemma.**

<!-- label: III.1.3 -->

If B is formally smooth over A, then B is flat over A.

Since flatness is invariant under completion, we may suppose A and B complete. Since flatness is invariant under a local
flat, hence faithfully flat, extension of the base ring, Definition III.1.1 reduces us to the case where B is a formal
power-series algebra over A. But then, as an A-module, B is isomorphic to a product of A-modules isomorphic to A; hence,
since the base ring A is noetherian, B is A-flat as a product of flat A-modules.

Let us place ourselves under the conditions of III.1.1. Since the residual extensions of the local components of $B'$
over $A'$ are trivial, it follows that $L \otimes_{k} k'$ is an artinian $k'$-algebra whose local components have
trivial residual extensions, where L, k, $k'$ are the residue fields of A, B, and $A'$. This necessary condition for the
finite free extension $A'$ to satisfy the condition stated in III.1.1 is also sufficient, as follows at once from
III.1.4 (i) and III.1.5 below.

<!-- original page 60 -->

**Proposition.**

<!-- label: III.1.4 -->

Let $A \to B$ be a local homomorphism of local rings with finite residual extension, and let $A'$ be a finite local
A-algebra over A, so that $B' = B \otimes_{A} A'$ is finite over B and hence is a semi-local ring, also noetherian.

1. If B is formally smooth over A, then the localizations of $B'$ at its maximal ideals are formally smooth over $A'$.
1. The converse is true if $A'$ is free over A.

We are immediately reduced to the case where A and B are complete.

For (i), let $A''$ be a finite free local extension of A such that the local components of $B'' = B \otimes_{A} A''$ are
formal power-series algebras over $A''$. Extending scalars $A'' \to A'' \otimes_{A} A' \to A'''$, where $A'''$ is a
local component of $A'' \otimes_{A} A'$, one sees that the local components of $B'' \otimes_{A''} A''' = B \otimes_{A}
A'''$ are formal power-series algebras over $A'''$. But we also have

```text
B ⊗_A A‴ = (B ⊗_A A′) ⊗_{A′} A‴ = B′ ⊗_{A′} A‴.
```

Moreover, since $A''$ is free over A, $A'' \otimes_{A} A'$ is free over $A'$, and consequently so is $A'''$, which is a
direct factor of it. This proves that $B'$ is formally smooth over $A'$.

For (ii), let $A''$ be a finite free local $A'$-algebra such that the local components of $B' \otimes_{A'} A'' = B
\otimes_{A} A''$ are formal power-series algebras over $A''$. Since $A'$ is free over A, so is $A''$; hence B is
formally **smooth** over A.

**Proposition.**

<!-- label: III.1.5 -->

Let $A \to B$ be a local homomorphism of local rings with **trivial** residual extension. In order that B be formally
smooth over A, it is necessary and sufficient that $\bar{B}$ be isomorphic to a formal power-series algebra over
$\bar{A}$.

Only the necessity has to be proved, and we may suppose A and B complete. Let $\mathfrak{m}$ and $\mathfrak{n}$ be the
maximal ideals of A and B, respectively, and let $t_{1},...,t_{n}$ be elements of $\mathfrak{n}$ defining a basis of the
vector space

$$ (\mathfrak{n}/\mathfrak{n}^{2})/Im(\mathfrak{m}/\mathfrak{m}^{2}) = \mathfrak{n}/(\mathfrak{n}^{2} + \mathfrak{m}B).
$$

These elements therefore define a homomorphism of local A-algebras

$$ B_{1} = A[[t_{1},...,t_{n}]] \to B. $$

We prove that it is an isomorphism. It suffices to prove that for every power $\mathfrak{m}^{q}$ of $\mathfrak{m}$, one
obtains an isomorphism after reducing modulo $\mathfrak{m}^{q}$, since $B_{1}$ and B are the projective limits of the
corresponding rings reduced modulo $\mathfrak{m}^{q}$, with q variable. Since B and $B_{1}$ are flat A-modules, the
graded rings associated with the $\mathfrak{m}$-adic filtration are obtained by tensoring over $k = A/\mathfrak{m}$ with
$gr(A)$ the rings $B_{1}/\mathfrak{m}B_{1}$ and $B/\mathfrak{m}B$, respectively. We are thus reduced to showing that
$B_{1}/\mathfrak{m}B_{1} \to B/\mathfrak{m}B$ is an isomorphism. Taking III.1.3 into account, we are thereby reduced to
the case where A is a **field** k. On the other hand, if $A'$ is a finite free local A-algebra such that $B \otimes_{A}
A'$ is a formal power-series algebra over $A'$, note that this algebra is local since the residual extension of B over A
is trivial. To prove that $B_{1} \to B$ is an isomorphism, it suffices to prove that $B_{1} \otimes_{A} A' \to B
\otimes_{A} A'$ is one. This reduces us to the case where B is already a formal power-series algebra; this reduction
should have been made first, before reducing to the case of a base field. But then B is a regular local ring with
coefficient field k, and it is well known, and immediate by considering the graded rings associated with the
$\mathfrak{n}_{1}$-adic and $\mathfrak{n}$-adic filtrations on $B_{1}$ and B, that $B_{1} \to B$ is an isomorphism. This
completes the proof.

**Corollary.**

<!-- label: III.1.6 -->

If B is formally smooth over A, then there exists a finite local A-algebra $A'$ such that the local components of

```text
B̄ ⊗_{Ā} A′̄ = completion of (B ⊗_A A′)
```

are isomorphic to formal power-series algebras over $A\bar{'}$.

Indeed, if L/k is the residual extension of B/A, consider an extension $k'/k$ such that the residual extensions in the
$k'$-algebra $L \otimes_{k} k'$ are trivial. Let $A'$ be an algebra finite and free over A such that $A'/\mathfrak{m}A'
= k'$; one knows that such an algebra exists, for example by reducing step by step to the case where $k'/k$ is
monogenic, and then lifting to A the coefficients of the minimal polynomial of a generator of $k'$ over k. It is local.
Then $B \otimes_{A} A'$ has, at its maximal ideals, trivial residual extensions over that $k'$ of $A'$, and the
conclusion follows with the help of III.1.5.

**Corollary.**

<!-- label: III.1.7 -->

Let $A \to B$ be a local homomorphism of local rings. In order that B be formally smooth over A, it is necessary and
sufficient that B be flat over A and that $B/\mathfrak{m}B$ be formally smooth over $k = A/\mathfrak{m}$.

Making a suitable finite free local extension $A'$ of A and using III.1.4 (ii), we are reduced to the case where the
residual extension of B/A is trivial. We know moreover by III.1.4 (i) and III.1.3 that the stated conditions are
necessary. For the sufficiency, it suffices to observe that the proof of III.1.5 proves, under the hypotheses made here,
that B is a formal power-series algebra over A, supposing A and B complete, which is permissible.

<!-- original page 62 -->

**Remark.**

<!-- label: III.1.8 -->

It would not be difficult to develop, for formally smooth homomorphisms, the analogue of all the properties of smooth
morphisms studied in II. For the differential properties, however, this requires a modification of the usual definition
of Kähler differentials, cf. I.1, with completed tensor products replacing ordinary tensor products. We shall content
ourselves with evoking these abysses here, what precedes being sufficient for our purpose.

It remains to make the link between formal smoothness and the notion of smoothness developed in II, which we have not
yet used at all.

**Proposition.**

<!-- label: III.1.9 -->

Let $A \to B$ be a local homomorphism, with B a localization of an A-algebra of finite type. In order that B be smooth
over A, it is necessary and sufficient that it be formally smooth over A.

Using III.1.7 and II.2.1, we are reduced to the case where A is a field.

Using III.1.4 (ii) and II.4.13, a suitable extension $k'$ of k reduces us to the case where the residual extension for
B/k is trivial. By III.1.5, respectively II.5.2, B is smooth over k, respectively formally **smooth over** k, if and
only if B is a regular local ring, respectively its completion is a formal power-series algebra over k. But it is well
known that these two conditions are equivalent when the residual extension is trivial.

## 2. The Lifting Property Characteristic of Formally Smooth Homomorphisms

<!-- label: III.2 -->

**Theorem.**

<!-- label: III.2.1 -->

Let $A \to B$ be a local homomorphism of local rings defining a finite residual extension. The following conditions are
equivalent:

1. B is formally smooth over A.
1. For every local homomorphism $A \to C$, where C is a **complete** local ring, every ideal J of C contained in the
   radical $\mathfrak{r}(C)$, and every local A-homomorphism $B \to C/J$, there exists an A-homomorphism, necessarily
   local, $B \to C$ lifting it.
1. For every A-algebra C, not necessarily noetherian, every nilpotent ideal J of C, and every continuous A-homomorphism
   $B \to C/J$, i.e. one vanishing on a power of $\mathfrak{r}(B)$, there exists an A-homomorphism $B \to C$,
   necessarily continuous as well, lifting it.
1. The same statement as (ii) and (iii), but with C a local artinian ring finite over A.
1. As in (iv), but with J moreover square-zero.

**Remark.** For the rest of this exposé, we shall use only the implication (iv) ⇒ (i), or (iv bis) ⇒ (i). The direct
implication (i) ⇒ (ii) will be proved by another method in the next number when B is a localization of an algebra of
finite type over A. Recall that in the “good” theory of Cohen theorems,[^iii-2-1-1] property (ii) or (iii) becomes the
definition of formally smooth homomorphisms, while III.1.1 becomes a characteristic property valid only in the case of a
finite residual extension. Care should be taken that neither of properties (ii) and (iii) is more general than the
other. One could give an equivalent property covering both by introducing a linearly topologized ring C, **separated**
and **complete**, a **closed topologically nilpotent** ideal of C, and a continuous homomorphism $A \to C$, thus making
C a topological A-algebra; we leave this modification to the reader.

**Proof of III.2.1.** We shall prove (i) ⇒ (iii) ⇒ (ii), then (iv) ⇒ (i). Since (ii) ⇒ (iv) is trivial, and the
equivalence of (iv) and (iv bis) is seen by an immediate induction on the integer n such that $J^{n} = 0$, this will
finish the proof.

(i) ⇒ (iii). An immediate induction reduces us to the case J² = 0. Since C is finite over A, some power
$\mathfrak{m}^{q}$ of the maximal ideal of A annihilates C. Dividing by $\mathfrak{m}^{q}$, and noting that
$B/\mathfrak{m}^{qB}$ is still formally smooth over $A/\mathfrak{m}^{q}$ by III.1.4 (i), we may suppose A artinian.
Since B is flat over A by III.1.3, B **is free over** A because A is artinian. Thus there exists an **A-module
homomorphism**

$$ w: B \to C $$

lifting the given homomorphism $u: B \to C/J$. Put

```text
f(x,y) = w(xy) − w(x)w(y),     x,y ∈ B.
```

Then f(x,y) ∈ J, and f is therefore an A-bilinear map from $B \times B$ to J. For there to exist a lift $v: B \to C$ of
u that is an algebra homomorphism, it is necessary and sufficient that there exist an A-linear map $g: B \to J$ such
that $v = w + g$ is an algebra homomorphism, which is written

```text
g(1) = 1 − w(1),
g(xy) − u(x)g(y) − u(y)g(x) = −f(x,y),     x,y ∈ B.
```

This is a system of **linear** equations in $\operatorname{Hom}_{A}(B,J)$, with right-hand sides in J. Hence it has a
solution if and only if the corresponding system in $\operatorname{Hom}_{A}(B,J) \otimes_{A} A'$, with right-hand sides
in $J' = J \otimes_{A} A'$, has a solution, where $A'$ denotes a faithfully flat algebra over A. Let $A'$ be an algebra
finite and free over A, local, such that $B' = B \otimes_{A} A'$ is a formal power-series algebra over $A'$. In our
proof we may suppose A and B complete, as is immediately checked. Since $A'$ is free of finite type over A, we have

```text
Hom_A(B,J) ⊗_A A′ = Hom_{A′}(B′,J′),
```

and one verifies that the system of equations obtained in $\operatorname{Hom}_{A'}(B',J')$ is the one that determines
the homomorphisms of $A'$-algebras $B' \to C' = C \otimes_{A} A'$ lifting the homomorphism $u': B' \to C'/J'$ deduced
from u by extension of scalars, by “correcting” by an $A'$-module homomorphism $g': B' \to J'$ the $A'$-module
homomorphism $w': B' \to C'$ deduced from w by extension of scalars. Note that B generates $B'$ as an $A'$-module. We
are thereby reduced to proving (iii) when B is a **formal power-series algebra** over A, $B = A[[t_{1},...,t_{n}]]$.
Lift arbitrarily the images in C/J of the $t_{i}$ to elements $z_{i}$ of C. Since the $z_{i}$ modulo J are nilpotent,
$u: B \to C/J$ being continuous, the $z_{i}$ themselves are nilpotent, since J is nilpotent. Thus the $z_{i}$ define a
continuous homomorphism of topological A-algebras from B to the discrete ring C, evidently lifting u, as required.

(iii) ⇒ (ii). Let $\mathfrak{n}$ be the maximal ideal of C, and for every integer q > 0 put

```text
C_q = C/𝔫^q,    J_q = (J + 𝔫^q)/𝔫^q.
```

Thus $C_{q}/J_{q}$ identifies with a quotient algebra of C/J. On the other hand, the composite homomorphism $u_{q}: B
\to C/J \to C_{q}/J_{q}$ is continuous from B to the discrete ring $C_{q}/J_{q}$, and $J_{q}$ is a nilpotent ideal in
$C_{q}$. We then construct, step by step, A-homomorphisms

$$ v_{q}: B \to C_{q} $$

such that (a) $v_{q}$ lifts $u_{q}$ and (b) $v_{q}$ lifts $v_{q-1}$. The possibility of the induction is checked easily:
since

```text
u_q: B → C/(J + 𝔫^q)     and     v_{q−1}: B → C/𝔫^{q−1}
```

define the same homomorphism

```text
B → C/((J + 𝔫^q) + 𝔫^{q−1}) = C/(J + 𝔫^{q−1}) = C_{q−1}/J_{q−1},
```

namely $u_{q-1}$, they define a homomorphism

```text
B → C/J′_q,    where J′_q = (J + 𝔫^q) ∩ 𝔫^{q−1} ⊃ 𝔫^q,
```

from which both arise by reduction. We are therefore reduced to lifting a homomorphism $B \to C/J'_{q}$ from B into a
quotient of $C_{q}$ by an ideal $J'_{q}/\mathfrak{n}^{q}$ contained in $J_{q}$, hence nilpotent; this is possible by
hypothesis (iii).

This done, the $v_{q}$ define a homomorphism from B into the projective limit C of the $C_{q}$. Since J is closed, J is
the projective limit of the $J_{q}$; hence v lifts u, as required.

(iv) ⇒ (i). First one observes at once that if (iv) holds, then (iv) remains true for the local components of $B
\otimes_{A} A'$ over $A'$, if $A'$ is a finite local algebra over A. Taking $A'$ free over A and such that the residual
extensions of $B'$ over $A'$ are trivial, we are reduced, by III.1.4 (ii), to the case where the residual extension of B
over A is trivial. We shall then prove the slightly more precise result:

**Corollary.**

<!-- label: III.2.2 -->

Under the conditions of III.2.1, suppose moreover that the residual extension of B over A is trivial. Then the
equivalent conditions of III.2.1 are also equivalent to the following two conditions, supposing in (v) that A and B are
complete:

1. As in (iv), but with the local artinian ring C finite over A restricted to have trivial residual extension; and
   moreover, if one wants, with the ideal J square-zero.
1. There exists a local A-homomorphism, where $n = \dim \mathfrak{n}/(\mathfrak{n}^{2} + \mathfrak{m}B)$,

```text
u: B → B₁ = A[[t₁,...,t_n]]
```

inducing an **isomorphism**

```text
𝔫/(𝔫² + 𝔪B) → 𝔫₁/(𝔫₁² + 𝔪B₁),
```

where $\mathfrak{n}$ and $\mathfrak{n}_{1}$ are the maximal ideals of B and $B_{1}$, respectively, and $\mathfrak{m}$ is
that of A.

**Proof.** Since (iv bis) evidently implies (iv ter), setting aside the square-zero-ideal joke, it will suffice to prove
(iv ter) ⇒ $(v) \Rightarrow (i)$.

For (iv ter) ⇒ (v), choose a basis $a_{1},...,a_{n}$ of $\mathfrak{n}/(\mathfrak{n}^{2} + \mathfrak{m}B)$. This
therefore defines a local homomorphism of A-algebras

```text
B → B₁/(𝔫₁² + 𝔪B₁) = k[t₁,...,t_n]/(t₁,...,t_n)²,
```

which can be lifted step by step, by (iv ter), to homomorphisms of A-algebras from B into $B_{1}/\mathfrak{n}^{2}_{1}$,
$B_{1}/\mathfrak{n}^{3}_{1}$, and so on; passing to the projective limit gives the homomorphism $B \to B_{1}$ with the
desired property.

For $(v) \Rightarrow (i)$, in the commutative diagram

```text
𝔪/𝔪² → 𝔫/𝔫² → 𝔫/(𝔫² + 𝔪B) → 0
↓       ↓       ↓
𝔪/𝔪² → 𝔫₁/𝔫₁² → 𝔫₁/(𝔫₁² + 𝔪B₁) → 0
```

the two rows are exact, and the extreme vertical arrows are surjective; the middle arrow is therefore surjective, and it
follows, since B is complete, that $B \to B_{1}$ is **surjective**. Let $x_{i}$, $1 \leq i \leq n$, be elements of B
lifting the $t_{i}$. They define a homomorphism of A-algebras $B_{1} \to B$, which is surjective for the same reason as
u, and whose composite with u is the identity by construction. Thus $B_{1} \to B$ is also injective, and consequently is
an isomorphism. We obtain:

**Corollary.**

<!-- label: III.2.3 -->

Under the conditions of III.2.2 (v), u is necessarily an isomorphism.

This finishes the proof that B is formally smooth over A. At the same time we have recovered III.1.5, though there is
little merit in that.

## 3. Local Infinitesimal Extension of Morphisms into a Smooth S-Scheme

<!-- label: III.3 -->

**Theorem.**

<!-- label: III.3.1 -->

Let $f: X \to Y$ be a morphism locally of finite type. The following conditions are equivalent:

1. f is smooth.
1. For every prescheme $Y'$ over Y, every closed sub-prescheme $Y'_{0}$ of $Y'$ having the same underlying space as
   $Y'$, every Y-morphism $g_{0}: Y'_{0} \to X$, and every $z \in Y'_{0}$, there exists an open neighborhood U of z in
   $Y'$ and an extension g of $g_{0}|_{Y'_{0} \cap U}$ to a Y-morphism $U \to X$.
1. For $Y'$, $Y'_{0}$, and z as in (ii), putting $X' = X \times_{Y} Y'$ and $X'_{0} = X \times_{Y} Y'_{0}$, every
   section of $X'_{0}$ over $Y'_{0}$ extends to a section of $X'$ over an open neighborhood U of z.
1. For every Y-scheme $Y'$ that is the spectrum of a local artinian ring finite over some $\mathcal{O}_{y}$, with $y \in
   Y$, every nonempty closed sub-prescheme $Y'_{0}$ of $Y'$, and every Y-morphism $g_{0}: Y'_{0} \to X$, there exists a
   Y-morphism $g: Y' \to X$ extending $g_{0}$.
1. For every $Y'$ and $Y'_{0}$ as in (iii), putting $X' = X \times_{Y} Y'$ and $X'_{0} = X \times_{Y} Y'_{0}$, every
   section of $X'_{0}$ over $Y'_{0}$ extends to a section of $X'$ over $Y'$.

**Proof.** The equivalence of (ii) and (ii bis), on the one hand, and of (iii) and (iii bis), on the other, is trivial,
as is the implication (ii) ⇒ (iii). It remains to prove (i) ⇒ (ii) and (iii) ⇒ (i).

(i) ⇒ (ii). Let $x = g_{0}(z)$. Replacing X by a suitable open neighborhood of x, and $Y'$ by the prescheme induced on
the open inverse image of the latter under $g_{0}$, we may suppose that X is étale over $Y[t_{1},...,t_{n}]$. Consider
the composite Y-morphism $Y'_{0} \to X \to Y[t_{1},...,t_{n}]$; it is defined by n sections of the sheaf
$\mathcal{O}_{Y'_{0}}$, which can therefore be extended in a neighborhood of z to sections of $\mathcal{O}_{Y'}$. Thus
we may suppose that the morphism in question has been extended to a Y-morphism $Y' \to Y[t_{1},...,t_{n}]$. By I.5.6,
there is then a unique Y-morphism $g: Y' \to X$ lifting the preceding one and at the same time extending $g_{0}$.

<!-- original page 68 -->

(iii) ⇒ (i). Since the set of points where f is smooth is open, it suffices to prove that it contains every $x \in X$
that is **closed** in its fiber. Let y = f(x). Then $\mathcal{O}_{x}$ is an algebra over $\mathcal{O}_{y}$, a
localization of an algebra of finite type, with finite residual extension. On the other hand, hypothesis (iii) implies
that every homomorphism from $\mathcal{O}_{x}$ into an algebra A/J, where A is a local artinian algebra finite over
$\mathcal{O}_{y}$ and J is an ideal contained in its radical, lifts to a homomorphism from $\mathcal{O}_{x}$ into the
algebra A, taking into account that a morphism from $\operatorname{Spec}(B)$, with B local, into X is determined
bijectively by a local homomorphism from some $\mathcal{O}_{x}$, $x \in X$, into B. By III.2.1 it follows that
$\mathcal{O}_{x}$ is formally smooth over $\mathcal{O}_{y}$, hence smooth over $\mathcal{O}_{y}$ by III.1.9.

**Corollary.**

<!-- label: III.3.2 -->

Let $f: X \to Y$ be as in III.3.1. The following conditions are equivalent:

1. f is étale.
1. Condition (ii) of III.3.1 holds with **uniqueness** of the extension g of $g_{0}$ to U.
1. Condition (iii) of III.3.1 holds with **uniqueness** of g.

It suffices to note, in the proof of (i) ⇒ (ii) above, that one can have uniqueness, when $Y'_{0}$ is not identical to
$Y'$ in a neighborhood of z, only if $n = 0$, a condition that is known to be sufficient.

**Corollary.**

<!-- label: III.3.3 -->

Let X be a prescheme locally of finite type over a **complete** local ring A, let y be the closed point of $Y =
\operatorname{Spec}(A)$, and let x be a point of $f^{-1}(y)$ **rational** over $\kappa(y)$. If X is **smooth over A at
x**, then there exists a section s of X over Y “passing through x”, i.e. such that s(y) = x.

In particular, if X is smooth over A, then the natural map

```text
Γ(X/Y) → Γ(X ⊗_A k / k)
```

from sections of X over Y to the set of points of the fiber $f^{-1}(y) = X \otimes_{A} k$ rational over k is surjective.
This fact was especially well known and used when A is a discrete valuation ring and X is proper over A, in fact
projective over A. In that case the sections of X over Y, i.e. the “points of X with values in A”, also identify with
the rational sections, i.e. with the points of $X \otimes_{A} K = X_{K}$, which is a proper smooth scheme over K, with
values in K, the field of fractions of A; in other words, with the points of X rational over K.

## 4. Local Infinitesimal Extension of Smooth S-Schemes

<!-- label: III.4 -->

**Theorem.**

<!-- label: III.4.1 -->

Let Y be a locally noetherian prescheme, let $Y_{0}$ be a closed sub-prescheme with the same underlying space, let
$X_{0}$ be a smooth $Y_{0}$-prescheme, and let x be a point of $X_{0}$. Then there exist an open neighborhood $U_{0}$ of
x, a prescheme X smooth over Y, and a $Y_{0}$-isomorphism

```text
h: U₀ → X ×_Y Y₀.
```

Moreover, if `(U′₀`, $X'$, `h′)` is another solution of this problem, then “it is isomorphic to the first in a
neighborhood of x”.

We leave it to the reader to make precise what is meant by this. One may note that, for $U_{0}$ given, a solution of the
stated problem amounts to giving on $U_{0}$ a sheaf of algebras $\mathcal{B}$ over $f^{-1}_{0}(\mathcal{O}_{Y})$, where
$f_{0}$ is the continuous map underlying the structural morphism $U_{0} \to Y_{0}$, together with a homomorphism of
rings $\mathcal{B} \to \mathcal{O}_{U_{0}}$ compatible with the homomorphism $f^{-1}(\mathcal{O}_{Y}) \to
f^{-1}(\mathcal{O}_{Y_{0}})$, such that:

1. This homomorphism induces an isomorphism

```text
ℬ ⊗_{f⁻¹(𝒪_Y)} f⁻¹(𝒪_{Y₀}) → 𝒪_{Y₀}.
```

1. $U_{0}$ equipped with $\mathcal{B}$ becomes a smooth Y-prescheme.

In this way the precise meaning of the assertion of local uniqueness becomes particularly evident.

**Proof.** We may already suppose that $X_{0}$ is étale over some $Y_{0}[t_{1},...,t_{n}] = Y'_{0}$. But the latter may
be regarded as a closed sub-prescheme of $Y' = Y[t_{1},...,t_{n}]$ having the same underlying space. By I.8.3, there
exists an X étale over $Y'$ and a $Y'_{0}$-isomorphism $X \times_{Y'} Y'_{0} \to X'$. We have won existence. For
uniqueness, use property III.3.1 (ii) of smooth morphisms, taking into account the following lemma.

<!-- original page 70 -->

**Lemma.**

<!-- label: III.4.2 -->

Let Y be a prescheme, let $Y_{0}$ be a closed sub-prescheme defined by a locally nilpotent sheaf of ideals
$\mathcal{J}$, let X and $X'$ be Y-preschemes, and let $u: X \to X'$ be a Y-morphism. Suppose X is flat over Y. In order
that u be an isomorphism, it is necessary and sufficient that

```text
u₀: X ×_Y Y₀ → X′ ×_Y Y₀
```

be an isomorphism.

The proof is easy, by passing to the affine case and looking at associated graded rings. One should note moreover that
the analogous statement obtained by replacing “isomorphism” by “closed immersion” is also valid, and without the
flatness hypothesis.

**Remark.**

<!-- label: III.4.3 -->

It is essential to note that the local extension X obtained in III.4.1 **is not canonical**; in other words, the local
isomorphism between two solutions is not unique, i.e. in general there exist nontrivial Y-automorphisms of X inducing
the identity on the closed sub-prescheme $X_{0} = X \times_{Y} Y_{0}$. This is why, for the construction of **global**
infinitesimal extensions of smooth preschemes, one must expect the existence of an obstruction of cohomological nature,
which will be made precise below in III.6.

## 5. Global Infinitesimal Extension of Morphisms

<!-- label: III.5 -->

Let T be a topological space, let $\mathcal{G}$ be a sheaf of groups on X, and let $\mathcal{P}$ be a sheaf of sets on T
on which $\mathcal{G}$ acts, on the right to fix ideas. We say that $\mathcal{P}$ is **formally principal homogeneous**
under $\mathcal{G}$ if the familiar homomorphism

```text
𝒢 × 𝒫 → 𝒫 × 𝒫
```

of sheaves of sets, deduced from the operations of $\mathcal{G}$ on $\mathcal{P}$, is an **isomorphism**. This is
equivalent to saying that for every $x \in T$, $\mathcal{P}_{x}$ is **empty or a principal homogeneous space** under the
ordinary group $\mathcal{G}_{x}$; or also that for every open U of T, $\mathcal{P}(U)$ is empty or a principal
homogeneous space under the ordinary group $\mathcal{G}(U)$. We say that $\mathcal{P}$ is a **principal homogeneous
sheaf** under $\mathcal{G}$ if it is so formally and if, in addition, the $\mathcal{P}_{x}$ are nonempty; in other
words, if **all** the $\mathcal{P}_{x}$ are principal homogeneous spaces, hence nonempty, under the
$\mathcal{G}_{x}$.[^iii-5-0-1] Recall that the set of classes, up to isomorphism, of principal homogeneous sheaves under
$\mathcal{G}$ identifies with the cohomology set $H^{1}(T,\mathcal{G})$, which is also the usual cohomology group of T
with coefficients in $\mathcal{G}$ when $\mathcal{G}$ is commutative. Thus, for every principal homogeneous
$\mathcal{P}$, there is a characteristic class $c(\mathcal{P}) \in H^{1}(T,\mathcal{G})$, whose triviality is necessary
and sufficient for $\mathcal{P}$ to be trivial, i.e. isomorphic to $\mathcal{G}$, on which $\mathcal{G}$ acts by right
translations, or equivalently for $\mathcal{P}$ to have a section.

**Proposition.**

<!-- label: III.5.1 -->

Let S be a prescheme, let X and Y be preschemes over S, and let $Y_{0}$ be a closed sub-prescheme of Y defined by an
ideal $\mathcal{J}$ on Y **of square zero**. Let $g_{0}$ be an S-morphism from $Y_{0}$ to X, and let
$\mathcal{P}(g_{0})$ be the sheaf on Y whose sections on an open U are the extensions $g: U \to X$ of $g_{0}|_{U \cap
Y_{0}}$ to an S-morphism g. Then $\mathcal{P}(g_{0})$ is, naturally, a **formally principal homogeneous** sheaf under
the commutative sheaf of groups

$$ \mathcal{G} = \operatorname{Hom}_{\mathcal{O}_{Y_{0}}}(g_{0}*(\Omega^{1}_{X/S}), \mathcal{J}). $$

Put $\mathcal{P} = \mathcal{P}(g_{0})$. For every open U of Y we must define a map

$$ \mathcal{P}(U) \times \mathcal{G}(U) \to \mathcal{P}(U) $$

so that: for fixed $g \in \mathcal{P}(U)$, the map s ↦ gs from $\mathcal{G}(U)$ to $\mathcal{P}(U)$ is bijective;
$\mathcal{P}(U)$ becomes a set with group of operators $\mathcal{G}(U)$; and these maps are compatible with restriction
operators for an open $V \subset U$. The verification of the last point is trivial, so for simplicity we may suppose $U
= Y$. The verification of the second point, which is local if one wants, is left to the reader. We shall limit
ourselves, for a given $g \in \mathcal{P}(Y)$, to defining a natural bijection from $\mathcal{G}(Y)$ onto
$\mathcal{P}(Y)$. Thus suppose already given an S-morphism $g: Y \to X$, and seek a canonical bijection

$$ \operatorname{Hom}_{\mathcal{O}_{Y_{0}}}(g_{0}*(\Omega^{1}_{X/S}), \mathcal{J}) \to \mathcal{P}(Y), $$

<!-- label: eq:III.5.1.* -->

where $\mathcal{P}(Y)$ is the set of S-morphisms $g'$ from Y to X inducing the same morphism $g_{0}: Y_{0} \to X$ as g.
Giving such a $g'$ is equivalent to giving an S-morphism $h: Y \to X \times_{S} X$ such that $pr_{1} \circ h = g$ and $h
\circ i = (g_{0},g_{0})$, where $pr_{1}: X \times_{S} X \to X$ is the first projection, $i: Y_{0} \to Y$ is the
canonical immersion, and $(g_{0},g_{0}): Y_{0} \to X \times_{S} X$ is the morphism $\Delta_{X/S} g_{0}$ with components
$g_{0},g_{0}:$

```text
Y₀ --h₀=(g₀,g₀)--> X ×_S X
|                         |
i                         pr₁
v                         v
Y  --------g----------->  X
```

Since $h_{0}$ factors through the diagonal immersion $\Delta_{X/S}$, and since Y is in the first-order infinitesimal
neighborhood of $Y_{0}$, i.e. $\mathcal{J}^{2} = 0$, the desired h necessarily factor, uniquely, through the first-order
infinitesimal neighborhood of the diagonal. This neighborhood identifies, as an X-prescheme via $pr_{1}$, with the
spectrum $X'$ of the sheaf of algebras $\mathcal{O}_{X} + \Omega^{1}_{X/S}$, where the second term is regarded as a
square-zero ideal; the diagonal morphism $X \to X'$ corresponds to the canonical augmentation of this sheaf of algebras.
Put $Y' = X' \times_{X} Y$ and $Y'_{0} = Y' \times_{Y} Y_{0} = X' \times_{X} Y_{0}$. The desired h are then in bijective
correspondence with sections u of $Y'$ over Y extending a given section $u_{0}$ of $Y'_{0}$ over $Y_{0}$. We may
moreover identify $Y'$ with the spectrum of the sheaf of algebras on Y

```text
𝒜 = g*(𝒪_X + Ω¹_{X/S}) = 𝒪_Y + g*(Ω¹_{X/S}),
```

and $Y'_{0}$ with the sheaf of algebras

```text
𝒜₀ = 𝒜 ⊗_{𝒪_Y} 𝒪_{Y₀} = 𝒪_{Y₀} + g₀*(Ω¹_{X/S}).
```

Then $u_{0}$ is the section defined by the canonical augmentation of $\mathcal{A}_{0}$ into $\mathcal{O}_{Y_{0}}$. Thus
$\mathcal{P}(Y)$ identifies with the set of algebra homomorphisms $\mathcal{A} \to \mathcal{O}_{Y}$ inducing the
canonical augmentation $\mathcal{A}_{0} \to \mathcal{O}_{Y_{0}}$. But the algebra homomorphisms $\mathcal{A} \to
\mathcal{O}_{Y}$ correspond bijectively to module homomorphisms $\mathcal{M} \to \mathcal{O}_{Y}$, putting for
simplicity $\mathcal{M} = g*(\Omega^{1}_{X/S})$, and we are interested in those inducing the **zero** homomorphism
$\mathcal{M}_{0} \to \mathcal{O}_{Y_{0}}$, where $\mathcal{M}_{0} = \mathcal{M} \otimes_{\mathcal{O}_{Y}}
\mathcal{O}_{Y_{0}}$; that is, those sending $\mathcal{M}$ into the augmentation ideal $\mathcal{J}$. We therefore find
the set

$$ \operatorname{Hom}_{\mathcal{O}_{Y}}(\mathcal{M},\mathcal{J}) =
\operatorname{Hom}_{\mathcal{O}_{Y_{0}}}(\mathcal{M}_{0},\mathcal{J}), $$

since $\mathcal{J}$ is annihilated by $\mathcal{J}$. This is the desired canonical bijection $III.5.1.*$.

Taking into account the implication (i) ⇒ (iii) in III.3.1, one obtains:

**Corollary.**

<!-- label: III.5.2 -->

<!-- original page 73 -->

If X is smooth over S, at least at the points of $g_{0}(Y_{0})$, then $\mathcal{P}$ is even a **principal homogeneous
sheaf** under the commutative sheaf of groups $\mathcal{G}$, which in this case may also be written

```text
𝒢 = g₀*(𝔤_{X/S}) ⊗_{𝒪_{Y₀}} 𝒥,
```

where $\mathfrak{g}_{X/S}$ is the sheaf on X dual to $\Omega^{1}_{X/S}$, i.e. the **tangent sheaf**, or **sheaf of
derivations**, of X relative to S. This last formula comes from the fact that $\Omega^{1}_{X/S}$ is then free of finite
type.

In particular, this principal homogeneous sheaf determines a cohomology class in $H^{1}(Y_{0},\mathcal{G})$, whose
vanishing is necessary and sufficient for the existence of an S-morphism g extending $g_{0}$. And if such an extension
exists, the set of all possible extensions is a homogeneous space under the group $H^{0}(Y_{0},\mathcal{G})$.

In applying the methods of formal geometry, the situation is most often the following. We are given two S-preschemes X
and Y, and a coherent ideal $\mathcal{I}$ on S. Let $S_{n}$ denote the closed sub-prescheme of S defined by
$\mathcal{I}^{n+1}$, and put

```text
X_n = X ×_S S_n,    Y_n = Y ×_S S_n.
```

Suppose we have an $S_{n}$-morphism

$$ g_{n}: Y_{n} \to X_{n} $$

or, what amounts to the same thing, an S-morphism $Y_{n} \to X$, or again an $S_{n+1}$-morphism $Y_{n} \to X_{n+1}$,
since such a morphism necessarily induces $Y_{n} \to X_{n}$. We seek to extend it to an $S_{n+1}$-morphism

$$ g_{n+1}: Y_{n+1} \to X_{n+1}. $$

If this can be continued indefinitely, one obtains a morphism $\hat{Y} \to \hat{X}$ for the formal preschemes obtained
by completing Y and X for the ideals $\mathcal{I}\mathcal{O}_{Y}$ and $\mathcal{I}\mathcal{O}_{X}$. We may apply III.5.1
with $(S,X,Y,Y_{0},g_{0})$ replaced by `(S_{n+1}`, $X_{n+1}$, $Y_{n+1}$, $Y_{n}$, `g_n)`. The sheaf $\mathcal{G}$ here
becomes the sheaf of module homomorphisms from $g_{n}*(\Omega^{1}_{X_{n+1}/S_{n+1}})$ into

$$ \mathcal{J} = \mathcal{I}^{n+1}\mathcal{O}_{Y} / \mathcal{I}^{n+2}\mathcal{O}_{Y}. $$

Since $\mathcal{J}$ is annihilated by $\mathcal{I}\mathcal{O}_{Y}$, we may then replace
$g_{n}*(\Omega^{1}_{X_{n+1}/S_{n+1}})$ by the sheaf it induces on $Y_{0}$, namely $h_{0}*(\Omega^{1}_{X/S})$, where
$h_{0}$ is the composite $Y_{0} \to Y_{n} \to X_{n+1}$, or again the composite $Y_{0} \to X_{0} \to X_{n+1}$, where
$g_{0}: Y_{0} \to X_{0}$ is induced by $g_{n}$. Since the inverse image of $\Omega^{1}_{X_{n+1}/S_{n+1}}$ on $X_{0} =
X_{n+1} \times_{S_{n+1}} S_{0}$ is $\Omega^{1}_{X_{0}/S_{0}}$, one sees that one also has

```text
𝒢 = Hom_{𝒪_{Y₀}}(g₀*(Ω¹_{X₀/S₀}), 𝓘^{n+1}𝒪_Y / 𝓘^{n+2}𝒪_Y).
```

Thus we obtain:

**Corollary.**

<!-- label: III.5.3 -->

Let S, X, Y, $\mathcal{I}$, and $g_{n}$ be as above, and let $\mathcal{P}(g_{n})$ be the sheaf on Y whose sections on an
open U are the extensions $g_{n+1}$ of $g_{n}$ to an $S_{n+1}$-morphism $Y_{n+1} \to X_{n+1}$. Then $\mathcal{P}(g_{n})$
is a formally principal homogeneous sheaf under the sheaf of groups

$$ \mathcal{G} = \operatorname{Hom}_{\mathcal{O}_{Y_{0}}}(g_{0}*(\Omega^{1}_{X_{0}/S_{0}}),
gr^{n+1}_{\mathcal{I}\mathcal{O}_{Y}}(\mathcal{O}_{Y})). $$

In particular:

**Corollary.**

<!-- label: III.5.4 -->

If moreover X is smooth over S, at least at the points of $g_{0}(Y_{0})$, then $\mathcal{P}(g_{n})$ is even a principal
homogeneous sheaf. In particular, it defines an obstruction class in $H^{1}(Y_{0},\mathcal{G})$, whose vanishing is
necessary and sufficient for the existence of a global extension $g_{n+1}$ of $g_{n}$. And if such an extension exists,
the set of all global extensions is a principal homogeneous space under $H^{0}(Y_{0},\mathcal{G})$. Finally, in the case
considered, the sheaf $\mathcal{G}$ may also be written

```text
𝒢 = g₀*(𝔤_{X₀/S₀}) ⊗_{𝒪_{Y₀}} gr^{n+1}_{𝓘𝒪_Y}(𝒪_Y).
```

Proceeding step by step, one sees therefore that if all the $H^{1}(Y_{0},\mathcal{G}_{n})$ vanish, where

$$ \mathcal{G}_{n} = g_{0}*(\mathfrak{g}_{X_{0}/S_{0}}) \otimes gr^{n}_{\mathcal{I}\mathcal{O}_{Y}}(\mathcal{O}_{Y}), $$

then, starting with an arbitrary $g_{k}$, one can extend it successively to $g_{k+1}$, and so on. In particular, if
$\mathcal{I}$ is nilpotent, one will be able to find an extension g of $g_{k}$ to Y. The vanishing condition for the H¹
is satisfied in particular if $Y_{0}$ is affine. Thus one obtains:

**Corollary.**

<!-- label: III.5.5 -->

<!-- original page 75 -->

In the statement of Theorem III.3.1, one obtains a necessary and sufficient condition equivalent to the others by
supposing that the $Y'$ occurring in (ii), or (ii bis), is affine, and by requiring the existence of a **global
extension** g of $g_{0}$ to all of $Y'$.

Note that the proof of III.3.1 could not have given this result directly.

An important case is that where Y is **flat** over S. Then one has

```text
gr^n(𝒪_Y) = gr^n(𝒪_S) ⊗_{𝒪_{S₀}} 𝒪_{Y₀},
```

and when, moreover, the $gr^{n}(\mathcal{O}_{S})$ are **locally free on** S, one finds

```text
𝒢_n = Hom_{𝒪_{Y₀}}(g₀*(Ω¹_{X₀/S₀}), 𝒪_{Y₀}) ⊗_{𝒪_{S₀}} gr^n(𝒪_S),
```

or again, if $\Omega^{1}_{X_{0}/S_{0}}$ is itself locally free, for example if X is smooth over S,

```text
𝒢_n = g₀*(𝔤_{X₀/S₀}) ⊗_{𝒪_{S₀}} gr^n(𝒪_S).
```

If, for example, S is affine with affine ring A, and $\mathcal{I}$ is defined by an ideal I of A, one finds

```text
H^i(Y₀,𝒢_n) = H^i(Y₀,𝒢₀) ⊗_A gr_I^n(A)
```

for every i; indeed, the question is local on $S_{0}$, and one is reduced to the case where one tensors by a free
module. **In this case, the vanishing of $H^{1}(Y_{0},\mathcal{G}_{0})$ implies that all obstructions to the successive
extensions of $g_{n}$ vanish.** Thus one obtains:

**Corollary.**

<!-- label: III.5.6 -->

Let $(S,X,Y,\mathcal{I},g_{n})$ be as above. Suppose moreover that X is smooth over S and Y is flat over S, and finally
that S is affine and the

$$ gr^{n}(\mathcal{O}_{S}) = \mathcal{I}^{n}/\mathcal{I}^{n+1} $$

are locally free. Then the obstruction to constructing $g_{n+1}$ lies in

$$ H^{1}(Y_{0},\mathcal{G}_{0}) \otimes_{A} gr^{n+1}_{I}(A), $$

where A is the ring of S and I the ideal of A defining $\mathcal{I}$, with

$$ \mathcal{G}_{0} = g_{0}*(\mathfrak{g}_{X_{0}/S_{0}}). $$

If $H^{1}(Y_{0},\mathcal{G}_{0}) = 0$, then $g_{n}$ can be extended to an `Ŝ`-morphism ĝ: $\hat{Y} \to \hat{X}$.

Of course, this result would remain valid exactly as stated if, instead of starting with ordinary S-preschemes X and Y,
one started with formal $\hat{\mathcal{I}}$-adic `Ŝ`-preschemes $\mathfrak{X}$ and $\mathfrak{Y}$. It allows one to
prove, for example, that certain formal schemes proper over a complete local ring are in fact algebraic. Indeed,
proceeding as in Lemma III.4.2, one finds:

<!-- original page 76 -->

**Corollary.**

<!-- label: III.5.7 -->

Under the conditions of III.5.6, if $g_{0}$ is an isomorphism, then so is ĝ.

The same result holds for closed immersions.

Thus one obtains:

**Proposition.**

<!-- label: III.5.8 -->

Let A be a complete local ring with maximal ideal $\mathfrak{m}$ and residue field k. Let $\mathfrak{X}$ and
$\mathfrak{Y}$ be two $\mathfrak{m}$-adic formal preschemes over A, flat over A, meaning that for every n, $X_{n}$ and
$Y_{n}$ are flat over $A_{n} = A/\mathfrak{m}^{n+1}$. Suppose $X_{0} = \mathfrak{X} \otimes_{A} k$ is smooth over k and
$H^{1}(X_{0},\mathfrak{g}_{X_{0}/k}) = 0$. Then every k-isomorphism from $Y_{0}$ onto $X_{0}$ extends to an
A-isomorphism from $\mathfrak{Y}$ onto $\mathfrak{X}$; this extension is unique if moreover
$H^{0}(X_{0},\mathfrak{g}_{X_{0}/k}) = 0$.

This gives in particular a result on the **uniqueness** of a smooth formal prescheme over A reducing to a given
prescheme $X_{0}$, provided $H^{1}(X_{0},\mathfrak{g}_{X_{0}/k}) = 0$. Moreover, if $\mathfrak{X}$ and $\mathfrak{Y}$
come from ordinary proper schemes over A, say X and Y, then by the existence theorem for sheaves in formal geometry, cf.
the Bourbaki seminar exposé no. 182,[^iii-5-8-1] there is a bijective correspondence between the A-isomorphisms $Y \to
X$ and the A-isomorphisms of the formal completions. Hence:

**Corollary.**

<!-- label: III.5.9 -->

The preceding statement III.5.8 remains valid when $\mathfrak{X}$ and $\mathfrak{Y}$ are replaced by ordinary A-schemes
X and Y, **proper** over A.

Finally, when $\mathfrak{X}$ is a formal scheme proper over A, and $\mathfrak{Y}$ is of the form `Ŷ` where Y is an
ordinary proper scheme over A, Proposition III.5.8 gives sufficient conditions for finding an isomorphism of
$\mathfrak{X}$ with `Ŷ`, and hence for the formal scheme $\mathfrak{X}$ to be in fact “algebraic”, i.e. isomorphic to an
$\hat{X}$, with X an ordinary proper scheme over A, which will then be canonically determined. This happens notably if
$X_{0} = \mathbb{P}^{r}_{k}$, or more generally if $X_{0}$ is a Severi-Brauer scheme, i.e. becomes isomorphic to the
standard projective space over the algebraic closure of k: every formal scheme proper and flat over A, with fiber
$\mathbb{P}^{r}_{k}$, is algebraizable, and more precisely is isomorphic to the $\mathfrak{m}$-adic formal completion of
$\mathbb{P}^{r}_{A}$. In particular, thanks to the “existence theorem”, every ordinary proper scheme over A with fiber
$\mathbb{P}^{r}_{k}$ is isomorphic to $\mathbb{P}^{r}_{A}$, where A is a complete local ring. Using descent theory, one
can prove that if A is not complete, X becomes isomorphic to $\mathbb{P}^{r}$ after making a finite étale extension $A
\to A'$ of the base; in this form, the result remains valid for a fiber that is a Severi-Brauer scheme.

## 6. Global Infinitesimal Extension of Smooth S-Schemes

<!-- label: III.6 -->

Under the conditions of Theorem III.4.1, we propose to seek whether there exists a prescheme X smooth over Y such that
$X \times_{Y} Y_{0}$ is $Y_{0}$-isomorphic to $X_{0}$, knowing that such a scheme “exists locally on $X_{0}$”. Taking up
again the step-by-step construction method, we are led to replace Y by the letter S, to suppose given a closed
sub-prescheme $S_{0}$ of S defined by a sheaf of ideals $\mathcal{I}$, which it is no longer necessary to suppose
locally nilpotent, to introduce the closed sub-preschemes $S_{n}$ of S defined by the $\mathcal{I}^{n+1}$, and to
suppose given a sub-prescheme $X_{n}$ smooth over $S_{n}$. We propose to find an $S_{n+1}$-prescheme $X_{n+1}$ “reducing
to $X_{n}$”, i.e. equipped with an isomorphism

```text
X_n → X_{n+1} ×_{S_{n+1}} S_n
```

that is **smooth** over $S_{n+1}$, or equivalently by II.2.1, **flat** over $S_{n+1}$. As we noted in III.4, such data
amount to giving a sheaf of algebras $\mathcal{B}$ over $f^{-1}(\mathcal{O}_{S_{n+1}})$, where f is the continuous map
underlying the structural morphism $X_{n} \to S_{n}$, equipped with an augmentation $\mathcal{B} \to
\mathcal{O}_{X_{n}}$ compatible with the augmentation $f^{-1}(\mathcal{O}_{S_{n+1}}) \to f^{-1}(\mathcal{O}_{S_{n}})$,
and satisfying two conditions (a) and (b) that we shall not rewrite, merely noting that they are **local in nature** on
the topological space underlying $X_{n}$. By III.4.1, a solution exists locally. It is moreover unique up to nonunique
isomorphism, at least locally. Let us begin by making this point precise.

<!-- original page 78 -->

**Proposition.**

<!-- label: III.6.1 -->

Let $X_{n+1}$ over $S_{n+1}$ reduce to $X_{n}$ over $S_{n}$. Then the sheaf, on the topological space underlying
$X_{n}$, or equivalently $X_{0}$, of $S_{n+1}$-automorphisms of $X_{n+1}$ inducing the identity on $X_{n}$ is
canonically isomorphic to

```text
𝒢 = 𝔤_{X₀/S₀} ⊗_{𝒪_{S₀}} gr^{n+1}_𝓘(𝒪_S)
```

as a sheaf of groups.

Indeed, by III.5.4 and III.4.2 this sheaf is a principal homogeneous sheaf under $\mathcal{G}$. Since it has a
distinguished section, the identity automorphism of $X_{n+1}$, it identifies as a sheaf of sets with $\mathcal{G}$. One
must verify that this identification is compatible with the group structures. This is easy, and is moreover a special
case of a more general result on the compatibility of the principal-bundle structures in III.5.1 and III.5.3 with
composition of morphisms, a result that we do not state here but that ought to appear in the hyperplodocus.

In particular, the sheaf on $X_{0}$ of germs of automorphisms of $X_{n+1}$, with the structures just made explicit, is
**commutative**. It follows that if $X'_{n+1}$ is another solution of the problem, isomorphic to $X_{n+1}$ over the open
U of $X_{0}$, then the isomorphism from $\operatorname{Aut}(X_{n+1})|U$ to $\operatorname{Aut}(X'_{n+1})|U$ deduced by
transport of structure from an isomorphism $X_{n+1}|U \to X'_{n+1}|U$ **does not depend** on the choice of the latter.
It is in fact nothing but the identity isomorphism of $\mathcal{G}$, when both automorphism sheaves are identified with
$\mathcal{G}$ by III.6.1.

From III.6.1 one deduces:

**Corollary.**

<!-- label: III.6.2 -->

Let $X_{n+1}$ and $X'_{n+1}$ be smooth over $S_{n+1}$ and “reduce to $X_{n}$”. Then the sheaf, on the space underlying
$X_{0}$, of $S_{n+1}$-isomorphisms from $X_{n+1}$ to $X'_{n+1}$ inducing the identity on $X_{n}$ is naturally a
principal homogeneous sheaf under $\mathcal{G}$.

This expresses indeed that $X_{n+1}$ and $X'_{n+1}$ are locally isomorphic, and that the sheaf of germs of automorphisms
of the first is $\mathcal{G}$.

Now note that by III.4.1 one can always find a covering $(U_{i})$ of $X_{n}$ by opens, which may be supposed affine, and
for each i a smooth scheme $X^{i}$ over $S_{n+1}$ reducing to $U_{i}$. Suppose for simplicity that $X_{n}$ is
**separated**, so the $U_{ij} = U_{i} \cap U_{j}$ are still **affine** opens of $X_{n}$. Since H¹ of such an open with
values in the quasi-coherent sheaf $\mathcal{G}$ is zero, Corollary III.6.2 implies that $X^{i}|U_{ij}$ is isomorphic to
$X^{j}|U_{ij}$; let

$$ f_{ji}: X^{i}|U_{ij} \to X^{j}|U_{ij} $$

be such an isomorphism. It is determined up to a section of $\mathcal{G}$ on $U_{ij}$. For every triple of indices put

```text
f_{ji}^{(k)} = f_{ji}|U_{ijk},    where U_{ijk} = U_i ∩ U_j ∩ U_k.
```

If one had

$$ f^{(i)}_{kj} f^{(k)}_{ji} = f^{(j)}_{ki}, $$

<!-- label: eq:III.6.1 -->

it would follow that the $X^{i}$ glue by the $f_{ji}$, and hence define a solution $X = X_{n+1}$ of the desired problem.
Such a solution exists more generally if one can modify the $f_{ji}$ into $f'_{ji}:$

```text
f′_{ji} = f_{ji} g_{ji},    g_{ji} ∈ Γ(U_{ij},𝒢),
```

<!-- label: eq:III.6.2 -->

so that the $f'_{ji}$ satisfy the preceding transitivity condition. This sufficient condition for the existence of a
solution is also necessary, as one sees by recalling that such a solution X must, on each $U_{i}$, be isomorphic to
$X^{i}$; this allows one to choose isomorphisms

$$ f_{i}: X|U_{i} \to X^{i} $$

and to define

```text
f′_{ji} = (f_j|U_{ij})(f_i|U_{ij})^{-1}: X^i|U_{ij} → X^j|U_{ij},
```

satisfying the gluing condition.

Now put

```text
f_{ijk} = (f_{ki}^{(j)})^{-1} f_{kj}^{(i)} f_{ji}^{(k)}.
```

<!-- label: eq:III.6.3 -->

This is an automorphism of $X^{i}|U_{ijk}$, which we identify with a section of $\mathcal{G}$ by III.6.1. One checks, by
a small formal calculation left to the reader, that it is a **2-cocycle** f of the open covering $\mathcal{U} =
(U_{i})$, with coefficients in $\mathcal{G}$. The same calculation shows that, under III.6.2, the gluing condition
III.6.1 **for the** $f'_{ij}$ is equivalent to the formula

```text
f = dg,
```

<!-- label: eq:III.6.4 -->

where $g = (g_{ij})$ is regarded as a 1-cochain of $\mathcal{U}$ with coefficients in $\mathcal{G}$. Thus **the
necessary and sufficient condition for the existence of a solution of the problem is that the cohomology class in
$H^{2}(\mathcal{U},\mathcal{G})$ defined by the cocycle III.6.3 be zero**. Moreover, since $\mathcal{U} = (U_{i})$ is an
affine covering of $X_{0}$, which is a **scheme**, $H^{2}(\mathcal{U},\mathcal{G})$ identifies with
$H^{2}(X_{0},\mathcal{G})$. It is immediate that the cohomology class thus obtained in $H^{2}(X_{0},\mathcal{G})$ does
not depend on the affine covering considered. We shall call it the **obstruction class to extending $X_{n}$ to a scheme
$X_{n+1}$ smooth over $S_{n+1}$**.

Suppose this obstruction is zero. Then the argument sketched above shows that every solution $X = X_{n+1}$ is isomorphic
to a solution obtained by gluing from isomorphisms $f'_{ji}$, which may be supposed of the form III.6.2, the gluing
condition being just III.6.3. The set of admissible g is therefore a principal homogeneous space under the group
$Z^{1}(\mathcal{U},\mathcal{G})$ of 1-cocycles of $\mathcal{U}$ with coefficients in $\mathcal{G}$. Moreover, one sees
at once that **two cochains g and $g'$**, with dg = $dg' = f$, **define isomorphic solutions if and only if the cocycle
$g - g'$ is of the form dh**, with $h = (h_{i}) \in C^{0}(\mathcal{U},\mathcal{G})$. Thus one obtains:

**Theorem.**

<!-- label: III.6.3 -->

Let $(S,\mathcal{I},X_{n})$ be as above, with $X_{n}$ assumed separated.[^iii-6-3-1] Then one can define canonically an
obstruction class in $H^{2}(X_{0},\mathcal{G})$, where $\mathcal{G}$ is defined in III.6.1, whose vanishing is necessary
and sufficient for the existence of a scheme $X_{n+1}$, smooth over $S_{n+1}$, reducing to $X_{n}$. If this obstruction
is zero, then the set of isomorphism classes, with isomorphisms inducing the identity on $X_{n}$, of
$S_{n+1}$-preschemes $X_{n+1}$ reducing to $X_{n}$ is naturally a principal homogeneous space under
$H^{1}(X_{0},\mathcal{G})$.

**Remarks.**

<!-- label: III.6.4 -->

Starting from III.6.1, the arguments made here are purely formal, and are advantageously transcribed in the setting of
local categories, or even of general fibered categories. The obstruction class to the existence of a “global” object of
a category, where one can find an object “locally”, any two objects are always “locally isomorphic”, and the
automorphism group of any object is commutative, obtained in this general context, contains as a special case the
“second boundary homomorphism” in an exact sequence of sheaves of not necessarily commutative groups, studied for
example by Grothendieck in Kansas or Tôhoku. The silly cocycle calculation made here should therefore be regarded as a
makeshift, due to the absence of a satisfactory reference text.

### 6.5

<!-- label: III.6.5 -->

Note that in III.6.3 there is in general no distinguished element in the principal homogeneous space under
$H^{1}(X_{0},\mathcal{G})$ under consideration. This is reflected in particular by the fact that, after localizing on S,
one obtains a principal homogeneous sheaf on $S_{0}$ with structural group $R^{1}f_{*}(\mathcal{G})$, which is not
necessarily trivial, i.e. which defines a cohomology class in $H^{1}(S_{0},R^{1}f_{*}(\mathcal{G}))$ that is not
necessarily zero. This is when one supposes that the class d ∈ $H^{2}(X_{0},\mathcal{G})$ is not zero, but is zero
“locally over S”, i.e. defines a zero section of $R^{2}f_{*}(\mathcal{G})$, equivalently a zero element in
$H^{0}(S_{0},R^{2}f_{*}(\mathcal{G}))$.

### 6.6

<!-- label: III.6.6 -->

For the moment we know almost nothing about the general algebraic mechanism of the cohomology classes introduced in this
number and their relations with the preceding number, and we have nothing precise to say about them in the simplest
particular cases, such as the case of abelian schemes over artinian rings.[^iii-6-6-1] One hopes that people will be
found to work the question out thoroughly; it seems particularly interesting. It is intimately linked, in particular, to
the “module theory” of algebraic structures.

**Corollary.**

<!-- label: III.6.7 -->

Suppose $H^{2}(X_{0},\mathcal{G}) = 0$. Then an $X_{n+1}$ exists, and it is unique up to isomorphism if moreover
$H^{1}(X_{0},\mathcal{G}) = 0$.

In particular, proceeding step by step, and observing that an affine scheme is acyclic for a quasi-coherent sheaf, one
concludes:

**Corollary.**

<!-- label: III.6.8 -->

<!-- original page 82 -->

Under the conditions of Theorem III.4.1, if $X_{0}$ is affine, then there exists an X smooth over Y reducing to $X_{0}$,
and this X is unique up to nonunique isomorphism.

Note that the direct proof of Theorem III.4.1 could not have given this result.

**Corollary.**

<!-- label: III.6.9 -->

Under the conditions of III.6.3, suppose S is affine with ring A, $\mathcal{I}$ is defined by an ideal I of A, and
finally the

$$ gr^{n}_{\mathcal{I}}(\mathcal{O}_{S}) = \mathcal{I}^{n}/\mathcal{I}^{n+1} $$

are locally free. Then $H^{i}(X_{0},\mathcal{G})$ identifies with

$$ H^{i}(X_{0},\mathcal{G}_{0}) \otimes_{A} gr^{n+1}_{I}(A), $$

where

$$ \mathcal{G}_{0} = \mathfrak{g}_{X_{0}/S_{0}}. $$

Thus the obstruction class to extending $X_{n}$ lies in $H^{2}(X_{0},\mathcal{G}_{0}) \otimes_{A} gr^{n+1}_{I}(A)$, and,
if it is zero, the set of isomorphism classes of solutions is a principal homogeneous space under
$H^{1}(X_{0},\mathcal{G}_{0}) \otimes_{A} gr^{n+1}_{I}(A)$.

In particular:

**Corollary.**

<!-- label: III.6.10 -->

Under the conditions of III.6.9, suppose

$$ H^{2}(X_{0},\mathfrak{g}_{X_{0}/S_{0}}) = 0. $$

Then there exists an $\hat{\mathcal{I}}$-adic formal scheme $\mathfrak{X}$ over the $\mathcal{I}$-adic formal completion
`Ŝ` of S, “smooth over S”, i.e. such that the $\mathfrak{X}_{p}$ are smooth over the $S_{p}$, and reducing to $X_{n}$,
i.e. equipped with an isomorphism

```text
X_n → 𝔛 ×_S S_n.
```

If moreover $H^{1}(X_{0},\mathfrak{g}_{X_{0}/S_{0}}) = 0$, then such a $\mathfrak{X}$ is unique up to isomorphism.

Indeed, one constructs $X_{n+1}$, $X_{n+2}$, and so on step by step, whence $\mathfrak{X}$ by passing to the inductive
limit of the $X_{i}$. The uniqueness assertion already appears in the preceding number.

## 7. Application to the Construction of Formal Schemes and Ordinary Smooth Schemes over a Complete Local Ring A

<!-- label: III.7 -->

The results of the preceding number sometimes make it possible to prove the existence of an $\mathfrak{m}$-adic formal
scheme over such a ring, reducing to a given smooth scheme $X_{0}$ over k. Distinguish two cases.

1. **A is “of equal characteristics”.** This is the case in particular if k has characteristic 0. Then one knows that
   there exists a **coefficient subfield of** A, i.e. a subfield $k'$ such that $A \to k$ induces an isomorphism $k' \to
   k$. **Then there even exists an ordinary smooth scheme over A reducing to $X_{0}$**, namely $X = X_{0} \otimes_{k}
   A$, with A regarded as an algebra over k by the homomorphism $k \to k' \to A$ defined by $k'$. It should be noted,
   however, that this construction is not “natural”. It is easy to convince oneself, already in the case where A =
   k[t]/(t²), the algebra of dual numbers, that another lifting homomorphism $k \to A$, in this case defined by an
   absolute derivation of k into itself, defines an $X'$ over A that in general **is not isomorphic to X**, if
   $H^{1}(X_{0},\mathfrak{g}_{X_{0}/k}) \neq 0$. It would moreover be interesting to study, for k of characteristic 0,
   or imperfect of characteristic p > 0, which X smooth over A are obtained in this way, and under what condition two
   homomorphisms $k \to A$ define isomorphic A-schemes. Nevertheless, the existence of $k'$ is enough to imply that the
   first obstruction to lifting $X_{0}$, which lies in $H^{2}(X_{0},\mathfrak{g}_{X_{0}/k}) \otimes_{k}
   \mathfrak{m}/\mathfrak{m}^{2}$, is necessarily zero. Of course, once $X_{0}$ has then been lifted to $X_{1}$ smooth
   over $A/\mathfrak{m}^{2}$, the new obstruction to constructing $X_{2}$ will in general not be zero: it will depend on
   a variable element in a certain principal homogeneous space under $H^{1}(X_{0},\mathcal{G}_{0}) \otimes
   \mathfrak{m}/\mathfrak{m}^{2}$ and lies in $H^{2}(X_{0},\mathcal{G}_{0}) \otimes \mathfrak{m}^{2}/\mathfrak{m}^{3}$.
   The situation ought to be studied in detail.[^iii-7-a-1]

2) **A is of unequal characteristics.** In this case we know nothing, except if by luck
   $H^{2}(X_{0},\mathfrak{g}_{X_{0}/k}) = 0$, in which case one can construct an $\mathfrak{m}$-adic formal smooth
   scheme over A reducing to k. Even if $A = \mathbb{Z}/p^{2}\mathbb{Z}$ and $X_{0}$ is an “abelian” scheme of dimension
   2, one does not know whether it can be lifted to an $X = X_{1}$ smooth over A;[^iii-7-b-1] on the other hand, we have
   no example of an $X_{0}$ that has been proved not to come from an ordinary scheme X smooth over A. I have the
   impression that such examples should exist, with $X_{0}$ a projective surface.[^iii-7-b-2] Let us simply point out
   that by Cohen's theorem, there exists a Cohen p-ring B with residue field k and a homomorphism $B \to A$ inducing the
   identity isomorphism on residue fields. Consequently, the “strongest” lifting result would be obtained by taking A to
   be a Cohen p-ring: if there is an ordinary or formal solution over such a ring, there is one over every complete
   local ring with residue field k. In particular, since for a Cohen p-ring $\mathfrak{m}/\mathfrak{m}^{2}$ identifies
   canonically with k, one sees that **for every smooth scheme $X_{0}$ over a field k of characteristic p > 0, there
   exists a cohomology class in $H^{2}(X_{0},\mathfrak{g}_{X_{0}/k})$**, the first obstruction to lifting $X_{0}$ to a
   smooth scheme over a Cohen p-ring. We do not know whether it can be nonzero.[^iii-7-b-3]

Even if one succeeds step by step in constructing the $X_{n}$ reducing to $X_{0}$, this generally gives only a
**formal** scheme $\mathfrak{X}$ smooth over A, reducing to $X_{0}$. When $X_{0}$ is proper over A, there remains the
question whether $\mathfrak{X}$ is in fact algebraizable, in order to obtain an **ordinary** proper scheme over A,
smooth over A, reducing to $X_{0}$. The only known criterion, noted in the Bourbaki seminar and appearing in the
Éléments, Chapter III, 4.7.1, is the following: if $\mathfrak{X}$ is proper over A, and if $\mathcal{L}$ is an
invertible sheaf on $\mathfrak{X}$ such that the induced sheaf $\mathcal{L}_{0}$ on $X_{0}$ is ample, i.e. some tensor
power $\mathcal{L}^{\otimes n}_{0}$, n > 0, comes from a projective immersion of $X_{0}$, then there exists a scheme X
projective over A, and an ample invertible sheaf on X, such that $(\mathfrak{X},\mathcal{L})$ is obtained from it by
$\mathfrak{m}$-adic completion. This leads us, given a locally free sheaf $\mathcal{E}_{0}$ on $X_{0}$, which we shall
choose invertible and ample for our purpose, to extend it to a locally free sheaf $\mathcal{E}$ on $\mathfrak{X}$. For
this, one is reduced to constructing step by step locally free sheaves $\mathcal{E}_{n}$ on the $X_{n}$. The discussion
is entirely analogous to that of III.6, cf. Remark III.6.4; the essential role is played by the **sheaf of
automorphisms** of an $\mathcal{E}_{n+1}$ inducing the identity on $\mathcal{E}_{n}$. One shows at once that this sheaf
identifies with

```text
𝒢 = Hom_{𝒪_{X₀}}(𝓔₀, 𝓔₀ ⊗ gr^{n+1}_𝓘(𝒪_X))
  = Hom_{𝒪_{X₀}}(𝓔₀,𝓔₀) ⊗ gr^{n+1}_𝓘(𝒪_X),
```

which is again a sheaf of commutative groups. One obtains:

<!-- original page 85 -->

**Proposition.**

<!-- label: III.7.1 -->

Let S be a prescheme equipped with a quasi-coherent sheaf of ideals $\mathcal{I}$, let X be a prescheme over S, let
$S_{n}$ be the sub-prescheme of S defined by $\mathcal{I}^{n+1}$, and let $X_{n} = X \times_{S} S_{n}$ for every integer
n. Let $\mathcal{E}_{n}$ be a locally free sheaf on $X_{n}$, and seek to extend it to a locally free sheaf
$\mathcal{E}_{n+1}$ on $X_{n+1}$. Then $\mathcal{E}_{n}$ defines a canonical obstruction class in
$H^{2}(X_{0},\mathcal{G})$, where $\mathcal{G}$ is the quasi-coherent sheaf given by the formula above. The vanishing of
this class is necessary and sufficient for the existence of an $\mathcal{E}_{n+1}$ extending $\mathcal{E}_{n}$. If this
class is zero, then the set of isomorphism classes, with isomorphisms inducing the identity on $\mathcal{E}_{n}$, of
solutions $\mathcal{E}_{n+1}$ is a principal homogeneous space under $H^{1}(X_{0},\mathcal{G})$.

This proposition gives rise to the usual corollaries. Let us only point out that if X is **flat** over S, then one may
write

```text
𝒢 = Hom_{𝒪_{X₀}}(𝓔₀,𝓔₀) ⊗_{𝒪_{S₀}} gr^{n+1}_𝓘(𝒪_S),
```

whence, if S is affine with ring A and the $\mathcal{I}^{n}/\mathcal{I}^{n+1}$ are locally free, the sufficient
condition

```text
H²(X₀,𝒢₀) = 0,    with    𝒢₀ = Hom_{𝒪_{X₀}}(𝓔₀,𝓔₀),
```

for the existence of an $\mathcal{E}_{n+1}$, and hence, step by step, for the existence of successive extensions
$\mathcal{E}_{m}$, $m = n$, $n + 1$, etc.

Returning to the initial situation, we therefore find:

**Proposition.**

<!-- label: III.7.2 -->

Let A be a complete local ring, and let $\mathfrak{X}$ be a formal scheme proper and flat over A, such that $X_{0}$ is
projective and $H^{2}(X_{0},\mathcal{O}_{X_{0}}) = 0$. Then there exists a scheme X projective over A whose
$\mathfrak{m}$-adic formal completion is isomorphic to $\mathfrak{X}$.

Combining this with III.6.10, one finds:

**Theorem.**

<!-- label: III.7.3 -->

Let A be a complete local ring with residue field k, and let $X_{0}$ be a projective smooth scheme over k such that

$$ H^{2}(X_{0},\mathfrak{g}_{X_{0}/k}) = H^{2}(X_{0},\mathcal{O}_{X_{0}}) = 0. $$

Then there exists a smooth and projective scheme X over A reducing to $X_{0}$.

More generally, if one is given an $X_{n}$ smooth over $A_{n} = A/\mathfrak{m}^{n+1}$ reducing to $X_{0}$, then there
exists an X smooth and proper over A and an isomorphism $X \otimes_{A} A_{n} = X_{n}$.

**Corollary.**

<!-- label: III.7.4 -->

Every smooth proper curve over k is obtained by reduction from a smooth proper curve over A.

This result will be the essential tool, together with the existence theorem for sheaves in formal geometry, for studying
the fundamental group of $X_{0}$ by transcendental means.

<!-- original page 86 -->

<!-- end of Exposé III source block: next chapter begins at smf_doc-math_3_01.tex line 6269 -->

[^iii-1-1-1]: For a more general and more conceptual definition, motivated by III.2.1 below, cf.
    [EGA 0_IV 19.3.1](https://jcreinhold.github.io/ega/iv/06-ch0-19-formally-smooth-algebras.html#193-formally-smooth-algebras).

[^iii-1-2-1]: Or better, “essentially unramified”, respectively “essentially étale”; compare
    [EGA IV 18.6.1](https://jcreinhold.github.io/ega/iv/31-ch4-18-complements-etale-morphisms.html#186-henselization).

[^iii-2-1-1]: Cf.
    [EGA 0_IV 19.3](https://jcreinhold.github.io/ega/iv/06-ch0-19-formally-smooth-algebras.html#193-formally-smooth-algebras),
    19.8.

[^iii-5-0-1]: It seems preferable to adopt the shorter and more expressive term “torsor under $\mathcal{G}$”, introduced
    in J. Giraud's thesis.

[^iii-5-8-1]: Cf.
    [EGA III 5.4.1](https://jcreinhold.github.io/ega/iii/12-ch3-05-existence-coherent-algebraic-sheaves.html#54-application-comparison-of-morphisms-of-usual-schemes-and-of-morphisms-of-formal-schemes-algebraizable-formal-schemes)
    for the proof.

[^iii-6-3-1]: This condition is in fact unnecessary, and one can avoid the cocycle calculations above. Cf. J. Giraud,
    _Cohomologie Non Abélienne_, forthcoming from Springer Verlag, 1971. Compare Remarks III.6.4.

[^iii-6-6-1]: It is now known that this obstruction is always zero in this case \[added in 2003 by MR: cf. F. Oort,
    “Finite group schemes, local moduli for abelian varieties and lifting problems”, *Algebraic Geometry Oslo
    1970*, Wolters-Noordhoff, 1972, pp. 223-254\].

[^iii-7-a-1]: It is probably described by the Kodaira-Spencer bracket operation; cf. Séminaire Cartan, 1960/61, Exposé
    4\.

[^iii-7-b-1]: This is now proved; cf. note III.6.6, page 81 in the original numbering.

[^iii-7-b-2]: Such an example was later constructed by J.-P. Serre, _Proc. Nat. Acad. Sci. USA_ **47** (1961), no. 1,
    pp. 108-109, at least in certain dimensions. D. Mumford gave an unpublished example with an algebraic **surface**.

[^iii-7-b-3]: It can be nonzero, as indicated in note iii-7-b-2.
