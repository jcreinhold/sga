# Exposé VII_A. Infinitesimal study: differential operators and restricted `p`-Lie algebras

<!-- label: III.VII_A -->

*by P. Gabriel*

<!-- original page 412 -->

In Exposé II we restricted ourselves to the study of first-order differential invariants and did not address certain
phenomena specific to characteristic `p > 0` or to characteristic 0. Our object in part A of this Exposé is to fill in
this gap.

Moreover, the infinitesimal study of arbitrary order of a group scheme is related to that of the associated formal
group; the object of the second part of this Exposé is to present the first definitions and properties concerning formal
groups.

## A) Differential operators and restricted `p`-Lie algebras[^VII_A-A-1]

[^VII_A-A-1]: Part A of the present Exposé had not been treated seriously in the oral seminars.

## 1. Differential operators

<!-- label: III.VII_A.1 -->

In this section, as well as in sections 2 and 3, `S` denotes a fixed scheme and the products considered are cartesian
products in the category of `S`-schemes.[^N.D.E-VII_A-1] If `X` is an `S`-scheme, we write `p_{X/S}`, `p_X` or simply
`p` for the structural morphism of `X` into `S`.

[^N.D.E-VII_A-1]: In particular, if `X` and `Y` are two `S`-schemes, `X ×_S Y` is denoted simply `X × Y`. Moreover, let
us point out that for the content of sections 1 and 2, one may also consult [DG70], § II.4, nos 5–6; see also [Ja03],
§ I.7.

### 1.1.

<!-- label: III.VII_A.1.1 -->

Let `u : Y → X` be a morphism of `S`-schemes and endow the direct image `u_*(O_Y)` of the structure sheaf of `Y` with
the `O_X`-module structure induced by `u`. The sheaf `H = Hom_{p_X^{-1}(O_S)}(O_X, u_*(O_Y))` of `p_X^{-1}(O_S)`-module
homomorphisms <!-- original page 413 -->
from `O_X` into `u_*(O_Y)` is therefore naturally equipped with a structure of `O_X`-bimodule: if `U` is an open of `X`,
`f` and `d` sections of `O_X` and `H` on `U`, then `fd` and `df` are respectively the morphisms `g ↦ f d(g)` and
`g ↦ d(fg)` from `O_X` into `u_*(O_Y)`. We shall henceforth write `(ad f)(d)` in place of `fd − df`.

**Definition 1.1.1.** *An `S`-deviation of order `⩽ n` is by definition a pair `D = (u, d)` consisting of a morphism of
`S`-schemes `u : Y → X` and a morphism of `p_X^{-1}(O_S)`-modules `d : O_X → u_*(O_Y)` such that, for every open `U` of
`X` and every sequence of `n + 1` sections `f₀, …, f_n ∈ O_X(U)`, one has in `Hom_{p_U^{-1}(O_S)}(O_U, u_*(O_Y)|_U)` the
equality:*

<!-- label: III.VII_A.1.1.1 -->

```text
(∗_n)                    (ad f₀)(ad f₁) ··· (ad f_n)(d) = 0.
```

[^N.D.E-VII_A-2]

In this case, we shall also say that `d` is an `S`-deviation of `u` of order `⩽ n`. In particular, an `S`-deviation of
`u` of order `⩽ 0` is a morphism of `O_X`-modules from `O_X` into `u_*(O_Y)`, i.e., an element of `Γ(Y, O_Y)`.

[^N.D.E-VII_A-2]: One sees easily that this is equivalent to saying that, for every `x ∈ X` and `f₀, …, f_n, g ∈ O_{X,x}`,
one has `(ad f₀)(ad f₁) ··· (ad f_n)(d_x)(g) = 0`. On the other hand, recall that the adjunction isomorphism

    ```text
    θ : Hom_{p_X^{-1}(O_S)}(O_X, u_*(O_Y)) ⥲ Hom_{p_Y^{-1}(O_S)}(u^{-1}(O_X), O_Y)
    ```

    associates with every morphism of `p_X^{-1}(O_S)`-modules `d : O_X → u_*(O_Y)` the morphism `d' = ε ∘ u^{-1}(d)`,
    where `ε` is the canonical morphism `u^{-1} u_*(O_Y) → O_Y`. Conversely, for every `p_Y^{-1}(O_S)`-morphism
    `d' : u^{-1}(O_X) → O_Y`, one has `θ^{-1}(d') = u_*(d') ∘ η`, where `η` is the canonical morphism
    `O_X → u_* u^{-1}(O_X)`. It follows that `d` satisfies `(∗_n)` if and only if `d'` satisfies:

    ```text
    (∗'_n)                  (ad f₀) ··· (ad f_n)(d')(g) = 0
    ```

    for every open `V` of `Y` and `f₀, …, f_n, g ∈ u^{-1}(O_X)(V)`.

**Definition 1.1.2.** *A morphism of `p_X^{-1}(O_S)`-modules `d : O_X → u_*(O_Y)` is an `S`-deviation of `u` if, for
every point `y` of `Y`, there exist an open neighborhood `U` of `u(y)` in `X` and an open neighborhood `V` of `y` in `Y`
satisfying the following conditions:*

   *a) `u(V) ⊂ U`;*

   *b) if `v : V → U` is the morphism induced by `u`, there is an integer `n` such that the morphism `O_U → v_*(O_V)`
   induced by `d` is an `S`-deviation of `v` of order `⩽ n`.*[^N.D.E-VII_A-3]

[^N.D.E-VII_A-3]: If `X` and `u` are quasi-compact, every `S`-deviation of `u` is therefore of order `⩽ n`, for some
integer `n`.

<!-- label: III.VII_A.1.1.2 -->

If `d` is an `S`-deviation of `u`, we also say that the pair `D = (u, d)` is an `S`-deviation and it will happen that we
write `Y ─D→ X` or `Y ─d→ X` (over `u`).

When `d` is the algebra homomorphism `u^♮ : O_X → u_*(O_Y)` corresponding to the morphism `u : Y → X`, we shall also
write `u` in place of `D`.

**Remarks 1.1.3.**[^N.D.E-VII_A-4] Let `Dév(u)` (resp. `Dév_{⩽n}(u)`) be the set of `S`-deviations of `u` (resp.
`S`-deviations of `u` of order `⩽ n`). It is equipped with a natural structure of `O_Y(Y)`-module: if `λ ∈ O_Y(Y)`,
`λd` is the deviation sending `f` to `λ d(f)`, for every section `f` of `O_X` on an open `U`.

[^N.D.E-VII_A-4]: These remarks have been added, as they will be useful in 1.3, 1.4 and 2.1.

<!-- label: III.VII_A.1.1.3 -->

For every open `V` of `Y`, set `𝒟év(u)(V) = Dév(u|_V)`, i.e., `𝒟év(u)(V)` is the set of

```text
d_V ∈ Hom_{p_X^{-1}(O_S)}(O_X, (u|_V)_*(O_V)) ≃ Hom_{p_Y^{-1}(O_S)}((u|_V)^{-1} O_X, O_V)
                                              ≃ Hom_{p_Y^{-1}(O_S)}(u^{-1} O_X, O_Y)(V)
```

<!-- original page 444 -->

such that, for every open `U` of `X`, the map `d_V(U) : O_X(U) → O_Y(u^{-1}(U) ∩ V)` satisfies `(∗_n)`. This defines a
presheaf of `O_Y`-modules on `Y`, and one sees easily that it is a sheaf (more precisely, a subsheaf of
`Hom_{p_Y^{-1}(O_S)}(u^{-1} O_X, O_Y)`).

### 1.2.

<!-- label: III.VII_A.1.2 -->

Consider now two `S`-deviations `D = (u, d)` and `E = (v, e)`:

```text
Z ─v,e→ Y ─u,d→ X.
```

When `U` ranges over the opens of `X`, the composed maps

```text
Γ(U, O_X) ─d(U)→ Γ(u^{-1} U, O_Y) ─e(u^{-1} U)→ Γ(v^{-1} u^{-1} U, O_Z)
```

define an `S`-deviation of `uv` which we shall denote `de`; <!-- original page 414 --> when `d` is of order `⩽ m` and
`e` of order `⩽ n`, `de` is of order `⩽ m + n`. We shall also write

```text
(†)                              D ∘ E = (uv, de)
```

[^N.D.E-VII_A-5]

and we shall say that `D ∘ E` or `DE` is the *composed `S`-deviation*. When `d = u^♮` (i.e., `D = u` with the convention
of 1.1), one also says that `DE` is the *image of `E` by `u`*.

[^N.D.E-VII_A-5]: One will note that with this notation, `de` denotes the composition "`d` followed by `e`".

The map `(D, E) ↦ D ∘ E` we have just defined will henceforth allow us to speak of the *category of `S`-deviations*,
whose objects are the `S`-schemes and whose morphisms are the `S`-deviations.[^N.D.E-VII_A-6]

[^N.D.E-VII_A-6]: Often, one considers only the `S`-deviations of the morphism `id_X`, which form the algebra of
`S`-differential operators of `X`, cf. 1.4 below. However, the more general framework of `S`-deviations provides a
convenient "functorial" language for proving statements such as: "if `G` is an `S`-group, the algebra of `S`-differential
operators on `G` invariant under left translation is isomorphic to the algebra of `S`-deviations of the unit section
`ε : S → G`, cf. 2.1 and 2.4 below."

**Definition 1.2.0.**[^N.D.E-VII_A-7] *Let `w : Z → X` be an `S`-morphism. An `S`-derivation of `w`, or `S`-derivation
of `O_X` into `w_*(O_Z)`, is a morphism of `p^{-1}(O_S)`-modules `d : O_X → w_*(O_Z)` such that, for every open `U` of
`X` and `f, g ∈ O_X(U)`,*

<!-- label: III.VII_A.1.2.0 -->

```text
d(fg) = w^♮(f) d(g) + w^♮(g) d(f).
```

*Then `d` is a deviation of `w` of order `⩽ 1` which vanishes on the unit section of `O_X`. We denote by `Dér_S(w)` the
set of `S`-derivations of `w`; it is an `O(Z)`-module.*

[^N.D.E-VII_A-7]: This paragraph has been expanded, with the number 1.2.0 (resp. 1.2.1) being assigned to this definition
(resp. to the lemma which follows).

With the notations of 1.2, take `Y` equal to `I_Z = Spec O_Z[t]`, where `t² = 0`, and `v` equal to the zero section
`τ : Z → I_Z`, defined by the morphism of `O_Z`-algebras `O_Z[t] → O_Z` sending `t` to `0`, and take `e` equal to the
morphism of `O_Z`-modules `σ : O_Z[t] → O_Z` defined by `σ(1) = 0` and `σ(t) = 1`,[^N.D.E-VII_A-8] which it is convenient
to denote `∂_t`.

[^N.D.E-VII_A-8]: The following has been added, i.e. the notation `∂_t` has been introduced.

If `u : I_Z → X` is a morphism satisfying `w = u ∘ τ`, then `σ ∘ u^♮` is an `S`-derivation of `O_X` into `w_*(O_Z)`.
Conversely, to every `S`-derivation `d` we associate the morphism `u : I_Z → X` such that `u = w` on the underlying
spaces, and

```text
u^♮(f) = w^♮(f) + d(f) t,
```

<!-- original page 446 -->

for every section `f` of `O_X` on an open `U`. One thus obtains:

**Lemma 1.2.1.** *Let `E = (τ, ∂_t)` be the deviation of `τ : Z → I_Z` defined above. For every `S`-morphism
`w : Z → X`, the map `u ↦ u ∘ E` is a bijection between the `S`-morphisms `u : I_Z → X` such that `u ∘ τ = w`, and the
`S`-derivations of `w`.*

<!-- label: III.VII_A.1.2.1 -->

### 1.2.2.

<!-- label: III.VII_A.1.2.2 -->

Let `d` be an `S`-deviation of `u : Y → X`. On the one hand, `d` is obviously an `S'`-deviation of `u` for every
morphism `s : S → S'`.

On the other hand, let `t : T → S` be a morphism with target `S`, and let `u_T : Y_T → X_T` be the morphism deduced
from `u` by base change, and `t_Y : Y_T → Y` and `t_X : X_T → X` the canonical projections. Then there exists one and
only one `T`-deviation of `u_T`, which we shall denote `d_T` or `d × T`, satisfying the equality `t_X d_T = d t_Y`, in
the sense of `(†)` above, i.e., for every open `U` of `X`, one has a commutative diagram:[^N.D.E-VII_A-9]

```text
                 t_X^♮
   O(U)  ─────────────────→  O(U × T)

  d(U)                              d_T(U × T)

                 t_Y^♮
   O(u^{-1} U)  ────────→  O(u^{-1} U × T).
```

[^N.D.E-VII_A-9]: Explicitly, if `V` is an affine open of `S` and `U` (resp. `U'`) an affine open of `X` (resp. `T`)
above `V`, so that `O_{X × T}(U × U') = O_X(U) ⊗_{O_S(V)} O_T(U')`, then `d_T(U × U')` is the composition:

    ```text
    O_X(U) ⊗_{O_S(V)} O_T(U') ──d(U) ⊗ id→ O_Y(u^{-1} U) ⊗_{O_S(V)} O_T(U') ──→ O_{Y × T}(u^{-1} U × U').
    ```

    The author left to the reader the verification that `d_T` is well-defined, and the editors do the same.

If one sets `D = (u, d)`, one will also write `D_T = (u_T, d_T)` and we shall say that `d_T` and `D_T` are deduced from
`d` and `D` by base change.

### 1.2.3.

<!-- label: III.VII_A.1.2.3 -->
<!-- original page 415 -->

For example, let `u : Y → X` and `v : Z → T` be two `S`-morphisms, `d` and `e` `S`-deviations of `u` and `v`. One has a
commutative diagram

```text
            u_T
X × T  ←─────────  Y × T
  ↑                  ↑
v_X │  u×v        v_Y │
  │                  │
            u_Z
X × Z  ←─────────  Y × Z
```

and we shall denote by `d × e` (the *product* of `d` and `e`) the `S`-deviation of `u × v` equal to `d_T e_Y = e_X d_Z`
(with the convention `(†)` above), i.e., for every open `U` of `X × T`, if we denote
<!-- original page 447 --> by `W` the open `v_Y^{-1} u_T^{-1} U = u_Z^{-1} v_X^{-1} U`, one has a commutative diagram:

```text
                       d_T(U)
       O(U)  ──────────────────→  O(u_T^{-1} U)
         ╲                              ↑
   e_X(U) ╲    (d × e)(U)               │ e_Y(u_T^{-1} U)
           ╲                            │
                d_Z(v_X^{-1} U)
       O(v_X^{-1} U)  ────────────→  O(W).
```

If one sets `D = (u, d)` and `E = (v, e)`, we shall also write `D × E = (u × v, d × e)`.

### 1.3.

<!-- label: III.VII_A.1.3 -->

[^N.D.E-VII_A-10] Let `u : Y → X` be a morphism of `S`-schemes. Recall that the adjunction isomorphism

```text
Hom_{p_X^{-1}(O_S)}(O_X, u_*(O_Y)) ⥲ Hom_{p_Y^{-1}(O_S)}(u^{-1}(O_X), O_Y)
```

associates with every morphism of `p^{-1}(O_S)`-modules `d : O_X → u_*(O_Y)` the morphism `d' = ε ∘ u^{-1}(d)`, where
`ε` is the canonical morphism `u^{-1} u_*(O_Y) → O_Y`.

[^N.D.E-VII_A-10]: This paragraph has been expanded with respect to the original; see also N.D.E. (2) in 1.1.1.

Let us write `J_u` (resp. `I_u`) for the kernel of the algebra homomorphism `u^♮ : O_X → u_*(O_Y)` (resp.
`u^{♮'} : u^{-1}(O_X) → O_Y`), and let `d : O_X → u_*(O_Y)` be a morphism of `p^{-1}(O_S)`-modules. If `U` is an open
of `X` and `f₀, …, f_n, g ∈ O_X(U)`, one sees easily by induction on `n` that the condition `(∗_n)` is equivalent to
the following equality (cf. EGA IV₄, 16.8.8.2):

<!-- label: III.VII_A.1.3.1 -->

```text
(∗∗_n)                     0 = ∑_{I ⊂ ⟦0,n⟧} (−1)^{|I|} u^♮(f_{⟦0,n⟧ − I}) d(f_I g),
```

where `f_I` denotes the product of the `f_i`, for `i ∈ I`. It follows that if `d` satisfies `(∗_n)`, then `d` vanishes on
the ideal `J_u^{n+1}`.

Suppose now `Y` equal to `S`; then `u : S → X` is a section of `p : X → S`, hence is an immersion
(cf. EGA I, 5.3.13). Then, on the one hand, `ε : u^{-1} u_* O_S → O_S` is an isomorphism, so that
`u^{-1}(J_u) = I_u`. On the other hand, one has an isomorphism:

```text
(⋆)                         u^{-1}(O_X) ≃ O_S ⊕ I_u.
```

Suppose that `d` vanishes on `J_u^{n+1}`. Then `d' = ε ∘ u^{-1}(d)` vanishes on `I_u^{n+1}` and hence `d'` satisfies the
analogues `(∗∗'_n)` and `(∗'_n)` of `(∗∗_n)` and `(∗_n)`, when `f₀, …, f_n ∈ I_u(u^{-1}(U))`. Moreover, since
`(ad a)(φ) = 0` for every `a ∈ O_S(u^{-1}(U))` and every morphism of `O_{u^{-1}(U)}`-modules
`φ : u^{-1}(O_U) → O_{u^{-1}(U)}`, one deduces from `(⋆)` that `d'` satisfies the analogue `(∗'_n)` of `(∗_n)`. It follows
that `d` satisfies `(∗_n)`. Consequently, one has obtained:

**Lemma.** *If `u : S → X` is a section of `p : X → S`, then `d` is an `S`-deviation of `u` of order `⩽ n` if and only
if `d'` vanishes on `I_u^{n+1}`.*

This interpretation may be generalized as follows. Let `u : Y → X` be an arbitrary `S`-morphism and `Γ_u` the graph of
`u`, i.e., the morphism `Y → Y × X` <!-- original page 448 --> with components `id_Y` and `u`. For every `S`-deviation
`d` of `u` of order `⩽ n`, one obtains by composition

```text
Y ──diag.→ Y × Y ──d_Y→ Y × X (over u_Y)
```

a `Y`-deviation of `Γ_u` of order `⩽ n` which we shall denote `Γ_d` (the graph of `d`).

Conversely, to every `Y`-deviation `e` of `Γ_u` one associates the composed `S`-deviation `e_X = pr₂ ∘ e`:

```text
Y ──e→ Y × X ──pr₂→ X (over Γ_u).
```

One sees at once that `(Γ_d)_X = d`, and the equality `Γ_{e_X} = e` follows from the fact that `e` is `O_Y`-
linear.[^N.D.E-VII_A-11] One thus obtains an isomorphism of `O_Y(Y)`-modules:

```text
{ S-deviations of u of order ⩽ n }  ⥲  { Y-deviations of Γ_u of order ⩽ n }
                                 d ↦ Γ_d.
```

Moreover, one sees easily that `d` is an `S`-derivation of `u` if and only if `Γ_d` is a `Y`-derivation of `Γ_u`.

[^N.D.E-VII_A-11]: If `λ, f` are local sections of `O_Y` and `O_X`, one has `(Γ_{e_X})(λ ⊗ f) = λ · e(1 ⊗ g)`, and this
equals `e(λ ⊗ g)` since `e` is `O_Y`-linear.

<!-- original page 416 -->

Let us call `I_{Γ_u}` the kernel of the algebra homomorphism `(Γ_u)^{-1}(O_{Y × X}) → O_Y` corresponding to `Γ_u`.
Taking into account the preceding lemma, one has obtained:

**Proposition.** *Let `u : Y → X` be an `S`-morphism and `Γ_u : Y → Y × X` its graph. The `S`-deviations of `u` of order
`⩽ n` are identified with the `Y`-deviations of `Γ_u` of order `⩽ n`, which are in bijection with*

```text
Hom_{O_Y}((Γ_u)^{-1}(O_{Y × X}) / I_{Γ_u}^{n+1}, O_Y).
```

### 1.3.1.

<!-- label: III.VII_A.1.3.1 -->

[^N.D.E-VII_A-12] Let us return to the case where `u : S → X` is a section of `p : X → S`. Then the homomorphism
`φ : u^{-1}(O_X) → O_S` admits a section, which we shall denote simply `g ↦ g · 1`, so that, with the notations of 1.3,
one has an isomorphism of `O_S`-modules:

```text
(⋆)                     u^{-1}(O_X) ≃ O_S ⊕ I_u,
```

and for every section `f` of `u^{-1}(O_X)`, `f − φ(f) · 1` is a section of `I_u`.

[^N.D.E-VII_A-12]: This paragraph has been added.

Let `d` be an `S`-deviation of `u` of order `⩽ 1`, and `d'` the `O_S`-morphism `u^{-1}(O_X) → O_S` corresponding to `d`.
If `a, b` are sections of `u^{-1}(O_X)`, one has:

```text
0 = d'((a − φ(a) · 1)(b − φ(b) · 1)) = d'(ab) − φ(a) d'(b) − φ(b) d'(a) + φ(ab) d'(1).
```

Consequently, one sees that `d` is an `S`-derivation of `u` (cf. 1.2.1 and N.D.E. (2)) if and only if `d'(1) = 0`. One
thus obtains:

<!-- original page 449 -->

**Lemma.** *The `S`-derivations of `u` are exactly the `S`-deviations of `u` of order `1` which vanish on the unit
section of `O_X`; they correspond to the `O_S(S)`-module*

```text
Hom_{O_S}(I_u / I_u², O_S),
```

*and one has an isomorphism of `O_S(S)`-modules `Dév_{⩽1}(u) ≃ O_S(S) ⊕ Dér_S(u)`.*

Returning to the general case, one deduces, with the notations of 1.3,

**Corollary.** *Let `u : Y → X` be an `S`-morphism and `Γ_u : Y → Y × X` its graph. One has a canonical isomorphism of
`O_Y(Y)`-modules*

```text
Dér_S(u) ≃ Dér_Y(Γ_u) ≃ Hom_{O_Y}(I_{Γ_u} / I_{Γ_u}², O_Y).
```

### Definition 1.4.

<!-- label: III.VII_A.1.4 -->

*Let `X` be an `S`-scheme. We call `S`-differential operator (resp. `S`-differential operator of order `⩽ n`) on `X`
any `S`-deviation (resp. any `S`-deviation of order `⩽ n`) of the identity morphism of `X`.*

According to 1.1, an `S`-differential operator of order `⩽ n` is therefore an endomorphism of `p^{-1}(O_S)`-module of
`O_X` which satisfies the equalities `(∗_n)` of 1.1. We shall denote by `Dif^n_{X/S}` the `Γ(O_S)`-module
[^N.D.E-VII_A-13] formed by the `S`-differential operators of order `⩽ n`, and by `Dif_{X/S}` that formed by all the
`S`-differential operators.

[^N.D.E-VII_A-13]: In this Exposé, the ring `Γ(S, O_S) = O_S(S)` is denoted `Γ(O_S)`.

As we saw in 1.2, one can compose `S`-deviations of `id_X`, which equips `Dif_{X/S}` with a structure of
`Γ(O_S)`-algebra; we shall say that this is the *algebra of differential operators of `X / S`*.

Similarly, for every open `V` of `X`, set `𝒟if_{X/S}(V) = Dif_{V/S} = Dév(id_V)`; according to 1.1.3, this defines a
sheaf of `O_X`-modules, called the *sheaf of `S`-differential operators on `X`*.[^N.D.E-VII_A-14]

[^N.D.E-VII_A-14]: We have modified the original here, which mentioned the sheaf `U ↦ Dif_{X_U / U}`, where `U` ranges
over the opens of `S`; this is the direct image of `𝒟if_{X/S}` by the morphism `p_X : X → S`.

### 1.4.1.

<!-- label: III.VII_A.1.4.1 -->

As we saw in 1.3, one can interpret the differential operators of `X / S` by means of the graph of the identity morphism
of `X`, i.e., of the diagonal morphism `∆ = ∆_{X/S}` of `X` into `X × X`. Let us translate into the present context the
statements of 1.3.

Endow `O_{X × X}` with the `pr₁^{-1}(O_X)`-algebra structure defined by `pr₁`, so that `∆^{-1}(O_{X × X})` is equipped
with a structure of algebra over `O_X = ∆^{-1} pr₁^{-1}(O_X)`. Let `I_{X/S}` be the kernel of the homomorphism

```text
∆^{-1}(O_{X × X}) ──m→ O_X
```

adjoint to the homomorphism `O_{X × X} → ∆_*(O_X)`, and let `P^m_{X/S}` be the `O_X`-algebra

```text
∆^{-1}(O_{X × X}) / I_{X/S}^{m+1}.
```

If `V` is an affine open of `S` and `U` an affine open of `X` above `V`, and if one sets
<!-- original page 417 --> `k = Γ(V, O_S)` and `A = Γ(U, O_X)`, one has therefore:

```text
Γ(U, P^m_{X/S}) = (A ⊗_k A) / I^{m+1},
```

<!-- original page 450 -->

where `I` is the ideal generated by the elements `a ⊗ 1 − 1 ⊗ a`, for `a ∈ A`. This being so, one has according to 1.3
an isomorphism of `O_X(X)`-modules:

```text
j_X : Dif^m_{X/S} ⥲ Hom_{O_X}(P^m_{X/S}, O_X)
```

which one can define as follows: if `d` belongs to `Dif^m_{X/S}` and if `c` is a section of `P^m_{X/S}` on `U` of the
form `a ⊗ b + I^{m+1}`, one has `j_X(d)(c) = a · d(b)`.[^N.D.E-VII_A-15]

[^N.D.E-VII_A-15]: Via this isomorphism, the `X`-derivations of `∆_{X/S}` correspond, according to 1.3.1, to the
`S`-derivations of `id_X`, i.e., to the `p^{-1}(O_S)`-derivations of `O_X`.

### 1.4.2.

<!-- label: III.VII_A.1.4.2 -->

Let `d` be a differential operator and `u` a section of `X` over `S`. We call *value of `d` at `u`* the composed
`S`-deviation

```text
S ──u→ X ──d→ X (over id_X).
```

According to 1.3 and 1.4.1, if `d` is a differential operator of order `⩽ m`, then `du` (resp. `d`) is canonically
associated with a morphism of `O_S`-modules `d' : u^{-1}(O_X) / I_u^{m+1} → O_S` (resp. a morphism of `O_X`-modules
`d'' : P^m_{X/S} → O_X`).

It is clear that one can construct `d'` from `d''` as follows: the square

```text
                 u × X
   X ≃ S ×_X X  ──────→  X × X
       │                   │
       p                   pr₁
       │           u       │
       ▼                   ▼
       S          ───────→ X
```

is cartesian, which allows us to identify `X` with `S ×_X (X × X)`, `u` with `S ×_X ∆`, hence `u^*(P^m_{X/S})` with
`u^{-1}(O_X) / I_u^{m+1}`. One thus identifies `u^*(d'')` with a morphism `u^{-1}(O_X) / I_u^{m+1} → O_S`, which is none
other than `d'`.

### 1.5.

<!-- label: III.VII_A.1.5 -->
<!-- original page 418 -->

Set as usual `I_S = Spec O_S[T] / (T²)`. Let `τ : S → I_S` be the zero section and `σ` the canonical deviation of `τ`
which we defined in 1.2.0, i.e. the homomorphism of `O_S`-modules which vanishes on the unit section of `O_S[T]/(T²)`
and which sends the class `t` of `T` modulo `T²` to the unit section of `O_S`.

Let `X` be an `S`-scheme. To every `I_S`-automorphism `u` of `I_S × X` inducing the identity on `X` there is associated
by composition a differential operator `D_u` of `X`:

```text
X ≃ S × X ──σ × X→ I_S × X ──u→ I_S × X ──pr₂→ X.
```

According to II, 3.14, the map `u ↦ D_u` is an isomorphism of the `Γ(O_S)`-Lie algebra

```text
Lie(Aut X) := Lie(Aut X)(S)
```

onto the `Γ(O_S)`-Lie algebra of `p^{-1}(O_S)`-derivations of `O_X`. The inverse isomorphism associates with every
derivation `D` the automorphism of `I_S × X` corresponding to the automorphism `a + bt ↦ a + (Da + b)t` of `O_X[T]/(T²)`.

## 2. Invariant differential operators on group schemes

<!-- label: III.VII_A.2 -->

### 2.1.

<!-- label: III.VII_A.2.1 -->
<!-- original page 419 -->

Let `G` be an `S`-group scheme; we denote by `ε` or `ε_G : S → G` the unit section of `G`.

**Definition.** *Let `U(G)` be the `Γ(O_S)`-module of `S`-deviations of `ε_G` (or `S`-deviations of the origin) (cf.
1.1).*

*If `d` and `e` are two elements of `U(G)`, `d × e` is an `S`-deviation of `ε × ε : S ≃ S × S → G × G`. The image of
`d × e` by the multiplication morphism `m : G × G → G` (cf. 1.2) will be called the product of `d` and `e` and will be
denoted `d · e`.*

*The `Γ(O_S)`-module `U(G)` is thus equipped with a structure of associative `Γ(O_S)`-algebra having `ε_G` as unit
element (1.1). We shall say that `U(G)` is the* infinitesimal algebra *of `G`.*[^N.D.E-VII_A-16]

[^N.D.E-VII_A-16]: One now says "the algebra of distributions" (at the origin) of `G`, cf. [DG70], § II.4, 6.1 and
[Ja03], I 7.7.

When `T` ranges over the schemes above `S`, the infinitesimal algebra `U(G_T)` of the `T`-group `G × T` obviously varies
contravariantly in `T`, so that we may speak of the *infinitesimal algebra functor*.

When `T` ranges over the opens of `S`, one therefore obtains a presheaf `T ↦ U(G_T)` of `O_S`-algebras; moreover,
according to 1.1.3, this is a sheaf. We shall denote it `𝒰(G)` and we shall call it the *sheaf of infinitesimal algebras
of `G`*.

The algebra `U(G)` is also a covariant functor in `G`. Indeed, if `u : G → H` is a homomorphism of `S`-groups and `d` an
`S`-deviation of `ε_G`, the image of `d` by `u` is an element `U(u)(d) = ud` of `U(H)`. The map
`U(u) : U(G) → U(H)` thus defined is obviously a homomorphism of `Γ(O_S)`-algebras. One defines similarly a homomorphism
`𝒰(u)` from `𝒰(G)` to `𝒰(H)`.

### 2.2.

<!-- label: III.VII_A.2.2 -->

Let `d` be an element of `U(G)`, i.e., an `S`-deviation of the origin of `G`. Consider the `S`-deviation `d × G` of
`ε × G : G ≃ S × G → G × G` obtained from `d` by base change (1.2.2); the image of `d × G` by the multiplication
morphism `m : G × G → G` is an `S`-deviation of `m ∘ (ε × id_G) = id_G`, i.e., an element of `Dif_{G/S}`, which we shall
denote `d_G`.

The map `d ↦ d_G` is obviously `Γ(O_S)`-linear and the "commutative" diagram below shows that one has
`(e · d)_G = d_G · e_G`:[^N.D.E-VII_A-17] <!-- original page 420 -->

[^N.D.E-VII_A-17]: We have corrected the original, replacing in the diagram `d × G × G` by `G × d × G`, so that the
composition on the left side of the triangle is `(e × d) × G`, and so that the map `d ↦ d_G` is an anti-isomorphism of
`U(G)` onto the right-invariant differential operators (cf. 2.3, 2.4 below); on the other hand, by defining `_G d` as
the image under `m` of `G × d`, one would obtain similarly an isomorphism of `U(G)` onto the left-invariant differential
operators (cf. [DG70], § II.4, Th. 6.5). We have corrected 2.4 and 2.5 accordingly.

```text
                                 m × G
   G × G × G  ─────────────────────────────→  G × G
       △                                       △
       │ G × d × G                              │ G × m
       │ ε × G × G                              │

  G × G                              G × G                     m
   △  △                              △  △
   │  │ e × G   m                   │  │ d × G   m
   │  │ ε × G                       │  │ ε × G
   │                                │
   │           e_G                  │           d_G
   G  ─────────────→  G  ─────────────→  G       (over id_G everywhere).
```

The commutativity of the two bottom triangles follows from the definition of `d_G` and `e_G`; on the other hand, the
composed `S`-deviation of `e × G` and `G × d × G` is `(e × d) × G` (cf. 1.2.2), its image by `m × G` is
`(e · d) × G`, and the image of the latter by `m` is therefore equal to `(e · d)_G`.

One thus obtains an anti-homomorphism `U(G) → Dif_{G/S}` of `Γ(O_S)`-algebras, called *right translation*.[^N.D.E-VII_A-18]

[^N.D.E-VII_A-18]: It would be preferable to call this a *left action*. Indeed, let for example `d` be an `S`-derivation
of the origin; according to 1.2.1, `d` is the composition of the `S`-derivation `(τ, ∂_t) : S → I_S` and a morphism
`x : I_S → G` such that `x ∘ τ = ε` (i.e. `x ∈ Lie(G/S)(S)`), and then `d_G` is the derivation of `O_G` which sends a
local section `φ` to the section `g ↦ ∂_t φ(xg)`. Moreover, with this terminology, one could say: "the left action
commutes with right translations".

If `𝒟if_{G/S}` denotes the sheaf of `S`-differential operators on `G` (cf. 1.4) and `p` the structural morphism
`G → S`, one defines similarly a "right translation": `𝒰(G) → p_*(𝒟if_{G/S})`.

### 2.3.

<!-- label: III.VII_A.2.3 -->

We shall now characterize the differential operators of `G` over `S` of the form `d_G`. Let `g : S → G` be a section
of the structural morphism of `G` and `g_G` the right translation of `G` by `g`, i.e., the composed morphism:

```text
g_G : G ≃ G × S ──G × g→ G × G ──m→ G.
```

For every differential operator `D` of `G` over `S`, the composition `g_G^{-1} D g_G` (cf. 1.2) is again an
`S`-deviation of `id_G`, i.e., an element of `Dif_{X/S}`; we shall denote:

```text
D^g = g_G^{-1} D g_G.
```

We shall say that `D` is *right-invariant* if, for every base change `t : T → S` and every section `g : T → G × T`, one
has `(D_T)^g = D_T`.

**Lemma.** *For every differential operator `D` of `G` over `S`, the following assertions are equivalent (where `m` is
the multiplication morphism of `G`):*

<!-- original page 421 -->

   *(i) `D` is right-invariant.*

   *(ii) The two following deviations of `m` are equal: `D m = m(D × G)`.*

(ii) ⇒ (i): since the condition (ii) is stable under base change, it suffices to show that (ii) entails the equality
`D^g = D` for every section `g : S → G`. Let `h` be the morphism `G × g : G ≃ G × S → G × G`, so that `m ∘ h` is the
right translation `g_G`. The equality `D^g = D` is equivalent to the equality `g_G ∘ D = D ∘ g_G`, and this follows
from the commutative diagram:

```text
                    m                     h
       G  ←──────────  G × G  ←──────────  G

   D, id_G        D × G, id_{G × G}      D, id_G

                    m                     h
       G  ←──────────  G × G  ←──────────  G.
```

(i) ⇒ (ii): take indeed for `t : T → S` the structural morphism `p : G → S`, for section `g : T → G × T` the diagonal
morphism `∆ : G → G × G`. The right translation

```text
∆_{G × G} : G × G  ⟶  G × G
```

is then the morphism from `G × G` into `G × G` with components `m` and `pr₂`. The equality `(D_G)^∆ = D_G` is then
equivalent to the commutativity of the first square of the following diagram:

```text
                  ∆_{G × G}                  pr₁
       G × G  ──────────────→  G × G  ──────────→  G

   D_G, id_{G × G}          D_G, id_{G × G}    D, id_G

                  ∆_{G × G}                  pr₁
       G × G  ──────────────→  G × G  ──────────→  G.
```

The equality (ii) thus follows from the fact that `m = pr₁ ∘ ∆_{G × G}`.

<!-- original page 422 -->

Consider for example an element `d` of the infinitesimal algebra `U(G)`. The squares of the diagram

```text
                          d × G × G                            m × G
       G × G  ←────  S × G × G  ──────────────→  G × G × G  ──────────→  G × G
                          ε × G × G

         m                    S × m                  G × m                  m

                          d × G                                m
         G  ←────  S × G  ──────────────→  G × G  ──────────→  G
                          ε × G
```

are then commutative. Since one has

```text
m ∘ (d × G) = d_G    and    (m × G) ∘ (d × G × G) = d_G × G,
```

one also has `d_G ∘ m = m ∘ (d_G × G)`. Therefore: *for every `S`-deviation `d` of the origin, `d_G` is a right-invariant
differential operator*.

### 2.4. Theorem.

<!-- label: III.VII_A.2.4 -->

*(i) The map `d ↦ d_G` is an anti-isomorphism[^N.D.E-VII_A-19] of the infinitesimal algebra `U(G)` onto the subalgebra
`Dif^G_{G/S}` of `Dif_{G/S}` formed by the right-invariant differential operators.*

*(ii) Similarly, the map `d ↦ _G d` is an isomorphism of `U(G)` onto the subalgebra of `Dif_{G/S}` formed by the
left-invariant differential operators.*

[^N.D.E-VII_A-19]: We have corrected "isomorphism" to "anti-isomorphism", and added assertion (ii), cf. N.D.E. (17).

Let in fact `D` be an arbitrary differential operator of `G` over `S` and let us denote by `D_0` its value at the origin,
i.e., the composed deviation `S ──ε→ G ──D→ G` (over `id_G`). The right-invariant differential operator `(D_0)_G` is
then obtained by composition:

```text
G ≃ S × G ──ε × G→ G × G ──D × G→ G × G ──m→ G (over id_{G × G}).
```

If `D` is right-invariant, one has `D m = m(D × G)`, whence

```text
D = D m(ε × G) = m(D × G)(ε × G) = (D_0)_G.
```

In particular, the map `d ↦ d_G` is surjective.

Conversely, let `d` be an `S`-deviation of the origin. One then has a commutative square

```text
                          d × G
       G × G  ←──────────  G
         △                  △
   G × ε │                  │ ε
                       d
       G × S ≃ G  ←──────  S
```

<!-- original page 423 -->

whence it follows that `d = m(G × ε) d = m(d × G) ε = (d_G)_0`. *A fortiori*, the map `d ↦ d_G` is injective. This proves
the theorem.

When `S` varies, Theorem 2.4 obviously implies that the right translation `𝒰(G) → p_*(𝒟if_{G/S})` is an anti-isomorphism
of `O_S`-algebras of `𝒰(G)` onto the sheaf of `O_S`-algebras `p_*(𝒟if_{G/S})^G`, which to every open `U` of `S`
associates `Dif^{G_U}_{G_U / U}`.

### 2.4.1. Remark.

<!-- label: III.VII_A.2.4.1 -->

Consider the commutative diagram

```text
                       η
        G  ←──────────  G × G
        △               △    △
     p  │   ε        pr₁ │    │ ∆
        │       p        │
        S  ←──────────  G,
```

where `η` denotes the morphism "`(x, y) ↦ y x^{-1}`".[^N.D.E-VII_A-20] The latter induces morphisms

```text
η' : η^{-1}(O_G) ⟶ O_{G × G}    and    ∆^{-1}(η') : p^{-1} ε^{-1}(O_G) ⟶ ∆^{-1}(O_{G × G}).
```

[^N.D.E-VII_A-20]: i.e., `G` acts on itself on the left by right translations.

For every integer `n ⩾ 1`, set `p^n_{G/S} = ε^{-1}(O_G) / I_ε^{n+1}` (cf. 1.3 and 1.4 for the notations).[^N.D.E-VII_A-21]
Since the square formed by the morphisms `ε`, `η`, `∆` and `p` is cartesian, `∆^{-1}(η')` induces an isomorphism of
`O_G`-modules:

```text
p^*(p^n_{G/S}) ⥲ P^n_{G/S}.
```

[^N.D.E-VII_A-21]: In what follows, we have corrected the original, which referred to the square formed by the morphisms
`p`, `p`, `η`, and `pr₁`, instead of `ε`, `η`, `∆` and `p`.

The differential operators of `G` over `S` of order `⩽ n` therefore correspond bijectively to the morphisms of
`O_G`-modules `p^*(p^n_{G/S}) ⟶ O_G`, i.e., to the morphisms <!-- original page 424 --> of `O_S`-modules

```text
p^n_{G/S} ⟶ p_*(O_G).
```

In this bijection, the right-invariant differential operators correspond to the composed arrows

```text
p^n_{G/S} ──→ O_S ──can.→ p_*(O_G).
```

One thus recovers the isomorphism of Theorem 2.4.

### 2.5.

<!-- label: III.VII_A.2.5 -->

[^N.D.E-VII_A-22] Let `Lie(G)` be the Lie algebra of `G`;[^N.D.E-VII_A-23] we shall define a morphism of `Γ(O_S)`-Lie
algebras `α : Lie(G) → U(G)`.

[^N.D.E-VII_A-22]: In this paragraph, we have modified the order, beginning by defining the map `α : Lie(G) → U(G)`,
and we have corrected the original as indicated in N.D.E. (17).

[^N.D.E-VII_A-23]: In this Exposé, if `G` (resp. `X`) is an `S`-group scheme (resp. an `S`-scheme), the "Lie algebra"
`Lie(G)` (resp. `Lie(Aut X)`) denotes, with the notations of Exposé II, `Lie(G/S)(S)` (resp. `Lie(Aut_S(X)/S)(S)`); it
is a `Γ(O_S)`-Lie algebra, according to II, 4.11 and 3.14.

Let `s : S → I_S` be the zero section of `I_S → S` and `σ` the deviation of `s` defined in 1.2.0. Recall (cf. II, 4.1)
that `Lie(G)` is the set of morphisms `x : I_S → G` such that `x ∘ s = ε_G`. Then the composition

```text
S ──σ→ I_S ──x→ G (over s)
```

is an `S`-deviation of `ε_G`, i.e., an element of `U(G)`; with the notations of 1.2 `(†)`, it is denoted `σx`. Moreover,
according to 1.2.1, the map `α : x ↦ σx` is an isomorphism of `O_S(S)`-modules from `Lie(G)` onto the submodule
`Dér(ε_G)` of `U(G)` formed by the `S`-derivations of `ε_G`. We shall see that `α` is a morphism of Lie
algebras.[^N.D.E-VII_A-24] Let

```text
ρ' : U(G) ⟶ Dif_{G/S}
```

be the algebra morphism which to an `S`-deviation `d` of `ε_G` associates the left-invariant differential operator
`_G d ∈ Dif_{G/S}`, cf. 2.2, N.D.E. (17).

[^N.D.E-VII_A-24]: See also II, 4.11.

Let `ρ : G → Aut_S(G)` be the homomorphism of group functors which to an `S`-morphism `g : T → G` associates the right
translation of `G_T` by `g`, i.e. the morphism:

```text
G_T ≃ T ×_T G_T ──G_T × g→ G_T ×_T G_T ──m_T→ G_T.
```

Recall also (cf. 1.5 and II, 3.14) that `Lie(Aut G) = Lie(Aut_S(G)/S)(S)` is identified with the infinitesimal
automorphisms of `G`, i.e., with the automorphisms of `I_S × G` inducing the identity on `G`.
<!-- original page 456 -->
Since `ρ` is a monomorphism, the same holds for the morphism `Lie(ρ) : Lie(G/S) → Lie(Aut_S(G)/S)` (see, for example,
Exp. II, N.D.E. (50)), hence `Lie(ρ) : Lie(G) → Lie(Aut G)` is injective.

On the other hand, according to 1.5, the map `β` which to every infinitesimal automorphism `u` of `G` associates the
differential operator `D_u` of `G`:

```text
G ≃ S × G ──σ × G→ I_S × G ──u→ I_S × G ──pr₂→ G
```

is an isomorphism of `Lie(Aut G)` onto the Lie subalgebra of `Dif_{G/S}` formed by the `p^{-1}(O_S)`-derivations of
`O_G`.

For every `x ∈ Lie(G)`, one has the commutative square below which determines the image of `x` by `Lie(ρ)`:

```text
                       Lie(ρ)(x)
       I_S × G  ───────────────→  I_S × G

   x × G                                pr₂
                          m
       G × G  ──────────────────→  G.
```

<!-- original page 425 -->

Taking this diagram into account, the image of `Lie(ρ)(x)` by `β` is the composed deviation

```text
G ≃ S × G ──σ × G→ I_S × G ──G × x→ G × G ──m→ G (over s × G)
```

which, according to 2.2 N.D.E. (17), is none other than `_G(σx) = ρ'(α(x))`. One thus obtains a commutative diagram:

```text
                       Lie(ρ)
       Lie(G)  ─────────────────→  Lie(Aut G)
          │                              │
        α │                              │ β
          │              ρ'              │
          ▼                              ▼
       U(G)  ──────────────────────────→  Dif_{G/S}
```

where `Lie(ρ)`, `β` and `ρ'` are morphisms of Lie algebras. Since `ρ'` is injective, it follows that `α` is also a
morphism of Lie algebras. Consequently, one has obtained:

**Proposition.** *`α` is an isomorphism of `O_S(S)`-Lie algebras, from `Lie(G)` into the Lie algebra of `S`-derivations
of `ε_G`, itself isomorphic via `Lie(ρ)` to the Lie algebra of `S`-derivations of `G` invariant under left
translation.*[^N.D.E-VII_A-25]

[^N.D.E-VII_A-25]: There are examples of Lie algebras `𝔤` over a ring `A`, such that the map `𝔤 → U(𝔤)` is not
injective, cf. [BLie], § I.2, Ex. 9. The above result shows (since `α` factors through `Lie(G) → U(Lie(G)) → U(G)`) that
this cannot happen for "algebraic" Lie algebras, i.e., of the form `Lie(G)`, where `G` is an `A`-group scheme.

## 3. Coalgebras and Cartier duality

<!-- label: III.VII_A.3 -->

### 3.1.

<!-- label: III.VII_A.3.1 -->
<!-- original page 426 -->

Let `S` be a scheme (or, more generally, a ringed space). An *`O_S`-coalgebra*[^N.D.E-VII_A-26] is a pair
`(𝒰, ∆_𝒰)` consisting of an `O_S`-module `𝒰` and a morphism of `O_S`-modules `∆_𝒰 : 𝒰 → 𝒰 ⊗_{O_S} 𝒰` (called the
*diagonal morphism* or *comultiplication*) such that:

   (i) `σ ∘ ∆_𝒰 = ∆_𝒰`, where `σ(a ⊗ b) = b ⊗ a`.

   (ii) The square

```text
                              ∆_𝒰
       𝒰  ──────────────────────→  𝒰 ⊗_{O_S} 𝒰

   ∆_𝒰                                    id_𝒰 ⊗ ∆_𝒰

                          ∆_𝒰 ⊗ id_𝒰
       𝒰 ⊗_{O_S} 𝒰  ──────────────────→  𝒰 ⊗_{O_S} 𝒰 ⊗_{O_S} 𝒰
```

is commutative.

   (iii) There exists a morphism of `O_S`-modules `ε_𝒰 : 𝒰 → O_S`, called the *augmentation*, such that the composed
morphisms

```text
𝒰 ──∆_𝒰→ 𝒰 ⊗_{O_S} 𝒰 ──id_𝒰 ⊗ ε_𝒰→ 𝒰 ⊗_{O_S} O_S ≃ 𝒰
𝒰 ──∆_𝒰→ 𝒰 ⊗_{O_S} 𝒰 ──ε_𝒰 ⊗ id_𝒰→ O_S ⊗_{O_S} 𝒰 ≃ 𝒰
```

are the identity morphism of `𝒰`.

[^N.D.E-VII_A-26]: One also says "cogebra", cf. [BAlg], III § 11.1. On the other hand, one will note that in this
Exposé (as well as in VII_B), we place ourselves in the category of cocommutative coalgebras (i.e., those satisfying
condition (i)), which is crucial for defining the product and the notion of group coalgebra (cf. 3.1.0 and 3.2).

If `ε_𝒰` and `ε'_𝒰` are two augmentations, one has `ε_𝒰 = (ε_𝒰 ⊗ ε'_𝒰) ∘ ∆_𝒰 = ε'_𝒰`; the augmentation is therefore
uniquely determined by (iii).

If `(𝒰, ∆_𝒰)` and `(𝒱, ∆_𝒱)` are two `O_S`-coalgebras, a *morphism* from the first into the second is a morphism of
`O_S`-modules `f : 𝒰 → 𝒱` such that the diagrams

```text
        f                              f
   𝒰  ────→  𝒱                    𝒰  ────→  𝒱
   │          │                    │          │
 ∆_𝒰         ∆_𝒱      and        ε_𝒰        ε_𝒱
   ▼          ▼                    │          │
                                   ▼          ▼
   𝒰 ⊗ 𝒰  ─f ⊗ f→  𝒱 ⊗ 𝒱                  O_S
```

are commutative. Morphisms of coalgebras compose like morphisms of `O_S`-modules, so that we shall be able to speak of
the *category of `O_S`-coalgebras*.

<!-- original page 427 -->

### 3.1.0.

<!-- label: III.VII_A.3.1.0 -->

[^N.D.E-VII_A-27] This category has finite products: the final object is the `O_S`-module `O_S`, the comultiplication
being the identity; the product of two coalgebras `(𝒰, ∆_𝒰)` and `(𝒱, ∆_𝒱)` is the tensor product `𝒰 ⊗_{O_S} 𝒱`, the
comultiplication being the composed morphism

```text
𝒰 ⊗ 𝒱 ──∆_𝒰 ⊗ ∆_𝒱→ 𝒰 ⊗ 𝒰 ⊗ 𝒱 ⊗ 𝒱 ──id_𝒰 ⊗ σ ⊗ id_𝒱→ 𝒰 ⊗ 𝒱 ⊗ 𝒰 ⊗ 𝒱
```

where `σ(a ⊗ b) = b ⊗ a`; the canonical projections of `𝒰 ⊗ 𝒱` onto the factors `𝒰` and `𝒱` are the morphisms
`id_𝒰 ⊗ ε_𝒱` and `ε_𝒰 ⊗ id_𝒱`,[^N.D.E-VII_A-28] and the "diagonal morphism" `𝒰 → 𝒰 ⊗ 𝒰` (corresponding to the pair of
morphisms `(id_𝒰, id_𝒰)`) is none other than the comultiplication `∆_𝒰`.

[^N.D.E-VII_A-27]: We have added the numbering 3.1.0, for later references.

[^N.D.E-VII_A-28]: The following has been added. Let us also recall that, to show that `𝒰 ⊗ 𝒱` is indeed the product
of `𝒰` and `𝒱` in the category of cocommutative `O_S`-cogebras, one verifies that if one has an arbitrary `O_S`-cogebra
`ℰ` and morphisms of cogebras `f : ℰ → 𝒰` and `g : ℰ → 𝒱`, then every morphism of cogebras `φ : ℰ → 𝒰 ⊗ 𝒱` such that
`pr_𝒰 ∘ φ = f` and `pr_𝒱 ∘ φ = g` is necessarily equal to `(f ⊗ g) ∘ ∆_ℰ`, and this is a morphism of cogebras if and
only if it equals `(g ⊗ f) ∘ ∆_ℰ`.

### 3.1.1.

<!-- label: III.VII_A.3.1.1 -->

Let `𝒜` be a commutative `O_S`-algebra, locally free and of finite type as an `O_S`-module. If we set

```text
𝒜^* = Hom_{O_S-Mod.}(𝒜, O_S),
```

the canonical morphism `φ` from `𝒜^* ⊗_{O_S} 𝒜^*` into `(𝒜 ⊗_{O_S} 𝒜)^*` is invertible. If `m : 𝒜 ⊗ 𝒜 → 𝒜` is the
morphism defining the multiplication of `𝒜`, one obtains by composition a diagonal morphism

```text
∆_{𝒜^*} : 𝒜^* ──m^*→ (𝒜 ⊗ 𝒜)^* ──φ^{-1}→ 𝒜^* ⊗ 𝒜^*.
```

This diagonal morphism obviously makes `𝒜^*` an `O_S`-coalgebra whose augmentation is the
<!-- original page 428 --> transpose morphism of the morphism `O_S → 𝒜` defined by the unit section of `𝒜`. Moreover,
it is clear that:

*The functor `𝒜 ↦ 𝒜^*` is an anti-equivalence of the category of `O_S`-algebras which are locally free and of finite
type as `O_S`-modules, onto the category of `O_S`-coalgebras locally free and of finite type as `O_S`-modules.*

### 3.1.2.

<!-- label: III.VII_A.3.1.2 -->

To every `O_S`-coalgebra `𝒰` is canonically associated an `S`-functor

```text
Spec^* 𝒰 : (Sch/S)° ⟶ (Ens).
```

Note indeed that, for every `S`-scheme `q : T → S`, `q^*(𝒰 ⊗_{O_S} 𝒰)` is identified with
`q^*(𝒰) ⊗_{O_T} q^*(𝒰)`, so that `q^*(∆_𝒰)` makes `𝒰_T = q^*(𝒰)` into an `O_T`-coalgebra; we can therefore set by
definition and with an obvious abuse of notation:[^N.D.E-VII_A-29]

```text
(Spec^* 𝒰)(T) = { x ∈ Γ(T, 𝒰_T) | ε_{𝒰_T}(x) = 1 and ∆_{𝒰_T}(x) = x ⊗ x }.
```

[^N.D.E-VII_A-29]: For every `x ⊗ y ∈ Γ(T, 𝒰_T) ⊗_{O(T)} Γ(T, 𝒰_T)`, its image in `Γ(T, 𝒰_T ⊗_{O_T} 𝒰_T)` is again
denoted `x ⊗ y`.

<!-- original page 458 -->

The sections `x` of `𝒰_T` obviously correspond to the morphisms of `O_T`-modules `ξ : O_T → 𝒰_T`; the conditions
`ε(x) = 1` and `∆(x) = x ⊗ x` simply express that `ξ` is a morphism of coalgebras. One therefore also has:

```text
(Spec^* 𝒰)(T) = Hom_{O_T-coalg.}(O_T, 𝒰_T).
```

In particular, one has the following proposition:[^N.D.E-VII_A-30]

**Proposition 3.1.2.1.** *Let `𝒜` be a commutative `O_S`-algebra which is locally free of finite type as an `O_S`-module.
Then the `S`-functor `Spec^* 𝒜^*` is represented by `Spec 𝒜`.*

<!-- label: III.VII_A.3.1.2.1 -->

Indeed, for every `S`-scheme `T`, one has canonical isomorphisms:

```text
(Spec^* 𝒜^*)(T) = Hom_{O_T-coalg.}(O_T, 𝒜_T^*) ≃ Hom_{O_T-alg.}(𝒜_T, O_T) ≃ (Spec 𝒜)(T).
```

[^N.D.E-VII_A-30]: We have added the numbering 3.1.2.1, for later references. Note moreover that the `S`-functor
`Spec^* 𝒰` is a sheaf for the Zariski topology (and even for the (fpqc) topology if `𝒰` is a quasi-coherent
`O_S`-module).

### 3.2.

<!-- label: III.VII_A.3.2 -->

An `O_S`-*coalgebra in groups* (i.e., a group in the category of `O_S`-coalgebras) consists of the data of an
`O_S`-coalgebra `(𝒰, ∆_𝒰)` and three morphisms of `O_S`-coalgebras `m_𝒰 : 𝒰 ⊗ 𝒰 → 𝒰`, `η_𝒰 : O_S → 𝒰` and
`c_𝒰 : 𝒰 → 𝒰` satisfying the conditions (ii)*, (iii)* and (vi) below; on the other hand, the fact that `m_𝒰` is a
morphism of cogebras translates into the commutativity of diagrams (iv) and (v)
<!-- original page 429 --> below:

```text
                              m_𝒰
       𝒰 ⊗ 𝒰  ────────────────────→  𝒰

   ∆_𝒰 ⊗ ∆_𝒰
       │
(iv)   ▼                                  ∆_𝒰
   𝒰 ⊗ 𝒰 ⊗ 𝒰 ⊗ 𝒰

   id_𝒰 ⊗ σ ⊗ id_𝒰
                              m_𝒰 ⊗ m_𝒰
   𝒰 ⊗ 𝒰 ⊗ 𝒰 ⊗ 𝒰  ──────────────────→  𝒰 ⊗ 𝒰
```

```text
                              m_𝒰
       𝒰 ⊗ 𝒰  ────────────────────→  𝒰
              ╲                    ╱
(v)            ╲                  ╱
        ε_𝒰 ⊗ ε_𝒰              ε_𝒰
                  ╲          ╱
                       O_S
```

   (ii)* The square

```text
                              id_𝒰 ⊗ m_𝒰
       𝒰 ⊗ 𝒰 ⊗ 𝒰  ──────────────────→  𝒰 ⊗ 𝒰

   m_𝒰 ⊗ id_𝒰                                 m_𝒰

                              m_𝒰
       𝒰 ⊗ 𝒰  ────────────────────→  𝒰
```

is commutative.

   (iii)* The two compositions below equal the identity morphism of `𝒰`:

```text
𝒰 ≃ 𝒰 ⊗ O_S ──id_𝒰 ⊗ η_𝒰→ 𝒰 ⊗ 𝒰 ──m_𝒰→ 𝒰
𝒰 ≃ O_S ⊗ 𝒰 ──η_𝒰 ⊗ id_𝒰→ 𝒰 ⊗ 𝒰 ──m_𝒰→ 𝒰.
```

   (vi) The composed morphism below is equal to `η_𝒰 ∘ ε_𝒰`:

<!-- original page 430 -->

```text
𝒰 ──∆_𝒰→ 𝒰 ⊗ 𝒰 ──c_𝒰 ⊗ id_𝒰→ 𝒰 ⊗ 𝒰 ──m_𝒰→ 𝒰.
```

### 3.2.1.

<!-- label: III.VII_A.3.2.1 -->

The morphisms `η_𝒰` and `c_𝒰` are uniquely determined by `m_𝒰`. On the other hand, conditions (ii)* and (iii)* simply
express that `m_𝒰` makes `𝒰` an `O_S`-algebra having as unit section the image by `η_𝒰` of the unit section of `O_S`.
Condition (iv) also expresses that the diagonal morphism `∆_𝒰` is compatible with multiplication; and indeed,
`∆_𝒰 : 𝒰 → 𝒰 ⊗ 𝒰` must be a homomorphism of group coalgebras, which also entails the commutativity of the triangle

```text
                       O_S
                  ╱         ╲
             η_𝒰              η_𝒰 ⊗ η_𝒰
(v)*            ╱               ╲
              ╱                   ╲
       𝒰  ───────────────────→  𝒰 ⊗ 𝒰.
                       ∆_𝒰
```

On the other hand, as in every category, the *antipode* `c_𝒰` is an isomorphism of `𝒰` onto the "opposite" group
object;[^N.D.E-VII_A-31] in particular, `c_𝒰` induces an algebra isomorphism of `𝒰` onto the opposite algebra `𝒰°`.

[^N.D.E-VII_A-31]: i.e. endowed with the multiplication `m'_𝒰 = m_𝒰 ∘ σ`.

### 3.2.2.

<!-- label: III.VII_A.3.2.2 -->

Since the functor `𝒰 ↦ Spec^* 𝒰` commutes with finite products, it transforms a group coalgebra into a group
`S`-functor; and indeed, for every `S`-scheme `T`, the elements `x ∈ Γ(T, 𝒰_T)` belonging to `(Spec^* 𝒰)(T)` form a
group under the multiplication of the algebra `Γ(T, 𝒰_T)`; the inverse of `x` is none other than `c_𝒰(x)`. According to
3.1.2.1, one has:

**Scholium 3.2.2.1.**[^N.D.E-VII_A-32] *Let `𝒰` be an `O_S`-coalgebra in groups, finite and locally free as an
`O_S`-module. Then the group `S`-functor `Spec^* 𝒰` is represented by the `S`-group, finite and locally free,
`Spec 𝒰^*`.*

<!-- label: III.VII_A.3.2.2.1 -->

[^N.D.E-VII_A-32]: We have added this scholium, implicit in the original.

**Remark 3.2.2.2.** *Let `ℒ` be an `O_S`-Lie algebra and `𝒰(ℒ)` the enveloping algebra of `ℒ`, i.e., the sheaf on `S`
associated with the presheaf which to every open `V` assigns the enveloping algebra `U(Γ(V, ℒ))` of the Lie algebra
`Γ(V, ℒ)`.*

<!-- label: III.VII_A.3.2.2.2 -->

Every homomorphism from `ℒ` into the Lie algebra underlying an associative `O_S`-algebra factors in one and only one
way through the canonical morphism <!-- original page 431 --> from `ℒ` into `𝒰(ℒ)`; moreover, this universal property
entails, besides the functoriality of `𝒰(ℒ)` in `ℒ`, that the enveloping algebra of a product of Lie algebras is
identified with the tensor product of the enveloping algebras.

In particular, the diagonal morphism `δ : ℒ → ℒ × ℒ` induces an algebra homomorphism
`∆ : 𝒰(ℒ) → 𝒰(ℒ × ℒ) ≃ 𝒰(ℒ) ⊗ 𝒰(ℒ)`. The zero morphism `ℒ → 0` induces a homomorphism `ε : 𝒰(ℒ) → 𝒰(0) ≃ O_S`. The
isomorphism `x ↦ −x` of `ℒ` onto the opposite Lie algebra `ℒ°` induces an anti-isomorphism `c` of the algebra `𝒰(ℒ)`.
One then verifies easily that the multiplication `m` of the algebra `𝒰(ℒ)` makes `(𝒰(ℒ), ∆)` an `O_S`-coalgebra in
groups with `ε` as augmentation and `c` as antipode.[^N.D.E-VII_A-33]

[^N.D.E-VII_A-33]: The group `S`-functor `Spec^* 𝒰(ℒ)` is not representable in general, but one will see later (5.5)
that if `S` is a scheme of characteristic `p`, if `ℒ` is finite locally free over `O_S` and if `𝒰_p(ℒ)` is its restricted
enveloping algebra (cf. 5.3), then `Spec^* 𝒰_p(ℒ)` is represented by a finite and locally free `S`-group.

### 3.2.3.

<!-- label: III.VII_A.3.2.3 -->

[^N.D.E-VII_A-34] Let `𝒰` be an `O_S`-coalgebra in groups. We shall see that the group `S`-functor `G = Spec^* 𝒰` is
*very good*, in the sense of II, 4.6 and 4.10.

[^N.D.E-VII_A-34]: We have expanded this paragraph.

Let `M` be a free `O_S`-module of rank `r`, and let `T → S` be an `S`-scheme. Since `I_T(M) = Spec(O_T ⊕ M_T)`, so that
`π : I_T(M) → T` is affine, one has

```text
π_*(𝒰_{I_T(M)}) = 𝒰_T ⊗_{O_T} π_*(O_{I_T(M)}) = 𝒰_T ⊗_{O_T} (O_T ⊕ M_T),
```

and so

```text
(1)    Γ(I_T(M), 𝒰_{I_T(M)}) ≃ Γ(T, 𝒰_T) ⊗_{O(T)} (O(T) ⊕ Γ(T, M_T)).
```

Let `(d_1, …, d_r)` be a basis of `M`. Then an element `u_0 + ∑_i u_i d_i` of `Γ(I_T(M), 𝒰_{I_T(M)})` belongs to
`G(I_T(M))` if and only if one has:

```text
1 = ε(u_0 + ∑_i u_i d_i) = ε(u_0) + ∑_i ε(u_i) d_i,
```

and

```text
(u_0 + ∑_i u_i d_i) ⊗ (u_0 + ∑_i u_i d_i) = ∆(u_0 + ∑_i u_i d_i) = ∆(u_0) + ∑_i ∆(u_i) d_i,
```

that is to say:

```text
(2)    { ε(u_0) = 1,  ∆ u_0 = u_0 ⊗ u_0,    (i.e. u_0 ∈ G(T))
       { ε(u_i) = 0,  ∆(u_i) = u_i ⊗ u_0 + u_0 ⊗ u_i,  for i = 1, …, r.
```

Moreover, the morphism `G(I_T(M)) → G(T)` corresponding to the zero section of `I_T(M) → T` is given by
`u_0 + ∑_i u_i d_i ↦ u_0`. From this, combined with (1) and (2), one deduces that, if `N` is a second free `O_S`-module
of finite rank, the diagram of sets

```text
       G(I_T(M ⊕ N))          ─────→  G(I_T(N))
           │                              │
           ▼                              ▼
       G(I_T(M))               ─────→  G(T)
```

is cartesian, i.e. `G` satisfies condition (E) of II, 3.5.

<!-- original page 462 -->

Let us denote by `Prim Γ(T, 𝒰_T)` the sub-`O(T)`-module of `Γ(T, 𝒰_T)` formed by the *primitive elements*, i.e., the
elements `u` which satisfy (with the abuse of notation signaled in 3.1.2):

```text
∆u = u ⊗ 1 + 1 ⊗ u,    ε(u) = 0.
```

[^N.D.E-VII_A-35]

[^N.D.E-VII_A-35]: Note that the second condition is a consequence of the first, since the first entails that
`u = (id ⊗ ε) ∆(u) = u + ε(u)`, whence `ε(u) = 0`.

Since `(Lie G)(T)` is the set of elements `u_0 + u d ∈ G(I_T)` above the unit element `u_0 = 1` of `G(T)`, one obtains
an isomorphism of `O(T)`-modules, functorial in `T`:[^N.D.E-VII_A-36]

```text
(Lie G)(T) ≃ Prim Γ(T, 𝒰_T).
```

[^N.D.E-VII_A-36]: The structure of `O_S`-module on `Lie G` is defined in II, Prop. 3.6.

On the other hand, one deduces from (1) that

```text
Prim Γ(I_T(M), 𝒰_{I_T(M)}) ≃ Prim Γ(T, 𝒰_T) ⊗_{O(T)} O(I_T(M)),
```

and it follows that the natural morphism of `O(I_T(M))`-modules:

```text
(Lie G)(T) ⊗_{O(T)} O(I_T(M)) ⟶ (Lie G)(I_T(M))
```

is an isomorphism, i.e. `Lie G` is a *good `O_S`-module* (cf. II, Déf. 4.4).

So `G` is a good group `S`-functor (cf. II, Déf. 4.6), and according to II, 4.7.2, `Lie G` is equipped with an
`O_S`-bilinear "Lie bracket" satisfying the Jacobi identity. It remains to show that `G` is very good, i.e., that the
"bracket" on `(Lie G)(T)` satisfies `[u, u] = 0` for every `u ∈ (Lie G)(T)` (cf. II, 4.10).

Let `u, v` be two elements of `(Lie G)(T)`, i.e., two primitive elements of `Γ(T, 𝒰_T)`. Set
`I = Spec O_S[d]/(d²)` and `I' = Spec O_S[d']/(d'²)`. Since the composition law of `G(I × I')` is induced by the
multiplication of the algebra `𝒰_{I × I'}`, one has in `G(I × I')` the equality:

```text
(1 + ud)(1 + vd')(1 + ud)^{-1}(1 + vd')^{-1} = (1 + ud)(1 + vd')(1 − ud)(1 − vd')
                                              = 1 + (uv − vu) dd'
```

<!-- original page 432 -->

According to the description of the bracket `[u, v]` given before Prop. 4.8 of Exp. II, one obtains that

```text
[u, v] = uv − vu,
```

where the right-hand term is the commutator of `u` and `v` in the algebra `Γ(T, 𝒰_T)`, whence `[u, u] = 0`. One has thus
obtained the following proposition:[^N.D.E-VII_A-37]

**Proposition.** *Let `𝒰` be an `O_S`-coalgebra in groups. The group `S`-functor `G = Spec^* 𝒰` is very good, and one
has an isomorphism `Lie G ≃ Prim 𝒲(𝒰)` of `O_S`-Lie algebras, where `Prim 𝒲(𝒰)` denotes the functor which to every
`T → S` associates the `O(T)`-Lie algebra formed by the primitive elements of `𝒲(𝒰)(T) = Γ(T, 𝒰_T)`.*

[^N.D.E-VII_A-37]: We have added this proposition, which summarizes the preceding discussion.

### 3.3.

<!-- label: III.VII_A.3.3 -->

Suppose finally that `𝒰` is a commutative group coalgebra, i.e., the triangle

```text
                              σ
       𝒰 ⊗ 𝒰  ────────────────────→  𝒰 ⊗ 𝒰
              ╲                    ╱
(i)*           ╲                  ╱
              m_𝒰              m_𝒰
                  ╲          ╱
                       𝒰
```

is commutative, or in other words that `m_𝒰` makes `𝒰` a commutative `O_S`-algebra. Conditions (i), (ii), (iii), (iv),
(v), (vi), (i)*, (ii)*, (iii)* and (v)* then also signify that `𝒰` is a cogroup in the category of commutative
`O_S`-algebras. Therefore, if moreover `𝒰` is a quasi-coherent `O_S`-module, then the affine `S`-scheme `Spec 𝒰` is a
commutative `S`-group scheme.

In this case, since the diagonal morphism `∆'` of `O_S[T, T^{-1}]` sends `T` to `T ⊗ T`, the morphisms of `S`-groups
from `Spec 𝒰` into `𝔾_{m, S}` (I 4.3.2) correspond bijectively to the morphisms of unital `O_S`-algebras

```text
φ : O_S[T, T^{-1}] ⟶ 𝒰
```

such that `(φ ⊗ φ) ∘ ∆' = ∆_𝒰 ∘ φ` (in this case, `ε_𝒰 ∘ φ` is the neutral element of `𝔾_{m, S}(S)`, i.e., the
augmentation `ε'`). Such a morphism `φ` is determined by the image `φ(T)`, which must be an invertible element `x` of
`𝒰` satisfying `∆_𝒰 x = x ⊗ x` and `ε_𝒰(x) = ε'(T) = 1`. One therefore has:

```text
Hom_{S-gr.}(Spec 𝒰, 𝔾_{m, S}) ≃ (Spec^* 𝒰)(S)
```

and since this formula remains valid after any base change, this gives: <!-- original page 433 -->

```text
Spec^* 𝒰 ≃ Hom_{S-gr.}(Spec 𝒰, 𝔾_{m, S}).
```

One has therefore obtained the

**Proposition 3.3.0.** *If `𝒰` is an `O_S`-coalgebra in commutative groups, quasi-coherent as an `O_S`-module, then the
affine `S`-scheme `G = Spec 𝒰` is a commutative `S`-group scheme, and one has an isomorphism of group `S`-functors*

<!-- label: III.VII_A.3.3.0 -->

```text
Spec^* 𝒰 ≃ Hom_{S-gr.}(G, 𝔾_{m, S}).
```

If one supposes moreover that `𝒰` is a locally free `O_S`-module of finite type, then, according to 3.1.2.1, the group
`S`-functor `Spec^* 𝒰` is represented by `Spec 𝒰^*`. One thus obtains the

**Proposition 3.3.1 (Cartier duality).** *The functor*

<!-- label: III.VII_A.3.3.1 -->

```text
𝒜(G) ↦ 𝒜(G)^* = Hom_{O_S-Mod.}(𝒜(G), O_S)
```

*induces a duality `(∗)` of the category of commutative, finite and locally free `S`-group schemes; it associates with
`G` the `S`-group `Hom_{S-gr.}(G, 𝔾_{m, S})`.*

[^VII_A-3-1]: A *duality* of a category `𝒞` is a pair `(D, φ)` consisting of a contravariant functor `D` from `𝒞` into
`𝒞` and a functorial isomorphism `φ : Id_𝒞 → DD` such that the isomorphisms `φD : D → DDD` and `Dφ^{-1} : DDD → D` are
inverses of each other.[^N.D.E-VII_A-38]

[^N.D.E-VII_A-38]: We have corrected `Dφ` to `Dφ^{-1}`.

## 4. "Frobeniuseries"

<!-- label: III.VII_A.4 -->
<!-- original page 434 -->

Let `p` be a fixed prime number and `(Sch/𝔽_p)` the category of schemes of characteristic `p`, i.e., of schemes above
the prime field `𝔽_p`. Following the general conventions of this Seminar, we identify `(Sch/𝔽_p)` with a subcategory of
`(Sch/𝔽_p)^∧` by means of the functor `h` of I 1.1. We likewise take advantage of the isomorphism from `Hom(h_X, F)`
onto `F(X)` defined in I 1.1 to identify these two sets whenever `X` is an `𝔽_p`-scheme and `F` an object of
`(Sch/𝔽_p)^∧`.

**Notations 4.0.**[^N.D.E-VII_A-39] *If `T` is an `𝔽_p`-scheme, a `T`-functor is a morphism `q : F → T` of
`(Sch/𝔽_p)^∧` having `T` as target; for every `T`-scheme `r : X → T`, the set of `T`-morphisms `X → F`, i.e., of
`𝔽_p`-morphisms `s : X → F` such that `q ∘ s = r`, will then be denoted `q(r)`, `q(X/T)`, `F(r)` or `F(X/T)` (or even
`F(X)` when no confusion will be possible with `Hom(h_X, F)`).*

<!-- label: III.VII_A.4.0 -->

[^N.D.E-VII_A-39]: We have added the numbering 4.0, for later references.

### 4.1.

<!-- label: III.VII_A.4.1 -->

For every scheme `S` of characteristic `p`, we denote by `fr(S)`, or simply `fr`, the endomorphism of `S` which induces
the identity on the underlying topological space of `S` and which associates `x^p` with a section `x` of `O_S` on an
open `U`.

Then the map `fr : S ↦ fr(S)` is an endomorphism of the identity functor of `(Sch/𝔽_p)`,[^N.D.E-VII_A-40] which implies
the following results. Let `E` be an `𝔽_p`-functor, i.e., an object of `(Sch/𝔽_p)^∧`; the map which to every
`𝔽_p`-scheme `S` associates the endomorphism `E(fr(S))` of `E(S)` is a functorial endomorphism of `E` which we shall
denote `fr(E)` or `fr`; this notation is compatible with the identification of `(Sch/𝔽_p)` with a subcategory of
`(Sch/𝔽_p)^∧`. Moreover, the map `E ↦ fr(E)` is an endomorphism of the identity functor of `(Sch/𝔽_p)^∧` (which we
shall again denote `fr`).[^N.D.E-VII_A-41]

[^N.D.E-VII_A-40]: i.e. for every morphism of `𝔽_p`-schemes `f : Y → X`, the diagram below is commutative:

    ```text
                       f
              Y  ────────→  X
       fr(Y)                fr(X)
                       f
              Y  ────────→  X.
    ```

[^N.D.E-VII_A-41]: One says that `fr(X)` is the "absolute" Frobenius morphism of `X`, to distinguish it from the
"relative" Frobenius morphism `Fr(X/S)` introduced below.

For every `𝔽_p`-scheme `S` and every `S`-functor `q : X → S`, we denote by `X^{(p/S)}` or `X^{(p)}` the inverse image
of `X` by the base change `fr(S)`:

```text
                  pr_X
       X^{(p/S)}  ──────→  X
           │                  │ q
           ▼                  ▼
                fr(S)
            S  ──────────→  S.
```

<!-- original page 465 -->

The commutative square

```text
                       fr(X)
              X  ──────────→  X
              │                  │
            q │                  │ q
              ▼       fr(S)       ▼
              S  ──────────→  S
```

induces an `S`-morphism, denoted `Fr(X/S)` (or simply `Fr`), from `X` into `X^{(p/S)}` such that
`fr(X) = pr_X ∘ Fr(X/S)`:

```text
              X
              │ ╲
              │  ╲  Fr(X/S)
              │   ╲
              │    ╲             fr(X)
              │     X^{(p/S)}  ──pr_X→  X
              │       │                  │
            q │       │ q^{(p/S)}        │ q
              ▼       ▼       fr(S)       ▼
              S       S       ─────→     S.
```

We shall say that `Fr(X/S)` is the *Frobenius morphism of `X` relative to `S`*; it is clear that the map
`Fr : X ↦ Fr(X/S)` is a functorial homomorphism.

[^N.D.E-VII_A-42] Let `r : T → S` be an `S`-scheme. For every `φ ∈ X(r) = Hom_S(T, X)` (cf. 4.0), one has a commutative
diagram:

```text
                  Fr(X/S)              pr_X
       X  ──────────────→  X^{(p/S)}  ──────→  X
        ╲                         │                  │
         ╲ φ                      │ q^{(p/S)}        │ q
       r  ╲                       │                  │
            ╲                     ▼      fr(S)       ▼
              T  ──────────────→  S  ──────────→  S.
```

[^N.D.E-VII_A-42]: We have expanded the original in what follows.

According to the definition of `X^{(p/S)}` as fibered product, `pr_X` induces a bijection:

```text
X^{(p/S)}(r) = Hom_S(T, X^{(p/S)})  ⥲  Hom_S(T, X) = X(fr(S) ∘ r).
```

On the other hand, `r ∘ fr(T) = fr(S) ∘ r`, since `fr` is an endomorphism of the identity functor. It follows that the
map `Fr(X/S)(r) : X(r) → X^{(p/S)}(r)` can be characterized by the commutativity of the following square:

```text
                  Fr(X/S)(r)
       X(r)  ────────────────→  X^{(p/S)}(r)

(†)   X(fr(T))                       ≀
                                          
       X(r ∘ fr(T))           X(fr(S) ∘ r).
```

<!-- original page 466 -->

For example, if `X` is the subscheme of `S` defined by a quasi-coherent ideal `ℐ`, then `X^{(p)}` is the subscheme of
`S` defined by the ideal `ℐ^{{p}}` generated by the `p`-th powers of the sections of `ℐ`; moreover, `Fr(X/S)` is then
the canonical immersion of `Spec(O_X / ℐ)` into `Spec(O / ℐ^{{p}})`.

### 4.1.1.

<!-- label: III.VII_A.4.1.1 -->

[^N.D.E-VII_A-43] Let `t : T → S` be a base change and `X_T = X ×_{q, t} T`. Consider the inverse image of `X_T` by
`fr(T)`:

```text
       (X_T)^{(p/T)}  ────→  X_T  ─────→  X
                                              │ q
                  fr(T)              t
              T  ──────→  T  ──→  S.
```

<!-- original page 436 -->

Since `t ∘ fr(T) = fr(S) ∘ t`, then `(X_T)^{(p/T)}` is identified with the inverse image of `X^{(p/S)}` by `t`; in
other words, one has a canonical isomorphism:

```text
X_T^{(p/T)}  ⥲  (X^{(p/S)})_T.
```

It is clear that, in this identification, `Fr(X_T / T)` is identified with the inverse image `Fr(X/S)_T` of `Fr(X/S)`.

[^N.D.E-VII_A-43]: We have expanded the original in what follows.

#### 4.1.1.1.

<!-- label: III.VII_A.4.1.1.1 -->

In particular, if `S` is the spectrum of the prime field `𝔽_p`, `X^{(p/S)}` is equal to `X` and `Fr(X/S)` to `fr(X)`.
Consequently, `X_T^{(p/T)}` is identified with `X_T` and `Fr(X_T / T)` with `fr(X)_T`.

For example, if `E` is a set and `E_T` the constant `T`-scheme of type `E`, one has `E_T^{(p/T)} ≃ E_T` and
`Fr(E_T / T) ≃ id_{E_T}`.

### 4.1.2.

<!-- label: III.VII_A.4.1.2 -->

The functor `X ↦ X^{(p/S)}` obviously commutes with products; it therefore transforms an `S`-group `G` into an
`S`-group `G^{(p/S)}`; moreover, since `Fr` is a functorial homomorphism, then

```text
Fr(G/S) : G ⟶ G^{(p/S)}
```

is a homomorphism of `S`-groups. We shall denote `Fr G` its kernel.

If `r : T → S` is a scheme above `S`, it follows from the diagram `(†)` of 4.1 that the value of `Fr G` at `r` is the
kernel of the homomorphism

```text
G(fr(T)) : G(r) ⟶ G(r ∘ fr(T)).
```

Now, when `T` is the scheme `I_R` of dual numbers over an `S`-scheme `R`, `fr(I_R)` factors as follows:

```text
I_R  ──can.→  R  ──fr(R)→  R  ──s→  I_R,
```

where `s` is the zero section. It follows that `(Fr G)(I_R)` contains the kernel `Lie(G/S)(R)` of the morphism
`G(s) : G(I_R) → G(R)`, and that one therefore has: `Lie(G/S) = Lie(Fr G / S)`.

### 4.1.3.

<!-- label: III.VII_A.4.1.3 -->
<!-- original page 437 -->

More generally, for every `S`-functor `X`, we define the `S`-functor `X^{(p^n)}` by recursion on `n` by means of the
formulas:

```text
X^{(p)} = X^{(p/S)}    and    X^{(p^n)} = (X^{(p^{n-1})})^{(p)}.
```

Similarly, `Fr^n(X/S)` or `Fr^n` denote the composed functorial homomorphism

```text
X ──Fr(X/S)→ X^{(p)} ──Fr(X^{(p)}/S)→ X^{(p²)} ──→ ··· ──→ X^{(p^{n-1})} ──Fr(X^{(p^{n-1})}/S)→ X^{(p^n)}.
```

One will note that, according to 4.1.1, `Fr(X^{(p)}/S)` coincides with `Fr(X/S)^{(p)}`, i.e., the following diagram is
commutative:

```text
       X^{(p)}  ────→  X

   Fr(X^{(p)}/S)         Fr(X/S)

       X^{(p²)}  ────→  X^{(p)}.
```

If `G` is a group `S`-functor, `G^{(p^n)}` is also one and `Fr^n(G/S)` is a homomorphism of group `S`-functors.

**Definition.** *We shall denote by `Fr^n G` the kernel of `Fr^n(G/S)` and we shall say that `G` is of height `⩽ n` if
`Fr^n(G/S)` is zero, i.e., if `Fr^n G = G`.*

**Lemma.** *The group subfunctor `Fr^n G` of `G` is characteristic, i.e., for every `S`-scheme `T`, every endomorphism
`φ` of the group `T`-functor `G_T` induces an endomorphism of `(Fr^n G)_T`.*

Indeed, since the construction of `G^{(p^n)}` and of `Fr^n(G/S)` commutes with base changes according to 4.1.1, one may
suppose `T = S`; in this case, the assertion follows from the fact that `Fr^n(G/S)` is a functorial homomorphism.

### 4.1.4. Examples.

<!-- label: III.VII_A.4.1.4 -->

a) Consider first an "abstract" abelian group `M` and the diagonalizable group `G = D_S(M)` of type `M` (I 4.4): for
every `S`-scheme `T`, `G(T)` is therefore the abelian group `Hom_{(Ab)}(M, Γ(T, O_T)^×)`. Since `G` is the inverse image
of the diagonalizable group `D(M)` over `𝔽_p`, `G^{(p)}` is identified with `G` and `Fr(G/S)(T)` is identified with the
endomorphism `x ↦ x^p` of `G(T)` (4.1.1). In particular, when `M` is equal to `ℤ`, one has `D_S(M) = 𝔾_{m, S}`, so that:

> `Fr 𝔾_{m, S}` is the `S`-group `μ_{p, S}` which to every `S`-scheme `T` associates the group of `p`-th roots of unity
> in `Γ(T, O_T)^*`.

b) Consider now a scheme `S` of characteristic `p` and a sheaf of modules `ℰ` on `S`. According to I 4.6.2, one has a
canonical isomorphism

```text
𝒲(ℰ)^{(p)} ≃ 𝒲(ℰ^{(p)}),
```

where `ℰ^{(p)}` is the inverse image of `ℰ` by `fr(S)`. For every `S`-scheme `π : T → S`, the map <!-- original page 438 -->
`Fr(𝒲(ℰ))(π)` is determined, according to 4.1 `(†)`, by the commutative triangle

```text
       Γ(T, π^* fr(S)^* ℰ)  ──can.~→  Γ(T, fr(T)^* π^* ℰ)
              ╲                                    ╱
               ╲                                  ╱
        Fr(𝒲(ℰ)/S)(π)                          f'
                  ╲                          ╱
                    Γ(T, π^* ℰ),
```

where `f'` is the map induced by `fr(T)`.

In particular, if `ℰ` is equal to `O_S`, `𝒲(ℰ)` is identified with the additive group `𝔾_{a, S}`. In this case, one has
`ℰ^{(p)} = ℰ = O_S` and the Frobenius morphism `Fr(𝔾_{a, S}/S)` sends `x ∈ Γ(T, O_T)` to `x^p`. So:

> `Fr 𝔾_{a, S}` is the `S`-group `α_{p, S}` which to every `S`-scheme `T` associates the group:
> `{ x ∈ Γ(T, O_T) | x^p = 0 }`.

c) One would see similarly that, for every quasi-coherent `O_S`-algebra `𝒜`, `(Spec 𝒜)^{(p)}` is identified with the
spectrum `Spec 𝒜^{(p)}` of the inverse image of `𝒜` by `fr(S)`. If `π` denotes the endomorphism `x ↦ x^p` of the sheaf
of rings `O_S`, one has therefore

```text
𝒜^{(p)} = 𝒜 ⊗_π O_S    [^N.D.E-VII_A-44]
```

and `Fr((Spec 𝒜)/S)` is induced by the morphism of `O_S`-algebras `𝒜 ⊗_π O_S → 𝒜` defined by `a ⊗_π x ↦ a^p x`.

[^N.D.E-VII_A-44]: `𝒜 ⊗_π O_S` denotes the `O_S`-algebra obtained by extension of scalars `π : O_S → O_S`, i.e., one
has: `ax ⊗_π 1 = a ⊗_π x^p`, and `x · (a ⊗_π 1) = a ⊗_π x`.

For every quasi-coherent `O_S`-module `ℰ`, finally, one has canonical isomorphisms

```text
𝒱(ℰ)^{(p)} ≃ 𝒱(ℰ^{(p)})    and    𝒮(ℰ)^{(p)} ≃ 𝒮(ℰ^{(p)}),
```

where `𝒮(ℰ)` denotes the symmetric algebra of the `O_S`-module `ℰ`.

<!-- original page 439 -->

d) Let `𝒰` be an `O_S`-coalgebra (3.1) and `T` a scheme of characteristic `p`. If `𝒰^{(p/S)}` or `𝒰^{(p)}` denote the
inverse image of the coalgebra `𝒰` by `fr(S)`, one has as in b) a canonical isomorphism:

```text
(Spec^* 𝒰)^{(p)} ≃ Spec^* 𝒰^{(p)}.
```

If `𝒰` is a coalgebra in groups, the value of `Fr(Spec^* 𝒰)`, i.e., of the kernel of the Frobenius morphism
`Spec^* 𝒰 → (Spec^* 𝒰)^{(p)}`, for an `S`-scheme `T` is therefore the set of elements `γ` of

```text
(Spec^* 𝒰)(T) = { x ∈ Γ(T, 𝒰_T) | ε_{𝒰_T}(x) = 1, ∆_{𝒰_T} x = x ⊗ x }
```

such that the image in `Γ(T, 𝒰_T ⊗_{fr(T)} O_T)` of the element `γ ⊗_{fr(T)} 1` of `Γ(T, 𝒰_T) ⊗_{fr(T)} O(T)` is equal
to `1`.

### 4.2.

<!-- label: III.VII_A.4.2 -->
<!-- original page 440 -->

[^N.D.E-VII_A-45] We shall now occupy ourselves with a construction close to the preceding one: let `S` be a scheme of
characteristic `p`, `X` an `S`-scheme and `X^{p_S}` the product in the category `(Sch/S)` of `p` copies of `X`.

[^N.D.E-VII_A-45]: For the content of nos 4.2 and 4.3, one may also consult [DG70], § IV.3, nos 4–6.

We then denote by `U_p(X)` the open subscheme of `X^{p_S}` which is the union of the products `U^{p_S}`, when `U` ranges
over the affine opens of `X`. A point `x` of `X^{p_S}` therefore belongs to `U_p(X)` if and only if the projections
`pr_i x` of `x` onto the factors of `X^{p_S}` belong to a common affine open of `X`. For example, if every finite part
of `X` is contained in an affine open, one has `U_p(X) = X^{p_S}`.

The symmetric group `𝔖_p` of order `p` operates on `X^{p_S}` by permutation of factors and leaves stable the open
`U_p(X)`. We shall call the *`p`-fold symmetric product of `X`* and we shall denote `Σ^p X` the quotient of `X^{p_S}` by
`𝔖_p` in the category of ringed spaces. Let `q(X)`, or simply `q`, be the canonical projection `X^{p_S} → Σ^p X`.

Then `q` maps `U_p(X)` onto an open `V_p(X)` of the symmetric product, which one may describe as follows (cf. V 4.1).
The structure sheaf of `Σ^p X` induces on `V_p(X)` a scheme structure; the morphism `q'(X) : U_p(X) → V_p(X)` induced
by `q(X)` is affine and even integral; when `U` ranges over the affine opens of `X` which project into an affine open
`V` of `S` varying, the `Σ^p U` form an affine covering of `V_p(X)`; if `R` <!-- original page 441 --> denotes the
affine algebra of `V` and `A` that of `U`, `Σ^p U` has as affine algebra the subalgebra `Σ^p A` of `⨂^p_R A` formed by
the symmetric tensors.

Consider now the diagonal morphism `δ` of `X` into `U_p(X)`. If `V = Spec R` is an affine open of `S` and `U = Spec A`
an affine open of `X` above `V`, the restriction of `δ` to `U` is defined by the algebra morphism

```text
η : ⨂^p_R A ⟶ A,    a_1 ⊗ ··· ⊗ a_p ↦ a_1 a_2 ··· a_p.
```

One therefore has, if `N` is the symmetrization operator:

```text
η(N(a_1 ⊗ ··· ⊗ a_p)) = η(∑_{σ ∈ 𝔖_p} a_{σ(1)} ⊗ ··· ⊗ a_{σ(p)}) = p! a_1 ··· a_p = 0.
```

In other words, `η` vanishes on the subspace `N(⨂^p_R A)` of `Σ^p A` formed by the symmetrized tensors. Moreover, if `f`
is a symmetric tensor, one has obviously `N(f a) = f N(a)`, which shows that `N(⨂^p_R A)` is an ideal of `Σ^p A`. We
shall henceforth denote

```text
U^{[p/S]} = Spec(Σ^p A / N(⨂^p_R A));
```

it is a closed subscheme of `Σ^p(U) = V_p(U)`. The union of the `U^{[p/S]}`, when `U` ranges over the affine opens of
`X` which project into a varying affine open `V` of `S`, is a closed subscheme of `V_p(X)`, denoted `X^{[p/S]}`.

Moreover, if `i(X)` denotes the inclusion of `X^{[p/S]}` into `V_p(X)`, we have just seen that `q'(X) ∘ δ` factors
through `X^{[p/S]}`, whence a morphism `F^{[p]}(X/S) : X → X^{[p/S]}`:[^N.D.E-VII_A-46]

[^N.D.E-VII_A-46]: In the original, this morphism (resp. the relative Frobenius morphism) was denoted `F'` (resp. `F`).

<!-- original page 470 -->

```text
                                   δ(X)
       X^{p_S}  ⊃  U_p(X)  ←──────────  X

   q(X)             q'(X)            F^{[p]}(X/S)

                                   i(X)
       Σ^p(X)  ⊃  V_p(X)  ←──────────  X^{[p/S]}.
```

It is clear that `X^{[p/S]}` is functorial in `X` and that the map `F^{[p]} : X ↦ F^{[p]}(X/S)` is a functorial
homomorphism.

### 4.2.1.

<!-- label: III.VII_A.4.2.1 -->

The schemes `X^{[p/S]}` and `X^{(p/S)}` are obviously related: let `V` be an affine open of `S` with affine ring `R` and
`U` an affine open of `X` above `V`; let `A` be the affine algebra of `U`. If `π` denotes the endomorphism `x ↦ x^p` of
`R`, then `U^{(p/S)}` has `A ⊗_π R` as affine algebra. One verifies moreover that the map

```text
a ⊗_π λ ↦ (λ a ⊗ ··· ⊗ a    mod    N(⨂^p_R A))
```

defines a morphism of `R`-algebras from `A ⊗_π R` into `Σ^p A / N(⨂^p_R A)`, and the latter induces a morphism
`φ(U) : U^{[p/S]} → U^{(p/S)}` such that `φ(U) ∘ F^{[p]}(U/S) = Fr(U/S)`.

"Gluing the pieces", one then obtains a commutative triangle

```text
                              X
                       ╱           ╲
              F^{[p]}(X/S)         Fr(X/S)
                  ╱                   ╲
                ╱                       ╲
              X^{[p/S]}  ──────φ(X)────→  X^{(p/S)}.
```

For example, if `X` is the subscheme of `S` defined by a quasi-coherent ideal `ℐ`, `F^{[p]}(X/S)` is identified with
the identity morphism of `X`, so that `φ(X)` is the canonical immersion of `Spec(O_S / ℐ)` into `Spec(O_S / ℐ^{{p}})`.
One thus sees that `φ(X)` is not an isomorphism in general.

However, when `M` is a free `R`-module, it is clear that the map

```text
M ⊗_π R ⟶ Σ^p M / N(⨂^p_R M),    m ⊗_π λ ↦ (λ m ⊗ ··· ⊗ m    mod    N(⨂^p_R M))
```

is bijective; this map therefore remains bijective when `M` is `R`-flat, because every flat module is a filtered direct
limit of free modules (Lazard[^VII_A-4-1] [^N.D.E-VII_A-47]). It follows that

> `φ(X) : X^{[p/S]} → X^{(p/S)}` is an isomorphism if `X` is a flat `S`-scheme.

[^VII_A-4-1]: D. Lazard, C. R. Acad. Sc. Paris 258, 1964, p. 6313–6316.

[^N.D.E-VII_A-47]: See also: D. Lazard, Bull. Soc. Math. France 97 (1969), 81–128, or: [BAlg], X § 1.6, Th. 1.

### 4.3.

<!-- label: III.VII_A.4.3 -->
<!-- original page 471 -->

Consider finally an `S`-group scheme `G` in abelian groups. Then the composed morphism
`μ(G) : U_p(G) ↪ G^{p_S} → G`, which is defined by the multiplication, factors through `V_p(G)`, i.e., there exists a
morphism `ν(G) : V_p(G) → G` such that `ν(G) ∘ q'(G) = μ(G)`, so that one has the following commutative diagram:

```text
                          μ(G)                δ(G)
       G  ←──────────  U_p(G)  ←──────────  G
        ╲                  │                  │
         ╲ ν(G)             │                  │ F^{[p]}(G/S)
          ╲                 │ q'(G)            │
                            ▼                  ▼
                          V_p(G)  ←──────  G^{[p/S]}
                                  i(G)
        Ver(G/S)                                Fr(G/S)
                                          ╲       ╱
                                            φ(G)
                                              ▼
                                          G^{(p/S)}.
```

<!-- original page 442 -->

When `G` is `S`-flat, `φ(G)` is an isomorphism and one can define a morphism (called the *Verschiebung*)

```text
Ver(G/S) : G^{(p/S)} ⟶ G
```

by means of the formula `Ver(G/S) = ν(G) ∘ i(G) ∘ φ(G)^{-1}`. When `G` ranges over `S`-flat group schemes in abelian
groups, the map `Ver : G ↦ Ver(G/S)` is obviously a functorial homomorphism; consequently, `Ver(G/S)` is a group
homomorphism. For every `S`-scheme `T` finally, the composed map

```text
G(T) ──δ(G)(T)→ U_p(G)(T) ──μ(G)(T)→ G(T)
```

sends `x ∈ G(T)` to `p · x`. We may write `p · id_G` instead of `μ(G) ∘ δ(G)`, thus obtaining the classical formula:

```text
(∗)                       Ver(G/S) ∘ Fr(G/S) = p · id_G.
```

**Examples 4.3.1.**

<!-- label: III.VII_A.4.3.1 -->

(a) When `G` is a constant `S`-scheme in abelian groups, we know that `Fr(G/S)` is identified with the identity morphism
of `G` (cf. 4.1.1.1). One therefore has `Ver(G/S) = p id_G`.

(b) When `G` is the diagonalizable `S`-group of type `M`, `Fr(G/S)` is equal to `p id_G` according to 4.1.4 (a); one
then sees easily that `Ver(G/S)` is the identity morphism of `G`.

(c) When `ℰ` is a flat `O_S`-module and `G` is the `S`-group `𝒱(ℰ)`, the morphism `Ver(G/S)` is zero, as is `p · id_G`.
One will see in Exposé VII_B that a commutative algebraic group `G` over a field `k` is "unipotent" if and only if the
composed homomorphism

```text
G^{(p^n)} ──Ver(G^{(p^{n-1})}/S)→ G^{(p^{n-1})} ──→ ··· ──→ G^{(p)} ──Ver(G/S)→ G
```

<!-- original page 443 -->

is zero for some `n` (one has set `G^{(p^n)} = (G^{(p^{n-1})})^{(p)}`, cf. 4.1.3).[^N.D.E-VII_A-48]

[^N.D.E-VII_A-48]: Since this does not appear explicitly in VII_B, one refers to [DG70], § IV.3, Prop. 4.11.

### 4.3.2.

<!-- label: III.VII_A.4.3.2 -->

Since the map `Ver : G ↦ Ver(G/S)` is a functorial homomorphism when `G` ranges over `S`-flat group schemes in
commutative groups, the square

```text
                          Ver(G/S)
       G^{(p)}  ──────────────────→  G

   Fr(G/S)^{(p)}                            Fr(G/S)
                                
                       Ver(G^{(p)}/S)
       G^{(p²)}  ──────────────────→  G^{(p)}
```

is commutative, where `Fr(G/S)^{(p)}` denotes the inverse image of `Fr(G/S)` by the base change `fr(S)`. According to
4.1.1, one has `Fr(G/S)^{(p)} = Fr(G^{(p)}/S)`, so, according to 4.3 `(∗)` applied to `G^{(p)}`, one obtains:

```text
(∗∗)        Fr(G/S) ∘ Ver(G/S) = Ver(G^{(p)}/S) ∘ Fr(G^{(p)}/S) = p · id_{G^{(p)}}.
```

### 4.3.3.

<!-- label: III.VII_A.4.3.3 -->
<!-- original page 444 -->

Suppose finally that `G` is a commutative, finite and locally free `S`-group; let `𝒜` be the `O_S`-affine algebra of
`G` and `π` the endomorphism of the sheaf of rings `O_S` which sends a section `x` of `O_S` to `x^p`.[^N.D.E-VII_A-49]
We denote by `Σ^p 𝒜` the subalgebra of `⨂^p_{O_S} 𝒜` formed by the sections invariant under the action of the symmetric
group, by `i(𝒜)` the inclusion of `Σ^p 𝒜` into the tensor product. Let `∆_p(𝒜) : 𝒜 → ⨂^p_{O_S} 𝒜` be the morphism
obtained by iterating the diagonal morphism of the coalgebra `𝒜` (it corresponds to the morphism of multiplication
`U_p(G) = G^{p_S} → G`); according to the beginning of paragraph 4.3, `∆_p(𝒜)` factors through `Σ^p 𝒜`, i.e., it induces
a morphism

```text
a(𝒜) : 𝒜 ⟶ Σ^p 𝒜
```

such that `i(𝒜) ∘ a(𝒜) = ∆_p(𝒜)`.

[^N.D.E-VII_A-49]: We have modified the order, by first introducing the objects appearing in the diagram that follows.

On the other hand, let `S^p(𝒜)` be the degree-`p` component of the symmetric algebra of `𝒜` and
`q(𝒜) : ⨂^p_{O_S} 𝒜 → S^p(𝒜)` the canonical projection. The multiplication `m_p(𝒜) : ⨂^p_{O_S} 𝒜 → 𝒜` factors through
`S^p(𝒜)`, i.e., it induces a map

```text
b(𝒜) : S^p(𝒜) ⟶ 𝒜
```

such that `b(𝒜) ∘ q(𝒜) = m_p(𝒜)`.

Since `Σ^p 𝒜` is the affine algebra of `V_p(𝒜)`, then, according to the beginning of 4.3 again, the composed morphism
`i(G) ∘ φ(G)^{-1}` induces an algebra homomorphism

```text
r(𝒜) : Σ^p 𝒜 ⟶ 𝒜 ⊗_π O_S;
```

this homomorphism vanishes on the sections of the form

```text
∑_{σ ∈ 𝔖_p} a_{σ(1)} ⊗ ··· ⊗ a_{σ(p)}
```

<!-- original page 473 -->

and sends `a ⊗ ··· ⊗ a` to `a ⊗_π 1`. Similarly, `j(𝒜)` is the morphism of `O_S`-modules `a ⊗_π 1 ↦ q(a ⊗ ··· ⊗ a)`. One
thus obtains the commutative diagram:

```text
                       ∆_p(𝒜)                       m_p(𝒜)
       𝒜  ────────────→  ⨂^p_{O_S} 𝒜  ──────────────→  𝒜
        ╲                  ▲     │                       ▲
         ╲ a(𝒜)      i(𝒜) │     │ q(𝒜)         b(𝒜) ╱
          ╲                │     ▼                     ╱
(𝒜)        Σ^p 𝒜                  S^p(𝒜)
              ╲                                       ╱
               ╲ r(𝒜)                          j(𝒜) ╱
                ╲                                  ╱
                   𝒜 ⊗_π O_S.
```

The composition `r(𝒜) ∘ a(𝒜)` is associated with the Verschiebung morphism `Ver(G/S)`, while `b(𝒜) ∘ j(𝒜)` is
associated with the Frobenius morphism `Fr(G/S)`.

The commutative diagram `(𝒜)` above is self-dual; let `D` indeed be the functor which to every `O_S`-module `ℳ`
associates the dual `O_S`-module `Hom_{O_S}(ℳ, O_S)`; it is clear that the image of the diagram `(𝒜)` by the functor
`D` is none other than the diagram `(D𝒜)`, the morphisms `Dr(𝒜)`, `Da(𝒜)`, `Dj(𝒜)` and `Db(𝒜)` being identified
respectively with `j(D𝒜)`, `b(D𝒜)`, `r(D𝒜)` and `a(D𝒜)`. According to 3.3.1, one therefore sees that:

> In the category of commutative, finite and locally free `S`-groups, Cartier duality interchanges the Frobenius
> morphism and the Verschiebung.[^N.D.E-VII_A-50]

[^N.D.E-VII_A-50]: See also [DG70], § IV.3, 4.9.

## 5. Restricted `p`-Lie algebras

<!-- label: III.VII_A.5 -->
<!-- original page 445 -->

Let us first recall some results from the *Séminaire Sophus Lie*.[^N.D.E-VII_A-51]

[^N.D.E-VII_A-51]: cf. P. Cartier, Exemples d'hyperalgèbres, Sém. Sophus Lie 1955/56, Exp. 3 (accessible on the Numdam
site: http://www.numdam.org).

### 5.1.

<!-- label: III.VII_A.5.1 -->

Let `p` be a prime number, `R` a commutative ring of characteristic `p` and `A` an associative `R`-algebra, but not
necessarily commutative. If `a` and `b` are two elements of `A`, we set `[a, b] = ab − ba` and `a · b = L_a(b) = R_b(a)`.
One then has:

```text
(ad x^p)(y) = [x^p, y] = (L_x^p − R_x^p)(y) = (L_x − R_x)^p(y) = (ad x)^p(y)
```

whence Jacobson's first formula:

```text
(i)                        ad(x^p) = (ad x)^p.
```

If `a_1, …, a_p` are `p` arbitrary elements of `A`, then, denoting by `N` the symmetrization operator (cf. 4.2), one has
the equalities:

```text
(∗)    N(a_1 ⊗ ··· ⊗ a_p) = ∑_σ a_{σ(1)} ··· a_{σ(p)} = ∑_τ [a_{τ(1)} [a_{τ(2)} [··· [a_{τ(p-1)}, a_p] ···]]]
```

<!-- original page 474 -->

where `σ` ranges over the permutations of `p` letters and `τ` over those of `(p − 1)` letters. Indeed, the last term
equals

```text
∑_τ ∑_{r=0}^{p-1} ∑_{i_1 < ··· < i_r} (−1)^s a_{τ(i_1)} a_{τ(i_2)} ··· a_{τ(i_r)} a_p a_{τ(j_s)} ··· a_{τ(j_1)}
```

where `τ` ranges over the permutations of `p − 1` letters, `i_1, …, i_r` the strictly increasing sequences of integers
of the interval `[1, p − 1]` and where `j_1, …, j_s` denotes the strictly increasing sequence whose values are the
integers of `[1, p − 1]` different from `i_1, …, i_r`. For a fixed value of `r`, the sum of the terms
`(−1)^s a_{τ(i_1)} ··· a_{τ(i_r)} a_p a_{τ(j_s)} ··· a_{τ(j_1)}` obviously equals

```text
(−1)^s (p−1 choose s) ∑_ρ a_{ρ(1)} ··· a_{ρ(r)} a_p a_{ρ(r+1)} ··· a_{ρ(p−1)}
```

<!-- original page 446 -->

where `ρ` ranges over the permutations of `p − 1` letters. Now `(−1)^s (p−1 choose s) = 1` in `𝔽_p`, since in `𝔽_p[x]`
(`x` an indeterminate) one has: `(x − 1)^p = x^p − 1 = (x − 1)(x^{p−1} + ··· + 1)` and therefore
`(x − 1)^{p−1} = x^{p−1} + ··· + 1`. This proves `(∗)`.

On the other hand, if `x_0` and `x_1` are two elements of `A`, one has

```text
(x_0 + x_1)^p = x_0^p + x_1^p + ∑ x_{z(1)} x_{z(2)} ··· x_{z(p)},
```

where `z` ranges over the non-constant maps from `[1, p]` into `{0, 1}`. One deduces

```text
(x_0 + x_1)^p = x_0^p + x_1^p + ∑_{0 < r < p} 1/(r!(p−r)!) N(x_0, …, x_0, x_1, …, x_1)
```

(with `r` factors `x_0` and `p−r` factors `x_1`).[^N.D.E-VII_A-52] Now, according to `(∗)`, one has:

```text
N(x_0, …, x_0, x_1, …, x_1) = r! (p − 1 − r)! ∑_t [x_{t(1)} x_{t(2)} ··· x_{t(p−1)}, x_1] ···
```

(with `r` factors `x_0` and `p−r` factors `x_1`), where `t` ranges over the maps `[1, p−1] → {0, 1}` taking the value
`0` exactly `r` times. From this one deduces Jacobson's second formula:

```text
(ii)    (x_0 + x_1)^p = x_0^p + x_1^p − ∑_{0 < r < p} ∑_t (1/r) [x_{t(1)} x_{t(2)} ··· x_{t(p−1)}, x_1] ···
```

where `t` ranges over the maps `[1, p−1] → {0, 1}` taking the value `0` exactly `r` times.

[^N.D.E-VII_A-52]: We have inserted the explanation that follows, taken from [DG70], § II.7, 3.2.

### 5.2.

<!-- label: III.VII_A.5.2 -->

Let now `𝔤` be an `R`-Lie algebra. One says that a map `x ↦ x^{(p)}` from `𝔤` into `𝔤` makes `𝔤` a *restricted `p`-Lie
algebra* over `R` if the following conditions are satisfied:

   (0) `(λ x)^{(p)} = λ^p · x^{(p)}`, for `λ ∈ R`, `x ∈ 𝔤`

   (i) `ad x^{(p)} = (ad x)^p`, for `x ∈ 𝔤`

   (ii) `(x_0 + x_1)^{(p)} = x_0^{(p)} + x_1^{(p)} − ∑_{0 < r < p} ∑_t (1/r) [x_{t(1)} x_{t(2)} ··· x_{t(p−1)}, x_1] ···`

<!-- original page 447 -->

where `t` ranges over the maps `[1, p−1] → {0, 1}` taking the value `0` exactly `r` times (`x_0, x_1 ∈ 𝔤`). The map
`x ↦ x^{(p)}` will then be called the "*symbolic `p`-th power*".

For example, if `A` is an associative `R`-algebra, we saw in 5.1 that one obtains a `p`-Lie algebra, which we shall
denote `A_{Lie}`, by taking the `R`-module underlying `A` and setting, for `x, y ∈ A`,

```text
[x, y] = xy − yx    and    x^{(p)} = x^p.
```

We shall say that `A_{Lie}` is the `p`-Lie algebra underlying `A`.

In what follows we shall consider mostly sub-`p`-Lie algebras of `p`-algebras of the form `A_{Lie}`; here is an example:
let `S` be a scheme of characteristic `p > 0` and `X` an `S`-scheme. Recall that a derivation of `X` over `S` is an
endomorphism `D` of the sheaf of abelian groups `O_X` such that

```text
D(λ · s) = λ · D(s)    and    D(st) = (Ds) t + s (Dt)
```

when `λ` and `s, t` range over the sections of `O_S` and of `O_X` on opens such that the formulas make sense. Leibniz's
formula

```text
D^n(st) = ∑_{i=0}^n (n choose i) (D^i s)(D^{n−i} t)
```

shows that `D^p` is again a derivation of `X` over `S`, taking into account the equality `(p choose i) ≡ 0 (mod p)`
for `i ≠ 0, p`. It follows that:

> The algebra `Dér_{X/S}` of derivations of `X` over `S` is a sub-`p`-Lie algebra of the `Γ(S, O_S)`-algebra of
> differential operators of `X` over `S`.

#### 5.2.1.

<!-- label: III.VII_A.5.2.1 -->

If `𝔤` and `𝔥` are two `p`-Lie algebras, a *homomorphism* `h : 𝔤 → 𝔥` is an `R`-linear map from `𝔤` into `𝔥` such that
`h([x, y]) = [h(x), h(y)]` and `h(x^{(p)}) = h(x)^{(p)}` if `x, y ∈ 𝔤`. The composition of two homomorphisms is again a
homomorphism, so that we may speak of the *category of `p`-Lie algebras* over `R`.

If `(X, R)` is a ringed space, we shall say that an `R`-module `𝔤` is equipped with a structure of `p`-Lie algebra over
`R` if, for every open `U`, `Γ(U, 𝔤)` is equipped with a structure of `p`-Lie algebra over `Γ(U, R)` <!-- original page 448 -->
and if the restrictions are homomorphisms.

### 5.3.

<!-- label: III.VII_A.5.3 -->

We are now interested in the left adjoint functor to the functor `A ↦ A_{Lie}` of 5.2. Let `𝔤` be a `p`-Lie algebra over
the ring `R` of characteristic `p`, `U(𝔤)` the enveloping algebra of the Lie algebra underlying `𝔤` (cf. [BLie], I § 2.1)
and `i_𝔤` (or simply `i`) the canonical map `𝔤 → U(𝔤)`.

Let `A` be a unital associative `R`-algebra. One knows that, for every Lie algebra homomorphism `φ : 𝔤 → A_{Lie}` there
exists a unique homomorphism of unital `R`-algebras `ψ : U(𝔤) → A` such that `ψ ∘ i = φ`. Moreover, `φ` is a
`p`-Lie algebra homomorphism if and only if `ψ` vanishes on the elements `i(x)^p − i(x^{(p)})`, when `x` ranges over `𝔤`.

**Definition.** *One denotes by `U^R_p(𝔤)` or simply `U_p(𝔤)` the quotient of `U(𝔤)` by the two-sided ideal generated by
the elements `i(x)^p − i(x^{(p)})`, and `j_𝔤` (or simply `j`) the map `𝔤 → U_p(𝔤)` composed of `i : 𝔤 → U(𝔤)` and the
canonical map `U(𝔤) → U_p(𝔤)`. One says that `U_p(𝔤)` is the* restricted enveloping algebra *of `𝔤`.*

According to what precedes, one has the

**Proposition.** *For every unital associative `R`-algebra and every `p`-Lie algebra morphism `φ : 𝔤 → A_{Lie}`, there
exists a unique homomorphism of unital algebras `ψ : U_p(𝔤) → A` such that `ψ ∘ j = φ`. In other words, the functor
`𝔤 ↦ U_p(𝔤)` is left adjoint to the forgetful functor `A ↦ A_{Lie}`.*

#### 5.3.1.

<!-- label: III.VII_A.5.3.1 -->

With the notations of 5.3, set now `β(x) = i(x)^p − i(x^{(p)})`. For every element `y` of `𝔤`, one has, according to 5.1
(i) and 5.2 (i):

```text
β(x) i(y) = i(y) β(x) + [β(x), i(y)]
          = i(y) β(x) + (ad i(x))^p i(y) − i((ad x)^p y)
          = i(y) β(x),
```

<!-- original page 449 -->

so `β(x)` belongs to the center of `U(𝔤)`; in particular, the left ideal generated by the elements `β(x)` is already
two-sided.

On the other hand, it is clear that `β(λ x) = λ^p β(x)`, for `λ ∈ R`, and it follows from 5.1 (ii) and 5.2 (ii) that, for
`x, y ∈ 𝔤`,

```text
β(x + y) = β(x) + β(y).
```

In particular, if `(x_α)` is a family of generators of the `R`-module `𝔤`, the left ideal generated by the elements
`β(x)` is already generated by the `β(x_α)`.

#### 5.3.2. Proposition.

<!-- label: III.VII_A.5.3.2 -->

[^N.D.E-VII_A-53] *Let `𝔤` be an `R`-Lie algebra whose underlying `R`-module is free with basis `(x_α)`. Then the
structures of `p`-Lie algebra on `𝔤` correspond bijectively to the families `(y_α)` of `𝔤` such that
`ad y_α = (ad x_α)^p`.*

[^N.D.E-VII_A-53]: In this paragraph, we have modified the order, first stating the result, then detailing the proof.

Indeed, if `𝔤` is equipped with a structure of `p`-Lie algebra `x ↦ x^{(p)}`, then according to 5.2 (i) and (0), (ii),
the `y_α = x_α^{(p)}` satisfy `ad y_α = (ad x_α)^p`, and determine the `p`-Lie algebra structure.

Let us prove the converse. Since `𝔤` is a free `R`-module, the canonical map `i : 𝔤 → U(𝔤)` is injective, according to
the Poincaré–Birkhoff–Witt theorem (cf. [BLie], I § 2.7), so one can identify `𝔤` with an `R`-submodule of `U(𝔤)`.
Suppose that `(y_α)` is a family of elements of `𝔤` such that `ad y_α = (ad x_α)^p`. Let `π` be the map `r ↦ r^p` from
`R` into `R`, and let `𝔤 ⊗_π R` be the `R`-Lie algebra obtained by extension of scalars `π : R → R`.[^N.D.E-VII_A-54]

[^N.D.E-VII_A-54]: i.e., `x r ⊗_π 1 = x ⊗_π r^p` and `r · (x ⊗_π 1) = x ⊗_π r`, for `x ∈ 𝔤`, `r ∈ R`.

There then exists an `R`-linear map `γ` from `𝔤 ⊗_π R` into `U(𝔤)` which sends `x_α ⊗_π 1` to `x_α^p − y_α`; moreover,
since one has, for every `x ∈ 𝔤`,

```text
(ad x_α^p)(x) = (ad x_α)^p(x) = (ad y_α)(x),
```

`γ` maps `𝔤 ⊗_π R` into the center of `U(𝔤)`. Set, for every `x ∈ 𝔤`:

```text
x^{(p)} = x^p − γ(x ⊗_π 1).
```

Then, for every `α`, one has `x_α^{(p)} = y_α`. If `x = ∑ λ_α x_α`, one deduces from 5.1 (ii) (by induction on the number
of indices `α` such that `λ_α ≠ 0`), that

<!-- original page 477 -->

```text
x^p − ∑_α λ_α^p x_α^p ∈ 𝔤;
```

denoting this element by `z`, one then has `x^{(p)} = ∑ λ_α^p y_α + z` and therefore `x^{(p)} ∈ 𝔤`.

It is clear that the map `x ↦ x^{(p)}` satisfies `(λ x)^{(p)} = λ^p x^{(p)}`. Moreover, since `γ(x ⊗_π 1)` is central,
then `ad x^{(p)} = ad x^p` and therefore, according to Jacobson's first formula (5.1 (i)), one has

```text
ad x^{(p)} = (ad x)^p.
```

Finally, according to Jacobson's second formula (5.1 (ii)), the map `x ↦ x^{(p)}` satisfies condition (ii) of 5.2. It
therefore makes `𝔤` a `p`-Lie algebra. This proves the proposition.

#### 5.3.3. Proposition.

<!-- label: III.VII_A.5.3.3 -->

*Let `𝔤` be a `p`-Lie algebra over `R` whose underlying module is free with basis `(x_α)`. Then the map
`j : 𝔤 → U_p(𝔤)` is injective and, if one sets `z_α = j(x_α)`, then `U_p(𝔤)` has as basis the monomials*

```text
∏_α z_α^{n_α}    where    0 ⩽ n_α < p,
```

*(the `n_α` are assumed to be zero except for a finite number of them; one assumes the basis to be totally ordered and
the products to be performed in increasing order).*

Indeed, identify `𝔤` with a submodule of the enveloping algebra `U(𝔤)` by means of the canonical map `i`. For every
family `n = (n_α)` of natural integers, zero except for a finite number of them, set

```text
|n| = ∑_α n_α    and    x^n = ∏_α x_α^{n_α}.
```

<!-- original page 450 -->

Writing `n_α = m_α + p ℓ_α`, with `0 ⩽ m_α < p`, set also

```text
T_n = ∏_α x_α^{m_α} β(x_α)^{ℓ_α}
```

where `β(x) = x^p − x^{(p)}` is the map `𝔤 → U(𝔤)` defined in 5.3.1.

For every `r ∈ ℕ`, denote by `U_r` the sub-`R`-module of `U(𝔤)` generated by the `x^n` such that `|n| ⩽ r`. Since the
graded ring `⨁_r U_r / U_{r−1}` is commutative (cf. [BLie], I § 2.6), one sees that, for every `n`:

```text
T_n − ∏_α x_α^{n_α} ∈ U_{|n| − 1}.
```

For every `s ∈ ℕ`, the `x^n` such that `|n| = s` form, according to the Poincaré–Birkhoff–Witt theorem (loc. cit., § 2.7),
a basis of `U_s / U_{s−1}`, and therefore the same holds for the `T_n` such that `|n| = s`.

Therefore, when `s = |n|` varies, the `T_n` form a basis of `U(𝔤)`. Now the kernel `J` of the canonical map
`U(𝔤) → U_p(𝔤)` is the left ideal of `U(𝔤)` generated by the central elements `β(x_α)` (5.3.1). Consequently, the `T_n`
such that `ℓ = (ℓ_α) ≠ 0` <!-- original page 478 --> form a basis of `J`, and the `T_n` such that `n_α < p` for every
`α`, form a basis of `U_p(𝔤) = U(𝔤) / J`.

#### 5.3.3 bis.

<!-- label: III.VII_A.5.3.3-bis -->

Let `𝔤` be a `p`-Lie algebra over `R` and `f : R → R'` an extension of the base ring. I claim that there exists on the
`R'`-module `R' ⊗_R 𝔤` a `p`-Lie algebra structure and only one such that

```text
(∗)    [λ ⊗ x, μ ⊗ y] = λμ ⊗ [x, y]    and    (λ ⊗ x)^{(p)} = λ^p ⊗ x^{(p)}.
```

It will follow, in particular, that the functor `𝔤 ↦ R' ⊗_R 𝔤` is left adjoint to the functor "restriction of scalars
from `R'` to `R`".

The uniqueness of the `p`-Lie algebra structure defined by `(∗)` being clear, let us prove existence. When `𝔤` is free
with basis `(x_α)` there exists, according to 5.3.2, one and only one `p`-Lie algebra structure on the Lie algebra
`R' ⊗_R 𝔤` such that

```text
(1 ⊗ x_α)^{(p)} = 1 ⊗ x_α^{(p)};
```

this structure is the one we seek.

When `𝔤` is an arbitrary `p`-Lie algebra, there exists a `p`-Lie algebra `L_0` free (as an `R`-module) and a surjective
homomorphism `q_0 : L_0 → 𝔤`; it suffices for example to take for `L_0` the `p`-Lie algebra `R ⊗_{𝔽_p} 𝔤`, where `𝔽_p`
denotes the prime field <!-- original page 451 --> of characteristic `p`, and for `q_0` the homomorphism
`λ ⊗ x ↦ λ x` (`𝔤` is free over `𝔽_p`!). The kernel of `q_0` is then a `p`-ideal of `L_0`, i.e., an ideal of the Lie
algebra `L_0` which is stable under the endomorphism `x ↦ x^{(p)}`; there is therefore also a `p`-Lie algebra `L_1` free
(as an `R`-module) and a homomorphism `q_1 : L_1 → L_0` whose image is `Ker q_0`, whence the exact sequence:

```text
L_1 ──q_1→ L_0 ──q_0→ 𝔤 ──→ 0.
```

One deduces from this an exact sequence of `R'`-Lie algebras

```text
R' ⊗_R L_1 ──R' ⊗_R q_1→ R' ⊗_R L_0 ──R' ⊗_R q_0→ R' ⊗_R 𝔤 ──→ 0.
```

Since `R' ⊗_R q_1` is manifestly a homomorphism of `p`-Lie algebras, the kernel of `R' ⊗_R q_0` is a `p`-ideal, so that
the symbolic `p`-th power operation of `R' ⊗_R L_0` induces by passage to the quotient a map from `R' ⊗_R 𝔤` into
`R' ⊗_R 𝔤` (use formula (ii) of 5.2); this last one equips `R' ⊗_R 𝔤` with the `p`-Lie algebra structure sought.

### 5.3.4.

<!-- label: III.VII_A.5.3.4 -->

The canonical map `j_𝔤 : 𝔤 → U_p(𝔤)` induces, for every extension `R → R'` of the base ring, a homomorphism

```text
R' ⊗_R j_𝔤 : R' ⊗_R 𝔤 ⟶ R' ⊗_R U_p(𝔤),
```

whence a homomorphism

```text
h : U_p(R' ⊗_R 𝔤) ⟶ R' ⊗_R U_p(𝔤)
```

such that `h ∘ j_{R' ⊗ 𝔤} = R' ⊗_R j_𝔤`. It obviously follows from the universal properties of `R' ⊗_R 𝔤` and the
restricted enveloping algebra that `h` is an isomorphism, which will allow us to identify `U_p(R' ⊗_R 𝔤)` with
`R' ⊗_R U_p(𝔤)`.

In particular, if `r` is an element of `R` and if `R'` is the localized ring `R_r`, one sees that `𝔤_r = R_r ⊗_R 𝔤` is
equipped canonically with a structure of `p`-Lie algebra over `R_r`, <!-- original page 452 --> so that the sheaf `𝔤̃`
on `Spec R` is a quasi-coherent `p`-Lie algebra on `Spec R`. Moreover, the restricted enveloping algebra
`U^{R_r}_p(𝔤_r)` is identified with `U^R_p(𝔤)_r`, so that the sheaf associated with the presheaf
`V ↦ U_p(Γ(V, 𝔤̃))` is quasi-coherent.

**Definition.** *More generally, if `S` is a scheme of characteristic `p` and `𝒢` a quasi-coherent `p`-Lie algebra on
`O_S`, the sheaf associated with the presheaf `V ↦ U_p(Γ(V, 𝒢))` is quasi-coherent; it will be denoted `𝒰_p(𝒢)` and
called the* restricted enveloping algebra *of `𝒢`. If `V` is affine, `U_p(Γ(V, 𝒢))` is identified with
`Γ(V, 𝒰_p(𝒢))`.*

### 5.4.

<!-- label: III.VII_A.5.4 -->

The universal character of `U_p(𝔤)` entails that `U_p(𝔤)` is functorial in `𝔤`: every homomorphism of `p`-Lie algebras
`φ : 𝔤 → 𝔥` induces a homomorphism of unital algebras `U_p(φ)` and only one such that `j_𝔥 ∘ φ = U_p(φ) ∘ j_𝔤`. Here are
some examples:

a) If `𝔥 = 0`, `U_p(𝔥)` is identified with the base ring and `U_p(φ)` is an algebra homomorphism
`ε_𝔤 : U_p(𝔤) → R` called the *augmentation*.

b) Now take for `𝔥` the algebra `𝔤°` opposite to `𝔤`, i.e., `𝔤°` has the same underlying module as `𝔤`, the same
symbolic `p`-th power, the bracket of two elements in `𝔤°` being the opposite of the bracket in `𝔤`. It is clear that we
can identify `U_p(𝔤°)` with the algebra opposite to `U_p(𝔤)`. Moreover, the isomorphism `x ↦ −x` of `𝔤` onto `𝔤°`
induces an isomorphism `c_𝔤` of `U_p(𝔤)` onto `U_p(𝔤°) ≃ U_p(𝔤)°`. One says that `c_𝔤` is the *antipode* of `U_p(𝔤)`.

c) Let finally `𝔣` and `𝔤` be two `p`-Lie algebras and `𝔥` the `p`-Lie algebra product `𝔣 × 𝔤` which has as underlying
`R`-module the direct product `𝔣 × 𝔤`, the bracket and the symbolic `p`-th power being defined by the formulas

```text
[(x, y), (x', y')] = ([x, x'], [y, y'])    and    (x, y)^{(p)} = (x^{(p)}, y^{(p)}).
```

If `h_1 : 𝔣 → 𝔨` and `h_2 : 𝔤 → 𝔨` are two `p`-Lie algebra homomorphisms <!-- original page 453 --> such that
`[h_1(x), h_2(y)] = 0` for every `x` of `𝔣` and every `y` of `𝔤`, the map `h_1 + h_2 : (x, y) → h_1(x) + h_2(y)` is a
`p`-Lie algebra homomorphism; conversely, every homomorphism from `𝔣 × 𝔤` into `𝔨` is of this type, which allows us to
characterize `𝔣 × 𝔤` as the solution of a universal problem. For example, the maps

```text
h_1 : x ↦ i_𝔣(x) ⊗ 1    and    h_2 : y ↦ 1 ⊗ i_𝔤(y)
```

induce a homomorphism `h_1 + h_2` from `𝔣 × 𝔤` into the `p`-Lie algebra underlying `U_p(𝔣) ⊗ U_p(𝔤)`. It follows from the
universal characters of `𝔣 × 𝔤` and of the restricted enveloping algebras that `h_1 + h_2` extends to an isomorphism:

```text
φ : U_p(𝔣 × 𝔤) ⥲ U_p(𝔣) ⊗ U_p(𝔤).
```

**Definition.** *If `𝔣 = 𝔤`, the diagonal map `δ : x ↦ (x, x)` of `𝔤` into `𝔤 × 𝔤` induces a homomorphism of `U_p(𝔤)`
into `U_p(𝔤 × 𝔤)`. We shall denote by `∆_𝔤` the composition of this homomorphism with the isomorphism
`φ : U_p(𝔤 × 𝔤) ⥲ U_p(𝔤) ⊗ U_p(𝔤)`.*[^N.D.E-VII_A-55]

[^N.D.E-VII_A-55]: i.e. `∆_𝔤(x) = x ⊗ 1 + 1 ⊗ x` for every `x ∈ 𝔤`; in particular, the comultiplication `∆_𝔤` is indeed
cocommutative …

One then sees easily that `∆_𝔤` and the multiplication of the algebra `U_p(𝔤)` make `U_p(𝔤)` an `R`-coalgebra in groups
(cf. 3.2) which has `ε_𝔤` as augmentation and `c_𝔤` as antipode.

### 5.5.

<!-- label: III.VII_A.5.5 -->

[^N.D.E-VII_A-56] Let now `S` be a scheme of characteristic `p`. First, if `𝒰` is an `O_S`-coalgebra in groups and `G`
the group `S`-functor `Spec^* 𝒰`, we saw (3.2.3) that, for every `T → S`, `(Lie G)(T)` is the Lie subalgebra of
`Γ(T, 𝒰_T)` formed by the primitive elements. Now, if `x` is such an element, one has
`∆(x^p) = x^p ⊗ 1 + 1 ⊗ x^p` (since `(p choose i) = 0 mod p` for `0 < i < p`), i.e. `x^p` is again a primitive element.
It follows, according to 5.1 and 5.2, that the map `x ↦ x^p` equips `(Lie G)(T)` with a structure of `O(T)`-`p`-Lie
algebra.

[^N.D.E-VII_A-56]: We have transformed § 5.4.1 of the original into this § 5.5: on the one hand, Proposition 5.5.1
combines the results of Section 5 and Proposition 3.2.3 and contains Lemma 7.3 of the original; on the other hand, the
proof of 5.5.3 (ii) takes up, in expanded form, that of the implication (i) ⇒ (ii) in Theorem 7.4 below.

Let now `ℒ` be an `O_S`-`p`-Lie algebra, quasi-coherent on `O_S`. When `V` ranges over the opens of `S`, the structures
of group coalgebras previously defined on the sets `U_p(Γ(V, ℒ))` induce on the associated sheaf, i.e., on the
restricted enveloping algebra `𝒰_p(ℒ)`, a structure of `O_S`-coalgebra in groups. Moreover, <!-- original page 480 -->
for every `S`-scheme `T`, one has an isomorphism `𝒰_p(ℒ_T) ⥲ 𝒰_p(ℒ)_T`.

Denote by `Prim 𝒰_p(ℒ)` the subpresheaf of `𝒰_p(ℒ)` associating with every open `V` the set of primitive elements of
`𝒰_p(ℒ)(V)`; one sees easily that this is a sheaf. When `V` ranges over the opens of `S`, the composed maps

```text
Γ(V, ℒ) ──j→ Prim U_p(Γ(V, ℒ)) ──→ Prim 𝒰_p(ℒ)(V)
```

define a morphism `ℒ → Prim 𝒰_p(ℒ)`, which we shall again denote `j` or `j_ℒ`, and this defines further a morphism of
`O_S`-`p`-Lie algebras `𝒲(ℒ) → Prim 𝒲(𝒰_p(ℒ))` (cf. 3.2.3).

**Proposition 5.5.1.** *Let `ℒ` be an `O_S`-`p`-Lie algebra, locally free as an `O_S`-module. Then `j_ℒ` induces an
isomorphism of `O_S`-`p`-Lie algebras:*

<!-- label: III.VII_A.5.5.1 -->

```text
𝒲(ℒ) ⥲ Prim 𝒲(𝒰_p(ℒ)).
```

*Proof.* Let `T` be an `S`-scheme; taking into account the identification `𝒰_p(ℒ_T) = 𝒰_p(ℒ)_T`, the task is to show
that the map `Γ(T, ℒ_T) → Prim Γ(T, 𝒰_p(ℒ_T))` is bijective. Replacing `S` by `T`, one is reduced to the case where
`T = S`, and it then suffices to show that the morphism of sheaves `j_ℒ : ℒ → Prim 𝒰_p(ℒ)` is an isomorphism. This
question being local on `S`, we may suppose that `S` is affine with ring `R` and that `ℒ` is the sheaf associated with
an `R`-`p`-Lie algebra `L` with basis `(x_α)`. As in 5.3.3, denote by `z_α` the image of `x_α` in `U = U_p(L)` and, for
every family `n = (n_α)` of integers between `0` and `p − 1`, zero except for a finite number of them, denote `z^{(n)}`
the product

```text
∏_α z_α^{n_α} / n_α!
```

<!-- original page 481 -->

(one supposes the basis `(x_α)` totally ordered and the products performed in increasing order).

Since `∆(z_α) = z_α ⊗ 1 + 1 ⊗ z_α`, one sees easily that

```text
∆(z^{(n)}) = ∑_r z^{(n−r)} ⊗ z^{(r)}
```

the sum being taken over the (finite!) set of `r` such that `0 ⩽ r_α ⩽ n_α` for every `α`. Since the `z^{(n)}` (resp.
the `z^{(n)} ⊗ z^{(m)}`) form a basis of `U` (resp. of `U ⊗ U`), one deduces that an element `u` of `U` satisfies
`∆(u) = u ⊗ 1 + 1 ⊗ u` if and only if `u` is a linear combination of the `z_α`. This proves 5.5.1.

**Remark 5.5.2.** *Recall (cf. 3.2.2 and 3.2.3), that the group `S`-functor `G = Spec^* 𝒰_p(ℒ)` is very good and that
`Lie(G) = Prim 𝒲(𝒰_p(ℒ))`. The preceding proposition therefore signifies that `j_ℒ` induces an isomorphism
`𝒲(ℒ) ⥲ Lie(G)`.*

<!-- label: III.VII_A.5.5.2 -->

If one supposes moreover that `ℒ` is a locally free `O_S`-module of finite rank, then `𝒰_p(ℒ)` is finite locally free
over `O_S`, according to 5.3.3, so `Spec^* 𝒰_p(ℒ)` is represented by the `S`-group `𝔊_p(ℒ) = Spec 𝒰_p(ℒ)^*` (cf. 3.2.2.1),
and one obtains the following more precise proposition:

**Proposition 5.5.3.** *Let `ℒ` be an `O_S`-`p`-Lie algebra, locally free of finite rank as an `O_S`-module, let
`𝒜 = 𝒰_p(ℒ)^*` and let `G = 𝔊_p(ℒ)` be the affine `S`-group `Spec 𝒜`.*

<!-- label: III.VII_A.5.5.3 -->

   *(i) `j_ℒ` induces an isomorphism `𝒲(ℒ) ⥲ Lie(G)` of `O_S`-`p`-Lie algebras.*

   *(ii) Let `ℐ` be the augmentation ideal of `𝒜` and `ω_G = ℐ / ℐ²` (cf. II, 4.11.4). Then `ω_G` is identified with
`ℒ^* = Hom_{O_S}(ℒ, O_S)`, hence is a locally free `O_S`-module of finite rank (and one has `ω_{G/S}^* = ℒ`).*

*Proof.* (i) following from 5.5.2, let us prove (ii). Denote by `η_𝒰` and `ε_𝒰` the unit section and the augmentation of
`𝒰 = 𝒰_p(ℒ)`, by `η_𝒜` and `ε_𝒜` those of `𝒜`, and `𝒥 = Ker ε_𝒰`. Then one has:

```text
(1)                  𝒰 = η_𝒰(O_S) ⊕ 𝒥.
```

Let `δ` be the morphism defined by the diagram below, where `τ` and `π` denote the inclusion and the projection deduced
from the decomposition (1):

```text
       𝒥  ──────────δ─────────→  𝒥 ⊗ 𝒥
       │                           ▲
     τ │                           │ π
       ▼            ∆               │
       𝒰  ──────────────────────→  𝒰 ⊗ 𝒰
```

then one has an exact sequence:

```text
(∗)        0  ──→  ℒ^*  ──j_ℒ→  𝒥  ──δ→  𝒥 ⊗ 𝒥.
```

Moreover, according to 5.3.3, the `O_S`-module `𝒥 / ℒ` is locally free and, according to 5.5.1, the sequence `(∗)`
remains exact after every base change. So, according to [BAC], II § 3, <!-- original page 482 --> prop. 6, `δ` induces
an isomorphism of `𝒥 / ℒ` onto a submodule `Q` locally direct factor of `𝒥 ⊗ 𝒥`. It follows that `(∗)` gives by duality
the exact sequence:

```text
(∗∗)        0  ←──  ℒ  ←──ᵗj_ℒ──  ℐ  ←──ᵗδ──  ℐ ⊗ ℐ.
```

Now the decomposition (1) corresponds by duality to the decomposition:

```text
(2)                  𝒜 = η_𝒜(O_S) ⊕ ℐ
```

and the transpose of `∆` is the multiplication `m_𝒜 : 𝒜 ⊗ 𝒜 → 𝒜`. Since `ℐ` is an ideal of `𝒜`, `m_𝒜` sends `ℐ ⊗ ℐ`
into `ℐ`; more precisely, taking into account decomposition (2), one has a commutative square

```text
                            m'
       ℐ  ←──────────  ℐ ⊗ ℐ
       │                  │
     ᵗτ                  ᵗπ
       ▼            m_𝒜    ▼
       𝒜  ←──────────  𝒜 ⊗ 𝒜
```

which shows that the restriction `m'` of `m_𝒜` to `ℐ ⊗ ℐ` is the transpose of `δ`. The exact sequence `(∗∗)` then gives
`ℐ / ℐ² ≃ ℒ^*`, and the proposition follows.

## 6. `p`-Lie algebra of an `S`-group scheme

<!-- label: III.VII_A.6 -->
<!-- original page 454 -->

Let `S` be a scheme of characteristic `p > 0`. In paragraph 5.5 we associated with every quasi-coherent
`O_S`-`p`-Lie algebra `ℒ` a group `S`-functor `𝔊_p(ℒ) = Spec^* 𝒰_p(ℒ)`. We shall now see that, for every `S`-group
scheme `G`, the `O_S`-Lie algebra `Lie(G/S)` defined in II 4.11 is naturally equipped with a structure of
`O_S`-`p`-Lie algebra.

### 6.1.

<!-- label: III.VII_A.6.1 -->

Let us first identify `Lie(G/S)(S)` and `Lie(Aut G/S)(S)` respectively with Lie subalgebras of `U(G)` and `Dif_{G/S}` by
means of the injections `α` and `β` of 2.5; `Lie(Aut G/S)(S)` is therefore identified with the `Γ(O_S)`-Lie algebra of
`S`-derivations of `O_G`. According to 5.2, this latter is a sub-`p`-Lie algebra of `Dif_{G/S}`.

On the other hand, the image of `L = Lie(G/S)(S)` by the injective algebra morphism `ℓ : U(G) → Dif_{G/S}`, `d ↦ _G d`,
is formed by the left-invariant derivations (cf. 2.2, N.D.E. (17), 2.4 and 2.5). If `x` belongs to `L`, `ℓ(x)^p` is none
other than `ℓ(x^p)`, according to loc. cit. Since `ℓ(x)^p` is again a derivation, one sees that `x^p` belongs to
`Lie(G/S)(S)`. Therefore:[^N.D.E-VII_A-57]

> `Lie(G/S)(S)` is a sub-`p`-Lie algebra of the infinitesimal algebra `U(G)`.

[^N.D.E-VII_A-57]: One can also show directly (without the intermediary of `Dif_{G/S}`) that the Lie algebra of
derivations of `G` at the origin (isomorphic to `Lie(G/S)(S)` according to 2.5) is stable under raising to the `p`-th
power in `U(G)`: this is done in 6.2 below.

#### 6.1.1.

<!-- label: III.VII_A.6.1.1 -->

Let `φ : G → H` be a homomorphism of `S`-group schemes. It is clear that the homomorphisms `Lie(φ/S)(S)` and `U(φ)` are
compatible with the identifications of `Lie(G/S)(S)` and `Lie(H/S)(S)` with sub-`p`-Lie algebras of `U(G)` and `U(H)`.
Since `U(φ)` is an algebra homomorphism, one sees therefore that `Lie(φ/S)(S)` is a homomorphism of `p`-Lie algebras.

Similarly, if `s : T → S` is a base change, the map from `Lie(G/S)(S)` into `Lie(G/S)(T)`, which is induced by `s`, is a
homomorphism of `p`-Lie algebras. One can translate this by saying that the functor `Lie(G/S)` is equipped with a
structure of `O_S`-`p`-Lie algebra. In particular, when `T` ranges over the opens of `S`, one sees that
<!-- original page 455 --> the sheaf `Lie(G/S)` is equipped with a structure of `O_S`-`p`-Lie algebra.

### 6.2.

<!-- label: III.VII_A.6.2 -->

Following an idea of Demazure, we shall now generalize what precedes to certain group `S`-functors not necessarily
representable. For this, we shall first give another definition of the symbolic `p`-th power in the Lie algebra of an
`S`-group scheme `G`.

Let `D` be a derivation of `G` at the origin;[^N.D.E-VII_A-58] according to 1.2.1, `D` is the composition of the
`S`-derivation `δ = (τ, ∂_t)` of the zero section `τ : S → I_S`, and a morphism `x : I_S → G` such that `x ∘ τ = ε`
(i.e. `x ∈ Lie(G/S)(S)`). According to the definition we gave in 2.1, `D^p` is the following composed deviation:

```text
S ≃ S × S × ··· × S ──δ × ··· × δ→ I_S × ··· × I_S ──x × ··· × x→ G × ··· × G ──m^{(p)}→ G
```

(`p` copies), where `m^{(p)}` is the morphism induced by the multiplication `m : G × G → G`. Since `I_S × ··· × I_S` is
affine over `S` and has as affine algebra `B = O_S[d_1, …, d_p] / (d_1², …, d_p²)`, the deviation `δ × ··· × δ` is
defined by the morphism of `O_S`-modules

```text
φ : B ⟶ O_S
```

which sends to `1` the monomial `d_1 d_2 ··· d_p`, and to `0` the other monomials `d_{i_1} ··· d_{i_r}`, for
`0 ⩽ r < p`. On the other hand, if `pr_i` denotes the projection of `I_S^p` onto the `i`-th factor and if `x_i` is the
image in `G(I_S^p)` of `x` by `G(pr_i)`, then the composed morphism `m^{(p)} ∘ (x × ··· × x)` is none other than the
product `x_1 x_2 ··· x_p`. Consequently, `D^p` is also the following composed deviation:

```text
S ──δ × ··· × δ→ I_S × ··· × I_S ──x_1 x_2 ··· x_p→ G.
```

[^N.D.E-VII_A-58]: We have expanded the original in what follows.

This description allows us to re-prove that `D^p` is a derivation of `G` at the origin. <!-- original page 456 -->
Indeed, since `G` is a very good group (II 4.11), the images `G(pr_1)(x)` and `G(pr_2)(x)` of `x` in `G(I_S × I_S)`
commute with each other. It follows that the elements `x_i` of `G(I_S^p)` commute pairwise and therefore, for every
permutation `γ` of the factors of `I_S^p`, one has `(x_1 ··· x_p) ∘ γ = x_1 ··· x_p`; it follows that `x_1 ··· x_p`
factors through the canonical projection of `I_S^p` into the symmetric product `Σ^p I_S` (cf. 4.2).

The symmetric product `Σ^p I_S` has as affine algebra the subalgebra `A` of `B` which has as basis over `O_S` the
elementary symmetric functions `1 = σ_0, σ_1, …, σ_p` of `d_1, …, d_p`. Denote by `κ` the inclusion `A ↪ B` and `π` the
morphism of `O_S`-algebras `A → O_S[t]/(t²)` which annihilates `σ_1, …, σ_{p−1}` and sends `σ_p` to `t`; then one has
`φ ∘ κ = ∂_t ∘ π` (recall that `∂_t : O_S[t]/(t²) → O_S` is the morphism of `O_S`-modules which annihilates `1` and
sends `t` to `1`). Consequently, denoting by `i` the closed immersion `I_S ↪ Σ^p I_S` defined by `π`, one has a
commutative diagram:

```text
                              D^p
       S  ──δ × ··· × δ→  I_S^p  ──x_1 ··· x_p→  G

   δ                              can.
              i                            y
       I_S  ──────────→  Σ^p I_S  ──────────→  G
```

which shows that `D^p` is of the form `y ∘ δ`, so is indeed a derivation of `G` at the origin.

### 6.3.

<!-- label: III.VII_A.6.3 -->

Let `𝔖_p` be the symmetric group of order `p` and `I_S^p × 𝔖_p` the direct sum of a family of copies of `I_S^p` indexed
by `𝔖_p`. We denote by `π : I_S^p × 𝔖_p → I_S^p` the canonical projection and

```text
μ : I_S^p × 𝔖_p ⟶ I_S^p
```

the morphism defining the action of `𝔖_p` on `I_S^p` (i.e., if `τ` is an element of `𝔖_p`, the restriction of `μ` to
`I_S^p × τ` has `pr_{τ(j)}` as `j`-th component). This being so, we lay down the following definition:

<!-- original page 457 -->

**Definition.** *A functor `X : (Sch/S)° → (Ens)` satisfies condition* (F) *if:*

   *a) `X` transforms finite direct sums into direct products,*

   *b) for every `S`-scheme `T`, the following sequence is exact:*

```text
X(T × Σ^p I_S)  ⟶  X(T × I_S^p)  ⇉  X(T × I_S^p × 𝔖_p),
                          (the two parallel arrows being X(id_T × π) and X(id_T × μ)).
```

Every `S`-scheme satisfies (F); if `ℱ` is an `O_S`-module, `𝒲(ℱ)` satisfies (F); every projective limit of functors
satisfying (F) also satisfies (F); if `Y` satisfies (F) and if `X` is an arbitrary `S`-functor, `Hom_S(X, Y)` satisfies
(F).

Let `X` be a very good group (II 4.10) satisfying condition (F). Denoting by `x : I_S → X` a morphism which extends the
unit section of `X` and resuming the notations of 6.2, one sees as above that `x_1 ··· x_p : I_S^p → X` factors through
`Σ^p I_S`:

```text
       I_S^p  ──x_1 ··· x_p→  X
           ╲                  ╱
         can. ╲              ╱ Σ^p(x)
                ╲          ╱
                   Σ^p I_S
```

and defines by composition a morphism

```text
x^{(p)} : I_S ──i→ Σ^p I_S ──Σ^p(x)→ X
```

which we shall call the *symbolic `p`-th power* of `x`.

<!-- original page 485 -->

The endomorphism `x ↦ x^{(p)}` of `Lie(G/S)(S)` is obviously compatible with base changes and is functorial in `G`. It
would be interesting to know for which `G` this endomorphism makes `Lie(G/S)(S)` a `p`-Lie algebra.

### 6.4.

<!-- label: III.VII_A.6.4 -->
<!-- original page 458 -->

The last definition of the symbolic `p`-th power, which we have just given, is particularly well-suited to computation.
Here are some examples:

#### 6.4.1.

<!-- label: III.VII_A.6.4.1 -->

Let `M` be an "abstract" abelian group and `D_S(M)` the diagonalizable `S`-group of type `M` (I 4.4.2). For every
`S`-scheme `T`, one has therefore

```text
D_S(M)(T) = Hom_{(Ab)}(M, O(T)^×).
```

Let `x` be an element of `Lie(D_S(M)/S)(S)`, i.e., a homomorphism of abelian groups

```text
M ──x→ Γ(S, O_S + d O_S)^×
```

of the form `m ↦ 1 + d ξ(m)`, where `ξ ∈ Hom_{(Ab)}(M, O(S))`. With the notations of 6.2 and 6.3, the product
`x_1 ··· x_p` associates with an element `m` of `M` the expression

```text
(1 + d_1 ξ(m)) ··· (1 + d_p ξ(m))
```

i.e. `1 + σ_1 ξ(m) + σ_2 ξ(m)² + ··· + σ_p ξ(m)^p`.

This expression indeed belongs to `O(Σ^p I_S)`. Projecting this into `O(S)[d]/(d²)` by annihilating `σ_1, …, σ_{p−1}`
and sending `σ_p` to `d`, one sees that `x^{(p)}` is the following homomorphism from `M` into `Γ(S, O_S + d O_S)^×`:

```text
m ↦ 1 + d ξ(m)^p.
```

In summary, if one identifies `Lie(D_S(M)/S)(S)` with `Hom_{(Ab)}(M, O(S))` as in II 5.1, the symbolic `p`-th power
associates with `ξ` the homomorphism `ξ^{(p)} : m ↦ ξ(m)^p`.

#### 6.4.2.

<!-- label: III.VII_A.6.4.2 -->
<!-- original page 459 -->

Let `ℱ` be an `O_S`-module and `G` the group `S`-functor in abelian groups `𝒲(ℱ)` (cf. I, 4.6). Let `y` be an element of
`𝒲(ℱ)(S) = Γ(S, ℱ)` and `y'` its image in `𝒲(ℱ)(I_S)` by `𝒲(ℱ)(I_S → S)`.

One knows (cf. II, 4.4.2 and 4.5.1) that the map `y ↦ d y'` is an isomorphism of `O(S)`-modules from `𝒲(ℱ)(S)` onto
`Lie(𝒲(ℱ)/S)(S)`. If one sets `x = d y'`, the quantity `x_i` of 6.2 is none other than `d_i y''`, where `y''` denotes
the canonical image of `y'`[^N.D.E-VII_A-59] in `𝒲(ℱ)(I_S^p)`. Consequently, the product `x_1 ··· x_p` is equal here to

```text
x_1 + ··· + x_p = (d_1 + ··· + d_p) y'' = σ_1 y''
```

and belongs to `𝒲(ℱ)(Σ^p I_S)`. Since the homomorphism `O(Σ^p I_S) → O(I_S)`, which defines the morphism `i` of 6.1,
annihilates `σ_1`, one sees that `x^{(p)}` is zero. Therefore:

> For every `O_S`-module `ℱ`, the operation `x ↦ x^{(p)}` in `Lie 𝒲(ℱ)` is zero.

[^N.D.E-VII_A-59]: We have corrected `x` to `y'`.

#### 6.4.3.

<!-- label: III.VII_A.6.4.3 -->

Let `X` be an `S`-scheme, `G` the group `S`-functor `Aut_S X` and `D` an `S`-derivation of the structure sheaf `O_X`.
According to 1.5, `D` can be identified with an `I_S`-automorphism `x` of `X_{I_S}`, inducing the identity on `X`,
which one can describe as follows. If `f` is a section of `O_S[d]/(d²)` of the form `a + bd`, set
`D_{I_S} f = D a + (D b) d`; in other words, `D_{I_S}` is deduced from `D` by the base change `I_S → S`; then the
automorphism in question of `X_{I_S}` is associated with the endomorphism
`f ↦ f + (D_{I_S} f) d = a + (D(a) + b) d` of `O_S[d]/(d²)`.

Similarly, let `D_{I_S^p}` be the differential operator of `X_{I_S^p}` deduced from `D` by the base change
`I_S^p → S`. With the notations of 6.2, the automorphism `x_i` of `X_{I_S^p}` is then associated with the endomorphism
`f ↦ f + (D_{I_S^p} f) d_i` of `O_S[d_1, …, d_p] / (d_1², …, d_p²)`. The product `x_1 ··· x_p` is therefore associated
with the endomorphism

```text
(1 + d_1 D_{I_S^p})(1 + d_2 D_{I_S^p}) ··· (1 + d_p D_{I_S^p})
```

<!-- original page 460 -->

i.e., `1 + σ_1 D_{I_S^p} + σ_2 D²_{I_S^p} + ··· + σ_p D^p_{I_S^p}`.

The coefficient of `σ_p` is `D^p_{I_S^p}`, which means that the Lie algebra isomorphism

```text
Dér_S(O_X) ⥲ Lie(Aut_S X),    D ↦ x
```

(cf. 1.5), is also an isomorphism of `p`-Lie algebras.

#### 6.4.4.

<!-- label: III.VII_A.6.4.4 -->

Using the same method, one sees that, for every `O_S`-module `ℱ`, the Lie algebra isomorphism

```text
Lie(Aut_{O_S-mod.} 𝒲(ℱ) / S)(S) ⥲ (End_{O_S-mod.} 𝒲(ℱ))(S).
```

(cf. II 4.8) is also an isomorphism of `p`-Lie algebras.

#### 6.4.5.

<!-- label: III.VII_A.6.4.5 -->

[^N.D.E-VII_A-60] Let `𝒰` be an `O_S`-coalgebra in groups and `G` the group `S`-functor `Spec^* 𝒰`; suppose that `G` is
representable. In this case, for every `T → S`, one has defined in 5.5 and 6.1.1 two structures of `p`-Lie algebra on
`L(T) = Lie(G)(T)`. Since one has a commutative diagram

```text
                              τ
       L(T)  ─────────────────→  Γ(T, 𝒰_T)
          │ ╲                      ▲
          │   ╲ i                  │ ψ
        α │     ╲                  │
          │       ╲                │
          ▼          ▼              │
       U(G_T)  ←─────────────  U(L(T))
                       φ
```

where `U(L(T))` is the enveloping algebra of `L(T)` and `φ`, `ψ` the algebra morphisms induced by `α`, `τ`, one sees
that the two `p`-Lie algebra structures coincide: if one identifies `x ∈ L(T)` with its image in `U(G_T)` (resp.
`Γ(T, 𝒰_T)`), then `x^{(p)}` is the image of the element `x^p` of `U(L(T))` by `φ` (resp. `ψ`).

[^N.D.E-VII_A-60]: We have added the numbering 6.4.5, and expanded the original.

## 7. Radicial groups of height 1

<!-- label: III.VII_A.7 -->
<!-- original page 461 -->

[^N.D.E-VII_A-61] Let `S` be a scheme of characteristic `p > 0`. We shall say that an `O_S`-algebra `𝒜` (resp. an
`O_S`-`p`-Lie algebra `ℒ`) is *finite locally free* if the `O_S`-module underlying `𝒜` (resp. `ℒ`) is locally free and
of finite type. If `ℒ` is a finite locally free `O_S`-`p`-Lie algebra, we know (cf. 5.5.2) that the group `S`-functor
`Spec^* 𝒰_p(ℒ)` is represented by an `S`-group scheme `𝔊_p(ℒ)`, finite and locally free. We shall see that this
`S`-group scheme is the solution of a universal problem (7.2) and we shall characterize the `S`-group schemes of the
form `𝔊_p(ℒ)` (7.4).

[^N.D.E-VII_A-61]: For the results of this section, one may also consult [DG70], § II.7, nos 3-4.

### Definition 7.0.

<!-- label: III.VII_A.7.0 -->

[^N.D.E-VII_A-62] *Let `H = Spec 𝒜` be a finite locally free `S`-group scheme. We say that `H` is* infinitesimal *if
the unit section `ε_H : S → H` is a homeomorphism, which is equivalent to saying that the augmentation ideal of `𝒜` is
locally nilpotent.*

[^N.D.E-VII_A-62]: We have added this definition (cf. [DG70], § II.4, 7.1), which will be used in 7.2.1.

### 7.1.

<!-- label: III.VII_A.7.1 -->

[^N.D.E-VII_A-63] Let `ℒ` be a finite locally free `O_S`-`p`-Lie algebra and let `𝔊_p(ℒ)` be the affine `S`-group
`Spec 𝒰_p(ℒ)`. According to 5.5, one knows that `ℒ` is identified with `Lie 𝔊_p(ℒ)`.

[^N.D.E-VII_A-63]: We have simplified the original, taking into account the additions made in 5.5.

Consider now a very good group `S`-functor `G` satisfying condition (F) of 6.3 and let `φ : 𝔊_p(ℒ) → G` be a morphism
of group `S`-functors. According to 6.3, the morphism of `O_S`-Lie algebras `Lie φ : Lie 𝔊_p(ℒ) → Lie G` is compatible
with the symbolic `p`-th power. If we denote by `Hom_p(ℒ, Lie G)` the set of `O_S`-Lie algebra morphisms which are
compatible with the symbolic `p`-th power, one therefore has a map <!-- original page 462 -->

```text
Lie : Hom_{S-Gr.}(𝔊_p(ℒ), G) ⟶ Hom_p(ℒ, Lie G),    φ ↦ Lie φ.
```

### 7.2. Theorem.

<!-- label: III.VII_A.7.2 -->

*If `ℒ` is a finite locally free `O_S`-`p`-Lie algebra, the map*

```text
Hom_{S-gr.}(𝔊_p(ℒ), G) ⟶ Hom_p(ℒ, Lie G)
```

*is bijective in each of the following cases:*

   *(i) `G` is an `S`-group scheme;*

   *(ii) `G` is of the form `Aut_S X`, where `X` is an `S`-scheme;*

   *(iii) `G` is of one of the forms `𝒲(ℱ)` or `Aut_{O_S-mod} 𝒲(ℱ)`, where `ℱ` denotes a quasi-coherent `O_S`-module.*

The proof of the theorem rests on the following lemma:

**Lemma.** *If `ℒ` is a finite locally free `O_S`-`p`-Lie algebra, the `S`-group `G = 𝔊_p(ℒ)` is annihilated by the
Frobenius morphism `Fr : G → G^{(p)}`. In particular, `G` is infinitesimal.*

[^N.D.E-VII_A-64] Let in fact `𝒰` be the restricted enveloping algebra of `ℒ`, `𝒜 = 𝒰^*` the affine algebra of `G`,
and `ℐ = Ker ε_𝒜` the augmentation ideal of `𝒜`. One has

```text
(1)                      𝒜 = ℐ ⊕ η_𝒜(O_S),
```

where `η_𝒜` denotes the unit section of `𝒜`, and since `ε_𝒜` (resp. `η_𝒜`) is the transpose of `η_𝒰` (resp. `ε_𝒰`),
this decomposition corresponds by duality to the decomposition

```text
(2)                      𝒰 = 𝒥 ⊕ η_𝒰(O_S),
```

where `𝒥` is the augmentation ideal of `𝒰`; one therefore has `𝒥 = ℐ^*`.

[^N.D.E-VII_A-64]: We have expanded the original in what follows. For another proof, see [DG70], § II.7, 3.9.

Let `π` denote the endomorphism `x ↦ x^p` of `O_S`. We must show that the morphism `Fr : G → G^{(p)}` factors through
the unit section of `G^{(p)}`, which is equivalent to saying (cf. 4.1.4 (c)) that the morphism
`Φ : a ⊗_π x ↦ a^p x` from `ℐ ⊗_π O_S` into `𝒜` is zero. Since `𝒜` is finite locally free over `O_S`, it suffices to
see that the transposed morphism `^t Φ` is zero.

Now `Φ` is none other than the following composition

```text
ℐ ⊗_π O_S ──τ→ 𝒜 ⊗_π O_S ──j(𝒜)→ S^p 𝒜 ──b(𝒜)→ 𝒜,
```

where `τ` is deduced from the inclusion `ℐ ↪ 𝒜`, and `b(𝒜)` and `j(𝒜)` are defined as in 4.3.3 (i.e. `b(𝒜)` is induced
by the multiplication of `𝒜` and `j(𝒜)` sends `a ⊗_π 1` to the image of `a ⊗ ··· ⊗ a` in `S^p 𝒜`). Since the
`O_S`-dual module of `S^p 𝒜` is none other than the submodule `Σ^p 𝒰` of `⨂^p 𝒰` formed by the sections invariant
under the action of the symmetric group of order `p`, one sees that `^t Φ` is the following composed morphism:
<!-- original page 463 -->

```text
𝒰 ──a(𝒰)→ Σ^p 𝒰 ──r(𝒰)→ 𝒰 ⊗_π O_S ──q→ 𝒥 ⊗_π O_S,
```

where `q` is deduced from the projection `𝒰 → 𝒥` of kernel `η_𝒰(O_S)`, `a(𝒰)` is induced by the comultiplication of
`𝒰` and `r(𝒰)` vanishes on the symmetrized tensors and sends a section `x ⊗ ··· ⊗ x` to `x ⊗_π 1` (confer 4.3.3).

It is clear that `^t Φ ∘ η_𝒰 = 0` and therefore, according to (2), it remains to see that `^t Φ` annihilates the
augmentation ideal `𝒥`. Since `^t Φ` is an algebra morphism and since the ideal `𝒥` is generated by `ℒ` (identified
with its image in `𝒰`), it suffices to see that `^t Φ(x) = 0` for every section `x` of `ℒ`. Now
`−a(𝒰)(x) = (p − 1)! a(𝒰)(x)` is the symmetrization of `x ⊗ 1 ⊗ ··· ⊗ 1`, so its image by `r(𝒰)` is zero. This proves
the first assertion of the lemma.

The second follows. Indeed, since every local section of `ℐ` has `p`-th power zero and since `ℐ` is an `O_S`-module of
finite type, `ℐ` is locally nilpotent (explicitly, if `V` is an affine open of `S` such that `I = Γ(V, ℐ)` is generated
by `r` elements, then `I^{r(p−1)+1} = 0`), whence `G_{red} = S_{red}` and therefore the unit section `ε_G : S → G` is a
homeomorphism.

#### 7.2.1.

<!-- label: III.VII_A.7.2.1 -->

[^N.D.E-VII_A-65] We shall first prove assertion (ii) of Theorem 7.2. Let `π : X → S` be an `S`-scheme. Consider first
an arbitrary infinitesimal `S`-group `H`. The <!-- original page 489 --> morphisms `φ` from `H` into `Aut X` correspond
bijectively to left actions `μ : H × X → X` of `H` on `X`. For such an action, if `ε` is the unit section of `H`, the
composed morphism

[^N.D.E-VII_A-65]: We have expanded the original in what follows.

```text
X ≃ S × X ──ε × X→ H × X ──μ→ X
```

must be the identity. Since `(H × X)_{red}` is identified with `X_{red}`, one sees that `μ` must induce the identity on
the associated reduced schemes. In particular, `μ` induces an action of `H` on each open of `X`, and one therefore
obtains, for every open `U` of `X`, affine over `S`, a morphism of unital associative algebras:

```text
𝒜(U) ⟶ 𝒜(H) ⊗ 𝒜(U)
```

making `𝒜(U)` an `𝒜(H)`-comodule on the left, in such a way that the restriction maps `𝒜(U) → 𝒜(U')`, for `U' ⊂ U`,
are comodule morphisms. Conversely, every datum of this type comes from a unique left action `μ : H × X → X`. On the
other hand, one has the following lemma:

**Lemma.** *Let `X = Spec 𝒞` be an affine `S`-scheme, `H = Spec 𝒜` an infinitesimal `S`-group,*
<!-- original page 464 -->
*and `𝒰 = 𝒜^* = Hom_{O_S}(𝒜, O_S)`. The left actions of `H` on `X` correspond bijectively to the representations of the
algebra `𝒰` in the `O_S`-module `𝒞` such that one has:*

```text
(a)    u(1_𝒞) = ε(u) · 1_𝒞
(b)    u(xy) = ∑_i v_i(x) w_i(y)    if    ∆u = ∑_i v_i ⊗ w_i.
```

   *(In the formulas above, `u` denotes an arbitrary section of `𝒰` on an affine open `V` of `S`, `x` and `y` sections
of `𝒞` on `V`; one denotes by `1_𝒞` the unit section of `𝒞`, by `ε` and `∆` the augmentation and the diagonal morphism
of `𝒰`.)*

Indeed, a left action `μ` of `H` on `X` is defined by a morphism of unital associative algebras:

```text
λ : 𝒞 ⟶ 𝒜 ⊗ 𝒞
```

making `𝒞` an `𝒜`-comodule on the left. We shall denote by `α` the composed morphism

```text
𝒰 ⊗_{O_S} 𝒞 ──𝒰 ⊗ λ→ 𝒰 ⊗_{O_S} 𝒜 ⊗_{O_S} 𝒞 ──γ ⊗ 𝒞→ O_S ⊗_{O_S} 𝒞 ≃ 𝒞
```

where `γ` is the "contraction" of `𝒜^* ⊗_{O_S} 𝒜` into `O_S`. Since `𝒜` is finite locally free over `O_S`, one knows
that the map `λ ↦ (γ ⊗ 𝒞)(𝒰 ⊗ λ)` is a bijection from `Hom_{O_S}(𝒞, 𝒜 ⊗ 𝒞)` onto `Hom_{O_S}(𝒰 ⊗ 𝒞, 𝒞)`. Moreover, one
sees easily that the condition that `λ` define a structure of `𝒜`-comodule on the left (resp. be a morphism of unital
associative algebras) is equivalent, by duality, to the condition that `α` be a representation of `𝒰` in `𝒞` (resp.
that `α` satisfy conditions (a) and (b)). This proves the lemma.

Moreover, it is clear that, for every representation of `𝒰` in the `O_S`-module `𝒞`, the sections `u` of `𝒰` which
satisfy conditions (a) and (b) of the lemma form a subalgebra of `𝒰`.

In the particular case `H = 𝔊_p(ℒ)` of interest to us, these conditions will therefore be satisfied for all sections
`u` of `𝒰 = 𝒰_p(ℒ)`, if they are true for the <!-- original page 490 --> sections `u` of `ℒ` (by identifying `ℒ` with
its image in `𝒰_p(ℒ)`). Now, if `u` is a section of `ℒ`, conditions (a) and (b) simply mean that `u(1_𝒞) = 0` and that
`u(xy) = u(x) y + x u(y)`, i.e. that `α(u)` is an `O_S`-derivation of `𝒞 = 𝒜(X)`. Assertion (ii)
<!-- original page 465 --> of 7.2 follows. Indeed, every morphism `φ` from `𝔊_p = 𝔊_p(ℒ)` into `Aut X` defines a
homomorphism of `p`-Lie algebras `Lie φ` from `ℒ = Lie 𝔊_p` into `π_*(Dér_{O_S} O_X)`, and conversely every datum of
this type comes, according to what precedes, from a unique action `μ : G × X → X`.

#### 7.2.2.

<!-- label: III.VII_A.7.2.2 -->

Let us now show how assertion (i) of Theorem 7.2 follows from (ii). Let `G` be an `S`-group scheme. If `T` is an
`S`-scheme and `x` an element of `G(T)`, we denote by `ℓ^T_x` (resp. `r^T_x`) the left translation (resp. right
translation) of `G_T` defined by `x`. The maps `ℓ^T : x ↦ ℓ^T_x` therefore determine a homomorphism `ℓ` from `G` into
`Aut G`. On the other hand, let `f` be a `T`-automorphism of `G_T`; one then defines `^x f` as being equal to
`(r^T_x)^{-1} f r^T_x`, i.e. for every `T' → T` and `g ∈ G(T')`, `(^x f)(g) = f(g x) x^{-1}`. In this way `G` acts on the
left on the group `S`-functor `Aut G`, hence also on the functors `T ↦ Hom_{T-Gr.}(𝔊_p(ℒ_T), Aut G_T)` and
`T ↦ Hom_p(ℒ_T, Lie(Aut G_T / T))`. On the other hand, the morphism `ℓ^T : G_T → Aut G_T` identifies `G_T` with the
group of automorphisms of the `T`-scheme `G_T` commuting with right translations, and the derived morphism `Lie(ℓ^T)`
identifies `Lie G_T` with the `p`-Lie algebra of `O_T`-derivations of `O_{G_T}` commuting with right translations
(cf. II, 4.11.1); they therefore induce commutative squares

```text
                                          Lie
       Hom_{T-Gr.}(𝔊_p(ℒ_T), G_T)  ───────────→  Hom_p(ℒ_T, Lie(G_T / T))

             ℓ^T                                       Lie ℓ^T

                                          Lie
       Hom_{T-Gr.}(𝔊_p(ℒ_T), Aut G_T)  ─────→  Hom_p(ℒ_T, Lie(Aut G_T / T)).
```

The images of the two vertical arrows are the subfunctors formed by the invariants under the action of the `S`-group
`G`. Since the bottom horizontal arrow is invertible according to 7.2.1 and is compatible with the action of `G`, the
top horizontal arrow is also invertible. This proves 7.2 (i).

#### 7.2.3.

<!-- label: III.VII_A.7.2.3 -->
<!-- original page 466 -->

Consider now the case where `G = Aut_{O_S-mod.} 𝒲(ℱ)`.[^N.D.E-VII_A-66] Set `𝒰 = 𝒰_p(ℒ)`, `𝒜 = 𝒰^*` and
`H = 𝔊_p(ℒ) = Spec 𝒜`. Since `H` is affine over `S` then, according to VI_B 11.6.1, a morphism of `S`-groups from `H`
into `Aut_{O_S-mod.} 𝒲(ℱ)` is the same thing as a structure of `𝒜`-comodule on the right

```text
μ : ℱ ⟶ ℱ ⊗ 𝒜.
```

Moreover, since `𝒜` is finite locally free over `O_S`, this is equivalent to the datum of a representation

```text
α : 𝒰 ⟶ End_{O_S}(ℱ)
```

of `𝒰` in `ℱ`. Finally, according to the universal property of `𝒰 = 𝒰_p(ℒ)`, to give such a morphism `α` is equivalent
to giving its restriction `ρ` to `ℒ` (identified with its image in `𝒰`), which is a `p`-Lie algebra morphism from `ℒ`
into `End_{O_S}(ℱ)`.

[^N.D.E-VII_A-66]: In what follows, we have expanded (and simplified) the original, taking into account VI_B, 11.6.1.

[^N.D.E-VII_A-67] Finally, consider the case where `G = 𝒲(ℱ)`, keeping the preceding notations. First, to give a
morphism of `S`-functors `φ : H → 𝒲(ℱ)` is equivalent to giving an element `θ` of `Γ(H, ℱ ⊗ O_H)`, and since `H` is
finite locally free over `S`, one has:

```text
Γ(H, ℱ ⊗ O_H) = Γ(S, ℱ ⊗ 𝒜) = Hom_{O_S}(𝒰, ℱ).
```

The condition that `φ` be a group morphism then translates into the fact that `θ`, considered as morphism of
`O_S`-modules `𝒰 → ℱ`, vanishes on `1_𝒰` and on `𝒥² / 𝒥`, where `𝒥` is the augmentation ideal of `𝒰`, whence

```text
(1)                  Hom_{S-gr.}(H, 𝒲(ℱ)) = Hom_{O_S}(𝒥 / 𝒥², ℱ).
```

[^N.D.E-VII_A-67]: We have added the following. (The original indicated "the case of `𝒲(ℱ)` is analogous").

On the other hand, consider the quasi-coherent sheaf `[ℒ, ℒ]`, image of the morphism `ℒ ⊗ ℒ → ℒ`, `x ⊗ y ↦ [x, y]`;
for every affine open `V` of `S`, one has `[ℒ, ℒ](V) = [ℒ(V), ℒ(V)]`. Then one has an exact sequence

```text
(†)        0  ⟶  [ℒ, ℒ]  ⟶  ℒ  ──π→  𝒥 / 𝒥²  ⟶  0,
```

where `π` is the composition of the inclusion `ℒ ↪ 𝒥` and the projection `𝒥 → 𝒥 / 𝒥²`.

Indeed, the question being local on `S`, we may suppose that `S` is affine with ring `R` and that `L = ℒ(S)` is free
with basis `(x_1, …, x_r)`. Identifying `L` with its image in `U = U_p(L)`, let `K` be the sub-`R`-module of `U` direct
sum of `[L, L]` and the submodule with basis the monomials `x_1^{n_1} ··· x_r^{n_r}` such that `n_1 + ··· + n_r ⩾ 2`;
one then verifies that `K` is a two-sided ideal of `U`. Since `K` is contained in `J²` (where `J` is the augmentation
ideal of `U`) and contains all the products `x_i x_j` (which generate `J²`), one deduces that `K = J²`, whence
`J² ∩ L = [L, L]` and one has the exact sequence `(†)`.

On the other hand, one knows from 6.4.2 that `Lie 𝒲(ℱ)` is none other than `𝒲(ℱ)`, the Lie bracket and the symbolic
`p`-th power being zero. From this and from what precedes one deduces that

```text
(2)        Hom_p(ℒ, ℱ) = Hom_{O_S}(ℒ / [ℒ, ℒ], ℱ) = Hom_{O_S}(𝒥 / 𝒥², ℱ)
```

and this, combined with (1), completes the proof of Theorem 7.2.

### 7.3. Lemma.

<!-- label: III.VII_A.7.3 -->

*If `ℒ` is a finite locally free `O_S`-`p`-Lie algebra, the morphism `j_ℒ : ℒ → Lie 𝔊_p(ℒ)` of 5.5 is invertible.*

<!-- original page 467 -->

[^N.D.E-VII_A-68] For the proof, see 5.5.1.

[^N.D.E-VII_A-68]: In order not to modify the numbering, the statement 7.3 has been preserved, although it has been
included, with its proof, in 5.5.1.

### 7.4.

<!-- label: III.VII_A.7.4 -->

To end this section, we shall give a characterization of the `S`-group schemes of the form `𝔊_p(ℒ)`, where `ℒ` is a
finite locally free `O_S`-`p`-Lie algebra.

Let `G` be an `S`-group scheme, `ε_G` the unit section and `ℐ'` the kernel of the morphism `ε_G^{-1}(O_G) → O_S`
corresponding to `ε_G`. The image of `Lie(G/S)(S)` in `U(G)` is identified, according to 2.5 and 1.3.1, with the
morphisms of `O_S`-modules from `ε_G^{-1}(O_G)` into `O_S` which vanish on the unit section of `ε_G^{-1}(O_G)` and on
`ℐ'²`. One thus recovers the canonical isomorphism of `Lie(G/S)(S)` onto `Hom_{O_S}(ℐ' / ℐ'², O_S)` of II, 3.3 and
4.11.4.[^N.D.E-VII_A-69] We shall set `ω_{G/S} = ℐ' / ℐ'²` as in loc. cit., so that the sheaf `Lie(G/S)` is identified
with `ω_{G/S}^* = Hom_{O_S}(ω_{G/S}, O_S)`.[^N.D.E-VII_A-70] Moreover, if `G = 𝔊_p(ℒ)`, where `ℒ` is a finite locally
free `O_S`-`p`-Lie algebra, one saw in 5.5.3 that `ω_{G/S} = ℒ^*`.

[^N.D.E-VII_A-69]: If `G` is affine over `S` and if `ℐ` denotes the augmentation ideal of `𝒜(G)`, then `ℐ' / ℐ'²` is
identified with `ε_G^*(ℐ / ℐ²)`, cf. loc. cit.

[^N.D.E-VII_A-70]: We have added the following sentence.

**Theorem.** *If `G` is a group scheme over a scheme `S` of characteristic `p > 0`, the following assertions are
equivalent:*

   *(i) There exists a finite locally free `O_S`-`p`-Lie algebra `ℒ` such that `G ≃ 𝔊_p(ℒ)`.*

   *(i') The `O_S`-`p`-Lie algebra `Lie(G)` is finite locally free and `G ≃ 𝔊_p(Lie(G))`.*

   *(ii) `G` is affine over `S`, `ω_{G/S}` is a locally free `O_S`-module of finite type and the affine algebra of `G`
is locally isomorphic to the quotient of the symmetric algebra `S_{O_S}(ω_{G/S})` by the ideal generated by the `p`-th
powers of the sections of `ω_{G/S}`.*

   *(iii) `G` is locally of finite presentation over `S`, of height `⩽ 1`, and `ω_{G/S}` is locally free.*

   *(iii') `G` is locally of finite type over `S`, of height `⩽ 1`, and `ω_{G/S}` is locally free.*

   *(iv) `G` is locally of finite presentation and flat over `S`, of height `⩽ 1`.*[^N.D.E-VII_A-71]

[^N.D.E-VII_A-71]: We have added, on the one hand, assertion (i'), implicit in the original, and on the other hand,
assertions (iii') and (iv), pointed out by O. Gabber; assertion (iv) takes up a footnote of the original, which
indicated: "The condition on `ω_{G/S}` is in fact useless, as one sees easily by reducing to the case where `S` is
local with residue field `k`, and applying the theorem to the case of the group `G_k`". As pointed out by Gabber, this
is inaccurate without a flatness hypothesis: if `A` is an Artinian local ring of characteristic `p > 0` and `J` a
proper non-zero ideal of `A`, let `H` be the subgroup `Spec A[x] / (x^p, J x)` of `α_{p, A}` (i.e. for every `A`-algebra
`R`, `H(R) = { x ∈ R | x^p = 0 and J x = 0 }`), then `H` is not flat over `A` so is not of the form `𝔊_p(ℒ)`, where `ℒ`
is a free `p`-Lie algebra of finite rank over `A`.

#### 7.4.1.

<!-- label: III.VII_A.7.4.1 -->
<!-- original page 468 -->

The equivalence (i) ⇔ (i') follows from 5.5.3 (i), the implications (ii) ⇒ (iii) ⇒ (iii') are clear, and one has
(i) ⇒ (iv) since `𝔊_p(ℒ)` is finite locally free and of height `⩽ 1`, according to 5.5.2 and Lemma 7.2. Let us show
that (i) entails (ii). Denote by `ℐ` the augmentation ideal of `𝒜 = 𝒰_p(ℒ)^*`. One has already seen in 5.5.3 (ii) that
`ω_{G/S} = ℐ / ℐ²` is identified with `ℒ^*`, hence is finite locally free.

Now suppose `S` affine. There is then a section `σ : ω_{G/S} → ℐ` of the projection `ℐ → ℐ / ℐ²`; it induces an algebra
morphism `σ' : S_{O_S}(ω_{G/S}) → 𝒜` and, according to Lemma 7.2, `σ'` factors into a morphism

```text
φ : S_{O_S}(ω_{G/S}) / K ⟶ 𝒜,
```

where `K` denotes the ideal generated by the `p`-th powers of sections of `ω_{G/S}`. If one filters `𝒜` (resp.
`S_{O_S}(ω_{G/S}) / K`) by the powers of `ℐ` (resp. of the ideal generated by `ω_{G/S}`), it is clear that `φ` induces
an epimorphism of the associated graded modules. So `φ` is an epimorphism of locally free `O_S`-modules of the same
rank (cf. 5.3.3); so `φ` is an isomorphism. This proves that (i) ⇒ (ii).

#### 7.4.2.

<!-- label: III.VII_A.7.4.2 -->

Suppose now `G` of height `⩽ 1` and locally of finite presentation <!-- original page 469 -->
over `S`.[^N.D.E-VII_A-72] Since the Frobenius morphism `Fr : G → G^{(p)}` is integral and factors through the unit
section of `G^{(p)}`, then `G` is integral (hence affine) over `S`. Let then `𝒜 = 𝒜(G)`; since `G` is supposed locally
of finite presentation over `S`, it follows that `G` is finite and of finite presentation over `S`, hence `𝒜(G)` is an
`O_S`-module of finite presentation (cf. EGA IV₁, 1.4.7). Let `ℐ` be the augmentation ideal of `𝒜`; since
`𝒜 = η_𝒜(O_S) ⊕ ℐ` (where `η_𝒜` is the unit section of `𝒜`), `ℐ` is an `O_S`-module of finite presentation, and so is
`ω_G = ℐ / ℐ²`. When one supposes `G` of height `⩽ 1` and locally of finite type over `S`, one obtains similarly that
`𝒜(G)`, `ℐ` and `ω_G = ℐ / ℐ²` are `O_S`-modules of finite type.

[^N.D.E-VII_A-72]: We have expanded (and simplified) the original in what follows.

So, under hypothesis (iii'), one obtains that `ω_{G/S}` is finite locally free over `O_S`, as is
`ℒ = Lie(G/S) = ω_{G/S}^*`. Let then `ℬ = 𝒰_p(ℒ)^*` and `H = 𝔊_p(ℒ) = Spec ℬ`. According to Theorem 7.2, the identity
map of `ℒ` corresponds to a group morphism from `H = 𝔊_p(ℒ)` to `G`, hence to a morphism of `O_S`-algebras
`θ : 𝒜 → ℬ`. The task is to show that `θ`, which induces by definition an isomorphism of `ω_{G/S}` onto `ω_{H/S}`, is
an isomorphism.

For this, one may restrict to the case where `S` is affine. There is then a section `τ` of the projection
`ℐ → ω_{G/S}`; it induces an algebra morphism `τ' : S_{O_S}(ω_{G/S}) → 𝒜` and since every local section of `ℐ` has
`p`-th power zero (since `Fr : G → G^{(p)}` factors through the unit section of `G^{(p)}`), `τ'` induces a morphism of
`O_S`-algebras `ψ` which fits in the commutative diagram below:

```text
                                          ψ
              S_{O_S}(ω_{G/S}) / K  ──────→  𝒜
                       ╲                        │
                         ╲                      │ θ
                         φ ╲                    │
                              ╲                 ▼
                                                ℬ
```

where `K` is the ideal generated by the `p`-th powers of sections of `ω_{G/S}`. On the one hand, one shows as in 7.4.1
that `ψ` is an epimorphism of `O_S`-modules. On the other hand, we saw in 7.4.1 that `φ = θ ∘ ψ` is an isomorphism. The
same therefore holds for `θ`. This proves that (iii') ⇒ (i).

#### 7.4.3.

<!-- label: III.VII_A.7.4.3 -->

[^N.D.E-VII_A-73] Let us finally show that (iv) entails (iii). It suffices to show that `ω_{G/S}` is locally free, so
one may suppose `S` affine with ring `R`. As remarked at the beginning of 7.4.2, hypothesis (iv) then entails that
`G = Spec A`, for an `R`-algebra `A` which is an `R`-module of finite presentation, as is `ω_{G/A} = I / I²` (where `I`
is the augmentation ideal of `A`). Since one supposes moreover that `G` is flat over `S`, then `A` is a finite locally
free `R`-module (cf. [BAC] II, § 5.2, Th. 1 and cor. 2) and, according to loc. cit., to show that `ω_{G/A}` is locally
free of finite rank, it suffices to show that `(ω_{G/A})_𝔪` is flat for every maximal ideal `𝔪` of `R`. So one may
suppose `R` local <!-- original page 494 --> and `A` free of rank `n + 1`, hence `I` free of rank `n`. Let `𝔪` be the
maximal ideal of `R` and `k = R / 𝔪`.

[^N.D.E-VII_A-73]: We have added this paragraph to prove that (iv) ⇒ (iii), cf. N.D.E. (71).

Denote by `I_k` the augmentation ideal of `A_k` and `r` the dimension of `ω_{G_k / k} = I_k / I_k²`. Let
`(e_1, …, e_n)` be a basis of `I_k` such that `(e_{r+1}, …, e_n)` is a basis of `I_k²`, and let `x_1, …, x_n` be
elements of `I` lifting the `e_i`. According to Nakayama's lemma, `(x_1, …, x_n)` is a basis of `I` over `R`. Let `N`
be the sub-`R`-module of `I` with basis `(x_1, …, x_r)` and let `B` be the quotient of the symmetric algebra of `N` by
the ideal generated by the elements `x^p`, for `x ∈ N`. Since every element of `I` has `p`-th power zero, one obtains a
morphism of `R`-algebras

```text
ψ : B ⟶ A.
```

According to 7.4.2, `ψ ⊗ k` is an isomorphism. It follows that `Coker ψ = 0` and that, denoting `K = Ker ψ`, the
morphism `τ : K ⊗ k → B ⊗ k` is zero. But since `ψ` is surjective and `A` is flat over `R`, then `τ` is also injective,
whence `K ⊗ k = 0`. On the other hand, since `A` is an `R`-module of finite presentation, `K` is an `R`-module of finite
type (cf. [BAC] I, § 2.8, Lemma 9), whence `K = 0` by Nakayama. So `ψ` is an isomorphism of `R`-algebras, and since
`ψ^{-1}(I)` contains the augmentation ideal `J` of `B`, it follows that `ψ^{-1}(I) = J`, and therefore `ψ^{-1}` induces
an isomorphism of `R`-modules from `I / I²` onto `J / J² = N`. This proves that `ω_{G/S}` is finite locally free, whence
the implication (iv) ⇒ (iii). This completes the proof of Theorem 7.4.

### Remark 7.5.

<!-- label: III.VII_A.7.5 -->

[^N.D.E-VII_A-74] It obviously follows from Theorems 7.2 and 7.4 that the functors `G ↦ Lie(G)` and `ℒ ↦ 𝔊_p(ℒ)` induce
equivalences, quasi-inverses of each other, between the category of `S`-groups locally of finite presentation and flat,
of height `⩽ 1`, and the full subcategory of that of `O_S`-`p`-Lie algebras formed by the finite locally free
`O_S`-`p`-Lie algebras.

[^N.D.E-VII_A-74]: We have added this remark.

## 8. The case of a base field

<!-- label: III.VII_A.8 -->
<!-- original page 470 -->

### 8.1.

<!-- label: III.VII_A.8.1 -->

Let us now summarize the results obtained in the case where `S` is the spectrum of a field `k` of characteristic
`p > 0`. Let us then say that a `k`-group scheme is *algebraic* if the underlying scheme is of finite type over `k`. In
this case, according to Theorem 7.2, one obtains:[^N.D.E-VII_A-75]

[^N.D.E-VII_A-75]: We have added the numbering 8.1.1 to 8.1.3, to highlight the results stated there.

#### Theorem 8.1.1.

<!-- label: III.VII_A.8.1.1 -->

*The functor `𝔊_p`, which to every `p`-Lie algebra `ℒ` of finite dimension over `k` associates the `k`-group `𝔊_p(ℒ)`,
is left adjoint to the functor which to every algebraic `k`-group `G` associates `Lie(G)`.*

Combining this with Theorem 7.4, one obtains:

#### Theorem 8.1.2.

<!-- label: III.VII_A.8.1.2 -->

*The functors `𝔊_p : ℒ ↦ 𝔊_p(ℒ)` and `G ↦ Lie(G)` induce equivalences, quasi-inverses of each other, between the
category of `p`-Lie algebras of finite dimension over `k`, and that of algebraic `k`-groups of height `⩽ 1`.*

Then, since `𝔊_p` is a left adjoint functor, it commutes with inductive limits,[^N.D.E-VII_A-76] hence in particular
with the formation of cokernels. On the other hand, if one has two morphisms `φ : G → H` and `φ' : G' → H` between
algebraic `k`-groups of height `⩽ 1`, then the fibered product `G ×_H G'` is again an algebraic `k`-group of height
`⩽ 1` (since the morphism `Fr : G → G^{(p)}` commutes with fibered products). So the inclusion of the category of
algebraic `k`-groups of height `⩽ 1` into that of all algebraic `k`-groups commutes with fibered products, hence in
particular with the formation of kernels. From this one deduces the:

[^N.D.E-VII_A-76]: We have expanded what follows, as well as the proof of the corollary below.

#### Corollary 8.1.3.

<!-- label: III.VII_A.8.1.3 -->

*The functor `𝔊_p` is exact, in the following sense. If `π : ℒ_1 → ℒ_2` is a surjective morphism between `p`-Lie
algebras of finite dimension over `k` and if `i` is the inclusion of `ℒ_0 = Ker π` in `ℒ_1`, one has an exact sequence
of algebraic `k`-groups:*

```text
1  ⟶  𝔊_p(ℒ_0)  ──𝔊_p(i)→  𝔊_p(ℒ_1)  ──𝔊_p(π)→  𝔊_p(ℒ_2)  ⟶  1.
```

[^N.D.E-VII_A-77]

[^N.D.E-VII_A-77]: Moreover, according to VI_A, 3.2, `𝔊_p(ℒ_2)` represents the (fppf) sheaf quotient of `𝔊_p(ℒ_1)` by
`𝔊_p(ℒ_0)`.

Indeed, according to what precedes, `𝔊_p(i)` induces an isomorphism of `𝔊_p(ℒ_0)` onto `Ker(𝔊_p(π))` (this kernel being
the same in the category of all algebraic `k`-groups `H` or in that of `H` of height `⩽ 1`), and
`𝔊_p(π) : 𝔊_p(ℒ_1) → 𝔊_p(ℒ_2)` identifies `𝔊_p(ℒ_2)` with the quotient of `𝔊_p(ℒ_1)` by `𝔊_p(ℒ_0)` in the category of
algebraic `k`-groups.

#### Remark 8.1.4.

<!-- label: III.VII_A.8.1.4 -->

[^N.D.E-VII_A-78] Let `φ : G → H` be a morphism of `k`-groups and `K = Ker(φ)`. Suppose `φ` covering for the (fpqc)
topology (this will be the case, in particular, if `φ` is covering for a less fine topology, for example the (fppf)
topology). Then, on the one hand, `φ` is a `K`-torsor above `H` (cf. IV 5.1.7.1). On the other hand, (cf. IV 6.3.1)
there exists a covering of `H` by affine opens `S_i`, and for each `i` an affine faithfully flat morphism `T_i → S_i`
factoring through `φ`. Then `G ×_H T_i` is `T_i`-isomorphic to `K × T_i`, hence faithfully flat over `T_i`, and
therefore, by (fpqc) descent, `G ×_H S_i → S_i` is faithfully flat, so that `φ` is faithfully flat.

[^N.D.E-VII_A-78]: We have added this remark, pointed out by O. Gabber, which will be useful in 8.3.1.

Conversely, if `φ` is faithfully flat and quasi-compact (resp. and locally of finite presentation), it is covering for
the (fpqc) topology (resp. (fppf)), cf. IV 6.3.1. Recall finally that a morphism of sheaves is covering if and only if
it is an epimorphism, cf. IV 4.4.3. One therefore obtains, in particular, that a quasi-compact morphism of `k`-groups
is faithfully flat if and only if it is an epimorphism of (fpqc) sheaves.

### 8.2. Proposition.

<!-- label: III.VII_A.8.2 -->

*Consider an exact sequence*[^N.D.E-VII_A-79] *of algebraic groups over a field `k` of characteristic `p > 0`*

```text
1  ⟶  G'  ──τ→  G  ──π→  G''  ⟶  1
```

[^N.D.E-VII_A-79]: i.e. `π` is faithfully flat and `i` is an isomorphism of `G'` onto `Ker π`, so that `G''` represents
the (fppf) sheaf quotient of `G` by `G'`, cf. VI_A, 3.2 and 5.2.

<!-- original page 496 -->

*and the following assertions:*

   *(i) The morphism `π` is smooth.*

   *(ii) `G'` is smooth.*

   *(iii) For every integer `n > 0`, the following sequence, induced by `τ` and `π`, is exact:*

<!-- original page 471 -->

```text
1 ⟶ Fr^n G' ⟶ Fr^n G ⟶ Fr^n G'' ⟶ 1.
```

   *(iv) The morphism `Fr π : Fr G → Fr G''` is an epimorphism of (fppf) sheaves.*

   *(v) The morphism `Lie(π) : Lie(G) → Lie(G'')` is surjective.*

*Then one has the implications (i) ⇔ (ii) ⇒ (iii) ⇒ (iv) ⇔ (v) and all the assertions are equivalent when `G` is smooth
over `k`.*

Indeed, (i) is equivalent to (ii) according to VI_B 9.2 (vii), and it is clear that (iii) implies (iv). On the other
hand, the equivalence of (iv) and (v) follows from 8.1.3.

The implication (ii) ⇒ (iii) follows from the diagram:

```text
       1  ⟶  G'  ──τ→  G  ──π→  G''  ⟶  1

          Fr^n(G'/k)     Fr^n(G/k)     Fr^n(G''/k)
                                                              
       1  ⟶  G'^{(p^n)}  ──τ^{(p^n)}→  G^{(p^n)}  ──π^{(p^n)}→  G''^{(p^n)}  ⟶  1
```

whose two rows are exact: since `Fr^n(G'/k)` is an epimorphism of (fppf) sheaves according to Corollary 8.3.1 below, `π`
induces an epimorphism of `Fr^n G` onto `Fr^n G''` (generalize the snake lemma to sheaves of groups not necessarily
commutative).

Similarly, when `G` is smooth over `k`, `Fr(G/k)` is an epimorphism, so if moreover `Fr π` is an epimorphism, the same
snake lemma applied to the diagram above for `n = 1` shows that `Fr(G'/k)` is an epimorphism, so `G'` is smooth over
`k`, according to 8.3.1 below.

### 8.3. Proposition.

<!-- label: III.VII_A.8.3 -->

*If `G` is a group locally of finite type*[^N.D.E-VII_A-80] *over a field `k` of characteristic `p > 0`, there exists
an integer `n_0` such that `G / (Fr^n G)` is smooth over `k` for `n ⩾ n_0`.*

[^N.D.E-VII_A-80]: We have replaced "algebraic" by "locally of finite type".

<!-- original page 472 -->

Since the construction of `G / (Fr^n G)` commutes with extension of the base field (4.1.1 and VI_A, 3.3.2), we may
suppose `k` perfect. In this case, `G_{red}` is a `k`-group locally of finite type (cf. VI_A 0.2) and one has the
following commutative and exact diagram, where one has denoted by `H` the `k`-scheme `G_{red} \ G`:

```text
       1  ⟶  G_{red}  ⟶  G  ⟶  H

              Fr^n(G_{red}/k)    Fr^n(G/k)     Fr^n(H/k)
                                                              
       1  ⟶  G_{red}^{(p^n)}  ⟶  G^{(p^n)}  ⟶  H^{(p^n)}.
```

Now `H` is the spectrum of a finite local `k`-algebra with residue field `k` (cf. VI_A, 5.6.1). Consequently, there
exists an integer `n_0` such that, for every `n ⩾ n_0`, `Fr^n(H/k)` factors through the "unit" section of `H^{(p^n)}`.
It follows that, for `n ⩾ n_0`, `Fr^n(G/k)` factors through `G_{red}^{(p^n)}` and therefore, according to VI_A, 5.4.1,
one has a commutative diagram

```text
                              Fr^n(G/k)
              G  ───────────────────→  G_{red}^{(p^n)}
                ╲                              ▲
              π  ╲                              │ i
                  ╲                              │
                   ╲                              │
                G / (Fr^n G)
```

where `i` is a closed immersion (and `π` is the canonical projection). Since moreover `i` induces a homeomorphism of
the underlying topological spaces, it is therefore an isomorphism. Since `k` is perfect, `G_{red}^{(p^n)}` is smooth
over `k` (VI_A, 1.3.1), and therefore `G / (Fr^n G)` is smooth over `k`, for every `n ⩾ n_0`.

#### 8.3.1. Corollary.

<!-- label: III.VII_A.8.3.1 -->

*Let `G` be a group locally of finite type over a field `k` of characteristic `p > 0` and let `n` be an integer
`⩾ 1`.*[^N.D.E-VII_A-81] *The following conditions are equivalent:*

   *(i) `G` is smooth over `k`.*

   *(ii) `Fr^n(G/k) : G → G^{(p^n)}` is an epimorphism of (fppf) sheaves.*

   *(iii) `Fr^n(G/k) : G → G^{(p^n)}` is faithfully flat.*

[^N.D.E-VII_A-81]: We have made explicit the equivalence between (ii) and (iii) and we have expanded the proof.

First, since `G` is locally of finite type over `k`, `Fr^n(G/k)` is of finite presentation, so the equivalence of (ii)
and (iii) follows from 8.1.4. Suppose `G` smooth over `k`, hence `G` reduced. Then, since `Fr^n(G/k)` is surjective, it
is faithfully flat (cf. VI_A, 6.2 or VI_B, 1.3).

Conversely, suppose `Fr^n(G/k)` faithfully flat. Since `Fr^n(G^{(p^n)}/k)` is deduced from `Fr^n(G/k)` by base change
(cf. 4.1.3), it is therefore also faithfully flat, as is the composition:

```text
Fr^{2n}(G/k) : G ⟶ G^{(p^n)} ⟶ G^{(p^{2n})}.
```

One thus obtains that, for every `m ∈ ℕ`, `Fr^{mn}(G/k) : G → G^{(p^{mn})}` is faithfully flat, hence induces an
isomorphism `G / (Fr^{mn} G) ≃ G^{(p^{mn})}` (cf. VI_A, 5.4.1). Now, according to Proposition 8.3, `G^{(p^{mn})}` is
smooth over `k` for `m` large, so `G` is also, by (fpqc) descent (cf. EGA IV₄, 17.7.1).

### 8.4.

<!-- label: III.VII_A.8.4 -->
<!-- original page 498 -->

In the two statements which end this Exposé, we return to the case of a field `k` of arbitrary characteristic.

When `k` is of characteristic 0 (resp. `p > 0`), let `n` be an integer `⩾ 1` (resp. an integer `⩾ 1` and coprime to
`p`); in both cases, we say simply that `n` is *coprime to the characteristic of `k`*. Moreover, if `G` is a group
scheme over `k`, we denote by `n_G : G → G` the morphism of `k`-schemes <!-- original page 473 --> which sends an
element `x` of `G(T)` to `x^n ∈ G(T)`, when `T` is a `k`-scheme.

**Proposition.** *Let `G` be an algebraic group over a field `k` and `n` an integer coprime to the characteristic of
`k`. Then `n_G : G → G` is an étale morphism.*

[^N.D.E-VII_A-82] According to VI_B 1.3, it suffices to show that `n_G` is étale at the origin. Let `A` be the local
ring of `G` at the origin and `I` the maximal ideal of `A`. According to II 3.9.4, the map
`Lie(n_G) : Lie(G) → Lie(G)`, which is induced by `n_G`, is the homothety of ratio `n`. It is therefore an isomorphism,
as is the endomorphism induced by `n_G` on `I / I² = Lie(G)^*`. If `k` is of characteristic 0, `G` is smooth over `k`
(VI_B 1.6.1, see also VII_B 3.3.1), so the canonical morphism `S(I / I²) → gr_I(A)` is an isomorphism, where `gr_I(A)`
denotes the graded module associated with the `I`-adic filtration. It follows that `n_G` induces an automorphism of
`gr_I(A)`, hence also of the completion `Â` of `A`, hence `n_G` is étale at the origin (cf. EGA IV₄, 17.6.3).

[^N.D.E-VII_A-82]: We have changed in the statement "étale at the origin" to "étale", and we have added the following
sentence.

If the characteristic is `p > 0` and if `G` is of height `⩽ 1`, then `A` is isomorphic to the quotient of the symmetric
algebra of `ω_{G/k} = I / I²` by the ideal generated by the `p`-th powers of the elements of `ω_{G/k}` (cf. 7.4); one
may then apply the "same" reasoning as in characteristic 0, and one obtains that `n_G` induces an automorphism of `A`.

If `G` is of height `⩽ r` and if we suppose our assertion proved for groups of height `⩽ r − 1`, denote by `B`, `A` and
`A'` the affine algebras of `Fr G`, `G` and `G' = Fr G \ G`, and `n_B`, `n_A` and `n_{A'}` the endomorphisms of `B`,
`A` and `A'` which are induced by `n_{Fr G}`, `n_G` and `n_{G'}`.[^N.D.E-VII_A-83] Let `I' = I ∩ A'` be the maximal
ideal of `A'`, since one has a cartesian square

```text
              Fr G  ────────→  G
                                          
                                          
                e ─────────→  G'
```

one has `B = A / I' A`. Observe that `n_{A'}` (resp. `n_B`) is none other than the endomorphism induced by `n_A` on
`A'` (resp. on `B`). According to VI_A 3.2, `A` is a faithfully flat `A'`-module, and since `A'` is an Artinian local
ring (`G'` being an algebraic `k`-group of height `⩽ r − 1`), it follows that `A` is a free `A'`-module. Since the
restriction of `n_A` to `A'` is `n_{A'}`, which is an isomorphism according to the inductive hypothesis, it follows
from Nakayama's lemma that `n_A` will be an automorphism if the endomorphism it induces on `A / I' A` is one.
<!-- original page 499 --> Now this endomorphism is none other than `n_B`, which is an automorphism since `B` is of
height `⩽ 1`. So `n_A` is an automorphism.

[^N.D.E-VII_A-83]: We have expanded the original in what follows.

Finally, when `G` is an arbitrary algebraic group over a field of characteristic `p > 0`, what precedes shows that
`n_G` induces automorphisms of the `k`-schemes `Fr^r G`; these schemes are affine over `k` and have as algebras the
quotients of the local algebra `A` by the ideal `I^{{p^r}}` generated by the `p^r`-th powers of the elements of `I`.
Since <!-- original page 474 --> `n_G` defines automorphisms of the algebras `A / I^{{p^r}}`, one sees by passage to
the projective limit that `n_G` induces an automorphism of `Â`, hence `n_G` is étale at the origin (EGA IV₄, 17.6.3).

### 8.5. Proposition.

<!-- label: III.VII_A.8.5 -->

*Let `G` be a finite algebraic group, of rank `n` over the field `k`. Then `n_G : G → G` is the zero morphism of `G`.*

Let us point out at once the following corollary, obtained by combining 8.4 and 8.5:[^N.D.E-VII_A-84]

[^N.D.E-VII_A-84]: We have added this corollary, indicated implicitly in the original by: "(confer 8.4)". For another
proof of the corollary, not using 8.5, see for example [TO70], Lemma 5.

#### Corollary 8.5.1.

<!-- label: III.VII_A.8.5.1 -->

*Let `G` be a finite algebraic group, of rank `n` over the field `k`. If `n` is coprime to the characteristic of `k`,
then `G` is étale over `k`.*

Let us now prove 8.5. Let `H` be a normal subgroup of `G` of rank `m` over `k`. Denote by `λ : H × G → G` the morphism
induced by the multiplication of `G`. Then, with the notations of VI_A 3.2, one has a cartesian square:

```text
              H × G  ──λ→  G
              pr_2          π
                              
                              
                G  ───→  H \ G.
```

Since `π : G → H \ G` is faithfully flat, quasi-compact (VI_A 3.2), and since `pr_2` is locally free of rank `m`, it
follows from EGA IV₂, 2.5.2, that `G → H \ G` is locally free of rank `m`. Denoting `r = rg_k(H \ G)`, one therefore has
`n = rg_k(G) = r m`.

On the other hand, one has an exact sequence of "abstract" groups

```text
1 ⟶ H(T) ⟶ G(T) ⟶ (H \ G)(T)
```

for every `k`-scheme `T`; it is therefore clear that `n_G` is zero if `m_H` and `r_{H \ G}` are. If one takes for `H`
the neutral component `G_0` of `G`, then `G_0 \ G` is étale (cf. VI_A 5.5.1), so that one may suppose `G` étale over `k`
or else infinitesimal (cf. 7.0).

If `G` is étale, one reduces, by extension of the base field, to the case where `k` is algebraically closed. In this
case, `G` is a constant group (cf. I 4.1), and the statement is classical.

If `G` is infinitesimal and non-zero, `k` is necessarily of characteristic `p > 0` (cf. VI_B 1.6.1 or VII_B 3.3.1); the
subgroups `Fr^n G` then form a composition series of `G`, whose quotients are of height `⩽ 1`. <!-- original page 475 -->

This reduces us to the case where `G` is of height `⩽ 1`. Let then `A` (resp. `L`) be the affine algebra (resp. the
Lie algebra) of `G` and `U = U_p(L)`. According to 7.4, one has `G = 𝔊_p(L)` whence `A = U^*`; so if `dim_k L = r`, the
rank of `G` over `k` is `p^r` (cf. 5.3.3). We shall therefore study the morphism `p_G : G → G` defined by raising to the
`p`-th power; it induces an endomorphism `p_A` of `A` and, by duality, an endomorphism `p_U` of `U`.

Let `I` be the augmentation ideal of `A`; we shall show that `p_A(I) ⊂ I^p`. Supposing this established, one will
therefore have `p_A^r(I) ⊂ I^{p^r}`. On the other hand, one knows that `I^{r(p−1)+1} = 0` (since `I` is generated by `r`
elements of `p`-th power zero). Since `p^r > r(p − 1)`, it follows that `p_A^r(I) = 0`, so `p_G^r` is the zero morphism.
It therefore remains to show the assertion:

```text
(∗)                          p_A(I) ⊂ I^p.
```

For every integer `s ⩾ 1`, we shall denote `m_A^{s-1} : A^{⊗s} → A` (resp. `∆_U^{s-1} : U → U^{⊗s}`) the map induced by
the multiplication `m_A` of `A` (resp. the comultiplication `∆_U` of `U`). Then `p_A` is equal to the following
composition:

```text
A ──∆_A^{p-1}→ A^{⊗p} ──m_A^{p-1}→ A,
```

and since the transpose of `m_A` (resp. `∆_A`) is `∆_U` (resp. `m_U`), the endomorphism `p_U = ᵗp_A` of `U` is the
following composition:

```text
U ──∆_U^{p-1}→ U^{⊗p} ──m_U^{p-1}→ U.
```

[^N.D.E-VII_A-85] Let `J` be the augmentation ideal of `U`; one has `U = k 1_U ⊕ J` and one will denote by `π` the
projection `U → J` of kernel `k 1_U`. For every integer `s ⩾ 1`, denote `(I^s)^⊥` the orthogonal of `I^s` in
`A^* = U`, i.e., `(I^s)^⊥` is the set of `u ∈ U` such that the composition below is zero:

```text
I^{⊗s} ──m_A^{s-1}→ I ──u→ k.
```

Since the transpose of `m_A` is `∆_U`, one sees that `(I^s)^⊥` is the vector subspace `P_{s-1}` formed by the
`u ∈ U` such that `∆_U^{s-1}(u)` vanishes on `I^{⊗s}`, i.e., denoting by `∆̄_U^{s-1}` the composition of `∆_U^{s-1}` and
the projection `π^{⊗s} : U^{⊗s} → J^{⊗s}`, one obtains that

```text
(I^s)^⊥ = P_{s-1} = Ker ∆̄_U^{s-1}
```

(see also VII_B, 1.3.6). So, to prove assertion `(∗)`, one must show that the transpose map `p_U = ᵗp_A` sends `P_{p-1}`
into `I^⊥ = k 1_U`. Since `p_U(1_U) = 1_U`, it suffices to show the assertion below, where `P^+_{p-1}` denotes
`J ∩ P_{p-1}`:

```text
(∗∗)                          p_U(P^+_{p-1}) = 0.
```

[^N.D.E-VII_A-85]: We have expanded the original in the paragraph that follows.

On the other hand, one shows easily, by induction on `s`, that `P^+_{s-1}` is the vector subspace of `U` generated by
the products `x_1 ··· x_t`, with `1 ⩽ t ⩽ s − 1` and `x_i ∈ L` (cf. VII_B <!-- original page 501 --> 4.3). Now, if
`x_1, x_2, …, x_t` are elements of `L`, one has:

```text
p_U(x_1 x_2 ··· x_t) = m_U^{p-1}( ∏_{j=1}^t ∑_{i=1}^p 1 ⊗ ··· ⊗ x_j ⊗ ··· ⊗ 1 )    (x_j in position i)
```

It is clear that the expression `∏_j ∑_i 1 ⊗ ··· ⊗ x_j ⊗ ··· ⊗ 1` is a sum of `p^t` terms `x_h` indexed by the maps `h`
from `{1, …, t}` into `{1, …, p}`.[^N.D.E-VII_A-86] Such a map `h` defines an ordered partition `p_h` of `{1, …, t}`
into at most `p` parts. Indeed, denote `i_1 < ··· < i_r` the elements of the image of `h` and, for `s = 1, …, r`, set
`I_s = h^{-1}(i_s)` and `x_{I_s} = ∏_{j ∈ I_s} x_j`, the product being taken in increasing order. Then `h` corresponds
to the `p`-tensor

```text
1 ⊗ ··· ⊗ x_{I_1} ⊗ ··· ⊗ x_{I_r} ⊗ ··· ⊗ 1
```

(where each `x_{I_s}` is in position `i_s`), and its image by `m_U^p` is the product:

```text
x_{I_1} ⊗ ··· ⊗ x_{I_r}
```

which depends only on the ordered partition `p = (I_1, …, I_r)`, and which one will denote `x_p`. For `p` fixed, `x_p`
is obtained for all choices of `i_1 < ··· < i_r` in `{1, …, p}`, and one therefore obtains the equality

```text
p_U(x_1 x_2 ··· x_t) = ∑_p (p choose n(p)) x_p,
```

where `p` ranges over the set of ordered partitions of `{1, …, t}` into at most `p` parts, and where `n(p)` denotes the
number of parts of `p`. (One has `1 ⩽ n(p) ⩽ min(t, p)`.)

[^N.D.E-VII_A-86]: We have expanded the original in what follows, replacing the notion of preorder by the equivalent
notion of ordered partition.

When `t < p`, all the terms `(p choose n(p))` are therefore zero, so that `p_U(x_1 ··· x_t) = 0`. <!-- original page 476 -->
So `p_U` vanishes on `P^+_{p-1}`, which proves assertion `(∗∗)`, and hence `(∗)`, and completes the proof of 8.5.

#### Corollary 8.5.2.

<!-- label: III.VII_A.8.5.2 -->

[^N.D.E-VII_A-87] *Let `S` be a reduced scheme and `G` a finite locally free `S`-group of rank `n`. Then
`n_G : G → G` is the zero morphism of `G`.*

[^N.D.E-VII_A-87]: We have added this corollary, signaled in Exp. VIII, Remark 7.3.1.

Indeed, let `S'` be the sum of the `Spec O_{S, η}`, for `η` ranging over the maximal points of `S`. Since `S` is
reduced, the morphism `S' → S` is schematically dominant, and the same holds for the morphism `f : G_{S'} → G`, since
`G` is finite locally free over `S` (cf. EGA IV₃, 11.10.5). Since `G → S` is affine, hence separated, the locus of
coincidence of `n_G` and the zero morphism is a closed subscheme of `G`, and it majorizes `f` according to 8.5, hence
equals `G`, i.e. `n_G` is the zero morphism.

#### Remark 8.5.3.

<!-- label: III.VII_A.8.5.3 -->

Let us also point out that, according to a theorem of P. Deligne (see [TO70], p. 4), if `G` is a commutative finite
locally free `S`-group of rank `n` over an arbitrary base `S`, then `n_G = 0`.

## Bibliography

- [BAlg] N. Bourbaki, *Algèbre*, Chap. I–III, Hermann, 1974, Chap. X, Masson, 1980.
- [BAC] N. Bourbaki, *Algèbre commutative*, Chap. I–IV, Masson, 1985.
- [BLie] N. Bourbaki, *Groupes et algèbres de Lie*, Chap. I, Hermann, 1971.
- [DG70] M. Demazure, P. Gabriel, *Groupes algébriques*, Masson & North-Holland, 1970.
- [Ja03] J. C. Jantzen, *Representations of algebraic groups*, Academic Press 1987; 2nd edition, Amer. Math. Soc., 2003.
- [TO70] J. Tate, F. Oort, *Groups schemes of prime order*, Ann. scient. Éc. Norm. Sup. 3 (1970), 1–21.

<!-- LEDGER DELTA — Exposé VII_A — for consolidation in Phase 3

| French | English | Note |
| ------ | ------- | ---- |
| déviation | deviation | Used both for `S`-deviation (composed pair `(u, d)`) and order-`n` deviation. Kept literal. |
| `S`-déviation d'ordre `⩽ n` | `S`-deviation of order `⩽ n` | Standard. |
| `S`-dérivation | `S`-derivation | Distinct from deviation; satisfies Leibniz rule. |
| algèbre infinitésimale | infinitesimal algebra | Per VII_A 2.1; modern usage: algebra of distributions (cf. [DG70]). |
| opérateur différentiel invariant à droite / à gauche | right-invariant / left-invariant differential operator | Standard. |
| translation à droite / à gauche | right / left translation | Standard. |
| coalgèbre / cogèbre | coalgebra | Bourbaki's *cogèbre* is rendered "cogebra" in N.D.E. quotations; main text uses "coalgebra". |
| coalgèbre en groupes | coalgebra in groups | Group object in the category of coalgebras. |
| comultiplication / morphisme diagonal | comultiplication / diagonal morphism | Both terms preserved. |
| antipodisme | antipode | Standard modern term. |
| élément primitif | primitive element | `∆u = u ⊗ 1 + 1 ⊗ u`. |
| dualité de Cartier | Cartier duality | Standard. |
| morphisme de Frobenius absolu / relatif | absolute / relative Frobenius morphism | Per VII_A 4.1 N.D.E. (41). |
| Verschiebung | Verschiebung | Loanword preserved per modern English usage. |
| `p`-algèbre de Lie (restreinte) | restricted `p`-Lie algebra | Title preference; modern English: restricted Lie algebra. First gloss provided. |
| puissance `p`-ième symbolique | symbolic `p`-th power | The operation `x ↦ x^{(p)}`. |
| algèbre enveloppante restreinte | restricted enveloping algebra | `U_p(𝔤)`. |
| très bon groupe / bon foncteur | very good group / good functor | Per II 4.4, 4.6, 4.10. |
| groupe radiciel de hauteur 1 | radicial group of height 1 | Section 7 title. *Radiciel* = purely inseparable per glossary. |
| hauteur ⩽ n | height ⩽ n | `Fr^n(G/S) = 0`. |
| produit symétrique p-uple | `p`-fold symmetric product | `Σ^p X`. |
| tenseur symétrisé | symmetrized tensor | Image of `N` operator. |
| Frobeniuseries | "Frobeniuseries" | Gabriel's coinage; kept with quotation marks as in source. |
| recouvrement (fpqc, fppf) | covering (for the (fpqc), (fppf) topology) | Per glossary. |
| schématiquement dominant | schematically dominant | Per EGA IV. |
| groupe infinitésimal | infinitesimal group | Per Definition 7.0. |
-->

