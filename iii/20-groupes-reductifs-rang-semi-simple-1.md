# Exposé XX. Reductive groups of semisimple rank 1

<!-- label: III.XX -->

*by M. Demazure*

<!-- N.D.E.: Version of 13/10/2024 -->

## 1. Elementary systems. The groups `U_α` and `U_{−α}`

<!-- label: III.XX.1 -->

<!-- original page 35 -->

**Recollection 1.1.** *Let `S = Spec(k)`, where `k` is an algebraically closed field, and
let `G` be a reductive `S`-group of semisimple rank 1, `T` a maximal torus (necessarily
split) of `G`. One then has*

```text
g = t ⊕ g_α ⊕ g_{−α},
```

*where `α` and `−α` are the roots of `G` with respect to `T`. Moreover, there exist two
group monomorphisms*

```text
p_α : G_{a, S} → G    and    p_{−α} : G_{a, S} → G
```

*such that*

```text
t p_α(x) t⁻¹ = p_α(α(t) x)    and    t p_{−α}(x) t⁻¹ = p_{−α}(α(t)⁻¹ x),
```

*for every `S′ → S` and all `t ∈ T(S′)`, `x ∈ G_a(S′)`, and such that the morphism*

```text
G_{a, S} ×_S T ×_S G_{a, S} → G,
```

*defined by `(y, t, x) ↦ p_{−α}(y) t p_α(x)`, is radicial and dominant (*Bible*, § 13.4, cor. 2 to th. 3).*

<!-- label: III.XX.1.1 -->

Since the tangent map at the identity is bijective, this morphism is also separable, hence
birational; by Zariski's "Main Theorem" (EGA III₁, 4.4.9), it is therefore an open
immersion.

**Lemma 1.2.** *Let `S` be a scheme, `G` an `S`-group scheme, `T` a torus of `G`, `Q` a
subtorus of `T`, `α` a character of `T` inducing on `Q` a non-trivial character on each
fiber. Let `p_α : G_{a, S} → G` (resp. `p_{−α} : G_{a, S} → G`) be a group morphism
normalized by `T` with multiplier `α` (resp. `−α`). Suppose that the morphism*

<!-- original page 36 -->

```text
u : G_{a, S} ×_S T ×_S G_{a, S} → G,
```

*defined set-theoretically by `u(y, t, x) = p_{−α}(y) t p_α(x)`, is an open immersion.
Let finally `q` be an integer `⩾ 0` and*

```text
p : G_{a, S} → G
```

*a group morphism such that for every `S′ → S` and all `t ∈ Q(S′)`, `x ∈ G_a(S′)` one has*

```text
int(t)(p(x)) = p(α(t)^q x).
```

*Then there exists a unique `ν ∈ G_a(S)` such that `p(x) = p_α(ν x^q)`.*

<!-- label: III.XX.1.2 -->

Indeed, let `Ω` be the image of `u` and `U = p⁻¹(Ω)`. This is an open subset of `G_{a, S}`
containing the zero section. For every section `t` of `Q`, the automorphism of `G_{a, S}`
defined by multiplication by `α(t)` leaves `U` globally fixed. We have `U = G_{a, S}`;
indeed, it suffices to check this when `S` is the spectrum of an algebraically closed field
`k`; then `α : Q(k) → k*` is surjective, which proves at once that `U(k) ⊃ k*`, hence
`U = G_{a, k}`. There therefore exist three morphisms

```text
a : G_{a, S} → G_{a, S},   b : G_{a, S} → T,   c : G_{a, S} → G_{a, S},
```

such that

```text
p(x) = p_{−α}(a(x)) b(x) p_α(c(x)).
```

The condition on `p` translates to

```text
a(α(t) x) = α(t)^{−q} a(x),
b(α(t) x) = b(x),
c(α(t) x) = α(t)^q c(x).
```

<!-- original page 37 -->

For the same reason as before, one therefore has for every `S′ → S` and every
`z ∈ G_m(S′)`,

```text
a(z x) = z^{−q} a(x),   b(z x) = b(x),   c(z x) = z^q c(x),
```

hence

```text
z^q a(z) = a(1),   b(z) = b(1),   c(z) = z^q c(1).
```

Since `G_{m, S}` is schematically dense in `G_{a, S}`, one has at once for every
`x ∈ G_a(S′)`, `S′ → S`:

```text
x^q a(x) = a(1) = a(0) = 0,    hence a = 0,
c(x) = x^q c(1) = ν x^q,       for some ν ∈ G_a(S),
b(x) = b(1) = b(0) = e,        hence b = e,
```

which completes the proof.

**Definition 1.3.** *Let `S` be a scheme. By an `S`-*elementary system* one means a triple
`(G, T, α)` where*

*(i) `G` is a reductive `S`-group of semisimple rank 1 (Exp. XIX 2.7),*

*(ii) `T` is a maximal torus of `G`,*

*(iii) `α` is a root of `G` with respect to `T` (Exp. XIX 3.2).*

<!-- label: III.XX.1.3 -->

One thus has a direct sum decomposition (Exp. XIX 3.5)[^N.D.E-XX-1]

```text
g = t ⊕ g_α ⊕ g_{−α},
```

`g_α` and `g_{−α}` being locally free of rank one.

**1.4.** If `(G, T, α)` is an `S`-elementary system, then `(G_{S′}, T_{S′}, α_{S′})` is an
`S′`-elementary system for every `S′ → S`. If `(G, T, α)` is an `S`-elementary system, then
`(G, T, −α)` is also one.

<!-- original page 38 -->

If `S` is a scheme, `G` a reductive `S`-group, `T` a maximal torus of `G`, `α` a root of
`G` with respect to `T`, then (Exp. XIX 3.9), `(Z_α, T, α)` is an `S`-elementary system.

Let `(G, T, α)` be an `S`-elementary system. The invertible module `g_α` is canonically
endowed with a `T`-module structure. One therefore has also a `T`-module structure on the
vector bundle `W(g_α)`. On the other hand, the inner automorphisms of `T` define on `G` a
structure of group with group of operators `T`.

**Theorem 1.5.** *Let `(G, T, α)` be an `S`-elementary system.*

*(i) There exists a unique morphism of groups with group of operators `T`*

```text
exp : W(g_α) → G
```

*which induces on the Lie algebras the canonical morphism `g_α → g`.*[^N.D.E-XX-2]

*In other words, `exp` is the unique morphism satisfying the following conditions: for every
`S′ → S` and every `t ∈ T(S′)`, `X, X′ ∈ W(g_α)(S′)`, one has*

```text
exp(X + X′) = exp(X) exp(X′),
int(t)(exp(X)) = exp(α(t) X),
Lie(exp)(X) = X.
```

*(ii) If one defines analogously (in the `S`-elementary system `(G, T, −α)`)*

```text
exp : W(g_{−α}) → G,
```

*then the morphism*

```text
W(g_{−α}) ×_S T ×_S W(g_α) → G
```

*defined set-theoretically by `(Y, t, X) ↦ exp(Y) · t · exp(X)` is an open immersion.*

<!-- label: III.XX.1.5 -->

Suppose we have proved the existence of the desired `exp` morphisms, and let us prove the
other assertions of the theorem. We first prove (ii). Since both sides are of finite
presentation and flat over `S`, it suffices to do so when `S` is the spectrum of an
algebraically closed field (SGA 1, I 5.7 and VIII 5.5). Let then `S = Spec k`. Let
`X ∈ Γ(S, g_α)^×`, `Y ∈ Γ(S, g_{−α})^×`. It suffices to prove that the morphism

<!-- original page 39 -->

```text
G_{a, k} ×_k T ×_k G_{a, k} → G,   (y, t, x) ↦ exp(yY) t exp(xX)
```

is an open immersion. Now by 1.1 and 1.2, there exist `a, b ∈ k` such that

```text
exp(yY) = p_{−α}(a y)    and    exp(xX) = p_α(b x).
```

Since `exp : W(g_{−α}) → G` induces a monomorphism on Lie algebras, one has `a ≠ 0`;
likewise `b ≠ 0`, and one is reduced to 1.1.

The uniqueness of the morphism `exp` may be proved locally on `S`; one then reduces to the
case where `g_α` and `g_{−α}` are free, and one has only to apply 1.2 (with `Q = T` and
`q = 1`).

It remains then to prove the existence of the desired morphism `exp`. Let us first remark
that, by virtue of the theory of faithfully flat descent and the uniqueness assertion just
proved, it suffices to demonstrate this existence locally on `S` for the (fpqc) topology.
By the usual arguments using finite presentation, one reduces to the case where `S` is
noetherian, then to the case where it is noetherian local. By virtue of the preceding
remark, one can therefore content oneself with proving the existence of the desired
morphism `exp` when `S = Spec(A)`, with `A` a complete noetherian local ring with
algebraically closed residue field `k`. Let then `p_0 : G_{a, k} → G_k` be a monomorphism
of `k`-groups normalized by `T_k` with multiplier `α_0 = α ⊗_A k` (one exists by 1.1). One
knows (1.1 and 1.2) that the corresponding morphism `T_k ·_{α_0} G_{a, k} → G_k` is an
immersion, hence in particular a monomorphism. Let us provisionally admit the following
two lemmas:

<!-- original page 40 -->

**Lemma 1.6.** *Let `S` be a scheme, `G` an `S`-group of finite presentation, `T` an
`S`-torus, `α` a character non-trivial on each fiber of `T`, `s_0` a point of `S`. Let*

```text
f : T ·_α G_{a, S} → G
```

*be an `S`-group morphism such that `f_{s_0}` is a monomorphism and the restriction of `f`
to `T` is a monomorphism. There exists an open neighborhood `U` of `s_0` such that `f|U`
is a monomorphism.*

<!-- label: III.XX.1.6 -->

**Lemma 1.7.** *Let `A` be a complete noetherian local ring with algebraically closed
residue field `k`, `(G, T, α)` an `A`-elementary system, `p_0 : G_{a, k} → G_k` a morphism
of `k`-groups normalized by `T_k` with multiplier `α ⊗_A k`. There exists a group morphism
`p : G_{a, A} → G` normalized by `T` with multiplier `α`.*

<!-- label: III.XX.1.7 -->

Let `p` be the morphism whose existence is asserted by 1.7. Let `f : T ·_α G_{a, S} → G`
be the corresponding morphism. It satisfies the hypotheses of 1.6, hence is a monomorphism;
in particular `p` is a monomorphism. One then concludes by Exp. XIX 4.9.

*Proof of 1.6.* Denote by `ε : S → T ·_α G_{a, S}` the unit section. Since `f` is
unramified at `ε(s_0)`, it is so at `ε(s)` for all `s` in an open neighborhood `U` of
`s_0`; `f|U` is therefore unramified (Exp. X 3.5)[^N.D.E-XX-3], hence its kernel
`Ker(f)_U` is unramified over `U`. To prove that `f|U` is a monomorphism, it suffices
therefore[^N.D.E-XX-4] to prove that `Ker(f)_U` is radicial over `U`, which is a
set-theoretic question. One is thus reduced to proving:

<!-- original page 41 -->

**Lemma 1.8.** *Let `k` be an algebraically closed field; let `N` be an invariant subgroup
of `T ·_α G_{a, k}` (`α` a non-trivial character of the torus `T`), étale over `k` and
such that `N ∩ T = {e}`. Then `N = {e}`.*

<!-- label: III.XX.1.8 -->

One has `int(t′)(t, x) = (t, α(t′) x)`. If `(t, x)` is a point of `N`, with `x ≠ 0`, then
`(t, z x)` is also a point of `N` for `z ∈ k*`, and `(t, x)` is not isolated; hence `N` is
not quasi-finite. One therefore has set-theoretically `N ⊂ T`, and we are done.

*Proof of 1.7.* Let `m` be the radical of `A`, and `S_n = Spec(A/m^{n+1})`, `n ⩾ 0`. We
first show, by induction on `n`, that `p_0` can be extended for each `n` to a morphism of
`S_n`-groups

```text
p_n : G_{a, S_n} → G_{S_n}
```

normalized by `T_{S_n}` with multiplier `α_{S_n}`, the `p_n` further satisfying the
condition `p_{n+1} ×_{S_{n+1}} S_n = p_n`.

Let `H = T ·_α G_{a, S}`. The morphism `H_{S_n} → G_{S_n}` defined by `p_n` is denoted
`f_n`. Let us admit the following lemma:

**Lemma 1.9.** *If `(G, T, α)` is a `k`-elementary system, `k` algebraically closed, and if
`p : G_{a, k} → G` is a monomorphism normalized by `T` with multiplier `α`, one has*

```text
H²(T ·_α G_{a, k}, g) = 0.
```

*(One lets `T ·_α G_{a, k}` act on `g` through the morphism `T ·_α G_{a, k} → G` defined by
`p`, and the adjoint representation of `G`).*

<!-- label: III.XX.1.9 -->

Then, by virtue of Exp. III 2.8, `f_n` extends to a morphism of `S_{n+1}`-groups

```text
f′_{n+1} : H_{S_{n+1}} → G_{S_{n+1}}.
```

<!-- original page 42 -->

Now `f′_{n+1}` and the canonical immersion of `T_{S_{n+1}}` into `G_{S_{n+1}}` have the
same restriction to `T_{S_n}`. By Exp. III 2.5, there exists an element `g ∈ G(S_{n+1})`
such that `g ×_{S_{n+1}} S_n = e` and such that
`f_{n+1} = int(g) ∘ f′_{n+1}` restricts to `T_{n+1}` along the canonical immersion of
`T_{n+1}`. Let `p_{n+1}` be the restriction of `f_{n+1}` to `G_{a, S_{n+1}}`. It is a
morphism normalized by `T_{S_{n+1}}` with multiplier `α_{S_{n+1}}`, which extends `p_n`.

One has thus constructed a coherent system `(f_n)` and one must now algebraize it. Now one
has:

**Lemma 1.10.** *Let `A` be a complete noetherian local ring, `m` its maximal ideal,
`S = Spec(A)`, `S_n = Spec(A/m^{n+1})`, `T` an `S`-torus, `α` a non-zero character of `T`,
`X` an affine `S`-scheme on which `T` acts. Let `T` act on `G_{a, S}` via `α`. Let `q` be an
integer `⩾ 0`, and let `(f_n)_{n ⩾ 0}` be a coherent system of morphisms*

```text
f_n : G_{a, S_n}^q → X_{S_n}
```

*of objects with operators `T_{S_n}`. There exists a unique morphism of objects with
operators `T`*

```text
f : G_{a, S}^q → X
```

*which induces the `f_n` (compare with Exp. IX 7.1).*

<!-- label: III.XX.1.10 -->

**Corollary 1.11.** *If `X` is a group with group of operators `T` and if the `f_n` are
group morphisms, then `f` is one too.*

<!-- label: III.XX.1.11 -->

It suffices to apply the uniqueness assertion of the lemma to the two morphisms
`G_{a, S}^{2q} → X` deduced from `f` in the usual way.

<!-- original page 43 -->

*Proof of 1.10.* Suppose `T` split, which is moreover the case in the application of 1.10
to the proof of 1.5. One knows (Exp. I 4.7.3.1) that `X ↦ A(X)` realizes an equivalence
between the category of affine `S`-schemes equipped with a `T`-operation and the opposite
category of `S`-graded algebras of type `M = Hom_{S-gr.}(T, G_{m, S})`.

One therefore has gradings

```text
B = A(X) = ⨁_{m ∈ M} B_m    and    C = A(G_{a, S}^q) = ⨁_{m ∈ M} C_m.
```

One sees at once that each `C_m` is free of finite type over `A`. (Indeed, one has
`C_m = 0` if `m` is not a multiple of `α`, and if `m = d α`, `C_m` is isomorphic to the
`A`-module of homogeneous polynomials of degree `d`, in `q` variables.) Set

```text
B̂_m = lim_n B_m ⊗_A (A/m^{n+1}),
Ĉ_m = lim_n C_m ⊗_A (A/m^{n+1}),
B̂ = ⨁_{m ∈ M} B̂_m,    Ĉ = ⨁_{m ∈ M} Ĉ_m.
```

One then has canonical morphisms of `M`-graded algebras

```text
g_B : B → B̂    and    g_C : C → Ĉ.
```

It follows from the remark made above that `g_C` is an isomorphism. To give a coherent
system `(f_n)` as in the statement is equivalent to giving a morphism of graded
`A`-algebras

```text
F̂ : B̂ → Ĉ.
```

To find a morphism `f` as in the statement is equivalent to finding a morphism of graded
`A`-algebras `F : B → C` rendering commutative the diagram

```text
B  ──F──→  C
│           │
g_B         g_C
↓           ↓
B̂  ──F̂──→  Ĉ.
```

Since `g_C` is an isomorphism, the existence and uniqueness of `F` are immediate. This
proves 1.10.

<!-- original page 44 -->

To complete the proof of 1.5, it remains only to prove 1.9.

**1.12. Proof of 1.9.** One has `g = t ⊕ g_α ⊕ g_{−α}`. As explained in 1.9, consider `g`
as a `(T ·_α G_{a, k})`-module. It is clear that `t ⊕ g_α` is a submodule of `g`, the
quotient being isomorphic to `g_{−α}` as a `k`-vector space and even as a `T`-module. It
is clear that `G_{a, k}` acts trivially on this quotient, which is of dimension 1 (for
every group morphism from `G_{a, k}` to `G_{m, k}` is trivial). Similarly `g_α` is a
submodule of `t ⊕ g_α`, the quotient being isomorphic to `t` as a `T`-module, `G_{a, k}`
acting trivially on it. To summarize:

<!-- label: III.XX.1.12 -->

**Lemma 1.13.** *Under the conditions of 1.9, `g` admits a composition series as
`(T ·_α G_{a, k})`-module whose successive quotients are*

```text
g_{−α}, t, g_α,
```

*viewed as `(T ·_α G_{a, k})`-modules via the projection `T ·_α G_{a, k} → T`.*

<!-- label: III.XX.1.13 -->

One is therefore reduced to computing the cohomology of `T ·_α G_{a, k}` acting via the
projection `T ·_α G_{a, k} → T` and the character `β` of `T` (here `β = 0`, `α`, or `−α`)
on `W(k)`.[^N.D.E-XX-5] Let `k[x_1, …, x_n]` denote the algebra of polynomials over `k` in
`n` variables and `k_q[x_1, …, x_n]` the subspace of homogeneous polynomials of degree
`q`.

**Lemma 1.14.** *With the preceding notations, one has `H^n(T ·_α G_{a, k}, k) = H^n(C^*_{α, β})`,
where the complex `C^*_{α, β}` is defined by*

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

Indeed, the functor `M ↦ H^0(T, M)` is exact on the category of `T`-modules (and the
`H^q(T, −)` vanish), by Exp. I 5.3.2. It follows, as in the usual case of group cohomology,
that `H^n(T ·_α G_{a, k}, k)` can be computed as the `n`-th cohomology group of the
complex of cochains of `G_{a, k}` in `k`, invariant under `T`, i.e. satisfying

```text
f(α(t) x_1, …, α(t) x_n) = β(t) f(x_1, …, x_n).
```

This indeed gives the announced complex.

To prove 1.9, it therefore suffices to prove that `H²(C^*_{α, β}) = 0` for `β = 0, α, −α`,
which is done at once.

**Remark 1.15.** *One can explicitly compute the groups `H^n(C^*_{α, β})` for `β = q α`
(see M. Lazard,* Lois de groupes et analyseurs*, Annales E.N.S., 1955). In particular, one
finds `H^n(C^*_{α, q α}) = 0` for `n > q`.*

<!-- label: III.XX.1.15 -->

**Notations 1.16.** *The image of the canonical immersion*

```text
W(g_{−α}) ×_S T ×_S W(g_α) → G
```

<!-- original page 46 -->

*will be denoted `Ω`. It is an open subset of `G` containing the unit section. The image of*

```text
W(g_{−α}),   resp. W(g_α),   resp. W(g_{−α}) ×_S T,   resp. T ×_S W(g_α)
```

*will be denoted*[^N.D.E-XX-6]

```text
U_{−α},   resp. U_α,   resp. U_{−α} · T,   resp. T · U_α.
```

*Then `U_α` (resp. `U_{−α}`) is a subgroup of `G` canonically endowed with a vector bundle
structure, and one has*

```text
int(t)(x) = x^{α(t)}    (resp. x^{−α(t)}),
```

*for every `S′ → S`, `t ∈ T(S′)`, `x ∈ U_α(S′)` (resp. `x ∈ U_{−α}(S′)`).*

<!-- label: III.XX.1.16 -->

One has canonical isomorphisms

```text
T · U_α ≅ T ·_α U_α    and    T · U_{−α} ≅ T ·_{−α} U_{−α}.
```

The open set `Ω` is stable under `int(T)`: one has

```text
int(t′)(y · t · x) = y^{−α(t′)} · t · x^{α(t′)}.
```

**Corollary 1.17.** *One has `Lie(U_α / S) = g_α` and `Lie(U_{−α} / S) = g_{−α}`. The
isomorphisms*

```text
W(g_α)  ──exp──→  U_α    and    W(g_{−α})  ──exp──→  U_{−α}
```

*are those of Exp. XIX 4.2.*

<!-- label: III.XX.1.17 -->

**Corollary 1.18.** *The open set `Ω` is relatively schematically dense in `G` (cf. XVIII,
§ 1).*

<!-- label: III.XX.1.18 -->

Clear by Exp. XVIII, 1.3.[^N.D.E-XX-7]

**Corollary 1.19.** *The center of `G` is `Centr(G) = Ker(α)`. It is therefore a closed
subgroup of `G`, of multiplicative type and of finite type.*

<!-- label: III.XX.1.19 -->

The second assertion follows from the first by Exp. IX 2.7. Let us therefore prove the
first. The inner automorphism defined by a section of `Ker(α)` acts trivially on `Ω` (last
formula of 1.16), hence on `G` by 1.18. Conversely, if `g ∈ G(S)` centralizes `G`, then it
centralizes `T` and `U_α`, hence is a section of `T` (Exp. XIX 2.8) annihilating `α`; since
this also holds after any base change, one indeed has `Centr(G) = Ker(α)`.

**Corollary 1.20.** *For there to exist a monomorphism `p_α : G_{a, S} → G` normalized by
`T` with multiplier `α`, it is necessary and sufficient that the `O_S`-module `g_α` be
free. More precisely, one has a bijection given by*

```text
X_α ↦ (x ↦ exp(x X_α))    and    p_α ↦ Lie(p_α)
```

<!-- original page 47 -->

*between `Γ(S, g_α)^×` and the set of monomorphisms `p_α` as above (which is also the set
of isomorphisms of vector group schemes `G_{a, S} ─∼→ U_α`).*[^N.D.E-XX-8]

<!-- label: III.XX.1.20 -->

**Corollary 1.21.** *The subgroups `U_α` and `U_{−α}` of `G` commute on no fiber.*

<!-- label: III.XX.1.21 -->

Indeed, if `(U_α)_s` and `(U_{−α})_s` commute, then `Ω_s` is a subgroup of `G_s`, hence
`Ω_s = G_s`[^N.D.E-XX-9] and `G_s` is solvable, which contradicts the hypothesis that
`G_s` is reductive of semisimple rank 1.

[^N.D.E-XX-1]: N.D.E.: of `O_S`-modules.
[^N.D.E-XX-2]: N.D.E.: We shall see later (Cor. 5.9) that `exp` is an isomorphism of `W(g_α)` onto a closed subgroup of `G`.
[^N.D.E-XX-3]: N.D.E.: see also VI_B, 2.5.
[^N.D.E-XX-4]: N.D.E.: by EGA IV₄, 17.9.1.
[^N.D.E-XX-5]: N.D.E.: We have added the sentence that follows.
[^N.D.E-XX-6]: N.D.E.: We have replaced `P_{−α}` and `P_α` by `U_{−α}` and `U_α`.
[^N.D.E-XX-7]: N.D.E.: see also EGA IV₃, 11.10.10.
[^N.D.E-XX-8]: N.D.E.: Indeed, on the one hand, `Lie(G_{a, S}) = O_S` and `Lie(p_α)` is an element of `Hom_{O_S}(O_S, g_α) = Γ(S, g_α)`.
[^N.D.E-XX-9]: N.D.E.: by 1.18.

## 2. Structure of elementary systems

<!-- label: III.XX.2 -->

**Theorem 2.1.** *Let `S` be a scheme, `(G, T, α)` an `S`-elementary system. There exists a
morphism of `O_S`-modules*

```text
g_α ⊗_{O_S} g_{−α} → O_S,   (X, Y) ↦ ⟨X, Y⟩,
```

*and a morphism of `S`-groups*

```text
α* : G_{m, S} → T
```

*such that for every `S′ → S` and all `X ∈ Γ(S′, g_α ⊗ O_{S′})`, `Y ∈ Γ(S′, g_{−α} ⊗ O_{S′})`
one has the equivalence:*

```text
exp(X) · exp(Y) ∈ Ω(S′) ⇐⇒ 1 + ⟨X, Y⟩ ∈ G_m(S′),
```

*and under these conditions one has the formula:*

```text
(F)    exp(X) · exp(Y) = exp( Y / (1 + ⟨X, Y⟩) ) · α*(1 + ⟨X, Y⟩) · exp( X / (1 + ⟨X, Y⟩) ).
```

<!-- label: eq:III.XX.2.1.F -->

*Moreover, the morphisms `(X, Y) ↦ ⟨X, Y⟩` and `α*` are uniquely determined, the former is
an isomorphism, hence puts the modules `g_α` and `g_{−α}` in duality, and one has*
`α ∘ α* = 2` *(squaring in `G_{m, S}`).*

<!-- label: III.XX.2.1 -->

<!-- original page 48 -->

In view of the uniqueness assertions of the theorem, it suffices to do the proof locally on
`S`. One can therefore assume `g_α` and `g_{−α}` free on `S`. Take then
`X ∈ Γ(S, g_α)^×`, `Y ∈ Γ(S, g_{−α})^×` and set `p_α(x) = exp(x X)`, `p_{−α}(y) = exp(y Y)`,
for `x, y ∈ G_a(S′)`, `S′ → S`. By 1.5 and 1.21, it suffices to prove:

**Proposition 2.2.** *Let `S` be a scheme, `G` an `S`-group, `T` a torus of `G`, `α` a
character of `T` non-trivial on each fiber, `p_α : G_{a, S} → G` (resp.
`p_{−α} : G_{a, S} → G`) a group monomorphism normalized by `T` with multiplier `α`
(resp. `−α`). Suppose that:*

*(i) The morphism `G_{a, S} ×_S T ×_S G_{a, S} → G` defined by
`(y, t, x) ↦ p_{−α}(y) t p_α(x)` is an open immersion. Denote its image by `Ω`.*

*(ii) For every `s ∈ S`, `(p_α)_s(G_{a, κ(s)})` and `(p_{−α})_s(G_{a, κ(s)})` do not
commute.*

*Then there exist `a ∈ G_a(S)` and `α* ∈ Hom_{S-gr.}(G_{m, S}, T)`, uniquely determined,
having the following properties: for every `S′ → S` and all `x, y ∈ G_a(S′)`, one has*

```text
p_α(x) p_{−α}(y) ∈ Ω(S′) ⇐⇒ 1 + a x y ∈ G_m(S′),
```

<!-- original page 49 -->

*and, under this condition, one has the formula*

```text
p_α(x) p_{−α}(y) = p_{−α}( y / (1 + a x y) ) · α*(1 + a x y) · p_α( x / (1 + a x y) ).
```

*Moreover, `a` is invertible (i.e. `a ∈ G_m(S)`) and `α ∘ α* = 2`.*

<!-- label: III.XX.2.2 -->

*Proof:*

A) Consider the morphism

```text
G_{a, S}² → G
```

defined by `(x, y) ↦ p_α(x) p_{−α}(y)`. Let `U` be the inverse image of `Ω` under this
morphism. It is an open subset of `G_{a, S}²` containing `0 ×_S G_{a, S}` and
`G_{a, S} ×_S 0`. There therefore exist uniquely determined `S`-scheme morphisms

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

Let `S′` be a separated `S`-scheme and let `t ∈ T(S′)` be a point of `T`. Since `Ω_{S′}` is
stable under `int(t)`, then, by the last formula of 1.16, `U_{S′}` is stable under the
automorphism `(x, y) ↦ (α(t) x, α(t)⁻¹ y)` of `G_{a, S′}²`, and one has the relations:

```text
A(α(t) u, α(t)⁻¹ v) = α(t)⁻¹ A(u, v),
C(α(t) u, α(t)⁻¹ v) = α(t) C(u, v),
B(α(t) u, α(t)⁻¹ v) = B(u, v).
```

Since `α` is faithfully flat, one deduces that for every `S′ → S` and every `z ∈ G_m(S′)`,
`U_{S′}` is stable under the transformation `(x, y) ↦ (z x, z⁻¹ y)` and one has

```text
A(z u, z⁻¹ v) = z⁻¹ A(u, v),
C(z u, z⁻¹ v) = z C(u, v),
B(z u, z⁻¹ v) = B(u, v).
```

Suppose first that `v` is invertible; setting `z = v`, one deduces that if `(u, v)` is a
section of `U`, then `(u v, 1)` is also one, and one has

```text
A(u v, 1) = v⁻¹ A(u, v),    B(u v, 1) = B(u, v).
```

Let then `V` be the open set of `G_{a, S}²` defined by[^N.D.E-XX-10]

```text
(u, v) ∈ V(S′) ⇐⇒ (u, v), (u v, 1) and (1, u v) belong to U(S′).
```

<!-- original page 50 -->

Since `U` is an open set of `G_{a, S}²` containing `0 ×_S G_{a, S}` and `G_{a, S} ×_S 0`,
then `V` is a neighborhood of the zero section of `G_{a, S}²` and we have just seen that
the morphisms

```text
(u, v) ↦ A(u, v) and (u, v) ↦ v A(u v, 1)
resp. (u, v) ↦ B(u, v) and (u, v) ↦ B(u v, 1)
```

coincide on `V ∩ (G_{a, S} ×_S G_{m, S})`. Since `G_{a, S} ×_S G_{m, S}` is schematically
dense in `G_{a, S}²`, these morphisms therefore coincide on `V`.

One knows that `A(0, 1) = 1`; it follows that there exists an open set `W_1` of `G_{a, S}`
containing the zero section such that for every section `x` of `W_1`, `A(x, 1)` is
invertible; setting `A(x, 1)⁻¹ = F(x)`, one obtains that if `(u, v) ∈ V(S′)`[^N.D.E-XX-11]
and `u v ∈ W_1(S′)`, `S′ → S`, then `A(u, v) = v A(u v, 1) = v F(u v)⁻¹`. Arguing similarly
for `C`, one obtains that there exists an open set `W_2` of `G_{a, S}` containing the zero
section, and an element `E`[^N.D.E-XX-12] of `O(W_2)^×`, such that
`C(u, v) = u C(1, u v) = u E(u v)⁻¹`, if `(u, v) ∈ V(S′)` and `u v ∈ W_2(S′)`. Consequently,
setting `W = W_1 ∩ W_2`, one obtains:

There exists an open set `W` of `G_{a, S}` containing the zero section, and
`S`-morphisms

```text
F : W → G_{m, S},   F(0) = 1,
H : W → T,         H(0) = e,
E : W → G_{m, S},   E(0) = 1,
```

such that if `(u, v) ∈ V(S′)` and `u v ∈ W(S′)`, `S′ → S`, one has

```text
(+)    p_α(u) p_{−α}(v) = p_{−α}(v F(u v)⁻¹) H(u v) p_α(u E(u v)⁻¹).
```

B) Let us now use the associativity of `G` to write

```text
p_α(u) p_{−α}(v) p_{−α}(w) = p_α(u) p_{−α}(v + w).
```

There exists an open set `L` of `G_{a, S}³`, containing the unit section, such that
`(u, v, w) ∈ L(S′)` is equivalent to

```text
(u, v) ∈ V(S′),   (u E(u v)⁻¹, w) ∈ V(S′),   (u, v + w) ∈ V(S′),
u v ∈ W(S′),     u w E(u v)⁻¹ ∈ W(S′),       u(v + w) ∈ W(S′).
```

Using then the formula (+), one writes at once for `(u, v, w) ∈ L(S′)` the relations:

<!-- original page 51 -->

```text
(1)   E(u v + u w) = E(u w E(u v)⁻¹) E(u v),
(2)   H(u v + u w) = H(u w E(u v)⁻¹) H(u v),
(3)   (v + w) F(u v + u w)⁻¹ = α(H(u v)⁻¹) w F(u w E(u v)⁻¹)⁻¹ + v F(u v)⁻¹.
```

It is immediate from the definition of `L` that `(1, 0, 0) ∈ L(S)`. Consider therefore

```text
L ∩_T (1 ×_S G_{a, S} ×_S G_{a, S}) = 1 ×_S M;
```

`M` is an open set of `G_{a, S}²`, containing the section `(0, 0)`, and for
`(v, w) ∈ M(S′)`, one has `v, w E(v)⁻¹, v + w ∈ W(S′)` and

```text
(1′)   E(v + w) = E(w E(v)⁻¹) E(v),
(2′)   H(v + w) = H(w E(v)⁻¹) H(v),
(3′)   (v + w) F(v + w)⁻¹ = α(H(v))⁻¹ w F(w E(v)⁻¹)⁻¹ + v F(v)⁻¹.
```

Consider finally the morphism from `M` to `G_{a, S}²` defined set-theoretically by
`(v, w) ↦ (v, w E(v)⁻¹)`.[^N.D.E-XX-13] It preserves the section `(0, 0)` and induces an
isomorphism of `M` onto an open set `N` of `G_{a, S}²` containing the zero section (the
inverse isomorphism being given by `(x, y) ↦ (x, y E(x))`).[^N.D.E-XX-14] One has thus
proved the following assertion:

There exists an open set `N` of `G_{a, S}²`, containing the zero section, such that if
`(x, y) ∈ N(S′)`, then `x, y` and `x + y E(x)`[^N.D.E-XX-15] belong to `W(S′)` and:

```text
(1″)   E(x + y E(x)) = E(x) E(y),
(2″)   H(x + y E(x)) = H(x) H(y),
(3″)   (x + y E(x)) F(x + y E(x))⁻¹ = x F(x)⁻¹ + α(H(x))⁻¹ y E(x) F(y)⁻¹.
```

C) Arguing similarly with left associativity, one demonstrates the following
assertion:[^N.D.E-XX-16]

There exists an open set `N′` of `G_{a, S}²`, containing the zero section, such that if
`(x, y) ∈ N′(S′)`, then `x, y` and `x + y F(x)`[^N.D.E-XX-17] belong to `W(S′)`, and

<!-- original page 52 -->

```text
(4″)   F(x + y F(x)) = F(x) F(y),
(5″)   H(x + y F(x)) = H(x) H(y),
(6″)   (x + y F(x)) E(x + y F(x))⁻¹ = x E(x)⁻¹ + α(H(x))⁻¹ y F(x) E(y)⁻¹.
```

We are therefore led to solve the "functional equation" (1″).

**Lemma 2.3.** *Let `S` be a scheme, `W` an open set of `G_{a, S}` containing the unit
section, `F : W → G_{m, S}` an `S`-morphism. Suppose that `F(0) = 1` and that there
exists an open set `N` of `G_{a, S}²` containing the zero section such that for
`(x, y) ∈ N(S′)`, `x, y`, and `x + y F(x)`[^N.D.E-XX-17] belong to `W(S′)` and that one
has:*

```text
(†)    F(x + y F(x)) = F(x) F(y).
```

*(i) If `S` is the spectrum of a field `k`, there exists `a ∈ k` such that `F(x) = 1 + a x`.*

*(ii) If `a = F′(0) ∈ Γ(S, O_S)` is invertible, then `F(x) = 1 + a x`.*

<!-- label: III.XX.2.3 -->

By the hypotheses, we can differentiate the given equation at `x = 0` (resp. at `y = 0`)
and we find that

```text
(∗)    F′(y) (1 + y F′(0)) = F′(0) F(y)    for (0, y) ∈ N(S′),
```

resp.

```text
F′(x) F(x) = F(x) F′(0)    for (x, 0) ∈ N(S′).
```

Since `F` takes its values in `G_m`, the second relation gives us

```text
(∗′)   F′(x) = F′(0)    for (x, 0) ∈ N(S′);
```

whence, by the first,

```text
F′(0)(1 + y F′(0)) = F′(0) F(y)    for (y, 0), (0, y) ∈ N(S′).
```

If `a = F′(0)` is invertible, this gives us

<!-- original page 53 -->

```text
F(y) = 1 + a y,
```

for `y` a section of an open set of `W` containing the unit section, hence schematically
dense in `W`, which proves (ii). This also proves (i) when `F′(0) ≠ 0`.

If `F′(0) = 0`, then, by (∗′), `F′(x) = 0` when `x` is "near 0", hence `F′ = 0` by
schematic density. If `k` is of characteristic 0, `F` is a rational fraction with zero
derivative, hence constant and equal to `F(0) = 1`.

If `k` is of characteristic `p`, and if `F` is not constant,[^N.D.E-XX-18] there exists an
integer `n > 0` and a rational fraction `F_1 ∈ k(X)` such that `F′_1(X) ≠ 0` and

```text
F(X) = F_1(X^{p^n}) = F_1(X)^{p^n}.
```

Substituting in the functional equation, one finds

```text
(†_1)   F_1(x + y F_1(x)^{p^n}) = F_1(x) F_1(y).
```

Differentiating at `x = 0`, one finds

```text
(∗_1)   F′_1(y) = F′_1(0) F_1(y),
```

and differentiating (†_1) at `y = 0`, one obtains

```text
(∗′_1)  F′_1(x) F_1(x)^{p^n} = F_1(x) F′_1(0).
```

Since, by hypothesis, `F′_1(X)` is an invertible element of `k(X)`, one deduces from these
two equalities that

```text
F_1(X)^{p^n} = 1,
```

hence `F_1` is a constant, contradicting the initial hypothesis. This shows that `F` is
constant, and equal to `1 = F(0)`.

D) Suppose `S` is the spectrum of a field. If `F′(0) = 0`, then `F = 1`. Formula (5″) then
gives us `H(x + y) = H(x) H(y)`, which shows that `H` extends to a group morphism
`G_{a, S} → T` (Exp. XVIII 2.3), which is necessarily constant of value `e`. On the other
hand, by Lemma 2.3, one will also have `E(x) = 1 + b x` for some `b ∈ k`. But then (6″)
gives, for `(x, y) ∈ N(S′)`,

```text
(x + y) E(x + y)⁻¹ = x E(x)⁻¹ + y E(y)⁻¹,
```

hence,[^N.D.E-XX-19] by Exp. XVIII 2.3 again, `x ↦ x E(x)⁻¹` extends to a morphism of
`k`-groups `G_{a, k} → G_{a, k}`, hence `x/(1 + b x) = c x` for some `c ∈ k`, whence `b = 0`
(and `c = 1`).

<!-- original page 54 -->

This shows that `F, H, E` are constant of value `(1, e, 1)` in a neighborhood of the unit
section, hence everywhere, which by (+) shows that `U_α` and `U_{−α}` commute, contrary to
hypothesis (ii).

If `S` is now arbitrary, one has therefore proved that `F′(0)` is non-zero on no fiber,
hence is invertible. The same evidently holds for `E′(0)`, which by Lemma 2.3 shows that
there exist `a, b ∈ G_m(S)` such that

```text
(♦_1)   F(x) = 1 + a x,    E(x) = 1 + b x,    for x ∈ W(S′).
```

E) The rest is now easy. Substituting the preceding results into (3″), one finds

```text
y α(H(x)) (1 + a y) = y (1 + a x + a y(1 + b x)) (1 + a x).
```

This formula is valid for every section `(x, y)` of `N`. But since `G_{a, S} ×_S G_{m, S}`
is schematically dense in `G_{a, S}²`, one deduces

```text
(1 + a y) α(H(x)) = (1 + a x + a y(1 + b x)) (1 + a x).
```

Setting `y = 0`, this gives `α(H(x)) = (1 + a x)²`. Substituting this into the preceding
equality, one finds[^N.D.E-XX-20]

```text
a² x y = a b x y.
```

Since `G_{m, S}` is schematically dense in `G_{a, S}`, one deduces `a² = a b`, whence,
since `a` is invertible,

```text
(♦_2)   a = b    and    α(H(x)) = (1 + a x)².
```

Since `a` is invertible, `x ↦ 1 + a x` is an automorphism of `G_{a, S}`; one can therefore
find an open set `W′` of `G_{a, S}` containing the section `1` and a morphism

```text
P : W′ → T
```

such that `P(1 + a x) = H(x)`.[^N.D.E-XX-21]

Substituting in the relation (2′), one finds at once for `(x, y) ∈ N(S′)`,

```text
P(1 + a x + a y) = P((1 + a x + a y) / (1 + a x)) P(1 + a x),
```

which proves that there exists an open neighborhood of `1` in `G_{m, S}` such that one has
for `x` and `y` in this neighborhood `P(x) P(y) = P(x y)`. By Exp. XVIII 2.3, there exists
a group morphism

```text
(♦_3)   α* : G_{m, S} → T
```

<!-- original page 55 -->

extending `P`. Since `α(H(x)) = (1 + a x)²` near the section `0`, one has `α(α*(z)) = z²`
near the section `1`, hence

```text
(♦_4)   α ∘ α* = 2.
```

F)[^N.D.E-XX-22] Assembling the results (+) and (♦_1 — ♦_4), one sees that there exist
`a ∈ G_m(S)` and `α* ∈ Hom_{S-gr.}(G_{m, S}, T)` such that `α ∘ α* = 2` and that, if
`(u, v) ∈ V(S′)` and `u v ∈ W(S′)`, then `1 + a u v` is invertible and

```text
p_α(u) p_{−α}(v) = p_{−α}( v / (1 + a u v) ) · α*(1 + a u v) · p_α( u / (1 + a u v) ).
```

Consider the open set `V′` of `G_{a, S}²` defined by "`1 + a u v` invertible", i.e.
`V′ = (G_{a, S}²)_f` where `f(u, v) = 1 + a u v`. The two sides of the preceding formula
define morphisms from `V′` to `G` which coincide in a neighborhood of the section `0`,
hence coincide on `V′`. The preceding formula is therefore valid for every section
`(u, v)` of `V′`. In particular, it follows that `V′ ⊂ U`, where `U` is the open set
introduced at the beginning of A).

Let us prove that `U = V′`. Returning to the notations of A), one has a morphism

```text
A : U → G_{a, S}
```

which, on `V′`, is defined by `A(u, v) = v (1 + a u v)⁻¹`. To show that `U = V′`, which is
a set-theoretic question, one is reduced to the case where `S` is the spectrum of a field
`k`, hence to the obvious assertion: the domain of definition of the rational map
`G_{a, k}² → G_{a, k}` defined by the rational fraction `Y / (1 + a X Y)` is the open set
defined by the function `1 + a X Y`.

G) One has thus proved the existence of `a` and `α*`, as well as the two additional
properties announced. It remains to prove uniqueness. Let then `a′` and `α*′` also satisfy
the required conditions. If `u, v ∈ G_a(S′)²`, one has at once:

<!-- original page 56 -->

```text
1 + a u v invertible ⇒ 1 + a′ u v invertible and v / (1 + a u v) = v / (1 + a′ u v);
```

one therefore has for every section `u` of `G_a(S′)`

```text
1 + a u invertible ⇒ 1 + a u = 1 + a′ u,
```

which proves at once `a = a′`.

With the same notations, one then has

```text
1 + a u invertible ⇒ α*(1 + a u) = α*′(1 + a u),
```

hence also `α* = α*′`.

**Corollary 2.4.** *Let `exp(Y) t exp(X)` and `exp(Y′) t′ exp(X′)` be two elements of
`Ω(S′)`. Then their product is in `Ω(S′)` if and only if `u = 1 + ⟨X, Y′⟩` is invertible,
and one has then*

```text
(F′)    exp(Y) t exp(X) · exp(Y′) t′ exp(X′) =
             exp(Y + u⁻¹ α(t)⁻¹ Y′) · t t′ α*(u) · exp(u⁻¹ α(t′)⁻¹ X + X′).
```

<!-- label: III.XX.2.4 -->

**Remark 2.5.** *One can also write formula (F) of Theorem 2.1 without invoking the
morphisms `exp`. Indeed, transporting through these morphisms the duality
`g_α ⊗ g_{−α} → O_S`, one obtains a canonical pairing of vector bundles:*

```text
U_α ×_S U_{−α} → G_{a, S},
```

*which we shall still denote `(x, y) ↦ ⟨x, y⟩`. One therefore has*

```text
⟨exp X, exp Y⟩ = ⟨X, Y⟩.
```

*If `x ∈ U_α(S′)`, `y ∈ U_{−α}(S′)` and if `1 + ⟨x, y⟩ ∈ G_m(S′)`, one has*

```text
(F)    x · y = y^{(1 + ⟨x, y⟩)⁻¹} · α*(1 + ⟨x, y⟩) · x^{(1 + ⟨x, y⟩)⁻¹}.
```

<!-- label: III.XX.2.5 -->

**Corollary 2.6.** *The pairing*

```text
W(g_α) ×_S W(g_{−α}) → G_{a, S}
```

<!-- original page 57 -->

*defines a pairing of principal `G_{m, S}`-bundles*

```text
W(g_α)^× ×_S W(g_{−α})^× → G_{m, S}.
```

*This pairing will be denoted `(X, Y) ↦ ⟨X, Y⟩`, or more simply `(X, Y) ↦ X Y`.*

<!-- label: III.XX.2.6 -->

For every section `X ∈ Γ(S, g_α)^×`, there therefore exists a unique section `X⁻¹` of
`Γ(S, g_{−α})^×` such that `X X⁻¹ = 1`. One has `(z X)⁻¹ = z⁻¹ X⁻¹`. The morphism

```text
s : W(g_α)^× → W(g_{−α})^×
```

thus defined is therefore an isomorphism of schemes, compatible with the isomorphism
`s : z ↦ z⁻¹` on the operator groups.

**Definition 2.6.1.** *One says that `X` and `s(X) = X⁻¹` are* paired.

<!-- label: III.XX.2.6.1 -->

Apply Corollary 2.4 to `Y = 0 = X′` and `Y′ = a X⁻¹`, `a ∈ O_S(S)`. Then `u = 1 + a` and
`u⁻¹ Y′ = u⁻¹(u − 1) X⁻¹ = (1 − u⁻¹) X⁻¹`, whence:

**Corollary 2.7.** *Let `X ∈ Γ(S, g_α)^×` and `u ∈ Γ(S, O_S)^×`. One has*

```text
α*(u) = exp((u⁻¹ − 1) X⁻¹) exp(X) exp((u − 1) X⁻¹) exp(−u⁻¹ X).
```

<!-- label: III.XX.2.7 -->

**Definition 2.8.** *The morphism `α*` is called the* coroot *associated with the root
`α`.*

<!-- label: III.XX.2.8 -->

**Remark 2.9.** *If `(G, T, α)` is an `S`-elementary system, `(G, T, −α)` is also one. By
Theorem 2.1 one therefore has a duality between `g_{−α}` and `g_α`, and a coroot `(−α)*`.
Taking the inverse of formula (F), one proves at once*

```text
⟨X, Y⟩ = ⟨Y, X⟩,    (−α)* = −α*.
```

<!-- label: III.XX.2.9 -->

Let us now pass to the Lie algebra of `G`. The root `α` and the coroot `α*` define the
linear forms

```text
O_S  ──α*──→  t  ──α──→  O_S.
```

<!-- original page 58 -->

One will denote `H_α = α*(1)`. One calls `α` the *infinitesimal root* associated with `α`,
and `H_α` the corresponding *infinitesimal coroot*.

**Lemma 2.10.** *Let `S′ → S` and `X, X′ ∈ W(g_α)(S′)`, `H ∈ W(t)(S′)`,
`Y, Y′ ∈ W(g_{−α})(S′)`, `t ∈ T(S′)`. One has*

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

```text
(4)   H_{−α} = −H_α.
```

```text
(5)   α(H_α) = 2.
```

<!-- label: III.XX.2.10 -->

The proof of these various formulas is either trivial or an immediate consequence of
formula (F) of 2.1.

**Corollary 2.11.** *Suppose `H_α` is non-zero on every fiber (which is in particular the
case if `2` is invertible on `S`, by (5)). Then `X_α ∈ Γ(S, g_α)^×` and
`X_{−α} ∈ Γ(S, g_{−α})^×` are paired if and only if `[X_α, X_{−α}] = H_α`.*

<!-- label: III.XX.2.11 -->

<!-- original page 59 -->

**2.12.** Let `(G, T, α)` be an `S`-elementary system. We know (1.19) that the center of
`G` is `Centr(G) = Ker(α)`, a group of multiplicative type and of finite type. If `Q` is a
subgroup of multiplicative type of `Centr(G)`, the quotient `G/Q` is affine over `S`
(Exp. IX 2.5), smooth over `S` (Exp. VI_B 9.2) with connected reductive fibers of
semisimple rank 1 (Exp. XIX 1.8).

Set `G′ = G/Q`; this is a reductive `S`-group of semisimple rank 1; `T′ = T/Q` is a maximal
torus of it. The open set `U_{−α} · T · U_α` of `G` is stable under `Q`, and one sees at
once that the quotient is isomorphic to `U_{−α} ×_S (T/Q) ×_S U_α`. If one denotes by `α′`
the character of `T′` induced by `α`, it follows that the morphism derived from the
canonical morphism `G → G′` induces isomorphisms

```text
g_α  ──∼──→  g′_{α′}    and    g_{−α}  ──∼──→  g′_{−α′}.
```

In particular, `α′` is a root of `G′` with respect to `T′`. Hence, denoting by `α/Q` the
character `T/Q → G_{m, S}` induced by `α`, one has:

**Lemma 2.13.** *If `Q` is a subgroup of multiplicative type of `Ker(α)`, then*

```text
(G/Q, T/Q, α/Q)
```

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

[^N.D.E-XX-10]: N.D.E.: We have added the condition "`(1, u v) ∈ U(S′)`".
[^N.D.E-XX-11]: N.D.E.: here and in what follows, we have replaced `U(S′)` by `V(S′)`.
[^N.D.E-XX-12]: N.D.E.: We have denoted by `E` the element denoted `G` in the original, since `G` already denotes the `S`-group under consideration.
[^N.D.E-XX-13]: N.D.E.: We have corrected what follows.
[^N.D.E-XX-14]: N.D.E.: that is, we have made the "change of variables" `x = v`, `y = w E(v)⁻¹`, i.e. `v = x`, `w = y E(x)`.
[^N.D.E-XX-15]: N.D.E.: We have corrected `y E(x)` to `x + y E(x)`.
[^N.D.E-XX-16]: N.D.E.: that is, one writes the equalities resulting from `p_α(t) p_α(u) p_{−α}(v) = p_α(t + u) p_{−α}(v)` and sets `v = 1` and `x = u`, `t = y F(u)` (i.e. `y = t F(u)⁻¹`).
[^N.D.E-XX-17]: N.D.E.: We have corrected `y F(x)` to `x + y F(x)`.
[^N.D.E-XX-18]: N.D.E.: We have corrected what follows.
[^N.D.E-XX-19]: N.D.E.: We have added the sentence that follows. One can also see by a direct calculation that the preceding equality entails `0 = x y b (2 + (x + y) b)`, hence `0 = b(2 + (x + y) b)`, and finally `b = 0`.
[^N.D.E-XX-20]: N.D.E.: In the three preceding equalities, we have corrected the original by replacing the factor `(1 + b x)` on the right by `1 + a x`. Substituting the third equality into the second and taking into account that `1 + a x` is invertible, one obtains the equality `a² x y = a b x y`.
[^N.D.E-XX-21]: N.D.E.: that is, we have made the change of variables `x′ = 1 + a x`, i.e. `x = (x′ − 1)/a`.
[^N.D.E-XX-22]: N.D.E.: We have slightly modified what follows, since an open set `V` was already introduced in A).

## 3. The Weyl group

<!-- label: III.XX.3 -->

<!-- original page 60 -->

**Notations 3.0.**[^N.D.E-XX-23] If `(G, T, α)` is an `S`-elementary system, one will
denote

```text
N = Norm_G(T),    W = Norm_G(T) / T,
```

(cf. Exp. XIX 6.3); `N` is a closed subgroup of `G`, smooth over `S`. One will denote by
`N^×  = N − T` the open subscheme of `N` induced on the complement of `T`.[^N.D.E-XX-24]
Let `R` be the (unique) maximal torus of `Ker(α)`, and `T′` the image of
`α* : G_{m, S} → T`, which is a subtorus of dimension 1 of `T`.

The morphism

```text
T′ ×_S R → T
```

induced by the product in `T` is surjective (hence faithfully flat); indeed, one is
reduced to checking this on the geometric fibers, and this follows at once from the
formula `α ∘ α* = 2`.

**Theorem 3.1.** *With the preceding notations:*

*(i) `W` is isomorphic to the constant group `(ℤ/2ℤ)_S`.*

<!-- original page 61 -->

*(ii) `N^×` is a principal homogeneous bundle locally trivial under `T`, on the left by the
law `(t, q) ↦ t q` (resp. on the right by the law `(q, t) ↦ q t`).*

*(iii) One has the formula*

```text
int(w) t = t · α*(α(t)⁻¹)
```

*for `w ∈ N^×(S′)`, `t ∈ T(S′)`, `S′ → S`. In the decomposition `T_{S′} = T′_{S′} · R_{S′}`,
`int(w)` induces the identity on `R_{S′}` and the symmetry on `T′_{S′}`. One has the
relations*

```text
α ∘ int(w) = α⁻¹,    int(w) ∘ α* = (α*)⁻¹.
```

*(iv) For `X ∈ W(g_α)^×(S′)`, `S′ → S`, set*

```text
w_α(X) = exp(X) exp(−X⁻¹) exp(X).
```

*Then `w_α(X) ∈ N^×(S′)` and the morphism `w_α : W(g_α)^× → N^×` thus defined satisfies*

```text
w_α(z X) = α*(z) w_α(X) = w_α(X) α*(z)⁻¹,
```

*for `z ∈ G_m(S′)`, `X ∈ W(g_α)^×(S′)`, `S′ → S`.*

*(v)[^N.D.E-XX-25] For `X, Y ∈ W(g_α)^×(S′)`, `S′ → S`, one has, with the notations of 2.6,*

```text
w_α(X) w_α(Y) = α∨(−X Y⁻¹).
```

*In particular,*

```text
w_α(X)² = α*(−1) ∈ ₂T(S) ∩ Centr(G)(S),
w_α(X)⁻¹ = w_α(−X) = α*(−1) w_α(X).
```

*(vi) If one defines analogously, for `Y ∈ W(g_{−α})^×(S′)`,*

```text
w_{−α}(Y) = exp(Y) exp(−Y⁻¹) exp(Y),
```

*one has (in addition to formulas analogous to the preceding)*

```text
w_{−α}(X⁻¹) = w_α(X)⁻¹ = w_α(−X),
w_α(X) w_{−α}(Y) = α*(X Y).
```

<!-- label: III.XX.3.1 -->

*Proof.* (i) has already been seen in Exp. XIX 2.4; it follows at once that `N^×` is indeed
a principal homogeneous bundle under `T` for the laws defined in (ii); the fact that it is
locally trivial (for the Zariski topology) follows notably from (iv).

<!-- original page 62 -->

Let us prove (iii); if `w ∈ N^×(S)`, it is clear that `α ∘ int(w)` is a root of `G` with
respect to `T`, hence is locally equal to `α` or `−α`; since on each fiber it is `−α`
(*Bible*, 12-05, proof of the corollary to prop. 1), one has `α ∘ int(w) = −α`. By
transport of structure, one deduces

```text
−α* = int(w)⁻¹ ∘ α* = int(w) ∘ α*,
```

since `int(w)² = int(w²)` and `w²` is a section of `T`. Therefore `int(w)` induces the
symmetry on `T′`; since `R` is central, `int(w)` induces the identity on `R`. The formula
of (iii) defines a morphism `T → T` which satisfies the same properties, hence coincides
with `int(w)`.

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

but `α ∘ α* = 2`, which gives at once `a = 0` and `w_α(X) ∈ N^×(S′)`.

Let us prove the second assertion of (iv). One has[^N.D.E-XX-26]

```text
α*(z) w_α(X) = exp(z² X) exp(−z⁻² X⁻¹) exp(z² X) α*(z)
             = exp(z X) exp((z² − z) X) exp(−z⁻² X⁻¹) exp(z² X) α*(z)
             = exp(z X) exp(−z⁻¹ X⁻¹) α*(z)⁻¹ exp((z³ − z²) X) exp(z² X) α*(z)
             = exp(z X) exp(−z⁻¹ X⁻¹) exp(z X) = w_α(z X).
```

<!-- original page 63 -->

Let us prove (v). By virtue of the preceding result, the first formula of (v) follows at
once from the second; let us prove the second:

```text
w_α(X)² = exp(X) exp(−X⁻¹) exp(2 X) exp(−X⁻¹) exp(X)
        = exp(X) exp(−X⁻¹) exp(X⁻¹) α*(−1) exp(−2 X) exp(X)
        = exp(X) α*(−1) exp(−X) = α*(−1),
```

since `α(α*(−1)) = (−1)² = 1`, which proves that `α*(−1) ∈ Centr(G)(S)`.

Let us prove (vi). The first assertion is a particular case of the second; let us prove the
second. Both sides of this formula define morphisms `W(g_α)^× ×_S W(g_{−α})^× → G`. To
prove that they coincide, it suffices to do so on a non-empty open set on each fiber
(Exp. XVIII 1.4); it therefore suffices to verify the relation when `1 + X Y` is
invertible. One then has successively:

```text
w_α(X) w_{−α}(Y) = exp(X) exp(−X⁻¹) exp(X) exp(Y) exp(−Y⁻¹) exp(Y)
                 = exp(X) exp(−X⁻¹) exp(Y / (1 + X Y)) α*(1 + X Y) exp(X / (1 + X Y)) exp(−Y⁻¹) exp(Y)
                 = exp(X) exp(−X⁻¹ / (1 + X Y)) α*(1 + X Y) exp(−Y⁻¹ / (1 + X Y)) exp(Y)
                 = exp(−X⁻² Y⁻¹) α*(X Y / (1 + X Y)) exp(X + Y⁻¹) α*(1 + X Y) exp(−Y⁻¹ / (1 + X Y)) exp(Y)
                 = exp(−X⁻² Y⁻¹) α*(X Y) exp((Y⁻¹ + X) / (1 + X Y)²) exp(−Y⁻¹ / (1 + X Y)) exp(Y)
                 = α*(X Y) exp(−Y) exp(Y) = α*(X Y).
```

<!-- original page 64 -->

**Corollary 3.2.** *Let `n ∈ ℤ`, `n ≠ 0`. For every `w ∈ G(S)`, the following conditions are
equivalent:*

*(i) `w ∈ N^×(S)`,*

*(ii) one has `int(w) ∘ n α* = −n α*` (recall that `(n α*)(z) = α*(z)^n`).*

<!-- label: III.XX.3.2 -->

One has (i) ⇒ (ii) (assertion (iii) of Theorem 3.1); conversely, one may suppose that
`N^×` admits a section, and one is reduced to proving:

**Lemma 3.3.** *One has `Centr_G(n α*) = T` for `n ≠ 0`.*

<!-- label: III.XX.3.3 -->

Indeed, the image `T′` of `n α*` is a subtorus of `G`. It follows (Exp. XIX 2.8) that
`Centr_G(n α*)` is a reductive subgroup of `G` containing `T`. Since on each fiber one has
`Centr_{G_s}(n α*_s) ≠ G_s`, then `Centr_{G_s}(n α*_s) = T_s` (Exp. XIX 1.6.3)[^N.D.E-XX-27],
hence `Centr_G(n α*) = T`, since these are smooth subgroups of `G`.

**Remark 3.4.** *The construction of `w_α` and the fact that `w_α(X)` normalizes `T` rely
only on formula (F). In particular, if `G` is an `S`-group satisfying the conditions of
2.2, `Norm_G(T)` differs from `T` on each fiber. It follows that if `G` is an affine
`S`-group with connected fibers satisfying the conditions of 2.2, it is reductive of
semisimple rank 1. Indeed, it is smooth in a neighborhood of the unit section, hence
smooth, and one can apply the criterion of Exp. XIX 1.11.*

<!-- label: III.XX.3.4 -->

**3.5.** Before stating the following theorem, let us make a few remarks. We identify as
usual `g_{−α}` with `(g_α)^{⊗−1}`. Similarly, we shall identify
`Hom_{O_S}(g_{−α}, g_α)` with `(g_α)^{⊗2}` and hence

<!-- original page 65 -->

```text
Isom_{O_S-mod.}(W(g_{−α}), W(g_α)) ≅ W((g_α)^{⊗2})^×.
```

If `w ∈ N^×(S)`, then `Ad(w)` permutes `g_α` and `g_{−α}` (3.1, (iii)), hence defines an
isomorphism:

```text
a_α(w) : g_{−α} ──∼──→ g_α,
```

which we shall therefore identify with a section `a_α(w) ∈ Γ(S, (g_α)^{⊗2})^×`. This
construction is compatible with base change and therefore defines a morphism

```text
a_α : N^× → W((g_α)^{⊗2})^×,
```

such that `a_α(w) Y = Ad(w) Y` for all `w ∈ N^×(S′)`, `Y ∈ Γ(S′, g_{−α})^×`, `S′ → S`.

**Theorem 3.6.** *(i) One has*

```text
int(w) exp(Y) = exp(a_α(w) Y)
```

*for every `S′ → S` and all `w ∈ N^×(S′)`, `Y ∈ W(g_{−α})(S′)`.*

*(ii) One has*

```text
a_α(t w) = α(t) a_α(w),    a_α(w t) = α(t)⁻¹ a_α(w).
```

*(iii) If one defines analogously `a_{−α} : N^× → W((g_{−α})^{⊗2})^×`, one has*

```text
a_{−α}(w) = a_α(w)⁻¹.
```

[^N.D.E-XX-28]

*(iv) For every `X ∈ W(g_α)^×(S′)`, `S′ → S`, one has*

```text
a_α(w_α(X)) = −X².
```

<!-- label: III.XX.3.6 -->

<!-- original page 66 -->

Assertion (i) is trivial, by the characterization of the morphisms `exp` given in 1.5.
Assertion (ii) is immediate, as is (iii). Let us prove (iv): let `X ∈ Γ(S′, g_α)^×`,
`Z ∈ Γ(S′, g_α)`; by definition[^N.D.E-XX-29]

```text
a_α(w_α(X))⁻¹(Z) = Ad(w_α(X))(Z) = Ad(exp(X)) Ad(exp(−X⁻¹)) Ad(exp(X))(Z).
```

Applying formulas (2′) and (2) of Lemma 2.10, as well as the equalities `H_{−α} = −H_α`,
`α(H_α) = 2` (*loc. cit.* (4) and (5)) and `⟨X, X⁻¹⟩ = 1` (2.6), one obtains that the
right-hand side equals successively:

```text
Ad(exp(X)) Ad(exp(−X⁻¹))(Z) = Ad(exp(X))(Z + ⟨X⁻¹, Z⟩ (H_α − X⁻¹))
                            = Z + ⟨X⁻¹, Z⟩ (H_α − 2 X − X⁻¹ − H_α + X)
                            = Z − ⟨X⁻¹, Z⟩ X − ⟨X⁻¹, Z⟩ X⁻¹.
```

But `Z = ⟨X⁻¹, Z⟩ X` and `⟨X⁻¹, Z⟩ X⁻¹ = X⁻² Z`, hence this shows that
`a_α(w_α(X))⁻¹ = −X⁻²`, whence `a_α(w_α(X)) = −X²`.

**Corollary 3.7.** *One has in particular*

```text
int(w_α(X)) exp(X) = exp(−X⁻¹),
```

*whence (by the definition of `w_α(X)`):*

```text
w_α(X) exp(X) w_α(X)⁻¹ = exp(−X) w_α(X) exp(−X),
```

*or, by an immediate calculation,*

```text
(w_α(X) exp(X))³ = e.
```

<!-- label: III.XX.3.7 -->

**Corollary 3.8.** *Let `X ∈ Γ(S, g_α)^×` and `n ∈ ℤ`, `n ≠ 0`. Then `w_α(X)` is the unique
section `w ∈ G(S)` satisfying*

*(i) `int(w) ∘ n α* = −n α*`.*

*(ii) `(w exp(X))³ = e`.*

<!-- label: III.XX.3.8 -->

<!-- original page 67 -->

One knows that `w_α(X)` does satisfy these conditions. Conversely, let `w ∈ G(S)` satisfy
(i) and (ii). By 3.2 and 3.1 (ii), one knows that there exists `t ∈ T(S)` such that
`w = w_α(X) t`. Set `u = exp(X)`. One then has

```text
w u w⁻¹ = w_α(X) t exp(X) t⁻¹ w_α(X)⁻¹ = exp(−α(t) X⁻¹),
```

and on the other hand

```text
u⁻¹ w u⁻¹ = exp(−X) w_α(X) t exp(−X)
          = exp(−X) w_α(X) exp(−X) exp(X − α(t) X) t
          = exp(−X⁻¹) exp(X − α(t) X) t = exp(−X⁻¹) t exp(H).
```

Now `(w u)³ = e ⇔ w u w⁻¹ = u⁻¹ w u⁻¹`; comparing the two decompositions of this element
on `U_{−α} · T · U_α`, one extracts `t = e`.

**Remark 3.9.** *One can summarize a number of results of this number by the following
diagram of principal homogeneous (left) bundles*

```text
W(g_α)^×  ──w_α──→  N^×  ──a_α──→  W((g_α)^{⊗2})^×
   ↓                  ↓                   ↓
G_{m, S}  ──α*──→  T  ──α──→  G_{m, S}.
```

*Note that `a_α` is faithfully flat (`α` being so) and that `w_α` is a monomorphism if and
only if `α*` is a monomorphism. We leave the reader the task of writing the corresponding
diagrams for the right principal bundle structures, as well as the analogous diagrams for
the root `−α`, and of studying the relations between these various diagrams.*

<!-- label: III.XX.3.9 -->

**Lemma 3.10.** *Let `S` be a scheme, `q` an integer `> 0` such that `x ↦ x^q` defines an
endomorphism of `G_{a, S}`, `(G, T, α)` and `(G′, T′, α′)` two `S`-elementary systems,
`f : G → G′` an `S`-group morphism. Let*

<!-- original page 68 -->

```text
h : (g_α)^{⊗q} ──∼──→ g′_{α′}
```

*be an isomorphism of `O_S`-modules and*

```text
h^∨ : (g_{−α})^{⊗q} ──∼──→ g′_{−α′}
```

*the contragredient isomorphism. For every `S′ → S` and every `X ∈ W(g_α)(S′)`, suppose:*

```text
f(exp(X)) = exp(h(X^q)).
```

*Then the following conditions are equivalent:*

*(i) `f(α*(z)) = α′*(z)^q`.*

*(ii) `f(w_α(Z)) = w_{α′}(h(Z^q))`.*

*(iii) `f(exp(Y)) = exp(h^∨(Y^q))`.*

*(Each condition is to be read: for every `S′ → S` and every `z ∈ G_m(S′)`,
`Z ∈ W(g_α)^×(S′)`, `Y ∈ W(g_{−α})(S′)`, one has …).*

<!-- label: III.XX.3.10 -->

Indeed, (i) ⇒ (ii) by 3.8, (ii) ⇒ (iii) by 3.7, (iii) ⇒ (i) by 2.7.

**Proposition 3.11.** *Let `S` be a scheme, `q ∈ ℤ`, `q > 0`, such that `x ↦ x^q` defines an
endomorphism of `G_{a, S}`, `(G, T, α)` and `(G′, T′, α′)` two `S`-elementary systems,
`f : G → G′` an `S`-group morphism. The following conditions on `f` are equivalent:*

*(i) The restriction of `f` to `T` factors through a morphism `f_T : T → T′` making the
diagram*

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

```text
h : (g_α)^{⊗q} → g′_{α′}
```

*such that `f(exp(X)) = exp(h(X^q))`, `f(exp(Y)) = exp(h^∨(Y^q))` for all
`X ∈ W(g_α)(S′)`, `Y ∈ W(g_{−α})(S′)`, `S′ → S` (it follows that `f` also satisfies the
equivalent conditions of 3.10).*

<!-- label: III.XX.3.11 -->

One has (ii) ⇒ (i). Indeed, by 3.10, condition (ii) entails `f ∘ α* = q α′*`, hence, by
3.3, `f|T` factors through `T′`. It remains to prove `α′(f(t)) = α(t)^q`, which follows at
once from the fact that `f` induces a morphism of groups `T · U_α → T′ · U_{α′}`.

Let us prove (i) ⇒ (ii). Let `X ∈ Γ(S, g_α)`, `Y ∈ Γ(S, g_{−α})`. Set `p^+(x) = f(exp(x X))`
and `p^−(y) = f(exp(y Y))`; these are group morphisms

```text
p^+, p^− : G_{a, S} → G.
```

Now one has

```text
int(α′*(z))^q (p^+(x)) = int(f_T(α*(z))) (f(exp(x X)))
                       = f(int(α*(z))(exp(x X)))
                       = f(exp(z² x X)) = p^+(z² x).
```

Applying Lemma 1.2 (with `Q = α′*(G_{m, S})`), one deduces that there exists a section
`X′ ∈ Γ(S, g′_{α′})` such that

```text
f(exp(x X)) = p^+(x) = exp(x^q X′).
```

Similarly, there exists a section `Y′ ∈ Γ(S, g′_{−α′})` such that

```text
f(exp(y Y)) = exp(y^q Y′).
```

Writing now that `f` is a group morphism, hence that it respects formula (F), one obtains
at once

```text
X^q Y^q = (X Y)^q = X′ Y′.
```

<!-- original page 70 -->

One concludes easily that `X^q ↦ X′` and `Y^q ↦ Y′` define isomorphisms `h` and `h^∨` as
announced.

**Proposition 3.12.** *Let `(G, T, α)` be an `S`-elementary system, `w ∈ N^×(S)`; set*

```text
Ω_0 = Ω ∩ int(w⁻¹)(Ω).
```

*Let `d` be the function on `Ω` defined by*

```text
d(exp(Y) · t · exp(X)) = α(t)⁻¹ + X Y.
```

*Then `Ω_0 = Ω_d`, and one has for `exp(Y) · t · exp(X) ∈ Ω_0(S′)` the following formula
(set `z = d(exp(Y) · t · exp(X))`):*

```text
(⋆)    int(w)(exp(Y) · t · exp(X)) = exp(z⁻¹ a_α(w)⁻¹ X) · t α*(z) · exp(z⁻¹ a_α(w) Y).
```

*Moreover, one has `d ∘ int(w) = d⁻¹`.*

<!-- label: III.XX.3.12 -->

Indeed, one has at once[^N.D.E-XX-30]

```text
int(w)(exp(Y) · t · exp(X)) = exp(a_α(w) Y) · t α*(α(t)⁻¹) · exp(a_α(w)⁻¹ X)
                            = exp(a_α(w) Y) · exp(α(t) a_α(w)⁻¹ X) · t α*(α(t)⁻¹).
```

By 2.1, this is a section of `Ω` if and only if `1 + α(t) X Y` is invertible, which proves
indeed the equality `Ω_0 = Ω_d`; applying then formula (F) of *loc. cit.*, one deduces by
an immediate calculation the announced formula (⋆). Finally, it follows from (⋆) that one
has

```text
(d ∘ int(w))(exp(Y) · t · exp(X)) = α(t α*(z))⁻¹ + z⁻² X Y = z⁻² (α(t)⁻¹ + X Y) = z⁻¹,
```

whence the last assertion.

*N.B.* One notes that the function `d` is independent of the choice of `w`.

[^N.D.E-XX-23]: N.D.E.: We have added the numbering 3.0, for later references.
[^N.D.E-XX-24]: N.D.E.: We have replaced `Q` by the more suggestive notation `N^×`.
[^N.D.E-XX-25]: N.D.E.: We have corrected the first formula of the original.
[^N.D.E-XX-26]: N.D.E.: The first equality follows from 1.5 (i) which, combined with the equality `α ∘ α* = 2`, gives the formulas

    ```text
    (†)   α*(z) exp(X) α*(z)⁻¹ = exp(z² X),    α*(z) exp(X⁻¹) α*(z)⁻¹ = exp(z⁻² X),
    ```

    the third equality follows from formula (F), and the fourth from (†), again. Finally, an analogous calculation shows that `w_α(X) α*(z⁻¹) = w_α(z X)`.
[^N.D.E-XX-27]: N.D.E.: The hypothesis `Centr_{G_s}(n α*_s) ≠ G_s` entails that `dim Centr_{G_s}(n α*_s) − dim T_s < 2`, but this difference is even, by *loc. cit.*
[^N.D.E-XX-28]: N.D.E.: that is, `a_{−α}(w)` and `a_α(w)` are paired, cf. 2.6.1.
[^N.D.E-XX-29]: N.D.E.: We have detailed what follows.
[^N.D.E-XX-30]: N.D.E.: We have corrected the original by swapping `a_α(w)` and `a_α(w)⁻¹`, and we have detailed the proof of the equality `d ∘ int(w) = d⁻¹`.

## 4. The isomorphism theorem

<!-- label: III.XX.4 -->

<!-- original page 71 -->

**Theorem 4.1.** *Let `S` be a scheme, `q ∈ ℤ`, `q > 0`, such that `x ↦ x^q` is an
endomorphism of `G_{a, S}`, `(G, T, α)` and `(G′, T′, α′)` two `S`-elementary systems. Let*

```text
h : (g_α)^{⊗q} → g′_{α′}    and    h^∨ : (g_{−α})^{⊗q} → g′_{−α′}
```

*be two isomorphisms contragredient to each other. Let `f_T : T → T′` be an `S`-group
morphism making the diagram*

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

*There exists a unique morphism of `S`-groups `f : G → G′` which extends `f_T` and satisfies*

```text
f(exp(X)) = exp(h(X^q))
```

*for every `X ∈ W(g_α)(S′)`, `S′ → S`. Moreover, this morphism also satisfies*

```text
f(exp(Y)) = exp(h^∨(Y^q))    and    f(w_α(Z)) = w_α(h(Z^q)),
```

*for every `S′ → S` and all `Y ∈ Γ(S′, g_{−α})`, `Z ∈ Γ(S′, g_α)^×`.*

<!-- label: III.XX.4.1 -->

If `f : G → G′` extends `f_T`, then `f ∘ α* = (α′*)^q`. If moreover `f` satisfies the
second condition, then it satisfies the two others as well by 3.10. It follows that `f` is
determined on `Ω` by the relation

```text
f(exp(Y) t exp(X)) = exp(h^∨(Y^q)) f_T(t) exp(h(X^q)).
```

Since `Ω` is schematically dense in `G`, this already proves the uniqueness of `f`. To
prove its existence, it suffices, by virtue of Exp. XVIII 2.3, to prove that the preceding
formula defines a "generically multiplicative" morphism from `Ω` to `G′`. Now, by 2.4, this
amounts to verifying that `α′ ∘ f = α^q`, which follows from the fact that `f` extends
`f_T`.

**Scholie 4.2.** *One can also interpret 4.1 as follows: consider the category `E` of
`S`-elementary systems and the category `D` of tuples*

```text
(G_{m, S}  ──α*──→  T  ──α──→  G_{m, S},  L),
```

*where `T` is a torus, `α` and `α*` are group morphisms such that `α ∘ α* = 2`, and `L` is
an invertible `O_S`-module (the reader will specify the morphisms of the two categories
under consideration). One defines a functor `E → D` by*

```text
(G, T, α) ↦ (G_{m, S}  ──α*──→  T  ──α──→  G_{m, S},  g_α).
```

*The preceding theorem says that this functor is fully faithful. It is in fact an
equivalence of categories, as one will see in the next number. One already has:*

<!-- label: III.XX.4.2 -->

**Corollary 4.3.** *If `q = 1` and if `f_T` is an isomorphism, then `f` is an isomorphism.*

<!-- label: III.XX.4.3 -->

**Corollary 4.4.** *If `q = 1` and if `f_T` is faithfully flat with kernel `Q` (cf.
Exp. IX 2.7), then `f` is faithfully flat (quasi-compact) with kernel `Q`, hence identifies
`G′` with `G/Q`.*

<!-- label: III.XX.4.4 -->

Indeed, if `f_T` is faithfully flat with kernel `Q`, then

```text
Q = Ker(f_T) ⊂ Ker(f_T ∘ α′) = Ker(α).
```

Introducing the `S`-elementary system `(G/Q, T/Q, α/Q)` of 2.13, one is reduced by 2.14 to
proving that `f/Q` induces an isomorphism of `G/Q` onto `G′`, which follows at once from
4.3.

## 5. Examples of elementary systems, applications

<!-- label: III.XX.5 -->

<!-- original page 73 -->

**5.1.** Let `S` be a scheme, `L` an invertible `O_S`-module. Consider the group `GL` over
`S` defined by

```text
GL(S′) = { ( a  b )  | a, d ∈ G_a(S′), b ∈ W(L)(S′), c ∈ W(L⁻¹)(S′), a d − b c ∈ G_m(S′) }
         ( c  d )
```

equipped with the usual matrix multiplication law. It is locally isomorphic to `GL_{2, S}`.
It is therefore an `S`-group scheme, affine and smooth over `S`, with connected fibers.

*Remark.* Let `L′` and `L″` be two invertible sheaves on `S`, such that
`L = L′ ⊗ L″⁻¹`.[^N.D.E-XX-31] Then one has an isomorphism of `S`-groups:

```text
GL  ──∼──→  GL(L′ ⊕ L″)
```

defined as follows: if `x` (resp. `y`) is a section of `L′` (resp. `L″`) on an open set
`V` of `S`, one has

```text
( a  b ) ( x )   ( a x + b y )
( c  d ) ( y ) = ( c x + d y ).
```

**5.2.** One will denote by `SL` the closed subgroup of `GL` defined by the relation
`a d − b c = 1`. It is also an `S`-group scheme, affine and smooth over `S`, with connected
fibers (isomorphic to `SL(L′ ⊕ L″)` by the preceding isomorphism).

Likewise, consider the morphism `G_{m, S} → GL` defined by `z ↦ (z 0 / 0 z)`. It is a
central monomorphism; by passage to the quotient, one deduces a group `PL`, smooth and
affine over `S`, with connected fibers (cf. Exp. VIII 5.7).

One can see that, by passage to the quotient from the isomorphism of the preceding remark,
`PL` is identified with the group of automorphisms of the projective bundle
`P(L′ ⊕ L″)` (cf. EGA, II 4.2.7). One will denote by `i` and `p` the canonical morphisms

<!-- original page 74 -->

```text
SL  ──i──→  GL  ──p──→  PL;
```

`i` is a closed immersion, `p` is faithfully flat and affine.

**5.3.** Consider the group morphisms

```text
t_G : G²_{m, S} → GL,    t_G(z, z′) = ( z   0 ),
                                       ( 0   z′ )
t_S : G_{m, S} → SL,     t_S(z) = ( z    0 ),
                                  ( 0   z⁻¹ )
t_P : G_{m, S} → PL,     t_P(z) = p(t_G(z, 1)).
```

These are group monomorphisms, which define in each group a (split) torus of relative
codimension 2. For every `s ∈ S`, let

```text
X ∈ Γ(s, L ⊗ s)^×;
```

then the section `( 0  X / −X⁻¹  0 )` of `GL_s` normalizes `t_G(G²_{m, s})` and does not
centralize it; one concludes from Exp. XIX 1.6 that `GL` is reductive, of semisimple
rank 1, with maximal torus `t_G(G²_{m, S})`.

One argues similarly for `SL` and `PL`, and one sees that `SL` (resp. `PL`) is reductive,
of semisimple rank 1, with maximal torus `t_S(G_{m, S})` (resp. `t_P(G_{m, S})`).

<!-- original page 74 -->

**5.4.** Reasoning as usual, one determines at once the Lie algebra of these various
groups and the adjoint action of the chosen maximal torus. Let us do it for `GL`; this is
immediate by Exp. II 4.8: `Lie(GL/S)` is the Lie algebra of the matrices below:

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

Denote `Lie(GL/S) = g`. Let `α_G : t_G(G²_{m, S}) → G_{m, S}` be the character defined by

```text
α_G(t_G(z, z′)) = z z′⁻¹.
```

One sees at once from the preceding relation that `α_G` is a root of `GL` with respect to
`t_G(G²_{m, S})` and that the morphism

```text
u : L → g    (resp. u⁻ : L⁻¹ → g)
```

defined by `u(X) = ( 0  X / 0  0 )` (resp. `u⁻(X) = ( 0  0 / X  0 )`) is an isomorphism of
`L` onto `g_{α_G}` (resp. of `L⁻¹` onto `g_{−α_G}`).

One has thus proved that `(G, t_G(G²_{m, S}), α_G)` is an `S`-elementary system.

Setting likewise

```text
α_S(t_S(z)) = z²,    α_P(t_P(z)) = z,
```

one proves that `(SL, t_S(G_{m, S}), α_S)` and `(PL, t_P(G_{m, S}), α_P)` are elementary
systems, and one defines isomorphisms of `L` (resp. `L⁻¹`) with the corresponding direct
summands of the Lie algebras of `SL` and `PL`.

**5.5.** Set `exp ( 0  X / 0  0 ) = ( 1  X / 0  1 )`. One has thus defined a morphism

```text
W(g_{α_G}) → GL
```

which induces on the Lie algebras the canonical morphism, hence is the unique morphism of
this type (1.5). Similarly, one sets `exp ( 0  0 / Y  0 ) = ( 1  0 / Y  1 )`. Carrying out
the explicit calculation of formula (F), one finds

```text
⟨ ( 0  X / 0  0 ), ( 0  0 / Y  0 ) ⟩ = X Y,    α*_G(z) = ( z   0  ) = t_G(z, z⁻¹).
                                                          ( 0   z⁻¹)
```

[^N.D.E-XX-32]

<!-- original page 76 -->

The open set `N^× = N^×_G` (defined before 3.1) is:

```text
N^×_G(S′) = { ( 0  P ) | P ∈ W(g_α)^×(S′), Q ∈ W(g_{−α})^×(S′) },
             ( Q  0 )
```

the morphism `w_{α_G}` (cf. 3.1 (iv)) is given, for every `X ∈ W(g_α)^×(S′)`, by

```text
w_{α_G}(X) = (  0     X );
             ( −X⁻¹  0 )
```

the morphism `a_{α_G}` (cf. 3.5) is given by:

```text
if w = ( 0  P ) ∈ N^×_G(S′), then a_{α_G}(w) = P Q⁻¹ ∈ W((g_α)^{⊗2})^×(S′),
       ( Q  0 )
```

that is, for every `Y ∈ W(g_{−α})^×(S′)`, one has `a_{α_G}(w)(Y) = P Q⁻¹ Y ∈ W(g_α)^×(S′)`.

**5.6.** We leave the reader the task of carrying out the same computations in `SL` and
`PL`. One finds the same duality formula and the coroots

```text
α*_S(z) = t_S(z),    α*_P(z) = t_P(z²).
```

Denote by `p_T` the morphism induced by `p : GL → PL` on `t_S(G_{m, S})`, i.e.

```text
p_T(t_S(z)) = t_P(z²).
```

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

One recognizes in the central part the commutative diagram of 4.1[^N.D.E-XX-34] relative to
the canonical morphism `p ∘ i : SL → PL`, which induces a morphism of the preceding
`S`-elementary systems.

<!-- original page 76 -->

**5.7.** Let now `(G, T, α)` be any `S`-elementary system. Consider the commutative
diagram:

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

**Proposition 5.8.** *Let `S` be a scheme, `(G, T, α)` an `S`-elementary system. Set
`L = g_α` (and hence `L⁻¹ = g_{−α}`).*

*(i) There exists a unique group morphism `f : SL → G` satisfying the following equivalent
conditions:*

```text
(a)   f( z   0  ) = α*(z),    f( 1  X ) = exp(X);
     ( 0   z⁻¹)              ( 0  1 )

(b)   f( 1  X ) = exp(X),     f( 1  0 ) = exp(Y);
     ( 0  1 )                ( Y  1 )

(c)   f( 1  X ) = exp(X),     f(  0     X ) = w_α(X).
     ( 0  1 )                ( −X⁻¹  0 )
```

*(ii) There exists a unique group morphism `g : G → PL` satisfying*

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

*The morphism `g` is faithfully flat quasi-compact with kernel `Ker(α) = Centr(G)`, and
`g ∘ f` is the canonical morphism `SL → PL`.*

<!-- label: III.XX.5.8 -->

Note that conditions (b) of (i) give an explicit description of the duality between `g_α`
and `g_{−α}`.

**Corollary 5.9.** *Let `(G, T, α)` be an `S`-elementary system. The subgroups `T · U_α`,
`T · U_{−α}`, `U_α` and `U_{−α}` are closed.*

<!-- label: III.XX.5.9 -->

Since `U_α` is a closed subgroup scheme of `T · U_α`, it suffices to make the verification
for the latter. By Noether's theorem (Exp. IV 5.3.1 and 6.4.1), it suffices to prove that
`(T · U_α)/Ker(α)` is a closed subgroup of `G/Ker(α)`. By virtue of 5.8, one is therefore
reduced to proving that the subgroup of `PL` (or of `GL`, which amounts to the same by a
new application of Noether's theorem) defined by `c = 0` is closed, which is trivial.

Consequently, the morphisms `exp` of Theorem 1.5 (i) are closed immersions.

*N.B.* The corollary also follows from the fact that `T · U_α` and `T · U_{−α}` are "Borel
subgroups" of `G` (cf. Exp. XII 7.10).

**5.10.** Let `L` be an invertible `O_S`-module and

```text
G_{m, S}  ──α*──→  T  ──α──→  G_{m, S}
```

a diagram of groups[^N.D.E-XX-35] such that `α ∘ α* = 2`. Let `R` be the maximal torus of
`Ker(α)` and `K = α*⁻¹(R)`. Then `K` is a subgroup of multiplicative type of `G_{m, S}`;
by virtue of `α ∘ α* = 2`, it is even a subgroup of `μ_{2, S}`. In particular the morphism

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

Consider the group `G = (R × SL)/K` obtained by passage to the quotient. It is an affine
and smooth group over `S`, with connected fibers. It is immediate that the sequence

```text
1 → K → R × t_S(G_{m, S})  ──u──→  T → 1
```

where `u(x, t_S(z)) = x α*(z)` is exact. The image of `R × t_S(G_{m, S})` in `G` is
therefore a torus `T′` isomorphic to `T`. One then shows without difficulty that if `α′`
is the character of `T′` deduced from `α` by the preceding isomorphism, `(G, T′, α′)` is
an `S`-elementary system, that `g′_{α′}` is isomorphic to `L`, and that `α′*` is obtained
from `α*` by the isomorphism `T ─∼→ T′`. One has therefore constructed an `S`-elementary
system `(G, T′, α′)` such that the corresponding object

<!-- original page 80 -->

```text
(G_{m, S}  ──α′*──→  T′  ──α′──→  G_{m, S},  g′_{α′})
```

of the category `D` defined in 4.2 is isomorphic to

```text
(G_{m, S}  ──α*──→  T  ──α──→  G_{m, S},  L).
```

One has therefore proved the

**Theorem 5.11.** *In the notations of 4.2, the functor*

```text
(G, T, α) ↦ (G_{m, S}  ──α*──→  T  ──α──→  G_{m, S},  g_α)
```

*is an equivalence of categories between `E` and `D`.*

<!-- label: III.XX.5.11 -->

[^N.D.E-XX-31]: N.D.E.: We have corrected `L″ ⊗ L′⁻¹` to `L′ ⊗ L″⁻¹` and we have detailed the sentence that follows.
[^N.D.E-XX-32]: N.D.E.: We have detailed what follows.
[^N.D.E-XX-33]: N.D.E.: where `t_S` and `t_P` are isomorphisms.
[^N.D.E-XX-34]: N.D.E.: with `q = 1`.
[^N.D.E-XX-35]: N.D.E.: `T` being a torus.

## 6. Generators and relations for an elementary system

<!-- label: III.XX.6 -->

<!-- original page 80 -->

**6.1.** Let `S` be a scheme, `(G, T, α)` an `S`-elementary system. Let `X ∈ W(g_α)^×(S)`
and `u = exp(X)`; one has seen in 3.8 that the element `w = w_α(X)` satisfies in particular
the relation

```text
(w u)³ = e.
```

[^N.D.E-XX-36]

One denotes by `s_α` the automorphism of `T` induced by `int(w)`; according to Theorem
3.1 (iii), for every `S′ → S` and `t ∈ T(S′)`, one has

```text
s_α(t) = int(w)(t) = t · α*(α(t)⁻¹).
```

**Theorem 6.2.** *Let `H` be an `S`-sheaf of groups for (fppf). Let*

```text
f_T : T → H,    f_α : U_α → H
```

*be group morphisms and `h ∈ H(S)` a section of `H`. For there to exist a (necessarily
unique) group morphism*

```text
f : G → H
```

*extending `f_T` and `f_α` and satisfying `f(w) = h`, it is necessary and sufficient that
the following conditions be satisfied:*

*(i) For every `S′ → S`, every `t ∈ T(S′)` and every `x ∈ U_α(S′)`, one has*

```text
(1)   f_T(t) f_α(x) f_T(t)⁻¹ = f_α(t x t⁻¹) = f_α(x^{α(t)}).
```

*(in other words, `f_T` and `f_α` extend to a group morphism from the semidirect product
`T · U_α` into `H`).*

*(ii) For every `S′ → S` and every `t ∈ T(S′)`, one has*

```text
(2)   h f_T(t) h⁻¹ = f_T(s_α(t)) = f_T(t · α*(α(t)⁻¹)).
```

<!-- original page 81 -->

*(iii) One has the two relations in `H(S)`:*

```text
(3)   h² = f_T(α*(−1)),
(4)   (h f_α(u))³ = e.
```

<!-- label: III.XX.6.2 -->

*Proof.* Denote additively `U_α` and `U_{−α}` and multiplicatively their vector structure.
If `f` satisfies the conditions of the statement, one necessarily has for every
`y ∈ U_{−α}(S′)`,

```text
f(y) = f(w⁻¹ w y w⁻¹ w) = h f_α(w⁻¹ y w) h⁻¹.
```

Let then `f_{−α} : U_{−α} → H` be the morphism defined by

```text
(∗_1)    f_{−α}(y) = h f_α(w⁻¹ y w) h⁻¹.
```

It is a group morphism. On the other hand, `f` is determined on the big cell `Ω` by

```text
f(y t x) = f_{−α}(y) f_T(t) f_α(x).
```

This shows the uniqueness of `f`; since the conditions of the statement are manifestly
necessary, let us show that they are sufficient.

One has by (4)

```text
h f_α(u) h⁻¹ h² = f_α(−u) h⁻¹ f_α(−u).
```

Now, by (3) and (1), `h² = f_T(α*(−1))` commutes with `f_α(−u)`, which gives

```text
h f_α(u) h⁻¹ = f_α(−u) h f_α(−u).
```

But, by definition, `h f_α(u) h⁻¹ = f_{−α}(w u w⁻¹)`; by 3.7, since `u = exp(X)` and
`w = w_α(X)`, one has

<!-- original page 82 -->

```text
(∗_2)    w u w⁻¹ = −ũ,
```

where `ũ` denotes the element paired with `u`. One obtains therefore:

```text
(∗_3)    f_{−α}(−ũ) = f_α(−u) h f_α(−u).
```

Let now `t` be a section of `T` over a variable `S′ → S`. Apply `int(f_T(t))` to the
preceding formula. One obtains on the left-hand side[^N.D.E-XX-37]

```text
f_T(t) f_{−α}(−ũ) f_T(t)⁻¹ = f_T(t) h f_α(u) h⁻¹ f_T(t)⁻¹
                           = h (h⁻¹ f_T(t) h) f_α(u) (h⁻¹ f_T(t)⁻¹ h) h⁻¹
                           = h f_T(s_α(t)) f_α(u) f_T(s_α(t))⁻¹ h⁻¹ = h f_α(α(s_α(t)) u) h⁻¹
```

by (2) and (1); then since `s_α(t) = t · α*(α(t)⁻¹)` and `α ∘ α* = 2`, this equals

```text
h f_α(α(t)⁻¹ u) h⁻¹.
```

Finally, by (∗_1) and (∗_2) one has

```text
h f_α(α(t)⁻¹ u) h⁻¹ = f_{−α}(α(t)⁻¹ w u w⁻¹) = f_{−α}(−α(t)⁻¹ ũ).
```

The right-hand side of (∗_3) gives

```text
f_α(−α(t) u) · f_T(t) h f_T(t)⁻¹ h⁻¹ · h · f_α(−α(t) u)
```

and since `h f_T(t)⁻¹ h⁻¹ = f_T(s_α(t⁻¹)) = f_T(t · α*(α(t)))`, this equals

```text
f_α(−α(t) u) · f_T(α*(α(t))) · h · f_α(−α(t) u).
```

Comparing the two expressions obtained, one obtains

```text
f_{−α}(−α(t)⁻¹ ũ) = f_α(−α(t) u) · f_T(α*(α(t))) · h · f_α(−α(t) u).
```

Since `α : T → G_{m, S}` is faithfully flat and `H` is a separated presheaf, one can
replace `−α(t)⁻¹` by an arbitrary section of `G_{m, S}`, and one obtains the

**Lemma 6.2.1.** *For every `z ∈ G_m(S′)`, `S′ → S`, one has*

```text
f_{−α}(z ũ) = f_α(z⁻¹ u) · f_T(α*(−z⁻¹)) · h · f_α(z⁻¹ u).
```

<!-- label: III.XX.6.2.1 -->

<!-- original page 83 -->

Let now `x, y ∈ G_a(S′)`, `S′ → S`; suppose `y` and `(1 + x y)` invertible. Applying the
lemma first to `z = y`, one obtains[^N.D.E-XX-38]

```text
f_α(x u) f_{−α}(y ũ) = f_α((x + y⁻¹) u) · f_T(α*(−y⁻¹)) · h · f_α(y⁻¹ u).
```

Now `x + y⁻¹ = y⁻¹(1 + x y)`. Applying the lemma to `z = y / (1 + x y)`, one finds

```text
f_α((x + y⁻¹) u) = f_{−α}( y/(1 + x y) · ũ ) f_α(−(x + y⁻¹) u) · h · f_T(α*(−y / (1 + x y))).
```

Substituting in the preceding equality, one obtains

```text
f_α(x u) f_{−α}(y ũ) = f_{−α}( y / (1 + x y) · ũ ) f_α(−(x + y⁻¹) u) · h⁻¹ · f_T(α*(1 + x y)⁻¹) · h · f_α(y⁻¹ u).
```

Since `h⁻¹ f_T(t) h = f_T(s_α(t))` by (2) (note that `s²_α = id`) and since
`s_α ∘ α* = −α*` (cf. 6.2.1), this equals

```text
f_{−α}( y / (1 + x y) · ũ ) f_α(−(x + y⁻¹) u) · f_T(α*(1 + x y)) · f_α(y⁻¹ u).
```

Finally, since for all `x′ ∈ U_α(S′)` and `z ∈ G_m(S′)` one has

```text
f_α(x′) f_T(α*(z)) = f_T(α*(z)) f_α(z⁻² x′),
```

one obtains

```text
f_α(x u) f_{−α}(y ũ) = f_{−α}( y / (1 + x y) · ũ ) · f_T(α*(1 + x y)) · f_α( −y⁻¹ (1 + x y)⁻¹ / (1 + x y)² + y⁻¹ · u )
                     = f_{−α}( y / (1 + x y) · ũ ) · f_T(α*(1 + x y)) · f_α( x / (1 + x y) · u ).
```

One has thus proved:

**Lemma 6.2.2.** *Let `S′ → S`. If `a ∈ U_α(S′)`, `b ∈ U^×_{−α}(S′)`, and
`1 + a b ∈ G_m(S′)`, one has*

```text
f_α(a) f_{−α}(b) = f_{−α}( b / (1 + a b) ) f_T(α*(1 + a b)) f_α( a / (1 + a b) ).
```

<!-- label: III.XX.6.2.2 -->

<!-- original page 84 -->

By schematic density, this formula remains valid when `b ∈ U_{−α}(S′)`, `1 + a b` being
always invertible. Consider then the morphism

```text
f : Ω → H
```

defined by `f(y t x) = f_{−α}(y) f_T(t) f_α(x)`.

It follows at once from 6.2.2, from condition 6.2 (i), and from formula (F′) of 2.4 that
if `g, g′ ∈ Ω(S′)` and `g g′ ∈ Ω(S′)`, one has `f(g g′) = f(g) f(g′)`. By Exp. XVIII 2.3 (iii)
and 2.4[^N.D.E-XX-39], there therefore exists a group morphism `G → H` extending `f`.
Denote it also by `f`; it answers the question; it suffices to prove, indeed, that
`f(w_α) = h`. Now `w_α = u · (−ũ) · u`, whence, by (∗_3):[^N.D.E-XX-40]

```text
f(w_α) = f_α(u) f_{−α}(−ũ) f_α(u) = h.
```

**Remark 6.3.** *We shall complete these results in Exp. XXIII 3.5.*

<!-- label: III.XX.6.3 -->

[^N.D.E-XX-36]: N.D.E.: We have added the sentence that follows.
[^N.D.E-XX-37]: N.D.E.: We have corrected what follows.
[^N.D.E-XX-38]: N.D.E.: We have detailed the calculations that follow.
[^N.D.E-XX-39]: N.D.E.: Note that each geometric fiber of `G` is connected, for example by 1.1.
[^N.D.E-XX-40]: N.D.E.: We have simplified the original by invoking (∗_3).

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

