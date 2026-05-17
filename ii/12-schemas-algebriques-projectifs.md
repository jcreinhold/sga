# Exposé XII. Applications to projective algebraic schemes

<!-- label: XII -->

<!-- original page 109 -->

## 1. Projective duality theorem and finiteness theorem

<!-- label: XII.1 -->

[^XII-1-star]

The following theorem, essentially contained in *FAC*[^XII-1-starstar] (except that at the time Serre did not yet have
at his disposal the language of `Ext` of sheaves of modules[^N.D.E-XII-1]), is the global analogue of the local duality
theorem (Exp. IV), which was modelled on it.

**Theorem.**

<!-- label: XII.1.1 -->

Let `k` be a field, `X = P^r_k` projective space of dimension `r` over `k`, and `F` a variable coherent module on `X`.
Then one has an isomorphism of `∂`-functors in `F`:

```text
Hⁱ(X, F)′ ⥲ Ext^{r−i}(X; F, Ωʳ_{X/k}),
```

<!-- label: eq:XII.1.1 -->

where one sets

```text
Ωʳ_{X/k} = O_{P^r_k}(−r − 1).
```

<!-- label: eq:XII.1.2 -->

**Remark.**

Of course, this module is also the module of relative differentials of degree `r` of `X` over `k`. In this form, the
theorem remains true if `X` is a proper and smooth scheme over `k` (for the projective case, see A. Grothendieck,
"Théorèmes de dualité pour les faisceaux algébriques cohérents", *Séminaire Bourbaki*, May 1957).[^XII-1-starstarstar]
When `F` is locally free, one recovers Serre's duality theorem

```text
Hⁱ(X, F)′ ⥲ H^{r−i}(Hom_{O_X}(F, Ωʳ_{X/k})).
```

Theorem 1.1 (which moreover recovers the case of `X` projective over `k`, as in *loc. cit.*) will suffice for our
purposes.

<!-- original page 110 -->

The homomorphism (1) is deduced from the Yoneda pairing

```text
Hⁱ(X, F) × Ext^{r−i}(X; F, Ωʳ_{X/k}) → Hʳ(X, Ωʳ_{X/k}),
```

<!-- label: eq:XII.1.3 -->

and from a well-known isomorphism (cf. *FAC*, or *EGA* III 2.1.12):

```text
Hʳ(X, Ωʳ_{X/k}) = Hʳ(P^r_k, O_{P^r_k}(−r − 1)) ⥲ k.
```

<!-- label: eq:XII.1.4 -->

To show that (1) is an isomorphism, one proceeds as in the case of the local duality theorem, noting that `Hʳ(X, F)`, as
a functor in `F`, is right exact (since `Hⁿ(X, F) = 0` for `n > r`), and that every coherent module is isomorphic to a
quotient of a direct sum of modules of the form `O(−m)` with `m` large. This reduces us, by descending induction on `i`,
to making the verification for a sheaf of the form `O(−m)`, where it is contained in the well-known explicit
computations (*FAC*, or *EGA* III 2.1.12). One may moreover assume `−m ⩽ −r − 1`, in which case `Hⁱ(X, O(−m)) = 0` for
`i ≠ r`.

**Corollary.**

<!-- label: XII.1.2 -->

For `F` coherent and given, and `m` large enough, one has a canonical isomorphism

```text
Hⁱ(X, F(−m))′ ⥲ H⁰(X, ℰxt^{r−i}_{O_X}(F, Ωʳ_{X/k})(m))
```

<!-- label: eq:XII.1.5 -->

(where `′` denotes the vector-space dual).

Indeed, on projective space `X`, for any pair of coherent sheaves `F`, `G` and for `n` large enough one has a canonical
isomorphism:

```text
Extⁿ(X; F(−m), G) ≅ Extⁿ(X; F, G(m)) ⥲ H⁰(X, ℰxtⁿ_{O_X}(F, G)(m)),
```

<!-- label: eq:XII.1.6 -->

(the isomorphism of the first two terms being trivially true for any `m`), as follows from the spectral sequence of
global `Ext`

```text
Hᵖ(X, ℰxt^q_{O_X}(F, G(m))) ⇒ Ext^•(X; F, G(m)),
```

<!-- original page 111 -->

which degenerates for `m` large thanks to the fact that

```text
ℰxt^q_{O_X}(F, G(m)) ≅ ℰxt^q_{O_X}(F, G)(m),
```

and that the `ℰxt^q_{O_X}(F, G)` are coherent sheaves. Hence (5) follows from (6) and (1).

**Corollary.**

<!-- label: XII.1.3 -->

For given `i, F`, the following conditions are equivalent:

1. `Hⁱ(X, F(−m)) = 0` for `m` large.
1. (i bis) `Hⁱ(X, F(·)) = ⨁_{m ∈ ℤ} Hⁱ(X, F(−m))` is a finitely generated `S`-module, where `S = k[t₀, …, t_r]`.
1. `ℰxt^{r−i}_{O_X}(F, Ωʳ_{X/k}) = 0`.
1. (ii bis) `ℰxt^{r−i}_{O_X}(F, O_X) = 0`.
1. `Hⁱ_x(F_x) = 0` for every closed point `x` of `X`.
1. `H^{i+1}_x(F̃_x) = 0` for every closed point `x` of the punctured projecting cone `X̃ = Spec(S) − Spec(k)` of `X`,
    where `F̃` denotes the inverse image of `F` under the canonical morphism `X̃ → X`.

*Proof.*

(i) ⇔ (i bis) since the submodule of `Hⁱ(X, F(·))` formed by the sum of the homogeneous components of degree `⩾ ν` is
finitely generated over `S` (in fact, for `i ≠ 0`, it is even finitely generated over `k`), cf. *FAC* or *EGA* III 2.2.1
and 2.3.2.

(i) ⇔ (ii) by virtue of Corollary 1.2.

(ii) ⇔ (ii bis) since `Ωʳ_{X/k}` is locally isomorphic to `O_X`.

(ii bis) ⇔ (iii) by virtue of the local duality theorem for `O_{X,x}` (which is a regular local ring of dimension `r`),
according to which the "dual" of `ℰxt^{r−i}_{O_X}(F, O_X)_x` is identified with `Hⁱ_x(F_x)` (V 2.1).

(ii bis) is equivalent to the analogous relation

```text
ℰxt^{r−i}_{O_{X̃}}(F̃, O_{X̃}) = 0
```

(thanks to the fact that `X̃ → X` is faithfully flat, so the inverse image of `ℰxt^{r−i}_{O_X}(F, O_X)` is isomorphic to
`ℰxt^{r−i}_{O_{X̃}}(F̃, O_{X̃})`), and this last relation is equivalent to (iv) by the local duality theorem for the
local ring `O_{X̃,x}`, which is regular of dimension `r + 1`.

In particular, applying this to all `i ⩽ n`, one finds:

**Corollary.**

<!-- label: XII.1.4 -->

Equivalent conditions for given `n, F`:

1. `Hⁱ(X, F(−m)) = 0` for `i ⩽ n` and `m` large.
1. (i bis) `Hⁱ(X, F(·))` is a finitely generated `S`-module for `i ⩽ n`.
1. `prof(F_x) > n` for every closed point `x` of `X`.
1. `prof(F̃_x) > n + 1` for every closed point `x` of `X̃`.

The interest of Corollaries 1.3 and 1.4 is to express a global condition (i) or (i bis) in terms of local conditions,
namely the vanishing of local invariants such as `Hⁱ_x(X, F_x)` or `Hⁱ_x(X̃, F̃_x)`, or an inequality on depth. In this
form, these results remain trivially valid for an arbitrary projective scheme `X` and a very ample invertible sheaf
`O_X(1)` on `X`, as one sees by inducing the latter using a suitable projective immersion `X → P^r_k`. (Of course,
conditions 1.3 (ii) and 1.3 (ii bis) are no longer equivalent to the others in this general case, except if one assumes
for example that `X` is regular.) One may moreover generalize to the case of a projective morphism `X → S` as follows:

**Proposition.**

<!-- label: XII.1.5 -->

<!-- original page 112 -->

Let `f: X → S` be a projective morphism with `S` noetherian, `O_X(1)` an invertible module on `X` very ample relatively
to `S`, `F` a coherent module on `X`, flat with respect to `S`, `s` an element of `S`, `X_s` the fiber of `X` at `s`
(considered as a projective scheme over `k(s)`), `F_s` the sheaf induced on `X_s` by `F`, finally `i` an integer.
Suppose that for every closed point `x` of `X_s`, one has `Hⁱ_x(F_{s,x}) = 0` (for example `prof(F_{s,x}) > i`). Then
there exists an open neighborhood `U` of `s` such that the same condition is verified for `s′ ∈ U`. Moreover, for such a
`U`, one has

```text
Rⁱf_∗(F(−m)) = 0 for m large,
```

and if `𝒮` is a graded quasi-coherent algebra on `S`, generated by `𝒮¹`, that defines `X` together with `O_X(1)` as
`X = Proj(𝒮)`, `O_X(1) = Proj(𝒮(1))`, then the `𝒮`-module

```text
Rⁱf_∗(F(·)) = ⨁_{m ∈ ℤ} Rⁱf_∗(F(m))
```

is finitely generated on `U`.

Embed `X` in some `X′ = P^r_S` so that `O_X(1)` is induced by `O_{X′}(1)` (which is possible, possibly by replacing `S`
by an affine neighborhood of `s`). Set[^XII-1-star2] for every integer `j` and every `t ∈ S`:

```text
Eʲ(t) = Ext^j_{O_{X′_t}}(F′_t, O_{X′_t}(−r − 1)).
```

<!-- label: eq:XII.1.7 -->

Thus `Eʲ(t)` is a coherent module on `X_t`. I claim that, for variable `t`, the family of these modules is
"constructible" in the following sense: for every `t ∈ S` there exists a non-empty open subset `V` of the closure of
`t`, which one endows with the induced reduced structure, and a coherent module `Eʲ(V)` on `X_V = X ×_S V`, flat
relatively to `V`, such that for every `t′ ∈ V`, `Eʲ(t′)` is isomorphic to the module induced by `Eʲ(V)` on `X_{t′}`. To
verify this assertion, setting `Z = {t}` with its induced structure, one considers the coherent modules

```text
Eʲ(Z) = Ext^j_{O_{X′_Z}}(F_Z, O_{X′_Z}(−r − 1))
```

(where the subscript `Z` means again that one induces over `Z`), and one takes for `V` a non-empty open subset of `Z`
such that the modules `Eʲ(Z)` are flat over `V`: this is possible since one checks immediately that `Eʲ(Z) = 0` for `j`
not lying in the interval `[0, r]`, and one may apply *SGA* 1 IV 6.11. One then takes `Eʲ(V) = Eʲ(Z)|X_V`, and one
verifies easily that it answers the question.

<!-- original page 113 -->

From the preceding remark it follows that there exists a finite partition of `S` formed by sets `V_α` of the form
`V = V(t)` as above (noetherian induction), and applying Serre's theorem *EGA* III 2.2.1 to the `Eʲ(V_α)`, one sees that
there exists an integer `m₀` such that

```text
Rⁱf_{V_α∗}(Eʲ(V_α)) = 0 for i ≠ 0, m ⩾ m₀, for all j,
```

whence it follows, using the flatness of `Eʲ(V_α)` with respect to `V_α` and easy Künneth-type relations (cf. *EGA* III,
§7), that

```text
Hⁱ(X_t, Eʲ(t)(m)) = 0 for i ≠ 0, m ⩾ m₀, for all j,
```

for every `t ∈ V_α`, hence for every `t` since the `V_α` cover `S`. From this and the spectral sequence of global `Ext`
follows, thanks to 1.1 and as in the proof of 1.2, an isomorphism

```text
Hⁱ(X_t, F_t(−m))′ ⥲ H⁰(X_t, E^{r−i}(t)(m)) for m ⩾ m₀,
```

<!-- label: eq:XII.1.8 -->

every integer `i`, and every `t ∈ S`.

Let us now use the hypothesis on `F_s`, which is written

```text
E^{r−i}(s) = 0,
```

<!-- label: eq:XII.1.9 -->

and which, thanks to (8), is equivalent to

```text
Hⁱ(X_s, F_s(−m)) = 0 for m ⩾ m₀.
```

<!-- label: eq:XII.1.10 -->

Since `F`, hence `F(−m)`, is flat with respect to `S`, it follows by the Künneth-type relations already invoked that
(for `m` given) the same relation (10) holds when `s` is replaced by a `t` near `s`, in particular for any generization
`t` of `s`. By virtue of (8), one will therefore have, for such a generization,

```text
E^{r−i}(t) = 0,
```

<!-- label: eq:XII.1.11 -->

now the set of `t ∈ S` for which this relation holds is plainly a constructible set (since it induces an open set on
each `V_α`); since it contains the generizations of `s`, it contains an open neighborhood `U` of `s`. This proves the
first assertion of 1.5. Moreover, for `t ∈ U`, one concludes from (11) and (8) that

```text
Hⁱ(X_t, F_t(−m)) = 0 for m ⩾ m₀, t ∈ U,
```

<!-- label: eq:XII.1.12 -->

which, by virtue of the Künneth-type relations, implies (in fact, is much stronger than)

```text
Rⁱf_∗(F(−m)) = 0 on U, for m ⩾ m₀.
```

<!-- label: eq:XII.1.13 -->

This proves the second assertion of 1.5. Finally the last assertion follows at once, by proceeding as at the start of
the proof of 1.3.

**Remark.**

<!-- label: XII.1.6 -->

[^XII-1-star3]

The proof simplifies notably (by eliminating any consideration of constructibility) when one assumes already that the
hypothesis made for `s ∈ S` is verified at every `s′ ∈ S`. In fact, when one makes the hypothesis that `F_s` is of depth
`> i` at the closed points of `X_s`, one has at one's disposal a general statement, local in nature on `X`, which says
that the same condition is verified for all `X_t`, on condition of replacing `X` by a suitable open neighborhood of the
fiber `X_s` (in other words, a certain part of `X`, defined by conditions on the modules induced by `F` on the fibers,
is open, cf. *EGA* IV). Since `f` is proper here, one may therefore take this neighborhood of the form `f⁻¹(U)`, which
recovers the first assertion of 1.5 without any tedious dévissage. In this general case, one may still prove by the
method of *loc. cit.* that the first assertion of 1.5 (proved here by global means, using that `X` is projective over
`S`) follows from a purely local statement on `X` (which the reader will spell out if he thinks it useful).

<!-- original page 114 -->

## 2. Lefschetz theory for a projective morphism: Grauert's comparison theorem

<!-- label: XII.2 -->

It is the following theorem:

**Theorem.**

<!-- label: XII.2.1 -->

Let `f: X → S` be a projective morphism with `S` noetherian, `O_X(1)` an invertible module on `X`, ample relatively to
`S`, `Y` the prescheme of zeros of a section `t` of `O_X(1)`, `𝒥` the ideal defining `Y`, `X_n` the subprescheme of `X`
defined by `𝒥^{n+1}`, `X̂` the formal completion of `X` along `Y`, `f̂: X̂ → S` the composite morphism `X̂ → X → S`, `F`
a coherent module on `X`, flat relatively to `S`. Suppose moreover that for every `s ∈ S`, the module `F_s` induced on
the fiber `X_s` is of depth `> n` at the points of that fiber, and that `t` is `F`-regular. Under these conditions:

1. The canonical homomorphism

    ```text
    Rⁱf_∗(F) → Rⁱf̂_∗(F̂)
    ```

    is an isomorphism for `i < n`, a monomorphism for `i = n`.

1. The canonical homomorphism

    ```text
    Rⁱf̂_∗(F̂) → lim_m Rⁱf_∗(F_m)
    ```

    is an isomorphism for `i ⩽ n`.

*Proof.*

One reduces at once to the case where `S` is affine, and to proving in this case the following:

**Corollary.**

<!-- label: XII.2.2 -->

Under the conditions of 2.1, suppose moreover that `S` is affine. Then:

1. The canonical homomorphism

    ```text
    Hⁱ(X, F) → Hⁱ(X̂, F̂)
    ```

    is an isomorphism for `i < n`, a monomorphism for `i = n`.

1. <!-- original page 115 -->

    The canonical homomorphism

    ```text
    Hⁱ(X̂, F̂) → lim_m Hⁱ(X_m, F_m)
    ```

    is an isomorphism for `i ⩽ n`.

Replacing `O_X(1)` by a tensor power, and `t` by a power of `t` if necessary, one may assume `O_X(1)` very ample
relatively to `S`. On the other hand, `t`, hence `tᵐ`, being `F`-regular, multiplication by `tᵐ`, considered as a
homomorphism from `F(−m)` to `F`, is injective; so one has for every `m ⩾ 0` an exact sequence:

```text
0 → F(−m) ──tᵐ──→ F → F_m → 0,
```

<!-- label: eq:XII.2.14 -->

whence a cohomology exact sequence

```text
Hⁱ(X, F(−m)) → Hⁱ(X, F) → Hⁱ(X, F_m) → H^{i+1}(X, F(−m)).
```

Now by virtue of 1.5 one has `Hⁱ(X, F(−m)) = 0` for `i ⩽ n` and `m` large enough, which proves the following:

**Lemma.**

<!-- label: XII.2.3 -->

For `m` large, the canonical homomorphism

```text
Hⁱ(X, F) → Hⁱ(X, F_m)
```

is bijective if `i < n`, injective if `i = n`.

This shows that for `i < n`, the projective system `(Hⁱ(X_m, F_m))_{m⩾0}` is essentially constant, *a fortiori*
satisfies the Mittag-Leffler condition; therefore (taking into account `F̂ = lim F_m`) one concludes (ii) by *EGA* 0_III
13.3. On the other hand, (i) follows trivially, taking into account 2.3.

**Corollary.**

<!-- label: XII.2.4 -->

[^N.D.E-XII-2]

Let `f: X → S` be a flat projective morphism with `S` locally noetherian, `O_X(1)` an invertible module on `X`, ample
relatively to `S`, `t` a section of this module that is `O_X`-regular, `Y` the subprescheme of zeros of `t`, `X̂` the
formal completion of `X` along `Y`. Suppose that for every `s ∈ S`, `X_s` is of depth `⩾ 1` (resp. of depth `⩾ 2`) at
its closed points. Then for every open neighborhood `U` of `Y`, the functor

```text
F ↦ F̂
```

from the category of locally free coherent modules on `U` to the category of locally free coherent modules on `X̂` is
faithful (resp. fully faithful, i.e. the Lefschetz condition (Lef) of X 2 is verified).

For two locally free modules `F` and `G` on `U` introduce the module

```text
H = Hom_{O_U}(F, G);
```

one is reduced to proving that the canonical homomorphism

```text
H⁰(U, H) → H⁰(Û, Ĥ)
```

<!-- label: eq:XII.2.15 -->

is injective (resp. bijective). Now the modules `H_t` are of depth `⩾ 1` (resp. `⩾ 2`) at the closed points of `X_t`;
one may therefore apply 2.1, which implies the conclusion of 2.4 in the case where `U = X`. In the case of an arbitrary
`U`, one notes that the question is local on `S`, so one may assume `S` affine. Then every coherent module on `X` is a
quotient of a locally free coherent module (since `O_X(1)` is a relatively ample invertible module on `X`). Since the
dual module `H′ = Hom(H, O_U)` extends to a coherent module on `X`, which is therefore isomorphic to a cokernel of a
homomorphism of locally free modules on `X`, it follows by transposition that one may find a homomorphism

```text
u′: L′⁰ → L′¹
```

<!-- original page 116 -->

of locally free modules on `X`, inducing a homomorphism

```text
u: L⁰ → L¹
```

of locally free modules on `U`, such that one has an exact sequence

```text
0 → H → L⁰ ──u──→ L¹.
```

Using the five lemma (which becomes the three lemma), and the left exactness of the functor `H⁰`, one is reduced to
proving that (15) is injective (resp. bijective) when `H` is replaced by `L⁰`, `L¹`, which reduces us to the case where
`H` is induced by a locally free module `H′` on `X`. Moreover, in the non-respective case this reduction is even
unnecessary, since the kernel of (15) is in any case formed of the sections of `H` on `U` that vanish in a suitable open
neighborhood `V` of `Y`; now the restriction homomorphism `H⁰(U, H) → H⁰(V, H)` is injective, since `H` is of depth
`⩾ 1` at the points of any closed subset `Z` of `X` not meeting `Y` (cf. the lemma below). In the respective case, one
is reduced to proving that

```text
H⁰(X, H′) → H⁰(U, H′)
```

is bijective, which follows from the fact that `H′` is of depth `⩾ 2` at every point of a closed subset `Z = X − U` of
`X` not meeting `Y`. One therefore needs only to prove the following:

**Lemma.**

<!-- label: XII.2.5 -->

Let `F` be a coherent module on `X`, flat with respect to `S`, such that for every `s ∈ S`, `F_s` is of depth `⩾ n` at
every closed point of `X_s`. Then for any closed subset `Z` of `X` not meeting `Y`, `F` is of depth `⩾ n` at every point
of `Z`.

Indeed, for every `x ∈ X`, setting `s = f(x)`, one has

```text
prof(F_x) ⩾ prof(F_{s,x}),
```

<!-- label: eq:XII.2.16 -->

<!-- original page 117 -->

as one sees by lifting in any way a maximal `F_{s,x}`-regular sequence of elements of `𝔯(O_{X_s,x})`, which yields an
`F_x`-regular sequence by virtue of *SGA* 1 IV 5.7. Now if `x` belongs to a `Z` as in Lemma 2.5, then `x` is necessarily
closed in `X_s`; in other words, `Z` is finite over `S`. Indeed `Z` (endowed with a structure induced by `X`) is
projective over `S` as a closed subprescheme of `X` which is so, and `Z` is affine over `S` as a closed subprescheme of
`X − Y`, which is so.

**Remark.**

<!-- label: XII.2.6 -->

Suppose that for every `s ∈ S` the section `t_s` of `O_{X_s}(1)` induced by `t` is `O_{X_s}`-regular (which implies, by
*SGA* 1 IV 5.7, that `t` is `O_X`-regular). Then the hypotheses made are stable under base extension `S′ → S` (`S′`
locally noetherian). Hence the conclusion remains valid after any base change.

## 3. Lefschetz theory for a projective morphism: existence theorem

<!-- label: XII.3 -->

**Theorem.**

<!-- label: XII.3.1 -->

[^N.D.E-XII-3]

Let `f: X → S` be a projective morphism, with `S` noetherian, `O_X(1)` an invertible module on `X` ample relatively to
`S`, `X₀` the subprescheme of zeros of a section `t` of `O_X(1)`, `X̂` the formal completion of `X` along `X₀`, `ℱ` a
coherent module on `X̂`, `ℱ₀` the module that it induces on `X₀`. Suppose moreover:

- a) `ℱ` is flat with respect to `S`.
- b) For every `s ∈ S`, the section `t_s` induced by `t` on `X_s` is `ℱ_s`-regular (which implies that `ℱ₀` is also flat
    with respect to `S`, cf. *SGA* 1 IV 5.7).
- c) For every `s ∈ S`, `ℱ_{0,s}` is of depth `⩾ 2` at the closed points of `X_{0,s}`.

Suppose moreover that `S` admits an ample invertible sheaf. Under these conditions, there exists a coherent module `F`
on `X` and an isomorphism of its formal completion `F̂` with `ℱ`.

This statement will follow from the following:

**Corollary.**

<!-- label: XII.3.2 -->

Under conditions a), b), c) above, one has the following:

1. <!-- original page 118 -->

    The module `f̂_∗(ℱ)` on `S` is coherent; hence for every `n`, the module `f̂_∗(ℱ(n))` on `S` is coherent.

1. For `n` large, the canonical homomorphism `f̂*f̂_∗(ℱ(n)) → ℱ(n)` is surjective.

Let us admit the corollary for the moment, and prove 3.1. Thanks to the last hypothesis made in 3.1, one may reduce to
the case where `X = P^r_S`, by replacing `O_X(1)`, `t` by a suitable power. I claim that one may moreover assume that
for every `s`, `t_s ≠ 0`. Otherwise, indeed, one has `ℱ_s = 0` by b), or what amounts to the same by Nakayama,
`ℱ_{0,s} = 0` i.e. `s` does not belong to the image of `Supp ℱ₀` by the morphism `f₀: X₀ → S` induced by `f`. Now this
image `S′` is open by virtue of a), b), since `ℱ₀` is flat with respect to `S`; and it is obvious that it suffices to
prove the conclusion of 3.1 in the situation obtained by restricting above `S′`, since the coherent module `F′` on
`X|S′` obtained will be the restriction of a coherent module `F` on `X`, which will answer the question. One may
therefore assume that, in addition to hypotheses a), b), c), the following hypotheses are also verified:

- a′) `O_X` is flat with respect to `S`.
- b′) For every `s ∈ S`, the section `t_s` is `O_{X_s}`-regular.
- c′) For every `s ∈ S`, `O_{X_{0,s}}` is of depth `⩾ 2` at the closed points of `X_{0,s}`.

(It suffices to choose `X = P^r_S` with `r ⩾ 3`, which is permissible.)

Now 3.2 implies that one may find an epimorphism

```text
L̂ → ℱ → 0,
```

<!-- label: eq:XII.3.17 -->

where `L` is a module on `X` of the form `f*(G)(−n)`, `G` being a locally free coherent module on `S`: for `n` large, it
suffices indeed to represent the coherent module `f̂_∗(ℱ)` on `S` as a quotient of such a `G`. On the other hand, the
hypotheses a), b), c) on `f`, `t` imply that `L̂` satisfies the same conditions a), b), c) as `ℱ`. One concludes easily
that the same holds for the kernel of (17), to which one may therefore apply the same argument; so that `ℱ` is
represented as a cokernel of a homomorphism

```text
L̂′ → L̂,
```

<!-- label: eq:XII.3.18 -->

where `L`, `L′` are locally free modules on `X`. Now by virtue of a′) and the second part of c′), and of 2.1 or 2.4 as
preferred, the homomorphism (18) comes from a homomorphism `L′ → L` of modules on `X`. It suffices now to take for `F`
the cokernel of `L′ → L`, and one wins.

It remains to prove 3.2. This had been done in the seminar by a somewhat tedious expedient, consisting in interpreting
everything in terms of cohomology on the punctured projecting cone of `X` relative to `S`, in order to reduce to Theorem
2.1. A more direct and more satisfactory way (although substantially the same) seems to me now the following. It
consists in noting that in IX, no. 2 (and with the notation of that exposé), the hypothesis that the morphism
`f: 𝒳 → 𝒳′` be adic does not intervene anywhere in the proof of 2.1, via *EGA* 0_III 13.7.7; it suffices to assume in
its place that `𝒳` is also adic, and to choose two ideals of definition `𝒥` for `𝒳′`, `ℐ` for `𝒳`, such that
`𝒥 O_𝒳 ⊂ ℐ`, and to define `𝒮 = gr_𝒥(O_{𝒳′})`, and to consider `gr_ℐ(ℱ)`. In any case, 2.1 may be applied directly to
the morphism `f̂: X̂ → S` considered in the present section, where one simply takes `𝒥 = 0`. Thus, to verify that
`f̂_∗(ℱ)` is coherent, it suffices, by virtue of *loc. cit.*, to verify that `Rⁱf₀_∗(gr_ℐ(ℱ))` is coherent on `S` for
`i = 0, 1`; for this one notes that by virtue of a) and b), the module considered is none other than
`⨁_{m⩾0} Rⁱf₀_∗(ℱ₀(−m))`, which is indeed coherent by virtue of hypothesis c) and of 1.5.

This proves 3.2 (i). For 3.2 (ii), we shall need the following:

**Lemma.**

<!-- label: XII.3.3 -->

<!-- original page 119 -->

Under conditions a), b), c) of 3.1, set

```text
G_m = f̂_∗(ℱ(·)_m) = ⨁_n f_∗(ℱ_m(n)).
```

Then the projective system `(G_m)` satisfies the Mittag-Leffler condition.

One may assume `S` affine, with ring `A`. Let `𝒮` then be a finitely generated graded `A`-algebra with positive degrees,
and `t′ ∈ 𝒮₁`, such that `X` immerses into `Proj(𝒮)`, `O_X(1)` being induced by `O(1)` and the section `t` being the
image of `t′`. Equip `𝒮` with the `𝒥`-adic filtration, where `𝒥 = t′𝒮`, and consider the projective system of the
`ℱ(·)_m` in the category of abelian sheaves on `X₀`. One is again under the preliminary conditions of *EGA* 0_III
13.7.7[^XII-3-star] and moreover `Hⁱ(X₀, gr(ℱ(·)))` is a finitely generated module on `gr_𝒥(𝒮)` for `i = 0, 1`. Indeed,
since `t′` is `ℱ`-regular, one sees at once that as a module on `(𝒮/t′𝒮)[T]` (of which `gr_𝒥(𝒮)` is a quotient), the
module under consideration is identified with `Hⁱ(X₀, ℱ₀(·)) ⊗_{𝒮/t′𝒮} (𝒮/t′𝒮)[T]`; now by virtue of 1.5,
`Hⁱ(X₀, ℱ₀(·))` is finitely generated on `𝒮`, hence on `𝒮/t′𝒮`, for `i = 0, 1`, which proves our assertion. Consequently
one is under the conditions for applying 0_III 13.7.7 with `n = 1`, which proves 3.3.

This point being acquired (and assuming `S` still affine, which is permissible for proving 3.2 (ii)) let `m₀` be such
that `m ⩾ m₀` implies `Im(G_m → G₀) = Im(G_{m₀} → G₀)`, so that both sides are also equal to
`Im(lim G_m → G₀) = Im(f̂_∗(ℱ(·)) → f_∗ℱ₀(·))`. Note now that for `n` large, `ℱ_{m₀}(n)` is generated by its sections;
hence `ℱ₀(n)` is generated by sections that lift to `ℱ_{m₀}`, and so (thanks to the choice of `m₀`) that lift to `ℱ`. So
the sections of `ℱ` generate `ℱ₀`, hence also `ℱ` thanks to Nakayama. This proves 3.2 (ii), hence 3.1.

**Corollary.**

<!-- label: XII.3.4 -->

Let `f: X → S` be a flat projective morphism with `S` locally noetherian, `O_X(1)` an invertible module on `X`, ample
relatively to `S`, `t` a section of this module such that for every `s ∈ S` the section `t_s` induced on the fiber `X_s`
is `O_{X_s}`-regular, `X₀` the subprescheme of zeros of `t`, `X̂` the formal completion of `X` along `X₀`. Suppose that
for every `s ∈ S`, `X_{0,s}` is of depth `⩾ 2` at its closed points (i.e. `X_s` is of depth `⩾ 3` at the closed points
of `X_{0,s}`), and `X_s` is of depth `⩾ 2` at its closed points. Under these conditions, the pair `(X, X₀)` satisfies
the effective Lefschetz condition (Leff) of paragraph 2 of Exposé X, i.e.:

1. <!-- original page 120 -->

    For every open neighborhood `U` of `X₀` in `X`, the functor

    ```text
    F ↦ F̂
    ```

    from the category of locally free coherent modules on `U` to the category of locally free coherent modules on `X̂` is
    fully faithful.

1. For every locally free coherent module `ℱ` on `X̂`, there exists an open neighborhood `U` of `X₀`, and a locally free
    coherent module `F` on `U` such that `F̂` is isomorphic to `ℱ`.

Indeed, a) has already been noted in 2.4 under weaker conditions. For b), one applies 3.1, which gives the conclusion,
at least if `S` is noetherian and admits an absolutely ample invertible module, in particular if `S` is affine. Indeed,
if `F` is a coherent module on `X` such that `F̂` is isomorphic to `ℱ` and hence locally free, it follows that `F` is
locally free on a neighborhood `U` of `X₀`, and `F|U` will satisfy the required condition. But let us now note that by
virtue of 2.5, for such an `F`, its image under the immersion `U → X` is coherent, and moreover is independent of the
chosen solution `(U, F)` (taking into account the fact that two solutions coincide in a neighborhood of `X₀`, by virtue
of a)). Precisely, one may find a coherent module `F` on `X` and an isomorphism `F̂ ⥲ ℱ` such that `F` is of depth `⩾ 2`
at every point of `X` that is closed in its fiber, and this determines `F` up to a unique isomorphism. Thanks to this
uniqueness property, the solutions of the problem found by inducing above the affine open subsets of `S` glue together,
yielding a coherent `F` on all of `X` and an isomorphism `F̂ ≅ ℱ`. Restricting `F` to the open subset `U` of points
where it is free, one finds what one was looking for.

Thanks to 2.4 and 3.4, one may exploit, in the situation of a projective algebraic scheme and a "hyperplane section"
thereof, the general facts established in Exposés X and XI concerning the conditions (Lef) and (Leff). Thus:

**Corollary.**

<!-- label: XII.3.5 -->

Let `X` be a projective algebraic scheme equipped with an ample invertible module `O_X(1)`, let `t` be a section of this
module that is `O_X`-regular, and let `X₀` be the subscheme of zeros of `t`. Suppose that `X` is of depth `⩾ 2` at its
closed points (resp. and of depth `⩾ 3` at the closed points of `X₀`). Then `π₀(X₀) → π₀(X)` is bijective, in particular
`X` is connected if and only if `X₀` is, and choosing a geometric base point in `X₀`, `π₁(X₀) → π₁(X)` is surjective,
and more generally for every open subset `U ⊃ X₀`, the homomorphism `π₁(X₀) → π₁(U)` is surjective (resp. the
homomorphism `π₁(X₀) → lim_U π₁(U)` is bijective). In the respective case, if one assumes moreover that the local ring
of every closed point of `X` not in `X₀` is pure (3.2) (for example is regular, or only a complete intersection), then
`π₁(X₀) → π₁(X)` is an isomorphism.

One applies 2.4 and 3.4. One will note that in the respective case the hypothesis that `X` be of depth `⩾ 3` at the
closed points of `X₀` implies that all the irreducible components of dimension `≠ 0` of `X` are of dimension `⩾ 3` (as
one sees by noting that any such component necessarily meets `X₀`, and looking at a closed point of the intersection).

**Remark.**

When `X` is normal, of dimension `⩾ 2` at all its points, it is of depth `⩾ 2` at its closed points and one is under the
non-respective conditions of 3.5. In this case, one has a more elementary proof of the surjectivity of `π₁(X₀) → π₁(X)`
using Bertini's theorem (cf. *SGA* 1 X.2.10). If one assumes moreover `X₀` normal, and `X` of dimension `⩾ 3` at all its
points, then one is under the respective conditions of 3.5. In this case, 3.5 was established by Grauert (indeed, thanks
to the normality hypothesis, one then succeeds in dispensing with the existence theorem 3.1 by certain expedients). It
is this proof of Grauert that was the starting point of the "Lefschetz theory" that is the subject of the present
seminar.

<!-- original page 121 -->

**Corollary.**

<!-- label: XII.3.6 -->

Let `X, O_X(1), t, X₀` be as in 3.5. Suppose that `X` is of depth `⩾ 2` at its closed points, and that

```text
Hⁱ(X₀, O_{X₀}(−n)) = 0
```

for `n > 0` and for `i = 1` (resp. for `i = 1` and for `i = 2`), which implies by virtue of 1.4 that `X₀` is of depth
`⩾ 2` (resp. `⩾ 3`) at its closed points, i.e. that `X` is of depth `⩾ 3` (resp. `⩾ 4`) at the closed points of `X₀`.
Under these conditions, for every open neighborhood `U` of `X₀`, `Pic(U) → Pic(X₀)` is injective, in particular
`Pic(X) → Pic(X₀)` is injective (resp. `lim_U Pic(U) → Pic(X₀)` is bijective). In the respective case, if one assumes
moreover that the local ring of `X` at every closed point not in `X₀` is parafactorial (3.1) (for example is regular, or
more generally a complete intersection), then `Pic(X) → Pic(X₀)` is bijective.

One applies XI 3.12 and 3.13, noting that the respective hypothesis implies that the irreducible components of dimension
`≠ 0` of `X` are of dimension `⩾ 4`. One finds in particular, by applying this to the case where `X` is a global
complete intersection of dimension `⩾ 4` in projective space:

**Corollary.**

<!-- label: XII.3.7 -->

Let `X` be an algebraic scheme of dimension `⩾ 3`, which is a complete intersection in a scheme `P^r_k`. Then `Pic(X)`
is the free group generated by the class of the sheaf `O_X(1)`.

One reasons by induction on the number of hypersurfaces of which `X` is the intersection, applying 3.6 and noting that
for a complete intersection `X` of dimension `⩾ 3`, one has `Hⁱ(X, O_X(n)) = 0` for `i = 1, 2` and every `n`.

**Remark.**

<!-- label: XII.3.8 -->

In the case where `X` is a non-singular hypersurface, 3.7 is due to Andreotti. The result 3.7 may also be expressed
(when `X` is non-singular) by saying that the homogeneous coordinate ring of `X` is factorial, and in this form is
contained in XI 3.13 (ii). Let us also point out that Serre had given a proof of 3.7 in the non-singular case, by
transcendental means, using a specialization argument to reduce to the case of characteristic 0, where one has the
Lefschetz theorem in its classical form. Of course, the fact that the purely algebraic proof given here makes it
possible to dispense with non-singularity hypotheses in the statement of Lefschetz's theorem invites one to reconsider
the latter also in the classical case. Cf. the following exposé, which proposes conjectures in this direction.

<!-- original page 122 -->

In Corollaries 3.5 and 3.7 we have placed ourselves over a base field, whereas the key theorems 2.4 and 3.4 are valid
over an arbitrary base. To generalize Corollaries 3.5 and 3.6 to a general `S`, we must give serviceable criteria for a
point of `X` (flat over `S`) to have a "pure" or, respectively, parafactorial local ring. This will be the object of the
following section.

## 4. Formal completion and normal flatness

<!-- label: XII.4 -->

**Theorem.**

<!-- label: XII.4.1 -->

Let `X` be a locally noetherian prescheme, locally immersible in a regular scheme, `Y` a closed part of `X`,
`U = X − Y`, `X₀` a closed subprescheme of `X` defined by an ideal `𝒥`, `X̂` the formal completion of `X` along `X₀`,
`U₀` the trace of `X₀` on `U`, `Û` the formal completion of `U` along `U₀`, `i: U → X` and `î: Û → X̂` the canonical
immersions, `n` an integer. Suppose:

- a) `X` is normally flat along `X₀` at the points of `Y ∩ X₀`, i.e. at these points the modules `𝒥ⁿ/𝒥^{n+1}` on `X₀`
    are flat, i.e. locally free.
- b) For every `x ∈ Y ∩ X₀`, one has `prof O_{X₀,x} ⩾ n + 2`.

Under these conditions, one has the following:

1. Let `F` be a coherent module on `U`; suppose that one has:

    - c) For every `x ∈ Y − Y ∩ X₀`, one has `prof O_{X,x} ⩾ n + 2`.
    - d) `F` is free at the points of `U₀`, and of depth `⩾ n + 1` at every point of `U` where it is not free.

    Then the graded module

    ```text
    ⨁_{m⩾0} Rᵖi_∗(𝒥ᵐF)
    ```

    on `⨁_{m⩾0} 𝒥ᵐ` is finitely generated for `p ⩽ n`.

1. Let `F` be a coherent module on `Û`. Then the graded module

    ```text
    ⨁_{m⩾0} Rᵖi_∗(𝒥ᵐF/𝒥^{m+1}F)
    ```

    on `⨁_{m⩾0} 𝒥ᵐ/𝒥^{m+1} = gr_𝒥(O_X)` is finitely generated for `p ⩽ n`.

*Proof.*

(1) Let `X′ = Spec(⨁_{m⩾0} 𝒥ᵐ)`; the base change `f: X′ → X` then defines `U′ = X′ − Y′`, `X′₀`, `U′₀ = X′₀ ∩ U′`, and
immersions `i′: U′ → X′`, `i′₀: U′₀ → X′₀`. One has therefore a cartesian square

```text
       i′
X′ ←──── U′
│         │
f│         │g
↓    i    ↓
X ←────── U
```

and one has

```text
⨁_{m⩾0} Rᵖi_∗(𝒥ᵐF) = Rᵖi_∗(⨁_{m⩾0} 𝒥ᵐF) = Rᵖi_∗(g_∗(F′)),
```

<!-- label: eq:XII.4.19 -->

<!-- original page 123 -->

where `F′ = g*F`, so that one has indeed a canonical isomorphism

```text
g_∗(F′) ⥲ ⨁_{m⩾0} 𝒥ᵐF,
```

since this is true at the points of `U₀`, due to the fact that `F` is free there by virtue of d), and also at the points
outside `U₀`, due to the fact that there one has `𝒥ᵐ = O_U` (so that in both cases, `𝒥ᵐ ⊗_{O_U} F → 𝒥ᵐF` is an
isomorphism).

On the other hand, since `f` and consequently `g` are affine, one has

```text
Rᵖi_∗(g_∗(F′)) = Rᵖ(ig)_∗(F′) = Rᵖ(fi′)_∗(F′) = f_∗(Rᵖi′_∗(F′)),
```

<!-- label: eq:XII.4.20 -->

so comparing (19) and (20), one sees that assertion (1) is equivalent to the following: `Rᵖi′_∗(F′)` is a finitely
generated module, i.e. coherent on `X′`, for every `p ⩽ n`. Now since `X` is locally immersible in a regular scheme, the
same holds of `X′`, which is of finite type over `X`, and one may apply the coherence criterion VIII 2.3 to a coherent
extension `F″` of `F′`: one wants to express that `Hᵖ_{Y′}(F″)` is coherent for `p ⩽ n + 1`, and this is also equivalent
to saying that for every `x′ ∈ U′` such that

```text
codim({x′} ∩ Y′, {x′}) = 1,
```

<!-- label: eq:XII.4.20bis -->

one has

```text
prof F′_{x′} ⩾ n + 1.
```

<!-- label: eq:XII.4.21 -->

Now this condition is verified at the points `x′` where `F′` is not free, since for such an `x′` one has `x′ ∉ U′₀` by
virtue of d), so `g` is an isomorphism there, and by virtue of d) again, `F` is of depth `⩾ n + 1` at `g(x′)`, so `F′`
is of depth `⩾ n + 1` at `x′`. It therefore suffices to verify condition (21) at the `x′ ∈ U′` satisfying (20 bis) and
at which `F′` is free. For this, it suffices to prove that one has

```text
prof O_{X′,x′} ⩾ n + 1
```

<!-- label: eq:XII.4.21bis -->

at these points, *a fortiori* it suffices to establish that one has this relation at all points `x′` of `U′` satisfying
(20 bis). Now, again by virtue of criterion 2.3 of Exposé VIII, this is equivalent to the assertion that the modules

```text
Hᵖ_{Y′}(O_{X′}) for p ⩽ n + 1
```

are coherent. In fact, we are going to prove that they are even zero, or what amounts to the same by virtue of Exposé
III, that one has

```text
prof O_{X′,x′} ⩾ n + 2 for every x′ ∈ Y′.
```

<!-- label: eq:XII.4.22 -->

<!-- original page 124 -->

For this, we distinguish two cases. If `x′ ∉ X′₀`, then `f` is an immersion at `x′`, and it is necessary to verify that
`F` is of depth `⩾ n + 2` at the image `x = f(x′)`, which is none other than condition c). If on the contrary
`x′ ∈ X′₀`, i.e. `x = f(x′) ∈ X₀` so `x ∈ Y ∩ X₀`, one applies conditions a) and b) thanks to the following:

**Lemma.**

<!-- label: XII.4.2 -->

Let `X` be a locally noetherian prescheme, `X₀` a closed subprescheme of `X` defined by an ideal `𝒥`,
`X′ = Spec(⨁_{m⩾0} 𝒥ᵐ)`, `X′₀ = Spec(⨁_{m⩾0} 𝒥ᵐ/𝒥^{m+1}) = X′ ×_X X₀`, `x` a point of `X₀` at which `X` is normally flat
along `X₀`, i.e. such that `gr_𝒥(O_X) = ⨁_{m⩾0} 𝒥ᵐ/𝒥^{m+1}` is flat there as a module on `X₀`. Then for any sequence of
elements `f_i (1 ⩽ i ⩽ m)` of `O_{X,x}` whose images in `O_{X₀,x}` form an `O_{X₀,x}`-regular sequence, and for every
`x′ ∈ X′` above `x`, the images of the `f_i` in `O_{X′,x′}` (resp. in `O_{X′₀,x′}`) form respectively an
`O_{X′,x′}`-regular sequence (resp. an `O_{X′₀,x′}`-regular sequence); in particular one has

```text
prof O_{X′,x′} ⩾ prof O_{X₀,x},  prof O_{X′₀,x′} ⩾ prof O_{X₀,x}.
```

<!-- label: eq:XII.4.23 -->

To prove this, one may assume that `X` is local with closed point `x`, hence affine of ring `A = O_{X,x}`, `𝒥` being
defined by an ideal `J`; and it suffices to prove that for any sequence `f_i (1 ⩽ i ⩽ m)` of elements of `A` whose
images in `A/J` form an `A/J`-regular sequence, the `f_i` form an `(⨁_{m⩾0} Jᵐ)`-regular sequence and an
`(⨁_{m⩾0} Jᵐ/Jᵐ⁺¹)`-regular sequence, i.e. for every `m`, they form a `Jᵐ`-regular sequence and a `Jᵐ/Jᵐ⁺¹`-regular
sequence. The second assertion is trivial, since `Jᵐ/Jᵐ⁺¹` is a free module on `A/J`. The first follows by looking at
the `J`-adic filtration of `Jᵐ` and noting that, for the graded module associated with `Jᵐ` for this filtration, the
sequence of the `f_i` is regular.

This proves 4.2 and consequently 4.1, (1).

Let us prove 4.1, (2). For this, let us use the cartesian square

```text
        i′₀
X′₀ ←────── U′₀
│            │
f₀│            │g₀
↓     i₀     ↓
X₀ ←──────── U₀
```

and proceeding as at the beginning of the proof of (1), one finds that

```text
⨁_{m⩾0} Rᵖi_∗(𝒥ᵐF/𝒥^{m+1}F) ≅ f₀_∗(Rᵖi′₀_∗(F′₀)),
```

<!-- label: eq:XII.4.24 -->

where `F₀ = F/𝒥F` and `F′₀ = g₀*(F₀)` (using the fact that `F` is locally free). Hence the conclusion of (2) amounts to
saying that for `p ⩽ n`, `Rᵖi′₀_∗(F′₀)` is a coherent module.

Here again, taking into account that `F′₀` is locally free, criterion VIII 2.3 lets us reduce to proving that this is so
when one replaces `F′₀` by `O_{U′₀}`, i.e. to proving that the modules

```text
Hᵖ_{Y′₀}(O_{X′₀}) for p ⩽ n + 1  (where Y′₀ = Y′ ∩ X′₀ = X′₀ − U′₀)
```

<!-- original page 125 -->

are coherent. One proves again that they are in fact zero, i.e. that one has

```text
prof O_{X′₀,x′} ⩾ n + 2 for every x′ ∈ Y′₀.
```

<!-- label: eq:XII.4.25 -->

Now this indeed follows from conditions a) and b), taking into account 4.2. This completes the proof of 4.1.

**Remark.**

<!-- label: XII.4.3 -->

One sees at once, by descent, that the hypothesis: `X` locally immersible in a regular scheme, may be replaced by the
following weaker one: there exists a morphism `X̄ → X`, faithfully flat and quasi-compact, such that `X̄` is locally
immersible in a regular scheme.

Theorem 4.1 puts us in a position to apply the results of Exposé IX (comparison and existence theorems). We shall be
particularly interested in the following:

**Corollary.**

<!-- label: XII.4.4 -->

Suppose conditions a), b), c) of Theorem 4.1 verified, with `n = 1`, and `X = Spec(A)`, `A` being separated and complete
for the `𝒥`-adic topology. Then:

1. The functor `F ↦ F̂` from the category of locally free coherent modules on `U` to the category of locally free
    coherent modules on `Û` is fully faithful.
1. For every locally free coherent module `ℱ` on `Û`, there exists a coherent module `F` on `U` and an isomorphism
    `F̂ ⥲ ℱ`.

In particular, if for every `x ∈ U` whose closure in `U` does not meet `U₀`, i.e. such that `{x} ∩ X₀ ⊂ Y`, one has
`prof O_{U,x} ⩾ 2`, then the pair `(U, U₀)` satisfies the effective Lefschetz condition (Leff) of Exposé X.

(For the last assertion, one proceeds as in X 2.1.)

A particular case of 4.4:

**Corollary.**

<!-- label: XII.4.5 -->

Let `A` be a noetherian ring, `J` an ideal of `A` contained in the radical, `A₀ = A/J`. Suppose

1. `prof A₀ ⩾ 3`.
1. `gr_J(A)` is a free `A₀`-module.
1. `A` is complete for the `J`-adic topology.

Let `X = Spec(A)`, `X₀ = Spec(A₀) = V(J)`, `a` the closed point of `X`, `U = X − {a}`, `U₀ = X₀ − {a}`, `Û` the formal
completion of `U` along `U₀`. Then the functor `F ↦ F̂` from the category of locally free coherent modules on `U` to the
category of locally free coherent modules on `Û` is fully faithful. Moreover, for every locally free coherent module `ℱ`
on `Û`, there exists a coherent module (not necessarily locally free!) `F` on `U`, and an isomorphism `F̂ ≅ ℱ`.

One will note that thanks to 4.3, we did not have to suppose that `A` is a quotient of a regular ring, since the
completion of `A` for the `𝔯(A)`-adic topology satisfies this condition in any case.

Proceeding as in Exposés X and XI, one concludes from 4.5:

**Corollary.**

<!-- label: XII.4.6 -->

Under the conditions of 4.5, one has the following:

- a) `U` and `U₀` are connected (III 3.1).

    Choosing a geometric base point in `U₀`, the homomorphism

    ```text
    π₁(U₀) → π₁(U)
    ```

    is surjective.

- b) The homomorphism

    ```text
    Pic(U) → Pic(U₀)
    ```

    is injective.

<!-- original page 126 -->

To prove b), taking 4.5 into account, this amounts to verifying that any isomorphism `L′₀ ⥲ L₀` lifts to an isomorphism
`L̂′ ⥲ L̂`. Now for this one lifts step by step to isomorphisms `L′_n ⥲ L_n`; the obstructions lie in
`H¹(U₀, 𝒥ⁿ/𝒥^{n+1})`, and these modules are zero because `Jⁿ/Jⁿ⁺¹` is free and `prof A₀ ⩾ 3`.

We are now in a position to prove the following:

**Theorem.**

<!-- label: XII.4.7 -->

Let `A` be a noetherian local ring, `J` an ideal of `A` contained in its radical, `A₀ = A/J`. Suppose

1. `prof A₀ ⩾ 3`.
1. `gr_J(A)` is a free module on `A₀`.

Then, if `A₀` is "pure" (X 3.1) (resp. parafactorial (XI 3.1)), so is `A`.

*Proof.*

By descent, one may assume that one also has

1. `A` is complete for the `J`-adic topology.

Indeed, by virtue of (i) and (ii), one has `prof(A) ⩾ 3`, hence `prof(Â) ⩾ 3`, where `Â` is the completion of `A` for
the `J`-adic topology, and one applies X 3.6 and XI 3.6. One is therefore under the conditions of 4.5. Since
`prof(A) ⩾ 3 ⩾ 2`, to say that `A` is parafactorial means simply that `Pic(U) = 0`, and by virtue of 4.6 b) it suffices
for this that `Pic(U₀) = 0`, i.e. that `A₀` be parafactorial. To prove that `A` is "pure" if `A₀` is, one needs to prove
that if `V` is an étale cover of `U`, defined by an algebra `B` on `U`, then `H⁰(U, B)` is a finite étale algebra over
`A`. Now `A₀` being pure, the same holds of the `A_n` (which differ from it only by nilpotent elements), so for every
`n`, `B_n = H⁰(U, B_n)` is an étale algebra over `A/J^{n+1}`, and these algebras of course glue, so that `lim B_n` is an
étale algebra over `A`. Now by virtue of 4.5, this algebra is none other than `H⁰(U, B)`, which establishes our
assertion.

**Corollary.**

<!-- label: XII.4.8 -->

Let `f: X → Y` be a flat morphism of locally noetherian preschemes, `x ∈ X`, `y = f(x)`; suppose that `O_{X_y,x}` is a
"pure" (resp. parafactorial) local ring of depth `⩾ 3`. Then the same holds for `O_{X,x}`.

This is the result of the type promised at the end of the preceding section, in order to generalize Corollaries 3.5 and
following. One thus finds, using 3.4, the following:

**Corollary.**

<!-- label: XII.4.9 -->

<!-- original page 127 -->

Let `f: X → S` be a flat projective morphism with `S` locally noetherian, `O_X(1)` an invertible module on `X` ample
with respect to `S`, `t` a section of `O_X(1)` such that for every `s ∈ S` the section `t_s` induced on `X_s` is
`O_{X_s}`-regular, `X₀` the subscheme of zeros of `t`, `X_m` the subscheme of zeros of `t^{m+1}`. Suppose that for every
`s ∈ S`, `X_s` is of depth `⩾ 3` at all its closed points. Then:

- a) If the local rings of the closed points of `X_s − X_{0,s}` (`s ∈ S`) are "pure", for example are complete
    intersections, then the functor `X′ ↦ X′₀ = X′ ×_X X₀` from the category of étale covers of `X` to the category of
    étale covers of `X₀` is an equivalence of categories; in particular, choosing a geometric base point in `X₀`, the
    homomorphism

    ```text
    π₁(X₀) → π₁(X)
    ```

    is an isomorphism.[^N.D.E-XII-4]

- b) If the local rings of the closed points of `X_s − X_{0,s}` (`s ∈ S`) are "parafactorial", for example regular, or
    complete intersections of dimension `⩾ 4`, then for every integer `m` such that `Rⁱf₀_∗(O_{X₀}(−n)) = 0` for `n > m`
    and `i = 1, 2`, the map `Pic(X) → Pic(X_m)` is bijective.

Moreover, if `S` is noetherian and the `X_{0,s}` are of depth `⩾ 3` at their closed points, there exist such `m` (cf.
1.5).

**Remark.**

<!-- label: XII.4.10 -->

Under the conditions of the last assertion of 4.9 b), one has seen in 1.5 that there exists an `m` such that `n > m`
implies even `Hⁱ(X₀, O_{X₀}(−n)) = 0` for `i = 1, 2` (and even for `i ⩽ 2`). This condition is stronger than
`Rⁱf_∗(O_{X₀}(−n)) = 0` for `i = 1, 2`, and it has moreover the advantage of being stable under base change. The same
holds of the depth hypotheses made in 4.9, and also of a hypothesis of the type "the `X_s` are locally complete
intersections". It then follows, under these conditions, that 4.9 b) also implies that the functor morphism

```text
Pic_{X/S} → Pic_{X_n/S}
```

in `Sch/S` is an isomorphism, hence also the morphism for the relative Picard schemes, when these exist:

```text
Pic_{X/S} → Pic_{X_n/S}.
```

Even in the case where `S` is the spectrum of an algebraically closed field, this statement is markedly more precise
than the statement saying merely that `Pic(X) → Pic(X_n)` is bijective.

<!-- original page 128 -->

One may ask whether one can always take `n = 0` in the preceding conclusions (assuming therefore the `X_{0,s}` of depth
`⩾ 3` at their closed points). When `X₀` is smooth over `S` and the residue characteristics of `S` are zero, this is
indeed so, by virtue of Kodaira's "vanishing theorem" (proved by transcendental means, using a Kählerian metric) which
implies that for every smooth connected projective scheme of dimension `n` over a field `k` of characteristic zero, and
every ample invertible module `L` on `X`, one has `Hⁱ(X, L⁻¹) = 0` for `i ≠ n`. It is not known[^N.D.E-XII-5] at present
whether this theorem may be replaced by a generalization in characteristic `p > 0`, and whether the smoothness
hypothesis may be replaced by a hypothesis of a more general nature (bearing on depth, or of "complete intersection"
type ...).

## 5. Universal finiteness conditions for a non-proper morphism

<!-- label: XII.5 -->

Let us recall for the record the following:

**Proposition.**

<!-- label: XII.5.1 -->

Let `f: X → S` be a proper morphism of preschemes with `S` locally noetherian, `U` an open part of `X`, `g: U → X` the
canonical immersion, `h = fg: U → S`, `F` a module on `U`. Suppose that the modules `Rⁱg_∗(F)` are coherent for `i ⩽ n`
(a hypothesis of local nature on `X`, which is verified in practice using criterion VIII 2.3). Then `Rⁱh_∗(F)` is
coherent for `i ⩽ n`.

This follows at once from the Leray spectral sequence

```text
E₂^{p,q} = Rᵖf_∗(R^qg_∗(F)) ⇒ R^∗h_∗(F),
```

<!-- label: eq:XII.5.26 -->

and from the fact that the higher direct images by `f` of a coherent module on `X` are coherent (*EGA* III 3.2.1).

**Proposition.**

<!-- label: XII.5.2 -->

<!-- original page 129 -->

Let `S` be a locally noetherian prescheme, `𝒮` a quasi-coherent graded algebra of finite type on `S`, generated by `𝒮₁`,
`X` a subprescheme of `Proj(𝒮)`, `O_X(1)` the invertible module on `X` very ample relatively to `S` induced by
`Proj(𝒮(1))`, `U` an open part of `X`, `g: U → X` the canonical immersion, `h = fg: U → S`, `F` a quasi-coherent module
on `U`, whence twisted modules `F(m) = F ⊗ O_X(m)` (`m ∈ ℤ`), `n` an integer, `m₀` an integer. The following conditions
are equivalent:

1. `Rⁱg_∗(F)` is coherent for `i ⩽ n`.
1. `⨁_{m>m₀} Rⁱh_∗(F(m))` is a finitely generated `𝒮`-module for `i ⩽ n`.

*Proof.*

Replacing `F` by `F(m)` in the spectral sequence above one finds a spectral sequence of graded `𝒮`-modules

```text
E₂^{p,q} = ⨁_{m⩾m₀} Rᵖf_∗(R^qg_∗(F(m))) ⇒ ⨁_{m⩾m₀} R^∗h_∗(F(m)).
```

Since one has

```text
R^qg_∗(F(m)) ≅ R^qg_∗(F)(m),
```

one sees that if the `Rⁱg_∗(F)` are coherent, `E₂^{p,q}` is finitely generated on `𝒮` for `q ⩽ n`, thanks to part a) of
Lemma 5.3 below, which implies that the abutment is finitely generated on `𝒮` in degree `i ⩽ n`. This proves (i) ⇒ (ii).
Moreover, reasoning in the abelian category of graded `𝒮`-modules modulo the thick subcategory `C` of those that are
quasi-coherent of finite type, one finds by the preceding spectral sequence

```text
⨁_{m⩾m₀} R^{n+1}h_∗(F(m)) ≅ ⨁_{m⩾m₀} f_∗(R^{n+1}g_∗(F)(m)) mod C,
```

which proves that if the left-hand side is a finitely generated `𝒮`-module, then `R^{n+1}g_∗(F)` is coherent, by virtue
of part b) of Lemma 5.3. This proves the implication (ii) ⇒ (i) by induction on `n`. It remains to prove:

**Lemma.**

<!-- label: XII.5.3 -->

Let `S`, `𝒮`, `X`, `f` be as in 5.2, and `G` a quasi-coherent module on `X`, `m₀` an integer. Then:

- a) If `G` is coherent, then for every integer `i`, the graded module

    ```text
    ⨁_{m⩾m₀} Rⁱf_∗(G(m))
    ```

    on `𝒮` is finitely generated.

- b) Conversely, suppose that the module `⨁_{m⩾m₀} Rⁱf_∗(G(m))` on `𝒮` is finitely generated; then `G` is coherent.

*Proof of 5.3.*

For a), the case `i = 0` is given in *EGA* III 2.3.2; the case `i > 0` follows from *EGA* III 2.2.1 (i)(ii), which says
that the `Rⁱf_∗ G(m)` are coherent, and zero for `m` large (if one assumes `S` noetherian, which is permissible).

<!-- original page 130 -->

For b), one notes that `G` is isomorphic to `Proj(⨁_{m⩾m₀} f_∗(G(m)))` (*EGA* II 3.4.4 and 3.4.2), which proves that `G`
is coherent if `⨁_{m⩾m₀} f_∗(G(m))` is finitely generated on `𝒮`, by virtue of *loc. cit.* 3.4.4.

**Corollary.**

<!-- label: XII.5.4 -->

(`S` noetherian.) Suppose that `Rⁱg_∗(F)` is coherent for `i ⩽ n`; then for `i ⩽ n + 1` and `m` large, one has a
canonical isomorphism:

```text
Rⁱh_∗(F(m)) ≅ f_∗(Rⁱg_∗(F)(m)).
```

Indeed the spectral sequence (26) for `F(m)` then degenerates in degree `⩽ n`, by *EGA* III 2.2.1 (ii), whence at once
the result (which moreover recovers the implication (ii) ⇒ (i) of 5.2).

**Corollary.**

<!-- label: XII.5.5 -->

Under the preliminary conditions of 5.2, `S` noetherian, the following conditions are equivalent:

1. `⨁_{m⩾m₀} h_∗(F(m))` is finitely generated on `𝒮`, and `Rⁱh_∗(F(m)) = 0` for `0 < i ⩽ n` and `m` large.
1. `g_∗(F)` is coherent, and `Rⁱg_∗(F) = 0` for `0 < i ⩽ n`.
1. (ii bis) `g_∗(F)` is coherent, and `prof_Y g_∗(F) > n + 1`.

The equivalence of (ii) and (ii bis) is contained in III 3.3. Moreover, by virtue of 5.2 conditions (i) and (ii) both
imply that the `Rⁱg_∗(F)` (`i ⩽ n`) are coherent. The equivalence of (i) and (ii) then follows from 5.4, taking into
account the fact that for a coherent module `G` on `X`, one has `G = 0` if and only if `f_∗(G(m)) = 0` for `m` large,
for instance by virtue of *EGA* III 2.2.1 (iii).

**Remark.**

<!-- label: XII.5.6 -->

One may interpret criteria 5.2 and 5.5 by saying that the "simultaneous finiteness condition" 5.2 (ii) is expressed by
properties of local regularity (in terms of depth, thanks to VIII 2.1) of `F` at the points of `U` neighboring
`Y = X − U`, whereas the "asymptotic vanishing condition" 5.5 (i) is of a markedly stronger nature, and is expressed by
conditions of local regularity of `g_∗(F)` at the points of `Y` itself. It would be interesting, in order to generalize
the Lefschetz-type theorems for projective morphisms to quasi-projective morphisms, to find local criteria on `X`
necessary and sufficient for the `𝒮`-modules `⨁_{m⩾0} Rⁱh_∗(F(m))` for `i ⩽ n` to be finitely generated. When `S` is the
spectrum of a field (and doubtless more generally, when it is the spectrum of an artinian ring) and `Y = X − U` is
finite, one can show that it is necessary and sufficient that the following conditions be verified:

<!-- original page 131 -->

1. `prof F_x > n` for every closed point `x` of `U` (compare 1.4).
1. `Rⁱg_∗(F)` is coherent for `i ⩽ n`, or what amounts to the same, there exists an open neighborhood `V` of `Y` such
    that for every closed point `x` of `U ∩ V`, one has `prof F_x > n + 1`.

**Proposition.**

<!-- label: XII.5.7 -->

Let `S` be a locally noetherian prescheme, `g: U → X` a morphism of preschemes of finite type over `S`,[^XII-5-star]
with structural morphisms `h` and `f`, `F` a quasi-coherent module on `U`, `n` an integer. The following conditions are
equivalent:

1. For every base change `S′ → S` with `S′` noetherian, the module `Rⁿg′_∗(F′)` on `X′` is coherent.

1. For every base change as above, and every coherent ideal `J` on `S′`, denoting by `ℐ` the ideal `J O_{X′}` on `X′`,
    the graded module

    ```text
    ⨁_{m⩾0} Rⁿg′_∗(ℐᵐF′)
    ```

    on `⨁_{m⩾0} ℐᵐ` is finitely generated.

1. For every base change `S′ → S`, and `J` as above, the graded module

    ```text
    ⨁_{m⩾0} Rⁿg′_∗(ℐᵐF′/ℐ^{m+1}F′)
    ```

    on `gr_ℐ(O_{X′}) = ⨁_{m⩾0} ℐᵐ/ℐ^{m+1}` is finitely generated.

Plainly (ii) ⇒ (i) and (iii) ⇒ (i), as one sees by setting `ℐ = 0` in conditions (ii) and (iii). The reverse
implications are obtained by applying (i) to the composite base change `S″ → S′ → S`, where `S″` is equal to
`Spec(⨁_{m⩾0} Jᵐ)` resp. `Spec(⨁_{m⩾0} Jᵐ/J^{m+1})`.

The interest of this proposition is that conditions of form (ii) are those that intervene in the "algebraic-formal
comparison theorems", whereas conditions of form (iii) intervene in the "existence theorems" that complement them, cf.
Exposé IX. A first interesting case is the one where `f: X → S` is the identity, and where it is therefore a question of
conditions on a morphism `h: U → S` locally of finite type and a quasi-coherent module `F` on `U` flat with respect to
`S`. To obtain sufficient conditions, we are going to assume that `U` embeds, via `g: U → X`, as an open subprescheme of
an `X` proper over `S`. Applying 5.1, one sees therefore:

**Corollary.**

<!-- label: XII.5.8 -->

Let `f: X → S` be a proper morphism with `S` locally noetherian, `U` an open subset of `X`, `g: U → X` the canonical
immersion, `h = fg: U → S`, `F` a quasi-coherent module on `X`, flat with respect to `S`. Suppose that for every base
change `S′ → S` with `S′` locally noetherian, one has `Rⁱg′_∗(F′)` coherent on `X′` for `i ⩽ n`. Then one has the
following:

1. For every base change `S′ → S` with `S′` locally noetherian, `Rⁱh′_∗(F′)` is coherent on `S′` for `i ⩽ n`.

1. For every `S′ → S` as above, and every coherent ideal `J` on `S′`, the graded modules

    ```text
    ⨁_{m⩾0} Rⁱh′_∗(JᵐF′)
    ```

    <!-- original page 132 -->

    on `⨁_{m⩾0} Jᵐ` are finitely generated for `i ⩽ n`.

1. For every `S′ → S` and `J` as above, the graded modules

    ```text
    ⨁_{m⩾0} Rⁱh′_∗(JᵐF′/J^{m+1}F′)
    ```

    on `gr_J(O_{S′}) = ⨁_{m⩾0} Jᵐ/J^{m+1}` are finitely generated for `i ⩽ n`.

Moreover, under the conditions of (ii), and by virtue of the comparison theorem 1.1, denoting by `Ŝ′` the formal
completion of `S′` along `J` and by `Û′` that of `U′` along `J O_{U′}`, the canonical homomorphisms

```text
R̂ⁱh′_∗(F′) → Rⁱĥ′_∗(F̂′) → lim_k Rⁱh′_∗(F′_k)
```

are isomorphisms for `i ⩽ n − 1`.

**Remark.**

<!-- label: XII.5.9 -->

Suppose moreover under the conditions of 5.8 with `F` coherent, and consider a base change `S′ → S` as in 5.9 (i).
Suppose moreover that `S′` is locally immersible in a regular scheme, or more generally, that there exists a morphism
`S″ → S′` faithfully flat and quasi-compact such that `S″` is locally immersible in a regular scheme; this condition is
verified in particular if `S′` is local. Then the conclusion of 5.8 (i) and (ii) remains valid when `F′` is replaced by
a module `G′` on `U′` such that every point of `U′` has an open neighborhood on which `G′` is isomorphic to a module of
the form `F′ⁿ`. Indeed, one is reduced to the case where `S′` itself is locally immersible in a regular scheme, so that
the same holds of `S″ = Spec(⨁_{m⩾0} Jᵐ)` and of `X″ = X′ ×_{S′} S″ = X ×_S S″`, which are of finite type over it. One
then applies the finiteness criterion VIII 2.3 to the direct images for `i ⩽ n` of `G″` under the immersion `U″ → X″`,
noting that they are satisfied by hypothesis for `F″`, hence also for `G″`, since they are expressed in terms of depth
and `G″` is locally isomorphic to a `F″ⁿ`. The same argument shows that if `𝒢′` is a coherent module on `Û′` (completion
of `U′` along the ideal `J O_{U′}`) such that `𝒢′₀ = 𝒢′/J 𝒢′` is locally of the form `F′₀ⁿ`, then the conclusion of
(iii) remains valid when `F′` is replaced there by `𝒢′`. One thus obtains the following result, using the results of
Exposé IX:

**Corollary.**

<!-- label: XII.5.10 -->

Let `f: X → S` be a proper morphism with `S` locally noetherian, `U` an open part of `X`; suppose `U` flat with respect
to `S`, and that for every base change `S′ → S` with `S′` locally noetherian, one has `Rⁱg′_∗(O_{U′})` coherent on `X′`
for `i = 0, 1`. Suppose then that `S′` is of the form `Spec(A)`, where `A` is a noetherian ring equipped with an ideal
`J` such that `A` is separated and complete for the `J`-adic topology. Under these conditions:

1. The functor `F ↦ F̂` from the category of locally free modules on `U′` to the category of locally free modules on
    `Û′` is fully faithful.
1. For every locally free module `𝓕` on `Û′`, there exists a coherent module `F` on `U′` (not necessarily locally free,
    alas), and an isomorphism `F̂ ≅ 𝓕`.

It remains only to prove (ii), thanks to 5.9. Now by that remark and 2.1, it follows that `𝓕` is induced by a coherent
module `𝓖` on `X̂′`. By the existence theorem *EGA* III 5.1.4, `𝓖` is of the form `F̂`, where `F` is coherent on `X`,
whence the conclusion.

<!-- original page 133 -->

**Remarks.**

<!-- label: XII.5.11 -->

1. Using 5.10, 4.7 and a suitable hypothesis, saying that certain local rings of the geometric fibers of `X′ → S′` are
    "pure" resp. parafactorial, one ought to be able to obtain statements saying that the functor `Z′ ↦ Ẑ′` from the
    category of étale covers of `X′` to the category of étale covers of `X̂′` (or what amounts to the same, of `X′₀`)
    is an equivalence of categories, resp. that the functor `L ↦ L̂` from the category of invertible modules on `X′` to
    the category of invertible modules on `X̂′` is an equivalence. Using recent results of Murre, it is probable that
    one ought to be able to deduce existence theorems for Picard schemes of certain non-proper algebraic
    schemes.[^N.D.E-XII-6] More generally, the elimination of purity hypotheses in various existence theorems, notably
    of representability of functors like Hilbert or Picard functors, by means of the techniques developed in this
    seminar, deserves a systematic study.

1. One may set oneself the problem of giving handy necessary and sufficient conditions, in terms of depth, for the
    universal finiteness condition envisaged in 5.10 to be verified. When `S` is the spectrum of a field, it follows
    easily from *EGA* III 1.4.15 that it is necessary and sufficient that the `Rⁱg_∗(F)` (`i ⩽ n`) be coherent, which
    is expressed in terms of depth thanks to VIII 2.3. In the general case, one will note however that it does not
    suffice to require that the preceding condition be verified for all the fibers `U_s ⊂ X_s` (`s ∈ S`), even in the
    case where `n = 0`. Take for example `X = S`, `S` the spectrum of a discrete valuation ring, `U` the open subset
    reduced to the generic point, `F = O_U`.

1. Here is, however, a sufficient condition ensuring that one is under the conditions of the hypothesis of 5.10: it
    suffices that `f` be flat, and that for every `s ∈ S` and every `x ∈ Y_s = X_s − U_s`, one has

    ```text
    prof O_{X_s,x} ⩾ n + 2.
    ```

    Indeed, taking into account Lemma 2.5 (cf. relation (16) after 2.5), it follows that one then has `g_∗(O_U) ≅ O_X`
    and `Rⁱg_∗(O_U) = 0` for `0 < i ⩽ n`, and the same relations will plainly be verified after any base change
    `S′ → S`.

<!-- ────────────────────────────────────────────────────────────────────── -->

<!-- Ledger delta — Exposé XII                                               -->

<!-- ────────────────────────────────────────────────────────────────────── -->

<!--
The following terminological choices were fixed in the present Exposé. They
extend the entries already recorded in `glossary.md`; merge into the master
glossary on the next consolidation pass.

| French                                            | English                                          | Note                                                                                  |
| ------------------------------------------------- | ------------------------------------------------ | ------------------------------------------------------------------------------------- |
| `schéma algébrique projectif`                     | projective algebraic scheme                      | Title-level term for the Exposé.                                                      |
| `théorème de dualité projective`                  | projective duality theorem                       | Serre, *FAC*; modelled on local duality (Exp. IV).                                    |
| `théorème de comparaison de Grauert`              | Grauert's comparison theorem                     | Heading of §2.                                                                        |
| `cône projetant épointé`                          | punctured projecting cone                        | `X̃ = Spec(S) − Spec(k)` of `X = P^r_k`.                                              |
| `section hyperplane`                              | hyperplane section                               | Zeros of a regular section of `O_X(1)`.                                               |
| `Module cohérent`                                 | coherent module                                  | Capital "Module" in the source preserved as lowercase in English.                     |
| `Algèbre graduée quasi-cohérente`                 | quasi-coherent graded algebra                    | As above; capital "Algèbre" lowercased.                                               |
| `Idéal cohérent`                                  | coherent ideal                                   | As above.                                                                             |
| `Ext_OX(F, G)` (underlined in source)             | `ℰxt_{O_X}(F, G)`                                | Sheafified Ext rendered with calligraphic `ℰ`, matching Exp. VI convention.           |
| `complété formel de X le long de Y`               | formal completion of `X` along `Y`               | Notation `X̂` preserved across line breaks.                                           |
| `platitude normale`                               | normal flatness                                  | Heading of §4; `gr_𝒥(O_X)` flat on `X₀`.                                              |
| `couple (X, X₀)`                                  | pair `(X, X₀)`                                   | Per SGA 2 master glossary.                                                            |
| `pur` (anneau local), respecté `respé`            | "pure" (local ring); the "respective" case       | Quotation marks preserve the SGA-era technical usage of `pur` (X 3.1).                |
| `parafactoriel`                                   | parafactorial                                    | XI 3.1.                                                                               |
| `condition de Lefschetz effective (Leff)`         | effective Lefschetz condition (Leff)             | X §2.                                                                                 |
| `morphisme adique`                                | adic morphism                                    | IX §2; the source notes the hypothesis is dispensable in 3.2's proof.                 |
| `générisation`                                    | generization                                     | Topological term used in 1.5.                                                         |
| `condition de finitude universelle`               | universal finiteness condition                   | Heading of §5; appears in 5.7 (i)–(iii).                                              |
| `condition de finitude simultanée`                | simultaneous finiteness condition                | 5.6: 5.2 (ii) reinterpreted.                                                          |
| `condition de nullité asymptotique`               | asymptotic vanishing condition                   | 5.6: 5.5 (i) reinterpreted.                                                           |
| `morphisme quasi-projectif`                       | quasi-projective morphism                        | 5.6.                                                                                  |
| `revêtement étale`                                | étale cover                                      | Per glossary; "covering" reserved for general topological covers.                     |
| `aboutissement`                                   | abutment                                         | Per glossary.                                                                         |
| `système projectif essentiellement constant`      | essentially constant projective system           | Mittag-Leffler reduction in proof of 2.2.                                             |
| `loisible`                                        | permissible                                      | "Allowable" reads too casual in proof prose.                                          |
| `tedious dévissage` (`pénible dévissage`)         | tedious dévissage                                | 1.6; "dévissage" kept as loanword per glossary.                                       |
| `expedient` (`expédient`)                         | expedient                                        | 3.5 Remark; "a somewhat tedious expedient".                                           |
| `on gagne`                                        | one wins                                         | End of proof of 3.1; preserved literally as a Grothendieckism.                        |

Unresolved / flagged:

- The source uses the Grothendieck-era capital "Module", "Algèbre", "Idéal" to
  signal sheaves of modules / algebras / ideals on a scheme; in English these
  are uniformly rendered with lowercase initial letter, since the typographic
  device is not standard in present-day mathematical English. The accompanying
  word (e.g. "coherent module", "graded algebra", "coherent ideal") preserves
  the technical content.
- The source labels equation (20 bis) and (21 bis) in §4; these are rendered
  as `eq:XII.4.20bis` and `eq:XII.4.21bis` to keep the numbering visible.
- The Roman-numbered conditions a)/b)/c) inside 3.1 and a′)/b′)/c′) inside the
  proof of 3.1 are kept as in the source; they are not Markdown-numbered list
  items because of the prime in a′), b′), c′).
- The "Comments on Exposé XIII (XIII 6)" reference visible in the introduction
  is not cited in Exposé XII proper; no action needed.
- Footnote [^N.D.E-XII-6] is very long because the source footnote (6) on
  pp. 133–134 carries a full bibliographic survey; it is rendered verbatim.
-->

[^XII-1-star]: The present exposé, written up in January 1963, is markedly more detailed than the oral exposé was, in
    June 1962.

[^XII-1-starstar]: J.-P. Serre, "Faisceaux algébriques cohérents", *Ann. of Math.* **61** (1955), pp. 197–278.

[^N.D.E-XII-1]: *N.D.E.* The reader fond of the History of Mathematics will consult with interest the letter that
    Grothendieck wrote to Serre on 15 December 1955 and the latter's reply of 22 December of the same year;
    see *Correspondance Grothendieck-Serre*, edited by Pierre Colmez and Jean-Pierre Serre, Documents
    Mathématiques, vol. 2, Société Mathématique de France, Paris, 2001.

[^XII-1-starstarstar]: For a more general duality theorem, cf. the Hartshorne seminar cited at the end of Exp. IV.

[^XII-1-star2]: The first part of 1.5 may be obtained at once by applying the purely local statement *EGA* IV 12.3.4 to
    the preceding `Eʲ`, which short-circuits the greater part of the proof that follows.

[^XII-1-star3]: This remark is made more precise by the footnote on page 112.

[^N.D.E-XII-2]: *N.D.E.* See Corollary I.1.4 of the article of Mme Raynaud (Raynaud M., "Théorèmes de Lefschetz en
    cohomologie des faisceaux cohérents et en cohomologie étale. Application au groupe fondamental", *Ann.
    Sci. Éc. Norm. Sup.* (4) **7** (1974), pp. 29–52).

[^N.D.E-XII-3]: *N.D.E.* For a version without flatness hypothesis, see (Raynaud M., "Théorèmes de Lefschetz en
    cohomologie des faisceaux cohérents et en cohomologie étale. Application au groupe fondamental", *Ann.
    Sci. Éc. Norm. Sup.* (4) **7** (1974), pp. 29–52, Theorem II.3.3).

[^XII-3-star]: Rectified as indicated in IX p. 85.

[^N.D.E-XII-4]: *N.D.E.* Let us point out the spectacular connectedness result obtained since by Fulton and Hansen, in
    the case where `S = Spec(k)` (`k` an algebraically closed field). Let `g: X → P^m_k × P^m_k` be such
    that `dim g(X) > m`; then the inverse image of the diagonal is connected. Among other things, this
    allows one to generalize Corollary 4.9 when `f` is the structural morphism of the projective space
    `P^m_k` over `S = Spec(k)`: precisely, an irreducible subvariety `X` of `P^m_k` of dimension `> m/2` has
    trivial fundamental group! (cf. Fulton W. & Hansen J., "A connectedness theorem for projective
    varieties, with applications to intersections and singularities of mappings", *Ann. of Math.* (2)
    **110** (1979), no. 1, pp. 159–166). For generalizations to the case of Grassmannians or abelian
    varieties, see Debarre O., "Théorèmes de connexité pour les produits d'espaces projectifs et les
    grassmanniennes", *Amer. J. Math.* **118** (1996), no. 6, pp. 1347–1367 and "Théorèmes de connexité et
    variétés abéliennes", *Amer. J. Math.* **117** (1995), no. 3, pp. 787–805. The triviality result for the
    fundamental group of `X` as above was obtained independently by Faltings, who proves moreover that
    `Pic(X)` has no torsion prime to the characteristic of `k`, by methods of algebraization of formal
    vector bundles, more in the line of Grothendieck's techniques, cf. (Faltings G., "Algebraization of some
    formal vector bundles", *Ann. of Math.* (2) **110** (1979), no. 3, pp. 501–514).

[^N.D.E-XII-5]: *N.D.E.* As Raynaud has remarked, the decomposition result for the de Rham complex of Deligne and
    Illusie easily entails the vanishing of the group `Hⁱ(X, L⁻¹)` (with `L` ample on `X` projective and
    smooth over `k` of characteristic `p > 0`) for `i < inf(p, dim(X))` as soon as one assumes that `X` is
    liftable to a flat scheme over `W₂(k)` (cf. Deligne P. & Illusie L., "Relèvements modulo `p²` et
    décomposition du complexe de de Rham", *Invent. Math.* **89** (1987), no. 2, pp. 247–270); this gives a
    purely algebraic proof of Kodaira's result for projective varieties in characteristic zero. If `X` is
    not liftable, it is well known that the "vanishing theorem" is false; cf. the example in (Raynaud M.,
    "Contre-exemple au 'vanishing theorem' en caractéristique `p > 0`", in *C.P. Ramanujam — a tribute*,
    Tata Inst. Fund. Res. Studies in Math., vol. 8, Springer, Berlin–New York, 1978, pp. 273–278); see also
    the very pretty examples in (Haboush W. & Lauritzen N., "Varieties of unseparated flags", in *Linear
    algebraic groups and their representations (Los Angeles, CA, 1992)*, Contemp. Math., vol. 153, American
    Mathematical Society, Providence, RI, 1993, pp. 35–57), simplified in (Lauritzen N. & Rao A.P.,
    "Elementary counterexamples to Kodaira vanishing in prime characteristic", *Proc. Indian Acad. Sci.
    Math. Sci.* **107** (1997), no. 1, pp. 21–25). On the other hand, I do not know an example where the map
    `Pic(X_{n+1}) → Pic(X_n)` is not surjective for `n > 1` in positive characteristic, where `X_n` denotes
    a thickened hyperplane section of `X` projective and smooth as above.

[^XII-5-star]: It suffices in fact that `g` be quasi-compact and quasi-separated (*EGA* IV 1.2.1), without conditions on
    `U`, `X`.

[^N.D.E-XII-6]: *N.D.E.* Of course, in the projective case one refers to Grothendieck's existence theorems of *FGA*; cf.
    Grothendieck A., "Technique de descente et théorèmes d'existence en géométrie algébrique. VI. Les
    schémas de Picard: propriétés générales", in *Séminaire Bourbaki*, vol. 7, Société mathématique de
    France, Paris, 1995, Exp. 236, pp. 221–243 and "Technique de descente et théorèmes d'existence en
    géométrie algébrique. V. Les schémas de Picard: théorèmes d'existence", in *Séminaire Bourbaki*, vol. 7,
    Société mathématique de France, Paris, 1995, Exp. 232, pp. 143–161. The nine finiteness conjectures
    contained therein are proved in Exposés XII and XIII of Mme Raynaud and Kleiman in SGA 6. For an
    excellent elementary text on the subject, see Kleiman's expository article (Kleiman S., "The Picard
    scheme", to appear in *Contemp. Math.*). For an application of these techniques to the global
    generalized Jacobians of a relative smooth curve, see (Contou-Carrère C., "La jacobienne généralisée
    d'une courbe relative; construction et propriété universelle de factorisation", *C. R. Acad. Sci. Paris
    Sér. A-B* **289** (1979), no. 3, A203–A206 and "Jacobiennes généralisées globales relatives", in *The
    Grothendieck Festschrift*, Vol. II, Progr. Math., vol. 87, Birkhäuser, Boston, 1990, pp. 69–109). See
    also, by the same author, in the purely local context, the construction and study of the "local
    generalized Jacobian" functor ("Jacobienne locale, groupe de bivecteurs de Witt universel, et symbole
    modéré", *C. R. Acad. Sci. Paris Sér. I Math.* **318** (1994), no. 8, pp. 743–746). Moreover, while in
    the case of a projective and smooth morphism the connected components of the Picard scheme are proper,
    this is no longer the case in the singular case. The problem of compactifying Picard schemes arises
    naturally: this problem has been studied in detail, notably in (Altman A.B. & Kleiman S., "Compactifying
    the Picard scheme", *Adv. in Math.* **35** (1980), no. 1, pp. 50–112, and "Compactifying the Picard
    scheme. II", *Amer. J. Math.* **101** (1979), no. 1, pp. 10–41). The case of curves had been studied
    earlier (D'Souza C., "Compactification of generalised Jacobians", *Proc. Indian Acad. Sci. Sect. A Math.
    Sci.* **88** (1979), no. 5, pp. 419–457). One even knows exactly when the compactified Jacobian of a
    curve is irreducible (Rego C.J., "The compactified Jacobian", *Ann. Sci. Éc. Norm. Sup.* (4) **13**
    (1980), no. 2, pp. 211–223), this being the closure of the (ordinary) Jacobian when the curve is
    geometrically integral and locally planar; for a family construction of compactified Jacobians, see
    (Esteves E., "Compactifying the relative Jacobian over families of reduced curves", *Trans. Amer. Math.
    Soc.* **353** (2001), no. 8, pp. 3045–3095). Since then, existence results for the Picard scheme in the
    proper case have progressed since the original edition of SGA 2; cf. (Murre J.P., "On contravariant
    functors from the category of pre-schemes over a field into the category of abelian groups (with an
    application to the Picard functor)", *Publ. Math. Inst. Hautes Études Sci.* **23** (1964), pp. 5–43) and
    especially (Artin M., "Algebraization of formal moduli. I", in *Global Analysis (Papers in Honor of K.
    Kodaira)*, Univ. Tokyo Press, Tokyo, 1969, pp. 21–71). See also (Raynaud M., "Spécialisation du foncteur
    de Picard", *Publ. Math. Inst. Hautes Études Sci.* **38** (1970), pp. 27–76) in the case of a proper
    scheme over a discrete valuation ring, but not necessarily flat. For a discussion of more recent
    results, particularly those of Artin, for the Picard functor of proper and flat schemes, in particular
    in the cohomologically flat case in dimension 0, see Chapter VIII of (Bosch S., Lütkebohmert W. &
    Raynaud M., *Néron models*, Ergebnisse der Mathematik und ihrer Grenzgebiete (3), vol. 21,
    Springer-Verlag, Berlin, 1990) and the references cited. Much more recently, very fine results have been
    obtained in the case of relative curves `f: X → S` over the spectrum `S` of a discrete valuation ring
    with perfect residue field. More precisely, one assumes that `f` is proper and flat, `X` regular and
    `f_∗ O_X = O_S`. On the other hand, one does not assume `f` cohomologically flat in dimension 0, i.e.
    one does not assume `H¹(X, O)` torsion-free. The Picard scheme is then not representable, either by a
    scheme or an algebraic space, as soon as the torsion in question is non-zero. Let `J` be the Néron model
    of the generic fiber of `f`: it is a quotient of the Picard functor `P`. Then, Raynaud has shown that
    the kernel of the tangent map `H¹(X, O) = Lie(P) → Lie(J)` coincides with the torsion subgroup of `H¹`
    and that the cokernel has the same length (see Theorem 3.1 of (Liu Q., Lorenzini D. & Raynaud M., "Néron
    models, Lie algebras, and reduction of curves of genus one", *Invent. Math.* **157** (2004), pp.
    455–518)). This result allows the above-mentioned authors to study the link between the
    Birch–Swinnerton-Dyer and Artin–Tate conjectures (see Theorem 6.6 of *loc. cit.*). Concerning the local
    Picard scheme, see Boutot's thesis, cited in editor's note (13) page 149.
