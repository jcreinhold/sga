# Exposé VI_A. Generalities on algebraic groups

<!-- label: III.VI_A -->

*by P. Gabriel*

> [^N.D.E-VI_A-0] Version of 13/10/2024.

Throughout this entire chapter, $A$ will denote an Artinian local ring with residue field $k$. A group scheme $G$ over
$\operatorname{Spec} A$ will be called simply an $A$-*group*. This $A$-group is said to be *locally of finite type* if
the underlying scheme is locally of finite type over $A$; it is said to be *algebraic* if the underlying scheme is of
finite type over $A$.

<!-- original page 287 -->

## 0. Preliminary remarks

<!-- label: III.VI_A.0 -->

### 0.1

Let us first consider a group scheme $G$ over an arbitrary scheme $S$. We call *multiplication* the structural morphism
`µ : G ×_S G → G`, and *inversion* the morphism $c : G \to G$ defined by the equalities $c(T)(x) = x^{-1}$ (with $T$ a
scheme over $S$ and $x$ an element of $G(T)$). If $U$ and $V$ are subsets of the underlying set of $G$, we write $U
\cdot V$ for the image under the multiplication morphism of the part of $G \times_{S} G$ consisting of points whose
first projection lies in $U$ and second projection in $V$. Likewise, the notations $U^{-1}$ and $c(U)$ are equivalent.

Let $pr_{1}$ denote the projection of $G \times_{S} G$ onto the first factor and $\sigma : G \times_{S} G \to G
\times_{S} G$ the morphism with components $pr_{1}$ and `µ`. For every $S$-scheme $T$, $\sigma(T)$ is the map $(x, y)
\mapsto (x, xy)$; it follows that $\sigma$ is an automorphism. The composition of this automorphism with the projection
$pr_{2}$ of $G \times_{S} G$ onto the second factor is the multiplication morphism. When $G$ is flat over $S$, $pr_{2}$
and hence `µ` are flat morphisms; when $G$ is smooth over $S$, $pr_{2}$ and hence `µ` are smooth morphisms, etc.

<!-- original page 288 -->

### 0.2

We assume from now on that $S$ is the spectrum of an Artinian local ring $A$ with residue field $k$. We denote by
$(Sch/k)_{red}$ the category of reduced schemes over $k$. For every scheme $X$ over $A$, the reduced scheme $X_{red}$ is
an object of $(Sch/k)_{red}$, and the functor $X \mapsto X_{red}$ is right adjoint to the inclusion of $(Sch/k)_{red}$
into $(Sch/A)$. It follows that, for every $A$-group $G$, $G_{red}$ is a group in the category
$(Sch/k)_{red}$,[^N.D.E-VI_A-1] i.e., for every reduced $k$-scheme $T$, $G_{red}(T)$ is equipped with a group structure,
functorial in $T$. One should beware that $G_{red}$ is not necessarily a $k$-group, since the "multiplication" is only a
morphism from `(G_red ×_k G_red)_red` into $G_{red}$.[^N.D.E-VI_A-2]

<!-- original page 294 -->

[^N.D.E-VI_A-3] However, if $k$ is a perfect field, the inclusion of $(Sch/k)_{red}$ into $(Sch/k)$ commutes with
products, so that groups in the category $(Sch/k)_{red}$ are identified with group schemes over $k$ whose underlying
scheme is reduced. In this case, if $G$ is a $k$-group, $G_{red}$ is a group subscheme of $G$; this subgroup is not in
general normal in $G$.

For example, if $k$ is a field of characteristic 3, the constant group $(\mathbb{Z}/2\mathbb{Z})_{k}$ acts non-trivially
on the diagonalizable group $D_{k}(\mathbb{Z}/3\mathbb{Z})$ (cf. Exp. I, 4.1 and 4.4); if $G$ denotes the semidirect
product of $D_{k}(\mathbb{Z}/3\mathbb{Z})$ by $(\mathbb{Z}/2\mathbb{Z})_{k}$ defined by this action, $G_{red}$ is
identified with $(\mathbb{Z}/2\mathbb{Z})_{k}$ and is not normal in $G$.[^N.D.E-VI_A-4]

Let $k$ be an arbitrary field, $k^{p^{-\infty}}$ its perfect closure, and $H$ a group in the category $(Sch/k)_{red}$.
Then $(H \otimes_{k} k^{p^{-\infty}})_{red}$ is a group scheme over the perfect field $k^{p^{-\infty}}$. Since $H
\otimes_{k} k^{p^{-\infty}}$ and $(H \otimes_{k} k^{p^{-\infty}})_{red}$ have the same underlying topological space, one
sees that the groups of $(Sch/k)_{red}$ share with $k$-groups certain topological properties invariant under extension
of the base field: for example, it will follow from 0.3 and the remarks just made that every group of $(Sch/k)_{red}$ is
separated.

<!-- original page 289 -->

We shall encounter groups of $(Sch/k)_{red}$ in what follows whenever we deal with a non-empty, locally closed subset
$U$ of an $A$-group $G$ such that $U \cdot U = U$ and $U^{-1} = U$: indeed, the reduced subscheme of $G$ defined by $U$
is then a group of $(Sch/k)_{red}$.

### 0.3

An $A$-group $G$ is always separated, since the unit section $e : \operatorname{Spec} A \to G$ is a closed immersion.
Indeed, let $x$ be the unique point of $\operatorname{Spec} A$ and $\eta$ the structural morphism $G \to
\operatorname{Spec} A$. Since $\eta \circ e = id_{\operatorname{Spec} A}$, for every affine open $U =
\operatorname{Spec} B$ of $G$ containing $e(x)$, the morphism $B \to A$ has a section, and so is surjective. It follows
that $e$ is a closed immersion.[^N.D.E-VI_A-5] Now the diagonal of $G \times_{A} G$ is identified with the functor from
$(Sch/A)^{\circ}$ with values in `(Ens)` that associates to every scheme $S$ over $A$ the inverse image of the unit
element of $G(S)$ under the map $\phi(S) : (x, y) \mapsto x \cdot y^{-1}$ from $G(S) \times G(S)$ to $G(S)$. We
therefore have the cartesian square below, so that the diagonal morphism, being obtained from a closed immersion by base
change, is itself a closed immersion:

```text
            φ
G ×_S G ─────────→ G
   │                ▲
   │ diagonal       │ unit section
   ▼                │
   G ─────────→ Spec A.
```

<!-- original page 295 -->

### 0.4

[^N.D.E-VI_A-6] Let $G$ be an $A$-scheme. We shall say that a point $g$ of $G$ is *strictly rational over* $A$ if there
exists an $A$-morphism $s : \operatorname{Spec} A \to G$ sending the unique point of $\operatorname{Spec} A$ to $g$,
i.e. if the morphism $A \to O_{G,g}$ admits a retraction. Note that one then has $\kappa(g) = k$, and so $g$ is a closed
point of $G$ (if $B$ is the ring of an affine open neighborhood of $g$ and $\mathfrak{p}$ the prime ideal of $B$
corresponding to $g$, then $B/\mathfrak{p} \subset k$ is a finite $A$-algebra, hence an integral Artinian ring, hence a
field).

<!-- original page 290 -->

Suppose henceforth that $G$ is an $A$-group; then such a section $s : \operatorname{Spec} A \to G$ defines an
automorphism $r_{s}$ of the scheme $G$ over $A$, which we call *right translation by* $s$: for every morphism $\pi : S
\to \operatorname{Spec} A$, $r_{s}(\pi)$ is the automorphism of $G(S)$ defined by $x \mapsto x \cdot G(\pi)(s)$, for
every $x \in G(S)$. Similarly, we write $\ell_{s}$ for the *left translation by* $s$, i.e. the automorphism of $G$
defined by the equalities $\ell_{s}(\pi)(x) = G(\pi)(s) \cdot x$, for every $x \in G(S)$.

Since $G \otimes_{A} k$ and $G$ have the same underlying topological space $G$, since $G \otimes_{A} k$ is a $k$-group,
and since $s \otimes_{A} k$ depends only on $g$ and not on $s$, one sees that the automorphisms of $G$ induced by
$r_{s}$ and $\ell_{s}$ (or by $r_{s \otimes k}$ and $\ell_{s \otimes k}$) depend only on $g$ and not on $s$; when $P$ is
a subset of $G$, we may therefore write $r_{g}(P)$ or $P \cdot g$ (resp. $\ell_{g}(P)$ or $g \cdot P$) instead of
$r_{s}(P)$ (resp. $\ell_{s}(P)$), in agreement with 0.1.

**Remark 0.4.1.** *If $g$ is a strictly rational point of $G$ and if $A \to A'$ is a morphism of Artinian local rings,
then $G' = G \otimes_{A} A'$ has a unique point $g'$ above $g$, and $g'$ is strictly rational over $A'$; moreover, if
one writes $P'$ for the inverse image of $P$ in $G'$, then $P' \cdot g'$ is the inverse image of $P \cdot g$ (cf. EGA I,
3.4.8).*

<!-- label: III.VI_A.0.4.1 -->

**Proposition 0.5.** [^N.D.E-VI_A-7] *Let $G$ be an $A$-group and `U, V` two dense open subsets of $G$. Then $U \cdot V$
(i.e. the image of $U \times_{A} V$ under multiplication) is equal to the whole underlying space of $G$.*

<!-- label: III.VI_A.0.5 -->

*Proof.* Since $G$ and $G \otimes_{A} k$ have the same underlying space, we may, possibly replacing $A$ by $k$ and $G$
by $G \otimes_{A} k$, assume that $A = k$. Let $g \in G$. Set $K = \kappa(g)$; then left translation $\ell_{g}$ is an
automorphism of `G_K`. Since the projection $G_{K} \to G$ is open, `U_K` and `V_K` are dense open subsets of `G_K`, as
is the image of `V_K` under $\lambda_{g}$. There exists therefore $v \in V_{K}$ such that $u = \ell_{g}(v)$ belongs to
`U_K`. Let $L$ be an extension of $K$ containing $\kappa(v)$ (and so $\kappa(u)$), and let $g_{L}$ and $v_{L}$ be the
$L$-points of `G_L` deduced from $g$ and $v$. Then $g_{L} \cdot v_{L} = u'$ is a point of `G_L` above $u$, and so $g_{L}
= u' \cdot v^{-1}_{L}$ lies above $U \cdot V$, whence $g \in U \cdot V$, which proves the proposition.

<!-- original page 296 -->

**Corollary 0.5.1.** [^N.D.E-VI_A-8] *If $G$ is an irreducible $A$-group, then $G$ is quasi-compact.*

<!-- label: III.VI_A.0.5.1 -->

*Proof.* Let $U$ be a non-empty affine open subset of $G$; then $U$ is dense in $G$, so by 0.5 the morphism
`µ : U ×_A U → G` is surjective, and therefore $G$ is quasi-compact since $U \times_{A} U$ is.

**Corollary 0.5.2.** [^N.D.E-VI_A-9] *Let $G$ be an $A$-group scheme, and $H$ a group subscheme of $G$ over $A$. Then
$H$ is closed.*

<!-- label: III.VI_A.0.5.2 -->

*Proof.* Let $k'$ be the perfect closure of the residue field $k$ of $A$. Since the underlying topological spaces of $G$
and $H$ are unchanged under the base change $A \to k \to k'$, we may suppose that $A = k$ is a perfect field. We may
then suppose that $G$ and $H$ are reduced, hence geometrically reduced.

Let $\bar{H}$ be the closure of $H$; then `µ⁻¹(H̄)` is a closed subset of $G \times G$ containing $H \times H$. Since the
morphism $H \to \operatorname{Spec} k$ (resp. $\bar{H} \to \operatorname{Spec} k$) is universally open, and since $H$ is
dense in $\bar{H}$, then $H \times H$ is dense in $H \times \bar{H}$ and $H \times \bar{H}$ is dense in $\bar{H} \times
\bar{H}$, so $H \times H$ is dense in $\bar{H} \times \bar{H}$. Therefore `µ(H̄ × H̄) ⊂ H̄`, and so, since $\bar{H} \times
\bar{H}$ is reduced, `µ` induces a morphism `µ′ : H̄ × H̄ → H̄`.

Let then $g \in \bar{H}$, and set $K = \kappa(g)$. Since the projection $\bar{H}_{K} \to \bar{H}$ is open, `H_K` and
$\ell_{g}(H_{K})$ are two dense open subsets of $\bar{H}_{K}$, so there exist $u, v \in H_{K}$ such that $\ell(g)(v) =
u$. One concludes, as in the proof of 0.5, that $g$ belongs to $H \cdot H = H$, whence $\bar{H} = H$.

## 1. Local properties of an $A$-group locally of finite type

<!-- label: III.VI_A.1 -->

<!-- original page 292 -->

We shall first see that, if $G$ is locally of finite type and flat over $A$, one can "make strictly rational any closed
point of $G$" by means of a finite, flat extension of the base.

### 1.1

Unless explicit mention is made to the contrary, we assume from now on that $G$ is an $A$-group locally of finite type.
When $A$ is a field $k$, we shall obtain in Exposé VII_B very precise results on the local rings of $G$.[^N.D.E-VI_A-10]
We content ourselves here with a few elementary results:

**Proposition 1.1.1.** *Let $x$ be a point of an $A$-group $G$ locally of finite type and flat over $A$. Then the local
ring $O_{G,x}$ is Cohen–Macaulay, and there exists a system $a_{1}, \cdots, a_{n}$ of parameters of $O_{G,x}$ such that
$O_{G,x}/(a_{1}, \cdots, a_{n})$ is a finite and flat (hence finite and free) $A$-module.*

<!-- label: III.VI_A.1.1.1 -->

We first assume $A$ equal to its residue field $k$; it then suffices to prove that $O_{G,x}$ is Cohen–Macaulay and one
may limit oneself to the case where $x$ is a closed point (cf. EGA 0_IV, 16.5.13). By Lemma 1.1.2 below, $G$ contains a
closed point $y$ such that $O_{G,y}$ is Cohen–Macaulay. By SGA 1, I § 9, this amounts to saying that, for every finite
extension $K$ of the base field $k$ and every point `ȳ` of $\bar{G} = G \otimes_{k} K$ above $y$, $O_{\bar{G},\bar{y}}$
is Cohen–Macaulay. If the extension $K$ has been chosen large enough — i.e. if $K$ contains a normal extension of $k$
containing the residue fields $\kappa(y)$ and $\kappa(x)$ — then `ȳ` is (strictly) rational over $K$, as is every point
$\bar{x}$ of `Ḡ` above $x$.[^N.D.E-VI_A-11] Since the automorphism $r_{\bar{x}} \circ (r_{\bar{y}})^{-1}$ sends `ȳ` to
$\bar{x}$, it follows that $O_{\bar{G},\bar{x}}$, and hence $O_{G,x}$ (SGA 1, I § 9), are Cohen–Macaulay.

<!-- original page 293 -->

When $A$ is again assumed arbitrary, the preceding argument applies to $k \otimes_{A} G$, so that $k \otimes_{A}
O_{G,x}$ is Cohen–Macaulay. If $a_{1}, \cdots, a_{n}$ is a sequence of elements of $O_{G,x}$ whose image in $k
\otimes_{A} O_{G,x}$ is a system of parameters, it follows from SGA 1, IV 5.7 or from EGA 0_IV, 15.1.16, that $a_{1},
\cdots, a_{n}$ is an $O_{G,x}$-regular sequence and that $O_{G,x}/(a_{1}, \cdots, a_{n})$ is finite and flat (hence
finite and free) over $A$.

**Lemma 1.1.2.** *Every non-empty scheme $X$, locally of finite type over an Artinian ring $A$, contains a closed point
$x$ whose local ring is Cohen–Macaulay.*

<!-- label: III.VI_A.1.1.2 -->

We may of course assume $X$ affine with algebra $B$, and argue by induction on $\dim X$ (the assertion is clear if $X$
is discrete, since all local rings are then Artinian). Since $B$ is of finite type over $A$, if $\dim B > 0$, $B$
contains an element $a$ that is non-invertible and not a zero-divisor.[^N.D.E-VI_A-12] The closed subscheme $X' =
\operatorname{Spec} B/(a)$ of $X$ is then of dimension strictly less than $\dim X$, and by induction contains a closed
point $x$ such that $O_{X',x}$ is Cohen–Macaulay. Since $O_{X',x} = O_{X,x}/(a)$ and $a$ is non-invertible and not a
zero-divisor in $O_{X,x}$, then $O_{X,x}$ is Cohen–Macaulay (see also EGA IV_2, 6.11.3).

**Proposition 1.2.** *Let $A$ be an Artinian local ring, $G$ an $A$-group locally of finite type and flat over $A$, and
$x$ a closed point of $G$. There exists an $A$-algebra $A'$ that is local, finite and free over $A$, such that every
point of $G \otimes_{A} A'$ above $x$ is strictly rational over $A'$.*

<!-- label: III.VI_A.1.2 -->

<!-- original page 294 -->

[^N.D.E-VI_A-13] Indeed, let $k_{1}$ be a normal extension of finite degree of $k$ containing the residue field
$\kappa(x)$ of $x$. By Lemma V 4.1.2, there exists an $A$-algebra `A_1` that is local, finite and free over $A$, with
residue field $k_{1}$. In this case (cf. N.D.E. (11)) all the points $g_{1}, \cdots, g_{n}$ of $G \otimes_{A} A_{1}$
above $x \in G$ have $k_{1}$ as residue field (i.e. $g_{1}, \cdots, g_{n}$ are rational over `A_1` in the sense of Exp.
V, § 4.e)).

Let then $B_{1}, \cdots, B_{n}$ be the local rings of $g_{1}, \cdots, g_{n}$. By 1.1.1, $B_{1}, \cdots, B_{n}$ have
quotients $B'_{1}, \cdots, B'_{n}$ that are Artinian and finite and free over `A_1`. Set $A' = B'_{1} \otimes_{A_{1}}
\cdots \otimes_{A_{1}} B'_{n}$. Then $A'$ is local, finite and free over `A_1` and, for each $i = 1, \cdots, n$, we have
surjective homomorphisms

```text
B_i ⊗_{A_1} A′ ↠ B′_i ⊗_{A_1} A′ ↠ A′,
```

the second induced by the multiplication map $B'_{i} \otimes_{A_{1}} B'_{i} \twoheadrightarrow B'_{i}$. Consequently,
$A'$ answers the question.

### 1.3

Let $e$ denote the unit element (or origin) of $G$, i.e. the image of the unique point of $\operatorname{Spec} A$ by the
unit section $\operatorname{Spec} A \to G$. By definition itself, $e$ is strictly rational over $A$.

**Proposition 1.3.1.** [^N.D.E-VI_A-14] *Let $G$ be a group locally of finite type and flat over an Artinian ring $A$,
and $K$ (resp. $\bar{k}$) the perfect closure (resp. an algebraic closure) of the residue field $k$ of $A$.*

*(1) For every closed point $x$ of $\bar{G} = G \otimes_{k} \bar{k}$, the local rings $O_{\bar{G},\bar{e}}$ and
$O_{\bar{G},x}$ are isomorphic. In particular, the tangent spaces $T_{e} G$ and $T_{x} G$ have the same dimension.*

*(2) The following assertions are equivalent:*

*(i) $G \otimes_{A} K$ is reduced.* *(i bis) $O_{G,e} \otimes_{A} K$ is reduced.* *(ii) $G$ is smooth over $A$.* *(ii
bis) $G$ is smooth over $A$ at the origin.*

<!-- label: III.VI_A.1.3.1 -->

*Proof.* (1) Let $x$ be a closed point of `Ḡ`; there is exactly one $\bar{k}$-morphism $s : \operatorname{Spec} \bar{k}
\to \bar{G}$ whose image is $x$; right translation $r_{s}$ then induces an isomorphism from $O_{\bar{G},\bar{e}} =
O_{G,e} \otimes_{k} \bar{k}$ onto $O_{\bar{G},x}$, whence assertion (1).

<!-- original page 295 -->

Let us prove assertion (2). By SGA 1, II.2.1, one reduces immediately to the case where $A$ is a field ($A = k$). The
implications (i) ⇒ (i bis), (ii) ⇒ (ii bis), (ii) ⇒ (i) and (ii bis) ⇒ (i bis) are obvious, so it suffices to prove that
(i bis) implies (ii).

Now, it follows from (i bis) that $O_{G,e} \otimes_{k} \bar{k}$ is reduced. Hence, by (1), $O_{\bar{G},x}$ is reduced
for every closed point $x$ of `Ḡ`, so that `Ḡ` is reduced. Then, since `Ḡ` is locally of finite type over $\bar{k}$,
there exists at least one closed point $y$ such that $O_{\bar{G},y}$ is regular. Since, by (1), the local rings of the
closed points of `Ḡ` are all isomorphic to $O_{\bar{G},\bar{e}}$, one sees that all these local rings are regular, so
that `Ḡ` is smooth over $\bar{k}$, and hence $G$ is smooth over $k$.

[^N.D.E-VI_A-15] One may now give the examples below, signalled by M. Raynaud, of group schemes $G$ over a non-perfect
field $k$ such that $G_{red}$ is not a group scheme over $k$.

**Examples 1.3.2.** *Let $k$ be a non-perfect field of characteristic $p > 0$, $t \in k - k^{p}$, $\bar{k}$ an algebraic
closure of $k$, and $\alpha \in \bar{k}$ such that $\alpha^{p} = t$.*

<!-- label: III.VI_A.1.3.2 -->

*(1) Consider the additive group $G_{a,k} = \operatorname{Spec} k[X]$, and let $G$ be the group subscheme, finite over
$k$, defined by the additive polynomial $X^{p^{2}} - tX^{p}$. Then*

```text
G_red = Spec k[X]/X(X^{p(p−1)} − t)
```

*is étale at the origin. If it were a group scheme over $k$, it would be smooth (by 1.3.1); but $G_{red}$ is not
geometrically reduced, so it is not a group scheme over $k$.*

*(2) Consider $G^{4}_{a,k} = \operatorname{Spec} k[X, Y, U, V]$ and let $G$ be the group subscheme defined by the ideal
$I$ generated by the additive polynomials $P = X^{p} - tY^{p}$ and $Q = U^{p} - tV^{p}$. Then $G$ is of dimension 2 and
irreducible, since $(G_{\bar{k}})_{red} \cong \operatorname{Spec} \bar{k}[Y, V]$ is.*

Let $A = k[X, Y, U, V]$ and $\mathfrak{m}$ its augmentation ideal. Denote by `x, y, u, v` the images of `dX, dY, dU, dV`
in $\Omega^{1}_{A/k} \otimes_{A} (A/\mathfrak{m})$, viewed as linear forms on the tangent space $k^{4} = T_{0}
G^{4}_{a,k}$. Let us show that the subspace $E = T_{0} G_{red}$ equals $k^{4}$. Otherwise, there would exist a linear
form $f = ax + by + a'u + b'v$, with $a, b, a', b' \in k$ not all zero, vanishing on $E$. Recall that the formation of
$\Omega^{1}_{A/k}$ (and hence of tangent spaces) commutes with base change (cf. EGA IV_4, 16.4.5), and identify $f$ with
its image in $(\bar{k}^{4})*$. Since $(G_{\bar{k}})_{red} \subset (G_{red})_{\bar{k}}$, then $f$ vanishes on the
subspace $T_{0} (G_{\bar{k}})_{red}$ of $\bar{k}^{4}$, which is defined by the equations $g_{1} = x - \alpha y$ and
$g_{2} = u - \alpha v$, and so `f = λg_1 + µg_2`, with `λ, µ ∈ k̄`. Now `λg_1 + µg_2` belongs to $k^{4}$ only if
`λ = µ = 0`! This contradiction shows that $E = k^{4}$, and so $T_{0} (G_{red})_{\bar{k}} = \bar{k}^{4}$.

On the other hand, $R = XV - YU$ belongs to $\sqrt{I}$, since $R^{p} = (X^{p} - tY^{p})V^{p} - Y^{p}(U^{p} - tV^{p})$.
Consequently, the tangent space $F$ at the point $(\alpha, 1, \alpha, 1)$ of $(G_{red})_{\bar{k}}$ is contained in the
hyperplane $H$ of $\bar{k}^{4}$ with equation $\alpha dV + dX - dU - \alpha dY = 0$, hence is of dimension $\leq
3$.[^N.D.E-VI_A-16] Therefore, by point (1) of 1.3.1, $G_{red}$ is not a group scheme over $k$.

## 2. Connected components of an $A$-group locally of finite type

<!-- label: III.VI_A.2 -->

<!-- original page 296 -->

### 2.1

Let us first consider an arbitrary $A$-group $G$, and let $G'$ be the connected component of the origin $e$ of $G$. This
connected component is evidently closed, so that we may identify it with the reduced closed subscheme of $G$ having $G'$
as underlying space.[^N.D.E-VI_A-17]

**Proposition 2.1.1.** *For every extension $K$ of the residue field $k$ of $A$, $G' \otimes_{A} K$ has as underlying
space the connected component of the origin in the $K$-group $G \otimes_{A} K$ (i.e. $G'$ is geometrically connected).*

<!-- label: III.VI_A.2.1.1 -->

Indeed, let $(G \otimes_{A} K)'$ be the connected component of the origin in $G \otimes_{A} K$. Since the image of $(G
\otimes_{A} K)'$ in $G$ is connected and contains the unit element of $G$, this image is contained in $G'$, so that $(G
\otimes_{A} K)'$ is contained in the inverse image

<!-- original page 300 -->

$G' \otimes_{A} K$ of $G'$ in $G \otimes_{A} K$. The proposition therefore follows from the connectedness of $G'
\otimes_{A} K$, which is proved in Lemma 2.1.2.

**Lemma 2.1.2.** *Let $X$ and $Y$ be two connected schemes over a field $k$. If $X$ contains a rational point, then $X
\times_{k} Y$ is connected.*

<!-- label: III.VI_A.2.1.2 -->

We give below a direct proof of this result from EGA IV_2 (4.5.8 and 4.5.14).

Suppose first $Y$ non-empty, connected and affine, with algebra $B$. In this case, $X \times_{k} Y$ is the spectrum of
the quasi-coherent `O_X`-algebra $\mathcal{B} = O_{X} \otimes_{k} B$. We want to show that every subset $U$ of $X
\times_{k} Y$ that is open, closed, and non-empty coincides with $X \times_{k} Y$. Now $U$ is affine over $X$ and its
affine `O_X`-algebra is a direct factor of $\mathcal{B}$. It therefore follows from Lemma 2.1.3 below that the image of
$U$ in $X$ is open and closed,

<!-- original page 297 -->

i.e. coincides with all of $X$. This image contains in particular a rational point $x$ of $X$, so that $U$ meets the
inverse image of $x$ in $X \times_{k} Y$. Since this inverse image is isomorphic to $Y$, hence connected, $U$ contains
this inverse image. The same would hold for the complement of $U$ in $X \times_{k} Y$ if $U$ were distinct from $X
\times_{k} Y$, which would be absurd.

If $Y$ is now an arbitrary $k$-scheme, what precedes shows that the fibers of the canonical projection $X \times_{k} Y
\to Y$ are connected. If $x$ is a rational point of $X$, these fibers all meet the subscheme ${x} \times_{k} Y$, which
is itself connected, whence the proposition.

**Lemma 2.1.3.** *Let $X$ be a scheme and $\mathcal{A}$ a quasi-coherent `O_X`-algebra which is locally[^N.D.E-VI_A-18]
a direct factor of a free `O_X`-module. The image of $\operatorname{Spec} \mathcal{A}$ in $X$ is then open and closed.*

<!-- label: III.VI_A.2.1.3 -->

Let $V$ be this image. It is clear that $V$ is contained in the support of $\mathcal{A}$. Conversely, if $x$ belongs to
the support of $\mathcal{A}$, then $\mathcal{A}_{x}$ is non-zero and is a free $O_{X,x}$-module, since by Kaplansky
every projective module over a local ring is free. Consequently the fiber of $\operatorname{Spec} \mathcal{A}$ at $x$,
which is affine with algebra $\mathcal{A}_{x} \otimes_{O_{X,x}} \kappa(x)$, is non-empty. One thus sees that the image
of $\operatorname{Spec} \mathcal{A}$ coincides with the support of $\mathcal{A}$.

If $s$ is the unit section of $\mathcal{A}$, the equality $s_{x} = 0$ implies that $s$, and hence $\mathcal{A}$, are

<!-- original page 298 -->

zero in a neighborhood of $x$. So the support of $\mathcal{A}$ is closed. On the other hand, one may assume that
$\mathcal{A}$ is a direct factor of the direct sum $L$ of a family $(O^{\alpha}_{X})$ of copies of
`O_X`.[^N.D.E-VI_A-19] For every $\beta$, write $\phi_{\beta}$ for the restriction to $\mathcal{A}$ of the canonical
projection of $L = \oplus_{\alpha} O^{\alpha}_{X}$ onto $O^{\beta}_{X}$. For $x \in X$, denote by $\mathcal{A}^{*}_{x}$
the dual module $\operatorname{Hom}_{O_{X,x}}(\mathcal{A}_{x}, O_{X,x})$. Since $\mathcal{A}_{x}$ is a direct factor of
$L_{x}$, the restriction map

```text
Hom_{O_{X,x}}(L_x, O_{X,x}) → Hom_{O_{X,x}}(𝓐_x, O_{X,x}) = 𝓐_x^*
```

<!-- original page 299 -->

is surjective. If $\mathcal{A}_{x} \neq 0$ then, since $\mathcal{A}_{x}$ is free and non-zero, there exist $a \in
\mathcal{A}_{x}$ and a linear form $\phi \in \mathcal{A}^{*}_{x}$ such that $\phi(a) = 1$. There exists therefore a
family $(\xi^{\alpha})$ of elements of $O_{X,x}$ such that, for every $u \in \mathcal{A}_{X,x}$, one has $\phi(u) =
\sum_{\alpha} \xi^{\alpha} \phi^{\alpha}(u)$ (this sum being finite since $\phi^{\alpha}(u) = 0$ except for finitely
many $\alpha$). Applying this to $u = a$, one obtains that there exist $\alpha_{1}, \cdots, \alpha_{n}$ such that

```text
1 = φ(a) = ξ^{α_1} φ^{α_1}(a) + ⋯ + ξ^{α_n} φ^{α_n}(a).
```

There exists then an open neighborhood $U$ of $x$ such that $a$ and the $\xi^{\alpha_{i}}$ come from sections $\tilde{a}
\in \mathcal{A}(U)$ and $\tilde{\xi}^{\alpha_{i}} \in O_{X}(U)$, and the equality $\sum_{i} \tilde{\xi}^{\alpha_{i}}
\phi^{\alpha}(\tilde{a}) = 1$ on $U$ shows that $\tilde{a}_{y} \neq 0$ for every $y \in U$. ("The support of a
projective module is open.")

### 2.2

The notations being still those of 2.1, it is clear that $G'$ is a reduced $k$-scheme. Lemma 2.1.2 shows that $G'
\times_{k} G'$ is connected, so that $(G' \times_{k} G')_{red}$ is the reduced subscheme of $G \times_{A} G$ having as
underlying space the connected component of the origin. In particular, the multiplication morphism `µ : G ×_A G → G`
induces a morphism `µ′ : (G′ ×_k G′)_red → G′` that makes $G'$ a group in $(Sch/k)_{red}$.

### 2.2.bis

[^N.D.E-VI_A-20] One recalls (cf. Exp. V) that, if $P$ is a scheme, one writes $P$ for the underlying topological space
of $P$. Now one defines a sub-$A$-functor $G^{0}$ of $G$ by setting, for every $A$-scheme $S$,

```text
G⁰(S) = {u ∈ G(S) | u(S) ⊂ G′}.
```

Let $c : G \to G$ be the inversion morphism; since $c(G') = G'$, we have $c \circ u \in G^{0}(S)$ for every $u \in
G^{0}(S)$. On the other hand, if $u, v \in G^{0}(S)$, then $u \boxtimes v$ sends $S$ into the subspace of $G \times_{A}
G$ consisting of points whose two projections belong to $G'$; this subspace is identified with the underlying space of
$G' \times_{A} G'$, which is connected by Lemma 2.1.2. Consequently, `µ ∘ (u ⊠ v)` sends $S$ into $G'$. This shows that
$G^{0}$ is a sub-$A$-functor in groups of $G$.

If the connected component of $e$ is open in $G$, then the subfunctor $G^{0}$ is representable by the subscheme induced
by $G$ on this open set, which is therefore a group subscheme of $G$; we shall also write $G^{0}$ for it. In this case,
with the notations of 2.1, one has $G' = (G^{0})_{red}$ and the topological spaces $G'$ and $G^{0}$
coincide.[^N.D.E-VI_A-21]

### 2.3

In accordance with our conventions of 1.1, we again assume from now on that $G$ is locally of finite type over $A$. Then
$G$ is locally noetherian, hence locally connected,[^N.D.E-VI_A-22] hence: every connected component of $G$ is open.

We then write $G^{0}$ for the subscheme induced by $G$ on the connected component $G'$ of the unit element. By 2.2.bis,
$G^{0}$ is a group subscheme of $G$, which we shall call the *neutral component* of $G$;

<!-- original page 300 -->

for every $A$-scheme $S$ we therefore have:

```text
G⁰(S) = {u ∈ G(S) | u(S) ⊂ G⁰ = G′}.
```

Let $G^{\alpha}$ be an arbitrary connected component of $G$ and $\nu^{\alpha} : G^{\alpha} \times_{A} G^{0} \to G$ the
morphism defined by the equalities

$$ \nu^{\alpha}(S)(g, \gamma) = g\gamma g^{-1}, $$

for every $S \in (Sch/A)$, $g \in G^{\alpha}(S)$, $\gamma \in G^{0}(S)$.

If $e$ is the origin of $G$, the restriction of $\nu^{\alpha}$ to $G^{\alpha} \times_{A} {e}$ is the trivial morphism;
since $G^{\alpha} \times_{A} G^{0}$ is connected by 2.1.2, one sees that $\nu^{\alpha}$ factors through $G^{0}$.
Therefore, for every $A$-scheme $S$, $G^{0}(S)$ is a normal subgroup of $G(S)$. We have thus obtained the following
proposition:[^N.D.E-VI_A-23]

**Proposition 2.3.1.** *Let $G$ be an $A$-group locally of finite type. Then the neutral component $G^{0}$ is an open
normal group subscheme of $G$.*

<!-- label: III.VI_A.2.3.1 -->

**Proposition 2.4.** *Let $G$ be an $A$-group locally of finite type.*

*(i) $G^{0}$ is irreducible, and $G^{0} \otimes_{A} k$ is geometrically irreducible over $k$.*

*(ii) $G^{0}$ is quasi-compact, hence of finite type over $A$.*

<!-- label: III.VI_A.2.4 -->

[^N.D.E-VI_A-24] *Proof.* (i) Since $G^{0}$ and $G^{0} \otimes_{A} k$ have the same underlying topological space, it
suffices to show the second assertion. Let $\bar{k}$ be an algebraic closure of $k$. By 2.2, $(G \otimes_{A}
\bar{k})_{red}$ is a $\bar{k}$-group locally of finite type and reduced, hence smooth over $\bar{k}$ (1.3.1). A fortiori
the local rings of $(G \otimes_{A} \bar{k})_{red}$ are integral domains, so,[^N.D.E-VI_A-25] since $G \otimes_{A}
\bar{k}$ is locally noetherian, the connected components of $G \otimes_{A} \bar{k}$ are irreducible (cf. EGA I, 6.1.10).
In particular, the connected component $G^{0} \otimes_{A} \bar{k}$ (cf. 2.1.1) is irreducible.

(ii) Let us now show that $G^{0}$ is of finite type over $A$. Since $G^{0}$ is locally of finite type over $A$, it
suffices to prove that $G^{0}$ is quasi-compact. As $G^{0}$ is irreducible, this follows from 0.5.1.

<!-- original page 301 -->

**Corollary 2.4.1.** *Every connected component of $G$ is irreducible,[^N.D.E-VI_A-26] of finite type over
$A$,[^N.D.E-VI_A-27] and of the same dimension as $G^{0}$.*

<!-- label: III.VI_A.2.4.1 -->

One may indeed assume $A$ equal to its residue field $k$. Let then $C$ be a connected component of $G$, $x$ a closed
point of $C$, $\kappa(x)$ the residue field of $x$, and $k'$ a normal extension of $k$ containing $\kappa(x)$ and of
finite degree over $k$. The canonical projection $\pi : C \otimes_{k} k' \to C$ is open and closed;[^N.D.E-VI_A-28]
consequently, if $C'$ is a connected component of $C \otimes_{k} k'$, the projection $C' \to C$ is surjective, so $C'$
contains a point $y \in \pi^{-1}(x)$, and such a point is rational over $k'$ (cf. the proof of 1.2), so that $C'$ is the
image by translation $r_{y}$ of $G^{0} \otimes_{k} k'$. Now $G^{0} \otimes_{k} k'$ is of finite type over $k'$ by 2.4,
and $\pi^{-1}(x)$ is finite (of cardinality $\leq [k' : k]$), so $C \otimes_{k} k'$ is of finite type over $k'$, and
hence $C$ is of finite type over $k$.

On the other hand, since $G^{0} \otimes_{k} k'$ is irreducible by 2.4, the same holds for $C'$,[^N.D.E-VI_A-29] and
hence also for $C$, since the projection $C' \to C$ is surjective.

Finally, we have seen above that $C \otimes_{k} k'$ is a disjoint union of finitely many translates of $G^{0}
\otimes_{k} k'$. Since dimension is invariant under extension of the base field (cf. EGA IV_2, 4.1.4), it follows that
$C$ has the same dimension as $G^{0}$. (Moreover, by EGA IV_2, 5.2.1, one has $\dim_{g} G = \dim G^{0}$ for every point
$g \in G$.)

### 2.5

This paragraph has been added. The results that follow appear in Exp. VI_B, but could (or should) have figured in VI_A,
and it is useful to have them available from now on, in order to make precise Theorem 3.2 below.

**Lemma 2.5.1.** *Let $(A, \mathfrak{m})$ be an Artinian local ring, and $k = A/\mathfrak{m}$ its residue field.*

*(i) If $X$ is an $A$-scheme such that $X \otimes_{A} k$ is locally of finite type (resp. of finite type) over $k$, then
the same holds for $X$ over $A$.*

*(ii) Let $u : X \to Y$ be a morphism of $A$-schemes. If $u \otimes_{A} k$ is an immersion (resp. a closed immersion),
then so is $u$.*

<!-- label: III.VI_A.2.5.1 -->

*Proof.* (i) Suppose $X \otimes_{A} k$ locally of finite type over $k$. Let $U = \operatorname{Spec} B$ be an affine
open of $X$. By hypothesis, there exist elements $x_{1}, \cdots, x_{n}$ of $B$ whose images generate $B/\mathfrak{m}B$
as a $k$-algebra, and it follows from the "nilpotent Nakayama lemma" that the $x_{i}$ generate $B$ as an $A$-algebra.
This proves that $X$ is locally of finite type over $A$. If, in addition, $X \otimes_{A} k$ is quasi-compact, then so is
$X$ (which has the same underlying topological space), and hence $X$ is of finite type over $A$. This proves (i).

Let us prove (ii). Suppose $u \otimes_{A} k$ is an immersion (resp. a closed immersion). Then $u$ is a homeomorphism of
$X$ onto a locally closed (resp. closed) part of $Y$, and for every $x \in X$, the ring morphism $\phi_{x} : O_{Y,u(x)}
\to O_{X,x}$ is such that $\phi_{x} \otimes_{A} k$ is surjective. By the nilpotent Nakayama lemma, it follows that
$\phi_{x}$ is surjective, so $u$ is an immersion (resp. a closed immersion).

**Proposition 2.5.2.** *Let $A$ be an Artinian local ring with residue field $k$, and let $u : G \to H$ be a
quasi-compact morphism between $A$-group schemes locally of finite type.*

*(a) The set $u(G)$ is closed in $H$, and its connected components are irreducible and all of the same dimension.*

*(b) One has `dim G = dim u(G) + dim Ker(u)`.*

*(c) If $u$ is a monomorphism, it is a closed immersion.*

<!-- label: III.VI_A.2.5.2 -->

*Proof.* By the preceding lemma, it suffices to prove the proposition in the case where $A = k$. Moreover, since the
properties under consideration are stable by

<!-- original page 304 -->

(fpqc) descent, and since dimension is invariant under extension of the base field, one may assume $k$ algebraically
closed.

Let us prove (a). Denote by $C$ the reduced subscheme of $H$ whose underlying topological space is $u(G)$. Since $u(G)$
is stable under the inversion morphism of $H$, so is $C$. On the other hand, $u : G \to C$ is quasi-compact and
dominant, so by EGA IV_2, 2.3.7 the same holds for $u \times_{k} id_{G}$ and $id_{H} \times_{k} u$, and hence for their
composition $u \times_{k} u : G \times_{k} G \to C \times_{k} C$. Consequently, the multiplication of $H$ sends $C
\times_{k} C$ into $C$, and so $C$ is a group subscheme of $H$.

So, replacing $H$ by $C$, we reduce to the case where $u$ is dominant. Then $G(k)$ is dense in $H$, hence meets every
connected component of $H$, and hence acts transitively on the set of these connected components. It therefore suffices
to show that $u(G)$ contains $H^{0}$. Replacing $G$ by $u^{-1}(H^{0})$, we may suppose $H = H^{0}$; in this case, by
2.4, $H$ is irreducible and of finite type over $k$, hence noetherian. On the other hand, $u$ is locally of finite type
(cf. EGA I, 6.6.6) and quasi-compact, hence of finite type. Consequently, by Chevalley's constructibility theorem (cf.
EGA IV_1, 1.8.5), $u(G)$ is a constructible (and dense) part of $H = u(G)$, hence contains a dense open $U$ of $H$ (cf.
EGA 0_III, 9.2.2). Then, by 0.5, one has $H = U \cdot U \subset u(G)$, whence $u(G) = H$. Taking 2.4.1 into account,
this proves assertion (a).

Let us prove (b). Recall first that the functor $Ker(u)$ (cf. I, 2.3.6.1) is representable by $u^{-1}(e)$, where $e$
denotes the unit element of $H$. Since $u$ is of finite type, $Ker(u)$ is of finite type over $k$. On the other hand,
replacing $H$ by the reduced closed subscheme $u(G)$, we may assume $u$ surjective. Denote by $u^{0}$ the restriction of
$u$ to $G^{0}$. Since $G$ and $Ker(u)$ are equidimensional, and since $Ker(u)^{0} \subset Ker(u^{0})$, we reduce to the
case where $G$, and hence also $H$, are irreducible.

Then, by EGA IV_3, 9.2.6.2 and 10.6.1 (ii), the set of $y \in H$ such that `dim u⁻¹(y) = dim G − dim H` contains a
non-empty open set $V$. Since $u$ is surjective, $U = u^{-1}(V)$ is then a non-empty open subset of $G$, hence contains
a closed point $x$ of $G$, since $G$ is a Jacobson scheme (cf. EGA IV_3, 10.4.8). Then right translation $r_{x}$ is an
isomorphism of $Ker(u)$ onto $u^{-1}(u(x))$, whence:

```text
dim Ker(u) = dim u⁻¹(u(x)) = dim G − dim H.
```

Let us prove (c), following [DG70], I, § 3.4. (Another proof is given in Exp. VI_B, 1.4.2.) Assume $u$ a monomorphism.
If $C$ is a connected component of $G$, there exists a closed point $x \in G$ such that $C = r_{x}(G^{0})$, and if one
denotes by $u_{C}$ (resp. $u^{0}$) the restriction of $u$ to $C$ (resp. to $G^{0}$), one has $u_{C} = r_{u(x)} \circ
u^{0} \circ r^{-1}_{x}$, so it suffices to show that $u^{0}$ is a closed immersion. We may therefore suppose $G =
G^{0}$, so that $G$ is irreducible and of finite type over $k$.

Let $\xi$ be the generic point of $G$; then $O_{G,\xi}$ is an Artinian local ring; denote by $\mathfrak{m}$ its maximal
ideal. On the other hand, let $h = u(\xi)$, $\mathfrak{n}$ the maximal ideal of $O_{H,h}$, and $A =
O_{G,\xi}/\mathfrak{n} O_{G,\xi}$. Since $u$ is a monomorphism, so is the morphism $u_{h} : \operatorname{Spec}(A) \to
\operatorname{Spec}(\kappa(h))$ obtained by base change, so the multiplication morphism $A \otimes_{\kappa(h)} A \to A$
is an isomorphism (cf. EGA I, 5.3.8), whence $A = \kappa(h)$. By Nakayama's lemma (since $\mathfrak{n} O_{G,\xi}$ is
contained in $\mathfrak{m}$, hence nilpotent), it follows that the morphism $O_{H,h} \to O_{G,\xi}$ is surjective.

<!-- original page 305 -->

Let then $V$ be an affine open of $H$ containing $h$, $U$ a non-empty affine open of $G$ contained in $u^{-1}(V)$,
$\phi : O_{H}(V) \to O_{G}(U)$ the morphism of $k$-algebras induced by $u$, $\mathfrak{p}$ the prime ideal of $O_{G}(U)$
corresponding to $\xi$, and $\mathfrak{q} = \phi^{-1}(\mathfrak{p})$. Since $G$ is of finite type over $k$, $O_{G}(U)$
is generated as a $k$-algebra by a finite number of elements $a_{1}, \cdots, a_{n}$. By what precedes, there exist
elements $b_{1}, \cdots, b_{n}$ and $s$ in $O_{H}(V)$ such that $s \notin \mathfrak{q}$ and such that one has in
$O_{G}(U)_{\mathfrak{p}}$ the equalities $a_{i}/1 = \phi(b_{i})/\phi(s)$. There exist therefore elements
$t_{1}, \cdots, t_{n}$ of $O_{G}(U) - \mathfrak{p}$ such that $t_{i}(a_{i} \phi(s) - \phi(b_{i})) = 0$. Then, setting
$t = t_{1} \cdots t_{n} \phi(s) \in O_{G}(U) - \mathfrak{p}$, the equalities $a_{i}/1 = \phi(b_{i})/\phi(s)$ already
hold in $O_{G}(U)_{t}$ and, since $t \in O_{G}(U) = k[a_{1}, \cdots, a_{n}]$, there exists $b \in O_{H}(V)$ such that
$t/1 = \phi(b)/\phi(s)^{r}$, for some $r \in \mathbb{N}$. Consequently, $\phi$ induces a surjection of $O_{H}(V)_{sb}$
onto $O_{G}(U)_{t}$, and so $u$ is a local immersion at the point $\xi$.

The open subset $W$ of $G$ consisting of the points at which $u$ is a local immersion is therefore non-empty. Since $G$
is a Jacobson scheme, $W$ contains a closed point $y$, and to show $W = G$, it suffices to show that every closed point
of $G$ belongs to $W$. Now every closed point $x$ is the image of $y$ by translation $r_{x} \circ r^{-1}_{y}$, hence
belongs to $W$, whence $W = G$. This proves that $u$ is a local immersion.

Since $G$ is irreducible, it follows that $u$ is an immersion. Indeed, for every $x \in G$, let $U_{x}$ and $V_{x}$ be
open subsets of $G$ and $H$ such that $x \in U_{x}$ and such that $u$ induces a closed immersion of $U_{x}$ into
$V_{x}$. Since $U_{x}$ is dense in $G$, $u(U_{x})$ is dense in $u(G) \cap V_{x}$, and since $u(U_{x})$ is closed in
$V_{x}$, one has $u(U_{x}) = V_{x}$. Moreover, since $u$ is injective, one has $U_{x} = u^{-1}(V_{x})$, and it follows
that $u$ induces a closed immersion of $G$ into the open subscheme of $H$ covered by the $V_{x}$. So $u : G \to H$ is an
immersion. But we have already seen that $u(G)$ is closed in $H$, hence $u$ is a closed immersion.

**Lemma 2.5.3.** [^N.D.E-VI_A-30] *Let $A$ be an Artinian local ring, $k$ its residue field, $G$ a flat $A$-group, $X$
an $A$-scheme equipped with a left action `µ : G ×_A X → X` of $G$ and with a section $s_{0} : \operatorname{Spec} A \to
X$. (This is the case, for instance, if $G'$ is a second $A$-group and one is given an $A$-group morphism $G \to G'$.)*

*Let $\phi$ be the morphism `µ ∘ (id_G × s_0)` from $G = G \times_{A} A$ to $X$. If $\phi$ is flat at a point $g$ of
$G$, then $\phi$ is flat.*

<!-- label: III.VI_A.2.5.3 -->

*Proof.* Since $G$ is flat over $A$, the flatness-by-fibers criterion (EGA IV_3, 11.3.10.2) shows that it suffices to
show that $\phi \otimes_{A} k$ is flat; hence we may suppose $A = k$. In this case, the datum of $s_{0}$ is equivalent
to that of a $k$-point $x_{0} \in X(k)$, and $\phi$ is the morphism $h \mapsto h x_{0}$.

Let then $h \in G$; let us show that $\phi$ is flat at the point $h$. Let $K$ be an extension of $k$ containing a copy
of $\kappa(g)$ and of $\kappa(h)$; one has a cartesian square

```text
            φ_K
G_K ────────────→ X_K
 │                 │
 │                 │
 ▼      φ          ▼
 G ────────────→ X
```

<!-- original page 306 -->

in which the two vertical arrows are faithfully flat. So, by V 7.4 (i), $\phi_{K}$ is flat at every point $g' \in G_{K}$
above $g$, and to show that $\phi$ is flat at $h$, it suffices to show that $\phi_{K}$ is flat at a point $h'$ above
$h$. We are thus reduced to the case where $g$ and $h$ are rational. Let then $u = h g^{-1}$ and $\ell_{u}$ (resp.
`µ_u`) the left translation of $G$ (resp. of $X$) defined by $u$; since `φ ∘ ℓ_u = µ_u ∘ φ`, one obtains a commutative
square

```text
                ~
O_{G,h} ──────────→ O_{G,g}
    ▲                  ▲
    │                  │
    │       ~          │
O_{X, hx_0} ────→ O_{X, gx_0}
```

in which the horizontal arrows are isomorphisms. Since the morphism $O_{X, gx_{0}} \to O_{G,g}$ is flat, the morphism
$O_{X, hx_{0}} \to O_{G,h}$ is also flat.

**Proposition 2.5.4.** *Let $A$ be an Artinian local ring, $k$ its residue field, $G$ an $A$-group locally of finite
type, $X \neq \emptyset$ an $A$-scheme locally of finite type equipped with a left action of $G$. Assume that the
morphism $\phi : G \times_{A} X \to X \times_{A} X$ defined set-theoretically by $(g, x) \mapsto (gx, x)$ is surjective.
Then:*

*(i) The connected components of $X$ are of finite type, irreducible, and all of the same dimension.*

*(ii) More precisely, let $\bar{k}$ be an algebraic closure of $k$ and $x$ a closed point of $X \otimes_{A} \bar{k}$;
its stabilizer $F$ is a closed group subscheme of $G \otimes_{A} \bar{k}$, and the dimension of the irreducible
components of $X$ is $\dim G - \dim F$.*

<!-- label: III.VI_A.2.5.4 -->

Taking Lemma 2.5.1 into account, we may suppose $A = k$. Suppose first $k$ algebraically closed. Then $G_{red}$ is a
$k$-group locally of finite type, and hence, replacing $G$ by $G_{red}$ and $X$ by $X_{red}$, we may suppose $G$ and $X$
reduced.

Since $G \times_{k} X$ is locally of finite type over $k$, $\phi$ is locally of finite type (cf. EGA I, 6.6.6 (v)),
hence locally of finite presentation since $X \times_{k} X$ is locally noetherian. Let $x$ be a rational point of $X$;
then the morphism $\phi_{x} : G \to X$ obtained from $\phi$ by base change is surjective and locally of finite
presentation. If $\eta$ is a maximal point of $X$, then $O_{X,\eta}$ is a field (since $X$ is reduced), so $\phi_{x}$ is
flat at every point of $G$ above $\eta$. So, by Lemma 2.5.3, $\phi_{x}$ is flat. Consequently, $\phi_{x} : G \to X$ is
faithfully flat and locally of finite presentation, hence open (cf. EGA IV_2, 2.4.6). Since $G^{0}$ is open in $G$,
irreducible and quasi-compact (by 2.4), each orbit $G^{0} x = \phi_{x}(G^{0})$, for $x$ running through the rational
points of $X$, is an open subset of $X$, irreducible and quasi-compact, hence of finite type over $k$ (since $X$ is
locally of finite type over $k$).

Since every non-empty open subset of $X$ contains a rational point, it follows that $X$ is covered by these open sets.
Moreover, two such open sets are either disjoint or equal. Indeed, if $\phi_{x}(G^{0}) \cap \phi_{y}(G^{0})$ is
non-empty, it contains a rational point $z$, and there exist therefore two rational points $g, h \in G^{0}$ such that
$gx = z = hy$, whence $x = g^{-1}z$ and $y = h^{-1}z$, and so $\phi_{x}(G^{0}) = \phi_{z}(G^{0}) = \phi_{y}(G^{0})$. It
follows that the orbits $\phi_{x}(G^{0})$ are also closed, and so are at once the connected components and the
irreducible components of $X$.

<!-- original page 307 -->

Finally, let `x, y` be two rational points of $X$. Since $\phi_{x}$ is surjective, there exists a rational point $g \in
G$ such that $y = gx$, and since $G^{0}$ is a normal subgroup of $G$, the orbit $G^{0} y$ is the image of $G^{0}$ under
translation $\ell_{g}$ of $X$, so that $G^{0} y$ and $G^{0} x$ have the same dimension.

Moreover, by I, 2.3.3.1, the stabilizer of $x$ is represented by the closed subscheme $F$ of $G$ defined by the
cartesian square below:

```text
F ─────────→ G
│            │
│            │ φ_x
▼            ▼
Spec k ────→ X.
```

Then $F$ is a $k$-group locally of finite type, $F \cap G^{0}$ is a $k$-group of finite type containing $F^{0}$, and by
2.4.1, $F$ and $F \cap G^{0}$ are equidimensional, of the same dimension as $F^{0}$. Let $C = \phi_{x}(G^{0})$ be the
irreducible component of $X$ containing $x$. Proceeding as in the proof of point (b) of 2.5.2, one obtains that
`dim C = dim G⁰ − dim F⁰ = dim G − dim F`.

In the general case (i.e. for $k$ an arbitrary field), let $\bar{k}$ be an algebraic closure of $k$. Let $C$ be a
connected component of $X$ and $C'$ a connected component of $C \otimes_{k} \bar{k}$; then $C'$ is a connected component
of $X' = X \otimes_{k} \bar{k}$. The morphism $\pi : X' \to X$ is open (cf. EGA IV_2, 2.4.10), and since it is integral,
it is also closed; consequently $\pi(C') = C$. Since $C'$ is irreducible and quasi-compact, $C$ is irreducible and
quasi-compact, hence of finite type over $k$ (since $X$ is locally of finite type over $k$).

Finally, since dimension is invariant under extension of the base field (cf. EGA IV_2, 4.1.4), $\dim C = \dim C'$, and
since all the irreducible components of $X'$ have the same dimension, the same holds for those of $X$.

### 2.6. Complements

This paragraph has been added, drawn from [Per75] II, §§ 1–2, with complements due to O. Gabber.[^N.D.E-VI_A-31] This
shows that the preceding results are valid for any group scheme $G$ over a field $k$. (This will be used in sections 5,
6 and 7 of Exp. VI_B.)

We fix a field $k$. Let us begin with the following lemma (loc. cit., II 2.1.1), which does not appear explicitly in EGA
IV_2, § 4.4 (although it can perhaps be read between the lines at the beginning of loc. cit., § 4.4.1).

**Lemma 2.6.0.** *Let $X$ be an irreducible $k$-scheme, $K$ an extension of $k$, $X'$ an irreducible component of `X_K`.
The projection $X' \to X$ is surjective.*

<!-- label: III.VI_A.2.6.0 -->

Indeed, let $B$ be a transcendence basis of $K$ over $k$ and $L = k(B) \subset K$. By EGA IV_2, 4.3.2 and 4.4.1, `X_L`
is irreducible and $X'$ dominates `X_L`. The morphism $X' \to X_{L}$ is therefore integral and dominant, hence
surjective. Since $X_{L} \to X$ is surjective (loc. cit., 4.4.1), so is $X' \to X$.

<!-- original page 308 -->

For the rest of 2.6, we fix a $k$-group scheme $G$ and an action `µ : G × X → X` of $G$ on a $k$-scheme $X$ satisfying
the following condition:

```text
(⋆)    the morphism Φ : G × X → X × X, (g, x) ↦ (gx, x) is surjective
```

(this is the case in particular for $G$ acting on itself by left translations). We shall then say, for short: "Let $X$
be a $G$-scheme satisfying (⋆)". Finally, we write $k'$ for the perfect closure of $k$.

**Proposition 2.6.1.** *Let $X$ be a $G$-scheme satisfying $(\star)$.*

*(i) $X$ is geometrically pointwise irreducible over $k$, i.e. for every extension $K$ of $k$, each $x \in X_{K}$
belongs to a unique irreducible component of `X_K`.*

*(ii) Each local ring of $(X_{k'})_{red}$ is normal.*

*(iii) Let $\eta$ be a maximal point of $(X_{k'})_{red}$, $C = {\eta}^{-}$, and $L$ the algebraic closure of $k$ in
$\kappa(\eta)$. Then $C$ is an $L$-scheme, and is geometrically irreducible over $L$ (i.e. $C \otimes_{L} K$ is
irreducible for every extension $K$ of $L$).*

*(iv) In particular, if $x$ is a rational point of $X$, then the irreducible component of $X$ containing $x$ is
geometrically irreducible over $k$.*

<!-- label: III.VI_A.2.6.1 -->

*Proof.* (i) Since hypothesis $(\star)$ is preserved by every base change $k \to K$, it suffices to show that each $x
\in X$ belongs to a unique irreducible component of $X$. Since the morphism $\operatorname{Spec}(k') \to
\operatorname{Spec}(k)$ is a universal homeomorphism, we may moreover assume $k$ perfect. We may then assume $G$ and $X$
reduced. Let $\eta$ be a maximal point of $X$ and $z$ an arbitrary point of $Z = {\eta}^{-}$. Since $X$ is reduced, the
local ring $O_{X,\eta}$ equals $\kappa(\eta)$, and since $k$ is perfect, for every extension $K$ of $k$, $\kappa(\eta)
\otimes_{k} K$ is normal (cf. EGA IV_2, 6.14.2), so every point of `X_K` above $\eta$ is normal.

Since $\Phi$ is surjective, there exists a point $\gamma$ of $G \times X$ such that $\Phi(\gamma)$ has projections $z$
and $\eta$. Let $K = \kappa(\gamma)$; there exist then rational points $g$ and $\eta'$ of `G_K` and `X_K` such that
$\eta'$ lies above $\eta$ and $z' = g \eta'$ lies above $z$. By what precedes, $\eta'$ is a normal point of `X_K`, hence
so is $z'$. Since $\pi : X_{K} \to X$ is flat, it follows that $z = \pi(z')$ is a normal point of $X$ (cf. EGA IV_2,
2.1.13). This proves (ii) and (i).

The first assertion of (iii) then follows from (ii). Then, since $L$ is algebraically closed in $\kappa(\eta)$, $C$ is
geometrically irreducible over $L$, by EGA IV_2, 4.5.9.

Finally, if $X$ has a rational point $x$, it follows from (iii) that $L = k$, and so $X$ is geometrically irreducible
over $k$. This can also be seen directly as follows (cf. [Per75], II 2.1): let $C$ be the irreducible component of $X$
containing $x$ and let $K$ be an extension of $k$; `X_K` has a unique point $e_{K}$ above $e$, and, by (i), $e_{K}$
belongs to a unique irreducible component $C'$ of `X_K`; on the other hand, by 2.6.0, every irreducible component of
`C_K` contains $e_{K}$, hence equals $C'$.

**Notation.** Let us write provisionally $C^{0}$ for the reduced closed subscheme of $G$ whose underlying space is the
unique irreducible component of $G$ containing the unit element $e$.

<!-- original page 309 -->

**Corollary 2.6.2.** *$C^{0}$ is geometrically irreducible over $k$ and is set-theoretically stable under the group law,
i.e. $(C^{0}_{k'})_{red}$ is a subgroup of $(G_{k'})_{red}$. Consequently, $C^{0}$ is quasi-compact.*

<!-- label: III.VI_A.2.6.2 -->

Indeed, by 2.6.1, $C^{0}$ is geometrically irreducible over $k$, so $C^{0} \times C^{0}$ is irreducible, so $\nu(C^{0}
\times C^{0}) \subset C^{0}$, where $\nu$ denotes the morphism $(g, h) \mapsto gh^{-1}$. Since $\operatorname{Spec} k'
\to \operatorname{Spec} k$ is a universal homeomorphism, the same conclusion holds for $C^{0}_{k'}$, and then for $H =
(C^{0}_{k'})_{red}$, and so, since $H \times_{k'} H$ is reduced, $\nu$ induces a morphism $H \times_{k'} H \to H$, i.e.
$H$ is a subgroup of $(G_{k'})_{red}$. Consequently, by 0.5.1, $H$ (and hence also $C^{0}$) is quasi-compact.

**Recollection 2.6.3.** *Let $Y$ be a scheme. Recall (EGA 0_III, 9.1.1) that a subset $E$ of $Y$ is said to be*
retrocompact *if the inclusion $E \hookrightarrow Y$ is quasi-compact, and that, by EGA IV_1, 1.9.5 (v) and 1.10.1, if
$U$ is a retrocompact open subset of $Y$, then the closure $U^{-}$ of $U$ is the union of the closures ${y}^{-}$ of the
points $y \in U$, and of course it is enough to take $y$ running through the maximal points of $U$, i.e. the maximal
points of $Y$ contained in $U$.*

<!-- label: III.VI_A.2.6.3 -->

*Consequently, if $Y$ is quasi-separated and if $\eta$ is a maximal point of $Y$, then the intersection of the closed
neighborhoods of $\eta$ equals ${\eta}^{-}$: indeed, if $y \in Y - {\eta}^{-}$, then $y$ is contained in an affine open
$V$ not containing $\eta$; since $Y$ is quasi-separated, $V$ is retrocompact, so $V^{-}$ is the union of the
${\xi}^{-}$, for $\xi$ running through the maximal points of $Y$ belonging to $V$, and hence $\eta \notin V^{-}$, i.e.
$Y - V^{-}$ is a closed neighborhood of $\eta$ not containing $y$.*

**Proposition 2.6.4.** *Let $X$ be a $G$-scheme satisfying $(\star)$ and let $U$ be an open subset of $X$.*

*(i) $C^{0} U$ is an open subset of $X$, equal to the union of the irreducible components of $X$ whose generic point
belongs to $U$.*

*(i′) Consequently, if $X$ is irreducible, it is quasi-compact.*

*(ii) If moreover $U$ is retrocompact in $X$, then $C^{0} U$ equals $U^{-}$, hence is an open-and-closed subset of $X$.*

<!-- label: III.VI_A.2.6.4 -->

*Proof.* (i) First, $C^{0} U$ is open, since it is the union, for $g \in C^{0}$, of the projections of the open sets $g
\cdot U_{\kappa(g)} \subset X_{\kappa(g)}$, and each projection $X_{\kappa(g)} \to X$ is open.

To prove the second assertion of (i), we may replace $k$ by $k'$ (since $\operatorname{Spec} k' \to \operatorname{Spec}
k$ is a universal homeomorphism), and so assume $k$ perfect. We may then assume $G$ and $X$ reduced, hence geometrically
reduced.

Let $\eta$ be a maximal point of $X$ contained in $U$ and let $Z$ be its closure. Consider the morphism
`µ′ : C⁰ × Z → X`. Since $C^{0}$ is geometrically irreducible, $C^{0} \times Z$ is irreducible; write $\gamma$ for its
generic point. Since `µ′` sends the point $\epsilon(\eta)$ (where $\epsilon$ denotes the unit section of $C^{0}$) to
$\eta$, then $\gamma$ is sent to a generization of $\eta$, hence to $\eta$. So `µ′` sends the underlying space of $C^{0}
\times Z$ into $Z$, and so, since $C^{0} \times Z$ is reduced, `µ′` factors through $Z$.

Let now $z \in Z$. Set $K = \kappa(z)$. Then the morphism `µ_z : G_K → X_K`, $h \mapsto h \cdot z$ is surjective; let
$\alpha$ be a maximal point of `X_K`; the local ring $O_{X_{K}, \alpha}$ is

<!-- original page 310 -->

a field, since `X_K` is reduced, so `µ_z` is flat at every point of `G_K` above $\alpha$, so `µ_z` is flat, by Lemma
2.5.3.

On the other hand, `µ_z` sends the generic point $\omega$ of $C^{0}_{K}$ to a point $t \in Z_{K}$. Let $\beta$ be a
maximal point of `Z_K` such that $t \in {\beta}^{-}$; since `µ_z` is flat, there exists a generization $\xi$ of $\omega$
such that `µ_z(ξ) = β`, and since $\omega$ is a maximal point of `G_K`, one necessarily has $\xi = \omega$, and so
`µ_z(ω)` equals $\beta$, which lies above $\eta$ (since $Z_{K} \to Z$ is flat).

Set $L = \kappa(\omega)$ and let $\omega_{L}$ and $z_{L}$ be the $L$-points deduced from $\omega$ and $z$; then
$\omega_{L} \cdot z_{L} = \beta'$ is a point of `Z_L` above $\beta$, and so $z_{L} = \omega^{-1}_{L} \cdot \beta' \in
C^{0}_{L} \cdot U_{L}$, whence $z \in C^{0} \cdot U$. This proves (i).

Since $C^{0}$ is quasi-compact, by 2.6.2, point (i′) follows from this: if $X$ is irreducible and if $U$ is a non-empty
affine open, then $X$ equals $C^{0} U$, i.e. is the image of the morphism $C^{0} \times U \to X$, hence is
quasi-compact. Finally, if $U$ is retrocompact in $X$, then (cf. 2.6.3) $U^{-}$ is the union of the ${\eta}^{-}$ for
$\eta$ running through the maximal points of $X$ contained in $U$, hence equals $C^{0} U$. This proves (ii).

One then obtains the following result ([Per75] II Th. 2.4, see also [Per76], Prop. 4.1.1):

**Theorem 2.6.5.** *Let $k$ be a field, $G$ a $k$-group scheme.*

*(i) There exists a unique group subscheme $G^{0}$ of $G$, called the* neutral component *of $G$, such that:*

*(a) The underlying space of $G^{0}$ is the irreducible component of the unit element.* *(b) $G^{0} \to G$ is a flat
closed immersion, i.e. $O_{G,g} = O_{G^{0},g}$ for every $g \in G^{0}$.*

*(ii) Moreover, $G^{0}$ is quasi-compact, geometrically irreducible, and is a characteristic subgroup of $G$.*

*(iii) If $G$ is connected, then $G = G^{0}$.*

<!-- label: III.VI_A.2.6.5 -->

*Proof.* (i) Recall first that $G$ is separated (0.3), hence a fortiori quasi-separated. Let $U$ be an affine open of
$G$ containing the generic point $\omega$ of $C^{0}$. By 2.6.3 and 2.6.4, $U^{-} = C^{0} U$ is at once open and closed,
and $C^{0} = {\omega}^{-}$ is set-theoretically the intersection of these open-and-closed parts.

For $U$ running through the affine opens containing $\omega$, one obtains a projective system of $G$-schemes $U^{-}$,
whose transition morphisms are affine (since they are closed immersions). One may therefore form the projective limit
$G^{0}$ (cf. EGA IV_3, 8.2.2), i.e. for every affine open $V$ of $G$, $G^{0} \cap V$ is the spectrum of the algebra

```text
lim O_G(V ∩ U) = O_G(V) / ∑_U I_U(V),
→
```

where $I_{U}(V)$ denotes the kernel of $O_{G}(V) \to O_{G}(V \cap U)$. It follows that $G^{0}$ has $C^{0}$ as underlying
space, and that $G^{0} \to G$ is a closed immersion. Moreover, for every $g \in G^{0}$, $O_{G^{0},g}$ is the inductive
limit, for $V$ running through the affine opens of $G$ containing $g$, of the $k$-algebras $O_{G^{0}}(V \cap G^{0}) =
\lim_{U} O_{G}(V \cap U)$, and this double inductive limit is

<!-- original page 311 -->

identified with

```text
lim lim O_G(V) = O_{G,g}
→   →
 U   V
g∈V⊂U
```

i.e. one has $O_{G^{0},g} = O_{G,g}$ (see also EGA IV_2, 5.13.3 (ii)). So $i : G^{0} \to G$ is a flat closed immersion.
Conversely, this condition implies that $i^{*}(O_{G}) = O_{G^{0}}$, and so $G^{0}$ is uniquely determined by conditions
(a) and (b). This proves (i).

The first two assertions of (ii) follow from 2.6.2. Finally, let $S$ be a $k$-scheme and $\phi$ an automorphism of the
$S$-group `G_S`. For every $s \in S$, $\phi_{s}$ sends $G^{0}_{\kappa(s)}$ into itself, so $\phi(G^{0}_{S}) \subset
G^{0}_{S}$. Moreover, the closed immersion $i_{S} : G^{0}_{S} \hookrightarrow G_{S}$ deduced from $i$ by base change is
flat, so one has $O_{G_{S}, \phi(z)} = O_{G^{0}_{S}, \phi(z)}$ for every $z \in G^{0}_{S}$, and so $\phi \circ i_{S}$
factors through $G^{0}_{S}$. This proves that $G^{0}$ is a characteristic subgroup of $G$, whence (ii). Finally, (iii)
is a particular case of point (i) of the following proposition.[^N.D.E-VI_A-32]

**Proposition 2.6.6.** *Let $k$ be a field, $G$ a $k$-group acting on a $k$-scheme $X$ in such a way that the morphism
$G \times X \to X \times X$, $(g, x) \mapsto (gx, x)$ is surjective. Suppose $X$ quasi-separated. Then:*

*(i) Every connected component $C$ of $X$ is irreducible.*

*(ii) Let $\eta$ be the generic point of $C$ and $L$ the algebraic closure of $k$ in $\kappa(\eta)$. Then $C$ is an
$L$-scheme, geometrically irreducible over $L$, and the morphism*

```text
G⁰_L ×_L C → C ×_L C
```

*is surjective.*

*(iii) In particular, if $C$ contains a rational point $x$, then $C$ is geometrically irreducible over $k$ and the
morphism $\phi : G^{0} \to C$, $g \mapsto gx$ is surjective.*

<!-- label: III.VI_A.2.6.6 -->

*Proof.* (i) Let $C$ be a connected component of $X$, $Y$ an irreducible component of $X$ contained in $C$, $\eta$ the
generic point of $Y$, and $U$ an affine open of $X$ containing $\eta$. Since $X$ is quasi-separated, $U$ is retrocompact
in $X$, so by 2.6.4, $U^{-} = G^{0} U$ is an open-and-closed part of $X$ meeting $C$, hence containing $C$. Now, by
2.6.3, the intersection of the $U^{-}$, for $U$ running through a fundamental system of affine open neighborhoods of
$\eta$, equals ${\eta}^{-}$. It follows that $C = {\eta}^{-}$. This proves (i).

The first assertion of (ii) (and also of (iii)) follows from 2.6.1. Let us start by showing the second assertion of
(iii). Denote by $\omega$ (resp. $\eta$) the generic point of $G^{0}$ (resp. $C$). Let $z \in C$ and $K = \kappa(z)$.
Since $G^{0}$ (resp. $C$) is geometrically irreducible over $k$, $G^{0}_{K}$ (resp. `C_K`) is irreducible; let $\xi$
(resp. $\beta$) denote its generic point. We saw in the proof of 2.6.4 that the morphism `µ_z : G_K → C_K`, $h \mapsto h
\cdot z$ sends $\xi$ to $\beta$, and similarly one has $\phi(\omega) = \eta$.

<!-- original page 312 -->

Let $L = \kappa(\xi)$ and let $\xi_{L}, z_{L}$ be the $L$-points deduced from $\xi$ and $z$; then $\xi_{L} \cdot z_{L} =
\beta'$ is a point of `C_L` above $\beta \in C_{K}$, hence also above $\eta \in C$. Consider the cartesian square:

```text
            φ_L
G⁰_L ──────────→ C_L
 │                │
 π_{G⁰}           π_C
 │       φ        │
 ▼                ▼
 G⁰ ────────────→ C ;
```

since $\phi^{-1}_{L}(\pi^{-1}_{G^{0}}(\omega)) = \pi^{-1}_{C}(\eta)$ (cf. EGA I, 3.4.8), there exists $g \in G^{0}_{L}$
such that $\phi_{L}(g) = \beta'$. One therefore has $z_{L} = \xi^{-1}_{L} \cdot \phi_{L}(g) = \phi_{L}(\xi^{-1}_{L} g)$,
whence $\phi(\pi_{G^{0}}(\xi^{-1}_{L} g)) = \pi_{C}(z_{L}) = z$. This proves that $\phi$ is surjective.

Now let us prove the second assertion of (ii). It suffices to show that, for every $z \in C$, the morphism
`µ_z : G⁰_L ⊗_L κ(z) → C ⊗_L κ(z)` is surjective, but this follows from (iii), since $z$ is a rational point of $C
\otimes_{L} \kappa(z)$.

**Remark 2.6.7.** *Under the hypotheses of 2.6.6, if $C(k) = \emptyset$, the morphism $G^{0} \times_{k} C \to C
\times_{k} C$ is not necessarily surjective. For example, for $k = \mathbb{R}$ and $G = {\pm 1}_{\mathbb{R}}$, the
$G$-torsor $X = \operatorname{Spec} \mathbb{R}[X]/(X^{2} + 1)$ is connected, but the morphism $G^{0} \times_{\mathbb{R}}
X \to X \times_{\mathbb{R}} X$ is not surjective. (But one has $L = \mathbb{C}$ and the morphism $G^{0}
\times_{\mathbb{R}} X \to X \times_{\mathbb{C}} X$ is an isomorphism.)*

<!-- label: III.VI_A.2.6.7 -->

## 3. Construction of quotients $F\backslash G$ (for `G, F` of finite type)

<!-- label: III.VI_A.3 -->

<!-- original page 302 -->

### 3.1

Let $A$ be an Artinian local ring and $u : F \to G$ a homomorphism of $A$-groups. If `µ : F ×_A F → F` and $\nu : G
\times_{A} G \to G$ denote the multiplication morphisms and $\lambda$ the composite morphism

```text
            u × G              ν
F ×_A G ─────────→ G ×_A G ────→ G,
```

we recall that the *left quotient* $F\backslash G$ of $G$ by $F$ is the cokernel of the $(Sch/A)$-groupoid $G_{*}$
described below:

```text
                            F × λ
                            ───→
                            µ × G                λ
                  F ×_A F ×_A G    ──→  F ×_A G ───→ G
                            ───→                pr_2
                            pr_{2,3}
```

($pr_{2}$ and $pr_{2,3}$ are the projections of $F \times_{A} G$ and $F \times_{A} (F \times_{A} G)$ onto the second
factors). We shall say that $G_{*}$ is the *groupoid with base $G$ defined by* $u$ (cf. Exp. V, § 2.a; as in Exposé V,
we do not follow in this Exposé the convention of IV, 4.6.15).

Since the unique $A$-morphism $F \to \operatorname{Spec} A$ is universally open (EGA IV_2, 2.4.9), $pr_{2}$ is an open
morphism; the same therefore holds for $\lambda$, which is the composition of $pr_{2}$ and the automorphism $\sigma$ of
$F \times_{A} G$ defined by the formulas: $\sigma(S)(x, y) = (x, u(S)(x) \cdot y)$, where $S$ is a variable $A$-scheme,
and $x$ and $y$ belong to $F(S)$ and $G(S)$. One sees in the same way that $pr_{2}$ and $\lambda$ are flat when $F$ is
flat over $A$.

<!-- original page 303 -->

Let us also note, to conclude these preliminaries, that every $A$-morphism $s : \operatorname{Spec} A \to G$ defines an
automorphism of the groupoid $G_{*}$ which induces on $G$, $F \times_{A} G$ and $F \times_{A} F \times_{A} G$ the
automorphisms $r_{s}$, $id_{F} \times_{A} r_{s}$ and $id_{F} \times_{A} id_{F} \times_{A} r_{s}$ respectively. We shall
again write $r_{s}$ for this automorphism of $G_{*}$, and we shall say that $r_{s}$ is the *right translation defined
by* $s$ (cf. 0.4).

### 3.2. Theorem

**Theorem 3.2.** *Let $F$ and $G$ be flat groups locally of finite type over an Artinian local ring $A$. Let $u : F \to
G$ be a quasi-compact $A$-group homomorphism with kernel finite over $A$. Then:*[^N.D.E-VI_A-33]

*(i) The left quotient $F\backslash G$ of $G$ by $F$ exists in $(Sch/A)$, and the sequence*

```text
              λ        p
F ×_A G  ─────→  G  ─────→  F\backslash G
             pr_2
```

*is exact in the category of all ringed spaces.*

*(ii) The canonical morphism $p : G \to F\backslash G$ is surjective and open, and $F\backslash G$ is a direct sum of
schemes of finite type over $A$.*

*(ii′) More precisely, $X = F\backslash G$ is equipped with a right action of $G$ such that $p(e) \cdot g = p(g)$ for
every $g \in G$; consequently, the connected components of $X$ are of finite type over $A$, irreducible, and all of
dimension $\dim G - \dim F$.*

*(iii) The canonical morphism $F \times_{A} G \to G \times_{F\backslash G} G$ is surjective.*

*(iv) If $u$ is a monomorphism,[^N.D.E-VI_A-34] then:*

*(a) $F \times_{A} G \xrightarrow{(\lambda,pr_{2})} G \times_{F\backslash G} G$ is an isomorphism, and $G \to
F\backslash G$ is faithfully flat and locally of finite presentation.* *(a′) $F\backslash G$ represents the (fppf)
quotient sheaf `F\̃G`, and $G \to F\backslash G$ is a locally trivial $F$-torsor for the (fppf) topology.* *(b)
$F\backslash G$ is flat over $A$, and is smooth over $A$ if $G$ is so.* *(c) $u : F \to G$ is a closed immersion, and
$F\backslash G$ is separated.* *(d) If, in addition, $F$ is a normal subgroup of $G$, there exists on $F\backslash G$
one and only one $A$-group structure such that $p : G \to F\backslash G$ is a morphism of $A$-groups.*

<!-- label: III.VI_A.3.2 -->

In the proof of this theorem, $A'$ will denote an $A$-algebra that is local, finite and free over $A$. If $R$ is a
relation involving $A'$, we shall say that "$R(A')$ is true when $A'$ is large enough" if there exists an $A$-algebra
`A_1` that is local, finite and free over $A$ such that the relation $R(A')$ is satisfied for each $A$-algebra $A'$ that
is local, finite and free over `A_1`.

<!-- original page 304 -->

We shall first prove the theorem when $F$ and $G$ are of finite type over $A$.

#### 3.2.1

Suppose for a moment that every point of $G$ has an open saturated neighborhood $W$ such that the groupoid induced by
$G_{*}$ on $W$ possesses a quasi-section (cf. V § 6). Then, by V 6.1, one has assertions (i), (ii), (iii) and (iv)(a),
and $F\backslash G$ is of finite type over $k$. Moreover, under the hypothesis of (iv), since $G \to F\backslash G$ is
faithfully flat and locally of finite presentation, assertion (b) follows from EGA IV, 2.2.14 and 17.7.7. On the other
hand, assertion (iv)(a′) follows from (iv)(a), by Exp. IV, 3.4.3.1, 5.2.2 and 5.1.6. Finally, (iv)(c) will be proved in
3.2.5, and (ii′) and (iv)(d) will be proved in section 5.

Let us now prove the following assertion:

```text
(†)    every finite subset of F\backslash G is then contained in an affine open.
```

[^N.D.E-VI_A-35]

If $U$ is a quasi-section of the groupoid induced by $G_{*}$ on a saturated open $W$ of $G$, then $U \otimes_{A} A'$ is
a quasi-section of the $(Sch/A')$-groupoid induced by $G_{*} \otimes_{A} A'$ on $W \otimes_{A} A'$. Moreover, if $U_{*}$
is the $(Sch/A)$-groupoid induced by $G_{*}$ on $U$, then $U_{*} \otimes_{A} A'$ is identified with the
$(Sch/A')$-groupoid induced by $G_{*} \otimes_{A} A'$ on $U \otimes_{A} A'$.[^N.D.E-VI_A-36]

It follows from the proofs of Exposé V that the construction of the quotient $X = F\backslash G$ commutes with the
extension $A \to A'$ of the base of the type considered here.[^N.D.E-VI_A-37]

Let then $x_{1}, \cdots, x_{n}$ be points of $X = F\backslash G$, which we may assume closed,[^N.D.E-VI_A-38] and
$g_{1}, \cdots, g_{n}$ closed points of $G$ projecting onto $x_{1}, \cdots, x_{n}$. Let $V$ be an everywhere dense
affine open of $X$,[^N.D.E-VI_A-39] and let $U$ be the inverse image of $V$ in $G$. By 1.2, there exists an $A$-algebra
$A'$ that is local, finite and free over $A$, such that the points $g'_{1}, \cdots, g'_{p}$ of $G' = G \otimes_{A} A'$
above $g_{1}, \cdots, g_{n}$ are strictly rational over $A'$.[^N.D.E-VI_A-40] Since the morphisms $G' \to G$ and $G \to
X$ are open, $U' = U \otimes_{A} A'$ is dense in $G'$, so the open set $\bigcap^{p}_{i=1} (U')^{-1} \cdot g'_{i}$ is
non-empty, hence contains a closed point $x$. So, by 1.2 (and 0.4.1), one may suppose, by possibly enlarging $A'$, that
$x$ is strictly rational over $A'$. Then, since $x \in (U')^{-1} \cdot g'_{i}$, one has $g'_{i} \in U' \cdot x$.

Denote by $V'$ the inverse image of $V$ in $X' = X \otimes_{A} A'$; this is an affine open of $X'$, and is also the
image of $U'$ under the projection $G' \to X'$. Since right translation $r_{x}$ is an automorphism of the groupoid
$G_{*} \otimes_{A} A'$, it induces an automorphism, again denoted $r_{x}$, of the quotient $X'$. Consequently, the image
$V' \cdot x = r_{x}(V')$ of $U' \cdot x$ in $X'$ is

<!-- original page 305 -->

an affine open of $X'$ containing the images $x'_{1}, \cdots, x'_{p}$ of $g'_{1}, \cdots, g'_{p}$.

Consider now the equivalence relation on $X' = X \otimes_{A} A'$ defined by the projection $X \otimes_{A} A' \to X$:

```text
                  d_1
                  ───→
X ⊗_A A′ ⊗_A A′       X ⊗_A A′  ─→  X,
                  ───→
                  d_0
```

where $d_{0}$ and $d_{1}$ are induced by the two canonical injections of $A'$ into $A' \otimes_{A} A'$. Since $A'$ is a
finite, free $A$-algebra, say of rank $n$, then $d_{0}$ and $d_{1}$ are finite and locally free of rank $n$;
consequently, one may apply the reasoning of Exp. V, 5.b (drawn from the proof of SGA 1, VIII.7.6). One thus obtains
that $x'_{1}, \cdots, x'_{p}$ are contained in an affine saturated open $W'$ contained in the affine open $V' \cdot x$.
The image of $W'$ in $X$ then contains $x_{1}, \cdots, x_{n}$ and is an affine open of $X$, by V, 4.1 (ii).

#### 3.2.2

For every $A$-algebra $A'$ that is local, finite and free over $A$, let us now write $U(A')$ for the set of points of $G
\otimes_{A} A'$ having an open saturated neighborhood $W$ such that the groupoid induced by $G_{*} \otimes_{A} A'$ on
$W$ has a quasi-section. It is clear that $U(A')$ is saturated for the action of $G(\operatorname{Spec} A')$ on $G
\otimes_{A} A'$. We shall see that, when $A'$ is large enough, $U(A')$ is equal to $G \otimes_{A} A'$.

By Theorem V 8.1, $U(A)$ is non-empty, hence contains a closed point $y$. The proof then proceeds by induction on
$\dim(G - U(A))$. Let $g_{1}, \cdots, g_{n}$ be closed points belonging to the various irreducible components of $G -
U(A)$. By 1.2, there exists $A'$ local, finite and free over $A$, such that the points $g'_{1}, \cdots, g'_{p}$ (resp.
$x = x_{1}, \cdots, x_{r}$) of $G' = G \otimes_{A} A'$ projecting onto $g_{1}, \cdots, g_{n}$ (resp. onto $y$) are
strictly rational over $A'$. Then $U(A')$ contains $(U(A) \otimes_{A} A') \cdot x^{-1} g'_{i}$ for every $i$; so $U(A')$
contains

<!-- original page 306 -->

$g'_{1}, \cdots, g'_{p}$, and one has

```text
dim(G′ − U(A′)) < dim(G − U(A)).
```

The induction hypothesis then implies the existence of an algebra $A''$ local, finite and free over $A'$ such that one
has $U(A'') = G' \otimes_{A'} A'' = G \otimes_{A} A''$.

#### 3.2.3

We are now in a position to prove the existence of $F\backslash G$ when $F$ and $G$ are of finite type over $A$. Let
$A'$ be large enough over $A$ so that $U(A')$ coincides with $G \otimes_{A} A'$ (cf. 3.2.2). We shall set $A'' = A'
\otimes_{A} A'$ and, for every $A$-scheme $X$, we shall denote by $X'$ and $X''$ the fibered products $X \otimes_{A} A'$
and $X \otimes_{A} A''$. By 3.2.1 and 3.2.2, the quotients $F'\backslash G'$ and $F''\backslash G''$ exist, and one has
the following commutative diagram, in which the first two lines and columns are exact:

```text
                       pr′′_2          p′′
   F′′ ×_{A′′} G′′  ──────→  G′′  ──────→  F′′ \ G′′
                       λ′′
    w_1   w_2           v_1   v_2          u_1   u_2
                                       
                       pr′_2           p′
(∗) F′ ×_{A′} G′    ──────→  G′   ──────→  F′ \ G′
                       λ′
         h                       g

                       pr_2
   F ×_A G        ──────────→  G       .
                       λ
```

In this diagram, $pr'_{2}$ and $\lambda'$ (resp. $pr''_{2}$ and $\lambda''$) are obtained from $pr_{2}$ and $\lambda$ by
obvious base changes; the morphisms $g$ and $h$ are induced by the canonical injection $A \to A'$. One denotes by $p'$
and $p''$ the canonical morphisms; the morphisms $v_{1}, v_{2}$ and $w_{1}, w_{2}$ are induced by the two canonical
injections of $A'$ into $A''$. Finally, since the construction of the quotient $F'\backslash G'$ commutes with the two
base changes

<!-- original page 307 -->

$f_{1}, f_{2} : \operatorname{Spec} A'' \Rightarrow \operatorname{Spec} A'$, one has, writing $\pi' : F'\backslash G'
\to \operatorname{Spec} A'$ for the structural morphism, canonical isomorphisms, for $i = 1, 2$:

```text
            ∼
τ_i : F′′\backslash G′′ ──→ (F′\backslash G′) ×_{π′, f_i} Spec A′′,
```

and the morphism $u_{i}$ is the composite of $\tau_{i}$ and the projection $(F'\backslash G') \times_{\pi', f_{i}}
\operatorname{Spec} A'' \to F'\backslash G'$.

Now, when one has a diagram of type $(\ast)$ with the first two rows and columns exact, one verifies easily that
$Coker(pr_{2}, \lambda)$ exists if and only if $Coker(u_{1}, u_{2})$ exists, and these two cokernels are identified. The
existence of $F\backslash G$ will therefore follow from that of $Coker(u_{1}, u_{2})$.

Now it follows from the compatibility of the formation of $F\backslash G$ with the base extensions considered here (cf.
N.D.E. (37) in 3.2.1, and 4.6 below) that the composite morphism

```text
                            τ_1⁻¹                          τ_2
(F′\backslash G′) ×_{π′, f_1} Spec A′′ ────→ F′′\backslash G′′ ────→ (F′\backslash G′) ×_{π′, f_2} Spec A′′
```

is a descent datum on $F'\backslash G'$ relative to $f : \operatorname{Spec} A' \to \operatorname{Spec} A$. By 3.2.1 (†)
and SGA 1, VIII 7.6, this descent datum is effective, that is, $Coker(u_{1}, u_{2})$ exists (one could also use directly
Theorem 4.1 of Exp. V).

#### 3.2.4

To complete the proof of assertions (i), (ii), (iii) and (iv)(a) of 3.2 in the case where $F$ and $G$ are of finite type
over $A$, it remains to study the quotient $F\backslash G$. By V 6.1, assertions (ii), (iii) and (iv)(a) "become true"
after the base change $f : \operatorname{Spec} A' \to \operatorname{Spec} A$; by EGA IV_2, 2.6.1, 2.6.2 and 2.7.1, these
assertions were therefore true before the base change. Finally, to prove the second assertion of (i), i.e. that
$F\backslash G$ is the cokernel of $(pr_{2}, \lambda)$ in the category of all ringed spaces, one need only refer to V §
6.c).

<!-- original page 313 -->

#### 3.2.5

[^N.D.E-VI_A-41] Let us now prove assertion (iv)(c) of 3.2, by reproducing the proof of VI_B, 9.2.1. Write $X =
F\backslash G$, and $d$ for the morphism $F \times_{A} G \to G \times_{A} G$ with components $\lambda$ and $pr_{2}$.

Since $u$ is a closed immersion by 2.5.2, and since $d = \sigma \circ (u \times id_{G})$, where $\sigma$ is the
automorphism of $G \times_{A} G$ defined by $\sigma(x, y) = (xy, y)$, $d$ is a closed immersion. On the other hand, by
(iv)(a), one has the cartesian square

```text
                  d
F ×_A G ────────────→ G ×_A G
   │                      │
   │                      │ p × p
   ▼      Δ_X              ▼
   X ────────────────→ X ×_A X
```

and $p$, hence also $p \times p$, is faithfully flat and locally of finite presentation. So, by (fppf) descent, since
$d$ is a closed immersion, the same holds for $\Delta_{X}$, i.e. $X$ is separated.

### 3.3

[^N.D.E-VI_A-42] In Theorem 3.2, the hypothesis that $G$ be flat can be removed when $u : F \to G$ is a monomorphism.
This generalization is mentioned in Remark 9.3 b) of Exp. VI_B, and also in [Ray67a], Example a) i), p. 82. The proof,
found in Theorem 4 of [An73], follows from Theorem 3.2 and from the following theorem of Grothendieck (mentioned in
[Ray67a], Th. 1 ii) and proved in [DG70], § III.2, 7.1). If $X$ is a scheme and $R$ an equivalence relation in $X$, we
shall write $\tilde{X}/R$ for the (fppf) quotient sheaf of $X$ by $R$ (cf. IV 4.4.9).

**Theorem 3.3.1 (Grothendieck).** *Let $A$ be a ring, $X$ an $A$-scheme, and $d_{0}, d_{1} : R \to X$ an $A$-equivalence
relation in $X$, such that $d_{i}$ is faithfully flat, of finite presentation. Let `X_0` be a saturated closed subscheme
of $X$, defined by a nilpotent ideal, and let `R_0` be the equivalence relation induced by $R$ on `X_0`. Then, if the
(fppf) quotient sheaf $\tilde{X}_{0}/R_{0}$ is representable by an $A$-scheme, so is $\tilde{X}/R$.*

<!-- label: III.VI_A.3.3.1 -->

For the proof, we refer to [DG70], § III.2, 7.1. Let us now return to the case where $A$ is an Artinian local ring. Let
$u : F \to G$ be a quasi-compact morphism between $A$-groups locally of finite type, and suppose further that $u$ is a
monomorphism. Then, by 2.5.2, $u$ is a closed immersion.

One may now state the following variant of Theorem 3.2.

**Theorem 3.3.2.** *Let $A$ be an Artinian local ring, $G$ an $A$-group locally of finite type, $F$ a closed subgroup of
$G$, flat over $A$.*[^N.D.E-VI_A-43] *Then:*

*(i) The (fppf) quotient sheaf $\tilde{F}\backslash G$ is representable by an $A$-scheme $F\backslash G$ that is
separated and locally of finite type; moreover, the sequence*

```text
            //         p
F ×_A G ─────→  G  ─────→  F\backslash G
```

<!-- original page 318 -->

*is exact in the category of all ringed spaces.*

*(ii) $F \times_{A} G \xrightarrow{(\lambda,pr_{2})} G \times_{F\backslash G} G$ is an isomorphism, and $p : G \to
F\backslash G$ is faithfully flat and locally of finite presentation, so that $p$ is a locally trivial $F$-torsor for
the (fppf) topology.*

*(iii) If $G$ is flat (resp. of finite type, resp. smooth) over $A$, then so is $F\backslash G$.*

*(iv) $X = F\backslash G$ is equipped with a right action of $G$, such that $p(e) \cdot g = p(g)$ for every $g \in G$;
consequently, the connected components of $X$ are of finite type over $A$, irreducible, and all of dimension $\dim G -
\dim F$.*

*(v) If, in addition, $F$ is a normal subgroup of $G$, there exists on $F\backslash G$ one and only one $A$-group
structure such that $p : G \to F\backslash G$ is a morphism of $A$-groups.*

<!-- label: III.VI_A.3.3.2 -->

Assertions (i) and (ii) follow from 3.2 and 3.3.1, and since $G \to F\backslash G$ is faithfully flat and locally of
finite presentation, assertion (iii) follows from EGA IV, 2.2.14, 2.7.1 and 17.7.7. We shall prove assertions (iv) and
(v) in section 5. Let us note immediately the following corollary.

**Corollary 3.3.3.** *Let $A$ be an Artinian local ring, $G$ an $A$-group locally of finite type, $H$ a closed subgroup
of $G$, flat over $A$. Write $p$ for the morphism $G \to G/H$ and $\lambda$ (resp. $pr_{1}$) for the morphism $G \times
H \to G$ defined by $\lambda(g, h) = gh$ (resp. the projection $G \times H \to G$). Then, for every open subset $U$ of
$G/H$, one has*

```text
O(U) = {φ ∈ O(p⁻¹(U)) | φ ∘ λ = φ ∘ pr_1}
```

*i.e. $O(U)$ is the set of $\phi \in O(p^{-1}(U))$ such that $\phi(gh) = \phi(g)$ for every $A$-scheme $S$ and $g \in
G(S)$, $h \in H(S)$.*

<!-- label: III.VI_A.3.3.3 -->

Indeed, since $p : G \to G/H$ is faithfully flat and locally of finite presentation, hence covering for the (fppf)
topology, this follows from IV, 3.3.3.2.

## 4. Construction of quotients $F\backslash G$ (general case)

<!-- label: III.VI_A.4 -->

<!-- original page 308 -->

We now assume the hypotheses of Theorem 3.2 to be satisfied, $F$ and $G$ not necessarily being of finite type over $A$.

### 4.1

Let us first consider a connected component $G^{\alpha}$ of $G$ and show that the saturation
$S(G^{\alpha})$[^N.D.E-VI_A-44] of $G^{\alpha}$ for the equivalence relation defined by the groupoid $G_{*}$ is an
open-and-closed subset of $G$ (in other words, is the union of certain connected components of $G$).

This saturation is the image of $F \times_{A} G^{\alpha}$ under $\lambda$, hence is open in $G$ (cf. § 3.1). If $k$ is
the residue field of $A$ and $\bar{k}$ an algebraic closure of $k$, it remains to show that the image of $(F \times_{A}
G^{\alpha}) \otimes_{A} \bar{k}$ by $\lambda \otimes_{A} \bar{k}$ is closed in $G \otimes_{A} \bar{k}$, or equivalently,
by SGA 1, VIII.4.4, that the image of $(F \times_{A} G^{\alpha}) \otimes_{A} \bar{k}$ by $\lambda \otimes_{A} \bar{k}$
is closed. Since $G^{\alpha} \otimes_{A} \bar{k}$ is the union of a finite number of connected components of $G
\otimes_{A} \bar{k}$, we are reduced to the case where $A$ is an algebraically closed field, which we shall assume. In
this case, $S(G^{\alpha})$ is the union of the images of $G^{\alpha}$ under the left translations $\ell_{u(x)}$, where

<!-- original page 319 -->

$x$ runs through the closed points of $F$; the assertion follows therefore from the fact that these images are connected
components of $G$.

### 4.2

Let us in particular take $G^{\alpha}$ to be the connected component $G^{0}$ of the origin of $G$. Then $S(G^{0})$
obviously contains the image of $F$ under $u$, which is none other than the equivalence class of the origin. On the
other hand, if $F^{\beta}$ is a connected component of $F$, $F^{\beta} \times_{A} G^{0}$ is connected (2.1.2), so that
the image of $F^{\beta} \times_{A} G^{0}$ by $\lambda$ is contained in the connected component of $u(F^{\beta})$ in $G$.
In other words, $S(G^{0})$ is the union of the connected components which meet the image of $F$.

One will also note that the open subscheme of $G$ having $S(G^{0})$ as underlying space is a subgroup of $G$ (which we
still denote $S(G^{0})$):

<!-- original page 309 -->

indeed, the inversion morphism of $G$ preserves the image of $F$ and permutes the connected components of $G$ meeting
this image; it therefore suffices to show that $\nu : G \times_{A} G \to G$ sends $S(G^{0}) \times_{A} S(G^{0})$ into
$S(G^{0})$, and for this one may suppose that $A$ is an algebraically closed field (with the notations of 4.1, $S(G^{0})
\otimes_{A} \bar{k}$ is indeed identified with the saturation of $(G \otimes_{A} \bar{k})^{0}$ by the equivalence
relation defined by the homomorphism $u \otimes_{A} \bar{k}$); if $G^{\gamma}$ and $G^{\delta}$ are then connected
components of $S(G^{0})$, $G^{\gamma} \times_{A} G^{\delta}$ is connected and its image under $\nu$ meets the image of
$F$; consequently, $u(G^{\gamma} \times_{A} G^{\delta})$ is contained in a connected component of $G$ meeting $u(F)$.

### 4.3

It follows from what precedes that the groupoid $G_{*}$ with base $G$ defined by $u$ is the direct sum of the groupoids
$S(G^{\alpha})_{*}$ induced by $G_{*}$ on the various open-and-closed parts of $G$ of the form $S(G^{\alpha})$. The
cokernel of $G_{*}$ is therefore the direct sum of the cokernels of these groupoids $S(G^{\alpha})_{*}$, which one is
led to study separately.

Let us first consider the groupoid $S(G^{0})_{*}$ induced by $G_{*}$ on $S(G^{0})$. It is clear that $S(G^{0})_{*}$ is
the groupoid with base $S(G^{0})$ defined by the homomorphism from $F$ into $S(G^{0})$ induced by $u$ (§ 3.1). The
cokernel whose existence we wish to prove is therefore identified with $F\backslash S(G^{0})$. Consider on the other
hand the groupoid

```text
              ℓ′_2
              ────→     ℓ_1
              ℓ′_1            ────→
G⁰_2          ────→   G⁰_1   ────→   G⁰_0 = G⁰
                              ℓ_0
              ℓ′_0
```

induced by $S(G^{0})_{*}$ on $G^{0}$. If one refers to the construction explicit in V § 3.b), the object then denoted
$Y_{0} \times_{X_{0}} X_{1}$ is none other than

<!-- original page 310 -->

$F \times_{A} G^{0}$, so that $G^{0}_{1}$ is the inverse image of $G^{0}$ under the morphism $F \times_{A} G^{0} \to
S(G^{0})$ induced by $\lambda$.

I claim that this inverse image is $F^{0} \times_{A} G^{0}$, where $F^{0}$ denotes the inverse image of $G^{0}$ under
$u$. Indeed, if $F^{\beta}$ is a connected component of $F^{0}$, $F^{\beta} \times_{A} G^{0}$ is connected (2.1.2) and
$\lambda(F^{\beta} \times_{A} G^{0})$ is contained in $G^{0}$; conversely, if $F^{\beta}$ is a connected component of
$F$ not contained in $F^{0}$, the image of $F^{\beta} \times_{A} G^{0}$ is again connected and contains $u(F^{\beta})$;
if $u(F^{\beta})$ is not contained in $G^{0}$, $\lambda(F^{\beta} \times_{A} G^{0})$ does not meet $G^{0}$.

It follows from what precedes that the groupoid $G^{0}_{*}$ induced by $G_{*}$ on $G^{0}$ is the groupoid with base
$G^{0}$ defined by the homomorphism $F^{0} \to G^{0}$ induced by $u$. Since $G^{0}$, and hence $F^{0}$, are of finite
type over $A$, then, by paragraph 4, $G^{0}_{*}$ has a cokernel which is none other than $F^{0}\backslash G^{0}$.

I now claim that $F^{0}\backslash G^{0}$ is identified with $F\backslash S(G^{0})$. Indeed, the proof is analogous to
that of the first part of assertion (i) of Lemma V § 6.1; consider the diagram:

```text
                v                                pr_2
S(G⁰) ←──────────  F ×_A G⁰  ──────────→  G⁰,
```

where $v$ is the morphism induced by $\lambda$. Since $pr_{2}$ has a section, $pr_{2}$ is a universal effective
epimorphism, so that $F^{0}\backslash G^{0}$ coincides with $Coker(v_{0}, v_{1})$, where

```text
              v′_2
              ────→
              v′_1            v_1
                              ────→
V_2           ────→   V_1     ────→   V = F ×_A G⁰
                              v_0
              v′_0
```

<!-- original page 311 -->

is the inverse image by $pr_{2}$ of the groupoid $G^{0}_{*}$ (cf. V § 3.a), that is, also the inverse image of
$S(G^{0})_{*}$ by the composite morphism

```text
            inclusion                pr_2
F ×_A G⁰ ─────────→ F ×_A S(G⁰) ─────────→ S(G⁰).
```

Similarly, since $v$ is faithfully flat and quasi-compact, $F\backslash S(G^{0})$ coincides with the cokernel of the
inverse image of $S(G^{0})_{*}$ by the base change $v$. Now this inverse image is isomorphic to $V_{*}$ by Exp. V, §
3.c; it follows that the canonical inclusion of $G^{0}_{*}$ into $S(G^{0})_{*}$ induces an isomorphism of
$F^{0}\backslash G^{0}$ onto $F\backslash S(G^{0})$.

We finally note that: the construction of $F\backslash S(G^{0})$ commutes with finite locally free base changes, because
the same holds for $F^{0}\backslash G^{0}$ (cf. N.D.E. (37) and 4.6 below).

### 4.4

It remains to construct the cokernel of the groupoid $S(G^{\alpha})_{*}$ when $G^{\alpha}$ is an arbitrary connected
component of $G$. If $A'$ is a large enough local, finite, free $A$-algebra (cf. 3.2), $G^{\alpha} \otimes_{A} A'$ is
the union of a finite number of connected components $C_{1}, \cdots, C_{n}$ of $G \otimes_{A} A'$, all of which have a
strictly rational point. For every $i$, there exists therefore a right translation $r_{i}$ of $G \otimes_{A} A'$ sending
$G^{0} \otimes_{A} A'$ onto $C_{i}$; this translation induces an isomorphism of the groupoid $S(G^{0}_{*}) \otimes_{A}
A'$ onto $S(C^{i}_{*})$, so that the groupoid induced by $G_{*} \otimes_{A} A'$ on the saturation of $C_{i}$ has a
cokernel.

Since $S(G^{\alpha}_{*}) \otimes_{A} A'$ is the direct sum of some of the $S(C^{i}_{*})$, then $S(G^{\alpha}_{*})
\otimes_{A} A'$ has a cokernel; this cokernel is the direct sum of a certain number of copies of
`(F⁰ ⊗_A A′)\(G⁰ ⊗_A A′)`, so that every finite subset of this cokernel is contained in an affine open; moreover, the
construction of this cokernel commutes with finite locally free extensions

<!-- original page 312 -->

of the base (cf. N.D.E. (37) and 4.6 below). One thus sees, as in 3.2.3, that this cokernel is of the form $Y
\otimes_{A} A'$, where $Y$ is a cokernel of $S(G^{\alpha}_{*})$.

### 4.5

We have therefore constructed $F\backslash G$ and shown that it is a direct sum of schemes of finite type over $A$. The
other assertions of Theorem 3.2 reduce directly to assertions concerning the groupoids $S(G^{\alpha}_{*})$. As in V § 6,
the second assertion of (i) follows from the first and from (ii) and (iii), so it suffices to prove (ii), (iii) and
(iv)(a). Since $A'$ is a local, finite, free $A$-algebra, the morphism $A \to A'$ is faithfully flat and of finite
presentation, so, by SGA 1, VIII (3.1, 4.6, 5.4), it suffices to verify the corresponding assertions in the case of the
groupoid $S(G^{\alpha}_{*}) \otimes_{A} A'$. Now the latter is isomorphic to the direct sum of a finite number of copies
of $S(G^{0}_{*}) \otimes_{A} A'$ (cf. 4.4), so that one is reduced to the groupoid $S(G^{0}_{*})$.

For this last one continues to mimic the proof established in V § 6, as one began to do in 4.3.

### 4.6

Let us add to conclude this paragraph some remarks concerning Lemma 6.1 and § 9.a of Exposé V: with the hypotheses and
notations of V § 9.a, we seek a condition under which the construction of the cokernel of the $(Sch/S)$-groupoid $X_{*}$
commutes with an extension $\pi : S' \to S$ of the base. Since the cokernels of $X_{*}$ and $X'_{*}$ are identified with
the cokernels of the groupoids $U_{*}$ and $U'_{*}$ induced by $X_{*}$ and $X'_{*}$ on the quasi-sections $U$ and $U'$,
one is reduced to the case of a $(Sch/S)$-groupoid satisfying the hypotheses of Theorem V 4.1.

[^N.D.E-VI_A-45] If one denotes by $Y$ the cokernel of $U_{*}$, $Y' = Y \times_{S} S'$, and `Y_1` the cokernel of
$U'_{*}$, one saw in V § 9.a that the canonical morphism $Y_{1} \to Y'$ is a homeomorphism (and even a universal
homeomorphism); one may therefore identify `Y_1` and $Y'$ as topological spaces. If $p : U \to Y$ is the canonical
morphism and if $p' : U' \to Y'$ is obtained from it by base change, we then want the sequence of $O_{Y'}$-modules

```text
                p′_*(O_{U′})
(∗)  O_{Y′}  ─────────→  ──→  p′_* u′_{1*}(O_{U′_1}) = p′_* u′_{0*}(O_{U′_1})
                         ──→
```

<!-- label: eq:III.VI_A.4.6-star -->

to be exact.[^N.D.E-VI_A-46] Since we are under the hypotheses of V 4.1, $u_{0}$ and $u_{1}$ are finite and locally
free; and, by V.4.1 (ii), $p$ is integral. Then, $p$ and $p \circ u_{i}$ are affine, hence separated and quasi-compact.

<!-- original page 313 -->

Consequently, if $S'$ is flat over $S$, it follows from EGA III_1, 1.4.15 (taking into account the correction Err_III 25
in EGA III_2) that the sequence $(\ast)$ is identified with the inverse image of the sequence

```text
                          p_*(O_U)
(∗∗)  O_Y  ─────────→  ─────────→  p_* u_{1*}(O_{U_1}) = p_* u_{0*}(O_{U_1}),
                       ─────────→
```

<!-- label: eq:III.VI_A.4.6-doublestar -->

which is an exact sequence.[^N.D.E-VI_A-47] An analogous argument applies when the groupoid $X_{*}$ has "locally"
quasi-sections (cf. the proof of Theorem V 7.1). One thus obtains the:

**Proposition 4.6.1.** *The construction of the cokernel of $X_{*}$ commutes with flat extensions of the base when
$X_{*}$ has locally quasi-sections.*

<!-- label: III.VI_A.4.6.1 -->

### 4.7

Let us now consider the case of the groupoid $G_{*}$ of Theorem 3.2 when one provisionally assumes $F$ and $G$ of finite
type over $A$.

By 3.2.2, there exists an $A$-algebra $A'$ local, finite and free over $A$ such that the groupoid $G_{*} \otimes_{A} A'$
has "locally" quasi-sections. For every extension $T \to \operatorname{Spec} A$ of the base, the sequence

```text
                                  //
(F′′\backslash G′′) ×_{Spec A} T  ─────→  (F′\backslash G′) ×_{Spec A} T  ─────→  (F\backslash G) ×_{Spec A} T
```

deduced from the diagram $(\ast)$ of 3.2.3 is exact. If one supposes in addition $T$ flat over $\operatorname{Spec} A$,
then $(F''\backslash G'') \times_{\operatorname{Spec} A} T$ and $(F'\backslash G') \times_{\operatorname{Spec} A} T$ are
identified respectively, by 4.6, with the cokernels of the groupoids

```text
(G_* ⊗_A A′′) ×_{Spec A} T    and    (G_* ⊗_A A′) ×_{Spec A} T.
```

The diagram deduced from 3.2.3 $(\ast)$ by the base change $T \to \operatorname{Spec} A$ then shows that $(F\backslash
G) \times_{\operatorname{Spec} A} T$ is identified with the cokernel of $G_{*} \times_{\operatorname{Spec} A} T$. An
analogous argument is valid in the general case (i.e. when $G$ and $F$ are locally of finite type over $A$). One
therefore obtains:[^N.D.E-VI_A-48]

**Proposition 4.7.1.** *Under the hypotheses of Theorem 3.2, for every flat $A$-scheme $T$, $(F\backslash G)
\times_{\operatorname{Spec} A} T$ is identified with the left quotient of $G \times_{\operatorname{Spec} A} T$ by $F
\times_{\operatorname{Spec} A} T$.*

<!-- label: III.VI_A.4.7.1 -->

## 5. Connections with Exposé IV and consequences

<!-- label: III.VI_A.5 -->

<!-- original page 314 -->

### 5.1

[^N.D.E-VI_A-49] We resume the notations of § 3 and the hypotheses of Theorem 3.2; one then has the following
commutative diagram

```text
                          F × ν
F ×_A G ×_A G  ──────────→  F ×_A G

pr_2 × G    λ × G            pr_2    λ
                          ν
   G ×_A G            ──────────→  G

   p × G                           p
                       ρ
   (F\backslash G) ×_A G  ⇢ ⇢ ⇢ ⇢ ⇢ ⇢ ⇢ F\backslash G,
```

which satisfies the equalities $pr_{2} \circ (F \times \nu) = \nu \circ (pr_{2} \times G)$ and $\lambda \circ (F \times
\nu) = \nu \circ (\lambda \times G)$. Moreover, since $G$ is assumed flat over $A$, the left vertical sequence is exact
by 4.7, so that $\nu$ induces a morphism of $A$-schemes:

```text
ρ : (F\backslash G) ×_A G → F\backslash G.
```

This morphism $\rho$ makes $G$ act on the right on $F\backslash G$, as one verifies immediately; moreover, the canonical
morphism $G \to F\backslash G$ commutes with the right actions of $G$ on $G$ and on $F\backslash G$.

[^N.D.E-VI_A-50] This proves the first assertion of point (ii′) of 3.2. By 2.5.4, one then obtains that the connected
components of $X = F\backslash G$ are of finite type, irreducible, and all of the same dimension. To evaluate this
dimension, one may suppose $A = k$ and $k$ algebraically closed. By I, 2.3.3.1, the stabilizer of the $k$-point $p(e)$
is represented by the fiber $H = p^{-1}(p(e))$, and since $F\backslash G$ is the quotient of $G$ by $F$ in the category
of ringed spaces, this fiber has $u(F)$ as underlying space, and since $Ker(u)$ is finite, one therefore has
`dim H = dim u(F) = dim F`. By 2.5.4 (ii), one obtains therefore that `dim X = dim G − dim F`. This proves point (ii′)
of Theorem 3.2 (and hence also point (iv) of 3.3.2).

### 5.2

When the homomorphism of $A$-groups $u : F \to G$ is a monomorphism, one can recover 5.1 by using the results of Exposé
IV. Indeed, the canonical morphism $p : G \to F\backslash G$ is faithfully flat and open by 3.2; it is therefore
covering for the (fpqc) topology (IV 6.3.1), and one may apply corollaries IV.5.2.2 and IV.5.2.4.

<!-- original page 315 -->

In particular, if we assume, in addition to the hypotheses of 3.2, that $u$ is the inclusion in $G$ of a normal subgroup
$F$, there exists on $F\backslash G$ one and only one $A$-group structure such that the canonical morphism $p : G \to
F\backslash G$ is a homomorphism of $A$-groups.[^N.D.E-VI_A-51] This proves point (v) of 3.3.2.

### 5.3

We shall now review some statements from Exposé IV.

#### 5.3.1

Statements IV 5.2.7 and IV 5.3.1 translate as follows. Let $F$ and $G$ be two groups locally of finite type and flat
over $A$, $F$ being a closed normal subgroup of $G$. The maps $H \mapsto F\backslash H$ and $H' \mapsto H'
\times_{(F\backslash G)} G$ define a bijective correspondence between flat $A$-subgroups of $G$ containing $F$ and flat
$A$-subgroups of $F\backslash G$. In this bijection, closed (resp. normal) subgroups of $G$ containing $F$ correspond to
closed (resp. normal) subgroups of $F\backslash G$.[^N.D.E-VI_A-52]

#### 5.3.2

Proposition IV 5.2.9 implies the following result. Let $F$, $H$ and $G$ be groups locally of finite type and flat over
$A$; assume $F \subset H \subset G$, with $F$ closed in $G$ and normal in $H$. Under these conditions, $F\backslash H$
acts freely on the left on $F\backslash G$, the quotient scheme `(F\backslash H)\(F\backslash G)` exists, and there is a
canonical isomorphism of schemes with operator group $G$:

$$ (F\backslash H) \ (F\backslash G) = H\backslash G. $$

#### 5.3.3

From IV 5.2.8, finally, follows the assertion below. Let $F$, $H$ and $G$ be groups locally of finite type and flat over
$A$; assume that $F$ is contained in, closed and normal

<!-- original page 316 -->

in $G$, that $H$ is contained in $G$, and that $F \cap H$ is flat over $A$. Let $F \times^{\tau}_{A} H$ denote the
$A$-group having the product $F \times_{A} H$ as underlying scheme, with multiplication defined by the morphism $((x,
h), (y, h')) \mapsto (xhyh^{-1}, hh')$; similarly, let $u : H \cap F \to F \times^{\tau}_{A} H$ be the monomorphism $x
\mapsto (x^{-1}, x)$, and let $F \cdot H$ be the quotient `(F ∩ H)\(F ×^τ_A H)`. Under these conditions, there is a
canonical isomorphism

```text
F\backslash(F · H) = (F ∩ H)\backslash H.
```

### 5.4

[^N.D.E-VI_A-53] Let $u : G \to H$ be a quasi-compact morphism between $A$-groups locally of finite type, such that the
kernel $N$ of $u$ is flat over $A$. In this case, by 3.3.2 and 5.2, the quotient $A$-group $C = N\backslash G$ exists
and the morphism $p : G \to C$ is faithfully flat and locally of finite presentation. On the other hand, by IV 5.2.6,
$u$ induces a monomorphism $v : C \to H$, which is quasi-compact (because $u$ is, and $G \to C$ is surjective; cf. EGA
IV_1, 1.1.3), hence is a closed immersion by 2.5.2. We have therefore obtained the following proposition:

**Proposition 5.4.1.** *Let $u : G \to H$ be a quasi-compact morphism between $A$-groups locally of finite type, such
that $N = Ker u$ is flat over $A$. Then one has the factorization:*

```text
              u
G ───────────────→ H
 \                ↗
  p             ↗
   \         ↗ i
    ↘     ↗
     N\backslash G
```

*where $p$ is faithfully flat, locally of finite presentation, and $i$ a closed immersion.*

<!-- label: III.VI_A.5.4.1 -->

Suppose in addition $G$ flat over $A$. Then, by 3.3.2, $C = N\backslash G$ is flat over $A$, and so the quotient $X =
C\backslash H$ exists in $(Sch/A)$ and represents the (fppf) quotient sheaf $\tilde{C}\backslash H$, and $q : H \to X$
is a $C$-torsor. Consequently, writing $e : \operatorname{Spec} A \to G$ for the unit section of $G$, $v$ induces an
isomorphism of (fppf) sheaves between $\tilde{C}$ and the fibered product of $q$ and of $q \circ e : \operatorname{Spec}
A \to X$, which is represented by a closed subscheme of $H$. Consequently, $v$ is an isomorphism of $C$ onto a closed
group subscheme $K$ of $G$ (equal to the stabilizer of the $A$-point $q \circ e$ of $X$). (This gives another proof of
the fact that every quasi-compact monomorphism $v : C \to H$ between $A$-groups locally of finite type is a closed
immersion, cf. 2.5.2 and VI_B 1.4.2.)

Suppose in addition that $C$ is a normal subgroup of $H$; in this case, the $A$-group $\bar{H} = C\backslash H$ is the
cokernel in the category of $A$-groups of the morphism $u : G \to H$, and $K$ is the kernel of the morphism $H \to
\bar{H}$. When $G$ and $H$ are abelian $A$-groups, $K$ is the image of $u$ in the category of abelian $A$-groups, while
$C = (Ker u)\backslash G$ is the coimage of $u$. Taking into account the isomorphism $C \xrightarrow{\sim} K$ just
established, one obtains:[^N.D.E-VI_A-54]

**Theorem 5.4.2.** *Let $k$ be a field. The category of commutative algebraic $k$-groups is abelian.*

<!-- label: III.VI_A.5.4.2 -->

Indeed, when $k$ is a field, $Ker(u)$ is flat over $k$ whatever $u$.

[^N.D.E-VI_A-55] Let us note that the full subcategory of affine commutative algebraic $k$-groups is *thick*. Indeed,
consider an exact sequence of commutative algebraic $k$-groups:

```text
1  ───→  N  ───→  G  ───→  G/N  ───→  1.
```

If $G$ is affine, it is clear that $N$ is so, and $G/N$ is also so by a theorem of Chevalley, cf. VI_B, 11.17.
Conversely, if $N$ and $G/N$ are affine, then so is $G$, by VI_B, 9.2 (viii). One therefore obtains:

**Corollary 5.4.3.** *Let $k$ be a field. The category of commutative affine algebraic $k$-groups is abelian.*

<!-- label: III.VI_A.5.4.3 -->

Let us further point out that the category of all commutative affine $k$-groups (not necessarily of finite type) is
abelian; this is deduced from VI_B, 11.17 and 11.18.2 (cf. [DG70], § III.3, 7.4), see also VII_B, 2.4.2 for a proof
using formal groups.

<!-- original page 317 -->

### 5.5

Let $G$ be a group locally of finite type and flat over an Artinian local ring $A$. We know (2.3) that the connected
component of the origin $G^{0}$ is a normal open group subscheme of $G$, hence also flat over $A$. Then, by 3.2 and 5.2,
$G^{0}\backslash G$ is an $A$-group scheme, flat over $A$. Moreover, since each connected component $G^{\alpha}$ of $G$
is saturated for the equivalence relation defined by $G^{0}$, then $G^{0}\backslash G$ is the direct sum of the
$G^{0}\backslash G^{\alpha}$ (cf. 4.3). In particular, the connected component of the origin in $G^{0}\backslash G$ is
none other than $G^{0}\backslash G^{0} \cong \operatorname{Spec} A$, and so $G^{0}\backslash G \to \operatorname{Spec}
A$ is a local isomorphism at the origin. Consequently, $G^{0}\backslash G$ is étale over $\operatorname{Spec} A$, by
VI_B, 1.3.[^N.D.E-VI_A-56] One therefore obtains the following proposition (for point (ii), one refers to [DG70], §
II.5, 1.7–1.10):

**Proposition 5.5.1.** *Let $A$ be an Artinian local ring and $G$ an $A$-group locally of finite type and flat.*

*(i) $G^{0}\backslash G$ is an étale $A$-group.*

*(ii) Consequently, if $A = k$ is an algebraically closed field, $G^{0}\backslash G$ is a constant $k$-group, acting in
a simply transitive way on the set of connected components of $G$; hence if $G$ is algebraic, $G^{0}\backslash G$ is
finite.*

<!-- label: III.VI_A.5.5.1 -->

### 5.6

Let $k$ be a perfect field and $G$ a $k$-group locally of finite type. We have seen (0.2) that $G_{red}$ is then a group
subscheme of $G$. Moreover, the equivalence class of the origin of $G$ under the left action of $G_{red}$ on $G$ is the
whole underlying space of $G$. So, by Theorem 3.2, one obtains:

**Proposition 5.6.1.** *Let $k$ be a perfect field and $G$ a $k$-group locally of finite type. Then the $k$-scheme
$G_{red}\backslash G$ is the spectrum of a finite, local $k$-algebra with residue field $k$.*

<!-- label: III.VI_A.5.6.1 -->

[^N.D.E-VI_A-57] Indeed, by 3.2, $G_{red}\backslash G$ has a single point, with residue field $k$, and is a $k$-scheme
of finite type; it is therefore the spectrum of a local $k$-algebra of finite dimension (cf. EGA I, 6.4.4).

**Proposition 5.6.2.** *Let $u : F \to G$ be a morphism between groups locally of finite type over a perfect field $k$.
The following assertions are equivalent:*

*(i) $u$ is flat.*

*(ii) $u^{0} : F^{0} \to G^{0}$ is dominant and the morphism $v : F_{red}\backslash F \to G_{red}\backslash G$ induced
by $u$ is flat.*

<!-- label: III.VI_A.5.6.2 -->

<!-- original page 318 -->

[^N.D.E-VI_A-58] Indeed, consider the following commutative diagram:

```text
                p
F ─────────────→ F_red\backslash F

u                       v
        q
G ─────────────→ G_red\backslash G,
```

where $p$ and $q$ denote the canonical projections. By 3.2 (iv), $p$ and $q$ are faithfully flat; consequently, if $u$
is flat, then $q \circ u = v \circ p$ is flat, hence so is $v$.

Conversely, suppose $v$ flat and $u^{0}$ dominant. Since $u^{0}$ is quasi-compact ($F^{0}$ being of finite type over $k$
by 2.4, hence noetherian), it sends the generic point $\xi$ of $F^{0}$ to the generic point $\eta$ of $G^{0}$. Let $R$
be the finite local $k$-algebra of which $G_{red}\backslash G$ is the spectrum, and $\mathfrak{m}$ its maximal ideal.
One has local morphisms of local rings: $R \to O_{G,\eta} \to O_{F,\xi}$. Note that one has a cartesian square:

```text
G_red ──────────→ G

                  q
                  ▼
Spec(R/𝔪) ──→ Spec(R)
```

and so $O_{G,\eta}/\mathfrak{m} O_{G,\eta} \cong O_{G_{red}, \eta} = \kappa(\eta)$, so that $O_{F,\xi}/\mathfrak{m}
O_{F,\xi}$ is flat over $O_{G,\eta}/\mathfrak{m} O_{G,\eta}$.

On the other hand, since $q$ and $v \circ p$ are flat, $G$ and $F$ are flat over $R$. Consequently, by the local
flatness criterion (cf. EGA IV_3, 11.3.10.2), $O_{F,\xi}$ is flat over $O_{G,\eta}$, i.e. $u$ is flat at the point
$\xi$. So, by 2.5.3, $u$ is flat.

## 6. Complements on $k$-groups not necessarily of finite type

<!-- label: III.VI_A.6 -->

[^N.D.E-VI_A-59] Let us further point out the following results, which will be useful in the addendum VI_B, § 12. We fix
a base field $k$.

**Lemma 6.1.** *Let $G$ be a $k$-group. For every $x \in G$, there exists a point $u \in G \times G$ such that
`µ(u) = x` and that the two projections $p_{1}(u)$ and $p_{2}(u)$ are maximal points of $G$.*

<!-- label: III.VI_A.6.1 -->

<!-- original page 327 -->

*Proof.* Set $K = \kappa(x)$. Since the projection $G_{K} \to G$ sends maximal points to maximal points, one is reduced
to the case where $x$ is rational. Then left translation $\lambda_{x}$ (resp. right translation $\rho_{x}$) gives us a
morphism $G \to G \times G$, $g \mapsto (\lambda_{x}(g^{-1}), g)$ (resp. $g \mapsto (g, \rho_{x}(g^{-1}))$) which
induces an isomorphism of $G$ onto `µ⁻¹(x)`, inverse of $p_{2}$ (resp. $p_{1}$). So, if $u$ is a maximal point of
`µ⁻¹(x)`, then $p_{1}(u)$ and $p_{2}(u)$ are maximal points of $G$, and so $u$ is suitable.

**Corollary 6.2.** *Let $f : G \to H$ be a quasi-compact, dominant morphism of $k$-groups.*

*(i) $f$ is surjective.*

*(ii) If $H$ is reduced, $f$ is faithfully flat.*

<!-- label: III.VI_A.6.2 -->

*Proof.* Write `µ_H` (resp. `µ_G`) for the multiplication of $H$ (resp. $G$). Let $h \in H$. By 6.1, there exists $u \in
H \times H$ such that `µ_H(u) = h` and that $\alpha = p_{1}(u)$ and $\beta = p_{2}(u)$ are maximal points of $H$. Since
$f$ is quasi-compact and dominant, $f^{-1}(\alpha)$ and $f^{-1}(\beta)$ are non-empty (cf. EGA IV_1, 1.1.5), and so
there exists $v \in G \times G$ such that $(f \times f)(v) = u$ (cf. EGA I, 3.5.2). Then `g = µ_G(v)` satisfies $f(g) =
h$. This shows that $f$ is surjective.

Suppose in addition $H$ reduced. Then $O_{H,\alpha}$ is a field, and we have seen above that $f^{-1}(\alpha) \neq
\emptyset$, so $f$ is flat at every point $\xi$ of $f^{-1}(\alpha)$, so $f$ is flat by Lemma 2.5.3.

**Recollection 6.3.** *Recall (cf. EGA IV_3, 11.10.1) that a morphism of schemes $f : X \to Y$ is said to be*
schematically dominant *if it satisfies the following condition: for every open $U$ of $Y$, if $Z$ is a closed subscheme
of $U$ such that the morphism $f^{-1}(U) \to U$ factors through $Z$, then $Z = U$. When $f$ is quasi-compact and
quasi-separated, this is equivalent to saying that the closed image of $X$ by $f$ is $Y$ (cf. loc. cit., 11.10.3 (iv)
and EGA I, 9.5.8).*

<!-- label: III.VI_A.6.3 -->

**Proposition 6.4.** *Let $f : H \to G$ be a quasi-compact morphism of $k$-groups. Then the closed image of $f$ is a
group subscheme $H'$ of $G$, and $f$ factors as:*

```text
         f
H ────────────→ G
 \             ↗
  \          ↗
   f′      ↗ i
    ↘    ↗
     H′
```

*where $f'$ is schematically dominant, quasi-compact and surjective.*

<!-- label: III.VI_A.6.4 -->

*Proof.* Since $H$ is separated (0.3), $f$ is quasi-compact and separated, so $f_{*}(O_{H})$ is a quasi-coherent
`O_G`-module, and the closed image $H'$ of $f$ exists and is the closed subscheme of $G$ defined by the quasi-coherent
ideal $I = Ker(O_{G} \to f_{*}(O_{H}))$ (cf. EGA I, § 9.5).

<!-- original page 328 -->

Write $c_{G}$ and `µ_G` (resp. $c_{H}$ and `µ_H`) for the inversion and multiplication morphisms of $G$ (resp. $H$).
Then $c_{G} \circ f = f \circ c_{H}$ factors through the closed subscheme $c_{G}(H')$, whence $H' \subset c_{G}(H')$ and
so $H' = c_{G}(H')$ (since $c^{2}_{G} = id_{G}$). Similarly, since $f \circ \pi_{H} = \pi_{G} \circ (f \times f)$
factors through $H'$, then $f \times f$ factors through the closed subscheme $\pi^{-1}_{G}(H')$ of $G \times G$. On the
other hand, since the formation of the closed image commutes with flat base changes (EGA III 1.4.15 and IV_1 1.7.21),
the closed image of $f \times id_{H}$ (resp. $id_{H'} \times f$) is $H' \times H$ (resp. $H' \times H'$). So, by
"transitivity of closed images" (EGA I, 9.5.5), the closed image of $f \times f$ is $H' \times H'$, which is therefore
contained in $\pi^{-1}_{G}(H')$, i.e. the restriction of $\pi_{G}$ to $H' \times H'$ factors through $H'$. This shows
that $H'$ is a closed group subscheme of $G$. Write $i$ for the inclusion $H' \hookrightarrow G$.

Then $f$ equals $i \circ f'$, where $f' : H \to H'$ is schematically dominant and quasi-compact (since $f$ is
quasi-compact and $i$ is separated). So, by 6.2, $f'$ is surjective. This proves 6.4.

One can now state the following theorem ([Per75], V 3.1 & 3.2, see also [Per76], 0.0 & 0.1).

**Theorem 6.5 (D. Perrin).** *Let $G$ be a quasi-compact $k$-group. Then*

*(i) $G$ is the projective limit of a filtered system $(G_{i})$ of $k$-groups of finite type (whose transition morphisms
$u_{ij} : G_{j} \to G_{i}$ are affine for $i$ large enough), and the morphisms $G \to G_{i}$ are faithfully flat (and
affine for $i$ large enough).*

*(ii) Let $H$ be a closed $k$-subgroup of $G$. Then the (fpqc) quotient sheaf $\tilde{G}/H$ is a $k$-scheme in the
following two cases:*

*(1) The immersion $H \to G$ is of finite presentation; in this case, $G/H$ is of finite type over $k$.* *(2) $H$ is
normal in $G$.*

<!-- label: III.VI_A.6.5 -->

For the proof of this theorem (which rests on several intermediate theorems), we refer to [Per75]. For the reader's
convenience, let us however prove the two corollaries below, cf. [Per75] V 3.3 to 3.4 or [Per76] 4.2.3 to 4.2.5.

**Corollary 6.6.** *Let $f : G \to H$ be a quasi-compact morphism of $k$-groups.*

*(i) If $f$ is schematically dominant, it is faithfully flat.*

*(ii) This is the case, in particular, if $H$ is affine and the morphism $f^{\natural} : O(H) \to O(G)$ is injective.*

<!-- label: III.VI_A.6.6 -->

*Proof.* Suppose $f$ schematically dominant. Then, by 6.2 (i), $f$ is surjective, so, by 2.5.3, it suffices to show that
$f$ is flat at the unit element of $G$. Since $O_{H,e} = O_{H^{0},e}$ (cf. 2.6.5), one may replace $H$ by $H^{0}$, and
hence assume $H$ irreducible. Then $H$ is quasi-compact (loc. cit.), and since $f$ is quasi-compact, so is $G$. By 6.5
(i), $H = \lim_{i} H_{i}$, where each $H_{i}$ is an algebraic $k$-group. Denote by $N_{i}$ the kernel of $G \to H_{i}$;
this is a closed normal $k$-subgroup of $G$. Moreover, since the unit section ${e} \to H_{i}$ is of finite presentation,
the immersion $N_{i} \to G$ is

<!-- original page 329 -->

also so; so, by 6.5 (ii), the (fpqc) quotient $G/N_{i}$ is an algebraic $k$-group. One has then a commutative diagram

```text
         f
G ──────────────→ H
 q_i               p_i
        f_i
G/N_i ──────────→ H_i
```

where $f$ is schematically dominant, $p_{i}, q_{i}$ are faithfully flat (hence schematically dominant). Then $f_{i}
\circ q_{i} = p_{i} \circ f$ is schematically dominant, and so $f_{i}$ is also so. On the other hand, $f_{i}$ is a
monomorphism, hence a closed immersion, since $G/N_{i}$ and $H_{i}$ are algebraic (2.5.2). It follows that $f_{i}$ is an
isomorphism, and so $G \to H_{i}$ is faithfully flat. Then, by [BAC] I § 2.7, Prop. 9, the morphism $G \to H$ is flat;
on the other hand, it is surjective by 6.2 (i), so it is faithfully flat. This proves point (i); and point (ii) follows,
since if $H$ is affine and $f^{\natural}$ injective, then the closed image of $f$ equals $H$, so $f$ is schematically
dominant (cf. 6.4).

**Corollary 6.7.** *Let $u : G \to H$ be a morphism of $k$-groups and $N = Ker(u)$. Suppose $u$ quasi-compact.*

*(i) The (fpqc) quotient sheaf $\tilde{G}/N$ is represented by a $k$-group scheme $G/N$, and $u$ factors as:*

```text
            u
G ────────────────→ H
 \                 ↗
  p              ↗
   \           ↗ i
    ↘        ↗
     G/N
```

*where $p$ is faithfully flat and $i$ a closed immersion.*

*(ii) In particular, if $u$ is a monomorphism, $u$ is a closed immersion, and if $u$ is schematically dominant, $u$ is
faithfully flat.*

<!-- label: III.VI_A.6.7 -->

*Proof.* (i) By 6.4 and 6.6, the closed image $G'$ of $u$ is a closed group subscheme of $G$, and $p : G \to G'$ is
faithfully flat and quasi-compact. One evidently has $Ker(p) = Ker(u) = N$, and so by Exp. IV, 3.3.2.1 and 5.1.7, $G'$
represents the (fpqc) quotient sheaf $\tilde{G}/N$.

(ii) The second assertion is contained in 6.6; let us show the first. If $u$ is a monomorphism, so is $p$; then $p$ is
at once a monomorphism and an effective epimorphism, hence an isomorphism (cf. IV, 1.14). This proves 6.7.

Let us finally point out the following corollaries (cf. [Per76], 4.2.6 to 4.2.8).

**Corollary 6.8.** *The category of commutative quasi-compact $k$-group schemes is abelian.*

<!-- label: III.VI_A.6.8 -->

Taking 6.7 into account, the proof is analogous to that of 5.4.2.

**Corollary 6.9.** *If $char(k) = 0$, every $k$-group scheme $G$ is geometrically reduced.*

<!-- label: III.VI_A.6.9 -->

<!-- original page 330 -->

Indeed, if $g \in G$ and if $K$ is an algebraic closure of $\kappa(g)$, one has $O_{G,e} \otimes_{k} K \simeq O_{G_{K},
g_{K}}$, so it suffices to show that $O_{G,e} = O_{G^{0}, e}$ is geometrically reduced. One is thus reduced to the case
where $G$ is connected, hence quasi-compact (2.6.5). Then the result follows from 6.5 and from Cartier's theorem for
algebraic groups (cf. VI_B, 1.6.1 or [DG70] § II.6, Th. 1.1).

**Corollary 6.10.** *Let $G$ be a quasi-compact $k$-group. Assume $k$ algebraically closed.*

*(i) Let $f : G \to H$ be a faithfully flat morphism of $k$-groups. Then the induced map $G(k) \to H(k)$ is surjective.*

*(ii) The set of rational points is dense in $G$.*

<!-- label: III.VI_A.6.10 -->

For the proof, we refer to [Per75], V 3.7 & 3.9.

## Bibliography

[^N.D.E-VI_A-60]

**[An73]** S. Anantharaman, *Schémas en groupes, espaces homogènes et espaces algébriques sur une base de dimension 1*,
Mém. Soc. Math. France **33** (1973), 5–79.

**[BAC]** N. Bourbaki, *Algèbre commutative*, Chap. I–IV et V–VII, Masson, 1985.

**[DG70]** M. Demazure, P. Gabriel, *Groupes algébriques*, Masson & North-Holland, 1970.

**[Per75]** D. Perrin, *Schémas en groupes quasi-compacts sur un corps*, Publ. Math. Orsay N° 165–75.46 (1ère partie),
<http://portail.mathdoc.fr/PMO/>

**[Per76]** D. Perrin, *Approximation des schémas en groupes, quasi-compacts sur un corps*, Bull. Soc. Math. France
**104** (1976), 323–335.

**[Ray67a]** M. Raynaud, *Passage au quotient par une relation d'équivalence plate*, pp. 78–85 in: Proc. Conf. Local
Fields (Driebergen) (ed. T. A. Springer), Springer-Verlag, 1967.

**[Ray67b]** M. Raynaud, *Sur le passage au quotient par un groupoïde plat*, C. R. Acad. Sci. Paris (Sér. A) **265**
(1967), 384–387.

**[Ray70]** M. Raynaud, *Faisceaux amples sur les schémas en groupes et les espaces homogènes*, Lect. Notes Maths.
**119**, Springer-Verlag, 1970.

## Footnotes

<!-- LEDGER DELTA — Exposé VI_A — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| anneau local artinien | Artinian local ring | Standard. |
| corps résiduel | residue field | Already in glossary. |
| `A`-groupe | `A`-group | Shorthand for group scheme over `Spec A`. |
| algébrique (groupe) | algebraic (group) | Underlying scheme of finite type over `A`. |
| localement de type fini | locally of finite type | Standard. |
| de type fini | of finite type | Standard. |
| composante neutre | neutral component | The connected component of the identity, denoted `G⁰`. |
| composante connexe | connected component | Standard. |
| strictement rationnel | strictly rational | Used by Gabriel: a point with a chosen `A`-section through it. |
| rendre strictement rationnel | make strictly rational | Gabriel's coinage. |
| sous-groupe distingué | normal subgroup | Standard English does not distinguish "distingué"/"normal". |
| sous-groupe caractéristique | characteristic subgroup | Standard. |
| sous-groupe radical | (not used here) | — |
| saturé | saturated | For an equivalence relation: stable under the relation. |
| « rendre rationnel » | "make rational" | Gabriel's metaphor, preserved with quotes. |
| quotient à gauche `F\backslash G` | left quotient `F\backslash G` | Standard notation; preserve backslash. |
| conoyau (du groupoïde) | cokernel (of the groupoid) | Standard. |
| groupoïde | groupoid | Standard. |
| quasi-section | quasi-section | Standard. |
| ouvert et saturé | open and saturated | Standard. |
| descente fppf / fpqc | fppf / fpqc descent | Standard. |
| schématiquement dominant | schematically dominant | EGA IV term. |
| image fermée | closed image | EGA I term. |
| Nakayama nilpotent | nilpotent Nakayama | Standard. |
| limite projective | projective limit | The source uses both; modern English often says inverse limit, but the Exposé style here keeps "projective limit". |
| clôture parfaite | perfect closure | Standard; written `k^{p^{-∞}}` or `k′`. |
| clôture algébrique | algebraic closure | Standard. |
| point maximal | maximal point | Equivalent to "generic point of an irreducible component" in this setting. |
| générisation | generization | Standard. |
| rétrocompact | retrocompact | EGA term. |
| translation à gauche / à droite | left / right translation | Standard. |
| `Gréd` | `G_red` | Reduced scheme associated to `G`. |
| `D_k(M)` | `D_k(M)` | Cartier dual, as in Exp. VIII. |
| Bible (Séminaire Chevalley) | the *Bible* | Not used here; mentioned only via VI_B/VII_B cross-refs. |
-->

[^N.D.E-VI_A-0]: N.D.E.: Version of 13/10/2024.

[^N.D.E-VI_A-1]: N.D.E.: The sentences that follow have been added.

[^N.D.E-VI_A-2]: N.D.E.: For examples of group schemes $G$ over a non-perfect field $k$ such that $G_{red}$ is not a
    group scheme over $k$, see 1.3.2 below.

[^N.D.E-VI_A-3]: N.D.E.: We have slightly modified what follows of 0.2, as well as 0.3.

[^N.D.E-VI_A-4]: N.D.E.: To have an analogous example with $G$ connected, one may consider, for $char(k) = p > 0$, the
    semidirect product of $\alpha_{p,k}$ and $G_{m,k}$.

[^N.D.E-VI_A-5]: N.D.E.: This argument is valid for every local ring $A$ of dimension zero, and shows that if $S$ is a
    discrete scheme, every $S$-group is separated, cf. VI_B, 5.2; on the other hand (cf. VI_B, 5.6.4), if $S$ contains a
    closed point $s$ that is not isolated, the $S$-scheme $G$ obtained by gluing two copies of $S$ along the open subset
    $S - {s}$ is not separated over $S$, but is equipped with an $S$-group structure.

[^N.D.E-VI_A-6]: N.D.E.: We have detailed the original in what follows, in particular we have added Remark 0.4.1.

[^N.D.E-VI_A-7]: N.D.E.: The original stated this result under the hypothesis that $G$ is locally of finite type over
    $A$. Since it is useful to have it available in the general case, and since the proof is essentially the same, we
    have stated and proved the result in the general case. This will be used several times in what follows.

[^N.D.E-VI_A-8]: N.D.E.: We have inserted this corollary here, cf. 2.4 and 2.6.2 below.

[^N.D.E-VI_A-9]: N.D.E.: We have added this corollary, used implicitly in VIII, 6.7; see also VI_B 6.2.5.

[^N.D.E-VI_A-10]: N.D.E.: For example, they are always complete intersections, cf. VII_B, 5.5.1. Moreover, if $char(k) =
    0$ then $G$ is smooth (VI_B, 1.6.1; see also VII_B, 3.3.1).

[^N.D.E-VI_A-11]: N.D.E.: Indeed, the hypothesis on $K$ entails that, for every extension $L$ of $K$, every $k$-morphism
    $\kappa(x) \to L$ (resp. $\kappa(y) \to L$) factors through $K$; consequently, all points of $G \otimes_{k} K$ above
    $x$ or $y$ have $K$ as residue field, i.e. are (strictly) rational over $K$.

[^N.D.E-VI_A-12]: N.D.E.: Indeed, $B$ is a noetherian Jacobson ring (cf. [BAC], V § 3.4). If every non-invertible
    element is a zero-divisor, then every prime ideal is an associated prime ideal of $B$, so in particular $B$ has only
    a finite number of maximal ideals $\mathfrak{m}_{1}, \cdots, \mathfrak{m}_{n}$. Since $B$ is a Jacobson ring, the
    intersection of the $\mathfrak{m}_{i}$ is the nilradical of $B$, and it follows that each $\mathfrak{m}_{i}$ is a
    minimal prime ideal of $B$, so that $\dim B = 0$.

[^N.D.E-VI_A-13]: N.D.E.: We have detailed the original in what follows.

[^N.D.E-VI_A-14]: N.D.E.: We have added point (1), useful in the examples 1.3.2 that follow.

[^N.D.E-VI_A-15]: N.D.E.: We have added the sentence that follows and the examples 1.3.2.

[^N.D.E-VI_A-16]: N.D.E.: In fact one sees without difficulty that $\sqrt{I}$ is generated by `P, Q, R` at every point
    $\neq 0$, so $F = H$.

[^N.D.E-VI_A-17]: N.D.E.: We shall see below (2.2) that $G'$ is a group in the category $(Sch/k)_{red}$.

[^N.D.E-VI_A-18]: N.D.E.: We have added the word "locally". Moreover, the reference to Kaplansky is: *Projective
    modules*, Ann. of Maths. **68** (1958), 372–377; see also [BAC], § II.3, Ex. 3.

[^N.D.E-VI_A-19]: N.D.E.: We have detailed the original in what follows.

[^N.D.E-VI_A-20]: N.D.E.: We have added this paragraph, in order to make the link with VI_B, § 3.

[^N.D.E-VI_A-21]: N.D.E.: In this Exposé, the notation $G^{0}$ is reserved for the case where the connected component of
    $e$ is open; in VI_B, § 3, this connected component will be denoted $G^{0}$ in all cases. This is a slightly abusive
    notation, but one that is compatible with what precedes when the connected component is the underlying topological
    space of an open group subscheme $G^{0}$ of $G$.

[^N.D.E-VI_A-22]: N.D.E.: Indeed, in a noetherian space, the connected components are finite in number, hence each one
    is open; see also EGA I, 6.1.9.

[^N.D.E-VI_A-23]: N.D.E.: We have added the numbering 2.3.1 to make this statement explicit. Note moreover that $G^{0}$
    is even a characteristic subgroup of $G$, cf. 2.6.5 (ii).

[^N.D.E-VI_A-24]: N.D.E.: In the statement, we have replaced "$G^{0}$ is geometrically irreducible" by "$G^{0}
    \otimes_{A} k$ is geometrically irreducible over $k$", and we have detailed the proof.

[^N.D.E-VI_A-25]: N.D.E.: We have detailed the original by adding the reference to EGA I, 6.1.10.

[^N.D.E-VI_A-26]: N.D.E.: One should beware that a non-neutral connected component is not in general geometrically
    connected. For example, if $k = \mathbb{R}$, the group `µ_{3,ℝ}`, represented by $\mathbb{R}[X]/(X^{3} - 1)$, has
    two connected components: ${e} = \operatorname{Spec} \mathbb{R}$ and $C = \operatorname{Spec} \mathbb{R}[X]/(X^{2} +
    X + 1)$, and $C \otimes_{\mathbb{R}} \mathbb{C}$ has two components.

[^N.D.E-VI_A-27]: N.D.E.: We have added the assertion that follows, cf. VI_B, 1.5.

[^N.D.E-VI_A-28]: N.D.E.: We have detailed the original in what follows.

[^N.D.E-VI_A-29]: N.D.E.: We have simplified the original here.

[^N.D.E-VI_A-30]: N.D.E.: We make no finiteness hypotheses in this statement; this will be useful later (cf. 6.2 and
    VI_B, § 12).

[^N.D.E-VI_A-31]: N.D.E.: These results were communicated to us by O. Gabber, in particular 2.6.6, which plays an
    important role in section 5 of VI_B.

[^N.D.E-VI_A-32]: N.D.E.: This proposition (as well as the preceding results) was communicated to us by O. Gabber; it
    will be used to correct the proof of Theorem 5.3 of VI_B.

[^N.D.E-VI_A-33]: N.D.E.: We have added (ii′) and detailed point (iv), taking into account the additions made in 2.5.2,
    2.5.4, and in Exp. V, 6.1.

[^N.D.E-VI_A-34]: N.D.E.: In this case, the hypothesis that $G$ is flat may be removed, cf. subsection 3.3.

[^N.D.E-VI_A-35]: N.D.E.: Let us point out here that if $A = k$ is a field, then every quasi-compact open of
    $F\backslash G$ is quasi-projective (a result due to Chow for smooth algebraic groups), cf. [Ray70], VI 2.6. By
    contrast, over the Artinian local ring $A = \mathbb{C}[\epsilon]/(\epsilon^{2})$, there exist abelian $A$-schemes
    $G$ that are not projective (loc. cit., XII 4.2).

[^N.D.E-VI_A-36]: N.D.E.: What precedes is valid for every base change $A \to A'$.

[^N.D.E-VI_A-37]: N.D.E.: This is detailed in 4.6 below: it is a matter of seeing that the formation of the direct image
    by the morphisms $p$, $\lambda$ and $pr_{2}$ commutes with flat base changes $A \to A'$. Since $F$ and $G$ are of
    finite type over the Artinian ring $A$, the morphisms $f$ in question are all quasi-compact and quasi-separated, and
    the equality $f_{*}(O_{X}) \otimes_{A} A' = f'_{*}(O_{X'})$ (with obvious notations) follows from EGA IV_1, 1.7.21.

[^N.D.E-VI_A-38]: N.D.E.: Indeed, let $y_{1}, \cdots, y_{n}$ be arbitrary points of $X$; since $X$ is of finite type
    over $A$, each $y_{i}$ has in its closure a closed point $x_{i}$, and every open subset containing $x_{i}$ contains
    $y_{i}$.

[^N.D.E-VI_A-39]: N.D.E.: Such an open exists, since $X$ is of finite type over $k$: $X$ has a finite number of
    irreducible components $C_{1}, \cdots, C_{p}$, and it suffices to take, for each $i$, a non-empty affine open
    contained in $C_{i} - \bigcup_{j \neq i} C_{j}$. (Here one knows moreover, by (ii′), that the $C_{i}$ are disjoint…)

[^N.D.E-VI_A-40]: N.D.E.: We have detailed the original in what follows.

[^N.D.E-VI_A-41]: N.D.E.: We have added this paragraph.

[^N.D.E-VI_A-42]: N.D.E.: We have added this subsection.

[^N.D.E-VI_A-43]: N.D.E.: For an example where $F$ is not flat and $\tilde{F}\backslash G$ not representable, see
    [DG70], § III.3, n° 3.3.

[^N.D.E-VI_A-44]: N.D.E.: We have written $S(G^{\alpha})$ instead of $\bar{G}^{\alpha}$ for the saturation of
    $G^{\alpha}$.

[^N.D.E-VI_A-45]: N.D.E.: We have added the sentence that follows.

[^N.D.E-VI_A-46]: N.D.E.: In what follows, we have modified the original; the supplementary hypotheses made on $X_{*}$
    were superfluous.

[^N.D.E-VI_A-47]: N.D.E.: We have added on the one hand the following sentence and, on the other hand, the numbering
    4.6.1 below, to make the stated result explicit.

[^N.D.E-VI_A-48]: N.D.E.: We have added the numbering 4.7.1 below to make the stated result explicit.

[^N.D.E-VI_A-49]: N.D.E.: We have changed the title of this section (called "Compléments" in the original).

[^N.D.E-VI_A-50]: N.D.E.: We have added what follows.

[^N.D.E-VI_A-51]: N.D.E.: We have added the sentence that follows.

[^N.D.E-VI_A-52]: N.D.E.: In addition to the aforementioned statements of Exp. IV, one uses the fact that, since $G \to
    F\backslash G$ is faithfully flat, an $A$-subgroup $H$ of $G$ is flat over $A$ if and only if $F\backslash H$ is.

[^N.D.E-VI_A-53]: N.D.E.: We have detailed the original in what follows; in particular, we have added Proposition 5.4.1.

[^N.D.E-VI_A-54]: N.D.E.: We have added the number 5.4.2 to this theorem.

[^N.D.E-VI_A-55]: N.D.E.: We have added what follows.

[^N.D.E-VI_A-56]: N.D.E.: We have detailed the original in what precedes and have added Proposition 5.5.1 to make this
    result explicit.

[^N.D.E-VI_A-57]: N.D.E.: We have added the numbering 5.6.1, as well as the proof that follows.

[^N.D.E-VI_A-58]: N.D.E.: We have detailed the proof of (ii) ⇒ (i), and have simplified the diagram below.

[^N.D.E-VI_A-59]: N.D.E.: We have added the results that follow, taken from [Per75]. Note that Lemma 6.1 can be
    expressed, in Weil's language, by saying that "every point of $G$ is the product of two generic points".

[^N.D.E-VI_A-60]: N.D.E.: Additional references cited in this Exposé.
