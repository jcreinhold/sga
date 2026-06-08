# Exposé X. Application to the fundamental group

<!-- label: X -->

<!-- original page 89 -->

Throughout this Exposé, $X$ will denote a locally noetherian prescheme, $Y$ a closed part of $X$, $U$ a variable open
neighborhood of $Y$ in $X$, and $\hat{X}$ the formal completion of $X$ along $Y$ ([EGA I 10.8](https://jcreinhold.github.io/ega/i/01-10-formal-schemes.html#108-formal-completion-of-a-prescheme-along-a-closed-subset)). For every prescheme $Z$,
we denote by $\hat{E}t(Z)$ the category of étale coverings of $Z$, and by $L(Z)$ the category of locally free coherent
Modules on $Z$.

## 1. Comparison of $\hat{E}t(\hat{X})$ and $\hat{E}t(Y)$

<!-- label: X.1 -->

Let $I$ be an ideal of definition of $Y$ in $X$. Set, for every $n \in \mathbb{N}$, $Y_{n} = (Y,
(\mathcal{O}_{X}/I^{n+1})|Y)$. The $Y_{n}$ form a direct system of ordinary preschemes, or also of formal preschemes, by
equipping the structure sheaves with the discrete topology. One knows ([EGA I 10.6.2](https://jcreinhold.github.io/ega/i/01-10-formal-schemes.html#106-formal-preschemes-as-inductive-limits)) that $\hat{X}$ is the direct limit,
in the category of formal preschemes, of the direct system of the $Y_{n}$. One also knows ([EGA I 10.13](https://jcreinhold.github.io/ega/i/01-10-formal-schemes.html#1013-morphisms-of-finite-type)) that to give a
formal $\hat{X}$-prescheme of finite type $R$ is the same as to give a direct system of $Y_{n}$-preschemes $R_{n}$ of
finite type, such that $R_{n} \simeq (R_{n+1}) \times_{(Y_{n+1})} (Y_{n})$. Moreover, in order that $R$ be an étale
covering of $\hat{X}$, it is necessary and sufficient that for every $n$, $R_{n}$ be an étale covering of $Y_{n}$. This
said, it is easy to see that nilpotent elements do not matter for étale coverings (SGA 1 8.3), that is, that the
base-change functor

$$ \hat{E}t(Y_{n+1}) \longrightarrow \hat{E}t(Y_{n}) $$

is an equivalence of categories for every $n \in \mathbb{N}$. Hence:

**Proposition.**

<!-- label: X.1.1 -->

With the notation introduced above, the natural functor $\hat{E}t(\hat{X}) \to \hat{E}t(Y)$ is an equivalence of
categories (cf. SGA 1 8.4).

## 2. Comparison of $\hat{E}t(Y)$ and $\hat{E}t(U)$, for $U$ variable

<!-- label: X.2 -->

<!-- original page 90 -->

We shall introduce two conditions from which the announced comparison theorem will follow easily. Let $X$ be a locally
noetherian prescheme and let $Y$ be a closed part of $X$. One says that the pair $(X, Y)$ satisfies the *Lefschetz
condition*, written $Lef(X, Y)$, if, for every open $U$ of $X$ containing $Y$ and every locally free coherent sheaf $E$
on $U$, the natural homomorphism

```text
Γ(U, E) ⟶ Γ(X̂, Ê)
```

is an isomorphism.

One says that the pair $(X, Y)$ satisfies the *effective Lefschetz condition*, written $Leff(X, Y)$, if $Lef(X, Y)$
holds and if, moreover, for every locally free coherent sheaf $E$ on $\hat{X}$, there exist an open neighborhood $U$ of
$Y$, a locally free coherent sheaf $E$ on $U$, and an isomorphism $\hat{E} \simeq E$.

These conditions are satisfied in two important examples:

**Example.**[^N.D.E-X-1]

<!-- label: X.2.1 -->

Let $A$ be a noetherian ring and let $t \in \mathfrak{r}(A)$ be an $A$-regular element belonging to the radical
$\mathfrak{r}(A)$ of $A$. Suppose that $A$ is a quotient of a regular local ring and that $A$ is complete for the
$t$-adic topology (for example $A$ complete for the $\mathfrak{r}(A)$-adic topology). Set $X' = \operatorname{Spec}(A)$
and $Y' = V(t)$; further, set $x = \mathfrak{r}(A)$ and $X = X' - {x}$, $Y = Y' - {x}$. So $X$ is open in $X'$ and $Y =
X \cap Y'$. Then:

1. If, for every prime ideal $\mathfrak{p}$ of $A$ such that $\dim A/\mathfrak{p} = 1$ (i.e. for every closed point of
   $X$), one has $prof A_{\mathfrak{p}} \geqslant 2$, then $Lef(X, Y)$ holds;
1. if, moreover, for every prime ideal $\mathfrak{p}$ of $A$ such that $t \in \mathfrak{p}$ and $\dim A/\mathfrak{p} =
   1$ (i.e. for every closed point of $Y$), one has $prof A_{\mathfrak{p}} \geqslant 3$, then $Leff(X, Y)$ holds.

Let us first show that, for every open neighborhood $U$ of $Y$ in $X$, the complement of $U$ in $X$ is a union of a
finite number of closed points (in $X$). Note that $U$ is open in $X$, hence in $X'$, so $Z' = X' - U$ is closed.

<!-- original page 91 -->

Let $I$ be an ideal of definition of $Z'$; it suffices to prove that $A/I$ is of dimension `1`. But $Z' \cap Y' = {x}$,
so $A/(I + (t))$ is artinian, whence the conclusion by the "Hauptidealsatz".

The first hypothesis is equivalent to: "for every prime ideal $\mathfrak{p}$ of $A$, $\mathfrak{p} \neq
\mathfrak{r}(A)$, one has $prof A_{\mathfrak{p}} \geqslant 3 - \dim A/\mathfrak{p}$". Indeed, $A$ is a quotient of a
regular ring, so one may apply VIII 2.3 to the prescheme $X'$, to the closed part ${x}$, and to the coherent sheaf
$\mathcal{O}_{X'}$, observing that $c(\mathfrak{p}) = \dim(A/\mathfrak{p})$ for $\mathfrak{p} \in U = X' - {x}$ (since
$x$ is the closed point of $X'$).

Let $U$ be an open neighborhood of $Y$ in $X$ and let $E$ be a locally free $\mathcal{O}_{U}$-module. Set $Z = X - U$
and let $u: U \to X$ be the canonical immersion. We shall first prove that $u_{*}(E)$ is a coherent
$\mathcal{O}_{X}$-Module, or what amounts to the same, that $\mathcal{H}^{i}_{Z}(E')$ is coherent for $i = 0, 1$, where
$E'$ is a coherent extension of $E$ to $X$. To do this, one applies Theorem VIII 2.1 to the prescheme $X$, to the closed
part $Z$, and to the coherent sheaf $E'$. It suffices to verify that for every point $\mathfrak{p} \in U$ such that
$c(\mathfrak{p}) = 1$, one has $prof E'_{\mathfrak{p}} \geqslant 1$, where we have set

```text
c(𝔭) = codim({𝔭}̄ ∩ Z, {𝔭}̄).
```

Now if $\mathfrak{p} \in U$ and $c(\mathfrak{p}) = 1$, denoting again by $\mathfrak{p}$ the ideal of $A$ corresponding
to $\mathfrak{p}$, one sees that $\dim A/\mathfrak{p} = 2$, since the complement of $U$ is a union of a finite number of
closed points and $A$ is a quotient of a regular ring. Moreover, $E$ is locally free, so for every $\mathfrak{p} \in
Supp E$ one has $prof E_{\mathfrak{p}} = prof \mathcal{O}_{U,\mathfrak{p}}$. Finally, if $\mathfrak{p} \in U$ and
$c(\mathfrak{p}) = 1$, one has

```text
prof E′_𝔭 = prof E_𝔭 = prof 𝒪_{U,𝔭} = prof A_𝔭 ⩾ 3 − 2 = 1.
```

We must now prove that the natural homomorphism

```text
Γ(U, E) ⟶ Γ(X̂, Ê)
```

<!-- label: eq:X.2.1.1 -->

is an isomorphism. Setting then $\tilde{E} = u_{*}(E)$, one notes that `Ẽ` is coherent and of depth $\geqslant 2$ at
every closed point of $X$. It follows that $R^{i} f_{*}(\tilde{E})$ is coherent for $i = 0, 1$, where $f: X \to X'$
denotes the canonical immersion of $X$ into $X' = \operatorname{Spec}(A)$ (Exp. VIII). One then applies (IX 1.5) and
concludes that

<!-- original page 92 -->

```text
Γ(U, E) ⟶ Γ(X̂, Ê)
```

<!-- label: eq:X.2.1.2 -->

is an isomorphism, since $A$ is complete for the $t$-adic topology. One has a commutative diagram

```text
       Γ(X, Ẽ) ────≃────→ Γ(U, E)
            ╲              ╱
             ╲            ╱
              ≃          ↓
               ╲        ╱
                ↘     ↙
                Γ(X̂, Ê)
```

whence the conclusion.

Now let $E$ be a locally free coherent sheaf on $\hat{X}$. If one has proved that $E$ is algebraizable, i.e. is
isomorphic to the formal completion of a coherent $\mathcal{O}_{X}$-Module `Ẽ`, it is easy to see that `Ẽ` is locally
free in a neighborhood of $Y$, hence to prove $Leff(X, Y)$. Let $\hat{X}'$ be the formal spectrum of $A$ for the
$t$-adic topology, which is identified with the formal completion of $X'$ along $Y'$. Denote by $f$ the canonical
immersion of $X$ in $X'$, by $f'$ the canonical immersion of $Y$ in $Y'$, and by $\hat{f}$ the morphism deduced by
passing to the completions. In order that $E$ be algebraizable, it suffices that $\hat{f}_{*}(E)$ be a coherent
$\mathcal{O}_{\hat{X}'}$-Module, since $A$ is complete for the $t$-adic topology. Let $I = t\mathcal{O}_{\hat{X}}$; this
is an ideal of definition of $\hat{X}$.

For every $n \geqslant 0$, set $E_{n} = E/I^{n+1}E$. At every closed point $y \in Y$, the depth of $E_{0}$ is $\geqslant
2$; indeed, $t$ is an $A$-regular element, so $prof \mathcal{O}_{Y_{0},y} = prof \mathcal{O}_{X,y} - 1 \geqslant 2$. One
concludes that $\hat{f}_{*}(E)$ is coherent (IX 2.3). QED.

<!-- original page 92 -->

**Example** (Will allow comparison of the fundamental group of a projective variety and a hyperplane section).

<!-- label: X.2.2 -->

Let $K$ be a field and let $X$ be a proper $K$-prescheme. Let $L$ be an ample invertible $\mathcal{O}_{X}$-Module. Let
$t \in \Gamma(X, L)$ be an $\mathcal{O}_{X}$-regular element, which means that, for every open $U$ and every isomorphism
$u: L|U \to \mathcal{O}_{U}$, $u(t)$ is a non-zero-divisor in $\mathcal{O}_{U}$ (a condition that does not depend on
$u$). Let $Y = V(t)$ be the subscheme of $X$ of equation $t = 0$.[^N.D.E-X-2] Then:

1. If, for every closed point $x$ in $X$, one has $prof \mathcal{O}_{X,x} \geqslant 2$, then $Lef(X, Y)$ holds;
1. if, moreover, for every closed point $y \in Y$ one has $prof \mathcal{O}_{X,y} \geqslant 3$, then $Leff(X, Y)$ holds.

This example will be treated in detail in Exp. XII.

Let $S$ be a prescheme; one knows ([EGA II 6.1.2](https://jcreinhold.github.io/ega/ii/02-06-integral-finite-morphisms.html#61-preschemes-integral-over-another)) that the functor which to every finite flat covering $r: R \to S$
associates the $\mathcal{O}_{X}$-Algebra $r_{*}(\mathcal{O}_{R})$ induces an equivalence between the category of finite
flat coverings of $S$ and the category of locally free coherent $\mathcal{O}_{X}$-Algebras. Let $U$ be an open
neighborhood of $Y$, and let $r: R \to U$ be a finite flat covering of $U$. Let $\hat{R}$ be the finite flat covering of
$\hat{X}$ deduced from it by base change. One has $\hat{r}_{*}(\mathcal{O}_{\hat{R}}) \simeq
r_{*}\hat{\mathcal{O}_{R}}$.

Suppose then that $Lef(X, Y)$ holds. This implies that, for every $U$, the inverse image functor

$$ L(U) \longrightarrow L(\hat{X}) $$

is fully faithful. Indeed, let $E$ and $F$ be two locally free coherent $\mathcal{O}_{U}$-Modules;
$\operatorname{Hom}(E, F)$ is also coherent and locally free. By hypothesis the natural map

```text
Γ_U(Hom(E, F)) ⟶ Γ_{X̂}(Hom(E, F)̂)
```

is an isomorphism, whence the conclusion, since `Hom` commutes with `̂` since everything is locally free. Now the `̂`
commutes with the tensor product, from which one deduces that the functor which to every locally free coherent
$\mathcal{O}_{U}$-Algebra $A$ associates the $\mathcal{O}_{\hat{X}}$-Algebra `Â` is fully faithful. Better, if $E$ is a
locally free coherent $\mathcal{O}_{U}$-Module, there is a bijective correspondence between the commutative
$\mathcal{O}_{\hat{X}}$-Algebra structures on `Ê`.

<!-- original page 92 (continued) -->

**Proposition.**

<!-- label: X.2.3 -->

Let $X$ be a locally noetherian prescheme and let $Y$ be a closed part of $X$. Let $\hat{X}$ be the formal completion of
$X$ along $Y$. For every open $U$ of $X$, $U \supset Y$, denote by `L_U` (resp. `P_U`, resp. `E_U`) the functor which to
every locally free coherent $\mathcal{O}_{U}$-Module (resp. every finite flat covering of $U$, resp. every étale
covering of $U$) associates its inverse image by $\hat{X} \to X$.

1. If $Lef(X, Y)$ holds, then for every open neighborhood $U$ of $Y$, the functors `L_U`, `P_U`, and `E_U` are fully
   faithful.

<!-- original page 93 -->

1. If $Leff(X, Y)$ holds, then for every locally free coherent $\mathcal{O}_{\hat{X}}$-Module $E$ (resp. ...), there
   exist an open $U$ and a locally free coherent $\mathcal{O}_{U}$-Module `Ẽ` (resp. ...), such that $L_{U}(\tilde{E})
   \simeq E$ (resp. ...).

(i) Has been seen.

(ii) Follows from (i) and from the hypothesis, at least for `L_U` and `P_U`. Moreover, if $R$ is an étale covering of
$\hat{X}$, there exist an open neighborhood $U$ of $Y$ in $X$ and a finite flat covering $R'$ of $U$ such that $\hat{R}'
\simeq R$. From it one deduces a covering $R''$ of $Y$ which is étale by 1.1, so $R'$ is étale in a neighborhood $U'$ of
$Y$. QED.

**Corollary.**

<!-- label: X.2.4 -->

If $Lef(X, Y)$ holds, then in order that a finite flat covering $R$ of an open neighborhood $U$ of $Y$ be connected, it
is necessary and sufficient that $R \times_{U} \hat{X}$ be connected. In particular, in order that $Y$ be connected, it
is necessary and sufficient that the open neighborhood $U$ of $Y$ be connected, or again that $\hat{X}$ be connected.

Indeed, in order that a ringed space in local rings $(X, \mathcal{O}_{X})$ be connected, it is necessary and sufficient
that $\Gamma(X, \mathcal{O}_{X})$ not be a direct product of two non-zero rings. Now one has

```text
Γ(U, r_*(𝒪_R)) ≃ Γ(X̂, r̂_*(𝒪_{R̂}))
```

by $Lef(X, Y)$.

**Corollary.**

<!-- label: X.2.5 -->

If $Lef(X, Y)$ holds, then for every $U$, the functor

$$ \hat{E}t(U) \longrightarrow \hat{E}t(Y) $$

is fully faithful. If $Leff(X, Y)$ holds, then for every étale covering $R$ of $Y$, there exist an open neighborhood $U$
of $Y$ and a covering $R'$ of $U$ such that $R' \times_{U} Y \simeq R$.

**Corollary.**[^N.D.E-X-3]

<!-- label: X.2.6 -->

If $Lef(X, Y)$ holds and $Y$ is connected, then every open neighborhood $U$ of $Y$ is connected and the natural
homomorphism $\pi_{1}(Y) \to \pi_{1}(U)$ is surjective. If, moreover, $Leff(X, Y)$ holds, the natural homomorphism

```text
π₁(Y) ⟶ lim_{←, U} π₁(U)
```

is an isomorphism. (N.B. One assumes that a "base-point" has been chosen in $Y$, which one also takes as base-point in
$X$, for the definition of the fundamental groups.)

All of this follows trivially from Proposition 1.1 and Proposition 2.3.

<!-- original page 94 -->

## 3. Comparison of $\pi_{1}(X)$ and $\pi_{1}(U)$

<!-- label: X.3 -->

**Definition.**

<!-- label: X.3.1 -->

Let $X$ be a prescheme and $Z$ a closed part of $X$. Set $U = X - Z$. One says that the pair $(X, Z)$ is *pure* if, for
every open $V$ of $X$, the functor

```text
Êt(V) ⟶ Êt(V ∩ U)
V′ ↦ V′ ×_V (V ∩ U)
```

is an equivalence of categories.[^X-3-pur-star]

**Definition.**

<!-- label: X.3.2 -->

<!-- original page 94 (continued) -->

Let $A$ be a noetherian local ring. Set $X = \operatorname{Spec} A$. Let $\mathfrak{r}(A)$ be the radical of $A$ and let
$x = \mathfrak{r}(A)$ be the closed point of $X$. One says that $A$ is *pure* if the pair `(X, {x})` is.

We leave to the reader the task of not proving the following proposition:

**Proposition.**

<!-- label: X.3.3 -->

Let $X$ be a locally noetherian prescheme and let $Z$ be a closed part of $X$. In order that the pair $(X, Z)$ be pure
it is necessary and sufficient that, for every $z \in Z$, the ring $\mathcal{O}_{X,z}$ be pure.[^X-3-pur-starstar]

This said, the following theorem is the essential result of this number:

**Theorem** (Purity theorem).[^N.D.E-X-4]

<!-- label: X.3.4 -->

1. A regular noetherian local ring of dimension $\geqslant 2$ is pure (Zariski–Nagata purity theorem).
1. A noetherian local ring of dimension $\geqslant 3$ which is a complete intersection is pure.

<!-- original page 95 -->

Recall that one says that a local ring is a *complete intersection* if there exist a regular noetherian local ring $B$
and a $B$-regular sequence $(t_{1}, \cdots, t_{k})$ of elements of the radical $\mathfrak{r}(B)$ of $B$ such that

$$ A \simeq B/(t_{1}, \cdots, t_{k}). $$

In this connection, let us remark that it would be less ambiguous to say that $A$ is an *absolute* complete
intersection, by opposition with the situation, already encountered, in which $X$ is a locally noetherian prescheme
(which need not be regular) and $Y$ is a closed part of $X$, of which one says that it is "locally set-theoretically a
complete intersection in $X$".

Let us first prove a few lemmas.

**Lemma.**

<!-- label: X.3.5 -->

Let $X$ be a locally noetherian prescheme and let $U$ be an open part of $X$. Set $Z = X - U$. Let $i: U \to X$ be the
canonical immersion of $U$ into $X$. The following conditions are equivalent:

1. For every open $V$ of $X$, if one sets $V' = V \cap U$, the functor $F \mapsto F|V'$ from the category of locally
   free coherent $\mathcal{O}_{V}$-Modules to the category of locally free coherent $\mathcal{O}_{V'}$-Modules is fully
   faithful;
1. the natural homomorphism $\mathcal{O}_{X} \to i_{*}(\mathcal{O}_{U})$ is an isomorphism;
1. for every $z \in Z$, one has $prof \mathcal{O}_{X,z} \geqslant 2$.

One has already seen (III 3.3) the equivalence of (ii) and (iii). Let us show that (ii) implies (i). Let $F$ and $G$ be
two locally free coherent $\mathcal{O}_{V}$-Modules; $\operatorname{Hom}(F, G)$ is also one, so $\operatorname{Hom}(F,
G) \to i_{*}(\operatorname{Hom}(F|V', G|V'))$ is an isomorphism, so $\operatorname{Hom}(F, G) \simeq
\operatorname{Hom}(F|V', G|V')$. Conversely, one takes $F = G = \mathcal{O}_{X}$ and applies (i) to every open $V$ of
$X$.

Here is a useful "descent lemma":

**Lemma.**

<!-- label: X.3.6 -->

Let $X$ be a locally noetherian prescheme and let $Z$ be a closed part of $X$. Set $U = X - Z$. Suppose that the
homomorphism $\mathcal{O}_{X} \to i_{*}(\mathcal{O}_{U})$ is an isomorphism. Let $f: X_{1} \to X$ be a faithfully flat
and quasi-compact morphism. Set $Z_{1} = f^{-1}(Z)$. If the pair $(X_{1}, Z_{1})$ is pure, then so is $(X, Z)$.

Note that the hypothesis $\mathcal{O}_{X} \simeq i_{*}(\mathcal{O}_{U})$ is preserved by flat extension of the base,
since $i$ is a quasi-compact morphism and, in that case, direct image commutes with inverse image. Now this hypothesis
implies that the functor

$$ \hat{E}t(V) \longrightarrow \hat{E}t(U \cap V) $$

defined by

```text
V′ ↦ V′ ×_V (V ∩ U)
```

is fully faithful, as shown by the interpretation of an étale covering in terms of locally free coherent Algebras. It
remains to prove effectivity.

<!-- original page 95 (continued) -->

One can, for example, introduce the square $X_{2}$ and the cube $X_{3}$ of $X_{1}$ over $X$ and observe that a
faithfully flat and quasi-compact morphism is a morphism of universal effective descent for the fibered category of
étale coverings, above the category of preschemes. The conclusion is formal from there.[^X-3-giraud-star]

**Remark.**

<!-- label: X.3.7 -->

<!-- original page 96 -->

We have shown in passing that if $\mathcal{O}_{X} \to i_{*}(\mathcal{O}_{U})$ is an isomorphism, then $X$ is connected
if and only if $U$ is, and then $\pi_{1}(U) \to \pi_{1}(X)$ is surjective.

**Corollary.**

<!-- label: X.3.8 -->

Let $A$ be a noetherian local ring. Suppose that $prof A \geqslant 2$. Then if `Â` is pure, $A$ is pure.

Follows from Lemma 3.5 and Lemma 3.6.

The following lemma is the essential point in the proof of the purity theorem:

**Lemma.**

<!-- label: X.3.9 -->

Let $A$ be a noetherian local ring and let $t \in \mathfrak{r}(A)$ be an $A$-regular element. Suppose that $A$ is
complete for the $t$-adic topology and is, moreover, a quotient of a regular local ring (for example $A$ complete). Set
$B = A/tA$.

1. If for every prime ideal $\mathfrak{p}$ of $A$ such that $\dim A/\mathfrak{p} = 1$, one has $prof A_{\mathfrak{p}}
   \geqslant 2$, then $B$ pure implies $A$ pure.
1. If for every prime ideal $\mathfrak{p}$ of $A$ such that $\dim A/\mathfrak{p} = 1$, one has $prof A_{\mathfrak{p}}
   \geqslant 2$, if $A_{\mathfrak{p}}$ is pure when $t \notin \mathfrak{p}$, and if[^N.D.E-X-5] $prof A_{\mathfrak{p}}
   \geqslant 3$ when $t \in \mathfrak{p}$, then $A$ pure implies $B$ pure.

Let $X' = \operatorname{Spec}(A)$ and $Y' = V(t)$, which one identifies with the spectrum of $B$. Let $x =
\mathfrak{r}(A)$, and set $X = X' - {x}$ and $Y = Y' - {x} = X \cap Y'$. Denote by $\hat{X}'$ the formal spectrum of $A$
for the $t$-adic topology, which is identified with the formal completion of $X'$ along $Y'$.

Since $A$ is complete for the $t$-adic topology, one notes that $\hat{E}t(X') \to \hat{E}t(\hat{X}')$ is an equivalence
of categories. Likewise $\hat{E}t(\hat{X}') \to \hat{E}t(Y')$ by Proposition 1.1, so $\hat{E}t(X') \to \hat{E}t(Y')$ is
an equivalence of categories.

<!-- original page 97 -->

Let us show (i). Consider the diagrams

```text
   X′  ←──  X                    Êt(X′)  ──a──→  Êt(X)
   ↑        ↑                       │              │
   │        │                       c              b
   │        │                       ↓              ↓
   Y′  ←──  Y                    Êt(Y′)  ──d──→  Êt(Y)
```

We have just seen that $c$ is an equivalence; $d$ is also one by the hypothesis that $B$ is pure; and finally $b$ is
fully faithful as seen in Example 2.1, cf. 2.3 (i).

Let us show (ii). This time one assumes that $A$ is pure, so $a$ is an equivalence; likewise $c$. Let us see that $b$ is
an equivalence. By Example 2.1 we know that $Leff(X, Y)$ holds, so $b$ is already fully faithful; let us prove that it
is essentially surjective. One uses 2.3 (ii), noting that if $U$ is an open neighborhood of $Y$ in $X$, the complement
of $U$ in $X$ is a union of a finite number of closed points; the pair $(X, X - U)$ is thus pure by Proposition 3.3,
since at such a point $\mathfrak{p}$, $\mathcal{O}_{X,\mathfrak{p}} = A_{\mathfrak{p}}$ is pure by hypothesis. Whence
the conclusion.

**Proof of the purity theorem.**

Let us first prove (i) by induction on the dimension. Let $A$ be a noetherian local ring of dimension `2`. Set $X' =
\operatorname{Spec}(A)$, $x = \mathfrak{r}(A)$, $X = X' - {x}$. One has $prof A = 2$. One may therefore apply Lemma 3.5
to the pair $(X', {x})$, and so $\hat{E}t(X') \to \hat{E}t(X)$ is fully faithful. Let now $r: R \to X$ be an étale
covering defined by a locally free coherent and étale $\mathcal{O}_{X}$-Algebra $A = r_{*}(\mathcal{O}_{R})$. Denote by
$i: X \to X'$ the canonical immersion of $X$ into $X'$. I claim that $i_{*}(A) = B$ is a coherent
$\mathcal{O}_{X'}$-Algebra. Indeed, it suffices to apply the "finiteness theorem" VIII 2.3. I claim that this algebra is
of depth $\geqslant 2$ at $x$. Indeed, it is the direct image of an $\mathcal{O}_{X}$-Module, with $X = X' - {x}$. Since
$A$ is a regular ring of dimension `2`, one has $dp B + prof B = \dim A = 2$, where `dp B` denotes the projective
dimension of $B$. So $dp B = 0$, hence $B$ is projective, hence free. It follows that $B$ defines a finite flat covering
of $X' = \operatorname{Spec}(A)$. The set of points of $X'$ where this covering is not étale is a closed part of $X'$
whose equation is a principal ideal: the discriminant ideal of $B/A$. Now, by construction, this closed set is contained
in $x = \mathfrak{r}(A)$, hence is empty since $\dim A = 2$.

<!-- original page 97 (continued) -->

Let $A$ be a regular noetherian local ring, $\dim A = n \geqslant 3$. Suppose (i) proved for rings of dimension $< n$.
To prove that $A$ is pure, one may assume $A$ complete by 3.8. Let $t \in \mathfrak{r}(A)$ whose image in
$\mathfrak{r}(A)/\mathfrak{r}(A)^{2}$ is nonzero. Then $B = A/tA$ is a regular noetherian local ring of dimension $n -
1$, hence is pure, since $n - 1 \geqslant 2$. One concludes by Lemma 3.9 (i), which is applicable since $A$ is complete.

Let us show (ii). Let $A$ be a noetherian local ring of dimension $\geqslant 3$. Suppose that there exist a regular
noetherian local ring $B$ and a $B$-sequence $(t_{1}, \cdots, t_{k})$ such that $A \simeq B/(t_{1}, \cdots, t_{k})$. Let
us prove that $A$ is pure, by induction on $k$. If $k = 0$, one knows it by (i). Suppose $k \geqslant 1$ and the result
acquired for $k' < k$. By Corollary 3.8[^TRANSLATOR-X-1] one may assume that $A$ (hence also $B$) is complete. Set $C =
B/(t_{1}, \cdots, t_{k-1})$, so $A \simeq C/t_{k} C$ and $t_{k}$ is $C$-regular. By the induction hypothesis one knows
that $C$ is pure; it suffices to prove that Lemma 3.9 (ii) is applicable. Notation: the $A$ and $B$ of the lemma become
$C$ and $A$. One has $\dim C \geqslant 4$, so for every prime ideal $\mathfrak{p}$ of $C$ such that $\dim C/\mathfrak{p}
= 1$, one has $prof C_{\mathfrak{p}} \geqslant 3$. Moreover, $C_{\mathfrak{p}}$ is a complete intersection with $k'
\leqslant k - 1$, hence is pure by the induction hypothesis. QED.

**Theorem.**

<!-- label: X.3.10 -->

<!-- original page 97 (continued) -->

Let $X$ be a locally noetherian prescheme and let $Y$ be a closed part of $X$. Suppose that one has $Leff(X, Y)$ (cf.
Examples 2.1 and 2.2). Suppose moreover that, for every open neighborhood $U$ of $Y$ and every $x \in X - U$, the local
ring $\mathcal{O}_{X,x}$ is regular of dimension $\geqslant 2$ or a complete intersection of dimension $\geqslant 3$.
Then

$$ \pi_{0}(Y) \longrightarrow \pi_{0}(X) $$

<!-- original page 98 -->

is a bijection, and if $X$ is connected

$$ \pi_{1}(Y) \longrightarrow \pi_{1}(X) $$

is an isomorphism.

There is nothing more to prove. One remarks that, in the two examples cited 2.1 and 2.2, the complement of $U$ is a
union of a finite number of closed points, from which it follows that the hypothesis on the dimension of
$\mathcal{O}_{X,x}$ is not a farce.

<!--
LEDGER DELTA (Exposé X):

| French | English | Note |
| --- | --- | --- |
| revêtement étale | étale covering | Per SGA 1 glossary. |
| Module cohérent localement libre | locally free coherent Module | Capital `M` preserved per SGA capitalisation. |
| complété formel (de X le long de Y) | formal completion (of X along Y) | Standard; hat `X̂` preserved. |
| condition de Lefschetz / Lefschetz effective | Lefschetz condition / effective Lefschetz condition | `Lef(X, Y)` / `Leff(X, Y)` notation preserved. |
| couple pur de préschémas | pure pair of preschemes | Per glossary; rendered "the pair `(X, Z)` is pure". |
| anneau local pur | pure local ring | Per glossary. |
| théorème de pureté de Zariski-Nagata | Zariski–Nagata purity theorem | Central local result X 3.4. |
| anneau régulier (local noethérien) | regular (noetherian local) ring | Standard. |
| intersection complète (absolue) | (absolute) complete intersection | Grothendieck's qualifier "absolue" preserved. |
| suite B-régulière | B-regular sequence | Standard. |
| Hauptidealsatz | Hauptidealsatz | Kept as Krull's principal-ideal theorem name. |
| algébrisable | algebraizable | Standard formal-geometry term. |
| canularesque | a farce / farcical | Grothendieck slang; preserves the joking register of "canularesque" (from "canular", hoax/joke). |
| Je dis que … | I claim that … | Preserve the first-person move. |
| « point-base » | "base-point" | Preserved with quotes. |
| Nous laissons au lecteur le soin de ne pas démontrer | We leave to the reader the task of not proving | Grothendieck's joke about the obviousness of 3.3; preserve literally. |
| morphisme fidèlement plat et quasi-compact | faithfully flat and quasi-compact morphism | Standard. |
| descente effective universelle | universal effective descent | Standard. |
| dimension projective (dp) | projective dimension (dp) | Auslander–Buchsbaum formula context. |
| idéal discriminant | discriminant ideal | Standard. |
| dim A/𝔭 = 1 (point fermé) | closed point | French phrase "i.e. pour tout point fermé" preserved. |
| 𝔯(A) | 𝔯(A) | Radical of `A`; preserve fraktur. |
-->

[^N.D.E-X-1]: *N.D.E.* One can slightly improve (i): see Mme Raynaud (Raynaud M., "Théorèmes de Lefschetz en cohomologie
    des faisceaux cohérents et en cohomologie étale. Application au groupe fondamental", *Ann. Sci. Éc. Norm. Sup.* (4)
    **7** (1974), pp. 29–52, corollaries I.1.4 and I.5); the condition (ii) can be improved so as to get rid of the
    depth conditions along $Y$ (see Theorem 3.3 of loc. cit. for a precise statement). The proof of this last point is
    very technical, the article cited above giving only indications of proof and referring to a detailed earlier version
    published in the *Bulletin de la Société mathématique de France*.

[^N.D.E-X-2]: *N.D.E.* Condition (ii) is superfluous; see footnote on page 90.

[^N.D.E-X-3]: *N.D.E.* Joined with 3.3 and the criteria 2.4 and 3.4, one obtains the following relative Lefschetz
    theorem. Let $f: X \to S$ be a projective flat morphism of connected noetherian schemes and let $D$ be an effective
    relative Cartier divisor in $X$ which is relatively ample. If, for every $s \in S$, the depth of $X_{s}$ at each
    closed point is $\geqslant 2$, then $D$ is connected and, for every open $U$ of $X$ containing $D$, the arrow
    $i_{U}: \pi_{1}(D) \to \pi_{1}(U)$ is surjective. If, moreover, the depth of $X_{s}$ along each closed point of
    $D_{s}$ is $\geqslant 3$, and if the local rings of $X$ at its closed points are pure — for example, complete
    intersections (cf. X 3.4) — then $i_{X}$ is an isomorphism. Cf. Bost J.-B., "Lefschetz theorem for Arithmetic
    Surfaces", *Ann. Sci. Éc. Norm. Sup.* (4) **32** (1999), pp. 241–312, Theorems 1.1 and 2.1. In the case where $X$ is
    simply a smooth and geometrically connected projective surface over a field, connectedness of $D$ and surjectivity
    of $\pi_{1}(D) \to \pi_{1}(U)$ (where $U$ is an open containing $D$) always hold for $D$ only nef of square `> 0`
    (cf. loc. cit., Theorem 2.3 and also Theorem 2.4 for surfaces only normal and complete). In the case of an
    arithmetic surface (normal and quasi-projective) $X$ over a ring of integers $\mathcal{O}_{K}$, Bost, improving on
    results of Ihara (Ihara Y., "Horizontal divisors on arithmetic surfaces associated with Belyĭ uniformizations", in
    *The Grothendieck theory of dessins d'enfants* (Luminy, 1993), London Math. Soc. Lect. Note Series, vol. 200,
    Cambridge Univ. Press, Cambridge, 1994, pp. 245–254 or loc. cit., corollary 7.2), has shown that if a point $P \in
    X(\mathcal{O}_{K})$, playing the role of the divisor $D$ in the geometric situation, satisfies certain positivity
    conditions, then the arrow $\pi_{1}(X) \to \pi_{1}(\operatorname{Spec} \mathcal{O}_{K})$ deduced from the projection
    was invertible with inverse the arrow $\pi_{1}(\operatorname{Spec} \mathcal{O}_{K}) \to \pi_{1}(X)$ deduced from $P$
    (loc. cit., Theorem 1.2).

[^X-3-pur-star]: For a more satisfactory notion in some respects, cf. the commentary XIV 1.6 d).

[^X-3-pur-starstar]: Compare with the non-commutative case of XIV 1.8, whose proof is essentially the same as that of
    3.3.

[^N.D.E-X-4]: *N.D.E.* For the history of the methods employed, see Grothendieck's letter of October 1, 1961 to Serre,
    *Correspondance Grothendieck–Serre*, edited by Pierre Colmez and Jean-Pierre Serre, Documents Mathématiques, vol. 2,
    Société Mathématique de France, Paris, 2001.

[^X-3-giraud-star]: Cf. J. Giraud, *Méthode de la descente*, Mémoire no. 2 du Bulletin de la Société Mathématique de
    France (1964).

[^N.D.E-X-5]: *N.D.E.* This last condition can be improved, cf. the editor's note (1) on page 90.

[^TRANSLATOR-X-1]:
    <!-- TRANSLATOR NOTE: The French source reads "D'après le corollaire 3.9", but the result invoked
    is Corollary 3.8 (the reduction to the complete case via `Â`). Lemma 3.9 itself is applied in the next sentence.
    The reference has been silently corrected here; the original numbering anomaly is preserved as a translator
    note. -->
