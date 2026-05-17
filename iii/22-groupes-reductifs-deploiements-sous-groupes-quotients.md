# Exposé XXII. Reductive groups: splittings, subgroups, quotient groups

<!-- label: III.XXII -->

*by M. Demazure*

<!-- original page 109 -->

[^N.D.E-XXII-0] This Exposé consists of two parts. The first (1 through 5.5) gathers the technical results needed for
the proof of the uniqueness and existence theorems. The second (5.6 to the end) will not be used in that proof; the end
of section 5 will be used in particular in Exposé XXVI on parabolic subgroups; section 6 establishes, in the
scheme-theoretic setting, the classical results on the derived group of a reductive group.

## 1. Roots and coroots. Split groups and root data

<!-- label: III.XXII.1 -->

**Theorem 1.1.** *Let `S` be a scheme, `G` an `S`-reductive group, `T` a maximal torus of `G`, `α` a root of `G`
relative to `T`.*

<!-- label: III.XXII.1.1 -->

*(i) There exists a unique morphism of groups with operator group `T`*

```text
expα : W(gα) → G
```

*inducing on the Lie algebras the canonical morphism `gα → g`. This morphism is a closed immersion. The corresponding
morphism*

```text
T ·α W(gα) → G
```

<!-- original page 110 -->

*is also a closed immersion.*

*If `pα : Ga,S → G` is a monomorphism normalized by `T` with multiplier `α`, there exists a unique
`Xα ∈ Γ(S, gα)×`[^N.D.E-XXII-1] such that `pα(x) = expα(xXα)`; one has `Lie(pα)(1) = Xα`, and the two preceding formulas
set up a bijective correspondence between `Γ(S, gα)×` and the set of monomorphisms `Ga,S → G` normalized by `T` with
multiplier `α`.*

*(ii) There exists a unique duality (denoted `(X, Y) ↦ XY`)*

```text
gα ⊗_{O_S} g_{-α} ⥲ O_S,
```

*and a unique morphism of groups*

```text
α* : Gm,S → T,
```

*such that formula (F) of Exp. XX 2.1 holds. One has*

```text
α ∘ α* = 2,     (-α)* = -α*,
```

*and `α*` is given by the formula of Exp. XX 2.7.*

Indeed, a morphism normalized by `T` with multiplier `α` factors necessarily through the closed subgroup
`Zα = Centr_G(Tα)` of `G` (cf. Exp. XIX 3.9). Now `(Zα, T, α)` is an `S`-elementary system (Exp. XX 1.4), and one is
reduced to the results of Exposé XX (1.5, 2.1, and 5.9).

**Remark 1.2.** *Part (i) of Theorem 1.1 remains valid if one only assumes that `α` is a character of `T`, non-trivial
on each fiber. Indeed, one then has a decomposition `S = S′ ∐ S′′` such that `α|S′` is a root of `G_{S′}` relative to
`T_{S′}` and `gα|S′′ = 0`. If `S = S′`, one is reduced to 1.1; if `S = S′′` the result is trivial; the general case
follows immediately.*

<!-- label: III.XXII.1.2 -->

**Notations 1.3.** *As in Exposé XX, we denote by `Uα` the image of `W(gα)`; it is a closed subgroup of `G`, equipped
canonically with a vector-space structure. We shall call it the* vector group associated with the root `α`. *We say that
`α*` is the* coroot associated with `α`. *Sections `Xα ∈ Γ(S, gα)` and `X_{-α} ∈ Γ(S, g_{-α})` are said to be* paired
*if `Xα · X_{-α} = 1`. Then `Xα ∈ Γ(S, gα)×` and likewise for `X_{-α}`. The corresponding morphisms `pα` and `p_{-α}`
are contragredient to one another in the sense of XX, 1.5,[^N.D.E-XXII-2] and one has*

<!-- label: III.XXII.1.3 -->

```text
pα(x) p_{-α}(y) = p_{-α}(y / (1 + xy)) · α*(1 + xy) · pα(x / (1 + xy)).
```

**Proposition 1.4.** *Under the conditions of 1.1, let `w ∈ Norm_G(T)(S)`. Then `β = α ∘ int(w)⁻¹ : T → Gm,S` is a root
of `G` relative to `T`, `β* = int(w) ∘ α*` is the corresponding coroot, and the following diagram is commutative:*

<!-- label: III.XXII.1.4 -->

```text
W(gα)  --expα-->  G
  |                |
Ad(w)            int(w)
  ↓                ↓
W(gβ)  --expβ-->  G.
```

Trivial: transport of structure.

**Definitions 1.5.** *(a) Under the conditions of 1.1, we denote by `sα` the automorphism of `T` defined by*

<!-- label: III.XXII.1.5 -->

```text
sα(t) = t · α*(α(t))⁻¹.
```

*We denote by `( , )` the canonical pairing:*

```text
Hom_{S-gr.}(Gm,S, T) × Hom_{S-gr.}(T, Gm,S) → Hom_{S-gr.}(Gm,S, Gm,S) = ℤ_S.
```

*Then `sα` operates on `Hom_{S-gr.}(T, Gm,S)`, resp. `Hom_{S-gr.}(Gm,S, T)`, by the following formulas, where `χ` (resp.
`u`) denotes an arbitrary section of `Hom_{S-gr.}(T, Gm,S)` (resp. of `Hom_{S-gr.}(Gm,S, T)`):*

```text
sα(χ) = χ − (α*, χ) α,
sα(u) = u − (u, α) α*.
```

*One has `sα ∘ sα = id` and `s_{-α} = sα`.*

*(b) If `X ∈ Γ(S, gα)×`, then the inner automorphism `wα(X)` of `T` defined by*

```text
wα(X) = expα(X) exp_{-α}(-X⁻¹) expα(X)
```

*(cf. Exp. XX 3.1) coincides with `sα` (loc. cit.). One then concludes from 1.4:*

**Corollary 1.6.** *Let `S` be a scheme, `G` an `S`-reductive group, `T` a maximal torus of `G`, `α` and `β` two roots
of `G` relative to `T`. Then*

<!-- label: III.XXII.1.6 -->

```text
sα(β) = β − (α*, β) α
```

*is a root of `G` relative to `T`, and the corresponding coroot is*

```text
sα(β)* = sα(β*) = β* − (β*, α) α*.
```

**Corollary 1.7.** *Under the preceding conditions, `α* = β*` implies `α = β`.*

<!-- label: III.XXII.1.7 -->

Indeed, if `α* = β*`, one has (cf. XXI.1.4)

```text
sβ(α) = α − 2β,    sα(β) = β − 2α,
```

and from this one deduces immediately

```text
(sβ sα)ⁿ(α) = α + 2n(β − α).
```

If `β ≠ α`, there exists `s ∈ S` such that `α_s ≠ β_s`. But then the preceding formula shows that there exist infinitely
many distinct roots of `G_s` relative to `T_s`, which is impossible.

**Definitions 1.8.0.**[^N.D.E-XXII-3] *If `u : Gm,S → T` is a morphism of groups, we shall say that `u` is a* coroot *of
`G` relative to `T` if there exists a root `α` of `G` relative to `T` such that `α* = u`. Consider the functor `R*` of
coroots of `G` relative to `T` defined as follows:*

<!-- label: III.XXII.1.8.0 -->

```text
R*(S′) = the set of coroots of G_{S′} relative to T_{S′}.
```

*If `R` is the functor of roots of `G` relative to `T` (Exp. XIX 3.8), one has a canonical morphism `R → R*`. By virtue
of 1.7 and Exp. XIX 3.8, one has:*

**Corollary 1.8.** *The canonical morphism `R → R*` is an isomorphism. In particular, `R*` is representable by a finite
twisted constant `S`-scheme, which is an open and closed subscheme of `Hom_{S-gr}(Gm,S, T)`.*

<!-- label: III.XXII.1.8 -->

This leads us to the following definition:

**Definition 1.9.** *Let `S` be a scheme, `T` an `S`-torus. We call* twisted root datum *in `T` the data:*

<!-- label: III.XXII.1.9 -->

*(i) a finite subscheme `R` of `Hom_{S-gr.}(T, Gm,S)`,*

*(ii) a finite subscheme `R*` of `Hom_{S-gr.}(Gm,S, T)`,*

*(iii) an isomorphism `R ⥲ R*` denoted `α ↦ α*`,*

*satisfying the following conditions:*

```text
(DR 1)  For every S′ → S and every α ∈ R(S′), one has α ∘ α* = 2.
(DR 2)  For every S′ → S and every α, β ∈ R(S′), one has
        α − (β*, α) β ∈ R(S′),    α* − (α*, β) β* ∈ R*(S′).
```

*Moreover, if for `α ∈ R(S′)` (`S′ ≠ ∅`) one has `2α ∉ R(S′)`, the root datum is said to be* reduced.

**Proposition 1.10.** *Let `S` be a scheme, `G` an `S`-reductive group, `T` a maximal torus of `G`, `R` (resp. `R*`) the
scheme of roots (resp. of coroots) of `G` relative to `T`. Then `(R, R*)` is a reduced twisted root datum in `T`.*

<!-- label: III.XXII.1.10 -->

The only thing that remains to be checked is that this twisted root datum is reduced. This was done in Exp. XIX 3.10.

### 1.11.

<!-- label: III.XXII.1.11 -->

Let `T = D_S(M)` be a trivialized torus. If we denote by `M*` the abelian group dual to `M`, we have canonical
isomorphisms (cf. Exp. VIII 1.5):

```text
Hom_{S-gr.}(T, Gm,S) ⥲ M_S,
Hom_{S-gr.}(Gm,S, T) ⥲ M*_S,
```

hence isomorphisms of groups:

```text
Hom_{S-gr.}(T, Gm,S) → Hom_{loc.const.}(S, M),
Hom_{S-gr.}(Gm,S, T) → Hom_{loc.const.}(S, M*).
```

A character of `T` (resp. a morphism of groups `Gm,S → T`) will be called *constant* (relative to the given
trivialization) if the preceding isomorphism transforms it into a constant map from `S` to `M` (resp. `M*`).

### 1.12.

<!-- label: III.XXII.1.12 -->

With the same notations, let `(M, M*, R, R*)` be a root datum (Exp. XXI). Then `(R_S, R*_S)` is a twisted root datum in
`T`. Conversely, if `(R, R*)` is a twisted root datum in a torus `T`, a *splitting* of this root datum is the data of an
ordinary root datum `(M, M*, R, R*)` together with an isomorphism `T ≃ D_S(M)` that transforms `(R, R*)` into
`(R_S, R*_S)`.

**Definition 1.13.** *Let `S` be a scheme, `G` an `S`-reductive group, `T` a maximal torus of `G`. We call* splitting
*of `G` relative to `T` the data*

<!-- label: III.XXII.1.13 -->

*(i) of an abelian group `M` and an isomorphism `T ≃ D_S(M)`,*

*(ii) of a system of roots `R` of `G` relative to `T` (Exp. XIX 3.6),*

*satisfying the following two conditions:*

*(D₁) `S` is non-empty and the roots `α ∈ R` (resp. the corresponding coroots) are identified with constant functions
from `S` to `M` (resp. `M*`).*

*(D₂) The `gα` (`α ∈ R`) are free `O_S`-modules.*

*We say that `G` is* splittable *relative to `T` if there exists a splitting of `G` relative to `T`. By a* splitting of
`G` *we mean the data of a maximal torus `T` of `G` and a splitting of `G` relative to `T`. We say that `G` is*
splittable *if there exists a splitting of `G`. By an* `S`-split group *we mean an `S`-reductive group equipped with a
splitting; we denote it by a symbol of the form `(G, T, M, R)`, or simply `G` when there is no risk of confusion.*

Condition (D₁) entails that `R` (resp. `R*`) is canonically identified with a subset of `M` (resp. `M*`).

**Proposition 1.14.** *Let `S` be a scheme (non-empty), `(G, T, M, R)` an `S`-split group. Then*

<!-- label: III.XXII.1.14 -->

```text
R(G, T, M, R) = (M, M*, R, R*)
```

*is a reduced root datum (Exp. XXI 1.1 and 2.1.3); it is a splitting of the twisted root datum of 1.10.*

This is a trivial consequence of 1.10 and Exp. XIX 3.7.

We shall sometimes write, for simplicity, `R(G, T, M, R) = R(G)`. We shall systematically use the notations `V`, `V(R)`,
`W`, … of Exp. XXI.

**Remark 1.15.** *(a) If `S` is connected non-empty (resp. if `Pic(S) = 0`), the condition (D₁) (resp. (D₂)) is
automatically satisfied.*

<!-- label: III.XXII.1.15 -->

*(b) If `(G, T, M, R)` is an `S`-split group, then for every `S′ → S`, `S′ ≠ ∅`, `(G_{S′}, T_{S′}, M, R)` is an
`S′`-split group, and `R(G, T, M, R) = R(G_{S′}, T_{S′}, M, R)`.*

### 1.16.

<!-- label: III.XXII.1.16 -->

Let `T = D_S(M)` be a trivialized torus. The Lie algebra `t` of `T` is canonically identified (Exp. II 5.1.1) with

```text
t ≃ M* ⊗ O_S.
```

For every morphism of groups `u : T → Gm,S`, `Lie(u)` is a linear form

```text
Lie(u) : t → O_S = Lie(Gm,S/S).
```

In particular, if `u` is defined by an element `α ∈ M`, then `Lie(u)` is the linear form `α` on `M* ⊗ O_S` defined by
`α`:

```text
α(m ⊗ x) = (m, α) x.
```

Symmetrically, for every morphism of groups `h : Gm,S → T`, `Lie(h)` is an `O_S`-morphism `O_S = Lie(Gm,S/S) → t`,
canonically defined by the section

```text
H = Lie(h)(1) ∈ Γ(S, t).
```

In particular, if `h` is defined by an element `m ∈ M*`, one has

```text
H = Lie(h)(1) = m ⊗ 1.
```

Comparing the two definitions, one finds in particular

```text
α(H) = (h, α) · 1 ∈ Γ(S, O_S).
```

### 1.17.

<!-- label: III.XXII.1.17 -->

These definitions apply in particular to the case where `T` is the maximal torus of a split group. Each root `α ∈ R`
defines an *infinitesimal root* `α ∈ Hom_{O_S}(t, O_S)` with

```text
α(m ⊗ x) = (m, α) x.
```

Each coroot `α* ∈ R*` defines an *infinitesimal coroot*

```text
Hα ∈ Γ(S, t),    Hα = α* ⊗ 1.
```

For `α, β ∈ R`, one has the relation

```text
α(Hβ) = (β*, α) · 1,
```

and in particular

```text
α(Hα) = 2.
```

In particular, if `2` is invertible on `S`, then `α` and `Hα` are non-zero on each fiber.

## 2. Existence of a splitting. Type of a reductive group

<!-- label: III.XXII.2 -->

<!-- original page 114 -->

**Proposition 2.1.** *Let `S` be a scheme, `G` an `S`-reductive group, `T` a maximal torus of `G`. Suppose `T` is split.
Then `G` is locally splittable relative to `T`: for every `s₀ ∈ S`, there exists an open neighborhood `U` of `s₀` such
that the `U`-group `G_U` is splittable relative to `T_U`.*

<!-- label: III.XXII.2.1 -->

Indeed, write `T ≃ D_S(M)` and

```text
g = ⨿_{m ∈ M} g^m.
```

Let `R = { m ∈ M | m ≠ 0, g^m(s₀) ≠ 0 }`. Shrinking `S` if necessary (replacing it by an open neighborhood of `s₀`), we
may suppose that the `gα`, `α ∈ R`, are free, and that the `g^m`, `m ≠ 0`, `m ∉ R`, are zero. We then have

```text
g = t ⨿ ⨿_{α ∈ R} gα,
```

with the `gα` free of rank 1. It follows that `R` is a system of roots of `G` relative to `T` (Exp. XIX 3.6). The
coroots `α*` corresponding to the `α ∈ R` are then identified with locally constant functions on `S` with values in
`M*`. Shrinking `S` further, we may take them constant, and we are done.

Note that the proof gives immediately:

**Proposition 2.2.** *Let `S` be a non-empty connected scheme with `Pic(S) = 0`, for example `Spec(ℤ)` or a local scheme
(in particular the spectrum of a field). If `G` is an `S`-reductive group possessing a split maximal torus `T`, then `G`
is splittable relative to `T`.*

<!-- label: III.XXII.2.2 -->

We deduce immediately from 2.1 and the fact that a reductive group locally possesses maximal tori for the étale topology
(Exp. XIX 2.5):

**Corollary 2.3.** *Let `S` be a scheme, `G` an `S`-reductive group (resp. and `T` a maximal torus of `G`). Then `G` is
locally splittable (resp. locally splittable relative to `T`) for the étale topology on `S`.*

<!-- label: III.XXII.2.3 -->

**Corollary 2.4.** *Let `k` be a field, `G` a `k`-reductive group. There exists a finite separable extension `K/k` such
that `G_K` is splittable.*

<!-- label: III.XXII.2.4 -->

**Remark 2.5.** *Using 2.1 and the remark Exp. XIX 2.9, one immediately proves the following result: let
`G = (G, T, M, R)` be an `S`-split group; there exists a cover of `S` by open sets `Uᵢ` such that each split group
`G_{Uᵢ}` arises by base change from a split group over a noetherian ring (in fact, a finitely generated `ℤ`-algebra). We
will furthermore prove that every split group over `S` already arises from a `ℤ`-split group (Exp. XXV).*

<!-- label: III.XXII.2.5 -->

### 2.6.

<!-- label: III.XXII.2.6 -->

Let `k` be an algebraically closed field and `G` a `k`-reductive group. One knows (e.g. by 2.4) that there exist
splittings of `G`. Let `(G, T, M, R)` and `(G, T′, M′, R′)` be two splittings of `G`; the root data `R(G, T, M, R)` and
`R(G, T′, M′, R′)` are then isomorphic.

Indeed, one sees first that one can reduce to the case where `T = T′` (because there exists `g ∈ G(k)` such that
`T′ = int(g) T`, and one verifies easily that if one transports a splitting by an automorphism of `G`, one obtains a
root datum isomorphic to the initial datum); but since `S = Spec(k)` is connected, the isomorphism
`D_k(M) ⥲ T ⥲ D_k(M′)` arises from a unique isomorphism `M ≃ M′`; for the same reason, there is at most one system of
roots of `G` relative to `T`.

**Definition 2.6.1.**[^N.D.E-XXII-4] *If `G` is a `k`-reductive group (`k` an algebraically closed field), we call* type
of `G` *the isomorphism class of the root datum defined by an arbitrary splitting of `G`; if `G` is a torus, of type `M`
in the sense of Exp. IX 1.4, then the type of `G` as reductive group is given by the trivial root datum
`(M, M*, ∅, ∅)`.*

<!-- label: III.XXII.2.6.1 -->

By 1.15 (b),[^N.D.E-XXII-5] the type is invariant under (algebraically closed) extension of the base field.

**Definition 2.7.** *If `G` is an `S`-reductive group and `s ∈ S`, we call* type of `G` at `s` *the type of the
`s`-reductive group `G_s`.*

<!-- label: III.XXII.2.7 -->

For every `S′ → S` and every `s′ ∈ S′` projecting to `s ∈ S`, the type of `G_{S′}` at `s′` is equal to the type of `G`
at `s`.

If `G` is splittable, and if `(G, T, M, R)` is a splitting of `G`, then the type of `G` at `s` is the isomorphism class
of `R(G, T, M, R)` by 1.15 (b).[^N.D.E-XXII-5] It then follows immediately from 2.3:

**Proposition 2.8.** *Let `G` be an `S`-reductive group (`S ≠ ∅`). The function*

<!-- label: III.XXII.2.8 -->

```text
s ↦ type of G at s
```

*is locally constant on `S`. In particular, there is a partition of `S` into non-empty open subschemes such that on each
of them `G` is of constant type. More precisely, let `E` be the set of types of the fibers of `G`; for every `t ∈ E`,
let `S_t` be the set of points `s ∈ S` where `G` is of type `t`; then `(S_t)_{t ∈ E}` is a partition of `S` and each
`S_t` is open and closed (and non-empty).*

## 3. The Weyl group

<!-- label: III.XXII.3 -->

<!-- original page 118 -->

### 3.1.

<!-- label: III.XXII.3.1 -->

Let `S` be a scheme, `G` an `S`-reductive group, `T` a maximal torus of `G`. Then

```text
W_G(T) = Norm_G(T)/T
```

is a finite étale `S`-group (Exp. XIX 2.5). The morphism `n ↦ int(n)` induces, by passage to the quotient, a canonical
monomorphism (which is in fact an open immersion):

```text
W_G(T) → Aut_{S-gr.}(T).
```

### 3.2.

<!-- label: III.XXII.3.2 -->

Suppose now that `G` is splittable relative to `T`. Choose a splitting, say `(G, T, M, R)`. We then have a canonical
isomorphism (Exp. VIII 1.5)

```text
Aut_{S-gr.}(T) ≃ (Aut_{gr.}(M))_S.
```

In particular, if `W` is the Weyl group of the root datum `R(G)` (Exp. XXI 1.1.8), we have a monomorphism

```text
W_S → Aut_{S-gr.}(T).
```

### 3.3.

<!-- label: III.XXII.3.3 -->

For each root `α ∈ R`, the symmetry `sα ∈ W` operates on `M` by

```text
sα(x) = x − (α*, x) α,
```

hence on `T` (via the preceding morphism) by

```text
sα(t) = t · α*(α(t))⁻¹.
```

On the other hand, since `gα` is assumed free, there exists `X ∈ Γ(S, gα)×`. Consider `wα(X) ∈ Norm_G(T)(S)` (Exp. XX
3.1). One has (loc. cit.)

```text
int(wα(X))(t) = sα(t).
```

Since `W` is generated by the `sα`, `α ∈ R`, it follows from the preceding remarks that if we regard `W` and
`Norm_G(T)(S)/T(S)` as groups of automorphisms of `T`, we have

```text
W ⊂ Norm_G(T)(S)/T(S) ⊂ W_G(T)(S).
```

By definition of the constant group `W_S` associated with `W` (cf. I 1.8), we thus have a commutative diagram

```text
W_S  ──────────→  W_G(T)
   ↘                ↙
       Aut_{S-gr.}(T).
```

**Proposition 3.4.** *Let `S` be a scheme, `(G, T, M, R)` an `S`-split group, `W` the Weyl group of the root datum
`R(G)`. Then the canonical monomorphism*

<!-- label: III.XXII.3.4 -->

```text
W_S → W_G(T) = Norm_G(T)/T
```

*is an isomorphism.*

These are both étale groups over `S`; it therefore suffices to check that for every `s ∈ S`, `W_S(s) → W_G(T)(s)` is an
isomorphism.[^N.D.E-XXII-6] The latter assertion follows, for example, from *Bible*, § 11.3, th. 2.

**Remark 3.5.** *Using 2.3, the preceding proposition gives a new proof of the fact that the Weyl group of a maximal
torus of an `S`-reductive group `G` is finite over `S` (Exp. XIX 2.5 (ii)).*[^N.D.E-XXII-7]

<!-- label: III.XXII.3.5 -->

### 3.6.

<!-- label: III.XXII.3.6 -->

Under the conditions of 3.1, for every `w ∈ W_G(T)(S)`, we denote by `N_w`[^N.D.E-XXII-8] the fiber product of the
following diagram:

```text
N_w  ────→  Norm_G(T)
 |              |
 ↓              ↓ w
 S    ────→  W_G(T).
```

This is an open and closed subscheme of `Norm_G(T)`, which is a principal homogeneous bundle under `T` on the left
(resp. on the right) by the law `(t, q) ↦ tq` (resp. `(q, t) ↦ qt`). If `n ∈ N_w(S)`, one has

```text
N_{ww′} = n · N_{w′},    N_{w′w} = N_{w′} · n.
```

### 3.7.

<!-- label: III.XXII.3.7 -->

In particular, if `α` is a root of `G` relative to `T`, `N_{sα}` is none other than what was denoted `N×` in Exp. XX
3.0. If `gα` is free on `S`, one then has `N_{sα}(S) ≠ ∅`.

By 3.4 and condition (D₂) of the splitting, we deduce:

**Corollary 3.8.** *Under the conditions of 3.4, the morphism*

<!-- label: III.XXII.3.8 -->

```text
Norm_G(T)(S) → W_G(T)(S) = Hom_{loc.cons.}(S, W)
```

*is surjective. In particular, for every `w ∈ W`, there exists `n_w ∈ Norm_G(T)(S)` such that `int(n_w)|T = w`.*

## 4. Homomorphisms of split groups

<!-- label: III.XXII.4 -->

<!-- original page 121 -->

### 4.1. The "big cell"

<!-- label: III.XXII.4.1 -->

#### 4.1.1.

<!-- label: III.XXII.4.1.1 -->

Let `(G, T, M, R)` be a split `S`-reductive group. Choose a system of positive roots (Exp. XXI 3.2.1) `R+` of the root
datum `R(G)`. Set `R− = −R+`.

Choose a total ordering on `R+` (resp. `R−`) and consider the morphism induced by the product in `G`

```text
u : ∏_{α ∈ R−} Uα ×_S T ×_S ∏_{α ∈ R+} Uα → G.
```

This is an open immersion. Indeed, since both sides are flat and of finite presentation over `S`, it suffices to verify
this on each geometric fiber (SGA 1, I 5.7 and VIII 5.4); one is thus reduced to the case where `S` is the spectrum of
an algebraically closed field; but, by *Bible*, § 13.4, cor. 2 to th. 3, `u` is radicial and dominant; since the tangent
map of `u` at the origin is an isomorphism (definition of a system of roots), `u` is birational; but `G` being normal,
one may apply Zariski's "Main Theorem" (EGA III₁, 4.4.9) and `u` is an open immersion.

Let us show that the image `Ω` of this open immersion is independent of the ordering chosen on `R+` (resp. `R−`). Since
this is a question of comparing open subsets of `G`, one is reduced to proving that they have the same geometric points,
so one may again assume that `S` is the spectrum of an algebraically closed field. Then the assertion is none other than
*Bible*, § 13, prop. 1 (c) and th. 1 (a).

We have thus proved:

**Proposition 4.1.2.** *Let `(G, T, M, R)` be an `S`-split group. Let `R+` be a system of positive roots of `R`. There
exists an open subset `Ω_{R+}` of `G` such that for every total ordering on `R+` (resp. `R−`), the morphism induced by
the product in `G`*

<!-- label: III.XXII.4.1.2 -->

```text
∏_{α ∈ R−} Uα ×_S T ×_S ∏_{α ∈ R+} Uα → G
```

*is an open immersion with image `Ω_{R+}`.*

**Remark 4.1.3.** *One can translate 4.1.2 as follows: choose, for every `α ∈ R`, an isomorphism of vector groups
`pα : Ga,S ⥲ Uα` (cf. 1.19); then the morphism (set `N = Card(R+) = Card(R−)`)*

<!-- label: III.XXII.4.1.3 -->

```text
Ga,S^N ×_S T ×_S Ga,S^N → G
```

*defined set-theoretically by*

```text
((xα)_{α ∈ R−}, t, (xα)_{α ∈ R+}) ↦ ∏_{α ∈ R−} pα(xα) · t · ∏_{α ∈ R+} pα(xα)
```

*is an open immersion whose image depends only on `R+` (and not on the choice of the `pα` or the orderings on `R+` and
`R−`).*

**Notation 4.1.4.** *We write `Ω_{R+} = ∏_{α ∈ R−} Uα · T · ∏_{α ∈ R+} Uα`.*[^N.D.E-XXII-9]

<!-- label: III.XXII.4.1.4 -->

**Proposition 4.1.5.** *The scheme `Ω_{R+}` is of finite presentation over `S` (hence retrocompact in `G`) and is
universally schematically dense in `G` relative to `S` (cf. Exp. XVIII 1).*

<!-- label: III.XXII.4.1.5 -->

The first assertion is trivial. Then,[^N.D.E-XXII-10] `Ω_{R+}` is flat and of finite presentation over `S`, and contains
the unit section, hence meets each fiber of `G` in a non-empty open subset, hence in a dense one; the second assertion
follows from Exp. XVIII 1.3.[^N.D.E-XXII-11]

**Corollary 4.1.6.** *Let `(G, T, M, R)` be a split `S`-reductive group. Then*

<!-- label: III.XXII.4.1.6 -->

```text
Centr(G) = ⋂_{α ∈ R} Ker(α).
```

[^N.D.E-XXII-12]

*Consequently, `Centr(G)` is representable by a closed diagonalizable subgroup of `G`.*

The second assertion follows immediately from the first. To prove the latter, one may invoke Exp. XII 4.8 and 4.11; one
may also proceed directly as follows.[^N.D.E-XXII-13]

Let `S′ → S`. If `t ∈ T(S′)` and `α(t) = 1` for every `α ∈ R`, then `int(t)` induces the identity on `T_{S′}` and on
each `(Uα)_{S′}`, `α ∈ R`, hence also on `(Ω_{R+})_{S′}`, hence on `G_{S′}` by schematic density, whence
`t ∈ Centr(G)(S′)`.

Conversely, since `Centr_{G_{S′}}(T_{S′}) = T_{S′}` (cf. Exp. XIX 2.8), if `g ∈ G(S′)` centralizes `T_{S′}` and the
`(Uα)_{S′}`, it is a section of `T_{S′}` that annihilates the `α ∈ R`.

**Corollary 4.1.7.** *Let `S` be a scheme, `G` an `S`-reductive group. Then the center of `G` is representable by a
closed subgroup of `G`, of multiplicative type; it is also "the intersection of the maximal tori of `G`" in the
following sense: for every `S′ → S`, `Centr(G)(S′)` is the set of `g ∈ G(S′)` whose inverse image in `G(S′′)`, for every
`S′′ → S′`, is contained in all the `T(S′′)`, where `T` runs through the set of maximal tori of `G_{S′′}`.*

<!-- label: III.XXII.4.1.7 -->

Taking into account 2.3, the first assertion follows from 4.1.6 by descent.[^N.D.E-XXII-14] Let us prove the second
assertion. Let `H` be "the intersection of the maximal tori of `G`" in the preceding sense. One obviously has
`Centr(G) ⊂ H`.[^N.D.E-XXII-15] Then, by descent, it suffices to prove `Centr(G) = H` in the case where `G` is split.
Since `H` is contained in the intersection of the maximal tori of `G` in the usual sense, this follows from the
following remark: if `(G, T, M, R)` is a splitting, `α ∈ R` and `X ∈ Γ(S, gα)×`, then `int(expα(X))(T) ∩ T = Ker(α)`, as
a trivial computation shows. (Cf. also Exp. XII 8.6 and 8.8 for a more general statement.)

**Remark 4.1.8.** *In what follows, we shall systematically identify, in the split case, `T` with `D_S(M)`. Then
`Centr(G)` is none other than `D_S(M/Γ₀(R))`, where `Γ₀(R)` is the subgroup of `M` generated by `R` (cf. Exp. XXI
1.1.6). If `{α₁, α₂, …, αₙ}` is a system of simple roots of `R`, one immediately has (cf. Exp. XX 1.19):*

<!-- label: III.XXII.4.1.8 -->

```text
Centr(G) = ⋂ Ker(αᵢ) = ⋂ Centr(Z_{αᵢ}).
```

**Proposition 4.1.9.** *Let `S` be a scheme, `(G, T, M, R)` an `S`-split group, `Q` an `S`-torus, `α₀` a character of
`Q`, `L` an invertible `O_S`-module,*

<!-- label: III.XXII.4.1.9 -->

```text
f : Q → T,    p : W(L) → G
```

*morphisms of groups satisfying the set-theoretic relation*

```text
p(α₀(q) x) = int(f(q)) · p(x),
```

*for all `q ∈ Q(S′)`, `x ∈ W(L)(S′)`, `S′ → S`. Suppose that `f` separates the elements of `R` in the following sense:
if `α, α′ ∈ R` and `m, m′ ∈ ℤ`, then `m α ∘ f = m′ α′ ∘ f` implies `m α = m′ α′`.[^N.D.E-XXII-16] Finally, let `s ∈ S`
be such that `(α₀)_s ≠ e` and `p_s ≠ e`.*

*There then exist an open set `U` of `S` containing `s`, an integer `q > 0` such that `x ↦ x^q` is an endomorphism of
`Ga,U`, a root `α ∈ R`, and an isomorphism of `O_U`-modules*

```text
h : (L|U)^{⊗q} ⥲ gα|U
```

*such that*

*(i) `(α ∘ f)|U = (q α₀)|U`,*

*(ii) `p(X) = expα(h(X^q))` for every `X ∈ W(L)(S′)`, `S′ → U`.*

*Moreover, once `U` is chosen, `q`, `α` and `h` are uniquely determined.*

Shrinking `S` if necessary, we may suppose that `α₀` is non-zero on every fiber of `S`. Choose a system of positive
roots `R+` of `R` and let `V = p⁻¹(Ω_{R+})`. This is an open subset of `W(L)` containing the zero section and stable
under multiplication by every `α₀(q)`, `q ∈ Q(S′)`, `S′ → S`. Since `α₀` is non-trivial on every fiber, it follows
immediately that `V = W(L)`, hence that `p` factors through `Ω_{R+}`. Choose an arbitrary ordering on `R+` and `R−`; all
products will be taken in this ordering. We thus have unique morphisms

```text
aα : W(L) → Uα,    α ∈ R,
b  : W(L) → T
```

such that

```text
p(x) = ∏_{α ∈ R−} aα(x) · b(x) · ∏_{α ∈ R+} aα(x).
```

Writing the covariance condition under `Q`, one obtains immediately

```text
aα(α₀(q) x) = α(f(q)) aα(x),    α ∈ R,
b(α₀(q) x)  = b(x)
```

for all `x ∈ W(L)(S′)`, `q ∈ Q(S′)`, `S′ → S`. The second condition gives at once `b = e`.

Now let `α ∈ R` be such that `(aα)_s ≠ e` (we know such an `α` exists, since `p_s` is supposed `≠ e`). Applying Exp. XIX
4.12 (a), one deduces that there exists an integer `n > 0` such that `(α ∘ f)_s = (n α₀)_s`. Shrinking `S`, one can
assume `α ∘ f = n α₀` (Exp. IX 5.3). But then, for every `α′ ∈ R`, `α′ ≠ α`, one has `(α′ ∘ f)_s ≠ m α₀` for every
integer `m > 0`, by virtue of the hypothesis made on `f` (and the fact that the only roots proportional to `α` are `α`
and `−α`). Applying again Exp. XIX 4.12 (a), this time to `aα′`, one deduces that `aα′` is zero in a neighborhood of
`S`; since `R` is finite, one may, shrinking `S` again, suppose the `aα′` zero for `α′ ∈ R`, `α′ ≠ α`. One then has
`p = aα`, and one may apply Exp. XIX 4.12 (b), then (c), which gives the announced result (the uniqueness assertions are
obvious).

**Remark 4.1.10.** *The condition imposed on `f` in 4.1.9 is satisfied in particular when `f` is surjective (=
faithfully flat).*

<!-- label: III.XXII.4.1.10 -->

**Proposition 4.1.11.** *Let `(G, T, M, R)` be an `S`-split group, `R+` a system of positive roots of `R`, `Ω_{R+}` the
corresponding "big cell".*

<!-- label: III.XXII.4.1.11 -->

*(i) Let `H` be a separated `S`-group functor[^N.D.E-XXII-17] for (fppf). If `f, g : G ⇒ H` are two morphisms of groups
that coincide on `Ω_{R+}`, then `f = g`.*

*(ii) Let `H` be an `S`-sheaf of groups for (fppf) and `f : Ω_{R+} → H` an `S`-morphism satisfying the following
condition: for every `S′ → S` and every `x, y ∈ Ω_{R+}(S′)` such that `xy ∈ Ω_{R+}(S′)`, one has `f(xy) = f(x) f(y)`.
There then exists a (unique, by (i)) morphism of groups `f̄ : G → H` extending `f`.*

Indeed, by 4.1.5, (i) (resp. (ii)) follows immediately from Exp. XVIII 2.2 (resp. 2.3 and 2.4).

**Remark 4.1.12.** *If `α ∈ R+`, one has*

<!-- label: III.XXII.4.1.12 -->

```text
(†)    Ω_{R+} ∩ Zα = U_{-α} · T · Uα.
```

[^N.D.E-XXII-18] Indeed, for every `S′ → S`, if `g = ∏_{β ∈ R−} pβ(xβ) · t · ∏_{β ∈ R+} pβ(xβ)` is an element of
`Ω_{R+}(S′)` and if `t′ ∈ Tα(S′′)`, then

```text
t′ g t′⁻¹ = ∏_{β ∈ R−} pβ(β(t′) xβ) · t · ∏_{β ∈ R+} pβ(β(t′) xβ)
```

and since `α` and `−α` are the only two elements of `R` that take the value 1 on `Tα`, we obtain that `g` belongs to
`Zα = Centr(Tα)` if and only if `xβ = 0` for `β ≠ ±α`.

By (†), one deduces from XX 2.1 that if `X ∈ Γ(X, gα)` and `Y ∈ Γ(S, g_{-α})`, one has:

```text
expα(X) exp_{-α}(Y) ∈ Ω_{R+}(S) ⇔ 1 + XY invertible.
```

### 4.2. Morphisms of split groups

<!-- label: III.XXII.4.2 -->

**Definition 4.2.1.** *Let `S` be a scheme (non-empty), `(G, T, M, R)` and `(G′, T′, M′, R′)` two `S`-split groups. We
say that the morphism of `S`-groups `f : G → G′` is* compatible with the splittings, *or defines a* morphism of split
groups, *if the restriction of `f` to `T` factors through a morphism `f_T : T → T′` of the form `f_T = D_S(h)`, where
`h : M′ → M` is a morphism of groups satisfying the following condition:*

<!-- label: III.XXII.4.2.1 -->

*there exists a bijection `d : R ⥲ R′`[^N.D.E-XXII-19] and for each `α ∈ R` an integer `q(α) > 0` such that
`x ↦ x^{q(α)}` is an endomorphism of `Ga,S` and that*

```text
h(d(α)) = q(α) α,    ᵗh(α*) = q(α) d(α)*.
```

**Remark 4.2.2.** *It is immediate that `h`, `d`, `q(α)` for `α ∈ R`, are uniquely determined by `f`. One writes
`h = R(f)`. The `q(α)` are the* root exponents *of `f` (or of `h`).*

<!-- label: III.XXII.4.2.2 -->

Let `p` be the prime number (if it exists) that is zero on `S`; set `p = 1` if there is no prime number zero on `S`.
Then `R(f)` is a `p`-morphism of reduced root data in the sense of Exp. XXI 6.8. One has thus defined a functor `R` from
the category of `S`-split groups to that of reduced root data (equipped with `p`-morphisms).

**Proposition 4.2.3.** *Under the conditions of 4.2.1, one has the following properties:*

<!-- label: III.XXII.4.2.3 -->

*(i) For every `α ∈ R`, there exists a unique isomorphism of `O_S`-modules*

```text
fα : (gα)^{⊗q(α)} ⥲ g′_{d(α)}
```

*such that*

```text
f(expα(X)) = exp_{d(α)}(fα(X^{q(α)}))
```

*for every `X ∈ W(gα)(S′)`, `S′ → S`.*

*(ii) For every `α ∈ R`, one has `q(−α) = q(α)` and `fα` and `f_{-α}` are contragredient to one another.*

*(iii) For every `α ∈ R`, every `Z ∈ W(gα)*(S′)`, `S′ → S`, one has*

```text
f(wα(Z)) = w_{d(α)}(Z^{q(α)}).
```

By hypothesis the diagram

```text
Gm,S  --α*-->   T   --α-->   Gm,S
 |              |              |
 q(α)          f_T            q(α)
 ↓              ↓              ↓
Gm,S  --d(α)*-> T′ --d(α)--> Gm,S
```

is commutative. It follows that `f` maps `Ker(α)` into `Ker(d(α))`, hence `Tα` into `T′_{d(α)}`, hence `Zα` into
`Z′_{d(α)}`. There is then nothing more to do than apply Exp. XX 3.10 and 3.11 to the groups `Zα` and `Z′_{d(α)}`.

**Proposition 4.2.4.** *The morphism `f` induces a morphism `f_N` of `Norm(T)` into `Norm_{G′}(T′)`, hence a morphism
`f_W` of `W_G(T)` into `W_{G′}(T′)`; the latter is an isomorphism. More precisely, if we denote by
`d : W(R(G)) = W → W′ = W(R(G′))` the isomorphism extending `sα ↦ s_{d(α)}` (Exp. XXI 6.8.4), we have a commutative
diagram of isomorphisms:*

<!-- label: III.XXII.4.2.4 -->

```text
W_G(T)  --f_W-->  W_{G′}(T′)
   ↑                  ↑
   ≀                  ≀
   |                  |
  W_S  --d_S-->     W′_S.
```

This follows immediately from 3.4, Exp. XXI 6.8.4, and (iii) above.

**Remark 4.2.5.** *With the notations of 4.2.3, the restriction of `f` to `Ω_{R+}` (for a system of positive roots `R+`)
is written explicitly: it maps `Ω_{R+}` to `Ω′_{d(R+)}` (`d(R+)` is a system of positive roots of `R′` by Exp. XXI
6.8.7) and is given by the set-theoretic formula:*

<!-- label: III.XXII.4.2.5 -->

```text
f(∏_{α ∈ R−} expα(Xα) · t · ∏_{α ∈ R+} expα(Xα))
  = ∏_{α ∈ R−} exp_{d(α)}(fα(Xα^{q(α)})) · f_T(t) · ∏_{α ∈ R+} exp_{d(α)}(fα(Xα^{q(α)})).
```

**Proposition 4.2.6.** *(i) `f` is surjective (= faithfully flat in the present case, cf. VI_B 3.11) if and only if
`f_T` is.*

<!-- label: III.XXII.4.2.6 -->

*(ii) One has `Ker(f) ⊂ Ω_{R+}`.*

Let us prove (i): if `f` is surjective, then `f_T(T) = f(T)` is a maximal torus of `G′` (indeed `f(T)` is a subtorus of
a maximal torus `T′` (Exp. IX 6.8); to verify that `f(T) = T′`, one reduces to the case of an algebraically closed
field, where this is *Bible*, § 7.3, th. 3 (a)).

If `f_T` is surjective, the preceding formula shows that `f` induces a surjection from `Ω = Ω_{R+}` onto
`Ω′ = Ω′_{d(R+)}`.[^N.D.E-XXII-20] Since the fibers of `G′` are connected, it follows (cf. Exp. VI_A, 0.5) that `f` is
surjective.

Let us prove (ii) and for this admit a result to be proved below (5.7.4): choose for each `w ∈ W` an
`n_w ∈ Norm_G(T)(S)` representing it; then the open sets `n_w Ω` (`w ∈ W`) form a cover of `G`. It is then enough to
prove that `Ker(f) ∩ n_w Ω ≠ ∅` implies `w = 1`. If `x ∈ Ω(S′)`, `S′ → S` and `f(n_w x) = 1`, then `f(x) = f(n_w)⁻¹`;
but `f(x) ∈ Ω′(S′)` and `f(n_w)⁻¹ ∈ Norm_{G′}(T′)(S′)`. By 4.2.4, one is reduced to proving:

**Lemma 4.2.7.** *Under the conditions of 4.1.2, one has `Ω ∩ Norm_G(T) = T`.*

<!-- label: III.XXII.4.2.7 -->

Let

```text
x = ∏_{α ∈ R−} pα(xα) · t · ∏_{α ∈ R+} pα(xα) = v t u ∈ Ω(S′).
```

If `x` normalizes `T_{S′}`, one has for every `t′ ∈ T(S′)`,

```text
x t′ x⁻¹ = t′′ ∈ T(S′),
```

that is, `x t′ = t′′ x`, which is written

```text
v (t t′) (t′⁻¹ u t′) = (t′′ v t′′⁻¹) (t′′ t) u,
```

which gives `t′⁻¹ u t′ = u`, hence `u ∈ Centr_G(T)(S′) = T(S′)`, that is `u = 1`. Similarly `v = 1`.

**Corollary 4.2.8.** *One has*

<!-- label: III.XXII.4.2.8 -->

```text
Ker(f) = ∏_{α ∈ R−} Kα · Ker(f_T) · ∏_{α ∈ R+} Kα,
```

*where for each `α ∈ R`, `Kα` denotes the finite `S`-group*

```text
Kα = Ker(Uα → Uα^{⊗q(α)}) ≃ α_{q(α), S}.
```

To apply this corollary, let us set:

**Definition 4.2.9.** *Let `S` be a scheme, `G` and `G′` two `S`-reductive groups. A morphism of `S`-groups `f : G → G′`
that is faithfully flat and finite (i.e. surjective with finite kernel over `S`) is called an* isogeny. *If moreover
`Ker(f)` is a central subgroup of `G`, one says that `f` is a* central isogeny.

<!-- label: III.XXII.4.2.9 -->

**Proposition 4.2.10.** *Let `f : G → G′` be a morphism of split groups. For `f` to be an isogeny (resp. a central
isogeny) it is necessary and sufficient that `f_T` be an isogeny, i.e. that `R(f)` be injective with finite cokernel
(resp. and that for every `α ∈ R`, one has `q(α) = 1`).*

<!-- label: III.XXII.4.2.10 -->

Indeed, by 4.2.8, `Ker(f)` is finite over `S` if and only if `Ker(f_T)` is finite over `S`, and `Ker(f) ⊂ T` if and only
if each `q(α) = 1` (`Ker(f)` is then central since of multiplicative type and invariant, cf. Exp. IX 5.5).

**Remark 4.2.11.** *(a) One thus sees that `f : G → G′` is a central isogeny if and only if `R(f) : R(G′) → R(G)` is an
isogeny in the sense of Exp. XXI 6.2; moreover one has in this case (with the notations of loc. cit.):*

<!-- label: III.XXII.4.2.11 -->

```text
Ker(f) = D_S(K(R(f))),    K(R(f)) = Coker(R(f)).
```

*(b) If `G` and `G′` are semisimple, every morphism of split groups `f : G → G′` is an isogeny.*[^N.D.E-XXII-21]

*(c) If `f : G → G′` is faithfully flat and finite and if `G` is reductive (resp. semisimple), then `G′` is also. It is
indeed of finite presentation over `S` (Exp. V 9.1), affine over `S` (EGA II 6.7.1), smooth over `S` (Exp. VI 9.2), with
connected reductive (resp. semisimple) geometric fibers by Exp. XIX 1.7.*

Definition 4.2.1 may seem arbitrary. It is justified by the following proposition (which we state, for simplicity, for
semisimple groups).

We say that a morphism `f : G → G′` of `S`-reductive groups is *splittable* if there exist splittings of `G` and `G′`
with which `f` is compatible. One then has:

**Proposition 4.2.12.** *Let `S` be a scheme, `G` and `G′` two semisimple `S`-groups, `f : G → G′` a morphism of groups.
Let `s ∈ S`. The following conditions are equivalent:*

<!-- label: III.XXII.4.2.12 -->

*(i) `Ker f_s` is finite (⇔ `e` is isolated in `Ker f(s)`) and `f_s` is surjective, i.e. `f_s` is an isogeny.*

*(ii) `f_s` is splittable.*

*(iii) There exists an étale morphism `S′ → S` covering `s` such that `f_{S′} : G_{S′} → G′_{S′}` is splittable.*

One has obviously (iii) ⇔ (ii); (ii) ⇒ (i) follows from 4.2.11 (b) (this is where the hypothesis that `G` and `G′` are
semisimple intervenes — the other implications are valid for reductive groups).

Let us now prove (i) ⇒ (iii). One may suppose `G` and `G′` split in such a way that `f` induces a morphism
`f_T : T → T′` (2.3 and Exp. XIX 2.8); shrinking `S`, one may suppose that `f_T = D_S(h)`, where `h` is a morphism of
groups `M′ → M`. Let `α ∈ R`, and consider the composite morphism

```text
p : W(gα) --expα--> G --f--> G′.
```

Since `Ker(p_s)` is finite, `p_s ≠ e`. On the other hand `f_{T_s}` is surjective; one may therefore apply 4.1.9, and
there exist an open subset `V_α` of `S` containing `s`, a root `α′ ∈ R′`, an integer `q(α)` such that `x ↦ x^{q(α)}` is
an endomorphism of `Ga,V_α`, and an isomorphism of `O_{V_α}`-modules

```text
fα : (gα)^{⊗q(α)}|V_α ⥲ g′_{α′}|V_α
```

such that `f(expα(Xα)) = exp_{d(α)}(fα(Xα^{q(α)}))` and `α′ ∘ f_T = h(α′) = q(α) α`. One may replace `S` by the
intersection of the `V_α`, for `α ∈ R`. Set `α′ = d(α)`. It is clear that `d : R → R′` is a bijection, because the
kernel of `h` is finite (`f_{T_s}` being surjective). It only remains to prove that `f_T ∘ α* = q(α) α′*`, which is done
by a trivial modification of the argument used in Exp. XX 3.11.

In any case, as one has seen in the course of the demonstration, one has (i) ⇒ (iii). Therefore:

**Corollary 4.2.13.** *Let `S` be a scheme, `f : G → G′` an isogeny of reductive groups. Then `f` is locally splittable
for the étale topology.*

<!-- label: III.XXII.4.2.13 -->

### 4.3. Central quotients of reductive groups

<!-- label: III.XXII.4.3 -->

Let us first consider a particular case.

**Proposition 4.3.1.** *Let `S` be a scheme, `(G, T, M, R)` an `S`-split group, `N` a subgroup of `M` containing `R`,
`Q = D_S(M/N) ⊂ Centr(G)`. Then:*

<!-- label: III.XXII.4.3.1 -->

*(i) `G′ = G/Q` is an `S`-reductive group, and `T′ = T/Q` is a maximal torus of it;*

*(ii) if one identifies `T′` with `D_S(N)`, then `R ⊂ N` is a system of roots of `G′` relative to `T′`, `(G′, T′, N, R)`
is a splitting of `G′`, and `R(G′)` is canonically identified with the induced root datum (Exp. XXI 6.5) `R(G)^N`;*

*(iii) the canonical morphism `G → G′` is compatible with the splittings, with root exponents 1, and gives by
functoriality the canonical morphism (loc. cit.) `R(G)^N → R(G)`.*

One knows that `G′ = G/Q` is representable by an affine group scheme over `S` (Exp. VIII 5.7), smooth over `S` (Exp.
VI_B 9.2), with connected reductive geometric fibers (as quotients of reductive groups, cf. Exp. XIX 1.7); `G′` is
therefore an `S`-reductive group.

It is clear that `T′ = T/Q ≃ D_S(N)` is a maximal torus of it. Note next that, choosing a system of positive roots `R+`
of `R`, the open set `Ω_{R+}` of 4.2 is stable under `Q` and that one has a canonical isomorphism

```text
Ω_{R+}/Q ≃ ∏_{α ∈ R−} Uα ×_S (T/Q) ×_S ∏_{α ∈ R+} Uα,
```

and that `Ω_{R+}/Q` is an open subset of `G′` containing the unit section (cf. Exp. IV, 4.7.2 and 6.4.1).

It follows that, if one denotes by `g′` the Lie algebra of `G′` and by `ᾱ` the character of `T/Q` induced by `α` (or,
which amounts to the same, defined by `α ∈ N` in the identification `T/Q = D_S(N)`), the canonical morphism `g → g′`
induces for each `α ∈ R` an isomorphism

```text
gα ⥲ g′_{ᾱ}.
```

One has thus proved that `R` is a system of roots of `G′` relative to `T′`, and one finishes the proof without
difficulty.

**Corollary 4.3.2.** *Let `S` be a scheme, `G` an `S`-reductive group, `Q` a normal subgroup of multiplicative type of
`G`. Then `Q` is central in `G`, the quotient `G/Q` is representable by an `S`-reductive group, and the canonical
morphism `G → G/Q` is locally splittable for the étale topology (with root exponents equal to 1).*

<!-- label: III.XXII.4.3.2 -->

The first assertion follows from Exp. IX 5.5; the others are local for the étale topology and one is reduced to 4.3.1.

**Definition 4.3.3.** *Let `G` be an `S`-reductive group. We say that `G` is* adjoint *(resp.* simply connected\*) if
for every `s ∈ S`, the type of `G` at `s` is given by an adjoint (resp. simply connected) root datum, i.e. (Exp. XXI
6.2.6) such that `M` be generated by `R` (resp. `M*` generated by `R*`).\*

<!-- label: III.XXII.4.3.3 -->

**Proposition 4.3.4.** *(i) An adjoint (resp. simply connected) reductive group is semisimple.*

<!-- label: III.XXII.4.3.4 -->

*(ii) If `T` is a maximal torus of the adjoint (resp. simply connected) reductive group `G` and `α` is a root of `G`
relative to `T`, then the infinitesimal root `α` is non-zero on every fiber (resp. `α*` is a monomorphism and the
infinitesimal coroot `Hα` is non-zero on every fiber).*

Indeed, (i) is trivial; (ii) is checked on geometric fibers and follows immediately from Exp. XXI 6.2.8.

**Proposition 4.3.5.** *(i) For the reductive group `G` to be adjoint, it is necessary and sufficient that
`Centr(G) = {e}_S`.*

<!-- label: III.XXII.4.3.5 -->

*(ii) For every reductive group `G`, the quotient group `G/Centr(G)` is an adjoint reductive group.*

Indeed, one may suppose `G` split; then (i) is trivial (since `Centr(G) = D_S(M/Γ₀(R))`), and (ii) follows from 4.3.1.

**Definition 4.3.6.** *Let `G` be an `S`-reductive group. We call* adjoint group of `G` *and denote by `ad(G)` the group
`G/Centr(G)`. We call* radical of `G` *and denote by `rad(G)` the maximal torus (unique by Exp. XII 1.12) of `Centr(G)`.
We call* semisimple group associated with `G` *the quotient `G/rad(G)`.*

<!-- label: III.XXII.4.3.6 -->

The preceding definitions are compatible with base change. If `s ∈ S`, `rad(G)_s` is indeed the radical of `G_s` in the
usual sense (Exp. XIX 1.6).

#### 4.3.7.

<!-- label: III.XXII.4.3.7 -->

If `(G, T, M, R)` is a split group, then `rad(G) = D_S(M/N)`, where `N = M ∩ V(R)`, so the semisimple group associated
with `G` (and similarly the adjoint group of `G`) is equipped with a canonical splitting (4.3.1) and one has a diagram
of split groups

```text
G → ss(G) → ad(G)
```

corresponding to the canonical diagram of root data (Exp. XXI 6.5.5)

```text
ad(R(G)) → ss(R(G)) → R(G).
```

**Remark 4.3.8.** *Let `(G, T, M, R)` be an `S`-split adjoint (resp. simply connected) group, `Δ` a system of simple
roots of `R`. Then the family `{α}_{α ∈ Δ}`, resp. `{α*}_{α ∈ Δ}`, induces an isomorphism*

<!-- label: III.XXII.4.3.8 -->

```text
T ⥲ (Gm,S)^Δ,    resp.    (Gm,S)^Δ ⥲ T.
```

Indeed, `M = Γ₀(R)` (resp. …) and `Δ` is a basis of the free abelian group `Γ₀(R)` (Exp. XXI 3.1.8).

**Remark 4.3.9.** *The radical of a reductive group is a characteristic subgroup (i.e. stable under `Aut_{S-gr.}(G)`),
by its very definition.*

<!-- label: III.XXII.4.3.9 -->

## 5. Subgroups of type (R)

<!-- label: III.XXII.5 -->

<!-- original page 128 -->

We are especially interested in reductive groups, but some of the results we shall establish are valid more generally
for a wider class of groups: groups of type (RR).

### 5.1. Groups of type (RR)

<!-- label: III.XXII.5.1 -->

**Definition 5.1.1.** *Let `S` be a scheme, `G` an `S`-group scheme. We say that `G` is* of type (RR) *if it satisfies
the following conditions:*

<!-- label: III.XXII.5.1.1 -->

*(i) `G` is smooth and of finite presentation over `S` and has connected fibers.*

*(ii) `G` locally possesses maximal tori for the (fpqc) topology.*

*(iii) For every `s ∈ S`, every maximal torus `T` of `G_s`, and every root of `G_s` relative to `T_s` (Exp. XIX 1.10),
`Lie(G_s)^α` is of rank 1 (as a vector space over `κ(s)`).*

*(iv) For every `s ∈ S` and every maximal torus `T` of `G_s`, let `R` denote the set of roots of `G_s` relative to `T`
and `Γ₀(R)` the subgroup of `Hom_{s-gr.}(T, Gm,s)` generated by `R`; then the content[^N.D.E-XXII-22] of every root
`α ∈ R` in the free abelian group `Γ₀(R)` (which is therefore a positive integer) is invertible on `S`.*

**Recall 5.1.1.1.**[^N.D.E-XXII-23] *Let us recall that if `G` is a smooth connected algebraic group over an
algebraically closed field `k`, a* Cartan subgroup *of `G` is the centralizer of a maximal torus of `G` (XII 1.0), and
such a subgroup is smooth and connected: for this, as well as for other characterizations of Cartan subgroups, see
Bible, § 7.1, Th. 1 in the affine case and Exp. XII Th. 6.6 in the general case. If `S` is an arbitrary scheme and `G`
an `S`-smooth group of finite type, a* Cartan subgroup *of `G` is an `S`-smooth subgroup `C` of `G` such that, for every
`s ∈ S`, `C_s` is a Cartan subgroup of `G_s` (XII Def. 3.1).*

<!-- label: III.XXII.5.1.1.1 -->

**Remark 5.1.2.** *(a) By virtue of Exp. XII 7.1 (where the hypothesis that `G` is separated holds here since `G` has
connected fibers, cf. Exp. VI_B 5.5), (i) and (ii) entail that `G` locally possesses, for the étale topology, maximal
tori (resp. Cartan subgroups), conjugate locally for the étale topology.*

<!-- label: III.XXII.5.1.2 -->

*(b) The Cartan subgroups of `G` have connected fibers (Exp. XII 6.6).*

*(c) If `G` is affine over `S`, (i) and (ii) are respectively equivalent to*

*(i′) `G` is smooth over `S` with connected fibers.*

*(ii′) The reductive rank of the fibers of `G` is locally constant (Exp. XII 1.7).*

*(d) By Exp. XII 8.8 (c) and (d), `G` has a reductive center `Z` and, for every `s ∈ S`, with the notations of (iv), one
has[^N.D.E-XXII-24] `Z_s = ⋂_{α ∈ R} Ker(α)`, whence*

```text
Hom_{s-gr.}((T/Z)_s, Gm,s) ≃ Γ₀(R).
```

*(e) Condition (iv) holds in particular in the following two cases:*

*(1) `S` is of characteristic 0;*

*(2) every root is an indivisible element of the group generated by the roots.*

*(f) Being of type (RR) is stable under base change and is local for the (fpqc) topology.*

From remarks (c) and (e), one immediately deduces:

**Proposition 5.1.3.** *A reductive group is of type (RR).*

<!-- label: III.XXII.5.1.3 -->

**Proposition 5.1.4.** *Let `S` be a scheme, `G` an `S`-group of type (RR), `Q` a central subgroup of `G` of finite
presentation over `S` such that the quotient `G/Q` is representable (for instance `G` affine over `S` and `Q` of
multiplicative type (IX 2.3) or else `S` artinian (VI_A 3.3.2)); then `G/Q` is an `S`-group of type (RR).*

<!-- label: III.XXII.5.1.4 -->

Indeed, `G/Q` is smooth over `S` (Exp. VI_B 9.2), of finite presentation over `S` (Exp. V 9.1) and with connected
fibers, so condition (i) holds. On the other hand, condition (ii) follows from Exp. XII 7.6; it remains to verify
conditions (iii) and (iv).

Let `G′ = G/Q`, `u : G → G′` the canonical morphism, `T′ = u(T)` the maximal torus of `G′` image of `T` (cf. Exp. XII
7.1 (e)); for each `α ∈ R`, denote again by `α` the character of `T′` defined by `α` (one has `Q ∩ T ⊂ ⋂_{α ∈ R} Ker(α)`
according to 5.1.2 (d)). Let us first prove:

**Lemma 5.1.5.** *Under the conditions of 5.1.4, let `T = D_S(M)` be a trivialized maximal torus of `G`, and suppose
that the decomposition of `g = Lie(G)` under `Ad(T)` is of the form*

<!-- label: III.XXII.5.1.5 -->

```text
g = g⁰ ⨿ ⨿_{α ∈ R} gα,    R ⊂ M − {0},
```

*where for every `s ∈ S`, `gα(s) ≠ 0` for `α ∈ R` (so `gα` is an invertible `O_S`-module for every `α ∈ R` and `R` is
the set of roots of `G_s` relative to `T_s` for every `s ∈ S`).*

*Then the Lie algebra `g′` of `G′` decomposes under `Ad(T′)` as follows:*

```text
g′ = g′⁰ ⨿ ⨿_{α ∈ R} g′^α,
```

*and `Lie(u)` induces an isomorphism of `gα` onto `g′^α`.*

Indeed, let `p = Lie(u) : g → g′`. One immediately has `p(gα) ⊂ g′^α` for every `α ∈ R`, and `p(g⁰) ⊂ g′⁰`. Since

```text
Ker(p) = Lie(Q) ⊂ Lie(Centr_G(T)) = g⁰,
```

`p` induces a monomorphism from `gα` into `g′^α`, for every `α ∈ R`.

To prove the lemma, it suffices to do so when `S` is the spectrum of an algebraically closed field, and by virtue of the
preceding remarks, it then suffices to prove that `rg(g′) = rg(g′⁰) + Card(R)`. Now set `C = Centr_G(T)`,
`C′ = Centr_{G′}(T′)`; by Exp. XII 7.1 (e), `u` induces a faithfully flat morphism `C → C′` of kernel `Q`. One thus has

```text
dim C′ + dim Q = dim C.
```

But `G`, `G′`, `C` and `C′` are smooth, so

```text
dim G = rg(g) = rg(g⁰) + Card(R) = dim C + Card(R)
              = dim Q + dim C′ + Card(R) = dim Q + rg(g′⁰) + Card(R)
rg(g′) = dim G′ = dim G − dim Q
```

which entails

```text
rg(g′) = rg(g′⁰) + Card(R),
```

that is, the desired relation.

Let us return to the proof of 5.1.4; one may suppose that `S` is the spectrum of an algebraically closed field. Let `T`
be a maximal torus of `G`; applying 5.1.5, one immediately has (iii) and (iv) for `G/Q`.

To use the preceding proposition, let us introduce a definition:

**Definition 5.1.6.** *We say that the `S`-group scheme `G` is* of type (RA) *if it is of type (RR) and if it further
satisfies the following condition (iv′) (stronger than (iv)):*

<!-- label: III.XXII.5.1.6 -->

*(iv′) For every `s ∈ S` and every maximal torus `T` of `G_s`, every root of `G_s` relative to `T` has a content in
`Hom_{s-gr.}(T, Gm,s)` that is invertible on `S`.*

**Remarks 5.1.7.** *(a) An `S`-reductive adjoint group is of type (RA).*

<!-- label: III.XXII.5.1.7 -->

*(b) If `S` is of characteristic 0, every group of type (RR) is of type (RA).*

*(c) Being of type (RA) is stable under base change and is local for the (fpqc) topology.*

Remark (a) above generalizes to:

**Proposition 5.1.8.** *Let `S` be a scheme, `G` an `S`-group of type (RR), `Z` its reductive center, suppose the
quotient `G/Z` representable (for instance `G` affine over `S`, or `S` artinian); then `G/Z` is of type (RA).*

<!-- label: III.XXII.5.1.8 -->

Indeed, this follows immediately from 5.1.4, 5.1.5, and 5.1.2 (d).

**Remark 5.1.9.** *If `G` is of type (RR) and if `T` is a maximal torus of `G`, one may apply Exp. XIX 6.3. In
particular `W_G(T)` is étale, quasi-finite and separated over `S`.*

<!-- label: III.XXII.5.1.9 -->

### 5.2. Subgroups of type (R)

<!-- label: III.XXII.5.2 -->

**Definition 5.2.1.** *Let `S` be a scheme, `G` a smooth `S`-group scheme of finite presentation with connected
fibers,[^N.D.E-XXII-25] `H` a group subscheme of `G`. We say that `H` is* of type (R) *if:*

<!-- label: III.XXII.5.2.1 -->

*(i) `H` is smooth, of finite presentation over `S` and with connected fibers.[^N.D.E-XXII-25]*

*(ii) For every `s ∈ S`, `H_s` contains a Cartan subgroup of `G_s`.*

*This notion is stable under base change and local for the (fpqc) topology.*

**Recall 5.2.2.** *(cf. Exp. XII 7.9) Under the preceding conditions:*

<!-- label: III.XXII.5.2.2 -->

*(a) `H = Norm_G(H)⁰`.*

*(b) If `G` locally possesses, for the étale topology, Cartan subgroups (resp. maximal tori), so does `H`, and the
Cartan subgroups (resp. maximal tori) of `H` are Cartan subgroups (resp. maximal tori) of `G`.*

**Examples 5.2.3.** *(a) Borel subgroups: a* Borel subgroup *of `G` is a subgroup `H` of type (R) whose geometric fibers
are Borel subgroups of those of `G`.*[^N.D.E-XXII-26]

<!-- label: III.XXII.5.2.3 -->

*(b) Parabolic subgroups: a* parabolic subgroup *of `G` is a subgroup of type (R) whose geometric fibers contain Borel
subgroups.*

Other examples are given by the following propositions.

**Proposition 5.2.4.** *Let `G` be as in 5.2.1, `K ⊂ H` two group subschemes of `G`, `H` assumed to be of type (R). Then
`K` is a subgroup of type (R) of `H` if and only if it is a subgroup of type (R) of `G`.*

<!-- label: III.XXII.5.2.4 -->

[^N.D.E-XXII-27] Indeed, let `s ∈ S`. Since `H` is of type (R), every maximal torus of `H_s` is a maximal torus of
`G_s`, and so likewise for Cartan subgroups.

**Proposition 5.2.5.** *Let `G` be as in 5.2.1, `T` a maximal torus of `G`, `Q` a subtorus of `T`, `Z = Centr_G(Q)`. If
`H` is a subgroup of type (R) of `G` containing `T`, then `H ∩ Z` is a subgroup of type (R) of `Z`.*

<!-- label: III.XXII.5.2.5 -->

Let us first recall that `Z` is a closed group subscheme of `G`, of finite presentation (Exp. XI 6.11), with connected
fibers (Exp. XII 6.6), smooth over `S` (Exp. XI 2.4), so it satisfies the conditions imposed in Definition 5.2.1.
Similarly, `H ∩ Z` is of finite presentation, smooth and has connected fibers (since `H ∩ Z = Centr_H(Q)`); moreover
`H ∩ Z ⊃ Centr_G(T)`.

**Proposition 5.2.6.** *Let `S` be a scheme, `G` an `S`-group of type (RR) (resp. (RA)), `H` a subgroup of type (R) of
`G`. Then `H` is an `S`-group of type (RR) (resp. (RA)).*

<!-- label: III.XXII.5.2.6 -->

Indeed, (i) is clear, (ii) follows from 5.2.2 (b), (iii) and (iv) (resp. (iv′)) are to be verified when `S` is the
spectrum of an algebraically closed field. Then `H` contains a maximal torus `T` of `G` (and hence also
`C = Centr_G(T)`),[^N.D.E-XXII-28] and the assertions to be proved follow immediately from:

**Lemma 5.2.7.** *Let `S` be a scheme, `G` an `S`-group of type (RR), `T` a maximal torus of `G` equipped with a
trivialization `T ≃ D_S(M)`, and suppose that*

<!-- label: III.XXII.5.2.7 -->

```text
g = g⁰ ⨿ ⨿_{α ∈ R} gα
```

*(the `gα` being then invertible `O_S`-modules).*

*Let `H` be a subgroup of type (R) containing `C = Centr_G(T)` (i.e. containing `T`). Then `h = Lie(H/S)` is locally on
`S` of the form*

```text
g⁰ + ⨿_{α ∈ R′} gα = g_{R′};
```

*more precisely, let, for each `s ∈ S`, `R′(s) = {α ∈ R | gα(s) ⊂ h(s)}`. Then `R′(s)` is a locally constant function of
`s`; if `U` is an open subset of `S` on which `R′(s) = R′`, one has*

```text
h_U = g⁰_U ⨿ ⨿_{α ∈ R′} gα_U.
```

Indeed, `h` is a submodule of `g`, locally a direct factor, containing `g⁰` and stable under `T`.

### 5.3. Strict transporter of two subgroups of type (R). Applications

<!-- label: III.XXII.5.3 -->

**Recall 5.3.0.**[^N.D.E-XXII-29] *Let `S` be a scheme, `G` an `S`-smooth group, `g = Lie(G/S)` and `h` a
sub-`O_S`-module of `g` that is locally a direct factor. The `O_S`-algebra `A = Sym(ω¹_{G/S})` is locally free, so the
`S`-scheme `Lie(G/S) = W(g) = Spec(A)` is essentially free in the sense of Exp. VIII, 6.1. Since `W(h)` is a closed
subscheme of `Lie(G/S)`, of finite presentation over `Lie(G/S)`, then `N = Norm_G(h)` is representable by a closed group
subscheme of `G`, of finite presentation over `G`, by Exp. VIII, 6.5 (a). (See also the additions 6.2.3 and 6.2.4 (a) in
Exp. VI_B.) On the other hand, by Exp. II 5.3.1, one has `Lie(N/S) = Norm_{Lie(G/S)}(h)`.*

*Finally, by Exp. VI_B 3.10, if `N` is smooth over `S` at the points of the unit section, then the group subfunctor `N⁰`
(defined in VI_B 3.1) is represented by an open group subscheme of `N`, smooth over `S`.*

**Proposition 5.3.1.** *Let `S` be a scheme, `G` an `S`-group of type (RA) (5.1.6), `H` a subgroup of type (R) of `G`,
`g ⊃ h` their Lie algebras.*

<!-- label: III.XXII.5.3.1 -->

*Then `Norm_G(h)` (which is representable by a closed subscheme of `G` of finite presentation over `S` according to
5.3.0) is smooth over `S` at every point of the unit section, and one has*

```text
Norm_G(h)⁰ = H.
```

[^N.D.E-XXII-30] Proof. Set `N = Norm_G(h)` and `n = Lie(N/S)`. One has `H ⊂ N` and, by Exp. II 5.3.1, one has for every
`s ∈ S`

```text
h(s) ⊂ n(s) = Norm_{g(s)}(h(s)).
```

Now, by 5.3.2 below, one has `h(s) = Norm_{g(s)}(h(s))`, and since `H` is smooth over `S`, one has
`dim_{κ(s)} h(s) = dim H_s` (cf. [DG70], § II.5, Th. 2.1). One thus obtains

```text
dim_{κ(s)} n(s) = dim_{κ(s)} h(s) = dim H_s ⩽ dim N_s
```

whence `N⁰_s = H⁰_s = H_s` (`H` having connected fibers). It follows that the group subfunctor `N⁰` (defined in VI_B,
3.1) is represented by the smooth `S`-group `H`. This proves 5.3.1, modulo the following lemma:

**Lemma 5.3.2.** *Under the conditions of 5.2.7, if `G` is of type (RA), one has, for every `s ∈ S`,*

<!-- label: III.XXII.5.3.2 -->

```text
Norm_{g(s)}(h(s)) = h(s).
```

Indeed, one is reduced to the case where `S` is the spectrum of a field, so where `h = g_{R′}` for some `R′ ⊂ R`. But
one already has

```text
Transp_g(t, h) = h.
```

Indeed, if `H ∈ t` and `X ∈ gα`, one has `[H, X] = α(H) X`, where `α : t → O_S` is the derived morphism of `α`. Now
condition (iv′) says precisely that `α ≠ 0` for every `α ∈ R`.

**Corollary 5.3.3.** *Let `S` be a scheme, `G` an `S`-group of type (RA), `H` and `H′` two subgroups of type (R) of `G`,
`h` and `h′` their Lie algebras. Then*

<!-- label: III.XXII.5.3.3 -->

```text
H = H′ ⇔ h = h′.
```

**Corollary 5.3.4.** *Under the conditions of 5.2.7, with `G` of type (RA), the maps*

<!-- label: III.XXII.5.3.4 -->

```text
H ↦ Lie(H/S),    h ↦ Norm_G(h)⁰
```

*realize a bijective correspondence between the set of subgroups of type (R) of `G` containing `T` and the set of Lie
subalgebras of `g` containing `g⁰`, stable under `T`, and whose normalizer in `G` is smooth over `S` at every point of
the unit section.*

[^N.D.E-XXII-31] Indeed, let `h` be a Lie subalgebra of `g` having the above properties. By 5.3.0, `H = Norm_G(h)⁰` is a
smooth `S`-group scheme. Moreover, since `C = Centr_G(T)` stabilizes each `gα` and has connected fibers (XII 6.6), one
has `C ⊂ H`. Therefore `H` is a subgroup of `G` of type (R). By Exp. II 5.3.1, one has `Lie(H) = Norm_g(h)`. Finally, by
the proof of 5.3.2, one has `Norm_g(h) = h`.

**Corollary 5.3.5.** *Let `S` be a scheme, `G` an `S`-group of type (RR) (5.1.1), `T` a maximal torus of `G`, `H` and
`H′` two subgroups of type (R) of `G`, both containing `T`. Then*

<!-- label: III.XXII.5.3.5 -->

```text
H = H′ ⇔ h = h′.
```

By virtue of the finite presentation hypotheses, one reduces as usual (cf. EGA IV₃, § 8 and Exp. VI_B § 10) to the case
where `S` is noetherian; it suffices then to verify that `h = h′` implies `H_{S′} = H′_{S′}` for every `S′` spectrum of
an artinian quotient of a local ring of `S`;[^N.D.E-XXII-32] one is thus reduced to the case where `S` is artinian, and
one may apply 5.1.8. Let `u : G → G′ = G/Z` be the canonical morphism and `T′ = T/Z` the maximal torus of `G′`
corresponding to `T`. By Exp. XII 7.12, there exist subgroups of type (R) `H₁` and `H′₁` of `G′`, containing `T′`, such
that `H = u⁻¹(H₁)` and `H′ = u⁻¹(H′₁)`. It suffices to prove that `H₁ = H′₁`. But by 5.2.7 and 5.1.5, one has

```text
Lie(H₁) = Lie(H′₁),
```

and one reduces to 5.3.3.

**Remark 5.3.6.** *The fact that `H` and `H′` contain the same maximal torus is essential for the validity of 5.3.5 when
`G` is not of type (RA). Example: maximal tori of `SL₂,k` for `k` of characteristic 2.*[^N.D.E-XXII-33]

<!-- label: III.XXII.5.3.6 -->

**Corollary 5.3.7.** *Let `S` be a scheme, `G` an `S`-group of type (RR), `T` a maximal torus of `G`, `H` and `H′` two
subgroups of type (R) of `G`, both containing `T`. The set `U` of `s ∈ S` such that `H_s = H′_s` is open and closed in
`S` and `H_U = H′_U`.*

<!-- label: III.XXII.5.3.7 -->

Indeed, this follows immediately from 5.3.5 and 5.2.7.

**Corollary 5.3.8.** *The "functor of subgroups of type (R) containing `T`", where `T` is a given maximal torus in a
group `G` of type (RR), is formally unramified (Exp. XI 1.1).*

<!-- label: III.XXII.5.3.8 -->

**Theorem 5.3.9.** *Let `G` be an `S`-group of type (RR) (5.1.1), `H` and `H′` two subgroups of type (R) (5.2.1). Let
`Transt_G(H, H′)` be the strict transporter of `H` into `H′` defined by*

<!-- label: III.XXII.5.3.9 -->

```text
Transt_G(H, H′)(S′) = {g ∈ G(S′) | int(g) H_{S′} = H′_{S′}}.
```

*Then `Transt_G(H, H′)` is representable by a closed subscheme of `G`, which is smooth and of finite presentation over
`S`.*

The fact that `Transt_G(H, H′)` is representable by a closed subscheme of `G`, of finite presentation over `S`, follows
from Exp. XI 6.11 (a). To prove that it is smooth over `S`, we must show that if `S` is affine and `S₀` is the closed
subscheme defined by a nilpotent ideal `J`, and if `g₀ ∈ G(S₀)` and `int(g₀) H₀ = H′₀`, there exists `g ∈ G(S)`
projecting to `g₀` and such that `int(g) H = H′`. Since the question of smoothness is local for the étale topology, we
may suppose that `H` contains a maximal torus `T` of `G`.

Then `T₀` is a maximal torus of `H₀`, hence `int(g₀) T₀` is a maximal torus of `H′₀`. By Exp. IX 3.6 bis, there exists a
torus `T′` of `H′` such that `T′₀ = int(g₀) T₀`; by Exp. IX 3.3 bis, there thus exists `g ∈ G(S)` projecting to `g₀` and
such that `int(g) T = T′`. Replacing `H` by `int(g) H` if necessary, we may therefore suppose that `H` and `H′` contain
the same maximal torus `T` and that `H₀ = H′₀`. But then `H = H′` by 5.3.7. QED.

**Corollary 5.3.10.** *Let `G` be an `S`-group of type (RR), `H` a subgroup of type (R) of `G`. Then `Norm_G(H)` is
representable by a closed group subscheme of `G`, of finite presentation and smooth over `S`.*

<!-- label: III.XXII.5.3.10 -->

Using now the reasoning that, in Exp. XI, served to deduce 5.4 bis from 5.2 bis, one obtains:

**Corollary 5.3.11.** *Under the hypotheses of 5.3.9, the following conditions are equivalent:*

<!-- label: III.XXII.5.3.11 -->

*(i) `H` and `H′` are locally conjugate in `G` for the étale topology.*

*(i bis) idem for the (fpqc) topology.*

*(ii) For every `s ∈ S`, `H_s` and `H′_s` are conjugate by an element of `G(s)`.*

*(ii bis) The structural morphism `Transt_G(H, H′) → S` is surjective.*

*(iii) `Transt_G(H, H′)` is a principal homogeneous bundle under the action of the smooth `S`-group scheme of finite
presentation `Norm_G(H)`.*

Let us simply remark that the non-trivial assertion (iii) ⇒ (i) is Hensel's lemma.

Using now Bible, § 6.4, th. 4 (= [Ch05], § 6.5 th. 5) and § 9.3, th. 1, one obtains by 5.3.10 and 5.3.11:

**Corollary 5.3.12.** *Let `G` be an `S`-group of type (RR). The Borel subgroups of `G` are closed in `G`, equal to
their normalizer, and conjugate locally for the étale topology.*

<!-- label: III.XXII.5.3.12 -->

**Definition 5.3.13.** *Let `S` be a scheme, `G` a smooth `S`-group scheme of finite presentation with connected
fibers.[^N.D.E-XXII-34] By a* Killing couple *of `G` we mean a couple `T ⊂ B`, where `T` is a maximal torus of `G` and
`B` a Borel subgroup of `G` containing `T`.*

<!-- label: III.XXII.5.3.13 -->

Using now the conjugacy of the maximal tori in `B` (cf. 5.1.2 (a) and 5.2.6, for example), one has:

**Corollary 5.3.14.** *Let `G` be an `S`-group of type (RR). The Killing couples of `G` are conjugate locally for the
étale topology.*

<!-- label: III.XXII.5.3.14 -->

**Corollary 5.3.15.** *Let `G` be an `S`-group of type (RR). Let `T` be a maximal torus of `G`,
`W_G(T) = Norm_G(T)/Centr_G(T)` the corresponding Weyl group (Exp. XIX 6.3). The "functor of Borel subgroups of `G`
containing `T`" is formally principal homogeneous under `W_G(T)`.*

<!-- label: III.XXII.5.3.15 -->

This follows immediately from 5.3.14 and from the fact that if `B` is a Borel subgroup of `G` containing `T`, one has

```text
Norm_G(T) ∩ B = Centr_G(T),
```

cf. Exp. XIV 4.4.

**Proposition 5.3.16.** *Let `G` be an `S`-group of type (RR), `H` a subgroup of type (R), `N = Norm_G(H)` its
normalizer (5.3.10). Let `T` be a maximal torus of `H`, `W_H(T)` and `W_N(T)` the corresponding Weyl groups (étale,
quasi-finite, separated by Exp. XIX 6.3). One has the following exact sequence of sheaves (for the étale topology) (the
morphisms are induced by the morphisms `Norm_H(T) → Norm_N(T) → N/H`):*

<!-- label: III.XXII.5.3.16 -->

```text
1 → W_H(T) → W_N(T) → N/H → 1.
```

The only non-trivial point is that the last arrow is an epimorphism. So let `n ∈ N(S′)`, `S′ → S`. The two maximal tori
`T` and `int(n) T` of `H` are conjugate in `H` locally for the étale topology. There thus exists a covering family
`{S′_i → S′}` and for each `i` an `h_i ∈ H(S′_i)` such that `int(h_i) T = int(n) T`. Hence `n h_i⁻¹ ∈ Norm_N(T)`, which
gives the desired result.

**Remark 5.3.17.** *One can describe `W_N(T)` as follows: suppose we are reduced to the situation of 5.2.7, with
`h = g_{R′}`. Then `W_N(T)` equals `Norm_W(R′)`, the sheaf of sections of `W = W_G(T)` that, acting on `R`, normalize
`R′`. Indeed, by 5.3.5, one has*

<!-- label: III.XXII.5.3.17 -->

```text
Norm_N(T) = Norm_G(H) ∩ Norm_G(T) = Norm_G(h) ∩ Norm_G(T).
```

**Corollary 5.3.18.** *Let `G` be an `S`-group of type (RR), `H` a subgroup of type (R). Suppose that "the Weyl groups
of `G` are finite", i.e. that for every `S′ → S` and every maximal torus `T` of `G_{S′}`, the étale `S′`-scheme
`Norm_{G_{S′}}(T)/Centr_{G_{S′}}(T)` is finite (cf. Exp. XIX 6.3 (iii)). The following conditions are equivalent:*

<!-- label: III.XXII.5.3.18 -->

*(i) `H` is closed in `G`.*

*(ii) `Norm_G(H)/H` is representable by a finite étale `S`-scheme.*

*(iii) "The Weyl groups of `H` are finite".*

Indeed, one may suppose that `H` possesses a maximal torus `T`. By 5.3.10, `N = Norm_G(H)` is closed in `G`, so `W_N(T)`
is closed in `W_G(T)` and hence finite over `S`. One obviously has (i) ⇒ (iii), and (iii) ⇒ (ii) by the exact sequence
of 5.3.16. Finally, (ii) ⇒ (i), because if `N/H` is finite, it is separated, so `H` is closed in `N`, hence in `G`.

**Remark 5.3.19.** *When `G` is reductive, the preceding conditions on `H` seem always satisfied. We prove them below in
most cases.*

<!-- label: III.XXII.5.3.19 -->

### 5.4. Subgroups of type (R) of a split reductive group (generalities)

<!-- label: III.XXII.5.4 -->

#### 5.4.1.

<!-- label: III.XXII.5.4.1 -->

If `H` is a subgroup of type (R) of the reductive group `G`, then `H` contains locally, for the étale topology, a
maximal torus of `G` (5.2.2). By 2.3, one may, locally for the étale topology, suppose `G` split relative to this torus.
Let then `(G, T, M, R)` be an `S`-split group, `H` a subgroup of type (R) of `G` containing `T`. By 5.3.5, such a
subgroup is characterized by its Lie algebra, which (5.2.7) is locally on `S` of the form `g_{R′}`:

```text
g_{R′} = t ⨿ ⨿_{α ∈ R′} gα.
```

**Definition 5.4.2.** *Let `(G, T, M, R)` be an `S`-split group. We shall say that the subset `R′` of `R` is* of type
(R) *if `g_{R′}` is the Lie algebra of a subgroup of type (R) of `G` containing `T`. This subgroup, uniquely determined
by `R′`, is denoted `H_{R′}`.*

<!-- label: III.XXII.5.4.2 -->

**Lemma 5.4.3.** *Under the preceding conditions, one has the following equivalences:*

<!-- label: III.XXII.5.4.3 -->

```text
H ∩ Zα = T  ⇔  α ∉ R′,  −α ∉ R′,
H ⊃ Uα     ⇔  α ∈ R′,
H ∩ Uα = e  ⇔  α ∉ R′,
H ⊃ Zα     ⇔  α ∈ R′,  −α ∈ R′.
```

Indeed, `H ∩ Zα` is a subgroup of type (R) of `Zα`, by 5.2.5; but a subgroup of type (R) of `Zα` containing `T` is
locally equal to one of the following subgroups: `T`, `T · Uα`, `T · U_{-α}`, `Zα`, by 5.3.5.

**Lemma 5.4.4.** *Under the conditions of 5.4.2, let `R+` be a system of positive roots; choose orderings on `R′ ∩ R+`
and `R′ ∩ −R+`. The morphism*

<!-- label: III.XXII.5.4.4 -->

```text
Ω_{R+, R′} = ∏_{α ∈ R′ ∩ −R+} Uα ×_S T ×_S ∏_{α ∈ R′ ∩ R+} Uα → G
```

*induced by the product in `G` induces an open immersion*

```text
Ω_{R+, R′} → H_{R′}.
```

Indeed, by 5.4.3, this morphism factors through `H_{R′}` and thus induces an immersion `Ω_{R+, R′} → H_{R′}`. One then
argues as in 4.1.1.

**Proposition 5.4.5.** *Let `(G, T, M, R)` be an `S`-split group. Let `R′` and `R′′` be two subsets of `R` of type (R).*

<!-- label: III.XXII.5.4.5 -->

*(i) `H_{R′} ∩ H_{R′′}` is smooth at every point of the unit section, `R′ ∩ R′′` is of type (R), and one has*

```text
(H_{R′} ∩ H_{R′′})⁰ = H_{R′ ∩ R′′}.
```

*(ii) One has the equivalence*

```text
H_{R′} ⊂ H_{R′′}  ⇔  R′ ⊂ R′′.
```

Indeed, (ii) follows immediately from (i). To prove (i), it suffices to show that `H_{R′} ∩ H_{R′′}` is smooth at every
point of the unit section: its neutral component (cf. Exp. VI_B 3.10) will then be a subgroup of type (R) containing
`T`, hence equal to `H_{R′ ∩ R′′}`; but `Ω_{R+, R′} ∩ Ω_{R+, R′′} = Ω_{R+, R′ ∩ R′′}` is an open subset of
`H_{R′} ∩ H_{R′′}` containing the unit section and smooth over `S`.

**Corollary 5.4.6.** *Let `S` be a scheme, `G` an `S`-reductive group, `T` a maximal torus of `G`, `s` a point of `S`.
If `H` and `H′` are two subgroups of type (R) of `G` containing `T` such that `H_s ⊂ H′_s`, there exists an open subset
`U` of `S` containing `s` such that `H_U ⊂ H′_U`.*

<!-- label: III.XXII.5.4.6 -->

Indeed, one may suppose `G` split relative to `T`. The assertion then follows immediately from 5.4.5 (ii).

One is led to ask which subsets `R′` of `R` are of type (R). One may suppose the group adjoint; one then has to verify
that `g_{R′}` is a Lie algebra and that its normalizer is smooth at every point of the unit section. The most important
case is given by:

**Theorem 5.4.7.** *Every closed subset `R′` of `R` is of type (R). (Recall, cf. Exp. XXI 3.1.4, that `R′ ⊂ R` is
called* closed *if `α, β ∈ R′`, `α + β ∈ R` entail `α + β ∈ R′`.)*

<!-- label: III.XXII.5.4.7 -->

**Remark 5.4.8.** *We shall see later (Exp. XXIII 6.6) that if `6 · 1_S ≠ 0`[^N.D.E-XXII-35] (for example, if `S` has
residue characteristic distinct from 2 and 3), the fact that `g_{R′}` is a Lie algebra already entails that `R′` is
closed, so `R′` is of type (R) if and only if it is closed. Theorem 5.4.7 thus gives all subsets of type (R)
"independent of the characteristic".*

<!-- label: III.XXII.5.4.8 -->

Let us first prove:

**Lemma 5.4.9.** *Choose for each `α ∈ R` an `Xα ∈ Γ(S, gα)×`. Let `α, β ∈ R`, with `α + β ≠ 0` and let `q` be the
largest integer `i` such that `α + iβ ∈ R`. There exist sections `Mα,β,i ∈ Γ(S, O_S)`, uniquely determined, such that*

<!-- label: III.XXII.5.4.9 -->

```text
Ad(expα(xXα))(Xβ) = Xβ + ∑_{i=1}^{q} Mα,β,i x^i X_{β+iα},
```

*for every `x ∈ Ga(S′)`, `S′ → S`.*

Indeed, `x ↦ Ad(expα(xXα))(Xβ)` defines a morphism `Ga,S → W(g) ≃ Gm_{a,S}`. There thus exist sections `Y_n ∈ Γ(S, g)`,
uniquely determined, such that

```text
Ad(expα(xXα))(Xβ) = ∑_{n ⩾ 0} x^n Y_n.
```

Applying the inner automorphism defined by a section `t` of `T`, one finds immediately

```text
Ad(t)(Y_n) = β(t) α(t)^n Y_n,
```

which entails `Y_n ∈ Γ(S, g^{β+nα})`. Since `α` and `β` are not proportional, none of the `β + nα` is zero; one thus has
`Y_n = 0` for `n > q`, `Y_n = Mα,β,n X_{β+nα}` for `0 ⩽ n ⩽ q`, where `Mα,β,n ∈ Ga(S)` is uniquely determined. Setting
`x = 0` in the formula obtained, one finds `Y₀ = Xβ`, which completes the proof.

**Remark 5.4.10.** *Differentiating the preceding formula at `x = 0`, one finds*

<!-- label: III.XXII.5.4.10 -->

```text
[Xα, Xβ] = { Nα,β X_{α+β},  where Nα,β = Mα,β,1, if α + β ∈ R,
           { 0                                  if α + β ∉ R, α + β ≠ 0.
```

Let us now prove 5.4.7. If `R′` is a closed subset of `R`, then `g_{R′}` is a Lie subalgebra of `g`, by 5.4.10 and Exp.
XX 2.10, formula (3). By 5.4.9 and Exp. XX 2.10, formula (2), `Uα` normalizes `g_{R′}` for each `α ∈ R′`. Choose a
system of positive roots `R+` and consider the open set `Ω_{R+}` of 4.1.2; let `Ω_{R+, R′}` be the closed subscheme of
`Ω_{R+}` defined as follows:

```text
Ω_{R+, R′} = ∏_{α ∈ R′ ∩ −R+} Uα · T · ∏_{α ∈ R′ ∩ R+} Uα.
```

The canonical immersion `Ω_{R+, R′} → G` factors through `i : Ω_{R+, R′} → Norm_G(g_{R′})`. Suppose `G` adjoint; the
tangent map of `i` at the points of the unit section is bijective by 5.3.2; in particular, the morphism `i` is étale at
every point of the unit section, hence is a local immersion[^N.D.E-XXII-36] at every point of the unit section, hence
`Norm_G(g_{R′})` is smooth at every point of the unit section, as was to be shown.

### 5.5. Borel subgroups of a split reductive group

<!-- label: III.XXII.5.5 -->

**Proposition 5.5.1.** *Let `(G, T, M, R)` be an `S`-split group. For every system of positive roots `R+` of `R`,
`H_{R+}` (which exists by 5.4.7) is a Borel subgroup of `G` and, for every ordering on `R+`, the morphism induced by the
product in `G`*

<!-- label: III.XXII.5.5.1 -->

```text
T ×_S ∏_{α ∈ R+} Uα → G
```

*is a closed immersion with image `H_{R+}`. One writes `B_{R+} = H_{R+}`.*

By definition of the Borel subgroups, the first assertion may be verified by replacing `S` by the spectrum of an
algebraically closed field. Let `B` be the Borel subgroup of `G` containing `T` and corresponding to the system of
positive roots `R+` (Bible, § 10.4, prop. 9); the Lie algebra of `B` is `g_{R+}`; one therefore has `B = H_{R+}` by
5.3.5.

Let us prove the second assertion: the morphism in the statement induces an open immersion
`i : T ×_S ∏_{α ∈ R+} Uα → H_{R+}` (5.4.4). Now `i` is surjective (Bible, § 15.1, cor. 1 to prop. 1).

**Corollary 5.5.2.** *Choose an arbitrary ordering on `R+` and for each `α ∈ R+` an `Xα ∈ Γ(S, gα)×`. Let `α, β ∈ R+`.
For each pair `(i, j) ∈ ℕ* × ℕ*` such that `iα + jβ ∈ R`, there exists a unique section*

<!-- label: III.XXII.5.5.2 -->

```text
C_{i,j,α,β} ∈ Γ(S, O_S)
```

*such that, for all `x, y ∈ Ga(S′)`, `S′ → S`, one has*

```text
expα(xXα) expβ(yXβ) expα(xXα)⁻¹ =
    expβ(yXβ) ∏_{i,j ∈ ℕ*, iα+jβ ∈ R} exp_{iα+jβ}(C_{i,j,α,β} x^i y^j X_{iα+jβ}).
```

If `α = β`, the assertion is trivial. Suppose therefore `α ≠ β`; then, by virtue of the proposition, there exist unique
morphisms

```text
F₀ : G²_{a,S} → T,    Fγ : G²_{a,S} → Ga,S    (γ ∈ R+)
```

such that one has

```text
exp(xXα) exp(yXβ) exp(xXα)⁻¹ = F₀(x, y) ∏_{γ ∈ R+} exp(Fγ(x, y) Xγ).
```

Let `t ∈ T(S′)`, `S′ → S`. Let `int(t)` act on this formula; one immediately has the relations

```text
(1)   F₀(α(t) x, β(t) y) = F₀(x, y),
(2)   Fγ(α(t) x, β(t) y) = γ(t) Fγ(x, y).
```

Since `α` and `β` are two linearly independent characters (over `ℚ`) of `T`, one concludes as usual from the first
relation that `F₀` is constant, so `F₀(x, y) = e`. Write next

```text
Fγ(x, y) = ∑ aᵢⱼ x^i y^j,    with aᵢⱼ ∈ Γ(S, O_S).
```

Substituting in relation (2) and identifying the polynomials of the two sides, one finds

```text
aᵢⱼ (α(t)^i β(t)^j − γ(t)) = 0.
```

If `γ ≠ iα + jβ`, one knows (Exp. XIX 4.13) that there exists an `S′ → S` faithfully flat quasi-compact and a
`t ∈ T(S′)` such that `α(t)^i β(t)^j − γ(t) = 1`. One thus has `aᵢⱼ = 0` on `S′`, hence on `S`. If `γ = iα + jβ`, one
sets `aᵢⱼ = C_{i,j,α,β}`. Setting `x = 0` (resp. `y = 0`), one finds `C_{0,1,α,β} = 1` (resp. `C_{1,0,α,β} = 0`).

**Remark 5.5.3.** *Differentiating at `y = 0` and comparing with 5.4.9, one finds*

<!-- label: III.XXII.5.5.3 -->

```text
C_{i,1,α,β} = Mα,β,i.
```

**Corollary 5.5.4.** *Let `S` be a scheme, `G` an `S`-reductive group, `T` a maximal torus of `G`, `α ≠ β` two roots of
`G` relative to `T` such that `α + β` is non-trivial on every fiber. Order the set of `iα + jβ` (`i, j ∈ ℕ*`) in an
arbitrary way. For all `i, j ∈ ℕ*` such that `iα + jβ ∈ R`, there exists a unique morphism of `O_S`-modules*

<!-- label: III.XXII.5.5.4 -->

```text
fα,β,i,j : (gα)^{⊗i} ⊗ (gβ)^{⊗j} → g^{iα+jβ}
```

*such that for every `S′ → S` and every `X ∈ W(gα)(S′)`, `Y ∈ W(gβ)(S′)` one has (the `exp` on the right being taken in
the sense of 1.2[^N.D.E-XXII-37]):*

```text
expα(X) expβ(Y) expα(−X) = expβ(Y) ∏_{(i,j)} exp_{iα+jβ}(fα,β,i,j(X^i ⊗ Y^j)).
```

The assertion is local for (fpqc). By § 2, one may therefore suppose `G` split relative to `T`, and `α` and `β` constant
in the splitting. Since `α + β ≠ 0`, there exists a system of positive roots `R+` containing `α` and `β` (Exp. XXI
3.5.4), and one is reduced to 5.5.2.

**Corollary 5.5.5.** *Let `S` be a scheme, `G` an `S`-reductive group.*

<!-- label: III.XXII.5.5.5 -->

*(i) `G` possesses Borel subgroups locally for the étale topology. If `T` is a maximal torus of `G`, then `G` also
possesses Borel subgroups containing `T` locally for the étale topology.*

*(ii) If `T` is a maximal torus of `G`, the "functor of Borel subgroups of `G` containing `T`" is representable by a
principal homogeneous bundle under `W_G(T)`.*

*(iii) If `(G, T, M, R)` is split, every Borel subgroup `B` of `G` containing `T` is locally on `S` of the form
`B_{R+}`, where `R+` is a system of positive roots of `R`.*

*(iv) If `T ⊂ B` is a Killing couple of `G`, there exists a covering family `{S_i → S}` for the étale topology, and for
each `i` a splitting `(G_{S_i}, T_{S_i}, M_i, R_i)` and a system of positive roots `R_{i+}` of `R_i` such that
`B_{S_i} = B_{R_{i+}}`.*

Indeed, (i) follows from 2.3 and 5.5.1, (ii) from (i) and 5.3.15, (iii) from (ii) and 5.5.1, (iv) from (iii) and 2.3.

**Lemma 5.5.6.** *Choose on the group `Γ₀(R)` generated by the roots a structure of totally ordered group such that the
positive roots are the elements of `R+` (cf. Exp. XXI 3.5.6).[^N.D.E-XXII-38] Let `α₁ < ⋯ < α_N` be the elements of
`R+`. Consider the isomorphism*

<!-- label: III.XXII.5.5.6 -->

```text
f : T ×_S U_{α₁} ×_S ⋯ ×_S U_{αN} → B_{R+}
```

*induced by the product in `G`. Set for `i = 1, …, N`:*

```text
U_{⩾i} = f(U_{αᵢ} ×_S ⋯ ×_S U_{αN}).
```

*(i) Each `U_{⩾i}` is a normal subgroup of `B_{R+}`.*

*(ii) For `1 ⩽ i ⩽ N − 1`, `U_{⩾i}` is identified with the semi-direct product*

```text
U_{⩾i} = U_{αᵢ} · U_{⩾i+1}.
```

*(iii) `B_{R+}` is identified with the semi-direct product*

```text
B_{R+} = T · U_{⩾1}.
```

*(iv) For `1 ⩽ i ⩽ N − 1`, the inner automorphisms of `U_{⩾1}` act trivially on `U_{⩾i}/U_{⩾i+1}` (which is identified
with `U_{αᵢ}` by (ii)).*

Let us first prove by induction on `i` the following assertion:

> `U_{⩾i}` is a normal subgroup of `B_{R+}`, semi-direct product of `U_{αᵢ}` and `U_{⩾i+1}`.

The assertion is true for `i = N`; suppose it for `i + 1` and let us prove it for `i`. One has (as schemes)

```text
U_{⩾i} = U_{αᵢ} · U_{⩾i+1};
```

it is clear first that `U_{⩾i}` is stable under the inner automorphisms of `B_{R+}`. This is clear for `int(t)`,
`t ∈ T(S)`; it suffices to verify it for `int(x)`, `x ∈ Uα(S)`, `α ∈ R+`. Now `U_{⩾i+1}` is supposed normal, so it
suffices to see that `int(x) U_{αᵢ} ⊂ U_{⩾i}`. By 5.5.2, if `y ∈ U_{αᵢ}(S′)`, one has `y⁻¹ x y x⁻¹ ∈ U_{⩾i+1}(S′)`,
which entails `int(x)(y) ∈ U_{⩾i}(S′)`.

Let us now prove that `U_{⩾i}` is a subgroup of `B_{R+}`. If `x, y ∈ U_{⩾i}(S)`, one may write `x = p x′`, `y = q y′`,
with `p, q ∈ U_{αᵢ}(S)`, and `x′, y′ ∈ U_{⩾i+1}(S)`. One has

```text
xy = p x′ q y′ = pq(q⁻¹ x′ q) y′ ∈ U_{αᵢ}(S′) U_{⩾i+1}(S′);
```

similarly `x⁻¹ = p⁻¹ (p x′⁻¹ p⁻¹) ∈ U_{αᵢ}(S′) U_{⩾i+1}(S′)`. We have thus proved (i) and (ii), as well as (iv) along
the way. As for (iii), it is a trivial consequence of 5.5.1.

**Lemma 5.5.7.** *With the preceding notations, choose for each `1 ⩽ i ⩽ N` an `X_i ∈ Γ(S, g^{αᵢ})×` and consider the
isomorphism*

<!-- label: III.XXII.5.5.7 -->

```text
a : G^N_{a,S} → U_{⩾1}
```

*defined set-theoretically by*

```text
a(x₁, …, x_N) = exp_{α₁}(x₁ X₁) ⋯ exp_{αN}(x_N X_N).
```

*There exists a unique family `(Qᵢ)`, `i = 1, …, N`, of polynomials*

```text
Qᵢ = Qᵢ(x₁, …, x_N, y₁, …, y_N)
```

*with coefficients in `Γ(S, O_S)` such that one has set-theoretically*

```text
a(x₁, …, x_N) a(y₁, …, y_N) = a(Q₁(x₁, …, y_N), …, Q_N(x₁, …, y_N)).
```

*Furthermore, the `Qᵢ` have coefficients in the subring of `Γ(S, O_S)` generated by the `C_{i,j,α,β}` of 5.5.2
(`α, β ∈ R+`, `i, j ∈ ℕ*`) and each `Qᵢ` is of the form*

```text
Qᵢ(x₁, …, y_N) = xᵢ + yᵢ + Q′ᵢ(x₁, …, xᵢ₋₁, y₁, …, yᵢ₋₁).
```

The existence and uniqueness of the `Qᵢ` follow immediately from the fact that `a` is an isomorphism of schemes.
Denoting `z`, `z′`, `z′′` sections of `U_{⩾i+1}`, one has

```text
a(x₁, …, x_N) a(y₁, …, y_N) =
  a(x₁, …, xᵢ₋₁, 0, …, 0) exp(xᵢ Xᵢ) z · a(y₁, …, yᵢ₋₁, 0, …, 0) exp(yᵢ Xᵢ) z′;
```

using 5.5.6 (i) and (iv), the right-hand side is written

```text
a(x₁, …, xᵢ₋₁, 0, …, 0) a(y₁, …, yᵢ₋₁, 0, …, 0) exp((xᵢ + yᵢ) Xᵢ) z′′;
```

which gives, reusing 5.5.6,

```text
Qᵢ(x₁, …, x_N, y₁, …, y_N) = xᵢ + yᵢ + Q′ᵢ(x₁, …, xᵢ₋₁, y₁, …, yᵢ₋₁),
```

with

```text
Q′ᵢ(x₁, …, xᵢ₋₁, y₁, …, yᵢ₋₁) = Qᵢ(x₁, …, xᵢ₋₁, 0, …, 0, y₁, …, yᵢ₋₁, 0, …, 0);
```

that is, the precise form requested.

Let us prove finally the assertion on the coefficients of the polynomials `Qᵢ`. Let `A` be the subring of `Γ(S, O_S)`
generated by the `C_{i,j,α,β}` (`α, β ∈ R+`, `i, j ∈ ℕ*`). Let us prove by descending induction on `i` that if
`x₁ = ⋯ = xᵢ₋₁ = 0` and `y₁ = ⋯ = yᵢ₋₁ = 0`, that is, if `a(x₁, …, x_N)` and `a(y₁, …, y_N)` are sections of `U_{⩾i}`,
then the polynomials

```text
Rⱼ(xᵢ, …, x_N, yᵢ, …, y_N) = Qⱼ(x₁, …, x_N, y₁, …, y_N)
```

have coefficients in `A`. This is trivial for `i = N` and also for `j < i` (because `Rⱼ = 0` for `j < i`). Let `i < N`,
suppose the assertion verified for `i + 1`, and let us prove it for `i` (and `j ⩾ i`). One has

```text
a(0, …, 0, xᵢ, …, x_N) = exp(xᵢ Xᵢ) a(0, …, 0, xᵢ₊₁, …, x_N) = exp(xᵢ Xᵢ) Zᵢ.
```

Similarly write

```text
a(0, …, yᵢ, …, y_N) = exp(yᵢ Xᵢ) Tᵢ.
```

One has

```text
a(0, …, xᵢ, …, x_N) a(0, …, yᵢ, …, y_N) = exp((xᵢ + yᵢ) Xᵢ) int(exp(−yᵢ Xᵢ))(Zᵢ) · Tᵢ.
```

Now

```text
int(exp(−yᵢ Xᵢ))(Zᵢ) = int(exp(−yᵢ Yᵢ))(exp(xᵢ₊₁ Xᵢ₊₁) ⋯ exp(x_N X_N))
```

is a product of `N − i − 1` sections of `U_{⩾i+1}` whose coefficients in the decomposition
`U_{⩾i+1} = U_{αᵢ₊₁} ⋯ U_{αN}` are polynomials in `yᵢ` and `xᵢ₊₁`, …, `x_N` with coefficients in `A` (by 5.5.2).
Applying the induction hypothesis, one deduces that the coefficients of

```text
int(exp(−yᵢ Xᵢ))(Zᵢ) · Tᵢ
```

are also polynomials with coefficients in `A`, which finishes the proof.

Let us remark that the preceding induction immediately gives a proof of:

**Lemma 5.5.8.** *With the notations of 5.5.6, let, for each `i = 1, …, N`, a morphism of groups*

<!-- label: III.XXII.5.5.8 -->

```text
fᵢ : U_{αᵢ} → H,
```

*where `H` is an `S`-group functor. For the morphism*

```text
f : U_{⩾1} → H
```

*defined by*

```text
f(exp(x₁ X₁) ⋯ exp(x_N X_N)) = f₁(exp(x₁ X₁)) ⋯ f_N(exp(x_N X_N))
```

*to be a morphism of groups, it is necessary and sufficient that for every pair `i < j`, one has*

```text
fⱼ(exp(xⱼ Xⱼ)) fᵢ(exp(xᵢ Xᵢ)) fⱼ(exp(−xⱼ Xⱼ)) = f(exp(xⱼ Xⱼ) exp(xᵢ Xᵢ) exp(−xⱼ Xⱼ)).
```

### 5.6. Subgroups of type (R) with solvable fibers

<!-- label: III.XXII.5.6 -->

**Proposition 5.6.1.** *Let `(G, T, M, R)` be an `S`-split group, `R′` a subset of `R` of type (R) (5.4.2), `H_{R′}` the
corresponding subgroup of `G`. The following conditions are equivalent:*

<!-- label: III.XXII.5.6.1 -->

*(i) `H_{R′}` has solvable geometric fibers.*

*(ii) There exists a system of positive roots `R+` such that `R′ ⊂ R+`, hence `H_{R′} ⊂ B_{R+}` (cf. 5.4.5).*

*(iii) `R′ ∩ −R′ = ∅`.*

*(iv) For every ordering on `R′`, the morphism induced by the product in `G`*

```text
T ×_S ∏_{α ∈ R′} Uα → H_{R′}
```

*is an isomorphism.*

*(v) `H_{R′} ∩ Norm_G(T) = T`.*

*(vi) For every subset `R′′` of `R`, of type (R), one has (cf. 5.4.5)*

```text
H_{R′} ∩ Norm_G(H_{R′′}) = H_{R′ ∩ R′′}.
```

We shall prove these equivalences according to the logical scheme

```text
(iii) ⇔ (ii) ⇒ (vi)
              ⇒ (iv) ⇒ (v)
              ⇒ (i) ⇔ (ii).
```

One obviously has (ii) ⇒ (iii) and (vi) ⇒ (v) (take `R′′ = ∅`). By 5.4.6, it suffices to verify (i) ⇒ (ii) on geometric
fibers; now if `S` is the spectrum of an algebraically closed field, `H_{R′}` is contained in a Borel subgroup
containing `T`, so of the form `H_{R+}` (5.5.5 (iii)).

Similarly (iii) ⇒ (i) is verified on geometric fibers; suppose (iii) is satisfied; if `H_{R′}` were not solvable, there
would exist a subtorus `Q` of `T`, of codimension 1 in `T`, such that `Centr_{H_{R′}}(Q)` is not solvable (Bible, §
10.4, prop. 8); now `Centr_{H_{R′}}(Q)` has Lie algebra `g_{R′′}`, where `R′′` is the set of roots of `R′` vanishing on
`Q`, so `R′′ = ∅` or `{α}` (by virtue of (iii)); hence `Centr_{H_{R′}}(Q)`, which is a subgroup of type (R) of `G`, is
`T` or `T · Uα`, hence solvable, contrary to the hypothesis.

Similarly (ii) ⇒ (iv) is verified on geometric fibers (since these are flat `S`-schemes of finite presentation); by
Bible, § 13.2, th. 1 d), the morphism in question is bijective; it induces an isomorphism on the tangent spaces at the
origin, and one concludes as usual (cf. 4.1.1).

One has (iv) ⇒ (v) by 4.2.7. To prove (v) ⇒ (i), one is again reduced to the case where `S` is the spectrum of an
algebraically closed field, and one concludes by Bible, § 10.3, cor. to prop. 6 and § 9.3, cor. 3 to th. 1.

It thus remains only to prove the assertion (ii) ⇒ (vi). One may reduce to the case where `G` is adjoint. One then has,
by 5.3.3,

```text
Norm_G(H_{R′′}) = Norm_G(g_{R′′}) ⊂ Transp_G(t, g_{R′′}).
```

[^N.D.E-XXII-39] By 5.4.5, it suffices to prove

```text
(x)    H_{R′}(S) ∩ Transp_{G(S)}(t, g_{R′′}) ⊂ H_{R′ ∩ R′′}(S).
```

Let us first prove a lemma.

**Lemma 5.6.2.** *In the notations of 5.5.7, let*

<!-- label: III.XXII.5.6.2 -->

```text
u = exp(x₁ X₁) ⋯ exp(x_N X_N)
```

*where `xᵢ ∈ Ga(S)`. Let `m` be an integer, `1 ⩽ m ⩽ N`, such that `xᵢ = 0` for `i < m`.*

*(a) If `H ∈ Γ(S, t)`, the component of `Ad(u) H` on `g^{αₘ}` is*

```text
−αₘ(H) xₘ Xₘ.
```

*(b) If `Y ∈ Γ(S, g^{−αₘ})`, the component of `Ad(u) Y` on `t` is (with the notations of Exp. XX 2.6)*

```text
xₘ ⟨Xₘ, Y⟩ H_{αₘ}.
```

Denote indeed `u = g^{αₘ₊₁} + ⋯ + g^{αN}`. By 5.4.9, one has

```text
Ad(exp(xᵢ Xᵢ)) u ⊂ u,    for i > m.
```

By Exp. XX 2.10, one has

```text
Ad(exp(xᵢ Xᵢ)) H = H − αᵢ(H) xᵢ Xᵢ.
```

This immediately gives, modulo `u`,

```text
Ad(u) H = Ad(exp(xₘ Xₘ)) H = H − αₘ(H) xₘ Xₘ,
```

which entails the first result.

Likewise denote[^N.D.E-XXII-40] `n = g^{α₁} + ⋯ + g^{αN}` and `u₁ = exp(xₘ₊₁ Xₘ₊₁) ⋯ exp(x_N X_N)`. For `i > m`, one has
`αᵢ > αₘ` so, by 5.4.9, one has, modulo `n`,

```text
Ad(u₁) Y ≡ Y,    whence    Ad(u) Y ≡ Ad(exp(xₘ Xₘ)) Y.
```

Applying Exp. XX 2.10, one therefore obtains, modulo `n`,

```text
Ad(u) Y − Y ≡ xₘ ⟨Xₘ, Y⟩ H_{αₘ}
```

whence the second result.

Let us return to the proof of inclusion (x). Suppose that there exists `h ∈ H_{R′}(S)`, `h ∉ H_{R′ ∩ R′′}(S)`, such that

```text
Ad(h) t ⊂ g_{R′′}.
```

One may write

```text
h = t exp(x₁ X₁) ⋯ exp(x_N X_N).
```

Since `h ∉ H_{R′ ∩ R′′}(S)`, there exists a smallest `m` such that

```text
t exp(x₁ X₁) ⋯ exp(x_{m−1} X_{m−1}) ∈ H_{R′ ∩ R′′}(S)    and    αₘ ∉ R′′,   xₘ ≠ 0.
```

Then `h′ = exp(xₘ Xₘ) ⋯ exp(x_N X_N)` also satisfies the conditions imposed on `h` above. But by 5.6.2, for every
`H ∈ Γ(S, t)` the component of `Ad(h′) H` on `g^{αₘ}` is `−αₘ(H) xₘ Xₘ`. By virtue of the hypothesis on `h` and on `m`,
one has therefore `αₘ(H) = 0` for every `H ∈ Γ(S, t)`, which is impossible (because `G` is supposed adjoint and `αₘ` is
therefore non-zero on every fiber).

**Remark 5.6.2. bis.** *Resume the notations of 5.6.2. If `Ad(u)` is the identity on `t` and on `g^{−αₘ}`, one has
`xₘ = 0`. Indeed, one has `xₘ αₘ = 0` and `xₘ H_{αₘ} = 0`; if `αₘ ∉ 2M`, then `αₘ` is non-zero on every fiber; if
`αₘ ∈ 2M`, then `α*_m ∉ 2M*` and `H_{αₘ}` is non-zero on every fiber; in each case, this entails `xₘ = 0`. It follows
that `u = e` if `Ad(u)` operates trivially on `g`.*

<!-- label: III.XXII.5.6.2.bis -->

**Remark 5.6.3.** *If `H` is a subgroup of type (R) of the reductive group `G`, with solvable geometric fibers, then `H`
is closed in `G` and `Norm_G(H)/H` is representable by a separated finite étale `S`-scheme.*

<!-- label: III.XXII.5.6.3 -->

This follows from 5.3.18 and, at one's choice, 3.5 or Exp. XIX 2.5 (ii).

**Corollary 5.6.4.** *Let `(G, T, M, R)` be a split reductive group. If `R′ ⊂ R` is closed and `R′ ∩ −R′ = ∅`, then `R′`
is contained in a system of positive roots.*[^N.D.E-XXII-41]

<!-- label: III.XXII.5.6.4 -->

Indeed, `R′` is of type (R) by 5.4.7, so the result follows from 5.6.1.

**Corollary 5.6.5.** *Under the conditions of 5.6.1, the product in `G` induces an isomorphism*

<!-- label: III.XXII.5.6.5 -->

```text
∏_{α ∈ R′} Uα ⥲ U_{R′},
```

*where `U_{R′}` is a closed group subscheme of `G`, smooth over `S`, with connected and unipotent geometric fibers,
independent of the choice of ordering on `R′`. Moreover, `H_{R′}` is the semi-direct product `T · U_{R′}` (`U_{R′}`
normal).*

Indeed, if `R′ ⊂ R+`, then `H_{R′} ∩ U_{⩾1}` (notations of 5.5.6) is a closed subgroup of `G` of finite presentation,
normal in `H_{R′}`. By 5.6.1 (iv), one has `H_{R′} = T · U_{R′}`, which entails the other assertions.

**Remark 5.6.6.** *In particular, `U_{R+}` is the group `U_{⩾1}` of 5.5.6.*

<!-- label: III.XXII.5.6.6 -->

Let us extract some corollaries of the preceding results concerning groups of type `U_{R′}`.

**Corollary 5.6.7.** *Let `(G, T, M, R)` be a split reductive group, `R′` and `R′′` two subsets of `R` of type (R), with
`R′ ∩ −R′ = ∅`.*

<!-- label: III.XXII.5.6.7 -->

*(i) One has*

```text
U_{R′} ∩ Norm_G(H_{R′′}) = U_{R′ ∩ R′′}.
```

*(ii) Suppose `R′` closed. If the conditions `α ∈ R′`, `β ∈ R′′` and `α + β ∈ R` entail `α + β ∈ R′`, then `H_{R′′}`
normalizes `U_{R′}`.*

Indeed, (i) follows immediately from 5.6.5 and 5.6.1 (vi). To prove (ii), it suffices, by 5.4.4, to show that `T` and
each `Uβ`, `β ∈ R′′`, normalize `U_{R′}`.[^N.D.E-XXII-42] For `T`, this is trivial; for `Uβ`, it follows from 5.5.2 and
Exp. XXI 3.1.2.[^N.D.E-XXII-43]

**Corollary 5.6.8.** *Let `(G, T, M, R)` be an `S`-split group, `R+` a system of positive roots, `α` a simple root of
`R+` (i.e. an element of `R+` such that `R+ − {α}` is closed). Denote*

<!-- label: III.XXII.5.6.8 -->

```text
U_{α̂} = U_{R+ − {α}}.
```

*Then*

*(i) `U_{α̂}` is a normal subgroup of `B_{R+}`.*

*(ii) `U_{R+}` is the semi-direct product of `U_{α̂}` by `Uα`.*

*(iii) `U_{−α}` normalizes `U_{α̂}`.*

*(iv) `Zα` normalizes `U_{α̂}`.*

*If one defines similarly `U_{−α̂} = U_{R− − {−α}}` (where `R− = −R+`), one has*

```text
Ω_{R+} = U_{−α̂} · U_{−α} · T · Uα · U_{α̂}.
```

Indeed, (ii) follows from 5.6.5, and (i) from 5.6.7 (ii). Similarly, (iii) follows from 5.5.2 (indeed, if `β ∈ R+`,
`β ≠ α`, no combination `i(−α) + jβ`, with `i, j > 0`, can be negative because `β` contains at least one simple root
`≠ α`). Then (iv) follows from (i) and (iii), because `U_{−α} · T · Uα` is schematically dense in `Zα`. Finally, the
last assertion follows from (ii) and its analogue for `U_{R−}`.

Let us return to the general situation.

**Proposition 5.6.9.** *Let `S` be a scheme, `G` an `S`-reductive group, `H` a subgroup of type (R) with solvable
geometric fibers.*

<!-- label: III.XXII.5.6.9 -->

*(i) `D_S(H) = Hom_{S-gr.}(H, Gm,S)` is representable by a twisted constant `S`-group, whose type at `s ∈ S` is
`ℤ^{rg_red(G_s)}`. The biduality morphism (Exp. VIII § 1)*

```text
f : H → D_S(D_S(H))
```

*is smooth and surjective.*

*(ii) The kernel `H_u` of `f` is the largest closed normal group subscheme of `H`, smooth over `S`, with connected and
unipotent geometric fibers. We call it the* unipotent part *of `H` and write also `H_u = rad_u(H)`.*

*Then `H_u` is also the sheaf of commutators of `H`: every morphism of groups from `H` to an `S`-presheaf of commutative
groups separated for (fppf) vanishes on `H_u` and thus factors through `H/H_u = D_S(D_S(H))`.*

*(iii) If `T` is a maximal torus of `H`, the morphism `T → H` induces isomorphisms `D_S(H) ⥲ D_S(T)` and
`T ⥲ D_S(D_S(H))`. Furthermore, `H` is identified with the semi-direct product of `H_u` by `T`.*

*(iv) In the situation of 5.6.1, if `H = H_{R′}`, then `H_u = U_{R′}`.*

The assertions of the proposition are local for the étale topology (Exp. X 5.5). One may therefore reduce to the case of
5.6.1. One then knows (5.6.5) that `H_{R′}` is the semi-direct product of `U_{R′}` by `T`. Let us show that `U_{R′}` is
the sheaf of commutators of `H_{R′}`: since `H_{R′}/U_{R′} = T` is commutative, it suffices to prove that every morphism
of groups `φ : H_{R′} → V` as in (ii) vanishes on `U_{R′}`. It suffices to prove that `φ` vanishes on each `Uα`,
`α ∈ R′`. Now if `t ∈ T(S′)`, `X ∈ W(gα)(S′)`, one has

```text
1 = φ(t expα(X) t⁻¹ expα(−X)) = φ(expα((α(t) − 1) X)).
```

Since `α : T → Gm,S` is faithfully flat, one deduces immediately that `φ` vanishes on `U×_α`; but every section of `Uα`
is locally the sum of two sections of `U×_α`. One thus has

```text
Hom_{S-gr.}(H, V) = Hom_{S-gr.}(H/U_{R′}, V)
```

for every `V` as above. Applying this result to `V = Gm,S`, one deduces immediately (i) and (iii), then (iv) and the
second assertion of (ii). It now suffices to prove the first assertion of (ii); the only non-trivial fact is that every
closed normal subgroup `U` of `H`, smooth over `S` with connected unipotent geometric fibers, is a subgroup of `H_u`.
Now one first has:

**Lemma 5.6.10.** *Let `G` be an `S`-reductive group, `T` a maximal torus, `U` a group subscheme of `G`, smooth over
`S`, with unipotent geometric fibers, normalized by `T`. Then `U ∩ T = e`.*

<!-- label: III.XXII.5.6.10 -->

Indeed, since `T = Centr_G(T)`, one has `U ∩ T = U^T` (invariants under `int(T)`). Applying Exp. XIX 1.4, one deduces
that `U ∩ T` is smooth over `S`, but it is also radicial over `S`: for every `s ∈ S`, `U(s) ∩ T(s)` consists of elements
that are simultaneously unipotent and semisimple. This proves the lemma.

Let us return to the proof of 5.6.9 (ii). If `U` is a normal subgroup of `H` as above, then the semi-direct product
`T · U` is a subgroup of type (R) of `G`, with solvable geometric fibers. One may therefore suppose it of the form
`H_{R′′}`, with `R′′ ⊂ R′`. It suffices to prove `U = U_{R′′}` and one is therefore reduced to the case where
`H = T · U`; but the quotient `H/U` being commutative, `U` is a subsheaf of the sheaf of commutators of `H`, which is
`H_u`. QED.

Let us remark that we have in fact just proved:

**Proposition 5.6.11.** *Let `S` be a scheme, `G` an `S`-reductive group, `T` a maximal torus of `G`. The maps*

<!-- label: III.XXII.5.6.11 -->

```text
H ↦ H_u,    U ↦ T · U
```

*are mutually inverse bijections between the set of subgroups `H` of type (R) of `G` containing `T` and having solvable
geometric fibers, and the set of subgroups `U` of `G`, smooth over `S`, normalized by `T`, with connected and unipotent
geometric fibers.*[^N.D.E-XXII-44]

In particular, when `(G, T, M, R)` is split, the groups `H_{R′}` and `U_{R′}` correspond.

**Corollary 5.6.12.** *Let `S` be a scheme, `(G, T, M, R)` an `S`-split group (resp. and `R+` a system of positive roots
of `R` defining the Borel subgroup `B`).*

<!-- label: III.XXII.5.6.12 -->

*Every smooth group subscheme of `G` with connected and unipotent geometric fibers (resp. every smooth group subscheme
of `B_u`) normalized by `T` is locally on `S` of the form `U_{R′}`, where `R′` is a subset of `R` contained in a system
of positive roots (resp. a subset of `R+`) of type (R).*

For the "resp." case, it suffices to note that the geometric fibers of the given group are unipotent and connected, by
Bible, § 13.2, th. 1 (d).

Proposition 5.6.9 has moreover the following corollary:

**Corollary 5.6.13.** *Let `S` be a scheme, `G` an `S`-reductive group, `H` a subgroup of type (R) with solvable
geometric fibers, `Tor(H)` the functor of maximal tori of `H`:*

<!-- label: III.XXII.5.6.13 -->

```text
Tor(H)(S′) = {maximal tori of H_{S′}}.
```

*Then `Tor(H)` is representable by an affine and smooth `S`-scheme, which is a principal homogeneous bundle under `H_u`
for the law `(h, T) ↦ int(h) T`.*[^N.D.E-XXII-45]

Indeed, if `T` and `T′` are two maximal tori of `H_{S′}`, there exists a unique section `h ∈ H_u(S′)` such that
`int(h) T = T′`. The uniqueness of `h` follows immediately from the equality

```text
Norm_G(T) ∩ H_u = e
```

(cf. for example 5.6.1); it therefore suffices to prove the existence of `h` locally for the étale topology. By 5.2.6
and 5.1.2 (a), one may suppose `T` and `T′` conjugate by a section of `H`, whence the desired conclusion since
`H = H_u · T` by 5.6.9 (iii). It follows that `Tor(H)` is a principal homogeneous sheaf under `H_u`, which is affine and
smooth over `S`, which immediately entails the statement.[^N.D.E-XXII-46]

### 5.7. Bruhat's theorem

<!-- label: III.XXII.5.7 -->

**Recall 5.7.1.** *Let `k` be an algebraically closed field, `G` a `k`-reductive group, `B` a Borel subgroup of `G`, `T`
a maximal torus of `B`, `N = Norm_G(T)`. Then*

<!-- label: III.XXII.5.7.1 -->

```text
G(k) = B(k) N(k) B(k);
```

*this is Bruhat's theorem (Bible, § 13.4, cor. 1 to th. 3); more precisely, with the notations of 3.6, the sets*

```text
B(k) N_w(k) B(k) = B_u(k) N_w(k) B_u(k)
```

*form, as `w` runs through `(N/T)(k)`, a partition of `G(k)`. If `B′` is another Borel subgroup of `G` containing `T`,
the sets `B′(k) N_w(k) B(k)` also form a partition of `G(k)`. Indeed, if `y ∈ N(k)` is such that `int(y) B = B′`, one
has*

```text
y B(k) N_w(k) B(k) = B′(k) N_{yw}(k) B(k).
```

**Definition 5.7.2.** *Let `(G, T, M, R)` be an `S`-split group, `R−` a system of positive roots of `R`, `B′ = B_{R−}`
the Borel group it defines. For `w ∈ W`, one writes (cf. 5.6.5):*

<!-- label: III.XXII.5.7.2 -->

```text
R^w_− = R− ∩ w(R−),    B′u_w = U_{R^w_−} = ∏_{α ∈ R^w_−} Uα.
```

*If `n_w ∈ Norm_G(T)(S)` is a representative of `w` (3.8), one may also write*

```text
B′u_w = B′u ∩ int(n_w) B′u.
```

**Lemma 5.7.3.** *Let `(G, T, M, R)` be an `S`-split group, `R+` a system of positive roots of `R`, `R− = −R+`, `B`
(resp. `B′`) the Borel subgroup of `G` defined by `R+` (resp. `R−`). Let `w ∈ W`, `N_w` and `B′u_w` the corresponding
subschemes of `G` (3.8 and 5.7.2).*

<!-- label: III.XXII.5.7.3 -->

*(i) The sheaf `B′ · N_w · B`, image of the morphism*

```text
B′ ×_S N_w ×_S B → G
```

*induced by the product in `G`, is representable by a subscheme of `G` (in fact a closed subscheme of the open set
`n_w Ω_{R+}`).*

*(ii) The morphism*

```text
B′u_w ×_S N_w ×_S B^u → G,
```

*induced by the product in `G`, is an immersion with image the preceding subscheme.*

Let us first show that the morphism of (ii) is an immersion. By definition, `int(n_w)⁻¹` induces a closed immersion of
`B′u_w` into `B′u`, so the morphism

```text
(u, b) ↦ n_w⁻¹ u n_w b
```

induces a closed immersion

```text
B′u_w ×_S B → Ω_{R+}.
```

This immediately entails that the morphism of (ii) induces a closed immersion of the first member into the open set
`n_w Ω_{R+}`. To prove (i), it suffices to see that

```text
B′(S) N_w(S) B(S) = B′u_w(S) N_w(S) B^u(S).
```

Now, if `α ∈ R`, one has `int(n_w) Uα(S) = U_{w(α)}(S)`, so if `w⁻¹(α) ∈ R+`,

```text
Uα(S) N_w(S) B(S) = Uα(S) n_w T(S) B^u(S)
                 = n_w U_{w⁻¹(α)}(S) T(S) B^u(S)
                 = n_w B(S) = N_w(S) B^u(S).
```

This immediately entails, in view of the definition of `R^w_−`, the desired assertion.

**Theorem 5.7.4.** *Let `S` be a scheme, `(G, T, M, R)` an `S`-split group, `B` the Borel subgroup defined by the system
of positive roots `R+`, `B′` the Borel subgroup defined by `R− = −R+`.*

<!-- label: III.XXII.5.7.4 -->

*(i) (Bruhat's theorem) The schemes `B′u_w · N_w · B` form, as `w` runs through `W`, a partition of the underlying set
of `G`.*

*(ii) For each `w ∈ W`, let `n_w` be a representative of `w` in `Norm_G(T)(S)` (3.8); then the open sets
`n_w Ω = n_w B′u · T · B^u` form, as `w` runs through `W`, a cover of `G`.*

The two assertions are verified on geometric fibers, where one concludes by 5.7.1 and 5.7.3.

**Remark 5.7.5.** *(i) entails that if `S` is the spectrum of a field, `G(S)` is the disjoint union of the
`B′u_w(S) · T(S) · B^u(S)`. The corresponding assertion for an arbitrary `S` (even local or artinian) is obviously
false. Note however that (ii) entails that if `S` is local, `G(S)` is the union of the `n_w Ω(S)`. In fact:*

<!-- label: III.XXII.5.7.5 -->

**Corollary 5.7.6.** *Let `Δ` be a system of simple roots of the split group `G` over the local scheme `S`.*

<!-- label: III.XXII.5.7.6 -->

*(i) Then `G(S)` is generated by `T(S)` and the `Uα(S)`, `α ∈ Δ ∪ −Δ`.*

*(ii) If `G` is simply connected (4.3.3), `G(S)` is already generated by the `Uα(S)`, `α ∈ Δ ∪ −Δ`.*

Indeed, let `H` be the subgroup of `G(S)` generated by the `Uα(S)`, `α ∈ Δ ∪ −Δ`. Let us first remark that `H` contains
a representative of each `sα` (`α ∈ Δ`) in `Norm_G(T)(S)` (Exp. XX 3.1), hence a representative `n_w` of each `w ∈ W`.

Since every `α ∈ R` is written `w(α₀)` with `w ∈ W`, `α₀ ∈ Δ`, one has

```text
Uα(S) = int(n_w) U_{α₀}(S) ⊂ H.
```

The subgroup generated by `H` and `T(S)` thus contains `Ω(S)` and is therefore the whole of `G(S)`, by the remark made
above.

If now `G` is simply connected, let us prove that `H ⊃ T(S)`. By Exp. XX 2.7, `H` contains `α*(Gm(S))` for every
`α ∈ Δ`, and it suffices to apply 4.3.8.

**Remark 5.7.6.1.** *Instead of taking, for each `α ∈ Δ`, `Uα(S)` and `U_{−α}(S)`, one may content oneself with taking
`Uα(S)` and a representative `wα` of the symmetry `sα`, or else `Uα(S)` and a section of `U×_{−α}`, ….*

<!-- label: III.XXII.5.7.6.1 -->

**Corollary 5.7.7.** *If `G` is of semisimple rank 1, choose a `uα ∈ U×_α(S)`. Then `Ω` and `uα Ω` form a cover of `G`.*

<!-- label: III.XXII.5.7.7 -->

Indeed, if `u_{−α}` is the section of `U_{−α}` paired with `uα` (cf. 1.3), one has, by 5.7.4 (ii),

```text
G = Ω ∪ u_{−α}⁻¹ uα u_{−α}⁻¹ Ω,
```

whence

```text
G = u_{−α} G = u_{−α} Ω ∪ uα u_{−α}⁻¹ Ω = Ω ∪ uα Ω.
```

**Corollary 5.7.8.** *Let `S` be a scheme, `G` an `S`-reductive group. Then `G` is essentially free over `S` (Exp. VIII
6.1).*[^N.D.E-XXII-47]

<!-- label: III.XXII.5.7.8 -->

Indeed, the assertion is local for the (fpqc) topology; one may suppose `G` split. Then `G` admits a cover by open
subsets isomorphic to `G^N_{a,S} ×_S G^n_{m,S}`, which are essentially free.

**Lemma 5.7.9.** *Under the conditions of 5.7.4, let `α` be a simple root of `R+` and `uα ∈ U×_α(S)`. For every
`v ∈ U_{−α}(S)`, one has*

<!-- label: III.XXII.5.7.9 -->

```text
Ω · v ⊂ Ω ∪ uα · Ω.
```

We have to compare two open subsets of `G`; it suffices to do so when `S` is the spectrum of a field `k`. One thus has
to prove

```text
Ω(k) v ⊂ Ω(k) ∪ uα Ω(k).
```

Now

```text
Ω(k) v = B′u(k) T(k) B^u(k) v = U_{−α̂}(k) U_{−α}(k) T(k) Uα(k) U_{α̂}(k) v
       ⊂ U_{−α̂}(k) Zα(k) U_{α̂}(k) v.
```

(One uses the decomposition of 5.6.8.) Applying now 5.6.8 (iii) and using 5.7.7 for the group `Zα`, one obtains

```text
Ω(k) v ⊂ U_{−α̂}(k) Zα(k) v U_{α̂}(k) ⊂ U_{−α̂}(k) Zα(k) U_{α̂}(k)
       ⊂ U_{−α̂}(k) U_{−α}(k) T(k) Uα(k) U_{α̂}(k)   ∪   U_{−α̂}(k) uα U_{−α}(k) T(k) Uα(k) U_{α̂}(k).
```

Using again 5.6.8 (iii) (for `R−` instead of `R+`), one obtains the result.

**Proposition 5.7.10.** *Under the conditions of 5.7.4, choose for each simple root `α` a `uα ∈ U×_α(S)`. Let `U₁` be
the submonoid of `B^u(S)` generated by the `uα`. The open sets `u Ω`, for `u ∈ U₁`, form a cover of `G`.*

<!-- label: III.XXII.5.7.10 -->

Once again, one may suppose that `S` is the spectrum of a field `k`; by virtue of 5.7.6, it suffices to prove that
`⋃_{u ∈ U₁} u Ω(k)` is stable under right multiplication by `T(k)`, `Uα(k)`, `U_{−α}(k)` (for `α` simple). In the first
two cases, this is trivial. In the last, it follows from the lemma.

**Remark 5.7.11.** *Let us point out a particular case of 5.7.2. If `w = sα` is the symmetry with respect to the simple
root `α`, then*

<!-- label: III.XXII.5.7.11 -->

```text
R− ∩ sα(R−) = R− − {−α}
```

*(Exp. XXI 3.3.1), and, in the notations of 5.6.8, one therefore has*

```text
B′u_{sα} = U_{−α̂}.
```

**Remark 5.7.12.** *In fact, the proof of 5.7.10 immediately gives the following statement: under the conditions of
5.7.10, let `Γ` be a submonoid of `G(S)`; for the open sets `g Ω` (`g ∈ Γ`) to form a cover of `G`, it is necessary and
sufficient that for every `s ∈ S` and every simple root `α`, one has*

<!-- label: III.XXII.5.7.12 -->

```text
(uα)_s B′u(s) ⊂ Γ · B′u(s) · T(s) · B^u(s).
```

**Remark 5.7.13.** *By 5.5.5 (iii), reasoning as in 5.7.1, one obtains immediately the following variant of 5.7.4: let
`(G, T, M, R)` be an `S`-split group, `B` and `B′` two Borel subgroups of `G` containing `T`; for every `w ∈ W`, the
sheaf `B′ · N_w · B` is representable by a subscheme of `G`; these subschemes form, for `w ∈ W`, a partition of the
underlying set of `G`. One may also give the analogue of 5.7.3 (ii): one must set*

<!-- label: III.XXII.5.7.13 -->

```text
B′u_w = B′u ∩ int(n_w) B̃^u
```

*where `B̃` is the Borel subgroup "opposite" to `B` relative to `T` (cf. 5.9.2).*

**Proposition 5.7.14.** *Let `S` be a scheme, `G` an `S`-reductive group, and*

<!-- label: III.XXII.5.7.14 -->

```text
Ad : G → GL_{O_S}(g)
```

*its adjoint representation. Then `Ker(Ad) = Centr(G)` (in other words, the canonical homomorphism deduced from `Ad` by
passage to the quotient:*

```text
Ad : G/Centr(G) = ad(G) → GL_{O_S}(g)
```

*is a monomorphism).*[^N.D.E-XXII-48]

One may suppose `G` split. Choose on `Γ₀(R)` a total ordering structure compatible with the group structure and let `R+`
be the set of positive roots. By virtue of 5.7.4 (ii) and 4.1.6, it suffices to prove that if `n_w` is a representative
of the element `w` of `W`, if `u ∈ U(S)`, `t ∈ T(S)`, `v ∈ U_−(S)`, and if `Ad(n_w v t u) = id`, then `w = e`, `v = e`,
`u = e`. For each `m ∈ R ∪ {0}`, set

```text
g_{>m} = ⨿_{n > m} g^n,    g_{<m} = ⨿_{n < m} g^n.
```

Let `X ∈ Γ(S, g^m)`; write `Ad(tu) X = Ad(v⁻¹ n_w⁻¹) X`. Now

```text
Ad(t) Ad(u) X − m(t) X ∈ Γ(S, g_{>m}),
Ad(v⁻¹ n_w⁻¹) X − Ad(n_w⁻¹) X ∈ Γ(S, g_{<w⁻¹(m)}).
```

If `w ≠ e`, there exists `α ∈ R` such that `w⁻¹(α) < α`, and setting `m = α`, one obtains a contradiction because

```text
Ad(tu) X ∈ Γ(S, g^α + g_{>α}) ∩ Γ(S, g^{w⁻¹(α)} + g_{<w⁻¹(α)}) = 0.
```

Hence `w = e`, and one may choose `n_w = e`; one then has

```text
Ad(v⁻¹) X − X ∈ Γ(S, g_{<m} ∩ (g^m + g_{>m})) = 0,
```

whence `Ad(v) X = X` for every `X ∈ Γ(S, g^m)`, so `Ad(v) = id`. Similarly `Ad(u) = id`. One concludes by 5.6.2 bis.

### 5.8. Schemes associated with a reductive group

<!-- label: III.XXII.5.8 -->

**Theorem 5.8.1.** *Let `S` be a scheme, `G` an `S`-reductive group. Let `H` be the functor of subgroups of type (R) of
`G`: for every `S′ → S`, `H(S′)` is the set of subgroups of type (R) of `G_{S′}` (cf. 5.2.1). Then `H` is representable
by a quasi-projective `S`-scheme of finite presentation over `S`.*

<!-- label: III.XXII.5.8.1 -->

[^N.D.E-XXII-49] Let `G′ = G/Centr(G)` be the adjoint group of `G` (4.3.6) and `u` the morphism `G → G′`. By Exp. XII
7.12, the map `H′ ↦ u⁻¹(H′)` establishes a bijection between the set of subgroups of type (R) of `G′` and of `G` (and
this remains valid after any base change). Thus, replacing `G` by `G′`, one may suppose that `G` is adjoint. Consider
then the morphism

```text
u : H → Grass(g)
```

which associates with each subgroup of type (R) its Lie algebra (which is a sub-`O_S`-module of `g` that is locally a
direct factor.[^N.D.E-XXII-50]). Then `u` is a monomorphism by 5.3.3. It suffices to prove that it is representable by
an immersion of finite presentation, in other words to prove the following assertion: for every `S₁ → S`, given a
sub-`O_S`-module locally a direct factor `h` of `g_{S₁}`, the `S′ → S₁` such that `h_{S′}` is the Lie algebra of a
subgroup of type (R) of `G_{S′}` are exactly those that factor through some subscheme `Σ` of finite presentation of
`S₁`. Replacing `S₁` by `S`, we reduce to `S₁ = S`, and we may furthermore suppose `S` affine; then there exists a
noetherian affine scheme `S₀` such that `G` (resp. `h`) arises by base change from an adjoint `S₀`-reductive group `G₀`
(resp. a sub-`O_S`-module locally a direct factor `h₀` of `g₀ = Lie(G₀/S₀)`). It suffices to show that there exists a
subscheme `Σ₀` of `S₀` with the required properties (because one will then have `Σ = Σ₀ ×_{S₀} S`). Replacing `S` by
`S₀`, one may therefore suppose `S` affine and noetherian (note that then every subscheme of `S` is of finite
presentation over `S`). Finally, replacing `S` by a sufficiently small open set, one may suppose that `g` is free of
rank `n` and that `h` is a direct factor, free of rank `r`.

One must first write that `h_{S′}` is a Lie subalgebra of `g_{S′}`, i.e. that the morphism induced by the Lie bracket:

```text
φ : h ⊗ h --[,]--> g
```

factors through `h`. If `(e₁, …, e_n)` is a basis of `g` such that `(e₁, …, e_r)` is a basis of `h`, then `φ` is given
by sections `a^{ij}_k` of `O_S` (where `i, j = 1, …, r` and `k = 1, …, n`), and the preceding condition is equivalent to
saying that `S′ → S` factors through the closed subscheme of `S` defined by the equations `a^{ij}_k = 0` for
`k = r + 1, …, n` and `i, j = 1, …, r`. Replace `S` by this closed subscheme.

Then, by 5.3.0, `N = Norm_G(h)` is a closed group subscheme of `G` of finite presentation over `G`. One must now write
(cf. 5.3.1) that `N_{S′}` is smooth at every point of the unit section, of relative dimension `r = rank(h)`, and that
the inclusion of `h_{S′}` in `Lie(N_{S′}/S′)` is an equality.

[^N.D.E-XXII-51] Since `N` is affine over `S` (being closed in `G`), the unit section `ε : S → N` is a closed immersion,
so `ε(S)` is defined by a quasi-coherent ideal `J` of `A(N)`. Note that `n_{S/N} = J/J²` is identified with
`ε*(Ω¹_{N/S})`, so its formation commutes with every base change `S′ → S`. By the equivalence (c′) ⇔ (a) in EGA IV₄,
17.12.1 (applied to `f : N → S` and `j = ε`), `N_{S′} → S′` is smooth, of relative dimension `r`, at every point of
`ε(S′)` if and only if `n_{S′/N′} = n_{S/N} ⊗_{O_S} O_{S′}` is locally free of rank `r` and the morphism
`φ_n(S′) : Sym^n(n_{S′/N′}) → J^n_{S′}/J^{n+1}_{S′}` is an isomorphism for every `n ⩾ 1`. Denote
`K_n(S′) = Ker φ_n(S′)`. By TDTE I, Lemma 3.6, `n_{S/N} ⊗_{O_S} O_{S′}` is locally free of rank `r` if and only if
`S′ → S` factors through some subscheme `Z` of `S`. Replacing `S` by `Z`, we may therefore suppose that `n_{S/N} = J/J²`
is locally free of rank `r`. Then, for every `S′ → S`, one has `(J²/J³) ⊗_{O_S} O_{S′} = J²_{S′}/J³_{S′}` and hence
`K₂(S′) = K₂(S) ⊗_{O_S} O_{S′}`. It follows that `φ₂(S′)` is an isomorphism if and only if `S′ → S` factors through the
closed subscheme `S₂` of `S` defined by the ideal generated by the image of `Sym²(n_{S/N})* ⊗ K₂(S)` in `O_S`. Then,
over `S₂`, `J²/J³` is isomorphic to `Sym²(n_{S/N})`, hence locally free, and the same argument shows that `φ₃(S′)` is an
isomorphism if and only if `S′ → S` factors through some closed subscheme `S₃` of `S`, etc. One obtains thus that
`N_{S′} → S′` is smooth, of relative dimension `r`, at every point of `ε(S′)` if and only if `S′ → S` factors through
the closed subscheme `Z` intersection of the `S_n`. But then, for every `S′ → Z`, `Lie(N_{S′}/S′)` is locally a direct
factor of rank `r` of `g_{S′}`, and so the inclusion `h_{S′} ⊂ Lie(N_{S′}/S′)` is an equality. One then sets `H = N⁰`.

Replacing `S` by `Z`, it remains only to express that `H_{s′}` is of the same reductive rank as `G_{s′}` at every point
`s′ ∈ S′`, or, equivalently, that `H_s` is of the same reductive rank as `G_s` at every point `s` of the (set-theoretic)
image of `S′` in `S`. Now this condition defines an open subset of `S` (Exp. XIX 6.2).

**Remark.** *In general, the scheme `H` is not smooth over `S`. It is however smooth if `6` is invertible on `S`, or if
there exists a prime number `p` such that `p · 1_S = 0` (i.e. if `S` is of characteristic `p > 0`).*

**Corollary 5.8.2.** *Let `S` be a scheme, `G` an `S`-reductive group, `H` a subgroup of type (R) of `G`. (Recall
(5.3.10) that `Norm_G(H)` is representable by a closed group subscheme of `G`, smooth over `S`.)*

<!-- label: III.XXII.5.8.2 -->

*Then the quotient sheaf `G/Norm_G(H)` is representable by a quasi-projective `S`-scheme, smooth and of finite
presentation over `S` (which is in fact an open subset of `H`).*

Indeed, consider the morphism

```text
f : G → H,
```

defined set-theoretically by `f(g) = int(g) H`. By 5.3.9, this morphism is smooth and of finite presentation, hence
open. Let `V = f(G)` equipped with its structure of open subscheme of `H`. The morphism `f : G → V` is covering and of
kernel `Norm_G(H)`, which proves that `G/Norm_G(H)` is representable by `V` (cf. Exp. IV 4.6.5).

**Corollary 5.8.3.** *Let `S` be a scheme, `G` an `S`-reductive group. Consider the functors `Tor(G)`, `Bor(G)`,
`Kil(G)` defined by*

<!-- label: III.XXII.5.8.3 -->

```text
Tor(G)(S′) = {maximal tori of G_{S′}},
Bor(G)(S′) = {Borel subgroups of G_{S′}},
Kil(G)(S′) = {Killing couples of G_{S′} (cf. 5.3.13)}.
```

*(i) `Tor(G)`, `Bor(G)`, `Kil(G)` are representable by smooth `S`-schemes of finite presentation, with integral
geometric fibers, and respectively affine, projective, affine over `S`.*

*(ii) The canonical morphism `Kil(G) → Tor(G)` (resp. `Kil(G) → Bor(G)`) is finite étale surjective (resp. affine smooth
surjective).*

*(iii) Let `T` be a maximal torus of `G` (resp. `B` a Borel subgroup of `G`, resp. `B ⊃ T` a Killing couple of `G`). The
morphism*

```text
G → Tor(G),    resp. G → Bor(G),    resp. G → Kil(G)
```

*defined by*

```text
g ↦ int(g) T,    resp. g ↦ int(g) B,    resp. g ↦ (int(g) B, int(g) T)
```

*induces an isomorphism*

```text
G/Norm_G(T) ⥲ Tor(G),    resp. G/B ⥲ Bor(G),    resp. G/T ⥲ Kil(G).
```

One sees first that (iii) follows from the conjugacy theorem for maximal tori (resp. Borel subgroups, resp. Killing
couples) and the fact that

```text
Norm_G(B) = B,    Norm_G(B) ∩ Norm_G(T) = T,
```

all results previously established (5.1.2, 5.3.12, 5.3.14, 5.6.1).

It follows first that the canonical morphisms

```text
Tor(G) → H,    Bor(G) → H
```

are representable, locally for the étale topology, by open immersions (5.8.2 and 5.1.2, resp. 5.5.5), hence by descent
that `Tor(G)` and `Bor(G)` are representable by open subsets of `H`. Similarly `Kil(G)` is locally (for the étale
topology) representable by a scheme affine over the base (Exp. IX 2.3), hence representable by an affine `S`-scheme, by
descent of affine schemes.[^N.D.E-XXII-52]

The assertions of (ii) follow immediately from 5.5.5 (ii) and 5.6.13. It already follows that `Tor(G)` is affine over
`S` (EGA II 6.7.1). It thus remains only to prove the fact that `Bor(G)` is projective over `S`. We already know that it
is quasi-projective; it remains to prove that it is proper;[^N.D.E-XXII-53] but it has connected fibers, so by EGA IV₃,
15.7.10, one is reduced to proving it on geometric fibers; if `S` is the spectrum of an algebraically closed field, one
has `Bor(G) = G/B` by (iii) and one concludes by Bible, § 6.4, th. 4 (or [Ch05], § 6.5, th. 5).

**Remark 5.8.4.** *Under the conditions of 5.8.3, let `Q` be a central subgroup of multiplicative type of `G`. The
obvious morphisms define isomorphisms*

<!-- label: III.XXII.5.8.4 -->

```text
Tor(G) ≃ Tor(G/Q),    Bor(G) ≃ Bor(G/Q),    Kil(G) ≃ Kil(G/Q).
```

**Corollary 5.8.5.** *Let `S` be a scheme, `G` an `S`-reductive group, `P` a group subscheme of `G`, smooth and of
finite presentation over `S`. The following conditions are equivalent:*

<!-- label: III.XXII.5.8.5 -->

*(i) For each `s ∈ S`, `P_s` is a parabolic subgroup of `G_s` (i.e. the quotient scheme `G_s/P_s` is proper over `s`, or
equivalently `P_s` contains a Borel subgroup of `G_s`, cf. Bible, § 6.4, th. 4 or [Ch05], § 6.5, th. 5).*

*(ii) The quotient sheaf `G/P` is representable by an `S`-scheme that is smooth and projective over `S`.*

*Moreover, under these conditions, `P` is closed in `G`, with connected fibers, and one has `P = Norm_G(P)`.*

One obviously has (ii) ⇒ (i). If (i) holds, then `P(s) = Norm_{G(s)}(P_s)` and `P_s` is connected (for the first point,
cf. Bible, § 12.3, lemme 4;[^N.D.E-XXII-54] the second point follows from this, because `P′ = P^0_s` is a parabolic
subgroup of `G_s` normalized by `P_s`, whence `P′(s) = P(s)` and thus `P′ = P_s`); it follows that `P` is of type (R),
and that `P` equals `Norm_G(P)`, hence is closed in `G`. By 5.8.2, `G/P = G/Norm_G(P)` is representable by a
quasi-projective `S`-scheme. Its fibers are connected and proper, hence it is projective by the reasoning of 5.8.3.

**Remark 5.8.6.** *The statements 5.8.1, 5.8.2, 5.8.5 are valid for an `S`-group of type (RA), or for an `S`-group of
type (RR) satisfying 5.1.8.*[^N.D.E-XXII-55]

<!-- label: III.XXII.5.8.6 -->

**Remark 5.8.7.** *Through the inner automorphisms of `G`, one has canonical operations:*

<!-- label: III.XXII.5.8.7 -->

```text
G → Aut_S(Tor(G)),    G → Aut_S(Bor(G)),    G → Aut_S(Kil(G)),
```

*which, in the situation of 5.8.3 (iii), are identified with the canonical operations*

```text
G → Aut_S(G/Norm_G(T)),    G → Aut_S(G/B),    G → Aut_S(G/T).
```

*One concludes in particular that*

```text
Ker(G → Aut_S(Tor(G))) = Ker(G → Aut_S(Bor(G))) = Ker(G → Aut_S(Kil(G))) = Centr(G).
```

It is indeed clear that `Centr(G)` operates trivially on each of the three schemes. Conversely, the kernel of
`G → Aut_S(Kil(G))` is "the intersection of the maximal tori of `G`" in the sense of 4.1.7, hence equals `Centr(G)`
(loc. cit.). For `Bor(G)`, one notes that "the intersection of the Borel subgroups of `G`" is also "the intersection of
its maximal tori" (see the following section). For `Tor(G)`, one uses Exp. XII 4.11.

### 5.9. Properties peculiar to Borel subgroups

<!-- label: III.XXII.5.9 -->

Most of these properties will be generalized in Exp. XXVI to parabolic subgroups.

**Definition 5.9.1.** *Let `S` be a scheme, `G` an `S`-reductive group, `B` and `B′` two Borel subgroups of `G`. We say
that `B` and `B′` are in* general position *(or that `B′` is in general position relative to `B`) if `B ∩ B′` is a torus
(necessarily maximal) of `G`.*

<!-- label: III.XXII.5.9.1 -->

*If `T` is a maximal torus of `G` contained in `B` and `B′`, we say that `B` and `B′` are* opposite *(relative to `T`)
if `B ∩ B′ = T`.*

**Proposition 5.9.2.** *Let `S` be a scheme, `G` an `S`-reductive group, `B` a Borel subgroup of `G`, `T` a maximal
torus of `B`. There exists a unique Borel subgroup `B′` of `G`, opposite to `B` relative to `T`.*

<!-- label: III.XXII.5.9.2 -->

*If `(G, T, M, R)` is a splitting of `G` relative to `T` and if `B = B_{R+}` (5.5.1), then `B′ = B_{−R+}`.*

By faithfully flat descent, it suffices to prove the proposition in the split case, when `B = B_{R+}` (5.5.5 (iv)). Then
`B_{−R+}` is indeed opposite to `B` (4.1.2); let us show that it is the only Borel subgroup of `G` containing `T` that
is opposite to `B`. If `B′` is a Borel subgroup of `G` containing `T`, then `B′` is locally on `S` of the form
`B_{R′+}`, where `R′+` is another system of positive roots of `R` (5.5.5 (iii)). If `R′+ ≠ −R+`, there exists
`α ∈ R′+ ∩ R+`, so that `Uα ⊂ B_{R+} ∩ B_{R′+}`.

**Proposition 5.9.3.** *Let `S` be a scheme, `G` an `S`-reductive group, `B` a Borel subgroup of `G`.*

<!-- label: III.XXII.5.9.3 -->

*(i) If `B′` is a Borel subgroup of `G`, the following conditions are equivalent:*

*(a) `B′` is in general position relative to `B` (5.9.1).*

*(b) `B′u ∩ B^u = e`.*

*(b′) `B′u ∩ B = e`.*

*(c) The product in `G` induces an open immersion `B′u ×_S B → G`.*

*(c′) The canonical morphism `B′u → G/B` is an open immersion.*

*(ii) The functor `Opp(B)`:*

```text
S′ ↦ {Borel subgroups of G_{S′} in general position relative to B_{S′}}
```

*is representable by an open subscheme of `Bor(G)` (5.8.3). The morphism*

```text
Opp(B) → Tor(B)
```

*defined by `B′ ↦ B ∩ B′` is an isomorphism. In particular (5.6.13) the inner automorphisms of `B^u` equip `Opp(B)` with
a structure of principal homogeneous bundle under `B^u`.*

Let us first examine (i). One has (a) ⇒ (c): indeed, (c) is local for the étale topology; by 5.5.5 (iv), one reduces to
the case where `G` is split relative to `B ∩ B′` and `B` of the form `B_{R+}`; by 5.9.2, one then has `B′u = U_{−R+}`
and one is reduced to 4.1.2.

One trivially has (c′) ⇔ (c) ⇒ (b′) ⇒ (b). It therefore remains to prove (b) ⇒ (a). Let us first prove (ii): the second
assertion is a formal consequence of 5.9.2, the third follows immediately from this by 5.6.13; let us prove the first;
it is local for the étale topology and one may therefore suppose that `B` possesses a maximal torus `T`; let `B′_0` be
opposite to `B` relative to `T` (5.9.2).

By what precedes, the morphism `B^u → Bor(G)` induced by the canonical morphism `G → G/B′_0 → Bor(G)` (5.8.3) induces an
isomorphism `B^u ⥲ Opp(B)`. One thus has a commutative diagram

```text
B^u    ────→  G/B′_0
 ≀              ≀
 ↓              ↓
Opp(B) ────→  Bor(G).
```

Now the morphism `B^u → G/B′_0` is an open immersion (by (i) (a) ⇒ (c′)), which finishes the proof of (ii). Let us
immediately note the corollary:

**Corollary 5.9.4.** *Let `G` be an `S`-reductive group and `B` and `B′` two Borel subgroups of `G`. If `s ∈ S` is such
that `B_s` and `B′_s` are in general position, there exists an open subset `V` of `S` containing `s` such that `B_V` and
`B′_V` are in general position.*

<!-- label: III.XXII.5.9.4 -->

It only remains to prove (b) ⇒ (a). By virtue of the preceding corollary, it suffices to do so when `S` is the spectrum
of an algebraically closed field `k`. One may suppose `G` split relative to a maximal torus `T` of `B`. Let `B′_0` be
the Borel subgroup opposite to `B`. Since the Borel subgroups of `G` are conjugate under `G(k)`, there exists `g ∈ G(k)`
such that `int(g) B′_0 = B′`. By Bruhat's theorem (5.7.4), one may write `g = b n b′`, with `b ∈ B(k)`, `b′ ∈ B′_0(k)`,
`n ∈ Norm_G(T)(k)`. One thus has

```text
B′ = int(b) int(n) B′_0
```

and `B′ ∩ B = int(b) (int(n) B′_0 ∩ B)`. If `n ∉ T(k)`, `int(n) B′u_0 ∩ B^u ≠ e` (cf. proof of 5.9.2); it follows that
(b) entails `B′ ∩ B = int(b)(B′_0 ∩ B) = int(b) T`. QED.

**Proposition 5.9.5.** *Let `S` be a scheme, `G` an `S`-reductive group, `B` a Borel subgroup of `G`, `B^u` its
unipotent part. There exists a sequence of subgroups of `B`:*

<!-- label: III.XXII.5.9.5 -->

```text
U₀ = B^u ⊃ U₁ ⊃ ⋯ ⊃ U_n ⊃ ⋯
```

*possessing the following properties:*

*(i) Each `U_i` is smooth, with connected fibers, characteristic in `B`; the inner automorphisms of `B^u` act trivially
on the (sheaf) quotients `U_i/U_{i+1}`.*

*(ii) For each `i ⩾ 0`, there exists a locally free `O_S`-module `E_i` and an isomorphism of `S`-sheaves of groups*

```text
U_i/U_{i+1} ⥲ W(E_i).
```

*(iii) For every `s ∈ S`, `(U_n)_s = e` for `n ⩾ dim(B^u_s)`.*

Suppose first that there exists a splitting `(G, T, M, R)` of `G` and a system of positive roots `R+` of `R` such that
`B = B_{R+}`. We denote by `Δ` the set of simple roots of `R+`; for each `α ∈ R+`, we write `ord(α)` for the sum of the
coefficients of `α` in the basis `Δ` of `Γ₀(R)`; it is the *order* of `α` relative to `R+`. One has `ord(α) ⩽ Card(R+)`.
For every `i > 0`, let `R^{(i)}` be the set of roots of order `> i`; it is a closed set of positive roots, so one may
construct (5.6.5)

```text
U_i = U_{R^{(i)}}.
```

If `α ∈ R+` and `β ∈ R^{(i)}`, then `α + β ∈ R^{(i+1)}`. It follows, by 5.5.2, that each `U_i` is a normal subgroup of
`B` and that the inner automorphisms of `B^u` operate trivially on `U_i/U_{i+1}`. This group is moreover identified with

```text
∏_{ord(α) = i + 1} Uα
```

and is thus equipped with a vector-space structure.

If `B` is of the form `B_{R′}` for another splitting `(G, T′, M′, R′)` of `G`, let us show that the groups `U′_i`
constructed as above using the new splitting coincide with the `U_i` and that the vector-space structures on the
successive quotients also coincide. By 5.6.13, there exists `b ∈ B^u(S)` such that `T′ = int(b) T`; the assertion to be
proved is local on `S` and one may therefore suppose that the isomorphism `T ⥲ T′` induced by `int(b)` arises by duality
from an isomorphism of root data

```text
h : (M′, M′*, R′, R′*) ⥲ (M, M*, R, R*).
```

It is clear that the roots of `R′+` are the `α ∘ int(b) = h(α)`, `α ∈ R+`, and that the simple roots of `R′+` are the
`α ∘ int(b) = h(α)`, `α ∈ Δ`, hence `ord(h(α)) = ord(α)` for `α ∈ R+`. On the other hand, it is clear by transport of
structure that the vector groups `U′_{h(α)}` are none other than the `int(b) Uα`. One thus has `int(b) U_i = U′_i`; but
`U_i` being invariant, this gives `U_i = U′_i`.

Similarly the isomorphism of vector groups

```text
int(b) : U_i/U_{i+1} ⥲ U′_i/U′_{i+1}
```

is the identity, by virtue of what has already been proved.

Let us now treat the general case. There exists a covering family for the étale topology `{S_i → S}` and for each `i` a
splitting `(G_i, T_i, M_i, R_i)` and a system of positive roots `R_{i+}` of `R_i` such that `B ×_S S_i = B_{R_{i+}}`
(5.5.5, (iii)). For each `i`, one thus has a family

```text
B_{S_i} = U_{i,0} ⊃ U_{i,1} ⊃ ⋯ ⊃ U_{i,j} ⊃ ⋯
```

and vector-space structures on the `U_{i,j}/U_{i,j+1}`. By descent, it suffices to prove that for every pair `(i, i′)`
and every `j`, one has

```text
U_{i,j} ×_{S_i} S_{ii′} = U_{i′,j} ×_{S_{i′}} S_{ii′}
```

(one writes `S_{ii′} = S_i ×_S S_{i′}`) and that the vector-space structures on the quotients

```text
(U_{i,j}/U_{i,j+1}) ×_{S_i} S_{ii′}    and    (U_{i′,j}/U_{i′,j+1}) ×_{S_i} S_{ii′}
```

coincide. Now if `S_{ii′} = ∅`, this is trivial; if `S_{ii′} ≠ ∅`, then one is in the situation studied above:
`B ×_S S_{ii′}` is defined by the system of positive roots `R_{i+}` (resp. `R_{i′+}`) in the splitting
`(G_{S_{ii′}}, T_i ×_{S_i} S_{ii′}, M_i, R_i)` (resp. in the splitting
`(G_{S_{ii′}}, T_{i′} ×_{S_{i′}} S_{ii′}, M_{i′}, R_{i′})`).

**Corollary 5.9.6.** *If `S` is affine, `H¹(S, B^u) = e`, i.e. every principal bundle under `B^u` possesses a section.*

<!-- label: III.XXII.5.9.6 -->

Indeed, `S` decomposes as a direct sum of subschemes on each of which `B^u` is of constant relative dimension. One may
therefore, by 5.9.5 (iii), suppose that there exists an `n` such that `U_n = e`. Since, by TDTE I,
B.1.1,[^N.D.E-XXII-56]

```text
H¹(S, U_i/U_{i+1}) = H¹(S, W(E_i)) = 0,
```

one has `H¹(S, B^u) = 0`.

**Corollary 5.9.7.** *If `S` is affine, `B` possesses maximal tori. If `T` is a maximal torus of `B`, one has
`H¹(S, T) = H¹(S, B)`.*

<!-- label: III.XXII.5.9.7 -->

The first assertion follows immediately from 5.9.6 and 5.6.13; the second follows in standard fashion.[^N.D.E-XXII-57]

**Corollary 5.9.8.** *If `G` is an `S`-reductive group, the canonical morphism (cf. 5.8.3)*

<!-- label: III.XXII.5.9.8 -->

```text
Kil(G) → Bor(G)
```

*possesses sections over every affine open subset.*

**Corollary 5.9.9.** *Under the conditions of 5.9.5, suppose `S` affine; then there exists a locally free `O_S`-module
`E` such that `B^u` is, as a scheme, `S`-isomorphic to `W(E)`.*

<!-- label: III.XXII.5.9.9 -->

Let us show by induction on `i` that `B^u/U_i` is `S`-isomorphic to `W(E₀ ⊕ ⋯ ⊕ E_{i−1})`. This is clear for `i = 0`;
suppose `i ⩾ 1`. Then `B^u/U_i` is a principal homogeneous bundle of base `X = B^u/U_{i−1}` under the group
`(U_{i−1}/U_i)_X`. Since `B^u/U_{i−1}` is affine, by the induction hypothesis, and since `U_{i−1}/U_i = W(E_{i−1})`,
this bundle is trivial. One thus has (at least) an isomorphism of `S`-schemes

```text
B^u/U_i ⥲ (B^u/U_{i−1}) ×_S W(E_{i−1}) = W(E₀ ⊕ ⋯ ⊕ E_{i−1}).
```

One concludes immediately by condition (iii) of 5.9.5.

**Corollary 5.9.10.** *Let `S` be a semi-local scheme, `{s_i}` its closed points, `B` a Borel subgroup of the
`S`-reductive group `G`. The canonical map*

<!-- label: III.XXII.5.9.10 -->

```text
B^u(S) → ∏_i B^u(Spec κ(s_i))
```

*is surjective.*

Indeed, if `S = Spec(A)`, `κ(s_i) = A/p_i` and if `E` is given by the `A`-module `E`, one has

```text
B^u(S) = E ⊗ A,    B^u(Spec κ(s_i)) = E ⊗_A (A/p_i).
```

The assertion then follows immediately from the fact that `A → ∏_i A/p_i` is surjective.

### 5.10. Subgroups of type (R) with reductive fibers

<!-- label: III.XXII.5.10 -->

**Proposition 5.10.1.** *Let `(G, T, M, R)` be an `S`-split group, `R′` a subset of `R` of type (R) (5.4.2), `H_{R′}`
the corresponding subgroup of `G`. The following conditions are equivalent:*

<!-- label: III.XXII.5.10.1 -->

*(i) `H_{R′}` is reductive (i.e. has reductive geometric fibers).*

*(ii) One has `R′ = −R′`, i.e. `R′` is symmetric.*

*Moreover, under these conditions, `(H_{R′}, T, M, R′)` is a splitting of `H_{R′}`; for every system of positive roots
`R+` of `R`, `R′+ = R′ ∩ R+` is a system of positive roots of `R′` and*

```text
B_{R+} ∩ H_{R′} = H_{R′+}
```

*is a Borel subgroup of `H_{R′}`, whose unipotent part is*

```text
U_{R+} ∩ H_{R′} = U_{R′+}.
```

One has obviously (i) ⇒ (ii) (it suffices to check it fiber by fiber and `R′` is a system of roots of `H_{R′}` relative
to `T`). To prove (ii) ⇒ (i), one remarks by 5.4.3 that

```text
H_{R′} ∩ Zα = Centr_{H_{R′}}(Tα) = Zα
```

for every `α ∈ R′` and one applies the criterion of Exp. XIX 1.12.

If `R+` is a system of positive roots of `R`, then `R′+ = R+ ∩ R′` is obviously a closed subset of `R′` such that
`R′+ ∪ −R′+ = R′` and `R′+ ∩ −R′+ = ∅`, hence a system of positive roots of `R′`. The other two assertions follow
respectively from 5.6.1 (vi) and 5.6.7 (i).

**Corollary 5.10.2.** *Let `S` be a scheme, `G` an `S`-reductive group, `H` an `S`-reductive subgroup such that for
every `s ∈ S`, `G_s` and `H_s` have the same reductive rank. Then `H` is closed in `G`, `Norm_G(H)` is smooth over `S`,
`Norm_G(H)/H` is representable by a finite étale `S`-scheme.*

<!-- label: III.XXII.5.10.2 -->

*If `T` is a maximal torus of `H` and `B` a Borel subgroup of `G` containing `T`, then `B ∩ H` is a Borel subgroup of
`H`, whose unipotent part is `(B ∩ H)_u = B^u ∩ H`.*

The first assertions follow immediately from 5.3.10 and 5.3.18, via the fact that the Weyl groups of `G` and `H` are
finite (Exp. XIX 2.5). The other assertions are local for the étale topology and reduce to the case studied in 5.10.1.

**Proposition 5.10.3.** *Let `S` be a scheme, `G` an `S`-reductive group.*

<!-- label: III.XXII.5.10.3 -->

*(a) If `Q` is a torus of `G`, `Centr_G(Q)` is a subgroup of type (R) of `G` with reductive fibers. If `Q ⊂ Q′` are two
tori of `G`, then `Centr_G(Q) ⊃ Centr_G(Q′)`.*

*(b) If `H` is a subgroup of type (R) of `G` with reductive fibers, then `rad(H)` (4.3.6) is a torus of `G`. If `H ⊂ H′`
are two subgroups of type (R) of `G` with reductive fibers, then `rad(H) ⊃ rad(H′)`.*

*(c) If `Q` is a torus of `G`, one has*

```text
rad(Centr_G(Q)) ⊃ Q    and    Centr_G(rad(Centr_G(Q))) = Centr_G(Q).
```

*(d) If `H` is a subgroup of type (R) of `G` with reductive fibers, one has*

```text
Centr_G(rad(H)) ⊃ H    and    rad(Centr_G(rad(H))) = rad(H).
```

Indeed, (a) follows immediately from Exp. XIX 2.8. To prove (b), it suffices to note that `rad(H′) ⊂ H`, because `H`
contains (locally for (fpqc)) a maximal torus of `G`, hence of `H′`. The first assertion of (c) (resp. (d)) is trivial,
the second follows by the usual reasoning.

This proposition leads to the following definition:

**Definition 5.10.4.** *Let `S` be a scheme, `G` an `S`-reductive group, `H` a reductive subgroup of type (R) of `G`,
and `Q` a subtorus of `G`.*[^N.D.E-XXII-58]

<!-- label: III.XXII.5.10.4 -->

*1) We say that `H` is a* critical subgroup *if it is the centralizer of its radical.*

*2) We say that `Q` is a* C-critical torus *if it is the radical of its centralizer.*

It then follows from Proposition 5.10.3:

**Corollary 5.10.5.** *(i) For every subtorus `Q` of `G`, `Centr_G(Q)` is critical.*

<!-- label: III.XXII.5.10.5 -->

*(ii) For every subgroup of type (R) with reductive fibers `H` of `G`, `rad(H)` is a C-critical torus of `G`.*

*(iii) The maps*

```text
Q ↦ Centr_G(Q),    H ↦ rad(H)
```

*are mutually inverse bijections between the set of C-critical tori of `G` and the set of its critical reductive
subgroups of type (R).*

*(iv) If `Q` is a torus of `G`, `rad(Centr_G(Q))` is the smallest C-critical torus of `G` containing `Q`.*

*(v) If `H` is a reductive subgroup of type (R) of `G`, `Centr_G(rad(H))` is the smallest critical reductive subgroup of
type (R) of `G` containing `H`.*

**Remark 5.10.5.1.**[^N.D.E-XXII-58] *(1) A torus `T` of `G` is a critical subgroup of `G` if and only if it is a
maximal torus.*

<!-- label: III.XXII.5.10.5.1 -->

*(2) In what follows, "critical torus" means "C-critical torus".*

**Proposition 5.10.6.** *Let `(G, T, M, R)` be an `S`-split group, `R′` a subset of `R`. The following conditions are
equivalent:*

<!-- label: III.XXII.5.10.6 -->

*(i) `R′` is of type (R), `H_{R′}` is reductive and critical.*

*(ii) There exists a system of simple roots `Δ` of `R` and a subset `Δ′` of `Δ` such that `R′` is the set of elements of
`R` that are linear combinations of elements of `Δ′`.*

*(iii) `R′` is closed, symmetric, and every system of simple roots of `R′` is the intersection with `R′` of a system of
simple roots of `R`.*

Indeed, by Exp. XXI 3.4.8, (ii) and (iii) are equivalent and are also equivalent to the fact that `R′` is the
intersection of `R` with a `ℚ`-subspace of `M ⊗ ℚ`. Now this last condition is entailed by (i): if
`H_{R′} = Centr_G(Q)`, then `R′` is the set of elements of `R` that vanish on `Q` (Exp. II 5.2.3 (ii)). Finally, this
condition entails (i), because `rad(H_{R′})` is the maximal torus of `⋂_{α ∈ R′} Ker(α)`, hence `Centr_G(rad(H_{R′}))`
is none other than `H_{R′′}` where `R′′` is the intersection of `R` with the subspace generated by `R′`.

#### 5.10.7.

<!-- label: III.XXII.5.10.7 -->

Let us summarize some of the preceding results: let `(G, T, M, R)` be an `S`-split group, and let `Δ` be a system of
simple roots of `R` and `R+` the corresponding system of positive roots; choose a subset `Δ′` of `Δ`, denote `R′` the
set of elements of `R` that are linear combinations of elements of `Δ′` and set `R′+ = R′ ∩ R+`. Let `T_{Δ′}` be the
maximal torus of `⋂_{α ∈ Δ′} Ker(α)` and `Z_{Δ′} = Centr_G(T_{Δ′})`.

Then `Z_{Δ′}` is a reductive subgroup of `G`, with radical `T_{Δ′}`; `(Z_{Δ′}, T, M, R′)` is an `S`-split group;
`B_{R+} ∩ Z_{Δ′}` is the Borel subgroup of `Z_{Δ′}` defined by the system of positive roots `R′+` (or by the system of
simple roots `Δ′`) and its unipotent part is `U_{R+} ∩ Z_{Δ′} = U_{R′+}`.

**Remark 5.10.8.** *Under the conditions of 5.10.4, let `Q` be a critical torus of `G`, `L = Centr_G(Q)` its
centralizer. Since `Q = rad(L)`, then `Q` is a characteristic subgroup of `L`; it follows immediately that*

<!-- label: III.XXII.5.10.8 -->

```text
Norm_G(L) = Norm_G(Q),
```

*hence also*

```text
Norm_G(L)/L = Norm_G(Q)/Centr_G(Q) = W_G(Q).
```

By 5.10.2, one deduces:

**Proposition 5.10.9.** *Let `S` be a scheme, `G` an `S`-reductive group, `Q` a critical torus of `G`. The Weyl group
`W_G(Q)` is (étale) finite over `S`.*

<!-- label: III.XXII.5.10.9 -->

**Remark 5.10.10.** *Under the conditions of 5.10.7, one may make explicit*

<!-- label: III.XXII.5.10.10 -->

```text
W_G(T_{Δ′}) = Norm_G(Z_{Δ′})/Z_{Δ′}.
```

*It is the constant group associated with the quotient `W₁/W₂`, where `W₁` is the subgroup of `W` formed by the elements
that normalize the subgroup of `M` generated by `Δ′`, and `W₂` is the subgroup of `W` generated by the `sα`, `α ∈ Δ′`.*

### 5.11. Subgroups of type (RC)

<!-- label: III.XXII.5.11 -->

**Definition 5.11.1.** *Let `S` be a scheme, `G` an `S`-reductive group. A group subscheme `H` of `G` is called* of type
(RC) *if it is of type (R), i.e. (5.2.1) satisfies the following two conditions:*

<!-- label: III.XXII.5.11.1 -->

*(i) `H` is smooth over `S`, with connected fibers;*

*(ii) for every `s ∈ S`, `H_s` contains a maximal torus of `G_s`;*

*and if it further satisfies the following condition:*

*(iii) for every `s ∈ S` and every maximal torus `T` of `H_s`, the set of roots of `H_s` relative to `T` is a closed
subset of the set of all roots of `G_s` relative to `T`.*

**Remark 5.11.2.** *As we have already noted in 5.4.8, condition (iii) is a consequence of the others when `6` is
invertible on `S`.*[^N.D.E-XXII-59]

<!-- label: III.XXII.5.11.2 -->

**Lemma 5.11.3.** *Let `(G, T, M, R)` be an `S`-split group and `R′` a closed subset of `R`. Let*

<!-- label: III.XXII.5.11.3 -->

```text
R₁ = {α ∈ R′ | −α ∈ R′}    and    R₂ = {α ∈ R′ | −α ∉ R′}.
```

*Then `R₁` and `R₂` are closed. Consider the groups `H_{R′}`, `H_{R₁}` and `U_{R₂}` (5.4.7 and 5.6.5), which are smooth
with connected fibers.*

*(i) The group `U_{R₂}` is normal in `H_{R′}` and `H_{R′}` is the semi-direct product of `U_{R₂}` by `H_{R₁}`.*

*(ii) `H_{R₁}` is reductive, `U_{R₂}` has connected and unipotent geometric fibers; every normal subgroup of `H_{R′}`,
smooth over `S` and with connected and unipotent geometric fibers, is contained in `U_{R₂}`, and every reductive
subgroup of `H_{R′}` containing `T` is contained in `H_{R₁}`.*

*(iii) One has `U_{R₂} ∩ Norm_G(H_{R₁}) = e`.*

One first has (iii) by 5.6.7 (i). The first assertion of (i) follows from 5.6.7 (ii). Since `U_{R₂} ∩ H_{R₁} = e` by
(iii), the semi-direct product `H_{R₁} · U_{R₂}` is a subgroup of `H_{R′}`; but these are two subgroups of type (R) of
`G`, containing `T`, and they have the same Lie algebra `g_{R′}`; they thus coincide by 5.3.5, finishing the proof of
(i).

Let us now prove (ii); the first two assertions are simply 5.10.1 and 5.6.5. Let `U` be a group subscheme of `H_{R′}`,
smooth and of finite presentation, normal (hence normalized by `T`), with connected and unipotent geometric fibers; by
5.6.12, one has, locally on `S`, `U = U_{R′′}`, where `R′′` is a subset of `R′` such that `R′′ ∩ −R′′ = ∅`. If
`U ⊄ U_{R₂}`, then `R′′ ⊄ R₂`, so there exists `α ∈ R′′` such that `−α ∈ R′`. Then `Zα ⊂ H_{R′}` (5.4.3), so `Zα`
normalizes `U`. But `U` contains `Uα` and `Zα` possesses a section `w` such that `int(w) Uα = U_{−α}`; this entails
`−α ∈ R′′`, contradicting the hypothesis `R′′ ∩ −R′′ = ∅`.

Finally, if `L` is a reductive subgroup of `H_{R′}` containing `T`, one has locally on `S`, `L = H_{R′′′}`, with `R′′′`
symmetric contained in `R′`, hence contained in `R₁`.

**Proposition 5.11.4.** *Let `S` be a scheme, `G` an `S`-reductive group, `H` a group subscheme of `G` of type (RC).*

<!-- label: III.XXII.5.11.4 -->

*(i) `H` is closed in `G`, `Norm_G(H)/H` is representable by a finite étale `S`-group scheme.*

*(ii) `H` possesses a largest normal group subscheme that is smooth and of finite presentation over `S`, with connected
and unipotent geometric fibers; we call it the* unipotent radical *of `H` and denote it `rad_u(H)`. The quotient sheaf
`H/rad_u(H)` is representable by an `S`-reductive group.*

*(iii) If `T` is a maximal torus of `H`, `H` possesses a reductive subgroup `L` containing `T` of type (RC) possessing
the two following properties:*

*(a) Every reductive subgroup of `H` containing `T` is contained in `L`.*

*(b) `H` is the semi-direct product `H = L · rad_u(H)`, i.e. the canonical morphism `L → H/rad_u(H)` is an isomorphism.*

*Furthermore, `L` is the unique reductive subgroup of `H` containing `T` and satisfying one or the other of the two
preceding conditions. Finally, one has the following equalities:*

```text
Norm_H(L) = L,    Norm_H(T) = Norm_L(T),    W_H(T) = W_L(T),
```

*in particular `W_H(T)` is finite over `S`.*

*Proof.* Let us first note that (i) is local for the étale topology. Therefore, by Corollary 5.3.18, (i) is a
consequence of the last assertion of (iii).

The assertions of (ii) are local for the étale topology. One may therefore suppose to be in the situation of 5.11.3,
where one concludes immediately by (i) and (ii).

By virtue of the uniqueness assertions contained in it, (iii) is also local for the étale topology and one may again
reduce to the situation of 5.11.3, where properties (a) and (b) have been verified. The uniqueness of an `L` satisfying
(a) is trivial; the uniqueness of an `L` satisfying (b) is obvious, given (a). The equality `Norm_H(L) = L` is none
other than 5.11.3 (iii); if a section of `H` normalizes `T`, then it normalizes `L`, by uniqueness of `L`, hence is a
section of `L` by what was just demonstrated, which proves the second equality; the third is then trivial.

**Proposition 5.11.5.** *Let `S` be a scheme, `G` an `S`-reductive group, `Hc` the functor of subgroups of type (RC) of
`G`, which is a subfunctor of the functor `H` of 5.8.1.*

<!-- label: III.XXII.5.11.5 -->

*(i) `Hc` is representable by an open subscheme of `H`, smooth, quasi-projective, and of finite presentation over `S`.*

*(ii) There exists a finite étale `S`-scheme `Cℓ_c` and a morphism*

```text
cℓ : Hc → Cℓ_c,
```

*smooth, quasi-projective, of finite presentation, surjective, with connected geometric fibers, possessing the following
property:*

*For every `S′ → S` and every `H, H′ ∈ Hc(S′)`, `cℓ(H) = cℓ(H′)` if and only if `H` and `H′` are conjugate in `G`
locally for the étale topology (or, equivalently by 5.3.11, if for every `s ∈ S`, `H_s` and `H′_s` are conjugate by an
element of `G(s)`).*

*(iii) `Cℓ_c` and `cℓ` are determined (up to unique isomorphism) by the preceding conditions.*

*(iv) If `(G, T, M, R)` is a splitting of `G`, let `E` be the set of conjugacy classes modulo `W` of closed subsets of
`R`; then there exists an isomorphism `Cℓ_c ⥲ E_S` such that, for every closed subset `R′` of `R`, `cℓ(H_{R′})`
corresponds to the canonical image of `R′` in `E_S(S) = Hom_{loc.const.}(S, E)`.*

It is first clear that `Hc` is a sheaf for the étale topology and that (ii) entails that `Cℓ_c` is none other than the
quotient sheaf of `Hc` by the equivalence relation defined by conjugation.

This entails first (iii), as well as the fact that it suffices to verify (i) and (ii) locally for the étale topology.
One thus reduces to the situation of (iv); let us first construct a morphism

```text
f : Hc → E_S.
```

It suffices to construct an application `Hc(S) → E_S(S)` functorial in `S`; so let `H` be a subgroup of type (RC) of
`G`; since `H` locally for the étale topology possesses maximal tori, and since the maximal tori of `G` are conjugate
locally for the étale topology, there exists a covering family `{S_i → S}` and for each `i` a `g_i ∈ G(S_i)` and a
closed subset `R_i` of `R` such that `int(g_i)(H ×_S S_i) = H_{R_i} ×_S S_i`; each `R_i` defines a section `η_i` of
`E_{S_i}`, i.e. an element of `E_S(S_i)`; it now suffices to prove that the family `(η_i)` arises from a section
`η = f(H)` of `E_S` over `S`, and that the latter depends only on `H`.

For this, one is reduced to proving that `H_{R′}` and `H_{R′′}` are conjugate locally for the étale topology if and only
if `R′` and `R′′` are conjugate by an element of the Weyl group `W`, which is trivial.

For every `η ∈ E`, there exists an `H₀ ∈ Hc(S)` such that `f(H₀) = η`: it suffices to take `H₀ = H_{R′}` where `R′` is a
closed subset of `R` whose image in `E` is `η`. If `H ∈ H₀(S′)`, `S′ → S`, `H` is conjugate to `H₀` locally for the
étale topology if and only if `f(H) = η` (as one sees immediately by the preceding argument), which shows that `f⁻¹(η)`
is identified with the quotient `G/Norm_G(H₀)`, which by 5.8.2 is an open subset of `H`, smooth, quasi-projective of
finite presentation over `S`, with connected and non-empty fibers. Since `E_S` is the sum of the open subschemes images
of the sections corresponding to the `η ∈ E`, `Hc` is identified with the sum of the `f⁻¹(η)`, `η ∈ E`, which proves (i)
and (ii). Finally, (iv) holds by construction.

**Corollary 5.11.6.** *If `u ∈ Cℓ_c(S′)`, `S′ → S`, `cℓ⁻¹(u)` is an `S′`-scheme that is smooth, quasi-projective, of
finite presentation, with non-empty connected fibers; it is an open subset of `Hc` and a "homogeneous" scheme under
`G_{S′}` (by inner automorphisms). In particular, if `H ∈ cℓ⁻¹(u)(S′)`, the morphism `G_{S′} → (Hc)_{S′}` defined by
`g ↦ int(g) H` identifies `G_{S′}/Norm_{G_{S′}}(H)` with `cℓ⁻¹(u)`.*

<!-- label: III.XXII.5.11.6 -->

**Examples 5.11.7.** *In particular, one has two canonical sections `u_t`, `u_b` of `Cℓ_c` corresponding respectively to
maximal tori (`R′ = ∅`) and to Borel subgroups (`R′ =` system of positive roots). The `S`-schemes `cℓ⁻¹(u_t)` and
`cℓ⁻¹(u_b)` are none other than the `S`-schemes `Tor(G)` and `Bor(G)` introduced in 5.8.3. We will see other examples in
Exp. XXVI.*

<!-- label: III.XXII.5.11.7 -->

**Remark 5.11.8.** *One may construct an `S`-scheme `Cℓ`, of finite presentation and unramified, and a morphism `H → Cℓ`
smooth and surjective, with connected geometric fibers, enjoying properties analogous to 5.11.5 (ii) and (iii).*

<!-- label: III.XXII.5.11.8 -->

## 6. The derived group

<!-- label: III.XXII.6 -->

### 6.1. Preliminaries

<!-- label: III.XXII.6.1 -->

In this section, we fix a scheme `S`, an `S`-split group `(G, T, M, R)`, a system of positive roots `R+` of `R`, and
write

```text
B = B_{R+},    B_- = B_{R−},    U = B^u,    U_- = (B_-)^u,
Ω = Ω_{R+} = U_- · T · U.
```

#### 6.1.1.

<!-- label: III.XXII.6.1.1 -->

We denote by `T′` the subtorus of `T` "image of the family `α*`, `α ∈ R`"; in other words, `T′` is the image of the
morphism of groups

```text
G^R_{m,S} → T
```

defined by `(z_α)_{α ∈ R} ↦ ∏_{α ∈ R} α*(z_α)`. One sees immediately that if `Δ` denotes the set of simple roots of
`R+`, the morphism

```text
G^Δ_{m,S} → T′
```

defined in the same way is surjective with finite kernel. If we identify `T` with `D_S(M)`, then `T′` is identified with
`D_S(M/N)`, where

```text
N = M ∩ V(R*)^⊥
```

(we denote by `V(R*)^⊥` the orthogonal of `V(R*)` in the duality between `V` and `V*`).

**Lemma 6.1.2.** *The morphism defined by the product in `T`*

<!-- label: III.XXII.6.1.2 -->

```text
rad(G) ×_S T′ → T
```

*is an isogeny (cf. 4.2.9).*

Indeed, the canonical morphism `rad(T) → T/T′` arises by duality from the morphism of commutative groups

```text
M ∩ V(R*)^⊥ → M/(M ∩ V(R)),
```

which one sees immediately to be injective with finite cokernel (cf. Exp. XXI 6.3).

**Definition 6.1.3.** *One writes `Ω′ = U_- · T′ · U`; it is a closed subscheme of `Ω = U_- · T · U`.*

<!-- label: III.XXII.6.1.3 -->

**Lemma 6.1.4.** *Let `α` be a simple root and `w_α ∈ Norm_G(T)(S)` lifting `s_α`. One has*

<!-- label: III.XXII.6.1.4 -->

```text
int(w_α) Ω′ ∩ Ω ⊂ Ω′.
```

It suffices for us to prove that if `g ∈ Ω′(S)` and `int(w_α) g ∈ Ω(S)`, then `int(w_α) g ∈ Ω′(S)`. By 5.6.8, write

```text
g = a · exp_{-α}(Y) · t · expα(X) · b,
```

with `a ∈ U_{-α̂}(S)`, `Y ∈ Γ(S, g^{-α})`, `t ∈ T′(S)`, `X ∈ Γ(S, g^α)`, `b ∈ U_{α̂}(S)`. One then has

```text
int(w_α) g = int(w_α) a · int(w_α)(exp_{-α}(Y) t expα(X)) · int(w_α) b.
```

By virtue of 5.6.8 (iv), one has

```text
int(w_α) a ∈ U_{-α̂}(S),    int(w_α) b ∈ U_{α̂}(S).
```

It follows that one has the following equivalences (setting `h = exp_{-α}(Y) t expα(X)`):

```text
int(w_α) g ∈ Ω(S)   ⇔   int(w_α) h ∈ Ω(S)
int(w_α) g ∈ Ω′(S)  ⇔   int(w_α) h ∈ Ω′(S).
```

One is therefore reduced to the case where `g = h`. Since one has (4.1.12)

```text
Zα ∩ Ω = U_{-α} · T · Uα,    Zα ∩ Ω′ = U_{-α} · T′ · Uα,
```

one is reduced to proving the following assertion:

```text
int(w_α) h ∈ (U_{-α} · T · Uα)(S)  ⇒  int(w_α) h ∈ (U_{-α} · T′ · Uα)(S).
```

Now this latter follows immediately from Exp. XX 3.12, which shows that the component on `T` of `int(w_α) h` is of the
form `t · α*(z) ∈ T′(S)`.

**Lemma 6.1.5.** *For every `w ∈ Norm_G(T)(S)`, there exists an open subset `V_w` of `G` containing the unit section,
such that*

<!-- label: III.XXII.6.1.5 -->

```text
int(w) Ω′ ∩ V_w ⊂ Ω′.
```

Choose, for each simple root `α`, an `n_α ∈ Norm_G(T)(S)` lifting `s_α`. For every point `s ∈ S`, there exist an open
subset `V` of `S` containing `s`, a `t ∈ T(V)` and over `V` a relation

```text
w = n_{α₁} ⋯ n_{α_p} t,    with the αᵢ simple.
```

One may obviously content oneself with making the demonstration for `V = S`; it is done by induction on `p`. If `p = 0`,
then `w ∈ T(S)` and one takes `V_w = G`; suppose therefore `w = n_α · w′`, `w′` satisfying the conclusion of the lemma;
there thus exists an open subset `V_{w′}` of `G`, containing the unit section, such that `int(w′) Ω′ ∩ V_{w′} ⊂ Ω′`. One
may then write

```text
int(w) Ω′ ∩ (int(n_α) V_{w′} ∩ Ω) = int(n_α)(int(w′) Ω′ ∩ V_{w′}) ∩ Ω
                                  ⊂ int(n_α) Ω′ ∩ Ω ⊂ Ω′,
```

by 6.1.4. One then takes `V_w = int(n_α) V_{w′} ∩ Ω` and we are done.

**Lemma 6.1.6.** *There exists an open subset `V₀` of `G`, containing the unit section, such that for every `S′ → S`,
one has*

<!-- label: III.XXII.6.1.6 -->

```text
U(S′) U_-(S′) ∩ V₀(S′) ⊂ Ω′(S′).
```

Let `n₀` be an element of `Norm_G(T)(S)` lifting the symmetry `w₀` of the Weyl group,[^N.D.E-XXII-60] that is, such that
`int(n₀) U = U_-` (cf. Exp. XXI 3.6.14); then `n₀² ∈ T(S)`. Let us show that the open set `V₀ = V_{n₀}` of 6.1.5 answers
the question. Indeed

```text
U(S′) U_-(S′) = int(n₀)(int(n₀)⁻¹ U(S′) · int(n₀)⁻¹ U_-(S′))
              = int(n₀)(U_-(S′) · U(S′)) ⊂ int(n₀) Ω′(S′).
```

Whence

```text
U(S′) U_-(S′) ∩ V₀(S′) ⊂ int(n₀) Ω′(S′) ∩ V₀(S′) ⊂ Ω′(S′).
```

**Lemma 6.1.7.** *Consider the morphism*

<!-- label: III.XXII.6.1.7 -->

```text
f : Ω = U_- · T · U → T/T′
```

*composite of the second projection and the canonical morphism of `T` into `T/T′`. Then `f` is "generically
multiplicative": there exists an open subset `V` of `Ω ×_S Ω`, containing the unit section (and hence relatively
schematically dense, Exp. XVIII 1.3) such that for every `S′ → S` and every `(x, y) ∈ V(S′)`, one has `xy ∈ Ω(S′)` and
`f(xy) = f(x) f(y)`.*

Let `x` and `y` be two sections of `Ω` over `S′`. Write

```text
x = u t v,    y = u′ t′ v′,    with u, u′ ∈ U_-(S′), t, t′ ∈ T(S′), v, v′ ∈ U(S′).
```

Let `V₀` be the open set of 6.1.6 and `V` the open subset of `Ω ×_S Ω` defined by "`v u′ ∈ V₀(S′)`" (it is the inverse
image of `V₀` by the morphism `Ω ×_S Ω` written set-theoretically `(x, y) ↦ v u′`). Then `V` answers the question.
Indeed, for `(x, y) ∈ V(S′)`, one has

```text
xy = (u t v)(u′ t′ v′) = (u t)(v u′)(t′ v′).
```

But `v u′ ∈ Ω′(S′)`, whence

```text
xy ∈ U_-(S′) · t · Ω′(S′) · t′ · U(S′) ⊂ U_-(S′) · tt′ T′(S′) · U(S′),
```

which shows that `xy ∈ Ω(S′)` and that

```text
f(xy) = f(tt′) = f(t) f(t′) = f(x) f(y).
```

**Proposition 6.1.8.** *There exists a morphism of groups*

<!-- label: III.XXII.6.1.8 -->

```text
f : G → T/T′
```

*inducing on `T` the canonical projection. The kernel `Ker(f)` of `f` is a closed group subscheme of `G` smooth over `S`
and with connected fibers. Every morphism of groups from `G` to a presheaf of commutative groups on `S`, separated for
(fppf), vanishes on `Ker(f)`.*

The first assertion follows immediately from 4.1.11. One has immediately `Ker(f) ∩ Ω = Ω′`, which proves that `Ker(f)`
is smooth over `S` at every point of the unit section.[^N.D.E-XXII-61] By 5.6.9 (ii), every morphism `φ` from `G` to a
presheaf of commutative groups separated for (fppf) vanishes on `U` and `U_-`. By Exp. XX 2.7, `φ` therefore vanishes
also on `T′`, hence on `Ω′`. Taking the notations of 5.7.10, one sees that the monoid `U₁` is contained in `Ker(f)(S)`,
which shows that

```text
Ker(f) = ⋃_{u ∈ U₁} u Ω′.
```

It follows on the one hand that every `φ` as above vanishes on `Ker(f)`, and on the other hand that `Ker(f)` has
connected fibers, hence is smooth over `S` by Exp. VI_B 3.10.

### 6.2. Derived group of a reductive group

<!-- label: III.XXII.6.2 -->

**Theorem 6.2.1.** *Let `S` be a scheme, `G` an `S`-reductive group.*

<!-- label: III.XXII.6.2.1 -->

*(i) `D_S(G) = Hom_{S-gr.}(G, Gm,S)` is representable by a twisted constant `S`-group, whose type at `s ∈ S` is
`ℤ^{rg_red(G_s) − rg_ss(G_s)}`.*

*(ii) Write `corad(G) = D_S(D_S(G))`, which is therefore an `S`-torus. The biduality morphism (cf. Exp. VIII § 1)*

```text
f₀ : G → corad(G)
```

*is smooth and surjective.*

*(iii) The composite morphism*

```text
rad(G) → G → corad(G)
```

*is an isogeny (cf. 4.2.9).*

*(iv) The kernel of `f₀`, denoted*

```text
dér(G) = Ker(f₀)
```

*is a closed group subscheme of `G`, semisimple over `S`, called the* derived group *of `G`. If `G` is semisimple, one
has `dér(G) = G`.*

*(v) Every morphism of groups from `G` to an `S`-presheaf of commutative groups, separated for (fppf), vanishes on
`dér(G)` and thus factors through `f₀`.*

*Proof.* All assertions of the theorem are local for the étale topology; one may thus reduce to the case where `G` is
split over `S`. Consider then the morphism `f` of 6.1.8. By the last assertion of 6.1.8, one immediately has an
isomorphism

```text
Hom_{S-gr.}(G, Gm,S) ⥲ Hom_{S-gr.}(T/T′, Gm,S),
```

which proves (i), then (ii) and gives a commutative diagram

```text
G ─────f₀──→ corad(G)
 ↘            ≀
   f         ↓
    ↘  →  T/T′.
```

One then has (v) by 6.1.8, and (iii) by 6.1.2. One also has `Ker(f) = Ker(f₀)`, which by 6.1.8 entails that `dér(G)` is
smooth over `S` and has connected fibers; it remains to verify that its fibers are semisimple; now they are reductive by
Exp. XIX 1.7, as invariant subgroups of reductive groups. By (iii), `rad(G) ∩ dér(G)` is finite, which indeed entails
that the fibers of `dér(G)` are semisimple.

**Remark 6.2.2.** *(a) By construction, in the case where `G` is split, `dér(G)` is the (fppf) subsheaf of `G` generated
by the `Uα`, `α ∈ R`. (It even suffices to take the `Uα`, `α ∈ Δ ∪ −Δ`, where `Δ` is a basis of `R`.)*

<!-- label: III.XXII.6.2.2 -->

*(b)*[^N.D.E-XXII-62] *Let `C` be the presheaf of commutators of `G`, i.e. the `S`-group functor that associates with
every `S′ → S` the group of commutators of `G(S′)` (i.e. the subgroup of `G(S′)` generated by the elements `xyx⁻¹y⁻¹`,
for `x, y ∈ G(S′)`), and let `C̃` be the associated (fppf) sheaf. Since the quotient `G/dér(G) = T/T′` is commutative,
then `dér(G)` contains `C` and hence `C̃` (cf. Exp. IV 4.3.12).*

*On the other hand, the quotient presheaf `G/C̃` is separated (Exp. IV 4.4.8.1), and therefore by (v) one has
`dér(G) ⊂ C̃`, whence `dér(G) = C̃`, i.e. `dér(G)` is the (fppf) sheaf of commutators of `G`.*

*Let us finally note that `C`, being a subpresheaf of `G`, is separated, but is not equal to `dér(G)` in general: for
example, `dér(SL₂) = SL₂` but `SL₂(F₂) ≃ S₃` is not equal to its derived group.*

*(c) When `S` is the spectrum of an algebraically closed field `k`, `dér(G)(k)` is the group of commutators of `G(k)`
(Exp. VI_B 7.10).*

#### 6.2.3.

<!-- label: III.XXII.6.2.3 -->

Consider now the two exact sequences

```text
1 → rad(G) → G → ss(G) → 1,
1 → dér(G) → G → corad(G) → 1.
```

Since `rad(G)` is central in `G`, the product in `G` defines a morphism of groups

```text
u : rad(G) ×_S dér(G) → G
```

which is covering by virtue of 6.2.1 (iii), hence surjective and flat (Exp. VI_B 9.2 (xi)).[^N.D.E-XXII-63] Its kernel
is isomorphic to `rad(G) ∩ dér(G)`, which is also the kernel of `rad(G) → corad(G)`, hence is a finite subgroup of
multiplicative type of `rad(G)`.

One reasons similarly for the morphism

```text
G → corad(G) ×_S ss(G),
```

whose kernel is `dér(G) ∩ rad(G)`. One thus has:

**Proposition 6.2.4.** *Let `G` be an `S`-reductive group. The morphisms*

<!-- label: III.XXII.6.2.4 -->

```text
rad(G) ×_S dér(G) → G,    G → corad(G) ×_S ss(G),    rad(G) → corad(G)
```

*are central isogenies, and their kernels are isomorphic.*

**Corollary 6.2.5.** *The following conditions are equivalent:*

<!-- label: III.XXII.6.2.5 -->

*(i) `G` is the product of a semisimple group and a torus.*

*(ii) `rad(G) ×_S dér(G) ⥲ G`.*

*(iii) `G ⥲ corad(G) ×_S ss(G)`.*

*(iv) `rad(G) ∩ dér(G) = e`.*

#### 6.2.6.

<!-- label: III.XXII.6.2.6 -->

Let us return provisionally to the case of a split group. Let us keep the notations of 6.1. Set `N = M ∩ V(R*)^⊥`. One
thus has `T′ = D_S(M/N)`. One has seen that `U_- · T′ · U` was an open neighborhood of the unit section of `dér(G)`. One
thus has

```text
Lie(dér(G)/S) = t′ ⨿ ⨿_{α ∈ R} g^α.
```

Since the characters induced on `T′` by the `α ∈ R` are non-zero and distinct (cf. Exp. XXI 1.2.5 — one has moreover
already used this fact in 6.1.2), `R` is a system of roots of `dér(G)` relative to `T′`. It is then immediate (since
`Uα ⊂ dér(G)`) that the `exp` morphisms of `dér(G)` "are" those of `G` and similarly for the coroots.

It follows:

**Proposition 6.2.7.** *In the preceding notations, `(dér(G), T′, M/N, R)` is a split group with root datum `dér(R(G))`.
The canonical morphism `dér(G) → G` gives by functoriality the canonical morphism of root data `R(G) → dér(R(G))` of
Exp. XXI 6.5.*

<!-- label: III.XXII.6.2.7 -->

*N. B.* The reader may, as an exercise, construct the diagram of split groups corresponding to the three left columns of
the diagram of root data of Exp. XXI 6.5.7.

**Proposition 6.2.8.** *Let `S` be a scheme, `G` an `S`-reductive group, `dér(G)` its derived group.*

<!-- label: III.XXII.6.2.8 -->

*(i) For every maximal torus `T` of `G`, `T ∩ dér(G)` is a maximal torus of `dér(G)`. For every maximal torus `T′` of
`dér(G)`, `Centr_G(T′) = rad(G) · T′` is a maximal torus of `G`. The two preceding constructions are inverse to one
another and set up a bijective correspondence between maximal tori of `G` and of `dér(G)`.*

*(ii) For every Borel subgroup `B` of `G`, `B ∩ dér(G)` is a Borel subgroup `B′` of `dér(G)`. One has `B′u = B^u`. For
every Borel subgroup `B′` of `dér(G)`, `Norm_G(B′) = rad(G) · B′` is a Borel subgroup of `G`. The preceding applications
are inverse to one another and set up a bijective correspondence between Borel subgroups of `G` and of `dér(G)`.*

By the local conjugacy theorem for maximal tori and the construction of the derived group, the only assertion that
remains to prove in (i) is the following: if `T` is a maximal torus of `G`, then

```text
T = (T ∩ dér(G)) · rad(G) = Centr_G(T ∩ dér(G)).
```

The first equality is trivial (one reduces to the split case); the second follows from this immediately, because
`rad(G)` is central in `G`, so `T = Centr_G(T) = Centr_G(T ∩ dér(G))`. One reasons similarly for (ii).

### 6.3. Subgroups with commutative quotients

<!-- label: III.XXII.6.3 -->

#### 6.3.1.

<!-- label: III.XXII.6.3.1 -->

Let `G` be an `S`-reductive group. If `H` is a group subsheaf of `G`, the following conditions are equivalent:

- `H` contains `dér(G)`.
- `H` is normal and `G/H` is commutative.

In this case, the canonical morphism `f₀ : G → corad(G)` sends `H` to a subsheaf `f₀(H)` of `corad(G)`; one has

```text
G/H ≃ corad(G)/f₀(H),    H/dér(H) ≃ f₀(H),
dér(G) = dér(H),    H = f₀⁻¹(f₀(H)).
```

Since `dér(G)` is smooth over `S` and has connected fibers,[^N.D.E-XXII-64] by Exp. IV, 5.3.1 and 6.3.1, and Exp. IV_B
9.2, the map `H ↦ f₀(H)` establishes a bijective correspondence between group subschemes (resp. closed group subschemes)
of `G` containing `dér(G)`, smooth over `S` and with connected fibers, and group subschemes (resp. closed group
subschemes) of `corad(G)`, smooth over `S` and with connected fibers.

Now, if `H′` is a group subscheme of `corad(G)`, smooth over `S` with connected fibers, then `H′` is of finite
presentation over `S` (Exp. VI_B 5.5) and its fibers are tori (since those of `corad(G)` are), so by Exp. X 8.2, `H′` is
a subtorus of `corad(G)`, hence is closed in `corad(G)` (Exp. IX 2.6).

Consequently, every subgroup of `G`, smooth with connected fibers and containing `dér(G)`, is closed in
`G`.[^N.D.E-XXII-64]

#### 6.3.2.

<!-- label: III.XXII.6.3.2 -->

If `H` is a closed group subscheme of `G`, smooth over `S`, with connected fibers, and normal in `G`, then `H` is
reductive. If furthermore `H ⊃ dér(G)`, then `dér(H) = dér(G)` and `f₀(H)` is identified with `corad(H)`. One has thus
proved:

**Proposition 6.3.3.** *Let `G` be an `S`-reductive group. Every group subscheme `H` of `G`, normal in `G`, with
commutative quotient (i.e. containing `dér(G)`), smooth over `S`, with connected fibers,[^N.D.E-XXII-65] is closed and
reductive. One has `dér(H) = dér(G)` and `f₀(H)` is identified with `corad(H)`; one has*

<!-- label: III.XXII.6.3.3 -->

```text
G/H ≃ corad(G)/corad(H),    H = (H ∩ rad(G)) · dér(G).
```

*Furthermore, `H ↦ f₀(H)` defines a bijection between the set of subgroups `H` of `G` possessing the preceding
properties and the set of subtori of `corad(H)`.*

By a further application of Noether's theorem (Exp. IV, 5.3.1 and 6.3.1), one deduces:

**Proposition 6.3.4.** *Let `S` be a scheme, `G` an `S`-reductive group, `T` a maximal torus of `G`. For every subgroup
`H` of `G` as above, `T ∩ H` is a maximal torus of `G` and one has*

<!-- label: III.XXII.6.3.4 -->

```text
G/H ≃ T/(T ∩ H),    H = (T ∩ H) · dér(G).
```

*Furthermore, `H ↦ T ∩ H` is a bijection between the set of subgroups `H` of `G` as above and the set of subtori of `T`
containing `T ∩ dér(G)`.*

## Bibliography

[BLie] N. Bourbaki, *Groupes et algèbres de Lie*, Ch. IV–VI, Hermann, 1968.

[Ch05] C. Chevalley, *Classification des groupes algébriques semi-simples* (with the collaboration of P. Cartier, A.
Grothendieck, M. Lazard), Collected Works, vol. 3, Springer, 2005.

[DG70] M. Demazure, P. Gabriel, *Groupes algébriques*, Masson & North-Holland, 1970.

[Gi71] J. Giraud, *Cohomologie non abélienne*, Springer-Verlag, 1971.

[Se64] J.-P. Serre, *Cohomologie galoisienne*, Springer-Verlag, 1964; 5th ed. 1994.

## Editor's Notes

<!-- LEDGER DELTA — Exposé XXII — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| déploiement | splitting | Standard for SGA 3 Tome III. |
| déployé | split | Standard. |
| déployable | splittable | Standard. |
| donnée radicielle tordue | twisted root datum | Per 1.9; matches XXI usage. |
| racine / coracine | root / coroot | Standard. |
| exposant radiciel | root exponent | Per 4.2.2. |
| isogénie centrale | central isogeny | Per 4.2.9. |
| morphisme de groupes déployés | morphism of split groups | Per 4.2.1. |
| centre réductif | reductive center | Per 5.1.2(d). |
| grosse cellule | big cell | Per 4.1.4 footnote; quotes preserved. |
| sous-groupe de type (R) | subgroup of type (R) | Per 5.2.1. |
| sous-groupe de type (RR) / (RA) / (RC) | group of type (RR) / (RA) / (RC) | Per 5.1.1, 5.1.6, 5.11.1. |
| transporteur strict | strict transporter | Per 5.3.9. |
| couple de Killing | Killing couple | Per 5.3.13; "Killing pair" is also common but we follow the French structure. |
| position générale | general position | Per 5.9.1. |
| sous-groupe critique | critical subgroup | Per 5.10.4. |
| tore C-critique | C-critical torus | Per 5.10.4 (modified by editor). |
| radical unipotent | unipotent radical | Per 5.11.4. |
| corad(G) / dér(G) / rad(G) / ss(G) / ad(G) | corad(G) / dér(G) / rad(G) / ss(G) / ad(G) | Notation preserved (French `dér` for derived). |
| contenu (d'une racine) | content (of a root) | Per 5.1.1(iv) and N.D.E. (22). |
| en position générale | in general position | Per 5.9.1. |
| Bible | Bible | Italicized when standing alone; cf. Séminaire Chevalley 1956/58. |
| symmetrie w₀ | symmetry w₀ | Per 6.1.6 (longest element of Weyl group). |
| séparé (pour fppf) | separated (for fppf) | Per 4.1.11 footnote. |
| sous-groupe radiciel | root subgroup | Standard; `Uα` notation preserved. |
-->

[^N.D.E-XXII-0]: Version of 13/10/2024.

[^N.D.E-XXII-1]: The set `Γ(S, gα)×` is defined in XIX 4.4.1.

[^N.D.E-XXII-2]: That is, if one denotes by `⟨ , ⟩` the duality between `gα` and `g_{-α}` and if one identifies `gα`
    with `Uα` via `pα(x) = exp(xXα)`, and similarly for `−α`, then `⟨pα(x), p_{-α}(y)⟩ = xy`.

[^N.D.E-XXII-3]: We have added the numbering 1.8.0 to highlight these definitions.

[^N.D.E-XXII-4]: We have added the number 2.6.1 for later references.

[^N.D.E-XXII-5]: We have corrected the original, which referred to 1.17.

[^N.D.E-XXII-6]: Indeed, since `W_S` and `W_G(T) = Norm_G(T)/T` are étale over `S`, the morphism
    `f : W_S → W_G(T) = Norm_G(T)/T` is étale (EGA IV₄, 17.3.4); if furthermore each `f_s` is an
    isomorphism, then, by loc. cit., 17.9.1, `f` is a surjective open immersion, hence an isomorphism.

[^N.D.E-XXII-7]: Indeed, let `T` be a maximal torus of `G`. The fact that `W_G(T)` is finite over `S` is local for the
    (fpqc) topology (EGA IV₂, 2.7.1), so a fortiori for the étale topology. By 2.3, one may therefore
    suppose that `G` is split relative to `T`, in which case the assertion follows from 3.4.

[^N.D.E-XXII-8]: We have replaced `Q_w` by `N_w`, just as in XX 3.0 we had replaced `Q` by `N×`.

[^N.D.E-XXII-9]: And we call it the "big cell" corresponding to `R+`.

[^N.D.E-XXII-10]: We have expanded the original in what follows.

[^N.D.E-XXII-11]: See also EGA IV₃, 11.10.10.

[^N.D.E-XXII-12]: We have added the following sentence.

[^N.D.E-XXII-13]: We have expanded the original in what follows.

[^N.D.E-XXII-14]: Indeed, the representability of the center by a closed subscheme of `G` is local for the (fpqc)
    topology (SGA 1, VIII 5.2 and 5.4), so a fortiori for the étale topology, and the same holds for the
    property "of multiplicative type".

[^N.D.E-XXII-15]: We have expanded the original in what follows.

[^N.D.E-XXII-16]: Note that this is equivalent to the hypothesis: if `α, α′ ∈ R`, `m, m′ ∈ ℤ` and if
    `(m α ∘ f)_s = (m′ α′ ∘ f)_s` for every geometric point `s` of `S`, then `m α = m′ α′`. In particular,
    this separation hypothesis is stable under base change.

[^N.D.E-XXII-17]: Recall (cf. Exp. IV, 4.3.5) that an `S`-prefunctor `H` is separated for a topology `T` if for every
    `S′ → S` and every family of `S`-morphisms `(S′_i → S′)_{i ∈ I}` covering for `T`, the map
    `H(S′) → ∏_i H(S′_i)` is injective.

[^N.D.E-XXII-18]: We have expanded the original in what follows.

[^N.D.E-XXII-19]: We have replaced the notation `u : R → R′` by `d : R → R′`.

[^N.D.E-XXII-20]: We have expanded the reference to Exp. VI in what follows.

[^N.D.E-XXII-21]: Indeed, since `G` and `G′` are semisimple, `f_T` is surjective with finite kernel, so `f` is
    faithfully flat with finite kernel by 4.2.6 (i) and 4.2.8.

[^N.D.E-XXII-22]: The content of the root `α` is the positive generator of the ideal `{f(α), f ∈ Γ₀(R)*}` of `ℤ`; it is
    the largest integer `c > 0` such that `α/c ∈ Γ₀(R)`.

[^N.D.E-XXII-23]: We have added this recall.

[^N.D.E-XXII-24]: The original stated "under the conditions of (iv)", but the last condition of (iv) does not seem to be
    used here.

[^N.D.E-XXII-25]: The hypothesis that `G` (resp. `H`) be of finite presentation over `S` is automatically verified
    because `G` (resp. `H`) being smooth over `S` with connected fibers, is quasi-compact and separated
    over `S` (VI_B 5.5), so of finite presentation over `S`.

[^N.D.E-XXII-26]: This amounts to saying that `H` is a smooth subgroup of `G`, each of whose geometric fibers `H_s` is a
    Borel subgroup of `G_s` (since every Borel subgroup of `G_s` is connected and contains a Cartan
    subgroup of `G_s`).

[^N.D.E-XXII-27]: We have expanded what follows.

[^N.D.E-XXII-28]: By hypothesis, `H` contains `Centr_G(T′)` for some maximal torus `T′` of `G`; then `T` and `T′` are
    conjugate in `H`, so `H` also contains `C = Centr_G(T)`.

[^N.D.E-XXII-29]: We have added this recall, which is used in the proofs of 5.3.1 and 5.3.4.

[^N.D.E-XXII-30]: We have expanded the original in what follows.

[^N.D.E-XXII-31]: We have added the following proof.

[^N.D.E-XXII-32]: Indeed, let `g ∈ G`, `s` its image in `S`, `m` the maximal ideal of `O_{G,g}`, `n` that of `O_{S,s}`,
    and `I` (resp. `I′`) the kernel of the morphism of `O_{G,g}` into `O_{H,g}` (resp. `O_{H′,g}`) (the
    latter being the zero ring if `g ∉ H`, resp. `g ∉ H′`). Since `O_{G,g}` is noetherian, `I` and `I′`
    are closed for the `m`-adic topology, so a fortiori for the `n`-adic topology, so it suffices to show
    that `I + n^n O_{G,g} = I′ + n^n O_{G,g}` for every `n ∈ ℕ`.

[^N.D.E-XXII-33]: Indeed, if `k` is algebraically closed, all the maximal tori of `G = SL₂,k` are conjugate under
    `G(k)`, and all have for Lie algebra the line `k · id ⊂ M₂(k)` (which is invariant under the adjoint
    action).

[^N.D.E-XXII-34]: Cf. footnote (25).

[^N.D.E-XXII-35]: In fact, it suffices (cf. loc. cit.) that 2 and 3 be non-zero on `S`.

[^N.D.E-XXII-36]: By EGA IV₄, 17.11.2, `i` is étale at every point of the unit section (and `Norm_G(g_{R′})` is smooth
    at every point of the unit section). Furthermore, let `V` be the largest open subset of `Ω_{R+, R′}`
    on which `i` is étale; since `i` is a monomorphism, `i_V` is an open immersion (ibid., 17.9.1).

[^N.D.E-XXII-37]: That is, if `g^{iα+jβ} = 0` on a connected component of `S`, the corresponding exponential is 1 on
    this component.

[^N.D.E-XXII-38]: Note that such an ordering is necessarily compatible with `ord_Δ`, where `Δ = S(R+)` (cf. XXI 3.2.15).

[^N.D.E-XXII-39]: The inclusion follows from `t ⊂ g_{R′′}`.

[^N.D.E-XXII-40]: We have corrected the original in what follows.

[^N.D.E-XXII-41]: This is in fact a statement about root systems, completing Exposé XXI (cf. [BLie], VI § 1.7, Prop. 22)
    and proved here by an indirect route.

[^N.D.E-XXII-42]: Indeed, `G` having connected fibers is separated over `S` by VI_B 5.5, so by XI 6.11 (see also the
    addition 6.5.5 in VI_B), `Norm_G(U_{R′})` is represented by a closed group subscheme `N` of `G`. If
    `N` contains `T` and the `Uβ`, for `β ∈ R′′`, it then contains the big cell `Ω_{R+, R′′}`; now this is
    schematically dense in `H_{R′′}` by 5.4.4 and EGA IV₃, 11.10.10 (the fibers of `H_{R′′}` are integral
    and `Ω_{R+, R′′}` contains a non-empty open subset of each fiber). It follows that `H_{R′′} ⊂ N`,
    hence `H_{R′′}` normalizes `U_{R′}`.

[^N.D.E-XXII-43]: One must see that, under the hypotheses of (ii), if `α ∈ R′` and `β ∈ R′′`, then all roots of the form
    `iα + jβ` with `i, j ∈ ℕ*` belong to `R′`, and for this we have replaced the reference XXI 2.3.5 by
    XXI 3.1.2. This may also be seen directly by inspection of the rank 2 root systems.

[^N.D.E-XXII-44]: We have removed the hypothesis that `U` be closed, which is automatically verified. Indeed, for such a
    `U`, one has `U ∩ T = e` by 5.6.10, so the semi-direct product `H = T · U` is a subgroup of type (R)
    of `G` (cf. 5.2.1), with solvable geometric fibers. So, by 5.6.3, `H` is closed in `G`, and since `U`
    is closed in `H`, it is closed in `G`.

[^N.D.E-XXII-45]: This re-proves and refines XII 1.10 (for `G` reductive).

[^N.D.E-XXII-46]: By SGA 1, VIII 2.1 and EGA IV₄, 17.7.1.

[^N.D.E-XXII-47]: See also the additions made in VI_B, 6.2.1 to 6.2.6 and 6.5.2 to 6.5.5.

[^N.D.E-XXII-48]: It is in fact a closed immersion, by Exp. XVI 1.5 (a).

[^N.D.E-XXII-49]: We have expanded the original in what follows.

[^N.D.E-XXII-50]: Cf. Exp. II 4.11.8.

[^N.D.E-XXII-51]: The original next indicated that, denoting `n_{N/G}` the inverse image of the conormal sheaf `N_{N/G}`
    by the unit section `S → N`, the condition that `n_{N_{S′}/G_{S′}} → ω¹_{G_{S′}/S′}` be universally
    injective is equivalent to the fact that `S′ → S` factors through some open subscheme of `S`. We were
    unable to justify this point, in view of the fact that the formation of `N_{N/G}` does not commute
    with base change, and we have replaced this argument with the one that follows, indicated by O.
    Gabber.

[^N.D.E-XXII-52]: Cf. SGA 1, VIII 2.1.

[^N.D.E-XXII-53]: One may suppose `S` affine and, since `Bor(G)` is of finite presentation over `S` by (i), reduce to
    the case where `S` is noetherian; one is then under the hypotheses of EGA IV₃, 15.7.10.

[^N.D.E-XXII-54]: We have expanded what follows.

[^N.D.E-XXII-55]: Indeed, the proof of 5.8.1 only uses 5.3.3 (valid for a group of type (RA)) and XIX 6.2 which, by XII
    1.7 (b), is also valid for groups of type (RR).

[^N.D.E-XXII-56]: This is the corollary on page 18 of TDTE I.

[^N.D.E-XXII-57]: Indeed, one has an exact sequence `H¹(S, B^u) → H¹(S, B) ──π──→ H¹(S, B/B^u) = H¹(S, T)`, see [Se64],
    I § 5.5, Prop. 38 or [Gi71], III Prop. 3.3.1. Now `H¹(S, T) → H¹(S, B)` is a section of `π`, so `π` is
    surjective; on the other hand `H¹(S, B^u) = 0` by 5.9.6.

[^N.D.E-XXII-58]: We have modified the original, introducing the terminology "C-critical torus" instead of "critical
    torus", in order to avoid confusions in later references (cf. Exp. XXVI, 3.9). We have also expanded
    the statement of 5.10.5 and added Remark 5.10.5.1.

[^N.D.E-XXII-59]: I.e. when every residue characteristic of `S` is `> 3`.

[^N.D.E-XXII-60]: The symmetry `w₀` is defined in XXI 3.6.14.

[^N.D.E-XXII-61]: We have added "at every point of the unit section" as well as the reference to VI_B 3.10 at the end of
    the proof. Furthermore, in the next sentence we have replaced "prescheme" with "presheaf".

[^N.D.E-XXII-62]: In what follows, we have expanded the original, and suppressed the assertion that "`dér(G)` is the
    separated (fppf) presheaf of commutators of `G`".

[^N.D.E-XXII-63]: Indeed, `G` is the (fppf) quotient of `rad(G) ×_S dér(G)` by `Ker(u)`, which is a group of
    multiplicative type, hence flat over `S`. Therefore, by VI_B 9.2 (xi), the morphism `u` is flat.

[^N.D.E-XXII-64]: We have expanded the original in what follows. In particular, we have added the conclusion (implicit
    in the original) that every subgroup of `G`, smooth with connected fibers and containing `dér(G)`, is
    closed in `G`.

[^N.D.E-XXII-65]: We have removed the hypothesis that `H` be retrocompact in `G`, which is automatically verified
    because, by VI_B 5.5, `G` and `H` are separated and quasi-compact over `S`, so `H ↪ G` is
    quasi-compact by EGA IV₁, 1.1.2 (v).
