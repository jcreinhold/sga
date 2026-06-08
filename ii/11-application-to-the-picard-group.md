# Exposé XI. Application to the Picard group

<!-- label: XI -->

<!-- original page 99 -->

This Exposé is modeled on the preceding one, but this time the result of no. 1 is weaker.

Throughout this Exposé, $X$ will denote a locally noetherian prescheme, $I$ a quasi-coherent ideal of `O_X` (so that $Y
= V(I)$ is a closed part of $X$), $U$ a variable open neighborhood of $Y$ in $X$, and $\hat{X}$ the formal completion of
$X$ along $Y$. For every ringed space $(Z, O_{Z})$, we denote by $P(Z)$ the category of invertible `O_Z`-Modules — in
other words, locally free of rank 1 — and by $\operatorname{Pic}(Z)$ the group of isomorphism classes of invertible
Modules on $Z$.

<!-- original page 100 -->

## 1. Comparison of Pic(X̂) and Pic(Y)

<!-- label: XI.1 -->

For every $n \in \mathbb{N}$, set $X_{n} = (Y, O_{X}/I^{n+1})$ and $P_{n} = I^{n+1}/I^{n+2}$. The sequence of sheaves of
abelian groups on $Y$

```text
0 ⟶ P_n ──u──→ O*_{X_{n+1}} ──v──→ O*_{X_n} ⟶ 1
```

<!-- label: eq:XI.1.1 -->

is exact. Let us be precise: the group structure on $P_{n}$ is the additive structure, $u(x) = 1 + x$ for every $x \in
P_{n}$, and $v$ is the homomorphism deduced from the injection $I^{n+2} \to I^{n+1}$. We see that $v$ is surjective by
remarking that, for every $y \in Y$, $O_{X_{n}, y}$ is a local ring, the quotient of $O_{X_{n+1}, y}$ by a nilpotent
ideal; the rest is equally trivial. From (1.1) we deduce an exact cohomology sequence:

```text
(∗)   H¹(Y, P_n) ──u¹──→ H¹(Y, O*_{X_{n+1}}) ──v¹──→ H¹(Y, O*_{X_n}) ──d──→ H²(Y, P_n).
```

<!-- label: eq:XI.1.star -->

On the other hand, for every $n \in \mathbb{N}$, one knows how to identify $\operatorname{Pic}(X_{n})$ with $H^{1}(Y,
O*_{X_{n}})$; moreover, if $E$ is an invertible $O_{X_{n+1}}$-Module corresponding to a cohomology class $c(E)$, the
cohomology class corresponding to the inverse image of $E$ on $X_{n}$ is equal to $v^{1}(c(E))$.

<!-- original page 101 -->

Whence the following proposition:

**Proposition.**

<!-- label: XI.1.1 -->

Retain the notations introduced above. Let $p \in \mathbb{N}$. The map $\operatorname{Pic}(\hat{X}) \to
\operatorname{Pic}(Y_{n})$:

1. is injective for $n \geqslant p$, if $H^{1}(Y, P_{n}) = 0$ for $n \geqslant p$;
1. is an isomorphism for $n \geqslant p$, if $H^{i}(Y, P_{n}) = 0$ for $n \geqslant p$ and $i = 1, 2$.

Of course, the exact sequence (∗) contains more information than the proposition above. The reader will have noticed
that we have said nothing about the functor $P(\hat{X}) \to P(Y)$. Given two invertible $O_{\hat{X}}$-Modules $E$, $F$,
the sheaf $H = \operatorname{Hom}(E, F)$ is also invertible. If we indicate reduction modulo $I^{n+1}$ by a subscript
$n$, we find an exact sequence:

```text
0 ⟶ H_0 ⊗ P_n ⟶ Hom(E_{n+1}, F_{n+1}) ⟶ Hom(E_n, F_n) ⟶ 0.
```

<!-- label: eq:XI.1.2 -->

Whence an exact cohomology sequence that we shall not write down and whose interpretation is evident; one may use this
remark to study the functor $P$.

## 2. Comparison of Pic(X) and Pic(X̂)

<!-- label: XI.2 -->

The reader will find in Exposé X, no. 2, the proof of what follows:

**Proposition.**

<!-- label: XI.2.1 -->

Suppose that $Lef(X, Y)$ holds; then for every open neighborhood $U$ of $Y$ in $X$, the functor

$$ P(U) \longrightarrow P(\hat{X}) $$

<!-- label: eq:XI.2.1 -->

is fully faithful, so that the map

$$ \operatorname{Pic}(U) \longrightarrow \operatorname{Pic}(\hat{X}) $$

<!-- label: eq:XI.2.2 -->

<!-- original page 102 -->

is injective. If $Leff(X, Y)$ holds, then the map (2.3) is an isomorphism:

```text
lim→_U Pic(U) ⟶ Pic(X̂).
```

<!-- label: eq:XI.2.3 -->

**Corollary.**

<!-- label: XI.2.2 -->

Suppose that $Lef(X, Y)$ holds and that $H^{1}(Y, P_{n}) = 0$ for every integer $n \geqslant p$; then for every open $U
\supset Y$, the maps

```text
Pic(X) ⟶ Pic(U) ⟶ Pic(Y_n)
```

are injective for $n \geqslant p$. If $Leff(X, Y)$ holds and if, moreover, $H^{i}(Y, P_{n}) = 0$ for every integer $n
\geqslant p$ and $i = 1, 2$, then the map

```text
lim→_U Pic(U) ⟶ Pic(Y_n)
```

is an isomorphism for $n \geqslant p$.

<!-- original page 103 -->

## 3. Comparison of P(X) and P(U)

<!-- label: XI.3 -->

A definition:

**Definition.** [^XI-3-star1]

<!-- label: XI.3.1 -->

Let $X$ be a prescheme and let $Z$ be a closed part of $X$. Set $U = X - Z$. We say that $X$ is *parafactorial at the
points of* $Z$ if, for every open set $V$ of $X$, the functor $P(V) \to P(V \cap U)$ is an equivalence of categories. We
also say that the pair $(X, Z)$ is *parafactorial*.

Recall that $P(Z)$ denotes the category of Modules locally free of rank 1 on $Z$.

**Definition.**

<!-- label: XI.3.2 -->

A noetherian local ring is said to be *parafactorial* if the pair $(\operatorname{Spec}(A), {r(A)})$ is parafactorial.

One proves the following proposition, which shows that the notion is "pointwise":

**Proposition.**

<!-- label: XI.3.3 -->

Suppose $X$ is locally noetherian. In order that the pair $(X, Z)$ be parafactorial, it is necessary and sufficient
that, for every $z \in Z$, the local ring $O_{X,z}$ be so.

Note that in "parafactorial" there is "fully faithful". One proves, as in Lemma 3.5 of Exposé X, the:

**Lemma.**

<!-- label: XI.3.4 -->

If $X$ is a locally noetherian prescheme and if $Z = X - U$ is a closed part of $X$, the following conditions are
equivalent:

1. for every open set $V$ of $X$, the functor $P(V) \to P(V \cap U)$ is fully faithful;
1. the homomorphism $O_{X} \to i_{*}(O_{U})$ is an isomorphism;
1. for every $z \in Z$, one has $prof(O_{X,z}) \geqslant 2$.

Thus "parafactorial" means that the conditions of 3.4 are satisfied and that, for every open set $V$ of $X$, the
homomorphism $\operatorname{Pic}(V) \to \operatorname{Pic}(V \cap U)$ is surjective. In particular, if $X$ is the
spectrum of a noetherian local ring, we find:

**Proposition.**

<!-- label: XI.3.5 -->

Let $A$ be a noetherian local ring; in order that it be parafactorial, it is necessary and sufficient that $prof A
\geqslant 2$ and $\operatorname{Pic}(X' - {x}) = 0$, where we have set $X' = \operatorname{Spec}(A)$ and $x$ is the
unique closed point of $X'$.

Note that a local ring of dimension $\leqslant 1$ is never parafactorial, since its depth is $\leqslant 1$. Hence
"factorial" does not imply "parafactorial"; however, the converse holds for noetherian local rings of dimension
$\geqslant 2$, as we shall see below.

<!-- original page 104 -->

**Lemma.**

<!-- label: XI.3.6 -->

Let $X$ be a locally noetherian prescheme and let $Z$ be a closed part of $X$. Let $f: X_{1} \to X$ be a faithfully flat
and quasi-compact morphism. Set $Z_{1} = f^{-1}(Z)$. If $(X_{1}, Z_{1})$ is parafactorial, then so is $(X, Z)$.

We first remark that, if $i: (X - Z) \to X$ denotes the canonical immersion of $U = X - Z$ into $X$, the formation of
the direct image by $i$ of a quasi-coherent `O_U`-Module commutes with the base change $f$, since the latter is flat. It
is therefore equivalent to assume the equivalent conditions of Lemma 3.5 for $(X, Z)$ or for $(X_{1}, Z_{1})$, since $f$
is a morphism of descent for the category of quasi-coherent sheaves. It remains to prove that, for every open set $V$ of
$X$, $\operatorname{Pic}(V) \to \operatorname{Pic}(V \cap U)$ is surjective. We make the base change $V \to X$, which
changes nothing (*sic*), and we are reduced to the case $V = X$. We then remark that, if $L$ is an invertible
`O_U`-Module and if $L$ admits a locally free prolongation, this prolongation is isomorphic to $i_{*}(L)$, because of
what has just been seen. It remains to prove that $i_{*}(L)$ is invertible. Using once more the fact that the direct
image by $i$ commutes with flat base change, and that "locally free of rank 1" is a property that descends by faithfully
flat and quasi-compact morphism, we are done.

**Corollary.**

<!-- label: XI.3.7 -->

Let $A$ be a noetherian local ring; if `Â` is parafactorial, so is $A$.

Do not believe that, if $A$ is parafactorial, so is `Â`.[^N.D.E-XI-1]

Before stating the principal theorem of this section, let us make the connection with the theory of divisors and the
notion of factorial ring.[^XI-3-star2]

Let $X$ be a noetherian and normal prescheme. Let $Z^{1}(X)$ be the free abelian group generated by the $x \in X$ such
that $\dim O_{X,x} = 1$. The local ring of such a point is a discrete valuation ring. We shall write $v_{x}$ for the
corresponding normalized valuation. Let $K(X)$ be the ring of rational functions on $X$ and let

$$ p: K(X)* \longrightarrow Z^{1}(X) $$

be the map that to every $f \in K(X)*$ associates the codimension-one cycle:

```text
(f) = Σ_{x ∈ X, dim O_{X,x} = 1} v_x(f) · x.
```

<!-- original page 105 -->

The image of $p$ is denoted $P(X)$, and its elements are called *principal divisors*.[^XI-3-star3] We set

$$ Cl(X) = Z^{1}(X)/P(X). $$

Let $Z'^{1}(X)$ be the subgroup of $Z^{1}(X)$ whose elements are the locally principal divisors. One knows that

$$ \operatorname{Pic}(X) \simeq Z'^{1}(X)/P(X), $$

and consequently $\operatorname{Pic}(X)$ is identified with a subgroup of $Cl(X)$.

Note that if $U$ is a dense open of $X$, then $K(X) \to K(U)$ is an isomorphism, and that if $codim(X - U, X) \geqslant
2$, i.e. if every $x \in X$ such that $\dim O_{X,x} \leqslant 1$ belongs to $U$, the homomorphism $Z^{1}(X) \to
Z^{1}(U)$, and consequently $Cl(X) \to Cl(U)$, is also an isomorphism. Finally, if every $x \in U$ is factorial — i.e.
$O_{X,x}$ is so — then $Z^{1}(U) = Z'^{1}(U)$, and so $\operatorname{Pic}(U) \simeq Cl(U)$.

**Proposition.**

<!-- label: XI.3.7.1 -->

Let $X$ be a noetherian and normal prescheme. Let $(U_{i})_{i \in I}$ be a family of open sets of $X$ such that:

1. the $U_{i}$ form a filter base;[^N.D.E-XI-2]
1. if one sets $Y_{i} = X - U_{i}$, then $codim(Y_{i}, X) \geqslant 2$ for every $i$;
1. if $x \in U_{i}$ for every $i \in I$, then $O_{X,x}$ is factorial.

Then one has an isomorphism:

```text
lim→_{i ∈ I} Pic(U_i) ──≅──→ Cl(X).
```

Note that b) implies that every $x \in X$ such that $\dim O_{X,x} \leqslant 1$ belongs to $U_{i}$ for every $i$. Hence
the $U_{i}$ are dense, and moreover the homomorphism $Z^{1}(U_{i}) \to Z^{1}(X)$ is an isomorphism, as is $K(U_{i}) \to
K(X)$. So $\operatorname{Pic}(U) \subset Cl(U_{i}) \simeq Cl(X)$. To prove what is desired, it therefore suffices to
show that every $D \in Z^{1}(X)$ belongs to $Z'^{1}(U_{i})$ for a suitable $i$. It suffices to do this for irreducible
positive "divisors". Let then $x \in X$ be such that $\dim O_{X,x} = 1$. It suffices to prove that there exists $i \in
I$ such that ${x}$ is locally principal at the points of $U_{i}$. Let $I$ be the largest ideal of definition of the
closed set ${x}$. The set of points in whose neighborhood $I$ is free is an open set $U$. Now $U \supset \bigcap_{i \in
I} U_{i}$ by c). If we set $Y = X - U$, then $Y \subset \bigcup_{i \in I} Y_{i}$ with $Y_{i} = X - U_{i}$; now $Y$ is
closed, so admits a finite number of generic points, so is contained in the union of finitely many $Y_{i}$, hence in
some $Y_{j}$ for a $j \in I$, because the $U_{i}$ form a filter base. Thus $U \supset U_{j}$. QED.

**Corollary.**

<!-- label: XI.3.8 -->

Let $X$ be a noetherian and normal prescheme and let $Y$ be a closed part of codimension $\geqslant 2$. Suppose that,
for every $p \in X - Y$, $O_{X,p}$ is factorial; then

```text
Pic(X − Y) ⟶ Cl(X − Y) ⟶ Cl(X)
```

are isomorphisms.

<!-- original page 106 -->

**Corollary.**

<!-- label: XI.3.9 -->

Let $A$ be a noetherian, normal local ring. Set $X' = \operatorname{Spec}(A)$ and $x = r(A)$. In order that $A$ be
factorial, it is necessary and sufficient that $\operatorname{Pic}(X' - {x}) = 0$ and that $p \in X' - {x}$ implies
$A_{p}$ factorial.

Indeed, in order that $A$ be factorial, it is necessary and sufficient that $Cl(X') = 0$.[^N.D.E-XI-3]

**Corollary.**

<!-- label: XI.3.10 -->

Let $A$ be a noetherian local ring of dimension $\geqslant 2$. Set $X' = \operatorname{Spec}(A)$ and let $x = r(A)$. Set
$X = X' - {x}$. The following conditions are equivalent:

1. $A$ is factorial;
1. a) for every $y \in X$, $O_{X,y}$ is factorial, and b) $A$ is parafactorial, i.e. $prof A \geqslant 2$ and
   $\operatorname{Pic}(X) = 0$.

<!-- original page 107 -->

Before proving this corollary, let us state the:

**Serre's criterion of normality.** [^XI-3-star4]

<!-- label: XI.3.11 -->

Let $A$ be a noetherian local ring. In order that $A$ be normal, it is necessary and sufficient that

1. for every prime ideal $p$ of $A$ such that $\dim A_{p} \leqslant 1$, $A_{p}$ be normal;
1. for every prime ideal $p$ of $A$ such that $\dim A_{p} \geqslant 2$, one have $prof A_{p} \geqslant 2$.

Let us prove 3.10.

(i) ⇒ (ii). Knowing that a localization of a factorial ring is factorial, we have (ii) a). Moreover $A$ is normal, so
$prof A \geqslant 2$, since $\dim A \geqslant 2$ (3.11 (ii)). Finally $A$ is parafactorial; indeed
$\operatorname{Pic}(X) \simeq Cl(X') = 0$ (cf. 3.9).

(ii) ⇒ (i). We first prove that $A$ is normal by applying Serre's criterion. Since $\dim A \geqslant 2$, condition (i)
of the criterion is among the hypotheses. Moreover, for every $p \in X$, $A_{p}$ is factorial, hence normal, hence of
depth $\geqslant 2$, at least if $\dim A_{p} \geqslant 2$. Finally $prof A \geqslant 2$ by (ii) b). It remains to apply
3.9.

Let us summarize the preceding:

**Proposition.**

<!-- label: XI.3.12 -->

Let $X$ be a locally noetherian prescheme and let $I$ be a quasi-coherent ideal of $X$. Set $Y = V(I)$. Let $p \in
\mathbb{N}$. Suppose that:

1. $Leff(X, Y)$ holds (Exposé X);
1. $H^{i}(X, I^{n+1}/I^{n+2}) = 0$ if $i = 1$ or `2` and if $n \geqslant p$;
1. for every open neighborhood $U$ of $Y$ in $X$ and every $x \in X - U$, the ring $O_{X,x}$ is parafactorial.

Then, for every $n \geqslant p$ and every open neighborhood $U$ of $Y$, the homomorphisms

```text
Pic(X) ⟶ Pic(U) ⟶ Pic(X_n)
```

(with the canonical commutative triangle) are isomorphisms.

One knows some parafactorial rings:

<!-- original page 108 -->

**Theorem.**

<!-- label: XI.3.13 -->

1. (Auslander–Buchsbaum)[^N.D.E-XI-4] A regular noetherian local ring is factorial (hence parafactorial if its dimension
   is $\geqslant 2$).
1. A noetherian local ring of dimension $\geqslant 4$ that is a complete intersection is parafactorial.

**Corollary** (Samuel conjecture)[^N.D.E-XI-5]**.**

<!-- label: XI.3.14 -->

A noetherian local ring $A$ that is a complete intersection and that is factorial in codimension $\geqslant 3$ (i.e.
$\dim A_{p} \leqslant 3$ implies that $A_{p}$ is factorial) is factorial.

*Proof of the corollary.* We argue by induction on the dimension of $A$. If $\dim A \leqslant 3$, then $A$ is factorial
by hypothesis. If $\dim A > 3$, by the induction hypothesis, and remarking that a localization of a complete
intersection is also a complete intersection, all localizations of $A$ other than $A$ itself are factorial. By Theorem
3.13 (ii), $A$ is parafactorial, hence factorial by 3.10.

*Proof of 3.13 (i)* (following Kaplansky).[^XI-3-star5]

Let $A$ be a regular noetherian local ring; set $\dim A = n$. If $n = 0$ or `1`, the result is known. Suppose $n
\geqslant 2$, and argue by induction on $n$: suppose $n \geqslant 2$ and the theorem proved for rings of dimension $<
n$. Set $X' = \operatorname{Spec}(A)$ and $X = X' - {x}$, where $x = r(A)$. The localizations of $A$ other than $A$ are
regular and of dimension $< n$, hence factorial. Moreover $prof A = \dim A \geqslant 2$. It therefore suffices to prove
that $\operatorname{Pic}(X) = 0$ (Cor. 3.10). Let then $L$ be an invertible `O_X`-Module; one knows that one can prolong
it to a coherent $O_{X'}$-Module $L'$. There exists a resolution of $L'$ by free $O_{X'}$-Modules:

$$ 0 \longleftarrow L' \longleftarrow L'_{1} \longleftarrow \cdots \longleftarrow L'_{n} \longleftarrow 0, $$

since the cohomological dimension of $A$ is finite. By restriction to $X$ one obtains a finite free resolution. It
therefore suffices to prove the following lemma:

<!-- original page 109 -->

**Lemma.**

<!-- label: XI.3.15 -->

Let $(X, O_{X})$ be a ringed space and let $L$ be a locally free `O_X`-Module that admits a finite resolution by free
modules of finite type. Then $det(L) \simeq O_{X}$.

Recall that one defines $det(L)$ as the maximal exterior power of $L$. In the case envisaged, $det(L) \simeq L$ since
$L$ is invertible, so the lemma allows us to conclude. Let us prove this lemma. Let

```text
0 ⟵ L_0 ⟵ L_1 ⟵ L_2 ⟵ ⋯ ⟵ L_n ⟵ 0
```

be the announced exact sequence, where $L_{0} = L$. Since everything is locally free, one has:

```text
⨂_{0 ⩽ i ⩽ n} (det(L_i))^{(−1)^i} ≃ O_X;
```

now all the $L_{i}$ for $i > 0$ are free, so their determinants are free as well, hence so is the determinant of $L_{0}
= L$. QED.

It remains to prove (ii) of the theorem. Beforehand, let us prove a lemma that will permit us to proceed by induction:

**Lemma.**

<!-- label: XI.3.16 -->

Let $A$ be a noetherian local ring that is a quotient of a regular ring. Let $t \in r(A)$ be an $A$-regular element.
Suppose that $A$ is complete for the $t$-adic topology. Set $X' = \operatorname{Spec}(A)$, $Y' = V(t) \simeq
\operatorname{Spec}(B)$, $B = A/tA$, $X = X' - {x}$, $Y = Y' - {x}$, $x = r(A)$. Suppose that:

1. for every $y \in X$ closed in $X$, one has $prof O_{X,y} \geqslant 2$,
1. $prof A/tA \geqslant 3$,

then the map $\operatorname{Pic}(X) \to \operatorname{Pic}(Y)$ is injective. In particular, if $B$ is parafactorial,
then so is $A$.

One knows that a) implies $Lef(X, Y)$ thanks to X 2.1. If we prove that $H^{1}(Y, P_{n}) = 0$ for every $n \geqslant 0$,
we shall know thanks to (2.2) that $\operatorname{Pic}(X) \to \operatorname{Pic}(Y)$ is injective. If, moreover, $B$ is
parafactorial, we shall know that $\operatorname{Pic}(Y) = 0$ (3.5), hence $\operatorname{Pic}(X) = 0$; now $prof(A)
\geqslant 3 + 1 \geqslant 2$ since $t$ is $A$-regular, so $A$ will be parafactorial by 3.5.[^TRANSLATOR-XI-1]

Let $I = (tA)^{\sim}$ be the $O_{X'}$-Module associated with the ideal `tA`. In no. 1, we set $P_{n} =
(I^{n+1}/I^{n+2})|Y$ for every $n \geqslant 0$. Now $t$ is $A$-regular, so $P_{n} \simeq O_{Y}$. It therefore remains to
prove that $H^{1}(Y, O_{Y}) = 0$. Now $Y = Y' - {x}$ is an open subset of $Y'$, so we have an exact sequence (I (27)):

```text
H¹(Y′, O_{Y′}) ⟶ H¹(Y, O_Y) ⟶ H²_x(Y′, O_{Y′}),
```

whose right-hand term is zero by virtue of hypothesis b), and whose left-hand term is zero because $Y'$ is affine. QED.

**Lemma.**

<!-- label: XI.3.17 -->

Retaining the hypotheses of 3.16, suppose moreover that:

1. (c) for every $y$ closed in $Y$, $prof O_{X,y} \geqslant 3$,
1. (d) $prof A/tA \geqslant 4$ (stronger than b),
1. (e) for every $y$ closed in $X$ with $y \in Y$, the ring $O_{X,y}$ is parafactorial.

Then the map $\operatorname{Pic}(X) \to \operatorname{Pic}(Y)$ is an isomorphism; in particular, in order that $A$ be
parafactorial, it is necessary and sufficient that $B$ be so.

One knows (X 2.1) that a) and c) imply $Leff(X, Y)$. Moreover, by the reasoning just made, d) implies that $H^{i}(Y,
P_{n}) = 0$ for every $n \geqslant 0$ and $i = 1$ or $i = 2$. Furthermore, for every open neighborhood $U$ of $Y$ in
$X$, the complement of $U$ in $X$ consists of a finite number of closed points. Thanks to e) and Theorem 3.12, we deduce
that $\operatorname{Pic}(X) \to \operatorname{Pic}(Y)$ is an isomorphism. On the other hand, $prof A \geqslant prof B
\geqslant 2$; by criterion 3.5, we deduce that $A$ is parafactorial if and only if $B$ is so.

Let us now prove 3.13 (ii). Let $R$ be a regular noetherian local ring. Let $(t_{1}, \cdots, t_{k})$ be an $R$-sequence.
Set $B = R/(t_{1}, \cdots, t_{k})$ and suppose $\dim B \geqslant 4$. We must prove that $B$ is parafactorial. We argue
by induction on $k$. If $k = 0$, then $B$ is regular, hence factorial by 3.13 (i), hence parafactorial by 3.10. Suppose
$k \geqslant 1$ and the theorem proved for $k' < k$. Set $A = R/(t_{1}, \cdots, t_{k-1})$, so $B = A/t_{k} A$. We may
suppose $B$ complete by 3.7. By the induction hypothesis, $A$ is parafactorial. Let us prove that we may apply Lemma
3.17. We have supposed $B$ complete, hence so is $A$, and therefore $A$ is complete for the $t_{k}$-adic topology. If $x
\in X$, and if $x$ is closed in $X$, then $A_{x}$ is a complete intersection of dimension $\geqslant 4$, with $k' < k$.
By the induction hypothesis, $A_{x}$ is parafactorial, and moreover of depth $\geqslant 4$. This gives a), c), and e).
Moreover $\dim A \geqslant 5$, whence d). QED.

**Theorem.**

<!-- label: XI.3.18 -->

Let $X$ be a locally noetherian prescheme and let $I$ be a coherent sheaf of ideals on $X$. Set $Y = V(I)$. Let $n$ be
an integer. Suppose that:

1. $Leff(X, Y)$ holds (cf. examples X 2.1 and X 2.2);
1. for every $p \geqslant n$, one has $H^{i}(Y, I^{p+1}/I^{p+2}) = 0$ for $i = 1$ and $i = 2$;
1. for every open $U \supset Y$ and every $x \in X - U$, the ring $O_{X,x}$ is regular of dimension $\geqslant 2$ or a
   complete intersection of dimension $\geqslant 4$.

Then, for every open $U \supset Y$ and every integer $p \geqslant n$, the homomorphisms

```text
Pic(X) ⟶ Pic(U) ⟶ Pic(Y_p)
```

are isomorphisms, where $Y_{p}$ denotes the prescheme $(Y, O_{X}/I^{p+1})$.

It suffices to combine 3.12 and 3.13.

<!--
LEDGER DELTA (Exposé XI):

| French | English | Note |
| --- | --- | --- |
| application au groupe de Picard | application to the Picard group | Title. |
| calqué sur | modeled on | Standard. Not "traced from"; the French sense is structural mimicry. |
| Module inversible | invertible Module | Capital preserved per source. |
| classe à isomorphisme près | isomorphism class | Standard. |
| complété formel `X̂` | formal completion `X̂` | Standard; hat preserved across OCR line breaks. |
| voisinage ouvert variable | variable open neighborhood | Preserves the "running variable" sense. |
| Pic(X̂) | Pic(X̂) | Notation preserved; the OCR repeatedly breaks the hat across a line ("Pic( b\nX)"). |
| `X_n = (Y, O_X/I^{n+1})` | `X_n = (Y, O_X/I^{n+1})` | Source uses both `X_n` and `Y_n` for this prescheme; preserved as-is. |
| `Y_n` (in Prop 1.1, Cor 2.2) | `Y_n` | Same prescheme as `X_n`; the source switches subscript carrier between §1 and §2. Y_p is explicitly redefined this way in 3.18. |
| `Lef(X, Y)`, `Leff(X, Y)` | `Lef(X, Y)`, `Leff(X, Y)` | Lefschetz / effective Lefschetz condition; defined in Exp. X. |
| pleinement fidèle | fully faithful | Standard. |
| parafactoriel aux points de Z | parafactorial at the points of Z | Per glossary. |
| couple parafactoriel | parafactorial pair | Per glossary. |
| anneau local parafactoriel | parafactorial local ring | Per glossary. |
| factoriel | factorial | Standard (unique factorization). |
| intersection complète | complete intersection | Standard. |
| factoriel en codimension `⩾ 3` | factorial in codimension `⩾ 3` | Standard. |
| critère de normalité de Serre | Serre's criterion of normality | Standard. |
| diviseur principal | principal divisor | Standard. |
| diviseur localement principal | locally principal divisor | EGA-style terminology. |
| diviseur de Cartier | Cartier divisor | Standard. |
| anneau régulier | regular ring | Standard. |
| anneau de valuation discrète | discrete valuation ring | Standard. |
| résolution libre finie | finite free resolution | Standard. |
| dimension cohomologique | cohomological dimension | Standard. |
| base de filtre | filter base | The N.D.E. glosses this as a "decreasing filtered family". |
| `A`-régulier (élément, suite) | `A`-regular (element, sequence) | Standard; cf. SGA 2 glossary on `M`-regular. |
| topologie `t`-adique | `t`-adic topology | Standard. |
| déterminant `det(L)` | determinant `det(L)` | Maximal exterior power; per the lemma. |
| sic | sic | Source-author marker; preserved. |
| C.Q.F.D. | QED | Per glossary. |
| théorème d'Auslander–Buchsbaum | Auslander–Buchsbaum theorem | Per glossary. |
| conjecture de Samuel | Samuel conjecture | Per glossary. |
| morphisme fidèlement plat et quasi-compact | faithfully flat and quasi-compact morphism | Standard. |
| morphisme de descente | morphism of descent | Standard. |
-->

[^XI-3-star1]: For a more detailed study of the notion of parafactoriality, and the proof of 3.3, cf. EGA IV 21.13,
    21.14.

[^N.D.E-XI-1]: *N.D.E.* For a precise study of the link between the factoriality of $A$ and that of its completion, see
    (Heitmann R., "Characterization of completions of unique factorization domains", *Trans. Amer. Math. Soc.* **337**
    (1993), no. 1, pp. 379–387).

[^XI-3-star2]: For the generalities that follow, cf. also EGA IV 21.

[^XI-3-star3]: In conformity with the terminology of EGA IV 21, we now prefer to reserve the name "divisors" for
    "locally principal divisors" or "Cartier divisors".

[^N.D.E-XI-2]: *N.D.E.* i.e. a decreasing filtered family.

[^N.D.E-XI-3]: *N.D.E.* See Bourbaki, *Algèbre commutative* VII.1.4, cor. to th. 2, and VII.3.2, th. 1.

[^XI-3-star4]: Cf. EGA IV 5.8.6.

[^N.D.E-XI-4]: *N.D.E.* To be compared with the following purity result, due to Gabber. Let $X$ be the spectrum of a
    regular local ring $A$ of dimension 3, $a$ an element of nonzero differential, i.e. $a \in m - m^{2}$, and $U$ the
    complement of $V(a)$. Then a vector bundle on $U$ is free (for a simple proof, see Swan R.G., "A simple proof of
    Gabber's theorem on projective modules over a localized local ring", *Proc. Amer. Math. Soc.* **103** (1988), no. 4,
    pp. 1025–1030). The rank-1 case is a particular case of Theorem 3.13. For purity results concerning vector bundles
    of arbitrary rank, in either the analytic or the algebraic setting, see (Gabber O., "On purity theorems for vector
    bundles", *Internat. Math. Res. Notices* (2002), no. 15, pp. 783–788).

[^N.D.E-XI-5]: *N.D.E.* For a proof in the same vein, but more elementary, see Call F. & Lyubeznik G., "A simple proof
    of Grothendieck's theorem on the parafactoriality of local rings", in *Commutative algebra: syzygies,
    multiplicities, and birational algebra* (South Hadley, MA, 1992), Contemp. Math., vol. 159, American Mathematical
    Society, Providence, RI, 1994, pp. 15–18.

[^XI-3-star5]: It is the proof reproduced in EGA IV 21.11.1.

[^TRANSLATOR-XI-1]:
    <!-- TRANSLATOR NOTE: The source literally has "prof(A) = 3 + 1 ⩾ 2 car t est A-régulier". The
    intended chain is: since `t ∈ r(A)` is `A`-regular and `A` is complete for the `t`-adic topology, `prof(A) ⩾
    prof(A/tA) + 1 = prof(B) + 1`; using b) `prof(B) ⩾ 3` gives `prof(A) ⩾ 4`, and only `⩾ 2` is needed for the
    application of 3.5. The translation preserves the "3 + 1" numeric form. -->
