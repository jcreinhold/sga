# Exposé VI_A. Generalities on algebraic groups

<!-- label: III.VI_A -->

*by P. Gabriel*

> [^N.D.E-VI_A-0] Version of 13/10/2024.

Throughout this entire chapter, `A` will denote an Artinian local ring with residue field `k`. A group scheme `G` over
`Spec A` will be called simply an `A`-*group*. This `A`-group is said to be *locally of finite type* if the underlying
scheme is locally of finite type over `A`; it is said to be *algebraic* if the underlying scheme is of finite type over
`A`.

<!-- original page 287 -->

## 0. Preliminary remarks

<!-- label: III.VI_A.0 -->

### 0.1.

Let us first consider a group scheme `G` over an arbitrary scheme `S`. We call *multiplication* the structural morphism
`µ : G ×_S G → G`, and *inversion* the morphism `c : G → G` defined by the equalities `c(T)(x) = x⁻¹` (with `T` a scheme
over `S` and `x` an element of `G(T)`). If `U` and `V` are subsets of the underlying set of `G`, we write `U · V` for
the image under the multiplication morphism of the part of `G ×_S G` consisting of points whose first projection lies in
`U` and second projection in `V`. Likewise, the notations `U⁻¹` and `c(U)` are equivalent.

Let `pr₁` denote the projection of `G ×_S G` onto the first factor and `σ : G ×_S G → G ×_S G` the morphism with
components `pr₁` and `µ`. For every `S`-scheme `T`, `σ(T)` is the map `(x, y) ↦ (x, xy)`; it follows that `σ` is an
automorphism. The composition of this automorphism with the projection `pr₂` of `G ×_S G` onto the second factor is the
multiplication morphism. When `G` is flat over `S`, `pr₂` and hence `µ` are flat morphisms; when `G` is smooth over `S`,
`pr₂` and hence `µ` are smooth morphisms, etc.

<!-- original page 288 -->

### 0.2.

We assume from now on that `S` is the spectrum of an Artinian local ring `A` with residue field `k`. We denote by
`(Sch/k)_red` the category of reduced schemes over `k`. For every scheme `X` over `A`, the reduced scheme `X_red` is an
object of `(Sch/k)_red`, and the functor `X ↦ X_red` is right adjoint to the inclusion of `(Sch/k)_red` into `(Sch/A)`.
It follows that, for every `A`-group `G`, `G_red` is a group in the category `(Sch/k)_red`,[^N.D.E-VI_A-1] i.e., for
every reduced `k`-scheme `T`, `G_red(T)` is equipped with a group structure, functorial in `T`. One should beware that
`G_red` is not necessarily a `k`-group, since the "multiplication" is only a morphism from `(G_red ×_k G_red)_red` into
`G_red`.[^N.D.E-VI_A-2]

<!-- original page 294 -->

[^N.D.E-VI_A-3] However, if `k` is a perfect field, the inclusion of `(Sch/k)_red` into `(Sch/k)` commutes with
products, so that groups in the category `(Sch/k)_red` are identified with group schemes over `k` whose underlying
scheme is reduced. In this case, if `G` is a `k`-group, `G_red` is a group subscheme of `G`; this subgroup is not in
general normal in `G`.

For example, if `k` is a field of characteristic 3, the constant group `(ℤ/2ℤ)_k` acts non-trivially on the
diagonalizable group `D_k(ℤ/3ℤ)` (cf. Exp. I, 4.1 and 4.4); if `G` denotes the semidirect product of `D_k(ℤ/3ℤ)` by
`(ℤ/2ℤ)_k` defined by this action, `G_red` is identified with `(ℤ/2ℤ)_k` and is not normal in `G`.[^N.D.E-VI_A-4]

Let `k` be an arbitrary field, `k^{p^{-∞}}` its perfect closure, and `H` a group in the category `(Sch/k)_red`. Then
`(H ⊗_k k^{p^{-∞}})_red` is a group scheme over the perfect field `k^{p^{-∞}}`. Since `H ⊗_k k^{p^{-∞}}` and
`(H ⊗_k k^{p^{-∞}})_red` have the same underlying topological space, one sees that the groups of `(Sch/k)_red` share
with `k`-groups certain topological properties invariant under extension of the base field: for example, it will follow
from 0.3 and the remarks just made that every group of `(Sch/k)_red` is separated.

<!-- original page 289 -->

We shall encounter groups of `(Sch/k)_red` in what follows whenever we deal with a non-empty, locally closed subset `U`
of an `A`-group `G` such that `U · U = U` and `U⁻¹ = U`: indeed, the reduced subscheme of `G` defined by `U` is then a
group of `(Sch/k)_red`.

### 0.3.

An `A`-group `G` is always separated, since the unit section `e : Spec A → G` is a closed immersion. Indeed, let `x` be
the unique point of `Spec A` and `η` the structural morphism `G → Spec A`. Since `η ∘ e = id_{Spec A}`, for every affine
open `U = Spec B` of `G` containing `e(x)`, the morphism `B → A` has a section, and so is surjective. It follows that
`e` is a closed immersion.[^N.D.E-VI_A-5] Now the diagonal of `G ×_A G` is identified with the functor from `(Sch/A)°`
with values in `(Ens)` that associates to every scheme `S` over `A` the inverse image of the unit element of `G(S)`
under the map `φ(S) : (x, y) ↦ x · y⁻¹` from `G(S) × G(S)` to `G(S)`. We therefore have the cartesian square below, so
that the diagonal morphism, being obtained from a closed immersion by base change, is itself a closed immersion:

```text
            φ
G ×_S G ─────────→ G
   │                ▲
   │ diagonal       │ unit section
   ▼                │
   G ─────────→ Spec A.
```

<!-- original page 295 -->

### 0.4.

[^N.D.E-VI_A-6] Let `G` be an `A`-scheme. We shall say that a point `g` of `G` is *strictly rational over* `A` if there
exists an `A`-morphism `s : Spec A → G` sending the unique point of `Spec A` to `g`, i.e. if the morphism `A → O_{G,g}`
admits a retraction. Note that one then has `κ(g) = k`, and so `g` is a closed point of `G` (if `B` is the ring of an
affine open neighborhood of `g` and `𝔭` the prime ideal of `B` corresponding to `g`, then `B/𝔭 ⊂ k` is a finite
`A`-algebra, hence an integral Artinian ring, hence a field).

<!-- original page 290 -->

Suppose henceforth that `G` is an `A`-group; then such a section `s : Spec A → G` defines an automorphism `r_s` of the
scheme `G` over `A`, which we call *right translation by* `s`: for every morphism `π : S → Spec A`, `r_s(π)` is the
automorphism of `G(S)` defined by `x ↦ x · G(π)(s)`, for every `x ∈ G(S)`. Similarly, we write `ℓ_s` for the *left
translation by* `s`, i.e. the automorphism of `G` defined by the equalities `ℓ_s(π)(x) = G(π)(s) · x`, for every
`x ∈ G(S)`.

Since `G ⊗_A k` and `G` have the same underlying topological space `G`, since `G ⊗_A k` is a `k`-group, and since
`s ⊗_A k` depends only on `g` and not on `s`, one sees that the automorphisms of `G` induced by `r_s` and `ℓ_s` (or by
`r_{s ⊗ k}` and `ℓ_{s ⊗ k}`) depend only on `g` and not on `s`; when `P` is a subset of `G`, we may therefore write
`r_g(P)` or `P · g` (resp. `ℓ_g(P)` or `g · P`) instead of `r_s(P)` (resp. `ℓ_s(P)`), in agreement with 0.1.

**Remark 0.4.1.** *If `g` is a strictly rational point of `G` and if `A → A′` is a morphism of Artinian local rings,
then `G′ = G ⊗_A A′` has a unique point `g′` above `g`, and `g′` is strictly rational over `A′`; moreover, if one writes
`P′` for the inverse image of `P` in `G′`, then `P′ · g′` is the inverse image of `P · g` (cf. EGA I, 3.4.8).*

<!-- label: III.VI_A.0.4.1 -->

**Proposition 0.5.** [^N.D.E-VI_A-7] *Let `G` be an `A`-group and `U, V` two dense open subsets of `G`. Then `U · V`
(i.e. the image of `U ×_A V` under multiplication) is equal to the whole underlying space of `G`.*

<!-- label: III.VI_A.0.5 -->

*Proof.* Since `G` and `G ⊗_A k` have the same underlying space, we may, possibly replacing `A` by `k` and `G` by
`G ⊗_A k`, assume that `A = k`. Let `g ∈ G`. Set `K = κ(g)`; then left translation `ℓ_g` is an automorphism of `G_K`.
Since the projection `G_K → G` is open, `U_K` and `V_K` are dense open subsets of `G_K`, as is the image of `V_K` under
`λ_g`. There exists therefore `v ∈ V_K` such that `u = ℓ_g(v)` belongs to `U_K`. Let `L` be an extension of `K`
containing `κ(v)` (and so `κ(u)`), and let `g_L` and `v_L` be the `L`-points of `G_L` deduced from `g` and `v`. Then
`g_L · v_L = u′` is a point of `G_L` above `u`, and so `g_L = u′ · v_L^{-1}` lies above `U · V`, whence `g ∈ U · V`,
which proves the proposition.

<!-- original page 296 -->

**Corollary 0.5.1.** [^N.D.E-VI_A-8] *If `G` is an irreducible `A`-group, then `G` is quasi-compact.*

<!-- label: III.VI_A.0.5.1 -->

*Proof.* Let `U` be a non-empty affine open subset of `G`; then `U` is dense in `G`, so by 0.5 the morphism
`µ : U ×_A U → G` is surjective, and therefore `G` is quasi-compact since `U ×_A U` is.

**Corollary 0.5.2.** [^N.D.E-VI_A-9] *Let `G` be an `A`-group scheme, and `H` a group subscheme of `G` over `A`. Then
`H` is closed.*

<!-- label: III.VI_A.0.5.2 -->

*Proof.* Let `k′` be the perfect closure of the residue field `k` of `A`. Since the underlying topological spaces of `G`
and `H` are unchanged under the base change `A → k → k′`, we may suppose that `A = k` is a perfect field. We may then
suppose that `G` and `H` are reduced, hence geometrically reduced.

Let `H̄` be the closure of `H`; then `µ⁻¹(H̄)` is a closed subset of `G × G` containing `H × H`. Since the morphism
`H → Spec k` (resp. `H̄ → Spec k`) is universally open, and since `H` is dense in `H̄`, then `H × H` is dense in
`H × H̄` and `H × H̄` is dense in `H̄ × H̄`, so `H × H` is dense in `H̄ × H̄`. Therefore `µ(H̄ × H̄) ⊂ H̄`, and so,
since `H̄ × H̄` is reduced, `µ` induces a morphism `µ′ : H̄ × H̄ → H̄`.

Let then `g ∈ H̄`, and set `K = κ(g)`. Since the projection `H̄_K → H̄` is open, `H_K` and `ℓ_g(H_K)` are two dense open
subsets of `H̄_K`, so there exist `u, v ∈ H_K` such that `ℓ(g)(v) = u`. One concludes, as in the proof of 0.5, that `g`
belongs to `H · H = H`, whence `H̄ = H`.

## 1. Local properties of an `A`-group locally of finite type

<!-- label: III.VI_A.1 -->

<!-- original page 292 -->

We shall first see that, if `G` is locally of finite type and flat over `A`, one can "make strictly rational any closed
point of `G`" by means of a finite, flat extension of the base.

### 1.1.

Unless explicit mention is made to the contrary, we assume from now on that `G` is an `A`-group locally of finite type.
When `A` is a field `k`, we shall obtain in Exposé VII_B very precise results on the local rings of `G`.[^N.D.E-VI_A-10]
We content ourselves here with a few elementary results:

**Proposition 1.1.1.** *Let `x` be a point of an `A`-group `G` locally of finite type and flat over `A`. Then the local
ring `O_{G,x}` is Cohen–Macaulay, and there exists a system `a_1, …, a_n` of parameters of `O_{G,x}` such that
`O_{G,x}/(a_1, …, a_n)` is a finite and flat (hence finite and free) `A`-module.*

<!-- label: III.VI_A.1.1.1 -->

We first assume `A` equal to its residue field `k`; it then suffices to prove that `O_{G,x}` is Cohen–Macaulay and one
may limit oneself to the case where `x` is a closed point (cf. EGA 0_IV, 16.5.13). By Lemma 1.1.2 below, `G` contains a
closed point `y` such that `O_{G,y}` is Cohen–Macaulay. By SGA 1, I § 9, this amounts to saying that, for every finite
extension `K` of the base field `k` and every point `ȳ` of `Ḡ = G ⊗_k K` above `y`, `O_{Ḡ,ȳ}` is Cohen–Macaulay. If the
extension `K` has been chosen large enough — i.e. if `K` contains a normal extension of `k` containing the residue
fields `κ(y)` and `κ(x)` — then `ȳ` is (strictly) rational over `K`, as is every point `x̄` of `Ḡ` above
`x`.[^N.D.E-VI_A-11] Since the automorphism `r_{x̄} ∘ (r_{ȳ})⁻¹` sends `ȳ` to `x̄`, it follows that `O_{Ḡ,x̄}`, and
hence `O_{G,x}` (SGA 1, I § 9), are Cohen–Macaulay.

<!-- original page 293 -->

When `A` is again assumed arbitrary, the preceding argument applies to `k ⊗_A G`, so that `k ⊗_A O_{G,x}` is
Cohen–Macaulay. If `a_1, …, a_n` is a sequence of elements of `O_{G,x}` whose image in `k ⊗_A O_{G,x}` is a system of
parameters, it follows from SGA 1, IV 5.7 or from EGA 0_IV, 15.1.16, that `a_1, …, a_n` is an `O_{G,x}`-regular sequence
and that `O_{G,x}/(a_1, …, a_n)` is finite and flat (hence finite and free) over `A`.

**Lemma 1.1.2.** *Every non-empty scheme `X`, locally of finite type over an Artinian ring `A`, contains a closed point
`x` whose local ring is Cohen–Macaulay.*

<!-- label: III.VI_A.1.1.2 -->

We may of course assume `X` affine with algebra `B`, and argue by induction on `dim X` (the assertion is clear if `X` is
discrete, since all local rings are then Artinian). Since `B` is of finite type over `A`, if `dim B > 0`, `B` contains
an element `a` that is non-invertible and not a zero-divisor.[^N.D.E-VI_A-12] The closed subscheme `X′ = Spec B/(a)` of
`X` is then of dimension strictly less than `dim X`, and by induction contains a closed point `x` such that `O_{X′,x}`
is Cohen–Macaulay. Since `O_{X′,x} = O_{X,x}/(a)` and `a` is non-invertible and not a zero-divisor in `O_{X,x}`, then
`O_{X,x}` is Cohen–Macaulay (see also EGA IV_2, 6.11.3).

**Proposition 1.2.** *Let `A` be an Artinian local ring, `G` an `A`-group locally of finite type and flat over `A`, and
`x` a closed point of `G`. There exists an `A`-algebra `A′` that is local, finite and free over `A`, such that every
point of `G ⊗_A A′` above `x` is strictly rational over `A′`.*

<!-- label: III.VI_A.1.2 -->

<!-- original page 294 -->

[^N.D.E-VI_A-13] Indeed, let `k_1` be a normal extension of finite degree of `k` containing the residue field `κ(x)` of
`x`. By Lemma V 4.1.2, there exists an `A`-algebra `A_1` that is local, finite and free over `A`, with residue field
`k_1`. In this case (cf. N.D.E. (11)) all the points `g_1, …, g_n` of `G ⊗_A A_1` above `x ∈ G` have `k_1` as residue
field (i.e. `g_1, …, g_n` are rational over `A_1` in the sense of Exp. V, § 4.e)).

Let then `B_1, …, B_n` be the local rings of `g_1, …, g_n`. By 1.1.1, `B_1, …, B_n` have quotients `B′_1, …, B′_n` that
are Artinian and finite and free over `A_1`. Set `A′ = B′_1 ⊗_{A_1} ⋯ ⊗_{A_1} B′_n`. Then `A′` is local, finite and free
over `A_1` and, for each `i = 1, …, n`, we have surjective homomorphisms

```text
B_i ⊗_{A_1} A′ ↠ B′_i ⊗_{A_1} A′ ↠ A′,
```

the second induced by the multiplication map `B′_i ⊗_{A_1} B′_i ↠ B′_i`. Consequently, `A′` answers the question.

### 1.3.

Let `e` denote the unit element (or origin) of `G`, i.e. the image of the unique point of `Spec A` by the unit section
`Spec A → G`. By definition itself, `e` is strictly rational over `A`.

**Proposition 1.3.1.** [^N.D.E-VI_A-14] *Let `G` be a group locally of finite type and flat over an Artinian ring `A`,
and `K` (resp. `k̄`) the perfect closure (resp. an algebraic closure) of the residue field `k` of `A`.*

*(1) For every closed point `x` of `Ḡ = G ⊗_k k̄`, the local rings `O_{Ḡ,ē}` and `O_{Ḡ,x}` are isomorphic. In
particular, the tangent spaces `T_e G` and `T_x G` have the same dimension.*

*(2) The following assertions are equivalent:*

*(i) `G ⊗_A K` is reduced.* *(i bis) `O_{G,e} ⊗_A K` is reduced.* *(ii) `G` is smooth over `A`.* *(ii bis) `G` is smooth
over `A` at the origin.*

<!-- label: III.VI_A.1.3.1 -->

*Proof.* (1) Let `x` be a closed point of `Ḡ`; there is exactly one `k̄`-morphism `s : Spec k̄ → Ḡ` whose image is `x`;
right translation `r_s` then induces an isomorphism from `O_{Ḡ,ē} = O_{G,e} ⊗_k k̄` onto `O_{Ḡ,x}`, whence assertion
(1).

<!-- original page 295 -->

Let us prove assertion (2). By SGA 1, II.2.1, one reduces immediately to the case where `A` is a field (`A = k`). The
implications (i) ⇒ (i bis), (ii) ⇒ (ii bis), (ii) ⇒ (i) and (ii bis) ⇒ (i bis) are obvious, so it suffices to prove that
(i bis) implies (ii).

Now, it follows from (i bis) that `O_{G,e} ⊗_k k̄` is reduced. Hence, by (1), `O_{Ḡ,x}` is reduced for every closed
point `x` of `Ḡ`, so that `Ḡ` is reduced. Then, since `Ḡ` is locally of finite type over `k̄`, there exists at least one
closed point `y` such that `O_{Ḡ,y}` is regular. Since, by (1), the local rings of the closed points of `Ḡ` are all
isomorphic to `O_{Ḡ,ē}`, one sees that all these local rings are regular, so that `Ḡ` is smooth over `k̄`, and hence `G`
is smooth over `k`.

[^N.D.E-VI_A-15] One may now give the examples below, signalled by M. Raynaud, of group schemes `G` over a non-perfect
field `k` such that `G_red` is not a group scheme over `k`.

**Examples 1.3.2.** *Let `k` be a non-perfect field of characteristic `p > 0`, `t ∈ k − k^p`, `k̄` an algebraic closure
of `k`, and `α ∈ k̄` such that `α^p = t`.*

<!-- label: III.VI_A.1.3.2 -->

*(1) Consider the additive group `G_{a,k} = Spec k[X]`, and let `G` be the group subscheme, finite over `k`, defined by
the additive polynomial `X^{p²} − tX^p`. Then*

```text
G_red = Spec k[X]/X(X^{p(p−1)} − t)
```

*is étale at the origin. If it were a group scheme over `k`, it would be smooth (by 1.3.1); but `G_red` is not
geometrically reduced, so it is not a group scheme over `k`.*

*(2) Consider `G_{a,k}^4 = Spec k[X, Y, U, V]` and let `G` be the group subscheme defined by the ideal `I` generated by
the additive polynomials `P = X^p − tY^p` and `Q = U^p − tV^p`. Then `G` is of dimension 2 and irreducible, since
`(G_{k̄})_red ≅ Spec k̄[Y, V]` is.*

Let `A = k[X, Y, U, V]` and `𝔪` its augmentation ideal. Denote by `x, y, u, v` the images of `dX, dY, dU, dV` in
`Ω¹_{A/k} ⊗_A (A/𝔪)`, viewed as linear forms on the tangent space `k⁴ = T_0 G_{a,k}^4`. Let us show that the subspace
`E = T_0 G_red` equals `k⁴`. Otherwise, there would exist a linear form `f = ax + by + a′u + b′v`, with
`a, b, a′, b′ ∈ k` not all zero, vanishing on `E`. Recall that the formation of `Ω¹_{A/k}` (and hence of tangent spaces)
commutes with base change (cf. EGA IV_4, 16.4.5), and identify `f` with its image in `(k̄⁴)*`. Since
`(G_{k̄})_red ⊂ (G_red)_{k̄}`, then `f` vanishes on the subspace `T_0 (G_{k̄})_red` of `k̄⁴`, which is defined by the
equations `g_1 = x − αy` and `g_2 = u − αv`, and so `f = λg_1 + µg_2`, with `λ, µ ∈ k̄`. Now `λg_1 + µg_2` belongs to
`k⁴` only if `λ = µ = 0`! This contradiction shows that `E = k⁴`, and so `T_0 (G_red)_{k̄} = k̄⁴`.

On the other hand, `R = XV − YU` belongs to `√I`, since `R^p = (X^p − tY^p)V^p − Y^p(U^p − tV^p)`. Consequently, the
tangent space `F` at the point `(α, 1, α, 1)` of `(G_red)_{k̄}` is contained in the hyperplane `H` of `k̄⁴` with
equation `α dV + dX − dU − α dY = 0`, hence is of dimension `≤ 3`.[^N.D.E-VI_A-16] Therefore, by point (1) of 1.3.1,
`G_red` is not a group scheme over `k`.

## 2. Connected components of an `A`-group locally of finite type

<!-- label: III.VI_A.2 -->

<!-- original page 296 -->

### 2.1.

Let us first consider an arbitrary `A`-group `G`, and let `G′` be the connected component of the origin `e` of `G`. This
connected component is evidently closed, so that we may identify it with the reduced closed subscheme of `G` having `G′`
as underlying space.[^N.D.E-VI_A-17]

**Proposition 2.1.1.** *For every extension `K` of the residue field `k` of `A`, `G′ ⊗_A K` has as underlying space the
connected component of the origin in the `K`-group `G ⊗_A K` (i.e. `G′` is geometrically connected).*

<!-- label: III.VI_A.2.1.1 -->

Indeed, let `(G ⊗_A K)′` be the connected component of the origin in `G ⊗_A K`. Since the image of `(G ⊗_A K)′` in `G`
is connected and contains the unit element of `G`, this image is contained in `G′`, so that `(G ⊗_A K)′` is contained in
the inverse image

<!-- original page 300 -->

`G′ ⊗_A K` of `G′` in `G ⊗_A K`. The proposition therefore follows from the connectedness of `G′ ⊗_A K`, which is proved
in Lemma 2.1.2.

**Lemma 2.1.2.** *Let `X` and `Y` be two connected schemes over a field `k`. If `X` contains a rational point, then
`X ×_k Y` is connected.*

<!-- label: III.VI_A.2.1.2 -->

We give below a direct proof of this result from EGA IV_2 (4.5.8 and 4.5.14).

Suppose first `Y` non-empty, connected and affine, with algebra `B`. In this case, `X ×_k Y` is the spectrum of the
quasi-coherent `O_X`-algebra `𝓑 = O_X ⊗_k B`. We want to show that every subset `U` of `X ×_k Y` that is open, closed,
and non-empty coincides with `X ×_k Y`. Now `U` is affine over `X` and its affine `O_X`-algebra is a direct factor of
`𝓑`. It therefore follows from Lemma 2.1.3 below that the image of `U` in `X` is open and closed,

<!-- original page 297 -->

i.e. coincides with all of `X`. This image contains in particular a rational point `x` of `X`, so that `U` meets the
inverse image of `x` in `X ×_k Y`. Since this inverse image is isomorphic to `Y`, hence connected, `U` contains this
inverse image. The same would hold for the complement of `U` in `X ×_k Y` if `U` were distinct from `X ×_k Y`, which
would be absurd.

If `Y` is now an arbitrary `k`-scheme, what precedes shows that the fibers of the canonical projection `X ×_k Y → Y` are
connected. If `x` is a rational point of `X`, these fibers all meet the subscheme `{x} ×_k Y`, which is itself
connected, whence the proposition.

**Lemma 2.1.3.** *Let `X` be a scheme and `𝓐` a quasi-coherent `O_X`-algebra which is locally[^N.D.E-VI_A-18] a direct
factor of a free `O_X`-module. The image of `Spec 𝓐` in `X` is then open and closed.*

<!-- label: III.VI_A.2.1.3 -->

Let `V` be this image. It is clear that `V` is contained in the support of `𝓐`. Conversely, if `x` belongs to the
support of `𝓐`, then `𝓐_x` is non-zero and is a free `O_{X,x}`-module, since by Kaplansky every projective module over a
local ring is free. Consequently the fiber of `Spec 𝓐` at `x`, which is affine with algebra `𝓐_x ⊗_{O_{X,x}} κ(x)`, is
non-empty. One thus sees that the image of `Spec 𝓐` coincides with the support of `𝓐`.

If `s` is the unit section of `𝓐`, the equality `s_x = 0` implies that `s`, and hence `𝓐`, are

<!-- original page 298 -->

zero in a neighborhood of `x`. So the support of `𝓐` is closed. On the other hand, one may assume that `𝓐` is a direct
factor of the direct sum `L` of a family `(O_X^α)` of copies of `O_X`.[^N.D.E-VI_A-19] For every `β`, write `φ_β` for
the restriction to `𝓐` of the canonical projection of `L = ⊕_α O_X^α` onto `O_X^β`. For `x ∈ X`, denote by `𝓐_x^*` the
dual module `Hom_{O_{X,x}}(𝓐_x, O_{X,x})`. Since `𝓐_x` is a direct factor of `L_x`, the restriction map

```text
Hom_{O_{X,x}}(L_x, O_{X,x}) → Hom_{O_{X,x}}(𝓐_x, O_{X,x}) = 𝓐_x^*
```

<!-- original page 299 -->

is surjective. If `𝓐_x ≠ 0` then, since `𝓐_x` is free and non-zero, there exist `a ∈ 𝓐_x` and a linear form `φ ∈ 𝓐_x^*`
such that `φ(a) = 1`. There exists therefore a family `(ξ^α)` of elements of `O_{X,x}` such that, for every
`u ∈ 𝓐_{X,x}`, one has `φ(u) = ∑_α ξ^α φ^α(u)` (this sum being finite since `φ^α(u) = 0` except for finitely many `α`).
Applying this to `u = a`, one obtains that there exist `α_1, …, α_n` such that

```text
1 = φ(a) = ξ^{α_1} φ^{α_1}(a) + ⋯ + ξ^{α_n} φ^{α_n}(a).
```

There exists then an open neighborhood `U` of `x` such that `a` and the `ξ^{α_i}` come from sections `ã ∈ 𝓐(U)` and
`ξ̃^{α_i} ∈ O_X(U)`, and the equality `∑_i ξ̃^{α_i} φ^α(ã) = 1` on `U` shows that `ã_y ≠ 0` for every `y ∈ U`. ("The
support of a projective module is open.")

### 2.2.

The notations being still those of 2.1, it is clear that `G′` is a reduced `k`-scheme. Lemma 2.1.2 shows that
`G′ ×_k G′` is connected, so that `(G′ ×_k G′)_red` is the reduced subscheme of `G ×_A G` having as underlying space the
connected component of the origin. In particular, the multiplication morphism `µ : G ×_A G → G` induces a morphism
`µ′ : (G′ ×_k G′)_red → G′` that makes `G′` a group in `(Sch/k)_red`.

### 2.2.bis.

[^N.D.E-VI_A-20] One recalls (cf. Exp. V) that, if `P` is a scheme, one writes `P` for the underlying topological space
of `P`. Now one defines a sub-`A`-functor `G⁰` of `G` by setting, for every `A`-scheme `S`,

```text
G⁰(S) = {u ∈ G(S) | u(S) ⊂ G′}.
```

Let `c : G → G` be the inversion morphism; since `c(G′) = G′`, we have `c ∘ u ∈ G⁰(S)` for every `u ∈ G⁰(S)`. On the
other hand, if `u, v ∈ G⁰(S)`, then `u ⊠ v` sends `S` into the subspace of `G ×_A G` consisting of points whose two
projections belong to `G′`; this subspace is identified with the underlying space of `G′ ×_A G′`, which is connected by
Lemma 2.1.2. Consequently, `µ ∘ (u ⊠ v)` sends `S` into `G′`. This shows that `G⁰` is a sub-`A`-functor in groups of
`G`.

If the connected component of `e` is open in `G`, then the subfunctor `G⁰` is representable by the subscheme induced by
`G` on this open set, which is therefore a group subscheme of `G`; we shall also write `G⁰` for it. In this case, with
the notations of 2.1, one has `G′ = (G⁰)_red` and the topological spaces `G′` and `G⁰` coincide.[^N.D.E-VI_A-21]

### 2.3.

In accordance with our conventions of 1.1, we again assume from now on that `G` is locally of finite type over `A`. Then
`G` is locally noetherian, hence locally connected,[^N.D.E-VI_A-22] hence: every connected component of `G` is open.

We then write `G⁰` for the subscheme induced by `G` on the connected component `G′` of the unit element. By 2.2.bis,
`G⁰` is a group subscheme of `G`, which we shall call the *neutral component* of `G`;

<!-- original page 300 -->

for every `A`-scheme `S` we therefore have:

```text
G⁰(S) = {u ∈ G(S) | u(S) ⊂ G⁰ = G′}.
```

Let `G^α` be an arbitrary connected component of `G` and `ν^α : G^α ×_A G⁰ → G` the morphism defined by the equalities

```text
ν^α(S)(g, γ) = gγg⁻¹,
```

for every `S ∈ (Sch/A)`, `g ∈ G^α(S)`, `γ ∈ G⁰(S)`.

If `e` is the origin of `G`, the restriction of `ν^α` to `G^α ×_A {e}` is the trivial morphism; since `G^α ×_A G⁰` is
connected by 2.1.2, one sees that `ν^α` factors through `G⁰`. Therefore, for every `A`-scheme `S`, `G⁰(S)` is a normal
subgroup of `G(S)`. We have thus obtained the following proposition:[^N.D.E-VI_A-23]

**Proposition 2.3.1.** *Let `G` be an `A`-group locally of finite type. Then the neutral component `G⁰` is an open
normal group subscheme of `G`.*

<!-- label: III.VI_A.2.3.1 -->

**Proposition 2.4.** *Let `G` be an `A`-group locally of finite type.*

*(i) `G⁰` is irreducible, and `G⁰ ⊗_A k` is geometrically irreducible over `k`.*

*(ii) `G⁰` is quasi-compact, hence of finite type over `A`.*

<!-- label: III.VI_A.2.4 -->

[^N.D.E-VI_A-24] *Proof.* (i) Since `G⁰` and `G⁰ ⊗_A k` have the same underlying topological space, it suffices to show
the second assertion. Let `k̄` be an algebraic closure of `k`. By 2.2, `(G ⊗_A k̄)_red` is a `k̄`-group locally of
finite type and reduced, hence smooth over `k̄` (1.3.1). A fortiori the local rings of `(G ⊗_A k̄)_red` are integral
domains, so,[^N.D.E-VI_A-25] since `G ⊗_A k̄` is locally noetherian, the connected components of `G ⊗_A k̄` are
irreducible (cf. EGA I, 6.1.10). In particular, the connected component `G⁰ ⊗_A k̄` (cf. 2.1.1) is irreducible.

(ii) Let us now show that `G⁰` is of finite type over `A`. Since `G⁰` is locally of finite type over `A`, it suffices to
prove that `G⁰` is quasi-compact. As `G⁰` is irreducible, this follows from 0.5.1.

<!-- original page 301 -->

**Corollary 2.4.1.** *Every connected component of `G` is irreducible,[^N.D.E-VI_A-26] of finite type over
`A`,[^N.D.E-VI_A-27] and of the same dimension as `G⁰`.*

<!-- label: III.VI_A.2.4.1 -->

One may indeed assume `A` equal to its residue field `k`. Let then `C` be a connected component of `G`, `x` a closed
point of `C`, `κ(x)` the residue field of `x`, and `k′` a normal extension of `k` containing `κ(x)` and of finite degree
over `k`. The canonical projection `π : C ⊗_k k′ → C` is open and closed;[^N.D.E-VI_A-28] consequently, if `C′` is a
connected component of `C ⊗_k k′`, the projection `C′ → C` is surjective, so `C′` contains a point `y ∈ π⁻¹(x)`, and
such a point is rational over `k′` (cf. the proof of 1.2), so that `C′` is the image by translation `r_y` of
`G⁰ ⊗_k k′`. Now `G⁰ ⊗_k k′` is of finite type over `k′` by 2.4, and `π⁻¹(x)` is finite (of cardinality `≤ [k′ : k]`),
so `C ⊗_k k′` is of finite type over `k′`, and hence `C` is of finite type over `k`.

On the other hand, since `G⁰ ⊗_k k′` is irreducible by 2.4, the same holds for `C′`,[^N.D.E-VI_A-29] and hence also for
`C`, since the projection `C′ → C` is surjective.

Finally, we have seen above that `C ⊗_k k′` is a disjoint union of finitely many translates of `G⁰ ⊗_k k′`. Since
dimension is invariant under extension of the base field (cf. EGA IV_2, 4.1.4), it follows that `C` has the same
dimension as `G⁰`. (Moreover, by EGA IV_2, 5.2.1, one has `dim_g G = dim G⁰` for every point `g ∈ G`.)

### 2.5.

This paragraph has been added. The results that follow appear in Exp. VI_B, but could (or should) have figured in VI_A,
and it is useful to have them available from now on, in order to make precise Theorem 3.2 below.

**Lemma 2.5.1.** *Let `(A, 𝔪)` be an Artinian local ring, and `k = A/𝔪` its residue field.*

*(i) If `X` is an `A`-scheme such that `X ⊗_A k` is locally of finite type (resp. of finite type) over `k`, then the
same holds for `X` over `A`.*

*(ii) Let `u : X → Y` be a morphism of `A`-schemes. If `u ⊗_A k` is an immersion (resp. a closed immersion), then so is
`u`.*

<!-- label: III.VI_A.2.5.1 -->

*Proof.* (i) Suppose `X ⊗_A k` locally of finite type over `k`. Let `U = Spec B` be an affine open of `X`. By
hypothesis, there exist elements `x_1, …, x_n` of `B` whose images generate `B/𝔪B` as a `k`-algebra, and it follows from
the "nilpotent Nakayama lemma" that the `x_i` generate `B` as an `A`-algebra. This proves that `X` is locally of finite
type over `A`. If, in addition, `X ⊗_A k` is quasi-compact, then so is `X` (which has the same underlying topological
space), and hence `X` is of finite type over `A`. This proves (i).

Let us prove (ii). Suppose `u ⊗_A k` is an immersion (resp. a closed immersion). Then `u` is a homeomorphism of `X` onto
a locally closed (resp. closed) part of `Y`, and for every `x ∈ X`, the ring morphism `φ_x : O_{Y,u(x)} → O_{X,x}` is
such that `φ_x ⊗_A k` is surjective. By the nilpotent Nakayama lemma, it follows that `φ_x` is surjective, so `u` is an
immersion (resp. a closed immersion).

**Proposition 2.5.2.** *Let `A` be an Artinian local ring with residue field `k`, and let `u : G → H` be a quasi-compact
morphism between `A`-group schemes locally of finite type.*

*(a) The set `u(G)` is closed in `H`, and its connected components are irreducible and all of the same dimension.*

*(b) One has `dim G = dim u(G) + dim Ker(u)`.*

*(c) If `u` is a monomorphism, it is a closed immersion.*

<!-- label: III.VI_A.2.5.2 -->

*Proof.* By the preceding lemma, it suffices to prove the proposition in the case where `A = k`. Moreover, since the
properties under consideration are stable by

<!-- original page 304 -->

(fpqc) descent, and since dimension is invariant under extension of the base field, one may assume `k` algebraically
closed.

Let us prove (a). Denote by `C` the reduced subscheme of `H` whose underlying topological space is `u(G)`. Since `u(G)`
is stable under the inversion morphism of `H`, so is `C`. On the other hand, `u : G → C` is quasi-compact and dominant,
so by EGA IV_2, 2.3.7 the same holds for `u ×_k id_G` and `id_H ×_k u`, and hence for their composition
`u ×_k u : G ×_k G → C ×_k C`. Consequently, the multiplication of `H` sends `C ×_k C` into `C`, and so `C` is a group
subscheme of `H`.

So, replacing `H` by `C`, we reduce to the case where `u` is dominant. Then `G(k)` is dense in `H`, hence meets every
connected component of `H`, and hence acts transitively on the set of these connected components. It therefore suffices
to show that `u(G)` contains `H⁰`. Replacing `G` by `u⁻¹(H⁰)`, we may suppose `H = H⁰`; in this case, by 2.4, `H` is
irreducible and of finite type over `k`, hence noetherian. On the other hand, `u` is locally of finite type (cf. EGA I,
6.6.6) and quasi-compact, hence of finite type. Consequently, by Chevalley's constructibility theorem (cf. EGA IV_1,
1.8.5), `u(G)` is a constructible (and dense) part of `H = u(G)`, hence contains a dense open `U` of `H` (cf. EGA 0_III,
9.2.2). Then, by 0.5, one has `H = U · U ⊂ u(G)`, whence `u(G) = H`. Taking 2.4.1 into account, this proves assertion
(a).

Let us prove (b). Recall first that the functor `Ker(u)` (cf. I, 2.3.6.1) is representable by `u⁻¹(e)`, where `e`
denotes the unit element of `H`. Since `u` is of finite type, `Ker(u)` is of finite type over `k`. On the other hand,
replacing `H` by the reduced closed subscheme `u(G)`, we may assume `u` surjective. Denote by `u⁰` the restriction of
`u` to `G⁰`. Since `G` and `Ker(u)` are equidimensional, and since `Ker(u)⁰ ⊂ Ker(u⁰)`, we reduce to the case where `G`,
and hence also `H`, are irreducible.

Then, by EGA IV_3, 9.2.6.2 and 10.6.1 (ii), the set of `y ∈ H` such that `dim u⁻¹(y) = dim G − dim H` contains a
non-empty open set `V`. Since `u` is surjective, `U = u⁻¹(V)` is then a non-empty open subset of `G`, hence contains a
closed point `x` of `G`, since `G` is a Jacobson scheme (cf. EGA IV_3, 10.4.8). Then right translation `r_x` is an
isomorphism of `Ker(u)` onto `u⁻¹(u(x))`, whence:

```text
dim Ker(u) = dim u⁻¹(u(x)) = dim G − dim H.
```

Let us prove (c), following [DG70], I, § 3.4. (Another proof is given in Exp. VI_B, 1.4.2.) Assume `u` a monomorphism.
If `C` is a connected component of `G`, there exists a closed point `x ∈ G` such that `C = r_x(G⁰)`, and if one denotes
by `u_C` (resp. `u⁰`) the restriction of `u` to `C` (resp. to `G⁰`), one has `u_C = r_{u(x)} ∘ u⁰ ∘ r_x^{-1}`, so it
suffices to show that `u⁰` is a closed immersion. We may therefore suppose `G = G⁰`, so that `G` is irreducible and of
finite type over `k`.

Let `ξ` be the generic point of `G`; then `O_{G,ξ}` is an Artinian local ring; denote by `𝔪` its maximal ideal. On the
other hand, let `h = u(ξ)`, `𝔫` the maximal ideal of `O_{H,h}`, and `A = O_{G,ξ}/𝔫 O_{G,ξ}`. Since `u` is a
monomorphism, so is the morphism `u_h : Spec(A) → Spec(κ(h))` obtained by base change, so the multiplication morphism
`A ⊗_{κ(h)} A → A` is an isomorphism (cf. EGA I, 5.3.8), whence `A = κ(h)`. By Nakayama's lemma (since `𝔫 O_{G,ξ}` is
contained in `𝔪`, hence nilpotent), it follows that the morphism `O_{H,h} → O_{G,ξ}` is surjective.

<!-- original page 305 -->

Let then `V` be an affine open of `H` containing `h`, `U` a non-empty affine open of `G` contained in `u⁻¹(V)`,
`φ : O_H(V) → O_G(U)` the morphism of `k`-algebras induced by `u`, `𝔭` the prime ideal of `O_G(U)` corresponding to `ξ`,
and `𝔮 = φ⁻¹(𝔭)`. Since `G` is of finite type over `k`, `O_G(U)` is generated as a `k`-algebra by a finite number of
elements `a_1, …, a_n`. By what precedes, there exist elements `b_1, …, b_n` and `s` in `O_H(V)` such that `s ∉ 𝔮` and
such that one has in `O_G(U)_𝔭` the equalities `a_i/1 = φ(b_i)/φ(s)`. There exist therefore elements `t_1, …, t_n` of
`O_G(U) − 𝔭` such that `t_i(a_i φ(s) − φ(b_i)) = 0`. Then, setting `t = t_1 … t_n φ(s) ∈ O_G(U) − 𝔭`, the equalities
`a_i/1 = φ(b_i)/φ(s)` already hold in `O_G(U)_t` and, since `t ∈ O_G(U) = k[a_1, …, a_n]`, there exists `b ∈ O_H(V)`
such that `t/1 = φ(b)/φ(s)^r`, for some `r ∈ ℕ`. Consequently, `φ` induces a surjection of `O_H(V)_{sb}` onto
`O_G(U)_t`, and so `u` is a local immersion at the point `ξ`.

The open subset `W` of `G` consisting of the points at which `u` is a local immersion is therefore non-empty. Since `G`
is a Jacobson scheme, `W` contains a closed point `y`, and to show `W = G`, it suffices to show that every closed point
of `G` belongs to `W`. Now every closed point `x` is the image of `y` by translation `r_x ∘ r_y^{-1}`, hence belongs to
`W`, whence `W = G`. This proves that `u` is a local immersion.

Since `G` is irreducible, it follows that `u` is an immersion. Indeed, for every `x ∈ G`, let `U_x` and `V_x` be open
subsets of `G` and `H` such that `x ∈ U_x` and such that `u` induces a closed immersion of `U_x` into `V_x`. Since `U_x`
is dense in `G`, `u(U_x)` is dense in `u(G) ∩ V_x`, and since `u(U_x)` is closed in `V_x`, one has `u(U_x) = V_x`.
Moreover, since `u` is injective, one has `U_x = u⁻¹(V_x)`, and it follows that `u` induces a closed immersion of `G`
into the open subscheme of `H` covered by the `V_x`. So `u : G → H` is an immersion. But we have already seen that
`u(G)` is closed in `H`, hence `u` is a closed immersion.

**Lemma 2.5.3.** [^N.D.E-VI_A-30] *Let `A` be an Artinian local ring, `k` its residue field, `G` a flat `A`-group, `X`
an `A`-scheme equipped with a left action `µ : G ×_A X → X` of `G` and with a section `s_0 : Spec A → X`. (This is the
case, for instance, if `G′` is a second `A`-group and one is given an `A`-group morphism `G → G′`.)*

*Let `φ` be the morphism `µ ∘ (id_G × s_0)` from `G = G ×_A A` to `X`. If `φ` is flat at a point `g` of `G`, then `φ` is
flat.*

<!-- label: III.VI_A.2.5.3 -->

*Proof.* Since `G` is flat over `A`, the flatness-by-fibers criterion (EGA IV_3, 11.3.10.2) shows that it suffices to
show that `φ ⊗_A k` is flat; hence we may suppose `A = k`. In this case, the datum of `s_0` is equivalent to that of a
`k`-point `x_0 ∈ X(k)`, and `φ` is the morphism `h ↦ h x_0`.

Let then `h ∈ G`; let us show that `φ` is flat at the point `h`. Let `K` be an extension of `k` containing a copy of
`κ(g)` and of `κ(h)`; one has a cartesian square

```text
            φ_K
G_K ────────────→ X_K
 │                 │
 │                 │
 ▼      φ          ▼
 G ────────────→ X
```

<!-- original page 306 -->

in which the two vertical arrows are faithfully flat. So, by V 7.4 (i), `φ_K` is flat at every point `g′ ∈ G_K` above
`g`, and to show that `φ` is flat at `h`, it suffices to show that `φ_K` is flat at a point `h′` above `h`. We are thus
reduced to the case where `g` and `h` are rational. Let then `u = h g⁻¹` and `ℓ_u` (resp. `µ_u`) the left translation of
`G` (resp. of `X`) defined by `u`; since `φ ∘ ℓ_u = µ_u ∘ φ`, one obtains a commutative square

```text
                ~
O_{G,h} ──────────→ O_{G,g}
    ▲                  ▲
    │                  │
    │       ~          │
O_{X, hx_0} ────→ O_{X, gx_0}
```

in which the horizontal arrows are isomorphisms. Since the morphism `O_{X, gx_0} → O_{G,g}` is flat, the morphism
`O_{X, hx_0} → O_{G,h}` is also flat.

**Proposition 2.5.4.** *Let `A` be an Artinian local ring, `k` its residue field, `G` an `A`-group locally of finite
type, `X ≠ ∅` an `A`-scheme locally of finite type equipped with a left action of `G`. Assume that the morphism
`φ : G ×_A X → X ×_A X` defined set-theoretically by `(g, x) ↦ (gx, x)` is surjective. Then:*

*(i) The connected components of `X` are of finite type, irreducible, and all of the same dimension.*

*(ii) More precisely, let `k̄` be an algebraic closure of `k` and `x` a closed point of `X ⊗_A k̄`; its stabilizer `F`
is a closed group subscheme of `G ⊗_A k̄`, and the dimension of the irreducible components of `X` is `dim G − dim F`.*

<!-- label: III.VI_A.2.5.4 -->

Taking Lemma 2.5.1 into account, we may suppose `A = k`. Suppose first `k` algebraically closed. Then `G_red` is a
`k`-group locally of finite type, and hence, replacing `G` by `G_red` and `X` by `X_red`, we may suppose `G` and `X`
reduced.

Since `G ×_k X` is locally of finite type over `k`, `φ` is locally of finite type (cf. EGA I, 6.6.6 (v)), hence locally
of finite presentation since `X ×_k X` is locally noetherian. Let `x` be a rational point of `X`; then the morphism
`φ_x : G → X` obtained from `φ` by base change is surjective and locally of finite presentation. If `η` is a maximal
point of `X`, then `O_{X,η}` is a field (since `X` is reduced), so `φ_x` is flat at every point of `G` above `η`. So, by
Lemma 2.5.3, `φ_x` is flat. Consequently, `φ_x : G → X` is faithfully flat and locally of finite presentation, hence
open (cf. EGA IV_2, 2.4.6). Since `G⁰` is open in `G`, irreducible and quasi-compact (by 2.4), each orbit
`G⁰ x = φ_x(G⁰)`, for `x` running through the rational points of `X`, is an open subset of `X`, irreducible and
quasi-compact, hence of finite type over `k` (since `X` is locally of finite type over `k`).

Since every non-empty open subset of `X` contains a rational point, it follows that `X` is covered by these open sets.
Moreover, two such open sets are either disjoint or equal. Indeed, if `φ_x(G⁰) ∩ φ_y(G⁰)` is non-empty, it contains a
rational point `z`, and there exist therefore two rational points `g, h ∈ G⁰` such that `gx = z = hy`, whence `x = g⁻¹z`
and `y = h⁻¹z`, and so `φ_x(G⁰) = φ_z(G⁰) = φ_y(G⁰)`. It follows that the orbits `φ_x(G⁰)` are also closed, and so are
at once the connected components and the irreducible components of `X`.

<!-- original page 307 -->

Finally, let `x, y` be two rational points of `X`. Since `φ_x` is surjective, there exists a rational point `g ∈ G` such
that `y = gx`, and since `G⁰` is a normal subgroup of `G`, the orbit `G⁰ y` is the image of `G⁰` under translation `ℓ_g`
of `X`, so that `G⁰ y` and `G⁰ x` have the same dimension.

Moreover, by I, 2.3.3.1, the stabilizer of `x` is represented by the closed subscheme `F` of `G` defined by the
cartesian square below:

```text
F ─────────→ G
│            │
│            │ φ_x
▼            ▼
Spec k ────→ X.
```

Then `F` is a `k`-group locally of finite type, `F ∩ G⁰` is a `k`-group of finite type containing `F⁰`, and by 2.4.1,
`F` and `F ∩ G⁰` are equidimensional, of the same dimension as `F⁰`. Let `C = φ_x(G⁰)` be the irreducible component of
`X` containing `x`. Proceeding as in the proof of point (b) of 2.5.2, one obtains that
`dim C = dim G⁰ − dim F⁰ = dim G − dim F`.

In the general case (i.e. for `k` an arbitrary field), let `k̄` be an algebraic closure of `k`. Let `C` be a connected
component of `X` and `C′` a connected component of `C ⊗_k k̄`; then `C′` is a connected component of `X′ = X ⊗_k k̄`.
The morphism `π : X′ → X` is open (cf. EGA IV_2, 2.4.10), and since it is integral, it is also closed; consequently
`π(C′) = C`. Since `C′` is irreducible and quasi-compact, `C` is irreducible and quasi-compact, hence of finite type
over `k` (since `X` is locally of finite type over `k`).

Finally, since dimension is invariant under extension of the base field (cf. EGA IV_2, 4.1.4), `dim C = dim C′`, and
since all the irreducible components of `X′` have the same dimension, the same holds for those of `X`.

### 2.6. Complements.

This paragraph has been added, drawn from [Per75] II, §§ 1–2, with complements due to O. Gabber.[^N.D.E-VI_A-31] This
shows that the preceding results are valid for any group scheme `G` over a field `k`. (This will be used in sections 5,
6 and 7 of Exp. VI_B.)

We fix a field `k`. Let us begin with the following lemma (loc. cit., II 2.1.1), which does not appear explicitly in EGA
IV_2, § 4.4 (although it can perhaps be read between the lines at the beginning of loc. cit., § 4.4.1).

**Lemma 2.6.0.** *Let `X` be an irreducible `k`-scheme, `K` an extension of `k`, `X′` an irreducible component of `X_K`.
The projection `X′ → X` is surjective.*

<!-- label: III.VI_A.2.6.0 -->

Indeed, let `B` be a transcendence basis of `K` over `k` and `L = k(B) ⊂ K`. By EGA IV_2, 4.3.2 and 4.4.1, `X_L` is
irreducible and `X′` dominates `X_L`. The morphism `X′ → X_L` is therefore integral and dominant, hence surjective.
Since `X_L → X` is surjective (loc. cit., 4.4.1), so is `X′ → X`.

<!-- original page 308 -->

For the rest of 2.6, we fix a `k`-group scheme `G` and an action `µ : G × X → X` of `G` on a `k`-scheme `X` satisfying
the following condition:

```text
(⋆)    the morphism Φ : G × X → X × X, (g, x) ↦ (gx, x) is surjective
```

(this is the case in particular for `G` acting on itself by left translations). We shall then say, for short: "Let `X`
be a `G`-scheme satisfying (⋆)". Finally, we write `k′` for the perfect closure of `k`.

**Proposition 2.6.1.** *Let `X` be a `G`-scheme satisfying `(⋆)`.*

*(i) `X` is geometrically pointwise irreducible over `k`, i.e. for every extension `K` of `k`, each `x ∈ X_K` belongs to
a unique irreducible component of `X_K`.*

*(ii) Each local ring of `(X_{k′})_red` is normal.*

*(iii) Let `η` be a maximal point of `(X_{k′})_red`, `C = {η}^-`, and `L` the algebraic closure of `k` in `κ(η)`. Then
`C` is an `L`-scheme, and is geometrically irreducible over `L` (i.e. `C ⊗_L K` is irreducible for every extension `K`
of `L`).*

*(iv) In particular, if `x` is a rational point of `X`, then the irreducible component of `X` containing `x` is
geometrically irreducible over `k`.*

<!-- label: III.VI_A.2.6.1 -->

*Proof.* (i) Since hypothesis `(⋆)` is preserved by every base change `k → K`, it suffices to show that each `x ∈ X`
belongs to a unique irreducible component of `X`. Since the morphism `Spec(k′) → Spec(k)` is a universal homeomorphism,
we may moreover assume `k` perfect. We may then assume `G` and `X` reduced. Let `η` be a maximal point of `X` and `z` an
arbitrary point of `Z = {η}^-`. Since `X` is reduced, the local ring `O_{X,η}` equals `κ(η)`, and since `k` is perfect,
for every extension `K` of `k`, `κ(η) ⊗_k K` is normal (cf. EGA IV_2, 6.14.2), so every point of `X_K` above `η` is
normal.

Since `Φ` is surjective, there exists a point `γ` of `G × X` such that `Φ(γ)` has projections `z` and `η`. Let
`K = κ(γ)`; there exist then rational points `g` and `η′` of `G_K` and `X_K` such that `η′` lies above `η` and
`z′ = g η′` lies above `z`. By what precedes, `η′` is a normal point of `X_K`, hence so is `z′`. Since `π : X_K → X` is
flat, it follows that `z = π(z′)` is a normal point of `X` (cf. EGA IV_2, 2.1.13). This proves (ii) and (i).

The first assertion of (iii) then follows from (ii). Then, since `L` is algebraically closed in `κ(η)`, `C` is
geometrically irreducible over `L`, by EGA IV_2, 4.5.9.

Finally, if `X` has a rational point `x`, it follows from (iii) that `L = k`, and so `X` is geometrically irreducible
over `k`. This can also be seen directly as follows (cf. [Per75], II 2.1): let `C` be the irreducible component of `X`
containing `x` and let `K` be an extension of `k`; `X_K` has a unique point `e_K` above `e`, and, by (i), `e_K` belongs
to a unique irreducible component `C′` of `X_K`; on the other hand, by 2.6.0, every irreducible component of `C_K`
contains `e_K`, hence equals `C′`.

**Notation.** Let us write provisionally `C⁰` for the reduced closed subscheme of `G` whose underlying space is the
unique irreducible component of `G` containing the unit element `e`.

<!-- original page 309 -->

**Corollary 2.6.2.** *`C⁰` is geometrically irreducible over `k` and is set-theoretically stable under the group law,
i.e. `(C⁰_{k′})_red` is a subgroup of `(G_{k′})_red`. Consequently, `C⁰` is quasi-compact.*

<!-- label: III.VI_A.2.6.2 -->

Indeed, by 2.6.1, `C⁰` is geometrically irreducible over `k`, so `C⁰ × C⁰` is irreducible, so `ν(C⁰ × C⁰) ⊂ C⁰`, where
`ν` denotes the morphism `(g, h) ↦ gh⁻¹`. Since `Spec k′ → Spec k` is a universal homeomorphism, the same conclusion
holds for `C⁰_{k′}`, and then for `H = (C⁰_{k′})_red`, and so, since `H ×_{k′} H` is reduced, `ν` induces a morphism
`H ×_{k′} H → H`, i.e. `H` is a subgroup of `(G_{k′})_red`. Consequently, by 0.5.1, `H` (and hence also `C⁰`) is
quasi-compact.

**Recollection 2.6.3.** *Let `Y` be a scheme. Recall (EGA 0_III, 9.1.1) that a subset `E` of `Y` is said to be*
retrocompact *if the inclusion `E ↪ Y` is quasi-compact, and that, by EGA IV_1, 1.9.5 (v) and 1.10.1, if `U` is a
retrocompact open subset of `Y`, then the closure `U^-` of `U` is the union of the closures `{y}^-` of the points
`y ∈ U`, and of course it is enough to take `y` running through the maximal points of `U`, i.e. the maximal points of
`Y` contained in `U`.*

<!-- label: III.VI_A.2.6.3 -->

*Consequently, if `Y` is quasi-separated and if `η` is a maximal point of `Y`, then the intersection of the closed
neighborhoods of `η` equals `{η}^-`: indeed, if `y ∈ Y − {η}^-`, then `y` is contained in an affine open `V` not
containing `η`; since `Y` is quasi-separated, `V` is retrocompact, so `V^-` is the union of the `{ξ}^-`, for `ξ` running
through the maximal points of `Y` belonging to `V`, and hence `η ∉ V^-`, i.e. `Y − V^-` is a closed neighborhood of `η`
not containing `y`.*

**Proposition 2.6.4.** *Let `X` be a `G`-scheme satisfying `(⋆)` and let `U` be an open subset of `X`.*

*(i) `C⁰ U` is an open subset of `X`, equal to the union of the irreducible components of `X` whose generic point
belongs to `U`.*

*(i′) Consequently, if `X` is irreducible, it is quasi-compact.*

*(ii) If moreover `U` is retrocompact in `X`, then `C⁰ U` equals `U^-`, hence is an open-and-closed subset of `X`.*

<!-- label: III.VI_A.2.6.4 -->

*Proof.* (i) First, `C⁰ U` is open, since it is the union, for `g ∈ C⁰`, of the projections of the open sets
`g · U_{κ(g)} ⊂ X_{κ(g)}`, and each projection `X_{κ(g)} → X` is open.

To prove the second assertion of (i), we may replace `k` by `k′` (since `Spec k′ → Spec k` is a universal
homeomorphism), and so assume `k` perfect. We may then assume `G` and `X` reduced, hence geometrically reduced.

Let `η` be a maximal point of `X` contained in `U` and let `Z` be its closure. Consider the morphism `µ′ : C⁰ × Z → X`.
Since `C⁰` is geometrically irreducible, `C⁰ × Z` is irreducible; write `γ` for its generic point. Since `µ′` sends the
point `ε(η)` (where `ε` denotes the unit section of `C⁰`) to `η`, then `γ` is sent to a generization of `η`, hence to
`η`. So `µ′` sends the underlying space of `C⁰ × Z` into `Z`, and so, since `C⁰ × Z` is reduced, `µ′` factors through
`Z`.

Let now `z ∈ Z`. Set `K = κ(z)`. Then the morphism `µ_z : G_K → X_K`, `h ↦ h · z` is surjective; let `α` be a maximal
point of `X_K`; the local ring `O_{X_K, α}` is

<!-- original page 310 -->

a field, since `X_K` is reduced, so `µ_z` is flat at every point of `G_K` above `α`, so `µ_z` is flat, by Lemma 2.5.3.

On the other hand, `µ_z` sends the generic point `ω` of `C⁰_K` to a point `t ∈ Z_K`. Let `β` be a maximal point of `Z_K`
such that `t ∈ {β}^-`; since `µ_z` is flat, there exists a generization `ξ` of `ω` such that `µ_z(ξ) = β`, and since `ω`
is a maximal point of `G_K`, one necessarily has `ξ = ω`, and so `µ_z(ω)` equals `β`, which lies above `η` (since
`Z_K → Z` is flat).

Set `L = κ(ω)` and let `ω_L` and `z_L` be the `L`-points deduced from `ω` and `z`; then `ω_L · z_L = β′` is a point of
`Z_L` above `β`, and so `z_L = ω_L⁻¹ · β′ ∈ C⁰_L · U_L`, whence `z ∈ C⁰ · U`. This proves (i).

Since `C⁰` is quasi-compact, by 2.6.2, point (i′) follows from this: if `X` is irreducible and if `U` is a non-empty
affine open, then `X` equals `C⁰ U`, i.e. is the image of the morphism `C⁰ × U → X`, hence is quasi-compact. Finally, if
`U` is retrocompact in `X`, then (cf. 2.6.3) `U^-` is the union of the `{η}^-` for `η` running through the maximal
points of `X` contained in `U`, hence equals `C⁰ U`. This proves (ii).

One then obtains the following result ([Per75] II Th. 2.4, see also [Per76], Prop. 4.1.1):

**Theorem 2.6.5.** *Let `k` be a field, `G` a `k`-group scheme.*

*(i) There exists a unique group subscheme `G⁰` of `G`, called the* neutral component *of `G`, such that:*

*(a) The underlying space of `G⁰` is the irreducible component of the unit element.* *(b) `G⁰ → G` is a flat closed
immersion, i.e. `O_{G,g} = O_{G⁰,g}` for every `g ∈ G⁰`.*

*(ii) Moreover, `G⁰` is quasi-compact, geometrically irreducible, and is a characteristic subgroup of `G`.*

*(iii) If `G` is connected, then `G = G⁰`.*

<!-- label: III.VI_A.2.6.5 -->

*Proof.* (i) Recall first that `G` is separated (0.3), hence a fortiori quasi-separated. Let `U` be an affine open of
`G` containing the generic point `ω` of `C⁰`. By 2.6.3 and 2.6.4, `U^- = C⁰ U` is at once open and closed, and
`C⁰ = {ω}^-` is set-theoretically the intersection of these open-and-closed parts.

For `U` running through the affine opens containing `ω`, one obtains a projective system of `G`-schemes `U^-`, whose
transition morphisms are affine (since they are closed immersions). One may therefore form the projective limit `G⁰`
(cf. EGA IV_3, 8.2.2), i.e. for every affine open `V` of `G`, `G⁰ ∩ V` is the spectrum of the algebra

```text
lim O_G(V ∩ U) = O_G(V) / ∑_U I_U(V),
→
```

where `I_U(V)` denotes the kernel of `O_G(V) → O_G(V ∩ U)`. It follows that `G⁰` has `C⁰` as underlying space, and that
`G⁰ → G` is a closed immersion. Moreover, for every `g ∈ G⁰`, `O_{G⁰,g}` is the inductive limit, for `V` running through
the affine opens of `G` containing `g`, of the `k`-algebras `O_{G⁰}(V ∩ G⁰) = lim_U O_G(V ∩ U)`, and this double
inductive limit is

<!-- original page 311 -->

identified with

```text
lim lim O_G(V) = O_{G,g}
→   →
 U   V
g∈V⊂U
```

i.e. one has `O_{G⁰,g} = O_{G,g}` (see also EGA IV_2, 5.13.3 (ii)). So `i : G⁰ → G` is a flat closed immersion.
Conversely, this condition implies that `i^*(O_G) = O_{G⁰}`, and so `G⁰` is uniquely determined by conditions (a) and
(b). This proves (i).

The first two assertions of (ii) follow from 2.6.2. Finally, let `S` be a `k`-scheme and `φ` an automorphism of the
`S`-group `G_S`. For every `s ∈ S`, `φ_s` sends `G⁰_{κ(s)}` into itself, so `φ(G⁰_S) ⊂ G⁰_S`. Moreover, the closed
immersion `i_S : G⁰_S ↪ G_S` deduced from `i` by base change is flat, so one has `O_{G_S, φ(z)} = O_{G⁰_S, φ(z)}` for
every `z ∈ G⁰_S`, and so `φ ∘ i_S` factors through `G⁰_S`. This proves that `G⁰` is a characteristic subgroup of `G`,
whence (ii). Finally, (iii) is a particular case of point (i) of the following proposition.[^N.D.E-VI_A-32]

**Proposition 2.6.6.** *Let `k` be a field, `G` a `k`-group acting on a `k`-scheme `X` in such a way that the morphism
`G × X → X × X`, `(g, x) ↦ (gx, x)` is surjective. Suppose `X` quasi-separated. Then:*

*(i) Every connected component `C` of `X` is irreducible.*

*(ii) Let `η` be the generic point of `C` and `L` the algebraic closure of `k` in `κ(η)`. Then `C` is an `L`-scheme,
geometrically irreducible over `L`, and the morphism*

```text
G⁰_L ×_L C → C ×_L C
```

*is surjective.*

*(iii) In particular, if `C` contains a rational point `x`, then `C` is geometrically irreducible over `k` and the
morphism `φ : G⁰ → C`, `g ↦ gx` is surjective.*

<!-- label: III.VI_A.2.6.6 -->

*Proof.* (i) Let `C` be a connected component of `X`, `Y` an irreducible component of `X` contained in `C`, `η` the
generic point of `Y`, and `U` an affine open of `X` containing `η`. Since `X` is quasi-separated, `U` is retrocompact in
`X`, so by 2.6.4, `U^- = G⁰ U` is an open-and-closed part of `X` meeting `C`, hence containing `C`. Now, by 2.6.3, the
intersection of the `U^-`, for `U` running through a fundamental system of affine open neighborhoods of `η`, equals
`{η}^-`. It follows that `C = {η}^-`. This proves (i).

The first assertion of (ii) (and also of (iii)) follows from 2.6.1. Let us start by showing the second assertion of
(iii). Denote by `ω` (resp. `η`) the generic point of `G⁰` (resp. `C`). Let `z ∈ C` and `K = κ(z)`. Since `G⁰` (resp.
`C`) is geometrically irreducible over `k`, `G⁰_K` (resp. `C_K`) is irreducible; let `ξ` (resp. `β`) denote its generic
point. We saw in the proof of 2.6.4 that the morphism `µ_z : G_K → C_K`, `h ↦ h · z` sends `ξ` to `β`, and similarly one
has `φ(ω) = η`.

<!-- original page 312 -->

Let `L = κ(ξ)` and let `ξ_L, z_L` be the `L`-points deduced from `ξ` and `z`; then `ξ_L · z_L = β′` is a point of `C_L`
above `β ∈ C_K`, hence also above `η ∈ C`. Consider the cartesian square:

```text
            φ_L
G⁰_L ──────────→ C_L
 │                │
 π_{G⁰}           π_C
 │       φ        │
 ▼                ▼
 G⁰ ────────────→ C ;
```

since `φ_L⁻¹(π_{G⁰}⁻¹(ω)) = π_C⁻¹(η)` (cf. EGA I, 3.4.8), there exists `g ∈ G⁰_L` such that `φ_L(g) = β′`. One therefore
has `z_L = ξ_L⁻¹ · φ_L(g) = φ_L(ξ_L⁻¹ g)`, whence `φ(π_{G⁰}(ξ_L⁻¹ g)) = π_C(z_L) = z`. This proves that `φ` is
surjective.

Now let us prove the second assertion of (ii). It suffices to show that, for every `z ∈ C`, the morphism
`µ_z : G⁰_L ⊗_L κ(z) → C ⊗_L κ(z)` is surjective, but this follows from (iii), since `z` is a rational point of
`C ⊗_L κ(z)`.

**Remark 2.6.7.** *Under the hypotheses of 2.6.6, if `C(k) = ∅`, the morphism `G⁰ ×_k C → C ×_k C` is not necessarily
surjective. For example, for `k = ℝ` and `G = {±1}_ℝ`, the `G`-torsor `X = Spec ℝ[X]/(X² + 1)` is connected, but the
morphism `G⁰ ×_ℝ X → X ×_ℝ X` is not surjective. (But one has `L = ℂ` and the morphism `G⁰ ×_ℝ X → X ×_ℂ X` is an
isomorphism.)*

<!-- label: III.VI_A.2.6.7 -->

## 3. Construction of quotients `F\G` (for `G, F` of finite type)

<!-- label: III.VI_A.3 -->

<!-- original page 302 -->

### 3.1.

Let `A` be an Artinian local ring and `u : F → G` a homomorphism of `A`-groups. If `µ : F ×_A F → F` and
`ν : G ×_A G → G` denote the multiplication morphisms and `λ` the composite morphism

```text
            u × G              ν
F ×_A G ─────────→ G ×_A G ────→ G,
```

we recall that the *left quotient* `F\G` of `G` by `F` is the cokernel of the `(Sch/A)`-groupoid `G_*` described below:

```text
                            F × λ
                            ───→
                            µ × G                λ
                  F ×_A F ×_A G    ──→  F ×_A G ───→ G
                            ───→                pr_2
                            pr_{2,3}
```

(`pr_2` and `pr_{2,3}` are the projections of `F ×_A G` and `F ×_A (F ×_A G)` onto the second factors). We shall say
that `G_*` is the *groupoid with base `G` defined by* `u` (cf. Exp. V, § 2.a; as in Exposé V, we do not follow in this
Exposé the convention of IV, 4.6.15).

Since the unique `A`-morphism `F → Spec A` is universally open (EGA IV_2, 2.4.9), `pr_2` is an open morphism; the same
therefore holds for `λ`, which is the composition of `pr_2` and the automorphism `σ` of `F ×_A G` defined by the
formulas: `σ(S)(x, y) = (x, u(S)(x) · y)`, where `S` is a variable `A`-scheme, and `x` and `y` belong to `F(S)` and
`G(S)`. One sees in the same way that `pr_2` and `λ` are flat when `F` is flat over `A`.

<!-- original page 303 -->

Let us also note, to conclude these preliminaries, that every `A`-morphism `s : Spec A → G` defines an automorphism of
the groupoid `G_*` which induces on `G`, `F ×_A G` and `F ×_A F ×_A G` the automorphisms `r_s`, `id_F ×_A r_s` and
`id_F ×_A id_F ×_A r_s` respectively. We shall again write `r_s` for this automorphism of `G_*`, and we shall say that
`r_s` is the *right translation defined by* `s` (cf. 0.4).

### 3.2. Theorem.

**Theorem 3.2.** *Let `F` and `G` be flat groups locally of finite type over an Artinian local ring `A`. Let `u : F → G`
be a quasi-compact `A`-group homomorphism with kernel finite over `A`. Then:*[^N.D.E-VI_A-33]

*(i) The left quotient `F\G` of `G` by `F` exists in `(Sch/A)`, and the sequence*

```text
              λ        p
F ×_A G  ─────→  G  ─────→  F\G
             pr_2
```

*is exact in the category of all ringed spaces.*

*(ii) The canonical morphism `p : G → F\G` is surjective and open, and `F\G` is a direct sum of schemes of finite type
over `A`.*

*(ii′) More precisely, `X = F\G` is equipped with a right action of `G` such that `p(e) · g = p(g)` for every `g ∈ G`;
consequently, the connected components of `X` are of finite type over `A`, irreducible, and all of dimension
`dim G − dim F`.*

*(iii) The canonical morphism `F ×_A G → G ×_{F\G} G` is surjective.*

*(iv) If `u` is a monomorphism,[^N.D.E-VI_A-34] then:*

*(a) `F ×_A G ─^{(λ,pr_2)}→ G ×_{F\G} G` is an isomorphism, and `G → F\G` is faithfully flat and locally of finite
presentation.* *(a′) `F\G` represents the (fppf) quotient sheaf `F\̃G`, and `G → F\G` is a locally trivial `F`-torsor
for the (fppf) topology.* *(b) `F\G` is flat over `A`, and is smooth over `A` if `G` is so.* *(c) `u : F → G` is a
closed immersion, and `F\G` is separated.* *(d) If, in addition, `F` is a normal subgroup of `G`, there exists on `F\G`
one and only one `A`-group structure such that `p : G → F\G` is a morphism of `A`-groups.*

<!-- label: III.VI_A.3.2 -->

In the proof of this theorem, `A′` will denote an `A`-algebra that is local, finite and free over `A`. If `R` is a
relation involving `A′`, we shall say that "`R(A′)` is true when `A′` is large enough" if there exists an `A`-algebra
`A_1` that is local, finite and free over `A` such that the relation `R(A′)` is satisfied for each `A`-algebra `A′` that
is local, finite and free over `A_1`.

<!-- original page 304 -->

We shall first prove the theorem when `F` and `G` are of finite type over `A`.

#### 3.2.1.

Suppose for a moment that every point of `G` has an open saturated neighborhood `W` such that the groupoid induced by
`G_*` on `W` possesses a quasi-section (cf. V § 6). Then, by V 6.1, one has assertions (i), (ii), (iii) and (iv)(a), and
`F\G` is of finite type over `k`. Moreover, under the hypothesis of (iv), since `G → F\G` is faithfully flat and locally
of finite presentation, assertion (b) follows from EGA IV, 2.2.14 and 17.7.7. On the other hand, assertion (iv)(a′)
follows from (iv)(a), by Exp. IV, 3.4.3.1, 5.2.2 and 5.1.6. Finally, (iv)(c) will be proved in 3.2.5, and (ii′) and
(iv)(d) will be proved in section 5.

Let us now prove the following assertion:

```text
(†)    every finite subset of F\G is then contained in an affine open.
```

[^N.D.E-VI_A-35]

If `U` is a quasi-section of the groupoid induced by `G_*` on a saturated open `W` of `G`, then `U ⊗_A A′` is a
quasi-section of the `(Sch/A′)`-groupoid induced by `G_* ⊗_A A′` on `W ⊗_A A′`. Moreover, if `U_*` is the
`(Sch/A)`-groupoid induced by `G_*` on `U`, then `U_* ⊗_A A′` is identified with the `(Sch/A′)`-groupoid induced by
`G_* ⊗_A A′` on `U ⊗_A A′`.[^N.D.E-VI_A-36]

It follows from the proofs of Exposé V that the construction of the quotient `X = F\G` commutes with the extension
`A → A′` of the base of the type considered here.[^N.D.E-VI_A-37]

Let then `x_1, …, x_n` be points of `X = F\G`, which we may assume closed,[^N.D.E-VI_A-38] and `g_1, …, g_n` closed
points of `G` projecting onto `x_1, …, x_n`. Let `V` be an everywhere dense affine open of `X`,[^N.D.E-VI_A-39] and let
`U` be the inverse image of `V` in `G`. By 1.2, there exists an `A`-algebra `A′` that is local, finite and free over
`A`, such that the points `g′_1, …, g′_p` of `G′ = G ⊗_A A′` above `g_1, …, g_n` are strictly rational over
`A′`.[^N.D.E-VI_A-40] Since the morphisms `G′ → G` and `G → X` are open, `U′ = U ⊗_A A′` is dense in `G′`, so the open
set `⋂_{i=1}^p (U′)⁻¹ · g′_i` is non-empty, hence contains a closed point `x`. So, by 1.2 (and 0.4.1), one may suppose,
by possibly enlarging `A′`, that `x` is strictly rational over `A′`. Then, since `x ∈ (U′)⁻¹ · g′_i`, one has
`g′_i ∈ U′ · x`.

Denote by `V′` the inverse image of `V` in `X′ = X ⊗_A A′`; this is an affine open of `X′`, and is also the image of
`U′` under the projection `G′ → X′`. Since right translation `r_x` is an automorphism of the groupoid `G_* ⊗_A A′`, it
induces an automorphism, again denoted `r_x`, of the quotient `X′`. Consequently, the image `V′ · x = r_x(V′)` of
`U′ · x` in `X′` is

<!-- original page 305 -->

an affine open of `X′` containing the images `x′_1, …, x′_p` of `g′_1, …, g′_p`.

Consider now the equivalence relation on `X′ = X ⊗_A A′` defined by the projection `X ⊗_A A′ → X`:

```text
                  d_1
                  ───→
X ⊗_A A′ ⊗_A A′       X ⊗_A A′  ─→  X,
                  ───→
                  d_0
```

where `d_0` and `d_1` are induced by the two canonical injections of `A′` into `A′ ⊗_A A′`. Since `A′` is a finite, free
`A`-algebra, say of rank `n`, then `d_0` and `d_1` are finite and locally free of rank `n`; consequently, one may apply
the reasoning of Exp. V, 5.b (drawn from the proof of SGA 1, VIII.7.6). One thus obtains that `x′_1, …, x′_p` are
contained in an affine saturated open `W′` contained in the affine open `V′ · x`. The image of `W′` in `X` then contains
`x_1, …, x_n` and is an affine open of `X`, by V, 4.1 (ii).

#### 3.2.2.

For every `A`-algebra `A′` that is local, finite and free over `A`, let us now write `U(A′)` for the set of points of
`G ⊗_A A′` having an open saturated neighborhood `W` such that the groupoid induced by `G_* ⊗_A A′` on `W` has a
quasi-section. It is clear that `U(A′)` is saturated for the action of `G(Spec A′)` on `G ⊗_A A′`. We shall see that,
when `A′` is large enough, `U(A′)` is equal to `G ⊗_A A′`.

By Theorem V 8.1, `U(A)` is non-empty, hence contains a closed point `y`. The proof then proceeds by induction on
`dim(G − U(A))`. Let `g_1, …, g_n` be closed points belonging to the various irreducible components of `G − U(A)`. By
1.2, there exists `A′` local, finite and free over `A`, such that the points `g′_1, …, g′_p` (resp. `x = x_1, …, x_r`)
of `G′ = G ⊗_A A′` projecting onto `g_1, …, g_n` (resp. onto `y`) are strictly rational over `A′`. Then `U(A′)` contains
`(U(A) ⊗_A A′) · x⁻¹ g′_i` for every `i`; so `U(A′)` contains

<!-- original page 306 -->

`g′_1, …, g′_p`, and one has

```text
dim(G′ − U(A′)) < dim(G − U(A)).
```

The induction hypothesis then implies the existence of an algebra `A′′` local, finite and free over `A′` such that one
has `U(A′′) = G′ ⊗_{A′} A′′ = G ⊗_A A′′`.

#### 3.2.3.

We are now in a position to prove the existence of `F\G` when `F` and `G` are of finite type over `A`. Let `A′` be large
enough over `A` so that `U(A′)` coincides with `G ⊗_A A′` (cf. 3.2.2). We shall set `A′′ = A′ ⊗_A A′` and, for every
`A`-scheme `X`, we shall denote by `X′` and `X′′` the fibered products `X ⊗_A A′` and `X ⊗_A A′′`. By 3.2.1 and 3.2.2,
the quotients `F′\G′` and `F′′\G′′` exist, and one has the following commutative diagram, in which the first two lines
and columns are exact:

```text
                       pr′′_2          p′′
   F′′ ×_{A′′} G′′  ──────→  G′′  ──────→  F′′ \ G′′
                       λ′′
    w_1   w_2           v_1   v_2          u_1   u_2
                                       
                       pr′_2           p′
(∗) F′ ×_{A′} G′    ──────→  G′   ──────→  F′ \ G′
                       λ′
         h                       g

                       pr_2
   F ×_A G        ──────────→  G       .
                       λ
```

In this diagram, `pr′_2` and `λ′` (resp. `pr′′_2` and `λ′′`) are obtained from `pr_2` and `λ` by obvious base changes;
the morphisms `g` and `h` are induced by the canonical injection `A → A′`. One denotes by `p′` and `p′′` the canonical
morphisms; the morphisms `v_1, v_2` and `w_1, w_2` are induced by the two canonical injections of `A′` into `A′′`.
Finally, since the construction of the quotient `F′\G′` commutes with the two base changes

<!-- original page 307 -->

`f_1, f_2 : Spec A′′ ⇒ Spec A′`, one has, writing `π′ : F′\G′ → Spec A′` for the structural morphism, canonical
isomorphisms, for `i = 1, 2`:

```text
            ∼
τ_i : F′′\G′′ ──→ (F′\G′) ×_{π′, f_i} Spec A′′,
```

and the morphism `u_i` is the composite of `τ_i` and the projection `(F′\G′) ×_{π′, f_i} Spec A′′ → F′\G′`.

Now, when one has a diagram of type `(∗)` with the first two rows and columns exact, one verifies easily that
`Coker(pr_2, λ)` exists if and only if `Coker(u_1, u_2)` exists, and these two cokernels are identified. The existence
of `F\G` will therefore follow from that of `Coker(u_1, u_2)`.

Now it follows from the compatibility of the formation of `F\G` with the base extensions considered here (cf. N.D.E.
(37) in 3.2.1, and 4.6 below) that the composite morphism

```text
                            τ_1⁻¹                          τ_2
(F′\G′) ×_{π′, f_1} Spec A′′ ────→ F′′\G′′ ────→ (F′\G′) ×_{π′, f_2} Spec A′′
```

is a descent datum on `F′\G′` relative to `f : Spec A′ → Spec A`. By 3.2.1 (†) and SGA 1, VIII 7.6, this descent datum
is effective, that is, `Coker(u_1, u_2)` exists (one could also use directly Theorem 4.1 of Exp. V).

#### 3.2.4.

To complete the proof of assertions (i), (ii), (iii) and (iv)(a) of 3.2 in the case where `F` and `G` are of finite type
over `A`, it remains to study the quotient `F\G`. By V 6.1, assertions (ii), (iii) and (iv)(a) "become true" after the
base change `f : Spec A′ → Spec A`; by EGA IV_2, 2.6.1, 2.6.2 and 2.7.1, these assertions were therefore true before the
base change. Finally, to prove the second assertion of (i), i.e. that `F\G` is the cokernel of `(pr_2, λ)` in the
category of all ringed spaces, one need only refer to V § 6.c).

<!-- original page 313 -->

#### 3.2.5.

[^N.D.E-VI_A-41] Let us now prove assertion (iv)(c) of 3.2, by reproducing the proof of VI_B, 9.2.1. Write `X = F\G`,
and `d` for the morphism `F ×_A G → G ×_A G` with components `λ` and `pr_2`.

Since `u` is a closed immersion by 2.5.2, and since `d = σ ∘ (u × id_G)`, where `σ` is the automorphism of `G ×_A G`
defined by `σ(x, y) = (xy, y)`, `d` is a closed immersion. On the other hand, by (iv)(a), one has the cartesian square

```text
                  d
F ×_A G ────────────→ G ×_A G
   │                      │
   │                      │ p × p
   ▼      Δ_X              ▼
   X ────────────────→ X ×_A X
```

and `p`, hence also `p × p`, is faithfully flat and locally of finite presentation. So, by (fppf) descent, since `d` is
a closed immersion, the same holds for `Δ_X`, i.e. `X` is separated.

### 3.3.

[^N.D.E-VI_A-42] In Theorem 3.2, the hypothesis that `G` be flat can be removed when `u : F → G` is a monomorphism. This
generalization is mentioned in Remark 9.3 b) of Exp. VI_B, and also in [Ray67a], Example a) i), p. 82. The proof, found
in Theorem 4 of [An73], follows from Theorem 3.2 and from the following theorem of Grothendieck (mentioned in [Ray67a],
Th. 1 ii) and proved in [DG70], § III.2, 7.1). If `X` is a scheme and `R` an equivalence relation in `X`, we shall write
`X̃/R` for the (fppf) quotient sheaf of `X` by `R` (cf. IV 4.4.9).

**Theorem 3.3.1 (Grothendieck).** *Let `A` be a ring, `X` an `A`-scheme, and `d_0, d_1 : R → X` an `A`-equivalence
relation in `X`, such that `d_i` is faithfully flat, of finite presentation. Let `X_0` be a saturated closed subscheme
of `X`, defined by a nilpotent ideal, and let `R_0` be the equivalence relation induced by `R` on `X_0`. Then, if the
(fppf) quotient sheaf `X̃_0/R_0` is representable by an `A`-scheme, so is `X̃/R`.*

<!-- label: III.VI_A.3.3.1 -->

For the proof, we refer to [DG70], § III.2, 7.1. Let us now return to the case where `A` is an Artinian local ring. Let
`u : F → G` be a quasi-compact morphism between `A`-groups locally of finite type, and suppose further that `u` is a
monomorphism. Then, by 2.5.2, `u` is a closed immersion.

One may now state the following variant of Theorem 3.2.

**Theorem 3.3.2.** *Let `A` be an Artinian local ring, `G` an `A`-group locally of finite type, `F` a closed subgroup of
`G`, flat over `A`.*[^N.D.E-VI_A-43] *Then:*

*(i) The (fppf) quotient sheaf `F̃\G` is representable by an `A`-scheme `F\G` that is separated and locally of finite
type; moreover, the sequence*

```text
            //         p
F ×_A G ─────→  G  ─────→  F\G
```

<!-- original page 318 -->

*is exact in the category of all ringed spaces.*

*(ii) `F ×_A G ─^{(λ,pr_2)}→ G ×_{F\G} G` is an isomorphism, and `p : G → F\G` is faithfully flat and locally of finite
presentation, so that `p` is a locally trivial `F`-torsor for the (fppf) topology.*

*(iii) If `G` is flat (resp. of finite type, resp. smooth) over `A`, then so is `F\G`.*

*(iv) `X = F\G` is equipped with a right action of `G`, such that `p(e) · g = p(g)` for every `g ∈ G`; consequently, the
connected components of `X` are of finite type over `A`, irreducible, and all of dimension `dim G − dim F`.*

*(v) If, in addition, `F` is a normal subgroup of `G`, there exists on `F\G` one and only one `A`-group structure such
that `p : G → F\G` is a morphism of `A`-groups.*

<!-- label: III.VI_A.3.3.2 -->

Assertions (i) and (ii) follow from 3.2 and 3.3.1, and since `G → F\G` is faithfully flat and locally of finite
presentation, assertion (iii) follows from EGA IV, 2.2.14, 2.7.1 and 17.7.7. We shall prove assertions (iv) and (v) in
section 5. Let us note immediately the following corollary.

**Corollary 3.3.3.** *Let `A` be an Artinian local ring, `G` an `A`-group locally of finite type, `H` a closed subgroup
of `G`, flat over `A`. Write `p` for the morphism `G → G/H` and `λ` (resp. `pr_1`) for the morphism `G × H → G` defined
by `λ(g, h) = gh` (resp. the projection `G × H → G`). Then, for every open subset `U` of `G/H`, one has*

```text
O(U) = {φ ∈ O(p⁻¹(U)) | φ ∘ λ = φ ∘ pr_1}
```

*i.e. `O(U)` is the set of `φ ∈ O(p⁻¹(U))` such that `φ(gh) = φ(g)` for every `A`-scheme `S` and `g ∈ G(S)`,
`h ∈ H(S)`.*

<!-- label: III.VI_A.3.3.3 -->

Indeed, since `p : G → G/H` is faithfully flat and locally of finite presentation, hence covering for the (fppf)
topology, this follows from IV, 3.3.3.2.

## 4. Construction of quotients `F\G` (general case)

<!-- label: III.VI_A.4 -->

<!-- original page 308 -->

We now assume the hypotheses of Theorem 3.2 to be satisfied, `F` and `G` not necessarily being of finite type over `A`.

### 4.1.

Let us first consider a connected component `G^α` of `G` and show that the saturation `S(G^α)`[^N.D.E-VI_A-44] of `G^α`
for the equivalence relation defined by the groupoid `G_*` is an open-and-closed subset of `G` (in other words, is the
union of certain connected components of `G`).

This saturation is the image of `F ×_A G^α` under `λ`, hence is open in `G` (cf. § 3.1). If `k` is the residue field of
`A` and `k̄` an algebraic closure of `k`, it remains to show that the image of `(F ×_A G^α) ⊗_A k̄` by `λ ⊗_A k̄` is
closed in `G ⊗_A k̄`, or equivalently, by SGA 1, VIII.4.4, that the image of `(F ×_A G^α) ⊗_A k̄` by `λ ⊗_A k̄` is
closed. Since `G^α ⊗_A k̄` is the union of a finite number of connected components of `G ⊗_A k̄`, we are reduced to the
case where `A` is an algebraically closed field, which we shall assume. In this case, `S(G^α)` is the union of the
images of `G^α` under the left translations `ℓ_{u(x)}`, where

<!-- original page 319 -->

`x` runs through the closed points of `F`; the assertion follows therefore from the fact that these images are connected
components of `G`.

### 4.2.

Let us in particular take `G^α` to be the connected component `G⁰` of the origin of `G`. Then `S(G⁰)` obviously contains
the image of `F` under `u`, which is none other than the equivalence class of the origin. On the other hand, if `F^β` is
a connected component of `F`, `F^β ×_A G⁰` is connected (2.1.2), so that the image of `F^β ×_A G⁰` by `λ` is contained
in the connected component of `u(F^β)` in `G`. In other words, `S(G⁰)` is the union of the connected components which
meet the image of `F`.

One will also note that the open subscheme of `G` having `S(G⁰)` as underlying space is a subgroup of `G` (which we
still denote `S(G⁰)`):

<!-- original page 309 -->

indeed, the inversion morphism of `G` preserves the image of `F` and permutes the connected components of `G` meeting
this image; it therefore suffices to show that `ν : G ×_A G → G` sends `S(G⁰) ×_A S(G⁰)` into `S(G⁰)`, and for this one
may suppose that `A` is an algebraically closed field (with the notations of 4.1, `S(G⁰) ⊗_A k̄` is indeed identified
with the saturation of `(G ⊗_A k̄)⁰` by the equivalence relation defined by the homomorphism `u ⊗_A k̄`); if `G^γ` and
`G^δ` are then connected components of `S(G⁰)`, `G^γ ×_A G^δ` is connected and its image under `ν` meets the image of
`F`; consequently, `u(G^γ ×_A G^δ)` is contained in a connected component of `G` meeting `u(F)`.

### 4.3.

It follows from what precedes that the groupoid `G_*` with base `G` defined by `u` is the direct sum of the groupoids
`S(G^α)_*` induced by `G_*` on the various open-and-closed parts of `G` of the form `S(G^α)`. The cokernel of `G_*` is
therefore the direct sum of the cokernels of these groupoids `S(G^α)_*`, which one is led to study separately.

Let us first consider the groupoid `S(G⁰)_*` induced by `G_*` on `S(G⁰)`. It is clear that `S(G⁰)_*` is the groupoid
with base `S(G⁰)` defined by the homomorphism from `F` into `S(G⁰)` induced by `u` (§ 3.1). The cokernel whose existence
we wish to prove is therefore identified with `F\S(G⁰)`. Consider on the other hand the groupoid

```text
              ℓ′_2
              ────→     ℓ_1
              ℓ′_1            ────→
G⁰_2          ────→   G⁰_1   ────→   G⁰_0 = G⁰
                              ℓ_0
              ℓ′_0
```

induced by `S(G⁰)_*` on `G⁰`. If one refers to the construction explicit in V § 3.b), the object then denoted
`Y_0 ×_{X_0} X_1` is none other than

<!-- original page 310 -->

`F ×_A G⁰`, so that `G⁰_1` is the inverse image of `G⁰` under the morphism `F ×_A G⁰ → S(G⁰)` induced by `λ`.

I claim that this inverse image is `F⁰ ×_A G⁰`, where `F⁰` denotes the inverse image of `G⁰` under `u`. Indeed, if `F^β`
is a connected component of `F⁰`, `F^β ×_A G⁰` is connected (2.1.2) and `λ(F^β ×_A G⁰)` is contained in `G⁰`;
conversely, if `F^β` is a connected component of `F` not contained in `F⁰`, the image of `F^β ×_A G⁰` is again connected
and contains `u(F^β)`; if `u(F^β)` is not contained in `G⁰`, `λ(F^β ×_A G⁰)` does not meet `G⁰`.

It follows from what precedes that the groupoid `G⁰_*` induced by `G_*` on `G⁰` is the groupoid with base `G⁰` defined
by the homomorphism `F⁰ → G⁰` induced by `u`. Since `G⁰`, and hence `F⁰`, are of finite type over `A`, then, by
paragraph 4, `G⁰_*` has a cokernel which is none other than `F⁰\G⁰`.

I now claim that `F⁰\G⁰` is identified with `F\S(G⁰)`. Indeed, the proof is analogous to that of the first part of
assertion (i) of Lemma V § 6.1; consider the diagram:

```text
                v                                pr_2
S(G⁰) ←──────────  F ×_A G⁰  ──────────→  G⁰,
```

where `v` is the morphism induced by `λ`. Since `pr_2` has a section, `pr_2` is a universal effective epimorphism, so
that `F⁰\G⁰` coincides with `Coker(v_0, v_1)`, where

```text
              v′_2
              ────→
              v′_1            v_1
                              ────→
V_2           ────→   V_1     ────→   V = F ×_A G⁰
                              v_0
              v′_0
```

<!-- original page 311 -->

is the inverse image by `pr_2` of the groupoid `G⁰_*` (cf. V § 3.a), that is, also the inverse image of `S(G⁰)_*` by the
composite morphism

```text
            inclusion                pr_2
F ×_A G⁰ ─────────→ F ×_A S(G⁰) ─────────→ S(G⁰).
```

Similarly, since `v` is faithfully flat and quasi-compact, `F\S(G⁰)` coincides with the cokernel of the inverse image of
`S(G⁰)_*` by the base change `v`. Now this inverse image is isomorphic to `V_*` by Exp. V, § 3.c; it follows that the
canonical inclusion of `G⁰_*` into `S(G⁰)_*` induces an isomorphism of `F⁰\G⁰` onto `F\S(G⁰)`.

We finally note that: the construction of `F\S(G⁰)` commutes with finite locally free base changes, because the same
holds for `F⁰\G⁰` (cf. N.D.E. (37) and 4.6 below).

### 4.4.

It remains to construct the cokernel of the groupoid `S(G^α)_*` when `G^α` is an arbitrary connected component of `G`.
If `A′` is a large enough local, finite, free `A`-algebra (cf. 3.2), `G^α ⊗_A A′` is the union of a finite number of
connected components `C_1, …, C_n` of `G ⊗_A A′`, all of which have a strictly rational point. For every `i`, there
exists therefore a right translation `r_i` of `G ⊗_A A′` sending `G⁰ ⊗_A A′` onto `C_i`; this translation induces an
isomorphism of the groupoid `S(G⁰_*) ⊗_A A′` onto `S(C^i_*)`, so that the groupoid induced by `G_* ⊗_A A′` on the
saturation of `C_i` has a cokernel.

Since `S(G^α_*) ⊗_A A′` is the direct sum of some of the `S(C^i_*)`, then `S(G^α_*) ⊗_A A′` has a cokernel; this
cokernel is the direct sum of a certain number of copies of `(F⁰ ⊗_A A′)\(G⁰ ⊗_A A′)`, so that every finite subset of
this cokernel is contained in an affine open; moreover, the construction of this cokernel commutes with finite locally
free extensions

<!-- original page 312 -->

of the base (cf. N.D.E. (37) and 4.6 below). One thus sees, as in 3.2.3, that this cokernel is of the form `Y ⊗_A A′`,
where `Y` is a cokernel of `S(G^α_*)`.

### 4.5.

We have therefore constructed `F\G` and shown that it is a direct sum of schemes of finite type over `A`. The other
assertions of Theorem 3.2 reduce directly to assertions concerning the groupoids `S(G^α_*)`. As in V § 6, the second
assertion of (i) follows from the first and from (ii) and (iii), so it suffices to prove (ii), (iii) and (iv)(a). Since
`A′` is a local, finite, free `A`-algebra, the morphism `A → A′` is faithfully flat and of finite presentation, so, by
SGA 1, VIII (3.1, 4.6, 5.4), it suffices to verify the corresponding assertions in the case of the groupoid
`S(G^α_*) ⊗_A A′`. Now the latter is isomorphic to the direct sum of a finite number of copies of `S(G⁰_*) ⊗_A A′` (cf.
4.4), so that one is reduced to the groupoid `S(G⁰_*)`.

For this last one continues to mimic the proof established in V § 6, as one began to do in 4.3.

### 4.6.

Let us add to conclude this paragraph some remarks concerning Lemma 6.1 and § 9.a of Exposé V: with the hypotheses and
notations of V § 9.a, we seek a condition under which the construction of the cokernel of the `(Sch/S)`-groupoid `X_*`
commutes with an extension `π : S′ → S` of the base. Since the cokernels of `X_*` and `X′_*` are identified with the
cokernels of the groupoids `U_*` and `U′_*` induced by `X_*` and `X′_*` on the quasi-sections `U` and `U′`, one is
reduced to the case of a `(Sch/S)`-groupoid satisfying the hypotheses of Theorem V 4.1.

[^N.D.E-VI_A-45] If one denotes by `Y` the cokernel of `U_*`, `Y′ = Y ×_S S′`, and `Y_1` the cokernel of `U′_*`, one saw
in V § 9.a that the canonical morphism `Y_1 → Y′` is a homeomorphism (and even a universal homeomorphism); one may
therefore identify `Y_1` and `Y′` as topological spaces. If `p : U → Y` is the canonical morphism and if `p′ : U′ → Y′`
is obtained from it by base change, we then want the sequence of `O_{Y′}`-modules

```text
                p′_*(O_{U′})
(∗)  O_{Y′}  ─────────→  ──→  p′_* u′_{1*}(O_{U′_1}) = p′_* u′_{0*}(O_{U′_1})
                         ──→
```

<!-- label: eq:III.VI_A.4.6-star -->

to be exact.[^N.D.E-VI_A-46] Since we are under the hypotheses of V 4.1, `u_0` and `u_1` are finite and locally free;
and, by V.4.1 (ii), `p` is integral. Then, `p` and `p ∘ u_i` are affine, hence separated and quasi-compact.

<!-- original page 313 -->

Consequently, if `S′` is flat over `S`, it follows from EGA III_1, 1.4.15 (taking into account the correction Err_III 25
in EGA III_2) that the sequence `(∗)` is identified with the inverse image of the sequence

```text
                          p_*(O_U)
(∗∗)  O_Y  ─────────→  ─────────→  p_* u_{1*}(O_{U_1}) = p_* u_{0*}(O_{U_1}),
                       ─────────→
```

<!-- label: eq:III.VI_A.4.6-doublestar -->

which is an exact sequence.[^N.D.E-VI_A-47] An analogous argument applies when the groupoid `X_*` has "locally"
quasi-sections (cf. the proof of Theorem V 7.1). One thus obtains the:

**Proposition 4.6.1.** *The construction of the cokernel of `X_*` commutes with flat extensions of the base when `X_*`
has locally quasi-sections.*

<!-- label: III.VI_A.4.6.1 -->

### 4.7.

Let us now consider the case of the groupoid `G_*` of Theorem 3.2 when one provisionally assumes `F` and `G` of finite
type over `A`.

By 3.2.2, there exists an `A`-algebra `A′` local, finite and free over `A` such that the groupoid `G_* ⊗_A A′` has
"locally" quasi-sections. For every extension `T → Spec A` of the base, the sequence

```text
                                  //
(F′′\G′′) ×_{Spec A} T  ─────→  (F′\G′) ×_{Spec A} T  ─────→  (F\G) ×_{Spec A} T
```

deduced from the diagram `(∗)` of 3.2.3 is exact. If one supposes in addition `T` flat over `Spec A`, then
`(F′′\G′′) ×_{Spec A} T` and `(F′\G′) ×_{Spec A} T` are identified respectively, by 4.6, with the cokernels of the
groupoids

```text
(G_* ⊗_A A′′) ×_{Spec A} T    and    (G_* ⊗_A A′) ×_{Spec A} T.
```

The diagram deduced from 3.2.3 `(∗)` by the base change `T → Spec A` then shows that `(F\G) ×_{Spec A} T` is identified
with the cokernel of `G_* ×_{Spec A} T`. An analogous argument is valid in the general case (i.e. when `G` and `F` are
locally of finite type over `A`). One therefore obtains:[^N.D.E-VI_A-48]

**Proposition 4.7.1.** *Under the hypotheses of Theorem 3.2, for every flat `A`-scheme `T`, `(F\G) ×_{Spec A} T` is
identified with the left quotient of `G ×_{Spec A} T` by `F ×_{Spec A} T`.*

<!-- label: III.VI_A.4.7.1 -->

## 5. Connections with Exposé IV and consequences

<!-- label: III.VI_A.5 -->

<!-- original page 314 -->

### 5.1.

[^N.D.E-VI_A-49] We resume the notations of § 3 and the hypotheses of Theorem 3.2; one then has the following
commutative diagram

```text
                          F × ν
F ×_A G ×_A G  ──────────→  F ×_A G

pr_2 × G    λ × G            pr_2    λ
                          ν
   G ×_A G            ──────────→  G

   p × G                           p
                       ρ
   (F\G) ×_A G  ⇢ ⇢ ⇢ ⇢ ⇢ ⇢ ⇢ F\G,
```

which satisfies the equalities `pr_2 ∘ (F × ν) = ν ∘ (pr_2 × G)` and `λ ∘ (F × ν) = ν ∘ (λ × G)`. Moreover, since `G` is
assumed flat over `A`, the left vertical sequence is exact by 4.7, so that `ν` induces a morphism of `A`-schemes:

```text
ρ : (F\G) ×_A G → F\G.
```

This morphism `ρ` makes `G` act on the right on `F\G`, as one verifies immediately; moreover, the canonical morphism
`G → F\G` commutes with the right actions of `G` on `G` and on `F\G`.

[^N.D.E-VI_A-50] This proves the first assertion of point (ii′) of 3.2. By 2.5.4, one then obtains that the connected
components of `X = F\G` are of finite type, irreducible, and all of the same dimension. To evaluate this dimension, one
may suppose `A = k` and `k` algebraically closed. By I, 2.3.3.1, the stabilizer of the `k`-point `p(e)` is represented
by the fiber `H = p⁻¹(p(e))`, and since `F\G` is the quotient of `G` by `F` in the category of ringed spaces, this fiber
has `u(F)` as underlying space, and since `Ker(u)` is finite, one therefore has `dim H = dim u(F) = dim F`. By 2.5.4
(ii), one obtains therefore that `dim X = dim G − dim F`. This proves point (ii′) of Theorem 3.2 (and hence also point
(iv) of 3.3.2).

### 5.2.

When the homomorphism of `A`-groups `u : F → G` is a monomorphism, one can recover 5.1 by using the results of Exposé
IV. Indeed, the canonical morphism `p : G → F\G` is faithfully flat and open by 3.2; it is therefore covering for the
(fpqc) topology (IV 6.3.1), and one may apply corollaries IV.5.2.2 and IV.5.2.4.

<!-- original page 315 -->

In particular, if we assume, in addition to the hypotheses of 3.2, that `u` is the inclusion in `G` of a normal subgroup
`F`, there exists on `F\G` one and only one `A`-group structure such that the canonical morphism `p : G → F\G` is a
homomorphism of `A`-groups.[^N.D.E-VI_A-51] This proves point (v) of 3.3.2.

### 5.3.

We shall now review some statements from Exposé IV.

#### 5.3.1.

Statements IV 5.2.7 and IV 5.3.1 translate as follows. Let `F` and `G` be two groups locally of finite type and flat
over `A`, `F` being a closed normal subgroup of `G`. The maps `H ↦ F\H` and `H′ ↦ H′ ×_{(F\G)} G` define a bijective
correspondence between flat `A`-subgroups of `G` containing `F` and flat `A`-subgroups of `F\G`. In this bijection,
closed (resp. normal) subgroups of `G` containing `F` correspond to closed (resp. normal) subgroups of
`F\G`.[^N.D.E-VI_A-52]

#### 5.3.2.

Proposition IV 5.2.9 implies the following result. Let `F`, `H` and `G` be groups locally of finite type and flat over
`A`; assume `F ⊂ H ⊂ G`, with `F` closed in `G` and normal in `H`. Under these conditions, `F\H` acts freely on the left
on `F\G`, the quotient scheme `(F\H)\(F\G)` exists, and there is a canonical isomorphism of schemes with operator group
`G`:

```text
(F\H) \ (F\G) = H\G.
```

#### 5.3.3.

From IV 5.2.8, finally, follows the assertion below. Let `F`, `H` and `G` be groups locally of finite type and flat over
`A`; assume that `F` is contained in, closed and normal

<!-- original page 316 -->

in `G`, that `H` is contained in `G`, and that `F ∩ H` is flat over `A`. Let `F ×^τ_A H` denote the `A`-group having the
product `F ×_A H` as underlying scheme, with multiplication defined by the morphism `((x, h), (y, h′)) ↦ (xhyh⁻¹, hh′)`;
similarly, let `u : H ∩ F → F ×^τ_A H` be the monomorphism `x ↦ (x⁻¹, x)`, and let `F · H` be the quotient
`(F ∩ H)\(F ×^τ_A H)`. Under these conditions, there is a canonical isomorphism

```text
F\(F · H) = (F ∩ H)\H.
```

### 5.4.

[^N.D.E-VI_A-53] Let `u : G → H` be a quasi-compact morphism between `A`-groups locally of finite type, such that the
kernel `N` of `u` is flat over `A`. In this case, by 3.3.2 and 5.2, the quotient `A`-group `C = N\G` exists and the
morphism `p : G → C` is faithfully flat and locally of finite presentation. On the other hand, by IV 5.2.6, `u` induces
a monomorphism `v : C → H`, which is quasi-compact (because `u` is, and `G → C` is surjective; cf. EGA IV_1, 1.1.3),
hence is a closed immersion by 2.5.2. We have therefore obtained the following proposition:

**Proposition 5.4.1.** *Let `u : G → H` be a quasi-compact morphism between `A`-groups locally of finite type, such that
`N = Ker u` is flat over `A`. Then one has the factorization:*

```text
              u
G ───────────────→ H
 \                ↗
  p             ↗
   \         ↗ i
    ↘     ↗
     N\G
```

*where `p` is faithfully flat, locally of finite presentation, and `i` a closed immersion.*

<!-- label: III.VI_A.5.4.1 -->

Suppose in addition `G` flat over `A`. Then, by 3.3.2, `C = N\G` is flat over `A`, and so the quotient `X = C\H` exists
in `(Sch/A)` and represents the (fppf) quotient sheaf `C̃\H`, and `q : H → X` is a `C`-torsor. Consequently, writing
`e : Spec A → G` for the unit section of `G`, `v` induces an isomorphism of (fppf) sheaves between `C̃` and the fibered
product of `q` and of `q ∘ e : Spec A → X`, which is represented by a closed subscheme of `H`. Consequently, `v` is an
isomorphism of `C` onto a closed group subscheme `K` of `G` (equal to the stabilizer of the `A`-point `q ∘ e` of `X`).
(This gives another proof of the fact that every quasi-compact monomorphism `v : C → H` between `A`-groups locally of
finite type is a closed immersion, cf. 2.5.2 and VI_B 1.4.2.)

Suppose in addition that `C` is a normal subgroup of `H`; in this case, the `A`-group `H̄ = C\H` is the cokernel in the
category of `A`-groups of the morphism `u : G → H`, and `K` is the kernel of the morphism `H → H̄`. When `G` and `H` are
abelian `A`-groups, `K` is the image of `u` in the category of abelian `A`-groups, while `C = (Ker u)\G` is the coimage
of `u`. Taking into account the isomorphism `C ⥲ K` just established, one obtains:[^N.D.E-VI_A-54]

**Theorem 5.4.2.** *Let `k` be a field. The category of commutative algebraic `k`-groups is abelian.*

<!-- label: III.VI_A.5.4.2 -->

Indeed, when `k` is a field, `Ker(u)` is flat over `k` whatever `u`.

[^N.D.E-VI_A-55] Let us note that the full subcategory of affine commutative algebraic `k`-groups is *thick*. Indeed,
consider an exact sequence of commutative algebraic `k`-groups:

```text
1  ───→  N  ───→  G  ───→  G/N  ───→  1.
```

If `G` is affine, it is clear that `N` is so, and `G/N` is also so by a theorem of Chevalley, cf. VI_B, 11.17.
Conversely, if `N` and `G/N` are affine, then so is `G`, by VI_B, 9.2 (viii). One therefore obtains:

**Corollary 5.4.3.** *Let `k` be a field. The category of commutative affine algebraic `k`-groups is abelian.*

<!-- label: III.VI_A.5.4.3 -->

Let us further point out that the category of all commutative affine `k`-groups (not necessarily of finite type) is
abelian; this is deduced from VI_B, 11.17 and 11.18.2 (cf. [DG70], § III.3, 7.4), see also VII_B, 2.4.2 for a proof
using formal groups.

<!-- original page 317 -->

### 5.5.

Let `G` be a group locally of finite type and flat over an Artinian local ring `A`. We know (2.3) that the connected
component of the origin `G⁰` is a normal open group subscheme of `G`, hence also flat over `A`. Then, by 3.2 and 5.2,
`G⁰\G` is an `A`-group scheme, flat over `A`. Moreover, since each connected component `G^α` of `G` is saturated for the
equivalence relation defined by `G⁰`, then `G⁰\G` is the direct sum of the `G⁰\G^α` (cf. 4.3). In particular, the
connected component of the origin in `G⁰\G` is none other than `G⁰\G⁰ ≅ Spec A`, and so `G⁰\G → Spec A` is a local
isomorphism at the origin. Consequently, `G⁰\G` is étale over `Spec A`, by VI_B, 1.3.[^N.D.E-VI_A-56] One therefore
obtains the following proposition (for point (ii), one refers to [DG70], § II.5, 1.7–1.10):

**Proposition 5.5.1.** *Let `A` be an Artinian local ring and `G` an `A`-group locally of finite type and flat.*

*(i) `G⁰\G` is an étale `A`-group.*

*(ii) Consequently, if `A = k` is an algebraically closed field, `G⁰\G` is a constant `k`-group, acting in a simply
transitive way on the set of connected components of `G`; hence if `G` is algebraic, `G⁰\G` is finite.*

<!-- label: III.VI_A.5.5.1 -->

### 5.6.

Let `k` be a perfect field and `G` a `k`-group locally of finite type. We have seen (0.2) that `G_red` is then a group
subscheme of `G`. Moreover, the equivalence class of the origin of `G` under the left action of `G_red` on `G` is the
whole underlying space of `G`. So, by Theorem 3.2, one obtains:

**Proposition 5.6.1.** *Let `k` be a perfect field and `G` a `k`-group locally of finite type. Then the `k`-scheme
`G_red\G` is the spectrum of a finite, local `k`-algebra with residue field `k`.*

<!-- label: III.VI_A.5.6.1 -->

[^N.D.E-VI_A-57] Indeed, by 3.2, `G_red\G` has a single point, with residue field `k`, and is a `k`-scheme of finite
type; it is therefore the spectrum of a local `k`-algebra of finite dimension (cf. EGA I, 6.4.4).

**Proposition 5.6.2.** *Let `u : F → G` be a morphism between groups locally of finite type over a perfect field `k`.
The following assertions are equivalent:*

*(i) `u` is flat.*

*(ii) `u⁰ : F⁰ → G⁰` is dominant and the morphism `v : F_red\F → G_red\G` induced by `u` is flat.*

<!-- label: III.VI_A.5.6.2 -->

<!-- original page 318 -->

[^N.D.E-VI_A-58] Indeed, consider the following commutative diagram:

```text
                p
F ─────────────→ F_red\F

u                       v
        q
G ─────────────→ G_red\G,
```

where `p` and `q` denote the canonical projections. By 3.2 (iv), `p` and `q` are faithfully flat; consequently, if `u`
is flat, then `q ∘ u = v ∘ p` is flat, hence so is `v`.

Conversely, suppose `v` flat and `u⁰` dominant. Since `u⁰` is quasi-compact (`F⁰` being of finite type over `k` by 2.4,
hence noetherian), it sends the generic point `ξ` of `F⁰` to the generic point `η` of `G⁰`. Let `R` be the finite local
`k`-algebra of which `G_red\G` is the spectrum, and `𝔪` its maximal ideal. One has local morphisms of local rings:
`R → O_{G,η} → O_{F,ξ}`. Note that one has a cartesian square:

```text
G_red ──────────→ G

                  q
                  ▼
Spec(R/𝔪) ──→ Spec(R)
```

and so `O_{G,η}/𝔪 O_{G,η} ≅ O_{G_red, η} = κ(η)`, so that `O_{F,ξ}/𝔪 O_{F,ξ}` is flat over `O_{G,η}/𝔪 O_{G,η}`.

On the other hand, since `q` and `v ∘ p` are flat, `G` and `F` are flat over `R`. Consequently, by the local flatness
criterion (cf. EGA IV_3, 11.3.10.2), `O_{F,ξ}` is flat over `O_{G,η}`, i.e. `u` is flat at the point `ξ`. So, by 2.5.3,
`u` is flat.

## 6. Complements on `k`-groups not necessarily of finite type

<!-- label: III.VI_A.6 -->

[^N.D.E-VI_A-59] Let us further point out the following results, which will be useful in the addendum VI_B, § 12. We fix
a base field `k`.

**Lemma 6.1.** *Let `G` be a `k`-group. For every `x ∈ G`, there exists a point `u ∈ G × G` such that `µ(u) = x` and
that the two projections `p_1(u)` and `p_2(u)` are maximal points of `G`.*

<!-- label: III.VI_A.6.1 -->

<!-- original page 327 -->

*Proof.* Set `K = κ(x)`. Since the projection `G_K → G` sends maximal points to maximal points, one is reduced to the
case where `x` is rational. Then left translation `λ_x` (resp. right translation `ρ_x`) gives us a morphism `G → G × G`,
`g ↦ (λ_x(g⁻¹), g)` (resp. `g ↦ (g, ρ_x(g⁻¹))`) which induces an isomorphism of `G` onto `µ⁻¹(x)`, inverse of `p_2`
(resp. `p_1`). So, if `u` is a maximal point of `µ⁻¹(x)`, then `p_1(u)` and `p_2(u)` are maximal points of `G`, and so
`u` is suitable.

**Corollary 6.2.** *Let `f : G → H` be a quasi-compact, dominant morphism of `k`-groups.*

*(i) `f` is surjective.*

*(ii) If `H` is reduced, `f` is faithfully flat.*

<!-- label: III.VI_A.6.2 -->

*Proof.* Write `µ_H` (resp. `µ_G`) for the multiplication of `H` (resp. `G`). Let `h ∈ H`. By 6.1, there exists
`u ∈ H × H` such that `µ_H(u) = h` and that `α = p_1(u)` and `β = p_2(u)` are maximal points of `H`. Since `f` is
quasi-compact and dominant, `f⁻¹(α)` and `f⁻¹(β)` are non-empty (cf. EGA IV_1, 1.1.5), and so there exists `v ∈ G × G`
such that `(f × f)(v) = u` (cf. EGA I, 3.5.2). Then `g = µ_G(v)` satisfies `f(g) = h`. This shows that `f` is
surjective.

Suppose in addition `H` reduced. Then `O_{H,α}` is a field, and we have seen above that `f⁻¹(α) ≠ ∅`, so `f` is flat at
every point `ξ` of `f⁻¹(α)`, so `f` is flat by Lemma 2.5.3.

**Recollection 6.3.** *Recall (cf. EGA IV_3, 11.10.1) that a morphism of schemes `f : X → Y` is said to be*
schematically dominant *if it satisfies the following condition: for every open `U` of `Y`, if `Z` is a closed subscheme
of `U` such that the morphism `f⁻¹(U) → U` factors through `Z`, then `Z = U`. When `f` is quasi-compact and
quasi-separated, this is equivalent to saying that the closed image of `X` by `f` is `Y` (cf. loc. cit., 11.10.3 (iv)
and EGA I, 9.5.8).*

<!-- label: III.VI_A.6.3 -->

**Proposition 6.4.** *Let `f : H → G` be a quasi-compact morphism of `k`-groups. Then the closed image of `f` is a group
subscheme `H′` of `G`, and `f` factors as:*

```text
         f
H ────────────→ G
 \             ↗
  \          ↗
   f′      ↗ i
    ↘    ↗
     H′
```

*where `f′` is schematically dominant, quasi-compact and surjective.*

<!-- label: III.VI_A.6.4 -->

*Proof.* Since `H` is separated (0.3), `f` is quasi-compact and separated, so `f_*(O_H)` is a quasi-coherent
`O_G`-module, and the closed image `H′` of `f` exists and is the closed subscheme of `G` defined by the quasi-coherent
ideal `I = Ker(O_G → f_*(O_H))` (cf. EGA I, § 9.5).

<!-- original page 328 -->

Write `c_G` and `µ_G` (resp. `c_H` and `µ_H`) for the inversion and multiplication morphisms of `G` (resp. `H`). Then
`c_G ∘ f = f ∘ c_H` factors through the closed subscheme `c_G(H′)`, whence `H′ ⊂ c_G(H′)` and so `H′ = c_G(H′)` (since
`c_G² = id_G`). Similarly, since `f ∘ π_H = π_G ∘ (f × f)` factors through `H′`, then `f × f` factors through the closed
subscheme `π_G⁻¹(H′)` of `G × G`. On the other hand, since the formation of the closed image commutes with flat base
changes (EGA III 1.4.15 and IV_1 1.7.21), the closed image of `f × id_H` (resp. `id_{H′} × f`) is `H′ × H` (resp.
`H′ × H′`). So, by "transitivity of closed images" (EGA I, 9.5.5), the closed image of `f × f` is `H′ × H′`, which is
therefore contained in `π_G⁻¹(H′)`, i.e. the restriction of `π_G` to `H′ × H′` factors through `H′`. This shows that
`H′` is a closed group subscheme of `G`. Write `i` for the inclusion `H′ ↪ G`.

Then `f` equals `i ∘ f′`, where `f′ : H → H′` is schematically dominant and quasi-compact (since `f` is quasi-compact
and `i` is separated). So, by 6.2, `f′` is surjective. This proves 6.4.

One can now state the following theorem ([Per75], V 3.1 & 3.2, see also [Per76], 0.0 & 0.1).

**Theorem 6.5 (D. Perrin).** *Let `G` be a quasi-compact `k`-group. Then*

*(i) `G` is the projective limit of a filtered system `(G_i)` of `k`-groups of finite type (whose transition morphisms
`u_{ij} : G_j → G_i` are affine for `i` large enough), and the morphisms `G → G_i` are faithfully flat (and affine for
`i` large enough).*

*(ii) Let `H` be a closed `k`-subgroup of `G`. Then the (fpqc) quotient sheaf `G̃/H` is a `k`-scheme in the following
two cases:*

*(1) The immersion `H → G` is of finite presentation; in this case, `G/H` is of finite type over `k`.* *(2) `H` is
normal in `G`.*

<!-- label: III.VI_A.6.5 -->

For the proof of this theorem (which rests on several intermediate theorems), we refer to [Per75]. For the reader's
convenience, let us however prove the two corollaries below, cf. [Per75] V 3.3 to 3.4 or [Per76] 4.2.3 to 4.2.5.

**Corollary 6.6.** *Let `f : G → H` be a quasi-compact morphism of `k`-groups.*

*(i) If `f` is schematically dominant, it is faithfully flat.*

*(ii) This is the case, in particular, if `H` is affine and the morphism `f^♮ : O(H) → O(G)` is injective.*

<!-- label: III.VI_A.6.6 -->

*Proof.* Suppose `f` schematically dominant. Then, by 6.2 (i), `f` is surjective, so, by 2.5.3, it suffices to show that
`f` is flat at the unit element of `G`. Since `O_{H,e} = O_{H⁰,e}` (cf. 2.6.5), one may replace `H` by `H⁰`, and hence
assume `H` irreducible. Then `H` is quasi-compact (loc. cit.), and since `f` is quasi-compact, so is `G`. By 6.5 (i),
`H = lim_i H_i`, where each `H_i` is an algebraic `k`-group. Denote by `N_i` the kernel of `G → H_i`; this is a closed
normal `k`-subgroup of `G`. Moreover, since the unit section `{e} → H_i` is of finite presentation, the immersion
`N_i → G` is

<!-- original page 329 -->

also so; so, by 6.5 (ii), the (fpqc) quotient `G/N_i` is an algebraic `k`-group. One has then a commutative diagram

```text
         f
G ──────────────→ H
 q_i               p_i
        f_i
G/N_i ──────────→ H_i
```

where `f` is schematically dominant, `p_i, q_i` are faithfully flat (hence schematically dominant). Then
`f_i ∘ q_i = p_i ∘ f` is schematically dominant, and so `f_i` is also so. On the other hand, `f_i` is a monomorphism,
hence a closed immersion, since `G/N_i` and `H_i` are algebraic (2.5.2). It follows that `f_i` is an isomorphism, and so
`G → H_i` is faithfully flat. Then, by [BAC] I § 2.7, Prop. 9, the morphism `G → H` is flat; on the other hand, it is
surjective by 6.2 (i), so it is faithfully flat. This proves point (i); and point (ii) follows, since if `H` is affine
and `f^♮` injective, then the closed image of `f` equals `H`, so `f` is schematically dominant (cf. 6.4).

**Corollary 6.7.** *Let `u : G → H` be a morphism of `k`-groups and `N = Ker(u)`. Suppose `u` quasi-compact.*

*(i) The (fpqc) quotient sheaf `G̃/N` is represented by a `k`-group scheme `G/N`, and `u` factors as:*

```text
            u
G ────────────────→ H
 \                 ↗
  p              ↗
   \           ↗ i
    ↘        ↗
     G/N
```

*where `p` is faithfully flat and `i` a closed immersion.*

*(ii) In particular, if `u` is a monomorphism, `u` is a closed immersion, and if `u` is schematically dominant, `u` is
faithfully flat.*

<!-- label: III.VI_A.6.7 -->

*Proof.* (i) By 6.4 and 6.6, the closed image `G′` of `u` is a closed group subscheme of `G`, and `p : G → G′` is
faithfully flat and quasi-compact. One evidently has `Ker(p) = Ker(u) = N`, and so by Exp. IV, 3.3.2.1 and 5.1.7, `G′`
represents the (fpqc) quotient sheaf `G̃/N`.

(ii) The second assertion is contained in 6.6; let us show the first. If `u` is a monomorphism, so is `p`; then `p` is
at once a monomorphism and an effective epimorphism, hence an isomorphism (cf. IV, 1.14). This proves 6.7.

Let us finally point out the following corollaries (cf. [Per76], 4.2.6 to 4.2.8).

**Corollary 6.8.** *The category of commutative quasi-compact `k`-group schemes is abelian.*

<!-- label: III.VI_A.6.8 -->

Taking 6.7 into account, the proof is analogous to that of 5.4.2.

**Corollary 6.9.** *If `char(k) = 0`, every `k`-group scheme `G` is geometrically reduced.*

<!-- label: III.VI_A.6.9 -->

<!-- original page 330 -->

Indeed, if `g ∈ G` and if `K` is an algebraic closure of `κ(g)`, one has `O_{G,e} ⊗_k K ≃ O_{G_K, g_K}`, so it suffices
to show that `O_{G,e} = O_{G⁰, e}` is geometrically reduced. One is thus reduced to the case where `G` is connected,
hence quasi-compact (2.6.5). Then the result follows from 6.5 and from Cartier's theorem for algebraic groups (cf. VI_B,
1.6.1 or [DG70] § II.6, Th. 1.1).

**Corollary 6.10.** *Let `G` be a quasi-compact `k`-group. Assume `k` algebraically closed.*

*(i) Let `f : G → H` be a faithfully flat morphism of `k`-groups. Then the induced map `G(k) → H(k)` is surjective.*

*(ii) The set of rational points is dense in `G`.*

<!-- label: III.VI_A.6.10 -->

For the proof, we refer to [Per75], V 3.7 & 3.9.

## Bibliography

[^N.D.E-VI_A-60]

**[An73]** S. Anantharaman, *Schémas en groupes, espaces homogènes et espaces algébriques sur une base de dimension 1*,
Mém. Soc. Math. France **33** (1973), 5–79.

**[BAC]** N. Bourbaki, *Algèbre commutative*, Chap. I–IV et V–VII, Masson, 1985.

**[DG70]** M. Demazure, P. Gabriel, *Groupes algébriques*, Masson & North-Holland, 1970.

**[Per75]** D. Perrin, *Schémas en groupes quasi-compacts sur un corps*, Publ. Math. Orsay N° 165–75.46 (1ère partie),
http://portail.mathdoc.fr/PMO/

**[Per76]** D. Perrin, *Approximation des schémas en groupes, quasi-compacts sur un corps*, Bull. Soc. Math. France
**104** (1976), 323–335.

**[Ray67a]** M. Raynaud, *Passage au quotient par une relation d'équivalence plate*, pp. 78–85 in: Proc. Conf. Local
Fields (Driebergen) (ed. T. A. Springer), Springer-Verlag, 1967.

**[Ray67b]** M. Raynaud, *Sur le passage au quotient par un groupoïde plat*, C. R. Acad. Sci. Paris (Sér. A) **265**
(1967), 384–387.

**[Ray70]** M. Raynaud, *Faisceaux amples sur les schémas en groupes et les espaces homogènes*, Lect. Notes Maths.
**119**, Springer-Verlag, 1970.

## Footnotes

<!-- LEDGER DELTA — Exposé VI_A — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| anneau local artinien | Artinian local ring | Standard. |
| corps résiduel | residue field | Already in glossary. |
| `A`-groupe | `A`-group | Shorthand for group scheme over `Spec A`. |
| algébrique (groupe) | algebraic (group) | Underlying scheme of finite type over `A`. |
| localement de type fini | locally of finite type | Standard. |
| de type fini | of finite type | Standard. |
| composante neutre | neutral component | The connected component of the identity, denoted `G⁰`. |
| composante connexe | connected component | Standard. |
| strictement rationnel | strictly rational | Used by Gabriel: a point with a chosen `A`-section through it. |
| rendre strictement rationnel | make strictly rational | Gabriel's coinage. |
| sous-groupe distingué | normal subgroup | Standard English does not distinguish "distingué"/"normal". |
| sous-groupe caractéristique | characteristic subgroup | Standard. |
| sous-groupe radical | (not used here) | — |
| saturé | saturated | For an equivalence relation: stable under the relation. |
| « rendre rationnel » | "make rational" | Gabriel's metaphor, preserved with quotes. |
| quotient à gauche `F\G` | left quotient `F\G` | Standard notation; preserve backslash. |
| conoyau (du groupoïde) | cokernel (of the groupoid) | Standard. |
| groupoïde | groupoid | Standard. |
| quasi-section | quasi-section | Standard. |
| ouvert et saturé | open and saturated | Standard. |
| descente fppf / fpqc | fppf / fpqc descent | Standard. |
| schématiquement dominant | schematically dominant | EGA IV term. |
| image fermée | closed image | EGA I term. |
| Nakayama nilpotent | nilpotent Nakayama | Standard. |
| limite projective | projective limit | The source uses both; modern English often says inverse limit, but the Exposé style here keeps "projective limit". |
| clôture parfaite | perfect closure | Standard; written `k^{p^{-∞}}` or `k′`. |
| clôture algébrique | algebraic closure | Standard. |
| point maximal | maximal point | Equivalent to "generic point of an irreducible component" in this setting. |
| générisation | generization | Standard. |
| rétrocompact | retrocompact | EGA term. |
| translation à gauche / à droite | left / right translation | Standard. |
| `Gréd` | `G_red` | Reduced scheme associated to `G`. |
| `D_k(M)` | `D_k(M)` | Cartier dual, as in Exp. VIII. |
| Bible (Séminaire Chevalley) | the *Bible* | Not used here; mentioned only via VI_B/VII_B cross-refs. |
-->

[^N.D.E-VI_A-0]: N.D.E.: Version of 13/10/2024.

[^N.D.E-VI_A-1]: N.D.E.: The sentences that follow have been added.

[^N.D.E-VI_A-2]: N.D.E.: For examples of group schemes `G` over a non-perfect field `k` such that `G_red` is not a group
    scheme over `k`, see 1.3.2 below.

[^N.D.E-VI_A-3]: N.D.E.: We have slightly modified what follows of 0.2, as well as 0.3.

[^N.D.E-VI_A-4]: N.D.E.: To have an analogous example with `G` connected, one may consider, for `char(k) = p > 0`, the
    semidirect product of `α_{p,k}` and `G_{m,k}`.

[^N.D.E-VI_A-5]: N.D.E.: This argument is valid for every local ring `A` of dimension zero, and shows that if `S` is a
    discrete scheme, every `S`-group is separated, cf. VI_B, 5.2; on the other hand (cf. VI_B, 5.6.4), if
    `S` contains a closed point `s` that is not isolated, the `S`-scheme `G` obtained by gluing two copies
    of `S` along the open subset `S − {s}` is not separated over `S`, but is equipped with an `S`-group
    structure.

[^N.D.E-VI_A-6]: N.D.E.: We have detailed the original in what follows, in particular we have added Remark 0.4.1.

[^N.D.E-VI_A-7]: N.D.E.: The original stated this result under the hypothesis that `G` is locally of finite type over
    `A`. Since it is useful to have it available in the general case, and since the proof is essentially
    the same, we have stated and proved the result in the general case. This will be used several times in
    what follows.

[^N.D.E-VI_A-8]: N.D.E.: We have inserted this corollary here, cf. 2.4 and 2.6.2 below.

[^N.D.E-VI_A-9]: N.D.E.: We have added this corollary, used implicitly in VIII, 6.7; see also VI_B 6.2.5.

[^N.D.E-VI_A-10]: N.D.E.: For example, they are always complete intersections, cf. VII_B, 5.5.1. Moreover, if
    `char(k) = 0` then `G` is smooth (VI_B, 1.6.1; see also VII_B, 3.3.1).

[^N.D.E-VI_A-11]: N.D.E.: Indeed, the hypothesis on `K` entails that, for every extension `L` of `K`, every `k`-morphism
    `κ(x) → L` (resp. `κ(y) → L`) factors through `K`; consequently, all points of `G ⊗_k K` above `x` or
    `y` have `K` as residue field, i.e. are (strictly) rational over `K`.

[^N.D.E-VI_A-12]: N.D.E.: Indeed, `B` is a noetherian Jacobson ring (cf. [BAC], V § 3.4). If every non-invertible
    element is a zero-divisor, then every prime ideal is an associated prime ideal of `B`, so in
    particular `B` has only a finite number of maximal ideals `𝔪_1, …, 𝔪_n`. Since `B` is a Jacobson ring,
    the intersection of the `𝔪_i` is the nilradical of `B`, and it follows that each `𝔪_i` is a minimal
    prime ideal of `B`, so that `dim B = 0`.

[^N.D.E-VI_A-13]: N.D.E.: We have detailed the original in what follows.

[^N.D.E-VI_A-14]: N.D.E.: We have added point (1), useful in the examples 1.3.2 that follow.

[^N.D.E-VI_A-15]: N.D.E.: We have added the sentence that follows and the examples 1.3.2.

[^N.D.E-VI_A-16]: N.D.E.: In fact one sees without difficulty that `√I` is generated by `P, Q, R` at every point `≠ 0`,
    so `F = H`.

[^N.D.E-VI_A-17]: N.D.E.: We shall see below (2.2) that `G′` is a group in the category `(Sch/k)_red`.

[^N.D.E-VI_A-18]: N.D.E.: We have added the word "locally". Moreover, the reference to Kaplansky is: *Projective
    modules*, Ann. of Maths. **68** (1958), 372–377; see also [BAC], § II.3, Ex. 3.

[^N.D.E-VI_A-19]: N.D.E.: We have detailed the original in what follows.

[^N.D.E-VI_A-20]: N.D.E.: We have added this paragraph, in order to make the link with VI_B, § 3.

[^N.D.E-VI_A-21]: N.D.E.: In this Exposé, the notation `G⁰` is reserved for the case where the connected component of
    `e` is open; in VI_B, § 3, this connected component will be denoted `G⁰` in all cases. This is a
    slightly abusive notation, but one that is compatible with what precedes when the connected component
    is the underlying topological space of an open group subscheme `G⁰` of `G`.

[^N.D.E-VI_A-22]: N.D.E.: Indeed, in a noetherian space, the connected components are finite in number, hence each one
    is open; see also EGA I, 6.1.9.

[^N.D.E-VI_A-23]: N.D.E.: We have added the numbering 2.3.1 to make this statement explicit. Note moreover that `G⁰` is
    even a characteristic subgroup of `G`, cf. 2.6.5 (ii).

[^N.D.E-VI_A-24]: N.D.E.: In the statement, we have replaced "`G⁰` is geometrically irreducible" by "`G⁰ ⊗_A k` is
    geometrically irreducible over `k`", and we have detailed the proof.

[^N.D.E-VI_A-25]: N.D.E.: We have detailed the original by adding the reference to EGA I, 6.1.10.

[^N.D.E-VI_A-26]: N.D.E.: One should beware that a non-neutral connected component is not in general geometrically
    connected. For example, if `k = ℝ`, the group `µ_{3,ℝ}`, represented by `ℝ[X]/(X³ − 1)`, has two
    connected components: `{e} = Spec ℝ` and `C = Spec ℝ[X]/(X² + X + 1)`, and `C ⊗_ℝ ℂ` has two
    components.

[^N.D.E-VI_A-27]: N.D.E.: We have added the assertion that follows, cf. VI_B, 1.5.

[^N.D.E-VI_A-28]: N.D.E.: We have detailed the original in what follows.

[^N.D.E-VI_A-29]: N.D.E.: We have simplified the original here.

[^N.D.E-VI_A-30]: N.D.E.: We make no finiteness hypotheses in this statement; this will be useful later (cf. 6.2 and
    VI_B, § 12).

[^N.D.E-VI_A-31]: N.D.E.: These results were communicated to us by O. Gabber, in particular 2.6.6, which plays an
    important role in section 5 of VI_B.

[^N.D.E-VI_A-32]: N.D.E.: This proposition (as well as the preceding results) was communicated to us by O. Gabber; it
    will be used to correct the proof of Theorem 5.3 of VI_B.

[^N.D.E-VI_A-33]: N.D.E.: We have added (ii′) and detailed point (iv), taking into account the additions made in 2.5.2,
    2.5.4, and in Exp. V, 6.1.

[^N.D.E-VI_A-34]: N.D.E.: In this case, the hypothesis that `G` is flat may be removed, cf. subsection 3.3.

[^N.D.E-VI_A-35]: N.D.E.: Let us point out here that if `A = k` is a field, then every quasi-compact open of `F\G` is
    quasi-projective (a result due to Chow for smooth algebraic groups), cf. [Ray70], VI 2.6. By contrast,
    over the Artinian local ring `A = ℂ[ε]/(ε²)`, there exist abelian `A`-schemes `G` that are not
    projective (loc. cit., XII 4.2).

[^N.D.E-VI_A-36]: N.D.E.: What precedes is valid for every base change `A → A′`.

[^N.D.E-VI_A-37]: N.D.E.: This is detailed in 4.6 below: it is a matter of seeing that the formation of the direct image
    by the morphisms `p`, `λ` and `pr_2` commutes with flat base changes `A → A′`. Since `F` and `G` are
    of finite type over the Artinian ring `A`, the morphisms `f` in question are all quasi-compact and
    quasi-separated, and the equality `f_*(O_X) ⊗_A A′ = f′_*(O_{X′})` (with obvious notations) follows
    from EGA IV_1, 1.7.21.

[^N.D.E-VI_A-38]: N.D.E.: Indeed, let `y_1, …, y_n` be arbitrary points of `X`; since `X` is of finite type over `A`,
    each `y_i` has in its closure a closed point `x_i`, and every open subset containing `x_i` contains
    `y_i`.

[^N.D.E-VI_A-39]: N.D.E.: Such an open exists, since `X` is of finite type over `k`: `X` has a finite number of
    irreducible components `C_1, …, C_p`, and it suffices to take, for each `i`, a non-empty affine open
    contained in `C_i − ⋃_{j ≠ i} C_j`. (Here one knows moreover, by (ii′), that the `C_i` are disjoint…)

[^N.D.E-VI_A-40]: N.D.E.: We have detailed the original in what follows.

[^N.D.E-VI_A-41]: N.D.E.: We have added this paragraph.

[^N.D.E-VI_A-42]: N.D.E.: We have added this subsection.

[^N.D.E-VI_A-43]: N.D.E.: For an example where `F` is not flat and `F̃\G` not representable, see [DG70], § III.3, n°
    3.3.

[^N.D.E-VI_A-44]: N.D.E.: We have written `S(G^α)` instead of `Ḡ^α` for the saturation of `G^α`.

[^N.D.E-VI_A-45]: N.D.E.: We have added the sentence that follows.

[^N.D.E-VI_A-46]: N.D.E.: In what follows, we have modified the original; the supplementary hypotheses made on `X_*`
    were superfluous.

[^N.D.E-VI_A-47]: N.D.E.: We have added on the one hand the following sentence and, on the other hand, the numbering
    4.6.1 below, to make the stated result explicit.

[^N.D.E-VI_A-48]: N.D.E.: We have added the numbering 4.7.1 below to make the stated result explicit.

[^N.D.E-VI_A-49]: N.D.E.: We have changed the title of this section (called "Compléments" in the original).

[^N.D.E-VI_A-50]: N.D.E.: We have added what follows.

[^N.D.E-VI_A-51]: N.D.E.: We have added the sentence that follows.

[^N.D.E-VI_A-52]: N.D.E.: In addition to the aforementioned statements of Exp. IV, one uses the fact that, since
    `G → F\G` is faithfully flat, an `A`-subgroup `H` of `G` is flat over `A` if and only if `F\H` is.

[^N.D.E-VI_A-53]: N.D.E.: We have detailed the original in what follows; in particular, we have added Proposition 5.4.1.

[^N.D.E-VI_A-54]: N.D.E.: We have added the number 5.4.2 to this theorem.

[^N.D.E-VI_A-55]: N.D.E.: We have added what follows.

[^N.D.E-VI_A-56]: N.D.E.: We have detailed the original in what precedes and have added Proposition 5.5.1 to make this
    result explicit.

[^N.D.E-VI_A-57]: N.D.E.: We have added the numbering 5.6.1, as well as the proof that follows.

[^N.D.E-VI_A-58]: N.D.E.: We have detailed the proof of (ii) ⇒ (i), and have simplified the diagram below.

[^N.D.E-VI_A-59]: N.D.E.: We have added the results that follow, taken from [Per75]. Note that Lemma 6.1 can be
    expressed, in Weil's language, by saying that "every point of `G` is the product of two generic
    points".

[^N.D.E-VI_A-60]: N.D.E.: Additional references cited in this Exposé.
