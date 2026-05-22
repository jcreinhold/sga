# Exposé XVII. Unipotent algebraic groups. Extensions between unipotent groups and groups of multiplicative type

<!-- label: III.XVII -->

*by M. Raynaud*[^XVII-0-0]

## 0. Some notations

<!-- label: III.XVII.0 -->

<!-- original page 531 -->

In the present chapter, we shall mostly consider algebraic groups defined over a field $k$. The number $p \geqslant 0$
will always denote the characteristic of $k$, $F_{p}$ the prime field with $p$ elements if $p > 0$, $\bar{k}$ an
algebraically closed extension of $k$, $q$ a prime number distinct from $p$.

For every $S$-prescheme, $(G_{a})_{S}$ (resp. $(G_{m})_{S}$) denotes the additive group (resp. the multiplicative group)
over $S$ (cf. Exp. I, 4.3). For every integer $n > 0$, $(\mu_{n})_{S}$ (resp. $(\mathbb{Z}/n\mathbb{Z})_{S}$) denotes
the group of $n$-th roots of unity (Exp. I, 4.4.4) (resp. the constant group over $S$ associated with the abstract group
$\mathbb{Z}/n\mathbb{Z}$ (Exp. I, 4.1)). The group $(\mathbb{Z}/n\mathbb{Z})_{S}$ is finite and étale over $S$; the
group $(\mu_{n})_{S}$ is flat and finite over $S$, and is étale over $S$ if and only if $n$ is invertible on $S$ (Exp.
VIII, 2.1).

If $S$ is a prescheme of characteristic $p > 0$, for every integer $n > 0$ and every $S$-prescheme in groups $G$, we
denote by $F_{n}(G)$ the radicial sub-$S$-prescheme in groups of $G$ equal to the kernel of the $n$-th iterate of the
Frobenius morphism relative to $G$ (Exp. VII_A). In particular, if $G = (G_{a})_{S}$ we set
$F_{n}(G) = (\alpha_{p^{n}})_{S}$, which is a radicial $S$-group, flat and finite over $S$, representing the following
functor: for every $S$-prescheme $S'$, $(\alpha_{p^{n}})_{S}(S')$ is the set of $x' \in \Gamma(S', O_{S'})$ such that
$x'^{p^{n}} = 0$.

The group $(\mu_{p^{n}})_{S}$, already defined, is canonically isomorphic to $F_{n}(G_{m})_{S}$.

<!-- original page 532 -->

When there is no ambiguity about the base scheme $S$, we shall simply write $G_{a}$, $G_{m}$, $\alpha_{p^{n}}$, etc.
instead of $(G_{a})_{S}$, $(G_{m})_{S}$, $(\alpha_{p^{n}})_{S}$, etc.

If $G$ is an $S$-prescheme in commutative groups, for every integer $n > 0$, ${}_{n} G$ is the sub-prescheme in groups
of $G$ equal to the kernel of raising to the $n$-th power in $G$.

For the convenience of the reader, we have gathered in an appendix some properties of algebraic groups proved in Exp. VI
and VII, as well as elementary properties of Hochschild cohomology, which will be useful in this chapter.

## 1. Definition of unipotent algebraic groups

<!-- label: III.XVII.1 -->

<!-- original page 533 -->

**Definition 1.1.** *An algebraic group $G$ defined over an algebraically closed field $k$ is said to be* unipotent *if
$G$ admits a composition series whose successive quotients are isomorphic to algebraic subgroups of $(G_{a})_{k}$.*

<!-- label: III.XVII.1.1 -->

**Proposition 1.2.** *Let $k$ be an algebraically closed field, $K$ an algebraically closed extension of $k$, and $G$ an
algebraic group defined over $k$. Then, in order that $G$ be unipotent, it is necessary and sufficient that `G_K` be
unipotent.*

<!-- label: III.XVII.1.2 -->

The necessity of the condition is clear, since a composition series gives a composition series by extension of the base.

The proof of sufficiency is standard: $K$ is the direct limit of its finitely generated $k$-subalgebras. By Exp. VI_B §
10, one can find a finitely generated $k$-subalgebra $A$ of $K$, a composition series $G_{i}$ of `G_S`
($S = \operatorname{Spec} A$), and immersions $u_{i} : H_{i} = G_{i} / G_{i+1} \to (G_{a})_{S}$. To prove that $G$ is
unipotent, it then suffices to make a $k$-base extension $A \to k$, which is possible because
$\operatorname{Hom}_{k-alg}(A, k)$ is non-empty, since $A$ is a non-zero $k$-algebra of finite type over the
algebraically closed field $k$.

**Definition 1.3.** *Let $G$ be an algebraic group defined over a field $k$. We shall say that $G$ is* unipotent *if
there exists an algebraically closed extension $\bar{k}$ of $k$ such that $G_{\bar{k}}$ is unipotent (Definition 1.1).*

<!-- label: III.XVII.1.3 -->

<!-- original page 534 -->

By 1.2, the property is independent of the chosen algebraically closed extension $\bar{k}$.

**Definition 1.4.** *Let $G$ be an algebraic group defined over a field $k$ and $H$ an algebraic group defined over an
extension $k'$ of $k$. We shall say that $H$ is a* form *of $G$ over $k'$ if the algebraic groups $G_{\bar{k}'}$ and
$H_{\bar{k}'}$ become isomorphic over $\bar{k}'$ (as above, one sees that the property does not depend on the choice of
the algebraically closed extension $\bar{k}'$ of $k'$). We shall also say that $H$ is a* twisted *form of $G$.*

<!-- label: III.XVII.1.4 -->

We are now in a position to describe the algebraic subgroups of $G_{a}$.

**Proposition 1.5.** *Let $k$ be a field of characteristic $p \geqslant 0$. Then an algebraic subgroup $H$ of
$(G_{a})_{k}$ is of one of the following types:*

<!-- label: III.XVII.1.5 -->

*(i) $H = 0$.*

*(ii) $H = G_{a}$.*

*(iii) (If $p > 0$) $H$ is an extension of a twisted constant group $(\mathbb{Z}/p\mathbb{Z})^{r}$ by a radicial group
$\alpha_{p^{n}}$ ($r$ and $n$ integers $\geqslant 0$, $r + n > 0$). If moreover $k$ is perfect, this extension is
necessarily trivial.*

*Proof.* If $H$ is of dimension 1, it is clear that $H = G_{a}$. Otherwise $H$ is of dimension 0 and consequently is an
extension[^N.D.E-XVII-1] of an étale group `H''` by its identity component $H'$, which is a radicial group. To describe
$H''_{\bar{k}}$, it suffices to know the abstract group $H''(\bar{k})$, isomorphic to $H(\bar{k})$.

<!-- original page 535 -->

Now this latter is a finite subgroup of $G_{a}(\bar{k})$, hence is zero if $p = 0$, and of the form
$(\mathbb{Z}/p\mathbb{Z})^{r}$ otherwise, since it is annihilated by $p$. The group $H'$ is closed in $G_{a}$ and is
defined by a single equation (the ring `k[T]` of $G_{a}$ is principal), which over $\bar{k}$ admits `0` as its only
root, so this equation is of the form $T^{n} = 0$. Compatibility with the group law entails that $(T + T')^{n}$ belongs
to the ideal generated by $T^{n}$ and $T'^{n}$ in the ring `k[T, T']`, hence: if $p = 0$, one has $n = 1$ and $H'$ is
the trivial group; if $p > 0$, one has $n = p^{m}$ and $H' = \alpha_{p^{m}}$.

The last assertion of 1.5 follows, more generally, from the lemma:

**Lemma 1.6.** *If $k$ is a perfect field, every extension $H$ of an étale algebraic group `H''` by a radicial group
$H'$ is trivial. Moreover, there is a unique lift of `H''` in $H$, namely $H_{red}$.*

<!-- label: III.XVII.1.6 -->

Indeed, since $k$ is perfect, the reduced $k$-scheme $H_{red}$ is an algebraic subgroup of $H$ (Exp. VI_A, 0.2) which is
geometrically reduced, hence smooth over $k$ (Exp. VI_A, 1.3.1), hence étale, since $H$ is of dimension 0. To see that
the canonical projection $H_{red} \to H''$ is an isomorphism, it suffices to verify it after base extension
$k \to \bar{k}$, in which case it suffices to show that one has an isomorphism on the $\bar{k}$-valued points, which is
clear. The last assertion follows from the fact that every lift of `H''` in $H$, being étale over $k$, is reduced, hence
is necessarily contained in $H_{red}$.

<!-- original page 536 -->

Note that $\alpha_{p^{n}}$ is a multiple extension of groups isomorphic to $\alpha_{p}$. From 1.5 we then deduce the
corollary:

**Corollary 1.7.** *In order that an algebraic group $G$ defined over an algebraically closed field $k$ be unipotent, it
is necessary and sufficient that it possess a composition series whose successive quotients are isomorphic to $G_{a}$ if
$p = 0$, and to one of the groups $G_{a}$, $\mathbb{Z}/p\mathbb{Z}$, $\alpha_{p}$ if $p > 0$. (We shall call these the*
elementary unipotent groups\*.)\*

<!-- label: III.XVII.1.7 -->

## 2. First properties of unipotent groups

<!-- label: III.XVII.2 -->

<!-- original page 537 -->

**Proposition 2.1.** *A unipotent algebraic group defined over a field $k$ is affine over $k$.*

<!-- label: III.XVII.2.1 -->

By fpqc descent of affine morphisms, it suffices to prove 2.1 when $k$ is algebraically closed. In this case, $G$ is by
definition a multiple extension of affine algebraic groups, hence is affine, by Exp. VI_B, 9.2 (viii) applied to affine
morphisms.[^N.D.E-XVII-2]

**Proposition 2.2.**

<!-- label: III.XVII.2.2 -->

*i) The property of being unipotent for an algebraic group is invariant under base field extension.*

*ii) Every algebraic subgroup of a unipotent group is unipotent.*

*iii) Every algebraic quotient group of a unipotent group is unipotent.*

*iv) Every extension of a unipotent algebraic group by a unipotent algebraic group is likewise unipotent.*

*Proof.* i) follows immediately from 1.3 and 1.2. To establish the other properties, we may suppose the field $k$
algebraically closed. Then iv) is evident from Definition 1.3.

<!-- original page 538 -->

Let then $G$ be a unipotent algebraic group, $G'$ an algebraic subgroup of $G$, `G''` an algebraic quotient group of
$G$, and $G_{i}$ ($i = 1, \cdots, n$) a composition series of $G$ such that $H_{i} = G_{i} / G_{i+1}$ is an elementary
unipotent group (1.7).

To prove ii), consider the composition series of $G'$ induced by that of $G$: $G'_{i} = G_{i} \cap G'$. The group
$G'_{i} / G'_{i+1}$ is identified with an algebraic subgroup of $H_{i}$, hence is isomorphic to a subgroup of $G_{a}$,
and consequently $G'$ is unipotent.

To prove iii), consider the composition series of `G''` image of that of $G$: $G''_{i} =$ image of $G_{i}$ in `G''`. The
group $G''_{i} / G''_{i+1}$ is then a quotient of $H_{i}$, and it suffices to prove the lemma:

**Lemma 2.3.** *If $H$ is an elementary unipotent group (1.7) defined over a field $k$, every algebraic quotient group
`H''` of $H$ is zero or is isomorphic to $H$ over $k$.*

<!-- label: III.XVII.2.3 -->

*Proof.* If $H = G_{a}$ in characteristic 0, or if $H = \alpha_{p}$ or $\mathbb{Z}/p\mathbb{Z}$ ($p > 0$), it suffices
to note that it follows from 1.5 that $H$ has no algebraic subgroups other than 0 and $H$ (observe that a non-zero
algebraic subgroup of $\alpha_{p}$ is defined by a $k$-algebra of $k$-rank at least $p$ (1.5 iii)), hence is equal to
$\alpha_{p}$).

Now let $H = G_{a}$ ($p > 0$), so that one has an exact sequence:

$$
0 \longrightarrow N \longrightarrow G_{a} \longrightarrow H'' \longrightarrow 0.
$$

If $N = G_{a}$, then $H'' = 0$. Otherwise, proceeding by induction on the length of a composition series of $N$, one may
assume that $N = \alpha_{p}$, or that $N$ is a form of $(\mathbb{Z}/p\mathbb{Z})^{r}$ (1.5).

<!-- original page 539 -->

a) If $N \simeq \alpha_{p}$, the proof of 1.5 iii) shows that $N$ is necessarily the kernel of the Frobenius morphism
$F$ in $G_{a}$, and one concludes using the exact sequence:

```text
0 → α_p → G_a ─F→ G_a → 0.
```

b) If $N \simeq \mathbb{Z}/p\mathbb{Z}$, it is immediate that there exists $a \in k*$ such that $N$ is the closed
subscheme of $G_{a} = \operatorname{Spec} k[X]$ defined by the equation $X^{p} - aX = 0$. One then concludes using the
exact sequence:

```text
0 → N → G_a ─P→ G_a → 0,
```

where $P$ is the Artin–Schreier morphism $x \mapsto x^{p} - ax$.

c) If $N$ is a form of $(\mathbb{Z}/p\mathbb{Z})^{r}$, there exists a finite Galois extension $k'$ of $k$ that
trivializes $N$. By b) and an evident induction on $r$, $G_{a} / N$ is a form of $G_{a}$ trivialized by $k'$. It then
suffices to apply the following lemma:

**Lemma 2.3 bis.** *Let $k$ be a field, $G$ a $k$-algebraic group which is a form of $G_{a}$, trivialized by a finite
separable extension $k'$ of $k$. Then $G$ is isomorphic to $G_{a}$.*

<!-- label: III.XVII.2.3bis -->

Indeed, the group of $k'$-automorphisms of the algebraic group $(G_{a})_{k'}$ is the group of non-zero homotheties
$(k')^{\times}$ (*Bible*, Exp. 9, Lemma 1), and the Galois cohomology group $H^{1}(k'/k, G_{m})$ is zero (one may
suppose that $k'$ is a Galois extension of $k$), by Hilbert's Theorem 90. Lemma 2.3 bis then follows from the
classification of $k$-forms of an algebraic group (cf. J.-P. Serre, *Cohomologie galoisienne*, Chap. III, 1.3).

This completes the proof of 2.2.

<!-- original page 540 -->

**Proposition 2.4.** *Let $k$ be a field, $M$ a $k$-group of multiplicative type (Exp. VIII) and of finite type, $U$ a
unipotent $k$-algebraic group. Then:*

<!-- label: III.XVII.2.4 -->

*i) $\operatorname{Hom}_{k-gr}(M, U) = e$ (a fortiori $\operatorname{Hom}_{k-gr}(M, U) = e$).*

*ii) $\operatorname{Hom}_{k-gr}(U, M) = e$.*

To prove i) we must establish that for every prescheme $S$ over $k$, $\operatorname{Hom}_{S-gr}(M_{S}, U_{S}) = e$. But
this follows from the following lemma:

**Lemma 2.5.** *Let $S$ be a prescheme, $M$ an $S$-group of multiplicative type and of finite type over $S$, $U$ an
$S$-prescheme in groups of finite presentation over $S$ with unipotent fibers. Then
$\operatorname{Hom}_{S-gr}(M, U) = e$.*

<!-- label: III.XVII.2.5 -->

Indeed, under the hypotheses made, in order that an $S$-morphism of groups $u : M \to U$ be the unit homomorphism, it
suffices that the restriction of $u$ to the fibers of $M$ over the points of $S$ be the zero morphism (Exp. IX, 5.2). We
are thus reduced to the case where $S$ is the spectrum of a field, which we may further assume to be algebraically
closed. In view of Definition 1.1, we may restrict to $U = G_{a}$, in which case the property has already been proved
(Exp. XII, 4.4.1).

Let us now prove 2.4 ii). Let $u : U \to M$ be a $k$-morphism of groups. The image $u(U)$ is representable by an
algebraic subgroup `U''` of $M$ (Exp. VI_B, 5.4).[^N.D.E-XVII-3] The group `U''` is unipotent as a quotient of a
unipotent group (2.2 iii)) and is of multiplicative type as a subgroup of a group of multiplicative type

<!-- original page 541 -->

(cf. *Bible*, Exp. 4, Th. 2 cor. 1, or Exp. IX, 6.8), so `U''` is the trivial group by 2.4 i).

**Remark 2.6.** *Keeping the notations of 2.4, it is no longer true in general that the functor
$\operatorname{Hom}_{k-gr}(U, M)$ is equal to $e$. Thus, take a prescheme $S$ such that $\Gamma(S, O_{S})$ contains a
non-zero element $\epsilon$ such that $\epsilon^{2} = 0$ (for example the spectrum of the algebra of dual numbers of a
ring $A$). For every $S'$ over $S$, the map $u \mapsto 1 + \epsilon_{S'} u$ defines a homomorphism, functorial in $S'$,
from the additive group $\Gamma(S', O_{S'})$ to the multiplicative group $\Gamma(S', O^{\times}_{S'})$, hence defines an
$S$-morphism of groups $(G_{a})_{S} \to (G_{m})_{S}$, and since $\epsilon \neq 0$, this morphism is not zero.*

<!-- label: III.XVII.2.6 -->

Let us recall (Exp. VII_A § 3) that when $G$ is an $S$-prescheme in commutative groups, finite and flat over $S$, one
has Cartier duality at one's disposal, and $G$ is reflexive in the sense of Exp. VIII § 1. More precisely, the functor
$G \mapsto \operatorname{Hom}_{S-gr}(G, G_{m})$ is representable

<!-- original page 542 -->

by an $S$-prescheme in commutative groups $D(G)$, finite and flat over $S$, and the canonical morphism $G \to D(D(G))$
is an isomorphism. In particular, one obtains:

(i) $D(\mu_{n}) \simeq \mathbb{Z}/n\mathbb{Z}$ and consequently $D(\mathbb{Z}/n\mathbb{Z}) \simeq \mu_{n}$.

(ii) If $S$ is of characteristic $p > 0$, $D(\alpha_{p}) \simeq \alpha_{p}$.

## 3. Unipotent groups acting on a vector space

<!-- label: III.XVII.3 -->

<!-- original page 542 -->

Let us recall (Exp. I, 4.6.1) that if $S$ is a prescheme and $M$ a sheaf of `O_S`-modules, one denotes by $W(M)$ the
$S$-functor $(Sch/S)^{\circ} \to (Ens)$ defined by the condition $W(M)(S') = \Gamma(S', M \otimes O_{S'})$ for every
$S$-prescheme $S'$.

Moreover, let us recall that if an $S$-group acts on an $S$-functor $V$, one defines the $S$-functor $V^{G}$ of
invariants of $V$ under $G$ as the subfunctor of $V$ whose set of points with values in some $S'$ over $S$ is the set of
$x \in V(S')$ such that $x_{S''}$ is fixed under $G(S'')$ for every `S''` over $S'$.

This being so, one has the following lemma:

**Lemma 3.1.** *Let $S$ be a prescheme, $G$ an $S$-prescheme in groups, affine over $S$, defined by the quasi-coherent
`O_S`-algebra $A$. Suppose that $G$ acts on a quasi-coherent sheaf of `O_S`-modules $M$, and let
$\mu : M \to A \otimes_{O_{S}} M$ be the comorphism defining the action of $G$ on $M$ (Exp. I, 4.7.2), and
$\nu : M \to A \otimes_{O_{S}} M$ the morphism $x \mapsto \mu(x) - 1 \otimes x$. Then:*

<!-- label: III.XVII.3.1 -->

*i) $M^{G}(S) = \Gamma Ker(\nu)$.*

*ii) If $S$ is the spectrum of a field $k$, $M^{G}$ is of the form $W(N)$, where $N$ is a vector subspace of $M$.*

*iii) If $S$ is the spectrum of a field $k$, every element $x$ of $M$ is contained in a finite-dimensional $k$-vector
subspace of $M$, stable under the action of $G$.*

<!-- original page 543 -->

*Proof.* iii) is included for the record and has already been proved in Exp. VI_B, 11.2.

i) It is clear that $M^{G}(S)$ contains $\Gamma Ker(\nu)$. To establish the converse, one may suppose $S$ affine with
ring $B$. Let $m \in M^{G}(S)$. Then for every $B$-algebra $B'$ and every $u$ in $\operatorname{Hom}_{B-alg}(A, B')$
($u$ corresponds to an element of $G(\operatorname{Spec} B')$), one has:

```text
(u ⊗ 1_M) ν(m) = 0   in   B' ⊗_B M.
```

Taking in particular $B' = A$ and $u$ the identity of $A$, one finds $\nu(m) = 0$.

ii) Let $N$ be the kernel of $\nu$, equal to $M^{G}(k)$ by i). Every $k$-prescheme $S$ is flat over $k$, so one has:

```text
M^G(S) = Γ Ker(ν ⊗_k S) = Γ(N ⊗_k S).
```

So $M^{G}$ is isomorphic to the functor $W(N)$.

**Proposition 3.2.** *Let $G$ be a unipotent algebraic group defined over a field $k$, acting on a $k$-vector space $V$.
Then if $V \neq 0$, one has $V^{G} \neq 0$.*

<!-- label: III.XVII.3.2 -->

In view of 3.1 ii) and iii), one may suppose $k$ algebraically closed and $V$ of finite dimension over $k$.

Let $0 \to G' \to G \to G'' \to 0$ be an exact sequence of algebraic groups and suppose that $G$ acts on a sheaf $V$
(for the fpqc topology). Of course $V^{G} \subset V^{G'}$,

<!-- original page 544 -->

and the quotient presheaf $G/G'$ acts naturally on $V^{G'}$. But $V^{G'}$ is a sheaf (as kernel of the well-known pair
of morphisms $V \Rightarrow \operatorname{Hom}(G', V)$); consequently, the sheaf associated with $G/G'$, that is, `G''`,
acts on $V^{G'}$, and it is immediate to verify that $(V^{G'})^{G''} = V^{G} = (V^{G'})^{G/G'}$.

This remark allows us to reduce, in order to prove 3.2, to the case where $G$ is an elementary unipotent group (1.7).

a) $G = G_{a}$, $p = 0$. It follows from (*Bible* 4 prop. 4) that a morphism from $G_{a}$ into the linear group $GL(V)$
is given by an exponential map:

```text
T ↦ Σ_{q=0}^∞ T^q n^q / q!
```

where $n$ is a nilpotent endomorphism of $V$. But then $V \neq 0 \Rightarrow Ker n \neq 0$, and it is clear that every
vector of $V$ annihilated by $n$ is left fixed by $G$.

Suppose now $p > 0$.

b) $G = \alpha_{p}$. The group $\alpha_{p}$ being a radicial group of height 1 (Exp. VII_A § 7), giving a representation
of $\alpha_{p}$ in $V$ amounts to giving a representation of the $p$-Lie algebra $\alpha_{p}$ in $gl(V)$ (App. II 2.2),
that is, here, to giving an element $X$ of $\operatorname{End}(V)$ such that $X^{p} = 0$ (App. II 2.1). But then
$V \neq 0 \Rightarrow W = Ker(X) \neq 0$, and still by (App. II 2.2), one has $W = V^{\alpha_{p}}$.

c) $G = \mathbb{Z}/p\mathbb{Z}$. A representation of $G$ in $V$ is equivalent to giving an element $x$ of
$\operatorname{Aut}(V)$ such that $x^{p} = 1$, i.e. $(1 - x)^{p} = 0$, so $x$ is of the form $1 + n$ with $n$ nilpotent,
and $W = Ker n$ is left fixed by $x$.

<!-- original page 545 -->

d) $G = G_{a}$. Let $G_{i}$, $i \in I$, be the increasing filtered family of étale algebraic subgroups of $G_{a}$, hence
isomorphic to $(\mathbb{Z}/p\mathbb{Z})^{r_{i}}$ (prop. 1.5), and let $V_{i} = V^{G_{i}}$. Since $V$ is of finite,
non-zero dimension, and $V_{i}$ is non-zero by c), the decreasing filtered family of the $V_{i}$ is stationary, and
$W = \bigcap_{i \in I} V_{i} \neq 0$. Now one has the lemma:

**Lemma 3.3.** *The family of étale subgroups of $(G_{a})_{S}$ ($S$ an $S$-prescheme of characteristic $p > 0$) is
schematically dense in $G$ (Exp. IX, 4.1).*

<!-- label: III.XVII.3.3 -->

By Exp. IX, 4.4, it suffices to prove the lemma when $S$ is the spectrum of the prime field $F_{p}$. In this case, it
suffices to consider the family of étale subgroups $G_{n}$ ($n \geqslant 1$) with equation $X^{p^{n}} - X = 0$, which is
schematically dense in $(G_{a})_{F_{p}}$ since it contains every closed point.

This being so, let us return to the proof of 3.2 d). If $w \in W$, its stabilizer in $G$ is an algebraic subgroup of
$G_{a}$ that majorizes $G_{i}$ for every $i \in I$, hence is equal to $G_{a}$ (3.3), and consequently $W = V^{G}$.

One deduces immediately from 3.2 the

**Corollary 3.4.** *Let $k$ be a field, $G$ a unipotent $k$-algebraic group acting on a finite-dimensional $k$-vector
space $V$. Then $V$ possesses a sequence of vector subspaces $V_{i}$, defined over $k$, stable under $G$,*

<!-- label: III.XVII.3.4 -->

<!-- original page 546 -->

```text
0 = V_0 ⊂ V_1 ⊂ … ⊂ V_n = V,
```

*such that $G$ acts trivially on $V_{i+1} / V_{i}$. One may further suppose $V_{i+1} / V_{i}$ of dimension 1.*

We shall now summarize and complement the properties of unipotent groups already proved, in the following theorem:

**Theorem 3.5.** *Let $G$ be an algebraic group defined over a field $k$. The following properties are equivalent:*

<!-- label: III.XVII.3.5 -->

*i) $G$ is unipotent.*

*ii) $G$ possesses a composition series, defined over $k$, whose successive quotients are isomorphic to $G_{a}$ if
$p = 0$ (resp. to $\alpha_{p}$, $G_{a}$, or twisted $(\mathbb{Z}/p\mathbb{Z})^{r}$ (1.4) if $p > 0$).*

*iii) As in ii), but one further assumes the composition series to be central.*

*iv) $G$ possesses a characteristic composition series (Exp. VI_B) defined over $k$, whose successive quotients are
isomorphic to $(G_{a})^{r}$ if $p = 0$ (resp. to $(\alpha_{p})^{r}$, twisted $(G_{a})^{s}$, or twisted
$(\mathbb{Z}/p\mathbb{Z})^{t}$, taken in this order, if $p > 0$).*

*v) $G$ is isomorphic to an algebraic subgroup of the group $Trigstr(n)_{k}$ of strictly upper-triangular matrices of
the linear group $GL(n)_{k}$, for some suitable integer $n \geqslant 0$.*

*vi) $G$ is affine and, for every linear representation of $G$ in a non-zero finite-dimensional $k$-vector space $V$,
one has $V^{G} \neq 0$.*

<!-- original page 547 -->

*Proof.*

i) ⇒ vi) by 2.1 and 3.2.

vi) ⇒ v). Since the algebraic group $G$ is affine, $G$ is an algebraic subgroup of a suitable linear group $GL(V)$ (Exp.
VI_B, 11.3). Applying 3.4 to the representation of $G$ in $V$ defined by this embedding, one finds v).

v) ⇒ iii). One knows that the algebraic group $Trigstr(n)$ possesses a central composition series with successive
quotients isomorphic to $G_{a}$. The composition series induced on $G$ gives property iii), taking 1.5 into account.

iii) ⇒ ii) ⇒ i) and iv) ⇒ i) is clear.

We shall prove i) ⇒ iv) shortly, but first let us note some consequences of what has been proved.

**Definition 3.6.** *We shall say that a $p$-Lie algebra $g$ ($p > 0$) (cf. Exp. VII_A § 5) is* unipotent *if the map
$x \mapsto x^{(p)}$ is nilpotent, i.e. if for every $x \in g$, there exists an integer $n > 0$ such that
$x^{(p^{n})} = 0$.*

<!-- label: III.XVII.3.6 -->

**Corollary 3.7.** *A unipotent algebraic group $G$ is nilpotent (Exp. VI_B § 8); its Lie algebra $g$ is nilpotent
(Bourbaki, *Groupes et algèbres de Lie*, Chap. 1 § 4) and is isomorphic to a Lie algebra of nilpotent endomorphisms of a
finite-dimensional vector space.*

<!-- label: III.XVII.3.7 -->

<!-- original page 548 -->

*In characteristic $p > 0$, $g$ is a unipotent $p$-Lie algebra (3.6).*

Since i) ⇒ v), it suffices to prove 3.7 when $G = Trigstr(n)$. We have already used the fact that $Trigstr(n)$ is a
nilpotent algebraic group. Moreover, the Lie algebra $h$ of $Trigstr(n)$ consists of the upper-triangular endomorphisms
of $V$ having zeros on the principal diagonal. They are therefore nilpotent and consequently $h$ is nilpotent (Bourbaki,
*loc. cit.* Chap. 1 § 4 cor. 3). If $p > 0$, since the $p$-th power in the $p$-Lie algebra
$gl(V) = \operatorname{End}(V)$ coincides with the $p$-th power of the endomorphisms of $V$ (Exp. VII_A, 6.4.4), one
sees that $h$ is unipotent.

**Corollary 3.8.** *Let $k$ be an algebraically closed field and $G$ a smooth and affine algebraic group over $k$. Then
the following properties are equivalent:*

<!-- label: III.XVII.3.8 -->

*i) $G$ is unipotent.*

*ii) $G(k)$ consists of unipotent elements (*Bible* 4 prop. 4 cor. 1), that is, $G$ is unipotent in the sense of the
*Bible*.*

i) ⇒ ii) because $G$ is isomorphic to an algebraic subgroup of a group $Trigstr(n)$ by 3.2 i) ⇒ v).

ii) ⇒ i). Let $G$ be an algebraic group, unipotent in the sense of the *Bible*, and let $G^{0}$ denote its identity
component. The maximal tori of $G^{0}$, being made up of unipotent elements, are trivial, so $G^{0}$ is equal to its
Cartan subgroups. Consequently, $G^{0}$ is solvable (*Bible* 6 Th. 6), hence triangularizable (*Bible* 6, Th. 1). In
brief, $G^{0}$ is an algebraic subgroup of a group $Trigstr(n)$, and is therefore unipotent in the sense of the present
Exposé.

The group $(G/G^{0})(k)$ is a finite group made up of unipotent elements; it is therefore zero if $p = 0$ and equal to a
finite $p$-group if $p > 0$ (*Bible* 4 prop. 4). But then $G/G^{0}$ is unipotent in the sense of the present Exposé as a
multiple extension of groups isomorphic to $\mathbb{Z}/p\mathbb{Z}$. This proves that $G$ is unipotent.

*End of the proof of 3.5.* Let us prove that i) ⇒ iv).

<!-- original page 549 -->

a) $p > 0$. Consider the increasing sequence of algebraic subgroups of $G$:

```text
{e} ⊂ F(G) ⊂ F_2(G) ⊂ ⋯ ⊂ F_n(G) ⊂ G⁰ ⊂ G.
```

One thus obtains a characteristic composition series of $G$ (App. II 1), and for $n$ large enough, $G / F_{n}(G)$ is
smooth (App. II 3.1), so that the successive quotients are, in order:

(1) radicial groups of height 1,

(2) a smooth and connected group,

(3) an étale group.

To prove i) ⇒ iv) it therefore suffices to prove the:

**Lemma 3.9.** *Let $G$ be a unipotent algebraic group defined over a field $k$ of characteristic $p > 0$. Then $G$
possesses a characteristic composition series, defined over $k$, whose successive quotients are isomorphic to:*

<!-- label: III.XVII.3.9 -->

*i) $(\alpha_{p})^{r}$ if $G$ is radicial.*

*ii) Twisted $(G_{a})^{r}$ if $G$ is smooth and connected.*

*iii) Twisted $(\mathbb{Z}/p\mathbb{Z})^{r}$ if $G$ is étale.*

*Proof.* i) The group $G$ is radicial. Filtering $G$ by the $F_{n}(G)$, one reduces to the case where $G$ is radicial of
height 1. Since $G$ is nilpotent (3.5 i) ⇒ iii)), and since the center of an algebraic group is representable (Exp.
VIII, 6.5 e)), one may consider the ascending central series of $G$, evidently characteristic in $G$, which reduces us
to the case where $G$ is moreover commutative.

<!-- original page 550 -->

Let $g = Lie(G)$. The $p$-th power morphism $\pi$ is therefore additive on $g$ (Exp. VII_A); we shall reduce to the case
where it is zero. For every prescheme $S$ over $k$, set $g_{S} = g \otimes_{k} O_{S}$, and let $h_{S}$ be the subsheaf
of abelian groups of $g_{S}$ image of $g_{S}$ under $\pi_{S}$. Finally, let $\bar{h}_{S}$ be the subsheaf of
`O_S`-modules of $g_{S}$ generated by $h_{S}$. It is clear that $\bar{h}_{S} = \bar{h}_{k} \otimes_{k} O_{S}$ and that
$\bar{h}_{S}$[^N.D.E-XVII-4] is a characteristic sub-$p$-Lie algebra of $g_{S}$ (i.e. is stable under the $S$-functor
$\operatorname{Aut}_{p-Lie}(g)$). It then follows from App. II 2.2 that $\bar{h}_{k}$ is the Lie algebra of an algebraic
subgroup $H$ of $G$ that is characteristic in $G$.

Moreover, taking 3.7 and Lemma 3.9 bis below into account, if $G \neq {e}$, $H$ is distinct from $G$, because
$\bar{h}_{k}$ is distinct from $g$. On the other hand, if $G/H = G''$, one has $Lie G'' = g / \bar{h}_{k}$ (App. II
2.2), and consequently, the $p$-th power is zero in `Lie G''`. Proceeding by induction on $\dim Lie G$, we are thus
reduced to the case where `Lie G` is a $p$-Lie algebra in which the $p$-th power is zero. But then `Lie G''` is
isomorphic to $Lie(\alpha_{p})^{r}$ for some suitable integer $r \geqslant 0$ (App. II 2.1), and consequently (App. II
2.2), `G''` is isomorphic to $(\alpha_{p})^{r}$. It remains to prove the:

**Lemma 3.9 bis.** *Let $k$ be a field of characteristic $p > 0$, $g$ a commutative, unipotent (3.6), finite-dimensional
$p$-Lie algebra over $k$, and $h$ the sub-$p$-Lie algebra of $g$ generated by the image of the $p$-th power in $g$. Then
if $g \neq 0$, one has $h \neq g$.*

<!-- label: III.XVII.3.9bis -->

Indeed, since $g$ is commutative, $h$ is simply the $k$-vector subspace of $g$ generated by the $X^{(p)}$ ($X \in g$).
If $g \neq 0$ and is unipotent, there exists $X \in g$, $X \neq 0$, such that $X^{(p)} = 0$.

<!-- original page 551 -->

Let $X_{1}, \cdots, X_{n}$ be a basis of a supplement in $g$ of the line `kX`. The Lie algebra $h$ is then the
$k$-vector subspace of $g$ generated by $X^{(p)}_{1}, \cdots, X^{(p)}_{n}$, hence has dimension at most
$n = \dim g - 1$.

*Proof of 3.9 ii)*. $G$ is smooth and connected. In this case, the descending central series of $G$ is representable by
characteristic smooth connected algebraic subgroups $G_{i}$ (Exp. VI_B, 8.3 and 7.4), and $G_{i} = 0$ for $i$ large
enough, since $G$ is nilpotent (3.5 i) ⇒ iii)). It suffices to prove 3.9 for the groups $G_{i} / G_{i+1}$, which reduces
us to the case where moreover $G$ is commutative. For every integer $n > 0$, let $G_{n}$ be the algebraic subgroup of
$G$ which is the image of $G$ under the $p^{n}$-th power morphism. The group $G_{n}$ is therefore smooth, connected and
characteristic, and it follows from Definition 1.1 of unipotent groups that $G_{n} = 0$ for $n$ large enough. Replacing
$G$ by $G_{n} / G_{n+1}$, one may further suppose that $G$ is annihilated by raising to the $p$-th power. But then, by
(J.-P. Serre, *Groupes algébriques et corps de classes*, Chap. VII, prop. 11), $G$ is a form of $(G_{a})^{r}$ for some
suitable integer $r$.

*Proof of 3.9 iii)*. $G$ is étale. Proceeding as in ii), one reduces to the case where $G$ is commutative, then to the
case where $G$ is annihilated by $p$, but then $G_{\bar{k}}$ is isomorphic to $(\mathbb{Z}/p\mathbb{Z})^{r}$.

*Proof of 3.5 i) ⇒ iv) in the case b)* $p = 0$. The group $G$ is then smooth and connected, and proceeding as in 3.9
ii), one reduces to the case where $G$ is moreover commutative. One then has the following more precise result:

**Lemma 3.9 ter.** *Let $k$ be a field of characteristic `0`, $G$ a commutative unipotent $k$-algebraic group,
$g = Lie G$. Then there exists a canonical isomorphism:*

<!-- label: III.XVII.3.9ter -->

<!-- original page 552 -->

$$
\exp : W(g) \xrightarrow{\sim} G.
$$

*The morphism `exp` is the unique homomorphism $W(g) \to G$ that induces the identity on Lie algebras.*

Since $G$ is unipotent, $G$ is realized as an algebraic subgroup of $Trigstr(n)$ for some suitable integer $n$ (3.5 i) ⇒
v)). The choice of such an embedding allows one to identify $g$ with a Lie subalgebra of $gl(n)$ consisting of nilpotent
endomorphisms. Whence a $k$-morphism:

```text
exp : W(g) ⟶ GL(n),    T ↦ Σ_{i ⩾ 0} T^i / i!.
```

Since $G$ is commutative, the morphism `exp` is a homomorphism. Let $G'$ be the algebraic group image of $W(g)$ under
the morphism `exp`. If one canonically identifies `Lie W(g)` with $g$, the linear tangent map of `exp` is simply the
injection $g \to gl(n)$. Consequently $Lie(G \cap G') = g \cap g = g$. Since $G \cap G'$ is smooth (Exp. VI_B, 1.6.1)
and $G$ is connected (being a multiple extension of groups $G_{a}$ (3.5 i) ⇒ ii)), one necessarily has $G = G'$. The
kernel $Ker(\exp)$ is a unipotent étale group, hence is the trivial group, and consequently `exp` is an isomorphism of
$W(g)$ onto $G$.

If $h : W(g) \to G$ is another homomorphism such that $Lie(h)$ is the identity map of $g$, the morphism $h - \exp$ is a
homomorphism ($G$ being commutative) whose linear tangent map is therefore zero. Since $k$ is of characteristic 0 and
$W(g)$ is connected, it again follows from Cartier's theorem that one necessarily has $h = \exp$.

<!-- original page 553 -->

**Proposition 3.10.** *Let $G$ be an algebraic group defined over an algebraically closed field $k$. Then the following
properties are equivalent:*

<!-- label: III.XVII.3.10 -->

*i) Every morphism of a group of multiplicative type $M$ into $G$ is the zero morphism.*

*i bis) $G$ has no non-zero subgroups of multiplicative type.*

*ii) a) if $p = 0$: $G(k)$ contains no points of finite order other than $e$;*

*b) if $p \neq 0$: for every prime number $q \neq p$, $x \in G(k)$ and $x^{q} = e$ imply $x = e$,*

```
   *for every `X ∈ g = Lie G` such that `X^{(p)} = X`, one has `X = 0`.*
```

*ii bis) a) if $p = 0$: as in ii) a);*

```
   *b) if `p ≠ 0`: every finite subgroup of `G(k)` is a `p`-group,*

          *for every `X ∈ g = Lie G` such that `X^{(p)} = X`, one has `X = 0`.*
```

*Proof.*

i) ⇔ i bis), since the image of a group of multiplicative type is of multiplicative type (Exp. IX, 2.7).

<!-- original page 554 -->

ii) ⇔ ii bis). Because if an ordinary finite group $H$ has order not a power of $p$, there exists a prime number
$q \neq p$, and an element $x$ of $H$ distinct from $e$, such that $x^{q} = e$ (Sylow's theorem, cf. J.-P. Serre, *Corps
locaux*, Chap. IX § 2).

i) ⇒ ii) follows from the following lemma:

**Lemma 3.11.** *Let $G$ be an algebraic group defined over a field $k$.*

<!-- label: III.XVII.3.11 -->

*a) If $k$ contains the $n$-th roots of unity, with $n$ an integer prime to $p$, one has:*

```text
Hom_{k-gr}(μ_n, G) ≃ Hom_{k-gr}(ℤ/nℤ, G) ≃ _n G(k)
```

*(points of order $n$ of $G(k)$).*

*b) If $p > 0$, `Hom_{k-gr}(μ_p, G) ≃ {X ∈ g = Lie G, such that X^{(p)} = X}`.*

Indeed, to prove a) we note that $\mu_{n}$ is then isomorphic over $k$ to $\mathbb{Z}/n\mathbb{Z}$, and b) is a
consequence of App. II 2.1.

ii) ⇒ i bis). By Lemma 3.11, ii) is equivalent to the fact that for every prime number $r$, $G$ does not contain any
subgroups $\mu_{r}$, which entails i bis) by reason of the:

**Lemma 3.12.** *Let $G$ be a diagonalizable $S$-group, of finite type over $S$ and distinct from the trivial group.
Then there exists a prime number $r$ and a subgroup of $G$ isomorphic to $(\mu_{r})_{S}$.*

<!-- label: III.XVII.3.12 -->

Let $G = D_{S}(M)$, where $M$ is a finitely generated abelian group, hence extension of a free group `M''` by a finite
group $M'$. If $M'' \neq 0$, it is clear that $M$ admits quotients isomorphic to $\mathbb{Z}/r\mathbb{Z}$ for every
integer $r$. If $M'' = 0$, $M'$ admits a quotient isomorphic to $\mathbb{Z}/r\mathbb{Z}$ for every prime number $r$
dividing the order of $M$.

<!-- original page 555 -->

One then deduces the lemma by duality.

We have seen (Prop. 2.4) that a unipotent group satisfies the equivalent conditions of 3.10. The aim of the next section
is to prove the converse.

## 4. A characterization of unipotent groups

<!-- label: III.XVII.4 -->

<!-- original page 556 -->

As announced, we shall show that an algebraic group $G$ defined over an algebraically closed field $k$, which does not
contain any non-zero subgroup of multiplicative type, is unipotent. In fact, it suffices that it does not contain
certain particular "elementary" subgroups of multiplicative type, which depend on the hypotheses made on $G$. Before
stating the general theorem, let us study in detail some special cases.

### 4.1. Smooth, connected, affine algebraic groups

<!-- label: III.XVII.4.1 -->

**Proposition 4.1.1.** *Let $k$ be a field, $G$ a smooth, connected, affine $k$-algebraic group, $g = Lie G$. Then the
following properties are equivalent:*

<!-- label: III.XVII.4.1.1 -->

*i) $G$ is unipotent.*

*ii) $G$ possesses a central composition series whose successive quotients are forms of $G_{a}$.*

*iii) $G$ possesses a central, characteristic composition series whose successive quotients are forms of $(G_{a})^{r}$.*

*iv) There exists an integer $n > 1$ such that $G_{\bar{k}}$ does not contain any subgroup isomorphic to $\mu_{n}$.*

*v) Every maximal torus of $G$ is the trivial group.*

*Suppose moreover that $G$ is an algebraic subgroup of a linear group $GL(n)$. Then the preceding conditions are also
equivalent to:*

<!-- original page 557 -->

*vi) $g \subset gl(n)$ consists of nilpotent endomorphisms.*

*vii) $g$ is nilpotent and its center contains no non-zero semisimple endomorphism.*

*Proof.* ii) ⇒ i) is clear, and i) ⇒ iii) was seen in 3.9. The implication iii) ⇒ ii) will follow from the following
lemma:

**Lemma 4.1.2.** *Let $k$ be a field, $G$ a $k$-algebraic group which is a form of $(G_{a})^{r}$. Then:*

<!-- label: III.XVII.4.1.2 -->

*a) $G$ is realized as an algebraic subgroup of the group $(G_{a})^{n}$ for some suitable integer $n$.*

*b) $G$ possesses a composition series whose successive quotients are forms of $G_{a}$.*

Indeed, by hypothesis, there exists an extension $k'$ of $k$ such that $G_{k'}$ is isomorphic to $(G_{a, k'})^{r}$. By
the principle of finite extension (EGA IV 9.1.1), one may suppose that $k'$ is a finite extension of $k$. But then, for
a), it suffices to consider the canonical closed immersion (EGA V[^N.D.E-XVII-5]):

```text
G ⟶ ∏_{k'/k} (G_{k'})/k' ⥲ (G_{a, k})^n   (with n = r deg(k'/k)).
```

To prove b), in view of a), one may suppose that $G$ is a closed subgroup of $G' = (G_{a})^{n}$. If $G \neq 0$, there
exists a hyperplane $h$ of $g' = Lie G'$ not containing $g$. Let $H$ be the vector subgroup $W(h)$ of $W(g') = G'$.
Since $H$ is defined by an equation in $G'$, $H \cap G$ is defined by an equation in $G$, and one has the inequalities:

```text
dim G − 1 ⩽ dim(G ∩ H)
         ⩽ dim Lie(G ∩ H) = dim_k(g ∩ h) = dim_k(g) − 1 = dim G − 1.
```

Hence `dim(G ∩ H) = dim Lie(G ∩ H)`, and consequently $G \cap H$ is smooth. The group $G_{1} = (G \cap H)^{0}$

<!-- original page 558 -->

is an algebraic subgroup of $G$, smooth and connected, such that $G/G_{1}$ is smooth, connected, of dimension 1, hence a
form of $G_{a}$ (4.1 i) ⇒ iii)). One finishes by induction on the dimension of $G$.

Before continuing the proof of 4.1, let us note that the equivalence i) ⇔ ii) and 2.3 bis entail the following
corollary:

**Corollary 4.1.3.** *If $k$ is a perfect field, a smooth and connected $k$-algebraic group is unipotent if and only if
it possesses a composition series whose successive quotients are isomorphic to $G_{a}$.*

<!-- label: III.XVII.4.1.3 -->

*Continuation of the proof of 4.1.*

i) ⇒ iv) by 2.4 i).

iv) ⇒ v). By Exp. XIV, 4.1, $G$ possesses a maximal torus $T$ defined over $k$. Now if $r = \dim T$,
$({}_{n} T)_{\bar{k}}$ is isomorphic to $(\mu_{n})^{r}$. Hence $r = 0$.

v) ⇒ i) as remarked in the proof of 3.8.

i) ⇒ vi). By 3.4, $G$ is in fact contained in an algebraic subgroup of $GL(n)$ isomorphic to $Trigstr(n)$, hence $g$
consists of nilpotent endomorphisms.

vi) ⇒ vii). Indeed, $g$ is nilpotent by Engel's theorem (Bourbaki, *Groupes et algèbres de Lie*, Chap. I § 4 cor. 3).

vii) ⇒ v). Let $T$ be a maximal sub-torus of $G$ (Exp. XIV, 1.1), $t$ its Lie algebra. The embedding of $G$ in $GL(n)$
defines a representation of $T$ which is necessarily semisimple (this is seen on an algebraic closure $\bar{k}$ of $k$,
and one applies Exp. I, 4.7.3).

<!-- original page 559 -->

Hence if $X \in t$, $X$ is a semisimple endomorphism in $gl(n)$. One sees immediately that this entails that the map

```text
ad X : Y ↦ [X, Y]
```

is a semisimple endomorphism of $gl(n)$, hence of $g$. Since, moreover, this endomorphism is nilpotent ($g$ being
nilpotent), `ad X` is zero, so $X$ is central. But then $t$ is central and consists of semisimple endomorphisms, hence
is zero by hypothesis; *a fortiori*, $T$ is the trivial group.

**Remark 4.1.4.**

<!-- label: III.XVII.4.1.4 -->

*a) We shall give below (4.3.1) an infinitesimal characterization of unipotent groups in characteristic $p > 0$, which
is independent of an embedding in $GL(n)$.*

*b) When $k$ is perfect, conditions ii) and iii) of 4.1.1 simplify by reason of the following lemma:*

**Lemma 4.1.5.** *If $k$ is a perfect field, every $k$-algebraic group $G$ which is a form of $(G_{a})^{r}$ is
isomorphic to $(G_{a})^{r}$.*

<!-- label: III.XVII.4.1.5 -->

The lemma follows from 3.9 ter if the characteristic $p$ of $k$ is zero, and from 2.3 bis if $r = 1$. In the general
case ($p > 0$), realize $G$ as an algebraic subgroup of $(G_{a})^{n}$ for some suitable integer $n$ (4.1.2), and argue
by induction on the integer $n - r$. If $r = n$, one indeed has $G = (G_{a})^{r}$. Otherwise the quotient group
$G^{n}_{a} / G$ is a non-zero smooth connected unipotent group which, taking 4.1.1 i) ⇒ ii) and 2.3 bis into account,

<!-- original page 560 -->

possesses a composition series with quotients isomorphic to $G_{a}$. One deduces that there exists an algebraic subgroup
`G_1` of $(G_{a})^{n}$, smooth and connected, containing $G$, such that $G^{n}_{a} / G_{1} = G_{a}$. By induction it
suffices to show that `G_1` is isomorphic to $(G_{a})^{n-1}$. Now it is immediate to verify that a homomorphism from
$\operatorname{Spec} k[X_{1}, \cdots, X_{n}] = G^{n}_{a}$ to $G_{a} = \operatorname{Spec} k[T]$ is defined by an
additive polynomial of the form:

$$
\Sigma_{i,j} a_{i,j} X^{p^{j}}_{i}.
$$

Since `G_1` is smooth, the linear part of this polynomial is non-zero. Possibly making a linear change of the
coordinates $X_{i}$, we may assume that `G_1` is an algebraic subgroup of $(G_{a})^{n}$ defined by the equation:

```text
(*)   P(X) = −X_1 + Σ_{j=1}^q a_j X_1^{p^j} + Q(X_2, …, X_n) = 0,
                                        with   Q(X_2, …, X_n) = Σ_{i>1, j>0} b_{i,j} X_i^{p^j}.
```

Proceed then by induction on the degree of $P$. If $deg P = 1$, it is clear that $G_{1} \xrightarrow{\sim} G^{n-1}_{a}$.
Otherwise, since $k$ is perfect, one has $Q(X) = Q_{1}(X)^{p}$ and we may define an endomorphism $v$ of $G^{n}_{a}$ by
the formulas:

```text
X_i ↦ X_i   for i > 1,        X_1 ↦ Σ_{j=1}^q a_j^{1/p} X_1^{p^{j−1}} + Q_1(X).
```

It is clear that $v$ induces an isomorphism on `G_1` and that $v(G_{1})$ has equation in $G^{n}_{a}$:

```text
(*)_1   P_1(X) = −X_1 + Σ_{j=1}^q a_j^{1/p} X_1^{p^j} + Q_1(X_2, …, X_n) = 0.
```

Let us then distinguish two cases:

<!-- original page 561 -->

*1st case.* $deg(Q) = deg P > p^{q}$. Then $deg P_{1} < deg P$ and one wins by the induction hypothesis.

*2nd case.* $deg P = p^{q}$ ($a_{q} \neq 0$). One then has $deg P_{1} = deg P = p^{q}$ and $deg Q_{1} < p^{q}$. (One
cannot have $Q = 0$, otherwise `G_1` would not be connected.) If the polynomial `Q_1` has no linear part, one can
iterate the preceding transformation. Continuing the process, one finally obtains an equation of the form:

```text
(*)_s   P_s(X) = −X_1 + Σ_{j=1}^q a_j^{1/p^s} X_1^{p^j} + Q_s(X),
```

where $Q_{s}(X) = Q(X_{2}, \cdots, X_{n})^{1/p^{s}}$ is an additive polynomial having a non-zero linear part, and
moreover $deg Q_{s} < p^{q}$. Suppose, for example, that the coefficient of `X_2` in $Q_{s}$ is non-zero, and let $-L$
be the linear part of $P_{s}(X)$. Possibly making a linear change of coordinates, the equation of `G_1` becomes:

```text
P'(X) = −L + Σ_{j=1}^q a_j^{1/p^s} X_1^{p^j} + Q'(L, X_3, …, X_n),
```

where $Q'$ is an additive polynomial without linear part, and $deg(Q') < p^{q}$. But then we are reduced to the first
case.[^N.D.E-XVII-6]

### 4.2. Radicial groups

<!-- label: III.XVII.4.2 -->

**Proposition 4.2.1.** *Let $G$ be a radicial algebraic group defined over a field $k$ of characteristic $p > 0$. Then
the following conditions are equivalent:*

<!-- label: III.XVII.4.2.1 -->

*i) $G$ is unipotent.*

*ii) $G$ possesses a central composition series with successive quotients isomorphic to $\alpha_{p}$.*

<!-- original page 562 -->

*iii) $G$ possesses a central and characteristic composition series with successive quotients isomorphic to
$(\alpha_{p})^{r}$.*

*iv) $G_{\bar{k}}$ contains no subgroup isomorphic to $\mu_{p}$.*

*v) $g = Lie G$ is a unipotent $p$-Lie algebra (3.6).*

*Proof.* iii) ⇒ ii) ⇒ i) is clear, i) ⇒ iii) is 3.9 i), and i) ⇒ iv) by 2.4 i).

We shall need the following lemma on abelian $p$-Lie algebras:

**Lemma 4.2.2.** *Let $g$ be an abelian, finite-dimensional $p$-Lie algebra over a perfect field $k$. Then $g$ can be
written uniquely as a direct sum of a sub-$p$-Lie algebra $r$ on which the $p$-th power is bijective, and a sub-$p$-Lie
algebra $u$, unipotent (3.6). (The algebra $r$ will be called the* reductive part *of $g$ and $u$ the* unipotent
part\*.) The formation of $r$ and $u$ is compatible with extension of the field $k$. If moreover $k$ is algebraically
closed, $r$ admits a basis $e_{i}$ such that $e^{(p)}_{i} = e_{i}$.\*

<!-- label: III.XVII.4.2.2 -->

The proof of this lemma is easy and left to the reader (cf. Bourbaki, *Groupes et algèbres de Lie*, Chap. I § 1 exercise
23). Let us simply say that $u$ is the kernel of a suitable iterate of the map $X \mapsto X^{(p)}$, and that $r$ is the
image of the same iterate.

<!-- original page 563 -->

This being so, let us prove iv) ⇒ v). Possibly making an extension of the base field, one may suppose $k$ algebraically
closed.

Let then $X$ be an element of $g$ and $h$ the sub-$p$-Lie algebra generated by $X$ in $g$. The algebra $h$ is evidently
commutative, and its reductive part (4.2.2) is zero, otherwise by *loc. cit.*, $h$ would contain an element $Y \neq 0$
such that $Y^{(p)} = Y$, and consequently (App. II 2.1 and 2.2) $G$ would contain a subgroup isomorphic to $\mu_{p}$
contrary to hypothesis. Hence $h$, and consequently $g$, is a unipotent $p$-Lie algebra.

v) ⇒ i). This is the least trivial implication of 4.2.1.

a) Case where $G$ is of height 1 (Exp. VII_A, 4.1.3). Since $G$ is radicial, it is affine, hence isomorphic to an
algebraic subgroup of a linear group $GL(V)$ (Exp. VI_B, § 11). This embedding identifies $g$ with a sub-$p$-Lie algebra
of $\operatorname{End}(V)$, the $p$-th power of $X$ in $g$ coinciding with the $p$-th power of the endomorphism $X$
(Exp. VII_A, 6.4.4). Since $g$ is unipotent by hypothesis, $g$ is therefore an algebra of nilpotent endomorphisms of
$V$, and by Engel's theorem (Bourbaki, *Groupes et algèbres de Lie*, Chap. I § 4 th. 1) is a Lie subalgebra of the Lie
algebra $h$ of the group of strictly upper-triangular matrices $Trigstr(n)$ with respect to a suitable basis of $V$.
Since $G$ is of height 1, one then deduces from App. II 2.2 that $G$ itself is an algebraic subgroup of $Trigstr(n)$,
hence is unipotent (3.5 v) ⇒ i)).

b) General case. Proceed by induction on the height $h$ of $G$[^XVII-4-1]. The case $h = 1$ has just been treated.
Suppose $h > 1$, and set $G' = F G$ and $G'' = G/G'$. The group $G'$ is of height 1 and $Lie G' = Lie G$ is unipotent,
hence $G'$ is unipotent by a).

<!-- original page 564 -->

To show that $G$ is unipotent, it therefore suffices to prove that `G''` is unipotent (2.2). But `G''` is of height
$h - 1$, hence, by induction hypothesis, it suffices to show that `Lie G''` is unipotent. Since iv) ⇒ v), it suffices to
show that $G''_{\bar{k}}$ does not contain any group isomorphic to $\mu_{p}$. Let then a subgroup of $G''_{\bar{k}}$
isomorphic to $\mu_{p}$, $H$ its inverse image in $G_{\bar{k}}$. The group $G'$ being unipotent, we shall prove in § 5
that the extension:

```text
e ⟶ G'_{k̄} ⟶ H ⟶ μ_p ⟶ e
```

is necessarily trivial (the proof given of this fact is independent of the results of the present section). Briefly, the
group $\mu_{p}$ lifts in $H$, but being of height 1 it is necessarily contained in $G'_{\bar{k}} = F G_{\bar{k}}$,
whence a contradiction, $G'$ being unipotent.

### 4.3. Connected affine groups in characteristic $p > 0$

<!-- label: III.XVII.4.3 -->

**Proposition 4.3.1.** *Let $G$ be a connected affine algebraic group over a field $k$ of characteristic $p > 0$. Then
the following conditions are equivalent:*

<!-- label: III.XVII.4.3.1 -->

*i) $G$ is unipotent.*

*ii) $G$ possesses a composition series with successive quotients isomorphic to $\alpha_{p}$ and $G_{a}$ (taken in this
order).*

*iii) $G$ admits a characteristic composition series with successive quotients isomorphic to $(\alpha_{p})^{r}$ and
$(G_{a})^{s}$ (taken in this order).*

*iv) $G_{\bar{k}}$ contains no subgroup isomorphic to $\mu_{p}$.*

*v) $g = Lie G$ is unipotent (3.6).*

<!-- original page 565 -->

*vi) $g$ is nilpotent, and the reductive part of the center of $g$ (4.2.2) is trivial.*

*vi bis) $g$ is nilpotent, and every subgroup of multiplicative type of the identity component of the center of $G$ is
zero.*

*vi ter) $G$ is nilpotent, and every subgroup of multiplicative type of the identity component of the center of $G$ is
zero.*

*Proof.* It is clear that iii) ⇒ ii) ⇒ i). To establish i) ⇒ iii), we shall need the following lemma:

**Lemma 4.3.2.** *Let $k$ be a field of characteristic $p > 0$, $n \in \mathbb{N}$, $k'$ a radicial extension of $k$
such that $(k')^{p^{n}}$ is contained in $k$; for every $k$-prescheme $X$ (resp. every $k'$-prescheme $X'$), denote by
$X^{(p^{n})}$ (resp. $X'^{\phi}$) the $k$-prescheme deduced from $X$ (resp. $X'$) by the base change:*

<!-- label: III.XVII.4.3.2 -->

```text
F^n : k ⟶ k,   x ↦ x^{p^n},   (resp.   φ : k' ⟶ k,   x' ↦ x'^{p^n}).
```

*Then, for every $k$-prescheme $X$, there exists a functorial isomorphism:*

$$
(X_{k'})^{\phi} \xrightarrow{\sim} X^{(p^{n})}.
$$

*Consequently, if $X$ and $Y$ are two $k$-preschemes such that there exists a $k'$-isomorphism
$u' : X_{k'} \xrightarrow{\sim} Y_{k'}$, then there exists a $k$-isomorphism
$v : X^{(p^{n})} \xrightarrow{\sim} Y^{(p^{n})}$. If moreover $X$ and $Y$ are equipped with structures of $k$-preschemes
in groups and if $u'$ is a $k'$-homomorphism, then $v$ is a $k$-homomorphism.*

<!-- original page 566 -->

The lemma follows simply from the transitivity of base changes and from the fact that the composite morphism
$k \to k' \xrightarrow{\phi} k$ is equal to $F^{n}$.

*Continuation of the proof of 4.3.1.*

i) ⇒ iii). Proceed by induction on $\dim G$. If $\dim G = 0$, since $G$ is connected, it is radicial, and one applies
3.9 i). If $\dim G > 0$, there exists an integer $m \geqslant 0$ such that the quotient $G / F_{m} G$ is a smooth group
(App. II 3.1), evidently connected and non-zero. Applying 4.1.1 i) ⇒ iii) to the latter, one sees that there exists an
algebraic subgroup $G'$ of $G$ which is characteristic and connected, and such that the quotient $G'' = G/G'$ is a form
of $G^{r}_{a}$ ($r > 0$). By 4.1.5, if $K$ is a perfect closure of $k$, one has
$G''_{K} \xrightarrow{\sim} (G_{a, K})^{r}$. Since `G''` is of finite type over $k$, there exists a finite radicial
extension $k'$ of $k$ such that $G''_{k'} \xrightarrow{\sim} (G_{a, k'})^{r}$ (Exp. VI_B § 10). Let $n > 0$ be such that
$(k')^{p^{n}} \subset k$. Keeping the notations of 4.3.2, one deduces that there exists a $k$-isomorphism of algebraic
groups:

```text
(G_{a, k})^r = (G_{a, k'})^{rφ} ⥲ (G'')^{(p^n)}.
```

Consider then the Frobenius homomorphism relative to `G''` (Exp. VII_A § 4)

$$
F^{n} : G'' \longrightarrow (G'')^{(p^{n})}.
$$

Since `G''` (and hence also $(G'')^{(p^{n})}$) is smooth over $k$, and $F^{n}$ is radicial, $F^{n}$ is an epimorphism
for the fpqc topology, so that $(G'')^{(p^{n})}$ is identified with $G''/ F_{n}(G'')$. Finally we have shown that
$G''/ F_{n}(G'')$ is isomorphic, as an algebraic group, to $(G_{a})^{r}$.

<!-- original page 567 -->

The inverse image $G'_{n}$ of $F_{n}(G'')$ in $G$ is a subgroup of $G$, connected, characteristic, of dimension strictly
less than that of $G$, to which we may apply the induction hypothesis.

i) ⇒ iv) by 2.4 i).

iv) ⇒ i). Consider $G$ as an extension of a smooth connected group `G''` by a radicial group $G'$ (App. II 3.1). The
group $G'$ is unipotent (4.2.1 iv) ⇔ i)). It suffices to see that `G''` is unipotent, and for that it suffices to show
that $G''_{\bar{k}}$ does not contain a subgroup isomorphic to $\mu_{p}$ (4.1.1 i) ⇔ iv)). Now if $G''_{\bar{k}}$
contained a subgroup $\mu_{p}$, the latter would lift in $G_{\bar{k}}$, by the result (5.1) — already used — proved in §
5, whence a contradiction with iv).

i) ⇒ v) by 3.7.

v) ⇒ vi). Indeed, since $(ad X)^{p^{r}} = ad(X^{(p^{r})})$ (VII_A, 5.2), `ad X` is nilpotent if $g$ is unipotent, hence
$g$ is nilpotent by Engel's theorem (Bourbaki, *Groupes et algèbres de Lie*, Chap. I § 4). On the other hand, if $g$ is
unipotent, evidently so is its center, whose reductive part is then trivial (4.2.2).

vi) ⇒ iv). Indeed, if $G_{\bar{k}}$ contains a subgroup isomorphic to $\mu_{p}$, there exists a non-zero element $X$ of
its Lie algebra such that $X^{(p)} = X$ (App. II 2.1), hence $X^{(p^{r})} = X$ for every $r > 0$. Since `ad X` is
nilpotent (because $g$ is nilpotent and $(ad X)^{p^{r}} = ad X^{(p^{r})}$), necessarily $ad X = 0$, so $X$ belongs to
the reductive part of the center of $g_{\bar{k}}$, whence a contradiction with vi).

i) ⇒ vi ter) follows from 2.4 i) and from 3.5 i) ⇒ iii).

<!-- original page 568 -->

vi ter) ⇒ vi bis). Indeed, if $G$ is nilpotent, so is its subgroup `F G`. It also follows from App. II 2.2 that `F G` is
nilpotent if and only if $Lie F G = Lie G$ (Exp. VII_A) is nilpotent.

vi bis) ⇒ vi). Let $Z$ be the identity component of the center of $G$, and let $r$ be the reductive component of the
center of $g$. We must show that $r = 0$. Now it is immediate that $r$ is a characteristic sub-$p$-Lie algebra of
$g = Lie F G$ (i.e. stable under the functor $\operatorname{Aut}_{p-Lie}(g)$); hence $r$ is the Lie algebra of a
characteristic radicial subgroup $R$ of `F G` (App. II 2.2). On the other hand, it follows from the last assertion of
4.2.2 and from App. II 2.1 that $R$ is a form of $(\mu_{p})^{r}$. The group $R$ being characteristic in `F G`, which is
itself a characteristic subgroup of $G$ (App. II 1), $R$ is *a fortiori* invariant in $G$, hence is central, $G$ being
connected (Exp. IX, 5.5). Hence by hypothesis vi bis), $R$ is zero, and so therefore is $r$.

### 4.4. Étale groups

<!-- label: III.XVII.4.4 -->

The following proposition is an easy consequence of Sylow's theorems and of the structure of finite $q$-groups (cf.
J.-P. Serre, *Corps locaux*, Chap. IX § 1).

**Proposition 4.4.1.** *Let $G$ be a finite étale algebraic group defined over an algebraically closed field $k$. Then
in order that $G$ be unipotent, it is necessary and sufficient that for every prime number $q$ distinct from the
characteristic $p$ of $k$, $G$ does not contain a subgroup isomorphic to $\mu_{q}$.*

<!-- label: III.XVII.4.4.1 -->

### 4.5. Abelian varieties

<!-- label: III.XVII.4.5 -->

<!-- original page 569 -->

Let $G$ be an abelian variety defined over an algebraically closed field $k$. Then the following conditions are
equivalent:

i) $G$ is unipotent.

ii) $G = 0$.

iii) There exists an integer $n$, prime to the characteristic $p$ of $k$, such that $G$ does not contain a subgroup
isomorphic to $\mu_{n}$.

Indeed, if $G$ is an abelian variety of dimension $d$, one knows (cf. S. Lang, *Abelian varieties*, Chap. IV § 3 th. 6)
that the group ${}_{n} G(k)$ ($n$ an integer prime to $p$) is isomorphic to $(\mathbb{Z}/n\mathbb{Z})^{2d}$, hence is
isomorphic to $(\mu_{n})^{2d}$. Whence iii) ⇒ ii), and ii) ⇒ i) ⇒ iii) are obvious.

### 4.6. General case

<!-- label: III.XVII.4.6 -->

If $G$ and $H$ are two algebraic groups defined over an algebraically closed field $k$, we shall denote by $P(G, H)$ the
property: "there is no algebraic subgroup of $G$ isomorphic to $H$". One then obtains the following characterizations of
unipotent groups:

**Theorem 4.6.1.** *Let $G$ be an algebraic group defined over an algebraically closed field $k$ of characteristic $p$.
Then:*

<!-- label: III.XVII.4.6.1 -->

*i) If $G$ is smooth, affine, and connected:*

```text
G is unipotent ⇐⇒ ∃ n > 1 such that P(G, μ_n) is true ⇐⇒ P(G, G_m) is true.
```

*ii) If $G$ is smooth and connected:*

```text
G is unipotent ⇐⇒ ∃ n prime to p such that P(G, μ_n) is true.
```

<!-- original page 570 -->

*iii) If $G$ is smooth:*

```text
G is unipotent ⇐⇒ for every prime number n ≠ p, P(G, μ_n) is true.
```

*iv) $G$ affine connected and $p > 0$:* $G$ *unipotent ⇐⇒ $P(G, \mu_{p})$ is true.*

*v) $G$ connected and $p > 0$:*

```text
G unipotent ⇐⇒ ∃ n prime to p such that P(G, μ_n) is true and P(G, μ_p) is true.
```

*vi) $G$ an arbitrary algebraic group:*

```text
G is unipotent ⇐⇒ for every prime number n, P(G, μ_n) is true.
```

*Proof.* i) follows from 4.1.1, and iv) from 4.3.1. We shall prove vi); ii), iii), v) are proved analogously and are
left to the reader.

Let then $G$ be an algebraic group. If $G$ is unipotent, $P(G, \mu_{n})$ is true for every $n > 1$ (2.4 i)). Conversely,
suppose $P(G, \mu_{n})$ is true for every prime number $n$, and let us show that $G$ is unipotent. Let $G^{0}$ be the
identity component of $G$. If $G^{0}$ is smooth, it follows from a classical theorem of Chevalley[^XVII-4-2] that
$G^{0}$ is an extension of an abelian variety $A$ by an affine, connected, smooth group $L$. If $G$ is not smooth, which
presupposes $p > 0$ (Exp. VI_B, 1.6.1), there exists an integer $n > 0$ such that $G'' = G^{0} / F_{n}(G)$ is smooth
(App. II 3.1). Then `G''` is an extension of an abelian variety $A$ by a smooth connected linear group `L''`. Denote by
$L$ the inverse image of `L''` in $G^{0}$, which is still affine and connected, since $F_{n}(G)$ is radicial. In all
cases, $G$ therefore possesses a composition series:

<!-- original page 571 -->

$$
0 \subset L \subset G^{0} \subset G
$$

such that $L$ is affine and connected, $G^{0}/L = A$ is an abelian variety, and $G/G^{0}$ an étale group.

If $P(G, \mu_{n})$ is true, *a fortiori* $P(L, \mu_{n})$ is true, hence $L$ is unipotent (4.1.1 and 4.3.1). If $A$ is
non-zero, there exists a prime number $n$ and a subgroup of $A$ isomorphic to $\mu_{n}$ (4.5); by 5.1 below, this
subgroup lifts in $G$, which contradicts the hypothesis $P(G, \mu_{n})$; hence $A = 0$. Finally if $G/G^{0}$ is not
unipotent, there exists an integer $q$ and a subgroup of $G/G^{0}$ isomorphic to $\mu_{q}$ (4.4.1). One deduces as above
that $P(G, \mu_{q})$ is not true; hence $G/G^{0}$ is unipotent, and consequently so is $G$.

## 5. Extension of a group of multiplicative type by a unipotent group

<!-- label: III.XVII.5 -->

<!-- original page 572 -->

### 5.1. Statement of the theorem

<!-- label: III.XVII.5.1 -->

**Definition 5.1.0.** *Let $k$ be a field, $G$ a $k$-algebraic group. Following the terminology introduced by Rosenlicht
(Questions of rationality for solvable algebraic groups over non perfect fields, Annali di Math. 61 (1963)), we shall
say that $G$ is "$k$-solvable" if it satisfies the following equivalent conditions:*

<!-- label: III.XVII.5.1.0 -->

*i) $G$ possesses a composition series with successive quotients isomorphic to $G_{a}$.*

*ii) $G$ possesses a characteristic composition series $(G_{i})$ such that the successive quotients $G_{i} / G_{i+1}$
are commutative and possess a composition series with successive quotients isomorphic to $G_{a}$.*

The fact that i) ⇒ ii) is proved in *loc. cit.* In fact, one may take as composition series $(G_{i})$ the composition
series introduced in the proof of 3.9 ii).

**Theorem 5.1.1.** *Let $k$ be a field, $U$ a unipotent $k$-algebraic group, $H$ a $k$-group of multiplicative type, $E$
a $k$-algebraic group extension of $H$ by $U$, so that one has the exact sequence:*

<!-- label: III.XVII.5.1.1 -->

$$
1 \longrightarrow U \longrightarrow E \longrightarrow H \longrightarrow 1.
$$

*Then:*

<!-- original page 573-574 -->

*i) The extension $E$ is trivial in each of the following cases:*

*a) $k$ is algebraically closed.*

*b) $k$ is perfect and one of the groups $U$ or $H$ is connected.*

*c) $U$ is $k$-solvable.*

*d) $U$ is smooth and $H$ is connected.*

*ii) If $H'$ and `H''` are two lifts of $H$ in $E$, then $H'$ and `H''` are conjugate by an element of $U(k)$ in each of
the following cases:*

*a) $k$ is algebraically closed and $H$ is smooth.*

*b) $k$ is algebraically closed and $U$ is smooth.*

(We shall indicate in the course of the proof other cases where the conclusion of ii) is true without assuming $k$
algebraically closed.)

If $U$ is an algebraic group (resp. a commutative algebraic group) defined over a field $k$, we denote by $H^{1}(k, U)$
(resp. $H^{i}(k, U)$, $i \geqslant 0$) the pointed set (resp. the $i$-th group) of Galois cohomology of $k$ with values
in $U$ (cf. J.-P. Serre, *Cohomologie Galoisienne*, Lecture Notes Maths. n° 5, Springer).

<!-- original page 575 -->

If $S$ is a prescheme, $H$ an $S$-prescheme in commutative groups, $G$ an $S$-prescheme in groups acting on $H$, we
denote by $H^{i}(G, H)$[^N.D.E-XVII-7] the $i$-th Hochschild cohomology group of $G$ with values in $H$ (App. I 1).

To prove 5.1.1, we shall proceed in several steps.

### 5.2. Proof of 5.1.1 i) and ii) in the case $U$ smooth and $H$ étale

<!-- label: III.XVII.5.2 -->

**Lemma 5.2.1.** *With the notations of 5.1.1, if $H$ is étale, the canonical morphism $E \to H$ possesses a section
$s : H \to E$, defined over $k$, in the following cases:*

<!-- label: III.XVII.5.2.1 -->

*a) $k$ is algebraically closed.*

*b) $k$ is perfect and $U$ is smooth and connected.*

*c) $U$ is "$k$-solvable".*

a) follows simply from the fact that $E(k) \to H(k)$ is surjective. One has b) ⇒ c) by 4.1.2 b) and 2.3 bis. It
therefore suffices to treat case c). Let $x$ be a point of $H$; $x$ is both an open and closed part of $H$, and the
induced subscheme is isomorphic to $\operatorname{Spec} K$, where $K$ is a finite separable extension of $k$. Let $X$ be
the inverse image in $E$ of the scheme $x$. The $K$-scheme $X$ is a principal homogeneous $K$-space under the group
`U_K`. But `U_K` possesses a composition series with successive quotients isomorphic to $(G_{a})_{K}$, hence
$H^{1}(K, U_{K}) = 0$ (J.-P. Serre, *Cohomologie Galoisienne*, Chap. III, prop. 6), and consequently $X$ is trivial,
hence has a $K$-rational point. One thus obtains a $k$-section of $E \to H$ over $x$, for every point $x$ of $H$, whence
the existence of a section $H \to E$.

**Lemma 5.2.3.**[^N.D.E-XVII-8] *With the notations of 5.1.1, suppose $H$ étale. Then:*

<!-- label: III.XVII.5.2.3 -->

*i) The extension $E$ is trivial in each of the following cases:*

*a) $U$ is commutative and $E \to H$ possesses a section.*

<!-- original page 576 -->

*b) $k$ is algebraically closed.*

*c) $k$ is perfect and $U$ is connected.*

*d) $U$ is "$k$-solvable".*

*Moreover, in each of the above cases, two lifts $H'$ and `H''` of $H$ in $E$ are conjugate by an element of $U(k)$.*

*ii) Let $R$ be the $k$-functor $(Sch/k)^{\circ} \to (Ens)$ such that, for every $k$-prescheme $S$, $R(S)$ is the set of
lifts of `H_S` in `E_S`. Then if $U$ is commutative, $R$ is representable by a non-empty affine $k$-scheme. The group
$U$ acts by inner automorphisms on $R$, and this action makes $R$ into a homogeneous space under $U$ (for the fpqc
topology (cf. Exp. IV)).*

*Proof of i)*. We shall reduce cases b), c), and d) to case a).

*Case b)* Since $U$ possesses a characteristic composition series with successive commutative quotients (3.5 i) ⇔ iv)),
one immediately reduces to the case where $U$ is commutative. Moreover $E \to H$ possesses a section by 5.2.1 a), and we
are reduced to case a).

*Case d)* One proceeds similarly using 5.1.0 ii) and 5.2.1 c).

*Case c)* Let $E_{red}$ be the reduced subgroup associated with $E$. Since $H$ is smooth, $E_{red}$ is an extension of
$H$ by $U_{0} = U \cap E_{red}$, and one may replace $E$ by $E_{red}$. But $U$, and therefore also `U_0`, is connected,
and it is clear that `U_0` is the identity component of $E_{red}$, hence is smooth. But then `U_0` is smooth and
connected, $k$ is perfect, hence `U_0` is $k$-solvable (4.1.4 b)) and we are reduced to case d).

<!-- original page 577 -->

The preceding reductions show that in cases b), c), and d) one may suppose that $U$ possesses a characteristic
composition series $(U_{i})$ such that $U_{i} / U_{i+1}$ is commutative and such that the maps
$U_{i}(k) \to (U_{i} / U_{i+1})(k)$ are surjective (in cases c) and d), this last point comes from
$H^{1}(k, G_{a}) = 0$). An immediate dévissage then shows that it suffices to prove the conjugacy of two lifts $H'$ and
`H''` in $E$ when $U$ is commutative. In short, it suffices to prove i) a). In this case, the triviality of the
extension $E$ is ensured if $H^{2}(H, U) = 0$ (App. I 3.1), and the conjugacy of $H'$ and `H''` if $H^{1}(H, U) = 0$.
Now we have the following lemma:

**Lemma 5.2.4.** *Let $S$ be a prescheme, $U$ an $S$-prescheme in commutative groups, $H$ an $S$-prescheme in groups,
étale, finite, of rank $n$, acting on $U$. Then the groups $H^{i}(H, U)$ ($i > 0$) are annihilated by $n$ in the
following two cases:*

<!-- label: III.XVII.5.2.4 -->

*a) $H$ is a constant $S$-group (Exp. I 4.1).*

*b) $S$ is the spectrum of a field.*

*Proof of a)*. The group $H$ is by hypothesis the constant group associated with an ordinary group ${H}$ of order $n$.
It is clear[^N.D.E-XVII-9] that $H^{i}(H, U)$ is isomorphic to the $i$-th cohomology group $H^{i}({H}, U(S))$ of the
group ${H}$, with values in the ordinary group $U(S)$, and it is classical that these groups are annihilated by $n$
(J.-P. Serre, *Corps locaux*, Chap. VIII, prop. 4 cor. 1).

*Proof of b)*. Let $x \in H^{i}(H, U)$ ($i > 0$), which one represents by an $i$-cocycle $f : H^{(i)} \to U$

<!-- original page 578 -->

(where $H^{(i)}$ denotes the product, over $k$, of $i$ copies of $H$). If $K$ is a finite Galois extension of $k$ that
decomposes $H$, it follows from a) that $nf_{K}$ is a coboundary. More precisely, an easy computation shows that if one
defines the $K$-morphism $F_{K} : H^{(i-1)}_{K} \to U_{K}$ by the formula:

```text
F_K(h_1, …, h_{i−1}) = Σ_{h ∈ H(K)} f_K(h_1, …, h_{i−1}, h),
```

one has, up to sign:

```text
d(F_K) = n f_K   (d coboundary operator).
```

Now an immediate Galois argument shows that `F_K` comes from a $k$-morphism $F : H^{(i-1)} \to U$, and consequently one
has $d(F) = nf$.

**Corollary 5.2.4 bis.** *With the notations of 5.2.4, suppose moreover that $U$ is flat and of finite presentation over
$S$, with unipotent fibers, and that $n$ is prime to the residue characteristics of $S$. Then, in cases a) and b) above,
one has $H^{i}(H, U) = 0$ for $i > 0$.*

<!-- label: III.XVII.5.2.4bis -->

It suffices to show that raising to the $n$-th power in $U$ is an isomorphism, since this will entail that
multiplication by $n$ in $H^{i}(H, U)$ is both an isomorphism and the zero morphism, hence $H^{i}(H, U) = 0$. Now, under
the hypotheses on $U$, it suffices to verify that raising to the $n$-th power is an isomorphism on the fibers of $U$
(EGA IV 17.9.5), which reduces us to the case where $S$ is the spectrum of a field $k$ of characteristic $p$. Since
$(n, p) = 1$, raising to the $n$-th power in $U$ is an étale morphism (Exp. VII), and is a monomorphism (2.4 i)), hence
an open immersion (EGA IV 17.9.1).

<!-- original page 579 -->

This already proves that the restriction to the identity component $U^{0}$ is an isomorphism; since $U/U^{0}$ is a
finite $p$-group, we are done.

This finishes the proof of 5.2.3 i) a), since $H$, being an étale group of multiplicative type, is of order prime to
$p$.

*Proof of 5.2.3 ii)*. It is clear that $R$ is a sheaf for the fpqc topology. Moreover, taking the descent of affine
schemes into account, the assertions of 5.2.3 ii) are local for the fpqc topology. We may therefore suppose $k$
algebraically closed. The group $H$ is then decomposed and the extension $E$ is trivial (i b)); let `H_0` be a lift of
$H$ in $E$. For every $k$-prescheme $S$, and every lift `H''` of `H_S` in `E_S`, $H_{0,S}$ and `H''` are conjugate by an
element of $U(S)$, since $H^{1}(H_{S}, U_{S}) = 0$ (5.2.4 bis). Let then $U^{H_{0}}$ be the sheaf of invariants of $U$
under `H_0`, which is representable by an algebraic subgroup of $U$ (Exp. VIII 6.5 d)). It follows from the preceding
remarks that the $k$-morphism:

```text
U ⟶ R,   u ↦ int(u) H_0   (u ∈ U(S))
```

defines a $k$-isomorphism $U / U^{H_{0}} \xrightarrow{\sim} R$. This proves the representability of $R$ and the fact
that $R$ is affine (2.1).

**Remark 5.2.5.** *One can show that the assertions of 5.2.3 ii) remain true when $U$ is not commutative, but we shall
not need this to prove 5.1.1.*

<!-- label: III.XVII.5.2.5 -->

<!-- original page 580 -->

### 5.3. Study of the case $H$ smooth

<!-- label: III.XVII.5.3 -->

**Proposition 5.3.1.** *The assertions contained in 5.2.3 i) remain true when one replaces the hypothesis "$H$ étale" by
"$H$ smooth".*

<!-- label: III.XVII.5.3.1 -->

Proceeding as in the proof of 5.2.3 i), one reduces to the case where moreover $U$ is commutative.

Let `N_0` be the set of integers `> 0` prime to $p$, ordered by divisibility. For every $n \in N_{0}$, ${}_{n} H$ is an
étale group and the family of ${}_{n} H$ ($n \in N_{0}$) is schematically dense in $H$, since $H$ is smooth (Exp. IX,
4.10). Denote by $E_{n}$ the inverse image of ${}_{n} H$ in $E$, so that $E_{n}$ is an extension of ${}_{n} H$ by $U$,
and finally let $R_{n}$ be the $k$-functor of lifts of ${}_{n} H$ in $E_{n}$ (cf. 5.2.3 ii)). If $n$ divides $m$, it is
clear that one has a natural $k$-morphism $R_{m} \to R_{n}$, so the $R_{n}$ form an inverse system of $k$-functors.
Since $R_{n}$ is representable by a non-empty affine $k$-scheme (5.2.3 ii)), and since a filtered direct limit of
non-zero rings is non-zero, the functor $R = \lim R_{n}$ is representable by a non-empty affine $k$-scheme (EGA IV 8 and
1.9.1). There therefore exists an extension $K$ of $k$ and a point $u \in R(K)$. The image $u_{n}$ of $u$ in $R_{n}(K)$
corresponds to a lift $H'_{n}$ of $({}_{n} H)_{K}$ in $(E_{n})_{K}$. By construction, $H'_{n} = {}_{n}(H'_{m})$ if $n$
divides $m$. Set $U_{n} = (U_{K})^{H'_{n}}$. The choice of $H'_{n}$ allows one to identify $(R_{n})_{K}$ with
$U_{K} / U_{n}$. But the family of $H'_{n}$ is filtered increasing, hence the family of $U_{n}$ is filtered decreasing
and consequently is stationary for $n$ large enough (`U_K` is noetherian). It follows that the family of $(R_{n})_{K}$
is stationary, and consequently so is the family of $R_{n}$.

<!-- original page 581 -->

In brief, one has $R_{n} = R$ for $n$ large enough.

Under the hypotheses made, it follows from 5.2.3 i) that $R_{n}(k)$ is non-empty. One can therefore find a coherent
system of lifts $H'_{n}$ of ${}_{n} H$ for $n \in N_{0}$. Denote by $H'$ the smallest closed subscheme of $E$ majorizing
$H'_{n}$ for every $n$ (Exp. VI_B § 7). The argument made in Exp. XV 4.6 shows that $H'$ is a smooth commutative
algebraic group whose formation commutes with base field extension. To show that $H'$ is a lift of $H$ in $E$, we may
therefore suppose $k$ algebraically closed. By *Bible* 4 th. 4, $H'$ is then the direct product of a (smooth) group of
multiplicative type $M$ and a unipotent group $V$. The groups $H'_{n}$ are then necessarily contained in $M$ (2.4) and
in view of the definition of $H'$ this entails $H' = M$. So $H'$ is of multiplicative type and consequently
$H' \cap U = 0$. The morphism $H' \to H$ is therefore a monomorphism; moreover, it follows from the density theorem
(Exp. IX, 4.10) that it is an epimorphism, hence an isomorphism.

Let now $H'$ and `H''` be two lifts of $H$ in $E$. For every $n \in N_{0}$, denote by
$T_{n} = Transp({}_{n} H', {}_{n} H'')$ the transporter of ${}_{n} H'$ into ${}_{n} H''$, which is representable by a
closed subscheme of $U$ (Exp. VIII 6.5 e)). The $T_{n}$ form a decreasing filtered family of closed subschemes of $U$,
non-empty by 5.2.3 i a). Let $T$ be the stationary value. Under the hypotheses of 5.2.3 i), $T_{n}(k)$ is non-empty.
There therefore exists an element $u$ of $U(k)$ such that ${}_{n} H'' = int(u) {}_{n} H'$ for every $n \in N_{0}$. But
then $H'' = int(u) H'$ (Exp. IX, 4.8 b).

<!-- original page 582 -->

### 5.4. Study of the case $U$ radicial

<!-- label: III.XVII.5.4 -->

**Proposition 5.4.1.** *If $k$ is a perfect field of characteristic $p > 0$, and if $U$ is radicial, the extension $E$
of 5.1.1 is trivial.*

<!-- label: III.XVII.5.4.1 -->

Using a characteristic composition series of $U$, we may limit ourselves to the case where $U$ is equal to
$(\alpha_{p})^{r}$ (3.9).

It follows from App. II 2.2 and 2.1 that one has isomorphisms of $k$-functors:

```text
Aut_{k-gr}(α_p)^r ⥲ Aut_{p-Lie}(Lie(α_p)^r) ⥲ GL(Lie(α_p)^r).
```

Consider then a $k$-vector space $V$ of rank $r$, the $k$-scheme of vector groups $W(V)$ (Exp. I 4.6), and identify
$(\alpha_{p})^{r}$ with `F V`. The preceding remarks then show that the action of $H$ on `F V`, defined by the extension
$E$, comes from a linear representation $v$ of $H$ in $V$. Consider then the exact sequence:

```text
(*)     0 → F V → V ─F→ V^{(p)} → 0,
```

<!-- original page 583 -->

where $F$ is the Frobenius morphism. Then `(*)` is an exact sequence of $H$-groups, provided one makes $H$ act on the
factor $V^{(p)}$ via the linear representation $H \xrightarrow{v} GL(V) \xrightarrow{F} GL(V^{(p)})$.

Since the field $k$ is perfect, the morphism $F : V \to V^{(p)}$ induces a surjective map $V(k) \to V^{(p)}(k)$. It then
follows from App. I 2.1 that the exact sequence `(*)` defines an exact sequence:

```text
(**)    H¹(H, V^{(p)}) ⟶ Ext_{alg}(H, F V) ⟶ Ext_{alg}(H, V).
```

Let us show that $Ext_{alg}(H, V) = 0$. Let then `E_0` be an algebraic group extension of $H$ by $V$:

```text
1 → V → E_0 ─h→ H → 1.
```

The scheme `E_0` is a torsor with base $H$ and group $G^{r}_{a}$, hence defines an element of $H^{1}(H, O^{r}_{H})$ (in
the sense of the cohomology of coherent sheaves). Since $H$ is affine, one has $H^{1}(H, O^{r}_{H}) = 0$ (EGA III § 1).
That is to say, $E_{0} \to H$ possesses a section. Consequently, the group $Ext_{alg}(H, V)$ is isomorphic to
$H^{2}(H, V)$ (App. I 3.1). Now $H^{i}(H, V) = H^{i}(H, W(V)) = 0$ for $i > 0$ (Exp. IX, 3.1). One then concludes, by
the exact sequence `(**)`, that $Ext_{alg}(H, F V) = 0$, hence that $E$ is a trivial extension.

### 5.5. Proof of 5.1.1 i)

<!-- label: III.XVII.5.5 -->

If $k$ is of characteristic 0, $U$ is $k$-solvable (4.1.3) and $H$ is smooth; the fact that $E$ is a trivial extension
therefore follows from 5.3.1 and 5.2.3 d). One proves similarly that two lifts of $H$ in $E$ are conjugate by an element
of $U(k)$.

Henceforth, we therefore suppose that $k$ is a field of characteristic $p > 0$.

*Proof of i) b)*: *Case $k$ perfect, $U$ connected.*

We shall reduce to the case where $U$ is radicial. For this, note that since $k$ is perfect, $H_{red}$ is smooth; let
`E_0` be its inverse image in $E$. It then follows from 5.3.1 and

<!-- original page 584 -->

5.2.3 i) c) that the extension:

$$
1 \longrightarrow U \longrightarrow E_{0} \longrightarrow H_{red} \longrightarrow 1
$$

is trivial. Let `H_1` be a lift of $H_{red}$ in $E$. By App. II 3.1, there exists an integer $n > 0$ such that
$E^{(n)} = E / F_{n}(E)$ is smooth; let `E''` be the algebraic subgroup of $E$ generated by `H_1` and $F_{n}(E)$ (i.e.
the inverse image in $E$ of the image of `H_1` in $E^{(n)}$). Denote by `H''` the image of `E''` in $H$. Then I claim
that $H'' = H$. Indeed, denote by $R$ the image of $F_{n}(E)$ in $H$, so that `H''` is generated by $R$ and $H_{red}$.
The group $H/R$ is a quotient of $E^{(n)}$ hence is smooth; consequently the canonical morphism

$$
H_{red} \longrightarrow H/R
$$

is an epimorphism, so $H$ is generated by $R$ and $H_{red}$, hence equals `H''`. One thus obtains an exact sequence:

```text
(†)      1 ⟶ U'' = U ∩ E'' ⟶ E'' ⟶ H ⟶ 1.
```

But `E''` has the same underlying space as `H_1`, so `U''` is radicial. Moreover, it is clear that it suffices to prove
that the extension (†) is trivial, which follows from 5.4.1.

*Proof of i) b)*: *Case $k$ perfect, $H$ connected.*

The group $U$ is an extension of an étale group by its identity component $U^{0}$. The case $U$ connected having just
been treated, it suffices to examine the case $U$ étale. One then has the more precise lemma:

**Lemma 5.5.1.** *With the notations of 5.1.1, suppose moreover $U$ étale. Then:*

<!-- label: III.XVII.5.5.1 -->

*i) If $H$ is connected, there exists a unique lift of $H$ in $E$, namely the identity component $E^{0}$ of $E$.*

<!-- original page 585 -->

*ii) If $k$ is algebraically closed, $E$ is trivial, and two lifts of $H$ in $E$ are conjugate by an element of $U(k)$.*

i) The formation of the identity component commuting with base field extension, we may limit ourselves to the case $k$
algebraically closed. If $H$ is a torus, $E$ is trivial (5.3.1 and 5.2.3 i b)), and it is clear that $E^{0}$ is the
unique lift of $H$. This already proves that, in the general case, $E^{0} \cap U$ is radicial; since moreover it is
étale ($U$ being étale), it is zero. The morphism $E^{0} \to H$ is therefore a monomorphism, flat (since $E^{0}$ is open
in $E$) and surjective ($H$ is connected), hence an isomorphism. If now $H'$ is another lift of $H$, $H'$ is connected,
hence contained in $E^{0}$, and consequently equal to $E^{0}$.

ii) Let `H_0` be the identity component of $H$. By i), $E^{0}$ is the unique lift of `H_0` in $E$. Set
$E_{0} = E/E^{0}$, $H_{0}' = H/H_{0}$, so that one has the extension:

$$
1 \longrightarrow U \longrightarrow E_{0} \longrightarrow H_{0}' \longrightarrow 1.
$$

$H_{0}'$ being étale, this extension is trivial (5.2.3 i b)). If $H_{1}'$ is a lift of $H_{0}'$ in `E_0`, `H_1` its
inverse image in $E$, it is clear that `H_1` lifts $H$ in $E$. If `H_2` is a second lift of $H$ in $E$, it contains
$E^{0}$; by 5.2.3 i b), the image of `H_2` in `E_0` is conjugate to $H_{1}'$ by an element $u$ of $U(k)$, whence
immediately $H_{2} = int(u) H_{1}$.

**Remark 5.5.2.** *Under the hypotheses of 5.5.1 i), it is easy to see that $E^{0}$ centralizes $U$.*

<!-- label: III.XVII.5.5.2 -->

<!-- original page 586 -->

*Proof of 5.1.1 i) a)*. Using the composition series

$$
1 \longrightarrow U^{0} \longrightarrow U \longrightarrow U/U^{0} \longrightarrow 1,
$$

i) a) follows from the conjunction of i) b) and 5.5.1 ii).

Before proving 5.1.1 c) and d), we shall first establish 5.1.1 ii).

*Proof of 5.5.1 ii) a)*. For lack of a satisfactory general statement, we shall describe a certain number of cases
where, when $H$ is smooth, two lifts of $H$ in $E$ are conjugate:

**Proposition 5.6.1.** *With the notations of 5.1.1, suppose moreover $H$ smooth, and let $H'$ and `H''` be two lifts of
$H$ in $E$. Then $H'$ and `H''` are conjugate by an element of $U(k)$ in each of the following cases:*

<!-- label: III.XVII.5.6.1 -->

*a) $k$ is algebraically closed.*

*b) $U$ is commutative.*

*c) $k$ is perfect and $U$ is connected.*

*d) $U$ is $k$-solvable.*

*e) The centralizer of $H'$ in $U$ is $k$-solvable.*

*f) The group of multiplicative type $H$ is trivialized by a finite Galois extension $K$ of $k$ of degree prime to $p$.*

<!-- original page 587 -->

*Proof.* a), b), c), d) follow from 5.3.1.

e) Let $Z$ be the centralizer of $H'$ in $U$, $T$ the transporter of $H'$ into `H''`. By a), $T$ is non-empty, so $T$ is
a principal homogeneous space under $Z$, and the hypothesis on $Z$ entails that it is trivial.

f) Proceeding as in 5.3.1, one sees that it suffices to consider the case $H$ étale. Suppose first $H$ diagonalizable,
defined by the ordinary group $M$, of order $m$ prime to $p$. The data of the two lifts $H'$ and `H''` defines a
1-cocycle of $M$ with values in $U(\bar{k})$, that is, a map $h$ from $M$ to $U(\bar{k})$ such that
$h(mn) = h(m) \cdot {}}^{m} h(n)$ for every pair `m, n` of elements of $M$. The groups $H'$ and `H''` are conjugate by
an element of $U(k)$ if and only if there exists $a \in U(\bar{k})$ such that

```text
h(m) = a^{−1} ({}^m a).
```

Now the abstract group $U(\bar{k})$ possesses a composition series with successive quotients commutative and annihilated
by a power of $p$ (one may suppose $p > 0$ in view of 5.6.1 c)). One deduces immediately in this case that $h$ is a
coboundary.

Let us now examine the general case. Still denote by $Z$ the centralizer of $H'$ in $U$, and by $T$ the transporter of
$H'$ into `H''`, which is a torsor under $Z$. By hypothesis, there exists a finite Galois extension $K$ of $k$, with
Galois group $G$, of order prime to $p$, that trivializes $H$. By the preceding study, $H'_{K}$ and $H''_{K}$ are
conjugate by an element of $U(K)$,

<!-- original page 588 -->

hence `T_K` is trivial. Consequently $T$ is defined by an element of $H^{1}(G, Z)$. For the same reasons as above, the
hypothesis on $G$ entails that $H^{1}(G, Z) = e$, hence $T$ is trivial.

### 5.7. Proof of 5.1.1 ii) b)

<!-- label: III.XVII.5.7 -->

**Lemma 5.7.1.** *Let $S$ be a prescheme, $G$ an $S$-prescheme in groups, separated and smooth over $S$, $H$ an
$S$-group of multiplicative type acting on $G$. Then the $S$-functor $Z = G^{H}$ of invariants of $G$ under $H$ is
representable by a sub-$S$-prescheme in groups of $G$, closed and smooth over $S$.*

<!-- label: III.XVII.5.7.1 -->

The fact that $G^{H}$ is representable by a closed subprescheme in groups of $G$ follows from Exp. VIII 6.5 d). Consider
then the semidirect product $K = G \times_{S} H$. The centralizer of $H$ in $K$ is then equal to $Z \times_{S} H$. To
prove that $Z$ is smooth, we must verify that if $S$ is affine, $S'$ is a closed subscheme of $S$ defined by a
square-zero ideal, and $u_{0}$ is an element of $Z(S')$, then there exists an element $u$ of $Z(S)$ lifting $u_{0}$. Now
since $G$ is smooth over $S$, there exists an element $u$ of $G(S)$ lifting $u_{0}$. Let $i$ be the canonical immersion
of $H$ into $K$ and consider the two $S$-morphisms of groups

```text
H ⇒ K,   i   and   int(u) i = j.
```

Since $u_{0}$ belongs to $Z(S')$, one has $i_{S'} = j_{S'}$. By Exp. IX, 3.2, there exists $v \in K(S)$

<!-- original page 589 -->

lifting the unit section of $K(S')$, and such that

```text
i = int(v) j = int(vu) i.
```

So $vu = (u', v')$ belongs to $(Z \times_{S} H)(S)$. So $u'$ belongs to $Z(S)$ and lifts $u_{0}$.

**Lemma 5.7.2.** *Let $k$ be a field, $H$ a $k$-algebraic group, and let $P(H)$ be the following property:*

<!-- label: III.XVII.5.7.2 -->

> *"for every smooth unipotent $k$-group $U$, and for every extension $E$ of $H$ by $U$, two lifts of $H$ in $E$ are
> conjugate by an element of $U(k)$".*

*Then if $H$ is an algebraic group extension of a group of multiplicative type `H''` by a group of multiplicative type
$H'$, and if $P(H')$ and $P(H'')$ are true, $P(H)$ is true.*

Indeed, let $U$ be a smooth unipotent $k$-group, $E$ an extension of $H$ by $U$, `H_1` and `H_2` two lifts of $H$ in
$E$, $H_{1}'$ and $H_{2}'$ the corresponding lifts of $H'$. Since $P(H')$ is true, there exists $u \in U(k)$ such that
$H_{2}' = int(u) H_{1}'$. Possibly replacing `H_1` by $int(u) H_{1}$, we may suppose $H_{1}' = H_{2}'$, which we allow
ourselves to denote simply `H_0`. Let $E_{0} = Centr_{E} H_{0}$, which is equal to

```text
U^{H_0} · H_1 = U^{H_0} · H_2.
```

By 5.6.1, $U^{H_{0}} = U_{0}$ is smooth. Consider then the extension

$$
1 \longrightarrow U_{0} \longrightarrow E_{0} \longrightarrow H \longrightarrow 1.
$$

By construction `H_0` is central in `E_0`, hence invariant. By passage to the quotient, one obtains the exact sequence:

$$
1 \longrightarrow U_{0} \longrightarrow E_{0}' \longrightarrow H'' \longrightarrow 1.
$$

Since `U_0` is smooth, and since $P(H'')$ is true, the two images of `H_1` and `H_2`

<!-- original page 590 -->

in $E_{0}'$ are conjugate by an element $u$ of $U_{0}(k)$, but then $H_{1} = int(u) H_{2}$.

To prove 5.1.1 ii) b), note then that, since $k$ is algebraically closed, $H$ possesses a composition series whose
successive quotients are smooth or isomorphic to $\mu_{p}$ when $p > 0$. By repeated use of 5.7.2, we are reduced to the
case where $H$ is smooth or equal to $\mu_{p}$. In the first case, it suffices to apply 5.1.1 ii) a). There remains the
case $H = \mu_{p}$. Since $U$ is smooth, $U$ possesses a characteristic composition series with successive quotients
étale or isomorphic to $(G_{a})^{r}$ (3.9). If $U$ is étale, one applies 5.5.1. There finally remains the case
$H = \mu_{p}$, $U = G^{r}_{a}$.

We must show that $H^{1}(\mu_{p}, U) = 0$. The method used in 5.4.1 no longer applies here, since $\mu_{p}$ does not in
general act linearly on $(G_{a})^{r}$. Let us fix the notations: $H'$ denotes a lift of $H$ in $E$, $e = Lie E$,
$u = Lie U$, $h = Lie H$, $h' = Lie H'$. Let $X$ be a non-zero element of $h$ such that $X^{(p)} = X$ (App. II 3.1), and
let $X'$ be its lift in $h'$.

Since $\mu_{p}$ is a radicial group of height 1, there is a bijective correspondence between the set of lifts of $H$ in
$E$ and the set $A$ of $Y \in e$ such that $Y^{(p)} = Y$ and which project to $X$ (App. II 2.2). Likewise if $Y \in A$
corresponds to the lift `H''` of $H$ in $E$, and if $u \in U(k)$, then $int(u) H' = H''$ if and only if $Ad(u) X = Y$.
Let then $B$ be the subset of $Y \in e$ of the form `Ad(u) X`, where $u \in U(k)$. One has evidently $B \subset A$, and
everything reduces to showing that $A = B$ if $k$ is

<!-- original page 591 -->

algebraically closed.

a) *Study of $A$.* Since $u$ is commutative and normalized by $h$, Jacobson's formula (Exp. VII_A 5.2) gives simply, for
$u \in u$:

```text
(X' + u)^{(p)} = X'^{(p)} + u^{(p)} + (ad X')^{p−1}(u) = X' + (ad X')^{p−1}(u),
```

so that $X' + u \in A \Leftrightarrow u = (ad X')^{p-1}(u)$.

Now let $u = \oplus_{n \in \mathbb{Z}/p\mathbb{Z}} u_{n}$ be the canonical decomposition of $u$ under the action of
$H'$, which one may also write:

```text
u = u_0 ⊕ ⊕_{n ∈ (ℤ/pℤ)^×} u_n.
```

If $u \in u_{0}$, one has $ad X'(u) = 0$. If $u \in u_{n}$ ($n \in (\mathbb{Z}/p\mathbb{Z})^{\times}$), one has
$(ad X')^{p-1}(u) = u$. Finally, $Y = X' + u$ is an element of $A$ if and only if
$u \in \oplus_{n \in (\mathbb{Z}/p\mathbb{Z})^{\times}} u_{n}$. Note that $A$ is the set of $k$-rational points of an
irreducible subscheme of $W(e)$, of dimension equal to $rg u - rg u_{0} = rg u - rg Centr_{u}(X')$.

b) *Study of $B$.* We shall need the following lemma:

**Lemma 5.7.3.** *(Rosenlicht). Let $U$ be a unipotent algebraic group over a field $k$ acting on a quasi-affine
$k$-scheme $X$. Then the orbit of every point $x \in X(k)$ is closed in $X$ (by* orbit *of $x$ we mean the subset of
$ens(X)$ image of $G$ under the morphism $g \mapsto g \cdot x$).*

<!-- label: III.XVII.5.7.3 -->

<!-- original page 592 -->

By functoriality, $G$ acts on the affine envelope of $X$ (that is, $\operatorname{Spec} \Gamma(X, O_{X})$), which allows
us to suppose $X$ affine. One may further suppose $k$ algebraically closed, $X$ reduced, and $U$ smooth (note that
$U_{red}$ acts on $X_{red}$ if $k$ is perfect). Let $Y$ be the schematic image of $G$ (EGA I 9.5.1) under the morphism
$g \mapsto g \cdot x$, which is a closed and reduced subscheme of $X$ on which $G$ acts. It follows easily from EGA IV
1.8.6 that the orbit of $x$ is an open part $Z$ of $Y$, dense in $Y$. We must show that $Z = ens(Y)$. Let $F$ be the
closed reduced subscheme of $Y$ having `Y \ Z` as underlying space. One has therefore $F = V(J)$, where $J$ is a
non-zero ideal of $\Gamma(Y, O_{Y})$. Since $G$ is smooth, $G$ acts on $F$, hence on $J$, and consequently (3.2)
$J^{G} \neq 0$. If $a$ is a non-zero element of $J^{G}$, $a$ is necessarily constant on the orbit $Z$, hence is constant
on $Y$, $Z$ being dense in $Y$. But then the ideal $J$ contains $k$, and $F = \emptyset$.

This being so, let us apply the preceding lemma to the group $U$ acting on the affine space $W(e)$ via the adjoint
representation. One obtains that the orbit of $X'$ is the underlying set of a closed sub-prescheme of $W(e)$. Moreover,
the stabilizer $Z$ of $X'$ is the centralizer of $X'$ in $U$, and one has a closed immersion:

$$
U/Z \longrightarrow W(e).
$$

Let us note that the orbit of $X'$ is the underlying space of a closed subscheme of $W(e)$ of dimension equal to
$\dim U - \dim Z$.

c) *End of the proof of 5.1.1 ii) b)*. When $k$ is algebraically closed, the canonical map $U(k) \to (U/Z)(k)$ is
surjective,

<!-- original page 593 -->

so that by point b) above, $B$ is the set of $k$-rational points of a closed subscheme of $W(e)$ of dimension
$\dim U - \dim Z$. Taking point a) into account, to prove that $A = B$, it then suffices to show that one has:

```text
rg u − rg Centr_u(X') ⩽ dim U − dim Centr_U(X').
```

Now since $U$ is smooth, one has $\dim U = rg u$. On the other hand, one has (Exp. II 5.3.3):

```text
dim Centr_U(X') ⩽ rg Centr_u(X'),
```

whence the result (note that one in fact has `dim Centr_U(X') = rg Centr_u(X')`, which gives another proof that $Z$ is
smooth (5.7.1)).

### 5.8. End of the proof of 5.1.1 i)

<!-- label: III.XVII.5.8 -->

It remains to prove i) c) and i) d).

*Proof of 5.1.1 i) d) ($U$ smooth, $H$ connected)*. We shall need the following lemma:

**Lemma 5.8.1.** *With the notations of 5.1.1, suppose $U$ smooth and $H$ radicial, and let `H_1` be an algebraic
subgroup of $H$ that possesses a lift $H_{1}'$ in $E$. Then $H$ possesses a lift $H'$ in $E$ majorizing $H_{1}'$.*

<!-- label: III.XVII.5.8.1 -->

By induction on the height of $H/H_{1}$, one may suppose $H/H_{1}$ of height 1. Let $C' = Centr_{E}(H_{1}')$. I claim
that the canonical morphism $C' \to H$ is an epimorphism. To establish this point, we may suppose $k$ algebraically
closed; but then, the extension $E$ is trivial (5.1.1 i a)); let `H''` be a lift of $H$ in $E$, $H_{1}''$ the inverse
image of `H_1` in `H''`.

<!-- original page 594 -->

The groups $H_{1}'$ and $H_{1}''$ are two lifts of `H_1` in $E$, hence are conjugate by an element of $U(k)$, since $k$
is algebraically closed and $U$ smooth (5.1.1 ii b)). It is clear then that to prove the assertion on $C'$, it suffices
to prove it for $C'' = Centr_{E}(H_{1}'')$. But in this case, `C''` majorizes `H''`, and the property is clear.
Moreover, it follows from 5.7.1 that $C \cap U$ is smooth. It is clear then that we may replace $E$ by $C$, hence
suppose $H_{1}'$ central. But then, possibly passing to the quotient by $H_{1}'$, we may suppose $H_{1} = 0$ and $H$ of
height 1.

Since $U$ is smooth, one has the exact sequence of $p$-Lie algebras (App. II 3.2):

```text
(*)    0 ⟶ Lie U ⟶ Lie E ⟶ Lie H ⟶ 0.
```

Taking App. II 2.2 into account, saying that $E$ is trivial is equivalent to saying that `(*)` is a trivial extension of
$p$-Lie algebras. Suppose $H \neq 0$ (hence $Lie H \neq 0$) and suppose we have found a non-zero sub-$p$-Lie algebra
$h_{1}$ of $h = Lie H$ that lifts to a sub-$p$-Lie algebra $h_{1}'$ of `Lie E`. By *loc. cit.*, there exists a subgroup
`H_1` of $H$ such that $Lie H_{1} = h_{1}$, and a lift $H_{1}'$ of `H_1` in $E$ such that $Lie H_{1}' = h_{1}'$.
Applying again the reduction described above, one is reduced to the same problem, where one has replaced $H$ by
$H/H_{1}$. Since $H$ is of height 1, `Lie(H/H_1) = Lie H / Lie H_1` (*loc. cit.*), so
$rg Lie(H/H_{1}) \leqslant rg Lie H - 1$. In brief, proceeding by induction on the rank of `Lie H`, one sees that it
suffices, when $h \neq 0$,

<!-- original page 595 -->

to find a non-zero Lie subalgebra of `Lie H` that lifts in `Lie E`. Now we have the following lemma:

**Lemma 5.8.2.** *Let $k$ be a field of characteristic $p > 0$, and $\phi$ a surjective morphism of finite-rank
$p$-$k$-Lie algebras $g \to h$. Then:*

<!-- label: III.XVII.5.8.2 -->

*i) If $h_{\bar{k}}$ is reductive (4.2.2) and $\neq 0$, there exists a reductive Lie subalgebra $h_{1}$ of $g$ whose
image in $h$ is non-zero.*

*ii) If $k$ is perfect and if $u$ is a unipotent element of $h$ (i.e. there exists $n$ such that $u^{(p^{n})} = 0$),
then $u$ lifts to a unipotent element of $g$.*

Take $X$ a non-zero element of $h$ in case i) and $u$ in case ii), and let $X'$ be a lift of $X$ in $g$. The sub-$p$-Lie
algebra of $g$ generated by $X'$ is an abelian $p$-Lie algebra (Exp. VII) $h_{0}$.

*Case i)*. It is clear from the description given in 4.2.2 that the reductive part (*loc. cit.*) of $h_{0, \bar{k}}$ is
already defined over $k$; denote it $r_{0}$. I claim that the image of $r_{0}$ in $h$ is non-zero. To establish this
point we may suppose $k$ algebraically closed, so that $h_{0} = r_{0} \oplus u_{0}$ ($u_{0}$ the unipotent part of
$h_{0}$). If the image of $r_{0}$ in $h$ were zero, the image of $h_{0}$ in $h$ would be unipotent, hence would be zero
since $h$ is reductive (cf. 2.4 ii)); now by construction it contains $X$.

*Case ii)*. One proceeds similarly, exchanging the roles of $r_{0}$ and $u_{0}$.

<!-- original page 596 -->

*End of the proof of 5.8.1*. Supposing $H \neq 0$, by 5.8.2 there exists a non-zero reductive Lie subalgebra $h_{1}'$ of
`Lie E`. Since `Lie U` is unipotent (4.3 i)), one necessarily has $(Lie U) \cap h_{1}' = 0$, so $h_{1}'$ is a lift of a
sub-$p$-Lie algebra of `Lie H`.

*End of the proof of 5.1.1 i d)*. By 5.8.1, there exists a family of algebraic subgroups $H_{n}'$ ($n \in \mathbb{N}$)
of $E$, such that $H_{n+1}'$ majorizes $H_{n}'$ and $H_{n}'$ lifts $F_{n} H$. The decreasing sequence of subgroups
$Centr_{E}(H_{n}')$ is stationary; let $C$ be the stationary value. The center $Z$ of $C$ majorizes $H_{n}'$ for every
$n$, hence the image of $Z$ in $H$ majorizes $F_{n}(H)$ for every $n$, and is consequently an open subgroup of $H$ (Exp.
VII_A § 4), hence is equal to $H$ since $H$ is connected. To prove that $E$ is trivial, we may therefore replace $E$ by
$Z$, hence suppose $E$ commutative. We shall then see in 7.2.1 that $E$ contains a maximal subgroup of multiplicative
type $M$, whose formation commutes with base field extension. Since $E_{\bar{k}}$ is a trivial extension (5.1.1 i) a))
and $U$ is unipotent, it is clear that $M$ is the unique lift of $H$ in $E$.

*Proof of 5.1.1 i) c) ($U$ $k$-solvable)*. Since $(H/H)^{0}(k)$ is of order prime to $p$, it is immediate by duality
that there exists an integer $n$ such that ${}_{n} H$ is an étale subgroup and the canonical morphism
${}_{n} H \to H/H^{0}$ is an epimorphism, so that $H/_{n} H$ is connected. By 5.2.3 d), there exists a lift $H'$ of
${}_{n} H$ in $E$. One shows, as at the beginning of the proof of 5.8.1, that $C = Centr_{E}(H')$

<!-- original page 597 -->

is a subgroup of $E$ such that $C \to H$ is an epimorphism and such that $C \cap U$ is smooth. Replacing $E$ by $C$ and
passing to the quotient by $H'$, one is reduced to the case where $U$ is smooth and $H$ connected, that is, to case i)
d).

This finishes the proof of 5.1.1.

### 5.9. Counterexamples

<!-- label: III.XVII.5.9 -->

Let us first indicate a procedure for obtaining non-trivial extensions of a $k$-group of multiplicative type $H$ by a
unipotent $k$-group $U$. Suppose given an action of $H$ on $U$, and let $E$ be the semidirect product $E = U \cdot H$.
Suppose moreover that one is given an element of $H^{1}(k, U)$ represented by a 1-cocycle $a$. The group $U$ acts by
inner automorphisms on $E$. The datum of $a$ therefore defines a $k$-form of $E$ denoted $E_{a}$. Suppose moreover that
$U$ is commutative; then $U$ acts trivially on $U$ and on the quotient $E/U = H$, so that $E_{a}$ is still an extension
of $H$ by $U$. Suppose, for simplicity, that $H$ is an étale diagonalizable group, so that the Galois group $G$ of
$\bar{k}/k$ acts trivially on $H(\bar{k})$; the action of $G$ on the points of $E_{a}(\bar{k})$ is then given by the
formula:

```text
{}^g (u, h) = ({}^g u + a(g) − {}^h a(g), h)   (g ∈ G, u ∈ U(k̄), h ∈ H(k̄)).
```

If $h$ is a point of $H(k)$, $X$ its inverse image in $E_{a}$, $X$ is therefore a torsor under $U$ defined by the class
of the 1-cocycle of $G$ with values in $U$, $g \mapsto a(g) - {}}^{h} a(g)$. It follows that if there exists a point $h$
of $H(k)$ such that the preceding 1-cocycle is non-trivial,

<!-- original page 598 -->

the extension $E_{a}$ is non-trivial. We shall apply this construction in two particular cases:

a) *Non-trivial extension of an étale diagonalizable group $H$ by $\mathbb{Z}/p\mathbb{Z}$.*

Take for $H$ the group $(\mathbb{Z}/p\mathbb{Z})^{\times}$ acting by multiplication on $U = \mathbb{Z}/p\mathbb{Z}$. Let
$k$ be a field of characteristic $p$, $K$ an extension of $k$ with Galois group $G$ isomorphic to
$\mathbb{Z}/p\mathbb{Z}$, $a$ a non-zero element of $H^{1}(G, U) = \operatorname{Hom}(G, U)$. The group $E_{a}$ then
answers the question.

b) *Example of a non-trivial extension of an étale diagonalizable group $H$ by a smooth connected unipotent group $U$.*

Take for $k$ a non-perfect field such that there exists a $k$-form $U$ of $G_{a}$ with $H^{1}(k, U) \neq 0$. For example
(cf. J.-P. Serre, *Cohomologie Galoisienne*), one may take for $k$ the field of fractions of a discrete valuation ring
of equal characteristic $p > 0$, and for $U$ the algebraic subgroup of $G_{a} \times_{k} G_{a}$ with equation
$X^{p} + X + t Y^{p} = 0$, where $t$ denotes a uniformizer of $k$. Indeed, supposing for simplicity that $k$ contains
the $(p - 1)$-th roots of unity, one has an exact sequence of algebraic groups:

```text
0 ⟶ ℤ/pℤ ⟶ U ⟶ G_a ⟶ 0,   (x, y) ↦ y,
```

hence an exact sequence of cohomology:

<!-- original page 599 -->

```text
G_a(k) ─d→ H¹(k, ℤ/pℤ) → H¹(k, U) → 0,
```

where $d$ sends $x$ to the principal homogeneous space under $\mathbb{Z}/p\mathbb{Z}$ with equation

```text
X^p + X + t x^p = 0.
```

Moreover, one knows that $H^{1}(k, \mathbb{Z}/p\mathbb{Z})$ is isomorphic to $k / P(k)$ (where $P(x) = x^{p} + x$),
hence $H^{1}(k, U)$ is isomorphic to $k / (P(k) + t k^{p})$. Suppose moreover $p \neq 2$; it is then clear that $t^{2}$
is an element of $k$ not belonging to $P(k) + t k^{p}$, hence $H^{1}(k, U) \neq 0$.

On the other hand $\mu_{p-1}$ acts on $U$ by the formula:

```text
(h, x, y) ↦ (hx, hy).
```

Denote by $G$ the Galois group of the extension $K$ defined by the equation

$$
X^{p} + X + t^{2} = 0,
$$

and let $a \in H^{1}(G, U)$ be the non-zero element described above. One verifies immediately that $E_{a}$ is then a
non-trivial extension of $\mu_{p-1}$ by $U$.

c) *Non-trivial extension of $G_{m}$ by $\alpha_{p}$.*

By 5.1.1 i) b), such an extension can only exist over a non-perfect field $k$. Let then $k$ be a non-perfect field, $G$
the semidirect product of $U = G_{a}$ by $H = G_{m}$, with $G_{m}$ acting on $G_{a}$ by homotheties. Since $U$ is
invariant in $G$, so is `F U`. Let $G'' = G / F U$. The group `G''` is isomorphic to $G_{a} \cdot G_{m}$, where $G_{m}$
acts on $G_{a}$ by the formula:

```text
(h, u) ↦ h^p u.
```

<!-- original page 600 -->

The functor `T_G` (resp. $T_{G''}$) of subtori of $G$ (resp. `G''`) (cf. Exp. XV) is isomorphic to $G_{a}$, and the
morphism $T_{G} \to T_{G''}$ deduced from the morphism $G \to G''$ is identified with the morphism $u \mapsto u^{p}$. It
follows that if `T''` is a subtorus of `G''` corresponding to a point $x$ of $k \simeq G_{a}(k)$ such that $x^{1/p}$ is
not in $k$, the inverse image $E$ of `T''` in $G$ will be an extension of a torus `T''` by $F U = \alpha_{p}$, will not
possess maximal tori defined over $k$, hence will not be trivial. One finds for $E$ the subgroup of
$G = \operatorname{Spec} k[U, T, T^{-1}]$ with equation $U^{p} = x - x T^{p}$.

**Remark 5.9.1.** *This last example shows that a non-smooth algebraic group defined over a non-perfect field does not
necessarily possess maximal tori, and thus answers the question raised in Exp. XIV, 1.5 b).*

<!-- label: III.XVII.5.9.1 -->

d) Let us now give an example of a trivial extension $E$ of a group of multiplicative type $H$ by a unipotent group $U$,
and of two lifts $H'$ and `H''` of $H$ that are not conjugate by an element of $U(k)$.

Take for $E$ the semidirect product of $U = G_{a}$ by $\mu_{p} = \operatorname{Spec} k[T] / (T^{p} - 1)$, the action of
$\mu_{p}$ on $G_{a} = \operatorname{Spec} k[U]$ being defined by the comorphism:

```text
U ↦ (U + U^p) T − U^p.
```

The centralizer of $\mu_{p}$ in $U$ is then the étale group $Z$ of equation $U + U^{p} = 0$. It follows that if $k$ is
not algebraically closed, the canonical map $U(k) \to (U/Z)(k)$ is not in general surjective,

<!-- original page 601 -->

hence, taking 5.1.1 ii) b) into account, two lifts of $\mu_{p}$ in $E$ are not necessarily conjugate by an element of
$U(k)$.

Here is another example, with $k$ algebraically closed of characteristic $p > 0$. Let $G$ be the radicial group
semidirect product of $\mu_{p}$ by $\alpha_{p}$, where $\mu_{p}$ acts on $\alpha_{p}$ by "homotheties". One then has an
exact sequence of algebraic groups, with $\mu_{p}$ as operator group:

```text
0 → α_p → G_a → G_a → 0,   x ↦ x^p,
```

where $\mu_{p}$ acts by homotheties on the first term $G_{a}$, and trivially on the second. The exact cohomology
sequence (App. I, prop. 11) furnishes here the exact sequence:

```text
0 ⟶ G_a(k) ⟶ H¹(μ_p, α_p) ⟶ H¹(μ_p, G_a).
```

Since the last term is zero (I 5.3.3), one sees that $H^{1}(\mu_{p}, \alpha_{p})$ is non-zero, hence two lifts of
$\mu_{p}$ in $G$ are not necessarily conjugate.

## 6. Extension of a unipotent group by a group of multiplicative type

<!-- label: III.XVII.6 -->

<!-- original page 602 -->

### 6.1. Statement of the theorem

<!-- label: III.XVII.6.1 -->

**Theorem 6.1.1.** *Let $k$ be a field, $U$ a unipotent $k$-algebraic group, $H$ a $k$-group of multiplicative type, $E$
a $k$-algebraic group extension of $U$ by $H$, so that one has the exact sequence*

<!-- label: III.XVII.6.1.1 -->

$$
1 \longrightarrow H \longrightarrow E \longrightarrow U \longrightarrow 1.
$$

*Then the extension $E$ is trivial and there exists a unique lift of $U$ in $E$ in each of the following cases:*

*A) The group $U$ is smooth and one of the following conditions is satisfied:*

*i) $U$ is connected and the canonical morphism $E \to U$ possesses a section.*

*ii) $U$ possesses a composition series with successive quotients isomorphic to $G_{a}$.*

*iii) $H$ is étale.*

*iv) $k$ is perfect.*

*B) $U = \alpha_{p}$ and $k$ is perfect.*

*C) $E$ is commutative and $k$ is perfect.*

### 6.2. Proof of 6.1.1 A)

<!-- label: III.XVII.6.2 -->

Let us first establish three lemmas.

**Lemma 6.2.1.** *Let $S$ be a prescheme, $E$ an $S$-prescheme in groups, extension of an $S$-prescheme in groups $U$
with connected fibers, by an $S$-group of multiplicative type and of finite type $H$ (i.e. $U$ is the quotient of $E$ by
$H$ for the fpqc topology). Then $E$ is a central extension.*

<!-- label: III.XVII.6.2.1 -->

<!-- original page 603 -->

Indeed, since $H$ is commutative, the group $U$ acts by inner automorphisms on $H$, via an $S$-morphism of groups

$$
u : U \longrightarrow \operatorname{Aut}_{S-gr}(H).
$$

The functor $\operatorname{Aut}_{S-gr}(H)$ is representable by an étale $S$-scheme (Exp. X 5.10), and consequently the
unit section is both an open and closed immersion. Since $U$ has connected fibers, one deduces that $u$ is the unit
morphism.

**Lemma 6.2.2.** *With the notations of 6.1.1, if $E$ is trivial, there exists a unique lift of $U$ in $E$.*

<!-- label: III.XVII.6.2.2 -->

Let $U'$ and `U''` be two lifts of $U$ in $E$. To show that $U' = U''$, we may suppose $k$ algebraically closed, and it
suffices to show that $H^{1}(U, H) = 0$. If $U$ is connected, $U$ centralizes $H$ (6.2.1), hence

```text
H¹(U, H) = Hom_{k-gr}(U, H) = 0
```

by 2.4 ii). In the general case, denote by $U_{1}'$ the unique lift in $E$ of the connected component `U_0` of $U$, and
let $N = Norm_{E}(U_{1}')$. If $g \in E(k)$, $int(g) U_{1}'$ is a lift of `U_0`, hence is equal to $U_{1}'$, and
consequently $N(k) \supset E(k)$. Moreover, $N$ majorizes $H$ (6.2.1) and $U_{1}'$, whence immediately the fact that
$N = E$. Passing to the quotient by $U_{1}'$,

<!-- original page 604 -->

one is reduced to the case where $U$ is étale. In this case, $k$ being algebraically closed, $H^{1}(U, H)$ is identified
with the ordinary cohomology group $H^{1}(U(k), H(k))$[^N.D.E-XVII-10], and consequently is zero, since $U(k)$ is a
finite $p$-group and $H(k)$ is uniquely $p$-divisible.

**Corollary 6.2.3.** *To prove that $E$ is trivial, it suffices to show that $E$ becomes trivial after a finite
separable extension of the base field; in particular, one may suppose $H$ diagonalizable.*

<!-- label: III.XVII.6.2.3 -->

**Lemma 6.2.4.** *For every central extension $E$ of $U$ by a diagonalizable $k$-group $H$ to be trivial, it suffices
that every central extension of $U$ by $G_{m}$ be trivial.*

<!-- label: III.XVII.6.2.4 -->

Indeed, by induction on $r$, one notes first that the hypothesis entails that $E$ is trivial if $H = G^{r}_{m}$. In the
general case, $H$ embeds in $G^{r}_{m}$ for a suitable integer $r$ (this is immediate by duality); let
$H'' = G^{r}_{m} / H$. One obtains the exact sequence (App. I 2.1):

```text
Z¹(U, H'') ⟶ Ext_{alg}(U, H) ⟶ Ext_{alg}(U, G_m^r) = 0
```

(where $U$ acts trivially on $H$, `H''`, $G^{r}_{m}$). But $Z^{1}(U, H'') = \operatorname{Hom}_{k-gr}(U, H'') = 0$ (2.4
ii)), hence $Ext_{alg}(U, H) = 0$.

*Proof of 6.1.1 A) i)*. Since $E \to U$ possesses a section, $E$ defines an element $f$ of $H^{2}(U, H)$ (App. I 3.1).
We must show that $f$ is zero, and for this, it suffices to show that a 2-cocycle $f : U \times_{k} U \to H$ is a
constant morphism, which will follow from the following lemma:

<!-- original page 605 -->

**Lemma 6.2.5.** *Let $U$ be a smooth connected unipotent $k$-algebraic group, $H$ a $k$-group of multiplicative type;
then every $k$-morphism (of preschemes)*

<!-- label: III.XVII.6.2.5 -->

$$
f : U \longrightarrow H
$$

*is constant.*

To prove this lemma, we may suppose $k$ algebraically closed. We proceed by increasing induction on $\dim U$. If
$\dim U > 0$, $U$ possesses a composition series (cf. 3.9):

```text
1 → U' → U ─π→ U'' → 1
```

with $U' \simeq G_{a}$ and $\dim U'' < \dim U$. It suffices to show that $f$ factors through `U''`. Since the graph of
the equivalence relation defined by $\pi$ is smooth over $k$, hence reduced, it suffices to show that if $x, y \in U(k)$
have the same image $z$ in `U''(k)`, then $f(x) = f(y)$. Now $\pi^{-1}(z)$ is isomorphic to $G_{a}$, hence the
restriction of $f$ to $\pi^{-1}(z)$ factors through a reduced irreducible component of $H$, hence through a $k$-scheme
isomorphic to $(G_{m})^{r}$. It then suffices to note that every morphism from $G_{a}$ into $(G_{m})^{r}$ is constant,
since every invertible regular function on $G_{a}$ is constant.

*Proof of 6.1.1 A) ii)*. Thanks to 6.2.1, 6.2.3, and 6.2.4, we may suppose that $H = G_{m}$. By hypothesis, $U$
possesses a composition series $U \supset U_{1} \supset \cdots$ such that $U_{i} / U_{i+1}$ is isomorphic to $G_{a}$.
Let `E_1` be the inverse image of `U_1` in $E$. By induction on $\dim U$, one may suppose the extension `E_1` is
trivial; let $U_{1}'$ be the unique

<!-- original page 606 -->

lift of `U_1`. Proceeding as in the proof of 6.2.4, one shows that $U_{1}'$ is invariant in $E$. After passing to the
quotient by $U_{1}'$, one is reduced to the case where $U = G_{a}$. The $S$-scheme $E$ (where $S = U$) is then a torsor
under the $S$-group $G_{m} \times_{k} S$, hence possesses a section, since $\operatorname{Pic}(S) = 0$ (Exp. VIII 4.3).
The extension $E$ is then trivial by A) i).

*Proof of 6.1.1 A) iii) ($U$ smooth, $H$ étale)*. Suppose first $U$ connected. The group $U_{\bar{k}}$ then possesses a
composition series with successive quotients isomorphic to $G_{a}$, hence $E_{\bar{k}}$ is trivial by A) ii). Since $H$
is étale, it is clear that the unique lift of $U_{\bar{k}}$ in $E_{\bar{k}}$ is the connected component of
$E_{\bar{k}}$, hence this lift is already defined over $k$. In the general case, possibly passing to the quotient by the
connected component of $E$, one is reduced to the case where $E$ is étale, then to the case where $E$ is completely
decomposed (6.2.3). Since $U(k)$ is a $p$-group and $H(k)$ is of order prime to $p$, one may take as a lift of $U(k)$
the Sylow $p$-subgroup of $E(k)$.

*Proof of 6.1.1 A) iv) ($U$ smooth, $k$ perfect)*. If $U$ is connected, $U$ possesses a composition series with
successive quotients isomorphic to $G_{a}$ (4.1.2 b)), and one applies A) ii). In the general case, what precedes allows
us to reduce to the case where $U$ is étale, then to the case where $U$ is completely decomposed and $H$ diagonalizable
(6.2.3). Using now a characteristic composition series of $H$ ($H \supset H^{0} \supset F_{n}(H) \supset 0$), one
reduces to the case where $H$ is of one of the three following types:

<!-- original page 607 -->

a) $H$ is étale.

b) $H = G^{r}_{m}$.

c) $H$ is radicial.

In case a), one applies A) iii); in case c), one applies 1.6. Finally in case b), one notes that by Hilbert's Theorem
90, $E \to U$ possesses a section, so that it suffices to show that
$H^{2}(U, G^{r}_{m}) = H^{2}(U(k), G^{r}_{m}(k)) = 0$. Now $U(k)$ is a finite $p$-group, while $G^{r}_{m}(k)$ is
uniquely $p$-divisible (since $k$ is perfect).

### 6.3. Proof of 6.1.1 B) and C)

<!-- label: III.XVII.6.3 -->

Thanks to 6.2.1, 6.2.3, 6.2.4, one sees that it suffices to prove B) when $H = G_{m}$. One therefore has an exact
sequence:

$$
1 \longrightarrow G_{m} \longrightarrow E \longrightarrow \alpha_{p} \longrightarrow 1.
$$

Since $G_{m}$ is smooth, one deduces an exact sequence of $p$-Lie algebras (App. II 3.2):

```text
(*)    0 ⟶ Lie G_m ⟶ Lie E ⟶ Lie α_p ⟶ 0.
```

The group $\alpha_{p}$ being of height 1, the extension $E$ is trivial if and only if (App. II 2.2) the exact sequence
`(*)` of $p$-Lie algebras is split. One knows that $Lie \alpha_{p}$ is generated by an element $X \neq 0$ such that
$X^{(p)} = 0$ (App. II 2.1); it therefore suffices to show that $X$ lifts to an element $Z$ of `Lie E` such that
$Z^{(p)} = 0$. Now by 5.8.2 ii), there exists a unipotent element $Z$ of `Lie E` lifting $X$. Since the unipotent part
of `Lie E` is clearly at most of dimension 1, one necessarily has $Z^{(p)} = 0$.

*Proof of 6.1.1 C)*. If $U_{1}'$ is a lift in $E$ of an algebraic subgroup `U_1` of $U$, $U_{1}'$ is invariant in $E$,
since $E$ is supposed commutative, and we may pass to the quotient by $U_{1}'$. Using a composition series of $U$ (3.5
ii)),

<!-- original page 608 -->

the preceding remark allows us to reduce to the case where $U$ is smooth or equal to $\alpha_{p}$. But then $E$ is
trivial by A) iv) and B).

### 6.4. Examples of extensions of a unipotent group $U$ by a group of multiplicative type $H$ that are non-trivial

<!-- label: III.XVII.6.4 -->

In view of 6.1.1 A) iv), the problem only arises in characteristic $p > 0$.

a) $H = G_{m}$, $U$ is a non-trivial form of $G_{a}$ (cf. App. III, § 5).

Let $k$ be a non-perfect field of characteristic 2, $u$ an element of $k$ such that $u^{1/2}$ does not belong to $k$.
Consider the affine group $E$ with ring $k[X, Y, (X^{2} + uY^{2})^{-1}]$, where multiplication is given by the
comorphism:

```text
(X, Y) ↦ (XX' + uYY', XY' + YX').
```

The group $E$ is smooth, connected, commutative, of dimension 2; the subscheme $Y = 0$ defines a subgroup
$H \simeq G_{m}$. The kernel $K$ of squaring in $E$ has equation:

$$
X^{2} + uY^{2} = 1,
$$

hence is of dimension 1. The group $K$ contains the unipotent radical of $E$ (defined over $\bar{k}$) but also the
contribution of $H$ which is isomorphic to $\mu_{2}$. Since $K$ is reduced over $k$, the unipotent radical of $E$ is not
defined over $k$,

<!-- original page 609 -->

and $U = E/H$ does not lift in $E$. (One verifies immediately that $U$ is the form of $G_{a}$ having ring
$k[V, W] / (V + uV^{2} + W^{2})$, the morphism $E \to U$ corresponding to the comorphism:
$V \mapsto Y^{2} / (X^{2} + Y^{2} u)$, $W \mapsto XY / (X^{2} + Y^{2} u)$).

b) $H = G_{m}$, $U = \mathbb{Z}/2\mathbb{Z}$, $k$ non-perfect of characteristic 2.

Choosing $k$ and $u$ as in a), consider the subgroup $E$ of `GL_2` generated by the element $X$ such that:

$$
X = ( 0   1) = ( u^{1/2}   0)( 0          u^{-1/2}).
    ( u   0)   ( 0         u^{1/2})( u^{1/2}    0)
$$

The group $E$ is an extension of $\mathbb{Z}/2\mathbb{Z}$ by $G_{m}$, but this extension is not trivial because the
unipotent part of $X$ is not defined over $k$.

c) $H = \mu_{p}$, $U = \alpha_{p}$, $k$ non-perfect.

Let $e$ be the commutative $p$-Lie algebra generated by two elements $X$ and $Y$ such that $X^{(p)} = X$ and
$Y^{(p)} = aX$. By App. II 2.2, $e$ is the $p$-Lie algebra of an algebraic group $E$ extension of $\alpha_{p}$ by
$\mu_{p}$, but this extension is trivial if and only if there exists $b \in k$ such that $b^{p} = a$ (since one then has
$(bX + Y)^{(p)} = 0$).

d) $H = \mu_{2}$, $U = \alpha_{2} \times \alpha_{2}$, $E$ non-commutative, $k$ a field of characteristic 2.

Consider the special linear group $SL_{2, k}$ and let $E = F(SL_{2, k})$. The group $E$ is a radicial group of height 1,
whose Lie algebra is generated by three elements

<!-- original page 610 -->

$X$, $Y$, $Z$ satisfying the following relations:

```text
[X, Y] = Z,    [X, Z] = [Y, Z] = 0,
X^{(p)} = Y^{(p)} = 0,    Z^{(p)} = Z.
```

Consequently, $E$ is a central extension of $U \simeq \alpha_{2} \times \alpha_{2}$ by $\mu_{2}$. Each factor
$\alpha_{2}$ of $U$ lifts uniquely in $E$, but $U$ itself does not lift in $E$, because $[X, Y] \neq 0$.

## 7. Nilpotent affine algebraic groups

<!-- label: III.XVII.7 -->

<!-- original page 611 -->

### 7.1. Extensions of groups of multiplicative type

<!-- label: III.XVII.7.1 -->

**Proposition 7.1.1.** *Let $S$ be a prescheme, $H$ and $K$ two $S$-preschemes in groups of multiplicative type and of
finite type, $E$ a prescheme in groups extension of $K$ by $H$ (i.e. $K$ is the quotient of $E$ by $H$ for the fpqc
topology). Then $E$ is of multiplicative type in the following two cases:*

<!-- label: III.XVII.7.1.1 -->

*a) $E$ is commutative.*

*b) The fibers of $K$ are connected.*

*Proof.* i) *Case where $S$ is the spectrum of a field $k$.*

The assertion to prove is local for the fpqc topology, which allows us to suppose $k$ algebraically closed, hence $H$
and $K$ diagonalizable. Note that $K$ acts trivially on $H$ by inner automorphisms: this is clear in case a) and follows
from 6.2.1 in case b). By induction on the length of a suitable composition series of $K$, one is reduced to the case
where $K$ is of one of three types: a) $K = G_{m}$, b) $K = \mu_{p}$, c) $K = \mu_{q}$ with $(q, p) = 1$, and in this
last case, $E$ is commutative. Using now an embedding of $H$ into $G^{r}_{m}$, one deduces that $E$ embeds into an
extension of $K$ by $G^{r}_{m}$. One may therefore suppose $H = G^{r}_{m}$.

a) If $K = G_{m}$, $E$ is a smooth, connected, affine (Exp. VI_B 9.2) algebraic group of unipotent rank zero, hence is a
torus.

b) $K = \mu_{p}$. In this case $E$ is a trivial extension.

<!-- original page 612 -->

Indeed, since $H$ is smooth, the canonical morphism $Lie E \to Lie \mu_{p}$ is surjective (App. II 3.2), and it suffices
to apply 5.8.2 i), taking App. II 2.2 into account.

c) $K = \mu_{q}$, with $(q, p) = 1$ and $E$ commutative. Here again the extension $E$ is trivial. Indeed, let
$x \in E(k)$ be a lift of a generator $\bar{x}$ of $\mu_{q}(k)$. The element $x^{q}$ is an element of $H(k)$, hence is
of the form $y^{q}$, $y \in H(k)$ (note that $G^{r}_{m}(k)$ is $q$-divisible). Since $E$ is commutative, $y^{-1} x$ is a
lift of $\bar{x}$ of order $q$.

ii) *General case.* The groups $H$ and $K$ are flat, affine, and of finite presentation over $S$ (Exp. IX 2.1), and
consequently so is $E$ (Exp. VI_B 9.2). Using then the general technique of VI_B § 10, we reduce to the case where $S$
is noetherian. To show that $E$ is of multiplicative type, it suffices then to prove that $E$ is commutative and that
${}_{n} E$ is finite over $S$ for every $n$ (Exp. X 4.8 b).

a) $E$ is commutative. One must verify that the morphism:

```text
E ×_S E ⟶ E,    (x, y) ↦ [x, y] = xyx^{−1} y^{−1}
```

factors through the unit section of $E$, and it suffices to verify this when $S$ is the spectrum of a local Artinian
ring. But then $E$ is of multiplicative type by i) and Exp. X 2.3.

<!-- original page 613 -->

b) ${}_{n} E$ is finite over $S$. Indeed, one has the exact sequence:

```text
0 → _n H → _n E → _n K ─u→ H_n
```

(where $H_{n}$ is the cokernel of raising to the $n$-th power in $H$). One knows that $H_{n}$ is of multiplicative type
(Exp. IX 2.7), hence separated, and that ${}_{n} H$ and ${}_{n} K$ are finite over $S$; `Ker u` is a closed subgroup of
${}_{n} K$, hence is finite over $S$, and ${}_{n} E$ is finite over $S$, as an extension of a finite group by a finite
group (Exp. VI_B 9.2).

### 7.2. Structure of commutative affine algebraic groups

<!-- label: III.XVII.7.2 -->

**Theorem 7.2.1.** *Let $k$ be a field, $G$ a commutative affine $k$-algebraic group. Then:*

<!-- label: III.XVII.7.2.1 -->

*a) $G$ contains a largest subgroup of multiplicative type $M$. The group $M$ is characteristic in $G$ and $G/M$ is
unipotent, and its formation commutes with extension of the field $k$.*

*b) If $k$ is perfect, $G$ is the direct product of $M$ and a unipotent algebraic subgroup $U$, and this in a unique
manner.*

*Proof.* i) *$k$ algebraically closed.*

When $G$ is smooth, 7.2.1 b) is well-known (*Bible* § 4 Th. 4). If $G$ is radicial of height 1, to the decomposition of
`Lie G` described in 4.2.2 corresponds, taking 4.3.1 v) and App. II 2.2 into account, a decomposition of $G$ of the type
7.2.1 b). In the general case, $G$ admits a composition series whose successive quotients are smooth or radicial of
height 1 (App. II 3.1). To prove 7.2.1 b), it then suffices to note that if one has an exact sequence of commutative
algebraic groups:

$$
0 \longrightarrow G' \longrightarrow G \longrightarrow G'' \longrightarrow 0,
$$

<!-- original page 614 -->

where $G'$ (resp. `G''`) is a product of a group of multiplicative type by a unipotent group, $G' = M' \cdot U'$ (resp.
$G'' = M'' \cdot U''$), then so is $G$. Indeed, consider the exact sequence:

$$
0 \longrightarrow G'/U' \longrightarrow G/U' \longrightarrow G'' \longrightarrow 0.
$$

By 7.1.1 a), the inverse image in $G/U'$ of `M''` is a subgroup of multiplicative type `M_1`. The group `M_1` lifts to a
subgroup $M$ of $G$ (5.1.1 i) a)). Likewise, using this time 6.1.1 C), one proves that there exists a unipotent subgroup
$U$ of $G$, extension of `U''` by $U'$. It is clear that $G = M \cdot U$.

ii) *General $k$.* By i), $G_{\bar{k}}$ is a direct product of a group of multiplicative type $M_{\bar{k}}$ by a
unipotent group $U_{\bar{k}}$. Set $S = \bar{k} \times_{k} \bar{k}$ and let `M_1` and `M_2` be the two inverse images of
$M_{\bar{k}}$ under the two projections $S \Rightarrow \bar{k}$. The group $G_{S} / M_{2} = (G/M_{\bar{k}})_{S}$ has
unipotent fibers, so the image of `M_1` in $G_{S} / M_{2}$ is zero (2.4 i)) and `M_2` majorizes `M_1`. Likewise `M_1`
majorizes `M_2`, and finally $M_{1} = M_{2}$. By fpqc descent, it follows that $M_{\bar{k}}$ comes from an algebraic
subgroup $M$ of $G$. It is clear that $M$ is of multiplicative type, that $G/M$ is unipotent, and that the formation of
$M$ is compatible with every extension of the field $k$. For every $k$-prescheme $S$, every subgroup of multiplicative
type $H$ of `G_S` is contained in `M_S`. Indeed, by 2.5, its image in the group with unipotent fibers
$(G/M)_{S} = G_{S} / M_{S}$ is zero. Taking in particular

<!-- original page 615 -->

for $H$ the transform of `M_S` under an automorphism of `G_S`, one deduces that $M$ is characteristic in $G$.

Finally if $k$ is perfect, $G/M$ lifts in $G$ to a unipotent group, and this in a unique manner by 6.1.1 C).

**Remark 7.2.2.**

<!-- label: III.XVII.7.2.2 -->

*i) If $k$ is not perfect, the unipotent component of $G_{\bar{k}}$ is not necessarily defined over $k$, as shown by the
example 6.4 a).*

*ii) Unlike what happens for the multiplicative-type component $M$, the unipotent component $U$ is not in general
characteristic in $G$ (whatever the characteristic of $k$). Of course, the uniqueness of the decomposition 7.2.1 b)
entails that $U$ is invariant under every $k$-automorphism of $G$. But if $U$ and $M$ are such that there exists a
$k$-prescheme $S$ and a non-zero $S$-homomorphism $h : U_{S} \to M_{S}$ (cf. 2.6), one deduces an $S$-automorphism of
`G_S`, $(u, m) \mapsto (u, h(u) + m)$, which does not leave `U_S` invariant.*

*iii) If $G$ is finite over $k$, $G/M$ corresponds by Cartier duality (2.6) to the connected component of the dual
$D(G)$ of $G$.*

### 7.3. Structure of nilpotent affine algebraic groups

<!-- label: III.XVII.7.3 -->

**Theorem 7.3.1.** *Let $k$ be a field, $G$ a nilpotent (Exp. VI_B § 8), affine, connected $k$-algebraic group. Then $G$
possesses a largest subgroup of multiplicative type $M$. The group $M$ is central and characteristic, and $G/M$ is a
unipotent algebraic group.*

<!-- label: III.XVII.7.3.1 -->

Let $Z$ be the center of $G$, $M$ the largest subgroup of multiplicative type of $Z$ (7.2.1). Since $Z$ is
characteristic in $G$ and $M$ characteristic in $Z$, $M$ is characteristic in $G$. It suffices to show that $G/M$ is
unipotent. By induction on the length of the ascending central series of $G$, this will follow, more generally, from the
following lemma:

<!-- original page 616 -->

**Lemma 7.3.2.** *(Rosenlicht). Let $G$ be a connected $k$-algebraic group, $Z$ its center. Then the center $Z'$ of
$G' = G/Z$ is unipotent.*

<!-- label: III.XVII.7.3.2 -->

*Proof.* We may suppose $k$ algebraically closed. It then suffices to show that $Z'$ does not contain a subgroup
isomorphic to $\mu_{\ell}$ for every prime number $\ell$ (4.6.1 vi)). Let then $\mu_{\ell}$ be a subgroup of $Z'$, $N$
its inverse image in $G$. Since $\mu_{\ell}$ is central in $G'$, $N$ is invariant in $G$.

i) *Case where $(\ell, p) = 1$.* One may find an element $x$ of $N(k)$ and an integer $n$ having the following
properties:

a) $x$ lifts a generator $\bar{x}$ of $\mu_{\ell}$.

b) $x^{\ell^{n}} \in Z^{0}(k)$;

(it suffices to choose a lift of $\bar{x}$ whose image in $N/Z^{0}(k)$ belongs to the $\ell$-Sylow subgroup).

Raising to the $\ell$-th power in the commutative group $Z^{0}$ is an étale morphism, hence $Z^{0}(k)$ is
$\ell$-divisible. Consequently, possibly multiplying $x$ by an element of $Z^{0}(k)$, one may suppose
$x^{\ell^{n}} = 0$. The group $N$ is then generated by two commuting commutative groups ($Z$ and the group generated by
$x$), hence is commutative. The group ${}_{\ell^{n}} N$ is a group of multiplicative type, characteristic in $N$, hence
invariant in $G$, and consequently central, $G$ being connected (Exp. IX, 5.5). Hence ${}_{\ell^{n}} N$ is contained in
$Z$, which contradicts the fact that its image in $G'$ contains $\mu_{\ell}$.

<!-- original page 617 -->

ii) *$\ell = p$.* There then exists an integer $n$ such that the image of $F_{n} N$ in $G'$ contains $\mu_{p}$, so that
one has the exact sequence:

```text
(*)    1 ⟶ K ⟶ F_n N ⟶ μ_p ⟶ 1.
```

The group $K$ is contained in $Z$, hence is commutative; it then follows from 7.2.1 and from 7.1.1 b) and 5.5.1 that
there exists a subgroup of multiplicative type contained in $F_{n} N$ whose image in the quotient by $K$ is $\mu_{p}$.
One deduces, as in i), that $F_{n} N$ is commutative. The multiplicative-type component of $F_{n} N$ (7.2.1) is
characteristic in $F_{n} N$, hence invariant in $G$, hence central (Exp. IX, 5.5); since its image in $G'$ contains
$\mu_{p}$, one obtains a contradiction.

## A. Appendix I. Hochschild cohomology and extensions of algebraic groups

<!-- label: III.XVII.A -->

<!-- original page 618 -->

### A.1. Definition of cohomology groups

<!-- label: III.XVII.A.1 -->

Let $k$ be a field, $G$ a $k$-algebraic group, $(Ab)_{G}$ the abelian category of commutative $k$-algebraic groups on
which $G$ acts. If $A \in Ob(Ab)_{G}$, the functor $h_{A} : (Sch/k)^{\circ} \to (Ens)$ canonically defined by $A$ is a
$G$-$\mathbb{Z}$-module in the sense of I 3.2. We may therefore consider the standard complex $C^{\bullet}(G, A)$ of
algebraic cochains of $G$ with values in $A$ (Exp. I 5.1), as well as the group of $i$-cocycles $Z^{i}(G, A)$, of
$i$-coboundaries $B^{i}(G, A)$, and the $i$-th cohomology group $H^{i}(G, A)$. As usual, $H^{0}(G, A)$ is identified
with the group $A^{G}(k)$, where $A^{G}$ is the $k$-functor of invariants of $A$ under $G$. The group $H^{1}(G, A)$
classifies the principal homogeneous spaces under $A$, trivial, on which $G$ acts.

The functor $A \mapsto H^{\bullet}(G, A)$ is not in general a cohomological functor from the category $(Ab)_{G}$ to
`Ab`; however, one has the following proposition:

**Proposition A.1.1.** *Let $0 \to A' \xrightarrow{u} A \xrightarrow{v} A'' \to 0$ be an exact sequence in $(Ab)_{G}$.
Then:*

<!-- label: III.XVII.A.1.1 -->

*a) If $v$ possesses a section (that is, if there exists a $k$-morphism of preschemes $s : A'' \to A$ such that
$vs = 1_{A''}$), one has the usual exact cohomology sequence:*

```text
… → H^i(G, A) → H^i(G, A'') ─d→ H^{i+1}(G, A') → …
```

<!-- original page 619 -->

*b) If $A(k) \to A''(k)$ is surjective, one has the exact sequence:*

```text
(1)    0 → A'^G(k) → A^G(k) → A''^G(k) ─d→ H¹(G, A') → H¹(G, A) → H¹(G, A'').
```

*Proof.* a) One notes that the existence of a section entails the exactness of the sequence of complexes:

```text
0 ⟶ C^•(G, A') ⟶ C^•(G, A) ⟶ C^•(G, A'') ⟶ 0.
```

b) If $x'' \in A''^{G}(k)$, its inverse image in $A$ is a principal homogeneous space under $A'$, trivial (since
$A(k) \to A''(k)$ is supposed surjective), on which $G$ acts, hence defines an element $d(x'') \in H^{1}(G, A')$. The
exactness of the sequence (1) is then immediate.

### A.2. The group $Ext_{alg}(G, A)$

<!-- label: III.XVII.A.2 -->

Let $A$ and $G$ be two $k$-algebraic groups, $E$ and $E'$ two $k$-algebraic group extensions of $G$ by $A$. These two
extensions are said to be *isomorphic* if there exists a $k$-morphism of groups $u : E \to E'$ making the diagram

```text
                E
              ↗   ↘
            A       G
              ↘   ↗
                E'
```

commutative. The group $E$ acts on $A$ by inner automorphisms, and if $A$ is commutative, this action factors through
$G$, so $G$ acts on $A$. Conversely, if $A \in Ob(Ab)_{G}$, we denote by $Ext_{alg}(G, A)$ the set of classes of
algebraic extensions $E$ of $G$ by $A$ for which the action of $G$ on $A$ defined by $E$, and that coming from the
structure

<!-- original page 620 -->

of object of $(Ab)_{G}$, coincide.

$Ext_{alg}(G, A)$ is in a natural way a bifunctor, covariant in $A$ and contravariant in $G$. More precisely:

a) If $f : A \to B$ is a morphism in $(Ab)_{G}$, and if $E$ represents an element of $Ext_{alg}(G, A)$, one defines
$f_{*}(E) \in Ext_{alg}(G, B)$ as the class of the extension of $G$ by $B$ equal to the quotient of the semidirect
product $B \cdot E$ ($E$ acting on $B$ through $G$) by the algebraic subgroup image of $A$ under the morphism $(f, i)$
(this quotient is representable by Exp. VI_A § 5), so that one has a commutative diagram:

```text
1 ⟶ A ─i→ E ⟶ G ⟶ 1
      ↓f      ↓     ↓1_G
1 ⟶ B ⟶ f_*(E) ⟶ G ⟶ 1.
```

b) If $g : H \to G$ is a $k$-morphism of $k$-algebraic groups, and if $E$ is an extension of $G$ by $A$, the fiber
product $E \times_{G} H$ is naturally an extension of $H$ by $A$, denoted $g^{*}(E)$. One therefore has a commutative
diagram:

$$
1 \longrightarrow A \longrightarrow g^{*}(E) \longrightarrow H \longrightarrow 1
     \downarrow 1_{A}          \downarrow      \downarrow g
1 \longrightarrow A \longrightarrow E \longrightarrow G \longrightarrow 1.
$$

Adapting the proofs given in J.-P. Serre, *Groupes algébriques et corps de classes*, Chap. VII, one endows
$Ext_{alg}(G, A)$ with a natural abelian group structure, functorial in $A$ and $G$.

<!-- original page 621 -->

**Proposition A.2.1.** *Let $0 \to A' \to A \to A'' \to 0$ be an exact sequence in $(Ab)_{G}$. Then:*

<!-- label: III.XVII.A.2.1 -->

*a) One has a canonical exact sequence of abelian groups:*

```text
Z¹(G, A) → Z¹(G, A'') ─d→ Ext_{alg}(G, A') → Ext_{alg}(G, A) → Ext_{alg}(G, A'').
```

*b) If $A(k) \to A''(k)$ is surjective, one deduces from a) the exact sequence:*

```text
(2)   H¹(G, A) → H¹(G, A'') ─d→ Ext_{alg}(G, A') → Ext_{alg}(G, A) → Ext_{alg}(G, A'').
```

The exact sequence of a) generalizes the usual exact sequence of $\operatorname{Hom}(\cdot, \cdot)$ valid in the
framework of commutative extensions (*loc. cit.*) and is proved in the same way. Let us simply recall the definition of
the coboundary $d : Z^{1}(G, A'') \to Ext_{alg}(G, A')$. For this, consider the extension

```text
1 ⟶ A' ⟶ A · G ⟶ A'' · G ⟶ 1,
```

deduced in the obvious way from the exact sequence $0 \to A' \to A \to A'' \to 0$. If $u \in Z^{1}(G, A'')$, $u$ defines
in the usual way a section homomorphism $u : G \to A'' \cdot G$. One then has $d(u) = u^{*}(A \cdot G)$.

### A.3. Comparison of $H^{2}(G, A)$ and $Ext_{alg}(G, A)$

<!-- label: III.XVII.A.3 -->

It is well known, in the case of abstract groups, that there exists a functorial isomorphism between the abelian groups
$H^{2}(G, A)$ and $Ext(G, A)$. Likewise in the present case, if $A$ is an element of $(Ab)_{G}$, to every 2-cocycle
$u \in Z^{2}(G, A)$ one can associate a structure of algebraic group on the prescheme $A \times_{k} G$ which makes it an
element of $Ext_{alg}(G, A)$. Moreover this extension is trivial if and only if $u \in B^{2}(G, A)$ (cf. Exp. III
1.2.2). Let us recall that the composition law on $A \times G$ is defined by the formula:

```text
(a, g)(a', g') = (a + {}^g a' + u(g, g'), gg').
```

<!-- original page 622 -->

It is clear that the extensions of $G$ by $A$ thus obtained are not arbitrary, since they possess a section. But
conversely, if $E \in Ext_{alg}(G, A)$ possesses a section $s$, $E$ is isomorphic to the extension of $G$ by $A$
associated with the 2-cocycle $u$ such that:

```text
u(g, g') = s(g) s(g') s(gg')^{−1}.
```

One finally obtains the following proposition:

**Proposition A.3.1.** *There exists a functorial isomorphism between the bifunctors with values in abelian groups:*

<!-- label: III.XVII.A.3.1 -->

```text
(G, A) ↦ H²(G, A)   and   (G, A) ↦ Ext_s(G, A),
```

*where $Ext_{s}(G, A)$ denotes the subgroup of $Ext_{alg}(G, A)$ formed by the classes of extensions of $G$ by $A$ that
possess a section.*

## B. Appendix II. Reminders and complements on radicial groups

<!-- label: III.XVII.B -->

<!-- original page 623 -->

Let $p$ be a prime number `> 1` and let $S$ be an $F_{p}$-prescheme.

### B.1. The Frobenius morphism

<!-- label: III.XVII.B.1 -->

For every $S$-prescheme $X$ and every integer $n > 0$, denote by $P_{n} : X \to X$ the $F_{p}$-endomorphism
corresponding to raising to the $p^{n}$-th power in `O_X`, and denote by $X^{(n)}$ the $S$-prescheme inverse image of
$X$ under the morphism $P_{n} : S \to S$. There then exists a unique $S$-morphism $F_{n} : X \to X^{(n)}$ making the
diagram

```text
X ────────→ X
 ↘         ↗
  ↘  F_n  ↗
   X^{(n)}
    ↓
    ↓P_n
    ↓
    S ────→ S
        P_n
```

commutative.

It is clear that $F_{n}$ is identified with the "$n$-th iterate" of $F_{1} = F$, called the Frobenius morphism of $X/S$.

If $G$ is an $S$-prescheme in groups, $G^{(n)}$ is an $S$-prescheme in groups and $F_{n} : G \to G^{(n)}$ is an
$S$-morphism of groups. Its kernel $F_{n}(G)$ is a characteristic sub-prescheme in groups of $G$ (i.e. stable under the
functor $\operatorname{Aut}_{S-gr}(G)$), and radicial over $S$. If $G$ is an $S$-prescheme in groups that is radicial,
one says that $G$ is

<!-- original page 624 -->

of height $\leqslant h$ if $F_{h}(G) = G$.

### B.2. Groups and $p$-Lie algebras

<!-- label: III.XVII.B.2 -->

If $G$ is an $S$-prescheme in groups, $Lie(G)$ (Exp. II) is naturally a restricted $p$-Lie algebra (Exp. VII_A §§ 5 and
6). In particular one has the following result (cf. Exp. VII_A):

**Proposition B.2.1.** *i) $Lie(\alpha_{p})_{S} = Lie(G_{a})_{S}$[^N.D.E-XVII-11] is a sheaf of `O_S`-modules, free over
`O_S` of rank 1, generated by an element $X$ such that $X^{(p)} = 0$.*

<!-- label: III.XVII.B.2.1 -->

*ii) $Lie(\mu_{p})_{S} = Lie(G_{m})_{S}$ is a sheaf of `O_S`-modules, free over `O_S` of rank 1, possessing a canonical
basis $X$ such that $X^{(p)} = X$.*

Let us now recall the fundamental result proved in Exp. VII_A § 7:

**Theorem B.2.2.** *Suppose $S$ affine with ring $A$. Then the functor*

<!-- label: III.XVII.B.2.2 -->

```text
G ⟼ Lie G
```

*establishes an equivalence of categories between, on the one hand, the category of $S$-preschemes in groups $G$ of
finite presentation and flat over $S$, of height 1, whose Lie algebra is locally free over `O_S`,*

<!-- original page 625 -->

*and, on the other hand, the category of restricted $p$-$A$-Lie algebras locally free of finite rank.*

*Moreover, if $G$ is as above and if $H$ is an $S$-prescheme in groups of finite presentation, the canonical morphism:*

```text
Hom_{S-gr}(G, H) ⟶ Hom_{p-A-Lie}(Lie G(S), Lie H(S))
```

*is an isomorphism.*

### B.3. Radicial groups and smooth groups

<!-- label: III.XVII.B.3 -->

We now suppose that $S$ is the spectrum of a field $k$ of characteristic $p$.

Let us recall that in Exp. VI_A § 5, it was shown that if $G$ is a $k$-algebraic group, $H$ an algebraic subgroup of
$G$, then the sheaf $G/H$ (sheaf for the fpqc topology) is representable. Recall then (VII_A 8.3):

**Proposition B.3.1.** *Let $G$ be a $k$-algebraic group. Then there exists an integer $m$ such that for every
$n \geqslant m$, the algebraic group $G / F_{n}(G)$ is smooth over $k$.*

<!-- label: III.XVII.B.3.1 -->

**Proposition B.3.2.** *Consider an exact sequence of $k$-algebraic groups:*

<!-- label: III.XVII.B.3.2 -->

```text
1 → G' → G ─u→ G'' → 1
```

*and the following assertions:*

*i) The morphism $u$ is smooth.*

*ii) $G'$ is smooth over $k$.*

*iii) For every integer $n > 0$, one has the exact sequence:*

$$
1 \longrightarrow F_{n}(G') \longrightarrow F_{n}(G) \longrightarrow F_{n}(G'') \longrightarrow 1.
$$

*iv) The morphism $F G \to F G''$ is an epimorphism.*

*v) The morphism $(Lie G)(k) \to (Lie G'')(k)$ is surjective.*

*Then one has the following implications:*

```text
i) ⇔ ii) ⇒ iii) ⇒ iv) ⇔ v).
```

*Moreover, if $G$ is smooth, the five assertions are equivalent.*

<!-- original page 626 -->

i) ⇔ ii) by Exp. VI_B 9.2 vii).

ii) ⇒ iii). If $G'$ is smooth, $F_{n} : G' \to G'^{(n)}$ is an epimorphism and iii) follows from the snake lemma
diagram.

iii) ⇒ iv) is clear.

iv) ⇔ v) by Theorem B.2.2.

v) ⇒ ii) when $G$ is smooth. Indeed `G''` is then smooth, and v) entails that one has `dim G' = dim_k(Lie G')(k)`, hence
$G'$ is smooth.

## C. Appendix III. Remarks and complements concerning Exposés XV, XVI, XVII

<!-- label: III.XVII.C -->

<!-- original page 627 -->

### C.1.

<!-- label: III.XVII.C.1 -->

It may be that propositions 1.2 and 1.2 bis of XV remain true if one removes the hypothesis that $H'$ is smooth over
$S'$. This is in particular the case if $G$ is finite, flat, and commutative.

### C.2. Complement to XV 4.8

<!-- label: III.XVII.C.2 -->

The following proposition, as well as Theorems C.3.1 and C.4.1 below, will appear in a paper in preparation by M.
Raynaud on group schemes over a discrete valuation ring.[^N.D.E-XVII-12]

**Proposition C.2.1.** *Let $S$ be the spectrum of a discrete valuation ring, $t$ its generic point, $G$ an
$S$-prescheme in groups of finite type and flat, $\tilde{G} = \operatorname{Spec} \Gamma(G, O_{G})$,
$u : G \to \tilde{G}$ the canonical morphism. Then:*

<!-- label: III.XVII.C.2.1 -->

*(1) $\tilde{G}$ is naturally an $S$-group scheme and $u$ is a homomorphism.*

*(2) $Ker(u)$ is flat over $S$ and $(\tilde{G}, u)$ is an fpqc quotient of $G$ by $Ker(u)$, so that $\tilde{G}$ is the
largest affine quotient of $G$.*

*(3) If $G_{t}$ is affine, $Ker(u)$ is an étale group over $S$, equal to the trivial group if and only if $G$ is
separated over $S$. In particular, an $S$-group scheme $G$, flat, of finite type, separated, with affine generic fiber,
is affine.*

### C.3.

<!-- label: III.XVII.C.3 -->

In the statement of XV 6.6, the hypothesis that $H$ is equal to its connected normalizer is unnecessary for the set of
points $s$ of $S$ such that $H_{s}$ is a parabolic subgroup of $G_{s}$ to be an open set. Indeed, taking up the proof
given in paragraph c) preceding Lemma 6.9, and denoting by $N$ the schematic closure of $N_{t}$ in $G$. Then $N$ is a
closed subscheme in groups of $G$, flat over $S$, majorizing $H$ and contained in $N$. It then follows from the theorem
below

<!-- original page 628 -->

that $G/N$ is representable. Since $G_{s} / N_{s}$ is proper and connected, one finishes as in *loc. cit.*

**Theorem C.3.1.**[^N.D.E-XVII-13] *Let $S$ be the spectrum of a henselian discrete valuation ring, $G$ an $S$-prescheme
in groups locally of finite type, $H$ a closed sub-prescheme in groups of $G$, flat over $S$. Then $G/H$ is
representable.*

<!-- label: III.XVII.C.3.1 -->

### C.4. Complement to (XVI 1.1)

<!-- label: III.XVII.C.4 -->

The following theorem refines (VIII 7.9).

**Theorem C.4.1.** *Let $S$ be the spectrum of a discrete valuation ring of residue characteristic $p > 0$, and let $G$
be a commutative, smooth $S$-group scheme of finite type and separated over $S$. Then the following conditions are
equivalent:*

<!-- label: III.XVII.C.4.1 -->

*(i) ${}_{p} G$ is finite over $S$.*

*(ii) For every $S$-prescheme $S'$ and for every $S'$-prescheme in groups $H'$, of finite presentation over $S'$,
separated over $S'$, every $S'$-monomorphism $u : G_{S'} \to H'$ is an immersion.*

### C.5.

<!-- label: III.XVII.C.5 -->

The example (XVII 6.4 a)) provides an example of a smooth group over a field $k$, whose unipotent radical is not defined
over $k$. The following proposition gives a general method for obtaining such groups:

<!-- original page 629 -->

**Proposition C.5.1.** *Let $k$ be a field, $K$ a finite radicial extension of $k$ of degree `> 1`, $H$ a connected,
smooth $K$-algebraic group of dimension $r$, $G = \prod_{K/k} H/K$, which is a $k$-algebraic group, smooth, connected,
of dimension $r[K : k]$. Let $u : G_{K} \to H$ be the canonical homomorphism, and $R = Ker(u)$. Then:*

<!-- label: III.XVII.C.5.1 -->

*i) The morphism $u$ is an epimorphism and $R$ is a smooth, unipotent, connected algebraic group.*

*ii) If $U$ is a smooth algebraic subgroup of $G$ such that `U_K` majorizes $R$, then $U = G$.*

**Corollary.** *Keep the notations of the preceding proposition.*

*a) If $H$ is not unipotent, the unipotent radical of $G_{\bar{k}}$ is not defined over $k$.*

*b) If $H$ is a non-zero abelian variety, $G$ is not an extension of an abelian variety by a smooth linear group.*

*c) If $H$ is not solvable, the solvable radical of $G_{\bar{k}}$ is not defined over $k$, and $G$ does not possess a
Borel subgroup defined over $k$.*

Let us first show how the corollary follows from the proposition.

a) Let $U$ be a unipotent radical of $G$. Then `U_K` is the unipotent radical of `G_K`, hence majorizes $R$, since $R$
is smooth unipotent connected by i), hence $U = G$ by ii). Now `G_K` admits $H$ as a quotient, and $H$ is not unipotent
by hypothesis, hence $G$ is not unipotent, whence a contradiction.

b) If $G$ is an extension of an abelian variety by a linear group $L$, smooth over $k$, necessarily `L_K` majorizes $R$,
hence $L = G$. Now $G$ cannot be a linear group since `G_K` possesses a quotient that is a non-zero abelian variety.

c) Let $S$ (resp. $B$) be a solvable radical of $G$ (resp. a Borel subgroup of $G$); then `S_K` (resp. `B_K`) majorizes
$R$, hence $S = G$ (resp. $B = G$). But then $G$ is solvable, which contradicts the fact that `G_K` possesses a quotient
that is not solvable.

*Proof of Proposition C.5.1.*

i) Let us begin by describing the morphism $u$. The data of a $K$-scheme

$$
f : S \longrightarrow \operatorname{Spec}(K)
$$

<!-- original page 630 -->

allows one to construct the diagram:

```text
Spec(K) ←─h──── T ──jT──→ X
   ↓ j           ↓ s
   ↓             ↓
Spec(k) ←──g──── S          (where g = j ∘ f)
```

where $T = \operatorname{Spec}(K) \times_{\operatorname{Spec}(k)} S$, $h$ and `jT` are the two projections, and $s$ is
the section of $T$ over $S$ such that $h \circ s = f$. The map

$$
u(S) : G_{K}(S) \longrightarrow H(S)
$$

is simply the composite map:

$$
G_{K}(S) \xrightarrow{\sim} H(T) \to H(S),
$$

where the last arrow is defined by the section $s$.

Take in particular for $S$ the spectrum of an algebraic closure $\bar{k}$ of $k$ and for $f$ the unique $k$-morphism
$K \to \bar{k}$, so that $T$ is a local Artinian scheme. To prove i) it suffices to do so after extension
$K \to \bar{k}$ of the base field. Now it is clear that $G_{S} = \prod_{T/S} H_{T} / T$ represents the Greenberg functor
of `H_T` relative to $S$ (M. J. Greenberg, *Schemata over local rings*, Ann. of Maths. 73, 1961, p. 624-648). The
description made above then shows that, by means of this last identification, $u_{S}$ is the canonical transition
morphism:

```text
Green(H_T) ⟶ H_S = H_T ×_T S.
```

Assertion i) then follows from the fact that $H$ is smooth over $K$ and from (M. J. Greenberg, *Schemata over local
rings II*, Ann. of Maths. 78, 1963, p. 256-266).

ii) To establish ii) we may suppose $k$ separably closed. Let $U$ be a smooth algebraic subgroup of $G$ such that
$U_{K} \supset R$, and let us show that $U = G$.

<!-- original page 631 -->

Since $G$ is connected, we may suppose $U$ connected. Let $V$ be the smooth connected algebraic subgroup $u(U_{K})$ of
$H$, and $V' = \prod_{K/k} V/K$, which is a smooth connected algebraic subgroup of $G$. The group $V'_{K}$ is an
algebraic subgroup of `G_K`, and the canonical morphism $V'_{K} \to V$ is simply the restriction of $u$ to $V'_{K}$. By
hypothesis, `U_K` majorizes $R$, *a fortiori* `U_K` majorizes $Ker(V'_{K} \to V)$; on the other hand, by construction,
the image of `U_K` in $H$ is equal to $V$. One deduces that `U_K` majorizes $V'_{K}$, hence $U$ majorizes $V'$. On the
other hand, the canonical isomorphism

```text
G(k) ↪ G(K) ─u(K)→ H(K)
```

evidently sends $U(k)$ into $V(K) = V'(k)$; that is to say, $U(k)$ is contained in `V'(k)`. Since $U$ is smooth and $k$
is separably closed, this entails $U \subset V'$, whence $U = V'$. One then has the equalities:

```text
([K : k] − 1) dim V = dim Ker(V'_K → V) = dim R = ([K : k] − 1) dim H.
```

Since $K \neq k$, one concludes that $\dim V = \dim H$, whence $V = H$ and finally $U = V' = G$.

## Footnotes

<!-- LEDGER DELTA — Exposé XVII — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| groupe algébrique unipotent | unipotent algebraic group | Per Exposé title. |
| extension (de groupes algébriques) | extension (of algebraic groups) | Standard. |
| groupe de type multiplicatif | group of multiplicative type | Per Exp. IX–X. |
| groupe additif / multiplicatif | additive / multiplicative group | `G_a` / `G_m`. |
| groupe constant | constant group | Standard. |
| groupe radiciel | radicial group | Per glossary. |
| groupe radiciel de hauteur 1 | radicial group of height 1 | Per Intro §1. |
| morphisme de Frobenius | Frobenius morphism | Standard. |
| `F_n(G)` | `F_n(G)` | Kernel of `n`-th iterate of relative Frobenius. |
| `α_{p^n}` | `α_{p^n}` | Standard. |
| `μ_n` | `μ_n` | `n`-th roots of unity. |
| Cb (OCR) | `Ĉ` | Hat on category symbol restored where it occurred. |
| forme tordue | twisted form | Per Exposé 1.4. |
| suite de composition | composition series | Standard. |
| suite de composition centrale | central composition series | Standard. |
| suite de composition caractéristique | characteristic composition series | Per Exp. VI_B. |
| groupe unipotent élémentaire | elementary unipotent group | Per 1.7. |
| `Trigstr(n)` | `Trigstr(n)` | Strictly upper-triangular matrices. |
| `p`-algèbre de Lie | `p`-Lie algebra | Per glossary. |
| `p`-algèbre de Lie restreinte | restricted `p`-Lie algebra | Per Exp. VII_A. |
| `p`-algèbre de Lie unipotente | unipotent `p`-Lie algebra | Per 3.6. |
| partie réductive / unipotente (d'une `p`-algèbre de Lie) | reductive / unipotent part | Per 4.2.2. |
| Lemme d'Artin–Schreier (morphisme) | Artin–Schreier morphism | `x ↦ x^p − ax`. |
| théorème 90 de Hilbert | Hilbert's Theorem 90 | Standard. |
| théorème d'Engel | Engel's theorem | Standard. |
| théorème de Cartier | Cartier's theorem | Per characteristic 0 connectivity argument. |
| Bible | *Bible* | Séminaire Chevalley 1956/58; italicized. |
| relèvement (d'un sous-groupe) | lift (of a subgroup) | Standard. |
| centralisateur / normalisateur / transporteur | centralizer / normalizer / transporter | American spelling. |
| `k`-résoluble | `k`-solvable | Per Rosenlicht 1963; preserve hyphenated `k`. |
| espace principal homogène | principal homogeneous space | Standard. |
| torseur | torsor | Standard. |
| produit semi-direct | semidirect product | Standard. |
| produit direct | direct product | Standard. |
| sous-tore (maximal) | (maximal) subtorus | Standard. |
| dévissage | dévissage | Loanword. |
| variété abélienne | abelian variety | Standard. |
| topologie fpqc | fpqc topology | Standard. |
| cohomologie de Hochschild | Hochschild cohomology | Standard. |
| cohomologie galoisienne | Galois cohomology | Standard. |
| `Ext_{alg}(G, A)` | `Ext_{alg}(G, A)` | Algebraic extensions group. |
| dualité de Cartier | Cartier duality | Standard. |
| groupe vectoriel `W(M)` | vector group `W(M)` | Per Exp. I 4.6.1. |
| extension infinitésimale | infinitesimal extension | Standard. |
| EGA III, IV, V | `EGA III` / `EGA IV` / `EGA V` | Standard. |
| Sém. Bourbaki | *Sém. Bourbaki* | Italics in journal citation. |
| « k-résoluble » (guillemets) | "`k`-solvable" | English double quotes for Grothendieckian coinages. |
| « Tôhoku » | "Tôhoku" | Per glossary. |
| corps non parfait | non-perfect field | Standard. |
| morphisme étale / lisse / plat | étale / smooth / flat morphism | Standard. |
| de présentation finie | of finite presentation | Per glossary. |
| de type fini | of finite type | Per glossary, when source uses this term. |
| groupe nilpotent | nilpotent group | Per Exp. VI_B § 8. |
| anneau local artinien | local Artinian ring | Standard. |
| sous-groupe distingué | normal subgroup | Standard (English does not distinguish). |
| schématiquement dense | schematically dense | Per Exp. IX 4.1. |
| schéma quotient | quotient scheme | Per Exp. V. |
| anneau de valuation discrète | discrete valuation ring | Standard. |
| anneau de valuation discrète hensélien | henselian discrete valuation ring | Standard. |
| foncteur de Greenberg | Greenberg functor | Per Greenberg 1961, 1963. |
| sous-groupe de Borel | Borel subgroup | Per Exp. XXVI. |
| sous-groupe parabolique | parabolic subgroup | Per Exp. XXVI. |
| radical résoluble / unipotent | solvable / unipotent radical | Standard. |
| clôture parfaite / algébrique / séparable | perfect / algebraic / separable closure | Standard. |
| sous-faisceau de groupes abéliens | subsheaf of abelian groups | Standard. |
| principe de l'extension finie | principle of finite extension | Per EGA IV 9.1.1. |
| comorphisme | comorphism | Standard. |
| formule de Jacobson | Jacobson's formula | Per Exp. VII_A 5.2. |
| Cohomologie Galoisienne (Serre) | *Cohomologie Galoisienne* | Italics. |
| Corps locaux (Serre) | *Corps locaux* | Italics. |
| Groupes algébriques et corps de classes (Serre) | *Groupes algébriques et corps de classes* | Italics. |
| Groupes algébriques I (Demazure–Gabriel) | *Groupes algébriques I* | Italics. |
| Abelian varieties (Lang) | *Abelian varieties* | Italics. |
| Groupes et algèbres de Lie (Bourbaki) | *Groupes et algèbres de Lie* | Italics. |
| caractéristique résiduelle | residue characteristic | Per glossary. |
-->

[^XVII-0-0]: cf. note on page 1 of Exposé XV.

[^N.D.E-XVII-1]: N.D.E.: reference to VII_A?

[^N.D.E-XVII-2]: N.D.E.: verify this reference.

[^N.D.E-XVII-3]: N.D.E.: verify this reference.

[^N.D.E-XVII-4]: N.D.E.: $h$ has been changed to $\bar{h}$.

[^N.D.E-XVII-5]: N.D.E.: give another reference here…

[^N.D.E-XVII-6]: N.D.E.: replacing `X_1` by $L$.

[^XVII-4-1]: i.e. the smallest integer such that $F^{h} = id_{G}$, cf. App. II 1.

[^XVII-4-2]: *Sém. Bourbaki* n° 145, 1956/57.

[^N.D.E-XVII-7]: N.D.E.: $H^{i}_{0}$ has been replaced by $H^{i}$, to be in accord with the notations of App. I and of
    Exp. I.

[^N.D.E-XVII-8]: N.D.E.: there is no number 5.2.2.

[^N.D.E-XVII-9]: N.D.E.: This is Proposition III.6.4.2 of the book by M. Demazure and P. Gabriel, *Groupes algébriques
    I*, Masson & North-Holland (1970).

[^N.D.E-XVII-10]: N.D.E.: see, for example, Proposition III.6.4.2 of the book by M. Demazure and P. Gabriel, *Groupes
    algébriques I*, Masson & North-Holland (1970).

[^N.D.E-XVII-11]: N.D.E.: the definition of $\alpha_{p}$, already given at the start of this Exposé, has been deleted
    here.

[^N.D.E-XVII-12]: N.D.E.: comments to be added here, including references to VI_B…

[^N.D.E-XVII-13]: N.D.E.: See Theorem 4C in: S. Anantharaman, *Schémas en groupes, espaces homogènes et espaces
    algébriques sur une base de dimension 1*, Bull. Soc. Math. France, Mém. 33 (1976), 5-79.
