# Exposé XV. Complements on sub-tori of a group scheme. Application to smooth groups

<!-- label: III.XV -->

*by M. Raynaud* [^XV-0-1]

## 0. Introduction

<!-- label: III.XV.0 -->

<!-- original page 349 -->

This Exposé complements and partially recasts Exposés XI and XII; the contents of Exposés XIII and XIV are not
indispensable. Continuing the effort undertaken in XII, we shall work with $S$-preschemes in groups that are not
necessarily affine and not necessarily separated over $S$.

Sections 1, 2, 3, 4 are devoted to the study of sub-tori of a group prescheme. We obtain theorems of infinitesimal
lifting (§ 2) and global lifting (§ 4), in which an essential role is played by points of finite order (§ 1).

Sections 5, 6 and 7 are independent of the preceding ones. The consideration of infinitesimal neighborhoods leads to the
representability of the functor of smooth subgroups equal to their connected normalizer (§ 5). In §§ 6 and 7, we turn
more specifically to Cartan subgroups.

Finally, in § 8 we give a necessary and sufficient condition for the functor of sub-tori of a smooth group, or that of
maximal tori, to be representable.

## 1. Lifting of finite subgroups

<!-- label: III.XV.1 -->

<!-- original page 350 -->

### 1.1. Finite, smooth and central subgroups of multiplicative type

<!-- label: III.XV.1.1 -->

**Proposition 1.1.** *Let $S$ be an affine scheme, $S_{0}$ a closed subscheme of $S$ defined by an ideal of square zero,
$G$ an $S$-prescheme in groups, $H_{0}$ a subgroup scheme of $G_{0} = G \times_{S} S_{0}$ which is smooth over $S_{0}$,
of finite type, and of multiplicative type. Then, in order that there exist a subgroup scheme of $G$, of multiplicative
type, which lifts $H_{0}$, it is necessary and sufficient that there exist a subscheme $H'$ of $G$, flat over $S$, which
lifts $H_{0}$.*

<!-- label: III.XV.1.1.statement -->

The necessity of the condition is clear; let us prove sufficiency. The group $H_{0}$ of multiplicative type is
quasi-isotrivial (X 4.5); by Exp. X 2.1, there exist an $S$-group $H$ of multiplicative type and an $S_{0}$-isomorphism
of groups:

```text
u₀ : H ×_S S₀ ⥲ H₀.
```

Since $H'$ is flat over $S$ and $H' \times_{S} S_{0}$ is of finite presentation over $S_{0}$ (Exp. IX 2.1 b)), $H'$ is
of finite presentation over $S$; moreover, its fibers are smooth, so $H'$ is smooth over $S$
([EGA IV 17.5.1](https://jcreinhold.github.io/ega/iv/30-ch4-17-smooth-unramified-etale-morphisms.html#175-characterizations-of-smooth-morphisms)).
Since $S$ is affine, $u_{0}$ therefore lifts to an $S$-morphism of preschemes:

$$ u : H \longrightarrow H'. $$

It then follows from Exp. III 2.1 and Exp. IX 3.1 that the composed morphism $v_{0} : H \times_{S_{0}} S
\xrightarrow{\sim} H_{0} \to G_{0}$

<!-- original page 351 -->

also lifts to an $S$-morphism of groups:

$$ v : H \longrightarrow G. $$

Since $v_{0}$ is an immersion, so is $v$. The image of $H$ by $v$ is therefore a subgroup scheme of $G$, of
multiplicative type, which lifts $H_{0}$.

**Proposition 1.2.** *Let $S$ be a prescheme, $S_{0}$ a subprescheme of $S$ defined by a locally nilpotent sheaf of
ideals, $G$ an $S$-prescheme in groups, flat and of finite presentation over $S$, and $H_{0}$ a subgroup scheme of
$G_{0} = G \times_{S} S_{0}$ which is smooth, finite over $S_{0}$, of multiplicative type and central. Then there exists
a unique subgroup scheme $H$ of $G$, of multiplicative type, which lifts $H_{0}$. Moreover $H$ is central. (See XVII
App. III, 1).*

<!-- label: III.XV.1.2 -->

**Proposition 1.2 bis.** *Let $S$, $G$, $S_{0}$, $G_{0}$ be as above, $H$ an $S$-group scheme of multiplicative type,
smooth and finite over $S$, and $u_{0} : H_{0} = H \times_{S} S_{0} \to G_{0}$ a central homomorphism. Then $u_{0}$
lifts uniquely to a homomorphism $u : H \to G$. Moreover $u$ is central.*

<!-- label: III.XV.1.2bis -->

The existence of the lifting $u$ in 1.2 bis is easily deduced from 1.2 by considering the graph of $u_{0}$. The lifting
$u$ is unique and central by Exp. IX 3.4 and Exp. IX 5.1.

*Proof of 1.2.* The uniqueness of $H$ and the fact that $H$ is central follow from Exp. IX 5.6 b) and Exp. IX 3.4 bis.
Given uniqueness, in order to prove the existence

<!-- original page 352 -->

of $H$ we may assume $S$ affine and $S_{0}$ defined by an ideal of square zero, and it suffices (1.1) to find a
subscheme of $G$, flat over $S$, which lifts $H_{0}$.

Since $H_{0}$ is smooth and finite over $S_{0}$, we may assume — possibly after restricting $S$ — that there exists an
integer $n > 0$, invertible on $S$, such that $H_{0} = {}_{n}H_{0}$. Consider the $n$-th power morphism in $G$:

```text
u : G ⟶ G,    x ↦ xⁿ.
```

We still denote by ${}_{n}G$ the "kernel of $u$", that is, the inverse image under $u$ of the unit section of $G$ (N.B.
$u$ is not in general a group morphism). Granting for a moment the following lemma:

**Lemma 1.3.** *Let $k$ be a field, $G$ a group scheme locally of finite type over $k$, $n$ an integer prime to the
characteristic of $k$, $u$ the $n$-th power morphism in $G$. Then $u$ is étale at every point $x$ of $G$ belonging to
the center of $G$.*

<!-- label: III.XV.1.3 -->

Since $G$ is flat and of finite presentation over $S$, it follows from the preceding lemma and from
[EGA IV 17.8.2](https://jcreinhold.github.io/ega/iv/30-ch4-17-smooth-unramified-etale-morphisms.html#178-criteria-for-smoothness-and-unramifiedness-by-fibres)
that if $x$ is a point of $G$ projecting to $s$ in $S$ and belonging to the center of $G_{s}$, the morphism $u$ is étale
at $x$. If moreover $x$ is a point of ${}_{n}G$, then ${}_{n}G$ is étale over $S$ at $x$. By hypothesis, the group
$H_{0}$ is central and contained in ${}_{n}G_{0}$, so it is in fact contained in the largest open subset $V$ of
${}_{n}G$ which is étale over $S$. Since $H_{0}$ and $V \times_{S} S_{0} = V_{0}$ are étale over $S_{0}$, $H_{0}$ is an
open subset of $V_{0}$
([EGA IV 17.8.7](https://jcreinhold.github.io/ega/iv/30-ch4-17-smooth-unramified-etale-morphisms.html#178-criteria-for-smoothness-and-unramifiedness-by-fibres)
and 17.9.1).

<!-- original page 353 -->

But then the open subprescheme of $V$ having the same underlying space as $H_{0}$ is a subscheme of $G$, flat over $S$,
which lifts $H_{0}$.

It remains to prove Lemma 1.3. For this, note that the largest open subset of $G$ on which $u$ is étale is invariant
under base field extension (EGA IV 17.8.2); this allows us to reduce to the case where $x$ is rational over $k$. Let
$t_{x}$ denote translation by $x$, which is a $k$-automorphism of the scheme $G$. Since $x$ is in the center of $G$, we
have the commutative diagram:

```text
G ──u──→ G
│        │
tₓ       tₓⁿ
│        │
▼        ▼
G ──u──→ G.
```

It therefore suffices to show that $u$ is étale at the origin, but this was seen in VII_A 8.4.

### 1.2. Global lifting of finite groups

<!-- label: III.XV.1.2-global -->

**Lemma 1.4.** *Let $A$ be a local ring, separated and complete for the topology defined by its maximal ideal
$\mathfrak{m}$, let $S = \operatorname{Spec}(A)$, $S_{n} = \operatorname{Spec}(A/\mathfrak{m}^{n})$. Then for every
prescheme $X$ (resp. every $S$-prescheme $X$), the canonical map*

```text
(*)    Hom(S, X) ⟶ lim_{←n} Hom(Sₙ, X)
```

*(resp.*

```text
(**)   Γ(X/S) ⟶ lim_{←n} Γ(Xₙ/Sₙ),    where Xₙ = X ×_S Sₙ)
```

*is bijective.*

<!-- label: III.XV.1.4 -->

Statement (\*\*) is an easy consequence of (*). Let us prove (*).

<!-- original page 354 -->

Let $u_{n} : S_{n} \to X$ ($n \in \mathbb{N}$) be a coherent system of morphisms. The image $y$ of the closed point of
$S_{n}$ is therefore independent of $n$, and $u_{n}$ factors through $\operatorname{Spec}(\mathcal{O}_{y})$. The
morphisms $u_{n}$ define, by passage to the projective limit, a ring morphism

```text
ũ : 𝒪_y ⟶ lim_{←n} (A/𝔪ⁿ) = A.
```

This shows that (\*) is surjective; it is injective as soon as $A$ is separated for the $\mathfrak{m}$-adic topology.

**Corollary 1.5.** *Let $A$ be a complete noetherian local ring, $\mathfrak{m}$ its maximal ideal, $S =
\operatorname{Spec}(A)$, $S_{n} = \operatorname{Spec}(A/\mathfrak{m}^{n})$, $X$ a finite scheme over $S$ and $Y$ an
$S$-prescheme. Then the canonical map*

```text
Hom_S(X, Y) ⟶ lim_{←n} Hom_{Sₙ}(Xₙ, Yₙ)
```

*(where $X_{n} = X \times_{S} S_{n}$ and similarly $Y_{n} = \cdots$) is bijective.*

<!-- label: III.XV.1.5 -->

Indeed, it follows from [EGA II 6.2.5](https://jcreinhold.github.io/ega/ii/02-06-integral-finite-morphisms.html#62-quasi-finite-morphisms) that $X$ is a finite sum of local $S$-schemes finite over $S$. This reduces us to
the case where $X$ itself is the spectrum of a complete noetherian local ring. But $\operatorname{Hom}_{S}(X, Y) =
\Gamma(Z/X)$ where $Z$ is the $X$-prescheme $Y \times_{S} X$, and we apply the preceding proposition.

**Proposition 1.6.** *Let $A$, $S$, $S_{n}$ be as above, and let $G$ and $M$ be two $S$-preschemes in groups, with $M$
finite over $S$. Then:*

*a) The canonical map*

```text
Hom_{S-gr}(M, G) ⟶ lim_{←n} Hom_{Sₙ-gr}(Mₙ, Gₙ)
```

*is bijective.* <!-- original page 355 -->

*b) If $M$ is of multiplicative type and $G$ is smooth over $S$, the canonical map*

```text
φ : Hom_{S-gr}(M, G) ⟶ Hom_{S₀-gr}(M₀, G₀)
```

*is surjective. Moreover, if $\phi(u) = \phi(u') = u_{0}$, then $u$ and $u'$ are conjugate by an element of $G(S)$
reducing to the unit element of $G(S_{0})$.*

*c) If $M$ is of multiplicative type and smooth over $S$, if $G$ is flat of finite type over $S$, and if $u_{0} : M_{0}
\to G_{0}$ is a central homomorphism, then $u_{0}$ lifts uniquely to a homomorphism*

$$ u : M \longrightarrow G. $$

*Moreover $u$ is central if $G$ has connected fibers.*

<!-- label: III.XV.1.6 -->

*Proof.* a) Follows from 1.5, from the fact that $M \times_{S} M$ is finite over $S$, and from the characterization of
group morphisms as those rendering commutative the well-known diagram:

```text
M ×_S M ──u×u──→ G ×_S G
   │                │
   │                │
   ▼                ▼
   M  ────u───────→ G.
```

b) By Exp. IX 3.6, one can construct a coherent system of homomorphisms $u_{n} : M_{n} \to G_{n}$ lifting a homomorphism
$u_{0} : M_{0} \to G_{0}$. Hence the first assertion of b), in view of a).

If now $u$ and $u'$ are two liftings of $u_{0}$, then $u_{n}$ and $u'_{n}$ are conjugate

<!-- original page 356 -->

by an element $g_{n}$ of $G(S_{n})$ lifting the unit element of $G(S_{0})$ (Exp. IX 3.6); *loc. cit.* also implies that
one may choose the $g_{n}$ in a coherent way, and hence (1.4) coming from a section $g$ of $G(S)$. The morphisms $u$ and
$int(g)\cdot u'$ then coincide modulo $\mathfrak{m}^{n}$ for every $n$, so they coincide (1.5).

c) The existence and uniqueness of $u$ follow from a) and 1.2 bis. If $G$ has connected fibers, $u$ is central by Exp.
IX 5.6 a).

## 2. Infinitesimal lifting of sub-tori

<!-- label: III.XV.2 -->

<!-- original page 357 -->

### 2.1. Statement of the theorem

<!-- label: III.XV.2.statement -->

We shall give a theorem of infinitesimal lifting of sub-tori of a group prescheme which does not appeal to smoothness
hypotheses (in contrast to Exp. IX 3.6 bis) and which moreover answers a very natural question[^N.D.E-XV-1]: does it
suffice to be able to lift "enough" points of finite order of a sub-torus $T_{0}$ in order to be assured of being able
to lift $T_{0}$ (infinitesimally, of course)?

**Theorem 2.1.** *Let $S$ be a noetherian affine scheme, $S_{0}$ a closed subscheme of $S$ defined by an ideal $J$ of
square zero, $G$ an $S$-prescheme in groups of finite type, $G_{0} = G \times_{S} S_{0}$, $T_{0}$ a sub-torus of
$G_{0}$, $q$ an integer `> 0` invertible on $S$. Suppose that for every integer $n$ equal to a power of $q$, there
exists a subscheme $M_{n}$ of $G$, flat over $S$, such that $M_{n} \times_{S} S_{0} = {}_{n}T_{0}$. Then there exists a
sub-torus $T$ of $G$ such that $T \times_{S} S_{0} = T_{0}$.*

<!-- label: III.XV.2.1 -->

Theorem 2.1 will be useful to us through the following two corollaries:

**Corollary 2.2.** *Let $S$ be a locally noetherian prescheme, $S_{0}$ a closed subprescheme of $S$ defined by a locally
nilpotent sheaf of ideals, $G$ an $S$-prescheme in groups of finite type, $T_{0}$ a sub-torus of $G_{0} = G \times_{S}
S_{0}$, $q$ an integer `> 0` invertible on $S$; finally, with the integer $n$ ranging over powers of $q$, let $(M_{n})$
be a coherent system*

<!-- original page 358 -->

*of $S$-subgroup schemes of $G$, of multiplicative type, which lifts the ${}_{n}T_{0}$ (N.B. The system of subgroups of
multiplicative type $(M_{n})$ is said to be coherent if $M_{m} = {}_{m}(M_{n})$ whenever the integer $m$ divides $n$.)
Then there exists one and only one sub-torus $T$ of $G$ such that $T \times_{S} S_{0} = T_{0}$ and ${}_{n}T = M_{n}$ for
every $n$.*

<!-- label: III.XV.2.2 -->

**Corollary 2.3.** *Let $G$ be an $S$-prescheme in groups, flat and of finite presentation over $S$, $S_{0}$ a closed
subprescheme of $S$ defined by a sheaf of ideals of finite type and locally nilpotent, $T_{0}$ a central torus of $G_{0}
= G \times_{S} S_{0}$. Then there exists one and only one sub-torus $T$ of $G$ lifting $T_{0}$. Moreover $T$ is
central.*

<!-- label: III.XV.2.3 -->

**Remark 2.4.** We leave to the reader the task of formulating the analogue of statements 2.1, 2.2, 2.3 in which,
instead of lifting a sub-torus of $G_{0}$, one is given a torus $T$ over $S$ and one proposes to lift a morphism

$$ u_{0} : T_{0} \longrightarrow G_{0} $$

(one reduces to the preceding cases by considering the graph of $u_{0}$).

<!-- label: III.XV.2.4 -->

Let us show how Corollaries 2.2 and 2.3 are deduced from 2.1.

*Proof of Corollary 2.2.* The uniqueness of $T$ follows from Exp. IX 4.8 b) and Exp. IX 4.10. To prove the existence of
$T$, we may therefore reduce to the case where $S$ is affine, hence noetherian, and where $S_{0}$ is defined by an ideal
of square zero.

<!-- original page 359 -->

**Lemma 2.5.** *Let $G$ be an $S$-prescheme in groups, of finite presentation, and $H$ a subgroup scheme of $G$, of
multiplicative type, smooth over $S$. Then $Centr_{G}(H)$ is representable by a subgroup prescheme of $G$, of finite
presentation.*

<!-- label: III.XV.2.5 -->

The lemma follows from Exp. VIII 6.5 e), without smoothness hypothesis on $H$, when $G$ is separated over $S$. In the
present case, one notes that the assertion to be proved is local for the fpqc topology, which allows us to assume $H$
diagonalizable, hence of the form $D_{S}(M)$. We may also assume $S$ affine, then $S$ noetherian thanks to
[EGA IV 8](https://jcreinhold.github.io/ega/iv/21-ch4-08-projective-limits.html#8-projective-limits-of-preschemes).
Since $H$ is smooth over $S$ and of finite type, the order $q$ of the torsion subgroup of $M$ is invertible on $S$ (Exp.
VIII 2.1 e)). It is then immediate (cf. Exp. IX 4.10) that the subgroups ${}_{n}H$, where $n$ ranges over powers of $q$,
are schematically dense in $H$ (Exp. IX 4.1). But ${}_{n}H$ is a completely decomposed covering of $S$ (i.e. is
isomorphic to a finite direct sum of copies of $S$), so $Centr_{G}({}_{n}H) = Z_{n}$ is representable as the
intersection of the centralizers in $G$ of the sections of ${}_{n}H$ over $S$. It then suffices to apply the lemma:

**Lemma 2.5 bis.** *Let $S$ be a noetherian prescheme, $G$ an $S$-prescheme in groups of finite type, $H$ a subgroup of
$G$ of multiplicative type, $(H_{i})$ an increasing filtered family of subgroups of $G$ of multiplicative type, and
suppose that $Z_{i} = Centr_{G}(H_{i})$ is representable by a subgroup prescheme of $G$. Then the family of `Zᵢ` is
stationary.*

<!-- original page 360 -->

*If moreover the `Hᵢ` are schematically dense in $H$, one has $Z_{i} = Centr_{G}(H)$ for $i$ large enough.*

<!-- label: III.XV.2.5bis -->

To see that the family of `Zᵢ` is stationary, it suffices to show that the family of underlying sets $ens(Z_{i})$ is
stationary. Indeed, the stationary value will then be a closed subset of an open subset $U$ of $G$; and, possibly
replacing $G$ by $U$, we are reduced to studying a decreasing filtered family of closed subpreschemes of a noetherian
prescheme. An easy constructibility argument reduces us to the case where $S$ is integral. We must then show that the
family of $ens(Z_{i})$ is stationary above some non-empty open subset of $S$. Now the generic fiber of $G$ is separated
(Exp. VI_A 0.3), so, possibly restricting $S$, we may assume $G$ separated over $S$ (EGA IV 8). But then `Zᵢ` is closed
in $G$ (Exp. VIII 6.5 e)).

To establish the last assertion of the lemma, denote by $Z$ the stationary value of the family `Zᵢ`. It is clear that
$Centr_{G}(H)$ is a subfunctor of $Z$; let us show that $Z$ centralizes $H$. Let $E$ be the subprescheme of $H
\times_{S} Z$ which is the kernel of the pair of morphisms:

```text
H ×_S Z ⇒ G
(h, c) ↦ c
(h, c) ↦ hch⁻¹.
```

The prescheme $E$ majorizes $H_{i} \times_{S} Z$ for every $i$. On the other hand, the `Hᵢ` are flat over $S$, so ([EGA
IV 11.10.9](https://jcreinhold.github.io/ega/iv/23a-ch4-11-flatness-loci-and-descent.html#1110-schematically-dominant-families-of-morphisms-and-schematically-dense-families-of-subpreschemes)) for every point $s$ of $S$, the $(H_{i})_{s}$ are schematically dense in $H_{s}$ and the $H_{i} \times_{S}
Z$ are schematically dense in $H \times_{S} Z$. Since $G_{s}$ is separated, $E_{s}$ is closed in $(H \times_{s} Z)_{s}$
and therefore equal to it. But then $E$ is closed in

<!-- original page 361 -->

$H \times_{S} Z$, so equals $H \times_{S} Z$. This says that $Z$ centralizes $H$.

Let us return to the proof of 2.2. By 2.5, $Z_{n} = Centr_{G}(M_{n})$ is representable, and by 2.5 bis the decreasing
family of subpreschemes $Z_{n}$ is stationary; let $Z$ be its stationary value. The group $Z$ majorizes $T_{0}$ and the
$M_{n}$. Possibly replacing $G$ by $Z$, we may therefore assume the $M_{n}$ central.

We are then in the conditions of application of Theorem 2.1, and there exists a sub-torus $T$ of $G$ lifting $T_{0}$.
The groups ${}_{n}T$ and $M_{n}$ are then two liftings of ${}_{n}T_{0}$, hence are conjugate (Exp. IX 3.2 bis) and
consequently coincide, $M_{n}$ being central. The torus $T$ answers the question.

*Proof of Corollary 2.3.* The uniqueness of $T$ follows from Exp. IX 5.1 bis, and the fact that $T$ is central follows
from IX 5.6 b). This remark allows us, by the usual procedure, to reduce to the case where $S$ is affine (so $S_{0}$ is
defined by a nilpotent ideal of finite type), then to the case where $S$ is noetherian. Possibly restricting $S$, we may
assume that there exists an integer $q$ invertible on $S$. Corollary 2.3 is then a consequence of 2.2 and of 1.2.

**Remark 2.6.** One easily shows that Corollary 2.3 remains true if one replaces the torus $T_{0}$ by a smooth central
subgroup of multiplicative type of $G_{0}$.

<!-- label: III.XV.2.6 -->

### 2.2. Proof of 2.1

<!-- label: III.XV.2.proof -->

<!-- original page 362 -->

**a) Reduction to the case $T_{0} = G_{m, S_{0}}$.**

Thanks to 1.1, we may assume that $M_{n}$ is a subgroup of multiplicative type. Using Exp. IX 3.2 bis, we may assume
that the family of the $M_{n}$ is coherent (2.2). The centralizer $Z_{n}$ of $M_{n}$ in $G$ is representable (2.5), and
the filtered family of $Z_{n}$ is stationary (2.5 bis). Possibly replacing $G$ by $Z_{n}$ for $n$ large enough, we may
therefore assume $T_{0}$ and the $M_{n}$ central. The uniqueness of the lifting of $T_{0}$ is then assured (Exp. IX 5.1
bis).

Proceeding as in the proof of 1.1, we may assume that there exist an $S$-torus $T$ and an $S_{0}$-isomorphism

```text
u₀ : T ×_S S₀ ⥲ T₀,
```

and it is equivalent to lift $u_{0}$ or to lift $T_{0}$. In view of uniqueness, it suffices to prove the existence of a
lifting of $u_{0}$ after performing a faithfully flat affine extension $S' \to S$ of finite type (fpqc descent), which
allows us to assume $T = G^{r}_{m, S}$ (Exp. X 4.5). If the restriction of $u_{0}$ to each factor $G_{m}$ lifts to an
$S$-morphism — necessarily central — one immediately deduces a lifting of $u_{0}$. In short, we may assume $T_{0} =
G_{m, S_{0}}$.

**b) Definition of the obstruction to the existence of a lifting of $T_{0}$.**

To prove 2.1, it suffices by 1.1 to find a subscheme of $G$, flat over $S$, which lifts $T_{0}$. We shall see that one
can define the obstruction to the existence of such a lifting as an element of a certain $Ext^{1}(\cdot, \cdot)$ of
sheaves of modules.

<!-- original page 363 -->

Let $U$ be an open subset of $G$ such that $T_{0}$ is closed in $U$, and let us still denote by $U$ (resp. $U_{0}$) the
open subscheme of $G$ (resp. $G_{0}$) having $U$ as underlying space. The sheaf $\mathcal{O}_{T_{0}}$, viewed as a sheaf
on $U$, is therefore a quotient of $\mathcal{O}_{U_{0}}$. Let $h$ be the canonical epimorphism:

$$ h : \mathcal{O}_{U_{0}} \longrightarrow \mathcal{O}_{T_{0}}. $$

**Lemma 2.7.** *The canonical map*

```text
h̃ = id_J ⊗ h : J ⊗_{S₀} 𝒪_{U₀} ⟶ J ⊗_{S₀} 𝒪_{T₀}
```

*factors (evidently uniquely) as $i \circ j_{U}$, where $j_{U}$ is the canonical epimorphism*

```text
J ⊗_{S₀} 𝒪_{U₀} ⟶ J𝒪_U ≃ J𝒪_{U₀}.
```

<!-- label: III.XV.2.7 -->

We must show that $\tilde{h}(K) = 0$, where $K$ is the kernel of $j_{U}$. Now for every integer $n$ equal to a power of
$q$, we have an epimorphism

$$ h_{n} : \mathcal{O}_{T_{0}} \longrightarrow \mathcal{O}_{{}_{n}T_{0}} $$

and since ${}_{n}T_{0}$ lifts to a scheme $M_{n}$ flat over $S$, the canonical morphism

```text
jₙ : J ⊗_{S₀} 𝒪_{ₙT₀} ⟶ J𝒪_{Mₙ}
```

is an isomorphism.

<!-- original page 364 -->

The commutative diagram below:

```text
K ──→ J ⊗_{S₀} 𝒪_{U₀} ──j_U──→ J𝒪_U ⊂ 𝒪_U
            │             ⤡
            │ h̃           i
            ▼            ↗
       J ⊗_{S₀} 𝒪_{T₀}
            │
            │ h̃ₙ
            ▼            ≅
      J ⊗_{S₀} 𝒪_{ₙT₀} ──jₙ──→ J𝒪_{Mₙ} ⊂ 𝒪_{Mₙ}
```

shows that $\tilde{h}(K)$ is contained in $Ker \tilde{h}_{n}$ for every $n$, hence is contained in $\bigcap_{n} Ker
\tilde{h}_{n}$, and it suffices to show that this last intersection is zero. Now the sheaf $\mathcal{O}_{T_{0}}$ is
equal to the sheaf $\mathcal{O}_{S_{0}}[\mathbb{Z}]$, the algebra of the group $\mathbb{Z}$ with coefficients in
$\mathcal{O}_{S_{0}}$, while $\mathcal{O}_{{}_{n}T_{0}}$ is the quotient algebra
$\mathcal{O}_{S_{0}}[\mathbb{Z}/n\mathbb{Z}]$.

Let $a = \Sigma_{m \in \mathbb{Z}} a_{m} \otimes m$ be an element of $J \otimes_{S_{0}} \mathcal{O}_{T_{0}}$. The
$a_{m}$ are then sections of $J$, almost all zero. Take $n$ large enough that the indices $m$ for which $a_{m}$ is
non-zero have distinct images in $\mathbb{Z}/n\mathbb{Z}$. Then if $a \in Ker \tilde{h}_{n}$, one necessarily has $a =
0$. This proves that $\bigcap_{n} Ker \tilde{h}_{n} = 0$, and proves 2.7.

Let then $K_{0}$ be the kernel of $h$; consider the following diagram:

```text
                          0
                          │
                          ▼
       J𝒪_U              K₀
        ≅│                │
         ▼                ▼
   0 → J𝒪_{U₀} ────→ 𝒪_U ────→ 𝒪_{U₀} → 0
         │ i               h    │
         ▼                      ▼
  J ⊗_{S₀} 𝒪_{T₀}            𝒪_{T₀}
                                │
                                ▼
                                0.
```

The sheaf $\mathcal{O}_{U}$ defines an element $\Phi$ of the group $Ext^{1}_{\mathcal{O}_{U}}(\mathcal{O}_{U_{0}},
J\mathcal{O}_{U_{0}})$. Let $\Psi$ be the element of

<!-- original page 365 -->

$Ext^{1}_{\mathcal{O}_{U}}(K_{0}, J \otimes_{S_{0}} \mathcal{O}_{T_{0}})$ deduced from $\Phi$ by bifunctoriality of
$Ext^{1}(\cdot, \cdot)$ through the morphisms $K_{0} \to \mathcal{O}_{U_{0}}$ and $i : J\mathcal{O}_{U_{0}} \to J
\otimes_{S_{0}} \mathcal{O}_{T_{0}}$. It follows from Exp. III 4.1 and from the infinitesimal flatness criterion (cf.
Exp. III 4.3) that there exists a subscheme of $U$, flat over $S$, which lifts $T_{0}$, if and only if $\Psi$ is zero.

But note that $T_{0}$ is affine, so it suffices (Exp. III 4.5 and 4.6) to show that there locally on $U$ exists a
subscheme flat over $S$ lifting $T_{0}$. In short, it suffices to show that the image of $\Psi$ in the sheaf

```text
ℰ = Ext¹_{𝒪_U}(K₀, J ⊗_{S₀} 𝒪_{T₀})
```

is zero. We shall still denote by $\Psi$ this element of $\Gamma(U, \mathcal{E})$.

**c) Reduction to the case $S$ local artinian with algebraically closed residue field.**

Since $K_{0}$ and $J \otimes_{S_{0}} \mathcal{O}_{T_{0}}$ are coherent sheaves, so is the sheaf $\mathcal{E}$; moreover
$\mathcal{E}$ has its support in $T_{0}$, since this is the case for $J \otimes_{S_{0}} \mathcal{O}_{T_{0}}$. To show
that the section $\Psi$ of $\mathcal{E}$ is zero, it suffices to see that for every point $u$ of $T_{0}$, the image of

<!-- original page 366 -->

$\Psi$ in the fiber of $\mathcal{E}$ at the point $u$ is zero. But the formation of the $Ext^{i}(\cdot, \cdot)$ of
coherent sheaves commutes with flat extensions of the base[^N.D.E-XV-2], so we are reduced to proving the existence of a
lifting of $T_{0} \cap \operatorname{Spec} \mathcal{O}_{u}$ flat over $S$. Let $s$ be the projection of $u$ on $S$; we
may then replace $S$ by $\operatorname{Spec} \mathcal{O}_{s}$ and $G$ by $G \times_{S} \operatorname{Spec}
\mathcal{O}_{s}$.

Possibly again making a faithfully flat extension, we may assume that $\mathcal{O}_{s}$ has an algebraically closed
residue field
([EGA 0_III, 10.3.1](https://jcreinhold.github.io/ega/iii/03-ch0-10-complements-flat-modules.html#103-existence-of-flat-extensions-of-local-rings)).

Let $\mathfrak{m}$ be the maximal ideal of $\mathcal{O}_{s}$ and
$S_{n} = \operatorname{Spec} \mathcal{O}_{s}/\mathfrak{m}^{n}$. Suppose we have shown that for every $n > 0$ the
obstruction to lifting $T_{0} \times_{S} S_{n} = (T_{0})_{n}$ to a subscheme of $G_{n} = G \times_{S} S_{n}$, flat over
$S_{n}$, is zero, and let $T_{n}$ be the unique flat lifting of $(T_{0})_{n}$ over $S_{n}$ which is a sub-torus of
$G_{n}$. It is clear that if $n > n'$, one has

```text
(Tₙ) ×_{Sₙ} Sₙ′ = Tₙ′.
```

If then $u$ is a point of $T_{0}$ projecting onto $s$, it follows from the lemma below, applied to the coherent system
of liftings $(T_{n} \cap \operatorname{Spec} \mathcal{O}_{u})$ of $(T_{0})_{n} \cap \operatorname{Spec}
\mathcal{O}_{u}$, that there indeed exists a lifting of $T_{0} \cap \operatorname{Spec} \mathcal{O}_{u}$ flat over
$\mathcal{O}_{s}$. We are therefore reduced to proving that $\Psi$ is zero when $S = S_{n}$ is the spectrum of an
artinian local ring with algebraically closed residue field, and to proving:

**Lemma 2.8.** *Let $A \to B$ be a local homomorphism of noetherian local rings, $\mathfrak{m}$ the maximal ideal of
$A$, $J$ an ideal of square zero of $A$, $M$ a $B$-module of finite type, $A_{0} = A/J$, $B_{0} = B/JB$, $M_{0} = M/JM$,
$N_{0}$ a quotient $B_{0}$-module of $M_{0}$ which is flat over $A_{0}$. For every integer $n > 0$, let $A_{n}$,
$A_{0},_{n}$, etc., be the objects obtained by base extension*

<!-- original page 367 -->

*$A \to A/\mathfrak{m}^{n} = A_{n}$, and let $J_{n}$ be the image of $J$ in $A_{n}$. For every integer $n > 0$, let
$N_{n}$ be a quotient $B_{n}$-module of $M_{n}$, flat over $A_{n}$, lifting $N_{0},_{n}$, and suppose that for $n
\geqslant n'$, $N_{n}'$ is obtained from $N_{n}$ by base extension $A_{n} \to A_{n}'$. Then there exists a $B$-module
$N$, quotient of $M$, flat over $A$, lifting $N_{0}$.*

<!-- label: III.XV.2.8 -->

*Proof of 2.8.* Let $P_{0}$ be the kernel of the epimorphism $M_{0} \to N_{0}$. For every $n > 0$, we have the following
commutative diagram in which the horizontal rows are exact:

```text
                                       0
                                       │
                                       ▼
                                     P₀,ₙ
                                       │
                                       ▼
   0 ──→ Jₙ Mₙ ──→ Mₙ ──→ M₀,ₙ ──→ 0
            ↗
        Jₙ ⊗_{A₀,ₙ} M₀,ₙ
            ↘
                         ▼      ▼       ▼
   0 ──→ Jₙ ⊗_{A₀,ₙ} N₀,ₙ ──→ Nₙ ──→ N₀,ₙ ──→ 0
                                       ▼     ▼
                                       0     0
```

\*(*ₙ*)

Moreover, by hypothesis, the diagram $(*)_{n+1}$ reduces modulo $\mathfrak{m}^{n}$ to $(*)_{n}$.

The Artin–Rees lemma (Bourbaki, *Algèbre commutative*, Chap. 3 § 3 cor. 1) shows that the filtration defined on `JM`
(resp. $J \otimes_{A_{0}} M_{0}$ and $J \otimes_{A_{0}} N_{0}$) by the kernels of the morphisms

<!-- original page 368 -->

```text
JM ⟶ Jₙ Mₙ,   (resp.   J ⊗_{A₀} M₀ ⟶ Jₙ ⊗_{A₀,ₙ} M₀,ₙ   and   J ⊗_{A₀} N₀ ⟶ Jₙ ⊗_{A₀,ₙ} N₀,ₙ)
```

is $\mathfrak{m}B$-good, so that, passing to the projective limit on the diagrams $(*)_{n}$ and denoting by $\hat{Q}$
the separated completion of a $B$-module $Q$ for the $\mathfrak{m}B$-adic topology, one obtains the following
commutative diagram, where the two horizontal rows are still exact:

```text
                                       0
                                       │
                                       ▼
                                      P̂₀
                                       │
                                       ▼
   0 ──→ ĴM ──→ M̂ ──→ M̂₀ ──→ 0
           ↗
        Ĵ ⊗_{A₀} M₀
           ↘
   0 ──→ Ĵ ⊗_{A₀} N₀ ──→ lim_{←n} Nₙ ──→ N̂₀ ──→ 0
                                       ▼      ▼
                                       0      0
```

(*ˆ*)

Now $(B, \mathfrak{m}B)$ is a Zariski ring and $J \otimes_{A_{0}} N_{0}$ is of finite type over $B$, so it is separated
for the $\mathfrak{m}B$-adic topology. The diagram $(\hat{*})$ then shows that the morphism

```text
J ⊗_{A₀} M₀ ⟶ J ⊗_{A₀} N₀
```

deduced from the epimorphism $M_{0} \to N_{0}$ factors through `JM`:

```text
J ⊗_{A₀} M₀ ──can.──→ JM
       ↘            ↙
        J ⊗_{A₀} N₀.
```

Under these conditions, it follows from Exp. III 4.1 and Exp. III 4.3 that there exists a $B$-module quotient $N$ of
$M$, flat over $A$, lifting $N_{0}$, if and only if a certain element $g$ of $E = Ext^{1}_{B}(P_{0}, J \otimes_{A_{0}}
N_{0})$ is zero. More precisely, the exact sequence

$$ 0 \longrightarrow JM \longrightarrow M \longrightarrow M_{0} \longrightarrow 0 $$

defines an element $f$ of $F$, where $F$ is the $B$-module $Ext^{1}_{B}(M_{0}, JM)$, and $g$ is the image of $f$

<!-- original page 369 -->

under the natural morphism $F \to E$ arising by bifunctoriality from the morphisms

```text
P₀ ⟶ M₀    and    JM ⟶ J ⊗_{A₀} N₀.
```

It follows from the diagram $(\hat{*})$ and from Exp. III 4.1 that the image of $g$ in `Ê`, canonically identified with
$Ext^{1}_{\hat{B}}(\hat{P}_{0}, \hat{J} \otimes_{A_{0}} N_{0})$, is zero. But $E$ is of finite type over $B$,

<!-- original page 370 -->

so is separated for the $\mathfrak{m}B$-adic topology, and consequently $g$ is indeed equal to `0`, which completes the
proof of 2.8.

**d) Study of $\mathcal{E}$.** We therefore suppose that $S$ is the spectrum of a local artinian ring $A$ with
algebraically closed residue field $k$. Let $A_{0}$ be the ring of $S_{0}$, $\mathfrak{m}_{0}$ the maximal ideal of
$A_{0}$. Since $S_{0}$ is artinian, $T_{0}$ is closed in $G$ (Exp. VI_B 1.4.2); we may therefore take the open subset
$U$ equal to $G$, so that

```text
ℰ = Ext¹_{𝒪_G}(K₀, J ⊗_{S₀} 𝒪_{T₀}).
```

Let $B_{0}$ be the ring of the affine $S_{0}$-scheme $T_{0} = G_{m, S_{0}}$, and $B'_{0}$ the ring of the special fiber
$T_{0} \times_{S_{0}} \operatorname{Spec}(k) = G_{m, k}$ of $T_{0}$. The sheaf $\mathcal{E}$ is a coherent
$\mathcal{O}_{T_{0}}$-module, so is defined by a $B_{0}$-module of finite type which we shall denote $E$.

Consider the graded module associated to $E$ and to the $\mathfrak{m}_{0} B_{0}$-adic filtration:

```text
Eᵣ = 𝔪₀ʳ E / 𝔪₀^{r+1} E.
```

Each `Eᵣ` is therefore a $B'_{0}$-module of finite type, and $E_{r} = 0$ for $r$ large enough, since $S_{0}$ is
artinian.

Let then $g$ be a section of $G$ above $S$ which on $S_{0}$ induces a section $g_{0}$ of $T_{0}$. Translation (on the
left, to fix ideas) by the element $g$ defines an "automorphism of the situation" from the viewpoint of the obstruction
problem under consideration. In particular, to $g$ corresponds an $S_{0}$-automorphism of the sheaf $\mathcal{E}$
leaving the obstruction $\Psi$ fixed. More precisely, $g$ defines a semi-linear automorphism of the $B_{0}$-module $E$
(relative to the $A_{0}$-automorphism of $B_{0}$ defined by translation by $g_{0}$ in the group $T_{0}$). By reduction
modulo $\mathfrak{m}^{r+1}_{0}$, $g$ then defines a semi-linear automorphism of `Eᵣ` (relative to the $k$-automorphism
of $B'_{0}$ defined by translation by $g_{0} \times_{S_{0}} \operatorname{Spec}(k)$ in $T_{0} \times_{S_{0}}
\operatorname{Spec}(k)$).

**Lemma 2.9.** *For every integer $r \geqslant 0$, `Eᵣ` is a locally free $B'_{0}$-module.*

<!-- label: III.XV.2.9 -->

Let $x$ be a point of $T_{0}$, $\kappa(x)$ its residue field, $(E_{r})_{x}$ "the fiber" of `Eᵣ` at $x$, equal to $E_{r}
\otimes_{B'_{0}} \kappa(x)$, $\ell(x)$ the rank of $(E_{r})_{x}$ over $\kappa(x)$, $\ell$ the maximum value of $\ell(x)$
as $x$ ranges over the points of $T_{0}$. Let $L$ be the largest closed subscheme of $\operatorname{Spec} B'_{0} = G_{m,
k}$ above which `Eᵣ` is locally free of rank $\ell$ (TDTE IV Lemma 3.6). Let $\beta$ be a point of $L(k)$ (there is one,
$L$ being of finite type over $k$ algebraically closed) and let $\alpha$ be a point of $G_{m, k}(k)$ of order equal to a
power $n$ of $q$. The point $\alpha$ is therefore rational

<!-- original page 371 -->

over $k$, and since by hypothesis ${}_{n}T_{0}$ lifts to a subscheme $M_{n}$ étale over $S$, there exists a section $a$
of $G$ above $S$ which lifts $\alpha$ and which, above $S_{0}$, is a section of $T_{0}$. The remarks made above then
show that the fibers of `Eᵣ` are $k$-isomorphic at the points $\beta$ and $\alpha \beta$ of $G_{m, k}(k)$. But the
points of order a power of $q$ are dense in $G_{m, k}$, and similarly their translates by $\beta$. Since $L$ is closed
in $G_{m, k}$ and $G_{m, k}$ is reduced, $L$ equals $G_{m, k}$ and `Eᵣ` is locally free over $B'_{0}$ of rank $\ell$.

**e) End of the proof of Theorem 2.1.**

Let $K_{0}(n)$ be the sheaf of ideals of $\mathcal{O}_{G_{0}}$ defining the closed subscheme ${}_{n}T_{0}$. The sheaf
$K_{0}$[^N.D.E-XV-3] is therefore a subsheaf of $K_{0}(n)$. Set, for simplicity,

```text
R = J ⊗_{S₀} 𝒪_{T₀}    and    R(n) = J ⊗_{S₀} 𝒪_{ₙT₀}.
```

The sheaf $R(n)$ is therefore a quotient of $R$, and one has the diagram of morphisms:

```text
                K₀
                │
                ▼
              K₀(n)
                │
                ▼
0 ──→ J𝒪_G ──→ 𝒪_G ──→ 𝒪_{G₀} ──→ 0
        │
        ▼
        R
        │
        ▼
      R(n)
```

Using then the bifunctoriality of $Ext^{1}_{\mathcal{O}_{G}}(\cdot, \cdot)$, one obtains the following commutative
diagram:

```text
Ext¹_{𝒪_G}(𝒪_{G₀}, J𝒪_G)
        ↘
         Ext¹_{𝒪_G}(K₀(n), R) ──→ Ext¹_{𝒪_G}(K₀, R) = ℰ
               │                          │
               ▼                          ▼
         Ext¹_{𝒪_G}(K₀(n), R(n)) ──→ Ext¹_{𝒪_G}(K₀, R(n)).
```

Let us again denote by $\Phi$ the element of $Ext^{1}_{\mathcal{O}_{G}}(\mathcal{O}_{G_{0}}, J\mathcal{O}_{G})$ defined
by the exact sequence

<!-- original page 372 -->

$$ 0 \longrightarrow J\mathcal{O}_{G} \longrightarrow \mathcal{O}_{G} \longrightarrow \mathcal{O}_{G_{0}}
\longrightarrow 0, $$

so that $\Psi$ is the image of $\Phi$ in $\mathcal{E}$. Since ${}_{n}T_{0}$ lifts to a subscheme $M_{n}$ of $G$, flat
over $S$, the image of $\Phi$ in the sheaf $Ext^{1}_{\mathcal{O}_{G}}(K_{0}(n), R(n))$ is zero (Exp. III 4.1); *a
fortiori*, the image of $\Phi$ in $Ext^{1}_{\mathcal{O}_{G}}(K_{0}, R(n))$, which is also the image of $\Psi$, is zero.

**Lemma 2.10.** *The canonical morphism*

```text
Ext¹_{𝒪_G}(K₀, R) ⊗_{B₀} 𝒪_{ₙT₀} ⟶ Ext¹_{𝒪_G}(K₀, R(n))
```

*is injective for every integer $n$.*

<!-- label: III.XV.2.10 -->

Indeed, the affine scheme $T_{0} = G_{m, S_{0}}$ has ring

$$ B_{0} = A_{0}[T, T^{-1}]. $$

The subscheme ${}_{n}T_{0}$ is defined by the vanishing of the following section of $B_{0}$:

$$ h(n) = T^{n} - 1, $$

which is regular
([EGA 0_IV 15.2.2](https://jcreinhold.github.io/ega/iv/02-ch0-15-mf-regular-sequences.html#152-f-regular-sequences)) and
remains regular after any base change $S'_{0} \to S_{0}$. We therefore have an exact sequence of sheaves:

```text
0 ⟶ 𝒪_{T₀} ──h(n)──→ 𝒪_{T₀} ⟶ 𝒪_{ₙT₀} ⟶ 0.
```

<!-- original page 373 -->

Since ${}_{n}T_{0}$ is flat over $S$, one obtains, by tensoring with $J$ over $\mathcal{O}_{S_{0}}$, the exact sequence

```text
0 ⟶ R ──h(n)──→ R ⟶ R(n) ⟶ 0,
```

then the exact sequence of `Ext`:

```text
⋯ ⟶ Ext¹_{𝒪_G}(K₀, R) ──h(n)──→ Ext¹_{𝒪_G}(K₀, R) ⟶ Ext¹_{𝒪_G}(K₀, R(n)),
```

which completes the proof of the lemma.

The foregoing shows that for every integer $n$ equal to a power of $q$, the image of $\Psi$ in
$\mathcal{E}/h(n)\mathcal{E}$ is zero. To show that $\Psi$ is zero, it suffices to see that if $\Psi \in
\mathfrak{m}^{r}_{0} \mathcal{E}$, then $\Psi \in \mathfrak{m}^{r+1}_{0} \mathcal{E}$. Let $\bar{\Psi}$ be the image of
$\Psi$ in `Eᵣ`. There exists an element $\Psi(n)$ of $\mathcal{E}$ such that one has

```text
Ψ = Ψ(n) · h(n)    (n equal to a power of q).
```

We noted that the image $\bar{h}(n)$ of $h(n)$ in $B'_{0}$ is again $B'_{0}$-regular. Since $E_{s}$ is locally free over
$B'_{0}$ for every $s$ (2.9), multiplication by $\bar{h}(n)$ in `Eᵣ` is injective. One deduces immediately that
$\Psi(n)$ is in $\mathfrak{m}^{r}_{0} \mathcal{E}$. Let $\bar{\Psi}(n)$ be its image in `Eᵣ`, so that one has the
relation

```text
Ψ̄ = h̄(n) Ψ̄(n)    (n equal to a power of q).
```

This shows that the set $F$ of points of $G_{m, k}$ at which $\bar{\Psi}$ takes the value `0` contains the dense set of
points of order a power of $q$. Moreover $F$ is a closed set (since `Eᵣ` is locally free over $B'_{0}$) and $G_{m, k}$
is reduced, so $\bar{\Psi}$ is zero.

This completes the proof of Theorem 2.1.

## 3. Characterization of a sub-torus by its underlying set

<!-- label: III.XV.3 -->

<!-- original page 374 -->

### 3.1. Statement of the theorem

<!-- label: III.XV.3.statement -->

**Notation.** If $X$ is a prescheme, $ens(X)$ denotes the underlying set of $X$. If $X$ and $S'$ are two $S$-preschemes,
$X_{S'} = X \times_{S} S'$, $u : X_{S'} \to X$ the canonical morphism, $E$ a subset of $ens(X)$, one denotes by $E_{S'}$
(or $E \times_{S} S'$) the subset of $ens(X_{S'})$ equal to $u^{-1}(E)$.

**Theorem 3.1.** *Let $S$ be a locally noetherian prescheme, $G$ an $S$-prescheme in groups of finite type, $q$ an
integer `> 0` invertible on $S$, $E$ a subset of $ens(G)$. Consider the following assertions concerning $E$:*

- *(i) The set $E$ is the underlying set of a sub-torus $T$ of $G$.*
- *(ii) a) For every point $s$ of $S$, there exists a sub-torus $T_{s}$ of $G_{s}$ such that $E \cap ens(G_{s}) = E_{s}$
  is the underlying set of $T_{s}$.*
- - b) As the integer $n$ ranges over powers of $q$, there exists a coherent family (cf. 2.2) $M_{n}$ of subgroup
    schemes of $G$, of multiplicative type, such that for every point $s$ of $S$ one has\*

$$ (M_{n})_{s} = {}_{n} T_{s}. $$

- *(iii) a) As in (ii) a).*
- - b) The set $E$ is locally closed in $ens(G)$, and the dimension of the fibers of $E$ over $S$ is locally constant.\*
- *(iv) a) As in (ii) a).*
- - b) For every $S$-scheme $S'$ which is the spectrum of a complete discrete valuation ring with algebraically closed
    residue field, $E_{S'}$ is the underlying set of a sub-torus of $G_{S'}$.\*

*Then one has the following implications:*

- *A) (i) ⇔ (ii) ⇒ (iii) ⇒ (iv).*
- *B) If $G$ is separated over $S$, one has (iii) ⇔ (iv), and moreover $E$ is closed.*
- *C) Conditions (i), (ii), (iii) (and also (iv) if $G$ is separated over $S$) are equivalent in the following two
  cases:*
- - 1st case: a) The prescheme $S$ is reduced, or $G$ is flat over $S$, and\*
- - ```
    b) For every point `s` of `S`, `Tₛ` is a central torus of `Gₛ`.*
    ```
    ```
    - - 2nd case: `S` is normal.\*
    ```

<!-- original page 375 -->

*Moreover, in the two cases above, the torus $T$ with underlying set $E$ is unique.*

<!-- label: III.XV.3.1 -->

**Remarks 3.2.** a) When $S$ is reduced, it is unnecessary in (ii) to assume that the family $M_{n}$ is coherent, this
condition being entailed by the other hypotheses. Indeed, if the integer $m$ divides $n$, the subgroups ${}_{m}M_{n}$
and $M_{m}$ are étale over $S$, hence reduced, and have the same underlying space, so they coincide.

<!-- original page 376 -->

b) If $S$ is not assumed normal, it is no longer true in general that (iii) ⇒ (i), even when $S$ is reduced,
geometrically unibranched and $G$ is a smooth group scheme over $S$. Indeed, consider the Borel subgroup of $SL_{2, S}$
formed by matrices of the form

$$ ( t u) ( 0 t^{-1}), $$

where $S$ is the affine curve over a field $k$ with ring

$$ k[x, y]/(y^{2} - x^{3}). $$

Consider then the set $E$ obtained as follows: above the "cusp of $S$" ($x = y = 0$) we take the diagonal torus ($u =
0$). Above the complementary open subset ($x \neq 0$) we take the torus deduced from the diagonal torus by conjugation
by the element

$$ ( 1 y/x) ( 0 1). $$

The set $E$ so obtained satisfies (iii) a); on the other hand it is closed in $G$, and the reduced subscheme having $E$
as underlying set has equations

$$ xu + y(t - t^{-1}) = 0 u^{2} - x(t - t^{-1})^{2} = 0. $$

<!-- original page 377 -->

This is therefore not a sub-torus of $G$, since the fiber above the cusp is not reduced.

<!-- label: III.XV.3.2 -->

**Plan of the proof of 3.1.** In a first part we shall establish the following "easy" implications:

```text
                  (ii)
              ↗        ↘
         (i)              (iv)
              ↘        ↗
                  (iii)
```

and `[(iv) ⇒ (iii) and E closed if G is separated over S]`.

The proof of the more delicate implications will be carried out in three stages:

- I) Reduction of the implication (iii) ⇒ (i) (under the hypotheses of C), 1st case) to the case where $S$ is normal.
- II) (iii) ⇒ (ii) when $S$ is normal.
- III) (ii) ⇒ (i).

### 3.2. Proof of the "easy" assertions contained in 3.1

<!-- label: III.XV.3.easy -->

(i) ⇒ (ii) and (iii) is trivial.

(iii) ⇒ (iv). Possibly replacing $S$ by $S'$, we may assume that $S$ is the spectrum of a discrete valuation ring. Let
$t$ be the generic point of $S$ and $s$ the closed point.

Since $E$ is locally closed, there exists a subprescheme of $G$ which is reduced and whose underlying space is $E$; we
shall denote it $E$. The generic fiber $E_{t}$ of $E$ is therefore equal to the sub-torus $T_{t}$ of rank $r$ of $G_{t}$
(by (iii) a)). Let $E'$ be the schematic closure of $E_{t}$ in $E$. The prescheme

<!-- original page 378 -->

$E'$ is irreducible, and its closed fiber $E'_{s}$ is non-empty (it contains the unit section of $G_{s}$), so $E'_{s}$
is of dimension $r$ (EGA IV 14.3.10). But then $E'_{s}$ is a closed subscheme of $E_{s}$, and the latter is of dimension
$r$ (by (iii) b)) and irreducible (since it has the same underlying space as $T_{s}$), so $E'_{s}$ has the same
underlying space as $E_{s}$, and consequently $E' = E$, which proves that $E$ is flat over $S$.

Let now $E''$ be the schematic closure of $E_{t}$ in $G$. Then $E''$ is a subprescheme in groups of $G$, flat over $S$
(Exp. VIII 7.1), which majorizes $E'$, hence $E$. The closed

<!-- original page 379 -->

fiber $E''_{s}$ is an algebraic subgroup of $G_{s}$ of dimension $r$ (*loc. cit.*). Since $T_{s}$ is a closed
irreducible subset of $G_{s}$ of dimension $r$, $E_{s}$ has the same underlying set as the connected component
$(E''_{s})^{0}$ of $E''_{s}$. Let $(E'')^{0}$ be the "connected component" of $E''$, i.e. the open subgroup of $E''$
complementary to the union of the irreducible components of $E''_{s}$ not containing the origin. One then has

$$ E = ens[(E'')^{0}]. $$

Since $E$ and $E''$ are reduced, one has even $E = (E'')^{0}$. Finally $E$ is a subgroup prescheme of $G$, flat and of
finite type over $S$, with connected fibers, hence separated (Exp. VI_B 5.2), whose generic fiber is a torus $T_{t}$,
and whose reduced closed fiber is a torus $T_{s}$; but then $E$ is a torus (Exp. X 8.8).

(ii) ⇒ (iv). One may again assume that $S$ is the spectrum of a discrete valuation ring, and we keep the notation
introduced above. The schematic closure in $G$ of $T_{t}$ is a subgroup prescheme $T$ of $G$, flat over $S$, which
majorizes $M_{n}$ for every integer $n$ equal to a power of $q$. Consequently the closed fiber of $T$ is a closed
subscheme of $G_{s}$ majorizing $(M_{n})_{s}$ for every $n$, hence majorizing $T_{s}$. For dimension reasons, the
"connected component" $T^{0}$ of $T$ has $E$ as underlying set, and one concludes as above that $T^{0}$ is a sub-torus
of $G$.

(iv) ⇒ \[(iii) and $E$ closed\], if $G$ is separated over $S$. Let us show that $E$ is closed.[^N.D.E-XV-4] First let us
prove the lemma:

**Lemma 3.3.** *If the conditions stated in 3.1 (iv) are satisfied, $E$ is a locally constructible part of $ens(G)$.*

<!-- label: III.XV.3.3 -->

By the usual method, we are reduced to studying the case where $S$ is noetherian, integral, with generic point $\eta$.
Possibly restricting $S$, we may assume (Exp. VI_B 10.10) that there exists a subgroup scheme $H$ of $G$, flat over $S$,
with connected fibers, whose generic fiber $H_{\eta}$ is equal to $T_{\eta}$. To prove 3.3 it then suffices to show that
$ens(H) = E$. Now if $s$ is a point of $S$, there exists, by EGA II 7.1.9, an $S$-scheme $S'$, the spectrum of a
discrete valuation ring, that one may assume complete with algebraically closed residue field, whose generic point $t'$
projects onto $\eta$ and whose closed point $s'$ projects onto $s$. By (iv) b), there exists a sub-torus $T_{S'}$ of
$G_{S'}$ having $E_{S'}$ as underlying space. The two subprescheme in groups $T_{S'}$ and $H_{S'} = H \times_{S} S'$ of
$G_{S'}$ are flat over $S'$, have connected fibers, and the same generic fiber $T_{t'}$, so they coincide with the
connected component of the schematic closure

<!-- original page 380 -->

of $T_{t'}$ in $G_{S'}$. Consequently $ens(H_{s}) = E_{s}$, so $ens(H) = E$, which proves the lemma.

This being so, knowing that $E$ is locally constructible, in order to see that $E$ is closed it suffices to show that
every specialization in $G$ of a point of $E$ is a point of $E$. By the usual technique we are reduced to the case where
$S$ is the spectrum of a complete discrete valuation ring with algebraically closed residue field. But then the
sub-torus of $G$ of underlying space $E$ ((iv) b)) is closed in $G$ since $G$ is separated (Exp. VIII 7.12).

### 3.3. Continuation of the proof of 3.1

<!-- label: III.XV.3.cont -->

**I) Reduction of (iii) ⇒ (i) (C, 1st case) to the case where $S$ is normal.**

**a) Reduction to the case $S$ affine reduced.** We therefore assume that for every point $s$ of $S$, $E_{s}$ is the
underlying space of a central sub-torus of $G_{s}$. The uniqueness of $T$ then follows from Exp. IX 5.1 bis, and
moreover $T$ will necessarily be central (*loc. cit.*). In view of uniqueness, to prove the existence of $T$ we may
assume $S$ noetherian, affine of ring $A$. If $S$ is not reduced, by hypothesis $G$ is flat over $S$. By 2.3 it then
suffices to solve the problem for $S_{red}$ and $G \times_{S} S_{red}$. We may therefore assume in addition that $S$ is
reduced.

**b) Reduction to the case where the ring $A$ is of finite type over $\mathbb{Z}$.** Let us first prove two lemmas:

<!-- original page 381 -->

**Lemma 3.4.** *Let $k$ be a field, $G$ a $k$-algebraic group, $E$ a subset of $G$, $k'$ an extension of $k$, $T_{k'}$ a
sub-torus of $G_{k'}$ having $E_{k'}$ as underlying space. Then, if $T_{k'}$ is central or if $k$ is perfect, $E$ is the
underlying set of a sub-torus of $G_{k}$.*

<!-- label: III.XV.3.4 -->

Indeed, by fpqc descent it suffices to show that the two inverse images of $T_{k'}$ in $G_{k''}$, where $k'' = k'
\otimes_{k} k'$, coincide. Now they have the same underlying space, namely the inverse image of $E$. If $T_{k'}$ is
central, the lemma is a consequence of Exp. IX 5.1 bis. If $k$ is perfect, $k''$ is reduced and the two inverse images
of $T_{k'}$, being smooth over $k''$, are reduced, hence coincide.

**Remark 3.5.** It follows from the preceding lemma that in the statement of 3.1 (iv), property (iv) a) is a consequence
of (iv) b) in the two following cases:

1. One assumes that the residue fields of the points of $S$ are perfect.
1. For every $S'$ as in (iv) b), one assumes that the torus with underlying space $E_{S'}$ is central in $G_{S'}$.

<!-- label: III.XV.3.5 -->

**Lemma 3.6.** *Let $S$ be a prescheme projective limit of affine schemes `Sᵢ` (cf. EGA IV 8), $H$ an $S$-group scheme
of multiplicative type and of finite type. Then there exist an index $i$, an `Sᵢ`-group scheme `Hᵢ` of multiplicative
type and of finite type, and an $S$-isomorphism*

```text
Hᵢ ×_{Sᵢ} S ⥲ H.
```

*If moreover $H$ is isotrivial, one may assume `Hᵢ` isotrivial.*

<!-- label: III.XV.3.6 -->

<!-- original page 382 -->

Since $H$ is of finite type over $S$, $H$ is in fact of finite presentation over $S$ (Exp. IX 2.1 b)); there therefore
exist an index $\ell$ and an $S_{\ell}$-group scheme $H_{\ell}$ such that $H_{\ell} \times_{S_{\ell}} S$ is isomorphic
to $H$ (Exp. VI_B 10). Setting $H_{i} = H_{\ell} \times_{S_{\ell}} S_{i}$, one therefore has $H \cong H_{i}
\times_{S_{i}} S$ for every $i \geqslant \ell$.

Since $H$ is of finite type over $S$, $H$ is quasi-isotrivial (Exp. X 4.5), hence trivialized by an étale surjective
morphism $S' \to S$. Using the quasi-compactness of $S$, one easily sees that there exist a covering of $S$ by a finite
number of affine open subsets $S_{\alpha}$, and for every $\alpha$ an étale, surjective and finitely presented morphism
$S'_{\alpha} \to S_{\alpha}$ trivializing $H|S_{\alpha}$. This covering $(S_{\alpha})$ of $S$ then comes from a covering
$(S_{i, \alpha})$ of `Sᵢ` for $i$ large enough (EGA IV 8). Possibly replacing `Sᵢ` by $S_{i, \alpha}$ and $S$ by
$S_{\alpha}$, we may therefore assume that $H$ is trivialized by an étale surjective morphism $S' \to S$ of finite
presentation. For $i$ large enough, there then exist a prescheme $S'_{i}$, an étale surjective morphism $S'_{i} \to
S_{i}$ of finite presentation, and an $S$-isomorphism $S'_{i} \times_{S_{i}} S \to S'$ (EGA IV 17.16). Set then for $j$
large enough:

```text
S′_j = S′ᵢ ×_{Sᵢ} S_j,    H′_j = H_j ×_{S_j} S′_j,    H′ = H ×_S S′.
```

Given the choice of $S'$, there exist a finitely generated abelian group $M$ and an $S'$-isomorphism of group schemes
$D_{S'}(M) \xrightarrow{\sim} H'$. Since the $S'_{i}$ are quasi-compact and $S' = \lim S'_{i}$, it follows from Exp.
VI_B 10 that there exist an index $j$ and an $S'_{j}$-isomorphism of group schemes

$$ D_{S'_{j}}(M) \xrightarrow{\sim} H'_{j}. $$

But this says that $H_{j}$ is a quasi-isotrivial group of multiplicative type.

<!-- original page 383 -->

When $H$ is isotrivial, one proceeds analogously, using a trivialization of $H$ by a finite étale morphism $S' \to S$.

This being so, we can carry out the announced reduction b). The ring $A$ of $S$ is a filtered inductive limit of its
subrings `Aᵢ` of finite type over $\mathbb{Z}$. Let $S_{i} = \operatorname{Spec} A_{i}$, $u_{j} : S \to S_{j}$ and
$u_{jk} : S_{k} \to S_{j}$ ($k \geqslant j$) the transition morphisms. Since $S$ is noetherian and $G$ is of finite
presentation over $S$, there exist an index $i$ and an `Sᵢ`-prescheme in groups `Gᵢ`, of finite type over `Sᵢ`, such
that $G$ is $S$-isomorphic to $G_{i} \times_{S_{i}} S$. Similarly, since $E$ is locally closed in $G$, we may assume
that there exists a locally closed subset `Eᵢ` of `Gᵢ` such that $E = E_{i} \times_{S_{i}} S$ (EGA IV 8.3.11). For every
$j > i$, let $G_{j} = G_{i} \times_{S_{i}} S_{j}$ and $E_{j} = E_{i} \times_{S_{i}} S_{j}$, and let $Q_{j}$ be the set
of points $s$ of $S_{j}$ such that $(E_{j})_{s}$ is the underlying set of a central sub-torus of $(G_{j})_{s}$.

It follows from 3.4 that $Q_{k} = u^{-1}_{jk}(Q_{j})$ for $k \geqslant j$, and by hypothesis $ens(S) =
u^{-1}_{j}(Q_{j})$ for $j \geqslant i$. Moreover, I claim that $Q_{j}$ is ind-constructible (EGA IV 1.9.4). Indeed,
since $S_{j}$ is noetherian, it suffices (EGA IV 1.9.10) to see that if $S$ is a noetherian integral scheme with generic
point $\eta$, and if $E_{\eta}$ is the underlying set of a central sub-torus $T_{\eta}$ of $G_{\eta}$, there exists a
neighborhood $U$ of $\eta$ such that for every point $s$ of $U$, $E_{s}$ has the same property. Now, possibly
restricting $S$, we may assume that the

<!-- original page 384 -->

center $Z$ of $G$ is representable and that there exists a subgroup scheme $T$ of $G$ whose generic fiber is $T_{\eta}$
(VI_B § 10). But then $ens(T)$ and $E$ are two locally closed subsets of $ens(G)$ which coincide on the generic fiber;
one may therefore find a neighborhood $U$ of $\eta$ such that, above $U$, $ens(T) = E$ (EGA IV 8.3.11). For the same
reasons, one may assume that above $U$, $T$ is central, since $T$ is a torus (3.6).

Knowing now that $Q_{j}$ is ind-constructible, it follows from EGA IV 8.3.4 that $Q_{j} = ens(S_{j})$ for $j$ large
enough. We may then replace $S$, $G$, $E$ by $S_{j}$, $G_{j}$, $E_{j}$, which reduces us to the case where $S$ is an
affine reduced scheme of finite type over $\mathbb{Z}$.

**c) Reduction to the case where $S$ is the spectrum of a complete reduced noetherian local ring.** Owing to the
uniqueness of the torus of underlying set $E$, the usual technique (EGA IV 8) and Lemma 3.6 allow us to replace $S$ by
the spectrum of the local ring $A$ of a point of $S$. Let `Ŝ` be the spectrum of the completion `Â` of $A$ for the
topology defined by the maximal ideal. Since $A$ is the localization of a finitely generated algebra over $\mathbb{Z}$,
`Ŝ` is still

<!-- original page 385 -->

reduced (EGA IV 7.6.5). I claim that it suffices to solve the problem after the base change $\hat{S} \to S$. Indeed if
$\hat{T}$ is the sub-torus of $G_{\hat{S}}$ with underlying space $E_{\hat{S}}$, its two inverse images in $G_{\hat{S}}
\times_{S} \hat{S}$ are two central sub-tori with the same underlying space, so they coincide (Exp. IX 5.1 bis), and by
fpqc descent, $\hat{T}$ comes from a torus $T$ of $G$ which answers the question (cf. 3.4).

**d) A descent lemma.** Let us recall the following properties of finite morphisms which were noted in TDTE I: Let $S$
and $S'$ be two preschemes and $u : S' \to S$ a finite morphism. Then:

1. The morphism $u$ is an epimorphism if and only if the canonical morphism of sheaves $\mathcal{O}_{S} \longrightarrow
   u_{*}(\mathcal{O}_{S'})$ is injective.
1. The morphism $u$ is an effective epimorphism (Exp. IV 1.3) if and only if the canonical diagram $0 \longrightarrow
   \mathcal{O}_{S} \longrightarrow u_{*}(\mathcal{O}_{S'}) \Rightarrow u_{*}(\mathcal{O}_{S'}) \otimes_{\mathcal{O}_{S}}
   u_{*}(\mathcal{O}_{S'})$ is exact.
1. If moreover $S$ is noetherian and if $u$ is an epimorphism, $u$ is the composite of a finite sequence of effective
   finite epimorphisms.

We are then in a position to prove the following lemma, whose proof uses a technique of non-flat descent:

**Lemma 3.7.** *Let $S$ be a locally noetherian prescheme, $G$ an $S$-prescheme in groups of finite type, $S'$ a
prescheme and $u : S' \to S$ a finite morphism. For every $S$-prescheme $T$, let $M(T)$ denote the set of subgroups of
multiplicative type of `G_T`*

<!-- original page 386 -->

*(resp. the set of central subgroups of multiplicative type of `G_T`), so that $M$ is in a natural way a contravariant
functor defined on $Sch/S$. Then, if $u$ is an effective epimorphism (resp. an epimorphism), the diagram of sets*

```text
(*)    M(S) ⟶ M(S′) ⇒ M(S′ ×_S S′)
```

*is exact.*

<!-- label: III.XV.3.7 -->

*Proof.* i) **Reduction to the case where $u$ is an effective epimorphism.** We are then interested in the functor of
central subgroups of multiplicative type of $G$. The injectivity of $M(S) \to M(S')$ is a local question on $S$, and,
this injectivity being granted, the exactness of (\*) becomes a local problem on $S$. We may therefore assume $S$ affine
noetherian.

Let us study the case where $u : S' \to S$ is the composite of two finite epimorphisms:

```text
S′ ──v──→ S″ ──w──→ S.
```

I claim that if the two diagrams

```text
(*)′    M(S″) ⟶ M(S′) ⇒ M(S′ ×_{S″} S′)
(*)″    M(S) ⟶ M(S″) ⇒ M(S″ ×_S S″)
```

are exact, then so is (\*).

Indeed the injectivity of $M(S) \to M(S')$ is clear. If now $T'$ is an element of $Ker M(S') \Rightarrow M(S' \times_{S}
S')$, *a fortiori* $T'$ belongs to $Ker M(S') \Rightarrow M(S' \times_{S''} S')$, so by exactness of (\*)′ comes from a
unique element $T''$ of $M(S'')$. It suffices

<!-- original page 387 -->

to show that $T''$ belongs to $Ker M(S'') \Rightarrow M(S'' \times_{S} S'')$, since, by exactness of (\*)″, $T''$ will
descend to $S$. Let $T''_{1}$ and $T''_{2}$ be the two inverse images of $T''$ in $M(S'' \times_{S} S'')$. Since these
are two central subgroups of multiplicative type of $G_{S'' \times_{S} S''}$, to show that $T''_{1} = T''_{2}$ it
suffices to see that they have the same fibers (Exp. IX 5.1 bis). Consider the commutative diagram

```text
S′ ←──── S′ ×_S S′
│          │
v          v × v
▼          ▼
S″ ←──── S″ ×_S S″.
```

The morphism $v$ is a finite epimorphism, hence is dominant (property (a) above) and closed, hence is surjective, and
the same is true of $v \times v$. Let $x''$ be a point of $S'' \times_{S} S''$ and $x'$ a point of $S' \times_{S} S'$
above $x''$. It follows from commutativity of the diagram above that the two inverse images of $(T''_{1})_{x''}$ and
$(T''_{2})_{x''}$ in $G_{x'}$ coincide, so $(T''_{1})_{x''} = (T''_{2})_{x''}$ (EGA IV 2.2.15).

What precedes, and an immediate induction on the number of factors of a factorization of $u : S' \to S$ into effective
epimorphisms (property (c) recalled above), show that to prove the exactness of (\*) in the case of central subgroups of
multiplicative type, we may restrict to the case where $u$ is an effective epimorphism. Finally, using once again Exp.
IX 5.1 bis, one sees that it suffices to prove 3.7 when $M$ is the functor of subgroups of multiplicative type of $G$
and $u$ an effective epimorphism.

ii) **Injectivity of $M(S) \to M(S')$.** Since $u : S' \to S$ is an epimorphism, the canonical

<!-- original page 388 -->

morphism $\mathcal{O}_{S} \longrightarrow u_{*}(\mathcal{O}_{S'})$ is injective; moreover an $S$-group of multiplicative
type is flat over $S$; the injectivity of $M(S) \to M(S')$ is therefore a consequence of the more general following
lemma:

**Lemma 3.8.** *Let $f : X \to S$ and $g : S' \to S$ be two morphisms of preschemes, $\mathcal{F}$ a quasi-coherent
$\mathcal{O}_{X}$-module, $X' = X \times_{S} S'$, $\mathcal{F}' = \mathcal{F} \otimes_{\mathcal{O}_{S}}
\mathcal{O}_{S'}$, $Q(\mathcal{F})$ the set of quotient $\mathcal{O}_{X}$-modules $\mathcal{G}$ of $\mathcal{F}$ which
are quasi-coherent and flat over $S$, $Q(\mathcal{F}')$ the analogue relative to $\mathcal{F}'$, $X'$ and $S'$. Suppose
$g$ is quasi-compact and $\mathcal{O}_{S} \to g_{*}(\mathcal{O}_{S'})$ injective; then the canonical map*

```text
Q(ℱ) ⟶ Q(ℱ′)
𝒢 ↦ 𝒢 ⊗_{𝒪_S} 𝒪_{S′}
```

*is injective.*

<!-- label: III.XV.3.8 -->

Indeed, one may assume $S$ affine, then $X$ affine. The morphism $g$ being quasi-compact, $S'$ is then a union of a
finite number of affine open subsets $S'_{i}$. Possibly replacing $S'$ by $\coprod S'_{i}$ (an operation which preserves
the injectivity of $\mathcal{O}_{S} \to g_{*}(\mathcal{O}_{S'})$), one may assume $S'$ affine. One is then reduced to
proving the following lemma, whose proof is immediate:

<!-- original page 389 -->

**Lemma 3.9.** *Let $A \to A'$ be an injective homomorphism of rings, $M$ an $A$-module, $N = M/P$ a quotient $A$-module
flat over $A$, $M' = M \otimes_{A} A'$, $N' = N \otimes_{A} A' = M'/P'$. Then $P$ is the inverse image of $P'$ under the
canonical homomorphism $M \to M'$ (so $N$ and $P$ are known when one knows $N'$ and $P'$).*

<!-- label: III.XV.3.9 -->

iii) **Exactness of 3.7 (\*) at $M(S')$.** Let $T'$ be an element of $Ker M(S') \Rightarrow M(S' \times_{S} S')$.
Suppose we have proved iii) when $S$ is the spectrum of a noetherian local ring. For every point $s$ of $S$, there then
exists a subgroup of multiplicative type $T_{s}$ of $G \times_{S} \operatorname{Spec}(\mathcal{O}_{S, s})$ which comes
by descent from $T' \times_{S'} u^{-1} \operatorname{Spec}(\mathcal{O}_{S, s})$. By (Exp. VI_B § 10 and 3.6), there
exist a neighborhood $U$ of $s$ in $S$ and a subgroup scheme $T$ of $G$ above $U$ which is of multiplicative type and
which extends $T_{s}$. Let $U'$ be the inverse image of $U$ in $S'$. One then knows two subschemes of $G'|U'$: $T'|U'$
and $T \times_{U} U'$, which coincide on $u^{-1}(\operatorname{Spec}(\mathcal{O}_{S, s}))$. If one regards
$u^{-1}(\operatorname{Spec}(\mathcal{O}_{S, s}))$ as the projective limit of the schemes $u^{-1}(V)$ where $V$ ranges
over the open neighborhoods of $s$ in $U$, it follows from EGA IV 8 that there exists an open neighborhood $V$ of $s$ in
$U$ such that $T \times_{U} U'$ and $T'$ coincide above $u^{-1}(V)$. So with the hypotheses made, $T'$ descends locally
on $S$; but, owing to the uniqueness proved in ii), $T'$ then descends globally on $S$. In short, it suffices to prove
iii) when $S$ is the spectrum of a noetherian local ring.

<!-- original page 390 -->

Let then `Ŝ` denote the spectrum of the completion of the ring of $S$, and let $S'' = S' \times_{S} S'$, $\hat{S}' =
\hat{S} \times_{S} S'$, $\hat{S}'' = \hat{S} \times_{S} S'' = \hat{S}' \times_{\hat{S}} \hat{S}'$. I claim it suffices
to show that the diagram

$$ (*) M(\hat{S}) \longrightarrow M(\hat{S}') \Rightarrow M(\hat{S}'') $$

is exact at $M(\hat{S}')$. This follows from the commutative diagram below, in which the second row is exact at
$M(\hat{S}')$ by hypothesis, the first two columns are exact (fpqc descent), and the map $f$ is injective as follows
from ii) applied to the finite epimorphism

```text
Ŝ′ ×_{Ŝ} Ŝ′ ⟶ Ŝ ×_S Ŝ
```

deduced from $S' \to S$ by the flat base change $\hat{S} \times_{S} \hat{S} \to S$:

```text
M(S) ────→ M(S′) ───⇒───→ M(S″)
  │            │             │
  ▼            ▼             ▼
M(Ŝ) ────→ M(Ŝ′) ───⇒───→ M(Ŝ″)
  │ ▼          │ ▼
M(Ŝ ×_S Ŝ) ──f──→ M(Ŝ′ ×_{S′} Ŝ′)
```

(the diagram-chase is left to the reader). It follows from the characterization (b) of effective finite epimorphisms
that the morphism $\hat{S}' \to \hat{S}$, deduced from $S' \to S$ by the flat base change $\hat{S} \to S$, is again an
effective finite epimorphism. We are therefore reduced to the case where furthermore $S$ is the spectrum of a complete
noetherian local ring.

<!-- original page 391 -->

Let $S_{0}$ denote the reduced subscheme of $S$ whose underlying space is the closed point of $S$. Let $T'$ be an
element of $Ker M(S') \Rightarrow M(S'')$, $T'_{0}$ its image in $M(S'_{0})$. Since $S''_{0} = S'_{0} \times_{S_{0}}
S'_{0}$ is faithfully flat over $S_{0}$, there exists an $S$-subgroup of multiplicative type $T'_{S_{0}}$ of $G_{S_{0}}$
whose inverse image in $G_{S''_{0}}$ is $T'_{S'_{0}}$ (fpqc descent). But $S$ is local complete noetherian, so there
exist an $S$-group of multiplicative type $T$ and an $S_{0}$-morphism $u_{0} : T \times_{S} S_{0} \to T'_{S_{0}}$ (Exp.
X 3.3). The inverse image $u'_{0}$ of $u_{0}$ above $S'_{0}$ extends uniquely to an $S'$-isomorphism $u' : T_{S'} \to
T'$, still by Exp. X 3.3 (note that $S'$, being finite over $S$ local complete, is the sum of a finite number of
complete local schemes). The two inverse images of $u'$ above $S''$ are two morphisms of $T_{S''}$ into $T''$ which
coincide on $S_{0} \times_{S} S''$, so they coincide (*loc. cit.*). Since $T$ is flat over $S$ and $S' \to S$ is a
finite effective epimorphism, it follows from TDTE I page 8 that the diagram

```text
Hom_S(T, G) ⟶ Hom_{S′}(T_{S′}, G_{S′}) ⇒ Hom_{S″}(T_{S″}, G_{S″})
```

is exact. So $u'$ comes from a morphism of preschemes $u : T \to G$. Similarly $T \times_{S} T$ is flat over $S$, and
consequently the map

```text
Hom_S(T ×_S T, G) ⟶ Hom_{S′}(T_{S′} ×_{S′} T_{S′}, G_{S′})
```

is injective. One deduces immediately that $u$ is a morphism of groups, since this is so of $u'$. Moreover $u$ is a
monomorphism. Indeed, note first that `Ker u` is flat over $S$, since to establish this fact one may assume $S$ artinian
local (EGA 0_III 10.2.2), hence $G$ separated (Exp. VI_A 0.3); but then `Ker u` is of multiplicative type (Exp. IX 6.8),
hence is flat over $S$. Since $Ker(u) \times_{S} S' = Ker(u') = 0$, one has $Ker(u) = 0$ (3.8). But $u$ being a
monomorphism is an immersion (Exp. VIII, remarks 7.13), and the image group $u(T)$ is indeed an element of $M(S)$ whose
image in $M(S')$ is $T'$. This completes the proof of 3.7.

**e) End of the proof of I).**

<!-- original page 392 -->

We are reduced by reduction c) to the case where $S$ is the spectrum of a complete reduced noetherian local ring $A$.
Let $S'$ be the spectrum of the normalization $A'$ of $A$, which is finite over $A$ by Nagata (EGA 0_IV 23.1.5); $S' \to
S$ is an epimorphism since $A$ embeds injectively into $A'$. Suppose then that there exists a torus $T'$ of $G_{S'}$
having $E_{S'}$ as underlying space. The two inverse images of $T'$ in $G_{S' \times_{S} S'}$ are two central sub-tori
with the same underlying space, so they coincide (Exp. IX 5 bis); hence, by 3.7, $T'$ comes from a central sub-torus $T$
of `G_S` which evidently has $E$ as underlying space. It therefore suffices to prove the existence of $T'$, which
reduces us to the case where $S$ is normal and completes the proof of I).

**II) Proof of (iii) ⇒ (ii) when $S$ is normal.**

We may restrict to the case where $S$ is integral; let $t$ be its generic point. For every integer $n$ equal to a power
of $q$, let ${}_{n}G$ be the subprescheme of $G$ "kernel" of the $n$-th power morphism in $G$. Since $E$ is locally
closed in $G$ (by (iii) b)), the intersection of $ens({}_{n}G)$ with $E$ is locally closed in $ens(G)$; let us then
denote by $E(n)$ the reduced subprescheme of $G$ having $ens({}_{n}G) \cap E$ as underlying space.

Let us show that the structural morphism $E(n) \to S$ is separated and universally open. For these two properties we
have a valuative criterion (EGA II 7.2.3 and

<!-- original page 393 -->

EGA IV 14.5.8). Let then $S'$ be an $S$-scheme which is the spectrum of a complete discrete valuation ring with
algebraically closed residue field. We have shown that 3.1 (iii) ⇒ 3.1 (iv), so there exists a sub-torus $T'$ of
$G_{S'}$ having $E_{S'}$ as underlying space. Now ${}_{n}T'$ is finite and étale over $S'$, hence separated and
universally open over $S'$, and the same is true of $E(n) \times_{S} S'$, which has the same underlying space as
${}_{n}T'$.

Moreover, the fibers of $E(n)$ have the same number of geometric points, namely $r^{n}$ if $r$ is the rank of the torus
$T_{t}$. Finally, the generic fiber $E(n)_{t}$, being reduced, is equal to ${}_{n}T_{t}$, hence is étale over
$\operatorname{Spec}(t)$. Since $S$ is normal, it then follows from SGA I 10.11 that $E(n)$ is an étale covering of $S$.

If $s$ is a point of $S$, $E(n)_{s}$ is étale over $\operatorname{Spec} \kappa(s)$, hence reduced, and consequently
coincides with the group of multiplicative type ${}_{n}T_{s}$. Let us show that $E(n)$ is a subgroup prescheme of $G$.
Indeed, let $m$ be the morphism

```text
E(n) ×_S E(n) ⟶ G
```

induced by the multiplication in $G$. The underlying map $ens(m)$ factors through $E(n)$, so $m$ factors through the
prescheme $E(n)$, since its source $E(n) \times_{S} E(n)$ is étale over $S$, hence reduced. It then follows from Exp. X
4.8 a) that $E(n)$ is a subgroup of multiplicative type. As already noted (3.2 a)), the family of subgroups $E(n)$ is
necessarily coherent. We have therefore proved that (iii) ⇒ (ii) when $S$ is normal.

<!-- original page 394 -->

**III) Proof of (ii) ⇒ (i).**

In fact we shall show that there exists a unique sub-torus $T$ of $G$ with underlying space equal to $E$ and such that
${}_{n}T = M_{n}$ for every $n$ equal to a power of $q$. The uniqueness of $T$ follows simply from Exp. IX 4.8 b). To
establish the existence of $T$, in view of uniqueness, we may successively assume:

a) $S$ is noetherian.

b) The $M_{n}$ are central subgroups. Indeed, it suffices to replace $G$ by $Z_{n} = Centr_{G}(M_{n})$ for $n$ large
enough (2.5 and 2.5 bis).

c) $S$ is the spectrum of a local ring. Suppose indeed the problem solved after every base change
$\operatorname{Spec}(\mathcal{O}_{S, s}) \to S$ where $s$ ranges over the points of $S$. Let $T_{s}$ be the sub-torus of
$G \times_{S} \operatorname{Spec}(\mathcal{O}_{S, s})$ thus obtained. For every $s$ there then exist an open
neighborhood $U$ of $s$ and a sub-torus $T$ of $G|U$ extending $T_{s}$ (Exp. VI_B § 10 and 3.6). We have shown that 3.1
(ii) ⇒ 3.1 (iv); since $S$ is noetherian, $E$ is therefore constructible (3.3). Consequently, possibly restricting $U$,
we may assume that $ens(T) = E \times_{S} U$ (EGA IV 9.5.2). But then, for every integer $n$ equal to a power of $q$,
${}_{n}T$ and $M_{n} \times_{S} U$ are two subgroups of multiplicative type of $G|U$ with the same fibers, hence which
coincide, $M_{n}$ being central (Exp. IX 5.3 bis). In short, with the hypotheses made, there exists a solution locally
on $S$, hence by uniqueness, there exists a global solution.

<!-- original page 395 -->

d) $S$ is the spectrum of a complete noetherian local ring, and if $s$ is the closed point, $T_{s}$ is trivial. This
follows from EGA 0_III 10.3.1 and from fpqc descent.

e) $S$ is reduced. One applies 2.2.

f) $S$ is normal. One applies Nagata's finiteness theorem (EGA 0_IV 23.1.5) and Lemma 3.7 in the case of central
sub-tori.

These reductions being made, since $T_{s}$ is trivial, $(M_{n})_{s}$ is trivial, so $M_{n}$ is trivial (Exp. X 3.3). If
$t$ is a point of $S$, the subgroups ${}_{n}T_{t}$ of $T_{t}$ are therefore trivial for every $n$ equal to a power of
$q$, and it follows easily from Exp. X 1.4 that $T_{t}$ itself is trivial. It then suffices to prove the lemma:

**Lemma 3.10.** *Under the hypotheses of 3.1 (ii), suppose in addition that $S$ is noetherian and normal and that for
every point $s$ of $S$, $T_{s}$ is a trivial torus. Then there exists a unique sub-torus $T$ of $G$ with underlying
space equal to $E$, such that ${}_{n}T = M_{n}$ for every $n$ equal to a power of $q$. Moreover $T$ is trivial.*

<!-- label: III.XV.3.10 -->

The uniqueness of $T$ follows from the fact that $T$, being smooth over $S$, is reduced. To prove the existence, we may
assume $S$ irreducible with generic point $\eta$. Let $r$ be the rank of $T_{\eta}$, $T^{0} = G^{r}_{m, S}$, $u_{\eta}$
an isomorphism of $T^{0}_{\eta}$ onto $T_{\eta}$, ${}_{n}u_{\eta}$ the restriction of $u_{\eta}$ to
${}_{n}T^{0}_{\eta}$. Since ${}_{n}T^{0}$ and $M_{n}$ are trivial, there exists a unique extension ${}_{n}u$ of
${}_{n}u_{\eta}$ to an $S$-isomorphism of ${}_{n}T^{0}$ onto $M_{n}$. I claim that for every point $s$ of $S$ there
exists a group isomorphism, necessarily unique:

$$ u_{s} : T^{0}_{s} \xrightarrow{\sim} T_{s} $$

extending ${}_{n}u_{s}$ for every $n$ equal to a power of $q$. Indeed, let $S_{1}$ be an $S$-scheme,

<!-- original page 396 -->

spectrum of a complete discrete valuation ring with algebraically closed residue field, whose generic point $t_{1}$
projects onto $\eta$ and whose closed point $s_{1}$ projects onto $s$ (EGA II 7.1.9). It follows from the proof of 3.1
(ii) ⇒ 3.1 (iv) that there exists a sub-torus $T_{1}$ of $G_{S_{1}}$ such that $(M_{n})_{S_{1}} = {}_{n}T_{1}$ for every
$n$ equal to a power of $q$. Since $S_{1}$ is normal, $T_{1}$ is isotrivial (Exp. X 5.16), and it follows from the
classification of isotrivial tori (Exp. X 1.2) and from SGA 1 V 8.2 that $T_{1}$, having trivial generic fiber, is
trivial. One may therefore extend the isomorphism $u_{\eta} \times_{\eta} t_{1}$ to an $S_{1}$-isomorphism of group
schemes

```text
u₁ : T⁰ ×_S S₁ ⥲ T₁.
```

The restriction of $u_{1}$ to ${}_{n}T^{0} \times_{S} S_{1}$ on the one hand, and ${}_{n}u \times_{S} S_{1}$ on the
other, coincide on the generic fiber by construction, hence coincide. The restriction $u_{1, s_{1}}$ of $u_{1}$ to the
closed fiber thus realizes the desired extension after the residue field extension $\kappa(s) \to \kappa(s_{1})$. It
then follows from Exp. IX 4.8 a) and from fpqc descent that $u_{1, s_{1}}$ descends to $\kappa(s)$ to a group
isomorphism $u_{s} : T^{0}_{s} \xrightarrow{\sim} T_{s}$ answering the question.

Moreover, $T^{0}$ is smooth over $S$ which is normal, hence is normal. It then follows from an easy extension criterion
for rational maps (EGA IV4 20.4.6) that for the existence of an $S$-morphism $u : T^{0} \to G$ whose restriction to
$T^{0}_{s}$, for every point $s$ of $S$, is the composite morphism

```text
T⁰ₛ ──uₛ──→ Tₛ ⟶ Gₛ,
```

it is necessary and sufficient that this be the case after every base change $S_{1} \to S$ where $S_{1}$ is the spectrum

<!-- original page 397 -->

of a complete discrete valuation ring with algebraically closed residue field.

Now in the present case, a reasoning analogous to the one just made shows that the extension condition is indeed
satisfied. Let $u$ denote the $S$-morphism $T^{0} \to G$ thus obtained.

Let us show that $u$ is indeed a morphism of groups. Let $m_{T^{0}}$ (resp. $m_{G}$) be the morphism defining the
multiplication in $T^{0}$ (resp. $G$). We must verify that $m_{G} \circ (u \times_{S} u) = u \circ m_{T^{0}}$. Now the
subprescheme of coincidences of these two morphisms is a subprescheme of $T^{0} \times_{S} T^{0}$, which majorizes the
fibers (since $u_{s}$ is a group morphism), so has the same underlying space as $T^{0} \times_{S} T^{0}$, hence is equal
to it, since $T^{0} \times_{S} T^{0}$ is smooth over $S$, hence reduced.

Finally, note that $u$ is a monomorphism (since this is so on the fibers), hence is an immersion (Exp. VIII 7.9). The
image of $T^{0}$ by $u$ is then a sub-torus of $G$ having $E$ as underlying set.

This completes the proof of Theorem 3.1.

## 4. Characterization of a sub-torus $T$ by the subgroups ${}_{n}T$

<!-- label: III.XV.4 -->

<!-- original page 398 -->

### 4.1. Statement of the main theorem

<!-- label: III.XV.4.statement -->

**Theorem 4.1.** *Let $S$ be a locally noetherian connected prescheme, $G$ an $S$-prescheme in groups of finite type
over $S$, $q$ an integer `> 1` invertible on $S$, $r$ a positive integer. For every integer $n$ equal to a power of $q$,
let $M(n)$ be a subgroup scheme of $G$, of multiplicative type and of type $(\mathbb{Z}/n\mathbb{Z})^{r}$. Suppose:*

- *a) The family of subgroups $M(n)$ is coherent, that is, if the integer $m$ divides $n$, one has*

$$ {}_{m}M(n) = M(m). $$

- *b) There exists a point $s$ of $S$ and a sub-torus $T_{s}$ of $G_{s}$ such that*

```text
M(n)ₛ = ₙTₛ    for every n.
```

- *c) For every point $t$ of $S$, there exists a closed affine subscheme $F_{t}$ of $G_{t}$ majorizing $M(n)_{t}$ for
  every $n$.*

*Then there exists one and only one sub-torus $T$ of $G$ such that ${}_{n}T = M(n)$ for every $n$ equal to a power of
$q$.*

<!-- label: III.XV.4.1 -->

One has an analogous theorem concerning the lifting of morphisms:

**Theorem 4.1 bis.** *Let $S$, $G$ and $q$ be as above, $T$ an $S$-torus, and for every integer $n$ equal to a power of
$q$, let $u(n)$ be an $S$-group morphism ${}_{n}T \to G$. Suppose:*

- *a) The family of morphisms $u(n)$ is coherent, i.e., if $m$ divides $n$, one has*

<!-- original page 399 -->

$$ u(m) = u(n)|_{{}_{m}T}. $$

- *b) There exists a point $s$ of $S$ and a group morphism $u_{s} : T_{s} \to G_{s}$ such that $u_{s}|_{{}_{n}T_{s}} =
  u(n)_{s}$ for every $n$ equal to a power of $q$.*
- *c) For every point $t$ of $S$, there exists a closed affine subscheme $F_{t}$ of $G_{t}$ majorizing
  $u(n)_{t}({}_{n}T_{t})$ for every $n$.*

*Then there exists a unique group morphism $u : T \to G$ such that for every $n$ equal to a power of $q$, the
restriction of $u$ to ${}_{n}T$ is equal to $u(n)$.*

<!-- label: III.XV.4.1bis -->

**Remark 4.2.** Using the lower semicontinuity of the abelian rank of a flat group prescheme of finite type over the
spectrum of a discrete valuation ring (cf. Exp. X 8.7), one can, in the statements of 4.1 and 4.1 bis, weaken condition
c) by simply requiring that the required closed affine subscheme $F_{t}$ exists for every maximal point $t$ of $S$.

<!-- label: III.XV.4.2 -->

Let us show how 4.1 bis follows from 4.1. Let $G' = G \times_{S} T$. For every integer $n$ equal to a power of $q$,
consider the group morphism

$$ v(n) : {}_{n}T \longrightarrow G' $$

whose projections to $G$ and $T$ are respectively $u(n)$ and the canonical immersion ${}_{n}T \to T$. The morphism
$v(n)$ is therefore an immersion; let $M(n)$ be the image subgroup. It is clear that the family of subgroups $M(n)$ is
coherent in the sense of 4.1, that the group $M(n)_{s}$ is equal to

<!-- original page 400 -->

${}_{n}T'_{s}$, where $T'_{s}$ is the sub-torus of $G'_{s}$ which is the graph of $u_{s}$, and that for every point $t$
of $S$, the closed affine subscheme $F_{t} \times_{t} T_{t}$ of $G'_{t}$ majorizes the subgroups $M(n)_{t}$ for every
$n$. By 4.1, there therefore exists a sub-torus $T'$ of $G'$ such that ${}_{n}T' = M(n)$ for every $n$ equal to a power
of $q$. Let $f$ be the restriction to $T'$ of the projection of $G'$ to $T$, and $f(n)$ the restriction of $f$ to
$M(n)$. One has

$$ f(n) \circ v(n) = id_{{}_{n}T}. $$

The fiber at $s$ of $T'$ is the torus already denoted $T'_{s}$, equal to the graph of $u_{s}$ (this follows from Exp. IX
4.8 b)), so $f_{s}$ is an isomorphism. But `Ker f` and `Coker f` are groups of multiplicative type (Exp. IX 2.7) of
constant type, $S$ being connected, hence reduced to the unit group, and $f$ is an isomorphism. Let $v$ be the inverse
isomorphism of $f$. One has

$$ v|_{{}_{n}T} = v(n). $$

Consequently, the composite of $v$ and the projection of $G'$ onto $G$ is a morphism $u : T \to G$ answering the
question. The foregoing proves the existence of the morphism $u$; as for uniqueness, it follows in any case from Exp. IX
4.8 a).

### 4.2. Application

<!-- label: III.XV.4.app -->

We propose to generalize Theorem 7.1 of Exp. IX.

Let $A$ be a complete noetherian local ring, $I$ its maximal ideal,

<!-- original page 401 -->

$S = \operatorname{Spec} A$, $S_{m} = \operatorname{Spec}(A/I^{m})$. For every prescheme $X$, set $X_{m} = X \times_{S}
S_{m}$.

Let then $G$ be an $S$-prescheme in groups of finite type, $T$ an $S$-torus, $q$ an integer invertible on $S$, and
$u_{m} : T_{m} \to G_{m}$ ($m \in \mathbb{N}$) a coherent family of group morphisms. With $n$ ranging over the powers of
$q$, denote by $u_{m}(n)$ the restriction of $u_{m}$ to ${}_{n}T_{m}$, and by $u(n)$ the unique group morphism

$$ u(n) : {}_{n}T \longrightarrow G $$

extending the morphisms $u_{m}(n)$ for every $m$ (1.6 a)). We shall say that the family $(u_{m})$, $m \in \mathbb{N}$,
is *admissible* if for every point $t$ of $S$ there exists a closed affine subprescheme $F_{t}$ of $G_{t}$ majorizing
$u(n)_{t}({}_{n}T_{t})$ for every $n$ equal to a power of $q$ (this property is independent of $q$, as we shall see).

**Proposition 4.3.** *With the notation above, the canonical map*

```text
Hom_{S-gr}(T, G) ⟶ lim_{←m} Hom_{S_m-gr}(T_m, G_m)
```

*induces an isomorphism of the source onto the subset of the target consisting of "admissible" coherent families.*

<!-- label: III.XV.4.3 -->

Indeed, it suffices to apply 4.1 bis, taking for $s$ the closed point of $S$.

**Corollary 4.4.** *With the notation above, suppose in addition that $G$ has affine fibers; then the canonical map*

```text
Hom_{S-gr}(T, G) ⟶ lim_{←m} Hom_{S_m-gr}(T_m, G_m)
```

*is an isomorphism.* <!-- original page 402 -->

<!-- label: III.XV.4.4 -->

Indeed, if $G$ has affine fibers, every coherent family is "admissible".

**Remark 4.5.** When $G$ is separated, one may in 4.3 replace the ring $A$ by an $I$-adic noetherian ring; one may
indeed use EGA III 5.4.1 instead of 1.6 a).

<!-- label: III.XV.4.5 -->

### 4.3. Proof of 4.1

<!-- label: III.XV.4.proof -->

**Lemma 4.6.** *Let $k$ be a field, $G$ a $k$-algebraic group, $q$ an integer prime to the residue characteristic of
$k$, $r$ an integer `> 0`, $M(n)$ ($n$ ranging over the powers of $q$) a coherent family of subgroups of $G$, of
multiplicative type and of type $(\mathbb{Z}/n\mathbb{Z})^{r}$. Then there exists a smallest closed subscheme $H$ of $G$
majorizing the $M(n)$ for every $n$. Moreover, $H$ is a smooth, connected and commutative algebraic subgroup of $G$
"whose formation is compatible with base field extension".*

<!-- label: III.XV.4.6 -->

Let $M$ be the subset of $ens(G)$ which is the union of the underlying sets of the subgroups $M(n)$ for every $n$, and
$H$ the reduced closed subscheme of $G$ having the closure of $M$ as underlying space. Since $M(n)$ is étale over $k$
hence reduced, $M(n)$ is contained in $H$, and consequently $H$ is the smallest closed subscheme of $G$ majorizing
$M(n)$ for every $n$. Now let $\bar{k}$ be an algebraically closed extension of $k$. By

<!-- original page 403 -->

construction the subschemes $M(n)$ are schematically dense in $H$ (Exp. IX 4.1); the $M(n)_{\bar{k}}$ are therefore
schematically dense in $H_{\bar{k}}$ (Exp. IX 4.5); moreover $M(n)_{\bar{k}}$ is reduced, and it follows that
$H_{\bar{k}}$ is necessarily equal to the closed reduced subscheme of $G_{\bar{k}}$ having as underlying space the
closure of $M_{\bar{k}}$. This proves that $H$ is geometrically reduced (EGA IV 4.6.1). The family $M(n)$ being
coherent, $M$ is stable under the group law; moreover $M \times_{k} M$ is dense in $ens(H \times_{k} H)$ and $H
\times_{k} H$ is reduced (EGA IV 4.6.5); one immediately deduces that $H$ is an algebraic subgroup of $G$. Moreover $H$
is smooth over $S$, since it is geometrically reduced (Exp. VI_A 1.3.1), and $H$ is commutative since the $M(n)$ are
commutative. It remains to see that $H$ is connected. Let $H^{0}$ be the connected component of $H$, $m$ the number of
geometric points of $H/H^{0}$, $q^{s}$ the exponent of $q$ in the decomposition of $m$ into prime factors. For every
integer $n$ equal to a power of $q$, ${}_{q^{s}} M(n)$ is then contained in $H^{0}$. But the family $M(n)$ is coherent
and $M(n)$ is of type $(\mathbb{Z}/n\mathbb{Z})^{r}$, so ${}_{q^{s}} M(nq^{s}) = M(n)$. Hence $H^{0}$ majorizes $M(n)$
for every $n$ and consequently equals $H$.

This being so, we shall make condition c) of 4.1 more precise. Indeed, by what precedes, we may consider the smallest
closed subscheme $H_{t}$ of $G_{t}$ majorizing $M(n)_{t}$ for every $n$. The formation of $H_{t}$ commuting with base
field extension (4.6), $H_{t} \otimes_{t} \bar{t}$ is contained in the affine closed subset $F_{t}$, hence is affine. In
short, $H_{t}$ is affine. On the other hand, we know (4.6) that $H_{t}$ is a smooth, connected, commutative algebraic
group. It then follows from the structure of smooth, commutative, connected affine algebraic groups over an
algebraically closed field (*Bible* 4 Th. 4),

<!-- original page 404 -->

that $H_{t}$ is a direct product of a torus $T_{t}$ and a unipotent group $U_{t}$. But then $M(n)_{t}$ is necessarily
contained in $T_{t}$, so $H_{t} = T_{t}$, and consequently $H_{t}$ is a torus.

We can now begin the proof of 4.1.

a) **Uniqueness of the solution:** it suffices to apply Exp. IX 4.8 b).

b) **Case where $S$ is the spectrum of a complete discrete valuation ring $A$ with algebraically closed residue field
$k$.** Denote by $K$ the field of fractions of $A$, $s$ the closed point of $S$, $t$ the generic point, $J$ the maximal
ideal of $A$, $S_{m} = \operatorname{Spec}(A/J^{m})$, $X_{m} = X \times_{S} S_{m}$.

Let us distinguish two cases:

**1st case: The point $s$ of 4.1 b) is the generic point $t$ of $S$.** Let then $T'$ be the schematic closure in $G$ of
the torus $T_{t}$. The closed fiber $T'_{s}$ is therefore an algebraic subgroup of $G_{s}$, of dimension $r$, majorizing
$M(n)_{s}$ for every $n$, hence $T'_{s}$ majorizes $H_{s}$. But $H_{s}$ is a torus containing $M(n)_{s}$, so $H_{s}$ has
rank at least $r$. Consequently $H_{s}$ has the same underlying space as the connected component of $T'_{s}$. The
"connected component" $(T')^{0}$ of $T'$ is then a subgroup prescheme of $G$, flat, separated (VI_B 5.2), whose generic
fiber $T_{t}$ is a torus and whose reduced closed fiber $H_{s}$ is a torus. But then $(T')^{0}$ is a torus (Exp. X 8.8)
which we denote by $T$. The groups ${}_{n}T$ and $M_{n}$ are smooth over $S$, hence reduced, and since they have the
same underlying space, they coincide. So the torus $T$ is the solution of the problem.

**2nd case: The point $s$ of 4.1 b) is the closed point $s$ of $S$.** Possibly replacing $G$ by

<!-- original page 405 -->

the schematic closure in $G$ of the smallest algebraic subgroup $H_{t}$ majorizing the family $M(n)_{t}$ (4.6), we may
assume $G_{t}$ affine.

For every integer $m \geqslant 0$, it follows from 2.2 that there exists a unique sub-torus $T_{m}$ of $G_{m}$ lifting
$T_{s}$ and such that for every integer $n$ equal to a power of $q$, one has ${}_{n}T_{m} = M(n)_{m}$. Moreover, let
$T^{0} = G^{r}_{m, S}$. Since $k$ is algebraically closed, $T_{s}$ is trivial, and there exists a $k$-isomorphism
$u_{s} : T^{0}_{s} \xrightarrow{\sim} T_{s}$. The morphism $u_{s}$ lifts uniquely to an $S_{m}$-isomorphism
$u_{m} : T^{0}_{m} \to T_{m}$ (Exp. IX 3.3). The family of morphisms $u_{m}$, $m \in \mathbb{N}$, defines in the limit a
morphism `û` of formal completions $\hat{T}^{0}$ and `Ĝ` of $T^{0}$ and $G$ along their closed fibers:

```text
T̂⁰ ──û──→ Ĝ
│            │
i            j
▼            ▼
T⁰           G,
```

where $i$ and $j$ denote the canonical morphisms.

We shall show that the morphism `û` is algebraizable. For this we shall reduce to the case where the group $G$ is
affine.

**Lemma 4.7.** *Let $S$ be the spectrum of a discrete valuation ring $A$, $X$ and $Y$ two $S$-preschemes, quasi-compact,
quasi-separated and flat over $S$. Then the canonical map*

```text
Γ(X, 𝒪_X) ⊗_A Γ(Y, 𝒪_Y) ⟶ Γ(X ×_S Y, 𝒪_{X ×_S Y})
```

*is an isomorphism.*

<!-- label: III.XV.4.7 -->

Let $f : X \to S$ (resp. $g : Y \to S$) be the structural morphism. Since $X$ (resp. $Y$)

<!-- original page 406 -->

is quasi-compact and quasi-separated, it follows from EGA I 9.2.2 and from EGA IV 1.7.4 that $f_{*}(\mathcal{O}_{X})$
(resp. $g_{*}(\mathcal{O}_{Y})$) is a quasi-coherent $\mathcal{O}_{S}$-algebra, which therefore corresponds to an affine
$S$-scheme $\tilde{X}$ (resp. `Ỹ`). By hypothesis $Y$ is flat over $S$; it then follows from EGA III 1.4.15, in view of
EGA IV 1.7.21, that the canonical map (deduced from the canonical morphism $X \to \tilde{X}$)

```text
Γ(X̃ ×_S Y, 𝒪_{X̃ ×_S Y}) ⟶ Γ(X ×_S Y, 𝒪_{X ×_S Y})
```

is an isomorphism. But $X$ being flat over $S$, $\tilde{X}$ is flat over $S$ (since flat over $A$ is equivalent to
torsion-free). Applying once again EGA III 1.4.15 with the roles of $X$ and $Y$ exchanged, one obtains an isomorphism

```text
Γ(X̃, 𝒪_{X̃}) ⊗_A Γ(Ỹ, 𝒪_{Ỹ}) ≃ Γ(X̃ ×_S Ỹ, 𝒪_{X̃ ×_S Ỹ}) ⥲ Γ(X̃ ×_S Y, 𝒪_{X̃ ×_S Y}),
```

whence the lemma.

In the present case, the $S$-group $G$ is flat over $S$ and of finite type, hence quasi-compact and quasi-separated. One
may therefore apply the lemma to $G \times_{S} G$:

```text
Γ(G, 𝒪_G) ⊗_A Γ(G, 𝒪_G) ⥲ Γ(G ×_S G, 𝒪_{G ×_S G}).
```

To the morphism $m_{G} : G \times_{S} G \to G$ defining the multiplication in $G$ there corresponds therefore a morphism

```text
Γ(G, 𝒪_G) ⟶ Γ(G ×_S G, 𝒪_{G ×_S G}) ⥲ Γ(G, 𝒪_G) ⊗_A Γ(G, 𝒪_G),
```

hence an $S$-morphism

```text
m_{G̃} : G̃ ×_S G̃ ⟶ G̃,
```

<!-- original page 407 -->

where $\tilde{G}$ denotes the affine $S$-scheme having $\Gamma(G, \mathcal{O}_{G})$ as $A$-algebra. It is formal, from
there, to verify that $m_{\tilde{G}}$ endows $\tilde{G}$ with a structure of $S$-group scheme such that the canonical
morphism $v : G \to \tilde{G}$ is an $S$-group morphism.

**Remark 4.8.** $\tilde{G}$ plays the role of a largest "affine quotient" of $G$; moreover one can show that $\tilde{G}$
is indeed a quotient of $G$ for fpqc, hence is of finite type over $S$ (XVII App. III, 2).

<!-- label: III.XV.4.8 -->

In the case at hand, the generic fiber $G_{t}$ of $G$ is affine; it then follows from EGA I 9.3.3 that $v_{t}$ is an
isomorphism. Since $\tilde{G}$ is affine, the coherent family of morphisms

```text
w_m = v_m u_m : T⁰_m ⟶ G̃_m    (m ∈ ℕ)
```

comes from a unique $S$-group morphism (Exp. IX 7.1)

$$ w : T^{0} \longrightarrow \tilde{G}. $$

Let $T_{t}$ be the sub-torus of $G_{t}$ equal to $v^{-1}_{t} w_{t}(T^{0}_{t})$. The torus $T_{t}$ is therefore of rank
at most $r$ (as the image of a torus of rank $r$). Let us show that $T_{t}$ majorizes $M(n)_{t}$ for every $n$. Indeed,
let $u(n)_{m}$ be the $S_{m}$-isomorphism $({}_{n}T^{0})_{m} \xrightarrow{\sim} M(n)_{m}$ obtained by restriction of
$u_{m}$ to $({}_{n}T^{0})_{m}$. The coherent family of morphisms $u(n)_{m}$ comes from a unique $S$-isomorphism $u(n) :
{}_{n}T^{0} \xrightarrow{\sim} M(n)$ (since $M(n)$ is finite over $S$). For every integer $m \geqslant 0$, one then has
the equalities

```text
w_m|_{(ₙT⁰)_m} = (v_m u_m)|_{(ₙT⁰)_m} = (v ∘ u(n))_m.
```

Consequently, $w|_{{}_{n}T^{0}} = v \circ u(n)$ (1.6 a)). In particular, one has $w_{t}|_{({}_{n}T^{0})_{t}} = v_{t}
\circ u(n)_{t}$, so $v^{-1}_{t} w_{t} ({}_{n}T^{0})_{t} = u(n)_{t} ({}_{n}T^{0})_{t} = M(n)_{t}$.

This indeed proves that $T_{t}$ majorizes $M(n)_{t}$, and entails that $T_{t}$ is of rank $r$. One concludes

<!-- original page 408 -->

as in the first case already studied, by considering the schematic closure in $G$ of $T_{t}$, namely $T''$. Since
$T_{t}$ majorizes $M(n)_{t}$, $T''_{s}$ majorizes $M(n)_{s}$, hence majorizes $T_{s}$ (density theorem). On the other
hand $T''$ is flat over $S$ and $T_{t}$ is of dimension $r$, so $T''_{s}$ is of dimension $r$ (Exp. VI_B 4). In short,
$T_{s}$ has the same underlying space as the connected component of $T''_{s}$, and one concludes as in the first case
that the connected component of $T''$ is a sub-torus of $G$ answering the question.

c) **End of the proof of 4.1.**

To prove the existence of the sub-torus $T$, we may assume $S$ reduced (2.2). In view of 3.1 (ii) ⇒ (i), it then
suffices to prove that the set $U$ of points $x$ of $S$ such that there exists a sub-torus $T_{x}$ of $G_{x}$ with
${}_{n}T_{x} = M(n)_{x}$ for every $n$ equal to a power of $q$, is equal to $ens(S)$. The torus $T_{x}$ in question is
necessarily unique, and by fpqc descent, it suffices to prove its existence after extension of the residue field of $x$
(Exp. IX 4.8 b)).

This being so, since $S$ is locally noetherian and connected and since $U$ is non-empty (it contains the point $s$ of
4.1 b)), one is reduced, by an immediate argument, to proving that if $x$ and $x'$ are two points of $S$, with $x$ a
specialization of $x'$, and if one of the two points belongs to $U$, then both points are in $U$. By the usual technique
(EGA II 7.1.9) one reduces to the case where $S$ is the spectrum of a complete discrete valuation ring with
algebraically closed residue field, a case which has been treated in b).

This completes the proof of Theorem 4.1.

## 5. Representability of the functor of smooth subgroups identical to their connected normalizer

<!-- label: III.XV.5 -->

<!-- original page 409 -->

**Proposition 5.1.** *Let $S$ be a prescheme, $G$ an $S$-prescheme in groups of finite presentation, $H$ a subgroup
prescheme of $G$, smooth with connected fibers. Then:*

- *a) The normalizer $N$ of $H$ in $G$ is representable by a closed subprescheme of $G$ of finite presentation over
  $S$.*
- *b) The following conditions are equivalent:*
    - *i) The canonical immersion $H \to N$ is an open immersion.*
    - *ii) The group $N$ is smooth along the unit section, and its connected component, which is then representable
      (Exp. VI_B 3.10), is equal to $H$.*
    - *iii) For every point $s$ of $S$, one has $H_{s} = (N_{s})^{0}$.*

<!-- label: III.XV.5.1 -->

*Proof.* The group prescheme $H$ is locally of finite presentation over $S$ ($H$ is smooth over $S$) and has connected
fibers, hence is of finite presentation over $S$ (Exp. VI_B 5.3.3). Assertion a) is then a consequence of Exp. XI 6.11.
The equivalence of the conditions appearing in b) is included here for the record and was proved in VI_B 6.5.1.

This being so, we can state the main theorem of this section:

<!-- original page 410 -->

**Theorem 5.2.** *Let $S$ be a prescheme, $G$ an $S$-prescheme in groups of finite presentation over $S$,
$\mathcal{L}_{G}$ (or simply $\mathcal{L}$ if there is no ambiguity) the $S$-functor such that for every $S$-prescheme
$S'$ one has:*

> *$\mathcal{L}_{G}(S')$ = set of subgroup preschemes of $G_{S'}$, smooth over $S'$, with connected fibers, which are
> identical to their connected normalizer.*

*Then the functor $\mathcal{L}$ is representable by an $S$-prescheme, a union of an increasing family $(U_{i})_{i \in
\mathbb{N}}$ of open subpreschemes, quasi-projective and of finite presentation over $S$, hence a fortiori separated
over $S$.*

<!-- label: III.XV.5.2 -->

**Initial reductions.**

For every integer $r \geqslant 0$, let $\mathcal{L}^{r}$ be the subfunctor of $\mathcal{L}$ such that for every
$S$-prescheme $S'$ one has:

> *$\mathcal{L}^{r}(S')$ = set of subgroup preschemes of $G_{S'}$, smooth, with connected fibers, identical to their
> connected normalizer and of relative dimension $r$.*

Since the dimension of the fibers of a smooth group is a locally constant function, the canonical monomorphism
$\mathcal{L}^{r} \to \mathcal{L}$ is representable by an immersion both open and closed. It therefore suffices to show
that for every $r$, $\mathcal{L}^{r}$ is representable by an $S$-prescheme having the properties stated above, since
$\mathcal{L}$ will then be representable by the $S$-prescheme sum $\coprod_{r \in \mathbb{N}} \mathcal{L}^{r}$.

<!-- original page 411 -->

For every integer $n \geqslant 0$, every $S$-prescheme $S'$ and every subgroup prescheme $H$ of $G_{S'}$, we denote by
$H^{(n)}$ the $n$-th normal invariant of the unit section $S' \to H$ of $H$ (EGA IV 16.1.2), so that $H^{(n)}$ is a
sheaf of $\mathcal{O}_{S'}$-modules of finite type corresponding to the $n$-th infinitesimal neighborhood of the unit
section of $H$. If $H$ is smooth over $S'$ of relative dimension $r$, $H^{(n)}$ is a locally free
$\mathcal{O}_{S}$-module whose rank $\phi(n, r)$ depends only on $n$ and $r$. Moreover, since $H$ is a subprescheme of
$G_{S'}$, one has a canonical epimorphism, compatible with base extension:

```text
G^{(n)} ⊗_{𝒪_S} 𝒪_{S′} ≃ G_{S′}^{(n)} → H^{(n)}.
```

Introduce then the projective $S$-scheme

```text
P_{φ(n, r)} = Grass_{φ(n, r)}(G^{(n)})
```

(EGA I 2nd ed. 9.7; cf. also Séminaire Cartan 1960/61, Exp. N° 14 by A. Grothendieck). It then follows from the
preceding remarks that the map

$$ H \mapsto H^{(n)} $$

defines a canonical morphism

```text
u_{n, r} : ℒ^r ⟶ P_{φ(n, r)}.
```

The group $G$ acts in a natural way on $G^{(n)}$, hence on $P_{\phi(n, r)}$, by means of the representation

```text
int : G ⟶ Aut_{S-gr}(G),    g ↦ int(g).
```

Moreover, if $S'$ is a quasi-compact $S$-prescheme and $H$ an element of $\mathcal{L}^{r}(S')$, one knows

<!-- original page 412 -->

(Exp. XI 6.11) that for $n$ large enough,

$$ N = Norm_{G_{S'}}(H) = Norm_{G_{S'}}(H^{(n)}). $$

For each integer $n \geqslant 0$, introduce the subfunctor $\mathcal{L}^{r}_{n}$ of $\mathcal{L}^{r}$ such that for
every $S$-prescheme $S'$ one has:

> *$\mathcal{L}^{r}_{n}(S')$ = set of subgroups $H$ of $G_{S'}$ belonging to $\mathcal{L}^{r}(S')$ such that
> $Norm_{G_{S'}}(H) = Norm_{G_{S'}}(H^{(n)})$.*

**Representability of $\mathcal{L}^{r}_{n}$.**

Since the integer $r$ is fixed until the end of the proof of 5.2, we shall not repeat it in the notation. Thus we shall
write $\mathcal{L}$, $\mathcal{L}_{n}$, $P_{n}$, $u_{n}$ instead of $\mathcal{L}^{r}$, $\mathcal{L}^{r}_{n}$,
$P_{\phi(n, r)}$, $u_{n, r}$.

Let $v_{n}$ be the restriction of $u_{n}$ to the subfunctor $\mathcal{L}_{n}$ of $\mathcal{L}$. It follows from the
definition of $\mathcal{L}_{n}$ and from 5.1 b) ii) that $v_{n}$ is a monomorphism. In fact one has the following lemma:

**Lemma 5.3.** *The morphism $v_{n}$ is an immersion of finite presentation. A fortiori, $\mathcal{L}_{n}$ is
representable by an $S$-prescheme, quasi-projective and of finite presentation over $S$.*

<!-- label: III.XV.5.3 -->

Possibly replacing $S$ by $P_{n}$, we are reduced by the usual technique to proving the following assertion: Let $Q \in
P_{n}(S)$ and consider the subfunctor $F$ of the functor $h_{S}$ represented by the final object $S$ of $Sch/S$, such
that for every $S$-prescheme $S'$ one has:

<!-- original page 413 -->

- *$F(S') = h_{S}(S')$ (set with one element) if there exists $H \in \mathcal{L}_{n}(S')$ such that $H^{(n)} = Q_{S'}$,*
- *$F(S') = \emptyset$ otherwise.*

Then the canonical monomorphism $F \to S$ is an immersion of finite presentation.

Let us first transform the definition of the functor $F$. For this, note that the normalizer of $Q$ in $G$ is
representable by a subgroup prescheme $N$ of finite presentation over $S$ (namely the inverse image of the point $Q$ of
$P_{n}(S)$ under the morphism $G \to P_{n}$, $g \mapsto g \cdot Q$). I claim that the functor $F$ coincides with the
following subfunctor of $h_{S}$:

> *$F(S') = h_{S}(S')$ if:*
>
> - *(a) $N_{S'}$ is smooth along the unit section and of relative dimension $r$,*
> - *(b) $(N_{S'})^{(n)}$ (which is then canonically an element of $P_{n}(S')$) is equal to $Q_{S'}$.*
>
> *$F(S') = \emptyset$ otherwise.*

Indeed, denote temporarily by `F_1` the functor $F$ in the first formulation, and `F_2` the functor $F$ in the second
formulation. Then:

i) $F_{1}(S') = h_{S}(S') \Rightarrow F_{2}(S') = h_{S}(S')$.

<!-- original page 414 -->

Indeed, let $H \in \mathcal{L}_{n}(S')$ be the subgroup of $G_{S'}$ such that $H^{(n)} = Q_{S'}$. Then

```text
Norm_{G_{S′}}(H) = Norm_{G_{S′}}(H^{(n)}) = Norm_{G_{S′}}(Q_{S′}) = N_{S′}.
```

So by 5.1 b) ii), $N_{S'}$ is smooth along the unit section and its connected component is $H$. Consequently $N_{S'}$ is
of relative dimension $r$; and since $H$ is open in $N_{S'}$ (by 5.1 b) i)), one has $(N_{S'})^{(n)} = H^{(n)} =
Q_{S'}$. In short, $F_{2}(S') = h_{S}(S')$.

ii) $F_{2}(S') = h_{S}(S') \Rightarrow F_{1}(S') = h_{S}(S')$.

By hypothesis, $N_{S'}$ is smooth along the unit section, of relative dimension $r$; its connected component is then
representable (Exp. VI_B 3.10) by a subgroup prescheme $H$, smooth over $S'$, with connected fibers of dimension $r$.
Since $H$ is invariant in $N_{S'}$ and open in $N_{S'}$, one has the following inclusions:

```text
N_{S′} ⊂ Norm_{G_{S′}}(H) ⊂ Norm_{G_{S′}}(H^{(n)}) = Norm_{G_{S′}}((N_{S′})^{(n)}) = Norm_{G_{S′}}(Q_{S′}) = N_{S′}.
```

These inclusions are therefore equalities. The first inclusion then shows that $H$ is equal to its connected normalizer,
and the second shows that $H$ is an element of $\mathcal{L}_{n}(S')$. This says that $F_{1}(S') = h_{S}(S')$.

Implications i) and ii) entail $F_{1} = F_{2}$. We keep the second definition of the functor $F$, and we shall first
"represent condition a)" by an immersion of finite presentation. For this it suffices to apply the:

**Lemma 5.4.** *Let $S$ be a prescheme, $X$ an $S$-prescheme locally of finite presentation over $S$, $\sigma : S \to X$
a section of $X$, $r$ an integer $\geqslant 0$, and $L : (Sch/S)^{\circ} \to (Ens)$ the subfunctor of $S$ defined as
follows:*

<!-- original page 415 -->

- *$L(S') = h_{S}(S')$ if $X_{S'}$ is smooth along the section $\sigma_{S'}$ and of relative dimension $r$ at the points
  of $\sigma_{S'}(S')$.*
- *$L(S') = \emptyset$ otherwise.*

*Then:*

- *a) The monomorphism $L \to S$ is an immersion of finite presentation.*
- *b) Let $\mathcal{J}$ be the conormal sheaf relative to the immersion $S \to X$ (EGA IV 16.1.2); assume that for every
  point $s$ of $S$, $\mathcal{J} \otimes_{\mathcal{O}_{S, s}} \kappa(s)$ is of rank at most $r$. Then the immersion $L
  \to S$ is a closed immersion.*

<!-- label: III.XV.5.4 -->

*Proof.* The functor $L$ is of local nature on $S$, which reduces us to the case where $S$ is affine. Possibly replacing
$X$ by a neighborhood of $\sigma(S)$, we may assume $X$ of finite presentation over $S$, then (EGA IV 8.9) $S$
noetherian (noting, in case b), that the formation of the conormal sheaf commutes with base extension (EGA IV 16.6.4)
and that the rank of the fibers of $\mathcal{J}$ is a constructible function on $S$). This being so, for every
$S$-prescheme $S'$, denote $\mathcal{J}_{0} = \mathcal{J}_{S'}$ the conormal sheaf relative to the section
$\sigma_{S'}$, $S_{\bullet}(\mathcal{J}_{0})$ (canonically isomorphic to $S_{\bullet}(\mathcal{J})_{S'}$) the symmetric
algebra of $\mathcal{J}_{0}$ over $\mathcal{O}_{S'}$, $Gr_{\bullet}(\sigma_{S'})$ the sheaf of graded
$\mathcal{O}_{S'}$-algebras associated to $\sigma_{S'}$ (EGA IV 16), and for every integer $n \geqslant 0$ let
$\sigma_{n, S'} : S_{n}(\mathcal{J}_{0}) \to Gr_{n}(\sigma_{S'})$ be the canonical epimorphism.

It follows from EGA IV 17.12.3 and from EGA 0_IV 19.5.4 that, for $X_{S'}$ to be smooth along the section $\sigma_{S'}$
and of relative dimension $r$ at the points of $\sigma_{S'}(S')$,

<!-- original page 416 -->

it is necessary and sufficient that:

- i) $\mathcal{J}_{0}$ be a locally free $\mathcal{O}_{S'}$-sheaf of rank $r$.
- ii) For every integer $n \geqslant 1$, $\sigma_{n, S'}$ be an isomorphism.

Now it follows from TDTE IV, Lemma 3.6, that "the functor that makes $\mathcal{J}$ locally free of rank $r$" is
representable by a subprescheme `S_1`, closed in $S$ in case b). Replacing $S$ by `S_1`, we are reduced to the case
where $\mathcal{J}$ is locally free of rank $r$. Let us then proceed by induction on the integer $n$. Suppose that we
have represented by a closed subprescheme $S_{n-1}$ of $S$ the "functor that makes the morphisms $\sigma_{q, S'}$
injective for every integer $q \leqslant n - 1$", and let us show that the "subfunctor[^N.D.E-XV-5] that makes
$\sigma_{n, S'}$ injective" is representable by a closed subprescheme $S_{n}$ of $S_{n-1}$. Replacing $S$ by $S_{n-1}$,
we may assume that $\sigma_{q, S}$ is bijective for $q \leqslant n - 1$. But then the $(n - 1)$-st normal invariant
$X^{(n-1)}$ relative to the section $\sigma_{s}$ admits a composition series $X^{(0)}, \cdots, X^{(n-1)}$ whose
successive quotients $Gr_{0}(\sigma_{s}), \cdots, Gr_{n-1}(\sigma_{s})$ are locally free over $\mathcal{O}_{S'}$, hence
flat; so $X^{(n-1)}$ is flat over $\mathcal{O}_{S}$. Since the formation of $X^{(i)}$ commutes with base extension (EGA
IV 16), one has, for every $S$-prescheme $S'$:

```text
Gr_n(σ_{S′}) = Ker(X_{S′}^{(n)} → X_{S′}^{(n-1)}) = (Gr_n(σ))_{S′}    and    σ_{n, S′} = (σ_{n, S})_{S′}.
```

So the functor that interests us is "the one that makes the morphism $\sigma_{n, S}$ injective".

<!-- original page 417 -->

This functor is of local nature on $S$, which allows us to assume $S$ affine and $S_{n}(\mathcal{J})$ free over
$\mathcal{O}_{S}$. But then it is clear that the functor in question is representable by the closed subscheme of $S$
defined by the ideal generated by the coordinates of $Ker \sigma_{n, S}$ with respect to a basis of
$S_{n}(\mathcal{J})$.

Since $S$ is noetherian, the decreasing sequence ${S_{n}}$ of closed subpreschemes of `S_1` is stationary, and the
stationary value represents the functor $L$, which completes the proof of 5.4.

Let us return to the question of representability of $\mathcal{L}_{n}$. Replacing $S$ by a suitable subprescheme `S_1`,
we may therefore assume $N$ smooth along the unit section and of relative dimension $r$. The functor $\mathcal{L}_{n}$
is then the "functor of coincidences" of two sections of $P_{n}$ above $S$, $h$ and $g$, corresponding to the sheaves
$Q$ and $N^{(n)}$ (condition b) appearing in the definition of the functor `F_2` above). It is therefore representable
by the closed subprescheme of $S$, inverse image of the diagonal of $P_{n} \times_{S} P_{n}$ by the morphism of finite
presentation $h \times_{S} g$. This completes the proof of 5.3.

**Study of the transition morphisms $\mathcal{L}_{n} \to \mathcal{L}_{m}$.**

If a subgroup $H$ of $G_{S'}$ belongs to $\mathcal{L}_{n}(S')$, it belongs *a fortiori* to $\mathcal{L}_{m}(S')$ for
every $m \geqslant n$, whence natural monomorphisms

```text
u^m_n : ℒ_n ⟶ ℒ_m    for m ⩾ n.
```

**Lemma 5.5.** *The morphism $u^{m}_{n}$ is an open immersion.*

<!-- label: III.XV.5.5 -->

Possibly changing $S$, we are reduced to the following problem: Let $H \in \mathcal{L}_{m}(S)$,

```text
N = Norm_G(H) = Norm_G(H^{(m)}),    N′ = Norm_G(H^{(n)}),
```

and let $D : (Sch/S)^{\circ} \to (Ens)$ be the functor of coincidences of $N$ and $N'$, defined by $D(S') = h_{S}(S')$
if $N_{S'} = N'_{S'}$, and $D(S') = \emptyset$ otherwise. We must show that $D \to S$

<!-- original page 418 -->

is an open immersion. Now I claim that $D$ is also the subfunctor of $S$ which "makes the immersion $H \to N'$ open".
Indeed, if $N_{S'} = N'_{S'}$, then $H_{S'} \to N'_{S'}$ is indeed an open immersion since this is so for $H_{S'} \to
N_{S'}$ (Prop. 5.1). Conversely, if $H_{S'} \to N'_{S'}$ is an open immersion, $H$ having connected fibers, $H_{S'}$ is
the connected component of $N'_{S'}$ (Exp. VI_B 3.10) and consequently is invariant in $N'_{S'}$, so $N'_{S'} \subset
N_{S'}$. Since in any case $N'$ majorizes $N$, one has $N_{S'} = N'_{S'}$. The group preschemes $H$ and $N'$ are of
finite presentation over $S$ and $H$ is flat over $S$; the fact that $D \to S$ is an open immersion then follows from
Exp. VI_B 2.6.

**End of the proof of 5.2.**

The functors $\mathcal{L}_{n}$ being representable and the transition morphisms $u^{m}_{n}$ being compatible with one
another and representable by open immersions, there exists an $S$-prescheme $X$, union of an increasing sequence of open
subsets $(X_{i})_{i \in \mathbb{N}}$, such that `Xᵢ` represents the functor $\mathcal{L}_{i}$, and such that if one
identifies $\mathcal{L}_{i}$ with `Xᵢ`, the inclusion $X_{i} \to X_{j}$ ($j \geqslant i$) is identified with
$u^{j}_{i}$. To conclude that $X$ represents the functor $\mathcal{L}$, it then suffices to remark that in the category
of sheaves on $Sch/S$ equipped with the Zariski topology (Exp. IV 6.1) one has

<!-- original page 419 -->

```text
X = lim_{→} Xᵢ    and    ℒ = lim_{→} ℒ_i.
```

**Remark 5.6.** With the preceding notation, suppose in addition that $S$ has all residue characteristics zero. Then,
for every integer $r \geqslant 0$, the functor $\mathcal{L}^{r}$ is equal to $\mathcal{L}^{r}_{1}$, hence is
representable by an $S$-prescheme of finite presentation and quasi-projective over $S$. Indeed, it suffices to show that
if $H \in \mathcal{L}^{r}(S')$, the canonical immersion

$$ H \longrightarrow N = Norm_{G_{S'}}(H^{(1)}) $$

is an open immersion (since this entails $N = Norm_{G_{S'}}(H)$, hence $H \in \mathcal{L}^{r}_{1}(S')$). Since $H$ is
flat over $S$, and $H$ and $N$ are of finite presentation over $S$, it suffices (Exp. VI_B 2.6) to show that for every
point $s$ of $S$, $H_{s} \to N_{s}$ is an open immersion. Now it follows easily[^N.D.E-XV-6] from Cartier's theorem
(Exp. VI_B 1.6) that if $G$ is an algebraic group over a field of characteristic 0 and $H$ is a connected algebraic
subgroup, one has

```text
Norm_G(H) = Norm_G(Lie H) = Norm_G(H^{(1)}).
```

On the other hand, if $S$ has non-zero residue characteristics, the subfunctors $\mathcal{L}^{r}_{n}$ of
$\mathcal{L}^{r}$ may form a strictly increasing sequence (even when $S$ is quasi-compact) and in this case
$\mathcal{L}^{r}$ is not representable by an $S$-prescheme quasi-compact over $S$. Take for example the algebraic group
$G$, defined over a field $k$ of characteristic $p > 0$, equal to the semidirect product of the torus $T = G_{m} \times
G_{m}$ by the unipotent group $U = G_{a} \times G_{a}$, the action of $T$ on $U$ being defined by $(t, t', u, u') \to
(tu, t'u')$. For every integer $n > 0$, consider the smooth connected subgroup $U_{n}$ of $U$ of equation $u' =
u^{p^{n}}$, and the sub-torus $T_{n}$ of $T$ of equation $t' = t^{p^{n}}$. It is immediate to verify that $T_{n}$ acts
on $U_{n}$ and that the subgroup $G_{n}$ of $G$, equal to $T_{n} \cdot U_{n}$, is smooth, connected and equal to its
normalizer in $G$. Now all the groups $G_{n}$, for $n \geqslant m$, are distinct but have the same infinitesimal
neighborhood of order `pᵐ`.

<!-- label: III.XV.5.6 -->

**Remark 5.7.** There exists on $\mathcal{L}$ a canonical invertible sheaf $L$,

<!-- original page 420 -->

whose restriction to every open subset $U$ of $\mathcal{L}$ quasi-compact over $S$ is $S$-ample. Indeed, consider the
subgroup prescheme $H$ of $G_{\mathcal{L}}$ smooth over $\mathcal{L}$, with connected fibers, equal to its connected
normalizer and universal for these properties. I claim that one may take for $L$ the sheaf $(det(Lie H))^{-1}$ (recall
that if $\mathcal{F}$ is a sheaf of $\mathcal{O}_{S}$-modules on a prescheme $S$ that is locally free of finite rank,
$det(\mathcal{F})$ denotes the invertible $\mathcal{O}_{S}$-module whose restriction to the open-closed subprescheme
$S_{r}$ of $S$ ($r \geqslant 0$) where $\mathcal{F}$ is of rank $r$ is equal to $\bigwedge^{r}(\mathcal{F})$). We keep
the notation from the proof of 5.2. To prove the assertion made on $L$, we may restrict to the functor
$\mathcal{L}^{r}_{n}$ and prove that $L|_{\mathcal{L}^{r}_{n}}$ is $S$-ample. Consider the canonical immersion $v_{n} :
\mathcal{L}^{r}_{n} \to P_{n}$, and let $Q$ be the locally free sheaf on $P_{n}$ universal for the Grassmannian $P_{n}$.
By construction, one has $v^{*}_{n}(Q) = H^{(n)}$ (where now $H$ denotes the subgroup prescheme of
$G_{\mathcal{L}^{r}_{n}}$ universal for the functor $\mathcal{L}^{r}_{n}$). Now $det(Q)$ is the canonical ample sheaf on
$P_{n}$ (EGA I 2nd ed. 9.7), so $det H^{(n)}$ is ample relative to $\mathcal{L}^{r}_{n}$ (EGA II 4.6.13 i) bis). Let
$\mathcal{J}$ still denote the conormal sheaf, equal to $H^{(1)}$, and $S^{q}(\mathcal{J})$ the homogeneous part of
degree $q$ of the symmetric algebra of $\mathcal{J}$ over $\mathcal{O}_{\mathcal{L}^{r}_{n}}$. Since $H$ is smooth over
$\mathcal{L}^{r}_{n}$, it is immediate that one has a canonical isomorphism:

```text
det H^{(n)} ≃ ∏_{1 ⩽ q ⩽ n} det S^q(𝒥).
```

On the other hand, one proves that for every locally free sheaf $\mathcal{J}$ of rank $r$ and for every integer $q > 0$,
there exists a canonical isomorphism:

<!-- original page 421 -->

```text
det S^q(𝒥) ≃ (det 𝒥)^{⊗ s},
```

where $s > 0$ is an integer depending only on $r$ and $q$. Finally, one obtains $det H^{(n)} \simeq (det
\mathcal{J})^{\otimes s}$ for a suitable integer $s > 0$, hence (EGA II 4.5.6), `det 𝒥 = (det Lie H)⁻¹` is indeed
$S$-ample.

<!-- label: III.XV.5.7 -->

**Remark 5.8.** Let $S$ be a prescheme, $G$ and $H$ two $S$-preschemes in groups of finite presentation over $S$, $i : H
\to G$ an $S$-homomorphism of groups which is a monomorphism. If $H$ is smooth over $S$ with connected fibers, one knows
(Exp. XI 6.11) that $N = Norm_{G}(H)$ is representable by a closed subgroup prescheme of $G$, of finite presentation
over $S$. Suppose in addition that $N$ is smooth along the unit section and has the same relative dimension over $S$ as
$H$. The connected component $N^{0}$ of $N$ is then representable by an open subgroup prescheme of $N$, smooth over $S$
(Exp. VI_B 3.10). The monomorphism $i$ evidently factors through $N^{0}$. In fact one has $H = N^{0}$. Indeed, for every
point $s$ of $S$, one has $H_{s} = (N^{0})_{s}$, these two algebraic groups being connected, smooth, of the same
dimension. Since $H$ is flat over $S$, one deduces that $H \to N^{0}$ is an isomorphism (EGA IV 17.9.5). Finally $H$ is
a subgroup prescheme of $G$. We have therefore shown that the functor $\mathcal{L}$ introduced in this section is
identical to the functor of subgroups $H$ of $G$, smooth over $S$, with connected fibers and equal to their connected
normalizer.

<!-- label: III.XV.5.8 -->

## 6. Functor of Cartan subgroups and functor of parabolic subgroups

<!-- label: III.XV.6 -->

<!-- original page 422 -->

When $G$ is a smooth, connected algebraic group defined over an algebraically closed field $k$, one has defined the
sub-tori of $G$, the maximal sub-tori, the Cartan subgroups (Exp. XII 1), the Borel subgroups (Exp. XIV 4.1), the
parabolic subgroups (Exp. XIV 4.8 bis). We extend these notions to the case of a group prescheme over an arbitrary base,
as follows:

**Definition 6.1.** *Let $S$ be a prescheme, $G$ an $S$-prescheme in groups of finite presentation over $S$, $H$ an
$S$-prescheme in groups, $i : H \to G$ an $S$-monomorphism making $H$ a subgroup of $G$. We say that $H$ is a sub-torus
of $G$ (resp. a maximal sub-torus of $G$, a Cartan subgroup, a Borel subgroup, a parabolic subgroup) if:*

- *i) $H$ is smooth over $S$.*
- *ii) For every geometric point $s$ above $S$, $H_{s}$ is a sub-torus of $(G_{s})^{0}_{red}$ (resp. a maximal
  sub-torus, a Cartan subgroup, a Borel subgroup, a parabolic subgroup).*

<!-- label: III.XV.6.1 -->

**Remarks 6.1 bis.**

a) If the $S$-group $H$ is a sub-torus of $G$ (resp. ...), its fibers are connected, and consequently $H$ is of finite
presentation over $S$ (Exp. VI_B 5.3.3).

<!-- original page 423 -->

b) If $H$ is a sub-torus of $G$, then $H$ is a torus in the sense of Exp. IX, as follows immediately from Exp. X 8.1.
Moreover the monomorphism $i : H \to G$ is an immersion (cf. 8.3 below).

c) If $G$ is smooth over $S$ with connected fibers and if $H$ is a Cartan subgroup of $G$ (resp. a Borel subgroup, a
parabolic subgroup), the monomorphism $i : H \to G$ is an immersion, so that our definitions coincide with those
introduced in Exp. XII and Exp. XIV. Indeed, $H$ is then identical to its connected normalizer (by XII 6.6 c), XIV 4.8
and 4.8 bis), and it suffices to apply 5.8.

<!-- label: III.XV.6.1bis -->

**Definition 6.1 ter.** *Let $S$ be a prescheme, $G$ an $S$-prescheme in groups locally of finite type, $s$ a point of
$S$. The **nilpotent rank** of $G$ at the point $s$, denoted $\rho_{n}(s)$, is the dimension of the Cartan subgroups of
$(G_{s})^{0}_{red}$. One similarly defines the reductive rank $\rho_{r}(s)$, the unipotent rank $\rho_{u}(s)$, the
abelian rank $\rho_{ab}(s)$ (cf. Exp. X 8.7).*

<!-- label: III.XV.6.1ter -->

If now $G$ is a smooth connected algebraic group defined over an algebraically closed field $k$, recall that the
**radical** of $G$, denoted $rad(G)$, is the largest invariant, smooth, connected, solvable algebraic subgroup of $G$;
$G/rad(G)$ is then semisimple (use Exp. XII 6.1 to reduce to the affine case). If $G$ is moreover affine, one defines
the **unipotent radical** $rad_{u}(G)$ of $G$ as the largest invariant, smooth, connected, unipotent algebraic subgroup
of $G$; $G/rad_{u}(G)$ is then reductive.

<!-- original page 424 -->

**Proposition 6.2.** *Let $S$ be a prescheme, $G$ and $H$ two $S$-preschemes in groups of finite presentation over $S$,
$i : H \to G$ an $S$-monomorphism making $H$ a subgroup of $G$, and let $P(s)$ be one of the following properties
concerning the point $s$ of $S$:*

- *i) $(G_{s})^{0}_{red}$ is an abelian variety (resp. is affine, is a torus, is unipotent).*
- *ii) $(H_{s})^{0}_{red}$ is a maximal torus of $G_{s}$.*
- *iii) $(H_{s})^{0}_{red}$ is the centralizer in $(G_{s})^{0}_{red}$ of a torus of $G_{s}$ (resp. is a Cartan subgroup
  of $G_{s}$).*
- *iv) $(H_{s})^{0}_{red}$ is a Borel subgroup (resp. a parabolic subgroup) of $G_{s}$.*
- *v) $(H_{s})^{0}_{red}$ is the radical of $G_{s}$ (resp. $(G_{s})^{0}_{red}$ is semisimple).*
- *vi) $G_{s}$ is affine and $(H_{s})^{0}_{red}$ is the unipotent radical of $G_{s}$ (resp. $(G_{s})^{0}_{red}$ is
  reductive).*

*Then the set $E$ of points $s$ of $S$ for which $P(s)$ is true is locally constructible (EGA 0_III 9.1.11).*

<!-- label: III.XV.6.2 -->

**Remark 6.2.1.** This proposition complements Exp. VI_B § 10. Moreover, one can further specify the structure of $E$ by
using semi-continuity theorems (cf. Exp. X 8.7); we shall see an example a little later.

<!-- label: III.XV.6.2.1 -->

*Proof of 6.2.* <!-- original page 425 --> Note that if $S$ is the spectrum of a field, $E$ is invariant under extension
of that field. A standard reduction (EGA IV 9) then allows us to reduce to the case where $S$ is noetherian, integral,
with generic point $\eta$. One must show that $E$ or `ens(S) \ E` contains a neighborhood of $\eta$ (EGA IV 9.2.1). One
may assume $S$ affine of ring $A$ and field of fractions $K$. If $L$ is a finite extension of $K$, it is immediate that
there exists an $A$-subalgebra $B$ of $L$, finite over $A$, having $L$ as field of fractions. The canonical morphism $S'
\to S$, where $S' = \operatorname{Spec} B$, is dominant, of finite presentation, so the image of a non-empty open subset
of $S'$ contains a non-empty open subset of $S$ (EGA IV 1.8.4). From the viewpoint that interests us, we may therefore
replace $S$ by $S'$, hence replace $K$ by a finite extension $L$. Thus we may choose $L$ so that $(G_{L})_{red}$ and
$(H_{L})_{red}$ are smooth over $L$ (EGA IV 4.6.6). Possibly restricting $S'$, we may assume that $G_{red}$ and
$H_{red}$ are group preschemes smooth over $S$ (Exp. VI_B § 10 and EGA IV 17). In view of the properties to be proved,
we may replace $G$ and $H$ by their reduced connected components (Exp. VI_B 10.9), hence assume $G$ and $H$ smooth over
$S$ with connected fibers. Finally we may assume $H$ is a closed subgroup prescheme of $G$ (Exp. VI_B 10.4).

*Proof of i).* Possibly after a finite extension of $K$, we may assume that $G_{\eta}$ admits a "Chevalley
decomposition", i.e. is an extension of an abelian variety $D_{\eta}$ by a smooth connected linear algebraic group
$F_{\eta}$ (Séminaire Bourbaki 1956/57 N° 145). By Exp. VI_B 10.16, there exists an open neighborhood $U$ of $\eta$

<!-- original page 426 -->

such that this generic extension comes from an extension $1 \to F \to G|_{U} \to D \to 1$. One may further assume $F$
and $D$ smooth over $U$ with connected fibers, $F$ affine over $U$ and $D$ proper over $U$ (EGA IV 8, 9 and 17). For
every point $s$ of $U$, $(D_{s}, F_{s})$ is then the "Chevalley decomposition" of $G_{s}$. Consequently, $G_{s}$ is an
abelian variety (resp. is affine) if and only if $F_{s}$ (resp. $D_{s}$) is the unit group, which is a constructible
property (EGA IV 9.2.6.1).

To establish the last two assertions of i), we may, by the preceding, assume $G$ affine over $S$. Let $q$ be a prime
number invertible on $S$ and ${}_{qG}$ the "kernel" of the $q$-th power morphism in $G$. It follows easily from the
structure of affine algebraic groups that $G_{s}$ is a torus (resp. is unipotent) if and only if a) `_qGₛ` is
quasi-finite, which is a constructible property (EGA IV 9.3.2), and b) `_qGₛ` has $r^{q}$ geometric points, where $r$
denotes the relative dimension of $G$ over $S$ (resp. `_qGₛ` has a single point). Now the function
`s ↦ (number of geometric points of _qGₛ)` is constructible (EGA IV 9.7.9). This completes the proof of (i).

*Proof of iii).* a) **Case of a centralizer of a torus.** Suppose $H_{\eta} = Centr_{G_{\eta}}(T_{\eta})$, where
$T_{\eta}$ is a torus of $G_{\eta}$, and let us show that $H_{s}$ is the centralizer of a sub-torus of $G_{s}$ for $s$
in a neighborhood of $\eta$. By i), possibly restricting $S$,

<!-- original page 427 -->

we may assume that $T_{\eta}$ comes from a sub-torus $T$ of $G$. But then $Z = Centr_{G}(T)$ is representable (Exp. XI
6.11) by a subgroup prescheme of $G$. Since $H$ and $Z$ coincide generically, they coincide over a neighborhood of
$\eta$. This proves to us that the set $E$ of points $s$ of $S$ such that $H_{s}$ is the centralizer in $G_{s}$ of a
sub-torus of $G_{s}$ is ind-constructible (EGA IV 1), and this result will suffice for us to establish, in Lemma 6.6
below, that $E$ is an open part of $S$; *a fortiori*, $E$ will indeed be a locally constructible part of $S$.

iii) b) **Case of a Cartan subgroup.** Suppose $H_{\eta}$ is a Cartan subgroup of $G_{\eta}$, and let us show that
$H_{s}$ is a Cartan subgroup of $G_{s}$ for every point $s$ of a neighborhood of $\eta$. The group $H_{\eta}$ is the
centralizer in $G_{\eta}$ of a torus of $G_{\eta}$ and is nilpotent (Exp. XII 6.6). By a) and Exp. VI_B 8.4, $H_{s}$ has
the same properties for every point $s$ of a neighborhood $U$ of $\eta$. For every point $s$ of $U$, the group $H_{s}$
thus has the same reductive rank as $G_{s}$, and its unique maximal torus is central (Exp. XII 6.7); it is therefore the
centralizer of a maximal torus of $G_{s}$, i.e. a Cartan group of $G_{s}$.

Suppose now that $H$ is not a Cartan subgroup of $G$, and let us show that $H_{s}$ is not a Cartan subgroup of $G_{s}$
for $s$ in a neighborhood $U$ of $\eta$. In view of the assertion provisionally admitted in (a) above, we may restrict
to the case where $H$ is the centralizer in $G$ of a sub-torus $T$. But then $H_{\eta}$ contains a Cartan subgroup
$C_{\eta}$ of $H_{\eta}$. We have just seen that, possibly restricting $S$, $C_{\eta}$ extends to a Cartan subgroup $C$
of $G$, which one may assume contained in $H$. By hypothesis $H_{\eta}$ strictly majorizes $C_{\eta}$, so $H_{s}$
strictly majorizes $C_{s}$ for $s$ in a neighborhood $U$ of $\eta$ (EGA IV 9.5.2); *a fortiori*, $H_{s}$ is not

<!-- original page 428 -->

a Cartan subgroup of $G_{s}$ for $s$ in $U$.

*Proof of ii).* Suppose $H_{\eta}$ is a maximal torus of $G_{\eta}$ and let $C_{\eta}$ be its centralizer in $G_{\eta}$.
By i) and iii), $H$ is a torus over a neighborhood $U$ of $\eta$ and $C = Centr_{G|U}(H|U)$ is a Cartan subgroup of
$G|U$. To prove that $H$ is a maximal torus of $G$ over a neighborhood of $\eta$, we may then replace $G$ by $C$, then
by the linear component $F$ of a Chevalley decomposition of $C$ (cf. i)). Let $q$ be an integer invertible on $S$,
${}_{qF}$ the kernel of the $q$-th power morphism in $F$. Since $F_{s}$ is affine, nilpotent, smooth and connected,
$F_{s}$ is the direct product of its maximal torus $T_{s}$ by a unipotent group (*Bible* 6-04), so `_qFₛ = _qTₛ`. Since
$H_{\eta}$ is a maximal torus, `_qH_η = _qF_η`, and consequently ${}_{qH} = {}_{qF}$ over a neighborhood $V$ of $\eta$.
For every point $s$ of $V$, `_qHₛ = _qTₛ`, so $H_{s} = T_{s}$ is a maximal torus.

Suppose now that $H_{\eta}$ is not a maximal torus of $G_{\eta}$. By i), we may restrict to the case where $H_{\eta}$ is
a torus, then assume that it is contained in a strictly larger torus $T_{\eta}$. The latter extends to a torus $T$
strictly majorizing $H$ over a neighborhood $U$ of $\eta$. *A fortiori*, $H_{s}$ is not a maximal torus for $s \in U$.

*Proof of iv).* Possibly restricting $S$, we may assume that the center $Z$ of $G$ is representable (Exp. VI_B 10.11)
and flat over $S$, as well as the quotient $G/Z$ (*loc. cit.*). The property "$H_{s}$ majorizes $Z_{s}$" is
constructible (EGA IV 9.5.2) and every parabolic subgroup of $G_{s}$ contains $Z_{s}$ (Exp. XIV 4.9 a)); this allows us
to replace $G$ by $G/Z$, hence assume $G$ affine over $S$ (Exp. XII 6.1 and i)). We may further

<!-- original page 429 -->

assume that $G/H$ is representable, but then $H_{s}$ is a parabolic subgroup of $G_{s}$ if and only if $(G/H)_{s}$ is
proper (*Bible* 6 Th. 4 b)), which is an ind-constructible property (EGA IV 9.3.5). So $E$ is ind-constructible, and
this will suffice for us to prove that $E$ is open (Lemma 6.6), hence locally constructible.

Let us now examine the case of Borel subgroups. If $H_{\eta}$ is a Borel subgroup of $G_{\eta}$, i.e. a solvable
parabolic subgroup of $G_{\eta}$, what precedes and Exp. VI_B 8.4 entail that these properties remain true at every
point $s$ of a neighborhood of $\eta$. If now $H_{\eta}$ is not a Borel subgroup of $G_{\eta}$, to prove that the same
holds at points $s$ of a neighborhood of $\eta$, we may restrict (in view of what precedes) to the case where $H_{\eta}$
is a parabolic subgroup, then assume that $H_{\eta}$ contains a Borel subgroup $B_{\eta}$. We have just shown that the
latter extends to a Borel subgroup $B$ of $G$ over a neighborhood $U$ of $\eta$. Since $H_{\eta}$ strictly majorizes
$B_{\eta}$, $H_{s}$ strictly majorizes $B_{s}$ at every point of an open subset $V$, and $H_{s}$ is not a Borel subgroup
of $G_{s}$ for $s \in V$.

*Proof of v).* Suppose $H_{\eta}$ is the radical of $G_{\eta}$. The group $H_{\eta}$ is then invariant in $G_{\eta}$,
solvable (smooth and connected); the same is therefore true for $H_{s}$ for $s$ belonging to a neighborhood $U$ of
$\eta$ (Exp. VI_B 8 and 10), so for $s \in U$, $H_{s}$ is contained in the radical of $G_{s}$. Replacing $G$ by $G/H$
(Exp. VI_B 10), we must

<!-- original page 430 -->

prove that if $G_{\eta}$ is semisimple, then $G_{s}$ is semisimple at every point of a neighborhood $V$ of $\eta$. Using
i) and ii), one may assume that $G$ is affine over $S$ and possesses a maximal torus $T$. Let $W$ be the Weyl group of
$T$ (Exp. XII 2), which is quasi-finite and étale over $S$, hence finite and étale over an open subset $V$. It then
follows from the elementary properties of roots (Exp. XIX 1.12) that $G$ is semisimple over $V$.

Suppose now that $H_{\eta}$ is not the radical of $G_{\eta}$. Possibly replacing $K$ by a finite extension $L$, we may
assume that $G_{\eta}$ admits a radical $R_{\eta}$. By what precedes, $R_{\eta}$ extends to a subgroup prescheme $R$ of
$G|_{U}$ such that for every $s \in U$, $R_{s}$ is the radical of $G_{s}$. By hypothesis, $R_{\eta} \neq H_{\eta}$. So
$R_{s} \neq H_{s}$ for $s \in V$. It remains to prove that if $G_{\eta}$ is not semisimple, neither is $G_{s}$ at
neighboring points, but this is a particular case of what precedes (take $H$ = unit group).

*Proof of vi).* The proof is entirely analogous to that of v), in view of i), and is left to the care of the reader.

**Corollary 6.3.** *Let $S_{0}$ be a quasi-compact prescheme, $(S_{i})_{i \in L}$ a projective system of
$S_{0}$-preschemes, affine over $S_{0}$, $S = \lim S_{i}$ (EGA IV 8.2), $G_{0}$ a group prescheme of finite presentation
over $S_{0}$, $G_{i} = G_{0} \times_{S_{0}} S_{i}$, $G = G_{0} \times_{S_{0}} S$, $H$ a subgroup of $G$. Then, if $H$ is
a sub-torus of $G$ (resp. a maximal sub-torus, a Cartan subgroup, a Borel subgroup, a parabolic subgroup), there exists
an index $i \in L$ and a subgroup `Hᵢ` of `Gᵢ` such that $H = H_{i} \times_{S_{i}} S$ and `Hᵢ` is a sub-torus of `Gᵢ`
(resp. ...).*

<!-- label: III.XV.6.3 -->

<!-- original page 431 -->

Indeed, $H$ is smooth with connected fibers, hence of finite presentation over $S$ (Exp. VI_B 5.3.3). By Exp. VI_B § 10,
there exist $i \in L$ and a subgroup `Hᵢ` of `Gᵢ`, smooth over $S$, such that $H = H_{i} \times_{S_{i}} S$. Corollary
6.3 then follows from Definition 6.1, from 6.2, and from EGA IV 9.3.3.

**Corollary 6.3 bis.** *Let $S$ be a prescheme, $G$ an $S$-prescheme in groups of finite presentation over $S$. Then the
functions $\rho_{n}$, $\rho_{r}$, $\rho_{u}$, $\rho_{ab}$ (cf. 6.1 ter) are locally constructible functions on $S$.*

<!-- label: III.XV.6.3bis -->

It suffices to show (EGA IV 9.) that if $S$ is a noetherian integral scheme with generic point $\eta$, the functions in
question are constant on a neighborhood of $\eta$. Possibly replacing $S$ by a scheme $S'$ finite over $S$ and
dominating $S$, we may assume that $G_{\eta}$ admits a Cartan subgroup $C_{\eta}$ with a Chevalley decomposition $1 \to
L_{\eta} \to C_{\eta} \to A_{\eta} \to 1$. The argument made in 6.2 i) proves that this decomposition extends to a
Chevalley decomposition over a neighborhood of $\eta$:

$$ 1 \longrightarrow L \longrightarrow C \longrightarrow A \longrightarrow 1. $$

Moreover, one may assume that $C$ is a Cartan subgroup of $G$ (6.3) and that the maximal torus $T_{\eta}$ of $L_{\eta}$
extends to a maximal torus $T$ of $L$ (6.3). The corollary follows immediately from this and from the definitions.

**6.4.0.** Let then $S$ be a prescheme, $G$ an $S$-prescheme in groups of finite presentation over $S$, $\mathcal{L}$
the functor of subgroups of $G$, smooth, with connected fibers and equal to their connected normalizer (cf. § 5);
$\mathcal{L}$ is representable (5.2 and 5.8). The remainder of this

<!-- original page 432 -->

section is devoted to the study of certain subfunctors of $\mathcal{L}$. More precisely, we introduce the subfunctors of
$\mathcal{L}$, denoted $\mathcal{L}_{C}$ (resp. $\mathcal{CT}$, resp. $\mathcal{P}$), defined as follows: for every
$S$-prescheme $S'$, $\mathcal{L}_{C}(S')$ (resp. $\mathcal{CT}(S')$, resp. $\mathcal{P}(S')$) is the set of subgroups
$H$ of $G_{S'}$, smooth over $S'$, with connected fibers, equal to their connected normalizer, and such that for every
point $s'$ of $S'$, $H_{s}'$ contains a Cartan subgroup (6.1) of $G_{s}'$ (resp. is the centralizer in
$(G_{s}')^{0}_{red}$ of a sub-torus of $G_{s}'$, resp. is a parabolic subgroup (6.1) of $G_{s}'$).

<!-- label: III.XV.6.4.0 -->

**Theorem 6.4.** *Let $S$ be a prescheme, $G$ an $S$-prescheme in groups of finite presentation over $S$. Then the
$S$-functors $\mathcal{L}_{C}$, $\mathcal{CT}$, $\mathcal{P}$ above (6.4.0) are representable by $S$-preschemes of
finite presentation over $S$, quasi-projective over $S$.*

<!-- label: III.XV.6.4 -->

**Remark 6.5.** If $G$ has smooth fibers, for example if $G$ is smooth over $S$, or if the residue characteristics of
$S$ are zero (Exp. VI_B 1.6.1), every subgroup $H$ of $G$, smooth over $S$ with connected fibers, such that for every
point $s$ of $S$, $H_{s}$ contains a Cartan subgroup of $(G_{s})^{0}$, is necessarily equal to its connected normalizer
(and consequently is an element of $\mathcal{L}_{C}(S)$). Indeed, using 5.1 iii), one may assume that $S$ is the
spectrum of a field, in which case the property was noted at the end of the statement of Exp. XIII 2.1.

<!-- label: III.XV.6.5 -->

Note that one has natural monomorphisms

```text
𝒞𝒯 ↘
       ℒ_C ──→ ℒ.
𝒫  ↗
```

<!-- original page 433 -->

Let us show that these monomorphisms are open immersions of finite presentation (which will already prove, in view of
5.2, that $\mathcal{L}_{C}$, $\mathcal{CT}$, $\mathcal{P}$ are representable by $S$-preschemes, union of an increasing
sequence of open subpreschemes, quasi-projective and of finite presentation over $S$). Now this will follow, by the
usual technique, from the following lemma:

**Lemma 6.6.** *Let $S$ be a prescheme, $G$ an $S$-prescheme in groups of finite presentation, $H$ a subgroup of $G$,
smooth with connected fibers. Then the set of points $s$ of $S$ such that $H_{s}$ contains a Cartan subgroup of $G_{s}$
(resp. is equal to the centralizer in $(G_{s})^{0}_{red}$ of a torus of $G_{s}$) is an open subset of $S$. If moreover
$H$ is equal to its connected normalizer*[^XV-6-1]*, the set of points $s$ of $S$ such that $H_{s}$ is a parabolic
subgroup of $G_{s}$ is also an open subset of $S$.*

<!-- label: III.XV.6.6 -->

The assertion to be proved is local on $S$, which allows us to assume $S$ affine, then, by EGA IV 8.1 and 6.3, $S$
noetherian. Denote by $E$ the set of points of $S$ having the property in question. It then follows from the assertions
effectively proved in 6.2 that $E$ is ind-constructible. But $S$ is noetherian, so to prove that $E$ is open, it
suffices to show that $E$ is stable under generizations (EGA IV 1.10.1). Using EGA II 7.1.9, we are finally led to prove
that if $S$ is the spectrum of a discrete valuation ring, and if the closed point $s$ belongs to $E$, then so does the
generic point $t$.

<!-- original page 434 -->

We shall need the following lemma:

**Lemma 6.7.** *Let $A$ be a complete noetherian local ring, $S = \operatorname{Spec} A$, $s$ the closed point of $S$,
$H$ an $S$-prescheme in groups, smooth with connected fibers, $T_{s}$ a sub-torus of $H_{s}$. Then:*

- *i) There exists a closed subgroup prescheme $C$ of $H$, smooth, with connected fibers, such that $C_{s} =
  Centr_{H_{s}}(T_{s})$.*
- *ii) For every point $t$ of $S$, $C_{t}$ is the centralizer in $H_{t}$ of a sub-torus $T_{t}$ of $H_{t}$.*

<!-- label: III.XV.6.7 -->

*Proof of 6.7.* Let $T^{0}$ be an $S$-torus such that there exists an isomorphism $u_{0} : T^{0}_{s} \xrightarrow{\sim}
T_{s}$ (Exp. X 4.6). Let $\mathfrak{m}$ be the maximal ideal of $A$, $A_{n} = A/\mathfrak{m}^{n}$, $S_{n} =
\operatorname{Spec} A_{n}$, $H_{n} = H \times_{S} S_{n}$, etc. Since $H$ is smooth over $S$, for every integer $n > 0$
there exists an $S_{n}$-group morphism $u_{n} : T^{0}_{n} \to H_{n}$ lifting $u_{0}$ (Exp. IX 3.6), and one may assume
by induction on $n$ that $u_{n}$ lifts $u_{n-1}$. Moreover, let $q$ be a prime number invertible on $S$; for every
integer $\ell$ equal to a power of $q$, denote by ${}_{\ell }u_{n}$ the restriction of $u_{n}$ to the subgroup ${}_{\ell
}T^{0}_{n}$. For fixed $\ell$ and variable $n$, the morphisms ${}_{\ell }u_{n}$ form a projective system, hence come
from a unique $S$-group morphism ${}_{\ell }u : {}_{\ell }T^{0} \to H$ (1.6 a)). Since $H$ is separated (Exp. VI_B 5.2)
and $u_{0}$ is a monomorphism, ${}_{\ell }u$ is a monomorphism (Exp. IX 6.8), and even a closed immersion since it is
finite, ${}_{\ell }T^{0}$ being finite over $S$. Denote by $M(\ell)$ the image group. It is clear that the family of
subgroups of multiplicative type $M(\ell)$ is coherent in the sense of 4.1. Let $C_{\ell} = Centr_{H}(M(\ell))$, which
is representable by a subgroup prescheme (2.5), closed ($H$ is separated),

<!-- original page 435 -->

smooth over $S$ (Exp. XI 2.4). The $C_{\ell}$ form a filtered decreasing family of closed subschemes, hence stationary,
$H$ being noetherian. The stationary value is a smooth closed subgroup $C$ such that $C_{s} = Centr_{H_{s}}(T_{s})$ by
the density theorem (Exp. IX 4.7). It remains to show that for every point $t$ of $S$, $C_{t}$ is the centralizer in
$H_{t}$ of a sub-torus $T_{t}$ (which will entail that $C_{t}$ is connected). But this will follow from the more precise
lemma below, applied to the family $M(\ell)_{t}$ of subgroups of $H_{t}$:

**Lemma 6.8.** *Let $G$ be a connected algebraic group defined over a field $k$, $r$ an integer `> 0`, $q$ an integer
prime to the characteristic*[^N.D.E-XV-7] *of $k$, $M(\ell)$ ($\ell$ ranging over the powers of $q$) a coherent family
of subgroups of $G$, of multiplicative type and of type $(\mathbb{Z}/\ell \mathbb{Z})^{r}$ (cf. 4.6), $M$ the algebraic
subgroup of $G$ generated by the $M(\ell)$ (*loc. cit.*), $T$ the unique maximal torus of $M$ (cf. 3.4). Then*

```text
Centr_G(T) = Centr_G(M) = Centr_G(M(ℓ))    for ℓ large enough.
```

<!-- label: III.XV.6.8 -->

The last equality is clear. To prove the first, introduce the center $Z$ of $G$, $G' = G/Z$, $M'$ (resp. $T'$) the image
of $M$ (resp. $T$) in $G'$, $K$ the inverse image of $T'$ in $G$ (i.e. the algebraic subgroup of $G$ generated by $T$
and $Z$). It evidently suffices to prove that $K \supset M$, hence that $T' = M'$. Now, $M$ is smooth and connected
(4.6) and $G'$ is affine (Exp. XII 6.1), so $M'$ is a direct product of its maximal torus

<!-- original page 436 -->

$T'$ (Exp. XII 6.6 d)) and a unipotent group (*Bible* 4 Th. 4) (one may assume $k$ algebraically closed). The image of
$M(\ell)$ in $M'$ is therefore necessarily contained in $T'$. So the inverse image of $T'$ in $M$ majorizes $M(\ell)$
for every $\ell$, hence equals $M$. Consequently $M' = T'$. This proves 6.8 and hence 6.7.

This being so, let us prove 6.6. We have reduced to the case where $S$ is the spectrum of a discrete valuation ring $A$,
which one may further assume complete with algebraically closed residue field. Possibly replacing $A$ by its
normalization in a finite extension of its field of fractions, one may assume that $(G_{t})_{red}$ is
smooth[^N.D.E-XV-8]. It is clear that to prove 6.6 one may replace $G$ by the connected component of the schematic
closure in $G$ of $(G_{t})^{0}_{red}$, hence assume $G$ flat over $S$ with connected fibers, and $G_{t}$ smooth.

a) Suppose $H_{s}$ is the centralizer in $(G_{s})_{red}$ of a torus $T_{s}$, and let us show that $H_{t}$ is then the
centralizer in $G_{t}$ of a sub-torus of $G_{t}$. By Lemma 6.7, there exists a subgroup scheme $C$ of $H$, smooth over
$S$, whose closed fiber is $H_{s}$ and such that $C_{t} = Centr_{H_{t}}(T_{t})$, where $T_{t}$ is a sub-torus of
$H_{t}$. Since $H$ is smooth over $S$ with connected fibers, one concludes for dimension reasons that $C = H$. Keeping
the notation of 6.7, one has $H = C = C_{\ell}$ for $\ell$ large. Consider similarly $C'_{\ell} = Centr_{G}(M(\ell))$
(2.5), and let $C'$ be the stationary value of $C'_{\ell}$ for $\ell$ large (2.5 bis). The group scheme $C'$ majorizes
$H$ and is such that $C'_{t} = Centr_{G_{t}}(T_{t})$ (6.8) and $C'_{s} = Centr_{G_{s}}(T_{s})$. The hypothesis made on
$H_{s}$ implies $\dim H_{s} = \dim C'_{s}$. Moreover, $\dim H_{s} = \dim H_{t}$ (since $H$ is smooth over $S$) and $\dim
C'_{t} \leqslant \dim C'_{s}$ (Exp. VI_B 4.1),

<!-- original page 437 -->

so $\dim H_{t} = \dim C'_{t}$. But $G_{t}$ being smooth and connected, $C'_{t} = Centr_{G_{t}}(T_{t})$ is smooth and
connected, so finally $H_{t} = C'_{t} = Centr_{G_{t}}(T_{t})$.

b) Suppose $H_{s}$ contains a Cartan subgroup $C_{s}$ of $G_{s}$, i.e. the centralizer in $(G_{s})_{red}$ of a maximal
torus $T_{s}$ of $G_{s}$. By 6.7, there exists a subgroup scheme $C$ of $H$, smooth over $S$, with connected fibers,
lifting $C_{s}$. It evidently suffices to prove that $C_{t}$ contains a Cartan subgroup of $G_{t}$. Now by a) applied
with $H = C$, $C_{t}$ is the centralizer in $G_{t}$ of a sub-torus of $G_{t}$, hence contains a Cartan subgroup of
$G_{t}$.

c) Suppose $H_{s}$ is a parabolic subgroup of $G_{s}$. Let $N = Norm_{G}(H)$. By hypothesis, $H$ is equal to its
connected normalizer, so $N_{s}$ is smooth, and consequently equals $Norm_{(G_{s})_{red}}(H_{s}) = H_{s}$ (Exp. XII 8
bis). But then $N$ is flat over $S$. We shall see in Exp. XVI that, under these conditions, $G/N$ is representable.
Since $H_{s} = N_{s}$ is a parabolic subgroup of $G$, $(G/N)_{s}$ is proper. Since $(G/N)$ has connected fibers and is
flat over $S$, it follows from EGA III 5.5.1 that $(G/N)$ is proper over $S$. So $(G/N)_{t} = G_{t}/N_{t}$ is proper
over $t$, and the same is true of $G_{t}/H_{t}$, since $N_{t}/H_{t}$ is finite. It then suffices to apply the following
lemma:

**Lemma 6.9.** \*Let $k$ be a field, $G$ a $k$-algebraic group, $H$ a smooth connected algebraic subgroup of $G$,

<!-- original page 438 -->

$N = Norm_{G} H$; then if $\dim H = \dim N$ and if $G/H$ is proper, $H$ is a parabolic subgroup of $G$.\*

<!-- label: III.XV.6.9 -->

Indeed, one may assume $k$ algebraically closed and $G$ smooth and connected. The center $Z$ of $G$ is contained in $N$,
and the hypothesis $\dim H = \dim N$ entails that $Z^{0} = (Z)^{0}_{red}$ is contained in $H$, so $G' = G/Z^{0}$ is
affine (Exp. XII 6.1). Replacing $G$ by $G'$ and $H$ by its image in $G'$, one is reduced to the case where $G$ is
affine (Exp. XIV 4.9), and Lemma 6.9 then follows from *Bible* 6 Th. 4. We have therefore proved Lemma 6.6.

To complete the proof of 6.4, we must prove that the $S$-preschemes representing $\mathcal{L}_{C}$ (resp.
$\mathcal{CT}$, resp. $\mathcal{P}$) are of finite presentation over $S$. This assertion is local on $S$, which allows
us to assume $S$ affine, then, $G$ being of finite presentation, $S$ noetherian (EGA IV 8.9). We have just seen that the
natural inclusions $\mathcal{CT} \to \mathcal{L}$ (resp. $\mathcal{P} \to \mathcal{L}$) are immersions, so the same is
true of the inclusions $\mathcal{CT} \to \mathcal{L}_{C}$ (resp. $\mathcal{P} \to \mathcal{L}_{C}$), and consequently it
suffices to prove that $\mathcal{L}_{C}$ is representable by an $S$-prescheme of finite presentation.

Let us resume the notation introduced in 5.2. For every integer $n \geqslant 0$, let $\mathcal{L}_{n}$ be the subfunctor
of $\mathcal{L}$ such that

```text
ℒ_n(S′) = {H ∈ ℒ(S′) such that Norm_{G_{S′}}(H) = Norm_{G_{S′}}(H^{(n)})}.
```

The $S$-functor $\mathcal{L}_{n}$ is therefore representable by an open subprescheme of $\mathcal{L}$, sum of the
$\mathcal{L}^{r}_{n}$. Each $\mathcal{L}^{r}_{n}$ is of finite presentation over $S$ (5.3) and is empty for $r > \sup_{s
\in S} \dim G_{s}$ (which is a finite number, $S$ being quasi-compact), so $\mathcal{L}_{n}$ is

<!-- original page 439 -->

of finite presentation over $S$. It suffices to prove that $\mathcal{L}_{C}$ is contained in $\mathcal{L}_{n}$ for $n$
large enough.

For every point $s$ of $S$, let $d(s)$ be the smallest integer $n$ (finite or infinite) such that $\mathcal{L}_{C,
G_{s}} \subset \mathcal{L}_{n, G_{s}}$. It suffices to show that the function $d$ is bounded on $S$, since if $M$ is an
upper bound, $\mathcal{L}_{C}$ will be set-theoretically contained in $\mathcal{L}_{M}$, so $\mathcal{L}_{C}$ will be
contained in $\mathcal{L}_{M}$, since the latter is an open subset of $\mathcal{L}$. An immediate constructibility
argument reduces us to proving that if $S$ is noetherian integral with generic point $t$, then $d$ is bounded on a
neighborhood of $t$.

a) **Reduction to the case where $G$ is smooth over $S$.** Proceeding as in 6.2, one sees that, possibly changing $S$,
one may assume that $(G)_{red}$ is a group prescheme smooth over $S$, which we shall denote $G'$. Set $X =
\mathcal{L}_{C, G}$, $X' = \mathcal{L}_{C, G'}$ and let $H$ (resp. $H'$) be the subgroup prescheme of `G_X` (resp.
$G'_{X'}$) universal for the functor $\mathcal{L}_{C, G}$ (resp. $\mathcal{L}_{C, G'}$). Since $H$ is smooth over $X$,
$H \times_{X} X_{red}$ is reduced, hence contained in $G'_{X_{red}}$, and is an element of $\mathcal{L}_{C,
G'}(X_{red})$, whence a canonical morphism $p : X_{red} \to X'$. It is clear that $p$ is a monomorphism; let us show
that $p$ is even an immersion. Let $N'$ be the normalizer of $H'$ in $G_{X'}$. The set of points $s$ of $X'$ such that
the immersion $H'_{s} \to N'_{s}$ is an open immersion is an open subset $U$, and $H'|_{U} \to N|_{U}$ is an open
immersion (Exp. VI_B 2.5 and EGA IV 17.9.5). It follows from 5.1 iii) that $U$ is the largest open subset of $X'$ above
which $H'$ is equal to its connected normalizer in $G_{X'}$, so $H'|_{U} \in \mathcal{L}_{C, G}(U)$. One immediately
deduces that $p$ is an isomorphism of $X_{red}$ onto $U_{red}$. If one shows that $\mathcal{L}_{C, G}$ is of finite type
when $G$ is smooth, $X'$ will be of finite type over $S$,

<!-- original page 440 -->

so $X_{red}$ will be of finite type ($S$ is noetherian) and consequently will be contained in $\mathcal{L}^{M}_{G}$ for
$M$ large enough, and the same will hold of $X$.

b) **Case where $S$ is the spectrum of an algebraically closed field $k$ of characteristic $p > 0$ and $G$ is a smooth
algebraic group over $k$.** Instead of using the infinitesimal neighborhoods $H^{(n)}$ of a subgroup prescheme $H$ of
$G$, we shall use the radicial subgroups $F_{n}(H)$, kernels of the iterates of the Frobenius morphism in $H$ (Exp.
VII_A 4), which is legitimate here, since $F_{n}(H)$ is contained in the infinitesimal neighborhood of order $p^{n}$ of
the unit section of $H$. If $T$ is a sub-torus of $G$, $F_{n}(T) = {}_{p^{n}}(T)$, and it is immediate by duality that
$Centr_{G}({}_{p^{n}}(T))$ is equal to $Centr_{G}(T)$ for $n$ large enough. One then has the following more precise
proposition:

**Proposition 6.10.** *Let $k$ be a field of characteristic $p > 0$, $G$ a smooth $k$-algebraic group, $T$ a maximal
torus of $G_{\bar{k}}$, $m$ the smallest integer such that*

$$ Centr_{G}({}_{p^{m}}(T))^{0} = Centr_{G}(T)^{0}. $$

*Then, for every $k$-prescheme $S$ and every $H \in \mathcal{L}_{C}(S)$, one has*

$$ Norm_{G_{S}}(H) = Norm_{G_{S}}(F_{m}(H)). $$

*A fortiori, $\mathcal{L}_{C}$ is contained in $\mathcal{L}^{p^{m}}$.*

<!-- label: III.XV.6.10 -->

Since $H$ is smooth over $S$, of finite presentation over $S$ and has a constant nilpotent rank (namely that of $G$), we
shall see in the following section (7.3) that the functor $\mathcal{C}_{H}$

<!-- original page 441 -->

of Cartan subgroups of $H$ is representable by an $S$-prescheme, smooth over $S$ (the reader will verify that the proof
given of this property does not use the fact that $\mathcal{L}_{C, H}$ is of finite type over $S$). It then follows from
Exp. XIII 3.1 that one may consider the open subset $U$ of regular points of $H$.

Let $S'$ be an $S$-prescheme, $g$ an element of $G(S')$ normalizing $F_{m}(H)_{S'}$. To prove that $g$ normalizes
$H_{S'}$, it suffices to prove that $int(g)U_{S'}$ is contained in $H_{S'}$; indeed, $H_{S'} \cap int(g)H_{S'}$ will
then contain an open subgroup of `int(g)H`, hence will be equal to

<!-- original page 442 -->

`int(g)H`, since the latter has connected fibers. Possibly replacing $S'$ by a suitable $S''$, then $S''$ by $S$, we are
reduced to proving that if $g \in G(S)$ normalizes $F_{m}(H)$ and if $u \in U(S)$, then $int(g)u \in H(S)$.

Now let $C$ be the unique Cartan subgroup of `H_S` "containing" $u$ (Exp. XIII 3.2). It suffices to show that $C' =
int(g)C \subset H$. Since $H \in \mathcal{L}_{C, G}(S)$, $C$ is also a Cartan subgroup of $G$; but the latter admits
maximal tori, so (Exp. XII 7.1 (a)) $C$ is the centralizer in $G^{0}_{S}$ of its unique maximal torus $T$. It follows
from the definition of $m$ (and from the fact that any two maximal tori of $G$ are locally conjugate for fpqc (Exp. XII
7.1)) that

$$ C = (Centr_{G}(T))^{0} = Centr_{G}({}_{p^{m}}(T))^{0}, $$

whence by conjugation by $g$:

$$ C' = Centr_{G}(int(g)({}_{p^{m}}(T)))^{0}. $$

But $int(g)({}_{p^{m}}(T))$ is a subgroup of multiplicative type of $int(g)(F_{m}(H)) = F_{m}(H)$ ($g$ normalizes
$F_{m}(H)$), hence is contained in $H$. It then follows from Exp. XIII 2.1 (which is proved when the base is a field,
but extends immediately to the case of an arbitrary base) that for $C'$ to be contained in $H$ it suffices that

```text
Lie C′ ⊂ Lie H.
```

Now `Lie C′ = int(g)(Lie C) ⊂ int(g)(Lie H)`.

On the other hand, if $m \geqslant 1$, which it is permissible to assume, one has (using Exp. VII_A 4.1.2):

```text
Lie H = Lie(F_m(H)) = Lie(int(g)(F_m(H))) = int(g)(Lie H).
```

So $Lie C' \subset Lie H$, which completes the proof of 6.10.

We shall need another definition of the integer $m$ introduced in 6.10.

**Lemma 6.11.** *Let $G$ be a smooth algebraic group defined over an algebraically closed field $k$ of characteristic
$p > 0$, $T$ a maximal torus of $G$, $\mathfrak{g} = Lie G$, and $R$ the family of non-zero characters of $T$ appearing
in the representation of $T$ in $\mathfrak{g}$ induced by the adjoint representation of $G$. For every element
$r \in R$, denote by $e_{r}$ the largest integer $n$ such that $p^{n}$ divides $r$ in the group of characters of $T$.
Then $m = \sup_{r \in R}(e_{r} + 1)$ if $R \neq \emptyset$, and $m = 0$ otherwise.*

<!-- label: III.XV.6.11 -->

Indeed, $Centr_{G}(T)$ is smooth and contained in $Centr_{G}({}_{p^{m}}(T))$, so

```text
(Centr_G T)⁰ = (Centr_G(_{pᵐ}(T)))⁰ ⇔ Lie(Centr_G T) = Lie(Centr_G(F_m(T)))
                                    ⇔ 𝔤^T = 𝔤^{_{pᵐ}(T)}    (Exp. II 5.2.3).
```

<!-- original page 443 -->

Now with the usual notation,

```text
𝔤 = 𝔤_0 ⊕ ∐_{r ∈ R} 𝔤_r.
```

So $\mathfrak{g}^{T} = \mathfrak{g}_{0}$ and $\mathfrak{g}^{{}_{p^{m}}(T)} = \mathfrak{g}_{0} + \coprod_{r \in R_{0}}
\mathfrak{g}_{r}$, where `R_0` is the subset of $R$ consisting of characters of $T$ whose restriction to ${}_{p^{m}}(T)$
is zero. But a non-zero character $r$ of $T$ has trivial restriction to ${}_{p^{m}}(T)$ if and only if $m \leqslant
e_{r}$, whence the lemma.

c) **Return to the proof of 6.4.** We have reduced (by point a) and the section preceding it) to the case where $S$ is a
noetherian integral scheme and $G$ is smooth over $S$. We must show that the function $d$ is bounded on a neighborhood
of the generic point $t$ of $S$. Possibly changing $S$, we may assume that $G$ admits a trivial maximal torus (6.2) $T =
D_{S}(M)$. Let then $\mathfrak{g} = \coprod_{\lambda \in M} \mathfrak{g}_{\lambda}$ be the decomposition of the Lie
algebra of $G$ according to the characters of $T$, and let $R$ be the finite set of non-zero characters of $M$ such that
$\mathfrak{g}_{\lambda} \neq 0$. Let us distinguish two cases:

**1st case: the point $t$, and hence all points of $S$, have residue characteristic $p > 0$.** It is clear, from what
precedes, that the function $d$ is then bounded by `pᵐ`, where $m$ is defined as in 6.11.

**2nd case: the point $t$ has residue characteristic zero.** For every $\lambda \in R$, let $n_{\lambda}$ be the largest
integer dividing $\lambda$ in the group $M$, and set $n = \prod n_{\lambda}$, $\lambda \in R$. For every prime number
$q$ dividing $n$, denote by $S_{q}$ the closed subset of $S$ consisting of points of $S$ whose residue characteristic
equals $q$, and let $U$ be the non-empty open subset (it contains $t$) complementary in $S$ to the union of the $S_{q}$.
If now $s$ is a point of $U$, either $s$

<!-- original page 444 -->

has residue characteristic zero, in which case $d(s) = 1$ (5.6), or $s$ has residue characteristic $p > 0$ not dividing
$n$, so the integer $m$ relative to the group $G_{s}$, defined in 6.11, is at most one. Moreover, it follows from Exp.
VII[^N.D.E-XV-9] that

```text
Norm_{G_{S′}}(F_1(H)) = Norm_{G_{S′}}(Lie H) = Norm_{G_{S′}}(H^{(1)}).
```

Finally, it follows from 6.10 that if $H \in \mathcal{L}_{C, G_{s}}(S')$, one has $Norm_{G_{S'}}(H) =
Norm_{G_{S'}}(H^{(1)})$, and consequently $d(s) \leqslant 1$, so $d$ is bounded by `1` on $U$.

This completes the proof of 6.4.

**Corollary 6.12.** *Let $S$ be a prescheme and $G$ an $S$-prescheme in groups of finite presentation. Suppose that the
nilpotent rank (resp. the dimension of the Borel subgroups) of the fibers of $G$ is a locally constant function on $S$.
Then the functor $\mathcal{C}$ of Cartan subgroups of $G$ (resp. the functor $\mathcal{B}$ of Borel subgroups of $G$) is
representable by an $S$-prescheme of finite presentation over $S$.*

<!-- label: III.XV.6.12 -->

Indeed, possibly restricting $S$, we may assume that the nilpotent rank $\nu$ of the fibers is constant. But then it is
clear that $\mathcal{C}$ is represented by the open-closed subprescheme of the prescheme $X$ representing
$\mathcal{L}_{C}$ (6.4) above which the universal subgroup of `G_X` relative to the functor $\mathcal{L}_{C}$ is of
relative dimension $\nu$. The proof is analogous for the functor $\mathcal{B}$, in view of the representability of the
functor $\mathcal{P}$.

## 7. Cartan subgroups of a smooth group

<!-- label: III.XV.7 -->

<!-- original page 445 -->

**Proposition 7.1.** *Let $S$ be a prescheme, $G$ an $S$-prescheme in groups of finite presentation, smooth over $S$,
with connected fibers.*

- *i) Let $\mathcal{CT}$ be the $S$-functor $(Sch/S)^{\circ} \to Ens$ such that for every $S$-prescheme $S'$:*
    > *$\mathcal{CT}(S')$ = set of subgroup preschemes $H$ of $G_{S'}$, smooth over $S'$, such that for every point $s'$ of $S'$,
    > $H_{s}'$ is the centralizer in $G_{s}'$ of a sub-torus of $G_{s}'$.*
- *Then $\mathcal{CT}$ is representable by an $S$-prescheme of finite presentation over $S$, smooth and quasi-projective
  over $S$.*
- *ii) If $S$ is artinian and $H \in \mathcal{CT}(S)$, then $H$ is the centralizer in $G$ of a sub-torus of $G$. If $S$
  is the spectrum of a Henselian local ring and $H \in \mathcal{CT}(S)$, then $H$ is the centralizer in $G$ of a
  subgroup of multiplicative type of $G$, étale over $S$.*
- *iii) If $L$ is an $S$-prescheme in groups, smooth and of finite presentation over $S$, $i : L \to G$ an $S$-group
  monomorphism, and $H$ an element of $\mathcal{CT}(S)$, then $Transp_{G}(H, L)$ and $Transp^{str}_{G}(H, L)$ (cf. Exp.
  VIII 6.5 e)) are representable by closed subpreschemes of $G$, smooth over $S$.*
- *iv) If $H \in \mathcal{CT}(S)$, $H$ is closed in $G$, $N = Norm_{G}(H)$ is representable by a closed subgroup
  prescheme of $G$, smooth over $S$;*

<!-- original page 446 -->

*$N/H$ is representable by an $S$-prescheme in groups, separated over $S$, étale and of finite type over $S$; $G/N$ is
representable by an $S$-prescheme smooth and quasi-projective over $S$.*

- *v) Let $G'$ be an $S$-prescheme in groups of finite presentation over $S$ and $u : G \to G'$ a faithfully flat
  $S$-group morphism, so that $G'$ satisfies the same hypotheses as $G$ (Exp. VI_B 9). Then if $H \in
  \mathcal{CT}_{G}(S)$, the image of $H$ by $u$ is representable by a subgroup prescheme $H'$ of $G'$ which is an
  element of $\mathcal{CT}_{G'}(S)$. Moreover, $H \to H'$ is faithfully flat, and if $H$ is the centralizer in $G$ of a
  torus $T$, $H'$ is the centralizer in $G'$ of the torus $T' = u(T)$.*
- *vi) Under the conditions of v), consider the $S$-morphism*

```text
ũ : 𝒞𝒯_G ⟶ 𝒞𝒯_{G′},    H ↦ H′ = u(H).
```

- *Then `ũ` is a quasi-compact faithfully flat morphism; if moreover `Ker u` is central, `ũ` is an isomorphism, the
  inverse isomorphism being $H' \mapsto u^{-1}(H')$.*

<!-- label: III.XV.7.1 -->

*Proof of ii).* For the first assertion, we may assume $S$ local artinian with closed point $s$. Let $H \in
\mathcal{CT}(S)$ and let $T_{s}$ be the maximal central torus of $H_{s}$, which is already defined over $\kappa(s)$ (cf.
3.4). Since $H_{s} \in \mathcal{CT}(s)$, one has $H_{s} = Centr_{G_{s}} T_{s}$. The group $H$ is smooth, so $T_{s}$
lifts uniquely to a sub-torus $T$ of $H$, central

<!-- original page 447 -->

in $H$ (Exp. IX 3.6 bis and Exp. IX 5.6). But then $H' = Centr_{G} T$ majorizes $H$ and has the same fiber as $H$; since
$H$ is flat over $S$, one has $H = H'$ (Exp. VI_B 2.5).

Suppose now that $S$ is the spectrum of a Henselian local ring, which one may assume noetherian by the usual reductions.
Denote by $s$ the closed point of $S$, $T_{s}$ the maximal central torus of $H_{s}$, $q$ an integer invertible on $S$,
$\ell$ a power of $q$, $T$ an $S$-torus having a closed fiber isomorphic to $T_{s}$ (Exp. X 4.6). Moreover, let
${}_{\ell }H$ be the "kernel" of the $\ell$-th power morphism in $H$, and let $U_{\ell}$ be the largest open subset of
${}_{\ell }H$ étale over $S$. It then follows from 1.3 and from the fact that $H$ is flat over $S$ that $U_{\ell}$
majorizes ${}_{\ell }T_{s}$. Since $S$ is Henselian, there exists a unique $S$-morphism

$$ u_{\ell} : {}_{\ell }T \longrightarrow U_{\ell} $$

which, on the closed fiber, induces the canonical immersion ${}_{\ell }T_{s} \to (U_{\ell})_{s}$. By uniqueness, one
easily sees that $u_{\ell}$ is an $S$-group morphism, central (Exp. IX 5.6 a)). Proceeding then as in 6.6 and 6.7, one
shows that $u_{\ell}$ is an immersion, and that if $M_{\ell}$ is the image group $u_{\ell}({}_{\ell }T)$, then
$Centr_{G}(M_{\ell})$ is equal to $H$ for $\ell$ large enough (this is where the noetherian hypothesis on $S$ is used).

*Proof of i).* The group $G$ is smooth over $S$ with connected fibers, so if $H \in \mathcal{CT}(S)$, $H$ has connected
fibers (Exp. XII 6.6 b)) and is equal to its connected normalizer (6.5), so that the functor $\mathcal{CT}$ defined in
7.1 i) coincides with the functor also denoted $\mathcal{CT}$ defined in 6.4.0. So, by Theorem 6.4, $\mathcal{CT}$ is
representable by an $S$-prescheme of finite presentation and quasi-projective over $S$. It remains to show that this
prescheme is smooth over $S$. One first reduces by EGA IV 8

<!-- original page 448 -->

to the case where $S$ is affine noetherian. Thanks to Exp. XI 1.5, it then suffices to prove that if $S$ is the spectrum
of a local artinian ring, $S_{0}$ a subscheme defined by a nilpotent ideal, $H_{0}$ an element of $\mathcal{CT}(S_{0})$,
then $H_{0}$ lifts to a subgroup prescheme $H$ of $G$, smooth over $S$. Now by ii), $H_{0} = Centr_{G_{0}} T_{0}$, where
$T_{0}$ is a sub-torus of $G_{0}$. Since $G$ is smooth, $T_{0}$ lifts to a sub-torus $T$ of $G$ (Exp. IX 3.6 bis), and
it suffices to take $H = Centr_{G}(T)$, which is indeed smooth over $S$ (Exp. XI 2.4 and Lemma 2.5).

*Proof of iii).* Since $H$ is smooth with connected fibers, by Exp. XI 6.11, $Transp_{G}(H, L)$ is representable by a
closed subprescheme of $G$ of finite presentation over $S$. To show that this transporter is smooth, one reduces, as
above, to proving that if $S$ is local artinian, $S_{0}$ a closed subprescheme of $S$, $g_{0} \in G(S_{0})$ such that
$int(g_{0})H_{0} \subset L_{0}$, then $g_{0}$ lifts to $g \in G(S)$ such that $int(g)H \subset L$. The group $G$ being
smooth over $S$, there exists a section $g_{1}$ of $G$ lifting $g_{0}$; let $H' = int(g_{1})H$. So this is an element of
$\mathcal{CT}(S)$ such that $H'_{0} \subset L_{0}$. By ii), $H'$ is the centralizer in $G$ of a torus $T'$ of $G$. Since
$L$ is smooth, the torus $T'_{0}$ of $L_{0}$ lifts to a torus $T''_{0}$ of $L$ (Exp. XI 3.6 bis). The group $Centr_{L}
T''_{0}$ is contained in $Centr_{G} T''_{0}$, has the same fiber as the latter (namely $H'_{0}$) and is smooth, so
equals $Centr_{G} T''_{0} = H'_{0}$. The sub-tori $T'$ and $T''_{0}$ of $G$ are two liftings of $T'_{0}$, so are
conjugate by an element $h$ of $G(S)$ reducing to the unit section of $G_{0}$ (Exp. IX 3.3 bis); the same is therefore
true of their centralizers $H'$ and $H''_{0}$ in $G$. The section $g = h g_{1}$ lifts $g_{0}$ and one has $int(g)H
\subset L$.

<!-- original page 449 -->

If now $g \in Transp_{G}(H, L)(S)$, for $int(g)H = L$ it is necessary and sufficient that for every $s \in S$, $\dim
H_{s} = \dim L_{s}$. It follows that if $U$ denotes the open-closed subprescheme of $S$ above which the fibers of $H$
have the same dimension as those of $L$, the strict transporter of $H$ in $L$, $Transp^{str}_{G}(H, L)$, is
representable by the $S$-prescheme

```text
U ×_S Transp_G(H, L).
```

*Proof of iv).* To see that if $H \in \mathcal{CT}(S)$, $H$ is closed in $G$, one may assume $S$ affine noetherian, then
$S$ spectrum of a complete local ring (EGA IV 8); but then $H$ is the centralizer in $G$ of a subgroup of multiplicative
type (by ii)), hence is closed since $G$ is separated over $S$ (Exp. VI_B 5.2).

By iii), `N = Norm_G(H) = Transp^{str}_G(H, H)` is representable by a subgroup prescheme smooth over $S$ and closed in
$G$. Consider the $S$-morphism

```text
G ⟶ 𝒞𝒯,    g ↦ int(g)H.
```

It follows from iii) that this morphism is smooth, so its image is an open subset $U$ of $\mathcal{CT}$. One then proves
as in Exp. XI 5.3 that $G/N$ is representable by $U$, hence in particular is quasi-projective.

Let us now study the quotient $N/H$. Thanks to EGA IV 8, to prove that $N/H$ is representable, one may assume $S$ affine
noetherian, then $S$ the spectrum of a local ring $A$, of finite (Krull[^N.D.E-XV-10]) dimension.

<!-- original page 450 -->

We shall proceed by increasing induction on the dimension of $S$. If $\dim S = 0$, the property follows from Exp. VI_A §
4\. Note now that if $N/H$ is representable, it is separated over $S$ (since $H$ is closed in $N$ by iv)), of finite
type and étale over $S$ (since $N$ is smooth over $S$, of finite type and $H$ is open in $N$), so $N/H$ is necessarily
quasi-affine over $S$ (SGA 1 VIII.6.2). By effective descent of quasi-affine schemes (*loc. cit.* 7.9), one may replace
$A$ by its completion, hence assume $S$ spectrum of a complete noetherian local ring. Let $s$ be its closed point and
`U = S \ s`. By induction hypothesis, $(N|_{U})/(H|_{U})$ is representable by a $U$-group $K$. Let then $T_{s}$ be the
maximal central torus of $H_{s}$, $q$ an integer invertible on $S$, $\ell$ a power of $q$, $M_{\ell}$ the unique central
subgroup of multiplicative type of $H$ lifting ${}_{\ell }T_{s}$ (cf. ii)). Choose $\ell$ large enough that
$Centr_{G}(M_{\ell}) = H$, and let $N' = Norm_{G}(M_{\ell})$. Since $Centr_{G}(M_{\ell}) = H$, one has $N' \subset
Norm_{G}(H)$. Moreover, one immediately verifies that $T_{s}$ (so also $(M_{\ell})_{s}$) is a characteristic subgroup of
$H_{s}$ (i.e. stable under $\operatorname{Aut}_{gr}(H_{s})$), so $N_{s}$ normalizes $(M_{\ell})_{s}$ and consequently
$N_{s} = N'_{s}$. The proof of Exp. XI 5.9 then shows that the quotient $N'/H = Norm_{G}(M_{\ell})/Centr_{G}(M_{\ell})$
is representable by an $S$-group $K'$. Since $N'$ is smooth over $S$ and $N'_{s} = N_{s}$, $N'$ is an open subgroup of
$N$ (Exp. VI_B 2.5) containing $H$, so the image of $N'|_{U}$ in $K$ is an open subgroup, isomorphic to $K'|_{U}$. Let
$L$ be the $S$-prescheme obtained by gluing $K$ and $K'$ along the previous isomorphism, and let $p$ be the $S$-morphism
$N \to L$ obtained by gluing the canonical projections $N|_{U} \to K$ and $N' \to K'$.

<!-- original page 451 -->

It is clear that $(L, p)$ represents the quotient $N/H$.

*Proof of v).* Suppose first that $S$ is the spectrum of a field $k$. The image $H'$ of $H$ is then a smooth subgroup of
$G'$. We must show that $H' \in \mathcal{CT}_{G'}(S)$, which will follow from the following more precise lemma:

**Lemma 7.2.** *Let $u : G \to G'$ be an epimorphism of smooth connected $k$-algebraic groups, $T$ a torus of $G$, $T'$
its image in $G'$. Then*

```text
u(Centr_G T) = Centr_{G′} T′.
```

<!-- label: III.XV.7.2 -->

Denote $H = Centr_{G} T$, $H' = Centr_{G'} T'$, $H'' = u(H)$. One has $H'' \subset H'$. To prove that $H' = H''$, one
may assume the base field algebraically closed, and it suffices to prove that every Cartan subgroup of $H'$ is contained
in $H''$. Indeed, $H''$ will then contain the open subset of regular points of $H'$, so $H''$ will be an open subgroup
of $H'$ and consequently will be equal to $H'$ since the latter has connected fibers. So let $C'$ be a Cartan subgroup
of $H'$; $C'$ is also a Cartan subgroup of $G'$, since $H'$ is the centralizer of a torus $T'$, hence has the same
reductive rank and the same nilpotent rank as $G'$. Set $K = (u^{-1}(C'))^{0}_{red}$. Since $T'$ is in the center of
$H'$, $C'$ contains $T'$, so $K$ contains $T$. Let then $C$ be a Cartan subgroup of $K$ containing $T$. The torus $T$ is
contained in the unique maximal torus of $C$, which is central in $C$ (Exp. XII 6.6 c)), so $C$ is contained in $H =
Centr_{G} T$. Using now the fact that any two Cartan subgroups of $G$ are conjugate and that the image of a Cartan
subgroup of $G$ is a Cartan subgroup of $G'$ (Exp. XII 6.6), one

<!-- original page 452 -->

deduces that $C$ is also a Cartan subgroup of $G$; its image is therefore a Cartan subgroup of $G'$; as it is contained
in $C'$, one has $u(C) = C'$, so $C'$ is indeed contained in $H''$.

We have therefore established v) when $S$ is the spectrum of a field $k$. Let us now study the general case. Since $G$,
$H$ and $G'$ are of finite presentation over $S$, to prove that $u(H)$ is representable and is an element of
$\mathcal{CT}_{G'}(S)$, one reduces by the usual technique to the case where $S$ is affine noetherian, then to the case
where $S$ is the spectrum of a local ring. By fpqc descent of subpreschemes of $G'$, one may even assume that $S$ is the
spectrum of a complete noetherian local ring $A$.

Let us resume the notation of ii), namely: let $T_{s}$ be the maximal central torus of $H_{s}$ ($s$ is the closed point
of $S$), $M_{\ell}$ a subgroup of multiplicative type of $H$ lifting ${}_{\ell }T_{s}$ such that $H = Centr_{G}
M_{\ell}$. Let $T'_{s}$ be the image of $T_{s}$ in $G'_{s}$. Since $G'$ is separated over $S$ (Exp. VI_B 5.2), the image
of $M_{\ell}$ by $u$ is a subgroup of multiplicative type $M'_{\ell}$ of $G'$ (Exp. IX 6.8). Set then $H' = Centr_{G'}
M'_{\ell}$, which is a smooth subgroup prescheme of $G'$. For every integer $\ell'$ equal to a power of $q$, there
exists $\ell$ such that $(M'_{\ell})_{s}$ majorizes ${}_{\ell'}T'_{s}$, so we may assume $\ell$ chosen large enough that
$H'_{s} = Centr_{G'_{s}} T'_{s} = u_{s}(H_{s})$, where the last equality follows from 7.2. The restriction of $u$ to
$H$, namely $v$, evidently factors through $H'$. Let us prove that $v : H \to H'$ is a flat morphism. Since $H$ and $H'$
are flat over $S$ and $H_{s} \to H'_{s}$ is flat, $v$ is flat on a neighborhood of $H_{s}$ (EGA IV 11.3.10 and 11.3.1).
The morphism $v$ is therefore flat on an open subgroup of $H$ (Exp. VI_B 2.2), so $v$ is flat, $H$ having connected
fibers.

<!-- original page 453 -->

The set-theoretic image of $H$ is therefore an open subset of $H'$ (necessarily equal to $(H')^{0}$) which, equipped
with its induced structure, represents the image sheaf $u(H)$ (for the fpqc topology). The fact that $u(H)$ is an
element of $\mathcal{CT}_{G'}(S)$ then follows from 7.2.

Suppose now that $H$ is the centralizer in $G$ of a torus $T$, and let $T'$ be the image of $T$ by $u$, which is a
sub-torus of $G'$ (Exp. IX 6.8). The image of $H$ by $u$ is contained in $Centr_{G'}(T')$, coincides fiber by fiber with
the latter (7.2), and is smooth over $S$, so $u(H) = Centr_{G'}(T')$.

*Proof of vi).* To show that `ũ` is a faithfully flat $S$-morphism, knowing that $\mathcal{CT}_{G}$ and
$\mathcal{CT}_{G'}$ are smooth over $S$ (by i)), it suffices to verify it on the geometric fibers. We are therefore
reduced to the case where $S$ is the spectrum of an algebraically closed field $k$. Let $H' \in \mathcal{CT}_{G'}(k)$,
$T'$ its maximal central torus, $T$ a sub-torus of $G$ whose image is $T'$, $H = Centr_{G}(T)$, so that $H' = u(H)$
(7.2), $N = Norm_{G}(H)$, $N' = Norm_{G'}(H')$. We have shown in iv) that $G/N$ (resp. $G'/N'$) canonically identifies
with open neighborhoods of $H$ in $\mathcal{CT}_{G}$

<!-- original page 454 -->

(resp. of $H'$ in $\mathcal{CT}_{G'}$). Under these identifications, the restriction of `ũ` to $G/N$ coincides with the
natural morphism

$$ w : G/N \longrightarrow G'/N' $$

deduced from $u$ by passage to the quotient. Now $w$ is an epimorphism of homogeneous spaces under $G$, hence is
faithfully flat. This proves that `ũ` is a flat morphism such that $\tilde{u}(\mathcal{CT}_{G})$, which is therefore an
open subset of $\mathcal{CT}_{G'}$, contains every point of $\mathcal{CT}_{G'}(k)$. Since $\mathcal{CT}_{G'}$ is of
finite type over $k$, one deduces that `ũ` is surjective, hence faithfully flat.

The complementary assertions contained in vi) in the case where `Ker u` is central follow from Exp. XII 7.12.

The following theorem generalizes Theorem 7.1 of Exp. XII:

**Theorem 7.3.** *Let $S$ be a prescheme, $G$ an $S$-prescheme in groups of finite presentation over $S$, smooth, with
connected fibers, and consider the $S$-functor $\mathcal{C} : (Sch/S)^{\circ} \to Ens$ such that:*

> *$\mathcal{C}(S')$ = set of Cartan subgroups of $G_{S'}$.*

- *i) The following conditions are equivalent:*
    - *a) The functor $\mathcal{C}$ is representable.*
    - *b) The functor $\mathcal{C}$ is representable by an $S$-prescheme, smooth, quasi-projective, of finite
      presentation over $S$, with affine fibers.*
    - *c) The group $G$ admits locally for the étale topology a Cartan subgroup.*
    - *d) The group $G$ admits locally for the faithfully flat topology a Cartan subgroup.*
    - *e) The nilpotent rank of the fibers of $G$ is a locally constant function on $S$.*
- *ii) If the preceding conditions hold, any two Cartan subgroups of $G$ are locally conjugate for the étale topology.*

<!-- original page 455 -->

*The set of regular points of the fibers of $G$ (Exp. XIII 2.7) is an open subset $G_{reg}$, of finite presentation over
$S$, and every section of $G_{reg}$ over $S$ is contained in a unique Cartan subgroup of $G$.*

- *iii) Let $G'$ be an $S$-prescheme in groups of finite presentation over $S$ and $u : G \to G'$ a faithfully flat
  $S$-group morphism, so that $G'$ is smooth over $S$ with connected fibers. Then if $C$ is a Cartan subgroup of $G$,
  $u(C) = C'$ is representable by a Cartan subgroup of $G'$, and $C \to C'$ is faithfully flat.*
- *iv) Under the conditions of i) and iii) the morphism*

```text
ũ : 𝒞_G ⟶ 𝒞_{G′},    C ↦ u(C) = C′
```

*is faithfully flat. If moreover $Ker(u)$ is central, `ũ` is an isomorphism.*

- *v) For any complementary information concerning the transporters, or the relations with maximal tori, one may consult
  7.1 and Exp. XII 7.1.*

<!-- label: III.XV.7.3 -->

*Proof.* i) We shall show that b) ⇒ c) ⇒ d) ⇒ e) ⇒ b) ⇒ a) ⇒ d).

b) ⇒ c). Let $s$ be a point of $S$. Since $C_{s}$ is smooth over $\kappa(s)$, there exist points of $C_{s}$ whose
residue field is a finite separable extension of $\kappa(s)$. Applying Exp. XI 1.10, one sees that there exist an open
neighborhood $U$ of $s$ and an étale surjective morphism

<!-- original page 456 -->

$U' \to U$ such that $G_{U'}$ admits a Cartan subgroup.

c) ⇒ d) is clear.

d) ⇒ e). Let $s \in S$. By hypothesis, there exists an $S$-prescheme $S'$, flat over $S$, whose image contains $s$, such
that $G_{S'}$ admits a Cartan subgroup. Let $s'$ be a point of $S'$ above $s$. The nilpotent rank of the fibers of
$G_{S'}$ is therefore constant on $\operatorname{Spec} \mathcal{O}_{S', s'}$, and consequently the nilpotent rank of the
fibers of $G$ is constant on $\operatorname{Spec} \mathcal{O}_{S, s}$ which is the image of $\operatorname{Spec}
\mathcal{O}_{S', s'}$ (EGA IV 2.3.4 ii)). Let $r$ be its value. It follows from 6.3 bis that the set $E_{r}$ of points
$x$ of $S$ such that the nilpotent rank of $G_{x}$ equals $r$ is an ind-constructible part of $S$, hence contains a
neighborhood of $s$ (EGA IV 1.10.1).

e) ⇒ b). The assertion is local on $S$, so one may assume that the nilpotent rank of the fibers of $G$ is constant and
equal to $r$. For every $S$-prescheme $S'$ there is then identity between the Cartan subgroups of $G_{S'}$ and the
subgroup preschemes of $G_{S'}$ smooth over $S'$ of relative dimension $r$, whose geometric fibers are centralizers of a
torus. Since $\mathcal{CT}$ is representable by 7.1, $\mathcal{C}$ is representable by the open-closed subprescheme of
$\mathcal{CT}$ representing the subfunctor of $\mathcal{CT}$ consisting of groups of relative dimension $r$. The other
assertions in b) are contained in 7.1 i), except for the fact that the fibers of $\mathcal{C}$ are affine, which itself
follows from Exp. XII 7.1 d).

It is clear that b) ⇒ a). Let us show that a) ⇒ d). It follows from 6.2 iii) that the functor $\mathcal{C}$

<!-- original page 457 -->

commutes with filtered inductive limits of rings, so if $\mathcal{C}$ is representable, it is necessarily representable
by an $S$-prescheme locally of finite presentation (EGA IV 8.14.2). To prove that $\mathcal{C}$ is smooth over $S$, one
is reduced to showing that if $S$ is affine and if $S_{0}$ is the closed subscheme defined by a nilpotent ideal $J$,
then every Cartan subgroup $C_{0}$ of $G_{0} = G \times_{S} S_{0}$ lifts to a Cartan subgroup $C$ of $G$. But the
existence of $C_{0}$ entails that condition e) is satisfied for $S_{0}$, hence for $S$ which has the same underlying
space, and one concludes from the fact that d) ⇒ b). Since $\mathcal{C}$ is smooth over $S$ and $\mathcal{C} \to S$ is
surjective, one sees that a) ⇒ d).

ii) Let $C$ and $C'$ be two Cartan subgroups of $G$. Then $Transp_{G}(C, C')$ is representable by a prescheme smooth
over $S$ (7.1 iii)) with non-empty fibers (cf. Exp. XII 6.6 a) and c)). The fact that $C$ and $C'$ are locally conjugate
for the étale topology is then a consequence of Hensel's lemma (Exp. XI 1.10).

The other assertions of ii) are consequences of XIII 3.1 and XIII 3.2, in view of i).

iii) Let $C$ be a Cartan subgroup of $G$. One knows (7.1 v)) that $u(C)$ is representable by a smooth subgroup $C'$ of
$G'$. Since the fibers of $C'$ are Cartan subgroups of the fibers of $G'$ (Exp. XII 6.6 d)), $C'$ is a Cartan subgroup
of $G'$.

iv) To prove that the morphism `ũ` is faithfully flat, one proceeds as in 7.1 vi).

If now `Ker u` is central and $C'$ is a Cartan subgroup of $G'$,

<!-- original page 458 -->

$u^{-1}(C') = C$ is smooth, with connected fibers (7.1 vi)) and its fibers are Cartan subgroups (Exp. XII 6.6 f)), so
$C$ is a Cartan subgroup of $G$, which completes the proof of iv), in view of 7.1 vi).

## 8. Representability criterion for the functor of sub-tori of a smooth group

<!-- label: III.XV.8 -->

<!-- original page 459 -->

**8.0.** In this section, if $S$ is a prescheme and $G$ an $S$-prescheme in groups, $\mathcal{T}_{G}$ (or simply
$\mathcal{T}$ if there is no ambiguity) denotes the $S$-functor $(Sch/S)^{\circ} \to Ens$ such that, for every
$S$-prescheme $S'$, one has

> *$\mathcal{T}(S')$ = set of sub-tori of $G_{S'}$.*

One similarly defines $\mathcal{T}_{C}$ as the functor of central sub-tori of $G$.

**Proposition 8.1.** *Let $S$ be a locally noetherian prescheme and $G$ an $S$-prescheme in groups of finite type. Then
the following conditions are equivalent:*

- *i) The functor $\mathcal{T}_{G}$ "commutes with adic limits of local artinian rings", i.e. for every $S$-prescheme of
  the form $\operatorname{Spec}(A) = S'$, where $A$ is a complete noetherian local ring for the topology defined by its
  maximal ideal $\mathfrak{m}$, the canonical map*

```text
𝒯(S′) ⟶ lim_{←n} 𝒯(S′_n)    (where S′_n = Spec(A/𝔪ⁿ))
```

*is bijective.*

- *ii) As in i) but restricted to the case where $A$ is a complete discrete valuation ring with algebraically closed
  residue field.*
- *iii) As in ii), but one restricts to the subfunctor $\mathcal{T}^{(1)}$ of $\mathcal{T}$ relative to sub-tori of $G$
  of relative dimension `1`.*

<!-- original page 460 -->

- *i bis) For every $S$-prescheme $S'$ as in i) and every $S'$-torus $T$, the canonical map*

```text
Hom_{S′-gr}(T, G_{S′}) ⟶ lim_{←n} Hom_{S′_n-gr}(T_{S′_n}, G_{S′_n})
```

*is bijective.*

- *ii bis) As i bis), but one restricts to the case where $A$ is a complete discrete valuation ring with algebraically
  closed residue field.*
- *iii bis) As ii bis), but one restricts to the case where $T$ is the multiplicative group $G_{m}$.*

<!-- label: III.XV.8.1 -->

**Remark 8.2.** One has an analogous proposition restricting to central sub-tori of $G$ and to central homomorphisms of
a torus into $G$.

<!-- label: III.XV.8.2 -->

*Proof.* We shall use the following lemma:

**Lemma 8.3.** *Let $S$ be a prescheme, $G$ an $S$-prescheme in groups, $T$ an $S$-torus, $u : T \to G$ an $S$-group
morphism. Assume in addition that $G$ is of finite presentation over $S$, or else that $S$ is locally noetherian and $G$
locally of finite type. Then:*

- *a) `Ker u` is a subgroup of multiplicative type of $T$.*
- *b) The quotient $T' = T/Ker u$ is a torus.*
- *c) The canonical monomorphism $T' \to G$ deduced from $u$ by passage to the quotient is an immersion.*

<!-- label: III.XV.8.3 -->

<!-- original page 461 -->

This lemma is a consequence of Exp. IX 6.8 when $G$ is separated over $S$. In the general case, one reduces as usual to
the case where $S$ is noetherian. Let us first show that $K = Ker u$ is flat. We may assume that $S$ is the spectrum of
a local artinian ring (EGA 0_III 10.2.6), in which case $G$ is separated (Exp. VI_B 5.2), so $K$ is of multiplicative
type (Exp. IX 6.8) and *a fortiori* flat over $S$. Let us now prove that `Ker u` is closed in $T$, which reduces us to
the case where $S$ is the spectrum of a discrete valuation ring (EGA II 7.2.1). Since $T$ is flat with connected fibers,
$u$ factors through the connected component of the schematic closure in $G$ of the generic fiber of $G$. We may
therefore assume $G$ flat with connected fibers, but then $G$ is separated (Exp. VI_B 5.2), so $K$ is closed. This being
so, it follows from Exp. X 4.8 b) that $K$ is a subgroup of multiplicative type of $T$. The quotient $T' = T/K$ is then
representable and $T'$ is a group of multiplicative type (Exp. IX 2.7) whose fibers are tori, so it is a torus. The fact
that the monomorphism $T' \to G$ is an immersion then follows from Exp. VIII 7.9.

*Proof of 8.1.* i) ⇒ i bis). Set $T_{n} = T_{S'_{n}}$, $G_{n} = G_{S'_{n}}$, and let $(u_{n})_{n \in \mathbb{N}}$ be an
element of `lim_{←n} Hom_{S′_n-gr}(T_n, G_n)`. For every integer $n$, $u_{n}(T_{n})$ is therefore a sub-torus $T'_{n}$
of $G_{n}$ (Lemma 8.3). By hypothesis, there exists a unique sub-torus $T'$ of $G$ lifting $T'_{n}$ for every $n$. Since
$T'$ has affine fibers, one concludes thanks to 4.4.

i bis) ⇒ i). Let $(T_{n})_{n \in \mathbb{N}}$ be an element of `lim_{←n} 𝒯(S_n)`. By Exp. X 4.6,

<!-- original page 462 -->

there exist an $S'$-torus $T^{0}$ and an $S'_{0}$-isomorphism $u_{0} : T^{0}_{0} \xrightarrow{\sim} T_{0}$. Since
$T_{n}$ is smooth over $S'_{n}$, $u_{0}$ lifts to an $S'_{n}$-morphism $u_{n} : T^{0}_{n} \to T_{n}$ (Exp. IX 3.6), and
one may assume the family $(u_{n})_{n \in \mathbb{N}}$ coherent, hence coming from a morphism $u : T^{0} \to G$. The
image of $T^{0}$ by $u$ is then a sub-torus of $G$ (Lemma 8.3) lifting $T_{n}$ for every $n$.

The implications i) ⇒ ii) ⇒ iii) on the one hand, and i bis) ⇒ ii bis) ⇒ iii bis) on the other, are evident. The
implication iii) ⇒ iii bis) is proved as i) ⇒ i bis). It therefore suffices to prove: iii bis) ⇒ ii bis) ⇒ i bis).

ii bis) ⇒ i bis). With the terminology introduced in 4.3, assertion i bis) is true if and only if every element
$(u_{n})_{n \in \mathbb{N}}$ of `lim_{←n} Hom_{S_n-gr}(T_n, G_n)` is "admissible". For every point $t$ of $S'$ distinct
from the closed point $s$ of $S'$, there exists an $S$-scheme $S''$, spectrum of a complete discrete valuation ring with
algebraically closed residue field, whose generic point projects to $t$ and whose closed point projects to $s$ (EGA II
7.1.9). One immediately deduces a valuative criterion for a family of morphisms to be admissible. This says that ii bis)
⇒ i bis).

iii bis) ⇒ ii bis). Let $T$ be an $S$-torus, where $S$ is the spectrum of a complete discrete valuation ring with
algebraically closed residue field. The torus $T$ is then trivial (Exp. X 4.6), i.e. isomorphic to $(G_{m, S})^{r}$ for
a suitable integer $r$. Let $(u_{n})_{n \in \mathbb{N}}$ be an element of `lim_{←n} Hom_{S_n-gr}((G_m)ʳ_{S_n}, G_n)`. By
hypothesis, the restrictions of $u_{n}$ to each

<!-- original page 463 -->

factor of $(G_{m})^{r}_{S}$ come from a group morphism $G_{m, S} \to G$. Whence a product morphism $(G_{m})^{r}_{S} \to
G^{r}$ which, composed with the morphism $G^{r} \to G$ defined by the composition law in $G$, gives a morphism

$$ v : (G_{m})^{r}_{S} \longrightarrow G. $$

Given the existence of the group morphism $u_{n}$, it is clear that $u_{n} = v_{n}$. It remains to see that $v$ is a
group morphism, which translates into the fact that two obvious morphisms $f, g : X = (G_{m})^{r}_{S} \times_{S}
(G_{m})^{r}_{S} \to G$ coincide. Let $Z$ be the subscheme of coincidences of $f$ and $g$. Since $(G_{m})^{r}_{S}$ has
connected fibers and $v((G_{m})^{r}_{S})$ contains the unit section, one sees as in 8.3 that $v$ factors through the
connected component of $G$, which allows us to assume $G$ separated (Exp. VI_B 5.2), so $Z$ is closed. On the other
hand, since $v_{n}$ is a group morphism, one has $f_{n} = g_{n}$ for every $n$, so $Z$ contains a neighborhood of the
closed fiber of $X$ (EGA I 10.9.4), hence is schematically dense in $X$, $X$ having smooth and irreducible fibers (Exp.
IX 4.6), and consequently $Z = X$, so $f = g$.

**Definition 8.4.** *Let $S$ be a locally noetherian prescheme, $G$ an $S$-prescheme in groups of finite type, and
$\mathcal{S}$ the set of $S$-schemes $S'$, spectrum of a complete discrete valuation ring with algebraically closed
residue field, of closed point $s$, of generic point $t$,*

<!-- original page 464 -->

*such that $(G_{t})^{0}_{red}$ is smooth and admits a Chevalley decomposition, i.e. is an extension of an abelian
variety by a smooth, connected linear algebraic subgroup $L_{t}$ (this decomposition is then unique). If $S' \in
\mathcal{S}$, denote by $G'$ (resp. $L$) the schematic closure in $G_{S'}$ of $G_{t}$ (resp. $L_{t}$).*

*Under these conditions, we shall say that*

> *"the abelian part of $G$ does not degenerate into a toric part", or more briefly that $G$ satisfies property AT,*

*if for every $S' \in \mathcal{S}$, $L_{s}$ has the same reductive rank as $G'_{s}$. (Intuitively, suppose that the
quotient $A = G'/L$ is representable, in which case $A$ is a flat group prescheme such that $(A_{t})^{0}_{red}$ is an
abelian variety. The condition "AT" then means that $A_{s}$ has reductive rank zero, hence $(A_{s})^{0}_{red}$ is an
extension of an abelian variety by a unipotent group.)*

*Similarly, assuming in addition $G$ has connected fibers, we shall say that*

> *$G$ satisfies property ATC*

*if for every $S' \in \mathcal{S}$, the schematic closure $Z$ of the center $Z_{t}$ of $G_{t}$ satisfies AT.*

<!-- label: III.XV.8.4 -->

These technical definitions are justified by the following proposition:

**Proposition 8.5.** *Let $S$ be a locally noetherian prescheme, $G$ an $S$-prescheme in groups of finite type. Then:*

- *a) For the functor $\mathcal{T}$ of sub-tori of $G$ to "commute with adic limits of local artinian rings" (cf. 8.1),
  it is necessary and sufficient that $G$ satisfy property AT (8.4).*
- *b) If $G$ has connected fibers, for the functor $\mathcal{T}_{C}$ of central sub-tori of $G$ to commute with adic
  limits of local artinian rings,*

<!-- original page 465 -->

*it is necessary and sufficient that $G$ satisfy property ATC (8.4).*

<!-- label: III.XV.8.5 -->

We shall need the following technical lemma:

**Lemma 8.6.** *Let $S$ be the spectrum of a discrete valuation ring, $s$ the closed point of $S$, $G$ an $S$-prescheme
in groups, flat and of finite type, $T_{s}$ a sub-torus of $G_{s}$. Then there exists an $S$-scheme $S'$, spectrum of a
discrete valuation ring faithfully flat over $S$, with closed point $s'$, and a subgroup scheme $C$ of $G_{S'}$, flat
over $S'$, commutative, with connected fibers, such that $C_{s}'$ majorizes $T_{s} \times_{s} s'$.*

<!-- label: III.XV.8.6 -->

Possibly replacing $S$ by $S'$, spectrum of a discrete valuation ring faithfully flat over $S$, we may assume that
$T_{s}$ is equal to $(G_{m})^{r}_{s}$ and that the transcendence degree of $\kappa(s)$ over the prime field is
$\geqslant r$ (EGA 0_III 10.3.1 and EGA II 7.1.9). There then exists an element $x$ of $T_{s}(s)$ such that every
algebraic subgroup of $G_{s}$ "containing" $x$ majorizes $T_{s}$ (cf. Exp. XIII proof of 2.1 (ii) ⇒ (vii)). Since $G$ is
flat over $S$, a quasi-section passes through $x$ (EGA IV 14.5.8), and consequently, possibly replacing $S$ by the
spectrum of a discrete valuation ring faithfully flat over $S$, one may assume that there exists a section $\tilde{x}$
of $G$ above $S$ lifting $x$. Let $C_{t}$ be the commutative algebraic subgroup of $G_{t}$ generated by $\tilde{x}_{t}$
(Exp. VI_B 7), and let $C$ be the schematic closure of $C_{t}$ in $G$. It is clear that $C_{s}$ contains $x$, hence
majorizes $T_{s}$, and consequently, the "connected component" of $C$ will be a flat and commutative group scheme
answering the question.

*Proof of 8.5 a).* <!-- original page 466 --> Suppose the functor $\mathcal{T}$ commutes with adic limits of artinian
rings and let us show that $G$ satisfies property AT. Let then $S' \in \mathcal{S}$, and let $T_{s}$ be a maximal torus
of $G'_{s}$. We must prove that $T_{s}$ is contained in $L_{s}$. The formation of $L$ and $G'$ evidently commutes with
faithfully flat extensions $S'' \to S'$ of discrete valuation rings. Possibly changing $S'$, we may therefore, by Lemma
8.6, assume that there exists a subgroup scheme $C$ of $G'_{S'}$, flat and commutative, such that $C_{s}$ majorizes
$T_{s}$. But then $T_{s}$ is a central sub-torus of $C_{s}$, and consequently lifts infinitesimally to a central
sub-torus (Cor. 2.3). Given the hypothesis made on $G$, $T_{s}$ lifts to a sub-torus $T$ of $G$. Evidently $T_{t}$ is
contained in the linear component $L_{t}$ of $G_{t}$, so $T$ is contained in $L$.

Suppose now that $G$ satisfies property AT, and let us show that condition 8.1 iii bis) is verified. Let then $S$ be the
spectrum of a complete discrete valuation ring $A$ with algebraically closed residue field, $\mathfrak{m}$ the maximal
ideal of $A$, $S_{n} = \operatorname{Spec}(A/\mathfrak{m}^{n})$, $u_{n}$, $n \in \mathbb{N}$, a coherent system of group
morphisms $u_{n} : (G_{m, S})_{n} \to G_{n} = G \times_{S} S_{n}$. Let $q$ be a prime number invertible on $S$. The
integer $\ell$ ranging over the powers of $q$, there exists a unique $S$-group morphism

```text
_ℓu : _ℓ G_{m, S} ⟶ G
```

lifting $u_{n}|_{{}_{\ell}(G_{m, S})_{n}}$ for every $n$ (Prop. 1.6 a)). Consequently, if there exists an $S$-group
morphism $u : G_{m, S} \to T$ lifting $u_{n}$ for every $n$, its restriction to ${}_{\ell} G_{m, S}$ is uniquely
determined. By the density theorem (Exp. IX 4.8 (a)), this proves

<!-- original page 467 -->

the uniqueness of $u$ and the fact that to prove the existence of $u$, we may allow a faithfully flat extension of the
base. Now $(G_{t})^{0}_{red}$ admits a Chevalley decomposition, and this is already defined over a finite extension $L$
of the field of fractions $K$ of $A$. Possibly replacing $S$ by the normalization of $S$ in $L$, we may therefore assume
$S \in \mathcal{S}$. The morphism ${}_{\ell }u_{t}$ factors through $(G_{t})_{red}$, so ${}_{\ell }u$ factors through
the schematic closure $G''$ of $(G_{t})_{red}$ in $G'$. Still by the density theorem, one deduces that $u_{n}$ factors
through $G''_{n}$ for every $n$. Since $G$ has property AT, every sub-torus of $G'_{s}$, and *a fortiori* of $G''_{s}$,
is contained in $L_{s}$, so $u_{s}$ factors through $L_{s}$. I claim that for every $n$, $u_{n}$ factors through
$L_{n}$. Indeed, since $L_{t}$ is invariant in $(G'')_{t}$, $L$ is invariant in $G''$; on the other hand, $L$ is flat
over $S$, so for every integer $n$, the quotient $H_{n} = G''_{n}/L_{n}$ is representable (Exp. VI_A § 4). The image of
$(G_{m, S})_{n}$ in $H_{n}$ is a sub-torus of $H_{n}$ (Exp. IX 6.8) whose closed fiber is zero, so this image is zero
and consequently $u_{n}$ factors through $L_{n}$. But since $L_{t}$ is affine, one deduces that the family $u_{n}$ is
admissible (Prop. 4.3), which completes the proof.

The proof of 8.5 b) is entirely analogous to that of 8.5 a), in view of 8.2 and Exp. IX 5.6 a).

**Proposition 8.7.** *Let $S$ be a locally noetherian prescheme, $G$ an $S$-prescheme in groups of finite type. Then:*

<!-- original page 468 -->

- *i) If $G$ has connected fibers and satisfies AT, it satisfies ATC.*
- *ii) If $G$ satisfies AT, every subgroup prescheme of $G$ satisfies AT.*
- *iii) If $G$ is flat over $S$ and the abelian rank of the fibers of $G$ is a locally constant function on $S$, then
  $G$ satisfies AT.*

<!-- label: III.XV.8.7 -->

i) follows immediately from 8.5 and Exp. IX 5.6 a).

ii) Let $H$ be a subgroup prescheme of $G$. To prove that $H$ satisfies property AT, we may assume that $S$ is the
spectrum of a complete discrete valuation ring and we must show that every coherent family of $S_{n}$-group morphisms

```text
u_n : (G_{m, S})_n ⟶ H_n
```

is admissible (8.5 and 8.1 iii bis)). Now by hypothesis, $G$ satisfies property AT, so there exists an $S$-group
morphism

$$ u : (G_{m})_{S} \longrightarrow G $$

lifting $u_{n}$ for every $n$. Proceeding as in the proof of 8.5, one sees that $u|_{{}_{\ell} G_{m, S}}$ (where $\ell$
ranges over the powers of a prime $q$ invertible on $S$) factors through $H$. By density, one deduces that on the
generic fiber, $u_{t}$ factors through $H_{t}$. Since $(G_{m})_{S}$ is reduced, it indeed follows that $u$ factors
through $H$.

iii) Let $S' \in \mathcal{S}$ (notation of 8.4). <!-- original page 469 --> The group $L$ is flat over $S$, its generic
fiber $L_{t}$ is affine; under these conditions, one can show that $L_{s}$ is necessarily affine (XVII App. III, 2).
Since $G$ and $L$ are flat, one has $G = G'$ and the dimension of the fibers of $G$ and $L$ is constant on $S$ (Exp.
VI_B 4), so that one has the inequalities:

```text
abelian rank Gₛ ⩽ dim Gₛ − dim Lₛ = dim G_t − dim L_t = abelian rank G_t.
```

The hypothesis entails that these inequalities are equalities. It follows that $(G_{s}/L_{s})^{0}_{red}$ is an abelian
variety, hence has reductive rank zero, and consequently $L_{s}$ has the same reductive rank as $G_{s}$.

We are now in a position to prove the main theorems of this section:

**Theorem 8.8.** *Let $G$ be a group prescheme of finite type over a locally noetherian prescheme $S$. Suppose $G$ flat
over $S$ with connected fibers. Then:*

- *a) For the functor $\mathcal{T}_{C}$ of central sub-tori of $G$ to be representable, it is necessary and sufficient
  that $G$ have property ATC (8.4). Moreover, in this case, $\mathcal{T}_{C}$ is representable by an $S$-prescheme étale
  and separated over $S$.*
- *b) Under the conditions of a), for every $S$-torus $T$, the functor $\operatorname{Hom}^{cent}_{S-gr}(T, G)$ of
  central homomorphisms of $T$ into $G$ is representable by an $S$-prescheme étale and separated over $S$.*

<!-- label: III.XV.8.8 -->

**Theorem 8.9.** *Let $S$ be a locally noetherian prescheme and $G$ an $S$-prescheme in groups of finite type, smooth
over $S$.*

- *a) For the functor $\mathcal{T}$ of sub-tori of $G$ to be representable, it is necessary and sufficient*

<!-- original page 470 -->

*that $G$ have property AT (8.4). Moreover, in this case, $\mathcal{T}$ is representable by an $S$-prescheme smooth and
separated over $S$; more precisely, the structural morphism $\mathcal{T} \to S$ admits a canonical factorization*

```text
𝒯 ──u──→ Y ──v──→ S,
```

*where $v$ is a smooth and quasi-projective morphism (hence of finite type) and $u$ is an étale separated morphism.*

- *b) Under the conditions of a), for every $S$-torus $T$, the functor $\operatorname{Hom}_{S-gr}(T, G)$ of
  homomorphisms of $T$ into $G$ is representable by an $S$-prescheme smooth and separated over $S$.*

<!-- label: III.XV.8.9 -->

*Proof of 8.8 a).* If the functor $\mathcal{T}_{C}$ is representable, it commutes with adic limits of artinian rings,
and consequently (8.2 and 8.5 b)) $G$ has property ATC. To establish the converse, we shall use the following result,
which will be proved in EGA VI, and is also found in Murre's exposé: Sém. Bourbaki, May 1965, N° 294, Theorem 1,
corollary 2.

**Lemma 8.10.** *Let $S$ be a locally noetherian prescheme and $F$ a contravariant functor defined on $Sch/S$ with
values in the category of sets. For $F$ to be representable by an étale separated $S$-prescheme, it is (necessary and)
sufficient that $F$ satisfy the following five properties:*

- *i) $F$ is a sheaf for the fpqc topology (Exp. IV).*

<!-- original page 471 -->

- *ii) $F$ commutes with inductive limits of rings (Exp. XI 3.2).*
- *iii) $F$ commutes with adic limits of local artinian rings (8.1 i)).*
- *iv) $F$ satisfies the "valuative criterion of separation", i.e. for every $S$-scheme $S'$ which is the spectrum of a
  discrete valuation ring with generic point $t$, the canonical map $F(S') \to F(t)$ is injective.*
- *v) $F$ is infinitesimally étale (Exp. XI 1.8).*

<!-- label: III.XV.8.10 -->

Let us show that the functor $\mathcal{T}_{C}$ of 8.8 satisfies the five conditions of 8.10.

i) The functor $\mathcal{T}$ (resp. $\mathcal{T}_{C}$) is a sheaf for the fpqc topology as soon as $G$ is of finite
presentation over $S$. Indeed, every monomorphism of a torus into $G$ is then an immersion (Exp. VIII 7.9), and the
property follows from fpqc descent of subpreschemes.

ii) Corollary 6.3 proves that the functor $\mathcal{T}$ commutes with inductive limits of rings if $G$ is of finite
presentation over $S$; one immediately deduces that the same is true of $\mathcal{T}_{C}$.

iii) By 8.5, condition iii) is precisely equivalent to property ATC.

iv) follows simply from the fact that if $S$ is the spectrum of a discrete valuation ring, two sub-tori of $G$ having
the same generic fiber coincide

<!-- original page 472 -->

and more precisely coincide with the connected component of the schematic closure in $G$ of their generic fiber.

v) follows from 2.3 since $G$ is flat over $S$.

*Proof of 8.8 b).* Proceeding as in Exp. XI 4.2, one sees that it suffices to prove that the product group $T \times_{S}
G$ again satisfies property ATC, which is immediate from the definition.

*Proof of 8.9 a).* Possibly replacing $G$ by its connected component (Exp. VI_B 3.10), we may assume $G$ has connected
fibers. If $T$ is a sub-torus of $G$, its centralizer $Centr_{G}(T)$ is then representable (Exp. XI 6.11) by a subgroup
prescheme of $G$, smooth over $S$ (Exp. XI 2.4), with connected fibers (Exp. XII 6.6 b)), hence is an element of
$\mathcal{CT}(S)$, where $\mathcal{CT}$ is the functor defined in 7.1 i). It is clear that the map

$$ T \mapsto Centr_{G}(T) $$

defines an $S$-morphism

$$ u : \mathcal{T} \longrightarrow \mathcal{CT}. $$

Since $\mathcal{CT}$ is representable by an $S$-prescheme smooth and quasi-projective over $S$ (7.1 i)), it suffices to
prove that the morphism $u$ is representable by a separated and étale morphism.

After a suitable base change $S' \to S$ (with $S' = \mathcal{CT}$, hence $S'$ locally noetherian),

<!-- original page 473 -->

we are reduced to the following problem: let $S$ be a locally noetherian prescheme, $G$ an $S$-prescheme in groups,
smooth and of finite type over $S$, with connected fibers, $H$ a subgroup of $G$, smooth over $S$ with connected fibers.
Consider the subfunctor $X$ of $\mathcal{T}_{C, H}$ such that, for every $S$-prescheme $S'$, $X(S')$ is the set of
central sub-tori $T$ of $H_{S'}$ such that $Centr_{G_{S'}}(T) = H_{S'}$. We shall show that $X$ is representable by an
$S$-prescheme étale and separated over $S$.

Indeed, by hypothesis, $G$ satisfies property AT, hence so does $H$ (8.7 ii)); and since $H$ has connected fibers, $H$
also satisfies property ATC (8.7 i)). On the other hand $H$ is smooth over $S$, hence flat. By 8.8 a), $\mathcal{T}_{C,
H}$ is representable by an $S$-prescheme étale and separated over $S$. It then suffices to show that the canonical
monomorphism $X \to \mathcal{T}_{C, H}$ is representable by an open immersion.

Set $S' = \mathcal{T}_{C, H}$ and let $K$ be the centralizer in $G_{S'}$ of the "universal" central torus of $H_{S'}$.
The group $K$ is a smooth group scheme over $S'$ with connected fibers, majorizing $H_{S'}$. By definition, $X =
\prod_{K/S'} H_{S'}/K$, which is indeed representable by the open-closed subprescheme of $S'$ above which $H_{S'}$ and
$K$ have the same relative dimension.

One proves 8.9 b) analogously to 8.8 b).

**Corollary 8.11.** *Let $S$ be a prescheme, $G$ an $S$-prescheme in groups smooth over $S$ and of finite presentation.
Then, if the abelian rank of the fibers of $G$ is a locally constant function on $S$ (in particular if the fibers of $G$
are affine), the functor*

<!-- original page 474 -->

*of sub-tori of $G$ is representable by an $S$-prescheme, smooth and separated over $S$, and the same is true of the
functor $\operatorname{Hom}_{S-gr}(T, G)$ for every $S$-torus $T$.*

<!-- label: III.XV.8.11 -->

Indeed, the assertion is local on $S$, so we may assume $S$ affine and the abelian rank of the fibers of $G$ constant.
One may then find (Exp. VI_B § 10) a noetherian affine scheme $S_{0}$ and an $S_{0}$-prescheme in groups $G_{0}$, smooth
and of finite type over $S_{0}$, such that $G$ is $S$-isomorphic to $G_{0} \times_{S_{0}} S$. Moreover, the abelian rank
of the fibers of an $S$-prescheme in groups of finite presentation over $S$ is an ind-constructible function (6.3 bis).
By a standard argument (EGA IV 8), one concludes that in the present case, one may assume the abelian rank of the fibers
of $G_{0}$ constant on $S_{0}$. But then $G_{0}$ has property AT (8.7 iii)), and consequently (8.10) the functor of
sub-tori of $G_{0}$ is representable by an $S_{0}$-prescheme smooth and separated over $S_{0}$, whence the announced
property for $G$. As for the functor $\operatorname{Hom}_{S-gr}(T, G)$, one proceeds analogously.

**Generalization of 8.9.**

The functor $\mathcal{T}$ of sub-tori of a smooth group $G$ not being necessarily representable, we shall state
sufficient conditions for a subfunctor of $\mathcal{T}$ to be representable.

**Proposition 8.12.** *Let $S$ be a locally noetherian prescheme, $G$ an $S$-prescheme in groups, smooth over $S$, with
connected fibers, and $F$ an $S$-subfunctor of the functor $\mathcal{T}$ of*

<!-- original page 475 -->

*sub-tori of $G$, satisfying the following properties:*

- *i) $F$ is a sheaf for the fpqc topology (Exp. IV).*
- *ii) $F$ commutes with inductive limits of rings (Exp. XI 3.2).*
- *iii) $F$ commutes with adic limits of local artinian rings (Exp. XI 3.3).*
- *iv) $F$ is infinitesimally smooth over $S$ (Exp. XI 1.8).*
- *v) $F$ is stable under inner automorphisms of $G$, i.e. for every $S$-prescheme $S'$, one has:*

```text
T ∈ F(S′) and g ∈ G(S′) ⇒ int(g)T ∈ F(S′).
```

*Then $F$ is representable by an $S$-prescheme, smooth and separated over $S$.*

<!-- label: III.XV.8.12 -->

**Proposition 8.12 bis.** *Let $S$ and $G$ be as above, $T$ an $S$-torus, and $F$ a subfunctor of
$\operatorname{Hom}_{S-gr}(T, G)$, satisfying the following properties:*

- *i), ii), iii), iv) as above.*
- *v) $F$ is stable under inner automorphisms of $G$, i.e. for every $S$-prescheme $S'$, one has:*

```text
u ∈ F(S′) and g ∈ G(S′) ⇒ int(g) u ∈ F(S′).
```

*Then $F$ is representable by an $S$-prescheme smooth and separated over $S$.*

<!-- label: III.XV.8.12bis -->

*Proof of 8.12.* (The proof of 8.12 bis is entirely analogous and is left to the care of the reader.)

<!-- original page 476 -->

Let $u : F \to \mathcal{CT}$ (7.1 i)) be the $S$-morphism which to every element $T$ of $F(S')$ associates the element
$Centr_{G_{S'}}(T)$ of $\mathcal{CT}(S')$. Since $\mathcal{CT}$ is representable by an $S$-prescheme smooth and
quasi-projective (7.1 i)), we are reduced to proving the representability of $u$. After base change $\mathcal{CT} \to
S$, we are reduced to the following problem: given $S$ and $G$ as above, $H$ a smooth subgroup of $G$ with connected
fibers, we must represent the functor `F_H` such that $F_{H}(S')$ = set of elements $T \in F(S')$ such that

$$ H_{S'} = Centr_{G_{S'}}(T). $$

We shall show that `F_H` is étale and separated over $S$. To do this, it suffices to verify the five conditions of 8.10.

Conditions i), ii) and iii) of 8.10 follow easily from 8.12 i), ii) and iii). One has already remarked that
$\mathcal{T}_{C, H}$ is a separated and infinitesimally étale functor, so `F_H`, which is a subfunctor of
$\mathcal{T}_{C, H}$, is separated and infinitesimally unramified (Exp. XI 1.8). It therefore suffices to show that
`F_H` is infinitesimally smooth (*loc. cit.*). Let $S$ be the spectrum of a local artinian ring, $S_{0}$ a subscheme of
$S$ defined by a nilpotent ideal, $T_{0}$ an element of $F_{H}(S_{0})$; let us prove that $T_{0}$ lifts to an element
$T$ of $F_{H}(S)$. By hypothesis (8.12 iv)), $T_{0}$ lifts to an element $T'$ of $F(S)$. On the other hand, $H$ being
smooth, $T_{0}$ lifts to a sub-torus $T''$ of `H_S` (Exp. IX 3.6 bis), which is conjugate to $T'$ by an element $g \in
G(S)$ (*loc. cit.*), so $T'' \in F(S)$ (8.12 v)). Since $Centr_{G_{S}}(T'')$ is smooth over $S$ and coincides with
$H_{S_{0}}$ above $S_{0}$, $T''$ lies in the

<!-- original page 477 -->

center of `H_S` (Exp. IX 5.6 a)) and its centralizer in $G$ is equal to `H_S`; in short, $T'' \in F_{H}(S)$, and one
takes $T = T''$.

**Corollary 8.13.** *Let $S$ be a prescheme, $G$ an $S$-prescheme in groups smooth and of finite presentation over $S$,
with connected fibers, and let $\mathcal{T}_{D}$ be the subfunctor of $\mathcal{T}$ whose set of points with values in
an $S$-prescheme $S'$ is the set of sub-tori $T$ of $G_{S'}$ such that for every point $s'$ of $S'$, $T_{s}'$ is
contained in the derived subgroup (Exp. VI_B 7) of $G_{s}'$. Then $\mathcal{T}_{D}$ is representable by an $S$-prescheme
smooth and separated over $S$.*

<!-- label: III.XV.8.13 -->

**Corollary 8.13 bis.** *Let $S$ and $G$ be as above, $T$ an $S$-torus, and let $\operatorname{Hom}^{der}_{S-gr}(T, G)$
be the subfunctor of $\operatorname{Hom}_{S-gr}(T, G)$ whose set of points with values in $S'$ is the set of
$S'$-morphisms $u : T_{S'} \to G_{S'}$ such that for every point $s'$ of $S'$, $u_{s}'$ factors through the derived
group of $G_{s}'$. Then this functor is representable by an $S$-prescheme smooth and separated over $S$.*

<!-- label: III.XV.8.13bis -->

Corollary 8.13 and Corollary 8.13 bis are proved analogously; let us prove 8.13 bis for example. By the usual procedure,
we reduce to the case where $S$ is noetherian. Let us verify that the five conditions of 8.12 bis are satisfied:

Conditions i) and iv) follow immediately from the corresponding properties of the functor $\operatorname{Hom}_{S-gr}(T,
G)$. Condition v) is satisfied since the derived group of an algebraic group is invariant (Exp. VI_B § 7). To establish
ii), we are reduced by a standard reduction (EGA IV 8) to proving that if $S$ is a noetherian integral scheme with
generic point $\eta$ and $u : T \to G$ is an $S$-group morphism which on the generic fiber

<!-- original page 478 -->

factors through the derived group of $G_{\eta}$, then there exists a neighborhood $U$ of $\eta$ such that, for every
point $s$ of $U$, $u_{s}$ factors through the derived group of $G_{s}$. But this follows immediately from Exp. VI_B
10.12. To establish iii), let us resume the notation of 4.3. To show that an element $(u_{m})_{m \in \mathbb{N}}$ of
`lim_{←m} Hom^{der}_{S_m-gr}(T_m, G_m)` is "admissible", in the sense of 4.3, and comes from an element of
$\operatorname{Hom}^{der}_{S-gr}(T, G)$, one reduces immediately to the case where $S$ is the spectrum of a complete
discrete valuation ring (cf. 8.1). Let $t$ be the generic point and $s$ the closed point of $S$, $D$ the schematic
closure in $G$ of the derived group $D_{t}$ of $G_{t}$.

a) $D_{s}$ contains the derived group of $G_{s}$. Indeed, since $D_{t}$ is invariant in $G_{t}$ and $G$ is flat over
$S$, $D$ is invariant in $G$. Moreover the morphism

```text
G ×_S G ⟶ G,    (x, y) ↦ x y x⁻¹ y⁻¹
```

factors through $D_{t}$ on the generic fiber, hence factors through $D$. Consequently the algebraic group $G_{s}/D_{s}$
is commutative, whence assertion a).

b) If $u_{m} \in \operatorname{Hom}^{der}_{S_{m}-gr}(T_{m}, G_{m})$, then $u_{m}$ factors through $D_{m}$. Indeed, by
hypothesis, $u_{s}$ factors through the derived group of $G_{s}$, hence *a fortiori* factors through $D_{s}$ by a).
Since $D_{m}$ is flat over $S_{m}$ and invariant in $G_{m}$, the quotient group $H_{m} = G_{m}/D_{m}$ is representable
(Exp. VI_A § 4). Since the image of $T_{m}$ in $H_{m}$ is a torus (Exp. IX 6.8) whose closed fiber is zero, the image of
$T_{m}$ is zero; this says that $u_{m}$ factors through $D_{m}$.

c) The family $(u_{m})_{m \in \mathbb{N}}$ is "admissible" and lifts to a morphism $T \to G$ belonging to
$\operatorname{Hom}^{der}_{S-gr}(T, G)$.

<!-- original page 479 -->

By what precedes and 4.1 bis, it suffices to prove that $D_{t}$ is an affine algebraic group, which follows from the
following lemma:

**Lemma 8.14.** *Let $G$ be a smooth connected algebraic group defined over a field $k$. Then the derived group $D$ of
$G$ is affine.*

<!-- label: III.XV.8.14 -->

Since the formation of $D$ commutes with base field extension (Exp. VI_B 7), one may assume $k$ algebraically closed.
But then $G$ is an extension of an abelian variety $A$ by a linear group $L$. Since $A$ is commutative, $D$ is
necessarily contained in $L$, hence is affine.

**Maximal tori.**

**Theorem 8.15.** *Let $S$ be a locally noetherian prescheme and $G$ an $S$-prescheme in groups, smooth and of finite
type over $S$. Then the following conditions are equivalent:*

- *i) The $S$-functor $\mathcal{T}_{M}$, whose set of points with values in an $S$-prescheme $S'$ is the set of maximal
  tori of $G_{S'}$ (Exp. XII 1.3), is representable.*
- *ii) The preceding functor $\mathcal{T}_{M}$ is representable by an $S$-prescheme smooth and quasi-projective over $S$
  with affine fibers.*
- *iii) The group $G$ admits locally for the étale topology a maximal torus.*

<!-- original page 480 -->

- *iv) The group $G$ admits locally for the faithfully flat topology a maximal torus.*
- *v) The group $G$ has property AT (8.4), and the reductive rank of its fibers is a locally constant function on $S$.*

<!-- label: III.XV.8.15 -->

*Proof.* ii) ⇒ i) is clear.

i) ⇒ iii). Indeed, since $G$ is of finite presentation over $S$, it follows from 6.3 that $\mathcal{T}_{M}$ commutes
with inductive limits of rings, hence is locally of finite presentation if it is representable (EGA IV 8.14). Moreover
$\mathcal{T}_{M}$ is formally smooth (Exp. XI 2.1 bis). So if it is representable, it is representable by a prescheme
smooth over $S$, and iii) then follows from Hensel's lemma (Exp. XI 1.10).

iii) ⇒ iv) is clear.

iv) ⇒ v). Let $s$ be a point of $S$. By hypothesis, there exists an $S$-prescheme $S'$, flat over $S$, whose image
contains $s$, such that $G_{S'}$ admits a maximal torus $T'$. Let $s'$ be a point of $S'$ above $s$. The reductive rank
of the fibers of $G_{S'}$ is therefore constant on $\operatorname{Spec} \mathcal{O}_{S', s'}$, and consequently the
reductive rank of the fibers of $G$ is constant on the image of $\operatorname{Spec} \mathcal{O}_{S', s'}$, which is
$\operatorname{Spec} \mathcal{O}_{S, s}$ (EGA IV 2.3.4 ii)). Now the reductive rank of the fibers of $G$ is a locally
constructible function on $S$ (6.3 bis), so this rank is constant on a neighborhood of $s$ (EGA IV 1.10.1).

To see that $G$ has property AT, consider an $S$-scheme $S_{1}$, spectrum of a discrete valuation ring, with closed
point $s_{1}$ projecting to the point $s$

<!-- original page 481 -->

above. The prescheme $S'_{1} = S_{1} \times_{S} S'$ is faithfully flat over $S_{1}$, and $G_{S'_{1}}$ admits a maximal
torus. Let $A$ (resp. $A'$) be the ring of $S_{1}$ (resp. $S'_{1}$). Regarding $A'$ as an inductive limit of its
finitely generated $A$-subalgebras, it follows from 6.3 that there exists an $S_{1}$-scheme $S''_{1}$ such that
$G_{S''_{1}}$ admits a maximal torus and the structural morphism $S''_{1} \to S_{1}$ is of finite type and surjective.
Using now EGA II 7.1.9, we may assume that $S'_{1}$ is the spectrum of a discrete valuation ring. But then it is clear
that $G_{S'_{1}}$, hence also $G_{S_{1}}$, has property AT. Since this is true for every $S$-prescheme $S_{1}$ spectrum
of a discrete valuation ring, $G$ has property AT.

v) ⇒ i). Indeed, by 8.9, the functor $\mathcal{T}$ of sub-tori of $G$ is representable, and it is clear that
$\mathcal{T}_{M}$ is representable by the open-closed subprescheme of $\mathcal{T}$ representing the subfunctor of tori
of rank $r$, where $r$ denotes the reductive rank of $G$ (which one may assume constant).

iii) ⇒ ii). Indeed, if condition iii) is realized, we may use the results of Exp. XII 7.1. The functor $\mathcal{T}_{M}$
is therefore canonically isomorphic to the functor of Cartan subgroups of $G$, and it suffices to apply 7.3 i).

**Remark 8.16.** One can show that the prescheme $\mathcal{T}_{M}$ of maximal tori of $G$ is affine over $S$[^XV-8-1],
which generalizes Exp. XII 5.4.

<!-- label: III.XV.8.16 -->

**Corollary 8.17.** *Let $S$ be a prescheme, $G$ an $S$-prescheme in groups,*

<!-- original page 482 -->

*smooth and of finite presentation over $S$. Suppose that the abelian rank and the reductive rank of the fibers of $G$
are locally constant functions on $S$; then $G$ satisfies the (equivalent) properties i) to iv) of 8.15.*

<!-- label: III.XV.8.17 -->

We may assume that the abelian rank and the reductive rank of the fibers of $G$ are constant. Proceeding as in 8.11, and
in view of 6.3 bis, we reduce to the case where $S$ is noetherian. But then $G$ has property AT (8.7), and one concludes
by 8.15 v).

**Corollary 8.18.** *Let $S$ be a prescheme, $G$ an $S$-prescheme in groups, smooth over $S$. Then the following
conditions are equivalent:*

- *a) The unipotent rank $\rho_{u}$ and the abelian rank $\rho_{ab}$ (6.1 ter) of the fibers of $G$ are locally constant
  functions on $S$.*
- *b) The unipotent rank $\rho_{u}$ is locally constant and $G$ admits locally for the fpqc topology maximal tori.*
- *c) The reductive rank $\rho_{r}$ (6.1 ter) and the abelian rank $\rho_{ab}$ of the fibers of $G$ are locally constant
  functions on $S$.*

<!-- label: III.XV.8.18 -->

**Remarks 8.19.** Under the hypotheses of 8.18, a more refined argument, using the lower semicontinuity of the abelian
rank (announced in Exp. X 8.7), shows that if two of the three ranks $\rho_{u}$, $\rho_{r}$, $\rho_{ab}$ are locally
constant, then so is the third.

<!-- label: III.XV.8.19 -->

*Proof of 8.18.* Possibly replacing $G$ by its connected component, we may assume $G$ of finite presentation over $S$
(Exp. VI_B 5.3.3).

<!-- original page 483 -->

a) ⇒ c). Let $s$ be a point of $S$. Since $\rho_{ab}$ is locally constant, it follows from 8.11 that, possibly after an
étale extension covering $S$, we may assume that there exists a sub-torus $T$ of $G$ whose fiber $T_{s}$ is a maximal
torus of $G_{s}$. Let $C = Centr_{G}(T)$, which is a subgroup prescheme of $G$, smooth over $S$ with connected fibers.
For every point $t$ of $S$, $C_{t}$ evidently contains a Cartan subgroup $C'_{t}$ of $G_{t}$. Possibly restricting $S$,
we may assume $\rho_{u}$, $\rho_{ab}$, and the relative dimension of $C$ over $S$ are constant. One then has the
inequalities

```text
dim Cₛ = dim C_t ⩾ dim C′_t ⩾ ρ_u(t) + ρ_{ab}(t) + dim T_t
                            = ρ_u(s) + ρ_{ab}(s) + dim Tₛ = ρ_ν(s) = dim Cₛ.
```

One deduces that $C_{t} = C'_{t}$, hence that $T$ is a maximal torus of $G$, and *a fortiori* $\rho_{r}(t) =
\rho_{r}(s)$.

c) ⇒ b) by 8.17.

b) ⇒ a). Indeed, since $G$ admits locally for the fpqc topology maximal tori, it admits locally for the fpqc topology
Cartan subgroups, and consequently (Exp. XII 7.3) the nilpotent rank $\rho_{\nu} = \rho_{u} + \rho_{r} + \rho_{ab}$ is
locally constant. Since $\rho_{r}$ and $\rho_{ab}$ are locally constant, $\rho_{u}$ is locally constant.

<!-- LEDGER DELTA — Exposé XV — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| relèvement | lifting | Standard. |
| relever | to lift | Standard. |
| relevable | liftable | Standard. |
| sous-tore | sub-torus | Hyphenated; plural "sub-tori". |
| sous-tore maximal | maximal sub-torus | Standard. |
| tore maximal | maximal torus | Standard. |
| variété des tores maximaux | functor `𝒯_M` of maximal tori | Per 8.15. |
| schéma des tores maximaux | scheme of maximal tori | Per 1.10 of XII. |
| sous-groupe parabolique | parabolic subgroup | Standard. |
| sous-groupe de Borel | Borel subgroup | Standard. |
| sous-groupe de Cartan | Cartan subgroup | Standard. |
| normalisateur connexe | connected normalizer | Per 5.1. |
| transporteur | transporter | Standard. |
| transporteur strict | strict transporter | Notation `Transp^{str}`. |
| voisinage infinitésimal | infinitesimal neighborhood | Standard. |
| invariant normal | normal invariant | Per [EGA IV 16.1.2](https://jcreinhold.github.io/ega/iv/29-ch4-16-differential-invariants.html#161-normal-invariants-of-an-immersion). |
| rang nilpotent | nilpotent rank | `ρ_n`. |
| rang réductif | reductive rank | `ρ_r`. |
| rang unipotent | unipotent rank | `ρ_u`. |
| rang abélien | abelian rank | `ρ_{ab}`. |
| décomposition de Chevalley | Chevalley decomposition | Standard. |
| adhérence schématique | schematic closure | Standard. |
| relèvement infinitésimal | infinitesimal lifting | Standard. |
| relèvement global | global lifting | Standard. |
| de type multiplicatif | of multiplicative type | Standard. |
| central | central | Standard. |
| densément schématique | schematically dense | Per Exp. IX 4.1. |
| revêtement complètement décomposé | completely decomposed covering | Per 2.5. |
| limite adique | adic limit | Per 8.1. |
| propriété AT / ATC | property AT / ATC | Coined in 8.4; preserve as labels. |
| dégénère en une partie torique | degenerate into a toric part | Per 8.4 (quoted phrase). |
| groupe formel / complété formel | formal completion | Per 4.6. |
| algébrisable | algebraizable | Per 4.6. |
| critère valuatif | valuative criterion | Standard. |
| ind-constructible | ind-constructible | Standard. |
| localement constructible | locally constructible | Standard. |
| caractéristique résiduelle | residue characteristic | Standard. |
| Bible | *Bible* | Italicised; the Chevalley Seminar 1956/58. |
| schéma en sous-groupes | subgroup scheme | Standard. |
| sous-préschéma en groupes | subgroup prescheme | Standard. |
| « noyau » de l'élévation à la puissance nième | "kernel" of the n-th power morphism | Preserve quotes around "kernel" since the n-th power map is not a homomorphism. |
| Hom centraux | central homomorphisms | Per 8.8. |
| Hom dérivés | derived homomorphisms | Per 8.13. |
-->

[^XV-0-1]: This Exposé and the two following ones (Exp. XVI and XVII) do not correspond to oral lectures of the seminar.
    They develop, with some additional material, the substance of (succinct) manuscript notes of A. Grothendieck,
    written in 1964 on the occasion of the present seminar.

[^N.D.E-XV-1]: The idea of approximating a torus by its finite subgroups appears in Grothendieck's proof of the
    connectedness of the centralizers of tori; see § 4.6 of *Bible*.

[^N.D.E-XV-2]: cf.
    [EGA 0_III, 12.3.5](https://jcreinhold.github.io/ega/iii/05-ch0-12-complements-cohomology-sheaves.html#123-complements-on-the-ext-functors-of-sheaves).

[^N.D.E-XV-3]: introduced after Lemma 2.7.

[^N.D.E-XV-4]: The fact that (iv) ⇒ (iii) will appear in the course of the proof.

[^N.D.E-XV-5]: We have replaced "functor" by "subfunctor". Should one rather write "which makes $\sigma_{q, S'}$
    injective for $q \leqslant n$"?

[^N.D.E-XV-6]: One may apply, for example, Proposition II.6.1 of the book by M. Demazure and P. Gabriel, *Groupes
    algébriques* I, Masson & North Holland (1970).

[^XV-6-1]: hypothesis in fact superfluous, cf. XVII App. III 3.

[^N.D.E-XV-7]: we have removed the word "residue".

[^N.D.E-XV-8]: details or references to be given here…

[^N.D.E-XV-9]: argument to be made explicit…

[^N.D.E-XV-10]: (Krull's)

[^XV-8-1]: cf. M. Raynaud, *Faisceaux amples sur les schémas en groupes et les espaces homogènes* (thesis, to
    appear)(N.D.E.: see Lecture Notes Math. 119 (1970), Springer), in particular IX 2.9.
