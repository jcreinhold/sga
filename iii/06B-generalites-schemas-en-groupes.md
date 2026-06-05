# Exposé VI_B. Generalities on group schemes

<!-- label: III.VI_B -->

*by J.-E. Bertin*

> [^N.D.E-VI_B-0] Version of 13/10/2024.

<!-- original page 319 -->

This Exposé, which corresponds to no oral lecture of the seminar, is intended to bring together a number of technical
results, commonly used, concerning group schemes.[^VI_B-0-1]

## 1. Morphisms of groups locally of finite type over a field

<!-- label: III.VI_B.1 -->

### 1.1.

Let $A$ be an Artinian local ring, $G$ and $H$ two $A$-groups[^N.D.E-VI_B-2], and $u : G \to H$ a morphism of
$A$-groups. Then $u$ induces a morphism of groups $u(A) : G(A) \to H(A)$.[^N.D.E-VI_B-3] Since $H(A)$ acts on $H$ by
right translation, $u(A)$ defines, by restriction, an action of $G(A)$ on $H$. This action is compatible with the
morphism $u$ and with the action of $G(A)$ on $G$ defined by right translation. Since $G(A)$ acts transitively on the
strictly rational points of $G$ (see (VI_A, 0.4) for the definition), one sees that these points "all behave in the same
way with respect to $u$"; from this spring the following properties.

**Proposition 1.2.** *Let $u : G \to H$ be a quasi-compact morphism between $A$-groups locally of finite type over $A$.
Then the set $u(G)$ is closed in $H$ and one has `dim G = dim u(G) + dim Ker u`.*[^N.D.E-VI_B-4]

<!-- label: III.VI_B.1.2 -->

<!-- original page 320 -->

Since $u$ commutes with the inversion morphisms of $G$ and $H$, the image $u(G)$ is invariant under the inversion
morphism of $H$; the same is therefore true of its closure $u(G)^{-}$ in $H$. On the other hand, let $L$ denote the set
of points of $H \times_{A} H$ whose two projections both lie in $u(G)$; it is clear that $L$ is the image of the
morphism $u \times_{A} u : G \times_{A} G \to H \times_{A} H$. Hence the multiplication morphism of $H$ sends $L$ into
$u(G)$, in other words $u(G) \cdot u(G) = u(G)$. On the other hand, Lemma 1.2.1 below shows that $L^{-}$, the closure of
$L$ in $H \times_{A} H$, is the set of points of $H \times_{A} H$ whose two projections lie in $u(G)^{-}$; hence
$u(G)^{-} \cdot u(G)^{-} = u(G)^{-}$, so that the reduced subscheme of $H$ whose underlying space is $u(G)^{-}$ is
naturally equipped with a group structure in the category $(Sch/k)_{red}$, where $k$ is the residue field of $A$ (cf.
(VI_A, 0.2)).

Let us prove the first assertion of 1.2. Replacing $A$ by the algebraic closure of its residue field $k$, we may assume
that $A$ is an algebraically closed field $k$ (cf. EGA IV₂, 2.3.12). Replacing $u$ by `u_red : G_red → H_red`, we may
assume $G$ and $H$ reduced; in this case, as we have just seen, $u(G)$ is the underlying space of a reduced group
subscheme of $G$; we may therefore assume $u$ dominant. Then $G(k)$ acts transitively on the set of connected components
of $H$, and it suffices to show that $u(G) \cap H^{0}$ is closed: we are reduced to the case where $H$ is connected,
hence irreducible and of finite type (VI_A, 2.4). Then $u$ is of finite type, since it is quasi-compact and locally of
finite type; since $H$ is noetherian, $u(G)$ is constructible (EGA IV₁, 1.8.5), so it contains an open subset $V$ of $H$
(EGA 0_III, 9.2.2), and then, by (VI_A, 0.5), we have $H = V \cdot V \subset u(G) \cdot u(G) = u(G)$.

Let us prove the second assertion. Recall first that the functor `Ker u` (cf. I, 2.3.6.1) is representable by
$u^{-1}(e)$, where $e$ denotes the unit element of $H$. When $u$ is locally of finite type, `Ker u` is therefore locally
of finite type over $A$. We reduce as before, this time using EGA IV₂, 4.1.4, to the case where $A$ is an algebraically
closed field $k$.

<!-- original page 321 -->

We may further assume $G$ and $H$ irreducible and of finite type and $u$ dominant: indeed, $k$ being algebraically
closed, it is clear that the connected components of $G$, on the set of which $G(k)$ acts transitively, all have the
same dimension, and that if $u^{0}$ denotes the restriction of $u$ to $G^{0}$, then $(Ker u)^{0} \subset Ker u^{0}$, and
`dim Ker u⁰ = dim Ker u`. One sees likewise that $u$ is then of finite type over $k$. If $\eta$ denotes the generic
point of $H$, one has `dim u⁻¹(η) = dim G − dim H` (EGA IV₃, 10.6.1 (ii)). By EGA IV₃, 9.2.3 and 9.2.6, the set of $y
\in H$ such that $\dim u^{-1}(y) = \dim u^{-1}(\eta)$ contains a non-empty open subset $V$. Since $u$ is dominant, $U =
u^{-1}(V)$ is then a non-empty open subset of $G$ and contains a closed point $x$ of $G$, since $G$ is a Jacobson scheme
(EGA IV₃, 10.4.7). Then right translation $r_{x}$ is an isomorphism of `Ker u` onto $u^{-1}(u(x))$, so that:

```text
dim Ker u = dim u⁻¹(u(x)) = dim u⁻¹(η) = dim G − dim H.
```

**Lemma 1.2.1.** *Let $f : X' \to X$ and $g : Y' \to Y$ be two quasi-compact, dominant morphisms of schemes over an
Artinian local ring $A$. Then $f \times_{A} g : X' \times_{A} Y' \to X \times_{A} Y$ is dominant (and quasi-compact).*

<!-- label: III.VI_B.1.2.1 -->

Indeed, one has $f \times_{A} g = (id_{X} \times_{A} g) \circ (f \times_{A} id_{Y'})$. It therefore suffices to show
that $f \times_{A} id_{Y'}$ and $id_{X} \times_{A} g$ are dominant. For this one may replace $A$ by its residue field
$k$. In this case, $X$ and $Y'$ are flat over $A = k$, and since $f \times_{A} id_{Y'}$ (resp. $id_{X} \times_{A} g$) is
deduced from $f$ (resp. $g$) by the flat base change $Y' \to A$ (resp. $X \to A$), it is dominant (and quasi-compact),
by EGA IV₂, 2.3.7.

<!-- original page 333 -->

**Counterexample 1.2.2.** *Let $k$ be a field of characteristic 0, $G$ the constant $k$-group $\mathbb{Z}$, and $H$ the
additive $k$-group $G_{a,k}$. Let $u : G \to H$ be a morphism of $k$-groups. If $u \neq 0$, then $u(G)$ is not closed in
$H$.*

<!-- label: III.VI_B.1.2.2 -->

**Proposition 1.3.** [^N.D.E-VI_B-5] *Let $A$ be an Artinian local ring, $k$ its residue field, $G$ an $A$-group locally
of finite type and flat, $u : G \to H$ a morphism of $A$-groups. The following assertions are equivalent:*

*(i) $u$ is flat (resp. quasi-finite, resp. unramified, resp. smooth, resp. étale) at some point of $G$.*[^N.D.E-VI_B-6]

*(ii) $u$ is flat (resp. quasi-finite, resp. unramified, resp. smooth, resp. étale).*

<!-- label: III.VI_B.1.3 -->

*Proof.* It suffices to show that (i) implies (ii). First, we have the following lemma.

**Lemma 1.3.0.** *Let $A \to B \to C$ be morphisms of commutative rings and let $n$ be a nilpotent ideal of $A$. Suppose
that $C/nC$ is a $(B/nB)$-algebra of finite type.*

*(i) Then $C$ is a $B$-algebra of finite type.*

*(ii) Moreover, if $C$ is flat over $A$ and if $C/nC$ is a $(B/nB)$-algebra of finite presentation, then $C$ is a
$B$-algebra of finite presentation.*

<!-- label: III.VI_B.1.3.0 -->

Indeed, let $x_{1}, \cdots, x_{n}$ be elements of $C$ whose images generate $C/nC$ as a $(B/n)$-algebra. By the
nilpotent Nakayama lemma, the $x_{i}$ generate $C$ as a $B$-algebra. This proves (i). Let $\phi$ be the resulting
surjective morphism $B[X_{1}, \cdots, X_{n}] \to C$, and let $I = Ker(\phi)$.

Suppose now that $C$ is flat over $A$ and that $C/nC$ is of finite presentation over $B/nB$. Then, on the one hand,
$I/nI$ is identified with the kernel of $\bar{\phi} = \phi \otimes_{A} (A/n)$. On the other hand, by EGA IV₁, 1.4.4, the
kernel of $\bar{\phi}$ is an ideal of finite type. Let then $P_{1}, \cdots, P_{s}$ be elements of $I$ whose images
generate $I/nI$ as an ideal; by the nilpotent Nakayama lemma, they generate $I$. This proves (ii).

Let us return to the proof of 1.3. Let $x$ be an arbitrary point of $G$. Since $G$ is flat over $A$, the fiber-wise
flatness criterion in the form of EGA IV₃, 11.3.10.2, shows that $u$ is flat at $x$ if $u \otimes_{A} k$ is. Likewise,
by the preceding lemma, one sees that $u$ is of finite type (resp. of finite presentation) at $x$ if $u \otimes_{A} k$
is. Since the other properties are then verified on fibers (cf. EGA IV₄, 17.4.1, 17.5.1, and 17.6.1, for unramified,
smooth, and étale), we are reduced to the case $A = k$.

<!-- original page 334 -->

Let now $x$ be a point of $G$ where one of the conditions of 1.3 (i) holds. Since the properties under consideration are
preserved by (fpqc) descent (cf. EGA IV, 2.5.1, 2.7.1, and 17.7.1), one reduces, by replacing $k$ by an algebraic
closure of $\kappa(x)$, to the case where $k$ is algebraically closed and $x \in G(k)$.

Since $G$ is a Jacobson scheme (cf. EGA IV₃, 10.4.7) and since the set $W$ of points of $G$ where $u$ is flat (resp.
quasi-finite, unramified, smooth, or étale) is stable under generization[^N.D.E-VI_B-7] (resp. open), it suffices to
show that every point $y \in G(k)$ belongs to $W$. Now, for such a point $y$, the translation $r_{y} \circ r^{-1}_{x}$
sends $x$ to $y$, hence $u$ has the desired property at $y$, i.e. $y \in W$. ∎

**Corollary 1.3.1.** *Let $A$ be an Artinian local ring, $k$ its residue field, $G$ a flat $A$-group. The following
assertions are equivalent:*[^N.D.E-VI_B-8]

*(i) $G$ is locally quasi-finite (resp. unramified, resp. smooth, resp. étale) over $A$ at some point.*

*(ii) $G$ is locally quasi-finite (resp. unramified, resp. smooth, resp. étale) over $A$.*

<!-- label: III.VI_B.1.3.1 -->

[^N.D.E-VI_B-9] *Proof.* Indeed, if $G$ satisfies one of the conditions of (i) at a point $x$, there exists an open
neighborhood $U$ of $x$ which is of finite type over $A$. Consequently, it suffices to apply 1.3 in the case where $H$
is the unit $A$-group, taking into account the following lemma. ∎

**Lemma 1.3.1.1.** *Let $A$ be an Artinian local ring and $G$ an $A$-group. If there exists a non-empty open subset of
$G$ of finite type over $A$, then $G$ is locally of finite type over $A$.*

<!-- label: III.VI_B.1.3.1.1 -->

By Lemma 1.3.0, we may assume $A$ equal to its residue field $k$. Moreover, by (fpqc) descent, we may assume $k$
algebraically closed (cf. EGA IV₂, 2.7.1). Let $V$ be the open subset of $G$ formed by the points where $G$ is of finite
type over $k$; by hypothesis, $V \neq \emptyset$. Since $G$ is a Jacobson scheme, $V$ contains a closed point $x$ and,
to show that $V = G$, it suffices to show that every closed point $y$ of $G$ belongs to $V$. Now, for such a point $y$,
the translation $r_{y} \circ r^{-1}_{x}$ sends $x$ to $y$, whence $y \in V$. ∎

**Corollary 1.3.2.** *Let $A$ be an Artinian local ring, $u : G \to H$ a morphism between $A$-groups locally of finite
type. The following assertions are equivalent:*

*(i) $u$ is universally open,*

*(ii) $u$ is open,*

*(iii) $u$ is open at some point of $G$,*

*(iv) the morphism $u^{0} : G^{0} \to H^{0}$ deduced from $u$ is dominant,*

*(iv′) $u^{0}$ is surjective,*

*(v) there exists a connected component $C$ of $G$ such that, if $D$ denotes the connected component of $H$ containing
$u(C)$, the morphism $u' : C \to D$ deduced from $u$ is dominant.*

<!-- label: III.VI_B.1.3.2 -->

*Proof.* The implications (i) ⇒ (ii) ⇒ (iii) and (iv′) ⇒ (iv) ⇒ (v) are clear. Since $G^{0}$ is of finite type over $A$
(VI_A, 2.4), and hence noetherian, $u^{0}$ is quasi-compact, so $u^{0}(G^{0})$ is closed in $H^{0}$ by 1.2; hence (iv) ⇒
(iv′). On the other hand, since $G^{0}$ (resp. $C$) is open in $G$ (VI_A, 2.3) and $H^{0}$ (resp. $D$) is irreducible
(VI_A, 2.4.1), one sees that (ii) implies (iv) (resp. (iii) implies (v)). It remains to show that (v) implies (i).

<!-- original page 324 -->

The open subset $C$ (resp. $D$) of $G$ (resp. $H$) will be endowed with its induced scheme structure, and $u'$ will
denote the morphism $C \to D$ deduced from $u$. Let $k$ be the residue field of $A$.[^N.D.E-VI_B-10] Since the base
change $\operatorname{Spec} k \to \operatorname{Spec} A$ is a universal homeomorphism, we may assume $A = k$. By
hypothesis, $u'$ is dominant and, since $C$ is of finite type over $k$ (VI_A, 2.4.1) and hence noetherian, $u'$ is
quasi-compact. By EGA IV₂, 2.3.7, $u' \otimes_{k} \bar{k}$ is again quasi-compact and dominant, where $\bar{k}$ denotes
an algebraic closure of $k$. Then, since $C \otimes_{k} \bar{k}$ is a union of connected components of $G \otimes_{k}
\bar{k}$, the morphism $u \otimes_{k} \bar{k} : G \otimes_{k} \bar{k} \to H \otimes_{k} \bar{k}$ satisfies assertion
(v). We are thus reduced to the case where $A = k$ is an algebraically closed field, taking into account EGA IV₂, 2.6.4.

In this case, we may further replace $u$ by $u_{red}$, and we are reduced to the case where $H$ is reduced. Let then
$\xi$ (resp. $\eta$) be the generic point of $C$ (resp. $D$). Since $u'$ is quasi-compact and dominant, $u'(\xi) = \eta$
(cf. EGA IV₁, 1.1.5). On the other hand, since $H$ is reduced, the local ring $O_{H,\eta}$ is a field, hence $u'$ is
flat at the point $\xi$.[^N.D.E-VI_B-11] Hence, by 1.3, $u$ is flat; moreover, since $u$ is locally of finite type and
$H$ is locally noetherian, $u$ is locally of finite presentation. Therefore, by EGA IV₂, 2.4.6, $u$ is universally open.
∎

**Proposition 1.4.** *Let $A$ be an Artinian local ring, and $u : G \to H$ a quasi-compact morphism between $A$-groups
locally of finite type. The following assertions are equivalent:*

*(i) $u$ is proper,*

*(ii) there exists $h \in H$ such that the fiber $u^{-1}(h)$ is non-empty and proper over $\kappa(h)$,*

*(iii) `Ker u` is proper over $A$.*

<!-- label: III.VI_B.1.4 -->

*Proof.* It is clear that (i) implies (iii), and that (iii) implies (ii). On the other hand, it follows from the
hypotheses that $u$ is of finite type and, since $G$ is separated (VI_A, 0.3), so is $u$ (EGA I, 5.5.1). It therefore
remains to show that assertion (ii) implies that $u$ is universally closed, so that we may assume $A$ equal to its
residue field $k$.[^N.D.E-VI_B-12] Let $k'$ be an algebraic closure of $\kappa(h)$, $u' : G' \to H'$ the morphism
deduced from $u$ by base change, and $h'$ a point of $H'$ above $h$; then the fiber $u'^{-1}(h') = u^{-1}(h)
\times_{\kappa(h)} k'$ is non-empty and proper, and it suffices to show that $u'$ is proper (EGA IV₂, 2.6.4). We may
therefore assume that $k$ is algebraically closed and $h \in H(k)$.

<!-- original page 336 -->

We have seen (1.2) that $u(G)$ is then the underlying set of a closed reduced group subscheme of $H$; since every closed
immersion is proper (EGA II, 5.4.2), we may assume that $u$ is surjective and that $H$ is reduced. Since $u$ is
surjective, the group $G(k)$ acts transitively on the set of closed points of $H$; whatever the closed point $y$ of $H$,
$u^{-1}(y)$ is therefore proper over $\kappa(y)$. By EGA IV₃, 9.6.1, the set of $y \in H$ such that $u^{-1}(y)$ is not
proper over $\kappa(y)$ is locally constructible; since it contains no closed point, it is empty (cf. EGA IV₃, 10.3.1
and 10.4.7).

[^N.D.E-VI_B-13] Consider now the generic point $\eta$ of $H^{0}$; by what precedes, the fiber $u^{-1}(\eta) = G
\times_{H} \operatorname{Spec} \kappa(\eta)$ is proper over $\kappa(\eta)$. On the other hand, since $H$ is reduced,
$\kappa(\eta)$ equals $O_{H,\eta}$. Since $O_{H,\eta}$ is the direct limit of the rings $O_{H}(V)$, as $V$ runs through
the non-empty open subsets of $H^{0}$, it follows from EGA IV₃, 8.1.2 a) and 8.10.5 (xii), that there exists a non-empty
open subset $V$ of $H^{0}$ such that the restriction of $u$ over $V$ is proper. It is then clear that the $g \cdot V$,
for $g \in G(k)$, form an open cover of $H$ such that, for every $g \in G(k)$, the restriction of $u$ over the open $g
\cdot V$ is proper; one deduces that $u$ is proper (cf. EGA II, 5.4.1). ∎

**Corollary 1.4.1.** *Let $A$ be an Artinian local ring, and $u : G \to H$ a morphism between $A$-groups locally of
finite type. The following assertions are equivalent:*

*(i) $u$ is locally quasi-finite,*

*(ii) $u$ is quasi-finite at some point,*

*(iii) `Ker u` is discrete,*

*(iv) the restriction of $u$ to each connected component of $G$ is finite.*

*If in addition $u$ is quasi-compact, these assertions are equivalent to the following:*

*(v) $u$ is finite.*

<!-- label: III.VI_B.1.4.1 -->

*Proof.* It is clear that (iv) implies (iii), that (iii) implies (ii) (EGA I, 6.4.4), and that, in the case where $u$ is
quasi-compact, assertions (iv) and (v) are equivalent. We have already seen in 1.3 that (i) and (ii) are equivalent.

Let us show finally that (i) implies (iv). Let $C$ be a connected component of $G$; since $C$ is of finite type over $A$
(VI_A, 2.4.1) and $G$ and $H$ are separated (VI_A, 0.2), by EGA I, 5.5.1 and 6.3.4, the restriction $u'$ of $u$ to $C$
is separated and of finite type.[^N.D.E-VI_B-14] Since the fibers of $u'$ are discrete, it follows that $u'$ is
quasi-finite (cf. EGA II, 6.2.2). Since every quasi-finite proper morphism is finite (cf. EGA III₁, 4.4.2), it therefore
suffices to show that $u'$ is universally closed.

For this, we may assume that $A$ is equal to its residue field $k$. Then, by (fpqc) descent (cf. EGA IV₂, 2.6.4), it
suffices to show that $u' \otimes_{k} \bar{k}$ is universally closed, where $\bar{k}$ denotes an algebraic closure of
$k$. Moreover, since $C$ is of finite type over $k$, $C \otimes_{k} \bar{k}$ is the sum of finitely many connected
components $C'_{1}, \cdots, C'_{n}$ of $G \otimes_{k} \bar{k}$, and it suffices to show the assertion for each $C'_{i}$.
One is thus reduced to the case where $k$ is algebraically closed.

<!-- original page 337 -->

Let then $g$ be a closed point of $C$. If $u^{0} : G^{0} \to H$ is the restriction of $u$ to $G^{0}$, one has $u' =
r_{u(g)} \circ u^{0} \circ r^{-1}_{g}$, where $r_{g}$ denotes right translation by $g$. Therefore, to show that $u'$ is
proper, it suffices to show that $u^{0}$ is. By hypothesis, $u$ is locally quasi-finite, so the fiber `Ker u` is
discrete (and non-empty); we have seen that $u^{0}$ is of finite type, so the fiber $Ker u^{0}$ is finite (cf. EGA II,
6.2.2), hence proper and non-empty. Therefore $u^{0}$ is proper by 1.4. ∎

**Corollary 1.4.2.** *Let $A$ be an Artinian local ring, and $u : G \to H$ a quasi-compact morphism between $A$-groups
locally of finite type. The following assertions are equivalent:*[^N.D.E-VI_B-15]

*(i) $u$ is a closed immersion,*

*(ii) $u$ is a monomorphism,*

*(iii) `Ker u` is trivial, i.e. isomorphic to the unit $k$-group.*

*In particular, every group subscheme[^N.D.E-VI_B-16] of $H$ is closed.*

<!-- label: III.VI_B.1.4.2 -->

*Proof.* It is clear that (i) implies (ii), and if one considers the functors represented respectively by $G$ and $H$,
it is immediate that conditions (ii) and (iii) are equivalent. Finally, if `Ker u` is the unit $k$-group, `Ker u` is a
proper non-empty fiber, so $u$ is a proper monomorphism by 1.4, of finite presentation since $H$ is locally noetherian
(EGA IV₁, 1.6.1), and hence a closed immersion (EGA IV₃, 8.11.5).

The last assertion follows from the fact that, since $H$ is locally noetherian, every immersion $G \to H$ is
quasi-compact (EGA I, 6.6.4). ∎

**Counterexample 1.4.3.** *Let $k$ be a field of characteristic 0, $G$ the constant $k$-group $\mathbb{Z}$, and $H$ the
$k$-group $G_{a,k}$. Let $u : G \to H$ be a morphism of $k$-groups. If $u \neq 0$, then $Ker u = 0$, but $u$ is not a
closed immersion (cf. 1.2.2).*

<!-- label: III.VI_B.1.4.3 -->

We shall use later the two following results, which should have appeared in Exposé VI_A:

**Lemma 1.5.** *Let $k$ be a field and $G$ a $k$-group locally of finite type. Then:*

*(i) All irreducible components of $G$ have the same dimension.*

*(ii) For every $g \in G$, one has $\dim_{g} G = \dim G$.*

<!-- label: III.VI_B.1.5 -->

<!-- original page 338 -->

[^N.D.E-VI_B-17] Assertion (i) has already been proved in (VI_A, 2.4.1), and assertion (ii) follows from it. Indeed, let
$g$ be a point of $G$ and $C$ the connected component of $G$ containing $g$. By definition (EGA 0_IV, 14.1.2), $\dim_{g}
G$ is the infimum of the integers $\dim U$, as $U$ runs through the open neighborhoods of $g$; one therefore has
$\dim_{g} G = \dim U_{0}$ for some `U_0`, which one may assume contained in $C$ (since $\dim V \leq \dim U$ if $V
\subset U$). Then, since $C$ is irreducible and of finite type over $k$ (VI_A, 2.4.1), one has
`dim U_0 = dim C = tr.deg_k κ(ξ)`, where $\xi$ is the generic point of $C$, by EGA IV₂, 5.2.1. Hence
`dim_g G = dim C = dim G`. ∎

**Proposition 1.6.** [^N.D.E-VI_B-18] *Let $S$ be a scheme of characteristic zero and $G$ an $S$-group scheme, locally
of finite presentation over $S$ at every point of the unit section $\epsilon(S)$. For $G$ to be smooth over $S$ at every
point of the unit section, it is necessary and sufficient that the `O_S`-module $\omega_{G/S} =
\epsilon*(\Omega^{1}_{G/S})$ (called the conormal module to the unit section of $G$) be locally free.*

<!-- label: III.VI_B.1.6 -->

Recall that a scheme $S$ is said to be *of characteristic zero* if for every closed point $x$ of $S$, the field
$\kappa(x)$ has characteristic zero.

Recall also (II 4.11) that, if $\pi$ denotes the structural morphism $G \to S$, one has $\Omega^{1}_{G/S} =
\pi*(\omega_{G/S})$, so that it comes to the same thing to say that the `O_S`-module $\omega_{G/S}$ is locally free, or
that the `O_G`-module $\Omega^{1}_{G/S}$ is locally free.

If there exists an open neighborhood $U$ of $\epsilon(S)$ which is smooth over $S$, then, by EGA IV₄, 17.2.3,
$\Omega^{1}_{U/S}$ is locally free of finite type, as well as $\omega_{G/S} = \epsilon*(\Omega^{1}_{U/S})$.

Conversely, if $\omega_{G/S}$ is locally free, the same holds for $\Omega^{1}_{G/S} = \pi*(\omega_{G/S})$. Since $S$ is
of characteristic `0`, the Jacobian criterion (EGA IV₄, 16.12.2) therefore implies that $G$ is differentially smooth
over $S$. Then it follows from EGA IV₄, 17.12.5, that $G$ is smooth over $S$ at every point of the unit section. ∎

**Corollary 1.6.1 (Cartier).** *Given a field $k$ of characteristic zero, every $k$-group locally of finite type over
$k$ is smooth over $k$.*

<!-- label: III.VI_B.1.6.1 -->

Indeed, it is then clear that the $k$-module $\omega_{G/k}$ is locally free, so, by 1.6, $G$ is smooth over $k$ at the
unit point $e$, and hence smooth over $k$ by 1.3.1. ∎

## 2. "Open properties" of groups and group morphisms locally of finite presentation

<!-- label: III.VI_B.2 -->

### 2.0.

In all that follows, $S$ will denote an arbitrary scheme; an $S$-group scheme will be called an $S$-*group*. Given an
$S$-group $G$, we shall denote by $\epsilon$ the unit section, by $c : G \to G$ the inversion morphism, and by `µ` the
multiplication morphism $G \times_{S} G \to G$. For every $S$-scheme $X$, we shall denote by $\pi$ or $\pi_{X}$ the
structural morphism $X \to S$.

<!-- original page 329 -->

Given a property $P(u)$ of a morphism of $S$-schemes $u : X \to Y$, we shall say that $P(u)$ is *stable under base
change* if, whenever $u$ satisfies $P(u)$, so does the morphism $u_{(Y')}$, for any $S$-morphism $Y' \to Y$. We say that
$P(u)$ is *local in nature for the topology $T$* (cf. Exp. IV, §§ 4 and 6) if $P(u)$ satisfies the following two
conditions:

a) $P(u)$ is stable under base change,

b) whenever there exists a covering family of $S$-morphisms $Y_{i} \to Y$ for the topology $T$ such that each morphism
$u_{(Y_{i})}$ satisfies $P(u)$, then $u$ satisfies $P(u)$.

**Proposition 2.1.** *Let $P(u)$ be a property of a morphism of $S$-schemes, local in nature for the (fpqc) topology.
Let $u : G \to H$ be a morphism of $S$-groups. Assume $G$ flat and universally open over $S$.*

*Let $W$ be the largest open subset of $H$ above which $u$ satisfies the property $P(u)$, and let $V = u^{-1}(W)$. Then
$U = \pi_{G}(V)$ is open in $S$ and $V$ is an open group subscheme of $G|_{U}$.*

<!-- label: III.VI_B.2.1 -->

The existence of a largest open subset $W$ of $H$ above which $u$ satisfies $P(u)$ follows from the fact that $P(u)$ is
local in nature for the Zariski topology. Since $\pi_{G}$ is universally open, $\pi_{G}(V)$ is an open subset $U$ of
$S$. It suffices to show that $V$ is a group subscheme of $G|_{U}$. We may therefore assume $U = S$.

<!-- original page 330 -->

Set then $G' = G \times_{S} V$, $H' = H \times_{S} V$, $V' = V \times_{S} V$, $W' = W \times_{S} V$, and $u' = u_{(V)}$;
let $W'_{1}$ be the largest open subset of $H'$ above which $u'$ satisfies $P(u)$; since $V$ is flat and universally
open over $S$, so is $H'$ over $H$, and Lemma 2.1.1 below shows that $W'_{1} = W'$. Now consider the automorphism of
$V$-schemes $a$ (resp. $b$) of $G'$ (resp. $H'$), namely right translation by the inverse of the diagonal section
$\delta$ (resp. by the inverse of $u(\delta)$), defined by

```text
a(g, v) = (g · v⁻¹, v),    (resp. b(h, v) = (h · u(v⁻¹), v)),
```

for any morphism $T \to S$, $g \in G(T)$, $v \in V(T)$, and $h \in H(T)$. It is clear that $u' \circ a = b \circ u'$,
which shows that $W'$ is stable under $b$, hence $V'$ is stable under $a$, so that $V$ is a group subscheme of $G$. ∎

**Lemma 2.1.1.** *Let $P(u)$ be a property of an $S$-morphism $u$, local in nature for the (fpqc) topology. Consider a
cartesian square of morphisms of $S$-schemes:*

```text
       f′
X′ ─────────→ Y′
│              │
│              │ g
▼              ▼
X  ─────────→ Y,
       f
```

*where $g$ is flat and open. Let $W$ (resp. $W'_{1}$) be the largest open subset of $Y$ (resp. $Y'$) above which $f$
(resp. $f' = f_{(Y')}$) satisfies $P(u)$. Then $W'_{1} = W \times_{Y} Y'$.*

<!-- label: III.VI_B.2.1.1 -->

Set $W' = W \times_{Y} Y'$; since $P(u)$ is stable under base change, one has $W' \subset W'_{1}$. Since $g$ is open,
$W_{1} = g(W'_{1})$ is an open subset of $Y$. Set $V_{1} = f^{-1}(W_{1})$ and $V'_{1} = V_{1} \times_{W_{1}} W'_{1}$; it
is clear that $V'_{1} = f'^{-1}(W'_{1})$. Since $g$ is flat and open, the morphism $W'_{1} \to W_{1} = g(W'_{1})$
deduced from $g$ is faithfully flat and open, hence covering for the (fpqc) topology (cf. IV 6.3.1 (iv)). Since the
morphism $V'_{1} \to W'_{1}$ deduced from $f'$ satisfies $P(u)$, the same holds for the morphism $V_{1} \to W_{1}$
deduced from $f$; hence $W_{1} \subset W$, and $W'_{1} \subset g^{-1}(W_{1}) \subset g^{-1}(W) = W'$; therefore $W' =
W'_{1}$. ∎

**Remark 2.1.2.** *A great many properties of a morphism are local in nature for the (fpqc) topology; let us mention the
properties of being flat, (universally) open, (locally) of finite type, of finite presentation, quasi-finite (cf. EGA
IV₂, 2.5.1, 2.6.1 and 2.7.1), smooth, étale, unramified (EGA IV₄, 17.7.3).*

*The proof of 2.1 in fact uses only base changes by flat morphisms; the proposition therefore applies to a property
satisfying condition b) of 2.0 relative to the (fpqc) topology, and stable under base change by flat morphisms (for
example, that of being quasi-compact and dominant).*

<!-- original page 331 -->

*Of course, one can state an analogous proposition concerning properties local in nature for a topology $T$ finer than
the Zariski topology, the condition to verify on $G$ being then that $\pi_{G}$ be universally open and covering for the
topology $T$.*

*In particular, if $G$ is flat and locally of finite presentation over $S$, one has an analogous statement for
properties stable under base change by flat morphisms locally of finite presentation, satisfying condition b) of 2.0
relative to the (fpqc) topology (e.g., the properties of being regular, reduced, Cohen–Macaulay, etc. (EGA IV₂, 6.8)).*

<!-- label: III.VI_B.2.1.2 -->

**Proposition 2.2.** *Let $G$ and $H$ be two $S$-groups and $u : G \to H$ a morphism of $S$-groups.
Then:*[^N.D.E-VI_B-19]

*(i) Suppose $G$ or $H$ flat over $S$, and $G$ or $H$ locally of finite presentation over $S$, and let $V$ be the
largest open subset of $G$ such that the restriction of $u$ to $V$ is flat and locally of finite presentation (resp.
smooth, resp. étale). Then $U = \pi_{V}(V)$ is open in $S$, and $V$ is an open group subscheme of $G|_{U}$.*

*(ii) Suppose $G$ or $H$ universally open over $S$, and let $V$ be the largest open subset of $G$ such that the
restriction of $u$ to $V$ is universally open. Then $U = \pi_{V}(V)$ is open in $S$, and $V$ is an open group subscheme
of $G|_{U}$.*

<!-- label: III.VI_B.2.2 -->

*Proof.* We first show (i). Let us show that the restriction $\pi_{V}$ of $\pi_{G}$ to $V$ is flat and locally of finite
presentation.

a) If $\pi_{G}$ is flat (resp. locally of finite presentation), so is $\pi_{V}$.

b) If $\pi_{H}$ is flat (resp. locally of finite presentation), so is $\pi_{V}$, as the composition of the restriction
of $u$ to $V$ and $\pi_{H}$.

So in the four cases envisaged in the statement, $\pi_{V}$ is flat and locally of finite presentation, hence universally
open (EGA IV₂, 2.4.6). Set $U = \pi_{V}(V)$; $U$ is therefore open in $S$. It then suffices to show that $V$ is an open
group subscheme of $G|_{U}$; we may therefore assume $U = S$.

Set then $G' = G \times_{S} V$, $H' = H \times_{S} V$, $V' = V \times_{S} V$ and $u' = u_{(V)}$. Then, since $V$ is flat
and locally of finite presentation over $S$, so is $H'$ over $H$. By EGA IV₄, 17.7.4, $V'$ is then the largest open
subset of $G'$ such that the restriction of $u'$ to $V'$ is flat and locally of finite presentation (resp. smooth, resp.
étale). With the automorphisms $a$ and $b$ defined as in the proof of 2.1, it is then clear that $V'$ is stable under
$a$, hence $V$ is a group subscheme of $G$.

Let us show (ii). The restriction $\pi_{V}$ of $\pi_{G}$ to $V$ is a universally open morphism, either because so is
$\pi_{G}$, or as the composition of the restriction of $u$ to $V$ and $\pi_{H}$ in the case where $\pi_{H}$ is
universally open. Set $U = \pi_{V}(V)$; $U$ is then open in $S$. It suffices to show that $V$ is an open group subscheme
of $G|_{U}$. We may therefore assume $U = S$.

Set as before $G' = G \times_{S} V$, $H' = H \times_{S} V$, $V' = V \times_{S} V$ and $u' = u_{(V)}$. Then $\pi_{V} : V
\to S$ is surjective and universally open, the same is true of $G' \to G$, so that $V'$ is the largest open subset of
$G'$ such that the restriction of $u'$ to $V'$ is universally open, by virtue of (EGA IV₃, 14.3.4 (i) and (ii)). With
the automorphisms $a$ and $b$ defined as before, it is then clear that $V'$ is stable under $a$, hence $V$ is a group
subscheme of $G$. ∎

<!-- original page 333 -->

**Corollary 2.3.** *Let $G$ be an $S$-group and $V$ the largest open subset of $G$ which is flat and locally of finite
presentation (resp. smooth, étale, universally open) over $S$. Then $U = \pi_{V}(V)$ is open in $S$, and $V$ is an open
group subscheme of $G|_{U}$.*

<!-- label: III.VI_B.2.3 -->

It suffices to apply 2.2 in the case where $H$ is the unit $S$-group and $u$ is the unique morphism of $S$-groups $G \to
H$, since then $\pi_{H}$ is an isomorphism and $\pi_{G} = \pi_{H} \circ u$. ∎

**Corollary 2.4.** *Let $G$ be an $S$-group; if there exists a neighborhood $X$ of the unit section having one (or
several) of the following properties:*

*$X$ is flat and locally of finite presentation (resp. smooth, étale, universally open) over $S$,*

*then there exists an open group subscheme of $G$ having the same properties.*

<!-- label: III.VI_B.2.4 -->

It suffices to apply 2.3, remarking that here, with the notations of 2.2, one has $\epsilon(S) \subset V$, hence $U =
S$. ∎

**Proposition 2.5.** [^N.D.E-VI_B-20] *Let $u : G \to H$ be a morphism of $S$-groups.*

*(i) Suppose that $G$ (resp. $H$) is of finite presentation and flat (resp. of finite type) over $S$ at the points of
its unit section. Then the sets:*

$$ U_{flat} \supset U_{smooth} \supset U_{\acute{e}}t, $$

*formed of the points $s \in S$ such that $u_{s}$ is flat (resp. smooth, étale), are open in $S$.*

*If moreover $G$ (resp. $H$) is locally of finite presentation and flat (resp. locally of finite type) over $S$, then
the set $V_{flat}$ (resp. $V_{smooth}$, $V_{\acute{e}}t$) of points of $G$ where $u$ is flat (resp. smooth, resp. étale)
is the inverse image under $\pi_{G}$ of $U_{flat}$ (resp. $U_{smooth}$, $U_{\acute{e}}t$).*

*(ii) Suppose that, for every $s \in S$, $G_{s}$ is locally of finite type over $\kappa(s)$ (a condition satisfied if
$G$ is of finite type over $S$ at the points of the unit section (1.3.1.1)), and that $u$ is locally of finite type
(resp. locally of finite presentation) at the points of the unit section of $G$. Then the sets:*

$$ U_{l}.q.f. \supset U_{n}.r. $$

*formed of the $s \in S$ such that $u_{s}$ is locally quasi-finite (resp. unramified) are open in $S$.*

*If moreover $u$ is locally of finite type (resp. locally of finite presentation), then the set $V_{l}.q.f.$ (resp.
$V_{n}.r.$) of points of $G$ where $u$ is quasi-finite (resp. unramified) is the inverse image under $\pi_{G}$ of
$U_{l}.q.f.$ (resp. $U_{n}.r.$).*

<!-- label: III.VI_B.2.5 -->

*Proof.* Let us show (i). First note (1.3.1.1) that, for every $s \in S$, $G_{s}$ is locally of finite type over
$\kappa(s)$. Let $Y$ be the open subset of $H$ formed by the points where $\pi_{H}$ is of finite type, and let `X_1` be
the open subset of $u^{-1}(Y)$ formed by the points where $\pi_{G}$ is of finite presentation. By EGA IV₃, 11.3.1, the
set $X$ of points of `X_1` where $\pi_{G}$ is of finite presentation and flat is open in `X_1`, hence in $G$.

Let $u_{X} : X \to Y$ be the morphism deduced from $u$. Since $Y$ (resp. $X$) contains the unit section of $H$ (resp.
$G$), the restriction $\pi_{X}$ of $\pi_{G}$ to $X$ is surjective, and the morphism $S \to X$ deduced from
$\epsilon_{G}$ is an $S$-section of $X$.

Consider the sets $W_{flat} \supset W_{smooth} \supset W_{\acute{e}}t$, formed by the points of $X$ where $u_{X}$ is
flat (resp. smooth, resp. étale). It is clear that $W_{smooth}$ and $W_{\acute{e}}t$ are open in $X$, cf. N.D.E. (6). On
the other hand, since $\pi_{Y}$ is locally of finite type and $\pi_{X} = \pi_{Y} \circ u_{X}$ is locally of finite
presentation, by EGA IV₁, 1.4.3 (v), $u_{X}$ is locally of finite presentation. Consequently, the flat locus `W_X` of
$u_{X}$ is open in $X$ (EGA IV₃, 11.3.1).

Let $x \in X$ and set $s = \pi_{X}(x)$; then by EGA IV₂, 11.3.10 (combined with EGA IV₄, 17.5.1, resp. 17.6.1), $x$
belongs to $W_{flat}$ (resp. $W_{smooth}$, $W_{\acute{e}}t$) if and only if $u_{s}$ is flat (resp. smooth, étale) at the
point $x$, or, what comes to the same by 1.3, if and only if $u_{s}$ is flat (resp. smooth, étale).

Consequently, for "♭ = flat, smooth or étale", one has $U_{\flat} = \epsilon^{-1}_{G}(W_{\flat})$ and $W_{\flat} =
\pi^{-1}_{X}(U_{\flat})$. Since $W_{\flat}$ is open in $X$, hence in $G$, the first equality shows that $U_{\flat}$ is
open in $S$.

<!-- original page 335 -->

The second assertion of (i) follows from what has just been seen, since then $Y = H$, $X = G$, and $V_{\flat} =
W_{\flat} = \pi^{-1}_{G}(U_{\flat})$.

Let us show assertion (ii). Let $V_{l}.t.f. \supset V_{l}.q.f.$ be the open subsets of $G$ formed by the points at which
$u$ is of finite type (resp. quasi-finite). Set $X = V_{l}.t.f.$ and denote by $u_{X}$ the restriction of $u$ to $X$. By
hypothesis, $X$ contains $\epsilon(S)$. Let $x \in X$ and set $s = \pi_{X}(x)$.

If $u$ is quasi-finite at $x$, then, by base change, $u_{s}$ is quasi-finite at $x$, and so, since $G_{s}$ is assumed
locally of finite type, $u_{s}$ is locally quasi-finite by 1.3.1.

Conversely, if $u_{s}$ is locally quasi-finite, then $u^{-1}_{X}(u_{X}(x)) \subset u^{-1}_{s}(u_{s}(x))$ is a finite
set. Since $u_{X} : X \to H$ is locally of finite type, it follows from Chevalley's semicontinuity theorem (EGA IV₃,
13.1.3) that there exists an open neighborhood $W$ of $x$ in $X$ such that the fiber $u^{-1}_{X}(u_{X}(x'))$ is discrete
for every $x' \in W$. Hence, by EGA II, 6.2.2 (and EGA III₂, Err_III 20), $u_{X}$ is quasi-finite at $x$.

Consequently, one has $U_{l}.q.f. = \epsilon^{-1}_{G}(V_{l}.q.f.)$ and $V_{l}.q.f. = \pi^{-1}_{X}(U_{l}.q.f.)$, and the
first equality shows that $U_{l}.q.f.$ is open in $S$.

If moreover $G$ is locally of finite type over $S$, then $X = G$, and so $V_{l}.q.f.$ is the inverse image under
$\pi_{G}$ of $U_{l}.q.f.$. This proves the first half of (ii).

Consider now the open subsets $V_{l}.p.f. \supset V_{n}.r.$, formed by the points where $u$ is of finite presentation
(resp. unramified), and suppose that $Z = V_{l}.p.f.$ contains the unit section of $G$. Let $z \in Z$; set $s =
\pi_{Z}(z)$ and $h = u_{Z}(z)$.

If $u$ is unramified at $z$, then, by base change, $u_{s}$ is unramified at $z$, and so, since $G_{s}$ is assumed
locally of finite type, $u_{s}$ is unramified by 1.3.1.

Conversely, if $u_{s}$ is unramified at the point $z$, then the fiber $u^{-1}_{s}(h) = u^{-1}(h)$ is unramified over
$\kappa(h)$ at the point $z$. Since $Z$ is an open subset of $G$, the fiber $u^{-1}_{Z}(h) = u^{-1}_{s}(h) \cap Z$ is
unramified over $\kappa(h)$ at the point $z$. Since $u_{Z}$ is locally of finite presentation, this entails, by EGA IV₄,
17.4.1, that $u_{Z}$ is unramified at the point $z$.

One therefore has $U_{n}.r. = \epsilon^{-1}_{G}(V_{n}.r.)$ and $V_{n}.r. = \pi^{-1}_{Z}(U_{n}.r.)$, and the first
equality shows that $U_{n}.r.$ is open in $S$.

If moreover $G$ is locally of finite presentation over $S$, then $Z = G$, and so $V_{n}.r.$ is the inverse image under
$\pi_{G}$ of $U_{n}.r.$. This completes the proof of assertion (ii). ∎

**Corollary 2.6.** *Let $u : G \to H$ be a morphism of $S$-groups which is a radicial morphism (which is the case if $u$
is a monomorphism (EGA I, 3.5.4)). Suppose $G$ (resp. $H$) locally of finite presentation and flat (resp. locally of
finite type) over $S$. Then the set $U$ of $s \in S$ such that $u_{s}$ is an open immersion is open in $S$, and the
restriction of $u$ over $U$ is an open immersion.*

<!-- label: III.VI_B.2.6 -->

By 2.5 (i), the set $U'$ of points $s \in S$ such that $u_{s}$ is étale is open in $S$. Since $u$ is radicial, so is
$u_{s}$, for every $s \in S$, hence by EGA IV₄, 17.9.1, one has $U = U'$, which shows that $U$ is open. Finally, by 2.5
(i), the restriction of $u$ over $U$ is étale; since $u$ is radicial, this restriction is an open immersion (EGA IV₄,
17.9.1). ∎

**Proposition 2.7.** *Let $G$ be an $S$-group. The following conditions are equivalent:*

*(i) $G$ is unramified over $S$ at the points of the unit section,*

*(ii) the unit section is an open immersion,*

*(iii) $G$ is of finite presentation over $S$ at the points of the unit section, and for every $s \in S$, $G_{s}$ is
unramified over $\kappa(s)$.*

*If, moreover, one assumes $G$ locally of finite presentation over $S$, then each of the three preceding conditions is
equivalent to the following:*

*(iv) $G$ is unramified over $S$.*

<!-- label: III.VI_B.2.7 -->

The equivalence of assertions (i) and (ii) follows from the more general Lemma 2.7.1 below. Note (1.3.1.1) that either
of conditions (i) or (iii) implies that, for every $s \in S$, $G_{s}$ is locally of finite type over $\kappa(s)$. Then
(EGA IV₄, 17.4.1), assertion (i) is equivalent to the fact that, for every $s \in S$, $G_{s}$ is unramified over
$\kappa(s)$ at the point $e_{s}$, unit of $G_{s}$, or again (1.3.1), to the fact that $G_{s}$ is unramified over
$\kappa(s)$, so assertions (i) and (iii) are equivalent. Finally, if $G$ is locally of finite presentation over $S$,
assertions (iii) and (iv) are equivalent (EGA IV₄, 17.4.1). ∎

**Lemma 2.7.1.** *Let $G$ be an $S$-scheme equipped with a section $\epsilon$. In order that $G$ be unramified over $S$
at the points of this section, it is necessary and sufficient that $\epsilon$ be an open immersion.*

<!-- label: III.VI_B.2.7.1 -->

The condition is necessary, by EGA IV₄, 17.4.1 a) ⇒ b″). Conversely, if $\epsilon$ is an open immersion, then the
restriction to $\epsilon(S)$ of the structural morphism $G \to S$ is an isomorphism, hence $G$ is unramified over $S$ at
the points of $\epsilon(S)$. ∎

**Corollary 2.8.** *Let $u : G \to H$ be a morphism of $S$-groups. Suppose that, for every $s \in S$, $G_{s}$ is locally
of finite type over $\kappa(s)$.*[^N.D.E-VI_B-21]

*a) If $u$ is locally of finite type, the following conditions are equivalent:*

*(i) $u$ is locally quasi-finite,*

*(ii) for every $s \in S$, $u_{s} : G_{s} \to H_{s}$ is locally quasi-finite,*

*(iii) `Ker u` is locally quasi-finite over $S$,*

*(iv) the fibers of `Ker u` are discrete.*

*b) If $u$ is locally of finite presentation, the following conditions are equivalent:*

*(v) $u$ is unramified,*

*(vi) for every $s \in S$, $u_{s} : G_{s} \to H_{s}$ is unramified,*

*(vii) `Ker u` is unramified,*

*(viii) the unit section $S \to Ker u$ is an open immersion.*

<!-- label: III.VI_B.2.8 -->

The equivalences (i) ⇔ (ii) and (v) ⇔ (vi) follow from 2.5 (ii), and Reminder 2.8.1 below shows that (i) ⇒ (iii) and (v)
⇒ (vii).

<!-- original page 345 -->

For every $s \in S$, denote by $e_{s}$ the unit element of $H_{s}$. Then (iii) (resp. (vii)) implies that, for every $s
\in S$,

```text
(Ker u)_s = Ker u_s = u_s⁻¹(e_s)
```

is locally quasi-finite (resp. unramified) over $\kappa(s) = \kappa(e_{s})$, hence $u_{s}$ is quasi-finite (resp.
unramified) at the unit point of $G_{s}$, hence, by 1.3, $u_{s}$ is locally quasi-finite (resp. unramified). So (iii) ⇒
(ii) and (vii) ⇒ (vi). Finally, (ii) ⇔ (iv) by 1.4.1, and (vii) ⇔ (viii) by 2.7. ∎

**Reminder 2.8.1.** *Recall (cf. I 2.3.6.1) that, given a morphism $u : G \to H$ of $S$-groups, the* kernel *of $u$,
denoted `Ker u`, is the group subfunctor of $G$ defined by setting, for any morphism $f : T \to S$,*

```text
(Ker u)(T) = {a ∈ G(T) | u ∘ a = ε_H ∘ f}.
```

*By loc. cit. (or EGA I, 4.4.1), this functor is representable by the $S$-group $G \times_{H} S =
u^{-1}(\epsilon_{H}(S))$, simply denoted `Ker u`. In particular, the structural morphism $Ker u \to S$ is deduced from
$u$ by base change.*

<!-- label: III.VI_B.2.8.1 -->

**Lemma 2.9.** *Let $\pi : X \to S$ be a morphism admitting an $S$-section $\epsilon$.*

*(i) If $\pi$ is injective, it is integral.*[^VI_B-2-9-i]

*(ii) If $\pi$ is locally of finite type, and if, for every $s \in S$, $\pi_{s}$ is an isomorphism, then $\pi$ is an
isomorphism.*[^VI_B-2-9-ii]

<!-- label: III.VI_B.2.9 -->

Let us first note that, by Lemma 2.9.1 below, $\pi$, being a homeomorphism, is an affine morphism.

If $\pi$ is injective, $\epsilon$ is surjective. Since $\epsilon$ is a surjective immersion, $\epsilon(S)$ is isomorphic
to the closed subscheme of $X$ defined by a nil-ideal $I$ of `O_X`. Since $\epsilon$ is an $S$-section of the morphism
$\pi$, one has a direct sum decomposition $O_{X} = O_{S} \oplus I$ of `O_S`-modules. Since $I$ is a nil-ideal of `O_X`,
$I$ is evidently integral over `O_S`, hence `O_X` is integral over `O_S`, and $\pi$ is integral.

Suppose now that $\pi$ is locally of finite type. Since $\pi \circ \epsilon = id_{S}$, $\epsilon$ is locally of finite
presentation (cf. EGA IV₁, 1.4.3 (v)), hence $I$ is an ideal of finite type of `O_X` (EGA IV₁, 1.4.1). For every $s \in
S$, one has $O_{X_{s}} = \kappa(s) \oplus I \otimes_{O_{S}} \kappa(s)$. By hypothesis, $\epsilon_{s}$ is an isomorphism,
hence $I \otimes_{O_{S}} \kappa(s) = 0$ for every $s \in S$, hence a fortiori $I \otimes_{O_{X}} \kappa(x) = 0$ for
every $x \in X$, which implies, by Nakayama's lemma, that $I = 0$, hence $\pi$ is an isomorphism. ∎

**Lemma 2.9.1.** *Let $f : X \to Y$ be a morphism of schemes which is a homeomorphism; then $f$ is an affine
morphism.*[^VI_B-2-9-1]

<!-- label: III.VI_B.2.9.1 -->

It suffices to show that every point $y \in Y$ has an open neighborhood $W$ such that the restriction of $f$ over $W$ is
an affine morphism. So let $y \in Y$, and let $V$ be an affine open neighborhood of $y$ in $Y$. Let $V' = f^{-1}(V)$.
Then $V'$ is an open neighborhood of $x = f^{-1}(y)$ in $X$. There exists an open affine neighborhood $W'$ of $x$ in $X$
contained in $V'$. Set then $W = f(W')$. Then $W$ is an open neighborhood of $y$ in $Y$ contained in the affine scheme
$V$, hence $W$ is separated. Since $W'$ is an affine scheme, the restriction of $f$ over $W$ is then an affine morphism
(EGA II, 1.2.3). ∎

**Corollary 2.10.** *Let $G$ be an $S$-group locally of finite type. Suppose that, for every $s \in S$, $G_{s}$ is the
unit $\kappa(s)$-group; then $G$ is the unit $S$-group.*

<!-- label: III.VI_B.2.10 -->

More generally:

**Corollary 2.11.** *Let $f : X \to Y$ be an $S$-morphism locally of finite type. In order that $f$ be a monomorphism,
it is necessary and sufficient that $f_{s}$ be a monomorphism for every $s \in S$.*

<!-- label: III.VI_B.2.11 -->

It is clear that the condition is necessary; let us show that it is sufficient. If, for every $s \in S$, $f_{s}$ is a
monomorphism, then a fortiori for every $y \in Y$, $f_{y}$ is a monomorphism; we may therefore assume $Y = S$.

By EGA I, 5.3.8, to show that $f$ is a monomorphism, it suffices to show that $\Delta_{f} : X \to X \times_{S} X$ is an
isomorphism, or, what comes to the same, that the first projection $p : X \times_{S} X \to X$ is an isomorphism. But, if
$f_{s}$ is a monomorphism, it likewise follows from EGA I, 5.3.8 that the first projection $X_{s} \times_{\kappa(s)}
X_{s} \to X_{s}$ (which is identified with $p_{s}$) is an isomorphism. Now $p$ has the $S$-section $\Delta_{f}$, hence
Lemma 2.9 affirms that if for every $s \in S$, $p_{s}$ is an isomorphism, then so is $p$. ∎

**Corollary 2.12.** *Let $G$ be an $S$-scheme having an $S$-section $\epsilon$ and such that the structural morphism
$\pi : G \to S$ is closed. Let $s \in S$ be such that $\pi$ is of finite presentation at the point $\epsilon(s)$ and
that $\epsilon_{s} : \operatorname{Spec}(\kappa(s)) \to G_{s}$ is an isomorphism (or, what comes to the same, that
$\pi_{s} : G_{s} \to \operatorname{Spec} \kappa(s)$ is an isomorphism). Then there exists an open neighborhood $U$ of
$s$ in $S$ such that $\epsilon|_{U} : U \to G \times_{S} U$ is an isomorphism.*

<!-- label: III.VI_B.2.12 -->

Let $V$ be the set of points of $G$ where $\pi$ is unramified; it is known that $V$ is open (cf. N.D.E. (6)) and
contains $\epsilon(s)$. Hence $W = \epsilon^{-1}(V)$ is an open subset of $S$ containing $s$, such that for every $t \in
W$, $\pi$ is unramified at $\epsilon(t)$. Since $\pi$ is closed, so is $\pi|_{W}$, hence we may assume $W = S$.

Then, by 2.7.1, $X = G - \epsilon(S)$ is a closed subset of $G$ not meeting $G_{s}$, hence, since $\pi$ is closed, $F =
\pi(X)$ is a closed subset of $S$ not containing $s$; set $U = S - F$; then $U$ is an open subset of $S$ such that
$\epsilon|_{U}$ is an isomorphism of $U$ onto $G|_{U}$. ∎

## 3. Neutral component of a group locally of finite presentation

<!-- label: III.VI_B.3 -->

### 3.0.

Given a part $A$ (resp. $B$) of an $S$-scheme $X$ (resp. $Y$), by abuse of notation, $A \times_{S} B$ will denote the
part of $X \times_{S} Y$ formed by the points whose first projection lies in $A$ and second in $B$.

<!-- original page 347 -->

Given a part $A$ of an $S$-group $G$, we shall say that $A$ is *stable under the group law of $G$* if $c(A) \subset A$
and `µ(A ×_S A) ⊂ A`.

**Definition 3.1.** *Let $G$ be an $S$-functor in groups satisfying the following condition:*

```text
(+)    for every s ∈ S, the functor G_s = G ⊗_S κ(s) is representable.
```

*One then denotes by $G^{0}_{s}$ the connected component of the unit element of the $\kappa(s)$-group
$G_{s}$.[^N.D.E-VI_B-22] One defines a sub-$S$-functor in groups of $G$, called the* neutral component *of $G$, denoted
$G^{0}$, by setting, for every morphism $T \to S$:*

```text
G⁰(T) = {u ∈ G(T) | ∀ s ∈ S, u_s(T_s) ⊂ G⁰_s}.
```

*One has thus defined the functor $G \mapsto G^{0}$ from $(Sch/S)$-gr. to $(Sch/S)$-gr.*

<!-- label: III.VI_B.3.1 -->

**Remark 3.2.** *(i) Let $G$ be an $S$-functor in groups satisfying condition (+); then $Lie(G^{0}/S) = Lie(G/S)$, by
virtue of Exposé II.[^N.D.E-VI_B-23] Indeed, for every $S$-scheme $T$, denote by `I_T` the $T$-scheme of dual numbers
over $T$ and by $\tau : T \to I_{T}$ the zero section (cf. II, 2.1). By definition, one has*

```text
Lie(G/S)(T) = {u ∈ G(I_T) | u ∘ τ = e},
```

*where $e : T \to G$ denotes the composition of $T \to S$ and the unit section $S \to G$, and likewise*

```text
Lie(G⁰/S)(T) = {u ∈ G⁰(I_T) | u ∘ τ = e}
              = {u ∈ G(I_T) | u ∘ τ = e and u_s((I_T)_s) ⊂ G⁰_s, ∀ s ∈ S}.
```

*Now, for every $s \in S$, $T_{s}$ and $(I_{T})_{s} = I_{T_{s}}$ have the same underlying set, hence if $u \in
Lie(G/S)(T)$, one has $u_{s}(I_{T_{s}}) = e_{s}$, where $e_{s}$ denotes the unit point of $G_{s}$, whence $u \in
Lie(G^{0}/S)(T)$. So the inclusion $Lie(G^{0}/S)(T) \subset Lie(G/S)(T)$ is an equality for every $T$, whence
$Lie(G^{0}/S) = Lie(G/S)$.*

*(ii) Let $G$ and $G'$ be two $S$-functors in groups satisfying (+); then:*

*a) if $G \subset G'$, then $G^{0} \subset G'^{0}$,*

*b) if $G \subset G'$ and $G'^{0} \subset G$, then $G^{0} = G'^{0}$,*

*c) if for every $s \in S$, $G_{s}$ is locally of finite type over $\kappa(s)$, then $G^{0}$ satisfies property (+), by
(VI_A, 2.3), and one has $(G^{0})^{0} = G^{0}$.*

<!-- label: III.VI_B.3.2 -->

**Proposition 3.3.** *Let $G$ be an $S$-functor in groups satisfying condition (+) and let $S'$ be an $S$-scheme. Then
$(G \times_{S} S')^{0} = G^{0} \times_{S} S'$; in other words, the functor $G \mapsto G^{0}$ commutes with base change,
i.e. the following diagram is commutative:*

```text
(Sch/S)-gr. ───── G ↦ G⁰ ────→ (Sch/S)-gr.
     │                              │
     ▼                              ▼
(Sch/S′)-gr. ─────────────────→ (Sch/S′)-gr.
```

<!-- label: III.VI_B.3.3 -->

<!-- original page 342 -->

It suffices indeed to check that, for every $s' \in S'$ with image $s$ in $S$, $((G \times_{S} S') \otimes_{S'}
\kappa(s'))^{0} = (G_{s} \otimes_{\kappa(s)} \kappa(s'))^{0}$ equals $G^{0}_{s} \otimes_{\kappa(s)} \kappa(s')$; this
follows from (VI_A, 2.1.2). Note, for later use in 4.2, that we have not used the group structure of $G_{s}$, only the
fact that $G^{0}_{s}$ has a rational point, namely $\epsilon(s)$, hence is geometrically connected (see also EGA IV₂,
4.5.14). ∎

**Special case 3.4.** *Let $G$ be an $S$-group scheme; denote by $G^{0}$ the subset of $G$ equal to the union of the
$G^{0}_{s}$ as $s$ runs through $S$. Then $G^{0}$ is a part of $G$ stable under the group law of $G$ (cf. 3.0), and for
any morphism $S' \to S$ one has:*

```text
G⁰(S′) = {u ∈ G(S′) | u(S′) ⊂ G⁰}.
```

*When $G^{0}$ is an open part of $G$, it is clear that $G^{0}$ is representable by the subscheme of $G$ induced on the
open $G^{0}$.*

<!-- label: III.VI_B.3.4 -->

**Proposition 3.5.** *Let $S$ be a quasi-compact and quasi-separated scheme, and $G$ an $S$-group with fibers locally of
finite type. Then there exists a quasi-compact open subset $U$ of $G$ containing $G^{0}$.*

<!-- label: III.VI_B.3.5 -->

The unit section $\epsilon$ being an immersion, $\epsilon(S)$ is a quasi-compact subspace of $G$, so there exists a
quasi-compact open subset $V$ of $G$ containing $\epsilon(S)$. Since $S$ is quasi-separated and $V$ quasi-compact, $V$
is quasi-compact over $S$ (EGA IV₁, 1.2.4), so $V \times_{S} V$ is quasi-compact over $S$, hence quasi-compact. Then
`V · V = µ(V ×_S V)` is quasi-compact. Set $V_{s} = V \cap G_{s}$ and $V^{0}_{s} = V \cap G^{0}_{s}$. Then $V^{0}_{s}$
is an open subset of $G^{0}_{s}$, dense in $G^{0}_{s}$ since $G^{0}_{s}$ is irreducible (VI_A, 2.4), so $V^{0}_{s} \cdot
V^{0}_{s} = G^{0}_{s}$ (VI_A, 0.5), which shows that $V_{s} \cdot V_{s} \supset G^{0}_{s}$, hence $V \cdot V \supset
G^{0}$. Finally, since $V \cdot V$ is quasi-compact, there exists a quasi-compact open subset $U$ of $G$ containing $V
\cdot V$ and a fortiori $G^{0}$. ∎

**Corollary 3.6.** *Let $G$ be an $S$-group with fibers locally of finite type and connected. Then $G$ is quasi-compact
over $S$.*

<!-- label: III.VI_B.3.6 -->

<!-- original page 343 -->

Our assertion being local on $S$ (EGA I, 6.6.1), one reduces to the case where $S$ is affine. By 3.5, there then exists
a quasi-compact open $U$ of $G$ containing $G^{0} = G$, hence $G$ is quasi-compact, hence quasi-compact over the affine
scheme $S$ (EGA I, 6.6.4 (v)). ∎

**Proposition 3.7.** [^N.D.E-VI_B-24] *Let $G$ be an $S$-group locally of finite presentation. Then:*

*(i) $G^{0}$ is ind-constructible in $G$.*

*(ii) If moreover $G$ is quasi-separated over $S$, and $S$ quasi-compact and quasi-separated, then $G^{0}$ is
constructible.*

*(iii) Consequently, if $G$ is quasi-separated over $S$, $G^{0}$ is locally constructible.*

<!-- label: III.VI_B.3.7 -->

*Proof.* Let us first show the first assertion. Since $\pi : G \to S$ is locally of finite presentation, given $s \in
S$, there exists an open subset $U$ of $G$ containing $\epsilon(s)$ and an open subset $V$ of $S$ containing $s$ such
that $\pi(U) \subset V$ and such that the morphism $\pi' : U \to V$ deduced from $\pi$ is of finite presentation. Then
$T = \epsilon^{-1}(U)$ is an open subset of $S$ and if we let $W = \pi'^{-1}(T)$ and $\pi'' = \pi'|_{W}$, then $\pi'' :
W \to T$ is of finite presentation, and admits as section the morphism $\epsilon'' : T \to W$ deduced from $\epsilon$.

For every $t \in T$, since $G^{0}_{t}$ is irreducible (VI_A, 2.4), $W \cap G^{0}_{t}$ is dense in $G^{0}_{t}$, hence
irreducible, hence connected: it is therefore the connected component of $\pi''^{-1}(t)$ containing $\epsilon''(t)$. It
then follows from EGA IV₃, 9.7.12 that the union $W^{0}$ of the $W \cap G^{0}_{t}$, for $t \in T$, is locally
constructible in $W$. On the other hand, it follows from (VI_A, 0.5) that $G^{0} \cap \pi^{-1}(T) = W^{0} \cdot W^{0}$,
i.e. $G^{0} \cap \pi^{-1}(T)$ is the image of $W^{0} \times_{T} W^{0}$ under the morphism `µ″ : W ×_T W → π⁻¹(T)`
deduced from `µ`.[^N.D.E-VI_B-25] Since $W \times_{T} W$ (resp. $\pi^{-1}(T)$) is of finite presentation (resp. locally
of finite presentation) over $T$, `µ″` is locally of finite presentation and quasi-separated, by EGA IV₁, 1.4.3 and
1.2.2; if moreover $\pi^{-1}(T)$ is quasi-separated over $T$, then `µ″` is quasi-compact (loc. cit. 1.2.4), hence of
finite presentation. Since $W^{0} \times_{T} W^{0}$ is locally constructible in $W \times_{T} W$ (since $W^{0}$ is in
$W$), it follows from Chevalley's constructibility theorem (loc. cit., 1.8.4 and 1.9.5 (viii)) that $G^{0} \cap
\pi^{-1}(T)$ is ind-constructible in $\pi^{-1}(T)$, and is locally constructible in $\pi^{-1}(T)$ if $G$ (and hence
$\pi^{-1}(T)$) is quasi-separated over $T$. This proves assertions (i) and (iii).

<!-- original page 344 -->

Suppose now $G$ quasi-separated over $S$, and $S$ quasi-compact and quasi-separated. Then, by 3.5, there exists a
quasi-compact open $U$ of $G$ containing $G^{0}$. Since $G$ is quasi-separated over $S$, $G$ is quasi-separated, so the
open $U$ is retrocompact (EGA IV₁, 1.2.7), and it suffices to show that $G^{0}$ is constructible in $U$ (EGA 0_III,
9.1.8). Moreover, $U$ being quasi-compact, hence quasi-compact over $S$ (EGA IV₁, 1.2.4), and quasi-separated over $S$,
the restriction of $\pi$ to $U$ is of finite presentation, so by EGA IV₃, 9.7.12, $G^{0}$ is locally constructible in
$U$, hence constructible in $U$, since $U$ is quasi-compact and quasi-separated (EGA IV₁, 1.8.1). This proves (ii), and
it follows that for every quasi-compact and quasi-separated open $T$ of $S$ (e.g., for every affine open of $S$), $G^{0}
\cap \pi^{-1}(T)$ is constructible. ∎

**Corollary 3.8.** *Let `S_0` be a quasi-compact and quasi-separated scheme, $I$ a filtered increasing preordered set,
$(A_{i})_{i \in I}$ a direct system of commutative quasi-coherent $O_{S_{0}}$-algebras, $A = \lim A_{i}$ (direct limit),
$S_{i} = \operatorname{Spec} A_{i}$ for $i \in I$, and $S = \operatorname{Spec} A$ (cf. EGA II, 1.3.1).*

*Let $G$ be an `S_0`-group scheme locally of finite presentation. Then the canonical map $\lim G^{0}(S_{i}) \to
G^{0}(S)$ is bijective.*

<!-- label: III.VI_B.3.8 -->

Since $G$ is locally of finite presentation over `S_0`, the canonical map $\lim G(S_{i}) \to G(S)$ is bijective, by EGA
IV₂, 8.14.2 c). It follows immediately that the canonical map $\lim G^{0}(S_{i}) \to G^{0}(S)$ is injective. Let us show
that it is surjective. Let $g \in G^{0}(S) \subset G(S)$. There exists $i \in I$ such that $g$ factors through $g_{i}
\in G(S_{i})$ via $S \to S_{i}$; by hypothesis, $g^{-1}(G^{0}) = S$. But, by 3.7, $G^{0}$ is ind-constructible in $G$,
so $g^{-1}_{i}(G^{0})$ is ind-constructible in $S_{i}$. It then follows from EGA IV₂, 8.3.4, that there exists an index
$j \geq i$ such that $g^{-1}_{j}(G^{0}) = S_{j}$, where $g_{j}$ is the map deduced from $g_{i}$ by the base change
$S_{j} \to S_{i}$. This shows that $g_{j} \in G^{0}(S_{j})$, hence that $g$ comes from an element of $\lim
G^{0}(S_{i})$. ∎

**Proposition 3.9.** *Let $G$ be an $S$-group locally of finite presentation. Suppose that $G^{0}$ is representable;
then the canonical morphism $i : G^{0} \to G$ is an open immersion; moreover, $G^{0}$ is quasi-compact over $S$.*

<!-- label: III.VI_B.3.9 -->

Since $G^{0}$ is a subfunctor of the functor $G$, the morphism $i$ is a monomorphism, hence radicial. By the definition
of the functor $G^{0}$, one verifies immediately from the definition (EGA IV₄, 17.1.1) that $i$ is a formally étale
morphism (noting that $G^{0}$ is the image of $i$ in $G$). Finally, it follows from the characterization (EGA IV₃,
8.14.2 c)) of $S$-schemes locally of finite presentation via the functor they represent, and from 3.8, that, since $G$
is locally of finite presentation over $S$, so is $G^{0}$. Hence $i$ is locally of finite presentation (cf. EGA IV₁,
1.4.3); it is therefore a radicial étale morphism; hence an open immersion (EGA IV₄, 17.9.1).

Finally, the last assertion follows from 3.6. ∎

**Theorem 3.10.** *Let $G$ be an $S$-group. The following conditions are equivalent:*

*(i) $G$ is smooth over $S$ at the points of the unit section.*

*(ii) $G$ is flat and locally of finite presentation over $S$ at the points of the unit section, and for every $s \in
S$, $G_{s}$ is smooth over $\kappa(s)$.*

*(iii) There exists an open group subscheme $G'$ of $G$, smooth over $S$.*

*(iv) $G^{0}$ is representable by an open subscheme of $G$, smooth over $S$.*

<!-- label: III.VI_B.3.10 -->

<!-- original page 351 -->

It is clear that (iv) ⇒ (iii) ⇒ (i) and, by 1.3.1 and 2.4, (i) implies (ii) and (iii). Moreover, (ii) ⇒ (i) by EGA IV₄,
17.5.1.

Let us show finally that (iii) implies (iv). Lemma 3.10.1 below shows that $G'$ contains $G^{0}$, and that $G'^{0} =
G^{0}$. It therefore suffices to show that $G^{0}$ is open in $G$, since we have already seen (3.4) that $G^{0}$ will
then be representable by the smooth group subscheme induced by $G'$ on the open $G'^{0} = G^{0}$. We may therefore
assume $G' = G$.

To show that $G^{0}$ is open, it suffices to show that every $s \in S$ has a neighborhood $T$ in $S$ such that $G^{0}
\cap \pi^{-1}(T)$ is open in $\pi^{-1}(T)$. Let $s \in S$. Since $G = G'$, $\pi$ is locally of finite presentation, so
one can construct, as in the proof of 3.7, an open subset $T$ of $S$ containing $s$, and an open subset $W$ of $G$
containing $\epsilon(s)$, such that the morphism $\pi'' : W \to T$ deduced from $\pi$ is of finite presentation and
admits as section the morphism $\epsilon'' : T \to W$ deduced from $\epsilon$. For every $t \in T$, $W \cap G^{0}_{t}$
is then the connected component of $\pi''^{-1}(t)$ containing $\epsilon''(t)$. Since $\pi$ is smooth, so is $\pi''$,
which is therefore smooth and of finite presentation. Then, by EGA IV₃, 15.6.5, the union $W^{0}$ of the $W \cap
G^{0}_{t}$ for $t \in T$ is open in $W$.

On the other hand, by (VI_A, 0.5), one has $W^{0} \cdot W^{0} = G^{0} \cap \pi^{-1}(T)$, and one must show that this is
open in $\pi^{-1}(T)$. We may therefore now assume $T = S$; it remains to show that $W^{0} \cdot W^{0}$ is open in $G$.
Since $\pi$ is universally open, so is `µ` (VI_A, 0.1). Hence, since $W^{0}$ is open in $G$, so is
`W⁰ · W⁰ = µ(W⁰ ×_S W⁰)`.

This result will be improved in 4.4. ∎

**Lemma 3.10.1.** *Let $G$ be an $S$-group with fibers locally of finite type. Then every open group subscheme $H$ of
$G$ contains $G^{0}$, and satisfies $G^{0} = H^{0}$.*

<!-- label: III.VI_B.3.10.1 -->

Let $s \in S$; set $G'_{s} = H_{s} \cap G^{0}_{s}$; then $G'_{s}$ is an open subset of $G^{0}_{s}$, which is dense in
$G^{0}_{s}$ since $G^{0}_{s}$ is irreducible (VI_A, 2.4), hence $G'_{s} \cdot G'_{s} = G^{0}_{s}$ (VI_A, 0.5), which
shows that $G^{0}_{s} = G'_{s} \cdot G'_{s} \subset H_{s} \cdot H_{s} = H_{s}$. One thus has $G^{0}_{s} = H^{0}_{s}$ for
every $s$, whence $G^{0} \subset H$ and $G^{0} = H^{0}$. ∎

**Proposition 3.11.** *Let $u : G \to H$ be a morphism between $S$-groups locally of finite presentation. If $u$ is
flat, the map $u^{0} : G^{0} \to H^{0}$ deduced from $u$ is surjective; the converse is true if $G$ is flat over $S$ and
$H$ has reduced fibers.*[^N.D.E-VI_B-26]

<!-- label: III.VI_B.3.11 -->

[^N.D.E-VI_B-27] Suppose $u$ flat; then for every $s \in S$, $u_{s}$ is flat and locally of finite presentation, hence
open (EGA IV₂, 2.4.6), so the morphism $u^{0}_{s} : G^{0}_{s} \to H^{0}_{s}$ is surjective by 1.3.2. Hence the map
$u^{0} : G^{0} \to H^{0}$ is surjective.

Conversely, suppose the map $u^{0} : G^{0} \to H^{0}$ is surjective, $G$ flat over $S$ and $H$ with reduced fibers.
Then, for every $s \in S$, the morphism $u^{0}_{s} : G^{0}_{s} \to H^{0}_{s}$ is surjective, hence flat at every point
above the generic point $\eta$ of $H^{0}_{s}$ (since $O_{H^{0}_{s}, \eta}$ is a field), hence $u_{s}$ is flat by 1.3.
Hence $u$ is flat, by the fiber-wise flatness criterion (EGA IV₃, 11.3.11). ∎

## 4. Dimension of fibers of groups locally of finite presentation

<!-- label: III.VI_B.4 -->

**Proposition 4.1.** *Let $G$ be an $S$-scheme locally of finite type, equipped with an $S$-section $\epsilon$, and such
that for every $s \in S$, one has $\dim G_{s} = \dim_{\epsilon(s)} G_{s}$ (which is the case if $G$ is an $S$-group
(1.5)).*

*(i) The function $s \mapsto \dim G_{s}$ is upper semicontinuous on $S$.*

*(ii) If, moreover, $G$ is locally of finite presentation over $S$, this function is locally constructible.*

<!-- label: III.VI_B.4.1 -->

Let $\pi : G \to S$ be the structural morphism. Chevalley's semicontinuity theorem (EGA IV₃, 13.1.3) asserts that the
function $x \mapsto \dim_{x} \pi^{-1}(\pi(x))$ is upper semicontinuous on $G$. Now, for every $s \in S$, one has

```text
dim G_s = dim π⁻¹(s) = dim_{ε(s)} π⁻¹(π(ε(s)));
```

and since the function $s \mapsto \epsilon(s)$ is continuous on $S$, the composite function $s \mapsto \dim G_{s}$ is
upper semicontinuous on $S$.

<!-- original page 348 -->

Suppose $G$ locally of finite presentation over $S$. To show that the function $s \mapsto \dim G_{s}$ is locally
constructible, one sees, reasoning as above, that it suffices to show that the function $x \mapsto \dim_{x}
\pi^{-1}(\pi(x))$ is locally constructible on $G$, which follows from EGA IV₃, 9.9.1. ∎

**Proposition 4.2.** *Let $\pi : G \to S$ be an $S$-scheme locally of finite presentation, equipped with an $S$-section
$\epsilon$ and satisfying the following two conditions (which are satisfied if $G$ is an $S$-group, by 1.5 and (VI_A,
2.4.1)):*

*a) For every $s \in S$ and every $x \in G_{s}$, one has $\dim G_{s} = \dim_{x} G_{s}$ (or, what comes to the same
(1.5), for every $s \in S$, all irreducible components of $G_{s}$ have the same dimension).*

*b) For every $s \in S$, if one denotes by $G^{0}_{s}$ the connected component of $G_{s}$ containing $\epsilon(s)$,
$G^{0}_{s}$ is geometrically irreducible.*

*Let $s \in S$. The following conditions are equivalent:*

*(i) $G$ is universally open over $S$ at the points of $G^{0}_{s}$.*

*(i bis) $G$ is universally open over $S$ at every point of a neighborhood of $\epsilon(s)$ in
$G^{0}_{s}$.*[^N.D.E-VI_B-28]

*(ii) The function $t \mapsto \dim G_{t}$ is constant in a neighborhood of $s$ in $S$.*

*(iii) $G^{0}$ is "universally open over $S$ at the points of $G^{0}_{s}$", i.e., given $S' \to S$, $s' \in S'_{s}$, $g
\in G^{0}_{s'}$ and $V$ an open neighborhood of $g$ in $G' = G_{S'}$, then $\pi(V \cap G'^{0})$ is an open neighborhood
of $s'$ in $S'$.*[^N.D.E-VI_B-29]

<!-- label: III.VI_B.4.2 -->

*Proof.* Clearly (i) ⇒ (i bis). By EGA IV₃, 14.3.3.1 (ii), the set of points of $G^{0}_{s}$ where $\pi_{G}$ is
universally open is closed in $G^{0}_{s}$. Hence, since $G^{0}_{s}$ is irreducible, one has (i bis) ⇒ (i).

Let us show that (i) implies (ii). Let $T$ be the set of $t \in S$ such that $\dim G_{t} = \dim G_{s}$. By 4.1, $T$ is
locally constructible, hence, by EGA IV₁, 1.10.1, to show that $T$ is a neighborhood of $s$, it suffices to show that
every generization $s'$ of $s$ belongs to $T$.

<!-- original page 349 -->

Let $x$ be the generic point of $G^{0}_{s}$ and $U$ an open subset of $G$ containing $x$. Since $\pi_{G}$ is universally
open at $\xi$, by EGA IV₃, 14.3.13, for every generization $s'$ of $s$, one has $\dim(U \cap G_{s'}) \geq \dim_{x}(U
\cap G_{s})$. Taking hypothesis a) into account, this entails $\dim G_{s'} \geq \dim G_{s}$. Since the function $s
\mapsto \dim G_{s}$ is upper semicontinuous by 4.1, one also has $\dim G_{s'} \leq \dim G_{s}$, whence $s' \in T$. This
proves that (i) ⇒ (ii).

It is clear that (iii) ⇒ (i); let us show that (ii) ⇒ (iii). Since the dimension of fibers is unchanged by extension of
the base field, and the formation of $G^{0}$ commutes with base change (cf. the proof of 3.3), one may assume $S' = S$
and $s' = s$. Moreover, since every open $V$ of $G$ meeting $G^{0}_{s}$ contains the generic point $\eta$ of
$G^{0}_{s}$, one may assume $g = \eta$.

One may further assume $S$ affine. Let $U$ be an affine open neighborhood of $\epsilon(s)$; it is then of finite
presentation over $S$. Replacing $S$ by $\epsilon^{-1}(U)$ and then $U$ by $U \cap \pi^{-1}(S)$, we reduce to the case
where $\pi : U \to S$ is of finite presentation and admits $\epsilon : S \to U$ as section. Then, by EGA IV₃, 9.7.12,
$G^{0} \cap U$ is constructible in $U$. Then, replacing $V$ by an affine open contained in $V \cap U$, we obtain that
$G^{0} \cap V$ is constructible in $V$. Since $\pi : V \to S$ is of finite presentation, $\pi(G^{0} \cap V)$ is locally
constructible in $S$, by Chevalley's constructibility theorem (cf. EGA IV₁, 1.8.4).

Hence, by loc. cit., 1.10.1, to show that $\pi(G^{0} \cap V)$ is an open neighborhood of $s$, it suffices to show that
for every generization $t$ of $s$, there exists a generization $\xi$ of $\eta$ belonging to $G^{0}$ (and hence to $G^{0}
\cap V$). Now the generic point $\xi$ of $G^{0}_{t}$ is a generization of $\eta$. Indeed, $\epsilon(s)$ belongs to the
closure $X$ of ${\xi}$ in $G$, so by Chevalley's semicontinuity theorem (cf. EGA IV₃, 13.1.3), one has
$\dim_{\epsilon(s)} X_{s} \geq \dim_{\xi} X_{t}$; on the other hand, hypothesis (ii) entails that $\dim_{\xi} G^{0}_{t}
= \dim_{\epsilon(s)} G_{s}$. It follows that one of the irreducible components of $X_{s}$ containing $\epsilon(s)$
equals $G^{0}_{s}$, whence $\eta \in {\xi}^{-}$. This proves that (ii) ⇒ (iii), which proves the proposition. ∎

[^N.D.E-VI_B-30] One can also prove the implication (ii) ⇒ (i) as follows. Since $\pi$ is locally of finite
presentation, there exists an open subset $U$ of $G$ containing $\epsilon(s)$ and an open subset $V$ of $S$ containing
$s$ such that $\pi(U) \subset V$ and such that the morphism $\pi' : U \to V$ deduced from $\pi$ is of finite
presentation. Set then $T = \epsilon^{-1}(U)$ and $W = \pi'^{-1}(T) = U \cap \pi^{-1}(T)$. Then the morphism $\pi'' : W
\to T$ deduced from $\pi'$ is of finite presentation and admits as section the morphism $\epsilon'' : T \to W$ deduced
from $\epsilon$. Moreover, for every $t \in T$, $G^{0}_{t}$ being irreducible, $W \cap G^{0}_{t}$ is dense in
$G^{0}_{t}$, hence irreducible, hence connected: so it is the connected component of $\pi''^{-1}(t)$ containing
$\epsilon''(t)$.

<!-- original page 354 -->

Since $W \cap G^{0}_{t}$ is a dense open subset of $G^{0}_{t}$, one has, by 1.5 and EGA IV₂, 5.2.1,
`dim(W ∩ G⁰_t) = dim G⁰_t = dim G_t`, so the function $t \mapsto \dim W \cap G^{0}_{t}$ is constant in a neighborhood of
$s$ in $T$. Let us show finally that, for every $t \in T$, $W \cap G^{0}_{t}$ is geometrically irreducible. Let $K$ be
an extension of $\kappa(t)$; then $(W \cap G^{0}_{t}) \otimes_{\kappa(t)} K = (W \otimes_{\kappa(t)} K) \cap (G^{0}_{t}
\otimes_{\kappa(t)} K)$ is a non-empty open subset of $G^{0}_{t} \otimes_{\kappa(t)} K$, hence is irreducible since
$G^{0}_{t} \otimes_{\kappa(t)} K$ is.

We are then in the conditions of application of EGA IV₃, 15.6.6 (ii), which asserts that $\pi''$ (hence $\pi$) is
universally open at the points of $W \cap G^{0}_{s}$. But, by EGA IV₃, 14.3.3.1 (ii), the subset of $G_{s}$ formed by
the points where $\pi$ is universally open is closed in $G_{s}$; since it contains $W \cap G^{0}_{s}$, it therefore
contains its closure $G^{0}_{s}$. ∎

<!-- original page 350 -->

**Corollary 4.3.** *Let $G$ be a flat $S$-group locally of finite presentation. Then the function $s \mapsto \dim G_{s}$
is locally constant on $S$.*

<!-- label: III.VI_B.4.3 -->

This follows immediately from 4.2, since every flat morphism locally of finite presentation is universally open (EGA
IV₂, 2.4.6). ∎

**Corollary 4.4.** *Let $G$ be an $S$-group locally of finite presentation over $S$ at the points of the unit section.
Consider the conditions:*

*(i) $G$ is smooth over $S$ at the points of the unit section (cf. 3.10).*

*(ii) For every $s \in S$, $G_{s}$ is smooth over $\kappa(s)$, and the function $s \mapsto \dim G_{s}$ is locally
constant on $S$.*

*(iii) For every $s \in S$, $G_{s}$ is smooth over $\kappa(s)$, and there exists a neighborhood $V$ of the unit section
such that $\pi_{V} : V \to S$ is universally open.*

*(iv) For every $s \in S$, $G^{0}_{s}$ is smooth over $\kappa(s)$, and $G^{0}$ is representable by an open group
subscheme of $G$, universally open over $S$.*

*Then one has the following implications: (i) ⇒ (ii) ⇔ (iii) ⇔ (iv).*

*If one further assumes $S$ reduced, then conditions (i) to (iv) are equivalent, and imply that $G^{0}$ is smooth over
$S$.*[^N.D.E-VI_B-31]

<!-- label: III.VI_B.4.4 -->

*Proof.* Let us show that (i) implies (ii). For every $x \in G$, one has $\dim_{x} \pi^{-1}(\pi(x)) = \dim
\pi^{-1}(\pi(x))$, by 1.5. Consequently, by EGA IV₄, 17.10.2, the function

```text
x ↦ dim_x π⁻¹(π(x)) = dim π⁻¹(π(x))
```

is continuous in a neighborhood of the unit section; so the function $s \mapsto \dim G_{s}$ is continuous on $S$, hence
locally constant on $S$. Moreover, for every $s \in S$, $G_{s}$ is smooth over $\kappa(s)$ by 1.3.1.

<!-- original page 355 -->

Let us show that (ii) implies (iv). It suffices to show that $G^{0}$ is open in $G$, for then, by 3.4, $G^{0}$ will be
representable by the group subscheme induced on $G^{0}$, and the properties of $G^{0}$ cited in the statement will
follow from 2.4 and 4.2. Given $s \in S$, construct as in the proof of 3.10, $W$, $T$, $\pi''$, $\epsilon''$, and
$W^{0}$. Then, by EGA IV₃, 15.6.7, $W^{0}$ is open in $W$. On the other hand, under hypothesis 4.4 (ii), it follows from
4.2 that $\pi$ is universally open at every point of $W^{0}$, hence (VI_A, 0.1) `µ` is universally open at every point
of $W^{0} \times_{S} W^{0}$, which shows that $W^{0} \cdot W^{0}$ is open, and one concludes as in the proof of Theorem
3.10.

It is clear that (iv) ⇒ (iii), and (iii) ⇒ (ii) follows from 4.2 applied to $V$.

Finally, suppose (ii)–(iv) hold and let us show that $G^{0}$ is smooth over $S$ if $S$ is reduced.[^N.D.E-VI_B-32] For
this, one may assume $G = G^{0}$. Then $G$ is of finite presentation over $S$ by virtue of 5.5 below. Thus, $\pi_{G}$ is
of finite presentation, with geometrically integral fibers, of locally constant dimension on $S$. Then, by EGA IV₃,
15.6.7, the morphism $G \times_{S} S_{red} \to S_{red}$ deduced from $\pi_{G}$ is flat, hence $\pi_{G}$ is flat if $S$
is reduced. In this case, $G = G^{0}$ is smooth over $S$, by Theorem 3.10. ∎

## 5. Separation of groups and homogeneous spaces

<!-- label: III.VI_B.5 -->

**Proposition 5.1.** *In order that an $S$-group $G$ be separated, it is necessary and sufficient that the unit section
of $G$ be a closed immersion.*

<!-- label: III.VI_B.5.1 -->

The condition is necessary (EGA I, 5.4.6); it is sufficient by virtue of the following cartesian diagram (cf. (VI_A,
0.3)):

```text
              µ ∘ (id_G × c)
G ×_S G ─────────────────────→ G
   │                            ▲
   │ Δ_{G/S}                    │ ε
   ▼                            │
   G ──────────────────────→ S.
              π
```

**Proposition 5.2.** *If $S$ is discrete, every $S$-group is separated.*

<!-- label: III.VI_B.5.2 -->

Indeed, $S$ is then equal to $\coprod_{s \in S} \operatorname{Spec} O_{S,s}$, and by EGA I, 5.5.5, it suffices to show
that for every $s \in S$, $G \times_{S} \operatorname{Spec} O_{S,s}$ is separated, which follows from (VI_A, 0.3), since
$O_{S,s}$ is a local ring of dimension 0.[^N.D.E-VI_B-33]

<!-- original page 352 -->

**Theorem 5.3.** *Let $S$ be a scheme, $G$ an $S$-group scheme locally of finite presentation over $S$ and universally
open over $S$ in a neighborhood of the unit section, $X$ an $S$-scheme on which $G$ acts in such a way that the
morphism:*

```text
Φ : G ×_S X ─→ X ×_S X,    (g, x) ↦ (gx, x)
```

*is surjective. Suppose moreover that, for every $s \in S$:*

*(i) there exists an open subscheme $U$ of $X$, separated over $S$, such that $U_{s}$ is dense in $X_{s}$,*

*(ii) the fiber $X_{s}$ is locally of finite type over $\kappa(s)$.*[^N.D.E-VI_B-34]

*Then $X$ is separated over $S$.*

<!-- label: III.VI_B.5.3 -->

**Corollary 5.4.** *Let $S$, $G$, $X$ be as in the preliminary hypotheses of 5.3. Suppose moreover that $X$ has fibers
locally of finite type and connected. Then:*

*(i) $X$ is separated over $S$.*

*(ii) If there exists an open subset $V$ of $X$, quasi-compact over $S$ and meeting every non-empty fiber
$X_{s}$,[^N.D.E-VI_B-35] then $X$ is quasi-compact over $S$.*

<!-- label: III.VI_B.5.4 -->

*Proof.* (i) Indeed, let $s \in S$ be such that $X_{s} \neq \emptyset$. Since the morphism $\Phi_{s} : G_{s}
\times_{\kappa(s)} X_{s} \to X_{s} \times_{\kappa(s)} X_{s}$ deduced from $\Phi$ by base change is surjective, and
$X_{s}$ is connected, $X_{s}$ is irreducible by (VI_A, 2.5.4). Hence, if $U$ is an affine open of $X$ such that $U_{s}$
is non-empty, $U_{s}$ is dense in $X_{s}$, and the theorem applies.

To prove (ii), one may assume $S$ affine. Then $V$ is quasi-compact and, by 3.5, there exists a quasi-compact open $U$
of $G$ containing $G^{0}$. Let $s \in S$ be such that $X_{s} \neq \emptyset$. Then $X_{s}$ is irreducible (VI_A, 2.6.6)
and so, since $U_{s}$ contains $G^{0}_{s}$, the morphism $U_{s} \times_{\kappa(s)} V_{s} \to X_{s}$, $(g, x) \mapsto
gx$, is surjective (VI_A, 2.6.4). Consequently, the morphism $U \times_{S} V \to X$ is surjective, and so $X$ is
quasi-compact (since $U$ and $V$ are); as we assumed $S$ affine, hence separated, it follows that $X$ is quasi-compact
over $S$ (cf. EGA I, 6.6.4 (v)). ∎

**Remark 5.4.1.** [^N.D.E-VI_B-36] *We shall see in the course of the proof that the conclusion of Theorem 5.3 holds if
one makes only the hypothesis: (i′) there exists an open subscheme $U$ of $X$, separated over $S$, such that $U_{s}$ is
dense in every irreducible component of $X_{s}$. (The latter is a consequence of (i) if $X_{s}$ has locally a finite
number of irreducible components, which is the case under hypothesis (ii).) On the other hand, we shall see later that
5.4 is also valid under the hypothesis that each fiber $X_{s}$ is quasi-separated and connected.*

<!-- label: III.VI_B.5.4.1 -->

**Theorem 5.3A (Raynaud).** *Let $G$ be an $S$-group locally of finite presentation, universally open over $S$, and with
connected fibers. Then $G$ is separated over $S$. More generally, any $S$-scheme $X$ locally of finite presentation over
$S$, equipped with an action of $G$ such that the morphism $\Phi : G \times_{S} X \to X \times_{S} X$, $(g, x) \mapsto
(gx, x)$ is surjective, is separated over $S$.*

<!-- label: III.VI_B.5.3.A -->

<!-- original page 357 -->

**Corollary 5.5.** *Let $S$ be a scheme, $G$ an $S$-group scheme, locally of finite presentation, with connected fibers,
and universally open over $S$. Then $G$ is separated and of finite presentation over $S$.*[^N.D.E-VI_B-37]

<!-- label: III.VI_B.5.5 -->

Indeed, by 3.6 and 5.4, $G$ is quasi-compact and separated over $S$, and since $G$ is locally of finite presentation
over $S$, it is therefore of finite presentation over $S$. ∎

### 5.6. Proof of Theorem 5.3.

Before establishing 5.3, let us prove a few lemmas.

**Lemma 5.6.0.** [^N.D.E-VI_B-38] *(i) Let $A \subset B$ be integral rings, with $B$ integral over $A$, and let $q \in
\operatorname{Spec}(B)$ be such that $A$ is unibranch at the point $p = q \cap A$. Then the morphism $\pi :
\operatorname{Spec}(B) \to \operatorname{Spec}(A)$ is open at the point $q$.*

*(ii) Let $X$, $Y$ be two irreducible preschemes, $f : X \to Y$ a dominant morphism, $x$ a point of $X$ such that $f$ is
quasi-finite at $x$ and $y = f(x)$ is a unibranch point of $Y$. Then $f$ is open at the point $x$. In particular, if $Y
= \operatorname{Spec}(O_{Y,y})$ is a local prescheme with closed point $y$, then $f(U) = Y$ for every neighborhood $U$
of $x$.*

<!-- label: III.VI_B.5.6.0 -->

*Proof.* (i) Let $K$ (resp. $L$) be the fraction field of $A$ (resp. $B$), $A'$ the normalization of $A$, and $B'$ the
subring of $L$ generated by $A'$ and $B$. Then $B'$ is integral over $A'$. Set $Y = \operatorname{Spec}(A)$, $X =
\operatorname{Spec}(B)$, $Y' = \operatorname{Spec}(A')$, $X' = \operatorname{Spec}(B')$, so that one has a commutative
diagram

```text
X′ ───── π′ ────→ Y′
│                  │
│                  │ φ
▼                  ▼
X ────── π ────→ Y
```

in which all morphisms are integral and surjective.

Since $A$ is unibranch at $p$, $Y'$ has a unique point $p'$ above $p$; consequently, if $U$ is an open neighborhood of
$p'$ in $Y'$, then $\phi(Y' - U)$ is a closed subset not containing $p$, so that the complementary open is contained in
$\phi(U)$. This shows that $\phi : Y' \to Y$ is open at $p'$, and so it suffices to show that $\pi'$ is open. We are
thus reduced to the case where $A = A'$ is normal.

Let $N$ be a quasi-Galois extension of $K$ containing $L$, let $\tilde{X} = \operatorname{Spec}(\tilde{B})$, where
$\tilde{B}$ is the integral closure of $B$ in $N$, and let $\Gamma = \operatorname{Aut}(N/K)$. Since $\tilde{X} \to X$
is surjective, it suffices to show that $\tilde{\pi} : \tilde{X} \to Y$ is open. Let $U$ be an open of $\tilde{X}$ and
$U' = \bigcup_{g \in \Gamma} gU$. Since $\Gamma$ acts transitively on the fibers of $\tilde{X} \to Y$ (cf. [BAC], Chap.
V, § 2.3, Prop. 6), $\tilde{\pi}(U)$ equals $\tilde{\pi}(U')$, and the latter equals the complementary open of the
closed $\tilde{\pi}(\tilde{X} - U')$. This proves (i).

<!-- original page 358 -->

(ii) One may assume $Y$ and $X$ reduced. By Zariski's "Main Theorem" (cf. EGA IV₃, 8.12.9), there exist affine open
neighborhoods $U$ of $x$, and $V = \operatorname{Spec}(A)$ of $y$, such that $f(U) \subset V$, and a factorization:

```text
       j
U ─────────→ V′
│            │
│ f          │ u
▼            ▼
            V,
```

where $j$ is an open immersion and $u$ is finite. Replacing $V'$ by the closure of $j(U)$, one may assume $V'$
irreducible, hence $V' = \operatorname{Spec}(B)$, where $B$ is an integral $A$-algebra, finite over $A$. Moreover, since
$f$ is dominant, so is $u$, so that the morphism $A \to B$ is injective. Since, by hypothesis, $A$ is unibranch at the
point $y$, it follows from (i) that $u$ is open at the point $j(x)$, and hence $f = u \circ j$ is open at the point $x$.
This proves the first assertion of (ii). The second follows, since if $Y$ is a local prescheme with closed point $y$,
every open containing $y$ equals $Y$. (In the case where $Y = \operatorname{Spec}(O_{Y,y})$, one may also use, instead
of EGA IV₃, 8.12.9, the local form of Zariski's Main Theorem, which one finds, e.g., in [Pes66], or [Ray70b], Ch. IV,
Th. 1.) ∎

**Lemma 5.6.1.0.** [^N.D.E-VI_B-39] *Let $f : X \to S$ be a morphism locally of finite presentation, $s \in S$, and $x
\in X_{s}$. Let $n = \dim_{x}(X_{s})$ and let $q$ be the structural morphism $A^{n}_{S} \to S$.*

*Suppose given a morphism $u : X \to A^{n}_{S}$ quasi-finite such that $f = q \circ u$, and suppose $f$ universally open
at the generic point $z$ of an irreducible component $z$ of $X_{s}$, containing $x$ and of dimension $n$. Then $u$ is
universally open at the point $x \in X$.*

<!-- label: III.VI_B.5.6.1.0 -->

Let us note first that: (†) the hypotheses are preserved by any base change $\pi : S' \to S$ covering $s$ (i.e., such
that $\pi^{-1}(s) \neq \emptyset$). Indeed, let $S' \to S$ be such a morphism, let

```text
       u′
X′ ─────────→ A^n_{S′}
│              │
│ f′           │ q′
▼              ▼
             S′
```

be the diagram obtained by base change, and let $s'$ be a point of $S'$ above $s$ and $x'$ a point of $X'_{s'}$ above
$x$. Since $X'_{s'} = X_{s} \otimes_{\kappa(s)} \kappa(s')$, by lifting of generizations and invariance of dimension
under field extension (EGA IV₂, 2.3.4 (i) and 4.1.4), $x'$ is contained in an irreducible component $z'$ of $X'_{s'}$
whose generic point $z'$ lies above $z$, and one has $n \leq \dim z' \leq \dim_{x'} X'_{s'} \leq n$, whence $\dim z' = n
= \dim_{x'} X'_{s'}$. Since $f$ is universally open at $x$, $f'$ is universally open at $x'$.

Set $Y = A^{n}_{S}$. By EGA IV₃, 14.3.3.1 (i), to prove that $u$ is universally open at $x$, it suffices to prove that,
for every integer $r \geq 0$ and every point $x'$ of

<!-- original page 359 -->

$X' = X[T_{1}, \cdots, T_{r}]$ above $x$, the morphism $u' : X' \to Y' = A^{n}_{S}[T_{1}, \cdots, T_{r}]$ is open at the
point $x'$. Now, with $S' = S[T_{1}, \cdots, T_{r}]$ and $q'$ the projection $Y' \cong A^{n}_{S'} \to S'$, one is in the
situation obtained by the base change $S' \to S$. So, by what precedes, one is reduced to showing that $u$ is open at
the point $x$.

Set $y = u(x)$. Since $u$ is locally of finite presentation (since $f$ and $q$ are, cf. EGA IV₁, 1.4.3), then by EGA
IV₁, 1.10.3, it suffices to show that $u(\operatorname{Spec} O_{X,x}) = \operatorname{Spec}(O_{Y,y})$. For this, one may
assume $S$ affine and integral. Let then $\pi : S' \to S$ be its normalization; denote by $u' : X' \to Y'$ the morphism
deduced from $u$ by base change. Since the morphism $\pi_{Y} : Y' \to Y$ is integral and surjective, one has

```text
Spec(O_{Y,y}) = ⋃_{y′} π_Y(Spec(O_{Y′, y′})),
```

the union being taken over all points of $Y'$ above $y$; it therefore suffices to show that, for each such $y'$, and
every $x' \in X'_{y'}$ above $x$, one has $u'(\operatorname{Spec} O_{X', x'}) = \operatorname{Spec} O_{Y', y'}$. As the
hypotheses are preserved by the base change $\pi : S' \to S$, one is thus reduced to the case of $S'$, i.e., one may
assume $S$ integral and normal.

Now, the hypotheses on $f$ imply, by EGA IV₃, 14.3.13, that there exists an irreducible component $Z$ of $X$ containing
$z$ (and hence $x$), dominating $S$ and such that

$$ \dim_{z}(Z_{s}) = n = \dim(Z_{\eta}), $$

where $\eta$ is the generic point of $S$. Let $\xi$ be the generic point of $Z$. Since $u$, and hence also $u_{\eta} :
Z_{\eta} \to A^{n}_{\eta}$, is quasi-finite, the closure in $A^{n}_{\eta}$ of the point $u_{\eta}(\xi) = u(\xi)$ is of
dimension $n$, hence $u(\xi)$ is the generic point of $A^{n}_{\eta}$, which is also the generic point of $Y =
A^{n}_{S}$. Consequently, denoting by $g$ the restriction of $u$ to $Z$, the morphism $g : Z \to Y$ is quasi-finite and
dominant. Since $Y$ is normal, it follows from Lemma 5.6.0 that $g$ is open, so that $u$ is open at every point of $Z$,
in particular at the point $x$. Consequently, $u(\operatorname{Spec} O_{X,x}) = \operatorname{Spec} O_{Y,y}$, and this
completes the proof of Lemma 5.6.1.0. ∎

The following lemma advantageously replaces EGA IV₃, 14.5.10,[^N.D.E-VI_B-40] in that it is independent of noetherian
hypotheses.

**Lemma 5.6.1.** *Let $S$ be a scheme, $f : X \to S$ an $S$-scheme locally of finite presentation, $s$ a point of $S$,
$x$ a closed point of $X_{s}$. Suppose that $f$ is universally open at the generic point $z$ of an irreducible component
$z$ of $X_{s}$, containing $x$ and such that $\dim_{x}(X_{s}) = \dim z$. Then there exists a commutative diagram:*

```text
            f
X ──────────────→ S
▲                ▲
│ h              │ w
│        φ       │
│ ↘            ↗
S″ ─────────→ S′
            π
```

*where $S'$ is an affine scheme, $w$ an étale morphism, $\pi$ a finite surjective morphism, of finite presentation, and
$\phi^{-1}(s)$ is formed of a single point $s''$, such that $h(s'') = x$ and $\kappa(s'') = \kappa(x)$.*[^N.D.E-VI_B-41]

<!-- label: III.VI_B.5.6.1 -->

<!-- original page 360 -->

*Proof.* First, one may assume $S = \operatorname{Spec} A$ and $X = \operatorname{Spec} B$, where $B$ is an $A$-algebra
of finite presentation. Let $p$ and $q$ be the prime ideals of $A$ and $B$ corresponding to $s$ and $x$, respectively,
so that $p = A \cap q$. Set $n = \dim_{x} X_{s}$, and let $t_{1}, \cdots, t_{n}$ be elements of $B$ whose images in
$O_{X_{s}, x} = B_{q} / p B_{q}$ form a system of parameters. Then $O_{X_{s}, x}/(t_{1}, \cdots, t_{n})$ is of finite
dimension over $\kappa(x)$ and hence also over $\kappa(s)$, since $x$ is a closed point of the $\kappa(s)$-algebraic
scheme $X_{s}$. Consequently, the $S$-morphism

```text
u : X ─→ A^n_S = Spec(A[T_1, …, T_n]),
```

defined by $T_{i} \mapsto t_{i}$, is of finite presentation, $x$ is isolated in its fiber $u^{-1}(u(x))$, and one has
$u(x) = \tau_{0}(s)$, where $\tau_{0} : S \to A^{n}_{S}$ denotes the "zero section" of $A^{n}_{S} \to S$, corresponding
to the morphism of $A$-algebras $A[T_{1}, \cdots, T_{n}] \to A$ that sends each $T_{i}$ to 0. Since the set of points of
$X$ that are isolated in their fiber above $A^{n}_{S}$ is open (EGA IV₃, 13.1.4), one may assume, shrinking $X$, that
$u$ is quasi-finite and that $u^{-1}(u(x)) = {x}$. By Lemma 5.6.1.0, $u$ is universally open at the point $x$.

Let $B_{0} = B/(t_{1}, \cdots, t_{n})$ and let $X_{0} = X \times_{A^{n}_{S}} \tau_{0}(S) = \operatorname{Spec} B_{0}$
and $u_{0} : X_{0} \to S$ be the morphism deduced from $u$ by the base change $\tau_{0} : S \hookrightarrow A^{n}_{S}$.
Then $u_{0}$ is quasi-finite and of finite presentation, universally open at the point $x$, and $x$ is the unique point
of `X_0` above $s$.

Let $A'$ be the henselization of the local ring $A_{p} = O_{S,s}$, and let $S' = \operatorname{Spec}(A')$, $B'_{0} =
B_{0} \otimes_{A} A'$, and $X'_{0} = X_{0} \times_{S} S' = \operatorname{Spec}(B'_{0})$. Then the closed point $s'$ of
$S'$ is the unique point of $S'$ above $s$, one has $\kappa(s') = \kappa(s)$, and $X'_{0}$ has a unique point $x'$ above
$s'$; one has $\kappa(x') = \kappa(x)$ and $x'$ is also the unique point of $X'_{0}$ above $s$ and above $x$. Since $A'$
is henselian, by EGA IV₄, 18.5.11, $X'_{0}$ is the disjoint sum of two open and closed parts:

```text
(*)    X′_0 = V ⊔ W,    where V = Spec(O_{X′_0, x′});
```

and the local ring $O_{X'_{0}, x'}$ is finite and of finite presentation over $A'$. The restriction $\pi$ of $u'_{0}$ to
$V$ is therefore finite and of finite presentation. Moreover, since $u'_{0} : X'_{0} \to S'$ is open at $x'$, one has
$u'_{0}(V) = \operatorname{Spec}(O_{S', s}) = S'$, so that $\pi$ is surjective.

This proves the desired result when $S = S'$. In the general case, $A'$ is a filtered direct limit of subalgebras
$A_{i}$ étale over $A$, and such that $S_{i} = \operatorname{Spec}(A_{i})$ has a unique point $s_{i}$ above $s$ (and
$\kappa(s_{i}) = \kappa(s)$). Then $B'_{0} = \lim B_{i}$, where $B_{i} = B_{0} \otimes_{A} A_{i}$. Set $X_{i} =
\operatorname{Spec}(B_{i}) = X_{0} \times_{S} S_{i}$ and $C = O_{X'_{0}, x'}$. By (∗) above, one has $C \cong B'_{0} / f
B'_{0}$, for some idempotent $f \in B'_{0}$, and there exist an index $i$ and $f_{i} \in B_{i}$ such that $f$ is the
image of $f_{i}$ in $B'_{0}$. Set $C_{i} = B_{i} / f_{i} B_{i}$ and $V_{i} = \operatorname{Spec}(C_{i})$.

<!-- original page 361 -->

Then $C = C_{i} \otimes_{A_{i}} A'$, whence $V = V_{i} \times_{S_{i}} S'$, and $C_{i}$ is an $A_{i}$-algebra of finite
presentation (since the same is true of $B_{i}$). Consequently, the morphisms:

```text
X′_0 ──── u′_0 ────→ S′
   ▲                  ▲
   │ h′                │ π
   │                  │
   V ─────────────────┘
```

come, by the base change $S' \to S_{i}$, from morphisms of finite presentation:

```text
X_i ──── u_i ────→ S_i
   ▲                ▲
   │ h_i             │ π_i
   │                ▲
   V_i ────────────┘
```

For every $j \geq i$, let $V_{j} = V_{i} \times_{S_{i}} S_{j}$ and let $\pi_{j} : V_{j} \to S_{j}$ be the morphism (of
finite presentation) deduced from $\pi_{i}$ by base change. Since $\pi : V \to S'$ is finite and surjective, by EGA IV₂,
8.10.5, there exists an index $j$ such that $\pi_{j} : V_{j} \to S_{j}$ is finite and surjective. Then $w : S_{j} \to S$
is étale affine, $S_{j}$ has a unique point $s_{j}$ above $s$, and $V_{j}$ has a unique point $x_{j}$ above $s_{j}$
(since $x'$ is the unique point of $V = V_{j} \times_{S_{j}} S'$ above $s'$):

```text
X_j ────→ X_0 ────→ X
 ▲          ▲        ▲
 │ u_j      │ u_0    │ u
 │ h_j      │ f      │ f
 │          │        │
 V_j ─────→ S_j ────→ S ─── τ_0 ───→ A^n_S.
            π_j        w
```

Hence $x_{j}$ is the unique point of $V_{j}$ above $s$, its image under the morphism $V_{j} \to X_{j} \to X$ is $x$, and
one has $\kappa(x_{j}) = \kappa(x)$. ∎

<!-- original page 354 -->

**Lemma 5.6.2.0.** [^N.D.E-VI_B-42] *Let $k$ be a field and $G$ a non-empty $k$-scheme of finite type.*

*(i) Let $K$ be an extension of $k$ and $W$ a dense open subset of `G_K`. Denote by $\pi$ the projection $G_{K} \to G$;
then*

```text
U = {g ∈ G | W contains every maximal point of π⁻¹(g)}
```

*is a dense open subset of $G$. (N.B. If $g$ is a closed point of $G$ belonging to $U$, then $\pi^{-1}(g) \subset W$.)*

*(ii) Suppose moreover $G$ geometrically irreducible. Let `µ : G × X → Y` be a morphism of $k$-schemes, $x$ a point of
$X$, and $\Omega$ an open of $Y$ such that `µ_x⁻¹(Ω_{κ(x)}) ≠ ∅`, where `µ_x` denotes the morphism $G_{\kappa(x)} \to
Y_{\kappa(x)}$, `g ↦ µ(g, x)`. Then:*

```text
U = {g ∈ G | µ sends every maximal point of g × x into Ω}
```

*is a dense open subset of $G$, and for every closed point $g$ of $G$ belonging to $U$, one has `µ(g × x) ⊂ Ω` and hence
`µ(g′, x) ∈ Ω_{κ(x)}` (resp. `µ(g, x′) ∈ Ω_{κ(g)}`), for every point $g' \in G_{\kappa(x)}$ above $g$ (resp. $x' \in
X_{\kappa(g)}$ above $x$).*

*(iii) Suppose $G = H^{0}$, where $H$ is a $k$-group scheme locally of finite type, acting on a non-empty $k$-scheme $X$
in such a way that the morphism $H \times_{S} X \to X \times_{S} X$, $(h, x) \mapsto (hx, x)$ is surjective. Let $U$ be
an open of $X$. Then:*

*(a) $G \cdot U$ is an open of $X$, equal to the union of the irreducible components of $X$ whose generic point belongs
to $U$.*

*(b) Suppose $U$ dense in every irreducible component of $X$. Then, for every finite subset $A$ of $X$, there exists a
closed point $g \in G$ such that $g \cdot A' \subset U_{\kappa(g)}$, where $A'$ is the inverse image of $A$ in
$X_{\kappa(g)}$. In particular, the morphism $G \times U \to X$ is surjective.*

<!-- label: III.VI_B.5.6.2.0 -->

*Proof.* (i) Let $\bar{k}$ be a separable closure of $k$ and let $L$ be an extension of $k$ containing a copy of
$\bar{k}$ and of $K$. Denote by $\pi_{L}$ (resp. $\phi$) the projection $G_{L} \to G$ (resp. $G_{L} \to G_{K}$). Since,
for every $g \in G$, $\phi$ sends the maximal points of $\pi^{-1}_{L}(g)$ surjectively onto those of $\pi^{-1}(g)$, one
sees that `U = {g ∈ G | W_L contains every maximal point of π_L⁻¹(g)}`. So, replacing $K$ by $L$, we reduce to the case
where $K$ contains $\bar{k}$.

Since the projection $p : G_{K} \to G_{\bar{k}}$ is surjective and open, $V = p(W)$ is a dense open of $G_{\bar{k}}$,
and since $p^{-1}(g) = \operatorname{Spec}(\kappa(g) \otimes_{\bar{k}} K)$ is irreducible for every $g \in G_{\bar{k}}$
(cf. EGA IV₂, 4.3.3), then for every $g \in V$, the generic point of $p^{-1}(g)$ belongs to $W$. On the other hand, let
$\Gamma = \operatorname{Gal}(\bar{k}/k)$; since the projection $q : G_{\bar{k}} \to G$ is surjective and $\Gamma$ acts
transitively on the fibers of $q$, then $U = q(V')$, where $V'$ is the intersection of the $\Gamma$-conjugates of $V$.

<!-- original page 362 -->

Now, let $Z$ be the closed $G_{\bar{k}} - V$, with its reduced closed subscheme structure. Since $G_{\bar{k}}$, and
hence $Z$, is of finite presentation over $\bar{k}$, $Z$ comes by base change from a reduced closed subscheme `Z_1` of
$G \otimes_{k} k_{1}$, for some finite Galois extension $k_{1}$ of $k$, so the $\Gamma$-conjugates of $Z$ are finite in
number, so that their union is again a rare closed $F$ of $G_{\bar{k}}$, and $V' = G_{\bar{k}} - F$ is a dense open of
$G_{\bar{k}}$. Hence, since the projection $q : G_{\bar{k}} \to G$ is surjective and open, $U = q(V')$ is a dense open
of $G$. Moreover, for every closed point $g$ of $G$, the fiber $\pi^{-1}(g)$ is formed of finitely many closed points of
`G_K`, so if $g \in U$ then $\pi^{-1}(g) \subset W$. This proves (i), and (ii) follows from it.

On the other hand, (iii)(a) has been proved in (VI_A, 2.6.4). Finally, if $U$ is dense in every irreducible component of
$X$, then $X = G \cdot U$, hence for every $x \in X$, `µ_x⁻¹(U_{κ(x)})` is a non-empty open of $G_{\kappa(x)}$, and then
(iii)(b) follows from (ii). ∎

**Corollary 5.6.2.** *Let $S$, $G$, $X$ be as in the preliminary hypotheses of 5.3, and let $U$ be an open of $X$, $s
\in S$, and $A$ a finite part of $X_{s}$. Suppose $U_{s}$ dense in $X_{s}$ and $X_{s}$ locally of finite type over
$\kappa(s)$.*[^N.D.E-VI_B-43]

*Then there exists a morphism $f : S'' \to S$, composed of a finite surjective morphism $S'' \to S'$ and an étale
morphism $S' \to S$, and a morphism $h : S'' \to G$, such that the inverse image $A''$ of $A$ in $X \times_{S} S''$
(i.e. in $X_{s} \times_{\operatorname{Spec} \kappa(s)} S''_{s}$) is contained in $\ell^{-1}_{h}(U_{S''})$, where
$\ell_{h}$ denotes the translation of $X_{S''} = X \times_{S} S''$ defined by the element $h \in G(S'')$.*

<!-- label: III.VI_B.5.6.2 -->

*Proof.* Since $X_{s}$ is locally of finite type over $\kappa(s)$, the connected components of $X_{s}$ are open, and
irreducible (cf. (VI_A, 2.5.4)), so $U_{s}$ is dense in every irreducible component of $X_{s}$.

Hence, by Lemma 5.6.2.0, there exists a closed point $g \in G^{0}_{s}$ such that $g \cdot a' \in U_{s}
\otimes_{\kappa(s)} \kappa(g)$ for every $a' \in X_{\kappa(g)}$ above a point of $A$.

<!-- original page 355 -->

By Lemma 5.6.1, there exists a morphism $f : S'' \to S$, composed of a finite surjective morphism $S'' \to S'$ and an
étale morphism $S' \to S$, and a morphism $h : S'' \to G$, such that $f^{-1}(s)$ is formed of a single point $s_{0}$,
and such that $h(s_{0}) = g$ and $\kappa(s_{0}) = \kappa(g)$. Then, denoting by $A''$ the inverse image of $A$ in $X_{s}
\times_{\operatorname{Spec} \kappa(s)} S''_{s} = X_{s} \otimes_{\kappa(s)} \kappa(s_{0}) = X_{s} \otimes_{\kappa(s)}
\kappa(g)$, the translation $\ell_{h}$ of $X_{S''}$ sends $A''$ into $U_{s} \otimes_{\kappa(s)} \kappa(s_{0})$. ∎

**Lemma 5.6.3.** *Let $X$ be an $S$-scheme. The following conditions are equivalent:*

*(i) $X$ is separated over $S$.*

*(ii) For every $S$-scheme $T$, every section $\sigma : T \to X_{T}$ is a closed immersion.*

*(iii) For every reduced $S$-scheme $T$, two $S$-morphisms $f_{1}$ and $f_{2} : T \to X$ that coincide on a dense open
$U$ of $T$ are equal.*

*(iv) For every $s \in S$ and every pair of points $x_{1}$, $x_{2}$ of $X_{s}$, there exists a morphism $\phi : S'' \to
S' \to S$ and an open subscheme $V$ of $X_{S''}$, separated over $S''$, such that:*

*a) $S' \to S$ is open, $S'' \to S'$ closed surjective, and $\phi^{-1}(s) \neq \emptyset$.*

*b) The inverse image of ${x_{1}, x_{2}}$ in $X_{S''}$ is contained in $V$.*

*(iv′) For every $s \in S$, every pair of points $x_{1}, x_{2} \in X_{s}$ is contained in an open $V$ of $X$, separated
over $S$.*[^N.D.E-VI_B-44]

<!-- label: III.VI_B.5.6.3 -->

*Proof.* The implication (ii) ⇒ (i) is clear (take $T = X$ and $\sigma =$ the diagonal section), as is (i) ⇒ (iv′) ⇒
(iv). On the other hand, one has (i) ⇒ (ii) by EGA I, 5.4.6.

(iii) ⇒ (ii). Let $\sigma : T \to X_{T}$ be a section of $p : X_{T} \to T$. By EGA I, 5.3.13, $\sigma$ is an immersion,
i.e. an isomorphism of $T$ onto a locally closed subscheme $E$ of `X_T`. To show that $E$ is closed, one may assume $T$
and $E$ reduced. Let `Ē` be the reduced closed subscheme of `X_T` having the closure of $E$ as underlying space, so that
$E$ is a dense open subscheme of `Ē`. Then the immersion $i : \bar{E} \hookrightarrow X_{T}$ and $\sigma \circ p \circ
i$ coincide on $E$, hence on `Ē` by hypothesis (iii). Hence every point of `Ē` belongs to $\sigma(T) = E$, whence $E =
\bar{E}$.

<!-- original page 364 -->

(i) ⇒ (iii). Suppose $X$ separated over $S$ and let $T$ be a reduced $S$-scheme, $f_{1}, f_{2}$ two $S$-morphisms $T \to
X$ that coincide on a dense open $U$ of $T$, and $g$ the morphism $T \to X \times_{S} X$ with components $f_{1}$ and
$f_{2}$. Since $D = \Delta_{X/S}(X)$ is closed, its inverse image under $g$ is a closed subset of $T$ containing $U$,
hence equal to $T$, and since $T$ is reduced, $g$ factors through $D$ (cf. EGA I, 5.2.2); consequently $f_{1} = p_{1}
\circ g$ equals $p_{2} \circ g = f_{2}$.

(iv) ⇒ (iii). Let $T$ be a reduced $S$-scheme and $f_{1}, f_{2}$ two $S$-morphisms $T \to X$ that coincide on a dense
open $U$. Since $T$ is reduced, to see that $f_{1} = f_{2}$, it suffices to see that $f_{1} = f_{2}$ set-theoretically.
Indeed, suppose this established, and let $t \in T$, $V$ an affine open of $X$ containing $f_{1}(t) = f_{2}(t)$, and $W$
the open neighborhood of $t$ equal to the inverse image of $V$ under the continuous map underlying $f_{1}$ and $f_{2}$;
then the morphisms $f_{i}|_{W} : W \to V$ coincide on the dense open $U \cap W$ of $W$. Since $V$ is separated and $W$
reduced, this entails that $f_{1}|_{W} = f_{2}|_{W}$, whence $f_{1} = f_{2}$.

Let then $t \in T$ and $s$ its image in $S$; let us show that the points $x_{1} = f_{1}(t)$ and $x_{2} = f_{2}(t)$ of
$X_{s}$ are equal. Let $\phi : S'' \to S' \to S$ and $V$ an open of $X \times_{S} S''$ as in (iv); set $T' = T
\times_{S} S'$ and $T'' = T \times_{S} S''$ and denote by $g : T'' \to T$ and $f_{i}'' : T'' \to X_{S''}$ ($i = 1, 2$)
the morphisms obtained by base change.

Since $U$ is dense in $T$ and $T' \to T$ is open, the inverse image $U'$ of $U$ in $T'$ is dense in $T'$. Let $U''$ be
the inverse image of $U'$ in $T''$ and let $F$ be the reduced subscheme of $T''$ having $U''$ as underlying space. Since
$T'' \to T'$ is surjective and closed, the image of $F$ contains $U'$ and is closed, hence equals $T'$. Consequently, $F
\cap g^{-1}(t)$ contains a point $u$.

For $i = 1, 2$, denote by $h_{i}$ the restriction to $F$ of $f_{i}''$. Then $h_{i}(u)$ is a point of $X_{S''}$ above
$f_{i}(t) = x_{i}$, hence belongs to $V$, since $V$ contains the inverse image of ${x_{1}, x_{2}}$ in $X_{S''}$.

Then $W = h^{-1}_{1}(V) \cap h^{-1}_{2}(V)$ is an open of $F$, containing $u$, and the $S''$-morphisms $h_{i}|_{W} : W
\to V$ coincide on the dense open $U'' \cap W$ of $W$. Since $V$ is separated over $S''$, one has $h_{1}|_{W} =
h_{2}|_{W}$, whence $h_{1}(u) = h_{2}(u)$, and hence $f_{1}(t) = f_{2}(t)$. This proves (iv) ⇒ (iii). ∎

Theorem 5.3 then follows from 5.6.2 and the implication (iv) ⇒ (i) of 5.6.3. ∎

**Counterexample 5.6.4.** *Not every $S$-group $G$ is separated. Let $S$ be a scheme having a non-isolated closed point
$s$; let $G$ be the scheme obtained by glueing two copies of $S$ along the open $S - {s}$; one sees easily that $G$ is
not separated over $S$, and that it is equipped with a natural structure of $S$-group, all of whose fibers are trivial,
except the fiber $G_{s}$ which is isomorphic to the two-element group $\mathbb{Z}/2\mathbb{Z}$.*[^N.D.E-VI_B-45]

<!-- label: III.VI_B.5.6.4 -->

**Theorem 5.7.** [^N.D.E-VI_B-46] *Let $S$ be a scheme, $G$ an $S$-group locally of finite presentation over $S$ such
that the function $s \mapsto \dim G_{s}$ is locally constant on $S$, $X$ an $S$-scheme on which $G$ acts, and $U$ an
open of $X$, separated over $S$. Then $G^{0} \cdot U$ is an open of $X$, separated over $S$.*

<!-- label: III.VI_B.5.7 -->

<!-- original page 365 -->

*Proof.* Denote by `µ : G ×_S X → X` the action of $G$ on $X$; it is the composition of the automorphism $(g, x) \mapsto
(g, gx)$ of $G \times_{S} X$ and the projection onto $X$. Since $G \times_{S} U$ is an open of $G \times_{S} X$, by 4.2
(iii), $V = G^{0} \cdot U$ is open in $X$.

Then, proceeding as in the proof of 5.6.2, one deduces from the implication (iv) ⇒ (i) of 5.6.3 that $V$ is separated
over $S$. ∎

**Corollary 5.7.1.** *Let $S$ and $G$ be as in 5.7, and let $\sigma$, $\tau$ be two $S$-sections of $G^{0}$ (i.e.
$\sigma, \tau \in G^{0}(S)$). Then the coincidence subscheme $S(\sigma, \tau) \subset S$ of $\sigma$ and $\tau$ (i.e.
the inverse image of the diagonal of $G \times_{S} G$ under the morphism $(\sigma, \tau)$) is closed.*

<!-- label: III.VI_B.5.7.1 -->

Indeed, for every $s \in S$, let $U$ be an affine open of $G$ containing $\epsilon(s)$; then $V = \epsilon^{-1}(U)$ is
an open neighborhood of $s$ in $S$, and since $G^{0} U$ is separated, $S(\sigma, \tau) \cap V$ is closed in $V$. ∎

**Remark 5.7.2.** *Gabber points out to us that one can show that if $S$ is henselian local, with closed point $s$, then
the intersection of the opens $G^{0} U$, where $U$ runs through the affine open neighborhoods of $\epsilon(s)$, is an
open group subscheme of $G$, separated over $S$.*

<!-- label: III.VI_B.5.7.2 -->

### 5.8. Complements.

[^N.D.E-VI_B-47] Let us begin by recalling Proposition (VI_A, 2.6.6):

**Proposition 5.8.1.** *Let $k$ be a field, $G$ a $k$-group locally of finite type acting on a $k$-scheme $X$ in such a
way that the morphism $G \times X \to X \times X$, $(g, x) \mapsto (gx, x)$ is surjective. Suppose $X$ quasi-separated.
Then the connected components of $X$ are irreducible.*

<!-- label: III.VI_B.5.8.1 -->

**Corollary 5.8.2.** *Let $S$, $G$, $X$ be as in the preliminary hypotheses of 5.3. Suppose moreover that every fiber
$X_{s}$ is quasi-separated and connected. Then $X$ is separated and quasi-compact over $S$.*

<!-- label: III.VI_B.5.8.2 -->

Indeed, by the preceding proposition, each fiber $X_{s}$ is irreducible, and the rest of the proof is identical to that
of 5.4. ∎

**Example 5.8.3.** *Fix an algebraically closed field $k$. Recall first that every "locally Boolean" topological space
$X$ (i.e. having a basis of compact open subsets), equipped with the sheaf of locally constant functions with values in
$k$, is a $k$-scheme (cf. [DG70], I § 1, 2.12). One then says that $X$ is a* locally Boolean $k$-scheme.

*Note moreover that every topological space $E$ admitting a basis of separated opens (and likewise every scheme $X$)
admits a dense separated open. Indeed, since every increasing union of separated opens is a separated open (for a scheme
$X$ this follows from 5.6.3), there exists such an open $U$ which is maximal. But then $U$ is dense, for if there
existed a non-empty open $V$ such that $U \cap V = \emptyset$, then $V$ would contain a non-empty separated open $W$,
and $U \cup W$ would still be separated, contradicting the maximality of $U$.*

*Now, let $C$ be the Cantor space, viewed as the underlying space of the group $(\mathbb{Z}/2\mathbb{Z})^{\mathbb{N}}$
equipped with the product topology. For every point $p$ of $C$, let $C(p)$ be another copy of $C$, and let $X$ be the
space obtained by glueing each $C(p)$ to $C$ along $C - {p}$; then $X$ is a non-separated locally Boolean $k$-scheme,
and $C$ is a dense open of $X$.*

*Let $G$ be the group of automorphisms of the $k$-scheme $X$ (i.e., of homeomorphisms of $X$). Then $G$ acts
transitively on $X$. Indeed, $X$ is the union of $C$ and, for each point $p \in C$, of a second point $p'$, which can be
characterized as the unique point $x$ of $X - {p}$ such that $(C - {p}) \cup {x}$ is separated. It follows that every
automorphism $\phi$ of $C$ extends to an automorphism $\phi_{X}$ of $X$ such that $\phi_{X}(p') = \phi_{X}(p)'$ for
every $p$. On the other hand, the map $\theta_{p} : X \to X$ that exchanges $p$ and $p'$ and fixes the other points is
an automorphism of $X$. Finally, the group of automorphisms of $C$ acts transitively on $C$: for example, using the
group structure of $C$, it suffices to consider translations.*

*Hence the discrete $k$-group $G$ (hence locally of finite type) acts on the $k$-scheme $X$ in such a way that the
morphism $G \times X \to X \times X$, $(g, x) \mapsto (gx, x)$ is surjective, but $X$ is not separated (although $C$ is
a dense separated open).*

<!-- label: III.VI_B.5.8.3 -->

**Example 5.8.4.** *We retain the notations of the preceding example. Using the description of $C$ as the set of
sequences $(u_{n})_{n \in \mathbb{N}}$ of elements of $\mathbb{Z}/2\mathbb{Z}$, one sees that $C$ minus a point $p$ is
homeomorphic to a countable disjoint union of copies of $C$. Indeed, using e.g. the group structure of $C$, one reduces
by translation to the case where $p$ is the element `0`, i.e. the zero sequence; then $C - {0}$ is the disjoint union of
the subspaces $C_{i} = {(u_{n})_{n \in \mathbb{N}} | u_{i} = 1 and u_{j} = 0 for j < i}$, for $i \in \mathbb{N}$, each
homeomorphic to $C$. For every non-empty finite subset $F$ of $C$, one deduces, by induction on $|F|$, that $C - F$ is
homeomorphic to a countable disjoint union of copies of $C$, hence to $C$ minus a point.*

*For each $F$ of cardinality 2, let $C(F)$ be another copy of $C$, denote by $q_{F}$ the point `0` of $C(F)$, and choose
a homeomorphism $\phi_{F} : C(F) - {q_{F}} \xrightarrow{\sim} C - F$; let then $X'$ be the space obtained by glueing
each $C(F)$ to $C$ by means of $\phi_{F}$. Then $X'$ is a non-separated locally Boolean $k$-scheme. Moreover, it follows
from the construction that every locally constant function $f : X' \to k$ is constant. Indeed, if $x, y \in C$ and $F =
{x, y}$, every neighborhood of $q_{F}$ meets every neighborhood of $x$ or $y$, so if $f : X \to k$ is locally constant,
one has $f(x) = f(q_{F}) = f(y)$, and if $F' = {z, t}$ with $z, t \in C$, one likewise has $f(q_{F'}) = f(z) = f(q_{{z,
x}}) = f(x)$. Consequently, $X'$ is connected.*

*Moreover, every point $x \in X'$ has a pointed neighborhood homeomorphic to `(C, 0)`. More precisely, fix for each $F$
a homeomorphism of pointed topological spaces $h_{F} : (C, 0) \xrightarrow{\sim} (C(F), q_{F})$, and denote by $T$ the
group of translations of $C$. Then, if $x = q_{F}$ one has the homeomorphism $q_{F}$, and if $x \in C$, the translation
$t_{x} \in T$ is a homeomorphism $(C, 0) \xrightarrow{\sim} (C, x)$ (and it is the unique element of $T$ having this
property).*

<!-- original page 367 -->

*Denote by $L$ the free group generated by the $h_{F}$ and let $G = T * L$ be the "free product" (= coproduct) of $T$
and $L$. For every $h \in {h_{F}}_{|F|=2} \cup T$, let $\sigma(h)$ be the generator of $G$ corresponding to $h$ and let
$S(h)$ (resp. $B(h)$) be the source (resp. target) of $h$. It is convenient to also set $\sigma(h^{-1}_{F}) =
\sigma(h_{F})^{-1}$ and $S(h^{-1}_{F}) = B(h_{F})$ (resp. $B(h^{-1}_{F}) = S(h_{F})$), and to denote by $E$ the set
formed by $T$, and the $h_{F}$ and $h^{-1}_{F}$.*

*On the product space $P = G \times X'$ (where $G$ is endowed with the discrete topology), consider the equivalence
relation generated by the relations:*

```text
(gσ(h), x) ∼ (g, h(x))    when x ∈ S(h)
```

*for every $h \in E$, and let $Z$ be the quotient space. Then $Z$ is obtained from the disjoint union $\coprod_{g \in G}
{g} \times X'$ by glueing of opens, and hence, for every open $\Omega$ of $P$, its saturate $\tilde{\Omega}$ is open
(cf. [BTop], I § 5.1, Example 2). Explicitly, since every open of $P$ is the union of its intersections with the
"slices" ${g} \times X'$, it suffices to consider an open of the form ${1} \times W$, where $W$ is an open of $X'$. In
this case, the saturate is the union of ${1} \times W$, and of*

```text
{σ(h_1)} × h_1⁻¹(W ∩ B(h_1)),    {σ(h_1) σ(h_2)} × h_2⁻¹(h_1⁻¹(W ∩ B(h_1)) ∩ B(h_2)),
```

*etc., for all finite sequences $h_{1}, \cdots, h_{n}$ of elements of $E$, hence is open. Therefore the projection
$\pi : P \to Z$ is open.*

*Note moreover that the word $\sigma(h_{1}) \cdots \sigma(h_{n})$ is a reduced word of $G$, except if one of the $h_{i}$
is the neutral element of $T$ or if two consecutive $h_{i}$ belong to $T$, or if $(h_{i}, h_{i+1})$ equals $(h_{F},
h^{-1}_{F})$ or $(h^{-1}_{F}, h_{F})$. So, if $x \in X'$ and if an element $\beta = (\sigma(h_{1}) \cdots \sigma(h_{n}),
h^{-1}_{n} \cdots h^{-1}_{1}(x))$ belongs to ${1} \times X'$, then one may assume that each $h_{i}$ is a translation
$t_{i}$, and in this case the equality $\sigma(t_{1} \cdots t_{n}) = 1$ entails that $t_{1} \cdots t_{n} = 1$, and hence
$\beta = (1, x)$. Since the equivalence relation is compatible with the action of $G$ (acting on $P = G \times X'$ by
left translations on the first factor), one deduces that for every $g \in G$, the restriction of $\pi$ to ${g} \times
X'$ is injective.*

*Let then $z \in Z$ be arbitrary and let $(g, x) \in P$ be a representative of $z$. By what precedes, $U = \pi({g}
\times X')$ is an open neighborhood of $z$, and the continuous map ${g} \times X' \to U$ induced by $\pi$ is open and
bijective, hence a homeomorphism. This shows that $Z$ is locally isomorphic to $X'$ (hence also to $C$), and is
therefore still a locally Boolean $k$-scheme.*

*Finally, $G$ acts transitively on $Z$. Indeed, since every $z \in Z$ is $G$-conjugate to an element of the form
$\pi((1, x))$, it suffices to see that every element $(1, x) \in P$ is equivalent to an element $(\sigma(h), 0)$; now if
$x \in C$ one may take for $h$ the translation $t_{x}$, and if $x = q_{F}$ one may take $h = h_{F}$. Hence $Z$ is a
locally Boolean $k$-scheme equipped with a transitive action of the discrete group $G$, but $Z$ is not separated.*

<!-- label: III.VI_B.5.8.4 -->

## 6. Subfunctors and group subschemes[^VI_B-6-1]

<!-- label: III.VI_B.6 -->

**Definition 6.1.** *(i) Let $X$ be an $S$-functor (i.e., a functor from $(Sch/S)^{\circ}$ into `(Ens)`), $G$ an
$S$-functor in groups, $u$ and $v$ two $S$-morphisms from $X$ to $G$. The* transporter of $u$ into $v$, *denoted
$Transp(u, v)$, is the sub-$S$-functor of $G$ defined as follows:*

```text
Transp(u, v)(S′) = {g ∈ G(S′) | (int g) ∘ u_{S′} = v_{S′}}
                 = {g ∈ G(S′) | g_{S″} u_{S″}(x) g_{S″}⁻¹ = v_{S″}(x), ∀ x ∈ X(S″), S″ → S′}.
```

*In particular, $Transp(u, u)$ is a sub-$S$-functor in groups of $G$; it is called the* centralizer of $u$ *and is
denoted $Centr(u)$.*

*(ii) Let $G$ be an $S$-functor in groups, $X$ and $Y$ two sub-$S$-functors of $G$. The* transporter of $X$ into $Y$
*(resp. the* strict transporter of $X$ into $Y$*), denoted $Transp_{G}(X, Y)$ (resp. $Transpstr_{G}(X, Y)$), is the
sub-$S$-functor of $G$ defined as follows:*

```text
Transp_G(X, Y)(S′)    = {g ∈ G(S′) | (int g)(X_{S′}) ⊂ Y_{S′}}
                      = {g ∈ G(S′) | g_{S″} X(S″) g_{S″}⁻¹ ⊂ Y(S″), ∀ S″ → S′}

Transpstr_G(X, Y)(S′) = {g ∈ G(S′) | (int g)(X_{S′}) = Y_{S′}}
                      = {g ∈ G(S′) | g_{S″} X(S″) g_{S″}⁻¹ = Y(S″), ∀ S″ → S′}.
```

*Note that one has*

```text
Transpstr_G(X, Y) = Transp_G(X, Y) ∩ c(Transp_G(Y, X)),
```

*where $c$ denotes the inversion morphism of $G$.*[^N.D.E-VI_B-49]

*(iii) Let $G$ be an $S$-functor in groups, $H$ a sub-$S$-functor of $G$, $i$ the canonical $S$-morphism $H \to G$; the*
centralizer *and* normalizer *of $H$ in $G$ are the following sub-$S$-functors in groups of $G$:*

```text
Centr_G H = Centr(i) = Transp(i, i),    Norm_G H = Transpstr_G(H, H).
```

*Finally, the* center *of $G$ is the $S$-functor in groups $Centr(id_{G}) = Centr_{G} G$; it will be denoted `Centr G`.*

<!-- label: III.VI_B.6.1 -->

**Remark 6.1.1.** [^N.D.E-VI_B-50] It follows from the definitions that the functors $Transp(u, v)$ and $Transp_{G}(X,
Y)$ (and hence also $Transpstr_{G}(X, Y)$) commute with base change: for every $S' \to S$, if $G', X', Y', u', v'$ are
deduced from `G, X, Y, u, v` by base change, then

```text
Transp(u, v)_{S′} = Transp(u′, v′)    and    Transp(X, Y)_{S′} = Transp(X′, Y′).
```

<!-- label: III.VI_B.6.1.1 -->

<!-- original page 369 -->

**Proposition 6.2.** [^N.D.E-VI_B-51] *Let $G$ be an $S$-group. For a subfunctor $T$ of the functor $G$, consider the
following property:*

```text
(+f)  for every s ∈ S, T_s is representable by a closed subscheme of G_s.
```

*Let $u, w : X \to G$ and $v : Y \to G$ be morphisms of $S$-schemes. Then:*

*(i) $Transp(u, w)$ and $Centr(u) = Transp(u, u)$ satisfy condition $(+f)$.*

*(ii) $Transp_{G}(u(X), v(Y))$ and $Norm_{G} v(Y)$ satisfy condition $(+f)$ if, for every $s \in S$, $v_{s}$ is a closed
immersion.*

*(iii) $Transpstr_{G}(X, Y)$ satisfies condition $(+f)$ if, for every $s \in S$, $u_{s}$ and $v_{s}$ are closed
immersions.*

<!-- label: III.VI_B.6.2 -->

This follows from Remark 6.1.1 and from Corollary 6.2.5 below.[^N.D.E-VI_B-52]

**Definition 6.2.1.** *Let $f : X \to S$ be a morphism of schemes. One says that $f$ is* essentially free, *or that $X$
is* essentially free over $S$, *if one can find a covering of $S$ by affine open sets $S_{i}$, for every $i$ an
$S_{i}$-scheme $S'_{i}$ affine and faithfully flat over $S_{i}$, and a covering $(X'_{ij})_{j}$ of $X'_{i} = X
\times_{S} S'_{i}$ by affine open sets $X'_{ij}$, such that for every $(i, j)$, the ring of $X'_{ij}$ is a
projective[^N.D.E-VI_B-53] module over the ring of $S'_{i}$.*

<!-- label: III.VI_B.6.2.1 -->

**Proposition 6.2.2.** *a) If $X$ is essentially free over $S$, it is flat over $S$; the converse is true if $S$ is
Artinian.*

*b) If $S$ is the spectrum of a field, every $S$-scheme is essentially free over $S$.*

*c) If $X$ is essentially free over $S$, then $X' = X \times_{S} S'$ is essentially free over $S'$, for every $S' \to
S$. The converse is true if $S' \to S$ is faithfully flat and quasi-compact.*

<!-- label: III.VI_B.6.2.2 -->

<!-- original page 370 -->

The proof is immediate; for the converse in a) one uses the fact that a flat module over an Artinian local ring is
free.[^N.D.E-VI_B-54]

The introduction of Definition 6.2.1 is justified by the following theorem.

**Theorem 6.2.3.** *Let $S$ be a scheme, $Z$ an essentially free $S$-scheme, $Y$ a closed subscheme of $Z$. Consider the
functor $F = \prod_{Z/S} Y/Z : (Sch)^{\circ}_{/S} \to (Ens)$ defined by the following condition: $F(S') = \emptyset$
when $Y_{S'} \neq Z_{S'}$, and $F(S')$ is reduced to a single element otherwise.*[^N.D.E-VI_B-55]

*(i) This functor is representable by a closed subscheme $T$ of $S$.*

*(ii) If moreover $Y \to Z$ is of finite presentation, then so is $T \to S$.*

<!-- label: III.VI_B.6.2.3 -->

Let us first note that the functor under consideration is a sheaf for the (fpqc) topology: since $F(S') = \emptyset$ or
`{pt}` for every $S'$, this reduces to verifying that if $(S_{i})$ is an open covering of $S$ (resp. $S' \to S$ a
faithfully flat and quasi-compact morphism), and if each $Y_{S_{i}} \to Z_{S_{i}}$ (resp. $Y_{S'} \to Z_{S'}$) is an
isomorphism, then so is $Y \to Z$; this is clear (resp. follows from SGA 1, VIII 5.4 or EGA IV₂, 2.7.1).

Moreover, by SGA 1, VIII 1.9, faithfully flat and quasi-compact morphisms are of effective descent for the fibered
category of closed-immersion arrows. This allows us, with the notations of 6.2.1, to limit ourselves to the case where
$S = S'_{i}$.

Let then $(Z_{j})$ be a covering of $Z$ by affine open sets such that $\mathcal{O}(Z_{j})$ is a projective module over
$A = \mathcal{O}(S)$, and let $Y_{j} = Y \cap Z_{j}$ and $F_{j} : (Sch)^{\circ}_{/S} \to (Ens)$ be the functor defined
in terms of $(Z_{j}, Y_{j})$ as $F$ is in terms of $(Z, Y)$. It is a subfunctor of the final functor, and one obviously
has $F = \bigcap_{j} F_{j}$, which reduces us to proving that each $F_{j}$ is representable by a closed subscheme
$T_{j}$ of $S$ (for then $F$ will be representable by the closed subscheme $T$ intersection of the $T_{j}$). We may
therefore also suppose $Z$ affine, $Z = \operatorname{Spec}(B)$, where $B$ is a projective $A$-module. Let $L$ be a free
$A$-module with basis $(e_{\lambda})_{\lambda \in \Lambda}$, of which $B$ is a direct factor as an $A$-module, and let
$\phi_{\lambda} : L \to A$ be the "coordinate" forms relative to this basis. Let $E$ be a generating set of the ideal
$J$ of $B$ defining the subscheme $Y$ of $Z$, and let $I$ be the ideal in $A$ generated by the coordinates
$\phi_{\lambda}(x)$, for $x \in E$. For every $A$-algebra $C$, one sees then that the morphism $B \otimes_{A} C \to
(B/J) \otimes_{A} C$ is an isomorphism if and only if the image of $x \otimes 1$ in $L \otimes_{A} C$ is zero for every
$x \in E$, which amounts to saying that the kernel of $A \to C$ contains the ideal $I$. This shows that $T = V(I) =
\operatorname{Spec}(A/I)$ satisfies the desired condition, which proves (i).

Moreover, if $Y \to Z$ is of finite presentation, one may take $E$ finite, and then $I$ is a finitely generated ideal of
$A$, i.e. the closed immersion $T \to S$ is of finite presentation.

<!-- original page 371 -->

**Examples 6.2.4.** *Let us give important examples of functors which reduce to functors $\prod_{Z/S} Y/Z$ of the type
considered in 6.2.3 and for which it is useful to have representability criteria in what follows. We denote by $S$ a
scheme, and by `X, Y, Z`, etc., schemes over $S$.*

*a) Suppose given an $S$-morphism*

```text
(x)    q : X → Hom_S(Y, Z),
```

*($X$ acts on $Y$, with values in $Z$), i.e. a morphism*

```text
(xx)   r : X ×_S Y → Z.
```

*Consider a subscheme $Z'$ of $Z$, whence a monomorphism*

```text
Hom_S(Y, Z′) → Hom_S(Y, Z)
```

*which makes the first functor a subfunctor of the second; let $X'$ be the inverse image of this subfunctor under the
morphism $q$. This is the subfunctor of $X$ such that $X'(T)$ is the set of $x \in X(T)$ such that $q(x) : Y_{T} \to
Z_{T}$ factors through $Z'_{T}$. This functor $X'$ can be described as follows: set $P = X \times_{S} Y$, let $P'$ be
the inverse image of $Z'$ under $r : P \to Z$; then one has an obvious isomorphism*

```text
(xxx)  X′ ≃ ∏_{P/X} P′/P.
```

*One thus obtains: if $Y$ is essentially free over $S$ and $Z'$ closed in $Z$, the subfunctor $X'$ of $X$ is
representable by a closed subscheme of $X$.*[^N.D.E-VI_B-56] *If moreover $Z' \to Z$ is of finite presentation, then so
is $X' \to X$.*

*b) Suppose given two ways of letting $X$ act on $Y$ with values in $Z$, i.e. two morphisms*

```text
q_1, q_2 : X ⇒ Hom_S(Y, Z),
```

*and set $X' = Ker(q_{1}, q_{2})$: this is the subfunctor of $X$ such that $X'(T)$ is the set of $x \in X(T)$ such that
the two morphisms $q_{1}(x), q_{2}(x) : Y_{T} \Rightarrow Z_{T}$ are equal. Now the data of $q_{1}, q_{2}$ is equivalent
to the data of a morphism*

```text
q : X → Hom_S(Y, Z ×_S Z),
```

*or equivalently of a morphism $r : X \times_{S} Y \to Z \times_{S} Z$; set then $U = Z \times_{S} Z$, let $U'$ be the
diagonal subscheme of $Z \times_{S} Z$. Then $X'$ is nothing but the inverse image of the subfunctor
$\operatorname{Hom}_{S}(Y, U')$ of $\operatorname{Hom}_{S}(Y, U)$ under $q$, hence can be put in the form `(xxx)`, with
$P = X \times_{S} Y$, and $P'$ = inverse image of the diagonal under $r$, i.e. kernel of $r_{1}, r_{2} : X \times_{S} Y
\Rightarrow Z$. One is therefore in the conditions of (a).*

*One sees consequently that: if $Y$ is essentially free over $S$ and $Z$ separated over $S$, then the subfunctor $X'$ of
$X$ is representable by a closed subscheme of $X$.*[^N.D.E-VI_B-56] *If moreover $Z \to S$ is locally of finite type,
then $X' \to X$ is of finite presentation.*

<!-- original page 372 -->

*c) Suppose given a morphism*

```text
q : X → Hom_S(Y, Y),
```

*i.e. "$X$ acts on $Y$". Let $X'$ be the "kernel" of this morphism, i.e. the subfunctor $X'$ of $X$ such that $X'(T)$ is
the set of $x \in X(T)$ such that $q(x) : Y_{T} \to Y_{T}$ is the identity. This functor falls under b), as one sees by
introducing a second homomorphism*

```text
q′ : X → Hom_S(Y, Y)
```

*"by letting $X$ act trivially on $Y$". Hence: if $Y$ is essentially free and separated over $S$, the subfunctor $X'$ of
$X$ kernel of $q$ is representable by a closed subscheme of $X$.*[^N.D.E-VI_B-56] *If moreover $Y \to S$ is locally of
finite type, then $X' \to X$ is of finite presentation.*

*d) Under the conditions of c), consider the subfunctor $Y'$ of $Y$ "of the invariants under $X$", so that $Y'(T)$ is
the set of $y \in Y(T)$ such that the corresponding morphism $q(y) : X_{T} \to Y_{T}$ is "the constant $T$-morphism with
value $y$". Introducing $q'$ as in c), and the homomorphisms corresponding to $q$ and $q'$:*

```text
q, q′ : Y ⇒ Hom_S(X, Y),
```

*one sees that $Y'$ is precisely $Ker(q, q')$, and hence falls again under b) (with the roles of `X, Y` reversed and $Z
= Y$).*

*Consequently, if $X$ is essentially free over $S$ and $Y$ separated over $S$, then the subfunctor $Y'$ of $Y$ of the
invariants under $X$ is representable by a closed subscheme of $Y$.*[^N.D.E-VI_B-56] *If moreover $Y \to S$ is locally
of finite type, then $Y' \to Y$ is of finite presentation.*

*e) Constructions of the type made explicit in the preceding examples are particularly frequent in group theory. Thus,
when $G$ is an $S$-group scheme acting on the $S$-scheme $X$:*

$$ q : G \to \operatorname{Aut}_{S}(X), $$

*the kernel of $q$ ("the subgroup of $G$ acting trivially") is a closed subscheme of $G$ provided $X$ is essentially
free and separated over $S$ (example c)), and the subobject $X^{G}$ of invariants is a closed subscheme of $X$, provided
$G$ is essentially free over $S$ and $X$ separated over $S$ (example d)).*

*Let `Y, Z` be subschemes of $X$; consider the subfunctor $Transp_{G}(Y, Z)$ of $G$ ("transporter of $Y$ into $Z$"),
whose points with values in a $T$ over $S$ are those $g \in G(T)$ such that the corresponding automorphism of `X_T`
satisfies $g(Y_{T}) \subset Z_{T}$, i.e. induces a morphism $Y_{T} \to X_{T}$ factoring through $Y_{T} \to Z_{T}$.
Hence: if $Y$ is essentially free over $S$, and $Z$ closed in $X$, then $Transp_{G}(Y, Z)$ is a closed subscheme of $G$
(example a)).*

*One may also consider the strict transporter of $Y$ into $Z$,*[^N.D.E-VI_B-57] *whose points with values in a $T$ over
$S$ are those $g \in G(T)$ such that $g(Y_{T}) = Z_{T}$, which is nothing but $Transp_{G}(Y, Z) \cap
\sigma(Transp_{G}(Z, Y))$, where $\sigma$ is the inversion morphism of $G$. Consequently,*

<!-- original page 373 -->

*if $Y$ and $Z$ are essentially free over $S$ and closed in $X$, the strict transporter of $Y$ into $Z$ is a closed
subscheme of $G$.*

*An important case is the one where $X = G$, with $G$ acting on itself by inner automorphisms. If $H$ is a subscheme of
$G$, the strict transporter of $H$ into $H$ is also called the* normalizer of $H$ in $G$*, and denoted $Norm_{G} H$.
Hence: if $H$ is a closed group subscheme of $G$, essentially free over $S$, then $Norm_{G} H$ is representable by a
closed group subscheme of $G$.*

*Let finally $Z$ be a subscheme of $G$; then its centralizer $Centr_{G}(Z)$ in $G$ is the subfunctor in groups of $G$
defined by the procedure of d), when one considers that "$Z$ acts on $G$" by the operations induced by those of $G$;
hence if $Z$ is essentially free over $S$ and $G$ is separated over $S$, $Centr_{G}(Z)$ is a closed group subscheme of
$G$. In particular, if $G$ is essentially free and separated over $S$, then the center $C$ of $G$, which is none other
than $Centr_{G}(G)$, is a closed group subscheme of $G$.*

<!-- label: III.VI_B.6.2.4 -->

When $S$ is the spectrum of a field, 6.2.2 b) shows that in examples a) to e) above, the "essentially free" conditions
are automatically satisfied; only the separation conditions remain. Recalling that a group scheme over a field is
necessarily separated (VI_A, 0.3), one finds for example:

**Corollary 6.2.5.** *Let $G$ be a group scheme over a field $k$ and let $Y, Y'$ be two subschemes of $G$. Then:*

*(i) The centralizer of $Y$ in $G$ is a closed group subscheme of $G$; in particular, this is the case for the center
$Centr_{G}(G)$ of $G$.*

*(i′) More generally, if $u, v : X \to G$ are morphisms of schemes, $Transp_{G}(u, v)$ is representable by a closed
subscheme of $G$.*

*(ii) If $Y$ is closed, the transporter $Transp_{G}(Y', Y)$ is a closed subscheme of $G$. If $Y'$ is also closed, the
same conclusion holds for $Transpstr_{G}(Y', Y)$.*

*(iii) For every group subscheme*[^N.D.E-VI_B-58] *$H$ of $G$, $Norm_{G}(H)$ is a closed group subscheme of $G$.*

<!-- label: III.VI_B.6.2.5 -->

**Corollary 6.2.6.** [^N.D.E-VI_B-59] *Let $k$ be a field, $G$ a connected algebraic $k$-group. Then $Centr_{G}(G)$ is
representable by a closed group subscheme $Z$ of $G$, and $G/Z$ is an affine algebraic $k$-group.*

<!-- label: III.VI_B.6.2.6 -->

*Proof.* The first assertion is of course contained in 6.2.5 (i), but we shall see that it also follows from the proof
of the second assertion. Indeed, $G$ acts by the adjoint representation on the finite-dimensional $k$-vector spaces
$V_{n} = \mathcal{O}_{G,e}/\mathfrak{m}^{n+1}_{e}$ (where $\mathfrak{m}_{e}$ is the maximal ideal of
$\mathcal{O}_{G,e}$); let $K_{n}$ denote the kernel of the morphism $\rho_{n} : G \to GL(V_{n})$. By VI_A, 5.4.1,
$\rho_{n}$ induces a closed immersion $G/K_{n} \hookrightarrow GL(V_{n})$, hence each $G/K_{n}$ is affine. Since $G$ is
noetherian, the intersection $K$ of the $K_{n}$ equals one of the $K_{n}$, so $G/K$ is affine.

<!-- original page 374 -->

On the other hand, letting $Z$ denote the center of $G$, it is clear that $Z \subset K$. Let us show that $Z = K$. Let
$\hat{\mathcal{O}}_{G,e}$ denote the completion of $\mathcal{O}_{G,e}$ for the $\mathfrak{m}_{e}$-adic topology and `Ŝ`
its spectrum (resp. $S = \operatorname{Spec} \mathcal{O}_{G,e}$). Since $\hat{S} \to S$ is faithfully flat and since the
two morphisms

```text
K ×_k S → S,    (g, x) ↦ gxg⁻¹    resp.    (g, x) ↦ x
```

coincide after base change $\hat{S} \to S$, they coincide, i.e. $K$ acts trivially on $\mathcal{O}_{G,e}$. Now, by 6.2.4
e), the subobject $G^{K}$ of invariants of $G$ under $K$ (which is none other than $Centr_{G}(K)$) is a closed subscheme
of $G$, hence defined by a quasi-coherent ideal $\mathcal{I}$ of $\mathcal{O}_{G}$. As $G^{K}$ majorizes $S =
\operatorname{Spec} \mathcal{O}_{G,e}$ and $\mathcal{I}$ is of finite type (since $G$ is noetherian), there exists an
open neighborhood $U$ of $e$ such that $\mathcal{I}|_{U} = 0$. Then the subgroup $G^{K} = Centr_{G}(K)$ contains $U$,
hence also $U \cdot U$, which equals $G$ since $G$ is irreducible (VI_A 0.5). Hence $Centr_{G}(K) = G$, whence $K
\subset Z$ and therefore $Z = K$. ∎

**Remark 6.3.** *Let $k$ be an algebraically closed field, $G$ a $k$-group and $H$ a group subscheme of $G$; assume $G$
and $H$ are of finite type over $k$ and reduced. Then $Norm_{G} H$ (resp. $Centr_{G} H$) is representable by a group
subscheme of $G$, whose associated reduced subscheme is none other than the normalizer (resp. the centralizer) of $H$ in
$G$ in the sense of the* Bible.

<!-- label: III.VI_B.6.3 -->

**Proposition 6.4.** *Let $G$ be an $S$-group and $u : X \to G$ a monomorphism of $S$-schemes. Set $T = Transp_{G}(X,
X)$. The following conditions are equivalent:*

*(i) $T$ is a sub-$S$-functor in groups of $G$.*

*(ii) $T = Transpstr_{G}(X, X) = Norm_{G} X$.*

*These conditions are satisfied in each of the two following cases:*

*a) $X$ is of finite presentation over $S$.*

*b) $T$ is representable by a scheme of finite presentation over $S$.*

<!-- label: III.VI_B.6.4 -->

The equivalence of conditions (i) and (ii) follows from the fact that, whatever the morphism $S' \to S$, whatever $t, t'
\in T(S')$, one has $tt' \in T(S')$, and from the fact that $Transpstr_{G}(X, X) = T \cap c(T)$ (cf. 6.1 (ii)).

Let us place ourselves in case a). Let $t \in T(S)$; then $int(t)$ is a monomorphism of $X$ into $X$, hence an
$S$-automorphism of $X$ (EGA IV₄, 17.9.6), so that $t$ belongs to $Transpstr_{G}(X, X)$, whence a).

In case b), it is clear that $\mu(T \times_{S} T) \subset T$, and the assertion follows from the following lemma.

**Lemma 6.4.2.** [^N.D.E-VI_B-60] *Let $G$ be an $S$-scheme of finite presentation, equipped with an associative law (in
the sense of EGA 0_III 8.2.5). Suppose that for every $S$-scheme $S'$ and every $g \in G(S')$, right and left
translations by $g$ in the set $G(S')$ are injective, and that $G(S) \neq \emptyset$. Then $G$ is an $S$-group.*

<!-- label: III.VI_B.6.4.2 -->

<!-- original page 375 -->

It suffices to show that, whatever the $S$-scheme $S'$, the set $G(S')$ is a group; now from the hypothesis it follows
at once that right and left translations by every element $g \in G(S')$ in $G_{S'}$ are $S$-monomorphisms of $G_{S'}$
into $G_{S'}$. They are therefore $S$-automorphisms, since $G$ is of finite presentation over $S$ (EGA IV₄, 17.9.6), so
that right and left translations by $g$ in the set $G(S')$ are bijective, and one is reduced to the following lemma.

**Lemma 6.4.3.** *Let $G$ be a non-empty set equipped with an associative law such that right and left translations are
bijective. Then $G$ is a group.*

<!-- label: III.VI_B.6.4.3 -->

The proof is left to the reader.

**Definition 6.5.** *Let $G$ be an $S$-group, $H$ an $S$-functor, and $u : H \to G$ a monomorphism.*

*(i) The* connected centralizer of $H$ in $G$, *denoted $Centr^{0}_{G} H$, is the neutral component of the functor
$Centr_{G} H$ (cf. 3.1 and 6.1 (iii)).*

*(i′) For every morphism $u : X \to G$, one defines similarly the functor $Centr^{0}(u)$ (cf. 6.2 (iv)).*

*(ii) When for every $s \in S$, $u_{s}$ is a closed immersion, the* connected normalizer of $H$ in $G$*, denoted
$Norm^{0}_{G} H$, is the neutral component of the functor $Norm_{G} H$.*

*N.B. By 1.4.2, the hypothesis in (ii) is satisfied when $H$ is an $S$-group scheme, $G$ and $H$ are locally of finite
type over $S$, and $u$ is a quasi-compact morphism of $S$-groups.*

<!-- label: III.VI_B.6.5 -->

**Proposition 6.5.1.** *Let $G$ be an $S$-group locally of finite presentation and quasi-separated over $S$, $H$ a
smooth $S$-group with connected fibers, and $u : H \to G$ a monomorphism. Let $N$ be the normalizer of $H$ in $G$ (cf.
6.1). According to 6.5.5 below, $N$ is representable by a closed group subscheme of $G$, of finite presentation over
$G$. This being so, the following conditions are equivalent:*

*(i) The canonical morphism $H \to N$ is an open immersion.*

*(ii) $N^{0} = H$ (cf. 3.10).*

*(iii) For every $s \in S$, one has $H_{s} = (N_{s})^{0}$.*

<!-- label: III.VI_B.6.5.1 -->

Condition (i) entails (ii) by Lemma 3.10.1, since $H^{0} = H$. On the other hand, it is clear that (ii) entails (iii),
since $H_{s} = (N^{0})_{s} = (N_{s})^{0}$.

Let us show finally that (iii) entails (i). Since $H_{s} = (N^{0})_{s}$ for every $s \in S$, then $H_{s} \to N_{s}$ is
an open immersion. Moreover, $H$ and $N$ are locally of finite presentation over $S$, and $H$ is flat over $S$, hence
(EGA IV₄, 17.9.5), $H \to N$ is an open immersion. ∎

[^N.D.E-VI_B-61] For the reader's convenience, we have included below the results 6.8 to 6.11 of Exp. XI.

<!-- original page 376 -->

**Theorem 6.5.2.** *Let $X$ be a smooth scheme over $S$, with geometrically irreducible fibers.*[^N.D.E-VI_B-62]

*(i) For every closed subscheme $Y$ of $X$, the functor $\prod_{X/S} Y/X$ is representable by a closed subscheme $T$ of
$S$.*

*(ii) Moreover, if $Y \to X$ is of finite presentation, then so is $T \to S$.*

<!-- label: III.VI_B.6.5.2 -->

Since $f : X \to S$ is faithfully flat locally of finite presentation, it is covering for the (fpqc) topology. On the
other hand, since $T = \prod_{X/S} Y/X$ is obviously a subsheaf of $S$ for the (fpqc) topology, it follows that the
question of representability of $T$ by a closed subscheme of $S$ is local in nature on $S$ for the (fpqc)
topology,[^N.D.E-VI_B-63] and the same is true of the question of deciding whether $T$ is of finite presentation over
$S$ (cf. EGA IV₂, 2.7.1). Up to making the base change $S' \to S$, with $S' = X$, one is reduced to the case where $X$
admits a section $\epsilon$ over $S$. One may moreover suppose $S$ affine and a fortiori quasi-compact. One then has:

**Corollary 6.5.3.** *Under the conditions of 6.5.2, suppose that $S$ is quasi-compact, that $X \to S$ admits a section
$\epsilon$, and that $Y \to X$ is of finite presentation. Then there exists an integer $n \geqslant 0$ such that one
has*

```text
∏_{X/S} Y/X = ∏_{X_n/S} Y_n/X_n,
```

*where $X_{n}$ is the $n$-th infinitesimal neighborhood of the immersion $\epsilon : S \to X$, and $Y_{n} = Y \cap
X_{n}$.*

<!-- label: III.VI_B.6.5.3 -->

When $Y$ is of finite presentation over $X$, this corollary implies 6.5.2: indeed, $X$ being smooth over $S$, $X_{n}$ is
finite and locally free over $S$, hence a fortiori "essentially free" over $S$ (cf. 6.2.1), so $\prod_{X_{n}/S}
Y_{n}/X_{n}$ is representable by a closed subscheme $T$ of $S$, of finite presentation over $S$, by 6.2.3.

Let us first prove 6.5.3 (and hence 6.5.2) when $S$ is noetherian. Let $T_{n} = \prod_{X_{n}/S} Y_{n}/X_{n}$; then the
$T_{n}$ form a decreasing sequence of closed subschemes of $S$, and $S$ being noetherian, this sequence is stationary.
Let $R = \bigcap_{n \geqslant 0} \prod_{X_{n}/S} Y_{n}/X_{n}$ be their common value for large $n$; one has obviously $T
\subset R$, and it suffices to establish that $R \subset T$. Up to making the base change $R \to S$, one is reduced to
the case where $R = S$, i.e. $Y_{n} = X_{n}$ for every $n$, i.e. $Y \supset X_{n}$ for every $n$, and one must then
prove that $T = S$, i.e. $Y = X$.

Now $Y \supset X_{n}$ for every $n$ implies (thanks to the fact that $X$ is locally noetherian) that $Y$ is, in a
neighborhood of every point of $\epsilon(S)$, an induced open subscheme of $X$;[^N.D.E-VI_B-64] hence there exists an
induced open $U$ of $X$, containing $\epsilon(S)$, such that $U \subset Y$. By virtue of EGA IV₃, 11.10.10, the fibers
of $X/S$ being integral, $U$ is schematically dense in $X$, hence ($Y$ being a closed subscheme majorizing $U$) one has
$Y = X$. This proves 6.5.3 hence 6.5.2 when $S$ is noetherian.

<!-- original page 377 -->

The general case proceeds by reduction to the preceding case. For every $s \in S$, there exists an affine open
neighborhood $U$ of $s$ and an affine open neighborhood $V$ of $\epsilon(s)$ such that $f(V) \subset U$. Then $f(V)$ is
an open neighborhood of $s$ contained in $U$, and if $S'$ is an affine open neighborhood of $s$ contained in
$\epsilon^{-1}(V) \cap f(V)$, and $X' = V \cap f^{-1}(S')$, then $X'$ and $S'$ are affine opens of $X$ resp. $S$, and
$X'/S'$ admits a section. Because of the local nature of 6.5.2 and 6.5.3 we may suppose $S = S'$. Then $X'$ is an affine
open of $X$ containing $\epsilon(S)$. As each fiber $X_{s}$ is supposed irreducible, $X'_{s}$ is schematically dense in
$X_{s}$, hence, by EGA IV₃, 11.10.10, $X'$ is schematically dense in $X$, and similarly, for every base change $S_{1}
\to S$, $X' \times_{S} S_{1}$ is schematically dense in $X \times_{S} S_{1}$.

It follows that $\prod_{X/S} Y/X = \prod_{X'/S} Y'/X'$, where $Y' = Y \cap X'$. This reduces us to the case where $X =
X'$, so one may suppose $S$ and $X$ affine. Moreover, if $X = \operatorname{Spec}(B)$ and if $J$ is the ideal of $B$
defining $Y$, then $J$ is a direct limit of its finitely generated sub-ideals, hence $Y$ is the intersection of closed
subschemes $Y_{i}$ of $X$ which are of finite presentation over $X$, and consequently $\prod_{X/S} Y/X = \bigcap_{i}
\prod_{X/S} Y_{i}/X$, which reduces us, to prove 6.5.2, to the case where $Y$ is of finite presentation over $X$, with
$S$ and $X$ affine.

But then $X$ and $Y$ over $S$ come by base change $S \to S_{0}$ from an analogous situation `X_0` and `Y_0` over `S_0`,
with `S_0` noetherian, which reduces us to the case where $S$ is noetherian, already treated. This completes the proof
of 6.5.2 and 6.5.3. ∎

**Corollary 6.5.4.** *Let $X$ be a smooth $S$-group scheme of finite presentation with connected fibers, $Y$ a group
scheme of finite presentation over $S$, $i : Y \to X$ a monomorphism of $S$-group schemes.*

*(i) Then $\prod_{X/S} Y/X$ is representable by a closed subscheme of finite presentation of $S$.*

*(ii) If moreover $S$ is quasi-compact, one has for large enough $n$:*

```text
∏_{X/S} Y/X = ∏_{X_n/S} Y_n/X_n,
```

*where $X_{n}$ denotes the $n$-th infinitesimal neighborhood of the unit section $\epsilon : S \to X$, and $Y_{n} =
X_{n} \cap Y$.*

<!-- label: III.VI_B.6.5.4 -->

The proof is essentially that of 6.5.3.[^N.D.E-VI_B-65] On the one hand, $i$ is locally of finite presentation (cf. EGA
IV₁, 1.4.3). On the other hand, the unit sections of $Y$ and of $X$ induce bijective immersions $S \to Y_{n}$ and $S \to
X_{n}$, hence isomorphisms of $S_{red}$ with $(Y_{n})_{red}$ and $(X_{n})_{red}$. Consequently, $i_{n}$ is quasi-compact
hence of finite type, and one has a commutative diagram:

```text
(Y_n)_red ──τ──→ Y_n
       ╲        │
        ╲       │ i_n
       σ ╲      │
          ╲     ↓
           ─→  X_n
```

<!-- original page 378 -->

where $\sigma, \tau$ are closed immersions and $\tau$ is surjective. Since $i_{n}$ is separated (being a monomorphism),
it follows that $i_{n}$ is proper (cf. EGA II, 5.4.3). Hence $i_{n}$ is a proper monomorphism of finite presentation,
hence a closed immersion (cf. EGA IV₃, 8.11.5). Consequently, by virtue of 6.2.3 already used, $\prod_{X_{n}/S}
Y_{n}/X_{n}$ is representable by a closed subscheme $T_{n}$ of $S$ of finite presentation over $S$, and it remains
therefore to prove the last assertion of 6.5.4 in the case where one supposes moreover $S$ affine.

One reduces immediately again to the case where $S$ is noetherian, and one is reduced to proving that one has $R = T$
(with the notations of the proof of 6.5.3), or, again, that $Y \supset X_{n}$ for every $n$ implies $Y = X$. Now the
hypothesis implies that $i : Y \to X$ is étale at the points of the unit section of $Y$ over $S$, hence $Y$ is smooth
over $S$ at the points of the unit section, whence it follows that the open $U$ of points of $Y$ at which $Y$ is smooth
over $S$ is an induced open subgroup of $Y$ (cf. 2.3). Then $\tau : U \to X$ is an étale monomorphism by virtue of 2.5,
hence an open immersion; since the fibers of $X$ are connected and every open subgroup of an algebraic group is also
closed, it follows that $\tau$ is a surjective open immersion, i.e. an isomorphism. Hence $U = X$ and a fortiori $Y =
X$, which completes the proof of 6.5.4. ∎

Proceeding as in 6.2.4 e), one concludes from 6.5.4:

**Corollary 6.5.5.** *Let $G$ be an $S$-group scheme locally of finite type and quasi-separated over $S$, $H$ a smooth
group scheme of finite presentation over $S$ with connected fibers, $i : H \to G$ a monomorphism of $S$-groups. Then:*

*a) $Centr_{G}(H)$ and $Norm_{G}(H)$ are representable by closed subschemes of $G$, of finite presentation over $G$.*

*a′) Similarly, for every monomorphism $j : K \to G$ of finite presentation of $S$-group schemes, $Transp_{G}(H, K)$ is
representable by a closed subscheme of $G$, of finite presentation over $G$.*

*b) If $G$ is quasi-compact, there exists an integer $n \geqslant 0$ such that (if $H_{n}$ denotes the $n$-th
infinitesimal neighborhood of the unit section of $H$) one has:*

```text
Centr_G(H) = Centr_G(H_n)        Norm_G(H) = Norm_G(H_n)
Transp_G(H, K) = Transp_G(H_n, K) = Transp_G(H_n, K_n).
```

<!-- label: III.VI_B.6.5.5 -->

*Proof.* [^N.D.E-VI_B-66] Let us first note that the hypothesis on $G$ entails that the monomorphism $H \to G$ is of
finite presentation (EGA IV₁, 1.2.4 and 1.4.3), as is the diagonal immersion $\Delta_{G/S} : G \to G \times_{S} G$ (loc.
cit. 1.4.3.1). The case of $Norm_{G}(H)$ therefore reduces to that of the transporter, by taking $H = K$. Taking 6.2.4
e) into account, we shall apply 6.5.4 to the group scheme $X = H_{G} = H \times_{S} G$ over the base scheme $G$, and to
the following group subscheme $Y$.

In the case of $Transp_{G}(H, K)$, we take for $Y$ the inverse image of `K_G` under the morphism of $G$-groups $H
\times_{S} G \to G \times_{S} G$, $(h, g) \mapsto (ghg^{-1}, g)$. In the case of

<!-- original page 379 -->

$Centr_{G}(H)$, we take for $Y$ the inverse image of the diagonal subgroup $\Delta_{G/S}(G)_{G}$ of $(G \times_{S}
G)_{G}$ under the morphism of $G$-groups:

```text
H ×_S G → G ×_S G ×_S G,    (h, g) ↦ (h, ghg⁻¹, g).
```

∎

**Definition 6.6.** *Let $G$ be an $S$-functor in groups, $H$ a sub-$S$-functor in groups; one says that $H$ is*
invariant *(resp.* central\*, resp.\* characteristic\*) in $G$ if $Norm_{G} H = G$ (resp. if $Centr_{G} H = G$, resp.
if, whatever the $S$-scheme $T$ and the automorphism $a \in \operatorname{Aut}_{T-gr.}(G_{T})$, one has $a(H_{T})
\subset H_{T}$), in other words, if, whatever the $S$-scheme $T$, the subgroup $H(T)$ of $G(T)$ is invariant in $G(T)$
(resp. central in $G(T)$, resp. invariant under every automorphism of `G_T`).\*

*N.B. If $H$ is central (resp. characteristic), then it is invariant.*

<!-- label: III.VI_B.6.6 -->

**Remark 6.7.** *Let $G$ and $H$ be two $S$-groups and $u : H \to G$ a monomorphism. For $H$ to be invariant (resp.
central) in $G$, it is necessary and sufficient that the morphism*

```text
(μ ∘ c ∘ pr_2, μ ∘ (u × id_G)) : H ×_S G → G
```

*(defined by $(h, g) \mapsto g^{-1} h g$ whatever $g \in G(S')$ and $h \in H(S')$) factor through $u$ (resp. equal $u
\circ pr_{1}$), and for $H$ to be characteristic in $G$, it is necessary and sufficient that for every $S$-scheme $T$
and every $T$-automorphism of groups $a$ of `G_T`, $a \circ u(T)$ factor through $u(T)$.*

<!-- label: III.VI_B.6.7 -->

**Example 6.8.** *Let $G$ be an $S$-functor in groups. Then `Centr G` is characteristic and central. If, for every $s
\in S$, $G_{s}$ is representable, then $G^{0}$ is characteristic. This follows from the definitions and from 3.3.*

<!-- label: III.VI_B.6.8 -->

### 6.9.

[^N.D.E-VI_B-67] In [RG71], I 3.3.3, the authors introduce the geometric notion of pure $S$-scheme, which is local on
$S$ for the étale topology; we refer to loc. cit. for the precise definition. Let us simply point out the following:

a) (loc. cit., Th. 3.3.5) If $B$ is a flat $A$-algebra of finite presentation, then $B$ is a projective $A$-module if
and only if $\operatorname{Spec}(B)$ is pure over $\operatorname{Spec}(A)$.

b) Consequently, if $X \to S$ is locally of finite presentation, flat and pure, then $X$ is essentially free over $S$.

c) (loc. cit., 3.3.4 (iii)) If $X \to S$ is locally of finite type, flat, with geometrically irreducible fibers and
without embedded components, then $X$ is pure over $S$.

Since every group scheme locally of finite type over a field is Cohen–Macaulay (cf. VI_A, 1.1.1), hence without embedded
components, one obtains in particular:

d) Every $S$-group scheme $G$ locally of finite presentation, flat, and with connected fibers is pure over $S$, hence
essentially free over $S$.

One may then take up again all the statements of 6.2.4 e) taking into account results (b) and (d) above.

<!-- label: III.VI_B.6.9 -->

<!-- original page 380 -->

## 7. Generated subgroups; commutator group

<!-- label: III.VI_B.7 -->

In this number, $k$ denotes a fixed field.

**Proposition 7.1.** *Let $G$ be a $k$-group, $(X_{i})_{i \in I}$ a family of geometrically reduced
$k$-schemes;*[^N.D.E-VI_B-68] *for every $i \in I$, let $f_{i} : X_{i} \to G$ be a $k$-morphism.*

*(i) There exists a smallest closed group sub-$k$-scheme of $G$ majorizing each of the $f_{i}$, denoted
$\Gamma_{G}((f_{i})_{i \in I})$. It is a geometrically reduced $k$-scheme, hence smooth in the case where $G$ is
supposed locally of finite type over $k$ (1.3.1).*

*(ii) Set $X = \coprod_{i \in I} X_{i}$, and let $f : X \to G$ be the morphism whose restriction to $X_{i}$ is $f_{i}$,
for every $i \in I$. Set $X^{1} = X \sqcup X$, let $f^{1} : X^{1} \to G$ be the morphism whose restrictions to $X$ are
respectively $f$ and $c \circ f$. For every $n > 1$, set*

```text
X^n = X¹ ×_k X^{n−1}    and    f^n = μ ∘ (f¹ ×_k f^{n−1}) : X^n → G.
```

*Then $\Gamma_{G}((f_{i})_{i \in I})$ is the reduced subscheme of $G$ whose underlying space is the closure of the union
of the $f^{n}(X^{n})$, for $n \geqslant 1$.*

*(iii) For every $k$-scheme $S$, $\Gamma_{G}((f_{i})_{i \in I})_{S}$ is the smallest closed group subscheme of `G_S`
majorizing each of the $f_{i,S} : X_{S} \to G_{S}$.*

*(iii′) Moreover, $\Gamma_{G}((f_{i})_{i \in I})_{S}$ is the smallest group subscheme of `G_S` majorizing each of the
$f_{i,S}$.*[^N.D.E-VI_B-69]

<!-- label: III.VI_B.7.1 -->

Let us first note that, to prove (i), (iii) and (iii′), by defining $X$ and $f$ as in (ii), one is reduced to the case
where $I$ is reduced to a single element.

Let $H$ be the reduced subscheme of $G$ with underlying set $\bigcup_{n \geqslant 1} f^{n}(X^{n})$. Then the family of
morphisms $f^{n} : X^{n} \to H$ is schematically dominant (cf. EGA IV₃, 11.10.4), hence every closed subscheme of $G$
which majorizes the $f^{n}$ also majorizes $H$. Moreover, by loc. cit., 11.10.7, $H$ is geometrically reduced. Hence to
show (i) and (ii), it suffices to show that $H$ is a group subscheme of $G$, i.e. that the restriction of $c$ to $H$ and
the restriction of $\mu$ to $H \times_{k} H$ factor through the injection $H \to G$.

Since $H$ is geometrically reduced, $H \times_{k} H$ is reduced, and it suffices to verify that $c(H) \subset H$ and
that $\mu(H \times_{k} H) \subset H$ (set-theoretically). But by EGA IV₃, 11.10.6, the union of the $f^{n}_{(H)}(X^{n}
\times_{k} H)$ is schematically dense in $H \times_{k} H$. Similarly, for every $n \geqslant 1$, the union of the
$f^{m}_{(X^{n})}(X^{n} \times_{k} X^{m})$, for $m \geqslant 1$, is schematically dense in $X^{n} \times_{k} H$. Hence it
suffices to show that $\mu(f^{n}_{(H)}(f^{m}_{(X^{n})}(X^{n} \times_{k} X^{m}))) \subset H$ and that $c(f^{n}(X^{n}))
\subset H$. Now

```text
μ(f^n_{(H)} (f^m_{(X^n)} (X^n ×_k X^m))) = μ((f^n × f^m)(X^n ×_k X^m)) = f^{n+m}(X^{n+m}) ⊂ H;
```

and, since $c(f^{1}(X^{1})) \subset f^{1}(X^{1})$, one has, whatever $n$, $c(f^{n}(X^{n})) \subset f^{n}(X^{n}) \subset
H$. This proves (i) and (ii).

<!-- original page 381 -->

Let us now show (iii). Let $G'$ be a closed group subscheme of `G_S` majorizing $f_{S}$; we must show that $G'$
majorizes `H_S`, or, what amounts to the same, that $H_{S} = H_{S} \times_{G_{S}} G'$. Set $H'_{S} = H_{S}
\times_{G_{S}} G' = G' \cap H_{S}$. Since $G'$ and `H_S` both majorize the $f^{n}_{S}$, the same is true of $H'_{S}$.
Now (EGA IV₃, 11.10.6), since the family of $f^{n} : X^{n} \to H$ is schematically dominant, the same is true of the
family of $f^{n}_{S} : X^{n}_{S} \to H_{S}$, so that $H'_{S}$, which majorizes each of the $f^{n}_{S}$, is equal to
`H_S` by EGA IV₃, 11.10.1 c). This proves (iii).

Let us show finally that `H_S` is the smallest group subscheme (not necessarily closed) of `G_S` majorizing $f_{S}$.

Let $G'$ be a group subscheme of `G_S` majorizing $f_{S}$. It must likewise be shown that, if one sets $H'_{S} = H_{S}
\times_{G_{S}} G'$, then $H'_{S} = H_{S}$. It suffices for this to show that $H'_{S}$ is closed in `H_S` and to apply
(iii). It suffices therefore to show that `H_S` and $H'_{S}$ have the same underlying set, a fortiori it suffices to
show that, for every $s \in S$, $H_{s}$ equals

```text
H′_s := H′_S ×_S κ(s) = H_s ×_{G_s} G′_s.
```

Now, by VI_A, 0.5.2, the group sub-$\kappa(s)$-scheme $G'_{s}$ is closed in $G_{s}$. Hence $H'_{s}$ is closed in
$H_{s}$, and then the preceding reasoning, applied to $H'_{s}$, to $H_{s}$ and to the $f^{n}_{s}$, shows that $H'_{s} =
H_{s}$. ∎

**Corollary 7.1.1.** [^N.D.E-VI_B-70] *Let $G$ be a $k$-group locally of finite type and let `A, B` be two
sub-$k$-groups of $G$, smooth and of finite type, and $i_{A}$ (resp. $i_{B}$) the inclusion of $A$ (resp. $B$) into $G$.
Assume that $B$ normalizes $A$. Then $A \cdot B = \Gamma_{G}(i_{A}, i_{B})$.*

<!-- label: III.VI_B.7.1.1 -->

Indeed, let `H = A ⋊ B` be the semidirect product of $A$ and $B$ (cf. I, 2.3.5); it is a smooth $k$-group of finite
type. Then the group morphism $u : H \to G$, $(a, b) \mapsto ab$, is quasi-compact, hence, by 1.2, $u(H) = A \cdot B$ is
a closed reduced subscheme of $G$, which is a group in the category $(Sch/k)_{red}$. Now, by EGA IV₃, 11.10.7, $A \cdot
B = u(H)$ is geometrically reduced (since $H$ is), so it is a closed subgroup of $G$. Since obviously $A \cdot B \subset
\Gamma_{G}(i_{A}, i_{B})$, the corollary follows. ∎

**Definitions and remarks 7.2.** [^N.D.E-VI_B-71] *(i) Given a $k$-group $G$, a family $(X_{i})_{i \in I}$ of
geometrically reduced $k$-schemes, and for each $i \in I$ a $k$-morphism $f_{i} : X_{i} \to G$, one calls* closed group
subscheme of $G$ generated by the family $(f_{i})_{i \in I}$*, and we shall denote in this number $\Gamma_{G}((f_{i})_{i
\in I})$, the smallest closed group subscheme of $G$ majorizing each of the $f_{i}$. If $X$ is a subscheme of $G$,
geometrically reduced over $k$, and if $f$ is the immersion $X \hookrightarrow G$, one writes $\Gamma_{G}(X)$ instead of
$\Gamma_{G}(f)$.*

*(i′) With the notations of 7.1 (ii), we shall sometimes set $\Gamma'_{G}(f) = \bigcup_{n \geqslant 1} f^{n}(X^{n})$.
Note that $\Gamma'_{G}(f)$ is a subset of $G$ stable for the group law (in the sense of 3.0).*

*(ii) It is clear that if `X_1` and `X_2` are two geometrically reduced $k$-schemes and $f_{1} : X_{1} \to G$ and
$f_{2} : X_{2} \to G$ two $k$-morphisms such that the sets $f_{1}(X_{1})$ and $f_{2}(X_{2})$ are equal, then
$\Gamma_{G}(f_{1}) = \Gamma_{G}(f_{2})$.*

<!-- original page 382 -->

*(iii) Let $E$ be a subset of $G$ such that the reduced subscheme $E$ of $G$ is geometrically reduced. One calls* closed
group subscheme of $G$ generated by $E$*, denoted $\Gamma_{G}(E)$, the group subscheme $\Gamma_{G}(i)$, where $i$ is the
injection of the reduced subscheme $E$ of $G$ into $G$.*

*(iv) Since every group subscheme of $G$ is closed, by VI_A, 0.5.2,*[^N.D.E-VI_B-72] *one will speak of "generated group
subscheme" instead of "generated closed group subscheme".*

*(v) Let $X$ be a geometrically reduced $k$-scheme and $f : X \to G$ a $k$-morphism. Suppose that $f(X)$ contains the
unit element $e$ of $G$. Set $X'^{1} = X \times_{k} X$ and $f'^{1} = \mu \circ (f \times_{k} (c \circ f))$, and for $n >
1$,*

```text
X′^n = X′¹ ×_k X′^{n−1}    and    f′^n = μ ∘ (f′¹ ×_k f′^{n−1}).
```

*Then $\Gamma_{G}(f)$ is the reduced subscheme of $G$ whose underlying space is the closure of the union of the
$f'^{n}(X'^{n})$, for $n \geqslant 1$.*

Indeed, recalling the notation of 7.1 (ii): $X^{1} = X \sqcup X$ and $X^{n} = X^{1} \times_{k} X^{n-1}$, for $n
\geqslant 2$, one has the following inclusions, where the first follows from the hypothesis $e \in f(X)$:

```text
f^n(X^n) ⊂ f′^n(X′^n) ⊂ f^{2n}(X^{2n}),    for every n ⩾ 1.
```

This shows moreover that, for there to exist an integer $n$ such that $f^{n}(X^{n}) = \Gamma_{G}(f)$, it is necessary
and sufficient that there exist an integer $m$ such that $f'^{m}(X'^{m}) = \Gamma_{G}(f)$.

From Remark 7.2 (v) one deduces the

<!-- label: III.VI_B.7.2 -->

**Corollary 7.2.1.** *Let $X$ be a geometrically reduced and geometrically connected $k$-scheme, and $f : X \to G$ a
$k$-morphism such that $f(X)$ contains the neutral element of $G$. Then the $k$-group $\Gamma_{G}(f)$ is connected,
hence irreducible.*

<!-- label: III.VI_B.7.2.1 -->

Indeed, each of the $X'^{n}$ is then connected, hence the union of the $f'^{n}(X'^{n})$ (which all contain the neutral
element) is connected, and the same is true of its closure $\Gamma_{G}(f)$. Hence $\Gamma_{G}(f)$ is irreducible, by
VI_A, 2.4 (when $G$, hence also $\Gamma_{G}(f)$, is locally of finite type over $k$) and 2.6.5 (iii) (in the general
case). ∎

**Definition 7.2.2.** *Let $G$ be a $k$-group.*

*a) Let $A$ and $B$ be two geometrically reduced group sub-$k$-schemes of $G$. The* commutator group subscheme of $A$
and $B$ in $G$*, denoted $(A, B)_{G}$ or simply $(A, B)$, is the closed group subscheme of $G$ generated by the morphism
$\nu : A \times_{k} B \to G$ defined by: $(a, b) \mapsto aba^{-1}b^{-1}$, for every $k$-scheme $S$ and $a \in A(S)$, $b
\in B(S)$.*

*b) Suppose $G$ geometrically reduced over $k$. The* derived group of $G$*, denoted $D(G)$,*[^N.D.E-VI_B-73] *is the
group $(G, G)$.*

*N.B. For $G$ to be commutative, it is necessary and sufficient that $D(G)$ be the unit $k$-group.*

<!-- label: III.VI_B.7.2.2 -->

<!-- original page 383 -->

**Reminders 7.3.0.** [^N.D.E-VI_B-74] *Recall that if $\phi : Y \to Z$ is a morphism of $S$-schemes, the image presheaf
$\phi(Y)$ is the $S$-functor which to every $S'$ over $S$ associates the subset $\phi(Y(S'))$ of $Z(S')$. Note that if
$T$ is a subscheme of $Z$ and if the inclusion of presheaves $\phi(Y) \hookrightarrow Z$ factors through $T$, i.e. if
$\phi \circ h \in T(S')$ for every $S$-morphism $h : S' \to Y$, then set-theoretically $\phi(Y) \subset T$ (take $h =
id_{Y}$), and the converse is true if $Y$ is reduced, since in this case $\phi$ factors through $T$.*

*Recall also that, by 6.2, if $H$ is a closed group sub-$k$-scheme of $G$, then $Centr_{G} H$ and $Norm_{G} H$ are
representable by closed group sub-$k$-schemes of $G$.*

<!-- label: III.VI_B.7.3.0 -->

**Corollary 7.3.** *Let $G$ be a $k$-group, $X$ a geometrically reduced $k$-scheme, $f : X \to G$ a $k$-morphism.*

*(i) Let $S$ be a $k$-scheme and $u$ an endomorphism of the $S$-group `G_S`.*

*(a) If one has $u(f_{S}(X_{S})) \subset \Gamma_{G}(f)_{S}$ (set-theoretically), then the morphism $u :
\Gamma_{G}(f)_{S} \to G_{S}$ factors through $\Gamma_{G}(f)_{S}$.*

*(b) If $u$ is an automorphism of the $S$-group `G_S` and if one has $u(f_{S}(X_{S})) = f_{S}(X_{S})$
(set-theoretically), then $u$ induces an automorphism of $\Gamma_{G}(f)_{S}$. In particular, if an element $g \in G(S)$
satisfies $int(g)(f_{S}(X_{S})) = f_{S}(X_{S})$ (set-theoretically), then $g \in Norm_{G_{S}}(\Gamma_{G}(f)_{S})(S)$.*

*(c) If $u \circ f_{S} = f_{S}$, then the restriction of $u$ to the subgroup $\Gamma_{G}(f)_{S}$ of `G_S` is the
identity. In particular, if an element $g \in G(S)$ satisfies $int(g)(f_{S}) = f_{S}$, then $g \in
Centr_{G_{S}}(\Gamma_{G}(f)_{S})(S)$.*

*(ii) Let $H$ be a group subscheme of $G$; then $H$ centralizes (resp. normalizes) $\Gamma_{G}(f)$ if and only if, for
every $S \to \operatorname{Spec} k$ and $h \in H(S)$, one has $int(h) \circ f_{S} = f_{S}$ (resp. $int(h)(f_{S}(X_{S}))
\subset \Gamma_{G}(f)_{S}$), i.e. if for every $S' \to S$ and $x \in X(S')$, the elements $h_{S'}$ and $f(x)$ of $G(S')$
commute (resp. $h_{S'} f(x) h^{-1}_{S'} \in \Gamma_{G}(f)(S')$).*

*(iii) In particular, let $Y$ be a second geometrically reduced $k$-scheme and $\phi : Y \to G$ a $k$-morphism. Suppose
that, whatever the $k$-scheme $S'$, for every $x \in X(S')$ and $y \in Y(S')$, the elements $\phi(y)$ and $f(x)$ of
$G(S')$ commute (resp. $int(\phi(y))(f(x)) \in \Gamma_{G}(f)(S')$).*

*Then $\Gamma_{G}(\phi)$ is a sub-$k$-group of $Centr_{G} \Gamma_{G}(f)$, resp. $Norm_{G} \Gamma_{G}(f)$.*

*(iv) If $g$ is a $k$-point of $G$, then the $k$-group $\Gamma_{G}({g})$ is commutative.*

*(v) Let $A$ and $B$ be two group subschemes of $G$ geometrically reduced over $k$. If $A$ and $B$ are invariant (resp.
characteristic), so is $(A, B)$.*

<!-- label: III.VI_B.7.3 -->

*Proof.* (i) Let us prove (a). Set $\Gamma_{S} = \Gamma_{G}(f)_{S}$. Then $u^{-1}(\Gamma_{S})$ is a closed group
sub-$S$-scheme of `G_S`, hence, by 7.1 (iii), it suffices to show that $f_{S}$ factors through $u^{-1}(\Gamma_{S})$.
Now, since $u(f_{S}(X_{S})) \subset \Gamma_{S}$ and since `X_S` is reduced, $u \circ f_{S}$ factors through
$\Gamma_{S}$, hence $f_{S}$ factors through $u^{-1}(\Gamma_{S})$. This proves (a).

<!-- original page 384 -->

Then the first assertion of (b) is a consequence of (a), applied to $u$ and $u^{-1}$ (and in fact it suffices to assume
that $u(f_{S}(X_{S})) \subset \Gamma_{S}$ and $u^{-1}(f_{S}(X_{S})) \subset \Gamma_{S}$), and the second assertion is
the particular case where $u = int(g)$.

Let us prove (c). Consider the morphism of $S$-groups $G_{S} \to G_{S} \times_{S} G_{S}$, $g \mapsto (u(g), g)$ and let
$H$ be the inverse image of the diagonal; it is a group subscheme of `G_S`. Since $G$ is separated over $k$ (VI_A 0.3),
`G_S` is separated over $S$, hence $H$ is closed in `G_S`. As, by hypothesis, $H$ majorizes $f_{S}$, it contains
$\Gamma_{G}(f)_{S}$, by 7.1 (iii). This proves the first assertion of (c), and the second is the particular case where
$u = int(g)$.

Let us prove (ii). Set $\Gamma = \Gamma_{G}(f)$ and let $i$ denote the inclusion $\Gamma \hookrightarrow G$. Then $H$ is
contained in $N = Norm_{G}(\Gamma)$ if and only if, for every $k$-scheme $S$ and $h \in H(S)$, one has
$int(h)(\Gamma_{S}) \subset \Gamma_{S}$ (this condition applied to $h$ and $h^{-1}$ entailing that $int(h)(\Gamma_{S}) =
\Gamma_{S}$); and by (i)(a) this is the case if and only if $int(h)(f_{S}(X_{S})) \subset \Gamma_{S}$.

Similarly, $H$ is contained in $C = Centr_{G}(\Gamma)$ if and only if, for every $k$-scheme $S$ and $h \in H(S)$, one
has $int(h) \circ i_{S} = i_{S}$, and by (i)(c) this is the case if and only if $int(h)(f_{S}) = f_{S}$. This proves
(ii).

Let us prove (iii). Taking (ii) into account, the hypothesis entails that $\phi$ factors through $C$ (resp. $N$); since
the latter is a closed subgroup of $G$, by 6.2, it therefore contains $\Gamma_{G}(f)$, by 7.1 (i).

Assertion (iv) follows from (iii), when one takes for $f$ and $\phi$ the closed immersion $\operatorname{Spec} k
\hookrightarrow G$ defined by $g$: in this case, for every $k$-scheme $S$, $X(S)$ and $Y(S)$ have only one point, which
is sent by $f$ (resp. $\phi$) to $g$.

Let us finally show (v). Let $\nu$ be the morphism $G \times G \to G$, $(g, h) \mapsto ghg^{-1}h^{-1}$ and let $\nu'$ be
its restriction to $A \times B$; by definition (7.2.2), $(A, B) = \Gamma_{G}(\nu')$. Let $S$ be a $k$-scheme, and $u$ an
inner automorphism (resp. an automorphism of $S$-group) of `G_S`. One has $u \circ \nu_{S} = \nu_{S} \circ (u \times
u)$. On the other hand, the hypothesis entails that $u$ induces an automorphism $u_{1}$ of `A_S` (resp. $u_{2}$ of
`B_S`), hence

```text
u(ν′_S(A_S ×_S B_S)) = ν′_S(u_1(A_S) ×_S u_2(B_S)) = ν′_S(A_S ×_S B_S).
```

Hence, by (i)(b), $u$ induces an automorphism of $(A, B)_{S}$. This proves (v). ∎

**Proposition 7.4.** *Let $G$ be a $k$-group locally of finite type, $X$ a $k$-scheme of finite type, geometrically
reduced and geometrically connected, and $f : X \to G$ a $k$-morphism such that $f(X)$ contains the neutral element $e$
of $G$. Then, with the notations of 7.1 (ii), there exists an integer $N$ such that one has (set-theoretically):*

$$ f^{N}(X^{N}) = \Gamma_{G}(f). $$

<!-- label: III.VI_B.7.4 -->

By 7.1 (iii) and EGA IV₂, 2.6.1, we may suppose $k$ algebraically closed. By Corollary 7.2.1, we may suppose $G =
G^{0}$; finally, it suffices to show that there exists an integer $N$ such that one has $f'^{N}(X'^{N}) =
\Gamma_{G}(f)$, with the notations of 7.2 (v).

*First case.* Suppose $X$ irreducible. Then the $f'^{n}(X'^{n})$ form an increasing sequence of irreducible closed sets
in the space $G$, which is noetherian, since $G = G^{0}$ is

<!-- original page 385 -->

of finite type over $k$ (VI_A 2.4). Hence this sequence is stationary, and there exists an integer $m$ such that
$f'^{m}(X'^{m}) = \Gamma_{G}(f)$.

Moreover, since $X$ and $G$ are of finite type over $k$, the morphisms $f'^{n}$ are of finite type over $k$.
Consequently, $f'^{m}(X'^{m})$ is constructible in $G$ (EGA IV₁, 1.8.5), hence contains an open $U$ of its closure
$\Gamma_{G}(f)$ (EGA 0_IV, 9.2.3). Then, by VI_A 0.5, one has:

```text
Γ_G(f) ⊂ U · U ⊂ f′^{2m}(X′^{2m}) ⊂ Γ_G(f),
```

whence $f'^{2m}(X'^{2m}) = \Gamma_{G}(f)$.

*Second case.* Suppose $X$ has exactly two irreducible components `A_1` and `A_2`. Then, since $X$ is connected and $k$
algebraically closed, there exists $a \in (A_{1} \cap A_{2})(k)$. Hence the four irreducible parts $A_{i} \times_{k}
A_{j}$ ($i, j = 1, 2$) cover $X \times_{k} X$, and the image of each of them under the morphism $f'^{1} = \mu \circ (f
\times_{k} (c \circ f))$ contains $e$. If $f'^{1}_{ij}$ denotes the restriction of $f'^{1}$ to the reduced subscheme
$A_{i} \times_{k} A_{j}$, set

```text
Y = (A_1 ×_k A_1) ×_k (A_1 ×_k A_2) ×_k (A_2 ×_k A_2) ×_k (A_2 ×_k A_1)    and
g = μ ∘ (μ ∘ (f′¹_{11} ×_k f′¹_{12}) ×_k μ ∘ (f′¹_{22} ×_k f′¹_{21})).
```

Then $Y$ is irreducible, reduced and of finite type, hence we just saw that there exists an integer $m$ such that
$g'^{m}(Y'^{m}) = \Gamma_{G}(g)$. Now, for every $n \geqslant 1$, one has $f'^{n}(X'^{n}) \subset g'^{n}(Y^{n}) \subset
f'^{4n}(X'^{4n})$, whence $\Gamma_{G}(f) = \Gamma_{G}(g)$ and $f'^{4m}(X'^{4m}) = \Gamma_{G}(f)$.

*General case.* Let us argue by induction on the number of irreducible components of $X$ (this number is finite since
$X$, being of finite type over $k$, is noetherian). Suppose the proposition proved in the case where $X$ has at most
$r - 1$ irreducible components, and suppose it has $r$, namely $A_{1}, \cdots, A_{r}$. Then $e$ belongs to the image of
one of the $A_{i}$; suppose for example that $e \in f(A_{1})$. Set then $Y = \Gamma_{G}(f_{r})$, where $f_{r}$ denotes
the restriction of $f$ to the reduced subscheme $X_{r} = A_{1} \cup \cdots \cup A_{r-1}$ (we suppose the numbering of
the $A_{i}$ chosen so that this scheme is connected, which is always possible). Then $Y$ is a subgroup of $G$, closed,
reduced and irreducible, by Corollary 7.2.1.

Set $Z = f(A_{r})$, and let $T = Y \cup Z$, equipped with the closed reduced subscheme structure, and $i$ the injection
of $T$ into $G$. It is clear (7.2 (ii)) that $\Gamma_{G}(i) = \Gamma_{G}(f)$ and that $T$ is connected (because since
$X$ is connected, $A_{1} \cup \cdots \cup A_{r-1}$ and $A_{r}$ have in common a point $a$, and $Y$ and $Z$ have in
common the point $f(a)$). Moreover, $e \in T$, and $T$ has at most two irreducible components, since $Y$ and $Z$ are
irreducible. By the induction hypothesis, there exists an integer $m$ such that one has $f'^{m}_{r}(X'^{m}_{r}) =
\Gamma_{G}(f_{r}) = Y$. Since $X = X_{r} \cup A_{r}$ and since $Z = f(A_{r})$ is contained in $f'^{m}(X'^{m})$ (since $e
\in f(A_{1})$), one therefore has:

```text
f(X) ⊂ Y ∪ Z ⊂ f′^m(X′^m).
```

On the other hand, since $T$ has at most two irreducible components, one has already seen that there exists an integer
$p$ such that $i'^{p}(T'^{p}) = \Gamma_{G}(i) = \Gamma_{G}(f)$. Now, $T \subset f'^{m}(X'^{m})$, hence $f'^{mp}(X'^{mp})
= \Gamma_{G}(f)$, and one shows, as in the first case, that this last equality entails $f'^{2mp}(X'^{2mp}) =
\Gamma_{G}(f)$. ∎

<!-- original page 386 -->

**Lemma 7.5.** *Let $S$ be a scheme, $G$ an $S$-group scheme, $X$ an $S$-prescheme, $f : X \to G$ an $S$-morphism.
Suppose that $X$ and $G$ are locally of finite presentation over $S$, and that for every $s \in S$ and every maximal
point $g$ of $G_{s}$, there exists a point $x$ of $X$ such that $f(x) = g$ and $f$ is flat at $x$. Then the morphism
$\mu \circ (f \times_{S} f) : X \times_{S} X \to G$ is covering for the (fppf) topology.*

<!-- label: III.VI_B.7.5 -->

[^N.D.E-VI_B-75] By EGA IV₃, 11.3.1, the set $V$ of points of $X$ at which $f$ is flat is open and $f|_{V}$ is an open
morphism, hence $U = f(V)$ is an open of $G$; moreover, by the hypothesis, $U \cap G_{s}$ is dense in $G_{s}$, for every
$s \in S$. Denote by $\phi$ the restriction to $V \times_{S} V$ of $\mu \circ (f \times_{S} f)$.

It suffices to show that $\phi$ is covering for the (fppf) topology, and for this it suffices to show that $\phi$ is
faithfully flat and of finite presentation (cf. IV, 6.3.1 (iv)). Now $\phi$ is equal to the composite $V \times_{S} V
-\to U \times_{S} U -\to G$, where the first morphism is faithfully flat and locally of finite presentation, since
$f|_{V}$ is. It therefore suffices to prove that the same is true of the restriction of $\mu$ to $U \times_{S} U$.

Now, $G \to S$ being locally of finite presentation and flat, the same is true of $\mu : G \times_{S} G \to G$ (which is
isomorphic to the morphism deduced from $G \to S$ by the base change $G \to S$, cf. VI_A 0.1), hence also of the induced
morphism $U \times_{S} U \to G$. To prove that the latter is surjective, it suffices to look fiber by fiber, where it
follows from VI_A 0.5, since $U \cap G_{s}$ is a dense open of $G_{s}$, for every $s \in S$. ∎

**Remark 7.6.0.** [^N.D.E-VI_B-76] *Let $S$ be a scheme, $H$ an $S$-group, and $f : X \to H$ a morphism of $S$-schemes.
The sub-presheaf in groups of $H$ generated by the image of $f$, denoted $\langle Im f\rangle$, is the sub-$S$-functor
in groups of $H$ which to every $S$-scheme $S'$ associates the subgroup of $H(S')$ generated by $f(X(S'))$. Since each
element of this subgroup can be written as a finite product $f(x_{1})^{\epsilon_{1}} \cdots f(x_{n})^{\epsilon_{n}}$,
with $n \in \mathbb{N}*$, $x_{i} \in X(S')$ and $\epsilon_{i} = \pm 1$, one sees therefore that if one sets $X^{1} = X
\sqcup X$ and defines the morphisms $f^{n} : X^{n} \to H$ as in 7.1, then $\langle Im f\rangle$ is nothing but the image
presheaf of the morphism*

$$ f^{\infty} : X^{\infty} \to H, $$

*where $X^{\infty} = \coprod_{n \geqslant 1} X^{n}$ and $f^{\infty} : X^{\infty} \to H$ is the $S$-morphism whose
restriction to each $X^{n}$ is $f^{n}$.*

<!-- label: III.VI_B.7.6.0 -->

**Proposition 7.6.** [^N.D.E-VI_B-77] *Let $S$ be a scheme, $X$ a flat $S$-scheme locally of finite presentation over
$S$, $H$ an $S$-group, locally of finite presentation over $S$ and with reduced fibers, $f : X \to H$ a morphism of
$S$-schemes, and $f^{\infty} : X^{\infty} \to H$ the $S$-morphism introduced above. The following conditions are
equivalent:*

*(i) $H$ represents the (fppf) $S$-sheaf associated with the presheaf $\langle Im f\rangle$.*

*(ii) $f^{\infty}$ is covering for the (fppf) topology.*

<!-- original page 387 -->

*(iii) $f^{\infty}$ is surjective, i.e. $H = \bigcup_{n \geqslant 1} f^{n}(X^{n})$.*

*If moreover $H$ is quasi-compact, these conditions are also equivalent to the following:*

*(iv) There exists an integer $n$ such that $f^{n} : X^{n} \to H$ is covering for the (fppf) topology (and a fortiori
surjective).*

*This applies in particular in the case where $X$ is a $k$-scheme locally of finite type and geometrically reduced, $G$
a $k$-group locally of finite type, $\phi : X \to G$ a morphism of $k$-schemes, $H = \Gamma_{G}(\phi)$, and $f : X \to
H$ the morphism induced by $\phi$.*

<!-- label: III.VI_B.7.6 -->

*Proof.* The sheaf considered in (i) is the image sheaf of $X^{\infty}$ by $f^{\infty}$, hence, by IV 4.4.3, to say that
$H$ represents this sheaf is equivalent to saying that $f^{\infty}$ is covering, and this implies that $f^{\infty}$ is
surjective. Conversely, suppose $f^{\infty}$ surjective and let us show that it is then covering for the (fppf)
topology.

Let $s \in S$, $\eta$ a maximal point of the fiber $H_{s}$, and $x \in X^{\infty}_{s}$ such that $f^{\infty}(x) = \eta$
(such an $x$ exists, since $f^{\infty}$ is surjective). Since the fiber $H_{s}$ is reduced, $\mathcal{O}_{H_{s}, \eta}$
is a field, hence $f^{\infty}_{s}$ is flat at the point $x$. Since $X^{\infty}$ and $H$ are locally of finite
presentation over $S$, and $X^{\infty}$ flat over $S$, it follows from the fibrewise flatness criterion (EGA IV₃,
11.3.10) that $f^{\infty}$ is flat at the point $x$. Hence, by Lemma 7.5, the morphism

```text
μ ∘ (f^∞ × f^∞) : X^∞ ×_S X^∞ → H
```

is covering for the (fppf) topology. Now, since $X^{n} \times_{S} X^{m}$ is canonically isomorphic to $X^{n+m}$, and
that, under this isomorphism, $\mu \circ (f^{n} \times_{S} f^{m})$ corresponds to $f^{n+m}$, it is clear that $\mu \circ
(f^{\infty} \times_{S} f^{\infty})$ factors through $f^{\infty}$, so that $f^{\infty}$ is covering for the (fppf)
topology. This proves that (iii) ⇒ (ii), whence the equivalence of conditions (i), (ii) and (iii).

Note moreover that, since the morphisms $X \to S$ and $H \to S$ are locally of finite presentation, the same is true of
$f : X \to H$ (cf. EGA IV₁, 1.4.3 (v)), and as $\mu : H \times_{S} H$ is also of finite presentation (cf. VI_A, 0.1), it
follows that each $f^{n} : X^{n} \to H$ is so. Hence, by EGA IV₁, 1.9.5 (viii), the $f^{n}(X^{n})$ are ind-constructible
parts of $H$.

Suppose moreover $H$ quasi-compact (then $S$ is also, since $H \to S$ is surjective). Then, by EGA IV₁, 1.9.9, one
concludes that there exists $p$ such that $f^{p}(X^{p}) = H$. As before, one then deduces, from the fact that the fibers
of $H$ are reduced and from Lemma 7.5, that the morphism $\mu \circ (f^{p} \times_{S} f^{p}) : X^{p} \times_{S} X^{p}
\to H$ is covering for the (fppf) topology; since this morphism equals $f^{2p} : X^{2p} \to H$, this concludes the proof
of 7.6. ∎

**Remark 7.6.1.** *Obviously, the equivalent conditions of 7.6 imply that the sheaf $F$ considered is representable. The
converse is false in general:*[^N.D.E-VI_B-78] *for example, if $k$ is of characteristic 0, let $G = G_{a,k}$ and let
$f : \operatorname{Spec} k \to G$ be the morphism given by the point `1` of $G(k)$; then $F$ is represented by the
constant $k$-group $\mathbb{Z}_{k}$, while $\Gamma_{G}(f) = G$, hence the monomorphism
$\mathbb{Z}_{k} \hookrightarrow G$ is not surjective.*

*Let us place ourselves, for simplicity, under the hypotheses of the particular case of 7.6, and suppose $F$
representable. Then, by EGA IV₃, 8.14.2, $F$ is locally*

<!-- original page 388 -->

*of finite presentation over $k$, hence the question is whether the dominant monomorphism $F \to \Gamma_{G}(f)$ is an
isomorphism, or equivalently, a closed immersion. This will be the case, by virtue of 1.4.2, if $F$ is quasi-compact,
and, by VI_A, 0.5.1, this will be verified if $F$ is connected, hence, in particular (7.2.1), if $X$ is connected and if
$f(X)$ contains the unit element of $G$.*

<!-- label: III.VI_B.7.6.1 -->

**Lemma 7.7.** *Let $k$ be an algebraically closed field, $G$ a $k$-group locally of finite type, $X$ a geometrically
reduced and locally of finite type $k$-scheme, $f : X \to G$ a $k$-morphism and $H$ a group subscheme of $G$ such that
$H \subset f(X)$. Set*

```text
Γ′ = ⋃_{n ⩾ 1} f^n(X^n),    Γ′_0 = Γ′ ∩ G(k),    H_0 = H(k)
```

*and assume `H_0` is of finite index in $\Gamma'_{0}$. Then there exists an integer $m$ such that $f^{m}(X^{m}) =
\Gamma_{G}(f)$ (cf. 7.6), and $\Gamma_{G}(f)$ is the union of finitely many translates of $H$.*

<!-- label: III.VI_B.7.7 -->

For every $n \geqslant 1$, $f^{n}(X^{n})$ is an ind-constructible part of $G$ (EGA IV₁, 1.9.5 (viii)), the same is
therefore true of $\Gamma'$, so that, since $G$ is a Jacobson scheme, $\Gamma'_{0}$ is dense in $\Gamma'$. By
hypothesis, there exists a finite sequence $a_{1}, \cdots, a_{r}$ of points of $\Gamma'_{0}$ such that $\Gamma'_{0} =
a_{1} H_{0} \cup \cdots \cup a_{r} H_{0}$, whence

```text
Γ_G(f) = Γ′ = Γ′_0 = a_1 H_0 ∪ … ∪ a_r H_0 = a_1 H_0 ∪ … ∪ a_r H_0 = a_1 H ∪ … ∪ a_r H,
```

the last equality resulting from the fact that translation by $a_{i}$ is a homeomorphism of $G$ onto $G$. One has
therefore $\Gamma_{G}(f) = a_{1} H \cup \cdots \cup a_{r} H$. On the other hand, it is clear that there exists an
integer $p$ such that each of the $a_{i}$ ($1 \leqslant i \leqslant r$) belongs to $f^{p}(X^{p})$. Finally, since $H
\subset f(X)$, one has, for every $i$: $a_{i} H \subset f^{p+1}(X^{p+1})$, so that $f^{p+1}(X^{p+1}) = \Gamma_{G}(f)$. ∎

**Proposition 7.8.** *Let $G$ be a $k$-group locally of finite type, $A$ and $B$ two geometrically reduced group
sub-$k$-schemes (hence smooth at the generic points of their irreducible components, hence smooth by 1.3) of $G$.
Suppose one of the following conditions a) or b) is satisfied:*

*a) $A$ and $B$ are invariant and of finite type over $k$.*

*b) $A$ is connected and $B$ is of finite type over $k$.*

*Then $(A, B)$ is of finite type over $k$, and represents the sheaf associated for the (fppf) topology (or (fpqc)) with
the presheaf in groups of commutators of $A$ and $B$ in $G$. Moreover,*[^N.D.E-VI_B-79] *the $k$-groups $(A, B^{0})$ and
$(A^{0}, B)$ are connected, and one has*

```text
(A, B)⁰ = (A, B⁰) · (A⁰, B).
```

<!-- label: III.VI_B.7.8 -->

*Proof.* By 7.6, to show that $(A, B)$ is the desired associated sheaf, it suffices to show that there exists an integer
$n$ such that $\nu^{n}((A \times_{k} B)^{n}) = (A, B)$ (notations of 7.2.2). To show this, as well as to show the two
other assertions, we may suppose

<!-- original page 389 -->

$k$ algebraically closed. Indeed, let $\bar{k}$ be an algebraic closure of $k$. By 7.1 (iii) and VI_A 2.4, one has, with
obvious notations:

```text
(A, B)_{k̄} = (A_{k̄}, B_{k̄}),    ((A, B)⁰)_{k̄} = (A_{k̄}, B_{k̄})⁰,    (A, B⁰)_{k̄} = (A_{k̄}, B⁰_{k̄}),    etc.
```

Consequently, if one shows that $(A_{\bar{k}}, B_{\bar{k}})$ is of finite type over $\bar{k}$ (resp. that $(A_{\bar{k}},
B^{0}_{\bar{k}})$ and $(A^{0}_{\bar{k}}, B_{\bar{k}})$ are connected, and that the morphism $(A_{\bar{k}},
B^{0}_{\bar{k}}) \times_{\bar{k}} (A_{\bar{k}}, B^{0}_{\bar{k}}) \to (A_{\bar{k}}, B_{\bar{k}})^{0}$ is surjective),
then the analogous assertions will be true over $k$, by EGA IV₂, 2.7.1 and 2.6.1.

Let then $B_{1}, \cdots, B_{p}$ be the connected components of $B$ other than the neutral component $B^{0}$ (these are
finite in number since $B$ is supposed of finite type over $k$, hence noetherian), and in case (a), let similarly
$A_{1}, \cdots, A_{q}$ be those of $A$. (In case (b), one will consider only $A^{0} = A$). Let $\nu_{ij}$ be the
restriction of $\nu$ to $A_{i} \times_{k} B_{j}$. Then each of the $A_{i}$ and $B_{j}$ is irreducible (VI_A 2.4.1), so
the same is true of $A^{0} \times_{k} B_{j}$ and $A_{i} \times_{k} B^{0}$. Since the neutral element of $G$ belongs to
$A^{0}$ and $B^{0}$, it belongs to $\nu_{0j}(A^{0} \times_{k} B_{j})$ and to $\nu_{i0}(A_{i} \times_{k} B^{0})$. Then
each of the $\Gamma_{G}(\nu_{0j})$ and $\Gamma_{G}(\nu_{i0})$ is connected (7.2.1). Similarly, if $u_{0j}$ (resp.
$u_{i0}$) denotes the injection of $\Gamma_{G}(\nu_{0j})$ (resp. $\Gamma_{G}(\nu_{i0})$) into $G$, then

```text
(A⁰, B) = Γ_G((u_{0j})_{j=0}^p)    and    (A, B⁰) = Γ_G((u_{i0})_{i=0}^q)
```

are connected. Moreover, one easily deduces from 7.4 and the preceding constructions that there exists an index $r$ such
that $(A^{0}, B)$ and $(A, B^{0})$ are included in $\nu^{r}((A \times_{k} B)^{r})$. In case b), one has $(A, B) =
(A^{0}, B)$, and we are done.

Let us now place ourselves in case (a).[^N.D.E-VI_B-80] We already know that $(A^{0}, B)$ and $(A, B^{0})$ are smooth
and connected sub-$k$-groups of $G$, hence of finite type (cf. VI_A, 2.4). On the other hand, since $A^{0}$ is a
characteristic subgroup of $A$ (cf. VI_A, 2.6.5), it is an invariant subgroup of $G$ and hence, by 7.3 (v), $(A^{0}, B)$
is an invariant subgroup of $G$, and similarly for $(A, B^{0})$. Hence, by 7.1.1, the subgroup $H$ of $G$ generated by
$(A, B^{0})$ and $(A^{0}, B)$ is none other than $(A, B^{0}) \cdot (A^{0}, B)$. In particular, one has therefore $H
\subset \nu^{2r}((A \times_{k} B)^{2r})$.

Given a part $X$ of $G$ stable for the group law (cf. 3.0), we shall denote by `X_0` the group of $k$-points of $G$
belonging to $X$. Set $\Gamma' = \bigcup_{q \geqslant 1} \nu^{q}((A \times_{k} B)^{q})$. Then, by Proposition 7.9 below,
one has:

```text
(A⁰, B)_0 = (A⁰_0, B_0),    (A, B⁰)_0 = (A_0, B⁰_0)    and    Γ′_0 = (A_0, B_0),
```

so that $H_{0} = (A^{0}_{0}, B_{0}) \cdot (A_{0}, B^{0}_{0})$ is of finite index in $\Gamma'_{0}$ (Bible, Exp. 3,
Appendix) since $A^{0}$ and $B^{0}$ are invariant, and $A^{0}_{0}$ (resp. $B^{0}_{0}$) is of finite index in `A_0`
(resp. `B_0`). We are then in the conditions of Lemma 7.7: since $H \subset \nu^{2r}((A \times_{k} B)^{2r})$, there
exists an integer $m$ such that $\nu^{2rm}((A \times_{k} B)^{2rm}) = (A, B)$, and there exists a finite sequence $a_{1},
\cdots, a_{n}$ of $k$-points of $G$ such that: $(A, B) = a_{1} H \cup \cdots \cup a_{n} H$. Then, since $H$ is of finite
type over $k$, each of the $a_{i} H$ is quasi-compact, hence their union $(A, B)$ is quasi-compact, hence of finite type
over $k$. Since $H$ is irreducible, the same is true of each of the $a_{i} H$, and since $e \in H$, it is clear that $H
= (A, B)^{0}$. ∎

<!-- original page 390 -->

**Proposition 7.9.** *Let $k$ be an algebraically closed field, $G$ a $k$-group locally of finite type.*

*(i) Let $A$ and $B$ be two ind-constructible parts of $G$. Denote by `A_0` the set of rational points of $G$ belonging
to $A$. Then $(A \cdot B)_{0} = A_{0} \cdot B_{0}$, the second product being taken in the group $G(k)$.*

*(ii) Let $X$ be a geometrically reduced and locally of finite type $k$-scheme, and $f : X \to G$ a $k$-morphism. Set
$\Gamma'_{G}(f) = \bigcup_{n \geqslant 1} f^{n}(X^{n})$. Then $\Gamma'_{G}(f)_{0}$ is the subgroup of $G(k)$ generated
by $f(X)_{0}$.*

*(iii) In particular, let $A$ and $B$ be two smooth group subschemes of $G$; set $\Gamma' = \bigcup_{n \geqslant 1}
\nu^{n}(A \times_{k} B)^{n}$ (notations of 7.2.2). Then $\Gamma'_{0}$ is the group of commutators of $A(k)$ and $B(k)$
in $G(k)$.*

<!-- label: III.VI_B.7.9 -->

Let us prove (i). It is clear that $A_{0} \cdot B_{0} \subset (A \cdot B)_{0}$. Conversely, let $z \in (A \cdot B)_{0}$.
Then $\mu^{-1}(z)$ is a closed subset of $G \times_{k} G$, and $A \times_{k} B$ (cf. 3.0) is an ind-constructible part
of $G \times_{k} G$, so that $\mu^{-1}(z) \cap (A \times_{k} B)$ is a non-empty ind-constructible part of $G \times_{k}
G$; by EGA IV₃, 10.4.8, it therefore contains a rational point of $G \times_{k} G$, whose projections $x$ and $y$ are
rational points of $G$ such that $x \in A$, $y \in B$ and $x \cdot y = z$, so that $(A \cdot B)_{0} = A_{0} \cdot
B_{0}$.

To prove (ii), note that, $f^{n}$ being locally of finite type, $f^{n}(X^{n})$ is an ind-constructible part of $G$ (EGA
IV₄, 1.9.5 (viii)). Assertion (i) then allows one to show by induction that, if one sets $A = f(X)_{0}$, one has:
$f^{n}(X^{n})_{0} = (A \cup A^{-1})^{n}$, and consequently,

```text
Γ′_G(f)_0 = ⋃_{n ⩾ 1} f^n(X^n)_0 = ⋃_{n ⩾ 1} (A ∪ A⁻¹)^n,
```

which is the subgroup of $G(k)$ generated by $A = f(X)_{0}$.

Finally, (iii) follows from (ii) and the definitions. ∎

**Corollary 7.10.** *Under the conditions of 7.8, if $k$ is algebraically closed, then `(A, B)(k)` is the commutator
subgroup of $A(k)$ and $B(k)$ in $G(k)$.*

<!-- label: III.VI_B.7.10 -->

Indeed, it suffices to apply 7.9 (iii), 7.8 and 7.6.

## 8. Solvable or nilpotent group schemes

<!-- label: III.VI_B.8 -->

### 8.1.

Let $\mathcal{C}$ be a category equipped with a topology $T$ (cf. IV § 4). For every presheaf $P$ on $\mathcal{C}$, we
denote by $P^{\flat}$ the associated sheaf.

Let $G$ be a presheaf in groups on $\mathcal{C}$, $A$ and $B$ two sub-presheaves in groups of $G$, and let $Comm(A, B)$
be the presheaf in groups of commutators of $A$ and $B$ in $G$; i.e., for every $S \in Ob \mathcal{C}$, $Comm(A, B)(S)$
is the subgroup of $G(S)$ generated by the commutators $aba^{-1}b^{-1}$, with $a \in A(S)$ and $b \in B(S)$. We write

```text
Comm_T(A, B) = Comm(A, B)^♭.
```

In the proof of 8.2, we shall need the following results.[^N.D.E-VI_B-81]

**Lemma 8.1.1.** *Let $A \subset G$ be sheaves in groups, with $A$ invariant in $G$.*

*(i) $Comm_{T}(G, A)$ is the smallest invariant sub-sheaf in groups $C$ of $G$ such that the sheaf $(A/C)^{\flat}$,
associated with the quotient presheaf $A/C$, is central in $(G/C)^{\flat}$.*

*(ii) In particular, $Comm_{T}(G, G)$ is the smallest invariant sub-sheaf in groups $C$ of $G$ such that the quotient
sheaf $(G/C)^{\flat}$ is commutative.*

<!-- label: III.VI_B.8.1.1 -->

Obviously, (ii) is the particular case $A = G$ of (i), so it suffices to show (i). Let $C$ be a sub-sheaf in groups of
$A$, invariant in $G$, and such that the quotient sheaf $(A/C)^{\flat}$ is central in $(G/C)^{\flat}$. By Lemma IV
4.4.8.1, the presheaves $A/C$ and $G/C$ are separated, hence, by IV 4.3.11, all the morphisms in the diagram below are
monomorphisms:

```text
A/C ────→ G/C
 │          │
 ↓          ↓
(A/C)^♭ ─→ (G/C)^♭
```

Since $(A/C)^{\flat}$ is central in $(G/C)^{\flat}$, then $A/C$ is central in $G/C$, whence $Comm(G, A) \subset C$, and
hence $C$ contains $Comm_{T}(G, A)$, by IV 4.3.12.

Conversely, $Comm(G, A)$ is a sub-presheaf in groups of $A$, invariant in $G$, and separated (cf. IV 4.3.1, N.D.E.
(24)), hence, by IV 4.4.8.2 (i) and IV 4.3.11, $C = Comm_{T}(G, A)$ is a sub-sheaf in groups of $A$, invariant in $G$
and containing $Comm(G, A)$. Consequently, the presheaf $A/C$ is central in $G/C$ and hence, by IV 4.4.8.2 (ii),
$(A/C)^{\flat}$ is central in $(G/C)^{\flat}$. This proves Lemma 8.1.1. ∎

**Lemma 8.1.2.** *Let $G$ be a sheaf in groups, `A, B` two sub-presheaves in groups of $G$.*

*(i) The morphism $\tau : Comm(A, B) \to Comm(A^{\flat}, B^{\flat})$ is a covering monomorphism.*

*(ii) Consequently, one has an isomorphism*

```text
Comm_T(A, B) ⥲ Comm_T(A^♭, B^♭).
```

<!-- label: III.VI_B.8.1.2 -->

*Proof.* (i) As $A$ (resp. $B$) is a sub-presheaf of $G$, then $A^{\flat}$ (resp. $B^{\flat}$) is a sub-presheaf of $G$
containing $A$ (resp. $B$), and it follows that $\tau$ is a monomorphism.

Let us show that $\tau$ is covering. Let $S \in Ob \mathcal{C}$ and $g \in Comm(A^{\flat}, B^{\flat})(S)$. Then, there
exists an integer $n \geqslant 1$ and, for $i = 1, \cdots, n$, elements $a'_{i} \in A^{\flat}(S)$, $b'_{i} \in
B^{\flat}(S)$, and $\epsilon_{i} \in {\pm 1}$, such that

```text
g = (a′_1, b′_1)^{ε_1} ⋯ (a′_n, b′_n)^{ε_n},
```

<!-- original page 392 -->

where $(a, b)$ denotes the commutator $aba^{-1}b^{-1}$, and there exists a refinement $R$ of $S$ such that $a'_{i} \in
A(R)$ and $b'_{i} \in B(R)$ for every $i$. Then $g$ is the composite morphism

```text
R ─(a′_1, …, b′_n)→ (A × B)^n ─Φ_{ε_1, …, ε_n}→ Comm(A, B),
```

where $\Phi = \Phi_{\epsilon_{1}, \cdots, \epsilon_{n}}$ is the morphism defined set-theoretically by:

```text
Φ(a_1, b_1, …, a_n, b_n) = (a_1, b_1)^{ε_1} ⋯ (a_n, b_n)^{ε_n},
```

for every $T \in Ob \mathcal{C}$ and $a_{i} \in A(T)$, $b_{i} \in B(T)$. This shows that $g \in Comm(A, B)(R)$ and it
follows, as in the proof of IV 4.3.11 (i), that $Comm(A, B) \to Comm(A^{\flat}, B^{\flat})$ is covering.

As $Comm(A^{\flat}, B^{\flat}) \to Comm(A^{\flat}, B^{\flat})^{\flat}$ is also a covering monomorphism (IV 4.3.11 (iv)),
the same is true of $Comm(A, B) \to Comm(A^{\flat}, B^{\flat})^{\flat}$, hence, by IV 4.3.12, one obtains an
isomorphism:

```text
Comm(A, B)^♭ ⥲ Comm(A^♭, B^♭)^♭.
```

This proves Lemma 8.1.2. ∎

**Proposition 8.2.** *Let $\mathcal{C}$ be a category, $T$ a topology on $\mathcal{C}$, $G$ a sheaf in groups on
$\mathcal{C}$, $n$ an integer $\geqslant 0$. The following conditions are equivalent:*

*(i) If one sets $K_{0} = G$, and for $p \geqslant 1$, $K_{p} = Comm(K_{p-1}, K_{p-1})$ (resp. $K_{p} = Comm(G,
K_{p-1})$), then $K_{n}$ is the unit presheaf in groups.*

*(ii) If one sets $K'_{0} = G$, and for $p \geqslant 1$, $K'_{p} = Comm_{T}(K'_{p-1}, K'_{p-1})$ (resp. $K'_{p} =
Comm_{T}(G, K'_{p-1})$), then $K'_{n}$ is the unit sheaf in groups.*

*(iii) There exists a sequence $G = H_{0} \supset H_{1} \supset \cdots \supset H_{n}$ of invariant sub-sheaves of $G$,
such that, whatever $i$, the quotient sheaf $H_{i}/H_{i+1}$ is commutative (resp. central in $G/H_{i+1}$), and $H_{n}$
is the unit sheaf.*

<!-- label: III.VI_B.8.2 -->

It is clear that $K_{n} \subset K'_{n}$; consequently (ii) entails (i). Let us show that (i) entails (ii). One has
$K'_{1} = Comm_{T}(G, G) = K^{\flat}_{1}$, and one deduces by induction from Lemma 8.1.2 that $K'_{p} = K^{\flat}_{p}$
for every $p$. Consequently, if $K_{n}$ is the unit presheaf, then $K'_{n} = K^{\flat}_{n}$ is the unit sheaf.

Finally, conditions (ii) and (iii) are equivalent by Lemma 8.1.1. ∎

**Definition 8.2.1.** *When these conditions are satisfied, the sheaf $G$ is said to be* solvable of class $n$ *(resp.*
nilpotent of class $n$*). When there exists an integer $n$ such that these conditions are satisfied, one says that $G$
is* solvable *(resp.* nilpotent\*).\*

*Note that, by condition (i), this does not depend on the topology $T$.*

<!-- label: III.VI_B.8.2.1 -->

**Proposition 8.3.** *Let $k$ be a field, $S$ a non-empty $k$-scheme, $\Omega$ an algebraically closed extension of $k$,
$G$ a smooth $k$-group of finite type. The following conditions are equivalent:*

*(i) $G$ is solvable of class $n$ (resp. nilpotent of class $n$).*

*(ii) $G \times_{k} S$ is solvable of class $n$ (resp. nilpotent of class $n$).*

*(iii) The group $G(\Omega)$ is solvable of class $n$ (resp. nilpotent of class $n$).*

<!-- original page 393 -->

*(iv) If one sets $K_{0} = G$ and considers, for $p \geqslant 1$, the $k$-groups $K_{p} = (K_{p-1}, K_{p-1})$ (resp.
$K_{p} = (G, K_{p-1})$) (cf. 7.2.2), then $K_{n}$ is the unit $k$-group.*

<!-- label: III.VI_B.8.3 -->

The equivalence of conditions (i) and (ii) follows from Proposition 8.2, given that the formation of the presheaf in
groups of commutators commutes with base change (IV 4.1.3).

The equivalence of (i) and (iv) follows from the fact that, by 7.8, the $k$-group $K_{p} = (K_{p-1}, K_{p-1})$ (resp.
$K_{p} = (G, K_{p-1})$) represents the sheaf $Comm_{T}(K_{p-1}, K_{p-1})$ (resp. $Comm_{T}(G, K_{p-1})$), where $T$ is
the (fppf) (or (fpqc)) topology.

To show that conditions (iii) and (iv) are equivalent, one may suppose $k = \Omega$, and then the equivalence of
conditions (iii) and (iv) follows from 7.10. ∎

**Proposition 8.4.** *Let $G$ be an $S$-group of finite presentation, such that for every $s \in S$, $G_{s}$ is smooth
over $\kappa(s)$. Let $T$ be the set of $s \in S$ such that $G_{s}$ is solvable (resp. nilpotent).*

*(i) Then $T$ is locally constructible in $S$.*

*(ii) If one moreover assumes $G$ flat and separated over $S$ (i.e. when $G$ is smooth, quasi-compact and separated over
$S$), then $T$ is closed in $S$.*

<!-- label: III.VI_B.8.4 -->

*Proof.* It is clear that one may suppose $S$ affine with ring $A$. There exists then, by 10.1 and 10.10 b),[^VI_B-8-1]
a noetherian subring $A'$ of $A$ and an $A'$-group of finite type $G'$ such that $G' \otimes_{A'} A$ is isomorphic to
$G$. By EGA IV₃, 11.2.6 and 8.10.5,[^N.D.E-VI_B-82] if $G$ is flat and separated over $S$, one may suppose $G'$ flat and
separated over $S' = \operatorname{Spec} A'$.[^N.D.E-VI_B-83] As $G$ is of finite presentation over $S$, then (EGA IV₃,
9.7.7) the set of $s \in S$ such that $G_{s}$ is geometrically reduced (or, equivalently, smooth over $\kappa(s)$) is
locally constructible. Hence, by EGA IV₃, 9.3.3, one may suppose that, for every $s' \in S'$, $G'_{s'}$ is smooth over
$\kappa(s')$. On the other hand, if $s'$ denotes the image of $s$ in $S'$, one has: $G'_{s'} \otimes_{\kappa(s')}
\kappa(s) \simeq G_{s}$. Hence, by 8.3, for $G_{s}$ to be solvable (resp. nilpotent), it is necessary and sufficient
that the same be true of $G'_{s'}$. We are therefore reduced to the case where $S$ is a noetherian affine scheme.

Let us show then that $T$ is constructible. By applying the criterion (EGA 0_III, 9.2.3), one sees, reasoning as before,
that one is reduced to showing that, in the case where $S$ is noetherian and integral, either $T$ or $S - T$ contains a
non-empty open of $S$.

Suppose then $S$ integral and noetherian, with generic point $\eta$. Set, whatever $s \in S$, $K^{0}_{s} = G_{s}$, and
$K^{p}_{s} = (K^{p-1}_{s}, K^{p-1}_{s})$ (resp. $K^{p}_{s} = (G, K^{p-1}_{s})$). Let us first show that the sequence of
closed subschemes $K^{p}_{\eta}$ is stationary. It follows from 7.3 (v) that each of the $K^{p}_{\eta}$ is invariant,
hence the sequence of $K^{p}_{\eta}$ is decreasing; this sequence is then stationary since $G_{\eta}$ is noetherian;
there exists therefore an integer $n$ such that, for every $p \geqslant n$, one has: $K^{p}_{\eta} = K^{n}_{\eta}$.

On the other hand, by 10.12.1 and 10.13, there exists a non-empty open $S'$ of $S$ and

<!-- original page 394 -->

an $S'$-group of finite presentation $D$ such that for every $s \in S'$, one has $D_{s} = K^{n}_{s}$ and $(D_{s}, D_{s})
= D_{s}$ (resp. $(G_{s}, D_{s}) = D_{s}$). We may suppose $S' = S$. Then, whatever $s \in S$, and whatever $p \geqslant
n$, one has $D_{s} = K^{p}_{s}$, so that $G_{s}$ is solvable (resp. nilpotent) if and only if $D_{s}$ is isomorphic to
the unit $\kappa(s)$-group.

But by EGA IV₃, 9.6.1 (xi), the set of $s \in S$ such that the structural morphism $D_{s} \to \operatorname{Spec}
\kappa(s)$ is an isomorphism is constructible,[^N.D.E-VI_B-84] hence is either rare or contains a non-empty open of $S$.
We have therefore obtained that $T$ is locally constructible.

Let us show that if, moreover, $G$ is flat and separated over $S$, then $T$ is closed. Since $T$ is locally
constructible, for $T$ to be closed, it is necessary and sufficient that $T$ be stable under specialization (cf. EGA
IV₁, 1.10.1).

Let then $s \in S$ and $s'$ a specialization of $s$ in $S$. Since one has reduced to the case where $S$ is noetherian,
then, by EGA II, 7.1.9, there exists a discrete valuation ring $A$ and a morphism $\operatorname{Spec}(A) \to S$ such
that $s$ (resp. $s'$) is the image of the generic point $\alpha$ (resp. of the closed point $a$) of
$\operatorname{Spec}(A)$. It suffices then to show that if one sets $G' = G \otimes_{S} A$, and if $G'_{\alpha}$ is
solvable (resp. nilpotent), then so is $G'_{a}$. Note that, since $G$ is flat and separated over $S$, $G'_{\alpha}$ is
flat and separated over $A$, so we are reduced to the case where $S$ is the spectrum of a discrete valuation ring $A$.

Then, since $G_{\alpha}$ is supposed solvable (resp. nilpotent), there exists an integer $q$ such that $K^{q}_{\alpha}$
(with the notations introduced above) is isomorphic to the unit $\kappa(\alpha)$-group. For every $n$, let
$\bar{K}^{n}_{\alpha}$ denote the schematic closure (in the sense of EGA IV₂, 2.8.5) of $K^{n}_{\alpha}$ in $G$. Let us
show, by induction on $p$, that $(\bar{K}^{p}_{\alpha})_{a} \supset K^{p}_{a}$. Note first that, since $G$ is flat over
$A$, then $G_{\alpha}$ is equal to $G$̄ (EGA IV₂, 2.8.5), so $(\bar{K}^{0}_{\alpha})_{a} = K^{0}_{a}$.

Let $p \geqslant 0$. Suppose we have established that $K^{p}_{a} \subset (\bar{K}^{p}_{\alpha})_{a}$, and denote by
$\nu_{a}, \nu_{\alpha}, \nu, \bar{\nu}_{a}$ the following morphisms, defined as in 7.2.2:

```text
                solvable case                                   nilpotent case
ν_a : K^p_a ×_{κ(a)} K^p_a → G_a,                   resp.       G_a ×_{κ(a)} K^p_a → G_a,
ν_α : K^p_α ×_{κ(α)} K^p_α → G_α                    resp.       G_α ×_{κ(α)} K^p_α → G_α,
ν   : K̄^p_α ×_A K̄^p_α → G,                        resp.       G ×_A K̄^p_α → G,
ν̄_a : (K̄^p_α)_a ×_{κ(a)} (K̄^p_α)_a → G_a,         resp.       G_a ×_{κ(a)} (K̄^p_α)_a → G_a.
```

Since $\nu_{\alpha}$ factors through $K^{p+1}_{\alpha}$, then $\nu$ factors through $\bar{K}^{p+1}_{\alpha}$, which is
obviously a group subscheme of $G$, hence $\bar{K}^{p+1}_{\alpha}$ contains $\Gamma_{G}(\nu)$. By 7.1 (iii), one has
$\Gamma_{G}(\nu)_{a} = \Gamma_{G_{a}}(\bar{\nu}_{a})$; and, by the induction hypothesis,

```text
K^p_a ×_{κ(a)} K^p_a ⊂ (K̄^p_α)_a ×_{κ(a)} (K̄^p_α)_a    resp.    G_a ×_{κ(a)} K^p_a ⊂ G_a ×_{κ(a)} (K̄^p_α)_a,
```

so that $K^{p+1}_{a} = \Gamma_{G_{a}}(\nu_{a}) \subset \Gamma_{G_{a}}(\bar{\nu}_{a}) = \Gamma_{G}(\nu)_{a} \subset
(\bar{K}^{p+1}_{\alpha})_{a}$.

<!-- original page 395 -->

But since $K^{q}_{\alpha}$ is isomorphic to the unit $\kappa(\alpha)$-group, and the unit $A$-group is flat over $A$ and
is isomorphic to a closed subscheme of $G$ (since $G$ is separated over $A$, cf. 5.1), it follows from EGA IV₂, 2.8.5
that the schematic closure $\bar{K}^{q}_{\alpha}$ is isomorphic to the unit $A$-group. As we just saw that $K^{q}_{a}
\subset (\bar{K}^{q}_{\alpha})_{a}$, this entails that $K^{q}_{a}$ is isomorphic to the unit $\kappa(a)$-group, so that
$G_{a}$ is solvable (resp. nilpotent). ∎

## 9. Quotient sheaves

<!-- label: III.VI_B.9 -->

The present number is limited essentially to a reminder, in the particular case of homogeneous spaces of groups, of
well-known general facts about passage to the quotient by flat equivalence relations (cf. Exp. IV).

**Definition 9.1.** *Given a monomorphism $u : G' \to G$ of $S$-groups, one denotes by $G/G'$ (resp. $G'\backslash G$),
and calls* right (resp. left) quotient sheaf of $G$ by $G'$*, the sheaf (for the (fpqc) topology) quotient of $G$ by the
equivalence relation defined by the monomorphism:*

```text
G ×_S G′ ─δ ∘ (id_G × u)→ G ×_S G    (resp. G′ ×_S G ─γ ∘ (u × id_G)→ G ×_S G),
```

*where $\delta$ (resp. $\gamma$) denotes the automorphism of $G \times_{S} G$ defined by $(g, h) \mapsto (g, gh)$ (resp.
$(h, g) \mapsto (hg, g)$) for $g, h \in G(T)$.*

<!-- label: III.VI_B.9.1 -->

**Proposition 9.2.** *Let $u : G' \to G$ be a monomorphism of $S$-groups. Suppose that $G/G'$ is representable by an
$S$-scheme $G''$. Then:*

*(i) The canonical morphism $p : G \to G''$ is covering for the (fpqc) topology.*

*(ii) If one sets $\epsilon'' = p \circ \epsilon$ (this morphism is called the unit section of $G''$), the following
diagrams are cartesian:*

```text
G ×_S G′ ─μ ∘ (id_G × u)→ G              G′ ──u──→ G
   │                      │              │         │
  pr_1                    p              π′        p
   │                      │              │         │
   ↓                      ↓              ↓         ↓
   G ────────p────────→ G″               S ──ε″──→ G″.
```

*In particular, $u$ is an immersion.*

*(iii) There exists on $G''$ a unique structure of $S$-scheme with left operator group $G$, such that $p$ is a morphism
of $S$-schemes with operator group $G$.*

*(iv) If one moreover supposes $G'$ invariant in $G$, there exists on $G''$ a unique structure of $S$-group such that
$p$ is a morphism of $S$-groups.*

*(v) Let `S_0` be an $S$-scheme; set $G_{0} = G \times_{S} S_{0}$, and $G'_{0} = G' \times_{S} S_{0}$; then
$G_{0}/G'_{0}$ is representable by $G''_{0} = G'' \times_{S} S_{0}$.*[^N.D.E-VI_B-85]

*(vi) Let $P$ be a property for an $S$-morphism. Suppose $P$ stable under base change; then if $p : G \to G''$ satisfies
$P$, the same is true of the structural morphism $\pi' : G' \to S$.*

<!-- original page 396 -->

*(vii) Let $P$ be a property for an $S$-morphism. Suppose $P$ is local in nature for the (fpqc) topology (cf. 2.0 and
2.1.2). Then, for the morphism $p : G \to G''$ to satisfy $P$, it is necessary and sufficient that the same be true of
$\pi' : G' \to S'$.*

*(viii) Let $P$ be a property for an $S$-morphism; suppose $P$ is local in nature for the (fpqc) topology, and stable
under composition; then, if the structural morphisms $G'' \to S$ and $G' \to S$ satisfy $P$, the same is true of the
structural morphism $G \to S$.*

*(ix) Suppose $G$ reduced; then $G''$ is reduced.*

*(x) For $G''$ to be separated over $S$, it is necessary and sufficient that $u$ (or, equivalently, $\epsilon''$) be a
closed immersion.*

*(xi) For $G'$ to be flat over $S$, it is necessary and sufficient that $p$ be a flat morphism (or, equivalently,
faithfully flat).*

*In this case, for $G''$ to be flat over $S$, it is necessary and sufficient that $G$ be flat over $S$.*

*(xii) For $G'$ to be flat and locally of finite presentation over $S$, it is necessary and sufficient that $p : G \to
G''$ be faithfully flat and locally of finite presentation.*

*In this case, for $G''$ to be locally of finite presentation (resp. locally of finite type, of finite type, smooth,
étale, unramified, locally quasi-finite, quasi-finite) over $S$, it suffices that the same be true of $G$ over $S$ (and
the condition is also necessary in the first two cases, cf. (viii)).*

*(xiii) Suppose $G'$ flat and of finite presentation over $S$.*

*a) Then $p$ is of finite presentation and faithfully flat;*

*b) moreover, for $G$ to be of finite presentation over $S$, it is necessary and sufficient that the same be true of
$G''$.*

<!-- label: III.VI_B.9.2 -->

Recall that the equivalence relation under consideration is universally effective (IV 4.4.9). Then assertions (i),
(iii), (iv), (v) and the first assertion of (ii) follow from IV 4.4.3, 5.2.2, 5.2.4, 3.4.5 and 3.3.2 (iii). The second
assertion of (ii) follows from the first, as the following cartesian diagram shows, since $(G \times_{S} G') \times_{G}
S$ is isomorphic to $G'$:

```text
G′ ─((ε ∘ π′), id_{G′})→ G ×_S G′ ─μ ∘ (id_G × u)→ G
│                          │                       │
π′                         pr_1                    p
│                          │                       │
↓                          ↓                       ↓
S ────────ε────────────→  G ─────────p──────────→ G″.
```

Finally, it is clear that $\epsilon''$ is an $S$-section of $G''$, hence an immersion (EGA I, 5.3.13); by the preceding
cartesian diagram, the same is true of $u$, which completes the proof of (ii). Moreover, (vi) is an immediate
consequence of the second cartesian diagram of (ii).

Let us show (vii). By (i), $p$ is covering for the (fpqc) topology; hence, by (ii), to show that $p$ satisfies $P$, it
suffices to show that the first projection $pr_{1} : G \times_{S} G' \to G$ satisfies $P$, which follows from the fact
that $P$ is stable under base change, since $pr_{1}$ comes from $\pi'$ by base change.

<!-- original page 397 -->

It is clear that (viii) follows from (vii), since $\pi = \pi'' \circ p$, where $\pi'' : G'' \to S$ denotes the
structural morphism.

Let us show (ix). By (i), $p$ is an epimorphism; since $G$ is reduced, $p$ factors through the immersion $G''_{red} \to
G''$, which is therefore also an epimorphism, hence an isomorphism (IV 4.4.4).

Let us show (x). If $G''$ is separated over $S$, then $\epsilon''$ is a closed immersion, by EGA I, 5.4.6. On the other
hand, one saw in (ii) that $\epsilon''$ is a closed immersion if and only if $u$ is. Finally, if $u$ is a closed
immersion, then so is $\delta \circ (id_{G} \times u) : G \times_{S} G' \to G \times_{S} G$; hence, by Lemma 9.2.1
below, $G''$ is separated over $S$.

Assertion (xi) follows from (vii) and from EGA IV₂, 2.2.13.

Assertion (xii) follows from (vii), from EGA IV₄, 17.7.5 and 17.7.7, and from the fact that, $p$ being universally open,
whatever $s \in S$, if the underlying space of $G_{s}$ is discrete, the same is true of the underlying space of
$G''_{s}$.

Finally, assertion (xiii) follows from (vii), (viii), and from EGA IV₄, 17.7.5. ∎

**Lemma 9.2.1.** *Let $X$ be an $S$-scheme and $R$ an equivalence relation defined on $X$ by the monomorphism $v : R \to
X \times_{S} X$. Suppose $R$ effective. Then:*

*(i) $v$ is an immersion, and is a closed immersion if $Y = X/R$ is separated.*

*(ii) Suppose moreover that $Y$ represents the (fpqc) quotient sheaf of $X$ by $R$*[^N.D.E-VI_B-86] *and that $v$ is a
closed immersion. Then $Y = X/R$ is separated over $S$.*

<!-- label: III.VI_B.9.2.1 -->

Recall (IV Def. 3.3.2) that the hypothesis "$R$ effective" means that there exists a morphism of $S$-schemes $p : X \to
Y$ such that the natural morphism $R \to X \times_{Y} X$ is an isomorphism. From this one deduces (EGA I, 5.3.5) the
following cartesian diagram:

```text
R ────v────→ X ×_S X
│              │
│              p × p
│              │
↓ Δ_{Y/S}      ↓
Y ─────────→ Y ×_S Y.
```

Then, since $\Delta_{Y/S}$ is an immersion (EGA I, 5.3.9), the same is true of $v$. Similarly, if $Y$ is separated over
$S$, $\Delta_{Y/S}$ is a closed immersion, hence so is $v$.

Conversely, suppose that $v$ is a closed immersion and that $Y$ represents the (fpqc) quotient sheaf of $X$ by $R$. Then
$p$ is covering for the (fpqc) topology (IV 4.4.3), and hence $p \times p$ is too (by base change, $p \times id_{X}$ and
$id_{Y} \times p$ are covering, hence so is their composite $p \times p$). Hence, by (fpqc) descent (cf. EGA IV₂,
2.7.1), $\Delta_{Y/S}$ is a closed immersion, i.e. $Y$ is separated over $S$. ∎

**Remark 9.2.2.** *Under the general hypotheses of 9.2, if one assumes $G'$ flat and locally of finite presentation over
$S$, then $p$ is covering for the (fppf) topology,*[^N.D.E-VI_B-87] *by 9.2 (vii), hence assertions (vii) and (viii) of
9.2 can be extended to properties $P$ local in nature for the (fppf) topology.*

<!-- label: III.VI_B.9.2.2 -->

<!-- original page 398 -->

**Remark 9.3.** *a) The question of whether a quotient $G/G'$ is representable or not is often delicate; in this seminar
we demonstrate the representability of certain particular quotients.*

*In general, in order to assert that the quotient $G/G'$ is representable, it is not sufficient to suppose $G$ and $G'$
of finite presentation over $S$ and $G'$ flat over $S$. Indeed, suppose moreover $G$ smooth with connected fibers. In
this case, if $G/G'$ is a scheme, it is separated, by Corollary 5.4, and hence $G' \hookrightarrow G$ is a closed
immersion, by 9.2 (x); consequently, if $G'$ is not closed in $G$, then $G/G'$ is not representable.*

*To obtain such a counterexample, one may take for $S$ the spectrum of a discrete valuation ring, and set $G = G_{m,S}$.
Consider moreover an integer $n > 1$, invertible on $S$; then $\mu_{n} = Ker(G \xrightarrow{n} G)$ is a closed subgroup
of $G$ étale over $S$*[^N.D.E-VI_B-88] *(cf. VII_A). Let $G'$ be the open subgroup of $\mu_{n}$ obtained by removing
from $\mu_{n}$ the closed part of the closed fiber of $\mu_{n}$ complementary to the origin. Then $G'$ is not closed in
$G$, hence $G/G'$ is not representable. (One can also fabricate such examples where $G'$ is smooth with connected
fibers.)*

*b) It is not excluded that $G/G'$ be representable on the other hand, when $G$ and $G'$ are of finite presentation over
$S$, and $G'$ is flat over $S$ and closed in $G$.*[^VI_B-9-1][^N.D.E-VI_B-89] *Under these hypotheses, it is known that
$G/G'$ is representable in the following particular cases:*

*1° — $S$ is the spectrum of an Artinian ring (cf. VI_A 3.2 and 3.3.2).*

*2° — $G'$ is proper over $S$ and $G$ quasi-projective over $S$ (cf. V 7.1).*

*3° — $S$ is locally noetherian of dimension 1 (cf. [An73], Th. 4.C).*

<!-- label: III.VI_B.9.3 -->

## 10. Passage to the inverse limit in group schemes and in schemes with operator group

<!-- label: III.VI_B.10 -->

### 10.0.

Let us recall the essential result of EGA IV₃, § 8.8. Suppose given the following situation: `S_0` a quasi-compact and
quasi-separated scheme, $I$ a filtered increasing preordered set, $(A_{i})_{i \in I}$ an inductive system of
quasi-coherent commutative $\mathcal{O}_{S_{0}}$-algebras, $A = \varinjlim A_{i}$, $S_{i} = \operatorname{Spec} A_{i}$
for $i \in I$, and $S = \operatorname{Spec} A$;[^N.D.E-VI_B-90] then the category of $S$-schemes of finite presentation
is determined up to equivalence by the data of the categories of $S_{i}$-schemes of finite presentation, of the functors
between these categories $\rho_{ji} : X_{i} \mapsto X_{i} \times_{S_{i}} S_{j}$ for $i \leqslant j$, and the
transitivity isomorphisms $\rho_{kj} \circ \rho_{ji} \xrightarrow{\sim} \rho_{ki}$.

Let us be precise. Given $j \in I$, and an $S_{j}$-scheme of finite presentation $X_{j}$, we shall set, for every $i \in
I$ such that $i \geqslant j$, $X_{i} = X_{j} \times_{S_{j}} S_{i}$, and $X = X_{j} \times_{S_{j}} S$. Then (EGA IV₃,
8.8.2):

(i) Given $j \in I$, and two $S_{j}$-schemes of finite presentation $X_{j}$ and $Y_{j}$, the canonical map
`lim⃗_{i ⩾ j} Hom_{S_i}(X_i, Y_i) → Hom_S(X, Y)` is bijective.

(ii) For every $S$-scheme of finite presentation $X$, there exists an index $j \in I$, an $S_{j}$-scheme of finite
presentation $X_{j}$ and an $S$-isomorphism $X \xrightarrow{\sim} X_{j} \times_{S_{j}} S$.

<!-- original page 386 -->

One concludes (EGA IV₃, 8.8.3) that, whenever one has a diagram $\mathcal{D}$ involving a finite number of objects and
arrows of the category of $S$-schemes of finite presentation, one can find an index $i \in I$ and a diagram
$\mathcal{D}_{i}$ in the category of $S_{i}$-schemes of finite presentation, such that the diagram $\mathcal{D}$ comes
up to isomorphism from the diagram $\mathcal{D}_{i}$ by base change $S \to S_{i}$. One can even find $i$ and
$\mathcal{D}_{i}$ such that every cartesian square of $\mathcal{D}$ comes from a cartesian square of $\mathcal{D}_{i}$.

### 10.1.

Moreover, a great number of common properties for a morphism, stable under base change, possess the following property:

> Let $u : X \to Y$ be an $S$-morphism between $S$-schemes of finite presentation; it comes by base change from an
> $S_{j}$-morphism $u_{j} : X_{j} \to Y_{j}$ between $S_{j}$-schemes of finite presentation, by 10.0; then, for $u$ to
> have property $P$, it is necessary and sufficient that there exist $i \geqslant j$ such that $u_{i} = u_{j}
> \times_{S_{j}} S_{i}$ has property $P$.

This is so in the case where $P$ is one of the following properties for a morphism: being separated, surjective,
radicial, affine, quasi-affine, finite, quasi-finite, proper, projective, quasi-projective, an isomorphism, a
monomorphism, an immersion, an open immersion, a closed immersion (EGA IV₃, 8.10.5), flat (EGA IV₃, 11.2.6), smooth,
unramified or étale (EGA IV₄, 17.7.8).[^N.D.E-VI_B-91]

Note that this is also the case where $P$ is the property of being covering for the (fppf) topology; indeed, given two
$S$-schemes of finite presentation $X$ and $Y$, and an $S$-morphism $u : X \to Y$, it follows from IV, 6.3.1
(i)[^N.D.E-VI_B-92] that, for $u$ to be covering for the (fppf) topology, it is necessary and sufficient that there
exist an $S$-scheme $Z$ and an $S$-morphism $v : Z \to Y$ faithfully flat and of finite presentation which factors
through $u$.

The aim of this section 10 is to give variants of this kind of results for the category of $S$-groups of finite
presentation, that of $S$-schemes with operator group, and for certain properties for monomorphisms of groups (being
invariant, central with representable quotient sheaf, etc.).

The two preliminary results of this type are the following. (In nos. 10.2 to 10.9 below, we keep the notations
introduced in 10.0.)

<!-- original page 400 -->

**Lemma 10.2.** *Let $G_{j}$ and $H_{j}$ be two $S_{j}$-groups of finite presentation; set, for every $i \geqslant j$,
$G_{i} = G_{j} \times_{S_{j}} S_{i}$, $G = G_{j} \times_{S_{j}} S$, and define similarly $H_{i}$ and $H$. Then the
canonical map below is bijective:*

```text
lim⃗_{i ⩾ j} Hom_{S_i-gr.}(G_i, H_i) → Hom_{S-gr.}(G, H).
```

<!-- label: III.VI_B.10.2 -->

**Lemma 10.3.** *Let $G$ be an $S$-group of finite presentation; then there exist $j \in I$, an $S_{j}$-group of finite
presentation $G_{j}$, and an isomorphism of $S$-groups $G \cong G_{j} \times_{S_{j}} S$.*

<!-- label: III.VI_B.10.3 -->

Assertions 10.2 and 10.3 are easy consequences of 10.0 and 10.1, taking into account the interpretation[^N.D.E-VI_B-93]
of the structure of $S$-group given in EGA 0_III, 8.2.5 and 8.2.6.

**Lemma 10.4.** *Let $u : G \to H$ be a morphism of $S$-groups between $S$-groups of finite presentation. By 10.3 and
10.2, $u$ comes by base change from a morphism $u_{j} : G_{j} \to H_{j}$ between $S_{j}$-groups of finite presentation.
Then, for $u$ to be a central monomorphism (resp. an invariant monomorphism), it is necessary and sufficient that there
exist $i \geqslant j$ such that $u_{i} = u_{j} \times_{S_{j}} S_{i}$ has the same property.*

<!-- label: III.VI_B.10.4 -->

This is an immediate consequence of 10.0 and 10.1, taking into account the characterization given in 6.7 of central or
invariant monomorphisms of groups.

**Corollary 10.5.** *Let $G_{j}$ be an $S_{j}$-group of finite presentation. For $G_{j} \times_{S_{j}} S$ to be
commutative, it is necessary and sufficient that there exist $i \geqslant j$ such that $G_{j} \times_{S_{j}} S_{i}$ is
so.*

<!-- label: III.VI_B.10.5 -->

Indeed, it amounts to the same to say that an $S$-group is commutative, or that, considered as a group subscheme of
itself, it is central.

**Proposition 10.6.** *Let $G_{j}$ be an $S_{j}$-group of finite presentation, $G'_{j}$ a group subscheme of $G_{j}$
flat and of finite presentation over $S_{j}$. For $(G_{j} \times_{S_{j}} S)/(G'_{j} \times_{S_{j}} S)$ to be
representable for the (fpqc) topology, it is necessary and sufficient that there exist $i \geqslant j$ such that $(G_{j}
\times_{S_{j}} S_{i})/(G'_{j} \times_{S_{j}} S_{i})$ is so.*

<!-- label: III.VI_B.10.6 -->

This is a consequence of the following more general lemma.

**Lemma 10.7.** *Let $X_{j}$ be an $S_{j}$-scheme of finite presentation, and $R_{j}$ an equivalence relation on $X_{j}$
flat and of finite presentation.*[^N.D.E-VI_B-94] *For the quotient sheaf $(X_{j} \times_{S_{j}} S)/(R_{j}
\times_{S_{j}} S)$ for the topology $T =$ (fppf) or (fpqc) to be representable, it is necessary and sufficient that
there exist $i \geqslant j$, such that the quotient sheaf $(X_{j} \times_{S_{j}} S_{i})/(R_{j} \times_{S_{j}} S_{i})$
for the topology $T$ is so.*

<!-- label: III.VI_B.10.7 -->

Taking into account the statements of EGA IV₂, 8.8.2, 8.8.3, 8.10.5 and 11.2.6 recalled in 10.0, this lemma is a
consequence of the following result.

<!-- original page 401 -->

**Lemma 10.8.** *Let $T$ be the (fppf) or (fpqc) topology; let $X$ be an $S$-scheme of finite presentation (resp.
locally of finite presentation), $R$ an equivalence relation on $X$ defined by a monomorphism $v : R \to X \times_{S} X$
such that $pr_{1} \circ v$ is flat and of finite presentation (resp. flat and locally of finite presentation). Then the
following conditions are equivalent:*

*(i) The quotient sheaf $X/R$ for the topology $T$ is representable.*

*(ii) There exist an $S$-scheme of finite presentation (resp. locally of finite presentation) $Y$ and a faithfully flat
morphism $p : X \to Y$ such that the diagram*

```text
(D)    R ──pr_1 ∘ v─→ X
       │              │
       pr_2 ∘ v       p
       │              │
       ↓              ↓
       X ─────p────→ Y
```

*is cartesian.*

<!-- label: III.VI_B.10.8 -->

Let us note first that, by IV, 3.3.2 and 4.4.3, for the sheaf $X/R$ for the topology $T$ to be representable by $Y$, it
is necessary and sufficient that the diagram (D) be cartesian and that $p$ be covering for the topology $T$.

Let us show that (i) entails (ii). Hypothesis (i) implies that the diagram (D) is cartesian, hence that $pr_{1} \circ v$
is deduced from $p$ by base change by $p$, and that $p$ is covering for the (fpqc) topology. Hence, by (fpqc) descent
(EGA IV₂, 2.7.1), since $pr_{1} \circ v$ is faithfully flat and (locally) of finite presentation, so is $p$. Then, by
EGA IV₄, 17.7.5, since $X$ is (locally) of finite presentation over $S$, so is $Y$.

Let us show that (ii) entails (i). It suffices to show that $p$ is covering for the (fppf) topology; now $p$ is
faithfully flat by hypothesis, and is locally of finite presentation since $X$ and $Y$ are locally of finite
presentation over $S$ (EGA IV₁, 1.4.3 (v)). ∎

**Lemma 10.9.** *Let $G_{j}$ be an $S_{j}$-group of finite presentation, and $G = G_{j} \times_{S_{j}} S$. For $G^{0}$
to be representable, it is necessary and sufficient that there exist $i \geqslant j$ such that $(G_{i})^{0} = (G_{j}
\times_{S_{j}} S_{i})^{0}$ is so.*

<!-- label: III.VI_B.10.9 -->

The condition is sufficient, since the functor $G \mapsto G^{0}$ commutes with base change, by 3.3.

Conversely, suppose $G^{0}$ representable. Then, by 3.9, $G^{0}$ is open in $G$ and quasi-compact over $S$, hence of
finite presentation over $S$, since $G$ is. Then, by 10.3 and 10.1, there exist $i \geqslant j$ and an open group
subscheme $H_{i}$ of $G_{i}$ such that $H_{i} \times_{S_{i}} S = G^{0}$. The structural morphism $G^{0} \to S$ is
connected, i.e. has geometrically connected fibers (VI_A 2.1.1), hence, by EGA IV₃, 9.3.3 and 9.7.7, up to increasing
$i$, one may suppose that the structural morphism $H_{i} \to S$ is connected. Then, by 3.10.1, the underlying space of
$H_{i}$ is none other than $(G_{i})^{0}$, and hence $H_{i}$ represents $(G_{i})^{0}$. ∎

### 10.10.

Let us recall two very useful particular cases of the situation stated in 10.0 (cf. EGA IV₃, 8.1.2 a) and c)):

<!-- original page 402 -->

a) Given a point $x$ of a scheme $X$, one sets $S_{0} = \operatorname{Spec} \mathbb{Z}$ and considers the filtered
decreasing projective system $(S_{i})_{i \in I}$ of affine open neighborhoods of $x$; then $S = \operatorname{Spec}
\mathcal{O}_{X,x}$. In particular, if $x$ is the generic point of an integral scheme $X$, one finds $S =
\operatorname{Spec} \kappa(x)$.

b) One sets $S_{0} = \operatorname{Spec} \mathbb{Z}$, and considers the family $(A_{i})_{i \in I}$ preordered by
inclusion of the finitely generated sub-$\mathbb{Z}$-algebras of the ring of an affine scheme $S$. Given that the
$A_{i}$ are noetherian rings, this allows in many cases to pass from the noetherian case to the general case.

We are now going to give two results concerning the particular case considered in a).[^N.D.E-VI_B-95]

**Proposition 10.11.** [^N.D.E-VI_B-96] *Let $S$ be an integral scheme with generic point $\eta$, $G$ (resp. `Y, Z`) an
$S$-group (resp. $S$-schemes) of finite presentation, $u, v, i : Y \to G$ and $j : Z \to G$ morphisms of $S$-schemes.
Suppose that $i_{\eta} : Y_{\eta} \to G_{\eta}$ and $j_{\eta} : Z_{\eta} \to G_{\eta}$ are closed immersions.*

*Then, there exists a non-empty open $S'$ of $S$ such that the morphisms $i' : Y' \to G'$ and $j' : Z' \to G'$ obtained
by base change are closed immersions, and such that the functors:*

```text
Transp(u′, v′),    Transp_{G′}(i′(Y′), j′(Z′))    and    Transpstr_{G′}(i′(Y′), j′(Z′))
```

*resp.*

```text
Centr(u′)    and    Norm_{G′} i′(Y′)
```

*are representable by closed sub-$S'$-schemes (resp. sub-$S'$-groups) of $G'$, of finite presentation over $S'$.*

<!-- label: III.VI_B.10.11 -->

We shall apply the results of 10.1, first in the situation of 10.10 a), then in that of 10.10 b). Since $G_{\eta},
Y_{\eta}, Z_{\eta}$ are flat over the field $\kappa(\eta)$, $G_{\eta}$ is separated over $\kappa(\eta)$ (VI_A 0.3), and
$i_{\eta}, j_{\eta}$ are closed immersions, then, by 10.1, there exists an affine open $S' = \operatorname{Spec}(A')$ of
$S$, a noetherian subring $A$ of $A'$, $A$-schemes $G_{A}, Y_{A}, Z_{A}$, flat and of finite presentation over $A$, and
morphisms $u_{A}, v_{A}, i_{A} : Y_{A} \to G_{A}$ and $j_{A} : Z_{A} \to G_{A}$, such that `G_A` is an $A$-group,
separated over $A$, $i_{A}$ and $j_{A}$ are closed immersions, and $G \times_{S} S' = G_{A} \otimes A'$, etc. As the
functors considered for $S'$ are deduced by base change from the analogous functors for $\operatorname{Spec}(A)$, it
suffices to establish the result for the latter.

By EGA IV₂, 6.9.2, up to replacing $A$ by a localization $A_{f}$ (and hence $S'$ by the affine open $S'_{f}$), one may
suppose that $G_{A}, Y_{A}, Z_{A}$ are essentially free over $A$ (in the sense of 6.2.1).[^N.D.E-VI_B-97] It follows
then from 6.2.4 b) and e) that, under the hypotheses of the statement, the functors considered are representable by
closed sub-$A$-schemes of `G_A` (hence of finite presentation over $A$, since $A$ is noetherian and `G_A` of finite
presentation

<!-- original page 403 -->

over $A$), and these are sub-$A$-groups of `G_A` in the case of $Centr(u_{A})$ and of $Norm_{G_{A}} i_{A}(Y_{A})$. ∎

**Corollary 10.11.1.** *Let $S$ be an integral scheme with generic point $\eta$, `G, H, K` $S$-groups of finite
presentation, $i : H \to G$ and $j : K \to G$ two quasi-compact monomorphisms of $S$-groups. Then, there exists a
non-empty open $S'$ of $S$ such that the morphisms $i' : H' \to G'$ and $j' : K' \to G'$ obtained by base change are
closed immersions, and such that the functors:*

```text
Transp_{G′}(H′, K′)    and    Transpstr_{G′}(H′, K′)    (resp. Centr_{G′} H′    and    Norm_{G′} H′)
```

*are representable by closed sub-$S'$-schemes (resp. sub-$S'$-groups) of $G'$, of finite presentation over $S'$.*

<!-- label: III.VI_B.10.11.1 -->

This follows from the preceding proposition since, by 1.4.2, the hypotheses entail that $i_{\eta}$ and $j_{\eta}$ are
closed immersions.

**Proposition 10.12.** *Let $S$ be an integral scheme, $G$ an $S$-group of finite presentation, $A$ and $B$ two group
subschemes of $G$, of finite presentation over $S$ and with smooth generic fiber. Suppose moreover satisfied one of the
following conditions:*

*a) $A$ has connected generic fiber,*

*b) $A$ and $B$ are invariant in $G$.*

*Then, there exists a non-empty open $S'$ of $S$ and a closed group subscheme $D'$ of $G' = G|_{S'}$, of finite
presentation over $S'$, with smooth fibers, which represents the (fppf) sheaf associated with the presheaf in groups of
commutators of $A' = A|_{S'}$ and $B' = B|_{S'}$ in $G'$, and $D'$ has connected fibers in case (a), and is invariant in
$G'$ in case (b).*

*In particular, for every $s \in S'$, one has $D'_{s} = (A_{s}, B_{s})$ with the notations of 7.2.2.*

<!-- label: III.VI_B.10.12 -->

Let $\eta$ be the generic point of $S$; set $H_{\eta} = (A_{\eta}, B_{\eta})$. Since $A_{\eta}$ and $B_{\eta}$ are
smooth, then, by 7.8 in case (a), and 7.3 (v) in case (b), $H_{\eta}$ is connected (resp. invariant in $G_{\eta}$).

We are in the situation of 10.0 corresponding to 10.10 (a); hence, by 10.3 and 10.1, there exists a non-empty open $S'$
of $S$ and a sub-$S'$-group scheme $D'$ of finite presentation and closed in $G'$, such that $D'_{\eta} = D'
\otimes_{S'} \kappa(\eta)$ equals $H_{\eta}$. Moreover, by EGA IV₃, 9.7.7 and 9.3.3, one may suppose that $D'$ has
geometrically reduced fibers. In case (a), one may suppose, by EGA IV₃, 9.7.7 and 9.3.3 again, that $D'$ has connected
fibers, hence geometrically connected (cf. VI_A, 2.1.1). In case (b), one may suppose, by 10.4, that $D'$ is invariant
in $G'$.

Moreover, we have seen, in the course of the proof of 7.8, that there exists an integer $n$ such that
$\nu^{n}_{\eta}((A_{\eta} \times_{\kappa(\eta)} B_{\eta})^{n}) = D'_{\eta}$, where $\nu_{\eta}$ and $\nu^{n}_{\eta}$ are
defined as in 7.2.2 (a) and 7.1 (ii). We may define by the same formulas the morphisms

```text
ν′ : A′ ×_{S′} B′ → G′    and    ν′^n : (A′ ×_{S′} B′)^n → G′,
```

and one has $\nu'^{n} \otimes_{S'} \kappa(\eta) = \nu^{n}_{\eta}$.

<!-- original page 404 -->

Consequently, by 10.1, one may choose $S'$ such that the morphism $\nu'^{n}$ is flat and factors through $D'$, and such
that the morphism $\nu'^{n} : (A' \times_{S'} B')^{n} \to D'$ thus obtained is surjective. Then, by 7.5, the
morphism[^N.D.E-VI_B-98]

```text
ν′^{2n} = μ ∘ (ν′^n ×_{S′} ν′^n) : (A′ ×_{S′} B′)^{2n} → D′,
```

is covering for the (fppf) topology. Hence, by 7.6, $D'$ represents the (fppf) sheaf associated with the presheaf of
commutators of $A'$ and $B'$ in $G'$.

Moreover, $\nu'^{n}$ induces, for every $s \in S'$, a surjective morphism $\nu^{n}_{s} : (A_{s} \times_{\kappa(s)}
B_{s})^{n} \to D'_{s}$.[^N.D.E-VI_B-99] Then $D'_{s}$ is a closed subgroup of $G_{s}$ containing $\nu_{s}(A_{s}
\times_{\kappa(s)} B_{s})$, hence also $(A_{s}, B_{s})$. As $\nu^{n}_{s}$ is surjective, $D'_{s}$ equals $(A_{s},
B_{s})$ and represents, by 7.6, the (fppf) sheaf of commutators of $A_{s}$ and $B_{s}$ in $G_{s}$. ∎

**Corollary 10.12.1.** [^N.D.E-VI_B-100] *Let $S$ be an integral scheme, with generic point $\eta$, and $G$ an $S$-group
of finite presentation with smooth fibers. Set $K^{0}_{\eta} = G_{\eta}$ and $K^{p}_{\eta} = (K^{p-1}_{\eta},
K^{p-1}_{\eta})$ (resp. $K^{p}_{\eta} = (G, K^{p-1}_{\eta})$) for every $p \in \mathbb{N}*$. Fix $n \in \mathbb{N}*$.
Then there exists a non-empty open $S'$ of $S$ and a group subscheme $D$ invariant in $G|_{S'}$, of finite presentation
and with smooth fibers, such that $D_{s} = K^{n}_{s}$ for every $s \in S'$.*

<!-- label: III.VI_B.10.12.1 -->

This follows from 10.12, by induction on $n$.

**Corollary 10.13.** *Let $S$ be an integral scheme with generic point $\eta$, $G$ an $S$-group, $H$ an invariant
sub-$S$-group scheme in $G$; suppose $G$ and $H$ of finite presentation over $S$ and with smooth generic
fiber.*[^N.D.E-VI_B-101]

*If one has $(H_{\eta}, H_{\eta}) = H_{\eta}$ (resp. $(G_{\eta}, H_{\eta}) = H_{\eta}$), then there exists a non-empty
open $S'$ of $S$ such that for every $s \in S'$, one has $(H_{s}, H_{s}) = H_{s}$ (resp. $(G_{s}, H_{s}) = H_{s}$).*

<!-- label: III.VI_B.10.13 -->

Indeed, by the proof of 10.12, there exists a non-empty open $S'$ of $S$ and a sub-$S'$-group scheme $D$ of $G|_{S'}$,
of finite presentation and with smooth fibers, such that $D_{s} = (H_{s}, H_{s})$ (resp. $D_{s} = (G_{s}, H_{s})$) for
every $s \in S'$. On the other hand, since $D_{\eta} = H_{\eta}$ and since $D$ and $H$ are of finite presentation over
$S'$, then, by EGA IV₃, 8.8.2.5, there exists a non-empty open $S''$ of $S'$ such that $D|_{S''} = H|_{S''}$. For every
$s \in S''$, one has therefore $H_{s} = D_{s} = (H_{s}, H_{s})$ (resp. $H_{s} = D_{s} = (G_{s}, H_{s})$). ∎

### 10.14.

Statements 10.2 and 10.3 concerning the category of $S$-groups of finite presentation extend to the category of pairs
formed by an $S$-group of finite presentation and an $S$-scheme of finite presentation with operator group $G$. To be
precise, in the situation recalled at the start of 10.0:

(i) Let $j \in I$ and $G_{j}$ and $G'_{j}$ two $S_{j}$-groups of finite presentation, $H_{j}$ (resp. $H'_{j}$) an
$S_{j}$-scheme of finite presentation with operator group $G_{j}$ (resp. $G'_{j}$). Set, for $i \in I$, $i \geqslant j$,
$G_{i} = G_{j} \times_{S_{j}} S_{i}$ and $G = G_{j} \times_{S_{j}} S$, and define similarly $G'_{i}, G', H_{i}, H,
H'_{i}$

<!-- original page 405 -->

and $H'$. Denote by $Dihom_{S-gr.}((G, H), (G', H'))$ the set of di-morphisms of $S$-groups and $S$-schemes with
operator group of the pair $(G, H)$ into the pair $(G', H')$. Then the canonical map

```text
lim⃗_{i ⩾ j} Dihom_{S_i-gr.}((G_i, H_i), (G′_i, H′_i)) → Dihom_{S-gr.}((G, H), (G′, H′))
```

is bijective.

(ii) Let $G$ be an $S$-group of finite presentation and $H$ an $S$-scheme of finite presentation with operator group
$G$; there then exists an index $j \in I$, an $S_{j}$-group of finite presentation $G_{j}$, an $S_{j}$-scheme of finite
presentation $H_{j}$ with operator group $G_{j}$ and a di-isomorphism of $S$-groups and $S$-schemes with operator groups
from $(G_{j} \times_{S_{j}} S, H_{j} \times_{S_{j}} S)$ onto $(G, X)$.

<!-- label: III.VI_B.10.14 -->

**Definition 10.15.** [^N.D.E-VI_B-102] *Let $T$ be a topology on $(Sch/S)$, less fine than the canonical topology.
Given an $S$-group scheme $G$ and an $S$-scheme $X$ with operator group $G$, one says that $X$ is a* formally
homogeneous space under $G$ *(relative to the topology $T$) if the morphism $\Phi : G \times_{S} X \to X \times_{S} X$,
defined by $(g, x) \mapsto (gx, x)$ for every $S' \to S$ and $g \in G(S')$, $x \in X(S')$, is an epimorphism in the
category of sheaves for the topology $T$, which amounts to saying that $\Phi$ is covering for the topology $T$ (cf. IV
4.4.3).*

*One says that $X$ is a* homogeneous space *if it is formally homogeneous and if moreover the morphism $X \to S$ is also
covering for the topology $T$.*

*In particular, one says that $X$ is a* formally principal homogeneous space under $G$ *if $\Phi$ is an isomorphism, and
that $X$ is a* principal homogeneous bundle *(or* $G$-torsor\*) if $\Phi$ is an isomorphism and if moreover the morphism
$X \to S$ is covering for the topology $T$ (cf. IV 5.1.5 and 5.1.6 (ii)).\*

<!-- label: III.VI_B.10.15 -->

**Proposition 10.16.** *We place ourselves in the situation considered at the beginning of 10.0. Let $j \in I$, $G_{j}$
an $S_{j}$-group and $X_{j}$ an $S_{j}$-scheme with operator group $G_{j}$. Suppose $G_{j}$ and $X_{j}$ of finite
presentation over $S_{j}$.*

*For $X = X_{j} \times_{S_{j}} S$ to be a homogeneous space (resp. a principal homogeneous bundle) under $G = G_{j}
\times_{S_{j}} S$ for the (fppf) topology, it is necessary and sufficient that there exist an index $i \geqslant j$ such
that $X_{i} = X_{j} \times_{S_{j}} S_{i}$ is a homogeneous space (resp. a principal homogeneous bundle) under $G_{i} =
G_{j} \times_{S_{j}} S_{i}$.*

<!-- label: III.VI_B.10.16 -->

Taking into account 10.14 and EGA IV₃, 8.8.2, 8.8.3 and 8.10.5, the statement follows from the property concerning
covering morphisms for the (fppf) topology recalled in 10.1.[^N.D.E-VI_B-103]

## 11. Affine group schemes

<!-- label: III.VI_B.11 -->

### 11.0. Reminders.

[^N.D.E-VI_B-C-104] Let $q : X \to S$ be a quasi-compact and quasi-separated morphism of schemes (cf. EGA IV₁, 1.1 &
1.2), and let $F$ be a quasi-coherent `O_X`-module. Recall that $q_{*}(F)$ is a quasi-coherent `O_S`-module (EGA I,
9.2.1). Moreover, by EGA III, 1.4.15 (completed by EGA IV₁, 1.7.21), one has point (c) below, and the proof of loc. cit.
also gives points (a) and (b):

(a) If $F$ is a filtered inductive limit of quasi-coherent submodules $F_{\alpha}$, then $q_{*}(F) = \lim_{\alpha}
q_{*}(F_{\alpha})$.

(b) If $E$ is a flat `O_S`-module, the canonical morphism $E \otimes_{O_{S}} q_{*}(O_{X}) \to q_{*} q*(E)$ is an
isomorphism.

(c) Let $p : S' \to S$ be a flat morphism, $q' : X' \to S'$ the morphism deduced from $q$ by base change, and $F '$ the
inverse image of $F$ on $X'$. Then the canonical morphism $p*q_{*}(F) \to q'_{*}(F ')$ is an isomorphism.

Indeed, let $U = \operatorname{Spec}(A)$ be an arbitrary affine open of $S$. By hypothesis, $q^{-1}(U)$ is the union of
affine opens $V_{i} = \operatorname{Spec}(B_{i})$, for $i = 1, \cdots, n$, and each intersection $V_{i} \cap V_{j}$ is
the union of finitely many affine opens `W_{ijk} = Spec(C_{ijk})`. Then $\Gamma(U, q_{*}(F)) = \Gamma(q^{-1}(U), F)$ is
the kernel of the morphism

```text
⊕_{i=1}^n Γ(V_i, F) → ⊕_{i,j,k} Γ(W_{ijk}, F).
```

Point (a) follows, since each of the terms above commutes with filtered inductive limits (since the $V_{i}$ and
$W_{ijk}$ are affine, hence quasi-compact). Let us prove (b): $E = \Gamma(U, E)$ is a flat $A$-module, and $\Gamma(U,
q_{*} q*(E))$ is the kernel $K(E)$ of the morphism

```text
⊕_{i=1}^n B_i ⊗_A E → ⊕_{i,j,k} C_{ijk} ⊗_A E
```

and since $E$ is flat over $A$, this kernel is identified with $K(A) \otimes_{A} E = O_{X}(q^{-1}(U)) \otimes_{A} E$.
Finally, if $U'$ is an arbitrary affine open of $S'$ above $U$, then $A' = O(U')$ is a flat $A$-algebra, and one obtains
as above that $F(q^{-1}(U)) \otimes_{A} A' \xrightarrow{\sim} F '(q'^{-1}(U))$.

**Notation.** Let $S$ be a scheme, $X$ an $S$-scheme, $f : X \to S$ the structural morphism; we set $\mathcal{A}(X) =
f_{*}(O_{X})$.

**Lemma 11.1.** *Let $X$ and $Y$ be two $S$-schemes quasi-compact and quasi-separated over $S$, $f : X \to S$ and $g : Y
\to S$ the structural morphisms. Then the canonical homomorphism*

```text
φ : 𝒜(X) ⊗_{O_S} 𝒜(Y) → 𝒜(X ×_S Y)
```

*is an isomorphism in each of the following cases:*[^N.D.E-VI_B-C-105]

*a) $f$ and $g$ are affine,*

*b) $g$ (or $f$) is flat and affine,*

*c) $g$ is flat and $f_{*}(O_{X})$ is a flat `O_S`-module.*

<!-- label: III.VI_B.11.1 -->

We shall assume, in case (b), that it is $g$ which is flat and affine. Set then $S' = \operatorname{Spec}
\mathcal{A}(X)$, $Y' = Y \times_{S} S'$, $g' = g \times_{S} S'$, and denote by $v$ the morphism $S' \to S$:

```text
       Y′ ───→ Y
       │        │
    g′ │        │ g
       ↓   v    ↓
Spec 𝒜(X) = S′ ──→ S
```

In cases (a) and (b), $g$ is affine and so, by EGA II, 1.5.2, one has:

```text
(1)        g′_*(O_{Y′}) = v* g_*(O_Y) = 𝒜(Y) ⊗_{O_S} O_{S′}.
```

One has the same equality in case (c), by 11.0 (c), since $S'$ is flat over $S$ and $g$ is quasi-compact and
quasi-separated.

On the other hand (EGA II 1.2.7), $f : X \to S$ factors through $v$ by means of a morphism $p : X \to S'$, and one has
$p_{*}(O_{X}) = O_{S'}$ and $X \times_{S} Y = X \times_{S'} Y'$. Since $f$ is quasi-separated, so is $p$ (EGA IV₁,
1.2.2), and since $f$ is quasi-compact and $v$ is quasi-separated, $p$ is also quasi-compact (EGA IV₁, 1.2.4). Consider
then the cartesian square:

```text
              p′
   X ×_S Y ────→ Y′
       │          │ g′
     p │          ↓
       ↓          S′
       X ────→
            p
```

In cases (b) and (c), $Y$ is flat over $S$, hence $Y'$ is flat over $S'$; applying 11.0 (c) again, one obtains:

```text
(2)        p′_*(O_{X ×_S Y}) = g′* p_*(O_X) = g′*(O_{S′}) = O_{Y′},
```

and one has the same equality in case (a), since in this case $p$ and $p'$ are isomorphisms.

Finally, $v$ being affine, one has, by EGA II, 1.4.7, $v_{*}(F \otimes_{O_{S}} O_{S'}) = F \otimes_{O_{S}}
\mathcal{A}(X)$ for every quasi-coherent `O_S`-module $F$. Combined with (2) and (1), this gives:

```text
𝒜(X ×_S Y) = v_* g′_* p′_*(O_{X ×_S Y}) = v_* g′_*(O_{Y′}) = v_*(𝒜(Y) ⊗_{O_S} O_{S′}) = 𝒜(Y) ⊗_{O_S} 𝒜(X).
```

∎

**Corollary 11.2.** *The functor $X \mapsto \operatorname{Spec} \mathcal{A}(X)$, from the full subcategory of $(Sch/S)$
formed of $S$-schemes $X$ flat, quasi-compact and quasi-separated over $S$, and such that $\mathcal{A}(X)$ is a flat
`O_S`-module, into that of $S$-schemes flat and affine over $S$, commutes with finite products, hence transforms
$S$-groups into $S$-groups.*

<!-- label: III.VI_B.11.2 -->

**Definition 11.3.** *Given an $S$-group $G$ flat, quasi-compact and quasi-separated over $S$, such that
$\mathcal{A}(G)$ is flat over `O_S`,[^N.D.E-VI_B-C-106] we shall denote by $G_{af}$, and call the* affine envelope *of
$G$, the $S$-group $G_{af} = \operatorname{Spec} \mathcal{A}(G)$.*

<!-- label: III.VI_B.11.3 -->

**Proposition 11.3.1.** [^N.D.E-VI_B-C-107] *The canonical morphism $\tau_{G} : G \to G_{af}$ is a morphism of
$S$-groups. Moreover, it satisfies the following universal property:*

*(i) For every morphism of $S$-schemes $\phi : G \to H$, where $H$ is affine over $S$, there exists a unique morphism of
$S$-schemes $\phi' : G_{af} \to H$ such that $\phi = \phi' \circ \tau_{G}$.*

*(ii) If moreover $H$ is an $S$-group and if $\phi$ is a morphism of $S$-groups, then so is $\phi'$.*

<!-- label: III.VI_B.11.3.1 -->

### 11.4.

[^N.D.E-VI_B-C-108] Let $E$ and $F$ be two quasi-coherent `O_S`-modules. Consider the $S$-functor
$\operatorname{Hom}_{O_{S}}(W(E), W(F))$ (cf. I, 3.1.4), i.e. for every $S$-scheme $f : X \to S$,

```text
Hom_{O_S}(W(E), W(F))(X) = Hom_{O_X}(W(E)_X, W(F)_X).
```

Moreover, by I, 4.6.2, one has $W(E)_{X} = W(f*(E))$ (and similarly for $F$) and

```text
Hom_{O_X}(W(f*(E)), W(f*(F))) = Hom_{O_X}(f*(E), f*(F)).
```

One thus obtains (using the adjunction formula for the last equality):

```text
(†)   Hom_{O_S}(W(E), W(F))(X) = Hom_{O_X}(f*(E), f*(F)) = Hom_{O_S}(E, f_* f*(F)).
```

**Proposition 11.5.** *Let $X$ be an $S$-scheme quasi-compact and quasi-separated over $S$, $f : X \to S$ the structural
morphism, $E$ and $E '$ two quasi-coherent `O_S`-modules. Suppose one of the two following conditions holds:*

*a) $f$ is affine,*

*b) $E$ is flat over `O_S`.*

*Then the canonical morphism $E \otimes_{O_{S}} \mathcal{A}(X) \to f_{*} f*(E)$ is an isomorphism, and one therefore
has*

```text
Hom_{O_S}(W(E ′), W(E))(X) = Hom_{O_S}(E ′, E ⊗_{O_S} 𝒜(X)).
```

<!-- label: III.VI_B.11.5 -->

Indeed, the second assertion follows from 11.4 and the first; this latter follows from EGA II, 1.4.7 in case (a), and
from 11.0 (b) in case (b).[^N.D.E-VI_B-C-109] ∎

### 11.6.

[^N.D.E-VI_B-C-110] Let $G$ be an $S$-group and $E$ a quasi-coherent `O_S`-module. To give $E$ a $G$-`O_S`-module
structure (i.e. an `O_S`-linear action of $G$ on $W(E)$, cf. I 4.7.1) is equivalent to giving a morphism of $S$-functors
in monoids $\rho : G \to \operatorname{End}_{O_{S}}(W(E))$ (indeed, such a $\rho$ necessarily sends $G$ into
$\operatorname{Aut}_{O_{S}}(W(E))$).

Now, by 11.4, giving a morphism of $S$-functors $\rho : G \to \operatorname{End}_{O_{S}}(W(E))$ is equivalent to giving
an element $\theta$ of $\operatorname{Hom}_{O_{G}}(f*(E), f*(E))$, which corresponds by adjunction to an element
$\delta$ of $\operatorname{Hom}_{O_{S}}(E, f_{*} f*(E))$, where one has denoted by $f$ the projection $G \to S$.

Let $m : G \times_{S} G \to G$ be the multiplication, $\delta_{G}$ the morphism $O_{G} \to m_{*}(O_{G \times_{S} G})$,
and $\phi$ the projection $G \times_{S} G \to S$ (which equals $f \circ m$). It is convenient to denote by $\boxtimes$
the "external" tensor product; one thus obtains a morphism

```text
id_E ⊠ δ_G :   f*(E) = E ⊠_{O_S} O_G → E ⊠_{O_S} m_*(O_{G×G})
```

and by abuse of notation, we shall denote again by $id_{E} \boxtimes \delta_{G}$ the composite of the preceding morphism
with the canonical morphism $E \boxtimes_{O_{S}} m_{*}(O_{G\times G}) \to m_{*} m* f*(E) = m_{*} \phi*(E)$.

On the other hand, designate by $h : G \to S$ a second copy of $f : G \to S$ and consider the following commutative
diagram, where $p$, $q$ denote the two projections:

```text
                  q
       G ×_S G ────→ G
            ╲        │
           p ╲    φ  │ h
              ╲      ↓
               G ──→ S
                  f
```

Denoting again by $\delta$ the morphism $E \to h_{*} h*(E)$, one obtains the morphism

```text
δ ⊠ id_{O_G} :   f*(E) = E ⊠_{O_S} O_G → h_* h*(E) ⊠_{O_S} O_G = f* h_* h*(E)
```

and by abuse we shall denote again by $\delta \boxtimes id_{O_{G}}$ the composite of this morphism with the canonical
morphism $f* h_{*} h*(E) \to p_{*} \phi*(E)$.

Then the condition that $\rho$ be compatible with the multiplication is equivalent to saying that, for every open $U$ of
$S$, the diagram below is commutative:

```text
                δ
    Γ(U, E) ─────────────────→ Γ(U ×_S G, E ⊠_{O_S} O_G)
        │                                │
      δ │                                │ id_E ⊠ δ_G
        ↓             δ ⊠ id_{O_G}       ↓
Γ(U ×_S G, E ⊠_{O_S} O_G) ────→ Γ(U ×_S G ×_S G, E ⊠_{O_S} O_G ⊠_{O_S} O_G).
```

(1)

Moreover, the unit section $\epsilon : S \to G$ induces a morphism $u$ from `O_G` to $\epsilon_{*} \epsilon*(O_{G}) =
\epsilon_{*}(O_{S})$, and the condition that $\rho$ preserves the unit elements is equivalent to the commutativity of
the diagram:

```text
                δ
    Γ(U, E) ─────────→ Γ(U ×_S G, E ⊠_{O_S} O_G)
        ╲                  ╱
       ≃ ╲                ╱ id_E ⊠ u
          ↓              ↙
       Γ(U ×_S S, E ⊠_{O_S} O_S).
```

(2)

One thus sees that giving $E$ a $G$-`O_S`-module structure is equivalent to giving a morphism of `O_S`-modules $\delta :
E \to f_{*} f*(E)$ satisfying conditions (1) and (2) above, and in this case the morphism $\theta : f*(E) \to f*(E)$,
deduced from $\delta$ by adjunction, is an isomorphism (since it corresponds to the isomorphism $G \times_{S} W(E)
\xrightarrow{\sim} G \times_{S} W(E)$ defined set-theoretically by $(g, x) \mapsto (g, gx)$; see also I, 6.5.4).

Suppose now that $G$ is flat, quasi-compact and quasi-separated over $S$, and that $\mathcal{A}(G)$ is a flat
`O_S`-module; then, by 11.1 (c), the canonical morphism $\mathcal{A}(G) \otimes_{O_{S}} \mathcal{A}(G) \to \mathcal{A}(G
\times_{S} G)$ is an isomorphism, and the morphism $\delta_{G} : \mathcal{A}(G) \to \mathcal{A}(G) \otimes_{O_{S}}
\mathcal{A}(G)$ will be denoted by `∆`.

If moreover $E \otimes_{O_{S}} \mathcal{A}(G) = f_{*} f*(E)$ (which is the case, by 11.5, if $G \to S$ is affine, or if
$E$ is flat over `O_S`), one obtains that conditions (1) and (2) are equivalent to the conditions below, which express
that $\delta : E \to E \otimes_{O_{S}} \mathcal{A}(G)$ makes $E$ a right $\mathcal{A}(G)$-comodule (cf. I 4.7.2):

(CM 1) Setting $A = \mathcal{A}(G)$, the diagram below is commutative:

```text
          δ
   E ────────→ E ⊗ A
   │            │
 δ │            │ id_E ⊗ ∆
   ↓ δ ⊗ id_A  ↓
   E ⊗ A ────→ E ⊗ A ⊗ A.
```

(CM 2) Denoting by $\eta : A \to O_{S}$ the morphism $\mathcal{A}(\epsilon)$, the diagram below is commutative:

```text
        δ
   E ───────→ E ⊗ A
    ╲           ╱
   ≃ ╲         ╱ id_E ⊗ η
      ↓       ↙
     E ⊗ O_S.
```

**Remark 11.6.A.** Recall that one denotes by $V(E)$ the vector fibration on $S$ representing the functor $V(E)$, i.e.
for every $S' \to S$, $V(E)(S') = \operatorname{Hom}_{O_{S'}}(E_{S'}, O_{S'})$. As one has, by I, 4.6.2, an
anti-isomorphism of $S$-functors in monoids $\operatorname{End}_{O_{S}}(W(E)) \simeq \operatorname{End}_{O_{S}}(V(E))$,
one sees that if $E$ is a left $G$-`O_S`-module, one has a right action $\mu : V(E) \times_{S} G \to V(E)$ of $G$ on
$V(E)$, defined set-theoretically by $(\phi g)(x) = \phi(gx)$, for every $g \in G(S')$, $x \in \Gamma(S', E_{S'})$ and
$\phi \in \operatorname{Hom}_{O_{S'}}(E_{S'}, O_{S'})$. One thus obtains commutative diagrams:

<!-- label: III.VI_B.11.6.A -->

```text
                μ × id_G                                         μ
V(E) ×_S G ×_S G ─────→ V(E) ×_S G                  V(E) ←──── V(E) ×_S G
        │                  │                          ╲             ↑
id × m  │                  │ μ                       ≃ ╲            │ id × ε
        ↓        μ         ↓                            ↓
   V(E) ×_S G ──────→ V(E)                                 V(E) ×_S S.
```

When $G$ is flat, quasi-compact and quasi-separated over $S$, when $\mathcal{A}(G)$ is a flat `O_S`-module, and when one
of the conditions of 11.5 is satisfied, one recovers similarly the conditions (CM 1) and (CM 2).

Consequently, we have obtained:

**Proposition 11.6.1.** *Let $G$ be an $S$-group flat, quasi-compact and quasi-separated over $S$, such that
$\mathcal{A}(G)$ is a flat `O_S`-module, and let $E$ be a quasi-coherent `O_S`-module.*

*(i) It amounts to the same to give an $\mathcal{A}(G)$-comodule structure $\delta : E \to E \otimes_{O_{S}}
\mathcal{A}(G)$ or a $G_{af}$-`O_S`-module structure on $E$ (i.e. an `O_S`-linear action of $G_{af}$ on $E$). By
composition with the morphism of $S$-groups $G \to G_{af}$, this defines a $G$-`O_S`-module structure on $E$.*

*(ii) If moreover $E$ is flat, every `O_S`-linear action of $G$ on $E$ factors through $G_{af}$ and corresponds to a
unique $\mathcal{A}(G)$-comodule structure on $E$.*

<!-- label: III.VI_B.11.6.1 -->

**Lemma 11.7.** *Let $G$ be an $S$-group flat, quasi-compact and quasi-separated over $S$, such that $A =
\mathcal{A}(G)$ is a flat `O_S`-module. Let $E$ be a quasi-coherent `O_S`-module, $\delta : E \to E \otimes A$ an
$A$-comodule structure, and $\rho : G \to \operatorname{Aut}_{O_{S}}(W(E))$ the action of $G$ on $E$ associated with
it.*

*Let `E_0` be a quasi-coherent `O_S`-submodule of $E$ such that the restriction $\delta_{0}$ of $\mu$ to `E_0` factors
through $E_{0} \to E_{0} \otimes A$, i.e. such that one has a commutative diagram:*

```text
   E_0 ────→ E
    │         │
δ_0 │         │ δ
    ↓         ↓
  E_0 ⊗ A ──→ E ⊗ A.
```

*(N.B. The morphism $E_{0} \otimes A \to E \otimes A$ is injective, since $A$ is flat over `O_S`.)*

*Then $\delta_{0}$ makes `E_0` an $\mathcal{A}(G)$-comodule, hence defines an action $\rho_{0}$ of $G$ on `E_0` (which
one will call the induced action on `E_0` by $\rho$, and one will say that `E_0` is* stable *under $\rho$).*

<!-- label: III.VI_B.11.7 -->

This follows immediately from the definitions and from 11.6. One will remark, however, that in general the canonical map
$W(E_{0}) \to W(E)$ is not a monomorphism. ∎

**Remark 11.7.bis.** [^N.D.E-VI_B-C-111] Let $G$ be a flat $S$-group and $E$ a quasi-coherent $G$-`O_S`-module. Denote
by $f$ the morphism $G \to S$ and by $\delta$ the morphism $E \to f_{*} f*(E)$ defined in 11.6. Let `E_0` be a
quasi-coherent `O_S`-submodule of $E$; since $f$ is flat, $f_{*} f*(E_{0})$ is an `O_S`-submodule of $f_{*} f*(E)$, and
similarly for $\phi = f \times f$. Consequently, if the restriction $\delta_{0}$ of $\delta$ to `E_0` factors through
$f_{*} f*(E_{0})$, then it makes `E_0` a $G$-`O_S`-module. In this case, one says that `E_0` is a $G$-stable submodule
of $E$.

<!-- label: III.VI_B.11.7.bis -->

**Definition 11.8.0.** [^N.D.E-VI_B-C-112] *Let $S$ be a scheme. An `O_S`-coalgebra is an `O_S`-module $C$ endowed with
two morphisms of `O_S`-modules `∆ : C → C ⊗ C` and $\epsilon : C \to O_{S}$, satisfying the following two axioms (cf. I
4.2):*

*(CO 1) `∆` is co-associative: the following diagram is commutative*

```text
            C ⊗ C
           ╱      ╲
        ∆ ╱        ╲ id ⊗ ∆
         ╱          ╲
        C            C ⊗ C ⊗ C
         ╲          ╱
        ∆ ╲        ╱ ∆ ⊗ id
           ╲      ╱
            C ⊗ C
```

*(CO 2): $\epsilon$ is a counit, i.e. the two following composites are the identity*

```text
        ∆          id ⊗ ε        ∼
   C ────→ C ⊗ C ────→ C ⊗ O_S ────→ C,
        ∆          ε ⊗ id         ∼
   C ────→ C ⊗ C ────→ O_S ⊗ C ────→ C.
```

*A (right) $C$-comodule is an `O_S`-module $E$ endowed with a morphism of `O_S`-modules $\mu : E \to E \otimes C$
satisfying the axioms (CM 1) and (CM 2) of 11.6.*

*One says that $C$ (resp. $E$) is a* quasi-coherent coalgebra *(resp. a* quasi-coherent comodule\*) if it is a
quasi-coherent `O_S`-module.\*

*Let $A$ be a commutative ring and $C$ an $A$-coalgebra; then $C^{\vee} = \operatorname{Hom}_{A}(C, A)$ is an
$A$-algebra. We shall denote by `ev` the natural evaluation map $C \otimes_{A} C^{\vee} \to A$.*

<!-- label: III.VI_B.11.8.0 -->

**Lemma 11.8.** *Let $C$ be an $A$-coalgebra, $V$ a $C$-comodule, $M$ an $A$-submodule of $V$. Suppose that $C$ is a
projective $A$-module.[^N.D.E-VI_B-C-113] Let $c(M)$ be the image of the morphism of $A$-modules*

```text
              μ ⊗ id              id ⊗ ev
θ :   M ⊗_A C^∨ ────→ V ⊗_A C ⊗_A C^∨ ────→ V.
```

*Then $c(M)$ is the smallest subcomodule of $V$ containing $M$, and is a finitely generated $A$-module if $M$ is. One
will say that $c(M)$ is the subcomodule generated by $M$.*

*Moreover, for every morphism of rings $A \to A'$, if one denotes by $M'$ the image of $M \otimes_{A} A'$ in $V' = V
\otimes_{A} A'$, then $c(M')$ is the image of $c(M) \otimes_{A} A'$ in $V'$, hence: "the formation of $c(M)$ commutes
with base change".*

<!-- label: III.VI_B.11.8 -->

First, $M \subset c(M)$ by (CM 2), and if $N$ is a subcomodule of $V$ containing $M$, one has $\mu(M) \subset N \otimes
C$ and therefore $c(M) \subset N$.

By hypothesis, $C$ is a direct factor of a free $A$-module $L$, with basis $(e_{i})_{i \in I}$. Denote by $\phi_{i}$ the
restriction to $C$ of the linear form $e^{*}_{i}$, defined by $e^{*}_{i}(e_{j}) = \delta_{ij}$. Let $x \in M$. One can
write:

```text
(1)      μ(x) = ∑_{i ∈ J} x_i ⊗ e_i,
```

where $x_{i} \in V$ and $J$ is a finite subset of $I$. Then $x_{i} = \theta(x \otimes \phi_{i})$ belongs to $c(Ax)$, and
one therefore has $c(Ax) = \sum_{i \in J} Ax_{i}$. Since $C$ is a direct factor of $L$, say $L = C \oplus R$, whence $V
\otimes L = (V \otimes C) \oplus (V \otimes R)$, one obtains that

```text
(c(Ax) ⊗ L) ∩ (V ⊗ C) = c(Ax) ⊗ C.
```

Consequently, $\mu(x)$ can also be written in the form

```text
(2)      μ(x) = ∑_{j ∈ J} x_j ⊗ b_j,
```

with $b_{j} \in C$. One can write `∆(b_j) = ∑_{i ∈ I} b_{ij} ⊗ e_i`, with $b_{ij} \in C$. Then, applying $\mu \otimes
id$ to (1) (resp. `id ⊗ ∆` to (2)) and using the axiom (CM 1), one obtains, for every $i \in J$:

```text
μ(x_i) = ∑_{j ∈ J} x_j ⊗ b_{ij} ∈ c(Ax) ⊗ C.
```

This shows that $c(M)$ is a subcomodule of $V$, and is therefore the smallest subcomodule of $V$ containing $M$.

It is clear that $c(M)$ is a finitely generated $A$-module if $M$ is: if $M = Ax_{1} + \cdots + Ax_{n}$ and $\mu(x_{k})
= \sum_{i} x_{ik} \otimes e_{i}$, then $c(M)$ is generated by the $x_{ik}$, for $k = 1, \cdots, n$ and $i$ running
through a finite subset of $I$.

Finally, let $A \to A'$ be a morphism of rings and let $M'$ be the image of $M \otimes A'$ in $V' = V \otimes A'$. Then
$c(M')$ (resp. the image of $c(M) \otimes A'$ in $V'$) is the image of the morphism $\theta'$ below (resp. of the
composite $\theta' \circ \tau$):

```text
                   τ                    θ′
M ⊗ A′ ⊗ C^∨ ────→ M ⊗ Hom_A(C, A′) ────→ V′.
```

Now, these two morphisms have the same image. Indeed, let $\psi \in \operatorname{Hom}_{A}(C, A')$ and $x \in M$. Set
$\mu(x) = \sum_{i \in J} x_{i} \otimes e_{i}$. Then

```text
θ′(x ⊗ ψ) = ∑_{i ∈ J} ψ(e_i) x_i
```

is the image by $\theta' \circ \tau$ of the element $\sum_{i \in J} x \otimes \psi(e_{i}) \otimes \phi_{i}$ of $M
\otimes A' \otimes C^{\vee}$. This proves the lemma. ∎

Moreover, one has the following proposition:

**Proposition 11.8.bis.** [^N.D.E-VI_B-C-114] *Let $A$ be a noetherian ring, $C$ an $A$-coalgebra flat over $A$, $V$ a
$C$-comodule, and $M$ a finitely generated $A$-submodule of $V$. Then there exists a subcomodule $W$ of $V$, finitely
generated over $A$, containing $M$.*

<!-- label: III.VI_B.11.8.bis -->

Indeed, since $M$ is finitely generated, so is `∆_V(M)`, hence there exists a finitely generated $A$-submodule $M'$ of
$V$ such that `∆_V(M) ⊂ M′ ⊗_A C`. Let $\pi$ be the projection $V \to V/M'$ and `∆̄_V = (π ⊗ id_C) ∆_V`, and let

```text
W = {x ∈ V | ∆̄_V(x) ∈ M′ ⊗_A C} = Ker ∆̄_V;
```

this is an $A$-submodule of $V$ containing $M$ and contained in $M'$ (since `x = (id_V ⊗ ε) ∆_V(x)`), hence finitely
generated over $A$. Moreover, `(∆̄_V ⊗ id_C) ∆_V = (π ⊗ ∆_C) ∆_V` vanishes on $W$, i.e. `∆_V(W)` is contained in the
kernel $K$ of `(∆̄_V ⊗ id_C)`. But since $C$ is flat over $A$, one has $K = W \otimes C$, hence $W$ is a subcomodule of
$V$. ∎

**Lemma 11.8.1.** [^N.D.E-VI_B-C-115] *Let $C$ be an $A$-coalgebra, $V$ a $C$-comodule, $M$ an $A$-submodule of $V$, and
$f : A \to A'$ a faithfully flat morphism of rings. Suppose that $C' = C \otimes A'$ is a projective $A'$-module.*

*(i) Then there exists a smallest subcomodule $t(M)$ of $V$ containing $M$, and $t(M)$ is a finitely generated
$A$-module if $M$ is. Moreover, "the formation of $t(M)$ commutes with base change".*

*(ii) More precisely, $C$ is a projective $A$-module, and one has $t(M) = c(M)$.*

<!-- label: III.VI_B.11.8.1 -->

*Proof.* (ii) By [RG71] (see Proposition 11.8.2 below), $C$ is a projective $A$-module. One can therefore apply Lemma
11.8: $c(M)$ is the smallest subcomodule of $V$ containing $M$, it is a finitely generated $A$-module if $M$ is, and its
formation commutes with base change.

To avoid an anachronism ([RG71] being subsequent to SGA 3), let us sketch a direct proof of point (i). Since $A \to A'$
is flat, $M' = M \otimes A'$ is an $A'$-submodule of $V' = V \otimes A'$, and, since $C'$ is a projective $A'$-module,
$c(M')$ is the smallest subcomodule of $V'$ containing $M'$. Denote by $V' \otimes A'$ and $A' \otimes V'$ the two $A'
\otimes A'$-comodule structures on $V'' = V' \otimes_{A'} (A' \otimes A')$ obtained by the two base changes $A'
\Rightarrow A' \otimes A'$, $a' \mapsto a' \otimes 1$ and $a' \mapsto 1 \otimes a'$. The $A'$-comodule $V'$ is equipped
with an isomorphism of $A' \otimes A'$-comodules $\phi : V' \otimes A' \xrightarrow{\sim} A' \otimes V'$, $(x \otimes
a') \otimes b' \mapsto b' \otimes (x \otimes a')$, which is a descent datum, i.e. which satisfies $\phi_{31} = \phi_{32}
\circ \phi_{21}$.

Since $M' = M \otimes A'$, $\phi$ sends $M' \otimes A'$ onto $A' \otimes M'$, and therefore $c(M' \otimes A')$ onto
$c(A' \otimes M')$. Since the formation of $c(M')$ commutes with base change, one has $c(M' \otimes A') = c(M') \otimes
A'$ and $c(A' \otimes M') = A' \otimes c(M')$. One therefore has

```text
φ(c(M′) ⊗ A′) = A′ ⊗ c(M′)
```

and it follows that $\phi$ equips $c(M')$ with a descent datum. By (fpqc) descent, there exists a unique subcomodule
$t(M)$ of $V$ such that $c(M') = t(M) \otimes A'$, and $t(M)$ contains $M$ since $t(M) \otimes A'$ contains $M'$.
Moreover, if $N$ is a subcomodule of $V$ containing $M$, then $N$ contains $t(M)$, since $N \otimes A'$ contains $c(M')
= t(M) \otimes A'$. Hence $t(M)$ is the smallest subcomodule of $V$ containing $M$.

Finally, let $A \to B$ be a morphism of rings. Let $B' = B \otimes A'$ and let `M_B` (resp. $M'_{B'}$) be the image of
$M \otimes B$ in $V_{B} = V \otimes B$ (resp. of $M' \otimes_{A'} B'$ in $V \otimes B'$); then $M_{B} \otimes_{B} B' =
M'_{B'}$. On the one hand, the preceding construction, applied to `C_B` and to the morphism $B \to B'$, gives:

```text
c(M_B ⊗_B B′) = t(M_B) ⊗_B B′ = t(M_B) ⊗ A′.
```

On the other hand, since the formation of $c(M')$ commutes with base change, $c(M'_{B'})$ is the image in $V'
\otimes_{A'} B' = V \otimes B \otimes A'$ of

```text
c(M′) ⊗_{A′} B′ = t(M) ⊗ B ⊗ A′.
```

It follows that $t(M_{B})$ is the image in `V_B` of $t(M) \otimes B$. ∎

**Proposition 11.8.2 (Gruson–Raynaud).** *Let $f : A \to A'$ be a faithfully flat morphism; then $f$ "descends
projectivity", i.e. if $M$ is an $A$-module and if $M \otimes_{A} A'$ is a projective $A'$-module, then $M$ is a
projective $A$-module.*

<!-- label: III.VI_B.11.8.2 -->

Indeed, by [RG71] II 2.5.1, $f$ "descends the Mittag-Leffler condition", and therefore, by loc. cit. II 3.1.3, $f$
descends projectivity.[^N.D.E-VI_B-C-116] ∎

**Proposition 11.9.** [^N.D.E-VI_B-C-117] *Let $C$ be an `O_S`-coalgebra, $E$ a $C$-comodule, $F$ an `O_S`-submodule of
$E$, all quasi-coherent. Suppose given a covering of $S$ by affine opens $U_{\alpha} = \operatorname{Spec} A_{\alpha}$,
and for each $\alpha$, a faithfully flat morphism of rings $A_{\alpha} \to A'_{\alpha}$ such that $\Gamma(U_{\alpha}, C)
\otimes_{A_{\alpha}} A'_{\alpha}$ is a projective $A'_{\alpha}$-module.[^VI_B-C-11-9]*

*Then there exists a smallest quasi-coherent subcomodule $t(F)$ of $E$ containing $F$, and $t(F)$ is a finitely
generated `O_S`-module if $F$ is. Moreover, for every base change $S' \to S$, if one denotes by $F '$ the image of $F
\otimes O_{S'}$ in $E ' = E \otimes O_{S'}$, then $t(F ')$ is the image of $t(F) \otimes O_{S'}$ in $E '$, i.e. "the
formation of $t(F)$ commutes with base change".*

<!-- label: III.VI_B.11.9 -->

*Proof.* For each $\alpha$, the $O_{U_{\alpha}}$-module $\mathcal{T}_{\alpha}$ associated with the $A_{\alpha}$-module
$T_{\alpha} = t(\Gamma(U_{\alpha}, F))$ is, by 11.8.1 (i), the smallest quasi-coherent subcomodule of $E|_{U_{\alpha}}$
containing $F|_{U_{\alpha}}$, and is a finitely generated $O_{U_{\alpha}}$-module if $F|_{U_{\alpha}}$ is.

For all $\alpha, \beta$, set $U_{\alpha \beta} = U_{\alpha} \cap U_{\beta}$. Since the construction of $t(M)$ commutes
with base change, one has, for all $\alpha, \beta$, canonical isomorphisms of $O_{U_{\alpha \beta}}$-modules

```text
φ_{αβ} : 𝒯_β ⊗_{A_β} O_{U_{αβ}} ⥲ 𝒯_α ⊗_{A_α} O_{U_{αβ}}
```

which satisfy the cocycle condition $\phi'_{\alpha \gamma} = \phi'_{\alpha \beta} \circ \phi'_{\beta \gamma}$, where
$\phi'_{\alpha \gamma}$ (resp. ⋯) denotes the restriction of $\phi_{\alpha \gamma}$ (resp. ⋯) to $U_{\alpha} \cap
U_{\beta} \cap U_{\gamma}$.

Consequently, the $\mathcal{T}_{\alpha}$ glue together into a quasi-coherent subcomodule $t(F)$ of $E$ containing $F$.
We leave to the reader the task of verifying that $t(F)$ is the smallest quasi-coherent subcomodule of $E$ containing
$F$, and that its formation commutes with base change. ∎

**Definition 11.9.1.** [^N.D.E-VI_B-C-118] *Let $S$ be a scheme and $P$ a quasi-coherent `O_S`-module. The following
conditions are equivalent:*

*(i) For every affine open $U$ of $S$, $\Gamma(U, P)$ is a projective $O_{S}(U)$-module.*

*(ii) There exists a covering $(U_{\alpha})$ of $S$ by affine opens such that each $\Gamma(U_{\alpha}, P)$ is a
projective $O_{S}(U_{\alpha})$-module.*

*(iii) There exists a covering $(U_{\alpha})$ of $S$ by affine opens, and faithfully flat morphisms of rings $A_{\alpha}
= O_{S}(U_{\alpha}) \to A'_{\alpha}$, such that, for each $\alpha$, $\Gamma(U_{\alpha}, P) \otimes_{A_{\alpha}}
A'_{\alpha}$ is a projective $A'_{\alpha}$-module.*

<!-- label: III.VI_B.11.9.1 -->

Indeed, it is clear that (i) ⇒ (ii) ⇒ (iii). Conversely, if (iii) is satisfied, 11.8.2 implies that each
$\Gamma(U_{\alpha}, P)$ is a projective $O_{S}(U_{\alpha})$-module, whence (ii). Finally, suppose (ii) satisfied and let
$V = \operatorname{Spec} A$ be an arbitrary affine open; it is covered by finitely many affine opens $V_{1}, \cdots,
V_{n}$, where each $V_{i} = \operatorname{Spec} A_{i}$ is contained in at least one $V \cap U_{\alpha}$, so that
$\Gamma(V_{i}, P)$ is a projective $A_{i}$-module. Let $A' = A_{1} \times \cdots \times A_{n}$; then $A \to A'$ is
faithfully flat and $\Gamma(V, P) \otimes_{A} A'$ is a projective $A'$-module. Hence, by 11.8.2, $\Gamma(V, P)$ is a
projective $A$-module.

When these equivalent conditions are satisfied, one says that $P$ is a *locally projective* `O_S`-module.

**Corollary 11.10.** *Let $S$ be a quasi-compact and quasi-separated scheme, $G$ an $S$-group, and $\rho$ a linear
action of $G$ on a quasi-coherent `O_S`-module $E$. Suppose that:*

*(i) $G$ satisfies one of the following conditions:*

*a) $G$ is affine and flat over $S$,*

*b) $G$ is flat, quasi-compact and quasi-separated over $S$, and $E$ is flat;*

*(ii) $\mathcal{A}(G)$ is a locally projective `O_S`-module.*

*Then $E$ is an inductive limit of a filtered increasing family of quasi-coherent finitely generated `O_S`-submodules of
$E$, stable under $G$.*

<!-- label: III.VI_B.11.10 -->

By hypothesis (i) and 11.6.1, $E$ is equipped with an $\mathcal{A}(G)$-comodule structure. On the other hand, since $S$
is quasi-compact and quasi-separated, $E$ is the inductive limit of its finitely generated quasi-coherent submodules
(EGA I, 9.4.9 and EGA IV₁, 1.7.7). Consequently, the corollary follows from Proposition 11.9, applied to the coalgebra
$\mathcal{A}(G)$. ∎

Moreover, one has the following proposition:

**Proposition 11.10.bis.** [^N.D.E-VI_B-C-119] *Let $S$ be a noetherian scheme, $G$ an $S$-group flat, quasi-compact and
quasi-separated over $S$, $E$ a quasi-coherent $G$-`O_S`-module, $M$ a coherent `O_S`-submodule of $E$. Then $M$ is
contained in a coherent `O_S`-submodule stable under $G$.*

<!-- label: III.VI_B.11.10.bis -->

*Proof.* Denote by $f$ the morphism $G \to S$ and by $\tau$ the adjunction morphism $E \to f_{*} f*(E)$. By 11.6, the
$G$-`O_S`-module structure on $E$ is given by an automorphism $\theta$ of the `O_G`-module $f*(E)$, such that the
morphism $\delta = \theta \circ \tau$ satisfies conditions (1) and (2) of 11.6. (The situation considered in [Th87] is
more general, in that the author considers a $G$-scheme $X$ and a $G$-equivariant `O_X`-module $E$ (cf. Exp. I, Section
6); here $X = S$ equipped with the trivial action of $G$.)

Since $S$ is noetherian, $E$ is the filtered inductive limit of its coherent submodules $F_{\alpha}$ (cf. EGA I, 9.4.9).
Then $f*(E)$ is the filtered inductive limit of the $f*(F_{\alpha})$, which are submodules of $f*(E)$ since $f$ is flat.
Since, moreover, $f$ is quasi-compact and quasi-separated, by 11.0, the `O_S`-module $f_{*} f*(E)$ is quasi-coherent and
is the filtered inductive limit of the quasi-coherent submodules $f_{*} f*(F_{\alpha})$. Consequently, $E$ is the
filtered inductive limit of the quasi-coherent `O_S`-submodules $E_{\alpha}$, where $E_{\alpha}$ denotes the inverse
image by $\delta$ of $f_{*} f*(F_{\alpha})$, i.e. the kernel of the composite morphism

```text
                δ                       
δ_α :   E ────→ f_* f*(E) ────→ f_* f*(E/F_α).
```

Since $M$ is coherent and $S$ noetherian, every increasing sequence of submodules of $M$ is stationary, so $M$ is
contained in some $E_{\alpha}$. Let us show that each $E_{\alpha}$ is coherent and $G$-stable.

Let $u$ be the morphism $f*(E) \to \epsilon_{*}(E)$ corresponding by adjunction to the identity morphism from $E$ to
$f_{*} \epsilon_{*}(E) = E$; then the composite morphism

```text
         τ                f_*(u)
E ────→ f_* f*(E) ────→ f_* ε_*(E) = E
```

is the identity (cf. 11.6 (2)). Since one has a commutative diagram:

```text
            δ                  f_*(u)
   E_α ────→ f_* f*(F_α) ────→ F_α
    │                              │
i_α │                              │ j_α
    ↓        τ          f_*(u)     ↓
   E   ────→ f_* f*(E) ────→ E,
```

where $i_{\alpha}$ (resp. $j_{\alpha}$) denotes the inclusion of $E_{\alpha}$ (resp. $F_{\alpha}$) into $E$, one deduces
that $i_{\alpha}$ factors through $j_{\alpha}$, i.e. $E_{\alpha}$ is a submodule of $F_{\alpha}$, hence is coherent.

Let us finally show that $E_{\alpha}$ is $G$-stable (cf. 11.7.bis). Designate by $h : G \to S$ a second copy of $f : G
\to S$ and consider the following commutative diagram:

```text
              q
   G ×_S G ────→ G
        ╲         │
       p ╲      φ │ h
          ↘       ↓
           G ───→ S.
              f
```

Then the exact sequence

```text
                                 δ_α
0 ────→ E_α ────→ E ────→ h_* h*(E/F_α)
```

gives, since $f$ is flat, the exact sequence

```text
(†)   0 ────→ f_* f*(E_α) ────→ f_* f*(E) ──f_* f*(δ_α)──→ f_* f* h_* h*(E/F_α).
```

Moreover, since $h$ is quasi-compact and quasi-separated, and $f$ flat, the canonical morphism

```text
f* h_* h*(E/F_α) → p_* q* h*(E/F_α) = p_* φ*(E/F_α)
```

is an isomorphism, so that the right-hand term in (†) is $\phi_{*} \phi*(E/F_{\alpha})$. Resuming the notations of 11.6
and denoting by $\pi_{\alpha}$ the projection $E \to E/F_{\alpha}$, one obtains the commutative diagram below, whose
bottom line is exact:

```text
                              δ                       
   E_α ────────────────────→ f_* f*(E)
    │                                  │ f_*(f*(π) ⊠ δ_G)
  δ │                                  ↓
f_* f*(E_α) ────→ f_* f*(E) ──f_* f*(δ_α)──→ φ_* φ*(E/F_α)
```

and since $f_{*}(f*(\pi) \boxtimes \delta_{G}) \circ \delta$ vanishes on $E_{\alpha}$, it follows that $\delta$ sends
$E_{\alpha}$ into $f_{*} f*(E_{\alpha})$, i.e. that $E_{\alpha}$ is $G$-stable. The proposition is proved. ∎

**Remark 11.10.1.** [^N.D.E-VI_B-C-120] In 11.8, it does not suffice to assume that $C$ be a flat $A$-module, even if
$A$ is a principal ring. Indeed, one has the following counterexamples, which were pointed out (independently) to us by
O. Gabber and J.-P. Serre.

<!-- label: III.VI_B.11.10.1 -->

(a) Let $(A, \mathfrak{m})$ be a discrete valuation ring, $K$ its field of fractions, and $G$ the "extension by zero"
$A$-group of the $K$-group $(\mathbb{Z}/2\mathbb{Z})_{K}$. Then the constant group $(\mathbb{Z}/2\mathbb{Z})_{A}$, and
hence also its subgroup $G$, acts on the free $A$-module $V$ with basis $v_{1}, v_{2}$ by exchanging $v_{1}$ and
$v_{2}$. Then $Av_{1}$ is not a sub-$G$-module of $V$, but it is the intersection of the sub-$G$-modules $Av_{1} +
\mathfrak{m}^{n} v_{2}$, for $n \in \mathbb{N}^{*}$. Hence there does not exist a smallest sub-$G$-module of $V$
containing $v_{1}$.

(b) Let $A$ be an integral ring, distinct from its field of fractions $K$, and let $G$ be the flat affine $A$-group
corresponding to the Hopf algebra

```text
𝒜(G) = {P ∈ K[T] | P(0) ∈ A},
```

the comultiplication, resp. the counit and the antipode, being defined by `∆(T) = T ⊗ 1 + 1 ⊗ T`, resp. $\epsilon(T) =
0$ and $\tau(T) = -T$. (N.B. One thus has $G \otimes_{A} K = G_{a,K}$.)

Let $V$ be the free $A$-module $Av_{1} \oplus Av_{2}$ and $u$ the endomorphism of $V$ defined by $u(v_{1}) = v_{2}$,
$u(v_{2}) = 0$, so that $u^{2} = 0$. Then $V$ is equipped with an $\mathcal{A}(G)$-comodule structure, defined by

```text
μ(m) = 1 ⊗ m + T ⊗ u(m).
```

The sub-$G$-modules of $V$ containing $v_{1}$ are exactly the sub-$A$-modules of the form $Av_{1} \oplus Iv_{2}$, for
$I$ a non-zero ideal of $A$; their intersection is $Av_{1}$, which is not a sub-$G$-module. Hence there does not exist a
smallest sub-$G$-module of $V$ containing $v_{1}$. (Note moreover that $C = A \oplus K \cdot T$ is a sub-coalgebra of
$\mathcal{A}(G)$, flat over $A$, and that the coaction $\mu : V \to V \otimes \mathcal{A}(G)$ factors through $V \otimes
C$, so one also obtains a counterexample for the "very simple" coalgebra $C$.)

Finally, note that the two preceding examples are particular cases of the following construction. Let $A$ be an integral
ring, distinct from its field of fractions $K$, let $B$ be an $A$-Hopf algebra, free over $A$. Denote by $\epsilon : B
\to A$ the augmentation of $B$ and $I = Ker(\epsilon)$ the augmentation ideal. Since $B = A \cdot 1 \oplus I$, one
easily sees that $B' = {b \in B \otimes_{A} K | \epsilon(b) \in A}$ is a sub-Hopf algebra of `B_K`. If $V$ is a
$B$-comodule, free with basis $(v_{1}, \cdots, v_{n})$ as $A$-module, and if $\mu_{V}(v_{1}) \neq v_{1} \otimes 1$, then
$Av_{1}$ is not a subcomodule of $V$ but it is the intersection of the subcomodules $Av_{1} + I \cdot V$, for $I$
running through the non-zero ideals of $A$. Hence there does not exist a smallest subcomodule of $V$ containing $v_{1}$.

**Proposition 11.11.** *Let $G$ be an algebraic group over the field $k$. The following conditions are equivalent:*

*(i) $G$ is affine.*

*(ii) $G$ is quasi-affine.*

*(iii) $G$ acts faithfully on a quasi-affine $k$-scheme $X$.*

*(iv) $G$ acts linearly and faithfully on a $k$-vector space (not necessarily of finite dimension).*

*(v) $G$ is isomorphic to a closed subgroup of a group $GL(n)_{k}$.*

<!-- label: III.VI_B.11.11 -->

*Proof.* One has (i) ⇒ (ii) trivially, and (ii) ⇒ (iii), since $G$ acts faithfully on itself by translations.

Suppose that $G$ acts faithfully on the right on a quasi-affine $k$-scheme $X$.[^N.D.E-VI_B-C-121] Since $X$ is
quasi-affine, it is separated and quasi-compact.[^N.D.E-VI_B-C-122] Similarly, $G$ is separated (VI_A 0.3) and
quasi-compact (since of finite type over $k$). Hence, by 11.1 (c), one has canonical isomorphisms:

```text
O(X × G) = O(X) ⊗ O(G)     and     O(X × G × G) = O(X) ⊗ O(G) ⊗ O(G).
```

One deduces that the morphism $\mu : O(X) \to O(X) \otimes O(G)$ induced by the morphism $X \times G \to X$ equips
$O(X)$ with a right $O(G)$-comodule structure, i.e. $G$ acts linearly on the left on the $k$-algebra $O(X)$.
Consequently, $G$ also acts on the right on the affine envelope $X_{af} = \operatorname{Spec} O(X)$ of $X$, and the
canonical morphism $X \to X_{af}$ is $G$-equivariant.

Moreover, $X$ being quasi-affine, $X \to X_{af}$ is an open immersion (EGA II, 5.1.2), hence a fortiori $G$ acts
faithfully on $X_{af}$. One thus obtains that the linear (left) action of $G$ on the $k$-algebra $O(X) = O(X_{af})$ is
faithful. This proves the implication (iii) ⇒ (iv).

Suppose now that $G$ acts faithfully on a $k$-vector space $V$. Then, by virtue of 11.10, $V$ is the inductive limit of
finite-dimensional vector subspaces $V_{i}$, stable under the action of $G$. If $K_{i}$ is the kernel of the induced
action of $G$ on $V_{i}$, i.e. of the morphism $G \to \operatorname{Aut}(V_{i})$, then $K_{i}$ is a closed subscheme of
$G$, and the hypothesis that $G$ acts faithfully is expressed by the fact that the intersection of the $K_{i}$ is the
unit subgroup of $G$. Since $G$ is noetherian, it follows that one of the $K_{i}$ is already reduced to the unit group,
hence that $G \to \operatorname{Aut}(V_{i})$ is a monomorphism. It is therefore a closed immersion by virtue of 1.4.2,
which proves that (iv) ⇒ (v). Since (v) ⇒ (i) trivially, this proves 11.11. ∎

**Remark 11.11.1.** One can generalize 11.11 as follows. Let $S$ be a regular locally noetherian scheme of dimension
$\leq 1$, and $G$ a group scheme flat, quasi-compact and quasi-separated over $S$. (In this case, $\mathcal{A}(G)$ is a
torsion-free `O_S`-module, hence flat.)

<!-- label: III.VI_B.11.11.1 -->

(a) One then has the equivalence of the following conditions:[^N.D.E-VI_B-C-123]

(i) $G$ is affine over $S$.

(ii) $G$ is quasi-affine over $S$.

(iii) $G$ acts faithfully on a quasi-affine and flat $S$-scheme.

(iv) $G$ acts linearly and faithfully on a flat quasi-coherent `O_S`-module.

(b) If moreover $G$ is of finite type over $S$ and $S$ noetherian, these conditions imply that $G$ is isomorphic to a
closed subgroup of an $\operatorname{Aut}(E)$, where $E$ is a finitely generated locally free
`O_S`-module.[^N.D.E-VI_B-C-124]

**Lemma 11.12.** *Let $k$ be a field, $G$ an affine $k$-group. Set $A = \mathcal{A}(G)$. Given $x \in A$, there exists a
finitely generated $k$-subalgebra $B$ of $A$ such that $x \in B$, that `∆(B) ⊂ B ⊗_k B`, and $u(B) \subset B$, where $u$
denotes the involution of $A$ corresponding to the inversion morphism of $G$.[^N.D.E-VI_B-C-125]*

<!-- label: III.VI_B.11.12 -->

One can suppose $x \neq 0$; then `∆(x) ≠ 0` since `(ε ⊗ id) ∆(x) = x`, where $\epsilon$ denotes the augmentation
(counit) of $A$. Write

```text
(1)     ∆(x) = ∑_{j=1}^n e_j ⊗ a_j     with n minimal,
```

in which case the $e_{j}$ (resp. $a_{j}$) are linearly independent. Complete $(e_{1}, \cdots, e_{n})$ into a basis
$(e_{i})_{i \in I}$ of $A$ and set, for $j \in J = {1, \cdots, n}$,

```text
∆(e_j) = ∑_{i ∈ I} e_i ⊗ b_{ij}.
```

Applying `∆ ⊗ id` and `id ⊗ ∆` to (1), one obtains from the axiom (CO 1) of 11.8.0 (see also (HA 1) in I 4.2) the
equalities:

```text
∑_{j ∈ J} e_j ⊗ ∆(a_j) = ∑_{ℓ ∈ J} ∆(e_ℓ) ⊗ a_ℓ = ∑_{i ∈ I} e_i ⊗ (∑_{ℓ ∈ J} b_{iℓ} ⊗ a_ℓ).
```

Since the $e_{i}$ are linearly independent, it follows that

```text
(2)     ∀ j ∈ J,     ∆(a_j) = ∑_{ℓ ∈ J} b_{jℓ} ⊗ a_ℓ.
```

Let then $B$ be the finitely generated $k$-subalgebra of $A$ generated by the $b_{ij}$ and the $u(b_{ij})$, for $i, j
\in J$. It is clear that $u(B) = B$.

Applying `∆ ⊗ id` and `id ⊗ ∆` to (2), one obtains further from (CO 1) the equalities:

```text
∑_{ℓ ∈ J} ∆(b_{jℓ}) ⊗ a_ℓ = ∑_{i ∈ J} b_{ji} ⊗ ∆(a_i) = ∑_{i, ℓ ∈ J} b_{ji} ⊗ b_{iℓ} ⊗ a_ℓ,
```

and since the $a_{\ell}$ are linearly independent, one deduces that

```text
(3)     ∀ j, ℓ ∈ J,     ∆(b_{jℓ}) = ∑_{i ∈ J} b_{ji} ⊗ b_{iℓ}.
```

Since `∆ ∘ u = (u × u) ∘ v ∘ ∆`, where $v(a \otimes b) = b \otimes a$, one therefore also has

```text
(4)     ∀ j, ℓ ∈ J,     ∆(u(b_{jℓ})) = ∑_{i ∈ J} u(b_{iℓ}) ⊗ u(b_{ji}).
```

Since `∆` is an algebra homomorphism, one deduces from (3) and (4) that `∆(B) ⊂ B ⊗_k B`. Finally, the axiom (CO 2) of
11.8.0 (see also (HA 2) in I, 4.2) shows that $a_{j} = \sum_{i \in I} \epsilon(a_{j}) b_{ij}$ and that $x = \sum_{j \in
J} \epsilon(e_{j}) a_{j}$, so that $x \in B$. ∎

**Proposition 11.13.** *Let $k$ be a field and $G$ an affine $k$-group with algebra $A$. Then $G$ is a projective limit
of an increasing filtered system of finitely generated affine $k$-groups, whose transition morphisms are faithfully
flat.*

<!-- label: III.VI_B.11.13 -->

If $B$ and $B'$ are two finitely generated subalgebras of $A$ stable under `∆` and $u$, then so is the subalgebra
generated by $B$ and $B'$. Hence, by Lemma 11.12, $A$ is the inductive limit of a filtered increasing family $(B_{i})_{i
\in I}$ of finitely generated subalgebras stable under `∆` and $u$. Then each $B_{i}$, equipped with the restriction of
$u$ and the morphism $B_{i} \to B_{i} \otimes_{k} B_{i}$ deduced from `∆`, is a Hopf algebra, hence by I 4.2 it is the
algebra of an affine $k$-group $G_{i}$, of finite type over $k$. Finally, since $A = \lim B_{i}$, one has $G = \lim
G_{i}$ (cf. EGA IV₃ 8.2.3). The transition morphisms are faithfully flat by the following lemma:

**Lemma 11.14.** *Let $k$ be a field, $u : G \to H$ a morphism between finitely generated affine $k$-groups, and
$u^{\natural} : B \to A$[^N.D.E-VI_B-C-126] the corresponding morphism of $k$-algebras. For $u$ to be faithfully flat,
it is necessary and sufficient that $u^{\natural}$ be injective.*

<!-- label: III.VI_B.11.14 -->

The condition is obviously necessary (cf. EGA 0_I 6.6.1). Let us show it is sufficient. Set $N = Ker u$. Then, by VI_A,
3.3.2 and 5.4.1, $G/N$ is a finitely generated $k$-group and $u$ factors as $G --p--> G/N --v--> H$, where $p$ is
faithfully flat and $v$ is a closed immersion. Hence, since $H$ is an affine scheme, $G/N$ is an affine scheme and the
morphism $v^{\natural} : B \to O(G/N)$ is surjective (cf. EGA I 4.2.3). Now, since $u^{\natural}$ is assumed injective,
and since $u^{\natural} = p^{\natural} \circ v^{\natural}$, then $v^{\natural}$ is also injective: it is therefore an
isomorphism, as is $v$, and since $p$ is faithfully flat, so is $u$. ∎

**Definition 11.15.** [^N.D.E-VI_B-C-127] *Let $k$ be a field, $G$ a quasi-compact $k$-group and $V$ a $k$-vector space
equipped with a $k$-linear action of $G$, hence with an $\mathcal{A}(G)$-comodule structure $\delta : V \to V \otimes
\mathcal{A}(G)$, by 11.6.1. Let $v \in V$ be non-zero. The following conditions are equivalent:*

*(i) There exists $\lambda \in \mathcal{A}(G)$ (necessarily unique) such that $\delta(v) = v \otimes \lambda$.*

*(ii) For every $k$-algebra $R$ and every $g \in G(R)$, one has $g \cdot v \in Rv$ (i.e. there exists $f \in R$,
necessarily unique, such that one has in $V \otimes R$ the equality $g \cdot v = v \otimes f$).*

<!-- label: III.VI_B.11.15 -->

Indeed, it is clear that (i) ⇒ (ii). Conversely, if (ii) is satisfied and one applies it to $R = \mathcal{A}(G)$ and $g
= id_{\mathcal{A}(G)}$, one obtains that there exists a unique $\lambda \in \mathcal{A}(G)$ such that $\delta(v) = v
\otimes \lambda$.

If $v$ satisfies these conditions, one says that $v$ is a *semi-invariant vector under $G$*, and that $\lambda$ is the
*weight* of $v$; one will also say that "$v$ is a semi-invariant of weight $\lambda$".

Denote by `∆` the comultiplication of $\mathcal{A}(G)$; then the equality

```text
v ⊗ λ ⊗ λ = (δ ⊗ id)(δ(v)) = (id ⊗ ∆)(δ(v)) = v ⊗ ∆(λ)
```

implies that `∆(λ) = λ ⊗ λ`. Consequently, $\lambda$ defines a morphism of Hopf algebras

```text
𝒜(G_{m,k}) = k[T, T⁻¹] → 𝒜(G),    T ↦ λ,
```

and hence a morphism of $k$-groups $\lambda : G \to G_{m,k}$, i.e. $\lambda$ is a *character* of $G$, called the
*character associated with the semi-invariant vector $v$*.

**Lemma 11.16.0.** [^N.D.E-VI_B-C-128] *Let $k$ be a field, $H$ an affine $k$-group, $V$ an $H$-module of dimension $n$
and $U$ a vector subspace of $V$ of dimension $d$. Consider the line $D = \bigwedge^{d} U \subset \bigwedge^{d} V$. For
$U$ to be stable under $H$, it is necessary and sufficient that $D$ be so.*

<!-- label: III.VI_B.11.16.0 -->

Necessity being clear, let us prove sufficiency. One may suppose $d < n$. Let $(e_{1}, \cdots, e_{d})$ be a basis of
$U$, complete it into a basis $(e_{1}, \cdots, e_{n})$ of $V$. For every $k$-algebra $R$, $V_{R} = V \otimes R$ is a
free $R$-module and one has

```text
U_R = {v ∈ V_R | v ∧ (e_1 ∧ ⋯ ∧ e_d) = 0}
```

(since for $i > d$ the $e_{i} \wedge e_{1} \wedge \cdots \wedge e_{d}$ are linearly independent in $\bigwedge^{d+1}
V_{R}$). Since $H(R)$ acts on $\bigwedge^{\bullet} V_{R}$ by

```text
h(x_1 ∧ ⋯ ∧ x_s) = h(x_1) ∧ ⋯ ∧ h(x_s),
```

it follows that if $H(R)$ stabilizes $D_{R} = R e_{1} \wedge \cdots \wedge e_{d}$, it also stabilizes `U_R`. ∎

**Theorem 11.16 (Chevalley).** *Let $k$ be a field, $G$ an algebraic affine $k$-group, $H$ a closed group subscheme of
$G$.[^N.D.E-VI_B-C-129] Then there exist a finite-dimensional $G$-module $V$ and a line $D$ in $V$ such that $H =
Norm_{G}(D)$, i.e. such that for every $k$-algebra $R$,*

```text
H(R) = {g ∈ G(R) | g(D_R) = D_R}.
```

*In other words, there exist finitely many elements $a_{1}, \cdots, a_{n} \in \mathcal{A}(G)$, which are semi-invariant,
all of the same weight $\lambda$, for the "right" action of $H$ (i.e. $a_{i}(gh) = \lambda(h) a_{i}(g)$, for every
$k$-algebra $R$ and $g \in G(R)$, $h \in H(R)$), such that $H$ be the largest closed group subscheme of $G$ under which
the $a_{i}$ are semi-invariant.*

<!-- label: III.VI_B.11.16 -->

Denote by `∆` (resp. $\epsilon$) the comultiplication (resp. the augmentation) of $A = \mathcal{A}(G)$. Then $H =
\operatorname{Spec}(A/I)$, for some ideal $I$ of $A$, contained in $Ker \epsilon$ and such that `∆(I) ⊂ I ⊗ A + A ⊗ I`.
Let $B = A/I$ and $\pi$ the projection $A \to B$. Consider the left action of $H$ on $A$ given by $(h\phi)(g) =
\phi(gh)$; the corresponding $B$-comodule structure is given by:

```text
∆̄ : A ──∆──→ A ⊗ A ──id_A ⊗ π──→ A ⊗ B.
```

Then $I$ is a sub-$H$-module of $A$, since `∆̄(I) ⊂ I ⊗ B`.

On the other hand, $A$ is a finitely generated $k$-algebra, hence noetherian, hence $I$ admits a finite system of
generators $(x_{1}, \cdots, x_{r})$. By 11.8, the $x_{i}$ are contained in a sub-$G$-module $V$ of finite dimension over
$k$. Then $W = V \cap I$ is an $H$-module of finite dimension, whose dimension we denote by $d$. Since $V$ contains all
the $x_{i}$, $W$ generates the ideal $I$.

Set $E = \bigwedge^{d} V$, let $(w_{1}, \cdots, w_{d})$ be a basis of $W$, and let $B = (e_{0}, \cdots, e_{n})$ be a
basis of $E$ containing the vector $e_{0} = w_{1} \wedge \cdots \wedge w_{d}$. The action of $G$ on $V$ canonically
determines an action of $G$ on $E$, hence an $A$-comodule structure $\rho : E \to E \otimes A$. For $j = 0, \cdots, n$,
set $\rho(e_{j}) = \sum^{n}_{i=1} e_{i} \otimes b_{ij}$; one has seen in the proof of 11.12 that

```text
(∗)     ∆(b_{ij}) = ∑_{ℓ=0}^n b_{iℓ} ⊗ b_{ℓj}.
```

Set $a_{i} = b_{i0}$, i.e. if $(e^{*}_{0}, \cdots, e^{*}_{n})$ is the dual basis of $B$, the $a_{i}$ are the "matrix
coefficients" $g \mapsto e^{*}_{i}(g e_{0})$. On the other hand, the action of $H$ on $E$ corresponds to:

```text
ρ̄ : E ──ρ──→ E ⊗ A ──id_E ⊗ π──→ E ⊗ B.
```

Since $W$ is stable under $H$, $e_{0}$ is semi-invariant under $H$, hence $\bar{\rho}(e_{0}) = e_{0} \otimes \pi(a_{0})$
and $a_{i} = b_{i0}$ belongs to $I$ for $i = 1, \cdots, n$. Substituting this into (∗), one obtains
`∆̄(a_i) = a_i ⊗ π(a_0)` for $i = 0, \cdots, n$, i.e. the $a_{i}$ are semi-invariant under $H$ with weight $\pi(a_{0})$.
(Moreover, possibly by replacing $E$ by the sub-$G$-module generated by $e_{0}$ (cf. 11.8), one may assume that the
$a_{i}$ are linearly independent.)

Conversely, let $H' = \operatorname{Spec} B'$, where $B' = A/I'$, be a closed group subscheme of $G$ under which each of
the $a_{i}$ is semi-invariant, with weight $\lambda_{i} \in B'$ (this is the case, in particular, if $e_{0}$ is
invariant under $H'$ with weight $\lambda'$). Let us show that $H' = H$. Denote by $\pi'$ the projection $A \to B'$; the
hypothesis implies that

```text
a_i ⊗ λ_i = (id_A ⊗ π′) ∆(b_{i0}) = ∑_{ℓ=0}^n b_{iℓ} ⊗ π′(a_ℓ),
```

whence $\lambda_{i} = \pi'(a_{0})$ and $a_{\ell} \in I'$ for $\ell = 1, \cdots, n$, and hence $e_{0}$ is semi-invariant
under $H'$. By Lemma 11.16.0, this implies that $W$ is stable under $H'$. Since the ideal $I$ is generated by $W$, it is
also stable under $H'$, and therefore

```text
∆(I) ⊂ I ⊗ A + A ⊗ I′.
```

Since $I \subset Ker \epsilon$ and `(ε ⊗ id_A) ∘ ∆ = id_A`, it follows that $I \subset I'$, whence $H' \subset H$. ∎

**Lemma 11.17.0.** [^N.D.E-VI_B-C-130] *Let $k$ be an algebraically closed field, $G$ a reduced algebraic affine
$k$-group, $V$ a finite-dimensional $G$-module over $k$, and $v \in V$. Let $E$ be the vector subspace of $V$ generated
by the vectors `gv`, for $g \in G(k)$. Then $E$ is the smallest sub-$G$-module of $V$ containing $v$, and hence the
morphism $G \times E \to V$, $(g, x) \mapsto gx$, factors through $E$.*

<!-- label: III.VI_B.11.17.0 -->

*Proof.* By 11.8, we know that there exists a smallest sub-$G$-module $U$ of $V$ containing $v$: if $\mu : V \to V
\otimes \mathcal{A}(G)$ denotes the comodule structure and if one writes $\mu(v) = \sum^{n}_{i=1} v_{i} \otimes a_{i}$
with the $a_{i}$ linearly independent, one has $U = Vect(v_{1}, \cdots, v_{n})$. It is clear that $U$ contains $E$, and
that the morphism $G \times U \to V$ factors through $U$.

Conversely, the inverse image of $E$ by the morphism $\mu_{v} : g \mapsto gv$ is a closed subset of $G$ which contains
the rational points; now these are dense in $G$, since $G$ is of finite type over $k$ (cf. EGA IV₃, 10.4.8), hence
$\mu^{-1}_{v}(E) = G$ and so, since $G$ is reduced, $\mu_{v}$ factors through $E$, whence $E = U$. ∎

**Theorem 11.17 (Chevalley).** *Let $k$ be a field, $G$ an affine $k$-group (not necessarily of finite type), and $N$ a
closed group subscheme of $G$ invariant in $G$; then the (fpqc) sheaf quotient $G/N$ is representable by an affine
$k$-group.*[^N.D.E-VI_B-C-131]

<!-- label: III.VI_B.11.17 -->

Suppose first $G$ of finite type. By VI_A 3.2 and 5.2, the (fpqc) sheaf quotient $G/N$ is representable by a $k$-group
$Q$; it therefore remains to show that $Q$ is affine. The proof is done in several stages; suppose first $k$
algebraically closed.[^N.D.E-VI_B-C-132]

(a) Suppose moreover $G$ reduced and connected, and $N$ reduced. By 11.16, there exist a $G$-module $V$, of finite
dimension over $k$, and a line $D = k e_{0}$ such that $Norm_{G}(D) = N$; in particular $N$ acts on $D$ via a character
$\chi : N \to G_{m, k}$.

Fix $h \in N(k)$. For every $g \in G(k)$, one has $hg e_{0} = g(g^{-1} h g) e_{0} = \chi(g^{-1} h g) g e_{0}$, hence
$\chi(g^{-1} h g)$ is an eigenvalue of $h$. Hence the continuous map $\phi : G(k) \to k$, $g \mapsto \chi(g^{-1} h g)$,
takes only finitely many values, and since $G(k)$ is irreducible (since dense in $G$), one therefore has $\phi(g) =
\phi(e) = \chi(h)$ for every $g \in G(k)$, and so

```text
χ(g⁻¹ h g) = χ(h),     ∀ g ∈ G(k), h ∈ N(k).
```

Let $E$ be the vector subspace of $V$ generated by the vectors $g e_{0}$, for $g \in G(k)$; by Lemma 11.17.0, this is
the sub-$G$-module of $V$ generated by $e_{0}$.

By what precedes, the two morphisms $N \times E \to E$, $(h, x) \mapsto hx$ and $(h, x) \mapsto \chi(h) x$, coincide on
the set of rational points $(N \times E)(k) = N(k) \times E(k)$, which is dense in $N \times E$. Since $N \times E$ is
reduced (and $E$ separated), these two morphisms are therefore equal, so $N$ acts on $E$ by homotheties. Consequently,
$N$ is contained in the kernel $K$ of the morphism $\rho : G \to GL(\operatorname{End}_{k}(E))$, defined by $\rho(g)(u)
= g u g^{-1}$, for every $g \in G(R)$ and $u \in \operatorname{End}_{R}(E \otimes R)$ ($R$ a $k$-algebra). On the other
hand, if $g \in K(R)$ then $g(R e_{0}) = R e_{0}$, whence $g \in N(R)$. This shows that $N = K$. Then, by VI_A 5.4.1,
the morphism $G/N \to GL(\operatorname{End}_{k}(E))$ is a closed immersion, and hence $G/N$ is affine.

(b) Suppose now $G$ and $N$ reduced, $G$ not necessarily connected. Set $N' = N \cap G^{0}$; then $G^{0}/N'$ is affine
by (a). On the other hand, $NG^{0}$ is an invariant subgroup of $G$ and $G/NG^{0}$, being a quotient of the finite
constant group $G/G^{0}$ (cf. VI_A, 5.5.1), is likewise a finite constant group. Hence $G/N$ is the direct sum of the
fibers of the morphism $G/N \to G/NG^{0}$, all isomorphic to $NG^{0}/N$, hence to $G^{0}/N'$, by VI_A, 5.3.3. Hence
$G/N$ is affine.

(c) Suppose $G$ reduced, and $N$ arbitrary. The morphism $G \times N \to N$, $(g, h) \mapsto ghg^{-1}$, induces a
morphism $(G \times N)_{red} \to N_{red}$; now, since $G$ is reduced and $k$ algebraically closed, one has $(G \times
N)_{red} = G \times N_{red}$, hence $N_{red}$ is an invariant subgroup of $G$. (N.B. this fails when $G$ is not reduced,
cf. VI_A, 0.2.)

Hence, by (a), $G' = G/N_{red}$ is affine. On the other hand, by VI_A 5.6.1, $N' = N/N_{red}$ is a finite $k$-group,
hence by Theorem 4.1 of Exp. V, the quotient $G/N = G'/N'$ is affine.

(d) For arbitrary $G$ and $N$, the equivalence relation deduced from $G \times N \Rightarrow G$ by the base change
$G_{red} \to G$ is:

```text
G_red × N′ ⇒ G_red,     where     N′ = N ∩ G_red.
```

Since the underlying spaces are the same (and since the quotient is the quotient ringed space), the morphism $G_{red} /
N' \to G/N$ is a homeomorphism. Since $G_{red} / N'$ is reduced (since $p : G_{red} \to G_{red}/N'$ is faithfully flat),
it follows that $(G/N)_{red}$ is identified with $G_{red} / N'$, which is affine by (c). Since $G/N$ is of finite type
over $k$ (cf. VI_A, 3.3.2), this implies, by EGA I, 5.1.10, that $G/N$ is affine.

Finally, for arbitrary $k$, let $\bar{k}$ be an algebraic closure of $k$. Then, by 9.2 (v), $(G \otimes_{k} \bar{k})/(N
\otimes_{k} \bar{k})$ is isomorphic to $(G/N) \otimes_{k} \bar{k}$, hence since the former is affine, so is the latter,
and so $G/N$ is also affine, by (fpqc) descent (cf. EGA IV₂, 2.7.1). This proves 11.17 when $G$ is of finite type. To
extend this to the general case, we shall need the following lemma.[^N.D.E-VI_B-C-133]

**Lemma 11.17.1.** *Let $(C_{i} \to A_{i})_{i \in I}$ be a filtered inductive system of ring morphisms, all faithfully
flat. Then $A = \lim A_{i}$ is faithfully flat over $C = \lim C_{i}$.*

<!-- label: III.VI_B.11.17.1 -->

*Proof.* By [BAC] § I.3, Prop. 9, for a morphism of rings $B \to B'$ to be faithfully flat, it is necessary and
sufficient that it be injective and that $B'/B$ be a flat $B$-module. Since each $C_{i} \to A_{i}$ is faithfully flat,
one therefore has exact sequences

```text
0 ────→ C_i ────→ A_i ────→ A_i / C_i ────→ 0
```

and $A_{i} / C_{i}$ is a flat $C_{i}$-module, hence $(A_{i} / C_{i}) \otimes_{C_{i}} C$ is a flat $C$-module. Since
inductive limits are exact and commute with the tensor product, one obtains an exact sequence

```text
0 ────→ C ────→ A ────→ A/C ────→ 0
```

as well as an isomorphism

```text
lim ((A_i / C_i) ⊗_{C_i} C) = (A/C) ⊗_C C = A/C,
```

from which one deduces that $A/C$ is a flat $C$-module. Hence $A$ is faithfully flat over $C$. ∎

Let us now return to the proof of 11.17 in the general case, i.e. when $G$ is not assumed to be of finite type. Set
$\mathcal{A}(G) = A$ and $\mathcal{A}(N) = B = A/J$. By 11.13, $A$ is the inductive limit of a filtered increasing
family $(A_{i})_{i \in I}$ of finitely generated sub-Hopf algebras, hence $G$ is the projective limit of the algebraic
affine $k$-groups $G_{i} = \operatorname{Spec}(A_{i})$. Denote by `∆` (resp. $\tau$) the comultiplication (resp. the
antipode) of $A$, and `∆_2 = (∆ ⊗ id_A) ∘ ∆`.

For every $i$, $B_{i} = A_{i} / (J \cap A_{i})$ is a quotient Hopf algebra of $A_{i}$, hence $N_{i} =
\operatorname{Spec}(B_{i})$ is a closed subgroup of $G_{i}$. Moreover, since $N$ is invariant in $G$, the morphism $G
\times N \to G$ defined by $(g, n) \mapsto gng^{-1}$ factors through $N$, and this is equivalent to saying that the
couple $(A, J)$ satisfies the following property:

```text
(m_{13} ∘ (∆ ⊗ τ) ∘ ∆_2)(J) ⊂ A ⊗_k J
```

where $m_{13}$ denotes the map $a_{1} \otimes a_{2} \otimes a_{3} \mapsto a_{1} a_{3} \otimes a_{2}$. It follows that
$(A_{i}, A_{i} \cap J)$ satisfies the analogous property, hence that $N_{i}$ is invariant in $G_{i}$. On the other hand,
one has $\lim B_{i} = B$ and hence $\lim N_{i} = N$.

By what we have seen previously, each (fpqc) sheaf quotient $G_{i} / N_{i}$ is representable by an affine $k$-group
$Q_{i} = \operatorname{Spec}(C_{i})$. Set $C = \lim C_{i}$. One thus has a filtered projective system of affine
$k$-groups $Q_{i}$; its projective limit $Q = \lim Q_{i}$ is the $k$-group $\operatorname{Spec}(C)$ (cf. EGA IV₃,
8.2.3). One then has an exact sequence of $k$-groups:

```text
1 ────→ N ────→ G ────→ Q.
```

Let us show that $Q$ represents the (fpqc) sheaf quotient of $G$ by $N$; for this, it suffices to verify that the
morphism $G \to Q$ is covering for the (fpqc) topology (cf. IV, 3.3.2.1 and 5.1.7.1). Now, each of the morphisms $G_{i}
\to Q_{i}$ is faithfully flat (cf. 9.2 (xi)), in other words $A_{i}$ is faithfully flat over $C_{i}$; since $A = \lim
A_{i}$ and $C = \lim C_{i}$, it follows from Lemma 11.17.1 that $A$ is faithfully flat over $C$, so that $G \to Q$ is a
faithfully flat morphism. Since this morphism is affine, it is quasi-compact, hence covering for the (fpqc) topology.
This completes the proof of Theorem 11.17. ∎

### 11.18. Complements.

[^N.D.E-VI_B-C-134] Moreover, one deduces from 11.17 (and from its proof) the following results, taken from [DG70], III
§ 3.7. Let $k$ be a field. We begin with the following lemma (cf. [An73], 2.3.3.2), which will be useful later (cf.
12.10).

**Lemma 11.18.1.** *Let $u : G \to G'$ be a morphism of $k$-groups, $N = Ker(u)$. Suppose $G'$ affine and $G$ of finite
type.*

*(i) The morphism $\tau : G/N \to G'$ is a closed immersion. In particular, $G/N$ is affine.*

*(ii) If moreover the morphism $u^{\natural} : O(G') \to O(G)$ is injective, then $\tau$ is an isomorphism. (And hence
$G'$ is of finite type and $u$ is faithfully flat.)*

<!-- label: III.VI_B.11.18.1 -->

Indeed, we know (11.13) that $G'$ is the projective limit of a filtered system of algebraic affine $k$-groups $G'_{i}$.
Denote by $u_{i}$ the composite morphism $G \to G' \to G'_{i}$ and by $N_{i}$ its kernel. Then the $N_{i}$ form a
filtered decreasing system of closed subgroups of $G$, whose intersection is $N$. Since $G$ is noetherian, there exists
an index $i$ such that $N = N_{i}$. Since $G$ and $G_{i}$ are of finite type, by VI_A, 3.2 and 5.4.1, the quotient $G/N$
is a finitely generated $k$-group and $u_{i}$ is the composite of the projection $p : G \to G/N$, which is faithfully
flat, and a closed immersion $\tau_{i} : G/N \hookrightarrow G_{i}$.

Consider then the following commutative diagram:

```text
        u
   G ────────→ G′
   │       ↗
 p │   τ ╱      ╲ q_i
   ↓   ╱          ↘
   G/N ─────→ G_i.
        τ_i
```

Since $q_{i} \circ \tau = \tau_{i}$ is a closed immersion and $q_{i}$ is separated ($G'$ being separated, cf. VI_A,
0.3), then $\tau$ is a closed immersion (cf. EGA I, 5.4.4). It follows that $G/N$ is affine, and that the morphism
$\tau^{\natural} : O(G') \to O(G/N)$ is surjective, whence (i).

If moreover $u^{\natural} : O(G') \to O(G)$ is injective, so is $\tau^{\natural}$, hence $\tau^{\natural}$ is an
isomorphism, hence so is $\tau$ (since $G'$ and $G/N$ are affine). This proves (ii). ∎

**Theorem 11.18.2.** *Let $G$ and $G'$ be two affine $k$-groups, with algebras $A$ and $A'$, and let $u : G \to G'$ be a
morphism of $k$-groups, $N = Ker(u)$, and $\phi : A' \to A$ the morphism induced by $u$.*

*(i) If $\phi$ is injective, then $u$ is faithfully flat and identifies $G'$ with $G/N$.*

*(ii) One has $G/N = \operatorname{Spec}(B)$, where $B = \phi(A')$, and hence $u$ is the composite of the faithfully
flat morphism $G \to G/N$, corresponding to the inclusion $B \hookrightarrow A$, and of the closed immersion $G/N
\hookrightarrow G'$, which corresponds to the surjection $A' \to B$. Moreover, $N$ is defined in $G$ by the ideal
$AB_{+}$, where $B_{+}$ denotes the augmentation ideal of $B$.*

*(iii) In particular, if $u$ is a monomorphism, it is a closed immersion.*

<!-- label: III.VI_B.11.18.2 -->

*Proof.* (i) Suppose $\phi$ injective and identify $A'$ with a sub-Hopf algebra of $A$. By 11.13, $A$ is the filtered
union of finitely generated sub-Hopf algebras $A_{i} = O(G_{i})$; denote $G'_{i} = \operatorname{Spec}(A'_{i})$, where
$A'_{i} = A' \cap A_{i}$, and $N_{i}$ the kernel of the morphism $G_{i} \to G'_{i}$ induced by the inclusion $A'_{i}
\hookrightarrow A_{i}$. By the preceding lemma, one has $G_{i} / N_{i} \cong G'_{i}$ and one therefore obtains, for
every $i$, an exact sequence

```text
                          p_i
1 ────→ N_i ────→ G_i ────→ G′_i ────→ 1
```

where $p_{i}$ is faithfully flat. Since $G = \lim_{i} G_{i}$ and $G' = \lim_{i} G'_{i}$, one therefore obtains an exact
sequence

```text
                     p
1 ────→ N ────→ G ────→ G/N
```

where one has set $N = \lim_{i} N_{i}$. Moreover, by Lemma 11.17.1, $p$ is faithfully flat (and affine), hence $G'$
represents the (fpqc) sheaf quotient of $G$ by $N$. This proves (i).

In the general case, $B = \phi(A')$ is a sub-Hopf algebra of $A$; denote by $H$ the $k$-group $\operatorname{Spec}(B)$
and $N'$ the kernel of the morphism $G \to H$ induced by the inclusion $B \hookrightarrow A$. By (i), $H$ is identified
with $G/N'$, and $u$ is therefore the composite of the projection $G \to G/N'$ and the closed immersion $G/N'
\hookrightarrow G'$ induced by the surjection $A' \to B$. It follows that $N' = N$. Moreover, by 9.2 (ii), one has a
cartesian square:

```text
   N ────→ G
   │        │ p
   ↓   ε    ↓
Spec(k) ──→ G′
```

where $\epsilon$ is the unit section of $G'$, which corresponds to the augmentation morphism $B \to k$. It follows that
$N$ is defined in $G$ by the ideal $AB_{+}$. This proves (ii), and (iii) follows. ∎

**Remark 11.18.3.** Let $G$ be an affine $k$-group and $N$ a normal $k$-subgroup. Since the morphism $p : G \to G/N$ is
faithfully flat and quasi-compact, by IV 3.3.3.2, $O(G/N)$ is the subalgebra of $O(G)$ formed of functions $\phi$ which
are right $N$-invariant, i.e. which satisfy $\phi(gh) = \phi(g)$, for every $k$-scheme $S$ and $g \in G(S)$, $h \in
N(S)$. Denoting by $J$ the ideal of $A = O(G)$ which defines $N$, this is equivalent to saying that
`∆(φ) − φ ⊗ 1 ∈ O(G) ⊗ J`, where `∆` is the comultiplication of $A$.

<!-- label: III.VI_B.11.18.3 -->

The preceding theorem can then be reformulated in terms of Hopf algebras as follows.

**Corollary 11.18.4.** *Let $k$ be a field, $A$ a commutative $k$-Hopf algebra, $G = \operatorname{Spec}(A)$.*

*(i) If $B$ is a sub-Hopf algebra of $A$, then $A$ is faithfully flat over $B$.*

*(ii) The map $N \mapsto O(G/N)$ is a bijection between the set of normal subgroups of $G$ and that of sub-Hopf algebras
of $A$; the inverse map is given by $B \mapsto \operatorname{Spec}(A/AB_{+})$. Moreover, if $J$ is the ideal of $A$
defining $N$, one has*

```text
O(G/N) = {x ∈ A | ∆(x) − x ⊗ 1 ∈ A ⊗ J}.
```

<!-- label: III.VI_B.11.18.4 -->

**Remarks 11.18.5.** (a) A consequence of the preceding theorem is that the category of commutative affine $k$-groups is
abelian. For this, as well as for other results on affine $k$-groups, we refer to [DG70], § III.3, 7.4 to 7.8.

(b) Let us finally point out that M. Takeuchi has given another proof of results 11.17 to 11.18.4, cf. [Ta72], § 5; he
moreover strengthened 11.18.4 (i) above by showing that $A$ is even a projective $B$-module, cf. [Ta79], Th. 5 (see also
[MW94], Th. 3.6).

<!-- label: III.VI_B.11.18.5 -->

## 12. Complements on $G_{af}$ and the "anti-affine" groups

<!-- label: III.VI_B.12 -->

[^N.D.E-VI_B-C-135] We begin with the following lemma, which extends 11.18.1 to the case where $G$ is not assumed to be
of finite type.[^N.D.E-VI_B-C-136]

**Lemma 12.1.** *Let $k$ be a field, $u : G \to H$ a monomorphism of $k$-groups, with $H$ affine. Suppose $u$
quasi-compact. Then $u$ is a closed immersion.*

<!-- label: III.VI_B.12.1 -->

*Proof.* By (fpqc) descent, one may suppose $k$ algebraically closed. By VI_A, 6.4, the closed image $I$ of $u$ is a
closed group subscheme of $H$, hence still affine. Hence, replacing $H$ by $I$, one may suppose $u$ schematically
dominant. Since $k$ is algebraically closed, $H' = H_{red}$ is a group subscheme of $H$; set $G' = G \times_{H} H'$;
then the morphism $u' : G' \to H'$ deduced from $u$ by base change is a quasi-compact monomorphism, and is dominant (the
underlying continuous map being the same for $u$ and $u'$). Hence, by VI_A, 6.2, $u'$ is faithfully flat; it is
therefore a quasi-compact faithfully flat monomorphism, hence an isomorphism (cf. IV 1.14).

Hence $u : G \to H$ is a homeomorphism, so it is affine by 2.9.1. Hence $G$ is affine, and so $u$ is a closed immersion
by 11.18.2 (iii). ∎

**Theorem 12.2.** *Let $G$ be an algebraic $k$-group. Denote by $\rho$ the canonical morphism $G \to G_{af}$ and $N$ its
kernel.*

*(i) The canonical morphism $G/N \to G_{af}$ is an isomorphism, and hence $G_{af}$ is an algebraic affine group, and
$\rho$ is faithfully flat.*

*(ii) One has a canonical isomorphism $(G/N)_{af} = G_{af}$.*

*(iii) $N$ is a characteristic subgroup of $G$.*

*(iv) $O(N) = k$.*

*(v) $N$ is smooth, connected, and commutative.*

<!-- label: III.VI_B.12.2 -->

*Proof.* Point (i) is a particular case of 11.18.1, and point (ii) follows from the universal properties of $G_{af}$ and
$(G/N)_{af}$.

Let us prove (iii). For an arbitrary $k$-scheme $\pi : S \to \operatorname{Spec} k$, consider the cartesian square:

```text
   G_S ────→ G
    │         │
  q │         │ p
    ↓    π    ↓
    S ────→ Spec k.
```

Since $p$ is quasi-compact and separated and $\pi$ flat, by EGA III 1.4.15 and EGA IV₁ 1.7.21, one has $q_{*}(O_{G_{S}})
= \pi*(O(G)) = \pi*(O(G_{af}))$, and hence, by EGA II, 1.5.2, one has $(G_{S})_{af} = (G_{af})_{S}$. Hence `N_S`, being
the kernel of the canonical morphism $G_{S} \to (G_{S})_{af}$, is invariant under every automorphism of `G_S`, i.e. $N$
is a characteristic subgroup of $G$.

To prove (iv), set $N' = Ker(N \to N_{af})$; by (ii), this is an invariant subgroup of $G$. Since $N$ is algebraic
(being a closed subgroup of $G$), by (i), $N/N' \cong N_{af}$; moreover, by VI_A, 3.2 and 5.3.2, one has an isomorphism
of $k$-groups

```text
(G/N′) / N_af ≅ (G/N′)/(N/N′) ≅ G/N.
```

Since $N_{af}$ is affine, the projection $G/N' \to G/N$ is also affine, by 9.2 (vii), and since $G/N = G_{af}$ is
affine, so is $G/N'$. Hence, by the universal property of $G_{af}$, the projection $p' : G \to G/N'$ factors through
$G_{af} = G/N$, whence $N \subset N'$ and hence $N = N'$. Hence $N_{af}$ is the trivial group, whence $O(N) = k$.

Finally, assertion (v) follows from the following lemma. ∎

**Lemma 12.3.** *Let $k$ be a field and $N$ an algebraic $k$-group such that $O(N) = k$. Then $N$ is smooth, connected,
and commutative.*

<!-- label: III.VI_B.12.3 -->

Indeed, one may suppose $k$ algebraically closed. Then $H = N^{0}_{red}$ is a $k$-subgroup of $N$, and the quotient
$k$-scheme $X = N/H$ is finite (hence affine) over $k$, by VI_A, 5.5.1 and 5.6.1. Moreover, since $p : N \to X$ is
faithfully flat, one has $O(X) \subset O(N) = k$. It follows that $N = N^{0}_{red}$, hence $N$ is smooth (VI_A 1.3.1)
and connected.

Let then $Z$ be the center of $N$. By 6.2.6, $N/Z$ is affine, and one obtains as above that $O(N/Z) = k$, whence $N =
Z$. This proves 12.3 and completes the proof of 12.2. ∎

Let us also state, without proof, the following theorem. (Recall that an *abelian variety* over a field $k$ is a proper,
smooth, and connected $k$-group scheme.)

**Theorem 12.4 (Chevalley).** *Let $k$ be a perfect field and $G$ an algebraic, smooth and connected $k$-group. Then
there exists an affine, smooth and connected $k$-subgroup $L$, invariant in $G$, such that the quotient $G/L$ is an
abelian variety. Moreover, $L$ is unique and its formation commutes with extension of the base field.*

<!-- label: III.VI_B.12.4 -->

**Remarks 12.5.** (1) This theorem was announced in 1953 by C. Chevalley, who published his proof in 1960 ([Ch60]).
Meanwhile, other proofs were obtained, independently, by I. Barsotti and M. Rosenlicht ([Ba55, Ro56]); see [Se99] for
historical comments.

(2) A modern version (i.e. in the language of schemes) of Chevalley's proof has been given by B. Conrad ([Co02]). (Note
that in loc. cit., "algebraic group" means smooth and connected $k$-group scheme.)

(3) On the other hand, a modern version of Rosenlicht's proof has been given by Ngô B.-C. in a course at Orsay in
2005-2006.

(4) If one drops the hypothesis that $k$ is perfect, there still exists a smallest invariant connected affine subgroup
$L$ (not necessarily smooth) such that $G/L$ is an abelian variety ([BLR], § 9.2, Thm. 1).

(5) One may also drop the hypothesis that $G$ is smooth over $k$: indeed, by VII_A, 8.3, there exists an integer $n \geq
1$ such that the quotient $G' = G/(Fr^{n} G)$ is smooth; then $G'$ contains a subgroup $L'$ as in (4) above, and the
inverse image of $L'$ in $G$ still has the same properties. Hence, for every connected algebraic group $G$ over a field
$k$, there exists an exact sequence

```text
1 ────→ H ────→ G ────→ A ────→ 1
```

where $H$ is an affine $k$-group and $A$ a $k$-abelian variety. Moreover, by [Per76], Cor. 4.2.9, one has such an exact
sequence for every connected $k$-group $G$ (not necessarily algebraic).

(6) Let $k$ be an algebraically closed field and $G$ the semi-direct product of an elliptic curve $E$ by the constant
$k$-group ${\pm 1}_{k}$, for the action defined by $(-1) \cdot x = -x$; in this case, if $L$ is a closed invariant
subgroup of $G$ such that $G/L$ is connected, then $L = G$.

<!-- label: III.VI_B.12.5 -->

**Remark 12.6.** One will say, following [Br09], that a $k$-group $N$ is *anti-affine* if $O(N) = k$. By 12.3 and 12.4,
if $k$ is perfect, every anti-affine algebraic $k$-group is an extension of an abelian variety by a smooth, connected,
commutative affine algebraic $k$-group. For the precise structure of anti-affine algebraic groups over a perfect field,
and various consequences, see the recent articles of M. Brion and C. & F. Sancho de Salas ([Br09, SS09]).

<!-- label: III.VI_B.12.6 -->

To conclude this section, we shall prove two results due to M. Raynaud, the first being Remark 11.11.1, the second
Proposition 2.1 of Exp. XVII, Appendix III. We shall need the following lemma,[^N.D.E-VI_B-C-137] which improves (for a
complete discrete valuation ring $R$) the flatness criteria given in [BAC], § III.5.

**Lemma 12.7.** *Let $R$ be a discrete valuation ring, $K$ its field of fractions, $\pi$ a uniformizer. Let $A$ be a
flat $R$-algebra and $M$ an $A$-module flat over $R$. Suppose that:*

*(i) $M/\pi M$ is a flat module over $\bar{A} = A/\pi A$,*

*(ii) $M \otimes_{R} K$ is a flat module over $A \otimes_{R} K$.*

*Then $M$ is a flat $A$-module.*

<!-- label: III.VI_B.12.7 -->

*Proof.* By the flatness criterion in the nilpotent case (cf. [BAC], III § 5.2, Th. 1), $M/\pi^{n} M$ is a flat module
over $A/\pi^{n} A$, for every $n \in \mathbb{N}^{*}$. It then follows from [RG71], II Lemma 1.4.2.1, that $M$ is a flat
$A$-module. For the reader's convenience, let us briefly indicate the proof. Set $s = \pi^{n}$ and $P = M/sM$. Since $P$
is flat over $A/sA$ and the latter is of projective dimension 1 over $A$, it follows from the spectral sequence of
composite functors that $P$ is of Tor-dimension $\leq 1$ over $A$. Now, since $M$ is $R$-flat hence without
$\pi$-torsion, $M_{K} / M$ is the inductive limit of the $A$-modules $\pi^{-n} M / M \cong M / \pi^{n} M$, and hence
$M_{K} / M$ is also of Tor-dimension $\leq 1$. Since one has the exact sequence $0 \to M \to M_{K} \to M_{K} / M \to 0$
and by hypothesis `M_K` is flat over `A_K` hence over $A$, it follows that $M$ is flat.

For completeness, let us also indicate the following simpler proof, pointed out by O. Gabber. Let $I$ be a finitely
generated ideal of $A$; one must show that the morphism $u : M \otimes_{A} I \to M$ is injective. By hypothesis (ii), $u
\otimes_{R} K$ is injective, hence $Ker(u)$ is an $R$-module of $\pi$-torsion. It therefore suffices to show that the
$\pi$-torsion part of $M \otimes_{A} I$ is zero; now this is a quotient of $Tor^{A}_{1}(M, I/\pi I)$, as one sees by
tensoring with $M$ the exact sequence:

```text
                π
0 ────→ I ────→ I ────→ I/πI ────→ 0.
```

On the other hand, $M$ being without $\pi$-torsion (since flat over $R$), one obtains that $Tor^{A}_{i}(M, \bar{A}) = 0$
for every $i \geq 1$. Consequently, if $(P_{\bullet})$ is a projective resolution of the $A$-module $M$, then
$(P_{\bullet} \otimes_{A} \bar{A})$ is a projective resolution of the `Ā`-module $\bar{M} = M/\pi M$, and hence for
every `Ā`-module $N$, one has $Tor^{A}_{i}(M, N) = Tor^{\bar{A}}_{i}(\bar{M}, N)$, and this is zero for $i \geq 1$ since
$\bar{M}$ is flat over `Ā`. One thus has $Tor^{A}_{1}(M, I/\pi I) = 0$, which proves the lemma. ∎

**Remark 12.8.** Let $S$ be a regular locally noetherian scheme of dimension 1, and $X$ a flat, quasi-separated and
quasi-compact $S$-scheme. Then $\mathcal{A}(X)$ is a flat `O_S`-module. Indeed, one may suppose $S$ local; denote by $s$
its closed point, $i$ the inclusion $X_{s} \hookrightarrow X$, and $\pi$ a uniformizer of $R = O(S)$; since $X$ is flat
over $S$, one has an exact sequence of sheaves

```text
                π
0 ────→ O_X ────→ O_X ────→ i_*(O_{X_s}) → 0
```

and so, by taking global sections, one obtains that $\mathcal{A}(X)$ is an $R$-module without $\pi$-torsion, hence
flat.[^N.D.E-VI_B-C-138] One obtains moreover that the morphism from $\mathcal{A}((X_{af})_{s}) = \mathcal{A}(X)/\pi
\mathcal{A}(X)$ to $\mathcal{A}(X_{s})$, induced by the morphism $X \to X_{af}$, is injective.

<!-- label: III.VI_B.12.8 -->

One can now prove the following proposition (cf. Remark 11.11.1).

**Proposition 12.9.** *Let $S$ be a regular locally noetherian scheme of dimension $\leq 1$, $G$ an $S$-group scheme
flat, quasi-separated and quasi-compact over $S$. Then the following conditions are equivalent:*

*(i) $G$ is affine over $S$.*

*(ii) $G$ is quasi-affine over $S$.*

*(iii) $G$ acts faithfully on a quasi-affine and flat $S$-scheme $X$.*

*(iv) $G$ acts linearly and faithfully on a quasi-coherent module $E$ flat over $S$.*

*(v) The morphism $\rho : G \to G_{af}$ is a monomorphism.*

<!-- label: III.VI_B.12.9 -->

*Proof.* The implication (i) ⇒ (ii) is evident, as is (ii) ⇒ (iii) (take $X = G$).

Suppose (iii) holds. Since $\mathcal{A}(G)$ and $\mathcal{A}(X)$ are flat `O_S`-modules, one obtains, proceeding as in
11.11, that $G$ acts (on the right) faithfully on $X_{af}$ and hence acts (on the left) linearly and faithfully on the
flat quasi-coherent `O_S`-module $\mathcal{A}(X)$.

Moreover, if (iv) holds, by 11.6.1 (ii), the monomorphism $G \to \operatorname{Aut}_{O_{S}}(E)$ factors through
$G_{af}$, hence $G \to G_{af}$ is a monomorphism.

Finally, suppose (v) holds and let us show that $\rho : G \to G_{af}$ is an isomorphism. Replacing $S$ by one of its
connected components, one may suppose $S$ irreducible, with generic point $\eta$. Since the formation of $G_{af}$
commutes with flat base changes, one has $(G_{af})_{\eta} = (G_{\eta})_{af}$, and therefore the morphism $G_{\eta} \to
(G_{\eta})_{af}$ is a monomorphism, hence a closed immersion by 12.1, hence an isomorphism since $O((G_{\eta})_{af}) =
O(G_{\eta})$. If $S = \operatorname{Spec}(\kappa(\eta))$ we are done; one may therefore suppose $\dim S = 1$.

Let then $s$ be a closed point of $S$; let us show that $G_{s} \to (G_{af})_{s}$ is an isomorphism and that $\rho$ is
flat at every point of $G_{s}$. For this, one may suppose $S$ local, with closed point $s$. The morphism $\rho_{s} :
G_{s} \to (G_{af})_{s}$ obtained by base change is a monomorphism, hence a closed immersion by 12.1, hence the morphism
$O((G_{af})_{s}) \to O(G_{s})$, induced by $\rho_{s}$, is surjective. Now, by the preceding remark, it is also
injective, hence it is an isomorphism. (In particular, $\rho$ is therefore surjective.)

It then follows from Lemma 12.7 that $\rho : G \to G_{af}$ is faithfully flat. Since $G$ is quasi-compact over $S$ and
$G_{af}$ separated over $S$, $\rho$ is also quasi-compact (cf. EGA I, 6.6.4). Consequently, $\rho$ is a faithfully flat
quasi-compact monomorphism, hence an isomorphism. This proves the proposition. ∎

Finally, let us prove Prop. 2.1 of Exp. XVII, Appendix III; taking into account [Per76], Cor. 4.2.5, we have substituted
in the hypotheses "quasi-compact and quasi-separated" for "of finite type" (if one assumes $G$ of finite type, one can
use 12.1 instead of loc. cit.).

**Proposition 12.10.** *Let $S$ be a regular locally noetherian scheme of dimension $\leq 1$, $G$ an $S$-group scheme
flat, quasi-compact and quasi-separated.*

*(i) The canonical morphism $\rho : G \to G_{af}$ is faithfully flat and quasi-compact. Consequently, $G_{af}$
represents the (fpqc) sheaf quotient of $G$ by $N = Ker(\rho)$.*

*(ii) If moreover $G$ is of finite type over $S$, then $\rho$ is of finite presentation and $G_{af}$ represents the
(fppf) sheaf quotient of $G$ by $N$ and is of finite type over $S$.*

*(iii) Suppose moreover $G_{\eta}$ affine for every maximal point $\eta$ of $S$. Then $N$ is an étale $S$-group, and is
the unit group if $G$ is separated over $S$.*

<!-- label: III.VI_B.12.10 -->

*Proof.* First, since $G_{af}$ is affine, hence separated over $S$, $\rho$ is quasi-compact (cf. EGA I, 6.6.4) and the
kernel $N = Ker(\rho)$ is a closed subgroup of $G$. Moreover, replacing $S$ by one of its connected components, one may
suppose $S$ irreducible, with generic point $\eta$.

Let us remark that, to prove (i) and (ii), it suffices to show that $\rho$ is faithfully flat, because then, by Exp. IV,
5.1.7.1, $G_{af}$ represents the (fpqc) sheaf quotient of $G$ by $N$, and if moreover $G$ is of finite type over $S$,
hence of finite presentation ($S$ being locally noetherian), then, by 9.2 (xiii), $\rho$ is of finite presentation (as
is $G_{af} \to S$) and hence $\rho$ is covering for the (fppf) topology.

One may therefore suppose $S = \operatorname{Spec}(R)$, where $R$ is a discrete valuation ring (if $\dim S = 1$) or else
the field $\kappa(\eta)$ (if $\dim S = 0$). Denote by $s$ the closed point of $S$. Since the formation of $G_{af}$
commutes with flat base changes, the canonical morphism $G_{\eta} \to (G_{\eta})_{af}$ is identified with the morphism
$\rho_{\eta} : G_{\eta} \to (G_{af})_{\eta}$, and since $O((G_{af})_{\eta}) = O((G_{\eta})_{af}) = O(G_{\eta})$, then
$\rho_{\eta}$ is faithfully flat by [Per76], 4.2.5 (see also the addition VI_A, 6.6). If $\dim S = 1$, one similarly
obtains that $\rho_{s}$ is faithfully flat, since the morphism $O((G_{af})_{s}) \to O(G_{s})$ is injective, by Remark
12.8. Hence, by Lemma 12.7, $\rho$ is faithfully flat. This proves (i) and (ii). In particular, $N$ is flat over $S$.

Suppose now $G_{\eta}$ affine. Since $\rho_{\eta}$ coincides with the canonical morphism $G_{\eta} \to (G_{\eta})_{af}$,
its kernel $N_{\eta}$ is the unit group. Let us show that $N$ is étale over $S$. Since $N$ is flat over $S$, it remains
to see that $N_{s}$ is étale over $\kappa(s)$, for every point $s \neq \eta$ of $S$. There is nothing to prove if $S =
\operatorname{Spec}(\kappa(\eta))$, so one may suppose $S = \operatorname{Spec}(R)$, where $R$ is a discrete valuation
ring. Let $s$ be the closed point of $S$, $K$ the field of fractions of $R$, and $\pi$ a uniformizer. Let $x \in N_{s}$
and $U_{x}$ an affine open neighborhood of $x$ in $N$; since $N$ is flat over $S$, $U_{x} \cap N_{\eta}$ is non-empty,
hence equal to ${\epsilon(\eta)}$, where $\epsilon$ denotes the unit section. Hence $A = O(U_{x})$ is a flat
$R$-algebra, such that $A_{K} = K$ and $\pi^{-1} \notin A$ (since $\pi$ belongs to the maximal ideal of $O_{U,x}$). It
follows that $A = R$, and hence the projection $U_{x} \to S$ is an isomorphism. This proves that $N$ is étale over $S$;
if moreover $G$ is separated over $S$, then the inverse isomorphism $S \to U_{x}$ equals the unit section (since they
coincide on the dense open subset ${\eta}$ of $S = \operatorname{Spec}(R)$), hence $N$ is the unit group. The
proposition is proved. ∎

One obtains in particular the following corollary, two other proofs of which are found in [An73], Prop. 2.3.1 and
[PY06], Prop. 3.1.

**Corollary 12.10.1.** *Let $R$ be a discrete valuation ring, $K$ its field of fractions, $G$ an $R$-group scheme
separated, flat and of finite type over $R$. If `G_K` is affine, then $G$ is affine.*

<!-- label: III.VI_B.12.10.1 -->

**Remarks 12.10.2.** (a) On the one hand, O. Gabber has pointed out to us examples where $G$ is a flat group of finite
type over a discrete valuation ring, whose generic fiber is an abelian variety, and where the kernel $N$ of $G \to
G_{af}$ is not smooth.

(b) On the other hand, let us point out that M. Raynaud has given an example, for $S$ the affine plane of dimension 2
over a field $k$, of a smooth and quasi-affine $S$-group scheme, with affine and connected fibers, which is not affine
over $S$, cf. [Ray70a], § VII.3, p. 116.

<!-- label: III.VI_B.12.10.2 -->

<!-- LEDGER DELTA — Exposé VI_B — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| passage à la limite projective | passage to the projective limit | Section-title rendering. |
| schéma à groupe d'opérateurs | scheme with operator group | Kept literal; SGA 3 distinguishes "groupe d'opérateurs" from a `G`-scheme. |
| di-morphisme | di-morphism | Preserve literally for pairs `(G, H) → (G′, H′)`. |
| espace formellement homogène | formally homogeneous space | 10.15. |
| fibré principal homogène | principal homogeneous bundle | 10.15; also "`G`-torseur" → "`G`-torsor". |
| enveloppe affine | affine envelope | `G_af = Spec 𝒜(G)`, Def. 11.3. |
| `𝒜(X) = f_*(O_X)` | `𝒜(X) = f_*(O_X)` | OCR sometimes lost the script-A; restored. |
| cogèbre | coalgebra | 11.8.0; American spelling. |
| coünité | counit | OCR may produce `coÃ¼nité`; restore. |
| comodule | comodule | Standard. |
| antipode | antipode | Hopf-algebra antipode `τ`. |
| sous-comodule engendré | subcomodule generated by | 11.8. |
| descente | descent | "descend la projectivité" → "descends projectivity". |
| localement projectif | locally projective | Def. 11.9.1. |
| vecteur semi-invariant | semi-invariant vector | 11.15. |
| poids | weight | 11.15 (semi-invariant weight). |
| Norm_G(D) | `Norm_G(D)` | Stabilizer of a line; 11.16. |
| caractéristique | characteristic | 12.2 (iii): "caractéristique" = "characteristic". |
| anti-affine | anti-affine | 12.6; Brion terminology. |
| variété abélienne | abelian variety | 12.4. |
| u♮ | `u^♮` | Algebra morphism dual to a group/scheme morphism. |
| coefficients matriciels | matrix coefficients | 11.16, 13.2 (with Hopf-algebra `b_{ij}`). |
| extension par zéro | extension by zero | 11.10.1 (a). |
| « anti-affines » | "anti-affine" | Guillemets rendered as English double quotes (Grothendieckian coinage). |
| (RE) (résolution équivariante) | equivariant resolution property (RE) | 13.4 (Thomason). |
| réflexif | reflexive | Module-theoretic, regular base of dim ≤ 2. |
-->

## 13. Flat affine groups over a regular base of dimension ≤ 2

<!-- label: III.VI_B.13 -->

[^N.D.E-VI_B-D-139] Let us begin by remarking that the well-known argument which shows that every affine algebraic group
over a field $k$ is linear, as well as Lemma 11.12, extend to the case of a group scheme $G$, affine, flat, and of
finite type over a base scheme $S$ which is noetherian, regular, of dimension $\leq 2$. For $S$ of dimension $\leq 1$,
this proves point (b) of Remark 11.11.1. The extension to the case $\dim S = 2$ rests on the following lemma, which was
communicated to us by O. Gabber.

**Lemma 13.1.** *Let $S$ be a normal noetherian scheme, $\mathcal{A}$ a flat quasi-coherent `O_S`-module, $\mathcal{F}$
a quasi-coherent `O_S`-submodule of finite type of $\mathcal{A}$, $\mathcal{F}**$ its bidual, and $U$ the flatness locus
of $\mathcal{F}$, i.e. the set of points $s \in S$ such that $\mathcal{F}_{s}$ is a flat $O_{S,s}$-module.*

*(i) $U$ is an open subset of $S$ and $\mathcal{F}** = j_{*} j*(\mathcal{F})$, where $j$ denotes the inclusion $U
\hookrightarrow X$.*

*(ii) The canonical morphism $j_{*}(\mathcal{E}) \otimes_{O_{S}} \mathcal{A} \to j_{*}(\mathcal{E} \otimes_{O_{U}}
j*(\mathcal{A}))$ is an isomorphism, for every quasi-coherent `O_U`-module $\mathcal{E}$.*

*(iii) In particular, $\mathcal{V} = j_{*} j*(\mathcal{F})$ is a submodule of $\mathcal{A} = j_{*} j*(\mathcal{A})$, and
the canonical morphism $\mathcal{V} \otimes_{O_{S}} \mathcal{A} \to j_{*} j*(\mathcal{F} \otimes_{O_{S}} \mathcal{A})$
is an isomorphism.*

<!-- label: III.VI_B.13.1 -->

*Proof.* Replacing $S$ by one of its connected components, we may suppose $S$ integral. By EGA IV₂, 2.1.12, the flatness
locus of $\mathcal{F}$, i.e. the set of points $s \in S$ such that $\mathcal{F}_{s}$ is a flat $O_{S,s}$-module, is an
open subset $U$ of $S$; denote by $j$ the inclusion $U \hookrightarrow S$. Since $\mathcal{A}_{s}$ is flat, hence
torsion-free, so is $\mathcal{F}_{s}$,

<!-- original page 436 -->

so $U$ contains every point of codimension $\leq 1$. Consequently, by [BAC], VII, § 4.2, cor. of th. 1, one has
$\mathcal{F}** = j_{*} j*(\mathcal{F})$, and one therefore obtains a monomorphism $\mathcal{F}** \to j_{*}
j*(\mathcal{A})$.

The proof of (ii) is analogous to that of EGA III, 1.4.15, recalled in 11.0. On the other hand, since $S$ is normal, the
morphism $O_{S} \to j_{*} j*(O_{S})$ is an isomorphism (cf. EGA IV₂, 5.8.6 and 5.10.5). By (ii) applied to $\mathcal{E}
= O_{U}$, one therefore has $\mathcal{A} = j_{*} j*(\mathcal{A})$. Finally, since $j*(\mathcal{F} \otimes_{O_{S}}
\mathcal{A}) = j*(\mathcal{F}) \otimes_{O_{U}} j*(\mathcal{A})$, the final assertion of (iii) follows from (ii) applied
to $\mathcal{E} = j*(\mathcal{F})$. The lemma is proved. ∎

Furthermore, recall that a finitely generated $R$-module $M$ is said to be *reflexive* if the canonical morphism from
$M$ to its bidual $M**$ is an isomorphism. When $R$ is a noetherian regular ring of dimension $\leq 2$, this entails
that $M$ is projective. Indeed, for every finitely generated $R$-module $N$, consider a resolution $L_{1} \to L_{0} \to
N \to 0$, where `L_0` and `L_1` are finitely generated free $R$-modules; then one has an exact sequence

```text
0 ⟶ N* ⟶ L_0* ⟶ L_1* ⟶ Q ⟶ 0,
```

where $Q$ denotes the cokernel of $L_{0}* \to L_{1}*$, and since $R$ is of homological dimension $\leq 2$ (cf. [BAC], X
§ 4.2, cor. 1 of th. 1), it follows that $N*$ is projective.

**Proposition 13.2.** *Let $S$ be a noetherian regular scheme of dimension $\leq 2$, $G$ an affine flat $S$-group,
$\mathcal{A}(G)$ its affine algebra.*

*(i) If $G$ is of finite type over $S$, it is isomorphic to a closed subgroup of $H =
\operatorname{Aut}_{O_{S}}(\mathcal{V})$, for some `O_S`-module $\mathcal{V}$ locally free of finite rank. If moreover
$S$ is affine, one may take $\mathcal{V} = O^{\oplus d}_{S}$ for some $d$, whence $H = GL_{d,S}$.*

*(ii) $\mathcal{A}(G)$ is a filtered inductive limit of flat `O_S`-sub-Hopf-algebras of finite type.*

<!-- label: III.VI_B.13.2 -->

*Proof.* Let $\mathcal{B}$ be a finitely generated `O_S`-subalgebra of $\mathcal{A}(G)$. Since every coherent module on
an open of $S$ extends to a coherent module on $S$ (cf. EGA I, 9.4.5), there exists a coherent `O_S`-submodule
$\mathcal{M}$ of $\mathcal{B}$ which generates $\mathcal{B}$ as an `O_S`-algebra (loc. cit., 9.6.5). By 11.10.bis,
$\mathcal{M}$ is contained in a coherent $G$-stable `O_S`-submodule $\mathcal{F}$. (N.B. Since $G$ is here affine over
$S$, the proof of loc. cit. is written more simply: one may there replace $f_{*} f*(\mathcal{E})$ by $\mathcal{E}
\otimes_{O_{S}} \mathcal{A}(G)$, etc.)

Let $j$ be the inclusion $U \hookrightarrow S$, where $U$ denotes the flatness locus of $\mathcal{F}$. By Lemma 13.1 and
the remarks following it, $\mathcal{V} = j_{*} j*(\mathcal{F})$ is a locally free `O_S`-submodule of $\mathcal{A}(G)$,
and since the canonical morphism

```text
𝒱 ⊗ 𝒜(G) ⟶ j_* j*(ℱ ⊗ 𝒜(G))
```

is an isomorphism, $\mathcal{V}$ is a $G$-submodule of $\mathcal{A}(G)$. The action of $G$ on $\mathcal{V}$ then induces
a morphism of affine $S$-groups $\rho_{\mathcal{V}} : G \to H = \operatorname{Aut}_{O_{S}}(\mathcal{V})$ and hence a
morphism of `O_S`-Hopf algebras $\phi_{\mathcal{V}} : \mathcal{A}(H) \to \mathcal{A}(G)$. Denote by
$\mathcal{A}_{\mathcal{V}}$ the image of $\phi_{\mathcal{V}}$; this is the affine algebra of a closed subgroup
$G_{\mathcal{V}}$ of $H$, which is the closed image of $\rho_{\mathcal{V}}$. Let us show that
$\mathcal{A}_{\mathcal{V}}$ contains $\mathcal{B}$.

The question being local on $S$, one may suppose $S = \operatorname{Spec}(R)$ and $V = \Gamma(S, \mathcal{V})$ is a free
$R$-module with basis $v_{1}, \cdots, v_{n}$; in this case $H \simeq GL_{n,R}$ and $\mathcal{A}(H)$ is generated as an
$R$-algebra by the "matrix coefficients" $c_{ij}$ and the element $d^{-1}$, where

<!-- original page 437 -->

$d$ denotes the determinant. Let $\Delta$ (resp. $\epsilon$) be the comultiplication (resp. the augmentation) of $A$.
For $j = 1, \cdots, n$, write $\Delta(v_{j}) = \sum^{n}_{i=1} v_{i} \otimes a_{ij}$; then $a_{ij} = \phi(c_{ij})$
belongs to $Im(\phi)$. On the other hand, since $V$ is an $R$-submodule of $A$, one can use the identity $(\epsilon
\otimes id_{A}) \circ \Delta = id_{A}$, which entails that $v_{j} = \sum_{i} \epsilon(v_{i}) a_{ij}$ belongs to
$Im(\phi)$. Since $V$ contains a system of generators of $B = \Gamma(S, \mathcal{B})$, it follows that $B \subset
Im(\phi)$.

If $G$ is of finite type over $S$, one may take $\mathcal{B} = \mathcal{A}(G)$ and $\phi$ is then surjective, so the
morphism of $S$-groups $G \to H = \operatorname{Aut}_{O_{S}}(\mathcal{V})$ is a closed immersion.

If moreover $S$ is affine, there exists a locally free `O_S`-module $\mathcal{V}'$ of finite rank such that $\mathcal{V}
\oplus \mathcal{V}' = O^{d}_{S}$ as `O_S`-modules. Regarding $\mathcal{V}'$ as a trivial $G$-module, one may replace
$\mathcal{V}$ by $O^{d}_{S}$, and one thus obtains that $G$ is a closed subgroup of $GL_{d,S}$.

Finally, let us return to the case of an arbitrary flat affine $S$-group $G$. By EGA I, 9.4.9, $\mathcal{A}(G)$ is the
union of its coherent `O_S`-submodules $\mathcal{M}$, hence also of the `O_S`-sub-Hopf-algebras
$\mathcal{A}_{\mathcal{V}}$ as above, whence (ii). ∎

**Example 13.3.** *Let $R$ be a discrete valuation ring, with uniformizer $\pi$ and field of fractions $K$. Consider the
filtered projective system of $R$-groups:*

```text
···  ⟶  G_{a,R}  ⟶^{×π}  G_{a,R}  ⟶^{×π}  G_{a,R}
```

*(corresponding to the inductive system $R[X_{0}] \to R[X_{1}] \to R[X_{2}] \to \cdots$, where the transition morphisms
are given by $X_{n} = \pi X_{n+1}$). Its projective limit $G$ is a flat affine $R$-group scheme, not of finite type,
whose special fiber is trivial and whose generic fiber is $G_{a,K}$; the affine $R$-algebra $\mathcal{A}(G)$ is the
subring of `K[X]` formed of polynomials whose constant coefficient belongs to $R$. (N.B. We have already encountered
this example in Remark 11.10.1.) Note that $G$ represents the functor which to every $R$-algebra $B$ associates the set
of sequences $(x_{n})_{n \in \mathbb{N}}$ of elements of $B$ such that $x_{n} = \pi x_{n+1}$ for every $n$. (In
particular, each $x_{n}$ is indefinitely $\pi$-divisible.)*

<!-- label: III.VI_B.13.3 -->

Now let $S$ be a noetherian scheme such that every coherent `O_S`-module is the quotient of a locally free `O_S`-module
of finite type; this is the case, for example, if $S$ is a separated noetherian regular scheme, cf. SGA 6, Exp. II,
2.1.1 and 2.2.7. (One can show that every noetherian regular scheme of dimension $\leq 1$ also has this property; on the
other hand, it fails when $S$ is the affine plane over a field $k$ with the origin doubled, cf. loc. cit., 2.2.7.2.)

**Definition 13.4.** *Let $G$ be a flat affine $S$-group. Following R. W. Thomason ([Th87], 2.1), we say that the pair
$(G, S)$ possesses the* equivariant resolution property\*, or satisfies (RE), if for every coherent $G$-`O_S`-module
$\mathcal{F}$, there exists a locally free $G$-`O_S`-module $\mathcal{E}$ of finite rank and a $G$-equivariant
epimorphism $\mathcal{E} \to \mathcal{F}$.\*

<!-- label: III.VI_B.13.4 -->

In loc. cit., Th. 3.1, Thomason proves the result below, under the hypothesis that $G$ is essentially free over $S$ (cf.
the remark further on). Gabber pointed out to us the simpler proof below, which does not use this hypothesis.

**Proposition 13.5.** *Let $S$ be a noetherian scheme and $G$ an $S$-group affine, flat, and of finite type, with affine
algebra $\mathcal{A}(G)$. Suppose that $(G, S)$ satisfies (RE). Then:*

<!-- original page 438 -->

*(i) $G$ is isomorphic to a closed subgroup of $H = \operatorname{Aut}_{O_{S}}(\mathcal{V})$, for some `O_S`-module
$\mathcal{V}$ locally free of finite rank.*

*(ii) If moreover $S$ is affine, one may take $\mathcal{V} = O^{\oplus d}_{S}$ for some $d$, whence $H = GL_{d,S}$.*

<!-- label: III.VI_B.13.5 -->

The proof is analogous to that of 13.2. As in loc. cit., there exists a coherent $G$-stable `O_S`-submodule
$\mathcal{F}$ which generates $\mathcal{A} = \mathcal{A}(G)$ as an `O_S`-algebra. Replacing $S$ by one of its connected
components, we may suppose $S$ connected. By hypothesis (RE), there exists a locally free $G$-`O_S`-module $\mathcal{E}$
of rank $n$, and an epimorphism of $\mathcal{A}$-comodules $\pi : \mathcal{E} \to \mathcal{F}$. Set $H =
\operatorname{Aut}_{O_{S}}(\mathcal{E})$; this is an $S$-group scheme, locally isomorphic to $GL_{n,S}$. The action of
$G$ on $\mathcal{E}$ induces a morphism of affine $S$-groups $\rho : G \to H$, corresponding to a morphism of `O_S`-Hopf
algebras $\phi : \mathcal{A}(H) \to \mathcal{A}(G)$. Let us show that $\rho$ is a closed immersion.

The question being local on $S$, one may suppose $S = \operatorname{Spec}(R)$ and $V = \Gamma(S, \mathcal{E})$ is a free
$R$-module with basis $v_{1}, \cdots, v_{n}$; in this case $H \simeq GL_{n,R}$ and $B = \Gamma(S, \mathcal{A}(H))$ is
generated as an $R$-algebra by the "matrix coefficients" $c_{ij}$ and the element $d^{-1}$, where $d$ denotes the
determinant. Let $\Delta$ (resp. $\epsilon$) be the comultiplication (resp. the augmentation) of $A = \Gamma(S,
\mathcal{A}(G))$, let $\mu : V \to V \otimes_{R} A$ be the $A$-comodule structure on $V$, and let $F = \Gamma(S,
\mathcal{F})$. For $j = 1, \cdots, n$, write

```text
μ(v_j) = ∑_{i=1}^n v_i ⊗ a_{ij}
```

then $\phi(c_{ij}) = a_{ij}$. On the other hand, since $\pi : V \to F$ is a morphism of $A$-comodules, one has

```text
∑_{i=1}^n π(v_i) ⊗ a_{ij} = (π ⊗_R id_A)(μ(v_j)) = Δ(π(v_j))
```

and therefore

```text
π(v_j) = (ε ⊗_R id_A) Δ(π(v_j)) = ∑_{i=1}^n (ε π(v_i)) a_{ij} = φ(∑_{i=1}^n (ε π(v_i)) c_{ij}).
```

Hence $\phi(B)$ contains $\pi(V) = F$, which generates $A$ as an $R$-algebra, and hence $\phi$ is surjective. This shows
that $\rho$ is a closed immersion, whence assertion (i).

If moreover $S$ is affine, there exists a locally free `O_S`-module $\mathcal{V}'$ of finite rank such that $\mathcal{V}
\oplus \mathcal{V}' = O^{d}_{S}$ as `O_S`-modules. Regarding $\mathcal{V}'$ as a trivial $G$-module, one may replace
$\mathcal{V}$ by $O^{d}_{S}$, and one thus obtains that $G$ is a closed subgroup of $GL_{d,S}$. The proposition is
proved. ∎

**Remarks 13.6.** (a) For the sake of completeness, let us briefly sketch Thomason's argument ([Th87], Th. 3.1), keeping
the preceding notation. The $G$-equivariant epimorphism $\pi : \mathcal{E} \to \mathcal{F}$ induces a closed immersion
$\tau : G \to V(\mathcal{E})$ such that $\tau(g' g) = \tau(g') \cdot g$ (N.B.: $G$ acts on the right on
$V(\mathcal{E})$), and one has an isomorphism $H \simeq \operatorname{Aut}_{O_{S}}(V(\mathcal{E}))^{op}$, which is
compatible with the actions of $G$ on the left on $\mathcal{E}$ and on the right on $V(\mathcal{E})$. Now let $N$ be the
strict transporter $Transp^{str}_{H}(\tau(G), \tau(G))$; when $G$ is essentially free over $S$, it follows from 6.2.4 e)
that $N$ is a closed subgroup scheme of $H$, hence affine over $S$. Moreover, $\rho$ factors through a

<!-- original page 439 -->

morphism of $S$-groups $\rho' : G \to N$. On the other hand, for every $S' \to S$ and $h \in N(S')$, set $\pi(h) =
\tau(1) \cdot h$ (where `1` is the unit element of $G(S')$); this defines a morphism of $S$-schemes $\pi : N \to
\tau(G)$, which is a retraction of $\rho'$ (when one identifies $G$ with $\tau(G)$). Since $N$ is separated over $S$, it
follows that $\rho'$ is a closed immersion.

(b) It seems that the proof of [Th87], Th. 3.1 requires the hypothesis that $G$ be essentially free over $S$, which does
not appear in loc. cit. (the author invoking in its place the fact that $H$ is essentially free). This hypothesis is
however satisfied when $G$ is reductive (cf. Exp. XXII 5.7.8), and so is satisfied in all the cases considered in loc.
cit., Cor. 3.2. In particular, Thomason proves in loc. cit., 2.5, that if $S$ is separated noetherian regular of
dimension $\leq 2$, and if $G$ is affine, of finite presentation, and such that $\mathcal{A}(G)$ is a locally projective
`O_S`-module, then $(G, S)$ satisfies (RE); by 13.5, this gives 13.2 under a slightly more restrictive hypothesis.

<!-- label: III.VI_B.13.6 -->

To conclude, let us point out that the proof of [Th87], 2.5, may be slightly simplified, as follows. (For brevity, we
place ourselves in the situation where $S = \operatorname{Spec}(R)$ is affine.)

**Proposition 13.7.** *Let $R$ be a noetherian regular ring of dimension $\leq 2$, $C$ an $R$-coalgebra, projective as
an $R$-module, and $F$ a $C$-comodule, of finite type over $R$. Then $F$ is the quotient of a $C$-comodule $V$,
projective of finite type over $R$.*

<!-- label: III.VI_B.13.7 -->

*Proof.* Replacing $\operatorname{Spec}(R)$ by one of its connected components, one may suppose $R$ integral, with field
of fractions $K$. Denote by $\Delta$ (resp. $\epsilon$) the comultiplication (resp. the augmentation) of $C$ and by
$\rho : F \to F \otimes C$ the comodule structure on $F$. Let $\pi : W \to F$ be a surjective morphism, where $W$ is a
free $R$-module of finite rank. We endow $W \otimes C$ with the comodule structure defined by $id_{W} \otimes \Delta$,
and similarly for $F \otimes C$. Then $\rho : F \to F \otimes C$ is a morphism of $C$-comodules, which admits $id_{F}
\otimes \epsilon$ as a section.

Let $W'$ be the $C$-comodule defined by the cartesian square below:

```text
W′ ─────────⟶ F
│             │
│ π ⊗ id_C   │ ρ
↓             ↓
W ⊗ C ──────⟶ F ⊗ C
```

i.e. $W'$ is identified with the kernel of the morphism $W \otimes C \to (F \otimes C)/\rho(F)$, and the projection
$\pi' : W' \to F$, given by $x \mapsto (\pi \otimes \epsilon)(x)$, is surjective. Since $F$ is a finitely generated
$R$-module, there exists a subcomodule $V'$ of $W'$, finitely generated over $R$, such that $\pi'(V') = F$. Since $W
\otimes C$ is $R$-torsion-free, so is $V'$; hence, replacing $F$ by $V'$, one may assume at the outset that $F$ is
torsion-free.

Applying the preceding construction to this new $F$, one obtains $V'$ as above. Consider then the subcomodule $V$,
kernel of the morphism

```text
W ⊗ C ⟶ E = (W ⊗ C ⊗ K) / (V′ ⊗ K).
```

Then $V$ contains $V'$, and $Q = (W \otimes C)/V$ is an $R$-submodule of the $K$-vector space $E$; set $Q' = E/Q$. Since
$W \otimes C$ and $E$ are flat $R$-modules, one obtains that,

<!-- original page 440 -->

for every $R$-module $N$,

```text
Tor₁^R(V, N) ≃ Tor₂^R(Q, N) ≃ Tor₃^R(Q′, N)
```

and since $R$ is regular of dimension $\leq 2$, the right-hand term is zero. This shows that $V$ is a flat $R$-module.
Let us finally show that $V$ is a finitely generated $R$-module. Set $M = W \otimes C$; it follows from the definition
that $V/V'$ is isomorphic to the $R$-torsion submodule $(M/V')_{tors}$ of $M/V'$.

Since $M$ is a projective $R$-module, there exists a projective $R$-module $P$ such that $M \oplus P$ is a free
$R$-module $L$. Then $(M/V')_{tors} \simeq (L/V')_{tors}$. On the other hand, since $V'$ is of finite type, there exists
a direct factor $L' \simeq R^{n}$ of $L$ such that $V' \subset L'$, and one therefore also has $(L/V')_{tors} \simeq
(L'/V')_{tors}$, and the latter is of finite type since $(L'/V')$ is. Consequently, $V$ is a flat $R$-module of finite
type, hence projective of finite type ($R$ being noetherian). Proposition 13.7 is proved. ∎

## Bibliography

[^N.D.E-VI_B-D-140]

[An73] S. Anantharaman, *Schémas en groupes, espaces homogènes et espaces algébriques sur une base de dimension 1*, Mém.
Soc. Math. France **33** (1973), 5–79.

[Ba55] I. Barsotti, *Un teorema di struttura per le varietà gruppali*, Atti Acad. Naz. Lincei Rend. Cl. Sci. Fis. Mat.
Nat. **18** (1955), 43–50.

[BLR] S. Bosch, W. Lütkebohmert, M. Raynaud, *Néron Models*, Springer-Verlag, 1990.

[BAC] N. Bourbaki, *Algèbre commutative*, Chap. I–IV, V–VII et X, Masson, 1985 et 1998.

[BTop] N. Bourbaki, *Topologie générale*, Chap. I–IV, Hermann, 1971.

[Br09] M. Brion, *Anti-affine algebraic groups*, J. Algebra **321** (2009), no. 3, 934–952.

[Ch60] C. Chevalley, *Une démonstration d'un théorème sur les groupes algébriques*, J. Maths. Pure Appl. **39** (1960),
307–317.

[Co02] B. Conrad, *A modern proof of Chevalley's theorem on algebraic groups*, J. Ramanujan Math. Soc. **17** (2002),
1–18.

[DG70] M. Demazure, P. Gabriel, *Groupes algébriques*, Masson & North-Holland, 1970.

[Gr73] L. Gruson, *Dimension homologique des modules plats sur un anneau noethérien*, Symposia Mathematica **XI**
(1973), 243–254.

[Kn71] D. Knutson, *Algebraic spaces*, Lect. Notes Maths. **203**, Springer-Verlag, 1971.

[Ma07] B. Margaux, *Passage to the Limit in Non-Abelian Čech Cohomology*, J. Lie Theory **17** (2007), 591–596.

[MW94] A. Masuoka, D. Wigner, *Faithful flatness of Hopf algebras*, J. Algebra **170** (1994), 156–184.

<!-- original page 441 -->

[Per76] D. Perrin, *Approximation des schémas en groupes, quasi-compacts sur un corps*, Bull. Soc. Math. France **104**
(1976), 323–335.

[Pes66] C. Peskine, *Une généralisation du "Main Theorem" de Zariski*, Bull. Sci. Math. **90** (1966), 119–127.

[PY06] G. Prasad, J.-K. Yu, *On quasi-reductive group schemes*, J. Alg. Geom. **15** (2006), 507–549.

[Ray70a] M. Raynaud, *Faisceaux amples sur les schémas en groupes et les espaces homogènes*, Lect. Notes Maths. **119**,
Springer-Verlag, 1970.

[Ray70b] M. Raynaud, *Anneaux locaux henséliens*, Lect. Notes Maths. **169**, Springer-Verlag, 1970.

[RG71] M. Raynaud, L. Gruson, *Critères de platitude et de projectivité*, Invent. math. **13** (1971), 1–89.

[Ro56] M. Rosenlicht, *Some basic theorems on algebraic groups*, Amer. J. Math. **78** (1956), 401–443.

[SS09] C. Sancho de Salas, F. Sancho de Salas, *Principal bundles, quasi-abelian varieties and structure of algebraic
groups*, J. Algebra **322** (2009), no. 8, 2751–2772.

[Se68] J.-P. Serre, *Groupes de Grothendieck des schémas en groupes réductifs déployés*, Publ. math. I.H.É.S. **34**
(1968), 37–52.

[Se99] C. S. Seshadri, *Chevalley: some reminiscences*, Transform. Groups **4** (1999), nos. 2–3, 119–125.

[Ta72] M. Takeuchi, *A correspondence between Hopf ideals and sub-Hopf algebras*, Manuscripta Math. **7** (1972),
251–270.

[Ta79] M. Takeuchi, *Relative Hopf modules — Equivalences and freeness criteria*, J. Algebra **60** (1979), 452–471.

[Th87] R. W. Thomason, *Equivariant resolution, linearization, and Hilbert's fourteenth problem over arbitrary base
schemes*, Adv. Math. **65** (1987), 16–34.

<!-- LEDGER DELTA — Exposé VI_B — for consolidation in Phase 3 (chunk-D add-on)
| French | English | Note |
| ------ | ------- | ---- |
| lieu de platitude | flatness locus | 13.1; the set of points where the module is flat. |
| bidual | bidual | 13.1; `M**` = double `R`-dual. Standard English. |
| réflexif | reflexive | Of finitely generated `R`-modules; bidual map is an isomorphism. |
| dimension homologique | homological dimension | 13.1 rappel; cf. [BAC] X § 4.2. |
| sous-G-module | `G`-submodule | 13.2; submodule stable under the `G`-action. |
| sous-OS-module G-stable | `G`-stable `O_S`-submodule | 13.2, 13.5; coherent submodule preserved by the comodule structure. |
| coefficients matriciels | matrix coefficients | 13.2, 13.5; Hopf-algebra generators of `𝒜(GL_n)`. |
| comultiplication | comultiplication | `Δ`. Standard. |
| augmentation | augmentation | `ε`. Standard. |
| algèbre affine | affine algebra | `𝒜(G)`. Already in chunk-C ledger. |
| sous-Hopf-algèbre plate | flat sub-Hopf-algebra | 13.2 (ii). |
| limite inductive filtrante | filtered inductive limit | 13.2 (ii). Already standard. |
| système projectif filtrant | filtered projective system | 13.3. Inverse system indexed by a filtered category. |
| fibre spéciale / générique | special / generic fiber | 13.3. |
| indéfiniment π-divisible | indefinitely `π`-divisible | 13.3; `xn = π x_{n+1}` for all `n`. |
| propriété de résolution équivariante (RE) | equivariant resolution property (RE) | 13.4; following Thomason [Th87]. Already in chunk-C ledger. |
| G-OS-module | `G`-`O_S`-module | 13.4; an `O_S`-module endowed with a `G`-action. |
| épimorphisme G-équivariant | `G`-equivariant epimorphism | 13.4. |
| transporteur strict | strict transporter | 13.6 (a); `Transp^{str}_H(τ(G), τ(G))`. |
| essentiellement libre | essentially free | 13.6; Thomason's hypothesis on `G` (or `H`) over `S`. |
| localement projectif | locally projective | 13.6 (b); already in chunk-C ledger (Def. 11.9.1). |
| R-cogèbre | `R`-coalgebra | 13.7; "cogèbre" → "coalgebra", American spelling. |
| C-comodule | `C`-comodule | 13.7. Already in chunk-C ledger. |
| sans R-torsion / sans torsion | `R`-torsion-free / torsion-free | 13.7. |
| sous-module de R-torsion | `R`-torsion submodule | 13.7; `(M/V′)_{tors}`. |
| facteur direct | direct summand / direct factor | 13.7; kept as "direct factor" to match the French structure of the argument. |
| carré cartésien | cartesian square | 13.7; pullback diagram. |
| rétraction | retraction | 13.6 (a); section in the opposite direction. |
| section unité | unit section | (Carried over from §12; mentioned implicitly in 13.6 (a) via `τ(1)`.) |
| algèbre de Hopf (sous-) | (sub-) Hopf algebra | 13.2 (ii). Standard. |
| OS-module localement libre de rang fini | locally free `O_S`-module of finite rank | 13.2 (i), 13.5 (i). |
| GLd,S | `GL_{d,S}` | 13.2, 13.5; relative general linear group. |
| AutOS(V) | `Aut_{O_S}(𝒱)` | 13.2, 13.5; automorphism group scheme of a locally free module. |
| V(ℰ) | `V(ℰ)` | 13.6 (a); the linear `S`-scheme `Spec Sym ℰ*` (covariant linear-scheme functor). |
-->

[^VI_B-0-1]: This Exposé has been seriously reworked since its mimeographed edition; in particular, §§ 10 and 11 have
    been entirely rewritten.[^N.D.E-VI_B-1]

[^N.D.E-VI_B-2]: Recall the convention adopted at the beginning of `VI_A`: an $A$-group is an $A$-group scheme (and such
    a scheme is separated, cf. (VI_A, 0.3)).

[^N.D.E-VI_B-3]: We have replaced "homomorphism" by "morphism".

[^N.D.E-VI_B-4]: This statement also appears in (VI_A, 2.5.2).

[^N.D.E-VI_B-5]: In the original, 1.3, 1.3.1, and 1.3.1.1 are stated for $A$ a field. For completeness, we have treated
    the case of an Artinian local ring; to do so, we have added Lemma 1.3.0.

[^N.D.E-VI_B-6]: Recall that a morphism of schemes $f : X \to Y$ is said to be *of finite type* (resp. *of finite
    presentation*, resp. *quasi-finite*) *at $x$* if there exist affine opens $V$ containing $f(x)$ and $U$ containing
    $x$ such that $f(U) \subset V$ and $O_{X}(U)$ is an $O_{Y}(V)$-algebra of finite type (resp. of finite presentation,
    resp. and moreover the fiber $f^{-1}(f(x'))$ is finite for all $x' \in U$; see also N.D.E. (40) of Exp. V). One says
    that $f$ is *locally quasi-finite* (resp. *of finite type*, *of finite presentation*) if it has this property at
    every point $x$. On the other hand, one says that $f$ is *smooth* (resp. *unramified*, resp. *étale*) *at $x$* if
    there exists an open neighborhood $U$ of $x$ such that the morphism $f|_{U} : U \to Y$ is smooth (resp. unramified,
    resp. étale). In view of these definitions, it is clear that the set of points where $f$ is of finite presentation,
    resp. of finite type, quasi-finite, smooth, unramified, étale, is open in $X$. Moreover, since the flat locus of a
    morphism locally of finite presentation is open (EGA IV₃, 11.3.1), the set of points of $X$ where $f$ is of finite
    presentation and flat is also open in $X$. All of this will be used repeatedly in what follows.

[^N.D.E-VI_B-7]: The original stated that $W_{flat}$ is open, which does not seem a priori obvious...

[^N.D.E-VI_B-8]: Note that it does not suffice to assume that $G$ is flat over $A$ at one point: for instance, suppose
    $A \neq k$, let $H$ be the constant $A$-group $(\mathbb{Z}/2\mathbb{Z})_{A}$ and $G$ the closed $A$-subgroup of $H$
    whose non-neutral component is reduced; then the structural morphism $G \to \operatorname{Spec} A$ is a local
    isomorphism at the unit point $e$, but is not flat at the point $g \neq e$.

[^N.D.E-VI_B-9]: We have added the following sentence, and simplified the proof of Lemma 1.3.1.1, by invoking EGA IV,
    2.7.1 instead of loc. cit., 17.7.5.

[^N.D.E-VI_B-10]: We have expanded the original in what follows.

[^N.D.E-VI_B-11]: The original invoked the generic flatness theorem (EGA IV₂, 6.9.1), which is not necessary here.

[^N.D.E-VI_B-12]: We have added the following sentence.

[^N.D.E-VI_B-13]: We have expanded the original in what follows.

[^N.D.E-VI_B-14]: We have expanded the original in what follows.

[^N.D.E-VI_B-15]: The hypothesis that $G$ and $H$ are locally of finite type may be removed, since according to \[Per76,
    4.2.4\]: every quasi-compact monomorphism $u : G \to H$ between group schemes over a field $k$ is a closed
    immersion; see also [DG70, III.3.7.2 b)] for the case where $G$ and $H$ are affine (in which case every morphism $G
    \to H$ is affine (EGA II, 1.6.2 (v)), hence quasi-compact).

[^N.D.E-VI_B-16]: In this particular case, see also (VI_A, 0.5.2), valid without finiteness hypotheses.

[^N.D.E-VI_B-17]: The implication (ii) ⇒ (i) is a general fact (cf. EGA 0_IV, 14.1.6), and (i) ⇒ (ii) follows from the
    fact that if $X$ is an irreducible scheme of finite type over a field, one has $\dim X = \dim U$ for every non-empty
    open subset $U$ of $X$; the essential point here is therefore to establish assertion (i), which has already been
    done in an addition to (VI_A, 2.4.1). We have modified the statement and proof of the lemma accordingly.

[^N.D.E-VI_B-18]: In the statement, we have replaced "along the unit section" by "at every point of the unit section";
    on the other hand, at the end of the proof, we have made explicit the results of EGA IV₄ cited in reference.

[^N.D.E-VI_B-19]: In case (i), the open subset $V$ is formed by all the points of $G$ at which $u$ is smooth, resp.
    étale, resp. of finite presentation and flat, cf. N.D.E. (6). On the other hand, in case (ii), $V$ is the largest
    open subset contained in the set $E$ of points of $G$ at which $u$ is universally open, but $E$ is not necessarily
    open, as shown by the following example (EGA IV₃, 14.1.3 (i)): let $k$ be a field, $H = S = \operatorname{Spec} A$
    with $A = k[x]$, and $G$ the $S$-group $\operatorname{Spec} A[y]/(xy)$; then $E$ equals the unit section of $G$,
    which is not open.

[^N.D.E-VI_B-20]: We have expanded the statement and the proof, and in (i) we have weakened the hypothesis on $H$ by
    replacing "of finite presentation" by "of finite type".

[^N.D.E-VI_B-21]: We have modified the presentation, separating the assertions relative to the "quasi-finite" case from
    those relative to the "unramified" case.

[^VI_B-2-9-i]: This is also a particular case of EGA IV₄, 18.12.11, since $\pi$ is evidently a universal homeomorphism.

[^VI_B-2-9-ii]: This is also an immediate consequence of EGA IV₄, 18.12.6.

[^VI_B-2-9-1]: Cf. EGA IV₄, 18.12.7.1 for a slightly more general result, provable by the same proof.

[^N.D.E-VI_B-22]: This is a slightly abusive notation, but one which is compatible with the notations of (VI_A, 2.3)
    when this connected component is the underlying topological space of an open group subscheme $G^{0}$ of $G$, cf.
    (VI_A, 2.2.bis).

[^N.D.E-VI_B-23]: We have added what follows.

[^N.D.E-VI_B-24]: Recall the following definitions and results (cf. EGA 0_III, § 9.1 and EGA IV₁, §§ 1.8 and 1.9). Let
    $X$ be a topological space. (i) An open $U$ of $X$ is called *retrocompact* if the inclusion $U \hookrightarrow X$
    is quasi-compact, i.e. if $U \cap V$ is quasi-compact for every quasi-compact open $V \subset X$. (ii) A part $C$ of
    $X$ is called *constructible* if it is a finite union of parts of the form $U - V$, where $U$ and $V$ are
    retrocompact opens in $X$. (iii) A part $L$ of $X$ is called *locally constructible* if for every $x \in X$ there
    exists an open neighborhood $U$ of $x$ in $X$ such that $L \cap U$ is constructible in $U$. (N.B. If $X$ is
    quasi-compact and quasi-separated, $L$ is then constructible.) (iv) A part $I$ of $X$ is called *ind-constructible*
    if for every $x \in X$, there exists an open neighborhood $U$ of $x$ in $X$ such that $I \cap U$ is a union of parts
    locally constructible in $U$. Let now $f : X \to Y$ be a morphism of schemes. By Chevalley's constructibility
    theorem (cf. EGA IV₁, 1.8.4 and 1.9.5 (viii)), if $f$ is of finite presentation (resp. locally of finite
    presentation), then the image under $f$ of any locally constructible part is locally constructible (resp.
    ind-constructible).

[^N.D.E-VI_B-25]: We have expanded the original in what follows.

[^N.D.E-VI_B-26]: Compare with (VI_A, 5.6).

[^N.D.E-VI_B-27]: We have shortened the original, referring here to 1.3.2. We have also simplified the argument below by
    removing a reference to the generic flatness theorem (EGA IV₂, 6.9.1), which is not necessary here.

[^N.D.E-VI_B-28]: One finds in the original: "at the points of $\epsilon(s)$"; it is not sufficient to assume that $G$
    is universally open over $S$ at $\epsilon(s)$, as shown by the example given in N.D.E. (19). We have corrected the
    proof accordingly.

[^N.D.E-VI_B-29]: We have added condition (iii), pointed out by O. Gabber; it will be useful later (5.7).

[^N.D.E-VI_B-30]: The preceding has been communicated to us by O. Gabber; we have also preserved the proof of the
    implication (ii) ⇒ (i) given in the original.

[^N.D.E-VI_B-31]: One cannot do without the hypothesis that $S$ is reduced here: if $k$ is a field, $S =
    \operatorname{Spec} A$, where $A = k[\delta]$ with $\delta^{2} = 0$, and $G$ the closed subgroup
    $\operatorname{Spec} A[X]/(\delta X)$ of $G_{a,S}$ (which to every $A$-algebra $R$ associates the subgroup of $r \in
    R$ such that $\delta r = 0$), then $G$ is an $S$-group satisfying (ii)–(iv), but is not flat, hence not smooth, over
    $S$.

[^N.D.E-VI_B-32]: We have expanded the original in what follows.

[^N.D.E-VI_B-33]: We have replaced "Artinian" by "of dimension 0" (and mentioned this generalization in (VI_A, 0.3)).

[^N.D.E-VI_B-34]: We have corrected the original by assuming $G$ universally open over $S$ in a neighborhood of the unit
    section and by adding hypothesis (ii); see below for examples, due to O. Gabber, showing that statements 5.3 and 5.4
    of the original are false without additional hypotheses. On the other hand, we note that Thm. 5.3 is a reworked
    version of Thm. 5.3A below, which appears in the 1965 edition of SGAD, and is due to M. Raynaud, cf. the Notes (∗)
    in Exp. X, 8.5 and 8.8.

[^N.D.E-VI_B-35]: Without this hypothesis, one has the following counterexample, pointed out by O. Gabber: let $G = S$
    be a local scheme with closed point $s$, such that $S* = S - {s}$ is not quasi-compact, and $X$ the disjoint union
    of ${s}$ and $S*$.

[^N.D.E-VI_B-36]: We have added this remark, cf. N.D.E. (34).

[^N.D.E-VI_B-37]: Let us point out here the following result ([Ray70a], VI 2.5): if $S$ is normal, $G$ smooth with
    connected fibers, and if $X$ is a (fppf) homogeneous $G$-space (i.e. the morphisms $X \to S$ and $G \times_{S} X \to
    X \times_{S} X$ are covering for the (fppf) topology), locally of finite type over $S$, then $X$ is locally
    quasi-projective over $S$. In particular, $G$ is quasi-projective over $S$. See also N.D.E. (35) in VI_A.

[^N.D.E-VI_B-38]: We have added this lemma, communicated by O. Gabber, which improves EGA IV₃, 14.4.1.2 and corrects the
    proof of loc. cit., 14.4.1.3 without modifying its hypotheses (compare with the erratum (Err_IV, 38) in EGA IV₄).

[^N.D.E-VI_B-39]: We have made this lemma explicit, used in the proof of Lemma 5.6.1.

[^N.D.E-VI_B-40]: We have corrected the original, which indicated 19.5.10.

[^N.D.E-VI_B-41]: Consequently, $h$ induces a section $\sigma$ of $X \times_{S} S'' \to S''$ such that $\sigma(s'')$
    lies above $x$; compare with EGA IV₃, 14.5.10.

[^N.D.E-VI_B-42]: We have added this lemma, communicated by O. Gabber. It allows us to simplify the proof of 5.6.2, and
    to prove Theorem 5.3, as well as 5.4, in a more general form, see 5.7 and 5.8 below.

[^N.D.E-VI_B-43]: We have added the hypothesis on $X_{s}$ and simplified (and corrected) the proof, taking into account
    the addition 5.6.2.0. Moreover, the proof shows that the conclusion is valid if one assumes only that $U_{s}$ is
    dense in every irreducible component of $X_{s}$.

[^N.D.E-VI_B-44]: We have simplified the formulation of condition (iv) and added condition (iv′). On the other hand, we
    have added the proof of the implication (i) ⇒ (iii), used in the proof of (iv) ⇒ (iii). Note moreover that if $T =
    \operatorname{Spec} k[\epsilon, x]/(\epsilon^{2}, \epsilon x)$ ($k$ a field), $X = T_{red} = \operatorname{Spec}
    k[x]$, then the morphisms $\phi_{\lambda} : T \to X$ defined by $x \mapsto x + \lambda \epsilon$ ($\lambda \in k$)
    coincide on the dense open $\operatorname{Spec} B_{x}$ but are not equal.

[^N.D.E-VI_B-45]: We have reproduced this example in (VI_A, 0.3), N.D.E. (5).

[^N.D.E-VI_B-46]: On the one hand, we have suppressed the corollary 5.6.5, which was a repetition of 5.5. On the other
    hand, the original stated as Remark 5.7 the corollary 5.7.1 below, referring for the proof to 4.7, a number which
    does not exist in Lect. Notes 151 (but which appeared in the 1965 edition of SGAD, whose nos. 4.5 and 4.6 became
    5.6.1 and 5.6.2); we have added Theorem 5.7, communicated by O. Gabber, which makes precise the aforementioned
    statement in SGAD.

[^N.D.E-VI_B-47]: We have added this paragraph of complements and counterexamples, all communicated by O. Gabber.

[^VI_B-6-1]: On the same theme, see also the results of XI 6, whose natural place would be in the present Exposé VI_B.
    There one finds in particular representability criteria for certain subfunctors-in-groups of a given group
    scheme.[^N.D.E-VI_B-48]

[^N.D.E-VI_B-49]: If $u : X \to G$ and $v : Y \to G$ are two arbitrary morphisms of $S$-functors, let $u(X)$ be the
    image-functor of $u$, defined by $u(X)(S') = u(S')(X(S')) \subset G(S')$; this is a subfunctor of $G$, as is the
    image-functor $v(Y)$. One may then consider the transporter of the image of $u$ into the image of $v$,
    $Transp_{G}(u(X), v(Y))$. We see thus that, in definition (ii), it is not necessary to restrict to subfunctors, i.e.
    to the case where $u$ and $v$ are monomorphisms. This restriction sometimes imposed in the original repetitions in
    the hypotheses, such as: "Let $u, v : X \to G$ be morphisms of $S$-functors, $w : H \to G$ and $w' : K \to G$
    monomorphisms, then $Transp(u, v)$, $Centr_{G}(w) = Centr_{G} H$ and $Transp_{G}(H, K)$ verify…", which can be
    avoided by considering $Transp_{G}(u(X), v(Y))$. We have made such modifications in 6.2 and, later, in 10.11.

[^N.D.E-VI_B-50]: We have added this remark, used implicitly in Proposition 6.2.

[^N.D.E-VI_B-51]: We have modified the statement, as indicated in N.D.E. (49).

[^N.D.E-VI_B-52]: The original referred to the results of Exp. VIII, § 6. For the reader's convenience, we have
    reproduced these results (with the exception of VIII, 6.3 and 6.8) in nos. 6.2.1 to 6.2.5 below. Moreover, this was
    suggested by A. Grothendieck in a Note at the beginning of VIII.6: "The present number is independent of the theory
    of diagonalizable groups; its natural place would be in VI_B."

[^N.D.E-VI_B-53]: On the one hand, we have replaced the word "free" by "projective", as indicated in VIII, Remark 6.8.
    On the other hand, the notion of essentially free $S$-scheme is intimately related to the geometric notion of flat
    and pure $S$-scheme, introduced and studied by M. Raynaud and L. Gruson ([RG71]); cf. the addition 6.9 below.

[^N.D.E-VI_B-54]: Indeed, let $(A, \mathfrak{m})$ be an Artinian local ring, $k$ its residue field, $M$ an arbitrary
    $A$-module, $(x_{i})_{i \in I}$ elements of $M$ whose images form a basis of $M/\mathfrak{m}M$ over $k$. Let $F$ be
    the free $A$-module with basis $(e_{i})_{i \in I}$, and $\phi : F \to M$ the $A$-morphism defined by $\phi(e_{i}) =
    x_{i}$. Then $Q = Coker \phi$ satisfies $Q = \mathfrak{m}Q$, hence, since $\mathfrak{m}$ is nilpotent, $Q = 0$.
    Suppose moreover $M$ flat over $A$; then $K = Ker \phi$ satisfies $K \otimes_{A} k = 0$, i.e. $K = \mathfrak{m}K$,
    hence $K = 0$.

[^N.D.E-VI_B-55]: cf. Exp. II § 1, where this functor is denoted $\prod_{Z/S} Y$; for every $S' \to S$, $F(S') =
    \Gamma(Y_{S'}/Z_{S'})$, which here equals ${id_{Z_{S'}}}$ if $Y_{S'} = Z_{S'}$, and is empty otherwise. On the other
    hand, we have added assertion (ii), used in the proof of 6.5.3.

[^N.D.E-VI_B-56]: We have added the sentence that follows.

[^N.D.E-VI_B-57]: denoted $Transpstr_{G}(Y, Z)$.

[^N.D.E-VI_B-58]: Indeed, over a field $k$, every group subscheme of $G$ is closed, cf. VI_A, 0.5.2. Moreover, 6.2.5
    concludes the insertion of the results drawn from VIII § 6.

[^N.D.E-VI_B-59]: We have inserted here this corollary (cf. Exp. XII, 6.1), which will be useful later. Moreover, in 6.3
    we return to the original text of VI_B.

[^N.D.E-VI_B-60]: We have kept the numbering of the original: there is no n° 6.4.1.

[^N.D.E-VI_B-61]: We have inserted here nos. 6.5.2 to 6.5.5, drawn from Exp. XI, 6.8 to 6.11. This was moreover
    suggested by A. Grothendieck in a Note at the beginning of XI 6: "The present number does not use the results of
    nos. 3, 4, 5 (of XI); its natural place would be in VI_B."

[^N.D.E-VI_B-62]: On the one hand, we have corrected the original, by replacing "connected" with "irreducible" (cf. the
    proof). On the other hand, by [RG71] I, 3.3.4 (iii) and 4.1.1, it suffices to assume that $X$ is flat over $S$, with
    geometrically irreducible fibers and without embedded components.

[^N.D.E-VI_B-63]: See for example the addition 1.7 in Exp. VIII.

[^N.D.E-VI_B-64]: see, for example, the proof of 6.2.6.

[^N.D.E-VI_B-65]: We have detailed the original in what follows, adding references to EGA IV.

[^N.D.E-VI_B-66]: We have detailed what follows. Moreover, this concludes the insertion of XI, 6.8 to 6.11, i.e. we
    return in 6.6 below to the original text of VI_B.

[^N.D.E-VI_B-67]: We have added this subsection.

[^N.D.E-VI_B-68]: We have replaced, here and in the sequel, the little-used terminology "separable" by the usual
    terminology "geometrically reduced", cf. EGA IV₂, 4.6.2.

[^N.D.E-VI_B-69]: The original stated (iii′) under the additional hypothesis that $G$ be locally of finite type over
    $k$, but this can be omitted, by VI_A, 0.5.2.

[^N.D.E-VI_B-70]: We have added this corollary, to point out this particular case of 7.1.

[^N.D.E-VI_B-71]: We have placed in (i′) the point (viii) of the original, and we have highlighted points (vi) and (vii)
    in the form of Corollary 7.2.1 and Definition 7.2.2 below.

[^N.D.E-VI_B-72]: We have suppressed here the hypothesis that $G$ be locally of finite type over $k$.

[^N.D.E-VI_B-73]: We have changed the notation $\operatorname{Der}(G)$ of the original, in order to avoid any risk of
    confusion with a space of derivations.

[^N.D.E-VI_B-74]: We have added these reminders, and modified accordingly, and detailed, the statement of 7.3.

[^N.D.E-VI_B-75]: We have detailed the original in what follows.

[^N.D.E-VI_B-76]: We have added this definition, which in the original was contained in the statement of Proposition
    7.6.

[^N.D.E-VI_B-77]: The original stated this result under the hypotheses of the particular case, but the more general form
    was used implicitly in the proof of 10.12; we have rewritten the statement accordingly.

[^N.D.E-VI_B-78]: We have detailed the original in what follows.

[^N.D.E-VI_B-79]: We have made the following precise and, in the proof, detailed the reduction to the case where $k$ is
    algebraically closed.

[^N.D.E-VI_B-80]: We have detailed the original in what follows, taking into account the addition 7.1.1.

[^N.D.E-VI_B-81]: These results are mentioned without proof in the original; we have highlighted them in the form of
    Lemmas 8.1.1 and 8.1.2, and detailed the proofs.

[^VI_B-8-1]: We shall make use in the course of this proof of results established in number 10, which do not depend, any
    more than number 9, on the present n° 8.

[^N.D.E-VI_B-82]: We have corrected 10.8.5 to 8.10.5.

[^N.D.E-VI_B-83]: We have detailed what follows.

[^N.D.E-VI_B-84]: Taking into account the fact that $S$ is supposed affine, hence quasi-compact and quasi-separated (cf.
    EGA 0_III, 9.1.12).

[^N.D.E-VI_B-85]: i.e., the quotient is universal, cf. Exp. IV § 3.

[^N.D.E-VI_B-86]: As pointed out by O. Gabber, this is used in the proof and must be inserted in the hypotheses.

[^N.D.E-VI_B-87]: We have corrected (fpqc) to (fppf).

[^N.D.E-VI_B-88]: see VII_A, 8.4 or VIII, 2.1.

[^VI_B-9-1]: This is too optimistic, as M. Raynaud shows in his thesis (loc. cit. X 14).

[^N.D.E-VI_B-89]: The remark (∗) refers to the counterexample X.14 in [Ray70a]. The base there is regular local of
    dimension 2.

[^N.D.E-VI_B-90]: Note that $S$, being affine over `S_0`, is therefore quasi-compact and quasi-separated, cf. N.D.E.
    (92) below.

[^N.D.E-VI_B-91]: We have added the word "flat", and corrected 17.7.6 to 17.7.8.

[^N.D.E-VI_B-92]: and from the fact that $Y$, being of finite presentation over $S$, is quasi-compact.

[^N.D.E-VI_B-93]: in terms of commutative diagrams of $S$-morphisms.

[^N.D.E-VI_B-94]: i.e., such that the composite $R_{j} \hookrightarrow X_{j} \times_{S_{j}} X_{j} \xrightarrow{pr_{1}}
    X_{j}$ is flat and of finite presentation.

[^N.D.E-VI_B-95]: Note that the proof uses also case b).

[^N.D.E-VI_B-96]: We have simplified the statement, and treated separately, in Corollary 10.11.1, the case of subgroups.

[^N.D.E-VI_B-97]: Indeed, `G_A` being flat and of finite presentation over $A$, it is covered by affine opens $G_{1},
    \cdots, G_{n}$ such that each $\mathcal{O}(G_{i})$ is a flat and finitely presented $A$-algebra; then, by EGA IV₂,
    6.9.2, there exists $f_{i} \in A$ such that $\mathcal{O}(G_{i})_{f_{i}}$ is a free module over $A_{f_{i}}$; one may
    then replace $\operatorname{Spec}(A)$ by the affine open $D(f)$, where $f = f_{1} \cdots f_{n}$, and one does the
    same for `Y_A` and `Z_A`.

[^N.D.E-VI_B-98]: We have corrected $n+1$ to `2n` below.

[^N.D.E-VI_B-99]: We have detailed the original in what follows.

[^N.D.E-VI_B-100]: We have added this corollary, used in the proof of 8.4.

[^N.D.E-VI_B-101]: The original assumed `G, H` of finite presentation and $H$ with smooth fibers; we have modified the
    hypothesis in order to be able to apply 10.12. We have also detailed the proof.

[^N.D.E-VI_B-102]: (Added by editors; see source.)

[^N.D.E-VI_B-103]: (End of section 10.)

[^N.D.E-VI_B-C-104]: We have added this reminders paragraph.

[^N.D.E-VI_B-C-105]: Note that if $k$ is a field and if $X$ is an infinite sum of copies of $S = \operatorname{Spec} k$
    (so that $X$ is not quasi-compact), then $\mathcal{A}(X) = k^{X}$ and the canonical morphism $k^{X} \otimes k^{X}
    \to k^{X\times X}$ is not surjective.

[^N.D.E-VI_B-C-106]: Note that if $S$ is a regular locally noetherian scheme of dimension $\leq 2$, and $X$ is a flat,
    quasi-compact and quasi-separated $S$-scheme, then $\mathcal{A}(X)$ is a flat `O_S`-module, cf. [Ray70a], VII 3.2.

[^N.D.E-VI_B-C-107]: We have added this proposition; see also the additional paragraph 12 below for a study of the
    morphism $G \to G_{af}$ and its kernel.

[^N.D.E-VI_B-C-108]: In 11.4–11.6, we have considered $\operatorname{Hom}_{O_{S}}(W(E), W(F))$ instead of
    $\operatorname{Hom}_{O_{S}}(V(F), V(E))$ (cf. I, 4.6.3) and simplified the original by taking into account the
    addition 11.0 (b).

[^N.D.E-VI_B-C-109]: We have simplified the original, which used the isomorphism $\operatorname{Hom}_{O_{S}}(W(E), W(E
    ')) \simeq \operatorname{Hom}_{O_{S}}(V(E '), V(E))$ then the inclusion of the right-hand side into
    `Hom_S(V(E), V(E ′)) = Hom_{O_S}(E ′, f_* f*(Sym(E)))` and applied EGA III, 4.1.15 to $V(E) =
    \operatorname{Spec}(Sym(E))$ to deduce 11.0 (b).

[^N.D.E-VI_B-C-110]: We have expanded 11.6, and highlighted the results obtained in the form of Proposition 11.6.1.

[^N.D.E-VI_B-C-111]: We have added this remark, which generalizes 11.7 and will be useful in 11.10.bis.

[^N.D.E-VI_B-C-112]: Since the statements 11.8 and 11.9 bear solely on the notion of comodule over a coalgebra, we have
    introduced Definition 11.8.0 and reformulated 11.8 and 11.9 accordingly.

[^N.D.E-VI_B-C-113]: In the original, it is assumed that $C$ is a free $A$-module; the generalization to the case where
    $C$ is a projective $A$-module, pointed out by J.-P. Serre, was mentioned in Remark 11.10.1. We have included this
    generalization here and in 11.9, and expanded the proofs accordingly.

[^N.D.E-VI_B-C-114]: We have added this proposition, taken from [Se68], § 1.5, Prop. 2.

[^N.D.E-VI_B-C-115]: We have added this lemma, which is used in the proof of 11.9.

[^N.D.E-VI_B-C-116]: Let us point out in passing that assertion II 2.5.2 of loc. cit., more general than II 2.5.1, is
    corrected in the article [Gr73] (this does not affect the case of faithfully flat morphisms).

[^N.D.E-VI_B-C-117]: As pointed out in N.D.E. (112), we have rewritten the statement for an `O_S`-coalgebra $C$ (rather
    than for an $S$-group $G$ satisfying the hypotheses indicated in Corollary 11.10). Moreover, we have spelled out the
    proof (the original indicated: "(⋯) the proposition is a consequence of Lemma 11.8.").

[^VI_B-C-11-9]: This is the case, for example, when $C = \mathcal{A}(G)$, where $G$ is a reductive $S$-group, as we
    shall see in Exp. XXII 5.7.8.

[^N.D.E-VI_B-C-118]: We have added this definition, taken from [RG71], bottom of p. 82. Thus, in Proposition 11.9, the
    hypothesis is that the coalgebra $C$ is a locally projective `O_S`-module, and we have used this terminology in
    Corollary 11.10.

[^N.D.E-VI_B-C-119]: We have added this proposition, which is a particular case of [Th87], 1.4–1.5. The author makes
    reference there to an argument of Deligne (cf. [Kn71], III Th. 1.1); one may also note the similarity with the
    argument of Serre ([Se68], Prop. 2) recalled in 11.8.bis.

[^N.D.E-VI_B-C-120]: The first part of the original Remark 11.10.1 has been incorporated into 11.8 and 11.9 (by
    replacing "free" by "projective"); the counterexamples below correct the second part.

[^N.D.E-VI_B-C-121]: We have expanded the original in what follows; on the other hand, we have chosen to have $G$ act on
    the right on $X$ in order to obtain a left linear action of $G$ on $O(X)$.

[^N.D.E-VI_B-C-122]: Recall that a $k$-scheme $X$ is said to be quasi-affine if it is isomorphic to a quasi-compact open
    of an affine $k$-scheme (EGA II, 5.1.1).

[^N.D.E-VI_B-C-123]: The equivalence of these conditions is proved in the additional section 12.

[^N.D.E-VI_B-C-124]: This is proved, with various generalizations, in the additional section 13.

[^N.D.E-VI_B-C-125]: On the one hand, this is generalized in Section 13 to the case where $G$ is affine and flat over a
    regular base of dimension $\leq 2$. On the other hand, in what follows we have spelled out and corrected the
    original.

[^N.D.E-VI_B-C-126]: We have denoted by $u^{\natural}$ (instead of $u^{\circ}$) the morphism $B \to A$ corresponding to
    $u : \operatorname{Spec}(A) \to \operatorname{Spec}(B)$.

[^N.D.E-VI_B-C-127]: We have added the hypothesis that $G$ be quasi-compact and spelled out the equivalence of
    conditions (i) and (ii).

[^N.D.E-VI_B-C-128]: We have added this lemma, taken from [DG70], § II.2, 3.5.

[^N.D.E-VI_B-C-129]: On the one hand, we recall that every group subscheme of $G$ is closed (1.4.2). On the other hand,
    we have stated the result in the usual form: "$H$ is the stabilizer of a line in a representation of $G$", while
    keeping the original formulation in terms of a sequence $a_{1}, \cdots, a_{n}$ of semi-invariants in
    $\mathcal{A}(G)$.

[^N.D.E-VI_B-C-130]: We have added this lemma, taken from the proof of thm. 5.6 of [DG70], § III.3 (by abuse of
    notation, we designate by the same letter $E$ a $k$-vector space and the $k$-scheme in modules $W(E) =
    \operatorname{Spec} S(E^{*})$).

[^N.D.E-VI_B-C-131]: For another proof of this theorem, not using the results of VI_A, see [Ta72], Th. 5.2 (see also
    Remark 11.18.5).

[^N.D.E-VI_B-C-132]: In what follows, we have spelled out the original (and corrected the erroneous assertion
    `(G/N)_red = G_red / N_red`), relying on [DG70], § III.3, 5.6.

[^N.D.E-VI_B-C-133]: We have added this lemma, taken from [DG70], § III.3, 7.1.

[^N.D.E-VI_B-C-134]: We have added this subsection.

[^N.D.E-VI_B-C-135]: We have added this section.

[^N.D.E-VI_B-C-136]: This lemma was communicated to us by M. Raynaud; it will be used in the proof of Proposition 12.9.

[^N.D.E-VI_B-C-137]: This is a version improved by O. Gabber of a statement communicated by M. Raynaud.

[^N.D.E-VI_B-C-138]: This is true, more generally, if $S$ is regular locally noetherian of dimension $\leq 2$, cf.
    [Ray70a], VII 3.2.

[^N.D.E-VI_B-D-139]: This section has been added.

[^N.D.E-VI_B-D-140]: Additional references cited in this Exposé.

[^N.D.E-VI_B-1]: And also § 5, cf. N.D.E. (34) and (46).

[^N.D.E-VI_B-48]: We have inserted these results in what follows (nos. 6.5.2 to 6.5.5).
