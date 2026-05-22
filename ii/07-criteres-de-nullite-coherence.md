# Exposé VII. Vanishing criteria and coherence conditions for the sheaves ℰxt^i_Y(F, G)

<!-- label: VII -->

<!-- original page 61 -->

<!-- TRANSLATOR NOTE: Throughout this Exposé, following the convention pinned in Exposé VI, the underlined `Ext^i_Z` of
the source — the sheafified Ext functor on `X` — is rendered with a script-E as `ℰxt^i_Z(F, G)`. The non-underlined
global `Ext^i_Z(X; F, G)` is unchanged. Likewise the sheafified local cohomology functor of Exposé I is `ℋ^i_Y(F)`,
while the global one is `H^i_Y(X, F)`. -->

## 1. Study for $i < n$

<!-- label: VII.1 -->

We prove a lemma.

<!-- original page 77 -->

**Lemma.**

<!-- label: VII.1.1 -->

Let $X$ be a locally noetherian prescheme, $Y$ a closed subset of $X$, and $G$ a quasi-coherent
$\mathcal{O}_{X}$-Module. Suppose that for every coherent $\mathcal{O}_{X}$-Module $F$ with support contained in $Y$,
one has

$$
\mathcal{E}xt^{n-1}(F, G) = 0.
$$

Then for every coherent $\mathcal{O}_{X}$-Module $F$ and every closed subset $Z$ of $X$ such that
$Y \supset Supp F \cap Z$, one has

```text
ℰxt^n_Z(F, G) ≅ ℋom(F, ℋ^n_Y(G)).
```

We first remark that

```text
ℰxt^i_Z(F, G) = ℰxt^i_{Z ∩ Supp F}(F, G)
```

(trivial, cf. Exposé VI). We first carry out the proof for $Z = X$, so that $Supp F \subset Y$. The functor

$$
F \mapsto \mathcal{E}xt^{n}(F, G),
$$

defined on the category of coherent $\mathcal{O}_{X}$-Modules with support contained in $Y$, is left exact. By (IV 1.3),
it is represented by

```text
I = lim_{→ k} ℰxt^n(𝒪_X/𝓘^{k+1}, G),
```

where $\mathcal{I}$ is the ideal of definition of $Y$. Now, by (II 6), one knows that

```text
ℋ^n_Y(G) ≅ lim_{→ k} ℰxt^n(𝒪_X/𝓘^{k+1}, G).
```

Whence the conclusion when $Z = X$. Still by (VI 2.3), one knows that

<!-- original page 78 -->

```text
ℰxt^n_Z(F, G) ≅ lim_{→ k} ℰxt^n(F/𝓙^{k+1}F, G),
```

where $\mathcal{J}$ is the ideal of definition of $Z$. The support of $F/\mathcal{J}^{k+1}F$ is contained in $Y$
whenever $Z \cap Supp F \subset Y$; by what we have just proved, we therefore have

```text
ℰxt^n_Z(F, G) ≅ lim_{→ k} ℋom(F/𝓙^{k+1}F, ℋ^n_Y(G)).
```

It remains to show that the natural homomorphism

```text
lim_{→ k} ℋom(F/𝓙^{k+1}F, ℋ^n_Y(G)) → ℋom(F, ℋ^n_Y(G))
```

is an isomorphism when $Z \cap Supp F \subset Y$. Now $X$ can be covered by noetherian affine open sets; one is thus
reduced to the case where $X$ is noetherian affine. Then $F(X)$ is a finitely generated $\mathcal{O}_{X}(X)$-Module and
$Supp \mathcal{H}^{n}_{Y}(G) \subset Y$. Hence every homomorphism $u: F(X) \to \mathcal{H}^{n}_{Y}(G)(X)$ is annihilated
by a power of $\mathcal{I}$, and therefore by a power of $\mathcal{J}$. QED.

**Proposition.**

<!-- label: VII.1.2 -->

Let $X$ be a locally noetherian prescheme, $Y$ a closed subset of $X$, $G$ a quasi-coherent $\mathcal{O}_{X}$-Module,
and $n$ an integer. For any closed subsets $Z$ and $S$ of $X$ such that $Z \cap S = Y$, the following conditions are
equivalent:

1. <!-- label: VII.1.2.i --> `ℋ^i_Y(G) = 0` for `i < n`;

1. <!-- label: VII.1.2.ii --> there exists a coherent `𝒪_X`-Module `F`, of support `S`, such that

    ```text
    ℰxt^i_Z(F, G) = 0 for i < n;
    ```

1. <!-- label: VII.1.2.iii --> for every coherent `𝒪_X`-Module `F` with support contained in `S` (i.e.

    $Supp F \cap Z = Supp F \cap Y$), one has

    ```text
    ℰxt^i_Z(F, G) = 0 for i < n;
    ```

    <!-- original page 79 -->

1. <!-- label: VII.1.2.iv --> for every coherent `𝒪_X`-Module `F`, one has

    ```text
    ℰxt^i_Y(F, G) = 0 for i < n.
    ```

Moreover, if these conditions hold, then for every coherent $\mathcal{O}_{X}$-Module $F$ and every closed subset $Z'$ of
$X$ such that $Z' \cap Supp F = Y \cap Supp F$, one has isomorphisms

```text
ℰxt^n_Z(F, G) ≅ ℰxt^n_Y(F, G) ≅ ℋom(F, ℋ^n_Y(G)).
```

*Proof.* We argue by induction. The proposition is trivial for $n < 0$. Suppose it has been proved for $n < q$. If one
of the conditions holds for $n = q$, and for two subsets $Z$ and $S$ as stated, then by the induction hypothesis we
have, for every closed subset $Z'$ of $X$ and every coherent $\mathcal{O}_{X}$-Module $F$ such that
$Z' \cap Supp F = Y \cap Supp F$, isomorphisms

```text
ℰxt^{q−1}_{Z'}(F, G) ≅ ℋom(F, ℋ^{q−1}_Y(G)) ≅ ℰxt^{q−1}_Y(F, G).
```

<!-- label: eq:VII.1.1 -->

Hence:

- (i) ⇒ (iv), by taking $Z' = Y$ in (1.1);

- (iv) ⇒ (iii), by taking $Z' = Z$ in (1.1);

- (iii) ⇒ (ii), by taking $F = \mathcal{O}_{S}$;

- (ii) ⇒ (i), by taking $Z' = Z$ in (1.1); this gives $\mathcal{H}om(F, \mathcal{H}^{q-1}_{Y}(G)) = 0$. One then remarks
  that

    <!-- original page 63 -->

    ```text
    Supp ℋ^{q−1}_Y(G) ⊂ Y = Z ∩ S ⊂ S = Supp F,
    ```

    and one applies the following lemma:

**Lemma.**

<!-- label: VII.1.3 -->

Let $X$ be a prescheme, let $P$ be a coherent $\mathcal{O}_{X}$-Module, and let $H$ be a quasi-coherent
$\mathcal{O}_{X}$-Module such that

```text
ℋom(P, H) = 0 and Supp P ⊃ Supp H.
```

Then $H = 0$.

It suffices to prove the lemma when $X$ is affine, since the affine open sets form a base of the topology of $X$ and the
hypotheses are preserved by restriction to an open set.

<!-- original page 80 -->

Now in that case one is reduced to a problem on $A$-modules, where $X = \operatorname{Spec}(A)$. One applies the formula
(valid under the sole hypothesis that $M$ is of finite type)

```text
Ass Hom_A(P, H) = Supp P ∩ Ass H.
```

One knows that `Ass H ⊂ Supp H ⊂ Supp P` and that $Ass \operatorname{Hom}_{A}(P, H) = \emptyset$; hence
$Ass H = \emptyset$, so $H = 0$.

<!-- TRANSLATOR NOTE: The source states the formula `Ass Hom_A(P, H) = Supp P ∩ Ass H` "under the sole hypothesis that
`M` is of finite type"; in context the finite-type module is `P` (the source uses `M` and `P` interchangeably in this
passage). The formula is the standard one for finitely generated `P` over a noetherian ring. -->

To complete the proof of the proposition, it remains to observe that (iv) allows us to apply 1.1.

**Corollary.**

<!-- label: VII.1.4 -->

Let $G$ be a coherent Cohen-Macaulay $\mathcal{O}_{X}$-Module, and let $n \in \mathbb{Z}$. The conditions of 1.2 are
equivalent to:

1. <!-- label: VII.1.2.v -->
    ```text
    codim(Y ∩ Supp G, Supp G) ⩾ n.
    ```

Recall first that an $\mathcal{O}_{X}$-module is said to be Cohen-Macaulay if, for every $x \in X$, the stalk $G_{x}$ is
a Cohen-Macaulay $\mathcal{O}_{X,x}$-module, i.e. one has for every $x \in S = Supp G$:

```text
prof G_x = dim G_x = dim 𝒪_{S,x}.
```

<!-- label: eq:VII.1.2 -->

By Proposition III 3.3, condition (i) of 1.2 is equivalent to

```text
prof_Y G = inf_{x ∈ Y} prof G_x ⩾ n,
```

<!-- label: eq:VII.1.3 -->

and therefore also to

```text
prof_Y G = inf_{x ∈ Y ∩ S} prof G_x ⩾ n,
```

since the depth of a zero module is infinite. Now, by definition,

```text
codim(Y ∩ S, S) = inf_{x ∈ S ∩ Y} dim 𝒪_{S,x},
```

whence the conclusion, by applying formula (1.2).

We shall now prove a result that lets us deduce the coherence conditions we have in view from certain vanishing
criteria.

<!-- original page 81 -->

<!-- original page 64 -->

**Lemma.**

<!-- label: VII.1.5 -->

Let $X$ be a locally noetherian prescheme. Let $T^{\bullet}$ be an exact contravariant $\partial$-functor, defined on
the category of coherent $\mathcal{O}_{X}$-Modules, with values in the category of $\mathcal{O}_{X}$-Modules. Let $Y$ be
a closed subset of $X$. Let $i \in \mathbb{Z}$. Suppose that, for every coherent $\mathcal{O}_{X}$-Module with support
contained in $Y$, $T^{i} F$ and $T^{i-1} F$ are coherent. Let $F$ be a coherent $\mathcal{O}_{X}$-Module. For $T^{i} F$
to be coherent, it is necessary and sufficient that $T^{i} F''$ be coherent, where we have set

$$
F'' = F/\Gamma_{Y}(F).
$$

Indeed, $F' = \Gamma_{Y}(F)$ is coherent because $X$ is locally noetherian; the cohomology exact sequence of
$T^{\bullet}$ then gives

```text
T^{i−1} F' → T^i F'' → T^i F → T^i F',
```

where the outer terms are coherent, whence the conclusion.

**Lemma.**

<!-- label: VII.1.6 -->

If $F$ and $G$ are coherent, and if $Supp F \subset Y$, then $\mathcal{E}xt^{i}_{Y}(F, G)$ is coherent.

Indeed, $\mathcal{E}xt^{i}_{Y}(F, G)$ is isomorphic to $\mathcal{E}xt^{i}(F, G)$; this is valid, moreover, on any ringed
space $X$: if $Z$ is a closed subset containing $Y \cap Supp F$, then $\mathcal{E}xt^{i}_{Z}(F, G)$ is isomorphic to
$\mathcal{E}xt^{i}_{Y}(F, G)$ (cf. Exposé VI).

**Proposition.**

<!-- label: VII.1.7 -->

Suppose $F$ and $G$ are coherent, and set $S = Supp F$, $S' = S \cap (X - Y)$. Suppose that, for every
$x \in Y \cap S'$, one has $prof G_{x} \geqslant n$. Then $\mathcal{E}xt^{i}_{Y}(F, G)$ is coherent for $i < n$.

Indeed, 1.6 allows us to apply 1.5 to $T^{\bullet}(F) = \mathcal{E}xt^{\bullet}_{Y}(F, G)$. Setting
$F'' = F/\Gamma_{Y}(F)$, one sees that $Supp F'' = S'$. Now, by III 3.3, the hypothesis on the depth of $G$ ensures the
vanishing of $\mathcal{H}^{i}_{Y \cap S'}(G)$ for $i < n$; by 1.2, one deduces the vanishing of $T^{i} F''$ for $i < n$,
whence the conclusion by 1.5.

## 2. Study for $i > n$

<!-- label: VII.2 -->

<!-- original page 82 -->

Let $X$ be a locally noetherian regular prescheme, that is, one all of whose local rings are regular. Let $Y$ be a
closed subset of $X$. Let $F$ and $G$ be two coherent $\mathcal{O}_{X}$-Modules. Set $S = Supp F$,
$S' = S \cap (X - Y)$. Set

```text
m = sup_{x ∈ Y ∩ S} dim 𝒪_{X,x},
n = sup_{x ∈ Y ∩ S'} dim 𝒪_{X,x};
```

one has $n \leqslant m$.

**Proposition.**

<!-- label: VII.2.1 -->

In the situation just described, one has:

1. $\mathcal{E}xt^{i}_{Y}(F, G) = 0$ for $i > m$,
1. $\mathcal{E}xt^{i}_{Y}(F, G)$ is coherent for $i > n$.

<!-- original page 65 -->

Note first that $\mathcal{E}xt^{i}_{Y}(F, G)$ is coherent for every $i$ when $Supp F \subset Y$. Moreover, setting
$F'' = F/\Gamma_{Y}(F)$ as above, one sees that $Supp F'' = S'$, so that (2) follows from (1) and from 1.3.

<!-- TRANSLATOR NOTE: The source reference here reads "1.3" (= Lemma VII.1.3) but the argument actually invokes Lemma
VII.1.5 to swap `F` for `F''`. We have preserved the source's "1.3"; readers checking the proof should compare 1.5. -->

To prove (1), one first remarks that

```text
ℰxt^i_Y(F, G) ≅ lim_{→ k} ℰxt^i(F/𝓙^k F, G),
```

where $\mathcal{J}$ is the ideal of definition of $Y$. On the other hand, it follows from Theorem 4.2.2 of (A.
Grothendieck, "Sur quelques points d'algèbre homologique", *Tôhoku Mathematical Journal* **9** (1957), pp. 119–221) that
the Ext sheaves commute with the formation of stalks, at least when $X$ is a locally noetherian prescheme and the first
argument is coherent; since the same is true of direct limits, one finds isomorphisms

```text
(ℰxt^i_Y(F, G))_x ≅ lim_{→ k} Ext^i_{𝒪_{X,x}}((F/𝓙^k F)_x, G_x)
```

for every $x \in X$. Since $Supp \mathcal{E}xt^{i}_{Y}(F, G) \subset S \cap Y$, to conclude it suffices to remark that
$x \in Y \cap S$ entails $\dim \mathcal{O}_{X,x} \leqslant m$, hence

<!-- original page 83 -->

```text
Ext^i_{𝒪_{X,x}}((F/𝓙^k F)_x, G_x) = 0 for i > m,
```

since the global cohomological dimension of a regular local ring is equal to its dimension.[^VII-2-1]

Let $X$ be a locally noetherian prescheme; for every subset $P$ of $X$, set

```text
D(P) = { dim 𝒪_{X,p} | p ∈ P }.
```

**Lemma.**

<!-- label: VII.2.2 -->

If $P$ is the underlying space of a connected subprescheme of $X$, then $D(P)$ is an interval.

<!-- TRANSLATOR NOTE: The source reads "sous-préschéma connexe de A"; the symbol "A" is almost certainly an OCR slip
for "X" — the lemma is about subpreschemes of the ambient `X` of the section. We render it as `X`. -->

Indeed, let $\alpha$ and $\beta$ belong to $D(P)$, corresponding to points $p$ and $q$ of $P$. We show that there exists
a sequence of points of $P$, $(p = p_{1}, \cdots, p_{n} = q)$, such that for $1 \leqslant i < n$ one has
$|\dim \mathcal{O}_{X,p_{i}} - \dim \mathcal{O}_{X,p_{i+1}}| = 1$; it will follow that $D(P)$ contains the interval
$[\alpha, \beta]$. For this, one remarks that $p$ and $q$ can be joined by a chain of irreducible components of $P$ such
that two successive components meet. One is reduced to the case where $p$ is the generic point of an irreducible
component $Q$ of $P$, and where $q \in Q$, and so $q \supset p$ as ideals of $\mathcal{O}_{q}$, where the assertion is
trivial from the definition of dimension.

<!-- TRANSLATOR NOTE: The source displayed equation reads `dim 𝒪_{X,p_i} − dim 𝒪_{X,p_{i+1}} = 1`, but for the
argument to give an interval-filling chain one needs unit jumps in either direction; we read this as an absolute value
and have rendered it `| … | = 1`. The source also writes the interval as `[p, q]` where `[α, β]` is intended. -->

**Proposition.**

<!-- label: VII.2.3 -->

Let $X$ be a locally noetherian regular prescheme, $Y$ a closed subset of $X$, and $F$ a coherent
$\mathcal{O}_{X}$-Module. Let $P = Y \cap Supp F \cap (X - Y)$. Let $n \in \mathbb{Z}$, and suppose that
$n \notin D(P)$. Then $\mathcal{E}xt^{n}_{Y}(F, \mathcal{O}_{X})$ is coherent.

<!-- original page 66 -->

The conclusion is local and the hypotheses are preserved by restriction to an open set. Now $P$ is closed and so locally
noetherian, hence locally connected; we may therefore assume $X$ affine and noetherian, and $P$ connected. Set
`D(P) = [a, b[`, which is legitimate by the preceding lemma. If $n > b$, we conclude by 2.1; if $n < a$, then
$n < \dim \mathcal{O}_{X,x} = prof \mathcal{O}_{X,x}$ for every $x \in P$, and we conclude by 1.7.

<!-- TRANSLATOR NOTE: The source defines `P = Y ∩ Supp F ∩ (X − Y)`, which is empty as written; the intended set is
almost certainly the closure intersection that appears in §1, e.g. `P = Supp F ∩ (closure of (Supp F ∩ (X − Y)))` or
`P = Y ∩ (Supp F ∩ closure …)`, depending on parsing. We have kept the source's expression literally and flagged it
here. The proof below works for any closed `P ⊂ Y ∩ Supp F` on which the dimension function is bounded by an interval
`[a, b[`. -->

## Translation ledger delta

| French                               | English                            | Note                                                                                                        |
| ------------------------------------ | ---------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| critères de nullité                  | vanishing criteria                 | Title-level. Per task spec.                                                                                 |
| conditions de cohérence              | coherence conditions               | Title-level. Per task spec.                                                                                 |
| $Ext^{i}_{Y}(F, G)$ (underlined)     | $\mathcal{E}xt^{i}_{Y}(F, G)$      | Sheafified Ext, per the script-E convention pinned in Exposé VI.                                            |
| $Ext^{i}_{Z}(F, G)$ (non-underlined) | $Ext^{i}_{Z}(X; F, G)$             | Global Ext (when displayed with the ambient $X$); unchanged.                                                |
| `Hom` (underlined)                   | $\mathcal{H}om$                    | Sheaf-Hom, parallel to the $\mathcal{E}xt$ convention.                                                      |
| $H^{i}_{Y}$ (underlined)             | $\mathcal{H}^{i}_{Y}$              | Sheafified local cohomology, matching the glossary entry.                                                   |
| $\Gamma_{Y}(F)$ (underlined)         | $\Gamma_{Y}(F)$                    | Sheafified sections-with-support; rendered without underline per the SGA 2 glossary's note on $\Gamma_{Z}$. |
| $\partial-foncteur$                  | $\partial$-functor                 | Standard.                                                                                                   |
| profondeur (`prof`)                  | depth (`prof`)                     | Standard SGA 2 usage; symbol `prof` kept.                                                                   |
| anneau de Cohen-Macaulay             | Cohen-Macaulay (ring / module)     | Standard.                                                                                                   |
| dimension cohomologique globale      | global cohomological dimension     | Per source.                                                                                                 |
| limite inductive                     | direct limit                       | Modern English; matches glossary policy for SGA 2.                                                          |
| Tôhoku                               | *Tôhoku*                           | Italicized journal title; accent restored.                                                                  |
| il est licite de                     | it is legitimate to                | "Legitimate" reads better than "permitted" in this register.                                                |
| quelles que soient $Z$ et $S$        | for any closed subsets $Z$ and $S$ | Re-articulated as English universal quantifier.                                                             |
| C.Q.F.D.                             | QED                                | Standard.                                                                                                   |
| en vertu de                          | by                                 | "By" suffices for a citation tag.                                                                           |
| compte tenu de                       | (not occurring)                    | —                                                                                                           |
| il en résulte                        | it follows                         | Standard.                                                                                                   |
| toujours d'après                     | still by                           | Standard.                                                                                                   |
| $7\to$, $-\to$, $\sim=$              | $\mapsto$, $\to$, $\cong$          | OCR repair, per the SGA 2 glossary.                                                                         |

[^VII-2-1]: Cf. EGA 0_IV 17.3.1.
