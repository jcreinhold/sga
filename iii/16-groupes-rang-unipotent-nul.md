# Exposé XVI. Groups of zero unipotent rank

<!-- label: III.XVI -->

*by M. Raynaud*[^XVI-0]

## 1. An immersion criterion

<!-- label: III.XVI.1 -->

<!-- original page 484 -->

### 1.1. Examples of monomorphisms of group preschemes that are not immersions.

<!-- label: III.XVI.1.1 -->

We are going to construct a prescheme `S`, two `S`-group preschemes `G` and `H`, and an `S`-group monomorphism
`u : G → H` that is not an immersion. The groups `G` and `H` will be of finite presentation over `S`, flat over `S`,
and `G` will even be smooth over `S` (cf. Exp. VIII, paragraph and footnote (∗) preceding 7.1; see also XVII App. III,
4).

a) Take first for `S` the spectrum of a discrete valuation ring `A`, of unequal characteristic and of residue
characteristic equal to 2. Let `t` be the generic point of `S` and `s` the closed point. Take for `G` the open subgroup
of the constant group `G₀ = (ℤ/2ℤ)_S` obtained by removing the point of the closed fiber `(ℤ/2ℤ)_s` distinct from the
identity element, and take for `H` the group of multiplicative type `(µ₂)_S` of second roots of unity (Exp. I 4.4.4). In
view of the choice of `S`, `H_t` is isomorphic to `(ℤ/2ℤ)_t` while `H_s` is a radicial group. One has an evident
morphism `G₀ → H` defined by the section `(−1)` of `H`, whence a morphism `u : G → H` which is a monomorphism but is
not an immersion (otherwise it would necessarily be an isomorphism (cf. Exp. VIII 7)). Here, Exp. VIII 7.9 does not
apply, since `₂G = G` is not finite over `S`.

b) Denote by `K` the `S`-group prescheme, étale and non-separated, obtained from the unit group <!-- original page 485
--> by "doubling" the unique point of the closed fiber. Take for `H` the product group `(µ₂)_S ×_S K`. Let `a` (resp.
`b`) be the unique section of `µ₂` (resp. `K`) over `S` distinct from the unit section, and let `h = (a, b)` be the
corresponding section of `H`. The datum of `h` defines an `S`-group morphism

```text
u : G = (ℤ/2ℤ)_S ⟶ H.
```

It is clear that `u` is a monomorphism and is not an immersion. Here, Exp. VIII 7.9 does not apply, since `₂H = H` is
not separated over `S`.

c) More interesting is the following example, in which `G` is a smooth group with connected fibers (and even
`G = (𝔾_a)_S`) (cf. Exp. VIII 7.10).

Take for `S` the spectrum of a discrete valuation ring `A` of equal characteristic 2, and let `π` be a uniformizer of
`A` and `𝔪` the maximal ideal of `A`.

Consider the additive group `(𝔾_a)_S`, the product group `(𝔾_a × 𝔾_a)_S` of ring `A[X, Y]`, and let `G₁` be the closed
subgroup of equation

```text
(1)    X² + X − πY = 0.
```

<!-- label: eq:III.XVI.1.1.1 -->

The group `G₁` is smooth over `S`, its generic fiber is isomorphic to `(𝔾_a)_t` and its closed fiber is isomorphic to
the product of `(𝔾_a)_s` by `(ℤ/2ℤ)_s`. One may take for the factor `(ℤ/2ℤ)_s` the subgroup `N_s` of `(G₁)_s` of
equation

```text
(2)    Y = X² + X = 0.
```

<!-- label: eq:III.XVI.1.1.2 -->

<!-- original page 486 -->

Let `N′` and `N″` be two group subschemes of `G₁`, isomorphic to `(ℤ/2ℤ)_S`, whose closed fibers coincide with `N_s`
and whose generic fibers are distinct. The groups `N′` and `N″` are therefore defined by the data of two sections of
`G₁` over `S` with coordinates `(a′, b′)` (resp. `(a″, b″)`) such that

```text
(3)    a′² + a′ − πb′ = a″² + a″ − πb″ = 0,
       a′ and a″ ≡ 1 (mod 𝔪), a′ ≠ a″,
       b′ and b″ ≡ 0 (mod 𝔪).
```

<!-- label: eq:III.XVI.1.1.3 -->

(One may take, for example, `(1, 0)` and `(1 + π², π + π³)`.)

The quotient groups `G′ = G₁/N′` and `G″ = G₁/N″` are representable (Exp. V 4.1). Let `u` be the canonical morphism

```text
u : G₁ ⟶ G′ ×_S G″,
```

and let `H` be the group subscheme of `G′ ×_S G″` equal to the schematic closure in `G′ ×_S G″` of `u_t((G₁)_t)`, so
that `u` factors through `H`. The kernel of `u` is `K = N′ ∩ N″`, whose generic fiber is the unit group and whose
closed fiber is equal to `N_s`; in particular, `K` is not flat over `S`. On the generic fiber, `u_t` is therefore an
isomorphism of `(G₁)_t` onto `H_t`. On the other hand, I claim that `H_s` is not smooth. Indeed, if `H_s` were smooth,
then since `u_s` is a morphism with finite kernel and `(G₁)_s` and `H_s` have the same dimension (namely 1), `u_s`
would be a flat morphism; since `G₁` and `H` are flat, `u` would be a flat morphism and consequently `Ker u` would be
flat over `S`, which is not the case. It is clear that the restriction of `u` to the connected component `G` of `G₁`
is a monomorphism (the fibers of `K ∩ G` are unit groups, so `K ∩ G` is the unit group (Exp. VI_B 2.9)), but it is not
an immersion (otherwise it would be an open immersion and `H_s` would be smooth). <!-- original page 487 --> Here, Exp.
VIII 7.9 does not apply, since `₂G = G` is not finite over `S`.

For lovers of equations, let us say that in the example above one may take for `H` the closed subgroup of
`(𝔾_a ×_S 𝔾_a)_S` with ring `A[V, W]/(F)`, where

```text
F = (a″b′ − b″a′)(a″²V − a′²W) − (a″V − a′W)²
```

(where `a′, a″, b′, b″` satisfy (3)). For `G`, one takes the group `(𝔾_a)_S` with ring `A[T]`, and for morphism
`u : G → H` the `S`-morphism defined by the maps

```text
V ↦ a′(a′T + πT²),    W ↦ a″(a″T + πT²).
```

**Remark 1.2.** *The preceding construction is inspired by the method of Koizumi–Shimura.[^N.D.E-XVI-1] It does not
apply when `S` is the spectrum of a ring of unequal characteristic, the points of finite order of `G` being then "too
rigid".*

<!-- label: III.XVI.1.2 -->

### 1.3. Statement of the immersion criterion.

<!-- label: III.XVI.1.3 -->

**Theorem 1.3.** *Let `S` be a locally noetherian prescheme, `G` an `S`-group prescheme, smooth over `S`, of finite
type, possessing locally for the fpqc topology Cartan subgroups (Exp. XV 6.1 and 7.3 (i)), `H` an `S`-group prescheme
locally of finite type, `u : G → H` an `S`-group monomorphism. Then:*

*a) If `G` has connected fibers, in order that `u` be an immersion, it is necessary and sufficient that for every
`S`-scheme `S′` which is the spectrum of a complete discrete valuation ring with algebraically closed residue field,
and for every Cartan subgroup `C` of `G_{S′}`, the restriction of `u_{S′}` to `C` be an immersion.*

*b) In order that `u` be an immersion (resp. a closed immersion), it is necessary and sufficient that for every `S′` as
above and every Cartan subgroup `C` of the connected component `(G_{S′})⁰` of `G_{S′}`, the restriction of `u_{S′}` to
the normalizer (Exp. XI 6.11) `N` of `C` in `G_{S′}` be an immersion (resp. a closed immersion).*

<!-- label: III.XVI.1.3 -->

<!-- original page 488 -->

Before proving 1.3, let us state some applications.

**Corollary 1.4.** *Let `S` be a prescheme, `G` an `S`-group prescheme smooth over `S`, of finite presentation over `S`,
of zero unipotent rank (Exp. XV 6.1 ter) and possessing locally for the fpqc topology maximal tori, `H` an `S`-group
prescheme, `u : G → H` an `S`-group monomorphism. Suppose further that either `H` is of finite presentation over `S`,
or `S` is locally noetherian and `H` locally of finite type. Then:*

*a) If `G` has connected fibers, `u` is an immersion.*

*b) If `H` is separated over `S` and if for every `S′` over `S` and every maximal torus `T` of `G_{S′}` the Weyl group*

```text
W = Norm_{G_{S′}}(T) / Centr_{G_{S′}}⁰(T)
```

*is representable (a condition always realized if `G` has connected fibers (Exp. XV 7.1 (iv))) and is finite over `S`,
then `u` is a closed immersion.*

<!-- label: III.XVI.1.4 -->

**Corollary 1.5.** *Let `S` be a prescheme, `G` an `S`-group prescheme smooth over `S`, of finite presentation over
`S`, with connected fibers, `H` an `S`-group prescheme, `u : G → H` an `S`-group monomorphism. Suppose either `H` of
finite presentation over `S`, or `S` locally noetherian and `H` locally of finite type. Then:*

<!-- original page 489 -->

*a) If `G` is reductive, i.e. is affine over `S` with reductive fibers (cf. Exp. XIX), `u` is an immersion, and a closed
immersion if `H` is separated.*

*b) If `G` has affine, solvable, connected fibers, of zero unipotent rank, `u` is an immersion, and a closed immersion
if `H` is separated.*

<!-- label: III.XVI.1.5 -->

**Proof of 1.4 from 1.3.**

*Reduction to the noetherian case.* If `S` is locally noetherian, the reduction is immediate, the properties to prove
being local on `S`. In the second case, `G` and `H` are of finite presentation over `S`. Replacing `S` by a smaller open
if necessary, we may assume `S` affine. By Exp. VI_B § 10, there exist a noetherian scheme `S₀`, an `S₀`-group prescheme
`G₀` smooth over `S₀` (with connected fibers in case a)), of finite type over `S₀`, an `S₀`-group prescheme `H₀` of
finite type (separated in case b)), and an `S₀`-group morphism

```text
u₀ : G₀ ⟶ H₀,
```

such that `G`, `H`, `u` are obtained from `G₀`, `H₀`, `u₀` by a base extension `S → S₀`. The fact that `u` is a
monomorphism translates to `Ker u =` unit group; we may therefore assume that `u₀` is a monomorphism. Since `G` has
zero unipotent rank `ρ_u` and possesses, locally for the fpqc topology, maximal tori, the abelian rank `ρ_{ab}` of the
fibers of `G` is locally constant (Exp. XV 8.18). But `ρ_u` and `ρ_{ab}` are locally constructible functions (Exp. XV
6.3 bis). A standard argument (cf. EGA IV 8.3.4) shows that one may choose `S₀` and `G₀` so that the unipotent rank
(resp. the abelian rank) of the fibers of `G₀` is zero (resp. locally constant). But then `G₀` possesses locally
maximal tori for the fpqc topology (Exp. XV 8.18), and <!-- original page 490 --> the functor `𝒯ℳ_{G₀}` of maximal tori
of `G₀` is representable by an `S₀`-scheme `X₀`, of finite type over `S₀` (Exp. XV 8.15). Let `T₀` be the "universal"
maximal torus of `(G₀)_{X₀}`, `X` the `S`-prescheme `X₀ ×_{S₀} S`, `T = T₀ ×_{S₀} S` the universal maximal torus for
`G`. By hypothesis, in case b), the Weyl group relative to `T` is representable and finite over `X`. These two
properties are compatible with projective limits of preschemes (Exp. VI_B 10.1 iii) and EGA IV 8.10.5). One may
therefore choose `S₀` so that the Weyl group of `T₀` is finite over `X₀`. Under these conditions it is clear that to
prove 1.4 we may replace `S`, `G`, `u`, `H` by `S₀`, `G₀`, `u₀`, `H₀`, hence assume `S` noetherian.

Let us use the valuative criterion provided by 1.3. We are reduced to the case where `S` is the spectrum of a discrete
valuation ring and where `G₀` possesses a Cartan subgroup `C`.

*Proof of 1.4 a).* We must show that the restriction of `u` to `C` is an immersion (1.3 a)), which reduces us to the
case where `G = C` has nilpotent connected fibers. Standard reductions (cf. Exp. VIII proof of 7.1) reduce us to the
case where `H` is flat over `S`, `u` is an isomorphism on the generic fiber, and `u` is an isomorphism of underlying
spaces on the closed fiber. The group `H` is then with connected fibers, hence separated over `S` (Exp. VI_B 5.2).
Granting for a moment the lemma:

**Lemma 1.6.** *Let `S` be a prescheme, `G` an `S`-group prescheme smooth over `S`, with connected, nilpotent fibers,
of zero unipotent rank. Then:*

<!-- label: III.XVI.1.6 -->

*i) `G` is commutative.*

*ii) For every integer `n > 0`, `_n G` is a group prescheme, flat, quasi-finite over `S`, finite over `S` if and only
if the abelian rank, or the reductive rank, of `G` is locally constant on `S`.*

*iii) For every integer `q > 0` invertible on `S`, the family of subgroups `_{qⁿ}G` is universally schematically dense
in `G` relative to `S` (EGA IV 11.10.8).*

<!-- original page 491 -->

Lemma 1.6 applies to the group `G`, and since `G` possesses locally maximal tori, the reductive rank of the fibers of
`G` is locally constant; hence (1.6 ii)), for every integer `n > 0`, `_n G` is finite over `S`. The fact that `u` is an
immersion then follows from Exp. VIII 7.9.

**Proof of 1.6.** Let us first examine the case where `S` is the spectrum of a field:

**Lemma 1.7.** *Let `k` be a field of characteristic `p`, `G` an algebraic `k`-group, smooth, connected, nilpotent, of
zero unipotent rank. Then `G` is a commutative group, extension of an abelian variety `A` by a torus `T`. For every
integer `n > 0`, `_n G` is a finite group, étale if `(n, p) = 1`, defined by a `k`-algebra of rank `n^{ρ_r + 2ρ_{ab}}`.
If `(q, p) = 1`, the family of subgroups `_{qⁿ}G (n ∈ ℕ)` is schematically dense in `G`.*

<!-- label: III.XVI.1.7 -->

**Proof of 1.7.** Let `Z` be the center of `G`. The group `G/Z` is affine (Exp. XII 6.1), of zero unipotent rank,
smooth and connected, hence is a torus (*Bible* 4 th. 4); but then `G` is commutative (Exp. XII 6.4). If `T` is the
unique maximal torus of `G` (Exp. XV 3.4), it follows at once from Chevalley's theorem (Sém. Bourbaki 1956/57, No. 145)
that `G` is an extension of an abelian variety `A` by `T`. For every integer `n > 0`, raising to the `n`th power is an
epimorphism in `T`; one deduces an exact sequence

```text
0 ⟶ _n T ⟶ _n G ⟶ _n A ⟶ 0.
```

A classical theorem of Weil (A. Weil: *Variétés abéliennes et courbes algébriques*, § IX th. 33 cor. 1) tells us that
`_n A` is a finite group defined by a `k`-algebra of rank `n^{2ρ_{ab}}`. Since `_n T` is a finite group of rank
`n^{ρ_r}`, one deduces the announced structure of `_n G`.

Now let `H` be the smallest closed subscheme of `G` majorizing `_{qⁿ}G` for every `n`. It follows from the foregoing
and from Exp. XV 4.6 that `H` is a smooth, connected subgroup, hence of the same type as `G`. Raising to the `n`th
power in `H` is an epimorphism (since `_q H` is finite), so that one has the exact sequence

```text
0 ⟶ _q H ⟶ _q G ⟶ _q(G/H) ⟶ 0.
```

It follows that `_q(G/H) = 0`, hence `G/H = 0`. That is to say, the subgroups `_{qⁿ}G` are schematically dense in `G`.
<!-- original page 493 -->

*Continuation of the proof of 1.6 i).* To show that `G` is commutative, we reduce by the usual procedure to the case
where `S` is noetherian, then to the case where `S` is the spectrum of a local ring with closed point `s`. The center
of `G` is representable by a closed group subscheme `Z` of `G` (Exp. XI 6.11). To show that `Z = G`, it suffices to
show that `Z = G` after reduction by every power of the maximal ideal of the ring of `S` (for `Z` will then be an open
subgroup of `G`, hence equal to `G` since `G` has connected fibers). This reduces us to the case where `S` is local
artinian.

Let `q` be an integer invertible on `S`. For every integer `n`, `_{qⁿ}G_s` is a subgroup of multiplicative type of
`G_s`, étale and central (1.7). Since `G` is smooth, `_{qⁿ}(G_s)` lifts to an `S`-group subscheme étale and central
`M_n` of `G` (Exp. XV 1.2). The family of flat subgroups `M_n`, `n ∈ ℕ`, is then schematically dense in `G` (1.7 and EGA
IV 11.10.9). Since `Z` is closed in `G` and majorizes all the `M_n`, we have `Z = G`.

*1.6 ii).* To see that `_n G` is flat and quasi-finite over `S`, it suffices to show that raising to the `n`th power in
`G` is a flat and quasi-finite morphism. Since `G` is flat over `S`, we are reduced to the case where `S` is the
spectrum of a field (EGA IV 11.3.10), and we noted in the proof of 1.7 that raising to the `n`th power was an
epimorphism. Moreover `_n G` is separated over `S`, since `G` is separated over `S` (Exp. VI_B <!-- original page 494
--> 5.2). For `_n G` to be finite over `S`, it is necessary and sufficient that the fibers of `_n G` be the spectra of
finite algebras, of locally constant rank (one sees this immediately by reducing to the case where `S` is the spectrum
of a henselian local ring). But, by 1.7, this condition amounts to saying that the abelian rank, or the reductive rank,
of the fibers of `G` is locally constant.

*1.6 iii).* To see that the family of subgroups `_{qⁿ}G (n ∈ ℕ)` is universally schematically dense in `G`, we again
reduce to the case `S` noetherian. Taking 1.7 and 1.6 b) into account, it suffices to apply EGA IV 11.10.9.

**Proof of 1.4 b).** We have reduced to the case where `S` is the spectrum of a discrete valuation ring and where `G₀`
possesses a Cartan subgroup `C`. Let `N = Norm_G C = Norm_G T`, where `T` is the unique maximal torus of `C` (Exp. XII
7.1 a) and b)). Since `H` is separated over `S`, it follows from 1.6 ii) and from Exp. VIII 7.12 that the restriction
of `u` to `C` is a closed immersion. On the other hand, to prove that `u` is a closed immersion, it suffices to show
that this is the case for `u|N` (1.3 b)). Since by hypothesis `W = N/C` is representable by a finite group scheme, this
will follow from the following lemma, applied to the exact sequence

```text
0 ⟶ C ⟶ N ⟶ W ⟶ 1
```

(note that a proper immersion is a closed immersion).

**Lemma 1.8.** *Let `S` be a prescheme, `G` an `S`-group prescheme of finite presentation over `S`, extension of a
group prescheme `G″`, proper and of finite presentation over `S`, by a group prescheme `G′`, of finite presentation
and flat over `S`:*

<!-- label: III.XVI.1.8 -->

<!-- original page 495 -->

```text
1 ⟶ G′ ⟶ G ⟶ G″ ⟶ 1.
```

*Let on the other hand `H` be an `S`-group prescheme of finite presentation over `S` (or locally of finite presentation
if `S` is locally noetherian) and `u : G → H` an `S`-group morphism. Then if the restriction of `u` to `G′` is proper,
`u` is proper.*

**Proof of 1.8.** We reduce as usual to the case where `S` is noetherian (Exp. VI_B § 10 and Exp. XV 6.2) and we may
then apply the valuative criterion of properness (EGA II 7.3.8). We therefore suppose that `S` is the spectrum of a
discrete valuation ring `A`, with closed point `s` and generic point `t`. Let `x ∈ G(t)` and `h ∈ H(S)` be such that
`u_t(x) = h(t)`. We must show that `x` comes from a unique element `x` of `G(S)`. It even suffices to prove the
existence and uniqueness of `x` after a faithfully flat extension of the discrete valuation ring `A`. Now let `y` be
the projection of `x` in `G″(t)`. Since `G″` is proper over `S`, `y` comes from a unique element `y` of `G″(S)`. Let
`X` be the inverse image of `y` in `G`. The prescheme `X` is faithfully flat over `S` (since `G′` is faithfully flat
over `S` as is the morphism `G → G″` (Exp. VI_B § 9)). Replacing if necessary the discrete valuation ring by a
faithfully flat one, we may assume that `X` has a section `ℓ` over `S` (EGA IV 14.5.8). Replacing `x` by `xℓ_t⁻¹`, we
may assume that `x ∈ G′(t)`. But then the existence and uniqueness of `x` follow from the fact that `u|G′` is proper.

**Proof of 1.5.**

<!-- original page 496 -->

a) We shall see in Exp. XIX that if `G` is reductive, `G` possesses locally for the faithfully flat topology maximal
tori, has a finite Weyl group, and has zero unipotent rank. Assertion a) follows, in view of 1.4.

b) If `G` has affine fibers of zero unipotent rank, `G` possesses maximal tori locally for the fpqc topology (Exp. XV
8.18). It then suffices to apply 1.4, taking into account the fact that `G`, having connected, smooth, affine, solvable
fibers, has unit Weyl group (*Bible* 6 th. 1 cor. 3).

**Proof of 1.3 a).**

Since the morphism `u` is already a monomorphism, in order to see that `u` is an immersion, it suffices to show that
`u` is proper at the points of `u(G)` (EGA IV 15.7.1); for that we may use the valuative criterion of local properness
(EGA IV 15.7.5). We are thus reduced to the case where `S` is the spectrum of a complete discrete valuation ring with
algebraically closed residue field, with closed point `s` and generic point `t`. Since `G` is flat over `S`, standard
reductions (cf. Exp. VIII proof of 7.1) allow us to reduce to the case where `H` is flat over `S`, `u_t` is an
isomorphism, and `u_s` is an isomorphism of underlying spaces. To say that `u` is an immersion is then equivalent to
saying that `u` is an isomorphism.

By hypothesis, the group `G` possesses locally Cartan subgroups for the fpqc topology, so we may speak of the open set
`U` of regular points of `G` <!-- original page 497 --> (Exp. XV 7.3 i) and ii)).

**Lemma 1.9.** *With the preceding hypotheses, in order that `u` be an immersion, it suffices that `u|U` be an
immersion.*

<!-- label: III.XVI.1.9 -->

Indeed, to say that `u|U` is an immersion means that there exist an open `V` of `H` and a closed `F` of `V` such that
`u|U` factors through `F` and induces an isomorphism of `U` onto `F`. Since `H_t`, and hence also `V_t`, is irreducible,
one necessarily has `V_t = F_t`. But then `F_t` majorizes the schematic closure of `V_t` in `V`, which is equal to `V`
since `H` is flat over `S`. In short, `V = F`. It follows that `u|U` is an open immersion, hence `u` is an open
immersion (VI_B 2.6).

It remains to show that `u|U` is an immersion, and for that we apply the valuative criterion of local properness.
Replacing `S` by the spectrum of a faithfully flat discrete valuation ring, we must show that if `h` is a section of
`H` over `S` whose image `h(S)` is contained in `u(U)`, then `h` is the image of a section `g` of `U` over `S`. It
suffices to show that `h` is contained in the image of a Cartan subgroup `C` of `G`. Indeed, by hypothesis `u|C` is an
immersion, so `h` is the image of a section `g` of `C`, which is necessarily a section of `U`.

<!-- original page 498 -->

Let `a ∈ U(s)` (resp. `b ∈ U(t)`) be such that `u_s(a) = h(s)` (resp. `u_t(b) = h(t)`). Since `u_t` is an isomorphism,
`h(t)` is a regular point of `H_t`, so is contained in a unique Cartan subgroup `D_t` of `H_t` (Exp. XIII 3.2). Let `D`
be the schematic closure of `D_t` in `H`.

**Lemma 1.10.** *i) `D_s` is a nilpotent algebraic group (Exp. VI_B § 8).*

<!-- label: III.XVI.1.10 -->

*ii) `dim D_s = ν =` nilpotent rank of `G =` nilpotent rank of `(H_s)_{red}`.*

*iii) `h(s) ∈ D_s(κ(s))`.*

i) Since `H` is separated (Exp. VI_B 5.2), so is `D`. Moreover, `D` is flat over `S`, and its generic fiber is
nilpotent. The fact that `D_s` is nilpotent then follows from Exp. VI_B 8.4.

ii) Since `(H_s)_{red} ≃ G_s`, these two groups have the same nilpotent rank. Since `G` possesses, locally for the fpqc
topology, Cartan subgroups, `G_s` and `G_t` have the same nilpotent rank `ν`. Finally, since `D` is flat over `S`, one
has `dim D_s = dim D_t = ν` (Exp. VI_B § 4).

c) Since `h_t` factors through `D_t`, `h` evidently factors through `D`, whence iii).

This being said, the following lemma proves that `(D_s)_{red}` is a Cartan subgroup of `(H_s)_{red} ≅ G_s`:

**Lemma 1.11.** *Let `G` be a smooth and connected algebraic group defined over an algebraically closed field `k`, `D` a
smooth nilpotent algebraic subgroup containing a regular element `a` of `G(k)`. Then `D⁰` is contained in a Cartan
subgroup of `G`. If moreover `dim D` is equal to the nilpotent rank of `G`, then `D` is a Cartan subgroup of `G` (and
hence is connected).*

<!-- label: III.XVI.1.11 -->

<!-- original page 499 -->

Let `Z` be the center of `G`, `G′ = G/Z` (which is affine, Exp. XII 6.1), `a′`, `D′` the images of `a`, `D` in `G′`. It
follows immediately from the correspondence between Cartan subgroups of `G` and Cartan subgroups of `G′` (Exp. XII 6.6
e)) that `a′` is a regular element of `G′` and that it suffices to prove the lemma for the pair `D′, G′`; this allows
us to assume `G` affine.

Let `s` then be the semisimple component of `a`, which belongs to `D(k)` (*Bible* 4 th. 3) and is regular (*Bible* 7
th. 2 cor. 1). By *Bible* 6 th. 2, `s` centralizes `D⁰`, hence `D⁰` is contained in the connected centralizer of `s`,
which is a Cartan subgroup of `G` (*Bible* 7 th. 2). If now `dim D =` nilpotent rank of `G`, `D⁰` is therefore a Cartan
subgroup of `G`, equal to `Centr_G(T)`, where `T` is the unique maximal torus of `D⁰` (Exp. XII 6.6). But `D` is
nilpotent, hence centralizes `T` (*Bible* 6 th. 2), hence `D = D⁰`.

Let us now work with the group `G`. The group `C_t = u_t⁻¹(D_t)` is the unique Cartan subgroup of `G_t` containing `b`.
Let `C` be the schematic closure of `C_t` in `G`.

By functoriality of the schematic closure, `u|C` factors through `D`, so `u_s(C_s) ⊂ D_s`. Since `u_s` is an isomorphism
of `G_s` onto `(H_s)_{red}`, since `dim C_s = dim C_t = ν = dim D_s` (1.10), and since `D_s` is connected (1.11), `u_s`
furnishes an isomorphism of `(C_s)_{red}` onto `(D_s)_{red}`, hence `(C_s)_{red}` is a Cartan subgroup of `G_s`. <!--
original page 500 --> The following lemma shows that `C` is in fact a Cartan subgroup of `G`.

**Lemma 1.12.** *Let `S` be the spectrum of a discrete valuation ring, `G` an `S`-group prescheme smooth, of finite
type, `C` a group sub-prescheme of `G`, flat over `S`, such that the generic fiber `C_t` is a Cartan subgroup of `G_t`
and the geometric reduced closed fiber `(C_s)_{red}` is a Cartan subgroup of `G_s`. Then `C` is a Cartan subgroup of
`G`.*

<!-- label: III.XVI.1.12 -->

We must show that `C` is smooth over `S`, and it suffices to establish this point after a faithfully flat extension of
the base. The hypotheses on `C` imply that the nilpotent rank of the fibers of `G` is constant, and we may therefore
speak of the open set `U` of regular points of `G` (Exp. XV 7.3). Since `(C_s)_{red}` is a Cartan subgroup of `G_s`,
`C_s` contains a regular point `a_s` of `G_s`. But `C` is flat over `S`, so (EGA IV 14.5.8), replacing the base by a
faithfully flat extension if necessary, we may assume that `a_s` is an element of `G(s)` lifting to a section `a` of
`C(S)`. Since `U` is open and contains `a(s)`, `U` contains `a`. Let `C′` be the unique Cartan subgroup of `G`
containing `a` (Exp. XV 7.3). One necessarily has `C_t = C′_t`, and consequently `C′` and `C` coincide with the
connected component of the schematic closure of `C_t` in `G` (note that `C′` and `C` are flat over `S`).

<!-- original page 501 -->

**End of the proof of 1.3 a).** By hypothesis, the restriction of `u` to the Cartan subgroup `C` of `G` is an
immersion. It is clear that `h(S)` is contained in `u(C) = D`, hence `h` is the image of a section `g` of `C(S)`. QED.

**Proof of 1.3 b).**

We shall again use the valuative criterion of local properness (EGA IV 15.5) in the case of an immersion (resp. the
valuative criterion of properness (EGA II 7.3.6) in the case of a closed immersion). This reduces us to the case where
`S` is the spectrum of a complete discrete valuation ring with algebraically closed residue field. Let `s` be the
closed point and `t` the generic point of `S`. Replacing `H` by the schematic closure in `H` of `u_t(G_t)`, we may
assume that `H` is flat over `S` and that `u_t` is an isomorphism.

Let `G⁰` be the connected component of `G`. By 1.2 a) [^XVI-1], `u|G⁰` is an immersion; denote by `H⁰` the group sub-prescheme
of `H` image of `G⁰`. One has therefore `H⁰_s = (H_s)⁰_{red}`.

To verify the valuative criterion, we must show that every section `h` of `H` over `S` such that `h(S)` is contained in
`u(G)` in the case of an immersion (resp. every section `h` of `H` over `S` in the case of a closed immersion) is the
image of a section `g` of `G` over `S`.

Let `C` be a Cartan subgroup of `G`, `D = u(C)` the Cartan subgroup of `H⁰` image of `C`. <!-- original page 502 -->
The `S`-group `D′ = int(h)D` has connected fibers, hence its underlying space is contained in that of `H⁰`; moreover,
being smooth over `S`, it is reduced, and consequently `D′` is a smooth group sub-prescheme of `H⁰`. The fibers of `D′`
are Cartan subgroups of the fibers of `H⁰`, so `D′` is a Cartan subgroup of `H⁰`, and `C′ = u⁻¹(D′)` is a Cartan
subgroup of `G`. But `Transp^{str}_G(C, C′)` is smooth and surjective over `S` (Exp. XII 7.1 b)). Since `S` is henselian
with algebraically closed residue field, there exists `g ∈ G(S)` such that `int(g)C = C′`. Replacing `h` by
`u(g)⁻¹h`, we may assume that `h(t)` normalizes `D_t` (and that `h(s)` is the image of an element of the normalizer of
`C_s` in `G_s` in the case of an immersion). Let `N = Norm_G(C)`. By hypothesis `u|N` is an immersion (resp. a closed
immersion), so `h` is the image of a section of `N` over `S`, which completes the proof.

## 2. A representability theorem for quotients

<!-- label: III.XVI.2 -->

<!-- original page 503 -->

Let us "recall" the following result:

**Theorem 2.1.** *Let `S` be a prescheme, `X` and `Y` two `S`-preschemes, `f : X → Y` an `S`-morphism. Suppose we are
in one of the following two cases:*

<!-- label: III.XVI.2.1 -->

*a) The morphism `f` is locally of finite presentation.*

*b) The prescheme `S` is locally noetherian and `X` is locally of finite type over `S`.*

*Then the following conditions are equivalent:*

*i) There exist an `S`-prescheme `X′` and a factorization of `f`:*

```text
f : X ──f′──→ X′ ──f″──→ Y,
```

*where `f′` is a faithfully flat `S`-morphism, locally of finite presentation, and `f″` is a monomorphism.*

*ii) The (first) projection*

```text
p₁ : X ×_Y X ⟶ X
```

*is a flat morphism.*

*Moreover, if the preceding conditions are satisfied, `(X′, f′)` is a quotient of `X` by the equivalence relation
defined by `f` (for the fpqc topology), so that the factorization `f = f″ ∘ f′` of i) is unique up to isomorphism.*

The proof of this delicate theorem will be found in EGA V; one may also consult the lecture by J.-P. Murre, *Séminaire
Bourbaki*, May 1965, No. 294 th. 2 cor. 2, where the case `Y` locally noetherian, `X` of finite type over `Y` is
treated. <!-- original page 504 --> We shall see that one may reduce to this case.

Let us first make some remarks:

a) i) ⇒ ii) is trivial. Indeed, the first projection

```text
p′₁ : X ×_{X′} X ⟶ X
```

factors through `X ×_Y X`:

```text
p′₁ : X ×_{X′} X ──u──→ X ×_Y X ──p₁──→ X.
```

The morphism `u` is an isomorphism, since `f″` is a monomorphism, and `p′₁` is flat, since `f′` is flat, so `p₁` is
flat.

b) The assertions of 2.1 are local on `Y` (and so are local on `S`); they are also local on `X`, as follows easily from
the fact that a flat morphism locally of finite presentation is open (EGA IV 11.3.1).

c) Under the hypotheses of 2.1 a), in view of the foregoing, we are reduced to the case where `X` and `Y` are affine
and `f` of finite presentation. Replacing `S` by `Y`, we may assume `X` and `Y` of finite presentation over `S`. We
then reduce to the case `S` noetherian thanks to EGA IV 11.2.6.

d) Under the hypotheses of 2.1 b), we may assume `S`, `X`, `Y` affine, `S` noetherian and `X` of finite type over `S`.
Consider `Y` as a filtered projective limit of affine schemes `Y_i` of finite type over `S`. The schemes `X ×_{Y_i} X`
form a decreasing filtered family of closed subschemes of `X ×_S X`, whose projective limit is `X ×_Y X`. Since
`X ×_S X` is noetherian, one has `X ×_{Y_i} X = X ×_Y X` for `i` large enough, so that

```text
f_i : X ──f──→ Y → Y_i
```

satisfies the hypotheses of 2.1 ii) if `f` does. <!-- original page 505 --> Since the equivalence relation defined by
`f` on `X` coincides with that defined by `f_i`, it is clear that it suffices to prove ii) ⇒ i) for `f_i`, which
reduces us to the case where `Y` is of finite type over `S`.

### Application to group preschemes

**Theorem 2.2.** *Let `S` be a prescheme, `G` an `S`-group prescheme locally of finite presentation over `S`, acting on
an `S`-prescheme `X`. Let `ξ ∈ X(S)` be a section of `X` over `S` such that the stabilizer `H` of `ξ` in `G` is an
`S`-group sub-prescheme of `G`, flat over `S`. Then, if `X` is locally of finite type over `S`, or if `S` is locally
noetherian, the homogeneous space quotient `G/H` is representable by an `S`-prescheme, locally of finite presentation
over `S`, and the `S`-morphism*

<!-- label: III.XVI.2.2 -->

```text
f : G ⟶ X,    g ↦ g · ξ
```

*factors as*

```text
       G
      ╱ ╲
     p   f
    ╱     ╲
   ↓       ↘
  G/H ──i──→ X,
```

*where `p` is the canonical projection, which is a faithfully flat morphism locally of finite presentation, and `i` is
a monomorphism. (For definiteness, we have assumed that `G` acts on the left on `X`.)*

**Proof.** The morphism `f` makes `G` into an `X`-prescheme. <!-- original page 506 --> By definition of the stabilizer
of `ξ`, the morphism

```text
G ×_S H ⟶ G ×_X G,    (g, h) ↦ (g, gh)
```

is an isomorphism. Since `H` is flat over `S`, `G ×_S H` is flat over `G`, so the first projection
`p₁ : G ×_S G → G` is a flat morphism. Furthermore, if `X` is locally of finite type over `S`, `f` is locally of finite
presentation (EGA IV 1.4.3 v)); otherwise `S` is assumed locally noetherian. It then suffices to apply 2.1 to the
morphism `f`.

It remains to see that `G/H` is locally of finite presentation over `S`, but this follows immediately from Exp. V 9.1.

**Corollary 2.3.** *Let `S` be a prescheme, `G` and `H` two `S`-group preschemes, `u : G → H` an `S`-homomorphism.
Suppose `G` locally of finite presentation over `S` and that either `H` is locally of finite type over `S`, or `S` is
locally noetherian. Then, if `K = Ker(u)` is flat over `S`, the quotient group `G/K` is representable by an `S`-group
prescheme locally of finite presentation over `S`, and `u` factors as*

<!-- label: III.XVI.2.3 -->

```text
       G ──u──→ H
       ╲       ↗
        p     i
         ↘   ↗
          G/K
```

*where `p` is the canonical projection and `i` a monomorphism.*

**Proof.** One applies 2.2 with `X = H` and `ξ` the unit section of `H`.

**Corollary 2.4.** *Let `S` be a prescheme, `G` an `S`-group prescheme of finite presentation over `S`, `H` an
`S`-group prescheme smooth over `S` with connected fibers (hence of finite presentation over `S`, by VI_B 5.5),
`i : H → G` a monomorphism of `S`-groups, so that `H` is a subgroup of `G`.*

<!-- label: III.XVI.2.4 -->

*Suppose that `N = Norm_G(H)` (which is representable by a closed group sub-prescheme of `G`, of finite presentation
over `S` (Exp. XI 6.11)) is flat over `S`. Then `G/N` is representable by an `S`-prescheme of finite presentation over
`S` and quasi-projective over `S`.*

All the assertions to be proved, except the last, are local on `S`. To establish them, we may therefore assume `S`
quasi-compact and the relative dimension of `H` over `S` constant and equal to `r`. Let us proceed as in XV § 5. For
every integer `n > 0`, let `G_{(n)}` (resp. `H_{(n)}`) be the `n`th normal invariant of the unit section of `G` (resp.
of `H`) (EGA IV 16). The sheaf of `𝒪_S`-modules `H_{(n)}` is a quotient of `G_{(n)}`, and `H` being smooth over `S` of
dimension `r`, `H_{(n)}` canonically defines an element `ξ_n` of `X_n = Grass_{ϕ(n,r)} G_{(n)}` (EGA I 2nd ed. § 9)
for a suitable integer `ϕ(n, r)`. On the other hand, `G` acts naturally on `G_{(n)}` (and hence also on `X_n`) via the
representation

```text
G ⟶ Aut_{S-gr}(G),    g ↦ int(g).
```

Since `S` is quasi-compact, there exists an integer `m` such that for `n ⩾ m` one has

```text
N = Norm_G(H) = Norm_G H_{(n)}    (Exp. XI 6.11 b)).
```

That is to say, `N` is the stabilizer of `ξ_n` for `n` large. <!-- original page 507 --> The representability of `G/N`
therefore follows from 2.2. The fact that `G/N` is of finite presentation over `S` is a consequence of Exp. V 9.1. It
remains to see that `G/N` is quasi-projective over `S`, and for that we shall exhibit a canonical invertible sheaf on
`G/N`, `S`-ample. Consider the functor `F : (Sch/S)° → Ens` such that for every `S`-prescheme `T` one has

```text
F(T) =  set of T-subgroups H of G_T, representable, smooth over T,
        with connected fibers.
```

Such a group `H` is of finite presentation over `S` (Exp. VI_B 5.5) and `H → G_T` is a quasi-affine morphism (EGA IV
8.11.2). By effective descent of quasi-affine morphisms (SGA 1, VIII 7.9), one deduces that `F` is a sheaf for the fpqc
topology. Since `G/N` is the sheaf associated to a subfunctor of `F`, one sees that there is a canonical monomorphism
`G/N → F`. There exists therefore a subgroup `H₀` of `G ×_S (G/N)`, representable, smooth over `G/N`, with connected
fibers, "universal" for the functor `G/N`. I claim that the invertible sheaf `L = (det(Lie H₀))⁻¹` is `S`-ample. In
this form, the assertion becomes local on `S`, and the proof is analogous to the one given in (Exp. XV 5.8).

The following corollary was announced in Exp. XIV 4.8 bis.

**Corollary 2.5.** *Let `S` be a prescheme, `G` an `S`-group prescheme smooth and of finite presentation over `S`, with
connected fibers, `P` a parabolic subgroup of `G` (Exp. XIV 4.8 bis). Then `G/P` is representable by an `S`-prescheme
smooth and projective over `S`.*

<!-- label: III.XVI.2.5 -->

<!-- original page 508 -->

It only remains to show (*loc. cit.*) that `G/P` is representable by an `S`-prescheme quasi-projective, of finite
presentation, which follows from 2.4, given that `P = Norm_G(P)` (*loc. cit.*) is therefore flat over `S`.

## 3. Groups with flat center

<!-- label: III.XVI.3 -->

<!-- original page 509 -->

**Proposition 3.1.** *Let `S` be a prescheme, `G` an `S`-group prescheme smooth and of finite presentation over `S`,
with connected fibers. Suppose that the center `Z` of `G` (which is representable by Exp. XI 6.11) is flat over `S`.
For every integer `n > 0`, let `G_{(n)}` denote the locally free `𝒪_S`-module equal to the `n`th normal invariant of
`G` along the unit section, and let `ρ_n` be the natural "adjoint representation" of `G` in `GL_S(G_{(n)})`. Then:*

<!-- label: III.XVI.3.1 -->

*a) The quotient `G′ = G/Z` is representable by an `S`-group prescheme, smooth, of finite presentation over `S`,
quasi-affine, with affine connected fibers.*

*b) The representation `ρ_n` factors through `G′`:*

```text
        G ──ρ_n──→ GL_S(G_{(n)})
        ╲          ↗
         ↘        ↗ i_n
          G/Z ──
```

*If `S` is quasi-compact, `i_n` is a monomorphism for `n` large enough.*

*c) The functor `𝒯_{G′}` of subtori of `G′` is representable by an `S`-prescheme, smooth over `S`, which is a sum of a
family of preschemes affine over `S` if `S` is quasi-compact.*

**Proof.** The assertions of a) are local on `S`, which allows us to assume `S` quasi-compact. By Exp. XI 6.11 b), `Z`
is equal to `Ker ρ_n` for `n` large enough, so this kernel is flat over `S`. The fact that `G/Z` is representable and
that <!-- original page 510 --> `i_n` is a monomorphism therefore follows from 2.3. Since `G` is smooth and of finite
presentation over `S`, the same is true of `G′` (Exp. VI_B § 9). The group `GL_S(G_{(n)})` is affine over `S`, and a
monomorphism of finite presentation is quasi-affine (EGA IV 8.11.2), hence `G′` is quasi-affine over `S` and has affine
fibers. Since `G′` is smooth over `S`, the functor `𝒯_{G′}` is formally smooth (Exp. XI 2.1 bis). Taking into account
Exp. XI 4.6 and 4.3, the assertions of 3.1 c) will therefore follow from the next lemma:

**Lemma 3.2.** *Let `S` be a prescheme, `G` and `H` two `S`-group preschemes of finite presentation over `S`,
`u : G → H` an `S`-group monomorphism, `𝒯_G` (resp. `𝒯_H`) the functors of subtori of `G` (resp. of `H`) (cf. Exp. XV §
8). Then the map `T ↦ u(T)` defines a monomorphism (XV 8.3 c))*

<!-- label: III.XVI.3.2 -->

```text
ũ : 𝒯_G ⟶ 𝒯_H
```

*which is representable by a closed immersion of finite presentation.*

By the usual procedure, we are reduced to the following problem: let `T` be a subtorus of `H`, `T′ = G ×_T H` its
inverse image in `G`, `u_T : T′ → T` the `S`-group monomorphism deduced from `u`. One must show that the `S`-functor
`∏_{T/S}(T′/T)` is representable by a closed sub-prescheme of `S`, of finite presentation. But `T`, being a torus, is
smooth over `S` with connected fibers, and it suffices to apply Exp. XI 6.10.

<!-- original page 511 -->

**Theorem 3.3.** *Let `S` be a prescheme, `G` an `S`-group prescheme smooth and of finite presentation over `S`, with
connected fibers, `Z` the center of `G`. Suppose that `Z` is flat over `S` and that the unipotent rank (Exp. XV 6.1
ter) of `G` is equal to that of `Z`. Then:*

<!-- label: III.XVI.3.3 -->

*a) The group `G′ = G/Z` is representable, and if `S` is quasi-compact, the canonical morphism
`i_n : G′ → GL_S(G_{(n)})` (cf. 3.1 b)) is an immersion for `n` large.*

*b) The group `G′` is quasi-affine over `S`, with affine fibers, the center of `G′` is the unit group, and `G′` has
zero unipotent rank.*

*c) The group `G′` possesses locally for the étale topology maximal tori, and these are also Cartan subgroups of `G′`.
The functor `𝒯ℳ_{G′}` of maximal tori of `G′` (Exp. XV § 8) is representable by an `S`-prescheme smooth and affine over
`S`.*

*d) The group `G` possesses locally for the étale topology Cartan subgroups, and the functor `𝒞_G` of Cartan subgroups
of `G` is representable by an `S`-prescheme, smooth and affine over `S`.*

**Proof.** By 3.1, the group `G′` is representable by an `S`-prescheme, smooth and quasi-affine over `S`, with affine
fibers. In view of the correspondence between Cartan subgroups of the fibers of `G` and of the fibers of `G′` (Exp.
XII 6.6 e)), the hypothesis on the unipotent rank of `Z` implies that `G′` has zero unipotent rank. Using now <!--
original page 512 --> Exp. XV 8.18, one sees that `G′` possesses locally for the étale topology maximal tori. The fact
that `i_n` is an immersion for `n` large then follows from 3.1 b) and 1.4 a). This completes the proof of a).

Let us now show c). Since `G′` has zero unipotent rank, it is clear that every maximal torus of `G′` is also a Cartan
subgroup of `G′`. The functor of maximal tori of `G′` is representable by a sub-prescheme both open and closed of the
functor of subtori of `G′`; moreover it is of finite type over `S` (Exp. XV 8.15); it follows from 3.1 c) that this
functor is representable by an `S`-prescheme, smooth and affine over `S`.

Since `G′` possesses, locally for the étale topology, Cartan subgroups, the same is true of `G`, and the functor of
Cartan subgroups of `G` is canonically isomorphic to that of `G′` (Exp. XV 7.3 iv)), so c) ⇒ d).

It remains to show b), and more precisely, it remains to prove that the center `Z′` of `G′` is the unit group. Since
`Z′` is representable (Exp. XI 6.11) and of finite presentation over `S`, it suffices to show that the fibers of `Z′`
are reduced to the unit group (Exp. VI_B 2.9), which reduces us to the case where `S` is the spectrum of an
algebraically closed field. The center `Z′` is evidently contained in every Cartan subgroup of `G′`, hence in every
maximal torus of `G′` by c), and is therefore of multiplicative type. Moreover, we shall see in Exp. XVII that if `G`
is a connected algebraic group with center `Z`, the center `Z′` of `G/Z` is unipotent. In the present case, `Z′` being
both of multiplicative type and unipotent, is reduced to the unit group (cf. Exp. XVII).

<!-- original page 513 -->

### Examples of groups whose center is flat

**Proposition 3.4.** *Let `S` be a prescheme, `G` an `S`-group prescheme of finite presentation over `S`, smooth, with
connected fibers, `Z` the center of `G`. Then `Z` is flat over `S` in the following two cases:*

<!-- label: III.XVI.3.4 -->

*a) The unipotent rank `ρ_u` (Exp. XV 6.1 ter) of the fibers of `G` is zero.*

*b) i) `S` is reduced.*

*ii) The dimension of the fibers of `Z` is a locally constant function on `S`.*

*iii) The unipotent rank of `G` is equal to the unipotent rank of `Z`.*

**Proof of 3.4 a).** We shall prove at the same time:

**Proposition 3.5.** *Under the hypotheses of 3.4 a), suppose moreover that `G` possesses a maximal torus `T` and let
`C = Centr_G(T)` be the Cartan subgroup of `G` associated to `T` (Exp. XII 7.1). Then:*

<!-- label: III.XVI.3.5 -->

*(i) `Z ∩ T` is a subgroup of multiplicative type of `G`.*

*(ii) `C` is commutative and equal to `T · Z`.*

*(iii) If the quotients `Z/Z ∩ T` and `C/T` are representable, they are representable by abelian preschemes (i.e.
`S`-group preschemes, smooth over `S`, whose fibers are abelian varieties) and the canonical monomorphism
`Z/Z ∩ T → C/T` is an isomorphism.*

Using the general properties of passage to the limit proved in Exp. VI_B § 10 and Exp. XV 6.2, 6.3, and 6.3 bis, we
reduce as usual to the case <!-- original page 514 --> where `S` is noetherian (note that the assertions of 3.4 and 3.5
are local on `S`). We noted in 3.1 that the hypotheses on `G` imply that `Z` is representable. To show that `Z` is flat
over `S`, we reduce by EGA 0_III 10.2.6 to the case where `S` is local artinian. But then, `G` being smooth, `G`
possesses locally for the étale topology maximal tori (Exp. XV 8.17). Replacing `S` by a finite flat extension if
necessary (which is allowable for proving that `Z` is flat), we may assume that `G` possesses a maximal torus `T`.

Let us show, in the same way, that to prove 3.5 we may reduce to the case `S` artinian.

i) Since `Z` is closed in `G` (Exp. XI 6.11), `Z ∩ T` is a closed group subscheme of `T`. It follows from Exp. X 4.8
b) that `Z ∩ T` is of multiplicative type if and only if it is flat over `S`. As before, it suffices to establish that
`Z ∩ T` is flat when `S` is artinian.

ii) Since `G` has zero unipotent rank, every Cartan subgroup `C` of `G` satisfies the hypotheses of Lemma 1.6, hence is
commutative. The fact that `C = T · Z` will follow from iii).

iii) If `C/T` is representable, `C/T` is smooth over `S` (Exp. VI_B 9) and its fibers are abelian varieties (1.7), so
`C/T` is an abelian prescheme. To show that the canonical monomorphism

```text
i : Z/Z ∩ T ⟶ C/T
```

is an isomorphism, it suffices to verify this when `S` is local artinian. <!-- original page 515 --> Indeed, one will
then deduce in succession that `Z/Z ∩ T` is flat over `S` (EGA 0_III 10.2.6), then that `i` is flat (EGA IV 11.3.10),
then that `i` is an open immersion (EGA IV 17.9.1), then that `i` is an isomorphism (since `C/T` has connected fibers).

We henceforth assume that `S` is local artinian with closed point `s` and that `G` possesses a maximal torus `T`. Let
`C = Centr_G(T)`. The group `C` is a Cartan subgroup of `G` (Exp. XII 7.1) and majorizes `Z`.

The algebraic group `M_s = Z_s ∩ T_s` is a subgroup of multiplicative type of `G_s` which is central. Since `T` is
smooth over `S`, `M_s` lifts to a group subscheme `M` of `T`, of multiplicative type (Exp. IX 3.6 bis) and contained in
the center of `G` (Exp. IX 3.9), hence contained in `Z ∩ T`. Since `S` is artinian and `M` and `T` are flat over `S`,
the quotient groups `Z ∩ T/M`, `Z′ = Z/M`, and `A = C/T` are representable (Exp. VI_A §§ 4 and 5). By construction,
`(Z ∩ T/M)_s` is the unit group, so `Z ∩ T = M` (Exp. VI_B 2.9); a fortiori it is flat over `S`, which proves 3.5 i).

By passage to the quotient, one has a canonical monomorphism `i : Z′ → A`, which is therefore a closed immersion (Exp.
VI_B 1.4.2). We have already noted that `A` is an abelian scheme. It remains to show that `i` is an isomorphism. This
will prove 3.5 iii) and will imply that `Z′` is flat over `S`, hence that `Z` is flat over `S` (as an extension of `Z′`
by the flat group `M` (Exp. VI_B § 9)). Since `Z_s` has the same abelian rank as `G_s` <!-- original page 516 --> (Exp.
XII 6.1), `i_s` is an epimorphism, hence an isomorphism. Let `q` be an integer `> 0`, invertible on `S`. By the density
theorem of 1.6 iii), to see that `i(Z′) = A`, it suffices to show that for every integer `n` equal to a power of `q`,
`i(Z′)` majorizes `_n A`. Now let `M⁰_s` be the connected component of `M_s`. It is immediate by duality that raising
to the `q`-th power in `M⁰_s` is an epimorphism. One deduces immediately that if `m₀` is the exponent of `q` in the
factorization into prime factors of `card(M_s / M⁰_s)`, the image of `_{nm₀}Z_s` in `A_s ≅ Z_s/M_s` majorizes `_n A_s`.
There exists therefore a subgroup of multiplicative type `M_s(n)` of `Z_s` whose image in `A_s` is `_n A_s`. As before,
one sees that `M_s(n)` lifts to a subgroup of `G`, central and of multiplicative type, `M(n)`. The image of `M(n)` in
`A` is a subgroup of multiplicative type (Exp. IX 6.8), hence necessarily equal to `_n A`, since it is so on the
reduced fiber (Exp. IX 5.1 bis). This completes the proof of 3.4 a) and of 3.5.

**Proof of 3.4 b).** The assertion to be proved is local on `S`; we may therefore assume `S` affine with ring `A`.
Considering `A` as an inductive limit of its sub-`ℤ`-algebras of finite type, we reduce as above to the case where `S`
is noetherian reduced.

To show that `Z` is flat, we have at our disposal a valuative criterion of flatness (EGA IV 11.8.1), which allows us
to reduce to the case where `S` is the spectrum of a complete discrete valuation ring with algebraically closed residue
field, with generic point `t` and closed point `s`. Let `Z′` be the schematic closure in `Z` of `Z_t`. We must show
that `Z′ = Z`, and it suffices even to show that `Z_s = Z′_s` (Exp. VI_B 2.6). <!-- original page 517 --> By (Exp.
VI_B § 4), one has the inequalities

```text
dim Z_t = dim Z′_t = dim Z′_s ⩽ dim Z_s.
```

But by hypothesis `dim Z_t = dim Z_s`, hence `dim Z′_s = dim Z_s` and consequently `Z′_s` majorizes `(Z_s)⁰_{red}`. It
follows that `G′_s = G_s / Z′_s` is affine (Exp. XII 6.1). In view of the correspondence between Cartan subgroups of `G`
and of `G′` (Exp. XII 6.6 e)), hypothesis 3.4 iii) implies that the unipotent rank of `G′_s` is zero, and consequently
its Cartan subgroups are also its maximal tori. The image `Z″_s` of `Z_s` in `G′_s` is a central algebraic subgroup of
`G′_s`, hence contained in every Cartan subgroup of `G′_s`, that is, in every maximal torus; `Z″_s` is therefore a
subgroup of multiplicative type of `G′_s`. Under these conditions, we shall show in (Exp. XVII § 7) that there exists a
finite subgroup of multiplicative type `M_s` of `Z_s` whose image in `Z_s/Z′_s` is `Z″_s` (we used this fact in the
proof of 3.4 a) when `Z″_s` is étale). Since `G` is smooth over `S` and `S` is the spectrum of a complete local ring,
`M_s` lifts to an `S`-subgroup of multiplicative type `M` of `G` (Exp. IX 3.6 bis and Exp. XV 1.6 b)) which is central
(Exp. IX 5.6 a)). So `M_t` is contained in `Z′_t = Z_t`, and since `M` is flat, `M` is contained in `Z′`. The group
`M_s` is therefore contained in `Z′_s`, but this implies that `Z″_s` is the unit group, i.e. `Z_s = Z′_s`. This
completes the proof of 3.4 b).

### Example of a smooth group prescheme with connected fibers whose center is not flat

Let `S` be the spectrum of a discrete valuation ring `A`, `π` a uniformizer of `A`, <!-- original page 518 --> `t` the
generic point of `S`, `s` the closed point. Let `G` be the smooth and affine `S`-group with ring
`B = A[T, T⁻¹, U]/F` with `F = 1 − T + πU`, the composition law being defined by

```text
((t, u), (t′, u′)) ↦ (tt′, πuu′ + u + u′).
```

The generic fiber `G_t` is therefore isomorphic to the multiplicative group `(𝔾_m)_t`, while the closed fiber `G_s` is
isomorphic to the additive group `(𝔾_a)_s`. The function `T` is invertible in `Γ(G, 𝒪_G)` and defines an `S`-group
morphism `ϕ : G → (𝔾_m)_S` which is an isomorphism on the generic fiber and the zero morphism on the closed fiber. The
datum of `ϕ` allows one to construct the semidirect product group `H = G · (𝔾_a)_S` (note that `(𝔾_m)_S` acts on
`(𝔾_a)_S`). The center `Z` of `H` is the unit group on the generic fiber and is equal to `H_s` on the closed fiber,
hence is not flat over `S`.

## 4. Groups with affine fibers, of zero unipotent rank

<!-- label: III.XVI.4 -->

<!-- original page 519 -->

**Theorem 4.1.** *Let `S` be a prescheme, `G` an `S`-group prescheme smooth over `S`, of finite presentation, with
affine, connected fibers, of zero unipotent rank (Exp. XV 6.1 ter). Then:*

<!-- label: III.XVI.4.1 -->

*a) The center `Z` of `G` is a group of multiplicative type (and is therefore a reductive center of `G` (Exp. XII
4.1)).*

*b) `G` satisfies conditions a) to d) of 3.3.*

*c) `G` possesses locally for the étale topology maximal tori, and these are also Cartan subgroups of `G`. The functor
`𝒯ℳ_G` of maximal tori of `G` is representable by an `S`-prescheme smooth and affine over `S`.*

*d) `G` is quasi-affine over `S`. Moreover, if `T` is a maximal torus of `G`, `N = Norm_G T` its normalizer in `G`,
`W = N/T` the Weyl group relative to `T`, the following conditions are equivalent:*

*(i) `G` is affine over `S`.*

*(ii) `G′ = G/Z` is affine over `S`.*

*(iii) `N` is affine over `S`.*

*(iv) `W` is affine over `S`.*

*These conditions are always realized if `S` is locally noetherian of dimension `⩽ 1`.*

**Proof.** Since `G` has affine fibers (and so abelian rank zero) and zero unipotent rank, `G` possesses locally for
the étale topology maximal tori (Exp. XV 8.18), and <!-- original page 520 --> every maximal torus of `G` is evidently
a Cartan subgroup of `G`, which proves the first part of c). To see that `Z` is of multiplicative type, we may assume,
by what precedes, that `G` possesses a maximal torus `T`. Since `T` is also a Cartan subgroup, `T` majorizes `Z` (since
`T = Centr_G(T)` by Exp. XII 7.1), and `Z = Z ∩ T` is of multiplicative type by 3.5 i). This proves a). Assertion b) is
clear, given a). On the other hand the functor `𝒯ℳ_G` is isomorphic to the functor of Cartan subgroups of `G` (Exp.
XII 7.1), hence is smooth and affine over `S` (3.3 c)), which completes the proof of c). It remains to prove d).

**Proof of d).** Since `G′` is quasi-affine (3.5 b)) and `Z` is of multiplicative type, hence affine over `S`, `G` is
quasi-affine (Exp. VI_B § 9).

i) ⇔ ii). If `G` is affine, `G′` is affine by Exp. IX 2.3. If `G′` is affine, `G` is affine as an extension of an
affine group by an affine group (Exp. VI_B § 9).

i) ⇔ iii). If `G` is affine, `N` is affine since closed in `G` (Exp. XI 6.11 a)). Moreover `G/N` is isomorphic to the
functor `𝒯ℳ_G` (conjugacy of maximal tori, cf. Exp. XII 7.1 b)), so is affine over `S` by c). Hence if `N` is affine
over `S`, `G` is affine, as an "extension" of an affine homogeneous space by an affine group (Exp. VI_B § 9).

iii) ⇔ iv). If `N` is affine, `W = N/T` is affine (Exp. IX 2.3) and conversely by Exp. VI_B § 9.

<!-- original page 521 -->

Moreover, `N/T` is representable by an `S`-group prescheme, étale, separated over `S`, of finite type (Exp. XV 7.1 iv)),
hence quasi-finite over `S`. The last assertion of d) will therefore follow from the following lemma, applied with
`X = W` and `Y = S`:

**Lemma 4.2.** *Let `S` be a locally noetherian prescheme of dimension 1, `X` and `Y` two `S`-preschemes locally of
finite type over `S`, `u : X → Y` an `S`-morphism quasi-finite and separated. Suppose that for every point `s` of `S`
the morphism `u_s : X_s → Y_s` deduced from `u` by the base change `Spec κ(s) → S` is finite. Then `u` is an affine
morphism.*

<!-- label: III.XVI.4.2 -->

The assertion to be proved is local on `Y`, which allows us to assume `Y` (and hence also `X`) of finite type over `S`.
By EGA IV 8, one sees that it suffices to prove 4.2 when `S` is the spectrum of a local ring `A`. By fpqc descent we
may assume `A` complete, then `A` reduced (EGA II 1.6.4), then `A` normal (Nagata's theorem (EGA 0_IV 22) and
Chevalley's theorem (EGA II 6.7.1)). If `A` is a field, `u` is finite by hypothesis, hence affine. Otherwise `A` is a
discrete valuation ring; let `s` be the closed point of `S`, `t` the generic point, `π` a uniformizer of `A`. Let `y`
be a point of `Y_s`. Applying EGA IV 8 once more, we may replace `Y` by the spectrum `Y′` of `𝒪_{Y,y}` and `X` by
`X′ = X ×_Y Y′`; we may even assume `𝒪_{Y,y}` complete. Since `u` is quasi-finite and separated, by EGA II 6.2.6 `X′`
is a sum of two schemes `X₁` and `X₂` with `X₁` finite over `Y′` (hence affine) and `X₂` such that `u(X₂)` does not
contain the closed point `y` of `Y′`. I claim that under these conditions `X₂` does not meet the closed fiber `X′_s`.
Indeed, by hypothesis <!-- original page 522 --> `X′_s → Y′_s` is finite, hence the restriction of this morphism to
the closed subset `(X₂)_s` is finite and its image in `(Y′)_s` is a closed subset. Since this image does not contain
the closed point of the local scheme `(Y′)_s`, `(X₂)_s` is empty. Since `u_t` is finite, the restriction to
`(X₂)_t = X₂` of the morphism `X′_t → Y′_t` is finite. Moreover, one has `Y′_t = Y′_π`, so the open immersion
`Y′_t → Y′` is affine. In short, the composed morphism `X₂ → Y′_t → Y′` is affine, and it follows that the morphism
`X′ = X₁ ⊔ X₂ → Y′` is affine.

**Corollary 4.3.** *Let `S` be a prescheme, `G` an `S`-group prescheme smooth and of finite presentation over `S`, with
affine, solvable, connected fibers, of zero unipotent rank. Then `G` is affine over `S`. If moreover the center of `G`
is the unit group and if `S` is quasi-compact, the canonical morphism `i_n : G → GL_S(G_{(n)})` (cf. 3.1 b)) is a
closed immersion for `n` large enough.*

<!-- label: III.XVI.4.3 -->

To prove that `G` is affine over `S`, we may assume that `G` possesses a maximal torus `T` (4.1 c)). Since `G` has
solvable fibers, the Weyl group relative to `T` is the unit group (*Bible* 6 th. 1 cor. 3) and condition 4.1 d) iv) is
satisfied. If the center of `G` is the unit group, `i_n` is a monomorphism for `n` large enough (3.1), hence is a
closed immersion (1.5 b)).

## 5. Application to reductive and semisimple groups

<!-- label: III.XVI.5 -->

<!-- original page 523 -->

**Definition 5.1.** *An `S`-group prescheme `G` is said to be reductive (resp. semisimple) if `G` is smooth and affine
over `S`, with reductive (resp. semisimple) fibers.*

<!-- label: III.XVI.5.1 -->

**5.1.1.** Reductive groups will be systematically studied from Exp. XIX onwards. In this section, we shall need the
following properties, which will be proved in Exp. XIX (without using the developments of the present Exposé).

<!-- label: III.XVI.5.1.1 -->

a) *Let `S` be a prescheme, `G` an `S`-group prescheme smooth and affine over `S`, with connected fibers, `s` a point
of `S` such that `G_s` is reductive (resp. semisimple). Then there exists a neighborhood `U` of `s` such that `G|U` is
reductive (resp. semisimple).*

b) *If `G` is reductive, `G` possesses locally for the étale topology maximal tori, and if `T` is a maximal torus of
`G`, the Weyl group `W = Norm_G(T)/T` is finite over `S`.*

c) *A reductive group has zero unipotent rank.*

This being admitted, we propose to improve assertion a) above.

**Theorem 5.2.** *Let `S` be a prescheme, `G` an `S`-group prescheme smooth and of finite presentation over `S`, with
connected fibers, `s` a point of `S`. Then:*

<!-- label: III.XVI.5.2 -->

*(i) If the fibers of `G` are affine and `G_s` is reductive, there exists an open neighborhood `U` of `s` such that
`G|U` is reductive.*

*(ii) If `G_s` is semisimple, there exists an open neighborhood `U` of `s` such that `G|U` is semisimple.*

<!-- original page 524 -->

Using Exp. XV 6.2 i) and Exp. VI_B § 10, one reduces to the case where `S` is noetherian.

In case (ii), consider the center `Z` of `G`, which is representable (Exp. XI 6.11 a)). Since `G_s` is semisimple, it
is well known that `Z_s` is finite. Consequently (Exp. VI_B § 4), there exists a neighborhood `U` of `s` such that `Z`
is quasi-finite over `U`. For every point `t` of `U`, `G_t` is then affine (Exp. XII 6.1). Replacing `S` by a smaller
open if necessary, we may therefore assume that the fibers of `G` are affine, both in case (ii) and in case (i).

To prove 5.2 it suffices, by a), to prove that `G` is affine over `S`. Since `G` has affine fibers, we know that the
functor of subtori of `G` is representable by a smooth `S`-prescheme (Exp. XV 8.11 and 8.9). Replacing `S` by an étale
extension covering `s` (which is allowable), we may therefore assume that there exists a subtorus `T` of `G` such that
`T_s` is a maximal torus of `G_s`. But then `C = Centr_G(T)` is a smooth subgroup of `G`, with connected fibers,
majorizing `T`, such that `C_s = T_s` (since `C_s` is a Cartan subgroup of `G_s` and `G_s` has zero unipotent rank by
c)). It follows that `C = T`, hence `T` is a Cartan subgroup and a maximal torus of `G`; a fortiori, the unipotent
rank of `G` is zero and one may apply 4.1.

By 4.1 d), it suffices to show that the Weyl group `W` relative to `T` is affine over a neighborhood `U` of `s`. In
fact we shall see that `W` is even finite over a neighborhood of `s`. Since `W` is quasi-finite over `S` (Exp. XV 7.1
iv)), to say that `W` is finite over a neighborhood `U` of `s` is equivalent to saying that the morphism `W → S` is
proper at `s` (EGA IV 15.7 and EGA III 4.4.2); to establish this we have at our disposal <!-- original page 525 -->
the valuative criterion of local properness (EGA IV 15.7), which reduces us to the case where `S` is the spectrum of a
discrete valuation ring, with closed point `s`. But then, by the last assertion of 4.1 d), `G` is affine over `S`, and
we may apply property a) recalled above to conclude that `G` is reductive (resp. semisimple). Using now property b),
we conclude that `W` is indeed finite over `S`, which completes the proof of 5.2.

## 6. Applications: extension of certain rigidity properties of tori to groups of zero unipotent rank

<!-- label: III.XVI.6 -->

<!-- original page 526 -->

**Proposition 6.1.** *Let `S` be a prescheme, `G` an `S`-group prescheme smooth over `S`, of finite presentation, with
connected affine fibers, and whose center is of multiplicative type (for example `G` of zero unipotent rank, cf. 4.1
a)). Then every closed normal subgroup `K` of `G`, of finite presentation over `S`, quasi-finite over `S`, is finite
over `S`.*

<!-- label: III.XVI.6.1 -->

Indeed, for every geometric point `s` above `S`, `(K_s)_{red}` is a finite étale subgroup of `G_s`, normal hence
central (since `G_s` is connected). Consequently `K₀ = Z ∩ K` (where `Z` denotes the center of `G`) has the same
underlying space as `K`, and it suffices to show that `K₀` is finite over `S`. Now `K₀` is a closed, quasi-finite
subgroup of the multiplicative-type group `Z`, hence is finite, as one sees immediately (locally on `S`, `K₀` will be
majorized by `_n Z` for a suitable integer `n`, and `_n Z` is finite over `S`).

**Corollary 6.2.** *Let `S` and `G` be as above, `K` an `S`-group sub-prescheme of `G`, of finite presentation over
`S`, normal and closed in `G`, `s` a point of `S`. If `K_s` is finite (resp. is the unit group), there exists an open
neighborhood `U` of `s` such that `K|U` is finite over `S` (resp. is the unit group).*

<!-- label: III.XVI.6.2 -->

In view of the upper semi-continuity of the dimension of the fibers of `K` (Exp. VI_B § 4), we may already assume,
replacing `S` by a smaller open if necessary, that `K` is quasi-finite over `S`, hence finite (6.1). <!-- original page
527 --> If moreover `K_s` is the unit group, one deduces easily by Nakayama's lemma that `K` is the unit group over
`Spec 𝒪_s`, hence over a neighborhood of `s`.

**Proposition 6.3.** *Let `S` be a prescheme, `G` an `S`-group prescheme smooth and of finite presentation over `S`,
with affine, connected fibers, of zero unipotent rank, `H` an `S`-group prescheme, `s` a point of `S`,
`u : G → H` an `S`-group morphism such that `Ker u_s` is central. Suppose moreover that `H` is of finite presentation
over `S` or that `S` is locally noetherian and `G` is locally of finite type over `S`. Then there exists an open
neighborhood `U` of `s` such that if `K = Ker u`, `K|U` is central, of multiplicative type. Moreover,
`G′ = (G|U)/(K|U)` is representable and the morphism `u′ : G′ → H|U` deduced from `u` by passage to the quotient is an
immersion.*

<!-- label: III.XVI.6.3 -->

**Proof.** Let `Z` be the center of `G`, and `K₀ = K ∩ Z`.

a) `K₀` is a subgroup of multiplicative type over a neighborhood `U` of `s`. Indeed, replacing `S` by an étale
extension over a neighborhood `U` of `s` if necessary (which is legitimate), we may assume that `G` possesses a maximal
torus `T` (4.1 c)). But then `T ∩ K` is a group of multiplicative type (Exp. XV 8.3) whose fiber at `s` is central by
hypothesis, so `T ∩ K` is central over a neighborhood of `s` (Exp. IX 5.6 a)) and consequently coincides with `K₀`.

b) Let us show that `K₀ = K` over a neighborhood `U` of `s`. <!-- original page 528 --> By a) we may already assume
that `K₀` is of multiplicative type, hence flat over `S`. Since `K₀_s = K_s`, the natural immersion `K₀ → K` is then
open over a neighborhood `U` of `s` (Exp. VI_B 2.6). If `t ∈ U`, the image of `K_t` in the group `G′_t = G_t/Z_t` is
then an étale finite group, normal in `G′_t` (since `K_t` is normal in `G_t`), hence central, hence reduced to the
unit group (3.3 b)). This says that `K_t` is contained in `Z_t`, hence is equal to `K₀_t`, whence `K = K₀` over `U`.

c) The representability of `G′` then follows from 2.3; the fact that `u′` is an immersion is contained in 1.3 a),
taking 4.1 c) applied to `G′` into account.

**Proposition 6.4.** *Let `S` be a prescheme, `G` an `S`-group prescheme smooth, of finite presentation over `S`, with
connected fibers, `s` a point of `S`, such that `G_s` is generated by its subtori (Exp. XII 8.2) (for example `G_s`
affine of zero unipotent rank), `H` an `S`-group prescheme, `u` and `v : G → H` two `S`-homomorphisms such that
`u_s = v_s` and such that `u_s` is central. Suppose moreover that `H` is of finite presentation over `S`, or that `S`
is locally noetherian. Then there exists a neighborhood `U` of `s` such that `u|U = v|U`.*

<!-- label: III.XVI.6.4 -->

We reduce as usual to the case where `S` is noetherian (to study the condition "`G_s` is generated by its subtori", one
uses Exp. VI_B 7.4). Since `G` has connected fibers, to show that `u = v` over a neighborhood `U` of `s`, it suffices
<!-- original page 529 --> to show that `u = v` after reduction by every power of the maximal ideal of the local ring
`𝒪_{S,s}`, which reduces us to the case where `S` is local artinian.

But then, the functor of maximal subtori of `G` is representable by an `S`-scheme `X`, smooth of finite type over `S`
(Exp. XV 8.17). Let `T` be the maximal subtorus of `G_X`, universal for the functor `X`. The hypothesis made on `G_s`
means that the algebraic subgroup of `G_s` generated (Exp. VI_B § 7) by the `κ(s)`-morphism `f : T_s → G_s` (composite
of the immersion `T_s → G_{X_s}` and the canonical projection `G_{X_s} → G_s`) is equal to `G_s` itself. But `X_s` is
geometrically connected (since if `T` is a maximal torus of `G_s`, `N` its normalizer in `G_s`, `X_s` is isomorphic to
`G_s/N`), and the image of `T_s` under `f` contains the unit section of `G_s`; it then follows from Exp. VI_B 7.4 that
there exist an integer `N > 0` and an `S`-morphism `f^N : T^N → G` (where `T^N = T ×_S ⋯ ×_S T` (`N` factors) and
`f^N` depends only on `f` and on the multiplication law of `G`) such that `(f^N)_s` is surjective.

Consider the base change `X → S` and the restrictions of `u_X` and `v_X` to the subtorus `T` of `G_X`. By hypothesis,
`u_{X_s} = v_{X_s}` and `u_{X_s} : T_{X_s} → H_{X_s}` is a central homomorphism. It then follows from Exp. IX 5.1 that
`u_X|T = v_X|T`. Making explicit the definition of `f^N` and using the fact that `u` and `v` are homomorphisms, one
deduces immediately that `u f^N = v f^N`. But the `κ(s)`-morphism `f^N_s` is surjective and `G_s` is smooth, hence
reduced; consequently `f^N_s` is generically flat. Since `T` is smooth over `S`, hence flat, there exists a non-empty
open set `V` of `T` such that `f^N|V` is flat (EGA IV 11.3.10). The image of `V` is an open `W` of `G` (EGA IV 11.3.1)
and `f^N : V → W` is faithfully flat, of finite presentation, hence covering for the fpqc topology. <!-- original page
530 --> The equality `u f^N = v f^N` then implies `u|W = v|W`. Since `W` is schematically dense in `G` (EGA IV
11.10.10) and `H` is separated over `S` (Exp. VI_A 0.3), one deduces immediately that `u = v`.

[^XVI-0]: Cf. footnote on page 1 of Exp. XV.

[^N.D.E-XVI-1]: N.D.E.: S. Koizumi & G. Shimura, Specialization of abelian varieties, *Sci. Papers Coll. Gen. Ed. Univ.
Tokyo* **9** (1959), 187–211.

[^XVI-1]: TRANSLATOR NOTE: the source reads "1.2 a)" here, which appears to be a typo for "1.3 a)" (the connected-fiber case of the immersion criterion stated and proved above).

<!-- LEDGER DELTA — Exposé XVI — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| rang unipotent nul | zero unipotent rank | Title-level term; matches Tome II glossary. |
| critère d'immersion | immersion criterion | Standard. |
| critère valuatif de propreté locale | valuative criterion of local properness | EGA IV 15.7.5 idiom. |
| critère valuatif de platitude | valuative criterion of flatness | EGA IV 11.8.1 idiom. |
| adhérence schématique | schematic closure | Standard. |
| schématiquement dense | schematically dense | Standard. |
| universellement schématiquement dense | universally schematically dense | Standard (EGA IV 11.10.8). |
| sous-groupe de Cartan | Cartan subgroup | Standard. |
| sous-tore | subtorus | Standard. |
| tore maximal | maximal torus | Standard. |
| groupe de Weyl | Weyl group | Standard. |
| dédoublant | doubling | For "obtenu en dédoublant l'unique point": étale, non-separated lift of a single point. |
| invariant normal | normal invariant | EGA IV 16 idiom (sheaf of jets along a section). |
| représentation adjointe | adjoint representation | Standard. |
| centre réductif | reductive center | Per Tome II glossary. |
| rang nilpotent | nilpotent rank | Standard. |
| rang abélien | abelian rank | Standard. |
| rang réductif | reductive rank | Standard. |
| variété abélienne | abelian variety | Standard. |
| préschéma abélien | abelian prescheme | Per Exp. XVI 3.5 (iii): smooth S-group with abelian-variety fibers. |
| groupe radiciel | radicial group | Per Tome I glossary. |
| transporteur strict | strict transporter | `Transp^{str}`; matches Exp. XII 7.1 b). |
| inégale caractéristique | unequal characteristic | Standard. |
| égale caractéristique | equal characteristic | Standard. |
| « Rappelons » | Let us "recall" | Source uses guillemets to flag a deferred proof; preserve quotation marks. |
| corps résiduel algébriquement clos | algebraically closed residue field | Standard. |
| anneau de valuation discrète complet | complete discrete valuation ring | Standard. |
| henselien | henselian | Standard (loanword). |
| topologie fpqc / étale / fidèlement plate | fpqc / étale / faithfully flat topology | Standard. |
| Bible | *Bible* | Italicized; refers to Chevalley Seminar 1956/58. |
| Sém. Bourbaki | Sém. Bourbaki | Preserve abbreviation. |
| N.D.E. | N.D.E. | Editors' note; rendered as `[^N.D.E-XVI-n]` footnote. |
-->

