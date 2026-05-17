# Exposé I. Global and local cohomological invariants with respect to a closed subspace

<!-- label: I -->

<!-- original page 5 -->

## 1. The functors `Γ_Z`, `ΓZ`

<!-- label: I.1 -->

Throughout this Exposé we write `ΓZ` for the sheafified section-with-support functor (underlined in the original source)
and `Γ_Z` for the global one.

<!-- original page 6 -->

Let `X` be a topological space, and let `C_X` be the category of abelian sheaves on `X`. Let `Φ` be a family of supports
in the sense of Cartan; one defines the functor `Γ_Φ` on `C_X` by:

```text
Γ_Φ(F) = subgroup of Γ(F) formed by the sections f such that support f ∈ Φ.
```

<!-- label: eq:I.1.1 -->

If `Z` is a closed part of `X`, we designate by abuse of language by `Γ_Z` the functor `Γ_Φ`, where `Φ` is the set of
closed parts of `X` contained in `Z`. Hence one has:

```text
Γ_Z(F) = subgroup of Γ(F) formed by the sections f such that support f ⊂ Z.
```

<!-- label: eq:I.1.2 -->

We wish to generalize this definition to the case where `Z` is a locally closed part of `X`, hence closed in a suitable
open part `V` of `X`. In this case we shall set:

```text
Γ_Z(F) = Γ_Z(F|V).
```

<!-- label: eq:I.1.3 -->

It must be verified that `Γ_Z(F)` "does not depend" on the open set chosen. It suffices to show that if `V′`, with
`V ⊃ V′ ⊃ Z`, is an open set, then the map `ρ^V_{V′}: F(V) → F(V′)` maps `Γ_Z(F|V)` isomorphically onto `Γ_Z(F|V′)`. Now

```text
Γ_Z(F|V) = ker ρ^V_{V−Z},
```

<!-- label: eq:I.1.4 -->

so if `f ∈ Γ_Z(F|V)` and if `ρ^V_{V′}(f) = ρ^V_{V−Z}(f) = 0`, then `f = 0`, since `(V′, V − Z)` is a covering of `V`.
Likewise, if `f′ ∈ Γ_Z(F|V′)`, then `f′ ∈ F(V′)` and `0 ∈ F(V − Z)` define an `f ∈ F(V)` such that `ρ^V_{V′}(f) = f′`,
`f ∈ Γ_Z(F|V)`; hence `ρ^V_{V′}` induces an isomorphism `Γ_Z(F|V) → Γ_Z(F|V′)`.

<!-- original page 7 -->

Note that every open set `W` of `Z` is induced by an open set `U` of `X` in which `W` is closed. It follows that
`W ↦ Γ_W(F)` defines a presheaf on `Z`, and one verifies that this is a sheaf, which we shall denote `i^!(F)`, where
`i: Z → X` is the canonical immersion. One finds:

```text
Γ_Z(F) = Γ(i^!(F)).
```

<!-- label: eq:I.1.5 -->

The sheaf `i^!(F)` is a subsheaf of `i*(F)`; indeed, the canonical homomorphism

```text
Γ(F|U) = Γ(U, F) ⟶ Γ(U ∩ Z, i*(F))
```

is injective on `Γ_{U∩Z}(F|U) ⊂ Γ(F|U)`. Summarizing, we have the following result:

**Proposition.**

<!-- label: I.1.1 -->

There exists a unique subsheaf `i^!(F)` of `i*(F)` such that, for every open set `U` of `X` such that `U ∩ Z` is closed
in `U`,

```text
Γ(F|U) = Γ(U, F) ⟶ Γ(U ∩ Z, i*(F))
```

induces an isomorphism `Γ_{U∩Z}(F|U) → Γ(U ∩ Z, i^!(F))`.

Note that if `Z` is open, one will simply have

```text
i^!(F) = i*(F) = F|Z, Γ_Z(F) = Γ(Z, F).
```

<!-- label: eq:I.1.6 -->

Suppose again that `Z` is arbitrary. Then, for `U` a variable open set of `X`, one sees that

```text
U ⟼ Γ_{U∩Z}(F|U) = Γ(U ∩ Z, i^!(F))
```

is a sheaf on `X`, which we shall denote `ΓZ(F)`; more precisely, by the preceding formula (expressing that `i^!`
commutes with restriction to open sets) one has an isomorphism

```text
ΓZ(F) = i_*(i^!(F))
```

<!-- label: eq:I.1.7 -->

<!-- original page 8 -->

by definition, one has, for every open set `U` of `X`,

```text
Γ(U, ΓZ(F)) = Γ_{U∩Z}(F|U).
```

<!-- label: eq:I.1.8 -->

Let us note here a characteristic difference between the case where `Z` is closed and the case where `Z` is open. In the
first case, formula (8) shows us that `ΓZ(F)` can be regarded as a subsheaf of `F`, and one thus has a canonical
immersion

```text
ΓZ(F) ↪ F.
```

<!-- label: eq:I.1.8′ -->

In the case where `Z` is open, on the contrary, one sees from (6) that the right-hand side of (8) is `Γ(U ∩ Z, F)`, so
receives `Γ(U, F)`, hence one has a canonical homomorphism in the opposite direction from the previous one:

```text
F ⟶ ΓZ(F),
```

<!-- label: eq:I.1.8″ -->

which is moreover none other than the canonical homomorphism[^N.D.E-I-1]

```text
F ⟶ i_* i*(F),
```

taking into account the isomorphism

```text
ΓZ(F) ≃ i_* i*(F)
```

<!-- label: eq:I.1.6bis -->

deduced from (6) and (7).

<!-- original page 9 -->

Of course, for `F` variable, `Γ_Z(F)`, `ΓZ(F)`, `i^!(F)` may be considered as functors in `F`, with values respectively
in the category of abelian groups, of abelian sheaves on `X`, and of abelian sheaves on `Z`. It is sometimes convenient
to interpret the functor

```text
i^!: C_X ⟶ C_Z
```

as the right adjoint of a well-known functor

```text
i_!: C_Z ⟶ C_X
```

defined by the following proposition:

**Proposition.**

<!-- label: I.1.2 -->

Let `G` be an abelian sheaf on `Z`. Then there exists a unique subsheaf of `i_*(G)`, say `i_!(G)`, such that, for every
open set `U` of `X`, the (identity) isomorphism

```text
Γ(U ∩ Z, G) = Γ(U, i_*(G))
```

defines an isomorphism

```text
Γ_{Φ_{U∩Z,U}}(U ∩ Z, G) = Γ(U, i_!(G)),
```

where `Φ_{U∩Z,U}` denotes the set of parts of `U ∩ Z` that are closed in `U`.

The verification reduces to noting that the left-hand side is a sheaf for `U` variable, i.e. that the property, for a
section of `i_*(G)` on `U` considered as a section of `G` on `U ∩ Z`, of having support closed in `U` is of local nature
on `U`. The sheaf `i_!(G)` just defined is also known under the name: sheaf deduced from `G` by extension by `0` outside
`Z`, cf. [Godement]. In particular, if `Z` is closed, one has

```text
i_!(G) = i_*(G);
```

<!-- label: eq:I.1.9 -->

but in the general case, the canonical injection `i_!(G) → i_*(G)` is not an isomorphism, as is already well known for
`Z` open. Evidently, `i_!(G)` depends functorially on `G` (and is even an exact functor in `G`). This said, one has:

**Proposition.**

<!-- label: I.1.3 -->

There exists an isomorphism of bifunctors in `G`, `F` (`G` an abelian sheaf on `Z`, `F` an abelian sheaf on `X`):

```text
Hom(i_!(G), F) = Hom(G, i^!(F)).
```

<!-- label: eq:I.1.10 -->

To define such an isomorphism, it amounts to the same to define functorial homomorphisms

```text
i_! i^!(F) ⟶ F, G ⟶ i^! i_!(G),
```

satisfying the well-known compatibility conditions (cf. for example Shih's exposé in the Cartan seminar on cohomological
operations).

Recalling that `i_!` is exact, hence transforms monomorphisms into monomorphisms, one concludes:

<!-- original page 10 -->

**Corollary.**

<!-- label: I.1.4 -->

If `F` is injective, `i^!(F)` is injective, hence `ΓZ(F) = i_* i^!(F)` is also injective.

Replacing `X` by a variable open set `U` of `X`, one also concludes from 1.3:

**Corollary.**

<!-- label: I.1.5 -->

One has an isomorphism functorial in `F`, `G`:

```text
ℋom(i_!(G), F) = i_*(ℋom(G, i^!(F))).
```

<!-- label: eq:I.1.11 -->

Taking for `G` the constant sheaf on `Z` defined by `ℤ`, say `ℤ_Z`, 1.3 and 1.5 specialize into

**Corollary.**

<!-- label: I.1.6 -->

One has isomorphisms functorial in `F`:

```text
Γ_Z(F) = Hom(ℤ_{Z,X}, F),
ΓZ(F)  = ℋom(ℤ_{Z,X}, F),
```

<!-- label: eq:I.1.12 -->

where `ℤ_{Z,X} = i_!(ℤ_Z)` is the abelian sheaf on `X` deduced from the constant sheaf on `Z` defined by `ℤ`, by
extension by `0` outside `Z`.

**Remark.**

<!-- label: I.1.7 -->

Suppose that `X` is a ringed space, and equip `Z` with the sheaf of rings `O_Z = i^{−1}(O_X)`; finally, denote by `C_X`
and `C_Z` the category of Modules on `X`, resp. `Z`. Then the preceding considerations extend word for word, taking `F`
to be a Module on `X` and `G` a Module on `Z`, and interpreting accordingly statements 1.3 to 1.6.

To finish these generalities, let us examine what happens when one changes the locally closed part `Z`. Let `Z′ ⊂ Z` be
another locally closed part, and let

```text
j: Z′ ⟶ Z,   i′: Z′ ⟶ X,   i′ = i j
```

<!-- original page 11 -->

be the canonical inclusions. Then one has functorial isomorphisms:

```text
(i j)^! = j^! i^!,   (i j)_! = i_! j_!.
```

<!-- label: eq:I.1.13 -->

The first isomorphism (13) defines a functorial isomorphism

```text
Γ_{Z′}(F) = Γ(Z′, (i j)^!(F)) ≃ Γ(Z′, j^!(i^!(F))) = Γ_{Z′}(i^!(F)).
```

<!-- label: eq:I.1.14 -->

Suppose now that `Z′` is closed in `Z`, and let

```text
Z″ = Z − Z′
```

be its complement in `Z`, which is open in `Z`, hence locally closed in `X`. The canonical inclusion (8′) applied to
`i^!(F)` on `Z` equipped with `Z′` defines, thanks to (14), an injective functorial canonical homomorphism

```text
Γ_{Z′}(F) ⟶ Γ_Z(F).
```

<!-- label: eq:I.1.15 -->

If in (14) one replaces `Z` by `Z″` and uses (8″), one finds a functorial canonical homomorphism:

```text
Γ_Z(F) ⟶ Γ_{Z″}(F).
```

<!-- label: eq:I.1.15′ -->

<!-- original page 12 -->

**Proposition.**

<!-- label: I.1.8 -->

Under the preceding conditions, the sequence of functorial homomorphisms

```text
0 ⟶ Γ_{Z′}(F) ⟶ Γ_Z(F) ⟶ Γ_{Z″}(F)
```

<!-- label: eq:I.1.16 -->

is exact. If `F` is flasque, the sequence remains exact when one puts a zero on the right.

*Proof.* Replacing `X` by an open set `V` in which `Z` is closed, one reduces to the case where `Z` is closed, hence
`Z′` is closed. Then `Z″` is closed in the open set `X − Z′`, and one has a canonical inclusion

```text
Γ_{Z″}(F) ⟶ Γ(X − Z′, F),
```

and the exactness of (16) simply means that the sections of `F` with support in `Z′` are those whose restriction to
`X − Z′` is zero.

When `F` is flasque, every element of `Γ_{Z″}(F)`, considered as a section of `F` on `X − Z′`, can be extended to a
section of `F` on `X`, and the latter will evidently have its support in `Z`, which proves that the last homomorphism in
(16) is then surjective.

**Corollary.**

<!-- label: I.1.9 -->

One has a functorial exact sequence

```text
0 ⟶ ΓZ′(F) ⟶ ΓZ(F) ⟶ ΓZ″(F),
```

<!-- label: eq:I.1.16bis -->

and if `F` is flasque, this sequence remains exact when one puts a `0` on the right.

One may interpret (1.8) in terms of results on the functors `Hom` and `ℋom` via 1.6, in the following way. Let us first
note that if `G` is an abelian sheaf on `Z`, inducing the sheaves `j*(G)` and `k*(G)` on `Z′` resp. `Z″` (where
`j: Z′ → Z` and `k: Z″ → Z` are the canonical injections), one has a canonical exact sequence of sheaves on `X`:

```text
0 ⟶ k*(G)_X ⟶ G_X ⟶ j*(G)_X ⟶ 0,
```

<!-- label: eq:I.1.17 -->

where, to simplify the notation, the subscript `X` designates the sheaf on `X` obtained by extending by `0` in the
complement of the space of definition of the sheaf in question. The exact sequence (17) generalizes a well-known exact
sequence in the case `Z = X` (cf. [Godement]), and is moreover deduced from the latter by writing the exact sequence in
question on `Z`, and applying the functor `i_!`. Taking `G = ℤ_Z`, one concludes in particular:

**Proposition.**

<!-- label: I.1.10 -->

Under the preceding conditions, one has an exact sequence of abelian sheaves on `X`:

```text
0 ⟶ ℤ_{Z″,X} ⟶ ℤ_{Z,X} ⟶ ℤ_{Z′,X} ⟶ 0.
```

<!-- label: eq:I.1.18 -->

This being so, the two exact sequences 1.8 and 1.9 are nothing other than the exact sequences deduced from (18) by
application of the functor `Hom(−, F)` resp. `ℋom(−, F)`.

This gives an evident proof of the fact that the sequences (16) and (16 bis) remain exact when one puts a zero on the
right, provided that `F` is injective.

<!-- original page 13 -->

## 2. The functors `H^*_Z(X, F)` and `ℋ^*_Z(F)`

<!-- label: I.2 -->

**Definition.**

<!-- label: I.2.1 -->

One denotes by `H^*_Z(X, F)` and `ℋ^*_Z(F)` the derived functors in `F` of the functors `Γ_Z(F)` resp. `ΓZ(F)`.

These are cohomological functors, with values in the category of abelian groups resp. in the category of abelian sheaves
on `X`. When `Z` is closed, `H^*_Z(X, F)` is, by definition, nothing other than `H^*_Φ(X, F)` where `Φ` denotes the
family of closed parts of `X` contained in `Z`. When `Z` is open, we shall see that `H^*_Z(X, F)` is nothing other than
`H^*(Z, F) = H^*(Z, F|Z)`, thanks to the following proposition.

**Proposition (Excision Theorem).**

<!-- label: I.2.2 -->

Let `V` be an open part of `X` containing `Z`. Then one has an isomorphism of cohomological functors in `F`:

```text
H^*_Z(X, F) ⟶ H^*_Z(V, F|V).
```

<!-- label: eq:I.2.19 -->

Indeed, one has a functorial isomorphism `Γ^X_Z ≃ Γ^V_Z j^!`, where `j: V → X` is the inclusion, and where `j^!` is thus
the restriction functor (cf. (14)). This last is exact, and transforms injectives into injectives by 1.4, whence the
isomorphism (19) at once.

When `Z` is open, one may take `V = Z` and one finds:

**Corollary.**

<!-- label: I.2.3 -->

Suppose `Z` open; then one has an isomorphism of cohomological functors:

```text
H^*_Z(X, F) = H^*(Z, F).
```

<!-- label: eq:I.2.20 -->

One concludes from isomorphisms 1.6 and from the definitions (cf. [Tôhoku]):

<!-- original page 14 -->

**Proposition.**[^N.D.E-I-2]

<!-- label: I.2.3bis -->

One has isomorphisms of cohomological functors:

```text
H^*_Z(X, F) ≃ Ext^*(X; ℤ_{Z,X}, F),
```

<!-- label: eq:I.2.21 -->

```text
ℋ^*_Z(F) ≃ ℰxt^*(ℤ_{Z,X}, F).
```

<!-- label: eq:I.2.21bis -->

One may therefore apply the results of [Tôhoku] on the `Ext` of Modules. Let us first point out the following
interpretation of the sheaves `ℋ^*_Z(F)` in terms of the global groups `H^*_Z(X, F)`:

**Corollary.**

<!-- label: I.2.4 -->

`ℋ^*_Z(F)` is canonically isomorphic to the sheaf associated to the presheaf

```text
U ⟼ H^*_{Z ∩ U}(U, F|U).
```

In particular, using corollary 2.3, one finds:

**Corollary.**

<!-- label: I.2.5 -->

Suppose `Z` open; then one has an isomorphism of cohomological functors:

```text
ℋ^*_Z(F) = R^* i_* i*(F)
```

<!-- label: eq:I.2.22 -->

(where `i: Z → X` is the inclusion).

The spectral sequence of `Ext` gives the important spectral sequence:

**Theorem.**

<!-- label: I.2.6 -->

One has a spectral sequence functorial in `F`, abutting to `H^*_Z(X, F)` and with initial term

```text
E^{p,q}_2(F) = H^p(X, ℋ^q_Z(F)).
```

<!-- label: eq:I.2.23 -->

**Remarks.**

<!-- label: I.2.7 -->

It follows at once from 2.4 that the sheaves `ℋ^q_Z(F)` are zero in `X − Z`, and also zero in the interior of `Z` for
`q ≠ 0` (so for such a `q`, `ℋ^q_Z(F)` is even supported on the boundary of `Z`).

<!-- original page 15 -->

Consequently, the right-hand side of (23) may be interpreted as a cohomology group on `Z`. We shall use 2.6 in the case
where `Z` is closed in `X`, in which case the right-hand side of (23)[^N.D.E-I-3] may be interpreted as a cohomology
group computed on `Z`:

```text
E^{p,q}_2(F) = H^p(Z, ℋ^q_Z(F)).
```

<!-- label: eq:I.2.23bis -->

Let us also note that when `Z` is open, the spectral sequence 2.6 is nothing other than the Leray spectral sequence for
the continuous map `i: Z → X`, taking into account the interpretation 2.5 in the calculation of the initial term of the
Leray spectral sequence.

Let us return to the exact sequence (18);[^N.D.E-I-4] it gives rise to an exact sequence of `Ext` (cf. [Tôhoku]):

**Theorem.**

<!-- label: I.2.8 -->

Let `Z` be a locally closed part of `X`, `Z′` a closed part of `Z`, and `Z″ = Z − Z′`. Then one has an exact sequence
functorial in `F`:

```text
0 ⟶ H⁰_{Z′}(X, F) ⟶ H⁰_Z(X, F) ⟶ H⁰_{Z″}(X, F) ─∂─→ H¹_{Z′}(X, F) ⟶ H¹_Z(X, F) ...

... H^i_{Z′}(X, F) ⟶ H^i_Z(X, F) ⟶ H^i_{Z″}(X, F) ─∂─→ H^{i+1}_{Z′}(X, F) ...
```

<!-- label: eq:I.2.24 -->

Let us recall how this exact sequence can be obtained. Let `C(F)` be an injective resolution of `F`; then the exact
sequence (18)[^N.D.E-I-5] gives rise to the exact sequence

```text
0 ⟶ Γ_{Z′}(C(F)) ⟶ Γ(C(F)) ⟶ Γ_{Z″}(C(F)) ⟶ 0,
```

<!-- label: eq:I.2.25 -->

(which is nothing other than the one defined in 1.8). One concludes an exact sequence of cohomology, which is nothing
other than (24).

<!-- original page 16 -->

The most important case for us is the one where `Z` is closed (and one can moreover always reduce to it by replacing `X`
by an open set `V` in which `Z` is closed). Then `Z′` is closed, `Z″` is closed in the open set `X − Z′`, and one may
write

```text
H^i_{Z″}(X, F) = H^i_{Z″}(X − Z′, F|_{X−Z′}),
```

<!-- label: eq:I.2.26 -->

which allows us to write the exact sequence (24) in terms of cohomologies with support in a given closed set. The most
frequent case is the one where `Z = X`. Setting then, for simplification, `Z′ = A`, one finds:

**Corollary.**

<!-- label: I.2.9 -->

Let `A` be a closed part of `X`. Then one has an exact sequence functorial in `F`:

```text
0 ⟶ H⁰_A(X, F) ⟶ H⁰(X, F) ⟶ H⁰(X − A, F) ─∂─→ H¹_A(X, F) ...

... H^i_A(X, F) ⟶ H^i(X, F) ⟶ H^i(X − A, F) ─∂─→ H^{i+1}_A(X, F) ...
```

<!-- label: eq:I.2.27 -->

This exact sequence shows that the cohomology group `H^i_A(X, F)` plays the role of a relative cohomology group of `X`
mod `X − A`, with coefficients in `F`. It is on this account that it was introduced naturally in applications. By
"sheafifying" (24) and (27), or by proceeding directly, one finds, taking into account that the sheaf associated to
`U ↦ H^i(U, F)` is zero if `i > 0`:

**Corollary.**

<!-- label: I.2.10 -->

Under the conditions of 2.8, one has an exact sequence functorial in `F`:

```text
... ℋ^i_{Z′}(F) ⟶ ℋ^i_Z(F) ⟶ ℋ^i_{Z″}(F) ─∂─→ ℋ^{i+1}_{Z′}(F) ...
```

<!-- label: eq:I.2.24bis -->

**Corollary.**

<!-- label: I.2.11 -->

Let `A` be a closed part of `X`; then one has an exact sequence functorial in `F`:

```text
0 ⟶ ℋ⁰_A(F) ⟶ F ⟶ f_*(F|_{X−A}) ─∂─→ ℋ¹_A(F) ⟶ 0,
```

<!-- label: eq:I.2.28 -->

and canonical isomorphisms, for `i ⩾ 2`:

```text
ℋ^i_A(F) = ℋ^{i−1}_{X−A}(F) = R^{i−1} f_*(F|_{X−A}),
```

<!-- label: eq:I.2.29 -->

where `f: (X − A) → X` is the inclusion.

This therefore defines `ℋ⁰_A(F)` and `ℋ¹_A(F)` respectively as the kernel and cokernel of the canonical homomorphism

```text
F ⟶ f_* f*(F) = f_*(F|_{X−A}),
```

and the `ℋ^i_A(F)` (`i ⩾ 2`) in terms of the derived functors of `f_*`.

<!-- original page 17 -->

**Corollary.**

<!-- label: I.2.12 -->

Let `F` be an abelian sheaf on `X`. If `F` is flasque, then for every locally closed part `Z` of `X` and every integer
`i ≠ 0`, one has `H^i_Z(X, F) = 0`, `ℋ^i_Z(F) = 0`. Conversely, if for every closed part `Z` of `X` one has
`H¹_Z(X, F) = 0`, then `F` is flasque.

Suppose that `F` is flasque; then `F` induces a flasque sheaf on every open set, so to prove `H^i_Z(X, F) = 0` for
`i > 0`, one may suppose `Z` closed, and then the assertion follows from the exact sequence (27).[^N.D.E-I-6] One
concludes, for every locally closed `Z`, by "sheafifying", i.e. applying 2.4, that `ℋ^i_Z(F) = 0` for `i > 0`.
Conversely, suppose `H¹_Z(X, F) = 0` for every closed `Z`; then the exact sequence (27)[^N.D.E-I-7] shows that for every
such `Z`, `H⁰(X, F) → H⁰(X − Z, F)` is surjective, which means that `F` is flasque.

Combining 2.6 and 2.8, we shall deduce from them:

**Proposition.**

<!-- label: I.2.13 -->

Let `F` be an abelian sheaf on `X`, `Z` a closed part of `X`, `U = X − Z`, `N` an integer. The following conditions are
equivalent:

(i) `ℋ^i_Z(F) = 0` for `i ⩽ N`.

(ii) For every open set `V` of `X`, considering the canonical homomorphism

```text
H^i(V, F) ⟶ H^i(V ∩ U, F),
```

this homomorphism is:

a) bijective for `i < N`,

b) injective for `i = N`.

(When `N > 0`, one may in (ii) restrict to requiring a)).

To prove (i) ⇒ (ii), one is reduced, thanks to the local nature of the `ℋ^i_Z(F)`, to proving the

**Corollary.**

<!-- label: I.2.14 -->

If condition 2.13 (i) is satisfied, then

```text
H^i(X, F) ⟶ H^i(U, F)
```

is bijective for `i < N`, injective for `i = N`.

Indeed, by virtue of the exact sequence (27), this also means `H^i_Z(X, F) = 0` for `i ⩽ N`, and this relation is an
immediate consequence of the spectral sequence (23 bis).[^N.D.E-I-8]

<!-- original page 18 -->

Conversely, hypothesis 2.13 (ii) means that for every open set `V` of `X`, one has

```text
H^i_{Z ∩ V}(V, F|V) = 0 for i ⩽ N,
```

which implies 2.13 (i) thanks to 2.4. If moreover `N > 0`, hypothesis b) is superfluous. Indeed, if `N = 1`, hypothesis
a) and (28) ensure the vanishing of `ℋ^i_Z(F) = 0` for `i ⩽ N`. If `N > 1`, hypothesis a) for `i = N − 1 > 0` and (29)
ensure the vanishing of `ℋ^i_Z(F)` for `i ⩽ N`.

Taking 2.11 into account, this further proves 2.13 (i)...

**Remark.**

Let `Y → X` be a closed immersion, and suppose that locally it is of the form `{0} × Y ⊂ ℝⁿ × Y`. Suppose that `F` is a
locally constant sheaf on `X`; then one finds

```text
ℋ^i_Y(F) ≃ { 0            if i ≠ n,
           { F ⊗ T_{Y,X}   if i = n,    where  T_{Y,X} ≃ ℋ^n_Y(ℤ_X)
```

<!-- label: eq:I.2.30 -->

is a sheaf, extension to `X` of a sheaf on `Y` locally isomorphic to `ℤ_Y`, called the "normal orientation sheaf of `Y`
in `X`".

Using the spectral sequence (23 bis),[^N.D.E-I-9] one finds in this case:

```text
H^i_Y(X, F) ≃ H^{i−n}(Y, F ⊗ T_{Y,X}),
```

<!-- label: eq:I.2.31 -->

and one recovers the "Gysin homomorphism":

```text
H^j(Y, F ⊗ T_{Y,X}) ⟶ H^{j+n}(X, F).
```

<!-- label: eq:I.2.32 -->

## Bibliography

<!-- label: I.bibliography -->

**[Godement]** R. Godement — *Topologie algébrique et théorie des faisceaux*, Act. Scient. et Ind., vol. 1252, Hermann,
Paris.

**[Tôhoku]** A. Grothendieck — "Sur quelques points d'algèbre homologique", *Tôhoku Math. J.* **9** (1957), pp. 119–221.

## Footnotes

<!--
LEDGER DELTA (Exposé I):
| French | English | Note |
| sous-faisceau | subsheaf | Standard. |
| extension par 0 (en dehors de Z) | extension by 0 (outside Z) | Standard for `j_!` constructions. |
| théorème d'excision | Excision Theorem | Stated as proposition in source, but the parenthetical name is preserved. |
| faisceau d'orientation normale | normal orientation sheaf | The "T_{Y,X}" of the closing remark. |
| famille de supports | family of supports | Cartan terminology, kept verbatim. |
| à support dans Z | with support in Z | Standard. |
| faisceautiser | "sheafify" | Kept in quotation marks as in the original (Grothendieck-era coinage). |
| par abus de langage | by abuse of language | Standard. |
| à valeurs dans | with values in | Standard. |
| aboutissement (d'une suite spectrale) | abutment (of a spectral sequence) | Per glossary. |
| terme initial | initial term | Per glossary. |
-->

[^N.D.E-I-1]: *N.D.E.* The original reference was (8).

[^N.D.E-I-2]: *N.D.E.* The proposition bears the number 2.3 in the original edition.

[^N.D.E-I-3]: *N.D.E.* The equation was numbered (23) in the original edition.

[^N.D.E-I-4]: *N.D.E.* The original reference was (1.10).

[^N.D.E-I-5]: *N.D.E.* See preceding note.

[^N.D.E-I-6]: *N.D.E.* The original reference was (2.9).

[^N.D.E-I-7]: *N.D.E.* The original reference was (2.9).

[^N.D.E-I-8]: *N.D.E.* See preceding note.

[^N.D.E-I-9]: *N.D.E.* The original reference was 2.6.
