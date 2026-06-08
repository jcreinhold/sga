# Exposé XIV. Regular elements (continuation). Applications to algebraic groups

<!-- label: III.XIV -->

*by A. Grothendieck, with an Appendix by J.-P. Serre*

## 1. Construction of Cartan subgroups and of maximal tori for a smooth algebraic group

<!-- label: III.XIV.1 -->

<!-- original page 296 -->

**Theorem 1.1.** *Let $G$ be a smooth algebraic group over a field $k$. Then $G$ admits a maximal torus $T$, hence a
Cartan subgroup $C = Centr_{G}(T)$.*

<!-- label: III.XIV.1.1 -->

By virtue of (XII 3.2), it amounts to the same to find a maximal torus $T$ of $G$ or a Cartan subgroup $C$ of $G$.
Moreover, since the maximal tori of $G$ are those of $G^{0}$, we may assume $G$ connected. We distinguish two cases:

1°) *The field $k$ is finite.* Let $T$ be the scheme of maximal tori of $G$ (Exp XII 1.10), which is a smooth scheme
over $k$. Note that $G$ operates on $T$ via inner automorphisms, and by virtue of the conjugation theorem (XII 6.6 a)),
two points of $T_{\bar{k}}$ rational over $\bar{k}$ are congruent under $G_{\bar{k}}(\bar{k})$. Taking into account that
$T$ is smooth over $k$, hence $T_{\bar{k}}$ smooth over $\bar{k}$, it follows that $T_{\bar{k}}$ is isomorphic to
$G_{\bar{k}}/N$, where $N$ is the stabilizer of an element of $T_{\bar{k}}(\bar{k})$, i.e. the normalizer of a maximal
torus $T$ of $G_{\bar{k}}$. Consequently, $T$ is a "homogeneous space" under the action of the group $G$. A well-known
theorem of Lang (Amer. J. Math. 78, 1956, pp. 555–563) tells us that every homogeneous space under a smooth connected
algebraic group over a finite field $k$ admits a rational point. In particular, $T$ admits a rational point, i.e. $G$
admits a maximal torus $T$. *QED*.

2°) *The field $k$ is infinite.* We shall use the <!-- original page 297 -->

**Lemma 1.2.** *Let $G$ be a smooth algebraic group over a field $k$. Then $G$ admits a subgroup of type (C) (XIII
6.2).*

<!-- label: III.XIV.1.2 -->

By virtue of (XIII 6.3), this amounts to saying that $\mathfrak{g}$ contains a Cartan subalgebra $\mathfrak{d}$. This is
trivial if $k$ is infinite, for then $\mathfrak{g}$ contains a regular element $a$, and one takes $\mathfrak{d} = Nil(a,
\mathfrak{g})$. The case of finite $k$ is handled exactly as in the proof of 1°) above, but requires the prior
construction of the scheme $\mathcal{D}$ of Cartan subalgebras of $\mathfrak{g}$ and the fact that this scheme is smooth
over $k$, which will be carried out below (2.16).

To establish 1.1 in case 2°), where we have placed ourselves, it suffices in any event to know 1.2 for $k$ infinite. Let
us also record for the record:

**Lemma 1.3.** *Let $G$ be a smooth, connected, affine algebraic group whose reductive center (XII 4.1 and 4.4) is
reduced to the unit group. Then $G$ is nilpotent if (and only if) its Lie algebra $\mathfrak{g}$ is nilpotent.*

<!-- label: III.XIV.1.3 -->

This is contained in (XII 4.9).

We can now give a procedure for constructing Cartan subgroups of $G$ (also valid when $k$ is finite, granting 1.2 in
that case). Suppose first that $G$ is affine. We proceed by induction on $n = \dim G$, the assertion being trivial if $n
= 0$. So suppose $n > 0$ and the assertion proved for dimensions $n' < n$. Let $Z$ be the reductive center of $G$, and
let

```text
u : G ⟶ G′ = G/Z
```

be the canonical homomorphism. By virtue of (XII 4.7 c)), one has a bijective correspondence $C' \mapsto C = u^{-1}(C')$
between Cartan subgroups of $G'$ and Cartan subgroups of $G$. So, replacing $G$ by $G'$ if necessary, we may suppose
that the reductive center $Z$ of $G$ is reduced to the unit element (since this is the case for that of $G'$ by XII 4.7
b)).

<!-- original page 298 --> By virtue of 1.3, `G` admits a subgroup `D` of type (C). We know that over the algebraic

closure $\bar{k}$ of $k$, $D_{\bar{k}}$ contains a Cartan subgroup of $G_{\bar{k}}$ (XIII 6.6 b)), hence every Cartan
subgroup of $D$ is a Cartan subgroup of $G$ (XIII 2.8 a)). So we are reduced to finding a Cartan subgroup of $D$. If
$\dim D = \dim G$, i.e. $D = G$, then the Lie algebra of $G$ is a Cartan subalgebra of itself, hence is nilpotent, hence
by 1.3 $G$ is nilpotent, hence is a Cartan subgroup of itself. If $\dim D < \dim G$, then by the induction hypothesis
there exists a Cartan subgroup of $D$, which is therefore a Cartan subgroup of $G$, which completes the proof in the
case where $G$ is affine. In the general case, let $Z$ be the center of $G$; then $G/Z = G'$ is affine (XII 6.1) and for
every Cartan subgroup $C'$ of $G'$, its inverse image $C$ in $G$ is a Cartan subgroup of $G$ (XII 6.6 e)). One is
reduced to finding a Cartan subgroup of the smooth affine algebraic group $G'$, a case already treated.

**Corollary 1.4.** *Let $G$ be a smooth group scheme of finite type over an artinian scheme $S$. Then $G$ admits a
maximal torus $T$, hence a Cartan subgroup $C = Centr_{G}(T)$. Every torus $S$ in $G$ is contained in a maximal torus.*

<!-- label: III.XIV.1.4 -->

One may indeed suppose $S$ local of residue field $k$; then by virtue of 1.1, $G_{0} = G \times_{S}
\operatorname{Spec}(k)$ admits a maximal torus $T_{0}$, and by virtue of (IX 3.6 bis) and (X 2.3), $T_{0}$ comes from a
torus $T$ of $G$, which is evidently a maximal torus. The last statement follows from this, applying the preceding
result to the centralizer of $S$, which is indeed smooth over $k$ (XI 2.4).

**Remarks 1.5.** a) We shall give below (3.20, 3.21 and XV) variants of 1.4 in the case where $S$ is not assumed
artinian.

<!-- label: III.XIV.1.5 -->

b) I do not know whether every algebraic group $G$ (not necessarily smooth) over a field $k$ admits a maximal torus. The
question only arises in characteristic $p > 0$, and <!-- original page 299 --> using 1.1 for a smooth quotient group of
the form $G' = G/I$, where $I$ is a suitable radicial subgroup of $G$ (for example, the kernel of a sufficiently high
power of the Frobenius homomorphism), one is reduced, by taking the inverse image in $G$ of a maximal torus of $G'$, to
the case where $(G_{\bar{k}})_{red}$ is a torus ($\bar{k}$ always denoting the algebraic closure of $k$). It is easy to
see that the answer is affirmative when $G$ is commutative (or more generally nilpotent): then $G$ admits a unique
maximal torus, which one may construct for example by descent from the maximal torus of $G_{\bar{k}}$ [^XIV-1-1].

c) In the case where $G$ is affine, and $k$ is perfect or $G$ solvable, 1.1 is known and due to Rosenlicht; his proof is
very different from the one given here.

d) When $k$ is infinite, 1.1 is a consequence of the much more precise result that the scheme $T$ of maximal tori of $G$
is a rational variety, proved below (6.1). The method is essentially a combination of the proof of 1.1 and of the
explicit description of the structure of the scheme $\mathcal{D}$ of Cartan subalgebras of $\mathfrak{g}$. To reach the
desired result, we must first generalize to the case of an arbitrary base prescheme certain results from (XIII 4 to 6)
(this is the goal of the next two sections), and refine the previous construction proving 1.1, by using the fact that
every Cartan subgroup of $G$ is contained in one and only one subgroup of type (C) of $G$ (Nos 4, 5).

## 2. Lie algebras over an arbitrary prescheme: regular sections and Cartan subalgebras

<!-- label: III.XIV.2 -->

**Lemma 2.1.** *Let $A$ be a ring, $\mathfrak{d}$ a Lie algebra over $A$, and for every $s \in \operatorname{Spec}(A)$,
let $\mathfrak{d}(s) = \mathfrak{d} \otimes_{A} k(s)$ be the corresponding Lie algebra over the residue field $k(s)$.
Suppose the $A$-module $\mathfrak{d}$ is of finite presentation. The following conditions are equivalent:*

<!-- label: III.XIV.2.1 -->

- *(i) For every $s \in \operatorname{Spec}(A)$, $\mathfrak{d}(s)$ is nilpotent.*
- *(ii) For every $x \in \mathfrak{d}$, $ad(x)$ is nilpotent.*
- *(iii) There exists an integer $N \geqslant 0$ such that for every sequence $x_{1}, \cdots, x_{N}$ of elements of
  $\mathfrak{d}$, one has*

<!-- original page 300 -->

$$ ad(x_{1}) ad(x_{2}) \cdots ad(x_{N}) = 0. $$

When $A$ is a field, the equivalence of (i) and (iii) is the definition of "nilpotent", that of (ii) and (iii) is a
well-known consequence of Engel's theorem (Bourbaki, *Groupes et algèbres de Lie*, Chap. I, § 4, N° 2). In the general
case, one has trivially (iii) ⇒ (ii), and (ii) ⇒ (i) thanks to the preceding result and to the fact that (ii) is stable
by passage to quotients and by localization. It remains to prove (i) ⇒ (iii). When $A$ is local artinian with maximal
ideal $\mathfrak{m}$, let $n > 0$ be an integer such that $\mathfrak{m}^{n} = 0$, let $N$ be an integer such that
condition (iii) is satisfied for $\mathfrak{d}(s) = \mathfrak{d} \otimes_{A} A/\mathfrak{m}$, and take $N' = nN$; one
sees at once that this integer satisfies (iii). When $A$ is noetherian, there exist finitely many elements $s_{i} \in
\operatorname{Spec}(A)$ and ideals of definition $\mathfrak{q}_{i} \subset A_{s_{i}}$ such that the natural map

```text
𝔡 ⟶ ∏_i 𝔡 ⊗_A A_i,    where A_i = A_{s_i}/𝔮_i,
```

is injective; then by what precedes there exists for every $i$ an integer $N_{i}$ satisfying (iii) for the Lie algebra
$\mathfrak{d} \otimes_{A} A_{i}$, and taking $N$ to be the largest of the $N_{i}$, one satisfies (iii) for
$\mathfrak{d}$. Finally, the general case reduces to the noetherian case by the usual procedure explained in
([EGA IV 8](https://jcreinhold.github.io/ega/iv/21-ch4-08-projective-limits.html#8-projective-limits-of-preschemes)).

**Definition 2.2.** *Let $S$ be a prescheme, $\mathfrak{d}$ a quasi-coherent Lie algebra over $S$ that is a module of
finite presentation. One says that $\mathfrak{d}$ is locally nilpotent if for every $s \in S$, the Lie algebra
$\mathfrak{d}(s)$ over $k(s)$ is nilpotent. One says that $\mathfrak{d}$ is strictly locally nilpotent if it is locally
free, and if on every open $U$ of $S$ on which it is of constant rank $r$, its Killing polynomial reduces to
$P_{\mathfrak{d}}(t) = t^{r}$.*

<!-- label: III.XIV.2.2 -->

Of course, if $\mathfrak{d}$ is a locally free Lie algebra (as a module) over $S$, one defines its Killing polynomial as
a polynomial

```text
P_𝔡 ∈ A[t],    where A = Γ(Sym_{𝒪_S}(𝔡)) ≃ Γ(W(𝔡))
```

<!-- original page 301 -->

is the ring of sections of the structure sheaf of the vector bundle $W(\mathfrak{d})$ defined by $\mathfrak{d}$.

It is evident that the two notions just introduced in 2.2 are stable by base change, and of local nature for the fpqc
topology. Let us note:

**Proposition 2.3.** *If $\mathfrak{d}$ is strictly locally nilpotent, it is locally nilpotent. The converse is true
when $\mathfrak{d}$ is locally free and $S$ is reduced.*

<!-- label: III.XIV.2.3 -->

The proof is immediate.

**Definition 2.4.** *Let $S$ be a prescheme, $\mathfrak{g}$ a Lie algebra over $S$ that is a locally free module of
finite type. Let $\mathfrak{d}$ be a Lie subalgebra of $\mathfrak{g}$; one says that it is a Cartan subalgebra if it
satisfies the following conditions:*

<!-- label: III.XIV.2.4 -->

- *(i) $\mathfrak{d}$ is a locally direct factor submodule (hence also locally free of finite type).*
- *(ii) For every $s \in S$, $\mathfrak{d}(s)$ is a Cartan subalgebra of $\mathfrak{g}(s)$.*

**Definition 2.5.** *Let $S$, $\mathfrak{g}$ be as in 2.4. A section $a$ of $\mathfrak{g}$ is called quasi-regular if
for every $s \in S$, $a(s) \in \mathfrak{g}(s)$ is a regular element of the Lie algebra $\mathfrak{g}(s)$ over $k(s)$.
One says that $a$ is a regular section if it is quasi-regular and contained in a Cartan subalgebra of $\mathfrak{g}$.*

<!-- label: III.XIV.2.5 -->

Notions 2.4 and 2.5 are again stable by base change, and of local nature for the fpqc topology. Only the last assertion,
and only for the notion "regular section", requires a proof, and follows from the fact that the Cartan subalgebra
containing a given regular section is uniquely determined. More precisely:

<!-- original page 302 -->

**Proposition 2.6.** *Let $S$, $\mathfrak{g}$ be as in 2.4 and let $a$ be a quasi-regular section of $\mathfrak{g}$.
Then there exists at most one Cartan subalgebra of $\mathfrak{g}$ containing $a$. For one to exist, i.e. for $a$ to be a
regular section, it is necessary and sufficient that $a$ satisfy the following condition: $\mathfrak{d} = Nil(a,
\mathfrak{g})$ is a locally direct factor submodule of $\mathfrak{g}$, and $ad(a)$ induces an automorphism of
$\mathfrak{g}/\mathfrak{d}$. In this case, $\mathfrak{d}$ is the unique Cartan subalgebra of $\mathfrak{g}$ containing
$a$.*

<!-- label: III.XIV.2.6 -->

Suppose indeed that $a$ is contained in the Cartan subalgebra $\mathfrak{d}$ of $\mathfrak{g}$. Then
$ad(a)_{\mathfrak{g}/\mathfrak{d}}$ is bijective on each fiber, hence (since $\mathfrak{g}/\mathfrak{d}$ is locally free
of finite type) it is an automorphism of $\mathfrak{g}/\mathfrak{d}$; on the other hand by virtue of 2.1
$ad(a)_{\mathfrak{d}}$ is locally nilpotent, hence $\mathfrak{d} = Nil(a, \mathfrak{g})$, which proves the uniqueness of
$\mathfrak{d}$, and the necessity of the stated regularity criterion. For sufficiency, note that the hypothesis made on
$a$ implies that the formation of $Nil(a, \mathfrak{g})$ commutes with base extension and in particular with passage to
fibers, which shows in particular that the fibers $\mathfrak{d}(s)$ of $\mathfrak{d} = Nil(a, \mathfrak{g})$ are Cartan
subalgebras of the $\mathfrak{g}(s)$; moreover $\mathfrak{d}$ is a Lie subalgebra of $\mathfrak{g}$ by virtue of (XIII
4.1), hence it is a Cartan subalgebra.

**Corollary 2.7.** *Under the conditions of 2.4, let $\mathfrak{d}$ be a Cartan subalgebra of $\mathfrak{g}$, $a$ a
section of $\mathfrak{d}$ that is regular in $\mathfrak{g}$, $u$ an automorphism of $\mathfrak{g}$. In order for $u$ to
preserve $\mathfrak{d}$, it is necessary and sufficient that $u(a)$ be a section of $\mathfrak{d}$.*

<!-- label: III.XIV.2.7 -->

Indeed, by transport of structure $u(a)$ is then a regular section of $\mathfrak{g}$, contained in the two Cartan
subalgebras $\mathfrak{d}$ and $u(\mathfrak{d})$, which are therefore identical.

**Corollary 2.8.** *Under the conditions of 2.4, let $\mathfrak{d}$ be a Cartan subalgebra of $\mathfrak{g}$. Then for
every $s \in S$ such that $k(s)$ is infinite, there exists an open neighborhood $V$ of $s$ and a regular section $a$ of
$\mathfrak{g}$ over $V$ such that $\mathfrak{d} = Nil(a, \mathfrak{g}|V)$ (i.e. such that $a$ is a section of
$\mathfrak{d}|V$).*

<!-- label: III.XIV.2.8 -->

Indeed, the fact that $k(s)$ is infinite ensures the existence of a regular element $a_{0}$ of <!-- original page 303 -->
$\mathfrak{g}(s)$ contained in $\mathfrak{d}(s)$; one can extend it to a section $a$ of $\mathfrak{d}$ on an open neighborhood $U$ of $s$, and since
$ad(a)_{\mathfrak{g}/\mathfrak{d}}$ induces an automorphism of $\mathfrak{g}(s)/\mathfrak{d}(s)$, it follows that, on restricting $V$, $ad(a)_{\mathfrak{g}/\mathfrak{d}}$ is an
automorphism, which implies that $a$ is a quasi-regular section of $\mathfrak{g}|V$ satisfying the desired condition.

Let $\mathfrak{g}$ be as in 2.4; then examination of its Killing polynomial implies at once that the function

```text
s ↦ nilpotent rank of 𝔤(s)
```

on $S$ is upper semi-continuous. We are above all interested in the case when this function is in fact continuous, i.e.
locally constant. Here are some variants of this property:

**Proposition 2.9.** *Let $S$, $\mathfrak{g}$ be as in 2.4. Consider the following conditions:*

<!-- label: III.XIV.2.9 -->

- *(C₀) The nilpotent rank of the $\mathfrak{g}(s)$ ($s \in S$) is a locally constant function of $s$.*
- *(C₁) There locally exists, for the fpqc topology, a Cartan subalgebra of $\mathfrak{g}$.*
- *(C₁′) Like (C₁), with "fpqc topology" replaced by "étale topology".*
- *(C₂) Condition (C₀) is satisfied, and for every $S'$ over $S$, every quasi-regular section of $\mathfrak{g}_{S'} =
  \mathfrak{g} \otimes_{S} S'$ is regular.*
- *(C₃) Every $s \in S$ has an open neighborhood $V$ on which the Killing polynomial of $\mathfrak{g}$ is of the form*

```text
tʳ(tⁿ⁻ʳ + c₁ tⁿ⁻ʳ⁻¹ + ⋯ + c_{n−r})
```

*where for every $s \in V$, $c_{n-r}(s) \in Sym(\mathfrak{g}(s)^{\vee})$ is non-zero.*

*With these notations, one has the implications*

```text
(C₃) ⇒ (C₂) ⇒ (C₁′) ⇒ (C₁) ⇒ (C₀),
```

<!-- original page 304 -->

*and when $S$ is reduced, the five conditions considered are equivalent.*

Let us also note that the conditions considered are manifestly stable by base change, and of local nature for the fpqc
topology.

The implications (C₁′) ⇒ (C₁) ⇒ (C₀) are trivial, the implication (C₀) ⇒ (C₃) when $S$ is reduced is immediate. Note
moreover:

**Corollary 2.10.** *Suppose condition (C₀) satisfied. Let $U$ be the set of elements of $W(\mathfrak{g})$ that are
regular in their fiber. Then $U$ is open; in particular, for every section $a$ of $\mathfrak{g}$ over $S$, the set $V$
of $s \in S$ such that $a(s) \in \mathfrak{g}(s)$ is regular, is open.*

<!-- label: III.XIV.2.10 -->

Indeed, the first assertion follows from the second (applied to $\mathfrak{g}_{S'}$ for every base change $S'$ over
$S$). For the second, since one may suppose here $S$ reduced, hence (C₃) verified, it suffices to examine the Killing
polynomial of $a$ in $\mathfrak{g}$.

The implication (C₂) ⇒ (C₁′) now follows easily from b) in the more precise statement that follows:

**Corollary 2.11.** *Suppose condition (C₂) satisfied. Then:*

<!-- label: III.XIV.2.11 -->

*a) For every $s \in S$ and every Cartan subalgebra $\mathfrak{d}_{0}$ of $\mathfrak{g}(s)$ such that $\mathfrak{d}_{0}$
contains a regular element of $\mathfrak{g}(s)$ (condition automatically satisfied if $k(s)$ is infinite), there exists
an open neighborhood $V$ of $s$ and a subalgebra $\mathfrak{d}$ of $\mathfrak{g}|V$ whose fiber at $s$ is
$\mathfrak{d}_{0}$. If $S_{1}$ is a subprescheme of $S$ containing $s$, and if one has already extended
$\mathfrak{d}_{0}$ to a Cartan subalgebra $\mathfrak{d}_{1}$ of $\mathfrak{g} \otimes_{S} S_{1}$, then one can find an
open neighborhood $V$ of $s$ in $S$ and a Cartan subalgebra $\mathfrak{d}$ of $\mathfrak{g}|V$ such that $\mathfrak{d}
\otimes_{V} (S_{1} \cap V)$ is equal to $\mathfrak{d}_{1}|(S_{1} \cap V)$.*

*b) For every $s \in S$ such that $\mathfrak{g}(s)$ contains a regular element (condition automatically satisfied if
$k(s)$ is infinite), <!-- original page 305 --> there exists an open neighborhood $V$ of $s$ and a Cartan subalgebra
$\mathfrak{d}$ of $\mathfrak{g}|V$.*

Statement b) follows from a) by taking $\mathfrak{d}_{0} = Nil(a_{0}, \mathfrak{g}(s))$, $a_{0}$ being a regular element
of $\mathfrak{g}(s)$. To prove a), let us say the second formulation, one considers a regular element $a_{0}$ of
$\mathfrak{g}(s)$ contained in $\mathfrak{d}_{0}$, one extends it to a neighborhood of $s$ in $S_{1}$ as a section of
$\mathfrak{d}_{1}$, and one extends this last to a section of $\mathfrak{g}$ in a neighborhood of $s$. By virtue of
2.10, this section is quasi-regular in an open neighborhood $V$ of $s$, hence regular by virtue of (C₂), hence by virtue
of 2.6 $\mathfrak{d} = Nil(a, \mathfrak{g}|V)$ satisfies the required conditions.

**Remark 2.12.** I do not know if statement 2.11 a) and b) is valid without the hypothesis of existence of regular
points (when $k(s)$ is finite).

<!-- label: III.XIV.2.12 -->

It remains to prove the implication (C₃) ⇒ (C₂). Let us also note the following equivalent form of (C₃):

- (C₃′) One has (C₀), i.e. the nilpotent rank of the $\mathfrak{g}(s)$ ($s \in S$) is locally constant, and on every
  open $V$ of $S$ where this rank has value $r$, the Killing polynomial of $\mathfrak{g}|V$ is divisible by `tʳ`.

It is necessary to show that this condition implies that every quasi-regular section $a$ of $\mathfrak{g}$ is regular.
Taking 2.6 into account, this is contained in the following lemma (applied to the endomorphism $ad(a)$ of
$\mathfrak{g}$), (iv) ⇒ (iii):

**Lemma 2.13.** *Let $A$ be a ring, $M$ a projective $A$-module of finite type, $u$ an endomorphism of $M$. The
following conditions are equivalent:*

<!-- label: III.XIV.2.13 -->

- *(i) $M$ is the direct sum of two stable submodules $M'$, $M''$ such that $u|M'$ is nilpotent and $u|M''$ is an
  automorphism of $M''$.*
- *(ii) There exists an integer $n > 0$ such that $Im u^{n} + Ker u^{n} = M$.*
- *(iii) The nil-space $Nil(u) = \bigcup_{n>0} Ker u^{n}$ is a direct factor in $M$, and $M = Nil(u) + u(M)$.*

*These conditions are implied by the following (and are equivalent to it when $A$ is reduced):*
    <!-- original page 306 -->

- *(iv) Locally on $\operatorname{Spec}(A)$ (for the Zariski topology) the characteristic polynomial $P_{u}(t)$ of $u$
  can be put in the form*

```text
tʳ(tⁿ⁻ʳ + c₁ tⁿ⁻ʳ⁻¹ + ⋯ + c_{n−r}),
```

*where $c_{n-r}$ is invertible.*

The equivalence of (i) (ii) (iii) is immediate and is recorded for the record. The fact that (i) implies (iv) when $A$
is reduced follows from the fact that in this case a nilpotent endomorphism of a projective module of rank $r$ has
characteristic polynomial `tʳ`, while in any case the characteristic polynomial of an automorphism of a projective
module of finite type has as constant term the determinant of $u$ up to sign (locally on $\operatorname{Spec}(A)$),
hence an invertible element of $A$. Finally, to prove (iv) ⇒ (i), one notes that $M$ is a module over the polynomial
ring `A[t]`, by letting $t$ act as $u$, and the well-known identity

```text
P(u) = 0
```

shows that $M$ is annihilated by `P A[t]`, hence can be considered as a module over $A[t]/P A[t]$. Now writing $P =
t^{r} Q$, where the constant term of $Q$ is invertible, one sees at once that

```text
P A[t] = tʳ A[t] ∩ Q A[t],
```

hence $A[t]/P A[t]$ decomposes into the product of the rings $A[t]/t^{r} A[t]$ and $A[t]/Q A[t]$, whence a corresponding
decomposition of $M$ as a sum of two `A[t]`-modules, i.e. as a sum of two $A$-submodules $M'$ and $M''$ stable under
$u$; this is the decomposition envisaged in (i).

This completes the proof of 2.13, hence of 2.9.

<!-- original page 307 -->

**Corollary 2.14.** *When condition (C₃) of 2.9 is satisfied, the Cartan subalgebras of $\mathfrak{g}$ are strictly
nilpotent (2.2).*

<!-- label: III.XIV.2.14 -->

The proof is immediate.

**Remark 2.15.** a) Let us point out that one can prove a converse of 2.14: (C₃) is equivalent to the fact that for
every $S'$ over $S$, every quasi-regular section of $\mathfrak{g}_{S'}$ is regular and every Cartan subalgebra of
$\mathfrak{g}_{S'}$ is strictly nilpotent, or again, every quasi-regular section of $\mathfrak{g}_{S'}$ is contained in
a strictly nilpotent Cartan subalgebra of $\mathfrak{g}_{S'}$.

<!-- label: III.XIV.2.15 -->

b) Contrary to the other conditions (C₀) to (C₂), condition (C₃) is of "infinitesimal nature". More precisely, when $S$
is locally noetherian, $\mathfrak{g}$ satisfies condition (C₃) if and only if for every base change $S' \to S$ with $S'$
local artinian (if one wishes, $S'$ the spectrum of an artinian quotient of a local ring of $S$), $\mathfrak{g}_{S'}$
satisfies the same condition. Similarly, when (C₀) is satisfied, the condition for a section of $\mathfrak{g}$ to be
regular is of infinitesimal nature.

c) When $\mathfrak{g}$ is the Lie algebra of a smooth prescheme in groups of finite presentation over $S$, then we shall
see that conditions (C₀), (C₁), (C₁′), (C₂) on $\mathfrak{g}$ are equivalent (5.2 a)); I do not know what is the case in
general (except that, even for $S$ local artinian, (C₀) does not imply (C₁)). However, even in the case where
$\mathfrak{g}$ comes from a $G$, and $S$ being local artinian, it is not true in general that (C₂) implies (C₃), since
$\mathfrak{g}$ can be nilpotent without being strictly nilpotent. One obtains an example of this fact starting from a
smooth affine group scheme $G$ over the spectrum $S$ of a discrete valuation ring such that the Lie algebra of the
generic fiber is non-nilpotent (for example the generic fiber is an adjoint semisimple group), and that of the special
fiber is nilpotent (for example, the special fiber being a vector group): then for $n$ large enough, the Lie algebra of
$G_{n} = G \times_{S} S_{n}$ is not strictly nilpotent, however it is nilpotent.

<!-- original page 308 -->

Let us still place ourselves under the conditions of 2.4, and let

$$ \mathcal{D} : (Sch)^{\circ}/S \longrightarrow (Ens) $$

be the functor defined by

```text
𝒟(S′) = set of Cartan subalgebras of 𝔤_{S′}.
```

Let us also introduce the functor

```text
X(S′) = set of pairs (𝔡, a), where 𝔡 is a Cartan subalgebra of 𝔤_{S′} and a a section of 𝔡.
```

One thus has two projections $(\mathfrak{d}, a) \mapsto \mathfrak{d}$ and $(\mathfrak{d}, a) \mapsto a$:

```text
p : X ⟶ 𝒟    and    ψ : X ⟶ W(𝔤).
```

When (C₀) is satisfied, we also consider the open $U$ of regular points of $W(\mathfrak{g})$ (cf. 2.10) and condition
(C₂) is then expressed by the fact that the morphism

$$ \psi^{-1}(U) \longrightarrow U $$

induced by $\psi$ is an isomorphism (a priori, it is a monomorphism thanks to 2.6). Note that it is trivial that the
morphism $p : X \to \mathcal{D}$ is representable by a projection of vector bundles (i.e. for every $S$-morphism $S' \to
\mathcal{D}$, corresponding to a Cartan subalgebra $\mathfrak{d}$ of $\mathfrak{g}_{S'}$, $X \times_{\mathcal{D}} S'$ is
representable by a vector bundle over $S'$, namely $W(\mathfrak{d})$); so if $\mathcal{D}$ is representable, the same is
true of $X$. Now one has:

**Theorem 2.16.** *Let $S$ be a prescheme, $\mathfrak{g}$ a Lie algebra over $S$ that is a locally free
$\mathcal{O}_{S}$-module of finite type; suppose condition (C₀) of 2.9 is satisfied.*

<!-- label: III.XIV.2.16 -->

*a) The functor $\mathcal{D}$ of Cartan subalgebras of $\mathfrak{g}$ defined above is representable by a quasi-projective prescheme of
finite presentation over $S$. The same is true of the functor $X$ defined above.* <!-- original page 309 -->

*b) When condition (C₂) of 2.9 is satisfied, $\mathcal{D}$ and $X$ are smooth over $S$, and the morphism $\psi^{-1}(U)
\to U$ induced by $\psi$ is an isomorphism.*

*c) Still assuming condition (C₂) satisfied, let $s \in S$, $\mathfrak{d}_{0}$ a Cartan subalgebra of $\mathfrak{g}(s)$,
corresponding to a point $d$ of $\mathcal{D}$ rational over $k(s)$. Suppose that $\mathfrak{d}_{0}$ contains a regular
point of $\mathfrak{g}(s)$ (condition automatically satisfied if $k(s)$ is infinite). Let $r$ be the infinitesimal rank
of $\mathfrak{g}(s)$, $n$ its rank over $k(s)$; then there exists an open neighborhood $V$ of $d$ in $\mathcal{D}$ that
is $S$-isomorphic to an open $V'$ of $S[t_{1}, \cdots, t_{n-r}]$.*

*Proof.* One may suppose $\mathfrak{g}$ of constant rank $n$ and of constant nilpotent rank $r$. The assertions made
about $X$ in a) and b) follow at once from the assertions made about $\mathcal{D}$ and from the fact that $X$ is a
vector bundle over $\mathcal{D}$ defined by a locally free module, and are stated only for the record.

a) The functor $\mathcal{D}$ is a subfunctor of the functor $Grass_{n-r}(\mathfrak{g})$ whose value at $S'$ is the set
of locally free quotient modules of rank $n - r$ of $\mathfrak{g}_{S'}$, and it is well known that this latter functor
is representable by a projective prescheme smooth over $S$ (cf. for example Séminaire Cartan 1960/61, Exp. 12, Nos 2 and
3, whose constructions transpose as they stand to the case of preschemes) [^XIV-2-1] [^N.D.E-XIV-1]. So one is reduced
to a relative problem, namely the following: given a locally free quotient module of rank $n - r$ of $\mathfrak{g}$, or
equivalently, a locally free submodule $\mathfrak{d}$ of rank $r$ that is locally a direct factor, represent the
following functor: $F(S') = \emptyset$ if $\mathfrak{d}$ is not a Cartan subalgebra of $\mathfrak{g}_{S'}$, $F(S') =
{\emptyset}$ otherwise. In fact, we shall see that $F$ is representable by a subprescheme of finite presentation of $S$
(which will show that $\mathcal{D} \to Grass$ is representable by an immersion of finite presentation, and will finish
proving a)). One begins by expressing the condition that $\mathfrak{d}_{S'}$ is a Lie subalgebra of $\mathfrak{g}_{S'}$;
one sees at once that this is expressed by the fact that $S' \to S$ factors through a certain closed subprescheme
$S_{1}$ of $S$, of <!-- original page 310 --> finite presentation over $S$ (whose local equations on $S$ can be written
immediately using a basis of $\mathfrak{g}$ adapted to the submodule $\mathfrak{d}$). One may therefore suppose that one
has already $S = S_{1}$. One must then express that $\mathfrak{d}_{S'}$ contains locally for fpqc a quasi-regular
section of $\mathfrak{g}_{S'}$, and for this one considers $V = W(\mathfrak{d}) \cap U$, where $U$ is the open of
regular points of $W(\mathfrak{g})$ (2.10); then the structure morphism $V \to S$ being smooth and quasi-compact, its
image $S_{1}$ is an open part of $S$ and the immersion morphism $S_{1} \to S$ is quasi-compact i.e. of finite
presentation. The condition envisaged on $S'$ is then expressed by saying that $S' \to S$ factors through $S_{1}$. So
one is reduced to the case where $S = S_{1}$, and using the theory of descent, to the case where $\mathfrak{d}$ admits a
section $a$ that is a quasi-regular section of $\mathfrak{g}$. It remains finally to express that the section $a_{S'}$
of $\mathfrak{g}_{S'}$ deduced from $a$ satisfies $ad(a_{S'})_{\mathfrak{g}_{S'}/\mathfrak{d}_{S'}}$ bijective, which
amounts again to saying that $S' \to S$ factors through a certain open subprescheme of finite presentation of $S$,
namely `S_D`, where $D$ is the determinant of $ad(a)_{\mathfrak{g}/\mathfrak{d}}$. But then one sees at once that
$\mathfrak{d}|S_{D}$ is a Cartan subalgebra of $\mathfrak{g}|S_{D}$, hence `S_D` represents the functor $F$, which
proves a).

b) Is immediate thanks to 2.11 a) and (XI 1.5). Of course b) is also a consequence of the more precise statement c).

c) Let $a_{0}$ be a regular point of $\mathfrak{g}(s)$ contained in $\mathfrak{d}_{0}$; extend it to a section $a$ of
$\mathfrak{g}$ on an open neighborhood $V$ of $s$; one may evidently suppose $V = S$. On the other hand let $M_{0}$ be a
complement of the vector space $\mathfrak{d}_{0}$ in $\mathfrak{g}(s)$; then in an open neighborhood $V$ of $S$ there
exists a submodule $M$ of $\mathfrak{g}$, a direct factor of $\mathfrak{g}|V$, such that $M(s) = M_{0}$, and one may
again suppose $V = S$. Let now $\mathcal{V}$ be the subfunctor of $\mathcal{D}$ such that $\mathcal{V}(S')$ is the set
of Cartan subalgebras $\mathfrak{d}'$ of $\mathfrak{g}_{S'}$ satisfying the two following conditions:

- 1°) $\mathfrak{d}'$ is a complement of $M_{S'}$, and
- 2°) the unique section of $(a_{S'} + M_{S'}) \cap \mathfrak{d}'$ is a regular section of $\mathfrak{g}_{S'}$.

<!-- original page 311 -->

Condition 1°) corresponds to an open $V_{1}$ of $\mathcal{D}$ (induced by the open of $Grass_{n-r}(\mathfrak{g})$
defined by the same condition 1°)); the conjunction of 1°) and 2°) corresponds to an open of $V_{1}$ by virtue of 2.10
and (C₂). Hence $\mathcal{V}$ is represented by an open subprescheme $V$ of $\mathcal{D}$, evidently containing $d$.

On the other hand let $\mathcal{V}'$ be the subfunctor of $W(M)$ defined by

$\mathcal{V}'(S') = set of sections u' of M_{S'}$ such that:

- (i) $a_{S'} + u'$ is a regular section of $\mathfrak{g}_{S'}$, and
- (ii) the unique Cartan subalgebra $\mathfrak{d}'$ of $\mathfrak{g}_{S'}$ containing $a_{S'} + u'$ is a complement of
  $M_{S'}$.

Then condition 1°) corresponds to an open subprescheme $V_{1}'$ of $W(M)$, namely the inverse image of the open $U$ of
regular points of $W(\mathfrak{g})$ (cf. 2.10) by the translation morphism $m \mapsto a + m$. The conjunction of (i) and
(ii) corresponds to an open $V'$ of $V_{1}'$, namely the inverse image of $V$ by the obvious morphism
$V_{1}' \to \mathcal{D}$ (associating to $u'$ the unique Cartan subalgebra $\mathfrak{d}'$ of $\mathfrak{g}_{S'}$
containing $a_{S'} + u'$). The restriction of this last morphism to $V'$ is a morphism

$$ V' \longrightarrow V, $$

which is evidently an isomorphism. This proves c).

**Corollary 2.17.** *Let $\mathfrak{g}$ be a finite-dimensional Lie algebra over a field $k$. Then the scheme
$\mathcal{D}$ of Cartan subalgebras of $\mathfrak{g}$ (2.16 a)) is quasi-projective, smooth and irreducible. When
$\mathfrak{g}$ contains a regular element (for example when $k$ is infinite), $\mathcal{D}$ is a rational variety, i.e.
its function field is a pure extension of $k$.*

<!-- label: III.XIV.2.17 -->

The fact that $\mathcal{D}$ is irreducible follows from the fact that one has a surjective morphism $\psi^{-1}(U) \to
\mathcal{D}$, and $\psi^{-1}(U)$ is irreducible, being isomorphic to the open $U$ of $W(\mathfrak{g})$. The assertion on
the function field is an immediate consequence of c).

**Remark 2.18.** I do not know if this conclusion remains valid if $k$ is finite, without supposing that $\mathfrak{g}$
contains a regular point; compare 2.12. One can prove that this is the case when $\mathfrak{g}$ is the Lie algebra of an
algebraic group $G$ smooth over $k$, at least when <!-- original page 312 --> $G/radical$ is an "adjoint" semisimple
group, by using a result of Chevalley pointed out below (cf. Appendix). It is plausible that this result remains valid
without restriction on $G$; it would suffice for this that the cited result of Chevalley be proved for every (not
necessarily adjoint) semisimple algebraic group.

<!-- label: III.XIV.2.18 -->

## 3. Subgroups of type (C) of group preschemes over an arbitrary prescheme

<!-- label: III.XIV.3 -->

**Theorem 3.1.** *Let $S$ be a prescheme, $G$ a smooth $S$-prescheme in groups, $\mathfrak{g}$ its Lie algebra (which is
a locally free module of finite type over $S$), $\mathfrak{h}$ a Lie subalgebra of $\mathfrak{g}$ that is (as a module)
a locally direct factor in $\mathfrak{g}$, and such that for every $s \in S$, the geometric fiber $\mathfrak{h}_{s}$
contains a Cartan subalgebra of $\mathfrak{g}_{s}$. Let $a$ be a quasi-regular section of $\mathfrak{g}$ (2.5). Then*

$$ M_{a} = Transp_{G}(a, \mathfrak{h}) $$

*(subfunctor of $G$ whose $S'$-valued points are the $g \in G(S')$ such that $ad(g) \cdot a_{S'} \in \Gamma(S',
\mathfrak{h}_{S'})$) is representable by a closed subprescheme [^N.D.E-XIV-2] of $G$ smooth over $S$, whose structure
morphism to $S$ is surjective.*

<!-- label: III.XIV.3.1 -->

Consider the canonical morphism

```text
ϕ : G ×_S W(𝔥) ⟶ W(𝔤)
```

given by $(g, x) \mapsto ad(g) \cdot x$; then $M_{a}$ is $S$-isomorphic to $\varphi^{-1}(a)$, the inverse image of $a$
(considered as a section of $W(\mathfrak{g})$ over $S$) by $\varphi$. It will suffice for the smoothness of $M_{a}$ to
show that $\varphi$ is smooth at points of $G \times_{S} W(\mathfrak{h})$ lying over $Im(a)$; more generally $\varphi$
is smooth at every point lying over a point of $W(\mathfrak{g})$ that is regular in its fiber $W(\mathfrak{g}(s))$ over
$S$. To see this, since the source and target of $\varphi$ are smooth, hence flat locally of finite presentation over
$S$, one is reduced to making the verification fiber by fiber, which reduces us to the case where $S$ is the spectrum of
an algebraically closed field, $G$ thus being a locally algebraic group over $k$, $\mathfrak{h}$ a Lie subalgebra of its
Lie algebra $\mathfrak{g}$, containing a Cartan subalgebra of $\mathfrak{g}$, and $a$ a regular point <!-- original page
313 --> of $\mathfrak{g}$. One may evidently suppose (taking into account that $\varphi$ is a $G$-morphism) that the
point of $G \times W(\mathfrak{h})$ envisaged is of the form $(e, a)$. One may evidently suppose $G$ connected, hence of
finite type over $k$, but then our assertion is none other than (XIII 5.4). Moreover, the fact that $M_{a}$ is a closed
subprescheme of $G$ (of finite presentation over $S$) is trivial, since $M_{a}$ is the inverse image of
$W(\mathfrak{h})$ by the morphism $g \mapsto ad(g) \cdot a$ of $G$ into $W(\mathfrak{g})$. The surjectivity of the
structure morphism $M_{a} \to S$ also reduces to the case of an algebraically closed base field, but then $\mathfrak{h}$
contains a Cartan subalgebra $\mathfrak{d}$ by hypothesis, which is therefore conjugate to the Cartan subalgebra
$\mathfrak{d} = Nil(a, \mathfrak{g})$ by the conjugation theorem (XIII 6.1 a)), hence $\mathfrak{h}$ contains a
conjugate of $a$. This completes the proof of 3.1.

**Corollary 3.2.** *Let $G$, $\mathfrak{g}$ be as in 3.1, with $G$ of finite type over $S$; let $\mathfrak{k}$ and
$\mathfrak{h}$ be two Lie subalgebras of $\mathfrak{g}$, locally direct factors (as modules); suppose that one is under
one of the two following hypotheses:*

<!-- label: III.XIV.3.2 -->

*a) For every $s \in S$, the geometric fiber $\mathfrak{k}_{s}$ is nilpotent and contains a regular element of
$\mathfrak{g}_{s}$; the geometric fiber $\mathfrak{h}_{s}$ contains a Cartan subalgebra of $\mathfrak{g}_{s}$.*

*b) $\mathfrak{k}$ is a Cartan subalgebra of $\mathfrak{g}$.*

*Then $Transp_{G}(\mathfrak{k}, \mathfrak{h})$ is a closed subprescheme of $G$ smooth over $S$; moreover, in case a),
its structure morphism to $S$ is surjective.*

The fact that the transporter is representable by a closed subprescheme of finite presentation of $G$ is immediate, and
left to the reader. Let us first prove smoothness in case a). Suppose first that there exists a section $a$ of
$\mathfrak{k}$ that is quasi-regular in $\mathfrak{g}$. Then it suffices to apply 3.1 and the

**Lemma 3.3.** *Under the conditions of 3.2 a), if $a$ is a section of $\mathfrak{k}$ quasi-regular in $\mathfrak{g}$,
then one has*

<!-- label: III.XIV.3.3 -->

```text
Transp_G(𝔨, 𝔥) = Transp_G(a, 𝔥).
```

<!-- original page 314 -->

Indeed, taking the definitions into account, this amounts to showing that if $a$ is moreover a section of
$\mathfrak{h}$, then one has $\mathfrak{k} \subset \mathfrak{h}$. Now since by hypothesis $\mathfrak{k}$ is locally
nilpotent, it follows from 2.1 that $\mathfrak{k} \subset Nil(a, \mathfrak{g})$; on the other hand $Nil(a, \mathfrak{g})
\subset \mathfrak{h}$ because $ad(a)_{\mathfrak{g}/\mathfrak{h}}$ is injective (being so fiber by fiber by virtue of
(XIII 4.8 b))). Whence the conclusion. In the general case, one reduces to the case where $S$ is affine noetherian by
the standard procedure, then to the case where $S$ is local artinian (smoothness being a property of infinitesimal
nature), and by flat descent to the case where its residue field is infinite, hence the fiber $K_{0}$ admits an element
that is regular in $\mathfrak{g}_{0}$. One lifts this element to an element of $K = \Gamma(\mathfrak{k})$, which reduces
us to the preceding case. Thus, in case a) we have proved the smoothness of the transporter; as for the fact that its
structure morphism is surjective, it reduces to the case where $S$ is the spectrum of an algebraically closed field,
hence where $K$ contains a regular point of $\mathfrak{g}$, and one applies 3.3 and 3.1.

To prove b), one is reduced by the definition of smoothness (XI 1.1) to proving that if $S$ is affine, $S_{0}$ a
subscheme defined by a quasi-coherent nilpotent ideal $J$, $g_{0}$ an element of $G(S_{0})$ that transports
$\mathfrak{k}_{0}$ into $\mathfrak{g}_{0}$, then $g_{0}$ lifts to an element $g$ of $G(S)$ that transports
$\mathfrak{k}$ into $\mathfrak{g}$. Now the hypothesis on $g_{0}$ implies that one is under the conditions of a),
already treated. This completes the proof.

Of course, when in 3.2 b) $\mathfrak{h}$ satisfies the stronger hypothesis of 3.1, then (and only then) the structure
morphism $Transp_{G}(\mathfrak{d}, \mathfrak{h}) \to S$ is surjective. Using Hensel's lemma (XI 1.10), one concludes
from 3.1 and 3.2:

**Corollary 3.4.** *Under the conditions of 3.1 for $G$ and $\mathfrak{h}$, and supposing $G$ of finite type over $S$:*

<!-- label: III.XIV.3.4 -->

*a) For every quasi-regular section $a$ of $\mathfrak{g}$, there locally exists for the étale topology a conjugate of
$a$ that is a section of $\mathfrak{h}$.*

*b) For every Cartan subalgebra $\mathfrak{d}$ of $\mathfrak{g}$, $\mathfrak{d}$ is locally for the étale topology
conjugate to a subalgebra of $\mathfrak{h}$.*

In particular, when $\mathfrak{h}$ is itself a Cartan subalgebra of $\mathfrak{g}$, one finds: <!-- original page 315 -->

**Corollary 3.5.** *Let $G$ be a smooth $S$-prescheme in groups of finite type, $\mathfrak{g}$ its Lie algebra,
$\mathfrak{d}$ and $\mathfrak{d}'$ two Cartan subalgebras of $\mathfrak{g}$. Then $Transp_{G}(\mathfrak{d},
\mathfrak{d}')$ is identical to the strict transporter of $\mathfrak{d}$ into $\mathfrak{d}'$, and is a closed
subprescheme of $G$ smooth over $S$, with surjective structure morphism. Locally for the étale topology, $\mathfrak{d}$
and $\mathfrak{d}'$ are conjugate.*

<!-- label: III.XIV.3.5 -->

The fact that the transporter is identical here to the strict transporter follows trivially from the fact that
$\mathfrak{d}$ and $\mathfrak{d}'$ are locally direct factors in $\mathfrak{g}$ and have the same rank at every point.
Hence 3.5 is a particular case of 3.4. In particular, if $\mathfrak{d} = \mathfrak{d}'$:

**Corollary 3.6.** *Let $G$ be as in 3.5, and let $\mathfrak{d}$ be a Cartan subalgebra of $\mathfrak{g}$. Then
$Norm_{G}(\mathfrak{d})$ is a closed subprescheme in groups of $G$ smooth over $S$, whose Lie algebra is identical to
$\mathfrak{d}$.*

<!-- label: III.XIV.3.6 -->

Indeed, this last assertion amounts to saying that $\mathfrak{d}$ is its own normalizer in $\mathfrak{d}$, which follows
at once from the fact that this is true fiber by fiber.

**Corollary 3.7.** *Let $G$, $\mathfrak{g}$ be as in 3.5. Then conditions (C₂), (C₁′), (C₁) of 2.9 are equivalent; in
other words, if $\mathfrak{g}$ admits locally for the fpqc topology a Cartan subalgebra, then every quasi-regular
section of $\mathfrak{g}$ is regular.*

<!-- label: III.XIV.3.7 -->

Indeed, let $a$ be a quasi-regular section; let us prove that it is regular. The question being local for the fpqc
topology, one may suppose that $\mathfrak{g}$ admits a Cartan subalgebra $\mathfrak{d}$. By virtue of 3.4 a), $a$ is
then locally for the étale topology conjugate to a section of $\mathfrak{d}$, which reduces us to the case where $a$ is
a section of $\mathfrak{d}$, where the conclusion is trivial from the definition.

**Definition 3.8.** *Let $G$ be a smooth prescheme in groups over a prescheme $S$. One calls a subgroup of type (C) of
$G$ a subprescheme in groups $D$ of $G$, smooth over $S$, with connected fibers, such that $\mathfrak{d} = Lie(D)$ is a
Cartan subalgebra (2.4) of $\mathfrak{g} = Lie(G)$, i.e. such that for every $s \in S$, $D_{s}$ is a subgroup of type
(C) of the algebraic group $G_{s}$ (XIII 6.2).*

<!-- label: III.XIV.3.8 -->

<!-- original page 316 -->

**Theorem 3.9.** *Let $G$ be a smooth $S$-prescheme in groups of finite presentation, $\mathfrak{g}$ its Lie algebra.
Then:*

<!-- label: III.XIV.3.9 -->

*a) The map*

$$ D \mapsto \mathfrak{d} = Lie(D) $$

*establishes a bijective correspondence between subgroups of type (C) of $G$ and Cartan subalgebras of $\mathfrak{g}$.*

*b) If $D$ and $\mathfrak{d}$ correspond, one has*

$$ Norm_{G}(D) = Norm_{G}(\mathfrak{d}), $$

*it is a closed subprescheme of $G$ smooth over $S$, and one has*

$$ D = Norm_{G}(D)^{0} = Norm_{G}(\mathfrak{d})^{0}. $$

*c) Two subgroups of type (C) $D$ and $D'$ of $G$ are conjugate locally for the étale topology.*

*Proof.* Let $D$ be a subgroup of type (C) of $G$, and $\mathfrak{d}$ its Lie algebra; then $D \subset
Norm_{G}(\mathfrak{d})$, and by virtue of Definition 3.8 and 3.6 this is an inclusion of preschemes in groups smooth
over $S$, inducing an isomorphism on the Lie algebras. Since $D$ has connected fibers, one therefore has $D =
Norm_{G}(\mathfrak{d})^{0}$. Hence the map envisaged in a) is injective; let us prove that it is surjective. So let
$\mathfrak{d}$ be a Cartan subalgebra of $\mathfrak{g}$; then by virtue of 3.6 $Norm_{G}(\mathfrak{d}) = N$ is a closed
subprescheme in groups of $G$ smooth over $S$, admitting $\mathfrak{d}$ as Lie algebra. Since $G$ is of finite
presentation over $S$, the same is true of $N$, hence (as was pointed out in XII after 7.3) the union of the connected
components of the fibers of $N$ is the underlying set of an open subprescheme in groups $N^{\circ}$ of $N$, which is
evidently a subgroup of type (C) of $G$ having Lie algebra $\mathfrak{d}$. This proves a); the first assertion of b)
follows from it at once; <!-- original page 317 --> and the formula $D = Norm_{G}(\mathfrak{d})^{0}$ has already been
proved. Finally, c) follows from a) and 3.5.

**Corollary 3.10.** *Suppose that $\mathfrak{g}$ admits locally for the fpqc topology a Cartan subalgebra (or
equivalently, by virtue of 3.9 a), that $G$ admits locally for the fpqc topology a subgroup of type (C)). Consider the
functor $\mathcal{D} : (Sch)^{\circ}/S \to (Ens)$ defined by $\mathcal{D}(S') =$ set of subgroups of type (C) of
$G_{S'}$. Then this functor is representable by a quasi-projective and smooth prescheme over $S$, with connected
geometric fibers. When $S$ is the spectrum of a field $k$, hence $G$ a smooth algebraic group over $k$, and
$\mathfrak{g}$ admits a regular point (condition automatically satisfied if $k$ is infinite), then $\mathcal{D}$ is a
rational variety over $k$.*

<!-- label: III.XIV.3.10 -->

Indeed, by virtue of 3.9 a), the functor $\mathcal{D}$ is canonically isomorphic to the functor envisaged in 2.16; on
the other hand by virtue of 3.7 condition (C₂) is satisfied. Hence 3.10 follows from 2.16 and 2.17.

**Corollary 3.11.** *Let $D$ be a subgroup of type (C) of $G$, and let $N$ be its normalizer in $G$. Then the quotient
sheaf $G/N$ is canonically isomorphic to the functor $\mathcal{D}$ of 3.10, hence representable by a quasi-projective
and smooth prescheme over $S$, with connected geometric fibers.*

<!-- label: III.XIV.3.11 -->

**Proposition 3.12.** *Let $G$ be a smooth $S$-prescheme in groups of finite presentation over $S$, $H$, $K$ two
subpreschemes in groups, smooth of finite presentation over $S$, with $K$ having connected fibers; $\mathfrak{g}$,
$\mathfrak{k}$, $\mathfrak{h}$ the corresponding Lie algebras. Suppose that one of the two following conditions is
realized for the geometric fibers of these latter:*

<!-- label: III.XIV.3.12 -->

<!-- original page 318 -->

*a) For every $s \in S$, $\mathfrak{k}_{s}$ contains a regular element of $\mathfrak{g}_{s}$, and $\mathfrak{h}_{s}$
contains a Cartan subalgebra of $\mathfrak{g}_{s}$.*

*b) For every $s \in S$, $\mathfrak{k}_{s}$ contains a Cartan subalgebra of $\mathfrak{g}_{s}$.*

*Under these conditions, in order to have $H \supset K$, it is necessary and sufficient that one have $\mathfrak{h}
\supset \mathfrak{k}$.*

Of course, we need only prove that if $\mathfrak{h} \supset \mathfrak{k}$, then $H \supset K$. In case b), the inclusion
$\mathfrak{h} \supset \mathfrak{k}$ shows that one is in fact under the conditions of a), so it suffices to prove a).
Proceeding as in 3.2 a) by reduction to the case $S$ local artinian, one is reduced to the case where there exists a
section $a$ of $\mathfrak{k}$ that is quasi-regular in $\mathfrak{g}$. In this case, proceeding as in (XIII 5.5), one is
reduced to the following statement:

**Corollary 3.13.** *Let $G$ be a smooth $S$-prescheme in groups of finite presentation over $S$, $H$ a subprescheme in
groups of $G$ smooth of finite presentation over $S$, $\mathfrak{g}$ and $\mathfrak{h}$ the Lie algebras, $a$ a section
of $\mathfrak{h}$ that is quasi-regular in $\mathfrak{g}$. Suppose that for every $s \in S$, the geometric fiber
$\mathfrak{h}_{s}$ contains a Cartan subalgebra of $\mathfrak{g}_{s}$. Let*

<!-- label: III.XIV.3.13 -->

$$ M_{a} = Transp_{G}(a, \mathfrak{h}), $$

*which is a closed subprescheme of $G$ smooth over $S$ (cf. 3.1), so that $M^{0}_{a}$ (union of the connected components
of the identity element in the fibers of $M_{a}$) is an open part of $M_{a}$, which we shall endow with the structure
induced by $M_{a}$. One then has $H^{0} = M^{0}_{a}$.*

Evidently one has $H \subset M_{a}$, whence $H^{0} \subset M^{0}_{a}$. Since this is an inclusion of preschemes smooth
over $S$, to prove that it is an equality, one is reduced to verifying it on the fibers, which reduces us to the case
where $S$ is the spectrum of an algebraically closed field, a case treated in (XIII 5.4).

**Corollary 3.14.** *Let $G$ be a smooth $S$-prescheme in groups of finite presentation, $D$ a subgroup of type (C) of
$G$, $H$ a subprescheme in groups of $G$ smooth over $S$ and of finite presentation over $S$, <!-- original page 319 -->
$\mathfrak{d}$ and $\mathfrak{h}$ their Lie algebras. Then one has*

<!-- label: III.XIV.3.14 -->

```text
Transp_G(D, H) = Transp_G(𝔡, 𝔥),
```

*and this functor is representable by a closed subprescheme of $G$ smooth over $S$.*

Indeed, the identity between the two transporters follows from 3.12 b), which allows one to apply 3.2.

**Corollary 3.15.** *Let $G$, $H$ be as in 3.14 and suppose that for every $s \in S$, the geometric fiber
$\mathfrak{h}_{s}$ contains a Cartan subalgebra of $\mathfrak{g}_{s}$. Suppose moreover that $\mathfrak{g}$ admits
locally for the fpqc topology a Cartan subalgebra. Then locally for the étale topology, $H$ contains a subgroup of type
(C) of $G$.*

<!-- label: III.XIV.3.15 -->

By virtue of 3.7 and 3.9 a), $G$ admits locally for the étale topology a subgroup of type (C), so one may suppose that
$G$ admits such a subgroup, say $D$. Then the hypothesis on $\mathfrak{h}$ means also that the structure morphism of the
transporter considered in 3.14 is surjective (taking into account the conjugation theorem XIII 6.1 a)). One concludes by
Hensel's lemma (XI 1.10).

**Corollary 3.16.** *Let $G$, $H$, $K$ be as in 3.12 a); suppose moreover that for every $s \in S$, the geometric fiber
$\mathfrak{k}_{s}$ is nilpotent (i.e. $\mathfrak{k}$ is locally nilpotent). Then one has*

<!-- label: III.XIV.3.16 -->

```text
Transp_G(K, H) = Transp_G(𝔨, 𝔥),
```

*and this functor is representable by a closed subprescheme of $G$ smooth over $S$, whose structure morphism to $S$ is
surjective. $H$ contains locally for the étale topology a subgroup conjugate to $K$.*

<!-- original page 320 -->

The identity of the two transporters is again contained in 3.12 a), the assertion on its structure is then none other
than 3.2 a), and the last assertion of 3.16 is then a consequence of Hensel's lemma.

**Remarks 3.17.** a) In 3.12 and 3.16, one may replace the hypothesis that $K$ is smooth over $S$ by the following
weaker hypothesis: the sheaf $e_{K}*(\Omega^{1}_{K/S}) = \omega^{1}_{K}$ of relative 1-differentials along the unit
section is locally free. In this way, 3.12 contains (XIII 5.5).

<!-- label: III.XIV.3.17 -->

b) Let $G$, $\mathfrak{g}$, $\mathfrak{h}$ be as in 3.1, with $G$ of finite presentation over $S$. Then $N =
Norm_{G}(\mathfrak{h})$ is not necessarily smooth over $S$ along the unit section, or equivalently, there does not
necessarily exist a subprescheme in groups $H$ of $S$ smooth over $S$ whose Lie algebra is $\mathfrak{h}$, even if $S$
is the spectrum of a field. When such an $H$ exists, so that one has (taking $H$ with connected fibers) $N =
Norm_{G}(H)$, I do not know whether $N$ is smooth over $S$. In this question, one may evidently reduce to the case where
$S$ is local artinian.

To conclude this section, let us examine the case where $G$ is "semisimple" over $S$:

**Theorem 3.18.** *Let $S$ be a prescheme, $G$ a smooth $S$-prescheme in groups over $S$, whose geometric fibers are
"adjoint" semisimple groups, i.e. semisimple with reductive center (XII 4.1 and 4.4) reduced to the unit group. Then the
subgroups of type (C) of $G$ are identical with its maximal tori, hence also with its Cartan subgroups (XII 3.1).*

<!-- label: III.XIV.3.18 -->

Taking definitions into account, one is reduced to the case where $S$ is the spectrum of an algebraically closed field,
and to proving then that for a maximal torus $T$ of $G$, the Lie algebra $\mathfrak{t}$ of $T$ is a Cartan subalgebra of $\mathfrak{g}$, that
is to say (taking into account the inequality `nilpotent rank of 𝔤 ⩾ nilpotent rank of G = dim T = rank 𝔱 = r`) that
there exists $x \in \mathfrak{t}$ with $\dim Nil(x, \mathfrak{g}) = r$. Since $\mathfrak{t}$ is abelian and *a fortiori* nilpotent, it amounts to the same
to say that there exists $a \in \mathfrak{t}$ such that $ad(a)_{\mathfrak{g}/\mathfrak{t}}$ is injective <!-- original page 321 --> (XIII 5.7 a)). Now
consider the characters $\alpha$ of $T$ that intervene in the representation of $T$ induced by the adjoint representation of
$G$. The structure theory of the semisimple group $G$ (*Bible*, 13 th. 1 a) and th. 3, cor. 2), more precisely the "big
cell" of $G$, semidirect product of $T$ and subgroups $P_{\alpha}$ isomorphic to the additive group $G_{a}$, preserved by $T$ and
corresponding to the "root" characters of $G$ for the torus $T$, shows that the eigenspace of $\mathfrak{g}$ relative to the
trivial character is none other than $\mathfrak{t}$, and the other eigenspaces are of dimension 1, the characters $\alpha$ associated
being none other than the roots of $G$ for $T$. By virtue of the computation of the reductive center of $G$ as the
intersection of the kernels of the characters of $T$ that intervene in the adjoint representation of $G$ (XII 4.8), one
sees that the fact that $G$ is adjoint is interpreted as saying that the roots generate the lattice $M = \operatorname{Hom}(T, G_{m})$.
Now a well-known lemma of the theory of roots tells us that every root is part of a system of simple roots, hence of a
basis of the group generated by the roots, and consequently of a basis of the dual $M$ of $T$ [^N.D.E-XIV-3]. We
conclude:

**Corollary 3.19.** *If $G$ is an adjoint semisimple algebraic group over an algebraically closed field $k$, $T$ a
maximal torus of $G$, then for every root $\alpha$ of $G$ with respect to $T$, $\alpha : T \to G_{m}$, the corresponding
homomorphism $\alpha' : \mathfrak{t} \to k$ is non-zero.*

<!-- label: III.XIV.3.19 -->

This result is essentially equivalent to Theorem 3.18, for given $t \in \mathfrak{t}$, $ad(t)$ is semisimple and its
eigenvalues in $\mathfrak{g}/\mathfrak{t}$ are none other than the $\alpha'(t)$, hence
$ad(t)_{\mathfrak{g}/\mathfrak{t}}$ is injective if and only if the $\alpha'(t)$ are $\neq 0$, and there exists $t \in
\mathfrak{t}$ having this property if and only if all the $\alpha'$ are $\neq 0$.

**Corollary 3.20.** *Let $S$ be a prescheme, $G$ an $S$-prescheme in groups, smooth, of finite presentation over $S$,
whose geometric fibers are connected reductive algebraic groups (i.e. extensions of a semisimple group by a torus). Then
for every $s \in S$ there exists an open neighborhood $U$ of $s$ such that $G|U$ admits a maximal torus.* [^XIV-3-1]

<!-- label: III.XIV.3.20 -->

We shall see indeed in XVI that the hypothesis just made on $G$ implies <!-- original page 322 --> that $G$ is affine
over $S$ and of locally constant reductive rank; hence (XII 4.7 c)) $G$ admits a reductive center $Z$, $G' = G/Z$ is a
smooth and affine group over $S$ whose reductive center is reduced to the unit group, and finally the maximal tori of
$G$ and of $G'$ are in bijective correspondence. Moreover, one sees at once that the geometric fibers of $G'$ are
connected semisimple groups, and moreover adjoint by definition (their reductive center being trivial). So it suffices
to limit oneself to the case where $G$ is semisimple and adjoint, and by virtue of 3.18 one is reduced to finding an
open neighborhood $U$ of $s$ and a subgroup of type (C) of $G|U$, or equivalently (3.9 a)) a Cartan subalgebra of
$\mathfrak{g}|U$. Now this is possible if $k(s)$ is infinite, since by virtue of 3.7 $\mathfrak{g}$ satisfies condition
(C₂) of 2.9, hence one may apply 2.11 b). In fact, statement 3.20 remains valid without supposing $k(s)$ infinite.
Indeed, by the preceding argument, it suffices to know that for every adjoint semisimple group $G$ over a finite field
$k$, the Lie algebra $\mathfrak{g}$ of $G$ contains a regular element. Now this statement has been proved by Chevalley
(using the properties of the Coxeter element of the Weyl group...), cf. the Appendix below by J.-P. Serre.

**Remarks 3.21.** a) Statement 3.20 remains valid, with essentially the same proof, replacing $G$ by a closed
subprescheme in groups $H$ smooth over $S$, having everywhere the same rank as $G$ (for example a "parabolic subgroup"
of $G$), provided that $k(s)$ is infinite. I do not know if here again the hypothesis that $k(s)$ is infinite is
superfluous. One can show that this is the case at least if $H$ is parabolic, thanks to the construction of the radical
$U$ of $H$ and of the quotient $H/U$, which reduces us to the semisimple case. Unfortunately, the method of regular
elements seems here powerless, since one easily constructs examples (for example with the projective group and its
"standard" Borel subgroup) where the Lie algebra $\mathfrak{h}$ of $H$ does not contain any regular element.

<!-- label: III.XIV.3.21 -->

<!-- original page 323 -->

b) The proof of 3.20 in fact shows a more precise result (by invoking 3.9 b)) in the case where $k(s)$ is infinite,
namely that every maximal torus $T_{0}$ of $G_{s}$ comes from a maximal torus $T$ on an open neighborhood of $s$. I do
not know if this statement remains valid when $k(s)$ is no longer supposed infinite; the difficulty obviously coming
from the fact that the Lie algebra $\mathfrak{t}_{0}$ of $T_{0}$ does not in general contain a regular element of the
Lie algebra $\mathfrak{g}_{0}$ of the fiber $G_{s}$. An affirmative answer to this problem would imply the following
statement (which is proved only in the case of an infinite residue field or when $A$ is separated and complete): Let $A$
be a local ring, with residue field $k$, $M$ an "Azumaya algebra" over $A$, i.e. an algebra such that $M$ is a free
module of finite type over $A$, and $M_{0} = M \otimes_{A} k$ a central simple algebra over $k$, $D_{0}$ a commutative
subalgebra of $M_{0}$ separable over $k$, such that $[M_{0} : k] = ([D_{0} : k])^{2}$; then there exists a commutative
subalgebra $D$ of $M$, which is a direct factor module in $M$ and such that $D \otimes_{A} k = D_{0}$ (?). (Note that
the datum of $M$ is equivalent to the datum of a principal homogeneous bundle under the projective group $PGL(n)_{A}$,
whence an "inner" twisted form $G$ of $PGL(n)$, and the maximal tori of $G$ correspond bijectively to the commutative
subalgebras $D$ of $M$ étale over $A$ of rank $n$ over $A$.)

c) Applying 3.20 to the centralizer of a subtorus $Q$ of $G$ ($G$ a reductive $S$-prescheme in groups), one deduces that
every such $Q$ is contained, locally for the Zariski topology, in a maximal torus of $G$.

## 4. A digression on Borel subgroups

<!-- label: III.XIV.4 -->

**Definition 4.1.** *Let $G$ be a smooth algebraic group over an algebraically closed field. One calls a Borel subgroup
of $G$ a smooth, solvable, connected algebraic subgroup that is maximal for these properties.*

<!-- label: III.XIV.4.1 -->

When $G$ is affine, one thus recovers the terminology of (*Bible* 6 def. 1). Let us note at once that if $Z$ is a
connected and smooth subgroup of $G$ contained in the center <!-- original page 324 --> (or more generally, solvable and
invariant), then for every Borel subgroup $B$ of $G$, the image `BZ` of $B \times Z$ by the morphism $(b, z) \mapsto bz$
of $B \times Z$ into $G$ is a smooth, solvable, connected subgroup of $G$ containing $B$, hence identical to $B$, hence
$B$ contains $Z$, hence $B$ is the inverse image of an algebraic subgroup $B'$ of $G' = G/Z$, and it is immediate that
$B'$ is a Borel subgroup of $G'$. Taking $Z = Centr(G^{0})^{\circ}_{red}$, $G' = G/Z$ is affine (XII 6.1), hence the
Borel subgroups of $G'$ are conjugate and for such a $B'$, $G'/B'$ is a projective variety (*Bible* 6 th. 4).
Consequently:

**Proposition 4.2.** *Let $G$ be as in 4.1. Then the Borel subgroups of $G$ are conjugate. If $B$ is a Borel subgroup,
then $G/B$ is a projective variety. The maximal tori of $B$ (resp. the Cartan subgroups of $B$, $G$ being connected) are
maximal tori of $G$ (resp. Cartan subgroups of $G$).*

<!-- label: III.XIV.4.2 -->

It remains to prove the last assertion, and one may evidently suppose $G = G^{0}$. For the Cartan subgroups, it follows
from the analogous assertion in $G'$ (*Bible* 6 th. 4 cor. 4) and from (XII 6.6 e)). For the maximal tori, it follows
from the preceding, since by (XII 6.6 c)) the maximal tori of a smooth algebraic group are the maximal tori of its
Cartan subgroups.

**Corollary 4.3.** *Suppose $G$ connected. Then every element of $G$ is contained in a Borel subgroup of $G$.*

<!-- label: III.XIV.4.3 -->

One is reduced to the same statement in $G'$, which is well known (*Bible* 6 th. 5 d)).

**Corollary 4.4.** *Let $B$ be a Borel subgroup of $G$, $C$ a Cartan subgroup of $B$, $N$ its normalizer in $G$; then $N
\cap B = C$.*

<!-- label: III.XIV.4.4 -->

Indeed, $N \cap B = Norm_{B}(C)$, so one is reduced to showing that when $G$ is connected and solvable, a Cartan
subgroup $C$ is its own connected <!-- original page 325 --> normalizer. Now with the preceding notations, $C$ is the
inverse image of a Cartan subgroup $C'$ of $G'$, so one is reduced to the case where $G$ is affine. Since one knows that
the normalizer of a Cartan subgroup is smooth ($C$ being its own connected normalizer, cf. for example XII 6.6 c)), it
suffices to see that $C$ and $N$ have the same $k$-valued points, which is none other than (*Bible* th. 6 d)).

**Definition 4.5.** *Let $G$ be a smooth prescheme in groups of finite presentation over a prescheme $S$. One calls a
Borel subgroup of $G$ any subprescheme in groups $B$ of $G$, smooth of finite presentation, such that for every $s \in
S$, the geometric fiber $B_{s}$ is a Borel subgroup of $G_{s}$.*

<!-- label: III.XIV.4.5 -->

This is therefore, as one verifies at once, a notion stable by base change and of local nature for the fpqc topology
(for if $k'$ is an algebraically closed extension of an algebraically closed field $k$, then an algebraic subgroup $B$
of the smooth algebraic group $G$ over $k$ is a Borel subgroup of $G$ if and only if $B_{k'}$ is one of $G_{k'}$). It
follows from this definition that if $G$ is a smooth algebraic group over an arbitrary field $k$, $B$ a Borel subgroup
of $G$, then $G/B$ is a projective variety, every maximal torus $T$ of $B$ is a maximal torus of $G$, its normalizer in
$B$ is identical to its centralizer $C$, and is a Cartan subgroup of $G$ when $G$ is connected.

**Remarks 4.6.** Unfortunately, it is no longer true in general (even if $G$ is affine over $S$ and $S$ is the spectrum
of the algebra of dual numbers over an algebraically closed field $k$) that two Borel subgroups of $G$ are conjugate
locally for the fpqc topology. As a consequence of this regrettable fact, let us point out that if $G$ is a smooth,
affine, connected algebraic group over a non-perfect field $k$, it is not possible in general to define in a natural way
a homogeneous space $\mathcal{D}$ under $G$, playing the role of a flag variety, i.e. of the variety of Borel subgroups of $G$
(which, over the algebraic closure $\bar{k}$ of $k$, would therefore be isomorphic to $G_{\bar{k}}/B$, where $B$ is a Borel
subgroup of $G_{\bar{k}}$). Indeed, when the quotient of $G_{\bar{k}}$ by its radical $R$ is an adjoint semisimple group, then the
kernel of $G_{\bar{k}} \to \operatorname{Aut}_{\bar{k}}(\mathcal{D})$ is the radical of <!-- original page 326 --> $G_{\bar{k}}$, hence if $\mathcal{D}$ came from a
homogeneous space $D$ under $G$, the radical $R$ would come from a subgroup $R$ of $G$. Now one easily constructs
examples where $G_{\bar{k}}/R$ is adjoint but $R$ is not "defined over $k$". It is easy to see that under these conditions,
the functor $\mathfrak{B} : (Sch)^{\circ}/S \to (Ens)$ such that $\mathfrak{B}(S') =$ set of Borel subgroups of $G_{S'}$ is not representable by a
smooth $S$-prescheme. From the infinitesimal point of view (III § 3), the non-validity of the conjugation theorem is
expressed by the fact that if $B$ is a Borel subgroup of the smooth algebraic group $G$, the cohomology group
$H^{1}(B, \mathfrak{g}/\mathfrak{b})$ [^N.D.E-XIV-4] can be different from zero.

<!-- label: III.XIV.4.6 -->

We shall see on the other hand in a later exposé that when $G$ is semisimple, or more generally reductive, such
unpleasant phenomena do not occur. It is these phenomena no doubt, as well as the absence of good existence theorems,
that explain why Borel subgroups play only a relatively effaced role in the study of general group schemes from the
scheme-theoretic point of view, while they will dominate the theory of semisimple group schemes in the later exposés.

**Proposition 4.8.** [^N.D.E-XIV-5] *Let $G$ be a smooth $S$-prescheme in groups of finite presentation with connected
fibers, $B$ a Borel subgroup of $G$; then $B$ is identical to its own normalizer, and is a closed subprescheme of $G$.*

<!-- label: III.XIV.4.8 -->

Indeed, by virtue of (XII 7.10), one is reduced to proving that over an algebraically closed field $k$, every element of
$G(k)$ that normalizes $B$ is in $B(k)$, which for $G$ affine is a fundamental result of Chevalley (*Bible* 9 th. 1);
the general case reduces to it at once by the reduction already used in 4.2.

**Remark 4.8.1.** One can generalize Definition 4.5 by also introducing the notion of parabolic subgroup of $G$: one
calls thus a subprescheme in groups $P$ of $G$, smooth and of finite presentation over $S$, such that for every $s \in
S$, the geometric fiber $P_{s}$ is a parabolic subgroup of $G_{s}$, i.e. contains a Borel subgroup of $G_{s}$. <!--
original page 327 --> Proposition 4.8 extends (with the same reduction proof to the "set-theoretic" statement, which is
known) to the case of a parabolic subgroup $P$ of $G$. Let us note the following consequence of this result (cf. XVI).
If $P$ is a parabolic subgroup of $G$, then $G/P$ is representable by a quasi-projective prescheme of finite
presentation over $S$ (N.B. one assumes $G$ to have connected fibers). Moreover $G/P$ is evidently smooth over $S$, and
moreover with connected and proper geometric fibers, whence one can conclude easily, using ([EGA III 5.5.1](https://jcreinhold.github.io/ega/iii/12-ch3-05-existence-coherent-algebraic-sheaves.html#55-a-decomposition-of-certain-schemes)), that $D =
G/P$ is in fact proper, hence projective, over $S$. Moreover, if its relative dimension is $n$, it is known that the
invertible sheaf $\Omega^{n}_{D/S}$ is such that its inverse induces on the geometric fibers of $D/S$ ample sheaves,
hence ([EGA III 4.7.1](https://jcreinhold.github.io/ega/iii/11-ch3-04-fundamental-theorem-proper-morphisms.html#47-an-ampleness-criterion)) $(\Omega^{n}_{D/S})^{-1}$ is ample on $D$ relative to $S$.

<!-- label: III.XIV.4.8.1 -->

One sees easily, by reduction to the affine case and to the case of an algebraically closed base field, that if $u : G
\to G'$ is an epimorphism of smooth algebraic groups, then for every Borel subgroup $B$ of $G$, $u(B) = B'$ is a Borel
subgroup of $G'$. We are interested in the case where one obtains in this way a bijective correspondence between Borel
subgroups of $G$ and of $G'$:

**Proposition 4.9.** *Let $G$, $G'$ be two smooth $S$-preschemes in groups of finite presentation with connected fibers,
$u : G \to G'$ a faithfully flat (i.e. surjective) homomorphism of groups [^N.D.E-XIV-6]. Suppose one is in one of the
following two cases (where one has set $N = Ker u$):*

<!-- label: III.XIV.4.9 -->

*a) $N$ is central in $G$.*

*b) $S$ is the spectrum of a field $k$, and if $\bar{k}$ denotes an algebraic closure of it, $N_{\bar{k}} = Ker
u_{\bar{k}}$ is contained in the radical of $G_{\bar{k}}$, i.e. in the largest smooth connected solvable invariant
subgroup of $G_{\bar{k}}$.*

*Then the map $B' \mapsto u^{-1}(B')$ induces a bijection of the set of Borel subgroups of $G'$ with the analogous set
for $G$.*

Case b) follows at once from the correspondence between algebraic subgroups of $G'$ and algebraic subgroups of $G$
containing $N$, and from the fact that when $k$ is <!-- original page 328 --> algebraically closed, the Borel subgroups
of $G$ contain the radical of $G$ (which is immediate by the reasoning preceding 4.2).

Let us prove case a). By virtue of (XII 7.12), the map $H' \mapsto H = u^{-1}(H')$ establishes a bijective
correspondence between subpreschemes in groups $H'$ of $G'$ that are smooth of finite presentation over $S$, with
connected fibers, and that have at every $s \in S$ the same reductive rank and the same nilpotent rank as $G'$, and the
subpreschemes in groups $H$ of $G$ having the analogous properties. Now Borel subgroups (of $G'$, or of $G$) have the
properties in question. It remains to prove that if $H'$, $H$ correspond, then $H'$ is a Borel subgroup of $G'$ if and
only if $H$ is one of $G$. By definition, this question reduces to the case where $S$ is the spectrum of an
algebraically closed field. Now since $N$ is central in $G$ hence in $H$, it follows that $H$ is solvable if and only if
$H'$ is. Finally, taking the correspondence between algebraic subgroups of $G'$ and algebraic subgroups of $G$
containing $N$ into account, one sees at once that $H'$ has the maximal character of Definition 4.1 if and only if $H$
does, which completes the proof.

**Corollary 4.10.** *With the notations of 4.7, if $B'$ and $B$ are Borel subgroups of $G'$ and $G$ which correspond,
one has*

<!-- label: III.XIV.4.10 -->

$$ \mathfrak{b} = Lie(u)^{-1}(\mathfrak{b}') $$

*where $\mathfrak{g}$, $\mathfrak{g}'$, $\mathfrak{b}$, $\mathfrak{b}'$ are the Lie algebras of $G$, $G'$, $B$, $B'$,
and where $Lie(u) : \mathfrak{g} \to \mathfrak{g}'$ is the homomorphism deduced from $u$.*

This statement follows trivially from the definitions and from the relation $u^{-1}(B') = B$.

We can now prove the principal result of the present section:

**Theorem 4.11.** *Let $G$ be a smooth algebraic group over an algebraically closed field $k$, $\mathfrak{g}$ its Lie
algebra. Then $\mathfrak{g}$ is equal to the union of the Lie algebras $\mathfrak{b}$ of the Borel subgroups $B$ of
$G$.*

<!-- label: III.XIV.4.11 -->

<!-- original page 329 -->

One may evidently suppose $G$ connected. Let $R$ be the radical of $G$ and let $G' = G/R$. Then 4.9 b) and 4.10 reduce
us to proving Theorem 4.11 for $G'$ instead of $G$, i.e. one may suppose $G$ semisimple. Let then $Z$ be the center of
$G$, identical to the reductive center, and let $G' = G/Z$. The same reasoning (now using 4.9 a)) reduces us to proving
the theorem for $G'$, i.e. one may suppose $G$ semisimple adjoint. Let $B$ be a Borel of $G$, $T$ a maximal torus of $B$
hence of $G$, and let $\mathfrak{b}$ and $\mathfrak{t}$ be the Lie algebras. By virtue of 3.18, $T$ is a subgroup of
type (C) of $G$, i.e. $\mathfrak{t}$ is a Cartan subalgebra of $\mathfrak{g}$, hence the union of the conjugates of
$\mathfrak{t}$ is dense in $\mathfrak{g}$ (XIII 5.1 (i) ⇒ (vii)). *A fortiori* the union of the conjugates of
$\mathfrak{b}$ is dense in $\mathfrak{g}$. Now let $X$ be the closed subscheme of $G/B \times W(\mathfrak{g})$ whose
$k$-valued points are the $(g', x)$ such that $x \in Ad(g) \cdot \mathfrak{b}$ (cf. XIII 1). Then the morphism $\psi : X
\to W(\mathfrak{g})$ induced by the second projection is proper since $G/B$ is proper over $k$; on the other hand we
have just seen that it is dominant, hence it is surjective, which proves 4.11.

The only result of the present section that we shall use in the rest of this exposé is the following corollary:

**Corollary 4.12.** *Let $k$ be an infinite field, $G$ a smooth algebraic group over $k$, $T$ a maximal torus of $G$,
$\mathfrak{g}$ and $\mathfrak{t}$ the Lie algebras, $u : G \to GL(V)$ a linear representation ($V$ a finite-dimensional
vector space over $k$), whence a representation of Lie algebras $u' : \mathfrak{g} \to \mathfrak{gl}(V)$, making $V$
into a $\mathfrak{g}$-module. Then the minimum of the nullity of $u'(x)$ ($x \in \mathfrak{g}$) is attained for an
element $x \in \mathfrak{t}$.*

<!-- label: III.XIV.4.12 -->

One is reduced at once to the case where $k$ is algebraically closed. One may evidently suppose $G$ connected, and
replacing $G$ by $G/(Ker u)_{red}$ if necessary, one may suppose $G$ affine. Using 4.11 and the conjugation theorem of
maximal tori of $G$, one is reduced to the case where $G$ is moreover solvable. Then $G$ is a semidirect product
$T \cdot V$, where $V$ is the "unipotent part" of $G$, which is a smooth connected unipotent group (*Bible* 6 th. 3).
Hence $\mathfrak{g}$ is the direct sum (as a vector space) of the Lie subalgebras $\mathfrak{t}$ and
$\mathfrak{v} = Lie(V)$. <!-- original page 330 --> By virtue of the Lie-Kolchin theorem (*Bible* 6 th. 1),
$\mathfrak{v}$ admits a composition series by stable subspaces $\mathfrak{v}_{i}$ such that
$\mathfrak{v}_{i}/\mathfrak{v}_{i+1} = w_{i}$ is of dimension 1. Then for each $i$, one has an induced representation
$u_{i} : G \to GL(w_{i}) = G_{m}$ and the corresponding homomorphism of Lie algebras $u'_{i} : \mathfrak{g} \to k$, so
that for every $x \in \mathfrak{g}$, the nullity of $u'(x)$ is equal to the number of $i$ such that $u'_{i}(x) = 0$.
Since $V$ is unipotent, the $u_{i}$ are trivial on $V$, hence the $u'_{i}$ are trivial on $\mathfrak{v}$, which proves
that if $x = t + v$ ($t \in \mathfrak{t}$, $v \in \mathfrak{v}$), then $u'_{i}(x) = u'_{i}(t)$ for all $i$, hence the
nullity of $u'(x)$ is equal to that of $u'(t)$. Assertion 4.12 follows at once.

## 5. Relations between Cartan subgroups and Cartan subalgebras

<!-- label: III.XIV.5 -->

Applying 4.12 to the adjoint representation of $G$, one finds:

**Theorem 5.1.** *Let $G$ be a smooth algebraic group over an infinite field, $T$ a maximal torus of $G$, $\mathfrak{g}
\supset \mathfrak{t}$ the Lie algebras; then $\mathfrak{t}$ contains a regular element of $\mathfrak{g}$.*

<!-- label: III.XIV.5.1 -->

**Corollary 5.2.** *Let $G$ be a smooth $S$-prescheme in groups of finite presentation, $\mathfrak{g}$ its Lie algebra.*

<!-- label: III.XIV.5.2 -->

*a) Conditions (C₀) to (C₂) of 2.9 on $\mathfrak{g}$ are equivalent; in particular, if the infinitesimal rank of the
fibers of $\mathfrak{g}$ at the points of $S$ is locally constant, then $\mathfrak{g}$ admits locally for the étale
topology a Cartan subalgebra, hence (by 3.9 a)) $G$ admits locally for the étale topology a subgroup of type (C).*

*b) Let $H$ be a subprescheme in groups of $G$ smooth of finite presentation over $S$, with connected fibers having the
same reductive rank as $G$ at each $s \in S$ (for example, $H$ is a maximal torus or a Cartan subgroup of $G$); let $D$
be a subgroup of type (C) of $G$; then one has $H \subset D$ if and only if one has $\mathfrak{h} \subset
\mathfrak{d}$.*

*c) Suppose condition (C₀) is satisfied, i.e. the infinitesimal rank of $G$ is locally constant. Let $H$ be a
subprescheme in groups of $G$ smooth of finite presentation over $S$, with connected nilpotent fibers having the same
reductive rank as $G$ at each point (for example, $H$ is a maximal torus or a Cartan subgroup of $G$). Then $H$ is
contained in one and only one subgroup $D$ of type (C) of $G$.*

*d) Suppose that $G$ admits locally for fpqc a Cartan subgroup; then the same is true of every subgroup $D$ of type (C)
of $G$.*

<!-- original page 331 -->

*Proof.* a) Suppose condition (C₀) is satisfied, and let us prove that the same is true of (C₂), i.e. that every
quasi-regular section $a$ of $\mathfrak{g}$ is regular. One reduces as usual to the case $S$ affine noetherian, then,
the question being "infinitesimal" (2.15 b)), to the case where $S$ is local artinian (in which case (C₀) is moreover
trivially satisfied). One may suppose moreover that the residue field $k$ of $S$ is infinite. Note that by virtue of 3.7
it suffices to establish that $\mathfrak{g}$ admits a Cartan subalgebra. Let $T$ be a maximal torus of $G$; by virtue of
5.1 there exists a quasi-regular element $t$ contained in the Lie algebra $\mathfrak{t}$ of $T$; let us prove that it is
regular, which will complete the proof. Consider the linear representation of $T$ in $\mathfrak{g}$ induced by the
adjoint representation of $G$; there exists therefore a finite set $(u_{i})_{i \in I}$ of characters of $T$, such that
$\mathfrak{g}$ decomposes as a direct sum of submodules $\mathfrak{g}_{i}$ stable under $T$, $T$ operating on
$\mathfrak{g}_{i}$ by $u_{i}$ (cf. I § 4.7.3). Let $u'_{i} : \mathfrak{t} \to A$ be the homomorphism of Lie algebras
deduced from $u_{i} : T \to G_{m}$ (N.B. $A$ denotes the ring of $S$). Consider the homomorphisms $u_{i0}$ and $u'_{i0}$
deduced from the preceding by passage to the fibers, i.e. by the base change $A \to k$. Let $I'$ be the set of $i \in I$
such that $u'_{i0} \neq 0$, and let $I'' = I - I'$. The fact that $t$ is regular is expressed by the condition
$u'_{i0}(t_{0}) \neq 0$ for all $i \in I'$, hence $u'_{i}(t)$ invertible for $i \in I'$. The Cartan subalgebra of
$\mathfrak{g}_{0}$ defined by $t$, i.e. the kernel subspace of the semisimple endomorphism $ad(t_{0})$ of
$\mathfrak{g}_{0}$, is $\sum_{i \in I''} (\mathfrak{g}_{i})_{0}$. Consider

```text
𝔡 = ∑_{i ∈ I″} 𝔤_i;
```

then $ad(t)$ is nilpotent in $\mathfrak{d}$; on the other hand it is an automorphism of $\mathfrak{g}/\mathfrak{d} \simeq \sum_{i \in I'} \mathfrak{g}_{i}$. <!-- original page
332 --> By virtue of 2.6, $t$ is therefore regular.

b) Follows from 3.12 a), $H$ satisfying the hypothesis that every geometric fiber of $\mathfrak{h}$ contains a regular
element of that of $\mathfrak{g}$, thanks to 5.1.

c) By virtue of b), one is reduced to proving that $\mathfrak{h}$ is contained in one and only one Cartan subalgebra of
$\mathfrak{d}$. By virtue of a) we know moreover that $\mathfrak{g}$ satisfies (C₂). One is thus reduced to the:

**Lemma 5.3.** *Let $\mathfrak{g}$ be a Lie algebra over $S$ that is a locally free module of finite type and satisfies
condition (C₂) of 2.9. Let $\mathfrak{h}$ be a Lie subalgebra of $\mathfrak{g}$ satisfying the following conditions: it
is a locally direct factor module, it is locally nilpotent, and for every $s \in S$, the geometric fiber
$\mathfrak{h}_{s}$ contains a regular element of $\mathfrak{g}_{s}$. Then $\mathfrak{h}$ is contained in one and only
one Cartan subalgebra of $\mathfrak{g}$.*

<!-- label: III.XIV.5.3 -->

(N.B. in the case of interest to us, $\mathfrak{h}$ satisfies the stated conditions: it is locally nilpotent because $H$
has nilpotent fibers, and the condition on regular elements follows from 5.1.) Since 5.3 is local for the fpqc topology,
it suffices to prove that at a point $s \in S$ such that $\kappa(s)$ is infinite, there exists an open neighborhood $U$
of $s$ such that existence and uniqueness hold for every base change $S' \to S$ factoring through $U$. Take a regular
element of $\mathfrak{g} \otimes \kappa(s)$ contained in $\mathfrak{h} \otimes \kappa(s)$, extend it to a section $a$ of
$\mathfrak{h}$ on an open neighborhood $U$ of $s$; thanks to (C₂) one may suppose this section is regular (2.10). One
may suppose $U = S$. A Cartan subalgebra of $\mathfrak{g}$ containing $\mathfrak{h}$ contains $a$, hence is identical to
$\mathfrak{d} = Nil(a, \mathfrak{g})$ (2.6), whence uniqueness. Moreover since $\mathfrak{h}$ is locally nilpotent, one
indeed has $\mathfrak{h} \subset \mathfrak{d}$, which proves existence.

d) Is a particular case of (XII 7.9 d)).

<!-- original page 333 -->

**Corollary 5.4.** *Let $G$ be a smooth and connected algebraic group over an algebraically closed field $k$, $H$ a
connected algebraic subgroup such that $\mathfrak{h}$ contains a Cartan subalgebra of $\mathfrak{g}$, i.e. such that $H$
contains a subgroup of type (C) of $G$. Then the number of conjugates of $H$ containing a regular element of $G(k)$ is
equal to the number of conjugates of $\mathfrak{h}$ containing a regular element of $\mathfrak{g}$.*

<!-- label: III.XIV.5.4 -->

Indeed, let $g$ be a regular element of $G(k)$, $C$ the unique Cartan subgroup of $G$ containing $g$ (XIII 2); then the
conjugates of $H$ containing $g$ are those containing $C$ (XIII 2.8 b)). Similarly, let $x$ be a regular element of
$\mathfrak{g}$; then if a conjugate $\mathfrak{h}'$ of $\mathfrak{h}$ contains $x$, then
$ad(x)_{\mathfrak{g}/\mathfrak{h}'}$ is injective (XIII 5.4), hence $\mathfrak{h}'$ contains $Nil(x, \mathfrak{g}) =
\mathfrak{d}$, hence the number of conjugates of $\mathfrak{h}$ containing $x$ is equal to the number of conjugates
containing the Cartan subalgebra $\mathfrak{d}$. Moreover $\mathfrak{d}$ is the Lie algebra of a subgroup $D$ of type
(C) of $G$. One may evidently suppose $C \subset D$, and assertion 5.4 will follow from this: in order for $H$ to
contain $C$, it is necessary and sufficient that $\mathfrak{h}$ contain $\mathfrak{d}$. Indeed, by virtue of (XIII 5.5)
the relation $\mathfrak{h} \supset \mathfrak{d}$ implies $H \supset D$ and *a fortiori* $H \supset C$. Conversely, by
5.1 $\mathfrak{t}$ contains a regular element $x$ of $\mathfrak{g}$; then $H \supset C$ implies $\mathfrak{h} \ni x$,
hence as already pointed out, this implies $\mathfrak{h} \supset \mathfrak{d}$. This completes the proof.

Let $G$ be as in 5.2 and suppose that the infinitesimal rank of the fibers of $G$ remains locally constant (condition
(C₀)). Then thanks to 5.2 c), one finds a homomorphism of functors on $(Sch)^{\circ}/S$:

$$ \mathcal{C} \longrightarrow \mathcal{D} $$

where

```text
𝒞(S′) = set of Cartan subgroups of G_{S′}
𝒟(S′) = set of subgroups of type (C) of G_{S′}.
```

<!-- original page 334 -->

By virtue of 3.10 and 5.2 a), $\mathcal{D}$ is representable by a smooth and quasi-projective prescheme over $S$.
Consider the subgroup $D$ of type (C) of $G_{\mathcal{D}}$ playing the universal role with respect to $G/S$; one may
then consider the functor $\mathcal{C}_{D} : (Sch)^{\circ}/\mathcal{D} \to (Ens)$ defined in terms of the
$\mathcal{D}$-group $D$ as $\mathcal{C}$ in terms of the $S$-group $G$. One then has the following result:

**Proposition 5.5.** *Under the preceding conditions, considering $\mathcal{C}$ as a functor over the prescheme
$\mathcal{D}$, then $\mathcal{C}$ is $\mathcal{D}$-isomorphic to the functor $\mathcal{C}_{D}$ "of Cartan subgroups of
$D$".*

<!-- label: III.XIV.5.5 -->

This follows at once from the:

**Corollary 5.6.** *Let $G$ be a smooth $S$-prescheme in groups of finite presentation, $D$ a subgroup of type (C) of
$G$. Then there is a bijective correspondence between Cartan subgroups of $G$ contained in $D$, and Cartan subgroups of
$D$ (more precisely, for a subgroup $H$ of $G$, $H$ is a Cartan subgroup of $G$ if and only if it is a Cartan subgroup
of $D$).*

<!-- label: III.XIV.5.6 -->

Indeed, this is a particular case of (XII 7.9 c)), taking into account that over an algebraically closed field, a
subgroup of type (C) of $G$ contains a Cartan subgroup of $G$.

For the following section, the main result obtained here is 5.2 c) for $H$ a Cartan subgroup of $G$, which permits
stating 5.5 and thus furnishes a useful "dévissage" of $\mathcal{C}$.

## 6. Applications to the structure of algebraic groups

<!-- label: III.XIV.6 -->

**Theorem 6.1.** *Let $G$ be a smooth algebraic group over a field $k$. Consider the scheme $\mathcal{T}$ of maximal
tori of $G$, isomorphic to the scheme $\mathcal{C}$ of Cartan subgroups of $G$, which is a homogeneous space under
$G^{0}$, and a smooth affine connected algebraic scheme (XII 7.1 d)). Then $\mathcal{C}$ is a rational variety, i.e. the
field of rational functions of $\mathcal{C}$ is a pure extension of $k$.*

<!-- label: III.XIV.6.1 -->

We shall first give the proof in the case where $k$ is infinite. One may evidently <!-- original page 335 --> suppose
$G$ connected, since $\mathcal{T}$ hence $\mathcal{C}$ does not change on replacing $G$ by $G^{0}$. Moreover, by virtue
of (XII 7.6), $\mathcal{C}$ does not change on dividing $G$ by a central subgroup. This allows us, first dividing by the
center of $G$, to suppose $G$ affine (XII 6.1), then, dividing by its reductive center (XII 4.1 and 4.4), to suppose
that the reductive center of $G$ is trivial (XII 4.7 b)). Moreover we proceed by induction on $n = \dim G$, supposing
the theorem proved for dimensions $n' < n$. If $G$ is nilpotent, then $\mathcal{C}$ is reduced to a single point
rational over $k$, and 6.1 is trivial. In the contrary case, the Lie algebra of $G$ is non-nilpotent (1.3), hence the
Cartan subalgebras of $\mathfrak{g}$ are of dimension $n' < n$, hence the subgroups of type (C) of $G$ are of dimension
$n' < n$. Consider then the morphism

$$ \mathcal{C} \longrightarrow \mathcal{D} $$

envisaged in 5.5. We know by 3.10 ($k$ being an infinite field, hence $\mathfrak{g}$ containing a regular element) that
$\mathcal{D}$ is a rational variety, i.e. the field $K$ of rational functions on $\mathcal{D}$ is a pure extension of
$k$. Consider the fiber of $\mathcal{C}$ over the generic point $x$ of $\mathcal{D}$; by virtue of 5.5 this is the
scheme of Cartan subgroups of a certain smooth and connected algebraic group $D_{x}$ over $K = \kappa(x)$ (namely $D_{x}
=$ "the generic subgroup of type (C) of $G$"). The field $L$ of rational functions on $\mathcal{C}$ is therefore
isomorphic to the field of rational functions on $\mathcal{C}_{D_{x}}$, which by the induction hypothesis (since $\dim
D_{x} = n' < n$) is a pure extension of $K$. So by transitivity $L$ is a pure extension of $k$.

When $k$ is finite, a different proof is needed. One may still suppose $G$ is affine and connected. Note that $k$ is
perfect; it follows at once that the radical $R$ of $G_{\bar{k}}$ is "defined over $k$", i.e. comes from a subgroup $R$
of $G$. Suppose first $R \neq G$, i.e. $G$ non-solvable, and let

```text
u : G ⟶ G′ = G/R
```

<!-- original page 336 -->

be the canonical morphism. Consider the corresponding morphism $C \mapsto u(C)$

$$ v : \mathcal{C}_{G} \longrightarrow \mathcal{C}_{G'} $$

(whose definition is immediate by virtue of (XII 7.1 e))). Let $x$ be the generic point of $\mathcal{C}_{G'}$; then the
fiber $v^{-1}(x)$ is identified with the scheme of Cartan subgroups of `G_K` (where $K = \kappa(x)$) whose image in
$G'_{K}$ is a certain Cartan subgroup $C'_{x}$ (namely, "the generic Cartan subgroup of $G'$"). It is therefore also the
scheme of Cartan subgroups of $H = u^{-1}_{K}(C')$ (XII 7.9 c)), and since $K$ is here an infinite extension of $k$, it
follows from the already proved part of 7.1 that the field $L$ of rational functions of $\mathcal{C}_{G}$, equal to that
of $\mathcal{C}_{H}$, is a pure transcendental extension of $K$. To prove that it is a pure transcendental extension of
$k$, it therefore suffices to prove that this is the case of $K$, i.e. one is reduced to the case where $G$ is
semisimple. One may moreover suppose that $G$ is adjoint (dividing $G$ by its reductive center if necessary). But then
by virtue of 3.18 one has $\mathcal{C}_{G} \simeq \mathcal{D}_{G}$, and by virtue of 3.10 it suffices to prove that
$\mathfrak{g}$ admits a regular point, which (as was pointed out in 3.20) is an unpublished result of Chevalley
[^N.D.E-XIV-7].

It only remains to treat the case where $k$ is finite, $G$ connected affine solvable. One in fact has a more general
result:

**Corollary 6.2.** *Let $G$ be a smooth solvable algebraic group over a field $k$; then the variety $\mathcal{C}$ of
Cartan subgroups of $G$ is isomorphic to an affine space $\operatorname{Spec} k[t_{1}, \cdots, t_{N}]$.*

<!-- label: III.XIV.6.2 -->

One may still suppose $G$ connected and affine. Let $G_{\infty}$ be the smallest of the groups appearing in the descending
central series of $G$ (by $G_{i}$ such that $G_{i+1} = [G, G_{i}]$); it is thus the smallest invariant algebraic subgroup of
$G$ such that $G/G_{\infty}$ is nilpotent. Let $C$ be a Cartan subgroup of $G$ (it exists by virtue of 1.1); then the image of
$C$ in $G/G_{\infty}$ is a Cartan subgroup of it, hence is equal to $G/G_{\infty}$, consequently the morphism $g \mapsto Ad(g) \cdot C$ of $G_{\infty}$
into $\mathcal{C}$ is an epimorphism, and identifies <!-- original page 337 --> $\mathcal{C}$ with the homogeneous space $G_{\infty}/N \cap G_{\infty}$,
where $N$ is the normalizer of $C$ in $G$ (moreover equal to $C$ as we recalled in 4.4, but this is of little importance
here). Note that $U = G_{\infty}$ is evidently a smooth connected "unipotent" algebraic group (since over the algebraic closure
of $k$, it is contained in the unipotent part of $G$, by virtue of the known structure of smooth affine solvable groups,
*Bible* 6 th. 3). When $k$ is perfect (the only case needed to establish 6.1), it follows very easily that $U$ is even
$k$-unipotent, i.e. admits a composition series by algebraic subgroups $U_{i}$ such that $U_{i}/U_{i+1}$ is isomorphic to
$G_{a}$. In fact, Rosenlicht has proved that this result remains valid for a group of the form $G_{\infty}$ as above, without
restriction on $k$ (M. Rosenlicht, *Questions of rationality for solvable algebraic groups over non perfect fields*,
Annali di Matematica 1963, pp. 97–120, theorem 4 cor. 2), a result clearly more delicate which we shall admit here. It
now suffices to apply the following lemma, doubtless well known to specialists:

**Lemma 6.3.** *Let $U$ be a smooth connected algebraic group over a field $k$, $X = U/V$ a homogeneous space under $U$
having a rational point over $k$. Suppose $U$ is $k$-unipotent. Then as a $k$-scheme, $X$ is isomorphic to an affine
space $\operatorname{Spec} k[t_{1}, \cdots, t_{N}]$.*

<!-- label: III.XIV.6.3 -->

Indeed, let $(U_{i})_{0 \leqslant i \leqslant n}$ be a composition series of $U$ by smooth connected subgroups, with
$U_{n} = (e)$, $U_{0} = U$, $U_{i}/U_{i+1} \simeq G_{a}$, the $U_{i}$ invariant in $U$. Then the $K_{i} = U_{i} V$ are
algebraic subgroups of $U$ (not necessarily smooth nor connected if $V$ is not, but no matter), and $K_{i+1}$ is
invariant in $K_{i}$. One has a canonical morphism $U_{i}/U_{i+1} \to K_{i}/K_{i+1}$ that is an epimorphism, which
proves that $K_{i}/K_{i+1}$ is either reduced to the unit group, or isomorphic to $G_{a}/H_{i}$, where $H_{i}$ is a
finite subgroup of $G_{a}$, which by virtue of Rosenlicht (loc. cit., th. 2) implies that $K_{i}/K_{i+1} \simeq G_{a}$
(a result moreover immediate if $k$ is perfect). Set now $X_{i} = U/K_{i}$; let us prove by induction on $i$ that
$X_{i}$ is isomorphic to an affine space. Indeed, if this is so for $X_{i}$, let us prove that the same is true of
$X_{i+1}$. If $K_{i}/K_{i+1} = e$ one has $X_{i} = X_{i+1}$ and this is trivial. Otherwise, $X_{i+1}$ is a principal
bundle with base $X_{i}$ and structure group $G_{a} \simeq K_{i}/K_{i+1}$. <!-- original page 338 --> So, $X_{i}$ being
affine, $X_{i+1}$ is a trivial bundle, hence is isomorphic to $X_{i} \times G_{a}$, which again proves that $X_{i+1}$ is
isomorphic to an affine space. This proves 6.2 and consequently completes the proof of 6.1.

**Corollary 6.4.** *Let $G$ be a smooth algebraic group over an infinite field $k$. Then the set of $k$-rational points
of $\mathcal{C}$ (notations of 6.1) is dense for the Zariski topology. The union of the Cartan subgroups of $G$ is dense
in $G$.*

<!-- label: III.XIV.6.4 -->

The first assertion is valid for any unirational variety over an infinite field, and is moreover the most important
"arithmetic" consequence of the unirationality results for us here. The second assertion follows from the first and from
the density theorem (XIII 2.1).

**Corollary 6.5.** *Let $G$ be a smooth connected algebraic group over $k$. Then the variety $Z$ of regular semisimple
points of $G$ (XIII 3.5) is a unirational variety. In particular, if $k$ is infinite, the set of $k$-rational points of
$Z$ is dense in $Z$.*

<!-- label: III.XIV.6.5 -->

Indeed, $Z$ is an open of a torus over $\mathcal{C}$, hence its function field $L$ is the function field of a torus
defined over the function field $K$ of $\mathcal{C}$ (namely the "generic maximal torus" of $G$); it is therefore a
unirational extension of $K$ (XIII 3.4), and since $K$ is a pure extension of $k$ by virtue of 6.1, $L$ is a unirational
extension of $k$.

**Corollary 6.6.** *Let $G$ be a smooth connected algebraic group over $k$, and let $H$ be the subgroup of $G$ generated
by the subvariety $Z$ of regular semisimple points, i.e. (XII 8.2) the smallest invariant algebraic subgroup of $G$ such
that $G/H$ has reductive rank zero (i.e. is, over the algebraic closure of $k$, an extension of an abelian variety by a
smooth connected unipotent group). Then $H$ is a unirational variety. In particular, if $G = H$, i.e. (XII 8.4) if $G$
is affine and if over the algebraic closure $\bar{k}$, <!-- original page 339 --> there exists no non-trivial
homomorphism of $G_{\bar{k}}$ to $G_{a}$, then $G$ is a unirational variety, hence if $k$ is infinite, the set of its
$k$-rational points is dense.*

<!-- label: III.XIV.6.6 -->

This follows at once from 6.5, for it is immediate that if one has smooth connected $k$-preschemes $Z_{i}$ that are
unirational varieties and morphisms $u_{i} : Z_{i} \to G$, then the algebraic subgroup of $G$ generated by the $u_{i}$
(VI_B 7.1) is a unirational variety.

As an interesting particular case of 6.5 or 6.6 (whichever one chooses), let us note:

**Corollary 6.7.** *Let $G$ be a smooth connected affine algebraic group of unipotent rank zero; then $G$ is a
unirational variety.*

<!-- label: III.XIV.6.7 -->

One can refine 6.4 as follows:

**Corollary 6.8.** *Let $G$ be a smooth connected algebraic group over the infinite field $k$, and let $C$ be a Cartan
subgroup of $G$. Then the union of the conjugates of $C$ by regular semisimple elements of $G(k)$ is dense in $G$.*

<!-- label: III.XIV.6.8 -->

This follows at once from 6.4 and from (XIII 3.6), which says that the morphism $\varphi : Z \times C \to G$ defined by
$\varphi(t, c) = ad(t)c$ is dominant. This result also implies (without supposing $k$ infinite):

**Corollary 6.9.** *Let $G$ be a smooth connected algebraic group over $k$, $H$ a smooth connected algebraic subgroup of
$G$ such that $H$ has the same reductive rank and the same nilpotent rank as $G$ (i.e. over the algebraic closure
$\bar{k}$ of $k$, $H_{\bar{k}}$ contains a Cartan subgroup of $G_{\bar{k}}$). If $H$ is a unirational variety, the same
is true of $G$. If $H(k)$ is dense in $H$, $G(k)$ is dense in $G$.*

<!-- label: III.XIV.6.9 -->

Indeed, the morphism $\varphi : Z \times H \to G$ defined by $\varphi(t, h) = ad(t)h$ is dominant. Now by virtue of 6.5,
$Z$ is a unirational variety, and by hypothesis the same is true of $H$, hence of $Z \times H$, whence the first result.
The second is proved analogously.

We now recover the following well-known result (due to Chevalley, in characteristic 0, to Rosenlicht in characteristic
$p > 0$):

<!-- original page 340 -->

**Corollary 6.10.** *Let $G$ be a smooth connected affine algebraic group over a perfect field $k$. Then $G$ is a
unirational variety, hence if $k$ is moreover infinite, $G(k)$ is dense in $G$.*

<!-- label: III.XIV.6.10 -->

Indeed, by virtue of 1.1, $G$ admits a Cartan subgroup $C$. By virtue of 6.9 it suffices to prove that this latter is a
unirational variety. Now $k$ being perfect, one sees at once by Galois descent from the case $k$ algebraically closed
(*Bible* 6 th. 2) that one has $C = T \times C_{u}$, where $T$ is the maximal torus of $C$ and $C_{u}$ a smooth
connected unipotent group. One already knows that $T$ is a unirational variety (XIII 3.4); it remains to see that the
same is true of $C_{u}$. Now $k$ being perfect, $C_{u}$ is even $k$-unipotent, and one may apply 6.3.

**Remarks 6.11.** a) One knows (Rosenlicht) examples of twisted forms of $G_{a}$ over a non-perfect field that have only
finitely many rational points, hence *a fortiori* are not unirational varieties. On the other hand, Chevalley has given
an example of a torus over a field of characteristic zero that is not a rational variety. By contrast, it follows from
Chevalley's theory of semisimple groups that over an algebraically closed field, every smooth connected affine algebraic
group is a rational variety. Let us note moreover that the question of unirationality only arises in any event for
affine algebraic groups, a unirational algebraic group being necessarily affine by Chevalley's structure theorem.

<!-- label: III.XIV.6.11 -->

b) With the notations of 6.6, it is tempting to try to give a unirationality condition on $G$ in terms of the group
$G/H$ (which is unipotent if $G$ is supposed affine). It is evidently necessary that this latter be unirational; is this
condition also sufficient? Note that an example of Rosenlicht (loc. cit.) shows that a smooth connected unipotent
algebraic group $U$ may be a rational variety without being $k$-unipotent.

c) It would be interesting to study, over a finite field $k$, questions of the "density" type, such as the following
(raised by Rosenlicht): Let $G$ be a smooth and connected algebraic group <!-- original page 341 --> over $k$; is $G$
generated by its Cartan subgroups? [^XIV-6-1] [^N.D.E-XIV-8]

In this question, one can reduce to the case $G$ affine, by dividing by the center. The answer would be affirmative in
the semisimple case, if one could refine the existence result for regular points of Chevalley pointed out in 3.20, so as
to obtain a regular element of $\mathfrak{g}$ that does not belong to $\mathfrak{h} = Lie(H)$, where $H$ is a smooth
algebraic subgroup of $G$ and $\neq G$ given in advance ($G$ an adjoint semisimple group over the finite field $k$).

## Appendix. Existence of regular elements over finite fields

<!-- label: III.XIV.7 -->

*by J.-P. Serre*

<!-- original page 342 -->

In all that follows, $k$ denotes a finite field, and $\bar{k}$ its algebraic closure; the Galois group of $\bar{k}/k$ is
denoted $\mathcal{G}$; one recalls that, if $q = Card(k)$, $\mathcal{G}$ is topologically generated by the "Frobenius"
element $F : x \mapsto x^{q}$.

We propose to prove the following theorem [^XIV-A-1]:

**Theorem.** *Let $G$ be an adjoint semisimple group defined over $k$, and let $\mathfrak{g}$ be its Lie algebra. The
$k$-Lie algebra $\mathfrak{g}(k)$ contains a regular element.*

<!-- label: III.XIV.7.theorem -->

**Remarks.** (1) It is well to recall that "adjoint" means that the center of $G$ is trivial (as a subgroup scheme of
$G$). In view of the Chevalley seminar, this also means that, if $T$ is a maximal torus of $G$, the group $X(T)$ of
characters of $T$ (defined over $\bar{k}$) is generated by the set $R$ of roots. It follows in particular that the rank
of the Lie algebra $\mathfrak{g}$ is equal to the dimension of $T$ (i.e. to the rank of $G$).

(2) The editor does not know whether the hypothesis that $G$ is adjoint is indispensable.

**Lemma 1.** *It suffices to prove the theorem when $G$ is geometrically simple.*

<!-- label: III.XIV.7.lemma-1 -->

(One says that $G$ is geometrically simple if $G \otimes \bar{k}$ does not contain any normal subgroup scheme smooth
over $\bar{k}$, apart from $G$ and ${e}$; an equivalent condition: the associated root system $R$ is irreducible.)

One may first suppose $G$ indecomposable over $k$. The group $G \otimes \bar{k}$ is then a <!-- original page 343 -->
product of geometrically simple components $S$ that are permuted transitively by the Galois group $\mathcal{G}$. If $H$
is the subgroup of $\mathcal{G}$ fixing one of these components $S$, this component is defined over the field $K$
corresponding to $H$ (i.e. comes by extension of scalars from a subscheme of $G \otimes K$), and a standard argument
shows that $G = \prod_{K/k}(S)$ (i.e. $R_{K/k}(S)$, for readers used to the notation of Weil). Likewise, the Lie algebra
$\mathfrak{g}$ of $G$ is identified with $\prod_{K/k} \mathfrak{s}$, where $\mathfrak{s}$ is the Lie algebra of $S$. If
the theorem is true for $S$, there exists $x \in \mathfrak{s}(K) = \mathfrak{g}(k)$ that is regular in $\mathfrak{s}$;
one then verifies easily that it is regular in $\mathfrak{g}$. *QED*.

From now on, one supposes $G$ geometrically simple and one chooses a maximal torus $T$ of $G$ (one knows this is
possible). One denotes by $X$ the group of characters of $T \otimes \bar{k}$, $R$ its root system, $W$ its Weyl group,
and $E$ the group of automorphisms of $X$ preserving $R$. The group $W$ is a normal subgroup of $E$.

If $T'$ is another torus of $G$, one denotes by $X'$, $R'$, $W'$, $E'$ the group of characters, root system, …,
corresponding. If one chooses $y \in G(\bar{k})$ such that $y \cdot (T \otimes \bar{k}) \cdot y^{-1} = T' \otimes
\bar{k}$, one can identify $X'$, $R'$, $W'$, $E'$ with $X$, $R$, $W$, $E$ thanks to $int(y)$. Changing $y$ modifies this
identification by an automorphism of $X$ corresponding to an element of $W$.

The canonical generator $x \mapsto x^{q}$ of $\mathcal{G}$ operates on $X'$ while preserving $R'$; it therefore defines
an element $f_{T'}$ of $E'$. In particular one sets $f = f_{T}$. When one identifies $E'$ with $E$ as just stated, the
element $f_{T'}$ is transformed into an element $f'$ of $E$, defined up to replacement by $wf'w^{-1}$ with $w \in W$. We
are going to compare this element to $f$:

**Lemma 2.** *One has $f' \equiv f mod W$; conversely, every $f' \in E$ satisfying this condition can be obtained from a
maximal torus $T'$ of $G$.*

<!-- label: III.XIV.7.lemma-2 -->

Set $\bar{T} = T \otimes \bar{k}$, $\bar{T}' = T' \otimes \bar{k}$, and let $y \in G(\bar{k})$ be such that $\bar{yT}y^{-1} = \bar{T}'$; since $y^{q} \bar{T} y^{-q} = \bar{T}'$,
    <!-- original
page 344 --> one concludes that $n = y^{-1} y^{q}$ belongs to the normalizer $N(T)$ of $T$. The effect of $f'$ on the points
of $\bar{T}(\bar{k})$ is then the following:

```text
f′(t) = y⁻¹(yty⁻¹)^q y = y⁻¹ y^q t^q y^{-q} y = n t^q n⁻¹.
```

If $w \in W$ is the element defined by $n$, this shows that $f'$ and $f \circ w$ have the same effect on the points of
$\bar{T}$, hence also on its characters, and one has $f' = f \circ w$, whence $f' \equiv f mod W$. Conversely, if $w \in
W$ is given, one represents it by an element $n \in N(T)(\bar{k})$; thanks to a classical theorem of Lang, one can write
$n$ in the form $n = y^{-1} y^{q}$, with $y \in G(\bar{k})$; the torus $\bar{T}' = \bar{yT}y^{-1}$ is then defined over
$k$, and the preceding calculation shows that the corresponding $f'$ is equal to $f \circ w$.

**Lemma 3.** *Let $X$, $R$, $W$, $E$ be as above ($R$ being irreducible), and let $\varphi \in E/W$. Then there exists
an element $f \in E$ representing $\varphi$, and a family $\theta_{1}, \cdots, \theta_{n}$ of roots enjoying the two
following properties:*

<!-- label: III.XIV.7.lemma-3 -->

*(1) $(\theta_{1}, \cdots, \theta_{n})$ is a basis of $X$.*

*(2) $R$ is the union of the orbits of the $\theta_{i}$ under the powers of $f$ (i.e. every $a \in R$ can be written $a
= f^{m} \theta_{i}$, with suitable $m$ and $i$).*

The proof will be given a little further on.

Here now is a lemma of linear algebra:

**Lemma 4.** *Let $V$ be a vector space over $k$, and let $(\theta_{1}, \cdots, \theta_{n})$ be a basis of the dual of
$V \otimes \bar{k}$. There exists $x \in V$ such that $\theta_{i}(x) \neq 0$ for all $i$.*

<!-- label: III.XIV.7.lemma-4 -->

Let $V*$ be the dual of $V$, and let $W_{i}$ be the subspace of $V* \otimes \bar{k}$ generated by the conjugates of
$\theta_{i}$; this subspace is defined over $k$, i.e. of the form $W_{i} \otimes \bar{k}$. The obvious application
$W_{1} \otimes \cdots \otimes W_{n} \to \wedge^{n} V*$ is not zero (otherwise its extension to $\bar{k}$ would be also,
which is absurd since $\theta_{i} \in W_{i}$ and $\theta_{1} \wedge \cdots \wedge \theta_{n} \neq 0$). There exists
therefore a basis of $V*$ formed of elements $u_{i} \in W_{i}$. Let $x \in V$ be such that $u_{i}(x) \neq 0$ for all $i$
(for example $u_{i}(x) = 1$). The element $x$ answers the question, for if one had $\theta_{i}(x) = 0$, the conjugates
of $\theta_{i}$ would also vanish at $x$, and the same would be true of $u_{i}$, which is not the case.

<!-- original page 345 -->

**End of the proof of the theorem.**

By combining Lemmas 2 and 3, one can choose a torus $T$ whose element $f$ satisfies the properties of Lemma 3. If $Y$ is
the dual of $X$, the Lie algebra $\mathfrak{t}(\bar{k})$ of $T$ [^N.D.E-XIV-9] is canonically identified with $Y \otimes
\bar{k}$, and this operation is compatible with the action of the Galois group (the latter operating on $Y \otimes
\bar{k}$ thanks to its action on $Y$ and on $\bar{k}$). Let $V = \mathfrak{t}(k)$ be the Lie algebra of $T$ over $k$. An
element $x \in V$ is regular if and only if it is not annihilated by any root $\alpha \in R$, or rather by any of the
linear forms $\alpha \in V* \otimes \bar{k}$ defined canonically by the $\alpha \in R$. By Lemma 4, one can find such an
$x$ not annihilated by any of the roots $\theta_{i}$; but every root is conjugate to a $\theta_{i}$ (this is what
condition (2) of Lemma 3 expresses); it follows that $x$ is not annihilated by any root, and it is indeed a regular
element.

**Proof of Lemma 3.**

It relies on properties of Coxeter transformations. Let us briefly recall what this involves:

Let $a_{1}, \cdots, a_{n}$ be a simple root system of $R$, and, for every $i$, let $r_{i}$ be the symmetry corresponding
to $a_{i}$. Set:

$$ c = r_{1} \cdots r_{n}. $$

One has $c \in W$; of course the element $c$ depends on the choice of the simple system $(a_{1}, \cdots, a_{n})$ as well
as on the order of the $a_{i}$; however one shows that its conjugacy class does not depend on any of these choices. One
calls $c$ the *Coxeter element* of the system considered. One shows (we shall admit it) that $c$ does not have 1 as an
eigenvalue.

**Lemma 5.** *Set $\theta_{i} = r_{n} \cdots r_{i+1}(a_{i})$. Then:*

<!-- label: III.XIV.7.lemma-5 -->

*(a) The $\theta_{i}$ form a basis of the group $X$ generated by the roots.*

*(b) One has $\theta_{i} > 0$ and $c(\theta_{i}) < 0$ for all $i$* [^XIV-A-2].

*(c) Every root $a \in R$ such that $a > 0$ and $c(a) < 0$ is equal to one of the $\theta_{i}$.*

<!-- original page 346 -->

*(d) $R$ is the union of the orbits of the $\theta_{i}$ under the powers of $c$.*

It is clear that $\theta_{i}$ is of the form $a_{i} + \sum_{j > i} m_{ij} a_{j}$, with $m_{ij} \in \mathbb{Z}$, which
proves (a). Assertions (b) and (c) are consequences of the following remark: the symmetry $r_{i}$ preserves the sign of
every root distinct from $\pm a_{i}$, and changes the sign of $\pm a_{i}$.

Finally, for (d) one remarks that an orbit of $c$ cannot be entirely formed of positive (resp. negative) roots, since,
taking the sum of these roots one would find a non-zero element of $X$ invariant under $c$, and we have admitted that
$c$ does not have 1 as an eigenvalue. There is therefore necessarily in every orbit an element $a > 0$ such that $c(a) <
0$, and one applies (c).

**Remark.** We have sketched the preceding proof only to facilitate the reader's task; one could have limited oneself to
referring to the canonical texts on Coxeter (cf. for example Koszul, Séminaire Bourbaki, 1959/1960, exposé 191). Said
texts contain other results: the orbits of $c$ all have the same number $h$ of elements, and each contains only one
$\theta_{i}$. In particular $h = Card(R)/n$.

Let us now return to the proof of Lemma 3. Distinguish three cases:

(1) *The element $\varphi \in E/W$ given is equal to the identity element.*

One must then take $f \in W$; one chooses $f = c$; it works by Lemma 5.

(2) *The system $R$ is of type $A_{n}$, with $n$ even $\geqslant 2$, and $\varphi$ is the unique non-trivial element of
$E/W$.*

One knows that $-1 \notin W$; one then takes $f = -c$. A simple calculation shows that $c$ is of order $h = n + 1$;
hence its order is odd. If $a \in R$ is any root, <!-- original page 347 --> one has $a = c^{m} \theta_{i}$ for a pair
$(m, i)$, cf. Lemma 5; by adding $h$ to $m$ if necessary, one may suppose $m$ even, and one sees that one has then $a =
(-c)^{m} \theta_{i} = f^{m} \theta_{i}$. The orbits of the $\theta_{i}$ therefore indeed fill $R$.

(3) *The element $\varphi \in E/W$ is non-trivial, and $R$ is of one of the following types:*

- $A_{n}$, $n$ odd $\geq 3$
- `D_4`
- $D_{n}$, $n \geq 5$
- `E_6`.

(A glance at the classification shows that these are indeed all the cases (with $A_{n}$, $n$ even) where $E/W$ is
non-trivial.)

Let $S$ be a simple root system, which we shall not number for the moment. One knows that $E$ is the semidirect product
of $W$ and the group $\Psi$ of permutations of $S$ that leave invariant the Cartan matrix (or the Dynkin diagram, it is the
same thing). The group $E/W$ is thereby identified with $\Psi$, and in particular $\varphi$ corresponds to an element $\psi \in \Psi$.
One observes by inspection of the Dynkin diagrams (cf. figures above) that every orbit of $\psi$ in $S$ is formed of roots
that are pairwise orthogonal (i.e. not linked in the diagram). \[Note that this would not be the case for $A_{n}$ ($n$
even), which obliged us to treat this case separately.\] If $\sigma$ is such an orbit, the symmetries $r_{a}$, $a \in \sigma$, commute
with each other; their product will be denoted $\rho_{\sigma}$. It is clear that $\rho_{\sigma}$ commutes with $\psi$.

This being so, let us choose on $S$ a total order such that every orbit is a segment for this order relation; this
amounts to numbering the elements of $S$: $S = {a_{1}, \cdots, a_{n}}$. Let $\theta_{1}, \cdots, \theta_{n}$ be the
roots defined above, and $c = r_{1} \cdots r_{n}$ the corresponding Coxeter element. The element $c$ is the product of
the $\rho_{\sigma}$, the $\sigma$ being arranged in a certain order; it follows that it commutes with $\psi$. One then
sets $f = c\psi$. One further remarks that $\psi$ permutes the $\theta_{i}$ among themselves. Indeed, one has
$\psi(\theta_{i}) > 0$ since $\theta_{i} > 0$ and $c(\psi(\theta_{i})) = \psi(c(\theta_{i'})) < 0$, hence (Lemma 5,
(c)), $\psi(\theta_{i})$ is equal to some $\theta_{j}$. It is now immediate <!-- original page 348 --> that $f = c\psi$
answers the question. Indeed, if $a \in R$, one has $a = c^{m} \theta_{i}$ for a pair $(m, i)$, whence $a = f^{m}
(\psi^{-m} \theta_{i}) = f^{m} \theta_{j}$ for some $j$. *QED*.

**Remark.** One can prove that, except in case (2), every orbit of $f$ has exactly $h = Card(R)/n$ elements and contains
one and only one $\theta_{i}$. In case (2), some of the $\theta_{i}$ are superfluous.

<!-- LEDGER DELTA — Exposé XIV — for consolidation in Phase 3
| French                                              | English                                             | Note                                                                                          |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| schéma des tores maximaux                           | scheme of maximal tori                              | Matches glossary "variété des tores maximaux"; here Grothendieck uses *schéma*.               |
| variété des sous-groupes de Cartan                  | variety of Cartan subgroups                         | Parallel to "variety of maximal tori".                                                        |
| sous-groupe de type (C)                             | subgroup of type (C)                                | Per Exposé XIII 6.2; preserved verbatim.                                                      |
| « espace homogène »                                 | "homogeneous space"                                 | Author quotes; preserve quotation marks.                                                      |
| section quasi-régulière / régulière                 | quasi-regular / regular section                     | Distinct technical notions (Def. 2.5).                                                        |
| algèbre de Lie localement nilpotente                | locally nilpotent Lie algebra                       | Def. 2.2.                                                                                     |
| strictement localement nilpotente                   | strictly locally nilpotent                          | Def. 2.2.                                                                                     |
| polynôme de Killing                                 | Killing polynomial                                  | Standard.                                                                                     |
| rang nilpotent / rang infinitésimal / rang réductif | nilpotent rank / infinitesimal rank / reductive rank | All preserved verbatim; standard.                                                              |
| « grosse cellule »                                  | "big cell"                                          | Author quotes; preserve.                                                                      |
| sous-groupe de Borel                                | Borel subgroup                                      | Standard.                                                                                     |
| sous-groupe parabolique                             | parabolic subgroup                                  | Standard.                                                                                     |
| « partie unipotente »                               | "unipotent part"                                    | Author quotes; preserve.                                                                      |
| « défini sur k »                                    | "defined over k"                                    | Author quotes; preserve.                                                                      |
| variété rationnelle                                 | rational variety                                    | Function field is a pure extension.                                                           |
| variété unirationnelle                              | unirational variety                                 | Standard.                                                                                     |
| corps parfait / non parfait                         | perfect / non-perfect field                         | Per task brief.                                                                               |
| descente non galoisienne                            | non-Galois descent                                  | Per task brief (not used explicitly in this Exposé; kept for ledger).                          |
| groupe k-unipotent                                  | `k`-unipotent group                                 | i.e. successive `G_a`-extensions over `k`.                                                    |
| dévissage                                           | dévissage                                           | Keep technical loanword (5.6 ff.).                                                            |
| forme tordue « intérieure »                         | "inner" twisted form                                | Author quotes; preserve.                                                                      |
| « algèbre d'Azumaya »                               | "Azumaya algebra"                                   | Author quotes; preserve.                                                                      |
| élément de Coxeter                                  | Coxeter element                                     | Standard.                                                                                     |
| nullité (d'un endomorphisme)                        | nullity (of an endomorphism)                        | dim ker.                                                                                      |
| Bible                                               | *Bible*                                             | The Chevalley Seminar 1956–58; italicised, per glossary.                                       |
| TranspG / NormG / CentrG                            | Transp_G / Norm_G / Centr_G                         | Notation preserved.                                                                           |
| sous-groupe de Cartan                               | Cartan subgroup                                     | Per glossary.                                                                                 |
| centre réductif                                     | reductive center                                    | Per glossary.                                                                                 |
| Killing couple (T, B)                               | Killing couple `(T, B)`                             | Used in N.D.E. footnote; loanword preserved.                                                  |
-->

[^XIV-1-1]: M. Raynaud gave a negative answer to the question raised here, cf. (XVII Example 5.9.c)).

[^XIV-2-1]: Cf. also
    [EGA I, 2](https://jcreinhold.github.io/ega/i/01-02-preschemes-and-morphisms.html#2-preschemes-and-morphisms-of-preschemes)nd
    edition (to appear in North Holland Publishing Co.).

[^N.D.E-XIV-1]: See § I.1.3 of M. Demazure and P. Gabriel, *Groupes algébriques*, Masson (1970).

[^N.D.E-XIV-2]: One has written $Transp_{G}(a, \mathfrak{h})$.

[^N.D.E-XIV-3]: One has replaced $\hat{T}$ by $T$.

[^XIV-3-1]: This result, as well as 2.11 on which it rests, generalizes immediately to the case where $s$ is replaced by
    a finite part of $S$ contained in an affine open.

[^N.D.E-XIV-4]: Where $\mathfrak{b}$ is the Lie algebra of $B$.

[^N.D.E-XIV-5]: There is no number 4.7.

[^N.D.E-XIV-6]: Add a reference here?

[^N.D.E-XIV-7]: Cf. the Appendix, by J.-P. Serre.

[^XIV-6-1]: This question has since been resolved affirmatively by Steinberg.

[^N.D.E-XIV-8]: Not having identified this result in the *Collected Papers* of R. Steinberg, we give a proof based on
    the Bruhat decomposition. Let $G/k$ be a semisimple group defined over the finite field $k$. The point is to show
    that $G$ is generated by its $k$-Cartan subgroups. This question is stable by central isogeny and by restriction of
    scalars; one is therefore reduced to the case where $G$ is geometrically simple (in the same way as in Lemma 1 of
    the appendix below). Denote by $G\sharp$ the subgroup of $G$ generated by its $k$-subtori. The group $G$ is
    quasi-split (Lang) and therefore admits a Killing couple $(T, B)$. By definition, one has $T \subset G\sharp$; in
    particular $T$ normalizes $G\sharp$. The big cell $R_{u}(B^{-}) T R_{u}(B)$ of $G$ indicates that it suffices to
    verify that $R_{u}(B) \subset G\sharp$. Let $S$ be the maximal split $k$-torus of $T$. One considers the relative
    root system $\Phi(G, S)$ and a basis $\Delta_{k}$. Given $\alpha \in \Phi(G, S)$, denote by $U_{\alpha}$ the
    unipotent subgroup associated to $\alpha$ (cf. A. Borel, *Linear Algebraic Groups*, second edition (1991), Springer,
    Prop. 21.9). Since the $k$-group $R_{u}(B)$ is generated by the $k$-unipotent groups $U_{\alpha}$ ($\alpha \in
    \Delta_{k}$), one is reduced to verifying that $U_{\alpha} \subset G\sharp$. A glance at the classification shows
    that there exists a semisimple group $G_{\alpha}$ of quasi-split type $A_{1}$, ${}^{2}A_{1}$, ${}^{3}A_{1}$ or
    ${}^{2}A_{2}$ such that $U_{\alpha} \subset G_{\alpha} \subset G$. It is therefore permissible to suppose that $G =
    PGL_{2}$ or $G = SU_{3}(K)$, where $K$ denotes the unique quadratic extension field of $k$. The group
    $PGL^{\sharp}_{2}$ containing the standard split torus $T$, the possibilities up to conjugation under $G(k)$ are the
    following: $PGL^{\sharp}_{2} = T$, $PGL^{\sharp}_{2} = B$, or $PGL^{\sharp}_{2} = PGL_{2}$. The case
    $PGL^{\sharp}_{2} = T$ is excluded since $PGL^{\sharp}_{2}$ contains the $k$-torus $R_{K/k}(G_{m})/G_{m}$. The
    preceding discussion indicates that if $PGL^{\sharp}_{2} = B$, then $PGL^{\sharp}_{2} = PGL_{2}$. Hence
    $PGL^{\sharp}_{2} = PGL_{2}$. If $G = SU_{3}(K)$, $\Delta_{k} = {\alpha}$ and the possibilities for $G\sharp$ (up to
    conjugation) are the following: $G\sharp = T$, $G\sharp = B$, `G♯ = U_(2α) ⋊ T`, $G\sharp = \langle U_{2\alpha},
    U_{-2\alpha}, T\rangle = SL_{2} \cdot T$, or $G\sharp = G$. The case $G\sharp = B$ is excluded as for $PGL_{2}$. The
    case $SL_{2} \cdot T$ is excluded because $G\sharp$ contains the $k$-torus $R^{1}_{K/k}(R^{1}_{K_{3}/K}(G_{m}))$,
    $K_{3}/K$ denoting the extension of degree 3 of $K$, and the isogeny class of this torus is irreducible. Moreover,
    this torus also excludes the cases $G\sharp = T$ and `G♯ = U_(2α) ⋊ T`. One concludes that $G\sharp = G$.

[^XIV-A-1]: This theorem is due to Chevalley. The editor wishes to express his gratitude to American Express which, by
    misplacing a trunk of Chevalley manuscripts, obliged him to reconstruct the proof.

[^N.D.E-XIV-9]: One has changed $\bar{T}$ to $T$.

[^XIV-A-2]: For the order relation defined by $(a_{1}, \cdots, a_{n})$.
