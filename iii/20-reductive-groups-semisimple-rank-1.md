# Exposé XX. Reductive groups of semisimple rank 1

<!-- label: III.XX -->

*by M. Demazure*

<!-- N.D.E.: Version of 13/10/2024 -->

## 1. Elementary systems. The groups $U_{\alpha}$ and $U_{-\alpha}$

<!-- label: III.XX.1 -->

<!-- original page 35 -->

**Recollection 1.1.** *Let $S = \operatorname{Spec}(k)$, where $k$ is an algebraically closed field, and let $G$ be a
reductive $S$-group of semisimple rank 1, $T$ a maximal torus (necessarily split) of $G$. One then has*

```text
g = t ⊕ g_α ⊕ g_{−α},
```

*where $\alpha$ and $-\alpha$ are the roots of $G$ with respect to $T$. Moreover, there exist two group monomorphisms*

```text
p_α : G_{a, S} → G    and    p_{−α} : G_{a, S} → G
```

*such that*

```text
t p_α(x) t⁻¹ = p_α(α(t) x)    and    t p_{−α}(x) t⁻¹ = p_{−α}(α(t)⁻¹ x),
```

*for every $S' \to S$ and all $t \in T(S')$, $x \in G_{a}(S')$, and such that the morphism*

```text
G_{a, S} ×_S T ×_S G_{a, S} → G,
```

*defined by $(y, t, x) \mapsto p_{-\alpha}(y) t p_{\alpha}(x)$, is radicial and dominant (*Bible*, § 13.4, cor. 2 to th.
3).*

<!-- label: III.XX.1.1 -->

Since the tangent map at the identity is bijective, this morphism is also separable, hence birational; by Zariski's
"Main Theorem" (EGA III₁, 4.4.9), it is therefore an open immersion.

**Lemma 1.2.** *Let $S$ be a scheme, $G$ an $S$-group scheme, $T$ a torus of $G$, $Q$ a subtorus of $T$, $\alpha$ a
character of $T$ inducing on $Q$ a non-trivial character on each fiber. Let $p_{\alpha} : G_{a, S} \to G$ (resp.
$p_{-\alpha} : G_{a, S} \to G$) be a group morphism normalized by $T$ with multiplier $\alpha$ (resp. $-\alpha$).
Suppose that the morphism*

<!-- original page 36 -->

```text
u : G_{a, S} ×_S T ×_S G_{a, S} → G,
```

*defined set-theoretically by $u(y, t, x) = p_{-\alpha}(y) t p_{\alpha}(x)$, is an open immersion. Let finally $q$ be an
integer $\geqslant 0$ and*

```text
p : G_{a, S} → G
```

*a group morphism such that for every $S' \to S$ and all $t \in Q(S')$, $x \in G_{a}(S')$ one has*

$$ int(t)(p(x)) = p(\alpha(t)^{q} x). $$

*Then there exists a unique $\nu \in G_{a}(S)$ such that $p(x) = p_{\alpha}(\nu x^{q})$.*

<!-- label: III.XX.1.2 -->

Indeed, let $\Omega$ be the image of $u$ and $U = p^{-1}(\Omega)$. This is an open subset of $G_{a, S}$ containing the
zero section. For every section $t$ of $Q$, the automorphism of $G_{a, S}$ defined by multiplication by $\alpha(t)$
leaves $U$ globally fixed. We have $U = G_{a, S}$; indeed, it suffices to check this when $S$ is the spectrum of an
algebraically closed field $k$; then $\alpha : Q(k) \to k*$ is surjective, which proves at once that $U(k) \supset k*$,
hence $U = G_{a, k}$. There therefore exist three morphisms

```text
a : G_{a, S} → G_{a, S},   b : G_{a, S} → T,   c : G_{a, S} → G_{a, S},
```

such that

```text
p(x) = p_{−α}(a(x)) b(x) p_α(c(x)).
```

The condition on $p$ translates to

```text
a(α(t) x) = α(t)^{−q} a(x),
b(α(t) x) = b(x),
c(α(t) x) = α(t)^q c(x).
```

<!-- original page 37 -->

For the same reason as before, one therefore has for every $S' \to S$ and every $z \in G_{m}(S')$,

```text
a(z x) = z^{−q} a(x),   b(z x) = b(x),   c(z x) = z^q c(x),
```

hence

```text
z^q a(z) = a(1),   b(z) = b(1),   c(z) = z^q c(1).
```

Since $G_{m, S}$ is schematically dense in $G_{a, S}$, one has at once for every $x \in G_{a}(S')$, $S' \to S$:

```text
x^q a(x) = a(1) = a(0) = 0,    hence a = 0,
c(x) = x^q c(1) = ν x^q,       for some ν ∈ G_a(S),
b(x) = b(1) = b(0) = e,        hence b = e,
```

which completes the proof.

**Definition 1.3.** *Let $S$ be a scheme. By an $S$-*elementary system* one means a triple $(G, T, \alpha)$ where*

*(i) $G$ is a reductive $S$-group of semisimple rank 1 (Exp. XIX 2.7),*

*(ii) $T$ is a maximal torus of $G$,*

*(iii) $\alpha$ is a root of $G$ with respect to $T$ (Exp. XIX 3.2).*

<!-- label: III.XX.1.3 -->

One thus has a direct sum decomposition (Exp. XIX 3.5)[^N.D.E-XX-1]

```text
g = t ⊕ g_α ⊕ g_{−α},
```

$g_{\alpha}$ and $g_{-\alpha}$ being locally free of rank one.

**1.4.** If $(G, T, \alpha)$ is an $S$-elementary system, then $(G_{S'}, T_{S'}, \alpha_{S'})$ is an $S'$-elementary
system for every $S' \to S$. If $(G, T, \alpha)$ is an $S$-elementary system, then $(G, T, -\alpha)$ is also one.

<!-- original page 38 -->

If $S$ is a scheme, $G$ a reductive $S$-group, $T$ a maximal torus of $G$, $\alpha$ a root of $G$ with respect to $T$,
then (Exp. XIX 3.9), $(Z_{\alpha}, T, \alpha)$ is an $S$-elementary system.

Let $(G, T, \alpha)$ be an $S$-elementary system. The invertible module $g_{\alpha}$ is canonically endowed with a
$T$-module structure. One therefore has also a $T$-module structure on the vector bundle $W(g_{\alpha})$. On the other
hand, the inner automorphisms of $T$ define on $G$ a structure of group with group of operators $T$.

**Theorem 1.5.** *Let $(G, T, \alpha)$ be an $S$-elementary system.*

*(i) There exists a unique morphism of groups with group of operators $T$*

$$ \exp : W(g_{\alpha}) \to G $$

*which induces on the Lie algebras the canonical morphism $g_{\alpha} \to g$.*[^N.D.E-XX-2]

*In other words, `exp` is the unique morphism satisfying the following conditions: for every $S' \to S$ and every $t \in
T(S')$, $X, X' \in W(g_{\alpha})(S')$, one has*

```text
exp(X + X′) = exp(X) exp(X′),
int(t)(exp(X)) = exp(α(t) X),
Lie(exp)(X) = X.
```

*(ii) If one defines analogously (in the $S$-elementary system $(G, T, -\alpha)$)*

$$ \exp : W(g_{-\alpha}) \to G, $$

*then the morphism*

```text
W(g_{−α}) ×_S T ×_S W(g_α) → G
```

*defined set-theoretically by $(Y, t, X) \mapsto \exp(Y) \cdot t \cdot \exp(X)$ is an open immersion.*

<!-- label: III.XX.1.5 -->

Suppose we have proved the existence of the desired `exp` morphisms, and let us prove the other assertions of the
theorem. We first prove (ii). Since both sides are of finite presentation and flat over $S$, it suffices to do so when
$S$ is the spectrum of an algebraically closed field (SGA 1, I 5.7 and VIII 5.5). Let then $S = \operatorname{Spec} k$.
Let $X \in \Gamma(S, g_{\alpha})^{\times}$, $Y \in \Gamma(S, g_{-\alpha})^{\times}$. It suffices to prove that the
morphism

<!-- original page 39 -->

```text
G_{a, k} ×_k T ×_k G_{a, k} → G,   (y, t, x) ↦ exp(yY) t exp(xX)
```

is an open immersion. Now by 1.1 and 1.2, there exist $a, b \in k$ such that

```text
exp(yY) = p_{−α}(a y)    and    exp(xX) = p_α(b x).
```

Since $\exp : W(g_{-\alpha}) \to G$ induces a monomorphism on Lie algebras, one has $a \neq 0$; likewise $b \neq 0$, and
one is reduced to 1.1.

The uniqueness of the morphism `exp` may be proved locally on $S$; one then reduces to the case where $g_{\alpha}$ and
$g_{-\alpha}$ are free, and one has only to apply 1.2 (with $Q = T$ and $q = 1$).

It remains then to prove the existence of the desired morphism `exp`. Let us first remark that, by virtue of the theory
of faithfully flat descent and the uniqueness assertion just proved, it suffices to demonstrate this existence locally
on $S$ for the (fpqc) topology. By the usual arguments using finite presentation, one reduces to the case where $S$ is
noetherian, then to the case where it is noetherian local. By virtue of the preceding remark, one can therefore content
oneself with proving the existence of the desired morphism `exp` when $S = \operatorname{Spec}(A)$, with $A$ a complete
noetherian local ring with algebraically closed residue field $k$. Let then $p_{0} : G_{a, k} \to G_{k}$ be a
monomorphism of $k$-groups normalized by $T_{k}$ with multiplier $\alpha_{0} = \alpha \otimes_{A} k$ (one exists by
1.1). One knows (1.1 and 1.2) that the corresponding morphism $T_{k} \cdot_{\alpha_{0}} G_{a, k} \to G_{k}$ is an
immersion, hence in particular a monomorphism. Let us provisionally admit the following two lemmas:

<!-- original page 40 -->

**Lemma 1.6.** *Let $S$ be a scheme, $G$ an $S$-group of finite presentation, $T$ an $S$-torus, $\alpha$ a character
non-trivial on each fiber of $T$, $s_{0}$ a point of $S$. Let*

```text
f : T ·_α G_{a, S} → G
```

*be an $S$-group morphism such that $f_{s_{0}}$ is a monomorphism and the restriction of $f$ to $T$ is a monomorphism.
There exists an open neighborhood $U$ of $s_{0}$ such that $f|U$ is a monomorphism.*

<!-- label: III.XX.1.6 -->

**Lemma 1.7.** *Let $A$ be a complete noetherian local ring with algebraically closed residue field $k$, $(G, T,
\alpha)$ an $A$-elementary system, $p_{0} : G_{a, k} \to G_{k}$ a morphism of $k$-groups normalized by $T_{k}$ with
multiplier $\alpha \otimes_{A} k$. There exists a group morphism $p : G_{a, A} \to G$ normalized by $T$ with multiplier
$\alpha$.*

<!-- label: III.XX.1.7 -->

Let $p$ be the morphism whose existence is asserted by 1.7. Let $f : T \cdot_{\alpha} G_{a, S} \to G$ be the
corresponding morphism. It satisfies the hypotheses of 1.6, hence is a monomorphism; in particular $p$ is a
monomorphism. One then concludes by Exp. XIX 4.9.

*Proof of 1.6.* Denote by $\epsilon : S \to T \cdot_{\alpha} G_{a, S}$ the unit section. Since $f$ is unramified at
$\epsilon(s_{0})$, it is so at $\epsilon(s)$ for all $s$ in an open neighborhood $U$ of $s_{0}$; $f|U$ is therefore
unramified (Exp. X 3.5)[^N.D.E-XX-3], hence its kernel $Ker(f)_{U}$ is unramified over $U$. To prove that $f|U$ is a
monomorphism, it suffices therefore[^N.D.E-XX-4] to prove that $Ker(f)_{U}$ is radicial over $U$, which is a
set-theoretic question. One is thus reduced to proving:

<!-- original page 41 -->

**Lemma 1.8.** *Let $k$ be an algebraically closed field; let $N$ be an invariant subgroup of $T \cdot_{\alpha} G_{a,
k}$ ($\alpha$ a non-trivial character of the torus $T$), étale over $k$ and such that $N \cap T = {e}$. Then $N = {e}$.*

<!-- label: III.XX.1.8 -->

One has $int(t')(t, x) = (t, \alpha(t') x)$. If $(t, x)$ is a point of $N$, with $x \neq 0$, then `(t, z x)` is also a
point of $N$ for $z \in k*$, and $(t, x)$ is not isolated; hence $N$ is not quasi-finite. One therefore has
set-theoretically $N \subset T$, and we are done.

*Proof of 1.7.* Let $m$ be the radical of $A$, and $S_{n} = \operatorname{Spec}(A/m^{n+1})$, $n \geqslant 0$. We first
show, by induction on $n$, that $p_{0}$ can be extended for each $n$ to a morphism of $S_{n}$-groups

```text
p_n : G_{a, S_n} → G_{S_n}
```

normalized by $T_{S_{n}}$ with multiplier $\alpha_{S_{n}}$, the $p_{n}$ further satisfying the condition $p_{n+1}
\times_{S_{n+1}} S_{n} = p_{n}$.

Let $H = T \cdot_{\alpha} G_{a, S}$. The morphism $H_{S_{n}} \to G_{S_{n}}$ defined by $p_{n}$ is denoted $f_{n}$. Let
us admit the following lemma:

**Lemma 1.9.** *If $(G, T, \alpha)$ is a $k$-elementary system, $k$ algebraically closed, and if $p : G_{a, k} \to G$ is
a monomorphism normalized by $T$ with multiplier $\alpha$, one has*

```text
H²(T ·_α G_{a, k}, g) = 0.
```

*(One lets $T \cdot_{\alpha} G_{a, k}$ act on $g$ through the morphism $T \cdot_{\alpha} G_{a, k} \to G$ defined by $p$,
and the adjoint representation of $G$).*

<!-- label: III.XX.1.9 -->

Then, by virtue of Exp. III 2.8, $f_{n}$ extends to a morphism of $S_{n+1}$-groups

$$ f'_{n+1} : H_{S_{n+1}} \to G_{S_{n+1}}. $$

<!-- original page 42 -->

Now $f'_{n+1}$ and the canonical immersion of $T_{S_{n+1}}$ into $G_{S_{n+1}}$ have the same restriction to $T_{S_{n}}$.
By Exp. III 2.5, there exists an element $g \in G(S_{n+1})$ such that $g \times_{S_{n+1}} S_{n} = e$ and such that
$f_{n+1} = int(g) \circ f'_{n+1}$ restricts to $T_{n+1}$ along the canonical immersion of $T_{n+1}$. Let $p_{n+1}$ be
the restriction of $f_{n+1}$ to $G_{a, S_{n+1}}$. It is a morphism normalized by $T_{S_{n+1}}$ with multiplier
$\alpha_{S_{n+1}}$, which extends $p_{n}$.

One has thus constructed a coherent system $(f_{n})$ and one must now algebraize it. Now one has:

**Lemma 1.10.** *Let $A$ be a complete noetherian local ring, $m$ its maximal ideal, $S = \operatorname{Spec}(A)$,
$S_{n} = \operatorname{Spec}(A/m^{n+1})$, $T$ an $S$-torus, $\alpha$ a non-zero character of $T$, $X$ an affine
$S$-scheme on which $T$ acts. Let $T$ act on $G_{a, S}$ via $\alpha$. Let $q$ be an integer $\geqslant 0$, and let
$(f_{n})_{n \geqslant 0}$ be a coherent system of morphisms*

```text
f_n : G_{a, S_n}^q → X_{S_n}
```

*of objects with operators $T_{S_{n}}$. There exists a unique morphism of objects with operators $T$*

```text
f : G_{a, S}^q → X
```

*which induces the $f_{n}$ (compare with Exp. IX 7.1).*

<!-- label: III.XX.1.10 -->

**Corollary 1.11.** *If $X$ is a group with group of operators $T$ and if the $f_{n}$ are group morphisms, then $f$ is
one too.*

<!-- label: III.XX.1.11 -->

It suffices to apply the uniqueness assertion of the lemma to the two morphisms $G^{2q}_{a, S} \to X$ deduced from $f$
in the usual way.

<!-- original page 43 -->

*Proof of 1.10.* Suppose $T$ split, which is moreover the case in the application of 1.10 to the proof of 1.5. One knows
(Exp. I 4.7.3.1) that $X \mapsto A(X)$ realizes an equivalence between the category of affine $S$-schemes equipped with
a $T$-operation and the opposite category of $S$-graded algebras of type $M = \operatorname{Hom}_{S-gr.}(T, G_{m, S})$.

One therefore has gradings

```text
B = A(X) = ⨁_{m ∈ M} B_m    and    C = A(G_{a, S}^q) = ⨁_{m ∈ M} C_m.
```

One sees at once that each $C_{m}$ is free of finite type over $A$. (Indeed, one has $C_{m} = 0$ if $m$ is not a
multiple of $\alpha$, and if $m = d \alpha$, $C_{m}$ is isomorphic to the $A$-module of homogeneous polynomials of
degree $d$, in $q$ variables.) Set

```text
B̂_m = lim_n B_m ⊗_A (A/m^{n+1}),
Ĉ_m = lim_n C_m ⊗_A (A/m^{n+1}),
B̂ = ⨁_{m ∈ M} B̂_m,    Ĉ = ⨁_{m ∈ M} Ĉ_m.
```

One then has canonical morphisms of $M$-graded algebras

```text
g_B : B → B̂    and    g_C : C → Ĉ.
```

It follows from the remark made above that $g_{C}$ is an isomorphism. To give a coherent system $(f_{n})$ as in the
statement is equivalent to giving a morphism of graded $A$-algebras

$$ \hat{F} : \hat{B} \to \hat{C}. $$

To find a morphism $f$ as in the statement is equivalent to finding a morphism of graded $A$-algebras $F : B \to C$
rendering commutative the diagram

```text
B  ──F──→  C
│           │
g_B         g_C
↓           ↓
B̂  ──F̂──→  Ĉ.
```

Since $g_{C}$ is an isomorphism, the existence and uniqueness of $F$ are immediate. This proves 1.10.

<!-- original page 44 -->

To complete the proof of 1.5, it remains only to prove 1.9.

**1.12. Proof of 1.9.** One has $g = t \oplus g_{\alpha} \oplus g_{-\alpha}$. As explained in 1.9, consider $g$ as a $(T
\cdot_{\alpha} G_{a, k})$-module. It is clear that $t \oplus g_{\alpha}$ is a submodule of $g$, the quotient being
isomorphic to $g_{-\alpha}$ as a $k$-vector space and even as a $T$-module. It is clear that $G_{a, k}$ acts trivially
on this quotient, which is of dimension 1 (for every group morphism from $G_{a, k}$ to $G_{m, k}$ is trivial). Similarly
$g_{\alpha}$ is a submodule of $t \oplus g_{\alpha}$, the quotient being isomorphic to $t$ as a $T$-module, $G_{a, k}$
acting trivially on it. To summarize:

<!-- label: III.XX.1.12 -->

**Lemma 1.13.** *Under the conditions of 1.9, $g$ admits a composition series as $(T \cdot_{\alpha} G_{a, k})$-module
whose successive quotients are*

$$ g_{-\alpha}, t, g_{\alpha}, $$

*viewed as $(T \cdot_{\alpha} G_{a, k})$-modules via the projection $T \cdot_{\alpha} G_{a, k} \to T$.*

<!-- label: III.XX.1.13 -->

One is therefore reduced to computing the cohomology of $T \cdot_{\alpha} G_{a, k}$ acting via the projection $T
\cdot_{\alpha} G_{a, k} \to T$ and the character $\beta$ of $T$ (here $\beta = 0$, $\alpha$, or $-\alpha$) on
$W(k)$.[^N.D.E-XX-5] Let $k[x_{1}, \cdots, x_{n}]$ denote the algebra of polynomials over $k$ in $n$ variables and
$k_{q}[x_{1}, \cdots, x_{n}]$ the subspace of homogeneous polynomials of degree $q$.

**Lemma 1.14.** *With the preceding notations, one has $H^{n}(T \cdot_{\alpha} G_{a, k}, k) = H^{n}(C^{*}_{\alpha,
\beta})$, where the complex $C^{*}_{\alpha, \beta}$ is defined by*

<!-- original page 45 -->

```text
C^n_{α, β} = { k_q[x_1, …, x_n]   if β = q α, with q ∈ ℕ*;
             { 0                  otherwise,
```

*and*

```text
δf(x_1, x_2, …, x_{n+1}) = f(x_2, …, x_{n+1})
                         + Σ_{i=1}^n (−1)^i f(x_1, …, x_i x_{i+1}, …, x_{n+1})
                         + (−1)^{n+1} f(x_1, …, x_n).
```

<!-- label: III.XX.1.14 -->

Indeed, the functor $M \mapsto H^{0}(T, M)$ is exact on the category of $T$-modules (and the $H^{q}(T, -)$ vanish), by
Exp. I 5.3.2. It follows, as in the usual case of group cohomology, that $H^{n}(T \cdot_{\alpha} G_{a, k}, k)$ can be
computed as the $n$-th cohomology group of the complex of cochains of $G_{a, k}$ in $k$, invariant under $T$, i.e.
satisfying

```text
f(α(t) x_1, …, α(t) x_n) = β(t) f(x_1, …, x_n).
```

This indeed gives the announced complex.

To prove 1.9, it therefore suffices to prove that $H^{2}(C^{*}_{\alpha, \beta}) = 0$ for $\beta = 0, \alpha, -\alpha$,
which is done at once.

**Remark 1.15.** *One can explicitly compute the groups $H^{n}(C^{*}_{\alpha, \beta})$ for $\beta = q \alpha$ (see M.
Lazard,* Lois de groupes et analyseurs\*, Annales E.N.S., 1955). In particular, one finds $H^{n}(C^{*}_{\alpha, q
\alpha}) = 0$ for $n > q$.\*

<!-- label: III.XX.1.15 -->

**Notations 1.16.** *The image of the canonical immersion*

```text
W(g_{−α}) ×_S T ×_S W(g_α) → G
```

<!-- original page 46 -->

*will be denoted $\Omega$. It is an open subset of $G$ containing the unit section. The image of*

```text
W(g_{−α}),   resp. W(g_α),   resp. W(g_{−α}) ×_S T,   resp. T ×_S W(g_α)
```

*will be denoted*[^N.D.E-XX-6]

```text
U_{−α},   resp. U_α,   resp. U_{−α} · T,   resp. T · U_α.
```

*Then $U_{\alpha}$ (resp. $U_{-\alpha}$) is a subgroup of $G$ canonically endowed with a vector bundle structure, and
one has*

```text
int(t)(x) = x^{α(t)}    (resp. x^{−α(t)}),
```

*for every $S' \to S$, $t \in T(S')$, $x \in U_{\alpha}(S')$ (resp. $x \in U_{-\alpha}(S')$).*

<!-- label: III.XX.1.16 -->

One has canonical isomorphisms

```text
T · U_α ≅ T ·_α U_α    and    T · U_{−α} ≅ T ·_{−α} U_{−α}.
```

The open set $\Omega$ is stable under $int(T)$: one has

```text
int(t′)(y · t · x) = y^{−α(t′)} · t · x^{α(t′)}.
```

**Corollary 1.17.** *One has $Lie(U_{\alpha} / S) = g_{\alpha}$ and $Lie(U_{-\alpha} / S) = g_{-\alpha}$. The
isomorphisms*

```text
W(g_α)  ──exp──→  U_α    and    W(g_{−α})  ──exp──→  U_{−α}
```

*are those of Exp. XIX 4.2.*

<!-- label: III.XX.1.17 -->

**Corollary 1.18.** *The open set $\Omega$ is relatively schematically dense in $G$ (cf. XVIII, § 1).*

<!-- label: III.XX.1.18 -->

Clear by Exp. XVIII, 1.3.[^N.D.E-XX-7]

**Corollary 1.19.** *The center of $G$ is $Centr(G) = Ker(\alpha)$. It is therefore a closed subgroup of $G$, of
multiplicative type and of finite type.*

<!-- label: III.XX.1.19 -->

The second assertion follows from the first by Exp. IX 2.7. Let us therefore prove the first. The inner automorphism
defined by a section of $Ker(\alpha)$ acts trivially on $\Omega$ (last formula of 1.16), hence on $G$ by 1.18.
Conversely, if $g \in G(S)$ centralizes $G$, then it centralizes $T$ and $U_{\alpha}$, hence is a section of $T$ (Exp.
XIX 2.8) annihilating $\alpha$; since this also holds after any base change, one indeed has $Centr(G) = Ker(\alpha)$.

**Corollary 1.20.** *For there to exist a monomorphism $p_{\alpha} : G_{a, S} \to G$ normalized by $T$ with multiplier
$\alpha$, it is necessary and sufficient that the `O_S`-module $g_{\alpha}$ be free. More precisely, one has a bijection
given by*

```text
X_α ↦ (x ↦ exp(x X_α))    and    p_α ↦ Lie(p_α)
```

<!-- original page 47 -->

*between $\Gamma(S, g_{\alpha})^{\times}$ and the set of monomorphisms $p_{\alpha}$ as above (which is also the set of
isomorphisms of vector group schemes $G_{a, S} \xrightarrow{\sim} U_{\alpha}$).*[^N.D.E-XX-8]

<!-- label: III.XX.1.20 -->

**Corollary 1.21.** *The subgroups $U_{\alpha}$ and $U_{-\alpha}$ of $G$ commute on no fiber.*

<!-- label: III.XX.1.21 -->

Indeed, if $(U_{\alpha})_{s}$ and $(U_{-\alpha})_{s}$ commute, then $\Omega_{s}$ is a subgroup of $G_{s}$, hence
$\Omega_{s} = G_{s}$[^N.D.E-XX-9] and $G_{s}$ is solvable, which contradicts the hypothesis that $G_{s}$ is reductive of
semisimple rank 1.

## 2. Structure of elementary systems

<!-- label: III.XX.2 -->

**Theorem 2.1.** *Let $S$ be a scheme, $(G, T, \alpha)$ an $S$-elementary system. There exists a morphism of
`O_S`-modules*

```text
g_α ⊗_{O_S} g_{−α} → O_S,   (X, Y) ↦ ⟨X, Y⟩,
```

*and a morphism of $S$-groups*

```text
α* : G_{m, S} → T
```

*such that for every $S' \to S$ and all $X \in \Gamma(S', g_{\alpha} \otimes O_{S'})$, $Y \in \Gamma(S', g_{-\alpha}
\otimes O_{S'})$ one has the equivalence:*

```text
exp(X) · exp(Y) ∈ Ω(S′) ⇐⇒ 1 + ⟨X, Y⟩ ∈ G_m(S′),
```

*and under these conditions one has the formula:*

```text
(F)    exp(X) · exp(Y) = exp( Y / (1 + ⟨X, Y⟩) ) · α*(1 + ⟨X, Y⟩) · exp( X / (1 + ⟨X, Y⟩) ).
```

<!-- label: eq:III.XX.2.1.F -->

*Moreover, the morphisms $(X, Y) \mapsto \langle X, Y\rangle$ and $\alpha*$ are uniquely determined, the former is an
isomorphism, hence puts the modules $g_{\alpha}$ and $g_{-\alpha}$ in duality, and one has* $\alpha \circ \alpha* = 2$
*(squaring in $G_{m, S}$).*

<!-- label: III.XX.2.1 -->

<!-- original page 48 -->

In view of the uniqueness assertions of the theorem, it suffices to do the proof locally on $S$. One can therefore
assume $g_{\alpha}$ and $g_{-\alpha}$ free on $S$. Take then $X \in \Gamma(S, g_{\alpha})^{\times}$, $Y \in \Gamma(S,
g_{-\alpha})^{\times}$ and set $p_{\alpha}(x) = \exp(x X)$, $p_{-\alpha}(y) = \exp(y Y)$, for $x, y \in G_{a}(S')$, $S'
\to S$. By 1.5 and 1.21, it suffices to prove:

**Proposition 2.2.** *Let $S$ be a scheme, $G$ an $S$-group, $T$ a torus of $G$, $\alpha$ a character of $T$ non-trivial
on each fiber, $p_{\alpha} : G_{a, S} \to G$ (resp. $p_{-\alpha} : G_{a, S} \to G$) a group monomorphism normalized by
$T$ with multiplier $\alpha$ (resp. $-\alpha$). Suppose that:*

*(i) The morphism $G_{a, S} \times_{S} T \times_{S} G_{a, S} \to G$ defined by $(y, t, x) \mapsto p_{-\alpha}(y) t
p_{\alpha}(x)$ is an open immersion. Denote its image by $\Omega$.*

*(ii) For every $s \in S$, $(p_{\alpha})_{s}(G_{a, \kappa(s)})$ and $(p_{-\alpha})_{s}(G_{a, \kappa(s)})$ do not
commute.*

*Then there exist $a \in G_{a}(S)$ and $\alpha* \in \operatorname{Hom}_{S-gr.}(G_{m, S}, T)$, uniquely determined,
having the following properties: for every $S' \to S$ and all $x, y \in G_{a}(S')$, one has*

```text
p_α(x) p_{−α}(y) ∈ Ω(S′) ⇐⇒ 1 + a x y ∈ G_m(S′),
```

<!-- original page 49 -->

*and, under this condition, one has the formula*

```text
p_α(x) p_{−α}(y) = p_{−α}( y / (1 + a x y) ) · α*(1 + a x y) · p_α( x / (1 + a x y) ).
```

*Moreover, $a$ is invertible (i.e. $a \in G_{m}(S)$) and $\alpha \circ \alpha* = 2$.*

<!-- label: III.XX.2.2 -->

*Proof:*

A) Consider the morphism

$$ G^{2}_{a, S} \to G $$

defined by $(x, y) \mapsto p_{\alpha}(x) p_{-\alpha}(y)$. Let $U$ be the inverse image of $\Omega$ under this morphism.
It is an open subset of $G^{2}_{a, S}$ containing $0 \times_{S} G_{a, S}$ and $G_{a, S} \times_{S} 0$. There therefore
exist uniquely determined $S$-scheme morphisms

```text
A : U → G_{a, S},   C : U → G_{a, S},   B : U → T
```

satisfying the set-theoretic relation:

```text
p_α(u) p_{−α}(v) = p_{−α}(A(u, v)) B(u, v) p_α(C(u, v)).
```

One has immediately the relations

```text
A(0, v) = v,   A(u, 0) = 0,   C(u, 0) = u,   C(0, v) = 0,
B(u, 0) = B(0, v) = e.
```

Let $S'$ be a separated $S$-scheme and let $t \in T(S')$ be a point of $T$. Since $\Omega_{S'}$ is stable under
$int(t)$, then, by the last formula of 1.16, $U_{S'}$ is stable under the automorphism $(x, y) \mapsto (\alpha(t) x,
\alpha(t)^{-1} y)$ of $G^{2}_{a, S'}$, and one has the relations:

```text
A(α(t) u, α(t)⁻¹ v) = α(t)⁻¹ A(u, v),
C(α(t) u, α(t)⁻¹ v) = α(t) C(u, v),
B(α(t) u, α(t)⁻¹ v) = B(u, v).
```

Since $\alpha$ is faithfully flat, one deduces that for every $S' \to S$ and every $z \in G_{m}(S')$, $U_{S'}$ is stable
under the transformation $(x, y) \mapsto (z x, z^{-1} y)$ and one has

```text
A(z u, z⁻¹ v) = z⁻¹ A(u, v),
C(z u, z⁻¹ v) = z C(u, v),
B(z u, z⁻¹ v) = B(u, v).
```

Suppose first that $v$ is invertible; setting $z = v$, one deduces that if $(u, v)$ is a section of $U$, then `(u v, 1)`
is also one, and one has

```text
A(u v, 1) = v⁻¹ A(u, v),    B(u v, 1) = B(u, v).
```

Let then $V$ be the open set of $G^{2}_{a, S}$ defined by[^N.D.E-XX-10]

```text
(u, v) ∈ V(S′) ⇐⇒ (u, v), (u v, 1) and (1, u v) belong to U(S′).
```

<!-- original page 50 -->

Since $U$ is an open set of $G^{2}_{a, S}$ containing $0 \times_{S} G_{a, S}$ and $G_{a, S} \times_{S} 0$, then $V$ is a
neighborhood of the zero section of $G^{2}_{a, S}$ and we have just seen that the morphisms

```text
(u, v) ↦ A(u, v) and (u, v) ↦ v A(u v, 1)
resp. (u, v) ↦ B(u, v) and (u, v) ↦ B(u v, 1)
```

coincide on $V \cap (G_{a, S} \times_{S} G_{m, S})$. Since $G_{a, S} \times_{S} G_{m, S}$ is schematically dense in
$G^{2}_{a, S}$, these morphisms therefore coincide on $V$.

One knows that $A(0, 1) = 1$; it follows that there exists an open set `W_1` of $G_{a, S}$ containing the zero section
such that for every section $x$ of `W_1`, $A(x, 1)$ is invertible; setting $A(x, 1)^{-1} = F(x)$, one obtains that if
$(u, v) \in V(S')$[^N.D.E-XX-11] and $u v \in W_{1}(S')$, $S' \to S$, then $A(u, v) = v A(u v, 1) = v F(u v)^{-1}$.
Arguing similarly for $C$, one obtains that there exists an open set `W_2` of $G_{a, S}$ containing the zero section,
and an element $E$[^N.D.E-XX-12] of $O(W_{2})^{\times}$, such that $C(u, v) = u C(1, u v) = u E(u v)^{-1}$, if $(u, v)
\in V(S')$ and $u v \in W_{2}(S')$. Consequently, setting $W = W_{1} \cap W_{2}$, one obtains:

There exists an open set $W$ of $G_{a, S}$ containing the zero section, and $S$-morphisms

```text
F : W → G_{m, S},   F(0) = 1,
H : W → T,         H(0) = e,
E : W → G_{m, S},   E(0) = 1,
```

such that if $(u, v) \in V(S')$ and $u v \in W(S')$, $S' \to S$, one has

```text
(+)    p_α(u) p_{−α}(v) = p_{−α}(v F(u v)⁻¹) H(u v) p_α(u E(u v)⁻¹).
```

B) Let us now use the associativity of $G$ to write

```text
p_α(u) p_{−α}(v) p_{−α}(w) = p_α(u) p_{−α}(v + w).
```

There exists an open set $L$ of $G^{3}_{a, S}$, containing the unit section, such that $(u, v, w) \in L(S')$ is
equivalent to

```text
(u, v) ∈ V(S′),   (u E(u v)⁻¹, w) ∈ V(S′),   (u, v + w) ∈ V(S′),
u v ∈ W(S′),     u w E(u v)⁻¹ ∈ W(S′),       u(v + w) ∈ W(S′).
```

Using then the formula (+), one writes at once for $(u, v, w) \in L(S')$ the relations:

<!-- original page 51 -->

```text
(1)   E(u v + u w) = E(u w E(u v)⁻¹) E(u v),
(2)   H(u v + u w) = H(u w E(u v)⁻¹) H(u v),
(3)   (v + w) F(u v + u w)⁻¹ = α(H(u v)⁻¹) w F(u w E(u v)⁻¹)⁻¹ + v F(u v)⁻¹.
```

It is immediate from the definition of $L$ that $(1, 0, 0) \in L(S)$. Consider therefore

```text
L ∩_T (1 ×_S G_{a, S} ×_S G_{a, S}) = 1 ×_S M;
```

$M$ is an open set of $G^{2}_{a, S}$, containing the section `(0, 0)`, and for $(v, w) \in M(S')$, one has $v, w
E(v)^{-1}, v + w \in W(S')$ and

```text
(1′)   E(v + w) = E(w E(v)⁻¹) E(v),
(2′)   H(v + w) = H(w E(v)⁻¹) H(v),
(3′)   (v + w) F(v + w)⁻¹ = α(H(v))⁻¹ w F(w E(v)⁻¹)⁻¹ + v F(v)⁻¹.
```

Consider finally the morphism from $M$ to $G^{2}_{a, S}$ defined set-theoretically by $(v, w) \mapsto (v, w
E(v)^{-1})$.[^N.D.E-XX-13] It preserves the section `(0, 0)` and induces an isomorphism of $M$ onto an open set $N$ of
$G^{2}_{a, S}$ containing the zero section (the inverse isomorphism being given by $(x, y) \mapsto (x, y
E(x))$).[^N.D.E-XX-14] One has thus proved the following assertion:

There exists an open set $N$ of $G^{2}_{a, S}$, containing the zero section, such that if $(x, y) \in N(S')$, then
`x, y` and $x + y E(x)$[^N.D.E-XX-15] belong to $W(S')$ and:

```text
(1″)   E(x + y E(x)) = E(x) E(y),
(2″)   H(x + y E(x)) = H(x) H(y),
(3″)   (x + y E(x)) F(x + y E(x))⁻¹ = x F(x)⁻¹ + α(H(x))⁻¹ y E(x) F(y)⁻¹.
```

C) Arguing similarly with left associativity, one demonstrates the following assertion:[^N.D.E-XX-16]

There exists an open set $N'$ of $G^{2}_{a, S}$, containing the zero section, such that if $(x, y) \in N'(S')$, then
`x, y` and $x + y F(x)$[^N.D.E-XX-17] belong to $W(S')$, and

<!-- original page 52 -->

```text
(4″)   F(x + y F(x)) = F(x) F(y),
(5″)   H(x + y F(x)) = H(x) H(y),
(6″)   (x + y F(x)) E(x + y F(x))⁻¹ = x E(x)⁻¹ + α(H(x))⁻¹ y F(x) E(y)⁻¹.
```

We are therefore led to solve the "functional equation" (1″).

**Lemma 2.3.** *Let $S$ be a scheme, $W$ an open set of $G_{a, S}$ containing the unit section, $F : W \to G_{m, S}$ an
$S$-morphism. Suppose that $F(0) = 1$ and that there exists an open set $N$ of $G^{2}_{a, S}$ containing the zero
section such that for $(x, y) \in N(S')$, `x, y`, and $x + y F(x)$[^N.D.E-XX-17] belong to $W(S')$ and that one has:*

```text
(†)    F(x + y F(x)) = F(x) F(y).
```

*(i) If $S$ is the spectrum of a field $k$, there exists $a \in k$ such that $F(x) = 1 + a x$.*

*(ii) If $a = F'(0) \in \Gamma(S, O_{S})$ is invertible, then $F(x) = 1 + a x$.*

<!-- label: III.XX.2.3 -->

By the hypotheses, we can differentiate the given equation at $x = 0$ (resp. at $y = 0$) and we find that

```text
(∗)    F′(y) (1 + y F′(0)) = F′(0) F(y)    for (0, y) ∈ N(S′),
```

resp.

```text
F′(x) F(x) = F(x) F′(0)    for (x, 0) ∈ N(S′).
```

Since $F$ takes its values in $G_{m}$, the second relation gives us

```text
(∗′)   F′(x) = F′(0)    for (x, 0) ∈ N(S′);
```

whence, by the first,

```text
F′(0)(1 + y F′(0)) = F′(0) F(y)    for (y, 0), (0, y) ∈ N(S′).
```

If $a = F'(0)$ is invertible, this gives us

<!-- original page 53 -->

```text
F(y) = 1 + a y,
```

for $y$ a section of an open set of $W$ containing the unit section, hence schematically dense in $W$, which proves
(ii). This also proves (i) when $F'(0) \neq 0$.

If $F'(0) = 0$, then, by (∗′), $F'(x) = 0$ when $x$ is "near 0", hence $F' = 0$ by schematic density. If $k$ is of
characteristic 0, $F$ is a rational fraction with zero derivative, hence constant and equal to $F(0) = 1$.

If $k$ is of characteristic $p$, and if $F$ is not constant,[^N.D.E-XX-18] there exists an integer $n > 0$ and a
rational fraction $F_{1} \in k(X)$ such that $F'_{1}(X) \neq 0$ and

$$ F(X) = F_{1}(X^{p^{n}}) = F_{1}(X)^{p^{n}}. $$

Substituting in the functional equation, one finds

```text
(†_1)   F_1(x + y F_1(x)^{p^n}) = F_1(x) F_1(y).
```

Differentiating at $x = 0$, one finds

$$ (\ast_{1}) F'_{1}(y) = F'_{1}(0) F_{1}(y), $$

and differentiating (†\_1) at $y = 0$, one obtains

```text
(∗′_1)  F′_1(x) F_1(x)^{p^n} = F_1(x) F′_1(0).
```

Since, by hypothesis, $F'_{1}(X)$ is an invertible element of $k(X)$, one deduces from these two equalities that

$$ F_{1}(X)^{p^{n}} = 1, $$

hence `F_1` is a constant, contradicting the initial hypothesis. This shows that $F$ is constant, and equal to $1 =
F(0)$.

D) Suppose $S$ is the spectrum of a field. If $F'(0) = 0$, then $F = 1$. Formula (5″) then gives us $H(x + y) = H(x)
H(y)$, which shows that $H$ extends to a group morphism $G_{a, S} \to T$ (Exp. XVIII 2.3), which is necessarily constant
of value $e$. On the other hand, by Lemma 2.3, one will also have $E(x) = 1 + b x$ for some $b \in k$. But then (6″)
gives, for $(x, y) \in N(S')$,

```text
(x + y) E(x + y)⁻¹ = x E(x)⁻¹ + y E(y)⁻¹,
```

hence,[^N.D.E-XX-19] by Exp. XVIII 2.3 again, $x \mapsto x E(x)^{-1}$ extends to a morphism of $k$-groups $G_{a, k} \to
G_{a, k}$, hence $x/(1 + b x) = c x$ for some $c \in k$, whence $b = 0$ (and $c = 1$).

<!-- original page 54 -->

This shows that `F, H, E` are constant of value `(1, e, 1)` in a neighborhood of the unit section, hence everywhere,
which by (+) shows that $U_{\alpha}$ and $U_{-\alpha}$ commute, contrary to hypothesis (ii).

If $S$ is now arbitrary, one has therefore proved that $F'(0)$ is non-zero on no fiber, hence is invertible. The same
evidently holds for $E'(0)$, which by Lemma 2.3 shows that there exist $a, b \in G_{m}(S)$ such that

```text
(♦_1)   F(x) = 1 + a x,    E(x) = 1 + b x,    for x ∈ W(S′).
```

E) The rest is now easy. Substituting the preceding results into (3″), one finds

```text
y α(H(x)) (1 + a y) = y (1 + a x + a y(1 + b x)) (1 + a x).
```

This formula is valid for every section $(x, y)$ of $N$. But since $G_{a, S} \times_{S} G_{m, S}$ is schematically dense
in $G^{2}_{a, S}$, one deduces

```text
(1 + a y) α(H(x)) = (1 + a x + a y(1 + b x)) (1 + a x).
```

Setting $y = 0$, this gives $\alpha(H(x)) = (1 + a x)^{2}$. Substituting this into the preceding equality, one
finds[^N.D.E-XX-20]

```text
a² x y = a b x y.
```

Since $G_{m, S}$ is schematically dense in $G_{a, S}$, one deduces $a^{2} = a b$, whence, since $a$ is invertible,

```text
(♦_2)   a = b    and    α(H(x)) = (1 + a x)².
```

Since $a$ is invertible, $x \mapsto 1 + a x$ is an automorphism of $G_{a, S}$; one can therefore find an open set $W'$
of $G_{a, S}$ containing the section `1` and a morphism

$$ P : W' \to T $$

such that $P(1 + a x) = H(x)$.[^N.D.E-XX-21]

Substituting in the relation (2′), one finds at once for $(x, y) \in N(S')$,

```text
P(1 + a x + a y) = P((1 + a x + a y) / (1 + a x)) P(1 + a x),
```

which proves that there exists an open neighborhood of `1` in $G_{m, S}$ such that one has for $x$ and $y$ in this
neighborhood $P(x) P(y) = P(x y)$. By Exp. XVIII 2.3, there exists a group morphism

```text
(♦_3)   α* : G_{m, S} → T
```

<!-- original page 55 -->

extending $P$. Since $\alpha(H(x)) = (1 + a x)^{2}$ near the section `0`, one has $\alpha(\alpha*(z)) = z^{2}$ near the
section `1`, hence

```text
(♦_4)   α ∘ α* = 2.
```

F)[^N.D.E-XX-22] Assembling the results (+) and (♦\_1 — ♦\_4), one sees that there exist $a \in G_{m}(S)$ and $\alpha*
\in \operatorname{Hom}_{S-gr.}(G_{m, S}, T)$ such that $\alpha \circ \alpha* = 2$ and that, if $(u, v) \in V(S')$ and $u
v \in W(S')$, then $1 + a u v$ is invertible and

```text
p_α(u) p_{−α}(v) = p_{−α}( v / (1 + a u v) ) · α*(1 + a u v) · p_α( u / (1 + a u v) ).
```

Consider the open set $V'$ of $G^{2}_{a, S}$ defined by "$1 + a u v$ invertible", i.e. $V' = (G^{2}_{a, S})_{f}$ where
$f(u, v) = 1 + a u v$. The two sides of the preceding formula define morphisms from $V'$ to $G$ which coincide in a
neighborhood of the section `0`, hence coincide on $V'$. The preceding formula is therefore valid for every section $(u,
v)$ of $V'$. In particular, it follows that $V' \subset U$, where $U$ is the open set introduced at the beginning of A).

Let us prove that $U = V'$. Returning to the notations of A), one has a morphism

```text
A : U → G_{a, S}
```

which, on $V'$, is defined by $A(u, v) = v (1 + a u v)^{-1}$. To show that $U = V'$, which is a set-theoretic question,
one is reduced to the case where $S$ is the spectrum of a field $k$, hence to the obvious assertion: the domain of
definition of the rational map $G^{2}_{a, k} \to G_{a, k}$ defined by the rational fraction $Y / (1 + a X Y)$ is the
open set defined by the function $1 + a X Y$.

G) One has thus proved the existence of $a$ and $\alpha*$, as well as the two additional properties announced. It
remains to prove uniqueness. Let then $a'$ and $\alpha*'$ also satisfy the required conditions. If $u, v \in
G_{a}(S')^{2}$, one has at once:

<!-- original page 56 -->

```text
1 + a u v invertible ⇒ 1 + a′ u v invertible and v / (1 + a u v) = v / (1 + a′ u v);
```

one therefore has for every section $u$ of $G_{a}(S')$

```text
1 + a u invertible ⇒ 1 + a u = 1 + a′ u,
```

which proves at once $a = a'$.

With the same notations, one then has

```text
1 + a u invertible ⇒ α*(1 + a u) = α*′(1 + a u),
```

hence also $\alpha* = \alpha*'$.

**Corollary 2.4.** *Let $\exp(Y) t \exp(X)$ and $\exp(Y') t' \exp(X')$ be two elements of $\Omega(S')$. Then their
product is in $\Omega(S')$ if and only if $u = 1 + \langle X, Y'\rangle$ is invertible, and one has then*

```text
(F′)    exp(Y) t exp(X) · exp(Y′) t′ exp(X′) =
             exp(Y + u⁻¹ α(t)⁻¹ Y′) · t t′ α*(u) · exp(u⁻¹ α(t′)⁻¹ X + X′).
```

<!-- label: III.XX.2.4 -->

**Remark 2.5.** *One can also write formula (F) of Theorem 2.1 without invoking the morphisms `exp`. Indeed,
transporting through these morphisms the duality $g_{\alpha} \otimes g_{-\alpha} \to O_{S}$, one obtains a canonical
pairing of vector bundles:*

```text
U_α ×_S U_{−α} → G_{a, S},
```

*which we shall still denote $(x, y) \mapsto \langle x, y\rangle$. One therefore has*

```text
⟨exp X, exp Y⟩ = ⟨X, Y⟩.
```

*If $x \in U_{\alpha}(S')$, $y \in U_{-\alpha}(S')$ and if $1 + \langle x, y\rangle \in G_{m}(S')$, one has*

```text
(F)    x · y = y^{(1 + ⟨x, y⟩)⁻¹} · α*(1 + ⟨x, y⟩) · x^{(1 + ⟨x, y⟩)⁻¹}.
```

<!-- label: III.XX.2.5 -->

**Corollary 2.6.** *The pairing*

```text
W(g_α) ×_S W(g_{−α}) → G_{a, S}
```

<!-- original page 57 -->

*defines a pairing of principal $G_{m, S}$-bundles*

```text
W(g_α)^× ×_S W(g_{−α})^× → G_{m, S}.
```

*This pairing will be denoted $(X, Y) \mapsto \langle X, Y\rangle$, or more simply $(X, Y) \mapsto X Y$.*

<!-- label: III.XX.2.6 -->

For every section $X \in \Gamma(S, g_{\alpha})^{\times}$, there therefore exists a unique section $X^{-1}$ of $\Gamma(S,
g_{-\alpha})^{\times}$ such that $X X^{-1} = 1$. One has $(z X)^{-1} = z^{-1} X^{-1}$. The morphism

$$ s : W(g_{\alpha})^{\times} \to W(g_{-\alpha})^{\times} $$

thus defined is therefore an isomorphism of schemes, compatible with the isomorphism $s : z \mapsto z^{-1}$ on the
operator groups.

**Definition 2.6.1.** *One says that $X$ and $s(X) = X^{-1}$ are* paired.

<!-- label: III.XX.2.6.1 -->

Apply Corollary 2.4 to $Y = 0 = X'$ and $Y' = a X^{-1}$, $a \in O_{S}(S)$. Then $u = 1 + a$ and
$u^{-1} Y' = u^{-1}(u - 1) X^{-1} = (1 - u^{-1}) X^{-1}$, whence:

**Corollary 2.7.** *Let $X \in \Gamma(S, g_{\alpha})^{\times}$ and $u \in \Gamma(S, O_{S})^{\times}$. One has*

```text
α*(u) = exp((u⁻¹ − 1) X⁻¹) exp(X) exp((u − 1) X⁻¹) exp(−u⁻¹ X).
```

<!-- label: III.XX.2.7 -->

**Definition 2.8.** *The morphism $\alpha*$ is called the* coroot *associated with the root $\alpha$.*

<!-- label: III.XX.2.8 -->

**Remark 2.9.** *If $(G, T, \alpha)$ is an $S$-elementary system, $(G, T, -\alpha)$ is also one. By Theorem 2.1 one
therefore has a duality between $g_{-\alpha}$ and $g_{\alpha}$, and a coroot $(-\alpha)*$. Taking the inverse of formula
(F), one proves at once*

```text
⟨X, Y⟩ = ⟨Y, X⟩,    (−α)* = −α*.
```

<!-- label: III.XX.2.9 -->

Let us now pass to the Lie algebra of $G$. The root $\alpha$ and the coroot $\alpha*$ define the linear forms

```text
O_S  ──α*──→  t  ──α──→  O_S.
```

<!-- original page 58 -->

One will denote $H_{\alpha} = \alpha*(1)$. One calls $\alpha$ the *infinitesimal root* associated with $\alpha$, and
$H_{\alpha}$ the corresponding *infinitesimal coroot*.

**Lemma 2.10.** *Let $S' \to S$ and $X, X' \in W(g_{\alpha})(S')$, $H \in W(t)(S')$, $Y, Y' \in W(g_{-\alpha})(S')$, $t
\in T(S')$. One has*

```text
(1)   Ad(t) H = H,    Ad(t) X = α(t) X,    Ad(t) Y = α(t)⁻¹ Y.
```

```text
(2)   { Ad(exp(X)) H = H − α(H) X,    Ad(exp(X)) X′ = X′,
      { Ad(exp(X)) Y = Y + ⟨X, Y⟩ H_α − ⟨X, Y⟩ X.
```

```text
(2′)  { Ad(exp(Y)) H = H + α(H) Y,    Ad(exp(Y)) Y′ = Y′,
      { Ad(exp(Y)) X = X + ⟨X, Y⟩ H_{−α} − ⟨X, Y⟩ Y.
```

```text
(3)   [H, X] = α(H) X,    [H, Y] = −α(H) Y,    [X, Y] = ⟨X, Y⟩ H_α.
```

$$ (4) H_{-\alpha} = -H_{\alpha}. $$

$$ (5) \alpha(H_{\alpha}) = 2. $$

<!-- label: III.XX.2.10 -->

The proof of these various formulas is either trivial or an immediate consequence of formula (F) of 2.1.

**Corollary 2.11.** *Suppose $H_{\alpha}$ is non-zero on every fiber (which is in particular the case if `2` is
invertible on $S$, by (5)). Then $X_{\alpha} \in \Gamma(S, g_{\alpha})^{\times}$ and $X_{-\alpha} \in \Gamma(S,
g_{-\alpha})^{\times}$ are paired if and only if $[X_{\alpha}, X_{-\alpha}] = H_{\alpha}$.*

<!-- label: III.XX.2.11 -->

<!-- original page 59 -->

**2.12.** Let $(G, T, \alpha)$ be an $S$-elementary system. We know (1.19) that the center of $G$ is $Centr(G) =
Ker(\alpha)$, a group of multiplicative type and of finite type. If $Q$ is a subgroup of multiplicative type of
$Centr(G)$, the quotient $G/Q$ is affine over $S$ (Exp. IX 2.5), smooth over $S$ (Exp. VI_B 9.2) with connected
reductive fibers of semisimple rank 1 (Exp. XIX 1.8).

Set $G' = G/Q$; this is a reductive $S$-group of semisimple rank 1; $T' = T/Q$ is a maximal torus of it. The open set
$U_{-\alpha} \cdot T \cdot U_{\alpha}$ of $G$ is stable under $Q$, and one sees at once that the quotient is isomorphic
to $U_{-\alpha} \times_{S} (T/Q) \times_{S} U_{\alpha}$. If one denotes by $\alpha'$ the character of $T'$ induced by
$\alpha$, it follows that the morphism derived from the canonical morphism $G \to G'$ induces isomorphisms

```text
g_α  ──∼──→  g′_{α′}    and    g_{−α}  ──∼──→  g′_{−α′}.
```

In particular, $\alpha'$ is a root of $G'$ with respect to $T'$. Hence, denoting by $\alpha/Q$ the character $T/Q \to
G_{m, S}$ induced by $\alpha$, one has:

**Lemma 2.13.** *If $Q$ is a subgroup of multiplicative type of $Ker(\alpha)$, then*

$$ (G/Q, T/Q, \alpha/Q) $$

*is an elementary system.*

<!-- label: III.XX.2.13 -->

<!-- original page 60 -->

**Lemma 2.14.** *Under the preceding conditions, the following diagrams are commutative:*

```text
W(g_α)  ──exp──→  G  ←──exp──  W(g_{−α})
   │                │                │
   can ≀            can              can ≀
   ↓                ↓                ↓
W(g′_{α′})  ──exp──→  G′  ←──exp──  W(g′_{−α′})
```

```text
g_α ⊗ g_{−α}  ──∼──→  O_S
     │                  │
     can ≀              id
     ↓                  ↓
g′_{α′} ⊗ g′_{−α′}  ──∼──→  O_S
```

```text
              T
        α*  ↗  ↘ α
G_{m, S}        G_{m, S}
        ↓ can   ↑
G_{m, S}  ⤴  ⤵  G_{m, S}
       α′*  ↘  ↗ α′
              T′
```

<!-- label: III.XX.2.14 -->

## 3. The Weyl group

<!-- label: III.XX.3 -->

<!-- original page 60 -->

**Notations 3.0.**[^N.D.E-XX-23] If $(G, T, \alpha)$ is an $S$-elementary system, one will denote

```text
N = Norm_G(T),    W = Norm_G(T) / T,
```

(cf. Exp. XIX 6.3); $N$ is a closed subgroup of $G$, smooth over $S$. One will denote by $N^{\times} = N - T$ the open
subscheme of $N$ induced on the complement of $T$.[^N.D.E-XX-24] Let $R$ be the (unique) maximal torus of $Ker(\alpha)$,
and $T'$ the image of $\alpha* : G_{m, S} \to T$, which is a subtorus of dimension 1 of $T$.

The morphism

```text
T′ ×_S R → T
```

induced by the product in $T$ is surjective (hence faithfully flat); indeed, one is reduced to checking this on the
geometric fibers, and this follows at once from the formula $\alpha \circ \alpha* = 2$.

**Theorem 3.1.** *With the preceding notations:*

*(i) $W$ is isomorphic to the constant group $(\mathbb{Z}/2\mathbb{Z})_{S}$.*

<!-- original page 61 -->

*(ii) $N^{\times}$ is a principal homogeneous bundle locally trivial under $T$, on the left by the law $(t, q) \mapsto t
q$ (resp. on the right by the law $(q, t) \mapsto q t$).*

*(iii) One has the formula*

```text
int(w) t = t · α*(α(t)⁻¹)
```

*for $w \in N^{\times}(S')$, $t \in T(S')$, $S' \to S$. In the decomposition $T_{S'} = T'_{S'} \cdot R_{S'}$, $int(w)$
induces the identity on $R_{S'}$ and the symmetry on $T'_{S'}$. One has the relations*

```text
α ∘ int(w) = α⁻¹,    int(w) ∘ α* = (α*)⁻¹.
```

*(iv) For $X \in W(g_{\alpha})^{\times}(S')$, $S' \to S$, set*

```text
w_α(X) = exp(X) exp(−X⁻¹) exp(X).
```

*Then $w_{\alpha}(X) \in N^{\times}(S')$ and the morphism $w_{\alpha} : W(g_{\alpha})^{\times} \to N^{\times}$ thus
defined satisfies*

```text
w_α(z X) = α*(z) w_α(X) = w_α(X) α*(z)⁻¹,
```

*for $z \in G_{m}(S')$, $X \in W(g_{\alpha})^{\times}(S')$, $S' \to S$.*

*(v)[^N.D.E-XX-25] For $X, Y \in W(g_{\alpha})^{\times}(S')$, $S' \to S$, one has, with the notations of 2.6,*

```text
w_α(X) w_α(Y) = α∨(−X Y⁻¹).
```

*In particular,*

```text
w_α(X)² = α*(−1) ∈ ₂T(S) ∩ Centr(G)(S),
w_α(X)⁻¹ = w_α(−X) = α*(−1) w_α(X).
```

*(vi) If one defines analogously, for $Y \in W(g_{-\alpha})^{\times}(S')$,*

```text
w_{−α}(Y) = exp(Y) exp(−Y⁻¹) exp(Y),
```

*one has (in addition to formulas analogous to the preceding)*

```text
w_{−α}(X⁻¹) = w_α(X)⁻¹ = w_α(−X),
w_α(X) w_{−α}(Y) = α*(X Y).
```

<!-- label: III.XX.3.1 -->

*Proof.* (i) has already been seen in Exp. XIX 2.4; it follows at once that $N^{\times}$ is indeed a principal
homogeneous bundle under $T$ for the laws defined in (ii); the fact that it is locally trivial (for the Zariski
topology) follows notably from (iv).

<!-- original page 62 -->

Let us prove (iii); if $w \in N^{\times}(S)$, it is clear that $\alpha \circ int(w)$ is a root of $G$ with respect to
$T$, hence is locally equal to $\alpha$ or $-\alpha$; since on each fiber it is $-\alpha$ (*Bible*, 12-05, proof of the
corollary to prop. 1), one has $\alpha \circ int(w) = -\alpha$. By transport of structure, one deduces

```text
−α* = int(w)⁻¹ ∘ α* = int(w) ∘ α*,
```

since $int(w)^{2} = int(w^{2})$ and $w^{2}$ is a section of $T$. Therefore $int(w)$ induces the symmetry on $T'$; since
$R$ is central, $int(w)$ induces the identity on $R$. The formula of (iii) defines a morphism $T \to T$ which satisfies
the same properties, hence coincides with $int(w)$.

Let us prove (iv). One has successively

```text
w_α(X) t w_α(X)⁻¹ = exp(X) exp(−X⁻¹) exp(X) t exp(−X) exp(X⁻¹) exp(−X)
                  = exp(X) exp(−X⁻¹) exp(X − α(t) X) exp(α(t)⁻¹ X⁻¹) exp(−α(t) X) t.
```

By application of formula (F), one has

```text
exp(−X⁻¹) exp((1 − α(t)) X) = exp((α(t)⁻¹ − 1) X) α*(α(t)⁻¹) exp(−α(t)⁻¹ X⁻¹).
```

Substituting in the preceding relation, one finds

```text
int(w_α(X)) t = exp(α(t)⁻¹ X) α*(α(t)⁻¹) exp(−α(t) X) t
              = exp(a X) α*(α(t)⁻¹) t,
```

where

```text
a = α(t)⁻¹ − (α ∘ α*)(α(t)⁻¹) α(t),
```

but $\alpha \circ \alpha* = 2$, which gives at once $a = 0$ and $w_{\alpha}(X) \in N^{\times}(S')$.

Let us prove the second assertion of (iv). One has[^N.D.E-XX-26]

```text
α*(z) w_α(X) = exp(z² X) exp(−z⁻² X⁻¹) exp(z² X) α*(z)
             = exp(z X) exp((z² − z) X) exp(−z⁻² X⁻¹) exp(z² X) α*(z)
             = exp(z X) exp(−z⁻¹ X⁻¹) α*(z)⁻¹ exp((z³ − z²) X) exp(z² X) α*(z)
             = exp(z X) exp(−z⁻¹ X⁻¹) exp(z X) = w_α(z X).
```

<!-- original page 63 -->

Let us prove (v). By virtue of the preceding result, the first formula of (v) follows at once from the second; let us
prove the second:

```text
w_α(X)² = exp(X) exp(−X⁻¹) exp(2 X) exp(−X⁻¹) exp(X)
        = exp(X) exp(−X⁻¹) exp(X⁻¹) α*(−1) exp(−2 X) exp(X)
        = exp(X) α*(−1) exp(−X) = α*(−1),
```

since $\alpha(\alpha*(-1)) = (-1)^{2} = 1$, which proves that $\alpha*(-1) \in Centr(G)(S)$.

Let us prove (vi). The first assertion is a particular case of the second; let us prove the second. Both sides of this
formula define morphisms $W(g_{\alpha})^{\times} \times_{S} W(g_{-\alpha})^{\times} \to G$. To prove that they coincide,
it suffices to do so on a non-empty open set on each fiber (Exp. XVIII 1.4); it therefore suffices to verify the
relation when $1 + X Y$ is invertible. One then has successively:

```text
w_α(X) w_{−α}(Y) = exp(X) exp(−X⁻¹) exp(X) exp(Y) exp(−Y⁻¹) exp(Y)
                 = exp(X) exp(−X⁻¹) exp(Y / (1 + X Y)) α*(1 + X Y) exp(X / (1 + X Y)) exp(−Y⁻¹) exp(Y)
                 = exp(X) exp(−X⁻¹ / (1 + X Y)) α*(1 + X Y) exp(−Y⁻¹ / (1 + X Y)) exp(Y)
                 = exp(−X⁻² Y⁻¹) α*(X Y / (1 + X Y)) exp(X + Y⁻¹) α*(1 + X Y) exp(−Y⁻¹ / (1 + X Y)) exp(Y)
                 = exp(−X⁻² Y⁻¹) α*(X Y) exp((Y⁻¹ + X) / (1 + X Y)²) exp(−Y⁻¹ / (1 + X Y)) exp(Y)
                 = α*(X Y) exp(−Y) exp(Y) = α*(X Y).
```

<!-- original page 64 -->

**Corollary 3.2.** *Let $n \in \mathbb{Z}$, $n \neq 0$. For every $w \in G(S)$, the following conditions are
equivalent:*

*(i) $w \in N^{\times}(S)$,*

*(ii) one has $int(w) \circ n \alpha* = -n \alpha*$ (recall that $(n \alpha*)(z) = \alpha*(z)^{n}$).*

<!-- label: III.XX.3.2 -->

One has (i) ⇒ (ii) (assertion (iii) of Theorem 3.1); conversely, one may suppose that $N^{\times}$ admits a section, and
one is reduced to proving:

**Lemma 3.3.** *One has $Centr_{G}(n \alpha*) = T$ for $n \neq 0$.*

<!-- label: III.XX.3.3 -->

Indeed, the image $T'$ of $n \alpha*$ is a subtorus of $G$. It follows (Exp. XIX 2.8) that $Centr_{G}(n \alpha*)$ is a
reductive subgroup of $G$ containing $T$. Since on each fiber one has $Centr_{G_{s}}(n \alpha*_{s}) \neq G_{s}$, then
$Centr_{G_{s}}(n \alpha*_{s}) = T_{s}$ (Exp. XIX 1.6.3)[^N.D.E-XX-27], hence $Centr_{G}(n \alpha*) = T$, since these are
smooth subgroups of $G$.

**Remark 3.4.** *The construction of $w_{\alpha}$ and the fact that $w_{\alpha}(X)$ normalizes $T$ rely only on formula
(F). In particular, if $G$ is an $S$-group satisfying the conditions of 2.2, $Norm_{G}(T)$ differs from $T$ on each
fiber. It follows that if $G$ is an affine $S$-group with connected fibers satisfying the conditions of 2.2, it is
reductive of semisimple rank 1. Indeed, it is smooth in a neighborhood of the unit section, hence smooth, and one can
apply the criterion of Exp. XIX 1.11.*

<!-- label: III.XX.3.4 -->

**3.5.** Before stating the following theorem, let us make a few remarks. We identify as usual $g_{-\alpha}$ with
$(g_{\alpha})^{\otimes-1}$. Similarly, we shall identify $\operatorname{Hom}_{O_{S}}(g_{-\alpha}, g_{\alpha})$ with
$(g_{\alpha})^{\otimes 2}$ and hence

<!-- original page 65 -->

$$ Isom_{O_{S}-mod.}(W(g_{-\alpha}), W(g_{\alpha})) \cong W((g_{\alpha})^{\otimes 2})^{\times}. $$

If $w \in N^{\times}(S)$, then $Ad(w)$ permutes $g_{\alpha}$ and $g_{-\alpha}$ (3.1, (iii)), hence defines an
isomorphism:

```text
a_α(w) : g_{−α} ──∼──→ g_α,
```

which we shall therefore identify with a section $a_{\alpha}(w) \in \Gamma(S, (g_{\alpha})^{\otimes 2})^{\times}$. This
construction is compatible with base change and therefore defines a morphism

$$ a_{\alpha} : N^{\times} \to W((g_{\alpha})^{\otimes 2})^{\times}, $$

such that $a_{\alpha}(w) Y = Ad(w) Y$ for all $w \in N^{\times}(S')$, $Y \in \Gamma(S', g_{-\alpha})^{\times}$, $S' \to
S$.

**Theorem 3.6.** *(i) One has*

```text
int(w) exp(Y) = exp(a_α(w) Y)
```

*for every $S' \to S$ and all $w \in N^{\times}(S')$, $Y \in W(g_{-\alpha})(S')$.*

*(ii) One has*

```text
a_α(t w) = α(t) a_α(w),    a_α(w t) = α(t)⁻¹ a_α(w).
```

*(iii) If one defines analogously $a_{-\alpha} : N^{\times} \to W((g_{-\alpha})^{\otimes 2})^{\times}$, one has*

$$ a_{-\alpha}(w) = a_{\alpha}(w)^{-1}. $$

[^N.D.E-XX-28]

*(iv) For every $X \in W(g_{\alpha})^{\times}(S')$, $S' \to S$, one has*

$$ a_{\alpha}(w_{\alpha}(X)) = -X^{2}. $$

<!-- label: III.XX.3.6 -->

<!-- original page 66 -->

Assertion (i) is trivial, by the characterization of the morphisms `exp` given in 1.5. Assertion (ii) is immediate, as
is (iii). Let us prove (iv): let $X \in \Gamma(S', g_{\alpha})^{\times}$, $Z \in \Gamma(S', g_{\alpha})$; by
definition[^N.D.E-XX-29]

```text
a_α(w_α(X))⁻¹(Z) = Ad(w_α(X))(Z) = Ad(exp(X)) Ad(exp(−X⁻¹)) Ad(exp(X))(Z).
```

Applying formulas (2′) and (2) of Lemma 2.10, as well as the equalities $H_{-\alpha} = -H_{\alpha}$, $\alpha(H_{\alpha})
= 2$ (*loc. cit.* (4) and (5)) and $\langle X, X^{-1}\rangle = 1$ (2.6), one obtains that the right-hand side equals
successively:

```text
Ad(exp(X)) Ad(exp(−X⁻¹))(Z) = Ad(exp(X))(Z + ⟨X⁻¹, Z⟩ (H_α − X⁻¹))
                            = Z + ⟨X⁻¹, Z⟩ (H_α − 2 X − X⁻¹ − H_α + X)
                            = Z − ⟨X⁻¹, Z⟩ X − ⟨X⁻¹, Z⟩ X⁻¹.
```

But $Z = \langle X^{-1}, Z\rangle X$ and $\langle X^{-1}, Z\rangle X^{-1} = X^{-2} Z$, hence this shows that
$a_{\alpha}(w_{\alpha}(X))^{-1} = -X^{-2}$, whence $a_{\alpha}(w_{\alpha}(X)) = -X^{2}$.

**Corollary 3.7.** *One has in particular*

```text
int(w_α(X)) exp(X) = exp(−X⁻¹),
```

*whence (by the definition of $w_{\alpha}(X)$):*

```text
w_α(X) exp(X) w_α(X)⁻¹ = exp(−X) w_α(X) exp(−X),
```

*or, by an immediate calculation,*

$$ (w_{\alpha}(X) \exp(X))^{3} = e. $$

<!-- label: III.XX.3.7 -->

**Corollary 3.8.** *Let $X \in \Gamma(S, g_{\alpha})^{\times}$ and $n \in \mathbb{Z}$, $n \neq 0$. Then $w_{\alpha}(X)$
is the unique section $w \in G(S)$ satisfying*

*(i) $int(w) \circ n \alpha* = -n \alpha*$.*

*(ii) $(w \exp(X))^{3} = e$.*

<!-- label: III.XX.3.8 -->

<!-- original page 67 -->

One knows that $w_{\alpha}(X)$ does satisfy these conditions. Conversely, let $w \in G(S)$ satisfy (i) and (ii). By 3.2
and 3.1 (ii), one knows that there exists $t \in T(S)$ such that $w = w_{\alpha}(X) t$. Set $u = \exp(X)$. One then has

```text
w u w⁻¹ = w_α(X) t exp(X) t⁻¹ w_α(X)⁻¹ = exp(−α(t) X⁻¹),
```

and on the other hand

```text
u⁻¹ w u⁻¹ = exp(−X) w_α(X) t exp(−X)
          = exp(−X) w_α(X) exp(−X) exp(X − α(t) X) t
          = exp(−X⁻¹) exp(X − α(t) X) t = exp(−X⁻¹) t exp(H).
```

Now $(w u)^{3} = e \Leftrightarrow w u w^{-1} = u^{-1} w u^{-1}$; comparing the two decompositions of this element on
$U_{-\alpha} \cdot T \cdot U_{\alpha}$, one extracts $t = e$.

**Remark 3.9.** *One can summarize a number of results of this number by the following diagram of principal homogeneous
(left) bundles*

```text
W(g_α)^×  ──w_α──→  N^×  ──a_α──→  W((g_α)^{⊗2})^×
   ↓                  ↓                   ↓
G_{m, S}  ──α*──→  T  ──α──→  G_{m, S}.
```

*Note that $a_{\alpha}$ is faithfully flat ($\alpha$ being so) and that $w_{\alpha}$ is a monomorphism if and only if
$\alpha*$ is a monomorphism. We leave the reader the task of writing the corresponding diagrams for the right principal
bundle structures, as well as the analogous diagrams for the root $-\alpha$, and of studying the relations between these
various diagrams.*

<!-- label: III.XX.3.9 -->

**Lemma 3.10.** *Let $S$ be a scheme, $q$ an integer `> 0` such that $x \mapsto x^{q}$ defines an endomorphism of $G_{a,
S}$, $(G, T, \alpha)$ and $(G', T', \alpha')$ two $S$-elementary systems, $f : G \to G'$ an $S$-group morphism. Let*

<!-- original page 68 -->

```text
h : (g_α)^{⊗q} ──∼──→ g′_{α′}
```

*be an isomorphism of `O_S`-modules and*

```text
h^∨ : (g_{−α})^{⊗q} ──∼──→ g′_{−α′}
```

*the contragredient isomorphism. For every $S' \to S$ and every $X \in W(g_{\alpha})(S')$, suppose:*

$$ f(\exp(X)) = \exp(h(X^{q})). $$

*Then the following conditions are equivalent:*

*(i) $f(\alpha*(z)) = \alpha'*(z)^{q}$.*

*(ii) $f(w_{\alpha}(Z)) = w_{\alpha'}(h(Z^{q}))$.*

*(iii) $f(\exp(Y)) = \exp(h^{\vee}(Y^{q}))$.*

*(Each condition is to be read: for every $S' \to S$ and every $z \in G_{m}(S')$, $Z \in W(g_{\alpha})^{\times}(S')$, $Y
\in W(g_{-\alpha})(S')$, one has …).*

<!-- label: III.XX.3.10 -->

Indeed, (i) ⇒ (ii) by 3.8, (ii) ⇒ (iii) by 3.7, (iii) ⇒ (i) by 2.7.

**Proposition 3.11.** *Let $S$ be a scheme, $q \in \mathbb{Z}$, $q > 0$, such that $x \mapsto x^{q}$ defines an
endomorphism of $G_{a, S}$, $(G, T, \alpha)$ and $(G', T', \alpha')$ two $S$-elementary systems, $f : G \to G'$ an
$S$-group morphism. The following conditions on $f$ are equivalent:*

*(i) The restriction of $f$ to $T$ factors through a morphism $f_{T} : T \to T'$ making the diagram*

```text
G_{m, S}  ──α*──→  T  ──α──→  G_{m, S}
   │                f_T          │
   q                              q
   ↓                ↓             ↓
G_{m, S}  ──α′*──→  T′  ──α′──→  G_{m, S}
```

*commutative.*

<!-- original page 69 -->

*(ii) There exists an (unique) isomorphism of `O_S`-modules*

$$ h : (g_{\alpha})^{\otimes q} \to g'_{\alpha'} $$

*such that $f(\exp(X)) = \exp(h(X^{q}))$, $f(\exp(Y)) = \exp(h^{\vee}(Y^{q}))$ for all $X \in W(g_{\alpha})(S')$, $Y \in
W(g_{-\alpha})(S')$, $S' \to S$ (it follows that $f$ also satisfies the equivalent conditions of 3.10).*

<!-- label: III.XX.3.11 -->

One has (ii) ⇒ (i). Indeed, by 3.10, condition (ii) entails $f \circ \alpha* = q \alpha'*$, hence, by 3.3, $f|T$ factors
through $T'$. It remains to prove $\alpha'(f(t)) = \alpha(t)^{q}$, which follows at once from the fact that $f$ induces
a morphism of groups $T \cdot U_{\alpha} \to T' \cdot U_{\alpha'}$.

Let us prove (i) ⇒ (ii). Let $X \in \Gamma(S, g_{\alpha})$, $Y \in \Gamma(S, g_{-\alpha})$. Set $p^{+}(x) = f(\exp(x
X))$ and $p^{-}(y) = f(\exp(y Y))$; these are group morphisms

```text
p^+, p^− : G_{a, S} → G.
```

Now one has

```text
int(α′*(z))^q (p^+(x)) = int(f_T(α*(z))) (f(exp(x X)))
                       = f(int(α*(z))(exp(x X)))
                       = f(exp(z² x X)) = p^+(z² x).
```

Applying Lemma 1.2 (with $Q = \alpha'*(G_{m, S})$), one deduces that there exists a section $X' \in \Gamma(S,
g'_{\alpha'})$ such that

```text
f(exp(x X)) = p^+(x) = exp(x^q X′).
```

Similarly, there exists a section $Y' \in \Gamma(S, g'_{-\alpha'})$ such that

```text
f(exp(y Y)) = exp(y^q Y′).
```

Writing now that $f$ is a group morphism, hence that it respects formula (F), one obtains at once

```text
X^q Y^q = (X Y)^q = X′ Y′.
```

<!-- original page 70 -->

One concludes easily that $X^{q} \mapsto X'$ and $Y^{q} \mapsto Y'$ define isomorphisms $h$ and $h^{\vee}$ as announced.

**Proposition 3.12.** *Let $(G, T, \alpha)$ be an $S$-elementary system, $w \in N^{\times}(S)$; set*

$$ \Omega_{0} = \Omega \cap int(w^{-1})(\Omega). $$

*Let $d$ be the function on $\Omega$ defined by*

```text
d(exp(Y) · t · exp(X)) = α(t)⁻¹ + X Y.
```

*Then $\Omega_{0} = \Omega_{d}$, and one has for $\exp(Y) \cdot t \cdot \exp(X) \in \Omega_{0}(S')$ the following
formula (set $z = d(\exp(Y) \cdot t \cdot \exp(X))$):*

```text
(⋆)    int(w)(exp(Y) · t · exp(X)) = exp(z⁻¹ a_α(w)⁻¹ X) · t α*(z) · exp(z⁻¹ a_α(w) Y).
```

*Moreover, one has $d \circ int(w) = d^{-1}$.*

<!-- label: III.XX.3.12 -->

Indeed, one has at once[^N.D.E-XX-30]

```text
int(w)(exp(Y) · t · exp(X)) = exp(a_α(w) Y) · t α*(α(t)⁻¹) · exp(a_α(w)⁻¹ X)
                            = exp(a_α(w) Y) · exp(α(t) a_α(w)⁻¹ X) · t α*(α(t)⁻¹).
```

By 2.1, this is a section of $\Omega$ if and only if $1 + \alpha(t) X Y$ is invertible, which proves indeed the equality
$\Omega_{0} = \Omega_{d}$; applying then formula (F) of *loc. cit.*, one deduces by an immediate calculation the
announced formula (⋆). Finally, it follows from (⋆) that one has

```text
(d ∘ int(w))(exp(Y) · t · exp(X)) = α(t α*(z))⁻¹ + z⁻² X Y = z⁻² (α(t)⁻¹ + X Y) = z⁻¹,
```

whence the last assertion.

*N.B.* One notes that the function $d$ is independent of the choice of $w$.

## 4. The isomorphism theorem

<!-- label: III.XX.4 -->

<!-- original page 71 -->

**Theorem 4.1.** *Let $S$ be a scheme, $q \in \mathbb{Z}$, $q > 0$, such that $x \mapsto x^{q}$ is an endomorphism of
$G_{a, S}$, $(G, T, \alpha)$ and $(G', T', \alpha')$ two $S$-elementary systems. Let*

```text
h : (g_α)^{⊗q} → g′_{α′}    and    h^∨ : (g_{−α})^{⊗q} → g′_{−α′}
```

*be two isomorphisms contragredient to each other. Let $f_{T} : T \to T'$ be an $S$-group morphism making the diagram*

```text
G_{m, S}  ──q──→  G_{m, S}
   │                  │
   α*                 α′*
   ↓     f_T          ↓
   T   ──────→        T′
   │                  │
   α                  α′
   ↓                  ↓
G_{m, S}  ──q──→  G_{m, S}
```

*commutative.*

<!-- original page 72 -->

*There exists a unique morphism of $S$-groups $f : G \to G'$ which extends $f_{T}$ and satisfies*

$$ f(\exp(X)) = \exp(h(X^{q})) $$

*for every $X \in W(g_{\alpha})(S')$, $S' \to S$. Moreover, this morphism also satisfies*

```text
f(exp(Y)) = exp(h^∨(Y^q))    and    f(w_α(Z)) = w_α(h(Z^q)),
```

*for every $S' \to S$ and all $Y \in \Gamma(S', g_{-\alpha})$, $Z \in \Gamma(S', g_{\alpha})^{\times}$.*

<!-- label: III.XX.4.1 -->

If $f : G \to G'$ extends $f_{T}$, then $f \circ \alpha* = (\alpha'*)^{q}$. If moreover $f$ satisfies the second
condition, then it satisfies the two others as well by 3.10. It follows that $f$ is determined on $\Omega$ by the
relation

```text
f(exp(Y) t exp(X)) = exp(h^∨(Y^q)) f_T(t) exp(h(X^q)).
```

Since $\Omega$ is schematically dense in $G$, this already proves the uniqueness of $f$. To prove its existence, it
suffices, by virtue of Exp. XVIII 2.3, to prove that the preceding formula defines a "generically multiplicative"
morphism from $\Omega$ to $G'$. Now, by 2.4, this amounts to verifying that $\alpha' \circ f = \alpha^{q}$, which
follows from the fact that $f$ extends $f_{T}$.

**Scholie 4.2.** *One can also interpret 4.1 as follows: consider the category $E$ of $S$-elementary systems and the
category $D$ of tuples*

```text
(G_{m, S}  ──α*──→  T  ──α──→  G_{m, S},  L),
```

*where $T$ is a torus, $\alpha$ and $\alpha*$ are group morphisms such that $\alpha \circ \alpha* = 2$, and $L$ is an
invertible `O_S`-module (the reader will specify the morphisms of the two categories under consideration). One defines a
functor $E \to D$ by*

```text
(G, T, α) ↦ (G_{m, S}  ──α*──→  T  ──α──→  G_{m, S},  g_α).
```

*The preceding theorem says that this functor is fully faithful. It is in fact an equivalence of categories, as one will
see in the next number. One already has:*

<!-- label: III.XX.4.2 -->

**Corollary 4.3.** *If $q = 1$ and if $f_{T}$ is an isomorphism, then $f$ is an isomorphism.*

<!-- label: III.XX.4.3 -->

**Corollary 4.4.** *If $q = 1$ and if $f_{T}$ is faithfully flat with kernel $Q$ (cf. Exp. IX 2.7), then $f$ is
faithfully flat (quasi-compact) with kernel $Q$, hence identifies $G'$ with $G/Q$.*

<!-- label: III.XX.4.4 -->

Indeed, if $f_{T}$ is faithfully flat with kernel $Q$, then

```text
Q = Ker(f_T) ⊂ Ker(f_T ∘ α′) = Ker(α).
```

Introducing the $S$-elementary system $(G/Q, T/Q, \alpha/Q)$ of 2.13, one is reduced by 2.14 to proving that $f/Q$
induces an isomorphism of $G/Q$ onto $G'$, which follows at once from 4.3.

## 5. Examples of elementary systems, applications

<!-- label: III.XX.5 -->

<!-- original page 73 -->

**5.1.** Let $S$ be a scheme, $L$ an invertible `O_S`-module. Consider the group `GL` over $S$ defined by

```text
GL(S′) = { ( a  b )  | a, d ∈ G_a(S′), b ∈ W(L)(S′), c ∈ W(L⁻¹)(S′), a d − b c ∈ G_m(S′) }
         ( c  d )
```

equipped with the usual matrix multiplication law. It is locally isomorphic to $GL_{2, S}$. It is therefore an $S$-group
scheme, affine and smooth over $S$, with connected fibers.

*Remark.* Let $L'$ and $L''$ be two invertible sheaves on $S$, such that $L = L' \otimes L''^{-1}$.[^N.D.E-XX-31] Then
one has an isomorphism of $S$-groups:

```text
GL  ──∼──→  GL(L′ ⊕ L″)
```

defined as follows: if $x$ (resp. $y$) is a section of $L'$ (resp. $L''$) on an open set $V$ of $S$, one has

```text
( a  b ) ( x )   ( a x + b y )
( c  d ) ( y ) = ( c x + d y ).
```

**5.2.** One will denote by `SL` the closed subgroup of `GL` defined by the relation $a d - b c = 1$. It is also an
$S$-group scheme, affine and smooth over $S$, with connected fibers (isomorphic to $SL(L' \oplus L'')$ by the preceding
isomorphism).

Likewise, consider the morphism $G_{m, S} \to GL$ defined by $z \mapsto (z 0 / 0 z)$. It is a central monomorphism; by
passage to the quotient, one deduces a group `PL`, smooth and affine over $S$, with connected fibers (cf. Exp. VIII
5.7).

One can see that, by passage to the quotient from the isomorphism of the preceding remark, `PL` is identified with the
group of automorphisms of the projective bundle $P(L' \oplus L'')$ (cf. EGA, II 4.2.7). One will denote by $i$ and $p$
the canonical morphisms

<!-- original page 74 -->

```text
SL  ──i──→  GL  ──p──→  PL;
```

$i$ is a closed immersion, $p$ is faithfully flat and affine.

**5.3.** Consider the group morphisms

```text
t_G : G²_{m, S} → GL,    t_G(z, z′) = ( z   0 ),
                                       ( 0   z′ )
t_S : G_{m, S} → SL,     t_S(z) = ( z    0 ),
                                  ( 0   z⁻¹ )
t_P : G_{m, S} → PL,     t_P(z) = p(t_G(z, 1)).
```

These are group monomorphisms, which define in each group a (split) torus of relative codimension 2. For every $s \in
S$, let

```text
X ∈ Γ(s, L ⊗ s)^×;
```

then the section $( 0 X / -X^{-1} 0)$ of $GL_{s}$ normalizes $t_{G}(G^{2}_{m, s})$ and does not centralize it; one
concludes from Exp. XIX 1.6 that `GL` is reductive, of semisimple rank 1, with maximal torus $t_{G}(G^{2}_{m, S})$.

One argues similarly for `SL` and `PL`, and one sees that `SL` (resp. `PL`) is reductive, of semisimple rank 1, with
maximal torus $t_{S}(G_{m, S})$ (resp. $t_{P}(G_{m, S})$).

<!-- original page 74 -->

**5.4.** Reasoning as usual, one determines at once the Lie algebra of these various groups and the adjoint action of
the chosen maximal torus. Let us do it for `GL`; this is immediate by Exp. II 4.8: $Lie(GL/S)$ is the Lie algebra of the
matrices below:

```text
Lie(GL/S) = { ( a  b )  | a and d sections of O_S, b section of L, c section of L⁻¹ }
            ( c  d )
```

with the usual bracket; one has

```text
Ad(t_G(z, z′)) ( a  b ) = ( a        z z′⁻¹ b ).
               ( c  d )   ( z′ z⁻¹ c    d   )
```

<!-- original page 75 -->

Denote $Lie(GL/S) = g$. Let $\alpha_{G} : t_{G}(G^{2}_{m, S}) \to G_{m, S}$ be the character defined by

```text
α_G(t_G(z, z′)) = z z′⁻¹.
```

One sees at once from the preceding relation that $\alpha_{G}$ is a root of `GL` with respect to $t_{G}(G^{2}_{m, S})$
and that the morphism

```text
u : L → g    (resp. u⁻ : L⁻¹ → g)
```

defined by $u(X) = ( 0 X / 0 0)$ (resp. $u^{-}(X) = ( 0 0 / X 0)$) is an isomorphism of $L$ onto $g_{\alpha_{G}}$ (resp.
of $L^{-1}$ onto $g_{-\alpha_{G}}$).

One has thus proved that $(G, t_{G}(G^{2}_{m, S}), \alpha_{G})$ is an $S$-elementary system.

Setting likewise

```text
α_S(t_S(z)) = z²,    α_P(t_P(z)) = z,
```

one proves that $(SL, t_{S}(G_{m, S}), \alpha_{S})$ and $(PL, t_{P}(G_{m, S}), \alpha_{P})$ are elementary systems, and
one defines isomorphisms of $L$ (resp. $L^{-1}$) with the corresponding direct summands of the Lie algebras of `SL` and
`PL`.

**5.5.** Set $\exp ( 0 X / 0 0) = ( 1 X / 0 1)$. One has thus defined a morphism

$$ W(g_{\alpha_{G}}) \to GL $$

which induces on the Lie algebras the canonical morphism, hence is the unique morphism of this type (1.5). Similarly,
one sets $\exp ( 0 0 / Y 0) = ( 1 0 / Y 1)$. Carrying out the explicit calculation of formula (F), one finds

```text
⟨ ( 0  X / 0  0 ), ( 0  0 / Y  0 ) ⟩ = X Y,    α*_G(z) = ( z   0  ) = t_G(z, z⁻¹).
                                                          ( 0   z⁻¹)
```

[^N.D.E-XX-32]

<!-- original page 76 -->

The open set $N^{\times} = N^{\times}_{G}$ (defined before 3.1) is:

```text
N^×_G(S′) = { ( 0  P ) | P ∈ W(g_α)^×(S′), Q ∈ W(g_{−α})^×(S′) },
             ( Q  0 )
```

the morphism $w_{\alpha_{G}}$ (cf. 3.1 (iv)) is given, for every $X \in W(g_{\alpha})^{\times}(S')$, by

$$ w_{\alpha_{G}}(X) = ( 0 X); ( -X^{-1} 0) $$

the morphism $a_{\alpha_{G}}$ (cf. 3.5) is given by:

```text
if w = ( 0  P ) ∈ N^×_G(S′), then a_{α_G}(w) = P Q⁻¹ ∈ W((g_α)^{⊗2})^×(S′),
       ( Q  0 )
```

that is, for every $Y \in W(g_{-\alpha})^{\times}(S')$, one has $a_{\alpha_{G}}(w)(Y) = P Q^{-1} Y \in
W(g_{\alpha})^{\times}(S')$.

**5.6.** We leave the reader the task of carrying out the same computations in `SL` and `PL`. One finds the same duality
formula and the coroots

```text
α*_S(z) = t_S(z),    α*_P(z) = t_P(z²).
```

Denote by $p_{T}$ the morphism induced by $p : GL \to PL$ on $t_{S}(G_{m, S})$, i.e.

$$ p_{T}(t_{S}(z)) = t_{P}(z^{2}). $$

One therefore has the commutative diagram:[^N.D.E-XX-33]

```text
                          G_{m, S}
                       id ╱   ╲ 2
                        ╱       ╲
                  α*_S ╱           ╲ α*_P
                     ╱               ╲
            t_S(G_{m, S})  ──p_T──→  t_P(G_{m, S})
              ↑                          ↑
            t_S                          t_P
              │                          │
         G_{m, S}                  G_{m, S}
                       α_S ╲   ╱ α_P
                            ╲ ╱
                         G_{m, S}.
                        ╱   2  ╲
                       id        
```

One recognizes in the central part the commutative diagram of 4.1[^N.D.E-XX-34] relative to the canonical morphism $p
\circ i : SL \to PL$, which induces a morphism of the preceding $S$-elementary systems.

<!-- original page 76 -->

**5.7.** Let now $(G, T, \alpha)$ be any $S$-elementary system. Consider the commutative diagram:

```text
                 G_{m, S}
              id ↙    ↘ 2
            ↙        α*       ↘
          ↙                       ↘
       ↙                              ↘
   G_{m, S}  ──α*──→  T  ──α──→  G_{m, S}
       ↘                              ↗
         ↘                       ↗
            ↘        α       ↗
             2 ↘   ↗ id
                 G_{m, S}
```

<!-- original page 77 -->

Combining the two preceding diagrams, one obtains a commutative diagram:

```text
                       G_{m, S}
                    α*_S ↙  α*  ↘ α*_P
                       ↙           ↘
                    ↙                 ↘
            ↙    α* ∘ t_S⁻¹       t_P ∘ α    ↘
   t_S(G_{m, S})  ────→  T  ────→  t_P(G_{m, S})
            ↘                                ↗
                ↘                       ↗
                    ↘     α       ↗
                    α_S ↘    ↗ α_P
                          G_{m, S}.
```

Using 4.1, one therefore has:

**Proposition 5.8.** *Let $S$ be a scheme, $(G, T, \alpha)$ an $S$-elementary system. Set $L = g_{\alpha}$ (and hence
$L^{-1} = g_{-\alpha}$).*

*(i) There exists a unique group morphism $f : SL \to G$ satisfying the following equivalent conditions:*

```text
(a)   f( z   0  ) = α*(z),    f( 1  X ) = exp(X);
     ( 0   z⁻¹)              ( 0  1 )

(b)   f( 1  X ) = exp(X),     f( 1  0 ) = exp(Y);
     ( 0  1 )                ( Y  1 )

(c)   f( 1  X ) = exp(X),     f(  0     X ) = w_α(X).
     ( 0  1 )                ( −X⁻¹  0 )
```

*(ii) There exists a unique group morphism $g : G \to PL$ satisfying*

```text
g(t) = ( α(t)  0 ),    g(exp(X)) = p( 1  X ).
       ( 0    1 )                    ( 0  1 )
```

*Moreover, one has*

```text
g(exp(Y)) = p( 1  0 ),    g(w_α(X)) = p(  0     X ).
              ( Y  1 )                  ( −X⁻¹  0 )
```

<!-- original page 78 -->

*The morphism $g$ is faithfully flat quasi-compact with kernel $Ker(\alpha) = Centr(G)$, and $g \circ f$ is the
canonical morphism $SL \to PL$.*

<!-- label: III.XX.5.8 -->

Note that conditions (b) of (i) give an explicit description of the duality between $g_{\alpha}$ and $g_{-\alpha}$.

**Corollary 5.9.** *Let $(G, T, \alpha)$ be an $S$-elementary system. The subgroups $T \cdot U_{\alpha}$, $T \cdot
U_{-\alpha}$, $U_{\alpha}$ and $U_{-\alpha}$ are closed.*

<!-- label: III.XX.5.9 -->

Since $U_{\alpha}$ is a closed subgroup scheme of $T \cdot U_{\alpha}$, it suffices to make the verification for the
latter. By Noether's theorem (Exp. IV 5.3.1 and 6.4.1), it suffices to prove that $(T \cdot U_{\alpha})/Ker(\alpha)$ is
a closed subgroup of $G/Ker(\alpha)$. By virtue of 5.8, one is therefore reduced to proving that the subgroup of `PL`
(or of `GL`, which amounts to the same by a new application of Noether's theorem) defined by $c = 0$ is closed, which is
trivial.

Consequently, the morphisms `exp` of Theorem 1.5 (i) are closed immersions.

*N.B.* The corollary also follows from the fact that $T \cdot U_{\alpha}$ and $T \cdot U_{-\alpha}$ are "Borel
subgroups" of $G$ (cf. Exp. XII 7.10).

**5.10.** Let $L$ be an invertible `O_S`-module and

```text
G_{m, S}  ──α*──→  T  ──α──→  G_{m, S}
```

a diagram of groups[^N.D.E-XX-35] such that $\alpha \circ \alpha* = 2$. Let $R$ be the maximal torus of $Ker(\alpha)$
and $K = \alpha*^{-1}(R)$. Then $K$ is a subgroup of multiplicative type of $G_{m, S}$; by virtue of $\alpha \circ
\alpha* = 2$, it is even a subgroup of $\mu_{2, S}$. In particular the morphism

```text
K → SL,    z ↦ ( z   0  )
                ( 0   z⁻¹)
```

is central. One has therefore a central group monomorphism:

<!-- original page 79 -->

```text
K → R × SL,    z ↦ (α*(z), ( z   0  )).
                            ( 0   z⁻¹)
```

Consider the group $G = (R \times SL)/K$ obtained by passage to the quotient. It is an affine and smooth group over $S$,
with connected fibers. It is immediate that the sequence

```text
1 → K → R × t_S(G_{m, S})  ──u──→  T → 1
```

where $u(x, t_{S}(z)) = x \alpha*(z)$ is exact. The image of $R \times t_{S}(G_{m, S})$ in $G$ is therefore a torus $T'$
isomorphic to $T$. One then shows without difficulty that if $\alpha'$ is the character of $T'$ deduced from $\alpha$ by
the preceding isomorphism, $(G, T', \alpha')$ is an $S$-elementary system, that $g'_{\alpha'}$ is isomorphic to $L$, and
that $\alpha'*$ is obtained from $\alpha*$ by the isomorphism $T \xrightarrow{\sim} T'$. One has therefore constructed
an $S$-elementary system $(G, T', \alpha')$ such that the corresponding object

<!-- original page 80 -->

```text
(G_{m, S}  ──α′*──→  T′  ──α′──→  G_{m, S},  g′_{α′})
```

of the category $D$ defined in 4.2 is isomorphic to

```text
(G_{m, S}  ──α*──→  T  ──α──→  G_{m, S},  L).
```

One has therefore proved the

**Theorem 5.11.** *In the notations of 4.2, the functor*

```text
(G, T, α) ↦ (G_{m, S}  ──α*──→  T  ──α──→  G_{m, S},  g_α)
```

*is an equivalence of categories between $E$ and $D$.*

<!-- label: III.XX.5.11 -->

## 6. Generators and relations for an elementary system

<!-- label: III.XX.6 -->

<!-- original page 80 -->

**6.1.** Let $S$ be a scheme, $(G, T, \alpha)$ an $S$-elementary system. Let $X \in W(g_{\alpha})^{\times}(S)$ and $u =
\exp(X)$; one has seen in 3.8 that the element $w = w_{\alpha}(X)$ satisfies in particular the relation

$$ (w u)^{3} = e. $$

[^N.D.E-XX-36]

One denotes by $s_{\alpha}$ the automorphism of $T$ induced by $int(w)$; according to Theorem 3.1 (iii), for every $S'
\to S$ and $t \in T(S')$, one has

```text
s_α(t) = int(w)(t) = t · α*(α(t)⁻¹).
```

**Theorem 6.2.** *Let $H$ be an $S$-sheaf of groups for (fppf). Let*

```text
f_T : T → H,    f_α : U_α → H
```

*be group morphisms and $h \in H(S)$ a section of $H$. For there to exist a (necessarily unique) group morphism*

$$ f : G \to H $$

*extending $f_{T}$ and $f_{\alpha}$ and satisfying $f(w) = h$, it is necessary and sufficient that the following
conditions be satisfied:*

*(i) For every $S' \to S$, every $t \in T(S')$ and every $x \in U_{\alpha}(S')$, one has*

```text
(1)   f_T(t) f_α(x) f_T(t)⁻¹ = f_α(t x t⁻¹) = f_α(x^{α(t)}).
```

*(in other words, $f_{T}$ and $f_{\alpha}$ extend to a group morphism from the semidirect product $T \cdot U_{\alpha}$
into $H$).*

*(ii) For every $S' \to S$ and every $t \in T(S')$, one has*

```text
(2)   h f_T(t) h⁻¹ = f_T(s_α(t)) = f_T(t · α*(α(t)⁻¹)).
```

<!-- original page 81 -->

*(iii) One has the two relations in $H(S)$:*

$$ (3) h^{2} = f_{T}(\alpha*(-1)), (4) (h f_{\alpha}(u))^{3} = e. $$

<!-- label: III.XX.6.2 -->

*Proof.* Denote additively $U_{\alpha}$ and $U_{-\alpha}$ and multiplicatively their vector structure. If $f$ satisfies
the conditions of the statement, one necessarily has for every $y \in U_{-\alpha}(S')$,

```text
f(y) = f(w⁻¹ w y w⁻¹ w) = h f_α(w⁻¹ y w) h⁻¹.
```

Let then $f_{-\alpha} : U_{-\alpha} \to H$ be the morphism defined by

```text
(∗_1)    f_{−α}(y) = h f_α(w⁻¹ y w) h⁻¹.
```

It is a group morphism. On the other hand, $f$ is determined on the big cell $\Omega$ by

```text
f(y t x) = f_{−α}(y) f_T(t) f_α(x).
```

This shows the uniqueness of $f$; since the conditions of the statement are manifestly necessary, let us show that they
are sufficient.

One has by (4)

```text
h f_α(u) h⁻¹ h² = f_α(−u) h⁻¹ f_α(−u).
```

Now, by (3) and (1), $h^{2} = f_{T}(\alpha*(-1))$ commutes with $f_{\alpha}(-u)$, which gives

```text
h f_α(u) h⁻¹ = f_α(−u) h f_α(−u).
```

But, by definition, $h f_{\alpha}(u) h^{-1} = f_{-\alpha}(w u w^{-1})$; by 3.7, since $u = \exp(X)$ and $w =
w_{\alpha}(X)$, one has

<!-- original page 82 -->

```text
(∗_2)    w u w⁻¹ = −ũ,
```

where `ũ` denotes the element paired with $u$. One obtains therefore:

```text
(∗_3)    f_{−α}(−ũ) = f_α(−u) h f_α(−u).
```

Let now $t$ be a section of $T$ over a variable $S' \to S$. Apply $int(f_{T}(t))$ to the preceding formula. One obtains
on the left-hand side[^N.D.E-XX-37]

```text
f_T(t) f_{−α}(−ũ) f_T(t)⁻¹ = f_T(t) h f_α(u) h⁻¹ f_T(t)⁻¹
                           = h (h⁻¹ f_T(t) h) f_α(u) (h⁻¹ f_T(t)⁻¹ h) h⁻¹
                           = h f_T(s_α(t)) f_α(u) f_T(s_α(t))⁻¹ h⁻¹ = h f_α(α(s_α(t)) u) h⁻¹
```

by (2) and (1); then since $s_{\alpha}(t) = t \cdot \alpha*(\alpha(t)^{-1})$ and $\alpha \circ \alpha* = 2$, this equals

```text
h f_α(α(t)⁻¹ u) h⁻¹.
```

Finally, by (∗\_1) and (∗\_2) one has

```text
h f_α(α(t)⁻¹ u) h⁻¹ = f_{−α}(α(t)⁻¹ w u w⁻¹) = f_{−α}(−α(t)⁻¹ ũ).
```

The right-hand side of (∗\_3) gives

```text
f_α(−α(t) u) · f_T(t) h f_T(t)⁻¹ h⁻¹ · h · f_α(−α(t) u)
```

and since $h f_{T}(t)^{-1} h^{-1} = f_{T}(s_{\alpha}(t^{-1})) = f_{T}(t \cdot \alpha*(\alpha(t)))$, this equals

```text
f_α(−α(t) u) · f_T(α*(α(t))) · h · f_α(−α(t) u).
```

Comparing the two expressions obtained, one obtains

```text
f_{−α}(−α(t)⁻¹ ũ) = f_α(−α(t) u) · f_T(α*(α(t))) · h · f_α(−α(t) u).
```

Since $\alpha : T \to G_{m, S}$ is faithfully flat and $H$ is a separated presheaf, one can replace $-\alpha(t)^{-1}$ by
an arbitrary section of $G_{m, S}$, and one obtains the

**Lemma 6.2.1.** *For every $z \in G_{m}(S')$, $S' \to S$, one has*

```text
f_{−α}(z ũ) = f_α(z⁻¹ u) · f_T(α*(−z⁻¹)) · h · f_α(z⁻¹ u).
```

<!-- label: III.XX.6.2.1 -->

<!-- original page 83 -->

Let now $x, y \in G_{a}(S')$, $S' \to S$; suppose $y$ and $(1 + x y)$ invertible. Applying the lemma first to $z = y$,
one obtains[^N.D.E-XX-38]

```text
f_α(x u) f_{−α}(y ũ) = f_α((x + y⁻¹) u) · f_T(α*(−y⁻¹)) · h · f_α(y⁻¹ u).
```

Now $x + y^{-1} = y^{-1}(1 + x y)$. Applying the lemma to $z = y / (1 + x y)$, one finds

```text
f_α((x + y⁻¹) u) = f_{−α}( y/(1 + x y) · ũ ) f_α(−(x + y⁻¹) u) · h · f_T(α*(−y / (1 + x y))).
```

Substituting in the preceding equality, one obtains

```text
f_α(x u) f_{−α}(y ũ) = f_{−α}( y / (1 + x y) · ũ ) f_α(−(x + y⁻¹) u) · h⁻¹ · f_T(α*(1 + x y)⁻¹) · h · f_α(y⁻¹ u).
```

Since $h^{-1} f_{T}(t) h = f_{T}(s_{\alpha}(t))$ by (2) (note that $s^{2}_{\alpha} = id$) and since $s_{\alpha} \circ
\alpha* = -\alpha*$ (cf. 6.2.1), this equals

```text
f_{−α}( y / (1 + x y) · ũ ) f_α(−(x + y⁻¹) u) · f_T(α*(1 + x y)) · f_α(y⁻¹ u).
```

Finally, since for all $x' \in U_{\alpha}(S')$ and $z \in G_{m}(S')$ one has

```text
f_α(x′) f_T(α*(z)) = f_T(α*(z)) f_α(z⁻² x′),
```

one obtains

```text
f_α(x u) f_{−α}(y ũ) = f_{−α}( y / (1 + x y) · ũ ) · f_T(α*(1 + x y)) · f_α( −y⁻¹ (1 + x y)⁻¹ / (1 + x y)² + y⁻¹ · u )
                     = f_{−α}( y / (1 + x y) · ũ ) · f_T(α*(1 + x y)) · f_α( x / (1 + x y) · u ).
```

One has thus proved:

**Lemma 6.2.2.** *Let $S' \to S$. If $a \in U_{\alpha}(S')$, $b \in U^{\times}_{-\alpha}(S')$, and $1 + a b \in
G_{m}(S')$, one has*

```text
f_α(a) f_{−α}(b) = f_{−α}( b / (1 + a b) ) f_T(α*(1 + a b)) f_α( a / (1 + a b) ).
```

<!-- label: III.XX.6.2.2 -->

<!-- original page 84 -->

By schematic density, this formula remains valid when $b \in U_{-\alpha}(S')$, $1 + a b$ being always invertible.
Consider then the morphism

$$ f : \Omega \to H $$

defined by $f(y t x) = f_{-\alpha}(y) f_{T}(t) f_{\alpha}(x)$.

It follows at once from 6.2.2, from condition 6.2 (i), and from formula (F′) of 2.4 that if $g, g' \in \Omega(S')$ and
$g g' \in \Omega(S')$, one has $f(g g') = f(g) f(g')$. By Exp. XVIII 2.3 (iii) and 2.4[^N.D.E-XX-39], there therefore
exists a group morphism $G \to H$ extending $f$. Denote it also by $f$; it answers the question; it suffices to prove,
indeed, that $f(w_{\alpha}) = h$. Now $w_{\alpha} = u \cdot (-\tilde{u}) \cdot u$, whence, by (∗\_3):[^N.D.E-XX-40]

```text
f(w_α) = f_α(u) f_{−α}(−ũ) f_α(u) = h.
```

**Remark 6.3.** *We shall complete these results in Exp. XXIII 3.5.*

<!-- label: III.XX.6.3 -->

<!-- LEDGER DELTA — Exposé XX — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| système élémentaire | elementary system | Triple `(G, T, α)`: reductive group of semisimple rank 1, maximal torus, root. Per Exp. XX Def. 1.3. |
| `S`-système élémentaire | `S`-elementary system | Relative form. |
| grosse cellule | big cell | The open subset `Ω = U_{−α} · T · U_α` of `G`. |
| multiplicateur | multiplier | For a morphism `p : G_{a, S} → G` "normalized by `T` with multiplier `α`": `t p(x) t⁻¹ = p(α(t) x)`. |
| morphisme normalisé par T avec le multiplicateur α | morphism normalized by `T` with multiplier `α` | Standard relative-Borel-style locution. |
| coracine | coroot | Already in glossary. Denoted `α*`. |
| coracine infinitésimale | infinitesimal coroot | `H_α = α*(1) ∈ t`. |
| racine infinitésimale | infinitesimal root | The linear form `α : t → O_S` derived from the character `α`. |
| appariés | paired | Of `X ∈ Γ(S, g_α)^×` and `X⁻¹ ∈ Γ(S, g_{−α})^×` with `X X⁻¹ = 1` under the duality pairing. Def. 2.6.1. |
| immersion ouverte | open immersion | Standard. |
| dominant | dominant | Standard. |
| radiciel | radicial | Standard (per glossary); means universally injective. |
| séparable | separable | Standard (here in the sense of *EGA* IV: smooth at a point + birational). |
| birationnel | birational | Standard. |
| fibré principal homogène | principal homogeneous bundle | Standard; in this Exposé locally trivial under `T`. |
| fibré principal homogène à gauche (resp. à droite) | left (resp. right) principal homogeneous bundle | Preserve the side. |
| fibré vectoriel | vector bundle | Standard; here `W(g_α)`. |
| groupe à groupe d'opérateurs T | group with group of operators `T` | Preserve; refers to `T`-action by inner automorphisms. |
| schématiquement dense | schematically dense | Per EGA IV. |
| relativement schématiquement dense | relatively schematically dense | Per Exp. XVIII §1. |
| densité schématique | schematic density | Standard. |
| « génériquement multiplicatif » | "generically multiplicative" | Preserve guillemets as scare quotes; per Exp. XVIII 2.3. |
| transport de structure | transport of structure | Standard. |
| Bible (12-05, démonstration du cor. à la prop. 1) | *Bible*, 12-05, proof of the corollary to prop. 1 | Per Chevalley Seminar convention. |
| ouvert | open set | Standard. |
| section unité (resp. nulle) | unit (resp. zero) section | Standard. |
| théorème d'isomorphisme | isomorphism theorem | Per Exp. XX §4 title. |
| Scholie | Scholie | Preserved (English borrows the Latin "Scholium"; the French title is kept here, matching Exp. XII's "Scholie" usage). |
| 2-torsion `₂T` | `₂T` | The 2-torsion subgroup scheme of `T`. Preserve subscript-left notation. |
| « équation fonctionnelle » | "functional equation" | Preserve guillemets. |
| Noether (théorème de) | Noether's theorem | Standard (here Exp. IV 5.3.1 and 6.4.1). |
| `int(t)` | `int(t)` | Inner automorphism. Standard. |
| `Ad` | `Ad` | Adjoint representation. |
| `Centr(G)`, `Centr_G(…)` | `Centr(G)`, `Centr_G(…)` | Center / centralizer. |
| `Norm_G(T)` | `Norm_G(T)` | Normalizer. |
| `Ker` | `Ker` | Standard. |
| `Hom_{S-gr.}` | `Hom_{S-gr.}` | Group-scheme homomorphisms over `S`. |
| sous-groupe de Borel | Borel subgroup | Per glossary; here in scare quotes per N.B. after Cor. 5.9. |
-->

[^N.D.E-XX-1]: N.D.E.: of `O_S`-modules.

[^N.D.E-XX-2]: N.D.E.: We shall see later (Cor. 5.9) that `exp` is an isomorphism of $W(g_{\alpha})$ onto a closed
    subgroup of $G$.

[^N.D.E-XX-3]: N.D.E.: see also VI_B, 2.5.

[^N.D.E-XX-4]: N.D.E.: by EGA IV₄, 17.9.1.

[^N.D.E-XX-5]: N.D.E.: We have added the sentence that follows.

[^N.D.E-XX-6]: N.D.E.: We have replaced $P_{-\alpha}$ and $P_{\alpha}$ by $U_{-\alpha}$ and $U_{\alpha}$.

[^N.D.E-XX-7]: N.D.E.: see also EGA IV₃, 11.10.10.

[^N.D.E-XX-8]: N.D.E.: Indeed, on the one hand, $Lie(G_{a, S}) = O_{S}$ and $Lie(p_{\alpha})$ is an element of
    $\operatorname{Hom}_{O_{S}}(O_{S}, g_{\alpha}) = \Gamma(S, g_{\alpha})$.

[^N.D.E-XX-9]: N.D.E.: by 1.18.

[^N.D.E-XX-10]: N.D.E.: We have added the condition "$(1, u v) \in U(S')$".

[^N.D.E-XX-11]: N.D.E.: here and in what follows, we have replaced $U(S')$ by $V(S')$.

[^N.D.E-XX-12]: N.D.E.: We have denoted by $E$ the element denoted $G$ in the original, since $G$ already denotes the
    $S$-group under consideration.

[^N.D.E-XX-13]: N.D.E.: We have corrected what follows.

[^N.D.E-XX-14]: N.D.E.: that is, we have made the "change of variables" $x = v$, $y = w E(v)^{-1}$, i.e. $v = x$, $w = y
    E(x)$.

[^N.D.E-XX-15]: N.D.E.: We have corrected `y E(x)` to $x + y E(x)$.

[^N.D.E-XX-16]: N.D.E.: that is, one writes the equalities resulting from $p_{\alpha}(t) p_{\alpha}(u) p_{-\alpha}(v) =
    p_{\alpha}(t + u) p_{-\alpha}(v)$ and sets $v = 1$ and $x = u$, $t = y F(u)$ (i.e. $y = t F(u)^{-1}$).

[^N.D.E-XX-17]: N.D.E.: We have corrected `y F(x)` to $x + y F(x)$.

[^N.D.E-XX-18]: N.D.E.: We have corrected what follows.

[^N.D.E-XX-19]: N.D.E.: We have added the sentence that follows. One can also see by a direct calculation that the
    preceding equality entails $0 = x y b (2 + (x + y) b)$, hence $0 = b(2 + (x + y) b)$, and finally $b = 0$.

[^N.D.E-XX-20]: N.D.E.: In the three preceding equalities, we have corrected the original by replacing the factor $(1 +
    b x)$ on the right by $1 + a x$. Substituting the third equality into the second and taking into account that $1 + a
    x$ is invertible, one obtains the equality $a^{2} x y = a b x y$.

[^N.D.E-XX-21]: N.D.E.: that is, we have made the change of variables $x' = 1 + a x$, i.e. $x = (x' - 1)/a$.

[^N.D.E-XX-22]: N.D.E.: We have slightly modified what follows, since an open set $V$ was already introduced in A).

[^N.D.E-XX-23]: N.D.E.: We have added the numbering 3.0, for later references.

[^N.D.E-XX-24]: N.D.E.: We have replaced $Q$ by the more suggestive notation $N^{\times}$.

[^N.D.E-XX-25]: N.D.E.: We have corrected the first formula of the original.

[^N.D.E-XX-26]: N.D.E.: The first equality follows from 1.5 (i) which, combined with the equality $\alpha \circ \alpha*
    = 2$, gives the formulas

    ```text
    (†)   α*(z) exp(X) α*(z)⁻¹ = exp(z² X),    α*(z) exp(X⁻¹) α*(z)⁻¹ = exp(z⁻² X),
    ```

    the third equality follows from formula (F), and the fourth from (†), again. Finally, an analogous calculation shows
    that $w_{\alpha}(X) \alpha*(z^{-1}) = w_{\alpha}(z X)$.

[^N.D.E-XX-27]: N.D.E.: The hypothesis $Centr_{G_{s}}(n \alpha*_{s}) \neq G_{s}$ entails that
    `dim Centr_{G_s}(n α*_s) − dim T_s < 2`, but this difference is even, by *loc. cit.*

[^N.D.E-XX-28]: N.D.E.: that is, $a_{-\alpha}(w)$ and $a_{\alpha}(w)$ are paired, cf. 2.6.1.

[^N.D.E-XX-29]: N.D.E.: We have detailed what follows.

[^N.D.E-XX-30]: N.D.E.: We have corrected the original by swapping $a_{\alpha}(w)$ and $a_{\alpha}(w)^{-1}$, and we have
    detailed the proof of the equality $d \circ int(w) = d^{-1}$.

[^N.D.E-XX-31]: N.D.E.: We have corrected $L'' \otimes L'^{-1}$ to $L' \otimes L''^{-1}$ and we have detailed the
    sentence that follows.

[^N.D.E-XX-32]: N.D.E.: We have detailed what follows.

[^N.D.E-XX-33]: N.D.E.: where $t_{S}$ and $t_{P}$ are isomorphisms.

[^N.D.E-XX-34]: N.D.E.: with $q = 1$.

[^N.D.E-XX-35]: N.D.E.: $T$ being a torus.

[^N.D.E-XX-36]: N.D.E.: We have added the sentence that follows.

[^N.D.E-XX-37]: N.D.E.: We have corrected what follows.

[^N.D.E-XX-38]: N.D.E.: We have detailed the calculations that follow.

[^N.D.E-XX-39]: N.D.E.: Note that each geometric fiber of $G$ is connected, for example by 1.1.

[^N.D.E-XX-40]: N.D.E.: We have simplified the original by invoking (∗\_3).
