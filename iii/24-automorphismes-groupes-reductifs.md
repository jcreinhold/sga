# Exposé XXIV. Automorphisms of reductive groups

<!-- label: III.XXIV -->

*by M. Demazure*

<!-- original page 215 -->

[^N.D.E-XXIV-0]

The first part of this Exposé (nos 1 to 5) is a direct consequence of the existence, for a reductive group, of
"sufficiently many outer automorphisms", a result which is itself a consequence of the weakest form of the isomorphism
theorem for pinned groups. The second part (nos 6 and 7) presents two applications of the more precise results of the
preceding Exposé; in particular, no 7 uses the theorem of generators and relations in its explicit form. Finally, we
have given in an appendix (no 8) some results on "Galois" cohomology used in the text.

Let us specify our cohomological notation: if `S` is a scheme and `G` an `S`-group scheme, we write `H¹(S, G)` for the
first cohomology set of `S` with coefficients in `G`, computed for the (fpqc) topology; this is also the set of
isomorphism classes of (fpqc) principal homogeneous sheaves under `G`. We write `H¹_ét(S, G)` for the corresponding set
for the étale topology; this is therefore the part of `H¹(S, G)` formed by classes of homogeneous sheaves under `G`
which are quasi-isotrivial (= locally trivial for the étale topology). We write `Fib(S, G)` for the part of `H¹(S, G)`
formed by classes of representable sheaves (principal homogeneous bundles). We thus have the inclusions

<!-- original page 216 -->

```text
H¹_ét(S, G) ⊂ H¹(S, G),
Fib(S, G) ⊂ H¹(S, G).
```

If every principal homogeneous sheaf under `G` is representable (for example if `G` is quasi-affine over `S`, cf. SGA 1,
VIII 7.9), then `Fib(S, G) = H¹(S, G)`.

If `S' → S` is a covering morphism for the (fpqc) topology, we write `H¹(S'/S, G)` for the kernel of the canonical map
`H¹(S, G) → H¹(S', G_{S'})`. It is known that `H¹(S'/S, G)` can be computed simplicially (TDTE I, § A.4), which implies
that when `S' → S` is covering for the étale topology, `H¹(S'/S, G)` is also the kernel of
`H¹_ét(S, G) → H¹_ét(S', G_{S'})`.

Finally, following Exp. VIII, 4.5, we call "theorem 90" the following assertion: "every principal homogeneous sheaf
under `G_{m, S}` is representable and locally trivial", an assertion equivalent to "`H¹(S, G_{m, S}) = Pic(S)`", or
again to "`H¹(S, G_{m, S}) = 0` for `S` local (or more generally semi-local)".

## 1. The automorphism scheme of a reductive group

<!-- label: III.XXIV.1 -->

### 1.0.

<!-- label: III.XXIV.1.0 -->

It is convenient first to make certain definitions of the preceding Exposé more precise. Let `S` be a nonempty scheme,
`G` an `S`-reductive group, `R = (M, M*, R, R*, Δ)` a pinned reduced root datum (Exp. XXIII 1.5). We call *pinning of
`G` of type `R`*, or *`R`-pinning of `G`*, the datum:

(i) of an isomorphism of `D_S(M)` onto a maximal torus `T` of `G` (or, what amounts to the same, of a monomorphism
`D_S(M) → G` whose image is a maximal torus `T` of `G`), identifying `R` with a root system of `G` relative to `T` (Exp.
XIX, 3.6) and `R*` with the corresponding set of coroots,

<!-- original page 217 -->

(ii) for each `α ∈ Δ`, of an `X_α ∈ Γ(S, g_α)^×`.

For `G` to possess an `R`-pinning, it is necessary and sufficient that it be splittable and of type `R` (Exp. XXII,
2.7).

If `u : G → G'` is an isomorphism of `S`-reductive groups, to every `R`-pinning `E` of `G` there corresponds by
"transport of structure" an `R`-pinning `u(E)` of `G'`. If `v : R' → R` is an isomorphism of pinned root data, to every
`R'`-pinning `E` of `G'` there corresponds by transport of structure an `R`-pinning `v(E)` of `G`.

Let us call a *pinned group* a triple `(G, R, E)` where `G` is an `S`-reductive group, `R` is a pinned reduced root
datum, and `E` is a pinning of `G` of type `R`. We call an *isomorphism of the pinned group `(G, R, E)` onto the pinned
group `(G', R', E')`* a pair `(u, v)` where `u` is an isomorphism `u : G → G'` and `v` is an isomorphism of pinned root
data `v : R' → R`, such that `u(E) = v(E')`.[^N.D.E-XXIV-1]

**N. B.** If `S` is nonempty, `v` is uniquely determined by `u`, and we shall also say by abuse of language that `u` is
an isomorphism of pinned groups. In particular, if `(G, R, E)` is a pinned group, an automorphism of `(G, R, E)` is
therefore an automorphism `u` of `G` such that there exists an automorphism `v` of `R` with `u(E) = v(E)`; it is
therefore an automorphism of `G` normalizing `T`, inducing on `T` an automorphism of the form `D_S(h)` where `h` is an
automorphism of `M`, and permuting among themselves the elements `X_α`, `α ∈ Δ`. (As is easily seen, the preceding
conditions moreover characterize the automorphisms of `(G, R, E)`.)

<!-- original page 218 -->

One has an obvious contravariant functor

```text
Φ :  (G, R, E) ↦ R,   (u, v) ↦ v
```

and the principal result of the preceding Exposé (Exp. XXIII, 4.1) shows us that this is a fully faithful functor (we
shall moreover see in the next Exposé that it is an equivalence of categories). It follows in particular that the group
of automorphisms of `(G, R, E)` is canonically isomorphic to the group of automorphisms of the pinned root datum `R`
(cf. Exp. XXIII, 5.5).

### 1.1.

<!-- label: III.XXIV.1.1 -->

Let `S` be a scheme; endow `(Sch)/S` with the (fpqc) topology and consider the `S`-group sheaf `Aut_{S-gr.}(G)`, where
`G` is an `S`-group scheme. One has an exact sequence of `S`-group sheaves

```text
1 → Centr(G) → G ─int→ Aut_{S-gr.}(G)
```

which defines a monomorphism

```text
j : G / Centr(G) → Aut_{S-gr.}(G).
```

The image sheaf of `j` is the sheaf of *inner automorphisms* of `G`; for an automorphism `u` of `G` to be inner, it is
necessary and sufficient that there exist a covering family `{S_i → S}` and for each `i` a `g_i ∈ G(S_i)` such that
`int(g_i) = u_{S_i}`. In this case, if `v` is another automorphism of `G`, one sees at once that `int(v) u = v u v^{-1}`
is the inner automorphism defined by the family `g'_i = v(g_i)`. It follows that the image of `j` is normal in
`Aut_{S-gr.}(G)`. The quotient group sheaf, denoted `Autext(G)`, is the sheaf of *outer automorphisms* of `G`. One thus
has an exact sequence

```text
1 → G / Centr(G) → Aut_{S-gr.}(G) → Autext(G) → 1.
```

The preceding definitions are all compatible with base change. They are naturally valid in any site.

### 1.2.

<!-- label: III.XXIV.1.2 -->

Let `S` be a scheme and `(G, R, E)` a pinned `S`-reductive group. Let `E` be the (abstract) group of automorphisms of
the pinned root datum `R`, i.e. the group of automorphisms of `R` normalizing `Δ`. By Exp. XXIII, 5.5, one has a
canonical monomorphism

```text
E → Aut_{S-gr.}(G)
```

which associates to `h ∈ E` the unique automorphism `u` of the pinned group `G` such that `Φ(u) = h`. This monomorphism
canonically defines a monomorphism of sheaves

```text
(*)    a : E_S → Aut_{S-gr.}(G).
```

For an automorphism `u` of `G` to be a section of the image sheaf of `a`, it is necessary and sufficient that the
following conditions be satisfied:

(i) `u` normalizes `T`. One then knows that `u` permutes the roots of `G` relative to `T`. If `α ∈ R`, then
`u(α) : t ↦ α(u^{-1}(t))` is locally on `S` of the form `t ↦ β(t)`, with `β ∈ R`. The second condition is then written
as follows:

<!-- original page 219 -->

(ii) If `α ∈ Δ` and if `U` is an open set of `S` such that `u(α)_U ∈ R`, then `u(α)_U ∈ Δ` and

```text
Lie(u_U)(X_α)_U = (X_{u(α)})_U.
```

It follows at once from the definitions that the sections of `a(E_S)` normalize the subgroups of `G` defined by the
pinning: `T`, `B`, `B^-`, `U`, `U^-`.

These definitions being set, one has:

**Theorem 1.3.** *Let `S` be a scheme, `G` an `S`-reductive group. Consider the canonical exact sequence of `S`-group
sheaves[^N.D.E-XXIV-2]*

```text
1 → ad(G) → Aut_{S-gr.}(G) ─p→ Autext(G) → 1.
```

*(i) `Aut_{S-gr.}(G)` is representable by a smooth and separated `S`-scheme.*

*(ii) `Autext(G)` is representable by a finitely generated twisted constant `S`-scheme (Exp. X, 5.1).*

*(iii) If `G` is splittable, the preceding exact sequence splits. More precisely, for every pinning of `G`, the morphism
(cf. 1.2 (\*))*

```text
p ∘ a : E_S → Autext(G)
```

*is an isomorphism.*

<!-- label: III.XXIV.1.3 -->

Let us first show how the theorem follows from the following lemma:

**Lemma 1.4.** *Under the hypotheses of (iii), `Aut_{S-gr.}(G)` is the semi-direct product
`a(E_S) · ad(G)`.*[^N.D.E-XXIV-3]

<!-- label: III.XXIV.1.4 -->

The lemma immediately implies the theorem when `G` is splittable. Since `G` is locally splittable for the étale topology
(Exp. XXII, 2.3), hence also for the (fppf) topology, and since the latter is "of effective descent" for the fibered
category of twisted constant morphisms (Exp. X, 5.5), one deduces (ii) in the general case (cf. Exp. IV, 4.6.8). To
deduce (i), one notes that `ad(G)` is affine over `S`, hence the morphism `p` is affine when `Aut_{S-gr.}(G)` is
representable, and one concludes by descent of affine schemes.[^N.D.E-XXIV-4]

<!-- original page 220 -->

It therefore remains only to prove 1.4. For this, it suffices to prove:

**Lemma 1.5.** *If `(R, E)` and `(R', E')` are two pinnings of the `S`-reductive group `G`, there exists a unique inner
automorphism `u` of `G` over `S` transforming one pinning into the other (i.e. such that there exists `v : R' ⥲ R` with
`u(E) = v(E')`, cf. 1.0).*

<!-- label: III.XXIV.1.5 -->

#### 1.5.1. Uniqueness.

It suffices to prove that if `G` is a pinned `S`-group and if `int(g)` is an automorphism of pinned group (`g ∈ G(S)`),
then `int(g) = id`. Now one has first `int(g) T = T`, `int(g) B = B`, so `g ∈ Norm_G(T)(S) ∩ Norm_G(B)(S) = T(S)` (cf.
for example Exp. XXII, 5.6.1). It follows that `int(g)` normalizes each `U_α` and that

```text
Lie(int(g)) X_α = Ad(g) X_α = α(g) X_α
```

for every `α ∈ Δ`. One thus has `α(g) = 1` for `α ∈ Δ`, so `g ∈ ⋂_{α ∈ Δ} (Ker α)(S) = Centr(G)(S)` (Exp. XXII, 4.1.8).
QED

#### 1.5.2. Existence.

It suffices to prove this locally for the (fpqc) topology. Let

```text
(T, M, R, Δ, (X_α)_{α ∈ Δ})    and    (T', M', R', Δ', (X'_{α'})_{α' ∈ Δ'})
```

be the two pinnings. By conjugacy of maximal tori, one may assume `T = T'`. Up to restricting `S`, one may assume that
the isomorphism `D_S(M) ≃ D_S(M')` comes from an isomorphism `M ≃ M'` carrying `R` onto `R'`, and one is reduced to the
situation `T = T'`, `M = M'`, `R = R'`. Since the systems of simple roots are conjugate by the Weyl group (Exp. XXI,
3.3.7), one may also assume `Δ = Δ'`. There then exists for each `α ∈ Δ` a scalar `z_α ∈ G_m(S)` such that
`X'_α = z_α X_α`, and it suffices to construct locally for (fpqc) a section `t` of `T` such that `α(t) = z_α` for each
`α ∈ Δ`. But the morphism `T → (G_{m, S})^Δ` with components `{α, α ∈ Δ}` is the dual of an injection `ℤ^Δ → M`, hence
faithfully flat, which completes the proof of 1.5.2 and so of 1.3.

<!-- original page 221 -->

**Corollary 1.6.** *Let `S` be a scheme, `G` an `S`-reductive group. The following conditions are equivalent:*

*(i) `Aut_{S-gr.}(G)` is affine (resp. of finite type, resp. of finite presentation, resp. quasi-compact) over `S`.*

*(ii) `Autext(G)` is finite over `S`.*

*(iii) For every `s ∈ S`, one has `rg_red(G_s) − rg_ss(G_s) ⩽ 1`.*

<!-- label: III.XXIV.1.6 -->

Indeed, since `ad(G)` is affine, flat and of finite presentation over `S`, the morphism `p : Aut_{S-gr.}(G) → Autext(G)`
is affine, faithfully flat and of finite presentation.

If `Autext(G)` is finite over `S`, it is affine over `S`, hence so is `Aut_{S-gr.}(G)`, which proves (ii) ⇒ (i). If
`Aut_{S-gr.}(G)` is quasi-compact over `S`, it is of finite presentation over `S` (being in any case locally of finite
presentation and separated over `S`); by Exp. V, 9.1, `Autext(G)` is then of finite presentation over `S`, hence finite,
which proves (i) ⇒ (ii). Finally, to prove the equivalence of (ii) and (iii), one may assume `G` split, and one is
reduced to Exp. XXI, 6.7.8.

**Corollary 1.7.** *Let `S` be a scheme and `G` an `S`-reductive group. Then `Aut_{S-gr.}(G)⁰ ≃ ad(G)`.*

<!-- label: III.XXIV.1.7 -->

**Corollary 1.8.** *Let `S` be a scheme, `G` an `S`-reductive group, `H` an `S`-group scheme smooth, affine and with
connected fibers over `S`. Then the `S`-functor*

```text
Isom_{S-gr.}(G, H)
```

*is representable by a smooth and separated `S`-scheme (which is affine over `S` if `G` is semisimple).*

<!-- label: III.XXIV.1.8 -->

Indeed, let `U` be the set of points `s` of `S` such that `H_s` is reductive; this is open (Exp. XIX, 2.6); if `S'` is
an `S`-scheme, `H_{S'}` is reductive if and only if `S' → S` factors through `U`. It follows that the canonical morphism
`Isom_{S-gr.}(G, H) → S` factors through `U`. One may therefore assume `S = U` and one is reduced to:

<!-- original page 222 -->

**Corollary 1.9.** *Let `S` be a scheme, `G` and `G'` two `S`-reductive groups. Then*

```text
F = Isom_{S-gr.}(G, G')
```

*is representable by a smooth and separated `S`-scheme (affine if `G` or `G'` is semisimple). Moreover, `S` decomposes
as a sum of two open subschemes `S_1` and `S_2` such that `F_{S_1} = ∅` and such that `F_{S_2}` is a principal
homogeneous bundle on the left (resp. right) under `Aut_{S_2-gr.}(G'_{S_2})` (resp. `Aut_{S_2-gr.}(G_{S_2})`).*

<!-- label: III.XXIV.1.9 -->

Indeed, let `S_2` be the set of points of `S` where `G` and `G'` are of the same type, and let `S_1` be its complement.

Since the type of a reductive group is a locally constant function, `S_1` and `S_2` are open. It is clear that
`F_{S_1} = ∅`, and one may assume `S = S_2`. By Exp. XXIII, 5.6, `F` is a principal homogeneous sheaf under
`Aut_{S-gr.}(G)`, locally trivial for the étale topology. It follows that `F_0 = F / ad(G)` is a principal homogeneous
sheaf under `Autext(G)`, locally trivial for the étale topology, hence representable (Exp. X, 5.5). Since `ad(G)` is
affine, `F` is therefore also representable.

Let us remark that in the course of the proof, we have obtained:

**Corollary 1.10.** *Let `S` be a scheme, `G` and `G'` two `S`-reductive groups of the same type at each `s ∈ S`. Then
`ad(G)` operates freely (on the right) in `Isom_{S-gr.}(G, G')`, the quotient sheaf*

```text
Isomext(G, G') = Isom_{S-gr.}(G, G') / ad(G)
```

*is representable by a twisted constant `S`-scheme, which is a principal homogeneous bundle under `Autext(G)` (and which
is therefore finite over `S` if `G` is semisimple). Moreover, the isomorphism*

```text
Isom_{S-gr.}(G, G') ≃ Isom_{S-gr.}(G', G)
```

*defined by `u ↦ u^{-1}` induces an isomorphism*

```text
Isomext(G, G') ≃ Isomext(G', G).
```

<!-- label: III.XXIV.1.10 -->

<!-- original page 223 -->

**Remark 1.11.** If `Isomext(G, G')(S) ≠ ∅`, one says that `G` is an *inner twisted form* of `G'`; then `G'` is an inner
twisted form of `G`; one can then reduce the structure group of `Isom_{S-gr.}(G, G')` to `ad(G)`. More precisely, let
`u ∈ Isomext(G, G')(S)`, considered as a section `u : S → Isomext(G, G')`. Write

```text
Isomint_u(G, G')
```

for the inverse image under the canonical morphism `Isom_{S-gr.}(G, G') → Isomext(G, G')` of the closed subscheme of
`Isomext(G, G')` image of `u`. The natural operation of `ad(G)` on `Isomint_u(G, G')` endows this scheme with a
structure of principal homogeneous bundle; by extension of the structure group[^N.D.E-XXIV-5] `ad(G) → Aut(G)`,
`Isomint_u(G, G')` recovers `Isom_{S-gr.}(G, G')`.

<!-- label: III.XXIV.1.11 -->

By Hensel's lemma (Exp. XI, 1.11), 1.8 gives at once:

**Corollary 1.12.** *Let `S` be a henselian local scheme, `G` an `S`-reductive group, `G'` a smooth affine `S`-group
with connected fibers, `s` the closed point of `S`. If `G_s` and `G'_s` are isomorphic `κ(s)`-algebraic groups, then `G`
and `G'` are isomorphic. More precisely, every `κ(s)`-isomorphism `G_s ≃ G'_s` comes from an `S`-isomorphism `G ≃ G'`.*

<!-- label: III.XXIV.1.12 -->

Applying now 1.7 (resp. 1.12) to the scheme of dual numbers over a field, one deduces from Exp. III, 2.10 (resp. 3.10)
point (i) (resp. (ii)) of the following corollary.

**Corollary 1.13.** *Let `k` be a field and `G` a `k`-reductive group.*

*(i) If `G` is adjoint, one has `H¹(G, Lie(G/k)) = 0`.[^N.D.E-XXIV-6]*

*(ii) One has `H²(G, Lie(G/k)) = 0`.*

<!-- label: III.XXIV.1.13 -->

**Remark 1.14.** (i) The assertion concerning `H¹` was known (Chevalley); the one concerning `H²` had been proved in
most cases of the classification by Chevalley.

<!-- original page 224 -->

(ii) In fact, the conjunction of 1.13 and the uniqueness theorem over an algebraically closed field is essentially
equivalent to the uniqueness theorem. A direct proof of 1.13 would therefore give a way to deduce the general uniqueness
theorem from Chevalley's uniqueness theorem over a field.

The existence of reductive groups of all types over all schemes (Exp. XXV) shows that the obstructions to lifting a
`k`-reductive group `G` over Artinian rings with residue field `k` (which by Exp. III, 3.8 are elements of

```text
H³(G, Lie(G/k) ⊗ V) ≃ H³(G, Lie(G/k)) ⊗ V,
```

where `V` is a certain `k`-vector space (equipped with the trivial action of `G`)) are zero. This seems to suggest that
`H³(G, Lie(G/k)) = 0`. Here too, a direct proof of this fact (if it is true) would doubtless give a way to deduce the
general existence theorem from the existence theorem over a field (Chevalley's Tôhoku).

<!-- label: III.XXIV.1.14 -->

**Corollary 1.15.** *Let `k` be a field,[^N.D.E-XXIV-7] `G` a `k`-reductive group. Consider `k` as a trivial `G`-module.
Then*

```text
H¹(G, k) = H²(G, k) = 0.
```

<!-- label: III.XXIV.1.15 -->

[^N.D.E-XXIV-8] Since `Hⁱ(G_{k̄}, k̄) = Hⁱ(G, k) ⊗ k̄`, one may assume `k` algebraically closed. An element of
`H¹(G, k)` is nothing but a morphism of `k`-groups `φ : G → G_{a, k}`. Then `φ(G) = G / Ker(φ)` is a smooth, connected
and reductive subgroup (cf. XIX 1.7) of `G_{a, k}`, hence trivial. So `H¹(G, k) = 0`.

<!-- original page 225 -->

Consider now the `k`-reductive group `H = G ×_k G_{m, k}`. One has `Lie(H/k) = Lie(G/k) ⊕ k`, a decomposition stable
under `H`. For any `H`-module `V`, one has

```text
Hⁱ(H, V) = Hⁱ(G, H⁰(G_{m, k}, V))
```

(this follows from the characterization of `Hⁱ(H, −)` as derived functors of `H⁰(H, −) = H⁰(G, H⁰(G_{m, k}, −))`, and
from the fact that the functor `H⁰(G_{m, k}, −)` is exact, cf. Exp. I, 5.3.1 and 5.3.3). In particular, one has for
every `i`

```text
Hⁱ(H, Lie(H/k)) = Hⁱ(G, Lie(G/k)) ⊕ Hⁱ(G, k)
```

whence `H²(G, k) = 0` by applying 1.13 (ii) to the reductive group `H`.

**Corollary 1.15.1.** [^N.D.E-XXIV-9] *Let `k` be a field, `G` a `k`-reductive group, `Z` its center and
`R = (M, M*, R, R*)` the type of `G`. Then one has*

```text
H¹(G, Lie(G/k)) ≃ Ext¹_ℤ(M / Γ₀(R), k).
```

*In particular, `H¹(G, Lie(G/k)) = 0` if and only if `Z` is smooth over `k`.*

<!-- label: III.XXIV.1.15.1 -->

Indeed, let `g` (resp. `z`, resp. `g_ad`) be the Lie algebra of `G` (resp. `Z`, resp. `G_ad = G/Z`). It follows from
1.15 (and from its proof) that

```text
H¹(G, g) = H¹(G_ad, g) ≃ H¹(G_ad, g/z).
```

Set `C = Coker(g → g_ad)`; one has an exact sequence

```text
0 → g/z → g_ad → C → 0.
```

Since `H¹(G_ad, g_ad) = 0` (1.13) and `H⁰(G_ad, g_ad) = 0` (cf. Exp. II, 5.2.3), one obtains

```text
H¹(G_ad, g/z) ≃ H⁰(G_ad, C).
```

To compute the right-hand term, one may assume `k` algebraically closed. Let `(G, T, M, R)` be a splitting of `G`; then
`Z = D_k(M / Γ₀(R))` and `C` is identified with

```text
Coker( Hom_ℤ(M, k) → Hom_ℤ(Γ₀(R), k) ) ≃ Ext¹_ℤ(M / Γ₀(R), k),
```

equipped with the trivial action of `G_ad`. The corollary follows, since `Z` is not smooth over `k` if and only if
`char(k) = p > 0` and `M / Γ₀(R)` has `p`-torsion (Exp. IX, 2.1).

**Definition 1.16.** *Let `S` be a scheme, `G` an `S`-reductive group. We call a* form of `G` over `S` *an `S`-group
scheme `G'` locally isomorphic to `G` for the (fpqc) topology (it amounts to the same to say (cf. Exp. XXIII, 5.6) that
`G'` is locally isomorphic to `G` for the étale topology, or again that `G'` is an `S`-reductive group of the same type
as `G` at every point of `S`).*

<!-- label: III.XXIV.1.16 -->

**Corollary 1.17.** *Let `S` be a scheme, `G` an `S`-reductive group.*

*(i) The functor*

```text
G' ↦ Isom_{S-gr.}(G, G')
```

*is an equivalence between the category of forms of `G` over `S` and the category of principal homogeneous bundles under
`Aut_{S-gr.}(G)`.*

<!-- original page 226 -->

*(ii) If `S' → S` is a covering morphism, forms of `G` trivialized by `S'` and bundles trivialized by `S'` correspond.*

*(iii) Every principal homogeneous sheaf under `Aut_{S-gr.}(G)` is representable and quasi-isotrivial (i.e. locally
trivial for the étale topology).*

<!-- label: III.XXIV.1.17 -->

The first assertion is formal in the category of sheaves (for (fpqc) for example). On the other hand, every sheaf
locally isomorphic to `G` (for (fpqc)) is representable (since `G` is affine over `S`) and locally isomorphic to `G` for
the étale topology. Finally, for every form `G'` of `G`, the `S`-sheaf `Isom_{S-gr.}(G, G')` is representable, by 1.8.
The corollary follows at once.

**Corollary 1.18.** *The set of isomorphism classes of forms of the reductive group `G` over `S` is isomorphic to*

```text
H¹(S, Aut_{S-gr.}(G)) = H¹_ét(S, Aut_{S-gr.}(G)) = Fib(S, Aut_{S-gr.}(G)).
```

*If `S' → S` is a covering morphism, the subset formed by forms trivialized by `S'` is isomorphic to
`H¹(S'/S, Aut_{S-gr.}(G))`.*

<!-- label: III.XXIV.1.18 -->

**Corollary 1.19.** *Let `S` be a scheme, `R` a pinned reduced root datum such that `Ép_S(R)`[^N.D.E-XXIV-10] exists
(condition automatically satisfied, cf. Exp. XXV). Write*

```text
A_S(R) = Aut_{S-gr.}(Ép_S(R)) = ad(Ép_S(R)) · E(R)_S.
```

*(i) The set of isomorphism classes of `S`-reductive groups of type `R` (Exp. XXII, 2.7) is isomorphic (by Exp. XXIII,
5.12) to*

```text
H¹(S, A_S(R)) = H¹_ét(S, A_S(R)) = Fib(S, A_S(R)).
```

*(ii) If `S' → S` is a covering morphism, the subset formed by the classes of groups splittable over `S'` is isomorphic
to `H¹(S'/S, A_S(R))`.*

<!-- label: III.XXIV.1.19 -->

**Remark 1.20.** With the preceding notation, to every `S`-reductive group of type `R` is canonically associated a right
principal homogeneous bundle under `A_S(R)`:

```text
Isom_{S-gr.}(Ép_S(R), G) = P.
```

Note that `P` is to be interpreted as the "scheme of pinnings of `G` of type `R`" (cf. 1.0). Moreover `P` is also a
principal homogeneous bundle (on the left) under `Aut_{S-gr.}(G)`, a structure that appears at once in the description
above.

<!-- label: III.XXIV.1.20 -->

**Proposition 1.21.** *Let `S` be a henselian local scheme, `s` its closed point. The functor*

```text
G ↦ G_s
```

*induces a bijection of the set of isomorphism classes of `S`-reductive groups onto the set of isomorphism classes of
`κ(s)`-reductive groups.*

*In particular, for every `S`-reductive group `G`, there exists a finite surjective étale morphism `S' → S` such that
`G_{S'}` is splittable.*

<!-- label: III.XXIV.1.21 -->

<!-- original page 227 -->

Using the existence of the `Ép_S(R)` (Exp. XXV), one is reduced to proving that if one writes `H = A_S(R)`, the
canonical map

```text
Fib(S, H) → Fib(κ(s), H_s)
```

is bijective (and that every element of `Fib(S, H)` has the property indicated above). Now, every finite part of `H` is
contained in an affine open set (it is indeed trivial for a constant group, and `H` is affine above a constant group);
one may therefore use the result proved in the appendix (8.1).

## 2. Automorphisms and subgroups

<!-- label: III.XXIV.2 -->

<!-- original page 228 -->

Let us introduce a notation: if `H = Aut_{S-gr.}(G)`, and if `X` is a subfunctor of `G`, we write

```text
Aut_{S-gr.}(G, X) = Norm_H(X),    Aut_{S-gr.}(G, id_X) = Centr_H(X).
```

If `Y` is a second subfunctor of `G`, one defines similarly
`Aut_{S-gr.}(G, X, Y) = Aut_{S-gr.}(G, X) ∩ Aut_{S-gr.}(G, Y)`, and if `G'` is a second `S`-group and `X'` a subfunctor
of `G'`, one writes `Isom_{S-gr.}(G, X; G', X')` for the subfunctor of `Isom_{S-gr.}(G, G')` defined by: for every
`S' → S`,

```text
Isom_{S-gr.}(G, X; G', X')(S') = { u ∈ Isom_{S-gr.}(G, G')(S') | u(X_{S'}) = X'_{S'} }
```

and one defines similarly `Isom_{S-gr.}(G, X, Y; G', X', Y')`, etc.[^N.D.E-XXIV-11]

**Proposition 2.1.** *Let `S` be a scheme, `G` an `S`-reductive group, `T` a maximal torus of `G` (resp. `B` a Borel
subgroup of `G`, resp. `B ⊃ T` a Killing couple of `G`). Write `T_ad` (resp. `B_ad`) for the maximal torus (resp. Borel
subgroup) of `ad(G)` corresponding to `T` (resp. `B`):*

```text
B_ad ≃ B / Centr(G) = B / Centr(B),
T_ad ≃ T / Centr(G).
```

*Then `Aut_{S-gr.}(G, T)` (resp. `Aut_{S-gr.}(G, B)`, resp. `Aut_{S-gr.}(G, B, T)`) is representable by a closed
subscheme of `Aut_{S-gr.}(G)`, smooth over `S`, and the exact sequence of Theorem 1.3 induces exact sequences:*

```text
1 → Norm_{ad(G)}(T_ad) → Aut_{S-gr.}(G, T) → Autext(G) → 1;
1 → B_ad → Aut_{S-gr.}(G, B) → Autext(G) → 1;
1 → T_ad → Aut_{S-gr.}(G, B, T) → Autext(G) → 1.
```

<!-- label: III.XXIV.2.1 -->

By descent of closed subschemes,[^N.D.E-XXIV-12] one is at once reduced to the case where `G` is pinned and where
`B ⊃ T` is its canonical Killing couple (cf. Exp. XXII, 5.5.5 (iv)). Since the group `E` of 1.2 normalizes `B` and `T`,
the result follows at once from the normalization theorems in `ad(G)` (Exp. XXII, 5.3.12 and 5.6.1).

<!-- original page 229 -->

Using now the conjugation theorems (cf. Exp. XXIII, 5.12), and arguing as in no 1, one deduces:

**Corollary 2.2.** *Let `S` be a scheme, `G` and `G'` two `S`-reductive groups of the same type at each point. Let
`B ⊃ T` (resp. `B' ⊃ T'`) be a Killing couple of `G` (resp. `G'`).*

*(i) The `S`-functor `Isom_{S-gr.}(G, T; G', T')` is representable by a closed smooth subscheme of `Isom_{S-gr.}(G, G')`
which is principal homogeneous under `Aut_{S-gr.}(G, T)`.*

*Moreover, `Norm_{ad(G)}(T_ad)` operates freely on this scheme, and one has a canonical isomorphism*

```text
Isom_{S-gr.}(G, T; G', T') / Norm_{ad(G)}(T_ad) ≃ Isomext(G, G').
```

*(ii) The `S`-functor `Isom_{S-gr.}(G, B; G', B')` is representable by a closed smooth subscheme of
`Isom_{S-gr.}(G, G')` which is principal homogeneous under `Aut_{S-gr.}(G, B)`.*

*Moreover, `B_ad` operates freely on this scheme and one has a canonical isomorphism*

```text
Isom_{S-gr.}(G, B; G', B') / B_ad ≃ Isomext(G, G').
```

*(iii) The `S`-functor `Isom_{S-gr.}(G, B, T; G', B', T')` is representable by a closed smooth subscheme of
`Isom_{S-gr.}(G, G')`, principal homogeneous under `Aut_{S-gr.}(G, B, T)`.*

*Moreover, `T_ad` operates freely on this scheme and one has a canonical isomorphism*

```text
Isom_{S-gr.}(G, B, T; G', B', T') / T_ad ≃ Isomext(G, G').
```

<!-- label: III.XXIV.2.2 -->

Arguing again as in no 1, one deduces:

**Corollary 2.3.** *Let `S` be a scheme, `G` an `S`-reductive group, `B ⊃ T` a Killing couple of `G`. The functor*

```text
(G', T') ↦ Isom_{S-gr.}(G, T; G', T'),
```

*resp.*

```text
(G', B') ↦ Isom_{S-gr.}(G, B; G', B'),
```

*resp.*

```text
(G', B', T') ↦ Isom_{S-gr.}(G, B, T; G', B', T'),
```

*is an equivalence between the category of pairs `(G', T')` (resp. of pairs `(G', B')`, resp. of triples
`(G', B', T')`), where `G'` is a form of `G` and `T'` a maximal torus of `G'` (resp. `B'` a Borel subgroup of `G'`,
resp. `B' ⊃ T'` a Killing couple of `G'`), and the category of principal homogeneous bundles under the `S`-group `H`,
where `H = Aut_{S-gr.}(G, T)` (resp. `H = Aut_{S-gr.}(G, B)`, resp. `H = Aut_{S-gr.}(G, B, T)`).*

<!-- original page 230 -->

*Moreover, every principal homogeneous sheaf under `H` is representable and quasi-isotrivial, so that one has*

```text
H¹(S, H) = H¹_ét(S, H) = Fib(S, H).
```

<!-- label: III.XXIV.2.3 -->

**Remark 2.4.** Under the conditions of 2.2, the morphism noted set-theoretically `u ↦ u(T)` (resp. `u ↦ u(B)`, resp.
`u ↦ (u(B), u(T))`) induces an isomorphism

```text
Isom_{S-gr.}(G, G') / Aut_{S-gr.}(G, T) ≃ Tor(G')
```

```text
resp.    Isom_{S-gr.}(G, G') / Aut_{S-gr.}(G, B) ≃ Bor(G'),
```

```text
resp.    Isom_{S-gr.}(G, G') / Aut_{S-gr.}(G, B, T) ≃ Kil(G').
```

The proof is immediate: it suffices to do it locally for (fpqc), so one may assume `G ≃ G'`, and one is reduced to Exp.
XXII, 5.8.3 (iii).

<!-- label: III.XXIV.2.4 -->

**Remark 2.5.** The preceding results are at once interpreted in terms of restriction of the structure group: if `G'` is
a form of `G`, corresponding to the principal bundle `Isom_{S-gr.}(G, G')`, to give a restriction of the structure group
of this bundle to `Aut_{S-gr.}(G, T)` amounts to giving a maximal torus `T'` of `G'`, the bijections suggested above
being that of 2.4 on the one hand, the map `T' ↦ Isom_{S-gr.}(G, T; G', T')` on the other. Similarly for Borel subgroups
and Killing couples.

<!-- label: III.XXIV.2.5 -->

**Proposition 2.6.** *Let `S` be a scheme, `G` and `G'` two `S`-reductive groups of the same type at each point, `T`
(resp. `T'`) a maximal torus of `G` (resp. `G'`). Then `T_ad` operates freely on `Isom_{S-gr.}(G, T; G', T')`, the
quotient*

```text
P = Isom_{S-gr.}(G, T; G', T') / T_ad
```

*is representable; it is a principal homogeneous bundle under*

```text
A = Aut_{S-gr.}(G, T) / T_ad,
```

*where `A` is representable by a twisted constant `S`-scheme, extension of `Autext(G)` by
`W_{ad(G)}(T_ad) = Norm_{ad(G)}(T_ad) / T_ad`. Moreover, if one makes `A` operate on `T` in the obvious way, the bundle
associated to `P` is none other than `T'`.[^N.D.E-XXIV-13]*

<!-- label: III.XXIV.2.6 -->

The first part of the proposition follows at once from the preceding results. To prove the second, one notes that there
is an obvious morphism `P ×_S T → T'` (defined by `(u, t) ↦ u(t)`); to show that after passage to the quotient by `A` it
induces an isomorphism, one may once again assume `(G, T) ≃ (G', T')`, in which case it is immediate.

In an entirely analogous way, one has:

**Proposition 2.7.** *Let `S` be a scheme, `G` and `G'` two `S`-reductive groups of the same type at each point, `B ⊃ T`
(resp. `B' ⊃ T'`) a Killing couple of `G` (resp. `G'`). If one makes `Aut_{S-gr.}(G, B, T) / T_ad ≃ Autext(G)` operate
in the obvious way on `T`, the bundle associated to `Isomext(G, G')` is none other than `T'`.*

<!-- label: III.XXIV.2.7 -->

**Corollary 2.8.** *Let `G` and `G'` be two `S`-reductive groups that are inner twisted forms of each other; let `B ⊃ T`
(resp. `B' ⊃ T'`) be a Killing couple of `G` (resp. `G'`). Then `T` and `T'` are isomorphic.[^N.D.E-XXIV-14]*

<!-- label: III.XXIV.2.8 -->

<!-- original page 231 -->

**Remark 2.9.** It is not true in general that `B` and `B'` are isomorphic; they are however inner twisted forms of each
other (cf. no 5).

<!-- label: III.XXIV.2.9 -->

One can develop "Isomint" variants[^N.D.E-XXIV-15] of the preceding results. Let us point out one:

**Proposition 2.10.** *Let `S` be a scheme, `G` and `G'` two `S`-reductive groups of the same type at each point,
`B ⊃ T` (resp. `B' ⊃ T'`) a Killing couple of `G` (resp. `G'`). Let `u ∈ Isomext(G, G')(S)`; consider*

```text
Isomint_u(G, B, T; G', B', T') = Isom_{S-gr.}(G, B, T; G', B', T') ∩ Isomint_u(G, G').
```

*It is a smooth and affine `S`-scheme which is a principal homogeneous bundle under `T_ad`. In particular,
`Isomint_u(G, B, T; G', B', T')(S) ≠ ∅` if and only if the corresponding element of `H¹(S, T_ad)` is zero.*

<!-- label: III.XXIV.2.10 -->

To conclude this section, let us prove two results which will be useful later:

**Proposition 2.11.** *Let `S` be a scheme, `G` an `S`-reductive group, `T` a maximal torus of `G`. The obvious
morphism*

```text
T_ad ⥲ Aut_{S-gr.}(G, id_T)
```

*is an isomorphism.*

<!-- label: III.XXIV.2.11 -->

This follows from the preceding statements; moreover, one has given a direct proof in the course of the proof of 1.5.2.

**Corollary 2.12.** *Under the preceding conditions, there exists an equivalence between the category of pairs
`(G', f)`, where `G'` is a form of `G` and `f` is an isomorphism of `T` onto a maximal torus of `G'`, and the category
of principal homogeneous bundles under `T_ad`.*

<!-- label: III.XXIV.2.12 -->

**Corollary 2.13.** *If `H¹(S, T_ad) = 0`, and if `G'` is a form of `G` possessing a maximal torus isomorphic to `T`,
then `G'` is isomorphic to `G`.*

<!-- label: III.XXIV.2.13 -->

**Corollary 2.14.** *Let `S` be a scheme such that `Pic(S) = 0`, and `G` an `S`-reductive group of constant type. For
`G` to be splittable, it is necessary and sufficient that `G` possess a split maximal torus.*

<!-- label: III.XXIV.2.14 -->

<!-- original page 232 -->

Let `G` be a reductive group, `rad(G)` its radical (Exp. XXII, 4.3.9); since `rad(G)` is central and characteristic in
`G`, one has a canonical morphism

```text
q : Autext(G) → Aut_{S-gr.}(rad(G)).
```

**Proposition 2.15.** *Let `G` be an `S`-reductive group. The following sequence is exact:*

```text
1 → ad(G) → Aut_{S-gr.}(G, id_{rad(G)}) ─p→ Autext(G) ─q→ Aut_{S-gr.}(rad(G))
```

*and `Ker(q) = Im(p)` is an open and closed subscheme of `Autext(G)`, finite over `S`.*

<!-- label: III.XXIV.2.15 -->

One may assume `G` split. The first assertion is immediate; the second follows from Exp. XXI, 6.7.5 and 6.7.7.

Writing `H = Aut_{S-gr.}(G, id_{rad(G)})`, one deduces:

**Corollary 2.16.** *There exists an equivalence between the category of pairs `(G', f)`, where `G'` is a form of `G`
and `f` is an isomorphism of `rad(G)` onto the radical of `G'`, and the category of principal bundles under a certain
`S`-group scheme `H`, where `H` is such that there exists an exact sequence*

```text
1 → ad(G) → H → F → 1,
```

*where the `S`-group `F` is étale and finite over `S`.*

<!-- label: III.XXIV.2.16 -->

## 3. Dynkin scheme of a reductive group. Quasi-split groups

<!-- label: III.XXIV.3 -->

### 3.1.

<!-- label: III.XXIV.3.1 -->

Recall (Exp. XXI, 7.4.1) that a *Dynkin diagram* is a finite set endowed with the structure defined by a set of pairs of
distinct elements (*bonds*) and a map to `{1, 2, 3}` (*lengths*). To each pinned reduced root datum `R` is associated a
Dynkin diagram `Δ(R)`, whose underlying set is the set of simple roots.

### 3.2.

<!-- label: III.XXIV.3.2 -->

Let `S` be a scheme. An `S`-*Dynkin scheme* is a finite twisted constant `S`-scheme `Δ`, equipped with the structure
defined by a subscheme `L` of `Δ ×_S Δ` having empty intersection with the diagonal, and by a morphism
`Δ → {1, 2, 3}_S`. If `S'` is a connected[^N.D.E-XXIV-16] `S`-scheme, `Δ(S')` is naturally endowed with a structure of
Dynkin diagram.

One defines at once the following notions: isomorphism of two Dynkin schemes, base change of a Dynkin scheme, constant
Dynkin scheme associated to a Dynkin diagram.

<!-- original page 233 -->

Every descent datum on a Dynkin scheme for the étale topology is effective.

### 3.3.

<!-- label: III.XXIV.3.3 -->

We propose to associate to each `S`-reductive group `G` an `S`-Dynkin scheme. Suppose first that `G` is splittable over
`S`; for every pinning `E` of `G`, write `Δ(E)` for the constant Dynkin scheme associated to the pinned root datum
defined by `E`; if `E` and `E'` are two pinnings of `G`, there exists by 1.5 a unique inner automorphism of `G` over `S`
transforming `E` into `E'`; this automorphism of `G` defines an isomorphism `a_{EE'} : Δ(E) ⥲ Δ(E')`; the `a_{EE'}`
evidently form a transitive system, so that one may identify the `Δ(E)` (i.e. take the inductive limit); the result is a
constant Dynkin scheme denoted `Dyn(G)`. If now `G` is an arbitrary `S`-reductive group, there exists a covering family
for the étale topology `{S_i → S}` such that `G_{S_i}` is splittable. Arguing as previously, one therefore has a
canonical descent datum on the `Dyn(G_{S_i})`, allowing one to construct by descent an `S`-Dynkin scheme `Dyn(G)`.

### 3.4.

<!-- label: III.XXIV.3.4 -->

This construction satisfies the following properties (which moreover essentially characterize it):

(i) To each `S`-reductive group is associated a Dynkin scheme `Dyn(G)`; to every isomorphism `u : G ⥲ G'` is
functorially associated an isomorphism `Dyn(u) : Dyn(G) ⥲ Dyn(G')`.

(ii) If `S'` is an `S`-scheme and `G` an `S`-reductive group, one has

```text
Dyn(G ×_S S') ≃ Dyn(G) ×_S S'.
```

(iii) If `E` is a pinning of `G`, defining the pinned root datum with Dynkin diagram `Δ`, one has

```text
Dyn(G) ≃ Δ_S.
```

(iv) If `u` is an inner automorphism of `G`, `Dyn(u)` is the identity automorphism of `Dyn(G)`.

### 3.5.

<!-- label: III.XXIV.3.5 -->

Let `S` be a scheme, `G` an `S`-reductive group. It is clear that the functor `Aut_{Dyn}(Dyn(G))` of automorphisms of
`Dyn(G)` for the structure of Dynkin scheme is representable by a finite twisted constant `S`-scheme. By 3.4 (i) and
(ii), one has a canonical morphism

```text
Aut_{S-gr.}(G) → Aut_{Dyn}(Dyn(G)),
```

which, by (iv), factors through a morphism

```text
Autext(G) → Aut_{Dyn}(Dyn(G)).
```

More generally, if `G` and `G'` are two `S`-reductive groups, one has a canonical morphism

```text
Isomext(G, G') → Isom_{Dyn}(Dyn(G), Dyn(G'));
```

in particular, if `G'` is an inner twisted form of `G` (1.11), the Dynkin schemes `Dyn(G)` and `Dyn(G')` are isomorphic.

### 3.6.

<!-- label: III.XXIV.3.6 -->

<!-- original page 234 -->

If `G` is semisimple (resp. adjoint or simply connected), the morphism

```text
Autext(G) → Aut_{Dyn}(Dyn(G))
```

is a monomorphism (resp. an isomorphism). Indeed, one may assume `G` pinned and one is reduced to the corresponding
result for pinned reduced root data (cf. Exp. XXI, 7.4.5).

One has an analogous result for `Isom`'s; whence it follows in particular that two semisimple adjoint (resp. simply
connected) `S`-groups are inner twisted forms of each other if and only if their Dynkin schemes are isomorphic.

### 3.7.

<!-- label: III.XXIV.3.7 -->

One can give a different construction of the Dynkin scheme associated to a reductive group. Let `R` be a pinned reduced
root datum, `G` an `S`-reductive group of type `R`; write `Δ(R)` for the Dynkin diagram defined by the root datum `R`.
One has (3.5) a canonical morphism

```text
A_S(R) = Aut_{S-gr.}(Ép_S(R)) → Aut_{Dyn}(Δ(R)_S).
```

The `S`-reductive group `G` corresponds (1.17) to a bundle `Isom_{S-gr.}(Ép_S(R), G)`, principal homogeneous under
`A_S(R)`. The bundle under `Aut_{Dyn}(Δ(R)_S)` associated corresponds to a form on `S` of `Δ(R)_S`: this is `Dyn(G)`; in
other words, this associated bundle is none other than `Isom_{Dyn}(Δ(R)_S, Dyn(G))`. In this last form, the proof is
immediate.

### 3.8. Dynkin scheme and Killing couples.

<!-- label: III.XXIV.3.8 -->

Let `S` be a scheme, `G` an `S`-reductive group, `B ⊃ T` a Killing couple of `G`. There exists a canonical morphism

```text
i : Dyn(G) → Hom_{S-gr.}(T, G_{m, S})
```

which identifies `Dyn(G)` with the "scheme of simple roots of `B` relative to `T`"; this morphism is defined at once by
descent from the pinned case. Note moreover that the datum of `T` and of `i` allows one to reconstruct `B` ("biunivocal
correspondence between systems of simple roots and systems of positive roots").

It follows from the preceding description of `D = Dyn(G)` that there exists a canonical root of `B_D` with respect to
`T_D`: this root `α_D` is the image under `i(D)` of the identity morphism of `D`. One thereby deduces a canonical
invertible `O_D`-module `g_D`:

```text
g_D = (g ⊗_{O_S} O_D)^{α_D}.
```

<!-- original page 235 -->

In the pinned case, one has

```text
D = ⨿_{α ∈ Δ} S_α,
```

where each `S_α` is a copy of `S`, and `g_D` is then the `O_D`-module which induces `g_α` on `S_α`, for every `α ∈ Δ`.

### 3.9. Quasi-pinnings. Quasi-pinned groups.

<!-- label: III.XXIV.3.9 -->

If `G` is an `S`-reductive group, we call *quasi-pinning of `G`* the datum:

(i) of a Killing couple `B ⊃ T` of `G`,

(ii) of a section `X ∈ Γ(Dyn(G), g_D)^×`.

We say that an `S`-reductive group is *quasi-splittable* if it possesses a quasi-pinning. We call *quasi-pinned group* a
reductive group equipped with a quasi-pinning.

Let `B ⊃ T` be a Killing couple of the `S`-reductive group `G`; then `G` is quasi-pinnable relative to this Killing
couple if and only if `g_D` possesses a non-zero section at every point, i.e. if the element of `Pic(Dyn(G))` defined by
`g_D` is zero. Suppose in particular that `S` is semi-local; then `Dyn(G)` is also semi-local, so `Pic(Dyn(G)) = 0`. One
deduces:

**Proposition 3.9.1.** *Let `S` be a semi-local scheme, `G` an `S`-reductive group. For `G` to be quasi-splittable, it
is necessary and sufficient that it possess a Borel subgroup.*

<!-- label: III.XXIV.3.9.1 -->

[^N.D.E-XXIV-17] Indeed, `S` is affine so, by the first assertion of Exp. XXII, 5.9.7, if `G` possesses a Borel subgroup
`B`, it also possesses a Killing couple `B ⊃ T`. Then, since `Pic(D) = 0`, `g_D` possesses a section `X` nowhere zero.

Let still `A` be a semi-local ring and `S = Spec(A)`; remark now that for every `S`-reductive group `G` the morphism
`Bor(G) → S` is surjective (since `G_s` possesses Borel subgroups, for every `s ∈ S`) and smooth and projective (Exp.
XXII, 5.8.3), so it possesses sections after a finite surjective étale extension of the base.[^N.D.E-XXIV-18] One
deduces:

**Corollary 3.9.2.** *Let `S` be a semi-local scheme, `G` an `S`-reductive group. There exists an étale, finite and
surjective morphism `S' → S` such that `G_{S'}` is quasi-splittable.*

<!-- label: III.XXIV.3.9.2 -->

**Remark 3.9.3.** Under the preceding conditions, let `T` be a maximal torus of `G` (cf. Exp. XIV, 3.20); then one may
moreover assume that `G_{S'}` is quasi-splittable relative to `T_{S'}`: it suffices to apply the preceding argument to
the "scheme of Borel subgroups containing `T`", which is finite and étale over `S` (Exp. XXII, 5.5.5 (ii)).

<!-- label: III.XXIV.3.9.3 -->

### 3.10.

<!-- label: III.XXIV.3.10 -->

Let `E` and `E'` be two quasi-pinnings of the `S`-reductive group `G`. There exists a unique inner automorphism of `G`
transforming `E` into `E'`. Indeed, one is at once reduced to the split case, where the assertion has already been
proved (1.5; it suffices indeed to note that for an inner automorphism of `G` it amounts to the same to respect a
pinning or the underlying quasi-pinning). One concludes as in no 1 that a

<!-- original page 236 -->

quasi-pinning of the `S`-reductive group `G` defines a splitting `h` of the exact sequence:

```text
1 → ad(G) → Aut_{S-gr.}(G) ⇄^{h}_{p} Autext(G) → 1,
```

the image of `h` being the subgroup of `Aut_{S-gr.}(G)` which leaves invariant the quasi-pinning.

Similarly if `G` and `G'` are two quasi-pinned `S`-groups, one defines in a natural way the subfunctor

```text
Isom_{S-gr. q-ép.}(G, G')
```

of `Isom_{S-gr.}(G, G')`; the projection of `Isom_{S-gr.}(G, G')` onto `Isomext(G, G')` induces an isomorphism

```text
(*)    Isom_{S-gr. q-ép.}(G, G') ⥲ Isomext(G, G').
```

**Theorem 3.11.** *Let `S` be a scheme, `R` a pinned reduced root datum such that `Ép_S(R)` exists (cf. Exp. XXV), `E`
the group of its automorphisms. Consider the three following categories:*

*(i) The category `Rev` of principal Galois coverings of `S` with group `E` (the morphisms are isomorphisms of
`E`-bundles).*

*(ii) The category `Redext` whose objects are the `S`-reductive groups of type `R` (Exp. XXII, 2.7), the morphisms from
`G` to `G'` being the elements of `Isomext(G, G')(S)`.*

*(iii) The category `Qép` of quasi-pinned `S`-reductive groups of type `R` (the morphisms are the isomorphisms
respecting the quasi-pinnings).*

*These three categories are equivalent: more precisely, one has a diagram of functors, commutative up to functorial
isomorphisms*

```text
       qép
Rev ───────→ Qép
   ╲          ╱
rev ╲        ╱ i
     ╲      ╱
       Redext
```

<!-- label: III.XXIV.3.11 -->

We shall describe below these three functors, leaving to the reader the task of verifying the commutativity of the
diagram.[^N.D.E-XXIV-19]

#### 3.11.1. The functor `i`.

It is the obvious functor: `i(G) = G`, `i(f) =` image of `f` under the isomorphism of 3.10 (\*).

#### 3.11.2. The functor `qép`.

Let `S'` be a principal Galois covering of `S` with group `E`. Let `(G, T, M, R, Δ, (X_α)_{α ∈ Δ})` be a pinning of
`G = Ép_S(R)` and `(X'_α)_{α ∈ Δ}` the corresponding pinning of `G' = G_{S'} = Ép_{S'}(R)`. By Exp. XXIII 5.5 bis, there
exists a unique morphism of groups

```text
θ : E → Aut_{S-gr.}(Ép_S(R)) = A(R)(S)
```

<!-- original page 237 -->

such that, for every `h ∈ E`, `θ(h)` induces `D_S(h)` on `T` and `Lie(θ(h))(X_α) = X_{h(α)}` for every `α ∈ Δ`. Taking
into account the action of `E` on `S'`, one thereby obtains an action of `E` on `G'`, compatible with the action of `E`
on `S'` and respecting the canonical quasi-pinning of `G'`.[^N.D.E-XXIV-20] Since `S' → S` is covering for the (fpqc)
topology, it is an effective descent morphism for the fibered category of affine morphisms, and one writes

```text
qép(S') = Q-Ép_{S'/S}(R)
```

for the quasi-pinned `S`-group obtained by Galois descent.[^N.D.E-XXIV-21]

#### 3.11.3. The functor `rev`.

Let `G` be an `S`-reductive group of type `R`. One writes

```text
rev(G) = Isomext(Ép_S(R), G);
```

this is a principal homogeneous bundle under `E_S` (cf. 1.10 and 1.19), that is, an object of `Rev`.

#### 3.11.4. [^N.D.E-XXIV-22]

It is clear, by the isomorphism 3.10 (\*), that the functor `i` is fully faithful. On the other hand, if `G_0`, `G`,
`G'` are `S`-reductive groups, the natural morphism

```text
Isom(G_0, G) ×_S Isom(G, G') → Isom(G_0, G')
```

induces a morphism

```text
(⋆)    Isomext(G_0, G) ×_S Isomext(G, G') → Isomext(G_0, G')
```

since, for every `S' → S`, if `g_0 ∈ G_0(S')`, `g ∈ G(S')`, `u ∈ Isom(G_0, G)(S')`, and `v ∈ Isom(G, G')(S')`, one has
the equality `v ∘ int(g) ∘ u ∘ int(g_0) = v ∘ u ∘ int(u^{-1}(g) g_0)`. Taking `G_0 = Ép_S(R)`, one obtains a map

```text
Isomext(G, G')(S) → Hom_{Rev}( Isomext(Ép_S(R), G), Isomext(Ép_S(R), G') )
```

and to show that this is a bijection, one may assume by (fpqc) descent that `G` and `G'` are pinned, in which case it is
evident.

<!-- original page 238 -->

Similarly, if `S_1`, `S_2` are two objects of `Rev` and if one writes `S_i ×^E Ép_S(R)` for the `S`-group `qép(S_i)`
obtained by twisting `Ép_S(R)` by the `E`-torsor `S_i` (cf. N.D.E. (21)), one has a natural map

```text
Hom_{Rev}(S_1, S_2) → Hom_{Qép}(S_1 ×^E Ép_S(R), S_2 ×^E Ép_S(R)),
```

and to show that this is a bijection, one may assume by (fpqc) descent that `S_1` and `S_2` are trivial `E`-bundles, in
which case it is evident.

Thus the three functors of the diagram are fully faithful. Moreover, for every object `S'` of `Rev`, one has a natural
morphism

```text
S' → Isomext(Ép_S(R), S' ×^E Ép_S(R))
```

and to see that this is an isomorphism, one may assume by (fpqc) descent that `S'` is a trivial `E`-bundle, in which
case it is evident.

One thus has an isomorphism of functors `Id_{Rev} → rev ∘ i ∘ qép`. Since the functor `rev` is fully faithful one
obtains therefore, for every `S`-reductive group `H` (not necessarily quasi-split), a bijection

```text
Isomext(Q-Ép_{rev(H)/S}(R), H)(S) ≃ Aut_{Rev}(rev(H))
```

functorial in `H`. In particular, the identity morphism of `rev(H)` corresponds to a "canonical" element `u_0` of
`Isomext(Q-Ép_{rev(H)/S}(R), H)(S)`; moreover, every `u ∈ Isomext(Q-Ép_{rev(H)/S}(R), H)(S)` corresponds to an
automorphism `φ_u` of `rev(H)`, and `qép(φ_u)` is the unique automorphism of pinned `S`-group of `Q-Ép_{rev(H)/S}(R)`
such that `u_0 ∘ qép(φ_u) = u`. We have thus proved theorem 3.11.

Let us develop one of the corollaries of 3.11:

**Corollary 3.12.** *For every `S`-reductive group `G`, there exists a quasi-pinned `S`-group `G_{q-ép.}` and an "outer
isomorphism" `u ∈ Isomext(G_{q-ép.}, G)(S)`. The pair `(G_{q-ép.}, u)` is unique up to a unique isomorphism.*

<!-- label: III.XXIV.3.12 -->

Indeed, one may assume `G` of constant type `R`, and one takes `G_{q-ép.} = Q-Ép_{rev(G)/S}(R)`.

#### 3.12.1.

<!-- label: III.XXIV.3.12.1 -->

Note that the datum of the pair `(G_{q-ép.}, u)` allows one to define canonically the `S`-scheme (cf. 1.11)

```text
Q = Isomint(G_{q-ép.}, G),[^N.D.E-XXIV-23]
```

which is a principal homogeneous bundle under `ad(G_{q-ép.})`, and whose datum "is equivalent" to that of the inner
twisted form `G` of `G_{q-ép.}`. Moreover, `Q` is none other than the "scheme of quasi-pinnings of `G`", a definition
which accounts for its structure of principal homogeneous bundle (on the left) under `ad(G)` (3.10) — compare with 1.20.

**Proposition 3.13.** *Let `S` be a scheme, `G` a semisimple adjoint (resp. simply connected) `S`-group, `B ⊃ T` a
Killing couple of `G`, `Dyn(G)` the Dynkin `S`-scheme*

<!-- original page 239 -->

*of `G`. There exists a canonical isomorphism of `S`-group schemes*

```text
T ⥲ ∏_{Dyn(G)/S} G_{m, Dyn(G)}.
```

*(Recall (cf. Exp. II, § 1) that the right-hand side is by definition the `S`-functor which to `S' → S` associates
`G_m(Dyn(G) ×_S S')`, or, what amounts to the same, `G_m(Dyn(G_{S'}))`.)*

<!-- label: III.XXIV.3.13 -->

*First proof.* Let us do it for simplicity in the adjoint case. Consider the composite morphism

```text
T → ∏_{D/S} T_D → ∏_{D/S} G_{m, D},
```

where the first morphism is the canonical morphism, the second is `∏_{D/S} α_D` (we have written `D = Dyn(G)`). To
verify that this morphism is an isomorphism, one may assume `G` split; now, in this case, this is none other than the
morphism `T → (G_{m, S})^Δ` with components `α`, for `α ∈ Δ`, and the latter is an isomorphism (Exp. XXII, 4.3.8).

*Second proof.* By 2.8, 3.5 and 3.11, one may assume that `G = Q-Ép_{S'/S}(R)`, `T` being the canonical maximal torus.
On `S'`, one has by Exp. XXII 4.3.8, an isomorphism `T_{S'} ⥲ (G_{m, S'})^Δ`, defined by the simple roots (resp. the
simple coroots). The group `E` operates on the right-hand side by permutation of `Δ`. Now the bundle associated to
`S'/S` by `E → Aut(Δ)` is `Dyn(G)` (3.7), and one concludes at once.

Using Prop. 8.4 of the appendix, one deduces:

**Corollary 3.14.** *Under the preceding conditions, one has*

```text
H¹(S, T) ⥲ H¹(Dyn(G), G_m) ⥲ Pic(Dyn(G)).
```

*In particular, `H¹(S, T) = 0` when `S` is semi-local.*

<!-- label: III.XXIV.3.14 -->

<!-- original page 240 -->

**Remark 3.15.** Let `S` be a scheme, `G` (resp. `G'`) an `S`-reductive group, `B ⊃ T` (resp. `B' ⊃ T'`) a Killing
couple of `G` (resp. `G'`), `u ∈ Isomext(G, G')(S)`. Set (cf. 2.10)

```text
P = Isomint_u(G, B, T; G', B', T');
```

this is a principal homogeneous bundle under `T_ad` (by `(f, t) ↦ f ∘ int(t)`).

Let on the other hand `D = Dyn(G) = Dyn(G')` (identified via `u` (3.5)), and let `L = Isom_D(g_D, g'_D)` be the
principal homogeneous bundle under `G_{m, D}` defined by the invertible `O_D`-module

```text
Hom_{O_D}(g_D, g'_D) = g'_D ⊗ (g_D)^∨.
```

Each `f ∈ P(S')` defines an isomorphism of `g_D ⊗_{O_S} O_{S'}` onto `g'_D ⊗_{O_S} O_{S'}`, whence a canonical morphism

```text
P → ∏_{D/S} L.
```

This morphism is an isomorphism, compatible with the isomorphism of operator groups

```text
T_ad ⥲ ∏_{D/S} G_{m, D}
```

defined above. Indeed, it suffices to verify it in the case where the two groups are pinned, where it is easy.

<!-- label: III.XXIV.3.15 -->

It follows in particular that in the isomorphism

```text
H¹(S, T_ad) ⥲ Pic(Dyn(G))
```

of 3.14, the class of the bundle `P` is transformed into `cℓ(g'^D) − cℓ(g_D)`. The bundle `P` is therefore trivial if
and only if `g'^D` and `g_D` are isomorphic.

If `(G, B, T)` is quasi-splittable, for example if one takes for `G` the group `G'_{q-ép.}`, with its canonical Killing
couple, it follows that the image of the class of `P` is none other than the obstruction to the quasi-splitting of `G'`
defined in 3.9.

### 3.16. Symmetries

<!-- label: III.XXIV.3.16 -->

#### 3.16.1.

<!-- label: III.XXIV.3.16.1 -->

Let `S` be a scheme, `G` an `S`-reductive group, `B ⊃ T` a Killing couple of `G`. Write `D = Dyn(G)`. Recall (Exp. XXII,
5.9.1) that there exists a unique Borel subgroup `B^-` of `G` such that `B ∩ B^- = T`. If `X ∈ Γ(D, g_D)^×` defines a
quasi-pinning of `G` relative to `(B, T)` (3.9), then `Y = −X^{-1} ∈ Γ(D, (g_D)^∨)^×` defines a quasi-pinning of `G`
relative to `(B^-, T)`; one says that this is the *opposite quasi-pinning*.

If `R` is a pinned reduced root datum and if `E` is an `R`-pinning of the `S`-reductive group `G`, one defines an
`R`-pinning `E^-` said to be *opposite to `E`* in the following way: one keeps the same maximal torus `T`, one takes the
opposite of the isomorphism `D_S(M) ⥲ T`, and one "pins" by `Y_α = −X_α^{-1} ∈ Γ(S, g^{-α})^×`, for `α ∈ Δ`. The
quasi-pinning underlying `E^-` is the quasi-pinning opposite to the quasi-pinning underlying `E`.

**Remark.** In the notation of Exp. XIX, 3.1, if one sets

```text
w_α(X_α) = exp(X_α) exp(−X_α^{-1}) exp(X_α),
```

one has `w_α(X_α) = w_{-α}(Y_α)` (loc. cit., 3.1 (vi)).

<!-- original page 241 -->

**Proposition 3.16.2.** *Let `S` be a scheme, `G` an `S`-reductive group.*

*(i) Let `T` be a maximal torus of `G`; there exists a unique*

```text
i_T ∈ (Aut_{S-gr.}(G, T) / T_ad)(S) ⊂ Aut_{S-gr.}(T)
```

*such that `i_T(t) = t^{-1}` for every section `t` of `T`.*

*(ii) Let `(B, T)` be a Killing couple of `G`; there exists a unique section*

```text
w_{B, T} ∈ (Norm_G(T) / T)(S) = W_G(T)(S)
```

*such that `int(w_{B, T})(B) = B^-` (with the obvious abuse of language).*

*(iii) Let `Q = (B, T, X)` be a quasi-pinning of `G`, `Q^- = (B^-, T, Y)` the opposite quasi-pinning; there exists a
unique inner automorphism of `G`*

```text
n_Q ∈ Norm_{ad(G)}(T_ad)(S) ⊂ Aut_{S-gr.}(G)
```

*such that `n_Q(Q) = Q^-`, that is, `n_Q(T) = T`, `n_Q(B) = B^-`, `n_Q(X) = Y`.*

*(iv) Let `(R, E)` be a pinning of `G`, `(R, E^-)` the opposite pinning; there exists a unique automorphism of `G`*

```text
u_E ∈ Aut_{S-gr.}(G, T) ⊂ Aut_{S-gr.}(G)
```

*such that `u_E(E) = E^-`, i.e. `u_E(t) = t^{-1}` for every section `t` of `T`, and `Ad(u_E) X_α = Y_α` for every
`α ∈ Δ`.*

<!-- label: III.XXIV.3.16.2 -->

*Proof.* (ii) follows from Exp. XXII, 5.5.5 (ii), then (iii) follows from 3.10, and (iv) follows from Exp. XXIII, 4.1.
Finally to prove (i), one may assume `G` pinned. Existence follows from (iv) for example, uniqueness from the fact that
an automorphism of `G` inducing the identity on `T` is given by a section of `T_ad` (2.11).

**Corollary 3.16.3.** *One has*

```text
i_T² = w_{B, T}² = n_Q² = u_E² = e.
```

*Moreover, `i_T` (resp. `u_E`) is `≠ e` if `G ≠ e`, and `w_{B, T}` (resp. `n_Q`) is `≠ e` if `G` is not a torus.*

<!-- label: III.XXIV.3.16.3 -->

**Corollary 3.16.4.** *In the situation of (iii) (resp. (iv)), `n_Q` projects onto `w_{B, T}` (resp. `u_E` projects onto
`i_T`) by the canonical morphism*

```text
Norm_{ad(G)}(T_ad) → W_{ad(G)}(T_ad) ≃ W_G(T),
```

*resp.*

```text
Aut_{S-gr.}(G, T) → Aut_{S-gr.}(G, T) / T_ad.
```

<!-- label: III.XXIV.3.16.4 -->

**Corollary 3.16.5.** *The preceding definitions are compatible with base change, and are functorial under isomorphism
(in an obvious sense).*

<!-- label: III.XXIV.3.16.5 -->

<!-- original page 242 -->

**Proposition 3.16.6.** *(i) One can define uniquely for each reductive group `G` over a scheme `S` an element*

```text
s_G ∈ Autext(G)(S)
```

*in such a way that this construction is functorial in `G` under isomorphism, is compatible with base change, and is
such that whenever `T` is a maximal torus of the `S`-reductive group `G`, `s_G` is the image of `i_T` under the
canonical morphism*

```text
Aut_{S-gr.}(G, T) / T_ad → Autext(G).
```

*(ii) One has `s_G² = e`, and `s_G` is a central element of `Autext(G)`.*

*(iii) Under the conditions of 3.16.2 (ii), if one identifies `Aut_{S-gr.}(G, B, T) / T_ad` with `Autext(G)` (2.2), one
has*

```text
w_{B, T} i_T = i_T w_{B, T} = s_G.
```

*(iv) Under the conditions of 3.16.2 (iv), if one identifies `Aut_{S-gr.-ép}(G, R, E)` with `Autext(G)` (1.3 (iii)), one
has*

```text
n_E u_E = u_E n_E = s_G.
```

<!-- label: III.XXIV.3.16.6 -->

*Proof.* (i) is proved without difficulty by descent. On the other hand, since `i_T` is evidently a central section of
square `e` in `Aut_{S-gr.}(T)`, (ii) follows immediately; (iii) is a consequence of (iv) by descent. Finally, under the
conditions of (iv), it is clear that `n_E u_E = u_E n_E` and that this automorphism of `G` respects the pinning; modulo
the identification made, it is therefore equal to its image in `Autext(G)`; but `n_E` is inner and `u_E` projects onto
`s_G`.

**Remark 3.16.7.** (i) One determines `s_G` explicitly in each case of the classification thanks to (iii): for each
irreducible pinned root datum it suffices to compose the symmetry through the origin with the symmetry in the Weyl group
(i.e. the element `w_0` of the Weyl group such that `w_0(Δ) = −Δ`). One finds the following results: one has `s_G = e`
except for `A_n` (`n ⩾ 2`), `D_n` (`n` odd) and `E_6`, in which case `s_G` is the unique non-trivial "outer
automorphism".

(ii) The automorphism `u_E` is the one used to construct "the compact real forms" in the theory of semisimple Lie
algebras.

<!-- label: III.XXIV.3.16.7 -->

<!-- original page 243 -->

**Remark 3.16.8.** We defined in 3.16.1 an involution in the `S`-scheme `Q = Isomint(G_{q-ép.}, G)` of quasi-pinnings of
`G` (cf. 3.12.1); by transport of structure from `G_{q-ép.}` to `G`, one sees at once that this involution is given by
the action of an element of `ad(G_{q-ép.})(S)`: the element `n_0` defined (3.16.2 (iii)) by the canonical quasi-pinning
of `G_{q-ép.}`.

In the same way, one has defined an involution in the `S`-scheme

```text
P = Isom_{S-gr.}(Ép_S(R), G)
```

of `R`-pinnings of `G` (cf. 1.20). Arguing as before, one sees that this involution is given by the action of the
automorphism `u_0` of `Ép_S(R)` defined (3.16.2 (iv)) by the canonical pinning of `Ép_S(R)`.

<!-- label: III.XXIV.3.16.8 -->

## 4. Isotriviality of reductive groups and of principal bundles under reductive groups

<!-- label: III.XXIV.4 -->

### 4.1. Definitions. Isotriviality theorem

<!-- label: III.XXIV.4.1 -->

**Definition 4.1.1.** *Let `S` be a scheme, `G` an `S`-group scheme, `P` a principal homogeneous bundle under `G`. One
says that `P` is* locally isotrivial *(resp.* semi-locally isotrivial\*) if for every point `s ∈ S` (resp. every finite
set `F` of points of `S` contained in an affine open set) there exist an open set `U` of `S` containing `s` (resp. `F`)
and a finite surjective étale morphism `S' → U` such that `P_{S'}` is trivial.\*

<!-- label: III.XXIV.4.1.1 -->

**Definition 4.1.2.** *Let `S` be a scheme, `G` an `S`-reductive group. One says that `G` is* locally isotrivial
*(resp.* semi-locally isotrivial\*) if for every point `s ∈ S` (resp. every finite set `F` of points of `S` contained in
an affine open set) there exist an open set `U` of `S` containing `s` (resp. `F`) and a finite surjective étale morphism
`S' → U` such that `G_{S'}` is splittable.\*

<!-- label: III.XXIV.4.1.2 -->

**Remark 4.1.3.** (i) The equivalence of categories 4.1.1 of 1.17 respects by definition local (resp. semi-local)
isotriviality.

<!-- original page 244 -->

(ii) Add to the conditions of 4.1.1: `G` locally of finite presentation over `S`. Then the principal bundle `P` (or the
reductive group `G`) is locally isotrivial (resp. semi-locally isotrivial) if and only if for every `S' → S`, `S'` local
(resp. semi-local), `P_{S'}` is isotrivial (or `G_{S'}` isotrivial), that is to say, if there exists `S'' → S'` finite
surjective étale such that `P_{S''}` is trivial (or `G_{S''}` split).

(iii) In the case of tori, definition 4.1.2 coincides with that of Exp. IX, 1.1.

<!-- label: III.XXIV.4.1.3 -->

#### 4.1.4.

<!-- label: III.XXIV.4.1.4 -->

Recall (Exp. XXII, 4.3 and 6.2) that for every reductive group `G`, we have introduced the groups `rad(G)`, `corad(G)`
and `dér(G)`. The groups `rad(G)` and `corad(G)` are tori, which are split when `G` is split; moreover, there exists an
isogeny `rad(G) → corad(G)`. The `S`-group `dér(G)` is semisimple, one has `G / dér(G) = corad(G)`; it follows that for
every principal homogeneous bundle `P` under `G`, `P / dér(G)` is a principal homogeneous bundle under `corad(G)`. This
said, one has:

**Theorem 4.1.5.** *Let `S` be a scheme, `G` an `S`-reductive group of constant type.*

*(i) The following conditions are equivalent:*

*(a) `G` is locally (resp. semi-locally) isotrivial.*

*(b) The torus `rad(G)` is.*

*(b') The torus `corad(G)` is.*

*(c) The Galois covering of `S` associated to `G` (3.11) is.*

*If `T` is a maximal torus of `G`, these conditions are also equivalent to*

*(d) The torus `T` is locally (resp. semi-locally) isotrivial.*

*(ii) Let `P` be a principal homogeneous bundle under `G`; for `P` to be locally (resp. semi-locally) isotrivial, it is
necessary and sufficient that the `corad(G)`-principal bundle `P / dér(G)` be so.*

<!-- label: III.XXIV.4.1.5 -->

**Corollary 4.1.6.** *The conditions of (i) are satisfied when `G` is semisimple or when `S` is locally noetherian and
normal (or more generally geometrically unibranch). The conditions of (ii) are satisfied when `G` is locally (resp.
semi-locally) isotrivial.*

<!-- label: III.XXIV.4.1.6 -->

For (i), the first assertion is trivial from (b), the second follows from (c) and Exp. X, 5.14 and 5.15. For (ii), it
suffices to note that by virtue of theorem 90, a principal bundle under a split torus is semi-locally isotrivial.

### 4.2. Proof: the semisimple case

<!-- label: III.XXIV.4.2 -->

Let us first prove, for later reference:

**Proposition 4.2.1.** *Let `S` be a scheme, `G` an `S`-reductive group, `T` a maximal torus of `G` (resp. `B` a Borel
subgroup, resp. `B ⊃ T` a Killing couple of `G`), `P` a principal homogeneous bundle under `G`, `G'` the twisted form of
`G` associated to `P` (via the morphism `int : G → Aut_{S-gr.}(G)`). One has canonical isomorphisms*

```text
P / Norm_G(T) ⥲ Tor(G'),    P / B ⥲ Bor(G'),    P / T ⥲ Kil(G').
```

<!-- label: III.XXIV.4.2.1 -->

<!-- original page 245 -->

By construction, `G'` is the quotient of `P ×_S G` by a certain action of `G` (`((p, g')) g = (pg, g^{-1} g' g)`); one
therefore has a morphism `P ×_S G → G'`, that is, a morphism

```text
P → Hom_S(G, G'),
```

which, as one sees at once, factors through a morphism

```text
f : P → Isom_{S-gr.}(G, G'),
```

(to verify this assertion, one may assume `G = P`, in which case one has `G' = G`, `f = int`). The set-theoretic map
`p ↦ f(p)(T)` defines a morphism

```text
P → Tor(G').
```

To verify that this morphism induces an isomorphism `P / Norm_G(T) ⥲ Tor(G')` as announced, one may again assume `P = G`
in which case one is reduced to Exp. XXII, 5.8.3 (iii). (In fact, *loc. cit.* should be replaced by the statement
above.) One argues similarly for `Bor` and `Kil`.

**Proposition 4.2.2.** *Let `S` be a semi-local scheme, `G` an `S`-semisimple group of constant type.*

*(i) `G` is isotrivial.*

*(ii) Every principal bundle under `G` is isotrivial.*

<!-- label: III.XXIV.4.2.2 -->

Let us prove (i). Up to making a finite surjective étale extension of the base, one may, by 3.9.2, assume `G`
quasi-split. But then `G` is isotrivial by construction (3.11, the group `E` being finite). To prove (ii), one may, by
(i), assume `G` split; one is then reduced to:

**Lemma 4.2.3.** *Let `S` be a semi-local scheme. Every principal bundle under a split reductive group is isotrivial.*

<!-- label: III.XXIV.4.2.3 -->

Indeed, with the notation of 4.2.1, where `B ⊃ T` denotes the canonical Killing couple of the split `G`, the `S`-scheme
`Kil(G')` possesses a section, after finite surjective étale extension of the base, by 3.9.2. One may therefore reduce
the structure group of `G` to `T`; but `T` is split, so `H¹(S, T) = 0` (theorem 90).

**Corollary 4.2.4.** *Let `S` be a scheme and*

```text
1 → G → G' → G'' → 1
```

*an exact sequence of `S`-group schemes (for (fpqc)), `G` being semisimple of constant type. Let `P` be a principal
homogeneous bundle under `G'`, suppose the sheaf[^N.D.E-XXIV-24] `P / G` associated representable (for example `G''`
affine over `S`). For `P` to be locally isotrivial (resp. semi-locally isotrivial), it is necessary and sufficient that
`P / G` be so (as bundle under `G''`).*

<!-- label: III.XXIV.4.2.4 -->

<!-- original page 246 -->

If `P` is trivial, `P / G` is too, which shows that the condition is necessary. Conversely, suppose `S` local (resp.
semi-local) and `P / G` isotrivial, so trivialized by a finite surjective étale extension `S'` of `S`. Extending the
base to `S'`, one may reduce the structure group of `P_{S'}` to `G_{S'}`. But `S'` is still semi-local and `G_{S'}`
semisimple of constant type, so the obtained bundle is isotrivial (4.2.2).

### 4.3. Proof: general case.

<!-- label: III.XXIV.4.3 -->

Let us first note that 4.1.5 (ii) follows at once from the application of 4.2.4 to the exact sequence

```text
1 → dér(G) → G → corad(G) → 1.
```

Let us therefore prove (i). If `G` is split, `rad(G)` and `corad(G)` are split, as is `rev(G)`; so (a) implies (b),
(b'), and (c).

#### 4.3.1.

<!-- label: III.XXIV.4.3.1 -->

One has (c) ⇒ (a). Let `R` be the type of `G`; one has an exact sequence

```text
1 → ad(Ép_S(R)) → A_S(R) → E_S → 1.
```

Applying 4.2.4 to the bundle `P = Isom_{S-gr.}(Ép_S(R), G)` and to the associated bundle `rev(G) = P / ad(Ép_S(R))`, one
has (c) ⇒ (a).

#### 4.3.2.

<!-- label: III.XXIV.4.3.2 -->

One has (b) ⇒ (a). It suffices to prove that if `rad(G)` is split, `G` is semi-locally isotrivial. Now let
`G_0 = Ép_S(R)`; consider the category of pairs `(G', f)`, where `G'` is a form of `G_0` and `f` is an isomorphism of
`rad(G_0)` onto `rad(G)`.

One knows (2.16) that this category is equivalent to the category of principal homogeneous bundles under a certain
`S`-group `H` extension of a finite twisted constant group by a semisimple group. It suffices to prove that every
principal bundle under `H` is semi-locally isotrivial; this follows at once from 4.2.4.

#### 4.3.3.

<!-- label: III.XXIV.4.3.3 -->

One has (b') ⇒ (a). One can argue as previously (it will moreover be the same group `H` that arises). One can also see
that (b) and (b') are equivalent: a torus isogenous to a locally split torus is also locally split (cf. Exp. IX, 2.11
(iii)).

#### 4.3.4.

<!-- label: III.XXIV.4.3.4 -->

One has (d) ⇒ (a). It suffices to prove that a group of constant type possessing a split maximal torus is semi-locally
isotrivial; this follows at once from 2.14.

#### 4.3.5.

<!-- label: III.XXIV.4.3.5 -->

One has (a) ⇒ (d). It suffices to prove that a maximal torus of a split group is semi-locally isotrivial. More
precisely:

**Lemma 4.3.6.** *Let `S` be a semi-local scheme, `G` an `S`-reductive group, `T_0` a split maximal torus of `G`,
`W_0 = Norm_G(T_0) / T_0` (this is a locally constant `S`-group, constant if `G` is of constant type, by 2.14), `T` a
maximal torus of `G`.*

*There exists a morphism `S' → S` which is principal homogeneous under `W_0` (hence étale finite and surjective, and
even principal Galois if `G` is of constant type) such that `T_{S'}` is conjugate to `(T_0)_{S'}` by an element of
`G(S')` (and so in particular split).*

<!-- label: III.XXIV.4.3.6 -->

<!-- original page 247 -->

Indeed, one knows that `Transp_G(T_0, T)` is a principal homogeneous bundle under `Norm_G(T_0)` (cf. for example Exp.
XI, 5.4 bis). Set `S' = Transp_G(T_0, T) / T_0`; this is a principal homogeneous bundle under `W_0`. Extending the base
from `S` to `S'`, one can reduce the structure group of `Transp_G(T_0, T)` to `T_0`. Now `S'` is semi-local and `T_0`
split, so `Transp_G(T_0, T)` possesses a section over `S'`.[^N.D.E-XXIV-25] QED

### 4.4. Use of the existence of maximal tori

<!-- label: III.XXIV.4.4 -->

Using Grothendieck's existence theorem for maximal tori (Exp. XIV, 3.20), one can considerably sharpen the preceding
results. Let us state at once:

**Theorem 4.4.1.** *Let `S` be a semi-local scheme, `R` a pinned reduced root datum, `W` its Weyl group, `E` the group
of its automorphisms. (Recall that `E` operates naturally on `W` and that the semi-direct product `A = W · E` is
identified with the group of automorphisms of `R` non-pinned, cf. Exp. XXI, 6.7.2).*

*(i) Every principal homogeneous bundle under `Ép_S(R)` is trivialized by a principal Galois covering `S' → S` of group
`W`.*

*(ii) Let `G` be an `S`-reductive group of type `R`; let `rev(G) = Isomext(Ép_S(R), G)` be the associated Galois
covering of `S` with group `E`. Let `W_0` be the form of `W_S` associated to `rev(G)`. There exists a morphism `S' → S`,
which is a principal homogeneous bundle under `W_0`, such that `G_{S'}` is quasi-splittable (i.e. possesses a Borel
subgroup).*

*(iii) Every `S`-reductive group of type `R` is split by a principal Galois covering `S̃ → S` with group `A`.*

<!-- label: III.XXIV.4.4.1 -->

Let us first state:

**Proposition 4.4.2.** *Let `S` be a scheme, `G` an `S`-reductive group, `T` a maximal torus of `G`, `P` a principal
homogeneous bundle under `G`, `G'` the twisted form of `G` associated to `P` (one then has, cf. 4.2.1, a canonical
isomorphism `P / Norm_G(T) ⥲ Tor(G')`). Let `T'` be a maximal torus of `G'`, defining a composite morphism*

```text
S → Tor(G') ⥲ P / Norm_G(T).
```

*Consider the canonical morphisms*

```text
P → P/T → P / Norm_G(T)
```

*and take their inverse images by the preceding morphism:*

```text
   P  →  P/T  →  P / Norm_G(T)
   ↑      ↑           ↑
   H  →   S'  →       S.
```

<!-- original page 248 -->

*Then `S'` (resp. `H`) is a principal homogeneous bundle over `S` (resp. `S'`) under `W_G(T)` (resp. `T_{S'}`).
Moreover, if one makes `W_G(T)` operate on `T` in the obvious way, the bundle associated to `S'` is isomorphic to `T'`.*

<!-- label: III.XXIV.4.4.2 -->

The first two assertions are trivial, the last is proved like the corresponding assertion of 2.6.

**Corollary 4.4.3.** *Let `S` be a semi-local scheme, `G` an `S`-reductive group, `T` a maximal torus of `G`. Suppose
one of the two following conditions is satisfied:*

*(i) `T` is split.*

*(ii) `T` is contained in a Borel subgroup of `G`, and `G` is either adjoint, or simply connected.*

*Let moreover `P` be a principal homogeneous bundle under `G`. There exists an `S`-scheme `S'`, which is a principal
homogeneous bundle under `W_G(T)`, such that `P_{S'}` is trivial.*

<!-- label: III.XXIV.4.4.3 -->

Indeed, if `G'` is the form of `G` associated to `P`, then `G'` possesses a maximal torus `T'` (Exp. XIV, 3.20).
Resuming the notation of the preceding proposition, one sees that `H¹(S', T_{S'}) = 0` (by theorem 90 for (i), by 3.14
for (ii)). The morphism `H → S'` possesses a section, so `P_{S'}` also possesses a section over `S'`. QED

Let us now prove the theorem. Assertion (i) is a particular case of the preceding corollary (take `G = Ép_S(R)`, endowed
with its canonical split torus). Let us prove (ii). One knows (3.12) that `G` is an inner twisted form of

```text
G_0 = Q-Ép_{rev(G)/S}(R).
```

If `T_0` is the canonical maximal torus of `G_0`, `W_{G_0}(T_0)` is the group `W_0` described in the statement. The form
`G` of `G_0` corresponds to a principal homogeneous bundle `P` under `ad(G_0)` (`P = Isomint(G_0, G)`). The group
`W_{ad(G_0)}(T_0^{ad})` is canonically isomorphic to `W_0`, and one obtains the wanted result by applying 4.4.3 to the
situation `(ad(G_0), T_0^{ad}, P)`, hypothesis (ii) of 4.4.3 being well verified. Let us finally prove (iii). Resume the
notation of (ii); one has a diagram

```text
              rev(G)
              ↗     ↘
            E_S      W_0
              ↘     ↗
                S'
```

<!-- original page 249 -->

One knows that `G_{S'}` is isomorphic to `(G_0)_{S'}` and that `(G_0)_{rev(G)}` is splittable. If one sets
`S̃ = S' ×_S rev(G)`, `G_{S̃}` is splittable, and it only remains to verify that `S̃` is indeed a principal Galois
covering of `S` with group `A`, which follows from the following more general lemma (naturally valid in any site):

**Lemma 4.4.4.** *Let `S` be a scheme, `G` and `H` two `S`-group schemes, `G → Aut_{S-gr.}(H)` an action of `G` on `H`,
`E` a `G`-principal homogeneous bundle, `F` an `H_0`-principal homogeneous bundle, where `H_0` is the form of `H`
associated to `E`. Then `E ×_S F` is endowed naturally with a structure of principal homogeneous bundle under the
semi-direct product `H · G`.*

<!-- label: III.XXIV.4.4.4 -->

Write `(e, g) ↦ eg` (resp. `(f, u) ↦ f u`) for the action (on the right) of `G` on `E` (resp. of `H_0` on `F`). Write

```text
p : E ×_S H → H_0
```

for the canonical projection (`H_0` is by definition the quotient of `E ×_S H` by `G` acting on it by the formula
`(e, h) g = (eg, g^{-1} h g)`). Consider the morphism

```text
r : E ×_S F ×_S H ×_S G → E ×_S F
```

defined set-theoretically by

```text
r(e, f, h, g) = (eg, f · p(e, h)).
```

The morphism `r` indeed defines an action of the semi-direct product `H · G` on `E ×_S F`. Indeed, one has
set-theoretically

```text
r(r(e, f, h, g), h', g') = (egg', f p(e, h) p(eg, h'));
```

but

```text
p(e, h) p(eg, h') = p(e, h) p(e, g h' g^{-1}) = p(e, h g h' g^{-1}),
```

whence

```text
r(r(e, f, h, g), h', g') = r(e, f, h g h' g^{-1}, g g'),
```

which had to be proved.

To prove now that this law is indeed a law of principal homogeneous bundle, one may assume that `E` and `F` are trivial,
in which case one sees at once that `E ×_S F` is also a trivial bundle.

### 4.5. Isotriviality of maximal tori of semisimple groups[^N.D.E-XXIV-26]

<!-- label: III.XXIV.4.5 -->

Let us bring out here the following result, contained implicitly in 2.6 (cf. the N.D.E. (13)) and which was mentioned at
the end of Exp. IX 1.2. Recall (XXIII 5.11) that, for every scheme `S` and every reduced root datum `R`, one writes
`Ép_S(R)` for the unique pinned `S`-group of type `R` (which exists by Exp. XXV) and `T_S(R)` its canonical maximal
torus.

**Proposition 4.5.1.** *Let `G` be an `S`-semisimple group of constant type `R`; assume that `G` possesses a maximal
torus `T` (which is the case if `S` is semi-local, by XIV 3.20).*

*(i) Then `P = Isom_{S-gr.}(Ép_S(R), T_S(R); G, T) / T_S(R)_{ad}` is a principal `S`-bundle under the finite group
`Aut(R)`, and `T_P` is a split maximal torus of `G_P`. Consequently, `T` is isotrivial.*

*(ii) Moreover, for every finite set `F` of points of `P` contained in an affine open set, there exists an open set `U`
of `P` containing `F` such that `G_U` is split.*

<!-- label: III.XXIV.4.5.1 -->

<!-- original page 250 -->

*Proof.* The exact sequence

```text
1 → T_S(R)_{ad} → Aut_{S-gr.}(Ép_S(R), T_S(R)) → Aut_{S-gr.}(T_S(R))
```

induces for every `S' → S` a morphism of bundles `P_{S'} → Isom_{S'-gr.}(T_{S'}(R), T_{S'})`, so if `P_{S'}` possesses a
section, then `T_{S'}(R)` and `T_{S'}` are isomorphic. This is in particular the case for `S' = P`.

Note moreover that `Aut_{S-gr.}(Ép_S(R), T_S(R)) / T_S(R)_{ad}` is none other than the constant `S`-group `Aut(R)_S`,
and that `P` is identified with the `Aut(R)_S`-torsor `Isom(R, R̃(G, T))`, where `R̃(G, T)` denotes the twisted root
datum associated to `(G, T)` (cf. XXII 1.10).

Then (ii) follows from (i) and from 2.14, taking into account the fact that the `g_α` (`α` ranging over the roots of
`R`) are free `O_U`-modules of rank 1 on a sufficiently small affine open set `U` containing `F`.

## 5. Canonical decomposition of an adjoint or simply connected group

<!-- label: III.XXIV.5 -->

In this section, we shall use the results of no 1 to generalize to the case of schemes a classical decomposition of
adjoint (resp. simply connected) groups. So as not to overburden the exposition indefinitely, the proofs are sketched
and the details are left to the reader; in fact it is always a matter of absolutely standard proofs in the theory of
principal bundles: reduction of the structure group, twisting, etc.

### 5.1.

<!-- label: III.XXIV.5.1 -->

Recall (Exp. XXI, 7.4) that a Dynkin diagram is a disjoint union of its connected components, which are Dynkin diagrams.
Moreover, every non-empty connected Dynkin diagram corresponding to a root datum is isomorphic to one of the standard
diagrams (`A_n`, `B_n`, ..., `G_2`) which were exhibited in Exp. XXI, 7.4.6. In the sequel, we shall be interested only
in Dynkin diagrams whose connected components are of one of the preceding types. Let `T` be the set of these standard
diagrams. For every Dynkin diagram `D`, let `n(t) = n_D(t)` be the number of connected components of `D` isomorphic to
`t`, where `t ∈ T`. The *type* of `D` is by definition `∑_{t ∈ T} n_D(t) · t`.

A Dynkin diagram of type `t` is said to be *simple of type `t`*, a Dynkin diagram of type `n · t` is said to be
*isotypic of type `t`*. Let `D_0` be the set of connected components of `D` and let

```text
a : D_0 → T
```

be the obvious map. The type of `D` is none other than `∑_{x ∈ D_0} a(x)`.

### 5.2.

<!-- label: III.XXIV.5.2 -->

Let `S` be a scheme, `D` an `S`-Dynkin scheme (verifying the restrictive condition stated above). The cokernel of the
pair of morphisms `L ⇒ D` (`L =`[^N.D.E-XXIV-27] scheme of bonds of `D`) is written `D_0`. This is the "scheme of
connected components" of `D` (it

<!-- original page 251 -->

exists trivially when `D` is constant; the general case is deduced from this by descent); it is a finite twisted
constant `S`-scheme. One has a canonical morphism

```text
a : D_0 → T_S.
```

For `t ∈ T`, set `a^{-1}(t) = D_{0, t}`; this is a subscheme of `D_0`, whose inverse image in `D`, written `D_t`, is the
*isotypic component of type `t`* of the Dynkin scheme `D`. Each `D_t` is a subscheme of `D`, and one has

```text
D = ⨿_{t ∈ T} D_t.
```

Note that the degree of `D_{0, t}` at `s ∈ S` is `n(s, t)`, if the type of `D` at `s` is `∑_t n(s, t) · t`.

### 5.3.

<!-- label: III.XXIV.5.3 -->

In what follows, we shall consider only semisimple adjoint (resp. simply connected) groups. To simplify the language, we
shall state the results for adjoint groups; all statements will remain valid if one substitutes everywhere "simply
connected" for "adjoint".

Recall that an adjoint reduced root datum is determined up to isomorphism by the type of its Dynkin diagrams. We shall
therefore say that an adjoint root datum `R` (resp. a semisimple adjoint group `G`) is *of type `∑ n(t) · t`* if its
Dynkin diagrams are (resp. if its type is given by an adjoint root datum of type `∑ n(t) · t`). We shall say that `R` or
`G` is *simple of type `t`* (resp. *isotypic of type `t`*) if its type is `t` (resp. `n · t`, `n > 0`).

If `G` is a semisimple adjoint group, we shall use the symbols `Dyn_0(G)` and `Dyn_{0, t}(G)` in the sense defined in
5.2.

### 5.4.

<!-- label: III.XXIV.5.4 -->

Let `t_i`, `i = 1, 2, ..., n`, be distinct elements of `T`, and let `R_i` be a pinned adjoint root datum isotypic of
type `t_i`. Consider the product `R = R_1 × ··· × R_n` (Exp. XXI, 6.4.1). Let `S` be a scheme such that the different
`Ép_S(R_i)` exist (cf. Exp. XXV). One verifies at once that there exists a canonical isomorphism

```text
(*)    Ép_S(R) = Ép_S(R_1) ×_S ··· ×_S Ép_S(R_n).
```

<!-- original page 252 -->

Moreover, if `E_i` denotes the group of automorphisms of `R_i`, `E` the group of automorphisms of `R`, `D_i` (resp. `D`)
the Dynkin diagram of `R_i` (resp. `R`), one has isomorphisms:

```text
E_i ≃ Aut(D_i),    D = ⨿ D_i,    E ≃ ∏ E_i ≃ Aut(D).
```

Combining with (\*) and 1.4, one sees that (\*) induces an isomorphism

```text
A_S(R) ≃ A_S(R_1) ×_S ··· ×_S A_S(R_n).
```

**Proposition 5.5.** *Let `S` be a scheme, `G` an `S`-semisimple adjoint group. There exists a unique decomposition*

```text
G ≃ ∏_{t ∈ T} G_t,
```

*where `G_t` is an `S`-semisimple adjoint group isotypic of type `t`. Moreover, the preceding decomposition induces
isomorphisms*

```text
Dyn_t(G) ≃ Dyn(G_t),    Aut_{S-gr.}(G) ≃ ∏_{t ∈ T} Aut_{S-gr.}(G_t).
```

<!-- label: III.XXIV.5.5 -->

This has indeed been proved above when `G` is split. In the general case, one may assume `G` of constant type `R`. Using
the preceding decomposition of `A_S(R)` and 1.17, one deduces the wanted decomposition of `G`. The other results are
then proved by descent.

**Remark 5.6.** More generally, if `G` and `H` are two semisimple adjoint groups, one has canonical isomorphisms as
follows (the diagram is commutative):

```text
Isom_{S-gr.}(G, H)            ⥲    ∏_{t ∈ T} Isom_{S-gr.}(G_t, H_t)
       ↓                                              ↓
Isomext(G, H)                  ⥲    ∏_{t ∈ T} Isomext(G_t, H_t)
       ≀                                              ≀
       ↓                                              ↓
Isom_{Dyn}(Dyn(G), Dyn(H))    ⥲    ∏_{t ∈ T} Isom_{Dyn}(Dyn(G_t), Dyn(H_t)).
```

<!-- label: III.XXIV.5.6 -->

**Remark 5.7.** One can give an intrinsic characterization of `G_t`, which we state below without proof: it is the
largest reductive subgroup of `G` invariant (and moreover characteristic) and isotypic of type `t`.

<!-- label: III.XXIV.5.7 -->

The preceding proposition allows one to reduce the study of semisimple adjoint groups to that of isotypic semisimple
adjoint groups. It is this study that we shall now undertake.

### 5.8.

<!-- label: III.XXIV.5.8 -->

Let `R` be a pinned reduced adjoint simple root datum of type `t`, `I` a nonempty finite set, `R^I` the product root
datum of copies `R_i` of `R`, for `i ∈ I`. Write `E` for the group of automorphisms of `R`, which is identified with the
group of automorphisms of the Dynkin diagram `D` of `R`. The Dynkin diagram of `R^I` is identified with `D^I`, which
shows that one has an exact sequence:

```text
1 → Aut(D)^I → Aut(D^I) → Aut(I) → 1,
```

where `Aut(I)` denotes the group of permutations of `I`. It follows that the canonical isomorphism

```text
Ép_S(R)^I ≃ Ép_S(R^I)
```

induces an exact sequence

```text
1 → A_S(R)^I → A_S(R^I) → Aut(I_S) → 1,
```

the last group being the `S`-constant group associated to `Aut(I)`. Note moreover that `I` is canonically identified
with the set of connected components of `D^I`.

<!-- original page 253 -->

<!-- original page 254 -->

If `G` is an `S`-semisimple group of type `R^I`, defining (cf. 1.17) a principal homogeneous bundle `P` under
`A_S(R^I)`, the definition of `Dyn(G)` by descent (3.7), and that of `Dyn_0(G)` (5.2), shows that the bundle associated
to `P` by the morphism `A_S(R^I) → Aut(I_S)` is none other than `Isom_S(I_S, Dyn_0(G))`, corresponding to the form
`Dyn_0(G)` of `I_S`. Using again the equivalence of categories 1.17 and the preceding exact sequence, one deduces by a
formal argument that there exists a `Dyn_0(G)`-reductive group of type `R`, say `G_0`, and an `S`-isomorphism
`G ≃ ∏_{Dyn_0(G)/S} G_0`.

**Proposition 5.9.** *Let `S` be a scheme, `G` an `S`-semisimple adjoint group isotypic of type `t`. There exist a
`Dyn_0(G)`-semisimple adjoint group `G_0` simple of type `t`, and an `S`-isomorphism (unique)*

```text
G ≃ ∏_{Dyn_0(G)/S} G_0.
```

*Moreover, this isomorphism induces an exact sequence*

```text
1 → ∏_{Dyn_0(G)/S} Aut_{S-gr.}(G_0) → Aut_{S-gr.}(G) → Aut_S(Dyn_0(G)) → 1.
```

<!-- label: III.XXIV.5.9 -->

One may evidently assume `G` of constant type `n · t`. The first assertion has already been proved (the uniqueness
assertion is evident). The second is then deduced from the split case by descent.

One can combine 5.5 and 5.9:

**Proposition 5.10.** *Let `S` be a scheme, `G` an `S`-semisimple adjoint group, `D = Dyn(G)` its Dynkin scheme.*

*(i) There exists a canonical decomposition*

```text
G ≃ ∏_{t ∈ T} ∏_{D_{0, t}/S} G_{0, t} ≃ ∏_{Dyn_0(G)/S} G_0,
```

*where each `G_{0, t}` is a `Dyn_{0, t}(G)`-simple adjoint group of type `t` (resp. where `G_0` is a
`Dyn_0(G)`-semisimple adjoint group whose type at `x ∈ Dyn_0(G)` is `a(x) ∈ T` (the morphism `a : Dyn_0(G) → T_S` was
defined in 5.2)).*

*(ii) The preceding decompositions induce isomorphic exact sequences (written vertically), where `Aut_{S, a}(D_0)`
denotes the scheme of automorphisms of `Dyn_0(G)` which commute with the morphism `a : Dyn_0(G) → T_S`:*

<!-- original page 255 -->

```text
                  1                              1
                  ↓                              ↓
   ∏_{t ∈ T} ∏_{D_{0, t}/S} Aut_gr.(G_{0, t}) ⥲ ∏_{Dyn_0(G)/S} Aut_gr.(G_0)
                  ↓                              ↓
        Aut_{S-gr.}(G)                    →     Aut_{S-gr.}(G)
                  ↓                              ↓
   ∏_{t ∈ T} Aut_S(Dyn_{0, t}(G))           ⥲  Aut_{S, a}(Dyn_0(G))
                  ↓                              ↓
                  1                              1
```

<!-- label: III.XXIV.5.10 -->

**Corollary 5.11.** *Under the preceding conditions, the three following categories are equivalent:*

*(i) the category of principal homogeneous bundles under `G`.*

*(ii) the category of principal homogeneous bundles under `G_0`.*

*(iii) the product category, for `t ∈ T`, of the categories of principal homogeneous bundles under the `G_{0, t}`.*

<!-- label: III.XXIV.5.11 -->

This is deduced formally from the preceding decompositions and from 8.4.

**Corollary 5.12.** *One has canonical isomorphisms*

```text
Tor(G) ≃ ∏_{t ∈ T} ∏_{D_{0, t}/S} Tor(G_{0, t}) ≃ ∏_{Dyn_0(G)/S} Tor(G_0),
```

*and similarly replacing `Tor` by `Bor` (resp. `Kil`).*

<!-- label: III.XXIV.5.12 -->

Trivial starting from the split case.

**Remark 5.13.** The canonical morphism

```text
Dyn(G) → Dyn_0(G)
```

allows one to consider `Dyn(G)` as a `Dyn_0(G)`-Dynkin scheme; in fact it is the Dynkin scheme `Dyn(G_0)` of `G_0`.

Similarly if `T ⊂ B` is a Killing couple of `G`, corresponding canonically to the Killing couple `T_0 ⊂ B_0` of `G_0`,
one verifies that the obstructions to the quasi-splitting of `G` and `G_0`, which lie (3.9) in
`Pic(Dyn(G)) = Pic(Dyn(G_0))` coincide. One deduces:

<!-- label: III.XXIV.5.13 -->

**Corollary 5.14.** *The following conditions are equivalent:*

*(i) `G` is quasi-splittable,*

<!-- original page 256 -->

*(ii) `G_0` is quasi-splittable,*

*(iii) each `G_{0, t}`, `t ∈ T`, is quasi-splittable.*

<!-- label: III.XXIV.5.14 -->

## 6. Automorphisms of Borel subgroups of reductive groups

<!-- label: III.XXIV.6 -->

**Lemma 6.1.** *Let `S` be a scheme, `(G, T, M, R)` a split `S`-group, `Δ` a system of simple roots of `R`, and `B` the
corresponding Borel subgroup. Then `B_u` is generated as (fppf) group sheaf by the `U_α`, `α ∈ Δ`.*

<!-- label: III.XXIV.6.1 -->

Let `H` be the group subsheaf of `B_u` generated by the `U_α`, `α ∈ Δ`. Let us prove `H ⊃ U_β` (`β ∈ R^+`) by induction
on the integer `ord(β) = ord_Δ(β) > 0` (cf. Exp. XXI, 3.2.15). The assertion is verified by hypothesis for `ord(β) = 1`.
Suppose then `ord(β) > 1` and `U_γ ⊂ H` as soon as `ord(γ) < ord(β)`. There exists `α ∈ Δ` such that `β − α ∈ R^+` (Exp.
XXI, 3.1.1). Let `p` be the largest integer such that `β − p α = β' ∈ R^+`. One has `U_α, U_{β'} ⊂ H`, `β' − α ∉ R`. One
is therefore reduced to proving:

**Lemma 6.2.** *Resume the notation of Exp. XXIII, 6.4. Suppose `p = 1`, that is, `β − α` not a root. If `H` is a group
subsheaf of `B_u` such that `U_α, U_β ⊂ H`, then `U_{iα + jβ} ⊂ H` whenever `iα + jβ ∈ R`, `i > 0`, `j > 0`.*

<!-- label: III.XXIV.6.2 -->

Let us distinguish four cases according to the value of `q = 0, 1, 2, 3`. In the sequel `x` and `y` denote two arbitrary
sections of `G_{a, S'}`, `S' → S`.

If `q = 0`, there is nothing to prove.

<!-- original page 257 -->

If `q = 1`, one has `p_{α+β}(±x) = p_β(−y) p_α(−x) p_β(y) p_α(x) ∈ H(S')`, so `U_{α+β} ⊂ H`.

If `q = 2`, one similarly has

```text
p_{α+β}(±xy) p_{2α+β}(±x²y) = p_β(−y) p_α(−x) p_β(y) p_α(x) ∈ H(S'),
```

whence, up to changing certain signs,

```text
F(x, y) = p_{α+β}(xy) p_{2α+β}(x²y) ∈ H(S').
```

Since `p_{α+β}` and `p_{2α+β}` commute, one then has `F(x, 1) F(1, −x) = p_{2α+β}(x² − x)`.[^N.D.E-XXIV-28] If
`a ∈ G_a(S)`, the equation `X² − X = a` defines a free surjective extension of `S` (this is `Spec O_S[X]/(X² − X − a)`);
one therefore has `p_{2α+β}(a) ∈ H(S')` so `U_{2α+β} ⊂ H`, hence also `U_{α+β} ⊂ H` (since `F(1, a) ∈ H(S')`).

If `q = 3`, one similarly has

```text
F(x, y) = p_{α+β}(xy) p_{2α+β}(x²y) p_{3α+β}(x³y) p_{3α+2β}(x³y²) ∈ H(S');
```

and since

```text
p_{3α+2β}(±x) = F(1, 1)^{-1} p_β(−x) F(1, 1) p_β(x) ∈ H(S'),
```

one obtains that `U_{3α+2β} ⊂ H` and so

```text
K(x, y) = p_{α+β}(xy) p_{2α+β}(x²y) p_{3α+β}(x³y) ∈ H(S').
```

Computing then

```text
K(x + y, 1) K(−x, 1) K(1, y)^{-1}
```

modulo `U_{3α+2β}`, one finds

```text
p_{2α+β}(2x² + y² + 2xy − y) p_{3α+β}(y³ + 3xy² + 3x²y − y) ∈ H(S').
```

If `a ∈ G_a(S)`, the "equations"

```text
x² = −xy − y + 1 − a
y² = 3y − 2 + 3a
```

define a free surjective extension of `S`; one then has `y³ + 3xy² + 3x²y − y = 0` and the preceding expression gives
`p_{2α+β}(a) ∈ H(S')`.[^N.D.E-XXIV-29] One has thus proved that `H` contains `U_{2α+β}` and `U_{3α+2β}` and that

<!-- original page 258 -->

```text
E(x, y) = p_{α+β}(xy) p_{3α+β}(x³y) ∈ H(S').
```

Since `p_{α+β}(xy)` and `p_{3α+β}` commute, one is reduced to the preceding computation, i.e.
`E(1, x) E(1, −x) = p_{3α+β}(x³ − x)`, whence `U_{3α+β} ⊂ H`, then `U_{α+β} ⊂ H`.

**Remark 6.2.1.** The preceding proof shows that one could have replaced the hypothesis "`H` contains `U_α` and `U_β`"
by "`H` contains `U_α` or `U_β`, and `H` is invariant under `int(U_α)` and `int(U_β)`".

<!-- label: III.XXIV.6.2.1 -->

**Theorem 6.3.** *Let `S` be a scheme, `G` and `G'` two `S`-semisimple groups, `B` (resp. `B'`) a Borel subgroup of `G`
(resp. `G'`). Every isomorphism `B ⥲ B'` is induced by a unique isomorphism `G ⥲ G'`.*

<!-- label: III.XXIV.6.3 -->

The assertion is local for the étale topology and one may assume `G` split: `G = (G, T, M, R)`, `B` being defined by the
system of positive roots `R^+` of `R`. The given isomorphism `u : B ⥲ B'` induces an isomorphism of `T` onto a maximal
torus `T'` of `B'`, hence of `G'`. The given isomorphism `T ≃ D_S(M)` gives an isomorphism `T' ≃ D_S(M)` in which the
elements of `R^+` become the constant roots of `B'` with respect to `T'`, hence the elements of `R` the constant roots
of `G'` with respect to `T'`. Since `G` and `G'` are semisimple, the coroots are determined by duality (Exp. XXI,
1.2.5), which proves that `(T', M, R)` is a splitting of `G'` such that `R(G) = R(G')`.

Applying Exp. XXIII, 5.1 (uniqueness theorem), one deduces that there exists a unique isomorphism `G ⥲ G'` coinciding
with `u` on `T` and the `U_α`, `α ∈ Δ`. By 5.1, the restriction of this isomorphism to `B` is `u`. QED

**Remark 6.3.1.** (i) Using Exp. XXII, 4.1.9 and arguing as in *loc. cit.* 4.2.12, one can in the statement of the
theorem replace "isomorphism" by "isogeny" (resp. "central isogeny").

(ii) The theorem is false for reductive groups. Take for example `G = G' = SL_2 × G_m` identified with the group of
matrices below:

```text
{ ( a b 0 )
  ( c d 0 ) : ad − bc = 1, h invertible };
  ( 0 0 h ) 
```

<!-- original page 259 -->

take for `B = B'` the Borel subgroup defined by `c = 0` and for `u` the automorphism of `B` below:
`u(a, b, d, h) = (a, b, d, ah)`.

<!-- label: III.XXIV.6.3.1 -->

**Corollary 6.4.** *The functor `(G, B) ↦ B` from the category formed by pairs `(G, B)`, where `G` is an `S`-semisimple
group and `B` a Borel subgroup of `G`, to the category of `S`-group schemes (morphisms being isomorphisms) is fully
faithful.*

<!-- label: III.XXIV.6.4 -->

**Corollary 6.5.** *Let `S` be a scheme, `G` an `S`-semisimple group, `B` a Borel subgroup of `G`, `B'` an `S`-group
locally isomorphic to `B` for (fpqc). Then `B'` is locally isomorphic to `B` for the local finite étale
topology[^N.D.E-XXIV-30] and there exists an `S`-semisimple group `G'` of which `B'` is a Borel subgroup; `G'` is unique
up to a unique isomorphism inducing the identity on `B'`.*

<!-- label: III.XXIV.6.5 -->

**Corollary 6.6.** *Let `S` be a scheme, `G` an `S`-semisimple group, `B` a Borel subgroup of `G`. Then `Aut_{S-gr.}(B)`
is representable by an affine and smooth `S`-scheme, `Autext(B)` is representable by an étale and finite `S`-scheme, and
the obvious morphisms induce an isomorphism of exact sequences*

```text
1 → B_ad → Aut_{S-gr.}(G, B) → Autext(G) → 1
        ≀         ≀                ≀
1 → B_ad → Aut_{S-gr.}(B) → Autext(B) → 1.
```

<!-- label: III.XXIV.6.6 -->

This follows at once from 2.1 and from the preceding results. The reader is left the task of developing the analogues of
the results of nos 1, 2, 3, 4 in the framework above.

**Remark 6.7.** If `S` is a scheme and `B` an `S`-group, `B` can therefore be a Borel subgroup only of a unique
semisimple group, well determined by `B`. It therefore remains to characterize the `S`-groups `B` that are Borel
subgroups of semisimple groups.[^N.D.E-XXIV-31]

<!-- label: III.XXIV.6.7 -->

<!-- original page 260 -->

## 7. Representability of the functors `Hom_{S-gr.}(G, H)`, for `G` reductive

<!-- label: III.XXIV.7 -->

### 7.1. The split case

<!-- label: III.XXIV.7.1 -->

#### 7.1.1.

<!-- label: III.XXIV.7.1.1 -->

Let `S` be a scheme, `G` a pinned `S`-group, `T` its maximal torus, `Δ` the set of simple roots and, for `α ∈ Δ`,

```text
u_α ∈ U_α^×(S),    w_α ∈ Norm_G(T)(S),
```

the elements defined by the pinning.

Let on the other hand `H` be an `S`-group scheme; we are interested in the functor `Hom_{S-gr.}(G, H)`, and more
precisely in the morphism

```text
q : Hom_{S-gr.}(G, H) → Hom_{S-gr.}(T, H).
```

Let then

```text
f_T : T → H
```

be a morphism of `S`-groups; consider `q^{-1}(f_T) = F`. This is the functor defined by

```text
F(S') = { f ∈ Hom_{S'-gr.}(G_{S'}, H_{S'}) | f = (f_T)_{S'} on T_{S'} }.
```

One has a morphism of `S`-functors

```text
i : F → H^{2n},
```

where `n = Card(Δ)`, defined set-theoretically by `i(f) = (f(u_α), f(w_α))_{α ∈ Δ}`. By Exp. XXIII, 1.9, `i` is moreover
a monomorphism.

**Proposition 7.1.2.** *If `H` is separated over `S`, `F` is representable and `i` is a closed immersion.*

<!-- label: III.XXIV.7.1.2 -->

The usual technique of relative representability[^N.D.E-XXIV-32] shows us that it suffices to prove that, given sections

```text
v_α, h_α ∈ H(S),    for α ∈ Δ,
```

the `S`-schemes `S'` such that there exists an `S'`-homomorphism

```text
f : G_{S'} → H_{S'}
```

extending `(f_T)_{S'}` and verifying `f(u_α) = v_α`, `f(w_α) = h_α`, are exactly those that factor through a certain
closed subscheme of `S`. One may evidently assume `S` affine.

To simplify the sequel, let us say that a morphism `Y → X`[^N.D.E-XXIV-33] of affine schemes verifies condition (L) if
`Y` is the spectrum of an `O(X)`-algebra which is a free `O(X)`-module. It is clear that if one restricts to the
category of affine schemes, a product, or a composite of morphisms verifying (L) verifies (L), and that (L) is stable
under base change.

**Lemma 7.1.3.** *Suppose `S` affine, and let `α ∈ Δ`. Consider the morphism*

```text
a : T ×_S T → G_{a, S}
```

*defined set-theoretically by `a(t, t') = α(t) + α(t')`.*

<!-- original page 261 -->

*(i) `a` is faithfully flat and of finite presentation.*

*(ii) Let `R` be the fibered square of `a`. The structure morphism `R → S` verifies (L).*

<!-- label: III.XXIV.7.1.3 -->

It is first clear that the morphism `a` is surjective, since `α : T → G_{m, S}` is. It is trivial that `a` is of finite
presentation. Since `α` verifies (L), it suffices, to prove (i) and (ii), to show that the morphism

```text
u : G_{m, S}² → G_{a, S}
```

defined set-theoretically by `u(x, y) = x + y` verifies (L). In other words, it suffices to verify that for every ring
`A`, the ring `A[X, Y, X^{-1}, Y^{-1}]` is a free module over its subring `A[X + Y]`.[^N.D.E-XXIV-34] Now `A[X, Y]` is a
free module with basis `{1, X}` over the subring `B = A[X + Y, XY]` (one has `X² − (X + Y) X + XY = 0`), so
`A[X^{±1}, Y^{±1}] = A[X, Y]_{XY}` is free over `B_{XY} = A[X + Y, (XY)^{±1}]` with basis `{1, X}`, and free over
`A[X + Y]` with basis the elements `(XY)^p` and `X(XY)^p`, for `p ∈ ℤ`.

**Lemma 7.1.4.** *Let `α ∈ Δ`, and let `b : T ×_S T → H` be the morphism defined set-theoretically by*

```text
b(t, t') = int(f_T(t)) v_α · int(f_T(t')) v_α.
```

*Let `f_α : U_α → H` be an `S`-morphism. The following conditions are equivalent:*[^N.D.E-XXIV-35]

*(i) `f_α` is a morphism of groups; one has `f_α(u_α) = v_α` and*

```text
f_T(t) f_α(x) f_T(t)^{-1} = f_α(α(t) x)
```

*for all `t ∈ T(S')`, `x ∈ U_α(S')`, `S' → S`.*

*(ii) One has `f_α(u_α) = v_α` and the relation*

```text
f_α(a(t, t') u_α) = b(t, t')
```

*for all `t, t' ∈ T(S')`, `S' → S`.*

<!-- label: III.XXIV.7.1.4 -->

If `f_α` verifies (i), one has `f_α(α(t) u_α) = int(f_T(t)) v_α`, which entails (ii) at once. Conversely, suppose (ii)
verified and let us prove the various conditions of (i); let us first prove the last. Since `a` is covering for (fpqc),
it suffices to prove that if `t, t', t'' ∈ T(S')`, one has

```text
f_T(t) f_α(a(t', t'') u_α) f_T(t)^{-1} = f_α(α(t) a(t', t'') u_α);
```

<!-- original page 262 -->

now this also reads

```text
f_T(t) b(t', t'') f_T(t)^{-1} = b(t t', t t''),
```

an evident property from the definition of `b`. It remains to prove that `f_α` is a morphism of groups. Now the
preceding property gives at once

```text
f_α(α(t) u_α) f_α(α(t') u_α) = (f_T(t) f_α(u_α) f_T(t)^{-1}) · (f_T(t') f_α(u_α) f_T(t')^{-1})
                              = b(t, t') = f_α(α(t) u_α + α(t) α(t') u_α).
```

One therefore has `f_α(x + x') = f_α(x) f_α(x')`, whenever `x` and `x'` are sections of the open subset `U_α^×` of
`U_α`, which is schematically dense; one concludes then by Exp. XVIII, 1.4.

#### 7.1.5.

<!-- label: III.XXIV.7.1.5 -->

Let us fix provisionally an `α ∈ Δ`. The morphism `a` is faithfully flat quasi-compact, so `G_{a, S}` is identified with
the quotient of `T ×_S T` by the equivalence relation `R` defined by `a`. Let

```text
R ⇉^{i_1}_{i_2} T ×_S T
```

be this equivalence relation.

For the morphism `b` to factor through `a`,[^N.D.E-XXIV-36] it is necessary and sufficient that `b ∘ i_1 = b ∘ i_2`;
that is, if one writes `K` for the kernel of the pair of morphisms

```text
R ⇉^{b ∘ i_1}_{b ∘ i_2} H,
```

it is necessary and sufficient that `K = R`. Now `H` is assumed separated over `S`, so `K` is a closed subscheme of `R`.
Recall, on the other hand, that `R` is essentially free over `S` (7.1.3).

#### 7.1.6.

<!-- label: III.XXIV.7.1.6 -->

By the foregoing, if `S'` is an `S`-scheme, for there to exist over `S'` an `f_α` verifying the conditions of 7.1.4 (i)
(and then necessarily unique), it is necessary and sufficient that `K_{S'} = R_{S'}`, and that the morphism `f_α`
obtained verify `f_α(u_α) = v_α`.

The first condition is equivalent to the fact that `S' → S` factors through a certain closed subscheme of `S` (Exp.
VIII, 6.4[^N.D.E-XXIV-37]); if one replaces `S` by this closed subscheme, the second condition defines once again a
closed subscheme of `S` (equality of two sections of `H`, now `H` is assumed separated over `S`).

Up to replacing `S` by this closed subscheme, one may therefore assume that there exists a morphism `f_α : U_α → H`
verifying the conditions of 7.1.4 (i). Taking the intersection of the subschemes of `S` obtained for each `α ∈ Δ`, one
may assume this condition verified for every `α ∈ Δ`.

#### 7.1.7.

<!-- label: III.XXIV.7.1.7 -->

Similarly, consider for each `α ∈ Δ` the two morphisms of `S`-groups

```text
f_T ∘ int(w_α), int(h_α) ∘ f_T : T → H.
```

Since `H` is separated over `S` and `T` essentially free over `S`, the same reasoning as previously shows that, up to
replacing `S` by a closed subscheme, one may assume that for every `α ∈ Δ` one has

```text
f_T ∘ int(w_α) = int(h_α) ∘ f_T.
```

#### 7.1.8.

<!-- label: III.XXIV.7.1.8 -->

Using now the theorem of generators and relations (Exp. XXIII, 3.5), one sees that there exists a homomorphism of groups
`f : G → H` verifying the required conditions if and only if a certain finite set of algebraic relations between the
sections `h_α, v_α, f_T(α^*(−1))` (`α ∈ Δ`) of `H` is satisfied:

<!-- original page 263 -->

```text
R_i( (h_α)_α, (v_α)_α, (f_T(α^*(−1)))_α ) = e,    i = 1, ..., n.
```

Since `H` is separated over `S`, this defines once again a closed subscheme of `S`, and one is done.

**Corollary 7.1.9.** *Let `S` be a scheme, `G` a split `S`-reductive group, `T` its maximal torus, `H` an `S`-group
scheme separated over `S`. Let further `P` be a property of morphisms such that:*

*(i) A closed immersion verifies `P`.*

*(ii) The composite of two morphisms verifying `P` also verifies `P`.*

*(iii) `P` is stable under base change.*

*(iv) The structure morphism `H → S` verifies `P`.*

*Then the canonical morphism*

```text
Hom_{S-gr.}(G, H) → Hom_{S-gr.}(T, H)
```

*is relatively representable by a separated morphism verifying `P`.*[^N.D.E-XXIV-38]

<!-- label: III.XXIV.7.1.9 -->

Indeed, one may assume `G` pinned; the structure morphism `H^{2n} → S` verifies `P` and one concludes by 7.1.2.

**Corollary 7.1.10.** *Let `S` be a scheme, `G` a split `S`-reductive group, and `H` an `S`-group scheme smooth and with
affine fibers.[^N.D.E-XXIV-39] Then the functor `Hom_{S-gr.}(G, H)` is representable by an `S`-scheme locally of finite
presentation and separated over `S`.*

<!-- label: III.XXIV.7.1.10 -->

Indeed, since `H` is smooth over `S`, one can consider its neutral component `H⁰`, which has affine fibers, is smooth,
separated and of finite presentation over `S` (Exp. VI_B, 3.10 and 5.5). Since `G` has connected fibers, one may replace
`H` by `H⁰`. Since `G` and `H` are then of finite presentation, one may assume `S` noetherian, and one applies 7.1.9
taking for `P` the property "of finite type". But, by Exp. XV, 8.9, one knows that `Hom_{S-gr.}(T, H)` is representable
by a separated `S`-scheme locally of finite type.

**Remark 7.1.11.** If `H` is affine over `S`, one can replace the reference to Exp. XV by Exp. XI, 4.2.

<!-- label: III.XXIV.7.1.11 -->

### 7.2. General case

<!-- label: III.XXIV.7.2 -->

**Proposition 7.2.1.** *Let `S` be a scheme, `G` an `S`-reductive group, `T` a maximal torus of `G`. Let on the other
hand `H` be an `S`-group scheme, such that the structure morphism `H → S` verifies the following condition:*

*(+) Each point `s ∈ S` possesses an open neighborhood `U` such that the morphism `H_U → U` is quasi-projective.*

*Then the canonical morphism*

```text
Hom_{S-gr.}(G, H) → Hom_{S-gr.}(T, H)
```

*is relatively representable by a morphism verifying (+).*

<!-- label: III.XXIV.7.2.1 -->

<!-- original page 264 -->

When `G` is splittable relative to `T`, one applies 7.1.9 taking for `P` the property (+) above. When `G` is locally
isotrivial, for example semisimple (4.2.2), one notes that the assertion of the theorem is local for the local finite
étale topology (indeed, the property of being quasi-projective is local for the global finite étale topology and ensures
the effectiveness of descent for this topology, cf. SGA 1, VIII, 7.7). Finally, in the general case, one uses the
following lemma:

**Lemma 7.2.2.** *Let `S` be a scheme, `G` an `S`-reductive group, `T` a maximal torus of `G`, `G'` the derived group of
`G` (Exp. XXII, 6.2), `T' = T ∩ G'` the maximal torus of `G'` corresponding to `T` (Exp. XXII, 6.2.8). Then the diagram*

```text
G ← G'
↑    ↑
T ← T'
```

*is an amalgamated sum in the category of `S`-group sheaves: that is, for every `S`-group sheaf `H`, the following
square is cartesian:*

```text
Hom_{S-gr.}(G, H)  →  Hom_{S-gr.}(G', H)
        ↓                    ↓
Hom_{S-gr.}(T, H)  →  Hom_{S-gr.}(T', H).
```

<!-- label: III.XXIV.7.2.2 -->

Indeed, if `rad(G)` is the radical of `G`, then `rad(G) ⊂ T`, so

```text
rad(G) ∩ G' = rad(G) ∩ T' = K,
```

and the product in `G` induces isogenies (Exp. XXII, 6.2)

```text
i : G' ×_S rad(G) → G,    j : T' ×_S rad(G) → T.
```

Let `f_{G'} : G' → H`, `f_T : T → H`, and `f_{T'} : T' → H` be morphisms of `S`-groups such that
`f_{G'}|_{T'} = f_T|_{T'} = f_{T'}`. Let us show that there exists a unique morphism of `S`-groups `f : G → H` inducing
`f_{G'}` and `f_T`. Let `f_{rad} = f_T|_{rad(G)}`[^N.D.E-XXIV-40] and let

```text
f_1 = f_{G'} · f_{rad} : G' ×_S rad(G) → H.
```

For `f` to exist (and it will evidently be unique), it is necessary and sufficient that `f_1` induce the identity on the
kernel of `i`, that is, that `f_{G'}` and `f_{rad}` coincide on `K`; but the existence of `f_T` shows by the same
argument that `f_{T'}` and `f_{rad}` coincide on `K`. It only remains to note that `f_{G'}` and `f_{T'}` evidently
coincide on `K ⊂ T'`.

Arguing now as in 7.1.10, one deduces from 7.2.1:

**Corollary 7.2.3.** *Let `S` be a scheme, `G` an `S`-reductive group, `H` an `S`-group scheme smooth and
quasi-projective over `S` with affine fibers. Then `Hom_{S-gr.}(G, H)` is representable by an `S`-scheme locally of
finite presentation and separated over `S`.*

<!-- label: III.XXIV.7.2.3 -->

### 7.3. Phenomena specific to characteristic 0

<!-- label: III.XXIV.7.3 -->

If `G` and `H` are two smooth `S`-groups, `g` and `h` their Lie algebras, one has a canonical morphism

```text
Lie : Hom_{S-gr.}(G, H) → Hom_{O_S\text{-Lie alg.}}(g, h),
```

where the right-hand side has an obvious definition.

<!-- original page 265 -->

**Proposition 7.3.1.** *Let `S` be a scheme of characteristic 0 (i.e. a `ℚ`-scheme), `G` an `S`-reductive group, `H` an
`S`-group scheme smooth and quasi-projective over `S` with affine fibers.*

*(i) `Hom_{S-gr.}(G, H)` is representable by a smooth and separated `S`-scheme over `S`.*

*(ii) If `G` is semisimple, this scheme is affine and of finite presentation over `S`.*

*(iii) If `G` is simply connected (Exp. XXII, 4.3.3), the canonical morphism*

```text
Lie : Hom_{S-gr.}(G, H) → Hom_{O_S\text{-Lie alg.}}(g, h)
```

*is an isomorphism.*

<!-- label: III.XXIV.7.3.1 -->

**Lemma 7.3.2.** *Let `k` be a field of characteristic 0, `G` a `k`-reductive group, `V` a finite-dimensional `k`-vector
space, `G → GL(V)` a linear representation of `G` in `V`. One has*

```text
H⁰(G, V) = H⁰(g, V),    Hⁱ(G, V) = 0,    for i > 0.
```

<!-- label: III.XXIV.7.3.2 -->

The first equality is true in general for a smooth connected group;[^N.D.E-XXIV-41] in the case of a reductive group,
one can prove it as follows: one may assume `k` algebraically closed, hence `G` splittable, hence `G` generated by
subgroups isomorphic to `G_{m, k}`,[^N.D.E-XXIV-42] and it suffices to verify the assertion for this group, which is
easy.

From this first equality it follows that `H⁰(G, V)` is an exact functor in `V` when `G` is semisimple; `g` is indeed
then a semisimple Lie algebra and one applies [BLie], § I.6, exercise 1 (b). The assertion remains true when `G` is
reductive; indeed, if one introduces the radical `R` of `G`[^N.D.E-XXIV-43] and the quotient `G/R` which is semisimple,
one has `H⁰(G, V) = H⁰(G/R, H⁰(R, V))`, and `H⁰(G, −)` is composed of two exact functors. Applying then Exp. I, 5.3.1,
one deduces `Hⁱ(G, V) = 0` for `i > 0`.

**Remark 7.3.3.** Under the preceding conditions, if `G` is semisimple, one has `H¹(g, V) = H²(g, V) = 0`, cf. [BLie],
*loc. cit.* (b) and (d).

<!-- label: III.XXIV.7.3.3 -->

#### 7.3.4.

<!-- label: III.XXIV.7.3.4 -->

Let us now prove the proposition. Already, by 7.2.3, `Hom_{S-gr.}(G, H)` is representable by an `S`-scheme locally of
finite presentation and separated over `S`; to show that it is smooth, it suffices to prove that it is infinitesimally
smooth (Exp. XI, 1.8),[^N.D.E-XXIV-44] which follows from Exp. III, 2.8 (i) by 7.3.2. We have thus proved (i).

Let us show that (ii) follows from (iii). It suffices first to prove that `Hom_{S-gr.}(G, H)` is affine over `S`; it
will then be of finite presentation over `S`, since it is smooth over `S` by (i); in any case
`Hom_{O_S\text{-Lie alg.}}(g, h)` is representable by a closed subscheme of

```text
Hom_{O_S\text{-mod.}}(g, h) ≃ W(g^∨ ⊗_{O_S} h)
```

which is an affine `S`-scheme, and the desired conclusion appears when `G` is simply connected.

<!-- original page 266 -->

In the general case, one may assume `G` split, so `G ≃ Ép_S(R)`; introducing the simply connected root datum `sc(R)`
(Exp. XXI, 6.5.5), and using the existence theorem (Exp. XXV, 1.1), one constructs a simply connected `S`-group `G̃` and
a central isogeny `G̃ → G`. The kernel `K` of this isogeny is a finite diagonalizable `S`-group (so a twisted constant
`S`-group, `S` being of characteristic 0) and `Hom_{S-gr.}(K, H)` is (trivially) representable by a separated `S`-scheme
(if `K ≃ (ℤ/nℤ)_S`, then `Hom_{S-gr.}(K, H)` is isomorphic to `Ker(H →^n H)`). One has an exact sequence of "pointed
`S`-schemes":

```text
1 → Hom_{S-gr.}(G, H) →^u Hom_{S-gr.}(G̃, H) → Hom_{S-gr.}(K, H),
```

so `u` is a closed immersion, hence `Hom_{S-gr.}(G, H)` is affine over `S`.

#### 7.3.5.

<!-- label: III.XXIV.7.3.5 -->

Let us finally prove (iii). Arguing as in the proof of (i) and using 7.3.3, one can show that the `S`-scheme
`Hom_{O_S\text{-Lie alg.}}(g, h)` is smooth over `S`. To prove (iii), one may therefore assume `S = Spec(k)`, where `k`
is an algebraically closed field of characteristic 0; it even suffices to prove that the morphism `Lie` is bijective on
`k`-valued points and that it induces a bijection on tangent spaces at two corresponding points. Let us first show that

```text
Hom_{k-gr.}(G, H) → Hom_{k\text{-Lie alg.}}(g, h)
```

is bijective.

If `u : G → H` is a morphism of `k`-groups, the graph of `u` is a connected subgroup of `G ×_k H` which is determined by
its Lie algebra which is the graph of `Lie(u)`; the map is therefore injective. Conversely, if `v : g → h` is a morphism
of Lie algebras, the graph `k` of `v` is a Lie subalgebra of `g × h`, isomorphic to `g`. In particular, since `g` is its
own derived algebra, the same is true of `k` and so, by a theorem of Chevalley ([Ch51], § 14, Th. 15), `k` is the Lie
algebra of a connected subgroup `K` of `G ×_k H`.[^N.D.E-XXIV-45] Moreover, since `k ≃ g` is semisimple, `G` is a
semisimple `k`-group. Since

```text
dim(K) = dim(k) = dim(g) = dim(G)
```

and since `K ∩ H` is finite (because its Lie algebra is zero), the canonical morphism `pr_1 : K → G` is finite and
dominant; since `G` is connected, `pr_1` is surjective; it is therefore an isogeny. Since `G` is simply connected and
`K` semisimple then, by Exp. XXI 6.2.7, `pr_1` is an isomorphism, so `K` is the graph of a morphism of `k`-groups
`u : G → H` such that `Lie(u) = v`.

Finally, let `u : G → H` be a morphism of `k`-groups. The tangent space to `Hom_{k-gr.}(G, H)` at `u` is identified with
`Z¹(G, h)` (cf. Exp. II, 4.2; `G` operates on `h` by `Ad_H ∘ u`); similarly, one can prove that the tangent space to
`Hom_{k\text{-Lie alg.}}(g, h)` at `Lie(u)` is identified with `Z¹(g, h)`. We must therefore prove that the canonical
map `Z¹(G, h) → Z¹(g, h)` is bijective. Now one has a commutative diagram

```text
0 → h^G → h → Z¹(G, h) → H¹(G, h)
        ↓    ↓        ↓        ↓
0 → h^g → h → Z¹(g, h) → H¹(g, h)
```

and by 7.3.2 and 7.3.3 one has `h^G = h^g` and `H¹(G, h) = 0 = H¹(g, h)`, whence the desired conclusion.

**Remark 7.3.6.** It is presumably the case that if `S` is a locally noetherian scheme, `G` an `S`-semisimple simply
connected group, `H` an `S`-group scheme smooth, `Ĝ` and `Ĥ` their formal completions along the unit section, every
homomorphism `Ĝ → Ĥ` comes from a unique homomorphism of `G` into `H`, which would generalize 7.3.1 (iii). When `S` is
the spectrum of a field `k` and `H` is affine and of finite type, this follows from a theorem of Dieudonné ([Di57], §
15, th. 4).[^N.D.E-XXIV-46]

<!-- label: III.XXIV.7.3.6 -->

### 7.4. An example

<!-- label: III.XXIV.7.4 -->

By way of example, we shall determine

```text
Hom_{S-gr.}(SL_{2, S}, SL_{2, S}).
```

#### 7.4.1.

<!-- label: III.XXIV.7.4.1 -->

Recall (Exp. XX, no 5) that `SL_{2, S}` is the `S`-group scheme formed by the matrices `( a b ; c d )` over `S`
satisfying `ad − bc = 1`. A maximal torus `T` is defined by the monomorphism `α^* : G_{m, S} → SL_{2, S}`

```text
α^*(z) = ( z   0   )
         ( 0  z^{-1} ).
```

A root of `G` with respect to `T` is defined by `α(α^*(z)) = z²`, a corresponding monomorphism

```text
p : G_{a, S} → SL_{2, S}
```

being defined by

```text
p(x) = ( 1 x )
       ( 0 1 ).
```

Finally, the representative of the Weyl group corresponding to `u = p(1)` is

```text
w = (  0  1 )
    ( -1  0 ).
```

<!-- original page 267 -->

Recall on the other hand (Exp. XX, 6.2) that `SL_{2, S}` is generated by `T`, `p(G_{a, S})` and `w`, subject to the
relations

```text
α^*(z) p(x) α^*(z^{-1}) = p(z² x),
w α^*(z) w^{-1} = α^*(z^{-1}),
w² = α^*(−1),
(w u)³ = 1.
```

#### 7.4.2.

<!-- label: III.XXIV.7.4.2 -->

Let `f` be an endomorphism of `SL_{2, S}`. It defines first a homomorphism `f ∘ α^* : G_{m, S} → SL_{2, S}`. The kernel
`Ker(f ∘ α^*)` is a closed subgroup of `G_{m, S}`, hence is locally on `S` equal to a `μ_{n, S}` (`n ⩾ 1`) or to
`G_{m, S}`. Up to restricting `S`, one may therefore assume that there exists an `n ∈ ℕ` and a monomorphism

```text
f' : G_{m, S} → SL_{2, S}
```

such that `f ∘ α^*(z) = f'(z^n)`.

By the conjugacy of monomorphisms `G_{m, S} → SL_{2, S}`, one can, after an étale-covering extension of the base, find a
section `g` of `G` such that `f ∘ α^*(z) = int(g) ∘ α^*(z^n)`. Transforming `f` by `int(g)`, one is therefore reduced to
the case where there exists an `n ∈ ℕ` such that `f ∘ α^*(z) = α^*(z^n)`.

#### 7.4.3.

<!-- label: III.XXIV.7.4.3 -->

Consider now the morphism

```text
f ∘ p : G_{a, S} → SL_{2, S}.
```

It verifies the condition

```text
α^*(z^n) (f ∘ p)(x) α^*(z^n)^{-1} = (f ∘ p)(z² x).
```

If `n = 0`, it follows at once that `f ∘ p` is invariant under the homotheties of `G_{a, S}`, hence constant. If
`n ≠ 0`, one can apply Exp. XXII, 4.1.9; `x ↦ x^n` is an endomorphism of `G_{a, S}`, there exists a `λ ∈ G_{m, S}` such
that

```text
f ∘ p(x) = p(λ x^n);
```

this relation is moreover valid for `n = 0`, taking `λ = 1`. Up to again extending `S`, one can find a `z ∈ G_{m, S}`
such that `z² = λ`. Replacing `f` by `int(α^*(z)) ∘ f`, one is therefore reduced to the case where one has

```text
f ∘ α^*(z) = α^*(z^n),    f ∘ p(x) = p(x^n).
```

<!-- original page 268 -->

#### 7.4.4.

<!-- label: III.XXIV.7.4.4 -->

Finally, one must have `f(w) α^*(z^n) f(w)^{-1} = α^*(z^n)^{-1}` and `(f(w) u)³ = 1`. By Exp. XX, 3.8, this entails
`f(w) = w^n`. Since `G` is generated by `T`, `p(G_{a, S})` and `w`, this entails that for every `( a b ; c d ) ∈ G(S')`,
`S' → S`, one has

```text
f( a b ) = ( a^n b^n )
  ( c d )   ( c^n d^n ).
```

#### 7.4.5.

<!-- label: III.XXIV.7.4.5 -->

Summarizing the preceding discussion, one sees that locally on `S` for the étale topology, one can find for every
endomorphism `f` of `SL_{2, S}` an (inner) automorphism `φ` of `SL_{2, S}`, and an integer `n ⩾ 0` such that
`f = φ ∘ F_n`, where

```text
F_n( a b ) = ( a^n b^n )
   ( c d )   ( c^n d^n ).
```

Note that if `f = φ ∘ F_n`, the integer `n` is well determined by a fiber `f_s` of `f`, for example by `Ker(f_s)`. It
follows that `n` is a locally constant function on `S`.

#### 7.4.6.

<!-- label: III.XXIV.7.4.6 -->

One deduces at once that if `f` is an endomorphism of `SL_{2, S}`, then `S` decomposes canonically as a sum of open and
closed subschemes `S_0`, `S_1`, `S_{p^n}` (where `p^n` ranges over the set of positive powers of prime numbers) such
that:

(i) `f_{S_0}` is the zero morphism,

(ii) `f_{S_1}` is an isomorphism (= an inner automorphism),

(iii) `S_{p^n}` is of characteristic `p` and `f_{S_{p^n}}` decomposes uniquely in the form `φ ∘ F_p^n`, where `φ` is an
inner automorphism and `F_p` the Frobenius endomorphism of `SL_{2, F_p}`.

#### 7.4.7.

<!-- label: III.XXIV.7.4.7 -->

In other words, `Hom_{ℤ-gr.}(SL_{2, ℤ}, SL_{2, ℤ})` is the sum scheme:

(i) of a scheme isomorphic to `Spec(ℤ)`,

(ii) of a scheme isomorphic to `Aut_{ℤ-gr.}(SL_{2, ℤ}) ≃ ad(SL_{2, ℤ})`,

(iii) for each prime number `p` and each integer `n > 0`, of a scheme isomorphic to
`Aut_{F_p-gr.}(SL_{2, F_p}) ≃ ad(SL_{2, F_p})`.

#### 7.4.8.

<!-- label: III.XXIV.7.4.8 -->

It follows in particular that

(i) `Hom_{F_p-gr.}(SL_{2, F_p}, SL_{2, F_p})` has an infinite number of connected components, and so is not
quasi-compact.

(ii) If `S` is a scheme of unequal characteristics, `Hom_{S-gr.}(SL_{2, S}, SL_{2, S})` is not flat over `S`.

## 8. Appendix: Cohomology of a smooth group over a henselian ring. Cohomology and the functor `∏`

<!-- label: III.XXIV.8 -->

<!-- original page 269 -->

**Proposition 8.1.** *Let `S` be a henselian local scheme, `s` its closed point, `G` an `S`-group scheme smooth such
that every finite subset of `G` is contained in an affine open set.[^XXIV-8-star] Then*

*(i) If `P` is a principal homogeneous bundle under `G`, there exists an `S' → S` finite, surjective étale that
trivializes `P`. One has `Fib(S, G) ≃ H¹_ét(S, G)`.*

*(ii) For every finite surjective étale morphism `S' → S`, the canonical map*

```text
H¹(S'/S, G) → H¹(S' ⊗_S κ(s) / κ(s), G_s)
```

*is bijective.*

*(iii) The canonical map*

```text
Fib(S, G) → Fib(κ(s), G_s)
```

*is bijective.*

<!-- label: III.XXIV.8.1 -->

#### 8.1.2.

<!-- label: III.XXIV.8.1.2 -->

If `K` is a finite separable extension of `κ(s)`, there exists an `S' → S` finite surjective étale such that
`K ≃ S' ⊗_S κ(s)`.[^N.D.E-XXIV-47] If `P` is a principal homogeneous bundle under `G`, then `P` is smooth over `S`,
hence `P_s` smooth over `κ(s)`; there therefore exists a finite separable extension `K` of `κ(s)` such that `P_K`
possesses a section (cf. EGA IV_4, 17.15.10). Representing `K` as said above, one sees that `P_{S'}` possesses a section
by "Hensel's lemma" (cf. EGA IV_4, 18.5.17), which proves the first part of (i).

Conversely, if `P` is a principal homogeneous sheaf under `G` for the étale topology, there exists an `S' → S` finite
surjective étale that trivializes `P` (indeed every covering family of a henselian local scheme for the étale topology
is dominated by a family reduced to a morphism `S' → S` of the wanted form).

By virtue of the descent hypothesis made on `G`, `P` is representable (SGA 1, VIII, 7.6), which completes the proof of
(i), and shows that (ii) entails (iii). It only remains to prove (ii).

<!-- original page 270 -->

#### 8.1.3.

<!-- label: III.XXIV.8.1.3 -->

The map of (ii) is injective: let `P` and `Q` be two principal homogeneous bundles under `G` trivialized by `S'`.
Consider the `S`-group sheaf `H = Isom_{G\text{-bundles}}(P, Q)`; since `H_{S'}` is isomorphic to `G_{S'}`, `H` is
representable, by the second hypothesis on `G`, cf. above. If `H(κ(s)) ≠ ∅`, then `H(S) ≠ ∅` by Hensel's lemma, so `P`
and `Q` are isomorphic.

#### 8.1.4.

<!-- label: III.XXIV.8.1.4 -->

Let us finally prove that the map of (ii) is surjective, or equivalently that the canonical map

```text
Z¹(S'/S, G) → Z¹(S' ⊗_S κ(s) / κ(s), G_s)
```

is surjective. Let `Z¹` be the `S`-functor defined by

```text
Z¹(T) = Z¹(S' ×_S T / T, G_T);
```

the preceding map is identified with the map

```text
Z¹(S) → Z¹(κ(s));
```

by a further application of Hensel's lemma, it suffices to prove that `Z¹` is representable by a smooth `S`-scheme.

#### 8.1.5.

<!-- label: III.XXIV.8.1.5 -->

Let us prove that `Z¹` is representable by an `S`-scheme locally of finite presentation. Let `C_i`, `i = 0, 1, ...`, be
the `S`-functor defined by

```text
C_i(T) = C_i(S' ×_S T / T, G_T),
```

that is

```text
C_i(T) = G((S' ×_S T / T)^{i+1}) = G((S'/S)^{i+1} ×_S T),
```

or again

```text
C_i = Hom_S((S'/S)^{i+1}, G).
```

Since `Z¹` is obtained from `C_1` and `C_2` by fibered products, it suffices to prove that `C_i`, `i = 1, 2`, is
representable by an `S`-scheme locally of finite presentation.

#### 8.1.6.

<!-- label: III.XXIV.8.1.6 -->

If `T → S` is a finite surjective étale morphism that decomposes `S'`, then

```text
C_i ×_S T = Hom_T((S' ×_S T / T)^{i+1}, G_T)
```

is representable by a product of `n` copies of `G_T`, where `n` is the degree of `(S'/S)^{i+1}`. Applying once more the
hypothesis on `G`, one deduces that `C_i` is indeed representable by an `S`-scheme locally of finite presentation (SGA
1, VIII, *loc. cit.*).

#### 8.1.7.

<!-- label: III.XXIV.8.1.7 -->

To prove that `Z¹` is smooth, we must now, by definition, prove that if `T` is an affine `S`-scheme, `T_0` the closed
subscheme defined by an ideal `J` of square zero, the canonical map

```text
Z¹(T) → Z¹(T_0)
```

is surjective. Since `G` is smooth, the canonical map `G(T) → G(T_0)` is surjective,

<!-- original page 271 -->

and it suffices to prove that the canonical map

```text
H¹(S' ×_S T / T, G_T) → H¹(S' ×_S T_0 / T_0, G_{T_0})
```

is bijective.

Changing notation slightly and generalizing the hypotheses, it now suffices for us to prove:

**Lemma 8.1.8.** *Let `S` and `S'` be two affine schemes, `S' → S` a faithfully flat morphism, `J` an ideal of square
zero on `S`, `S_0` the closed subscheme it defines, `G` a smooth `S`-group. Set `S'_0 = S' ×_S S_0`, `G_0 = G ×_S S_0`.
The canonical map*

```text
H¹(S'/S, G) → H¹(S'_0/S_0, G_0)
```

*is bijective.*

<!-- label: III.XXIV.8.1.8 -->

**Remark 8.1.9.** If one assumes `G` commutative, the same assertion is valid for all `Hⁱ`, `i > 0`, with an analogous
proof.

<!-- label: III.XXIV.8.1.9 -->

*Proof.* Let `M_0` be the quasi-coherent `O_{S_0}`-module `M_0 = Lie(G_0/S_0) ⊗_{O_{S_0}} J`. For each `S_0`-prescheme
`T_0`, set `M_0(T_0) = H⁰(T_0, M_0 ⊗_{O_{S_0}} O_{T_0})`, and let

```text
M = ∏_{S_0/S} M_0    and    Ḡ = ∏_{S_0/S} G_0
```

be the `S`-group functors defined by `M(T) = M_0(T_0)` and `Ḡ(T) = G_0(T_0)`, where `T_0 = T ×_S S_0`. By Exp. III, 0.9
and (0.6.2), there exists for every affine `S`-scheme `T` an exact sequence, functorial in `T`:

```text
1 → M(T) → G(T) → Ḡ(T) → 1.
```

We have to study the map

```text
H¹(S'/S, G) → H¹(S'_0/S_0, G_0) = H¹(S'/S, Ḡ).
```

Suppose first `G` commutative. One then has an exact cohomology sequence

```text
H¹(S'/S, M) → H¹(S'/S, G) → H¹(S'/S, Ḡ) → H²(S'/S, M);
```

but

```text
Hⁱ(S'/S, M) = Hⁱ(S'_0/S_0, M_0) = Hⁱ(S'_0/S_0, M_0),
```

and one knows (TDTE I, B, Lemma 1.1) that `Hⁱ(S'_0/S_0, M_0) = 0` for `i ≠ 0`.

If now `G` is not commutative, we must use the exact sequence of non-abelian cohomology. If `u ∈ Z¹(S'/S, Ḡ)`, one knows
that the elements of `H¹(S'/S, G)` having the same image in `H¹(S'/S, Ḡ)` as the class of `u` are in the image of the
corresponding coboundary map:

```text
H¹(S'/S, M_u) → H¹(S'/S, G),
```

where `M_u` is the `S`-functor `M` "twisted by `u`". Similarly, if `v` is an element of `Z¹(S'/S, Ḡ)`, there exists a
"coboundary"

```text
Δ(v) ∈ H²(S'/S, M_v),
```

<!-- original page 272 -->

where `M_v` is the `S`-functor `M` "twisted by `v`", such that `Δ(v) = 0` if and only if the class of `v` is in the
image of `H¹(S'/S, G)`. It suffices to prove that one has `H¹(S'/S, M_u) = H²(S'/S, M_v) = 0`.

Now recall (Exp. III 0.8) that the action of `G` on `M` defined by the exact sequence is none other than that which is
deduced functorially from the adjoint representation of `G_0`:

```text
ad : G_0 → Aut_{O_{S_0}}(Lie(G_0/S_0)).
```

The element `u` (resp. `v`) therefore acts in `M_{S' ×_S S'}` via an `S'_0 ×_{S_0} S'_0`-automorphism of `Lie(G_0/S_0)`.
Since `u` (resp. `v`) is a cocycle, this automorphism is a descent datum; write `L_u` (resp. `L_v`) for the
quasi-coherent `O_{S_0}`-module obtained. One verifies at once that for `T → S`, one has

```text
M_u(T) = H⁰(T_0, L_u ⊗_{O_{S_0}} J ⊗_{O_{S_0}} O_{T_0})
```

and the same relation replacing `u` by `v`. One therefore has

```text
H¹(S'/S, M_u) = H¹(S'_0/S_0, L_u ⊗ J),
H²(S'/S, M_v) = H²(S'_0/S_0, L_v ⊗ J),
```

and both are indeed zero by virtue of the result already used.

**Proposition 8.2.** *Let `C` be a category possessing fibered products, equipped with a topology coarser than the
canonical topology, `S' → S` a morphism of `C`, `G'` an `S'`-group sheaf, `G` the `S`-group sheaf `∏_{S'/S} G'`. Let
`H¹_S(S', G') ⊂ H¹(S', G')` be the set of classes of principal homogeneous sheaves under `G'` which are trivialized by a
sieve of `S'` obtained by base change from a suitable covering sieve of `S`. The canonical map `H¹(S, G) → H¹(S', G')`
defined by the functor*

```text
P ↦ P ×_S S'
```

*induces a bijection*

```text
H¹(S, G) ⥲ H¹_S(S', G');
```

*the inverse bijection is defined by the functor `P' ↦ ∏_{S'/S} P'`.*

<!-- label: III.XXIV.8.2 -->

For every object `X` of `C/S`, one has by definition a functorial isomorphism in `X`

```text
Hom_S(X, G) ⥲ Hom_{S'}(X ×_S S', G').
```

One therefore has for each `S`-object `T` a functorial bijection in `T`

```text
H¹(T/S, G) ⥲ H¹(T'/S', G').
```

Replacing now the unique morphism `T → S` by an arbitrary covering family of `S` and passing to the inductive limit, one
deduces the first part of the statement. The second part is deduced without difficulty.

**Lemma 8.3.** *Under the conditions of 8.2, the assertion `H¹_S(S', G') = H¹(S', G')` is local on `S`: suppose there
exists a covering family `{S_i → S}` such that for every `i`, one has `H¹_{S_i}(S' ×_S S_i, G') = H¹(S' ×_S S_i, G')`.
Then `H¹_S(S', G') = H¹(S', G')`.*

<!-- label: III.XXIV.8.3 -->

<!-- original page 273 -->

Indeed, let `P'` be a principal homogeneous sheaf under `G'`. Set

```text
P'_i = P' ×_{S'} (S' ×_S S_i);
```

by hypothesis, there exists a covering family `{S_{ij} → S_i}` such that for each `j`, `P' ×_{S'} (S' ×_S S_{ij})`
possesses a section. But `{S_{ij} → S}` is a covering family of `S`, and `P'` is indeed trivialized by the covering
family of `S'` obtained from this one by base change.

**Proposition 8.4.** *Let `S' → S` be a finite étale morphism of schemes. Let `G'` be an `S'`-group sheaf, `G` the
`S`-group sheaf `∏_{S'/S} G'`. For the étale (resp. local finite étale, resp. (fpqc)) topology, the functors*

```text
P    ↦   P ×_S S'
∏_{S'/S} P'    ↤    P'
```

*induce inverse bijections of each other:*

```text
H¹(S, G) ≃ H¹(S', G').
```

<!-- label: III.XXIV.8.4 -->

By 8.2, it suffices to show that `H¹_S(S', G') = H¹(S', G')`. By 8.3, it suffices to do this locally for the local
finite étale topology; one may therefore assume that `S'` is a finite direct sum of copies of `S`, say `I_S`, where `I`
is a suitable finite set. Then `G'` is given by a family `(G_i)_{i ∈ I}` of sheaves on `S` and

```text
H¹(S', G') ≃ ∏_{i ∈ I} H¹(S, G_i).
```

On the other hand

```text
H¹(S, G) ≃ ∏_{i ∈ I} H¹(S, G_i),
```

whence, by 8.2, `H¹_S(S', G') = H¹(S', G')`. QED

**Remarks 8.5.** One can interpret 8.2 and 8.3 by the following exact sequence (`f` is the given morphism `S' → S`)

```text
1 → H¹(S, f_*(G')) → H¹(S', G') → H⁰(S, R¹f_*(G')).
```

<!-- label: III.XXIV.8.5 -->

In the commutative case, this exact sequence follows from the Leray spectral sequence; it is still valid in the
non-commutative case (cf. Giraud's thesis[^N.D.E-XXIV-48]).

In this form, one sees that the result is still valid if `f` is only assumed finite, or simply integral, the topology
being the étale topology, because for every `G'`, one has

```text
R¹f_*(G') = \text{final sheaf},
```

by SGA 4, VIII, 5.3.[^N.D.E-XXIV-49]

On the other hand, this result becomes false if one takes a topology such as (fpqc) or (fppf), even if `S = Spec(k)`,
`k` algebraically closed field of characteristic `p ≠ 0`, `S' = Spec(k[t]/t²)`, `G' = μ_p` or `α_p`.

<!-- original page 274 -->

Similarly, 8.2 becomes false, even for the étale topology, if one suppresses in it the hypothesis that `f` is finite, as
one sees by taking for `f` an open immersion; for example if `S = Spec(V)`, `V` a complete discrete valuation ring with
algebraically closed residue field, `S'` being the open subset induced at the generic point, and `G'` the constant group
`(ℤ/nℤ)_{S'}`, with `n` prime to the residue characteristic of `V`, one has `H¹(S, G) = 0`, `H¹(S', G') ≠ 0`. Moreover,
replacing `S'` by `S ∐ S'`, one deduces an analogous example, with `S' → S` étale surjective, hence covering for the
topology considered.

## Bibliography

- [BLie] N. Bourbaki, *Groupes et algèbres de Lie*, Chap. I, Hermann, 1960.
- [Ch51] C. Chevalley, *Théorie des groupes de Lie*. t. II *Groupes algébriques*, Hermann, 1951.
- [Di57] J. Dieudonné, Lie groups and Lie hyperalgebras over a field of characteristic `p > 0`. VI, *Amer. J. Math.* 79
    (1957), no 2, 331-388.[^N.D.E-XXIV-50]
- [Bo91] A. Borel, *Linear algebraic groups*, 2nd edition, Springer-Verlag, 1991.
- [Ch05] C. Chevalley, *Classification des groupes algébriques semi-simples* (with the collaboration of P. Cartier, A.
    Grothendieck, M. Lazard), *Collected Works*, vol. 3, Springer, 2005.
- [DG70] M. Demazure, P. Gabriel, *Groupes algébriques*, Masson & North-Holland, 1970.
- [Gi71] J. Giraud, *Cohomologie non abélienne*, Springer-Verlag, 1971.
- [Ja87] J. C. Jantzen, *Representations of Algebraic Groups*, Academic Press, 1987; 2nd edition, Amer. Math. Soc.,
    2003\.
- [Jou83] J.-P. Jouanolou, *Théorèmes de Bertini et applications*, Birkhäuser, 1983.
- [Ta75] M. Takeuchi, On coverings and hyperalgebras of affine algebraic groups, *Trans. Amer. Math. Soc.* 211 (1975),
    249-275.

## Footnotes

<!-- LEDGER DELTA — Exposé XXIV — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| automorphismes extérieurs | outer automorphisms | Standard. |
| automorphismes intérieurs | inner automorphisms | Standard. |
| forme tordue intérieure | inner twisted form | Standard. |
| groupe quasi-épinglé / quasi-épinglage | quasi-pinned group / quasi-pinning | "Quasi-" prefix preserved. |
| quasi-déployable | quasi-splittable | Matches "déployable" → "splittable". |
| revêtement principal galoisien | principal Galois covering | Standard. |
| schéma de Dynkin | Dynkin scheme | Standard. |
| diagramme de Dynkin | Dynkin diagram | Standard. |
| schéma constant tordu | twisted constant scheme | Standard. |
| schéma constant tordu à engendrement fini | finitely generated twisted constant scheme | Per Exp. X, 5.1. |
| isotypique de type t | isotypic of type t | Standard. |
| simple de type t | simple of type t | Standard. |
| couple de Killing | Killing couple | Standard. |
| sous-groupe radiciel U_α | root subgroup U_α | Per glossary. |
| schéma des sous-groupes de Borel | scheme of Borel subgroups | Standard. |
| groupe adjoint | adjoint group | Standard. |
| groupe simplement connexe | simply connected group | Standard. |
| extension du groupe structural | extension of the structure group | Standard. |
| restriction du groupe structural | restriction of the structure group | Standard. |
| somme amalgamée | amalgamated sum | Standard. |
| topologie étale finie locale | local finite étale topology | Per Exp. IV 6.3 (étf). |
| théorème 90 | theorem 90 | Per Exp. VIII 4.5; kept lowercase as in source. |
| trivialiser / trivialisé | trivialize / trivialized | Standard. |
| fibré principal homogène | principal homogeneous bundle | Per glossary. |
| faisceau principal homogène | principal homogeneous sheaf | Distinguish from "fibré". |
| isotrivialité / isotrivial | isotriviality / isotrivial | Standard. |
| quasi-isotrivial | quasi-isotrivial | Standard. |
| extension étale finie surjective | finite surjective étale extension | Standard. |
| algèbre de Lie semi-simple | semisimple Lie algebra | Per glossary. |
| nombres duaux | dual numbers | Standard. |
-->

[^N.D.E-XXIV-0]: N.D.E.: Version of 13/10/2024.

[^N.D.E-XXIV-1]: N.D.E.: Hence `Lie(u)(X'_{v(α)}) = X_α`, for every `α ∈ R'`.

[^N.D.E-XXIV-2]: N.D.E.: One recalls that `ad(G) = G / Centr(G)` denotes the adjoint group of `G`, cf. XXII 4.3.6.

[^N.D.E-XXIV-3]: N.D.E.: We have replaced here and in the sequel the notation `int(G)` by `ad(G)`.

[^N.D.E-XXIV-4]: N.D.E.: cf. SGA 1, VIII 2.1.

[^N.D.E-XXIV-5]: N.D.E.: We have corrected `ad(G) → Autext(G)` to `ad(G) → Aut(G)`.

[^N.D.E-XXIV-6]: N.D.E.: We have corrected the original, which stated (i) without assuming `G` adjoint. Following the
    characterization of the `Hⁱ(G, −)` as derived functors of `Hom_G(k, −)` (Exp. I, 5.3.1; see also
    [Ja87], I 4.16), one has `Hⁱ(G, V) = Ext^i_G(k, V)` for every `G`-module `V`; now if `char(k) = p > 0`
    and `G = SL_{p, k}`, then `Lie(GL_p/k)` is a non-trivial extension of `k` by `g = Lie(SL_p/k)`, so
    `H¹(G, g) ≠ 0`. See also the addition 1.15.1 below.

[^N.D.E-XXIV-7]: N.D.E.: We have replaced "scheme" by "field".

[^N.D.E-XXIV-8]: N.D.E.: Because of the correction made in 1.13, we have given another proof in the case of `H¹`. On the
    other hand, it follows from a theorem of G. Kempf that `Hⁱ(G, k) = 0` for every `i > 0`, cf. [Ja87], II
    4.5 and 4.11.

[^N.D.E-XXIV-9]: N.D.E.: We have added this corollary, drawn from remarks of O. Gabber, which makes 1.13 (i) more
    precise.

[^N.D.E-XXIV-10]: N.D.E.: cf. XXIII, Definition 5.11.

[^N.D.E-XXIV-11]: N.D.E.: We have made explicit the preceding definitions (the original indicated "One defines similarly
    `Aut_{S-gr.}(G, X, Y)`, ..., `Isom_{S-gr.}(G, X; G', X')`, ...").

[^N.D.E-XXIV-12]: N.D.E.: cf. SGA 1, VIII 1.9.

[^N.D.E-XXIV-13]: N.D.E.: Therefore, if `P` possesses a section, then `T` and `T'` are isomorphic; in particular `T_P`
    and `T'_P` are isomorphic. See the addition 4.5.1 where this remark is developed in the case where
    `G = Ép_S(R)`.

[^N.D.E-XXIV-14]: N.D.E.: by 2.7, since `Isomext(G, G')` possesses a section (cf. the preceding N.D.E.).

[^N.D.E-XXIV-15]: N.D.E.: Recall that `Isomint_u(G, G')` is defined in 1.11.

[^N.D.E-XXIV-16]: N.D.E.: We have added the hypothesis that `S'` be connected.

[^N.D.E-XXIV-17]: N.D.E.: We have detailed the reference to Exp. XXII, 5.9.7.

[^N.D.E-XXIV-18]: N.D.E.: The original referred to EGA IV, § 24, which has not appeared. The point is to use "Bertini's
    theorem". Let us detail the argument, which was indicated to us by O. Gabber. Let `X → S` be a
    surjective, smooth and projective morphism; replacing `S` by a connected component, one may assume
    that `X/S` has constant relative dimension `d` at every point (cf. EGA IV_4, 17.10.2). One may also
    assume that `X` is a closed subscheme of a projective space `P^n_S = P(E)`, where `E` is a free
    `A`-module of rank `n + 1` (cf. EGA II, 5.3.3). Let `s_1, ..., s_r` be the closed points of `S`; by
    Bertini's theorem (see for example [Jou83], I 6.10), there exists an open set `U` of the product
    `P = P(E^*)^d`, with non-empty fibers, such that for every point `u = (f_1, ..., f_d)` of `U_{s_i}`,
    the intersection of `X_{κ(u)}` with the `d` hyperplanes of `P^n_{κ(u)}` defined by `u` is étale over
    `κ(u)`. Up to shrinking `U`, one may assume that `U` is the complement in the affine space `A^{nd}_S`
    of the locus of zeros `V(Q)` of a certain polynomial `Q` of degree `m > 0`. One then sees easily (by
    induction on the number of variables) that `V(Q)` cannot contain all rational points of
    `A^{nd}_{κ(s_i)}` if `|κ(s_i)| > m`. Since the morphism `A → ∏_i κ(s_i)` is surjective, one can find a
    monic polynomial `R ∈ A[X]` of degree `m` whose image in `κ(s_i)[X]` is irreducible if `κ(s_i)` is
    finite, and possesses `m` distinct roots if `κ(s_i)` is infinite. Put `A' = A[X]/(R)` and
    `S' = Spec(A')`; then `S' → S` is étale, finite and surjective, and the residue field at each of its
    closed points `s'_1, ..., s'_t` is of cardinality `⩾ 2m`. Then `U` possesses a rational point `u_i`
    over each closed point of `S'`, and since `A' → ∏_i κ(s_i)` is surjective, these lift to a section `u`
    of `P_{S'}`. Write `Z` for the intersection of `X_{S'}` with the `d` hyperplanes of `P^n_{S'}` defined
    by `u`, and `V` for the open set of `Z` formed by the points at which `Z` is étale over `S'`. By EGA
    IV_3, 11.3.8, `V` contains the fibers `Z_{s'_i}` for every `i`; since `π : Z → S'` is proper, it
    follows that the closed set `π(Z − V)` is empty, whence `V = Z`. Then `Z → S'` is surjective, étale
    and proper, hence finite, as is the composite `Z → S`, and this yields the desired section of `X → S`.

[^N.D.E-XXIV-19]: N.D.E.: We have sketched in 3.11.4 the verification of the fact that the functors `i`, `rev` and `qép`
    are fully faithful, and that the composite `rev ∘ i ∘ qép` is isomorphic to the identity functor of
    `Rev`.

[^N.D.E-XXIV-20]: N.D.E.: We have expanded the original in the foregoing, to show that the action of `E` on `G'` is
    obtained by combining the natural action of `E` on `Ép_{S'}(R)` and the given action on `S'`. The
    canonical Killing couple of `G'` is preserved by this action, as is the quasi-pinning given by the
    element `X̃'` of `Γ(Δ_{S'}, Lie(G'/S')_{Δ_{S'}})`, equal to `X'_α` on the copy of `S'` indexed by `α`
    (indeed, since `E` acts on `Δ_{S'}` by permutation of the copies of `S'`, one has indeed
    `h(X̃') = X̃'` for every `h ∈ E`).

[^N.D.E-XXIV-21]: N.D.E.: see, for example, TDTE I, p. 22, Example 1. One can also describe `qép(S')` as the twist of
    `G = Ép_S(R)` by the `E`-torsor `S'/S`, i.e. the (fpqc) sheaf quotient of `S' ×_S G` by the right
    action of `E` defined by `(s', g) · h = (s' h, h^{-1}(g))`. Since `G` is affine over `S` and since `E`
    acts on `G` by group automorphisms, this sheaf is representable by an `S`-group `G^♯`, which is a
    "twisted" form of `G`, and `D^♯ = Dyn(G^♯)` is the twist of the constant Dynkin scheme `Δ_S` by the
    torsor `S'/S`. Since `E` normalizes `B` and `T`, one obtains likewise a pair `(B^♯, T^♯)` which is a
    Killing couple of `G^♯`. On the other hand, let `g = Lie(G/S)` and `g^♯ = Lie(G^♯/S)`; for every
    `U → S`, the sections of `g^♯` on `U` are the `E`-equivariant `S`-morphisms `U ×_S S' → W(g)`. Since
    `D^♯ ×_S S'` is `E`-isomorphic to `Δ × S'`, equipped with the action
    `(α, s') · h = (h^{-1}(α), s' h)`, one obtains that the morphism given by `(α, s') ↦ X_α` is a section
    of `g^♯` on `D^♯` which is a quasi-pinning, i.e. a section nowhere zero of
    `(g^♯ ⊗_{O_S} O_{D^♯})^{D^♯}` (cf. 3.8).

[^N.D.E-XXIV-22]: N.D.E.: We have added this number.

[^N.D.E-XXIV-24]: N.D.E.: We have replaced "bundle" by "sheaf", and then `G'` by `G''`.

[^N.D.E-XXIV-25]: N.D.E.: by "theorem 90".

[^N.D.E-XXIV-26]: N.D.E.: We have added this no 4.5.

[^N.D.E-XXIV-27]: N.D.E.: We have replaced `R` by `L`, as in 3.2.

[^N.D.E-XXIV-28]: N.D.E.: We have corrected `F(−1, x)` to `F(1, −x)`.

[^N.D.E-XXIV-29]: N.D.E.: We have corrected `p_{3α+β}(a)` to `p_{2α+β}(a)`, and detailed the end of the argument.

[^N.D.E-XXIV-30]: N.D.E.: denoted (étf) in Exp. IV 6.3. In other words, for every `s ∈ S` there exist an open
    neighborhood `U` of `s` and a finite surjective étale morphism `V → U` such that `B' ×_S V ≃ B ×_S V`.

[^N.D.E-XXIV-31]: N.D.E.: One can ask whether every smooth affine `S`-group, each of whose geometric fibers is a Borel
    subgroup of a semisimple group, is a Borel subgroup of a semisimple `S`-group. (We have suppressed the
    "counter-example" given in the original, for `S =` scheme of dual numbers over a field `k`, which was
    erroneous, as M. Demazure pointed out to us.)

[^N.D.E-XXIV-32]: N.D.E.: See for example the proof of XXII 5.8.1.

[^N.D.E-XXIV-33]: N.D.E.: We have corrected `X → Y` to `Y → X`.

[^N.D.E-XXIV-34]: N.D.E.: We have simplified the proof of the original.

[^N.D.E-XXIV-35]: N.D.E.: In what follows, the group law of `U_α` is written additively, that is, if one writes
    `p_α : G_{a, S} ⥲ U_α` for the isomorphism such that `p_α(1) = u_α` and if `x = p_α(z)`, then `α(t) x`
    (resp. `a(t, t') u_α`) denotes `p_α(α(t) z)` (resp. `p_α(a(t, t')) = α(t) u_α + α(t') u_α`).

[^N.D.E-XXIV-36]: N.D.E.: i.e. for condition (ii) of 7.1.4 to be satisfied.

[^N.D.E-XXIV-37]: N.D.E.: see also the addition in Exp. VI_B, 6.2.3.

[^N.D.E-XXIV-38]: N.D.E.: i.e. for every `S' → Hom_{S-gr.}(T, H)`, with `S'` representable, `Hom_{S-gr.}(G, H) ×_S S'`
    is representable and the morphism of `S`-schemes `Hom_{S-gr.}(G, H) ×_S S' → S'` is separated and
    verifies `P`.

[^N.D.E-XXIV-39]: N.D.E.: We have suppressed the hypothesis that `H` be quasi-separated, which is superfluous.

[^N.D.E-XXIV-40]: N.D.E.: We have replaced `f_r` by `f_{rad}`.

[^N.D.E-XXIV-41]: N.D.E.: Indeed, it is clear that `V^G ⊂ V^g`. On the other hand, `H = Centr_G(V^g)` is a closed
    subgroup of `G`, smooth since `char(k) = 0`; by Exp. II 5.3.1, one has `Lie(H) = Centr_g(V^g) = g`,
    and since `H` is smooth and `G` connected this entails `H = G`, whence `V^g ⊂ V^G` (see also [DG70], §
    II.6, Prop. 2.1 (c)).

[^N.D.E-XXIV-42]: N.D.E.: Indeed, the union of the maximal tori of `G` is dense in `G`, cf. *Bible*, § 6.5, Th. 5 (=
    [Ch05], § 6.6, Th. 6).

[^N.D.E-XXIV-43]: N.D.E.: Note that `R` is a torus.

[^N.D.E-XXIV-44]: N.D.E.: i.e. that for every `S`-scheme `S'` local artinian, with closed point `s'`, every morphism of
    `κ(s')`-groups `G_{s'} → H_{s'}` lifts to a morphism of `S'`-groups `G_{S'} → H_{S'}`. By Exp. III
    2.8, this follows from the vanishing of `H²(G_{s'}, V)`, where `V = Lie(H_{s'}/κ(s'))`.

[^N.D.E-XXIV-45]: N.D.E.: see also [Bo91], II 7.9. Moreover, we have added the sentence that follows.

[^N.D.E-XXIV-46]: N.D.E.: See Exp. VII_B for the definition of the formal groups `Ĝ` and `Ĥ`. Suppose that
    `S = Spec(k)`, where `k` is a field. By *loc. cit.*, 2.2.1, to give a morphism of `k`-formal groups
    `v : Ĝ → Ĥ` is equivalent to giving a morphism of `k`-Hopf algebras `φ : Dist(G) → Dist(H)`, where
    `Dist(G)` denotes the algebra of distributions (at the origin) of `G`, cf. Exp. VII_A, 2.1 or [DG70],
    § II.4, 6.1 or [Ja87], I 7.7 (it is called the "hyperalgebra" of `G` in [Di57] and [Ta75]). Theorem 4
    of [Di57] (see also [Ta75], 0.3.4 (f) and (g)) generalizes in this context the theorem of Chevalley
    used in 7.3.5; one thereby obtains that there exists a closed connected `k`-subgroup `K` of `G × H`
    such that `K̂` equals the graph of `v`; since `Dist(K) → Dist(G)` is an isomorphism, `K → G` is a
    finite étale morphism. One then deduces that `K` is semisimple and then, by Exp. XXI 6.2.7, that
    `K → G` is an isomorphism (since `G` is simply connected); see also [Ta75], 1.8 and 2.2. More
    generally, *loc. cit.* studies the `k`-groups `G` having the property (SC): every finite étale
    morphism of `k`-groups `G' → G`, with `G'` connected, is an isomorphism. Note finally that what
    precedes shows that every `Dist(G)`-module `V` of finite dimension is, uniquely, a `G`-module; for an
    extension to the case of a split reductive `k`-group `G` (or even of a Borel subgroup of `G`) see
    [Ja87], II 1.20 (and the references therein).

[^XXIV-8-star]: This last condition is in fact unnecessary (cf. A. Grothendieck, *Groupe de Brauer III*, in *Dix Exposés
    sur la cohomologie des schémas*, North-Holland, 1968, theorem 11.7 and remarks 11.8.3).

[^N.D.E-XXIV-47]: N.D.E.: Note that `S'` is still local and henselian. Furthermore, we have kept the numbering of the
    original: there is no no 8.1.1.

[^N.D.E-XXIV-48]: N.D.E.: See § V 3.1.4 of [Gi71].

[^N.D.E-XXIV-49]: N.D.E.: This reference also refers to § V 3.1.4 of [Gi71].

[^N.D.E-XXIV-50]: N.D.E.: We have added to these three references, figuring in the original, the following references.

[^N.D.E-XXIV-23]: N.D.E.: We write `Isomint(G_{q-ép.}, G)` instead of `Isomint_u(G_{q-ép.}, G)` (cf. 1.11), since the
    pair `(G_{q-ép.}, u)` is unique up to a unique isomorphism.
