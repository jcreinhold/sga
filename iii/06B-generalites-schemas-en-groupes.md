# Exposé VI_B. Generalities on group schemes

<!-- label: III.VI_B -->

*by J.-E. Bertin*

> [^N.D.E-VI_B-0] Version of 13/10/2024.

<!-- original page 319 -->

This Exposé, which corresponds to no oral lecture of the seminar, is intended to bring together a number of technical
results, commonly used, concerning group schemes.[^VI_B-0-1]

[^VI_B-0-1]: This Exposé has been seriously reworked since its mimeographed edition; in particular, §§ 10 and 11 have been entirely rewritten.[^N.D.E-VI_B-1]

[^N.D.E-VI_B-1]: And also § 5, cf. N.D.E. (34) and (46).

[^N.D.E-VI_B-2]: Recall the convention adopted at the beginning of `VI_A`: an `A`-group is an `A`-group scheme (and such a scheme is separated, cf. (VI_A, 0.3)).

[^N.D.E-VI_B-3]: We have replaced "homomorphism" by "morphism".

[^N.D.E-VI_B-4]: This statement also appears in (VI_A, 2.5.2).

## 1. Morphisms of groups locally of finite type over a field

<!-- label: III.VI_B.1 -->

### 1.1.

Let `A` be an Artinian local ring, `G` and `H` two `A`-groups[^N.D.E-VI_B-2], and `u : G → H` a morphism of `A`-groups.
Then `u` induces a morphism of groups `u(A) : G(A) → H(A)`.[^N.D.E-VI_B-3] Since `H(A)` acts on `H` by right translation,
`u(A)` defines, by restriction, an action of `G(A)` on `H`. This action is compatible with the morphism `u` and with the
action of `G(A)` on `G` defined by right translation. Since `G(A)` acts transitively on the strictly rational points of
`G` (see (VI_A, 0.4) for the definition), one sees that these points "all behave in the same way with respect to `u`";
from this spring the following properties.

**Proposition 1.2.** *Let `u : G → H` be a quasi-compact morphism between `A`-groups locally of finite type over `A`.
Then the set `u(G)` is closed in `H` and one has `dim G = dim u(G) + dim Ker u`.*[^N.D.E-VI_B-4]

<!-- label: III.VI_B.1.2 -->

<!-- original page 320 -->

Since `u` commutes with the inversion morphisms of `G` and `H`, the image `u(G)` is invariant under the inversion
morphism of `H`; the same is therefore true of its closure `u(G)⁻` in `H`. On the other hand, let `L` denote the set of
points of `H ×_A H` whose two projections both lie in `u(G)`; it is clear that `L` is the image of the morphism
`u ×_A u : G ×_A G → H ×_A H`. Hence the multiplication morphism of `H` sends `L` into `u(G)`, in other words
`u(G) · u(G) = u(G)`. On the other hand, Lemma 1.2.1 below shows that `L⁻`, the closure of `L` in `H ×_A H`, is the set
of points of `H ×_A H` whose two projections lie in `u(G)⁻`; hence `u(G)⁻ · u(G)⁻ = u(G)⁻`, so that the reduced subscheme
of `H` whose underlying space is `u(G)⁻` is naturally equipped with a group structure in the category `(Sch/k)_red`,
where `k` is the residue field of `A` (cf. (VI_A, 0.2)).

Let us prove the first assertion of 1.2. Replacing `A` by the algebraic closure of its residue field `k`, we may assume
that `A` is an algebraically closed field `k` (cf. EGA IV₂, 2.3.12). Replacing `u` by `u_red : G_red → H_red`, we may
assume `G` and `H` reduced; in this case, as we have just seen, `u(G)` is the underlying space of a reduced group
subscheme of `G`; we may therefore assume `u` dominant. Then `G(k)` acts transitively on the set of connected components
of `H`, and it suffices to show that `u(G) ∩ H⁰` is closed: we are reduced to the case where `H` is connected, hence
irreducible and of finite type (VI_A, 2.4). Then `u` is of finite type, since it is quasi-compact and locally of finite
type; since `H` is noetherian, `u(G)` is constructible (EGA IV₁, 1.8.5), so it contains an open subset `V` of `H`
(EGA 0_III, 9.2.2), and then, by (VI_A, 0.5), we have `H = V · V ⊂ u(G) · u(G) = u(G)`.

Let us prove the second assertion. Recall first that the functor `Ker u` (cf. I, 2.3.6.1) is representable by `u⁻¹(e)`,
where `e` denotes the unit element of `H`. When `u` is locally of finite type, `Ker u` is therefore locally of finite
type over `A`. We reduce as before, this time using EGA IV₂, 4.1.4, to the case where `A` is an algebraically closed
field `k`.
<!-- original page 321 -->
We may further assume `G` and `H` irreducible and of finite type and `u` dominant: indeed, `k` being algebraically
closed, it is clear that the connected components of `G`, on the set of which `G(k)` acts transitively, all have the
same dimension, and that if `u⁰` denotes the restriction of `u` to `G⁰`, then `(Ker u)⁰ ⊂ Ker u⁰`, and
`dim Ker u⁰ = dim Ker u`. One sees likewise that `u` is then of finite type over `k`. If `η` denotes the generic point
of `H`, one has `dim u⁻¹(η) = dim G − dim H` (EGA IV₃, 10.6.1 (ii)). By EGA IV₃, 9.2.3 and 9.2.6, the set of `y ∈ H` such
that `dim u⁻¹(y) = dim u⁻¹(η)` contains a non-empty open subset `V`. Since `u` is dominant, `U = u⁻¹(V)` is then a
non-empty open subset of `G` and contains a closed point `x` of `G`, since `G` is a Jacobson scheme (EGA IV₃, 10.4.7).
Then right translation `r_x` is an isomorphism of `Ker u` onto `u⁻¹(u(x))`, so that:

```text
dim Ker u = dim u⁻¹(u(x)) = dim u⁻¹(η) = dim G − dim H.
```

**Lemma 1.2.1.** *Let `f : X′ → X` and `g : Y′ → Y` be two quasi-compact, dominant morphisms of schemes over an Artinian
local ring `A`. Then `f ×_A g : X′ ×_A Y′ → X ×_A Y` is dominant (and quasi-compact).*

<!-- label: III.VI_B.1.2.1 -->

Indeed, one has `f ×_A g = (id_X ×_A g) ∘ (f ×_A id_{Y′})`. It therefore suffices to show that `f ×_A id_{Y′}` and
`id_X ×_A g` are dominant. For this one may replace `A` by its residue field `k`. In this case, `X` and `Y′` are flat
over `A = k`, and since `f ×_A id_{Y′}` (resp. `id_X ×_A g`) is deduced from `f` (resp. `g`) by the flat base change
`Y′ → A` (resp. `X → A`), it is dominant (and quasi-compact), by EGA IV₂, 2.3.7.

<!-- original page 333 -->

**Counterexample 1.2.2.** *Let `k` be a field of characteristic 0, `G` the constant `k`-group `ℤ`, and `H` the additive
`k`-group `G_{a,k}`. Let `u : G → H` be a morphism of `k`-groups. If `u ≠ 0`, then `u(G)` is not closed in `H`.*

<!-- label: III.VI_B.1.2.2 -->

**Proposition 1.3.** [^N.D.E-VI_B-5] *Let `A` be an Artinian local ring, `k` its residue field, `G` an `A`-group locally
of finite type and flat, `u : G → H` a morphism of `A`-groups. The following assertions are equivalent:*

*(i) `u` is flat (resp. quasi-finite, resp. unramified, resp. smooth, resp. étale) at some point of `G`.*[^N.D.E-VI_B-6]

*(ii) `u` is flat (resp. quasi-finite, resp. unramified, resp. smooth, resp. étale).*

<!-- label: III.VI_B.1.3 -->

[^N.D.E-VI_B-5]: In the original, 1.3, 1.3.1, and 1.3.1.1 are stated for `A` a field. For completeness, we have treated the case of an Artinian local ring; to do so, we have added Lemma 1.3.0.

[^N.D.E-VI_B-6]: Recall that a morphism of schemes `f : X → Y` is said to be *of finite type* (resp. *of finite presentation*, resp. *quasi-finite*) *at `x`* if there exist affine opens `V` containing `f(x)` and `U` containing `x` such that `f(U) ⊂ V` and `O_X(U)` is an `O_Y(V)`-algebra of finite type (resp. of finite presentation, resp. and moreover the fiber `f⁻¹(f(x′))` is finite for all `x′ ∈ U`; see also N.D.E. (40) of Exp. V). One says that `f` is *locally quasi-finite* (resp. *of finite type*, *of finite presentation*) if it has this property at every point `x`. On the other hand, one says that `f` is *smooth* (resp. *unramified*, resp. *étale*) *at `x`* if there exists an open neighborhood `U` of `x` such that the morphism `f|_U : U → Y` is smooth (resp. unramified, resp. étale). In view of these definitions, it is clear that the set of points where `f` is of finite presentation, resp. of finite type, quasi-finite, smooth, unramified, étale, is open in `X`. Moreover, since the flat locus of a morphism locally of finite presentation is open (EGA IV₃, 11.3.1), the set of points of `X` where `f` is of finite presentation and flat is also open in `X`. All of this will be used repeatedly in what follows.

*Proof.* It suffices to show that (i) implies (ii). First, we have the following lemma.

**Lemma 1.3.0.** *Let `A → B → C` be morphisms of commutative rings and let `n` be a nilpotent ideal of `A`. Suppose that
`C/nC` is a `(B/nB)`-algebra of finite type.*

*(i) Then `C` is a `B`-algebra of finite type.*

*(ii) Moreover, if `C` is flat over `A` and if `C/nC` is a `(B/nB)`-algebra of finite presentation, then `C` is a
`B`-algebra of finite presentation.*

<!-- label: III.VI_B.1.3.0 -->

Indeed, let `x_1, …, x_n` be elements of `C` whose images generate `C/nC` as a `(B/n)`-algebra. By the nilpotent Nakayama
lemma, the `x_i` generate `C` as a `B`-algebra. This proves (i). Let `φ` be the resulting surjective morphism
`B[X_1, …, X_n] → C`, and let `I = Ker(φ)`.

Suppose now that `C` is flat over `A` and that `C/nC` is of finite presentation over `B/nB`. Then, on the one hand,
`I/nI` is identified with the kernel of `φ̄ = φ ⊗_A (A/n)`. On the other hand, by EGA IV₁, 1.4.4, the kernel of `φ̄` is
an ideal of finite type. Let then `P_1, …, P_s` be elements of `I` whose images generate `I/nI` as an ideal; by the
nilpotent Nakayama lemma, they generate `I`. This proves (ii).

Let us return to the proof of 1.3. Let `x` be an arbitrary point of `G`. Since `G` is flat over `A`, the fiber-wise
flatness criterion in the form of EGA IV₃, 11.3.10.2, shows that `u` is flat at `x` if `u ⊗_A k` is. Likewise, by the
preceding lemma, one sees that `u` is of finite type (resp. of finite presentation) at `x` if `u ⊗_A k` is. Since the
other properties are then verified on fibers (cf. EGA IV₄, 17.4.1, 17.5.1, and 17.6.1, for unramified, smooth, and
étale), we are reduced to the case `A = k`.

<!-- original page 334 -->

Let now `x` be a point of `G` where one of the conditions of 1.3 (i) holds. Since the properties under consideration are
preserved by (fpqc) descent (cf. EGA IV, 2.5.1, 2.7.1, and 17.7.1), one reduces, by replacing `k` by an algebraic
closure of `κ(x)`, to the case where `k` is algebraically closed and `x ∈ G(k)`.

Since `G` is a Jacobson scheme (cf. EGA IV₃, 10.4.7) and since the set `W` of points of `G` where `u` is flat (resp.
quasi-finite, unramified, smooth, or étale) is stable under generization[^N.D.E-VI_B-7] (resp. open), it suffices to
show that every point `y ∈ G(k)` belongs to `W`. Now, for such a point `y`, the translation `r_y ∘ r_x⁻¹` sends `x` to
`y`, hence `u` has the desired property at `y`, i.e. `y ∈ W`. ∎

[^N.D.E-VI_B-7]: The original stated that `W_flat` is open, which does not seem a priori obvious...

**Corollary 1.3.1.** *Let `A` be an Artinian local ring, `k` its residue field, `G` a flat `A`-group. The following
assertions are equivalent:*[^N.D.E-VI_B-8]

*(i) `G` is locally quasi-finite (resp. unramified, resp. smooth, resp. étale) over `A` at some point.*

*(ii) `G` is locally quasi-finite (resp. unramified, resp. smooth, resp. étale) over `A`.*

<!-- label: III.VI_B.1.3.1 -->

[^N.D.E-VI_B-8]: Note that it does not suffice to assume that `G` is flat over `A` at one point: for instance, suppose `A ≠ k`, let `H` be the constant `A`-group `(ℤ/2ℤ)_A` and `G` the closed `A`-subgroup of `H` whose non-neutral component is reduced; then the structural morphism `G → Spec A` is a local isomorphism at the unit point `e`, but is not flat at the point `g ≠ e`.

[^N.D.E-VI_B-9]: We have added the following sentence, and simplified the proof of Lemma 1.3.1.1, by invoking EGA IV, 2.7.1 instead of loc. cit., 17.7.5.

[^N.D.E-VI_B-9] *Proof.* Indeed, if `G` satisfies one of the conditions of (i) at a point `x`, there exists an open
neighborhood `U` of `x` which is of finite type over `A`. Consequently, it suffices to apply 1.3 in the case where `H`
is the unit `A`-group, taking into account the following lemma. ∎

**Lemma 1.3.1.1.** *Let `A` be an Artinian local ring and `G` an `A`-group. If there exists a non-empty open subset of
`G` of finite type over `A`, then `G` is locally of finite type over `A`.*

<!-- label: III.VI_B.1.3.1.1 -->

By Lemma 1.3.0, we may assume `A` equal to its residue field `k`. Moreover, by (fpqc) descent, we may assume `k`
algebraically closed (cf. EGA IV₂, 2.7.1). Let `V` be the open subset of `G` formed by the points where `G` is of finite
type over `k`; by hypothesis, `V ≠ ∅`. Since `G` is a Jacobson scheme, `V` contains a closed point `x` and, to show that
`V = G`, it suffices to show that every closed point `y` of `G` belongs to `V`. Now, for such a point `y`, the
translation `r_y ∘ r_x⁻¹` sends `x` to `y`, whence `y ∈ V`. ∎

**Corollary 1.3.2.** *Let `A` be an Artinian local ring, `u : G → H` a morphism between `A`-groups locally of finite
type. The following assertions are equivalent:*

*(i) `u` is universally open,*

*(ii) `u` is open,*

*(iii) `u` is open at some point of `G`,*

*(iv) the morphism `u⁰ : G⁰ → H⁰` deduced from `u` is dominant,*

*(iv′) `u⁰` is surjective,*

*(v) there exists a connected component `C` of `G` such that, if `D` denotes the connected component of `H` containing
`u(C)`, the morphism `u′ : C → D` deduced from `u` is dominant.*

<!-- label: III.VI_B.1.3.2 -->

*Proof.* The implications (i) ⇒ (ii) ⇒ (iii) and (iv′) ⇒ (iv) ⇒ (v) are clear. Since `G⁰` is of finite type over `A`
(VI_A, 2.4), and hence noetherian, `u⁰` is quasi-compact, so `u⁰(G⁰)` is closed in `H⁰` by 1.2; hence (iv) ⇒ (iv′). On
the other hand, since `G⁰` (resp. `C`) is open in `G` (VI_A, 2.3) and `H⁰` (resp. `D`) is irreducible (VI_A, 2.4.1), one
sees that (ii) implies (iv) (resp. (iii) implies (v)). It remains to show that (v) implies (i).

<!-- original page 324 -->

The open subset `C` (resp. `D`) of `G` (resp. `H`) will be endowed with its induced scheme structure, and `u′` will
denote the morphism `C → D` deduced from `u`. Let `k` be the residue field of `A`.[^N.D.E-VI_B-10] Since the base change
`Spec k → Spec A` is a universal homeomorphism, we may assume `A = k`. By hypothesis, `u′` is dominant and, since `C` is
of finite type over `k` (VI_A, 2.4.1) and hence noetherian, `u′` is quasi-compact. By EGA IV₂, 2.3.7, `u′ ⊗_k k̄` is
again quasi-compact and dominant, where `k̄` denotes an algebraic closure of `k`. Then, since `C ⊗_k k̄` is a union of
connected components of `G ⊗_k k̄`, the morphism `u ⊗_k k̄ : G ⊗_k k̄ → H ⊗_k k̄` satisfies assertion (v). We are thus
reduced to the case where `A = k` is an algebraically closed field, taking into account EGA IV₂, 2.6.4.

[^N.D.E-VI_B-10]: We have expanded the original in what follows.

In this case, we may further replace `u` by `u_red`, and we are reduced to the case where `H` is reduced. Let then `ξ`
(resp. `η`) be the generic point of `C` (resp. `D`). Since `u′` is quasi-compact and dominant, `u′(ξ) = η` (cf.
EGA IV₁, 1.1.5). On the other hand, since `H` is reduced, the local ring `O_{H,η}` is a field, hence `u′` is flat at the
point `ξ`.[^N.D.E-VI_B-11] Hence, by 1.3, `u` is flat; moreover, since `u` is locally of finite type and `H` is locally
noetherian, `u` is locally of finite presentation. Therefore, by EGA IV₂, 2.4.6, `u` is universally open. ∎

[^N.D.E-VI_B-11]: The original invoked the generic flatness theorem (EGA IV₂, 6.9.1), which is not necessary here.

**Proposition 1.4.** *Let `A` be an Artinian local ring, and `u : G → H` a quasi-compact morphism between `A`-groups
locally of finite type. The following assertions are equivalent:*

*(i) `u` is proper,*

*(ii) there exists `h ∈ H` such that the fiber `u⁻¹(h)` is non-empty and proper over `κ(h)`,*

*(iii) `Ker u` is proper over `A`.*

<!-- label: III.VI_B.1.4 -->

*Proof.* It is clear that (i) implies (iii), and that (iii) implies (ii). On the other hand, it follows from the
hypotheses that `u` is of finite type and, since `G` is separated (VI_A, 0.3), so is `u` (EGA I, 5.5.1). It therefore
remains to show that assertion (ii) implies that `u` is universally closed, so that we may assume `A` equal to its
residue field `k`.[^N.D.E-VI_B-12] Let `k′` be an algebraic closure of `κ(h)`, `u′ : G′ → H′` the morphism deduced from
`u` by base change, and `h′` a point of `H′` above `h`; then the fiber `u′⁻¹(h′) = u⁻¹(h) ×_{κ(h)} k′` is non-empty and
proper, and it suffices to show that `u′` is proper (EGA IV₂, 2.6.4). We may therefore assume that `k` is algebraically
closed and `h ∈ H(k)`.

[^N.D.E-VI_B-12]: We have added the following sentence.

<!-- original page 336 -->

We have seen (1.2) that `u(G)` is then the underlying set of a closed reduced group subscheme of `H`; since every closed
immersion is proper (EGA II, 5.4.2), we may assume that `u` is surjective and that `H` is reduced. Since `u` is
surjective, the group `G(k)` acts transitively on the set of closed points of `H`; whatever the closed point `y` of
`H`, `u⁻¹(y)` is therefore proper over `κ(y)`. By EGA IV₃, 9.6.1, the set of `y ∈ H` such that `u⁻¹(y)` is not proper
over `κ(y)` is locally constructible; since it contains no closed point, it is empty (cf. EGA IV₃, 10.3.1 and 10.4.7).

[^N.D.E-VI_B-13] Consider now the generic point `η` of `H⁰`; by what precedes, the fiber
`u⁻¹(η) = G ×_H Spec κ(η)` is proper over `κ(η)`. On the other hand, since `H` is reduced, `κ(η)` equals `O_{H,η}`.
Since `O_{H,η}` is the direct limit of the rings `O_H(V)`, as `V` runs through the non-empty open subsets of `H⁰`, it
follows from EGA IV₃, 8.1.2 a) and 8.10.5 (xii), that there exists a non-empty open subset `V` of `H⁰` such that the
restriction of `u` over `V` is proper. It is then clear that the `g · V`, for `g ∈ G(k)`, form an open cover of `H`
such that, for every `g ∈ G(k)`, the restriction of `u` over the open `g · V` is proper; one deduces that `u` is proper
(cf. EGA II, 5.4.1). ∎

[^N.D.E-VI_B-13]: We have expanded the original in what follows.

**Corollary 1.4.1.** *Let `A` be an Artinian local ring, and `u : G → H` a morphism between `A`-groups locally of finite
type. The following assertions are equivalent:*

*(i) `u` is locally quasi-finite,*

*(ii) `u` is quasi-finite at some point,*

*(iii) `Ker u` is discrete,*

*(iv) the restriction of `u` to each connected component of `G` is finite.*

*If in addition `u` is quasi-compact, these assertions are equivalent to the following:*

*(v) `u` is finite.*

<!-- label: III.VI_B.1.4.1 -->

*Proof.* It is clear that (iv) implies (iii), that (iii) implies (ii) (EGA I, 6.4.4), and that, in the case where `u` is
quasi-compact, assertions (iv) and (v) are equivalent. We have already seen in 1.3 that (i) and (ii) are equivalent.

Let us show finally that (i) implies (iv). Let `C` be a connected component of `G`; since `C` is of finite type over `A`
(VI_A, 2.4.1) and `G` and `H` are separated (VI_A, 0.2), by EGA I, 5.5.1 and 6.3.4, the restriction `u′` of `u` to `C`
is separated and of finite type.[^N.D.E-VI_B-14] Since the fibers of `u′` are discrete, it follows that `u′` is
quasi-finite (cf. EGA II, 6.2.2). Since every quasi-finite proper morphism is finite (cf. EGA III₁, 4.4.2), it therefore
suffices to show that `u′` is universally closed.

[^N.D.E-VI_B-14]: We have expanded the original in what follows.

For this, we may assume that `A` is equal to its residue field `k`. Then, by (fpqc) descent (cf. EGA IV₂, 2.6.4), it
suffices to show that `u′ ⊗_k k̄` is universally closed, where `k̄` denotes an algebraic closure of `k`. Moreover, since
`C` is of finite type over `k`, `C ⊗_k k̄` is the sum of finitely many connected components `C′_1, …, C′_n` of
`G ⊗_k k̄`, and it suffices to show the assertion for each `C′_i`. One is thus reduced to the case where `k` is
algebraically closed.

<!-- original page 337 -->

Let then `g` be a closed point of `C`. If `u⁰ : G⁰ → H` is the restriction of `u` to `G⁰`, one has
`u′ = r_{u(g)} ∘ u⁰ ∘ r_g⁻¹`, where `r_g` denotes right translation by `g`. Therefore, to show that `u′` is proper, it
suffices to show that `u⁰` is. By hypothesis, `u` is locally quasi-finite, so the fiber `Ker u` is discrete (and
non-empty); we have seen that `u⁰` is of finite type, so the fiber `Ker u⁰` is finite (cf. EGA II, 6.2.2), hence proper
and non-empty. Therefore `u⁰` is proper by 1.4. ∎

**Corollary 1.4.2.** *Let `A` be an Artinian local ring, and `u : G → H` a quasi-compact morphism between `A`-groups
locally of finite type. The following assertions are equivalent:*[^N.D.E-VI_B-15]

*(i) `u` is a closed immersion,*

*(ii) `u` is a monomorphism,*

*(iii) `Ker u` is trivial, i.e. isomorphic to the unit `k`-group.*

*In particular, every group subscheme[^N.D.E-VI_B-16] of `H` is closed.*

<!-- label: III.VI_B.1.4.2 -->

[^N.D.E-VI_B-15]: The hypothesis that `G` and `H` are locally of finite type may be removed, since according to [Per76, 4.2.4]: every quasi-compact monomorphism `u : G → H` between group schemes over a field `k` is a closed immersion; see also [DG70, III.3.7.2 b)] for the case where `G` and `H` are affine (in which case every morphism `G → H` is affine (EGA II, 1.6.2 (v)), hence quasi-compact).

[^N.D.E-VI_B-16]: In this particular case, see also (VI_A, 0.5.2), valid without finiteness hypotheses.

*Proof.* It is clear that (i) implies (ii), and if one considers the functors represented respectively by `G` and `H`,
it is immediate that conditions (ii) and (iii) are equivalent. Finally, if `Ker u` is the unit `k`-group, `Ker u` is a
proper non-empty fiber, so `u` is a proper monomorphism by 1.4, of finite presentation since `H` is locally noetherian
(EGA IV₁, 1.6.1), and hence a closed immersion (EGA IV₃, 8.11.5).

The last assertion follows from the fact that, since `H` is locally noetherian, every immersion `G → H` is quasi-compact
(EGA I, 6.6.4). ∎

**Counterexample 1.4.3.** *Let `k` be a field of characteristic 0, `G` the constant `k`-group `ℤ`, and `H` the `k`-group
`G_{a,k}`. Let `u : G → H` be a morphism of `k`-groups. If `u ≠ 0`, then `Ker u = 0`, but `u` is not a closed immersion
(cf. 1.2.2).*

<!-- label: III.VI_B.1.4.3 -->

We shall use later the two following results, which should have appeared in Exposé VI_A:

**Lemma 1.5.** *Let `k` be a field and `G` a `k`-group locally of finite type. Then:*

*(i) All irreducible components of `G` have the same dimension.*

*(ii) For every `g ∈ G`, one has `dim_g G = dim G`.*

<!-- label: III.VI_B.1.5 -->

<!-- original page 338 -->

[^N.D.E-VI_B-17] Assertion (i) has already been proved in (VI_A, 2.4.1), and assertion (ii) follows from it. Indeed,
let `g` be a point of `G` and `C` the connected component of `G` containing `g`. By definition
(EGA 0_IV, 14.1.2), `dim_g G` is the infimum of the integers `dim U`, as `U` runs through the open neighborhoods of `g`;
one therefore has `dim_g G = dim U_0` for some `U_0`, which one may assume contained in `C` (since `dim V ≤ dim U` if
`V ⊂ U`). Then, since `C` is irreducible and of finite type over `k` (VI_A, 2.4.1), one has
`dim U_0 = dim C = tr.deg_k κ(ξ)`, where `ξ` is the generic point of `C`, by EGA IV₂, 5.2.1. Hence
`dim_g G = dim C = dim G`. ∎

[^N.D.E-VI_B-17]: The implication (ii) ⇒ (i) is a general fact (cf. EGA 0_IV, 14.1.6), and (i) ⇒ (ii) follows from the fact that if `X` is an irreducible scheme of finite type over a field, one has `dim X = dim U` for every non-empty open subset `U` of `X`; the essential point here is therefore to establish assertion (i), which has already been done in an addition to (VI_A, 2.4.1). We have modified the statement and proof of the lemma accordingly.

**Proposition 1.6.** [^N.D.E-VI_B-18] *Let `S` be a scheme of characteristic zero and `G` an `S`-group scheme, locally
of finite presentation over `S` at every point of the unit section `ε(S)`. For `G` to be smooth over `S` at every point
of the unit section, it is necessary and sufficient that the `O_S`-module
`ω_{G/S} = ε*(Ω¹_{G/S})` (called the conormal module to the unit section of `G`) be locally free.*

<!-- label: III.VI_B.1.6 -->

[^N.D.E-VI_B-18]: In the statement, we have replaced "along the unit section" by "at every point of the unit section"; on the other hand, at the end of the proof, we have made explicit the results of EGA IV₄ cited in reference.

Recall that a scheme `S` is said to be *of characteristic zero* if for every closed point `x` of `S`, the field `κ(x)`
has characteristic zero.

Recall also (II 4.11) that, if `π` denotes the structural morphism `G → S`, one has `Ω¹_{G/S} = π*(ω_{G/S})`, so that it
comes to the same thing to say that the `O_S`-module `ω_{G/S}` is locally free, or that the `O_G`-module `Ω¹_{G/S}` is
locally free.

If there exists an open neighborhood `U` of `ε(S)` which is smooth over `S`, then, by EGA IV₄, 17.2.3, `Ω¹_{U/S}` is
locally free of finite type, as well as `ω_{G/S} = ε*(Ω¹_{U/S})`.

Conversely, if `ω_{G/S}` is locally free, the same holds for `Ω¹_{G/S} = π*(ω_{G/S})`. Since `S` is of characteristic
`0`, the Jacobian criterion (EGA IV₄, 16.12.2) therefore implies that `G` is differentially smooth over `S`. Then it
follows from EGA IV₄, 17.12.5, that `G` is smooth over `S` at every point of the unit section. ∎

**Corollary 1.6.1 (Cartier).** *Given a field `k` of characteristic zero, every `k`-group locally of finite type over
`k` is smooth over `k`.*

<!-- label: III.VI_B.1.6.1 -->

Indeed, it is then clear that the `k`-module `ω_{G/k}` is locally free, so, by 1.6, `G` is smooth over `k` at the unit
point `e`, and hence smooth over `k` by 1.3.1. ∎

## 2. "Open properties" of groups and group morphisms locally of finite presentation

<!-- label: III.VI_B.2 -->

### 2.0.

In all that follows, `S` will denote an arbitrary scheme; an `S`-group scheme will be called an `S`-*group*. Given an
`S`-group `G`, we shall denote by `ε` the unit section, by `c : G → G` the inversion morphism, and by `µ` the
multiplication morphism `G ×_S G → G`. For every `S`-scheme `X`, we shall denote by `π` or `π_X` the structural morphism
`X → S`.

<!-- original page 329 -->

Given a property `P(u)` of a morphism of `S`-schemes `u : X → Y`, we shall say that `P(u)` is *stable under base change*
if, whenever `u` satisfies `P(u)`, so does the morphism `u_{(Y′)}`, for any `S`-morphism `Y′ → Y`. We say that `P(u)` is
*local in nature for the topology `T`* (cf. Exp. IV, §§ 4 and 6) if `P(u)` satisfies the following two conditions:

a) `P(u)` is stable under base change,

b) whenever there exists a covering family of `S`-morphisms `Y_i → Y` for the topology `T` such that each morphism
`u_{(Y_i)}` satisfies `P(u)`, then `u` satisfies `P(u)`.

**Proposition 2.1.** *Let `P(u)` be a property of a morphism of `S`-schemes, local in nature for the (fpqc) topology.
Let `u : G → H` be a morphism of `S`-groups. Assume `G` flat and universally open over `S`.*

*Let `W` be the largest open subset of `H` above which `u` satisfies the property `P(u)`, and let `V = u⁻¹(W)`. Then
`U = π_G(V)` is open in `S` and `V` is an open group subscheme of `G|_U`.*

<!-- label: III.VI_B.2.1 -->

The existence of a largest open subset `W` of `H` above which `u` satisfies `P(u)` follows from the fact that `P(u)` is
local in nature for the Zariski topology. Since `π_G` is universally open, `π_G(V)` is an open subset `U` of `S`. It
suffices to show that `V` is a group subscheme of `G|_U`. We may therefore assume `U = S`.

<!-- original page 330 -->

Set then `G′ = G ×_S V`, `H′ = H ×_S V`, `V′ = V ×_S V`, `W′ = W ×_S V`, and `u′ = u_{(V)}`; let `W′_1` be the largest
open subset of `H′` above which `u′` satisfies `P(u)`; since `V` is flat and universally open over `S`, so is `H′` over
`H`, and Lemma 2.1.1 below shows that `W′_1 = W′`. Now consider the automorphism of `V`-schemes `a` (resp. `b`) of `G′`
(resp. `H′`), namely right translation by the inverse of the diagonal section `δ` (resp. by the inverse of `u(δ)`),
defined by

```text
a(g, v) = (g · v⁻¹, v),    (resp. b(h, v) = (h · u(v⁻¹), v)),
```

for any morphism `T → S`, `g ∈ G(T)`, `v ∈ V(T)`, and `h ∈ H(T)`. It is clear that `u′ ∘ a = b ∘ u′`, which shows that
`W′` is stable under `b`, hence `V′` is stable under `a`, so that `V` is a group subscheme of `G`. ∎

**Lemma 2.1.1.** *Let `P(u)` be a property of an `S`-morphism `u`, local in nature for the (fpqc) topology. Consider a
cartesian square of morphisms of `S`-schemes:*

```text
       f′
X′ ─────────→ Y′
│              │
│              │ g
▼              ▼
X  ─────────→ Y,
       f
```

*where `g` is flat and open. Let `W` (resp. `W′_1`) be the largest open subset of `Y` (resp. `Y′`) above which `f`
(resp. `f′ = f_{(Y′)}`) satisfies `P(u)`. Then `W′_1 = W ×_Y Y′`.*

<!-- label: III.VI_B.2.1.1 -->

Set `W′ = W ×_Y Y′`; since `P(u)` is stable under base change, one has `W′ ⊂ W′_1`. Since `g` is open, `W_1 = g(W′_1)`
is an open subset of `Y`. Set `V_1 = f⁻¹(W_1)` and `V′_1 = V_1 ×_{W_1} W′_1`; it is clear that `V′_1 = f′⁻¹(W′_1)`. Since
`g` is flat and open, the morphism `W′_1 → W_1 = g(W′_1)` deduced from `g` is faithfully flat and open, hence covering
for the (fpqc) topology (cf. IV 6.3.1 (iv)). Since the morphism `V′_1 → W′_1` deduced from `f′` satisfies `P(u)`, the
same holds for the morphism `V_1 → W_1` deduced from `f`; hence `W_1 ⊂ W`, and `W′_1 ⊂ g⁻¹(W_1) ⊂ g⁻¹(W) = W′`;
therefore `W′ = W′_1`. ∎

**Remark 2.1.2.** *A great many properties of a morphism are local in nature for the (fpqc) topology; let us mention
the properties of being flat, (universally) open, (locally) of finite type, of finite presentation, quasi-finite
(cf. EGA IV₂, 2.5.1, 2.6.1 and 2.7.1), smooth, étale, unramified (EGA IV₄, 17.7.3).*

*The proof of 2.1 in fact uses only base changes by flat morphisms; the proposition therefore applies to a property
satisfying condition b) of 2.0 relative to the (fpqc) topology, and stable under base change by flat morphisms (for
example, that of being quasi-compact and dominant).*

<!-- original page 331 -->

*Of course, one can state an analogous proposition concerning properties local in nature for a topology `T` finer than
the Zariski topology, the condition to verify on `G` being then that `π_G` be universally open and covering for the
topology `T`.*

*In particular, if `G` is flat and locally of finite presentation over `S`, one has an analogous statement for
properties stable under base change by flat morphisms locally of finite presentation, satisfying condition b) of 2.0
relative to the (fpqc) topology (e.g., the properties of being regular, reduced, Cohen–Macaulay, etc.
(EGA IV₂, 6.8)).*

<!-- label: III.VI_B.2.1.2 -->

**Proposition 2.2.** *Let `G` and `H` be two `S`-groups and `u : G → H` a morphism of `S`-groups. Then:*[^N.D.E-VI_B-19]

*(i) Suppose `G` or `H` flat over `S`, and `G` or `H` locally of finite presentation over `S`, and let `V` be the
largest open subset of `G` such that the restriction of `u` to `V` is flat and locally of finite presentation (resp.
smooth, resp. étale). Then `U = π_V(V)` is open in `S`, and `V` is an open group subscheme of `G|_U`.*

*(ii) Suppose `G` or `H` universally open over `S`, and let `V` be the largest open subset of `G` such that the
restriction of `u` to `V` is universally open. Then `U = π_V(V)` is open in `S`, and `V` is an open group subscheme of
`G|_U`.*

<!-- label: III.VI_B.2.2 -->

[^N.D.E-VI_B-19]: In case (i), the open subset `V` is formed by all the points of `G` at which `u` is smooth, resp. étale, resp. of finite presentation and flat, cf. N.D.E. (6). On the other hand, in case (ii), `V` is the largest open subset contained in the set `E` of points of `G` at which `u` is universally open, but `E` is not necessarily open, as shown by the following example (EGA IV₃, 14.1.3 (i)): let `k` be a field, `H = S = Spec A` with `A = k[x]`, and `G` the `S`-group `Spec A[y]/(xy)`; then `E` equals the unit section of `G`, which is not open.

*Proof.* We first show (i). Let us show that the restriction `π_V` of `π_G` to `V` is flat and locally of finite
presentation.

a) If `π_G` is flat (resp. locally of finite presentation), so is `π_V`.

b) If `π_H` is flat (resp. locally of finite presentation), so is `π_V`, as the composition of the restriction of `u` to
`V` and `π_H`.

So in the four cases envisaged in the statement, `π_V` is flat and locally of finite presentation, hence universally
open (EGA IV₂, 2.4.6). Set `U = π_V(V)`; `U` is therefore open in `S`. It then suffices to show that `V` is an open
group subscheme of `G|_U`; we may therefore assume `U = S`.

Set then `G′ = G ×_S V`, `H′ = H ×_S V`, `V′ = V ×_S V` and `u′ = u_{(V)}`. Then, since `V` is flat and locally of
finite presentation over `S`, so is `H′` over `H`. By EGA IV₄, 17.7.4, `V′` is then the largest open subset of `G′`
such that the restriction of `u′` to `V′` is flat and locally of finite presentation (resp. smooth, resp. étale). With
the automorphisms `a` and `b` defined as in the proof of 2.1, it is then clear that `V′` is stable under `a`, hence `V`
is a group subscheme of `G`.

Let us show (ii). The restriction `π_V` of `π_G` to `V` is a universally open morphism, either because so is `π_G`, or
as the composition of the restriction of `u` to `V` and `π_H` in the case where `π_H` is universally open. Set
`U = π_V(V)`; `U` is then open in `S`. It suffices to show that `V` is an open group subscheme of `G|_U`. We may
therefore assume `U = S`.

Set as before `G′ = G ×_S V`, `H′ = H ×_S V`, `V′ = V ×_S V` and `u′ = u_{(V)}`. Then `π_V : V → S` is surjective and
universally open, the same is true of `G′ → G`, so that `V′` is the largest open subset of `G′` such that the
restriction of `u′` to `V′` is universally open, by virtue of (EGA IV₃, 14.3.4 (i) and (ii)). With the automorphisms
`a` and `b` defined as before, it is then clear that `V′` is stable under `a`, hence `V` is a group subscheme of `G`. ∎

<!-- original page 333 -->

**Corollary 2.3.** *Let `G` be an `S`-group and `V` the largest open subset of `G` which is flat and locally of finite
presentation (resp. smooth, étale, universally open) over `S`. Then `U = π_V(V)` is open in `S`, and `V` is an open
group subscheme of `G|_U`.*

<!-- label: III.VI_B.2.3 -->

It suffices to apply 2.2 in the case where `H` is the unit `S`-group and `u` is the unique morphism of `S`-groups
`G → H`, since then `π_H` is an isomorphism and `π_G = π_H ∘ u`. ∎

**Corollary 2.4.** *Let `G` be an `S`-group; if there exists a neighborhood `X` of the unit section having one (or
several) of the following properties:*

*`X` is flat and locally of finite presentation (resp. smooth, étale, universally open) over `S`,*

*then there exists an open group subscheme of `G` having the same properties.*

<!-- label: III.VI_B.2.4 -->

It suffices to apply 2.3, remarking that here, with the notations of 2.2, one has `ε(S) ⊂ V`, hence `U = S`. ∎

**Proposition 2.5.** [^N.D.E-VI_B-20] *Let `u : G → H` be a morphism of `S`-groups.*

*(i) Suppose that `G` (resp. `H`) is of finite presentation and flat (resp. of finite type) over `S` at the points of
its unit section. Then the sets:*

```text
U_flat ⊃ U_smooth ⊃ U_ét,
```

*formed of the points `s ∈ S` such that `u_s` is flat (resp. smooth, étale), are open in `S`.*

*If moreover `G` (resp. `H`) is locally of finite presentation and flat (resp. locally of finite type) over `S`, then
the set `V_flat` (resp. `V_smooth`, `V_ét`) of points of `G` where `u` is flat (resp. smooth, resp. étale) is the inverse
image under `π_G` of `U_flat` (resp. `U_smooth`, `U_ét`).*

*(ii) Suppose that, for every `s ∈ S`, `G_s` is locally of finite type over `κ(s)` (a condition satisfied if `G` is of
finite type over `S` at the points of the unit section (1.3.1.1)), and that `u` is locally of finite type (resp. locally
of finite presentation) at the points of the unit section of `G`. Then the sets:*

```text
U_l.q.f. ⊃ U_n.r.
```

*formed of the `s ∈ S` such that `u_s` is locally quasi-finite (resp. unramified) are open in `S`.*

*If moreover `u` is locally of finite type (resp. locally of finite presentation), then the set `V_l.q.f.`
(resp. `V_n.r.`) of points of `G` where `u` is quasi-finite (resp. unramified) is the inverse image under `π_G` of
`U_l.q.f.` (resp. `U_n.r.`).*

<!-- label: III.VI_B.2.5 -->

[^N.D.E-VI_B-20]: We have expanded the statement and the proof, and in (i) we have weakened the hypothesis on `H` by replacing "of finite presentation" by "of finite type".

*Proof.* Let us show (i). First note (1.3.1.1) that, for every `s ∈ S`, `G_s` is locally of finite type over `κ(s)`.
Let `Y` be the open subset of `H` formed by the points where `π_H` is of finite type, and let `X_1` be the open subset
of `u⁻¹(Y)` formed by the points where `π_G` is of finite presentation. By EGA IV₃, 11.3.1, the set `X` of points of
`X_1` where `π_G` is of finite presentation and flat is open in `X_1`, hence in `G`.

Let `u_X : X → Y` be the morphism deduced from `u`. Since `Y` (resp. `X`) contains the unit section of `H` (resp. `G`),
the restriction `π_X` of `π_G` to `X` is surjective, and the morphism `S → X` deduced from `ε_G` is an `S`-section of
`X`.

Consider the sets `W_flat ⊃ W_smooth ⊃ W_ét`, formed by the points of `X` where `u_X` is flat (resp. smooth, resp.
étale). It is clear that `W_smooth` and `W_ét` are open in `X`, cf. N.D.E. (6). On the other hand, since `π_Y` is
locally of finite type and `π_X = π_Y ∘ u_X` is locally of finite presentation, by EGA IV₁, 1.4.3 (v), `u_X` is locally
of finite presentation. Consequently, the flat locus `W_X` of `u_X` is open in `X` (EGA IV₃, 11.3.1).

Let `x ∈ X` and set `s = π_X(x)`; then by EGA IV₂, 11.3.10 (combined with EGA IV₄, 17.5.1, resp. 17.6.1), `x` belongs to
`W_flat` (resp. `W_smooth`, `W_ét`) if and only if `u_s` is flat (resp. smooth, étale) at the point `x`, or, what comes
to the same by 1.3, if and only if `u_s` is flat (resp. smooth, étale).

Consequently, for "♭ = flat, smooth or étale", one has `U_♭ = ε_G⁻¹(W_♭)` and `W_♭ = π_X⁻¹(U_♭)`. Since `W_♭` is open
in `X`, hence in `G`, the first equality shows that `U_♭` is open in `S`.

<!-- original page 335 -->

The second assertion of (i) follows from what has just been seen, since then `Y = H`, `X = G`, and
`V_♭ = W_♭ = π_G⁻¹(U_♭)`.

Let us show assertion (ii). Let `V_l.t.f. ⊃ V_l.q.f.` be the open subsets of `G` formed by the points at which `u` is of
finite type (resp. quasi-finite). Set `X = V_l.t.f.` and denote by `u_X` the restriction of `u` to `X`. By hypothesis,
`X` contains `ε(S)`. Let `x ∈ X` and set `s = π_X(x)`.

If `u` is quasi-finite at `x`, then, by base change, `u_s` is quasi-finite at `x`, and so, since `G_s` is assumed
locally of finite type, `u_s` is locally quasi-finite by 1.3.1.

Conversely, if `u_s` is locally quasi-finite, then `u_X⁻¹(u_X(x)) ⊂ u_s⁻¹(u_s(x))` is a finite set. Since
`u_X : X → H` is locally of finite type, it follows from Chevalley's semicontinuity theorem (EGA IV₃, 13.1.3) that there
exists an open neighborhood `W` of `x` in `X` such that the fiber `u_X⁻¹(u_X(x′))` is discrete for every `x′ ∈ W`.
Hence, by EGA II, 6.2.2 (and EGA III₂, Err_III 20), `u_X` is quasi-finite at `x`.

Consequently, one has `U_l.q.f. = ε_G⁻¹(V_l.q.f.)` and `V_l.q.f. = π_X⁻¹(U_l.q.f.)`, and the first equality shows that
`U_l.q.f.` is open in `S`.

If moreover `G` is locally of finite type over `S`, then `X = G`, and so `V_l.q.f.` is the inverse image under `π_G` of
`U_l.q.f.`. This proves the first half of (ii).

Consider now the open subsets `V_l.p.f. ⊃ V_n.r.`, formed by the points where `u` is of finite presentation
(resp. unramified), and suppose that `Z = V_l.p.f.` contains the unit section of `G`. Let `z ∈ Z`; set `s = π_Z(z)` and
`h = u_Z(z)`.

If `u` is unramified at `z`, then, by base change, `u_s` is unramified at `z`, and so, since `G_s` is assumed locally of
finite type, `u_s` is unramified by 1.3.1.

Conversely, if `u_s` is unramified at the point `z`, then the fiber `u_s⁻¹(h) = u⁻¹(h)` is unramified over `κ(h)` at the
point `z`. Since `Z` is an open subset of `G`, the fiber `u_Z⁻¹(h) = u_s⁻¹(h) ∩ Z` is unramified over `κ(h)` at the
point `z`. Since `u_Z` is locally of finite presentation, this entails, by EGA IV₄, 17.4.1, that `u_Z` is unramified at
the point `z`.

One therefore has `U_n.r. = ε_G⁻¹(V_n.r.)` and `V_n.r. = π_Z⁻¹(U_n.r.)`, and the first equality shows that `U_n.r.` is
open in `S`.

If moreover `G` is locally of finite presentation over `S`, then `Z = G`, and so `V_n.r.` is the inverse image under
`π_G` of `U_n.r.`. This completes the proof of assertion (ii). ∎

**Corollary 2.6.** *Let `u : G → H` be a morphism of `S`-groups which is a radicial morphism (which is the case if `u`
is a monomorphism (EGA I, 3.5.4)). Suppose `G` (resp. `H`) locally of finite presentation and flat (resp. locally of
finite type) over `S`. Then the set `U` of `s ∈ S` such that `u_s` is an open immersion is open in `S`, and the
restriction of `u` over `U` is an open immersion.*

<!-- label: III.VI_B.2.6 -->

By 2.5 (i), the set `U′` of points `s ∈ S` such that `u_s` is étale is open in `S`. Since `u` is radicial, so is `u_s`,
for every `s ∈ S`, hence by EGA IV₄, 17.9.1, one has `U = U′`, which shows that `U` is open. Finally, by 2.5 (i), the
restriction of `u` over `U` is étale; since `u` is radicial, this restriction is an open immersion (EGA IV₄, 17.9.1). ∎

**Proposition 2.7.** *Let `G` be an `S`-group. The following conditions are equivalent:*

*(i) `G` is unramified over `S` at the points of the unit section,*

*(ii) the unit section is an open immersion,*

*(iii) `G` is of finite presentation over `S` at the points of the unit section, and for every `s ∈ S`, `G_s` is
unramified over `κ(s)`.*

*If, moreover, one assumes `G` locally of finite presentation over `S`, then each of the three preceding conditions is
equivalent to the following:*

*(iv) `G` is unramified over `S`.*

<!-- label: III.VI_B.2.7 -->

The equivalence of assertions (i) and (ii) follows from the more general Lemma 2.7.1 below. Note (1.3.1.1) that either
of conditions (i) or (iii) implies that, for every `s ∈ S`, `G_s` is locally of finite type over `κ(s)`. Then
(EGA IV₄, 17.4.1), assertion (i) is equivalent to the fact that, for every `s ∈ S`, `G_s` is unramified over `κ(s)` at
the point `e_s`, unit of `G_s`, or again (1.3.1), to the fact that `G_s` is unramified over `κ(s)`, so assertions (i)
and (iii) are equivalent. Finally, if `G` is locally of finite presentation over `S`, assertions (iii) and (iv) are
equivalent (EGA IV₄, 17.4.1). ∎

**Lemma 2.7.1.** *Let `G` be an `S`-scheme equipped with a section `ε`. In order that `G` be unramified over `S` at the
points of this section, it is necessary and sufficient that `ε` be an open immersion.*

<!-- label: III.VI_B.2.7.1 -->

The condition is necessary, by EGA IV₄, 17.4.1 a) ⇒ b″). Conversely, if `ε` is an open immersion, then the restriction
to `ε(S)` of the structural morphism `G → S` is an isomorphism, hence `G` is unramified over `S` at the points of
`ε(S)`. ∎

**Corollary 2.8.** *Let `u : G → H` be a morphism of `S`-groups. Suppose that, for every `s ∈ S`, `G_s` is locally of
finite type over `κ(s)`.*[^N.D.E-VI_B-21]

*a) If `u` is locally of finite type, the following conditions are equivalent:*

*(i) `u` is locally quasi-finite,*

*(ii) for every `s ∈ S`, `u_s : G_s → H_s` is locally quasi-finite,*

*(iii) `Ker u` is locally quasi-finite over `S`,*

*(iv) the fibers of `Ker u` are discrete.*

*b) If `u` is locally of finite presentation, the following conditions are equivalent:*

*(v) `u` is unramified,*

*(vi) for every `s ∈ S`, `u_s : G_s → H_s` is unramified,*

*(vii) `Ker u` is unramified,*

*(viii) the unit section `S → Ker u` is an open immersion.*

<!-- label: III.VI_B.2.8 -->

[^N.D.E-VI_B-21]: We have modified the presentation, separating the assertions relative to the "quasi-finite" case from those relative to the "unramified" case.

The equivalences (i) ⇔ (ii) and (v) ⇔ (vi) follow from 2.5 (ii), and Reminder 2.8.1 below shows that (i) ⇒ (iii) and
(v) ⇒ (vii).

<!-- original page 345 -->

For every `s ∈ S`, denote by `e_s` the unit element of `H_s`. Then (iii) (resp. (vii)) implies that, for every `s ∈ S`,

```text
(Ker u)_s = Ker u_s = u_s⁻¹(e_s)
```

is locally quasi-finite (resp. unramified) over `κ(s) = κ(e_s)`, hence `u_s` is quasi-finite (resp. unramified) at the
unit point of `G_s`, hence, by 1.3, `u_s` is locally quasi-finite (resp. unramified). So (iii) ⇒ (ii) and (vii) ⇒ (vi).
Finally, (ii) ⇔ (iv) by 1.4.1, and (vii) ⇔ (viii) by 2.7. ∎

**Reminder 2.8.1.** *Recall (cf. I 2.3.6.1) that, given a morphism `u : G → H` of `S`-groups, the* kernel *of `u`, denoted
`Ker u`, is the group subfunctor of `G` defined by setting, for any morphism `f : T → S`,*

```text
(Ker u)(T) = {a ∈ G(T) | u ∘ a = ε_H ∘ f}.
```

*By loc. cit. (or EGA I, 4.4.1), this functor is representable by the `S`-group `G ×_H S = u⁻¹(ε_H(S))`, simply denoted
`Ker u`. In particular, the structural morphism `Ker u → S` is deduced from `u` by base change.*

<!-- label: III.VI_B.2.8.1 -->

**Lemma 2.9.** *Let `π : X → S` be a morphism admitting an `S`-section `ε`.*

*(i) If `π` is injective, it is integral.*[^VI_B-2-9-i]

*(ii) If `π` is locally of finite type, and if, for every `s ∈ S`, `π_s` is an isomorphism, then `π` is an
isomorphism.*[^VI_B-2-9-ii]

<!-- label: III.VI_B.2.9 -->

[^VI_B-2-9-i]: This is also a particular case of EGA IV₄, 18.12.11, since `π` is evidently a universal homeomorphism.

[^VI_B-2-9-ii]: This is also an immediate consequence of EGA IV₄, 18.12.6.

Let us first note that, by Lemma 2.9.1 below, `π`, being a homeomorphism, is an affine morphism.

If `π` is injective, `ε` is surjective. Since `ε` is a surjective immersion, `ε(S)` is isomorphic to the closed
subscheme of `X` defined by a nil-ideal `I` of `O_X`. Since `ε` is an `S`-section of the morphism `π`, one has a direct
sum decomposition `O_X = O_S ⊕ I` of `O_S`-modules. Since `I` is a nil-ideal of `O_X`, `I` is evidently integral over
`O_S`, hence `O_X` is integral over `O_S`, and `π` is integral.

Suppose now that `π` is locally of finite type. Since `π ∘ ε = id_S`, `ε` is locally of finite presentation
(cf. EGA IV₁, 1.4.3 (v)), hence `I` is an ideal of finite type of `O_X` (EGA IV₁, 1.4.1). For every `s ∈ S`, one has
`O_{X_s} = κ(s) ⊕ I ⊗_{O_S} κ(s)`. By hypothesis, `ε_s` is an isomorphism, hence `I ⊗_{O_S} κ(s) = 0` for every
`s ∈ S`, hence a fortiori `I ⊗_{O_X} κ(x) = 0` for every `x ∈ X`, which implies, by Nakayama's lemma, that `I = 0`,
hence `π` is an isomorphism. ∎

**Lemma 2.9.1.** *Let `f : X → Y` be a morphism of schemes which is a homeomorphism; then `f` is an affine
morphism.*[^VI_B-2-9-1]

<!-- label: III.VI_B.2.9.1 -->

[^VI_B-2-9-1]: Cf. EGA IV₄, 18.12.7.1 for a slightly more general result, provable by the same proof.

It suffices to show that every point `y ∈ Y` has an open neighborhood `W` such that the restriction of `f` over `W` is
an affine morphism. So let `y ∈ Y`, and let `V` be an affine open neighborhood of `y` in `Y`. Let `V′ = f⁻¹(V)`. Then
`V′` is an open neighborhood of `x = f⁻¹(y)` in `X`. There exists an open affine neighborhood `W′` of `x` in `X`
contained in `V′`. Set then `W = f(W′)`. Then `W` is an open neighborhood of `y` in `Y` contained in the affine scheme
`V`, hence `W` is separated. Since `W′` is an affine scheme, the restriction of `f` over `W` is then an affine
morphism (EGA II, 1.2.3). ∎

**Corollary 2.10.** *Let `G` be an `S`-group locally of finite type. Suppose that, for every `s ∈ S`, `G_s` is the unit
`κ(s)`-group; then `G` is the unit `S`-group.*

<!-- label: III.VI_B.2.10 -->

More generally:

**Corollary 2.11.** *Let `f : X → Y` be an `S`-morphism locally of finite type. In order that `f` be a monomorphism, it
is necessary and sufficient that `f_s` be a monomorphism for every `s ∈ S`.*

<!-- label: III.VI_B.2.11 -->

It is clear that the condition is necessary; let us show that it is sufficient. If, for every `s ∈ S`, `f_s` is a
monomorphism, then a fortiori for every `y ∈ Y`, `f_y` is a monomorphism; we may therefore assume `Y = S`.

By EGA I, 5.3.8, to show that `f` is a monomorphism, it suffices to show that `Δ_f : X → X ×_S X` is an isomorphism, or,
what comes to the same, that the first projection `p : X ×_S X → X` is an isomorphism. But, if `f_s` is a monomorphism,
it likewise follows from EGA I, 5.3.8 that the first projection `X_s ×_{κ(s)} X_s → X_s` (which is identified with
`p_s`) is an isomorphism. Now `p` has the `S`-section `Δ_f`, hence Lemma 2.9 affirms that if for every `s ∈ S`, `p_s`
is an isomorphism, then so is `p`. ∎

**Corollary 2.12.** *Let `G` be an `S`-scheme having an `S`-section `ε` and such that the structural morphism
`π : G → S` is closed. Let `s ∈ S` be such that `π` is of finite presentation at the point `ε(s)` and that
`ε_s : Spec(κ(s)) → G_s` is an isomorphism (or, what comes to the same, that `π_s : G_s → Spec κ(s)` is an isomorphism).
Then there exists an open neighborhood `U` of `s` in `S` such that `ε|_U : U → G ×_S U` is an isomorphism.*

<!-- label: III.VI_B.2.12 -->

Let `V` be the set of points of `G` where `π` is unramified; it is known that `V` is open (cf. N.D.E. (6)) and contains
`ε(s)`. Hence `W = ε⁻¹(V)` is an open subset of `S` containing `s`, such that for every `t ∈ W`, `π` is unramified at
`ε(t)`. Since `π` is closed, so is `π|_W`, hence we may assume `W = S`.

Then, by 2.7.1, `X = G − ε(S)` is a closed subset of `G` not meeting `G_s`, hence, since `π` is closed, `F = π(X)` is a
closed subset of `S` not containing `s`; set `U = S − F`; then `U` is an open subset of `S` such that `ε|_U` is an
isomorphism of `U` onto `G|_U`. ∎

## 3. Neutral component of a group locally of finite presentation

<!-- label: III.VI_B.3 -->

### 3.0.

Given a part `A` (resp. `B`) of an `S`-scheme `X` (resp. `Y`), by abuse of notation, `A ×_S B` will denote the part of
`X ×_S Y` formed by the points whose first projection lies in `A` and second in `B`.

<!-- original page 347 -->

Given a part `A` of an `S`-group `G`, we shall say that `A` is *stable under the group law of `G`* if
`c(A) ⊂ A` and `µ(A ×_S A) ⊂ A`.

**Definition 3.1.** *Let `G` be an `S`-functor in groups satisfying the following condition:*

```text
(+)    for every s ∈ S, the functor G_s = G ⊗_S κ(s) is representable.
```

*One then denotes by `G⁰_s` the connected component of the unit element of the `κ(s)`-group
`G_s`.[^N.D.E-VI_B-22] One defines a sub-`S`-functor in groups of `G`, called the* neutral component *of `G`, denoted
`G⁰`, by setting, for every morphism `T → S`:*

```text
G⁰(T) = {u ∈ G(T) | ∀ s ∈ S, u_s(T_s) ⊂ G⁰_s}.
```

*One has thus defined the functor `G ↦ G⁰` from `(Sch/S)`-gr. to `(Sch/S)`-gr.*

<!-- label: III.VI_B.3.1 -->

[^N.D.E-VI_B-22]: This is a slightly abusive notation, but one which is compatible with the notations of (VI_A, 2.3) when this connected component is the underlying topological space of an open group subscheme `G⁰` of `G`, cf. (VI_A, 2.2.bis).

**Remark 3.2.** *(i) Let `G` be an `S`-functor in groups satisfying condition (+); then `Lie(G⁰/S) = Lie(G/S)`, by virtue
of Exposé II.[^N.D.E-VI_B-23] Indeed, for every `S`-scheme `T`, denote by `I_T` the `T`-scheme of dual numbers over `T`
and by `τ : T → I_T` the zero section (cf. II, 2.1). By definition, one has*

```text
Lie(G/S)(T) = {u ∈ G(I_T) | u ∘ τ = e},
```

*where `e : T → G` denotes the composition of `T → S` and the unit section `S → G`, and likewise*

```text
Lie(G⁰/S)(T) = {u ∈ G⁰(I_T) | u ∘ τ = e}
              = {u ∈ G(I_T) | u ∘ τ = e and u_s((I_T)_s) ⊂ G⁰_s, ∀ s ∈ S}.
```

*Now, for every `s ∈ S`, `T_s` and `(I_T)_s = I_{T_s}` have the same underlying set, hence if `u ∈ Lie(G/S)(T)`, one has
`u_s(I_{T_s}) = e_s`, where `e_s` denotes the unit point of `G_s`, whence `u ∈ Lie(G⁰/S)(T)`. So the inclusion
`Lie(G⁰/S)(T) ⊂ Lie(G/S)(T)` is an equality for every `T`, whence `Lie(G⁰/S) = Lie(G/S)`.*

*(ii) Let `G` and `G′` be two `S`-functors in groups satisfying (+); then:*

*a) if `G ⊂ G′`, then `G⁰ ⊂ G′⁰`,*

*b) if `G ⊂ G′` and `G′⁰ ⊂ G`, then `G⁰ = G′⁰`,*

*c) if for every `s ∈ S`, `G_s` is locally of finite type over `κ(s)`, then `G⁰` satisfies property (+), by (VI_A,
2.3), and one has `(G⁰)⁰ = G⁰`.*

<!-- label: III.VI_B.3.2 -->

[^N.D.E-VI_B-23]: We have added what follows.

**Proposition 3.3.** *Let `G` be an `S`-functor in groups satisfying condition (+) and let `S′` be an `S`-scheme. Then
`(G ×_S S′)⁰ = G⁰ ×_S S′`; in other words, the functor `G ↦ G⁰` commutes with base change, i.e. the following diagram is
commutative:*

```text
(Sch/S)-gr. ───── G ↦ G⁰ ────→ (Sch/S)-gr.
     │                              │
     ▼                              ▼
(Sch/S′)-gr. ─────────────────→ (Sch/S′)-gr.
```

<!-- label: III.VI_B.3.3 -->

<!-- original page 342 -->

It suffices indeed to check that, for every `s′ ∈ S′` with image `s` in `S`,
`((G ×_S S′) ⊗_{S′} κ(s′))⁰ = (G_s ⊗_{κ(s)} κ(s′))⁰` equals `G⁰_s ⊗_{κ(s)} κ(s′)`; this follows from (VI_A, 2.1.2). Note,
for later use in 4.2, that we have not used the group structure of `G_s`, only the fact that `G⁰_s` has a rational
point, namely `ε(s)`, hence is geometrically connected (see also EGA IV₂, 4.5.14). ∎

**Special case 3.4.** *Let `G` be an `S`-group scheme; denote by `G⁰` the subset of `G` equal to the union of the
`G⁰_s` as `s` runs through `S`. Then `G⁰` is a part of `G` stable under the group law of `G` (cf. 3.0), and for any
morphism `S′ → S` one has:*

```text
G⁰(S′) = {u ∈ G(S′) | u(S′) ⊂ G⁰}.
```

*When `G⁰` is an open part of `G`, it is clear that `G⁰` is representable by the subscheme of `G` induced on the open
`G⁰`.*

<!-- label: III.VI_B.3.4 -->

**Proposition 3.5.** *Let `S` be a quasi-compact and quasi-separated scheme, and `G` an `S`-group with fibers locally of
finite type. Then there exists a quasi-compact open subset `U` of `G` containing `G⁰`.*

<!-- label: III.VI_B.3.5 -->

The unit section `ε` being an immersion, `ε(S)` is a quasi-compact subspace of `G`, so there exists a quasi-compact open
subset `V` of `G` containing `ε(S)`. Since `S` is quasi-separated and `V` quasi-compact, `V` is quasi-compact over `S`
(EGA IV₁, 1.2.4), so `V ×_S V` is quasi-compact over `S`, hence quasi-compact. Then `V · V = µ(V ×_S V)` is
quasi-compact. Set `V_s = V ∩ G_s` and `V⁰_s = V ∩ G⁰_s`. Then `V⁰_s` is an open subset of `G⁰_s`, dense in `G⁰_s` since
`G⁰_s` is irreducible (VI_A, 2.4), so `V⁰_s · V⁰_s = G⁰_s` (VI_A, 0.5), which shows that `V_s · V_s ⊃ G⁰_s`, hence
`V · V ⊃ G⁰`. Finally, since `V · V` is quasi-compact, there exists a quasi-compact open subset `U` of `G` containing
`V · V` and a fortiori `G⁰`. ∎

**Corollary 3.6.** *Let `G` be an `S`-group with fibers locally of finite type and connected. Then `G` is quasi-compact
over `S`.*

<!-- label: III.VI_B.3.6 -->

<!-- original page 343 -->

Our assertion being local on `S` (EGA I, 6.6.1), one reduces to the case where `S` is affine. By 3.5, there then exists
a quasi-compact open `U` of `G` containing `G⁰ = G`, hence `G` is quasi-compact, hence quasi-compact over the affine
scheme `S` (EGA I, 6.6.4 (v)). ∎

**Proposition 3.7.** [^N.D.E-VI_B-24] *Let `G` be an `S`-group locally of finite presentation. Then:*

*(i) `G⁰` is ind-constructible in `G`.*

*(ii) If moreover `G` is quasi-separated over `S`, and `S` quasi-compact and quasi-separated, then `G⁰` is
constructible.*

*(iii) Consequently, if `G` is quasi-separated over `S`, `G⁰` is locally constructible.*

<!-- label: III.VI_B.3.7 -->

[^N.D.E-VI_B-24]: Recall the following definitions and results (cf. EGA 0_III, § 9.1 and EGA IV₁, §§ 1.8 and 1.9). Let `X` be a topological space. (i) An open `U` of `X` is called *retrocompact* if the inclusion `U ↪ X` is quasi-compact, i.e. if `U ∩ V` is quasi-compact for every quasi-compact open `V ⊂ X`. (ii) A part `C` of `X` is called *constructible* if it is a finite union of parts of the form `U − V`, where `U` and `V` are retrocompact opens in `X`. (iii) A part `L` of `X` is called *locally constructible* if for every `x ∈ X` there exists an open neighborhood `U` of `x` in `X` such that `L ∩ U` is constructible in `U`. (N.B. If `X` is quasi-compact and quasi-separated, `L` is then constructible.) (iv) A part `I` of `X` is called *ind-constructible* if for every `x ∈ X`, there exists an open neighborhood `U` of `x` in `X` such that `I ∩ U` is a union of parts locally constructible in `U`. Let now `f : X → Y` be a morphism of schemes. By Chevalley's constructibility theorem (cf. EGA IV₁, 1.8.4 and 1.9.5 (viii)), if `f` is of finite presentation (resp. locally of finite presentation), then the image under `f` of any locally constructible part is locally constructible (resp. ind-constructible).

*Proof.* Let us first show the first assertion. Since `π : G → S` is locally of finite presentation, given `s ∈ S`,
there exists an open subset `U` of `G` containing `ε(s)` and an open subset `V` of `S` containing `s` such that
`π(U) ⊂ V` and such that the morphism `π′ : U → V` deduced from `π` is of finite presentation. Then `T = ε⁻¹(U)` is an
open subset of `S` and if we let `W = π′⁻¹(T)` and `π″ = π′|_W`, then `π″ : W → T` is of finite presentation, and admits
as section the morphism `ε″ : T → W` deduced from `ε`.

For every `t ∈ T`, since `G⁰_t` is irreducible (VI_A, 2.4), `W ∩ G⁰_t` is dense in `G⁰_t`, hence irreducible, hence
connected: it is therefore the connected component of `π″⁻¹(t)` containing `ε″(t)`. It then follows from EGA IV₃, 9.7.12
that the union `W⁰` of the `W ∩ G⁰_t`, for `t ∈ T`, is locally constructible in `W`. On the other hand, it follows from
(VI_A, 0.5) that `G⁰ ∩ π⁻¹(T) = W⁰ · W⁰`, i.e. `G⁰ ∩ π⁻¹(T)` is the image of `W⁰ ×_T W⁰` under the morphism
`µ″ : W ×_T W → π⁻¹(T)` deduced from `µ`.[^N.D.E-VI_B-25] Since `W ×_T W` (resp. `π⁻¹(T)`) is of finite presentation
(resp. locally of finite presentation) over `T`, `µ″` is locally of finite presentation and quasi-separated, by
EGA IV₁, 1.4.3 and 1.2.2; if moreover `π⁻¹(T)` is quasi-separated over `T`, then `µ″` is quasi-compact (loc. cit.
1.2.4), hence of finite presentation. Since `W⁰ ×_T W⁰` is locally constructible in `W ×_T W` (since `W⁰` is in `W`), it
follows from Chevalley's constructibility theorem (loc. cit., 1.8.4 and 1.9.5 (viii)) that `G⁰ ∩ π⁻¹(T)` is
ind-constructible in `π⁻¹(T)`, and is locally constructible in `π⁻¹(T)` if `G` (and hence `π⁻¹(T)`) is quasi-separated
over `T`. This proves assertions (i) and (iii).

[^N.D.E-VI_B-25]: We have expanded the original in what follows.

<!-- original page 344 -->

Suppose now `G` quasi-separated over `S`, and `S` quasi-compact and quasi-separated. Then, by 3.5, there exists a
quasi-compact open `U` of `G` containing `G⁰`. Since `G` is quasi-separated over `S`, `G` is quasi-separated, so the
open `U` is retrocompact (EGA IV₁, 1.2.7), and it suffices to show that `G⁰` is constructible in `U` (EGA 0_III, 9.1.8).
Moreover, `U` being quasi-compact, hence quasi-compact over `S` (EGA IV₁, 1.2.4), and quasi-separated over `S`, the
restriction of `π` to `U` is of finite presentation, so by EGA IV₃, 9.7.12, `G⁰` is locally constructible in `U`, hence
constructible in `U`, since `U` is quasi-compact and quasi-separated (EGA IV₁, 1.8.1). This proves (ii), and it follows
that for every quasi-compact and quasi-separated open `T` of `S` (e.g., for every affine open of `S`), `G⁰ ∩ π⁻¹(T)` is
constructible. ∎

**Corollary 3.8.** *Let `S_0` be a quasi-compact and quasi-separated scheme, `I` a filtered increasing preordered set,
`(A_i)_{i ∈ I}` a direct system of commutative quasi-coherent `O_{S_0}`-algebras,
`A = lim A_i` (direct limit), `S_i = Spec A_i` for `i ∈ I`, and `S = Spec A` (cf. EGA II, 1.3.1).*

*Let `G` be an `S_0`-group scheme locally of finite presentation. Then the canonical map
`lim G⁰(S_i) → G⁰(S)` is bijective.*

<!-- label: III.VI_B.3.8 -->

Since `G` is locally of finite presentation over `S_0`, the canonical map `lim G(S_i) → G(S)` is bijective, by EGA IV₂,
8.14.2 c). It follows immediately that the canonical map `lim G⁰(S_i) → G⁰(S)` is injective. Let us show that it is
surjective. Let `g ∈ G⁰(S) ⊂ G(S)`. There exists `i ∈ I` such that `g` factors through `g_i ∈ G(S_i)` via `S → S_i`; by
hypothesis, `g⁻¹(G⁰) = S`. But, by 3.7, `G⁰` is ind-constructible in `G`, so `g_i⁻¹(G⁰)` is ind-constructible in `S_i`.
It then follows from EGA IV₂, 8.3.4, that there exists an index `j ≥ i` such that `g_j⁻¹(G⁰) = S_j`, where `g_j` is the
map deduced from `g_i` by the base change `S_j → S_i`. This shows that `g_j ∈ G⁰(S_j)`, hence that `g` comes from an
element of `lim G⁰(S_i)`. ∎

**Proposition 3.9.** *Let `G` be an `S`-group locally of finite presentation. Suppose that `G⁰` is representable; then
the canonical morphism `i : G⁰ → G` is an open immersion; moreover, `G⁰` is quasi-compact over `S`.*

<!-- label: III.VI_B.3.9 -->

Since `G⁰` is a subfunctor of the functor `G`, the morphism `i` is a monomorphism, hence radicial. By the definition of
the functor `G⁰`, one verifies immediately from the definition (EGA IV₄, 17.1.1) that `i` is a formally étale morphism
(noting that `G⁰` is the image of `i` in `G`). Finally, it follows from the characterization (EGA IV₃, 8.14.2 c)) of
`S`-schemes locally of finite presentation via the functor they represent, and from 3.8, that, since `G` is locally of
finite presentation over `S`, so is `G⁰`. Hence `i` is locally of finite presentation (cf. EGA IV₁, 1.4.3); it is
therefore a radicial étale morphism; hence an open immersion (EGA IV₄, 17.9.1).

Finally, the last assertion follows from 3.6. ∎

**Theorem 3.10.** *Let `G` be an `S`-group. The following conditions are equivalent:*

*(i) `G` is smooth over `S` at the points of the unit section.*

*(ii) `G` is flat and locally of finite presentation over `S` at the points of the unit section, and for every `s ∈ S`,
`G_s` is smooth over `κ(s)`.*

*(iii) There exists an open group subscheme `G′` of `G`, smooth over `S`.*

*(iv) `G⁰` is representable by an open subscheme of `G`, smooth over `S`.*

<!-- label: III.VI_B.3.10 -->

<!-- original page 351 -->

It is clear that (iv) ⇒ (iii) ⇒ (i) and, by 1.3.1 and 2.4, (i) implies (ii) and (iii). Moreover, (ii) ⇒ (i) by EGA IV₄,
17.5.1.

Let us show finally that (iii) implies (iv). Lemma 3.10.1 below shows that `G′` contains `G⁰`, and that `G′⁰ = G⁰`. It
therefore suffices to show that `G⁰` is open in `G`, since we have already seen (3.4) that `G⁰` will then be
representable by the smooth group subscheme induced by `G′` on the open `G′⁰ = G⁰`. We may therefore assume `G′ = G`.

To show that `G⁰` is open, it suffices to show that every `s ∈ S` has a neighborhood `T` in `S` such that
`G⁰ ∩ π⁻¹(T)` is open in `π⁻¹(T)`. Let `s ∈ S`. Since `G = G′`, `π` is locally of finite presentation, so one can
construct, as in the proof of 3.7, an open subset `T` of `S` containing `s`, and an open subset `W` of `G` containing
`ε(s)`, such that the morphism `π″ : W → T` deduced from `π` is of finite presentation and admits as section the
morphism `ε″ : T → W` deduced from `ε`. For every `t ∈ T`, `W ∩ G⁰_t` is then the connected component of `π″⁻¹(t)`
containing `ε″(t)`. Since `π` is smooth, so is `π″`, which is therefore smooth and of finite presentation. Then, by
EGA IV₃, 15.6.5, the union `W⁰` of the `W ∩ G⁰_t` for `t ∈ T` is open in `W`.

On the other hand, by (VI_A, 0.5), one has `W⁰ · W⁰ = G⁰ ∩ π⁻¹(T)`, and one must show that this is open in `π⁻¹(T)`. We
may therefore now assume `T = S`; it remains to show that `W⁰ · W⁰` is open in `G`. Since `π` is universally open, so is
`µ` (VI_A, 0.1). Hence, since `W⁰` is open in `G`, so is `W⁰ · W⁰ = µ(W⁰ ×_S W⁰)`.

This result will be improved in 4.4. ∎

**Lemma 3.10.1.** *Let `G` be an `S`-group with fibers locally of finite type. Then every open group subscheme `H` of
`G` contains `G⁰`, and satisfies `G⁰ = H⁰`.*

<!-- label: III.VI_B.3.10.1 -->

Let `s ∈ S`; set `G′_s = H_s ∩ G⁰_s`; then `G′_s` is an open subset of `G⁰_s`, which is dense in `G⁰_s` since `G⁰_s` is
irreducible (VI_A, 2.4), hence `G′_s · G′_s = G⁰_s` (VI_A, 0.5), which shows that
`G⁰_s = G′_s · G′_s ⊂ H_s · H_s = H_s`. One thus has `G⁰_s = H⁰_s` for every `s`, whence `G⁰ ⊂ H` and `G⁰ = H⁰`. ∎

**Proposition 3.11.** *Let `u : G → H` be a morphism between `S`-groups locally of finite presentation. If `u` is flat,
the map `u⁰ : G⁰ → H⁰` deduced from `u` is surjective; the converse is true if `G` is flat over `S` and `H` has reduced
fibers.*[^N.D.E-VI_B-26]

<!-- label: III.VI_B.3.11 -->

[^N.D.E-VI_B-26]: Compare with (VI_A, 5.6).

[^N.D.E-VI_B-27] Suppose `u` flat; then for every `s ∈ S`, `u_s` is flat and locally of finite presentation, hence open
(EGA IV₂, 2.4.6), so the morphism `u⁰_s : G⁰_s → H⁰_s` is surjective by 1.3.2. Hence the map `u⁰ : G⁰ → H⁰` is
surjective.

Conversely, suppose the map `u⁰ : G⁰ → H⁰` is surjective, `G` flat over `S` and `H` with reduced fibers. Then, for
every `s ∈ S`, the morphism `u⁰_s : G⁰_s → H⁰_s` is surjective, hence flat at every point above the generic point `η`
of `H⁰_s` (since `O_{H⁰_s, η}` is a field), hence `u_s` is flat by 1.3. Hence `u` is flat, by the fiber-wise flatness
criterion (EGA IV₃, 11.3.11). ∎

[^N.D.E-VI_B-27]: We have shortened the original, referring here to 1.3.2. We have also simplified the argument below by removing a reference to the generic flatness theorem (EGA IV₂, 6.9.1), which is not necessary here.

## 4. Dimension of fibers of groups locally of finite presentation

<!-- label: III.VI_B.4 -->

**Proposition 4.1.** *Let `G` be an `S`-scheme locally of finite type, equipped with an `S`-section `ε`, and such that
for every `s ∈ S`, one has `dim G_s = dim_{ε(s)} G_s` (which is the case if `G` is an `S`-group (1.5)).*

*(i) The function `s ↦ dim G_s` is upper semicontinuous on `S`.*

*(ii) If, moreover, `G` is locally of finite presentation over `S`, this function is locally constructible.*

<!-- label: III.VI_B.4.1 -->

Let `π : G → S` be the structural morphism. Chevalley's semicontinuity theorem (EGA IV₃, 13.1.3) asserts that the
function `x ↦ dim_x π⁻¹(π(x))` is upper semicontinuous on `G`. Now, for every `s ∈ S`, one has

```text
dim G_s = dim π⁻¹(s) = dim_{ε(s)} π⁻¹(π(ε(s)));
```

and since the function `s ↦ ε(s)` is continuous on `S`, the composite function `s ↦ dim G_s` is upper semicontinuous on
`S`.

<!-- original page 348 -->

Suppose `G` locally of finite presentation over `S`. To show that the function `s ↦ dim G_s` is locally constructible,
one sees, reasoning as above, that it suffices to show that the function `x ↦ dim_x π⁻¹(π(x))` is locally constructible
on `G`, which follows from EGA IV₃, 9.9.1. ∎

**Proposition 4.2.** *Let `π : G → S` be an `S`-scheme locally of finite presentation, equipped with an `S`-section `ε`
and satisfying the following two conditions (which are satisfied if `G` is an `S`-group, by 1.5 and (VI_A, 2.4.1)):*

*a) For every `s ∈ S` and every `x ∈ G_s`, one has `dim G_s = dim_x G_s` (or, what comes to the same (1.5), for every
`s ∈ S`, all irreducible components of `G_s` have the same dimension).*

*b) For every `s ∈ S`, if one denotes by `G⁰_s` the connected component of `G_s` containing `ε(s)`, `G⁰_s` is
geometrically irreducible.*

*Let `s ∈ S`. The following conditions are equivalent:*

*(i) `G` is universally open over `S` at the points of `G⁰_s`.*

*(i bis) `G` is universally open over `S` at every point of a neighborhood of `ε(s)` in
`G⁰_s`.*[^N.D.E-VI_B-28]

*(ii) The function `t ↦ dim G_t` is constant in a neighborhood of `s` in `S`.*

*(iii) `G⁰` is "universally open over `S` at the points of `G⁰_s`", i.e., given `S′ → S`, `s′ ∈ S′_s`, `g ∈ G⁰_{s′}` and
`V` an open neighborhood of `g` in `G′ = G_{S′}`, then `π(V ∩ G′⁰)` is an open neighborhood of `s′` in
`S′`.*[^N.D.E-VI_B-29]

<!-- label: III.VI_B.4.2 -->

[^N.D.E-VI_B-28]: One finds in the original: "at the points of `ε(s)`"; it is not sufficient to assume that `G` is universally open over `S` at `ε(s)`, as shown by the example given in N.D.E. (19). We have corrected the proof accordingly.

[^N.D.E-VI_B-29]: We have added condition (iii), pointed out by O. Gabber; it will be useful later (5.7).

*Proof.* Clearly (i) ⇒ (i bis). By EGA IV₃, 14.3.3.1 (ii), the set of points of `G⁰_s` where `π_G` is universally open
is closed in `G⁰_s`. Hence, since `G⁰_s` is irreducible, one has (i bis) ⇒ (i).

Let us show that (i) implies (ii). Let `T` be the set of `t ∈ S` such that `dim G_t = dim G_s`. By 4.1, `T` is locally
constructible, hence, by EGA IV₁, 1.10.1, to show that `T` is a neighborhood of `s`, it suffices to show that every
generization `s′` of `s` belongs to `T`.

<!-- original page 349 -->

Let `x` be the generic point of `G⁰_s` and `U` an open subset of `G` containing `x`. Since `π_G` is universally open at
`ξ`, by EGA IV₃, 14.3.13, for every generization `s′` of `s`, one has `dim(U ∩ G_{s′}) ≥ dim_x(U ∩ G_s)`. Taking
hypothesis a) into account, this entails `dim G_{s′} ≥ dim G_s`. Since the function `s ↦ dim G_s` is upper
semicontinuous by 4.1, one also has `dim G_{s′} ≤ dim G_s`, whence `s′ ∈ T`. This proves that (i) ⇒ (ii).

It is clear that (iii) ⇒ (i); let us show that (ii) ⇒ (iii). Since the dimension of fibers is unchanged by extension of
the base field, and the formation of `G⁰` commutes with base change (cf. the proof of 3.3), one may assume `S′ = S` and
`s′ = s`. Moreover, since every open `V` of `G` meeting `G⁰_s` contains the generic point `η` of `G⁰_s`, one may assume
`g = η`.

One may further assume `S` affine. Let `U` be an affine open neighborhood of `ε(s)`; it is then of finite presentation
over `S`. Replacing `S` by `ε⁻¹(U)` and then `U` by `U ∩ π⁻¹(S)`, we reduce to the case where `π : U → S` is of finite
presentation and admits `ε : S → U` as section. Then, by EGA IV₃, 9.7.12, `G⁰ ∩ U` is constructible in `U`. Then,
replacing `V` by an affine open contained in `V ∩ U`, we obtain that `G⁰ ∩ V` is constructible in `V`. Since
`π : V → S` is of finite presentation, `π(G⁰ ∩ V)` is locally constructible in `S`, by Chevalley's constructibility
theorem (cf. EGA IV₁, 1.8.4).

Hence, by loc. cit., 1.10.1, to show that `π(G⁰ ∩ V)` is an open neighborhood of `s`, it suffices to show that for
every generization `t` of `s`, there exists a generization `ξ` of `η` belonging to `G⁰` (and hence to `G⁰ ∩ V`). Now
the generic point `ξ` of `G⁰_t` is a generization of `η`. Indeed, `ε(s)` belongs to the closure `X` of `{ξ}` in `G`, so
by Chevalley's semicontinuity theorem (cf. EGA IV₃, 13.1.3), one has `dim_{ε(s)} X_s ≥ dim_ξ X_t`; on the other hand,
hypothesis (ii) entails that `dim_ξ G⁰_t = dim_{ε(s)} G_s`. It follows that one of the irreducible components of `X_s`
containing `ε(s)` equals `G⁰_s`, whence `η ∈ {ξ}⁻`. This proves that (ii) ⇒ (iii), which proves the proposition. ∎

[^N.D.E-VI_B-30] One can also prove the implication (ii) ⇒ (i) as follows. Since `π` is locally of finite presentation,
there exists an open subset `U` of `G` containing `ε(s)` and an open subset `V` of `S` containing `s` such that
`π(U) ⊂ V` and such that the morphism `π′ : U → V` deduced from `π` is of finite presentation. Set then `T = ε⁻¹(U)`
and `W = π′⁻¹(T) = U ∩ π⁻¹(T)`. Then the morphism `π″ : W → T` deduced from `π′` is of finite presentation and admits as
section the morphism `ε″ : T → W` deduced from `ε`. Moreover, for every `t ∈ T`, `G⁰_t` being irreducible, `W ∩ G⁰_t`
is dense in `G⁰_t`, hence irreducible, hence connected: so it is the connected component of `π″⁻¹(t)` containing
`ε″(t)`.

[^N.D.E-VI_B-30]: The preceding has been communicated to us by O. Gabber; we have also preserved the proof of the implication (ii) ⇒ (i) given in the original.

<!-- original page 354 -->

Since `W ∩ G⁰_t` is a dense open subset of `G⁰_t`, one has, by 1.5 and EGA IV₂, 5.2.1,
`dim(W ∩ G⁰_t) = dim G⁰_t = dim G_t`, so the function `t ↦ dim W ∩ G⁰_t` is constant in a neighborhood of `s` in `T`.
Let us show finally that, for every `t ∈ T`, `W ∩ G⁰_t` is geometrically irreducible. Let `K` be an extension of
`κ(t)`; then `(W ∩ G⁰_t) ⊗_{κ(t)} K = (W ⊗_{κ(t)} K) ∩ (G⁰_t ⊗_{κ(t)} K)` is a non-empty open subset of
`G⁰_t ⊗_{κ(t)} K`, hence is irreducible since `G⁰_t ⊗_{κ(t)} K` is.

We are then in the conditions of application of EGA IV₃, 15.6.6 (ii), which asserts that `π″` (hence `π`) is universally
open at the points of `W ∩ G⁰_s`. But, by EGA IV₃, 14.3.3.1 (ii), the subset of `G_s` formed by the points where `π`
is universally open is closed in `G_s`; since it contains `W ∩ G⁰_s`, it therefore contains its closure `G⁰_s`. ∎

<!-- original page 350 -->

**Corollary 4.3.** *Let `G` be a flat `S`-group locally of finite presentation. Then the function `s ↦ dim G_s` is
locally constant on `S`.*

<!-- label: III.VI_B.4.3 -->

This follows immediately from 4.2, since every flat morphism locally of finite presentation is universally open
(EGA IV₂, 2.4.6). ∎

**Corollary 4.4.** *Let `G` be an `S`-group locally of finite presentation over `S` at the points of the unit section.
Consider the conditions:*

*(i) `G` is smooth over `S` at the points of the unit section (cf. 3.10).*

*(ii) For every `s ∈ S`, `G_s` is smooth over `κ(s)`, and the function `s ↦ dim G_s` is locally constant on `S`.*

*(iii) For every `s ∈ S`, `G_s` is smooth over `κ(s)`, and there exists a neighborhood `V` of the unit section such that
`π_V : V → S` is universally open.*

*(iv) For every `s ∈ S`, `G⁰_s` is smooth over `κ(s)`, and `G⁰` is representable by an open group subscheme of `G`,
universally open over `S`.*

*Then one has the following implications: (i) ⇒ (ii) ⇔ (iii) ⇔ (iv).*

*If one further assumes `S` reduced, then conditions (i) to (iv) are equivalent, and imply that `G⁰` is smooth over
`S`.*[^N.D.E-VI_B-31]

<!-- label: III.VI_B.4.4 -->

[^N.D.E-VI_B-31]: One cannot do without the hypothesis that `S` is reduced here: if `k` is a field, `S = Spec A`, where `A = k[δ]` with `δ² = 0`, and `G` the closed subgroup `Spec A[X]/(δX)` of `G_{a,S}` (which to every `A`-algebra `R` associates the subgroup of `r ∈ R` such that `δr = 0`), then `G` is an `S`-group satisfying (ii)–(iv), but is not flat, hence not smooth, over `S`.

*Proof.* Let us show that (i) implies (ii). For every `x ∈ G`, one has `dim_x π⁻¹(π(x)) = dim π⁻¹(π(x))`, by 1.5.
Consequently, by EGA IV₄, 17.10.2, the function

```text
x ↦ dim_x π⁻¹(π(x)) = dim π⁻¹(π(x))
```

is continuous in a neighborhood of the unit section; so the function `s ↦ dim G_s` is continuous on `S`, hence locally
constant on `S`. Moreover, for every `s ∈ S`, `G_s` is smooth over `κ(s)` by 1.3.1.

<!-- original page 355 -->

Let us show that (ii) implies (iv). It suffices to show that `G⁰` is open in `G`, for then, by 3.4, `G⁰` will be
representable by the group subscheme induced on `G⁰`, and the properties of `G⁰` cited in the statement will follow from
2.4 and 4.2. Given `s ∈ S`, construct as in the proof of 3.10, `W`, `T`, `π″`, `ε″`, and `W⁰`. Then, by
EGA IV₃, 15.6.7, `W⁰` is open in `W`. On the other hand, under hypothesis 4.4 (ii), it follows from 4.2 that `π` is
universally open at every point of `W⁰`, hence (VI_A, 0.1) `µ` is universally open at every point of `W⁰ ×_S W⁰`,
which shows that `W⁰ · W⁰` is open, and one concludes as in the proof of Theorem 3.10.

It is clear that (iv) ⇒ (iii), and (iii) ⇒ (ii) follows from 4.2 applied to `V`.

Finally, suppose (ii)–(iv) hold and let us show that `G⁰` is smooth over `S` if `S` is reduced.[^N.D.E-VI_B-32] For this,
one may assume `G = G⁰`. Then `G` is of finite presentation over `S` by virtue of 5.5 below. Thus, `π_G` is of finite
presentation, with geometrically integral fibers, of locally constant dimension on `S`. Then, by EGA IV₃, 15.6.7, the
morphism `G ×_S S_red → S_red` deduced from `π_G` is flat, hence `π_G` is flat if `S` is reduced. In this case,
`G = G⁰` is smooth over `S`, by Theorem 3.10. ∎

[^N.D.E-VI_B-32]: We have expanded the original in what follows.

## 5. Separation of groups and homogeneous spaces

<!-- label: III.VI_B.5 -->

**Proposition 5.1.** *In order that an `S`-group `G` be separated, it is necessary and sufficient that the unit section
of `G` be a closed immersion.*

<!-- label: III.VI_B.5.1 -->

The condition is necessary (EGA I, 5.4.6); it is sufficient by virtue of the following cartesian diagram (cf.
(VI_A, 0.3)):

```text
              µ ∘ (id_G × c)
G ×_S G ─────────────────────→ G
   │                            ▲
   │ Δ_{G/S}                    │ ε
   ▼                            │
   G ──────────────────────→ S.
              π
```

**Proposition 5.2.** *If `S` is discrete, every `S`-group is separated.*

<!-- label: III.VI_B.5.2 -->

Indeed, `S` is then equal to `∐_{s ∈ S} Spec O_{S,s}`, and by EGA I, 5.5.5, it suffices to show that for every
`s ∈ S`, `G ×_S Spec O_{S,s}` is separated, which follows from (VI_A, 0.3), since `O_{S,s}` is a local ring of dimension
0.[^N.D.E-VI_B-33]

[^N.D.E-VI_B-33]: We have replaced "Artinian" by "of dimension 0" (and mentioned this generalization in (VI_A, 0.3)).

<!-- original page 352 -->

**Theorem 5.3.** *Let `S` be a scheme, `G` an `S`-group scheme locally of finite presentation over `S` and universally
open over `S` in a neighborhood of the unit section, `X` an `S`-scheme on which `G` acts in such a way that the
morphism:*

```text
Φ : G ×_S X ─→ X ×_S X,    (g, x) ↦ (gx, x)
```

*is surjective. Suppose moreover that, for every `s ∈ S`:*

*(i) there exists an open subscheme `U` of `X`, separated over `S`, such that `U_s` is dense in `X_s`,*

*(ii) the fiber `X_s` is locally of finite type over `κ(s)`.*[^N.D.E-VI_B-34]

*Then `X` is separated over `S`.*

<!-- label: III.VI_B.5.3 -->

[^N.D.E-VI_B-34]: We have corrected the original by assuming `G` universally open over `S` in a neighborhood of the unit section and by adding hypothesis (ii); see below for examples, due to O. Gabber, showing that statements 5.3 and 5.4 of the original are false without additional hypotheses. On the other hand, we note that Thm. 5.3 is a reworked version of Thm. 5.3A below, which appears in the 1965 edition of SGAD, and is due to M. Raynaud, cf. the Notes (∗) in Exp. X, 8.5 and 8.8.

**Corollary 5.4.** *Let `S`, `G`, `X` be as in the preliminary hypotheses of 5.3. Suppose moreover that `X` has fibers
locally of finite type and connected. Then:*

*(i) `X` is separated over `S`.*

*(ii) If there exists an open subset `V` of `X`, quasi-compact over `S` and meeting every non-empty fiber
`X_s`,[^N.D.E-VI_B-35] then `X` is quasi-compact over `S`.*

<!-- label: III.VI_B.5.4 -->

[^N.D.E-VI_B-35]: Without this hypothesis, one has the following counterexample, pointed out by O. Gabber: let `G = S` be a local scheme with closed point `s`, such that `S* = S − {s}` is not quasi-compact, and `X` the disjoint union of `{s}` and `S*`.

*Proof.* (i) Indeed, let `s ∈ S` be such that `X_s ≠ ∅`. Since the morphism
`Φ_s : G_s ×_{κ(s)} X_s → X_s ×_{κ(s)} X_s` deduced from `Φ` by base change is surjective, and `X_s` is connected, `X_s`
is irreducible by (VI_A, 2.5.4). Hence, if `U` is an affine open of `X` such that `U_s` is non-empty, `U_s` is dense in
`X_s`, and the theorem applies.

To prove (ii), one may assume `S` affine. Then `V` is quasi-compact and, by 3.5, there exists a quasi-compact open `U`
of `G` containing `G⁰`. Let `s ∈ S` be such that `X_s ≠ ∅`. Then `X_s` is irreducible (VI_A, 2.6.6) and so, since `U_s`
contains `G⁰_s`, the morphism `U_s ×_{κ(s)} V_s → X_s`, `(g, x) ↦ gx`, is surjective (VI_A, 2.6.4). Consequently, the
morphism `U ×_S V → X` is surjective, and so `X` is quasi-compact (since `U` and `V` are); as we assumed `S` affine,
hence separated, it follows that `X` is quasi-compact over `S` (cf. EGA I, 6.6.4 (v)). ∎

**Remark 5.4.1.** [^N.D.E-VI_B-36] *We shall see in the course of the proof that the conclusion of Theorem 5.3 holds if
one makes only the hypothesis: (i′) there exists an open subscheme `U` of `X`, separated over `S`, such that `U_s` is
dense in every irreducible component of `X_s`. (The latter is a consequence of (i) if `X_s` has locally a finite number
of irreducible components, which is the case under hypothesis (ii).) On the other hand, we shall see later that 5.4
is also valid under the hypothesis that each fiber `X_s` is quasi-separated and connected.*

<!-- label: III.VI_B.5.4.1 -->

[^N.D.E-VI_B-36]: We have added this remark, cf. N.D.E. (34).

**Theorem 5.3A (Raynaud).** *Let `G` be an `S`-group locally of finite presentation, universally open over `S`, and
with connected fibers. Then `G` is separated over `S`. More generally, any `S`-scheme `X` locally of finite presentation
over `S`, equipped with an action of `G` such that the morphism `Φ : G ×_S X → X ×_S X`, `(g, x) ↦ (gx, x)` is
surjective, is separated over `S`.*

<!-- label: III.VI_B.5.3.A -->

<!-- original page 357 -->

**Corollary 5.5.** *Let `S` be a scheme, `G` an `S`-group scheme, locally of finite presentation, with connected fibers,
and universally open over `S`. Then `G` is separated and of finite presentation over `S`.*[^N.D.E-VI_B-37]

<!-- label: III.VI_B.5.5 -->

[^N.D.E-VI_B-37]: Let us point out here the following result ([Ray70a], VI 2.5): if `S` is normal, `G` smooth with connected fibers, and if `X` is a (fppf) homogeneous `G`-space (i.e. the morphisms `X → S` and `G ×_S X → X ×_S X` are covering for the (fppf) topology), locally of finite type over `S`, then `X` is locally quasi-projective over `S`. In particular, `G` is quasi-projective over `S`. See also N.D.E. (35) in VI_A.

Indeed, by 3.6 and 5.4, `G` is quasi-compact and separated over `S`, and since `G` is locally of finite presentation
over `S`, it is therefore of finite presentation over `S`. ∎

### 5.6. Proof of Theorem 5.3.

Before establishing 5.3, let us prove a few lemmas.

**Lemma 5.6.0.** [^N.D.E-VI_B-38] *(i) Let `A ⊂ B` be integral rings, with `B` integral over `A`, and let `q ∈ Spec(B)`
be such that `A` is unibranch at the point `p = q ∩ A`. Then the morphism `π : Spec(B) → Spec(A)` is open at the point
`q`.*

*(ii) Let `X`, `Y` be two irreducible preschemes, `f : X → Y` a dominant morphism, `x` a point of `X` such that `f` is
quasi-finite at `x` and `y = f(x)` is a unibranch point of `Y`. Then `f` is open at the point `x`. In particular, if
`Y = Spec(O_{Y,y})` is a local prescheme with closed point `y`, then `f(U) = Y` for every neighborhood `U` of `x`.*

<!-- label: III.VI_B.5.6.0 -->

[^N.D.E-VI_B-38]: We have added this lemma, communicated by O. Gabber, which improves EGA IV₃, 14.4.1.2 and corrects the proof of loc. cit., 14.4.1.3 without modifying its hypotheses (compare with the erratum (Err_IV, 38) in EGA IV₄).

*Proof.* (i) Let `K` (resp. `L`) be the fraction field of `A` (resp. `B`), `A′` the normalization of `A`, and `B′` the
subring of `L` generated by `A′` and `B`. Then `B′` is integral over `A′`. Set `Y = Spec(A)`, `X = Spec(B)`,
`Y′ = Spec(A′)`, `X′ = Spec(B′)`, so that one has a commutative diagram

```text
X′ ───── π′ ────→ Y′
│                  │
│                  │ φ
▼                  ▼
X ────── π ────→ Y
```

in which all morphisms are integral and surjective.

Since `A` is unibranch at `p`, `Y′` has a unique point `p′` above `p`; consequently, if `U` is an open neighborhood of
`p′` in `Y′`, then `φ(Y′ − U)` is a closed subset not containing `p`, so that the complementary open is contained in
`φ(U)`. This shows that `φ : Y′ → Y` is open at `p′`, and so it suffices to show that `π′` is open. We are thus reduced
to the case where `A = A′` is normal.

Let `N` be a quasi-Galois extension of `K` containing `L`, let `X̃ = Spec(B̃)`, where `B̃` is the integral closure of `B`
in `N`, and let `Γ = Aut(N/K)`. Since `X̃ → X` is surjective, it suffices to show that `π̃ : X̃ → Y` is open. Let `U` be
an open of `X̃` and `U′ = ⋃_{g ∈ Γ} gU`. Since `Γ` acts transitively on the fibers of `X̃ → Y` (cf. [BAC], Chap. V,
§ 2.3, Prop. 6), `π̃(U)` equals `π̃(U′)`, and the latter equals the complementary open of the closed `π̃(X̃ − U′)`. This
proves (i).

<!-- original page 358 -->

(ii) One may assume `Y` and `X` reduced. By Zariski's "Main Theorem" (cf. EGA IV₃, 8.12.9), there exist affine open
neighborhoods `U` of `x`, and `V = Spec(A)` of `y`, such that `f(U) ⊂ V`, and a factorization:

```text
       j
U ─────────→ V′
│            │
│ f          │ u
▼            ▼
            V,
```

where `j` is an open immersion and `u` is finite. Replacing `V′` by the closure of `j(U)`, one may assume `V′`
irreducible, hence `V′ = Spec(B)`, where `B` is an integral `A`-algebra, finite over `A`. Moreover, since `f` is
dominant, so is `u`, so that the morphism `A → B` is injective. Since, by hypothesis, `A` is unibranch at the point
`y`, it follows from (i) that `u` is open at the point `j(x)`, and hence `f = u ∘ j` is open at the point `x`. This
proves the first assertion of (ii). The second follows, since if `Y` is a local prescheme with closed point `y`, every
open containing `y` equals `Y`. (In the case where `Y = Spec(O_{Y,y})`, one may also use, instead of EGA IV₃, 8.12.9,
the local form of Zariski's Main Theorem, which one finds, e.g., in [Pes66], or [Ray70b], Ch. IV, Th. 1.) ∎

**Lemma 5.6.1.0.** [^N.D.E-VI_B-39] *Let `f : X → S` be a morphism locally of finite presentation, `s ∈ S`, and
`x ∈ X_s`. Let `n = dim_x(X_s)` and let `q` be the structural morphism `A^n_S → S`.*

*Suppose given a morphism `u : X → A^n_S` quasi-finite such that `f = q ∘ u`, and suppose `f` universally open at the
generic point `z` of an irreducible component `z` of `X_s`, containing `x` and of dimension `n`. Then `u` is universally
open at the point `x ∈ X`.*

<!-- label: III.VI_B.5.6.1.0 -->

[^N.D.E-VI_B-39]: We have made this lemma explicit, used in the proof of Lemma 5.6.1.

Let us note first that: (†) the hypotheses are preserved by any base change `π : S′ → S` covering `s` (i.e., such that
`π⁻¹(s) ≠ ∅`). Indeed, let `S′ → S` be such a morphism, let

```text
       u′
X′ ─────────→ A^n_{S′}
│              │
│ f′           │ q′
▼              ▼
             S′
```

be the diagram obtained by base change, and let `s′` be a point of `S′` above `s` and `x′` a point of `X′_{s′}` above
`x`. Since `X′_{s′} = X_s ⊗_{κ(s)} κ(s′)`, by lifting of generizations and invariance of dimension under field
extension (EGA IV₂, 2.3.4 (i) and 4.1.4), `x′` is contained in an irreducible component `z′` of `X′_{s′}` whose generic
point `z′` lies above `z`, and one has `n ≤ dim z′ ≤ dim_{x′} X′_{s′} ≤ n`, whence `dim z′ = n = dim_{x′} X′_{s′}`.
Since `f` is universally open at `x`, `f′` is universally open at `x′`.

Set `Y = A^n_S`. By EGA IV₃, 14.3.3.1 (i), to prove that `u` is universally open at `x`, it suffices to prove that, for
every integer `r ≥ 0` and every point `x′` of

<!-- original page 359 -->

`X′ = X[T_1, …, T_r]` above `x`, the morphism `u′ : X′ → Y′ = A^n_S[T_1, …, T_r]` is open at the point `x′`. Now, with
`S′ = S[T_1, …, T_r]` and `q′` the projection `Y′ ≅ A^n_{S′} → S′`, one is in the situation obtained by the base change
`S′ → S`. So, by what precedes, one is reduced to showing that `u` is open at the point `x`.

Set `y = u(x)`. Since `u` is locally of finite presentation (since `f` and `q` are, cf. EGA IV₁, 1.4.3), then by
EGA IV₁, 1.10.3, it suffices to show that `u(Spec O_{X,x}) = Spec(O_{Y,y})`. For this, one may assume `S` affine and
integral. Let then `π : S′ → S` be its normalization; denote by `u′ : X′ → Y′` the morphism deduced from `u` by base
change. Since the morphism `π_Y : Y′ → Y` is integral and surjective, one has

```text
Spec(O_{Y,y}) = ⋃_{y′} π_Y(Spec(O_{Y′, y′})),
```

the union being taken over all points of `Y′` above `y`; it therefore suffices to show that, for each such `y′`, and
every `x′ ∈ X′_{y′}` above `x`, one has `u′(Spec O_{X′, x′}) = Spec O_{Y′, y′}`. As the hypotheses are preserved by the
base change `π : S′ → S`, one is thus reduced to the case of `S′`, i.e., one may assume `S` integral and normal.

Now, the hypotheses on `f` imply, by EGA IV₃, 14.3.13, that there exists an irreducible component `Z` of `X` containing
`z` (and hence `x`), dominating `S` and such that

```text
dim_z(Z_s) = n = dim(Z_η),
```

where `η` is the generic point of `S`. Let `ξ` be the generic point of `Z`. Since `u`, and hence also
`u_η : Z_η → A^n_η`, is quasi-finite, the closure in `A^n_η` of the point `u_η(ξ) = u(ξ)` is of dimension `n`, hence
`u(ξ)` is the generic point of `A^n_η`, which is also the generic point of `Y = A^n_S`. Consequently, denoting by `g`
the restriction of `u` to `Z`, the morphism `g : Z → Y` is quasi-finite and dominant. Since `Y` is normal, it follows
from Lemma 5.6.0 that `g` is open, so that `u` is open at every point of `Z`, in particular at the point `x`.
Consequently, `u(Spec O_{X,x}) = Spec O_{Y,y}`, and this completes the proof of Lemma 5.6.1.0. ∎

The following lemma advantageously replaces EGA IV₃, 14.5.10,[^N.D.E-VI_B-40] in that it is independent of noetherian
hypotheses.

[^N.D.E-VI_B-40]: We have corrected the original, which indicated 19.5.10.

**Lemma 5.6.1.** *Let `S` be a scheme, `f : X → S` an `S`-scheme locally of finite presentation, `s` a point of `S`,
`x` a closed point of `X_s`. Suppose that `f` is universally open at the generic point `z` of an irreducible component
`z` of `X_s`, containing `x` and such that `dim_x(X_s) = dim z`. Then there exists a commutative diagram:*

```text
            f
X ──────────────→ S
▲                ▲
│ h              │ w
│        φ       │
│ ↘            ↗
S″ ─────────→ S′
            π
```

*where `S′` is an affine scheme, `w` an étale morphism, `π` a finite surjective morphism, of finite presentation, and
`φ⁻¹(s)` is formed of a single point `s″`, such that `h(s″) = x` and `κ(s″) = κ(x)`.*[^N.D.E-VI_B-41]

<!-- label: III.VI_B.5.6.1 -->

[^N.D.E-VI_B-41]: Consequently, `h` induces a section `σ` of `X ×_S S″ → S″` such that `σ(s″)` lies above `x`; compare with EGA IV₃, 14.5.10.

<!-- original page 360 -->

*Proof.* First, one may assume `S = Spec A` and `X = Spec B`, where `B` is an `A`-algebra of finite presentation. Let
`p` and `q` be the prime ideals of `A` and `B` corresponding to `s` and `x`, respectively, so that `p = A ∩ q`. Set
`n = dim_x X_s`, and let `t_1, …, t_n` be elements of `B` whose images in `O_{X_s, x} = B_q / p B_q` form a system of
parameters. Then `O_{X_s, x}/(t_1, …, t_n)` is of finite dimension over `κ(x)` and hence also over `κ(s)`, since `x` is
a closed point of the `κ(s)`-algebraic scheme `X_s`. Consequently, the `S`-morphism

```text
u : X ─→ A^n_S = Spec(A[T_1, …, T_n]),
```

defined by `T_i ↦ t_i`, is of finite presentation, `x` is isolated in its fiber `u⁻¹(u(x))`, and one has
`u(x) = τ_0(s)`, where `τ_0 : S → A^n_S` denotes the "zero section" of `A^n_S → S`, corresponding to the morphism of
`A`-algebras `A[T_1, …, T_n] → A` that sends each `T_i` to 0. Since the set of points of `X` that are isolated in their
fiber above `A^n_S` is open (EGA IV₃, 13.1.4), one may assume, shrinking `X`, that `u` is quasi-finite and that
`u⁻¹(u(x)) = {x}`. By Lemma 5.6.1.0, `u` is universally open at the point `x`.

Let `B_0 = B/(t_1, …, t_n)` and let `X_0 = X ×_{A^n_S} τ_0(S) = Spec B_0` and `u_0 : X_0 → S` be the morphism deduced
from `u` by the base change `τ_0 : S ↪ A^n_S`. Then `u_0` is quasi-finite and of finite presentation, universally open
at the point `x`, and `x` is the unique point of `X_0` above `s`.

Let `A′` be the henselization of the local ring `A_p = O_{S,s}`, and let `S′ = Spec(A′)`, `B′_0 = B_0 ⊗_A A′`, and
`X′_0 = X_0 ×_S S′ = Spec(B′_0)`. Then the closed point `s′` of `S′` is the unique point of `S′` above `s`, one has
`κ(s′) = κ(s)`, and `X′_0` has a unique point `x′` above `s′`; one has `κ(x′) = κ(x)` and `x′` is also the unique point
of `X′_0` above `s` and above `x`. Since `A′` is henselian, by EGA IV₄, 18.5.11, `X′_0` is the disjoint sum of two open
and closed parts:

```text
(*)    X′_0 = V ⊔ W,    where V = Spec(O_{X′_0, x′});
```

and the local ring `O_{X′_0, x′}` is finite and of finite presentation over `A′`. The restriction `π` of `u′_0` to `V`
is therefore finite and of finite presentation. Moreover, since `u′_0 : X′_0 → S′` is open at `x′`, one has
`u′_0(V) = Spec(O_{S′, s}) = S′`, so that `π` is surjective.

This proves the desired result when `S = S′`. In the general case, `A′` is a filtered direct limit of subalgebras
`A_i` étale over `A`, and such that `S_i = Spec(A_i)` has a unique point `s_i` above `s` (and `κ(s_i) = κ(s)`). Then
`B′_0 = lim B_i`, where `B_i = B_0 ⊗_A A_i`. Set `X_i = Spec(B_i) = X_0 ×_S S_i` and `C = O_{X′_0, x′}`. By (∗) above,
one has `C ≅ B′_0 / f B′_0`, for some idempotent `f ∈ B′_0`, and there exist an index `i` and `f_i ∈ B_i` such that `f`
is the image of `f_i` in `B′_0`. Set `C_i = B_i / f_i B_i` and `V_i = Spec(C_i)`.

<!-- original page 361 -->

Then `C = C_i ⊗_{A_i} A′`, whence `V = V_i ×_{S_i} S′`, and `C_i` is an `A_i`-algebra of finite presentation (since the
same is true of `B_i`). Consequently, the morphisms:

```text
X′_0 ──── u′_0 ────→ S′
   ▲                  ▲
   │ h′                │ π
   │                  │
   V ─────────────────┘
```

come, by the base change `S′ → S_i`, from morphisms of finite presentation:

```text
X_i ──── u_i ────→ S_i
   ▲                ▲
   │ h_i             │ π_i
   │                ▲
   V_i ────────────┘
```

For every `j ≥ i`, let `V_j = V_i ×_{S_i} S_j` and let `π_j : V_j → S_j` be the morphism (of finite presentation)
deduced from `π_i` by base change. Since `π : V → S′` is finite and surjective, by EGA IV₂, 8.10.5, there exists an
index `j` such that `π_j : V_j → S_j` is finite and surjective. Then `w : S_j → S` is étale affine, `S_j` has a unique
point `s_j` above `s`, and `V_j` has a unique point `x_j` above `s_j` (since `x′` is the unique point of
`V = V_j ×_{S_j} S′` above `s′`):

```text
X_j ────→ X_0 ────→ X
 ▲          ▲        ▲
 │ u_j      │ u_0    │ u
 │ h_j      │ f      │ f
 │          │        │
 V_j ─────→ S_j ────→ S ─── τ_0 ───→ A^n_S.
            π_j        w
```

Hence `x_j` is the unique point of `V_j` above `s`, its image under the morphism `V_j → X_j → X` is `x`, and one has
`κ(x_j) = κ(x)`. ∎

<!-- original page 354 -->

**Lemma 5.6.2.0.** [^N.D.E-VI_B-42] *Let `k` be a field and `G` a non-empty `k`-scheme of finite type.*

*(i) Let `K` be an extension of `k` and `W` a dense open subset of `G_K`. Denote by `π` the projection `G_K → G`; then*

```text
U = {g ∈ G | W contains every maximal point of π⁻¹(g)}
```

*is a dense open subset of `G`. (N.B. If `g` is a closed point of `G` belonging to `U`, then `π⁻¹(g) ⊂ W`.)*

*(ii) Suppose moreover `G` geometrically irreducible. Let `µ : G × X → Y` be a morphism of `k`-schemes, `x` a point of
`X`, and `Ω` an open of `Y` such that `µ_x⁻¹(Ω_{κ(x)}) ≠ ∅`, where `µ_x` denotes the morphism `G_{κ(x)} → Y_{κ(x)}`,
`g ↦ µ(g, x)`. Then:*

```text
U = {g ∈ G | µ sends every maximal point of g × x into Ω}
```

*is a dense open subset of `G`, and for every closed point `g` of `G` belonging to `U`, one has `µ(g × x) ⊂ Ω` and hence
`µ(g′, x) ∈ Ω_{κ(x)}` (resp. `µ(g, x′) ∈ Ω_{κ(g)}`), for every point `g′ ∈ G_{κ(x)}` above `g`
(resp. `x′ ∈ X_{κ(g)}` above `x`).*

*(iii) Suppose `G = H⁰`, where `H` is a `k`-group scheme locally of finite type, acting on a non-empty `k`-scheme `X` in
such a way that the morphism `H ×_S X → X ×_S X`, `(h, x) ↦ (hx, x)` is surjective. Let `U` be an open of `X`. Then:*

*(a) `G · U` is an open of `X`, equal to the union of the irreducible components of `X` whose generic point belongs to
`U`.*

*(b) Suppose `U` dense in every irreducible component of `X`. Then, for every finite subset `A` of `X`, there exists a
closed point `g ∈ G` such that `g · A′ ⊂ U_{κ(g)}`, where `A′` is the inverse image of `A` in `X_{κ(g)}`. In particular,
the morphism `G × U → X` is surjective.*

<!-- label: III.VI_B.5.6.2.0 -->

[^N.D.E-VI_B-42]: We have added this lemma, communicated by O. Gabber. It allows us to simplify the proof of 5.6.2, and to prove Theorem 5.3, as well as 5.4, in a more general form, see 5.7 and 5.8 below.

*Proof.* (i) Let `k̄` be a separable closure of `k` and let `L` be an extension of `k` containing a copy of `k̄` and of
`K`. Denote by `π_L` (resp. `φ`) the projection `G_L → G` (resp. `G_L → G_K`). Since, for every `g ∈ G`, `φ` sends the
maximal points of `π_L⁻¹(g)` surjectively onto those of `π⁻¹(g)`, one sees that
`U = {g ∈ G | W_L contains every maximal point of π_L⁻¹(g)}`. So, replacing `K` by `L`, we reduce to the case where `K`
contains `k̄`.

Since the projection `p : G_K → G_{k̄}` is surjective and open, `V = p(W)` is a dense open of `G_{k̄}`, and since
`p⁻¹(g) = Spec(κ(g) ⊗_{k̄} K)` is irreducible for every `g ∈ G_{k̄}` (cf. EGA IV₂, 4.3.3), then for every `g ∈ V`, the
generic point of `p⁻¹(g)` belongs to `W`. On the other hand, let `Γ = Gal(k̄/k)`; since the projection
`q : G_{k̄} → G` is surjective and `Γ` acts transitively on the fibers of `q`, then `U = q(V′)`, where `V′` is the
intersection of the `Γ`-conjugates of `V`.

<!-- original page 362 -->

Now, let `Z` be the closed `G_{k̄} − V`, with its reduced closed subscheme structure. Since `G_{k̄}`, and hence `Z`, is
of finite presentation over `k̄`, `Z` comes by base change from a reduced closed subscheme `Z_1` of `G ⊗_k k_1`, for
some finite Galois extension `k_1` of `k`, so the `Γ`-conjugates of `Z` are finite in number, so that their union is
again a rare closed `F` of `G_{k̄}`, and `V′ = G_{k̄} − F` is a dense open of `G_{k̄}`. Hence, since the projection
`q : G_{k̄} → G` is surjective and open, `U = q(V′)` is a dense open of `G`. Moreover, for every closed point `g` of
`G`, the fiber `π⁻¹(g)` is formed of finitely many closed points of `G_K`, so if `g ∈ U` then `π⁻¹(g) ⊂ W`. This
proves (i), and (ii) follows from it.

On the other hand, (iii)(a) has been proved in (VI_A, 2.6.4). Finally, if `U` is dense in every irreducible component
of `X`, then `X = G · U`, hence for every `x ∈ X`, `µ_x⁻¹(U_{κ(x)})` is a non-empty open of `G_{κ(x)}`, and then
(iii)(b) follows from (ii). ∎

**Corollary 5.6.2.** *Let `S`, `G`, `X` be as in the preliminary hypotheses of 5.3, and let `U` be an open of `X`,
`s ∈ S`, and `A` a finite part of `X_s`. Suppose `U_s` dense in `X_s` and `X_s` locally of finite type over
`κ(s)`.*[^N.D.E-VI_B-43]

*Then there exists a morphism `f : S″ → S`, composed of a finite surjective morphism `S″ → S′` and an étale morphism
`S′ → S`, and a morphism `h : S″ → G`, such that the inverse image `A″` of `A` in `X ×_S S″` (i.e. in
`X_s ×_{Spec κ(s)} S″_s`) is contained in `ℓ_h⁻¹(U_{S″})`, where `ℓ_h` denotes the translation of `X_{S″} = X ×_S S″`
defined by the element `h ∈ G(S″)`.*

<!-- label: III.VI_B.5.6.2 -->

[^N.D.E-VI_B-43]: We have added the hypothesis on `X_s` and simplified (and corrected) the proof, taking into account the addition 5.6.2.0. Moreover, the proof shows that the conclusion is valid if one assumes only that `U_s` is dense in every irreducible component of `X_s`.

*Proof.* Since `X_s` is locally of finite type over `κ(s)`, the connected components of `X_s` are open, and irreducible
(cf. (VI_A, 2.5.4)), so `U_s` is dense in every irreducible component of `X_s`.

Hence, by Lemma 5.6.2.0, there exists a closed point `g ∈ G⁰_s` such that `g · a′ ∈ U_s ⊗_{κ(s)} κ(g)` for every
`a′ ∈ X_{κ(g)}` above a point of `A`.

<!-- original page 355 -->

By Lemma 5.6.1, there exists a morphism `f : S″ → S`, composed of a finite surjective morphism `S″ → S′` and an étale
morphism `S′ → S`, and a morphism `h : S″ → G`, such that `f⁻¹(s)` is formed of a single point `s_0`, and such that
`h(s_0) = g` and `κ(s_0) = κ(g)`. Then, denoting by `A″` the inverse image of `A` in
`X_s ×_{Spec κ(s)} S″_s = X_s ⊗_{κ(s)} κ(s_0) = X_s ⊗_{κ(s)} κ(g)`, the translation `ℓ_h` of `X_{S″}` sends `A″` into
`U_s ⊗_{κ(s)} κ(s_0)`. ∎

**Lemma 5.6.3.** *Let `X` be an `S`-scheme. The following conditions are equivalent:*

*(i) `X` is separated over `S`.*

*(ii) For every `S`-scheme `T`, every section `σ : T → X_T` is a closed immersion.*

*(iii) For every reduced `S`-scheme `T`, two `S`-morphisms `f_1` and `f_2 : T → X` that coincide on a dense open `U` of
`T` are equal.*

*(iv) For every `s ∈ S` and every pair of points `x_1`, `x_2` of `X_s`, there exists a morphism
`φ : S″ → S′ → S` and an open subscheme `V` of `X_{S″}`, separated over `S″`, such that:*

*a) `S′ → S` is open, `S″ → S′` closed surjective, and `φ⁻¹(s) ≠ ∅`.*

*b) The inverse image of `{x_1, x_2}` in `X_{S″}` is contained in `V`.*

*(iv′) For every `s ∈ S`, every pair of points `x_1, x_2 ∈ X_s` is contained in an open `V` of `X`, separated over
`S`.*[^N.D.E-VI_B-44]

<!-- label: III.VI_B.5.6.3 -->

[^N.D.E-VI_B-44]: We have simplified the formulation of condition (iv) and added condition (iv′). On the other hand, we have added the proof of the implication (i) ⇒ (iii), used in the proof of (iv) ⇒ (iii). Note moreover that if `T = Spec k[ε, x]/(ε², εx)` (`k` a field), `X = T_red = Spec k[x]`, then the morphisms `φ_λ : T → X` defined by `x ↦ x + λε` (`λ ∈ k`) coincide on the dense open `Spec B_x` but are not equal.

*Proof.* The implication (ii) ⇒ (i) is clear (take `T = X` and `σ =` the diagonal section), as is
(i) ⇒ (iv′) ⇒ (iv). On the other hand, one has (i) ⇒ (ii) by EGA I, 5.4.6.

(iii) ⇒ (ii). Let `σ : T → X_T` be a section of `p : X_T → T`. By EGA I, 5.3.13, `σ` is an immersion, i.e. an
isomorphism of `T` onto a locally closed subscheme `E` of `X_T`. To show that `E` is closed, one may assume `T` and `E`
reduced. Let `Ē` be the reduced closed subscheme of `X_T` having the closure of `E` as underlying space, so that `E` is
a dense open subscheme of `Ē`. Then the immersion `i : Ē ↪ X_T` and `σ ∘ p ∘ i` coincide on `E`, hence on `Ē` by
hypothesis (iii). Hence every point of `Ē` belongs to `σ(T) = E`, whence `E = Ē`.

<!-- original page 364 -->

(i) ⇒ (iii). Suppose `X` separated over `S` and let `T` be a reduced `S`-scheme, `f_1, f_2` two `S`-morphisms `T → X`
that coincide on a dense open `U` of `T`, and `g` the morphism `T → X ×_S X` with components `f_1` and `f_2`. Since
`D = Δ_{X/S}(X)` is closed, its inverse image under `g` is a closed subset of `T` containing `U`, hence equal to `T`,
and since `T` is reduced, `g` factors through `D` (cf. EGA I, 5.2.2); consequently `f_1 = p_1 ∘ g` equals `p_2 ∘ g = f_2`.

(iv) ⇒ (iii). Let `T` be a reduced `S`-scheme and `f_1, f_2` two `S`-morphisms `T → X` that coincide on a dense open
`U`. Since `T` is reduced, to see that `f_1 = f_2`, it suffices to see that `f_1 = f_2` set-theoretically. Indeed,
suppose this established, and let `t ∈ T`, `V` an affine open of `X` containing `f_1(t) = f_2(t)`, and `W` the open
neighborhood of `t` equal to the inverse image of `V` under the continuous map underlying `f_1` and `f_2`; then the
morphisms `f_i|_W : W → V` coincide on the dense open `U ∩ W` of `W`. Since `V` is separated and `W` reduced, this
entails that `f_1|_W = f_2|_W`, whence `f_1 = f_2`.

Let then `t ∈ T` and `s` its image in `S`; let us show that the points `x_1 = f_1(t)` and `x_2 = f_2(t)` of `X_s` are
equal. Let `φ : S″ → S′ → S` and `V` an open of `X ×_S S″` as in (iv); set `T′ = T ×_S S′` and `T″ = T ×_S S″` and
denote by `g : T″ → T` and `f_i″ : T″ → X_{S″}` (`i = 1, 2`) the morphisms obtained by base change.

Since `U` is dense in `T` and `T′ → T` is open, the inverse image `U′` of `U` in `T′` is dense in `T′`. Let `U″` be the
inverse image of `U′` in `T″` and let `F` be the reduced subscheme of `T″` having `U″` as underlying space. Since
`T″ → T′` is surjective and closed, the image of `F` contains `U′` and is closed, hence equals `T′`. Consequently,
`F ∩ g⁻¹(t)` contains a point `u`.

For `i = 1, 2`, denote by `h_i` the restriction to `F` of `f_i″`. Then `h_i(u)` is a point of `X_{S″}` above
`f_i(t) = x_i`, hence belongs to `V`, since `V` contains the inverse image of `{x_1, x_2}` in `X_{S″}`.

Then `W = h_1⁻¹(V) ∩ h_2⁻¹(V)` is an open of `F`, containing `u`, and the `S″`-morphisms `h_i|_W : W → V` coincide on
the dense open `U″ ∩ W` of `W`. Since `V` is separated over `S″`, one has `h_1|_W = h_2|_W`, whence
`h_1(u) = h_2(u)`, and hence `f_1(t) = f_2(t)`. This proves (iv) ⇒ (iii). ∎

Theorem 5.3 then follows from 5.6.2 and the implication (iv) ⇒ (i) of 5.6.3. ∎

**Counterexample 5.6.4.** *Not every `S`-group `G` is separated. Let `S` be a scheme having a non-isolated closed point
`s`; let `G` be the scheme obtained by glueing two copies of `S` along the open `S − {s}`; one sees easily that `G` is
not separated over `S`, and that it is equipped with a natural structure of `S`-group, all of whose fibers are trivial,
except the fiber `G_s` which is isomorphic to the two-element group `ℤ/2ℤ`.*[^N.D.E-VI_B-45]

<!-- label: III.VI_B.5.6.4 -->

[^N.D.E-VI_B-45]: We have reproduced this example in (VI_A, 0.3), N.D.E. (5).

**Theorem 5.7.** [^N.D.E-VI_B-46] *Let `S` be a scheme, `G` an `S`-group locally of finite presentation over `S` such
that the function `s ↦ dim G_s` is locally constant on `S`, `X` an `S`-scheme on which `G` acts, and `U` an open of `X`,
separated over `S`. Then `G⁰ · U` is an open of `X`, separated over `S`.*

<!-- label: III.VI_B.5.7 -->

[^N.D.E-VI_B-46]: On the one hand, we have suppressed the corollary 5.6.5, which was a repetition of 5.5. On the other hand, the original stated as Remark 5.7 the corollary 5.7.1 below, referring for the proof to 4.7, a number which does not exist in Lect. Notes 151 (but which appeared in the 1965 edition of SGAD, whose nos. 4.5 and 4.6 became 5.6.1 and 5.6.2); we have added Theorem 5.7, communicated by O. Gabber, which makes precise the aforementioned statement in SGAD.

<!-- original page 365 -->

*Proof.* Denote by `µ : G ×_S X → X` the action of `G` on `X`; it is the composition of the automorphism
`(g, x) ↦ (g, gx)` of `G ×_S X` and the projection onto `X`. Since `G ×_S U` is an open of `G ×_S X`, by 4.2 (iii),
`V = G⁰ · U` is open in `X`.

Then, proceeding as in the proof of 5.6.2, one deduces from the implication (iv) ⇒ (i) of 5.6.3 that `V` is separated
over `S`. ∎

**Corollary 5.7.1.** *Let `S` and `G` be as in 5.7, and let `σ`, `τ` be two `S`-sections of `G⁰` (i.e.
`σ, τ ∈ G⁰(S)`). Then the coincidence subscheme `S(σ, τ) ⊂ S` of `σ` and `τ` (i.e. the inverse image of the diagonal
of `G ×_S G` under the morphism `(σ, τ)`) is closed.*

<!-- label: III.VI_B.5.7.1 -->

Indeed, for every `s ∈ S`, let `U` be an affine open of `G` containing `ε(s)`; then `V = ε⁻¹(U)` is an open neighborhood
of `s` in `S`, and since `G⁰ U` is separated, `S(σ, τ) ∩ V` is closed in `V`. ∎

**Remark 5.7.2.** *Gabber points out to us that one can show that if `S` is henselian local, with closed point `s`, then
the intersection of the opens `G⁰ U`, where `U` runs through the affine open neighborhoods of `ε(s)`, is an open group
subscheme of `G`, separated over `S`.*

<!-- label: III.VI_B.5.7.2 -->

### 5.8. Complements.

[^N.D.E-VI_B-47] Let us begin by recalling Proposition (VI_A, 2.6.6):

[^N.D.E-VI_B-47]: We have added this paragraph of complements and counterexamples, all communicated by O. Gabber.

**Proposition 5.8.1.** *Let `k` be a field, `G` a `k`-group locally of finite type acting on a `k`-scheme `X` in such a
way that the morphism `G × X → X × X`, `(g, x) ↦ (gx, x)` is surjective. Suppose `X` quasi-separated. Then the connected
components of `X` are irreducible.*

<!-- label: III.VI_B.5.8.1 -->

**Corollary 5.8.2.** *Let `S`, `G`, `X` be as in the preliminary hypotheses of 5.3. Suppose moreover that every fiber
`X_s` is quasi-separated and connected. Then `X` is separated and quasi-compact over `S`.*

<!-- label: III.VI_B.5.8.2 -->

Indeed, by the preceding proposition, each fiber `X_s` is irreducible, and the rest of the proof is identical to that
of 5.4. ∎

**Example 5.8.3.** *Fix an algebraically closed field `k`. Recall first that every "locally Boolean" topological space
`X` (i.e. having a basis of compact open subsets), equipped with the sheaf of locally constant functions with values in
`k`, is a `k`-scheme (cf. [DG70], I § 1, 2.12). One then says that `X` is a* locally Boolean `k`-scheme.

*Note moreover that every topological space `E` admitting a basis of separated opens (and likewise every scheme `X`)
admits a dense separated open. Indeed, since every increasing union of separated opens is a separated open (for a
scheme `X` this follows from 5.6.3), there exists such an open `U` which is maximal. But then `U` is dense, for if
there existed a non-empty open `V` such that `U ∩ V = ∅`, then `V` would contain a non-empty separated open `W`, and
`U ∪ W` would still be separated, contradicting the maximality of `U`.*

*Now, let `C` be the Cantor space, viewed as the underlying space of the group `(ℤ/2ℤ)^ℕ` equipped with the product
topology. For every point `p` of `C`, let `C(p)` be another copy of `C`, and let `X` be the space obtained by glueing
each `C(p)` to `C` along `C − {p}`; then `X` is a non-separated locally Boolean `k`-scheme, and `C` is a dense open of
`X`.*

*Let `G` be the group of automorphisms of the `k`-scheme `X` (i.e., of homeomorphisms of `X`). Then `G` acts
transitively on `X`. Indeed, `X` is the union of `C` and, for each point `p ∈ C`, of a second point `p′`, which can be
characterized as the unique point `x` of `X − {p}` such that `(C − {p}) ∪ {x}` is separated. It follows that every
automorphism `φ` of `C` extends to an automorphism `φ_X` of `X` such that `φ_X(p′) = φ_X(p)′` for every `p`. On the
other hand, the map `θ_p : X → X` that exchanges `p` and `p′` and fixes the other points is an automorphism of `X`.
Finally, the group of automorphisms of `C` acts transitively on `C`: for example, using the group structure of `C`, it
suffices to consider translations.*

*Hence the discrete `k`-group `G` (hence locally of finite type) acts on the `k`-scheme `X` in such a way that the
morphism `G × X → X × X`, `(g, x) ↦ (gx, x)` is surjective, but `X` is not separated (although `C` is a dense separated
open).*

<!-- label: III.VI_B.5.8.3 -->

**Example 5.8.4.** *We retain the notations of the preceding example. Using the description of `C` as the set of
sequences `(u_n)_{n ∈ ℕ}` of elements of `ℤ/2ℤ`, one sees that `C` minus a point `p` is homeomorphic to a countable
disjoint union of copies of `C`. Indeed, using e.g. the group structure of `C`, one reduces by translation to the case
where `p` is the element `0`, i.e. the zero sequence; then `C − {0}` is the disjoint union of the subspaces
`C_i = {(u_n)_{n ∈ ℕ} | u_i = 1 and u_j = 0 for j < i}`, for `i ∈ ℕ`, each homeomorphic to `C`. For every non-empty
finite subset `F` of `C`, one deduces, by induction on `|F|`, that `C − F` is homeomorphic to a countable disjoint
union of copies of `C`, hence to `C` minus a point.*

*For each `F` of cardinality 2, let `C(F)` be another copy of `C`, denote by `q_F` the point `0` of `C(F)`, and choose
a homeomorphism `φ_F : C(F) − {q_F} ⥲ C − F`; let then `X′` be the space obtained by glueing each `C(F)` to `C` by
means of `φ_F`. Then `X′` is a non-separated locally Boolean `k`-scheme. Moreover, it follows from the construction that
every locally constant function `f : X′ → k` is constant. Indeed, if `x, y ∈ C` and `F = {x, y}`, every neighborhood of
`q_F` meets every neighborhood of `x` or `y`, so if `f : X → k` is locally constant, one has `f(x) = f(q_F) = f(y)`,
and if `F′ = {z, t}` with `z, t ∈ C`, one likewise has `f(q_{F′}) = f(z) = f(q_{{z, x}}) = f(x)`. Consequently, `X′` is
connected.*

*Moreover, every point `x ∈ X′` has a pointed neighborhood homeomorphic to `(C, 0)`. More precisely, fix for each `F` a
homeomorphism of pointed topological spaces `h_F : (C, 0) ⥲ (C(F), q_F)`, and denote by `T` the group of translations
of `C`. Then, if `x = q_F` one has the homeomorphism `q_F`, and if `x ∈ C`, the translation `t_x ∈ T` is a homeomorphism
`(C, 0) ⥲ (C, x)` (and it is the unique element of `T` having this property).*

<!-- original page 367 -->

*Denote by `L` the free group generated by the `h_F` and let `G = T * L` be the "free product" (= coproduct) of `T` and
`L`. For every `h ∈ {h_F}_{|F|=2} ∪ T`, let `σ(h)` be the generator of `G` corresponding to `h` and let `S(h)`
(resp. `B(h)`) be the source (resp. target) of `h`. It is convenient to also set `σ(h_F⁻¹) = σ(h_F)⁻¹` and
`S(h_F⁻¹) = B(h_F)` (resp. `B(h_F⁻¹) = S(h_F)`), and to denote by `E` the set formed by `T`, and the `h_F` and `h_F⁻¹`.*

*On the product space `P = G × X′` (where `G` is endowed with the discrete topology), consider the equivalence relation
generated by the relations:*

```text
(gσ(h), x) ∼ (g, h(x))    when x ∈ S(h)
```

*for every `h ∈ E`, and let `Z` be the quotient space. Then `Z` is obtained from the disjoint union
`∐_{g ∈ G} {g} × X′` by glueing of opens, and hence, for every open `Ω` of `P`, its saturate `Ω̃` is open (cf. [BTop],
I § 5.1, Example 2). Explicitly, since every open of `P` is the union of its intersections with the "slices"
`{g} × X′`, it suffices to consider an open of the form `{1} × W`, where `W` is an open of `X′`. In this case, the
saturate is the union of `{1} × W`, and of*

```text
{σ(h_1)} × h_1⁻¹(W ∩ B(h_1)),    {σ(h_1) σ(h_2)} × h_2⁻¹(h_1⁻¹(W ∩ B(h_1)) ∩ B(h_2)),
```

*etc., for all finite sequences `h_1, …, h_n` of elements of `E`, hence is open. Therefore the projection `π : P → Z`
is open.*

*Note moreover that the word `σ(h_1) ⋯ σ(h_n)` is a reduced word of `G`, except if one of the `h_i` is the neutral
element of `T` or if two consecutive `h_i` belong to `T`, or if `(h_i, h_{i+1})` equals `(h_F, h_F⁻¹)` or
`(h_F⁻¹, h_F)`. So, if `x ∈ X′` and if an element `β = (σ(h_1) ⋯ σ(h_n), h_n⁻¹ ⋯ h_1⁻¹(x))` belongs to `{1} × X′`,
then one may assume that each `h_i` is a translation `t_i`, and in this case the equality `σ(t_1 ⋯ t_n) = 1` entails
that `t_1 ⋯ t_n = 1`, and hence `β = (1, x)`. Since the equivalence relation is compatible with the action of `G`
(acting on `P = G × X′` by left translations on the first factor), one deduces that for every `g ∈ G`, the restriction
of `π` to `{g} × X′` is injective.*

*Let then `z ∈ Z` be arbitrary and let `(g, x) ∈ P` be a representative of `z`. By what precedes,
`U = π({g} × X′)` is an open neighborhood of `z`, and the continuous map `{g} × X′ → U` induced by `π` is open and
bijective, hence a homeomorphism. This shows that `Z` is locally isomorphic to `X′` (hence also to `C`), and is
therefore still a locally Boolean `k`-scheme.*

*Finally, `G` acts transitively on `Z`. Indeed, since every `z ∈ Z` is `G`-conjugate to an element of the form
`π((1, x))`, it suffices to see that every element `(1, x) ∈ P` is equivalent to an element `(σ(h), 0)`; now if
`x ∈ C` one may take for `h` the translation `t_x`, and if `x = q_F` one may take `h = h_F`. Hence `Z` is a locally
Boolean `k`-scheme equipped with a transitive action of the discrete group `G`, but `Z` is not separated.*

<!-- label: III.VI_B.5.8.4 -->




## 6. Subfunctors and group subschemes[^VI_B-6-1]

<!-- label: III.VI_B.6 -->

[^VI_B-6-1]: On the same theme, see also the results of XI 6, whose natural place would be in the present Exposé VI_B. There one finds in particular representability criteria for certain subfunctors-in-groups of a given group scheme.[^N.D.E-VI_B-48]

[^N.D.E-VI_B-48]: We have inserted these results in what follows (nos. 6.5.2 to 6.5.5).

**Definition 6.1.** *(i) Let `X` be an `S`-functor (i.e., a functor from `(Sch/S)°` into `(Ens)`), `G` an `S`-functor in
groups, `u` and `v` two `S`-morphisms from `X` to `G`. The* transporter of `u` into `v`, *denoted `Transp(u, v)`, is the sub-`S`-functor of `G` defined as follows:*

```text
Transp(u, v)(S′) = {g ∈ G(S′) | (int g) ∘ u_{S′} = v_{S′}}
                 = {g ∈ G(S′) | g_{S″} u_{S″}(x) g_{S″}⁻¹ = v_{S″}(x), ∀ x ∈ X(S″), S″ → S′}.
```

*In particular, `Transp(u, u)` is a sub-`S`-functor in groups of `G`; it is called the* centralizer of `u` *and is denoted
`Centr(u)`.*

*(ii) Let `G` be an `S`-functor in groups, `X` and `Y` two sub-`S`-functors of `G`. The* transporter of `X` into `Y`
*(resp. the* strict transporter of `X` into `Y`*), denoted `Transp_G(X, Y)` (resp. `Transpstr_G(X, Y)`), is the sub-`S`-functor of `G` defined as follows:*

```text
Transp_G(X, Y)(S′)    = {g ∈ G(S′) | (int g)(X_{S′}) ⊂ Y_{S′}}
                      = {g ∈ G(S′) | g_{S″} X(S″) g_{S″}⁻¹ ⊂ Y(S″), ∀ S″ → S′}

Transpstr_G(X, Y)(S′) = {g ∈ G(S′) | (int g)(X_{S′}) = Y_{S′}}
                      = {g ∈ G(S′) | g_{S″} X(S″) g_{S″}⁻¹ = Y(S″), ∀ S″ → S′}.
```

*Note that one has*

```text
Transpstr_G(X, Y) = Transp_G(X, Y) ∩ c(Transp_G(Y, X)),
```

*where `c` denotes the inversion morphism of `G`.*[^N.D.E-VI_B-49]

*(iii) Let `G` be an `S`-functor in groups, `H` a sub-`S`-functor of `G`, `i` the canonical `S`-morphism `H → G`; the* centralizer *and* normalizer *of `H` in `G` are the following sub-`S`-functors in groups of `G`:*

```text
Centr_G H = Centr(i) = Transp(i, i),    Norm_G H = Transpstr_G(H, H).
```

*Finally, the* center *of `G` is the `S`-functor in groups `Centr(id_G) = Centr_G G`; it will be denoted `Centr G`.*

<!-- label: III.VI_B.6.1 -->

[^N.D.E-VI_B-49]: If `u : X → G` and `v : Y → G` are two arbitrary morphisms of `S`-functors, let `u(X)` be the image-functor of `u`, defined by `u(X)(S′) = u(S′)(X(S′)) ⊂ G(S′)`; this is a subfunctor of `G`, as is the image-functor `v(Y)`. One may then consider the transporter of the image of `u` into the image of `v`, `Transp_G(u(X), v(Y))`. We see thus that, in definition (ii), it is not necessary to restrict to subfunctors, i.e. to the case where `u` and `v` are monomorphisms. This restriction sometimes imposed in the original repetitions in the hypotheses, such as: "Let `u, v : X → G` be morphisms of `S`-functors, `w : H → G` and `w′ : K → G` monomorphisms, then `Transp(u, v)`, `Centr_G(w) = Centr_G H` and `Transp_G(H, K)` verify…", which can be avoided by considering `Transp_G(u(X), v(Y))`. We have made such modifications in 6.2 and, later, in 10.11.

**Remark 6.1.1.** [^N.D.E-VI_B-50] It follows from the definitions that the functors `Transp(u, v)` and `Transp_G(X, Y)`
(and hence also `Transpstr_G(X, Y)`) commute with base change: for every `S′ → S`, if `G′, X′, Y′, u′, v′` are deduced
from `G, X, Y, u, v` by base change, then

```text
Transp(u, v)_{S′} = Transp(u′, v′)    and    Transp(X, Y)_{S′} = Transp(X′, Y′).
```

<!-- label: III.VI_B.6.1.1 -->

[^N.D.E-VI_B-50]: We have added this remark, used implicitly in Proposition 6.2.

<!-- original page 369 -->

**Proposition 6.2.** [^N.D.E-VI_B-51] *Let `G` be an `S`-group. For a subfunctor `T` of the functor `G`, consider the
following property:*

```text
(+f)  for every s ∈ S, T_s is representable by a closed subscheme of G_s.
```

*Let `u, w : X → G` and `v : Y → G` be morphisms of `S`-schemes. Then:*

*(i) `Transp(u, w)` and `Centr(u) = Transp(u, u)` satisfy condition `(+f)`.*

*(ii) `Transp_G(u(X), v(Y))` and `Norm_G v(Y)` satisfy condition `(+f)` if, for every `s ∈ S`, `v_s` is a closed immersion.*

*(iii) `Transpstr_G(X, Y)` satisfies condition `(+f)` if, for every `s ∈ S`, `u_s` and `v_s` are closed immersions.*

<!-- label: III.VI_B.6.2 -->

This follows from Remark 6.1.1 and from Corollary 6.2.5 below.[^N.D.E-VI_B-52]

[^N.D.E-VI_B-51]: We have modified the statement, as indicated in N.D.E. (49).

[^N.D.E-VI_B-52]: The original referred to the results of Exp. VIII, § 6. For the reader's convenience, we have reproduced these results (with the exception of VIII, 6.3 and 6.8) in nos. 6.2.1 to 6.2.5 below. Moreover, this was suggested by A. Grothendieck in a Note at the beginning of VIII.6: "The present number is independent of the theory of diagonalizable groups; its natural place would be in VI_B."

**Definition 6.2.1.** *Let `f : X → S` be a morphism of schemes. One says that `f` is* essentially free, *or that `X` is*
essentially free over `S`, *if one can find a covering of `S` by affine open sets `S_i`, for every `i` an
`S_i`-scheme `S′_i` affine and faithfully flat over `S_i`, and a covering `(X′_{ij})_j` of `X′_i = X ×_S S′_i` by affine
open sets `X′_{ij}`, such that for every `(i, j)`, the ring of `X′_{ij}` is a projective[^N.D.E-VI_B-53] module over the
ring of `S′_i`.*

<!-- label: III.VI_B.6.2.1 -->

[^N.D.E-VI_B-53]: On the one hand, we have replaced the word "free" by "projective", as indicated in VIII, Remark 6.8. On the other hand, the notion of essentially free `S`-scheme is intimately related to the geometric notion of flat and pure `S`-scheme, introduced and studied by M. Raynaud and L. Gruson ([RG71]); cf. the addition 6.9 below.

**Proposition 6.2.2.** *a) If `X` is essentially free over `S`, it is flat over `S`; the converse is true if `S` is
Artinian.*

*b) If `S` is the spectrum of a field, every `S`-scheme is essentially free over `S`.*

*c) If `X` is essentially free over `S`, then `X′ = X ×_S S′` is essentially free over `S′`, for every `S′ → S`. The
converse is true if `S′ → S` is faithfully flat and quasi-compact.*

<!-- label: III.VI_B.6.2.2 -->

<!-- original page 370 -->

The proof is immediate; for the converse in a) one uses the fact that a flat module over an Artinian local ring is
free.[^N.D.E-VI_B-54]

The introduction of Definition 6.2.1 is justified by the following theorem.

[^N.D.E-VI_B-54]: Indeed, let `(A, 𝔪)` be an Artinian local ring, `k` its residue field, `M` an arbitrary `A`-module, `(x_i)_{i ∈ I}` elements of `M` whose images form a basis of `M/𝔪M` over `k`. Let `F` be the free `A`-module with basis `(e_i)_{i ∈ I}`, and `φ : F → M` the `A`-morphism defined by `φ(e_i) = x_i`. Then `Q = Coker φ` satisfies `Q = 𝔪Q`, hence, since `𝔪` is nilpotent, `Q = 0`. Suppose moreover `M` flat over `A`; then `K = Ker φ` satisfies `K ⊗_A k = 0`, i.e. `K = 𝔪K`, hence `K = 0`.

**Theorem 6.2.3.** *Let `S` be a scheme, `Z` an essentially free `S`-scheme, `Y` a closed subscheme of `Z`. Consider the
functor `F = ∏_{Z/S} Y/Z : (Sch)°_{/S} → (Ens)` defined by the following condition: `F(S′) = ∅` when `Y_{S′} ≠ Z_{S′}`, and `F(S′)` is reduced to a single element otherwise.*[^N.D.E-VI_B-55]

*(i) This functor is representable by a closed subscheme `T` of `S`.*

*(ii) If moreover `Y → Z` is of finite presentation, then so is `T → S`.*

<!-- label: III.VI_B.6.2.3 -->

Let us first note that the functor under consideration is a sheaf for the (fpqc) topology: since `F(S′) = ∅` or `{pt}`
for every `S′`, this reduces to verifying that if `(S_i)` is an open covering of `S` (resp. `S′ → S` a faithfully flat
and quasi-compact morphism), and if each `Y_{S_i} → Z_{S_i}` (resp. `Y_{S′} → Z_{S′}`) is an isomorphism, then so is
`Y → Z`; this is clear (resp. follows from SGA 1, VIII 5.4 or EGA IV₂, 2.7.1).

Moreover, by SGA 1, VIII 1.9, faithfully flat and quasi-compact morphisms are of effective descent for the fibered
category of closed-immersion arrows. This allows us, with the notations of 6.2.1, to limit ourselves to the case where
`S = S′_i`.

Let then `(Z_j)` be a covering of `Z` by affine open sets such that `𝒪(Z_j)` is a projective module over `A = 𝒪(S)`, and
let `Y_j = Y ∩ Z_j` and `F_j : (Sch)°_{/S} → (Ens)` be the functor defined in terms of `(Z_j, Y_j)` as `F` is in terms of
`(Z, Y)`. It is a subfunctor of the final functor, and one obviously has `F = ⋂_j F_j`, which reduces us to proving that
each `F_j` is representable by a closed subscheme `T_j` of `S` (for then `F` will be representable by the closed
subscheme `T` intersection of the `T_j`). We may therefore also suppose `Z` affine, `Z = Spec(B)`, where `B` is a
projective `A`-module. Let `L` be a free `A`-module with basis `(e_λ)_{λ ∈ Λ}`, of which `B` is a direct factor as an
`A`-module, and let `φ_λ : L → A` be the "coordinate" forms relative to this basis. Let `E` be a generating set of the
ideal `J` of `B` defining the subscheme `Y` of `Z`, and let `I` be the ideal in `A` generated by the coordinates
`φ_λ(x)`, for `x ∈ E`. For every `A`-algebra `C`, one sees then that the morphism `B ⊗_A C → (B/J) ⊗_A C` is an
isomorphism if and only if the image of `x ⊗ 1` in `L ⊗_A C` is zero for every `x ∈ E`, which amounts to saying that the
kernel of `A → C` contains the ideal `I`. This shows that `T = V(I) = Spec(A/I)` satisfies the desired condition, which
proves (i).

Moreover, if `Y → Z` is of finite presentation, one may take `E` finite, and then `I` is a finitely generated ideal of
`A`, i.e. the closed immersion `T → S` is of finite presentation.

[^N.D.E-VI_B-55]: cf. Exp. II § 1, where this functor is denoted `∏_{Z/S} Y`; for every `S′ → S`, `F(S′) = Γ(Y_{S′}/Z_{S′})`, which here equals `{id_{Z_{S′}}}` if `Y_{S′} = Z_{S′}`, and is empty otherwise. On the other hand, we have added assertion (ii), used in the proof of 6.5.3.

<!-- original page 371 -->

**Examples 6.2.4.** *Let us give important examples of functors which reduce to functors `∏_{Z/S} Y/Z` of the type
considered in 6.2.3 and for which it is useful to have representability criteria in what follows. We denote by `S` a
scheme, and by `X, Y, Z`, etc., schemes over `S`.*

*a) Suppose given an `S`-morphism*

```text
(x)    q : X → Hom_S(Y, Z),
```

*(`X` acts on `Y`, with values in `Z`), i.e. a morphism*

```text
(xx)   r : X ×_S Y → Z.
```

*Consider a subscheme `Z′` of `Z`, whence a monomorphism*

```text
Hom_S(Y, Z′) → Hom_S(Y, Z)
```

*which makes the first functor a subfunctor of the second; let `X′` be the inverse image of this subfunctor under the
morphism `q`. This is the subfunctor of `X` such that `X′(T)` is the set of `x ∈ X(T)` such that `q(x) : Y_T → Z_T`
factors through `Z′_T`. This functor `X′` can be described as follows: set `P = X ×_S Y`, let `P′` be the inverse image
of `Z′` under `r : P → Z`; then one has an obvious isomorphism*

```text
(xxx)  X′ ≃ ∏_{P/X} P′/P.
```

*One thus obtains: if `Y` is essentially free over `S` and `Z′` closed in `Z`, the subfunctor `X′` of `X` is representable
by a closed subscheme of `X`.*[^N.D.E-VI_B-56] *If moreover `Z′ → Z` is of finite presentation, then so is `X′ → X`.*

*b) Suppose given two ways of letting `X` act on `Y` with values in `Z`, i.e. two morphisms*

```text
q_1, q_2 : X ⇒ Hom_S(Y, Z),
```

*and set `X′ = Ker(q_1, q_2)`: this is the subfunctor of `X` such that `X′(T)` is the set of `x ∈ X(T)` such that the two
morphisms `q_1(x), q_2(x) : Y_T ⇒ Z_T` are equal. Now the data of `q_1, q_2` is equivalent to the data of a morphism*

```text
q : X → Hom_S(Y, Z ×_S Z),
```

*or equivalently of a morphism `r : X ×_S Y → Z ×_S Z`; set then `U = Z ×_S Z`, let `U′` be the diagonal subscheme of `Z ×_S Z`. Then `X′` is nothing but the inverse image of the subfunctor `Hom_S(Y, U′)` of `Hom_S(Y, U)` under `q`, hence
can be put in the form `(xxx)`, with `P = X ×_S Y`, and `P′` = inverse image of the diagonal under `r`, i.e. kernel of
`r_1, r_2 : X ×_S Y ⇒ Z`. One is therefore in the conditions of (a).*

*One sees consequently that: if `Y` is essentially free over `S` and `Z` separated over `S`, then the subfunctor `X′` of
`X` is representable by a closed subscheme of `X`.*[^N.D.E-VI_B-56] *If moreover `Z → S` is locally of finite type, then
`X′ → X` is of finite presentation.*

[^N.D.E-VI_B-56]: We have added the sentence that follows.

<!-- original page 372 -->

*c) Suppose given a morphism*

```text
q : X → Hom_S(Y, Y),
```

*i.e. "`X` acts on `Y`". Let `X′` be the "kernel" of this morphism, i.e. the subfunctor `X′` of `X` such that `X′(T)` is
the set of `x ∈ X(T)` such that `q(x) : Y_T → Y_T` is the identity. This functor falls under b), as one sees by
introducing a second homomorphism*

```text
q′ : X → Hom_S(Y, Y)
```

*"by letting `X` act trivially on `Y`". Hence: if `Y` is essentially free and separated over `S`, the subfunctor `X′` of
`X` kernel of `q` is representable by a closed subscheme of `X`.*[^N.D.E-VI_B-56] *If moreover `Y → S` is locally of
finite type, then `X′ → X` is of finite presentation.*

*d) Under the conditions of c), consider the subfunctor `Y′` of `Y` "of the invariants under `X`", so that `Y′(T)` is the
set of `y ∈ Y(T)` such that the corresponding morphism `q(y) : X_T → Y_T` is "the constant `T`-morphism with value `y`".
Introducing `q′` as in c), and the homomorphisms corresponding to `q` and `q′`:*

```text
q, q′ : Y ⇒ Hom_S(X, Y),
```

*one sees that `Y′` is precisely `Ker(q, q′)`, and hence falls again under b) (with the roles of `X, Y` reversed and `Z = Y`).*

*Consequently, if `X` is essentially free over `S` and `Y` separated over `S`, then the subfunctor `Y′` of `Y` of the
invariants under `X` is representable by a closed subscheme of `Y`.*[^N.D.E-VI_B-56] *If moreover `Y → S` is locally of
finite type, then `Y′ → Y` is of finite presentation.*

*e) Constructions of the type made explicit in the preceding examples are particularly frequent in group theory. Thus,
when `G` is an `S`-group scheme acting on the `S`-scheme `X`:*

```text
q : G → Aut_S(X),
```

*the kernel of `q` ("the subgroup of `G` acting trivially") is a closed subscheme of `G` provided `X` is essentially free
and separated over `S` (example c)), and the subobject `X^G` of invariants is a closed subscheme of `X`, provided `G` is
essentially free over `S` and `X` separated over `S` (example d)).*

*Let `Y, Z` be subschemes of `X`; consider the subfunctor `Transp_G(Y, Z)` of `G` ("transporter of `Y` into `Z`"), whose
points with values in a `T` over `S` are those `g ∈ G(T)` such that the corresponding automorphism of `X_T` satisfies
`g(Y_T) ⊂ Z_T`, i.e. induces a morphism `Y_T → X_T` factoring through `Y_T → Z_T`. Hence: if `Y` is essentially free over
`S`, and `Z` closed in `X`, then `Transp_G(Y, Z)` is a closed subscheme of `G` (example a)).*

*One may also consider the strict transporter of `Y` into `Z`,*[^N.D.E-VI_B-57] *whose points with values in a `T` over
`S` are those `g ∈ G(T)` such that `g(Y_T) = Z_T`, which is nothing but `Transp_G(Y, Z) ∩ σ(Transp_G(Z, Y))`, where `σ`
is the inversion morphism of `G`. Consequently,*

[^N.D.E-VI_B-57]: denoted `Transpstr_G(Y, Z)`.

<!-- original page 373 -->

*if `Y` and `Z` are essentially free over `S` and closed in `X`, the strict transporter of `Y` into `Z` is a closed
subscheme of `G`.*

*An important case is the one where `X = G`, with `G` acting on itself by inner automorphisms. If `H` is a subscheme of
`G`, the strict transporter of `H` into `H` is also called the* normalizer of `H` in `G`*, and denoted `Norm_G H`. Hence:
if `H` is a closed group subscheme of `G`, essentially free over `S`, then `Norm_G H` is representable by a closed group
subscheme of `G`.*

*Let finally `Z` be a subscheme of `G`; then its centralizer `Centr_G(Z)` in `G` is the subfunctor in groups of `G`
defined by the procedure of d), when one considers that "`Z` acts on `G`" by the operations induced by those of `G`;
hence if `Z` is essentially free over `S` and `G` is separated over `S`, `Centr_G(Z)` is a closed group subscheme of `G`.
In particular, if `G` is essentially free and separated over `S`, then the center `C` of `G`, which is none other than
`Centr_G(G)`, is a closed group subscheme of `G`.*

<!-- label: III.VI_B.6.2.4 -->

When `S` is the spectrum of a field, 6.2.2 b) shows that in examples a) to e) above, the "essentially free" conditions
are automatically satisfied; only the separation conditions remain. Recalling that a group scheme over a field is
necessarily separated (VI_A, 0.3), one finds for example:

**Corollary 6.2.5.** *Let `G` be a group scheme over a field `k` and let `Y, Y′` be two subschemes of `G`. Then:*

*(i) The centralizer of `Y` in `G` is a closed group subscheme of `G`; in particular, this is the case for the center
`Centr_G(G)` of `G`.*

*(i′) More generally, if `u, v : X → G` are morphisms of schemes, `Transp_G(u, v)` is representable by a closed subscheme
of `G`.*

*(ii) If `Y` is closed, the transporter `Transp_G(Y′, Y)` is a closed subscheme of `G`. If `Y′` is also closed, the same
conclusion holds for `Transpstr_G(Y′, Y)`.*

*(iii) For every group subscheme*[^N.D.E-VI_B-58] *`H` of `G`, `Norm_G(H)` is a closed group subscheme of `G`.*

<!-- label: III.VI_B.6.2.5 -->

[^N.D.E-VI_B-58]: Indeed, over a field `k`, every group subscheme of `G` is closed, cf. VI_A, 0.5.2. Moreover, 6.2.5 concludes the insertion of the results drawn from VIII § 6.

**Corollary 6.2.6.** [^N.D.E-VI_B-59] *Let `k` be a field, `G` a connected algebraic `k`-group. Then `Centr_G(G)` is
representable by a closed group subscheme `Z` of `G`, and `G/Z` is an affine algebraic `k`-group.*

<!-- label: III.VI_B.6.2.6 -->

[^N.D.E-VI_B-59]: We have inserted here this corollary (cf. Exp. XII, 6.1), which will be useful later. Moreover, in 6.3 we return to the original text of VI_B.

*Proof.* The first assertion is of course contained in 6.2.5 (i), but we shall see that it also follows from the proof
of the second assertion. Indeed, `G` acts by the adjoint representation on the finite-dimensional `k`-vector spaces
`V_n = 𝒪_{G,e}/𝔪_e^{n+1}` (where `𝔪_e` is the maximal ideal of `𝒪_{G,e}`); let `K_n` denote the kernel of the morphism
`ρ_n : G → GL(V_n)`. By VI_A, 5.4.1, `ρ_n` induces a closed immersion `G/K_n ↪ GL(V_n)`, hence each `G/K_n` is affine.
Since `G` is noetherian, the intersection `K` of the `K_n` equals one of the `K_n`, so `G/K` is affine.

<!-- original page 374 -->

On the other hand, letting `Z` denote the center of `G`, it is clear that `Z ⊂ K`. Let us show that `Z = K`. Let
`𝒪̂_{G,e}` denote the completion of `𝒪_{G,e}` for the `𝔪_e`-adic topology and `Ŝ` its spectrum (resp. `S = Spec 𝒪_{G,e}`).
Since `Ŝ → S` is faithfully flat and since the two morphisms

```text
K ×_k S → S,    (g, x) ↦ gxg⁻¹    resp.    (g, x) ↦ x
```

coincide after base change `Ŝ → S`, they coincide, i.e. `K` acts trivially on `𝒪_{G,e}`. Now, by 6.2.4 e), the
subobject `G^K` of invariants of `G` under `K` (which is none other than `Centr_G(K)`) is a closed subscheme of `G`,
hence defined by a quasi-coherent ideal `𝓘` of `𝒪_G`. As `G^K` majorizes `S = Spec 𝒪_{G,e}` and `𝓘` is of finite type
(since `G` is noetherian), there exists an open neighborhood `U` of `e` such that `𝓘|_U = 0`. Then the subgroup
`G^K = Centr_G(K)` contains `U`, hence also `U · U`, which equals `G` since `G` is irreducible (VI_A 0.5). Hence
`Centr_G(K) = G`, whence `K ⊂ Z` and therefore `Z = K`. ∎

**Remark 6.3.** *Let `k` be an algebraically closed field, `G` a `k`-group and `H` a group subscheme of `G`; assume `G`
and `H` are of finite type over `k` and reduced. Then `Norm_G H` (resp. `Centr_G H`) is representable by a group
subscheme of `G`, whose associated reduced subscheme is none other than the normalizer (resp. the centralizer) of `H` in
`G` in the sense of the* Bible.

<!-- label: III.VI_B.6.3 -->

**Proposition 6.4.** *Let `G` be an `S`-group and `u : X → G` a monomorphism of `S`-schemes. Set `T = Transp_G(X, X)`.
The following conditions are equivalent:*

*(i) `T` is a sub-`S`-functor in groups of `G`.*

*(ii) `T = Transpstr_G(X, X) = Norm_G X`.*

*These conditions are satisfied in each of the two following cases:*

*a) `X` is of finite presentation over `S`.*

*b) `T` is representable by a scheme of finite presentation over `S`.*

<!-- label: III.VI_B.6.4 -->

The equivalence of conditions (i) and (ii) follows from the fact that, whatever the morphism `S′ → S`, whatever
`t, t′ ∈ T(S′)`, one has `tt′ ∈ T(S′)`, and from the fact that `Transpstr_G(X, X) = T ∩ c(T)` (cf. 6.1 (ii)).

Let us place ourselves in case a). Let `t ∈ T(S)`; then `int(t)` is a monomorphism of `X` into `X`, hence an
`S`-automorphism of `X` (EGA IV₄, 17.9.6), so that `t` belongs to `Transpstr_G(X, X)`, whence a).

In case b), it is clear that `μ(T ×_S T) ⊂ T`, and the assertion follows from the following lemma.

**Lemma 6.4.2.** [^N.D.E-VI_B-60] *Let `G` be an `S`-scheme of finite presentation, equipped with an associative law (in
the sense of EGA 0_III 8.2.5). Suppose that for every `S`-scheme `S′` and every `g ∈ G(S′)`, right and left translations
by `g` in the set `G(S′)` are injective, and that `G(S) ≠ ∅`. Then `G` is an `S`-group.*

<!-- label: III.VI_B.6.4.2 -->

[^N.D.E-VI_B-60]: We have kept the numbering of the original: there is no n° 6.4.1.

<!-- original page 375 -->

It suffices to show that, whatever the `S`-scheme `S′`, the set `G(S′)` is a group; now from the hypothesis it follows
at once that right and left translations by every element `g ∈ G(S′)` in `G_{S′}` are `S`-monomorphisms of `G_{S′}` into
`G_{S′}`. They are therefore `S`-automorphisms, since `G` is of finite presentation over `S` (EGA IV₄, 17.9.6), so that
right and left translations by `g` in the set `G(S′)` are bijective, and one is reduced to the following lemma.

**Lemma 6.4.3.** *Let `G` be a non-empty set equipped with an associative law such that right and left translations are
bijective. Then `G` is a group.*

<!-- label: III.VI_B.6.4.3 -->

The proof is left to the reader.

**Definition 6.5.** *Let `G` be an `S`-group, `H` an `S`-functor, and `u : H → G` a monomorphism.*

*(i) The* connected centralizer of `H` in `G`, *denoted `Centr⁰_G H`, is the neutral component of the functor `Centr_G H`
(cf. 3.1 and 6.1 (iii)).*

*(i′) For every morphism `u : X → G`, one defines similarly the functor `Centr⁰(u)` (cf. 6.2 (iv)).*

*(ii) When for every `s ∈ S`, `u_s` is a closed immersion, the* connected normalizer of `H` in `G`*, denoted `Norm⁰_G H`,
is the neutral component of the functor `Norm_G H`.*

*N.B. By 1.4.2, the hypothesis in (ii) is satisfied when `H` is an `S`-group scheme, `G` and `H` are locally of finite
type over `S`, and `u` is a quasi-compact morphism of `S`-groups.*

<!-- label: III.VI_B.6.5 -->

**Proposition 6.5.1.** *Let `G` be an `S`-group locally of finite presentation and quasi-separated over `S`, `H` a smooth
`S`-group with connected fibers, and `u : H → G` a monomorphism. Let `N` be the normalizer of `H` in `G` (cf. 6.1).
According to 6.5.5 below, `N` is representable by a closed group subscheme of `G`, of finite presentation over `G`. This
being so, the following conditions are equivalent:*

*(i) The canonical morphism `H → N` is an open immersion.*

*(ii) `N⁰ = H` (cf. 3.10).*

*(iii) For every `s ∈ S`, one has `H_s = (N_s)⁰`.*

<!-- label: III.VI_B.6.5.1 -->

Condition (i) entails (ii) by Lemma 3.10.1, since `H⁰ = H`. On the other hand, it is clear that (ii) entails (iii), since
`H_s = (N⁰)_s = (N_s)⁰`.

Let us show finally that (iii) entails (i). Since `H_s = (N⁰)_s` for every `s ∈ S`, then `H_s → N_s` is an open immersion.
Moreover, `H` and `N` are locally of finite presentation over `S`, and `H` is flat over `S`, hence (EGA IV₄, 17.9.5),
`H → N` is an open immersion. ∎

[^N.D.E-VI_B-61] For the reader's convenience, we have included below the results 6.8 to 6.11 of Exp. XI.

[^N.D.E-VI_B-61]: We have inserted here nos. 6.5.2 to 6.5.5, drawn from Exp. XI, 6.8 to 6.11. This was moreover suggested by A. Grothendieck in a Note at the beginning of XI 6: "The present number does not use the results of nos. 3, 4, 5 (of XI); its natural place would be in VI_B."

<!-- original page 376 -->

**Theorem 6.5.2.** *Let `X` be a smooth scheme over `S`, with geometrically irreducible fibers.*[^N.D.E-VI_B-62]

*(i) For every closed subscheme `Y` of `X`, the functor `∏_{X/S} Y/X` is representable by a closed subscheme `T` of `S`.*

*(ii) Moreover, if `Y → X` is of finite presentation, then so is `T → S`.*

<!-- label: III.VI_B.6.5.2 -->

[^N.D.E-VI_B-62]: On the one hand, we have corrected the original, by replacing "connected" with "irreducible" (cf. the proof). On the other hand, by [RG71] I, 3.3.4 (iii) and 4.1.1, it suffices to assume that `X` is flat over `S`, with geometrically irreducible fibers and without embedded components.

Since `f : X → S` is faithfully flat locally of finite presentation, it is covering for the (fpqc) topology. On the
other hand, since `T = ∏_{X/S} Y/X` is obviously a subsheaf of `S` for the (fpqc) topology, it follows that the question
of representability of `T` by a closed subscheme of `S` is local in nature on `S` for the (fpqc)
topology,[^N.D.E-VI_B-63] and the same is true of the question of deciding whether `T` is of finite presentation over
`S` (cf. EGA IV₂, 2.7.1). Up to making the base change `S′ → S`, with `S′ = X`, one is reduced to the case where `X`
admits a section `ε` over `S`. One may moreover suppose `S` affine and a fortiori quasi-compact. One then has:

[^N.D.E-VI_B-63]: See for example the addition 1.7 in Exp. VIII.

**Corollary 6.5.3.** *Under the conditions of 6.5.2, suppose that `S` is quasi-compact, that `X → S` admits a section
`ε`, and that `Y → X` is of finite presentation. Then there exists an integer `n ⩾ 0` such that one has*

```text
∏_{X/S} Y/X = ∏_{X_n/S} Y_n/X_n,
```

*where `X_n` is the `n`-th infinitesimal neighborhood of the immersion `ε : S → X`, and `Y_n = Y ∩ X_n`.*

<!-- label: III.VI_B.6.5.3 -->

When `Y` is of finite presentation over `X`, this corollary implies 6.5.2: indeed, `X` being smooth over `S`, `X_n` is
finite and locally free over `S`, hence a fortiori "essentially free" over `S` (cf. 6.2.1), so `∏_{X_n/S} Y_n/X_n` is
representable by a closed subscheme `T` of `S`, of finite presentation over `S`, by 6.2.3.

Let us first prove 6.5.3 (and hence 6.5.2) when `S` is noetherian. Let `T_n = ∏_{X_n/S} Y_n/X_n`; then the `T_n` form a
decreasing sequence of closed subschemes of `S`, and `S` being noetherian, this sequence is stationary. Let
`R = ⋂_{n ⩾ 0} ∏_{X_n/S} Y_n/X_n` be their common value for large `n`; one has obviously `T ⊂ R`, and it suffices to
establish that `R ⊂ T`. Up to making the base change `R → S`, one is reduced to the case where `R = S`, i.e. `Y_n = X_n`
for every `n`, i.e. `Y ⊃ X_n` for every `n`, and one must then prove that `T = S`, i.e. `Y = X`.

Now `Y ⊃ X_n` for every `n` implies (thanks to the fact that `X` is locally noetherian) that `Y` is, in a neighborhood
of every point of `ε(S)`, an induced open subscheme of `X`;[^N.D.E-VI_B-64] hence there exists an induced open `U` of
`X`, containing `ε(S)`, such that `U ⊂ Y`. By virtue of EGA IV₃, 11.10.10, the fibers of `X/S` being integral, `U` is
schematically dense in `X`, hence (`Y` being a closed subscheme majorizing `U`) one has `Y = X`. This proves 6.5.3 hence
6.5.2 when `S` is noetherian.

[^N.D.E-VI_B-64]: see, for example, the proof of 6.2.6.

<!-- original page 377 -->

The general case proceeds by reduction to the preceding case. For every `s ∈ S`, there exists an affine open
neighborhood `U` of `s` and an affine open neighborhood `V` of `ε(s)` such that `f(V) ⊂ U`. Then `f(V)` is an open
neighborhood of `s` contained in `U`, and if `S′` is an affine open neighborhood of `s` contained in `ε⁻¹(V) ∩ f(V)`,
and `X′ = V ∩ f⁻¹(S′)`, then `X′` and `S′` are affine opens of `X` resp. `S`, and `X′/S′` admits a section. Because of
the local nature of 6.5.2 and 6.5.3 we may suppose `S = S′`. Then `X′` is an affine open of `X` containing `ε(S)`. As
each fiber `X_s` is supposed irreducible, `X′_s` is schematically dense in `X_s`, hence, by EGA IV₃, 11.10.10, `X′` is
schematically dense in `X`, and similarly, for every base change `S_1 → S`, `X′ ×_S S_1` is schematically dense in
`X ×_S S_1`.

It follows that `∏_{X/S} Y/X = ∏_{X′/S} Y′/X′`, where `Y′ = Y ∩ X′`. This reduces us to the case where `X = X′`, so one
may suppose `S` and `X` affine. Moreover, if `X = Spec(B)` and if `J` is the ideal of `B` defining `Y`, then `J` is a
direct limit of its finitely generated sub-ideals, hence `Y` is the intersection of closed subschemes `Y_i` of `X` which
are of finite presentation over `X`, and consequently `∏_{X/S} Y/X = ⋂_i ∏_{X/S} Y_i/X`, which reduces us, to prove
6.5.2, to the case where `Y` is of finite presentation over `X`, with `S` and `X` affine.

But then `X` and `Y` over `S` come by base change `S → S_0` from an analogous situation `X_0` and `Y_0` over `S_0`, with
`S_0` noetherian, which reduces us to the case where `S` is noetherian, already treated. This completes the proof of
6.5.2 and 6.5.3. ∎

**Corollary 6.5.4.** *Let `X` be a smooth `S`-group scheme of finite presentation with connected fibers, `Y` a group
scheme of finite presentation over `S`, `i : Y → X` a monomorphism of `S`-group schemes.*

*(i) Then `∏_{X/S} Y/X` is representable by a closed subscheme of finite presentation of `S`.*

*(ii) If moreover `S` is quasi-compact, one has for large enough `n`:*

```text
∏_{X/S} Y/X = ∏_{X_n/S} Y_n/X_n,
```

*where `X_n` denotes the `n`-th infinitesimal neighborhood of the unit section `ε : S → X`, and `Y_n = X_n ∩ Y`.*

<!-- label: III.VI_B.6.5.4 -->

The proof is essentially that of 6.5.3.[^N.D.E-VI_B-65] On the one hand, `i` is locally of finite presentation (cf. EGA
IV₁, 1.4.3). On the other hand, the unit sections of `Y` and of `X` induce bijective immersions `S → Y_n` and `S → X_n`,
hence isomorphisms of `S_red` with `(Y_n)_red` and `(X_n)_red`. Consequently, `i_n` is quasi-compact hence of finite
type, and one has a commutative diagram:

```text
(Y_n)_red ──τ──→ Y_n
       ╲        │
        ╲       │ i_n
       σ ╲      │
          ╲     ↓
           ─→  X_n
```

[^N.D.E-VI_B-65]: We have detailed the original in what follows, adding references to EGA IV.

<!-- original page 378 -->

where `σ, τ` are closed immersions and `τ` is surjective. Since `i_n` is separated (being a monomorphism), it follows
that `i_n` is proper (cf. EGA II, 5.4.3). Hence `i_n` is a proper monomorphism of finite presentation, hence a closed
immersion (cf. EGA IV₃, 8.11.5). Consequently, by virtue of 6.2.3 already used, `∏_{X_n/S} Y_n/X_n` is representable by
a closed subscheme `T_n` of `S` of finite presentation over `S`, and it remains therefore to prove the last assertion of
6.5.4 in the case where one supposes moreover `S` affine.

One reduces immediately again to the case where `S` is noetherian, and one is reduced to proving that one has `R = T`
(with the notations of the proof of 6.5.3), or, again, that `Y ⊃ X_n` for every `n` implies `Y = X`. Now the hypothesis
implies that `i : Y → X` is étale at the points of the unit section of `Y` over `S`, hence `Y` is smooth over `S` at the
points of the unit section, whence it follows that the open `U` of points of `Y` at which `Y` is smooth over `S` is an
induced open subgroup of `Y` (cf. 2.3). Then `τ : U → X` is an étale monomorphism by virtue of 2.5, hence an open
immersion; since the fibers of `X` are connected and every open subgroup of an algebraic group is also closed, it
follows that `τ` is a surjective open immersion, i.e. an isomorphism. Hence `U = X` and a fortiori `Y = X`, which
completes the proof of 6.5.4. ∎

Proceeding as in 6.2.4 e), one concludes from 6.5.4:

**Corollary 6.5.5.** *Let `G` be an `S`-group scheme locally of finite type and quasi-separated over `S`, `H` a smooth
group scheme of finite presentation over `S` with connected fibers, `i : H → G` a monomorphism of `S`-groups. Then:*

*a) `Centr_G(H)` and `Norm_G(H)` are representable by closed subschemes of `G`, of finite presentation over `G`.*

*a′) Similarly, for every monomorphism `j : K → G` of finite presentation of `S`-group schemes, `Transp_G(H, K)` is
representable by a closed subscheme of `G`, of finite presentation over `G`.*

*b) If `G` is quasi-compact, there exists an integer `n ⩾ 0` such that (if `H_n` denotes the `n`-th infinitesimal
neighborhood of the unit section of `H`) one has:*

```text
Centr_G(H) = Centr_G(H_n)        Norm_G(H) = Norm_G(H_n)
Transp_G(H, K) = Transp_G(H_n, K) = Transp_G(H_n, K_n).
```

<!-- label: III.VI_B.6.5.5 -->

*Proof.* [^N.D.E-VI_B-66] Let us first note that the hypothesis on `G` entails that the monomorphism `H → G` is of finite
presentation (EGA IV₁, 1.2.4 and 1.4.3), as is the diagonal immersion `Δ_{G/S} : G → G ×_S G` (loc. cit. 1.4.3.1). The
case of `Norm_G(H)` therefore reduces to that of the transporter, by taking `H = K`. Taking 6.2.4 e) into account, we
shall apply 6.5.4 to the group scheme `X = H_G = H ×_S G` over the base scheme `G`, and to the following group subscheme
`Y`.

In the case of `Transp_G(H, K)`, we take for `Y` the inverse image of `K_G` under the morphism of `G`-groups
`H ×_S G → G ×_S G`, `(h, g) ↦ (ghg⁻¹, g)`. In the case of

[^N.D.E-VI_B-66]: We have detailed what follows. Moreover, this concludes the insertion of XI, 6.8 to 6.11, i.e. we return in 6.6 below to the original text of VI_B.

<!-- original page 379 -->

`Centr_G(H)`, we take for `Y` the inverse image of the diagonal subgroup `Δ_{G/S}(G)_G` of `(G ×_S G)_G` under the
morphism of `G`-groups:

```text
H ×_S G → G ×_S G ×_S G,    (h, g) ↦ (h, ghg⁻¹, g).
```

∎

**Definition 6.6.** *Let `G` be an `S`-functor in groups, `H` a sub-`S`-functor in groups; one says that `H` is*
invariant *(resp.* central*, resp.* characteristic*) in `G` if `Norm_G H = G` (resp. if `Centr_G H = G`, resp. if,
whatever the `S`-scheme `T` and the automorphism `a ∈ Aut_{T-gr.}(G_T)`, one has `a(H_T) ⊂ H_T`), in other words, if,
whatever the `S`-scheme `T`, the subgroup `H(T)` of `G(T)` is invariant in `G(T)` (resp. central in `G(T)`,
resp. invariant under every automorphism of `G_T`).*

*N.B. If `H` is central (resp. characteristic), then it is invariant.*

<!-- label: III.VI_B.6.6 -->

**Remark 6.7.** *Let `G` and `H` be two `S`-groups and `u : H → G` a monomorphism. For `H` to be invariant (resp. central)
in `G`, it is necessary and sufficient that the morphism*

```text
(μ ∘ c ∘ pr_2, μ ∘ (u × id_G)) : H ×_S G → G
```

*(defined by `(h, g) ↦ g⁻¹ h g` whatever `g ∈ G(S′)` and `h ∈ H(S′)`) factor through `u` (resp. equal `u ∘ pr_1`), and for
`H` to be characteristic in `G`, it is necessary and sufficient that for every `S`-scheme `T` and every `T`-automorphism
of groups `a` of `G_T`, `a ∘ u(T)` factor through `u(T)`.*

<!-- label: III.VI_B.6.7 -->

**Example 6.8.** *Let `G` be an `S`-functor in groups. Then `Centr G` is characteristic and central. If, for every `s ∈ S`, `G_s` is representable, then `G⁰` is characteristic. This follows from the definitions and from 3.3.*

<!-- label: III.VI_B.6.8 -->

### 6.9.

[^N.D.E-VI_B-67] In [RG71], I 3.3.3, the authors introduce the geometric notion of pure `S`-scheme, which is local on `S`
for the étale topology; we refer to loc. cit. for the precise definition. Let us simply point out the following:

a) (loc. cit., Th. 3.3.5) If `B` is a flat `A`-algebra of finite presentation, then `B` is a projective `A`-module if and
only if `Spec(B)` is pure over `Spec(A)`.

b) Consequently, if `X → S` is locally of finite presentation, flat and pure, then `X` is essentially free over `S`.

c) (loc. cit., 3.3.4 (iii)) If `X → S` is locally of finite type, flat, with geometrically irreducible fibers and
without embedded components, then `X` is pure over `S`.

Since every group scheme locally of finite type over a field is Cohen–Macaulay (cf. VI_A, 1.1.1), hence without embedded
components, one obtains in particular:

d) Every `S`-group scheme `G` locally of finite presentation, flat, and with connected fibers is pure over `S`, hence
essentially free over `S`.

One may then take up again all the statements of 6.2.4 e) taking into account results (b) and (d) above.

<!-- label: III.VI_B.6.9 -->

[^N.D.E-VI_B-67]: We have added this subsection.

<!-- original page 380 -->

## 7. Generated subgroups; commutator group

<!-- label: III.VI_B.7 -->

In this number, `k` denotes a fixed field.

**Proposition 7.1.** *Let `G` be a `k`-group, `(X_i)_{i ∈ I}` a family of geometrically reduced `k`-schemes;*[^N.D.E-VI_B-68] *for every `i ∈ I`, let `f_i : X_i → G` be a `k`-morphism.*

*(i) There exists a smallest closed group sub-`k`-scheme of `G` majorizing each of the `f_i`, denoted `Γ_G((f_i)_{i ∈ I})`. It is a geometrically reduced `k`-scheme, hence smooth in the case where `G` is supposed locally of finite type over `k` (1.3.1).*

*(ii) Set `X = ∐_{i ∈ I} X_i`, and let `f : X → G` be the morphism whose restriction to `X_i` is `f_i`, for every `i ∈ I`.
Set `X¹ = X ⊔ X`, let `f¹ : X¹ → G` be the morphism whose restrictions to `X` are respectively `f` and `c ∘ f`. For every
`n > 1`, set*

```text
X^n = X¹ ×_k X^{n−1}    and    f^n = μ ∘ (f¹ ×_k f^{n−1}) : X^n → G.
```

*Then `Γ_G((f_i)_{i ∈ I})` is the reduced subscheme of `G` whose underlying space is the closure of the union of the
`f^n(X^n)`, for `n ⩾ 1`.*

*(iii) For every `k`-scheme `S`, `Γ_G((f_i)_{i ∈ I})_S` is the smallest closed group subscheme of `G_S` majorizing each
of the `f_{i,S} : X_S → G_S`.*

*(iii′) Moreover, `Γ_G((f_i)_{i ∈ I})_S` is the smallest group subscheme of `G_S` majorizing each of the `f_{i,S}`.*[^N.D.E-VI_B-69]

<!-- label: III.VI_B.7.1 -->

[^N.D.E-VI_B-68]: We have replaced, here and in the sequel, the little-used terminology "separable" by the usual terminology "geometrically reduced", cf. EGA IV₂, 4.6.2.

[^N.D.E-VI_B-69]: The original stated (iii′) under the additional hypothesis that `G` be locally of finite type over `k`, but this can be omitted, by VI_A, 0.5.2.

Let us first note that, to prove (i), (iii) and (iii′), by defining `X` and `f` as in (ii), one is reduced to the case
where `I` is reduced to a single element.

Let `H` be the reduced subscheme of `G` with underlying set `⋃_{n ⩾ 1} f^n(X^n)`. Then the family of morphisms
`f^n : X^n → H` is schematically dominant (cf. EGA IV₃, 11.10.4), hence every closed subscheme of `G` which majorizes
the `f^n` also majorizes `H`. Moreover, by loc. cit., 11.10.7, `H` is geometrically reduced. Hence to show (i) and (ii),
it suffices to show that `H` is a group subscheme of `G`, i.e. that the restriction of `c` to `H` and the restriction of
`μ` to `H ×_k H` factor through the injection `H → G`.

Since `H` is geometrically reduced, `H ×_k H` is reduced, and it suffices to verify that `c(H) ⊂ H` and that
`μ(H ×_k H) ⊂ H` (set-theoretically). But by EGA IV₃, 11.10.6, the union of the `f^n_{(H)}(X^n ×_k H)` is schematically
dense in `H ×_k H`. Similarly, for every `n ⩾ 1`, the union of the `f^m_{(X^n)}(X^n ×_k X^m)`, for `m ⩾ 1`, is
schematically dense in `X^n ×_k H`. Hence it suffices to show that
`μ(f^n_{(H)}(f^m_{(X^n)}(X^n ×_k X^m))) ⊂ H` and that `c(f^n(X^n)) ⊂ H`. Now

```text
μ(f^n_{(H)} (f^m_{(X^n)} (X^n ×_k X^m))) = μ((f^n × f^m)(X^n ×_k X^m)) = f^{n+m}(X^{n+m}) ⊂ H;
```

and, since `c(f¹(X¹)) ⊂ f¹(X¹)`, one has, whatever `n`, `c(f^n(X^n)) ⊂ f^n(X^n) ⊂ H`. This proves (i) and (ii).

<!-- original page 381 -->

Let us now show (iii). Let `G′` be a closed group subscheme of `G_S` majorizing `f_S`; we must show that `G′` majorizes
`H_S`, or, what amounts to the same, that `H_S = H_S ×_{G_S} G′`. Set `H′_S = H_S ×_{G_S} G′ = G′ ∩ H_S`. Since `G′` and
`H_S` both majorize the `f^n_S`, the same is true of `H′_S`. Now (EGA IV₃, 11.10.6), since the family of
`f^n : X^n → H` is schematically dominant, the same is true of the family of `f^n_S : X^n_S → H_S`, so that `H′_S`,
which majorizes each of the `f^n_S`, is equal to `H_S` by EGA IV₃, 11.10.1 c). This proves (iii).

Let us show finally that `H_S` is the smallest group subscheme (not necessarily closed) of `G_S` majorizing `f_S`.

Let `G′` be a group subscheme of `G_S` majorizing `f_S`. It must likewise be shown that, if one sets
`H′_S = H_S ×_{G_S} G′`, then `H′_S = H_S`. It suffices for this to show that `H′_S` is closed in `H_S` and to apply
(iii). It suffices therefore to show that `H_S` and `H′_S` have the same underlying set, a fortiori it suffices to
show that, for every `s ∈ S`, `H_s` equals

```text
H′_s := H′_S ×_S κ(s) = H_s ×_{G_s} G′_s.
```

Now, by VI_A, 0.5.2, the group sub-`κ(s)`-scheme `G′_s` is closed in `G_s`. Hence `H′_s` is closed in `H_s`, and then
the preceding reasoning, applied to `H′_s`, to `H_s` and to the `f^n_s`, shows that `H′_s = H_s`. ∎

**Corollary 7.1.1.** [^N.D.E-VI_B-70] *Let `G` be a `k`-group locally of finite type and let `A, B` be two
sub-`k`-groups of `G`, smooth and of finite type, and `i_A` (resp. `i_B`) the inclusion of `A` (resp. `B`) into `G`.
Assume that `B` normalizes `A`. Then `A · B = Γ_G(i_A, i_B)`.*

<!-- label: III.VI_B.7.1.1 -->

[^N.D.E-VI_B-70]: We have added this corollary, to point out this particular case of 7.1.

Indeed, let `H = A ⋊ B` be the semidirect product of `A` and `B` (cf. I, 2.3.5); it is a smooth `k`-group of finite type.
Then the group morphism `u : H → G`, `(a, b) ↦ ab`, is quasi-compact, hence, by 1.2, `u(H) = A · B` is a closed reduced
subscheme of `G`, which is a group in the category `(Sch/k)_red`. Now, by EGA IV₃, 11.10.7, `A · B = u(H)` is
geometrically reduced (since `H` is), so it is a closed subgroup of `G`. Since obviously `A · B ⊂ Γ_G(i_A, i_B)`, the
corollary follows. ∎

**Definitions and remarks 7.2.** [^N.D.E-VI_B-71] *(i) Given a `k`-group `G`, a family `(X_i)_{i ∈ I}` of
geometrically reduced `k`-schemes, and for each `i ∈ I` a `k`-morphism `f_i : X_i → G`, one calls* closed group
subscheme of `G` generated by the family `(f_i)_{i ∈ I}`*, and we shall denote in this number
`Γ_G((f_i)_{i ∈ I})`, the smallest closed group subscheme of `G` majorizing each of the `f_i`. If `X` is a subscheme of `G`, geometrically reduced over `k`, and if `f` is the immersion `X ↪ G`, one writes `Γ_G(X)` instead of `Γ_G(f)`.*

*(i′) With the notations of 7.1 (ii), we shall sometimes set `Γ′_G(f) = ⋃_{n ⩾ 1} f^n(X^n)`. Note that `Γ′_G(f)` is a
subset of `G` stable for the group law (in the sense of 3.0).*

*(ii) It is clear that if `X_1` and `X_2` are two geometrically reduced `k`-schemes and `f_1 : X_1 → G` and `f_2 : X_2 → G` two `k`-morphisms such that the sets `f_1(X_1)` and `f_2(X_2)` are equal, then `Γ_G(f_1) = Γ_G(f_2)`.*

[^N.D.E-VI_B-71]: We have placed in (i′) the point (viii) of the original, and we have highlighted points (vi) and (vii) in the form of Corollary 7.2.1 and Definition 7.2.2 below.

<!-- original page 382 -->

*(iii) Let `E` be a subset of `G` such that the reduced subscheme `E` of `G` is geometrically reduced. One calls* closed
group subscheme of `G` generated by `E`*, denoted `Γ_G(E)`, the group subscheme `Γ_G(i)`, where `i` is the injection of
the reduced subscheme `E` of `G` into `G`.*

*(iv) Since every group subscheme of `G` is closed, by VI_A, 0.5.2,*[^N.D.E-VI_B-72] *one will speak of "generated
group subscheme" instead of "generated closed group subscheme".*

*(v) Let `X` be a geometrically reduced `k`-scheme and `f : X → G` a `k`-morphism. Suppose that `f(X)` contains the unit
element `e` of `G`. Set `X′¹ = X ×_k X` and `f′¹ = μ ∘ (f ×_k (c ∘ f))`, and for `n > 1`,*

```text
X′^n = X′¹ ×_k X′^{n−1}    and    f′^n = μ ∘ (f′¹ ×_k f′^{n−1}).
```

*Then `Γ_G(f)` is the reduced subscheme of `G` whose underlying space is the closure of the union of the `f′^n(X′^n)`,
for `n ⩾ 1`.*

[^N.D.E-VI_B-72]: We have suppressed here the hypothesis that `G` be locally of finite type over `k`.

Indeed, recalling the notation of 7.1 (ii): `X¹ = X ⊔ X` and `X^n = X¹ ×_k X^{n−1}`, for `n ⩾ 2`, one has the following
inclusions, where the first follows from the hypothesis `e ∈ f(X)`:

```text
f^n(X^n) ⊂ f′^n(X′^n) ⊂ f^{2n}(X^{2n}),    for every n ⩾ 1.
```

This shows moreover that, for there to exist an integer `n` such that `f^n(X^n) = Γ_G(f)`, it is necessary and
sufficient that there exist an integer `m` such that `f′^m(X′^m) = Γ_G(f)`.

From Remark 7.2 (v) one deduces the

<!-- label: III.VI_B.7.2 -->

**Corollary 7.2.1.** *Let `X` be a geometrically reduced and geometrically connected `k`-scheme, and `f : X → G` a
`k`-morphism such that `f(X)` contains the neutral element of `G`. Then the `k`-group `Γ_G(f)` is connected, hence
irreducible.*

<!-- label: III.VI_B.7.2.1 -->

Indeed, each of the `X′^n` is then connected, hence the union of the `f′^n(X′^n)` (which all contain the neutral
element) is connected, and the same is true of its closure `Γ_G(f)`. Hence `Γ_G(f)` is irreducible, by VI_A, 2.4 (when
`G`, hence also `Γ_G(f)`, is locally of finite type over `k`) and 2.6.5 (iii) (in the general case). ∎

**Definition 7.2.2.** *Let `G` be a `k`-group.*

*a) Let `A` and `B` be two geometrically reduced group sub-`k`-schemes of `G`. The* commutator group subscheme of `A` and `B` in `G`*, denoted `(A, B)_G` or simply `(A, B)`, is the closed group subscheme of `G` generated by the morphism
`ν : A ×_k B → G` defined by: `(a, b) ↦ aba⁻¹b⁻¹`, for every `k`-scheme `S` and `a ∈ A(S)`, `b ∈ B(S)`.*

*b) Suppose `G` geometrically reduced over `k`. The* derived group of `G`*, denoted `D(G)`,*[^N.D.E-VI_B-73] *is the
group `(G, G)`.*

*N.B. For `G` to be commutative, it is necessary and sufficient that `D(G)` be the unit `k`-group.*

<!-- label: III.VI_B.7.2.2 -->

[^N.D.E-VI_B-73]: We have changed the notation `Der(G)` of the original, in order to avoid any risk of confusion with a space of derivations.

<!-- original page 383 -->

**Reminders 7.3.0.** [^N.D.E-VI_B-74] *Recall that if `φ : Y → Z` is a morphism of `S`-schemes, the image presheaf
`φ(Y)` is the `S`-functor which to every `S′` over `S` associates the subset `φ(Y(S′))` of `Z(S′)`. Note that if `T` is
a subscheme of `Z` and if the inclusion of presheaves `φ(Y) ↪ Z` factors through `T`, i.e. if `φ ∘ h ∈ T(S′)` for every
`S`-morphism `h : S′ → Y`, then set-theoretically `φ(Y) ⊂ T` (take `h = id_Y`), and the converse is true if `Y` is
reduced, since in this case `φ` factors through `T`.*

*Recall also that, by 6.2, if `H` is a closed group sub-`k`-scheme of `G`, then `Centr_G H` and `Norm_G H` are
representable by closed group sub-`k`-schemes of `G`.*

<!-- label: III.VI_B.7.3.0 -->

[^N.D.E-VI_B-74]: We have added these reminders, and modified accordingly, and detailed, the statement of 7.3.

**Corollary 7.3.** *Let `G` be a `k`-group, `X` a geometrically reduced `k`-scheme, `f : X → G` a `k`-morphism.*

*(i) Let `S` be a `k`-scheme and `u` an endomorphism of the `S`-group `G_S`.*

*(a) If one has `u(f_S(X_S)) ⊂ Γ_G(f)_S` (set-theoretically), then the morphism `u : Γ_G(f)_S → G_S` factors through
`Γ_G(f)_S`.*

*(b) If `u` is an automorphism of the `S`-group `G_S` and if one has `u(f_S(X_S)) = f_S(X_S)` (set-theoretically), then
`u` induces an automorphism of `Γ_G(f)_S`. In particular, if an element `g ∈ G(S)` satisfies
`int(g)(f_S(X_S)) = f_S(X_S)` (set-theoretically), then `g ∈ Norm_{G_S}(Γ_G(f)_S)(S)`.*

*(c) If `u ∘ f_S = f_S`, then the restriction of `u` to the subgroup `Γ_G(f)_S` of `G_S` is the identity. In particular,
if an element `g ∈ G(S)` satisfies `int(g)(f_S) = f_S`, then `g ∈ Centr_{G_S}(Γ_G(f)_S)(S)`.*

*(ii) Let `H` be a group subscheme of `G`; then `H` centralizes (resp. normalizes) `Γ_G(f)` if and only if, for every
`S → Spec k` and `h ∈ H(S)`, one has `int(h) ∘ f_S = f_S` (resp. `int(h)(f_S(X_S)) ⊂ Γ_G(f)_S`), i.e. if for every
`S′ → S` and `x ∈ X(S′)`, the elements `h_{S′}` and `f(x)` of `G(S′)` commute (resp. `h_{S′} f(x) h_{S′}⁻¹ ∈ Γ_G(f)(S′)`).*

*(iii) In particular, let `Y` be a second geometrically reduced `k`-scheme and `φ : Y → G` a `k`-morphism. Suppose that,
whatever the `k`-scheme `S′`, for every `x ∈ X(S′)` and `y ∈ Y(S′)`, the elements `φ(y)` and `f(x)` of `G(S′)` commute
(resp. `int(φ(y))(f(x)) ∈ Γ_G(f)(S′)`).*

*Then `Γ_G(φ)` is a sub-`k`-group of `Centr_G Γ_G(f)`, resp. `Norm_G Γ_G(f)`.*

*(iv) If `g` is a `k`-point of `G`, then the `k`-group `Γ_G({g})` is commutative.*

*(v) Let `A` and `B` be two group subschemes of `G` geometrically reduced over `k`. If `A` and `B` are invariant
(resp. characteristic), so is `(A, B)`.*

<!-- label: III.VI_B.7.3 -->

*Proof.* (i) Let us prove (a). Set `Γ_S = Γ_G(f)_S`. Then `u⁻¹(Γ_S)` is a closed group sub-`S`-scheme of `G_S`, hence,
by 7.1 (iii), it suffices to show that `f_S` factors through `u⁻¹(Γ_S)`. Now, since `u(f_S(X_S)) ⊂ Γ_S` and since `X_S`
is reduced, `u ∘ f_S` factors through `Γ_S`, hence `f_S` factors through `u⁻¹(Γ_S)`. This proves (a).

<!-- original page 384 -->

Then the first assertion of (b) is a consequence of (a), applied to `u` and `u⁻¹` (and in fact it suffices to assume
that `u(f_S(X_S)) ⊂ Γ_S` and `u⁻¹(f_S(X_S)) ⊂ Γ_S`), and the second assertion is the particular case where
`u = int(g)`.

Let us prove (c). Consider the morphism of `S`-groups `G_S → G_S ×_S G_S`, `g ↦ (u(g), g)` and let `H` be the inverse
image of the diagonal; it is a group subscheme of `G_S`. Since `G` is separated over `k` (VI_A 0.3), `G_S` is separated
over `S`, hence `H` is closed in `G_S`. As, by hypothesis, `H` majorizes `f_S`, it contains `Γ_G(f)_S`, by 7.1 (iii).
This proves the first assertion of (c), and the second is the particular case where `u = int(g)`.

Let us prove (ii). Set `Γ = Γ_G(f)` and let `i` denote the inclusion `Γ ↪ G`. Then `H` is contained in `N = Norm_G(Γ)`
if and only if, for every `k`-scheme `S` and `h ∈ H(S)`, one has `int(h)(Γ_S) ⊂ Γ_S` (this condition applied to `h` and
`h⁻¹` entailing that `int(h)(Γ_S) = Γ_S`); and by (i)(a) this is the case if and only if `int(h)(f_S(X_S)) ⊂ Γ_S`.

Similarly, `H` is contained in `C = Centr_G(Γ)` if and only if, for every `k`-scheme `S` and `h ∈ H(S)`, one has
`int(h) ∘ i_S = i_S`, and by (i)(c) this is the case if and only if `int(h)(f_S) = f_S`. This proves (ii).

Let us prove (iii). Taking (ii) into account, the hypothesis entails that `φ` factors through `C` (resp. `N`); since the
latter is a closed subgroup of `G`, by 6.2, it therefore contains `Γ_G(f)`, by 7.1 (i).

Assertion (iv) follows from (iii), when one takes for `f` and `φ` the closed immersion `Spec k ↪ G` defined by `g`: in
this case, for every `k`-scheme `S`, `X(S)` and `Y(S)` have only one point, which is sent by `f` (resp. `φ`) to `g`.

Let us finally show (v). Let `ν` be the morphism `G × G → G`, `(g, h) ↦ ghg⁻¹h⁻¹` and let `ν′` be its restriction to
`A × B`; by definition (7.2.2), `(A, B) = Γ_G(ν′)`. Let `S` be a `k`-scheme, and `u` an inner automorphism (resp. an
automorphism of `S`-group) of `G_S`. One has `u ∘ ν_S = ν_S ∘ (u × u)`. On the other hand, the hypothesis entails that
`u` induces an automorphism `u_1` of `A_S` (resp. `u_2` of `B_S`), hence

```text
u(ν′_S(A_S ×_S B_S)) = ν′_S(u_1(A_S) ×_S u_2(B_S)) = ν′_S(A_S ×_S B_S).
```

Hence, by (i)(b), `u` induces an automorphism of `(A, B)_S`. This proves (v). ∎

**Proposition 7.4.** *Let `G` be a `k`-group locally of finite type, `X` a `k`-scheme of finite type, geometrically
reduced and geometrically connected, and `f : X → G` a `k`-morphism such that `f(X)` contains the neutral element `e`
of `G`. Then, with the notations of 7.1 (ii), there exists an integer `N` such that one has (set-theoretically):*

```text
f^N(X^N) = Γ_G(f).
```

<!-- label: III.VI_B.7.4 -->

By 7.1 (iii) and EGA IV₂, 2.6.1, we may suppose `k` algebraically closed. By Corollary 7.2.1, we may suppose `G = G⁰`;
finally, it suffices to show that there exists an integer `N` such that one has `f′^N(X′^N) = Γ_G(f)`, with the
notations of 7.2 (v).

*First case.* Suppose `X` irreducible. Then the `f′^n(X′^n)` form an increasing sequence of irreducible closed sets in
the space `G`, which is noetherian, since `G = G⁰` is

<!-- original page 385 -->

of finite type over `k` (VI_A 2.4). Hence this sequence is stationary, and there exists an integer `m` such that
`f′^m(X′^m) = Γ_G(f)`.

Moreover, since `X` and `G` are of finite type over `k`, the morphisms `f′^n` are of finite type over `k`. Consequently,
`f′^m(X′^m)` is constructible in `G` (EGA IV₁, 1.8.5), hence contains an open `U` of its closure `Γ_G(f)` (EGA 0_IV,
9.2.3). Then, by VI_A 0.5, one has:

```text
Γ_G(f) ⊂ U · U ⊂ f′^{2m}(X′^{2m}) ⊂ Γ_G(f),
```

whence `f′^{2m}(X′^{2m}) = Γ_G(f)`.

*Second case.* Suppose `X` has exactly two irreducible components `A_1` and `A_2`. Then, since `X` is connected and `k`
algebraically closed, there exists `a ∈ (A_1 ∩ A_2)(k)`. Hence the four irreducible parts `A_i ×_k A_j` (`i, j = 1, 2`)
cover `X ×_k X`, and the image of each of them under the morphism `f′¹ = μ ∘ (f ×_k (c ∘ f))` contains `e`. If
`f′¹_{ij}` denotes the restriction of `f′¹` to the reduced subscheme `A_i ×_k A_j`, set

```text
Y = (A_1 ×_k A_1) ×_k (A_1 ×_k A_2) ×_k (A_2 ×_k A_2) ×_k (A_2 ×_k A_1)    and
g = μ ∘ (μ ∘ (f′¹_{11} ×_k f′¹_{12}) ×_k μ ∘ (f′¹_{22} ×_k f′¹_{21})).
```

Then `Y` is irreducible, reduced and of finite type, hence we just saw that there exists an integer `m` such that
`g′^m(Y′^m) = Γ_G(g)`. Now, for every `n ⩾ 1`, one has
`f′^n(X′^n) ⊂ g′^n(Y^n) ⊂ f′^{4n}(X′^{4n})`, whence `Γ_G(f) = Γ_G(g)` and `f′^{4m}(X′^{4m}) = Γ_G(f)`.

*General case.* Let us argue by induction on the number of irreducible components of `X` (this number is finite since
`X`, being of finite type over `k`, is noetherian). Suppose the proposition proved in the case where `X` has at most
`r − 1` irreducible components, and suppose it has `r`, namely `A_1, …, A_r`. Then `e` belongs to the image of one of
the `A_i`; suppose for example that `e ∈ f(A_1)`. Set then `Y = Γ_G(f_r)`, where `f_r` denotes the restriction of `f` to
the reduced subscheme `X_r = A_1 ∪ … ∪ A_{r−1}` (we suppose the numbering of the `A_i` chosen so that this scheme is
connected, which is always possible). Then `Y` is a subgroup of `G`, closed, reduced and irreducible, by Corollary
7.2.1.

Set `Z = f(A_r)`, and let `T = Y ∪ Z`, equipped with the closed reduced subscheme structure, and `i` the injection of
`T` into `G`. It is clear (7.2 (ii)) that `Γ_G(i) = Γ_G(f)` and that `T` is connected (because since `X` is connected,
`A_1 ∪ … ∪ A_{r−1}` and `A_r` have in common a point `a`, and `Y` and `Z` have in common the point `f(a)`). Moreover,
`e ∈ T`, and `T` has at most two irreducible components, since `Y` and `Z` are irreducible. By the induction
hypothesis, there exists an integer `m` such that one has `f′^m_r(X′^m_r) = Γ_G(f_r) = Y`. Since `X = X_r ∪ A_r` and
since `Z = f(A_r)` is contained in `f′^m(X′^m)` (since `e ∈ f(A_1)`), one therefore has:

```text
f(X) ⊂ Y ∪ Z ⊂ f′^m(X′^m).
```

On the other hand, since `T` has at most two irreducible components, one has already seen that there exists an integer
`p` such that `i′^p(T′^p) = Γ_G(i) = Γ_G(f)`. Now, `T ⊂ f′^m(X′^m)`, hence `f′^{mp}(X′^{mp}) = Γ_G(f)`, and one shows,
as in the first case, that this last equality entails `f′^{2mp}(X′^{2mp}) = Γ_G(f)`. ∎

<!-- original page 386 -->

**Lemma 7.5.** *Let `S` be a scheme, `G` an `S`-group scheme, `X` an `S`-prescheme, `f : X → G` an `S`-morphism. Suppose
that `X` and `G` are locally of finite presentation over `S`, and that for every `s ∈ S` and every maximal point `g` of
`G_s`, there exists a point `x` of `X` such that `f(x) = g` and `f` is flat at `x`. Then the morphism
`μ ∘ (f ×_S f) : X ×_S X → G` is covering for the (fppf) topology.*

<!-- label: III.VI_B.7.5 -->

[^N.D.E-VI_B-75] By EGA IV₃, 11.3.1, the set `V` of points of `X` at which `f` is flat is open and `f|_V` is an open
morphism, hence `U = f(V)` is an open of `G`; moreover, by the hypothesis, `U ∩ G_s` is dense in `G_s`, for every
`s ∈ S`. Denote by `φ` the restriction to `V ×_S V` of `μ ∘ (f ×_S f)`.

[^N.D.E-VI_B-75]: We have detailed the original in what follows.

It suffices to show that `φ` is covering for the (fppf) topology, and for this it suffices to show that `φ` is
faithfully flat and of finite presentation (cf. IV, 6.3.1 (iv)). Now `φ` is equal to the composite
`V ×_S V −→ U ×_S U −→ G`, where the first morphism is faithfully flat and locally of finite presentation, since
`f|_V` is. It therefore suffices to prove that the same is true of the restriction of `μ` to `U ×_S U`.

Now, `G → S` being locally of finite presentation and flat, the same is true of `μ : G ×_S G → G` (which is isomorphic
to the morphism deduced from `G → S` by the base change `G → S`, cf. VI_A 0.1), hence also of the induced morphism
`U ×_S U → G`. To prove that the latter is surjective, it suffices to look fiber by fiber, where it follows from
VI_A 0.5, since `U ∩ G_s` is a dense open of `G_s`, for every `s ∈ S`. ∎

**Remark 7.6.0.** [^N.D.E-VI_B-76] *Let `S` be a scheme, `H` an `S`-group, and `f : X → H` a morphism of `S`-schemes.
The sub-presheaf in groups of `H` generated by the image of `f`, denoted `⟨Im f⟩`, is the sub-`S`-functor in groups of `H` which to every `S`-scheme `S′` associates the subgroup of `H(S′)` generated by `f(X(S′))`. Since each element of this subgroup can be written as a finite product `f(x_1)^{ε_1} ⋯ f(x_n)^{ε_n}`, with `n ∈ ℕ*`, `x_i ∈ X(S′)` and `ε_i = ±1`, one sees therefore that if one sets `X¹ = X ⊔ X` and defines the morphisms `f^n : X^n → H` as in 7.1, then `⟨Im f⟩` is nothing but the image presheaf of the morphism*

```text
f^∞ : X^∞ → H,
```

*where `X^∞ = ∐_{n ⩾ 1} X^n` and `f^∞ : X^∞ → H` is the `S`-morphism whose restriction to each `X^n` is `f^n`.*

<!-- label: III.VI_B.7.6.0 -->

[^N.D.E-VI_B-76]: We have added this definition, which in the original was contained in the statement of Proposition 7.6.

**Proposition 7.6.** [^N.D.E-VI_B-77] *Let `S` be a scheme, `X` a flat `S`-scheme locally of finite presentation over
`S`, `H` an `S`-group, locally of finite presentation over `S` and with reduced fibers, `f : X → H` a morphism of
`S`-schemes, and `f^∞ : X^∞ → H` the `S`-morphism introduced above. The following conditions are equivalent:*

*(i) `H` represents the (fppf) `S`-sheaf associated with the presheaf `⟨Im f⟩`.*

*(ii) `f^∞` is covering for the (fppf) topology.*

[^N.D.E-VI_B-77]: The original stated this result under the hypotheses of the particular case, but the more general form was used implicitly in the proof of 10.12; we have rewritten the statement accordingly.

<!-- original page 387 -->

*(iii) `f^∞` is surjective, i.e. `H = ⋃_{n ⩾ 1} f^n(X^n)`.*

*If moreover `H` is quasi-compact, these conditions are also equivalent to the following:*

*(iv) There exists an integer `n` such that `f^n : X^n → H` is covering for the (fppf) topology (and a fortiori
surjective).*

*This applies in particular in the case where `X` is a `k`-scheme locally of finite type and geometrically reduced, `G`
a `k`-group locally of finite type, `φ : X → G` a morphism of `k`-schemes, `H = Γ_G(φ)`, and `f : X → H` the morphism
induced by `φ`.*

<!-- label: III.VI_B.7.6 -->

*Proof.* The sheaf considered in (i) is the image sheaf of `X^∞` by `f^∞`, hence, by IV 4.4.3, to say that `H`
represents this sheaf is equivalent to saying that `f^∞` is covering, and this implies that `f^∞` is surjective.
Conversely, suppose `f^∞` surjective and let us show that it is then covering for the (fppf) topology.

Let `s ∈ S`, `η` a maximal point of the fiber `H_s`, and `x ∈ X^∞_s` such that `f^∞(x) = η` (such an `x` exists, since
`f^∞` is surjective). Since the fiber `H_s` is reduced, `𝒪_{H_s, η}` is a field, hence `f^∞_s` is flat at the point `x`.
Since `X^∞` and `H` are locally of finite presentation over `S`, and `X^∞` flat over `S`, it follows from the fibrewise
flatness criterion (EGA IV₃, 11.3.10) that `f^∞` is flat at the point `x`. Hence, by Lemma 7.5, the morphism

```text
μ ∘ (f^∞ × f^∞) : X^∞ ×_S X^∞ → H
```

is covering for the (fppf) topology. Now, since `X^n ×_S X^m` is canonically isomorphic to `X^{n+m}`, and that, under
this isomorphism, `μ ∘ (f^n ×_S f^m)` corresponds to `f^{n+m}`, it is clear that `μ ∘ (f^∞ ×_S f^∞)` factors through
`f^∞`, so that `f^∞` is covering for the (fppf) topology. This proves that (iii) ⇒ (ii), whence the equivalence of
conditions (i), (ii) and (iii).

Note moreover that, since the morphisms `X → S` and `H → S` are locally of finite presentation, the same is true of
`f : X → H` (cf. EGA IV₁, 1.4.3 (v)), and as `μ : H ×_S H` is also of finite presentation (cf. VI_A, 0.1), it follows
that each `f^n : X^n → H` is so. Hence, by EGA IV₁, 1.9.5 (viii), the `f^n(X^n)` are ind-constructible parts of `H`.

Suppose moreover `H` quasi-compact (then `S` is also, since `H → S` is surjective). Then, by EGA IV₁, 1.9.9, one
concludes that there exists `p` such that `f^p(X^p) = H`. As before, one then deduces, from the fact that the fibers of
`H` are reduced and from Lemma 7.5, that the morphism `μ ∘ (f^p ×_S f^p) : X^p ×_S X^p → H` is covering for the (fppf)
topology; since this morphism equals `f^{2p} : X^{2p} → H`, this concludes the proof of 7.6. ∎

**Remark 7.6.1.** *Obviously, the equivalent conditions of 7.6 imply that the sheaf `F` considered is representable. The
converse is false in general:*[^N.D.E-VI_B-78] *for example, if `k` is of characteristic 0, let `G = G_{a,k}` and let
`f : Spec k → G` be the morphism given by the point `1` of `G(k)`; then `F` is represented by the constant `k`-group
`ℤ_k`, while `Γ_G(f) = G`, hence the monomorphism `ℤ_k ↪ G` is not surjective.*

*Let us place ourselves, for simplicity, under the hypotheses of the particular case of 7.6, and suppose `F`
representable. Then, by EGA IV₃, 8.14.2, `F` is locally*

[^N.D.E-VI_B-78]: We have detailed the original in what follows.

<!-- original page 388 -->

*of finite presentation over `k`, hence the question is whether the dominant monomorphism `F → Γ_G(f)` is an
isomorphism, or equivalently, a closed immersion. This will be the case, by virtue of 1.4.2, if `F` is quasi-compact,
and, by VI_A, 0.5.1, this will be verified if `F` is connected, hence, in particular (7.2.1), if `X` is connected and if `f(X)` contains the unit element of `G`.*

<!-- label: III.VI_B.7.6.1 -->

**Lemma 7.7.** *Let `k` be an algebraically closed field, `G` a `k`-group locally of finite type, `X` a geometrically
reduced and locally of finite type `k`-scheme, `f : X → G` a `k`-morphism and `H` a group subscheme of `G` such that
`H ⊂ f(X)`. Set*

```text
Γ′ = ⋃_{n ⩾ 1} f^n(X^n),    Γ′_0 = Γ′ ∩ G(k),    H_0 = H(k)
```

*and assume `H_0` is of finite index in `Γ′_0`. Then there exists an integer `m` such that `f^m(X^m) = Γ_G(f)`
(cf. 7.6), and `Γ_G(f)` is the union of finitely many translates of `H`.*

<!-- label: III.VI_B.7.7 -->

For every `n ⩾ 1`, `f^n(X^n)` is an ind-constructible part of `G` (EGA IV₁, 1.9.5 (viii)), the same is therefore true
of `Γ′`, so that, since `G` is a Jacobson scheme, `Γ′_0` is dense in `Γ′`. By hypothesis, there exists a finite sequence
`a_1, …, a_r` of points of `Γ′_0` such that `Γ′_0 = a_1 H_0 ∪ … ∪ a_r H_0`, whence

```text
Γ_G(f) = Γ′ = Γ′_0 = a_1 H_0 ∪ … ∪ a_r H_0 = a_1 H_0 ∪ … ∪ a_r H_0 = a_1 H ∪ … ∪ a_r H,
```

the last equality resulting from the fact that translation by `a_i` is a homeomorphism of `G` onto `G`. One has
therefore `Γ_G(f) = a_1 H ∪ … ∪ a_r H`. On the other hand, it is clear that there exists an integer `p` such that each
of the `a_i` (`1 ⩽ i ⩽ r`) belongs to `f^p(X^p)`. Finally, since `H ⊂ f(X)`, one has, for every `i`:
`a_i H ⊂ f^{p+1}(X^{p+1})`, so that `f^{p+1}(X^{p+1}) = Γ_G(f)`. ∎

**Proposition 7.8.** *Let `G` be a `k`-group locally of finite type, `A` and `B` two geometrically reduced group
sub-`k`-schemes (hence smooth at the generic points of their irreducible components, hence smooth by 1.3) of `G`.
Suppose one of the following conditions a) or b) is satisfied:*

*a) `A` and `B` are invariant and of finite type over `k`.*

*b) `A` is connected and `B` is of finite type over `k`.*

*Then `(A, B)` is of finite type over `k`, and represents the sheaf associated for the (fppf) topology (or (fpqc)) with
the presheaf in groups of commutators of `A` and `B` in `G`. Moreover,*[^N.D.E-VI_B-79] *the `k`-groups `(A, B⁰)` and
`(A⁰, B)` are connected, and one has*

```text
(A, B)⁰ = (A, B⁰) · (A⁰, B).
```

<!-- label: III.VI_B.7.8 -->

[^N.D.E-VI_B-79]: We have made the following precise and, in the proof, detailed the reduction to the case where `k` is algebraically closed.

*Proof.* By 7.6, to show that `(A, B)` is the desired associated sheaf, it suffices to show that there exists an integer
`n` such that `ν^n((A ×_k B)^n) = (A, B)` (notations of 7.2.2). To show this, as well as to show the two other
assertions, we may suppose

<!-- original page 389 -->

`k` algebraically closed. Indeed, let `k̄` be an algebraic closure of `k`. By 7.1 (iii) and VI_A 2.4, one has, with
obvious notations:

```text
(A, B)_{k̄} = (A_{k̄}, B_{k̄}),    ((A, B)⁰)_{k̄} = (A_{k̄}, B_{k̄})⁰,    (A, B⁰)_{k̄} = (A_{k̄}, B⁰_{k̄}),    etc.
```

Consequently, if one shows that `(A_{k̄}, B_{k̄})` is of finite type over `k̄` (resp. that `(A_{k̄}, B⁰_{k̄})` and
`(A⁰_{k̄}, B_{k̄})` are connected, and that the morphism
`(A_{k̄}, B⁰_{k̄}) ×_{k̄} (A_{k̄}, B⁰_{k̄}) → (A_{k̄}, B_{k̄})⁰` is surjective), then the analogous assertions will be
true over `k`, by EGA IV₂, 2.7.1 and 2.6.1.

Let then `B_1, …, B_p` be the connected components of `B` other than the neutral component `B⁰` (these are finite in
number since `B` is supposed of finite type over `k`, hence noetherian), and in case (a), let similarly `A_1, …, A_q`
be those of `A`. (In case (b), one will consider only `A⁰ = A`). Let `ν_{ij}` be the restriction of `ν` to
`A_i ×_k B_j`. Then each of the `A_i` and `B_j` is irreducible (VI_A 2.4.1), so the same is true of `A⁰ ×_k B_j` and
`A_i ×_k B⁰`. Since the neutral element of `G` belongs to `A⁰` and `B⁰`, it belongs to `ν_{0j}(A⁰ ×_k B_j)` and to
`ν_{i0}(A_i ×_k B⁰)`. Then each of the `Γ_G(ν_{0j})` and `Γ_G(ν_{i0})` is connected (7.2.1). Similarly, if `u_{0j}`
(resp. `u_{i0}`) denotes the injection of `Γ_G(ν_{0j})` (resp. `Γ_G(ν_{i0})`) into `G`, then

```text
(A⁰, B) = Γ_G((u_{0j})_{j=0}^p)    and    (A, B⁰) = Γ_G((u_{i0})_{i=0}^q)
```

are connected. Moreover, one easily deduces from 7.4 and the preceding constructions that there exists an index `r`
such that `(A⁰, B)` and `(A, B⁰)` are included in `ν^r((A ×_k B)^r)`. In case b), one has `(A, B) = (A⁰, B)`, and we are
done.

Let us now place ourselves in case (a).[^N.D.E-VI_B-80] We already know that `(A⁰, B)` and `(A, B⁰)` are smooth and
connected sub-`k`-groups of `G`, hence of finite type (cf. VI_A, 2.4). On the other hand, since `A⁰` is a characteristic
subgroup of `A` (cf. VI_A, 2.6.5), it is an invariant subgroup of `G` and hence, by 7.3 (v), `(A⁰, B)` is an invariant
subgroup of `G`, and similarly for `(A, B⁰)`. Hence, by 7.1.1, the subgroup `H` of `G` generated by `(A, B⁰)` and
`(A⁰, B)` is none other than `(A, B⁰) · (A⁰, B)`. In particular, one has therefore `H ⊂ ν^{2r}((A ×_k B)^{2r})`.

Given a part `X` of `G` stable for the group law (cf. 3.0), we shall denote by `X_0` the group of `k`-points of `G`
belonging to `X`. Set `Γ′ = ⋃_{q ⩾ 1} ν^q((A ×_k B)^q)`. Then, by Proposition 7.9 below, one has:

```text
(A⁰, B)_0 = (A⁰_0, B_0),    (A, B⁰)_0 = (A_0, B⁰_0)    and    Γ′_0 = (A_0, B_0),
```

so that `H_0 = (A⁰_0, B_0) · (A_0, B⁰_0)` is of finite index in `Γ′_0` (Bible, Exp. 3, Appendix) since `A⁰` and `B⁰` are
invariant, and `A⁰_0` (resp. `B⁰_0`) is of finite index in `A_0` (resp. `B_0`). We are then in the conditions of Lemma
7.7: since `H ⊂ ν^{2r}((A ×_k B)^{2r})`, there exists an integer `m` such that
`ν^{2rm}((A ×_k B)^{2rm}) = (A, B)`, and there exists a finite sequence `a_1, …, a_n` of `k`-points of `G` such that:
`(A, B) = a_1 H ∪ … ∪ a_n H`. Then, since `H` is of finite type over `k`, each of the `a_i H` is quasi-compact, hence
their union `(A, B)` is quasi-compact, hence of finite type over `k`. Since `H` is irreducible, the same is true of
each of the `a_i H`, and since `e ∈ H`, it is clear that `H = (A, B)⁰`. ∎

[^N.D.E-VI_B-80]: We have detailed the original in what follows, taking into account the addition 7.1.1.

<!-- original page 390 -->

**Proposition 7.9.** *Let `k` be an algebraically closed field, `G` a `k`-group locally of finite type.*

*(i) Let `A` and `B` be two ind-constructible parts of `G`. Denote by `A_0` the set of rational points of `G` belonging
to `A`. Then `(A · B)_0 = A_0 · B_0`, the second product being taken in the group `G(k)`.*

*(ii) Let `X` be a geometrically reduced and locally of finite type `k`-scheme, and `f : X → G` a `k`-morphism. Set
`Γ′_G(f) = ⋃_{n ⩾ 1} f^n(X^n)`. Then `Γ′_G(f)_0` is the subgroup of `G(k)` generated by `f(X)_0`.*

*(iii) In particular, let `A` and `B` be two smooth group subschemes of `G`; set
`Γ′ = ⋃_{n ⩾ 1} ν^n(A ×_k B)^n` (notations of 7.2.2). Then `Γ′_0` is the group of commutators of `A(k)` and `B(k)` in
`G(k)`.*

<!-- label: III.VI_B.7.9 -->

Let us prove (i). It is clear that `A_0 · B_0 ⊂ (A · B)_0`. Conversely, let `z ∈ (A · B)_0`. Then `μ⁻¹(z)` is a closed
subset of `G ×_k G`, and `A ×_k B` (cf. 3.0) is an ind-constructible part of `G ×_k G`, so that
`μ⁻¹(z) ∩ (A ×_k B)` is a non-empty ind-constructible part of `G ×_k G`; by EGA IV₃, 10.4.8, it therefore contains a
rational point of `G ×_k G`, whose projections `x` and `y` are rational points of `G` such that `x ∈ A`, `y ∈ B` and
`x · y = z`, so that `(A · B)_0 = A_0 · B_0`.

To prove (ii), note that, `f^n` being locally of finite type, `f^n(X^n)` is an ind-constructible part of `G` (EGA IV₄,
1.9.5 (viii)). Assertion (i) then allows one to show by induction that, if one sets `A = f(X)_0`, one has:
`f^n(X^n)_0 = (A ∪ A⁻¹)^n`, and consequently,

```text
Γ′_G(f)_0 = ⋃_{n ⩾ 1} f^n(X^n)_0 = ⋃_{n ⩾ 1} (A ∪ A⁻¹)^n,
```

which is the subgroup of `G(k)` generated by `A = f(X)_0`.

Finally, (iii) follows from (ii) and the definitions. ∎

**Corollary 7.10.** *Under the conditions of 7.8, if `k` is algebraically closed, then `(A, B)(k)` is the commutator
subgroup of `A(k)` and `B(k)` in `G(k)`.*

<!-- label: III.VI_B.7.10 -->

Indeed, it suffices to apply 7.9 (iii), 7.8 and 7.6.

## 8. Solvable or nilpotent group schemes

<!-- label: III.VI_B.8 -->

### 8.1.

Let `𝒞` be a category equipped with a topology `T` (cf. IV § 4). For every presheaf `P` on `𝒞`, we denote by `P^♭` the
associated sheaf.

Let `G` be a presheaf in groups on `𝒞`, `A` and `B` two sub-presheaves in groups of `G`, and let `Comm(A, B)` be the
presheaf in groups of commutators of `A` and `B` in `G`; i.e., for every `S ∈ Ob 𝒞`, `Comm(A, B)(S)` is the subgroup of
`G(S)` generated by the commutators `aba⁻¹b⁻¹`, with `a ∈ A(S)` and `b ∈ B(S)`. We write

```text
Comm_T(A, B) = Comm(A, B)^♭.
```

In the proof of 8.2, we shall need the following results.[^N.D.E-VI_B-81]

[^N.D.E-VI_B-81]: These results are mentioned without proof in the original; we have highlighted them in the form of Lemmas 8.1.1 and 8.1.2, and detailed the proofs.

**Lemma 8.1.1.** *Let `A ⊂ G` be sheaves in groups, with `A` invariant in `G`.*

*(i) `Comm_T(G, A)` is the smallest invariant sub-sheaf in groups `C` of `G` such that the sheaf `(A/C)^♭`, associated
with the quotient presheaf `A/C`, is central in `(G/C)^♭`.*

*(ii) In particular, `Comm_T(G, G)` is the smallest invariant sub-sheaf in groups `C` of `G` such that the quotient sheaf
`(G/C)^♭` is commutative.*

<!-- label: III.VI_B.8.1.1 -->

Obviously, (ii) is the particular case `A = G` of (i), so it suffices to show (i). Let `C` be a sub-sheaf in groups of
`A`, invariant in `G`, and such that the quotient sheaf `(A/C)^♭` is central in `(G/C)^♭`. By Lemma IV 4.4.8.1, the
presheaves `A/C` and `G/C` are separated, hence, by IV 4.3.11, all the morphisms in the diagram below are monomorphisms:

```text
A/C ────→ G/C
 │          │
 ↓          ↓
(A/C)^♭ ─→ (G/C)^♭
```

Since `(A/C)^♭` is central in `(G/C)^♭`, then `A/C` is central in `G/C`, whence `Comm(G, A) ⊂ C`, and hence `C` contains
`Comm_T(G, A)`, by IV 4.3.12.

Conversely, `Comm(G, A)` is a sub-presheaf in groups of `A`, invariant in `G`, and separated (cf. IV 4.3.1, N.D.E. (24)),
hence, by IV 4.4.8.2 (i) and IV 4.3.11, `C = Comm_T(G, A)` is a sub-sheaf in groups of `A`, invariant in `G` and
containing `Comm(G, A)`. Consequently, the presheaf `A/C` is central in `G/C` and hence, by IV 4.4.8.2 (ii), `(A/C)^♭`
is central in `(G/C)^♭`. This proves Lemma 8.1.1. ∎

**Lemma 8.1.2.** *Let `G` be a sheaf in groups, `A, B` two sub-presheaves in groups of `G`.*

*(i) The morphism `τ : Comm(A, B) → Comm(A^♭, B^♭)` is a covering monomorphism.*

*(ii) Consequently, one has an isomorphism*

```text
Comm_T(A, B) ⥲ Comm_T(A^♭, B^♭).
```

<!-- label: III.VI_B.8.1.2 -->

*Proof.* (i) As `A` (resp. `B`) is a sub-presheaf of `G`, then `A^♭` (resp. `B^♭`) is a sub-presheaf of `G` containing
`A` (resp. `B`), and it follows that `τ` is a monomorphism.

Let us show that `τ` is covering. Let `S ∈ Ob 𝒞` and `g ∈ Comm(A^♭, B^♭)(S)`. Then, there exists an integer `n ⩾ 1` and,
for `i = 1, …, n`, elements `a′_i ∈ A^♭(S)`, `b′_i ∈ B^♭(S)`, and `ε_i ∈ {±1}`, such that

```text
g = (a′_1, b′_1)^{ε_1} ⋯ (a′_n, b′_n)^{ε_n},
```

<!-- original page 392 -->

where `(a, b)` denotes the commutator `aba⁻¹b⁻¹`, and there exists a refinement `R` of `S` such that `a′_i ∈ A(R)` and
`b′_i ∈ B(R)` for every `i`. Then `g` is the composite morphism

```text
R ─(a′_1, …, b′_n)→ (A × B)^n ─Φ_{ε_1, …, ε_n}→ Comm(A, B),
```

where `Φ = Φ_{ε_1, …, ε_n}` is the morphism defined set-theoretically by:

```text
Φ(a_1, b_1, …, a_n, b_n) = (a_1, b_1)^{ε_1} ⋯ (a_n, b_n)^{ε_n},
```

for every `T ∈ Ob 𝒞` and `a_i ∈ A(T)`, `b_i ∈ B(T)`. This shows that `g ∈ Comm(A, B)(R)` and it follows, as in the proof
of IV 4.3.11 (i), that `Comm(A, B) → Comm(A^♭, B^♭)` is covering.

As `Comm(A^♭, B^♭) → Comm(A^♭, B^♭)^♭` is also a covering monomorphism (IV 4.3.11 (iv)), the same is true of
`Comm(A, B) → Comm(A^♭, B^♭)^♭`, hence, by IV 4.3.12, one obtains an isomorphism:

```text
Comm(A, B)^♭ ⥲ Comm(A^♭, B^♭)^♭.
```

This proves Lemma 8.1.2. ∎

**Proposition 8.2.** *Let `𝒞` be a category, `T` a topology on `𝒞`, `G` a sheaf in groups on `𝒞`, `n` an integer `⩾ 0`.
The following conditions are equivalent:*

*(i) If one sets `K_0 = G`, and for `p ⩾ 1`, `K_p = Comm(K_{p−1}, K_{p−1})` (resp. `K_p = Comm(G, K_{p−1})`), then `K_n`
is the unit presheaf in groups.*

*(ii) If one sets `K′_0 = G`, and for `p ⩾ 1`, `K′_p = Comm_T(K′_{p−1}, K′_{p−1})` (resp. `K′_p = Comm_T(G, K′_{p−1})`),
then `K′_n` is the unit sheaf in groups.*

*(iii) There exists a sequence `G = H_0 ⊃ H_1 ⊃ … ⊃ H_n` of invariant sub-sheaves of `G`, such that, whatever `i`, the
quotient sheaf `H_i/H_{i+1}` is commutative (resp. central in `G/H_{i+1}`), and `H_n` is the unit sheaf.*

<!-- label: III.VI_B.8.2 -->

It is clear that `K_n ⊂ K′_n`; consequently (ii) entails (i). Let us show that (i) entails (ii). One has
`K′_1 = Comm_T(G, G) = K^♭_1`, and one deduces by induction from Lemma 8.1.2 that `K′_p = K^♭_p` for every `p`.
Consequently, if `K_n` is the unit presheaf, then `K′_n = K^♭_n` is the unit sheaf.

Finally, conditions (ii) and (iii) are equivalent by Lemma 8.1.1. ∎

**Definition 8.2.1.** *When these conditions are satisfied, the sheaf `G` is said to be* solvable of class `n` *(resp.*
nilpotent of class `n`*). When there exists an integer `n` such that these conditions are satisfied, one says that `G`
is* solvable *(resp.* nilpotent*).*

*Note that, by condition (i), this does not depend on the topology `T`.*

<!-- label: III.VI_B.8.2.1 -->

**Proposition 8.3.** *Let `k` be a field, `S` a non-empty `k`-scheme, `Ω` an algebraically closed extension of `k`, `G` a
smooth `k`-group of finite type. The following conditions are equivalent:*

*(i) `G` is solvable of class `n` (resp. nilpotent of class `n`).*

*(ii) `G ×_k S` is solvable of class `n` (resp. nilpotent of class `n`).*

*(iii) The group `G(Ω)` is solvable of class `n` (resp. nilpotent of class `n`).*

<!-- original page 393 -->

*(iv) If one sets `K_0 = G` and considers, for `p ⩾ 1`, the `k`-groups `K_p = (K_{p−1}, K_{p−1})` (resp. `K_p = (G, K_{p−1})`) (cf. 7.2.2), then `K_n` is the unit `k`-group.*

<!-- label: III.VI_B.8.3 -->

The equivalence of conditions (i) and (ii) follows from Proposition 8.2, given that the formation of the presheaf in
groups of commutators commutes with base change (IV 4.1.3).

The equivalence of (i) and (iv) follows from the fact that, by 7.8, the `k`-group
`K_p = (K_{p−1}, K_{p−1})` (resp. `K_p = (G, K_{p−1})`) represents the sheaf `Comm_T(K_{p−1}, K_{p−1})`
(resp. `Comm_T(G, K_{p−1})`), where `T` is the (fppf) (or (fpqc)) topology.

To show that conditions (iii) and (iv) are equivalent, one may suppose `k = Ω`, and then the equivalence of conditions
(iii) and (iv) follows from 7.10. ∎

**Proposition 8.4.** *Let `G` be an `S`-group of finite presentation, such that for every `s ∈ S`, `G_s` is smooth over
`κ(s)`. Let `T` be the set of `s ∈ S` such that `G_s` is solvable (resp. nilpotent).*

*(i) Then `T` is locally constructible in `S`.*

*(ii) If one moreover assumes `G` flat and separated over `S` (i.e. when `G` is smooth, quasi-compact and separated over
`S`), then `T` is closed in `S`.*

<!-- label: III.VI_B.8.4 -->

*Proof.* It is clear that one may suppose `S` affine with ring `A`. There exists then, by 10.1 and 10.10 b),[^VI_B-8-1] a
noetherian subring `A′` of `A` and an `A′`-group of finite type `G′` such that `G′ ⊗_{A′} A` is isomorphic to `G`. By
EGA IV₃, 11.2.6 and 8.10.5,[^N.D.E-VI_B-82] if `G` is flat and separated over `S`, one may suppose `G′` flat and
separated over `S′ = Spec A′`.[^N.D.E-VI_B-83] As `G` is of finite presentation over `S`, then (EGA IV₃, 9.7.7) the set
of `s ∈ S` such that `G_s` is geometrically reduced (or, equivalently, smooth over `κ(s)`) is locally constructible.
Hence, by EGA IV₃, 9.3.3, one may suppose that, for every `s′ ∈ S′`, `G′_{s′}` is smooth over `κ(s′)`. On the other
hand, if `s′` denotes the image of `s` in `S′`, one has: `G′_{s′} ⊗_{κ(s′)} κ(s) ≃ G_s`. Hence, by 8.3, for `G_s` to be
solvable (resp. nilpotent), it is necessary and sufficient that the same be true of `G′_{s′}`. We are therefore reduced
to the case where `S` is a noetherian affine scheme.

[^VI_B-8-1]: We shall make use in the course of this proof of results established in number 10, which do not depend, any more than number 9, on the present n° 8.

[^N.D.E-VI_B-82]: We have corrected 10.8.5 to 8.10.5.

[^N.D.E-VI_B-83]: We have detailed what follows.

Let us show then that `T` is constructible. By applying the criterion (EGA 0_III, 9.2.3), one sees, reasoning as
before, that one is reduced to showing that, in the case where `S` is noetherian and integral, either `T` or `S − T`
contains a non-empty open of `S`.

Suppose then `S` integral and noetherian, with generic point `η`. Set, whatever `s ∈ S`, `K⁰_s = G_s`, and
`K^p_s = (K^{p−1}_s, K^{p−1}_s)` (resp. `K^p_s = (G, K^{p−1}_s)`). Let us first show that the sequence of closed
subschemes `K^p_η` is stationary. It follows from 7.3 (v) that each of the `K^p_η` is invariant, hence the sequence of
`K^p_η` is decreasing; this sequence is then stationary since `G_η` is noetherian; there exists therefore an integer
`n` such that, for every `p ⩾ n`, one has: `K^p_η = K^n_η`.

On the other hand, by 10.12.1 and 10.13, there exists a non-empty open `S′` of `S` and

<!-- original page 394 -->

an `S′`-group of finite presentation `D` such that for every `s ∈ S′`, one has `D_s = K^n_s` and
`(D_s, D_s) = D_s` (resp. `(G_s, D_s) = D_s`). We may suppose `S′ = S`. Then, whatever `s ∈ S`, and whatever `p ⩾ n`,
one has `D_s = K^p_s`, so that `G_s` is solvable (resp. nilpotent) if and only if `D_s` is isomorphic to the unit
`κ(s)`-group.

But by EGA IV₃, 9.6.1 (xi), the set of `s ∈ S` such that the structural morphism `D_s → Spec κ(s)` is an isomorphism is
constructible,[^N.D.E-VI_B-84] hence is either rare or contains a non-empty open of `S`. We have therefore obtained
that `T` is locally constructible.

[^N.D.E-VI_B-84]: Taking into account the fact that `S` is supposed affine, hence quasi-compact and quasi-separated (cf. EGA 0_III, 9.1.12).

Let us show that if, moreover, `G` is flat and separated over `S`, then `T` is closed. Since `T` is locally
constructible, for `T` to be closed, it is necessary and sufficient that `T` be stable under specialization (cf. EGA
IV₁, 1.10.1).

Let then `s ∈ S` and `s′` a specialization of `s` in `S`. Since one has reduced to the case where `S` is noetherian,
then, by EGA II, 7.1.9, there exists a discrete valuation ring `A` and a morphism `Spec(A) → S` such that `s`
(resp. `s′`) is the image of the generic point `α` (resp. of the closed point `a`) of `Spec(A)`. It suffices then to
show that if one sets `G′ = G ⊗_S A`, and if `G′_α` is solvable (resp. nilpotent), then so is `G′_a`. Note that, since
`G` is flat and separated over `S`, `G′_α` is flat and separated over `A`, so we are reduced to the case where `S` is
the spectrum of a discrete valuation ring `A`.

Then, since `G_α` is supposed solvable (resp. nilpotent), there exists an integer `q` such that `K^q_α` (with the
notations introduced above) is isomorphic to the unit `κ(α)`-group. For every `n`, let `K̄^n_α` denote the schematic
closure (in the sense of EGA IV₂, 2.8.5) of `K^n_α` in `G`. Let us show, by induction on `p`, that
`(K̄^p_α)_a ⊃ K^p_a`. Note first that, since `G` is flat over `A`, then `G_α` is equal to `G`̄ (EGA IV₂, 2.8.5), so
`(K̄⁰_α)_a = K⁰_a`.

Let `p ⩾ 0`. Suppose we have established that `K^p_a ⊂ (K̄^p_α)_a`, and denote by `ν_a, ν_α, ν, ν̄_a` the following
morphisms, defined as in 7.2.2:

```text
                solvable case                                   nilpotent case
ν_a : K^p_a ×_{κ(a)} K^p_a → G_a,                   resp.       G_a ×_{κ(a)} K^p_a → G_a,
ν_α : K^p_α ×_{κ(α)} K^p_α → G_α                    resp.       G_α ×_{κ(α)} K^p_α → G_α,
ν   : K̄^p_α ×_A K̄^p_α → G,                        resp.       G ×_A K̄^p_α → G,
ν̄_a : (K̄^p_α)_a ×_{κ(a)} (K̄^p_α)_a → G_a,         resp.       G_a ×_{κ(a)} (K̄^p_α)_a → G_a.
```

Since `ν_α` factors through `K^{p+1}_α`, then `ν` factors through `K̄^{p+1}_α`, which is obviously a group subscheme of
`G`, hence `K̄^{p+1}_α` contains `Γ_G(ν)`. By 7.1 (iii), one has `Γ_G(ν)_a = Γ_{G_a}(ν̄_a)`; and, by the induction
hypothesis,

```text
K^p_a ×_{κ(a)} K^p_a ⊂ (K̄^p_α)_a ×_{κ(a)} (K̄^p_α)_a    resp.    G_a ×_{κ(a)} K^p_a ⊂ G_a ×_{κ(a)} (K̄^p_α)_a,
```

so that `K^{p+1}_a = Γ_{G_a}(ν_a) ⊂ Γ_{G_a}(ν̄_a) = Γ_G(ν)_a ⊂ (K̄^{p+1}_α)_a`.

<!-- original page 395 -->

But since `K^q_α` is isomorphic to the unit `κ(α)`-group, and the unit `A`-group is flat over `A` and is isomorphic to
a closed subscheme of `G` (since `G` is separated over `A`, cf. 5.1), it follows from EGA IV₂, 2.8.5 that the schematic
closure `K̄^q_α` is isomorphic to the unit `A`-group. As we just saw that `K^q_a ⊂ (K̄^q_α)_a`, this entails that
`K^q_a` is isomorphic to the unit `κ(a)`-group, so that `G_a` is solvable (resp. nilpotent). ∎

## 9. Quotient sheaves

<!-- label: III.VI_B.9 -->

The present number is limited essentially to a reminder, in the particular case of homogeneous spaces of groups, of
well-known general facts about passage to the quotient by flat equivalence relations (cf. Exp. IV).

**Definition 9.1.** *Given a monomorphism `u : G′ → G` of `S`-groups, one denotes by `G/G′` (resp. `G′\G`), and calls*
right (resp. left) quotient sheaf of `G` by `G′`*, the sheaf (for the (fpqc) topology) quotient of `G` by the equivalence
relation defined by the monomorphism:*

```text
G ×_S G′ ─δ ∘ (id_G × u)→ G ×_S G    (resp. G′ ×_S G ─γ ∘ (u × id_G)→ G ×_S G),
```

*where `δ` (resp. `γ`) denotes the automorphism of `G ×_S G` defined by `(g, h) ↦ (g, gh)` (resp. `(h, g) ↦ (hg, g)`) for
`g, h ∈ G(T)`.*

<!-- label: III.VI_B.9.1 -->

**Proposition 9.2.** *Let `u : G′ → G` be a monomorphism of `S`-groups. Suppose that `G/G′` is representable by an
`S`-scheme `G″`. Then:*

*(i) The canonical morphism `p : G → G″` is covering for the (fpqc) topology.*

*(ii) If one sets `ε″ = p ∘ ε` (this morphism is called the unit section of `G″`), the following diagrams are cartesian:*

```text
G ×_S G′ ─μ ∘ (id_G × u)→ G              G′ ──u──→ G
   │                      │              │         │
  pr_1                    p              π′        p
   │                      │              │         │
   ↓                      ↓              ↓         ↓
   G ────────p────────→ G″               S ──ε″──→ G″.
```

*In particular, `u` is an immersion.*

*(iii) There exists on `G″` a unique structure of `S`-scheme with left operator group `G`, such that `p` is a morphism of
`S`-schemes with operator group `G`.*

*(iv) If one moreover supposes `G′` invariant in `G`, there exists on `G″` a unique structure of `S`-group such that `p`
is a morphism of `S`-groups.*

*(v) Let `S_0` be an `S`-scheme; set `G_0 = G ×_S S_0`, and `G′_0 = G′ ×_S S_0`; then `G_0/G′_0` is representable by
`G″_0 = G″ ×_S S_0`.*[^N.D.E-VI_B-85]

*(vi) Let `P` be a property for an `S`-morphism. Suppose `P` stable under base change; then if `p : G → G″` satisfies
`P`, the same is true of the structural morphism `π′ : G′ → S`.*

[^N.D.E-VI_B-85]: i.e., the quotient is universal, cf. Exp. IV § 3.

<!-- original page 396 -->

*(vii) Let `P` be a property for an `S`-morphism. Suppose `P` is local in nature for the (fpqc) topology (cf. 2.0 and
2.1.2). Then, for the morphism `p : G → G″` to satisfy `P`, it is necessary and sufficient that the same be true of
`π′ : G′ → S′`.*

*(viii) Let `P` be a property for an `S`-morphism; suppose `P` is local in nature for the (fpqc) topology, and stable
under composition; then, if the structural morphisms `G″ → S` and `G′ → S` satisfy `P`, the same is true of the
structural morphism `G → S`.*

*(ix) Suppose `G` reduced; then `G″` is reduced.*

*(x) For `G″` to be separated over `S`, it is necessary and sufficient that `u` (or, equivalently, `ε″`) be a closed
immersion.*

*(xi) For `G′` to be flat over `S`, it is necessary and sufficient that `p` be a flat morphism (or, equivalently,
faithfully flat).*

*In this case, for `G″` to be flat over `S`, it is necessary and sufficient that `G` be flat over `S`.*

*(xii) For `G′` to be flat and locally of finite presentation over `S`, it is necessary and sufficient that
`p : G → G″` be faithfully flat and locally of finite presentation.*

*In this case, for `G″` to be locally of finite presentation (resp. locally of finite type, of finite type, smooth,
étale, unramified, locally quasi-finite, quasi-finite) over `S`, it suffices that the same be true of `G` over `S` (and
the condition is also necessary in the first two cases, cf. (viii)).*

*(xiii) Suppose `G′` flat and of finite presentation over `S`.*

*a) Then `p` is of finite presentation and faithfully flat;*

*b) moreover, for `G` to be of finite presentation over `S`, it is necessary and sufficient that the same be true of
`G″`.*

<!-- label: III.VI_B.9.2 -->

Recall that the equivalence relation under consideration is universally effective (IV 4.4.9). Then assertions (i),
(iii), (iv), (v) and the first assertion of (ii) follow from IV 4.4.3, 5.2.2, 5.2.4, 3.4.5 and 3.3.2 (iii). The second
assertion of (ii) follows from the first, as the following cartesian diagram shows, since `(G ×_S G′) ×_G S` is
isomorphic to `G′`:

```text
G′ ─((ε ∘ π′), id_{G′})→ G ×_S G′ ─μ ∘ (id_G × u)→ G
│                          │                       │
π′                         pr_1                    p
│                          │                       │
↓                          ↓                       ↓
S ────────ε────────────→  G ─────────p──────────→ G″.
```

Finally, it is clear that `ε″` is an `S`-section of `G″`, hence an immersion (EGA I, 5.3.13); by the preceding
cartesian diagram, the same is true of `u`, which completes the proof of (ii). Moreover, (vi) is an immediate
consequence of the second cartesian diagram of (ii).

Let us show (vii). By (i), `p` is covering for the (fpqc) topology; hence, by (ii), to show that `p` satisfies `P`, it
suffices to show that the first projection `pr_1 : G ×_S G′ → G` satisfies `P`, which follows from the fact that `P` is
stable under base change, since `pr_1` comes from `π′` by base change.

<!-- original page 397 -->

It is clear that (viii) follows from (vii), since `π = π″ ∘ p`, where `π″ : G″ → S` denotes the structural morphism.

Let us show (ix). By (i), `p` is an epimorphism; since `G` is reduced, `p` factors through the immersion
`G″_red → G″`, which is therefore also an epimorphism, hence an isomorphism (IV 4.4.4).

Let us show (x). If `G″` is separated over `S`, then `ε″` is a closed immersion, by EGA I, 5.4.6. On the other hand,
one saw in (ii) that `ε″` is a closed immersion if and only if `u` is. Finally, if `u` is a closed immersion, then so
is `δ ∘ (id_G × u) : G ×_S G′ → G ×_S G`; hence, by Lemma 9.2.1 below, `G″` is separated over `S`.

Assertion (xi) follows from (vii) and from EGA IV₂, 2.2.13.

Assertion (xii) follows from (vii), from EGA IV₄, 17.7.5 and 17.7.7, and from the fact that, `p` being universally
open, whatever `s ∈ S`, if the underlying space of `G_s` is discrete, the same is true of the underlying space of
`G″_s`.

Finally, assertion (xiii) follows from (vii), (viii), and from EGA IV₄, 17.7.5. ∎

**Lemma 9.2.1.** *Let `X` be an `S`-scheme and `R` an equivalence relation defined on `X` by the monomorphism
`v : R → X ×_S X`. Suppose `R` effective. Then:*

*(i) `v` is an immersion, and is a closed immersion if `Y = X/R` is separated.*

*(ii) Suppose moreover that `Y` represents the (fpqc) quotient sheaf of `X` by `R`*[^N.D.E-VI_B-86] *and that `v` is a
closed immersion. Then `Y = X/R` is separated over `S`.*

<!-- label: III.VI_B.9.2.1 -->

[^N.D.E-VI_B-86]: As pointed out by O. Gabber, this is used in the proof and must be inserted in the hypotheses.

Recall (IV Def. 3.3.2) that the hypothesis "`R` effective" means that there exists a morphism of `S`-schemes
`p : X → Y` such that the natural morphism `R → X ×_Y X` is an isomorphism. From this one deduces (EGA I, 5.3.5) the
following cartesian diagram:

```text
R ────v────→ X ×_S X
│              │
│              p × p
│              │
↓ Δ_{Y/S}      ↓
Y ─────────→ Y ×_S Y.
```

Then, since `Δ_{Y/S}` is an immersion (EGA I, 5.3.9), the same is true of `v`. Similarly, if `Y` is separated over `S`,
`Δ_{Y/S}` is a closed immersion, hence so is `v`.

Conversely, suppose that `v` is a closed immersion and that `Y` represents the (fpqc) quotient sheaf of `X` by `R`.
Then `p` is covering for the (fpqc) topology (IV 4.4.3), and hence `p × p` is too (by base change, `p × id_X` and
`id_Y × p` are covering, hence so is their composite `p × p`). Hence, by (fpqc) descent (cf. EGA IV₂, 2.7.1),
`Δ_{Y/S}` is a closed immersion, i.e. `Y` is separated over `S`. ∎

**Remark 9.2.2.** *Under the general hypotheses of 9.2, if one assumes `G′` flat and locally of finite presentation over
`S`, then `p` is covering for the (fppf) topology,*[^N.D.E-VI_B-87] *by 9.2 (vii), hence assertions (vii) and (viii) of
9.2 can be extended to properties `P` local in nature for the (fppf) topology.*

<!-- label: III.VI_B.9.2.2 -->

[^N.D.E-VI_B-87]: We have corrected (fpqc) to (fppf).

<!-- original page 398 -->

**Remark 9.3.** *a) The question of whether a quotient `G/G′` is representable or not is often delicate; in this seminar
we demonstrate the representability of certain particular quotients.*

*In general, in order to assert that the quotient `G/G′` is representable, it is not sufficient to suppose `G` and `G′`
of finite presentation over `S` and `G′` flat over `S`. Indeed, suppose moreover `G` smooth with connected fibers. In
this case, if `G/G′` is a scheme, it is separated, by Corollary 5.4, and hence `G′ ↪ G` is a closed immersion, by
9.2 (x); consequently, if `G′` is not closed in `G`, then `G/G′` is not representable.*

*To obtain such a counterexample, one may take for `S` the spectrum of a discrete valuation ring, and set
`G = G_{m,S}`. Consider moreover an integer `n > 1`, invertible on `S`; then `μ_n = Ker(G ─n→ G)` is a closed subgroup
of `G` étale over `S`*[^N.D.E-VI_B-88] *(cf. VII_A). Let `G′` be the open subgroup of `μ_n` obtained by removing from
`μ_n` the closed part of the closed fiber of `μ_n` complementary to the origin. Then `G′` is not closed in `G`, hence
`G/G′` is not representable. (One can also fabricate such examples where `G′` is smooth with connected fibers.)*

*b) It is not excluded that `G/G′` be representable on the other hand, when `G` and `G′` are of finite presentation
over `S`, and `G′` is flat over `S` and closed in `G`.*[^VI_B-9-1][^N.D.E-VI_B-89] *Under these hypotheses, it is known
that `G/G′` is representable in the following particular cases:*

*1° — `S` is the spectrum of an Artinian ring (cf. VI_A 3.2 and 3.3.2).*

*2° — `G′` is proper over `S` and `G` quasi-projective over `S` (cf. V 7.1).*

*3° — `S` is locally noetherian of dimension 1 (cf. [An73], Th. 4.C).*

<!-- label: III.VI_B.9.3 -->

[^N.D.E-VI_B-88]: see VII_A, 8.4 or VIII, 2.1.

[^VI_B-9-1]: This is too optimistic, as M. Raynaud shows in his thesis (loc. cit. X 14).

[^N.D.E-VI_B-89]: The remark (∗) refers to the counterexample X.14 in [Ray70a]. The base there is regular local of dimension 2.

## 10. Passage to the inverse limit in group schemes and in schemes with operator group

<!-- label: III.VI_B.10 -->

### 10.0.

Let us recall the essential result of EGA IV₃, § 8.8. Suppose given the following situation: `S_0` a quasi-compact and
quasi-separated scheme, `I` a filtered increasing preordered set, `(A_i)_{i ∈ I}` an inductive system of quasi-coherent
commutative `𝒪_{S_0}`-algebras, `A = lim⃗ A_i`, `S_i = Spec A_i` for `i ∈ I`, and `S = Spec A`;[^N.D.E-VI_B-90] then the
category of `S`-schemes of finite presentation is determined up to equivalence by the data of the categories of
`S_i`-schemes of finite presentation, of the functors between these categories `ρ_{ji} : X_i ↦ X_i ×_{S_i} S_j` for
`i ⩽ j`, and the transitivity isomorphisms `ρ_{kj} ∘ ρ_{ji} ⥲ ρ_{ki}`.

[^N.D.E-VI_B-90]: Note that `S`, being affine over `S_0`, is therefore quasi-compact and quasi-separated, cf. N.D.E. (92) below.

Let us be precise. Given `j ∈ I`, and an `S_j`-scheme of finite presentation `X_j`, we shall set, for every `i ∈ I` such
that `i ⩾ j`, `X_i = X_j ×_{S_j} S_i`, and `X = X_j ×_{S_j} S`. Then (EGA IV₃, 8.8.2):

(i) Given `j ∈ I`, and two `S_j`-schemes of finite presentation `X_j` and `Y_j`, the canonical map
`lim⃗_{i ⩾ j} Hom_{S_i}(X_i, Y_i) → Hom_S(X, Y)` is bijective.

(ii) For every `S`-scheme of finite presentation `X`, there exists an index `j ∈ I`, an `S_j`-scheme of finite
presentation `X_j` and an `S`-isomorphism `X ⥲ X_j ×_{S_j} S`.

<!-- original page 386 -->

One concludes (EGA IV₃, 8.8.3) that, whenever one has a diagram `𝒟` involving a finite number of objects and arrows
of the category of `S`-schemes of finite presentation, one can find an index `i ∈ I` and a diagram `𝒟_i` in the
category of `S_i`-schemes of finite presentation, such that the diagram `𝒟` comes up to isomorphism from the diagram
`𝒟_i` by base change `S → S_i`. One can even find `i` and `𝒟_i` such that every cartesian square of `𝒟` comes from a
cartesian square of `𝒟_i`.

### 10.1.

Moreover, a great number of common properties for a morphism, stable under base change, possess the following property:

> Let `u : X → Y` be an `S`-morphism between `S`-schemes of finite presentation; it comes by base change from an
> `S_j`-morphism `u_j : X_j → Y_j` between `S_j`-schemes of finite presentation, by 10.0; then, for `u` to have property
> `P`, it is necessary and sufficient that there exist `i ⩾ j` such that `u_i = u_j ×_{S_j} S_i` has property `P`.

This is so in the case where `P` is one of the following properties for a morphism: being separated, surjective,
radicial, affine, quasi-affine, finite, quasi-finite, proper, projective, quasi-projective, an isomorphism, a
monomorphism, an immersion, an open immersion, a closed immersion (EGA IV₃, 8.10.5), flat (EGA IV₃, 11.2.6), smooth,
unramified or étale (EGA IV₄, 17.7.8).[^N.D.E-VI_B-91]

[^N.D.E-VI_B-91]: We have added the word "flat", and corrected 17.7.6 to 17.7.8.

Note that this is also the case where `P` is the property of being covering for the (fppf) topology; indeed, given two
`S`-schemes of finite presentation `X` and `Y`, and an `S`-morphism `u : X → Y`, it follows from IV, 6.3.1 (i)[^N.D.E-VI_B-92] that, for `u` to be covering for the (fppf) topology, it is necessary and sufficient that there exist an `S`-scheme `Z` and an `S`-morphism `v : Z → Y` faithfully flat and of finite presentation which factors through `u`.

[^N.D.E-VI_B-92]: and from the fact that `Y`, being of finite presentation over `S`, is quasi-compact.

The aim of this section 10 is to give variants of this kind of results for the category of `S`-groups of finite
presentation, that of `S`-schemes with operator group, and for certain properties for monomorphisms of groups (being
invariant, central with representable quotient sheaf, etc.).

The two preliminary results of this type are the following. (In nos. 10.2 to 10.9 below, we keep the notations
introduced in 10.0.)

<!-- original page 400 -->

**Lemma 10.2.** *Let `G_j` and `H_j` be two `S_j`-groups of finite presentation; set, for every `i ⩾ j`,
`G_i = G_j ×_{S_j} S_i`, `G = G_j ×_{S_j} S`, and define similarly `H_i` and `H`. Then the canonical map below is
bijective:*

```text
lim⃗_{i ⩾ j} Hom_{S_i-gr.}(G_i, H_i) → Hom_{S-gr.}(G, H).
```

<!-- label: III.VI_B.10.2 -->

**Lemma 10.3.** *Let `G` be an `S`-group of finite presentation; then there exist `j ∈ I`, an `S_j`-group of finite
presentation `G_j`, and an isomorphism of `S`-groups `G ≅ G_j ×_{S_j} S`.*

<!-- label: III.VI_B.10.3 -->

Assertions 10.2 and 10.3 are easy consequences of 10.0 and 10.1, taking into account the interpretation[^N.D.E-VI_B-93]
of the structure of `S`-group given in EGA 0_III, 8.2.5 and 8.2.6.

[^N.D.E-VI_B-93]: in terms of commutative diagrams of `S`-morphisms.

**Lemma 10.4.** *Let `u : G → H` be a morphism of `S`-groups between `S`-groups of finite presentation. By 10.3 and 10.2,
`u` comes by base change from a morphism `u_j : G_j → H_j` between `S_j`-groups of finite presentation. Then, for `u` to
be a central monomorphism (resp. an invariant monomorphism), it is necessary and sufficient that there exist `i ⩾ j`
such that `u_i = u_j ×_{S_j} S_i` has the same property.*

<!-- label: III.VI_B.10.4 -->

This is an immediate consequence of 10.0 and 10.1, taking into account the characterization given in 6.7 of central or
invariant monomorphisms of groups.

**Corollary 10.5.** *Let `G_j` be an `S_j`-group of finite presentation. For `G_j ×_{S_j} S` to be commutative, it is
necessary and sufficient that there exist `i ⩾ j` such that `G_j ×_{S_j} S_i` is so.*

<!-- label: III.VI_B.10.5 -->

Indeed, it amounts to the same to say that an `S`-group is commutative, or that, considered as a group subscheme of
itself, it is central.

**Proposition 10.6.** *Let `G_j` be an `S_j`-group of finite presentation, `G′_j` a group subscheme of `G_j` flat and
of finite presentation over `S_j`. For `(G_j ×_{S_j} S)/(G′_j ×_{S_j} S)` to be representable for the (fpqc) topology,
it is necessary and sufficient that there exist `i ⩾ j` such that `(G_j ×_{S_j} S_i)/(G′_j ×_{S_j} S_i)` is so.*

<!-- label: III.VI_B.10.6 -->

This is a consequence of the following more general lemma.

**Lemma 10.7.** *Let `X_j` be an `S_j`-scheme of finite presentation, and `R_j` an equivalence relation on `X_j` flat
and of finite presentation.*[^N.D.E-VI_B-94] *For the quotient sheaf `(X_j ×_{S_j} S)/(R_j ×_{S_j} S)` for the topology
`T =` (fppf) or (fpqc) to be representable, it is necessary and sufficient that there exist `i ⩾ j`, such that the
quotient sheaf `(X_j ×_{S_j} S_i)/(R_j ×_{S_j} S_i)` for the topology `T` is so.*

<!-- label: III.VI_B.10.7 -->

[^N.D.E-VI_B-94]: i.e., such that the composite `R_j ↪ X_j ×_{S_j} X_j ─pr_1→ X_j` is flat and of finite presentation.

Taking into account the statements of EGA IV₂, 8.8.2, 8.8.3, 8.10.5 and 11.2.6 recalled in 10.0, this lemma is a
consequence of the following result.

<!-- original page 401 -->

**Lemma 10.8.** *Let `T` be the (fppf) or (fpqc) topology; let `X` be an `S`-scheme of finite presentation (resp. locally
of finite presentation), `R` an equivalence relation on `X` defined by a monomorphism `v : R → X ×_S X` such that
`pr_1 ∘ v` is flat and of finite presentation (resp. flat and locally of finite presentation). Then the following
conditions are equivalent:*

*(i) The quotient sheaf `X/R` for the topology `T` is representable.*

*(ii) There exist an `S`-scheme of finite presentation (resp. locally of finite presentation) `Y` and a faithfully flat
morphism `p : X → Y` such that the diagram*

```text
(D)    R ──pr_1 ∘ v─→ X
       │              │
       pr_2 ∘ v       p
       │              │
       ↓              ↓
       X ─────p────→ Y
```

*is cartesian.*

<!-- label: III.VI_B.10.8 -->

Let us note first that, by IV, 3.3.2 and 4.4.3, for the sheaf `X/R` for the topology `T` to be representable by `Y`, it
is necessary and sufficient that the diagram (D) be cartesian and that `p` be covering for the topology `T`.

Let us show that (i) entails (ii). Hypothesis (i) implies that the diagram (D) is cartesian, hence that `pr_1 ∘ v` is
deduced from `p` by base change by `p`, and that `p` is covering for the (fpqc) topology. Hence, by (fpqc) descent (EGA
IV₂, 2.7.1), since `pr_1 ∘ v` is faithfully flat and (locally) of finite presentation, so is `p`. Then, by EGA IV₄,
17.7.5, since `X` is (locally) of finite presentation over `S`, so is `Y`.

Let us show that (ii) entails (i). It suffices to show that `p` is covering for the (fppf) topology; now `p` is
faithfully flat by hypothesis, and is locally of finite presentation since `X` and `Y` are locally of finite
presentation over `S` (EGA IV₁, 1.4.3 (v)). ∎

**Lemma 10.9.** *Let `G_j` be an `S_j`-group of finite presentation, and `G = G_j ×_{S_j} S`. For `G⁰` to be
representable, it is necessary and sufficient that there exist `i ⩾ j` such that `(G_i)⁰ = (G_j ×_{S_j} S_i)⁰` is so.*

<!-- label: III.VI_B.10.9 -->

The condition is sufficient, since the functor `G ↦ G⁰` commutes with base change, by 3.3.

Conversely, suppose `G⁰` representable. Then, by 3.9, `G⁰` is open in `G` and quasi-compact over `S`, hence of finite
presentation over `S`, since `G` is. Then, by 10.3 and 10.1, there exist `i ⩾ j` and an open group subscheme `H_i` of
`G_i` such that `H_i ×_{S_i} S = G⁰`. The structural morphism `G⁰ → S` is connected, i.e. has geometrically connected
fibers (VI_A 2.1.1), hence, by EGA IV₃, 9.3.3 and 9.7.7, up to increasing `i`, one may suppose that the structural
morphism `H_i → S` is connected. Then, by 3.10.1, the underlying space of `H_i` is none other than `(G_i)⁰`, and hence
`H_i` represents `(G_i)⁰`. ∎

### 10.10.

Let us recall two very useful particular cases of the situation stated in 10.0 (cf. EGA IV₃, 8.1.2 a) and c)):

<!-- original page 402 -->

a) Given a point `x` of a scheme `X`, one sets `S_0 = Spec ℤ` and considers the filtered decreasing projective system
`(S_i)_{i ∈ I}` of affine open neighborhoods of `x`; then `S = Spec 𝒪_{X,x}`. In particular, if `x` is the generic
point of an integral scheme `X`, one finds `S = Spec κ(x)`.

b) One sets `S_0 = Spec ℤ`, and considers the family `(A_i)_{i ∈ I}` preordered by inclusion of the finitely generated
sub-`ℤ`-algebras of the ring of an affine scheme `S`. Given that the `A_i` are noetherian rings, this allows in many
cases to pass from the noetherian case to the general case.

We are now going to give two results concerning the particular case considered in a).[^N.D.E-VI_B-95]

[^N.D.E-VI_B-95]: Note that the proof uses also case b).

**Proposition 10.11.** [^N.D.E-VI_B-96] *Let `S` be an integral scheme with generic point `η`, `G` (resp. `Y, Z`) an
`S`-group (resp. `S`-schemes) of finite presentation, `u, v, i : Y → G` and `j : Z → G` morphisms of `S`-schemes.
Suppose that `i_η : Y_η → G_η` and `j_η : Z_η → G_η` are closed immersions.*

*Then, there exists a non-empty open `S′` of `S` such that the morphisms `i′ : Y′ → G′` and `j′ : Z′ → G′` obtained by
base change are closed immersions, and such that the functors:*

```text
Transp(u′, v′),    Transp_{G′}(i′(Y′), j′(Z′))    and    Transpstr_{G′}(i′(Y′), j′(Z′))
```

*resp.*

```text
Centr(u′)    and    Norm_{G′} i′(Y′)
```

*are representable by closed sub-`S′`-schemes (resp. sub-`S′`-groups) of `G′`, of finite presentation over `S′`.*

<!-- label: III.VI_B.10.11 -->

[^N.D.E-VI_B-96]: We have simplified the statement, and treated separately, in Corollary 10.11.1, the case of subgroups.

We shall apply the results of 10.1, first in the situation of 10.10 a), then in that of 10.10 b). Since `G_η, Y_η, Z_η`
are flat over the field `κ(η)`, `G_η` is separated over `κ(η)` (VI_A 0.3), and `i_η, j_η` are closed immersions, then,
by 10.1, there exists an affine open `S′ = Spec(A′)` of `S`, a noetherian subring `A` of `A′`, `A`-schemes `G_A, Y_A,
Z_A`, flat and of finite presentation over `A`, and morphisms `u_A, v_A, i_A : Y_A → G_A` and `j_A : Z_A → G_A`, such
that `G_A` is an `A`-group, separated over `A`, `i_A` and `j_A` are closed immersions, and
`G ×_S S′ = G_A ⊗ A′`, etc. As the functors considered for `S′` are deduced by base change from the analogous functors
for `Spec(A)`, it suffices to establish the result for the latter.

By EGA IV₂, 6.9.2, up to replacing `A` by a localization `A_f` (and hence `S′` by the affine open `S′_f`), one may
suppose that `G_A, Y_A, Z_A` are essentially free over `A` (in the sense of 6.2.1).[^N.D.E-VI_B-97] It follows then
from 6.2.4 b) and e) that, under the hypotheses of the statement, the functors considered are representable by closed
sub-`A`-schemes of `G_A` (hence of finite presentation over `A`, since `A` is noetherian and `G_A` of finite
presentation

[^N.D.E-VI_B-97]: Indeed, `G_A` being flat and of finite presentation over `A`, it is covered by affine opens `G_1, …, G_n` such that each `𝒪(G_i)` is a flat and finitely presented `A`-algebra; then, by EGA IV₂, 6.9.2, there exists `f_i ∈ A` such that `𝒪(G_i)_{f_i}` is a free module over `A_{f_i}`; one may then replace `Spec(A)` by the affine open `D(f)`, where `f = f_1 ⋯ f_n`, and one does the same for `Y_A` and `Z_A`.

<!-- original page 403 -->

over `A`), and these are sub-`A`-groups of `G_A` in the case of `Centr(u_A)` and of `Norm_{G_A} i_A(Y_A)`. ∎

**Corollary 10.11.1.** *Let `S` be an integral scheme with generic point `η`, `G, H, K` `S`-groups of finite presentation,
`i : H → G` and `j : K → G` two quasi-compact monomorphisms of `S`-groups. Then, there exists a non-empty open `S′` of
`S` such that the morphisms `i′ : H′ → G′` and `j′ : K′ → G′` obtained by base change are closed immersions, and such
that the functors:*

```text
Transp_{G′}(H′, K′)    and    Transpstr_{G′}(H′, K′)    (resp. Centr_{G′} H′    and    Norm_{G′} H′)
```

*are representable by closed sub-`S′`-schemes (resp. sub-`S′`-groups) of `G′`, of finite presentation over `S′`.*

<!-- label: III.VI_B.10.11.1 -->

This follows from the preceding proposition since, by 1.4.2, the hypotheses entail that `i_η` and `j_η` are closed
immersions.

**Proposition 10.12.** *Let `S` be an integral scheme, `G` an `S`-group of finite presentation, `A` and `B` two group
subschemes of `G`, of finite presentation over `S` and with smooth generic fiber. Suppose moreover satisfied one of the
following conditions:*

*a) `A` has connected generic fiber,*

*b) `A` and `B` are invariant in `G`.*

*Then, there exists a non-empty open `S′` of `S` and a closed group subscheme `D′` of `G′ = G|_{S′}`, of finite
presentation over `S′`, with smooth fibers, which represents the (fppf) sheaf associated with the presheaf in groups of
commutators of `A′ = A|_{S′}` and `B′ = B|_{S′}` in `G′`, and `D′` has connected fibers in case (a), and is invariant
in `G′` in case (b).*

*In particular, for every `s ∈ S′`, one has `D′_s = (A_s, B_s)` with the notations of 7.2.2.*

<!-- label: III.VI_B.10.12 -->

Let `η` be the generic point of `S`; set `H_η = (A_η, B_η)`. Since `A_η` and `B_η` are smooth, then, by 7.8 in case (a),
and 7.3 (v) in case (b), `H_η` is connected (resp. invariant in `G_η`).

We are in the situation of 10.0 corresponding to 10.10 (a); hence, by 10.3 and 10.1, there exists a non-empty open
`S′` of `S` and a sub-`S′`-group scheme `D′` of finite presentation and closed in `G′`, such that
`D′_η = D′ ⊗_{S′} κ(η)` equals `H_η`. Moreover, by EGA IV₃, 9.7.7 and 9.3.3, one may suppose that `D′` has
geometrically reduced fibers. In case (a), one may suppose, by EGA IV₃, 9.7.7 and 9.3.3 again, that `D′` has connected
fibers, hence geometrically connected (cf. VI_A, 2.1.1). In case (b), one may suppose, by 10.4, that `D′` is invariant
in `G′`.

Moreover, we have seen, in the course of the proof of 7.8, that there exists an integer `n` such that
`ν^n_η((A_η ×_{κ(η)} B_η)^n) = D′_η`, where `ν_η` and `ν^n_η` are defined as in 7.2.2 (a) and 7.1 (ii). We may define by
the same formulas the morphisms

```text
ν′ : A′ ×_{S′} B′ → G′    and    ν′^n : (A′ ×_{S′} B′)^n → G′,
```

and one has `ν′^n ⊗_{S′} κ(η) = ν^n_η`.

<!-- original page 404 -->

Consequently, by 10.1, one may choose `S′` such that the morphism `ν′^n` is flat and factors through `D′`, and such
that the morphism `ν′^n : (A′ ×_{S′} B′)^n → D′` thus obtained is surjective. Then, by 7.5, the
morphism[^N.D.E-VI_B-98]

```text
ν′^{2n} = μ ∘ (ν′^n ×_{S′} ν′^n) : (A′ ×_{S′} B′)^{2n} → D′,
```

is covering for the (fppf) topology. Hence, by 7.6, `D′` represents the (fppf) sheaf associated with the presheaf of
commutators of `A′` and `B′` in `G′`.

Moreover, `ν′^n` induces, for every `s ∈ S′`, a surjective morphism
`ν^n_s : (A_s ×_{κ(s)} B_s)^n → D′_s`.[^N.D.E-VI_B-99] Then `D′_s` is a closed subgroup of `G_s` containing
`ν_s(A_s ×_{κ(s)} B_s)`, hence also `(A_s, B_s)`. As `ν^n_s` is surjective, `D′_s` equals `(A_s, B_s)` and represents,
by 7.6, the (fppf) sheaf of commutators of `A_s` and `B_s` in `G_s`. ∎

[^N.D.E-VI_B-98]: We have corrected `n+1` to `2n` below.

[^N.D.E-VI_B-99]: We have detailed the original in what follows.

**Corollary 10.12.1.** [^N.D.E-VI_B-100] *Let `S` be an integral scheme, with generic point `η`, and `G` an `S`-group of
finite presentation with smooth fibers. Set `K⁰_η = G_η` and `K^p_η = (K^{p−1}_η, K^{p−1}_η)`
(resp. `K^p_η = (G, K^{p−1}_η)`) for every `p ∈ ℕ*`. Fix `n ∈ ℕ*`. Then there exists a non-empty open `S′` of `S` and a
group subscheme `D` invariant in `G|_{S′}`, of finite presentation and with smooth fibers, such that
`D_s = K^n_s` for every `s ∈ S′`.*

<!-- label: III.VI_B.10.12.1 -->

[^N.D.E-VI_B-100]: We have added this corollary, used in the proof of 8.4.

This follows from 10.12, by induction on `n`.

**Corollary 10.13.** *Let `S` be an integral scheme with generic point `η`, `G` an `S`-group, `H` an invariant
sub-`S`-group scheme in `G`; suppose `G` and `H` of finite presentation over `S` and with smooth generic
fiber.*[^N.D.E-VI_B-101]

*If one has `(H_η, H_η) = H_η` (resp. `(G_η, H_η) = H_η`), then there exists a non-empty open `S′` of `S` such that for
every `s ∈ S′`, one has `(H_s, H_s) = H_s` (resp. `(G_s, H_s) = H_s`).*

<!-- label: III.VI_B.10.13 -->

[^N.D.E-VI_B-101]: The original assumed `G, H` of finite presentation and `H` with smooth fibers; we have modified the hypothesis in order to be able to apply 10.12. We have also detailed the proof.

Indeed, by the proof of 10.12, there exists a non-empty open `S′` of `S` and a sub-`S′`-group scheme `D` of `G|_{S′}`,
of finite presentation and with smooth fibers, such that `D_s = (H_s, H_s)` (resp. `D_s = (G_s, H_s)`) for every
`s ∈ S′`. On the other hand, since `D_η = H_η` and since `D` and `H` are of finite presentation over `S′`, then, by EGA
IV₃, 8.8.2.5, there exists a non-empty open `S″` of `S′` such that `D|_{S″} = H|_{S″}`. For every `s ∈ S″`, one has
therefore `H_s = D_s = (H_s, H_s)` (resp. `H_s = D_s = (G_s, H_s)`). ∎

### 10.14.

Statements 10.2 and 10.3 concerning the category of `S`-groups of finite presentation extend to the category of pairs
formed by an `S`-group of finite presentation and an `S`-scheme of finite presentation with operator group `G`. To be
precise, in the situation recalled at the start of 10.0:

(i) Let `j ∈ I` and `G_j` and `G′_j` two `S_j`-groups of finite presentation, `H_j` (resp. `H′_j`) an `S_j`-scheme of
finite presentation with operator group `G_j` (resp. `G′_j`). Set, for `i ∈ I`, `i ⩾ j`, `G_i = G_j ×_{S_j} S_i` and
`G = G_j ×_{S_j} S`, and define similarly `G′_i, G′, H_i, H, H′_i`

<!-- original page 405 -->

and `H′`. Denote by `Dihom_{S-gr.}((G, H), (G′, H′))` the set of di-morphisms of `S`-groups and `S`-schemes with
operator group of the pair `(G, H)` into the pair `(G′, H′)`. Then the canonical map

```text
lim⃗_{i ⩾ j} Dihom_{S_i-gr.}((G_i, H_i), (G′_i, H′_i)) → Dihom_{S-gr.}((G, H), (G′, H′))
```

is bijective.

(ii) Let `G` be an `S`-group of finite presentation and `H` an `S`-scheme of finite presentation with operator group
`G`; there then exists an index `j ∈ I`, an `S_j`-group of finite presentation `G_j`, an `S_j`-scheme of finite
presentation `H_j` with operator group `G_j` and a di-isomorphism of `S`-groups and `S`-schemes with operator groups
from `(G_j ×_{S_j} S, H_j ×_{S_j} S)` onto `(G, X)`.

<!-- label: III.VI_B.10.14 -->

**Definition 10.15.** [^N.D.E-VI_B-102] *Let `T` be a topology on `(Sch/S)`, less fine than the canonical topology.
Given an `S`-group scheme `G` and an `S`-scheme `X` with operator group `G`, one says that `X` is a* formally
homogeneous space under `G` *(relative to the topology `T`) if the morphism `Φ : G ×_S X → X ×_S X`, defined by
`(g, x) ↦ (gx, x)` for every `S′ → S` and `g ∈ G(S′)`, `x ∈ X(S′)`, is an epimorphism in the category of sheaves for the
topology `T`, which amounts to saying that `Φ` is covering for the topology `T` (cf. IV 4.4.3).*

*One says that `X` is a* homogeneous space *if it is formally homogeneous and if moreover the morphism `X → S` is also
covering for the topology `T`.*

*In particular, one says that `X` is a* formally principal homogeneous space under `G` *if `Φ` is an isomorphism, and that
`X` is a* principal homogeneous bundle *(or* `G`-torsor*) if `Φ` is an isomorphism and if moreover the morphism `X → S`
is covering for the topology `T` (cf. IV 5.1.5 and 5.1.6 (ii)).*

<!-- label: III.VI_B.10.15 -->

[^N.D.E-VI_B-102]: (Added by editors; see source.)

**Proposition 10.16.** *We place ourselves in the situation considered at the beginning of 10.0. Let `j ∈ I`, `G_j` an
`S_j`-group and `X_j` an `S_j`-scheme with operator group `G_j`. Suppose `G_j` and `X_j` of finite presentation over
`S_j`.*

*For `X = X_j ×_{S_j} S` to be a homogeneous space (resp. a principal homogeneous bundle) under
`G = G_j ×_{S_j} S` for the (fppf) topology, it is necessary and sufficient that there exist an index `i ⩾ j` such
that `X_i = X_j ×_{S_j} S_i` is a homogeneous space (resp. a principal homogeneous bundle) under
`G_i = G_j ×_{S_j} S_i`.*

<!-- label: III.VI_B.10.16 -->

Taking into account 10.14 and EGA IV₃, 8.8.2, 8.8.3 and 8.10.5, the statement follows from the property concerning
covering morphisms for the (fppf) topology recalled in 10.1.[^N.D.E-VI_B-103]

[^N.D.E-VI_B-103]: (End of section 10.)

## 11. Affine group schemes

<!-- label: III.VI_B.11 -->

### 11.0. Reminders.

[^N.D.E-VI_B-C-104] Let `q : X → S` be a quasi-compact and quasi-separated morphism of schemes (cf. EGA IV₁, 1.1 &
1.2), and let `F` be a quasi-coherent `O_X`-module. Recall that `q_*(F)` is a quasi-coherent `O_S`-module
(EGA I, 9.2.1). Moreover, by EGA III, 1.4.15 (completed by EGA IV₁, 1.7.21), one has point (c) below, and the proof of
loc. cit. also gives points (a) and (b):

[^N.D.E-VI_B-C-104]: We have added this reminders paragraph.

(a) If `F` is a filtered inductive limit of quasi-coherent submodules `F_α`, then `q_*(F) = lim_α q_*(F_α)`.

(b) If `E` is a flat `O_S`-module, the canonical morphism `E ⊗_{O_S} q_*(O_X) → q_* q*(E)` is an isomorphism.

(c) Let `p : S′ → S` be a flat morphism, `q′ : X′ → S′` the morphism deduced from `q` by base change, and `F ′` the
inverse image of `F` on `X′`. Then the canonical morphism `p*q_*(F) → q′_*(F ′)` is an isomorphism.

Indeed, let `U = Spec(A)` be an arbitrary affine open of `S`. By hypothesis, `q⁻¹(U)` is the union of affine opens
`V_i = Spec(B_i)`, for `i = 1, …, n`, and each intersection `V_i ∩ V_j` is the union of finitely many affine opens
`W_{ijk} = Spec(C_{ijk})`. Then `Γ(U, q_*(F)) = Γ(q⁻¹(U), F)` is the kernel of the morphism

```text
⊕_{i=1}^n Γ(V_i, F) → ⊕_{i,j,k} Γ(W_{ijk}, F).
```

Point (a) follows, since each of the terms above commutes with filtered inductive limits (since the `V_i` and `W_{ijk}`
are affine, hence quasi-compact). Let us prove (b): `E = Γ(U, E)` is a flat `A`-module, and `Γ(U, q_* q*(E))` is the
kernel `K(E)` of the morphism

```text
⊕_{i=1}^n B_i ⊗_A E → ⊕_{i,j,k} C_{ijk} ⊗_A E
```

and since `E` is flat over `A`, this kernel is identified with `K(A) ⊗_A E = O_X(q⁻¹(U)) ⊗_A E`. Finally, if `U′` is
an arbitrary affine open of `S′` above `U`, then `A′ = O(U′)` is a flat `A`-algebra, and one obtains as above that
`F(q⁻¹(U)) ⊗_A A′ ⥲ F ′(q′⁻¹(U))`.

**Notation.** Let `S` be a scheme, `X` an `S`-scheme, `f : X → S` the structural morphism; we set
`𝒜(X) = f_*(O_X)`.

**Lemma 11.1.** *Let `X` and `Y` be two `S`-schemes quasi-compact and quasi-separated over `S`, `f : X → S` and
`g : Y → S` the structural morphisms. Then the canonical homomorphism*

```text
φ : 𝒜(X) ⊗_{O_S} 𝒜(Y) → 𝒜(X ×_S Y)
```

*is an isomorphism in each of the following cases:*[^N.D.E-VI_B-C-105]

*a) `f` and `g` are affine,*

*b) `g` (or `f`) is flat and affine,*

*c) `g` is flat and `f_*(O_X)` is a flat `O_S`-module.*

<!-- label: III.VI_B.11.1 -->

[^N.D.E-VI_B-C-105]: Note that if `k` is a field and if `X` is an infinite sum of copies of `S = Spec k` (so that `X` is not quasi-compact), then `𝒜(X) = k^X` and the canonical morphism `k^X ⊗ k^X → k^{X×X}` is not surjective.

We shall assume, in case (b), that it is `g` which is flat and affine. Set then `S′ = Spec 𝒜(X)`, `Y′ = Y ×_S S′`,
`g′ = g ×_S S′`, and denote by `v` the morphism `S′ → S`:

```text
       Y′ ───→ Y
       │        │
    g′ │        │ g
       ↓   v    ↓
Spec 𝒜(X) = S′ ──→ S
```

In cases (a) and (b), `g` is affine and so, by EGA II, 1.5.2, one has:

```text
(1)        g′_*(O_{Y′}) = v* g_*(O_Y) = 𝒜(Y) ⊗_{O_S} O_{S′}.
```

One has the same equality in case (c), by 11.0 (c), since `S′` is flat over `S` and `g` is quasi-compact and
quasi-separated.

On the other hand (EGA II 1.2.7), `f : X → S` factors through `v` by means of a morphism `p : X → S′`, and one has
`p_*(O_X) = O_{S′}` and `X ×_S Y = X ×_{S′} Y′`. Since `f` is quasi-separated, so is `p` (EGA IV₁, 1.2.2), and since
`f` is quasi-compact and `v` is quasi-separated, `p` is also quasi-compact (EGA IV₁, 1.2.4). Consider then the
cartesian square:

```text
              p′
   X ×_S Y ────→ Y′
       │          │ g′
     p │          ↓
       ↓          S′
       X ────→
            p
```

In cases (b) and (c), `Y` is flat over `S`, hence `Y′` is flat over `S′`; applying 11.0 (c) again, one obtains:

```text
(2)        p′_*(O_{X ×_S Y}) = g′* p_*(O_X) = g′*(O_{S′}) = O_{Y′},
```

and one has the same equality in case (a), since in this case `p` and `p′` are isomorphisms.

Finally, `v` being affine, one has, by EGA II, 1.4.7, `v_*(F ⊗_{O_S} O_{S′}) = F ⊗_{O_S} 𝒜(X)` for every
quasi-coherent `O_S`-module `F`. Combined with (2) and (1), this gives:

```text
𝒜(X ×_S Y) = v_* g′_* p′_*(O_{X ×_S Y}) = v_* g′_*(O_{Y′}) = v_*(𝒜(Y) ⊗_{O_S} O_{S′}) = 𝒜(Y) ⊗_{O_S} 𝒜(X).
```

∎

**Corollary 11.2.** *The functor `X ↦ Spec 𝒜(X)`, from the full subcategory of `(Sch/S)` formed of `S`-schemes `X`
flat, quasi-compact and quasi-separated over `S`, and such that `𝒜(X)` is a flat `O_S`-module, into that of `S`-schemes
flat and affine over `S`, commutes with finite products, hence transforms `S`-groups into `S`-groups.*

<!-- label: III.VI_B.11.2 -->

**Definition 11.3.** *Given an `S`-group `G` flat, quasi-compact and quasi-separated over `S`, such that `𝒜(G)` is flat
over `O_S`,[^N.D.E-VI_B-C-106] we shall denote by `G_af`, and call the* affine envelope *of `G`, the `S`-group
`G_af = Spec 𝒜(G)`.*

<!-- label: III.VI_B.11.3 -->

[^N.D.E-VI_B-C-106]: Note that if `S` is a regular locally noetherian scheme of dimension `≤ 2`, and `X` is a flat, quasi-compact and quasi-separated `S`-scheme, then `𝒜(X)` is a flat `O_S`-module, cf. [Ray70a], VII 3.2.

**Proposition 11.3.1.** [^N.D.E-VI_B-C-107] *The canonical morphism `τ_G : G → G_af` is a morphism of `S`-groups.
Moreover, it satisfies the following universal property:*

*(i) For every morphism of `S`-schemes `φ : G → H`, where `H` is affine over `S`, there exists a unique morphism of
`S`-schemes `φ′ : G_af → H` such that `φ = φ′ ∘ τ_G`.*

*(ii) If moreover `H` is an `S`-group and if `φ` is a morphism of `S`-groups, then so is `φ′`.*

<!-- label: III.VI_B.11.3.1 -->

[^N.D.E-VI_B-C-107]: We have added this proposition; see also the additional paragraph 12 below for a study of the morphism `G → G_af` and its kernel.

### 11.4.

[^N.D.E-VI_B-C-108] Let `E` and `F` be two quasi-coherent `O_S`-modules. Consider the `S`-functor
`Hom_{O_S}(W(E), W(F))` (cf. I, 3.1.4), i.e. for every `S`-scheme `f : X → S`,

```text
Hom_{O_S}(W(E), W(F))(X) = Hom_{O_X}(W(E)_X, W(F)_X).
```

Moreover, by I, 4.6.2, one has `W(E)_X = W(f*(E))` (and similarly for `F`) and

```text
Hom_{O_X}(W(f*(E)), W(f*(F))) = Hom_{O_X}(f*(E), f*(F)).
```

One thus obtains (using the adjunction formula for the last equality):

```text
(†)   Hom_{O_S}(W(E), W(F))(X) = Hom_{O_X}(f*(E), f*(F)) = Hom_{O_S}(E, f_* f*(F)).
```

[^N.D.E-VI_B-C-108]: In 11.4–11.6, we have considered `Hom_{O_S}(W(E), W(F))` instead of `Hom_{O_S}(V(F), V(E))` (cf. I, 4.6.3) and simplified the original by taking into account the addition 11.0 (b).

**Proposition 11.5.** *Let `X` be an `S`-scheme quasi-compact and quasi-separated over `S`, `f : X → S` the structural
morphism, `E` and `E ′` two quasi-coherent `O_S`-modules. Suppose one of the two following conditions holds:*

*a) `f` is affine,*

*b) `E` is flat over `O_S`.*

*Then the canonical morphism `E ⊗_{O_S} 𝒜(X) → f_* f*(E)` is an isomorphism, and one therefore has*

```text
Hom_{O_S}(W(E ′), W(E))(X) = Hom_{O_S}(E ′, E ⊗_{O_S} 𝒜(X)).
```

<!-- label: III.VI_B.11.5 -->

Indeed, the second assertion follows from 11.4 and the first; this latter follows from EGA II, 1.4.7 in case (a), and
from 11.0 (b) in case (b).[^N.D.E-VI_B-C-109] ∎

[^N.D.E-VI_B-C-109]: We have simplified the original, which used the isomorphism `Hom_{O_S}(W(E), W(E ′)) ≃ Hom_{O_S}(V(E ′), V(E))` then the inclusion of the right-hand side into `Hom_S(V(E), V(E ′)) = Hom_{O_S}(E ′, f_* f*(Sym(E)))` and applied EGA III, 4.1.15 to `V(E) = Spec(Sym(E))` to deduce 11.0 (b).

### 11.6.

[^N.D.E-VI_B-C-110] Let `G` be an `S`-group and `E` a quasi-coherent `O_S`-module. To give `E` a `G`-`O_S`-module
structure (i.e. an `O_S`-linear action of `G` on `W(E)`, cf. I 4.7.1) is equivalent to giving a morphism of
`S`-functors in monoids `ρ : G → End_{O_S}(W(E))` (indeed, such a `ρ` necessarily sends `G` into
`Aut_{O_S}(W(E))`).

[^N.D.E-VI_B-C-110]: We have expanded 11.6, and highlighted the results obtained in the form of Proposition 11.6.1.

Now, by 11.4, giving a morphism of `S`-functors `ρ : G → End_{O_S}(W(E))` is equivalent to giving an element `θ` of
`Hom_{O_G}(f*(E), f*(E))`, which corresponds by adjunction to an element `δ` of `Hom_{O_S}(E, f_* f*(E))`, where one
has denoted by `f` the projection `G → S`.

Let `m : G ×_S G → G` be the multiplication, `δ_G` the morphism `O_G → m_*(O_{G ×_S G})`, and `φ` the projection
`G ×_S G → S` (which equals `f ∘ m`). It is convenient to denote by `⊠` the "external" tensor product; one thus obtains
a morphism

```text
id_E ⊠ δ_G :   f*(E) = E ⊠_{O_S} O_G → E ⊠_{O_S} m_*(O_{G×G})
```

and by abuse of notation, we shall denote again by `id_E ⊠ δ_G` the composite of the preceding morphism with the
canonical morphism `E ⊠_{O_S} m_*(O_{G×G}) → m_* m* f*(E) = m_* φ*(E)`.

On the other hand, designate by `h : G → S` a second copy of `f : G → S` and consider the following commutative
diagram, where `p`, `q` denote the two projections:

```text
                  q
       G ×_S G ────→ G
            ╲        │
           p ╲    φ  │ h
              ╲      ↓
               G ──→ S
                  f
```

Denoting again by `δ` the morphism `E → h_* h*(E)`, one obtains the morphism

```text
δ ⊠ id_{O_G} :   f*(E) = E ⊠_{O_S} O_G → h_* h*(E) ⊠_{O_S} O_G = f* h_* h*(E)
```

and by abuse we shall denote again by `δ ⊠ id_{O_G}` the composite of this morphism with the canonical morphism
`f* h_* h*(E) → p_* φ*(E)`.

Then the condition that `ρ` be compatible with the multiplication is equivalent to saying that, for every open `U` of
`S`, the diagram below is commutative:

```text
                δ
    Γ(U, E) ─────────────────→ Γ(U ×_S G, E ⊠_{O_S} O_G)
        │                                │
      δ │                                │ id_E ⊠ δ_G
        ↓             δ ⊠ id_{O_G}       ↓
Γ(U ×_S G, E ⊠_{O_S} O_G) ────→ Γ(U ×_S G ×_S G, E ⊠_{O_S} O_G ⊠_{O_S} O_G).
```

(1)

Moreover, the unit section `ε : S → G` induces a morphism `u` from `O_G` to `ε_* ε*(O_G) = ε_*(O_S)`, and the condition
that `ρ` preserves the unit elements is equivalent to the commutativity of the diagram:

```text
                δ
    Γ(U, E) ─────────→ Γ(U ×_S G, E ⊠_{O_S} O_G)
        ╲                  ╱
       ≃ ╲                ╱ id_E ⊠ u
          ↓              ↙
       Γ(U ×_S S, E ⊠_{O_S} O_S).
```

(2)

One thus sees that giving `E` a `G`-`O_S`-module structure is equivalent to giving a morphism of `O_S`-modules
`δ : E → f_* f*(E)` satisfying conditions (1) and (2) above, and in this case the morphism `θ : f*(E) → f*(E)`,
deduced from `δ` by adjunction, is an isomorphism (since it corresponds to the isomorphism
`G ×_S W(E) ⥲ G ×_S W(E)` defined set-theoretically by `(g, x) ↦ (g, gx)`; see also I, 6.5.4).

Suppose now that `G` is flat, quasi-compact and quasi-separated over `S`, and that `𝒜(G)` is a flat `O_S`-module; then,
by 11.1 (c), the canonical morphism `𝒜(G) ⊗_{O_S} 𝒜(G) → 𝒜(G ×_S G)` is an isomorphism, and the morphism
`δ_G : 𝒜(G) → 𝒜(G) ⊗_{O_S} 𝒜(G)` will be denoted by `∆`.

If moreover `E ⊗_{O_S} 𝒜(G) = f_* f*(E)` (which is the case, by 11.5, if `G → S` is affine, or if `E` is flat over
`O_S`), one obtains that conditions (1) and (2) are equivalent to the conditions below, which express that
`δ : E → E ⊗_{O_S} 𝒜(G)` makes `E` a right `𝒜(G)`-comodule (cf. I 4.7.2):

(CM 1) Setting `A = 𝒜(G)`, the diagram below is commutative:

```text
          δ
   E ────────→ E ⊗ A
   │            │
 δ │            │ id_E ⊗ ∆
   ↓ δ ⊗ id_A  ↓
   E ⊗ A ────→ E ⊗ A ⊗ A.
```

(CM 2) Denoting by `η : A → O_S` the morphism `𝒜(ε)`, the diagram below is commutative:

```text
        δ
   E ───────→ E ⊗ A
    ╲           ╱
   ≃ ╲         ╱ id_E ⊗ η
      ↓       ↙
     E ⊗ O_S.
```

**Remark 11.6.A.** Recall that one denotes by `V(E)` the vector fibration on `S` representing the functor `V(E)`, i.e.
for every `S′ → S`, `V(E)(S′) = Hom_{O_{S′}}(E_{S′}, O_{S′})`. As one has, by I, 4.6.2, an anti-isomorphism of
`S`-functors in monoids `End_{O_S}(W(E)) ≃ End_{O_S}(V(E))`, one sees that if `E` is a left `G`-`O_S`-module, one has
a right action `μ : V(E) ×_S G → V(E)` of `G` on `V(E)`, defined set-theoretically by `(φg)(x) = φ(gx)`, for every
`g ∈ G(S′)`, `x ∈ Γ(S′, E_{S′})` and `φ ∈ Hom_{O_{S′}}(E_{S′}, O_{S′})`. One thus obtains commutative diagrams:

<!-- label: III.VI_B.11.6.A -->

```text
                μ × id_G                                         μ
V(E) ×_S G ×_S G ─────→ V(E) ×_S G                  V(E) ←──── V(E) ×_S G
        │                  │                          ╲             ↑
id × m  │                  │ μ                       ≃ ╲            │ id × ε
        ↓        μ         ↓                            ↓
   V(E) ×_S G ──────→ V(E)                                 V(E) ×_S S.
```

When `G` is flat, quasi-compact and quasi-separated over `S`, when `𝒜(G)` is a flat `O_S`-module, and when one of the
conditions of 11.5 is satisfied, one recovers similarly the conditions (CM 1) and (CM 2).

Consequently, we have obtained:

**Proposition 11.6.1.** *Let `G` be an `S`-group flat, quasi-compact and quasi-separated over `S`, such that `𝒜(G)` is
a flat `O_S`-module, and let `E` be a quasi-coherent `O_S`-module.*

*(i) It amounts to the same to give an `𝒜(G)`-comodule structure `δ : E → E ⊗_{O_S} 𝒜(G)` or a `G_af`-`O_S`-module
structure on `E` (i.e. an `O_S`-linear action of `G_af` on `E`). By composition with the morphism of `S`-groups
`G → G_af`, this defines a `G`-`O_S`-module structure on `E`.*

*(ii) If moreover `E` is flat, every `O_S`-linear action of `G` on `E` factors through `G_af` and corresponds to a
unique `𝒜(G)`-comodule structure on `E`.*

<!-- label: III.VI_B.11.6.1 -->

**Lemma 11.7.** *Let `G` be an `S`-group flat, quasi-compact and quasi-separated over `S`, such that `A = 𝒜(G)` is a
flat `O_S`-module. Let `E` be a quasi-coherent `O_S`-module, `δ : E → E ⊗ A` an `A`-comodule structure, and
`ρ : G → Aut_{O_S}(W(E))` the action of `G` on `E` associated with it.*

*Let `E_0` be a quasi-coherent `O_S`-submodule of `E` such that the restriction `δ_0` of `μ` to `E_0` factors through
`E_0 → E_0 ⊗ A`, i.e. such that one has a commutative diagram:*

```text
   E_0 ────→ E
    │         │
δ_0 │         │ δ
    ↓         ↓
  E_0 ⊗ A ──→ E ⊗ A.
```

*(N.B. The morphism `E_0 ⊗ A → E ⊗ A` is injective, since `A` is flat over `O_S`.)*

*Then `δ_0` makes `E_0` an `𝒜(G)`-comodule, hence defines an action `ρ_0` of `G` on `E_0` (which one will call the
induced action on `E_0` by `ρ`, and one will say that `E_0` is* stable *under `ρ`).*

<!-- label: III.VI_B.11.7 -->

This follows immediately from the definitions and from 11.6. One will remark, however, that in general the canonical
map `W(E_0) → W(E)` is not a monomorphism. ∎

**Remark 11.7.bis.** [^N.D.E-VI_B-C-111] Let `G` be a flat `S`-group and `E` a quasi-coherent `G`-`O_S`-module. Denote
by `f` the morphism `G → S` and by `δ` the morphism `E → f_* f*(E)` defined in 11.6. Let `E_0` be a quasi-coherent
`O_S`-submodule of `E`; since `f` is flat, `f_* f*(E_0)` is an `O_S`-submodule of `f_* f*(E)`, and similarly for
`φ = f × f`. Consequently, if the restriction `δ_0` of `δ` to `E_0` factors through `f_* f*(E_0)`, then it makes `E_0`
a `G`-`O_S`-module. In this case, one says that `E_0` is a `G`-stable submodule of `E`.

<!-- label: III.VI_B.11.7.bis -->

[^N.D.E-VI_B-C-111]: We have added this remark, which generalizes 11.7 and will be useful in 11.10.bis.

**Definition 11.8.0.** [^N.D.E-VI_B-C-112] *Let `S` be a scheme. An `O_S`-coalgebra is an `O_S`-module `C` endowed with
two morphisms of `O_S`-modules `∆ : C → C ⊗ C` and `ε : C → O_S`, satisfying the following two axioms (cf. I 4.2):*

*(CO 1) `∆` is co-associative: the following diagram is commutative*

```text
            C ⊗ C
           ╱      ╲
        ∆ ╱        ╲ id ⊗ ∆
         ╱          ╲
        C            C ⊗ C ⊗ C
         ╲          ╱
        ∆ ╲        ╱ ∆ ⊗ id
           ╲      ╱
            C ⊗ C
```

*(CO 2): `ε` is a counit, i.e. the two following composites are the identity*

```text
        ∆          id ⊗ ε        ∼
   C ────→ C ⊗ C ────→ C ⊗ O_S ────→ C,
        ∆          ε ⊗ id         ∼
   C ────→ C ⊗ C ────→ O_S ⊗ C ────→ C.
```

*A (right) `C`-comodule is an `O_S`-module `E` endowed with a morphism of `O_S`-modules `μ : E → E ⊗ C` satisfying the
axioms (CM 1) and (CM 2) of 11.6.*

*One says that `C` (resp. `E`) is a* quasi-coherent coalgebra *(resp. a* quasi-coherent comodule*) if it is a
quasi-coherent `O_S`-module.*

*Let `A` be a commutative ring and `C` an `A`-coalgebra; then `C^∨ = Hom_A(C, A)` is an `A`-algebra. We shall denote by
`ev` the natural evaluation map `C ⊗_A C^∨ → A`.*

<!-- label: III.VI_B.11.8.0 -->

[^N.D.E-VI_B-C-112]: Since the statements 11.8 and 11.9 bear solely on the notion of comodule over a coalgebra, we have introduced Definition 11.8.0 and reformulated 11.8 and 11.9 accordingly.

**Lemma 11.8.** *Let `C` be an `A`-coalgebra, `V` a `C`-comodule, `M` an `A`-submodule of `V`. Suppose that `C` is a
projective `A`-module.[^N.D.E-VI_B-C-113] Let `c(M)` be the image of the morphism of `A`-modules*

```text
              μ ⊗ id              id ⊗ ev
θ :   M ⊗_A C^∨ ────→ V ⊗_A C ⊗_A C^∨ ────→ V.
```

*Then `c(M)` is the smallest subcomodule of `V` containing `M`, and is a finitely generated `A`-module if `M` is. One
will say that `c(M)` is the subcomodule generated by `M`.*

*Moreover, for every morphism of rings `A → A′`, if one denotes by `M′` the image of `M ⊗_A A′` in `V′ = V ⊗_A A′`,
then `c(M′)` is the image of `c(M) ⊗_A A′` in `V′`, hence: "the formation of `c(M)` commutes with base change".*

<!-- label: III.VI_B.11.8 -->

[^N.D.E-VI_B-C-113]: In the original, it is assumed that `C` is a free `A`-module; the generalization to the case where `C` is a projective `A`-module, pointed out by J.-P. Serre, was mentioned in Remark 11.10.1. We have included this generalization here and in 11.9, and expanded the proofs accordingly.

First, `M ⊂ c(M)` by (CM 2), and if `N` is a subcomodule of `V` containing `M`, one has `μ(M) ⊂ N ⊗ C` and therefore
`c(M) ⊂ N`.

By hypothesis, `C` is a direct factor of a free `A`-module `L`, with basis `(e_i)_{i ∈ I}`. Denote by `φ_i` the
restriction to `C` of the linear form `e_i^*`, defined by `e_i^*(e_j) = δ_{ij}`. Let `x ∈ M`. One can write:

```text
(1)      μ(x) = ∑_{i ∈ J} x_i ⊗ e_i,
```

where `x_i ∈ V` and `J` is a finite subset of `I`. Then `x_i = θ(x ⊗ φ_i)` belongs to `c(Ax)`, and one therefore has
`c(Ax) = ∑_{i ∈ J} Ax_i`. Since `C` is a direct factor of `L`, say `L = C ⊕ R`, whence `V ⊗ L = (V ⊗ C) ⊕ (V ⊗ R)`,
one obtains that

```text
(c(Ax) ⊗ L) ∩ (V ⊗ C) = c(Ax) ⊗ C.
```

Consequently, `μ(x)` can also be written in the form

```text
(2)      μ(x) = ∑_{j ∈ J} x_j ⊗ b_j,
```

with `b_j ∈ C`. One can write `∆(b_j) = ∑_{i ∈ I} b_{ij} ⊗ e_i`, with `b_{ij} ∈ C`. Then, applying `μ ⊗ id` to (1)
(resp. `id ⊗ ∆` to (2)) and using the axiom (CM 1), one obtains, for every `i ∈ J`:

```text
μ(x_i) = ∑_{j ∈ J} x_j ⊗ b_{ij} ∈ c(Ax) ⊗ C.
```

This shows that `c(M)` is a subcomodule of `V`, and is therefore the smallest subcomodule of `V` containing `M`.

It is clear that `c(M)` is a finitely generated `A`-module if `M` is: if `M = Ax_1 + ⋯ + Ax_n` and
`μ(x_k) = ∑_i x_{ik} ⊗ e_i`, then `c(M)` is generated by the `x_{ik}`, for `k = 1, …, n` and `i` running through a
finite subset of `I`.

Finally, let `A → A′` be a morphism of rings and let `M′` be the image of `M ⊗ A′` in `V′ = V ⊗ A′`. Then `c(M′)`
(resp. the image of `c(M) ⊗ A′` in `V′`) is the image of the morphism `θ′` below (resp. of the composite `θ′ ∘ τ`):

```text
                   τ                    θ′
M ⊗ A′ ⊗ C^∨ ────→ M ⊗ Hom_A(C, A′) ────→ V′.
```

Now, these two morphisms have the same image. Indeed, let `ψ ∈ Hom_A(C, A′)` and `x ∈ M`. Set
`μ(x) = ∑_{i ∈ J} x_i ⊗ e_i`. Then

```text
θ′(x ⊗ ψ) = ∑_{i ∈ J} ψ(e_i) x_i
```

is the image by `θ′ ∘ τ` of the element `∑_{i ∈ J} x ⊗ ψ(e_i) ⊗ φ_i` of `M ⊗ A′ ⊗ C^∨`. This proves the lemma. ∎

Moreover, one has the following proposition:

**Proposition 11.8.bis.** [^N.D.E-VI_B-C-114] *Let `A` be a noetherian ring, `C` an `A`-coalgebra flat over `A`, `V` a
`C`-comodule, and `M` a finitely generated `A`-submodule of `V`. Then there exists a subcomodule `W` of `V`, finitely
generated over `A`, containing `M`.*

<!-- label: III.VI_B.11.8.bis -->

[^N.D.E-VI_B-C-114]: We have added this proposition, taken from [Se68], § 1.5, Prop. 2.

Indeed, since `M` is finitely generated, so is `∆_V(M)`, hence there exists a finitely generated `A`-submodule `M′` of
`V` such that `∆_V(M) ⊂ M′ ⊗_A C`. Let `π` be the projection `V → V/M′` and `∆̄_V = (π ⊗ id_C) ∆_V`, and let

```text
W = {x ∈ V | ∆̄_V(x) ∈ M′ ⊗_A C} = Ker ∆̄_V;
```

this is an `A`-submodule of `V` containing `M` and contained in `M′` (since `x = (id_V ⊗ ε) ∆_V(x)`), hence finitely
generated over `A`. Moreover, `(∆̄_V ⊗ id_C) ∆_V = (π ⊗ ∆_C) ∆_V` vanishes on `W`, i.e. `∆_V(W)` is contained in the
kernel `K` of `(∆̄_V ⊗ id_C)`. But since `C` is flat over `A`, one has `K = W ⊗ C`, hence `W` is a subcomodule of `V`. ∎

**Lemma 11.8.1.** [^N.D.E-VI_B-C-115] *Let `C` be an `A`-coalgebra, `V` a `C`-comodule, `M` an `A`-submodule of `V`,
and `f : A → A′` a faithfully flat morphism of rings. Suppose that `C′ = C ⊗ A′` is a projective `A′`-module.*

*(i) Then there exists a smallest subcomodule `t(M)` of `V` containing `M`, and `t(M)` is a finitely generated
`A`-module if `M` is. Moreover, "the formation of `t(M)` commutes with base change".*

*(ii) More precisely, `C` is a projective `A`-module, and one has `t(M) = c(M)`.*

<!-- label: III.VI_B.11.8.1 -->

[^N.D.E-VI_B-C-115]: We have added this lemma, which is used in the proof of 11.9.

*Proof.* (ii) By [RG71] (see Proposition 11.8.2 below), `C` is a projective `A`-module. One can therefore apply Lemma
11.8: `c(M)` is the smallest subcomodule of `V` containing `M`, it is a finitely generated `A`-module if `M` is, and
its formation commutes with base change.

To avoid an anachronism ([RG71] being subsequent to SGA 3), let us sketch a direct proof of point (i). Since
`A → A′` is flat, `M′ = M ⊗ A′` is an `A′`-submodule of `V′ = V ⊗ A′`, and, since `C′` is a projective `A′`-module,
`c(M′)` is the smallest subcomodule of `V′` containing `M′`. Denote by `V′ ⊗ A′` and `A′ ⊗ V′` the two
`A′ ⊗ A′`-comodule structures on `V′′ = V′ ⊗_{A′} (A′ ⊗ A′)` obtained by the two base changes `A′ ⇒ A′ ⊗ A′`,
`a′ ↦ a′ ⊗ 1` and `a′ ↦ 1 ⊗ a′`. The `A′`-comodule `V′` is equipped with an isomorphism of `A′ ⊗ A′`-comodules
`φ : V′ ⊗ A′ ⥲ A′ ⊗ V′`, `(x ⊗ a′) ⊗ b′ ↦ b′ ⊗ (x ⊗ a′)`, which is a descent datum, i.e. which satisfies
`φ_{31} = φ_{32} ∘ φ_{21}`.

Since `M′ = M ⊗ A′`, `φ` sends `M′ ⊗ A′` onto `A′ ⊗ M′`, and therefore `c(M′ ⊗ A′)` onto `c(A′ ⊗ M′)`. Since the
formation of `c(M′)` commutes with base change, one has `c(M′ ⊗ A′) = c(M′) ⊗ A′` and `c(A′ ⊗ M′) = A′ ⊗ c(M′)`. One
therefore has

```text
φ(c(M′) ⊗ A′) = A′ ⊗ c(M′)
```

and it follows that `φ` equips `c(M′)` with a descent datum. By (fpqc) descent, there exists a unique subcomodule
`t(M)` of `V` such that `c(M′) = t(M) ⊗ A′`, and `t(M)` contains `M` since `t(M) ⊗ A′` contains `M′`. Moreover, if `N`
is a subcomodule of `V` containing `M`, then `N` contains `t(M)`, since `N ⊗ A′` contains `c(M′) = t(M) ⊗ A′`. Hence
`t(M)` is the smallest subcomodule of `V` containing `M`.

Finally, let `A → B` be a morphism of rings. Let `B′ = B ⊗ A′` and let `M_B` (resp. `M′_{B′}`) be the image of
`M ⊗ B` in `V_B = V ⊗ B` (resp. of `M′ ⊗_{A′} B′` in `V ⊗ B′`); then `M_B ⊗_B B′ = M′_{B′}`. On the one hand, the
preceding construction, applied to `C_B` and to the morphism `B → B′`, gives:

```text
c(M_B ⊗_B B′) = t(M_B) ⊗_B B′ = t(M_B) ⊗ A′.
```

On the other hand, since the formation of `c(M′)` commutes with base change, `c(M′_{B′})` is the image in
`V′ ⊗_{A′} B′ = V ⊗ B ⊗ A′` of

```text
c(M′) ⊗_{A′} B′ = t(M) ⊗ B ⊗ A′.
```

It follows that `t(M_B)` is the image in `V_B` of `t(M) ⊗ B`. ∎

**Proposition 11.8.2 (Gruson–Raynaud).** *Let `f : A → A′` be a faithfully flat morphism; then `f` "descends
projectivity", i.e. if `M` is an `A`-module and if `M ⊗_A A′` is a projective `A′`-module, then `M` is a projective
`A`-module.*

<!-- label: III.VI_B.11.8.2 -->

Indeed, by [RG71] II 2.5.1, `f` "descends the Mittag-Leffler condition", and therefore, by loc. cit. II 3.1.3, `f`
descends projectivity.[^N.D.E-VI_B-C-116] ∎

[^N.D.E-VI_B-C-116]: Let us point out in passing that assertion II 2.5.2 of loc. cit., more general than II 2.5.1, is corrected in the article [Gr73] (this does not affect the case of faithfully flat morphisms).

**Proposition 11.9.** [^N.D.E-VI_B-C-117] *Let `C` be an `O_S`-coalgebra, `E` a `C`-comodule, `F` an `O_S`-submodule of
`E`, all quasi-coherent. Suppose given a covering of `S` by affine opens `U_α = Spec A_α`, and for each `α`, a
faithfully flat morphism of rings `A_α → A′_α` such that `Γ(U_α, C) ⊗_{A_α} A′_α` is a projective `A′_α`-module.[^VI_B-C-11-9]*

*Then there exists a smallest quasi-coherent subcomodule `t(F)` of `E` containing `F`, and `t(F)` is a finitely
generated `O_S`-module if `F` is. Moreover, for every base change `S′ → S`, if one denotes by `F ′` the image of
`F ⊗ O_{S′}` in `E ′ = E ⊗ O_{S′}`, then `t(F ′)` is the image of `t(F) ⊗ O_{S′}` in `E ′`, i.e. "the formation of
`t(F)` commutes with base change".*

<!-- label: III.VI_B.11.9 -->

[^VI_B-C-11-9]: This is the case, for example, when `C = 𝒜(G)`, where `G` is a reductive `S`-group, as we shall see in Exp. XXII 5.7.8.

[^N.D.E-VI_B-C-117]: As pointed out in N.D.E. (112), we have rewritten the statement for an `O_S`-coalgebra `C` (rather than for an `S`-group `G` satisfying the hypotheses indicated in Corollary 11.10). Moreover, we have spelled out the proof (the original indicated: "(⋯) the proposition is a consequence of Lemma 11.8.").

*Proof.* For each `α`, the `O_{U_α}`-module `𝒯_α` associated with the `A_α`-module `T_α = t(Γ(U_α, F))` is, by
11.8.1 (i), the smallest quasi-coherent subcomodule of `E|_{U_α}` containing `F|_{U_α}`, and is a finitely generated
`O_{U_α}`-module if `F|_{U_α}` is.

For all `α, β`, set `U_{αβ} = U_α ∩ U_β`. Since the construction of `t(M)` commutes with base change, one has, for all
`α, β`, canonical isomorphisms of `O_{U_{αβ}}`-modules

```text
φ_{αβ} : 𝒯_β ⊗_{A_β} O_{U_{αβ}} ⥲ 𝒯_α ⊗_{A_α} O_{U_{αβ}}
```

which satisfy the cocycle condition `φ′_{αγ} = φ′_{αβ} ∘ φ′_{βγ}`, where `φ′_{αγ}` (resp. ⋯) denotes the restriction
of `φ_{αγ}` (resp. ⋯) to `U_α ∩ U_β ∩ U_γ`.

Consequently, the `𝒯_α` glue together into a quasi-coherent subcomodule `t(F)` of `E` containing `F`. We leave to the
reader the task of verifying that `t(F)` is the smallest quasi-coherent subcomodule of `E` containing `F`, and that
its formation commutes with base change. ∎

**Definition 11.9.1.** [^N.D.E-VI_B-C-118] *Let `S` be a scheme and `P` a quasi-coherent `O_S`-module. The following
conditions are equivalent:*

*(i) For every affine open `U` of `S`, `Γ(U, P)` is a projective `O_S(U)`-module.*

*(ii) There exists a covering `(U_α)` of `S` by affine opens such that each `Γ(U_α, P)` is a projective
`O_S(U_α)`-module.*

*(iii) There exists a covering `(U_α)` of `S` by affine opens, and faithfully flat morphisms of rings
`A_α = O_S(U_α) → A′_α`, such that, for each `α`, `Γ(U_α, P) ⊗_{A_α} A′_α` is a projective `A′_α`-module.*

<!-- label: III.VI_B.11.9.1 -->

[^N.D.E-VI_B-C-118]: We have added this definition, taken from [RG71], bottom of p. 82. Thus, in Proposition 11.9, the hypothesis is that the coalgebra `C` is a locally projective `O_S`-module, and we have used this terminology in Corollary 11.10.

Indeed, it is clear that (i) ⇒ (ii) ⇒ (iii). Conversely, if (iii) is satisfied, 11.8.2 implies that each
`Γ(U_α, P)` is a projective `O_S(U_α)`-module, whence (ii). Finally, suppose (ii) satisfied and let `V = Spec A` be an
arbitrary affine open; it is covered by finitely many affine opens `V_1, …, V_n`, where each `V_i = Spec A_i` is
contained in at least one `V ∩ U_α`, so that `Γ(V_i, P)` is a projective `A_i`-module. Let
`A′ = A_1 × ⋯ × A_n`; then `A → A′` is faithfully flat and `Γ(V, P) ⊗_A A′` is a projective `A′`-module. Hence, by
11.8.2, `Γ(V, P)` is a projective `A`-module.

When these equivalent conditions are satisfied, one says that `P` is a *locally projective* `O_S`-module.

**Corollary 11.10.** *Let `S` be a quasi-compact and quasi-separated scheme, `G` an `S`-group, and `ρ` a linear action
of `G` on a quasi-coherent `O_S`-module `E`. Suppose that:*

*(i) `G` satisfies one of the following conditions:*

*a) `G` is affine and flat over `S`,*

*b) `G` is flat, quasi-compact and quasi-separated over `S`, and `E` is flat;*

*(ii) `𝒜(G)` is a locally projective `O_S`-module.*

*Then `E` is an inductive limit of a filtered increasing family of quasi-coherent finitely generated `O_S`-submodules
of `E`, stable under `G`.*

<!-- label: III.VI_B.11.10 -->

By hypothesis (i) and 11.6.1, `E` is equipped with an `𝒜(G)`-comodule structure. On the other hand, since `S` is
quasi-compact and quasi-separated, `E` is the inductive limit of its finitely generated quasi-coherent submodules
(EGA I, 9.4.9 and EGA IV₁, 1.7.7). Consequently, the corollary follows from Proposition 11.9, applied to the coalgebra
`𝒜(G)`. ∎

Moreover, one has the following proposition:

**Proposition 11.10.bis.** [^N.D.E-VI_B-C-119] *Let `S` be a noetherian scheme, `G` an `S`-group flat, quasi-compact
and quasi-separated over `S`, `E` a quasi-coherent `G`-`O_S`-module, `M` a coherent `O_S`-submodule of `E`. Then `M` is
contained in a coherent `O_S`-submodule stable under `G`.*

<!-- label: III.VI_B.11.10.bis -->

[^N.D.E-VI_B-C-119]: We have added this proposition, which is a particular case of [Th87], 1.4–1.5. The author makes reference there to an argument of Deligne (cf. [Kn71], III Th. 1.1); one may also note the similarity with the argument of Serre ([Se68], Prop. 2) recalled in 11.8.bis.

*Proof.* Denote by `f` the morphism `G → S` and by `τ` the adjunction morphism `E → f_* f*(E)`. By 11.6, the
`G`-`O_S`-module structure on `E` is given by an automorphism `θ` of the `O_G`-module `f*(E)`, such that the morphism
`δ = θ ∘ τ` satisfies conditions (1) and (2) of 11.6. (The situation considered in [Th87] is more general, in that the
author considers a `G`-scheme `X` and a `G`-equivariant `O_X`-module `E` (cf. Exp. I, Section 6); here `X = S` equipped
with the trivial action of `G`.)

Since `S` is noetherian, `E` is the filtered inductive limit of its coherent submodules `F_α` (cf. EGA I, 9.4.9). Then
`f*(E)` is the filtered inductive limit of the `f*(F_α)`, which are submodules of `f*(E)` since `f` is flat. Since,
moreover, `f` is quasi-compact and quasi-separated, by 11.0, the `O_S`-module `f_* f*(E)` is quasi-coherent and is the
filtered inductive limit of the quasi-coherent submodules `f_* f*(F_α)`. Consequently, `E` is the filtered inductive
limit of the quasi-coherent `O_S`-submodules `E_α`, where `E_α` denotes the inverse image by `δ` of `f_* f*(F_α)`,
i.e. the kernel of the composite morphism

```text
                δ                       
δ_α :   E ────→ f_* f*(E) ────→ f_* f*(E/F_α).
```

Since `M` is coherent and `S` noetherian, every increasing sequence of submodules of `M` is stationary, so `M` is
contained in some `E_α`. Let us show that each `E_α` is coherent and `G`-stable.

Let `u` be the morphism `f*(E) → ε_*(E)` corresponding by adjunction to the identity morphism from `E` to
`f_* ε_*(E) = E`; then the composite morphism

```text
         τ                f_*(u)
E ────→ f_* f*(E) ────→ f_* ε_*(E) = E
```

is the identity (cf. 11.6 (2)). Since one has a commutative diagram:

```text
            δ                  f_*(u)
   E_α ────→ f_* f*(F_α) ────→ F_α
    │                              │
i_α │                              │ j_α
    ↓        τ          f_*(u)     ↓
   E   ────→ f_* f*(E) ────→ E,
```

where `i_α` (resp. `j_α`) denotes the inclusion of `E_α` (resp. `F_α`) into `E`, one deduces that `i_α` factors
through `j_α`, i.e. `E_α` is a submodule of `F_α`, hence is coherent.

Let us finally show that `E_α` is `G`-stable (cf. 11.7.bis). Designate by `h : G → S` a second copy of `f : G → S` and
consider the following commutative diagram:

```text
              q
   G ×_S G ────→ G
        ╲         │
       p ╲      φ │ h
          ↘       ↓
           G ───→ S.
              f
```

Then the exact sequence

```text
                                 δ_α
0 ────→ E_α ────→ E ────→ h_* h*(E/F_α)
```

gives, since `f` is flat, the exact sequence

```text
(†)   0 ────→ f_* f*(E_α) ────→ f_* f*(E) ──f_* f*(δ_α)──→ f_* f* h_* h*(E/F_α).
```

Moreover, since `h` is quasi-compact and quasi-separated, and `f` flat, the canonical morphism

```text
f* h_* h*(E/F_α) → p_* q* h*(E/F_α) = p_* φ*(E/F_α)
```

is an isomorphism, so that the right-hand term in (†) is `φ_* φ*(E/F_α)`. Resuming the notations of 11.6 and denoting
by `π_α` the projection `E → E/F_α`, one obtains the commutative diagram below, whose bottom line is exact:

```text
                              δ                       
   E_α ────────────────────→ f_* f*(E)
    │                                  │ f_*(f*(π) ⊠ δ_G)
  δ │                                  ↓
f_* f*(E_α) ────→ f_* f*(E) ──f_* f*(δ_α)──→ φ_* φ*(E/F_α)
```

and since `f_*(f*(π) ⊠ δ_G) ∘ δ` vanishes on `E_α`, it follows that `δ` sends `E_α` into `f_* f*(E_α)`, i.e. that
`E_α` is `G`-stable. The proposition is proved. ∎

**Remark 11.10.1.** [^N.D.E-VI_B-C-120] In 11.8, it does not suffice to assume that `C` be a flat `A`-module, even if
`A` is a principal ring. Indeed, one has the following counterexamples, which were pointed out (independently) to us by
O. Gabber and J.-P. Serre.

<!-- label: III.VI_B.11.10.1 -->

[^N.D.E-VI_B-C-120]: The first part of the original Remark 11.10.1 has been incorporated into 11.8 and 11.9 (by replacing "free" by "projective"); the counterexamples below correct the second part.

(a) Let `(A, 𝔪)` be a discrete valuation ring, `K` its field of fractions, and `G` the "extension by zero" `A`-group
of the `K`-group `(ℤ/2ℤ)_K`. Then the constant group `(ℤ/2ℤ)_A`, and hence also its subgroup `G`, acts on the free
`A`-module `V` with basis `v_1, v_2` by exchanging `v_1` and `v_2`. Then `Av_1` is not a sub-`G`-module of `V`, but it
is the intersection of the sub-`G`-modules `Av_1 + 𝔪^n v_2`, for `n ∈ ℕ^*`. Hence there does not exist a smallest
sub-`G`-module of `V` containing `v_1`.

(b) Let `A` be an integral ring, distinct from its field of fractions `K`, and let `G` be the flat affine `A`-group
corresponding to the Hopf algebra

```text
𝒜(G) = {P ∈ K[T] | P(0) ∈ A},
```

the comultiplication, resp. the counit and the antipode, being defined by `∆(T) = T ⊗ 1 + 1 ⊗ T`, resp. `ε(T) = 0` and
`τ(T) = −T`. (N.B. One thus has `G ⊗_A K = G_{a,K}`.)

Let `V` be the free `A`-module `Av_1 ⊕ Av_2` and `u` the endomorphism of `V` defined by `u(v_1) = v_2`, `u(v_2) = 0`,
so that `u² = 0`. Then `V` is equipped with an `𝒜(G)`-comodule structure, defined by

```text
μ(m) = 1 ⊗ m + T ⊗ u(m).
```

The sub-`G`-modules of `V` containing `v_1` are exactly the sub-`A`-modules of the form `Av_1 ⊕ Iv_2`, for `I` a
non-zero ideal of `A`; their intersection is `Av_1`, which is not a sub-`G`-module. Hence there does not exist a
smallest sub-`G`-module of `V` containing `v_1`. (Note moreover that `C = A ⊕ K · T` is a sub-coalgebra of `𝒜(G)`,
flat over `A`, and that the coaction `μ : V → V ⊗ 𝒜(G)` factors through `V ⊗ C`, so one also obtains a counterexample
for the "very simple" coalgebra `C`.)

Finally, note that the two preceding examples are particular cases of the following construction. Let `A` be an
integral ring, distinct from its field of fractions `K`, let `B` be an `A`-Hopf algebra, free over `A`. Denote by
`ε : B → A` the augmentation of `B` and `I = Ker(ε)` the augmentation ideal. Since `B = A · 1 ⊕ I`, one easily sees
that `B′ = {b ∈ B ⊗_A K | ε(b) ∈ A}` is a sub-Hopf algebra of `B_K`. If `V` is a `B`-comodule, free with basis
`(v_1, …, v_n)` as `A`-module, and if `μ_V(v_1) ≠ v_1 ⊗ 1`, then `Av_1` is not a subcomodule of `V` but it is the
intersection of the subcomodules `Av_1 + I · V`, for `I` running through the non-zero ideals of `A`. Hence there does
not exist a smallest subcomodule of `V` containing `v_1`.

**Proposition 11.11.** *Let `G` be an algebraic group over the field `k`. The following conditions are equivalent:*

*(i) `G` is affine.*

*(ii) `G` is quasi-affine.*

*(iii) `G` acts faithfully on a quasi-affine `k`-scheme `X`.*

*(iv) `G` acts linearly and faithfully on a `k`-vector space (not necessarily of finite dimension).*

*(v) `G` is isomorphic to a closed subgroup of a group `GL(n)_k`.*

<!-- label: III.VI_B.11.11 -->

*Proof.* One has (i) ⇒ (ii) trivially, and (ii) ⇒ (iii), since `G` acts faithfully on itself by translations.

Suppose that `G` acts faithfully on the right on a quasi-affine `k`-scheme `X`.[^N.D.E-VI_B-C-121] Since `X` is
quasi-affine, it is separated and quasi-compact.[^N.D.E-VI_B-C-122] Similarly, `G` is separated (VI_A 0.3) and
quasi-compact (since of finite type over `k`). Hence, by 11.1 (c), one has canonical isomorphisms:

```text
O(X × G) = O(X) ⊗ O(G)     and     O(X × G × G) = O(X) ⊗ O(G) ⊗ O(G).
```

[^N.D.E-VI_B-C-121]: We have expanded the original in what follows; on the other hand, we have chosen to have `G` act on the right on `X` in order to obtain a left linear action of `G` on `O(X)`.

[^N.D.E-VI_B-C-122]: Recall that a `k`-scheme `X` is said to be quasi-affine if it is isomorphic to a quasi-compact open of an affine `k`-scheme (EGA II, 5.1.1).

One deduces that the morphism `μ : O(X) → O(X) ⊗ O(G)` induced by the morphism `X × G → X` equips `O(X)` with a right
`O(G)`-comodule structure, i.e. `G` acts linearly on the left on the `k`-algebra `O(X)`. Consequently, `G` also acts on
the right on the affine envelope `X_af = Spec O(X)` of `X`, and the canonical morphism `X → X_af` is `G`-equivariant.

Moreover, `X` being quasi-affine, `X → X_af` is an open immersion (EGA II, 5.1.2), hence a fortiori `G` acts faithfully
on `X_af`. One thus obtains that the linear (left) action of `G` on the `k`-algebra `O(X) = O(X_af)` is faithful. This
proves the implication (iii) ⇒ (iv).

Suppose now that `G` acts faithfully on a `k`-vector space `V`. Then, by virtue of 11.10, `V` is the inductive limit of
finite-dimensional vector subspaces `V_i`, stable under the action of `G`. If `K_i` is the kernel of the induced action
of `G` on `V_i`, i.e. of the morphism `G → Aut(V_i)`, then `K_i` is a closed subscheme of `G`, and the hypothesis that
`G` acts faithfully is expressed by the fact that the intersection of the `K_i` is the unit subgroup of `G`. Since `G`
is noetherian, it follows that one of the `K_i` is already reduced to the unit group, hence that `G → Aut(V_i)` is a
monomorphism. It is therefore a closed immersion by virtue of 1.4.2, which proves that (iv) ⇒ (v). Since (v) ⇒ (i)
trivially, this proves 11.11. ∎

**Remark 11.11.1.** One can generalize 11.11 as follows. Let `S` be a regular locally noetherian scheme of dimension
`≤ 1`, and `G` a group scheme flat, quasi-compact and quasi-separated over `S`. (In this case, `𝒜(G)` is a torsion-free
`O_S`-module, hence flat.)

<!-- label: III.VI_B.11.11.1 -->

(a) One then has the equivalence of the following conditions:[^N.D.E-VI_B-C-123]

(i) `G` is affine over `S`.

(ii) `G` is quasi-affine over `S`.

(iii) `G` acts faithfully on a quasi-affine and flat `S`-scheme.

(iv) `G` acts linearly and faithfully on a flat quasi-coherent `O_S`-module.

(b) If moreover `G` is of finite type over `S` and `S` noetherian, these conditions imply that `G` is isomorphic to a
closed subgroup of an `Aut(E)`, where `E` is a finitely generated locally free `O_S`-module.[^N.D.E-VI_B-C-124]

[^N.D.E-VI_B-C-123]: The equivalence of these conditions is proved in the additional section 12.

[^N.D.E-VI_B-C-124]: This is proved, with various generalizations, in the additional section 13.

**Lemma 11.12.** *Let `k` be a field, `G` an affine `k`-group. Set `A = 𝒜(G)`. Given `x ∈ A`, there exists a finitely
generated `k`-subalgebra `B` of `A` such that `x ∈ B`, that `∆(B) ⊂ B ⊗_k B`, and `u(B) ⊂ B`, where `u` denotes the
involution of `A` corresponding to the inversion morphism of `G`.[^N.D.E-VI_B-C-125]*

<!-- label: III.VI_B.11.12 -->

[^N.D.E-VI_B-C-125]: On the one hand, this is generalized in Section 13 to the case where `G` is affine and flat over a regular base of dimension `≤ 2`. On the other hand, in what follows we have spelled out and corrected the original.

One can suppose `x ≠ 0`; then `∆(x) ≠ 0` since `(ε ⊗ id) ∆(x) = x`, where `ε` denotes the augmentation (counit) of `A`.
Write

```text
(1)     ∆(x) = ∑_{j=1}^n e_j ⊗ a_j     with n minimal,
```

in which case the `e_j` (resp. `a_j`) are linearly independent. Complete `(e_1, …, e_n)` into a basis `(e_i)_{i ∈ I}`
of `A` and set, for `j ∈ J = {1, …, n}`,

```text
∆(e_j) = ∑_{i ∈ I} e_i ⊗ b_{ij}.
```

Applying `∆ ⊗ id` and `id ⊗ ∆` to (1), one obtains from the axiom (CO 1) of 11.8.0 (see also (HA 1) in I 4.2) the
equalities:

```text
∑_{j ∈ J} e_j ⊗ ∆(a_j) = ∑_{ℓ ∈ J} ∆(e_ℓ) ⊗ a_ℓ = ∑_{i ∈ I} e_i ⊗ (∑_{ℓ ∈ J} b_{iℓ} ⊗ a_ℓ).
```

Since the `e_i` are linearly independent, it follows that

```text
(2)     ∀ j ∈ J,     ∆(a_j) = ∑_{ℓ ∈ J} b_{jℓ} ⊗ a_ℓ.
```

Let then `B` be the finitely generated `k`-subalgebra of `A` generated by the `b_{ij}` and the `u(b_{ij})`, for
`i, j ∈ J`. It is clear that `u(B) = B`.

Applying `∆ ⊗ id` and `id ⊗ ∆` to (2), one obtains further from (CO 1) the equalities:

```text
∑_{ℓ ∈ J} ∆(b_{jℓ}) ⊗ a_ℓ = ∑_{i ∈ J} b_{ji} ⊗ ∆(a_i) = ∑_{i, ℓ ∈ J} b_{ji} ⊗ b_{iℓ} ⊗ a_ℓ,
```

and since the `a_ℓ` are linearly independent, one deduces that

```text
(3)     ∀ j, ℓ ∈ J,     ∆(b_{jℓ}) = ∑_{i ∈ J} b_{ji} ⊗ b_{iℓ}.
```

Since `∆ ∘ u = (u × u) ∘ v ∘ ∆`, where `v(a ⊗ b) = b ⊗ a`, one therefore also has

```text
(4)     ∀ j, ℓ ∈ J,     ∆(u(b_{jℓ})) = ∑_{i ∈ J} u(b_{iℓ}) ⊗ u(b_{ji}).
```

Since `∆` is an algebra homomorphism, one deduces from (3) and (4) that `∆(B) ⊂ B ⊗_k B`. Finally, the axiom (CO 2) of
11.8.0 (see also (HA 2) in I, 4.2) shows that `a_j = ∑_{i ∈ I} ε(a_j) b_{ij}` and that `x = ∑_{j ∈ J} ε(e_j) a_j`, so
that `x ∈ B`. ∎

**Proposition 11.13.** *Let `k` be a field and `G` an affine `k`-group with algebra `A`. Then `G` is a projective
limit of an increasing filtered system of finitely generated affine `k`-groups, whose transition morphisms are
faithfully flat.*

<!-- label: III.VI_B.11.13 -->

If `B` and `B′` are two finitely generated subalgebras of `A` stable under `∆` and `u`, then so is the subalgebra
generated by `B` and `B′`. Hence, by Lemma 11.12, `A` is the inductive limit of a filtered increasing family
`(B_i)_{i ∈ I}` of finitely generated subalgebras stable under `∆` and `u`. Then each `B_i`, equipped with the
restriction of `u` and the morphism `B_i → B_i ⊗_k B_i` deduced from `∆`, is a Hopf algebra, hence by I 4.2 it is the
algebra of an affine `k`-group `G_i`, of finite type over `k`. Finally, since `A = lim B_i`, one has `G = lim G_i`
(cf. EGA IV₃ 8.2.3). The transition morphisms are faithfully flat by the following lemma:

**Lemma 11.14.** *Let `k` be a field, `u : G → H` a morphism between finitely generated affine `k`-groups, and
`u^♮ : B → A`[^N.D.E-VI_B-C-126] the corresponding morphism of `k`-algebras. For `u` to be faithfully flat, it is
necessary and sufficient that `u^♮` be injective.*

<!-- label: III.VI_B.11.14 -->

[^N.D.E-VI_B-C-126]: We have denoted by `u^♮` (instead of `u°`) the morphism `B → A` corresponding to `u : Spec(A) → Spec(B)`.

The condition is obviously necessary (cf. EGA 0_I 6.6.1). Let us show it is sufficient. Set `N = Ker u`. Then, by
VI_A, 3.3.2 and 5.4.1, `G/N` is a finitely generated `k`-group and `u` factors as `G --p--> G/N --v--> H`, where `p` is
faithfully flat and `v` is a closed immersion. Hence, since `H` is an affine scheme, `G/N` is an affine scheme and the
morphism `v^♮ : B → O(G/N)` is surjective (cf. EGA I 4.2.3). Now, since `u^♮` is assumed injective, and since
`u^♮ = p^♮ ∘ v^♮`, then `v^♮` is also injective: it is therefore an isomorphism, as is `v`, and since `p` is
faithfully flat, so is `u`. ∎

**Definition 11.15.** [^N.D.E-VI_B-C-127] *Let `k` be a field, `G` a quasi-compact `k`-group and `V` a `k`-vector space
equipped with a `k`-linear action of `G`, hence with an `𝒜(G)`-comodule structure `δ : V → V ⊗ 𝒜(G)`, by 11.6.1. Let
`v ∈ V` be non-zero. The following conditions are equivalent:*

*(i) There exists `λ ∈ 𝒜(G)` (necessarily unique) such that `δ(v) = v ⊗ λ`.*

*(ii) For every `k`-algebra `R` and every `g ∈ G(R)`, one has `g · v ∈ Rv` (i.e. there exists `f ∈ R`, necessarily
unique, such that one has in `V ⊗ R` the equality `g · v = v ⊗ f`).*

<!-- label: III.VI_B.11.15 -->

[^N.D.E-VI_B-C-127]: We have added the hypothesis that `G` be quasi-compact and spelled out the equivalence of conditions (i) and (ii).

Indeed, it is clear that (i) ⇒ (ii). Conversely, if (ii) is satisfied and one applies it to `R = 𝒜(G)` and
`g = id_{𝒜(G)}`, one obtains that there exists a unique `λ ∈ 𝒜(G)` such that `δ(v) = v ⊗ λ`.

If `v` satisfies these conditions, one says that `v` is a *semi-invariant vector under `G`*, and that `λ` is the
*weight* of `v`; one will also say that "`v` is a semi-invariant of weight `λ`".

Denote by `∆` the comultiplication of `𝒜(G)`; then the equality

```text
v ⊗ λ ⊗ λ = (δ ⊗ id)(δ(v)) = (id ⊗ ∆)(δ(v)) = v ⊗ ∆(λ)
```

implies that `∆(λ) = λ ⊗ λ`. Consequently, `λ` defines a morphism of Hopf algebras

```text
𝒜(G_{m,k}) = k[T, T⁻¹] → 𝒜(G),    T ↦ λ,
```

and hence a morphism of `k`-groups `λ : G → G_{m,k}`, i.e. `λ` is a *character* of `G`, called the *character
associated with the semi-invariant vector `v`*.

**Lemma 11.16.0.** [^N.D.E-VI_B-C-128] *Let `k` be a field, `H` an affine `k`-group, `V` an `H`-module of dimension
`n` and `U` a vector subspace of `V` of dimension `d`. Consider the line `D = ⋀^d U ⊂ ⋀^d V`. For `U` to be stable
under `H`, it is necessary and sufficient that `D` be so.*

<!-- label: III.VI_B.11.16.0 -->

[^N.D.E-VI_B-C-128]: We have added this lemma, taken from [DG70], § II.2, 3.5.

Necessity being clear, let us prove sufficiency. One may suppose `d < n`. Let `(e_1, …, e_d)` be a basis of `U`,
complete it into a basis `(e_1, …, e_n)` of `V`. For every `k`-algebra `R`, `V_R = V ⊗ R` is a free `R`-module and one
has

```text
U_R = {v ∈ V_R | v ∧ (e_1 ∧ ⋯ ∧ e_d) = 0}
```

(since for `i > d` the `e_i ∧ e_1 ∧ ⋯ ∧ e_d` are linearly independent in `⋀^{d+1} V_R`). Since `H(R)` acts on
`⋀^• V_R` by

```text
h(x_1 ∧ ⋯ ∧ x_s) = h(x_1) ∧ ⋯ ∧ h(x_s),
```

it follows that if `H(R)` stabilizes `D_R = R e_1 ∧ ⋯ ∧ e_d`, it also stabilizes `U_R`. ∎

**Theorem 11.16 (Chevalley).** *Let `k` be a field, `G` an algebraic affine `k`-group, `H` a closed group subscheme of
`G`.[^N.D.E-VI_B-C-129] Then there exist a finite-dimensional `G`-module `V` and a line `D` in `V` such that
`H = Norm_G(D)`, i.e. such that for every `k`-algebra `R`,*

```text
H(R) = {g ∈ G(R) | g(D_R) = D_R}.
```

*In other words, there exist finitely many elements `a_1, …, a_n ∈ 𝒜(G)`, which are semi-invariant, all of the same
weight `λ`, for the "right" action of `H` (i.e. `a_i(gh) = λ(h) a_i(g)`, for every `k`-algebra `R` and `g ∈ G(R)`,
`h ∈ H(R)`), such that `H` be the largest closed group subscheme of `G` under which the `a_i` are semi-invariant.*

<!-- label: III.VI_B.11.16 -->

[^N.D.E-VI_B-C-129]: On the one hand, we recall that every group subscheme of `G` is closed (1.4.2). On the other hand, we have stated the result in the usual form: "`H` is the stabilizer of a line in a representation of `G`", while keeping the original formulation in terms of a sequence `a_1, …, a_n` of semi-invariants in `𝒜(G)`.

Denote by `∆` (resp. `ε`) the comultiplication (resp. the augmentation) of `A = 𝒜(G)`. Then `H = Spec(A/I)`, for some
ideal `I` of `A`, contained in `Ker ε` and such that `∆(I) ⊂ I ⊗ A + A ⊗ I`. Let `B = A/I` and `π` the projection
`A → B`. Consider the left action of `H` on `A` given by `(hφ)(g) = φ(gh)`; the corresponding `B`-comodule structure
is given by:

```text
∆̄ : A ──∆──→ A ⊗ A ──id_A ⊗ π──→ A ⊗ B.
```

Then `I` is a sub-`H`-module of `A`, since `∆̄(I) ⊂ I ⊗ B`.

On the other hand, `A` is a finitely generated `k`-algebra, hence noetherian, hence `I` admits a finite system of
generators `(x_1, …, x_r)`. By 11.8, the `x_i` are contained in a sub-`G`-module `V` of finite dimension over `k`.
Then `W = V ∩ I` is an `H`-module of finite dimension, whose dimension we denote by `d`. Since `V` contains all the
`x_i`, `W` generates the ideal `I`.

Set `E = ⋀^d V`, let `(w_1, …, w_d)` be a basis of `W`, and let `B = (e_0, …, e_n)` be a basis of `E` containing the
vector `e_0 = w_1 ∧ ⋯ ∧ w_d`. The action of `G` on `V` canonically determines an action of `G` on `E`, hence an
`A`-comodule structure `ρ : E → E ⊗ A`. For `j = 0, …, n`, set `ρ(e_j) = ∑_{i=1}^n e_i ⊗ b_{ij}`; one has seen in the
proof of 11.12 that

```text
(∗)     ∆(b_{ij}) = ∑_{ℓ=0}^n b_{iℓ} ⊗ b_{ℓj}.
```

Set `a_i = b_{i0}`, i.e. if `(e_0^*, …, e_n^*)` is the dual basis of `B`, the `a_i` are the "matrix coefficients"
`g ↦ e_i^*(g e_0)`. On the other hand, the action of `H` on `E` corresponds to:

```text
ρ̄ : E ──ρ──→ E ⊗ A ──id_E ⊗ π──→ E ⊗ B.
```

Since `W` is stable under `H`, `e_0` is semi-invariant under `H`, hence `ρ̄(e_0) = e_0 ⊗ π(a_0)` and `a_i = b_{i0}`
belongs to `I` for `i = 1, …, n`. Substituting this into (∗), one obtains `∆̄(a_i) = a_i ⊗ π(a_0)` for `i = 0, …, n`,
i.e. the `a_i` are semi-invariant under `H` with weight `π(a_0)`. (Moreover, possibly by replacing `E` by the
sub-`G`-module generated by `e_0` (cf. 11.8), one may assume that the `a_i` are linearly independent.)

Conversely, let `H′ = Spec B′`, where `B′ = A/I′`, be a closed group subscheme of `G` under which each of the `a_i` is
semi-invariant, with weight `λ_i ∈ B′` (this is the case, in particular, if `e_0` is invariant under `H′` with weight
`λ′`). Let us show that `H′ = H`. Denote by `π′` the projection `A → B′`; the hypothesis implies that

```text
a_i ⊗ λ_i = (id_A ⊗ π′) ∆(b_{i0}) = ∑_{ℓ=0}^n b_{iℓ} ⊗ π′(a_ℓ),
```

whence `λ_i = π′(a_0)` and `a_ℓ ∈ I′` for `ℓ = 1, …, n`, and hence `e_0` is semi-invariant under `H′`. By Lemma
11.16.0, this implies that `W` is stable under `H′`. Since the ideal `I` is generated by `W`, it is also stable under
`H′`, and therefore

```text
∆(I) ⊂ I ⊗ A + A ⊗ I′.
```

Since `I ⊂ Ker ε` and `(ε ⊗ id_A) ∘ ∆ = id_A`, it follows that `I ⊂ I′`, whence `H′ ⊂ H`. ∎

**Lemma 11.17.0.** [^N.D.E-VI_B-C-130] *Let `k` be an algebraically closed field, `G` a reduced algebraic affine
`k`-group, `V` a finite-dimensional `G`-module over `k`, and `v ∈ V`. Let `E` be the vector subspace of `V` generated
by the vectors `gv`, for `g ∈ G(k)`. Then `E` is the smallest sub-`G`-module of `V` containing `v`, and hence the
morphism `G × E → V`, `(g, x) ↦ gx`, factors through `E`.*

<!-- label: III.VI_B.11.17.0 -->

[^N.D.E-VI_B-C-130]: We have added this lemma, taken from the proof of thm. 5.6 of [DG70], § III.3 (by abuse of notation, we designate by the same letter `E` a `k`-vector space and the `k`-scheme in modules `W(E) = Spec S(E^*)`).

*Proof.* By 11.8, we know that there exists a smallest sub-`G`-module `U` of `V` containing `v`: if
`μ : V → V ⊗ 𝒜(G)` denotes the comodule structure and if one writes `μ(v) = ∑_{i=1}^n v_i ⊗ a_i` with the `a_i`
linearly independent, one has `U = Vect(v_1, …, v_n)`. It is clear that `U` contains `E`, and that the morphism
`G × U → V` factors through `U`.

Conversely, the inverse image of `E` by the morphism `μ_v : g ↦ gv` is a closed subset of `G` which contains the
rational points; now these are dense in `G`, since `G` is of finite type over `k` (cf. EGA IV₃, 10.4.8), hence
`μ_v⁻¹(E) = G` and so, since `G` is reduced, `μ_v` factors through `E`, whence `E = U`. ∎

**Theorem 11.17 (Chevalley).** *Let `k` be a field, `G` an affine `k`-group (not necessarily of finite type), and `N`
a closed group subscheme of `G` invariant in `G`; then the (fpqc) sheaf quotient `G/N` is representable by an affine
`k`-group.*[^N.D.E-VI_B-C-131]

<!-- label: III.VI_B.11.17 -->

[^N.D.E-VI_B-C-131]: For another proof of this theorem, not using the results of VI_A, see [Ta72], Th. 5.2 (see also Remark 11.18.5).

Suppose first `G` of finite type. By VI_A 3.2 and 5.2, the (fpqc) sheaf quotient `G/N` is representable by a `k`-group
`Q`; it therefore remains to show that `Q` is affine. The proof is done in several stages; suppose first `k`
algebraically closed.[^N.D.E-VI_B-C-132]

[^N.D.E-VI_B-C-132]: In what follows, we have spelled out the original (and corrected the erroneous assertion `(G/N)_red = G_red / N_red`), relying on [DG70], § III.3, 5.6.

(a) Suppose moreover `G` reduced and connected, and `N` reduced. By 11.16, there exist a `G`-module `V`, of finite
dimension over `k`, and a line `D = k e_0` such that `Norm_G(D) = N`; in particular `N` acts on `D` via a character
`χ : N → G_{m, k}`.

Fix `h ∈ N(k)`. For every `g ∈ G(k)`, one has `hg e_0 = g(g⁻¹ h g) e_0 = χ(g⁻¹ h g) g e_0`, hence `χ(g⁻¹ h g)` is an
eigenvalue of `h`. Hence the continuous map `φ : G(k) → k`, `g ↦ χ(g⁻¹ h g)`, takes only finitely many values, and
since `G(k)` is irreducible (since dense in `G`), one therefore has `φ(g) = φ(e) = χ(h)` for every `g ∈ G(k)`, and so

```text
χ(g⁻¹ h g) = χ(h),     ∀ g ∈ G(k), h ∈ N(k).
```

Let `E` be the vector subspace of `V` generated by the vectors `g e_0`, for `g ∈ G(k)`; by Lemma 11.17.0, this is the
sub-`G`-module of `V` generated by `e_0`.

By what precedes, the two morphisms `N × E → E`, `(h, x) ↦ hx` and `(h, x) ↦ χ(h) x`, coincide on the set of rational
points `(N × E)(k) = N(k) × E(k)`, which is dense in `N × E`. Since `N × E` is reduced (and `E` separated), these two
morphisms are therefore equal, so `N` acts on `E` by homotheties. Consequently, `N` is contained in the kernel `K` of
the morphism `ρ : G → GL(End_k(E))`, defined by `ρ(g)(u) = g u g⁻¹`, for every `g ∈ G(R)` and `u ∈ End_R(E ⊗ R)` (`R`
a `k`-algebra). On the other hand, if `g ∈ K(R)` then `g(R e_0) = R e_0`, whence `g ∈ N(R)`. This shows that `N = K`.
Then, by VI_A 5.4.1, the morphism `G/N → GL(End_k(E))` is a closed immersion, and hence `G/N` is affine.

(b) Suppose now `G` and `N` reduced, `G` not necessarily connected. Set `N′ = N ∩ G⁰`; then `G⁰/N′` is affine by (a).
On the other hand, `NG⁰` is an invariant subgroup of `G` and `G/NG⁰`, being a quotient of the finite constant group
`G/G⁰` (cf. VI_A, 5.5.1), is likewise a finite constant group. Hence `G/N` is the direct sum of the fibers of the
morphism `G/N → G/NG⁰`, all isomorphic to `NG⁰/N`, hence to `G⁰/N′`, by VI_A, 5.3.3. Hence `G/N` is affine.

(c) Suppose `G` reduced, and `N` arbitrary. The morphism `G × N → N`, `(g, h) ↦ ghg⁻¹`, induces a morphism
`(G × N)_red → N_red`; now, since `G` is reduced and `k` algebraically closed, one has `(G × N)_red = G × N_red`,
hence `N_red` is an invariant subgroup of `G`. (N.B. this fails when `G` is not reduced, cf. VI_A, 0.2.)

Hence, by (a), `G′ = G/N_red` is affine. On the other hand, by VI_A 5.6.1, `N′ = N/N_red` is a finite `k`-group, hence
by Theorem 4.1 of Exp. V, the quotient `G/N = G′/N′` is affine.

(d) For arbitrary `G` and `N`, the equivalence relation deduced from `G × N ⇒ G` by the base change `G_red → G` is:

```text
G_red × N′ ⇒ G_red,     where     N′ = N ∩ G_red.
```

Since the underlying spaces are the same (and since the quotient is the quotient ringed space), the morphism
`G_red / N′ → G/N` is a homeomorphism. Since `G_red / N′` is reduced (since `p : G_red → G_red/N′` is faithfully flat),
it follows that `(G/N)_red` is identified with `G_red / N′`, which is affine by (c). Since `G/N` is of finite type
over `k` (cf. VI_A, 3.3.2), this implies, by EGA I, 5.1.10, that `G/N` is affine.

Finally, for arbitrary `k`, let `k̄` be an algebraic closure of `k`. Then, by 9.2 (v), `(G ⊗_k k̄)/(N ⊗_k k̄)` is
isomorphic to `(G/N) ⊗_k k̄`, hence since the former is affine, so is the latter, and so `G/N` is also affine, by
(fpqc) descent (cf. EGA IV₂, 2.7.1). This proves 11.17 when `G` is of finite type. To extend this to the general case,
we shall need the following lemma.[^N.D.E-VI_B-C-133]

[^N.D.E-VI_B-C-133]: We have added this lemma, taken from [DG70], § III.3, 7.1.

**Lemma 11.17.1.** *Let `(C_i → A_i)_{i ∈ I}` be a filtered inductive system of ring morphisms, all faithfully flat.
Then `A = lim A_i` is faithfully flat over `C = lim C_i`.*

<!-- label: III.VI_B.11.17.1 -->

*Proof.* By [BAC] § I.3, Prop. 9, for a morphism of rings `B → B′` to be faithfully flat, it is necessary and
sufficient that it be injective and that `B′/B` be a flat `B`-module. Since each `C_i → A_i` is faithfully flat, one
therefore has exact sequences

```text
0 ────→ C_i ────→ A_i ────→ A_i / C_i ────→ 0
```

and `A_i / C_i` is a flat `C_i`-module, hence `(A_i / C_i) ⊗_{C_i} C` is a flat `C`-module. Since inductive limits are
exact and commute with the tensor product, one obtains an exact sequence

```text
0 ────→ C ────→ A ────→ A/C ────→ 0
```

as well as an isomorphism

```text
lim ((A_i / C_i) ⊗_{C_i} C) = (A/C) ⊗_C C = A/C,
```

from which one deduces that `A/C` is a flat `C`-module. Hence `A` is faithfully flat over `C`. ∎

Let us now return to the proof of 11.17 in the general case, i.e. when `G` is not assumed to be of finite type. Set
`𝒜(G) = A` and `𝒜(N) = B = A/J`. By 11.13, `A` is the inductive limit of a filtered increasing family
`(A_i)_{i ∈ I}` of finitely generated sub-Hopf algebras, hence `G` is the projective limit of the algebraic affine
`k`-groups `G_i = Spec(A_i)`. Denote by `∆` (resp. `τ`) the comultiplication (resp. the antipode) of `A`, and
`∆_2 = (∆ ⊗ id_A) ∘ ∆`.

For every `i`, `B_i = A_i / (J ∩ A_i)` is a quotient Hopf algebra of `A_i`, hence `N_i = Spec(B_i)` is a closed
subgroup of `G_i`. Moreover, since `N` is invariant in `G`, the morphism `G × N → G` defined by `(g, n) ↦ gng⁻¹`
factors through `N`, and this is equivalent to saying that the couple `(A, J)` satisfies the following property:

```text
(m_{13} ∘ (∆ ⊗ τ) ∘ ∆_2)(J) ⊂ A ⊗_k J
```

where `m_{13}` denotes the map `a_1 ⊗ a_2 ⊗ a_3 ↦ a_1 a_3 ⊗ a_2`. It follows that `(A_i, A_i ∩ J)` satisfies the
analogous property, hence that `N_i` is invariant in `G_i`. On the other hand, one has `lim B_i = B` and hence
`lim N_i = N`.

By what we have seen previously, each (fpqc) sheaf quotient `G_i / N_i` is representable by an affine `k`-group
`Q_i = Spec(C_i)`. Set `C = lim C_i`. One thus has a filtered projective system of affine `k`-groups `Q_i`; its
projective limit `Q = lim Q_i` is the `k`-group `Spec(C)` (cf. EGA IV₃, 8.2.3). One then has an exact sequence of
`k`-groups:

```text
1 ────→ N ────→ G ────→ Q.
```

Let us show that `Q` represents the (fpqc) sheaf quotient of `G` by `N`; for this, it suffices to verify that the
morphism `G → Q` is covering for the (fpqc) topology (cf. IV, 3.3.2.1 and 5.1.7.1). Now, each of the morphisms
`G_i → Q_i` is faithfully flat (cf. 9.2 (xi)), in other words `A_i` is faithfully flat over `C_i`; since `A = lim A_i`
and `C = lim C_i`, it follows from Lemma 11.17.1 that `A` is faithfully flat over `C`, so that `G → Q` is a faithfully
flat morphism. Since this morphism is affine, it is quasi-compact, hence covering for the (fpqc) topology. This
completes the proof of Theorem 11.17. ∎

### 11.18. Complements.

[^N.D.E-VI_B-C-134] Moreover, one deduces from 11.17 (and from its proof) the following results, taken from
[DG70], III § 3.7. Let `k` be a field. We begin with the following lemma (cf. [An73], 2.3.3.2), which will be useful
later (cf. 12.10).

[^N.D.E-VI_B-C-134]: We have added this subsection.

**Lemma 11.18.1.** *Let `u : G → G′` be a morphism of `k`-groups, `N = Ker(u)`. Suppose `G′` affine and `G` of finite
type.*

*(i) The morphism `τ : G/N → G′` is a closed immersion. In particular, `G/N` is affine.*

*(ii) If moreover the morphism `u^♮ : O(G′) → O(G)` is injective, then `τ` is an isomorphism. (And hence `G′` is of
finite type and `u` is faithfully flat.)*

<!-- label: III.VI_B.11.18.1 -->

Indeed, we know (11.13) that `G′` is the projective limit of a filtered system of algebraic affine `k`-groups `G′_i`.
Denote by `u_i` the composite morphism `G → G′ → G′_i` and by `N_i` its kernel. Then the `N_i` form a filtered
decreasing system of closed subgroups of `G`, whose intersection is `N`. Since `G` is noetherian, there exists an
index `i` such that `N = N_i`. Since `G` and `G_i` are of finite type, by VI_A, 3.2 and 5.4.1, the quotient `G/N` is a
finitely generated `k`-group and `u_i` is the composite of the projection `p : G → G/N`, which is faithfully flat, and
a closed immersion `τ_i : G/N ↪ G_i`.

Consider then the following commutative diagram:

```text
        u
   G ────────→ G′
   │       ↗
 p │   τ ╱      ╲ q_i
   ↓   ╱          ↘
   G/N ─────→ G_i.
        τ_i
```

Since `q_i ∘ τ = τ_i` is a closed immersion and `q_i` is separated (`G′` being separated, cf. VI_A, 0.3), then `τ` is
a closed immersion (cf. EGA I, 5.4.4). It follows that `G/N` is affine, and that the morphism
`τ^♮ : O(G′) → O(G/N)` is surjective, whence (i).

If moreover `u^♮ : O(G′) → O(G)` is injective, so is `τ^♮`, hence `τ^♮` is an isomorphism, hence so is `τ` (since `G′`
and `G/N` are affine). This proves (ii). ∎

**Theorem 11.18.2.** *Let `G` and `G′` be two affine `k`-groups, with algebras `A` and `A′`, and let `u : G → G′` be a
morphism of `k`-groups, `N = Ker(u)`, and `φ : A′ → A` the morphism induced by `u`.*

*(i) If `φ` is injective, then `u` is faithfully flat and identifies `G′` with `G/N`.*

*(ii) One has `G/N = Spec(B)`, where `B = φ(A′)`, and hence `u` is the composite of the faithfully flat morphism
`G → G/N`, corresponding to the inclusion `B ↪ A`, and of the closed immersion `G/N ↪ G′`, which corresponds to the
surjection `A′ → B`. Moreover, `N` is defined in `G` by the ideal `AB_+`, where `B_+` denotes the augmentation ideal of
`B`.*

*(iii) In particular, if `u` is a monomorphism, it is a closed immersion.*

<!-- label: III.VI_B.11.18.2 -->

*Proof.* (i) Suppose `φ` injective and identify `A′` with a sub-Hopf algebra of `A`. By 11.13, `A` is the filtered
union of finitely generated sub-Hopf algebras `A_i = O(G_i)`; denote `G′_i = Spec(A′_i)`, where `A′_i = A′ ∩ A_i`, and
`N_i` the kernel of the morphism `G_i → G′_i` induced by the inclusion `A′_i ↪ A_i`. By the preceding lemma, one has
`G_i / N_i ≅ G′_i` and one therefore obtains, for every `i`, an exact sequence

```text
                          p_i
1 ────→ N_i ────→ G_i ────→ G′_i ────→ 1
```

where `p_i` is faithfully flat. Since `G = lim_i G_i` and `G′ = lim_i G′_i`, one therefore obtains an exact sequence

```text
                     p
1 ────→ N ────→ G ────→ G/N
```

where one has set `N = lim_i N_i`. Moreover, by Lemma 11.17.1, `p` is faithfully flat (and affine), hence `G′`
represents the (fpqc) sheaf quotient of `G` by `N`. This proves (i).

In the general case, `B = φ(A′)` is a sub-Hopf algebra of `A`; denote by `H` the `k`-group `Spec(B)` and `N′` the
kernel of the morphism `G → H` induced by the inclusion `B ↪ A`. By (i), `H` is identified with `G/N′`, and `u` is
therefore the composite of the projection `G → G/N′` and the closed immersion `G/N′ ↪ G′` induced by the surjection
`A′ → B`. It follows that `N′ = N`. Moreover, by 9.2 (ii), one has a cartesian square:

```text
   N ────→ G
   │        │ p
   ↓   ε    ↓
Spec(k) ──→ G′
```

where `ε` is the unit section of `G′`, which corresponds to the augmentation morphism `B → k`. It follows that `N` is
defined in `G` by the ideal `AB_+`. This proves (ii), and (iii) follows. ∎

**Remark 11.18.3.** Let `G` be an affine `k`-group and `N` a normal `k`-subgroup. Since the morphism `p : G → G/N` is
faithfully flat and quasi-compact, by IV 3.3.3.2, `O(G/N)` is the subalgebra of `O(G)` formed of functions `φ` which
are right `N`-invariant, i.e. which satisfy `φ(gh) = φ(g)`, for every `k`-scheme `S` and `g ∈ G(S)`, `h ∈ N(S)`.
Denoting by `J` the ideal of `A = O(G)` which defines `N`, this is equivalent to saying that
`∆(φ) − φ ⊗ 1 ∈ O(G) ⊗ J`, where `∆` is the comultiplication of `A`.

<!-- label: III.VI_B.11.18.3 -->

The preceding theorem can then be reformulated in terms of Hopf algebras as follows.

**Corollary 11.18.4.** *Let `k` be a field, `A` a commutative `k`-Hopf algebra, `G = Spec(A)`.*

*(i) If `B` is a sub-Hopf algebra of `A`, then `A` is faithfully flat over `B`.*

*(ii) The map `N ↦ O(G/N)` is a bijection between the set of normal subgroups of `G` and that of sub-Hopf algebras of
`A`; the inverse map is given by `B ↦ Spec(A/AB_+)`. Moreover, if `J` is the ideal of `A` defining `N`, one has*

```text
O(G/N) = {x ∈ A | ∆(x) − x ⊗ 1 ∈ A ⊗ J}.
```

<!-- label: III.VI_B.11.18.4 -->

**Remarks 11.18.5.** (a) A consequence of the preceding theorem is that the category of commutative affine `k`-groups
is abelian. For this, as well as for other results on affine `k`-groups, we refer to [DG70], § III.3, 7.4 to 7.8.

(b) Let us finally point out that M. Takeuchi has given another proof of results 11.17 to 11.18.4, cf. [Ta72], § 5; he
moreover strengthened 11.18.4 (i) above by showing that `A` is even a projective `B`-module, cf. [Ta79], Th. 5 (see
also [MW94], Th. 3.6).

<!-- label: III.VI_B.11.18.5 -->

## 12. Complements on `G_af` and the "anti-affine" groups

<!-- label: III.VI_B.12 -->

[^N.D.E-VI_B-C-135] We begin with the following lemma, which extends 11.18.1 to the case where `G` is not assumed to
be of finite type.[^N.D.E-VI_B-C-136]

[^N.D.E-VI_B-C-135]: We have added this section.

[^N.D.E-VI_B-C-136]: This lemma was communicated to us by M. Raynaud; it will be used in the proof of Proposition 12.9.

**Lemma 12.1.** *Let `k` be a field, `u : G → H` a monomorphism of `k`-groups, with `H` affine. Suppose `u`
quasi-compact. Then `u` is a closed immersion.*

<!-- label: III.VI_B.12.1 -->

*Proof.* By (fpqc) descent, one may suppose `k` algebraically closed. By VI_A, 6.4, the closed image `I` of `u` is a
closed group subscheme of `H`, hence still affine. Hence, replacing `H` by `I`, one may suppose `u` schematically
dominant. Since `k` is algebraically closed, `H′ = H_red` is a group subscheme of `H`; set `G′ = G ×_H H′`; then the
morphism `u′ : G′ → H′` deduced from `u` by base change is a quasi-compact monomorphism, and is dominant (the
underlying continuous map being the same for `u` and `u′`). Hence, by VI_A, 6.2, `u′` is faithfully flat; it is
therefore a quasi-compact faithfully flat monomorphism, hence an isomorphism (cf. IV 1.14).

Hence `u : G → H` is a homeomorphism, so it is affine by 2.9.1. Hence `G` is affine, and so `u` is a closed immersion
by 11.18.2 (iii). ∎

**Theorem 12.2.** *Let `G` be an algebraic `k`-group. Denote by `ρ` the canonical morphism `G → G_af` and `N` its
kernel.*

*(i) The canonical morphism `G/N → G_af` is an isomorphism, and hence `G_af` is an algebraic affine group, and `ρ` is
faithfully flat.*

*(ii) One has a canonical isomorphism `(G/N)_af = G_af`.*

*(iii) `N` is a characteristic subgroup of `G`.*

*(iv) `O(N) = k`.*

*(v) `N` is smooth, connected, and commutative.*

<!-- label: III.VI_B.12.2 -->

*Proof.* Point (i) is a particular case of 11.18.1, and point (ii) follows from the universal properties of `G_af` and
`(G/N)_af`.

Let us prove (iii). For an arbitrary `k`-scheme `π : S → Spec k`, consider the cartesian square:

```text
   G_S ────→ G
    │         │
  q │         │ p
    ↓    π    ↓
    S ────→ Spec k.
```

Since `p` is quasi-compact and separated and `π` flat, by EGA III 1.4.15 and EGA IV₁ 1.7.21, one has
`q_*(O_{G_S}) = π*(O(G)) = π*(O(G_af))`, and hence, by EGA II, 1.5.2, one has `(G_S)_af = (G_af)_S`. Hence `N_S`, being
the kernel of the canonical morphism `G_S → (G_S)_af`, is invariant under every automorphism of `G_S`, i.e. `N` is a
characteristic subgroup of `G`.

To prove (iv), set `N′ = Ker(N → N_af)`; by (ii), this is an invariant subgroup of `G`. Since `N` is algebraic (being
a closed subgroup of `G`), by (i), `N/N′ ≅ N_af`; moreover, by VI_A, 3.2 and 5.3.2, one has an isomorphism of
`k`-groups

```text
(G/N′) / N_af ≅ (G/N′)/(N/N′) ≅ G/N.
```

Since `N_af` is affine, the projection `G/N′ → G/N` is also affine, by 9.2 (vii), and since `G/N = G_af` is affine, so
is `G/N′`. Hence, by the universal property of `G_af`, the projection `p′ : G → G/N′` factors through `G_af = G/N`,
whence `N ⊂ N′` and hence `N = N′`. Hence `N_af` is the trivial group, whence `O(N) = k`.

Finally, assertion (v) follows from the following lemma. ∎

**Lemma 12.3.** *Let `k` be a field and `N` an algebraic `k`-group such that `O(N) = k`. Then `N` is smooth,
connected, and commutative.*

<!-- label: III.VI_B.12.3 -->

Indeed, one may suppose `k` algebraically closed. Then `H = N⁰_red` is a `k`-subgroup of `N`, and the quotient
`k`-scheme `X = N/H` is finite (hence affine) over `k`, by VI_A, 5.5.1 and 5.6.1. Moreover, since `p : N → X` is
faithfully flat, one has `O(X) ⊂ O(N) = k`. It follows that `N = N⁰_red`, hence `N` is smooth (VI_A 1.3.1) and
connected.

Let then `Z` be the center of `N`. By 6.2.6, `N/Z` is affine, and one obtains as above that `O(N/Z) = k`, whence
`N = Z`. This proves 12.3 and completes the proof of 12.2. ∎

Let us also state, without proof, the following theorem. (Recall that an *abelian variety* over a field `k` is a
proper, smooth, and connected `k`-group scheme.)

**Theorem 12.4 (Chevalley).** *Let `k` be a perfect field and `G` an algebraic, smooth and connected `k`-group. Then
there exists an affine, smooth and connected `k`-subgroup `L`, invariant in `G`, such that the quotient `G/L` is an
abelian variety. Moreover, `L` is unique and its formation commutes with extension of the base field.*

<!-- label: III.VI_B.12.4 -->

**Remarks 12.5.** (1) This theorem was announced in 1953 by C. Chevalley, who published his proof in 1960 ([Ch60]).
Meanwhile, other proofs were obtained, independently, by I. Barsotti and M. Rosenlicht ([Ba55, Ro56]); see [Se99] for
historical comments.

(2) A modern version (i.e. in the language of schemes) of Chevalley's proof has been given by B. Conrad ([Co02]).
(Note that in loc. cit., "algebraic group" means smooth and connected `k`-group scheme.)

(3) On the other hand, a modern version of Rosenlicht's proof has been given by Ngô B.-C. in a course at Orsay in
2005-2006.

(4) If one drops the hypothesis that `k` is perfect, there still exists a smallest invariant connected affine subgroup
`L` (not necessarily smooth) such that `G/L` is an abelian variety ([BLR], § 9.2, Thm. 1).

(5) One may also drop the hypothesis that `G` is smooth over `k`: indeed, by VII_A, 8.3, there exists an integer
`n ≥ 1` such that the quotient `G′ = G/(Fr^n G)` is smooth; then `G′` contains a subgroup `L′` as in (4) above, and the
inverse image of `L′` in `G` still has the same properties. Hence, for every connected algebraic group `G` over a
field `k`, there exists an exact sequence

```text
1 ────→ H ────→ G ────→ A ────→ 1
```

where `H` is an affine `k`-group and `A` a `k`-abelian variety. Moreover, by [Per76], Cor. 4.2.9, one has such an
exact sequence for every connected `k`-group `G` (not necessarily algebraic).

(6) Let `k` be an algebraically closed field and `G` the semi-direct product of an elliptic curve `E` by the constant
`k`-group `{±1}_k`, for the action defined by `(−1) · x = −x`; in this case, if `L` is a closed invariant subgroup of
`G` such that `G/L` is connected, then `L = G`.

<!-- label: III.VI_B.12.5 -->

**Remark 12.6.** One will say, following [Br09], that a `k`-group `N` is *anti-affine* if `O(N) = k`. By 12.3 and
12.4, if `k` is perfect, every anti-affine algebraic `k`-group is an extension of an abelian variety by a smooth,
connected, commutative affine algebraic `k`-group. For the precise structure of anti-affine algebraic groups over a
perfect field, and various consequences, see the recent articles of M. Brion and C. & F. Sancho de Salas
([Br09, SS09]).

<!-- label: III.VI_B.12.6 -->

To conclude this section, we shall prove two results due to M. Raynaud, the first being Remark 11.11.1, the second
Proposition 2.1 of Exp. XVII, Appendix III. We shall need the following lemma,[^N.D.E-VI_B-C-137] which improves (for a
complete discrete valuation ring `R`) the flatness criteria given in [BAC], § III.5.

[^N.D.E-VI_B-C-137]: This is a version improved by O. Gabber of a statement communicated by M. Raynaud.

**Lemma 12.7.** *Let `R` be a discrete valuation ring, `K` its field of fractions, `π` a uniformizer. Let `A` be a
flat `R`-algebra and `M` an `A`-module flat over `R`. Suppose that:*

*(i) `M/πM` is a flat module over `Ā = A/πA`,*

*(ii) `M ⊗_R K` is a flat module over `A ⊗_R K`.*

*Then `M` is a flat `A`-module.*

<!-- label: III.VI_B.12.7 -->

*Proof.* By the flatness criterion in the nilpotent case (cf. [BAC], III § 5.2, Th. 1), `M/π^n M` is a flat module
over `A/π^n A`, for every `n ∈ ℕ^*`. It then follows from [RG71], II Lemma 1.4.2.1, that `M` is a flat `A`-module. For
the reader's convenience, let us briefly indicate the proof. Set `s = π^n` and `P = M/sM`. Since `P` is flat over
`A/sA` and the latter is of projective dimension 1 over `A`, it follows from the spectral sequence of composite
functors that `P` is of Tor-dimension `≤ 1` over `A`. Now, since `M` is `R`-flat hence without `π`-torsion, `M_K / M`
is the inductive limit of the `A`-modules `π⁻ⁿ M / M ≅ M / π^n M`, and hence `M_K / M` is also of Tor-dimension
`≤ 1`. Since one has the exact sequence `0 → M → M_K → M_K / M → 0` and by hypothesis `M_K` is flat over `A_K` hence
over `A`, it follows that `M` is flat.

For completeness, let us also indicate the following simpler proof, pointed out by O. Gabber. Let `I` be a finitely
generated ideal of `A`; one must show that the morphism `u : M ⊗_A I → M` is injective. By hypothesis (ii), `u ⊗_R K`
is injective, hence `Ker(u)` is an `R`-module of `π`-torsion. It therefore suffices to show that the `π`-torsion part
of `M ⊗_A I` is zero; now this is a quotient of `Tor^A_1(M, I/πI)`, as one sees by tensoring with `M` the exact
sequence:

```text
                π
0 ────→ I ────→ I ────→ I/πI ────→ 0.
```

On the other hand, `M` being without `π`-torsion (since flat over `R`), one obtains that `Tor^A_i(M, Ā) = 0` for every
`i ≥ 1`. Consequently, if `(P_•)` is a projective resolution of the `A`-module `M`, then `(P_• ⊗_A Ā)` is a projective
resolution of the `Ā`-module `M̄ = M/πM`, and hence for every `Ā`-module `N`, one has `Tor^A_i(M, N) = Tor^Ā_i(M̄, N)`,
and this is zero for `i ≥ 1` since `M̄` is flat over `Ā`. One thus has `Tor^A_1(M, I/πI) = 0`, which proves the lemma. ∎

**Remark 12.8.** Let `S` be a regular locally noetherian scheme of dimension 1, and `X` a flat, quasi-separated and
quasi-compact `S`-scheme. Then `𝒜(X)` is a flat `O_S`-module. Indeed, one may suppose `S` local; denote by `s` its
closed point, `i` the inclusion `X_s ↪ X`, and `π` a uniformizer of `R = O(S)`; since `X` is flat over `S`, one has an
exact sequence of sheaves

```text
                π
0 ────→ O_X ────→ O_X ────→ i_*(O_{X_s}) → 0
```

and so, by taking global sections, one obtains that `𝒜(X)` is an `R`-module without `π`-torsion, hence
flat.[^N.D.E-VI_B-C-138] One obtains moreover that the morphism from `𝒜((X_af)_s) = 𝒜(X)/π 𝒜(X)` to `𝒜(X_s)`, induced
by the morphism `X → X_af`, is injective.

<!-- label: III.VI_B.12.8 -->

[^N.D.E-VI_B-C-138]: This is true, more generally, if `S` is regular locally noetherian of dimension `≤ 2`, cf. [Ray70a], VII 3.2.

One can now prove the following proposition (cf. Remark 11.11.1).

**Proposition 12.9.** *Let `S` be a regular locally noetherian scheme of dimension `≤ 1`, `G` an `S`-group scheme
flat, quasi-separated and quasi-compact over `S`. Then the following conditions are equivalent:*

*(i) `G` is affine over `S`.*

*(ii) `G` is quasi-affine over `S`.*

*(iii) `G` acts faithfully on a quasi-affine and flat `S`-scheme `X`.*

*(iv) `G` acts linearly and faithfully on a quasi-coherent module `E` flat over `S`.*

*(v) The morphism `ρ : G → G_af` is a monomorphism.*

<!-- label: III.VI_B.12.9 -->

*Proof.* The implication (i) ⇒ (ii) is evident, as is (ii) ⇒ (iii) (take `X = G`).

Suppose (iii) holds. Since `𝒜(G)` and `𝒜(X)` are flat `O_S`-modules, one obtains, proceeding as in 11.11, that `G`
acts (on the right) faithfully on `X_af` and hence acts (on the left) linearly and faithfully on the flat
quasi-coherent `O_S`-module `𝒜(X)`.

Moreover, if (iv) holds, by 11.6.1 (ii), the monomorphism `G → Aut_{O_S}(E)` factors through `G_af`, hence
`G → G_af` is a monomorphism.

Finally, suppose (v) holds and let us show that `ρ : G → G_af` is an isomorphism. Replacing `S` by one of its
connected components, one may suppose `S` irreducible, with generic point `η`. Since the formation of `G_af` commutes
with flat base changes, one has `(G_af)_η = (G_η)_af`, and therefore the morphism `G_η → (G_η)_af` is a monomorphism,
hence a closed immersion by 12.1, hence an isomorphism since `O((G_η)_af) = O(G_η)`. If `S = Spec(κ(η))` we are done;
one may therefore suppose `dim S = 1`.

Let then `s` be a closed point of `S`; let us show that `G_s → (G_af)_s` is an isomorphism and that `ρ` is flat at
every point of `G_s`. For this, one may suppose `S` local, with closed point `s`. The morphism `ρ_s : G_s → (G_af)_s`
obtained by base change is a monomorphism, hence a closed immersion by 12.1, hence the morphism
`O((G_af)_s) → O(G_s)`, induced by `ρ_s`, is surjective. Now, by the preceding remark, it is also injective, hence it
is an isomorphism. (In particular, `ρ` is therefore surjective.)

It then follows from Lemma 12.7 that `ρ : G → G_af` is faithfully flat. Since `G` is quasi-compact over `S` and `G_af`
separated over `S`, `ρ` is also quasi-compact (cf. EGA I, 6.6.4). Consequently, `ρ` is a faithfully flat
quasi-compact monomorphism, hence an isomorphism. This proves the proposition. ∎

Finally, let us prove Prop. 2.1 of Exp. XVII, Appendix III; taking into account [Per76], Cor. 4.2.5, we have
substituted in the hypotheses "quasi-compact and quasi-separated" for "of finite type" (if one assumes `G` of finite
type, one can use 12.1 instead of loc. cit.).

**Proposition 12.10.** *Let `S` be a regular locally noetherian scheme of dimension `≤ 1`, `G` an `S`-group scheme
flat, quasi-compact and quasi-separated.*

*(i) The canonical morphism `ρ : G → G_af` is faithfully flat and quasi-compact. Consequently, `G_af` represents the
(fpqc) sheaf quotient of `G` by `N = Ker(ρ)`.*

*(ii) If moreover `G` is of finite type over `S`, then `ρ` is of finite presentation and `G_af` represents the (fppf)
sheaf quotient of `G` by `N` and is of finite type over `S`.*

*(iii) Suppose moreover `G_η` affine for every maximal point `η` of `S`. Then `N` is an étale `S`-group, and is the
unit group if `G` is separated over `S`.*

<!-- label: III.VI_B.12.10 -->

*Proof.* First, since `G_af` is affine, hence separated over `S`, `ρ` is quasi-compact (cf. EGA I, 6.6.4) and the
kernel `N = Ker(ρ)` is a closed subgroup of `G`. Moreover, replacing `S` by one of its connected components, one may
suppose `S` irreducible, with generic point `η`.

Let us remark that, to prove (i) and (ii), it suffices to show that `ρ` is faithfully flat, because then, by Exp. IV,
5.1.7.1, `G_af` represents the (fpqc) sheaf quotient of `G` by `N`, and if moreover `G` is of finite type over `S`,
hence of finite presentation (`S` being locally noetherian), then, by 9.2 (xiii), `ρ` is of finite presentation (as is
`G_af → S`) and hence `ρ` is covering for the (fppf) topology.

One may therefore suppose `S = Spec(R)`, where `R` is a discrete valuation ring (if `dim S = 1`) or else the field
`κ(η)` (if `dim S = 0`). Denote by `s` the closed point of `S`. Since the formation of `G_af` commutes with flat base
changes, the canonical morphism `G_η → (G_η)_af` is identified with the morphism `ρ_η : G_η → (G_af)_η`, and since
`O((G_af)_η) = O((G_η)_af) = O(G_η)`, then `ρ_η` is faithfully flat by [Per76], 4.2.5 (see also the addition
VI_A, 6.6). If `dim S = 1`, one similarly obtains that `ρ_s` is faithfully flat, since the morphism
`O((G_af)_s) → O(G_s)` is injective, by Remark 12.8. Hence, by Lemma 12.7, `ρ` is faithfully flat. This proves (i) and
(ii). In particular, `N` is flat over `S`.

Suppose now `G_η` affine. Since `ρ_η` coincides with the canonical morphism `G_η → (G_η)_af`, its kernel `N_η` is the
unit group. Let us show that `N` is étale over `S`. Since `N` is flat over `S`, it remains to see that `N_s` is étale
over `κ(s)`, for every point `s ≠ η` of `S`. There is nothing to prove if `S = Spec(κ(η))`, so one may suppose
`S = Spec(R)`, where `R` is a discrete valuation ring. Let `s` be the closed point of `S`, `K` the field of fractions
of `R`, and `π` a uniformizer. Let `x ∈ N_s` and `U_x` an affine open neighborhood of `x` in `N`; since `N` is flat
over `S`, `U_x ∩ N_η` is non-empty, hence equal to `{ε(η)}`, where `ε` denotes the unit section. Hence `A = O(U_x)` is
a flat `R`-algebra, such that `A_K = K` and `π⁻¹ ∉ A` (since `π` belongs to the maximal ideal of `O_{U,x}`). It
follows that `A = R`, and hence the projection `U_x → S` is an isomorphism. This proves that `N` is étale over `S`;
if moreover `G` is separated over `S`, then the inverse isomorphism `S → U_x` equals the unit section (since they
coincide on the dense open subset `{η}` of `S = Spec(R)`), hence `N` is the unit group. The proposition is proved. ∎

One obtains in particular the following corollary, two other proofs of which are found in [An73], Prop. 2.3.1 and
[PY06], Prop. 3.1.

**Corollary 12.10.1.** *Let `R` be a discrete valuation ring, `K` its field of fractions, `G` an `R`-group scheme
separated, flat and of finite type over `R`. If `G_K` is affine, then `G` is affine.*

<!-- label: III.VI_B.12.10.1 -->

**Remarks 12.10.2.** (a) On the one hand, O. Gabber has pointed out to us examples where `G` is a flat group of finite
type over a discrete valuation ring, whose generic fiber is an abelian variety, and where the kernel `N` of `G → G_af`
is not smooth.

(b) On the other hand, let us point out that M. Raynaud has given an example, for `S` the affine plane of dimension 2
over a field `k`, of a smooth and quasi-affine `S`-group scheme, with affine and connected fibers, which is not affine
over `S`, cf. [Ray70a], § VII.3, p. 116.

<!-- label: III.VI_B.12.10.2 -->

<!-- TRANSLATOR NOTE: §13 ("Groupes affines plats sur une base régulière de dimension ⩽ 2") and the Bibliography
remain to be translated. Translation paused here pending review; the per-statement structure for §13 is:
Lemma 13.1, Proposition 13.2, Example 13.3, Definition 13.4, Proposition 13.5, Remarks 13.6, Proposition 13.7,
followed by the bibliography. Source: /Users/jcreinhold/Code/papers/books/sga/iii/10-expose-06B-generalites-schemas-en-groupes.md
lines 5377–5680. -->

<!-- LEDGER DELTA — Exposé VI_B — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| passage à la limite projective | passage to the projective limit | Section-title rendering. |
| schéma à groupe d'opérateurs | scheme with operator group | Kept literal; SGA 3 distinguishes "groupe d'opérateurs" from a `G`-scheme. |
| di-morphisme | di-morphism | Preserve literally for pairs `(G, H) → (G′, H′)`. |
| espace formellement homogène | formally homogeneous space | 10.15. |
| fibré principal homogène | principal homogeneous bundle | 10.15; also "`G`-torseur" → "`G`-torsor". |
| enveloppe affine | affine envelope | `G_af = Spec 𝒜(G)`, Def. 11.3. |
| `𝒜(X) = f_*(O_X)` | `𝒜(X) = f_*(O_X)` | OCR sometimes lost the script-A; restored. |
| cogèbre | coalgebra | 11.8.0; American spelling. |
| coünité | counit | OCR may produce `coÃ¼nité`; restore. |
| comodule | comodule | Standard. |
| antipode | antipode | Hopf-algebra antipode `τ`. |
| sous-comodule engendré | subcomodule generated by | 11.8. |
| descente | descent | "descend la projectivité" → "descends projectivity". |
| localement projectif | locally projective | Def. 11.9.1. |
| vecteur semi-invariant | semi-invariant vector | 11.15. |
| poids | weight | 11.15 (semi-invariant weight). |
| Norm_G(D) | `Norm_G(D)` | Stabilizer of a line; 11.16. |
| caractéristique | characteristic | 12.2 (iii): "caractéristique" = "characteristic". |
| anti-affine | anti-affine | 12.6; Brion terminology. |
| variété abélienne | abelian variety | 12.4. |
| u♮ | `u^♮` | Algebra morphism dual to a group/scheme morphism. |
| coefficients matriciels | matrix coefficients | 11.16, 13.2 (with Hopf-algebra `b_{ij}`). |
| extension par zéro | extension by zero | 11.10.1 (a). |
| « anti-affines » | "anti-affine" | Guillemets rendered as English double quotes (Grothendieckian coinage). |
| (RE) (résolution équivariante) | equivariant resolution property (RE) | 13.4 (Thomason). |
| réflexif | reflexive | Module-theoretic, regular base of dim ≤ 2. |
-->



## 13. Flat affine groups over a regular base of dimension ≤ 2

<!-- label: III.VI_B.13 -->

[^N.D.E-VI_B-D-139] Let us begin by remarking that the well-known argument which shows that every affine algebraic
group over a field `k` is linear, as well as Lemma 11.12, extend to the case of a group scheme `G`, affine, flat, and
of finite type over a base scheme `S` which is noetherian, regular, of dimension `≤ 2`. For `S` of dimension `≤ 1`,
this proves point (b) of Remark 11.11.1. The extension to the case `dim S = 2` rests on the following lemma, which was
communicated to us by O. Gabber.

[^N.D.E-VI_B-D-139]: This section has been added.

**Lemma 13.1.** *Let `S` be a normal noetherian scheme, `𝒜` a flat quasi-coherent `O_S`-module, `ℱ` a quasi-coherent
`O_S`-submodule of finite type of `𝒜`, `ℱ**` its bidual, and `U` the flatness locus of `ℱ`, i.e. the set of points
`s ∈ S` such that `ℱ_s` is a flat `O_{S,s}`-module.*

*(i) `U` is an open subset of `S` and `ℱ** = j_* j*(ℱ)`, where `j` denotes the inclusion `U ↪ X`.*

*(ii) The canonical morphism `j_*(ℰ) ⊗_{O_S} 𝒜 → j_*(ℰ ⊗_{O_U} j*(𝒜))` is an isomorphism, for every quasi-coherent
`O_U`-module `ℰ`.*

*(iii) In particular, `𝒱 = j_* j*(ℱ)` is a submodule of `𝒜 = j_* j*(𝒜)`, and the canonical morphism
`𝒱 ⊗_{O_S} 𝒜 → j_* j*(ℱ ⊗_{O_S} 𝒜)` is an isomorphism.*

<!-- label: III.VI_B.13.1 -->

*Proof.* Replacing `S` by one of its connected components, we may suppose `S` integral. By EGA IV₂, 2.1.12, the
flatness locus of `ℱ`, i.e. the set of points `s ∈ S` such that `ℱ_s` is a flat `O_{S,s}`-module, is an open subset
`U` of `S`; denote by `j` the inclusion `U ↪ S`. Since `𝒜_s` is flat, hence torsion-free, so is `ℱ_s`,

<!-- original page 436 -->

so `U` contains every point of codimension `≤ 1`. Consequently, by [BAC], VII, § 4.2, cor. of th. 1, one has
`ℱ** = j_* j*(ℱ)`, and one therefore obtains a monomorphism `ℱ** → j_* j*(𝒜)`.

The proof of (ii) is analogous to that of EGA III, 1.4.15, recalled in 11.0. On the other hand, since `S` is normal,
the morphism `O_S → j_* j*(O_S)` is an isomorphism (cf. EGA IV₂, 5.8.6 and 5.10.5). By (ii) applied to `ℰ = O_U`, one
therefore has `𝒜 = j_* j*(𝒜)`. Finally, since `j*(ℱ ⊗_{O_S} 𝒜) = j*(ℱ) ⊗_{O_U} j*(𝒜)`, the final assertion of (iii)
follows from (ii) applied to `ℰ = j*(ℱ)`. The lemma is proved. ∎

Furthermore, recall that a finitely generated `R`-module `M` is said to be *reflexive* if the canonical morphism from
`M` to its bidual `M**` is an isomorphism. When `R` is a noetherian regular ring of dimension `≤ 2`, this entails that
`M` is projective. Indeed, for every finitely generated `R`-module `N`, consider a resolution `L_1 → L_0 → N → 0`,
where `L_0` and `L_1` are finitely generated free `R`-modules; then one has an exact sequence

```text
0 ⟶ N* ⟶ L_0* ⟶ L_1* ⟶ Q ⟶ 0,
```

where `Q` denotes the cokernel of `L_0* → L_1*`, and since `R` is of homological dimension `≤ 2` (cf. [BAC], X § 4.2,
cor. 1 of th. 1), it follows that `N*` is projective.

**Proposition 13.2.** *Let `S` be a noetherian regular scheme of dimension `≤ 2`, `G` an affine flat `S`-group, `𝒜(G)`
its affine algebra.*

*(i) If `G` is of finite type over `S`, it is isomorphic to a closed subgroup of `H = Aut_{O_S}(𝒱)`, for some
`O_S`-module `𝒱` locally free of finite rank. If moreover `S` is affine, one may take `𝒱 = O_S^{⊕d}` for some `d`,
whence `H = GL_{d,S}`.*

*(ii) `𝒜(G)` is a filtered inductive limit of flat `O_S`-sub-Hopf-algebras of finite type.*

<!-- label: III.VI_B.13.2 -->

*Proof.* Let `ℬ` be a finitely generated `O_S`-subalgebra of `𝒜(G)`. Since every coherent module on an open of `S`
extends to a coherent module on `S` (cf. EGA I, 9.4.5), there exists a coherent `O_S`-submodule `ℳ` of `ℬ` which
generates `ℬ` as an `O_S`-algebra (loc. cit., 9.6.5). By 11.10.bis, `ℳ` is contained in a coherent `G`-stable
`O_S`-submodule `ℱ`. (N.B. Since `G` is here affine over `S`, the proof of loc. cit. is written more simply: one may
there replace `f_* f*(ℰ)` by `ℰ ⊗_{O_S} 𝒜(G)`, etc.)

Let `j` be the inclusion `U ↪ S`, where `U` denotes the flatness locus of `ℱ`. By Lemma 13.1 and the remarks
following it, `𝒱 = j_* j*(ℱ)` is a locally free `O_S`-submodule of `𝒜(G)`, and since the canonical morphism

```text
𝒱 ⊗ 𝒜(G) ⟶ j_* j*(ℱ ⊗ 𝒜(G))
```

is an isomorphism, `𝒱` is a `G`-submodule of `𝒜(G)`. The action of `G` on `𝒱` then induces a morphism of affine
`S`-groups `ρ_𝒱 : G → H = Aut_{O_S}(𝒱)` and hence a morphism of `O_S`-Hopf algebras `φ_𝒱 : 𝒜(H) → 𝒜(G)`. Denote by
`𝒜_𝒱` the image of `φ_𝒱`; this is the affine algebra of a closed subgroup `G_𝒱` of `H`, which is the closed image of
`ρ_𝒱`. Let us show that `𝒜_𝒱` contains `ℬ`.

The question being local on `S`, one may suppose `S = Spec(R)` and `V = Γ(S, 𝒱)` is a free `R`-module with basis
`v_1, …, v_n`; in this case `H ≃ GL_{n,R}` and `𝒜(H)` is generated as an `R`-algebra by the "matrix coefficients"
`c_{ij}` and the element `d⁻¹`, where

<!-- original page 437 -->

`d` denotes the determinant. Let `Δ` (resp. `ε`) be the comultiplication (resp. the augmentation) of `A`. For
`j = 1, …, n`, write `Δ(v_j) = ∑_{i=1}^n v_i ⊗ a_{ij}`; then `a_{ij} = φ(c_{ij})` belongs to `Im(φ)`. On the other
hand, since `V` is an `R`-submodule of `A`, one can use the identity `(ε ⊗ id_A) ∘ Δ = id_A`, which entails that
`v_j = ∑_i ε(v_i) a_{ij}` belongs to `Im(φ)`. Since `V` contains a system of generators of `B = Γ(S, ℬ)`, it follows
that `B ⊂ Im(φ)`.

If `G` is of finite type over `S`, one may take `ℬ = 𝒜(G)` and `φ` is then surjective, so the morphism of `S`-groups
`G → H = Aut_{O_S}(𝒱)` is a closed immersion.

If moreover `S` is affine, there exists a locally free `O_S`-module `𝒱′` of finite rank such that `𝒱 ⊕ 𝒱′ = O_S^d` as
`O_S`-modules. Regarding `𝒱′` as a trivial `G`-module, one may replace `𝒱` by `O_S^d`, and one thus obtains that `G` is
a closed subgroup of `GL_{d,S}`.

Finally, let us return to the case of an arbitrary flat affine `S`-group `G`. By EGA I, 9.4.9, `𝒜(G)` is the union of
its coherent `O_S`-submodules `ℳ`, hence also of the `O_S`-sub-Hopf-algebras `𝒜_𝒱` as above, whence (ii). ∎

**Example 13.3.** *Let `R` be a discrete valuation ring, with uniformizer `π` and field of fractions `K`. Consider the
filtered projective system of `R`-groups:*

```text
···  ⟶  G_{a,R}  ⟶^{×π}  G_{a,R}  ⟶^{×π}  G_{a,R}
```

*(corresponding to the inductive system `R[X_0] → R[X_1] → R[X_2] → ⋯`, where the transition morphisms are given by
`X_n = π X_{n+1}`). Its projective limit `G` is a flat affine `R`-group scheme, not of finite type, whose special
fiber is trivial and whose generic fiber is `G_{a,K}`; the affine `R`-algebra `𝒜(G)` is the subring of `K[X]` formed of
polynomials whose constant coefficient belongs to `R`. (N.B. We have already encountered this example in Remark
11.10.1.) Note that `G` represents the functor which to every `R`-algebra `B` associates the set of sequences
`(x_n)_{n ∈ ℕ}` of elements of `B` such that `x_n = π x_{n+1}` for every `n`. (In particular, each `x_n` is
indefinitely `π`-divisible.)*

<!-- label: III.VI_B.13.3 -->

Now let `S` be a noetherian scheme such that every coherent `O_S`-module is the quotient of a locally free
`O_S`-module of finite type; this is the case, for example, if `S` is a separated noetherian regular scheme, cf.
SGA 6, Exp. II, 2.1.1 and 2.2.7. (One can show that every noetherian regular scheme of dimension `≤ 1` also has this
property; on the other hand, it fails when `S` is the affine plane over a field `k` with the origin doubled, cf. loc.
cit., 2.2.7.2.)

**Definition 13.4.** *Let `G` be a flat affine `S`-group. Following R. W. Thomason ([Th87], 2.1), we say that the pair
`(G, S)` possesses the* equivariant resolution property*, or satisfies (RE), if for every coherent `G`-`O_S`-module
`ℱ`, there exists a locally free `G`-`O_S`-module `ℰ` of finite rank and a `G`-equivariant epimorphism `ℰ → ℱ`.*

<!-- label: III.VI_B.13.4 -->

In loc. cit., Th. 3.1, Thomason proves the result below, under the hypothesis that `G` is essentially free over `S`
(cf. the remark further on). Gabber pointed out to us the simpler proof below, which does not use this hypothesis.

**Proposition 13.5.** *Let `S` be a noetherian scheme and `G` an `S`-group affine, flat, and of finite type, with
affine algebra `𝒜(G)`. Suppose that `(G, S)` satisfies (RE). Then:*

<!-- original page 438 -->

*(i) `G` is isomorphic to a closed subgroup of `H = Aut_{O_S}(𝒱)`, for some `O_S`-module `𝒱` locally free of finite
rank.*

*(ii) If moreover `S` is affine, one may take `𝒱 = O_S^{⊕d}` for some `d`, whence `H = GL_{d,S}`.*

<!-- label: III.VI_B.13.5 -->

The proof is analogous to that of 13.2. As in loc. cit., there exists a coherent `G`-stable `O_S`-submodule `ℱ` which
generates `𝒜 = 𝒜(G)` as an `O_S`-algebra. Replacing `S` by one of its connected components, we may suppose `S`
connected. By hypothesis (RE), there exists a locally free `G`-`O_S`-module `ℰ` of rank `n`, and an epimorphism of
`𝒜`-comodules `π : ℰ → ℱ`. Set `H = Aut_{O_S}(ℰ)`; this is an `S`-group scheme, locally isomorphic to `GL_{n,S}`. The
action of `G` on `ℰ` induces a morphism of affine `S`-groups `ρ : G → H`, corresponding to a morphism of `O_S`-Hopf
algebras `φ : 𝒜(H) → 𝒜(G)`. Let us show that `ρ` is a closed immersion.

The question being local on `S`, one may suppose `S = Spec(R)` and `V = Γ(S, ℰ)` is a free `R`-module with basis
`v_1, …, v_n`; in this case `H ≃ GL_{n,R}` and `B = Γ(S, 𝒜(H))` is generated as an `R`-algebra by the "matrix
coefficients" `c_{ij}` and the element `d⁻¹`, where `d` denotes the determinant. Let `Δ` (resp. `ε`) be the
comultiplication (resp. the augmentation) of `A = Γ(S, 𝒜(G))`, let `μ : V → V ⊗_R A` be the `A`-comodule structure on
`V`, and let `F = Γ(S, ℱ)`. For `j = 1, …, n`, write

```text
μ(v_j) = ∑_{i=1}^n v_i ⊗ a_{ij}
```

then `φ(c_{ij}) = a_{ij}`. On the other hand, since `π : V → F` is a morphism of `A`-comodules, one has

```text
∑_{i=1}^n π(v_i) ⊗ a_{ij} = (π ⊗_R id_A)(μ(v_j)) = Δ(π(v_j))
```

and therefore

```text
π(v_j) = (ε ⊗_R id_A) Δ(π(v_j)) = ∑_{i=1}^n (ε π(v_i)) a_{ij} = φ(∑_{i=1}^n (ε π(v_i)) c_{ij}).
```

Hence `φ(B)` contains `π(V) = F`, which generates `A` as an `R`-algebra, and hence `φ` is surjective. This shows that
`ρ` is a closed immersion, whence assertion (i).

If moreover `S` is affine, there exists a locally free `O_S`-module `𝒱′` of finite rank such that
`𝒱 ⊕ 𝒱′ = O_S^d` as `O_S`-modules. Regarding `𝒱′` as a trivial `G`-module, one may replace `𝒱` by `O_S^d`, and one
thus obtains that `G` is a closed subgroup of `GL_{d,S}`. The proposition is proved. ∎

**Remarks 13.6.** (a) For the sake of completeness, let us briefly sketch Thomason's argument ([Th87], Th. 3.1),
keeping the preceding notation. The `G`-equivariant epimorphism `π : ℰ → ℱ` induces a closed immersion
`τ : G → V(ℰ)` such that `τ(g′ g) = τ(g′) · g` (N.B.: `G` acts on the right on `V(ℰ)`), and one has an isomorphism
`H ≃ Aut_{O_S}(V(ℰ))^{op}`, which is compatible with the actions of `G` on the left on `ℰ` and on the right on
`V(ℰ)`. Now let `N` be the strict transporter `Transp^{str}_H(τ(G), τ(G))`; when `G` is essentially free over `S`, it
follows from 6.2.4 e) that `N` is a closed subgroup scheme of `H`, hence affine over `S`. Moreover, `ρ` factors
through a

<!-- original page 439 -->

morphism of `S`-groups `ρ′ : G → N`. On the other hand, for every `S′ → S` and `h ∈ N(S′)`, set `π(h) = τ(1) · h`
(where `1` is the unit element of `G(S′)`); this defines a morphism of `S`-schemes `π : N → τ(G)`, which is a
retraction of `ρ′` (when one identifies `G` with `τ(G)`). Since `N` is separated over `S`, it follows that `ρ′` is a
closed immersion.

(b) It seems that the proof of [Th87], Th. 3.1 requires the hypothesis that `G` be essentially free over `S`, which
does not appear in loc. cit. (the author invoking in its place the fact that `H` is essentially free). This hypothesis
is however satisfied when `G` is reductive (cf. Exp. XXII 5.7.8), and so is satisfied in all the cases considered in
loc. cit., Cor. 3.2. In particular, Thomason proves in loc. cit., 2.5, that if `S` is separated noetherian regular of
dimension `≤ 2`, and if `G` is affine, of finite presentation, and such that `𝒜(G)` is a locally projective
`O_S`-module, then `(G, S)` satisfies (RE); by 13.5, this gives 13.2 under a slightly more restrictive hypothesis.

<!-- label: III.VI_B.13.6 -->

To conclude, let us point out that the proof of [Th87], 2.5, may be slightly simplified, as follows. (For brevity, we
place ourselves in the situation where `S = Spec(R)` is affine.)

**Proposition 13.7.** *Let `R` be a noetherian regular ring of dimension `≤ 2`, `C` an `R`-coalgebra, projective as an
`R`-module, and `F` a `C`-comodule, of finite type over `R`. Then `F` is the quotient of a `C`-comodule `V`,
projective of finite type over `R`.*

<!-- label: III.VI_B.13.7 -->

*Proof.* Replacing `Spec(R)` by one of its connected components, one may suppose `R` integral, with field of fractions
`K`. Denote by `Δ` (resp. `ε`) the comultiplication (resp. the augmentation) of `C` and by `ρ : F → F ⊗ C` the
comodule structure on `F`. Let `π : W → F` be a surjective morphism, where `W` is a free `R`-module of finite rank. We
endow `W ⊗ C` with the comodule structure defined by `id_W ⊗ Δ`, and similarly for `F ⊗ C`. Then `ρ : F → F ⊗ C` is a
morphism of `C`-comodules, which admits `id_F ⊗ ε` as a section.

Let `W′` be the `C`-comodule defined by the cartesian square below:

```text
W′ ─────────⟶ F
│             │
│ π ⊗ id_C   │ ρ
↓             ↓
W ⊗ C ──────⟶ F ⊗ C
```

i.e. `W′` is identified with the kernel of the morphism `W ⊗ C → (F ⊗ C)/ρ(F)`, and the projection `π′ : W′ → F`,
given by `x ↦ (π ⊗ ε)(x)`, is surjective. Since `F` is a finitely generated `R`-module, there exists a subcomodule
`V′` of `W′`, finitely generated over `R`, such that `π′(V′) = F`. Since `W ⊗ C` is `R`-torsion-free, so is `V′`;
hence, replacing `F` by `V′`, one may assume at the outset that `F` is torsion-free.

Applying the preceding construction to this new `F`, one obtains `V′` as above. Consider then the subcomodule `V`,
kernel of the morphism

```text
W ⊗ C ⟶ E = (W ⊗ C ⊗ K) / (V′ ⊗ K).
```

Then `V` contains `V′`, and `Q = (W ⊗ C)/V` is an `R`-submodule of the `K`-vector space `E`; set `Q′ = E/Q`. Since
`W ⊗ C` and `E` are flat `R`-modules, one obtains that,

<!-- original page 440 -->

for every `R`-module `N`,

```text
Tor₁^R(V, N) ≃ Tor₂^R(Q, N) ≃ Tor₃^R(Q′, N)
```

and since `R` is regular of dimension `≤ 2`, the right-hand term is zero. This shows that `V` is a flat `R`-module.
Let us finally show that `V` is a finitely generated `R`-module. Set `M = W ⊗ C`; it follows from the definition that
`V/V′` is isomorphic to the `R`-torsion submodule `(M/V′)_{tors}` of `M/V′`.

Since `M` is a projective `R`-module, there exists a projective `R`-module `P` such that `M ⊕ P` is a free
`R`-module `L`. Then `(M/V′)_{tors} ≃ (L/V′)_{tors}`. On the other hand, since `V′` is of finite type, there exists a
direct factor `L′ ≃ R^n` of `L` such that `V′ ⊂ L′`, and one therefore also has `(L/V′)_{tors} ≃ (L′/V′)_{tors}`, and
the latter is of finite type since `(L′/V′)` is. Consequently, `V` is a flat `R`-module of finite type, hence
projective of finite type (`R` being noetherian). Proposition 13.7 is proved. ∎

## Bibliography

[^N.D.E-VI_B-D-140]

[An73] S. Anantharaman, *Schémas en groupes, espaces homogènes et espaces algébriques sur une base de dimension 1*,
Mém. Soc. Math. France **33** (1973), 5–79.

[Ba55] I. Barsotti, *Un teorema di struttura per le varietà gruppali*, Atti Acad. Naz. Lincei Rend. Cl. Sci. Fis. Mat.
Nat. **18** (1955), 43–50.

[BLR] S. Bosch, W. Lütkebohmert, M. Raynaud, *Néron Models*, Springer-Verlag, 1990.

[BAC] N. Bourbaki, *Algèbre commutative*, Chap. I–IV, V–VII et X, Masson, 1985 et 1998.

[BTop] N. Bourbaki, *Topologie générale*, Chap. I–IV, Hermann, 1971.

[Br09] M. Brion, *Anti-affine algebraic groups*, J. Algebra **321** (2009), no. 3, 934–952.

[Ch60] C. Chevalley, *Une démonstration d'un théorème sur les groupes algébriques*, J. Maths. Pure Appl. **39**
(1960), 307–317.

[Co02] B. Conrad, *A modern proof of Chevalley's theorem on algebraic groups*, J. Ramanujan Math. Soc. **17** (2002),
1–18.

[DG70] M. Demazure, P. Gabriel, *Groupes algébriques*, Masson & North-Holland, 1970.

[Gr73] L. Gruson, *Dimension homologique des modules plats sur un anneau noethérien*, Symposia Mathematica **XI**
(1973), 243–254.

[Kn71] D. Knutson, *Algebraic spaces*, Lect. Notes Maths. **203**, Springer-Verlag, 1971.

[Ma07] B. Margaux, *Passage to the Limit in Non-Abelian Čech Cohomology*, J. Lie Theory **17** (2007), 591–596.

[MW94] A. Masuoka, D. Wigner, *Faithful flatness of Hopf algebras*, J. Algebra **170** (1994), 156–184.

[^N.D.E-VI_B-D-140]: Additional references cited in this Exposé.

<!-- original page 441 -->

[Per76] D. Perrin, *Approximation des schémas en groupes, quasi-compacts sur un corps*, Bull. Soc. Math. France
**104** (1976), 323–335.

[Pes66] C. Peskine, *Une généralisation du "Main Theorem" de Zariski*, Bull. Sci. Math. **90** (1966), 119–127.

[PY06] G. Prasad, J.-K. Yu, *On quasi-reductive group schemes*, J. Alg. Geom. **15** (2006), 507–549.

[Ray70a] M. Raynaud, *Faisceaux amples sur les schémas en groupes et les espaces homogènes*, Lect. Notes Maths.
**119**, Springer-Verlag, 1970.

[Ray70b] M. Raynaud, *Anneaux locaux henséliens*, Lect. Notes Maths. **169**, Springer-Verlag, 1970.

[RG71] M. Raynaud, L. Gruson, *Critères de platitude et de projectivité*, Invent. math. **13** (1971), 1–89.

[Ro56] M. Rosenlicht, *Some basic theorems on algebraic groups*, Amer. J. Math. **78** (1956), 401–443.

[SS09] C. Sancho de Salas, F. Sancho de Salas, *Principal bundles, quasi-abelian varieties and structure of algebraic
groups*, J. Algebra **322** (2009), no. 8, 2751–2772.

[Se68] J.-P. Serre, *Groupes de Grothendieck des schémas en groupes réductifs déployés*, Publ. math. I.H.É.S. **34**
(1968), 37–52.

[Se99] C. S. Seshadri, *Chevalley: some reminiscences*, Transform. Groups **4** (1999), nos. 2–3, 119–125.

[Ta72] M. Takeuchi, *A correspondence between Hopf ideals and sub-Hopf algebras*, Manuscripta Math. **7** (1972),
251–270.

[Ta79] M. Takeuchi, *Relative Hopf modules — Equivalences and freeness criteria*, J. Algebra **60** (1979), 452–471.

[Th87] R. W. Thomason, *Equivariant resolution, linearization, and Hilbert's fourteenth problem over arbitrary base
schemes*, Adv. Math. **65** (1987), 16–34.

<!-- LEDGER DELTA — Exposé VI_B — for consolidation in Phase 3 (chunk-D add-on)
| French | English | Note |
| ------ | ------- | ---- |
| lieu de platitude | flatness locus | 13.1; the set of points where the module is flat. |
| bidual | bidual | 13.1; `M**` = double `R`-dual. Standard English. |
| réflexif | reflexive | Of finitely generated `R`-modules; bidual map is an isomorphism. |
| dimension homologique | homological dimension | 13.1 rappel; cf. [BAC] X § 4.2. |
| sous-G-module | `G`-submodule | 13.2; submodule stable under the `G`-action. |
| sous-OS-module G-stable | `G`-stable `O_S`-submodule | 13.2, 13.5; coherent submodule preserved by the comodule structure. |
| coefficients matriciels | matrix coefficients | 13.2, 13.5; Hopf-algebra generators of `𝒜(GL_n)`. |
| comultiplication | comultiplication | `Δ`. Standard. |
| augmentation | augmentation | `ε`. Standard. |
| algèbre affine | affine algebra | `𝒜(G)`. Already in chunk-C ledger. |
| sous-Hopf-algèbre plate | flat sub-Hopf-algebra | 13.2 (ii). |
| limite inductive filtrante | filtered inductive limit | 13.2 (ii). Already standard. |
| système projectif filtrant | filtered projective system | 13.3. Inverse system indexed by a filtered category. |
| fibre spéciale / générique | special / generic fiber | 13.3. |
| indéfiniment π-divisible | indefinitely `π`-divisible | 13.3; `xn = π x_{n+1}` for all `n`. |
| propriété de résolution équivariante (RE) | equivariant resolution property (RE) | 13.4; following Thomason [Th87]. Already in chunk-C ledger. |
| G-OS-module | `G`-`O_S`-module | 13.4; an `O_S`-module endowed with a `G`-action. |
| épimorphisme G-équivariant | `G`-equivariant epimorphism | 13.4. |
| transporteur strict | strict transporter | 13.6 (a); `Transp^{str}_H(τ(G), τ(G))`. |
| essentiellement libre | essentially free | 13.6; Thomason's hypothesis on `G` (or `H`) over `S`. |
| localement projectif | locally projective | 13.6 (b); already in chunk-C ledger (Def. 11.9.1). |
| R-cogèbre | `R`-coalgebra | 13.7; "cogèbre" → "coalgebra", American spelling. |
| C-comodule | `C`-comodule | 13.7. Already in chunk-C ledger. |
| sans R-torsion / sans torsion | `R`-torsion-free / torsion-free | 13.7. |
| sous-module de R-torsion | `R`-torsion submodule | 13.7; `(M/V′)_{tors}`. |
| facteur direct | direct summand / direct factor | 13.7; kept as "direct factor" to match the French structure of the argument. |
| carré cartésien | cartesian square | 13.7; pullback diagram. |
| rétraction | retraction | 13.6 (a); section in the opposite direction. |
| section unité | unit section | (Carried over from §12; mentioned implicitly in 13.6 (a) via `τ(1)`.) |
| algèbre de Hopf (sous-) | (sub-) Hopf algebra | 13.2 (ii). Standard. |
| OS-module localement libre de rang fini | locally free `O_S`-module of finite rank | 13.2 (i), 13.5 (i). |
| GLd,S | `GL_{d,S}` | 13.2, 13.5; relative general linear group. |
| AutOS(V) | `Aut_{O_S}(𝒱)` | 13.2, 13.5; automorphism group scheme of a locally free module. |
| V(ℰ) | `V(ℰ)` | 13.6 (a); the linear `S`-scheme `Spec Sym ℰ*` (covariant linear-scheme functor). |
-->
