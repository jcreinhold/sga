# Exposé IV. Dualizing modules and dualizing functors

<!-- label: IV -->

<!-- original page 43 -->

## 1. Generalities on module functors

<!-- label: IV.1 -->

Let

- `A` be a commutative noetherian ring,
- `C` the category of `A`-modules of finite type,
- `C′` the category of arbitrary `A`-modules,
- `Ab` the category of abelian groups.

The aim of this section is the study of certain properties of functors `T : C° → Ab` (assumed additive). Here `C°`
denotes the opposite category of `C`.

Note that if `M ∈ Ob C`, then `T(M)` may be canonically endowed with a structure of `A`-module, defined as follows: if
`f_M` is the homothety of `M` associated to `f ∈ A`, then `A` acts on `T(M)` by `f_{T(M)}`. In other words, `T` factors
as

```text
                         T
        C°  ───────────────────────────►  Ab
           \                            ↗
            \                        /
         T°  \                  /
              \              /
               ▼          /
                  C′
```

where `C′ → Ab` is the canonical functor. In what follows, `T(M)` will always be considered as endowed with this
`A`-module structure.

<!-- TRANSLATOR NOTE: source diagram is ASCII art with @@/~~~ glyphs; rendered above as a labeled commutative
triangle. -->

Composing with the isomorphism `M ⥲ Hom_A(A, M)` the morphism `Hom_A(A, M) → Hom_A(T(M), T(A))`, one obtains the
following morphisms, each deduced from the other in an obvious way:

```text
M ⟶ Hom_A(T(M), T(A)),
M × T(M) ⟶ T(A),
T(M) ⟶ Hom_A(M, T(A)),
```

and this defines a morphism `φ_T` of contravariant functors:

```text
φ_T : T ⟶ Hom_A(−, T(A)).
```

<!-- original page 44 -->

**Proposition.**

<!-- label: IV.1.1 -->

The following two properties are equivalent:

1. `φ_T` is an isomorphism of functors.
1. `T` is left exact.

The implication (i) ⇒ (ii) is trivial.

The implication (ii) ⇒ (i) follows from the fact that, for a morphism `u : F → F′` of two additive left exact functors
`F` and `F′` from `C°` to `Ab`, if `u(A)` is an isomorphism, then `u` is an isomorphism (one uses the fact that `A` is
noetherian, hence that every `A`-module of finite type is of finite presentation).

**Remark.**

<!-- label: IV.1.2 -->

This shows in particular that the representable functors `T : C′° → Ab` are precisely those that commute with arbitrary
inverse limits (over a preordered set, not necessarily filtered).

If `Hom(C°, Ab)_g` denotes the full subcategory of `Hom(C°, Ab)` whose objects are the left exact functors, one has
proved the equivalence of categories

```text
C′ ⥲ Hom(C°, Ab)_g
```

via the quasi-inverse functors

```text
H ↦ Hom_A(−, H)
```

and

```text
T ↦ T(A).
```

Now let `J` be an ideal of `A`, let `Y = V(J) ⊂ Spec A`, and denote by `C_Y` the full subcategory of `C` whose objects
are the `A`-modules `M` of finite type such that `Supp M ⊂ Y`. One has

```text
C_Y = ⋃_n C^{(n)},
```

where `C^{(n)}` is the full subcategory of `C_Y` consisting of the modules `M` such that `J^n M = 0`.

<!-- original page 45 -->

**Proposition.**

<!-- label: IV.1.3 -->

With the same notation as above, let `T : C_Y° → Ab` be a functor. To `H = lim_→ T(A/J^n)`[^N.D.E-IV-1] is associated a
natural morphism

```text
φ_T : T ⟶ Hom_A(−, H),
```

and the following conditions are equivalent:

1. `φ_T` is an isomorphism.
1. The functor `T` is left exact.

*Proof.* — a) *Definition of* `φ_T`.

Let `M ∈ Ob C_Y`. There exists an integer `n` such that `J^n M = 0`. Then `M` is an `A/J^n`-module, and if `T_n` denotes
the restriction of `T` to `C^{(n)}`, one knows how to define the morphism

```text
T_n ⟶ Hom_A(−, H_n),    where H_n = T(A/J^n);
```

<!-- original page 46 -->

whence

```text
T(M) = T_n(M) ⟶ Hom_A(M, lim_→ H_n) = Hom_A(M, H)
```

and

```text
φ_T : T ⟶ Hom_A(−, H).
```

b) *Equivalence of (i) and (ii).*

It is clear that (i) implies (ii). Suppose (ii) holds and let `M ∈ Ob C^{(n)}`. We have seen that
`T_n(M) ⥲ Hom_A(M, H_n)`; hence for every integer `n′ > n` one has

```text
T(M) = T_n(M) = T_{n′}(M) = lim_→ T_n(M),
```

and

```text
T(M) = lim_→ Hom_A(M, H_n).
```

Since these are filtered direct limits, one also has the isomorphism

```text
lim_→ Hom_A(M, H_n) ⥲ Hom_A(M, lim_→ H_n) = Hom_A(M, H).
```

If `C′_Y` denotes the category of `A`-modules with support contained in `Y`, but not necessarily of finite type, one
again has the natural equivalence of categories

```text
C′_Y ⥲ Hom(C_Y°, Ab)_g.
```

*Application.* — With the same notation, let

```text
T^• : C_Y° ⟶ Ab
```

be an exact `∂`-functor. For every `i ∈ ℤ`, set `H^i_n = T^i(A/J^n)` and `H^i = lim_→ H^i_n`.

**Theorem.**

<!-- label: IV.1.4 -->

Let `n ∈ ℤ`. If there exists `i₀ ∈ ℤ` such that `T^i = 0` for every `i < i₀`, then the following three conditions are
equivalent:

1. `T^i = 0` for every `i < n`.
1. `H^i = 0` for every `i < n`.
1. There exists a module `M₀` in `C_Y` such that `Supp M₀ = Y` and `T^i(M₀) = 0` for every `i < n`.

*Proof.* — It is evident that (i) implies (ii) and (iii) (take `M₀ = A/J`).

We show by induction on `n` that (ii) implies (i). It is true for `n = i₀`; suppose it has been proved up to rank `n`.
Suppose then that `H^i = 0` for every `i < n + 1`; by the induction hypothesis one has `T^i = 0` for `i < n`, but
`T^{n−1} = 0` implies that `T^n` is a left exact functor, and

```text
T^n ⥲ Hom_A(−, H^n) = 0.
```

We now show that (iii) implies (ii). It is again true for `n = i₀`; suppose it has been proved up to rank `n`. Let `M₀`
be an `A`-module in `C_Y` such that `Supp M₀ = Y` and `T^i(M₀) = 0` for every `i < n + 1`; by the induction hypothesis
one then has `H^i = 0` for every `i < n`; it remains to show that `H^n = 0`. But "`H^i = 0` for every `i < n`" implies
that `T^{n−1} = 0`, and therefore that `T^n ⥲ Hom_A(−, H^n)`. One then has

<!-- original page 47 -->

```text
Ass H^n = Ass Hom(M₀, H^n) = Supp M₀ ∩ Ass H^n = Ass H^n,
```

since

```text
Ass H^n ⊂ Supp H^n ⊂ Y = Supp M₀.
```

Hence `T^n(M₀) = 0 ⇔ Ass H^n = ∅ ⇔ H^n = 0`; this completes the proof.

## 2. Characterization of exact functors

<!-- label: IV.2 -->

The ring `A` is still assumed noetherian and commutative. The notation is that of Proposition 1.3:

```text
Y = V(J),    T : C_Y° ⟶ Ab,    H = lim_→ T(A/J^n),
```

where we assume that `T` is a left exact functor, whence

```text
T(M) ⥲ Hom_A(M, H).
```

**Proposition.**

<!-- label: IV.2.1 -->

The following properties are equivalent:

1. The functor `T` is exact.
1. `H` is injective in `C′`.

*Proof.* — It clearly suffices to show that (i) implies (ii), that is, to prove that if the restriction to `C_Y` of the
functor `Hom_A(−, H)` is an exact functor, then `H` is injective. But since `A` is noetherian, in order to show that `H`
is injective it suffices to prove that every homomorphism `f : N → H` whose source is an `A`-module `N` of finite type,
a submodule of an `A`-module `M` of finite type, extends to a homomorphism `f̄ : M → H`.

The definition of `H` and the fact that `N` is of finite type imply that there exists an integer `n` such that
`J^n · f(N) = 0`. Endow `M` and `N` with the `J`-adic topology. The `J`-adic topology of `N` is equivalent to the
topology induced by the `J`-adic topology of `M` (Krull's theorem). There therefore exists `V = J^k · M` such that

```text
U = V ∩ N ⊂ J^n N.
```

One then has the factorization

```text
N ──────────► N/U
 \           /
  \         /
 f \       / u
    \     /
     ▼   ▼
       H
```

<!-- original page 48 -->

with `N/U` and `M/V` in `C_Y`. The hypothesis therefore allows one to extend `u` to `ū`:

```text
N/U ──────────► M/V
   \           /
    \         /
   u \       / ū
      \     /
       ▼   ▼
         H
```

and `M → M/V → H` gives the desired extension `f̄`.

**Corollary.**

<!-- label: IV.2.2 -->

Let `K` be an injective `A`-module. Then the submodule `H⁰_J(K)` of `K` consisting of the elements annihilated by some
power of `J` is injective.

*Proof.* — It suffices to verify that the restriction to `C_Y` of the functor `Hom_A(−, H⁰_J(K))` is exact. Now let
`M ∈ Ob C_Y`; there exists `k` such that `J^k · M = 0`, and the inclusion

```text
Hom_A(−, H⁰_J(K)) ⟶ Hom_A(M, K)
```

is then an isomorphism. The result follows, since `Hom_A(−, K)` is exact.

## 3. Study of the case where T is left exact and T(M) is of finite type for every M

<!-- label: IV.3 -->

Let, as above,

```text
T : C_Y° ⟶ Ab;
```

we now assume that `T` is left exact and that one has the factorization

```text
                         T
        C_Y°  ─────────────────────────►  Ab
            \                          ↗
             \                       /
              \                    /
               ▼                 /
                    C_Y
```

where, as above, `C_Y → Ab` is the forgetful functor. One can therefore define `T(T(M)) = T ∘ T(M)`, and the canonical
morphism

```text
M ⟶ Hom_A(Hom_A(M, H), H)
```

defines a morphism

```text
M ⟶ T ∘ T(M).
```

<!-- original page 49 -->

**Proposition.**

<!-- label: IV.3.1 -->

The ring `A` being still assumed noetherian, if one makes the additional hypothesis that `A/J` is artinian, the
following conditions are equivalent:

1. `T` is left exact and, for every `M ∈ Ob C_Y`, `T(M)` is of finite type and `M → T ∘ T(M)` is an isomorphism.
1. `T` is exact and, for every residue field `k` associated to a maximal ideal containing `J`, one has `T(k) ⥲ k`.
1. One has `T ⥲ Hom_A(−, H)` with `H` injective, and, for every `k` as in (ii), one has `Hom_A(k, H) ⥲ k`.
1. `T` is exact and, for every `M ∈ Ob C_Y`, one has `long T(M) = long M`.

*Proof.* — We have already shown the equivalence of (ii) and (iii) (Prop. 2.1).

Let us show that (ii) implies (iv): first, if `M ∈ Ob C_Y`, then since `M` is an `A/J^n`-module with `A/J^n` artinian,
`long M` is finite. We argue by induction on the length of `M`. Condition (iv) holds when `long M = 1`, because then `M`
is a residue field falling under (ii). If `long M > 1`, there exists a submodule `M′` of `M` with `M′ ≠ 0` and
`long M′ < long M`. Form the exact sequence

```text
0 ⟶ M′ ⟶ M ⟶ M′′ ⟶ 0.
```

Since `T` is exact, one has the sequence

```text
0 ⟶ T(M′) ⟶ T(M) ⟶ T(M′′) ⟶ 0,
```

and `long T(M) = long T(M′) + long T(M′′) = long M′ + long M′′ = long M`.

(ii) ⇒ (i): Since (ii) implies (iv), let `M` be an `A`-module in `C_Y`; one has `long T(M) = long M`, hence `T(M)` is of
finite length and therefore of finite type.

It remains to show that `M → T ∘ T(M)` is an isomorphism; we again argue by induction on `long M`. For `M = k` it is
true. In the general case, write the commutative diagram with exact rows

<!-- original page 50 -->

```text
0 ⟶  M′  ⟶  M  ⟶  M′′ ⟶ 0
      ↓        ↓       ↓
0 ⟶ T∘T(M′) ⟶ T∘T(M) ⟶ T∘T(M′′) ⟶ 0,
```

where `M′` is a submodule of `M` with `M′ ≠ 0` and `long M′ < long M`. By the induction hypothesis the outer arrows are
isomorphisms, hence

```text
M ⟶ T ∘ T(M)
```

is an isomorphism.

(i) ⇒ (ii): Let

```text
0 ⟶ M′ ⟶ M ⟶ M′′ ⟶ 0
```

be an exact sequence of `A`-modules in `C_Y`, and let `Q` be the cokernel of `T(M) → T(M′)`. Applying `T` to the exact
sequence

```text
0 ⟶ T(M′) ⟶ T(M) ⟶ T(M′′) ⟶ Q ⟶ 0,
```

one obtains

```text
0 ⟶ T(Q) ⟶ T∘T(M′) ⟶ T∘T(M)
                ↑          ↑
                ≅          ≅
                M′    ⟶    M
```

hence `T(Q) = 0` and `Q ⥲ T(T(Q)) = 0`.

<!-- original page 51 -->

On the other hand, let `k` be a residue field, `k = A/𝔪`, `J ⊂ 𝔪`. One must show that `T(k) ⥲ k`. For this it suffices
to note that `T(k)` is a `k`-vector space. One then deduces

```text
T(k) ≃ k ⊕ V,
T(T(k)) ≃ T(k) ⊕ T(V) ≃ k ⊕ V ⊕ T(V) ≃ k,
```

whence `V = 0`.

Finally, let us show that (iv) implies (iii): it suffices to show that `T(k) ⥲ k`. Now `long T(k) = long k = 1`, so
`T(k) = k′` is a residue field, and `Supp k′ = Supp Hom_A(k, H) ⊂ Supp k`. Hence `k ≃ k′`.

**Remark.**

<!-- label: IV.3.2 -->

One can show that condition (iv) is equivalent to the condition

(iv)′ For every `M ∈ Ob C_Y`, one has `long T(M) = long M`.

## 4. Dualizing module; dualizing functor

<!-- label: IV.4 -->

**Definition.**

<!-- label: IV.4.1 -->

Let `A` be a noetherian local ring with maximal ideal `𝔪`. A *dualizing functor* for `A` is any functor

```text
T : C_𝔪° ⟶ Ab,
```

where we write `C_𝔪` in place of `C_Y` for `Y = V(𝔪)`, which satisfies the equivalent conditions of Proposition 3.1. An
`A`-module `I` is said to be *dualizing* for `A` if the functor `M ↦ Hom_A(M, I)` is dualizing.

Definition 4.1 can be generalized to the case where `A` is no longer assumed to be a local ring.

**Definition.**

<!-- label: IV.4.2 -->

Let `A` be a noetherian ring, and let `C̄` be the full subcategory of `C` consisting of the `A`-modules of finite
length. A *dualizing functor* is any `A`-linear functor `T` from `C̄°` to `C̄` which is exact and such that the morphism
of functors

```text
id ⟶ T ∘ T
```

is an isomorphism.

We will prove an existence theorem and also that the module `I` representing such a functor is locally artinian. We will
likewise show that, for every maximal ideal `𝔪` of `A`, the `𝔪`-primary component of the socle of `I` is of length 1.

**Proposition.**

<!-- label: IV.4.3 -->

Let `A` and `B` be two noetherian local rings with maximal ideals `𝔪_A` and `𝔪_B`, such that `B` is a finite
`A`-algebra. Then, if `I` is a dualizing module for `A`, `Hom_A(B, I)` is a dualizing module for `B`.

<!-- original page 52 -->

*Proof.* — Let

```text
R : C_{𝔪_B} ⟶ C_{𝔪_A}
```

be the restriction-of-scalars functor; it is exact. Let `T` be a dualizing functor for `A`,

```text
T : C_{𝔪_A} ⟶ Ab;
```

it is exact and, for every `M ∈ Ob C_{𝔪_A}`, the natural morphism `M → T ∘ T(M)` is an isomorphism; hence `T ∘ R` is a
dualizing functor for `B`. If `I` represents `T`, then by the classical formula `Hom_A(M, I) = Hom_B(M, Hom_A(B, I))`,
valid for every `B`-module `M`, we deduce that `Hom_A(B, I)` is a dualizing module for `B`.

**Corollary.**

<!-- label: IV.4.4 -->

Let `A` be a noetherian local ring and `𝔞` an ideal of `A`; set `B = A/𝔞`. If `I` is a dualizing module for `A`, then
the annihilator of `𝔞` in `I` is a dualizing module for `B`.

**Lemma.**

<!-- label: IV.4.5 -->

Let `A` be a noetherian local ring and `I` a locally artinian `A`-module. There is a canonical isomorphism

```text
I ⥲ Î = I ⊗_A Â.
```

*Proof.* — Let `I_n` denote the annihilator of `𝔪^n` in `I`, where `𝔪` is the maximal ideal of `A`. To say that `I` is
locally artinian is to say that `I` is the direct limit of the `I_n` and that these are of finite length. Now the tensor
product commutes with direct limits, so one is reduced to the case where `I` is artinian. In this case `I` is
annihilated by some power of the maximal ideal, say `𝔪^k`; therefore for `p ⩾ k` one has `I ⥲ I ⊗_A A/𝔪^p`, and hence
`I ⥲ I ⊗_A Â`, since `A` is noetherian and `I` is of finite type.

It follows that the restriction-of-scalars functor from `Â` to `A` and the extension-of-scalars functor induce
quasi-inverse equivalences between the category of locally artinian `Â`-modules and the category of locally artinian
`A`-modules.

<!-- original page 53 -->

**Proposition.**

<!-- label: IV.4.6 -->

Let `A` be a noetherian local ring, `Â` its completion, and `I` a dualizing module for `A` (resp. for `Â`). Let `J` be
the completion[^N.D.E-IV-2] of `I` (resp. the `A`-module obtained by restriction of scalars). Then `J` is a dualizing
module for `Â` (resp. for `A`). Moreover, the underlying abelian groups of `I` and `J` are isomorphic.

*Proof.* — One simply observes that the equivalence between the category of locally artinian `A`-modules and the
category of locally artinian `Â`-modules induces an isomorphism between the bifunctors `Hom_A(−, −)` and
`Hom_{Â}(−, −)`, and that the characterization of a dualizing functor or a dualizing module involves only these
bifunctors.

**Theorem.**

<!-- label: IV.4.7 -->

Let `A` be a noetherian local ring.

a) There always exists a dualizing module `I`.

b) Two dualizing modules are isomorphic (by a non-canonical isomorphism).

c) For a module `I` to be dualizing, it is necessary and sufficient that it be an injective envelope of the residue
field `k` of `A`.

**Remark.**

<!-- label: IV.4.8 -->

Proposition 4.6 reduces the proof to the case of a complete noetherian local ring. By a structure theorem of
Cohen,[^N.D.E-IV-3] such a ring is a quotient of a regular ring. Proposition 4.3 then allows one to assume `A` regular.
As we shall see later, this remark permits an explicit computation of the dualizing module;[^IV-4-1] nevertheless we
will prove Theorem 4.7 by other means.

*Recollections.* — Before proving the theorem, we make a few recollections on the notion of injective envelope. Cf.
Gabriel, *Thèse*, Paris 1961, *Des Catégories Abéliennes*, ch. II § 5.

<!-- original page 54 -->

Let `𝒞` be an abelian category in which direct limits exist and are exact[^N.D.E-IV-4] (e.g. `𝒞 =` the category of
modules). Every object `M` embeds in an injective object, and one calls *injective envelope* of `M` any minimal
injective object containing `M`. One has the following properties:

(i) Every object `M` has an injective envelope `I`.

(ii) If `I` and `J` are two injective envelopes of `M`, there exists between `I` and `J` an isomorphism (in general not
unique) inducing the identity on `M`.

(iii) `I` is an essential extension of `M`, that is to say `P ⊂ I` and `P ∩ M = {0}` imply `P = {0}`. Moreover, if `I`
is injective and an essential extension of `M`, then `I` is an injective envelope of `M`.

Granting these results, to prove Theorem 4.7 it suffices to prove c).

*Proof.* — Let `I` be a dualizing module for `A`. Then `I` is injective and `Hom_A(k, I)` is isomorphic to `k`.
Composing the isomorphism `k ≃ Hom_A(k, I)` with the inclusion

```text
Hom_A(k, I) ↪ Hom_A(A, I) ≃ I,
```

one obtains the inclusion

```text
k ↪ I.
```

Let us show that `I` is an injective envelope of `k`. Let `J` be an injective module such that

```text
k ⊂ J ⊂ I.
```

Since `J` is injective, there exists an injective `A`-submodule `J′` of `I` such that `I = J ⊕ J′`. We show that
`Hom_A(k, J′) = 0`. One has

```text
Hom_A(k, I) ≃ Hom_A(k, J) ⊕ Hom_A(k, J′);
```

<!-- original page 55 -->

`Hom_A(k, J)` is a vector subspace of `Hom_A(k, I) ≃ k` not reduced to zero (since it contains the inclusion `k ⊂ J`),
so `Hom_A(k, J) ≃ k`, and consequently `Hom_A(k, J′) = 0`.

Arguing by induction on the length, one deduces that `Hom_A(M, J′) = 0` for every `A`-module `M` of finite length; since
`I` is the direct limit of the modules `Hom(A/𝔪^n, I)` (cf. Proposition 1.3), which are of finite length by hypothesis,
the projection `I → J′` is zero, and consequently `J′ = 0`.

Conversely, let `I` be an injective envelope of `k`. To see that `I` is a dualizing module, it suffices, by 2.1 and 3.1
(ii), to show that `V = Hom_A(k, I)` is isomorphic to `k`. Now one has the double inclusion

```text
k ⊂ V ⊂ I;
```

`V` is a vector space over `k` that decomposes as the direct sum of `k` and a vector subspace `V′` of `I` such that
`V′ ∩ k = 0`. Now `I` is an essential extension of `k`, hence `V′ = 0` and `V = k`.

**Corollary.**

<!-- label: IV.4.9 -->

Let `A` be a noetherian local ring; every dualizing module for `A` is locally artinian.

*Proof.* — Let `I` be a dualizing module; it is an injective envelope of `k`. Using the notation and the result of
Corollary 2.2, one has

```text
k ⊂ H⁰_𝔪(I) ⊂ I,
```

and `H⁰_𝔪(I)` is injective. One deduces that `I = H⁰_𝔪(I)`, and hence that `I` is locally artinian.[^N.D.E-IV-5]

## 5. Consequences of the theory of dualizing modules

<!-- label: IV.5 -->

<!-- original page 56 -->

The functor

```text
T = Hom_A(−, I) : C_𝔪 ⟶ C_𝔪
```

is an anti-equivalence. Indeed, `T ∘ T` is isomorphic to the identity functor, and the argument is formal from there.

One deduces the usual properties of the notion of orthogonality:

Let `M* = Hom_A(M, I) = T(M)`, and let `N ⊂ M` be a submodule. Define the *orthogonal* of `N` to be the submodule `N′`
of `M*` consisting of the elements of `M*` that vanish on `N`. One thereby obtains a bijection between the set of
submodules of `M` and the set of submodules of `M*`, which reverses the order.

In particular:

- `long_M N = colong_{M*} N′`.
- The monogenic modules, i.e. those such that `M/𝔪M` is of dimension 0 or 1, correspond under duality to the modules
    whose socle is of length 0 or 1.
- If `A` is artinian, the ideals of `A` correspond to the submodules of `I`.

and so on.

Let `A` be a noetherian local ring, let `𝒟_A` be the category of `A`-modules `M` such that, for every `n ∈ ℕ`,
`M_(n) = M/𝔪^{n+1}M` is of finite length and such that `M = lim_← M_(n)`, and let `Â` be the completion of `A`. The
restriction-of-scalars functor and the completion functor are quasi-inverse equivalences between `𝒟_A` and `𝒟_{Â}`,
which commute up to isomorphism with the formation of the underlying abelian groups of the modules considered. Let `𝒞_A`
denote the category of locally artinian `A`-modules with socle of finite dimension.

**Proposition.**

<!-- label: IV.5.1 -->

Let `A` be a noetherian local ring and let `I` be a dualizing module for `A`. The functors

```text
Hom_A(−, I) : (𝒞_A)° ⟶ 𝒟_A
```

and

```text
Hom_{Â}(−, I) : 𝒟_A ⟶ (𝒞_A)°
```

are equivalences of categories, quasi-inverse to one another.

Moreover, if one transports these functors via the equivalences of categories between `𝒟_A` and `𝒟_{Â}` on the one hand,
and `𝒞_A` and `𝒞_{Â}` on the other, one finds the functor `Hom_{Â}(−, I)`.

<!-- original page 57 -->

*Proof.* — Let `X ∈ Ob 𝒞_A`. By definition,

```text
X = lim_→ X_k,    X_k = Hom_A(A/𝔪^{k+1}, X),
                  k ∈ ℕ
```

so

```text
Hom_A(X, I) = lim_← Hom_A(X_k, I).
```

Therefore `Y = lim_← X_k` is an `Â`-module of finite type, as follows from EGA 0_I 7.2.9. We note in this connection
that `𝒟_A` is also the category of `Â`-modules of finite type, or, if one prefers, that `𝒟_A` is the category of
complete `A`-modules of finite type over `Â`. Let then `Y` be such a module, and let `f : Y → I` be an `Â`-homomorphism.
The image of `f` is a submodule of finite type, hence is annihilated by `𝔪^k` for some `k`; indeed every `x ∈ I` is
annihilated by a power of `𝔪`. So `f` factors through `Y/𝔪^k Y`, whence it follows that

```text
Hom_{Â}(Y, I) = lim_→ Hom_{Â}(Y_(k), I)    with Y_(k) = Y/𝔪^{k+1}Y
                  k

              = lim_→ (Y_(k))*
                  k
```

belongs to `Ob 𝒞_A`. It then follows immediately that the two functors of the statement are quasi-inverse to one
another.

<!-- original page 58 -->

It follows from the foregoing that neither the categories nor the functors under consideration, nor the underlying
abelian groups of the modules considered, are changed by replacing `A` by `Â`; Proposition 5.1 then states as follows:

The restriction of the functor `Hom_{Â}(−, I)` to the category of `Â`-modules of finite type takes its values in the
category of locally artinian `Â`-modules with socle of finite dimension, and admits a quasi-inverse functor, which is
the restriction of the functor `Hom_{Â}(−, I)`. On the intersection of these two categories these two functors coincide
(obviously!) and establish an auto-duality of the category of `Â`-modules of finite length.

**Example** (Macaulay).

<!-- label: IV.5.2 -->

Let `A` be a local ring with residue field `k`. Let `k₀` be a subfield of `A` such that `k` is finite over `k₀`, with
`[k : k₀] = d`. Every `A`-module of finite length can be viewed as a `k₀`-vector space of finite dimension equal to
`d · long(M)`. The functor `T`:

```text
M ⟶ Hom_{k₀}(M, k₀)
```

is then exact and preserves length, hence is dualizing for `A`. The associated dualizing module is therefore

```text
A′ = lim_→ Hom_{k₀}(A/𝔪^n, k₀),
       n
```

the topological dual of `A` endowed with the `𝔪`-adic topology.

**Example.**

<!-- label: IV.5.3 -->

Let `A` be a regular noetherian local ring of dimension `n`. Let `𝔪` be its maximal ideal and `k` its residue field.
There exists a regular system of parameters `(x₁, x₂, …, x_n)` that generates `𝔪` and that is an `A`-regular sequence.
One can therefore compute the `Ext^i_A(k, A)` by the Koszul complex; one finds

```text
Ext^i_A(k, A) = 0    if i ≠ n,
Ext^n_A(k, A) ≃ k.
```

<!-- original page 59 -->

The depth of `A` being `n`, for every `M` annihilated by a power of `𝔪`, `Ext^i_A(M, A) = 0` if `i < n`; furthermore
`Ext^i_A(M, A) = 0` if `i > n`, since the global cohomological dimension of `A` is equal to `n`. Hence `Ext^n_A(−, A)`
is exact, and moreover `Ext^n_A(k, A) ≃ k`; it follows that:

**Proposition.**

<!-- label: IV.5.4 -->

If `A` is a regular noetherian local ring of dimension `n`, the functor

```text
M ⟶ Ext^n_A(M, A)
```

is dualizing. The associated dualizing module is

```text
I = lim_→ Ext^n_A(A/𝔪^r, A);
      r
```

it is isomorphic to `H^n_𝔪(A)` (Exposé II, Th. 6).[^IV-5-1]

**Remark.**

<!-- label: IV.5.5 -->

If `A` satisfies the hypotheses of both preceding examples, the two dualizing modules so obtained are isomorphic.
Suppose for example that `A` is regular of dimension `n`, complete, and of equal characteristic. There then exists a
field of representatives, say `K`. If one chooses a system of parameters `(x₁, …, x_n)` of `A`, one can construct an
isomorphism between `A` and the ring of formal power series `K[[T₁, …, T_n]]`; whence, as we shall now see, an explicit
isomorphism between the two dualizing modules

```text
v : H^n_𝔪(A) ⟶ A′.
```

One can find an intrinsic interpretation of this isomorphism using the module `Ω^n = Ω^n(A/K)` of completed relative
differentials of maximal degree. Indeed, it is known that `Ω^n` admits a basis consisting of the element
`dx₁ ∧ dx₂ ⋯ ∧ dx_n`. Whence an isomorphism

```text
u : H^n_𝔪(Ω^n) ⟶ H^n_𝔪(A).
```

A remarkable fact is then that the composite

```text
vu = w : H^n_𝔪(Ω^n) ⟶ A′
```

does not depend on the choice of system of parameters and commutes with change of base field.

<!-- original page 60 -->

To construct `v`, one computes `H^n_𝔪(A)` using the Koszul complex associated to the `x_i`; one finds

```text
H^n_𝔪(A) = lim_→ A/(x₁^r, …, x_n^r);
            r
```

where the transition morphisms are defined as follows: set `I_r = A/(x₁^r, …, x_n^r)`; let `e^r_{a₁,…,a_n}` denote the
image of `x₁^{a₁} x₂^{a₂} ⋯ x_n^{a_n}` in `I_r`. The `e^r_{a₁,…,a_n}`, for `0 ⩽ a_i < r`, form a basis of `I_r`.

That said, if `s` is an integer, the transition morphism

```text
t_{r, r+s} : I_r ⟶ I_{r+s}
```

is multiplication by `x₁^s x₂^s ⋯ x_n^s`, so

```text
u_{r, r+s}(e^r_{a₁,…,a_n}) = e^{r+s}_{a₁+s, …, a_n+s}.
```

Note that giving an `A`-homomorphism `w` from an `A`-module `M` to `A′` is equivalent to giving a `K`-linear form
`w′ : M → K` that is continuous on submodules of finite type. In the case `M = H^n_𝔪(Ω^n)`, the definition of `w` is
therefore equivalent to that of a linear form

```text
ρ : H^n_𝔪(Ω^n) ⟶ K,
```

called the *residue form*.[^IV-5-2] To construct `ρ`, it suffices to define forms `ρ_r : I_r → K` that fit together, and
one will take

```text
ρ_r(e^r_{a₁,…,a_n}) =
    1   if a_i = r − 1 for 1 ⩽ i ⩽ n,
    0   otherwise.
```

## Translation ledger (Exposé IV-specific)

| French                                           | English                                  | Note                                                                                           |
| ------------------------------------------------ | ---------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `T : C° → Ab` (foncteurs additifs)               | `T : C° → Ab` (additive functors)        | Contravariant; `C°` is the opposite category. Convention pinned at first use.                  |
| homothétie `f_M`                                 | homothety `f_M`                          | Standard. Multiplication-by-`f` map on `M`.                                                    |
| limite projective / inductive                    | inverse limit / direct limit             | Modern English (per glossary). The source's `lim_←`/`lim_→` notation is preserved.             |
| foncteur exact à gauche                          | left exact functor                       | Per glossary.                                                                                  |
| de présentation finie                            | of finite presentation                   | Standard.                                                                                      |
| ∂-foncteur exact                                 | exact `∂`-functor                        | Original Grothendieck notation preserved; modern usage would say *exact sequence of functors*. |
| corps résiduel                                   | residue field                            | Per glossary.                                                                                  |
| socle                                            | socle                                    | Standard module-theoretic term; kept as in source.                                             |
| longueur (`long M`)                              | length (`long M`)                        | Original abbreviation `long` preserved inside math.                                            |
| module dualisant / foncteur dualisant            | dualizing module / dualizing functor     | Per glossary.                                                                                  |
| enveloppe injective                              | injective envelope                       | Per glossary.                                                                                  |
| extension essentielle                            | essential extension                      | Per glossary.                                                                                  |
| restriction (resp. extension) des scalaires      | restriction (resp. extension) of scalars | Standard.                                                                                      |
| forme résidu                                     | residue form                             | Per glossary (§5.5).                                                                           |
| `Hom_A(B, I)` (with `B` a finite `A`-algebra)    | `Hom_A(B, I)`                            | Notation preserved; the `B`-module structure is via the second argument.                       |
| module localement artinien                       | locally artinian module                  | Standard. Direct limit of finite-length submodules.                                            |
| EGA 0_I 7.2.9                                    | EGA 0_I 7.2.9                            | Cross-reference preserved.                                                                     |
| `Ω^n(A/K)`                                       | `Ω^n(A/K)`                               | Completed relative differentials of maximal degree.                                            |
| C̄ (sous-catégorie des modules de longueur finie) | `C̄`                                      | Source uses an overline on `C`; rendered with the combining macron `C̄`.                        |

[^N.D.E-IV-1]: *N.D.E.* The definition of `H` is implicit in the original text.

[^N.D.E-IV-2]: *N.D.E.* Here one must understand by "the completion of `I`" the tensor product `Î = I ⊗_A Â` (cf. Lemma
    4.5), namely `I` endowed with its canonical `Â`-module structure, and not the `𝔪`-adic completion. For
    example, if `p` is a prime number and `A = Â = ℤ_p` is the ring of `p`-adic integers, then the injective
    envelope of the residue field `k = ℤ/pℤ` is the discrete `ℤ_p`-module `ℚ_p/ℤ_p`, whose completion for the
    `p`-adic topology is zero.

[^N.D.E-IV-3]: *N.D.E.* See Cohen I.S., "On the structure and ideal theory of complete local rings", *Trans. Amer. Math.
    Soc.* **59** (1946), pp. 54–106.

[^IV-4-1]: This was the method followed by Grothendieck (in 1957). The method by injective envelopes that now follows is
    due, it seems, to K. Morita, "Duality for modules and its applications to the theory of rings with minimum
    conditions", *Sc. Rep. Tokyo Kyoiku Daigaku* **6** (1958/59), pp. 83–142. Morita's work is, moreover,
    independent of Grothendieck's and considerably earlier than the present seminar, and is not limited to the
    case of commutative base rings.

[^N.D.E-IV-4]: *N.D.E.* Of course, what is assumed exact is the small filtered direct limits; one should also assume the
    existence of a generator. Cf. *Tôhoku*. As for the category of modules, which suffices for our purposes,
    one may also refer to Chapter 10 of Bourbaki's *Algèbre*.

[^N.D.E-IV-5]: *N.D.E.* As already observed, one may also simply remark that `I` is the direct limit of the modules
    `Hom_A(A/𝔪^n, I)`.

[^IV-5-1]: Let `A` be a ring, `J` an ideal of `A`, `M` an `A`-module, `i ∈ ℤ`; one then sets `H^i_J(M) = H^i_Y(X, F̃)`,
    where `X = Spec(A)`, `Y = V(J)` and `F̃ = M̃`.

[^IV-5-2]: For a more detailed study of the notion of residue, cf. R. Hartshorne, *Residues and Duality*, Lect. Notes in
    Math., vol. 20, Springer, 1966.
