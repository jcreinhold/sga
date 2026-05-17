# Exposé I. Algebraic structures. Group cohomology

<!-- label: III.I -->

*by M. Demazure*

<!-- original page 1 -->

[^I-0-0] This Exposé consists of two parts; the first gathers a certain number of general definitions and sets up
notations that will often be used in the sequel, while the second treats group cohomology and culminates in Theorem
5.3.3 (vanishing of the cohomology of diagonalizable groups).

We choose once and for all a Universe.[^N.D.E-I-1] All the definitions stated and all the constructions carried out will
be relative to this Universe. We shall systematically allow ourselves the following abuse of language: in order to
define a functor `f : C → C′`, we shall content ourselves with defining the object `f(S)` of `C′` for every object `S`
of `C`, each time that there is no ambiguity about the way to define `f(h)` for an arrow `h` of `C`. In practice, we
shall say: let `f : C → C′` be the functor defined by `f(S) = ⋯`.

## 1. Generalities

### 1.1.

Let `C` be a category. We shall denote by `Ĉ` the category `Hom(C°, (Ens))` of contravariant functors from `C` to the
category `(Ens)` of sets.[^N.D.E-I-2] There exists a canonical functor `h : C → Ĉ` which associates to every `X ∈ Ob(C)`
the functor `hX` such that

```text
hX(S) = Hom(S, X).
```

For every functor `F ∈ Ob(Ĉ)`, one defines (cf. for example EGA 0_III, 8.1.4) a bijection

```text
Hom(hX, F) ⥲ F(X).
```

[^N.D.E-I-3]

<!-- original page 2 -->

In particular, for every pair `X, Y` of objects of `C`, the following canonical map is bijective:

```text
Hom_C(X, Y) ⥲ Hom_Ĉ(hX, hY);
```

i.e. the functor `h` is fully faithful. It thus defines an isomorphism of `C` onto a full subcategory of `Ĉ`, and an
equivalence of `C` with the full subcategory of `Ĉ` formed by the representable functors (i.e. those isomorphic to a
functor of the form `hX`). In the sequel, we shall often identify `X` and `hX`. The following numbers aim to show that
this identification can be made without danger.

**Remark 1.1.1.**[^N.D.E-I-4] *We sometimes need the following variant. Let `D` be a full subcategory of `C` and let
`X, Y ∈ Ob(D)`; denote by `h′_X` and `h′_Y` the restrictions to `D` of `hX` and `hY`. Then one has*

```text
Hom_C(X, Y) = Hom_D(X, Y) = Hom_D̂(h′_X, h′_Y)
```

*and therefore: to give a morphism `X → Y` "is the same thing" as to give, functorially in `T`, a map
`φ(T) : Hom(T, X) → Hom(T, Y)`, for every `T ∈ Ob(D)`.*

<!-- label: III.I.1.1.1 -->

### 1.2.

[^N.D.E-I-5] We shall say that `F` is a *subobject* (or a *subfunctor*) of `G` if `F(S)` is a subset of `G(S)` for each
`S`.

In `Ĉ`, "arbitrary" inverse limits exist and are computed by:

```text
(lim←_i F_i)(S) = lim←_i F_i(S).
```

[^N.D.E-I-6] In particular, fiber products are defined by:

```text
(F ×_G F′)(S) = F(S) ×_{G(S)} F′(S).
```

[^N.D.E-I-7]

<!-- original page 3 -->

We shall choose as final object of `Ĉ` the functor `e` such that `e(S) = {∅}`[^N.D.E-I-8]. Every `F ∈ Ob(Ĉ)` has a
unique morphism into `e`, and one sets

```text
F × F′ = F ×_e F′.
```

The functor `h` commutes with inverse limits; in particular, for `X × X′` to exist (`X, X′ ∈ Ob(C)`), resp. for `C` to
admit a final object `e`, it is necessary and sufficient that `hX × hX′` be representable, resp. that `e` be
representable, and one has

```text
hX × hX′ ≃ h_{X×X′}    and    he ≃ e.
```

A monomorphism of `Ĉ` is nothing other than a morphism `F → G` such that, for every `S ∈ Ob(C)`, the corresponding map
of sets `F(S) → G(S)` is injective.[^N.D.E-I-9]

*The functor `Γ`.* For every `F ∈ Ob(Ĉ)`, one sets

```text
Γ(F) = Hom(e, F);
```

an element of `Γ(F)` is therefore a family `(γ_S)_{S∈Ob(C)}`, `γ_S ∈ F(S)`, such that for every arrow `f : S′ → S″` of
`C` one has `F(f)(γ_{S″}) = γ_{S′}`.

One sets `Γ(X) = Γ(hX)` for `X ∈ Ob(C)`. If `C` has a final object `e`, one therefore has an isomorphism
`Γ(X) ≃ Hom(e, X)`.

### 1.3.

Let `S ∈ Ob(C)`. We denote by `C/S` the category of objects of `C` over `S`, i.e. the category whose objects are the
arrows `f : T → S` of `C`, with `Hom(f, f′)` being the subset of `Hom(T, T′)` formed by those `u` such that
`f = f′ ∘ u`. If `C` has a final object `e`, then `C/e` is isomorphic to `C`. The category `C/S` has a final object: the
identity arrow `S → S`.

If `f : T → S` is an object of `C/S`, then one can form the category `(C/S)/f`, which by abuse of language one denotes
`(C/S)/T`, and one has a canonical isomorphism

```text
C/T ≃ (C/S)/T.
```

This construction also applies to the category `Ĉ`; one defines in particular the category `Ĉ/hS`. On the other hand,
one can form the category `Ĉ_{/S}`.

If `f : T → S` is an object of `C/S`, then `Γ(f)` is identified with the set `Γ(T/S)` of sections of `T` over `S`, that
is, of arrows `S → T` which are right inverses of `f`. Note that `hf : hT → hS` is then an object of `Ĉ/hS`, and one
has:

<!-- original page 4 -->

```text
Γ(hf) ≃ Γ(hT/hS) ≃ Γ(T/S) ≃ Γ(f).
```

### 1.4.

We now propose to define an equivalence of categories `Ĉ_{/S}` and `Ĉ/hS`, that is, to prove that "to give a functor on
the category of objects of `C` over `S` is `the same thing` as to give a functor on `C` endowed with a morphism into
`hS`".

**(i)** *Construction of `αS : Ĉ/hS → Ĉ_{/S}`.*

Let first `H : F → hS` be an object of `Ĉ/hS`. We must define a functor `αS(H)` on `C/S`. Let first `f : T → S` be an
object of `C/S`; we define `αS(H)(f)` as the inverse image of `f ∈ hS(T)` by the map `H(T) : F(T) → hS(T)`.[^N.D.E-I-10]

Next, let `u : f → f′` be an arrow of `C/S`; then `F(u) : F(T′) → F(T)` induces a map from `αS(H)(f′)` into `αS(H)(f)`,
which we denote `αS(H)(u)`. One verifies at once that the maps

```text
f ↦ αS(H)(f)    and    u ↦ αS(H)(u)
```

do define a functor on `C/S`, hence an object `αS(H)` of `Ĉ_{/S}`.

Finally, let `H : F → hS` and `H′ : F′ → hS` be two objects of `Ĉ/hS` and `U : H → H′` a morphism of `Ĉ/hS`:

```text
        U
   F ──────→ F′
    ╲       ╱
   H ╲     ╱ H′
      ╲   ╱
       hS
```

<!-- original page 5 -->

Then for every `f : T → S`, the map `U(T) : F(T) → F′(T)` induces a map

```text
αS(U)(f) :  αS(H)(f) → αS(H′)(f),
```

which defines a morphism of functors

```text
αS(U) :  αS(H) → αS(H′).
```

One verifies easily that the maps

```text
H ↦ αS(H)    and    U ↦ αS(U)
```

do define a functor `αS : Ĉ/hS → Ĉ_{/S}`.

**(ii) Proposition 1.4.1.** *The functor `αS : Ĉ/hS → Ĉ_{/S}` is an equivalence of categories.*

<!-- label: III.I.1.4.1 -->

We only indicate the principle of the construction of a quasi-inverse functor `βS : Ĉ_{/S} → Ĉ/hS`. Let `G` be a functor
on `C/S`; for every object `T` of `C`, one sets

```text
βS(G)(T) = sum of the sets G(f) for f ∈ Hom(T, S) = hS(T),
```

which defines a functor `βS(G)` on `C`, equipped with an obvious projection onto `hS`.

### 1.5.

The equivalence `αS` commutes with the functors `Γ`. In other words, if `H : F → hS` is an object of `Ĉ/hS` and `αS(H)`
the corresponding object of `Ĉ_{/S}`, one has

```text
Γ(αS(H)) ≃ Γ(H) ≃ Γ(F/hS).
```

The equivalence `αS` commutes with the functors `h`, i.e. if `f : T → S` is an object of `C/S`, then `hf : hT → hS` is
an object of `Ĉ/hS` whose transform by `αS` is nothing other than `h_{C/S}(f)`, where

```text
h_{C/S} : C/S → Ĉ_{/S}
```

is the canonical functor.[^N.D.E-I-11] As a consequence:

<!-- original page 6 -->

**Proposition 1.5.1.** *Let `H : F → hS` be an object of `Ĉ/hS`. For `αS(H) : (C/S)° → (Ens)` to be representable, it is
necessary and sufficient that `F : C° → (Ens)` be representable; if `F ≃ hT`, then `αS(H)` is representable by the
object `T → S` of `C/S`.*

<!-- label: III.I.1.5.1 -->

The equivalence `αS` is transitive in `S`: if `f : T → S` is an object of `C/S`, one has a commutative diagram of
equivalences

```text
                α_{S/hT}                    α_f
   (Ĉ/hS)/hT  ─────────→ (Ĉ_{/S})/h_T  ─────────→  Ĉ_{(C/S)/T}
        ╲                                              ╱
      ≃  ╲                                            ╱  ≃
          ╲                                          ╱
           ────────────→ Ĉ/hT  ──────────────→ Ĉ_{/T}
                                  α_T
```

where `α_{S/hT}` denotes (provisionally) the restriction (cf. 1.6) of the functor `αS` to objects above `hT`.

### 1.6. Base change in a functor

For every `S ∈ Ob(C)`, one has a canonical functor

```text
iS : C/S → C
```

defined by `iS(f) = T` if `f` is the arrow `T → S`. If `f : T → S` is an object of `C/S`, one denotes by `i_{T/S} = i_f`
the functor:

```text
i_{T/S} : (C/S)/T → C/S,
```

and one has the commutative diagram:

```text
                i_{T/S}       iS
   (C/S)/T  ─────────→ C/S  ─────→ C
        ╲                          ╱
      ≃  ╲                        ╱ iT
          ╲                      ╱
           C/T
```

that is, identifying `(C/S)/T` with `C/T` as we shall do henceforth,

<!-- original page 7 -->

```text
iS ∘ i_{T/S} = iT.
```

In the same way, if one identifies `C` and `C/e` when `C` has a final object `e`, then `i_{S/e} : C/S → C/e` is
identified with `iS`.

For `X ∈ Ob(C)` (resp. `Y ∈ Ob(C/S)`), let `pS(X)` (resp. `p_{T/S}(Y)`) denote the object of `C/S` (resp. of `C/T`),
when it exists, defined by `X × S` (resp. `Y ×_S T`) equipped with its second projection:

```text
   X × S                  Y ×_S T
     │                        │
   pS(X) ↓     resp.     p_{T/S}(Y) ↓
     │                        │
     S                        T
```

The (partially defined) functor `pS` (resp. `p_{T/S}`) is called the *base change functor*. It is by definition of the
product (resp. of the fiber product) the right adjoint of the functor `iS` (resp. `i_{T/S}`).[^N.D.E-I-12] One also
denotes

```text
pS(X) = XS    and    p_{T/S}(Y) = YT.
```

The functor `iS` defines a functor (restriction)

```text
i*_S : Ĉ → Ĉ_{/S};
```

one denotes `FS = i*_S(F) = F ∘ iS`. One has obviously

```text
i*_{T/S} ∘ i*_S = i*_T,
```

that is, for every functor `F ∈ Ob(Ĉ)`,

```text
(FS)T = FT.
```

The notation requires a justification, which is the following:

**Proposition 1.6.1.** *For the functor `(hX)S : (C/S)° → (Ens)` to be representable, it is necessary and sufficient
that the product `X × S` exist. One then has*

```text
(hX)S ≃ h_{XS}.
```

<!-- label: III.I.1.6.1 -->

This shows that `FS` has two interpretations: restriction of the functor `F` to `C/S`, and functor obtained by base
change `e ← S`. This leads to the following notation:

```text
   F        FS          FT

   │         │           │
   e ←────── S ←──────── T
```

which renders both of the preceding interpretations. Note that one has

```text
Γ(FS) ≃ Hom(hS, F) ≃ F(S),
```

in particular

```text
Γ(XS) ≃ Hom(S, X).
```

### 1.7.0.

[^N.D.E-I-13] Let `E` be an object of `Ĉ`. Consider the category `C_E` of objects of `C` above `E`: its objects are the
pairs `(V, ρ)` formed by an object `V` of `C` and a `Ĉ`-morphism `ρ : hV → E`, i.e. `ρ ∈ E(V)`; a morphism from `(V, ρ)`
to `(V′, ρ′)` is

<!-- original page 8 -->

the datum of a `C`-morphism `f : V → V′` such that `ρ′ ∘ f = ρ` (i.e. `E(f)(ρ′) = ρ`). Denote by `L` the functor

```text
lim→_{(V,ρ)∈C_E} hV,
```

i.e. for every `S ∈ Ob(C)`, `L(S) = lim→_{(V,ρ)} hV(S)` is the set of equivalence classes of triples `(V, ρ, v)`, where
`v : S → V` is a `C`-morphism, and where one identifies `(V, ρ, v)` with `(V′, ρ′, f ∘ v)` for every `C`-morphism
`f : V → V′` such that `ρ′ ∘ f = ρ`.

Then the map `φ_E(S)` which to the class of `(V, ρ, v)` associates the element `ρ ∘ v` of `E(S)` is well defined, and
defines a morphism of functors

```text
φ_E :  lim→_{(V,ρ)∈C_E} hV → E.
```

**Lemma.** *`φ_E` is an isomorphism.*

Indeed, let `S ∈ Ob(C)`. Every `x ∈ E(S)` is the image under `φ_E(S)` of the triple `(S, x, id_S)`; this shows that
`φ_E(S)` is surjective. On the other hand, let `ℓ_1 = (V_1, ρ_1, v_1)` and `ℓ_2 = (V_2, ρ_2, v_2)` be two elements of
`L(S)` having the same image in `E(S)`; set `γ = ρ_1 ∘ v_1 = ρ_2 ∘ v_2`. Then `ℓ_1` and `ℓ_2` are both equal, in `L(S)`,
to the class of the triple `(S, γ, id_S)`. This shows that `φ_E(S)` is injective.

**Corollary.** *For every object `F` of `Ĉ`, one has*

```text
Hom(E, F) = lim←_{(V,ρ)∈C_E} F(V).
```

### 1.7. Objects Hom, Isom, etc.

Let `F` and `G` be two objects of `Ĉ`. We shall define another object of `Ĉ` in the following way:

```text
Hom(F, G)(S) = Hom_{Ĉ_{/S}}(FS, GS) ≃ Hom_{Ĉ/hS}(F × hS, G × hS) ≃ Hom_Ĉ(F × hS, G).
```

The object `Hom(F, G)` defined above has the following properties:

**(i)** `Hom(e, G) ≃ G`.[^N.D.E-I-14]

**(ii)** *The formation of `Hom` commutes with base extension:*

<!-- original page 9 -->

```text
Hom(FS, GS) ≃ Hom(F, G)_S.
```

**(iii)** *`(F, G) ↦ Hom(F, G)` is a bifunctor, contravariant in `F` and covariant in `G`.*

These three properties are obvious from the definitions.

We shall show that, for every object `E` of `Ĉ`, one has

```text
Hom(E, Hom(F, G)) ≅ Hom(E × F, G).
```

Let `φ : E × F → G`; we must associate to it a morphism of `E` into `Hom(F, G)`. So let `S′ → S` be an arrow of `C`. One
has maps

```text
E(S) × F(S′) → E(S′) × F(S′) ──φ(S′)──→ G(S′).
```

Every element `e` of `E(S)` therefore defines, for every `S′ → S`, a map `F(S′) → G(S′)` functorial in `S′`, i.e. an
element `θ_φ(e)` of `Hom(F, G)(S)`. One has thus obtained a map

```text
φ ↦ θ_φ,    Hom(E × F, G) → Hom(E, Hom(F, G)),
```

which is "functorial in `E`".

**Proposition 1.7.1.**[^N.D.E-I-15] *Let `E, F, G ∈ Ob(Ĉ)`.*

*(a) The map `φ ↦ θ_φ` is a bijection:*

```text
Hom(E × F, G) ⥲ Hom(E, Hom(F, G)).
```

*(b) Moreover, one has an isomorphism of functors:*

```text
Hom(E, Hom(F, G)) ≃ Hom(E × F, G).
```

<!-- label: III.I.1.7.1 -->

*(a)* Consider both members as functors in `E`. The asserted result is true if `E = hX`; indeed, in that case it is
nothing other than the definition of the functor `Hom(F, G)`. On the other hand, both members as functors in `E`
transform direct limits into inverse limits. Finally, by Lemma 1.7.0, every object `E` of `Ĉ` is isomorphic to the
direct limit of the `hX`, where `X` runs over the category `C_E`. This proves (a).

[^N.D.E-I-15-alt] Let us sketch a direct proof of (a). To every `θ ∈ Hom(E, Hom(F, G))`, one associates the element
`φ_θ` of `Hom(E × F, G)` defined as follows. For every `S ∈ Ob(C)`, one has a map

```text
θ(S) : E(S) → Hom(F × S, G),
```

functorial in `S`. If `(e, f) ∈ E(S) × F(S)`, then `f` is a morphism `S → F`, hence `f × id_S` is a morphism
`S → F × S`; on the other hand, `θ(S)(e)` is a morphism `F × S → G`, so by composition one obtains a morphism:

```text
θ(S)(e) ∘ (f × id_S) : S → G,
```

i.e. an element `φ_θ(S)(e, f)` of `G(S)`. One verifies easily that the correspondence `S ↦ φ_θ(S)` is functorial in `S`,
hence defines a morphism `φ_θ` from `E × F` to `G`. We leave to the reader the verification that the maps `θ ↦ φ_θ` and
`φ ↦ θ_φ` are mutually inverse bijections.

<!-- original page 10 -->

Let us prove (b). If `S ∈ Ob(C)`, one has, by 1.7 (ii) and (a) applied to `C/S`:

```text
Hom(E, Hom(F, G))(S) ≃ Hom_S(ES, Hom_S(FS, GS))
                     ≅ Hom_S(ES ×_S FS, GS)
                     ≅ Hom(E × F × S, G)
                     ≅ Hom(E × F, G)(S)
```

and these isomorphisms are functorial in `S`.

**Corollary 1.7.2.** *One has:*

```text
Hom(E, Hom(F, G)) ≃ Hom(F, Hom(E, G)),
Hom(E, Hom(F, G)) ≃ Hom(F, Hom(E, G)).
```

<!-- label: III.I.1.7.2 -->

In particular, taking `E = e`, and taking into account `Hom(e, G) ≃ G`, one has

```text
Γ(Hom(F, G)) ≃ Hom(F, G).
```

Note that the composition of `Hom`'s provides functorial morphisms

```text
Hom(F, G) × Hom(G, H) → Hom(F, H).
```

If `F` and `G` are two objects of `Ĉ`, one denotes by `Isom(F, G)` the subset of `Hom(F, G)` formed by the isomorphisms
of `F` onto `G`. One then defines a subobject `Isom(F, G)` of `Hom(F, G)` by:

```text
Isom(F, G)(S) = Isom(FS, GS).
```

One then has isomorphisms

```text
Γ(Isom(F, G)) ≃ Isom(F, G),
Isom(F, G) ≃ Isom(G, F).
```

In the particular case where `F = G`, one sets

```text
End(F) = Hom(F, F),    End(F) = Hom(F, F) ≃ Γ(End(F)),
Aut(F) = Isom(F, F),    Aut(F) = Isom(F, F) ≃ Γ(Aut(F)).
```

The formation of the objects `Hom, Isom, Aut, End` commutes with base change.

**Remark 1.7.3.**[^N.D.E-I-16] One can construct an object isomorphic to `Isom(F, G)` in the following manner: one has a
morphism

```text
Hom(F, G) × Hom(G, F) → End(F);
```

permuting `F` and `G`, one deduces a morphism

```text
Hom(F, G) × Hom(G, F) → End(F) × End(G).
```

<!-- original page 11 -->

On the other hand, the identity morphism of `F` is an element of `End(F)` and therefore defines a morphism `e → End(F)`.
Doing the same with `G` and forming the product, one finds a morphism

```text
e → End(F) × End(G).
```

It is then immediate that the fiber product of `e` and of `Hom(F, G) × Hom(G, F)` over `End(F) × End(G)` is isomorphic
to `Isom(F, G)`.

<!-- label: III.I.1.7.3 -->

All these definitions apply in particular to the case where `F = hX, G = hY`. In the case where `Hom(hX, hY)` is
representable by an object of `C`, one denotes this object by `Hom(X, Y)`. It has the following property: if `Z × X`
exists, then

```text
Hom(Z, Hom(X, Y)) ≃ Hom(Z × X, Y).
```

This property characterizes it when the products exist in `C`.

One defines similarly (when they happen to exist) objects

```text
Isom(X, Y),    End(X),    Aut(X);
```

we simply note that, by the construction given above, `Isom(X, Y)` exists whenever fiber products exist in `C` and
`Hom(X, Y), Hom(Y, X), End(X)` and `End(Y)` exist.

All that precedes applies equally to categories of the form `C/S`. The corresponding objects will be denoted as
explicitly as possible by appropriate symbols: for example, if `T` and `T′` are two objects of `C` above `S`, one will
denote by `Hom_S(T, T′)` the object `Hom_{C/S}(T/S, T′/S)`.

### 1.8. Constant objects

Let `C` be a category in which direct sums and fiber products exist, and in which direct sums commute with base change
(for example, the category of schemes[^N.D.E-I-17]). For every set `E` and every object `S` of `C`, we set

```text
(1.8.1)    ES =  the direct sum of a family (S_i)_{i∈E}
                 of objects of C all isomorphic to S.
```

This object is characterized by the formula:

```text
(1.8.2)    Hom_C(ES, T) = Hom(E, Hom_C(S, T)),
```

for every `T ∈ Ob(C)`, where the second `Hom` is taken in the category of sets.

The object `ES` is equipped with a canonical projection onto `S`, in such a way that `E ↦ ES` is in fact a functor from
`(Ens)` to `C/S`.

[^N.D.E-I-18] If `S′ → S` is an arrow of `C`, one has, since direct sums commute with base change,

```text
E_{S′} = (ES)_{S′}.
```

In particular, if `C` has a final object `e`, one has

```text
ES = (Ee)_S.
```

<!-- original page 12 -->

The functor `E ↦ ES/S`, from `(Ens)` to `C/S`, commutes with finite products. For this, it suffices to see that

```text
(×)    ES ×_S FS = (E × F)_S.
```

<!-- label: eq:III.I.1.8-cross -->

Now, by the results of 1.7 applied to `C/S`, one has, for every `T ∈ Ob(C/S)`, natural isomorphisms (all unspecified
`Hom`'s being taken in `C/S`):

```text
Hom((E × F)_S, T) ≅ Hom_{(Ens)}(E × F, Hom(S, T)) ≅
        Hom_{(Ens)}(E, Hom_{(Ens)}(F, Hom(S, T))) ≅ Hom_{(Ens)}(E, Hom(FS, T))
```

and

```text
Hom(ES ×_S FS, T) ≅ Hom(ES, Hom(FS, T)) ≅ Hom_{(Ens)}(E, Hom(S, Hom(FS, T))).
```

Now `Hom(S, Hom(FS, T)) ≅ Hom(FS, T)`, hence `(×)`.

Suppose that, with `∅` denoting an initial object of `C`, the diagram

```text
   ∅ ────→ S
   │         │
   ↓         ↓
   S ────→ S ⊔ S
```

`(∗)` *is cartesian.*

(This is the case for the category of schemes.)[^N.D.E-I-19] Then the functor `E ↦ ES` commutes with finite inverse
limits.

Indeed, taking `(×)` into account, it suffices to see that `E ↦ ES` commutes with fiber products. Let `u : E → G` and
`v : F → G` be two maps of sets. Since in `C` direct sums commute with base change, one has

```text
(1)    FS ×_{GS} ES ≅ ⨆_{f∈F} S_f ×_{GS} ES ≅ ⨆_{f∈F, x∈E} S_f ×_{GS} S_x.
```

If `v(f) ≠ u(x)`, there exists in `C/S` a morphism

```text
S_f ×_{GS} S_x → S_f ×_{S_{v(f)} ⊔ S_{u(x)}} S_x;
```

now by hypothesis `(∗)` the right-hand term is `∅`. Consequently,

```text
(2)    S_f ×_{GS} S_x ≅ ∅    if v(f) ≠ u(x).
```

On the other hand, if `v(f) = u(x)`, there exists in `C/S` a morphism

```text
S → S_f ×_{GS} S_x;
```

since `S ──id──→ S` is the final object of `C/S`, it follows that

```text
(3)    S_f ×_{GS} S_x ≅ S    if v(f) = u(x).
```

<!-- original page 13 -->

Combining (1), (2), and (3) one obtains an isomorphism functorial in `S`

```text
FS ×_{GS} ES ≅ ⨆_{F ×_G E} S = (F ×_G E)_S.
```

An object of the form `ES` will be called a *constant object*. Note that one has a morphism functorial in `E`:

```text
E → Γ(ES/S)
```

which associates to each `i ∈ E` the section of `ES` over `S` defined by the isomorphism of `S` onto `S_i`. Suppose
condition `(∗)` is satisfied for every object `S` of `C`; then the morphism `E → Γ(ES/S)` is a monomorphism for every
`S ≄ ∅`.

If `C` is the category of schemes, then `Γ(ES/S)` is identified with the locally constant maps from the topological
space `S` to the set `E`, the preceding map associating to each element of `E` the corresponding constant map. Note
that, by what was just said, `ES` may also be defined as representing the functor which to every `S′` over `S`
associates the set of locally constant functions from the topological space `S′` to the set `E`.[^N.D.E-I-20]

## 2. Algebraic structures

Given a species of algebraic structure in the category of sets, we propose to extend it to the category `C`. Let us
first treat one example: the case of groups.

### 2.1. Group structures

We retain the notations of the preceding paragraph.

**Definition 2.1.1.** *Let `G ∈ Ob(Ĉ)`. By a* `Ĉ`-group structure *on `G`, we mean the datum, for every `S ∈ Ob(C)`, of
a group structure on the set `G(S)`, in such a way that for every arrow `f : S′ → S″` of `C`, the map
`G(f) : G(S″) → G(S′)` is a group homomorphism. If `G` and `H` are two `Ĉ`-groups, by a* morphism of `Ĉ`-groups *from
`G` into `H` we mean any morphism `u ∈ Hom(G, H)` such that for every `S ∈ Ob(C)`, the map of sets `u(S) : G(S) → H(S)`
is a group homomorphism.*

<!-- label: III.I.2.1.1 -->

One denotes by `Hom_{Ĉ-Gr.}(G, H)` the set of morphisms of `Ĉ`-groups from `G` into `H`, and by `(Ĉ-Gr.)` the category
of `Ĉ`-groups.

**Examples.** Let `E ∈ Ob(Ĉ)`; the object `Aut(E)` is endowed in an obvious manner with a `Ĉ`-group structure. The final
object `e` has a unique `Ĉ`-group structure which makes it a final object of `(Ĉ-Gr.)`.

For every `S ∈ Ob(C)`, let `e_G(S)` be the identity element of `G(S)`. The family of the `e_G(S)`

<!-- original page 14 -->

defines an element `e_G ∈ Γ(G) = Hom(e, G)` which is a morphism of `Ĉ`-groups `e → G`, and which is called the *unit
section* of `G`.

Note that to give a `Ĉ`-group structure on `G` amounts to giving a composition law on `G`, i.e. a `Ĉ`-morphism

```text
π_G : G × G → G
```

such that, for every `S ∈ Ob(C)`, `π_G(S)` endows `G(S)` with a group structure.

In the same way, `f : G → H` is a morphism of `Ĉ`-groups if and only if the following diagram is commutative:

```text
              π_G
   G × G ─────────→ G
     │              │
   (f,f)           f
     ↓     π_H      ↓
   H × H ─────────→ H
```

A subobject `H` of `G` such that, for every `S ∈ Ob(C)`, `H(S)` is a subgroup of `G(S)`, obviously has a `Ĉ`-group
structure induced by that of `G`: it is the only one for which the monomorphism `H → G` is a morphism of `Ĉ`-groups. The
`Ĉ`-group `H` endowed with this structure is called a *sub-`Ĉ`-group of `G`*.

If `G` and `H` are two `Ĉ`-groups, the product `G × H` is endowed with an obvious `Ĉ`-group structure: for every
`S ∈ Ob(C)`, one endows `G(S) × H(S)` with the product group structure of the group structures given on `G(S)` and
`H(S)`. The `Ĉ`-group `G × H` endowed with this structure will be called the *product `Ĉ`-group* of `G` and `H` (it is
indeed the product in the category of `Ĉ`-groups).

If `G` is a `Ĉ`-group, then for every `S ∈ Ob(C)`, `GS` is a `Ĉ_{/S}`-group. If `G` and `H` are two `Ĉ`-groups, one
defines the object `Hom_{Ĉ-Gr.}(G, H)` of `Ĉ` by:

```text
Hom_{Ĉ-Gr.}(G, H)(S) = Hom_{Ĉ_{/S}-Gr.}(GS, HS)
```

(Note: `Hom_{Ĉ-Gr.}` is not in general a `Ĉ`-group, nor a fortiori the `Hom` object in

<!-- original page 15 -->

the category `(Ĉ-Gr.)`).

One defines similarly the objects

```text
Isom_{Ĉ-Gr.}(G, H),    End_{Ĉ-Gr.}(G),    Aut_{Ĉ-Gr.}(G).
```

**Definition 2.1.2.** *Let `G ∈ Ob(C)`. By a* `C`-group structure *on `G`, we mean a `Ĉ`-group structure on
`hG ∈ Ob(Ĉ)`. By a* morphism of the `C`-group `G` into the `C`-group `H`, *we mean an element
`u ∈ Hom(G, H) ≃ Hom(hG, hH)` which defines a morphism of `Ĉ`-groups from `hG` into `hH`.*

<!-- label: III.I.2.1.2 -->

One denotes by `(C-Gr.)` the category of `C`-groups. Note that there exists in `(Cat)` a cartesian square

```text
   (C-Gr.) ─────────→ (Ĉ-Gr.)
      │                  │
      ↓        h         ↓
      C ─────────────→  Ĉ
```

All the preceding definitions and constructions therefore transport at once to `(C-Gr.)` whenever the functors they
involve (products, `Hom` objects, etc.) are representable. They also apply to the categories `C/S`. In that case, we
shall write `Hom_{S-Gr.}` for `Hom_{Ĉ_{/S}-Gr.}`, etc.

### 2.2.

More generally, if `(T)` is a species of structure on `n` base sets defined by finite inverse limits (for example, by
commutativities of diagrams constructed with cartesian products: structures of monoid, group, set with operators, module
over a ring, Lie algebra over a ring, etc.), the preceding construction permits one to define the notion of "structure
of species `(T)` on `n` objects `F_1, …, F_n` of `Ĉ`":

<!-- original page 16 -->

such a structure will be the datum, for each `S` of `C`, of a structure of species `(T)` on the sets `F_1(S), …, F_n(S)`
in such a way that for every arrow `S′ → S″` of `C`, the family of maps `(F_i(S″)) → (F_i(S′))` is a polyhomomorphism
for the species of structure `(T)`. One defines similarly the morphisms of the species of structure `(T)`, whence a
category `(Ĉ × Ĉ ⋯ × Ĉ)^{(T)}`. The fully faithful functor `(h × h × ⋯ × h)` then allows one to define by inverse image
the category `(C × C × ⋯ × C)^{(T)}`, and then, as it commutes with inverse limits, to transport to it all the
properties, notions, and notations of a functorial kind introduced in `Ĉ`. Suppose now that in `C` fiber products exist,
and let `(T)` be a species of algebraic structure defined by the datum of certain morphisms between cartesian products
satisfying axioms consisting of certain commutativities of diagrams constructed using the preceding arrows. A structure
of species `(T)` on a family of objects of `C` will therefore be defined by certain morphisms between cartesian products
satisfying certain commutation conditions. It follows that if `C` and `C′` are two categories possessing products and
`f : C → C′` is a functor commuting with products, then for every family of objects `(F_i)` of `C` endowed with a
structure of species `(T)`, the family `(f(F_i))` of objects of `C′` will thereby also be endowed with a structure of
species `(T)`. Every `C`-group will be transformed into a `C′`-group, every pair (`C`-ring, `C`-module over this
`C`-ring) into an analogous pair in `C′`, etc.

In particular, let `C` be a category satisfying the conditions of 1.8;[^N.D.E-I-21] the functor `E ↦ ES` defined in
*loc. cit.* commutes with finite inverse limits; it therefore transforms group into `S`-group (i.e. `C/S`-group), ring
into `S`-ring, etc.

**Remark.** It is good to note that the preceding construction procedure applied to the category `Ĉ` does give back the
notions already defined there; in other words, it amounts to the same thing to give on an object of `Ĉ` a structure of
species `(T)` when one considers this object as a functor on `C`, or to give a structure of species `(T)` on the
representable functor on `Ĉ` defined by this object.[^N.D.E-I-22]

<!-- original page 17 -->

We shall still treat two particular cases of the preceding construction, the case of structures with operator groups and
the case of modules.

### 2.3. Structures with operator groups

**Definition 2.3.1.** *Let `E ∈ Ob(Ĉ)` and `G ∈ Ob(Ĉ-Gr.)`. A structure of* object with `Ĉ`-operator group `G` (*or of
`G`-object*) *on `E` is the datum, on `E(S)`, for every `S ∈ Ob(C)`, of a structure of set with operator group `G(S)` in
such a way that, for every arrow `S′ → S″` of `C`, the map of sets `E(S″) → E(S′)` is compatible with the operator
homomorphism `G(S″) → G(S′)`.*

<!-- label: III.I.2.3.1 -->

As usual, it amounts to the same thing to give a morphism

```text
μ : G × E → E
```

which for each `S` endows `E(S)` with a structure of set with operators `G(S)`. But `Hom(G × E, E) ≃ Hom(G, End(E))`, so
`μ` defines a morphism `G → End(E)`, and it is immediate that this maps `G` into `Aut(E)` and is a morphism of
`Ĉ`-groups. Consequently: to give on `E` a structure of object with `Ĉ`-operator group `G` is equivalent to giving a
morphism of `Ĉ`-groups

```text
ρ : G → Aut(E).
```

In particular, every element `g ∈ G(S)` defines an automorphism `ρ(g)` of the functor `ES`, that is, an automorphism of
`E × hS` commuting with the projection `E × hS → hS`, and in particular an automorphism of the set `E(S′)` for every
`S′ → S`.

**Definition 2.3.2.** *One denotes by `E^G` the subobject of `E` defined as follows:*

```text
E^G(S) = {x ∈ E(S) | x_{S′} invariant under G(S′) for every S′ → S},
```

*where `x_{S′}` denotes the image of `x` by `E(S) → E(S′)`.*

<!-- label: III.I.2.3.2 -->

Then `E^G` (*"subobject of invariants of `G`"*)

<!-- original page 18 -->

is the largest subobject of `E` on which `G` operates trivially.

**Definition 2.3.3.** *Let `F` be a subobject of `E`. One denotes by `Norm_G F` and `Centr_G F` the sub-`Ĉ`-groups of
`G` defined by*

[^N.D.E-I-23]

```text
(Norm_G F)(S) = {g ∈ G(S) | ρ(g) FS = FS}
              = {g ∈ G(S) | ρ(g) F(S′) = F(S′), for every S′ → S},

(Centr_G F)(S) = {g ∈ G(S) | ρ(g)|FS = identity}
               = {g ∈ G(S) | ρ(g)|F(S′) = identity, for every S′ → S},
```

*where the vertical bar after `ρ(g)` denotes restriction.*

<!-- label: III.I.2.3.3 -->

**Scholium 2.3.3.1.**[^N.D.E-I-24] *In particular, let `x ∈ Γ(E)`, i.e. (cf. 1.2) a collection of elements `x_S ∈ E(S)`,
`S ∈ Ob(C)`, such that for every arrow `f : S′ → S` one has `E(f)(x_S) = x_{S′}` (if `C` has a final object `S_0` one
has `Γ(E) = E(S_0)`). Then `x` defines a subfunctor of `E`, which we shall denote `x̄`, and one has*
`Norm_G x̄ = Centr_G x̄`. *We shall denote by `Stab_G(x)` and call* stabilizer of `x` *this functor; for every
`S ∈ Ob(C)` one therefore has:*

```text
Stab_G(x)(S) = {g ∈ G(S) | ρ(g) x_S = x_S}.
```

*Suppose that fiber products exist in `C`; if `G = hG`* (resp. `E = hE`), *where `G` is a `C`-group (resp. `E ∈ Ob(C)`),
and if `C` has a final object `S_0`, so that `x` is a morphism `S_0 → E`, then `Stab_G(x)` is representable by the fiber
product `G ×_E S_0`, where `G → E` is the composite of `id_G × x : G = G × S_0 → G × E` and of `μ : G × E → E`.*

<!-- label: III.I.2.3.3.1 -->

**Remark 2.3.3.2.**[^N.D.E-I-24] *The formation of `E^G`, `Norm_G F` and `Centr_G F` commutes with base change, i.e. for
every `S ∈ Ob(C)` one has*

```text
(E^G)_S = (ES)^{GS},    (Norm_G F)_S ≃ Norm_{GS} F_S,    (Centr_G F)_S ≃ Centr_{GS} F_S.
```

<!-- label: III.I.2.3.3.2 -->

**Definition 2.3.4.** *If `G` is a `C`-group and `E` an object of `Ĉ`* (resp. `E` an object of `C`) *a structure of
`G`-object on `E`* (resp. on `E`) *is a structure of `hG`-object on `E`* (resp. `hE`).

<!-- label: III.I.2.3.4 -->

In view of this definition, all the notions and notations defined above transport to `C` when they involve only
representable functors: for example, if `Norm_{hG}(hF)` is representable, then there exists one and only one subobject
of `G` that represents it, and which is then a sub-`C`-group of `G`; one denotes it `Norm_G(F)`, etc.

**Definition 2.3.5.** *a) One says that the `Ĉ`-group `G`* operates *on the `Ĉ`-group `H` if `H` is endowed with a
structure of `G`-object such that, for every `g ∈ G(S)`, the automorphism of `H(S)` defined by `g` is a group
automorphism.*

It amounts to the same thing to say that for every `g ∈ G(S)`, the automorphism `ρ(g)` of `HS`

<!-- original page 19 -->

is an automorphism of `Ĉ_{/S}`-groups, or that the morphism of `Ĉ`-groups `G → Aut(H)` maps `G` into `Aut_{Ĉ-Gr.}(H)`.

*b) In the situation above, there exists on the product `H × G` a unique `Ĉ`-group structure such that, for every `S`,
`(H × G)(S)` is the semidirect product of the groups `H(S)` and `G(S)` relative to the given operation of `G(S)` on
`H(S)`. We shall denote this `Ĉ`-group `H ⋅ G` and call it the* semidirect product *of `H` by `G`. One therefore has by
definition*

```text
(H ⋅ G)(S) = H(S) ⋅ G(S).
```

<!-- label: III.I.2.3.5 -->

Let `G` be a `Ĉ`-group. For every arrow `S′ → S` of `C` and every `g ∈ G(S)`, let `Int(g)` be the automorphism of
`G(S′)` defined by `Int(g) h = g h g^{-1}`. This definition extends into that of a morphism of `Ĉ`-groups

```text
Int : G → Aut_{Ĉ-Gr.}(G) ⊂ Aut(G).
```

Definition 2.3.3 therefore applies, and one has sub-`Ĉ`-groups of `G`

```text
Norm_G(E) and Centr_G(E)
```

for every subobject `E` of `G`.

**Definition 2.3.6.** *One calls* center of `G` *and one denotes by `Centr(G)` the sub-`Ĉ`-group `Centr_G(G)` of `G`.
One says that `G` is* commutative *if `Centr(G) = G`, or, what amounts to the same thing, if `G(S)` is commutative for
every `S`.*

*One says that the sub-`Ĉ`-group `H` of `G` is* invariant *in `G` (or* normal\*) if `Norm_G(H) = G`, or, what amounts to
the same thing, if `H(S)` is invariant in `G(S)` for every `S`.\*[^N.D.E-I-25]

<!-- label: III.I.2.3.6 -->

**Definition 2.3.6.1.**[^N.D.E-I-26] *Let `f : G → G′` be a morphism of `Ĉ`-groups. One calls* kernel of `f`, *and one
denotes by `Ker f`, the sub-`Ĉ`-group of `G` defined by*

```text
(Ker f)(S) = {x ∈ G(S) | f(S)(x) = 1} = Ker f(S)
```

*for every `S ∈ Ob(C)`; it is an invariant sub-`Ĉ`-group.*

*Note that if `G = hG` and `G′ = hG′`, if `C` has a final object `S_0` and if fiber products exist in `C`, then `Ker(f)`
is representable by `S_0 ×_{G′} G`.*

<!-- label: III.I.2.3.6.1 -->

**Definition 2.3.6.2.**[^N.D.E-I-26] *Let `E ∈ Ĉ` and `G` a `Ĉ`-group operating on `E`. One says that the operation of
`G` on `E` is* faithful *if the kernel of the morphism `G → Aut(E)` is trivial, i.e. if for every `S ∈ Ob(C)` and
`g ∈ G(S)`, the condition `g_{S′} ⋅ x = x` for every `S′ → S` and `x ∈ E(S′)` entails `g = 1`.*

<!-- label: III.I.2.3.6.2 -->

Many definitions and propositions of the elementary theory of groups transpose easily. Let us simply point out the
following, which will be useful to us:

**Proposition 2.3.7.** *Let `f : W → G` be a morphism of `Ĉ`-groups. Set `H(S) = Ker f(S)`. Let `u : G → W` be a
morphism of `Ĉ`-groups which is a section of `f`*

<!-- original page 20 -->

*(and which is then necessarily a monomorphism). Then `W` is identified with the semidirect product of `H` by `G` for
the operation of `G` on `H` defined by `(g, h) ↦ Int(u(g)) h` for `g ∈ G(S)`, `h ∈ H(S)`, `S ∈ Ob(C)`.*

<!-- label: III.I.2.3.7 -->

The set of these definitions and propositions transports as usual to `C`. One defines in particular the semidirect
product of two `C`-groups `H` and `G` (with `G` operating on `H`) when the cartesian product `H × G` exists, and one has
the analogue of Proposition 2.3.7 in the following form:

**Proposition 2.3.8.** *Let `H ──i──→ W ──f──→ G` be a sequence of morphisms of `C`-groups such that for every
`S ∈ Ob(C)`, `(H(S), i(S))` is a kernel of `f(S) : W(S) → G(S)`. Let `u : G → W` be a morphism of `C`-groups which is a
section of `f`. Then `W` is identified with the semidirect product of `H` by `G` for the operation of `G` on `H` such
that if `S ∈ Ob(C)`, `g ∈ G(S)` and `h ∈ H(S)`, one has `Int(u(g)) i(h) = i({}^g h)`.*

<!-- label: III.I.2.3.8 -->

## 3. The category of O-modules, the category of G-O-modules

**Definition 3.1.** *Let `O` and `F` be two objects of `Ĉ`. One says that `F` is a* `Ĉ`-module *over the `Ĉ`-ring `O`,
or in abbreviated form an* `O`-module, *if, for every `S ∈ Ob(C)`, one has endowed `O(S)` with a ring structure and
`F(S)` with a structure of module over this ring in such a way that, for every arrow `S′ → S″` of `C`, `O(S″) → O(S′)`
is a ring homomorphism and `F(S″) → F(S′)` is a homomorphism of abelian groups compatible with this ring homomorphism.*

<!-- label: III.I.3.1 -->

If `O` is fixed, one defines in the usual way a morphism of the `O`-modules `F` and `F′`, whence the commutative group
`Hom_O(F, F′)`, and the category of `O`-modules, denoted `(O-Mod.)`.

**Lemma 3.1.1.**[^N.D.E-I-27] *`(O-Mod.)` is endowed with a structure of abelian category, defined "argument by
argument". Moreover, `(O-Mod.)` verifies the axiom (AB 5) (cf. [Gr57, 1.5]), i.e. arbitrary direct sums exist, and if
`M` is an `O`-module, `N` a submodule, and `(F_i)_{i∈I}` a directed family of submodules of `M`, then*

```text
⋃_{i∈I} (F_i ∩ N) = (⋃_{i∈I} F_i) ∩ N.
```

<!-- label: III.I.3.1.1 -->

Indeed, let `f : F → F′` be a morphism of `O`-modules. One defines the `O`-modules `Ker f` (resp. `Im f` and `Coker f`)
by setting, for every `S ∈ Ob(C)`, `(Ker f)(S) = Ker f(S)` (resp. ⋯). Then `Ker f` (resp. `Coker f`) is a kernel (resp.
cokernel) of `f`, and one has an isomorphism of `O`-modules `F/ Ker f ⥲ Im f`. This proves that `(O-Mod.)` is an abelian
category.

Arbitrary direct sums exist and are defined "argument by argument". Finally, if `M` is an `O`-module, `N` a submodule,
and `(F_i)_{i∈I}` a directed family of submodules of `M`, then the inclusion

```text
⋃_{i∈I} (F_i ∩ N) ⊂ (⋃_{i∈I} F_i) ∩ N
```

is an equality: indeed, if `S ∈ Ob(C)` and `x ∈ N(S) ∩ ⋃_i F_i(S)`, there exists `i ∈ I` such that `x ∈ N(S) ∩ F_i(S)`.

**Proposition 3.1.2.**[^N.D.E-I-27] *Suppose the category `C` is small, i.e. that `Ob(C)` is a set. Then `(O-Mod.)` has
a generator, and therefore enough injective objects.*

<!-- label: III.I.3.1.2 -->

*Proof.* For every object `S` of `C`, one defines the `O`-module `O_S` as follows. For every object `S′`, `O_S(S′)` is a
direct sum of copies of `O(S′)` indexed by `Hom(S′, S)`, i.e.

```text
O_S(S′) = ⊕_{g : S′ → S} O(S′) g.
```

For every morphism `f : S″ → S′`, denoting `f*` the ring homomorphism `O(S′) → O(S″)`, the morphism
`O_S(f) : O_S(S′) → O_S(S″)` sends each element `a g` of `O_S(S′)` (where

<!-- original page 19 -->

`a ∈ O(S′)` and `g : S′ → S`) to the element `f*(a) g ∘ f` of `O_S(S″)`. One verifies easily that this does define a
functor in `O`-modules.

Since, by hypothesis, `Ob(C)` is a set, one can consider the direct sum `G = ⊕_{S∈Ob(C)} O_S`.

**Lemma 3.1.2.1.** *Let `F` be an `O`-module. For every `S ∈ Ob(C)`, every element `x` of `F(S)` defines a unique
morphism of `O`-modules `x̃ : O_S → F` such that `x̃(1 id_S) = x`.*

<!-- label: III.I.3.1.2.1 -->

*Proof.* Let `φ` be a morphism of `O`-modules `O_S → F` such that `φ(1 id_S) = x`. Let `g : S′ → S` and `a ∈ O(S′)`. The
`O(S′)`-linearity and the commutativity of the diagram

```text
              φ
   O_S(S) ────────→ F(S)
     │              │
   O_S(g)          F(g)
     ↓     φ        ↓
   O_S(S′) ────────→ F(S′)
```

entail that `φ(ag) = a φ(1g) = a F(g)(φ(1 id_S)) = a F(g)(x)`. So `φ`, if it exists, is determined by the previous
equality. Conversely, if one defines `φ` thus, then for every `f : S″ → S′` one has

```text
φ ∘ O_S(f)(ag) = φ(f*(a) g ∘ f) = f*(a) F(g ∘ f)(x) = F(f)(a F(g)(x)) = F(f) ∘ φ(ag)
```

i.e. the diagram

```text
              φ
   O_S(S′) ────────→ F(S′)
     │              │
   O_S(f)          F(f)
     ↓     φ        ↓
   O_S(S″) ────────→ F(S″)
```

is commutative. This proves the lemma.

Now, let `F` be an `O`-module. For every `S ∈ Ob(C)`, let `F_0(S)` be a system of generators of the `O(S)`-module
`F(S)`, and let `L_S` be the direct sum indexed by `F_0(S)` of copies of `O_S`. By the lemma, one obtains a morphism of
`O`-modules `L_S → F`, such that the morphism `L_S(S) → F(S)` is surjective, hence an epimorphism in the category of
`O(S)`-modules.

Set `I = ⨆_{S∈Ob(C)} F_0(S)`. Then one obtains a morphism of `O`-modules

```text
G^{⊕I} ──→ ⊕_{S∈Ob(C)} L_S ──→ F
```

which is "argument by argument" an epimorphism, hence an epimorphism of `(O-Mod.)`. This shows that `G` is a generator
of `(O-Mod.)` (cf. [Gr57, 1.9.1]). Since `(O-Mod.)` verifies (AB 5), it then follows from [Gr57, 1.10.1] that `(O-Mod.)`
has enough injective objects.

**Remark 3.1.3.** *If `O_0` is the `Ĉ`-ring defined by `O_0(S) = ℤ` (which should not be confused with the functor
associated to the constant object `ℤ`), then the category of `O_0`-modules is isomorphic to the category of commutative
`Ĉ`-groups.*

<!-- label: III.I.3.1.3 -->

<!-- original page 20 -->

**Definition 3.1.4.** *Note that, if `F` is an `O`-module, then for every `S ∈ Ob(C)`, `FS` is an `O_S`-module. One can
therefore define a `Ĉ`-abelian group `Hom_O(F, F′)` by*

```text
Hom_O(F, F′)(S) = Hom_{O_S}(FS, F′_S).
```

*One defines similarly the objects*

```text
Isom_O(F, F′),    End_O(F)    and    Aut_O(F),
```

*the last being a `Ĉ`-group for the structure induced by the composition of automorphisms.*

<!-- label: III.I.3.1.4 -->

**Definition 3.2.** *Let `O` be a `Ĉ`-ring, `F` an `O`-module and `G` a `Ĉ`-group. By a* structure of `G`-`O`-module *on
`F` we mean a structure of `G`-object such that for every `S ∈ Ob(C)` and every `g ∈ G(S)`, the automorphism of `F(S)`
defined by `g` is an automorphism of its `O(S)`-module structure.*

<!-- label: III.I.3.2 -->

It amounts to the same thing to say that the morphism of `Ĉ`-groups

```text
ρ : G → Aut(F)
```

defined in 2.3 maps `G` into the sub-`Ĉ`-group `Aut_O(F)` of `Aut(F)`. To give a structure of `G`-`O`-module on the
`O`-module `F` is therefore to give a morphism of `Ĉ`-groups

```text
ρ : G → Aut_O(F).
```

One defines in a natural way the abelian group `Hom_{G-O}(F, F′)`, hence the additive category of `G`-`O`-modules
denoted `(G-O-Mod.)`.

**Remark 3.2.1.** *The reader will note that `(G-O-Mod.)` may also be defined as the category of `O[G]`-modules, where
`O[G]` is the algebra of the `Ĉ`-group `G` over the `Ĉ`-ring `O`, whose definition is clear.[^N.D.E-I-28] Consequently,
by 3.1.1 and 3.1.2, `(G-O-Mod.)` is an abelian category verifying the axiom (AB 5); moreover, if `C` is small,
`(G-O-Mod.)` has enough injective objects.*

<!-- label: III.I.3.2.1 -->

<!-- original page 22 -->

All the constructions of this paragraph specialize at once to the case where `G` (or `O`, or both) are representable by
objects of `C`, which are thereby endowed with the corresponding algebraic structures.

We have treated succinctly the case of the principal algebraic structures encountered in the rest of this seminar. For
the others (structure of `O`-Lie algebra for example), we believe that the reader will have had enough examples in this
paragraph to make the general mechanism sketched in 2.2 work himself in each particular case.

We shall now apply what we have just done to the category of schemes, denoted `(Sch)`, and more generally to the
categories `(Sch)/S` (also denoted `(Sch/S)`).

## 4. Algebraic structures in the category of schemes

We shall allow ourselves, whenever there is no ambiguity, the following abuses of language: one will designate by `T`
the object `T ──f──→ S` of `C/S`, the datum of `f` ("structural morphism of `T`") being understood, and one will
identify `C` with a subcategory of `Ĉ`. Given the compatibilities stated in the preceding paragraphs, these
identifications can be made without danger.

We shall further simplify the terminology along the following model: a `(Sch)`-group will also be called a *group
scheme*, a `(Sch)/S`-group a *group scheme over `S`*, or *`S`-group scheme*, or *`S`-group*, or *`A`-group* when `S` is
the spectrum of the ring `A`.

### 4.1. Constant schemes

The category of schemes satisfies the conditions required in 1.8. One can therefore define constant objects in it; for
every set `E`, one has a scheme `E_ℤ`, and for every scheme `S`, an `S`-scheme `ES = (E_ℤ)_S`. Recall (cf. *loc. cit.*)
that for every `S`-scheme `T`, `Hom_S(T, ES)` is the set of locally constant maps

<!-- original page 23 -->

from the topological space `T` to `E`.

The functor `E ↦ ES` commutes with finite inverse limits. In particular if `G` is a group, `GS` is an `S`-group scheme;
if `O` is a ring, `OS` is an `S`-ring scheme, etc.

### 4.2. Affine S-groups

Let us recall a certain number of things about affine `S`-schemes (EGA II, § 1). One says that the `S`-scheme `T` is
*affine over `S`* if the inverse image of every affine open subset of `S` is affine. The `OS`-algebra `f_*(O_T)`, which
one denotes `A(T)`, is then quasi-coherent (`f` denotes the structural morphism of `T`). Conversely, to every
quasi-coherent `OS`-algebra `A`, one can associate an `S`-scheme affine over `S`, denoted `Spec(A)`. These functors
`T ↦ A(T)` and `A ↦ Spec(A)` are quasi-inverse equivalences between the category of `S`-schemes affine over `S` and the
category opposite to that of quasi-coherent `OS`-algebras.

It follows that to give an algebraic structure on an `S`-scheme `T` affine over `S` is equivalent to giving the
corresponding structure on `A(T)` in the category opposite to that of quasi-coherent `OS`-algebras. In particular, if
`G` is an `S`-group affine over `S`, `A(G)` is endowed with a structure of augmented `OS`-bialgebra, that is, one has
two morphisms of `OS`-algebras

<!-- original page 24 -->

```text
Δ : A(G) → A(G) ⊗_{OS} A(G)    and    ε : A(G) → OS
```

corresponding to the morphisms of `S`-schemes

```text
π : G × G → G    and    e_G : S → G.
```

The maps `Δ` and `ε` satisfy the following conditions (which express that `G` is an `S`-monoid):[^N.D.E-I-29]

**(HA 1)** *`Δ` is co-associative: the following diagram is commutative*

```text
                       A(G) ⊗_{OS} A(G)
                        ╱            ╲
                Δ      ╱              ╲  id ⊗ Δ
                      ╱                ╲
                 A(G)                  A(G) ⊗_{OS} A(G) ⊗_{OS} A(G)
                      ╲                ╱
                       ╲              ╱  Δ ⊗ id
                Δ       ╲            ╱
                       A(G) ⊗_{OS} A(G)
```

**(HA 2)** *`Δ` is compatible with `ε`: the two following composites are the identity*

```text
        Δ                       id ⊗ ε                ∼
A(G) ────→ A(G) ⊗_{OS} A(G) ─────────→ A(G) ⊗_{OS} OS ──→ A(G),

        Δ                       ε ⊗ id                ∼
A(G) ────→ A(G) ⊗_{OS} A(G) ─────────→ OS ⊗_{OS} A(G) ──→ A(G).
```

Let us take this opportunity to note once more that it follows from the definition of an `S`-group structure that to
give such a structure on an `S`-scheme `G` affine over `S`, it is not necessary to verify anything on `A(G)`, but simply
to endow each `G(S′)` for `S′` above `S` with a group structure functorial in `S′`.

<!-- original page 25 -->

This remark applies *mutatis mutandis* to morphisms.

### 4.3. The groups G_a and G_m. The ring O

#### 4.3.1.

Let `G_a` be the functor from `(Sch)°` to `(Ens)` defined by

```text
G_a(S) = Γ(S, OS)
```

endowed with the `(Sch)̂`-group structure defined by the additive group structure of the ring `Γ(S, OS)`. It is
representable by an affine scheme, which we shall denote `G_a`, which is therefore a group scheme

```text
G_a = Spec ℤ[T].
```

Indeed, `G_a(S) = Hom(S, G_a) = Hom_{Alg.}(ℤ[T], Γ(S, OS)) ≃ Γ(S, OS)`.

For every scheme `S`, one therefore has an `S`-group affine over `S`, denoted `G_{a,S}`, which corresponds to the
`OS`-bialgebra `OS[T]`, with the diagonal map and the augmentation defined by:

```text
Δ(T) = T ⊗ 1 + 1 ⊗ T,    ε(T) = 0.
```

#### 4.3.2.

Let `G_m` be the functor from `(Sch)°` to `(Ens)` defined by

```text
G_m(S) = Γ(S, OS)^×,
```

where `Γ(S, OS)^×` denotes the multiplicative group of invertible elements of the ring `Γ(S, OS)`, endowed with its
natural `(Sch)̂`-group structure. It is representable by an affine scheme denoted `G_m`

```text
G_m = Spec ℤ[T, T^{-1}] = Spec ℤ[ℤ],
```

where `ℤ[ℤ]` denotes the algebra of the group `ℤ` over the ring `ℤ`. Indeed,

<!-- original page 26 -->

```text
G_m(S) = Hom_{Alg.}(ℤ[T, T^{-1}], Γ(S, OS)) ≃ Γ(S, OS)^×.
```

For every scheme `S`, one therefore has an `S`-group affine over `S` denoted `G_{m,S}`, which corresponds to the
`OS`-algebra `OS[ℤ]`, with the diagonal map and augmentation defined by:

```text
Δ(x) = x ⊗ x    and    ε(x) = 1,    for x ∈ ℤ.
```

#### 4.3.3.

Let `O` be the functor `G_a` endowed with its `(Sch)̂`-ring structure. It is represented by the scheme `Spec ℤ[T]`,
which we shall denote `O` when considering it as endowed with its ring scheme structure.

For every scheme `S`, `OS = S ×_{Spec ℤ} Spec ℤ[T] = Spec(OS[T])` is therefore an `S`-ring scheme, affine over `S`.
(Note: in EGA II 1.7.13, `OS` is denoted `S[T]`).

#### 4.3.3.1.

[^N.D.E-I-30] For every object `X` of `(Sch)̂`, `O(X) = Hom(X, O)` is endowed with a ring structure, functorial in `X`.
In particular, if `X′` is a scheme and one is given morphisms `x : X′ → X` and `f : X → O` (i.e. `f ∈ O(X)`), then
`f(x) = f ∘ x` is an element of `O(X′) = Γ(X′, O_{X′})`.

**Definition.** *Let `π : M → X` be a morphism of `(Sch)̂`, and let `OX = O × X`. One says that `M` is an `OX`-module if
one has given, for every `X`-scheme `X′`, a structure of `O(X′)`-module on `Hom_X(X′, M)`, functorial in `X′`.*

This amounts to giving a law of `X`-abelian group `μ : M ×_X M → M` and an "external law"

```text
O × M = OX ×_X M → M,    (f, m) ↦ f ⋅ m
```

which is an `X`-morphism (i.e. `π(f ⋅ m) = π(m)`) and which, for every `x ∈ X(S)`, endows `M(x) = {m ∈ M(S) | π(m) = x}`
with a structure of `O(S)`-module.

In this case, for every `Y ∈ Ob (Sch)̂_{/X}` (not necessarily representable), `Hom_X(Y, M) = Γ(M_Y/Y)` is an
`O(Y)`-module, functorially in `Y`.

### 4.4. Diagonalizable groups

#### 4.4.1.

The construction of `G_m` generalizes as follows: let `M` be a commutative group and `M_ℤ` the group scheme associated
to it by the procedure of 4.1. Consider the functor defined by

```text
D(M)(S) = Hom_{groups}(M, G_m(S)) ≃ Hom_{S-Gr.}(MS, G_{m,S}).
```

<!-- original page 27 -->

It is a commutative `(Sch)̂`-group representable by a group scheme that one will denote `D(M)`; one will therefore have
by definition:

```text
D(M) ≃ Hom_{(Sch)-Gr.}(M_ℤ, G_m).
```

Set in fact

```text
D(M) = Spec ℤ[M],
```

where `ℤ[M]` is the algebra of the group `M` over the ring `ℤ`; one has

```text
D(M)(S) = Hom_{Alg.}(ℤ[M], Γ(S, OS)) ≃ Hom_{groups}(M, Γ(S, OS)^×)
```

by the very definition of the algebra `ℤ[M]`.

#### 4.4.2.

For every scheme `S` one therefore has an `S`-group scheme affine over `S`

```text
D_S(M) = D(M)_S = Hom_{(Sch)-Gr.}(M_ℤ, G_m)_S = Hom_{S-Gr.}(MS, G_{m,S}).
```

It is associated to the `OS`-bialgebra `OS[M]`, endowed with the diagonal map and augmentation defined by

```text
Δ(x) = x ⊗ x    and    ε(x) = 1,    for x ∈ M.
```

#### 4.4.3.

If `f : M → N` is a homomorphism of commutative groups, one defines in an obvious manner a morphism of `S`-groups

```text
D_S(f) : D_S(N) → D_S(M),
```

whence a functor

```text
D_S : M ↦ D_S(M)
```

from the category of abelian groups to the category of `S`-groups affine over `S`, which one may also define as the
composite of the functor `M ↦ MS` and of the functor `MS ↦ Hom_{S-Gr.}(MS, G_{m,S})`. This functor commutes with
extensions of the base.

<!-- original page 28 -->

An `S`-group isomorphic to a group of the form `D_S(M)` is said to be *diagonalizable*. Note that the elements of `M`
are interpreted as certain characters of `D_S(M)`, that is, certain elements of `Hom_{S-Gr.}(D_S(M), G_{m,S})`. (Confer
VIII 1).

#### 4.4.4.

Let us give some examples of diagonalizable groups. One has first

```text
D(ℤ) = G_m    and    D(ℤ^r) = (G_m)^r.
```

One sets

```text
μ_n = D(ℤ/nℤ),
```

and calls it the *group of `n`-th roots of unity*. Indeed, one has

```text
μ_n(S) = Hom_{groups}(ℤ/nℤ, Γ(S, OS)^×) = {f ∈ Γ(S, OS) | f^n = 1}.
```

The `S`-group `μ_{n,S}` corresponds to the `OS`-algebra `OS[T]/(T^n - 1)`. Suppose in particular that `S` is the
spectrum of a field `k` of characteristic `p = n`. Setting `T - 1 = s`, one finds

```text
k[T]/(T^p - 1) = k[s]/(s^p),
```

which shows that the underlying topological space of `μ_{p,k}` reduces to a point, the local ring of this point being
the artinian `k`-algebra `k[s]/(s^p)`. (In the same vein, let us note that the `S`-schemes `G_{a,S}, G_{m,S}, OS` are
smooth over `S`, that `D_S(M)` is

<!-- original page 29 -->

flat over `S` and that it is formally smooth (resp. smooth) over `S` if and only if no residue characteristic of `S`
divides the torsion of `M` (resp. and if moreover `M` is of finite type), cf. Exp. VIII, 2.1).

### 4.5. Other examples of groups

The preceding procedure applies to the "classical groups" (linear groups `GL_n`, symplectic `Sp_n`, orthogonal `O_n`,
etc.). One defines for example `GL_n` as representing the functor `GL_n` such that:

```text
GL_n(S) = GL(n, Γ(S, OS)) = Aut_{OS}(OS^n).
```

One can construct it for example as the open subscheme of `Spec ℤ[T_{ij}]` (`1 ⩽ i, j ⩽ n`) defined by the function
`f = det((T_{ij})_{i,j=1}^n)`, that is, `Spec ℤ[T_{ij}, f^{-1}]`.

### 4.6. Functor-modules in the category of schemes

We propose to associate to every `OS`-module on the scheme `S` an `OS`-module (where `OS` denotes the functor-ring
introduced in 4.3.3). This can be done in two different ways. Precisely:

**Definition 4.6.1.** *Let `S` be a scheme. For every `OS`-module `F` one denotes by `V(F)` and `W(F)` the contravariant
functors on `(Sch)/S` defined by:*

```text
V(F)(S′) = Hom_{O_{S′}}(F ⊗_{OS} O_{S′}, O_{S′}),
W(F)(S′) = Γ(S′, F ⊗_{OS} O_{S′})
```

*(where `F ⊗_{OS} O_{S′}` denotes the inverse image on `S′` of the `OS`-module `F`).*

<!-- label: III.I.4.6.1 -->

Then `V(F)` and `W(F)` are endowed in an obvious manner with a structure of `OS`-modules (recall that
`OS(S′) = Γ(S′, O_{S′}) = W(OS)(S′)`), in such a way that one has in fact defined two functors `V` and `W` from the
category of `OS`-modules to the category of `OS`-modules, with `V` contravariant and `W` covariant.

We restrict ourselves in the rest of this paragraph to the case where the `OS`-modules in question are quasi-coherent,
that is, we consider `V` and `W` as

<!-- original page 30 -->

functors from the category `(OS-Mod.q.c.)` of quasi-coherent `OS`-modules to the category of `OS`-modules

```text
V : (OS-Mod.q.c.)° → (OS-Mod.),
W : (OS-Mod.q.c.) → (OS-Mod.).
```

**Remark 4.6.1.1.**[^N.D.E-I-31] *The reader will note that, in what follows, all the propositions involving only the
functor `W` are valid for arbitrary `OS`-modules, not necessarily quasi-coherent.*

<!-- label: III.I.4.6.1.1 -->

**Proposition 4.6.2.** *(i) The functors `V` and `W` commute with base extension: if `S′` is above `S` and if `F` is a
quasi-coherent `OS`-module, one has*

```text
V(F ⊗ O_{S′}) ≃ V(F)_{S′}    and    W(F ⊗ O_{S′}) ≃ W(F)_{S′}.
```

*(ii) The functors `V` and `W` are fully faithful: the canonical maps*

```text
Hom_{OS}(F, F′) → Hom_{OS}(V(F′), V(F))
Hom_{OS}(F, F′) → Hom_{OS}(W(F), W(F′))
```

*are bijective.*

*(iii) The functors `V` and `W` are additive:*

```text
V(F ⊕ F′) ≃ V(F) ×_S V(F′)    and    W(F ⊕ F′) ≃ W(F) ×_S W(F′).
```

<!-- label: III.I.4.6.2 -->

Parts (i) and (iii) are obvious from the definitions. For (ii), one takes for `S′` open subschemes of `S`. We leave the
proof to the reader (for `V`, use EGA II, 1.7.14).

Recall (cf. 3.1.4) that if `F, F′` are `OS`-modules, `Hom_{OS}(F, F′)` denotes the `S`-functor (in abelian groups) which
to every `S′ → S` associates `Hom_{O_{S′}}(F_{S′}, F′_{S′})`.

**Proposition 4.6.3.**[^N.D.E-I-32] *One has canonical morphisms in `(OS-Mod.)`:*

```text
                        W(Hom_{OS}(F, F′))
                        ╱             ╲
                       ↙               ↘
   Hom_{OS}(W(F), W(F′))           Hom_{OS}(V(F′), V(F))
```

<!-- label: III.I.4.6.3 -->

<!-- original page 31 -->

This follows immediately from 4.6.2 (i) and (ii).

**Notation 4.6.3.1.** *Let `F` be a quasi-coherent `OS`-module. One knows (EGA II, 1.7.8) that the `S`-functor `V(F)` is
representable by an `S`-scheme affine over `S` which one denotes `V(F)` and calls the* vector fibration[^N.D.E-I-33]
*defined by `F`:*

```text
V(F) = Spec(S(F)),
```

*where `S(F)` denotes the symmetric algebra of the `OS`-module `F`.[^N.D.E-I-34]*

<!-- label: III.I.4.6.3.1 -->

**Proposition 4.6.4.** *Let `F` and `F′` be two quasi-coherent `OS`-modules, `A` a quasi-coherent `OS`-algebra. One has
a functorial isomorphism:*

```text
Hom_S(Spec(A), Hom_{OS}(W(F′), W(F))) ⥲ Hom_{OS}(F′, F ⊗_{OS} A).
```

<!-- label: III.I.4.6.4 -->

Indeed, denoting `X = Spec(A)`, the first member is canonically isomorphic to `Hom_{OS}(W(F′), W(F))(X)`, that is, by
definition, to

```text
Hom_{OX}(W(F′)_X, W(F)_X) ≃ Hom_{OX}(W(F′ ⊗ O_X), W(F ⊗ O_X))
```

(cf. 4.6.2 (i)), which by 4.6.2 (ii) can also be written

<!-- original page 32 -->

```text
Hom_{OX}(F′ ⊗ O_X, F ⊗ O_X) = Hom_{OS}(F′, π_*(π*(F))),
```

where one denotes `π : X → S` the structural morphism. But, by EGA II, 1.4.7, one has `π_*(π*(F)) ≃ F ⊗ A`, which
completes the proof.

**Corollary 4.6.4.1.** *One has a canonical isomorphism*

```text
W(F ⊗ A) ≃ Hom_S(Spec(A), W(F)).
```

<!-- label: III.I.4.6.4.1 -->

Indeed,[^N.D.E-I-35] let `f : S′ → S` be an `S`-scheme and `X′ = X ×_S S′`; one has a cartesian square

```text
              f′
   X′ ───────→ X
   │           │
   π′          π
   ↓     f     ↓
   S′ ───────→ S
```

and by EGA II, 1.5.2, `X′` is affine over `S′` and `π′_*(O_{X′}) = f*(A)`. One has therefore

```text
Hom_S(Spec(A), W(F))(S′) = Hom_{S′}(Spec(f*(A)), W(f*(F)))
```

and by 4.6.4 applied to `f*(F)`, `F′ = O_{S′}` and `f*(A)`, this equals

```text
Γ(S′, f*(F) ⊗ f*(A)) = Γ(S′, f*(F ⊗ A)) = W(F ⊗ A)(S′).
```

**Proposition 4.6.5.** *If `F` and `F′` are two `OS`-modules locally free of finite type, the morphisms of 4.6.3 are
isomorphisms.*

<!-- label: III.I.4.6.5 -->

Indeed, for every `S′ → S`, one has

```text
W(Hom_{OS}(F, F′))(S′) = Γ(S′, Hom_{OS}(F, F′) ⊗ O_{S′}) = Hom_{O_{S′}}(F ⊗ O_{S′}, F′ ⊗ O_{S′}).
```

But the second member is indeed isomorphic to `Hom_{OS}(W(F), W(F′))(S′)` and to `Hom_{OS}(V(F′), V(F))(S′)`, by 4.6.2
(i) and (ii).

**Corollary 4.6.5.1.** *Let `F` be an `OS`-module locally free of finite type. Set `F^∨ = Hom_{OS}(F, OS)`. One has
canonical isomorphisms:*

<!-- original page 33 -->

```text
W(F^∨) ≃ Hom_{OS}(W(F), OS) ≃ V(F),
V(F^∨) ≃ Hom_{OS}(V(F), OS) ≃ W(F).
```

<!-- label: III.I.4.6.5.1 -->

One has finally the following proposition:

**Proposition 4.6.6.** *Let `f : F → F′` be a morphism of `OS`-modules locally free of finite rank. For
`W(f) : W(F) → W(F′)` to be a monomorphism, it is necessary and sufficient that `f` identify `F` locally with a direct
factor of `F′`.*

<!-- label: III.I.4.6.6 -->

The direct proposition is essentially contained in EGA 0_I, 5.5.5.[^N.D.E-I-36] Conversely, if `F` is locally a direct
factor of `F′`, then for every `π : S′ → S`, `π* F` is a submodule of `π* F′` (because locally a direct factor), so
`W(F)(S′) = Γ(S′, π* F)` is a submodule of `W(F′)(S′) = Γ(S′, π* F′)`.

### 4.7. The category of G-OS-modules

Let `G` be an `S`-group and `F` an `OS`-module; `W(F)` is endowed with a structure of `OS`-module.

**Definition 4.7.1.** *By a* structure of `G`-`OS`-module on `F` *we mean a structure of `hG`-`OS`-module on `W(F)` (cf.
3.2). A morphism of `G`-`OS`-modules is by definition a morphism of the associated `hG`-`OS`-modules. One thus obtains
the category `(G-OS-Mod.)`, and one denotes `(G-OS-Mod.q.c.)` the full subcategory formed by the `G`-`OS`-modules that
are quasi-coherent as `OS`-modules.*

<!-- label: III.I.4.7.1 -->

To give a structure of `G`-`OS`-module on `F` is therefore, by 3.2, to give a morphism of `(Sch)̂_{/S}`-groups

```text
ρ : hG → Aut_{OS}(W(F)).
```

**Remark 4.7.1.0.**[^N.D.E-I-37] *Since by 4.6.2 one has an anti-isomorphism of `S`-functors in groups*

```text
(†)    Aut_{OS}(W(F)) ≃ Aut_{OS}(V(F)),
```

*one sees that it is equivalent to give a structure of `hG`-`OS`-module on `W(F)` or on `V(F)`.* Indeed, let
`ρ : hG → Aut_{OS}(W(F))` be as above. For every `T → S` and `g ∈ G(T)`, denote by `ρ*(g)` the image of `ρ(g)` by the
anti-isomorphism `(†)`; one has therefore `ρ*(gh) = ρ*(h) ∘ ρ*(g)`, i.e. `ρ*` defines a structure of `hG`-`OS`-module
"on the right" on `V(F)`. Setting `ρ^∨(g) = ρ*(g^{-1})`, one obtains indeed a structure of `hG`-`OS`-module on `V(F)`,
the datum of which is equivalent to that of `ρ`.

<!-- label: III.I.4.7.1.0 -->

**Remark 4.7.1.1.** One can say that one has constructed the categories one has just defined by the cartesian squares:

```text
                        ───→ (G-OS-Mod.) ───→ (hG-OS-Mod.)
   (G-OS-Mod.q.c.)
                                                   │
                                                  forget
                              W                    ↓
   (OS-Mod.q.c.) ─────→ (OS-Mod.) ──────→ (OS-Mod.).
```

<!-- label: III.I.4.7.1.1 -->

[^N.D.E-I-38] The categories `(OS-Mod.)` and `(OS-Mod.)` are abelian, but one should be careful that in general the
functor `W` is neither left nor right exact.

<!-- original page 34 -->

**Remark 4.7.1.2.**[^N.D.E-I-39] Let `F` be a `G`-`OS`-module. The subsheaf of invariants `F^G` is defined as follows:
for every open subset `U` of `S`,

```text
F^G(U) = W(F)^G(U) = {x ∈ F(U) | g ⋅ x_{S′} = x_{S′} for every S′ ──f──→ U, g ∈ G(S′)},
```

where `x_{S′}` denotes the image of `x` in `Γ(S′, f*(F)) = Γ(U, f_* f*(F))`.

One should be careful that the natural morphism `W(F^G) → W(F)^G` is not in general an isomorphism. For example, if
`S = Spec(ℤ)` and `G` is the constant group `ℤ/2ℤ = {1, τ}` acting on `F = OS` by `τ ⋅ 1 = -1`, one has `F^G = 0` but,
if `R` is an `F_2`-algebra, `W(F)^G(Spec(R)) = R`.

<!-- label: III.I.4.7.1.2 -->

#### 4.7.2.

We suppose from now until the end of n° 4.7 that `G` is affine over `S`.[^N.D.E-I-40] Then, by virtue of 4.6.4, the
datum of a morphism of `S`-functors

```text
ρ : hG → End_{OS}(W(F))
```

is equivalent to that of a morphism of `OS`-modules

```text
μ : F → F ⊗_{OS} A(G).
```

To say that `ρ` is a morphism of `(Sch)̂_{/S}`-groups is then equivalent to saying that `μ` satisfies the following
axioms:

**(CM 1)** *the following diagram is commutative*

```text
              μ
   F ────────────→ F ⊗_{OS} A(G)
   │                   │
   μ                  id ⊗ Δ
   ↓     μ ⊗ id        ↓
   F ⊗_{OS} A(G) ──→ F ⊗_{OS} A(G) ⊗_{OS} A(G).
```

**(CM 2)** *the following composite is the identity*

```text
        μ                       id ⊗ ε              ∼
F ────────→ F ⊗ A(G) ──────────→ F ⊗ OS ────────→ F.
```

These axioms (CM 1) and (CM 2) are those of a (right) comodule structure[^N.D.E-I-41] over the bialgebra `A(G)`.

Set `A = A(G)`. If `F` and `F′` are `A`-comodules, a morphism of comodules `f : F → F′` is a morphism of `OS`-modules
such that the following diagram is

<!-- original page 30 -->

commutative:

```text
              f
   F ────────────→ F′
   │              │
   μ_F           μ_{F′}
   ↓     f ⊗ id   ↓
   F ⊗ A ──────→ F′ ⊗ A.
```

One thus obtains the category `(A-Comod.)`, and one will denote by `(A-Comod.q.c.)` the full subcategory formed by the
`A`-comodules that are quasi-coherent as `OS`-modules. One has thus obtained:

**Proposition 4.7.2.** *Let `G` be an `S`-group affine over `S`. One has equivalences of categories:*

```text
(G-OS-Mod.) ≅ (A(G)-Comod.)
(G-OS-Mod.q.c.) ≅ (A(G)-Comod.q.c.)
```

<!-- label: III.I.4.7.2 -->

[^N.D.E-I-42] *If moreover `S = Spec(Λ)` is affine and if one denotes `Λ[G] = Γ(S, A(G))`, one has an equivalence of
categories*

```text
(A(G)-Comod.q.c.) ≅ (Λ[G]-Comod.).
```

[^N.D.E-I-43] Suppose moreover that `A = A(G)` is a flat `OS`-module. Let `E` be an `A`-comodule and `F` a
sub-`OS`-module of `E`. Since `A` is flat over `OS`, one can identify `F ⊗ A` (resp. `F ⊗ A ⊗ A`) with a sub-`OS`-module
of `E ⊗ A` (resp. `E ⊗ A ⊗ A`). Suppose that `μ_E` maps `F` into `F ⊗ A`; then its restriction `μ_F : F → F ⊗ A` endows
`F` with a structure of `A`-comodule; one says that `F` is a *subcomodule* of `E`. By passage to the quotient, `μ_E`
defines a morphism of `OS`-modules `E/F → E/F ⊗ A`, which endows `E/F` with a structure of `A`-comodule. If `f : E → E′`
is a morphism of `A`-comodules, `Ker f` (resp. `Im f`) is a sub-`A`-comodule of `E` (resp. `E′`), and `f` induces an
isomorphism of `A`-comodules: `E/Ker f ⥲ Im f`. Moreover, if `E` and `E′` are quasi-coherent `OS`-modules, so are
`Ker f` and `Im f`. Consequently, `(A-Comod.)` and `(A-Comod.q.c.)` are abelian categories.

**Corollary 4.7.2.1.** *Suppose that `G` is affine and flat over `S`. Then the category `(G-OS-Mod.q.c.)` (resp.
`(G-OS-Mod.)`), equivalent to the category of `A(G)`-comodules quasi-coherent over `OS` (resp. `A(G)`-comodules), is
abelian.*

<!-- label: III.I.4.7.2.1 -->

#### 4.7.3.

Suppose now that `G` is a diagonalizable group, that is, that `A(G)` is the algebra of a commutative group `M` over the
sheaf of rings `OS`. If `F` is an `OS`-module, one has

```text
F ⊗ A(G) = ⨆_{m ∈ M} F ⊗ m OS.
```

To give a morphism of `OS`-modules

```text
μ : F → F ⊗ A(G)
```

<!-- original page 31 -->

is therefore equivalent to giving `OS`-endomorphisms `(μ_m)_{m ∈ M}` of `F`, such that for every section `x` of `F` on
an open subset of `S`, `(μ_m(x))` is a section of the direct sum `⨆_{m ∈ M} F` (this means that on every sufficiently
small open subset, there are only finitely many restrictions of the `μ_m(x)` that are nonzero).

For `μ` defined by

```text
μ(x) = ∑_{m ∈ M} μ_m(x) ⊗ m
```

to satisfy (CM 1) (resp. (CM 2)) it is necessary and sufficient that one have

```text
μ_m ∘ μ_{m′} = δ_{mm′} μ_m,    (resp. ∑_{m ∈ M} μ_m = Id_F),
```

which means that the `μ_m` are pairwise orthogonal projectors with sum the identity. One has thus proved:

**Proposition 4.7.3.** *If `G = D_S(M)` is a diagonalizable `S`-group, the category of quasi-coherent `G`-`OS`-modules
(resp. of `G`-`OS`-modules) is equivalent to the category of quasi-coherent `OS`-modules (resp. of `OS`-modules) graded
of type `M`.*

<!-- label: III.I.4.7.3 -->

**Remark.** If `F` is endowed with a structure of `OS`-algebra preserved by the operations of `G`, then the gradation of
`F` is a gradation of algebra. More precisely:

**Corollary 4.7.3.1.** *The functor `A ↦ Spec A` induces an equivalence between the category of quasi-coherent
`OS`-algebras graded of type `M` and the category opposite to that of `S`-schemes affine over `S` with `S`-operator
group `G = D_S(M)`.*

<!-- label: III.I.4.7.3.1 -->

**Proposition 4.7.4.** *Let `G` be a diagonalizable `S`-group. If `0 → F_1 → F_2 → F_3 → 0` is an exact sequence of
quasi-coherent `G`-`OS`-modules that splits as a sequence of `OS`-modules, then it also splits as a sequence of
`G`-`OS`-modules.*

<!-- label: III.I.4.7.4 -->

Indeed, if `G = D_S(M)`, each `F_i` is graded by the `(F_i)_m`, and for each `m ∈ M` the sequence

```text
0 → (F_1)_m → (F_2)_m → (F_3)_m → 0
```

of `OS`-modules is split. The preceding proposition then entails the result.

## 5. Group cohomology

<!-- original page 37 -->

### 5.1. The standard complex

[^N.D.E-I-44] Let `C` be a category, `G` a `Ĉ`-group, `O` a `Ĉ`-ring, and `F` a `G`-`O`-module. One sets, for `n ⩾ 0`,

```text
C^n(G, F) = Hom(G^n, F)    and    C^n(G, F) = Hom(G^n, F),
```

where `G^0` is the final object `e`. Then `C^n(G, F)` (resp. `C^n(G, F)`) is endowed in an obvious manner with a
structure of `O`-module (resp. of `Γ(O)`-module), and one has

```text
C^n(G, F) ≅ Γ(C^n(G, F))    and    C^n(G, F)(S) = C^n(GS, FS).
```

<!-- original page 32 -->

To give an element of `C^n(G, F)` is to give for each `S ∈ Ob(C)` an `n`-cochain of `G(S)` in `F(S)`, functorially in
`S`. The boundary operator

```text
∂ : C^n(G(S), F(S)) → C^{n+1}(G(S), F(S)),
```

which, recall, is given by the formula

```text
∂f(g_1, …, g_{n+1}) = g_1 f(g_2, …, g_{n+1})
                    + ∑_{i=1}^{n} (-1)^i f(g_1, …, g_i g_{i+1}, …, g_{n+1})
                    + (-1)^{n+1} f(g_1, …, g_n),
```

is functorial in `S` and therefore defines a homomorphism:

```text
∂ : C^n(G, F) → C^{n+1}(G, F)
```

<!-- original page 38 -->

such that `∂ ∘ ∂ = 0`. One has thus defined a complex of abelian groups (and even of `Γ(O)`-modules) denoted `C*(G, F)`.
One defines in the same way the complex of `O`-modules `C*(G, F)`, and one has:

```text
C*(G, F) = Γ(C*(G, F)).
```

One denotes by `H^n(G, F)` (resp. `H^n(G, F)`) the groups (resp. the `Ĉ`-groups) of cohomology of the complex `C*(G, F)`
(resp. `C*(G, F)`).

One has in particular

```text
H^0(G, F) = F^G    and    H^0(G, F) = Γ(F^G).
```

**Remark 5.1.1.**[^N.D.E-I-45] *The "set-theoretic" description of `∂` given above is convenient for verifying that
`∂ ∘ ∂ = 0`. One can also define `∂` in terms of the multiplication `m : G × G → G` and the action `μ : G × F → F` as
follows: for every `f ∈ C^n(G, F)`,*

```text
∂f = μ ∘ (id_G × f) + ∑_{i=1}^{n} (-1)^i f ∘ (id_{G^{i-1}} × m × id_{G^{n-i}}) + (-1)^{n+1} f ∘ pr_{[1,n]},
```

*where `pr_{[1,n]}` denotes the projection of `G^{n+1} = G^n × G` onto `G^n`. Similarly, for every `S ∈ Ob(C)` and
`f ∈ C^n(G, F)(S) = C^n(GS, FS)`, one has*

```text
∂f = μ_S ∘ (id_{GS} × f) + ∑_{i=1}^{n} (-1)^i f ∘ (id_{GS^{i-1}} × m_S × id_{GS^{n-i}}) + (-1)^{n+1} f ∘ pr_{[1,n]_S},
```

*where `m_S` and `μ_S` are deduced from `m` and `μ` by base change.*

<!-- label: III.I.5.1.1 -->

### 5.2.

[^N.D.E-I-46] Recall (cf. § 3) that `(G-O-Mod.)` is endowed with a structure of abelian category, defined "argument by
argument"; thus,

```text
0 → F′ → F → F″ → 0
```

is an exact sequence of `G`-`O`-modules if and only if the sequence of abelian groups

```text
0 → F′(S) → F(S) → F″(S) → 0
```

is exact, for every `S ∈ Ob(C)`.

<!-- original page 33 -->

[^N.D.E-I-47] Suppose `C` small; then, by 3.2.1, `(G-O-Mod.)` has enough injective objects, so that the derived functors
of the left exact functors `H^0` and `H^0` are defined. We now propose to show that the functors `H^n` (resp. `H^n`) are
indeed the derived functors of `H^0` (resp. `H^0`).

**Definition 5.2.0.**[^N.D.E-I-48] *For every `O`-module `P`, one denotes by `E(P)` the object `Hom(G, P)` of `Ĉ`
endowed with the structure of `G`-`O`-module defined as follows: for every `S ∈ Ob(C)` one has
`Hom(G, P)(S) = Hom_S(GS, PS)`, and one makes `g ∈ G(S)` and `a ∈ O(S)` operate on `φ ∈ Hom_S(GS, PS)` by the formulas*

```text
(g ⋅ φ)(h) = φ(hg)    and    (a ⋅ φ)(h) = a φ(h),
```

*for every `h ∈ G(S′)`, `S′ → S`. Moreover, for every `φ ∈ Hom_S(GS, PS)` one sets*

```text
ε(φ) = φ(1) ∈ P(S)
```

*(where `1` denotes the unit element of `G(S)`).*

<!-- label: III.I.5.2.0 -->

This defines a functor `E : (O-Mod.) → (G-O-Mod.)` and a natural transformation `ε : E → Id`, where `Id` denotes the
identity functor of `(O-Mod.)`.

**Remark 5.2.0.1.**[^N.D.E-I-48] *In what follows, let us denote by `G_1` and `G_2` two copies of `G`. Then the
morphism*

```text
G_1 × E(P) → E(P),    (g_1, φ) ↦ (g_2 ↦ φ(g_2 g_1))
```

*corresponds via the isomorphisms*

```text
Hom(G_1 × E(P), E(P)) ≃ Hom(E(P), Hom(G_1, Hom(G_2, P)))
                     ≃ Hom(E(P), Hom(G_2 × G_1, P))
```

*to the morphism `φ ↦ ((g_2, g_1) ↦ φ(g_2 g_1))`, i.e. to the morphism*

```text
Hom(G, P) → Hom(G_2 × G_1, P)
```

*induced by the multiplication `μ_G : G × G → G`, `(g_2, g_1) ↦ g_2 g_1`.*

<!-- label: III.I.5.2.0.1 -->

**Lemma 5.2.0.2.**[^N.D.E-I-48] *(i) The functor `E` is right adjoint to the forgetful functor `(G-O-Mod.) → (O-Mod.)`;
more precisely, `ε : E → Id` induces for every `M ∈ (G-O-Mod.)` and `P ∈ Ob(O-Mod.)` a bijection*

```text
Hom_{G-O-Mod.}(M, E(P)) ⥲ Hom_{O-Mod.}(M, P)
```

*functorial in `M` and `P`.*

*(ii) Consequently, if `I` is an injective object of `(O-Mod.)` then `E(I)` is an injective object of `(G-O-Mod.)`.*

<!-- label: III.I.5.2.0.2 -->

<!-- original page 34 -->

*Proof.* To every `O`-morphism `f : M → P`, one associates the element `φ_f` of `Hom_O(M, E(P))` defined as follows. For
every `S ∈ Ob(C)` and `m ∈ M(S)`, `φ_f(m)` is the element of `Hom_S(GS, PS)` defined by: for every `g ∈ G(S′)`,
`S′ → S`,

```text
φ_f(m)(g) = f(g m) ∈ P(S′).
```

Then, for every `h ∈ G(S)`, one has `φ_f(h m) = h ⋅ f(m)`, i.e. `φ_f` is an element of

```text
Hom_{G-O-Mod.}(M, E(P)).
```

If `φ ∈ Hom_{G-O-Mod.}(M, E(P))` and if one denotes, for every `m ∈ M(S)`, `f(m) = φ(m)(1)`, then

```text
φ_f(m)(g) = f(g m) = φ(g m)(1) = (g ⋅ φ(m))(1) = φ(m)(g),
```

i.e. `φ_f = φ`. Conversely, it is clear that `φ_f(m)(1) = f(m)`. This proves (i), and (ii) follows at once.

**Definition 5.2.0.3.** *Let `M` be a `G`-`O`-module; the identity map of `M` (considered as an `O`-module) corresponds
by adjunction to the morphism of `G`-`O`-modules*

```text
μ_M : M → E(M)
```

*such that for every `S ∈ Ob(C)` and `m ∈ M(S)`, `μ_M(m)` is the morphism `GS → MS` defined by: for every `S′ → S` and
`g ∈ G(S′)`, `μ_M(m)(g) = g ⋅ m_{S′} ∈ M(S′)`.*

<!-- label: III.I.5.2.0.3 -->

Note that `μ_M` is a monomorphism. Indeed, `ε_M : E(M) → M` is a morphism of `O`-modules such that `ε_M ∘ μ_M = id_M`;
consequently `M` is a direct factor, as an `O`-module, of `E(M)`.

<!-- original page 39 -->

**Proposition 5.2.1.** *Suppose that `C` is small, that finite products exist in it, and that `G` is representable.
Then, the functors `H^n(G, −)` (resp. `H^n(G, −)`) are the derived functors of the left exact functor `H^0(G, −)` (resp.
`H^0(G, −)`) on the category of `G`-`O`-modules.*

<!-- label: III.I.5.2.1 -->

By virtue of the well-known general results,[^N.D.E-I-49] it suffices to verify that the `H^n(G, −)` (resp. `H^n(G, −)`)
form an effaceable cohomological functor in degrees `> 0`.

Let

```text
0 → F′ → F → F″ → 0
```

be an exact sequence of `G`-`O`-modules, and let `S ∈ Ob(C)`. By hypothesis, `G` is representable by an object
`G ∈ Ob(C)`, and finite products exist in `C`; in particular `C` has a final element `e`. Hence each `G^n × hS` is
representable by `G^n × S` (with `G^0 = e`), and the sequence

```text
0 → F′(G^n × S) → F(G^n × S) → F″(G^n × S) → 0
```

is exact. This shows that the sequence of `O`-modules

```text
0 → C^n(hG, F′) → C^n(hG, F) → C^n(hG, F″) → 0
```

is exact. It follows that `C*(G, −)`, considered as a functor on `(G-O-Mod.)` with values in the category of complexes
of `(O-Mod.)`, is exact. This shows that the

<!-- original page 35 -->

`H^n(G, −)` indeed form a cohomological functor. Since the functor `Γ` is exact, the same is true for the `H^n(G, −)`.
It will now suffice to prove:

**Lemma 5.2.2.** *For every `P ∈ Ob(O-Mod.)`, one has:*

```text
H^n(G, Hom(G, P)) = 0    and    H^n(G, Hom(G, P)) = 0, for n > 0.
```

<!-- label: III.I.5.2.2 -->

It suffices to prove that `C*(G, Hom(G, P))` and `C*(G, Hom(G, P))` are homotopically trivial in degrees `> 0`. It
suffices even to do this for the second, the corresponding result for the first being deduced from it by base
change.[^N.D.E-I-50] Now, one defines for every `n ⩾ 0` a morphism

```text
σ : C^{n+1}(G, Hom(G, P)) → C^n(G, Hom(G, P))
```

as follows. Let `f ∈ C^{n+1}(G, Hom(G, P))`; for every `S ∈ Ob(C)` and `g_1, …, g_n ∈ G(S)`, `σ(f)(g_1, …, g_n)` is the
element of `Hom_S(GS, PS)` defined by: for every `S′ → S` and `x ∈ G(S′)`,

```text
σ(f)(g_1, …, g_n)(x) = f(x, g_1, …, g_n)(e) ∈ P(S′)
```

(where `e` denotes the unit element of `G(S′)`). Then, `σ` is a homotopy operator in degrees `> 0`. Indeed, for every
`g_1, …, g_{n+1} ∈ G(S)` and `x ∈ G(S′)` one has, on the one hand:

```text
∂σ(f)(g_1, …, g_{n+1})(x) = f(x g_1, g_2, …, g_{n+1})(e)
                          + ∑_{i=1}^{n} (-1)^i f(x, g_1, …, g_i g_{i+1}, …, g_{n+1})(e)
                          + (-1)^{n+1} f(x, g_1, …, g_n)(e),
```

and on the other hand:

```text
σ(∂f)(g_1, …, g_{n+1})(x) = (x f(g_1, g_2, …, g_{n+1}))(e) - f(x g_1, g_2, …, g_{n+1})(e)
                          + ∑_{i=1}^{n} (-1)^{i+1} f(x, g_1, …, g_i g_{i+1}, …, g_{n+1})
                          + (-1)^{n+2} f(x, g_1, …, g_n)(e),
```

whence

```text
(∂σ(f) + σ(∂f))(g_1, …, g_{n+1})(x) = f(g_1, …, g_{n+1})(x),
```

i.e. `∂σ + σ∂` is the identity map of `C^{n+1}(G, Hom(G, P))`, for every `n ⩾ 0`.

**Remark 5.2.3.**[^N.D.E-I-51] *The hypothesis "`C` small" is used only to ensure the existence of the derived functors
`R^n H^0` and `R^n H^0`. In any case, the foregoing shows that the functors `H^n(G, −)` (resp. `H^n(G, −)`) form a
cohomological functor, effaceable in degrees `> 0`, hence they are the (right) satellite functors of the left exact
functor `H^0(G, −)` (resp. `H^0(G, −)`), in the sense of [Gr57, 2.2]; if `(G-O-Mod.)` has enough injective objects
(which is the case if `C` is small), they coincide with the derived functors (*loc. cit.* 2.3).*

<!-- label: III.I.5.2.3 -->

<!-- original page 36 -->

### 5.3. Cohomology of G-OS-modules

Let `S` be a scheme, `G` an `S`-group, and `F` a quasi-coherent `G`-`OS`-module. One defines the cohomology groups of
`G` with values in `F` by

```text
H^n(G, F) = H^n(hG, W(F)).
```

(for the notations, cf. 4.6).

<!-- original page 40 -->

Suppose `G` is affine over `S`. Then, in view of Proposition 4.6.4, this cohomology is computed as follows: `H^n(G, F)`
is the `n`-th homology group of the complex `C*(G, F)` whose `n`-th term is:

```text
C^n(G, F) = Γ(S, F ⊗ A(G) ⊗ ⋯ ⊗ A(G))
                       └────── n times ──────┘
```

If `f` (resp. `a_i`) is a section of `F` (resp. of `A(G)`) on an open subset of `S`, one has

```text
∂(f ⊗ a_1 ⊗ ⋯ ⊗ a_n) = μ_F(f) ⊗ a_1 ⊗ a_2 ⊗ ⋯ ⊗ a_n
                     + ∑_{i=1}^{n} (-1)^i f ⊗ a_1 ⊗ ⋯ ⊗ Δ a_i ⊗ ⋯ ⊗ a_n
                     + (-1)^{n+1} f ⊗ a_1 ⊗ a_2 ⋯ ⊗ a_n ⊗ 1,
```

where `Δ : A(G) → A(G) ⊗ A(G)` and `μ_F : F → F ⊗ A(G)` describe the coalgebra structure of `A(G)` and the comodule
structure of `F`. Note in passing that the cohomology of `G` with values in `F` therefore depends only on the comodule
structure of `F`, and in particular only on the `S`-monoid structure of `G`.

One has in particular

```text
H^0(G, F) = Γ(S, F^G),
```

where `F^G`, the *sheaf of invariants of `F`*, is defined as the sheaf whose sections on the open subset `U` of `S` are
the sections of `F` on `U` whose inverse image in any `S′` over `U` is invariant under `G(S′)` (cf. 4.7.1.2).

<!-- original page 41 -->

**Theorem 5.3.1.** *Let `S` be an affine scheme, `G` an `S`-group affine and flat over `S`. The functors `H^n(G, −)` are
the derived functors of `H^0(G, −)` on the category of quasi-coherent `G`-`OS`-modules.*

<!-- label: III.I.5.3.1 -->

*Proof.*[^N.D.E-I-52] Since `G` is affine and flat over `S`, by 4.7.2.1, the category `(G-OS-Mod.q.c.)` is equivalent to
the category `(A(G)-Comod.q.c.)` of `A(G)`-comodules quasi-coherent over `OS`, and is therefore abelian. On the other
hand, `A(G)` being a flat `OS`-module, each functor `F ↦ F ⊗_{OS} A(G)^{⊗n}` is exact; since moreover `S` is affine, one
obtains that `C*(G, −)` is an exact functor on `(G-OS-Mod.q.c.)`.

Denote by `Δ` (resp. `η`) the comultiplication (resp. the augmentation) of `A(G)`. For every quasi-coherent `OS`-module
`P`, one denotes `Ind(P) = P ⊗_{OS} A(G)` endowed with the structure of `A(G)`-comodule defined by

```text
id_P ⊗ Δ : P ⊗_{OS} A(G) → P ⊗_{OS} A(G) ⊗_{OS} A(G);
```

<!-- original page 37 -->

this defines a functor `Ind : (OS-Mod.q.c.) → (G-OS-Mod.q.c.)`.

It follows from 4.6.4.1, 5.2.0, and 5.2.0.1 that one has an isomorphism of `G`-`OS`-modules:

```text
(∗)    W(Ind(P)) ≃ E(W(P)) = Hom(G, W(P)).
```

<!-- label: eq:III.I.5.3.1-star -->

Via this identification, the morphism `ε : E(W(P)) → W(P)` corresponds to the morphism of `OS`-modules
`id_P ⊗ η : Ind(P) → P`.

One has already used that the functor `W : (OS-Mod.) → (OS-Mod.)` is fully faithful; the same is true, by Definition
4.7.1, of its restriction to `(G-OS-Mod.)`, i.e. if `M, M′` are `G`-`OS`-modules, one has a functorial isomorphism

```text
Hom_{G-OS-Mod.}(M, M′) ≃ Hom_{G-OS-Mod.}(W(M), W(M′)).
```

Consequently, one deduces from Lemma 5.2.0.2 the following:

**Corollary 5.3.1.1.** *(i) The functor `Ind` is right adjoint to the forgetful functor
`(G-OS-Mod.q.c.) → (OS-Mod.q.c.)`. More precisely, the map `id_P ⊗ η : Ind(P) → P` induces for every object `M` of
`(G-OS-Mod.q.c.)` a bijection*

```text
Hom_{G-OS-Mod.}(M, Ind(P)) ⥲ Hom_{OS}(M, P).
```

*(ii) Consequently, if `I` is an injective object of `(OS-Mod.q.c.)` then `Ind(I)` is an injective object of
`(G-OS-Mod.q.c.)`.*

<!-- label: III.I.5.3.1.1 -->

Let `F` be a `G`-`OS`-module and `μ_F : F → Ind(F)` the map defining the structure of `A(G)`-comodule. It follows from
5.2.0.3 (or from axioms (CM 1) and (CM 2) of 4.7.2) that `μ_F` is a morphism of `G`-`OS`-modules, and that
`(id_F ⊗ η) ∘ μ_F = id_F`, hence that `F` is a direct factor of `Ind(F)` as `OS`-module; in particular, `μ_F` is a
monomorphism. Since, by `(∗)` and 5.2.2,

```text
H^n(G, W(Ind(F))) ≃ H^n(G, Hom_S(G, W(F))) = 0    for n > 0,
```

one therefore obtains that `H^n(G, −)` is effaceable for `n > 0`.

Finally, `S` being affine, `(OS-Mod.q.c.)` has enough injective objects. So let `F ↪ I` be a monomorphism of
`OS`-modules, where `I` is an injective object of `(OS-Mod.q.c.)`; then, `A(G)` being flat over `OS`, `Ind(F)` is a
sub-`G`-`OS`-module of `Ind(I)`, whence:

**Corollary 5.3.1.2.** *The abelian category `(G-OS-Mod.q.c.)` has enough injective objects.*

<!-- label: III.I.5.3.1.2 -->

Taking [Gr57, 2.2.1 and 2.3] into account (already used in the proof of 5.2.1), this completes the proof of Theorem
5.3.1.

**Remark 5.3.1.3.** *One can also prove 5.3.1.1 by the following computation. To every morphism of `G`-`OS`-modules
`φ : M → P ⊗_{OS} A(G)` one associates the `OS`-morphism `(id_P ⊗ η) ∘ φ : M → P`. Conversely, to every `OS`-morphism
`f : M → P` one associates the morphism of `G`-`OS`-modules `(f ⊗ id_{A(G)}) ∘ μ_M : M → P ⊗_{OS} A(G)`. One sees at
once that*

```text
(id_P ⊗ η) ∘ (f ⊗ id_{A(G)}) ∘ μ_M = (f ⊗ id_{OS}) ∘ (id_P ⊗ η) ∘ μ_M = f.
```

<!-- label: III.I.5.3.1.3 -->

<!-- original page 38 -->

*On the other hand, for every `φ` the following diagram is commutative:*

```text
              φ
   M ────────────→ P ⊗_{OS} A(G)
   │                   │
   μ_M               id_P ⊗ Δ
   ↓     φ ⊗ id_{A(G)}    ↓
   M ⊗_{OS} A(G) ──→ P ⊗_{OS} A(G) ⊗_{OS} A(G).
```

*It follows that*

```text
((id_P ⊗ η) ∘ φ ⊗ id_{A(G)}) ∘ μ_M = (id_P ⊗ η ⊗ id_{A(G)}) ∘ (φ ⊗ id_{A(G)}) ∘ μ_M
                                   = (id_P ⊗ η ⊗ id_{A(G)}) ∘ (id_P ⊗ Δ) ∘ φ = φ.
```

*This proves 5.3.1.1 (i) (and (ii) follows).*

Let `F` be a `G`-`OS`-module; one has seen above that axiom (CM 2) of 4.7.2 shows that, considered as `OS`-module, `F`
is a direct factor of `E(F)`. This entails:

**Proposition 5.3.2.** *Let `S` be an affine scheme and `G` an `S`-group affine and flat; suppose that every exact
sequence `0 → F_1 → F_2 → F_3 → 0` of quasi-coherent `G`-`OS`-modules that splits as a sequence of `OS`-modules also
splits as a sequence of `G`-`OS`-modules.*

*Then, the functors `H^n(G, −)` are zero for `n > 0` (or what amounts to the same, the functor `H^0(G, −)` is exact).*

<!-- label: III.I.5.3.2 -->

Indeed, by hypothesis, the sequence of `G`-`OS`-modules

```text
0 → F → E(F) → E(F)/F → 0
```

is split; `F` is therefore a direct factor, as `G`-`OS`-module, of `E(F)`, whose cohomology is zero.

One immediately deduces from this and from Proposition 4.7.4:

<!-- original page 42 -->

**Theorem 5.3.3.** *Let `S` be an affine scheme and `G` a diagonalizable `S`-group. For every quasi-coherent
`G`-`OS`-module `F`, one has `H^n(G, F) = 0`, for `n > 0`.*

<!-- label: III.I.5.3.3 -->

**Remark.** *Proposition 5.3.2 remains valid when `G` is not necessarily flat over `S`; the proof then appeals to
relative cohomology.[^N.D.E-I-53]*

## 6. G-equivariant objects and modules

[^N.D.E-I-54] Let `C` be a category having a final object and in which fiber products exist. Let `G` be a `Ĉ`-group,
`π : M → X` a morphism of `Ĉ`, and `λ = λ_X : G × X → X` an action of `G` on `X`. In the sequel, one will denote
`Y ×_f M` the fiber product of `π : M → X` and an `X`-functor `f : Y → X`.

For every `U ∈ Ob(C)` and `x ∈ X(U)`, one will denote `M_x = U ×_x M`, i.e. for every `φ : U′ → U`, one has

```text
M_x(U′) = {m ∈ M(U′) | π(m) = x_{U′} = φ*(x)}.
```

Finally, if `g ∈ G(U)` one will also denote `gx` the element `λ(g, x)` of `X(U)`.

**Definition 6.1.** *a) One says that `M` is a* `G`-equivariant `X`-object *if one has given an action `Λ : G × M → M`
of `G` on `M` lifting `λ`, i.e. such that the square below is commutative:*

```text
                   Λ
   G × M ─────────────→ M
   │                    │
   id_G × π             π
   ↓        λ           ↓
   G × X ─────────────→ X
```

*This amounts to giving for every morphism `(g, x) : U → G × X` maps*

```text
Λ_x^U(g) : M_x(U) → M_{gx}(U),    m ↦ g ⋅ m
```

*verifying `1 ⋅ m = m` and `g ⋅ (h ⋅ m) = (gh) ⋅ m` and functorial in the `(G × X)`-object `U`. This still amounts to
giving morphisms of `U`-objects:*

```text
Λ_x(g) : M_x → M_{gx}
```

*verifying `Λ_x(1) = id` and `Λ_{hx}(g) ∘ Λ_x(h) = Λ_x(gh)`.*

*b) Let now `O` be a `Ĉ`-ring and let `OX = O × X`. Under the conditions of (a), one says that `M` is a* `G`-equivariant
`OX`-module *if it is an `OX`-module (cf. Definition 4.3.3.1, valid for any ring functor on a category `C`) and if the
action `Λ` is compatible with the `OX`-module structure of `M`, i.e. if for every `(g, x) ∈ G(U) × X(U)` (`U ∈ Ob(C)`),
the map `Λ_x(g) : M_x → M_{gx}`, `m ↦ g ⋅ m` is a morphism of `OU`-modules.*

<!-- label: III.I.6.1 -->

**Remark 6.2.** *(i) In (a) above, the conditions `Λ_x(1) = id` and `Λ_{hx}(g) ∘ Λ_x(h) = Λ_x(gh)` evidently entail that
each `Λ_x(g)` is an isomorphism, with inverse `Λ_{gx}(g^{-1})`. Conversely, if one assumes that each `Λ_x(g)` is an
isomorphism, the condition `Λ_{hx}(g) ∘ Λ_x(h) = Λ_x(gh)` applied to `h = 1` gives `Λ_x(1) = id`.*

*(ii) Let `M` be an `OX`-module. First, one sees that giving a morphism `Λ : G × M → M` making the diagram of 6.1
commutative and such that each morphism*

<!-- original page 40 -->

`Λ_x(g) : M_x → M_{gx}`, `m ↦ g ⋅ m`, *is an isomorphism of `OU`-modules, is equivalent to giving an isomorphism of
`O_{G×X}`-modules:*

```text
θ : G × M = (G × X) ×_{pr_X} M ⥲ (G × X) ×_λ M
                (g, x, m) ↦ (g, x, g ⋅ m).
```

*Since one has assumed that each `Λ_x(g)` is an isomorphism, the equality `Λ_x(1) = id` will be a consequence of the
equality `Λ_{hx}(g) ∘ Λ_x(h) = Λ_x(gh)` applied to `h = 1`. One therefore obtains that `Λ` is an action of `G` on `M`
(i.e. `g ⋅ (h ⋅ m) = (gh) ⋅ m`) if and only if the diagram of `(G × G × X)`-isomorphisms below is commutative (where one
denotes `μ` the multiplication of `G` and `f*(θ)` the isomorphism deduced from `θ` by a base change
`f : G × G × X → G × X`):*

```text
                              pr*_{2,3}(θ)
   (G × G × X) ×_{pr_X ∘ pr_{2,3}} M  ⥲  (G × G × X) ×_{λ ∘ pr_{2,3}} M

       (μ × id_X)*(θ) ≀                              ≀ (id_G × λ)*(θ)

   (G × G × X) ×_{λ ∘ (μ × id_X)} M     (G × G × X) ×_{λ ∘ (id_G × λ)} M.
```

*One sees therefore that giving a `G`-equivariant `OX`-module structure on `M` is equivalent to giving an isomorphism
`θ` of `O_{G×X}`-modules as above, such that the diagram above is commutative.*

*(iii) All that precedes extends to the case where `G` is only a `Ĉ`-monoid: in that case, giving an action
`Λ : G × M → M` lifting `λ` and such that each `Λ_x(g) : M_x → M_{gx}` is a morphism of `OU`-modules is equivalent to
giving a morphism `θ` of `O_{G×X}`-modules as in (ii), such that the diagram above (without the ∼ under the arrows) is
commutative, and such that `p_M ∘ θ ∘ (ε_G × id_M) = id_M`, where `ε_G` denotes the unit section of `G` and `p_M` the
projection onto `M`.*

<!-- label: III.I.6.2 -->

### 6.3. G-equivariant morphisms

Let `Y` be a second object of `Ĉ`, endowed with an action `λ_Y : G × Y → Y` of `G`, and let `N` be a second
`G`-equivariant `OX`-module. One says that a `Ĉ`-morphism `f : Y → X` (resp. a morphism of `OX`-modules `φ : M → N`) is
*`G`-equivariant* if it commutes with the action of `G`, i.e. if one has set-theoretically `f(g ⋅ y) = g ⋅ f(y)` (resp.
`φ(g ⋅ m) = g ⋅ φ(m)`), which is equivalent to saying that `f ∘ λ_Y = λ_X ∘ (id_G × f)` (resp.
`φ ∘ Λ_M = Λ_N ∘ (id_G × φ)`).

One then obtains at once the following lemma:

<!-- original page 41 -->

**Lemma 6.3.1.** *Let `f : Y → X` be a `G`-equivariant morphism and `M` a `G`-equivariant `OX`-module. Then the inverse
image `f*(M) = Y ×_f M` is a `G`-equivariant `OY`-module.*

<!-- label: III.I.6.3.1 -->

On the other hand, `G` acts on `Hom_Ĉ(Y, X)`. Indeed, let `T ∈ Ob(C)`, `g ∈ G(T)` and `φ` a `T`-morphism `Y_T → X_T`;
then `g` defines automorphisms `λ_Y(g)` and `λ_X(g)` of `Y_T` and `X_T`, and one will denote `g ⋅ φ` (or also
`g φ g^{-1}`) the morphism `λ_X(g) ∘ φ ∘ λ_Y(g^{-1})`. This defines an action of `G(T)` on `Hom_T(Y_T, X_T)`, functorial
in `T`.

**Definition 6.3.2.** *If `φ : Y → X` is an arbitrary `Ĉ`-morphism, one can therefore consider its stabilizer
`Stab_G(φ)` (cf. 2.3.3.1): for every `T ∈ Ob(C)`, `Stab_G(φ)(T)` is the subgroup `G(T)` formed by the `g` such that
`g ∘ φ_T = φ_T ∘ g`, i.e. such that the diagram*

```text
              φ_T
   Y_T ────────────→ X_T
   │                  │
   g                  g
   ↓     φ_T          ↓
   Y_T ────────────→ X_T
```

*commutes. Then, the morphism `φ : Y → X` is equivariant under `Stab_G(φ)`.*

<!-- label: III.I.6.3.2 -->

### 6.4. Global sections

Let `M` be a `G`-equivariant `OX`-module. Denote by `S_0` the final object of `C`, and (cf. Exp. II, 1.1) by
`∏_{X/S_0} M` the "functor of sections of `M` over `X`": it is the functor which to every `T ∈ Ob(C)` associates

```text
Hom_X(X_T, M) = Hom_{X_T}(X_T, M_T) = Γ(M_T/X_T).
```

Recall, on the other hand, that every morphism `g : Z → Y` of `Ĉ`-objects above `X` induces a morphism of abelian groups
`M(g) : M(Y) → M(Z)`, which is compatible with the ring morphism `g* : O(Y) → O(Z)`. In particular, when `Z = Y` (with
`g` then an `X`-endomorphism of `Y`), one obtains a morphism of abelian groups

```text
M(g) : M(Y) → M(Y)
```

which is not in general a morphism of `O(Y)`-modules, but which verifies, for every `m ∈ M(Y)` and `α ∈ O(Y)`:

```text
M(g)(α ⋅ m) = g*(α) ⋅ M(g)(m).
```

This said, one will write simply, in the sequel, `g*` instead of `M(g)`.

Let `T ∈ Ob(C)` and let `X_T = X × T` and `pr_X` the projection `X_T → X`. For every `α ∈ O(X_T)` and `g ∈ G(T)`, set
`g(α) = (g^{-1})*(α)`: it is the element of `O(X_T)` defined set-theoretically by: for every `S ∈ Ob(C)` and `x ∈ X(S)`,
`t ∈ T(S)`,

```text
g(α)(x, t) = α(g^{-1} x, t).
```

One thus obtains a (left) action of `G(T)` by ring automorphisms on `O(X_T)`, functorial in `T`, and such that
`g(α) = α` if `α` is the image in `O(X_T)` of an element of `O(T)`.

Now denote by `φ` the identity morphism of `X_T` (cf. 6.3 and the generalization further below to a morphism
`φ : Y → X`) and designate `Hom_X(X_T, M)` by `M(φ g^{-1})` resp. `M(φ)`, according as `X_T` is regarded as an
`X`-object via `pr_X ∘ λ(g^{-1})_T`, resp. `pr_X`.

<!-- original page 42 -->

Then `λ(g^{-1})_T` is an `X`-morphism between these two `X`-objects, hence, by the preceding, one obtains a morphism of
abelian groups

```text
(g^{-1})* : M(φ) → M(φ g^{-1}),    m ↦ m ∘ λ(g^{-1})_T
```

which verifies `(g^{-1})*(α ⋅ m) = (g α) ⋅ (g^{-1})*(m)` for every `m ∈ M(φ)` and `α ∈ O(X_T)`. (If `m` is a section of
`M_T` on `X_T` then `(g^{-1})*(m)` is the section defined set-theoretically by `(x, t) ↦ m(g^{-1} x, t)`.) In
particular, `(g^{-1})*` is a morphism of `O(T)`-modules.

By the functoriality of the morphisms of `O(X_T)`-modules `Λ_x(g)`, one obtains a commutative diagram:

```text
                 (g^{-1})*
   M(φ) ──────────────→ M(φ g^{-1})
     │                      │
   Λ_φ(g)               Λ_{φ g^{-1}}(g)
     ↓     (g^{-1})*        ↓
   M(g φ) ─────────→ M(g φ g^{-1})
```

and `g φ g^{-1} = φ`, since `φ` is the identity map. Setting `A(g) = (g^{-1})* ∘ Λ_φ(g)`, one therefore obtains a
morphism of abelian groups

```text
A(g) : M(φ) → M(φ)
```

which is "compatible with the action of `G(T)` on `O(X_T)`", i.e. which verifies

```text
A(g)(α ⋅ m) = (g α) ⋅ A(g)(m).
```

Finally, if `h` is a second element of `G(T)`, it follows from the functoriality of `M` and of the morphisms `Λ_x(g)`
that one has a commutative diagram

```text
                M(φ)
                  ╲
                 Λ_φ(g)
                    ╲                Λ_φ(hg)
                     ╲
            Λ_φ(h)    ╲                         ╲
                       ↓                         ↘
                   M(g φ) ────────→ M(hg φ) ───────→ M(φ)
                   (g^{-1})*   Λ_φ(h)    (hg)^{-1}*
                                    
                       (g^{-1})*                ((hg)^{-1})*
                       
                   M(φ) ───────→ M(h φ) ─────────→ M(φ)
                          Λ_φ(h)         (h^{-1})*
```

whence `A(h) ∘ A(g) = A(hg)`. Consequently, one has obtained the following proposition:

**Proposition 6.4.1.** *For every `T`, the `O(X_T)`-module `(∏_{X/S_0} M)(T) = Γ(M_T/X_T)` is endowed, in a way
functorial in `T`, with an action of `G(T)` "compatible with the action of `G(T)` on `O(X_T)`", i.e. which verifies*

```text
A(g)(α ⋅ m) = g(α) ⋅ A(g)(m).
```

<!-- label: III.I.6.4.1 -->

Since `g(α) = α` for `α ∈ O(T)`, this gives in particular that `∏_{X/S_0} M` is a `G`-`O_{S_0}`-module.

More generally, let, as in 6.3, `Y` be a second `G`-equivariant `Ĉ`-object, `φ : Y → X` a `Ĉ`-morphism and
`H = Stab_G(φ)`. Then the fiber product `M_φ = Y ×_φ M` is an `H`-equivariant `OY`-module. One therefore obtains:

<!-- original page 43 -->

**Corollary 6.4.2.** *The functor `∏_{Y/S_0} M_φ` is a `Stab_G(φ)`-`O_{S_0}`-module.*

<!-- label: III.I.6.4.2 -->

### 6.5. G-equivariant OX-modules

Let us apply what precedes in the following situation. Let `S` be a scheme, `G` an `S`-group scheme acting on an
`S`-scheme `X`, and `F` an `OX`-module (not necessarily quasi-coherent).

**Definition 6.5.1.** *One says that `F` is a* `G`-equivariant `OX`-module *if the `OX`-module `M = W(F)` is
`G`-equivariant, i.e. if one has given, for every morphism `(g, x) : U → G ×_S X`, isomorphisms of `OU`-modules*

```text
Λ_x(g) : W(x*(F)) ⥲ W((gx)*(F)),
```

*functorial in `U` and verifying `Λ_{hx}(g) ∘ Λ_x(h) = Λ_x(gh)`.* Since the functor `W` is fully faithful (cf. 4.6.1.1
and 4.6.2), one therefore obtains isomorphisms of `OU`-modules

```text
Λ_x(g) : x*(F) ⥲ (gx)*(F),
```

where one recalls that `gx` denotes the morphism `λ ∘ (g, x) : U → X`. In particular, applying this to the identity
morphism of `G ×_S X`, one obtains an isomorphism of `O_{G ×_S X}`-modules

```text
(⋆)    θ : pr*_X(F) ⥲ λ*(F)
```

<!-- label: eq:III.I.6.5.1-star -->

*such that the diagram `(⋆⋆)` of morphisms of sheaves on `G ×_S G ×_S X` below is commutative:*

```text
                     pr*_{2,3}(θ)
   pr*_{2,3} ∘ pr*_X(F) ────────→ pr*_{2,3} ∘ λ*(F)    (id_G × λ)* ∘ pr*_X(F)

                                  (⋆⋆)                  ≀ (id_G × λ)*(θ)

   (μ × id_X)* ∘ pr*_X(F) ──→ (μ × id_X)* ∘ λ*(F)      (id_G × λ)* ∘ λ*(F).
```

<!-- label: III.I.6.5.1 -->

Moreover, if `E` is a second `G`-equivariant `OX`-module, one says that a morphism of `OX`-modules `φ : E → F` is
*`G`-equivariant* if the morphism `W(φ) : W(E) → W(F)` is. With the above notations, this is equivalent to saying that
`θ_F ∘ pr*_X(φ) = λ*(φ) ∘ θ_E`.

**Remark 6.5.2.** *If `f : Y → X` is a `G`-equivariant morphism, it follows from 6.3.1 that `f*(F)` is a `G`-equivariant
`OY`-module.*

<!-- label: III.I.6.5.2 -->

**Remark 6.5.3.** *Suppose moreover `F` quasi-coherent. Then it follows from what precedes that giving a `G`-equivariant
`OX`-module structure on `M = W(F)` is equivalent to giving such a structure on `V(F)`, which is itself equivalent to
giving an action of `G` on the vector fibration `V(F)`, compatible with the action on `X` and "linear" on the fibers.*

Indeed, denote by `φ` the isomorphism `λ*(F) ⥲ pr*_X(F)` inverse of `θ`. For every morphism `(g, x) : U → G ×_S X`, one
has an isomorphism of `OU`-modules `φ_x(g) = Λ_x(g)^{-1} = Λ_{gx}(g^{-1})` from `(gx)*(F)` to `x*(F)`; it induces an
isomorphism of `OU`-modules

```text
V((gx)*(F)) ⥲ V(x*(F))
```

<!-- original page 44 -->

which one will denote `t φ_x(g)`. One then has

```text
t φ_{gx}(h) ∘ t φ_x(g) = t (Λ_{gx}(h) ∘ φ_x(g))^{-1} = Λ_x(hg)^{-1} = t φ_x(hg).
```

Since, for every `X`-scheme `f : Y → X`, one has `V(F) ×_f Y ≃ V(f*(F))` (cf. 4.6.2), one therefore obtains that the
isomorphism

```text
t φ : G ×_S V(F) = (G ×_S X) ×_{pr_X} V(F) = V(pr*_X(F))
                                  ⥲ V(λ*(F)) = (G ×_S X) ×_λ V(F)
```

endows `V(F)` with a `G`-equivariant `OX`-module structure. Finally, identifying each functor `V(−)` with the vector
fibration that represents it, and composing `t φ` with the projection onto `V(F)`, one obtains an action of `G` on the
vector fibration `V(F)`, compatible with the action on `X` and "linear" on the fibers.

<!-- label: III.I.6.5.3 -->

One thus recovers the definition given, for example, in [GIT, Chap. 1, § 3], up to the fact that in *loc. cit.* Mumford
considers a locally free `OX`-module of finite rank `E`, and defines an action of `G` on `V(E) = W(E^∨)`. Indeed, the
diagram `(⋆⋆)` above, with `θ` replaced by `φ` and the direction of the arrows reversed, is exactly the one one finds in
*loc. cit.*, Def. 1.6, and the isomorphism `t φ` above coincides with the isomorphism `Φ` of *loc. cit.*, p. 31.

**Remark 6.5.4.** *Consider in particular the case where `X = S`, endowed with the trivial action of `G`. In this case,
a `G`-equivariant `OS`-module `F` is the same thing as a `G`-`OS`-module (cf. 4.7.1). Moreover, if one denotes `f` the
morphism `G → S` (equal here to `pr_X` and to `λ`), then the isomorphism*

```text
(⋆)    θ : f*(F) ⥲ f*(F)
```

*is an element of*

```text
Hom_{OG}(f*(F), f*(F)) = Hom_{OG}(W(f*(F)), W(f*(F))) = End_{OS}(W(F))(G)
```

*which is nothing other than the morphism `ρ : G → End_{OS}(W(F))` defining the operation of `G` on `W(F)`. Moreover,
`θ` corresponds by adjunction to the morphism of `OS`-modules `f_*(θ) ∘ τ : F → f_* f*(F)`, where `τ : F → f_* f*(F)` is
the "unit" morphism of the adjunction. (This will be used in `VI_B`, 11.10.bis.)*

<!-- label: III.I.6.5.4 -->

### 6.6. The functors ∏_{X/S} W(F) and W(p_\*(F))

Let `S` be a scheme, `G` an `S`-group scheme acting on `S`-schemes `X` and `Y` via the morphisms `λ : G ×_S X → X` and
`μ : G ×_S Y → Y`, and let `p : X → Y` be a `G`-equivariant morphism. Suppose that the morphisms `p : X → Y` and
`ν_Y : Y → S` are quasi-compact and quasi-separated, and that `π : G → S` is flat.

Then the projection `pr_Y : G ×_S Y → Y` is flat, as is `μ` (since `μ` is the composite of `pr_Y` and of the
automorphism `(g, y) ↦ (g, gy)`). Finally, for a variable `S`-scheme `f : T →`, one will denote by `p_T : X_T → T` and
`f_X : X_T → X` the morphisms deduced from `p` and `f` by base change.

Let `F` be a quasi-coherent and `G`-equivariant `OX`-module, and let `θ` be the isomorphism `pr*_X(F) ⥲ λ*(F)` of 6.5.1
`(⋆)`. Since `p` is quasi-compact and quasi-separated,

<!-- original page 45 -->

`p_*(F)` is quasi-coherent (cf. EGA I, 9.2.1).

**Lemma 6.6.1.** *The quasi-coherent `OY`-module `p_*(F)` is `G`-equivariant.*

<!-- label: III.I.6.6.1 -->

Indeed, one has the two cartesian squares below:

```text
                pr_X            λ
   G ×_S X ─────────→ X ←───────── G ×_S X
       q              │                q
                      p                 
                pr_Y            μ
   G ×_S Y ─────────→ Y ←───────── G ×_S Y.
```

Since `p` is quasi-compact and quasi-separated and `pr_Y` and `μ` are flat, it follows from EGA III, 1.4.15 (completed
by EGA IV_1, 1.7.21) that one has `q_* pr*_X(F) = pr*_Y p_*(F)` and `q_* λ*(F) = μ* p_*(F)`. Consequently, `θ` induces
an isomorphism:

```text
θ_Y : pr*_Y p_*(F) ⥲ μ* p_*(F),
```

and one obtains similarly that `θ_Y` verifies the "cocycle condition" 6.5.1 `(⋆⋆)` (since the morphisms
`G ×_S G ×_S Y → G ×_S Y` involved are flat). This proves the lemma.

In particular, take `Y = S` endowed with the trivial action of `G`. Taking Remark 6.5.4 into account, one then obtains
that `p_*(F)` is a `G`-`OS`-module. If moreover `G` is affine over `S` and if one denotes `A(G) = π_*(O_G)`, then
`p_*(F)` is therefore an `A(G)`-comodule, by 4.7.2.

On the other hand, by 6.4.1, the functor `∏_{X/S} W(F)`, which to every `f : T → S` associates

```text
W(f_X*(F))(X_T) = Γ(X_T, f_X*(F)) = Γ(T, p_{T*} f_X*(F))
```

is a `G`-`OS`-module. Moreover, one has a canonical morphism `τ : W(p_*(F)) → ∏_{X/S} W(F)`, which is given for every
`f : T → S` by the canonical morphism:

```text
Γ(T, f* p_*(F)) → Γ(T, p_{T*} f_X*(F))
```

and which is an isomorphism when restricted to the full subcategory of schemes `T` flat over `S`, and one verifies
without difficulty that `τ` is a morphism of `G`-`OS`-modules. Consequently, one has obtained the following proposition
(for point (ii), compare with [GIT], p. 32).

**Proposition 6.6.2.** *Let `S` be a scheme, `G` an `S`-group scheme acting on an `S`-scheme `X`, and `F` a
quasi-coherent and `G`-equivariant `OX`-module. Suppose that `π : G → S` is flat and that `p : X → S` is quasi-compact
and quasi-separated.*

*(i) Then `p_*(F)` is a quasi-coherent `G`-`OS`-module. Moreover, the canonical morphism `W(p_*(F)) → ∏_{X/S} W(F)` is a
morphism of `G`-`OS`-modules, and these two functors coincide on the category of flat `S`-schemes.*

*(ii) If moreover `G` is affine over `S` and if one denotes `A(G) = π_*(O_G)`, then `p_*(F)` is endowed with a structure
of `A(G)`-comodule.[^N.D.E-I-55]*

<!-- label: III.I.6.6.2 -->

<!-- original page 46 -->

### 6.7. Stabilizers

Let `S` be a scheme, `G` an `S`-group scheme acting on an `S`-scheme `X`, and let `F` be a quasi-coherent
`G`-equivariant `OX`-module. Let `Y` be a second `S`-scheme endowed with an action of `G` (possibly trivial), let
`φ : Y → X` be an `S`-morphism, not necessarily `G`-equivariant, and let `Stab_G(φ)` be the stabilizer in `G` of `φ`
(cf. 6.3.2).

Let us point out at once (see Exp. `VI_B`, § 6) that `Stab_G(φ)` is representable by a closed sub-group scheme `H` of
`G` if `X` is separated over `S` and if `Y` is essentially free over `S` (cf. *loc. cit.*, Déf. 6.2.1). Indeed, consider
the morphism `r : G ×_S Y → X ×_S X` given set-theoretically by `r(g, y) = (φ(y), g φ(g^{-1} y))`, and let `P = G ×_S Y`
and `P′` the inverse image by `r` of the diagonal `Δ_{X/S}`. Then one has (cf. *loc. cit.*, 6.2.4 (a))

```text
Stab_G(φ) = ∏_{P/G} P′
```

and therefore, by *loc. cit.*, `Stab_G(φ)` is representable by a closed sub-group scheme `H` of `G` if `X` is separated
over `S` and if `Y` is essentially free over `S`; this second condition being automatically verified if `S` is the
spectrum of a field, or if `Y = S`. Under these hypotheses, `φ*(F)` is then a quasi-coherent `H`-equivariant `OY`-module
(cf. 6.5.2).

Hence, if moreover `π : G → S` and `p : Y → S` are quasi-compact and quasi-separated over `S`, and `π` flat, then
`p_* φ*(F)` is an `H`-`OS`-module, by 6.6.2. In particular, one obtains:

**Corollary 6.7.1.** *Let `S` be a scheme, `G` an `S`-group scheme acting on an `S`-scheme `X`, and `F` a quasi-coherent
`G`-equivariant `OX`-module. Suppose that `π : G → S` is flat and that `X → S` is quasi-compact and separated. Let
`τ : S → X` be a section of `X` over `S`.*

*(i) The stabilizer `H = Stab_G(τ)` is a closed sub-group scheme of `G`, and `τ*(F)` is a quasi-coherent
`H`-`OS`-module.*

*(ii) If moreover `H` is affine over `S` (for example, if `G` is) and if one denotes `A(H) = π_*(O_H)`, then `τ*(F)` is
an `A(H)`-comodule.*

<!-- label: III.I.6.7.1 -->

### 6.8. G-equivariant sheaves on G

To conclude, let us point out two results (6.8.1 and 6.8.6 below) that will be used in Exposés II and III (cf. in
particular III, 4.25).

**Proposition 6.8.1.** *Let `S` be a scheme, `π : G → S` an `S`-group scheme, `ε : S → G` the unit section. Consider the
action by left translations of `G` on itself. Then the functors `E ↦ π*(E)` and `F ↦ ε*(F)` induce equivalences,
quasi-inverse to one another, between the category of quasi-coherent `OS`-modules and that of quasi-coherent
`G`-equivariant `OG`-modules.*

<!-- label: III.I.6.8.1 -->

*Proof.* Denote by `μ` the multiplication of `G` and by `pr_2` the second projection `G ×_S G → G`. Since
`π ∘ μ = π ∘ pr_2`, then, for every quasi-coherent `OS`-module `E`, one has a canonical isomorphism
`μ* π*(E) = pr*_2 π*(E)`, and one verifies easily that this isomorphism satisfies the "cocycle condition" 6.5.1 `(⋆⋆)`,
i.e. `π*(E)` is a `G`-equivariant `OG`-module. Since `ε* π*(E) = E`, the functor `E ↦ π*(E)` is

<!-- original page 47 -->

fully faithful; it remains therefore to see that for every `G`-equivariant `OG`-module `F`, one has `F ≃ π* ε*(F)`. By
hypothesis, one has an isomorphism `θ : pr*_2(F) ⥲ μ*(F)`; taking the inverse image of `θ` by the morphism
`τ : G → G ×_S G` of components `(id_G, ε ∘ π)`, one obtains an isomorphism `F ⥲ π* ε*(F)`.

**Remarks 6.8.2.** *(a) Consider the action of `G ×_S G` on `G` defined by `(g_1, g_2) ⋅ g = g_1 g g_2^{-1}`; then the
stabilizer of the unit section `ε : S → G` is the diagonal subgroup `H` of `G ×_S G`. Consequently, if `F` is a
quasi-coherent `(G ×_S G)`-equivariant `OG`-module then, by 6.5.2, `E = ε*(F)` is endowed with a structure of
`H`-`OS`-module.*

*(b) One can show that `F ↦ ε*(F)` is an equivalence of categories, between the category of quasi-coherent
`(G ×_S G)`-equivariant `OG`-modules and that of quasi-coherent `H`-`OS`-modules. This is a particular case of more
general "descent" results (cf. Exp. IV, § 2 and SGA 1, VIII), see for example [Th87], 1.2–1.3.*

<!-- label: III.I.6.8.2 -->

**Remark 6.8.3.** *One retains the notations of 6.8.1. For every quasi-coherent `OS`-module `E`, denote by `π_*^G π*(E)`
the sub-`OS`-module of `π_* π*(E)` whose sections on every open subset `V` of `S` are the `γ ∈ Γ(π^{-1}(V), π*(E))` such
that `g ⋅ γ_{S′} = γ_{S′}` for every `S′ → V` and `g ∈ G(S′)`. Then the natural morphism `E → π_*^G π*(E)` is an
isomorphism: this is immediate if `π_* π*(E) = E ⊗_{OS} π_*(O_G)` (for example if `G → S` is affine, or if `G → S` is
quasi-compact and quasi-separated and `E` flat), and it is verified without difficulty in the general case.*

<!-- label: III.I.6.8.3 -->

**Remark 6.8.4.** *Let `S` be a scheme, `H` an `S`-group scheme acting on an `S`-scheme `X`, `F` an `OX`-module. Suppose
`H` flat over `S` and denote by `W_P(F)` the restriction of the functor `W(F)` to the full subcategory formed by the
`S`-schemes that are flat. Since, by 6.5.1, endowing `F` with a structure of `H`-equivariant module is equivalent to
giving an isomorphism `θ : pr*_X(F) → λ*(F)` of sheaves on `G ×_S X`, verifying the "cocycle condition" `(⋆⋆)`, one sees
that to give an `H`-equivariant module structure on `F`, it suffices to give such a structure on `W_P(F)`.*

<!-- label: III.I.6.8.4 -->

**Recollection 6.8.5.** *Let `X` be an `S`-scheme and `Y` a sub-`S`-scheme of `X`. One denotes by `N_{Y/X}` the conormal
sheaf of the immersion `i : Y ↪ X` (cf. EGA IV_4, 16.1.2). If `S′ → S` is a flat morphism and if one denotes
`i′ : Y′ ↪ X′` the immersion deduced from `i` by base change, then by* loc. cit., *16.2.2 (iii), one has
`N_{Y/X} ⊗_{OY} O_{Y′} = N_{Y′/X′}`.*

<!-- label: III.I.6.8.5 -->

**Proposition 6.8.6.** *Let `S` be a scheme, `X` an `S`-group scheme, `Y` a sub-`S`-group scheme of `X`. Suppose `Y`
flat over `S`. Then the conormal sheaf `N_{Y/X}` is a `(Y ×_S Y)`-equivariant `OY`-module.*

<!-- label: III.I.6.8.6 -->

Indeed, `H = Y ×_S Y` is flat over `S`, so by Remark 6.8.4, it suffices to endow `W_P(N_{Y/X})` with an `H`-equivariant
module structure. Let `S′` be a flat `S`-scheme, let `Y′ ↪ X′` be the immersion obtained by base change, and let
`N′ = N_{X/Y} ⊗_{OY} O_{Y′}`. By 6.8.5, one has `N′ = N_{Y′/X′}`.

Every `h ∈ H(S′)` induces an automorphism of `Y′`, and one therefore obtains, for every `y ∈ Y′(S′)`, isomorphisms

```text
Γ(S′, y*(N′)) ⥲ Γ(S′, y* h*(N′))
```

<!-- original page 48 -->

which endow `W_P(N)` with a structure of `H`-equivariant module (cf. 6.1).

## Bibliography

[^N.D.E-I-56]

- [DG70] M. Demazure, P. Gabriel, *Groupes Algébriques*, Masson & North-Holland, 1970.
- [Gr57] A. Grothendieck, Sur quelques points d'algèbre homologique, *Tôhoku Math. J.* 9 (1957), 119–221.
- [Ja03] J. C. Jantzen, *Representations of algebraic groups*, Academic Press, 1987; 2nd ed. Amer. Math. Soc., 2003.
- [GIT] D. Mumford, *Geometric invariant theory*, Springer-Verlag, 1965; 2nd ed., with J. Fogarty, 1982; 3rd ed., with
    J. Fogarty & F. Kirwan, 1994.
- [Ni02] N. Nitsure, Representability of `GL_E`, *Proc. Indian Acad. Sci.* 112 (2002), No. 4, 539–542.
- [Ni04] N. Nitsure, Representability of Hom implies flatness, *Proc. Indian Acad. Sci.* 114 (2004), No. 1, 7–14.
- [Se68] J.-P. Serre, Groupes de Grothendieck des schémas en groupes réductifs déployés, *Publ. math. I.H.É.S.* 34
    (1968), 37–52.
- [Th87] R. W. Thomason, Equivariant resolution, linearization, and Hilbert's fourteenth problem over arbitrary base
    schemes, *Adv. Maths.* 65 (1987), 16–34.

## Footnotes

<!-- LEDGER DELTA — Exposé I — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| structure de groupe | group structure | Standard. |
| composition law / loi de composition | composition law | Standard. |
| section unité | unit section | Standard. |
| sous-`Ĉ`-groupe | sub-`Ĉ`-group | Hyphenated. |
| produit semi-direct | semidirect product | One word, no hyphen. |
| objet à groupe d'opérateurs | object with operator group | Standard. |
| poly-homomorphisme | polyhomomorphism | One word. |
| espèce de structure | species of structure | Bourbaki idiom. |
| objet constant | constant object | Standard. |
| schéma constant | constant scheme | Standard. |
| changement de base | base change | Standard. |
| bigèbre augmentée | augmented bialgebra | Standard. |
| co-associatif | co-associative | Hyphenated; preserves the French. |
| algèbre de Hopf | Hopf algebra | Standard. |
| fibration vectorielle | vector fibration | Per N.D.E.; distinct from "fibré vectoriel" = vector bundle. |
| fibré vectoriel | vector bundle | Locally trivial of rank `r`. |
| comodule | comodule | Standard. |
| objet à groupe d'opérateurs `G`-objet | `G`-object | Standard. |
| objet G-équivariant | `G`-equivariant object | Per Mumford GIT terminology. |
| OX-module G-équivariant | `G`-equivariant `OX`-module | Standard. |
| condition de cocycle | cocycle condition | Standard. |
| complexe de Hochschild | Hochschild complex | Per N.D.E. 5.1. |
| effaçable | effaceable | Standard. |
| faisceau conormal | conormal sheaf | Standard. |
| sous-comodule | subcomodule | One word. |
| section unité ε : S → G | unit section ε : S → G | Standard. |
| translations à gauche | left translations | Standard. |
| `p`-algèbre de Lie | `p`-Lie algebra | (not used in this Exposé, but glossary item). |
-->

[^I-0-0]: Version of 13/10/2024.

[^N.D.E-I-1]: N.D.E.: Cf. SGA 4, Exp. I, § 0 and Appendix; see also the discussion in [DG70], p. xxvi.

[^N.D.E-I-2]: N.D.E.: One calls it the category of presheaves on `C`, cf. IV 4.3.1.

[^N.D.E-I-3]: N.D.E.: This result is often called the "Yoneda Lemma"; we shall use this terminology in other N.D.E.

[^N.D.E-I-4]: N.D.E.: This remark has been added.

[^N.D.E-I-5]: N.D.E.: The order has been modified, in order to introduce fiber products before monomorphisms, cf. N.D.E.
    (9).

[^N.D.E-I-6]: N.D.E.: Likewise, "arbitrary" direct limits exist and are computed "argument by argument", i.e.
    `(lim→_i F_i)(S) = lim→_i F_i(S)`; but in general the functor `h` does not commute with direct limits.

[^N.D.E-I-7]: N.D.E.: In particular, the kernel of a pair of morphisms `u, v : F ⇒ G` is the subfunctor `Ker(u, v)` of
    `F` defined by `Ker(u, v)(S) = {x ∈ F(S) | u(x) = v(x)}`.

[^N.D.E-I-8]: N.D.E.: `{∅}` (the set of subsets of the empty set) denotes the one-element set.

[^N.D.E-I-9]: N.D.E.: If `F(S) → G(S)` is injective for every `S`, it is clear that `F → G` is a monomorphism; the
    converse is seen by considering the diagram `F ×_G F ⇒ F → G`. One thus obtains that: "`F → G` is a
    monomorphism if and only if the diagonal morphism `F → F ×_G F` is an isomorphism" (cf. EGA I, 5.3.8).
    Likewise, it is clear that if `F(S) → G(S)` is surjective for every `S`, then `F → G` is an epimorphism,
    and the converse is seen by considering the amalgamated sum `G ⨆_F G`, cf. the proof of Lemma 4.4.4 in
    Exp. IV.

[^N.D.E-I-10]: N.D.E.: For example, if `F = hX` then `H` corresponds to a morphism `h : X → S` and
    `H(T) : Hom_C(T, X) → Hom_C(T, S)` is the map `g ↦ h ∘ g`, whence `αS(hX) = Hom_{C/S}(−, X)`.

[^N.D.E-I-11]: N.D.E.: Cf. N.D.E. (10).

[^N.D.E-I-12]: N.D.E.: I.e. if `g : U → S` (resp. `h : V → T`) is an object of `C/S` (resp. `C/T`) then `iS(g) = U` and
    `i_{T/S}(h)` is the object `f ∘ h : V → S` of `C/S`, and one has:

    ```text
    Hom_{C/S}(U, X × S) ≃ Hom_C(U, X)    resp.    Hom_{C/T}(V, X ×_S T) ≃ Hom_{C/S}(V, X).
    ```

[^N.D.E-I-13]: N.D.E.: The following lemma has been added (cf. SGA 4, I.3.4); it is used in the proof of 1.7.1 and will
    be useful several times in the sequel.

[^N.D.E-I-14]: N.D.E.: And, if `E` is a third object of `Ĉ`, one has `Hom(E, F × G) ≅ Hom(E, F) × Hom(E, G)`.

[^N.D.E-I-15]: N.D.E.: Point (b) has been added, which will be useful in II.1 and II.3.11. On the other hand, a second,
    more direct, proof of (a) has been sketched.

[^N.D.E-I-15-alt]: (continuation of the proof of Proposition 1.7.1, sketching a direct argument)

[^N.D.E-I-16]: N.D.E.: The numbering 1.7.3 has been added, for subsequent references.

[^N.D.E-I-17]: N.D.E.: The former terminology "préschémas/schémas" has been replaced by the current terminology
    "schémas/schémas séparés".

[^N.D.E-I-18]: N.D.E.: In the three paragraphs that follow, the order of the sentences has been modified and some
    clarifications added concerning the role of the hypothesis `(∗)` below.

[^N.D.E-I-19]: N.D.E.: `(∗)` is not verified if `C` is the category whose arrows are `A → B` and `id_A, id_B`; in this
    case `B ⨆ B = B` and `B ×_B B = B ≄ A`.

[^N.D.E-I-20]: N.D.E.: Note also that the diagonal morphism `ES → ES ×_S ES = (E × E)_S` is a closed immersion, i.e.
    `ES` is separated over `S`.

[^N.D.E-I-21]: N.D.E.: Including the condition `(∗)`.

[^N.D.E-I-22]: N.D.E.: For example, for group structures: let `G ∈ Ob(Ĉ)`; if the functor `Ĉ → (Ens)`, `F ↦ Hom_Ĉ(F, G)`
    is endowed with a group structure, the same is true of its restriction to `C`, `X ↦ G(X)`. Conversely, if
    `G` is a `Ĉ`-group, then the "multiplication" morphism `π_G : G × G → G` induces for every `F ∈ Ob(Ĉ)` a
    group structure on `Hom_Ĉ(F, G)`, functorial in `F`.

[^N.D.E-I-23]: N.D.E.: We have corrected the original, replacing the inclusion `ρ(g) FS ⊂ FS` by an equality, in order
    to ensure that `Norm_G(F)` is indeed a group (see `VI_B` 6.4 for conditions under which the "transporter"
    coincides with the "strict transporter").

[^N.D.E-I-24]: N.D.E.: Scholium 2.3.3.1 and Remark 2.3.3.2 have been added.

[^N.D.E-I-25]: N.D.E.: Moreover, one says that `H` is *central* in `G` if `Centr_G(H) = G`, or, what amounts to the same
    thing, if `H(S)` is central in `G(S)` for every `S`.

[^N.D.E-I-26]: N.D.E.: Definitions 2.3.6.1 and 2.3.6.2 have been added.

[^N.D.E-I-27]: N.D.E.: Statements 3.1.1 and 3.1.2 have been added to make explicit that the category `(O-Mod.)` is
    abelian and verifies the axiom (AB 5), and moreover has enough injective objects if the category `C` is
    small. An error in 3.1.2, reported in 2016 by Linyuan Liu, has been corrected here.

[^N.D.E-I-28]: N.D.E.: The following sentence has been added; this will be used in section 5.

[^N.D.E-I-29]: N.D.E.: And, of course, the inversion morphism `G → G` induces a morphism of `OS`-algebras
    `τ : A(G) → A(G)` which, together with `Δ` and `ε`, makes `A(G)` an `OS`-Hopf algebra.

[^N.D.E-I-30]: N.D.E.: This paragraph has been added, which will be useful later (cf. II 1.3).

[^N.D.E-I-31]: N.D.E.: The numbering 4.6.1.1 has been added, for subsequent references.

[^N.D.E-I-32]: N.D.E.: The isomorphism `Hom_{OS}(W(F), W(F′)) ≅ Hom_{OS}(V(F′), V(F))` has been added.

[^N.D.E-I-33]: N.D.E.: "vector bundle" has been replaced by "vector fibration"; current usage being to call a vector
    fibration that is locally trivial of rank `r` a "vector bundle of rank `r`", i.e. one whose sheaf of
    sections is locally isomorphic to `OS^{⊕r}`.

[^N.D.E-I-34]: N.D.E.: Let us point out here the articles [Ni04] (resp. [Ni02]), which show that if `S` is noetherian
    and `F` is a coherent `OS`-module, then `W(F)` (resp. the `S`-group which to every `T → S` associates
    `Aut_{OT}(F ⊗ OT)`) is representable if and only if `F` is locally free.

[^N.D.E-I-35]: N.D.E.: The original has been detailed in what follows.

[^N.D.E-I-36]: N.D.E.: The following sentence has been detailed.

[^N.D.E-I-37]: N.D.E.: This remark has been added, taken from [DG], II, § 2, 1.1.

[^N.D.E-I-38]: N.D.E.: The original has been corrected by suppressing the assertion that the category `(G-OS-Mod.)` is
    abelian, see 4.7.2.1 below.

[^N.D.E-I-39]: N.D.E.: This remark has been added.

[^N.D.E-I-40]: N.D.E.: Cf. `VI_B`, §§ 11.1–11.6 for the extension of the results of 4.7.2 to the case where `G` is not
    necessarily affine, but where `G` and `F` are assumed to be flat over `S`.

[^N.D.E-I-41]: N.D.E.: Left `G`-`OS`-modules correspond in a natural way to right `A(G)`-comodules.

[^N.D.E-I-42]: N.D.E.: The following sentence has been added.

[^N.D.E-I-43]: N.D.E.: The following paragraph has been added, taken from [Se68, § 1.3].

[^N.D.E-I-44]: N.D.E.: This complex is often called the "Hochschild complex"; see for example § II.3 of [DG70].

[^N.D.E-I-45]: N.D.E.: This remark has been added.

[^N.D.E-I-46]: N.D.E.: The following recollection has been added.

[^N.D.E-I-47]: N.D.E.: The following sentence has been added.

[^N.D.E-I-48]: N.D.E.: The original has been modified, in order to introduce 5.2.0.1 and 5.2.0.2, which will be useful
    in the proof of Theorem 5.3.1.

[^N.D.E-I-49]: N.D.E.: Cf. [Gr57], 2.2.1 and 2.3. Moreover, the original has been detailed in what follows.

[^N.D.E-I-50]: N.D.E.: The original has been detailed in what follows.

[^N.D.E-I-51]: N.D.E.: This remark has been added.

[^N.D.E-I-52]: N.D.E.: The original has been modified to show that the category `(G-OS-Mod.q.c.)` is abelian and has
    enough injective objects. One may compare with [Ja03], Part I, 3.3-3.4, 3.9, 4.2 and 4.14-4.16 (where one
    should be aware that "`k`-group scheme" means "affine `k`-group scheme", cf. *loc. cit.*, 2.1).

[^N.D.E-I-53]: N.D.E.: The editors did not seek to develop this remark.

[^N.D.E-I-54]: N.D.E.: This section has been added.

[^N.D.E-I-55]: N.D.E.: The same is true if `G` is flat, quasi-compact and quasi-separated over `S` and if `p_*(F)` is a
    flat `OS`-module, cf. Exp. `VI_B`, 11.6.1 (ii).

[^N.D.E-I-56]: N.D.E.: additional references cited in this Exposé.
