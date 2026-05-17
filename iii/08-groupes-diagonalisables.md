# Exposé VIII. Diagonalizable groups

<!-- label: III.VIII -->

*by A. Grothendieck*

> Version 1.1 of 8 November 2009: additions in 1.2, 1.4, 1.7, 3.1, 3.4, 4.5.1, 6.4, 6.8 — 1.5.1 and section 7 to be
> revised.[^VIII-0-0]

## 1. Biduality

<!-- original page 1 -->

Let `C` be a category, which we identify, as is usual, with a full subcategory of `Ĉ = Hom(C°, (Ens))` (cf. Exp. I). Let
`I` be a commutative group functor, i.e. an object of `Ĉ` endowed with a commutative group structure (cf. I,
2.1).[^N.D.E-VIII-1] For every `X ∈ Ob(Ĉ)`, the object `Hom(X, I)` carries a commutative group structure induced by that
of `I`. For every group `G` in `Ĉ`, let

```text
D(G) = Hom_gr.(G, I)
```

be the subobject of `Hom(G, I)` defined, for every `S ∈ Ob(C)`, by

```text
(*)    D(G)(S) = Hom_{S-gr.}(G_S, I_S),
```

<!-- label: eq:III.VIII.1.0-star -->

where `G_S = G × S` and `I_S = I × S` are considered as `S`-groups, i.e. groups in `Ĉ/S`. Then `D(G)` is a `Ĉ`-subgroup
of `Hom(G, I)`. In this way one obtains a contravariant functor `D` from the category of `Ĉ`-groups to the category of
commutative `Ĉ`-groups.

The right-hand side of `(*)` can also be interpreted as the subset of `Hom(G × S, I)` consisting of morphisms
`G × S → I` which are "multiplicative with respect to the first argument `G`". Moreover, the preceding formulas remain
valid more generally when `S` is an arbitrary object of `Ĉ`, not necessarily coming from `C`.

If we now take for `S` a group in `Ĉ`, which we shall denote `G′`, then in the left-hand side `Hom(G′, D(G))` of `(*)`
we can single out the subset `Hom_gr.(G′, D(G))` consisting of morphisms that respect the group structures of `G′` and
`D(G)`.

<!-- original page 2 -->

It then corresponds to the subset of `Hom(G × G′, I)` consisting of morphisms that are multiplicative with respect to
the first and with respect to the second argument — which one may call *bilinear morphisms from `G × G′` to `I`*, or
*pairings of `G` and `G′` with values in `I`*. One thus finds

```text
(**)   Hom_gr.(G′, D(G)) ⥲ Hom_bil.(G × G′, I),
```

<!-- label: eq:III.VIII.1.0-doublestar -->

which is an isomorphism functorial in the pair `(G, G′)`. Since the right-hand side is symmetric in `G` and `G′`, one
deduces a functorial bijection

```text
(***)  Hom_gr.(G′, D(G)) ⥲ Hom_gr.(G, D(G′)).
```

<!-- label: eq:III.VIII.1.0-triplestar -->

In other words, "it amounts to the same thing" to give a group homomorphism `G′ → D(G)` or a group homomorphism
`G → D(G′)`, both reducing in effect to the datum of a pairing `G × G′ → I`.

Applying this to the case `G′ = D(G)` and to the identity homomorphism `G′ → D(G)`, one finds a canonical homomorphism

```text
(****) G → D(D(G)).
```

<!-- label: eq:III.VIII.1.0-quadstar -->

**Definition 1.0.**[^N.D.E-VIII-2] *We say that `G` is* reflexive *(relative to `I`) if the preceding homomorphism is an
isomorphism. We note that this implies that `G` is commutative.*

<!-- label: III.VIII.1.0 -->

One thus sees that:

**Proposition 1.0.1.** *The functor `D` induces an anti-equivalence of the category of reflexive `Ĉ`-groups with
itself.*

<!-- label: III.VIII.1.0.1 -->

In particular, if `G`, `H` are two reflexive groups, `D` induces an isomorphism

```text
Hom_gr.(G, H) ⥲ Hom_gr.(D(H), D(G))
```

(it even suffices that `H` be reflexive, as one sees from formula `(***)`).

<!-- original page 3 -->

**Definition 1.0.2.** *As usual, we shall then say that a `C`-group `G` is* reflexive *if it is reflexive as a `Ĉ`-group
(without worrying whether `D(G)` is representable or not).*

<!-- label: III.VIII.1.0.2 -->

One thus obtains, by `D`, an anti-equivalence of the category of reflexive `C`-groups `G` such that `D(G)` is
representable, with itself.

**Remark 1.0.3.** *To conclude these generalities, let us point out that the formation of duals `D(G)` commutes with
base extension, which therefore transforms reflexive groups into reflexive groups.*

<!-- label: III.VIII.1.0.3 -->

We shall be interested henceforth in the case where `C = (Sch)/S`, the category of preschemes over `S`, and
`I = G_{m,S}`, the "multiplicative group over `S`" (cf. Exp. I). For every ordinary group `M`, we consider the `S`-group
`M_S`. One sees at once that for every prescheme in groups `J` over `S`, there is a canonical isomorphism (functorial in
`M` and `J`, and compatible with base extension):

```text
Hom_{S-gr.}(M_S, J) = Hom_gr.(M, J(S)).
```

Applying this to `J = I = G_{m,S}` and to a variable `S′` over `S`, one finds a functorial isomorphism:

```text
(1.0.4)    D(M_S)(S′) ⥲ Hom_gr.(M, G_m(S′)).
```

<!-- label: eq:III.VIII.1.0.4 -->

One thus recovers the functor already considered in I, 4.4, also denoted `D_S(M)`, which is representable for `M`
commutative, since

```text
D_S(M) = D(M_S) = Spec O_S(M),
```

where `O_S(M)` denotes the algebra of the group `M` with coefficients in `O_S`. (Let us note moreover, in the general
case, that `D(M)` does not change if one replaces `M` by its abelianization, so that no information is lost by assuming
`M` commutative.)

**Definition 1.1.** *A prescheme in groups `G` over `S` is said to be* diagonalizable *if it is isomorphic to a scheme
of the form `D_S(M) = D(M_S) = Hom_{S-gr.}(M_S, G_m)` for some suitable commutative group `M`.*

<!-- label: III.VIII.1.1 -->

<!-- original page 4 -->

*We say that `G` is* locally diagonalizable *if every point of `S` admits an open neighborhood `U` such that `G|U` is
diagonalizable.*

**Theorem 1.2.** *Let `Γ` be a constant commutative group scheme over `S`, i.e. isomorphic to a group scheme of the form
`M_S`, where `M` is an ordinary commutative group. Then `Γ` is reflexive, i.e. the canonical homomorphism*

<!-- label: III.VIII.1.2 -->

```text
Γ → D(D(Γ))
```

*is an isomorphism.*[^N.D.E-VIII-3] *The diagonalizable group `D(M_S)` is therefore also reflexive.*

Taking the definitions into account, this follows from the following statement (which one will apply to a prescheme `S′`
over `S`):

**Corollary 1.3.** *Let `G = D(M_S)`. Then every homomorphism of `S`-groups*

<!-- label: III.VIII.1.3 -->

```text
u : G → G_{m,S}
```

*is defined by a uniquely determined section of `M_S` over `S`, i.e. by a uniquely determined locally constant map from
`S` to `M`.*

*Proof.* Since by definition

```text
G_{m,S} = GL(1)_S = Aut_{O_S-mod.}(O_S),
```

one sees that giving a group homomorphism `G → G_{m,S}` is equivalent to giving on `O_S` a structure of `G`-`O_S`-module
compatible with the natural `O_S`-module structure on `O_S` (cf. I, 4.7). By I, 4.7.3, this also amounts to giving an
`M`-grading on `O_S`, i.e. a decomposition of `O_S` as a direct sum of modules `L_m` (`m ∈ M`).

<!-- original page 5 -->

Now it is well known that a direct factor of a locally free module of finite type is locally free of finite type;
therefore each `L_m` is, in a neighborhood of each point of `S`, either zero or free of rank `1`, and in the latter case
identical to `O_S` in that neighborhood. Let `S_m` be the open subset of `S` consisting of the points where this second
alternative occurs. Expressing that `O_S` is the direct sum of the `L_m`, one sees that the union of the `S_m` is `S`,
and that the `S_m` are pairwise disjoint. Hence giving a group homomorphism `G → G_{m,S}` is equivalent to giving a
decomposition of `S` as a union of pairwise disjoint open subsets `S_m` (`m ∈ M`), i.e. to giving a locally constant map
from `S` to `M`. This establishes 1.3, hence 1.2.

**Corollary 1.4.** *A diagonalizable group is reflexive; the same therefore holds for a locally diagonalizable group. If
`M`, `N` are two ordinary commutative groups, the natural homomorphism*

<!-- label: III.VIII.1.4 -->

```text
Hom_{S-gr.}(M_S, N_S) → Hom_{S-gr.}(D(N_S), D(M_S))
```

*is bijective.*

[^N.D.E-VIII-4] The preceding isomorphism being compatible with base extension, one deduces an isomorphism of
`S`-functors in groups:

```text
(1)    Hom_{S-gr.}(M_S, N_S) ⥲ Hom_{S-gr.}(D(N_S), D(M_S)).
```

<!-- label: eq:III.VIII.1.4.1 -->

For every `S`-prescheme `T`, one has

```text
Hom_{S-gr.}(M_S, N_S)(T) = Hom_gr.(M, Γ(N_T/T)),
```

and, by I 1.8, `Γ(N_T/T)` is the abelian group of locally constant maps `T → N`. On the other hand, let
`Hom_gr.(M, N)_S` be the constant `S`-group associated with the ordinary abelian group `Hom_gr.(M, N)`. One has an
evident homomorphism of `S`-functors in commutative groups:

```text
(2)    Hom_gr.(M, N)_S  -θ→  Hom_{S-gr.}(M_S, N_S),
```

<!-- label: eq:III.VIII.1.4.2 -->

which is always a monomorphism. Moreover, it is an isomorphism if `M` is of finite type.[^N.D.E-VIII-5]

From the foregoing one deduces point (a) of the following corollary; point (b) follows from it by the descent results
"recalled" in 1.7.[^N.D.E-VIII-6]

<!-- original page 6 -->

**Corollary 1.5.** *a) Let `M`, `N` be two ordinary commutative groups, with `M` of finite type. Then one has an
isomorphism*

<!-- label: III.VIII.1.5 -->

```text
Hom_gr.(M, N)_S ⥲ Hom_{S-gr.}(D(N_S), D(M_S));
```

*consequently `Hom_{S-gr.}(D(N_S), D(M_S))` is representable.*

*b) More generally, if `G`, `H` are locally diagonalizable, with `H` of finite type, then `Hom_{S-gr.}(G, H)` is
representable.*

[^N.D.E-VIII-7] From 1.5 one concludes:

**Corollary 1.6.** *Under the conditions of 1.5, if `S` is connected, one has*

<!-- label: III.VIII.1.6 -->

```text
Hom_{S-gr.}(D_S(N), D_S(M)) ⥲ Hom_gr.(M, N)
```

*and*

```text
Isom_{S-gr.}(D_S(N), D_S(M)) ⥲ Isom_gr.(M, N).
```

### 1.7. Descent of representability

<!-- label: III.VIII.1.7 -->

[^N.D.E-VIII-8] In this paragraph we "recall" some descent results that will be used frequently in what follows.

**Scholium 1.7.1.** *Let `S` be a prescheme and `X`, `Y`, `T` `S`-preschemes. If `(T_i)` is an open covering of `T`, and
if we set `T_{ij} = T_i ∩ T_j = T_i ×_T T_j`, then, since giving a morphism of `T`-preschemes `X_T → Y_T` is local on
`T`, one has an exact sequence of sets:*

<!-- label: III.VIII.1.7.1 -->

```text
(1)    Hom_T(X_T, Y_T) → ∏_i Hom_{T_i}(X_{T_i}, Y_{T_i}) ⇒ ∏_{i,j} Hom_{T_{ij}}(X_{T_{ij}}, Y_{T_{ij}})
```

<!-- label: eq:III.VIII.1.7.1 -->

*i.e. `Hom_S(X, Y)` is a local `S`-functor, that is, a sheaf on `(Sch)/S` endowed with the Zariski topology.*

*More generally, by IV 4.5.13, `Hom_S(X, Y)` is a sheaf on `(Sch)/S` for every topology coarser than the canonical
topology — for example, for the (fpqc) topology.*

*If `G`, `H` are `S`-preschemes in groups, one deduces that the subfunctor `Hom_{S-gr.}(X, Y)` is a sheaf for the (fpqc)
topology (hence a fortiori a local functor).*

**Lemma 1.7.2.**[^N.D.E-VIII-9] *Let `F` be a local `S`-functor.*

<!-- label: III.VIII.1.7.2 -->

*(i) Suppose there exists an open covering `(S_i)` of `S` such that the restriction `F_i = F ×_S S_i` of `F` to each
`S_i` is representable by an `S_i`-prescheme `X_i`. Then `F` is representable by an `S`-prescheme `X`.*

*(ii) Suppose `F` is an (fpqc) sheaf and that there exists a faithfully flat quasi-compact morphism `S′ → S` such that
the restriction `F′ = F ×_S S′` of `F` is representable by an `S′`-prescheme `X′`. Then `X′` is endowed with a descent
datum (cf. IV 2.1) relative to `S′ → S`.*

*If moreover this descent datum is effective (which is the case if `X′` is affine over `S′`), then `F` is representable
by an `S`-prescheme `X`.*

<!-- original page 7 -->

*Proof.* (i) It follows from the hypothesis that `X_i ×_S S_j` and `X_j ×_S S_i` both represent the restriction of `F`
to `S_{ij} = S_i ×_S S_j`, hence, by the Yoneda lemma, there is a unique isomorphism of `S_{ij}`-preschemes

```text
c_{ji} : X_i ×_S S_j ⥲ X_j ×_S S_i;
```

one then has isomorphisms of preschemes over `S_{ijk} = S_i ×_S S_j ×_S S_k`:

```text
       c_{ji} × id_{S_k}                       c_{kj} × id_{S_i}
X_i ×_S S_j ×_S S_k ─────→ X_j ×_S S_i ×_S S_k ≅ X_j ×_S S_k ×_S S_i ─────→ X_k ×_S S_j ×_S S_i

       c_{ki} × id_{S_j}
X_i ×_S S_k ×_S S_j ─────→ X_k ×_S S_i ×_S S_j
```

and since all these objects represent the restriction of `F` to `S_{ijk}`, this diagram is commutative, i.e. the
`c_{ji}` satisfy the usual cocycle relation `c_{kj} ∘ c_{ji} = c_{ki}`.

It follows that the `X_i` glue together into an `S`-prescheme `X` such that `X ×_S S_i = X_i` for every `i`. For every
`Y` over `S_i`, one therefore has

```text
(*)    F(Y) = F_i(Y) = Hom_{S_i}(Y, X ×_S S_i) = Hom_S(Y, X) = h_X(Y).
```

Then, for `Y → S` arbitrary, the `Y_i = Y ×_S S_i` form an open covering of `Y`; set
`Y_{ij} = Y_i ×_Y Y_j = Y ×_S S_{ij}`. Since `F` (resp. `h_X`) is a local functor by hypothesis (resp. because the
Zariski topology is coarser than the canonical topology), `F(Y)` and `h_X(Y)` both identify, in view of `(*)`, with the
kernel of the double arrow:

```text
∏_i F(Y_i)  ⇒  ∏_{i,j} F(Y_{ij})

∏_i h_X(Y_i)  ⇒  ∏_{i,j} h_X(Y_{ij}).
```

This proves (i).

(ii) It follows from the hypothesis that `F″₁ = F′ ×_{S′} S″₁` (where `S″₁ = S″ = S′ ×_S S′` is considered as
`S′`-prescheme via the first projection) is represented by `X″₁ = X′ ×_{S′} S″₁`; similarly, `F″₂ = F′ ×_{S′} S″₂` is
represented by `X″₂ = X′ ×_{S′} S″₂`. Now `F″₁ = F ×_S S″ = F″₂`, hence there exists a (unique) `S″`-isomorphism
`c : X″₁ ⥲ X″₂`. Then, denoting by `q_i` (resp. `p_{ji}`) the projection of `S‴ = S′ ×_S S′ ×_S S′` onto the `i`-th
factor (resp. onto the factors `i` and `j`), `X‴_i = X′ ×_{S′} S‴_i` (where `S‴_i = S‴` considered as `S′`-prescheme via
`q_i`), and `p_{ji}^*(c) : X‴_i ⥲ X‴_j` the isomorphism of `S‴`-preschemes deduced from `c` by base change, one obtains
a diagram of isomorphisms of `S‴`-preschemes:

```text
              p_{21}^*(c)
        X‴_1 ─────────→ X‴_2
            ╲              │
  p_{31}^*(c) ╲             │ p_{32}^*(c)
              ╲             ↓
                X‴_3
```

<!-- original page 8 -->

and since all these objects represent the restriction of `F` to `S‴`, this diagram is commutative, i.e. the usual
cocycle relation `p_{32}^*(c) ∘ p_{21}^*(c) = p_{31}^*(c)` holds, i.e. `c` is a descent datum on `X′` relative to
`S′ → S` (cf. IV 2.1).

Suppose moreover that this descent datum is effective, i.e. that there exists an `S`-prescheme `X` such that
`X′ ≃ X ×_S S′` (by SGA 1, VIII 2.1, this is the case if `X′` is affine over `S′`[^N.D.E-VIII-10]). Then, for every
`Y → S′`, one has

```text
(**)    F(Y) = F′(Y) = Hom_{S′}(Y, X ×_S S′) = Hom_S(Y, X) = h_X(Y).
```

Then, for `Y → S` arbitrary, set `Y′ = Y ×_S S′` and `Y″ = Y′ ×_Y Y′ ≃ Y ×_S S″`. Then `Y′ → Y`, like `S′ → S`, is
faithfully flat and quasi-compact, hence an `M`-effective epimorphism (where `M` = family of faithfully flat
quasi-compact morphisms), i.e. the equivalence relation

```text
Y′ ×_Y Y′ ⇒ Y′
```

is `M`-effective and has quotient `Y`. Since `F` (resp. `h_X`) is an (fpqc) sheaf by hypothesis (resp. because the
(fpqc) topology is coarser than the canonical topology), `F(Y)` and `h_X(Y)` both identify, in view of `(**)`, with the
kernel of the double arrow

```text
F(Y′) ⇒ F(Y′ ×_Y Y′)

h_X(Y′) ⇒ h_X(Y′ ×_Y Y′).
```

This proves (ii).

**Corollary 1.7.3.** *Let `F` be an (fpqc) sheaf on `(Sch)/S`. Suppose there exists an open covering `(S_i)` of `S` and,
for each `i`, a faithfully flat quasi-compact morphism `S′_i → S_i` such that the restriction `F′_i = F ×_S S′_i` is
representable by an `S′_i`-prescheme `X′_i` affine over `S′_i`. Then `F` is representable by an `S`-prescheme `X` affine
over `S` (such that `X ×_S S′_i = X′_i` for every `i`).*

<!-- label: III.VIII.1.7.3 -->

*If moreover each `X′_i → S′_i` is a closed immersion (resp. a finite étale morphism), the same holds for `X → S`.*

The first assertion follows from 1.7.2. For the second, it suffices to verify that each morphism `X ×_S S_i → S_i` is a
closed immersion (resp. finite and étale), which follows from EGA IV₂, 2.7.1 (resp. and IV₄, 17.7.3).

**Remark 1.7.4.** *Assertion 1.5 (b) follows, as announced, from 1.7.1 and 1.7.2 (i).*

<!-- label: III.VIII.1.7.4 -->

## 2. Schematic properties of diagonalizable groups

They are summarized in the following.

<!-- original page 8 -->

**Proposition 2.1.** *Let `S` be a non-empty prescheme, `M` an ordinary commutative group, `G = D(M_S)` the
diagonalizable `S`-group defined by `M`. Then:*

<!-- label: III.VIII.2.1 -->

*a) `G` is faithfully flat over `S`, and affine over `S` (a fortiori quasi-compact over `S`).*

*b) `M` of finite type ⇔ `G` of finite type over `S` ⇔ `G` of finite presentation over `S`.*

*c) `M` finite ⇔ `G` finite over `S` ⇔ `G` of finite type over `S` and annihilated by an integer `n > 0`. Then
`deg(G/S) = Card(M)`.*

*c′) `M` a torsion group ⇔ `G` integral over `S`.*

*d) `M = 0` ⇔ `G` = unit `S`-group.*

*e) `M` of finite type, and the order of its torsion subgroup is prime to the residue characteristics of `S` ⇔ `G` is
smooth over `S`.*

The verification of (a) to (d) is trivial, and is left to the reader. Let us prove (e). If `G` is smooth over `S`, it is
locally of finite presentation over `S`, hence of finite presentation over `S` since it is affine over `S`, hence `M` is
of finite type. So we may already assume `M` of finite type, hence `G` of finite presentation over `S`.
Then[^N.D.E-VIII-11] `G` is smooth over `S` if and only if its geometric fibers are, which reduces us to the case where
`S` is the spectrum of an algebraically closed field `k`. Writing `M = T × L`, with `T` the torsion subgroup and `L`
free, `L ≃ ℤ^r`, one has `D(M) = D(T) × D(L)`, where `D(L) ≃ G_m^r` is smooth over `k`. So `G = D(M)` is smooth over `k`
if and only if `D(T)` is, which means, since `D(T)` is finite over `k` of degree equal to the order `n` of `T`, that
`D(T)(k)` has `n` elements. Now `T` is isomorphic to a sum of groups `ℤ/n_iℤ`, `n` being the product of the `n_i`, so
`D(T)` is the product of the `D(ℤ/n_iℤ) = μ_{n_i}` (group scheme of `n_i`-th roots of unity), hence

```text
card(D(T)(k)) = ∏_i card μ_{n_i}(k),
```

where `card μ_{n_i}(k)` = (number of `n_i`-th roots of unity in `k`) `⩽ n_i`, equality being attained if and only if
`n_i` is prime to the characteristic `p` of `k`. Hence one has `card(D(T)(k)) = n` (where `n = ∏_i n_i`) if and only if
all the `n_i` are prime to `p`, i.e. if and only if `n` is prime to `p`. QED.

## 3. Exactness properties of the functor `D_S`

**Theorem 3.1.** *Let `S` be a prescheme, and*

<!-- label: III.VIII.3.1 -->

```text
0 → M′ -u→ M -v→ M″ → 0
```

<!-- original page 8 -->

*an exact sequence of ordinary commutative groups. Consider the sequence of transposed homomorphisms:*

```text
0 → D_S(M″) -v^t→ D_S(M) -u^t→ D_S(M′) → 0.
```

*(i) `v^t` induces an isomorphism of `D_S(M″)` with the kernel of `u^t`, and `u^t` is faithfully flat and
quasi-compact.*

*(ii)*[^N.D.E-VIII-12] *`D_S(M′)` represents the (fpqc) quotient sheaf `D_S(M)/D_S(M″)`.*

<!-- original page 9 -->

Let `M` denote the family of faithfully flat quasi-compact morphisms. First, (ii) follows from (i) (cf. IV, 4.6.5.1).
Indeed, the equivalence relation in `D_S(M)` defined by `u^t` is the same as that defined by the subgroup
`Ker(u^t) = D_S(M″)`; since `u^t ∈ M`, this equivalence relation is `M`-effective (cf. IV, 3.3.2.1), and therefore
`D_S(M′)` represents the quotient sheaf for the (fpqc) topology (cf. IV, 4.6.5).

The first assertion of (i) is a trivial consequence of the definition of the functors `D_S(−)`; more generally, for any
exact sequence

```text
M′ → M → M″ → 0
```

(without zero on the left), one will have a transposed exact sequence:

```text
0 → D_S(M″) → D_S(M) → D_S(M′).
```

(This is valid more generally in the context of the beginning of §1.) On the other hand, since `D_S(M)` and `D_S(M′)`
are affine over `S`, `u^t` is necessarily an affine morphism, a fortiori quasi-compact (whatever the homomorphism
`u : M′ → M`). The second assertion of (i) will therefore follow from point (a) of the following:

**Corollary 3.2.** *Let `S` be a non-empty prescheme, `u : M′ → M` a homomorphism of ordinary commutative groups,
`u^t : G → G′` the transposed homomorphism. Then:*

<!-- label: III.VIII.3.2 -->

*a) For `u` to be a monomorphism, it is necessary and sufficient that `u^t` be faithfully flat.*

*b) For `u` to be an epimorphism, it is necessary and sufficient that `u^t` be a monomorphism (and then `u^t` is even a
closed immersion).*

To prove (a), one notes that if `u` is a monomorphism, then `O_S(M)` is a module over `O_S(M′)` admitting a non-empty
basis (namely, the system of sections defined by any system of representatives of `M` modulo `M′`), a fortiori it is
faithfully flat. Conversely, if this is the case, then `u^t : O_S(M′) → O_S(M)` is injective, which (for `S ≠ ∅`)
implies that `u : M′ → M` is injective.

To prove (b), one notes that if `u` is an epimorphism, then `O_S(M′) → O_S(M)` is surjective, hence `u^t` is a closed
immersion and a fortiori a monomorphism. Conversely, if this is the case, then `Ker u^t` = unit group; now setting
`M″ = Coker u`, we have seen that `Ker u^t ≃ D_S(M″)`, hence by 2.1 (d) one has `M″ = 0`, hence `u` is an epimorphism.

One concludes from 3.1 in the usual way:

**Corollary 3.3.** *Let `M′ -u→ M -v→ M″` be an exact sequence of ordinary commutative groups; consider the transposed
sequence*

<!-- label: III.VIII.3.3 -->

```text
G″ -v^t→ G -u^t→ G′.
```

*Then `v^t` induces a faithfully flat quasi-compact morphism from `G″` to `Ker u^t`, and the latter is a diagonalizable
group isomorphic to `D_S(v(M)) = D_S(Coker u)`.*

<!-- original page 10 -->

**Corollary 3.4.** *Let `S` be a prescheme, `u : G → H` a homomorphism of `S`-preschemes in locally diagonalizable
groups, with `H` of finite type over `S`. Set `G′ = Ker u`. Then:*

<!-- label: III.VIII.3.4 -->

*a) `G′` is locally diagonalizable; it is of finite type over `S` if `G` is.*

*b) The quotient `G/G′` "exists"; more precisely, the equivalence relation defined by `G′` in `G` is `M`-effective
(where `M` = set of faithfully flat quasi-compact morphisms, cf. IV, 3.4). Moreover, `G/G′` is locally diagonalizable,
of finite type over `S`.*

*c) The homomorphism `u : G → H` factors uniquely as*

```text
G -v→ G/G′ -w→ H,
```

*where `v` is the canonical homomorphism (so `v` is faithfully flat and quasi-compact). Moreover `w` is a closed
immersion, and a fortiori a monomorphism.*

*Finally, the quotient `H′ = H/Im w = Coker w = Coker u` exists; more precisely, the equivalence relation defined by
`G/G′` in `H` is `M`-effective, and `H′` is of finite type over `S`.*

The first assertion of (c) is a consequence of (b), by definition of the quotient `G/G′` (cf. IV,
3.2.3).[^N.D.E-VIII-13] Let us show that the (fpqc) quotient sheaf `G̃/G̃′` is representable. This may be verified
locally on `S`, as may all the other assertions; we may therefore suppose `G` and `H` diagonalizable, of the form
`D_S(M)` and `D_S(N)`.

Since `H` is of finite type over `S`, `N` is of finite type by 2.1 (b), hence by 1.5 `u` is defined by a homomorphism
`u_0 : N → M`. Then, in virtue of 3.1 and 3.2, `G′` is isomorphic to `D_S(Coker u_0)` and `G̃/G̃′` is representable by
`D_S(Im u_0)`; moreover, considering the exact sequence

```text
0 → Ker u_0 → N -w_0→ Im u_0 → 0,
```

one obtains that `w` is a closed immersion, and that the quotient `H′ = H/Im w` is `D_S(Ker u_0)`; the latter is of
finite type over `S` since `N`, and hence `Ker u_0`, is of finite type.

**Remarks.** The existence-of-quotients result 3.4 will be substantially generalized in §5.

On the other hand, one will note that in the present § and the preceding one, the hypothesis `S ≠ ∅` was used only to
ensure the validity of certain converses, enabling one to deduce from certain hypotheses on diagonalizable `S`-groups
properties of the corresponding ordinary groups. The "direct"-sense results are valid without restriction on `S`, and
the proofs given here apply in the general case.

**Corollary 3.5.** *Let `G` be a diagonalizable group prescheme over `S`, and let `n` be an integer `≠ 0`. Then the
subgroup `_nG` of `G`, kernel of the homomorphism `n · id_G : G → G`, is integral over `S`, and finite over `S` if `G`
is of finite type over `S`.*

<!-- label: III.VIII.3.5 -->

<!-- original page 11 -->

Indeed, if `G = D_S(M)`, then `_nG = D_S(M/nM)` by 3.1, and one concludes by 2.1 (b), (c), (c′).

## 4. Torsors under a diagonalizable group

Let `S` be a prescheme, and `G = D_S(M)` a diagonalizable group over `S`. We propose to determine the `G`-torsors (or
principal homogeneous `G`-bundles) on `S`, in the sense of the "faithfully flat quasi-compact topology" (cf. Exp. IV,
5.1). Recall that a prescheme `P` over `S` with operator group `G` is called a *torsor* or *principal homogeneous* if
every point of `S` admits an open neighborhood `U` and a faithfully flat quasi-compact morphism `S′ → U` such that
`P′ = P ×_S S′` is, as a bundle with operators, isomorphic to `G′ = G ×_S S′` (acting on itself by right translations).
Since `G` is affine over `S`, it follows from SGA 1, VIII 5.6 that `P` is necessarily affine over `S`. Note also that
since `G` is itself faithfully flat and quasi-compact over `S`, `P` is principal homogeneous under `G` if and only if it
is "formally principal homogeneous", and if moreover it is faithfully flat and quasi-compact over `S` (cf. IV, 5.1.6).

Recall on the other hand (Exp. I, 4.7.3) that giving an `S`-prescheme `P` affine over `S` with operator group
`G = D_S(M)` amounts to giving a quasi-coherent commutative `M`-graded algebra on `S`, i.e. a quasi-coherent algebra `𝓐`
on `S` endowed with a direct sum decomposition (as a module):

```text
𝓐 = ⨁_{m ∈ M} 𝓐_m,
```

with

```text
𝓐_m · 𝓐_{m′} ⊆ 𝓐_{m+m′}    for m, m′ ∈ M.
```

This said, the answer to the problem posed above is given by:

**Proposition 4.1.** *For the prescheme `P` with operator group `G = D_S(M)`, defined by the `M`-graded algebra `𝓐`, to
be a principal homogeneous bundle under `G`, it is necessary and sufficient that `𝓐` satisfy the following conditions:*

<!-- label: III.VIII.4.1 -->

*a) For every `m ∈ M`, `𝓐_m` is an invertible module on `S`.*

*b) For `m, m′ ∈ M`, the homomorphism*

```text
𝓐_m ⊗_{O_S} 𝓐_{m′} → 𝓐_{m+m′}
```

*induced by the multiplication in `𝓐`, is an isomorphism.*

<!-- original page 12 -->

The necessity of the conditions is immediate by descent, since they are satisfied in the case where `P` is the trivial
principal homogeneous bundle, i.e. `𝓐 = O_S(M)`. For the sufficiency, one notes that (a) already implies that `P` is
faithfully flat over `S`, it is in any case quasi-compact over `S` (being affine over `S`), so it remains to verify that
it is formally principal homogeneous under `G`, i.e. that the well-known homomorphism

```text
P ×_S G → P ×_S P
```

is an isomorphism. Now on affine algebras, this homomorphism is given explicitly as the homomorphism

```text
𝓐 ⊗ 𝓐 → 𝓐(M) = 𝓐 ⊗ O_S(M)
```

which in bidegree `(m, n)` (where `m, n ∈ M`) is given by

```text
x_m ⊗ y_n ↦ x_m y_n ⊗ e_n.
```

From the standpoint of degrees, this homomorphism is compatible with the homomorphism `M × M → M × M` given by

```text
(m, n) ↦ (m + n, n),
```

which is an isomorphism. This shows that (b) expresses precisely (independently of (a)) that `P` is formally principal
homogeneous, and establishes 4.1.

Note also that one obtains, by faithfully flat descent:

**Corollary 4.2.** *The conditions of 4.1 imply that the homomorphism*

<!-- label: III.VIII.4.2 -->

```text
O_S → 𝓐_0
```

*is an isomorphism.*

If for example `M = ℤ`, then under the conditions of 4.1 one sees that `𝓐` is essentially known when one knows
`𝓐_1 = 𝓛`, namely

```text
𝓐 ≃ ⨁_{n ∈ ℤ} 𝓛^{⊗n}
```

(isomorphism of graded algebras). One thereby recovers the well-known result:

**Corollary 4.3.** *There is an equivalence between the category of principal homogeneous bundles `P` on `S` with group
`G_{m,S}`, and the category of invertible modules `𝓛` on `S` (taking as morphisms, for the definition of each category,
the isomorphisms of the structures in play). One obtains two quasi-inverse functors by associating with each `P` the
degree-`1` component of its `ℤ`-graded affine algebra, and with each `𝓛` the spectrum of the `ℤ`-graded algebra
`⨁_{n ∈ ℤ} 𝓛^{⊗n}`.*

<!-- label: III.VIII.4.3 -->

In particular:

**Corollary 4.4.** *The group of classes of principal homogeneous bundles on `S` with group `G_{m,S}` is isomorphic to
the group `Pic(S)` of classes of invertible modules on `S`, i.e. to `H¹(S, O_S^×)`.*

<!-- label: III.VIII.4.4 -->

Taking into account that `G_{m,S}` is the scheme of automorphisms of the module `O_S`, one sees that 4.4 is equivalent
to the following statement, which is one of the variants of Hilbert's "Theorem 90":

**Corollary 4.5.** *Every principal homogeneous bundle on `S` with group `G_m` is locally trivial (in the sense of the
Zariski topology).*

<!-- label: III.VIII.4.5 -->

**Remark 4.5.1.** *One will note that the preceding statement is no longer true in general for a group such as `μ_n`, or
for a "twisted form" of `G_m`; for example, the unique twisted form of `G_m` over the field `ℝ` of reals gives a group
of `1`-cohomology equal to `ℤ/2ℤ`.*

<!-- label: III.VIII.4.5.1 -->

<!-- original page 13 -->

[^N.D.E-VIII-14] Indeed, let `S¹` be the kernel of the norm morphism `N : ∏_{ℂ/ℝ} G_{m,ℂ} → G_{m,ℝ}`; this is a
`ℂ/ℝ`-twisted form of `G_{m,ℝ}`. The equation `N(z) = −1` in `∏_{ℂ/ℝ}(G_{m,ℂ})` defines an `S¹`-torsor `X` over
`Spec(ℝ)`, locally trivial for the étale topology, but not trivial since `X(ℝ) = ∅`. Let us show that
`H¹_ét(ℝ, S¹) ≅ ℤ/2ℤ`. One has an exact sequence of smooth commutative `ℝ`-group schemes:

```text
1 → S¹ → ∏_{ℂ/ℝ} G_{m,ℂ} → G_{m,ℝ} → 1
```

which gives rise to a long exact sequence of étale cohomology (or of Galois cohomology):

```text
0 → S¹(ℝ) → ℂ^× -N→ ℝ^× → H¹_ét(ℝ, S¹) → H¹_ét(ℝ, ∏_{ℂ/ℝ} G_{m,ℂ}) → ⋯
```

Now (see for example XXIV, 8.4), `H¹_ét(ℝ, ∏_{ℂ/ℝ} G_{m,ℂ}) ≃ H¹_ét(ℂ, G_{m,ℂ})`, and the latter is zero by 4.5 (or,
here, because `ℂ` is algebraically closed). One thus obtains an isomorphism `H¹_ét(ℝ, S¹) ≃ ℝ^×/N(ℂ^×) ≃ {±1}`.

We shall need in the following § the following result:

**Proposition 4.6.** *Under the conditions of 4.1, conditions (a) and (b) are equivalent to the following conditions:*

<!-- label: III.VIII.4.6 -->

*a′) `O_S → 𝓐_0` is an isomorphism.*

*b′) For every `m` in `M` (it suffices: in a system of generators of `M`), one has*

```text
𝓐_m · 𝓐_{−m} = 𝓐_0.
```

The necessity being evident, taking 4.2 into account,[^N.D.E-VIII-15] we shall reduce to proving:

**Corollary 4.7.** *Let `A = ⨁_{n ∈ ℤ} A_n` be a `ℤ`-graded ring such that*

<!-- label: III.VIII.4.7 -->

```text
A_1 · A_{−1} = A_0.
```

*Then the `A_n` are invertible `A_0`-modules, and for `n, n′ ∈ ℤ`, the homomorphism*

```text
A_n ⊗_{A_0} A_{n′} → A_{n+n′}
```

*induced by the multiplication in `A`, is an isomorphism.*

By hypothesis, there exist `f_i ∈ A_1`, `g_i ∈ A_{−1}`, such that

```text
(*)    ∑_i f_i g_i = 1.
```

As the conclusion to be established is local on `Spec(A_0)`,[^N.D.E-VIII-16] and as, by `(*)`, `Spec(A_0)` is covered by
the affine opens `D(f_i g_i)`, one is reduced to the case where there exists an element `f ∈ A_1` invertible in `A`.
Then for every `n ∈ ℤ`, `f^n` is an element of `A_n` invertible in `A`, hence defines an isomorphism `h ↦ f^n h` from
`A_0` onto `A_n`. Moreover,

<!-- original page 14 -->

this shows that one obtains an isomorphism `A_0[t, t^{−1}] → A` of graded `A_0`-algebras by sending `t` to `f`, which
completes the proof of 4.7.

Then, under the conditions of 4.6, 4.7 already implies that the `𝓐_m` (`m ∈ M`) are invertible. To prove condition 4.1
(b), one may therefore suppose that `𝓐_m` and `𝓐_{m′}` admit bases `f_m` and `f_{m′}`, having inverses
`f_m^{−1} ∈ Γ(𝓐_{−m})` and `f_{m′}^{−1} ∈ Γ(𝓐_{−m′})`. Then the product by `f_m^{−1} f_{m′}^{−1} ∈ Γ(𝓐_{−m−m′})` defines
a homomorphism `𝓐_{m+m′} → 𝓐_0 ≃ O_S`, sending the image of `f_m ⊗ f_{m′}` to the section `1` of `O_S`. In the diagram

```text
                     w
                   ──────────────────────
                 ↗                       ↘
𝓐_m ⊗ 𝓐_{m′}  ─u→  𝓐_{m+m′}  ─v→  𝓐_0 ≃ O_S
```

`w` and `v` are therefore epimorphisms of invertible sheaves, hence isomorphisms, hence `u` is an isomorphism. QED.

## 5. Quotient of an affine scheme by a diagonalizable group acting freely

<!-- original page 15 -->

[^N.D.E-VIII-17] We denote by `M` the set of faithfully flat quasi-compact morphisms, and we recall that torsors are
considered in the sense of the (fpqc) topology.

**Theorem 5.1.** *Let `S` be a prescheme, `M` an ordinary commutative group, `G = D_S(M)` the diagonalizable group over
`S` defined by it, `P` an `S`-prescheme affine over `S` on which `G` acts freely on the right.*

<!-- label: III.VIII.5.1 -->

*Then the equivalence relation defined by `G` in `P` is `M`-effective (cf. IV, 3.4), i.e. the quotient `X = P/G` exists
and `P` is a torsor over `X` with group `G_X = D_X(M)`. Moreover, `P/G` is affine over `S`; more precisely, if `P` is
defined by the `M`-graded algebra `𝓐`, then `P/G` is isomorphic to `Spec(𝓐_0)`, where `𝓐_0 = 𝓐^G` is the degree-`0`
component of `𝓐`.*

*Proof.* Set `X = Spec(𝓐_0)`. Then one has a natural morphism `P → X`, deduced from `𝓐_0 → 𝓐`, which is invariant under
the action of `G`. In this way, `P` becomes an `X`-prescheme, affine over `X`, with operator group `G_X = D_X(M)`, and
the hypothesis that `G` acts freely on `P/S` implies that `G_X` acts freely on `P/X`. Everything reduces to showing that
`P` is a principal homogeneous bundle under `G_X`, using the fact that `𝓑_0 = O_X`, where `𝓑` is the `M`-graded algebra
on `X` defining `P/X`. We may then suppose `X = S` and `S` affine, so `P` is affine, given by an `M`-graded ring `A`
whose homogeneous part of degree `m` will be denoted `A_m`, so that `S = Spec(A_0)`. Taking 4.6 into account, it remains
to verify that one has:

```text
(*)    A_m · A_{−m} = A_0    for every m ∈ M.
```

One observes moreover by a direct computation that `(*)` is equivalent to saying that `P ×_S G → P ×_S P` is a closed
immersion, and not only a monomorphism (under the hypothesis that `G` acts freely), i.e. that the homomorphism on affine
rings

<!-- original page 16 -->

```text
θ : A ⊗_{A_0} A → A(M)
```

is surjective[^N.D.E-VIII-18]. This gives 5.1 when one supposes that the equivalence relation defined by `G` in `P` is
closed. We shall, however, show that this hypothesis is already a consequence of the fact that `G` acts freely (which is
moreover implicitly contained in Theorem 5.1, since `G ×_S P` must be isomorphic to `P ×_X P`, which is closed in
`P ×_S P` since `X` is affine over `S` hence separated over `S`).

Let `R = P ×_S G`. The hypothesis that `G` acts freely, i.e. that `R → P ×_S P` is a monomorphism, can be written as
saying that the diagonal morphism

```text
R → R ×_{(P ×_S P)} R = R₀
```

is an isomorphism. One has `R = Spec(A(M))` and

```text
R₀ = Spec(A(M × M)/K)
```

[^N.D.E-VIII-19] where `K` is the ideal generated by the elements of the form

```text
x_m(e_{m,0} − e_{0,m}),    with m ∈ M, x_m ∈ A_m;
```

let `φ : A(M × M) → A(M)` be the surjective ring homomorphism defined by

```text
x e_{m,n} ↦ x e_{m+n}    (m, n ∈ M, x ∈ A)
```

(where the `e_m`, resp. `e_{m,n} = e_m ⊗ e_n`, are the elements of the canonical basis of `A(M)`, resp. `A(M × M)`).
Then the diagonal morphism `R → R₀` corresponds to the homomorphism

```text
φ̄ : A(M × M)/K → A(M)
```

obtained by passing to the quotient by `K`. Now the kernel of `φ` is the ideal `K′` generated by the

```text
d_m = e_{m,0} − e_{0,m}.
```

One has `K ⊆ K′`, and the hypothesis that `G` acts freely on `P`, i.e. that `φ̄` is an isomorphism, is equivalent to the
equality `K′ = K`, which is expressed by the relations

```text
(**)   d_m ∈ K = ∑_p A(M × M) A_p d_p,    for every m ∈ M.
```

Using the natural tri-grading of `A(M × M)`, and the fact that the first degree of `d_m` is zero, this means that one
can write `d_m` as a sum of elements of the form

```text
f e_{r,s} (e_{p,0} − e_{0,p})    with f ∈ A_{−p} · A_p,
```

and using the fact that the total degree of `d_m` is `m`, one can restrict to terms such that

```text
r + s + p = m.
```

<!-- original page 16 -->

Hence one must have, for every `m ∈ M`, an expression:

```text
(***)   { d_m = e_{m,0} − e_{0,m} = ∑_{r,s} λ_{r,s}(e_{m−s,s} − e_{r,m−r})
         with λ_{r,s} ∈ J_p = A_p · A_{−p} ⊆ A_0, p = m − (r + s).
```

One must conclude the relation `(*)`, i.e. the relations

```text
(****)   J_n = A_0    for every n ∈ M.
```

Now for this, it suffices to establish the same relation modulo every maximal ideal of `A_0`. As the hypotheses made are
invariant under such a reduction, one may already suppose that `A_0` is a field.

**Lemma 5.2.** *Under the preceding conditions (with `A_0` a field), if `M ≠ 0`, there exists a `p ∈ M − {0}` such that
`J_p = A_0`.*

<!-- label: III.VIII.5.2 -->

Indeed, if this were not so, the sum in the right-hand side of `(***)` would be zero for every `m ∈ M`, which is absurd.

<!-- original page 18 -->

**Corollary 5.3.** *Under the preceding conditions, but without supposing any longer that `A_0` is a field, there exist
finitely many elements `p_i ∈ M − {0}` such that `∑_i J_{p_i} = A_0`.*

<!-- label: III.VIII.5.3 -->

Indeed, one applies the result 5.2 to the situations deduced from `A/A_0` by reduction modulo the maximal ideals of
`A_0`.[^N.D.E-VIII-20]

**Corollary 5.4.** *Suppose again that `A_0` is a field. Then for every subgroup `N` of `M` such that `N ≠ M`, there
exists a `p ∈ M − N` such that `J_p = A_0`.*

<!-- label: III.VIII.5.4 -->

Indeed, let `M′ = M/N`, and consider the `M′`-graded ring `A′`, whose underlying ring is `A`, and whose grading is given
by

```text
A′_{m′} = ⨁_{m ∈ h^{−1}(m′)} A_m,
```

where `h : M → M′ = M/N` is the canonical homomorphism. Geometrically, this construction amounts to considering the
subgroup `G′ = D_S(M′)` of `G`, and the structure on `P` of scheme with operator group `G′` induced by the action of
`G`. It is then evident that `G′` acts freely on `P′`, i.e. the pair `(M′, A′)` satisfies the hypotheses of 5.3. One
thus obtains

```text
1 = ∑_i f_i g_i    with f_i ∈ A′_{m′_i}, g_i ∈ A′_{−m′_i} and m′_i ∈ M′ − {0},
```

whence at once the conclusion 5.4 by taking the components of the right-hand side along `A_0`, and using that `A_0` is a
field.

Let us now note that

```text
J_p · J_q ⊆ J_{p+q}    and J_p = J_{−p},
```

<!-- original page 17 -->

so if `N` denotes the set of `m ∈ M` such that `J_p = A_0`, one sees that `N` is a subgroup of `M`. Using 5.4 one sees
that it is equal to `M`. This completes the proof of Theorem 5.1.

As we have pointed out in the course of the proof, Theorem 5.1 implies:

**Corollary 5.5.** *Under the conditions of 5.1, the graph morphism*

<!-- label: III.VIII.5.5 -->

```text
P ×_S G → P ×_S P
```

*is a closed immersion.*

One concludes at once:

**Corollary 5.6.** *Let `σ` be a section of `P` over `S`. Then the morphism `g ↦ σ · g` from `G` to `P` defined by `σ`
is a closed immersion.*

<!-- label: III.VIII.5.6 -->

**Corollary 5.7.** *Let `G`, `H` be two `S`-groups, with `G` diagonalizable, `H` affine over `S`, and let `u : G → H` be
a homomorphism of `S`-groups that is a monomorphism. Then `u` is a closed immersion, `H/G = X` exists and `H` is a
principal homogeneous bundle over `X` with group `G_X`; finally, `X` is affine over `S`.*

<!-- label: III.VIII.5.7 -->

**Corollary 5.8.** *Under the conditions of 5.1, if `P` is of finite type (resp. of finite presentation) over `S`, the
same holds for `X = P/G`.*

<!-- label: III.VIII.5.8 -->

Indeed, it follows from the hypothesis that the fibers of `G_X` are of finite type, hence `G_X` is of finite
presentation over `X` by 2.1 (b), hence `P` being a torsor under `G_X` is of finite presentation over
`X`[^N.D.E-VIII-21]. Since it is also faithfully flat over `X`, our conclusion then follows from Exp. V, Prop. 9.1.

## 6. Essentially free morphisms, and representability of certain functors of the form `∏_{Y/S} Z/Y`[^VIII-6-star]

<!-- original page 20 -->

**Definition 6.1.** *Let `f : X → S` be a morphism of preschemes. We say that `f` is* essentially free\*, or also that
`X` is\* essentially free over `S`*, if one can find a covering of `S` by affine opens `S_i`, for each `i` an
`S_i`-prescheme `S′_i` affine and faithfully flat over `S_i`, and a covering `(X′_{ij})_j` of `X′_i = X ×_S S′_i` by
affine opens `X′_{ij}`, such that for every `(i, j)`, the ring of `X′_{ij}` is a free module over the ring of
`S′_i`.*[^N.D.E-VIII-22]

<!-- label: III.VIII.6.1 -->

**Proposition 6.2.** *a) If `X` is essentially free over `S`, it is flat over `S`, the converse being true if `S` is
Artinian.*

<!-- label: III.VIII.6.2 -->

*b) If `S` is the spectrum of a field, every `S`-prescheme is essentially free over `S`.*

*c) If `X` is essentially free over `S`, and if `S′ → S` is a base change morphism, then `X′ = X ×_S S′` is essentially
free over `S′`. The converse is true if `S′ → S` is faithfully flat and quasi-compact.*

The proof is immediate, using for the converse in (a) the fact that a flat module over an Artinian local ring is
free.[^N.D.E-VIII-23]

**Proposition 6.3.** *Let `H` be an `S`-prescheme in groups that is diagonalizable (more generally, that becomes
diagonalizable by suitable faithfully flat quasi-compact extension of every affine open of `S`, i.e. `H` is "of
multiplicative type", cf. IX 1.1). Then `H` is essentially free over `S`.*

<!-- label: III.VIII.6.3 -->

Indeed, if `H` is diagonalizable, it is affine over `S` and defined by an algebra which is a free `O_S`-module.

<!-- original page 21 -->

The introduction of Definition 6.1 is justified by the following:

**Theorem 6.4.** *Let `S` be a prescheme, `Z` an essentially free `S`-prescheme, `Y` a closed subprescheme of `Z`.
Consider the following functor*[^N.D.E-VIII-24]

<!-- label: III.VIII.6.4 -->

```text
F = ∏_{Z/S} Y/Z : (Sch)°/S → (Ens),
F(S′) = Γ(Y_{S′}/Z_{S′}) = { ∅           if Z_{S′} ≠ Y_{S′};
                             {id_{Z_{S′}}}  if Z_{S′} = Y_{S′}.
```

*This functor is representable by a closed subprescheme of `S`.*[^N.D.E-VIII-25]

[^N.D.E-VIII-26] Let us first note that `F` is a sheaf for the (fpqc) topology: since `F(S′) = ∅` or `{pt}` for every
`S′`, this reduces to verifying that if `(S_i)` is an open covering of `S` (resp. `S′ → S` a faithfully flat
quasi-compact morphism), and if each `Y_{S_i} → Z_{S_i}` (resp. if `Y_{S′} → Z_{S′}`) is an isomorphism, the same holds
for `Y → Z`; now this is clear (resp. follows from SGA 1, VIII 5.4 or EGA IV₂, 2.7.1).

Moreover, by SGA 1, VIII 2.1 and 5.5, faithfully flat quasi-compact morphisms are of effective descent for the fibered
category of closed immersion arrows. This allows us to restrict ourselves, with the notation of 6.1, to the case where
`S = S′_i`.

Let `(Z_j)` be a covering of `Z` by affine opens such that `O(Z_j)` is a free module over `A = O(S)`, and let
`Y_j = Y ∩ Z_j` and `F_j : (Sch)°/S → (Ens)` be the functor defined in terms of `(Z_j, Y_j)` as `F` in terms of
`(Z, Y)`. It is a subfunctor of the final functor, and one evidently has `F = ⋂_j F_j`, which reduces us to

<!-- original page 19 -->

proving that each `F_j` is representable by a closed subscheme `T_j` of `S` (for then `F` will be representable by the
closed subscheme `T` intersection of the `T_j`). One may therefore suppose `Z` also affine, `Z = Spec(B)`, where `B` is
a free `A`-module. Let `J` be a subset of `B` defining the subscheme `Y` of `Z`, and let `K` be the ideal in `A`
generated by the `u_i(J) ⊆ A`, where the `u_i : B → A` are the coordinate forms with respect to the chosen basis. One
observes at once that `T = V(K) = Spec(A/K)` satisfies the desired condition, which completes the proof.

**Examples 6.5.** Let us give some important examples of functors that reduce to functors `∏_{Z/S} Y/Z` of the type
envisaged in 6.4 and for which it is useful in the sequel to have criteria of representability. We denote by `S` a
prescheme, by `X`, `Y`, `Z`, etc., preschemes over `S`.

<!-- label: III.VIII.6.5 -->

a) Suppose given an `S`-morphism

```text
(*)    q : X → Hom_S(Y, Z),
```

("`X` acts on `Y` with values in `Z`"), i.e. a morphism

```text
(**)   r : X ×_S Y → Z.
```

Consider a subprescheme `Z′` of `Z`, whence a monomorphism

<!-- original page 22 -->

```text
Hom_S(Y, Z′) → Hom_S(Y, Z)
```

which makes the first functor a subfunctor of the second; let `X′` be the inverse image of this subfunctor by `(*)`,
that is the subfunctor of `X` such that `X′(T)` is the set of `x ∈ X(T)` such that `q(x) : Y_T → Z_T` factors through
`Z′_T`. This functor `X′` can be described as follows: set `P = X ×_S Y`, let `P′` be the inverse image of `Z′` by
`r : P → Z`; then one has an evident isomorphism

```text
(***)   X′ ≃ ∏_{P/X} P′/P.
```

One thus obtains: *if `Y` is essentially free over `S` and `Z′` closed in `Z`, the subfunctor `X′` of `X` is
representable by a closed subprescheme of `X`*.

b) Suppose given two ways of making `X` act on `Y` with values in `Z`, i.e. two morphisms

```text
q_1, q_2 : X ⇒ Hom_S(Y, Z),
```

and set `X′ = Ker(q_1, q_2)`: this is the subfunctor of `X` such that `X′(T)` is the set of `x ∈ X(T)` such that the two
morphisms `q_1(x), q_2(x) : Y_T ⇒ Z_T` are equal. Now giving `q_1, q_2` is equivalent to giving a morphism

```text
q : X → Hom_S(Y, Z ×_S Z),
```

or, again, a morphism `r : X ×_S Y → Z ×_S Z`; setting `U = Z ×_S Z`, let `U′` be the diagonal subprescheme of
`Z ×_S Z`; then `X′` is none other than the inverse image of the subfunctor `Hom_S(Y, U′) → Hom_S(Y, U)` by `q`, hence
can be put in the form `(***)`, with `P = X ×_S Y` and `P′` = inverse image of the diagonal by `r`, i.e. kernel of

<!-- original page 23 -->

```text
X ×_S Y ⇒ Z.
```

One is thus in the conditions of (a). One sees consequently that: *if `Y` is essentially free over `S` and `Z` separated
over `S`, the subfunctor `X′` of `X` is representable by a closed subprescheme of `X`*.

c) Suppose given a morphism

```text
q : X → Hom_S(Y, Y),
```

i.e. "`X` acts on `Y`". Let `X′` be the "kernel" of this morphism, i.e. the subfunctor `X′` of `X` such that `X′(T)` is
the set of `x ∈ X(T)` such that `q(x) : Y_T → Y_T` is the identity. This functor is amenable to (b), as one sees by
introducing a second homomorphism

```text
q′ : X → Hom_S(Y, Y)
```

<!-- original page 20 -->

"by making `X` act trivially on `Y`". Hence: *if `Y` is essentially free over `S` and separated over `S`, the kernel
subfunctor of `q` is representable by a closed subprescheme of `X`*.

d) Under the conditions of (c), consider the subfunctor `Y′` of `Y` "of invariants under `X`", so `Y′(T)` is the set of
`y ∈ Y(T)` such that the corresponding morphism `q(y) : X_T → Y_T` is "the `T`-constant morphism with value `y`".
Introducing `q′` as in (c), and the homomorphisms corresponding to `q` and `q′`:

```text
q, q′ : Y ⇒ Hom_S(X, Y),
```

one sees that `Y′` is precisely `Ker(q, q′)`, and is therefore amenable again to (b) (with the roles of `X`, `Y`
reversed and `Z = Y`).

Consequently, *if `X` is essentially free over `S`, `Y` separated over `S`, then the subfunctor `Y′` of `Y` of
invariants under `X` is representable by a closed subprescheme of `Y`*.

<!-- original page 24 -->

e) Constructions of the type explained in the preceding examples are especially frequent in group theory. Thus, when `G`
is an `S`-prescheme in groups acting on the `S`-prescheme `X`:

```text
q : G → Aut_S(X),
```

the kernel of `q` ("the subgroup of `G` acting trivially") is a closed subscheme of `G` provided that `X` is essentially
free and separated over `S` (example (c)), and the subobject `X^G` of invariants is a closed subprescheme of `X`,
provided that `G` is essentially free over `S` and `X` separated over `S`[^N.D.E-VIII-27] (example (d)).

Let `Y`, `Z` be subpreschemes of `X`; consider the subfunctor `Transp_G(Y, Z)` of `G` ("transporter of `Y` into `Z`")
whose points with values in a `T` over `S` are the `g ∈ G(T)` such that the corresponding automorphism of `X_T`
satisfies `g(Y_T) ⊆ Z_T` i.e. induces a morphism `Y_T → X_T` factoring through `Y_T → Z_T`. Hence: *if `Y` is
essentially free over `S`, and `Z` closed in `X`, then `Transp_G(Y, Z)` is a closed subprescheme of `G`* (example (a)).

One may also consider the strict transporter of `Y` into `Z`,[^N.D.E-VIII-28] whose points with values in a `T` over `S`
are the `g ∈ G(T)` such that `g(Y_T) = Z_T`, which is nothing but `Transp_G(Y, Z) ∩ σ(Transp_G(Z, Y))`, where `σ` is the
symmetry of `G`. Consequently, if `Y` and `Z` are essentially free over `S` and closed in `X`, the strict transporter of
`Y` into `Z` is a closed subprescheme of `G`.

An important case is that where `X = G`, with `G` acting on itself by inner automorphisms. If `H` is a subprescheme of
`G`, the strict transporter of `H` into `H` is also called the *normalizer of `H` in `G`*, and denoted `Norm_G H`.
Hence: *if `H` is a closed subprescheme of `G` in groups, essentially free over `S`, then `Norm_G H` is representable by
a closed subprescheme of `G` in groups.*

Let finally `Z` be a subprescheme of `G`; then its *centralizer* `Centr_G(Z)` in `G` is the subfunctor of `G` in groups
defined by the procedure of (d), considering "`Z` acts on `G`" via the action induced by that of `G`; hence *if `Z` is
essentially free over `S` and `G` separated over `S`, `Centr_G(Z)` is a closed subprescheme of `G` in groups*.

<!-- original page 25 -->

In particular, if `G` is essentially free and separated over `S`, then *the center `C` of `G`, which is none other than
`Centr_G(G)`, is a closed subprescheme of `G` in groups*.

When `S` is the spectrum of a field, 6.3 (b) shows that in examples (a) to (e) above, the conditions "essentially free"
are automatically satisfied; only separation conditions remain. Recalling that a prescheme in groups over a field is
necessarily separated, one finds for example:

**Corollary 6.7.**[^N.D.E-VIII-29] *Let `G` be a prescheme in groups over a field `k`. Then:*

<!-- label: III.VIII.6.7 -->

*– For every subprescheme `Z` of `G`, the centralizer of `Z` in `G` is a closed subprescheme of `G` in groups; this is
in particular the case for the center `Centr_G(G)` of `G`.*

*– More generally, if `u, v : X → G` are morphisms of preschemes, `Transp_G(u, v)` is representable by a closed
subprescheme of `G`.*

*– For two subpreschemes `Y, Z` of `G`, with `Z` closed, `Transp_G(Y, Z)` is a closed subprescheme of `G`. If `Y` is
also closed, the same conclusion holds for `Transp^{str}_G(Y, Z)`.*

*– For every subprescheme in groups*[^N.D.E-VIII-30] *`H` of `G`, the normalizer `Norm_G(H)` is a closed subscheme of
`G` in groups.*

**Remark 6.8.**[^N.D.E-VIII-31] *Let `A` be a commutative ring, `M` an `A`-module, `M^∨ = Hom_A(M, A)`; endow the
`A`-module `End_A(M)` with the topology of pointwise convergence (discrete), i.e. a basis of neighborhoods of `0` is
formed by the following `A`-submodules, where `n ∈ ℕ` and `m_1, …, m_n ∈ M`:*

<!-- label: III.VIII.6.8 -->

```text
K(m_1, …, m_n) = { u ∈ End_A(M) | u(m_i) = 0  for i = 1, …, n }.
```

*We say that `M` is a* quasi-free `A`-module *if the image of the canonical morphism `Θ : M ⊗_A M^∨ → End_A(M)` contains
`id_M` in its closure, i.e. if the following condition holds:*

```text
(*)  { for all m_1, …, m_n ∈ M, there exist x_1, …, x_r ∈ M and f_1, …, f_r ∈ M^∨
     { such that m_i = Θ(∑_{s=1}^r x_s ⊗ f_s)(m_i) = ∑_{s=1}^r f_s(m_i) x_s for i = 1, …, n.
```

*(In this case, `Im Θ` is dense in `End_A(M)`, since for every `u ∈ End_A(M)` one has*

```text
u(m_i) = ∑_{s=1}^r f_s(m_i) u(x_s) = Θ(∑_{s=1}^r u(x_s) ⊗ f_s)(m_i).)
```

Let us note first that this property is stable under base change. Indeed, let `φ : A → A′` be a morphism of rings,
`M′ = M ⊗_A A′`, and `m′_1, …, m′_n ∈ M′`. Then `m′_i = ∑_j m_{ij} ⊗ b_{ij}` (`m_{ij} ∈ M`, `b_{ij} ∈ A′`); by
hypothesis, there exist `x_1, …, x_r ∈ M` and `f_1, …, f_r ∈ Hom_A(M, A)` such that `m_{ij} = ∑_s x_s f_s(m_{ij})` for
all `i, j`. Denote by `φ ∘ f_s` the image of `f_s` in `Hom_A(M, A′) = Hom_{A′}(M′, A′)`; then for every `i = 1, …, n`
one has:

```text
(∑_s x_s ⊗ φ ∘ f_s)(m′_i) = ∑_{s,j} x_s ⊗ φ(f_s(m_{ij})) b_{ij} = ∑_j (∑_s x_s f_s(m_{ij})) ⊗ b_{ij} = m′_i,
```

<!-- original page 22 -->

which proves that `M′` is quasi-free over `A′`.

Let us also note that every projective `A`-module `P` is quasi-free (there exist `A`-morphisms
`A^{(I)} -π→ P -τ→ A^{(I)}` such that `π ∘ τ = id_P`; denote by `(e_i)` the canonical basis of `A^{(I)}` and `f_i` the
linear form `e_i^* ∘ τ` on `P`; if `m_1, …, m_n ∈ P`, there exists a finite subset `J` of `I` such that
`m_k = ∑_{i ∈ J} f_i(m_k) π(e_i)` for `k = 1, …, n`).

Then, Theorem 6.4 remains valid if in the statement of Definition 6.1 the word "free" is replaced by "projective" or,
more generally, by "quasi-free". Indeed, proceeding as in the proof of 6.4, one is reduced to proving:

**Lemma 6.8.1.** *Let `M` be a quasi-free `A`-module, `N` a submodule, `F` the covariant functor `(A-algebras) → (Ens)`
such that `F(B) = {pt}` if `M_B = (M/N)_B`, and `F(B) = ∅` otherwise. Then there exists an ideal `K` of `A` such that
`F(B) = {pt}` if and only if the morphism `A → B` factors through `A/K`, i.e. one has a functorial isomorphism in `B`:*

<!-- label: III.VIII.6.8.1 -->

```text
F(B) ≃ Hom_{A-alg.}(A/K, B).
```

*Proof.* Let `(n_j)` be a system of generators of `N`, and let `F_j` be the subfunctor of the final functor `e`
(`e(B) = {pt}` for every `B`) corresponding to the submodule `A n_j`. One has `F(B) = {pt}` if and only if the image of
each `n_j` in `M_B` is zero, hence `F` is the intersection of the functors `F_j`. This reduces us to the case where `N`
is generated by one element `n`.

Let `φ : A → B` be an `A`-algebra; if the image `n ⊗ 1` of `n` in `M_B` is zero, then for every `f ∈ M^∨ = Hom_A(M, A)`
one has `0 = f(n) ⊗ 1 = φ(f(n))`. On the other hand, since `M` is quasi-free, there exist `x_1, …, x_r ∈ M` and
`f_1, …, f_r ∈ M^∨` such that `n = ∑_s f_s(n) x_s`, whence `n ⊗ 1 = ∑_s x_s ⊗ φ(f_s(n))`. It follows that `n ⊗ 1 = 0` if
and only if `φ` factors through `A/K`, where `K` is the ideal generated by the `f_s(n)` for `s = 1, …, r`. This proves
the lemma.

## 7. Appendix. On monomorphisms of preschemes in groups

The result proved in the present § is unnecessary for the sequel of the seminar, except for X 8.8 and XV and XVI. It
rests in an essential way on the existence theorem for quotient groups of Exposé VI_A.[^N.D.E-VIII-32]

<!-- original page 26 -->

Corollary 5.7 leads one to ask under what conditions one can assert that a monomorphism `u : G → H` of `S`-groups is an
immersion, or even a closed immersion.

We have seen in VI_B 1.4.2 that this is the case if `S` is the spectrum of a field, provided that `G` is of finite type
over `k` and `H` is locally of finite type over `k`. One easily concludes that the same result remains valid if one only
supposes `S` Artinian.[^N.D.E-VIII-33]

On the other hand, it is easy to give examples of bijective monomorphisms that are not immersions, with `S` being for
example the affine line over a field, or the spectrum of a discrete valuation ring. One will take for example
`H = (ℤ/2ℤ)_S`, `G = G_1 ×_S G_2`, where `G_1` is the open subgroup of `H`, the complement of the closed point `x`
distinct from `0` of the fiber `H_s ≃ ℤ/2ℤ` (where `s` denotes a fixed closed point of `S`), and `G_2` is the closed
subscheme of `H` that is the sum of the subscheme reduced to the unit section, and the closed reduced subscheme defined
by the closed point `x`. One easily verifies that `G_2` is indeed stable under the multiplication of `H`, hence is a
group scheme. The immersions `G_i → H` (`i = 1, 2`) then define a homomorphism of `S`-groups `G = G_1 × G_2 → H`, which
is obviously a bijective monomorphism (and moreover a local immersion), but is not an immersion. (One observes that `G`
and `H` are reduced, `G` having three disjoint irreducible components, while `H` has only two irreducible components.)
One will note that `G_1 → H` also gives an example of an open subgroup `G` of `H` which is not closed (contrary to what
occurs for algebraic groups over a field). The theory of the degeneration of elliptic curves provides further examples
of this latter phenomenon, with moreover `H` smooth over `S` of relative dimension `1`, and `G` with connected fibers.

It is possible[^VIII-7-star] on the other hand that, as soon as one assumes `G` flat over `S`, and (say) `G` and `H` of
finite presentation over `S`, a monomorphism `u : G → H` of `S`-groups is automatically an immersion. We shall prove a
result of this nature, under supplementary hypotheses.

Let us note first that one may assume `S` affine, and (thanks to the finite presentation hypothesis on `G` and `H`,
which allows one to reduce to the case of the spectrum of a ring of finite type over `ℤ`[^N.D.E-VIII-34]) `S`
Noetherian. Then `G` and `H` are Noetherian. To say that `u : G → H` is a closed immersion (resp. an immersion) then
amounts to saying that `u` is a monomorphism (which is true by hypothesis) and that `u` is proper (resp. and that `u` is

<!-- original page 27 -->

proper at every point of `u(G)`)[^N.D.E-VIII-35]. The valuative criterion of properness assures us that it suffices to
verify that for every base change `S′ → S`, with `S′` the spectrum of a discrete valuation ring, complete if one wishes,
the morphism `u′ : G′ → H′` has the same properness property. (The case of local properness was forgotten in EGA II 7.3,
and will appear as an erratum in EGA IV[^VIII-7-starstar].) This therefore reduces us to the case where `S` itself is
the spectrum of a complete discrete valuation ring — subject to the supplementary hypotheses on `G`, `H`, `u` that we
are led to formulate being stable under base change.

Let then `s` (resp. `s_0`) be the closed point (resp. the generic point) of `S`. Then the homomorphisms induced on the
fibers

```text
u_s : G_s → H_s    and   u_{s_0} : G_{s_0} → H_{s_0}
```

are closed immersions, since these are monomorphisms of group schemes of finite type over fields (VI_B 1.4.2). We may
therefore identify `G_{s_0}` with a closed subscheme of `H_{s_0}`. Now we have the following result:

**Lemma 7.1.** *Let `S` be the spectrum of a discrete valuation ring, `s_0` its generic point, `H` an `S`-prescheme,
`L_0` a closed subprescheme of the generic fiber `H_{s_0}`, so that `L_0` is also a subprescheme of `H`.*

<!-- label: III.VIII.7.1 -->

*Then the schematic closure `L̄_0` in `H` (i.e. the smallest closed subprescheme of `H` majorizing `L_0`, cf. EGA I 9.5)
exists and is also the unique closed subprescheme of `H`, flat over `S`, whose generic fiber is `L_0`. Moreover, the
formation of `L̄` is functorial with respect to a variable couple `(H, L_0)`, and commutes with the formation of
cartesian products over `S`.*

<!-- original page 28 -->

*In particular, if `H` is an `S`-group and `L_0` is a subgroup of `H_{s_0}`, then `L̄` is a subgroup of `H`.*

The proof is immediate and left to the reader[^VIII-7-starstarstar]. Applying this to the situation `H`, `G_{s_0}`, one
sees that the monomorphism `u : G → H` factors as `G → L → H`, where `L` is a subgroup of `H` that is a closed
subprescheme, flat over `S`, and where `G → L` induces an isomorphism on the generic fibers. Then `u : G → H` is an
immersion (resp. a closed immersion) if and only if `u′ : G → L` is. This therefore reduces us to the case where `H` is
flat over `S` and `u_{s_0} : G_{s_0} → H_{s_0}` is an isomorphism (subject to the supplementary hypotheses we may have
to formulate on `G`, `H`, `u` being respected when `H` is replaced by a closed subprescheme in groups). As then `H` is
the schematic closure of `H_{s_0}`, if `u` is an immersion, then `u(G)` will be a subprescheme[^N.D.E-VIII-36] of `H`
majorizing `H_{s_0}`, hence its schematic closure will also be `H`, and consequently `u(G)` will be an open subprescheme
of `H`. Hence, we shall in fact have to prove that `u` is an open immersion (resp. an isomorphism, if we want to
establish that `u` is a closed immersion). Since `G` and `H` are flat

<!-- original page 29 -->

over `S`, it amounts to the same thing to say that the morphisms induced on the fibers are open immersions, resp.
isomorphisms (cf. SGA 1, I 5.7), and since this is already the case for `u_{s_0}`, one is reduced to proving that `u_s`
is an open immersion, resp. an isomorphism.

Let us note first that, since `G` and `H` are flat over `S`, the dimension of their fibers remains constant (VI_B 4.3).
Since `G` and `H` have the same generic fiber, it follows that this dimension is the same for `G` and `H`, hence
`u_s : G_s → H_s` is a monomorphism of algebraic groups of the same dimension. One concludes easily that `G_s` is open
in `H_s`, and in fact is set-theoretically a union of connected components of `H_s` (one is reduced to the case where
the base field is algebraically closed, and `G` and `H` reduced, hence smooth over `k`, where it is immediate…). Hence
`H_s − G_s` is closed in `H_s`, hence in `H`, hence its complement `H_0` in `H` is open, and is obviously an open stable
under the group law of `H`. Hence, up to replacing `H` by `H_0`, one may, in order to prove that `u` is an immersion,
reduce (with the usual proviso) to the case where, in addition to the preceding hypotheses, one assumes `u` bijective,
i.e. `u_s : G_s → H_s` bijective. One is therefore in any case reduced to proving that `u` or again `u_s` is an
isomorphism, possibly under the hypothesis of bijectivity.

Suppose therefore first that `u` is bijective. If `H_s` is reduced, one can evidently conclude that `u_s` is an
isomorphism, since `G_s` identifies with a closed subscheme of `H_s` having the same underlying set. In particular, if
`k = κ(s)` is of characteristic zero, every algebraic group over `k` is reduced by Cartier (cf. VI_B, 1.6.1, or VII_B,
3.3.1, or EGA IV₄, 16.12.2 and 17.12.5), and one has thus obtained:

**Proposition 7.2.** *Let `u : G → H` be a homomorphism of preschemes in groups of finite presentation over `S`. Suppose
that `u` is a monomorphism, `G` flat over `S`, and the residue fields of `S` of characteristic zero. Then `u` is an
immersion.*

<!-- label: III.VIII.7.2 -->

When `κ(s)` is of characteristic `p > 0`, we shall restrict to the case where `G` is commutative. Then (with the
reductions made) `H` is also commutative, since it is the schematic closure of `H_{s_0}` which is isomorphic to
`G_{s_0}`, hence commutative. For every integer `n ⩾ 0`, we set `S_n = Spec(V/m^{n+1})` (where `V` is the valuation ring
defining `S` and `m` its maximal ideal), `G_n = G ×_S S_n`, `H_n = H ×_S S_n`. For every integer `m > 0`, we also
introduce the subgroups `_mG` and `_mH` of `G` and `H`, kernels of the `m`-th power. One defines similarly
`_m(G_n) = (_mG)_n`, which one denotes simply `_mG_n`, and likewise for `H`.

By virtue of VI_A 3.2, one can form the quotients `Q_n = H_n/G_n`. Then `Q_n` is a commutative group scheme over `S_n`,
flat over `S_n`, and `H_n → Q_n` is a faithfully flat morphism with kernel `G_n`. Since the formation of quotients
commutes with base extension[^N.D.E-VIII-37], one has

```text
Q_n ≃ Q_m ×_{S_m} S_n    for m ⩾ n,
```

in particular the fiber `Q_n ×_{S_n} S_0` is none other than `Q_0 = H_0/G_0`. Since `G_0` has the same

<!-- original page 30 -->

underlying set as `H_0`, then `Q_0` is set-theoretically reduced to a single point: it is a purely infinitesimal group.
Consequently, each `Q_n` is finite and flat over `S_n`. Hence `Q_n` is defined by an algebra `C_n` over
`V_n = V/m^{n+1}` which is a free module of finite type over this ring, and for `m ⩾ n` one has `C_n = C_m ⊗_{V_m} V_n`,
an isomorphism also respecting the diagonal map. One thus obtains a free module of finite type `C = lim_{←} C_n` over
`V = lim_{←} V_n`, and the diagonal maps of the `C_n` define a diagonal map of `C`, so that `Q = Spec(C)` becomes a
group scheme finite and flat over `S`, such that

```text
Q ×_S S_n = Q_n
```

for every `n`.

**Lemma 7.3.**[^N.D.E-VIII-38] *Let `K` be a field, `Q` a finite group scheme over `K`, of degree `n`. Then the `n`-th
power morphism in `Q` is zero.*

<!-- label: III.VIII.7.3 -->

Cf. VII_A 8.5.

**Remark 7.3.1.** *Statement 7.3 retains a sense for a group scheme `Q/S` finite and locally free over `S`, `S` being an
arbitrary base prescheme. It would be interesting to find a proof in this general case.*

<!-- label: III.VIII.7.3.1 -->

One will note that 7.3 (i.e. VII_A, 8.5) proves in any case that the envisaged statement is true if `S` is reduced, as
one sees by applying 7.3 to the fibers of `Q` at the maximal points (i.e. generic points of the irreducible components)
of `S`.[^N.D.E-VIII-39]

In particular, under the conditions of the preceding proof, where `S` is the spectrum of a discrete valuation ring and
`Q` is commutative, one finds that `n · id_Q = 0`. Moreover, here `n` is a power `p^{ν_0}` of the residue
characteristic, and one finds:

**Corollary 7.4.** *With `Q` and the `Q_n` as above, and their common degree being `p^{ν_0}`, one will have
`p^{ν_0} · id_Q = 0` and consequently `p^{ν_0} · id_{Q_n} = 0` for every `n`.*

<!-- label: III.VIII.7.4 -->

<!-- original page 31 -->

**Corollary 7.5.** *Suppose moreover that `G_0` is smooth over `k`, and the homomorphism `p · id_{G_0}` flat (which
amounts to saying, in virtue of the structure of algebraic groups over an algebraically closed field `k̄`, that `G_{k̄}`
contains no subgroup isomorphic to the additive group). Then for every `ν ⩾ ν_0` and `n > 0`, the group `_{p^ν}H_n` is
flat over `S_n`.*

<!-- label: III.VIII.7.5 -->

Indeed, it follows from `p^{ν_0} · id_{Q_n} = 0` that `p^ν · id_{H_n}` factors through `G_n`, so that one has a
commutative diagram:

```text
                         p^ν · id_{H_n}
            H_n  ─────────────────────────────→  H_n
              ╲                                    ↑
               ╲ v_n                              u_n
            u_n ╲                                  │
                 ↘    p^ν · id_{G_n}              │
                  G_n  ─────────────────────────→ G_n.
```

I claim that `v_n` is flat. Indeed, since `H_n` and `G_n` are flat over `S_n`, one is reduced to verifying that `v_0` is
flat (SGA 1, IV 5.9), so one may assume that `n = 0`, whence `S_n = Spec(k)`. Since `p · id_{G_0}`, and hence
`p^ν · id_{G_0}`, is flat, its image is an open induced subgroup `G′_0` of `G_0`, and since `u_0 : G_0 → H_0` is
surjective, it follows that `v_0` takes its values in `G′_0`, hence may be considered as a homomorphism into `G′_0`.
Since its composition with `u_0` is an epimorphism, it is itself an epimorphism, hence a flat homomorphism into `G′_0`,
hence a flat homomorphism into `G_0`. Hence `v_n` is flat, hence `Ker v_n = _{p^ν}H` is flat over `S`. QED.

**Remark.** We have not explicitly used the fact that `G_0` is smooth over `k`; but it is easy to see that this is a
consequence of the fact that `p · id_G` is flat — this is why we made this condition explicit in the hypothesis of
Corollary 7.5.

**Lemma 7.6.** *Let `u : G → H` be a surjective monomorphism of commutative algebraic groups over a field `k` of
characteristic `p > 0`; consider the (purely infinitesimal) group `Q = H/G`. Then there exists an integer `ν_1` such
that for `ν ⩾ ν_1`, the sequence*

<!-- label: III.VIII.7.6 -->

```text
0 → _{p^ν}G → _{p^ν}H → Q → 0
```

*is exact.*

It suffices to ensure exactness at `Q`, and for this to ensure that the homomorphism

```text
(*)    O_{Q,e} → O_{_{p^ν}H, e}
```

of local rings at the neutral elements is injective (N.B. recall that `Q` is set-theoretically reduced to the element
`e`). Now one has a natural homomorphism

```text
(**)   O_{_{p^ν}H, e} → O_{H,e}/m^{p^ν},
```

where `m` is the augmentation ideal (i.e. the maximal ideal) of `O_{H,e}`, as one sees by noting that `p^ν · id_H`
vanishes on the kernel of "the iterated Frobenius homomorphism" `F^ν`; the composite of the homomorphisms `(*)` and
`(**)` is also equal to the natural composite

```text
(***)  O_{Q,e} → O_{H,e} → O_{H,e}/m^{p^ν}.
```

<!-- original page 32 -->

Now `O_{Q,e} → O_{H,e}` is injective, since `H → Q` is an epimorphism hence is flat; on the other hand `O_{Q,e}` is
Artinian, and finally the intersection in `O_{H,e}` of the `m^{p^ν}` is reduced to `0`, hence so is the intersection of
their traces on `O_{Q,e}`. Consequently one of these traces is reduced to `0`, which proves that `(***)` is injective,
and a fortiori `(*)` is injective.

**Lemma 7.7.** *Under the conditions of 7.5 there exists a `ν_1` such that, for `ν ⩾ ν_1` and every `n`, the sequence of
`S_n`-groups*

<!-- label: III.VIII.7.7 -->

```text
0 → _{p^ν}G_n → _{p^ν}H_n -w_n→ Q_n → 0
```

*is exact (more precisely, `w_n` is faithfully flat and its kernel is `_{p^ν}G_n`).*

One takes `ν_1` as in 7.6 applied to `u_0 : G_0 → H_0`, and `ν_1 ⩾ ν_0` (where `p^{ν_0}` = rank `Q_0`). It only remains
to verify that `w_n` is faithfully flat. Now by virtue of 7.5, `_{p^ν}H` is flat over `S_n`, and since `Q_n` is too, one
is reduced to verifying that `w_0 : _{p^ν}H_0 → Q_0` is faithfully flat, i.e. is an epimorphism, which is true by the
choice of `ν_1`.

**Corollary 7.8.** *Suppose moreover `H` separated over `S`, more generally that `_{p^ν}H` is separated over `S` for
every `ν`, and that `_{p^ν}G` is finite over `S` for every `ν`. Then the group schemes `_{p^ν}G` and `_{p^ν}H` are
finite and flat over `S` for `ν ⩾ ν_1`, and one has an exact sequence*

<!-- label: III.VIII.7.8 -->

```text
0 → _{p^ν}G → _{p^ν}H -w→ Q → 0.
```

Since `u : G → H` is surjective, so is the induced morphism `_{p^ν}G → _{p^ν}H`, and since the first member is finite
over `S` and the second separated over `S`, it follows that the second member is finite over `S`. To then verify that
`_{p^ν}G` and `_{p^ν}H` are also flat over `S`, it suffices to verify that this is the case for `_{p^ν}G_n` and
`_{p^ν}H_n` for every `n`, which is contained in 7.5. Finally, the exact sequence of 7.8 comes from the exact sequences
7.7 for variable `n`.

<!-- original page 34 -->

Taking the generic fibers in the exact sequence 7.8 and recalling that `u_{s_0} : G_{s_0} → H_{s_0}` is an isomorphism,
one finds `Q_{s_0}` = unit group, whence (since `Q` is flat over `S`) `Q` = unit group, whence `Q_s` = unit group, hence
`u_s : G_s → H_s` is an isomorphism. Hence:

**Proposition 7.9.** *Let `u : G → H` be a homomorphism of preschemes in groups of finite presentation over the
prescheme `S`. Suppose:*

<!-- label: III.VIII.7.9 -->

*a) `u` is a monomorphism.*

*b) `G` is flat over `S`.*

*c) For every `s ∈ S` such that `κ(s)` is of residue characteristic `p > 0`, one wants the following conditions to be
satisfied for the homomorphism `u′ : G′ → H′` of preschemes in groups over `S′ = Spec(O_{S,s})` deduced from `u : G → H`
by the base change `S′ → S`:*

*– `G′` is commutative,*

*– the special fiber `G′_0 = G_s` is smooth over `κ(s)`,*

*– for every integer `ν > 0`, `_{p^ν}G′` is finite over `S′` and `_{p^ν}H′` is separated over `S′`.*

*Under these conditions, `u` is an immersion.*

It suffices to remark that, in (c), the condition that `_pG′_0` be finite over `S′` implies that `_pG′_0` is finite over
`κ(s)`, which already implies that `G′_0 ⊗_{κ(s)} \overline{κ(s)}` contains no subgroup isomorphic to the additive
group, so that one is under the hypotheses of 7.5.

<!-- original page 29 -->

**Remark 7.10.** *Examples of M. Raynaud (XVI 1.1 (a) and (b)) show that in (c) one cannot drop either the hypothesis
that the `_{p^ν}G′` are finite over `S′` or the hypothesis that the `_{p^ν}H′` are separated over `S′`.*

<!-- label: III.VIII.7.10 -->

We now want conditions ensuring that `u` is a closed immersion. We therefore preserve the hypotheses preceding 7.9 but
no longer assume `u` surjective (only `u` an isomorphism on the generic fibers). We already know that `u : G → H` is an
open immersion, hence also `u_0 : G_0 → H_0`, whose image therefore contains the connected component of the identity
element `(H_0)^0`. Note that, since `G_0` is smooth over `k` and "without additive component" over the algebraic closure
of `k`, the same holds for `H_0`. Now we have:

**Lemma 7.11.** *Let `H` be a commutative algebraic group over a field `k`, such that `H ⊗_k k̄` contains no subgroup
isomorphic to `G_a`. Let `n` = degree `H/H^0`; then the homomorphism*

<!-- label: III.VIII.7.11 -->

```text
_nH → H/H^0
```

*is surjective.*

One may indeed assume `k` algebraically closed, and then this follows from the well-known fact that `H^0(k)` is a
divisible group.

Suppose now (returning to our situation `u : G → H`) that the `_nG` (`n > 0`) are proper over `S`, and the `_nH` are
separated over `S`. Note on the other hand that the `_nH` are flat over `S`. Indeed, it suffices to see this at the
points above `s`; one is then reduced to proving that `n · id_H` is flat at the points above `s`, and for this one is
reduced to verifying that `n · id_{H_0}` is flat, which is equivalent (as we have already noted) to the fact that
`(H_0)^0` is smooth[^N.D.E-VIII-40] over `k` and has no `G_a`-component over the algebraic closure of `k`. As
`(H_0)^0 = (G_0)^0`, this follows from the analogous hypothesis made on `G_0`. On the other hand, the `_nH` are
separated over `S` since `H` is, hence the morphism `_nG → _nH` is proper, hence its image is closed. As this image
contains the generic fiber of `_nH` (since `u_{s_0} : G_{s_0} → H_{s_0}` is an isomorphism) and `_nH` is flat over `S`,
hence identical to the closure of its generic fiber, it follows that `_nG → _nH` is surjective, hence `_nG_0 → _nH_0` is
surjective. Recalling that `G_0 ⊃ (H_0)^0` and applying 7.11, one finds that `G_0 → H_0` is surjective, hence `u` is
surjective. One thus obtains:

**Proposition 7.12.** *With the notation of 7.9, suppose conditions (a) and (b) hold, as well as condition (c′)
(stronger than (c)), obtained by requiring that for every integer `n > 0` (not only of the form `p^ν`), `_nG′` be finite
over `S′` and `_nH′` separated over `S′`. Under these conditions, `u` is a closed immersion.*

<!-- label: III.VIII.7.12 -->

<!-- original page 36 -->

**Remark 7.13.** *a) One easily verifies that the separation hypothesis made on the `_nH` implies in fact that `H` is
separated over `S`. This is moreover formally contained in 7.12 by taking for `G` the unit `S`-group. Note also that
when `S` is locally Noetherian, one may in 7.9 restrict to assuming `H` locally of finite type over `S` (in*

<!-- label: III.VIII.7.13 -->

<!-- original page 30 -->

*place of: of finite type over `S`), the proof given applying as it stands; for 7.12 one will moreover assume that the
fibers of `H` are of finite type.*

*b) Using 7.12, it is not difficult to prove that if `u : G → H` is a monomorphism of `S`-preschemes in groups of finite
presentation, with `G` diagonalizable (or more generally, "of multiplicative type") and `H` separated over `S`, then `u`
is a closed immersion — which constitutes a satisfactory generalization of the first conclusion stated in 5.7. When `G`
is smooth over `S`, it suffices to apply 7.12, and the general case reduces easily to that one. When one no longer
assumes `H` separated over `S`, one can still show that `u` is an immersion; in the case where `G` is a torus, this fact
moreover follows also from what follows.*

*c) When in 7.9 one assumes `G` has connected fibers, one can in condition 7.9 (c) drop the hypothesis that the
`_{p^ν}H′` be separated over `S′`. Indeed, with the reductions made in the proof, one may assume `H` flat over `S` and
`u` bijective, hence `H` with connected fibers, hence `H` separated over `S` by virtue of Raynaud's theorem (VI_B
5.5).*[^N.D.E-VIII-41]

## Bibliography

[^N.D.E-VIII-42]

[RG71] M. Raynaud, L. Gruson, *Critères de platitude et de projectivité*, Invent. math. **13** (1971), 1–89.

[TO70] J. Tate, F. Oort, *Group schemes of prime order*, Ann. scient. Éc. Norm. Sup. (4) **3** (1970), 1–21.

______________________________________________________________________

## Footnotes

<!-- LEDGER DELTA — Exposé VIII — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| bidualité | biduality | Section title (§1). |
| réflexif (relativement à I) | reflexive (relative to I) | Definition 1.0; preserved as technical term. |
| anti-équivalence | anti-equivalence | Standard. |
| extension de la base | base extension | Standard. |
| accouplement (de G et G′ à valeurs dans I) | pairing (of G and G′ with values in I) | Standard. |
| morphisme bilinéaire | bilinear morphism | Standard. |
| foncteur-groupe commutatif | commutative group functor | Per Exp. I §2.1. |
| application localement constante | locally constant map | Standard. |
| graduation de type M | M-grading | Standard. |
| facteur direct | direct factor / direct summand | Used "direct factor" to preserve source. |
| descente de la représentabilité | descent of representability | Section heading §1.7. |
| foncteur local | local functor | Standard (sheaf for Zariski). |
| donnée de descente | descent datum | Per SGA 1. |
| donnée de descente effective | effective descent datum | Per SGA 1. |
| topologie (fpqc) | (fpqc) topology | Source uses parentheses; preserved. |
| fidèlement plat et quasi-compact | faithfully flat and quasi-compact | Standard. |
| M-effectif | M-effective | Preserved from Exp. IV §3.4. |
| schéma en groupes commutatifs constant | constant commutative group scheme | Standard. |
| schéma en groupes des racines n-èmes de l'unité | group scheme of n-th roots of unity | `μ_n` notation; standard. |
| caractéristiques résiduelles | residue characteristics | Standard. |
| sous-groupe de torsion | torsion subgroup | Standard. |
| groupe de torsion | torsion group | Standard. |
| transposé (d'un homomorphisme) | transposed (of a homomorphism) | `u^t` for the transposed map. |
| faisceau quotient | quotient sheaf | Standard. |
| (immersion) fermée / ouverte | closed / open (immersion) | Standard. |
| immersion locale | local immersion | Standard. |
| torseur / fibré principal homogène | torsor / principal homogeneous bundle | SGA 3 uses both; preserved. |
| formellement principal homogène | formally principal homogeneous | Standard. |
| algèbre quasi-cohérente graduée de type M | quasi-coherent M-graded algebra | Standard. |
| module inversible | invertible module | Standard. |
| théorème 90 de Hilbert | Hilbert's Theorem 90 | Standard. |
| forme tordue (de G_m) | twisted form (of G_m) | Per glossary. |
| morphisme de norme | norm morphism | Standard. |
| cohomologie galoisienne | Galois cohomology | Standard. |
| morphisme graphe | graph morphism | Standard. |
| essentiellement libre | essentially free | Definition 6.1; standard. |
| quasi-libre | quasi-free | Remark 6.8; preserved as technical coinage. |
| convergence ponctuelle discrète | pointwise convergence (discrete) | Topology on End_A(M). |
| transporteur strict | strict transporter | Per glossary (centralizer / transporter family). |
| normalisateur | normalizer | Per glossary. |
| centralisateur | centralizer | Per glossary. |
| centre | center | Per glossary. |
| automorphismes intérieurs | inner automorphisms | Standard. |
| sous-groupe distingué | normal subgroup | English does not distinguish; not used here. |
| adhérence schématique | schematic closure | Per SGA/EGA. |
| critère valuatif de propreté | valuative criterion of properness | Standard. |
| fibre générique / spéciale | generic / special fiber | Standard. |
| point fermé | closed point | Standard. |
| anneau de valuation discrète | discrete valuation ring | Standard. |
| purement infinitésimal | purely infinitesimal | Standard. |
| morphisme propre | proper morphism | Per glossary. |
| immersion (locale / ouverte / fermée) | (local / open / closed) immersion | Per glossary. |
| de présentation finie | of finite presentation | Per glossary. |
| de type fini | of finite type | Per glossary. |
| « lisse » remplaçant « simple » | "smooth" replacing "simple" | Per N.D.E. terminology update. |
| Frobenius itéré | iterated Frobenius | Standard. |
| sous-groupe radiciel / sous-tore | root subgroup / subtorus | Per glossary. |
| composante connexe de l'élément neutre | connected component of the identity element | Standard `H^0`. |
| groupe divisible | divisible group | Standard. |
| ν-ième puissance / p-ième puissance | ν-th power / p-th power | Standard. |
| groupe additif (G_a) | additive group (G_a) | Standard. |
| anneau local artinien | Artinian local ring | Per glossary. |
| morphisme diagonal | diagonal morphism | Standard. |
| relation de cocycle | cocycle relation | Standard. |
| anneau de valuation | valuation ring | Standard. |
| en bidegré (m,n) | in bidegree (m,n) | Standard. |
-->

[^VIII-0-0]: Version notice of the 2009 re-edition.

[^N.D.E-VIII-1]: N.D.E.: The original has been expanded in what follows.

[^N.D.E-VIII-2]: N.D.E.: We have added the numbering 1.0, 1.0.1, … in order to highlight the definitions and statements
    that occur there.

[^N.D.E-VIII-3]: N.D.E.: We have added the sentence that follows.

[^N.D.E-VIII-4]: N.D.E.: We have expanded what follows.

[^N.D.E-VIII-5]: N.D.E.: Indeed, if one denotes by `F(M)` (resp. `G(M)`) the left-hand (resp. right-hand) side of (2),
    and if `M = M_1 ⊕ M_2`, one has a canonical isomorphism `F(M) = F(M_1) ⊕ F(M_2)`, and likewise for `G`.
    This reduces us to verifying that `θ` is an isomorphism when `M = ℤ/rℤ`, for an integer `r ⩾ 0`. In
    this case, `F(M) = (_rN)_S`, where `_rN` is the kernel of `r · id_N`, and, for every `T → S`, the
    homomorphism

    ```text
    F(M)(T) = Γ(_rN_T/T) → G(M)(T) = _rΓ(N_T/T)
    ```

    is bijective, whence the desired result.

[^N.D.E-VIII-6]: N.D.E.: The original stated after 1.5: "One concludes more generally that if `G`, `H` are locally
    diagonalizable, with `H` of finite type, then `Hom_{S-gr.}(G, H)` is representable." We have included
    this assertion in the statement of 1.5, and have made its proof explicit in 1.7.

[^N.D.E-VIII-7]: N.D.E.: One should add a statement 1.5.1 treating the functor `Isom_{S-gr.}(G, H)`, considered in X
    5.10 and 5.11…

[^N.D.E-VIII-8]: N.D.E.: We have added this paragraph, to make explicit the "local on `S`" character of the
    representability of certain sheaves on `S`, used many times in the sequel (and implicitly in the
    original).

[^N.D.E-VIII-9]: N.D.E.: See also Remark XI 3.4.

[^N.D.E-VIII-10]: N.D.E.: For another effectivity criterion, see later X 5.4–5.6.

[^N.D.E-VIII-11]: N.D.E.: (since `G` is flat over `S`, by (a)).

[^N.D.E-VIII-12]: N.D.E.: We have added what follows, and have detailed the proof accordingly.

[^N.D.E-VIII-13]: N.D.E.: The original has been expanded in what follows.

[^N.D.E-VIII-14]: N.D.E.: We have added what follows.

[^N.D.E-VIII-15]: N.D.E.: We have corrected 4.1 to 4.2.

[^N.D.E-VIII-16]: N.D.E.: We have expanded the passage that follows.

[^N.D.E-VIII-17]: N.D.E.: We have added the sentence that follows.

[^N.D.E-VIII-18]: N.D.E.: Indeed, for every `b ∈ A`, `a_m ∈ A_m`, one has `θ(b ⊗ a_m) = b a_m ⊗ e_m`, hence the
    surjectivity of `θ` is equivalent to `(*)`.

[^N.D.E-VIII-19]: N.D.E.: We have denoted by `K` the ideal denoted `J` in the original, in order to distinguish it from
    the ideals `J_p` of `A_0` appearing in `(***)`. We have also made explicit later that the relations
    `(**)` are equivalent to the equality `K = K′` (see what follows).

[^N.D.E-VIII-20]: N.D.E.: It follows from 5.2 that `∑_{p ≠ 0} J_p = A_0`, hence `1` is written as a finite sum
    `∑_i x_i`, with `x_i ∈ J_{p_i}`.

[^N.D.E-VIII-21]: N.D.E.: cf. EGA II, 2.7.1 (vi).

[^VIII-6-star]: The present § is independent of the theory of diagonalizable groups; its natural place would be in VI_B.

[^N.D.E-VIII-22]: N.D.E.: One can replace "free" by "projective", cf. 6.8 below. On the other hand, this notion is to be
    compared with that of `S`-prescheme flat and pure, introduced and developed in [RG71]; see in
    particular *loc. cit.*, Part I, 3.3.12 and Part II, 3.1.4.1.

[^N.D.E-VIII-23]: N.D.E.: Indeed, let `(A, m)` be an Artinian local ring, `k` its residue field, `M` an arbitrary
    `A`-module, `(x_i)_{i ∈ I}` elements of `M` whose images form a basis of `M/mM` over `k`. Let `F` be
    the free `A`-module with basis `(e_i)_{i ∈ I}`, and `φ : F → M` the `A`-morphism defined by
    `φ(e_i) = x_i`. Then `Q = Coker φ` satisfies `Q = mQ`, whence, since `m` is nilpotent, `Q = 0`.
    Suppose moreover `M` flat over `A`; then `K = Ker φ` satisfies `K ⊗_A k = 0`, i.e. `K = mK`, whence
    `K = 0`.

[^N.D.E-VIII-24]: N.D.E.: cf. II.1, where this functor is denoted `∏_{Z/S} Y`.

[^N.D.E-VIII-25]: N.D.E.: We have corrected "Z" to "S".

[^N.D.E-VIII-26]: N.D.E.: We have expanded the original in what follows; see also 1.7.3.

[^N.D.E-VIII-27]: N.D.E.: We have corrected "S" to "S".

[^N.D.E-VIII-28]: N.D.E.: denoted `Transp^{str}_G(Y, Z)`.

[^N.D.E-VIII-29]: N.D.E.: We have kept the numbering of the original: there is no 6.6.

[^N.D.E-VIII-30]: N.D.E.: Indeed, over a field `k`, every subprescheme in groups of `G` is closed, cf. VI_A, 0.6.1.

[^N.D.E-VIII-31]: N.D.E.: We have expanded the original in what follows; in particular we have added Lemma 6.8.1.

[^N.D.E-VIII-32]: N.D.E.: cf. Exp. VI_A, Theorems 3.2 and 3.3.2.

[^N.D.E-VIII-33]: N.D.E.: take into account the additions made in VI_B…

[^VIII-7-star]: In fact, M. Raynaud has constructed a counter-example, with `G` smooth with connected fibers, cf. XVI
    1.1 (c). If one does not assume `G` has connected fibers, one may take `S = Spec(ℤ_2)`, `G = (ℤ/2ℤ)_S`
    deprived of the non-neutral closed point, `H = (μ_2)_S`.

[^N.D.E-VIII-34]: N.D.E.: cf. EGA IV₃, § 8, and Exp. VI_B, § 10.

[^N.D.E-VIII-35]: N.D.E.: cf. EGA IV₃, 8.11.5 and 15.7.1.

[^VIII-7-starstar]: Cf. EGA IV₃, 15.7.

[^VIII-7-starstarstar]: Cf. EGA IV₂, 2.8.

[^N.D.E-VIII-36]: N.D.E.: We have suppressed the word "closed".

[^N.D.E-VIII-37]: N.D.E.: Make this explicit in Exp. V and VI_A…

[^N.D.E-VIII-38]: N.D.E.: We have suppressed here the hypothesis that `Q` be commutative, and have modified 7.3.1
    accordingly. Note that if `Q` is not commutative, the `n`-th power morphism is not in general a group
    homomorphism.

[^N.D.E-VIII-39]: N.D.E.: Add this in VII_A — On the other hand, the statement is true for every `S` if `Q` is
    commutative, cf. Deligne's theorem in [TO70], p. 4.

[^N.D.E-VIII-40]: N.D.E.: We have updated the terminology, replacing "simple" by "smooth" (see, for example, footnote
    (1) of A. Grothendieck in SGA 1, Exp. II).

[^N.D.E-VIII-41]: N.D.E.: specify in VI_B § 5 this attribution, which appeared in SGAD 1965, indicating the
    modifications between SGAD and Lect. Notes 151.

[^N.D.E-VIII-42]: N.D.E.: additional references cited in this Exposé.
