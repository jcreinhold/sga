# Exposé VIII. Diagonalizable groups

<!-- label: III.VIII -->

*by A. Grothendieck*

> Version 1.1 of 8 November 2009: additions in 1.2, 1.4, 1.7, 3.1, 3.4, 4.5.1, 6.4, 6.8 — 1.5.1 and section 7 to be
> revised.[^VIII-0-0]

## 1. Biduality

<!-- original page 1 -->

Let $C$ be a category, which we identify, as is usual, with a full subcategory of
$\hat{C} = \operatorname{Hom}(C^{\circ}, (Ens))$ (cf. Exp. I). Let $I$ be a commutative group functor, i.e. an object of
`Ĉ` endowed with a commutative group structure (cf. I, 2.1).[^N.D.E-VIII-1] For every $X \in Ob(\hat{C})$, the object
$\operatorname{Hom}(X, I)$ carries a commutative group structure induced by that of $I$. For every group $G$ in `Ĉ`, let

$$
D(G) = \operatorname{Hom}_{gr}.(G, I)
$$

be the subobject of $\operatorname{Hom}(G, I)$ defined, for every $S \in Ob(C)$, by

$$
(*)    D(G)(S) = \operatorname{Hom}_{S-gr.}(G_{S}, I_{S}),
$$

<!-- label: eq:III.VIII.1.0-star -->

where $G_{S} = G \times S$ and $I_{S} = I \times S$ are considered as $S$-groups, i.e. groups in $\hat{C}/S$. Then
$D(G)$ is a `Ĉ`-subgroup of $\operatorname{Hom}(G, I)$. In this way one obtains a contravariant functor $D$ from the
category of `Ĉ`-groups to the category of commutative `Ĉ`-groups.

The right-hand side of `(*)` can also be interpreted as the subset of $\operatorname{Hom}(G \times S, I)$ consisting of
morphisms $G \times S \to I$ which are "multiplicative with respect to the first argument $G$". Moreover, the preceding
formulas remain valid more generally when $S$ is an arbitrary object of `Ĉ`, not necessarily coming from $C$.

If we now take for $S$ a group in `Ĉ`, which we shall denote $G'$, then in the left-hand side
$\operatorname{Hom}(G', D(G))$ of `(*)` we can single out the subset $\operatorname{Hom}_{gr}.(G', D(G))$ consisting of
morphisms that respect the group structures of $G'$ and $D(G)$.

<!-- original page 2 -->

It then corresponds to the subset of $\operatorname{Hom}(G \times G', I)$ consisting of morphisms that are
multiplicative with respect to the first and with respect to the second argument — which one may call *bilinear
morphisms from $G \times G'$ to $I$*, or *pairings of $G$ and $G'$ with values in $I$*. One thus finds

```text
(**)   Hom_gr.(G′, D(G)) ⥲ Hom_bil.(G × G′, I),
```

<!-- label: eq:III.VIII.1.0-doublestar -->

which is an isomorphism functorial in the pair $(G, G')$. Since the right-hand side is symmetric in $G$ and $G'$, one
deduces a functorial bijection

```text
(***)  Hom_gr.(G′, D(G)) ⥲ Hom_gr.(G, D(G′)).
```

<!-- label: eq:III.VIII.1.0-triplestar -->

In other words, "it amounts to the same thing" to give a group homomorphism $G' \to D(G)$ or a group homomorphism
$G \to D(G')$, both reducing in effect to the datum of a pairing $G \times G' \to I$.

Applying this to the case $G' = D(G)$ and to the identity homomorphism $G' \to D(G)$, one finds a canonical homomorphism

$$
(****) G \to D(D(G)).
$$

<!-- label: eq:III.VIII.1.0-quadstar -->

**Definition 1.0.**[^N.D.E-VIII-2] *We say that $G$ is* reflexive *(relative to $I$) if the preceding homomorphism is an
isomorphism. We note that this implies that $G$ is commutative.*

<!-- label: III.VIII.1.0 -->

One thus sees that:

**Proposition 1.0.1.** *The functor $D$ induces an anti-equivalence of the category of reflexive `Ĉ`-groups with
itself.*

<!-- label: III.VIII.1.0.1 -->

In particular, if $G$, $H$ are two reflexive groups, $D$ induces an isomorphism

```text
Hom_gr.(G, H) ⥲ Hom_gr.(D(H), D(G))
```

(it even suffices that $H$ be reflexive, as one sees from formula `(***)`).

<!-- original page 3 -->

**Definition 1.0.2.** *As usual, we shall then say that a $C$-group $G$ is* reflexive *if it is reflexive as a `Ĉ`-group
(without worrying whether $D(G)$ is representable or not).*

<!-- label: III.VIII.1.0.2 -->

One thus obtains, by $D$, an anti-equivalence of the category of reflexive $C$-groups $G$ such that $D(G)$ is
representable, with itself.

**Remark 1.0.3.** *To conclude these generalities, let us point out that the formation of duals $D(G)$ commutes with
base extension, which therefore transforms reflexive groups into reflexive groups.*

<!-- label: III.VIII.1.0.3 -->

We shall be interested henceforth in the case where $C = (Sch)/S$, the category of preschemes over $S$, and
$I = G_{m,S}$, the "multiplicative group over $S$" (cf. Exp. I). For every ordinary group $M$, we consider the $S$-group
`M_S`. One sees at once that for every prescheme in groups $J$ over $S$, there is a canonical isomorphism (functorial in
$M$ and $J$, and compatible with base extension):

```text
Hom_{S-gr.}(M_S, J) = Hom_gr.(M, J(S)).
```

Applying this to $J = I = G_{m,S}$ and to a variable $S'$ over $S$, one finds a functorial isomorphism:

$$
(1.0.4)    D(M_{S})(S') \xrightarrow{\sim} \operatorname{Hom}_{gr}.(M, G_{m}(S')).
$$

<!-- label: eq:III.VIII.1.0.4 -->

One thus recovers the functor already considered in I, 4.4, also denoted $D_{S}(M)$, which is representable for $M$
commutative, since

```text
D_S(M) = D(M_S) = Spec O_S(M),
```

where $O_{S}(M)$ denotes the algebra of the group $M$ with coefficients in `O_S`. (Let us note moreover, in the general
case, that $D(M)$ does not change if one replaces $M$ by its abelianization, so that no information is lost by assuming
$M$ commutative.)

**Definition 1.1.** *A prescheme in groups $G$ over $S$ is said to be* diagonalizable *if it is isomorphic to a scheme
of the form $D_{S}(M) = D(M_{S}) = \operatorname{Hom}_{S-gr.}(M_{S}, G_{m})$ for some suitable commutative group $M$.*

<!-- label: III.VIII.1.1 -->

<!-- original page 4 -->

*We say that $G$ is* locally diagonalizable *if every point of $S$ admits an open neighborhood $U$ such that $G|U$ is
diagonalizable.*

**Theorem 1.2.** *Let $\Gamma$ be a constant commutative group scheme over $S$, i.e. isomorphic to a group scheme of the
form `M_S`, where $M$ is an ordinary commutative group. Then $\Gamma$ is reflexive, i.e. the canonical homomorphism*

<!-- label: III.VIII.1.2 -->

$$
\Gamma \to D(D(\Gamma))
$$

*is an isomorphism.*[^N.D.E-VIII-3] *The diagonalizable group $D(M_{S})$ is therefore also reflexive.*

Taking the definitions into account, this follows from the following statement (which one will apply to a prescheme $S'$
over $S$):

**Corollary 1.3.** *Let $G = D(M_{S})$. Then every homomorphism of $S$-groups*

<!-- label: III.VIII.1.3 -->

$$
u : G \to G_{m,S}
$$

*is defined by a uniquely determined section of `M_S` over $S$, i.e. by a uniquely determined locally constant map from
$S$ to $M$.*

*Proof.* Since by definition

$$
G_{m,S} = GL(1)_{S} = \operatorname{Aut}_{O_{S}-mod.}(O_{S}),
$$

one sees that giving a group homomorphism $G \to G_{m,S}$ is equivalent to giving on `O_S` a structure of
$G$-`O_S`-module compatible with the natural `O_S`-module structure on `O_S` (cf. I, 4.7). By I, 4.7.3, this also
amounts to giving an $M$-grading on `O_S`, i.e. a decomposition of `O_S` as a direct sum of modules $L_{m}$ ($m \in M$).

<!-- original page 5 -->

Now it is well known that a direct factor of a locally free module of finite type is locally free of finite type;
therefore each $L_{m}$ is, in a neighborhood of each point of $S$, either zero or free of rank `1`, and in the latter
case identical to `O_S` in that neighborhood. Let $S_{m}$ be the open subset of $S$ consisting of the points where this
second alternative occurs. Expressing that `O_S` is the direct sum of the $L_{m}$, one sees that the union of the
$S_{m}$ is $S$, and that the $S_{m}$ are pairwise disjoint. Hence giving a group homomorphism $G \to G_{m,S}$ is
equivalent to giving a decomposition of $S$ as a union of pairwise disjoint open subsets $S_{m}$ ($m \in M$), i.e. to
giving a locally constant map from $S$ to $M$. This establishes 1.3, hence 1.2.

**Corollary 1.4.** *A diagonalizable group is reflexive; the same therefore holds for a locally diagonalizable group. If
$M$, $N$ are two ordinary commutative groups, the natural homomorphism*

<!-- label: III.VIII.1.4 -->

```text
Hom_{S-gr.}(M_S, N_S) → Hom_{S-gr.}(D(N_S), D(M_S))
```

*is bijective.*

[^N.D.E-VIII-4] The preceding isomorphism being compatible with base extension, one deduces an isomorphism of
$S$-functors in groups:

```text
(1)    Hom_{S-gr.}(M_S, N_S) ⥲ Hom_{S-gr.}(D(N_S), D(M_S)).
```

<!-- label: eq:III.VIII.1.4.1 -->

For every $S$-prescheme $T$, one has

```text
Hom_{S-gr.}(M_S, N_S)(T) = Hom_gr.(M, Γ(N_T/T)),
```

and, by I 1.8, $\Gamma(N_{T}/T)$ is the abelian group of locally constant maps $T \to N$. On the other hand, let
$\operatorname{Hom}_{gr}.(M, N)_{S}$ be the constant $S$-group associated with the ordinary abelian group
$\operatorname{Hom}_{gr}.(M, N)$. One has an evident homomorphism of $S$-functors in commutative groups:

```text
(2)    Hom_gr.(M, N)_S  -θ→  Hom_{S-gr.}(M_S, N_S),
```

<!-- label: eq:III.VIII.1.4.2 -->

which is always a monomorphism. Moreover, it is an isomorphism if $M$ is of finite type.[^N.D.E-VIII-5]

From the foregoing one deduces point (a) of the following corollary; point (b) follows from it by the descent results
"recalled" in 1.7.[^N.D.E-VIII-6]

<!-- original page 6 -->

**Corollary 1.5.** *a) Let $M$, $N$ be two ordinary commutative groups, with $M$ of finite type. Then one has an
isomorphism*

<!-- label: III.VIII.1.5 -->

```text
Hom_gr.(M, N)_S ⥲ Hom_{S-gr.}(D(N_S), D(M_S));
```

*consequently $\operatorname{Hom}_{S-gr.}(D(N_{S}), D(M_{S}))$ is representable.*

*b) More generally, if $G$, $H$ are locally diagonalizable, with $H$ of finite type, then
$\operatorname{Hom}_{S-gr.}(G, H)$ is representable.*

[^N.D.E-VIII-7] From 1.5 one concludes:

**Corollary 1.6.** *Under the conditions of 1.5, if $S$ is connected, one has*

<!-- label: III.VIII.1.6 -->

```text
Hom_{S-gr.}(D_S(N), D_S(M)) ⥲ Hom_gr.(M, N)
```

*and*

```text
Isom_{S-gr.}(D_S(N), D_S(M)) ⥲ Isom_gr.(M, N).
```

### 1.7. Descent of representability

<!-- label: III.VIII.1.7 -->

[^N.D.E-VIII-8] In this paragraph we "recall" some descent results that will be used frequently in what follows.

**Scholium 1.7.1.** *Let $S$ be a prescheme and $X$, $Y$, $T$ $S$-preschemes. If $(T_{i})$ is an open covering of $T$,
and if we set $T_{ij} = T_{i} \cap T_{j} = T_{i} \times_{T} T_{j}$, then, since giving a morphism of $T$-preschemes
$X_{T} \to Y_{T}$ is local on $T$, one has an exact sequence of sets:*

<!-- label: III.VIII.1.7.1 -->

```text
(1)    Hom_T(X_T, Y_T) → ∏_i Hom_{T_i}(X_{T_i}, Y_{T_i}) ⇒ ∏_{i,j} Hom_{T_{ij}}(X_{T_{ij}}, Y_{T_{ij}})
```

<!-- label: eq:III.VIII.1.7.1 -->

*i.e. $\operatorname{Hom}_{S}(X, Y)$ is a local $S$-functor, that is, a sheaf on $(Sch)/S$ endowed with the Zariski
topology.*

*More generally, by IV 4.5.13, $\operatorname{Hom}_{S}(X, Y)$ is a sheaf on $(Sch)/S$ for every topology coarser than
the canonical topology — for example, for the (fpqc) topology.*

*If $G$, $H$ are $S$-preschemes in groups, one deduces that the subfunctor $\operatorname{Hom}_{S-gr.}(X, Y)$ is a sheaf
for the (fpqc) topology (hence a fortiori a local functor).*

**Lemma 1.7.2.**[^N.D.E-VIII-9] *Let $F$ be a local $S$-functor.*

<!-- label: III.VIII.1.7.2 -->

*(i) Suppose there exists an open covering $(S_{i})$ of $S$ such that the restriction $F_{i} = F \times_{S} S_{i}$ of
$F$ to each $S_{i}$ is representable by an $S_{i}$-prescheme $X_{i}$. Then $F$ is representable by an $S$-prescheme
$X$.*

*(ii) Suppose $F$ is an (fpqc) sheaf and that there exists a faithfully flat quasi-compact morphism $S' \to S$ such that
the restriction $F' = F \times_{S} S'$ of $F$ is representable by an $S'$-prescheme $X'$. Then $X'$ is endowed with a
descent datum (cf. IV 2.1) relative to $S' \to S$.*

*If moreover this descent datum is effective (which is the case if $X'$ is affine over $S'$), then $F$ is representable
by an $S$-prescheme $X$.*

<!-- original page 7 -->

*Proof.* (i) It follows from the hypothesis that $X_{i} \times_{S} S_{j}$ and $X_{j} \times_{S} S_{i}$ both represent
the restriction of $F$ to $S_{ij} = S_{i} \times_{S} S_{j}$, hence, by the Yoneda lemma, there is a unique isomorphism
of $S_{ij}$-preschemes

```text
c_{ji} : X_i ×_S S_j ⥲ X_j ×_S S_i;
```

one then has isomorphisms of preschemes over $S_{ijk} = S_{i} \times_{S} S_{j} \times_{S} S_{k}$:

```text
       c_{ji} × id_{S_k}                       c_{kj} × id_{S_i}
X_i ×_S S_j ×_S S_k ─────→ X_j ×_S S_i ×_S S_k ≅ X_j ×_S S_k ×_S S_i ─────→ X_k ×_S S_j ×_S S_i

       c_{ki} × id_{S_j}
X_i ×_S S_k ×_S S_j ─────→ X_k ×_S S_i ×_S S_j
```

and since all these objects represent the restriction of $F$ to $S_{ijk}$, this diagram is commutative, i.e. the
$c_{ji}$ satisfy the usual cocycle relation $c_{kj} \circ c_{ji} = c_{ki}$.

It follows that the $X_{i}$ glue together into an $S$-prescheme $X$ such that $X \times_{S} S_{i} = X_{i}$ for every
$i$. For every $Y$ over $S_{i}$, one therefore has

```text
(*)    F(Y) = F_i(Y) = Hom_{S_i}(Y, X ×_S S_i) = Hom_S(Y, X) = h_X(Y).
```

Then, for $Y \to S$ arbitrary, the $Y_{i} = Y \times_{S} S_{i}$ form an open covering of $Y$; set
$Y_{ij} = Y_{i} \times_{Y} Y_{j} = Y \times_{S} S_{ij}$. Since $F$ (resp. $h_{X}$) is a local functor by hypothesis
(resp. because the Zariski topology is coarser than the canonical topology), $F(Y)$ and $h_{X}(Y)$ both identify, in
view of `(*)`, with the kernel of the double arrow:

```text
∏_i F(Y_i)  ⇒  ∏_{i,j} F(Y_{ij})

∏_i h_X(Y_i)  ⇒  ∏_{i,j} h_X(Y_{ij}).
```

This proves (i).

(ii) It follows from the hypothesis that $F''_{1} = F' \times_{S'} S''_{1}$ (where $S''_{1} = S'' = S' \times_{S} S'$ is
considered as $S'$-prescheme via the first projection) is represented by $X''_{1} = X' \times_{S'} S''_{1}$; similarly,
$F''_{2} = F' \times_{S'} S''_{2}$ is represented by $X''_{2} = X' \times_{S'} S''_{2}$. Now
$F''_{1} = F \times_{S} S'' = F''_{2}$, hence there exists a (unique) $S''$-isomorphism
$c : X''_{1} \xrightarrow{\sim} X''_{2}$. Then, denoting by $q_{i}$ (resp. $p_{ji}$) the projection of
$S''' = S' \times_{S} S' \times_{S} S'$ onto the $i$-th factor (resp. onto the factors $i$ and $j$),
$X'''_{i} = X' \times_{S'} S'''_{i}$ (where $S'''_{i} = S'''$ considered as $S'$-prescheme via $q_{i}$), and
$p^{*}_{ji}(c) : X'''_{i} \xrightarrow{\sim} X'''_{j}$ the isomorphism of $S'''$-preschemes deduced from $c$ by base
change, one obtains a diagram of isomorphisms of $S'''$-preschemes:

```text
              p_{21}^*(c)
        X‴_1 ─────────→ X‴_2
            ╲              │
  p_{31}^*(c) ╲             │ p_{32}^*(c)
              ╲             ↓
                X‴_3
```

<!-- original page 8 -->

and since all these objects represent the restriction of $F$ to $S'''$, this diagram is commutative, i.e. the usual
cocycle relation $p^{*}_{32}(c) \circ p^{*}_{21}(c) = p^{*}_{31}(c)$ holds, i.e. $c$ is a descent datum on $X'$ relative
to $S' \to S$ (cf. IV 2.1).

Suppose moreover that this descent datum is effective, i.e. that there exists an $S$-prescheme $X$ such that
$X' \simeq X \times_{S} S'$ (by SGA 1, VIII 2.1, this is the case if $X'$ is affine over $S'$[^N.D.E-VIII-10]). Then,
for every $Y \to S'$, one has

```text
(**)    F(Y) = F′(Y) = Hom_{S′}(Y, X ×_S S′) = Hom_S(Y, X) = h_X(Y).
```

Then, for $Y \to S$ arbitrary, set $Y' = Y \times_{S} S'$ and $Y'' = Y' \times_{Y} Y' \simeq Y \times_{S} S''$. Then
$Y' \to Y$, like $S' \to S$, is faithfully flat and quasi-compact, hence an $M$-effective epimorphism (where $M$ =
family of faithfully flat quasi-compact morphisms), i.e. the equivalence relation

```text
Y′ ×_Y Y′ ⇒ Y′
```

is $M$-effective and has quotient $Y$. Since $F$ (resp. $h_{X}$) is an (fpqc) sheaf by hypothesis (resp. because the
(fpqc) topology is coarser than the canonical topology), $F(Y)$ and $h_{X}(Y)$ both identify, in view of `(**)`, with
the kernel of the double arrow

```text
F(Y′) ⇒ F(Y′ ×_Y Y′)

h_X(Y′) ⇒ h_X(Y′ ×_Y Y′).
```

This proves (ii).

**Corollary 1.7.3.** *Let $F$ be an (fpqc) sheaf on $(Sch)/S$. Suppose there exists an open covering $(S_{i})$ of $S$
and, for each $i$, a faithfully flat quasi-compact morphism $S'_{i} \to S_{i}$ such that the restriction
$F'_{i} = F \times_{S} S'_{i}$ is representable by an $S'_{i}$-prescheme $X'_{i}$ affine over $S'_{i}$. Then $F$ is
representable by an $S$-prescheme $X$ affine over $S$ (such that $X \times_{S} S'_{i} = X'_{i}$ for every $i$).*

<!-- label: III.VIII.1.7.3 -->

*If moreover each $X'_{i} \to S'_{i}$ is a closed immersion (resp. a finite étale morphism), the same holds for
$X \to S$.*

The first assertion follows from 1.7.2. For the second, it suffices to verify that each morphism
$X \times_{S} S_{i} \to S_{i}$ is a closed immersion (resp. finite and étale), which follows from EGA IV₂, 2.7.1 (resp.
and IV₄, 17.7.3).

**Remark 1.7.4.** *Assertion 1.5 (b) follows, as announced, from 1.7.1 and 1.7.2 (i).*

<!-- label: III.VIII.1.7.4 -->

## 2. Schematic properties of diagonalizable groups

They are summarized in the following.

<!-- original page 8 -->

**Proposition 2.1.** *Let $S$ be a non-empty prescheme, $M$ an ordinary commutative group, $G = D(M_{S})$ the
diagonalizable $S$-group defined by $M$. Then:*

<!-- label: III.VIII.2.1 -->

*a) $G$ is faithfully flat over $S$, and affine over $S$ (a fortiori quasi-compact over $S$).*

*b) $M$ of finite type ⇔ $G$ of finite type over $S$ ⇔ $G$ of finite presentation over $S$.*

*c) $M$ finite ⇔ $G$ finite over $S$ ⇔ $G$ of finite type over $S$ and annihilated by an integer $n > 0$. Then
$deg(G/S) = Card(M)$.*

*c′) $M$ a torsion group ⇔ $G$ integral over $S$.*

*d) $M = 0$ ⇔ $G$ = unit $S$-group.*

*e) $M$ of finite type, and the order of its torsion subgroup is prime to the residue characteristics of $S$ ⇔ $G$ is
smooth over $S$.*

The verification of (a) to (d) is trivial, and is left to the reader. Let us prove (e). If $G$ is smooth over $S$, it is
locally of finite presentation over $S$, hence of finite presentation over $S$ since it is affine over $S$, hence $M$ is
of finite type. So we may already assume $M$ of finite type, hence $G$ of finite presentation over $S$.
Then[^N.D.E-VIII-11] $G$ is smooth over $S$ if and only if its geometric fibers are, which reduces us to the case where
$S$ is the spectrum of an algebraically closed field $k$. Writing $M = T \times L$, with $T$ the torsion subgroup and
$L$ free, $L \simeq \mathbb{Z}^{r}$, one has $D(M) = D(T) \times D(L)$, where $D(L) \simeq G^{r}_{m}$ is smooth over
$k$. So $G = D(M)$ is smooth over $k$ if and only if $D(T)$ is, which means, since $D(T)$ is finite over $k$ of degree
equal to the order $n$ of $T$, that $D(T)(k)$ has $n$ elements. Now $T$ is isomorphic to a sum of groups
$\mathbb{Z}/n_{i}\mathbb{Z}$, $n$ being the product of the $n_{i}$, so $D(T)$ is the product of the
$D(\mathbb{Z}/n_{i}\mathbb{Z}) = \mu_{n_{i}}$ (group scheme of $n_{i}$-th roots of unity), hence

```text
card(D(T)(k)) = ∏_i card μ_{n_i}(k),
```

where $card \mu_{n_{i}}(k)$ = (number of $n_{i}$-th roots of unity in $k$) $\leqslant n_{i}$, equality being attained if
and only if $n_{i}$ is prime to the characteristic $p$ of $k$. Hence one has $card(D(T)(k)) = n$ (where
$n = \prod_{i} n_{i}$) if and only if all the $n_{i}$ are prime to $p$, i.e. if and only if $n$ is prime to $p$. QED.

## 3. Exactness properties of the functor `D_S`

**Theorem 3.1.** *Let $S$ be a prescheme, and*

<!-- label: III.VIII.3.1 -->

```text
0 → M′ -u→ M -v→ M″ → 0
```

<!-- original page 8 -->

*an exact sequence of ordinary commutative groups. Consider the sequence of transposed homomorphisms:*

```text
0 → D_S(M″) -v^t→ D_S(M) -u^t→ D_S(M′) → 0.
```

*(i) $v^{t}$ induces an isomorphism of $D_{S}(M'')$ with the kernel of $u^{t}$, and $u^{t}$ is faithfully flat and
quasi-compact.*

*(ii)*[^N.D.E-VIII-12] *$D_{S}(M')$ represents the (fpqc) quotient sheaf $D_{S}(M)/D_{S}(M'')$.*

<!-- original page 9 -->

Let $M$ denote the family of faithfully flat quasi-compact morphisms. First, (ii) follows from (i) (cf. IV, 4.6.5.1).
Indeed, the equivalence relation in $D_{S}(M)$ defined by $u^{t}$ is the same as that defined by the subgroup
$Ker(u^{t}) = D_{S}(M'')$; since $u^{t} \in M$, this equivalence relation is $M$-effective (cf. IV, 3.3.2.1), and
therefore $D_{S}(M')$ represents the quotient sheaf for the (fpqc) topology (cf. IV, 4.6.5).

The first assertion of (i) is a trivial consequence of the definition of the functors $D_{S}(-)$; more generally, for
any exact sequence

$$
M' \to M \to M'' \to 0
$$

(without zero on the left), one will have a transposed exact sequence:

$$
0 \to D_{S}(M'') \to D_{S}(M) \to D_{S}(M').
$$

(This is valid more generally in the context of the beginning of §1.) On the other hand, since $D_{S}(M)$ and
$D_{S}(M')$ are affine over $S$, $u^{t}$ is necessarily an affine morphism, a fortiori quasi-compact (whatever the
homomorphism $u : M' \to M$). The second assertion of (i) will therefore follow from point (a) of the following:

**Corollary 3.2.** *Let $S$ be a non-empty prescheme, $u : M' \to M$ a homomorphism of ordinary commutative groups,
$u^{t} : G \to G'$ the transposed homomorphism. Then:*

<!-- label: III.VIII.3.2 -->

*a) For $u$ to be a monomorphism, it is necessary and sufficient that $u^{t}$ be faithfully flat.*

*b) For $u$ to be an epimorphism, it is necessary and sufficient that $u^{t}$ be a monomorphism (and then $u^{t}$ is
even a closed immersion).*

To prove (a), one notes that if $u$ is a monomorphism, then $O_{S}(M)$ is a module over $O_{S}(M')$ admitting a
non-empty basis (namely, the system of sections defined by any system of representatives of $M$ modulo $M'$), a fortiori
it is faithfully flat. Conversely, if this is the case, then $u^{t} : O_{S}(M') \to O_{S}(M)$ is injective, which (for
$S \neq \emptyset$) implies that $u : M' \to M$ is injective.

To prove (b), one notes that if $u$ is an epimorphism, then $O_{S}(M') \to O_{S}(M)$ is surjective, hence $u^{t}$ is a
closed immersion and a fortiori a monomorphism. Conversely, if this is the case, then $Ker u^{t}$ = unit group; now
setting $M'' = Coker u$, we have seen that $Ker u^{t} \simeq D_{S}(M'')$, hence by 2.1 (d) one has $M'' = 0$, hence $u$
is an epimorphism.

One concludes from 3.1 in the usual way:

**Corollary 3.3.** *Let $M' -u\to M -v\to M''$ be an exact sequence of ordinary commutative groups; consider the
transposed sequence*

<!-- label: III.VIII.3.3 -->

```text
G″ -v^t→ G -u^t→ G′.
```

*Then $v^{t}$ induces a faithfully flat quasi-compact morphism from $G''$ to $Ker u^{t}$, and the latter is a
diagonalizable group isomorphic to $D_{S}(v(M)) = D_{S}(Coker u)$.*

<!-- original page 10 -->

**Corollary 3.4.** *Let $S$ be a prescheme, $u : G \to H$ a homomorphism of $S$-preschemes in locally diagonalizable
groups, with $H$ of finite type over $S$. Set $G' = Ker u$. Then:*

<!-- label: III.VIII.3.4 -->

*a) $G'$ is locally diagonalizable; it is of finite type over $S$ if $G$ is.*

*b) The quotient $G/G'$ "exists"; more precisely, the equivalence relation defined by $G'$ in $G$ is $M$-effective
(where $M$ = set of faithfully flat quasi-compact morphisms, cf. IV, 3.4). Moreover, $G/G'$ is locally diagonalizable,
of finite type over $S$.*

*c) The homomorphism $u : G \to H$ factors uniquely as*

```text
G -v→ G/G′ -w→ H,
```

*where $v$ is the canonical homomorphism (so $v$ is faithfully flat and quasi-compact). Moreover $w$ is a closed
immersion, and a fortiori a monomorphism.*

*Finally, the quotient $H' = H/Im w = Coker w = Coker u$ exists; more precisely, the equivalence relation defined by
$G/G'$ in $H$ is $M$-effective, and $H'$ is of finite type over $S$.*

The first assertion of (c) is a consequence of (b), by definition of the quotient $G/G'$ (cf. IV,
3.2.3).[^N.D.E-VIII-13] Let us show that the (fpqc) quotient sheaf $\tilde{G}/\tilde{G}'$ is representable. This may be
verified locally on $S$, as may all the other assertions; we may therefore suppose $G$ and $H$ diagonalizable, of the
form $D_{S}(M)$ and $D_{S}(N)$.

Since $H$ is of finite type over $S$, $N$ is of finite type by 2.1 (b), hence by 1.5 $u$ is defined by a homomorphism
$u_{0} : N \to M$. Then, in virtue of 3.1 and 3.2, $G'$ is isomorphic to $D_{S}(Coker u_{0})$ and $\tilde{G}/\tilde{G}'$
is representable by $D_{S}(Im u_{0})$; moreover, considering the exact sequence

```text
0 → Ker u_0 → N -w_0→ Im u_0 → 0,
```

one obtains that $w$ is a closed immersion, and that the quotient $H' = H/Im w$ is $D_{S}(Ker u_{0})$; the latter is of
finite type over $S$ since $N$, and hence $Ker u_{0}$, is of finite type.

**Remarks.** The existence-of-quotients result 3.4 will be substantially generalized in §5.

On the other hand, one will note that in the present § and the preceding one, the hypothesis $S \neq \emptyset$ was used
only to ensure the validity of certain converses, enabling one to deduce from certain hypotheses on diagonalizable
$S$-groups properties of the corresponding ordinary groups. The "direct"-sense results are valid without restriction on
$S$, and the proofs given here apply in the general case.

**Corollary 3.5.** *Let $G$ be a diagonalizable group prescheme over $S$, and let $n$ be an integer $\neq 0$. Then the
subgroup ${}_{nG}$ of $G$, kernel of the homomorphism $n \cdot id_{G} : G \to G$, is integral over $S$, and finite over
$S$ if $G$ is of finite type over $S$.*

<!-- label: III.VIII.3.5 -->

<!-- original page 11 -->

Indeed, if $G = D_{S}(M)$, then ${}_{nG} = D_{S}(M/nM)$ by 3.1, and one concludes by 2.1 (b), (c), (c′).

## 4. Torsors under a diagonalizable group

Let $S$ be a prescheme, and $G = D_{S}(M)$ a diagonalizable group over $S$. We propose to determine the $G$-torsors (or
principal homogeneous $G$-bundles) on $S$, in the sense of the "faithfully flat quasi-compact topology" (cf. Exp. IV,
5.1). Recall that a prescheme $P$ over $S$ with operator group $G$ is called a *torsor* or *principal homogeneous* if
every point of $S$ admits an open neighborhood $U$ and a faithfully flat quasi-compact morphism $S' \to U$ such that
$P' = P \times_{S} S'$ is, as a bundle with operators, isomorphic to $G' = G \times_{S} S'$ (acting on itself by right
translations). Since $G$ is affine over $S$, it follows from SGA 1, VIII 5.6 that $P$ is necessarily affine over $S$.
Note also that since $G$ is itself faithfully flat and quasi-compact over $S$, $P$ is principal homogeneous under $G$ if
and only if it is "formally principal homogeneous", and if moreover it is faithfully flat and quasi-compact over $S$
(cf. IV, 5.1.6).

Recall on the other hand (Exp. I, 4.7.3) that giving an $S$-prescheme $P$ affine over $S$ with operator group
$G = D_{S}(M)$ amounts to giving a quasi-coherent commutative $M$-graded algebra on $S$, i.e. a quasi-coherent algebra
$\mathcal{A}$ on $S$ endowed with a direct sum decomposition (as a module):

```text
𝓐 = ⨁_{m ∈ M} 𝓐_m,
```

with

```text
𝓐_m · 𝓐_{m′} ⊆ 𝓐_{m+m′}    for m, m′ ∈ M.
```

This said, the answer to the problem posed above is given by:

**Proposition 4.1.** *For the prescheme $P$ with operator group $G = D_{S}(M)$, defined by the $M$-graded algebra
$\mathcal{A}$, to be a principal homogeneous bundle under $G$, it is necessary and sufficient that $\mathcal{A}$ satisfy
the following conditions:*

<!-- label: III.VIII.4.1 -->

*a) For every $m \in M$, $\mathcal{A}_{m}$ is an invertible module on $S$.*

*b) For $m, m' \in M$, the homomorphism*

```text
𝓐_m ⊗_{O_S} 𝓐_{m′} → 𝓐_{m+m′}
```

*induced by the multiplication in $\mathcal{A}$, is an isomorphism.*

<!-- original page 12 -->

The necessity of the conditions is immediate by descent, since they are satisfied in the case where $P$ is the trivial
principal homogeneous bundle, i.e. $\mathcal{A} = O_{S}(M)$. For the sufficiency, one notes that (a) already implies
that $P$ is faithfully flat over $S$, it is in any case quasi-compact over $S$ (being affine over $S$), so it remains to
verify that it is formally principal homogeneous under $G$, i.e. that the well-known homomorphism

```text
P ×_S G → P ×_S P
```

is an isomorphism. Now on affine algebras, this homomorphism is given explicitly as the homomorphism

```text
𝓐 ⊗ 𝓐 → 𝓐(M) = 𝓐 ⊗ O_S(M)
```

which in bidegree $(m, n)$ (where $m, n \in M$) is given by

```text
x_m ⊗ y_n ↦ x_m y_n ⊗ e_n.
```

From the standpoint of degrees, this homomorphism is compatible with the homomorphism $M \times M \to M \times M$ given
by

```text
(m, n) ↦ (m + n, n),
```

which is an isomorphism. This shows that (b) expresses precisely (independently of (a)) that $P$ is formally principal
homogeneous, and establishes 4.1.

Note also that one obtains, by faithfully flat descent:

**Corollary 4.2.** *The conditions of 4.1 imply that the homomorphism*

<!-- label: III.VIII.4.2 -->

$$
O_{S} \to \mathcal{A}_{0}
$$

*is an isomorphism.*

If for example $M = \mathbb{Z}$, then under the conditions of 4.1 one sees that $\mathcal{A}$ is essentially known when
one knows $\mathcal{A}_{1} = \mathcal{L}$, namely

```text
𝓐 ≃ ⨁_{n ∈ ℤ} 𝓛^{⊗n}
```

(isomorphism of graded algebras). One thereby recovers the well-known result:

**Corollary 4.3.** *There is an equivalence between the category of principal homogeneous bundles $P$ on $S$ with group
$G_{m,S}$, and the category of invertible modules $\mathcal{L}$ on $S$ (taking as morphisms, for the definition of each
category, the isomorphisms of the structures in play). One obtains two quasi-inverse functors by associating with each
$P$ the degree-`1` component of its $\mathbb{Z}$-graded affine algebra, and with each $\mathcal{L}$ the spectrum of the
$\mathbb{Z}$-graded algebra $\bigoplus_{n \in \mathbb{Z}} \mathcal{L}^{\otimes n}$.*

<!-- label: III.VIII.4.3 -->

In particular:

**Corollary 4.4.** *The group of classes of principal homogeneous bundles on $S$ with group $G_{m,S}$ is isomorphic to
the group $\operatorname{Pic}(S)$ of classes of invertible modules on $S$, i.e. to $H^{1}(S, O^{\times}_{S})$.*

<!-- label: III.VIII.4.4 -->

Taking into account that $G_{m,S}$ is the scheme of automorphisms of the module `O_S`, one sees that 4.4 is equivalent
to the following statement, which is one of the variants of Hilbert's "Theorem 90":

**Corollary 4.5.** *Every principal homogeneous bundle on $S$ with group $G_{m}$ is locally trivial (in the sense of the
Zariski topology).*

<!-- label: III.VIII.4.5 -->

**Remark 4.5.1.** *One will note that the preceding statement is no longer true in general for a group such as
$\mu_{n}$, or for a "twisted form" of $G_{m}$; for example, the unique twisted form of $G_{m}$ over the field
$\mathbb{R}$ of reals gives a group of `1`-cohomology equal to $\mathbb{Z}/2\mathbb{Z}$.*

<!-- label: III.VIII.4.5.1 -->

<!-- original page 13 -->

[^N.D.E-VIII-14] Indeed, let $S^{1}$ be the kernel of the norm morphism
$N : \prod_{\mathbb{C}/\mathbb{R}} G_{m,\mathbb{C}} \to G_{m,\mathbb{R}}$; this is a $\mathbb{C}/\mathbb{R}$-twisted
form of $G_{m,\mathbb{R}}$. The equation $N(z) = -1$ in $\prod_{\mathbb{C}/\mathbb{R}}(G_{m,\mathbb{C}})$ defines an
$S^{1}$-torsor $X$ over $\operatorname{Spec}(\mathbb{R})$, locally trivial for the étale topology, but not trivial since
$X(\mathbb{R}) = \emptyset$. Let us show that $H^{1}_{\acute{e}}t(\mathbb{R}, S^{1}) \cong \mathbb{Z}/2\mathbb{Z}$. One
has an exact sequence of smooth commutative $\mathbb{R}$-group schemes:

```text
1 → S¹ → ∏_{ℂ/ℝ} G_{m,ℂ} → G_{m,ℝ} → 1
```

which gives rise to a long exact sequence of étale cohomology (or of Galois cohomology):

```text
0 → S¹(ℝ) → ℂ^× -N→ ℝ^× → H¹_ét(ℝ, S¹) → H¹_ét(ℝ, ∏_{ℂ/ℝ} G_{m,ℂ}) → ⋯
```

Now (see for example XXIV, 8.4),
$H^{1}_{\acute{e}}t(\mathbb{R}, \prod_{\mathbb{C}/\mathbb{R}} G_{m,\mathbb{C}}) \simeq H^{1}_{\acute{e}}t(\mathbb{C}, G_{m,\mathbb{C}})$,
and the latter is zero by 4.5 (or, here, because $\mathbb{C}$ is algebraically closed). One thus obtains an isomorphism
$H^{1}_{\acute{e}}t(\mathbb{R}, S^{1}) \simeq \mathbb{R}^{\times}/N(\mathbb{C}^{\times}) \simeq {\pm 1}$.

We shall need in the following § the following result:

**Proposition 4.6.** *Under the conditions of 4.1, conditions (a) and (b) are equivalent to the following conditions:*

<!-- label: III.VIII.4.6 -->

*a′) $O_{S} \to \mathcal{A}_{0}$ is an isomorphism.*

*b′) For every $m$ in $M$ (it suffices: in a system of generators of $M$), one has*

$$
\mathcal{A}_{m} \cdot \mathcal{A}_{-m} = \mathcal{A}_{0}.
$$

The necessity being evident, taking 4.2 into account,[^N.D.E-VIII-15] we shall reduce to proving:

**Corollary 4.7.** *Let $A = \bigoplus_{n \in \mathbb{Z}} A_{n}$ be a $\mathbb{Z}$-graded ring such that*

<!-- label: III.VIII.4.7 -->

$$
A_{1} \cdot A_{-1} = A_{0}.
$$

*Then the $A_{n}$ are invertible `A_0`-modules, and for $n, n' \in \mathbb{Z}$, the homomorphism*

```text
A_n ⊗_{A_0} A_{n′} → A_{n+n′}
```

*induced by the multiplication in $A$, is an isomorphism.*

By hypothesis, there exist $f_{i} \in A_{1}$, $g_{i} \in A_{-1}$, such that

$$
(*)    \sum_{i} f_{i} g_{i} = 1.
$$

As the conclusion to be established is local on $\operatorname{Spec}(A_{0})$,[^N.D.E-VIII-16] and as, by `(*)`,
$\operatorname{Spec}(A_{0})$ is covered by the affine opens $D(f_{i} g_{i})$, one is reduced to the case where there
exists an element $f \in A_{1}$ invertible in $A$. Then for every $n \in \mathbb{Z}$, $f^{n}$ is an element of $A_{n}$
invertible in $A$, hence defines an isomorphism $h \mapsto f^{n} h$ from `A_0` onto $A_{n}$. Moreover,

<!-- original page 14 -->

this shows that one obtains an isomorphism $A_{0}[t, t^{-1}] \to A$ of graded `A_0`-algebras by sending $t$ to $f$,
which completes the proof of 4.7.

Then, under the conditions of 4.6, 4.7 already implies that the $\mathcal{A}_{m}$ ($m \in M$) are invertible. To prove
condition 4.1 (b), one may therefore suppose that $\mathcal{A}_{m}$ and $\mathcal{A}_{m'}$ admit bases $f_{m}$ and
$f_{m'}$, having inverses $f^{-1}_{m} \in \Gamma(\mathcal{A}_{-m})$ and $f^{-1}_{m'} \in \Gamma(\mathcal{A}_{-m'})$.
Then the product by $f^{-1}_{m} f^{-1}_{m'} \in \Gamma(\mathcal{A}_{-m-m'})$ defines a homomorphism
$\mathcal{A}_{m+m'} \to \mathcal{A}_{0} \simeq O_{S}$, sending the image of $f_{m} \otimes f_{m'}$ to the section `1` of
`O_S`. In the diagram

```text
                     w
                   ──────────────────────
                 ↗                       ↘
𝓐_m ⊗ 𝓐_{m′}  ─u→  𝓐_{m+m′}  ─v→  𝓐_0 ≃ O_S
```

$w$ and $v$ are therefore epimorphisms of invertible sheaves, hence isomorphisms, hence $u$ is an isomorphism. QED.

## 5. Quotient of an affine scheme by a diagonalizable group acting freely

<!-- original page 15 -->

[^N.D.E-VIII-17] We denote by $M$ the set of faithfully flat quasi-compact morphisms, and we recall that torsors are
considered in the sense of the (fpqc) topology.

**Theorem 5.1.** *Let $S$ be a prescheme, $M$ an ordinary commutative group, $G = D_{S}(M)$ the diagonalizable group
over $S$ defined by it, $P$ an $S$-prescheme affine over $S$ on which $G$ acts freely on the right.*

<!-- label: III.VIII.5.1 -->

*Then the equivalence relation defined by $G$ in $P$ is $M$-effective (cf. IV, 3.4), i.e. the quotient $X = P/G$ exists
and $P$ is a torsor over $X$ with group $G_{X} = D_{X}(M)$. Moreover, $P/G$ is affine over $S$; more precisely, if $P$
is defined by the $M$-graded algebra $\mathcal{A}$, then $P/G$ is isomorphic to $\operatorname{Spec}(\mathcal{A}_{0})$,
where $\mathcal{A}_{0} = \mathcal{A}^{G}$ is the degree-`0` component of $\mathcal{A}$.*

*Proof.* Set $X = \operatorname{Spec}(\mathcal{A}_{0})$. Then one has a natural morphism $P \to X$, deduced from
$\mathcal{A}_{0} \to \mathcal{A}$, which is invariant under the action of $G$. In this way, $P$ becomes an
$X$-prescheme, affine over $X$, with operator group $G_{X} = D_{X}(M)$, and the hypothesis that $G$ acts freely on $P/S$
implies that `G_X` acts freely on $P/X$. Everything reduces to showing that $P$ is a principal homogeneous bundle under
`G_X`, using the fact that $\mathcal{B}_{0} = O_{X}$, where $\mathcal{B}$ is the $M$-graded algebra on $X$ defining
$P/X$. We may then suppose $X = S$ and $S$ affine, so $P$ is affine, given by an $M$-graded ring $A$ whose homogeneous
part of degree $m$ will be denoted $A_{m}$, so that $S = \operatorname{Spec}(A_{0})$. Taking 4.6 into account, it
remains to verify that one has:

```text
(*)    A_m · A_{−m} = A_0    for every m ∈ M.
```

One observes moreover by a direct computation that `(*)` is equivalent to saying that
$P \times_{S} G \to P \times_{S} P$ is a closed immersion, and not only a monomorphism (under the hypothesis that $G$
acts freely), i.e. that the homomorphism on affine rings

<!-- original page 16 -->

```text
θ : A ⊗_{A_0} A → A(M)
```

is surjective[^N.D.E-VIII-18]. This gives 5.1 when one supposes that the equivalence relation defined by $G$ in $P$ is
closed. We shall, however, show that this hypothesis is already a consequence of the fact that $G$ acts freely (which is
moreover implicitly contained in Theorem 5.1, since $G \times_{S} P$ must be isomorphic to $P \times_{X} P$, which is
closed in $P \times_{S} P$ since $X$ is affine over $S$ hence separated over $S$).

Let $R = P \times_{S} G$. The hypothesis that $G$ acts freely, i.e. that $R \to P \times_{S} P$ is a monomorphism, can
be written as saying that the diagonal morphism

```text
R → R ×_{(P ×_S P)} R = R₀
```

is an isomorphism. One has $R = \operatorname{Spec}(A(M))$ and

$$
R_{0} = \operatorname{Spec}(A(M \times M)/K)
$$

[^N.D.E-VIII-19] where $K$ is the ideal generated by the elements of the form

```text
x_m(e_{m,0} − e_{0,m}),    with m ∈ M, x_m ∈ A_m;
```

let $\phi : A(M \times M) \to A(M)$ be the surjective ring homomorphism defined by

```text
x e_{m,n} ↦ x e_{m+n}    (m, n ∈ M, x ∈ A)
```

(where the $e_{m}$, resp. $e_{m,n} = e_{m} \otimes e_{n}$, are the elements of the canonical basis of $A(M)$, resp.
$A(M \times M)$). Then the diagonal morphism $R \to R_{0}$ corresponds to the homomorphism

```text
φ̄ : A(M × M)/K → A(M)
```

obtained by passing to the quotient by $K$. Now the kernel of $\phi$ is the ideal $K'$ generated by the

$$
d_{m} = e_{m,0} - e_{0,m}.
$$

One has $K \subseteq K'$, and the hypothesis that $G$ acts freely on $P$, i.e. that $\bar{\phi}$ is an isomorphism, is
equivalent to the equality $K' = K$, which is expressed by the relations

```text
(**)   d_m ∈ K = ∑_p A(M × M) A_p d_p,    for every m ∈ M.
```

Using the natural tri-grading of $A(M \times M)$, and the fact that the first degree of $d_{m}$ is zero, this means that
one can write $d_{m}$ as a sum of elements of the form

```text
f e_{r,s} (e_{p,0} − e_{0,p})    with f ∈ A_{−p} · A_p,
```

and using the fact that the total degree of $d_{m}$ is $m$, one can restrict to terms such that

```text
r + s + p = m.
```

<!-- original page 16 -->

Hence one must have, for every $m \in M$, an expression:

```text
(***)   { d_m = e_{m,0} − e_{0,m} = ∑_{r,s} λ_{r,s}(e_{m−s,s} − e_{r,m−r})
         with λ_{r,s} ∈ J_p = A_p · A_{−p} ⊆ A_0, p = m − (r + s).
```

One must conclude the relation `(*)`, i.e. the relations

```text
(****)   J_n = A_0    for every n ∈ M.
```

Now for this, it suffices to establish the same relation modulo every maximal ideal of `A_0`. As the hypotheses made are
invariant under such a reduction, one may already suppose that `A_0` is a field.

**Lemma 5.2.** *Under the preceding conditions (with `A_0` a field), if $M \neq 0$, there exists a $p \in M - {0}$ such
that $J_{p} = A_{0}$.*

<!-- label: III.VIII.5.2 -->

Indeed, if this were not so, the sum in the right-hand side of `(***)` would be zero for every $m \in M$, which is
absurd.

<!-- original page 18 -->

**Corollary 5.3.** *Under the preceding conditions, but without supposing any longer that `A_0` is a field, there exist
finitely many elements $p_{i} \in M - {0}$ such that $\sum_{i} J_{p_{i}} = A_{0}$.*

<!-- label: III.VIII.5.3 -->

Indeed, one applies the result 5.2 to the situations deduced from $A/A_{0}$ by reduction modulo the maximal ideals of
`A_0`.[^N.D.E-VIII-20]

**Corollary 5.4.** *Suppose again that `A_0` is a field. Then for every subgroup $N$ of $M$ such that $N \neq M$, there
exists a $p \in M - N$ such that $J_{p} = A_{0}$.*

<!-- label: III.VIII.5.4 -->

Indeed, let $M' = M/N$, and consider the $M'$-graded ring $A'$, whose underlying ring is $A$, and whose grading is given
by

```text
A′_{m′} = ⨁_{m ∈ h^{−1}(m′)} A_m,
```

where $h : M \to M' = M/N$ is the canonical homomorphism. Geometrically, this construction amounts to considering the
subgroup $G' = D_{S}(M')$ of $G$, and the structure on $P$ of scheme with operator group $G'$ induced by the action of
$G$. It is then evident that $G'$ acts freely on $P'$, i.e. the pair $(M', A')$ satisfies the hypotheses of 5.3. One
thus obtains

```text
1 = ∑_i f_i g_i    with f_i ∈ A′_{m′_i}, g_i ∈ A′_{−m′_i} and m′_i ∈ M′ − {0},
```

whence at once the conclusion 5.4 by taking the components of the right-hand side along `A_0`, and using that `A_0` is a
field.

Let us now note that

```text
J_p · J_q ⊆ J_{p+q}    and J_p = J_{−p},
```

<!-- original page 17 -->

so if $N$ denotes the set of $m \in M$ such that $J_{p} = A_{0}$, one sees that $N$ is a subgroup of $M$. Using 5.4 one
sees that it is equal to $M$. This completes the proof of Theorem 5.1.

As we have pointed out in the course of the proof, Theorem 5.1 implies:

**Corollary 5.5.** *Under the conditions of 5.1, the graph morphism*

<!-- label: III.VIII.5.5 -->

```text
P ×_S G → P ×_S P
```

*is a closed immersion.*

One concludes at once:

**Corollary 5.6.** *Let $\sigma$ be a section of $P$ over $S$. Then the morphism $g \mapsto \sigma \cdot g$ from $G$ to
$P$ defined by $\sigma$ is a closed immersion.*

<!-- label: III.VIII.5.6 -->

**Corollary 5.7.** *Let $G$, $H$ be two $S$-groups, with $G$ diagonalizable, $H$ affine over $S$, and let $u : G \to H$
be a homomorphism of $S$-groups that is a monomorphism. Then $u$ is a closed immersion, $H/G = X$ exists and $H$ is a
principal homogeneous bundle over $X$ with group `G_X`; finally, $X$ is affine over $S$.*

<!-- label: III.VIII.5.7 -->

**Corollary 5.8.** *Under the conditions of 5.1, if $P$ is of finite type (resp. of finite presentation) over $S$, the
same holds for $X = P/G$.*

<!-- label: III.VIII.5.8 -->

Indeed, it follows from the hypothesis that the fibers of `G_X` are of finite type, hence `G_X` is of finite
presentation over $X$ by 2.1 (b), hence $P$ being a torsor under `G_X` is of finite presentation over
$X$[^N.D.E-VIII-21]. Since it is also faithfully flat over $X$, our conclusion then follows from Exp. V, Prop. 9.1.

## 6. Essentially free morphisms, and representability of certain functors of the form $\prod_{Y/S} Z/Y$[^VIII-6-star]

<!-- original page 20 -->

**Definition 6.1.** *Let $f : X \to S$ be a morphism of preschemes. We say that $f$ is* essentially free\*, or also that
$X$ is\* essentially free over $S$*, if one can find a covering of $S$ by affine opens $S_{i}$, for each $i$ an
$S_{i}$-prescheme $S'_{i}$ affine and faithfully flat over $S_{i}$, and a covering $(X'_{ij})_{j}$ of
$X'_{i} = X \times_{S} S'_{i}$ by affine opens $X'_{ij}$, such that for every $(i, j)$, the ring of $X'_{ij}$ is a free
module over the ring of $S'_{i}$.*[^N.D.E-VIII-22]

<!-- label: III.VIII.6.1 -->

**Proposition 6.2.** *a) If $X$ is essentially free over $S$, it is flat over $S$, the converse being true if $S$ is
Artinian.*

<!-- label: III.VIII.6.2 -->

*b) If $S$ is the spectrum of a field, every $S$-prescheme is essentially free over $S$.*

*c) If $X$ is essentially free over $S$, and if $S' \to S$ is a base change morphism, then $X' = X \times_{S} S'$ is
essentially free over $S'$. The converse is true if $S' \to S$ is faithfully flat and quasi-compact.*

The proof is immediate, using for the converse in (a) the fact that a flat module over an Artinian local ring is
free.[^N.D.E-VIII-23]

**Proposition 6.3.** *Let $H$ be an $S$-prescheme in groups that is diagonalizable (more generally, that becomes
diagonalizable by suitable faithfully flat quasi-compact extension of every affine open of $S$, i.e. $H$ is "of
multiplicative type", cf. IX 1.1). Then $H$ is essentially free over $S$.*

<!-- label: III.VIII.6.3 -->

Indeed, if $H$ is diagonalizable, it is affine over $S$ and defined by an algebra which is a free `O_S`-module.

<!-- original page 21 -->

The introduction of Definition 6.1 is justified by the following:

**Theorem 6.4.** *Let $S$ be a prescheme, $Z$ an essentially free $S$-prescheme, $Y$ a closed subprescheme of $Z$.
Consider the following functor*[^N.D.E-VIII-24]

<!-- label: III.VIII.6.4 -->

```text
F = ∏_{Z/S} Y/Z : (Sch)°/S → (Ens),
F(S′) = Γ(Y_{S′}/Z_{S′}) = { ∅           if Z_{S′} ≠ Y_{S′};
                             {id_{Z_{S′}}}  if Z_{S′} = Y_{S′}.
```

*This functor is representable by a closed subprescheme of $S$.*[^N.D.E-VIII-25]

[^N.D.E-VIII-26] Let us first note that $F$ is a sheaf for the (fpqc) topology: since $F(S') = \emptyset$ or `{pt}` for
every $S'$, this reduces to verifying that if $(S_{i})$ is an open covering of $S$ (resp. $S' \to S$ a faithfully flat
quasi-compact morphism), and if each $Y_{S_{i}} \to Z_{S_{i}}$ (resp. if $Y_{S'} \to Z_{S'}$) is an isomorphism, the
same holds for $Y \to Z$; now this is clear (resp. follows from SGA 1, VIII 5.4 or EGA IV₂, 2.7.1).

Moreover, by SGA 1, VIII 2.1 and 5.5, faithfully flat quasi-compact morphisms are of effective descent for the fibered
category of closed immersion arrows. This allows us to restrict ourselves, with the notation of 6.1, to the case where
$S = S'_{i}$.

Let $(Z_{j})$ be a covering of $Z$ by affine opens such that $O(Z_{j})$ is a free module over $A = O(S)$, and let
$Y_{j} = Y \cap Z_{j}$ and $F_{j} : (Sch)^{\circ}/S \to (Ens)$ be the functor defined in terms of $(Z_{j}, Y_{j})$ as
$F$ in terms of $(Z, Y)$. It is a subfunctor of the final functor, and one evidently has $F = \bigcap_{j} F_{j}$, which
reduces us to

<!-- original page 19 -->

proving that each $F_{j}$ is representable by a closed subscheme $T_{j}$ of $S$ (for then $F$ will be representable by
the closed subscheme $T$ intersection of the $T_{j}$). One may therefore suppose $Z$ also affine,
$Z = \operatorname{Spec}(B)$, where $B$ is a free $A$-module. Let $J$ be a subset of $B$ defining the subscheme $Y$ of
$Z$, and let $K$ be the ideal in $A$ generated by the $u_{i}(J) \subseteq A$, where the $u_{i} : B \to A$ are the
coordinate forms with respect to the chosen basis. One observes at once that $T = V(K) = \operatorname{Spec}(A/K)$
satisfies the desired condition, which completes the proof.

**Examples 6.5.** Let us give some important examples of functors that reduce to functors $\prod_{Z/S} Y/Z$ of the type
envisaged in 6.4 and for which it is useful in the sequel to have criteria of representability. We denote by $S$ a
prescheme, by $X$, $Y$, $Z$, etc., preschemes over $S$.

<!-- label: III.VIII.6.5 -->

a) Suppose given an $S$-morphism

```text
(*)    q : X → Hom_S(Y, Z),
```

("$X$ acts on $Y$ with values in $Z$"), i.e. a morphism

```text
(**)   r : X ×_S Y → Z.
```

Consider a subprescheme $Z'$ of $Z$, whence a monomorphism

<!-- original page 22 -->

```text
Hom_S(Y, Z′) → Hom_S(Y, Z)
```

which makes the first functor a subfunctor of the second; let $X'$ be the inverse image of this subfunctor by `(*)`,
that is the subfunctor of $X$ such that $X'(T)$ is the set of $x \in X(T)$ such that $q(x) : Y_{T} \to Z_{T}$ factors
through $Z'_{T}$. This functor $X'$ can be described as follows: set $P = X \times_{S} Y$, let $P'$ be the inverse image
of $Z'$ by $r : P \to Z$; then one has an evident isomorphism

$$
(***)   X' \simeq \prod_{P/X} P'/P.
$$

One thus obtains: *if $Y$ is essentially free over $S$ and $Z'$ closed in $Z$, the subfunctor $X'$ of $X$ is
representable by a closed subprescheme of $X$*.

b) Suppose given two ways of making $X$ act on $Y$ with values in $Z$, i.e. two morphisms

```text
q_1, q_2 : X ⇒ Hom_S(Y, Z),
```

and set $X' = Ker(q_{1}, q_{2})$: this is the subfunctor of $X$ such that $X'(T)$ is the set of $x \in X(T)$ such that
the two morphisms $q_{1}(x), q_{2}(x) : Y_{T} \Rightarrow Z_{T}$ are equal. Now giving $q_{1}, q_{2}$ is equivalent to
giving a morphism

```text
q : X → Hom_S(Y, Z ×_S Z),
```

or, again, a morphism $r : X \times_{S} Y \to Z \times_{S} Z$; setting $U = Z \times_{S} Z$, let $U'$ be the diagonal
subprescheme of $Z \times_{S} Z$; then $X'$ is none other than the inverse image of the subfunctor
$\operatorname{Hom}_{S}(Y, U') \to \operatorname{Hom}_{S}(Y, U)$ by $q$, hence can be put in the form `(***)`, with
$P = X \times_{S} Y$ and $P'$ = inverse image of the diagonal by $r$, i.e. kernel of

<!-- original page 23 -->

```text
X ×_S Y ⇒ Z.
```

One is thus in the conditions of (a). One sees consequently that: *if $Y$ is essentially free over $S$ and $Z$ separated
over $S$, the subfunctor $X'$ of $X$ is representable by a closed subprescheme of $X$*.

c) Suppose given a morphism

```text
q : X → Hom_S(Y, Y),
```

i.e. "$X$ acts on $Y$". Let $X'$ be the "kernel" of this morphism, i.e. the subfunctor $X'$ of $X$ such that $X'(T)$ is
the set of $x \in X(T)$ such that $q(x) : Y_{T} \to Y_{T}$ is the identity. This functor is amenable to (b), as one sees
by introducing a second homomorphism

```text
q′ : X → Hom_S(Y, Y)
```

<!-- original page 20 -->

"by making $X$ act trivially on $Y$". Hence: *if $Y$ is essentially free over $S$ and separated over $S$, the kernel
subfunctor of $q$ is representable by a closed subprescheme of $X$*.

d) Under the conditions of (c), consider the subfunctor $Y'$ of $Y$ "of invariants under $X$", so $Y'(T)$ is the set of
$y \in Y(T)$ such that the corresponding morphism $q(y) : X_{T} \to Y_{T}$ is "the $T$-constant morphism with value
$y$". Introducing $q'$ as in (c), and the homomorphisms corresponding to $q$ and $q'$:

```text
q, q′ : Y ⇒ Hom_S(X, Y),
```

one sees that $Y'$ is precisely $Ker(q, q')$, and is therefore amenable again to (b) (with the roles of $X$, $Y$
reversed and $Z = Y$).

Consequently, *if $X$ is essentially free over $S$, $Y$ separated over $S$, then the subfunctor $Y'$ of $Y$ of
invariants under $X$ is representable by a closed subprescheme of $Y$*.

<!-- original page 24 -->

e) Constructions of the type explained in the preceding examples are especially frequent in group theory. Thus, when $G$
is an $S$-prescheme in groups acting on the $S$-prescheme $X$:

$$
q : G \to \operatorname{Aut}_{S}(X),
$$

the kernel of $q$ ("the subgroup of $G$ acting trivially") is a closed subscheme of $G$ provided that $X$ is essentially
free and separated over $S$ (example (c)), and the subobject $X^{G}$ of invariants is a closed subprescheme of $X$,
provided that $G$ is essentially free over $S$ and $X$ separated over $S$[^N.D.E-VIII-27] (example (d)).

Let $Y$, $Z$ be subpreschemes of $X$; consider the subfunctor $Transp_{G}(Y, Z)$ of $G$ ("transporter of $Y$ into $Z$")
whose points with values in a $T$ over $S$ are the $g \in G(T)$ such that the corresponding automorphism of `X_T`
satisfies $g(Y_{T}) \subseteq Z_{T}$ i.e. induces a morphism $Y_{T} \to X_{T}$ factoring through $Y_{T} \to Z_{T}$.
Hence: *if $Y$ is essentially free over $S$, and $Z$ closed in $X$, then $Transp_{G}(Y, Z)$ is a closed subprescheme of
$G$* (example (a)).

One may also consider the strict transporter of $Y$ into $Z$,[^N.D.E-VIII-28] whose points with values in a $T$ over $S$
are the $g \in G(T)$ such that $g(Y_{T}) = Z_{T}$, which is nothing but
$Transp_{G}(Y, Z) \cap \sigma(Transp_{G}(Z, Y))$, where $\sigma$ is the symmetry of $G$. Consequently, if $Y$ and $Z$
are essentially free over $S$ and closed in $X$, the strict transporter of $Y$ into $Z$ is a closed subprescheme of $G$.

An important case is that where $X = G$, with $G$ acting on itself by inner automorphisms. If $H$ is a subprescheme of
$G$, the strict transporter of $H$ into $H$ is also called the *normalizer of $H$ in $G$*, and denoted $Norm_{G} H$.
Hence: *if $H$ is a closed subprescheme of $G$ in groups, essentially free over $S$, then $Norm_{G} H$ is representable
by a closed subprescheme of $G$ in groups.*

Let finally $Z$ be a subprescheme of $G$; then its *centralizer* $Centr_{G}(Z)$ in $G$ is the subfunctor of $G$ in
groups defined by the procedure of (d), considering "$Z$ acts on $G$" via the action induced by that of $G$; hence *if
$Z$ is essentially free over $S$ and $G$ separated over $S$, $Centr_{G}(Z)$ is a closed subprescheme of $G$ in groups*.

<!-- original page 25 -->

In particular, if $G$ is essentially free and separated over $S$, then *the center $C$ of $G$, which is none other than
$Centr_{G}(G)$, is a closed subprescheme of $G$ in groups*.

When $S$ is the spectrum of a field, 6.3 (b) shows that in examples (a) to (e) above, the conditions "essentially free"
are automatically satisfied; only separation conditions remain. Recalling that a prescheme in groups over a field is
necessarily separated, one finds for example:

**Corollary 6.7.**[^N.D.E-VIII-29] *Let $G$ be a prescheme in groups over a field $k$. Then:*

<!-- label: III.VIII.6.7 -->

*– For every subprescheme $Z$ of $G$, the centralizer of $Z$ in $G$ is a closed subprescheme of $G$ in groups; this is
in particular the case for the center $Centr_{G}(G)$ of $G$.*

*– More generally, if $u, v : X \to G$ are morphisms of preschemes, $Transp_{G}(u, v)$ is representable by a closed
subprescheme of $G$.*

*– For two subpreschemes `Y, Z` of $G$, with $Z$ closed, $Transp_{G}(Y, Z)$ is a closed subprescheme of $G$. If $Y$ is
also closed, the same conclusion holds for $Transp^{str}_{G}(Y, Z)$.*

*– For every subprescheme in groups*[^N.D.E-VIII-30] *$H$ of $G$, the normalizer $Norm_{G}(H)$ is a closed subscheme of
$G$ in groups.*

**Remark 6.8.**[^N.D.E-VIII-31] *Let $A$ be a commutative ring, $M$ an $A$-module,
$M^{\vee} = \operatorname{Hom}_{A}(M, A)$; endow the $A$-module $\operatorname{End}_{A}(M)$ with the topology of
pointwise convergence (discrete), i.e. a basis of neighborhoods of `0` is formed by the following $A$-submodules, where
$n \in \mathbb{N}$ and $m_{1}, \cdots, m_{n} \in M$:*

<!-- label: III.VIII.6.8 -->

```text
K(m_1, …, m_n) = { u ∈ End_A(M) | u(m_i) = 0  for i = 1, …, n }.
```

*We say that $M$ is a* quasi-free $A$-module *if the image of the canonical morphism
$\Theta : M \otimes_{A} M^{\vee} \to \operatorname{End}_{A}(M)$ contains $id_{M}$ in its closure, i.e. if the following
condition holds:*

```text
(*)  { for all m_1, …, m_n ∈ M, there exist x_1, …, x_r ∈ M and f_1, …, f_r ∈ M^∨
     { such that m_i = Θ(∑_{s=1}^r x_s ⊗ f_s)(m_i) = ∑_{s=1}^r f_s(m_i) x_s for i = 1, …, n.
```

*(In this case, $Im \Theta$ is dense in $\operatorname{End}_{A}(M)$, since for every $u \in \operatorname{End}_{A}(M)$
one has*

```text
u(m_i) = ∑_{s=1}^r f_s(m_i) u(x_s) = Θ(∑_{s=1}^r u(x_s) ⊗ f_s)(m_i).)
```

Let us note first that this property is stable under base change. Indeed, let $\phi : A \to A'$ be a morphism of rings,
$M' = M \otimes_{A} A'$, and $m'_{1}, \cdots, m'_{n} \in M'$. Then $m'_{i} = \sum_{j} m_{ij} \otimes b_{ij}$
($m_{ij} \in M$, $b_{ij} \in A'$); by hypothesis, there exist $x_{1}, \cdots, x_{r} \in M$ and
$f_{1}, \cdots, f_{r} \in \operatorname{Hom}_{A}(M, A)$ such that $m_{ij} = \sum_{s} x_{s} f_{s}(m_{ij})$ for all
`i, j`. Denote by $\phi \circ f_{s}$ the image of $f_{s}$ in
$\operatorname{Hom}_{A}(M, A') = \operatorname{Hom}_{A'}(M', A')$; then for every $i = 1, \cdots, n$ one has:

```text
(∑_s x_s ⊗ φ ∘ f_s)(m′_i) = ∑_{s,j} x_s ⊗ φ(f_s(m_{ij})) b_{ij} = ∑_j (∑_s x_s f_s(m_{ij})) ⊗ b_{ij} = m′_i,
```

<!-- original page 22 -->

which proves that $M'$ is quasi-free over $A'$.

Let us also note that every projective $A$-module $P$ is quasi-free (there exist $A$-morphisms
$A^{(I)} -\pi\to P -\tau\to A^{(I)}$ such that $\pi \circ \tau = id_{P}$; denote by $(e_{i})$ the canonical basis of
$A^{(I)}$ and $f_{i}$ the linear form $e^{*}_{i} \circ \tau$ on $P$; if $m_{1}, \cdots, m_{n} \in P$, there exists a
finite subset $J$ of $I$ such that $m_{k} = \sum_{i \in J} f_{i}(m_{k}) \pi(e_{i})$ for $k = 1, \cdots, n$).

Then, Theorem 6.4 remains valid if in the statement of Definition 6.1 the word "free" is replaced by "projective" or,
more generally, by "quasi-free". Indeed, proceeding as in the proof of 6.4, one is reduced to proving:

**Lemma 6.8.1.** *Let $M$ be a quasi-free $A$-module, $N$ a submodule, $F$ the covariant functor
$(A-algebras) \to (Ens)$ such that $F(B) = {pt}$ if $M_{B} = (M/N)_{B}$, and $F(B) = \emptyset$ otherwise. Then there
exists an ideal $K$ of $A$ such that $F(B) = {pt}$ if and only if the morphism $A \to B$ factors through $A/K$, i.e. one
has a functorial isomorphism in $B$:*

<!-- label: III.VIII.6.8.1 -->

$$
F(B) \simeq \operatorname{Hom}_{A-alg.}(A/K, B).
$$

*Proof.* Let $(n_{j})$ be a system of generators of $N$, and let $F_{j}$ be the subfunctor of the final functor $e$
($e(B) = {pt}$ for every $B$) corresponding to the submodule $A n_{j}$. One has $F(B) = {pt}$ if and only if the image
of each $n_{j}$ in `M_B` is zero, hence $F$ is the intersection of the functors $F_{j}$. This reduces us to the case
where $N$ is generated by one element $n$.

Let $\phi : A \to B$ be an $A$-algebra; if the image $n \otimes 1$ of $n$ in `M_B` is zero, then for every
$f \in M^{\vee} = \operatorname{Hom}_{A}(M, A)$ one has $0 = f(n) \otimes 1 = \phi(f(n))$. On the other hand, since $M$
is quasi-free, there exist $x_{1}, \cdots, x_{r} \in M$ and $f_{1}, \cdots, f_{r} \in M^{\vee}$ such that
$n = \sum_{s} f_{s}(n) x_{s}$, whence $n \otimes 1 = \sum_{s} x_{s} \otimes \phi(f_{s}(n))$. It follows that
$n \otimes 1 = 0$ if and only if $\phi$ factors through $A/K$, where $K$ is the ideal generated by the $f_{s}(n)$ for
$s = 1, \cdots, r$. This proves the lemma.

## 7. Appendix. On monomorphisms of preschemes in groups

The result proved in the present § is unnecessary for the sequel of the seminar, except for X 8.8 and XV and XVI. It
rests in an essential way on the existence theorem for quotient groups of Exposé VI_A.[^N.D.E-VIII-32]

<!-- original page 26 -->

Corollary 5.7 leads one to ask under what conditions one can assert that a monomorphism $u : G \to H$ of $S$-groups is
an immersion, or even a closed immersion.

We have seen in VI_B 1.4.2 that this is the case if $S$ is the spectrum of a field, provided that $G$ is of finite type
over $k$ and $H$ is locally of finite type over $k$. One easily concludes that the same result remains valid if one only
supposes $S$ Artinian.[^N.D.E-VIII-33]

On the other hand, it is easy to give examples of bijective monomorphisms that are not immersions, with $S$ being for
example the affine line over a field, or the spectrum of a discrete valuation ring. One will take for example
$H = (\mathbb{Z}/2\mathbb{Z})_{S}$, $G = G_{1} \times_{S} G_{2}$, where `G_1` is the open subgroup of $H$, the
complement of the closed point $x$ distinct from `0` of the fiber $H_{s} \simeq \mathbb{Z}/2\mathbb{Z}$ (where $s$
denotes a fixed closed point of $S$), and `G_2` is the closed subscheme of $H$ that is the sum of the subscheme reduced
to the unit section, and the closed reduced subscheme defined by the closed point $x$. One easily verifies that `G_2` is
indeed stable under the multiplication of $H$, hence is a group scheme. The immersions $G_{i} \to H$ ($i = 1, 2$) then
define a homomorphism of $S$-groups $G = G_{1} \times G_{2} \to H$, which is obviously a bijective monomorphism (and
moreover a local immersion), but is not an immersion. (One observes that $G$ and $H$ are reduced, $G$ having three
disjoint irreducible components, while $H$ has only two irreducible components.) One will note that $G_{1} \to H$ also
gives an example of an open subgroup $G$ of $H$ which is not closed (contrary to what occurs for algebraic groups over a
field). The theory of the degeneration of elliptic curves provides further examples of this latter phenomenon, with
moreover $H$ smooth over $S$ of relative dimension `1`, and $G$ with connected fibers.

It is possible[^VIII-7-star] on the other hand that, as soon as one assumes $G$ flat over $S$, and (say) $G$ and $H$ of
finite presentation over $S$, a monomorphism $u : G \to H$ of $S$-groups is automatically an immersion. We shall prove a
result of this nature, under supplementary hypotheses.

Let us note first that one may assume $S$ affine, and (thanks to the finite presentation hypothesis on $G$ and $H$,
which allows one to reduce to the case of the spectrum of a ring of finite type over $\mathbb{Z}$[^N.D.E-VIII-34]) $S$
Noetherian. Then $G$ and $H$ are Noetherian. To say that $u : G \to H$ is a closed immersion (resp. an immersion) then
amounts to saying that $u$ is a monomorphism (which is true by hypothesis) and that $u$ is proper (resp. and that $u$ is

<!-- original page 27 -->

proper at every point of $u(G)$)[^N.D.E-VIII-35]. The valuative criterion of properness assures us that it suffices to
verify that for every base change $S' \to S$, with $S'$ the spectrum of a discrete valuation ring, complete if one
wishes, the morphism $u' : G' \to H'$ has the same properness property. (The case of local properness was forgotten in
EGA II 7.3, and will appear as an erratum in EGA IV[^VIII-7-starstar].) This therefore reduces us to the case where $S$
itself is the spectrum of a complete discrete valuation ring — subject to the supplementary hypotheses on $G$, $H$, $u$
that we are led to formulate being stable under base change.

Let then $s$ (resp. $s_{0}$) be the closed point (resp. the generic point) of $S$. Then the homomorphisms induced on the
fibers

```text
u_s : G_s → H_s    and   u_{s_0} : G_{s_0} → H_{s_0}
```

are closed immersions, since these are monomorphisms of group schemes of finite type over fields (VI_B 1.4.2). We may
therefore identify $G_{s_{0}}$ with a closed subscheme of $H_{s_{0}}$. Now we have the following result:

**Lemma 7.1.** *Let $S$ be the spectrum of a discrete valuation ring, $s_{0}$ its generic point, $H$ an $S$-prescheme,
`L_0` a closed subprescheme of the generic fiber $H_{s_{0}}$, so that `L_0` is also a subprescheme of $H$.*

<!-- label: III.VIII.7.1 -->

*Then the schematic closure $\bar{L}_{0}$ in $H$ (i.e. the smallest closed subprescheme of $H$ majorizing `L_0`, cf. EGA
I 9.5) exists and is also the unique closed subprescheme of $H$, flat over $S$, whose generic fiber is `L_0`. Moreover,
the formation of $\bar{L}$ is functorial with respect to a variable couple $(H, L_{0})$, and commutes with the formation
of cartesian products over $S$.*

<!-- original page 28 -->

*In particular, if $H$ is an $S$-group and `L_0` is a subgroup of $H_{s_{0}}$, then $\bar{L}$ is a subgroup of $H$.*

The proof is immediate and left to the reader[^VIII-7-starstarstar]. Applying this to the situation $H$, $G_{s_{0}}$,
one sees that the monomorphism $u : G \to H$ factors as $G \to L \to H$, where $L$ is a subgroup of $H$ that is a closed
subprescheme, flat over $S$, and where $G \to L$ induces an isomorphism on the generic fibers. Then $u : G \to H$ is an
immersion (resp. a closed immersion) if and only if $u' : G \to L$ is. This therefore reduces us to the case where $H$
is flat over $S$ and $u_{s_{0}} : G_{s_{0}} \to H_{s_{0}}$ is an isomorphism (subject to the supplementary hypotheses we
may have to formulate on $G$, $H$, $u$ being respected when $H$ is replaced by a closed subprescheme in groups). As then
$H$ is the schematic closure of $H_{s_{0}}$, if $u$ is an immersion, then $u(G)$ will be a subprescheme[^N.D.E-VIII-36]
of $H$ majorizing $H_{s_{0}}$, hence its schematic closure will also be $H$, and consequently $u(G)$ will be an open
subprescheme of $H$. Hence, we shall in fact have to prove that $u$ is an open immersion (resp. an isomorphism, if we
want to establish that $u$ is a closed immersion). Since $G$ and $H$ are flat

<!-- original page 29 -->

over $S$, it amounts to the same thing to say that the morphisms induced on the fibers are open immersions, resp.
isomorphisms (cf. SGA 1, I 5.7), and since this is already the case for $u_{s_{0}}$, one is reduced to proving that
$u_{s}$ is an open immersion, resp. an isomorphism.

Let us note first that, since $G$ and $H$ are flat over $S$, the dimension of their fibers remains constant (VI_B 4.3).
Since $G$ and $H$ have the same generic fiber, it follows that this dimension is the same for $G$ and $H$, hence
$u_{s} : G_{s} \to H_{s}$ is a monomorphism of algebraic groups of the same dimension. One concludes easily that $G_{s}$
is open in $H_{s}$, and in fact is set-theoretically a union of connected components of $H_{s}$ (one is reduced to the
case where the base field is algebraically closed, and $G$ and $H$ reduced, hence smooth over $k$, where it is
immediate…). Hence $H_{s} - G_{s}$ is closed in $H_{s}$, hence in $H$, hence its complement `H_0` in $H$ is open, and is
obviously an open stable under the group law of $H$. Hence, up to replacing $H$ by `H_0`, one may, in order to prove
that $u$ is an immersion, reduce (with the usual proviso) to the case where, in addition to the preceding hypotheses,
one assumes $u$ bijective, i.e. $u_{s} : G_{s} \to H_{s}$ bijective. One is therefore in any case reduced to proving
that $u$ or again $u_{s}$ is an isomorphism, possibly under the hypothesis of bijectivity.

Suppose therefore first that $u$ is bijective. If $H_{s}$ is reduced, one can evidently conclude that $u_{s}$ is an
isomorphism, since $G_{s}$ identifies with a closed subscheme of $H_{s}$ having the same underlying set. In particular,
if $k = \kappa(s)$ is of characteristic zero, every algebraic group over $k$ is reduced by Cartier (cf. VI_B, 1.6.1, or
VII_B, 3.3.1, or EGA IV₄, 16.12.2 and 17.12.5), and one has thus obtained:

**Proposition 7.2.** *Let $u : G \to H$ be a homomorphism of preschemes in groups of finite presentation over $S$.
Suppose that $u$ is a monomorphism, $G$ flat over $S$, and the residue fields of $S$ of characteristic zero. Then $u$ is
an immersion.*

<!-- label: III.VIII.7.2 -->

When $\kappa(s)$ is of characteristic $p > 0$, we shall restrict to the case where $G$ is commutative. Then (with the
reductions made) $H$ is also commutative, since it is the schematic closure of $H_{s_{0}}$ which is isomorphic to
$G_{s_{0}}$, hence commutative. For every integer $n \geqslant 0$, we set $S_{n} = \operatorname{Spec}(V/m^{n+1})$
(where $V$ is the valuation ring defining $S$ and $m$ its maximal ideal), $G_{n} = G \times_{S} S_{n}$,
$H_{n} = H \times_{S} S_{n}$. For every integer $m > 0$, we also introduce the subgroups ${}_{mG}$ and ${}_{mH}$ of $G$
and $H$, kernels of the $m$-th power. One defines similarly ${}_{m}(G_{n}) = ({}_{mG})_{n}$, which one denotes simply
`_mG_n`, and likewise for $H$.

By virtue of VI_A 3.2, one can form the quotients $Q_{n} = H_{n}/G_{n}$. Then $Q_{n}$ is a commutative group scheme over
$S_{n}$, flat over $S_{n}$, and $H_{n} \to Q_{n}$ is a faithfully flat morphism with kernel $G_{n}$. Since the formation
of quotients commutes with base extension[^N.D.E-VIII-37], one has

```text
Q_n ≃ Q_m ×_{S_m} S_n    for m ⩾ n,
```

in particular the fiber $Q_{n} \times_{S_{n}} S_{0}$ is none other than $Q_{0} = H_{0}/G_{0}$. Since `G_0` has the same

<!-- original page 30 -->

underlying set as `H_0`, then `Q_0` is set-theoretically reduced to a single point: it is a purely infinitesimal group.
Consequently, each $Q_{n}$ is finite and flat over $S_{n}$. Hence $Q_{n}$ is defined by an algebra $C_{n}$ over
$V_{n} = V/m^{n+1}$ which is a free module of finite type over this ring, and for $m \geqslant n$ one has
$C_{n} = C_{m} \otimes_{V_{m}} V_{n}$, an isomorphism also respecting the diagonal map. One thus obtains a free module
of finite type `C = lim_{←} C_n` over `V = lim_{←} V_n`, and the diagonal maps of the $C_{n}$ define a diagonal map of
$C$, so that $Q = \operatorname{Spec}(C)$ becomes a group scheme finite and flat over $S$, such that

```text
Q ×_S S_n = Q_n
```

for every $n$.

**Lemma 7.3.**[^N.D.E-VIII-38] *Let $K$ be a field, $Q$ a finite group scheme over $K$, of degree $n$. Then the $n$-th
power morphism in $Q$ is zero.*

<!-- label: III.VIII.7.3 -->

Cf. VII_A 8.5.

**Remark 7.3.1.** *Statement 7.3 retains a sense for a group scheme $Q/S$ finite and locally free over $S$, $S$ being an
arbitrary base prescheme. It would be interesting to find a proof in this general case.*

<!-- label: III.VIII.7.3.1 -->

One will note that 7.3 (i.e. VII_A, 8.5) proves in any case that the envisaged statement is true if $S$ is reduced, as
one sees by applying 7.3 to the fibers of $Q$ at the maximal points (i.e. generic points of the irreducible components)
of $S$.[^N.D.E-VIII-39]

In particular, under the conditions of the preceding proof, where $S$ is the spectrum of a discrete valuation ring and
$Q$ is commutative, one finds that $n \cdot id_{Q} = 0$. Moreover, here $n$ is a power $p^{\nu_{0}}$ of the residue
characteristic, and one finds:

**Corollary 7.4.** *With $Q$ and the $Q_{n}$ as above, and their common degree being $p^{\nu_{0}}$, one will have
$p^{\nu_{0}} \cdot id_{Q} = 0$ and consequently $p^{\nu_{0}} \cdot id_{Q_{n}} = 0$ for every $n$.*

<!-- label: III.VIII.7.4 -->

<!-- original page 31 -->

**Corollary 7.5.** *Suppose moreover that `G_0` is smooth over $k$, and the homomorphism $p \cdot id_{G_{0}}$ flat
(which amounts to saying, in virtue of the structure of algebraic groups over an algebraically closed field $\bar{k}$,
that $G_{\bar{k}}$ contains no subgroup isomorphic to the additive group). Then for every $\nu \geqslant \nu_{0}$ and
$n > 0$, the group ${}_{p^{\nu}}H_{n}$ is flat over $S_{n}$.*

<!-- label: III.VIII.7.5 -->

Indeed, it follows from $p^{\nu_{0}} \cdot id_{Q_{n}} = 0$ that $p^{\nu} \cdot id_{H_{n}}$ factors through $G_{n}$, so
that one has a commutative diagram:

```text
                         p^ν · id_{H_n}
            H_n  ─────────────────────────────→  H_n
              ╲                                    ↑
               ╲ v_n                              u_n
            u_n ╲                                  │
                 ↘    p^ν · id_{G_n}              │
                  G_n  ─────────────────────────→ G_n.
```

I claim that $v_{n}$ is flat. Indeed, since $H_{n}$ and $G_{n}$ are flat over $S_{n}$, one is reduced to verifying that
$v_{0}$ is flat (SGA 1, IV 5.9), so one may assume that $n = 0$, whence $S_{n} = \operatorname{Spec}(k)$. Since
$p \cdot id_{G_{0}}$, and hence $p^{\nu} \cdot id_{G_{0}}$, is flat, its image is an open induced subgroup $G'_{0}$ of
`G_0`, and since $u_{0} : G_{0} \to H_{0}$ is surjective, it follows that $v_{0}$ takes its values in $G'_{0}$, hence
may be considered as a homomorphism into $G'_{0}$. Since its composition with $u_{0}$ is an epimorphism, it is itself an
epimorphism, hence a flat homomorphism into $G'_{0}$, hence a flat homomorphism into `G_0`. Hence $v_{n}$ is flat, hence
$Ker v_{n} = {}_{p^{\nu}}H$ is flat over $S$. QED.

**Remark.** We have not explicitly used the fact that `G_0` is smooth over $k$; but it is easy to see that this is a
consequence of the fact that $p \cdot id_{G}$ is flat — this is why we made this condition explicit in the hypothesis of
Corollary 7.5.

**Lemma 7.6.** *Let $u : G \to H$ be a surjective monomorphism of commutative algebraic groups over a field $k$ of
characteristic $p > 0$; consider the (purely infinitesimal) group $Q = H/G$. Then there exists an integer $\nu_{1}$ such
that for $\nu \geqslant \nu_{1}$, the sequence*

<!-- label: III.VIII.7.6 -->

$$
0 \to {}_{p^{\nu}}G \to {}_{p^{\nu}}H \to Q \to 0
$$

*is exact.*

It suffices to ensure exactness at $Q$, and for this to ensure that the homomorphism

$$
(*)    O_{Q,e} \to O_{{}_{p^{\nu}}H, e}
$$

of local rings at the neutral elements is injective (N.B. recall that $Q$ is set-theoretically reduced to the element
$e$). Now one has a natural homomorphism

$$
(**)   O_{{}_{p^{\nu}}H, e} \to O_{H,e}/m^{p^{\nu}},
$$

where $m$ is the augmentation ideal (i.e. the maximal ideal) of $O_{H,e}$, as one sees by noting that
$p^{\nu} \cdot id_{H}$ vanishes on the kernel of "the iterated Frobenius homomorphism" $F^{\nu}$; the composite of the
homomorphisms `(*)` and `(**)` is also equal to the natural composite

$$
(***)  O_{Q,e} \to O_{H,e} \to O_{H,e}/m^{p^{\nu}}.
$$

<!-- original page 32 -->

Now $O_{Q,e} \to O_{H,e}$ is injective, since $H \to Q$ is an epimorphism hence is flat; on the other hand $O_{Q,e}$ is
Artinian, and finally the intersection in $O_{H,e}$ of the $m^{p^{\nu}}$ is reduced to `0`, hence so is the intersection
of their traces on $O_{Q,e}$. Consequently one of these traces is reduced to `0`, which proves that `(***)` is
injective, and a fortiori `(*)` is injective.

**Lemma 7.7.** *Under the conditions of 7.5 there exists a $\nu_{1}$ such that, for $\nu \geqslant \nu_{1}$ and every
$n$, the sequence of $S_{n}$-groups*

<!-- label: III.VIII.7.7 -->

```text
0 → _{p^ν}G_n → _{p^ν}H_n -w_n→ Q_n → 0
```

*is exact (more precisely, $w_{n}$ is faithfully flat and its kernel is ${}_{p^{\nu}}G_{n}$).*

One takes $\nu_{1}$ as in 7.6 applied to $u_{0} : G_{0} \to H_{0}$, and $\nu_{1} \geqslant \nu_{0}$ (where $p^{\nu_{0}}$
= rank `Q_0`). It only remains to verify that $w_{n}$ is faithfully flat. Now by virtue of 7.5, ${}_{p^{\nu}}H$ is flat
over $S_{n}$, and since $Q_{n}$ is too, one is reduced to verifying that $w_{0} : {}_{p^{\nu}}H_{0} \to Q_{0}$ is
faithfully flat, i.e. is an epimorphism, which is true by the choice of $\nu_{1}$.

**Corollary 7.8.** *Suppose moreover $H$ separated over $S$, more generally that ${}_{p^{\nu}}H$ is separated over $S$
for every $\nu$, and that ${}_{p^{\nu}}G$ is finite over $S$ for every $\nu$. Then the group schemes ${}_{p^{\nu}}G$ and
${}_{p^{\nu}}H$ are finite and flat over $S$ for $\nu \geqslant \nu_{1}$, and one has an exact sequence*

<!-- label: III.VIII.7.8 -->

```text
0 → _{p^ν}G → _{p^ν}H -w→ Q → 0.
```

Since $u : G \to H$ is surjective, so is the induced morphism ${}_{p^{\nu}}G \to {}_{p^{\nu}}H$, and since the first
member is finite over $S$ and the second separated over $S$, it follows that the second member is finite over $S$. To
then verify that ${}_{p^{\nu}}G$ and ${}_{p^{\nu}}H$ are also flat over $S$, it suffices to verify that this is the case
for ${}_{p^{\nu}}G_{n}$ and ${}_{p^{\nu}}H_{n}$ for every $n$, which is contained in 7.5. Finally, the exact sequence of
7.8 comes from the exact sequences 7.7 for variable $n$.

<!-- original page 34 -->

Taking the generic fibers in the exact sequence 7.8 and recalling that $u_{s_{0}} : G_{s_{0}} \to H_{s_{0}}$ is an
isomorphism, one finds $Q_{s_{0}}$ = unit group, whence (since $Q$ is flat over $S$) $Q$ = unit group, whence $Q_{s}$ =
unit group, hence $u_{s} : G_{s} \to H_{s}$ is an isomorphism. Hence:

**Proposition 7.9.** *Let $u : G \to H$ be a homomorphism of preschemes in groups of finite presentation over the
prescheme $S$. Suppose:*

<!-- label: III.VIII.7.9 -->

*a) $u$ is a monomorphism.*

*b) $G$ is flat over $S$.*

*c) For every $s \in S$ such that $\kappa(s)$ is of residue characteristic $p > 0$, one wants the following conditions
to be satisfied for the homomorphism $u' : G' \to H'$ of preschemes in groups over $S' = \operatorname{Spec}(O_{S,s})$
deduced from $u : G \to H$ by the base change $S' \to S$:*

*– $G'$ is commutative,*

*– the special fiber $G'_{0} = G_{s}$ is smooth over $\kappa(s)$,*

*– for every integer $\nu > 0$, ${}_{p^{\nu}}G'$ is finite over $S'$ and ${}_{p^{\nu}}H'$ is separated over $S'$.*

*Under these conditions, $u$ is an immersion.*

It suffices to remark that, in (c), the condition that ${{}_{pG}'}_{0}$ be finite over $S'$ implies that ${{}_{pG}'}_{0}$ is
finite over $\kappa(s)$, which already implies that $G'_{0} \otimes_{\kappa(s)} \overline{\kappa(s)}$ contains no
subgroup isomorphic to the additive group, so that one is under the hypotheses of 7.5.

<!-- original page 29 -->

**Remark 7.10.** *Examples of M. Raynaud (XVI 1.1 (a) and (b)) show that in (c) one cannot drop either the hypothesis
that the ${}_{p^{\nu}}G'$ are finite over $S'$ or the hypothesis that the ${}_{p^{\nu}}H'$ are separated over $S'$.*

<!-- label: III.VIII.7.10 -->

We now want conditions ensuring that $u$ is a closed immersion. We therefore preserve the hypotheses preceding 7.9 but
no longer assume $u$ surjective (only $u$ an isomorphism on the generic fibers). We already know that $u : G \to H$ is
an open immersion, hence also $u_{0} : G_{0} \to H_{0}$, whose image therefore contains the connected component of the
identity element $(H_{0})^{0}$. Note that, since `G_0` is smooth over $k$ and "without additive component" over the
algebraic closure of $k$, the same holds for `H_0`. Now we have:

**Lemma 7.11.** *Let $H$ be a commutative algebraic group over a field $k$, such that $H \otimes_{k} \bar{k}$ contains
no subgroup isomorphic to $G_{a}$. Let $n$ = degree $H/H^{0}$; then the homomorphism*

<!-- label: III.VIII.7.11 -->

$$
{}_{nH} \to H/H^{0}
$$

*is surjective.*

One may indeed assume $k$ algebraically closed, and then this follows from the well-known fact that $H^{0}(k)$ is a
divisible group.

Suppose now (returning to our situation $u : G \to H$) that the ${}_{nG}$ ($n > 0$) are proper over $S$, and the
${}_{nH}$ are separated over $S$. Note on the other hand that the ${}_{nH}$ are flat over $S$. Indeed, it suffices to
see this at the points above $s$; one is then reduced to proving that $n \cdot id_{H}$ is flat at the points above $s$,
and for this one is reduced to verifying that $n \cdot id_{H_{0}}$ is flat, which is equivalent (as we have already
noted) to the fact that $(H_{0})^{0}$ is smooth[^N.D.E-VIII-40] over $k$ and has no $G_{a}$-component over the algebraic
closure of $k$. As $(H_{0})^{0} = (G_{0})^{0}$, this follows from the analogous hypothesis made on `G_0`. On the other
hand, the ${}_{nH}$ are separated over $S$ since $H$ is, hence the morphism ${}_{nG} \to {}_{nH}$ is proper, hence its
image is closed. As this image contains the generic fiber of ${}_{nH}$ (since $u_{s_{0}} : G_{s_{0}} \to H_{s_{0}}$ is
an isomorphism) and ${}_{nH}$ is flat over $S$, hence identical to the closure of its generic fiber, it follows that
${}_{nG} \to {}_{nH}$ is surjective, hence `_nG_0 → _nH_0` is surjective. Recalling that $G_{0} \supset (H_{0})^{0}$ and
applying 7.11, one finds that $G_{0} \to H_{0}$ is surjective, hence $u$ is surjective. One thus obtains:

**Proposition 7.12.** *With the notation of 7.9, suppose conditions (a) and (b) hold, as well as condition (c′)
(stronger than (c)), obtained by requiring that for every integer $n > 0$ (not only of the form $p^{\nu}$), ${}_{nG}'$
be finite over $S'$ and ${}_{nH}'$ separated over $S'$. Under these conditions, $u$ is a closed immersion.*

<!-- label: III.VIII.7.12 -->

<!-- original page 36 -->

**Remark 7.13.** *a) One easily verifies that the separation hypothesis made on the ${}_{nH}$ implies in fact that $H$
is separated over $S$. This is moreover formally contained in 7.12 by taking for $G$ the unit $S$-group. Note also that
when $S$ is locally Noetherian, one may in 7.9 restrict to assuming $H$ locally of finite type over $S$ (in*

<!-- label: III.VIII.7.13 -->

<!-- original page 30 -->

*place of: of finite type over $S$), the proof given applying as it stands; for 7.12 one will moreover assume that the
fibers of $H$ are of finite type.*

*b) Using 7.12, it is not difficult to prove that if $u : G \to H$ is a monomorphism of $S$-preschemes in groups of
finite presentation, with $G$ diagonalizable (or more generally, "of multiplicative type") and $H$ separated over $S$,
then $u$ is a closed immersion — which constitutes a satisfactory generalization of the first conclusion stated in 5.7.
When $G$ is smooth over $S$, it suffices to apply 7.12, and the general case reduces easily to that one. When one no
longer assumes $H$ separated over $S$, one can still show that $u$ is an immersion; in the case where $G$ is a torus,
this fact moreover follows also from what follows.*

*c) When in 7.9 one assumes $G$ has connected fibers, one can in condition 7.9 (c) drop the hypothesis that the
${}_{p^{\nu}}H'$ be separated over $S'$. Indeed, with the reductions made in the proof, one may assume $H$ flat over $S$
and $u$ bijective, hence $H$ with connected fibers, hence $H$ separated over $S$ by virtue of Raynaud's theorem (VI_B
5.5).*[^N.D.E-VIII-41]

## Bibliography

[^N.D.E-VIII-42]

[RG71] M. Raynaud, L. Gruson, *Critères de platitude et de projectivité*, Invent. math. **13** (1971), 1–89.

[TO70] J. Tate, F. Oort, *Group schemes of prime order*, Ann. scient. Éc. Norm. Sup. (4) **3** (1970), 1–21.

______________________________________________________________________

## Footnotes

<!-- LEDGER DELTA — Exposé VIII — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| bidualité | biduality | Section title (§1). |
| réflexif (relativement à I) | reflexive (relative to I) | Definition 1.0; preserved as technical term. |
| anti-équivalence | anti-equivalence | Standard. |
| extension de la base | base extension | Standard. |
| accouplement (de G et G′ à valeurs dans I) | pairing (of G and G′ with values in I) | Standard. |
| morphisme bilinéaire | bilinear morphism | Standard. |
| foncteur-groupe commutatif | commutative group functor | Per Exp. I §2.1. |
| application localement constante | locally constant map | Standard. |
| graduation de type M | M-grading | Standard. |
| facteur direct | direct factor / direct summand | Used "direct factor" to preserve source. |
| descente de la représentabilité | descent of representability | Section heading §1.7. |
| foncteur local | local functor | Standard (sheaf for Zariski). |
| donnée de descente | descent datum | Per SGA 1. |
| donnée de descente effective | effective descent datum | Per SGA 1. |
| topologie (fpqc) | (fpqc) topology | Source uses parentheses; preserved. |
| fidèlement plat et quasi-compact | faithfully flat and quasi-compact | Standard. |
| M-effectif | M-effective | Preserved from Exp. IV §3.4. |
| schéma en groupes commutatifs constant | constant commutative group scheme | Standard. |
| schéma en groupes des racines n-èmes de l'unité | group scheme of n-th roots of unity | `μ_n` notation; standard. |
| caractéristiques résiduelles | residue characteristics | Standard. |
| sous-groupe de torsion | torsion subgroup | Standard. |
| groupe de torsion | torsion group | Standard. |
| transposé (d'un homomorphisme) | transposed (of a homomorphism) | `u^t` for the transposed map. |
| faisceau quotient | quotient sheaf | Standard. |
| (immersion) fermée / ouverte | closed / open (immersion) | Standard. |
| immersion locale | local immersion | Standard. |
| torseur / fibré principal homogène | torsor / principal homogeneous bundle | SGA 3 uses both; preserved. |
| formellement principal homogène | formally principal homogeneous | Standard. |
| algèbre quasi-cohérente graduée de type M | quasi-coherent M-graded algebra | Standard. |
| module inversible | invertible module | Standard. |
| théorème 90 de Hilbert | Hilbert's Theorem 90 | Standard. |
| forme tordue (de G_m) | twisted form (of G_m) | Per glossary. |
| morphisme de norme | norm morphism | Standard. |
| cohomologie galoisienne | Galois cohomology | Standard. |
| morphisme graphe | graph morphism | Standard. |
| essentiellement libre | essentially free | Definition 6.1; standard. |
| quasi-libre | quasi-free | Remark 6.8; preserved as technical coinage. |
| convergence ponctuelle discrète | pointwise convergence (discrete) | Topology on End_A(M). |
| transporteur strict | strict transporter | Per glossary (centralizer / transporter family). |
| normalisateur | normalizer | Per glossary. |
| centralisateur | centralizer | Per glossary. |
| centre | center | Per glossary. |
| automorphismes intérieurs | inner automorphisms | Standard. |
| sous-groupe distingué | normal subgroup | English does not distinguish; not used here. |
| adhérence schématique | schematic closure | Per SGA/EGA. |
| critère valuatif de propreté | valuative criterion of properness | Standard. |
| fibre générique / spéciale | generic / special fiber | Standard. |
| point fermé | closed point | Standard. |
| anneau de valuation discrète | discrete valuation ring | Standard. |
| purement infinitésimal | purely infinitesimal | Standard. |
| morphisme propre | proper morphism | Per glossary. |
| immersion (locale / ouverte / fermée) | (local / open / closed) immersion | Per glossary. |
| de présentation finie | of finite presentation | Per glossary. |
| de type fini | of finite type | Per glossary. |
| « lisse » remplaçant « simple » | "smooth" replacing "simple" | Per N.D.E. terminology update. |
| Frobenius itéré | iterated Frobenius | Standard. |
| sous-groupe radiciel / sous-tore | root subgroup / subtorus | Per glossary. |
| composante connexe de l'élément neutre | connected component of the identity element | Standard `H^0`. |
| groupe divisible | divisible group | Standard. |
| ν-ième puissance / p-ième puissance | ν-th power / p-th power | Standard. |
| groupe additif (G_a) | additive group (G_a) | Standard. |
| anneau local artinien | Artinian local ring | Per glossary. |
| morphisme diagonal | diagonal morphism | Standard. |
| relation de cocycle | cocycle relation | Standard. |
| anneau de valuation | valuation ring | Standard. |
| en bidegré (m,n) | in bidegree (m,n) | Standard. |
-->

[^VIII-0-0]: Version notice of the 2009 re-edition.

[^N.D.E-VIII-1]: N.D.E.: The original has been expanded in what follows.

[^N.D.E-VIII-2]: N.D.E.: We have added the numbering 1.0, 1.0.1, … in order to highlight the definitions and statements
    that occur there.

[^N.D.E-VIII-3]: N.D.E.: We have added the sentence that follows.

[^N.D.E-VIII-4]: N.D.E.: We have expanded what follows.

[^N.D.E-VIII-5]: N.D.E.: Indeed, if one denotes by $F(M)$ (resp. $G(M)$) the left-hand (resp. right-hand) side of (2),
    and if $M = M_{1} \oplus M_{2}$, one has a canonical isomorphism $F(M) = F(M_{1}) \oplus F(M_{2})$, and likewise for
    $G$. This reduces us to verifying that $\theta$ is an isomorphism when $M = \mathbb{Z}/r\mathbb{Z}$, for an integer
    $r \geqslant 0$. In this case, $F(M) = ({}_{rN})_{S}$, where ${}_{rN}$ is the kernel of $r \cdot id_{N}$, and, for
    every $T \to S$, the homomorphism

    ```text
    F(M)(T) = Γ(_rN_T/T) → G(M)(T) = _rΓ(N_T/T)
    ```

    is bijective, whence the desired result.

[^N.D.E-VIII-6]: N.D.E.: The original stated after 1.5: "One concludes more generally that if $G$, $H$ are locally
    diagonalizable, with $H$ of finite type, then $\operatorname{Hom}_{S-gr.}(G, H)$ is representable." We have included
    this assertion in the statement of 1.5, and have made its proof explicit in 1.7.

[^N.D.E-VIII-7]: N.D.E.: One should add a statement 1.5.1 treating the functor $Isom_{S-gr.}(G, H)$, considered in X
    5.10 and 5.11…

[^N.D.E-VIII-8]: N.D.E.: We have added this paragraph, to make explicit the "local on $S$" character of the
    representability of certain sheaves on $S$, used many times in the sequel (and implicitly in the original).

[^N.D.E-VIII-9]: N.D.E.: See also Remark XI 3.4.

[^N.D.E-VIII-10]: N.D.E.: For another effectivity criterion, see later X 5.4–5.6.

[^N.D.E-VIII-11]: N.D.E.: (since $G$ is flat over $S$, by (a)).

[^N.D.E-VIII-12]: N.D.E.: We have added what follows, and have detailed the proof accordingly.

[^N.D.E-VIII-13]: N.D.E.: The original has been expanded in what follows.

[^N.D.E-VIII-14]: N.D.E.: We have added what follows.

[^N.D.E-VIII-15]: N.D.E.: We have corrected 4.1 to 4.2.

[^N.D.E-VIII-16]: N.D.E.: We have expanded the passage that follows.

[^N.D.E-VIII-17]: N.D.E.: We have added the sentence that follows.

[^N.D.E-VIII-18]: N.D.E.: Indeed, for every $b \in A$, $a_{m} \in A_{m}$, one has
    $\theta(b \otimes a_{m}) = b a_{m} \otimes e_{m}$, hence the surjectivity of $\theta$ is equivalent to `(*)`.

[^N.D.E-VIII-19]: N.D.E.: We have denoted by $K$ the ideal denoted $J$ in the original, in order to distinguish it from
    the ideals $J_{p}$ of `A_0` appearing in `(***)`. We have also made explicit later that the relations `(**)` are
    equivalent to the equality $K = K'$ (see what follows).

[^N.D.E-VIII-20]: N.D.E.: It follows from 5.2 that $\sum_{p \neq 0} J_{p} = A_{0}$, hence `1` is written as a finite sum
    $\sum_{i} x_{i}$, with $x_{i} \in J_{p_{i}}$.

[^N.D.E-VIII-21]: N.D.E.: cf. EGA II, 2.7.1 (vi).

[^VIII-6-star]: The present § is independent of the theory of diagonalizable groups; its natural place would be in VI_B.

[^N.D.E-VIII-22]: N.D.E.: One can replace "free" by "projective", cf. 6.8 below. On the other hand, this notion is to be
    compared with that of $S$-prescheme flat and pure, introduced and developed in [RG71]; see in particular *loc.
    cit.*, Part I, 3.3.12 and Part II, 3.1.4.1.

[^N.D.E-VIII-23]: N.D.E.: Indeed, let $(A, m)$ be an Artinian local ring, $k$ its residue field, $M$ an arbitrary
    $A$-module, $(x_{i})_{i \in I}$ elements of $M$ whose images form a basis of $M/mM$ over $k$. Let $F$ be the free
    $A$-module with basis $(e_{i})_{i \in I}$, and $\phi : F \to M$ the $A$-morphism defined by $\phi(e_{i}) = x_{i}$.
    Then $Q = Coker \phi$ satisfies $Q = mQ$, whence, since $m$ is nilpotent, $Q = 0$. Suppose moreover $M$ flat over
    $A$; then $K = Ker \phi$ satisfies $K \otimes_{A} k = 0$, i.e. $K = mK$, whence $K = 0$.

[^N.D.E-VIII-24]: N.D.E.: cf. II.1, where this functor is denoted $\prod_{Z/S} Y$.

[^N.D.E-VIII-25]: N.D.E.: We have corrected "Z" to "S".

[^N.D.E-VIII-26]: N.D.E.: We have expanded the original in what follows; see also 1.7.3.

[^N.D.E-VIII-27]: N.D.E.: We have corrected "S" to "S".

[^N.D.E-VIII-28]: N.D.E.: denoted $Transp^{str}_{G}(Y, Z)$.

[^N.D.E-VIII-29]: N.D.E.: We have kept the numbering of the original: there is no 6.6.

[^N.D.E-VIII-30]: N.D.E.: Indeed, over a field $k$, every subprescheme in groups of $G$ is closed, cf. VI_A, 0.6.1.

[^N.D.E-VIII-31]: N.D.E.: We have expanded the original in what follows; in particular we have added Lemma 6.8.1.

[^N.D.E-VIII-32]: N.D.E.: cf. Exp. VI_A, Theorems 3.2 and 3.3.2.

[^N.D.E-VIII-33]: N.D.E.: take into account the additions made in VI_B…

[^VIII-7-star]: In fact, M. Raynaud has constructed a counter-example, with $G$ smooth with connected fibers, cf. XVI
    1.1 (c). If one does not assume $G$ has connected fibers, one may take $S = \operatorname{Spec}(\mathbb{Z}_{2})$,
    $G = (\mathbb{Z}/2\mathbb{Z})_{S}$ deprived of the non-neutral closed point, $H = (\mu_{2})_{S}$.

[^N.D.E-VIII-34]: N.D.E.: cf. EGA IV₃, § 8, and Exp. VI_B, § 10.

[^N.D.E-VIII-35]: N.D.E.: cf. EGA IV₃, 8.11.5 and 15.7.1.

[^VIII-7-starstar]: Cf. EGA IV₃, 15.7.

[^VIII-7-starstarstar]: Cf. EGA IV₂, 2.8.

[^N.D.E-VIII-36]: N.D.E.: We have suppressed the word "closed".

[^N.D.E-VIII-37]: N.D.E.: Make this explicit in Exp. V and VI_A…

[^N.D.E-VIII-38]: N.D.E.: We have suppressed here the hypothesis that $Q$ be commutative, and have modified 7.3.1
    accordingly. Note that if $Q$ is not commutative, the $n$-th power morphism is not in general a group homomorphism.

[^N.D.E-VIII-39]: N.D.E.: Add this in VII_A — On the other hand, the statement is true for every $S$ if $Q$ is
    commutative, cf. Deligne's theorem in [TO70], p. 4.

[^N.D.E-VIII-40]: N.D.E.: We have updated the terminology, replacing "simple" by "smooth" (see, for example, footnote
    (1) of A. Grothendieck in SGA 1, Exp. II).

[^N.D.E-VIII-41]: N.D.E.: specify in VI_B § 5 this attribution, which appeared in SGAD 1965, indicating the
    modifications between SGAD and Lect. Notes 151.

[^N.D.E-VIII-42]: N.D.E.: additional references cited in this Exposé.
