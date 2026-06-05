# Exposé III. Cohomological invariants and depth

<!-- label: III -->

<!-- original page 27 -->

## 1. Review

<!-- label: III.1 -->

We state a few definitions and results that the reader will find, for example, in Chapter I of the course taught by
J.-P. Serre at the Collège de France in 1957–58.[^N.D.E-III-1]

**Definition.**

<!-- label: III.1.1 -->

Let $A$ be a ring (commutative with unit element, as in everything that follows) and let $M$ be an $A$-module (unitary,
as in everything that follows). One calls:

- *annihilator of $M$*, denoted `Ann M`, the set of $a \in A$ such that $am = 0$ for every $m \in M$.
- *support of $M$*, denoted `Supp M`, the set of prime ideals $p$ of $A$ such that the localization $M_{p}$ is nonzero.
- *"assassin of $M$"* or *"set of prime ideals associated with $M$"*, denoted `Ass M`, the set of prime ideals $p$ of
  $A$ such that there exists a nonzero element of $M$ whose annihilator is $p$.

If $a$ is an ideal of $A$, we shall write $r(a)$ for the radical of $a$ in $A$, i.e. the set of elements of $A$ some
power of which lies in $a$.

The following results hold under the assumption that $A$ is noetherian and $M$ is finitely generated.

**Proposition.**

<!-- label: III.1.1bis -->

1. `Ass M` is a finite set.
1. <!-- original page 28 -->
    For an element of $A$ to annihilate a nonzero element of $M$, it is necessary and sufficient that it belong to one of
    the ideals associated with $M$.
1. The radical of the annihilator of $M$, $r(Ann M)$, is the intersection of the ideals associated with $M$ that are
   minimal (for the inclusion relation in `Ass M`).

<!-- TRANSLATOR NOTE: The source labels both the definition and the proposition that follows as "Proposition 1.1"; we
preserve the duplication and tag the second one *bis* in the spirit of the editor's note on numbering (cf. Introduction,
N.D.E. intro-1). The third assertion of this proposition is given as item (iii) in the source. -->

**Proposition.**

<!-- label: III.1.2 -->

Let $p$ be a prime ideal of $A$. The following assertions are equivalent:

1. $p \in Supp M$.
1. There exists $q \in Ass M$ such that $q \subset p$.
1. $p \supset Ann M$.
1. (iii bis) $p \supset r(Ann M)$.

**Proposition.**

<!-- label: III.1.3 -->

Let $N$ be a finitely generated $A$-module. One has the formula:

```text
Ass Hom_A(N, M) = Supp N ∩ Ass M.
```

## 2. Depth

<!-- label: III.2 -->

Throughout this paragraph, $A$ denotes a commutative ring, $I$ an ideal of $A$, and $M$, $N$ two $A$-modules. We write
$X$ for the prime spectrum of $A$ (we shall not use its structure sheaf in this paragraph) and $Y$ for the variety of
$I$, $Y = Supp(A/I) = {p \in X, p \supset I}$.

**Lemma.**

<!-- label: III.2.1 -->

Suppose that $A$ is noetherian and that the modules $M$ and $N$ are finitely generated. Suppose moreover that $Supp N =
Y$. Then the following assertions are equivalent:

1. $\operatorname{Hom}_{A}(N, M) = 0$.
1. $Supp N \cap Ass M = \emptyset$.
1. The ideal $I$ is not a zero divisor on $M$, meaning that for every $m \in M$, $Im = 0$ implies $m = 0$.
1. There exists an $M$-regular element in $I$. (An element $a$ of $A$ is said to be *$M$-regular* if multiplication by
   $a$ on $M$ is injective.)
1. For every $p \in Y$, the maximal ideal $pA_{p}$ of the local ring $A_{p}$ is not associated with $M_{p}$. In symbols:
   $pA_{p} \notin Ass M_{p}$.

*Proof.*

<!-- original page 29 -->

(i) ⇔ (ii), since $Ass \operatorname{Hom}_{A}(N, M) = \emptyset$ is equivalent to (ii) by Proposition 1.3, and to (i) by
an easy consequence of Proposition 1.2.

(iii) ⇒ (ii) by contradiction: "there exists $p \in Supp N \cap Ass M$" entails that $p \supset I$ and that there exists
$m \in M$ whose annihilator is $p$, hence $Im \subset pm = 0$, contradicting (iii).

(iv) ⇒ (iii) trivially.

(ii) ⇔ (iv), since $Supp N = Y$, so (ii) says that $I$ is contained in no ideal associated with $M$, or equivalently
(since the ideals associated with $M$ are prime and finite in number) that $I$ is not contained in the union of the
ideals associated with $M$. But by Proposition 1.1 (ii) this union is exactly the set of elements of $A$ that are not
$M$-regular.

(i) ⇒ (v): indeed, if $\operatorname{Hom}_{A}(N, M) = 0$ and if $p \in Y$, one deduces, by virtue of the formula

```text
Hom_A(N, M)_p = Hom_{A_p}(N_p, M_p),
```

that $\operatorname{Hom}_{A_{p}}(N_{p}, M_{p}) = 0$, hence, thanks to Proposition 1.3,

```text
Supp N_p ∩ Ass M_p = ∅;
```

but $pA_{p} \in Supp N_{p}$, so $pA_{p} \notin Ass M_{p}$.

(v) ⇒ (i): indeed, if $p \in Ass M$, there exists $m \in M$ whose annihilator is $p$, so the canonical image of $m$ in
$M_{p}$ is nonzero, and its annihilator is an ideal containing $p$, hence containing $pA_{p}$, hence equal to $pA_{p}$.
The ideal $pA_{p}$ is therefore associated with $M_{p}$, so $p \notin Y$ by (v), whence (i). QED

We shall now work with these conditions, replacing the functor `Hom` by its derived functors.

**Theorem.**

<!-- label: III.2.2 -->

<!-- original page 30 -->

Let $A$ be a commutative ring, $I$ an ideal of $A$, $M$ an $A$-module. Let $n$ be an integer.

a) If there exists a sequence $f_{1}, \cdots, f_{n+1}$ of elements of $I$ that is an $M$-regular sequence (i.e. $f_{1}$
is $M$-regular and $f_{i+1}$ is regular on $M/(f_{1}, \cdots, f_{i})M$ for $i \leqslant n$), then for every $A$-module
$N$ annihilated by a power of $I$, one has:

```text
Ext^i_A(N, M) = 0 for i ⩽ n.
```

b) If moreover $A$ is noetherian, $M$ is finitely generated, and there exists a finitely generated $A$-module $N$ such
that $Supp N = V(I)$ and $Ext^{i}_{A}(N, M) = 0$ for $i \leqslant n$, then there exists a sequence $f_{1}, \cdots,
f_{n+1}$ of elements of $I$ that is $M$-regular.

Let us prove a) first, by induction. If $n < 0$ the statement is empty.

Suppose $n \geqslant 0$, and that a) has been proved for $n' < n$. By hypothesis there exists $f_{1} \in I$ that is
$M$-regular. Denote by $f^{i}_{1}$ multiplication by $f_{1}$ on $Ext^{i}_{A}(N, M)$, and by $f^{M}_{1}$ multiplication
by $f_{1}$ on $M$. The sequence

```text
0 ⟶ M ──f_1^M──→ M ⟶ M/f_1 M ⟶ 0
```

<!-- label: eq:III.2.1 -->

is exact, hence so is the sequence:

```text
Ext^{i−1}_A(N, M/f_1 M) ──δ──→ Ext^i_A(N, M) ──f_1^i──→ Ext^i_A(N, M).
```

By hypothesis $I^{r} N = 0$, so $f^{0}_{1}$ is nilpotent; since $Ext^{i}$ is a universal functor, the same holds for
$f^{i}_{1}$ for every $i$. On the other hand, there is a regular sequence in $M/f_{1} M$ of length $n$, so by the
induction hypothesis,

```text
Ext^{i−1}_A(N, M) = 0 if i ⩽ n − 1.
```

<!-- TRANSLATOR NOTE: The source displays `Ext^{i−1}_A(N, M) = 0` here, but the intended module is `M/f_1 M`. We retain
the source as printed; the argument that follows uses what the induction hypothesis provides, namely vanishing for
`M/f_1 M`. -->

One deduces that if $i \leqslant n$, then $f^{i}_{1}$ is at once nilpotent and injective, hence $Ext^{i}_{A}(N, M) = 0$.

Let us prove b), also by induction. If $n < 0$, the statement is empty.

<!-- original page 31 -->

If $n = 0$, b) follows from the implication (i) ⇒ (iv) of Lemma 2.1.

If $n > 0$, by b) for $n = 0$ there exists an element $f_{1} \in I$ that is $M$-regular; from the exact sequence (2.1)
one deduces the exact sequence:

```text
Ext^{i−1}_A(N, M) ⟶ Ext^{i−1}_A(N, M/f_1 M) ⟶ Ext^i_A(N, M).
```

<!-- label: eq:III.2.2 -->

One concludes that the hypotheses of b) are satisfied for the module $M/f_{1} M$ and the integer $n - 1$. By the
induction hypothesis, there exists a sequence of $n$ elements of $I$ that is $M/f_{1} M$-regular, which entails that
there exists a sequence of $n + 1$ elements of $I$, beginning with $f_{1}$, that is $M$-regular.

This theorem invites us to generalize, as follows, the classical definition of the depth of a finitely generated module
over a noetherian ring:

**Definition.**

<!-- label: III.2.3 -->

Let $A$ be a commutative ring with unit, $M$ an $A$-module, $I$ an ideal of $A$. One calls the *$I$-depth of $M$*, and
denotes $prof_{I} M$, the supremum in $\mathbb{N} \cup {+\infty}$ of the set of natural integers $n$ such that for every
finitely generated $A$-module $N$ annihilated by a power of $I$, one has

```text
Ext^i_A(N, M) = 0 for every i < n.
```

One deduces from the previous theorem that if $n$ is the supremum of the lengths of $M$-regular sequences of elements of
$I$, one has $n \leqslant prof_{I} M$. More precisely:

**Proposition.**

<!-- label: III.2.4 -->

Let $A$ be a commutative ring, $I$ an ideal of $A$, $M$ an $A$-module, and $n \in \mathbb{N}$. Consider the assertions:

1. $n \leqslant prof_{I} M$.

1. For every finitely generated $A$-module $N$ annihilated by a power of $I$, one has:

    ```text
    Ext^i_A(N, M) = 0 for i < n.
    ```

1. <!-- original page 32 -->

    There exists a finitely generated $A$-module $N$ such that $Supp N = V(I)$ and $Ext^{i}_{A}(N, M) = 0$ for $i < n$.

1. There exists an $M$-regular sequence of length $n$ formed of elements of $I$.

The following logical implications hold:

```text
(1) ⇐⇒ (2)
        ⇓
       (3) ⇐= (4)
```

<!-- TRANSLATOR NOTE: The source's implication diagram shows (1) ⇔ (2), (2) ⇒ (3), and (4) ⇒ (2); we render this as a
two-line ASCII diagram. -->

Moreover, if $A$ is noetherian and $M$ is finitely generated, these conditions are equivalent.

*Proof.*

(1) ⇔ (2) by definition, and (2) ⇒ (3) by taking $N = A/I$. Moreover (4) ⇒ (2) by Theorem 2.2 a). Finally, if $A$ is
noetherian and $M$ is finitely generated, (3) ⇒ (4) by Theorem 2.2 b).

We assume $A$ noetherian and $M$ finitely generated until the end of this paragraph.

**Corollary.**

<!-- label: III.2.5 -->

Let $f \in I$ be an $M$-regular element. One has:

```text
prof_I M = prof_I(M/f M) + 1.
```

Indeed, if $n \leqslant prof_{I}(M/f M)$, there exists a sequence of elements of $I$, $f_{1}, \cdots, f_{n}$, that is
$(M/f M)$-regular, so the sequence $f, f_{1}, \cdots, f_{n}$ is $M$-regular, hence $n + 1 \leqslant prof_{I} M$, hence
$prof_{I} M \geqslant prof_{I}(M/f M) + 1$. On the other hand, by the exact sequence (2.2), if $i \leqslant prof_{I} M$
one has $Ext^{i-1}_{A}(N, M/f M) = 0$, hence $prof_{I} M - 1 \leqslant prof_{I}(M/f M)$.

**Corollary.**

<!-- label: III.2.6 -->

Every finite $M$-regular sequence formed of elements of $I$ may be extended to a maximal $M$-regular sequence, whose
length is necessarily equal to the $I$-depth of $M$.

**Remark.**

<!-- label: III.2.7 -->

<!-- original page 33 -->

One can scarcely keep oneself from saying that an $A$-module is the more beautiful the greater its depth. A module whose
support does not meet $V(I)$ is among the most beautiful; indeed, one can show that for $prof_{I} M$ to be finite, it is
necessary and sufficient that $Supp M \cap V(I) \neq \emptyset$.

**Remark.**

<!-- label: III.2.8 -->

If $A$ is a semi-local ring, let $r(A)$ be its radical and $k = A/r(A)$ its residue ring. The interesting notion of
depth is obtained by taking for $I$ the radical of $A$. We shall therefore agree to write simply `prof M` for the
$r(A)$-depth of an $A$-module $M$. One recovers in this case the notion of *homological codimension* (cf. Serre, op.
cit. note [^N.D.E-III-1], p. 21), denoted $codh_{A} M$, defined as the infimum of integers $i$ such that $Ext^{i}_{A}(k,
M) \neq 0$; indeed $Supp k = V(r(A))$.

**Proposition.**

<!-- label: III.2.9 -->

If $A$ is noetherian and $M$ is finitely generated, one has:

```text
prof_I M = inf_{p ∈ V(I)} prof M_p.
```

**Corollary.**

<!-- label: III.2.10 -->

If $A$ is a noetherian semi-local ring and $M$ is a finitely generated $A$-module, one has:

```text
prof M = inf_m prof M_m,
```

where $m$ ranges over the maximal ideals of $A$.

The corollary follows at once from Proposition 2.9; indeed, the prime ideals that contain the radical are precisely the
maximal ideals.

Moreover, let $f \in I$. If $f$ is $M$-regular, if $p \in X$ and $p \supset I$, then the image $g$ of $f$ in $A_{p}$
lies in $pA_{p}$, the maximal ideal of $A_{p}$; and $g$ is $M_{p}$-regular, as follows from the exact sequence

```text
0 ⟶ M_p ──g′──→ M_p ⟶ (M/f M)_p ⟶ 0,
```

<!-- label: eq:III.2.3 -->

where $g'$ denotes multiplication by $g$ on $M_{p}$. This exact sequence also gives that $(M/f M)_{p}$ is isomorphic to
$M_{p}/gM_{p}$; applying Corollary 2.5 to $M$ and to $M_{p}$, one deduces, by induction, that $prof_{I} M \leqslant
\nu(M)$, where one has set, for every $M$:

<!-- original page 34 -->

```text
ν(M) = inf_{p ∈ V(I)} prof M_p.
```

More precisely, still by induction, one knows that if $f$ is $M$-regular, then $\nu(M) = \nu(M/f M) + 1$; it remains
therefore to show that if $\nu(M) \geqslant 1$, there exists an $M$-regular element in $I$. But applying Lemma 2.1 to
$M_{p}$, $A_{p}$, and $pA_{p}$ for each $p \in V(I)$, one sees that $pA_{p} \notin Ass M_{p}$; hence, applying Lemma 2.1
to $A$, $M$, and $I$, the conclusion follows.

**Proposition.**

<!-- label: III.2.11 -->

Let $u: A \to B$ be a homomorphism of noetherian rings. Let $I$ be an ideal of $A$, $M$ a finitely generated $A$-module.
Set $IB = I \otimes_{A} B$ and $M_{B} = M \otimes_{A} B$. If $B$ is $A$-flat, one has:

```text
prof_{IB} M_B ⩾ prof_I M;
```

moreover, if $B$ is faithfully flat over $A$, one has equality.

Indeed, let $N = A/I$. By flatness, $N \otimes_{A} B = B/IB$; set $N_{B} = N \otimes_{A} B$. Again by flatness and the
noetherian hypotheses, one has:

```text
Ext^i_B(N_B, M_B) = Ext^i_A(N, M) ⊗_A B,
```

so $Ext^{i}_{A}(N, M) = 0$ implies $Ext^{i}_{B}(N_{B}, M_{B}) = 0$, and the converse holds if $B$ is faithfully flat
over $A$.

## 3. Depth and topological properties

<!-- label: III.3 -->

**Lemma.**

<!-- label: III.3.1 -->

Let $X$ be a topological space, $Y$ a closed subspace, $F$ a sheaf of abelian groups on $X$. Set $U = X - Y$. Let $n$ be
an integer. The following conditions are equivalent:

1. <!-- original page 35 -->

    $H^{i}_{Y}(X, F) = 0$ for $i < n$.

1. For every open $V$ of $X$, the homomorphism of groups

    ```text
    H^i(V, F) ⟶ H^i(V ∩ U, F)
    ```

    is bijective for $i < n - 1$ and injective for $i = n - 1$.

1. For every open $V$ of $X$,

    ```text
    H^i_{Y ∩ V}(V, F|V) = 0 for i < n.
    ```

*Proof.*

(ii) ⇔ (iii): indeed, let $V$ be an open of $X$, set $X' = V$, $Y' = Y \cap V$, $F' = F|V$, $U' = X' - Y'$. Then $Y'$ is
closed in $X'$, so one has an exact sequence:

```text
H^i_{Y′}(X′, F′) ⟶ H^i(X′, F′) ──ρ^i──→ H^i(U′, F′) ⟶ H^{i+1}_{Y′}(X′, F′).
```

If the outer terms vanish, the homomorphism $\rho^{i}$ is bijective; and if the left-hand term vanishes, $\rho^{i}$ is
injective. So (iii) ⇒ (ii). Conversely, if $i < n$, then $H^{i}_{Y'}(X', F')$ vanishes because $\rho^{i}$ is injective
and $\rho^{i-1}$ is surjective.

(i) ⇒ (iii): indeed, the "local-to-global" spectral sequence gives:

```text
H^p(X, ℋ^q_Y(X, F)) ⟹ H^*_Y(X, F).
```

<!-- TRANSLATOR NOTE: The source writes `H^q_Y(X, F)` for the sheafified `ℋ^q_Y(F)` (the underline is lost by OCR). The
abutment is `H^*_Y(X, F)`; per the SGA 2 conventions adopted for this translation, the sheafified functor on the
spectral sequence's `E_2` page is rendered with script `ℋ`. -->

Now, by hypothesis $\mathcal{H}^{q}_{Y}(X, F) = 0$ for $q < n$, hence $H^{p+q}_{Y}(X, F) = 0$ for $p + q < n$.

(iii) ⇒ (i): indeed, (iii) says that the presheaf

```text
V ⟼ H^i_{Y ∩ V}(V, F|V)
```

is zero, hence so is the associated sheaf, which is $\mathcal{H}^{i}_{Y}(X, F)$, since $Y$ is closed.

**Remark.**

<!-- label: III.3.2 -->

<!-- original page 36 -->

The equivalence of (i) and (ii) was proved in Proposition I 2.13. As remarked there, if $n \geqslant 2$, one may omit
the condition that $\rho^{n-1}$ be injective.[^N.D.E-III-2]

**Proposition.**

<!-- label: III.3.3 -->

Let $X$ be a locally noetherian prescheme, $Y$ a closed subprescheme of $X$, and $F$ a coherent
$\mathcal{O}_{X}$-module. The conditions of Lemma 3.1 are equivalent to each of the following:

1. (iv) For every $x \in Y$, one has $prof F_{x} \geqslant n$.

1. (v) For every coherent $\mathcal{O}_{X}$-module $G$ on $X$ whose support is contained in $Y$, one has

    ```text
    Ext^i_{𝒪_X}(G, F) = 0 for i < n;
    ```

1. (vi) There exists a coherent $\mathcal{O}_{X}$-module $G$ whose support is equal to $Y$ such that

    ```text
    Ext^i_{𝒪_X}(G, F) = 0 for i < n.
    ```

If $X$ is affine, all the work has been done (cf. Proposition 2.4) to establish the equivalence of the three conditions
of Proposition 3.3. These conditions are local, except for the implication (v) ⇒ (vi); but in that case one may take $G
= \mathcal{O}_{Y}$ and invoke Proposition 2.4 again. It therefore suffices to prove (i) ⇒ (vi) and (v) ⇒ (i).

Let $J$ be the ideal of $Y$: it is a coherent sheaf of ideals. Set $\mathcal{O}^{m}_{Y} = \mathcal{O}_{X}/J^{m+1}$: this
is a coherent $\mathcal{O}_{X}$-module whose support is equal to $Y$, and one knows (Theorem II 6.b) that

```text
ℋ^i_Y(X, F) = lim_{→ m} Ext^i_{𝒪_X}(𝒪_Y^m, F),
```

<!-- TRANSLATOR NOTE: The source writes `H^i_Y(X, F)` here for the sheafified Ext-limit; per the convention adopted in
this translation, the sheafified version is rendered as `ℋ^i_Y`. -->

so (v) ⇒ (i). Moreover, the transition morphisms in the projective system of the $\mathcal{O}^{m}_{Y}$ are epimorphisms.

<!-- original page 37 -->

If the functor $Ext^{i}$ is left exact in its first argument — at least when this argument is taken in the category of
coherent $\mathcal{O}_{X}$-modules with support contained in $Y$ — then the transition morphisms of the inductive system
obtained by applying $Ext^{i}$ to the $\mathcal{O}^{m}_{Y}$ will be injective; but (i) entails that the limit is zero,
so (i) will entail that the modules $Ext^{i}_{\mathcal{O}_{X}}(\mathcal{O}^{m}_{Y}, F)$ are zero for every $m$. We argue
by induction. The statement is trivial for $n < 0$. Suppose (i) ⇒ (vi) for $n < q$, then (i) ⇒ (v), so, by the long
exact sequence of `Ext`, $Ext^{q}$ is left exact in its first argument, hence the modules
$Ext^{q}_{\mathcal{O}_{X}}(\mathcal{O}^{m}_{Y}, F)$ are zero for every $m$. So (i) ⇒ (vi) for $n \leqslant q$. QED

**Example.**

<!-- label: III.3.4 -->

Let $A$ be a noetherian local ring, $m$ its maximal ideal, $M$ a finitely generated $A$-module, and $n$ an integer. Set
$X = \operatorname{Spec}(A)$, $Y = {m}$, $U = X - Y$. Let $F$ be the sheaf associated with $M$. The following conditions
are equivalent:

1. $prof M \geqslant n$.

1. The natural homomorphism

    ```text
    H^i(X, F) ⟶ H^i(U, F)
    ```

    is injective for $i = n - 1$ and bijective for $i < n - 1$.

1. $Ext^{i}_{A}(k, M) = 0$ for $i < n$, where $k = A/m$.

1. $H^{i}_{Y}(X, F) = 0$ for $i < n$.

Taking Remark 3.2 into account, one obtains:

**Corollary.**

<!-- label: III.3.5 -->

Let $X$ be a locally noetherian prescheme, $Y$ a closed subprescheme of $X$, $F$ a coherent $\mathcal{O}_{X}$-module.
The following conditions are equivalent:

1. For every $x \in Y$, $prof F_{x} \geqslant 2$.

1. <!-- original page 38 -->

    For every open $V$ of $X$, the natural homomorphism

    ```text
    H^0(V, F) ⟶ H^0(V ∩ (X − Y), F)
    ```

    is bijective.

**Theorem (Hartshorne).**

<!-- label: III.3.6 -->

Let $X$ be a locally noetherian prescheme, $Y$ a closed subprescheme of $X$. Suppose that, for every $x \in Y$, $prof
\mathcal{O}_{X,x} \geqslant 2$; then the natural map

$$ \pi_{0}(X) \longrightarrow \pi_{0}(X - Y) $$

is bijective.

*Proof.* Since $X$ is locally noetherian, $X$ is locally connected; it therefore suffices to prove that for $X$ to be
connected it is necessary and sufficient that $X - Y$ be. Now, for a ringed space in local rings $(X, \mathcal{O}_{X})$
to be connected, it is necessary and sufficient that $H^{0}(X, \mathcal{O}_{X})$ not be a direct product of two nonzero
rings. But the hypothesis implies, by Corollary 3.5 applied to $F = \mathcal{O}_{X}$, that the homomorphism

```text
H^0(X, 𝒪_X) ⟶ H^0(X − Y, 𝒪_X)
```

is an isomorphism, whence the conclusion.

**Corollary.**

<!-- label: III.3.7 -->

Let $X$ be a locally noetherian prescheme. Let $d$ be an integer such that $\dim \mathcal{O}_{X,x} \geqslant d$ implies
$prof \mathcal{O}_{X,x} \geqslant 2$. Then, if $X$ is connected, $X$ is connected in codimension $d - 1$, i.e. if $X'$
and $X''$ are two irreducible components of $X$, there exists a sequence of irreducible components of $X$:

```text
X′ = X_0, X_1, …, X_n = X″
```

such that for every $i$ with $0 \leqslant i < n$, the codimension of $X_{i} \cap X_{i+1}$ in $X$ is at most $d - 1$.

<!-- original page 39 -->

Note first that if $X$ is Cohen-Macaulay, then $d = 2$ enjoys the property invoked above. In this connection, recall
that one defines the codimension of $Y$ in $X$ as the infimum of the dimensions of the local rings in $X$ at the points
of $Y$.

*Proof.* Let $\mathcal{F}$ be the collection of closed subsets of $X$ whose codimension in $X$ is at least $d$. One
notes that $\mathcal{F}$ is an antifilter of closed subsets of $X$. Moreover, for a closed $Y \subset X$ to belong to
$\mathcal{F}$, it is necessary and sufficient that, for every $y \in Y$, there exist an open neighborhood $V$ of $y$ in
$X$ such that $Y \cap V$ has codimension $\geqslant d$ in $V$. Finally, if $X$ is connected and $Y \in \mathcal{F}$,
then $X - Y$ is connected by Hartshorne's theorem. The corollary thus follows from the next lemma, which is of a purely
topological nature.

<!-- TRANSLATOR NOTE: The source writes "il existe un voisinage ouvert V de X" ("an open neighborhood V of X"); the
sense requires "of `y`", which we have restored. -->

**Lemma.**

<!-- label: III.3.8 -->

Let $X$ be a connected, locally noetherian topological space, and let $\mathcal{F}$ be an antifilter of closed subsets
of $X$. Suppose that every closed $Y \subset X$ that locally belongs to $\mathcal{F}$ (i.e. for every point $x \in X$
there exist an open neighborhood $V$ of $x$ in $X$ and a $Y' \in \mathcal{F}$ such that $V \cap Y = V \cap Y'$) belongs
to $\mathcal{F}$. The following conditions are equivalent:

1. For every $Y \in \mathcal{F}$, $X - Y$ is connected.
1. If $X'$ and $X''$ are two distinct irreducible components of $X$, there exists a sequence of irreducible components
   of $X$, $X_{0}, X_{1}, \cdots, X_{n}$, such that $X' = X_{0}$, $X'' = X_{n}$ and, for each $i$ with $1 \leqslant i <
   n$, $X_{i} \cap X_{i+1} \notin \mathcal{F}$.

(ii) ⇒ (i). Let $Y \in \mathcal{F}$; we must show that the open set $U = X - Y$ is connected. Now, if $U'$ and $U''$ are
two irreducible components of $U$, there exist two irreducible components $X'$ and $X''$ of $X$ such that $X' \cap U =
U'$ and $X'' \cap U = U''$. Let $X_{0}, \cdots, X_{n}$ be a sequence of irreducible components of $X$ having the
property invoked above; if one sets $U_{i} = X_{i} \cap U$ for $0 \leqslant i \leqslant n$, the $U_{i}$ are irreducible
components of $U$, and moreover $U_{i} \cap U_{i+1}$ is nonempty for $0 \leqslant i < n$, since otherwise $X_{i} \cap
X_{i+1} \subset Y$ would be an element of $\mathcal{F}$, contrary to the choice of the sequence of the $X_{i}$. This
entails that $U$ is connected.

<!-- original page 40 -->

(i) ⇒ (ii). Let $Y = \bigcup_{X', X''} X' \cap X''$, where one requires $X'$ and $X''$ to be two distinct irreducible
components of $X$ such that $X' \cap X'' \in \mathcal{F}$. The family of the $X' \cap X''$ is locally finite since $X$
is locally noetherian; moreover the $X' \cap X''$ are closed, so $Y$ is closed. Also, $Y$ belongs locally to
$\mathcal{F}$, so $Y \in \mathcal{F}$. Hence $U = X - Y$ is connected. Let $X'$ and $X''$ be two distinct irreducible
components of $X$, and let $U'$ and $U''$ be their traces on $U$, which are nonempty by construction of $Y$. These are
irreducible components of $U$; but $U$ is connected, so, $U$ being locally noetherian, there exists a sequence of
irreducible components $U_{0}, \cdots, U_{n}$ of $U$ such that $U_{0} = U'$, $U_{n} = U''$, $U_{i} \cap U_{i+1} \neq
\emptyset$, and $U_{i} \cap U_{i+1} \neq U_{i}$ for $0 \leqslant i < n$. Let $X_{0}, \cdots, X_{n}$ be the sequence of
irreducible components of $X$ such that $X_{i} \cap U = U_{i}$; if $X_{i} \cap X_{i+1} \in \mathcal{F}$, then by the
construction of $\mathcal{F}$ one would have $U_{i} \cap U_{i+1} = \emptyset$ or $U_{i} = U_{i+1}$, which is impossible
by the choice of the $U_{i}$. QED

**Corollary.**

<!-- label: III.3.9 -->

Let $A$ be a noetherian local ring. Suppose that for every prime ideal $p$ of $A$ one has:

```text
(dim A_p ⩾ 2) ⟹ (prof A_p ⩾ 2).
```

Suppose moreover that $A$ satisfies the chain condition.[^III-3-1] Then, for every minimal prime ideal $p$ of $A$, $\dim
A/p = \dim A$, or equivalently, all the irreducible components of $\operatorname{Spec} A$ have the same dimension: that
of $A$.

If $X'$ and $X''$ are two irreducible components of $X$, one joins them by a chain having the properties enumerated in
Corollary 3.7; it then suffices to show that two successive components have the same dimension, which follows from the
second hypothesis.

**Example.**

<!-- label: III.3.10 -->

<!-- original page 41 -->

Let $X$ be the union of two complementary linear subspaces, of respective dimensions 2 and 3, in a vector space of
dimension 5; more precisely, let $X = \operatorname{Spec} A$, with $A = B/p \cap q$, where $B = k[X_{1}, \cdots,
X_{5}]$, $p$ is the ideal generated by $X_{1}, X_{2}, X_{3}$ and $q$ the ideal generated by `X_4` and `X_5`. Then $X$
can be disconnected by the intersection point $x$ of the two linear subspaces, so the depth of $\mathcal{O}_{X,x}$ is
equal to 1, since it cannot be $\geqslant 2$ by Theorem 3.6. Another reason: the equidimensionality conclusion of the
previous corollary fails.

More generally, taking a union $X$ of two linear subspaces of dimensions $p, q \geqslant 2$ in a vector space of
dimension $p + q$, for no embedding of $X$ in a regular scheme is $X$ even set-theoretically a complete intersection at
the origin: for (possibly modifying it without changing the underlying topological space in a neighborhood of the
origin), $X$ would be Cohen-Macaulay, hence of depth $\geqslant 2$ at the origin, which is not the case.

**Remark.**

<!-- label: III.3.11 -->

Let $X$ be a locally noetherian prescheme, $Y$ a closed subprescheme of $X$, $F$ an $\mathcal{O}_{X}$-module. Depth is a
purely topological notion, expressed in terms of the vanishing of the $H^{i}_{Y}(X, F)$ for $i < n$. One also wishes to
study these sheaves for a given $i$, or for $i > n$. In this connection one proves the following result:

**Lemma.**

<!-- label: III.3.12 -->

Let $m$ be an integer. For $H^{i}_{Y}(X, F) = 0$, $i > m$, to hold for every coherent $F$, it is necessary and
sufficient that it hold for $F = \mathcal{O}_{X}$.

By inductive limit, the property then holds for every quasi-coherent sheaf. For instance, if $Y$ can be described
locally by $m$ equations, or, as one says, if $Y$ is locally set-theoretically a complete intersection (which occurs for
example if $X$ and $Y$ are non-singular), it follows from the computation of the $H^{i}_{Y}(X, F)$ by the Koszul complex
that these sheaves are zero for $i > m$. We have, moreover, used this fact implicitly in Example 3.10.

<!-- original page 42 -->

This cohomological condition is, however, not sufficient, as the next example shows.

**Example.**

<!-- label: III.3.13 -->

Let $X = \operatorname{Spec}(A)$, where $A$ is a normal noetherian local ring of dimension 2. Let $Y$ be a curve in $X$.
One can show that the complement of the curve is an affine open, so[^N.D.E-III-3] $H^{i}_{Y}(\mathcal{O}_{X}) \cong
H^{i-1}_{X-Y}(\mathcal{O}_{X}) = 0$ for $i > 1$, since $H^{i-1}(X - Y, \mathcal{O}_{X}) = 0$. Nevertheless, one can
construct a curve that is not described by a single equation.

We shall seek[^III-3-2] conditions for the $H^{i}_{Y}(X, F)$ to be coherent for a given $i$, which is not the case in
general, as obvious examples show — for instance $H^{n}_{m}(A)$ for $A$ a noetherian local ring of dimension $n > 0$;
for example when $A$ is a discrete valuation ring with field of fractions $K$, one finds $H^{1}_{m}(A) \simeq K/A$,
which is not a finitely generated module over $A$. To enlighten the reader, let us say that the problem posed is
equivalent to the following: let $f: U \to X$ be an open immersion, let $G$ be a coherent sheaf on $U$; find criteria
for the higher direct images $R^{i} f_{*} G$ to be coherent sheaves on $X$ for a given $i$. These conditions are
necessary for the use of formal geometry that we saw in Exposé IX and the following ones.

<!--
LEDGER DELTA (Exposé III):
| French | English | Note |
| ------ | ------- | ---- |
| Rappels | Review | Section title. |
| annulateur | annihilator | Standard. |
| support | support | Standard. |
| assassin de M | "assassin of `M`" | Bourbaki idiom; kept with quotes to preserve the figure of speech and the explanatory gloss that follows. |
| ensemble des idéaux premiers associés à M | set of prime ideals associated with `M` | Per source. |
| racine de a | radical of `a` | Modern English; the symbol `r(a)` is kept. |
| de type fini | finitely generated | Module-level rendering. |
| profondeur | depth | Per glossary. |
| `I`-profondeur | `I`-depth | Per glossary; notation `prof_I M` preserved. |
| `M`-régulier | `M`-regular | Per glossary. |
| diviseur de 0 | zero divisor | Standard. |
| homothétie de rapport a | multiplication by `a` | English mathematical idiom; "homothety of ratio `a`" is unidiomatic in module-theoretic prose. |
| suite régulière | regular sequence | Standard. |
| foncteur universel | universal functor | Standard (in the sense of Grothendieck's *Tôhoku*: an exact connected sequence of functors that vanishes on injectives). |
| anneau semi-local | semi-local ring | Standard. |
| radical | radical | Standard; `r(A)` preserved. |
| codimension homologique | homological codimension | Per source; alongside the more modern *depth*. |
| codh_A M | `codh_A M` | Symbol preserved. |
| platitude / fidèlement plat | flatness / faithfully flat | Standard. |
| antifiltre | antifilter | Loanword from order theory; "antifilter of closed subsets" preserved as in source. |
| chaîne | chain | "Chain condition" for *condition des chaînes*; cross-reference to EGA 0_IV preserved. |
| Cohen-Macaulay | Cohen-Macaulay | Standard. |
| composante irréductible | irreducible component | Standard. |
| connexe en codimension d−1 | connected in codimension `d − 1` | Standard. |
| sous-espace vectoriel supplémentaire | complementary linear subspace | The vector-space sense ("complementary" = direct-sum complement). |
| ensemblistement | set-theoretically | Standard. |
| intersection complète | complete intersection | Standard. |
| image directe supérieure | higher direct image | Standard; notation `R^i f_*` preserved. |
| « passage du local au global » (suite spectrale) | "local-to-global" spectral sequence | Quoted in source; quotes preserved. |
| coquille | typo | N.D.E. footnote 3. |
| théorème de Hartshorne | Hartshorne's theorem | Attribution preserved per glossary. |
| spectre premier | prime spectrum | Per source. |
| condition des chaînes | chain condition | Per EGA 0_IV reference. |
| antifiltre | antifilter | Same as above. |
-->

[^N.D.E-III-1]: *N.D.E.* The reissue of Serre's text (Serre J.-P., *Algèbre locale. Multiplicités*, course at the
    Collège de France, 1957–1958, written up by Pierre Gabriel, second edition, *Lect. Notes in Math.*, vol. 11,
    Springer-Verlag, 1965) no longer contains the proofs of these statements. The reader may consult (Bourbaki N.,
    *Algèbre commutative*, Masson), as Serre himself suggests.

[^N.D.E-III-2]: *N.D.E.* The original edition gave a proof, not entirely correct.

[^III-3-1]: Cf. EGA 0_IV 14.3.2.

[^N.D.E-III-3]: *N.D.E.* There was a typo in the original edition.

[^III-3-2]: Cf. Exp. VIII.
