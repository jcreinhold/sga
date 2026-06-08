# Exposé XII. Maximal tori, the Weyl group, Cartan subgroups, the reductive center of smooth and affine group schemes

<!-- label: III.XII -->

*by A. Grothendieck*

<!-- original page 180 -->

From the present Exposé onwards, in contrast to the preceding Exposés, we make use of the known results on the structure
of smooth algebraic groups over an algebraically closed field $k$, and above all of Borel's theory of affine algebraic
groups, expounded in the Séminaire Chevalley 56/57: "Classification des groupes de Lie algébriques".[^N.D.E-XII-1]
Following the usage in the theory of algebraic groups, we refer to this Séminaire by the sigil *BIBLE*. For the next
Exposés, we shall need in particular the results of *BIBLE* 4, 5, 6, 7 (the number after *BIBLE* refers to the Exposé
number). It seems, moreover, that the theory of schemes brings no notable simplification to Borel's theory as exposed in
*BIBLE*. That is why it has not seemed useful to reproduce it in the present Séminaire, our aim here being to deduce,
from results known over algebraically closed fields, analogous results valid over an arbitrary base prescheme. (Things
will be different for Chevalley's structure theory of semisimple groups, which, it appears, is best treated *ab ovo*
over an arbitrary base prescheme.)

In the oral Exposés (which we have followed in Nos. 1 to 4) we restricted ourselves to affine group preschemes over $S$,
relying in an essential way on the representability theorems of Exp. XI N° 4. In the present notes (cf. Nos. 6 to 8)
    <!-- original page 181 --> we show rapidly how the affine hypotheses can be eliminated by a simpler method that does not
use the most delicate results of Exposé XI. For other generalizations of the results contained in the present Exposé,
see also Exposés XV and XVI. (It is evident that the content of Exposés XI, XII, XV, XVI ought to be completely
rewritten.)

## 1. Maximal tori

<!-- label: III.XII.1 -->

**1.0.** Let first $G$ be an algebraic group over an algebraically closed field $k$. By a *maximal torus of $G$* one
means an algebraic subgroup $T$ of $G$ which is a torus (meaning here, since $k$ is algebraically closed, that it is
isomorphic to a group of the form $G^{r}_{m}$), and which is maximal for this property. Note that, $k$ being perfect,
$G_{red}$ is a subgroup of $G$, smooth over $k$, so it is essentially an algebraic group in the sense of *BIBLE*.
Moreover, every reduced subgroup of $G$ (such as a torus) is automatically a subgroup of $G_{red}$, so the maximal tori
of $G$ coincide with the maximal tori of $G_{red}$. When $G$ is affine, hence $G_{red}$ is affine, a fundamental theorem
of Borel tells us that two maximal tori of $G$ are conjugate by an element of $G(k) = G_{red}(k)$ (*BIBLE* 6, th. 4 c));
in particular they have the same dimension. We shall call the common dimension of the maximal tori of $G$ the *reductive
rank of $G$*. Note moreover that the restriction that $G$ be affine is unnecessary, as follows from a known theorem of
Chevalley, asserting that every connected smooth algebraic group over $k$ is an extension of an abelian variety by an
affine group; cf. N° 6. In Nos. 1 to 4 we shall mostly restrict ourselves to affine group preschemes over the base.

Let $G$ be a smooth algebraic group over $k$, and $T$ a maximal torus of $G$; the centralizer $C(T)$ of $T$ in $G$ will
be called the *Cartan subgroup of $G$ associated with $T$*. For us this is a group subpreschema defined thanks to (VIII,
6.7), but one will note that, $G$ being smooth over $k$, the same holds for the Cartan subgroup $C$ by (XI, 5.3); hence
    <!-- original page 182 --> in this case $C$ is the unique group subpreschema of $G$ smooth over $k$ (i.e. an algebraic
subgroup of $G$ in the sense of *BIBLE*) such that $C(k)$ is the subgroup of $G(k)$ centralizing $T(k)$, i.e. it is
essentially the centralizer in the sense of *BIBLE*. By the conjugation theorem already cited, the Cartan subgroups
associated with the various maximal tori are conjugate to each other, hence have the same dimension. We shall call their
common dimension the *nilpotent rank of $G$*; it equals that of $G_{red}$. Let $\rho_{r}(G)$ and $\rho_{n}(G)$ denote the reductive
and nilpotent ranks of $G$; then one has

$$ \rho_{r}(G) \leqslant \rho_{n}(G), $$

and the difference

```text
ρ_u(G) = ρ_n(G) − ρ_r(G) = dim C/T
```

might be called, when $G$ is affine, the *unipotent rank of $G$*. When $G$ is smooth, affine, and connected, then $C$ is
a nilpotent connected algebraic group (*BIBLE* 6, th. 6 a) and c)), hence (*BIBLE* 6, th. 2) isomorphic to the product
$C_{s} \times C_{u}$, where $C_{s} = T$ is the maximal torus we started with (which is *a fortiori* a maximal torus in
$C$), and where $C_{u}$ is a smooth unipotent subgroup, i.e. a successive extension of groups isomorphic to $G_{a}$
(*BIBLE* 6 th. 1 cor. 1 and 7, th. 4). One then has also, in this case:

$$ \rho_{u}(G) = \dim C_{u}. $$

**Remark 1.1.** *Besides the three notions of rank we have just made precise for an affine algebraic group, there are
two others that are useful, namely the* semisimple rank $\rho_{s}(G)$, *which is by definition the reductive rank of the
quotient $G/R$, where $R$ is the radical of $G$, and finally the* infinitesimal rank $\rho_{i}(G)$, *which is by
definition the nilpotent rank of the Lie algebra of $G$ (which will be defined and studied in the following Exposé). We
shall not use them in the present Exposé. Let us only signal the inequalities:*

```text
ρ_s ⩽ ρ_r ⩽ ρ_n ⩽ ρ_i.
```

<!-- label: III.XII.1.1 -->

**Lemma 1.2.** *Let $G$ be an algebraic group over the algebraically closed field $k$, $T$ an algebraic subgroup of $G$,
$k'$ an algebraically closed extension of $k$, $G'$ and $T'$ the groups obtained from $G$, $T$ by extension of the base.
For $T$ to be a maximal torus of $G$, it is necessary and sufficient that $T'$ be a maximal torus of $G'$.*

<!-- label: III.XII.1.2 -->

<!-- original page 183 -->

This is an immediate consequence of the "principle of finite extension" ([EGA IV, 9.1.1](https://jcreinhold.github.io/ega/iv/22-ch4-09-constructible-properties.html#91-the-principle-of-finite-extension)).

**Definition 1.3.** *Let $S$ be a prescheme, $G$ an $S$-prescheme in groups of finite type, $T$ a group subpreschema of
$G$. One says that $T$ is a* maximal torus of $G$ *if*

*a) $T$ is a torus (IX, 1.3) and*

*b) for every $s \in S$, denoting by $\bar{s}$ the spectrum of an algebraic closure of $\kappa(s)$, $T_{\bar{s}}$ is a
maximal torus in $G_{\bar{s}}$.*

<!-- label: III.XII.1.3 -->

**Remarks 1.4.** *It follows from 1.2 that when $S$ is the spectrum of an algebraically closed field one recovers the
usual definition, and that property 1.3 is stable under any base change. Note that, by (X, 8.8), one may in Definition
1.3 replace condition a) by:*

*a′) $T$ is of finite presentation and flat over $S$.*

<!-- label: III.XII.1.4 -->

*One should beware that a maximal torus in the sense of Definition 1.3 is indeed maximal among the subtori of $G$ (as
follows at once from (IX, 2.9)), but that the converse cannot be valid—the base $S$ being, say, connected—unless $G$
effectively admits a maximal torus in the sense of 1.3, which is not the case in general (even if $S =
\operatorname{Spec}(\mathbb{Z})$ and $G$ is "semisimple"; see also 1.6). We shall see however in XIV that the converse
holds when $S$ is artinian, or when $S$ is a local scheme and $G$ is "reductive": in this case, every torus of $G$ is
contained in a maximal torus.*

**Definition 1.5.** *Let $G$ be an algebraic group over a field $k$. The* reductive rank *(resp.* nilpotent rank\*,
resp.\* unipotent rank\*, etc.) of $G$ is the reductive rank (resp. …) of $G_{\bar{k}}$, where $\bar{k}$ is an algebraic
closure of $k$.\*

<!-- label: III.XII.1.5 -->

<!-- original page 184 -->

One will note that, in view of 1.2 and the commutation of the formation of $Centr_{G}(T)$ with base extension, the
notions of rank introduced in 1.5 are invariant under extension of the base field; on the other hand, for $k$
algebraically closed, they coincide with those introduced at the beginning of the present number.

**Remark 1.6.** *It is not difficult to construct an affine smooth group scheme $G$ over the spectrum $S$ of a discrete
valuation ring, whose generic fiber is isomorphic to $G_{m}$, and whose special fiber is isomorphic to $G_{a}$. Such a
$G$ contains no torus except the trivial torus $T$ (reduced to the unit subgroup), which is evidently not a maximal
torus. More precisely, in the special fiber $G_{0} = G_{a,k}$, `T_0` is indeed a maximal torus, but in the generic fiber
$G_{1} = G_{m,K}$, `T_1` is no longer a maximal torus ($k$ is the residue field, $K$ the fraction field of the valuation
ring under consideration). One sees also from this example that the reductive rank of $G_{s}$ ($s \in S$) is not a
continuous function of $s$. One has however the following results:*

<!-- label: III.XII.1.6 -->

**Theorem 1.7.** *Let $S$ be a prescheme, $G$ an affine smooth $S$-prescheme in groups over $S$. For every $s \in S$,
consider $\rho_{r}(s) = \rho_{r}(G_{s})$ and $\rho_{n}(s) = \rho_{n}(G_{s})$, the reductive and nilpotent ranks of
$G_{s}$ (1.5). With these notations, one has the following:*

*a) The function $\rho_{r}$ on $S$ is lower semicontinuous, the function $\rho_{n}$ on $S$ is upper semicontinuous,
hence the function $\rho_{u} = \rho_{n} - \rho_{r}$ is upper semicontinuous.*

*b) The following conditions (stable under arbitrary base change) are equivalent:*

*(i) The function $\rho_{r}$ on $S$ is locally constant.*

<!-- original page 185 -->

*(ii) There exists, locally for the étale topology, a maximal torus in $G$.*

*(ii bis) There exists, locally for the faithfully flat quasi-compact topology, a maximal torus in $G$.*

*c) Let `T_1`, `T_2` be two maximal tori in $G$ (which implies that one is under the conditions of b)). Then `T_1`,
`T_2` are conjugate locally for the étale topology, i.e. there exists an étale surjective morphism $S' \to S$ such that
the subgroups $(T_{1})_{S'}$ and $(T_{2})_{S'}$ of $G_{S'}$ are conjugate by a section of $G_{S'}$ over $S'$.*

*d) Under the conditions of b), i.e. when $\rho_{r}$ is locally constant, the same holds for $\rho_{n}$ (hence also for
$\rho_{u} = \rho_{n} - \rho_{r}$).*

<!-- label: III.XII.1.7 -->

*Proof.* a) Note that for any morphism $S' \to S$, setting $G' = G \times_{S} S'$, the functions $\rho'_{r}$ etc. on
$S'$ defined in terms of $G'$ as $\rho_{r}$ etc. in terms of $G$ are obtained simply by composing the latter with $S'
\to S$. When $S' \to S$ is faithfully flat quasi-compact, it follows that $\rho'$ is continuous, resp. upper
semicontinuous, resp. lower semicontinuous, if and only if $\rho$ is, the Zariski topology of $S$ being in effect a
quotient of that of $S'$ (SGA 1, VIII 4.3). Consequently, the assertions of a) are local for the faithfully flat
quasi-compact topology. Let then $s \in S$; we wish to show that the set $U$ of $t \in S$ such that $\rho_{r}(t)
\geqslant \rho_{r}(s)$ (resp. $\rho_{n}(t) \leqslant \rho_{n}(s)$) is a neighborhood of $s$. By the principle of finite
extension, there exists a finite extension $k$ of $\kappa(s)$ such that $G_{k}$ admits a maximal torus. There then exist
an open neighborhood $U$ of $s$, and a finite surjective locally free morphism $S' \to U$ such that the fiber $S'_{s}$
is $\kappa(s)$-isomorphic to $\operatorname{Spec}(k)$ (cf. EGA III, 10.3.2, where the noetherian hypothesis is
manifestly unnecessary). Since $S' \to S$ is an open morphism (SGA 1, IV 6.6), we are reduced to the case where $S' =
S$, i.e. to the case where there exists a maximal torus $T_{s}$ in $G_{s}$. Furthermore, by (XI, 5.8 a)), possibly
replacing $S$ by an $S'$ étale over $S$ equipped with a point $s'$ above $s$, <!-- original page 186 --> we may suppose
that $T_{s}$ is the fiber at $s$ of a subtorus $T$ of $G$. Then for every $t \in S$, $\rho_{r}(t) = \rho_{r}(G_{t})
\geqslant \dim T_{t} = \dim T_{s} = \rho_{r}(G_{s}) = \rho_{r}(s)$, which proves that $\rho_{r}$ is lower
semicontinuous. On the other hand, by (XI, 5.3), the functor

$$ C = Centr_{G}(T) $$

is representable by $C = Centr_{G}(T)$,[^N.D.E-XII-2] a closed group subpreschema of $G$ smooth over $S$. So there
exists a neighborhood $U$ of $s$ such that $t \in U$ implies $\dim C_{t} = \dim C_{s} = \rho_{n}(s)$. The upper
semicontinuity of $\rho_{n}$ is then a consequence of the relation

```text
ρ_n(t) ⩽ dim C_t   for every t ∈ S,
```

which is itself contained in the following purely geometric lemma:

**Lemma 1.8.** *Let $k$ be a field, $G$ an affine smooth algebraic group over $k$, $T$ a torus in $G$, $C$ its
centralizer; then one has*

$$ \rho_{n}(G) \leqslant \dim C. $$

<!-- label: III.XII.1.8 -->

Indeed, one may suppose $k$ algebraically closed, so that $T$ is contained in a maximal torus `T_0`. Let `C_0` be the
centralizer of the latter; then $C_{0} \subset C$, hence $\dim C_{0} \leqslant \dim C$. QED.

b) If $\rho_{r}$ is locally constant, then for every torus $T$ in $G$, and every $s \in S$, if $T_{s}$ is a maximal torus in
$G_{s}$, then there exists an open neighborhood $U$ of $s$ such that $T|U$ is a maximal torus in $G|U$. Using now the
reasoning of a), one sees that (i) ⇒ (ii bis). On the other hand (ii bis) ⇒ (i), for when $G$ admits a maximal torus
$T$, then it is evident that $\rho_{r}(s) = \dim T_{s}$ is a locally constant function of $s$; now we signaled at the beginning
of the proof of a) that the question of continuity of $\rho_{r}$ was local for the faithfully flat topology. Hence (i) ⇔ (ii
bis), and obviously (ii) ⇒ (ii bis); it remains to prove the converse implication (i) ⇒ (ii). <!-- original page 187 -->
For this, introduce the functor $F$ of (XI, 4.1),[^N.D.E-XII-3] which is therefore a smooth separated prescheme over
$S$, and consider the subfunctor $\mathcal{T}$ of $F$, whose value for an $S'$ over $S$ is the set of maximal tori in $G_{S'}$.
Using the previous remark that, granted (i), a torus in $G_{S'}$ which is maximal in the fiber of some point $s \in S'$ is
maximal above an open neighborhood of $s$, one sees that $\mathcal{T}$ is representable by an open subpreschema of $F$, and is
therefore smooth and separated over $S$. Since the structural morphism $\mathcal{T} \to S$ is evidently surjective, it admits a
section locally for the étale topology by (XI, 1.10), which proves (i) ⇒ (ii).

c) This is an immediate consequence of (XI, 5.4 bis), taking into account Borel's conjugation theorem recalled at the
beginning of the number.

d) By the remark at the beginning of the proof in a), and taking into account b), we may suppose that there exists a
maximal torus $T$ in $G$. If $C$ is its centralizer, then $C$ is representable and smooth over $S$ by (XI, 5.3), so the
function $s \mapsto \rho_{n}(s) = \dim C_{s}$ is indeed locally constant.

The proof of 1.7 is complete. We shall refer to the conditions envisaged in 1.7 b) by saying that in this case $G$ is
*of locally constant reductive rank*. Let us note:

**Corollary 1.9.** *Let $G$ be as in 1.7, and let $s \in S$ be such that $\rho_{u}(s) = 0$, i.e. $\rho_{r}(s) =
\rho_{n}(s)$ (i.e. the Cartan subgroups of $G_{\bar{k}}$ are tori, where $\bar{k}$ is an algebraic closure of
$\kappa(s)$). Then there exists an open neighborhood $U$ of $s$ over which $\rho_{r}$ and $\rho_{n}$ are constant; in
particular, for every $t \in U$, the unipotent rank $\rho_{u}(t)$ of $G_{t}$ is zero.*

<!-- label: III.XII.1.9 -->

Indeed, this follows immediately from 1.7 a) and from the inequality $\rho_{r}(t) \leqslant \rho_{n}(t)$ for every $t
\in S$.

Note also that we have proved, at the same time as b), the

<!-- original page 188 -->

**Corollary 1.10.** *Let $G$ be as in 1.7, and suppose $G$ of locally constant reductive rank. Consider the functor*

$$ \mathcal{T} : (Sch)^{\circ} \longrightarrow (Ens), $$

*such that for every $S'$ over $S$, one has*

```text
𝒯(S′) = the set of maximal tori of G_{S′}.
```

*Then $\mathcal{T}$ is representable by a smooth, separated prescheme of finite type over $S$.*

<!-- label: III.XII.1.10 -->

It remains to verify that $\mathcal{T}$ is of finite type over $S$. The question being local for the faithfully flat
quasi-compact topology, we may suppose that $G$ admits a maximal torus $T$. By (XI, 5.3 bis) and the bis version of 5.5,
$Norm_{G}(T)$ and $G/Norm_{G}(T)$ are representable by preschemes $Norm_{G}(T)$ and $G/Norm_{G}(T)$, and $\mathcal{T}$
is isomorphic to $G/Norm_{G}(T)$.[^N.D.E-XII-4] The morphism $G \to \mathcal{T}$ defined by $g \mapsto int(g)(T)$ being
surjective, and $G$ quasi-compact over $S$, the same holds for $\mathcal{T}$, which completes the proof.

**Remarks 1.11.** *a) The prescheme $\mathcal{T}$ of 1.10 will rightly be called the* prescheme of maximal tori of $G$.
*We shall see in N° 5 that it is in fact affine over $S$. One can verify this directly when $G$ is isomorphic to a
closed group subpreschema of a prescheme of the form $GL(n)$, using (XI, 4.6) and remarking that, by the reasoning of
the proof of 1.7 b), $\mathcal{T}$ identifies with a subpreschema both open and closed of the prescheme $F$ which
represents the multiplicative-type subgroups of $G$.*

*b) It is possible to give a proof of 1.7—and hence of 1.9—not using the delicate results of XI, but only the easy
results (XI, 3.12) and (XI, 6.2), working only with multiplicative-type subgroups finite over the base (morally, the
groups ${}_{n} T$ where $T$ is a maximal torus); compare N° 7. The same remark applies to the proof of 1.10.*

<!-- label: III.XII.1.11 -->

<!-- original page 189 -->

We end this number by giving examples in which there exists a unique maximal torus.

**Proposition 1.12.** *Let $G$ be an $S$-prescheme in groups of multiplicative type and of finite type. Then $G$ admits
a unique maximal torus, and every torus in $G$ is contained in this maximal torus.*

<!-- label: III.XII.1.12 -->

Uniqueness obviously follows from the latter assertion, which characterizes the maximal torus as the largest subtorus of
$G$. From uniqueness it follows that the existence question is local for the faithfully flat quasi-compact topology,
which allows us to suppose $G$ diagonalizable, i.e. of the form $D_{S}(M)$, with $M$ a finitely generated commutative
group. Let `M_0` be the quotient of $M$ by its torsion subgroup; I claim that the torus $T = D_{S}(M_{0})$ in $G$ is a
maximal torus and a largest subtorus. Indeed, a subtorus $T'$ of $G$ is locally diagonalizable for the fpqc topology,
hence to prove $T' \subset T$ we may suppose $T'$ diagonalizable, hence of the form $D_{S}(N)$, where $N$ is a free
quotient of $M$ (VIII 1.4 and 3.2 b)), hence $N$ is a quotient of `M_0`, hence $T' \subset T$. Since the construction of
$T$ as $D_{S}(M_{0})$ is compatible with any base extension, this shows at the same time that $T$ is a maximal torus of
$G$, and completes the proof. In the case where $G$ is smooth over $S$, 1.12 may be generalized:

**Proposition 1.13.** *Let $G$ be an $S$-prescheme in groups of finite presentation over $S$. Suppose that $G$ admits,
locally for the faithfully flat quasi-compact topology, a central maximal torus. Then $G$ admits (globally) a unique
maximal torus,[^N.D.E-XII-5] and it is the largest subtorus of $G$.*

<!-- label: III.XII.1.13 -->

Here again, uniqueness is trivial from the last assertion, and renders existence a local question for fpqc, which allows
us to suppose that $G$ admits a central maximal torus $T$. We show that every torus $R$ of $G$ is contained in $T$.

This follows from the <!-- original page 190 -->

**Lemma 1.14.** *Let $G$ be an $S$-prescheme in groups of finite presentation over $S$, $T$ a maximal torus of $G$, $R$
a subtorus of $G$, and suppose that $T$ and $R$ commute. Then $R \subset T$.*

<!-- label: III.XII.1.14 -->

Indeed, since $R$ and $T$ commute, the morphism $R \times_{S} T \to G$ defined by $(r, t) \mapsto r \cdot t$ is a group
homomorphism, hence by (IX, 6.8) it admits an image subgroup $T'$ in $G$, which is a multiplicative-type group quotient
of $R \times_{S} T$, hence a torus, evidently containing $T$. Since $T$ is a maximal torus, one has $T' = T$ (1.4),
hence $R \subset T$, which proves 1.14 and hence 1.13. In particular, using 1.7 b):

**Corollary 1.15.** *Let $G$ be a commutative, smooth, and affine $S$-prescheme in groups over $S$, of locally constant
reductive rank. Then $G$ admits a unique maximal torus, and this latter contains every subtorus of $G$.*

<!-- label: III.XII.1.15 -->

**Corollary 1.16.** *Let $G$ be a smooth and affine $S$-prescheme in groups over $S$. Suppose that for every $s \in S$,
denoting by $\bar{s}$ the spectrum of an algebraic closure $\bar{k}$ of $\kappa(s)$, the geometric fiber $G_{\bar{s}}$
is a connected nilpotent algebraic group (in the sense of BIBLE, i.e. the group $G(\bar{k})$ of its $\bar{k}$-valued
points is nilpotent). Suppose moreover that the reductive rank of $G$ is locally constant. Then $G$ admits a unique
maximal torus $T$; moreover, $T$ is central and is the largest subtorus of $G$.*

<!-- label: III.XII.1.16 -->

By 1.7 b), $G$ admits a maximal torus locally for fpqc, and by 1.13 we are reduced to proving that a maximal torus of
$G$ is central. By (IX, 5.6 b)), we are reduced to the case where $S$ is the spectrum of a field, which one may suppose
algebraically closed. Then $T(k)$ lies in the center of $G(k)$ by *BIBLE* 6 th. 2, which implies that $T$ lies in the
center of $G$, since $Centr_{G}(T)$ is a closed subscheme of $G$ (VIII 6.6) which contains the points of $G(k)$, hence
is identical to $G$ by the Nullstellensatz (since $G$ is reduced).

<!-- original page 191 -->

Finally, for later reference, let us signal the following trivial proposition (of which we have already made implicit
use):

**Proposition 1.17.** *Let $G \supset H \supset T$ be preschemes in groups of finite type over $S$. Equivalent
conditions:*

*(i) $T$ is a maximal torus of $G$.*

*(ii) $T$ is a maximal torus of $H$, and for every $s \in S$, one has equality of the reductive ranks $\rho_{r}(G_{s}) =
\rho_{r}(H_{s})$.*

<!-- label: III.XII.1.17 -->

## 2. The Weyl group

<!-- label: III.XII.2 -->

Let first $k$ be an algebraically closed field, and let $G$ be a smooth affine algebraic group over $k$. If $T$ is a
maximal torus, $C$ its centralizer and $N$ its normalizer, then by (XI, 5.9) these are smooth closed subgroups of $G$,
and $C$ is an open subgroup of $N$, so that $W = N/C$ is a finite étale group over $k$, hence determined by the group
$W(k)$ of its $k$-valued points, as $W = W(k)_{k}$ (constant group defined by the ordinary finite group $W(k)$). The
finite group $W(k)$ will be called the *geometric Weyl group* (or simply the *Weyl group* if no confusion is to be
feared) of $G$ relative to $T$. By Borel's conjugation theorem, the Weyl groups relative to the various maximal tori are
isomorphic to each other; this is why one sometimes speaks of "the" Weyl group of $G$, without specifying a maximal
torus. Since the formation of $C$, $N$, and $N/C$ commutes with any base extension, one sees that if $k'$ is an
algebraically closed extension of $k$, the geometric Weyl group of $G_{k'}$ relative to $T_{k'}$ is canonically
isomorphic to that of $G$ relative to $T$; consequently, "the" geometric Weyl group of $G$ (which is properly speaking
an isomorphism class of ordinary finite groups) coincides with that of $G'$.

<!-- original page 192 -->

This allows one, when $G$ is a smooth affine algebraic group over an arbitrary field $k$, to speak of the *geometric
Weyl group of $G$* as the isomorphism class of the geometric Weyl group of $G_{k'}$, where $k'$ is any algebraically
closed extension of $k$. When $G$ admits a maximal torus $T$, then one may evidently form as above $C = Centr_{G}(T)$,
$N = Norm_{G}(T)$, $W = N/C$ which is a finite étale group over $k$, called the *Weyl group of $G$ relative to $T$*; the
geometric Weyl group is then nothing other than the class of the group of points of $W$ with values in any algebraically
closed extension $k'$ of $k$. Here, knowledge of the geometric Weyl group $W(k')$ evidently no longer suffices in
general to reconstruct the algebraic group $W$: one must also know the operations on $W(k')$ of the Galois group of the
separable algebraic closure of $k$ in $k'$.

When finally $G$ is an $S$-prescheme in groups over an arbitrary base $S$, $G$ smooth and affine over $S$, and if $T$ is
a maximal torus of $G$, then (XI, 5.9) still allows us to form the group

```text
W(T) = N(T)/C(T),
```

which is an étale, separated, quasi-finite $S$-prescheme in groups over $S$. Its geometric fibers (relative to the
algebraic closures of the residue fields $\kappa(s)$, $s \in S$) are the geometric Weyl groups of the fibers $G_{s}$.
Consequently, (XI, 5.10) gives information on the variation of these groups with $s \in S$. We can make this information
more precise and generalize it as follows:

**Theorem 2.1.** *Let $S$ be a prescheme, $G$ a smooth and affine $S$-prescheme in groups over $S$. For every $s \in S$,
let $w(s)$ be the geometric Weyl group of $G_{s}$, which is therefore an isomorphism class of finite groups. In the set
$E$ of such classes, introduce the following preorder relation: $w \leqslant w'$ if and only if $w$ and $w'$ are
represented by finite groups $W$ and $W'$ such that $W$ is isomorphic to a quotient of a subgroup of $W'$. With this
convention:*

*a) The function $s \mapsto w(s)$ from $S$ to $E$ is lower semicontinuous.*

<!-- original page 193 -->

*b) Suppose that the reductive rank of $G$ is locally constant. Then the following conditions are equivalent:*

*(i) The function $s \mapsto w(s)$ is locally constant.*

*(i bis) The function $s \mapsto card w(s)$ is locally constant.*

*(ii) There exists, locally for the étale topology (or merely for the fpqc topology), a maximal torus $T$, such that
$W(T)$ is finite over its base.*

*(ii bis) For every $S'$ over $S$, and every maximal torus $T$ of $G_{S'}$, the associated Weyl group $W(T)$ is finite
over $S'$.*

<!-- label: III.XII.2.1 -->

*Proof.* a) Proceeding as in 1.7 a), one is reduced, in order to prove that for every $s \in S$ there exists an open
neighborhood $U$ of $s$ such that $t \in U$ implies $w(t) \geqslant w(s)$, to the case where there exists a torus $R$ in
$G$ such that $R_{s}$ is a maximal torus in $G_{s}$. Let

$$ W(R) = Norm_{G}(R)/Centr_{G}(R) $$

as in (XI, 5.9); this is an étale, separated, quasi-finite group prescheme over $S$. For every $t \in S$, let $w'(t) \in
E$ be its geometric fiber at $t$. Since $R_{s}$ is a maximal torus in $G_{s}$, and the formation of `Norm`, `Centr`,
$Norm/Centr$ is compatible with any base extension, in particular with passage to the fibers, one sees that one has

$$ w(s) = w'(s); $$

I claim moreover that, for $t$ near $s$, one has the inequalities

```text
w(t) ⩾ w′(t)   and   w′(t) ⩾ w′(s),
```

which will suffice to establish a). These two inequalities are contained in the two following lemmas:

<!-- original page 194 -->

**Lemma 2.2.** *Let $S$ be a prescheme, $W$ an étale, separated, quasi-finite $S$-prescheme in groups over $S$. For
every $s \in S$, let $f(s)$ be the class of the geometric fiber of $W$ at $s$, which is an element of the ordered set
$E$ of isomorphism classes of finite groups, introduced in 2.1. Then the function $f : S \to E$ is lower semicontinuous.
For it to be constant in a neighborhood of $s \in S$, it is necessary and sufficient that the same hold for the function
$s \mapsto card f(s)$, and for this it is necessary and sufficient that $W$ be finite over $S$ above an open
neighborhood $U$ of $s$.*

<!-- label: III.XII.2.2 -->

This result is a refinement, in terms of groups, of the one invoked in the proof of (XI, 5.10); we content ourselves
with a sketch of the proof (which is of the most standard type). As usual, one is reduced to the case $S$ affine
noetherian. One sees at once that the function $f$ is constructible ([EGA 0_III, 9.3.1](https://jcreinhold.github.io/ega/iii/02-ch0-09-constructible-sets.html#93-constructible-functions) and 9.3.2, and the sundries of [EGA
IV, 9](https://jcreinhold.github.io/ega/iv/22-ch4-09-constructible-properties.html#9-constructible-properties)), and by ([EGA 0_III, 9.3.4](https://jcreinhold.github.io/ega/iii/02-ch0-09-constructible-sets.html#93-constructible-functions)) one is reduced, for the semicontinuity, to proving that if $t$ is a generalization of
$s$, one has $f(t) \geqslant f(s)$. This reduces us, thanks to ([EGA II, 7.1.7](https://jcreinhold.github.io/ega/ii/02-07-valuative-criteria.html#71-reminders-on-valuation-rings)), to the case where $S$ is the spectrum of
a discrete valuation ring, which one may suppose complete with algebraically closed residue field. But then, $s$
denoting the closed point of $S$, since $G$ is étale and separated over $S$, it contains a subscheme $G'$ both open and
closed, finite over $S$, such that $G'_{s} = G_{s}$ ([EGA II, 6.2.6](https://jcreinhold.github.io/ega/ii/02-06-integral-finite-morphisms.html#62-quasi-finite-morphisms)), and one sees at once that $G'$ is here a subgroup
of $G$. Moreover $G'$, being étale finite over $S = \operatorname{Spec}(V)$, with $V$ complete with algebraically closed
residue field, is a constant group, hence of the form `A_S`, where $A = G'(\kappa(s)) = G(\kappa(s))$ has class $f(s)$.
If $B$ is the geometric fiber of $G$ at the generic point $t$ of $S$, one has therefore a canonical monomorphism $A \to
B$, which proves $f(s) \leqslant f(t)$. (N.B. this proof in fact proves the semicontinuity for an order relation on $E$
finer than the one indicated in 2.1.) The fact that $f$ is continuous at $s$ if and only if $s \mapsto card f(s)$ is,
follows from the fact that for $w, w' \in E$, the relations $w \leqslant w'$ and $card w = card w'$ imply $w = w'$. The
fact that this condition is equivalent to the finiteness of $W$ on a neighborhood of $s$ is then independent of the
group structure <!-- original page 195 --> on $W$, and has been signaled after (XI, 5.10); its proof can moreover easily
be carried out by the preceding arguments, using the valuative criterion of properness ([EGA II, 7.3.8](https://jcreinhold.github.io/ega/ii/02-07-valuative-criteria.html#73-valuative-criterion-of-properness)).

**Lemma 2.3.** *Let $G$ be a smooth affine algebraic group over an algebraically closed field $k$, $R \subset T$ two
subtori, $W(R)$ and $W(T)$ the two associated finite groups as in (XI, 5.9), quotients of the normalizer by the
centralizer. Then $W(R)$ is isomorphic to a quotient of a subgroup of $W(T)$.*

<!-- label: III.XII.2.3 -->

Indeed, consider the diagram

```text
T ↪ C(T) ↪ C(R)
         ↓     ↓
   N(T) ∩ N(R) ↪ N(R)
       ↓
     N(T)
```

then $(N(T) \cap N(R))/C(T)$ is a subgroup of $W(T) = N(T)/C(T)$, and one has an obvious homomorphism:

```text
(N(T) ∩ N(R))/C(T) ⟶ W(R) = N(R)/C(R),
```

and everything reduces to proving that this last is surjective, i.e. that for every $k$-valued point $g$ of $N(R)$,
there exists a $k$-valued point $c$ of $C(R)$ such that `cg` normalizes $T$, i.e. such that

```text
int(c)(int(g)T) = T.
```

Now for this it suffices to note that `int(g)T` is a torus of $N(R)$ hence of $C(R)$ (which is an open subgroup
thereof). Then $T$ and `int(g)T` are maximal tori of $C(R)$, since they are maximal in $G$, and one concludes by Borel's
conjugation theorem.

This proves 2.3 and thereby 2.1 a).

<!-- original page 196 -->

b) We have already signaled that (i) and (i bis) are trivially equivalent; they imply (ii bis) by the converse to 2.2 or
to (XI, 5.10) at choice; (ii bis) ⇒ (ii) thanks to 1.7 b); finally (ii) ⇒ (i bis), for one sees as in 1.7 a) that the
condition (i) is local for fpqc, which allows us to suppose that $G$ admits a maximal torus $T$ such that $W(T)$ is
finite over $S$, and one concludes again by (XI, 5.10). This completes the proof of 2.1.

## 3. Cartan subgroups

<!-- label: III.XII.3 -->

**Definition 3.1.** *Let $G$ be a smooth $S$-prescheme in groups of finite type over the prescheme $S$. By a* Cartan
subgroup of $G$ *one means a group subpreschema $C$ of $G$, smooth over $S$, such that for every $s \in S$, denoting by
$\bar{s}$ the spectrum of an algebraic closure of $\kappa(s)$, $C_{\bar{s}}$ is a Cartan subgroup (cf. N° 1) of
$G_{\bar{s}}$.*

<!-- label: III.XII.3.1 -->

It is immediate that if $C$ is a Cartan subgroup of $G$, then for every $S'$ over $S$, $C_{S'}$ is a Cartan subgroup of
$G_{S'}$. If $S$ is the spectrum of an algebraically closed field, one recovers the notion recalled in N° 1. Finally,
one verifies at once that the property for a group subpreschema $C$ of $G$ to be a Cartan subgroup is local in nature
for the faithfully flat quasi-compact topology.

**Theorem 3.2.** *Let $G$ over $S$ be as in 3.1, and suppose that $G$ is affine over $S$ and of locally constant
reductive rank. Then the map*

```text
T ⟼ Centr_G(T)
```

*induces a bijection from the set of maximal tori of $G$ onto the set of Cartan subgroups[^XII-3-1] of $G$. If $C$
corresponds to $T$, then $T$ is the unique maximal torus*

<!-- original page 197 -->

*of $C$.*

<!-- label: III.XII.3.2 -->

If $T$ is a maximal torus of $G$, the functor $Centr_{G}(T)$ is representable, by (XI, 5.3) or (XI, 6.2), by a closed
smooth subpreschema of $G$, $C = Centr_{G}(T)$, and it follows from the definitions that $C$ is a Cartan subgroup of
$G$. Moreover, $T$ is obviously a maximal torus of $C$, and being central, it is the unique maximal torus of $C$ (1.13).
Hence the map $T \mapsto Centr_{G}(T)$ from the set of maximal tori into the set of Cartan subgroups is injective; it
remains to prove that it is surjective. Let then $C$ be a Cartan subgroup of $G$; we prove that it is of the form
$Centr_{G}(T)$, for $T$ a maximal torus of $G$. For this it suffices to find a maximal torus $T$ of $C$, for then $T$
will be a maximal torus of $G$ (since for every $s \in S$, $G_{s}$ and $C_{s}$ have the same reductive rank). By (IX,
5.6 b)) $T$ lies in the center of $C$, hence $C \subset C' = Centr_{G}(T)$, and then $C$ is a smooth subgroup of the
smooth group $C'$ over $S$, coinciding with $C'$ fiber by fiber, whence $C = C'$. Now since $G$ is of locally constant
reductive rank, the same holds for $C$, hence $C$ admits a maximal torus locally for the étale topology by 1.7 b), and
since this torus is central by the preceding reasoning, it follows by 1.13 that $C$ does admit a maximal torus, which
completes the proof.

**Corollary 3.3.** *Let $G$ be a smooth and affine $S$-prescheme in groups over $S$ of locally constant reductive rank,
and let $\mathcal{C} : (Sch)^{\circ}/S \to (Ens)$ be the functor defined by*

```text
𝒞(S′) = the set of Cartan subgroups of G_{S′}.
```

*Then the functor $\mathcal{C}$ is isomorphic to the functor $\mathcal{T}$ of 1.10, hence is representable by the same
smooth, separated prescheme of finite type over $S$.*

<!-- label: III.XII.3.3 -->

**Corollary 3.4.** *Under the conditions of 3.2, if $C = Centr_{G}(T)$, one has*

$$ Norm_{G}(C) = Norm_{G}(T). $$

<!-- label: III.XII.3.4 -->

<!-- original page 198 -->

**Remark 3.5.** *When $G$ is not of locally constant reductive rank, it is nevertheless possible that $G$ admit Cartan
subgroups (for example if $G$ has connected nilpotent fibers, $G$ is a Cartan subgroup of itself, but is not necessarily
of locally constant reductive rank, cf. 1.6). In XV, we develop the theory of Cartan subgroups without supposing $G$
affine over $S$ or of locally constant reductive rank, using the theory of regular elements of the next Exposé. See also
Nos. 6 and 7 for the elimination of the affine hypothesis.*

<!-- label: III.XII.3.5 -->

## 4. The reductive center

<!-- label: III.XII.4 -->

**Definition 4.1.** *Let $S$ be a prescheme, $G$ an $S$-group of finite presentation over $S$, with affine fibers, $Z$ a
group subpreschema of $G$. One says that $Z$ is a* reductive center of $G$ *if*

*(i) $Z$ is central, and of multiplicative type, and*

*(ii) for every base change $S' \to S$ and every central homomorphism $u : H \to G_{S'}$, where $H$ is a group of
multiplicative type and of finite type over $S'$, $u$ factors through $Z_{S'}$.*

<!-- label: III.XII.4.1 -->

*(For a variant of this notion when the fibers of $G$ are not supposed affine, cf. 8.6.)*

Note that such a $Z$ is necessarily of finite type over $S$ (since its fibers are), hence is uniquely determined as the
largest central multiplicative-type subgroup of $G$. It is easy to give examples where $G$ (smooth and affine over $S$)
admits a largest central multiplicative-type subgroup $Z$, but where $Z$ is not a reductive center (i.e. $G$ does not
admit a reductive center), cf. for example 1.6; it follows however easily from (IX, 6.8) that a subgroup $Z$ of $G$ is a
reductive center of $G$ if and only if it is a largest central multiplicative-type subgroup, and retains this property
under any base change; see also 4.3 below.

<!-- original page 199 -->

It is evident from 4.1 that if $Z$ is the reductive center of $G$, then for every base change $S' \to S$, $Z_{S'}$ is
the reductive center of $G_{S'}$. From this, and from the uniqueness of the reductive center, follows, thanks to the
theory of faithfully flat quasi-compact descent (SGA 1, VIII):

**Proposition 4.2.** *Let $G$ be an $S$-prescheme in groups of finite presentation over $S$ and with affine fibers. If
$G$ admits a reductive center locally for the faithfully flat quasi-compact topology, then it admits a reductive center.
For $Z$ to be a reductive center of $G$, it is necessary and sufficient that it be so locally for the fpqc topology.*

<!-- label: III.XII.4.2 -->

Let us also note:

**Proposition 4.3.** *Let $G$ be an $S$-prescheme in groups of finite presentation and with affine fibers, $Z$ a group
subpreschema. For $Z$ to be a reductive center of $G$, it is necessary and sufficient that it be of multiplicative type,
and that for every $s \in S$, $Z_{s}$ be a reductive center of $G_{s}$.*

<!-- label: III.XII.4.3 -->

Indeed, it follows first from (IX, 5.6 b)) that $Z$ is then central. Since the conditions envisaged are stable under
base change, it remains to prove that any central homomorphism $u : H \to G$, with $H$ of multiplicative type and of
finite type, factors through $Z$. Now, $Z$ being central, $u$ and the canonical immersion $v : Z \to G$ define a group
homomorphism

```text
w : H ×_S Z ⟶ G.
```

By (IX, 6.8) this last admits an image group $K$, which is a multiplicative-type subgroup of $G$, and everything reduces
to proving that $K = Z$. Now this is true fiber by fiber by the hypothesis on $Z$, and it now suffices to apply (IX, 5.1
bis), which completes the proof of 4.3.

One will note that in criterion 4.3, the hypothesis that for every $s \in S$, $Z_{s}$ is the reductive center of $G_{s}$
is in fact purely geometric, i.e. it suffices to verify it on the algebraic closure of $\kappa(s)$, as follows from the
second assertion of 4.2.

**Theorem 4.4.** *Let $G$ be an affine algebraic group over a field $k$. Then $G$*

<!-- original page 200 -->

*admits a reductive center.*

<!-- label: III.XII.4.4 -->

Since the center of $G$ is representable by a closed subgroup of $G$ (VIII, 6.7), one is immediately reduced to the case
where $G$ is commutative. Furthermore, by 4.2 one may suppose $k$ algebraically closed. We shall see in XVII that in
this case $G$ is written as a product $Z \times U$, where $Z$ is of multiplicative type and $U$ is "unipotent", from
which it will follow at once that $Z$ is indeed a reductive center of $G$. We shall give here a proof independent of the
structure theorem for commutative algebraic groups in the general form just indicated.

Note that it follows from (IX, 6.8) that the set of multiplicative-type subgroups $H$ of $G$ is filtered upward. We show
that it admits a largest element.

When $G$ is smooth over $k$, one applies the structure theorem *BIBLE* 4 th. 4,

$$ G = G_{s} \times G_{u}, $$

with $G_{s}$ of multiplicative type and $G_{u}$ "unipotent", which means here that $G_{u}$ admits a composition series
whose factors are subgroups (smooth if one insists) of $G_{a}$. (Indeed, $G_{u}/G^{0}_{u}$ is a unipotent group by
*BIBLE* 4 cor. to th. 3, hence a $p$-group where $p$ is the characteristic exponent, thanks to *BIBLE* 4 prop. 4; on the
other hand, $G^{0}_{u}$ admits a composition series with connected smooth quotients of dimension 1 by *BIBLE* 6 th. 1
cor. 1, and these are isomorphic to $G_{a}$ by *BIBLE* 7 th. 4.) Now one sees easily (cf. the lemma below) that every
homomorphism from a multiplicative-type group to $G_{a}$, and hence also to $G_{u}$, is trivial, which proves indeed
that every multiplicative-type subgroup of $G$ is contained in $G_{s}$.

In the general case, consider the subgroup

$$ G_{0} = G_{red} $$

of $G$, which is smooth over $k$, hence by the foregoing admits a largest <!-- original page 201 --> multiplicative-type
subgroup `Z_0`. The multiplicative-type subgroups of $G$ containing `Z_0` correspond to multiplicative-type subgroups of
$G^{0} = G/Z_{0}$. Now one has an exact sequence

$$ 0 \longrightarrow G_{0}/Z_{0} \longrightarrow G/Z_{0} \longrightarrow G/G_{0} \longrightarrow 0, $$

where by the foregoing, $G_{0}/Z_{0}$ has no multiplicative-type subgroup except the unit group. Since a subgroup of a
multiplicative-type group is of multiplicative type (IX, 8), it follows that for every multiplicative-type subgroup $H$
of $G/Z_{0}$, one has $H \cap (G_{0}/Z_{0}) = 0$, hence $H \to G/G_{0}$ is injective. Since $G/G_{0}$ is a radicial
algebraic group, hence finite over $k$, this implies that $H$ is itself radicial and of rank bounded by that of
$G/G_{0}$. This implies that the family of multiplicative-type subgroups of $G$ admits a largest element, say $Z$.

I claim that $G/Z$ has no multiplicative-type subgroup other than the unit subgroup. This follows from the fact (proved
in 7.1.1) that a commutative extension of two multiplicative-type algebraic groups is of multiplicative type: if then
$Z'$ is the inverse image in $G$ of a multiplicative-type subgroup of $G/Z$, then $Z'$ is of multiplicative type, hence
$Z' = Z$ by the maximal character of $Z$, hence $Z'/Z = 0$.

It now easily follows from the "principle of finite extension" that for any extension $K$ of $k$, $(G/Z)_{K} =
G_{K}/Z_{K}$ likewise has no multiplicative-type subgroup except the unit group.

We can now prove that $Z$ is a reductive center of $G$. Indeed, let $u : H \to G_{S}$ be a homomorphism of $S$-groups,
where $S$ is a prescheme over $k$ and $H$ a multiplicative-type group of finite type over $S$; we prove that $u$ factors
through `Z_S`. This amounts to saying that the composite homomorphism $H \to G_{S} \to (G/Z)_{S} = G_{S}/Z_{S}$ is zero.
Now setting $U = G/Z$, I claim that every homomorphism $u : H \to U_{S}$ is zero. Indeed, by (IX, 5.2) one is reduced to
the case where $S$ is the spectrum of a field, and by (IX, 6.8) this then follows from the fact that `U_K` has no
multiplicative-type subgroup other than `0`. <!-- original page 202 --> This completes the proof of 4.4. It only remains
to give the proof of the

**Lemma 4.4.1.** *Let $H$ be a multiplicative-type $S$-prescheme in groups; then every homomorphism of $S$-groups $u : H
\to G_{a}$ is trivial.*

<!-- label: III.XII.4.4.1 -->

Indeed, consider the module $O^{2}_{S} = E$ as an extension of $O_{S} = E'$ by $O_{S} = E''$; then $G_{a}$ identifies
with the prescheme of automorphisms of this extension, hence a homomorphism $u : H \to G_{a}$ identifies with an
$H$-module structure on $E$ respecting the extension structure, i.e. such that $E'$ is stable under $H$ and the
operations induced by $H$ on $E'$ and $E''$ are trivial. By (I, 4.7.3) it follows that $H$ operates trivially on $E$,
hence $u$ is trivial. QED.

**Remark 4.4.2.** *If $G$ is a nonzero abelian variety over $k$, then $G$ does not admit a reductive center in the sense
of 4.1 with the restriction "$G$ affine" omitted, because for $n$ coprime to the characteristic, ${}_{n} G$ is étale
over $k$ of order prime to the characteristic, hence of multiplicative type; now the family of ${}_{n} G$ is
schematically dense in $G$, so that if there were a reductive center, it would be identical to $G$, which is absurd,
since $G$ is not of multiplicative type. This is the reason why it is appropriate in 4.1 to impose the restriction that
$G$ have affine fibers.*

<!-- label: III.XII.4.4.2 -->

**Lemma 4.5.** *Let $S$ be a prescheme, $G$ a smooth $S$-prescheme in groups over $S$, affine over $S$, with connected
fibers, $T$ a maximal torus of $G$, $u : H \to G$ a central homomorphism, with $H$ a multiplicative-type $S$-prescheme
in groups of finite type. Then $u$ factors through $T$.*

<!-- label: III.XII.4.5 -->

Indeed, let $C$ be the centralizer of $T$, which is a closed group subpreschema of $G$ smooth over $S$ (XI, 5.3), hence
affine over $S$. Since $T$ is in the center of $C$, it is invariant, and one may consider the quotient group $C/T = U$,
which is representable (VIII, 5.1). Since $u$ is central, it factors through $C$, and everything reduces to proving that
    <!-- original page 203 --> the composite homomorphism $H \to C \to U = C/T$ is trivial. By (IX, 5.2) one is reduced to the
case where $S$ is the spectrum of a field, which one may suppose algebraically closed. But then by *BIBLE* 6, th. 2, $U$
is a connected algebraic group (smooth over $k$) which is "unipotent", meaning, as we have already observed, that it
admits a composition series with quotients isomorphic to $G_{a}$. Hence every homomorphism from a multiplicative-type
group of finite type $H$ to $U$ is trivial. This proves 4.5.

**Corollary 4.6.** *Let $G$ be as in 4.5. If $G$ admits a reductive center, the latter is contained in every maximal
torus of $G$.*

<!-- label: III.XII.4.6 -->

**Theorem 4.7.** *Let $S$ be a prescheme, $G$ an $S$-prescheme in groups, smooth over $S$, affine over $S$, with
connected fibers.*

*a) For every $s \in S$, let $z(s)$ be the type of the reductive center of $G_{s}$ (which is defined by 4.4). Order the
set $E$ of isomorphism classes of finitely generated $\mathbb{Z}$-modules, by declaring that the class of $M$ is greater
than that of $M'$ if $M'$ is*

<!-- original page 204 -->

*isomorphic to a quotient of $M$. Then the map $S \to E$, $s \mapsto z(s)$, is lower semicontinuous.*

*b) For $G$ to admit a reductive center $Z$, it is necessary and sufficient that the preceding function $z : S \to E$ be
locally constant. If this is so, $G/Z$ is representable (cf. VIII, 5.1), and $G/Z$ admits the unit subgroup as reductive
center.*

*c) Suppose that the reductive rank of $G$ is locally constant (cf. 1.7 b)). Then $G$ admits a reductive center $Z$. If
$G/Z$ is representable (for example, $G$ affine over $S$), then moreover the maximal tori $T$ of $G$ (resp. the Cartan
subgroups $C$ of $G$) and $T'$ (resp. $C'$) of $G' = G/Z$ are in bijective correspondence, to $T$ (resp. $C$)
corresponding $T' = T/Z$ (resp. $C' = C/Z$), and to $T'$ (resp. $C'$) corresponding $T = \varphi^{-1}(T')$ (resp. $C =
\varphi^{-1}(C')$), where $\varphi : G \to G'$ is the canonical homomorphism.*

*d) Let $T$ be a maximal torus of $G$, let $g$ denote the Lie algebra of $G$, and consider the homomorphism*

$$ \theta : T \longrightarrow GL(g), $$

*induced by the adjoint representation of $G$ (II, 4). Then the kernel of $\theta$ is a reductive center of $G$.*

<!-- label: III.XII.4.7 -->

*Proof.* a) and b). The proof of a) and of the first assertion of b) is essentially identical to that of 1.7 a) and b),
and we refrain from reproducing the reasoning here. We signal only that one must in a) appeal to (IX, 5.6) (using the
fact that $G$ has connected fibers). Let us prove the second assertion of b), i.e. that if $Z$ is a reductive center of
$G$, then $G' = G/Z$ admits the unit subgroup as reductive center. Note immediately that by (VIII, 5.1) the quotient
group $G/Z$ is indeed representable; it is affine over $S$, of finite presentation over $S$ (VIII, 5.8) and even smooth
over $S$ (for it suffices to see this on the fibers, $G'$ being flat of finite presentation over $S$; now on the fibers
we signaled in (VI_B, 9.2.(xii)) that a quotient of a smooth algebraic group over a field $k$ is smooth); finally, $G$
having connected fibers, the same holds for $G'$. Thus $G'$ satisfies the same starting hypotheses as $G$. To see that
the unit subgroup of $G'$ is a reductive center, we may restrict if we wish to the case where $S$ is the spectrum of a
field (4.3). Let $Z'$ be a central multiplicative-type subgroup of $G'$; everything reduces to proving that $Z'$ is
reduced to the unit group. Let `Z_1` be the inverse image of $Z'$ in $G$, and consider the operations of `Z_1` on $G$
induced by inner automorphisms of $G$. Since $Z$ is central, $Z$ operates trivially, so `Z_1` operates by way of
operations of $Z'$ on $G$. Moreover $Z$ being in the center of $G$, `Z_1` and hence $Z'$ operate trivially on $Z$; in
addition $Z'$ being in the center of $G'$, <!-- original page 205 --> the operations of $Z'$ on the quotient $G/Z = G'$
are also trivial. Since $Z$ is central, it follows at once that the operations of $Z'$ on $G$ come from a group
homomorphism

```text
u : Z′ ⟶ Hom_{S-gr}(G′, Z),
```

by

```text
r(z′) · g = g · u(z′)(ϕ(g)),
```

where $r : Z' \to \operatorname{Aut}_{S-gr}(G)$ is the envisaged representation of $Z'$ by automorphisms of $G$, and
$\varphi : G \to G'$ the canonical homomorphism. Now the datum of a group homomorphism $u$ as above amounts to the datum
of a group homomorphism

```text
v : G′ ⟶ Hom_{S-gr}(Z′, Z),
```

on the other hand by (X, 5.8) the right-hand side is representable and is an étale group over $S$, hence its unit
section is an open immersion, hence `Ker v` is an open subgroup of $G'$. Since $G'$ has connected fibers, it is equal to
$G'$, hence $v$ is zero, hence $u$ is zero, hence $Z'$ operates trivially on $G$, hence the same holds for `Z_1`, which
is therefore central in $G$. Thus `Z_1` is a commutative extension of a multiplicative- type group $Z'$ by a
multiplicative-type group $Z$, hence (since we are over a field) is a multiplicative-type group (7.1.1). Being central
in $G$, it is contained in the reductive center $Z$, i.e. $Z_{1} = Z$, whence $Z' =$ unit group, which completes the
proof of b).

d) Let $Z = Ker \theta$, which is a multiplicative-type subgroup of $T$ (e.g. by (IX, 6.8)). By 4.5, every central
homomorphism $u : H \to G$, with $H$ of multiplicative type and of finite type, factors through $T$, hence through $Z$.
Since the formation of $Z$ is compatible with any base change, it remains to prove that $Z$ is central, i.e. that the
centralizer $C$ of $Z$ equals $G$. Now by (XI, 5.3), $C$ is a closed smooth subgroup of $G$; on the other hand, since
$Z$ operates trivially on <!-- original page 206 --> $g$, one sees that $Lie(C) = g$. One easily concludes that $C = G$:
indeed, the immersion $C \to G$ is étale, since it is so fiber by fiber (being an unramified homomorphism of smooth
algebraic groups of the same dimension, VI_B, 1.3), and one may apply (X, 3.5). Thus $C \to G$ is an étale closed
immersion, hence an open immersion (SGA 1, I 5.1), and since it is also a closed immersion and $G$ has connected fibers,
it is an isomorphism.

c) By 1.7 b), $G$ admits a maximal torus locally for the fpqc topology, hence by 4.2 and by d) which we have just
proved, $G$ admits a reductive center $Z$. We saw in d) that every maximal torus $T$ of $G$ contains $Z$. One sees at
once that $T' = T/Z$ is a torus; to prove that it is a maximal torus in $G'$, one is reduced by Definition 1.3 to the
case where $S$ is the spectrum of an algebraically closed field, and then the assertion is contained in *BIBLE* 7 th. 3
a). Conversely, let $T'$ be a maximal torus of $G'$, and let $T = \varphi^{-1}(T')$; we prove that $T$ is a maximal
torus of $G$. The question being local for the fpqc topology, we may suppose that $G$ already admits a maximal torus,
say `T_0`, so that by the foregoing, $T'_{0} = T_{0}/Z_{0}$ is a maximal torus of $G'$. By the conjugation theorem 1.7
c), $T'$ and $T'_{0}$ are locally conjugate for the fpqc topology, hence (since $\varphi : G \to G'$ is covering for
this topology, so every section of $G'$ lifts locally to a section of $G$) $T$ and `T_0` are also locally conjugate.
Since `T_0` is a maximal torus, the same therefore holds for $T$. One proceeds analogously for the Cartan subgroups.
This completes the proof.

Let us give a useful translation of d), in the case where $T$ is diagonalizable, hence of the form $D_{S}(M)$, where $M$
is a finitely generated free $\mathbb{Z}$-module. Then (I, 4.7.3) the $T$-module <!-- original page 207 --> $g$
decomposes as a direct sum of $T$-submodules $g_{m}$ ($m \in M$):

```text
g = ⨁_{m ∈ M} g_m,
```

which are necessarily locally free. Suppose that for every $m \in M$, the rank of $g_{m}$ is constant (which is the case
in particular if $S$ is connected). Then the set $R$ of $m \in M$ such that $g_{m} \neq 0$ ("roots") is finite. With
this stated:

**Corollary 4.8.** *Under the preceding conditions and with the preceding notations, the reductive center of $G$ is the
intersection of the kernels of the root characters $m \in R$ on $T$. One thus has an isomorphism*

$$ Z \simeq D_{S}(N), $$

*where $N$ is the quotient of $M$ by the subgroup generated by $R$.*

<!-- label: III.XII.4.8 -->

**Corollary 4.9.** *Let $G$ be an algebraic group over an algebraically closed field $k$. Suppose $G$ smooth over $k$,
connected affine, with reductive center reduced to the unit group, and that the Lie algebra $g$ of $G$ is nilpotent.
Then $G$ is "unipotent", i.e. admits a composition series with quotients isomorphic to $G_{a}$.*

<!-- label: III.XII.4.9 -->

By *BIBLE* 6, th. 4, cor. 3 it suffices to prove that a maximal torus $T$ of $G$ is reduced to the unit group, or
equivalently that the Lie algebra $t$ of $T$ is reduced to `0`. Now it follows from the fact that the $T$-module $g$
decomposes according to the characters $\alpha$ of $T$ (I, 4.7.3) that for every $t \in t$, the operation $ad_{g}(t)$ on
$g$ is semisimple. If then $g$ is nilpotent, $ad_{g}(t)$ is zero. Now by 4.7 d), the reductive center of $G$ being
reduced to the identity element, the homomorphism $T \to GL(g)$ is a monomorphism, hence induces an injective
application on the Lie algebras, which means (II, 4.5) that for $t \in t$, the relation $ad_{g}(t) = 0$ implies $t = 0$.
This proves that $t = 0$ and completes the proof.

**Proposition 4.10.** *Let $G$ be an affine, smooth, connected algebraic group over an algebraically closed field $k$.
Then the reductive center of $G$ is the intersection of the maximal tori of $G$.*

<!-- label: III.XII.4.10 -->

<!-- original page 208 -->

Of course, this is the intersection in the schematic sense (or equivalently, in the sense of subfunctors of $G$), i.e.
the largest closed subpreschema of $G$ majorized by the maximal tori of $G$. It follows from the noetherian character of
$G$ that this is also the intersection of a suitable finite set of maximal tori of $G$.

Let $Z$ be the intersection in question; $Z$ is a closed subgroup of a torus, hence of multiplicative type; on the other
hand by 4.5 it contains the reductive center of $G$. To prove that it is equal, it remains to prove that it is central.
Since $G$ is connected, it suffices by (IX, 5.5) to prove that $Z$ is invariant. Now by construction $Z$ is invariant
under the $int(g)$, with $g \in G(k)$, hence the normalizer $N$ of $Z$ (cf. VIII, 6.7) is a closed subgroup of $G$
containing the rational points of $G$. Since $G$ is reduced, one has $N = G$, which completes the proof.

**Proposition 4.11.** *Let $S$ be a prescheme, $G$ a smooth $S$-prescheme in groups over $S$, affine over $S$, with
connected fibers, and of zero unipotent rank, which implies* *(1.9) that*

<!-- original page 209 -->

*$G$ is of locally constant reductive rank, hence (1.10) that the "prescheme of maximal tori of $G$" is defined, say
$\mathcal{T}$, and is smooth, separated, of finite type over $S$. Let $G$ operate on $\mathcal{T}$ via inner
automorphisms, whence a homomorphism of group functors*

$$ u : G \longrightarrow \operatorname{Aut}_{S}(\mathcal{T}). $$

*Under these conditions, the following three subfunctors of $G$ are identical:*

*(i) The reductive center $Z$ of $G$.*

*(ii) The center $Z'$ of $G$.*

*(iii) The kernel $Z'' = Ker u$ of the preceding homomorphism.*

*In particular, the center of $G$ is representable by a multiplicative-type subgroup of $G$.*

<!-- label: III.XII.4.11 -->

*Proof.* One has trivially $Z \subset Z' \subset Z''$; it remains to prove that $Z'' \subset Z$, which amounts to
proving (the hypotheses being stable under base change) that every section $g$ of $G$ over $S$ which operates trivially
on $\mathcal{T}$ is a section of $Z$. Introducing $G' = G/Z$ and using 4.7 b) and c), which imply in particular that the
prescheme $\mathcal{T}'$ of maximal tori of $G'$ is canonically isomorphic to $\mathcal{T}$, one is reduced to the case
where $G = G'$, i.e. to the case where the reductive center $Z$ of $G$ is zero. (N.B. note that by 4.7 c), the unipotent
rank of $G'$ equals that of $G$, hence is zero since that of $G$ is zero.) It thus remains to prove in this case that
$g$ is the unit section of $G$. The usual reduction procedure brings us to the case where $S$ is noetherian, and even to
the case where $S$ is local artinian (since to verify that $g$ is the unit section it suffices to verify when $S$ is
locally noetherian that this is so after any base change $S' \to S$ with $S'$ local artinian). Now in this case the
kernel $Z''$ of $u$ is representable (VIII, 6.2 a) and 6.5 c)) (Note that $Z''$ is representable by (XI, 6.8)). To prove
that $Z''$ is reduced to the unit subgroup, it suffices by Nakayama to prove that the same holds for its fiber
$Z''_{0}$. This thus reduces us to the case where $S$ is the spectrum of a field $k$, which one may evidently suppose
algebraically closed. Now $Z''$ is contained in the stabilizer of every point of $\mathcal{T}(k)$, i.e. in the
normalizer $N(T)$ of every maximal torus $T$ of $G$. Since the reductive rank of $G$ is zero, it follows by (XI, 5.9)
that $T$ is an open subgroup of $N(T)$, hence the Lie algebra of $N(T)$ is identical to that of $T$. Hence the Lie
algebra of $Z''$ is contained in that of $T$. On the other hand, it follows from 4.10 that the intersection of the Lie
algebras of the maximal tori $T$ of $G$ is none other than the Lie algebra of the reductive center $Z$, hence here zero,
since we have assumed $Z = 0$. Consequently, the Lie algebra of $Z''$ is zero, i.e. $Z''$ is étale over $k$. Moreover
$Z''$ is evidently invariant in $G$, and since $G$ is connected it follows easily that $Z''$ is in the center of $G$. It
is therefore in $T = Centr_{G}(T)$ for every maximal torus $T$, hence in the intersection of the maximal tori, i.e. in
$Z = 0$ by 4.10, which completes the proof.

## 5. Application to the scheme of multiplicative-type subgroups[^XII-5-0]

<!-- label: III.XII.5 -->

<!-- original page 210 -->

**Theorem 5.1.** *Let $S$ be a prescheme, $G$ a smooth and affine $S$-prescheme in groups over $S$, $M$ the "prescheme
of multiplicative-type subgroups of $G$", representing the* *functor explicit in (XI, 4.1). For every integer $n > 0$,
let $T_{n}$ be the subfunctor of $M$ such that $T_{n}(S') =$ the set of multiplicative-type group subpreschemata $H$ of
$G_{S'}$ such that $n \cdot id_{H} = 0$, so that $T_{n}$ is representable, and is affine over $S$ (XI, 3.12 a)). Let
$u_{n} : M \to T_{n}$ be the morphism defined by $u_{n}(H) = {}_{n} H$ (where ${}_{n} H = Ker(n \cdot id_{H})$). With
these notations, one has the following:*

*a) Every subpreschema $U$ of $M$ of finite type over $S$ is contained in a closed subpreschema of finite type over $S$,
and every closed subpreschema $X$ of $M$ of finite type over $S$ is affine over $S$.*

*b) Suppose $S$ quasi-compact, and let $X$ be a closed subpreschema of $M$ of finite type over $S$. Then there exists an
integer $n > 0$ such that for every multiple $m$ of $n$, the induced morphism*

$$ u_{m}|X : X \longrightarrow T_{m} $$

*is a closed immersion.*

<!-- label: III.XII.5.1 -->

*Proof.* a) To prove the first assertion of a), one takes for $X$ the schematic closure of $U$ ([EGA I, 9.5.1](https://jcreinhold.github.io/ega/i/01-09-complements-on-quasi-coherent-sheaves.html#95-closed-image-of-a-prescheme-closure-of-a-subprescheme) and 9.5.3),
which is defined since the immersion $i : U \to M$ is quasi-compact (because $U$ is of finite type over $S$ and $M$ is
separated over $S$ (4.1)). It therefore remains to prove that such an $X$ is affine over $S$, which will prove at the
same time the second assertion of a). In the foregoing form, one sees that the question is local on $S$, which one may
therefore suppose affine. Then $U$, being of finite type over $S$, is contained in a quasi-compact open of $M$, and this
brings us to the case where $U$ itself is <!-- original page 211 --> an open, of finite type over $S$, i.e.
quasi-compact. (N.B. A closed subscheme of a scheme affine over $S$ is affine over $S$.)

It suffices to prove that such a $U$ is majorized by a closed subpreschema of $M$ which is affine. In this form, the
usual reduction procedure brings us at once to the case where $S$ is noetherian. One proceeds similarly for b), which
reduces to the case where $S$ is affine noetherian.

Let us take up again the inverse limit $T$ of the $T_{n}$ used in the proof of (XI, 4.1), which is an affine prescheme
(but not of finite type) over $S$, and whose local rings are noetherian, as was seen at the beginning of the proof of
(IX, 3.7). (N.B. For $t \in T$, $t = (t_{n})$, the transition morphisms $T_{m} \to T_{n}$ being smooth and the dimension
of the $T_{m}$ being bounded, there exists an $n_{0}$ such that the $T_{n} \to T_{n_{0}}$ are étale at $t_{n}$ for every
$n$ multiple of $n_{0}$.) The proof of *loc. cit.*, or (XI, 3.11), show that the canonical morphism

$$ u : M \longrightarrow T $$

is an immersion, and induces isomorphisms on the local rings (but one will note that $u$ is not in general an open
immersion nor a quasi-compact morphism). Let $U$ be a quasi-compact open of $M$; we shall prove that its closure in $T$
is contained in $M$, which proves (if $X$ denotes the schematic closure of $U$ in $M$) that $u|X : X \to T$ is a closed
immersion, hence that $X$ is affine, and that will prove a). Since $U$ is noetherian, it has only finitely many
irreducible components, and every element $t \in T$ in the closure of $U$ is a specialization of an element $x$ of $U$.
Since the local ring of $t$ in $T$ is noetherian, the same holds for the local ring $A$ of $t$ in $\bar{x}$ endowed with
the induced reduced structure.

The canonical morphism of the noetherian integral local scheme $S' = \operatorname{Spec}(A)$ into $T$ then sends the closed point of
$S'$ to $t$, the generic point to $x \in M$, and one must show under these conditions that $t \in M$. Possibly replacing $A$
by the quotient of a suitable complete local $A$-algebra flat over $A$ ([EGA 0_III, 10.3.1](https://jcreinhold.github.io/ega/iii/03-ch0-10-complements-flat-modules.html#103-existence-of-flat-extensions-of-local-rings)) by a minimal prime ideal, we
may suppose that $A$ is complete with algebraically closed residue field, (and <!-- original page 212 --> we could even
reduce to the case where it is moreover a discrete valuation ring thanks to EGA II, 7.1.7). One is thus reduced (making
the change of notation: $S'$ denoted by $S$) to the

**Lemma 5.2.** *Let $S$ be the spectrum of a complete noetherian integral local ring with algebraically closed residue
field, $G$ a smooth and affine $S$-prescheme in groups over $S$, $(H(n))_{n > 0}$ a system of multiplicative-type
subgroups of $G$, indexed by the integers $n > 0$, $\eta$ the generic point of $S$. Suppose:*

*a) If $m$ is a multiple of $n$, one has $H(n) = {}_{n} H(m)$.*

*b) There exists a multiplicative-type subgroup $H_{\eta}$ of $G_{\eta}$ such that one has $H(n)_{\eta} =
{}_{n}(H_{\eta})$ for every $n > 0$.*

*Under these conditions, there exists a multiplicative-type subgroup $H$ of $G$ such that for every $n > 0$, one has
$H(n) = {}_{n} H$.*

<!-- label: III.XII.5.2 -->

For each $n$, let $C_{n} = Centr_{G}(H(n))$, which is a closed group subpreschema of $G$, smooth over $S$ (XI, 5.3). The
set of integers $n > 0$ being ordered by divisibility, the $C_{n}$ form a decreasing family of closed subpreschemata of
$G$, and since $G$ is noetherian, this family is stationary. Let $C$ be the common value of the $C_{n}$ for $n$ large.
Then $C$ satisfies the same conditions as $G$; moreover the $H(n)$ are in fact subgroups of $C$. Hence, replacing $G$ by
$C$, we may suppose that the $H(n)$ are central subgroups of $G$.

Let then $s$ be the closed point of $S$, and $Z_{s}$ the reductive center of $G_{s}$ (defined thanks to 4.4). By the
definition (4.1) $Z_{s}$ contains the $H(n)_{s}$. Since $A$ is complete, $Z_{s}$ comes from a multiplicative-type group
subpreschema $Z$ of $G$ (XI, 5.8). I claim that $Z$ contains the $H(n)$. Indeed, since $H(n)$ is central, it commutes
with $Z$ in $G$, hence one deduces a group homomorphism $Z \times H(n) \to G$, which by (IX, 6.8) admits an image group
which is a multiplicative-type subgroup $K$ of $G$ containing $Z$, and <!-- original page 213 --> everything reduces to
proving that $K = Z$, which follows from $K_{s} = Z_{s}$ and (IX, 5.1 bis).

One is thus reduced to proving the analogue of 5.2, but with $G$ replaced by a group $Z$ of multiplicative type and of
finite type over $S$ (not necessarily smooth over $S$). Since $A$ is complete with algebraically closed residue field,
$Z$ is diagonalizable (X, 3.3 and 1.4), hence of the form $D_{S}(M)$, with $M$ a finitely generated commutative group.
Consequently every multiplicative-type subgroup $H$ of $Z$ is diagonalizable (IX, 2.11 (i)), hence of the form
$D_{S}(N)$, where $N$ is a quotient group of $M$ (VIII, 3.2). Thus the $H(n)$ correspond to quotient groups $M(n)$ of
$M$, and the existence of a multiplicative-type subgroup $H$ of $Z$ such that $H(n) = {}_{n} H$ for every $n$ amounts to
that of a quotient group $N$ of $M$ such that $M(n) = N/nN$ for every $n$. Now this follows at once from the fact that
there exists a subgroup $H_{\eta}$ of $G_{\eta}$ such that $H(n)_{\eta} = {}_{n}(H_{\eta})$ for every $n$. This
completes the proof of 5.2 and hence of a).

b) We already know that $u|X : X \to T$ is a closed immersion. It easily follows that for $m$ large, the composite
$u_{m}|X : X \to T_{m}$ is also a closed immersion. Since we will not need this fact in the sequel, we omit the details
of the proof.

**Corollary 5.3.** *With the notations of 5.1, let $U$ be a part of $M$ both open and closed, of finite type over $S$.
Then $U$ is affine over $S$ for the structure induced by $M$, and if $S$ is quasi-compact, there exists an integer $n >
0$ such that for every multiple $m$ of $n$, the induced morphism $u_{m}|U : U \to T_{m}$ is an open and closed immersion
(i.e. an isomorphism onto an open and closed part of $T_{m}$, equipped with the induced structure).*

<!-- label: III.XII.5.3 -->

The first assertion follows from 5.1 a), the second from 5.1 b), taking into account that $u_{m} : M \to T_{m}$ is
smooth (XI, 2.2 bis) and that a smooth immersion, i.e. étale, is an open immersion.

<!-- original page 214 -->

**Corollary 5.4.** *Let $S$ be a prescheme, $G$ a smooth and affine $S$-prescheme in groups over $S$, of locally
constant reductive rank (1.7 b)), $\mathcal{T}$ the "prescheme of maximal tori of $G$" (1.10). Then $\mathcal{T}$ is
smooth and affine over $S$. If $T$ is a maximal torus of $G$, $N(T)$ its normalizer, then $G/N(T)$ (XI, 5.3 bis) is
affine over $S$. The same holds for $G/C(T)$ (where $C(T)$ is the centralizer of $T$) provided that $W(T) = N(T)/C(T)$
is finite over $S$ (cf. 2.1 b)).*

<!-- label: III.XII.5.4 -->

The second assertion is contained in the first, since by the conjugation theorem, $G/N(T)$ is isomorphic to
$\mathcal{T}$ (XI, 5.5 bis). For the first assertion, one notes that by construction, $\mathcal{T}$ is isomorphic to an
open and closed subpreschema of $M$ (for one may suppose the reductive rank of $G$ constant and equal to $r$, and then
$\mathcal{T}$ is the subpreschema of $M$ corresponding to the subtori of relative dimension $r$, i.e. the largest
subpreschema of $M$ over which the "universal multiplicative-type subgroup" $H \subset G_{M}$ is a torus of relative
dimension $r$). One may therefore apply 5.3. Finally, for the last assertion, one notes that $G/C(T)$ is finite over
$G/N(T) \simeq (G/C(T))/W(T)$, hence is affine since $G/N(T)$ is.

**Corollary 5.5.** *Let $G$ be a smooth and affine algebraic group over a field $k$. Then the scheme $M$ of
multiplicative-type subgroups of $G$ is a direct sum of affine schemes over $S$. For every multiplicative-type subgroup
$H$ of $G$, if $C$ and $N$ denote respectively its centralizer and its normalizer, the quotients $G/C$ and $G/N$ are
affine.*

<!-- label: III.XII.5.5 -->

Using (XI, 5.1 bis), one sees that the saturation under $G$ operating on $M$ of any finite closed part of $M$ is open:
indeed, one is reduced to the case where $k$ is algebraically closed, hence to the case of the trajectory of a
$k$-rational point $x$, but then by *loc. cit.* the morphism $g \mapsto g \cdot x$ from $G$ to $M$ is smooth hence open,
hence its image is open. Let $U$ be the union of the classes of the closed points of $M$ for the equivalence relation
defined by the operations of $G$. Then $U$ is open and contains every closed point of $M$, <!-- original page 215 -->
hence by the Nullstellensatz is identical to $M$. Thus $M$ is a disjoint union of opens, which are therefore necessarily
closed, hence $M$ is the sum prescheme of preschemata $M_{i}$, each of which is a $G$-trajectory of a closed point,
hence is quasi-compact, hence of finite type. By 5.3 the $M_{i}$ are therefore affine. If $H$ is a multiplicative-type
subgroup of $G$, it corresponds to a $k$-rational point $x$ of $M$, and $G/N$ identifies with the trajectory of $x$
under $G$ (XI, 5.5 bis). It is therefore affine by the foregoing. Since $C$ is an open subgroup of $N$ (XI, 5.9), $G/C$
is finite over $G/N$ (since the latter is isomorphic to $(G/C)/(N/C)$), hence affine since $G/C$ is.

This proof shows at the same time:

**Corollary 5.6.** *Under the conditions of 5.5 for $G$ and $H$, the subscheme $U$ of $M$ "of multiplicative-type
subgroups of $G$ that are locally conjugate to $H$" is an open and closed subpreschema of $G$.*

<!-- label: III.XII.5.6 -->

In picturesque language, every multiplicative-type subgroup $H'$ of $G$ that is a limit of subgroups of $G$ conjugate to
$H$, is itself conjugate to $H$.

**Remarks 5.7.** *Let $S$ be a prescheme, $G$ a smooth and affine $S$-prescheme over $S$, $H$ an $S$-prescheme of
multiplicative type and of finite type, and set $M = \operatorname{Hom}_{S-gr}(H, G)$, which by (XI, 4.2) is
representable and is smooth over $S$ and separated over $S$. One can then prove for $M$ a result entirely analogous to
5.1, either by reducing to 5.1 by an argument analogous to that of (XI, 4.2), or by proceeding directly by an argument
modeled on that of 5.1. From this one deduces corresponding variants for 5.3, 5.5, 5.6, which the reader will
formulate.*

<!-- label: III.XII.5.7 -->

## 6. Maximal tori and Cartan subgroups of not-necessarily-affine algebraic groups (algebraically closed base field)

<!-- label: III.XII.6 -->

<!-- original page 216 -->

**Lemma 6.1.** *Let $G$ be a connected algebraic group over a field $k$, $Z$ an algebraic subgroup of finite index in
its center; then $G/Z$ is affine.*

<!-- label: III.XII.6.1 -->

One may suppose that $Z$ is the center of $G$, since a scheme finite over an affine scheme is affine. Consider the
vector spaces

```text
P_n = P_n(G) = O_{G,e}/m_{G,e}^{n+1}   (n an integer ⩾ 0),
```

where $m_{G,e}$ is the maximal ideal; then $G$ operates on the $P_{n}(G)$ by the adjoint representation, and if $Z_{n}$
is the kernel of the corresponding homomorphism

$$ ad_{n} : G \longrightarrow GL(P_{n}), $$

one verifies easily (using the fact that $G$ is connected) that $Z$ is the intersection of the $Z_{n}$, hence ($G$ being
noetherian) equal to one of the $Z_{n}$. But $ad_{n}$ defines, on passage to the quotient, a monomorphism $G/Z_{n} \to
GL(P_{n})$, which is therefore a closed immersion, hence $G/Z_{n}$ is affine, and consequently $G/Z$ is.

**Lemma 6.2.** *Let $G$ be a smooth algebraic group over the field $k$, $Z$ a central algebraic subgroup, $G' = G/Z$,
$u : G \to G'$ the canonical homomorphism, $T$ a multiplicative-type subgroup in $G$, $T' = u(T)$ the image group, $C$
the centralizer of $T$ in $G$, $C'$ that of $T'$ in $G'$. Then one has*

$$ C'^{0} \subset u(C). $$

<!-- label: III.XII.6.2 -->

One may suppose $k$ algebraically closed. Let

$$ C_{1} = (u^{-1}(C')^{0})_{red}, $$

it suffices to prove that $C_{1} \subset C$, since $u(C_{1})$ is connected of finite index in $C'$ <!-- original page 217 -->
hence equal set-theoretically to $C'^{0}$, hence equal to $C'^{0}$ since $C'$ and consequently $C'^{0}$ are smooth.

Consider the morphism

$$ (g, t) \mapsto gtg^{-1}t^{-1} $$

from $G \times G$ to $G$; it induces a morphism

```text
ϕ : C_1 × T ⟶ Z_1,   where Z_1 = Z_red,
```

since the left-hand side being reduced, it suffices to see that for $g \in C_{1}(k)$, $t \in T(k)$, one has
$gtg^{-1}t^{-1} \in Z(k)$, which comes from the fact that $g$ centralizes $T$ modulo $Z$. One sees easily (by computing
on $k$-rational points) that $\varphi(g, t)$ is additive in $g$ and additive in $t$, hence is "bilinear"; I claim that
(with `Z_1` smooth and `C_1` connected) this homomorphism is identically zero, which will prove indeed that $C_{1}
\subset C$. Using the density theorem for $T$, we are reduced to the case where $T$ is finite, i.e. where there exists
an integer $n > 0$ such that $n \cdot id_{T} = 0$. Note that $\varphi$ is defined by a group homomorphism

$$ C_{1} \longrightarrow \operatorname{Hom}_{S-gr}(T, Z_{1}), $$

now `Z_1` being commutative and smooth, the right-hand side is representable by an étale algebraic group over $k$, and
`C_1` being connected, every group homomorphism from `C_1` to the latter is zero. QED.

**Corollary 6.3.** *Under the preceding conditions, suppose $C'$ connected; then one has*

```text
C′ = u(C),   C = u⁻¹(C′).
```

<!-- label: III.XII.6.3 -->

Indeed, then $C' = C'^{0}$; on the other hand $C$ obviously contains $Z$, hence is equal to $u^{-1}(u(C))$.

<!-- original page 218 -->

**Lemma 6.4.** *Let $G$ be an algebraic group over the field $k$, $Z$ a central algebraic subgroup such that $G/Z = G'$
is a torus. Then $G$ is commutative, and if $k$ is algebraically closed, there exists a torus $T$ in $G$ such that $u(T)
= G'$, where $u$ is the canonical homomorphism $G \to G/Z = G'$.*

<!-- label: III.XII.6.4 -->

One may suppose $k$ algebraically closed. Consider again the morphism $G \times G \to G$ defined by
$(g, h) \mapsto ghg^{-1}h^{-1}$; then (since $Z$ is central) this morphism factors through a morphism
$G' \times G' \to G$, and since $G'$ is commutative, this latter takes its values in $Z$, and even in $Z_{1} = Z_{red}$,
since $G' \times G'$ is reduced. One sees as above that the morphism $\varphi : G' \times G' \to Z_{red}$ thus obtained
is bilinear, hence zero, which proves that $G$ is commutative. To find a torus $T$ of $G$ such that $u(T) = G'$, one may
(replacing $G$ by $G^{0}_{red}$ if necessary) suppose $G$ smooth and connected, and moreover (replacing $Z$ by
$Z^{0}_{red}$ if necessary) <!-- original page 219 --> that $Z$ is smooth and connected. By a well-known theorem of
Chevalley,[^N.D.E-XII-6] $Z$ is an extension of an abelian variety by an affine group, which reduces us at once to
proving our assertion in each of the two following cases: 1°) $Z$ is affine, 2°) $Z$ is an abelian variety. In case 1°),
$G$ is affine and the result is well known (*BIBLE* 7 th. 3 a)). Suppose then that $Z$ is an abelian variety. Since
every homomorphism from the additive group $G_{a}$ to the torus $G' = R$ or to the abelian variety $Z$ is trivial, it
follows that the same holds for every homomorphism from $G_{a}$ to $G$, hence $G$ does not contain a subgroup isomorphic
to $G_{a}$. By Chevalley's structure theorem already invoked, one has an exact sequence

$$ (\ast) 0 \longrightarrow T \longrightarrow G \longrightarrow A \longrightarrow 0, $$

where $A$ is an abelian variety, and $T$ an affine smooth connected group. Since the latter is commutative and contains
no additive subgroup, it follows that $T$ is a torus (and it is evidently the unique maximal torus of $G$). Everything
reduces to proving that every epimorphism

$$ u : G \longrightarrow R, $$

where $R$ is a torus, satisfies $u(T) = R$. Set

```text
Hom_gr(T, G_m) = M,   Hom_gr(R, G_m) = P,
```

(these are finitely generated free $\mathbb{Z}$-modules which recover $T$, $R$ up to isomorphism by $T = D_{k}(M)$, $R =
D_{k}(P)$), and let

$$ B = Ext^{1}_{k-gr}(A, G_{m}), $$

($B$ is also the set of $k$-rational points of the abelian variety dual to $A$). One evidently has

```text
(××)  Ext¹(A, T) = Hom_gr(M, B),   Ext¹(A, R) = Hom_gr(P, B),
```

in particular the extension $G$ of $A$ by $T$ is given by a homomorphism

$$ \theta : M \longrightarrow B. $$

On the other hand the exact sequence (∗) gives the exact sequence

```text
0 ⟶ Hom(A, R) ⟶ Hom(G, R) ⟶ Hom(T, R) ⟶ Ext¹(A, R),
```

moreover $\operatorname{Hom}(A, R) = 0$, and $\operatorname{Hom}(T, R) \to Ext^{1}(A, R)$ identifies with the
homomorphism

```text
Hom(P, M) ⟶ Hom(P, B)
```

deduced from $\theta : M \to B$. Setting

$$ N = Ker(\theta), $$

one therefore finds a canonical bijection

```text
Hom(G, R) ≃ Hom(P, N) ≃ Hom(S, R),   where S = D_k(N),
```

which can be described geometrically at once as follows:

<!-- original page 220 -->

**Lemma 6.5.** *Let $G$ be an extension of an abelian variety $A$ by a torus $T = D_{k}(M)$, defined by a homomorphism
$\theta : M \to B = Ext^{1}(A, G_{m})$ (base field $k$ algebraically closed). Let $N = Ker \theta$, $S = D_{k}(N)$ the
corresponding torus, isomorphic to $T/U$ where $U = D_{k}(M/N)$; consider the extension $H = G/U$ of $A$ by $S$. This
extension splits,[^N.D.E-XII-7] hence one has a unique projection of $H$ onto $S$, whence a unique homomorphism*

$$ v : G \longrightarrow S $$

*extending the canonical homomorphism $T \to S$. With this stated, for every torus $R$ and every homomorphism $u : G \to
R$, there exists a unique homomorphism $u' : S \to R$ such that $u = u'v$. In particular, one has $Im(u) = Im(u') =
u(T)$.*

<!-- label: III.XII.6.5 -->

This shows in particular that if $u$ is an epimorphism, the same holds for its restriction to $T$, which completes the
proof of 6.4.

**Theorem 6.6.** *Let $G$ be a smooth and connected algebraic group over an algebraically closed field $k$.*

*a) The maximal tori of $G$ are conjugate.*

*b) Let $T$ be a torus in $G$; then its centralizer is smooth and connected.*

*c) The map $T \mapsto Centr_{G}(T)$ establishes a bijective correspondence between the set of maximal tori $T$ of $G$
and the set of Cartan subgroups (N° 1) of $G$. For an algebraic subgroup $C$ of $G$ to be a Cartan subgroup, it is
necessary and sufficient that it be smooth, nilpotent, and set-theoretically equal to its connected normalizer (and then
it is even equal to its connected normalizer); one then has $C = Centr_{G}(T)$, where $T$ is the unique maximal torus of
$C$, and $Norm_{G}(C) = Norm_{G}(T)$.*

*d) Let $v : G \to H$ be an epimorphism of smooth connected algebraic groups; then the maximal tori (resp. the Cartan
subgroups) of $H$ are the images of the maximal tori (resp. of the Cartan subgroups) of $G$. If $T$ is a maximal torus
of $G$ and $C$ its centralizer, then $v(C)$ is the centralizer of $v(T)$.*

<!-- original page 221 -->

*e) Under the conditions of d), suppose that `Ker v` is a central subgroup of $G$; then $T \mapsto v(T)$ (resp. $C
\mapsto v(C)$) establishes a bijective correspondence between the set of maximal tori (resp. the Cartan subgroups) of
$G$ and the set of maximal tori (resp. Cartan subgroups) of $H$. The Cartan subgroups of $G$ contain the center of $G$
and a fortiori `Ker v`, and are the groups of the form $v^{-1}(C')$, where $C'$ is a Cartan subgroup of $H$.*

<!-- label: III.XII.6.6 -->

Let us also state at once the following immediate consequence of c):

**Corollary 6.7.** *For $G$ to be nilpotent (i.e. the group $G(k)$ nilpotent) it is necessary and sufficient that the
tori in $G$ be central, or equivalently that $G$ have only a single maximal torus (and then this latter is the largest
subtorus of $G$).*

<!-- label: III.XII.6.7 -->

*Proof of 6.6.* Let $Z$ be a central algebraic subgroup of $G$, let $G' = G/Z$, and $u : G \to G'$ the canonical
homomorphism. Then $G'$ is a smooth and connected group. If $T'$ is a subtorus of $G'$, it follows from 6.4 that
$u^{-1}(T')$ is commutative and that $T'$ is the image of a subtorus of $u^{-1}(T')$, hence of a subtorus of $G$. Since
$u^{-1}(T')$ is commutative, it obviously admits a largest subtorus $T$ (since the sum of two subtori gives a third
containing both), and one therefore has $u(T) = T'$. From this it follows immediately that for every maximal torus $T$
of $G$, its image $T' = u(T)$ is a maximal torus of $G'$, and that $T \mapsto u(T)$ is a bijective correspondence
between maximal tori of $G$ and maximal tori of $G'$.

We now make

$$ Z = Centr(G)^{0}_{red}, $$

then $G'$ is affine by 6.1. Since the maximal tori of $G'$ are then conjugate, the same holds for those of $G$, which
proves a). <!-- original page 222 --> Moreover, for $G$ to be nilpotent, resp. have only a single maximal torus, it is
necessary and sufficient that $G'$ satisfy the same condition; now $G'$ being affine, the two conditions in question on
$G'$ are equivalent (*BIBLE* 6 th. 4 cor. 2), hence the same holds for the conditions in question on $G$. Moreover, if
$G$ has only a single maximal torus $T$, this latter is invariant hence central, and since every torus in $G$ is
contained in a maximal torus, it is central. Conversely, if every torus is central, the same holds for the maximal tori,
and by the conjugation theorem a) there is only a single maximal torus. This proves 6.7.

Let $T$ be any torus of $G$, $T' = u(T)$; then $C' = Centr_{G'}(T')$ is connected (*BIBLE* 6 th. 6 a)), hence by 6.3 the
centralizer $C$ of $T$ is equal to $u^{-1}(C')$, hence connected (since $Z$ is connected), which proves b). If $T$ is
maximal, hence $T'$ maximal, then we know that $C'$ is nilpotent, hence $C$ (which is a central extension of $C'$) is
nilpotent. Moreover, $T$ is a maximal torus of $C$, hence by 6.7 it is the unique maximal torus of $C$; consequently the
map $T \mapsto Centr_{G}(T)$ from the set of maximal tori of $G$ into the set of Cartan subgroups is bijective. Moreover
one has

```text
Centr_G(T) = C ⊂ Norm_G(C) ⊂ Norm_G(T)
```

and since we know that the centralizer of $T$ is of finite index in its normalizer (cf. XI, 5.9, whose reasoning is
valid without affine hypothesis, using only the representability of the two functors in question, as was signaled in
(XI, 6.5)), and that $C$ is smooth and connected, we conclude

$$ C = Norm_{G}(C)^{0}. $$

Moreover, by the bijective correspondence between maximal tori and Cartan subgroups, we see that $Norm_{G}(C)$ and
$Norm_{G}(T)$ have the same $k$-valued points, and since the latter is smooth, one has

$$ Norm_{G}(T) = Norm_{G}(C). $$

To complete the proof of c), it remains to prove that if $C$ is a smooth nilpotent connected subgroup
    <!-- original page 223 --> of $G$ of finite index in its normalizer, then $C$ is a Cartan subgroup. Now since $Z$ is
central, the normalizer of $C$ contains $Z$, and since $Z$ is smooth and connected, we conclude $Z \subset C$, whence
$C = u^{-1}(C')$, where $C' = u(C)$. One then has

$$ Norm_{G}(C) = u^{-1}(Norm_{G'}(C')), $$

which proves that $C'$ is nilpotent connected of finite index in its normalizer, hence <!-- original page 224 --> by
*BIBLE* 7 th. 1 it is a Cartan subgroup of $G'$, whence at once that $C$ is a Cartan subgroup of $G$.

Let us prove e): we are under the conditions of the start of the proof (setting $Ker u = Z$, $G' = H$); we have already
seen that $T \mapsto u(T)$ is a bijective correspondence between maximal tori of $G$ and maximal tori of $G'$. Taking
into account the bijective correspondence between maximal tori and Cartan subgroups just proved, we deduce a bijective
correspondence between Cartan subgroups $C$ of $G$ and Cartan subgroups $C'$ of $G'$, by making correspond to $C =
Centr_{G}(T)$ the group $C' = Centr_{G'}(T')$, where $T' = u(T)$. Since $C'$ is connected by b), it follows by 6.3 that
$C' = u(C)$, and $C = u^{-1}(C')$, which proves e).

It remains to prove d). Let $T$ be a maximal torus of $G$; we prove that $v(T)$ is a maximal torus of $H$ (which, taking
into account the conjugation theorem a), will imply that the maximal tori of $H$ are all of the form $v(T)$ as above).
Let then $R$ be a torus in $H$ containing $v(T)$; we prove $R = v(T)$. Replacing $H$ by $R$ and $G$ by
$v^{-1}(R)^{0}_{red}$, we may suppose $R = H$, i.e. that $H$ is a torus, and we are reduced to proving that then $v(T) =
H$. Let again $Z = Centr(G)^{0}_{red}$, $G' = G/Z$, and $H' = H/v(Z)$:

```text
e ⟶ Z ⟶ G ⟶^u G′ ⟶ e
       v″ ↓   v ↓   v′ ↓
e ⟶ v(Z) ⟶ H ⟶^{u′} H′ ⟶ e.
```

We already know that $u(T)$ is a maximal torus of $G'$, and since $G'$ is affine, so $v' : G' \to H'$ is an epimorphism
of affine smooth connected groups, $v'(u(T))$ is a maximal torus of $H'$ (*BIBLE* 7 th. 3 a)) hence equal to $H'$, i.e.
$u'(v(T)) = H'$; hence to prove $v(T) = H$ it suffices to show that $v(T) \supset v(Z)$. Now $v(Z)$ is a smooth
connected subgroup of $H$, hence a torus, and $v'' : Z \to v(Z)$ is an epimorphism, hence by 6.4 one has $v(Z) =
v''(S)$, where $S$ is a torus of $Z$. Now $S$, being central in $G$, is evidently contained in the maximal torus $T$,
whence $v(Z) \subset v(T)$. This proves assertion d) in the case of maximal tori.

Taking into account the bijective correspondence between maximal tori and Cartan subgroups, it remains to prove that if
$T$ is a maximal torus of $G$ and $C$ its centralizer, then $v(C)$ is the centralizer of $v(T)$. For this, take up again
the diagram (D) above (where of course $H$ is no longer supposed to be a torus), let $T' = u(T)$, $C' = u(C)$; we have
already seen in e) that $C'$ is the centralizer of the maximal torus $T'$, hence ($G'$ being affine, hence $H'$ being
affine) $v'(C')$ is the centralizer of the maximal torus $v'(T')$ of $H'$ (*BIBLE* 7 th. 3 a)), i.e. $u'(v(C))$ is the
centralizer of $u'(v(T))$; since $C$ contains $Z$, $v(C)$ contains $v(Z)$; $v(C)$ is therefore the inverse image by $u'$
of $u'(v(C))$, i.e. of the centralizer of $u'(v(T))$, hence is the centralizer of $v(T)$ as follows from e) applied to
$u' : H \to H'$ and to the maximal torus $v(T)$ of $H$. This completes the proof of 6.6.

## 7. Application to not-necessarily-affine smooth group preschemes

<!-- label: III.XII.7 -->

**Theorem 7.1.** *Let $S$ be a prescheme, $G$ an $S$-prescheme in groups smooth, separated and of finite type over $S$.
Suppose that $G$ admits, locally for the faithfully flat quasi-compact topology, a maximal torus. Then:*

*a) The map*

```text
T ⟼ Centr_G(T)
```

*induces a bijection from the set of maximal tori of $G$ onto the set of Cartan*

<!-- original page 225 -->

*subgroups of $G$. If $C$ corresponds to $T$, then $T$ is the unique maximal torus of $C$.*

*b) Let $T$, $T'$ be two maximal tori of $G$, $C$, $C'$ the corresponding Cartan subgroups; then one has*

```text
Transp_G(T, T′) = Transp_G(C, C′) = Transp_G(T, C′),
```

*the first two terms are also identical to the strict transporters; finally the functor in question is representable by
a closed subpreschema of $G$ smooth over $S$. The tori $T$, $T'$ and the Cartan subgroups $C$, $C'$ are conjugate
locally for the étale topology.*

*c) There exists, locally for the étale topology, a maximal torus of $G$ and a Cartan subgroup of $G$.*

*d) Suppose that every finite part of a fiber $G_{s}$ of $G$ is contained in an affine open of $G$ (for example $G$
quasi-projective over $S$, or $S$ artinian); then the functor $\mathcal{T} : (Sch)^{\circ}/S \to (Ens)$ defined in 1.10
(functor of maximal tori of $G$), isomorphic to the functor $\mathcal{C} : (Sch)^{\circ}/S \to (Ens)$ of Cartan
subgroups of $G$, is representable by a smooth, separated prescheme of finite type over $S$, which is quasi-projective
over $S$ when $G$ is, and is affine over $S$ when $G$ is affine over $S$, or when $S$ is artinian.*

*e) Let $u : G \to G'$ be a morphism of $S$-preschemata in groups, where $G'$ is smooth, separated of finite type over
$S$, and suppose that for every $s \in S$, one has $u_{s}(G_{s}) = G'_{s}$, i.e. $u_{s}$ is faithfully flat (Exp.
VI[^N.D.E-XII-8]). Then for every maximal torus $T$ of $G$, $u(T)$ is a maximal torus of $G'$; if $G'$ has connected
fibers, then for every Cartan subgroup $C$ of $G$, $u(C)$ is a Cartan subgroup of $G'$, and if $C$ is the centralizer of
$T$, $u(C)$ is the centralizer of $u(T)$. In either case, the induced morphism $T \to u(T)$, resp. $C \to u(C)$, is
faithfully flat.*

*f) Under the conditions of e), suppose moreover that `Ker u` is a central*

<!-- original page 226 -->

*subgroup of $G$. Then $T \mapsto u(T)$ is a bijective map from the set of maximal tori of $G$ onto the set of maximal
tori of $G'$, and if $G'$ has connected fibers, $C \mapsto u(C)$ is likewise a bijective map from the set of Cartan
subgroups of $G$ onto the set of Cartan subgroups of $G'$; if $C' = u(C)$, one has $C = u^{-1}(C')$.*

<!-- label: III.XII.7.1 -->

**Remarks 7.2.** *We shall see in XV that the conclusion of d) remains valid without the restrictive condition on the
finite parts of the $G_{s}$. We shall also prove there the conclusions concerning only the Cartan subgroups contained in
b), c), d), e), when one supposes only that $G$ admits, locally for the faithfully flat quasi-compact topology, a Cartan
subgroup (but not necessarily a maximal torus). For this we shall moreover need to use 7.1 in the case where $S$ is
artinian. Moreover, the proof of c) and d) (in the case $S$ not artinian) is considerably simplified by using the method
of XV.*

<!-- label: III.XII.7.2 -->

*Proof of 7.1.* a) Proceeding as in 3.2, one sees that for every maximal torus $T$ of $G$, $C = Centr_{G}(T)$ is indeed
a Cartan subgroup of $G$, and $T$ is determined in terms of $C$ as the unique maximal torus of $C$, so that it remains
only to show that every Cartan subgroup $C$ of $G$ is defined by a maximal torus of $G$, or equivalently that $C$ admits
a central maximal torus. The question being still local for the fpqc topology, we may suppose that $G$ admits a maximal
torus $T$. Then by (XI, 6.2), $Transp_{G}(T, C)$ is representable by a closed subpreschema $S'$ of $G$ smooth over $S$;
moreover $S' \to S$ is surjective, as follows from 6.6 c). Hence, replacing $S$ by $S'$, we may suppose that there
exists a section $g$ of $G$ such that $ad(g) \cdot T \subset C$; but then $ad(g) \cdot T$ is a maximal torus of $C$,
which is central fiber by fiber by 6.6 c), hence central by (IX, 5.6 b)). QED.

<!-- original page 227 -->

b) Let $T$, $T'$ be two maximal tori of $G$, and $C$, $C'$ the corresponding Cartan subgroups of $G$. Then the following
conditions are equivalent:

```text
(1) T ⊂ T′  (2) T = T′  (3) T ⊂ C′  (4) C ⊂ C′  (5) C = C′.
```

This follows trivially from a). Using the same result after arbitrary base change, one deduces the identity stated in b)
between various transporters and strict transporters. Moreover, we already noted in a) that $Transp_{G}(T, C')$ is
representable by a closed subpreschema of $G$, smooth over $S$, and that its structural morphism is surjective.
Consequently, by Hensel there exists locally for the étale topology a section of this prescheme over $S$, hence $T$ and
$T'$ on the one hand, $C$ and $C'$ on the other hand, are conjugate locally for the étale topology, which proves b).

c) Suppose first that $S$ is artinian, local. When $G$ admits a maximal torus $T$, then it follows from the conjugation
theorem proved in b) that the functor $\mathcal{T}$ of maximal tori of $G$ is representable by the homogeneous space
$G/N$, where $N$ is the normalizer of $T$ in $G$, which is smooth by b). Moreover, as we noted in (VI_A, 3.2.1), since
$\mathcal{T}$ is a homogeneous space under $G$, every finite part of $\mathcal{T}$ is contained in an affine open. In
the general case, there exists a finite extension $k'$ of the residue field $k$ of $S$ such that $G_{k'}$ has a maximal
torus; then $k'$ comes from $k$ by a finite flat base change $S' \to S$, and the maximal torus of $G_{k'}$ lifts to a
maximal torus of $G_{S'}$ (XI, 2.1 bis), so the functor $\mathcal{T}_{S'}$ is representable by a prescheme over $S'$,
smooth separated and of finite type over $S'$, every finite part of which is contained in an affine open. Hence the
natural descent datum on $\mathcal{T}_{S'}$ is effective, hence $\mathcal{T}$ is representable, and by descent one sees
that $\mathcal{T}$ is smooth over $S$, separated and of finite type over $S$. From smoothness it follows, thanks to
Hensel, that $\mathcal{T}$ admits a section locally for the <!-- original page 228 --> étale topology. This proves c)
and d) in the case $S$ artinian (N.B. we shall prove below that in this case, $\mathcal{T}$ is in fact affine over $S$).

Suppose now $S$ arbitrary. To prove c) and d), which are assertions local on $S$ for the Zariski topology, we may
suppose that there exists a prime $\ell$ prime to the residue characteristics of $S$, that $S$ is affine, and that the
reductive rank of the fibers of $G$ (which is evidently locally constant, thanks to the hypothesis of local existence
for fpqc of a maximal torus) is constant, say $r$. Let $S' \to S$ be a faithfully flat and quasi-compact morphism, $S'$
affine, such that $G_{S'}$ admits a maximal torus `T_0`. Let `C_0` be its centralizer; I claim that there exists a
suitable power $n$ of $\ell$ such that one has also $C = Centr_{G}({}_{n} T)$. Indeed, to see this, one is reduced at
once to the case $S'$ noetherian, where this was seen in (XI, 6.2). Fix $n$ thus, set

```text
M = (ℤ/nℤ)^r,   P = Hom_{S-gr}(M_S, G),
```

then $P$ is evidently representable as a closed subpreschema of finite presentation of $({}_{n} G)^{r}$, where

```text
_n G = Hom_{S-gr}((ℤ/nℤ)_S, G),
```

which is also the kernel of the $n$-th power morphism on $G$, hence representable by a closed subpreschema of finite
presentation of $G$. Moreover $P$ is smooth over $S$ by (XI, 2.1). Let $s \in S$; by what was seen above, there exists a
finite separable extension $k''$ of $\kappa(s)$ such that there exists a maximal torus $T''$ in $G_{k''}$; moreover,
since ${}_{n} T''$ is étale over $k''$ ($n$ being prime to the characteristic of $k''$) we may suppose (replacing $k''$
by a finite separable extension if necessary) that ${}_{n} T''$ is isomorphic to $M_{k''}$. Let $S'' \to S$ be an étale
morphism such that there exists $s'' \in S''$ above $s \in S$, giving rise to the residual extension
$\kappa(s'') \simeq k''$. One thus has a section of $P_{S''} \otimes \kappa(s'')$ over
$\operatorname{Spec}(\kappa(s''))$, hence by Hensel, replacing $(S'', s'')$ by $(S''', s''')$ étale over it if
necessary, we may suppose that there exists a section of $P_{S''}$ over $S''$, i.e. an element of $P(S'')$, extending
the given section. In other words, one has a homomorphism $M_{S''} \to G_{S''}$ which induces an isomorphism
$M_{\kappa(s'')} \simeq {}_{n} T''$. By (IX, 6.4) (which here reduces to a simple application of Nakayama's lemma) this
homomorphism is a closed immersion above an open neighborhood of $s'$, <!-- original page 229 --> which may be supposed
equal to $S''$. Let $H''$ be its image, and consider its centralizer $C''$ in $G_{S''}$, which is a closed smooth
subpreschema of $G$, by (XI, 6.2). Let us also note:

**Lemma 7.3.** *Under the preceding conditions for $\ell$, $n$, $r$, for every prescheme $S''$ over $S$ and every
maximal torus $T''$ of $G_{S''}$, one has*

$$ Centr_{G_{S''}}(T'') = Centr_{G_{S''}}({}_{n} T''). $$

<!-- label: III.XII.7.3 -->

Indeed, by faithfully flat descent from $S' \times_{S} S''$, one is reduced to the case where $G_{S''}$ admits a maximal
torus $T''_{1}$ for which the preceding relation is true. But since $T''$ is locally conjugate to $T''_{1}$ for the
étale topology by b), it follows that the same relation is true for $T''$.

Applying the foregoing result for $\operatorname{Spec}(\kappa(s''))$ instead of $S''$, one sees that the fiber
$C''_{s''}$ is a Cartan subgroup of $G$. Note now that $G$ being smooth over $S$, the union of the neutral components of
the fibers $G_{s}$ is an open of $G$ (by a general result of EGA IV on smooth morphisms[^N.D.E-XII-9]), evidently stable
under the group law of $G$; this is therefore a subgroup of $G$ for the prescheme structure induced by $G$. Moreover,
$G^{0}$ satisfies the preliminary hypotheses of $G$, and there is an evident bijective correspondence between the
maximal tori of $G$ and those of $G^{0}$. Hence to prove c) and d), we may suppose $G$ has connected fibers, which we
shall do. Then the Cartan subgroups of $G$ have connected fibers (6.6 a)). This being so, I claim that $C''^{0}$ is a
Cartan subgroup of $G_{S''}$ above an open neighborhood of <!-- original page 230 --> $s''$ in $S''$ (which will
complete the proof of c)). This follows indeed from the

**Lemma 7.4.** *Under the conditions of 7.1, suppose $G$ has connected fibers; let $C$ be a closed group subpreschema of
$G$, smooth over $S$, and $s$ an element of $S$ such that $C_{s}$ is a Cartan subgroup of $G_{s}$; then $C^{0}$ is a
Cartan subgroup of $G$ above an open neighborhood of $s$.*

<!-- label: III.XII.7.4 -->

One easily reduces to the case where $S$ is local and $s$ is its closed point, and to proving that then $C$ is a Cartan
subgroup of $G$; then by flat descent to the case where $G$ admits a maximal torus, say $T$. Then by (XI, 6.2),
$Transp_{G}(T, C)$ is representable by a closed subpreschema of $G$ smooth over $S$. Moreover, by the hypothesis on
$C_{s}$, the fiber of the transporter at $s$ is non-empty (taking into account the conjugation theorem 6.6 a)). This
reduces us by faithfully flat descent to the case where this transporter admits a section over $S$, hence to the case
where $C$ contains a maximal torus $T$ of $G$. But then $T$ is central in $C^{0}$ by (IX, 5.6 a)), hence $C^{0} \subset
Centr_{G}(T)$, and since this is an inclusion of smooth group schemes over $S$ having the same relative dimension
(namely, the dimension of their common fiber at $s$) and with connected fibers, it is an equality, which completes the
proof.

d) We keep the preceding notations and hypotheses for $\ell$, $n$, $r$, and the connectedness of the fibers of $G$. Let
$Q : (Sch)^{\circ}/S \to (Ens)$ be the functor defined by

```text
Q(S′) = the set of multiplicative-type subgroups of G_{S′} of type equal to (ℤ/nℤ)^r = M (IX, 1.4).
```

Then

```text
T ⟼ _n T
```

is a morphism

$$ \varphi : \mathcal{T} \longrightarrow Q, $$

which is a monomorphism by 7.3. I claim that $Q$ is representable by a separated prescheme of finite presentation over
$S$. Indeed, as we signaled in the proof of (XI, 3.12 a)), one has an isomorphism

$$ Q \simeq P_{0}/\Gamma $$

<!-- original page 231 -->

where `P_0` is the open and closed subpreschema of the prescheme $P = \operatorname{Hom}_{S-gr}(M_{S}, G)$ introduced in
c) corresponding to the monomorphisms $M_{S'} \to G_{S'}$ (cf. IX, 6.8), and where $\Gamma =
(\operatorname{Aut}_{gr}(M))_{S}$. The hypothesis that every finite part of a fiber $G_{s}$ is contained in an affine
open of $G$, being stable under passage to a closed subpreschema and under cartesian products, is evidently inherited by
$({}_{n} G)^{r}$ hence by $P$, hence by `P_0`, so that $Q$ is representable by a prescheme of finite presentation over
$S$ (cf. V).[^N.D.E-XII-10] One sees in the same way that if $G$ is quasi-projective (resp. affine) over $S$, the same
holds for $Q$. In any case, $Q$ is separated over $S$. Now one has the

**Lemma 7.5.** *The homomorphism $\varphi : \mathcal{T} \to Q$ above is representable by an open immersion.*

<!-- label: III.XII.7.5 -->

In other words, one must prove that if $H$ is a multiplicative-type subgroup of $G$, of type $M$, then there exists an
open part $U$ of $S$ such that for every $S'$ over $S$, $H_{S'}$ is of the form ${}_{n} T_{S'}$, for a suitable maximal
torus $T_{S'}$ of $G_{S'}$, if and only if $S' \to S$ factors through $U$. One may evidently suppose that the nilpotent
rank of the fibers of $G$ is constant (since by b), it is locally constant), say $r'$. Let $C = Centr_{G}(H)$, which is
a closed group subpreschema of $G$ smooth over $S$ (XI, 6.2). Then replacing $S$ by the open and closed part of the
points at which $C$ is of relative dimension $r'$, we may suppose $C$ of relative dimension $r'$ everywhere. One then
sees at once that $H$ is of the form ${}_{n} T$, for a maximal torus $T$ of $G$, if and only if $C^{0}$ admits a central
maximal torus $T$ of relative dimension $r$ everywhere and $H = {}_{n} T$, which gives another expression of the
subfunctor $U$ of $S$ we wish to represent (in replacing in the preceding criterion $S$ by an $S'$ over $S$). Moreover
by flat descent, we may suppose that $G$ admits a maximal torus `T_1`. Let $R$ be the subfunctor $Transp_{G}(T_{1},
Centr_{C^{0}}(C^{0}))$ of $Transp_{G}(T_{1}, C)$; the latter is representable by a smooth prescheme over $S$ by (XI,
6.2), and the former is representable by an induced open subpreschema, as follows at once from (IX, 5.6 a)); in
particular it is smooth over $S$. Consequently its structural morphism into $S$ is open, <!-- original page 232 -->
hence its image is open, and replacing $S$ by the said image (equipped with the induced structure) we may suppose the
structural morphism surjective. Then by 1.13 applied to $C^{0}$, $C^{0}$ admits a central maximal torus $T$ since it
admits one locally for fpqc, which will evidently be of relative dimension equal to that of `T_1`, i.e. $r$. Thus, the
condition to be expressed for $H$ is the equality $H = {}_{n} T$, which by (IX, 2.10) amounts again to taking a suitable
open (and closed) part of $S$.

Lemma 7.5 therefore implies that $\mathcal{T}$ is representable by a separated prescheme locally of finite presentation
over $S$, and even of finite presentation over $S$, as one sees by taking up again the proof of 7.5 to assure oneself
that $\varphi$ is in fact a quasi-compact open immersion, or by reducing by faithfully flat quasi-compact descent to the
case where $G$ admits a maximal torus, and where $\mathcal{T}$ is therefore isomorphic to $G/Norm_{G}(T)$. This last
expression, or at choice (XI, 2.1), show moreover that $\mathcal{T}$ is smooth over $S$. Finally, if $G$ is
quasi-projective over $S$, the same holds for $Q$ hence also for $\mathcal{T}$. If $G$ is affine over $S$, the assertion
that $\mathcal{T}$ is then affine over $S$ is recorded for memory, being established in 5.4 (N.B. I do not know whether
without the affine hypothesis on $G/S$, it is possible to choose $n$ in such a way that in 7.5 the open immersion is
also a closed immersion). For the assertion that $\mathcal{T}$ is affine over $S$ if $S$ is artinian, one is reduced to
the case where $S$ is the spectrum of a field ([EGA I, 6.1.7](https://jcreinhold.github.io/ega/i/01-06-finiteness-conditions.html#61-noetherian-and-locally-noetherian-preschemes)), which one may suppose algebraically closed. Then thanks to
f), which will be proved below, it suffices to prove the same assertion for $G/Centr(G)$; now this last is affine by
6.1, so that one is under the preceding conditions. This completes the proof of d).

e) By (IX, 6.8), we know that there exists a subtorus $T'$ of $G'$ such that $u$ induces a faithfully flat morphism $T
\to T'$ (which characterizes $T'$ as the subsheaf $u(T)$ of $G'$). Let $C$ be the centralizer of $T$, $C'$ that of $T'$;
we prove that the morphism <!-- original page 233 --> $C \to C'$ is flat, and faithfully flat if $G'$ has connected
fibers. Since $C$, $C'$ are flat of finite presentation over $S$, one is reduced to the case of a base field (SGA 1, I
5.9), which one may evidently suppose algebraically closed. Moreover one may suppose $G$, $G'$ connected (replacing them
by $G^{0}$ and $G'^{0}$ if necessary, which does not change $C^{0}$ and $C'^{0}$), and it then suffices to apply 6.6 d),
taking into account a).

f) Taking into account a) and e), one may restrict to proving the assertion concerning the Cartan subgroups. Now since a
Cartan subgroup of $G$ is the centralizer of a maximal torus, it contains the center of $G$ and a fortiori `Ker u`,
hence is of the form $u^{-1}(C')$, where $C' = u(C)$ is the Cartan subgroup of $G'$ envisaged in e). Hence the map $C
\mapsto u(C)$ is injective; to show that it is bijective, it suffices to see that for every Cartan subgroup $C'$ of
$G'$, $u^{-1}(C')$ is a Cartan subgroup of $G$. The question being local for fpqc, we may suppose that $G$ admits a
Cartan subgroup `C_1`, hence $u(C_{1}) = C'_{1}$ is a Cartan subgroup of $G'$, hence locally conjugate to $C'$ for fpqc
by b), and since $u^{-1}(C'_{1}) = C_{1}$ is a Cartan subgroup of $G$, it follows that $u^{-1}(C')$ is a Cartan subgroup
of $G$. QED.

One can also, to prove that $u^{-1}(C')$ is a Cartan subgroup, note that it is flat over $S$ since $u$ is (SGA 1, I
5.9), which reduces us by definition to the case of a base field, and one may apply 6.6 e).

**Corollary 7.6.** *Under the conditions of 7.1 e), $G'$ admits, locally for the étale topology, a maximal torus, hence
satisfies the preliminary conditions for $G$. If moreover `Ker u` is central, then the functors $\mathcal{T}_{G}$,
$\mathcal{C}_{G}$ of maximal tori of $G$ and Cartan subgroups of $G$ are isomorphic to the analogous functors
$\mathcal{T}_{G'}$, $\mathcal{C}_{G'}$ for $G'$ (hence, in the case where they are representable, they are represented
by isomorphic $S$-preschemata).*

<!-- label: III.XII.7.6 -->

**Remark 7.7.** *a) Contrary to what happens in the case where $G$ is affine over $S$ (it suffices, in fact, that $G$
have affine fibers, as one will see in XVI), it is not true* <!-- original page 234 --> *that the fact that $G$ has
locally constant reductive rank implies that $G$ admits, locally for fpqc, a maximal torus. For example, let $S$ be the
spectrum of a discrete valuation ring, `G_1` and `G_2` smooth separated group schemes of finite type over $S$ such that
the generic fiber of `G_1` is an elliptic curve, the special fiber a group $G_{m}$, and the generic fiber of `G_2` a
group $G_{m}$, the special fiber a group $G_{a}$, and take $G = G_{1} \times_{S} G_{2}$. Then the two fibers of $G$ have
reductive rank 1, but one sees at once that $G$ does not admit a maximal torus locally for fpqc. It is on the other hand
very plausible that the following condition (for a smooth separated group of finite type over a prescheme $S$) is
sufficient for the existence of a maximal torus locally for the étale topology: the reductive rank and the abelian rank
of the fibers of $G$ are locally constant functions.*

*b) In the proof of 7.1 (notably a)) we have invoked (XI, 6.2) in cases where $S$ is not supposed locally noetherian.
However, in the cases of application of (XI, 6.2) envisaged, the reduction to the case $S$ noetherian affine is
immediate.*

<!-- label: III.XII.7.7 -->

Here is a variant of 7.1 b):

**Proposition 7.8.** *Let $G$ be an $S$-prescheme in groups smooth of finite presentation with connected fibers, $H$ a
smooth $S$-prescheme in groups, $i : H \to G$ a monomorphism of $S$-groups (making $H$ an $S$-subgroup of $G$). Then for
every Cartan subgroup $C$[^XII-7-1] of $G$, $Transp_{G}(C, H)$ is representable by a closed subpreschema of $G$ smooth
over $S$.*

<!-- label: III.XII.7.8 -->

The fact that the transporter is representable by a closed subpreschema of $G$ of finite presentation is contained in
(XI, 6.11), taking into account that $C$ has connected fibers since $G$ does (6.6 b)). To show that the transporter is
smooth over $S$, one is reduced by the standard procedure to the case where $S$ is affine noetherian, then to the case
where $S$ is artinian local, and by descent to the case where the residue field of $S$ is algebraically closed. But then
    <!-- original page 235 --> $C$ admits a maximal torus $T$, which is a maximal torus of $G$. We may suppose that the
reductive rank and the nilpotent rank of the fiber `H_0` are equal to those of `G_0` (otherwise the transporter would be
empty), but then one sees at once (using the connectedness of $C$ and the fact that the centralizer in $H$ of a maximal
torus of $H$ is smooth) that one has

```text
Transp_G(C, H) = Transp_G(T, H)
```

and since we know that the second member is smooth (XI, 2.5), the same holds for the first. The preceding reasoning
shows more generally part b) of the

**Proposition 7.9.** *Let $G$ and $i : H \to G$ be as in 7.8, suppose moreover that for every $s \in S$, $H_{s}$ is
connected and has the same reductive rank and the same nilpotent rank as $G_{s}$ (i.e. $H_{s}$ contains a Cartan
subgroup of $G_{s}$). Then one has the following:*

*a) $Norm_{G}(H)$ is representable by a closed subpreschema $Norm_{G}(H)$ of $G$ of finite presentation over $S$, and
the canonical monomorphism $H \to Norm_{G}(H)$ is an open immersion; consequently $i$ is an immersion, and one has*

$$ H = Norm_{G}(H)^{0}. $$

*b) For every Cartan subgroup $C$ of $G$, $Transp_{G}(C, H)$ is a closed subpreschema of $G$, smooth over $S$, with
surjective structural morphism. If $C$ is the centralizer of a maximal torus $T$ of $G$, one has moreover*

```text
Transp_G(T, H) = Transp_G(C, H).
```

*c) Let $C$ be a group subpreschema of $H$. For it to be a Cartan subgroup of $H$, it is necessary and sufficient that
it be a Cartan subgroup of $G$.*

*d) Suppose that $G$ admits, locally for the étale topology, or for the fpqc topology,*

<!-- original page 236 -->

*a Cartan subgroup (resp. a maximal torus); then the same holds for $H$.*

<!-- label: III.XII.7.9 -->

*Proof.* a) The representability of $Norm_{G}(H)$ by a closed subpreschema $Norm_{G}(H)$ of $G$ of finite presentation
over $S$ is contained in (XI, 6.11). Since $H$ is smooth hence flat locally of finite presentation over $S$, to verify
that $H \to Norm_{G}(H)$ is an open immersion, one is reduced to verifying it on the fibers (VI_B, 2.6), which reduces
us to the case where $S$ is the spectrum of an algebraically closed field $k$. One is then reduced (Exp.
VI[^N.D.E-XII-11]) to verifying that the corresponding homomorphism on the Lie algebras is an isomorphism, or
equivalently that $(g/h)^{H} = 0$, where $g$ and $h$ are the Lie algebras of $G$ and of $H$, and the exponent $H$
denotes the invariants under $H$ (cf. II, 5.2.3 (i)). Now $H$ contains by hypothesis a Cartan subgroup $C$ of $G$, the
centralizer of the maximal torus $T$ of $G$, and it suffices therefore to prove that one has

$$ (g/h)^{T} = 0, $$

which follows, taking into account complete reducibility of the representations of $T$ (I, 4.7.3), from the analogous
relation $(g/c)^{T}$, where $c = Lie(C)$. As for this latter, equivalent to

$$ g^{T} = c, $$

it means that the centralizer $C$ and the normalizer $N$ of $T$ have the same Lie algebra, which follows from the fact
that $C$ is an open subgroup of $N$ (XI, 5.9). This completes the proof of a).

b) As we have signaled, the proof was given in 7.8.

c) Taking into account the fact that $H$ is a subpreschema of $G$, the assertion reduces trivially to the case where $S$
is the spectrum of an algebraically closed field, in which case it follows at once from the hypothesis made on $H$.

<!-- original page 237 -->

d) One uses b), c), and the "Hensel lemma" (XI, 1.10).

**Corollary 7.10.** *Let $G$ and $H$ be as in 7.9, and suppose that for every algebraically closed field $k$ over $S$,
every element of $G_{k}(k)$ which normalizes $H_{k}$ is in $H_{k}(k)$. Then $H$ is a closed subpreschema of $G$, and is
its own normalizer.*

<!-- label: III.XII.7.10 -->

This follows trivially from 7.9 a). We shall apply 7.10 in particular to the Borel subgroups (more generally, to the
parabolic subgroups) of $G$.

**Corollary 7.11.** *Let $G$, $H$ be as in 7.9. Then $H$ contains every group subpreschema $Z$ of $G$ which is central
in $G$, flat and of finite presentation over $S$.*

<!-- label: III.XII.7.11 -->

One may as usual reduce to the case $S$ affine noetherian, then to the case $S$ artinian, which implies that one is
under the conditions of 7.1. By 7.9 c) one may suppose that $H$ contains a Cartan subgroup $C$ of $G$, and one is
reduced to proving that $C \supset Z$. Now since $S$ is artinian, $G' = G/Z$ is representable by a prescheme in groups
of finite type over $S$, the canonical morphism $u : G \to G'$ being faithfully flat and its kernel being $Z$ (VI_A,
3.2). Obviously $G'$ is smooth over $S$, and one may apply 7.1 f), which implies that $C$ is of the form $u^{-1}(C')$,
hence contains $Z$.

**Corollary 7.12.** *Let $G$, $G'$ be two $S$-preschemata in groups smooth of finite presentation, $u : G \to G'$ a
faithfully flat group homomorphism (i.e. for every $s \in S$, $u_{s}$ is faithfully flat); suppose `Ker u` central and
$G$ with connected fibers. Then the map*

```text
H′ ⟼ H = u⁻¹(H′)
```

*establishes a bijective correspondence between group subpreschemata $H'$ of $G'$, smooth of finite presentation over
$S$, having the same reductive rank and the same*

<!-- original page 238 -->

*nilpotent rank as $G'$ at every $s \in S$, and the set of group subpreschemata $H$ of $G$, smooth of finite
presentation over $S$, having the same reductive rank and the same nilpotent rank as $G$ at every $s \in S$. For $H$ to
have connected fibers, it is necessary and sufficient that $H'$ do.*

<!-- label: III.XII.7.12 -->

Let $H$ be a group subpreschema of $G$ having the properties just specified. Then by 7.10, $H$ contains $Z = Ker u$,
hence by the theory of faithfully flat descent, is of the form $u^{-1}(H')$, where $H'$ is a well-determined group
subpreschema of $G'$, and one verifies at once, taking into account 6.6 e), that this latter has the properties stated
above. Moreover, if $H$ has connected fibers, the same evidently holds for $H' = H/Z$. It therefore remains to prove
that if one starts from a subgroup $H'$ of $G'$ having the stated properties, then $u^{-1}(H') = H$ has the same
properties in $G$; and that if $H'$ has connected fibers, the same holds for $H$. Taking into account 6.6 e), one is
reduced to proving that $H$ is smooth over $S$ (resp. and has connected fibers). Now $H$ is already flat over $S$ as the
inverse image of $H'$ which is, by the flat morphism $u$, hence one is reduced to verifying that the geometric fibers of
$H$ are smooth (resp. and connected) which reduces us to the case where $S$ is the spectrum of an algebraically closed
field. Then $H'$ contains a Cartan subgroup $C'$ of $G'$, hence $H$ contains the inverse image $C$ of $C'$, which is a
Cartan subgroup of $G$ by 6.6 e), hence $C$ is smooth and connected. Consequently 7.11 follows from the following lemma:

**Lemma 7.13.** *Let $G$, $G'$ be two preschemata in groups flat of finite presentation over $S$, $u : G \to G'$ a group
homomorphism which is faithfully flat, $C'$ a group subpreschema of $G'$ of finite presentation over $S$, such that $C =
u^{-1}(C')$ is smooth over $S$ (resp. has connected fibers). Then for every group subpreschema $H'$ of $G'$ of finite
presentation over $S$, containing $C'$, and such that $H'$ is smooth over $S$ (resp. has connected fibers), its inverse
image $H = u^{-1}(H')$ is smooth over $S$ (resp. has connected fibers).*

<!-- label: III.XII.7.13 -->

As we have remarked above, this statement reduces at once to the case where $S$ is the spectrum of a field. Note then
that $H$ is a principal bundle of base $H/C$, group $C$ (Exp. VI_B, 9); on the other hand $H/C \simeq H'/C'$ (cf. Exp.
IV), and $H'$ being smooth <!-- original page 239 --> (resp. connected) the same holds for $H'/C'$ hence for $H/C$.
Since the same holds for $C$ by hypothesis, it follows at once that the same holds for the bundle $H$. QED.

## 8. Semisimple elements; union and intersection of maximal tori in not-necessarily-affine group schemes

<!-- label: III.XII.8 -->

Throughout this number, $G$ denotes a smooth $S$-prescheme in groups of finite presentation over $S$, with connected
fibers.

<!-- original page 240 -->

Suppose first that $S$ is the spectrum of an algebraically closed field. When $G$ is affine, one has defined in *BIBLE*
4 N° 4 the notion of semisimple element of $G(k)$; one verifies at once that this notion is invariant under
algebraically closed extension $k'/k$ of the base field. Moreover, one has seen in *BIBLE* 6 th. 5 (c) that $g \in G(k)$
is semisimple if and only if it is contained in a maximal torus of $G$. When $G$ is no longer supposed affine, $G$ is
written canonically (thanks to Chevalley) as an extension of an abelian variety by a smooth and connected affine
algebraic group:

```text
(∗)    e ⟶ V ⟶ G ⟶ A ⟶ e.
```

We shall say that an element $g$ of $G(k)$ is *semisimple* if it is a semisimple element of $V(k)$. Since the maximal
tori of $V$ are obviously identical to the maximal tori of $G$, it amounts to the same to say that $g$ belongs to a
maximal torus of $G$. This is evidently still a notion invariant under algebraically closed extension $k'/k$ of the base
field $k$.

Suppose now that $S$ is the spectrum of an arbitrary field $k$, and let $g \in G$. Then (choosing an algebraically
closed extension $K$ of $\kappa(g)$) one sees that $g$ is the image of a geometric point $g'$ of $G$ with values in an
algebraically closed extension $K$ of $k$, and we shall say that $g$ is *semisimple* if $g'$ is semisimple, which is
independent of the particular choice of $g'$, thanks to what was said above. If $k'$ is an extension of $k$, then the
set of semisimple elements of $G_{k'}$ is the inverse image of the set $G^{ss}$ of semisimple elements of $G$.

Suppose finally $S$ arbitrary; then a point $g \in G$ is said to be *semisimple* if it is semisimple in its fiber
$G_{s}$. If $S' \to S$ is any morphism, then $G^{ss}_{S'}$ is the inverse image of $G^{ss}$. Suppose that the functor
$\mathcal{T}$ defined in 1.10 (functor of maximal tori) is representable by a prescheme of finite presentation over $S$
(which is the case for example if $G$ admits locally for fpqc a maximal torus, by 7.1 d), at least if $G$ is
quasi-projective over $S$). Consider the canonical maximal torus $T$ of $G_{\mathcal{T}}$ ("universal maximal torus of
$G$"), and the morphism

$$ u : T \longrightarrow G $$

induced by the projection $G_{\mathcal{T}} \to G$. Then it follows at once from the definition that $G^{ss}$ is none
other than the image of the preceding morphism. We shall conclude:

**Proposition 8.1.** *The set $G^{ss}$ of semisimple elements of $G$ is locally constructible (hence constructible if
$S$, hence $G$, is quasi-compact and quasi-separated).*

<!-- label: III.XII.8.1 -->

One reduces as usual to the case where $S$ is affine noetherian; moreover one may suppose (by the usual noetherian
criterion of constructibility ([EGA 0_III, 9.2.3](https://jcreinhold.github.io/ega/iii/02-ch0-09-constructible-sets.html#92-constructible-sets-in-noetherian-spaces))) that $S$ is integral, and restrict to proving that there exists a
nonempty open $U$ of $S$ such that $G^{ss}|U$ is constructible. Taking $U$ small enough, and replacing it if necessary
by a finite covering, one may suppose that $G$ is separated over $S$ and contains a maximal torus
    <!-- original page 241 --> $T$. But then by 7.1 d) the functor $\mathcal{T}$ is representable by a prescheme of finite
presentation over $S$, and the same therefore holds for $T$, whose image in $G$ is consequently constructible. QED.

Suppose again that $k$ is a field, and consider the subgroup $H$ of $G$ generated by the preceding morphism (cf. VI_B,
1.2). It is a smooth group subscheme of $G$, connected since $T$ is, whose formation is evidently compatible with any
base field extension (cf. VI), that of $T$ being so. When $k$ is algebraically closed, one sees at once that $H$ is also
the algebraic subgroup of $G$ generated by the maximal tori of $G$, or equivalently by the tori of $G$, and it is also
the smallest algebraic subgroup of $G$ that contains the semisimple elements of $G(k)$. (In fact, these
characterizations of $H$ remain valid as soon as $k$ is an infinite field, thanks to the fact, proved in XIV, that the
set of points of $T$ rational over $k$ is dense in $T$). Moreover, $H$ is invariant in $G$, for to see this, one may
restrict to the case where $k$ is algebraically closed, and then ($H$ and $G$ being smooth over $k$) it suffices to
verify that $H$ is stable under the inner automorphisms $int(g)$, $g \in G(k)$, which is evident. (One could even show
that $H$ is a characteristic subgroup of $G$, i.e. stable under $\operatorname{Aut}_{k-gr}(G)$.) It then follows at once
from 6.6 d) that the reductive rank of $G/H$ is zero; more precisely, if $K$ is an invariant algebraic subgroup of $G$,
it follows at once from the fact that for $k$ algebraically closed, the maximal tori of $G/K$ are the direct images of
the maximal tori of $G$, that the reductive rank of $G/K$ is zero if and only if $K$ contains all the maximal tori of
$G$ ($k$ being supposed algebraically closed), or equivalently if and only if $K$ contains $H$ ($k$ arbitrary): hence
$H$ is the smallest invariant algebraic subgroup of $G$ such that $G/H$ is of zero reductive rank. Another evident
characterization of $H$ is the following: it is the smallest algebraic subgroup of $G$ having the same reductive rank as
$G$. Let us note finally that $H$ is affine: indeed, to see this one may again suppose $k$ algebraically closed, and
taking up the exact sequence (∗) at the beginning of the N°, one notes that the maximal tori of $G$ are contained in
$V$, hence the same holds for $H$, hence $V$ <!-- original page 242 --> being affine, $H$ is. Let us summarize the
results obtained:

**Proposition 8.2.** *Let $G$ be a smooth and connected algebraic group over the field $k$, and let $\bar{k}$ be an
algebraic closure of $k$. There exists an algebraic subgroup $H$ of $G$ such that $H_{\bar{k}}$ is the algebraic
subgroup of $G_{\bar{k}}$ generated by the maximal tori (or equivalently the tori) of $G_{\bar{k}}$. The group $H$ is
also characterized as the smallest algebraic subgroup of $G$ having the same reductive rank as $G$, or the smallest
invariant algebraic subgroup of $G$ such that the reductive rank of $G/H$ is zero. It is a smooth connected invariant
and affine subgroup of $G$, whose formation commutes with any extension of the base field.*

<!-- label: III.XII.8.2 -->

In order to use the characterization of $H$ in terms of $G/H$, it is appropriate to make explicit the

**Corollary 8.3.** *Let $G$ be a smooth and connected algebraic group over an algebraically closed field $k$. For $G$ to
be of zero reductive rank (i.e. with the notations of 8.2, for one to have $H = (e)$) it is necessary and sufficient
that $G$ be an extension of an abelian variety by a smooth connected unipotent algebraic group (i.e. successive
extension of groups isomorphic to the additive group $G_{a}$).*

<!-- label: III.XII.8.3 -->

Indeed, thanks to Chevalley's exact sequence (∗), one is reduced to proving that the reductive rank of the smooth
connected affine group $V$ is zero if and only if $V$ is <!-- original page 158 --> unipotent, which is contained in
*BIBLE* 6.4 th. 4 cor. 3. Hence with the notations of 8.2, $H$ is the smallest invariant algebraic subgroup of $G$ such
that $(G/H)_{\bar{k}}$ is an extension of an abelian variety by a smooth connected affine unipotent algebraic group. One
concludes also:

**Corollary 8.4.** *With the notations of 8.2, for one to have $G = H$ (i.e. $G_{\bar{k}}$ generated by its maximal
tori) it is necessary and sufficient that $G$ be affine and that every homomorphism from $G_{\bar{k}}$ to the additive
group be trivial.*

<!-- label: III.XII.8.4 -->

<!-- original page 243 -->

**Remarks 8.5.** *a) Let $V$ be the largest smooth connected affine algebraic subgroup of $G_{\bar{k}}$ (so that
$G_{\bar{k}}$ is an extension of an abelian variety by $V$). It is well known (Rosenlicht[^N.D.E-XII-12]), if $k$ is not
perfect, that $V$ is in general not "defined over $k$", i.e. that there does not in general exist an algebraic subgroup
$V$ of $G$ such that $V_{\bar{k}} = V$. However, when $V$ is generated by its maximal tori, i.e. when $V$ admits no
quotient group isomorphic to the additive group $G_{a,\bar{k}}$, there exists such a $V$, namely the group $H$ of 8.2.
One thus sees that in this question of rationality, as in many others (cf. for example XIV, N° 6), all the troubles come
from the unipotent groups, i.e. from the additive group, while it is the presence of (enough) multiplicative-type groups
that on the contrary ensures that things go well.*

*b) One may also introduce, with the notations of 8.2, the inverse image $H'$ in $G$ of the commutator subgroup of
$G/H$; then $H'$ is the smallest invariant algebraic subgroup of $G$ such that $(G/H')_{\bar{k}}$ is a commutative
extension of an abelian variety by a smooth connected affine unipotent algebraic group. $H'$ is again a smooth connected
affine subgroup of $G$. Let $H''$ be the inverse image in $G$ of $p^{n}(G/H')$ for $n$ large, $p$ being the
characteristic (assumed `> 0`); then one sees easily that $H''/H'$ is an abelian variety, and $H''$ is the smallest
invariant algebraic subgroup of $G$ such that $G/H''$ is a commutative smooth connected affine unipotent algebraic
group. This being so, one sees easily that for $V = H_{\bar{k}}$ (notations of a)), i.e. for every homomorphism from $V$
to the additive group to be trivial, it is necessary and sufficient that $H'' = G$, or equivalently that every
homomorphism from $G_{\bar{k}}$ to the additive group be trivial.*

<!-- label: III.XII.8.5 -->

To finish, we shall generalize to smooth groups with connected fibers the notion of reductive center developed in N° 4,
inspired by 4.10. Let $\mathcal{Z}$ be the subfunctor of $G$ defined by

*$\mathcal{Z}(S') =$ Set of sections $g'$ of $G_{S'}$ over $S'$ such that for every $S''$ over*

<!-- original page 244 -->

*$S'$ and every maximal torus $T''$ of $G_{S''}$, the inverse image $g''$ of $g'$ by $S'' \to S'$ is a section of $T''$
over $S''$.*

Introducing the functors $\mathcal{T}(S') =$ set of maximal tori of $G_{S'}$, and $T(S') =$ set of pairs $(T', g')$,
where $T'$ is a maximal torus of $G_{S'}$ and $g'$ a section of $T'$ over $S'$, one sees that $T$ is a subfunctor of
$\mathcal{T} \times_{S} G = \mathcal{T}_{G}$, and with these notations, one may also write

$$ \mathcal{Z} = \prod_{\mathcal{T}_{G}/G} T/\mathcal{T}_{G}. $$

Using (XI, 6.8) and 7.1 d) which ensures the representability of $\mathcal{T}$ by a smooth $S$-prescheme under certain
conditions, one could conclude the representability of $\mathcal{Z}$ under certain conditions, which we shall however
obtain by a more direct route below.

**Definition 8.6.** *Let $G$ be a smooth $S$-prescheme in groups of finite presentation with connected fibers. One says
that $G$ admits a* reductive center *if the preceding functor $\mathcal{Z}$ (which is evidently a subgroup of $G$) is
representable by a multiplicative-type group. One then says that $\mathcal{Z}$ is the* reductive center of $G$.

<!-- label: III.XII.8.6 -->

One will note that if $Z$ is a reductive center of $G$, then for every base change $S' \to S$, $Z_{S'}$ is a reductive
center of $G_{S'}$; on the other hand, the existence of a reductive center is evidently a local question for the fpqc
topology. As for the terminology "reductive center", note that $Z$ is in any case central, since evidently $\mathcal{Z}$
is invariant under

$$ \operatorname{Aut}_{S}(G) $$

and *a fortiori* it is an invariant subgroup of $G$, and one applies (IX, 5.5).

Lemma 4.5 must be replaced here by:

**Lemma 8.7.** *Let $u : H \to G$ be a central homomorphism, where $H$ is of multiplicative*

<!-- original page 245 -->

*type and of finite type over $S$; suppose that for every algebraically closed field $k$ over $S$, $u_{k}(H_{k})$ is
contained in the largest affine smooth connected subgroup of $G_{k}$. Then $u$ factors through every maximal torus $T$
of $G$ (hence $u$ factors in fact through the subfunctor $\mathcal{Z}$ of $G$ defined above).*

<!-- label: III.XII.8.7 -->

Using an easy variant of (IX, 5.1 bis) (where the sign `=` would be replaced by an inclusion sign), one is reduced to
the case where $S$ is the spectrum of a field $k$, which one may suppose algebraically closed. (Reduce to the case $S$
affine noetherian, then artinian, then use (IX, 3.6).) Since $T$ is contained in the largest affine smooth connected
subgroup $V$ of $G$, one is then reduced to the case where $G = V$, i.e. where $G$ is affine, where the result was
proved in 4.5.

**Proposition 8.8.** *Let $G$ be a smooth $S$-prescheme in groups of finite presentation with connected fibers.*

*a) If $S$ is the spectrum of a field $k$, then $G$ admits a reductive center $Z$. When $G$ is an extension of an
abelian variety by a smooth connected affine algebraic group $V$ (for example if $k$ is algebraically closed), then $Z$
is also the reductive center of $V$, and is the largest central multiplicative-type subgroup of $V$.*

*b) Let $Z$ be a multiplicative-type group subpreschema of $G$. Then $Z$ is a reductive center of $G$ if and only if for
every $s \in S$, $Z_{s}$ is a reductive center of $G_{s}$. Then $Z$ is the largest multiplicative-type subgroup $K$ of
$G$ such that for every $s \in S$, $K_{s}$ is contained in the reductive center of $G_{s}$; more generally, for every
homomorphism $u : H \to G$, with $H$ of multiplicative type and of finite type over $S$, such that for every
algebraically closed field $k$ over $S$, $u_{k} : H_{k} \to G_{k}$ factors through the largest smooth connected affine
subgroup of $G_{k}$, $u$ factors through $Z$ (and in particular, $u$ is central).*

<!-- original page 246 -->

*c) If $G$ admits, locally for the fpqc topology, a maximal torus, then $G$ admits a reductive center.*

*d) Let $T$ be a maximal torus of $G$. Then $T \cap Centr(G) = Ker(T \to GL(g))$ and this is a reductive center of $G$.*

*e) Let $Z$ be a reductive center of $G$, and suppose $G' = G/Z$ representable (for example $S$ artinian); then $G'$
admits the unit subgroup as reductive center, and $T' \mapsto T = u^{-1}(T')$ establishes a bijective correspondence
between maximal tori of $G'$ and maximal tori of $G$.*

<!-- label: III.XII.8.8 -->

*Proof.* a) Suppose that $S$ is the spectrum of a field $k$. To prove the existence of a reductive center, one may
suppose $k$ algebraically closed, and one is reduced consequently to the case where $G$ is an extension of an abelian
variety by a smooth connected affine algebraic group $V$. Since for every $S'$ over $k$, the maximal tori of $G_{S'}$
are those of $V_{S'}$ (by (IX, 5.2) and the fact that over an algebraically closed field, a homomorphism from a torus to
an abelian variety is trivial), it follows that the functor $\mathcal{Z}$ defined above in terms of $G$ is the same as
the one defined in terms of $V$. One is thus reduced to the case $G$ affine. Since $\mathcal{T}$ is representable and
necessarily "essentially free" over $k$ (VIII, 6.1), it follows that $\mathcal{T}_{G}$ is essentially free over $G$, and
since $T$ is a closed subscheme of $\mathcal{T}_{G} = G_{\mathcal{T}}$ (by e.g. (VIII, 5.7)) it follows by (VIII, 6.4)
that $\mathcal{Z} = \prod_{\mathcal{T}_{G}/G} T/\mathcal{T}_{G}$ is representable by a closed subscheme of $G$. It is
therefore a group subscheme of $G$; I claim that it is of multiplicative type: indeed one may suppose $k$ algebraically
closed; then $G$ admits a maximal torus $T$, and by definition one will have $Z \subset T$, hence $Z$ is of
multiplicative type as an algebraic subgroup of a multiplicative-type group (IX, 8). This proves that $Z$ is a reductive
center of $G$. The fact that it is the largest central multiplicative-type subgroup of $V$ is contained in 8.7.

b) The "only if" being trivial, let us prove that if $Z$ is a multiplicative-type subgroup of $G$ such that for every $s
\in S$, $Z_{s}$ is the reductive center of $G_{s}$, <!-- original page 247 --> then $Z$ is a reductive center of $G$.
One must first prove that $Z$ is contained in every maximal torus of $G$ (which will thus remain true after every base
change): this is an immediate consequence of 8.7. Next, one must prove that if $g$ is a section of $G$ over $S$ such
that for every $S'$ over $S$ and every maximal torus $T'$ of $G_{S'}$, $g_{S'}$ is a section of $T'$, then $g$ is a
section of $Z$. Note that one could reduce as usual (taking into account that $\prod_{\mathcal{T}_{G}/G}
T/\mathcal{T}_{G} = \mathcal{Z}_{0}$ is an fpqc sheaf that commutes with inductive limits of rings) to the case $S$
affine, then $S$ noetherian, and finally $S$ artinian. Then $\mathcal{T}$ is representable by a smooth prescheme over
$S$ by 7.1 d), so proceeding as in a), one sees that $\prod_{\mathcal{T}_{G}/G} T/\mathcal{T}_{G}$ is representable by a
closed subscheme `Z_0` of $G$. We have already seen that $Z \subset Z_{0}$; on the other hand by hypothesis on $Z$ one
has `Z_k = Z_0_k` (where $k$ is the residue field); now $Z$ being flat over $S$, it follows $Z = Z_{0}$, which proves
that $Z$ is a reductive center of $G$. The other assertions of b) are contained in 8.7.

c) Reduces immediately to d).

d) Of course, $g$ denotes the Lie algebra of $G$, and $T \to GL(g)$ the homomorphism induced by the adjoint
representation of $G$. One has trivially

```text
T ∩ Centr_G ⊂ Ker(T → GL(g)),
```

the proof of the reverse inclusion is the same as in 4.7 d), we do not repeat it here. Let $Z$ be the group in question;
as $Ker(T \to GL(g))$ it is of multiplicative type (cf. for example (IX, 6.8)). To prove that it is a reductive center
of $G$, one is reduced by b) to the case where $S$ is the spectrum of a field. Let then `Z_0` be the reductive center
(which exists by a)); one has evidently $Z_{0} \subset T \cap Centr(G) = Z$; on the other hand since $Z$ is a central
multiplicative-type subgroup contained in the smooth connected affine subgroup $T$, it follows from a) that $Z_{0}
\supset Z$, hence $Z_{0} = Z$. QED.

e) Under the conditions of 7.1 f) set $Z = Ker u$ and suppose that for every algebraically closed field $k$ over $S$,
$Z_{k}$ is contained in a maximal torus of $G_{k}$. Then one verifies easily that the map $T' \mapsto u^{-1}(T')$
induces a bijective <!-- original page 248 --> correspondence between the set of maximal tori of $G'$ and the set of
maximal tori of $G$. Applying this to the situation 8.8 e), the desired conclusion follows at once.

**Remarks 8.9.** *a) The proof given of 8.8 is independent of the results of N° 4, and in particular that of 8.8 a) does
not use 4.4 (whose proof is a little burdensome).*

*b) One sees easily that the subgroup $\mathcal{Z}$ of $G$ envisaged in 8.6 is always central (whether it is
representable or not), and it may be tempting to call it the reductive center of $G$ in all cases.*

*c) One may also generalize 4.9; one finds the following statement: Let $G$ be a smooth and connected algebraic group
over an algebraically closed field. For $G$ to be an extension of an abelian variety by a smooth connected unipotent
algebraic group (i.e. for the reductive rank of $G$ to be zero, cf. 8.3) it is necessary and sufficient that the
reductive center of $G$ be reduced to the unit group and that the Lie algebra of $G$ be nilpotent.*

<!-- label: III.XII.8.9 -->

## 9. Complement: action of a group scheme and fixed points

<!-- label: III.XII.9 -->

The aim of this section, added in January 2008, is to study fixed points under the action of a group scheme.

### 9.1. Representability of the functor of fixed points

<!-- label: III.XII.9.1 -->

Let $S$ be a scheme, $G$ an $S$-group scheme acting on an $S$-scheme $X$. One defines the subfunctor $X^{G}$ of $X$ of
fixed points of $X$ under $G$: for every $S$-scheme $T$, $X^{G}(T)$ is the subset of $X(T)$ consisting of fixed points
under $G$ (VIII, 6.e).

Recall the notion of "$S$-pure scheme" introduced in ([G-R], § 3.3, [R]). Let $G$ be a flat $S$-group scheme of finite
presentation. Since the fibers of $G$ have no embedded components, the notion of purity for $G$ takes the following
form. The scheme $G$ is *$S$-pure* if for every strictly henselian local $S$-scheme $T$ with closed point $t$, every
generic point $\tilde{x}$ of a fiber of $G \times_{S} T$ specializes to a point of $G_{t}$, i.e. the closure of
$\tilde{x}$ in $G \times_{S} T$ meets $G_{t}$.

<!-- original page 162 -->

*Examples.* (1) If $G$ is quasi-finite and separated over $S$, $G$ is $S$-pure if and only if $G$ is finite over $S$.

(2) If $S = \operatorname{Spec}(R)$ and $G = \operatorname{Spec}(A)$, $G$ is $S$-pure if and only if $A$ is a projective
$R$-module ([G-R], 3.3.5). In particular $G$ is $S$-pure if $G$ is diagonalizable.

(3) A multiplicative-type group scheme is $S$-pure since the notion of purity is local for the étale topology on $S$.

(4) The scheme $G$ is $S$-pure if $G$ is $S$-proper or if the fibers of $G$ are irreducible or if $S$ is semi-local
artinian.

(5) In particular, an $S$-reductive group scheme $G$ is $S$-pure.

**Proposition 9.2.** *Let $G$ be an $S$-group scheme of finite presentation, $S$-flat and $S$-pure, acting on an
$S$-scheme $X$ of finite presentation. Then the functor $X^{G}$ of fixed points of $X$ under $G$ is representable by a
closed subscheme of $X$, of finite presentation over $S$.*

<!-- label: III.XII.9.2 -->

Indeed, let $a$ in $X(S)$ and let $H$ be the group subscheme of $G$ fixing $a$. Then $a$ is fixed under $G$ if and only
if $H = G$. Now the subfunctor $C$ of $S$ of coincidences (precisely, if $T$ is an $S$-scheme, $C(T) = {\emptyset}$ if
$H \times_{S} T \to G \times_{S} T$ is bijective, and $C(T) = \emptyset$ otherwise) of $H$ with $G$ is representable by
a closed subscheme of $S$, defined by a finitely generated sheaf of ideals ([G-R], 4.1.1). One applies this result with
$S = X$ taking for $a$ the universal point of $X$ (i.e. the identity in $X(X) = \operatorname{Hom}_{S}(X, X)$).

### 9.3. Infinitesimal obstruction

<!-- label: III.XII.9.3 -->

Under the hypothesis that $G$ is a flat $S$-group scheme of finite presentation acting (on the left) on a smooth
$S$-prescheme $X$, we shall now study the formal smoothness of the functor $X^{G}$.

One supposes here that $S$ is equipped with a closed subscheme `S_0` defined by a sheaf of quasi-coherent ideals
$\mathcal{I}$ of square zero. One writes $j : S_{0} \to S$, $G_{0} = G \times_{S} S_{0}$, $X_{0} = X \times_{S} S_{0}$.

Let $\epsilon_{0}$ be a point of $X^{G}(S_{0})$ that lifts to a point of $X(S)$. We shall study the obstruction to
lifting $\epsilon_{0}$ to a point of $X^{G}(S)$. Since $X$ is smooth, one knows that the liftings of $\epsilon_{0}$ to
$X(S)$ form a principal homogeneous space, trivial for the abelian group

$$ \operatorname{Hom}_{O_{S_{0}}}(\epsilon^{*}_{0}(\Omega^{1}_{X_{0}/S_{0}}), \mathcal{I}) $$

(III, 0.2, 0.3). One sets

$$ L_{0} = \operatorname{Hom}_{O_{S_{0}}}(\epsilon^{*}_{0}(\Omega^{1}_{X_{0}/S_{0}}), \mathcal{I}), $$

this is an $O_{S_{0}}$-module. Moreover, given that $\epsilon_{0}$ is fixed under $G$, `L_0` is naturally a
`G_0`-$O_{S_{0}}$-module. One writes $\rho_{0} : G_{0} \to \operatorname{Aut}_{S_{0}}(L_{0})$ (resp. $\rho : G \to
\operatorname{Aut}_{S}(j_{*}L_{0})$) for the associated representation.

**Lemma 9.4.** *There exists a certain class $c(\epsilon_{0}) \in H^{1}(G, j_{*}L_{0}) \simeq H^{1}(G_{0}, L_{0})$,
defined canonically by $\epsilon_{0}$, such that $\epsilon_{0}$ lifts to $X^{G}(S)$ if and only if $c(\epsilon_{0}) =
0$.*

<!-- label: III.XII.9.4 -->

<!-- original page 163 -->

The adjunction $H^{1}(G, j_{*}L_{0}) \simeq H^{1}(G_{0}, L_{0})$ is that of lemma (III, 1.1.2). We work with the small
fppf site on $S$. For every flat scheme $T$ of finite presentation over $S$, one writes $G_{T} = G \times_{S} T$, $X_{T}
= X \times_{S} T$ for the corresponding objects over $T$. Consider the sheaf $\mathcal{A}$ on the small fppf site of $S$
such that, for every $T$ flat and of finite presentation over $S$, one has:

```text
𝒜(T) = {set of liftings of ε_0 ×_S T in X(T)}.
```

Given that the formation of `L_0` commutes with flat base changes, the foregoing considerations indicate that
$\mathcal{A}(T)$ is a trivial principal homogeneous space under the abelian group $H^{0}(T, j_{*}L_{0})$. Again from the
fact that $\epsilon_{0}$ is fixed, for every $T$ flat and of finite presentation over $S$, and every $g$ in $G(T)$, $g$
acts by affine automorphisms on $\mathcal{A}(T)$, compatibly with the action of $G$ on $j_{*}L_{0}$. That is to say:

```text
g(a_T + v) = g(a_T) + ρ(g)(v),   v ∈ H¹(T, j_*L_0).
```

Since $G$ is flat of finite type one may apply these considerations taking $T = G$ and for $g$ the universal point
$id_{G}$ of $G$. One thus obtains an action of the fppf sheaf $G$ on $\mathcal{A}$.

Let $a$ be a lifting of $\epsilon_{0}$ in $X(S)$. One writes $g^{\sharp}$ for the universal point of $G$, and one
defines $v^{\sharp} \in H^{0}(G, j_{*}L_{0})$ by

```text
ρ(g^♯)(v^♯) = g^♯ . a_G − a_G.
```

For every $S$-prescheme $Y$, one sets $z(Y) : G(Y) \to H^{0}(Y, j_{*}L_{0})$, $g \mapsto v^{\sharp}(g)$. This defines
the 1-cocycle $z$ in $Z^{1}(G, L)$ (Exposé I, § 5).

Its class $c(\epsilon_{0})$ in $H^{1}(G, j_{*}L_{0})$ does not depend on the choice of $a$. In particular, if
$\epsilon_{0}$ lifts to $X^{G}(S)$, one has $c(\epsilon_{0}) = 0$. Conversely, if $c(\epsilon_{0}) = 0$, then there
exists $w \in H^{0}(S, j_{*}L_{0})$ such that $z(Y)(g) = g.w_{Y} - w_{Y}$ for every $S$-prescheme $Y$ and every $g \in
G(Y)$. Applying this to $Y = G$ and to $g^{\sharp}$, one concludes that $a - w \in X^{G}(S)$. We have thus established
that $\epsilon_{0}$ lifts in $X^{G}(S)$ if and only if $c(\epsilon_{0}) = 0$.

**Remark 9.5.** *In the case where $G$ is affine and flat of finite type over $S$ affine, one can refine this
obstruction into a class $\tilde{c}(\epsilon_{0}) \in H^{1}_{G_{0}}(X_{0}, L_{0})$ where $H^{1}_{G_{0}}(X_{0}, L_{0})$
is the `G_0`-equivariant cohomology group defined by Wevers ([W], app. C). In this case, it is not necessary to suppose
that $\epsilon_{0}$ lifts to $X(S)$.*

<!-- label: III.XII.9.5 -->

### 9.6. Smoothness of fixed points

<!-- label: III.XII.9.6 -->

**Theorem 9.7.** *Let $G$ be an $S$-group scheme flat, of finite type over a noetherian base $S$, acting on a smooth
$S$-scheme $X$. Suppose that $G$ is $S$-pure, and for every geometric point $s$ above $S$ (with algebraically closed
residue field), one has*

$$ H^{1}(G_{s}, (\Omega^{1}_{X_{s}})*) = 0. $$

*Then the functor $X^{G}$ of fixed points of $X$ under $G$ is representable by a closed subscheme of $X$ smooth over
$S$.*

<!-- label: III.XII.9.7 -->

Let us prove Theorem 9.7. We know that $X^{G}$ is representable by a closed subscheme of $X$ of finite presentation over
$S$. We may suppose $S = \operatorname{Spec}(A)$ local. Following the smoothness criterion (SGA 1, III, 3.1.iii bis), it
suffices to verify the formal smoothness of $X^{G}$ <!-- original page 164 --> for $S' = \operatorname{Spec}(A')$ and
the closed subscheme $S''_{0} = \operatorname{Spec}(A'/I') = \operatorname{Spec}(A''_{0})$, where $A'$ is an artinian
local ring and $I'$ an ideal of square zero of $A'$. By dévissage, one reduces to the case where $I'$ is annihilated by
the maximal ideal of $A'$. In particular, if $k$ denotes the residue field of $A'$, $I'$ is a $k$-vector space.

One is therefore given an element $\epsilon''_{0} \in X^{G}(S''_{0})$ which one wishes to lift to $X^{G}(S')$. One then
writes $X_{0} = X \times_{S} S'$, $G' = G \times_{S} S'$, $X''_{0} = X \times_{S} S''_{0}$, $G''_{0} = G \times_{S}
S''_{0}$. Given that $S'$ is affine and that `X_0` is smooth over $S'$, $\epsilon''_{0} \in X^{G}(S''_{0})$ lifts to
$X(S')$. By Lemma 9.4, the class

$$ c(\epsilon_{0}) \in H^{1}(G''_{0}, L''_{0}) $$

is the obstruction to lifting $\epsilon''_{0}$ in $X^{G}(S')$, where $L''_{0} =
\operatorname{Hom}_{O_{S''_{0}}}(\epsilon''_{0}*(\Omega^{1}_{X''_{0}/S''_{0}}), I')$. Given that $L''_{0}$ is a
$k$-vector space, one has a canonical isomorphism $H^{1}(G''_{0}, L''_{0}) \simeq H^{1}(G''_{0} \times_{A''_{0}} k,
L''_{0})$. It suffices to show that $H^{1}(G''_{0} \times_{A''_{0}} k, L''_{0}) = 0$. Writing $\bar{k}$ for an algebraic
closure of $k$, one has an isomorphism (IX, 3.1 in the affine case, lemma 9.11 in general)

```text
H¹(G″_0 ×_{A″_0} k, L″_0) ⊗_k k̄ ≃ H¹(G″_0 ×_{A″_0} k̄, L″_0 ⊗_k k̄).
```

One then remarks that the representation $L''_{0} \otimes_{k} \bar{k}$ is a direct sum of $(\Omega^{1}_{X_{0} \times_{k}
\bar{k}})*$. By hypothesis one has $H^{1}(G''_{0} \times_{k} A''_{0}, (\Omega^{1}_{X_{0} \times_{k} \bar{k}})*) = 0$,
which implies $H^{1}(G''_{0} \times_{A''_{0}} k, L''_{0}) = 0$.

**Corollary 9.8.** *Let $G$ be a flat $S$-group scheme of finite presentation acting on a smooth $S$-scheme $X$ of
finite presentation. Suppose that $G$ admits a composition series whose factors are of one of the following types:*

*(1) $S$-abelian scheme (i.e. $G$ is smooth over $S$ and its fibers are abelian varieties),*

*(2) $S$-group scheme of multiplicative type,*

*(3) $S$-group scheme finite, étale, of degree invertible on $S$,*

*(4) $S$-reductive group if $S$ is a $\mathbb{Q}$-scheme.*

*Then the functor $X^{G}$ of fixed points of $X$ under $G$ is representable by a closed subscheme of $X$, of finite
presentation, smooth over $S$.*

<!-- label: III.XII.9.8 -->

Indeed, if $1 \to G' \to G \to G'' \to 1$ is an exact sequence of $S$-groups satisfying the hypotheses of the theorem,
the $S$-group $G''$ acts on the functor $X^{G'}$, and the functor $X^{G}$ is nothing other than that of fixed points of
$X^{G'}$ under $G''$. Thus one is reduced to the case of an $S$-group of one of the four types above. By passage to the
limit, one may suppose $S$ noetherian. We shall verify the cohomological criterion stated above for a fiber $G_{s}$
above a geometric point $s$ of $S$ and a finite-dimensional linear representation $V$ of $G_{s}$.

In the case of an abelian scheme, every map from $G^{n}_{s}$ to $V$ is constant, and consequently the $H^{i}(G_{s}, V)$
are zero for $i > 0$.

In the case of a multiplicative-type group scheme, $G_{s}$ is a diagonalizable group. Theorem (I, 5.3.3) shows that the
$H^{i}(G_{s}, V)$ are zero for $i > 0$.

In the two following cases, the argument is the same since it rests on the semisimplicity of the linear representations
of $G_{s}$. Indeed in the case of an $S$-group scheme <!-- original page 165 --> finite, étale, of degree invertible on
$S$, $G_{s}$ is a constant finite group of degree invertible in the residue field $\kappa(s)$; it is well known that
every linear representation of $G_{s}$ is semisimple.

For the reductive case, the residue field $\kappa(s)$ is supposed (algebraically closed) of characteristic zero. One
knows then that every linear representation of $G_{s}$ is semisimple (see [T-Y], theorem 27.3.3).

**Remark 9.9.** *This applies in particular to the case of an action of $G/S$ on a smooth $S$-group scheme $H$. If $G$
is a multiplicative-type group acting by inner transformations on $H$ smooth and affine over $S$, one recovers then the
corollary (XI, 5.3) stating the smoothness of the centralizer of $G$ in $H$.*

<!-- label: III.XII.9.9 -->

**Remark 9.10.** *In the case where $S = \operatorname{Spec}(k)$ and $G$ is a linearly reductive algebraic group defined
over the algebraically closed field $k$, this result is due independently to Fogarty ([F], theorem 5.4) and Iversen
([I], proposition 1.3).*

<!-- label: III.XII.9.10 -->

The proof of Theorem 9.7 uses the following lemma, well known in the case of an affine group scheme (IX, 3.1).

**Lemma 9.11.** *Let $G$ be a group scheme over an affine scheme $S = \operatorname{Spec}(A)$, and $f : S' =
\operatorname{Spec}(A') \to S$ a flat morphism. Set $G' = G \times_{S} S'$. Then for every quasi-coherent
$G$-`O_S`-module $M$, one has canonical isomorphisms*

```text
H^i(G, M) ⊗_A A′ ≃ H^i(G′, M ⊗_A A′)   (i ⩾ 0).
```

<!-- label: III.XII.9.11 -->

Given that the chains of degree $n \geqslant 1$ for Hochschild cohomology are determined by their value at the point
$(id, \cdots, id) \in G(G) \times \cdots \times G(G)$, one has an isomorphism of $A$-modules $C^{n}(G, M) \simeq
\Gamma(G^{n}, M \otimes_{A} O_{G^{n}})$. The cohomology group $H^{n}(G, M)$ is the $n$-th cohomology group of the
complex

```text
L ⟶ Γ(G, M ⊗_A O_G) ⟶ Γ(G², M ⊗_A O_{G²}) ⟶ Γ(G³, M ⊗_A O_{G³}) ⟶ ⋯
```

Since $A'$ is flat over $A$, by ([EGA IV_1, 1.7.21](https://jcreinhold.github.io/ega/iv/12-ch4-01-relative-finiteness-conditions.html#17-improvements-of-earlier-results)) one has

```text
Γ(G^n, M ⊗_A O_{G^n}) ⊗_A A′ ≃ Γ(G′^n, (M ⊗_A A′) ⊗_{A′} O_{G′^n}).
```

This implies the required assertion by taking cohomology.

## Bibliography[^N.D.E-XII-13]

<!-- label: III.XII.bibliography -->

- [Fo73] J. Fogarty, *Fixed point schemes*, Amer. J. Math. 95 (1973), 35–51.
- [RG71] M. Raynaud, L. Gruson, *Critères de platitude et de projectivité*, Invent. Math. 13 (1971), 1–89.
- [Iv72] B. Iversen, *A fixed point formula for action of tori on algebraic varieties*, Invent. Math. 16 (1972),
  229–236.

<!-- original page 166 -->

- [Ray72] M. Raynaud, *Flat modules in algebraic geometry*, Compositio Math. 24 (1972), 11–31.
- [TY06] P. Tauvel, R. W. T. Yu, *Lie algebras and algebraic groups*, Springer-Verlag, 2006.
- [We05] S. Wewers, *Formal deformation of curves with group scheme action*, Ann. Inst. Fourier (Grenoble) 55 (2005),
  1105–1165.

## Footnotes

<!-- LEDGER DELTA — Exposé XII — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| rang réductif | reductive rank | Per glossary; defined here. |
| rang nilpotent | nilpotent rank | Defined here as `dim C` for `C` a Cartan subgroup. |
| rang unipotent | unipotent rank | `ρ_n − ρ_r`. |
| rang semi-simple | semisimple rank | Reductive rank of `G/R` (R = radical). |
| rang infinitésimal | infinitesimal rank | Nilpotent rank of the Lie algebra; defined in next Exposé. |
| BIBLE | *BIBLE* | Séminaire Chevalley 1956/58; italicized per glossary. |
| principe de l'extension finie | principle of finite extension | Standard phrase from EGA IV. |
| rang réductif localement constant | locally constant reductive rank | Recurrent technical condition. |
| préschéma des tores maximaux | prescheme of maximal tori | Per N° 1.10. |
| sous-groupe de Cartan associé à T | Cartan subgroup associated with T | `Centr_G(T)`. |
| groupe de Weyl géométrique | geometric Weyl group | `W(k)` for an algebraic closure `k`. |
| centre réductif | reductive center | Per glossary. |
| caractères racines | root characters | The characters `m ∈ R` of the `T`-module decomposition of `g`. |
| extension de Chevalley | Chevalley's extension | (∗) `e → V → G → A → e` for not-necessarily-affine smooth connected `G`. |
| élément semi-simple | semisimple element | Standard. |
| `S`-pur | `S`-pure | From Raynaud–Gruson; preserved with American spelling. |
| schéma S-pur | `S`-pure scheme | Same. |
| obstruction infinitésimale | infinitesimal obstruction | Per section 9.3 heading. |
| lissité formelle | formal smoothness | Standard. |
| dévissage | dévissage | Loanword per glossary tradition. |
| cohomologie de Hochschild | Hochschild cohomology | Standard. |
| sous-foncteur T | subfunctor 𝒯 | Functor of maximal tori; `T` reused in the source — italic-script in translation. |
| Transp_G | Transp_G | Notation preserved. |
| Norm_G, Centr_G | Norm_G, Centr_G | Notation preserved. |
| extension splitte | extension splits | N.D.E. correction `splitte → scindée`; rendered as "splits". |
-->

[^N.D.E-XII-1]: N.D.E.: This Séminaire has now been published, in a revised form by P. Cartier, as volume 3 of the
    *Œuvres de Chevalley* (Springer, 2005).

[^N.D.E-XII-2]: N.D.E.: modification made to introduce the prescheme $C = Centr_{G}(T)$ representing the functor
    $Centr_{G}(T)$.

[^N.D.E-XII-3]: N.D.E.: This is the functor of multiplicative-type subgroups of $G$.

[^N.D.E-XII-4]: N.D.E.: modification made to introduce the preschemata $Norm_{G}(T)$ and $G/Norm_{G}(T)$.

[^N.D.E-XII-5]: N.D.E.: which is central!

[^XII-3-1]: The proof given here actually only proves 3.2 for the closed Cartan subgroups of $G$. However, 7.1 a)
    establishes 3.2 in the form stated, and implies that the Cartan subgroups of $G$ are closed.

[^XII-5-0]: For a generalization of the results of the present number to the case where $G$ is not supposed affine over
    $S$, cf. M. Raynaud, *Faisceaux amples sur les schémas en groupes et les espaces homogènes*, Chap. IX.

[^N.D.E-XII-6]: N.D.E.: references to be given here.

[^N.D.E-XII-7]: N.D.E.: i.e. splits!

[^N.D.E-XII-8]: N.D.E.: reference not located in VI_B; see M. Demazure and P. Gabriel, *Groupes algébriques*, I, Masson
    (1970), proposition II.5.1.(c).

[^N.D.E-XII-9]: N.D.E.: to specify this reference.

[^N.D.E-XII-10]: N.D.E.: to specify this reference.

[^XII-7-1]: The proof shows that it suffices to suppose that $C$ is a smooth subgroup of $G$ each of whose geometric
    fibers is the connected centralizer of a subgroup of a maximal torus of `G_S`.

[^N.D.E-XII-11]: N.D.E.: reference not located in VI_B; see M. Demazure and P. Gabriel, *Groupes algébriques*, I, Masson
    (1970), corollary II.5.6.

[^N.D.E-XII-12]: N.D.E.: indicate references here.

[^N.D.E-XII-13]: N.D.E.: additional references cited in this Exposé.
