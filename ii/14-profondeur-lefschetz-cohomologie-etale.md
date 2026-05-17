# Exposé XIV. Depth and Lefschetz theorems in étale cohomology

*by Mme M. Raynaud, after unpublished notes of A. Grothendieck*[^XIV-0-1]

<!-- label: XIV -->

> **Translator note.** Per Raynaud's opening footnote, this Exposé adopts the modern terminology in which *scheme* denotes what Exposés I–XIII of SGA 2 called *prescheme*, and *separated scheme* denotes what they called *scheme*. This Exposé therefore breaks with the prescheme/scheme convention used elsewhere in this translation; the shift is deliberate and matches Raynaud's own.

> **Typographic note.** Throughout this Exposé we write `RΓ_Y` for the sheafified derived functor (underlined in source) and `RΓ_Y` for the global one; context disambiguates. Likewise, `ℋ^p_Y(F)` denotes the sheafified local cohomology and `H^p_Y(X, F)` the global one.

<!-- original page 203 -->

In §1 we define a notion of "étale depth" which is, in étale cohomology, the analogue of the notion of depth studied in III in the cohomology of coherent sheaves. After a technical part, we prove in §4 some "Lefschetz theorems", the central theorem being 4.2. Let `X` be a scheme, `Y` a closed part of `X`, `U` the complementary open set `X − Y`, and `F` an abelian sheaf on `X` for the étale topology; in a general manner, the aim of the Lefschetz theorems is to show that, if `F` satisfies certain local conditions on `U`, expressible in terms of étale depth at the points of `U`, then under certain supplementary global conditions on `U` (for example `U` affine), the natural map of étale cohomology groups

```text
H^i(X, F) → H^i(Y, F|Y)
```

is an isomorphism for values `i < n`, where `n` is a certain explicit integer. By taking for `F` a constant sheaf, one obtains in this way conditions for `π₀(X)` to equal `π₀(Y)` and conditions for the abelianized fundamental groups of `X` and `Y` to be the same. In §5, the introduction of a notion of "geometrical depth" enables us to give useful particular cases of the Lefschetz theorems (5.7). Finally in §6 we mention some conjectures, concerning in particular "non-commutative" variants of the theorems obtained.

## 1. Cohomological and homotopical depth

<!-- original page 204 -->

**1.0.** Fix the following notations. Let `X` be a scheme[^XIV-1-1], `Y` a closed part of `X`, `U` the complementary open set, and `i : Y = X − U → X` the canonical immersion. Let `ΓY` be the functor that, to an abelian sheaf on `X`, associates the "sheaf of sections with support in `Y`", that is `ΓY = i_* i^!` (cf. SGA 4 IV 3.8 and VIII 6.6), and let `Γ_Y` be the functor `Γ ∘ ΓY` (where `Γ` is the "global sections" functor). Consider the derived category `D⁺(X)` and the derived functor `RΓ_Y` (resp. `RΓ_Y`) of `Γ_Y` (resp. of `ΓY`) (cf. [3]). Given a complex `F` of abelian sheaves on `X` bounded below, we may consider it as an element of `D⁺(X)`; we then denote by `ℋ^p_Y(F)` the `p`-th cohomology sheaf of `RΓ_Y(F)` (sheafified) and by `H^p_Y(X, F)` the `p`-th cohomology group of `RΓ_Y(F)`. The results of (SGA 4 V 4.3 and 4.4) extend trivially to `ℋ^p_Y(F)` and `H^p_Y(X, F)`.

**Proposition 1.1.**
<!-- label: XIV.1.1 -->

Let `X` be a scheme, `Y` a closed part of `X`, `U` the complementary open set, and `i : U → X` the canonical immersion. Denote by `F` either a sheaf of sets on `X`, a sheaf of groups on `X`, or a complex of abelian sheaves on `X` bounded below. Fix the following notations: if `X′ → X` is a morphism, `U′` and `F′` denote the inverse images of `U` and `F` on `X′`; furthermore, if `y` is a geometric point of `X`, `X̄` denotes the strict localization of `X` at `y` and `Ū`, `F̄` the inverse images of `U` and `F` on `X̄`.

<!-- original page 205 -->

1°) Let `F` be a sheaf of sets on `X` and `n` an integer `⩽ 2`; then the following conditions are equivalent:

(i) The canonical morphism

```text
F → i_* i^* F
```

is injective if `n ⩾ 1`, bijective if `n ⩾ 2`.

(ii) For every scheme `X′` étale over `X`, the canonical morphism

```text
H⁰(X′, F′) → H⁰(U′, F′)
```

is injective if `n ⩾ 1`, bijective if `n ⩾ 2`.

Suppose moreover that `U` is retrocompact in `X`; then the preceding conditions are equivalent to the following:

(iii) For every geometric point `y` of `Y`, the canonical morphism

```text
H⁰(X̄, F̄) → H⁰(Ū, F̄)
```

is injective if `n ⩾ 1`, and bijective if `n ⩾ 2`.

2°) Let `F` be a sheaf of groups on `X` and `n` an integer `⩽ 3`; then the following conditions are equivalent:

(i) The canonical morphism

```text
F → i_* i^* F
```

is injective if `n ⩾ 1`, bijective if `n ⩾ 2`, and if `n ⩾ 3`, in addition to the preceding conditions, the pointed sheaf of sets `R¹ i_* (i^* F)` is null.

(ii) For every scheme `X′` étale over `X`, the canonical morphism

```text
H⁰(X′, F′) → H⁰(U′, F′)
```

<!-- original page 206 -->

is injective if `n ⩾ 1`, bijective if `n ⩾ 2`, and moreover the canonical morphism

```text
H¹(X′, F′) → H¹(U′, F′)
```

is injective if `n ⩾ 2`, bijective if `n ⩾ 3`.

(ii bis) Identical to (ii), except in the case `n = 2` where one only supposes `H⁰(X′, F′) → H⁰(U′, F′)` bijective.

Suppose moreover that `U` is retrocompact in `X`; then the preceding conditions are also equivalent to the following:

(iii) For every geometric point `y` of `Y`, the canonical morphism

```text
H⁰(X̄, F̄) → H⁰(Ū, F̄)
```

is injective if `n ⩾ 1`, bijective if `n ⩾ 2`; finally if `n ⩾ 3`, in addition to the preceding conditions, `H¹(Ū, F̄)` is null.

3°) Let `F` be a complex of abelian sheaves bounded below and `n` an integer; then the following conditions are equivalent:

(i) One has `ℋ^p_Y(F) = 0` for `p < n` (cf. 1.0).

(ii) For every scheme `X′` étale over `X`, the canonical morphism

```text
H^p(X′, F′) → H^p(U′, F′)
```

is bijective for `p < n − 1`, injective for `p = n − 1`.

Suppose `U` retrocompact in `X`, then the preceding conditions are also equivalent to the following:

(iii) For every geometric point `y` of `Y`, the canonical morphism

```text
H^p(X̄, F̄) → H^p(Ū, F̄)
```

is bijective for `p < n − 1`, injective for `p = n − 1`.

<!-- original page 207 -->

In the case where `F` is an abelian sheaf and `n ⩾ 2`, conditions (i) and (ii) are also equivalent to the following:

(ii bis) For every scheme `X′` étale over `X`, the canonical morphism

```text
H^p(X′, F′) → H^p(U′, F′)
```

is bijective for `p < n − 1`.

*Proof.*

1°) It is clear that (i) ⇔ (ii). Let us show that, if `U` is retrocompact in `X`, (i) ⇔ (iii). Indeed, (i) amounts to saying that for every geometric point `y` of `X`, the morphism `F_y → (i_* i^* F)_y` is injective if `n ⩽ 1` and bijective if `n ⩽ 2` (SGA 4 VIII 3.6). Since this morphism is bijective in any case when `y` is a geometric point of `U`, one can restrict to geometric points `y` of `Y`. Now it follows from the fact that `i` is quasi-compact and from (SGA 4 VIII 5.3) that the morphism

```text
F_y → (i_* i^* F)_y
```

is canonically identified with the morphism

```text
H⁰(X̄, F̄) → H⁰(Ū, F̄),
```

whence the equivalence of (i) and (iii).

2°) (i) ⇒ (ii). The assertions about `H⁰` follow from 1°). Let `i′` be the canonical immersion of `U′` into `X′`; the assertions about `H¹` follow from the exact sequence (SGA 4 XII 3.2)

```text
0 → H¹(X′, i′_* i′^* F′) → H¹(U′, F′) → H⁰(X′, R¹ i′_* (i′^* F′)).
```

<!-- original page 208 -->

(ii bis) ⇒ (i). By 1°), it suffices to show that, for `n ⩾ 3`, one has `R¹ i_* (i^* F) = 0`. Now `R¹ i_* (i^* F)` is the sheaf associated to the presheaf `X′ ↦ H¹(U′, F′)`, that is, by hypothesis, the sheaf associated to the presheaf `X′ ↦ H¹(X′, F′)`, which is null.

(i) ⇔ (iii). Taking 1°) into account, the only thing that remains to see is that the relation `R¹ i_* (i^* F) = 0` is equivalent to the fact that `H¹(Ū, F̄) = 0` for every geometric point `y` of `Y`. Since `R¹ i_* (i^* F)` is null outside `Y`, it amounts to the same to say that `R¹ i_* (i^* F) = 0` or that `(R¹ i_* (i^* F))_y = 0` for every geometric point `y` of `Y`. It then suffices to note that, `i` being quasi-compact, one has `(R¹ i_* (i^* F))_y = H¹(Ū, F̄)` (SGA 4 VIII 5.3).

3°) (i) ⇒ (ii). Let `X′` be a scheme étale over `X`; one has the exact sequence (SGA 4 V 4.5)

```text
(∗)    → H^p_{Y′}(X′, F′) → H^p(X′, F′) → H^p(U′, F′) →;
```

so (ii) is equivalent to `H^p_{Y′}(X′, F′) = 0` for `p < n` and for every scheme `X′` étale over `X`. Consider then the spectral sequence

```text
E_2^{pq} = H^p(X′, ℋ^q_{Y′}(F)) ⟹ H^{p+q}_{Y′}(X′, F′);
```

by hypothesis, `ℋ^q_Y(F) = 0` for `q < n`, whence `E_2^{pq} = 0` for `p + q < n` and consequently `H^p_{Y′}(X′, F′) = 0` for `p < n`.

(ii) ⇒ (i). The sheaf `ℋ^p_Y(F)` is associated to the presheaf `X′ ↦ H^p_{Y′}(X′, F′)`; since we have already remarked that (ii) is equivalent to the relation `H^p_{Y′}(X′, F′) = 0` for `p < n` and for every scheme `X′` étale over `X`, one indeed has `ℋ^p_Y(F) = 0` for `p < n`.

(i) ⇔ (iii). The sheaves `ℋ^p_Y(F)` are concentrated on `Y`; consequently it amounts to the same

<!-- original page 209 -->

to say that `ℋ^p_Y(F) = 0` or that, for every geometric point `y` of `Y`, the fiber `(ℋ^p_Y(F))_y` is null. Now, `i` being quasi-compact, one deduces from (SGA 4 VIII 5.2) that one has `(ℋ^p_Y(F))_y = H^p_Ȳ(X̄, F̄)`. The equivalence of (i) and (iii) follows, taking into account the analogue on `X̄` of the exact sequence (∗).

(ii bis) ⇒ (ii) in the case where `F` is an abelian sheaf. The only thing that remains to show is that `ℋ^{n−1}_Y(F) = 0`. Now, for `n > 2`, the sheaf `ℋ^{n−1}_Y(F)` is associated to the presheaf `X′ ↦ H^{n−2}(U′, F′) = H^{n−2}(X′, F′)`, hence is null. The case `n = 2` follows from the fact that `ℋ¹_Y(F)` is the cokernel of the morphism `F → i_* i^* F`.

**Definition 1.2.**
<!-- label: XIV.1.2 -->

The notations are those of 1.1. One says that `F` is of `Y`-étale depth `⩾ n` and writes

```text
prof_Y(F) ⩾ n
```

if `F` satisfies the equivalent conditions (i) and (ii) of 1.1. If `F` is a complex of abelian sheaves, one calls `Y`-étale depth of `F` the supremum of the `n`

<!-- original page 210 -->

for which `prof_Y(F) ⩾ n`; one will use the same notation if `F` is a sheaf of sets, resp. of not-necessarily-commutative groups (so that one then has `0 ⩽ prof_Y(F) ⩽ 2`, resp. `0 ⩽ prof_Y(F) ⩽ 3`, when context does not allow confusion as to which of the three variants envisaged here one is using).

If `L` is a set of prime numbers, one says that the `Y`-étale depth for `L` of `X` is `⩾ n` and writes

```text
prof_Y^L(X) ⩾ n
```

if, for every constant sheaf of the form `ℤ/ℓℤ` with `ℓ ∈ L`, one has `prof_Y(ℤ/ℓℤ) ⩾ n`. One defines in the obvious way the `Y`-étale depth for `L` of `X`. If `L = P`, the set of all prime numbers, and if there is no risk of confusion with the notation of (EGA IV 5.7.1) (relative to the case `F = O_X`), one omits `L` in the notation; otherwise one writes `prof_Y^ét(X)`.

Finally one says that `X` is of `Y`-homotopical depth `⩾ 3` for `L` and writes

```text
prof_Y^{hopL}(X) ⩾ 3
```

if, for every constant finite sheaf of `L`-groups `F` on `X`, one has `prof_Y(F) ⩾ 3`. If `L = P`, one omits `L` in the notation.

**Corollary 1.3.**
<!-- label: XIV.1.3 -->

Under the conditions of 1.1, if `prof_Y(F) ⩾ n`, then for every closed subset `Z` of `Y`, one has

```text
prof_Z(F) ⩾ n.
```

Let us, for example, carry out the reasoning in the case where `F` is a complex of abelian sheaves bounded below. We use 1.1 3°) (ii). Let `V = X − Z` and consider, for every integer `p`, the sequence of morphisms

```text
H^p(X, F) --f--> H^p(V, F) --g--> H^p(U, F).
```

By hypothesis `g` and `f ∘ g` are bijective for `p < n − 1` and injective for `p = n − 1`; the same therefore holds for `f`. Since the reasoning is valid when one replaces `X` by a scheme `X′` étale over `X`, this proves 1.3.

**Corollary 1.4.**
<!-- label: XIV.1.4 -->

<!-- original page 211 -->

The notations are those of 1.1 2°). If `X′` is a scheme over `X`, denote by `Φ′` the functor that associates to an étale covering of `X′` its restriction to `U′`, and by `Φ′_{F′}` the functor that associates to a torsor[^XIV-1-2] under `F′` its restriction to `U′`. Then the following conditions are equivalent:

(i) One has `prof_Y(F) ⩾ 1` (resp. `prof_Y(F) ⩾ 2`, resp. `prof_Y(F) ⩾ 3`).

(ii) For every scheme `X′` étale over `X`, the functor `Φ′_{F′}` is faithful (resp. fully faithful, resp. an equivalence of categories).

In particular, in order that `prof_Y(X) ⩾ 1` (resp. `prof_Y(X) ⩾ 2`, resp. `prof_Y^{hop}(X) ⩾ 3`), it is necessary and sufficient that the functor `Φ′` be faithful (resp. fully faithful, resp. an equivalence of categories).

This indeed follows from 1.1 2°) (ii), taking into account the interpretation of `H¹(X′, F′)` as the set of classes (mod isomorphism) of torsors under `F′` (SGA 4 VII 2), and of étale coverings `Z` of degree `n` of a scheme as associated to Galois principal coverings with group the symmetric group `S_n`, where to `Z` is associated the covering `Isom_X(Z₀, Z)`, where `Z₀` is the trivial covering of `X` of degree `n`.

**Corollary 1.5.**
<!-- label: XIV.1.5 -->

Under the conditions of 1.1 3°), suppose that `prof_Y(F) ⩾ n`; then one has

```text
H^n_Y(X, F) ≃ H⁰(X, ℋ^n_Y(F)).
```

The corollary follows from the spectral sequence

```text
E_2^{pq} = H^p(X, ℋ^q_Y(F)) ⟹ H^{p+q}_Y(X, F).
```

Indeed, one has by hypothesis `E_2^{pq} = 0` for `q < n`, whence

```text
H^n_Y(X, F) = E_2^{0,n} = H⁰(X, ℋ^n_Y(F)).
```

**Remarks 1.6.**
<!-- label: XIV.1.6 -->

<!-- original page 212 -->

a) The notion of `Y`-depth, in the form of the equivalent conditions (i) and (ii) of 1.1, makes sense for any site. In the particular case where `X` is a locally noetherian scheme equipped with the Zariski topology, and `F` a sheaf of coherent `O_X`-modules, one finds the usual notion of `Y`-depth as the infimum of the depths at the points of `Y` (III).

b) For `n ⩽ 2`, the notion of `Y`-étale depth of `X` is independent of `L`. For `n = 1`, it simply means that `U` is dense in `X`. Indeed this condition is necessary in order that `prof_Y(F) ⩾ 1`, and it is also sufficient since one may suppose `X` reduced, the case in which the condition `U` dense in `X` is preserved by étale base change (EGA IV 11.10.5 (ii) b)). If `U` is retrocompact in `X`, the relation `prof_Y(X) ⩾ 1` is also equivalent to saying that `Y` contains no maximal point of `X` (EGA I 6.6.5). For `n = 2` and `U` retrocompact in `X`, the condition `prof_Y(X) ⩾ 2` is equivalent to the fact that, for every geometric point `y` of `Y`, `Ū` is connected non-empty, that is, "`Y` does not disconnect `X` locally for the étale topology".

c) If `X` is of `Y`-depth `⩾ n` for `L` and `U` retrocompact in `X`, then for every locally constant abelian sheaf of `L`-torsion `F` on `X`, one has `prof_Y(F) ⩾ n`. Indeed, since the property `prof_Y(F) ⩾ n` is local for the étale topology, one may suppose `F` constant; then `F` is a filtered direct limit of sheaves that are finite sums of sheaves of the form `ℤ/p^m ℤ`, where `m` is a positive integer and `p ∈ L`. Using 1.1 (iii)

<!-- original page 213 -->

and (SGA 4 VII 3.3), one sees that one may reduce to the case `F = ℤ/p^m ℤ`, then, by induction on `m`, to the case `F = ℤ/pℤ` for which the assertion follows from the definition.

d) By 1.4, if `prof_Y(X) ⩾ 3`, the pair `(X, Y)` is pure in the sense of X 3.1. In fact the pure pairs that one encounters in practice (cf. X 3.4) satisfy the stronger condition of homotopical depth `⩾ 3`, and this notion may therefore advantageously be substituted for that of pure pair.

e) Let `F` be a complex of abelian sheaves and `T(F)` the complex obtained by applying to `F` the translation functor ([3]); then one evidently has:

```text
prof_Y(T(F)) = prof_Y(F) − 1.
```

f) Let us note that the recent works of Artin-Mazur ([1]) allow one to define the notion of homotopical depth `⩾ n` for every integer `n` (not only for `n ⩾ 3`).

g) Under the conditions of 1.1 3°), in order that `prof_Y(F) = ∞`, it is necessary and sufficient that `F ⥲ Ri_*(i^* F)` in `D⁺(X)`. Indeed, the `ℋ^p_Y(F)` are the cohomology sheaves of the cone (= mapping cylinder) of the canonical morphism `F → Ri_* i^*(F)`.

**Definition 1.7.**
<!-- label: XIV.1.7 -->

Let `X` be a scheme, `x` a point of `X`, `x̄` a geometric point above `x`, and `X̄` the strict localization of `X` at `x̄`. As before, `F` denotes either a sheaf of sets on `X`, a sheaf of groups on `X`, or a complex of abelian sheaves on `X` bounded below; `F̄` its inverse image on `X̄`, and `L` a set of prime numbers. One says that `F` is of étale depth `⩾ n` at the point `x` (resp. that the étale depth for `L` of `X` at `x` is

<!-- original page 214 -->

`⩾ n`, resp. that the homotopical depth for `L` of `X` at `x` is `⩾ 3`) and one writes `prof_x(F) ⩾ n` (resp. `prof_x^L(X) ⩾ n`, resp. `prof_x^{hopL}(X) ⩾ 3`) if one has `prof_{x̄}(F̄) ⩾ n` (resp. `prof_{x̄}^L(X̄) ⩾ n`, resp. `prof_{x̄}^{hopL}(X̄) ⩾ 3`). One defines in the obvious way the integer `prof_x^L(X)` and, if `F` is a complex of abelian sheaves, the integer `prof_x(F)`. If `L` is the set of all prime numbers, one omits `L` in the notation `prof_x^L(X)`, unless there is a risk of confusion with the notation of (EGA IV 5.7.1), in which case one writes `prof_x^ét(X)`.

One then has the following pointwise characterization of depth:

**Theorem 1.8.**
<!-- label: XIV.1.8 -->

Let `X` be a scheme, `Y` a closed part of `X` such that the open set `U = X − Y` is retrocompact in `X`. If `F` is either a sheaf of sets on `X`, a sheaf of groups on `X`, or a complex of abelian sheaves on `X` bounded below, then one has

```text
prof_Y(F) = inf_{y ∈ Y} prof_y(F).
```

**1.8.1.** Let us first show that, for every point `y` of `Y`, one has the inequality `prof_y(F) ⩾ prof_Y(F)`. Indeed, let `ȳ` be a geometric point above `y`, `X̄` the strict localization of `X` at `ȳ`, `F̄` and `Ȳ` the inverse images of `F` and `Y` on `X̄`. By 1.7 and 1.3,

```text
prof_y(F) = prof_{ȳ}(F̄) ⩾ prof_{Ȳ}(F̄) ⩾ prof_Y(F),
```

the last inequality using the hypothesis "`U` retrocompact", via the conditions (iii) in 1.1 and the transitivity in the formation of strict localizations.

<!-- original page 215 -->

**1.8.2.** Conversely, suppose that, for every point `y` of `Y`, one has `prof_y(F) ⩾ n` (`n` an integer) and let us show that one then has `prof_Y(F) ⩾ n`.

Let us first recall the following well-known results (SGA 4 VIII):

**Lemma 1.8.2.1.**
<!-- label: XIV.1.8.2.1 -->

Let `X` be a scheme, `F` a sheaf of sets on `X` (resp. `G → F` a monomorphism of sheaves of sets on `X`). Then, in order that two sections `s` and `s′` of `F` coincide (resp. that a section `s` of `F` come from a section of `G`), it is necessary and sufficient that this hold locally. In particular, if `s` and `s′` are two sections of `F`, there exists a largest open set `V` of `X` on which they coincide (resp. if `s` is a section of `F` over `X`, there exists a largest open set `V` of `X` such that `s|V` comes from a section of `G` over `V`). This open set is also the set of points `x` of `X` such that, denoting by `x̄` a geometric point above `x`, the sections `s` and `s′` have the same image in the fiber `F_{x̄}` (resp. that the image of `s` in `F_{x̄}` comes from an element of `G_{x̄}`).

Let us return to the proof of 1.8.

1°) Case where `F` is a sheaf of sets. If `n = 1`, it suffices to show that the canonical morphism

```text
H⁰(X, F) → H⁰(U, F)
```

is injective, the result still applying when one replaces `X` by a scheme étale over `X`. Let `s` and `s′` be two sections of `F` over `X` having the same image in `H⁰(U, F)` and let `V` be the largest open set over which they are equal; one evidently has `V ⊃ U`. Suppose `V ≠ X` and let `y` be a maximal point of `X − V`, `ȳ` a

<!-- original page 216 -->

geometric point above `y`, `X̄` the strict localization of `X` at `ȳ`, and `V̄` and `F̄` the inverse images of `V` and `F` on `X̄`. By the choice of `y`, one has `X̄ − ȳ = V̄`, and by hypothesis the morphism

```text
H⁰(X̄, F̄) → H⁰(X̄ − ȳ, F̄) = H⁰(V̄, F̄)
```

is injective. It follows that `s` and `s′` coincide at the point `y`, which is absurd. If `n = 2`, it suffices to show, taking the preceding into account, that the morphism

```text
H⁰(X, F) → H⁰(U, F) = H⁰(X, i_* i^* F)
```

is surjective (where `i` is the canonical immersion of `U` in `X`). Let `s` be a section of `i_* i^* F` over `X` and `V` the largest open set over which it comes from a section of `F`. Suppose `V ≠ X` and let `y` be a maximal point of `X − V`; with the preceding notations, it follows from the hypothesis that the canonical morphism

```text
H⁰(X̄, F̄) → H⁰(X̄ − ȳ, F̄) = H⁰(V̄, F̄)
```

is bijective; consequently `s|V` extends to the point `y`, which is absurd and completes the proof in case 1°).

2°) Case where `F` is a sheaf of groups. Taking 1°) into account, the only thing that remains to show is that, in the case `n = 3`, the morphism

```text
H¹(X, F) = H¹(X, i_* i^* F) → H¹(U, F)
```

<!-- original page 217 -->

is bijective. One already knows that it is injective by 1°) and 1.1 2°) (ii bis). For surjectivity, one uses the exact sequence (SGA 4 XII 3.2)

```text
0 → H¹(X, i_* i^* F) → H¹(U, F) --d--> H⁰(X, R¹ i_* (i^* F)).
```

Let `s ∈ H¹(U, F)` and `V ⊃ U` the largest open set over which `d(s) = 0`; it is also the largest open set such that `s` comes from an element of `H¹(V, F)`. Suppose `V ≠ X` and let `y` be a maximal point of `X − V`; if `X̄` is the strict localization of `X` at a geometric point `ȳ` above `y`, one has, with obvious notations, the exact sequence

```text
0 → H¹(X̄, i_* (i^* F̄)) → H¹(Ū, F̄) --d--> H⁰(X̄, R¹ i_* (i^* F̄)).
```

Since `i : U → X` is quasi-compact, `R¹ i_* (i^* F̄)` is the inverse image of `R¹ i_* (i^* F)` by the morphism `X̄ → X`, whence `H⁰(X̄, R¹ i_* (i^* F̄)) = (R¹ i_* (i^* F))_ȳ`. By hypothesis and given that `y ∈ Y`, the morphism

```text
H¹(X̄, F̄) → H¹(V̄, F̄)
```

is bijective. The image `s̄` of `s` in `H¹(Ū, F̄)`, which extends to `V̄` by definition of `V`, therefore also extends to `X̄`; it follows that `d(s̄) = 0`, hence the image of `d(s)` in the geometric fiber `(R¹ i_* (i^* F))_ȳ` is null; but this contradicts the definition of `V`, whence case 2°).

3°) Case where `F` is a complex of abelian sheaves bounded below. One reasons by induction on `n`. The conclusion is satisfied for `n` sufficiently small, since `F` is bounded below. So suppose that `prof_Y(F) ⩾ n − 1` and let us show that `prof_Y(F) ⩾ n`, knowing that, for every point `y` of `Y`, one has `prof_y(F) ⩾ n`. It suffices to see that the canonical morphism

```text
(∗)    H^{n−2}(X, F) → H^{n−2}(U, F)
```

is surjective and that

```text
(∗∗)   H^{n−1}(X, F) → H^{n−1}(U, F)
```

is injective (the result applying when one replaces `X` by a scheme étale over `X`).

<!-- original page 218 -->

a) Surjectivity of (∗). The proof is analogous to that of 2°). Taking 1.5 and (SGA 4 V 4.5) into account, one has the exact sequence

```text
H^{n−2}(X, F) → H^{n−2}(U, F) --d--> H^{n−1}_Y(X, F) = H⁰(X, ℋ^{n−1}_Y(F)).
```

Let `s ∈ H^{n−2}(U, F)` and `V ⊃ U` the largest open set over which `d(s) = 0`, which is also the largest open set such that `s` extends to `H^{n−2}(V, F)`. Suppose `V ≠ X` and let `y` be a maximal point of `X − V` and `X̄` the strict localization of `X` at a geometric point `ȳ` above `y`. Since `i : U → X` is quasi-compact, the formation of `ℋ^{n−1}_Y(F)` commutes with the base change `X̄ → X` and one therefore has (with obvious notations) the exact sequence

```text
H^{n−2}(X̄, F̄) → H^{n−2}(Ū, F̄) --d--> H^{n−1}_Ȳ(X̄, F̄) = (ℋ^{n−1}_Y(F))_ȳ,
```

the last equality resulting from the retrocompactness hypothesis on `U`.

Now one has by hypothesis the isomorphism

```text
H^{n−2}(X̄, F̄) ⥲ H^{n−2}(X̄ − ȳ, F̄) = H^{n−2}(V̄, F̄);
```

consequently the image `s̄` of `s` in `H^{n−2}(Ū, F̄)`, which extends (by definition of `V`) to `H^{n−2}(V̄, F̄)`, also extends to `H^{n−2}(X̄, F̄)`; but this shows that `d(s̄) = 0`, that is, that `d(s)` is null at `y`, which is absurd.

b) Injectivity of (∗∗). Using the surjectivity of (∗), one obtains the exact sequence

```text
0 → H⁰(X, ℋ^{n−1}_Y(F)) → H^{n−1}(X, F) → H^{n−1}(U, F)
```

<!-- original page 219 -->

and one must show that every element `s ∈ H⁰(X, ℋ^{n−1}_Y(F))` is null. Let `V` be the largest open set over which `s = 0`. Suppose `V ≠ X` and let `y` be a maximal point of `X − V`, `X̄` a strict localization of `X` at a geometric point `ȳ` above `y`. By the inductive hypothesis and by 1.8.1, one has the relation `prof_Ȳ(F̄) ⩾ prof_Y(F) ⩾ n − 1`, whence the fact that the map `e` in the diagram below is injective:

```text
H⁰(X̄, ℋ^{n−1}_Ȳ(F̄)) = (ℋ^{n−1}_Y(F))_ȳ --e--> H^{n−1}(X̄, F̄) --f--> H^{n−1}(V̄, F̄).
```

The same holds for `f` by virtue of the hypothesis; the left equality follows from the retrocompactness hypothesis on `U`. Let `s̄` be the image of `s` in `(ℋ^{n−1}_Y(F))_ȳ`; since `s` vanishes over `V`, one has `f · e(s̄) = 0`, whence `s̄ = 0`, which contradicts the choice of `y` and completes the proof.

**Remark 1.9.**
<!-- label: XIV.1.9 -->

A result analogous to 1.8 is doubtless valid in the case where one replaces the étale topos of a scheme `X` by a "topos locally of finite type", that is, definable by a site locally of finite type (SGA 4 VI 1.1). To see this, one must use a result of P. Deligne (SGA 4 VI.9), asserting that there are "sufficiently many fiber functors" in such a topos.

We are going to deduce from 1.8 important cases where one can determine the étale depth.

**Theorem 1.10** (Cohomological semi-purity theorem)[^N.D.E-XIV-1].
<!-- label: XIV.1.10 -->

Denote by `X` either a smooth scheme over a field `k`, or a regular excellent scheme (EGA IV 7.8.2) of characteristic zero (N.B. if one admits resolution of singularities in the sense of (SGA 4 XIX), it suffices to suppose, more generally, that `X` is a regular excellent scheme of equal characteristic). Let `Y` be a closed part of `X` and `L` the set

<!-- original page 220 -->

of prime numbers distinct from the characteristic of `X`. Then one has

```text
prof_Y^L(X) = 2 codim(Y, X).
```

*Proof.* It follows from 1.8 that one has

```text
prof_Y^L(X) = inf_{y ∈ Y} prof_y^L(X).
```

Since on the other hand `codim(Y, X) = inf_{y ∈ Y} dim O_{X,y}`, one is reduced to showing that

```text
prof_y^L(X) = 2 dim O_{X,y},
```

which follows from (SGA 4 XVI 3.7 and XIX 3.2).

**Theorem 1.11** (Homotopical purity theorem)[^N.D.E-XIV-2].
<!-- label: XIV.1.11 -->

If `X` is a locally noetherian scheme that is regular (resp. whose local rings are complete intersections), `Y` a closed part of `X` such that `codim(Y, X) ⩾ 2` (resp. `codim(Y, X) ⩾ 3`), then one has

```text
prof_Y^{hop}(X) ⩾ 3.
```

It indeed follows from 1.8 that one has `prof_Y^{hop}(X) = inf_{y ∈ Y} prof_y^{hop}(X)`. Now the strictly local rings of `X` at the various points of `Y` are regular rings of dimension `⩾ 2` (resp. complete intersections of dimension `⩾ 3`). It then follows from the purity theorem X 3.4 that `prof_y^{hop}(X) ⩾ 3`, which proves the theorem.

**Example 1.12.**
<!-- label: XIV.1.12 -->

Let `X` be a locally noetherian scheme, `Y` a closed part of `X`, and `n = 1` or `2`. Then, if `prof_Y(O_X) ⩾ n` (`prof_Y(O_X)` denoting the `Y`-depth in the sense of coherent sheaves, cf. 1.6 a)), one also has `prof_Y(X) ⩾ n`; this is evident for `n = 1` and, for `n = 2`, it is none other than Hartshorne's theorem

<!-- original page 221 -->

(III 1). On the other hand, the analogous assertion is false for `n ⩾ 3`. Take for example an

<!-- original page 222 -->

affine space of dimension `⩾ 3` over a field of characteristic `≠ 2` and let `ℤ/2ℤ` act by symmetry with respect to the origin. Let `X` be the quotient and `Y = {x}` the image of the origin in `X`. Then `O_{X,x}` is a Cohen-Macaulay ring, hence one has `prof_x(O_X) ⩾ 3`; but the affine space minus the origin is an étale covering of `X − {x}` that does not extend to an étale covering of `X`; hence one has by 1.4 `prof_Y(X) = 2`.

The following theorem is the analogue of (EGA IV 6.3.1):

**Theorem 1.13.**
<!-- label: XIV.1.13 -->

Let `f : X → S` be a morphism of schemes, `Y` a closed part of `X`, `Z` a closed part of `S` such that `f(Y) ⊂ Z`. Suppose that the local rings of `X` at the various points of `Y` are noetherian and that the open sets `X − Y` and `S − Z` are retrocompact in `X` and `S` respectively. Let `p, q, r` be integers such that `p ⩾ −r`, `q ⩾ 0`, `L` a set of prime numbers and `F` a complex of abelian sheaves of `L`-torsion on `S` such that the cohomology sheaves `H^i(F)` are null for `i < −r`. Suppose that

a) The morphism `f` is locally `(p + q + r − 2)`-acyclic for `L` (SGA 4 XV 1.11).

b) One has

```text
prof_Z(F) ⩾ p.
```

c) For every point `s` of `Z`, one has

```text
prof_{Y_s}^L(X_s) ⩾ q.
```

Then one has

```text
prof_Y(f^* F) ⩾ p + q.
```

We shall need the following lemma:

**Lemma 1.13.1.**
<!-- label: XIV.1.13.1 -->

Let `L` be a set of prime numbers, `n` and `r` integers, `f : X → S` a morphism locally `n`-acyclic for `L`. Let `F` be a complex of abelian sheaves with cohomology sheaves of `L`-torsion such that `H^i(F) = 0` for `i < −r`, `Z` a closed part of `S` such that `S − Z` is retrocompact in `S`, and `T = f^{−1}(Z)`. Then the canonical morphism

```text
f^* (ℋ^i_Z(F)) → ℋ^i_T(f^* F)
```

is bijective for `i < n − r + 2` and injective for `i = n − r + 2`.

Set `U = S − Z` and `V = X − T`, so that one has the cartesian square

```text
V --g--> U
|        |
k        j
|        |
v        v
X --f--> S
```

Consider the commutative diagram below whose rows are exact

```text
→ f^*(ℋ^i_Z(F))    → f^*(H^i(F))    → f^*(H^i(R j_*(j^* F)))    →
                       ≀
→ ℋ^i_T(f^* F)     → H^i(f^* F)     → H^i(R k_*(k^* f^* F))     → ;
```

it follows that one is reduced to showing that the morphism

```text
f^*(H^i(R j_*(j^* F))) → H^i(R k_*(k^* f^* F))
```

<!-- original page 223 -->

is bijective for `i < n − r + 1` and injective for `i = n − r + 1`. Now such a morphism comes from the following morphism between hypercohomology spectral sequences

```text
f^* E_2^{p,q} = f^* (R^p j_*(H^q(j^* F)))     ⟹ f^*(H^*(R j_*(j^* F)))
       ↓                                         ↓
E′_2^{p,q} = R^p k_*(H^q(k^* f^* F))           ⟹ H^*(R k_*(k^* f^* F)).
```

Since `j` is quasi-compact, it follows from (SGA 4 XV 1.10) that the morphism `f^*(E_2^{p,q}) → E′_2^{p,q}` is bijective for `p ⩽ n` and injective for `p = n + 1`; in particular it is bijective for `p + q ⩽ n − r` and injective for `p + q = n − r + 1`. The conclusion follows immediately.

Let us return to the proof of 1.13. Let `T = f^{−1}(Z)`. By 1.13.1 and condition a), the canonical morphism `f^*(ℋ^i_Z(F)) → ℋ^i_T(f^* F)` is an isomorphism for `i ⩽ p + q`. It therefore follows from b) that `ℋ^i_T(f^* F) = 0` for `i < p` and, for `i < p + q`, `ℋ^i_T(f^* F)` restricted to `T` is the inverse image of a sheaf `G_i` on `Z`. Let

```text
f_T : T → Z
```

be the restriction of `f` to `T`. It then follows from c) and from the corollary that follows that `ℋ^j_Y(f_T^*(G_i)) = 0` for `j < q`. One concludes that

```text
ℋ^j_Y(ℋ^i_T(f^* F)) = 0 for i + j < p + q,
```

since the inequality `i + j < p + q` entails either `i < p` and then `ℋ^i_T(f^* F) = 0`, or `j < q` and then `ℋ^j_Y(ℋ^i_T(f^* F)) = 0`. Given that one has, with the notations of 1.0, `Γ_Y = Γ_Y · Γ_T`, one has the spectral sequence

```text
(1.13.2)    E_2^{i,j} = ℋ^j_Y(ℋ^i_T(f^* F)) ⟹ ℋ^{i+j}_Y(f^* F);
```

<!-- label: eq:XIV.1.13.2 -->

since `E_2^{i,j} = 0` for `i + j < p + q`, one sees that `ℋ^k_Y(f^* F) = 0` for `k < p + q`.

<!-- original page 224 -->

The theorem will therefore be proved if one proves the following corollary (which is the particular case of 1.13 obtained by taking `Z = S`, `r = p = 0` and `F` reduced to degree `0`).

**Corollary 1.14.**
<!-- label: XIV.1.14 -->

Let `f : X → S` be a morphism, `Y` a closed part such that the complementary open set `X − Y` is retrocompact in `X` and that the local rings of `X` at the various points of `Y` are noetherian. Let `L` be a set of prime numbers, `q` an integer, and `F` an abelian sheaf of `L`-torsion on `S`. Suppose


that `f` is locally `(q − 2)`-acyclic for `L` and that, for every point `s` of `S`, one has `prof_{Y_s}^L(X_s) ⩾ q`. Then one has `prof_Y(f^* F) ⩾ q`.

1°) Reduction to the case where `X` and `S` are strictly local schemes, `f` a local morphism, and `Y` reduced to a closed point of `X`.

By 1.8, to establish 1.14, one must show that one has for every point `y` of `Y`:

```text
prof_y(f^* F) ⩾ q.
```

Let `s = f(y)`, `s̄` a geometric point above `s`, `ȳ` a geometric point above `y` and over `s̄`, `X̄` and `S̄` the strict localizations of `X` and `S` at `ȳ` and `s̄` respectively, `f̄ : X̄ → S̄` the canonical morphism, and `F̄` the inverse image of `F` on `S̄`. Since one has the relation `prof_y(f^* F) = prof_{ȳ}(f̄^* F̄)`, it suffices to show that the hypotheses of 1.14 are preserved when one replaces `f` (resp. `Y`, resp. `F`) by `f̄` (resp. `{ȳ}`, resp. `F̄`). The retrocompactness condition

<!-- original page 225 -->

follows from the noetherian hypothesis on `O_{X,x}`, which implies that `X̄` is noetherian. By (SGA 4 XV 1.10 (i)), `f̄` is still locally `(q − 2)`-acyclic for `L`. Moreover the fiber `(X̄)_{s̄}` of `X̄` over `s̄` is identified with the strict localization of `X_s` at `ȳ`, hence satisfies the relation `prof_{ȳ}((X̄)_{s̄}) ⩾ q`. Since an analogous relation is trivially verified for the fibers of the `S̄`-scheme `X̄` other than the closed fiber, this completes the reduction.

2°) Case where `X` and `S` are strictly local, `f` a local homomorphism, and `Y` reduced to the closed point of `X`. Let

```text
g : U = X − {y} → S
```

be the structural morphism of `U`. One must show that the canonical morphism

```text
u_i : H^i(X, f^* F) → H^i(U, f^* F)
```

is bijective for `i ⩽ q − 2` and injective for `i = q − 1`. Consider the commutative diagram

```text
H^i(X, f^* F) --u_i--> H^i(U, f^* F)
       ↖ v_i           ↗ w_i
          H^i(S, F)
```

The morphism `v_i` is evidently bijective for every `i`. On the other hand `g` is locally `(q − 2)`-acyclic for `L`; moreover its fibers are `(q − 2)`-acyclic for `L`, as follows from the fact that `prof_y(X_s) ⩾ q` and that the fibers of `f` are `(q − 2)`-acyclic for `L`; since `g` is quasi-compact (as `X` is noetherian), it follows from (SGA 4 XV 1.16) that `g` is `(q − 2)`-acyclic for `L`. Consequently `w_i`, hence also `u_i`, is bijective

<!-- original page 226 -->

for `i ⩽ q − 2` and injective for `i = q − 1`, which completes the proof of 1.14.

**Corollary 1.15.**
<!-- label: XIV.1.15 -->

Let `f : X → S` be a morphism of schemes, `L` a set of prime numbers, `m` and `r` integers, and `F` a complex of abelian sheaves of `L`-torsion on `S` such that `H^i(F) = 0` for `i < −r`. Let `x` be a point of `X`, `s = f(x)`

<!-- original page 227 -->

and suppose that the local ring `O_{X,x}` is noetherian. Then, if `f` is locally `m`-acyclic for `L`, one has the relation

```text
(∗)    prof_x(f^* F) ⩾ inf(prof_s(F) + prof_x^L(X_s), n)   where n = m − r + 2.
```

In particular, if `n ⩾ prof_s(F) + prof_x^L(X_s)`, for example if `f` is locally acyclic for `L`, one has

```text
(∗∗)   prof_x(f^* F) ⩾ prof_s(F) + prof_x^L(X_s).
```

If `L` is reduced to one element `ℓ` and if one has `n ⩾ prof_s(F) + prof_x^L(X_s)`, the preceding inequality is an equality.

One reduces to the case where `s` and `x` are closed points by taking the strict localizations of `S` and `x` at geometric points `s̄` above `s` and `x̄` above `x` and `s̄`. If one has the inequality `n ⩾ prof_s(F) + prof_x^L(X_s)`, then (∗) is obtained from 1.13 by taking `p = prof_s(F)` and `q = prof_x^L(X_s)` (the hypothesis that `S − {s}` is retrocompact in `S` follows from the fact that `X − X_s` is retrocompact in `X` and that `f` is surjective since it is `(−1)`-acyclic (except perhaps if the conclusion of 1.15 is empty)). If `n < prof_s(F) + prof_x^L(X_s)`, the inequality (∗) is again obtained from 1.13 by taking for example `p = prof_s(F)` and `q = n − p`. It remains to prove the last assertion. Let `p = prof_s(F)` and `q = prof_x(X_s)`; it follows from (1.13.2) that one has

```text
H^{p+q}_x(f^*(F)) ≃ H^q_x(f^*(H^p_s(F))).
```

Since `prof_s(F) = p`, the sheaf `H^p_s(F)` is a sheaf of `ℓ`-torsion, constant on `s`, non-zero. Consequently the sheaf `G = f^*(H^p_s(F))` is a sheaf of `ℓ`-torsion, constant on `X_s`, non-zero, hence contains a subsheaf isomorphic to `ℤ/ℓℤ`; since `H^q_x(ℤ/ℓℤ)` is non-zero, one indeed has `H^q_x(G) ≠ 0`.

**Corollary 1.16.**
<!-- label: XIV.1.16 -->

Let `f : X → S` be a regular morphism of excellent schemes (EGA IV 7.8.2) of characteristic zero, `ℓ` a prime number, and `F` a complex of sheaves of `ℓ`-torsion on `S`. Let `x ∈ X`, `s = f(x)`; then one has

```text
prof_x(f^* F) = prof_s(F) + 2 dim(O_{X_s,x}).
```

Indeed `f` is locally acyclic (SGA 4 XIX 4.1). It then follows from 1.15 that one has

```text
prof_x(f^* F) = prof_s(F) + prof_x(X_s).
```

Now one has by 1.10

```text
prof_x(X_s) = 2 dim O_{X_s,x},
```

whence the result.

**Remark 1.17.**
<!-- label: XIV.1.17 -->

It follows from 1.15 that 1.13 remains valid when one replaces b) and c) by the conditions:

<!-- original page 228 -->

b′) For every point `s ∈ f(Y)`, one has `prof_s(F) ⩾ p`.

c′) For every point `x ∈ Y`, if `s = f(x)`, one has `prof_x^L(X_s) ⩾ q`.

In the case of a sheaf of sets or of groups, one has the following theorem analogous to 1.13.

**Theorem 1.18.**
<!-- label: XIV.1.18 -->

Let `f : X → S` be a morphism of schemes, `Y` a closed part of `X` such that `X − Y` is retrocompact in `X` and that, for every point `x` of `Y`, the local ring `O_{X,x}` is noetherian.

1°) Let `F` be a sheaf of sets on `S` and `n` an integer equal to `1` or `2`. Suppose that `f` is locally `(n − 2)`-acyclic and that, for every point `s` of `f(Y)`, one has:

```text
prof_{Y_s}(X_s) + prof_s(F) ⩾ n.
```

Then one has:

```text
prof_Y(f^* F) ⩾ n.
```

2°) Let `L` be a set of prime numbers and `F` a sheaf of ind-`L`-groups. Suppose that `f` is locally `1`-aspherical for `L` (SGA 4 XV 1.11) and that, for every point `s` of `f(Y)`, one has:

```text
prof_{Y_s}^{hopL}(X_s) + prof_s(F) ⩾ 3.
```

Then one has:

```text
prof_Y(f^* F) ⩾ 3.
```

<!-- original page 229 -->

*Proof.* One reduces, as in 1.14 and 1.15, to the case where `X` and `S` are strictly local schemes, `f` a local homomorphism, and `Y` the closed point `x` of `X`. Let `s = f(x)` be the closed point of `S`; one has the commutative diagram:

```text
X − X_s --i--> X − {x} --j--> X
        \         |          /
         \        g         /
          \       |        / f
           \      v       /
            \   S − {s}  /
             \    |k    /
              \   v    /
                  S
```

1°) a) Case `n = 1`.

If `prof_s(F) ⩾ 1`, then the morphism `F → k_* k^* F` is injective, hence the morphism `f^* F → f^*(k_* k^* F)` is also injective. On the other hand it follows from the fact that `f` is locally `(−1)`-acyclic that the morphism `f^*(k_* k^* F) → (j · i)_*(f^* F|_{X − X_s})` is injective. Finally, the composite morphism `f^* F → (j · i)_*(f^* F|_{X − X_s})` is injective, which shows that one has `prof_{X_s}(f^* F) ⩾ 1`, hence also `prof_x(f^* F) ⩾ 1`.

If `prof_x(X_s) ⩾ 1`, one considers the commutative diagram

```text
                          v
H⁰(X, f^* F)          ----→    H⁰(X − {x}, f^* F)
    | ≀                            ↑
    v                              |
H⁰(X_s, f^* F)        --v′--→ H⁰(X_s − {x}, f^* F);
(∗)
```

By hypothesis, `v′` is injective, hence the same holds for `v`.

<!-- original page 230 -->

b) Case `n = 2`. One considers the commutative diagram

```text
            u
H⁰(S, F)  ----→   H⁰(S − {s}, F)
   m ≀                  n ≀
   |                      |
   v                      v
            v                     w
H⁰(X, f^* F) --→ H⁰(X − {x}, f^* F) --→ H⁰(X − X_s, f^* F);
(∗∗)
```

one must show that `v` is bijective. The morphism `m` is evidently bijective, and, since `f` is `0`-acyclic, `n` is also bijective.

If `prof_s(F) ⩾ 2`, `u` is bijective. As one has seen in a), the single hypothesis `prof_s(F) ⩾ 1` entails the relation `prof_{X_s}(f^* F) ⩾ 1`; consequently `v` and `w` are injective; it then follows from (∗∗) that `v` is bijective.

If `prof_x(X_s) ⩾ 2`, then `g` is `0`-acyclic (since it is locally `0`-acyclic and its fibers are `0`-acyclic). It follows that `v · m` is bijective, hence `v` is bijective.

If `prof_s(F) ⩾ 1` and `prof_x(X_s) ⩾ 1`, then one already knows that `v` and `w` are injective. Let `z` be a maximal point of `X_s − {x}` (such a point exists by the hypothesis `prof_x(X_s) ⩾ 1`), `Z̄` the strict localization of `X` at a geometric point above `z`, and `f^* F̄` the inverse image of `f^* F` on `Z̄`. Consider the commutative diagram

```text
H⁰(S, F) ----→ H⁰(S − {s}, F)
   |m ≀                |n ≀
   v                    v
H⁰(X, f^* F) --v--→ H⁰(X − {x}, f^* F) --w--→ H⁰(X − X_s, f^* F)
   |m′ ≀                |r                       |
   v                    v                        v
H⁰(Z̄, f^* F̄) ----→  H⁰(Z̄ − {z̄}, f^* F̄)
```

The morphism `m′ · m` is evidently bijective, and it follows from the fact that `f` is locally `0`-acyclic that `n′ · n` is bijective; consequently `m′` and `n′` are also bijective. Since `w` is injective, `r` is also injective, and consequently `v` is bijective.

2°) Taking b) into account, one already knows that `prof_x(f^* F) ⩾ 2`.

If `prof_s(F) ⩾ 3`, then `R¹ k_*(k^* F) = 1`[^N.D.E-XIV-3]. Since `f` is locally `1`-aspherical,

<!-- original page 231 -->

one has `R¹(j · i)_*(f^* F|_{X − X_s}) = f^*(R¹ k_*(k^* F)) = 1`. One therefore has `prof_{X_s}(f^* F) ⩾ 3` and consequently `prof_x(f^* F) ⩾ 3`.

If `prof_x(X_s) ⩾ 3`, then `g` is `1`-aspherical (since `g` is locally `1`-aspherical and its fibers are `1`-aspherical). One therefore has `H¹(X − {x}, f^* F) = H¹(S, F) = 1` and consequently `prof_x(f^* F) ⩾ 3`.

If `prof_s(F) ⩾ 2` and `prof_x(X_s) ⩾ 1`, one uses the exact sequence (SGA 4 XII 3.2):

```text
1 → R¹ j_*(i_*(f^* F|_{X − X_s})) → R¹(j · i)_*(f^* F|_{X − X_s}) → j_*(R¹ i_*(f^* F|_{X − X_s})).
```

Since `f` and `g` are locally `1`-aspherical, one has

```text
R¹(j · i)_*(f^* F|_{X − X_s}) ≃ f^*(R¹ k_*(k^* F))
R¹ i_*(f^* F|_{X − X_s}) ≃ g^*(R¹ k_*(k^* F));
```

the preceding exact sequence then writes in the form

```text
(∗∗∗)  1 → R¹ j_*(i_*(f^* F|_{X − X_s})) → f^*(R¹ k_*(k^* F)) --a--> j_*(j^*(f^*(R¹ k_*(k^* F)))).
```

The hypothesis `prof_s(F) ⩾ 2` shows that the morphism `F → k_* k^* F` is bijective; applying `g^*`, one finds, taking into account the fact that `g` is locally `0`-acyclic, `f^* F|_{X − {x}} = i_*(f^* F|_{X − X_s})`. The hypothesis `prof_x(X_s) ⩾ 1` shows that the morphism `a` is injective (note that `f^*(R¹ k_*(k^* F))` is a sheaf equal to `1` outside `X_s` and constant on `X_s`). It then follows from (∗∗∗) that one has `R¹ j_*(f^* F|_{X − {x}}) = 1`, hence

<!-- original page 232 -->

`prof_x(f^* F) ⩾ 3`.

If `prof_s(F) ⩾ 1` and `prof_x(f^* F) ⩾ 2`, one considers the sheaf of homogeneous spaces `G` defined by the exact sequence

```text
1 → F → k_* k^* F → G → 1.
```

Applying to this exact sequence the exact functor `g^*` and using (SGA 4 XII 3.1), one obtains the following commutative diagram whose rows are exact:

```text
f^*(k_* k^* F)       →     f^* G                   → 1
        |                    |b
        v                    v u
j_*(g^*(k_* k^* F)) --u-->  j_*(g^* G)      → R¹ j_*(g^* F) → R¹ j_*(g^*(k_* k^* F)).
```

Since `prof_x(X_s) ⩾ 2`, the morphism `b` is bijective hence `u` is surjective, and one thus has a map with kernel reduced to the neutral element:

```text
1 → R¹ j_*(g^* F) → R¹ j_*(g^*(k_* k^* F)) = R.
```

Since `g^*(k_* k^* F) ≃ i_*(f^* F|_{X − X_s})` (because `g` is locally `0`-acyclic), `R` is identified with the first term of the exact sequence (∗∗∗); now one saw in the preceding case that `R = 1` as soon as one has `prof_x(X_s) ⩾ 1`, which shows that `prof_x(f^* F) ⩾ 3` and completes the proof of 1.18.

The following corollaries are generalizations of (SGA 4 XVI 3.2 and 3.3).

**Corollary 1.19.**
<!-- label: XIV.1.19 -->

Let `f : X → S` be a flat morphism with separable fibers of locally noetherian schemes,

<!-- original page 233 -->

and `Y` a closed part of `X`. Suppose that for every point `s ∈ f(Y)`, the fiber `Y_s` is rare[^N.D.E-XIV-4] in `X_s` and that one of the two following conditions is verified:

a) the closure of `f(Y)` is rare in `S`.

b) `X_s` is geometrically unibranch at the points of `Y_s`.

Then one has

```text
prof_Y(X) ⩾ 2.
```

It indeed follows from the hypothesis on `f` that `f` is locally `0`-acyclic (SGA 4 XV 4.1). One then applies 1.13. The hypothesis `Y_s` rare in `X_s` (resp. `f(Y)` rare in `S`) is by 1.6 b) equivalent to the relation `prof_{Y_s}(X_s) ⩾ 1` (resp. `prof_{f(Y)}(S) ⩾ 1`). The hypothesis `X_s` geometrically unibranch at each point of `Y_s` is equivalent to saying that the strict localization of `X_s` at a geometric point of `Y_s` is irreducible; knowing that `Y_s` is rare in `X_s`, this evidently entails `prof_{Y_s}(X_s) ⩾ 2`, by 1.8. In either case 1.13 indeed gives `prof_Y(X) ⩾ 2`.

**Corollary 1.20.**
<!-- label: XIV.1.20 -->

Let `f : X → S` be a regular morphism (EGA IV 6.8.1) of locally noetherian schemes, `Y` a closed part of `X`. Suppose that, for every point `s ∈ f(Y)`, one of the following conditions is realized:

a) One has `codim(Y_s, X_s) ⩾ 2`.

b) One has `codim(Y_s, X_s) ⩾ 1` and `prof_s(S) ⩾ 1`.

c) One has `prof_s^{hop}(S) ⩾ 3`.

Then one has

<!-- original page 234 -->

```text
prof_Y^{hop}(X) ⩾ 3.
```

This indeed follows from 1.18, given that hypothesis a) implies `prof_{Y_s}^{hop}(X_s) ⩾ 3` (cf. 1.11), and that the condition `codim(Y_s, X_s) ⩾ 1` evidently implies `prof_Y(X) ⩾ 2`.

## 2. Technical lemmas

**2.1.** Let `S` be a locally noetherian scheme, `f : X → S` a morphism locally of finite type, `t` a point of `S`. If `x ∈ X` is such that `s = f(x) ∈ Spec O_{S,t}`, one sets

```text
δ_t(x) = deg.tr. k(x)/k(s) + dim({s}),
```

where `{s}` denotes the closure of `s` in `Spec O_{S,t}`, `k(x)` and `k(s)` the residue fields of `x` and `s` respectively. If `S` is a local ring with closed point `t`, one writes also `δ(x)` instead of `δ_t(x)` (cf. SGA 4 XIV 2.2).

**Lemma 2.1.1.**
<!-- label: XIV.2.1.1 -->

Let

```text
X′ --h--> X
|         |
f′        f
|         |
v         v
S′ --g--> S
```

be a cartesian square, where `S` and `S′` are noetherian local rings with closed points `t` and `t′` respectively, `g` a faithfully flat morphism such that `g^{−1}(t) = t′`, `f` a morphism locally

<!-- original page 235 -->

of finite type. Let `x′ ∈ X′`, `x = h(x′)`, `s = f(x)`, `s′ = f′(x′)`; then one has

```text
δ(x′) ⩽ δ(x).
```

Moreover the preceding inequality is an equality if and only if one has:

```text
deg.tr. k(x)/k(s) = deg.tr. k(x′)/k(s′)   and   dim({s}) = dim({s′}).
```

In particular, given `x ∈ X`, one can find `x′` such that `δ(x) = δ(x′)`.

One has indeed (EGA IV 6.11)

```text
dim({s}) = dim g^{−1}({s}).
```

It follows that, for every point `s′` of `g^{−1}(s)`, one has the relation `dim({s′}) ⩽ dim({s})`, and that, `s` being given, one can find `s′ ∈ g^{−1}(s)` such that one has the equality. Denote then by `Z` the schematic closure of `x` in the fiber `X_s` of `X` at `s`, and let `Z′ = Z ×_{Spec k(s)} Spec k(s′)`. Then `Z′` is equidimensional of dimension `deg.tr. k(x)/k(s)`; one therefore has, for every point `x′ ∈ Z′_x`,

```text
deg.tr. k(x′)/k(s′) ⩽ deg.tr. k(x)/k(s),  with equality
```

when `x′` is a maximal point of `Z′_x`. Whence immediately the announced conclusion.

**2.2.** Let `f : X → S` be a morphism locally of finite type and `T` a closed part of `S`. Let `x ∈ X`, `s = f(x)`; we shall set

```text
δ_T(x) = deg.tr. k(x)/k(s) + codim({s} ∩ T, {s}) = inf_{t ∈ T ∩ {s}} δ_t(x).
```

<!-- original page 236 -->

**Lemma 2.2.1.**
<!-- label: XIV.2.2.1 -->

Let

```text
X′ --h--> X
|         |
f′        f
|         |
v         v
S′ --g--> S
```

be a cartesian square, where the schemes `S` and `S′` are locally noetherian, catenary, the morphism `f` locally of finite type, and `g` faithfully flat. Let `T` be a closed part of `S`, `T′` a closed part of `S′` such that `g(T′) ⊂ T`, `x′` an element of `X′`, `x = h(x′)` and

```text
h_{x′} : Spec O_{X′,x′} → Spec O_{X,x}
```

the morphism induced by `h`. Then one has:

```text
δ_T(x) − δ_{T′}(x′) ⩽ dim h_{x′}^{−1}(x).
```

Let `s′ = f′(x′)`, `s = f(x)`. By definition:

```text
δ_T(x) − δ_{T′}(x′) = deg.tr. k(x)/k(s) − deg.tr. k(x′)/k(s′)
                     + codim({s} ∩ T, {s}) − codim({s′} ∩ T′, {s′}).
```

Since `g` is faithfully flat, it follows from (EGA IV 6.1.4) that one has

```text
(∗) codim({s} ∩ T, {s}) = codim(g^{−1}({s}) ∩ g^{−1}(T), g^{−1}({s}))
                       ⩽ codim(g^{−1}({s}) ∩ T′, g^{−1}({s}));
```

since `S′` is catenary, one has, by (EGA 0_IV 14.3.2 b)):

```text
codim({s′} ∩ T′, g^{−1}({s})) = codim({s′} ∩ T′, {s′}) + codim({s′}, g^{−1}({s}))
   = codim({s′} ∩ T′, g^{−1}({s}) ∩ T′) + codim(g^{−1}({s}) ∩ T′, g^{−1}({s})).
```

One deduces from this relation and (∗)

<!-- original page 237 -->

```text
δ_T(x) − δ_{T′}(x′) ⩽ deg.tr. k(x)/k(s) − deg.tr. k(x′)/k(s′) + codim({s′}, g^{−1}({s})).
```

Let us compute `codim({s′}, g^{−1}({s})) = dim O_{S′_s, s′}` (where `S′_s` is the fiber of `S′` at `s`). Let `Z` be the closed image of `x` in `X_s` and `Z′ ⊂ X′_s` the scheme defined by the cartesian square

```text
Z′ ----→ Z
|        |
v        v
S′_s --→ Spec k(s)
```

The morphism `Z → Spec k(s)` is flat, locally of finite type, and one has `dim Z = deg.tr. k(x)/k(s)`. It then follows from (EGA IV 6.1.2) that

```text
dim(O_{Z′,x′}) = dim(O_{S′_s, s′}) + deg.tr. k(x)/k(s) − deg.tr. k(x′)/k(s′);
```

taking into account the fact that `Z′_{s′} ≃ Z ⊗_{k(s)} k(s′)`, one obtains:

```text
δ_T(x) − δ_{T′}(x′) ⩽ dim(O_{Z′,x′}).
```

Now `Spec(O_{Z′,x′})` is identified with the fiber at `x` of the morphism

```text
(Spec(O_{X′,x′}))_s → (Spec(O_{X,x}))_s,
```

hence also with the fiber at `x` of `h_{x′}`, which proves the theorem.

**2.3.** The proofs of the theorems of §4 are based on duality theory; they use the following lemmas. Let `m` be an integer that is a power of a prime number `ℓ`; if `X` is a scheme, all the sheaves considered on `X` are sheaves of `ℤ/mℤ`-modules; one then has

<!-- original page 238 -->

the notion of dualizing complex on `X` (SGA 5 I 1.7). Suppose there exists such a complex `K` on `X`; then, for each geometric point `x̄` above a point `x` of `X`, one deduces from `K` (cf. SGA 5 I 4.5) a dualizing complex `K_{x̄}` on `Spec k(x̄)`, so that one has `K_{x̄} ≃ ℤ/mℤ[n]` (the bracket denoting the translation functor) for some integer `n` depending only on `x`. We shall set

```text
δ^K(x) = n.
```

If `K` is normalized at the point `x` (SGA 5 I 4.5), one therefore has `n = 0`.

**Lemma 2.3.1.**
<!-- label: XIV.2.3.1 -->

Let `X` be a locally noetherian scheme equipped with a dualizing complex `K`. If `x` and `x′` are two points of `X` such that `x` is a specialization of `x′` and that `codim({x}, {x′}) = 1`, then one has

```text
δ^K(x) = δ^K(x′) − 2.
```

One can first reduce to the case where `X` is a strictly local scheme. Indeed, let `X̄` be the strict localization of `X` at a geometric point `x̄` above `x`, `i : X̄ → X` the canonical morphism, and `x̄′` a geometric point of `X̄` above `x′`. Then `i^* K` is a dualizing complex on `X̄` and one has (SGA 5 I 4.5)

```text
(i^* K)_{x̄} ≃ K_{x̄} and (i^* K)_{x̄′} ≃ K_{x̄′},
```

<!-- original page 239 -->

which completes the reduction to the strictly local case.

If `j : {x′} → X` denotes the immersion of the reduced closed subscheme of `X` with underlying space `{x′}`, then `R^! j(K)` is a dualizing complex on `{x′}` and one sees immediately, using (SGA 5 I 4.5), that it suffices to prove the lemma for `{x′}`. One is thus reduced to the case where `X` is a strictly local integral scheme of dimension `1`.

Let then `X′` be the normalization of `X` and `f : X′ → X` the canonical morphism; `f` is an integral, surjective, radicial morphism, and it follows that `f^* K` is a dualizing complex on `X′` and that it suffices to prove the lemma for `X′` and for the points above `x` and `x′`. One is thus reduced to the case where `X` is a regular integral local scheme of dimension `1`, but one knows (cf. SGA 5 I 4.6.2 and 5.1) that then `μ_m[2]` and `ℤ/mℤ` are dualizing complexes, normalized respectively at the points `x` and `x′`; the lemma follows immediately.

**Lemma 2.3.2.**
<!-- label: XIV.2.3.2 -->

Let `S` be a noetherian local scheme, `f : X → S` a morphism of finite type. If `K` is a dualizing complex on `S`, normalized at the closed point `t` of `S`, and if `R^! f(K) = K′` is a dualizing complex on `X` (cf. SGA 5 I 3.4.3), one has, for every point `x` of `X`:

```text
δ^{K′}(x) = 2 δ(x).
```

Indeed let `s = f(x)` and `x′` a closed point of the fiber `X_s`; then one has `δ^{K′}(x′) = δ^K(s)` and by 2.3.1

```text
δ^K(s) = 2 codim({t}, {s}) = 2 dim({s}).
```

<!-- original page 240 -->

Since one can choose for `x′` a specialization of `x`, one has by 2.3.1

```text
δ^{K′}(x) = δ^{K′}(x′) + 2 codim({x}, {x′}) = δ^{K′}(x′) + 2 deg.tr. k(x)/k(s);
```

the lemma follows immediately.

The following lemma will be used only for the converse of the Lefschetz theorem in §4:

**Lemma 2.3.3.**
<!-- label: XIV.2.3.3 -->

Let

```text
X′ --h--> X
|         |
f′        f
|         |
v         v
S′ --g--> S
```

be a cartesian square, where `S` is a strictly local excellent scheme of characteristic zero, `S′` the completion of `S`, and `f` a morphism of finite type. Let `ℓ` be a prime number, `x ∈ X`, `Z` the

<!-- original page 241 -->

schematic closure of `X′_x` in `X′`, and `i : X′_x → Z`, `j : Z → X` the canonical morphisms. Then, if `k : X′ → R` is a closed immersion of `X′` into a regular excellent scheme `R` of characteristic zero, the complex

```text
K′ = i^*(R^!(k · j)(ℤ/ℓℤ))
```

is a dualizing complex on `X′_x` that is constant (that is, having only one non-null cohomology sheaf, isomorphic to `ℤ/ℓℤ`).

Taking (SGA 5 I 3.4.3) into account, the only thing to prove is that `K′` is constant. Now, since `Z` is excellent, the set of points of `Z` whose local rings are regular is an open set `U` (EGA IV 7.8.3 (iv)), and `U` evidently contains `X′_x` which is regular. Let then

```text
u : U → R
```

be the canonical immersion of `U` in `R`; it follows from the purity theorem (SGA 4 XIX 3.2 and 3.4) and from the isomorphism

```text
(μ_ℓ)_S ≃ (ℤ/ℓℤ)_S
```

(`S` strictly local) that one has

```text
R^! u(ℤ/ℓℤ) ≃ ℤ/ℓℤ[2c],
```

where `c` is a locally constant function on `U`, necessarily constant in a neighborhood of `X′_x`, since the fibers of `g` are geometrically integral by (EGA IV 18.9.1) hence `X′_x` integral. The lemma follows immediately.

## 3. Converse of the affine Lefschetz theorem

The present section will be used in §4 to prove a converse to the "Lefschetz theorem"; a reader interested only in the direct part of the said theorem may therefore omit the reading of the present section.

**3.1.** Let us recall the statement of the affine Lefschetz theorem[^N.D.E-XIV-5] (SGA 4 XIX 6.1 bis):

Let `S` be a strictly local excellent scheme of characteristic zero, `f : X → S` an affine morphism of finite type, and `F` a torsion sheaf on `X`. Then, if one sets

<!-- original page 242 -->

```text
δ(F) = sup{δ(x) | x ∈ X and F_x ≠ 0},
```

one has

```text
H^q(X, F) = 0 for q > δ(F).
```

Before stating the converse, let us prove a few lemmas.

**Lemma 3.2.**
<!-- label: XIV.3.2 -->

Let `K` be a field, `ℓ` a prime number distinct from the characteristic of `K`, and `F` an `ℓ`-torsion sheaf on `K`, constructible, non-null. Suppose that the `ℓ`-cohomological dimension of `K` (SGA 4 X 1) is equal to `n` (this is realized for example if `K` is the field of fractions of a strictly local excellent integral ring of characteristic zero of dimension `n` (SGA 4 XIX 6.3), or if `K` is a finitely generated extension of transcendence degree `n` of a separably closed field (SGA 4 X 2.1)). Then one can find a finite separable extension `L` of `K` such that:

```text
H^n(L, F|_L) ≠ 0.
```

One can find a finite extension `K′` of `K` such that the restrictions of `F` and `μ_ℓ` to `Spec K′` are constant sheaves. One then has `cd_ℓ(K′) = cd_ℓ(K) = n` (SGA 4 X 2.1), and it follows from ([2] II §3 Prop. 4 (iii)) that one can find a finite extension `L` of `K′` such that

<!-- original page 243 -->

```text
H^n(L, μ_ℓ) ≠ 0, i.e. H^n(L, ℤ/ℓℤ) ≠ 0.
```

Now the functor `H^n(L, ·)` is right exact on the category of `ℓ`-torsion sheaves, since `cd_ℓ(L) = n`; since `F` admits a quotient isomorphic to `ℤ/ℓℤ`, one also has `H^n(L, F|_L) ≠ 0`.

**Corollary 3.3.**
<!-- label: XIV.3.3 -->

Let `k` be a field, `K` a finitely generated extension of transcendence degree `n` of `k`, `F` a constructible non-null `ℓ`-torsion sheaf on `K`, with `ℓ` prime to the characteristic of `k`. Then one can find a finite separable extension `L` of `K` such that, if `u : Spec L → Spec k` denotes the canonical morphism, one has

```text
R^n u_*(F|_{Spec L}) ≠ 0.
```

When the field `k` is separably closed, the corollary is a particular case of 3.2. In the general case, one can find a finite separable extension `k_1` of `k` such that the irreducible components of `K ⊗_k k_1` are geometrically irreducible (EGA IV 4.5.11); let `K_1` be one of them. If `k′` is a separable closure of `k_1`, then `K′ = K_1 ⊗_{k_1} k′` is a field, and one has by (EGA IV 4.2)

```text
deg.tr. K′/k′ = deg.tr. K/k = n.
```

It then follows from 3.2 that one can find a finite separable extension `L′` of `K′` such that one has `H^n(L′, F|_{L′}) ≠ 0`. But `k′ = lim_i k_i` (direct limit), where `k_i` runs over the finite extensions of `k_1` contained in `k′`, and consequently `K′ = lim_i (k_i ⊗_{k_1} K_1)`. It follows that one

<!-- original page 244 -->

can find an index `i` and a finite separable extension `L` of `k_i ⊗_{k_1} K_1 = K_i` such that one has `L′ ≃ L ⊗_{K_i} K′`. The extension `L` of `K` answers the question; indeed it follows from the commutative diagram

```text
        Spec L
       /     \
      v       u
     /         \
    v           \
Spec k_i --w--> Spec k,
```

with `w` finite, hence `R^q w_* = 0` if `q > 0`, that one has

```text
R^n u_*(F|_{Spec L}) ≃ w_*(R^n v_*(F|_{Spec L})).
```

Now `R^n v_*(F|_{Spec L}) ≠ 0`, since `H^n(L′, F|_{L′}) ≠ 0`; one therefore also has `R^n u_*(F|_{Spec L}) ≠ 0`.

Let us recall the following well-known lemma (cf. EGA 0_III 10.3.1.2 and EGA IV 18.2.3):

**Lemma 3.4.**
<!-- label: XIV.3.4 -->

Let `X` be a scheme, `x` a point of `X`, `K` a finite separable extension of `k(x)`. Then there exists a scheme `X_1` étale over `X`, affine, and a point `x_1 ∈ X_1` above `x` such that `k(x_1)` is `k(x)`-isomorphic to `K`.

We shall use in §4 the following technical form of the converse of 3.1.

**Proposition 3.5.**
<!-- label: XIV.3.5 -->

<!-- original page 245 -->

Let

```text
X′ --h--> X
|         |
f′        f
|         |
v         v
S′ --g--> S,
```

be a cartesian square where the schemes `S` and `S′` are strictly local excellent of characteristic zero, the morphism `f` locally of finite type, `g` regular (EGA IV 6.8.1) surjective, with closed fiber of `g` reduced to the closed point of `S′`. Given an `S`-scheme `X_1` (resp. an `S`-morphism `f_1`, etc.), we shall denote by `X′_1` (resp. `f′_1`, etc.) the scheme `X_1 ×_S S′` (resp. the morphism `(f_1)_{(S′)}`, etc.). Let `F` be a constructible sheaf of `ℤ/mℤ`-modules on `X′` (`m` a power of a prime number `ℓ`) satisfying the following conditions:

(i) For every point `x ∈ X`, one can find a finite separable extension `K` of `k(x)` such that the restriction of `F` to the fiber `(X′)_{(Spec K)}` comes by inverse image from a constructible sheaf on `Spec K`.

(ii) For every morphism `f_1 : X_1 → S`, with `X_1` étale over `X`, affine, for every point `s ∈ S`, and for every integer `q > 0`, one can find a finite separable extension `K` of `k(s)` such that the restriction of `R^q f′_{1*}(F|_{X′_1})` to the fiber `S′_{(Spec K)}` comes by inverse image from a constructible sheaf on `Spec K`.

Let `n` be an integer, and suppose that for every scheme `X_1` étale over `X`, affine, one has

<!-- original page 246 -->

```text
H^i(X′_1, F) = 0 for i > n.
```

Then, if `x̄′` is a geometric point above the point `x′ ∈ X′` such that `F_{x̄′} ≠ 0`, one has

```text
δ(x′) ⩽ n.
```

Let `Z′` be the set of points `x′` of `X′` such that `F_{x̄′} = 0`. Then, if `Z = h(Z′)`, one has by (i) `Z′ = h^{−1}(Z)`; let `x′ ∈ X′`, `x = h(x′)`, `s′ = f′(x′)`, `s = f(x)`. It follows from 2.1.1 and from the fact that the function `δ` decreases under specialization that it suffices to prove the inequality `δ(x′) ⩽ n` when `x` is a maximal point of `Z` and `x′` is such that

```text
r = deg.tr. k(x)/k(s) = deg.tr. k(x′)/k(s′) and d = dim {s} = dim {s′}.
```

Let `x′` be such a point; it suffices to show that one can find a scheme `X_1` étale over `X`, affine, such that one has

```text
H^{d+r}(X′_1, F) ≠ 0.
```

The set `Z′` is constructible (SGA 4 IX 2.4), hence the same holds for `Z` (EGA IV 1.9.12); one can then suppose, by restricting `X` to a neighborhood of `x`, that `Z` is an irreducible closed set with generic point `x`. Let `T = f(Z)`; `T` is a constructible set contained in `{s}`; one can therefore find an affine open `U` of `S` such that `s ∈ U` and that `T ∩ U = T_U` is an irreducible closed set of `U` with generic point `s`.

<!-- original page 247 -->

Let then `V` be a scheme étale over `X`, affine, whose image in `X` contains `x` and whose image in `S` is contained in `U`; let `Z_V` be the inverse image of `Z` in `V` and `u : Z_V → T_U` the canonical morphism. Let `W` be a scheme étale over `U`, affine; we then denote by `T_W` the inverse image of `T_U` in `W` and let `X_1 = W ×_U V`. Since `F` is null outside `Z′`, one has the spectral sequence

```text
E_2^{pq} = H^p((T_W)′, R^q u′_*(F|_{(Z_V)′})) ⟹ H^{p+q}(X′_1, F).
```

We shall show that one can choose `V` and `W` such that one has

a) `E_2^{pq} = 0` for `p > d` and for `q > r`.

b) `E_2^{dr} ≠ 0`.

It will then follow from the spectral sequence that `H^{d+r}(X′_1, F) ≠ 0`.

1°) Set `G^q = R^q u′_*(F|_{(Z_V)′})`; then one has:

```text
(G^q)_{s′} = H^q((Z_V)′_{s′}, F|_{(Z_V)′_{s′}}),
```

since `s′` is a maximal point of `(T_U)′`. Since the fiber `(Z_V)′_{s′}` is an affine scheme of finite type of dimension `r` over a separably closed field, it follows from 3.1 that one has

```text
(G^q)_{s′} = 0 for q > r.
```

<!-- original page 248 -->

For `q > r`, let `Y′_q` be the set of points of `(T_U)′` where the geometric fiber of `G^q` is `≠ 0` and `Y_q = g(Y′_q)`; then one has `Y′_q = g^{−1}(Y_q)` by (ii), so `Y_q` is a constructible subset of `T_U` (SGA 4 XIX 5.1 and EGA 1.9.12) which does not contain `s`; restricting `U` to an open neighborhood of `s`, one can suppose that one has `G^q = 0` for `q > r`, hence `E_2^{pq} = 0` for `q > r`.

Moreover, since `(T_W)′` is an affine scheme of finite type over `g^{−1}({s})`, one has, whatever `q` (cf. 3.1):

```text
H^p((T_W)′, G^q) = 0 for p > dim g^{−1}({s}) = d,
```

whence condition a).

2°) Let us show that one can choose `V` such that `(G^r)_{s′} ≠ 0`. By (i), there exists a constructible sheaf `I`, defined on a finite separable extension `K` of `k(x)`, whose inverse image on `(X′)_{(Spec K)}` is isomorphic to `F|_{(X′)_{(Spec K)}}`. By 3.3, one finds a finite separable extension `L` of `K` such that, if `v : Spec L → Spec k(s)` denotes the canonical morphism, one has `R^r v_*(I) ≠ 0`. Since the morphism `S′_s → Spec k(s)` is regular, one has by (SGA 4 XIX 4.2):

```text
R^r v′_*(F|_{(Spec L)′}) ≃ (R^r v_*(I))′ ≠ 0.
```

By Lemma 3.4, one can find a scheme `X_2` étale over `X`, affine, and a point `x_2` of `X_2` above `x` such that `L` is `k(x)`-isomorphic to `k(x_2)`, and one can suppose `X_2` over `U`. Since `x` is a maximal point of `Z`, one has

<!-- original page 249 -->

```text
Spec L ≃ lim ← _V Z_V,
```

where `V` runs over the affine open neighborhoods of `x_2`. One deduces by passage to the limit (SGA 4 VII 5.8), after restriction to the geometric fiber at `s′`:

```text
(R^r v′_*(F|_{Spec L})′)_{s′} = lim → _V (R^r u′_*(F|_{(Z_V)′}))_{s′},
```

which shows that one can find `V` such that `(G^r)_{s′} ≠ 0`.

3°) The scheme `V` having been chosen in 2°), let us show that one can choose the scheme `W` such that one has

```text
E_2^{dr} = H^d((T_W)′, G^r) ≠ 0.
```

By (ii), there exists a constructible sheaf `J`, defined on a finite separable extension `K` of `k(s)`, whose inverse image on `(S′)_{(Spec K)}` is isomorphic to `G^r|_{(S′)_{(Spec K)}}`. By Lemma 3.2, one can find a finite separable extension `L` of `K` such that one has `H^d(Spec L, J) ≠ 0`. Since the morphism `(S′)_{(Spec L)} → Spec L` is acyclic (SGA 4 XIX 4.1 and XV 1.10 and 1.16), one has

```text
H^d((Spec L)′, G^r|_{(S′)_{(Spec L)}′}) = H^d(Spec L, J) ≠ 0.
```

By 3.4, one can find a scheme `U_1` étale over `U`, affine, and a point `s_1` above `s`, such that `k(s_1)` is `k(s)`-isomorphic to `L`. Now, `s` being a maximal point of `T_U`, one has

```text
Spec L ≃ lim ← _W T_W,
```

where `W` runs over the affine open neighborhoods of `s_1`. One deduces that `(Spec L)′ ≃`

<!-- original page 250 -->


`lim ← _W (T_W)′`, and by passage to the limit (SGA 4 VII 5.8):

```text
H^d((Spec L)′, G^r|_{(Spec L)′}) ≃ lim → _W H^d((T_W)′, G^r|_{(T_W)′});
```

consequently one can find `W` such that one has

```text
H^d((T_W)′, G^r|_{(T_W)′}) ≠ 0,
```

which completes the proof of the theorem.

**Corollary 3.6.**
<!-- label: XIV.3.6 -->

The hypotheses concerning `S, S′, f, f′, m` are those of 3.5. Denote now by `F` a complex of sheaves of `ℤ/mℤ`-modules on `X′`, bounded below and with constructible cohomology, and whose cohomology sheaves satisfy conditions (i) and (ii) of 3.5. Let `n` be an integer, and suppose that, for every scheme `X_1` étale over `X`, affine, one has

```text
H^i(X′_1, F) = 0 for i > n.
```

Then, if `x̄′` is a geometric point above a point `x′` of `X′` such that, for some integer `j`, `(H^j(F))_{x̄′} ≠ 0`, one has

```text
δ(x′) ⩽ n − j.
```

Let `T′` be the set of points of `X′` where the conclusion of 3.7 fails, and suppose `T′ ≠ ∅`; let `T = f(T′)`, `x` a maximal point of `T`, and `x′` a point of `X′` above

<!-- original page 251 -->

`x`. Let `j` be the largest integer such that `(H^j(F))_{x̄′} ≠ 0`; one therefore has `r = δ(x) > n − j`. Let `Z′_q` be the set of points where the geometric fiber of `H^q(F)` is `= 0` and `Z_q = h(Z′_q)`; as in the proof of 3.5, `Z_q` is constructible. One evidently has `Z′_q = ∅` for `q > n` and for `q` sufficiently small. The other values of `q` are distributed in three subsets. Let

```text
Q_1 = {q | x ∈ Z_q and a generization of x distinct from x is ∉ Z_q}.
```

One has `j ∈ Q_1` and one can find an affine open neighborhood `U_1` of `x` such that, for every `q ∈ Q_1`, `U_1 ∩ Z_q` is an irreducible closed set with generic point `x`. If `q ∈ Q_1`, one has

```text
(∗)    δ(H^q(F)|_{U′_1}) = δ(x)    (for the definition of δ(H^q(F)) cf. 3.1).
```

Let

```text
Q_2 = {q | no generization of x belongs to Z_q}.
```

Then, if `j < q ⩽ n`, one has `q ∈ Q_2`, and one can find an affine open neighborhood `U_2` of `x` such that, for every `q ∈ Q_2`, one has `Z_q ∩ U_2 = ∅`; thus

```text
(∗∗)   H^q(F)|_{U′_2} = 0 for q ∈ Q_2.
```

Let finally

```text
Q_3 = {q | Z_q contains strict generizations of x}.
```

Then one can find an affine open neighborhood `U_3` of `x` such that, for every `q ∈ Q_3`, all the maximal points of `Z_q ∩ U_3` are generizations of `x`. If `q ∈ Q_3`, one has

```text
(∗∗∗)  δ(H^q(F)|_{U′_3}) ⩽ n − q.
```

For every scheme `X_1` étale over `U_1 ∩ U_2 ∩ U_3`, affine, consider the

<!-- original page 252 -->

hypercohomology spectral sequence

```text
E_2^{pq} = H^p(X′_1, H^q(F)) ⟹ H^{p+q}(X′_1, F).
```

One has `E_2^{pq} = 0` for `q ∈ Q_2` by (∗∗). One has `E_2^{pq} = 0` for `p + q ⩾ r + j` except perhaps for `p = r`, `q = j`. Indeed this is clear if `q ∈ Q_2`; if `q ∈ Q_1`, one has `p > r` unless `p = r`, `q = j`, and this follows from 3.1 taking (∗) into account; finally if `q ∈ Q_3`, since `r > n − j`, one has `p > n − q` and the assertion follows from 3.1 taking (∗∗∗) into account. Given that `H^{r+j}(X′_1, F) = 0`, it follows from the spectral sequence that one has

```text
H^r(X′_1, H^j(F)) = 0;
```

now this entails, by 3.5, `δ(x) < r`, which is absurd.

**Corollary 3.7.**
<!-- label: XIV.3.7 -->

Let `S` be a strictly local excellent scheme of characteristic zero, `f : X → S` a morphism locally of finite type, `m` a power of a prime number, `F` a complex of sheaves of `ℤ/mℤ`-modules on `X`, bounded below with constructible cohomology, and `n` an integer. Then the following conditions are equivalent:

(i) For every scheme `X_1` étale over `X`, affine, one has

```text
H^i(X_1, F) = 0 for i > n.
```

(ii) For every geometric point `x̄` above the point `x` of `X` and for every integer `j`

<!-- original page 253 -->

such that `(H^j(F))_{x̄} ≠ 0`, one has

```text
δ(x) ⩽ n − j.
```

(i) ⇒ (ii) is the particular case of 3.6 obtained by taking `S = S′`.

(ii) ⇒ (i) follows immediately from 3.1, using the hypercohomology spectral sequence

```text
H^p(X_1, H^q(F)) ⟹ H^*(X_1, F).
```

## 4. Main theorem and variants

**4.0.** Let `g : X → S` be a separated morphism of finite type, `T` a closed part of `S`, `Z = g^{−1}(T)`, and `F` a complex of abelian sheaves on `X` bounded below. We call `i`-th cohomology group of `F` with proper support, with support in `Z`, the group

```text
H^i_{Z!}(X/S, F) = H^i_T(S, R^! g(F)),
```

<!-- original page 254 -->

where `R^! g` denotes "direct image with proper support" (SGA 4 XVII). In the particular case where `g` is proper, one simply has

```text
H^i_{Z!}(X/S, F) = H^i_Z(X, F).
```

**Proposition 4.1.**
<!-- label: XIV.4.1 -->

Let `f : U → S` be a morphism of finite type, `F` a complex of abelian sheaves on `U` bounded below. Suppose one has a factorization of `f`:

```text
U --i--> X
 \      /
  \    /
   f  g
    \/
    S
```

where `i` is an open immersion and `g` a separated morphism of finite type, and denote by `G` a complex of abelian sheaves on `X` bounded below that prolongs `F`. Let `Y` be a closed subscheme of `X` with underlying space `X − U`, so that one has a commutative diagram:

```text
Y --j--> X
 \      /
  h    g
   \  /
    S
```

Let finally `n` be an integer and `T` a closed part of `S`. Then the following conditions are equivalent:

(i) One has `prof_T(R^! f(F)) ⩾ n`.

(ii) The canonical morphism

```text
ℋ^i_T(R^! g(G)) → ℋ^i_T(R^! h(j^* G))
```

is bijective for `i < n − 1`, injective for `i = n − 1`.

<!-- original page 255 -->

(iii) For every scheme `S′` étale over `S`, if one denotes by `X′` (resp. `f′`, resp. etc.) the scheme `X ×_S S′` (resp. the morphism `f_{(S′)}`, resp. etc.), the canonical morphism

```text
H^i_{g′^{−1}(T′)!}(X′/S′, G′) → H^i_{h′^{−1}(T′)!}(Y′/S′, j′^* G′)
```

is bijective for `i < n − 1`, injective for `i = n − 1`.

Consider in the derived category `D⁺(X)` (cf. [3]) the distinguished triangle

```text
        j_* j^* G
       ↗      ↘
   i_! F ←-------- G.
```

In applying to this triangle the functor `R^! g`, one obtains the triangle

```text
              R^! h(j^* G)
             ↗            ↘
(∗)    R^! f(F) ←--------- R^! g(G).
```

Let us show (i) ⇔ (ii). Indeed, by Definition 1.2, (i) is equivalent to the relation

```text
ℋ^i_T(R^! f(F)) = 0 for i < n;
```

now one deduces from (∗) the exact sequence of sheaves

```text
→ ℋ^i_T(R^! f(F)) → ℋ^i_T(R^! g(G)) → ℋ^i_T(R^! h(j^* G)) →,
```

whence the equivalence of (i) and (ii).

<!-- original page 256 -->

(i) ⇔ (iii). Indeed (i) is equivalent to saying that, for every scheme `S′` étale over `S`, one has the relation

```text
(∗∗) H^i_{T′}(S′, R^! f′(F′)) = 0 for i < n.
```

Now one deduces from (∗) the exact sequence of abelian groups

```text
→ H^i_{T′}(S′, R^! f′(F′)) → H^i_{T′}(S′, R^! g′(G′)) → H^i_{T′}(S′, R^! h′(j′^* G′)) →;
```

taking 4.0 into account, this exact sequence writes in the form

```text
→ H^i_{T′}(S′, R^! f′(F′)) → H^i_{g′^{−1}(T′)!}(X′/S′, G′) → H^i_{h′^{−1}(T′)!}(Y′/S′, j′^* G′) →.
```

The equivalence of (i) and (iii) follows, taking the form (∗∗) of (i) into account.

**4.2.0.** When `f : U → S` is affine, we shall give local conditions on `F` for conditions (i) to (iii) of 4.1 to be verified. In what follows, the schemes considered are excellent schemes of characteristic zero, the sheaves are sheaves of `ℤ/mℤ`-modules, where `m` is a power of a prime number. If one had resolution of singularities in the sense of (SGA 4 XIX), the results stated, as well as their proofs, would still be valid for excellent schemes of equal characteristic, with `m` prime to the characteristic.

**Theorem 4.2.**
<!-- label: XIV.4.2 -->

<!-- original page 257 -->

Let `S` be an excellent scheme of characteristic zero and `f : U → S` a separated morphism of finite type. Let `F` be a complex of sheaves of `ℤ/mℤ`-modules on `U`, bounded below with constructible cohomology, `n` an integer, and `T` a closed part of `S`. Then the following conditions are equivalent:

(i) For every scheme `U_1` étale over `U`, affine over `S`, one has, denoting by `f_1` the structural morphism of `U_1` and by `F_1` the restriction of `F` to `U_1`:

```text
prof_T(R^! f_1(F_1)) ⩾ n
```

(cf. Prop. 4.1 on the meaning of this relation).

(ii) For every point `u` of `U`, one has:

```text
prof_u(F) ⩾ n − δ_T(u),
```

where one sets (cf. 2.2): `δ_T(u) = deg.tr.(k(x)/k(s)) + codim({s} ∩ T, {s})`.

*Proof.*

1°) Let `t` be a point of `T`, `S̄` the strict localization of `S` at a geometric point above `t`, and `S′` the completion of `S̄` with closed point `t′`; then `S̄` is excellent by (EGA IV 7.9.5), so `S′` is a complete strictly local excellent scheme. Given a scheme `U` over `X` (resp. an `S`-morphism `f`, resp. etc.), we shall denote by `U′` (resp. `f′`, resp. etc.) the scheme `U ×_S S′` (resp. the morphism `f_{(S′)}`, resp. etc.). One has the cartesian square

```text
U′ --h--> U
|         |
f′        f
|         |
v         v
S′ --g--> S,
```

<!-- original page 258 -->

in which the morphism `g` is regular (EGA IV 7.8.2). Let us show that it suffices to prove that (for every point `t ∈ T`) the two following properties are equivalent:

(i)_t For every scheme `U_1` étale over `U`, affine over `S`, setting `f_1 : U_1 → S`, one has

```text
prof_{t′}(R^! f′_1(F′_1)) ⩾ n.
```

(ii)_t For every point `u′` of `U′`, one has

```text
prof_{u′}(F′) ⩾ n − δ_{t′}(u′).
```

It suffices to prove the following lemma:

**Lemma 4.2.1.**
<!-- label: XIV.4.2.1 -->

One has (i) ⇔ (i)_t for every `t ∈ T` and (ii) ⇔ (ii)_t for every `t ∈ T`.

(i) ⇔ (i)_t for every `t ∈ T`. Indeed (i) is equivalent to saying that, for every scheme `U_1` étale over `U`, affine over `S`, one has

```text
prof_T(R^! f_1(F_1)) ⩾ n;
```

now by 1.8

```text
prof_T(R^! f_1(F_1)) = inf_{t ∈ T} prof_t(R^! f_1(F_1)).
```

Since `g^*(R^! f_1(F_1)) ≃ R^! f′_1(F′_1)` (SGA 4 XVII), one has by 1.16

```text
prof_t(R^! f_1(F_1)) = prof_{t′}(R^! f′_1(F′_1)),
```

<!-- original page 259 -->

so (i) is equivalent to saying that one has, for every `t ∈ T`, `prof_{t′}(R^! f′_1(F′_1)) ⩾ n`, which is none other than (i)_t.

(ii)_t for every `t ∈ T` ⇒ (ii). Indeed let `u ∈ U`; one must show the relation

```text
prof_u(F) ⩾ n − δ_T(u),
```

where `δ_T(u) = inf_{t ∈ T ∩ {s}} δ_t(u)` (cf. 2.2); one is therefore reduced to showing that one has, for every `t ∈ T ∩ {s}`

```text
prof_u(F) ⩾ n − δ_t(u).
```

Let `u′` be a point of `U′` such that `h(u′) = u` and `δ_{t′}(u′) = δ_t(u)` (cf. 2.1.1). Since `h` is locally acyclic (SGA 4 XIX 4.1), it follows from 1.16 and from the fact that `u′` is a generic point of `U′_u` that one has

```text
prof_{u′}(F′) = prof_u(F).
```

But one has by (ii)_t `prof_u(F) = prof_{u′}(F′) ⩾ n − δ_t(u)`, which proves (ii).

(ii) ⇒ (ii)_t for every `t`. With the notations of 2.2.1, for every point `u′` of `U′`, one has by 1.16

```text
prof_{u′}(F′) ⩾ prof_u(F) + 2 dim h_{u′}^{−1}(u) ⩾ prof_u(F) + dim h_{u′}^{−1}(u).
```

Taking 2.2.1 and (ii) into account, one obtains

```text
prof_{u′}(F′) ⩾ n − δ_T(u) + dim h_{u′}^{−1}(u) ⩾ n − δ_{t′}(u′),
```

which is none other than (ii)_t.

<!-- original page 260 -->

2°) (ii)_t ⇔ (i)_t. One immediately reduces to the case where `F` is bounded, by truncating `F` at a sufficiently high rank. One can realize `S′` as a closed subset of a complete regular local scheme, hence excellent; it then follows from (SGA 5 I 3.4.3) that there exists a dualizing complex `K` on `S′` and that `R^! f′(K) = K′` is a dualizing complex on `U′`. We shall choose `K` such that `δ^K(t′) = 0` (for the definition of `δ^K(t′)`, cf. 2.3), and denote by `DF′` the dual of `F′` with respect to `K′`. One can reformulate hypothesis (ii)_t as follows:

**Lemma 4.2.2.**
<!-- label: XIV.4.2.2 -->

Let `u′` be a point of `U′`; then the following conditions are equivalent:

(i) One has `prof_{u′}(F′) ⩾ n − δ_{t′}(u′)`.

(ii) One has `(H^q(DF′))_{ū′} = 0` for `q > −n − δ_{t′}(u′)` (`ū′` geometric point above `u′`).

Let `Ū′` be the strict localization of `U′` at `ū′` and `F̄′` the inverse image of `F′` by the morphism `Ū′ → U′`. The relation `prof_{u′}(F′) ⩾ n − δ_{t′}(u′)` is equivalent by definition to:

```text
(∗) H^i_{ū′}(F̄′) = 0 for i > n − δ_{t′}(u′).
```

Let `DH^i_{ū′}(F̄′)` be the dual of the abelian group `H^i_{ū′}(F̄′)` with respect to `ℤ/mℤ`. By 2.3.2, `K′[−2 δ_{t′}(u′)] = K′′` satisfies `δ^{K′′}(u′) = 0`; since `F′` has constructible cohomology, one has `DF′ = D(F̄′)` and the local duality theorem (SGA 5 I 4.5.3) shows then

<!-- original page 261 -->

that one has

```text
DH^i_{ū′}(F̄′) ≃ H^{−i − 2 δ_{t′}(u′)}(DF′)_{ū′}.
```

So (∗) is equivalent to the relation

```text
(∗∗) (H^q(DF′))_{ū′} = 0 for q > −n − δ_{t′}(u′).
```

We are now in a position to prove the theorem. The relation (ii)_t is equivalent to the relation (∗∗). Let `G^q = H^q(DF′)`; the affine Lefschetz theorem (3.1) entails in particular that, for every scheme `U_1` étale over `U`, affine over `S`, one has

```text
H^p(U′_1, G^q) = 0 for p > δ(G^q),
```

where `δ(G^q)` is the supremum of the `δ_{t′}(u′)` for the `u′` such that `(G^q)_{ū′} ≠ 0`; by (∗∗) one has `δ(G^q) ⩽ −n − q`, so (ii)_t entails the relation

```text
H^p(U′_1, H^q(DF′)) = 0 for p > −q − n.
```

Taking the hypercohomology spectral sequence of the functor "sections over `U′_1`" with respect to the complex `DF′`:

```text
E_2^{pq} = H^p(U′_1, H^q(DF′)) ⟹ H^{p+q}(U′_1, DF′),
```

one obtains the relation

```text
(∗∗∗) H^i(U′_1, DF′) = 0 for i > −n.
```

<!-- original page 262 -->

Conversely, suppose the preceding relation verified, for every `U_1` étale over `U`, affine over `S`. Apply Proposition 3.6 by replacing `S` by `S̄`; the hypotheses of 3.6 concerning `S` are satisfied, since for every scheme `U_1` étale over `U`, affine, one can find a scheme over `U_1` that comes by inverse image from an étale scheme over `U` affine over `S`; as for the hypotheses concerning `F`, they are satisfied thanks to 2.3.3. One thus has, for every point `u′` of `U′` such that `(H^q(DF′))_{ū′} ≠ 0`:

```text
δ_{t′}(u′) ⩽ −n − q,
```

which is none other than the relation (∗∗); one has therefore proved the equivalence

```text
(ii)_t ⇔ (∗∗∗).
```

We are going to transform the relation (∗∗∗); one has first

```text
H^i(U′_1, DF′) = H^i(R f′_{1*}(DF′_1))_{t′};
```

but by (SGA 5 I 1.12), there exists a canonical isomorphism

```text
R f′_{1*}(DF′_1) ≃ D(R^! f′_1(F′_1)),
```

where `D(R^! f′_1(F′_1))` denotes the dual of `R^! f′_1(F′_1)` with respect to `K`. One sees thus that (ii)_t is equivalent to

```text
(H^i(D(R^! f′_1(F′_1))))_{t′} = 0 for i > −n.
```

<!-- original page 263 -->

Applying again the local duality theorem (SGA 5 I 4.5.3), but this time at the point `t′`, one finds

```text
H^i(D(R^! f′_1(F′_1)))_{t′} ≃ D(H^{−i}_{t′}(R^! f′_1(F′_1))),
```

and finally (ii)_t is equivalent to the relation

```text
H^i_{t′}(R^! f′_1(F′_1)) = 0 for i < n,
```

that is, `prof_{t′}(R^! f′_1(F′_1)) ⩾ n`, which completes the proof of the theorem.

**Remark 4.2.3.**
<!-- label: XIV.4.2.3 -->

The reasoning simplifies considerably when one supposes that `S` admits (at least locally) a dualizing complex (for example is locally immersible in a regular scheme). This avoids recourse to a completion (the passage to the strictly local case being immediate), to 2.3.3, and to the rather unpleasant technical statement 3.6, which one can then replace by the more sympathetic reference 3.7.

**Corollary 4.3.**
<!-- label: XIV.4.3 -->

Let `S` be an excellent scheme of characteristic zero and `f : U → S` a separated morphism of finite type, such that `U` is the union of `c + 1` open sets, affine over `S`. Let `F` be a complex of sheaves of `ℤ/mℤ`-modules, bounded below with constructible cohomology, `n` an integer, and `T` a closed part of `S`. Suppose that, for every point `u ∈ U`, one has

```text
prof_u(F) ⩾ n − δ_T(u).
```

Then one has

<!-- original page 264 -->

```text
prof_T(R^! f(F)) ⩾ n − c.
```

Let indeed `U_j`, `0 ⩽ j ⩽ c`, be a covering of `U` by open sets `U_j` affine over `S`. Resuming the notations of the proof of 4.2, one has, for every `j`,

```text
H^i(U′_j, H^q(DF′)) = 0 for i > −n.
```

Using the spectral sequence relating the cohomology of `U` to that of the covering formed by the `U_j` (SGA 4 V 2.4), the preceding relation shows that one has

```text
H^i(U′, H^q(DF′)) = 0 for i > −n + c.
```

The corollary follows from the end of the proof of 4.2.

**Corollary 4.4.**
<!-- label: XIV.4.4 -->

Let `S` be an excellent scheme of characteristic zero, `g : X → S` a morphism, `U` an open set of `X`, union of `c + 1` opens affine over `S`, `Y` a closed subscheme with underlying space `X − U`, and `j : Y → X` the natural morphism. Let `F` be a complex of sheaves of `ℤ/mℤ`-modules on `X`, bounded below with constructible cohomology, `T` a closed part of `S`, and `n` an integer. Suppose that, for every point `u` of `U`, one has

```text
prof_u(F) ⩾ n − δ_T(u).
```

Then the canonical morphism

<!-- original page 265 -->

```text
H^i_{g^{−1}(T)!}(X/S, F) → H^i_{(g^{−1}(T) ∩ Y)!}(Y/S, j^* F)
```

is bijective for `i < n − c − 1`, injective for `i = n − c − 1`.

This follows immediately from 4.1 and 4.3.

**Corollary 4.5** (Local Lefschetz theorem).
<!-- label: XIV.4.5 -->

Let `S` be an excellent henselian local scheme of characteristic zero, `t` the closed point of `S`, `X` a scheme proper over `S′ = S − {t}`, and `U` an open set of `X`, union of `c + 1` affine opens. Let `Y` be a closed subscheme of `X` with underlying space `X − U`, `j : Y → X` the canonical morphism, `F` a complex of sheaves of `ℤ/mℤ`-modules on `X`, bounded below with constructible cohomology, and `n` an integer. Suppose that, for every point `u` of `U`, one has

```text
prof_u(F) ⩾ n − δ_{t′}(u), where δ_{t′}(u) = δ_t(u) − 1.
```

Then the canonical morphism

```text
H^i(X, F) → H^i(Y, j^* F)
```

is bijective for `i < n − c − 1`, injective for `i = n − c − 1`.

Let `f : U → S` be the canonical morphism; it follows from 4.2, applied by replacing `n` by `n + 1`, that one has

```text
prof_t(R^! f(F|_U)) ⩾ n + 1 − c.
```

<!-- original page 266 -->

The preceding relation shows that the canonical morphism

```text
H^i(S, R^! f(F|_U)) → H^i(S′, R^! f(F|_U))
```

is bijective for `i < n − c`, injective for `i = n − c`. Since `R^! f(F|_U)` is null outside `S′`, one has `H^i(S, R^! f(F|_U)) ≃ H^i(R^! f(F|_U))_t = 0`, and consequently

```text
(∗) H^i(S′, R^! f(F|_U)) = 0 for i < n − c.
```

Let `g : X → S′`, `h : Y → S′`, `f′ : U → S′` be the canonical morphisms. It follows from the distinguished triangle

```text
              R h_*(j^* F)
             ↗            ↘
   R^! f′(F|_U) ←----------- R g_*(F)
```

that condition (∗) is equivalent to the fact that the morphism

```text
H^i(S′, R g_*(F)) → H^i(S′, R h_*(j^* F))
```

is bijective for `i < n − c − 1`, injective for `i = n − c − 1`. Since this morphism is canonically identified with the morphism

```text
H^i(X, F) → H^i(Y, j^* F),
```

the conclusion follows immediately.

**Corollary 4.6** (Global Lefschetz theorem).
<!-- label: XIV.4.6 -->

<!-- original page 267 -->

Let `S` be the spectrum of a field, `X` a scheme proper over `S`, and `U` an open set of `X` union of `c + 1` affine opens. Let `Y` be a closed subscheme of `X` with underlying space `X − U`, `j : Y → X` the canonical morphism, `F` a complex of sheaves of `ℤ/mℤ`-modules on `X`, bounded below with constructible cohomology, and `n` an integer. Suppose that, for every point `u` of `U`, one has

```text
prof_u(F) ⩾ n − dim({u}).
```

Then the canonical morphism

```text
H^i(X, F) → H^i(Y, j^* F)
```

is bijective for `i < n − c − 1`, injective for `i = n − c − 1`.

More generally, if `g : X → S` is a separated morphism of finite type, the hypotheses on `S`, `U`, `Y`, `F` being the same as before, then the canonical morphism

```text
H^i_!(X/S, F) → H^i_!(Y/S, j^* F)
```

(where `H^i_!` denotes cohomology with proper support, that is, `H^i_!(X/S, F) = H^i(S, R^! g(F))`) is bijective for `i < n − c − 1`, injective for `i = n − c − 1`.

The corollary is a particular case of 4.4, with `T = S`.

Here is a partial converse to 4.3:

**Proposition 4.7.**
<!-- label: XIV.4.7 -->

<!-- original page 268 -->

Let `S` be a noetherian scheme, `f : U → S` a morphism of finite type. Suppose that there exists a dualizing complex `K` on `S` and that `R^! f(K)` is a dualizing complex on `U`. Let `T` be a closed part of `S` and `c` an integer. Then the following conditions are equivalent:

(i) For every complex of sheaves of `ℤ/mℤ`-modules `F` on `U`, bounded below with constructible cohomology, and for every integer `n` such that, for every point `u` of `U`,

```text
prof_u(F) ⩾ n − δ_T(u),
```

one has

```text
prof_T(R^! f(F)) ⩾ n − c.
```

(ii) For every constructible sheaf of `ℤ/mℤ`-modules `G` on `U` and for every point `t ∈ T`, one has

```text
(R^p f_*(G))_t = 0 for p > δ(G, f, t) + c
```

(let us recall from (SGA 4 XIX 6.0) that `δ(G, f, t) = sup{δ_t(u) | t ∈ {u} and G_u ≠ 0}`).

N.B. Condition (ii) is satisfied by virtue of 3.1 if `f` is separated and if `U` is, locally on `S` for the étale topology, a union of `c + 1` opens affine over `S`, so 4.7 contains 4.3.[^XIV-4-1]

One can evidently suppose that `S` is local and that `T` is the closed point `t` of `S`.

<!-- original page 269 -->

The proof of (ii) ⇒ (i) is essentially identical to part 2°) of the proof of 4.2. Let us show briefly that (i) ⇒ (ii). The local duality theorem (SGA 5 I 4.3.2) applied to `DG` shows that

```text
D H^i_u(DG) ≃ H^{−i − 2 δ_t(u)}(G)_u.
```

Since `G` is reduced to degree `0`, one therefore has `H^i_u(DG) = 0` except perhaps for `i = −2 δ_t(u)`; more precisely

```text
prof_u(DG) = { −2 δ_t(u)  if G_u ≠ 0,
              { ∞          if G_u = 0.
```

It follows that one has, whatever `u ∈ U`:

```text
prof_u(DG) ⩾ −n − δ_t(u).
```

<!-- original page 270 -->

It then follows from hypothesis (i) that one has `prof_t(R^! f(DG)) ⩾ −n − c`. One transforms this relation using the isomorphism `R^! f(DG) ≃ D(R f_*(G))` (SGA 5 I 1.12) and applying the local duality theorem at the point `t`; one obtains thus

```text
H^i(R f_*(G))_t = 0 for i > n + c,
```

which is none other than (ii).

**4.8.** The hypotheses being those of 4.4 with `g` proper (resp. 4.5, resp. 4.6 with `g` proper), if `V` is an open neighborhood of `Y` in `X`, the morphism

```text
H^i(V, F) → H^i(Y, j^* F)
```

is bijective for `i < n − c − 1`, injective for `i = n − c − 1`. If `ι : V → X` is the canonical morphism, it suffices indeed to see that one applies 4.4 (resp. 4.5, resp. 4.6) to the complex `R ι_*(F|_V)`. One can ask whether the preceding morphism is bijective for `i = n − c − 1`, injective for `i = n − c`. It evidently suffices for the hypotheses to be verified when one replaces `n` by `n + 1`; the proposition that follows shows that it suffices to require a little less.

**Proposition 4.9.**
<!-- label: XIV.4.9 -->

Let `S` be a local excellent scheme of characteristic zero with closed point `t` (resp. in addition to the preceding conditions, one supposes `S` henselian), `f : X → S` a scheme proper over `S` (resp. proper over `S − {t}`), and `U` an open set of `X` union of `c + 1` affine opens. Let `Y` be a closed subscheme of `X` with underlying space `X − U`, `j : Y → X` the canonical morphism, `F` a complex of sheaves of `ℤ/mℤ`-modules on `X`, bounded below with constructible cohomology, and `n` an integer. Suppose that one has, for every point `u` of `U`,

```text
prof_u(F) ⩾ inf(n − 1, n − δ_t(u))  (resp. prof_u(F) ⩾ inf(n − 1, n + 1 − δ_t(u))).
```

<!-- original page 271 -->

Then for every open neighborhood `V` of `Y` in `X`, the canonical morphism

```text
H^i_{f^{−1}(t)}(V, F) → H^i_{f^{−1}(t) ∩ Y}(Y, j^* F)   (resp. H^i(V, F) → H^i(Y, j^* F))
```

is bijective for `i < n − c − 2` and injective for `i = n − c − 2`. Moreover, there exists an open neighborhood `V_0` of `Y` in `X` such that, for every other such `V` with `V ⊂ V_0`, the canonical morphism

```text
H^i_{f^{−1}(t) ∩ V}(V, F) → H^i_{f^{−1}(t) ∩ Y}(Y, j^* F)   (resp. H^i(V, F) → H^i(Y, j^* F))
```

is bijective for `i < n − c − 1`, injective for `i = n − c − 1`.

*Proof.* Let us set, for simplicity, `δ_{t′}(u) = δ_t(u)` (resp. `δ_{t′}(u) = δ_t(u) − 1`). One deduces from 4.8 the first assertion of 4.9, since the hypotheses of 4.4 (resp. 4.5) are verified when one replaces `n` by `n − 1`. They are also verified for `n` itself, except at the points `u` such that `δ_{t′}(u) = 0`. Now, for `u ∈ U`, to say that `δ_{t′}(u) = 0` is equivalent to saying that `u` is a closed point of `U_t` (resp. a closed point of `X`). Let `E` be the set of points of `U` such that `δ_{t′}(u) = 0`; let us show that, for all the points `u ∈ E`, except a finite number, one has `prof_u(F) ⩾ n`. Let `S̄` be the strict localization of `S` at `t`, `S′` the completion of `S̄` with closed point `t′`, and consider the cartesian square

```text
U′ --h--> U
|         |
f′        f
|         |
v         v
S′ --g--> S.
```

<!-- original page 272 -->

The depth hypotheses at the points of `U` are preserved when one replaces `U` by `U′` and `F` by the inverse image `F′` of `F` on `U′`. Indeed let `u′ ∈ U′` and `u = h(u′)`. If `u ∉ E`, one has the relation `prof_u(F) ⩾ n − δ_{t′}(u)`, and it follows from 4.2.1 that this entails the relation `prof_{u′}(F′) ⩾ n − δ_{t′}(u′)`. If `u ∈ E`, `u′` is a closed point of `U′_t` (resp. a closed point of `X′ = X ×_S S′`), and since the fiber `U′_u` of `h` at `u` is of dimension zero and `h` regular, it follows from 1.16 that one has `prof_{u′}(F′) = prof_u(F) ⩾ n − 1`.

Let then `K` be a dualizing complex on `S′`, normalized at the closed point `t′`, and `DF′` the dual of `F′` with respect to `R^! f(K)`. By 4.2.2, the étale depth hypotheses at the points of `U′` translate by the relations:

```text
(H^q(DF′))_{ū′} = 0 for q > −n − δ_{t′}(u′)  (resp. q > −n − 2 − δ_{t′}(u′)),
```

if `u′` is not a point of `E′ = h^{−1}(E)`,

```text
(H^q(DF′))_{ū′} = 0 for q > −(n − 1)  (resp. q > −n − 1), if u′ ∈ E′.
```

Let `G = H^{−(n − 1)}(DF′)` (resp. `G = H^{−n − 1}(DF′)`); since `G` is a constructible sheaf, the set of points at which the geometric fiber is non-null is a constructible set (SGA 4 IX 2.4 (iv)); now by hypothesis this set is contained in the set `E′` of closed points of `U′_{t′}` (resp. of points of `U′` closed in `X′`); it therefore follows from 4.9.1 below that this set reduces to a finite number of points. Applying 4.2.2, one sees that, for all the points of `E′` except a finite number, one has `prof_{u′}(F′) ⩾ n`. It follows by 1.16 that, for all the points of `E` except a finite number, one has

<!-- original page 273 -->

```text
prof_u(F) ⩾ n.
```

Let `V` be an open neighborhood of `Y` in `X`, contained in the complement in `X` of the finite set of points `u` of `E` for which one has `prof_u(F) = n − 1`. If `ι : V → X` is the canonical immersion, let

```text
F_1 = R ι_*(F|_V);
```

then `F_1` is a complex of sheaves on `X` with constructible cohomology (SGA 4 XIX 5.1) and bounded below. We shall see that, for every point `u` of `U`, the complex `F_1` verifies the relation

```text
(∗)  prof_u(F_1) ⩾ n − δ_{t′}(u).
```

If `u ∈ U ∩ V`, one has `prof_u(F_1) = prof_u(F)`, and the relation (∗) is verified by hypothesis at the points of `U` not belonging to `E`; for the latter, it is also verified by the choice of `V`. Finally, if `u ∈ U` and `u ∉ V`, one has by 1.6 g) `prof_u(F_1) = ∞`. One then applies 4.4 (resp. 4.5) replacing `F` by `F_1`; one obtains the announced result, taking into account that one has, for every `i`:

```text
H^i_{f^{−1}(t)}(X, R ι_*(F|_V)) ≃ H^i_{f^{−1}(t) ∩ V}(V, F)  (resp. H^i(X, R ι_*(F|_V)) ≃ H^i(V, F)).
```

**Lemma 4.9.1.**
<!-- label: XIV.4.9.1 -->

A constructible set `E` contained in the set of closed points of a noetherian scheme `X`

<!-- original page 274 -->

is reduced to a finite number of points.

Indeed, `E` is a finite union of sets of the form `U ∩ ∁V`, where `U` and `V` are open sets of `X`; by hypothesis all the points of `U ∩ ∁V` are maximal points of this set, hence they are finite in number.

## 5. Geometrical depth

To apply 4.2 and its corollaries in practice, one needs a convenient criterion to verify the étale-depth hypotheses at the points of `U`. We shall give such a criterion, using the local Lefschetz theorem 4.5.

**5.1.** Let `A` be a noetherian local ring; when we speak of the étale depth of `A`, this will mean the depth at the closed point. We are going to introduce a notion of "geometrical depth of `A`", and use 4.5 to compare it to the étale depth `prof^ét(A)`.

**Proposition 5.2.**
<!-- label: XIV.5.2 -->

Let `A` be a noetherian local ring; suppose that `A` is isomorphic to a quotient of a regular local ring `B` by an ideal `I` (this is true, for example, when `A` is complete by virtue of the Cohen theorem (EGA 0_IV 19.8.8)). Let `q` be the minimal number of generators of `I`; then the number `dim(B) − q` is independent of the choice of `B`.

The minimal number of generators of `I` is also equal to the rank of the `k`-vector space `I ⊗_B k`, where `k` denotes the residue field of `A`. One reduces immediately to the case where `A` is complete, since one has `Â ≃ B̂/Î` with `dim B̂ = dim B` and `rg_k(I ⊗_B k) = rg_k(Î ⊗_{B̂} k)`; for the same reason one can suppose `B` complete.

<!-- original page 275 -->

Let `B` and `B′` be two complete regular local rings, `f : B → A`, `f′ : B′ → A` two surjective homomorphisms, and `I = Ker(f)`, `I′ = Ker(f′)`. One must show that

```text
dim B − rg_k(I ⊗_B k) = dim B′ − rg_k(I′ ⊗_{B′} k).
```

Let us first place ourselves in the case where one has a factorization of the form

```text
B --f--> A
 \      /
  g    f′
   \  /
    B′
```

with `g` surjective. Let `J = Ker(g)`; then `J ⊂ I` and `I/J = I′`. Since `B′` is regular, `dim(B′) = dim(B) − rg_k(J ⊗_B k)` and `J` is generated by elements forming part of a regular system of parameters of `B`. It follows that one has the exact sequence

```text
0 → J ⊗_B k → I ⊗_B k → J/I ⊗_{B′} k → 0,
```

and consequently

```text
dim B − rg_k(I ⊗_B k) = dim B − rg_k(J ⊗_B k) − rg_k(J/I ⊗_{B′} k) = dim B′ − rg_k(I′ ⊗_{B′} k).
```

The general case reduces to the preceding; to see this, it suffices to show that one can find a complete regular local ring `B′′` and surjective homomorphisms `g : B′′ → B` and `g′ : B′′ → B′`, rendering commutative the diagram

<!-- original page 276 -->

```text
                  B
                ↗    ↘ f
              g        \
(∗)      B′′            A
              g′       /
                ↘    ↗ f′
                  B′.
```

Now, if `W` is a Cohen ring with residue field `k`, one has a local morphism `W → A` that lifts to `B` and `B′` (EGA IV 19.8.6), so that one has the commutative diagram

```text
                  B
                ↗
               /
          W              A
               \
                ↘
                  B′.
```

One can find integers `n` and `n′` and surjective morphisms `h : W[[T_1, …, T_n]] → B` and `h′ : W[[T′_1, …, T′_{n′}]] → B′` that are morphisms of `W`-algebras (EGA 0_IV 19.8.8); if one then sets `B′′ = W[[T_1, …, T_n, T′_1, …, T′_{n′}]]` and if one defines `g` and `g′` as morphisms of `W`-algebras such that

```text
g(T_i) = h(T_i),  g(T′_i) = b_i,  g′(T_i) = b′_i,  g′(T′_i) = h′(T′_i),
```

where `b_i` (resp. `b′_i`) is an element of `B` (resp. of `B′`) lifting `(f′ ∘ h′)(T′_i)` (resp. `(f ∘ h)(T_i)`), the diagram (∗) is indeed commutative.

Proposition 5.2 justifies the following definition:

**Definition 5.3.**
<!-- label: XIV.5.3 -->

<!-- original page 277 -->

Let `A` be a noetherian local ring, `Â` its completion, which is therefore isomorphic to the quotient of a complete regular local ring `B` by an ideal `I`; if `q` is the minimal number of generators of `I`, one calls geometrical depth of `A` the number

```text
prof.géom(A) = dim B − q.
```

**Proposition 5.4.**
<!-- label: XIV.5.4 -->

Let `A` be a noetherian local ring. Then one has

```text
prof.géom(A) ⩽ dim A,
```

and one has equality if and only if `A` is a complete intersection.

One can suppose `A` complete. Let then `A = B/I`, where `B` is a complete regular local ring and `I` an ideal of `B`. If `(x_1, …, x_q)` is a minimal system of generators of `I`, one has `dim A ⩾ dim B − q`, and to say that `dim A = dim B − q` is equivalent to saying that `(x_1, …, x_q)` forms part of a system of parameters of `B` (EGA 0_IV 16.3.7); the proposition follows immediately.

**Proposition 5.5.**
<!-- label: XIV.5.5 -->

Let `A` and `A′` be noetherian local rings, `f : A → A′` a local homomorphism. Suppose that `f` is flat and that, denoting by `k` the residue field of `A`, `A′ ⊗_A k` is a field, a separable extension of `k`. Then one has

```text
prof.géom(A) = prof.géom(A′).
```

<!-- original page 278 -->

By replacing `A` and `A′` by their completions, one can suppose `A` and `A′` complete (it follows from (EGA 0_III 10.2.1) that the flatness hypothesis is preserved and this is evident for the other hypotheses). Let then `A = B/I`, where `B` is a regular local ring and `I` an ideal of `B`. Since `A′` is formally smooth over `A` (EGA 0_IV 19.8.2), it follows from (EGA 0_IV 19.7.2) that one can find a complete noetherian local ring `B′` and a local homomorphism `B → B′` such that `B′` is a flat `B`-module and `B′ ⊗_B A ≃ A′`. One therefore has `A′ ≃ B′/IB′`; moreover the ring `B′` is regular; indeed, if `𝔪` is the maximal ideal of `B`, `𝔪 B′` is the maximal ideal of `B′`, and since `𝔪` is generated by a regular sequence by definition of "regular", `𝔪 B′` is generated by a `B′`-regular sequence (EGA 0_IV 15.1.14). Since one evidently has `dim B = dim B′`, and since `I` and `IB′` have the same minimal number of generators, the assertion follows.

**Theorem 5.6.**[^N.D.E-XIV-6]
<!-- label: XIV.5.6 -->

Let `A` be an excellent local ring of characteristic zero. Then one has

```text
prof^ét(A) ⩾ prof.géom(A).
```

One can suppose `A` strictly local complete, since the geometrical depth and the étale depth are preserved by passage to the strict henselization and to the completion by 5.5 and 1.16. Let `A ≃ B/I`, where `B` is a complete regular local ring, and let `(f_1, …, f_q)` be a minimal system of generators of the ideal `I`. One therefore has

<!-- original page 279 -->

```text
π = prof.géom(A) = dim B − q.
```

Consider the closed immersion

```text
Y = Spec A → X = Spec B,
```

and let `U = X − Y = ⋃_{1 ⩽ i ⩽ q} X_{f_i}`. If `a` denotes the closed point of `X`, one must show that, for every prime number `p`, one has

```text
H^i_a(Y, ℤ/pℤ) = 0 for i < π.
```

Since `B` is regular excellent, one has `prof^ét(B) = 2 dim X` (cf. 1.10) and consequently `H^i_a(X, ℤ/pℤ) = 0` for `i < 2 dim X`. To prove the theorem, it therefore suffices to show that the morphism

```text
(∗) H^i_a(X, ℤ/pℤ) → H^i_a(Y, ℤ/pℤ)
```

is bijective for `i < π`. One applies for this the local Lefschetz theorem 4.5 with `n = π + q − 1`, `c = q − 1`, so `n − c = π`. Note that `U = X − Y` is the union of the `q` affine opens `X_{f_i}`. Let us show that one has, for every point `u` of `U`:

```text
prof^ét_u(X) ⩾ π + q − 1 − dim({u}) = dim O_{X,u}
```

(where `{u}` denotes the closure of `u` in `X − {a}`). Indeed it follows from 1.10 that one has

```text
prof^ét_u(X) = 2 dim O_{X,u} ⩾ dim O_{X,u}.
```

Using 4.5, one sees that (∗) is bijective for `i < π`, which completes the proof

<!-- original page 280 -->

of the theorem.

**Corollary 5.7.**
<!-- label: XIV.5.7 -->

Let `S` be the spectrum of a field of characteristic zero (resp. an excellent henselian local scheme of characteristic zero), `f : X → S` a scheme proper over `S` (resp. over `S − {s}`). Let `U` be a union of `c + 1` affine opens of `X`, `Y` a closed subscheme with underlying space `X − U`, `n` and `m` positive integers. Suppose that, for every point `u` of `U`, one has

```text
prof.géom(O_{X,u}) ⩾ n − dim({u})
```

(`{u}` closure of `u` in `X`). Then the canonical morphism

```text
H^i(X, ℤ/mℤ) → H^i(Y, ℤ/mℤ)
```

is bijective for `i < n − c − 1`, injective for `i = n − c − 1`.

One applies 4.5 and 4.6. The étale-depth hypotheses at the points of `U` are verified, since by 5.6

```text
prof^ét_u(X) ⩾ prof.géom(O_{X,u}) ⩾ n − dim({u}).
```

## 6. Open questions

**6.1.** One can ask whether the implication (ii) ⇒ (i) of 4.2 is valid more generally for torsion sheaves `F`, not necessarily annihilated by a given integer `m`

<!-- original page 281 -->

and not necessarily constructible. In the case where `S` is not of characteristic zero, it seems possible that this implication remains valid, even for `p`-torsion sheaves (`p` the residual characteristic). Finally it is not clear either that the hypothesis `S` excellent cannot be lifted.

**6.2.** Let `X` be a scheme proper over a field `k`, or the complement of the closed point of a henselian local scheme, and `j : Y → X` a closed subscheme of `X` whose complement `U` is affine. Then, if `F` is a sheaf of sets on `X` or a sheaf of not-necessarily-commutative groups, the statements 4.5 or 4.6 and 4.9 still have a meaning for such an `F`, provided one restricts to small values of `n`. If `u` is a point of `U`, one denotes by `ū` a geometric point above `u`, by `X_{(u)}` the strict localization of `X` at `ū`, and by `F_u` the fiber of `F` at `ū`. Then, by making possibly certain hypotheses on `X` and on `F`, for example by supposing `X` excellent (possibly of characteristic zero, or of equal characteristic by using resolution of singularities) and `F` ind-finite (or if needed even `L`-ind-finite with `L` prime to the characteristic of `X`), one would like to prove the following statements:

a) Let `F` be a sheaf of sets (resp. a sheaf of groups) and suppose that, for every point `u` of `U`, one has

```text
F_u → H⁰(X_{(u)} − ū, F)  injective if dim({u}) ⩽ 1
```

(that is, for such a `u`, one has `prof_u(F) ⩾ 1`). Then, when `V` runs over the set

<!-- original page 282 -->

of open neighborhoods of `Y`, the canonical morphism

```text
lim → _V H⁰(V, F) → H⁰(Y, j^* F)
```

is bijective (resp. one has the preceding conclusion and moreover the morphism `lim → _V H¹(V, F) → H¹(Y, j^* F)` is injective). If `F` is constructible, one can replace the `lim →` by the cohomology of `V` for `V` "small enough".

b) Let `F` be a sheaf of sets (resp. a sheaf of groups) and suppose that, for every point `u` of `U`, one has `prof_u(F) ⩾ 2 − dim({u})`, which translates also by the relations

```text
F_u → H⁰(X_{(u)} − ū, F) is bijective if dim({u}) = 0
F_u → H⁰(X_{(u)} − ū, F) is injective if dim({u}) = 1.
```

Then the canonical morphism

```text
H⁰(X, F) → H⁰(Y, j^* F)
```

is bijective (resp. one has the preceding conclusion and moreover the morphism `H¹(X, F) → H¹(Y, j^* F)` is injective).

c) Let `F` be an ind-finite sheaf of groups. Suppose that, for every point `u` of `U`, one has

```text
F_u → H⁰(X_{(u)} − ū, F) bijective if dim({u}) = 0 or 1,
F_u → H⁰(X_{(u)} − ū, F) injective if dim({u}) = 2.
```

Then, when `V` runs over the set of open neighborhoods of `Y`, the canonical

<!-- original page 283 -->

morphisms

```text
lim → _V H⁰(V, F) → H⁰(Y, j^* F)  and  lim → _V H¹(V, F) → H¹(Y, j^* F)
```

are bijective. If `F` is constructible, one can replace the `lim →` by the cohomology of `V` for `V` small enough.

d) Let `F` be a sheaf of groups. Suppose that, for every point `u` of `U`, one has `prof_u(F) ⩾ 3 − dim({u})`, which translates also by the conditions

```text
F_u → H⁰(X_{(u)} − ū, F) bijective, and H¹(X_{(u)} − ū, F) = 0 if dim({u}) = 0,
F_u → H⁰(X_{(u)} − ū, F) bijective if dim({u}) = 1,
F_u → H⁰(X_{(u)} − ū, F) injective if dim({u}) = 2.
```

Then the canonical morphisms

```text
H⁰(X, F) → H⁰(Y, j^* F)  and  H¹(X, F) → H¹(Y, j^* F)
```

are bijective.

As an indication in favor of these statements[^N.D.E-XIV-7], we mention XIII 2.1, X 3.4 and XII 3.5. Note that, thanks to the argument of 4.8 and 4.9, statement a) (resp. c)) would follow from b) (resp. d)).

**6.3.** From d) would follow the statement, analogous to 5.6: if `A` is a noetherian local ring (possibly excellent) and if `prof.géom(A) ⩾ 3`, then one has

<!-- original page 284 -->

`prof^{hop}(A) ⩾ 3`. To see this, one realizes `Y′ = Spec A` as a closed subset of a regular local scheme `X′ = Spec B`, whose complement is a union of `q` affine opens, with the relation `dim B − q = prof.géom(A)`. One has, for every point `x` of `X′`, if `n = dim B`, `prof^{hop}_x(X) ⩾ inf(3, n − dim({x}))` (cf. 1.11), and one deduces from d) that this entails `prof^{hop}_y(Y′) ⩾ inf(3, n − q − dim({y}))` for every point `y` of `Y′`. The result is obtained then by taking for `y` the closed point of `Y′`.

**6.4.** A variant of 4.2, at least of the implication (ii) ⇒ (i), should still be valid in the complex analytic case, provided one works with "analytically constructible" sheaves (cf. XIII); the proof would be analogous to that of 4.2, using the duality theory of J.-L. Verdier. Note, on the other hand, that for the complex analytic analogue of the non-commutative variants signalled in 6.2, one does not even have a method of attack for the statements concerning the fundamental group suggested by the results of Exposés X, XII, XIII recalled at the end of 6.2. The methods of the Séminaire indeed seem irremediably tied to the case of finite coverings (which can be studied in terms of coherent sheaves of algebras).

## Bibliography

1. M. Artin & B. Mazur — "Homotopy of Varieties in Etale Topology", in *Proceedings of a Conference on Local Fields*, Springer, 1967.
2. J.-P. Serre — *Cohomologie Galoisienne*, Springer-Verlag, 1964.
3. J.-L. Verdier — *Des catégories dérivées des catégories abéliennes*, with a preface by Luc Illusie, edited by Georges Maltsiniotis, Astérisque, vol. 239, Société mathématique de France, Paris, 1996.

## Footnotes

[^XIV-0-1]: After unpublished notes of A. Grothendieck.

[^XIV-1-1]: In accordance with the new terminology (cf. the re-edition of EGA I), we shall here call *scheme* what was previously called *prescheme* and *separated scheme* what was called *scheme*.

[^XIV-1-2]: I.e. a "principal homogeneous fiber bundle" in older terminology.

[^XIV-4-1]: At least in the case where `S` admits locally a dualizing complex, for example `S` locally immersible in a regular scheme.

[^N.D.E-XIV-1]: Editors' note: Gabber proved since — in 1994 — the absolute cohomological purity conjecture of Grothendieck: if `Y` is a closed subscheme of absolute noetherian schemes of pure codimension `c` and `n` an integer invertible on `X`, then `ℋ^q_Y(Λ)` is null if `q ≠ 2c` and equals `Λ_Y(−c)` (Tate twist) otherwise, where one has set `Λ = ℤ/nℤ`. See (Fujiwara K., "A Proof of the Absolute Purity Conjecture (after Gabber)", in *Algebraic geometry 2000, Azumino (Hotaka)*, Adv. Stud. in Pure Math., vol. 36, 2002, pp. 153-183). For applications to the existence of the dualizing complex, see (SGA 5, Lect. Notes in Math., vol. 589, Springer-Verlag, 1977, p. 1672), exposé 1 and loc. cit., §8. This conjecture had been proved in the case `n = ℓ^ν` with `ℓ` prime invertible on `X` sufficiently large by using `K`-theory crucially (Thomason R.W., "Absolute cohomological purity", Bull. Soc. Math. France 112 (1984), no. 3, p. 397-406). `K`-theory enters Gabber's proof via the Atiyah-Hirzebruch-Thomason spectral sequence relating étale cohomology and `K`-theory, a method already used in Thomason's approach. Besides this result, the other fundamental argument is the generalization of the Lefschetz theorem cited in note (5), page 181.

[^N.D.E-XIV-2]: Editors' note: recently, de Jong and Oort have obtained the following purity statement: let `S̃ → S` be a resolution of singularities of the spectrum `S` of a normal noetherian local ring of dimension 2 and let `U` be the complement of the closed point `s` in `S`. Suppose moreover that `k(s)` is algebraically closed. Then, for every prime number `p`, in particular if `S` is of characteristic `p`, the restriction morphism `H¹_ét(S̃, ℚ_p) → H¹_ét(U, ℚ_p)` is bijective (de Jong A.J. & Oort F, "Purity of the stratification by Newton polygons", J. Amer. Math. Soc. 13 (2000), no. 1, p. 209-241, theorem 3.2). If `k = ℂ` and `A` is the completion of a surface singularity, this result is due to Mumford (see page 158, [5]).

[^N.D.E-XIV-3]: Editors' note: the trivial torsor is successively denoted `0` or `1` in what follows; we have left this double notation, which, on reflection, brings no ambiguity.

[^N.D.E-XIV-4]: Editors' note: "rare" = "of empty interior", cf. Bourbaki TG IX.52.

[^N.D.E-XIV-5]: Editors' note: Gabber has proved the following generalization. Let `Y` be a strictly local scheme of arithmetic type over a regular noetherian scheme `S` of dimension `⩽ 1`. Let `f : X → Y` be an affine morphism of finite type, `Λ = ℤ/nℤ` with `n` invertible on `X` and `F` a `Λ`-sheaf. Then `H^q(X, F) = 0` if `q > δ(F)`. From this one deduces the following local Lefschetz theorem. Let `O` be strictly local of arithmetic type over `S`. For every `f ∈ O` not a zero divisor and every `Λ`-sheaf `F` on `Spec(O[f^{−1}])`, one has `H^q(Spec(O[f^{−1}]), F) = 0` for `q > dim(O)`. Cf. (Fujiwara K., "A Proof of the Absolute Purity Conjecture (after Gabber)", in *Algebraic geometry 2000, Azumino (Hotaka)*, Adv. Stud. in Pure Math., vol. 36, 2002, p. 153-183, §5) and especially the article of Illusie (Illusie L., "Perversité et variation", Manuscripta Math. 112 (2003), p. 271-295). This result is one of the crucial points used by Gabber in his proof of the Grothendieck purity theorem (cf. note (1), page 168).

[^N.D.E-XIV-6]: Editors' note: Illusie has since shown the inequality `prof_x(ℤ/ℓ^ν ℤ) ⩾ prof.géom_x(X/S) − δ(x) + 1` for `x` a point of `X` a scheme of finite type over a trait `S` of residual characteristic prime to `ℓ`, and `ν ⩾ 1`. If `S` is of characteristic zero, this is a consequence of theorem 5.6; see (Illusie L., "Perversité et variation", Manuscripta Math. 112 (2003), p. 271-295).

[^N.D.E-XIV-7]: Editors' note: all the statements of 6.2, apart from the constructible variants, have been proved by Mme Raynaud; see (Raynaud M., "Théorèmes de Lefschetz en cohomologie des faisceaux cohérents et en cohomologie étale. Application au groupe fondamental", Ann. Sci. Éc. Norm. Sup. (4) 7 (1974), p. 29-52, corollary III.1.3).

<!--
LEDGER DELTA (Exposé XIV):
| French | English | Note |
| ------ | ------- | ---- |
| schéma (Exp. XIV) | scheme | Modern usage = prescheme of Exp. I–XIII, per Raynaud's footnote. |
| schéma séparé (Exp. XIV) | separated scheme | Modern usage = scheme of Exp. I–XIII. |
| profondeur étale | étale depth | `prof_Y^ét(X)`, `prof_x^ét(X)`. |
| profondeur homotopique | homotopical depth | `prof_Y^{hopL}(X)`, `prof_x^{hopL}(X)`. |
| profondeur géométrique | geometrical depth | `prof.géom(A)`. |
| théorème de Lefschetz affine | affine Lefschetz theorem | 3.1; SGA 4 XIX 6.1 bis. |
| théorème de pureté cohomologique | cohomological purity theorem | 1.10 (semi-purity) and Gabber's absolute purity in N.D.E. |
| théorème de semi-pureté cohomologique | cohomological semi-purity theorem | 1.10. |
| théorème de pureté homotopique | homotopical purity theorem | 1.11. |
| théorème de Lefschetz local / global | local / global Lefschetz theorem | 4.5 / 4.6. |
| rare | rare | "Of empty interior" (Bourbaki TG IX.52); kept as a loanword per N.D.E.-XIV-4. |
| H^i_{Z!}(X/S, F) | H^i_{Z!}(X/S, F) | Cohomology with proper support, support in Z (4.0). |
| ΓY underlined | ℋ^p_Y / RΓ_Y (sheafified) | Convention pinned at 1.0. |
| ind-L-groupes | ind-`L`-groups | Per 1.18, 6.2. |
| 1-asphérique | 1-aspherical | Per 1.18 (SGA 4 XV 1.11). |
| n-acyclique | n-acyclic | Standard. |
| revêtement principal galoisien | Galois principal covering | 1.4 proof. |
| corps strictement local | strictly local field / strictly local ring | 3.2 and surrounding. |
-->
