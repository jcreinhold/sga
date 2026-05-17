# Exposé XIX. Reductive groups: generalities

<!-- label: III.XIX -->

*by M. Demazure*

<!-- original page 1 -->

[^N.D.E-XIX-0] The remainder of this Séminaire is devoted to the study of reductive groups. Its principal aim is the
generalization of Chevalley's classical results (*Bible* and *Tôhoku*)[^N.D.E-XIX-1] to arbitrary base schemes, the two
central results being the uniqueness theorem (Exp. XXIII, Th. 4.1 and Cor. 5.1 to 5.10) and the existence theorem
(Exp. XXV, Th. 1.1) for "pinned" reductive group schemes corresponding to prescribed "root data". The proofs employed
are inspired by Chevalley's, the technique of schemes permitting one to lend them increased efficiency.

The results of the first volume of the *Bible* (Exp. 1 to 13) will be used systematically. By contrast, we shall prove
directly over an arbitrary scheme the results of the second volume (in particular the isomorphism theorem); a knowledge
of the proofs over an algebraically closed field is therefore not absolutely indispensable.

In the proof of these two fundamental results, we shall use only the most elementary results from the theory of groups
of multiplicative type, contained essentially in Exp. VIII and IX; we shall, on the other hand, make essential use of
the results of Exposé XVIII.[^N.D.E-XIX-2] The reader specifically interested in the existence and uniqueness theorems
may, on a first reading, skip Exposés X to XVII.

## 1. Reminders on groups over an algebraically closed field

<!-- label: III.XIX.1 -->

<!-- original page 2 -->

**1.1.** In this number, `k` will always denote an algebraically closed field. As announced above, the only results
from *Bible* used in what follows are found in volume 1 (Exposés 1 to 13). All the results of *Bible* (*loc. cit.*)
concerning semisimple groups are valid more generally for reductive groups (definition below) and their proof is
identical, with the following innocuous modifications:

- Exp. 9, § 4, Definition 3: see 1.6.1 below.
- Exp. 12, § 4, Theorem 2, e): suppress "finite".
- Exp. 13, § 3, Theorem 2: replace "rank" by "semisimple rank".
- Exp. 13, § 4, Corollary 2 to Theorem 3: replace "rank" by "reductive rank".

**1.2.** Let `G` be a smooth affine connected `k`-group. The *radical* of `G` (*Bible*, § 9.4, Prop. 2)[^N.D.E-XIX-3] is
the reduced subgroup associated with the neutral component of the intersection of the Borel subgroups of `G`; it is
also the largest smooth connected solvable invariant subgroup of `G`; we shall denote it `rad(G)`.

The *unipotent radical* of `G` is the unipotent part of the radical of `G`; it is also the largest smooth connected
unipotent invariant subgroup of `G`; we shall denote it `rad_u(G)`.

**1.3.** Let `G` be a smooth affine connected `k`-group, and `Q` a torus of `G`. Then the centralizer `Centr_G(Q)` of
`Q` in `G` is a closed subgroup of `G` (Exp. VIII, 6.7), smooth (Exp. XI, 2.4), and connected (cf. *Bible*, § 6.6, Th. 6
a) or [Ch05], § 6.7, Th. 7 a)).

<!-- original page 3 -->

One has the fundamental relation:

```text
rad_u(Centr_G(Q)) = rad_u(G) ∩ Centr_G(Q).
```

<!-- label: eq:III.XIX.1.3.1 -->

First,[^N.D.E-XIX-4] `U = rad_u(G) ∩ Centr_G(Q)` is an invariant unipotent subgroup of `Centr_G(Q)`; let us show that
it is smooth and connected. If we make `Q` operate on `rad_u(G)` by inner automorphisms, `U` is none other than the
scheme of invariants of this operation. But this scheme is smooth and connected, by Lemma 1.4 below.

Consequently, `U` is a closed subgroup of `rad_u(Centr_G(Q))`. On the other hand, by *Bible*, Exp. 12, § 3, Cor. to
Th. 1, one has `rad_u(Centr_G(Q))(k) ⊂ rad_u(G)(k)`. The equality (1.3.1) follows.

Let us signal a particular case of the foregoing result: if `G` is a smooth affine connected `k`-group and if `T` is a
maximal torus of `G`, then

```text
Centr_G(T) = T · (Centr_G(T) ∩ rad_u(G)).
```

<!-- label: eq:III.XIX.1.3.2 -->

Indeed (cf. *Bible*, § 6.6, Th. 6 c) or [Ch05], § 6.7, Th. 7 c)), `Centr_G(T)` is a solvable group, hence the
semi-direct product of its maximal torus `T` and its unipotent radical.

<!-- original page 4 -->

By the density theorem (cf. *Bible*, § 6.5, Th. 5 a) or [Ch05], § 6.6, Th. 6 a)), the union of the `Centr_G(T)`, as `T`
runs through the set of maximal tori of `G`, contains a dense open subset of `G`; it therefore follows from (1.3.2):

**Corollary 1.3.3.** *If `G` is a smooth affine connected `k`-group, then the union of the `T · rad_u(G)`, where `T`
runs through the set of maximal tori of `G`, contains a dense open subset of `G`.*

<!-- label: III.XIX.1.3.3 -->

**Notations 1.4.0.** [^N.D.E-XIX-5] *We shall systematically use the following notation: if `S` is a scheme and `s` a
point of `S`, we denote by `s̄` the spectrum of an algebraic closure `κ(s)̄` of `κ(s)`.*

<!-- label: III.XIX.1.4.0 -->

**Lemma 1.4.** [^N.D.E-XIX-5] *Let `S` be a scheme, `Q` an `S`-torus operating on an `S`-group scheme `H`, separated and
smooth over `S`.*

*(i) The functor of invariants `H^Q` is representable by a closed subscheme of `H`, smooth over `S`.*

*(ii) If moreover `H` is affine over `S`, and has connected fibers, then `H^Q` does too.*

<!-- label: III.XIX.1.4 -->

*Proof.* First, by VIII 6.5 (d),[^N.D.E-XIX-6] since `H` is separated over `S` and `Q` essentially free over `S`, `H^Q`
is representable by a closed subscheme of `H`. In particular, if `H` is affine over `S`, then so is `H^Q`.

Consider now the semi-direct product `G = H · Q`; it is smooth and separated over `S`. Then, the centralizer
`Centr_G(Q)` is representable by a closed subscheme of `G`, of finite presentation over `G`, by Exp. XI
6.11 (a),[^N.D.E-XIX-6] and it is smooth over `S` by Exp. XI 2.4.

Since `Centr_G(Q) = H^Q · Q`, it follows that `H^Q` is smooth over `S`. (Indeed, using the section
`σ : H^Q → Centr_G(Q)` deduced from the unit section `ε_Q` of `Q`, one sees at once that `H^Q` is formally smooth over
`S`; and since moreover `ε_Q` is of finite presentation, `H^Q` is locally of finite presentation over `S`.) This
proves (i).

Finally, suppose `H` affine over `S` and with connected fibers. Then each geometric fiber `G_s̄` of `G` is a smooth
affine connected `κ(s)̄`-group, hence, by the first assertion of 1.3, so is

```text
Centr_{G_s̄}(Q_s̄) = (Centr_G(Q))_s̄ = (H^Q)_s̄ · Q_s̄,
```

and this entails that `(H^Q)_s̄` is connected.

**1.5.** We recall that the *reductive rank* of the smooth affine `k`-group `G` is the common dimension of the maximal
tori of `G`. We shall denote it `rgred(G/k)` or `rgred(G)`. In order that `rgred(G/k) = 0`, it is necessary and
sufficient that `G` be unipotent (i.e. that `G = rad_u(G)`), by *Bible*, § 6.4, Cor. 1 to Th. 4 or [Ch05], § 6.5,
Cor. 1 to Th. 5.

If `H` is an invariant subgroup of the smooth affine `k`-group `G`, then the quotient `G/H` is affine and smooth
(Exp. VI_B, 11.17 and VI_A, 3.3.2 (iii)). Moreover (*Bible*, § 7.3, Th. 3, a) and c)), one has

```text
rgred(G) = rgred(G/H) + rgred(H).
```

<!-- original page 4 (cont.) -->

**Definition 1.6.1.** [^N.D.E-XIX-7] *One says that the `k`-group `G` is* reductive *if it is smooth, affine, and
connected, and if `rad(G)` is a torus, i.e. if `rad_u(G) = {e}`.*

<!-- label: III.XIX.1.6.1 -->

**Lemma 1.6.2.** *Let `G` be a reductive `k`-group.*

*(i) If `Q` is a torus of `G`, then `Centr_G(Q)` is reductive.*

*(ii) In particular, if `T` is a maximal torus of `G`, then `Centr_G(T) = T`.*

*(iii) The center of `G` is contained in every maximal torus, hence is diagonalizable.*

*(iv) The radical of `G` is the (unique) maximal torus of `Centr(G)`.*

<!-- label: III.XIX.1.6.2 -->

*Proof.* Indeed, (i) follows from (1.3.1), (ii) from (1.3.2), and (iii) follows from (ii). Finally, the maximal torus
of `Centr(G)` (i.e. the neutral component `Centr(G)⁰`) is a smooth connected solvable subgroup, invariant in `G`,
hence contained in `rad(G)`; conversely, `rad(G)` is an invariant torus in `G`, hence central (*Bible*, § 4.3, Cor. to
Prop. 2), whence (iv).

<!-- original page 5 -->

**Remark 1.6.3.** *If `G` is reductive and if `dim(G) ≠ rgred(G)`, then `dim(G) − rgred(G) ⩾ 2`. Indeed, this
difference is always even (cf. 1.10 below).*

<!-- label: III.XIX.1.6.3 -->

**1.7.** Let `G` be a smooth affine connected `k`-group and `H` a smooth connected invariant subgroup. Then

```text
rad(H) = (rad(G) ∩ H)⁰_red   and   rad_u(H) = (rad_u(G) ∩ H)⁰_red,
```

<!-- label: eq:III.XIX.1.7.1 -->

as one sees at once. In particular, if `G` is reductive, so is `H`.

Let `f : G → G′` be a surjective morphism of smooth affine connected `k`-groups. Then

```text
f(rad_u(G)) = rad_u(G′).
```

<!-- label: eq:III.XIX.1.7.2 -->

In particular, if `G` is reductive, so is `G′`.

Let us prove (1.7.2). First, `f` sends `rad_u(G)` into `rad_u(G′)`. Introducing `H = (f⁻¹(rad_u(G′)))⁰_red`, which
contains `rad_u(G)`, one has `rad_u(H) = rad_u(G)` and one is reduced to the case where `G = H`, i.e. where `G′` is
unipotent. Since the union of the `T · rad_u(G)` (as `T` runs through the set of maximal tori of `G`) is dense in `G`,
the union of the `f(T) f(rad_u(G))` is dense in `G′`; but `f(T)` consists of semisimple elements, so `f(T) = {e}`,
`G′` being unipotent; this shows that `f(rad_u(G))` is dense in `G′`. Therefore, by *Bible*, § 5.4, Lemma 4 or [Ch05],
§ 6.1, Lemma 1,[^N.D.E-XIX-8] `f(rad_u(G))` is an open subgroup of `G′`; the latter being connected, it follows that
`f(rad_u(G)) = G′`. (N.B.: one can prove under the same hypotheses that `f(rad(G)) = rad(G′)`.)

**1.8.** One says that the `k`-group `G` is *semisimple* if it is smooth, affine, and connected and if `rad(G) = {e}`,
i.e. if `G` is reductive and `Centr(G)` is finite. If `G` is an arbitrary smooth affine connected `k`-group, then
`G / rad(G)` is semisimple (*Bible*, § 9.4, Prop. 2), and `G / rad_u(G)` is reductive. One calls the *semisimple rank
of `G`* and denotes by `rgss(G/k)` or `rgss(G)` the reductive rank of `G / rad(G)`.

If `G` is reductive, one therefore has

<!-- original page 6 -->

```text
rgred(G) = rgss(G) + dim(rad(G)).
```

If `G` is a smooth affine connected `k`-group and if `Q` is a central subtorus of `G`, then `G/Q` is semisimple if and
only if `G` is reductive and `Q = rad(G)`. Indeed, if `G/Q` is semisimple, `Q ⊃ rad(G)`, so `rad(G)` is a torus, so `G`
is reductive, so `rad(G)` is the maximal torus of `Centr(G)`, so `rad(G) = Q`. If `G` is reductive and if `Q` is a
central subgroup then (`G/Q` is reductive and) `rgss(G) = rgss(G/Q)`.

**1.9.** If `K` is an algebraically closed extension of `k` and if `G` is a smooth affine connected `k`-group, then `G`
is reductive (resp. semisimple) if and only if `G_K` is, and one has

```text
rgred(G/k) = rgred(G_K/K),
rgss(G/k) = rgss(G_K/K).
```

**1.10.** Let `G` be a smooth connected `k`-group and let `T` be a torus of `G`.[^N.D.E-XIX-9] Denote by `g` the
`k`-Lie algebra of `G`, i.e. `g = Lie(G) = Lie(G/k)(k)`; likewise denote `t = Lie(T)`. Then `g` decomposes under the
action of `T` (via `T → G` and the adjoint operation of `G`) as

```text
g = g₀ ⊕ ∐_{α ∈ R} g_α,
```

<!-- label: eq:III.XIX.1.10.1 -->

where the `α ∈ R` are non-trivial characters of `T` and the `g_α` are `≠ 0`. The characters `α ∈ R` are called the
*roots* of `G` with respect to `T`. By Exp. II, 5.2.3 (i), one has

<!-- original page 7 -->

```text
g₀ = Lie(Centr_G(T)).
```

<!-- label: eq:III.XIX.1.10.2 -->

In particular,[^N.D.E-XIX-10] since `Centr_G(T)` is connected (1.3 in the case where `G` is affine, and Exp. XII 6.6 b)
in the general case), `T` is its own centralizer if and only if `g₀ = Lie(T)`.

This condition entails that `T` is maximal and that `Centr(G) ⊂ T`, hence by Exp. XII 8.8 d) one has:

```text
Centr(G) = Ker(T → GL(g)) = ⋂_{α ∈ R} Ker(α);
```

<!-- label: eq:III.XIX.1.10.3 -->

moreover `Centr(G)` is then affine, hence `G → G/Centr(G)` is affine; since the latter group is affine (Exp. XII
6.1),[^N.D.E-XIX-11] so is `G`.

When `G` is reductive and `T` maximal, the roots in the preceding sense coincide with the roots in the sense of
*Bible*, § 12.2, Def. 1; the latter are indeed roots in the sense of this number (*Bible*, § 13.2, Th. 1, c)) and
there are `dim(G) − dim(T)` of them (*Bible*, § 13.4, Cor. 2 to Th. 3). Moreover, if `α` is a root, so is `−α`
(*Bible*, § 12.2, Cor. to Prop. 1). (As usual, one writes the group structure of `Hom_{k-gr.}(T, G_{m,k})`
indifferently additively or multiplicatively.) It follows that, for `G` reductive,

<!-- original page 8 -->

```text
dim(G) − rgred(G) = Card(R)
```

<!-- label: eq:III.XIX.1.10.4 -->

is always even.

The semisimple rank of the reductive group `G` is the rank of the subset `R` of the `Q`-vector space
`Hom_{k-gr.}(T, G_{m,k}) ⊗ Q` (*Bible*, § 13.3, Th. 2).

**Lemma 1.11.** *Let `k` be an algebraically closed field, `G` a smooth affine connected `k`-group, `T` a torus of `G`,
`W(T) = Norm_G(T) / Centr_G(T)` the Weyl group of `G` with respect to `T`. The following conditions are equivalent:*

*(i) `G` is reductive, `T` is maximal, `rgss(G) = 1`.*

*(ii) `G` is reductive, `T` is maximal, `G ≠ T`; there exists a subtorus `Q` of `T`, of codimension `1` in `T`, central
in `G`.*

*(iii) `G` is not solvable and `dim(G) − dim(T) ⩽ 2`.*

*(iv) `W(T) ≠ {e}` and `dim(G) − dim(T) ⩽ 2`.*

*(v) `W(T) = (Z/2Z)_k` and `dim(G) − dim(T) = 2`.*

*Moreover, under these conditions, there are exactly two roots of `G` with respect to `T`; they are opposite. Under the
conditions of (ii), `Q = rad(G)`.*

<!-- label: III.XIX.1.11 -->

*Proof.* One has obviously (v) ⇒ (iv). One has (iv) ⇒ (iii) by *Bible*, § 6.1, Cor. 3 to Th. 1 or [Ch05], § 6.2,
Cor. 3 to Th. 2. Let us prove (iii) ⇒ (ii): let `U` be the unipotent radical of `G`; one knows that `G/U` is reductive
and is not a torus (otherwise `G` would be solvable); one therefore has, by (1.10.4),

```text
dim(G/U) − rgred(G/U) = Card(R) ⩾ 2;
```

but

```text
rgred(G) = rgred(G/U) + rgred(U) = rgred(G/U),
```

whence

```text
dim(G) − dim(U) − rgred(G) = dim(G/U) − rgred(G/U)
                           ⩾ 2 ⩾ dim(G) − dim(T) ⩾ dim(G) − rgred(G).
```

This gives `dim(U) = 0`, hence `G` is reductive, `rgred(G) = dim(T)`, hence `T` is maximal, `dim(G) − dim(T) = 2`. By
*Bible*, § 10.4, Prop. 8, there exists a singular torus `Q` of codimension `1` in `T`; then `Centr_G(Q)` is reductive
(1.6.2 (i)), non-solvable (definition of a singular torus), hence
`dim(Centr_G(Q)) − rgred(G) ⩾ 2`, which proves that `G = Centr_G(Q)` and `Q` is central in `G`.

Let us prove (ii) ⇒ (i). One knows that `G/Q` is reductive (1.7) and that `rgred(G/Q) = 1`, hence
`rgss(G/Q) = 0` or `1`. The first case is impossible, for it would entail `rgss(G) = 0`, hence `G = T`;

<!-- original page 9 -->

one therefore has `rgred(G/Q) = rgss(G/Q) = 1`, which proves that `G/Q` is semisimple; hence `Q` is the radical of `G`
and `rgss(G) = 1`.

Let us finally prove (i) ⇒ (v). If `Q` is the radical of `G`, one has `dim(T) − dim(Q) = 1` and `Q` is central in `G`,
hence `G = Centr_G(Q)`, which proves that `Q` is a singular torus; by *Bible*, § 11.3, Th. 2, one has
`W_G(T) = (Z/2Z)_k`; by *Bible*, § 12.1, Lemma 1, one has `dim(G) − dim(T) = 2`. There are therefore at most two roots
of `G` with respect to `T`; but there are at least two, opposite to each other (1.10).

**Proposition 1.12.** *Let `k` be an algebraically closed field, `G` a smooth connected `k`-group, `T` a torus of `G`,
`R` the set of roots of `G` with respect to `T`, and*

```text
g = g₀ ⊕ ∐_{α ∈ R} g_α,    with g_α ≠ 0,
```

*the decomposition of `g` under `Ad(T)`. For each `α ∈ R`, let `T_α` be the maximal torus of `Ker(α)`[^N.D.E-XIX-12] and
`Z_α = Centr_G(T_α)`. The following conditions are equivalent:*

*(i) `G` is affine, reductive; `T` is maximal.*

*(ii) `g₀ = t`, each `Z_α` (`α ∈ R`) is reductive.*

*(iii) `g₀ = t`, each `g_α` (`α ∈ R`) is of dimension `1`; and if `α, β ∈ R` and `q ∈ Q` are such that `β = q α`, then
`q = ±1`; for each `α ∈ R`, there exists `w_α ∈ G(k)` which normalizes `T`, centralizes `T_α`, but does not centralize
`T`.*

*Moreover, under these conditions, each `Z_α` is of semisimple rank `1` and one has `Lie(Z_α) = t ⊕ g_α ⊕ g_{−α}`.*

<!-- label: III.XIX.1.12 -->

*Proof.* If `G` is affine and reductive and if `T` is maximal, each `Z_α` is affine and reductive (1.6.2 (i)), with
maximal torus `T`; moreover, `T` is its own centralizer (1.6.2 (ii)), hence `g₀ = t`, which proves (i) ⇒ (ii).

On the other hand `g₀ = t` entails that `T` is maximal and `G` affine (cf. 1.10), hence each `Z_α` is affine, smooth,
and connected, by 1.3. In any case, one has, by Exp. II, 5.2.2,

<!-- original page 10 -->

```text
Lie(Z_α) = g^{T_α} = g₀ ⊕ ∐_{β ∈ R ∩ Qα} g_β.
```

One therefore has

```text
Lie(Z_α) ⊃ t ⊕ g_α ⊕ g_{−α},
```

which entails `Z_α ≠ T`. Since `T_α` is a subtorus of codimension `1` in `T`, central in `Z_α`, one obtains by 1.11,
applied to `Z_α`, the equivalence (ii) ⇔ (iii) and the supplements.

It remains to prove (ii) ⇒ (i); one already knows that (ii) entails that `T` is maximal and `G` affine. Let `U` be its
unipotent radical; it is invariant in `G`, its Lie algebra is invariant under `Ad(T)`. One therefore has

```text
Lie(U) = (Lie(U) ∩ g₀) ⊕ ∐_{α ∈ R} (Lie(U) ∩ g_α).
```

By (1.3.1), one has

```text
U ∩ T = U ∩ Centr_G(T) = rad_u(Centr_G(T)) = rad_u(T) = {e},
U ∩ Z_α = U ∩ Centr_G(T_α) = rad_u(Centr_G(T_α)) = rad_u(Z_α) = {e}.
```

One therefore has[^N.D.E-XIX-13]

```text
Lie(U) ∩ g₀ = Lie(U) ∩ t = Lie(U ∩ T) = 0,
Lie(U) ∩ g_α ⊂ Lie(U) ∩ Lie(Z_α) = Lie(U ∩ Z_α) = 0;
```

whence `Lie(U) = 0` and `U = {e}`, i.e. `G` is reductive.

**Corollary 1.13.** *Let `k` be an algebraically closed field, `G` a smooth connected `k`-group, `T` a torus of `G`,
`R` the set of roots of `G` with respect to `T`, and*

```text
g = g₀ ⊕ ∐_{α ∈ R} g_α
```

*as above. For each `α ∈ R`, let `T_α` be the maximal torus of `Ker(α)` and `Z_α = Centr_G(T_α)`. The following
conditions are equivalent:*

<!-- original page 11 -->

*(i) `G` is affine, semisimple; `T` is maximal.*

*(ii) `g₀ = t`, each `Z_α` is reductive, and `⋂_{α ∈ R} Ker(α)` is finite.*

<!-- label: III.XIX.1.13 -->

[^N.D.E-XIX-14] This follows from the equalities `rad(G) = Centr(G)⁰` and `Centr(G) = ⋂_{α ∈ R} Ker(α)`, established in
1.6.2 (iv) and (1.10.3).

## 2. Reductive group schemes. Definitions and first properties

<!-- label: III.XIX.2 -->

**Scholie 2.1.** *If `G` is a group scheme over `S`, the following properties are equivalent:*

*(i) `G` is affine and smooth over `S`, with connected fibers.*

*(ii) `G` is affine and flat over `S`, of finite presentation over `S`, with geometrically integral fibers.*

*These properties are stable under base change and local for (fpqc).*

<!-- label: III.XIX.2.1 -->

[^N.D.E-XIX-15] Indeed, suppose (i) is satisfied. Since `G` is affine and smooth over `S`, it is of finite presentation
over `S`; and since its fibers are smooth and connected, they are geometrically integral, by VI_A, 2.4.

Conversely, if (ii) is satisfied, the fibers of `G` are connected and geometrically reduced, hence smooth (VI_A,
1.3.1); then `G` is smooth over `S`, by EGA IV₄, 17.5.2.

Of course, these properties are stable under base change: cf. EGA II, 1.5.1 for "affine", IV₁, 1.6.2 (iii) for "of
finite presentation", IV₂, 2.1.4 for "flat", and IV₂, 4.6.5 (i) for "with geometrically integral fibers".

<!-- original page 9 -->

On the other hand, these properties are clearly local for the Zariski topology, so it suffices to verify that if
`S′ → S` is a faithfully flat quasi-compact morphism and if `G_{S′} → S′` has the indicated properties, then so does
`G → S`. This follows from EGA IV₂, 2.5.1 for "flat", 2.7.1 (vi) and (xiii) for "of finite presentation" and "affine",
and 4.6.5 (i) for "with geometrically integral fibers" (and also EGA IV₄, 17.7.3 (ii) for "smooth").

**2.2.** Let `G` be an `S`-group scheme satisfying the preceding conditions, and `Q` a torus (cf. IX, Def. 1.3) of
`G`.[^N.D.E-XIX-16] Then, by XI, 6.11 a) and XI, 2.4, `Centr_G(Q)` is representable by a closed subgroup scheme of `G`
(hence affine over `S`), of finite presentation and smooth over `S`; moreover, since each geometric fiber `G_s̄` of `G`
is a smooth affine connected `κ(s)̄`-group, then, by the first assertion of 1.3, so is

```text
Centr_{G_s̄}(Q_s̄) = (Centr_G(Q))_s̄.
```

**Lemma 2.3.** *Let `S` be a scheme, `G` an `S`-group scheme smooth and affine over `S`, with connected fibers, `T` a
torus of `G`. The set of `s ∈ S` such that `G_s` is a reductive `s`-group, of semisimple rank `1` and with maximal
torus `T_s`, is an open subset `U` of `S`.*

<!-- label: III.XIX.2.3 -->

<!-- original page 12 -->

*Proof.* Since `G` and `T` are flat over `S`, the function

```text
s ↦ dim(G_s/s) − dim(T_s/s)
```

is locally constant; let `U₁` be the open subset of points of `S` where it equals `2`.

[^N.D.E-XIX-17] By 6.3, the Weyl group

```text
W_G(T) = Norm_G(T) / Centr_G(T)
```

is representable by an `S`-group scheme étale and separated over `S`, and the function

```text
s ↦ number of points of W_G(T)_s
```

is lower semicontinuous. Let `U₂` be the set of points of `S` where this function is `> 1`; it is open. By 1.11, the
set of `s` such that `G_s` is reductive, of semisimple rank `1`, with maximal torus `T_s`, is `U = U₁ ∩ U₂`; moreover,
for every `s ∈ U`, `W_G(T)_s` has exactly two points.

Consequently (cf. SGA 1, I 10.9 and EGA IV₃, 15.5.1 and IV₄, 18.12.4), `W_G(T)_U` is étale and finite over `U`.

**Remark 2.4.** *The group `W_G(T)_U` is isomorphic to `(Z/2Z)_U`.*

<!-- label: III.XIX.2.4 -->

Indeed, by what precedes, it is étale and finite over `U`; since the functor of automorphisms of `(Z/2Z)_U` is the
trivial group, it suffices to verify the assertion locally; but the assertion is immediate if the algebra `A` defining
`W_G(T)_U` is a free `O_U`-module.[^N.D.E-XIX-18]

**Notations and reminders 2.5.0.** [^N.D.E-XIX-19] *Let `S` be a scheme, `G` an `S`-group scheme, `ε : S → G` the unit
section of `G`. One has seen in II, § 4.11 that the functor `Lie(G/S)` is representable by the vector fibration
`V(ω¹_{G/S})` (where `ω¹_{G/S} = ε*(Ω¹_{G/S})`), and one denotes*

```text
g = Lie(G/S) = (ω¹_{G/S})ⱽ
```

*the sheaf of sections of this vector fibration. Suppose moreover that `G` is smooth over `S`; then `ω¹_{G/S}` and
hence `Lie(G/S)` are locally free `O_S`-modules of finite type, and one has (cf. I 4.6.5.1):*

```text
Lie(G/S) = W(Lie(G/S)),
```

*i.e. for every `S`-scheme `S′`,*

```text
Lie(G/S)(S′) = Γ(S′, Lie(G/S) ⊗ O_{S′}).
```

*By II 4.1.1.1, the adjoint action of `G` endows `Lie(G/S) = W(Lie(G/S))` with a `G`-`O_S`-module structure, hence
`Lie(G/S)` is a `G`-`O_S`-module (cf. I 4.7.1). If moreover `G` is affine over `S`, this amounts to saying, by I 4.7.2,
that `Lie(G/S)` is an `A(G)`-comodule.*

*If `T` is a torus over `S` (IX Def. 1.3), one says that `T` is* split *("trivial" in the original) if it is isomorphic
to `Gʳ_{m,S}` for some integer `r ⩾ 0`, and one says that `T` is* trivialized *if one has fixed such an isomorphism or,
more generally, an isomorphism `T ≃ D_S(M)`, where `M` is a free abelian group of rank `r`.*

*Let us finally recall (XII Def. 1.3) that a torus `T` of `G` is called* maximal *if, for every `s ∈ S`, `T_s̄` is a
maximal torus of `G_s̄`.*

<!-- label: III.XIX.2.5.0 -->

**Theorem 2.5.** *Let `S` be a scheme, `G` an `S`-group scheme affine and of finite presentation over `S`, with
connected fibers, and `s₀` a point of `S`. Suppose `G` flat over `S` at `ε(s₀)` and the geometric fiber `G_{s̄₀}`
(reduced and) reductive (resp. semisimple). Then there exists an open subset `U` of `S` containing `s₀` and an étale
surjective morphism `S′ → U` such that:*

<!-- original page 13 -->

*(i) `G_U` is smooth over `S`, with geometrically reductive (resp. semisimple) fibers, of constant reductive rank and
semisimple rank.*

*(ii) `G_{S′}` possesses a split[^N.D.E-XIX-20] maximal torus `T`, and the Weyl group (cf. 6.3)*

```text
W_{G_{S′}}(T) = Norm_{G_{S′}}(T) / Centr_{G_{S′}}(T) = Norm_{G_{S′}}(T) / T
```

*is finite over `S′`.*

<!-- label: III.XIX.2.5 -->

*Proof.*[^N.D.E-XIX-21] Denote by `π : G → S` the structure morphism and `ε : S → G` the unit section. Since `G` is
flat over `S` at `ε(s₀)` and `G_{s̄₀}` reduced (hence smooth over `s̄₀`, cf. VI_A 1.3.1), `G` is smooth over `S` at the
point `ε(s₀)` (EGA IV₄, 17.5.1), i.e. there exists an open neighborhood `V` of `ε(s₀)` such that `π|V` is smooth. Then,
`S′ = ε⁻¹(V)` is an open subset of `S`, and `G_{S′}` is smooth over `S′` at the points of `ε(S′)`. Since `G` has
connected fibers, `G_{S′}` is smooth over `S′`, by VI_B, 3.10. So, replacing `S` by `S′`, one may assume `G` smooth
over `S`.

By Exp. XI, Th. 4.1, the functor of subgroups of multiplicative type of `G` is representable by an `S`-scheme `𝓜`,
smooth and separated over `S`. Denote by `r₀` the rank of `G_{s̄₀}` and consider the open subscheme `𝓜_{r₀}` of `𝓜`,
which represents the functor of subtori of rank `r₀` of `G` (IX 1.4). Smoothness entails that `𝓜_{r₀}` admits a
rational point over a finite separable extension of `κ(s₀)` (cf. EGA IV₄, 17.15.10 (iii)). Thus there exists
`S′ → S` étale equipped with a point `s′₀` mapping to `s₀` such that `G_{s′₀}` admits a torus of rank `r₀`. Therefore,
replacing `S` by `S′`, one may assume that `G_{s₀}` admits a torus of rank `r₀`.

By "Hensel's lemma" (cf. XI, 1.10), the smoothness of `𝓜_{r₀}` permits one to lift this torus to an `S′`-torus `T` of
`G`, where `S′ → S` is étale equipped with a point `s′₀` mapping to `s₀`. By Exp. X, 4.5 (see also 6.1[^N.D.E-XIX-22]),
there exists an étale morphism `f : S″ → S′` splitting `T` and such that `f⁻¹(s′₀) ≠ ∅`. Since an étale morphism is
open and the assertions of (i) are local for the étale topology, one may therefore assume that `G` possesses a split
torus `T`,[^N.D.E-XIX-23] maximal at `s₀`. Write therefore `T = D_S(M)` and let

```text
g = ∐_{m ∈ M} g_m
```

be the decomposition of `g = Lie(G/S)` under `Ad(T)` (Exp. I, 4.7.3).

Put `t = Lie(T)` and, for every `m ∈ M`, denote `g_m(s₀) = g_m ⊗_{O_S} κ(s₀)`.[^N.D.E-XIX-24] Let `R` be the set of
`m ∈ M`, `m ≠ 0`, such that `g_m(s₀) ≠ 0`.[^N.D.E-XIX-25] Since `G_{s̄₀}` is reductive, one has `g₀(s₀) = t(s₀)`, hence

```text
g(s₀) = t(s₀) ⊕ ∐_{α ∈ R} g^α(s₀).
```

Since the modules in question are locally free, one may, by shrinking `S` if necessary, assume the `g_α` free and

<!-- original page 14 -->

```text
g = t ⊕ ∐_{α ∈ R} g_α.
```

One recalls, cf. Exp. XII, 1.12, that a group of multiplicative type possesses a unique maximal torus (this is moreover
essentially trivial by descent, the diagonalizable case being evident). Let then `T_α` be the maximal torus of the
kernel of `α` and `Z_α = Centr_G(T_α)`.[^N.D.E-XIX-26] By 2.2, `Z_α` is affine and smooth over `S`, with connected
fibers, and by 1.12, its fiber `(Z_α)_{s̄₀}` is reductive, of semisimple rank `1`, with maximal torus `T_{s̄₀}`. By 2.3,
there therefore exists an open subset `U_α` of `S`, containing `s₀`, such that `Z_α|U_α` has reductive fibers.

<!-- original page 14 (cont.) -->

Set `U = ⋂_{α ∈ R} U_α`. By 1.12, for every `s ∈ U`, `G_s̄` is reductive, with maximal torus `T_s̄` and the set of roots
of `G_s̄` with respect to `T_s̄` is identified with `R`, so that

```text
rgred(G_s̄) = dim(T) = rg(M),     rgss(G_s̄) = rg(R)   (cf. 1.10).
```

One has therefore proved (i) and the first assertion of (ii); it remains to prove that the Weyl group
`W_{G_U}(T_U)` is finite over `U`, i.e. "that it has the same number of points in each geometric fiber" (cf. SGA 1, I
10.9 and EGA IV₃, 15.5.1 and IV₄, 8.12.4).

For this, it suffices to remark that the geometric fiber of this group at `s ∈ U` is determined by the situation
`R ⊂ M`, as the constant group associated with the "abstract Weyl group of this root system", and in particular is
independent of the point `s`, cf. *Bible*, § 11.3, Th. 2 (see also Exp. XXII, no. 3).

**Corollary 2.6.** *Let `G` be an `S`-group affine and smooth over `S`, with connected fibers. The set of points
`s ∈ S` such that `G_s̄` is reductive (resp. semisimple) is an open subset `U` of `S`, and the functions*

```text
s ↦ rgred(G_s̄/s̄),     s ↦ rgss(G_s̄/s̄)
```

*are locally constant on `U`.*

<!-- label: III.XIX.2.6 -->

<!-- original page 15 -->

**Definition 2.7.** *An `S`-group (= `S`-group scheme) `G` is called* reductive *(resp.* semisimple*) if it is affine
and smooth over `S`, with geometrically connected fibers, and reductive (resp. semisimple).*

<!-- label: III.XIX.2.7 -->

The property of being reductive (resp. semisimple) for an `S`-group `G` is stable under base change and local for the
(fpqc) topology.

**2.8.** Let `G` be a reductive `S`-group. For every torus (resp. maximal torus) `Q` of `G`, `Z(Q) = Centr_G(Q)` is
reductive (resp. equals `Q`). This follows at once from 2.2 and 1.6. Applying 2.5 to `Centr_G(Q)`, one deduces from it
that `Q` is contained (locally for the étale topology) in a maximal torus.

**Remark 2.9.** *Using as usual the technique of EGA IV₃, § 8, the finite-presentation hypotheses, and Theorem 2.5, one
sees that if `G` is a reductive group over `S`, there exists an open covering of `S`, say `{U_i}`, such that each
`G_{U_i}` comes by base change from a reductive group over a noetherian ring (in fact, a finitely generated algebra
over `Z`). Likewise, if `G` possesses a split maximal torus `T`, one may further assume that `T_{U_i}` comes from a
split maximal torus of the preceding group, ….*

<!-- label: III.XIX.2.9 -->

## 3. Roots and root systems of reductive group schemes

<!-- label: III.XIX.3 -->

<!-- original page 16 -->

**3.1.** Let `S` be a scheme, `T` an `S`-torus operating linearly on a locally free `O_S`-module of finite type `F`
(cf. I, § 4.7). For every character `α` of `T` (i.e. `α ∈ Hom_{S-gr.}(T, G_{m,S})`), one defines a subfunctor of `W(F)`
by

```text
W(F)^α(S′) = { x ∈ W(F)(S′) | t·x = α(t) x for all t ∈ T(S″), S″ → S′ }.
```

**Lemma.** [^N.D.E-XIX-27] *Then `W(F)^α = W(F^α)`, where `F^α` is a submodule of `F`, locally a direct summand in `F`,
hence also locally free.*

<!-- label: III.XIX.3.1 -->

Indeed, the assertion is local for the (fpqc) topology, and one may assume `T = D_S(M)`, where `M` is a (free) abelian
group of finite type. Then `α` is identified with a locally constant function from `S` to `M` (Exp. VIII 1.3), and
shrinking `S` if necessary, one may assume that this function is constant. One is then reduced to Exp. I, 4.7.3.

**Definition 3.2.** *Let `S` be a scheme, `G` an `S`-group scheme smooth and with connected
fibers,[^N.D.E-XIX-28] `T` a torus of `G`. Denote `g = Lie(G/S)` and let `T` operate on `g` through the adjoint
representation of `G`.*

*One says that the character `α` of `T` is a* root *of `G` with respect to `T` if the following equivalent conditions
are satisfied:*

*(i) For every `s ∈ S`, `α_s̄` is a root of `G_s̄` with respect to `T_s̄` (1.10).*

*(ii) `α` is non-trivial on each fiber and `g^α(s) ≠ 0` for every `s ∈ S`.*

<!-- label: III.XIX.3.2 -->

**Lemma 3.3.** *Let `S` be a scheme, `T` an `S`-torus, `α` a character of `T`. The following conditions are
equivalent:*

<!-- original page 17 -->

*(i) `α` is non-trivial on each fiber, that is to say: for every `s ∈ S`, `α_s̄` is distinct from the unit character of
`T_s̄`.*

*(ii) For every `S′ → S`, `S′ ≠ ∅`, `α_{S′}` is distinct from the unit character of `T_{S′}`.*

*(iii) The morphism `α` is faithfully flat.*

<!-- label: III.XIX.3.3 -->

[^N.D.E-XIX-29] It is clear that (ii) ⇒ (i), and one sees easily that (iii) ⇒ (i). One has (i) ⇒ (ii), for if
`s′ ∈ S′` lies over `s` and if `α_{s′}` is the unit character, then so is `α_s`. Finally, to prove (i) ⇒ (iii), one
reduces to the case where `T` is diagonalizable and concludes by Exp. VIII 3.2 a).

**3.4.** [^N.D.E-XIX-30] Let `G` be a reductive `S`-group scheme, `T` a maximal torus of `G`. Let `α` be a root of `G`
with respect to `T`. Then, by 2.5.0 and 1.12, `g^α` is a locally free `O_S`-module of rank one. Moreover, by 1.10,
`−α` is also a root of `G` with respect to `T`. In particular, if `G` is of semisimple rank `1`, one has by 1.11 and
1.12:

<!-- original page 14 (cont.) -->

**Lemma 3.5.** *Let `S` be a scheme, `G` a reductive `S`-group of semisimple rank `1`, `T` a maximal torus of `G`. If
`α` is a root of `G` with respect to `T`, then `−α` is also one, and one has*

```text
g = t ⊕ g^α ⊕ g^{−α},
```

*where `g^α` and `g^{−α}` are locally free of rank `1`.*

<!-- label: III.XIX.3.5 -->

**Definition 3.6.** *Let `S` be a scheme, `G` a reductive `S`-group, `T` a maximal torus of `G`, `R` a set of roots of
`G` with respect to `T`. One says that `R` is a* root system *of `G` with respect to `T` if the following equivalent
conditions are satisfied:*

<!-- original page 18 -->

*(i) For every `s ∈ S`, `α ↦ α_s̄` is a bijection of `R` onto the set of roots of `G_s̄` with respect to `T_s̄`.*

*(ii) The elements of `R` are distinct on each fiber (i.e. if `α, α′ ∈ R`, `α ≠ α′`, then `α − α′` (= `α α′⁻¹`) is
non-trivial on each fiber), and for every `s ∈ S`, one has*

```text
dim(G_s/κ(s)) − dim(T_s/κ(s)) = Card(R).
```

*(iii) One has `g = t ⊕ ∐_{α ∈ R} g^α`.*

<!-- label: III.XIX.3.6 -->

The equivalence of these various conditions is trivial.

**Lemma 3.7.** *Let `S` be a scheme, `G` a reductive `S`-group, `T` a maximal torus of `G`, `R` a root system of `G`
with respect to `T`. Every root of `G` with respect to `T` is locally on `S` equal to an element of `R`.*

<!-- label: III.XIX.3.7 -->

*Proof.* Visible on condition (iii).

Put `𝓜 = Hom_{S-gr.}(T, G_{m,S})`; it is a twisted constant `S`-group scheme (Exp. X 5.6). If `G` admits a root system
`R` with respect to `T`, then the inclusion `R ↪ 𝓜(S)` defines a morphism `R_S → 𝓜`, where `R_S` is the constant
`S`-scheme defined by `R`; thanks to condition (ii), one sees easily that this morphism is an open and closed
immersion whose image is none other than `⋃_{α ∈ R} α(S)` (each `α ∈ R` being considered as a section `S → 𝓜`).

Let `𝓡` be the functor of roots of `G` with respect to `T`: by definition, `𝓡(S′)` is the set of roots of `G_{S′}`
with respect to `T_{S′}` for every `S′ → S`; if `S′ = ∅`, one sets `𝓡(∅) = {e}`, and if `S′ ≠ ∅` then the inclusion
`R ↪ 𝓜(S′)` identifies `R` with a root system of `G_{S′}` with respect to `T_{S′}`, and therefore, by 3.7, one has

```text
𝓡(S′) = Hom_{loc. const.}(S′, R),
```

which shows that `𝓡` is representable by `R_S`.

<!-- original page 19 -->

If one now no longer supposes necessarily that `G` possesses a root system relative to `T`, `𝓡` is in any case a
subsheaf of `𝓜` for (fpqc). Locally for this topology, `G` possesses a root system with respect to `T` (take for
example `T` split and use the proof of Th. 2.5). By Exp. IV 4.6.8 and the theory of descent of open (resp. closed)
subschemes,[^N.D.E-XIX-31] one obtains:

**Proposition 3.8.** *Let `S` be a scheme, `G` an `S`-group, `T` a maximal torus of `G`. The functor `𝓡` of roots of
`G` with respect to `T` is representable by a twisted constant finite `S`-scheme (Exp. X 5.1) which is an open and
closed subscheme of `Hom_{S-gr.}(T, G_{m,S})`.*

*For `R ⊂ Hom_{S-gr.}(T, G_{m,S})` to be a root system of `G` with respect to `T`, it is necessary and sufficient that
the morphism `R_S → Hom_{S-gr.}(T, G_{m,S})` defined by the preceding inclusion induce an isomorphism `R_S ⥲ 𝓡`.*

<!-- label: III.XIX.3.8 -->

**3.9.** Let `S` be a scheme, `G` a reductive `S`-group, `T` a maximal torus of `G`, `α` a root of `G` with respect to
`T` (i.e. a section of `𝓡`). Consider the kernel `Ker(α)` of `α`, its unique maximal torus `T_α`, and the centralizer
of the latter, `Z_α = Centr_G(T_α)`. It is an `S`-group closed in `G`, reductive (2.8) of semisimple rank `1` (1.12).
Moreover,

```text
Lie(Z_α/S) = t ⊕ g^α ⊕ g^{−α},
```

so `{α, −α}` is a root system of `Z_α` with respect to `T`.

**3.10.** Let `S` be a scheme, `G` a reductive `S`-group, `T` a maximal torus of `G`, `α` a root of `G` with respect
to `T`. If `q ∈ Q` and if `q α` is a root of `G` with respect to `T`, then `q = 1` or `q = −1`. This follows at once
from 1.12.

## 4. Roots and vector group schemes

<!-- label: III.XIX.4 -->

<!-- original page 20 -->

**4.1.** Let `S` be a scheme, `F` a locally free `O_S`-module of finite type. The `S`-scheme `W(F)` is smooth over
`S`. Its Lie algebra is canonically isomorphic to `F`. Indeed, one has a canonical isomorphism

```text
W(F) ⥲ Lie(W(F)/S) = W(Lie(W(F)/S))
```

(Exp. II, 4.4.1 and 4.4.2). We shall always identify `F` and `Lie(W(F)/S)`.

**Lemma 4.2.** *Let `S` be a scheme, `V` a vector fibration over `S`, smooth over `S`. Then there exists a unique
isomorphism of `O_S`-modules*

```text
exp : W(Lie(V/S)) ⥲ V
```

*inducing the identity on the Lie algebras.* [^N.D.E-XIX-32]

<!-- label: III.XIX.4.2 -->

*Proof.* Indeed, `V = V(F)` for some quasi-coherent `O_S`-module `F`. Since `V` is smooth over `S`, then
`F ≃ ω¹_{V/S}` is locally free of finite type, and therefore

```text
Lie(V/S) = V(ω¹_{V/S}) ≃ W(Lie(V/S)).
```

Moreover, by Exp. II *loc. cit.*, one has a canonical isomorphism

```text
V ⥲ Lie(V/S) ≃ W(Lie(V/S))
```

and one has at once the uniqueness of `exp`, since `W` is fully faithful.

**4.3. Notations.** If `V` is a vector bundle over `S`, one will denote by `V×` the open subset of `V` obtained by
removing the zero section. Write the group law of `V` in multiplicative notation. The action of `O_S` on `V` defining
the module structure will then be written exponentially

```text
O_S × V → V,    (x, v) ↦ v^x.
       S
```

<!-- original page 21 -->

One has `(v v′)^x = v^x v′^x`, `v^{x+x′} = v^x v^{x′}`, `v^{x x′} = (v^x)^{x′}`. In particular, if one restricts the
operator law to `G_{m,S}`, then `V×` is stable and is therefore endowed with a structure of object with group of
operators `G_{m,S}`. We shall again write this law as `(z, v) ↦ v^z`.

**Definition 4.4.1.** [^N.D.E-XIX-33] *Let `L` be an invertible module on `S` and `W(L)` the associated vector bundle.
Then `W(L)×` is a principal homogeneous bundle (locally trivial) under `G_{m,S}`. One denotes
`Γ(S, L)× = W(L)×(S)`.*

<!-- label: III.XIX.4.4.1 -->

**Scholie 4.4.2.** *There is a bijective correspondence between the isomorphisms of `O_S`-modules `O_S ≃ L`, the
isomorphisms of `O_S`-modules `O_S ≃ W(L)`,[^N.D.E-XIX-34] and the sections `S → W(L)×`.*

*This correspondence is effected by `f ↦ W(f) ↦ W(f)(1)`. It is compatible with extension of the base. One may
therefore consider `W(L)×` as the "scheme of trivializations of `W(L)`".*

<!-- label: III.XIX.4.4.2 -->

**4.5.** Let `S` be a scheme, `T` a torus over `S`, `P` an `S`-group with group of operators `G_{m,S}` (for example a
vector bundle), `α` a character of `T`. One denotes `T ·_α P` the semi-direct product of `P` by `T`, where `T` operates
on `P` by the composite morphism

```text
T --α--> G_{m,S} ----> Aut_{S-gr.}(P).
```

**Definition 4.6.** *Let `S` be a scheme, `G` an `S`-group scheme, `T` a subgroup of `G`, `α` a character of `T`, `L`
an `O_S`-module. Let*

```text
p : W(L) → G          [^N.D.E-XIX-35]
```

*be a morphism of `S`-group functors. One says that `p` is* normalized by `T` with multiplier `α` *if it satisfies the
following equivalent conditions:*

*(i) `p` is a morphism of objects with group of operators `T`, if one makes `T` operate on `W(L)` by `α` and on `G` by
inner automorphisms. In other words, for every `S′ → S` and all `t ∈ T(S′)` and `x ∈ W(L)(S′) = Γ(S′, L ⊗ O_{S′})`,
one has*

<!-- original page 22 -->

```text
int(t) p(x) = p(α(t) x).
```

*(ii) The morphism `T ·_α W(L) → G` defined by the product in `G` (i.e. by `(t, x) ↦ t · p(x)`) is a morphism of
groups.*

<!-- label: III.XIX.4.6 -->

**Lemma 4.7.** *Under the conditions of 4.6, suppose moreover that `G` is smooth and has connected
fibers,[^N.D.E-XIX-36] `T` is a maximal torus of `G`, `L` is invertible. If `p` is a monomorphism and `α` non-zero on
each fiber, then `α` is a root of `G` with respect to `T`.*

<!-- label: III.XIX.4.7 -->

*Proof.* Indeed `Lie(p) : L → g` is a monomorphism which factors through `g^α`.

**Proposition 4.8.** *Under the conditions of 4.7, suppose that `G` is reductive, and that `p` is a monomorphism. Then
`α` is a root of `G` with respect to `T` and `Lie(p)` induces an isomorphism*

```text
Lie(p) : L ⥲ g^α.
```

<!-- label: III.XIX.4.8 -->

*Proof.* Indeed, by virtue of 4.7 and the fact that `g^α` is invertible, it suffices to prove that `α` is non-zero on
each fiber. Let then `s ∈ S` be such that `α_s = 0` (= `1` in multiplicative notation). If `X` is a non-zero section of
`L ⊗_S κ(s)`, then `p(X)` is a unipotent element `≠ e` of `G(s̄)` which centralizes `T_s̄`, which is impossible, since
the latter is its own centralizer.

**Corollary 4.9.** *Under the conditions of 4.8, there exists a monomorphism of groups with operators `T` (i.e.
normalized by `T` with multiplier `α`)*

```text
W(g^α) → G
```

*which induces on the Lie algebras the canonical morphism `g^α → g`.*

<!-- label: III.XIX.4.9 -->

We shall see shortly that 4.9 is verified in fact whenever `G` is a reductive group and `α` a root of `G` with respect
to `T`, and that such a morphism is unique.

<!-- original page 23 -->

**Reminder 4.10.** *Let `k` be an algebraically closed field, `G` a reductive `k`-group, `T` a maximal torus of `G`,
`α` a root of `G` with respect to `T`. There exists a monomorphism*

```text
p : G_{a,k} → G
```

*normalized by `T` with multiplier `α`.*

<!-- label: III.XIX.4.10 -->

See *Bible*, § 13.1, Th. 1.

**4.11.** Let us conclude this section with a technical result that will be useful to us. Let `S` be a scheme, and `L`
an invertible `O_S`-module. Let `q` be an integer `> 0` such that `x ↦ x^q` is an endomorphism of the `S`-group
`G_{a,S}`. (If `S ≠ ∅`, one has `q = 1`, or `q = p^n`, `p` being a prime number that is zero on `S`; this follows at
once from the elementary fact: the gcd of the binomial coefficients `(q choose i)`, for `i ≠ 0, q`, is `p` if
`q = p^n`, `p` prime, and `1` in the contrary case.) The morphism defined by the `q`-th power

```text
L → L^{⊗q}
```

is a morphism of sheaves of abelian groups. It defines by base change a morphism of `S`-group schemes:

```text
W(L) → W(L^{⊗q}).
```

In particular, if `L′` is another invertible module and if one has a morphism of `O_S`-modules

```text
h : L^{⊗q} → L′,
```

one deduces from it a morphism of `S`-group schemes:

<!-- original page 24 -->

```text
W(L) → W(L′),    x ↦ h(x^q).
```

These notations laid down, one has:

**Proposition 4.12.** *Let `S` be a scheme, `T` (resp. `T′`) an `S`-torus, `L` (resp. `L′`) an invertible `O_S`-module,
`α` (resp. `α′`) a character of `T` (resp. `T′`).[^N.D.E-XIX-37] Let `f : T → T′` be a morphism of groups and
`g : W(L) → W(L′)` a morphism of `S`-schemes (not necessarily a morphism of `S`-groups) satisfying the following
condition:*

```text
(⋆)    g(α(t) x) = α′(f(t)) g(x)
```

*for all `x ∈ W(L)(S′)`, `t ∈ T(S′)`, `S′ → S`. Let `s₀ ∈ S` be such that `α_{s₀} ≠ 0`.*

*a) Suppose that `g` sends the zero section to the zero section and that for every integer `n > 0`, one has
`(α′ ∘ f)_{s₀} ≠ n α_{s₀}`. Then `g = 0` in a neighborhood of `s₀`.*

*b) Suppose that `g` is a morphism of groups such that `g_{s₀} ≠ 0`. Then there exist an open subset `U` of `S`
containing `s₀` and an integer `q > 0` such that `x ↦ x^q` is an endomorphism of `G_{a,U}` and `(α′ ∘ f)_U = q α_U`.*

*c) Suppose that `(α′ ∘ f)_{s₀} = q α_{s₀}`, where `q` is an integer `> 0` such that `x ↦ x^q` is an endomorphism of
`G_{a,S}`. Then there exist an open subset `U` of `S` containing `s₀` and a unique morphism of `O_S`-modules*

```text
h : L^{⊗q}|U → L′|U
```

*such that `g_U` is the composite morphism*

```text
W(L)_U --x↦x^q--> W(L^{⊗q})_U --W(h)--> (L′)_U.
```

<!-- label: III.XIX.4.12 -->

*Proof.* Let us prove (a). Since the conclusion is local on `S`, one may assume that

<!-- original page 25 -->

`W(L) = W(L′) = G_{a,S}` and therefore that `g` is expressed as a polynomial

```text
g(X) = ∑_{n ⩾ 0} a_n X^n,    a_n ∈ Γ(S, O_S).
```

The condition (⋆) linking `f` and `g` is written as an identity in `Γ(S′, O_{S′})[X]`:

```text
∑_{n ⩾ 0} a_n α′(f(t)) X^n = ∑_{n ⩾ 0} a_n α(t)^n X^n,
```

that is, for every `n ⩾ 0`, every `S′ → S` and every `t ∈ T(S′)`,

```text
a_n (α′(f(t)) − α(t)^n) = 0.
```

For each `n ⩾ 0`, let `S_n` be the set of `s ∈ S` such that `(α′ ∘ f)_s = n α_s`. One knows (Exp. IX 5.3) that the
`S_n` are open and closed, and that `(α′ ∘ f)_{S_n} = n α_{S_n}`. Moreover, since `α_{s₀} ≠ 0`, one may, shrinking `S`
if necessary, assume that `α` is non-zero on each fiber (same reference), which entails that the `S_n` are disjoint.
Shrinking `S` if necessary, one may therefore assume that one is in one of the two following cases: there exists an
`n` such that `S = S_n`, or all the `S_n` are empty.

Let `m ⩾ 0` be such that `S_m = ∅`; I claim that then `a_m = 0`; indeed `α′ ∘ f` and `m α` are distinct on each fiber
of `S`, and one has:

**Lemma 4.13.** *Let `S` be a scheme, `T` an `S`-torus, `α` and `α′` two characters of `T` distinct on each fiber;
there exists a family `{S_i → S}` covering for (fpqc), and for each `i` a `t_i ∈ T(S_i)`, such that
`α(t_i) − α′(t_i) = 1`.*

<!-- label: III.XIX.4.13 -->

*Proof.* The lemma is trivial, by reduction to the diagonalizable case, then to the case `T = G_{m,S}`.

Let us resume the proof of Proposition 4.12; we have just proved (a). In cases (b) and (c), there exists an `n` such
that `S = S_n` (with `n = q` in (c)). By the preceding result, one has therefore `a_m = 0` for `m ≠ n`, which proves
that `g` is written

<!-- original page 26 -->

```text
g(X) = a_n X^n,    a_n ∈ Γ(S, O_S).
```

This proves (c) at once. In case (b), one knows that `a_n(s₀) ≠ 0`, one may therefore assume `a_n` invertible on `S`,
which entails that `x ↦ x^n` is an endomorphism of `G_{a,S}` (by virtue of the hypothesis of (b)) and completes the
proof.

## 5. An instructive example

<!-- label: III.XIX.5 -->

**5.1.** Let `k` be an algebraically closed field of characteristic `0`. Put `A = k[t]`, the polynomial ring in one
variable over `k`, and `S = Spec(A)`. Consider the following Lie algebra `g` over `O_S`: as a module, it is free of
dimension `3`, with basis `{X, Y, H}`; the multiplication table is

```text
[X, Y] = 2t H,    [H, X] = X,   [H, Y] = −Y.
```

For `s ∈ S`, `s ≠ s₀` (the point defined by `t = 0`), the fiber `g(s) = g ⊗_A κ(s)` is isomorphic to the Lie algebra of
the group `PGL_{2, κ(s)}`. For `s = s₀`, it is a solvable Lie algebra.

**5.2.** Let `G₁` be the group scheme of automorphisms of `g`: for every `S′ → S`, `G₁(S′)` is the group of
automorphisms of the `O_{S′}`-Lie algebra `g ⊗_{O_S} O_{S′}`. It is a closed subscheme of the group `GL(g)` of
automorphisms of the `O_S`-module `g`. Let `S′ → S` and `u ∈ M₃(Γ(S′, O_{S′}))` considered as an endomorphism of the
`O_S`-module `g ⊗_{O_S} O_{S′}`:

<!-- original page 27 -->

```text
u(X) = a X + b Y + e H,
u(Y) = b′ X + a′ Y + e′ H,
u(H) = c X + c′ Y + d H.
```

One sees at once that `u` is a section of `G₁` if and only if `det(u)` is invertible and one has the
relations:[^N.D.E-XIX-38]

```text
(1)  a(d − 1) = e c,            (1′)  a′(d − 1) = e′ c′,
(2)  b(d + 1) = e c′,           (2′)  b′(d + 1) = e′ c,
(3)  e = 2t(b c − a c′),        (3′)  e′ = 2t(b′ c′ − a′ c),
(4)  2t c = e b′ − a e′,        (4′)  2t c′ = b e′ − e a′,
                       (5)  2t(a a′ − b b′) = 2t d.
```

**Lemma 5.3.** *The relations (1), (1′), (2), (2′) imply*

```text
det(u) = a a′ (2 − d) + b b′ (d + 2),
a a′ − b b′ = d · det(u).
```

<!-- label: III.XIX.5.3 -->

*Proof.* Indeed, the first assertion is obtained at once by inserting the relations (1), (1′), (2), (2′) into the
expansion of `det(u)`:

```text
det(u) = a a′ d + b e′ c + b′ c′ e − a′ e c − a e′ c′ − b b′ d
       = a a′ d + b b′ (d + 1) + b b′ (d + 1) − a a′ (d − 1) − b b′ d − a a′ (d − 1)
       = a a′ (d − d + 1 − d + 1) + b b′ (d + 1 + d + 1 − d)
       = a a′ (2 − d) + b b′ (d + 2).
```

Multiplying this relation by `d`, one obtains

```text
d · det(u) = a a′ (2d − d²) + b b′ (d² + 2d).
```

But the relation (1) × (1′) = (2) × (2′) gives at once

<!-- original page 28 -->

```text
a a′ (d − 1)² = b b′ (d + 1)².
```

Combining the two preceding relations, one finds at once the second sought formula.

**5.4.** Consider then `G = G₁ ∩ SL(g)`. It is the closed subgroup of `G₁` defined by the equation `det(u) = 1`. It is
therefore an affine group over `S`.

**Proposition 5.5.** *The group `G` is smooth over `S`.*

<!-- label: III.XIX.5.5 -->

To prove the proposition, we shall need the following lemmas.

**Lemma 5.6.** *Let `U` be the open subset of `End_A(g) ≃ W(M₃(O_S))` defined by the condition "the product `a d` is
invertible", i.e. the open subset `End_A(g)_f`, where `f` is the function defined by `f(u) = a d`. Then `U ∩ G` is the
closed subscheme of `U` defined by the six equations:*

```text
(1),  (2),  (2′),  (3),  (3′)   and   (D) : a a′ − b b′ = d.
```

<!-- label: III.XIX.5.6 -->

*Proof.* It is first clear that these six relations are verified by every "point" of `G` (Lemma 5.3), in particular by
every "point" of `U ∩ G`. Conversely, it must be shown that if `u ∈ U(S′)` (for every `S′ → S`), and if `u` verifies
the six conditions of the statement, then `det(u) = 1` and `u` also verifies (1′), (4), (4′) and (5).

One has first (D) ⇒ (5). By (2) and (2′), one has

```text
b b′ (d + 1) = b c e′ = b′ c′ e.
```

But by (3) and (3′), writing `2t(b c − a c′)(b′ c′ − a′ c)` in two ways:

```text
(b c − a c′) e′ = (b′ c′ − a′ c) e.
```

Combining with the preceding relation, this gives `a c′ e′ = a′ c e`. But by (1), `a′ c e = a′ a (d − 1)`, which proves
`a (a′ (d − 1) − e′ c′) = 0` and entails (1′), since `a` is supposed invertible.

Thus, (1), (2), (2′) and (1′) are verified, hence by Lemma 5.3 and (D) one has `d(det(u) − 1) = 0`. Since `d` is
supposed invertible, this entails `det(u) = 1`.

Let us prove (4) and (4′). Let us do it for example for (4′), the other calculation being deduced from it by symmetry.

<!-- original page 29 -->

By (3), (3′) and (D), one has at once

```text
a′ e + b e′ = −2t(a a′ − b b′) c′ = −2t d c′.
```

Combining (1′) and (2), one has also[^N.D.E-XIX-39]

```text
a′ e + b e′ = −d(b e′ − e a′),
```

which completes the proof of (4′), `d` being supposed invertible.

**Lemma 5.7.** *`G` is smooth over `S` along the unit section.*

<!-- label: III.XIX.5.7 -->

*Proof.* By 5.6 and SGA 1, II 4.10, it suffices to prove that the differentials of the functions

```text
a(d − 1) − e c,    b(d + 1) − e c′,    b′(d + 1) − e′ c,
e − 2t(b c − a c′),    e′ − 2t(b′ c′ − a′ c),    a a′ − b b′ − d,
```

at the points of the unit section of `G` are linearly independent. But denoting by a capital letter the differential of
the corresponding lower-case, these are[^N.D.E-XIX-40]

```text
D,    2B,    2B′,    E + 2t C′,    E′ + 2t C,    A + A′ − D,
```

which are indeed linearly independent modulo every `(t − λ)`, `λ ∈ k`.[^N.D.E-XIX-41]

**Lemma 5.8.** *For `s ∈ S`, `s ≠ s₀`, the fiber `G_s` is connected and semisimple.*

<!-- label: III.XIX.5.8 -->

*Proof.* [^N.D.E-XIX-42] Indeed, since `s ≠ s₀`, `g(s)` is isomorphic to the Lie algebra of `PGL_{2, κ(s)}` and, on the
other hand, one has `G_s = (G₁)_s`; but it is known that the group of automorphisms of the Lie algebra of `PGL_2` over
a field of characteristic `0` is `PGL_2` itself, which is connected and semisimple.

**Lemma 5.9.** *The fiber `G_{s₀}` is solvable and has two connected components which are of the following form:*

```text
              ⎛ a   0   0 ⎞                          ⎛ 0    b   0 ⎞
G⁰_{s₀} =     ⎜ 0  a⁻¹  0 ⎟      and     G⁻_{s₀} =   ⎜ b⁻¹  0   0 ⎟ .
              ⎝ c   c′  1 ⎠                          ⎝ c    c′ −1 ⎠
```

<!-- label: III.XIX.5.9 -->

<!-- original page 30 -->

*Proof.* Indeed, one has `e = e′ = 0`, since `t = 0` at `s₀`. One then solves immediately the equations (1), (1′), … (5)
and (D).

**Lemma 5.10.** *The matrix*

```text
      ⎛ 0   1   0 ⎞
w =   ⎜ 1   0   0 ⎟
      ⎝ 0   0  −1 ⎠
```

*is a section of `G` over `S`, such that `w(s₀) ∈ G⁻_{s₀}`.*

<!-- label: III.XIX.5.10 -->

Let us now prove 5.5.[^N.D.E-XIX-43] Denote by `G⁰` the union of the neutral components of the fibers of `G` (that is to
say the complement of `G⁻_{s₀}`); since `G` is smooth over `S` along the unit section (5.7), `G⁰` is an open subgroup of
`G`, smooth over `S`, by VI_B, 3.10. Since, by translation, `G` is evidently smooth at the points of `w(S)`, `G` is
smooth over `S`.

**5.11.** Consider the morphism `G_{m,S} → G⁰` defined by

```text
        ⎛ z   0   0 ⎞
z ↦     ⎜ 0  1/z  0 ⎟ .
        ⎝ 0   0   1 ⎠
```

It is a monomorphism that defines a torus `T` of `G⁰`. I claim that one has

```text
T = Centr_G(T) = Centr_{G⁰}(T).
```

It suffices indeed to verify the first equality. Since these are smooth subgroups of `G` over `S`, it suffices to
verify that they have the same geometric points. For the fibers at points `s ≠ s₀`, this follows from the fact that
`PGL_{2, κ(s)}` is reductive and that `T_s` is a maximal torus of it for reasons of dimensions (cf. 1.11). On the fiber
at `s₀`, the computation is done immediately. It follows in particular that `T` is a maximal torus of `G` and of `G⁰`.

**5.12.** The section `w` of `G` defined in 5.9 normalizes `T`. It follows at once (cf. 2.4) that the Weyl group of `G`
is isomorphic to `(Z/2Z)_S`, and in particular finite over `S`.

<!-- original page 31 -->

```text
W_G(T) = Norm_G(T) / T = (Z/2Z)_S.
```

On the other hand, `W_{G⁰}(T)` is not finite over `S`: it "lacks a point" above `s₀`.

**5.13.** The open immersion `G⁰ → G` is not a closed immersion (since `G⁰` is dense in `G`); it is however an affine
morphism (and therefore `G⁰` is affine over `S`). Indeed, since `G⁰_{s₀}` is closed in `G_{s₀}`, which is closed in `G`,
the complement `U` of `G⁰_{s₀}` in `G` is open; `G⁰` and `U` form an open covering of `G` and it suffices to verify that
the immersions `G⁰ → G⁰` and `G⁰ ∩ U → U` are affine; for the first this is trivial, for the second, one notes that
`U ∩ G⁰` is defined in `U` by the equation `b ≠ 0`.

We have therefore constructed an affine smooth `S`-group, with connected fibers, `G⁰`, possessing a maximal torus `T`
which is its own centralizer and whose Weyl group `W_{G⁰}(T)` is not finite (compare with Theorem 2.5).

## 6. Local existence of maximal tori. The Weyl group

<!-- label: III.XIX.6 -->

In the course of the proof of 2.5, we used a result from Exp. XI on the local existence for the étale topology of
maximal tori; the proof of Exp. XI uses a fine representability result (XI 4.1). In the particular case which occupies
us, one may give another proof, based on the ideas of Exp. XII no. 7, and of a much more elementary nature.

**Proposition 6.1.** *Let `S` be a scheme, `G` a smooth, affine `S`-group scheme with connected fibers over `S`, `s₀` a
point of `S` such that the maximal tori of the geometric fiber `G_{s̄₀}` are their own centralizer. There exists an
étale morphism `S′ → S` covering `s₀`, and a split maximal torus `T` of `G_{S′}`.*

<!-- label: III.XIX.6.1 -->

<!-- original page 32 -->

*Proof.* First, one may assume `S` affine.[^N.D.E-XIX-44] Since `G` is of finite presentation over `S`, one may assume
`S` noetherian, then local, then henselian with separably closed residue field (cf. EGA IV, 8.12, § 8.8, and § 18.8).
Set therefore `S = Spec(A)`, `A` henselian with separably closed residue field `k = κ(s₀)`. Choose a maximal torus `T₀`
of `G₀ (= G_k)` (one exists, for example because the scheme of maximal tori of `G₀` is smooth over `k`, Exp. XII,
7.1 c)); since `k` is separably closed, `T₀` is split (cf. X 1.4) and is therefore given by a monomorphism of groups

```text
f₀ : G^r_{m,k} → G₀.
```

Let `m` be an integer `> 1` prime to the characteristic of `k`. By Exp. VIII 6.7, for every `h > 0`,
`Centr_{G₀}(_{m^h}T₀)` is representable by a closed subscheme of `G₀`. Since the `_{m^h}T₀` are schematically dense in
`T₀` (cf. Exp. IX 4.10) and `G₀` is noetherian, there exists an `h` such that

```text
Centr_{G₀}(_{m^h}T₀) = Centr_{G₀}(T₀) = T₀.
```

Put `n = m^h`; since `n` is invertible on `S`, `_n G_{m,S}` is isomorphic to `(Z/nZ)_S`; `f₀` therefore defines a
monomorphism of groups

```text
u₀ : (Z/nZ)^r_k → G₀
```

such that `Centr_G(u₀) = T₀`. Now the `S`-functor

```text
𝓟 = Hom_{S-gr.}((Z/nZ)^r_S, G)
```

is representable by an `S`-scheme of finite type (as a closed subscheme of `r` copies of
`_n G = Hom_{S-gr.}((Z/nZ)_S, G) = Ker(G --n--> G)`). But `𝓟` is smooth over `S` (Exp. IX 3.6), hence `u₀ ∈ 𝓟(k)`
lifts to a section `u ∈ 𝓟(S)` (Hensel's lemma, Exp. XI 1.11):

<!-- original page 33 -->

```text
u : (Z/nZ)^r_S → G.
```

Consider `H = Centr_G(u)`; it is a closed subgroup scheme of `G`, by Exp. VIII 6.5 e), and one has `H₀ = T₀` by
hypothesis.[^N.D.E-XIX-45] Moreover, `H` is smooth over `S`: indeed, let `S′ = Spec(A)` be an affine scheme over `S`,
`u′ : (_n G_{m,S′})^r → G_{S′}` the morphism deduced from `u` by base change, `S′_J = Spec(A/J)`, where `J` is an ideal
of square zero, and let `x ∈ H(S′_J)`; since `G` is smooth, `x` lifts to an element `g` of `G(S′)`; then
`v = int(g)(u′)` verifies `v_J = u′_J` and therefore, by IX 3.2, there exists an element `g′` of `G(S′)` such that
`g′_J = e` and `int(g′)(v) = u′`; then `h = g′ g` belongs to `H(S′)` and verifies `h_J = x`.

Let then `H⁰` be the neutral component of `H`; it is a subgroup scheme of `G`, smooth and with connected fibers,
whose special fiber is a torus. By Exp. X 8.1, it is a torus, necessarily split (Exp. X 4.6). Put `H⁰ = T` and let
`C = Centr_G(T)`, which is a closed subgroup of `G` (Exp. VIII 6.5 e)), smooth (Exp. XI 2.4). Consider `C⁰` (in fact
`C⁰ = C`, but we do not need to know it); then `C⁰ ⊃ T` and these are two smooth groups with connected fibers. They
coincide at `s₀`, hence in a neighborhood. Shrinking `S` if necessary, one may therefore assume `C⁰ = T`, hence *a
fortiori* `T` maximal.

**Remark 6.2.** *The proof shows in particular that the reductive rank of `G_s̄` is constant in a neighborhood of
`s = s₀`.*

<!-- label: III.XIX.6.2 -->

**Proposition 6.3.** *Let `S` be a scheme, `G` an `S`-group scheme smooth and of finite presentation over `S`, `Q` a
subtorus of `G`.*

*(i) `Centr_G(Q)` and `Norm_G(Q)` are representable by closed subgroup schemes, smooth (and therefore of finite
presentation) over `S`.*

*(ii) `Centr_G(Q)` is an open and closed subscheme of `Norm_G(Q)`. The quotient `W_G(Q) = Norm_G(Q) / Centr_G(Q)` is
representable by an open subgroup scheme of `Aut_{S-gr.}(Q)`; it is therefore an `S`-group scheme quasi-finite, étale
and separated over `S`.*

<!-- original page 34 -->

*(iii) For every `s ∈ S`, put*

```text
w(s) = Norm_{G(s̄)}(Q(s̄)) / Centr_{G(s̄)}(Q(s̄)).
```

*Then `s ↦ w(s)` is lower semicontinuous, and is constant in a neighborhood of `s` if and only if `W_G(Q)` is finite
over `S` in a neighborhood of `s`.*

<!-- label: III.XIX.6.3 -->

*Proof.* By Exp. XI 6.11, `Centr_G(Q)` and `Norm_G(Q)` are representable by closed subschemes of finite presentation of
`G`. These are smooth by Exp. XI 2.4 and 2.4 bis, which proves (i). Assertions (ii) and (iii) are then proved as in
Exp. XI 5.9 and 5.10, whose proof uses in fact only (i) and not the fine theorems Exp. XI 4.1 and 4.2.

## Bibliography

[Bible] C. Chevalley (with the collaboration of P. Cartier, A. Grothendieck, M. Lazard), *Classification des groupes de
Lie algébriques*, 1956–58.

[Ch05] C. Chevalley, *Classification des groupes algébriques semi-simples* (with the collaboration of P. Cartier,
A. Grothendieck, M. Lazard), Collected Works, vol. 3, Springer, 2005.

[Tô55] C. Chevalley, *Sur certains groupes simples*, Tôhoku Math. J. (2) **7** (1955), 14–66.

[TO70] J. Tate & F. Oort, *Group schemes of prime order*, Ann. Scient. Éc. Norm. Sup. (4), t. **3** (1970), 1–21.

## Footnotes

[^N.D.E-XIX-0]: *N.D.E.*: Version of 13/10/2024.

[^N.D.E-XIX-1]: *N.D.E.*: See the bibliographical references at the end of this Exposé. In particular, a re-edition of
    the *Séminaire Chevalley 1956–58*, cited [Bible], revised by P. Cartier, was published in 2005,
    cf. [Ch05].

[^N.D.E-XIX-2]: *N.D.E.*: More precisely, Proposition XVIII 2.3 (extension of a "generic homomorphism" between groups)
    is used in XXII 4.1.11 and then in Exp. XXIII (proof of the uniqueness theorem), and also in Exp. XXIV;
    Theorem XVIII 3.7 (construction of a group from a group germ) is used only in Exp. XXV.

[^N.D.E-XIX-3]: *N.D.E.*: The reference 9-06 (= Exp. 9, p. 6) has been replaced by § 9.4 (= Exp. 9, § 4), which applies
    equally well to [Bible] and to [Ch05]. When the numbering of [Ch05] differs from [Bible], which is the
    case in Exp. 6, both references will be indicated explicitly.

[^N.D.E-XIX-4]: *N.D.E.*: The following has been detailed.

[^N.D.E-XIX-5]: *N.D.E.*: These notations, which figured in 2.3 of the original, have been inserted here; on the other
    hand, the statement and proof of 1.4 have been detailed.

[^N.D.E-XIX-6]: *N.D.E.*: See also the additions made in VI_B, 6.2.4 (d) and 6.5.5 (a).

[^N.D.E-XIX-7]: *N.D.E.*: 1.6 has been transformed into 1.6.1 to 1.6.3. Note that in this Séminaire every reductive
    (resp. semisimple, cf. 1.8) `k`-group is, by definition, connected.

[^N.D.E-XIX-8]: *N.D.E.*: The following has been detailed.

[^N.D.E-XIX-9]: *N.D.E.*: The following sentence has been added.

[^N.D.E-XIX-10]: *N.D.E.*: The following has been detailed.

[^N.D.E-XIX-11]: *N.D.E.*: See also the addition VI_B, 6.2.6.

[^N.D.E-XIX-12]: *N.D.E.*: i.e., the connected component of `Ker(α)`.

[^N.D.E-XIX-13]: *N.D.E.*: Note that if `U`, `L` are two subgroup schemes of `G`, one has
    `Lie(U) ∩ Lie(L) = Lie(U ∩ L)`.

[^N.D.E-XIX-14]: *N.D.E.*: The following sentence has been added.

[^N.D.E-XIX-15]: *N.D.E.*: The following has been added.

[^N.D.E-XIX-16]: *N.D.E.*: The following has been detailed.

[^N.D.E-XIX-17]: *N.D.E.*: The following has been detailed. Note, on the other hand, that section 6 is independent of
    the rest of this Exposé.

[^N.D.E-XIX-18]: *N.D.E.*: The hypothesis entails that `A` is locally free of rank `2`, and since the augmentation
    ideal `I` is a direct factor of `A`, then, replacing `U` by a sufficiently small affine open subset
    `Spec(R)`, one may assume that `I = Γ(U, I)` is a free `R`-module of rank `1`. If `x` is a generator of
    `I`, one then has `x² = a x` for a certain `a ∈ R`, and the hypothesis that `A = Γ(U, A)` be étale
    entails that `a` is invertible in `R`, and one then sees easily that `A` is the affine algebra of the
    constant `R`-group `Z/2Z` (compare with the first lines of [TO70]).

[^N.D.E-XIX-19]: *N.D.E.*: This paragraph of notations and reminders has been added.

[^N.D.E-XIX-20]: *N.D.E.*: "Split" has been added.

[^N.D.E-XIX-21]: *N.D.E.*: The proof has been detailed.

[^N.D.E-XIX-22]: *N.D.E.*: which is independent of the rest of this Exposé.

[^N.D.E-XIX-23]: *N.D.E.*: In all this volume, "trivial torus" has been replaced by "split torus".

[^N.D.E-XIX-24]: *N.D.E.*: The preceding sentence has been added.

[^N.D.E-XIX-25]: *N.D.E.*: Note that, `g` being a finite locally free `O_S`-module, `R` is a finite set.

[^N.D.E-XIX-26]: *N.D.E.*: The following sentence has been detailed.

[^N.D.E-XIX-27]: *N.D.E.*: This statement has been made into a lemma, in order to put it in evidence.

[^N.D.E-XIX-28]: *N.D.E.*: The original added the hypothesis that `G` be of finite presentation over `S`, which does
    not seem to be used in what follows. In any case, `G` being smooth over `S` and with connected fibers,
    it is quasi-compact and separated over `S` (VI_B, 5.5), hence of finite presentation over `S`.

[^N.D.E-XIX-29]: *N.D.E.*: The original has been simplified; it invoked Exp. IX, 5.2. Let us note, however, that
    *loc. cit.*, 5.3 shows that if `S` is connected, then the conditions of the lemma are verified as soon
    as (i) is verified at one point `s` of `S`.

[^N.D.E-XIX-30]: *N.D.E.*: The following has been modified, in order to recall the hypotheses of 3.2 and to add that
    `T` is a maximal torus.

[^N.D.E-XIX-31]: *N.D.E.*: see SGA 1, VIII 4.4 or EGA IV₂, 2.7.1.

[^N.D.E-XIX-32]: *N.D.E.*: We have kept the original proof; one can also detail it as follows. Let `F` be a
    quasi-coherent `O_S`-module, `V = V(F)`. Denote by `π` the projection `V → S` and `ε` the zero section
    `S → V`. Then `Ω¹_{V/S} = π* F`, whence

    ```text
    (1)    ω¹_{V/S} = ε* Ω¹_{V/S} ≃ ε* π* F ≃ F,
    ```

    and therefore `Lie(V/S) = (ω¹_{V/S})ⱽ ≃ Fⱽ`. If one supposes `V` smooth over `S` then, by (1), `F` is
    locally free of finite type, and therefore

    ```text
    (2)    V = V(F) ≃ W(Fⱽ) ≃ W(Lie(V/S)).
    ```

    Now, if `U` is an `S`-scheme equipped with a section `τ : S → U`, and if one is given an isomorphism
    `φ : V ⥲ U` of "pointed" `S`-schemes, i.e. such that `φ ∘ ε = τ` (for example if `U` is an `S`-group),
    then `φ` induces an isomorphism `dφ : Fⱽ ⥲ Lie(U/S)`, whence an isomorphism `ψ : W(Fⱽ) ⥲ W(Lie(U/S))`
    making the appropriate diagram commute, which permits one to identify `U` with `W(Lie(U/S))`. Since the
    functor `W` is fully faithful, there exists a unique isomorphism `exp : W(Lie(U/S)) ⥲ U` such that
    `Lie(ψ⁻¹ ∘ exp) = id`. In fact, one can see directly that `Lie(ψ) = id`, so that `exp = ψ`.

[^N.D.E-XIX-33]: *N.D.E.*: For later references, 4.4 has been transformed into 4.4.1 and 4.4.2.

[^N.D.E-XIX-34]: *N.D.E.*: Here, one identifies the vector bundle `W(L)` with the functor in `O_S`-modules that it
    represents.

[^N.D.E-XIX-35]: *N.D.E.*: Here, one has written `W(L)` (with `W` in boldface) since, for an arbitrary `O_S`-module
    `L`, `W(L)` is not necessarily representable. But in what follows, `L` will be assumed locally free of
    finite rank (and even invertible), in which case the functor is representable by the vector bundle
    `V(Lⱽ)`, and one will denote it simply `W(L)`.

[^N.D.E-XIX-36]: *N.D.E.*: cf. N.D.E. (28).

[^N.D.E-XIX-37]: *N.D.E.*: "consider the semi-direct product `T ·_α W(L)`, resp. `T′ ·_{α′} W(L′)`" has been removed.
    On the other hand, the hypothesis in (b) that `g` be a morphism of groups, combined with (⋆), amounts
    to saying that the morphism `(t, x) ↦ (f(t), g(x))` is a morphism of groups from `T ·_α W(L)` to
    `T′ ·_{α′} W(L′)`.

[^N.D.E-XIX-38]: *N.D.E.*: The equality `[u(X), u(Y)] = 2 t u(H)` (resp. `[u(H), u(X)] = u(X)`,
    resp. `[u(H), u(Y)] = −u(Y)`) gives the relations (4), (4′), and (5) (resp. (1)–(3), resp. (1′)–(3′)).

[^N.D.E-XIX-39]: *N.D.E.*: The sign has been corrected.

[^N.D.E-XIX-40]: *N.D.E.*: `A + A′ + B` has been corrected to `A + A′ − D`.

[^N.D.E-XIX-41]: *N.D.E.*: "`(t − a)`, `a ∈ A`" has been corrected to "`(t − λ)`, `λ ∈ k`".

[^N.D.E-XIX-42]: *N.D.E.*: The following sentence has been slightly modified.

[^N.D.E-XIX-43]: *N.D.E.*: The following sentence has been modified, by adding the reference to VI_B, 3.10.

[^N.D.E-XIX-44]: *N.D.E.*: The preceding sentence as well as the reference to EGA IV in what follows have been added.

[^N.D.E-XIX-45]: *N.D.E.*: The reference VIII 6.5 e) has been added in what precedes, and the following sentence has
    been detailed.

<!-- LEDGER DELTA — Exposé XIX — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| rang réductif (`rgred`) | reductive rank (`rgred`) | Notation preserved. |
| rang semi-simple (`rgss`) | semisimple rank (`rgss`) | Notation preserved. |
| rang nilpotent | nilpotent rank | Standard. |
| rang unipotent | unipotent rank | Standard. |
| rang infinitésimal | infinitesimal rank | Standard. |
| radical (`rad(G)`) | radical (`rad(G)`) | Standard. |
| radical unipotent (`rad_u(G)`) | unipotent radical (`rad_u(G)`) | Notation `rad_u` preserved. |
| tore singulier | singular torus | Standard. |
| tore déployé | split torus | Replaces "tore trivial" of the original (per N.D.E. 23). |
| tore trivialisé | trivialized torus | When equipped with a chosen isomorphism. |
| Scholie | Scholie | Kept as a heading register; not modernized to "Scholium" within the section title block. |
| caractère | character | Standard. |
| schéma des invariants (`H^Q`) | scheme of invariants (`H^Q`) | Standard. |
| produit semi-direct | semi-direct product | Standard. |
| fibration vectorielle | vector fibration | Standard; per Exp. II usage. |
| fibré vectoriel | vector bundle | Standard. |
| section unité (`ε`) | unit section (`ε`) | Standard. |
| W(F), V(F) | `W(F)`, `V(F)` | Notation preserved; `W` is the functor of sections, `V` the geometric vector fibration. |
| morphisme normalisé par T avec le multiplicateur α | morphism normalized by `T` with multiplier `α` | Per Def. 4.6. |
| groupe constant tordu | twisted constant group | Standard. |
| foncteur des racines (`𝓡`) | functor of roots (`𝓡`) | Notation preserved (script `𝓡`). |
| Lemme de Hensel | Hensel's lemma | Standard. |
| théorème de densité | density theorem | Standard. |
| Bible | *Bible* | Italicized title for Chevalley Seminar. |
| Tôhoku (groupes de) | *Tôhoku* (groups) | Kept with circumflex. |
| `s̄` | `s̄` | Spectrum of an algebraic closure of `κ(s)`; per Notations 1.4.0. |
-->


