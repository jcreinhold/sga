# Exposé XI. Representability criteria. Applications to multiplicative-type subgroups of affine group schemes

<!-- label: III.XI -->

*by A. Grothendieck*

## 0. Introduction

<!-- original page 127 -->

As we have already seen examples in Exp. X, N°s 4, 5, the representability of certain functors, such as certain functors
of type `Hom_S(X, Y)` and various variants, plays an important role in many questions concerning preschemes in groups.

Among the results particularly useful in this theory, let us mention (in addition to the questions of representability
of quotients, studied in Exposés V and VI_B and in Exp. VIII 5) the question of the representability of functors of the
form `∏_{X/S} Y/X` (where `Y` is a subobject of `X`), studied in Exp. VIII 6 in a very elementary case, of which we
shall give variants in N° 6 of the present Exposé; these results give us the representability of various centralizers,
normalizers, transporters.

Less elementary representability criteria, using results that will appear in EGA VI, are indicated in 6.12 and in Exp.
XV, XVI, where we shall give a criterion of representability of quotients `G/H` in cases not covered by the preceding
Exposés (a criterion that was not developed in the oral Exposés).

Our principal object in the present Exposé is the proof of theorems 4.1 and 4.2, which furnish a typical example of a
non-projective construction technique (close to the one that will be developed in EGA VI). It has indeed appeared, since
the oral Exposé and the writing of the present text, that the affine hypotheses made in 4.1 <!-- original page 128 -->
and 4.2 can to a large extent be eliminated (cf. XV), and that, on the other hand, one can, for the essential part of
the theory developed in the following Exposé, do without 4.1 and 4.2. It might finally be interesting to prove the
analogue of these results for a general reductive (for instance semisimple) group prescheme instead of a group of
multiplicative type, in which case 4.1 and 4.2 will doubtless be the key result for the proof.

## 1. Reminders on smooth, étale, and unramified morphisms

The reader is referred to EGA IV §§ 17 & 18, and pending its publication, to SGA 1, I, II, III (where it is however
appropriate to replace certain noetherian hypotheses, troublesome in applications, by hypotheses of finite
presentation).

**Definition 1.1.** *Let `S` be a prescheme, `F` a functor `(Sch)°/S → (Ens)`. One says that `F` is* formally smooth
*(resp.* formally unramified [^XI-1-1]*, resp.* formally étale\*) if for every `S`-prescheme `S′`, affine (in the
absolute sense), and every subscheme `S″` of `S′` defined by a nilpotent ideal `J`, the map\*

```text
F(S′) ⟶ F(S″)
```

*is surjective (resp. injective, resp. bijective). A prescheme `X` over `S` is said to be* formally smooth over `S`
*(resp.* formally unramified over `S`*, resp.* formally étale over `S`*) if the corresponding functor is formally smooth
(resp. formally unramified, resp. formally étale); one says that `X` is* smooth over `S` *(resp.* unramified over `S`*,
resp.* étale over `S`*) if it satisfies the preceding condition and if moreover `X` is locally of finite presentation
over `S`.*

<!-- label: III.XI.1.1 -->

<!-- original page 129 -->

The interest of these definitions for `X` resides in the fact that, on the one hand, they are expressed in a remarkably
simple way in terms of the functor represented by `X` (and in practice, `X` is often given as the object over `S`
representing some explicit functor), and that, on the other hand, they are also expressed by remarkable properties
concerning the local structure of `X`, which we shall recall in the following statements (for the proof, we refer to
loc. cit.).

**Proposition 1.2.** *Let `X` be a prescheme locally of finite presentation over `S`. Then:*

<!-- label: III.XI.1.2 -->

*(i) For `X` to be smooth over `S`, it is necessary and sufficient that `X` be flat over `S`, and that its geometric
fibers `X ⊗_S Spec(κ(s))` be regular schemes. More generally, for `X` to be smooth over `S` in a neighborhood of the
point `x ∈ X` (one then says that `X` is* smooth over `S` at `x`*), it is necessary and sufficient that `X` be flat over
`S` at `x` and `X_s` be smooth over `κ(s)` at `x`, i.e. `X_s ⊗_{κ(s)} κ̄(s)` be regular at the points (or simply, a
point) above `x`.*

*(ii) Suppose `S`, and hence `X`, locally noetherian; let `x ∈ X` and let `s ∈ S` be its image in `S`. Then the smooth
nature of `X` over `S` at `x` is detected on the local homomorphism `A = O_{S,s} → B = O_{X,x}` of noetherian local
rings (or even on the local homomorphism `Â → B̂` of their completions), by the following characteristic property: `B`
is flat over `A`, and `B ⊗_A k` is geometrically regular over `k` (the residue field of `A`), i.e. for every finite
extension `k′` of `k`, `(B ⊗_A k) ⊗_k k′ = B ⊗_A k′` is a regular semi-local ring. When the residual extension
`k(B)/k(A)` is trivial, these conditions are equivalent also to the following: `B̂` is isomorphic as `Â`-algebra to an
algebra of formal power series `Â[[t_1, …, t_n]]`.*

Thus, from the "formal" point of view, the structure of `X` over `S` is that of the typical affine space
`S[t_1, …, t_n]` over `S`.

**Proposition 1.3.** *Let `X` be a prescheme locally of finite presentation over `S`. Then:* <!-- original page 130 -->

<!-- label: III.XI.1.3 -->

*(i) The following conditions are equivalent:*

*a) `X` is unramified over `S`.*

*b) The diagonal morphism `X → X ×_S X` is an open immersion.*

*c) `Ω¹_{X/S} = 0`.*

*d) The geometric fibers of `X/S` are discrete and reduced, i.e. isomorphic to sums of copies of the base field.*

*e) For every `s ∈ S`, the fiber `X ⊗_S Spec κ(s) = X_s` is unramified over `κ(s)`, or equivalently is isomorphic to a
sum of spectra of finite separable extensions of `κ(s)`.*

*(ii) One has analogous conditions of pointwise nature for `X` to be unramified over `S` at a given point `x` (i.e. in a
neighborhood of the said point); for example, it is necessary and sufficient that `O_{X_s, x}` be a finite separable
extension of `κ(s)`, which is expressed also in terms of the local homomorphism `A = O_{S,s} → B = O_{X,x}` by the
condition that `B ⊗_A k` be a finite separable extension of `k` (residue field of `A`), i.e. `r(A) B = r(B)` and `k(B)`
is a finite separable extension of `k(A)`. When `A`, and hence also `B`, is noetherian, and `k(A) ⥲ k(B)`, this means
also that `Â → B̂` is surjective.*

Thus, from the "formal" point of view, to say that `X` is unramified over `S` means that `X` is essentially a
subprescheme of `S`. Observe also that conditions d) and e) are expressed solely in terms of the fibers of `X/S`.

**Proposition 1.4.** *Let `X` be a prescheme locally of finite presentation over `S`. For `X` to be étale over `S`, it
is necessary and sufficient that it be smooth over `S` and unramified over `S` (trivial by definition), which permits
applying criteria 1.2 and 1.3. One finds in particular:*

<!-- label: III.XI.1.4 -->

\*(i) For `X` to be étale over `S`, it is necessary and sufficient that it be flat over `S` and unramified over `S`.

<!-- original page 131 --> Analogous local criterion for `X` to be étale over `S` at a given point `x`.*

*(ii) Suppose moreover `S`, and hence `X`, locally noetherian. Then the fact that `X` is étale over `S` at a point `x`
is detected on the local homomorphism `A = O_{S,s} → B = O_{X,x}` (and even on the local homomorphism `Â → B̂`) by the
following characteristic property: `B` is flat over `A`, and `B ⊗_A k` is a finite separable extension of `k` (residue
field [^N.D.E-XI-1] of `A`). When `k(A) ⥲ k(B)`, this condition means simply that `Â → B̂` is an isomorphism.*

Thus, from the "formal" point of view, to say that `X` is étale over `S` means simply that `X` is locally isomorphic to
`S`.

**Remark 1.5.** When `X` is locally of finite presentation over `S` and one is given a point `x ∈ X`, then the fact that
`X` is smooth (resp. unramified, resp. étale) over `S` at `x`, i.e. in a neighborhood of `x`, is detected on the functor
`X : (Sch)°/S → (Ens)` by the following property: for every `S′` over `S`, `S′` the spectrum of a local ring, every
subscheme `S″` of `S′` defined by a nilpotent ideal, and every `S`-morphism `u″ : S″ → X` sending the closed point `s″`
of `S″` to `x`, there exists at least one (resp. at most one, resp. exactly one) `S`-morphism `u : S′ → X` which extends
it. This statement shows in particular that in definition 1.1 one may restrict to `S′` which are local schemes (provided
that the functor in question is representable by a prescheme locally of finite presentation over `S`). On the other
hand, when `S` is locally noetherian, one may even, in the preceding pointwise criterion, restrict to `S′` which are
local artinian schemes, and one may thus impose the same restriction on `S′` in definition 1.1 (provided that `S` is
locally noetherian and the functor in question is represented by a prescheme locally of finite type over `S`).

<!-- label: III.XI.1.5 -->

<!-- original page 132 -->

**Remark 1.6.** Of course, given a morphism `f : X → Y` of preschemes, one will say that `f` is smooth (resp. …) if `f`
makes `X` into a smooth (resp. …) `Y`-prescheme. When `X` and `Y` are `S`-preschemes and `f` an `S`-morphism of finite
presentation, then these properties of `f` are expressed immediately in terms of the morphism of functors
`F, G : (Sch)°/S → (Ens)` defined by `f`: `f` is smooth (resp. unramified, resp. étale) if for every `S`-prescheme `S′`,
`S′` affine (in the absolute sense), and every subscheme `S″` of `S′` defined by a nilpotent ideal `J`, the map

```text
F(S′) ⟶ F(S″) ×_{G(S″)} G(S′)
```

deduced from the commutative square

```text
F(S′) ⟶ G(S′)
  ↓        ↓
F(S″) ⟶ G(S″)
```

is surjective (resp. injective, resp. bijective), i.e. for every commutative square of morphisms of functors over `S`
(where `S′`, `S″` are as above and `i : S″ → S′` is the canonical immersion):

```text
        i
   S″ ─────→ S′
   │          │
u″ │          │ v
   ↓    f     ↓
   F ──────→ G                            (Q)
```

<!-- label: III.XI.1.6 -->

there exists at least one (resp. at most one, resp. exactly one) morphism `u : S′ → F` making the two corresponding
triangles commutative: `u″ = u i` and `v = f u`.

<!-- label: III.XI.1.6 -->

This property for a homomorphism of functors `f : F → G` over `S` keeps its meaning even when the functors in question
are not representable; one will say (if it is satisfied) that the homomorphism of functors `f : F → G` is *formally
smooth* (resp. *formally unramified*, resp. *formally étale*). One will note that this depends only on the homomorphism
of functors `(Sch)° → (Ens)` defined by `F`, `G` (cf. I 1.4.1), and not on the structural morphisms `F → S` and `G → S`.
An equivalent way of expressing the preceding definition, somewhat more manageable in applications, is the following:
the morphism of functors `F → G` over `S` is said to be formally smooth (resp. formally unramified, resp. formally
étale) when, for every `S′` over `S` and every morphism `S′ → G`, the functor `F′ = F ×_G S′` over `S′` is formally
smooth (resp. formally unramified, resp. formally étale).

**Remark 1.7.** Under the conditions of 1.6, when one is given a "point of `F`" with values in a field `k`, i.e. an
element `x` of `F(Spec(k))` or, what amounts to the same, a morphism `Spec(k) → F`, one says likewise that `f` is
*formally smooth* (resp. *formally unramified*, resp. *formally étale*) *at* `x`, if the condition of the preceding
definition is satisfied whenever `S′` is a local scheme and the morphism `S″ → F` in the diagram `(Q)` above is
"compatible with the marked points" in the following sense: if `k′` denotes the residue field of `S′` and of `S″` at
their closed point, the diagram

```text
Spec(k′)        Spec(k)
   │              │
 j ↓              ↓ x
   S″ ──────────→ F
```

(where `j : Spec(k′) → S″` denotes the canonical immersion) can be completed in <!-- original page 134 --> a commutative
diagram

```text
              Spec(k″)
             ╱        ╲
           ╱            ╲
         ↓                ↓
   Spec(k′)             Spec(k)
       │                  │
       ↓                  ↓
       S″ ──────────────→ F           ,
```

<!-- label: III.XI.1.7 -->

where `k″` is the spectrum of a field. When `F`, `G` are representable by `S`-preschemes `X`, `Y` and the `S`-morphism
`f : X → Y` is locally of finite presentation, this condition means precisely (by virtue of 1.5) that `f : X → Y` is
smooth at the point of `X` image of `Spec(k)` by `x : Spec(k) → X`.

**Remark 1.8.** When the condition of the preceding definition is satisfied while restricting to local artinian `S′`,
one will say that `F → G` is *infinitesimally smooth* (resp. *infinitesimally unramified*, resp. *infinitesimally
étale*) *at* `x`, and one says that `F → G` is infinitesimally smooth (resp. …) if it is so at every point `x`, in other
terms if the condition envisaged in 1.6 is satisfied whenever `S′` is local <!-- original page 90 --> artinian. This
variant of the preceding notions is technically useful, since it is often easier to verify, being a weaker notion, while
being frequently sufficient (for example if `F → G` is a morphism locally of finite presentation, with `G` representable
by a prescheme locally noetherian…) to entail the strong condition.

<!-- label: III.XI.1.8 -->

Smooth morphisms of preschemes behave in a remarkably simple way with respect to differential calculus. We confine
ourselves here to recalling the following property:

**Proposition 1.9.** *Let `f : X → S` be a smooth morphism of preschemes. Then `Ω¹_{X/S}` is a locally free module of
finite type over `X`, and its rank at a point `x ∈ X` equals the dimension of the fiber `X_s` (where `s = f(x)`) in a
neighborhood of the point `x`.*

<!-- label: III.XI.1.9 -->

<!-- original page 135 -->

This dimension is called the *relative dimension of `X` over `S` at `x`*. One will note that it is zero (when `f` is
smooth at `x`) if and only if `f` is étale at `x`. This dimension is computed in practice still in terms of the functor
`F` represented by `X`, in the following way. Let `ξ` be a point of `F` with values in a field `k`, "localized at `x`",
i.e. a morphism `Spec(k) → F = X` whose image is `x`. Consider the algebra `D(k) = k[t]/(t²)` of dual numbers over `k`,
considered as an `S`-prescheme, and consider the map

```text
F(D(k)) ⟶ F(k)
```

deduced from the augmentation `D(k) → k`, and let finally `F(D(k), ξ)` be the inverse image of `ξ ∈ F(k)` under this
map. Then this set is naturally endowed with a structure of vector space over `k` (in fact, it is the vector space dual
of `Ω¹_{X/S} ⊗_{O_{X,x}} k`), whose dimension is the relative dimension of `X` over `S` at `x`.

To make explicit the vector law on `F(D(k), ξ)`, it is convenient to introduce more generally, as in Exp. II, for every
vector space `V` over `k`, the algebra `D_k(V) = k + V` (with `V` an ideal of square zero), and to consider
`F(D_k(V), ξ)`, the inverse image of `ξ` by `F(D_k(V)) → F(k)`, as a covariant functor in `V`, with values in `(Ens)`.
It then suffices that this functor commute with products of two factors (which means that `F` transforms certain
amalgamated sums of a very special type into fibered products, compare Exp. II — a condition always satisfied when `F`
is representable), to conclude that the `F(D_k(V), ξ)` and in particular `F(D(k), ξ)` are endowed with vector structures
over `k`. One can thus define the relative dimension of `F` over `X` at the "point" `ξ`, under conditions appreciably
broader than the representability of `F`.

In the present Exposé, the fact that certain functors which we shall make explicit are representable by preschemes
smooth over `S` will serve us mainly through the intermediary of the following result, which will be for us the
technical intermediary to pass from constructions on the completion of the local ring `A` of a point `s` of a noetherian
scheme `S` <!-- original page 136 --> to a local ring `A′` over `A` étale over `A`, which will yield in particular a
means of passing from `s` to neighboring points:

**Proposition 1.10.** *Let `f : X → S` be a smooth morphism of preschemes, `s` a point of `S`, and `x` a point of `X`
above `s` such that `κ(x)` be a finite separable extension of `κ(s)`. Then there exists a subscheme `S′` of `S`, étale
over `S`, passing through `x`. Hence one can find an étale morphism `S′ → S`, a point `s′` of `S′` above `s` of residue
extension equal to `κ(x)/κ(s)`, and an `S`-morphism `S′ → X` sending `s′` to `x`.*

<!-- label: III.XI.1.10 -->

To construct `S′`, one simply takes a system `g_1, …, g_n` of sections of `O_X` on a neighborhood of `x`, which induce
at `x` a regular system of parameters of the local ring of the fiber `X_s` at `x`; the subscheme `S′` defined by the
`g_i` is then étale over `S` at `x`, and provided one shrinks `S′`, it will then be étale over `S`.

We shall use 1.10 when `κ(x) = κ(s)`, i.e. `x` is rational over `κ(s)`, i.e. `x` can be considered as a section of `X_s`
over `Spec(κ(s))`. Then 1.10 is in the nature of a theorem of extension of sections (after étale extension of the base).
It takes a particularly simple form in the following special case:

**Corollary 1.11.** *Under the conditions of 1.10, suppose that `S` is the spectrum of a henselian local ring, and that
`κ(x) = κ(s)`. Then there exists a section of `X` over `S` passing through `x` (uniquely determined if `X` is in fact
étale over `S` at `x`).*

<!-- label: III.XI.1.11 -->

Indeed, `S` being henselian, it follows under the conditions of 1.10 that `S′` contains an open subscheme which is
finite over `S` and whose fiber at `s` is reduced to `x`. As it is étale over `S`, it follows that it is isomorphic to
`S`, whence the conclusion. — One will note that when `S` is the spectrum of a complete local ring, 1.10 or 1.11 is more
or less the equivalent of the classical "Hensel's lemma", and one sometimes refers to it by this name.

## 2. Examples of formally smooth functors drawn from the theory of multiplicative-type groups

<!-- original page 137 -->

We are going to interpret, in the language introduced in the preceding N°, the results stated in IX 3 concerning
infinitesimal extensions of a homomorphism of a group of multiplicative type (consequences of the vanishing of the
Hochschild cohomology of such a group, established in Exposé I).

**Proposition 2.1.** *Let `S` be a prescheme, `H` a group of multiplicative type over `S`, `G` an `S`-prescheme in
groups smooth over `S`; consider the functor over `S`*

```text
M_H = Hom_{S-gr.}(H, G)
```

*(whose value at `S′` over `S` is the set of homomorphisms of `S′`-groups from `H_{S′}` to `G_{S′}`). This functor is
formally smooth over `S`.*

<!-- label: III.XI.2.1 -->

Cf. IX 3.6. More generally:

**Corollary 2.2.** *Let `S`, `G` be as above, and consider a homomorphism `u : H_1 → H_2` of group schemes of
multiplicative type over `S`, whence with the preceding notation a morphism of functors over `S`:*

```text
M_{H_2} ⟶ M_{H_1}        (M_{H_i} = Hom_{S-gr.}(H_i, G)),
```

*given by `w ↦ w ∘ u`. This homomorphism is formally smooth.*

<!-- label: III.XI.2.2 -->

Indeed, by virtue of definitions 1.6, this is equivalent to the following statement: when `S` is affine, `S′` a
subscheme defined by a nilpotent ideal, let

```text
v : H_1 ⟶ G
```

be a homomorphism of `S`-groups, and

```text
w′ : (H_2)_{S′} ⟶ G_{S′}
```

<!-- original page 138 --> a homomorphism of `S′`-groups such that `w′ u_{S′} = v_{S′}`; there then exists a

homomorphism of `S`-groups

```text
w : H_2 ⟶ G
```

extending `w′`, and such that `w u = v`. To see this, one begins by extending `w′` to a homomorphism of `S`-groups
`w_0 : H_2 → G`, which is possible by 2.1; consider then `v′ = w_0 u : H_1 → G`. It is such that `v′_{S′} = v_{S′}` by
hypothesis on `w′`, hence by virtue of VIII 3.6 there exists an element `g` of `G(S)`, whose image in `G(S′)` is the
unit element, and such that `v = int(g) v′`, whence `v = (int(g) w_0) u`, and it will therefore suffice to take
`w = int(g) w_0`.

**Corollary 2.3.** *With the notation of 2.1, consider `M_H = M` as a functor with group of operators `G` (`G` operating
by `(v, g) ↦ int(g) ∘ v`). Then the corresponding morphism*

```text
R : G ×_S M ⟶ M ×_S M
```

*defined by `(g, v) ↦ (int(g) ∘ v, v)` is a formally smooth morphism.*

<!-- label: III.XI.2.3 -->

By means of a base change `S′ → S`, this is equivalent to the following statement:

**Corollary 2.4.** *With the notation of 2.1, let `v_1, v_2 : H → G` be two morphisms of `S`-groups, and let
`Transp(v_1, v_2)` be the subfunctor of `G` formed of the `g` such that `int(g) ∘ v_1 = v_2`. Then this functor is
formally smooth over `S`. In particular (if `v_1 = v_2 = v`) the functor `Centr(v)`, subgroup of `G` formed of the `h`
such that `int(h) v = v`, is formally smooth over `S`.*

<!-- label: III.XI.2.4 -->

<!-- original page 139 -->

(N.B. The pair `(v_1, v_2)` can be considered as a section over `S` of the second member in the morphism `R` of 2.3, and
`Transp(v_1, v_2)` as the inverse image functor of the said section under `R`.) Statement 2.4 itself is equivalent to
the following: when `S` is affine and `S′` is a subscheme of `S` defined by a nilpotent ideal, for every `g_0 ∈ G(S′)`
such that `int(g_0)(v_1)_{S′} = (v_2)_{S′}`, `g_0` extends to a `g ∈ G(S)` such that `int(g) v_1 = v_2`. To prove this,
one begins by extending `g_0` to a section `g′` of `G` over `S`, which is possible since `G` is smooth over `S`; one
sets `v′_2 = int(g′) v_1`, one notes that `v_2` and `v′_2` have the same restriction over `S′`, hence by the result
already invoked IX 3.6 there exists a `g″ ∈ G(S)`, inducing the unit section over `S′`, and such that
`v_2 = int(g″) v′_2`, whence `v_2 = int(g″) int(g′) v_1 = int(g″ g′) v_1`, so that it suffices to take `g = g″ g′`.

**Proposition 2.1 bis.** *Let `S` be a prescheme, `G` an `S`-prescheme in groups smooth over `S`, and consider the
functor `M : (Sch)°/S → (Ens)`:*

```text
M(S′) = set of multiplicative-type subgroups of G_{S′}.
```

*Then `M` is formally smooth over `S`.*

<!-- label: III.XI.2.1bis -->

Cf. IX 3.6 bis.

**Corollary 2.2 bis.** *Let `n` be an integer, and consider the morphism of functors*

```text
φ_n : M ⟶ M
```

*defined by*

```text
φ_n(H) = ₙH = Ker(n · id_H).
```

*Then `φ_n` is a formally smooth morphism. If for every integer `p > 0`, `M_p` denotes the subfunctor of `M` such that
`M_p(S′)` is the set of multiplicative-type subgroups `H` of `G_{S′}` such that `ₚH = H`, then the morphism induced by
`φ_n`:*

```text
M_{np} ⟶ M_n
```

*is formally smooth.*

<!-- label: III.XI.2.2bis -->

<!-- original page 140 -->

The second assertion is trivially contained in the first and is included only for the convenience of a later reference.
The proof of the first is analogous to that of 2.2, invoking this time IX 3.6 bis.

**Corollary 2.3 bis.** *With the notation of 2.1 bis, consider `M` as a functor with group of operators `G` (`G`
operating by `(g, H) ↦ int(g)(H)`). Then the corresponding morphism*

```text
R : G ×_S M ⟶ M ×_S M
```

*defined by `(g, v) ↦ (int(g) v, v)` is formally smooth.*

<!-- label: III.XI.2.3bis -->

This is equivalent to the following statement:

**Corollary 2.4 bis.** *With the notation of 2.1 bis, let `H_1, H_2` be two multiplicative-type subgroups of `G`, and
let `Transp_G(H_1, H_2)` be the subfunctor of `G` formed of the `g` such that `int(g) H_1 = H_2`. Then this functor is
formally smooth over `S`. In particular, if `H_1 = H_2 = H`, the subfunctor `Norm_G(H)` of `G`, normalizer of `H`, is
formally smooth over `S`.*

<!-- label: III.XI.2.4bis -->

The proof is analogous to that of 2.4, invoking again IX 3.6 bis.

**Proposition 2.5.** *Let `S` be a prescheme, `G` an `S`-prescheme in groups smooth over `S`, `K` a sub-`S`-prescheme in
groups, smooth over `S` or of multiplicative type, `H` an `S`-prescheme in groups of multiplicative type, `u : H → G` a
homomorphism of `S`-groups, and denote by `Transp_G(u, K)` the subfunctor of `G` whose value, at an `S′` over `S`, is
formed of the `g ∈ G(S′)` such that `int(g) u_{S′} : H_{S′} → G_{S′}` factors through `K_{S′}`. Then this functor is
formally smooth over `S`.*

<!-- label: III.XI.2.5 -->

The proof is analogous to that of 2.2, invoking IX 3.6 and X 2.1 (the latter in the case `K` of multiplicative type).

<!-- original page 141 -->

## 3. Auxiliary representability results

**Proposition 3.1.** *Let `F → S` be a functor over the prescheme `S`. The following conditions are equivalent:*

<!-- label: III.XI.3.1 -->

*(i) `F` is representable, and `F → S` is an open immersion (one also says simply that `F → S` is an open immersion).*

*(ii) `F` is a sheaf for the faithfully flat quasi-compact topology, "commutes with inductive limits of rings", `F → S`
is a monomorphism, and finally the following condition is satisfied: for every local prescheme `S′` over `S`, of residue
field `k`, and every `S`-morphism `Spec(k) = S″ → F`, there exists an `S`-morphism `S′ → S` which extends it.*

*(iii) (When `S` is locally noetherian.) `F` is a sheaf for the faithfully flat quasi-compact topology, "commutes with
inductive limits of rings", "commutes with adic projective limits of local artinian rings", `F → S` is a monomorphism,
and is infinitesimally étale (cf. 1.8).*

Let us first make precise two points of terminology.

**Remark 3.2.** One says that a functor [^N.D.E-XI-2] `F` over `S` "*commutes with inductive (understood: filtered)
limits of rings*" if for every filtered projective system `(S′_i)_{i ∈ I}` of `S`-affine schemes above an affine open of
`S`, with rings `A′_i`, the natural homomorphism

```text
(*)    lim_→ F(S′_i) → F(S′)   (where S′ = Spec A′, A′ = lim_→ A′_i)
```

<!-- label: III.XI.3.2 -->

<!-- original page 142 -->

is bijective. One will note that `S′` is none other than the projective limit of `(S′_i)` in the category of preschemes
(and even of all ringed spaces), so that the condition envisaged is in the nature of a right-exactness condition
(commutation with certain inductive limits in `(Sch)°/S`), just as the condition of being a sheaf for some topology. One
will pay attention to the fact that the condition envisaged is essentially relative, i.e. involves the morphism `F → S`
and not only the functor `F : (Sch)° → (Ens)`; more precisely, in `(*)`, `F(S′_i)` and `F(S′)` denote `Hom_S(S′_i, F)`,
`Hom_S(S′, F)`. Thus, when `F` is representable, the condition envisaged means that `F` is locally of finite
presentation over `S`. (And we have used several times, in the last two Exposés, the fact that a functor represented by
an `S`-prescheme locally of finite presentation commutes with inductive limits of rings.)

**Remark 3.3.** One says that a functor [^N.D.E-XI-2] `F` over `S` *commutes with adic projective limits of local
artinian rings* if for every `S′` over `S` which is the spectrum of a complete noetherian local ring `A′`, setting
`S′_n = Spec(A′/rad(A′)^{n+1})`, the natural map

```text
(**)    F(S′) ⟶ lim_← F(S′_n)
```

<!-- label: III.XI.3.3 -->

is bijective. One will note that this condition, which is in the nature of a left-exactness condition, is satisfied
whenever `F` is representable. One sees easily that, contrary to the condition of commutation with inductive limits of
rings, it is intrinsic to `F` as an element of `Ob(Ŝch)`, i.e. it does not involve the morphism `F → S`.

**Remark 3.4.** Let `F` be a functor over `S` which is a sheaf for the Zariski topology, or as one also says, which is
"of local nature". (It suffices for this that `F` be a sheaf for a finer topology, such as the faithfully flat
quasi-compact topology.) Let `(S_i)` be a covering of `S` by opens; then one easily verifies (by a method of gluing
pieces) that `F` is representable if and only if the `F_i = F ×_S S_i` are, <!-- original page 143 --> which allows for
example reduction to the case where `S` is affine. Suppose that the functor `F` of local nature commutes with inductive
limits of rings. Then, for `F` to be representable, it is necessary and sufficient that its restriction to the category
of preschemes locally of finite presentation over `S` be representable. The "necessary" was pointed out in 3.2; the
"sufficient" amounts to this: if `X` is a prescheme locally of finite presentation over `S` and `X → F` a morphism such
that, for every `S′` locally of finite presentation over `S`, the induced morphism

```text
Hom_S(S′, X) ⟶ Hom_S(S′, F)
```

<!-- label: III.XI.3.4 -->

is bijective, then `X → F` is an isomorphism. Now this results easily from the fact that `X` and `F` are two functors of
local nature which commute with inductive limits of rings.

Let us now prove 3.1. The implications (i) ⇒ (ii) and (i) ⇒ (iii) are evident; let us prove the inverse implications.

One has (ii) ⇒ (i). Let `U` indeed be the set of `s ∈ S` such that the canonical monomorphism `Spec(κ(s)) → S` factors
through `F`. By virtue of the last condition (ii), for every `s ∈ U`, the canonical monomorphism `Spec(O_{S,s}) → U`
factors through `F`. Noting that `O_{S,s}` is the inductive limit of the rings of affine neighborhoods of `s`, it
follows from the fact that `F` commutes with inductive limits of rings that for every `s ∈ S`, there exists an open
neighborhood `U_s` such that the canonical immersion `U_s → S` factors through `F`. This implies `U_s ⊂ U`, so `U` is
open. As `F → S` is a monomorphism, and `F` is of local nature, the `S`-morphisms `U_s → F` glue on the intersections
`U_s ∩ U_{s′}` (`s, s′ ∈ U`), hence come from an `S`-morphism `U → F`. It remains to prove that this is an isomorphism,
hence that every `S`-morphism `S′ → F` factors uniquely through `U` (where `S′` is an `S`-prescheme). As `F → S` and
`U → S` are monomorphisms, it amounts to the same to say that the structural morphism `S′ → S` factors through `U`,
which reduces us to the case where `S′` is the spectrum of a field, hence reduced to a single point <!-- original page
144 --> `s′`. Let `s` be the point of `S` below `s′`; I say that the `S`-morphism `S′ → F` factors through
`Spec(κ(s)) = S_0 → F` (which implies `s ∈ U` and will prove what we want).

It amounts to the same, since `S′ → S_0` is covering for fpqc and `F` is a sheaf for this topology, that the two
composites

```text
S″ = S′ ×_{S_0} S′ ⇉ S′ → F
```

are the same, which follows from the fact that `F → S` is a monomorphism.

One has (iii) ⇒ (ii) (when `S` is locally noetherian). It suffices to prove the last condition of (ii), and moreover (by
virtue of the preceding proof) it suffices to do so when `S′` is of the form `Spec(O_{S,s})`, with `s ∈ S`. Let
`A = O_{S,s}`, `A_n = A/m^{n+1}`, `S_n = Spec(A_n)`. Then it follows from the hypothesis that `F → S` is infinitesimally
smooth, that the given morphism `S_0 → F` extends to morphisms `S_n → F`. As `F → S` is a monomorphism, one thus obtains
an element of `lim_← F(S_n)`, and since `F` commutes with adic projective limits of local artinian rings, the `S_n → F`
come from a morphism `Spec(Â) = Ŝ′ → F`. As `F → S` is a monomorphism, `F` a sheaf for fpqc, and `Ŝ′ → S′` covering for
the said topology, this morphism `Ŝ′ → F` factors through `S′ → F`, which completes the proof.

**Proposition 3.5.** *Let `S` be a locally noetherian prescheme, `F → S` a functor over `S`, `(X_i, u_i)_{i ∈ I}` a
family of `S`-morphisms `u_i : X_i → F`, where the `X_i` are preschemes locally of finite type over `S`. Suppose the
following conditions are satisfied:*

<!-- label: III.XI.3.5 -->

*a) `F` is a sheaf for the faithfully flat quasi-compact topology, commutes with inductive limits of rings, commutes
with adic projective limits of local artinian rings.*

*b) The `u_i : X_i → F` are monomorphisms, and are infinitesimally étale (cf. 1.8).* <!-- original page 145 -->

*c) The family of the `u_i` is "set-theoretically surjective".*

*Under these conditions, `F` is representable by a prescheme locally of finite type over `S` (and the `u_i` are open
immersions, which make the family of the `X_i` into an open covering of `F`).*

**Remark 3.6.** Proceeding as at the end of Remark 1.7, one defines, for every functor `F : (Sch)° → (Ens)`, an
"underlying set" `set(F)` as a quotient set of the set of points of `F` with values in fields (for the equivalence
relation made precise in 1.7). When `F` is representable by `X`, one recovers the underlying set of `X`. Evidently
`set(F)` depends functorially on `F`, so that if `G → F` is a morphism of functors, one will say that this morphism is
*set-theoretically surjective* if the induced map `set(G) → set(F)` is surjective. This means therefore also that every
point of `F` with values in a field `k` "comes from" a point of `G` with values in a suitable extension of `k`. This
definition extends immediately to the case of a family of morphisms `G_i → F`, which makes precise the meaning of c).

<!-- label: III.XI.3.6 -->

Let us prove 3.5. For this, let us introduce, for `(i, j) ∈ I × I`,

```text
X_{i,j} = X_i ×_F X_j,
```

and consider the projections

```text
v_{i,j} : X_{i,j} ⟶ X_i    and   w_{i,j} : X_{i,j} ⟶ X_j.
```

I say that these last are representable by open immersions. To see it, one applies criterion 3.1 (iii): `X_{i,j}`
satisfies the three exactness conditions (being a sheaf, commuting with `lim_→` of rings and with adic `lim_←` of local
artinian rings), since `F`, `X_i`, `X_j` satisfy them, and these conditions are stable under finite projective limits,
in particular under fibered products; <!-- original page 146 --> since `X_i → F` is a monomorphism, so is
`v_{i,j} : X_{i,j} → X_i` deduced from it by base change `X_j → F`, and symmetrically `v_{j,i}` is a monomorphism;
finally the "infinitesimally étale" condition is also preserved by base change. This proves that one is under the
conditions of 3.1 (iii).

We may now use the `X_i`, `X_{i,j}`, `v_{i,j}` and `w_{i,j}` to construct in the usual way an `S`-prescheme `X` such
that the `X_i` are identified with opens of `X`, the `X_{i,j}` with the intersections `X_i ∩ X_j`, and the `v_{i,j}`,
`w_{i,j}` with the canonical immersions. Note that `X` is also the quotient of

```text
Y = ⨿_i X_i
```

by the equivalence relation `R = ⨿_{i,j} X_{i,j}` (the two projections `v, w : R ⇉ Y` being defined by the `v_{i,j}`
resp. the `w_{i,j}`). More precisely, `F` being a sheaf for fpqc, the `u_i : X_i → F` come from a `u : Y → F`, and `R`
is none other than the equivalence relation defined by `u`, `R = Y ×_F Y`; finally the quotient `X = Y/R` is also a
quotient in the category of fpqc-sheaves (and even, in the category of sheaves for the Zariski topology): it suffices to
use the definitions of "quotient" and "sheaf" to convince oneself. Consequently, `u` factors uniquely through a morphism

```text
ū : X ⟶ F,
```

and this morphism is a monomorphism. It remains to show that it is an isomorphism. As `F` is of local nature, one may
suppose `S` affine, and as moreover `F` commutes with inductive limits of rings, it suffices to verify that for every
`T` affine of finite type over `S`, every morphism `T → F` factors through `X` (cf. 3.4). For this, consider
`G = X ×_F T → T`. It suffices to prove that this is an isomorphism. Now, `T` being noetherian, one sees as above that
this is an open immersion (N.B. `X → F` is infinitesimally étale, as follows at once from the fact that the induced
morphisms `u_i : X_i → F` are). Now by hypothesis `X → F` is set-theoretically surjective, and one sees at once that
this is a condition stable under base change, <!-- original page 147 --> hence `G → T` is set-theoretically surjective,
hence an isomorphism since it is an open immersion. QED.

**Proposition 3.7.** *Let `S` be a locally noetherian prescheme, `I` a filtered increasing index set, `(T_i)_{i ∈ I}` a
projective system of `S`-preschemes locally of finite type, `T = lim_← T_i` the projective limit functor, `F` a functor
over `S`, `u : F → T` an `S`-morphism. Suppose the following conditions are satisfied:*

<!-- label: III.XI.3.7 -->

*a) `F` is a sheaf for the faithfully flat quasi-compact topology, commutes with inductive limits of rings, and with
adic projective limits of local artinian rings.*

*b) The morphism `u : F → T` is a monomorphism.*

*b′) The morphism `u : F → T` is infinitesimally étale.*

*c) For every point `ξ` of `F` with values in the spectrum of a field `k`, denoting by `ξ_i ∈ T_i(Spec(k))` its image
and by `t_i` the corresponding element of `T_i`, there exists an `i ∈ I` such that for `j ⩾ i` the transition morphism
`p_{i,j} : T_j → T_i` is étale at `t_j`.*

*d) For every prescheme `X` locally of finite type over `S`, and every `S`-morphism `X → F`, the set of `x ∈ X` at which
this morphism is infinitesimally étale is open.*

*Under these conditions, `F` is representable by a prescheme locally of finite type over `S`.*

Let us note immediately that in the case which will occupy us in the following N°, one will verify conditions c) and d)
through the following corollary:

**Corollary 3.8.** *Granting a), b), b′), conditions c) and d) are implied by the following:*

<!-- label: III.XI.3.8 -->

<!-- original page 148 -->

*c′) The `T_i` are smooth over `S`, and the transition morphisms `p_{i,j} : T_j → T_i` are smooth.*

*d′) For every point `ξ` of `F` with values in the spectrum of a field `k`, let `t_i(ξ)` be the element of `T_i` defined
by `ξ`, `d_i(ξ)` the relative dimension of `T_i` over `S` at `t_i(ξ)`, and `d(ξ) = sup d_i(ξ)`. Then:*

*1°) for every `ξ` as above, one has `d(ξ) < +∞`, and*

*2°) for every prescheme `X` locally of finite type over `S` and every `S`-monomorphism `v : X → F`, the function
`x ↦ d(ξ_x)` on `X` is locally constant (where for `x ∈ X` one denotes by `ξ_x` the point of `F` with values in `κ(x)`
induced by `v`).*

Let us prove 3.7. Let us place ourselves under the conditions of c); let `t` be the element of `set(F)` defined by `ξ`
(cf. 3.6) and set

```text
O_t = lim_→ O_{T_i, t_i}.
```

Then using the condition stated in c), one sees easily that `O_t` is a noetherian local ring (EGA 0_IV 10.3.1.3). Its
residue field `κ(t)` is the inductive limit of the residue fields `κ(t_i)`, and `k` is an extension of it. If `η`
denotes the spectrum of `κ(t)`, `ξ` that of `k`, one has a commutative diagram

```text
ξ ─→ F
↓     ↓
η ─→ T          ,
```

whose definition is evident and left to the reader. As `ξ → η` is covering for the fpqc topology, `F` is a sheaf for it
by virtue of a), and `F → T` is a monomorphism by virtue of b), one sees at once that the morphism `η → T` factors
(uniquely) through a morphism `η → F`. Let us note now the

<!-- original page 149 -->

**Lemma 3.9.** *Under the conditions of 3.7, let `T_0 = Spec(A)` be a noetherian local scheme, `T_0″ = Spec(k(A))`,
`i : T_0″ → T_0` the canonical immersion, and suppose given a commutative square of morphisms*

```text
T_0″ ─→ F
  │      │
i ↓      ↓
T_0  ─→ T       .
```

*Then there exists a unique `T`-morphism `T_0 → F`.*

<!-- label: III.XI.3.9 -->

The proof is that of 3.1 (iii) ⇒ (ii) (where the fact that the `S` of the cited statement be representable was not
used), using that `F` is a sheaf for the fpqc topology, commutes with adic projective limits of local artinian rings (in
this case the `A/rad(A)^{n+1}`), and that `F → T` is a monomorphism and is infinitesimally étale.

We shall apply lemma 3.9 to the case where `T_0 = Spec(O_t)`, hence `T_0″ = Spec(κ(t))`, noting that we have just
constructed `T_0″ → F`, and that the canonical homomorphisms `O_{T_i, t_i} → O_t` define a projective system of
morphisms `Spec(O_t) → T_i`, whence a canonical morphism `Spec(O_t) → T`. The commutativity of the corresponding square
(×) is trivial (since by definition of `T`, it suffices to verify it with `T` replaced by `T_i`), whence a unique
`T`-morphism

```text
v′ : T_0 = Spec(O_t) ⟶ F.
```

As `F` commutes with inductive limits of rings, this morphism factors through

```text
v′_i : T′_i = Spec(O_{T_i, t_i}) ⟶ F
```

for `i` large. For such an `i`, one has

```text
T_0 ⥲ T′_i      i.e.        O_{T_i, t_i} ⥲ O_t.
```

Indeed, as `T_0 → T′_i` is faithfully flat quasi-compact, hence an effective epimorphism, <!-- original page 150 --> it
suffices to see that it is a monomorphism. Now if one has two morphisms `R ⇉ T_0` (with `R` representable) having the
same composite with `T_0 → T′_i`, they have the same composite with `T_0 → T` (which factors through `T_0 → T′_i`),
hence the same composite with `T_0 → T_j` for every `j`, hence with `T_0 → T′_j` for every `j`, hence are equal because
`T_0` is the projective limit of the `T′_j` in the category `(Sch)`.

Consider the diagram

```text
              v′
        T_0 ───────→ F
         │          ↗
         │       ↗ v′_i
         ↓     ↗
       T′_i ──────→ T_i           ,
```

where the unspecified arrows are the obvious ones. The square is commutative and so is the upper triangle, hence as
`T_0 → T′_i` is an epimorphism, it follows that the lower triangle is commutative. Now `O_{T_i, t_i}` is the inductive
limit of the affine rings of affine open neighborhoods of `t_i` in `T_i`, hence as `F` commutes with inductive limits of
rings, `v′_i` comes from a morphism

```text
v_t : U_t ⟶ F
```

from an open neighborhood `U_t` of `t_i` in `T_i`. One sees at once that, restricting this neighborhood if necessary,
`v_t` is necessarily a `T_i`-morphism (`T_i` being locally of finite type over `S`, hence also commuting with inductive
limits of rings). Then the composite of `v_t` with `F → T_i` is a monomorphism, hence `v_t` is a monomorphism. I say
that it is infinitesimally étale at `t_i`. Since `F → T` is infinitesimally étale, it amounts to the same to say that
the composite `T_i → F → T` is infinitesimally étale at `t_i`, or again that the induced morphism `T′_i → T` is
infinitesimally étale, or finally (since `T_0 ⥲ T′_i`) that <!-- original page 151 --> `T_0 → T` is infinitesimally
étale, which is immediate, this morphism being the projective limit of the infinitesimally étale morphisms `T′_i → T_i`.

Let us now apply condition d), which had not yet been used; it follows that `v_t` is infinitesimally étale in a
neighborhood of `t`, hence, restricting `U_t` to a smaller open if necessary, one may suppose that `v_t` is a
monomorphism infinitesimally étale.

For `t ∈ set(F)` variable, the family of morphisms `v_t` is amenable to 3.5, which implies the conclusion of 3.7.

Let us prove now 3.8, supposing satisfied conditions c′) and d′) of 3.8. Then with the notation of d′), one will have
`d_i(ξ) =` constant for `i` large, hence the relative dimension of `T_j` over `T_i` at `t_j`, equal to
`d_j(ξ) − d_i(ξ)`, is zero, hence `T_j → T_i` is étale at `t_j`, which proves condition c). Consequently the preceding
proof applies to give, for each `t ∈ set(F)`, an index `i`, an open neighborhood `U_t` of `t_i`, and a morphism
`U_t → F` which is a monomorphism, infinitesimally étale at `t_i`, and all reduces to proving that this morphism is
infinitesimally étale in a neighborhood of `t_i`. Now with the notation of d′) 2°), where one takes `X = U_t`, one may
suppose, replacing `U_t` by the connected component of `t_i` in `U_t` if necessary, that for every `x ∈ U_t`, one has

```text
d(ξ_x) = d(ξ_{t_i}) for every x ∈ U_t.
```

Now `d(ξ_{t_i})` = relative dimension of `T_i` over `S` at `t_i`, and as the relative dimension of `T_i` over `S`
remains constant on `U_t`, one will have also, for every `x ∈ U_t`:

```text
(*)    d(ξ_x) = relative dimension of U_t over S at x.
```

On the other hand, with the notation of the proof of 3.7, one sees at once that for every <!-- original page 152 -->
local noetherian prescheme `R_0 = Spec(A)`, setting `R_0″ = Spec k(A)`, every morphism `R_0 → F` such that the induced
morphism `R_0″ → F` factors through `F` (i.e. sends the closed point of `R_0` to `t ∈ set(F)`) factors (uniquely in an
obvious way) through `T_0`. (The proof is that of 3.1 or 3.9: one uses that `T_0 → F` is a monomorphism infinitesimally
étale at `t`, and that `T_0` is a sheaf for fpqc commuting with adic `lim_←` …). Applying this result to the morphism
`Spec(O_{U_t, x}) = R_0 → F` induced by `v_t` and to the point `t_x ∈ set(F)` image of the closed point of `R_0`, i.e.
image of `x` by `v_t`, one finds a factorization

```text
Spec(O_{U_t, x}) ⟶ Spec(O_{t_x}) ⟶ F
```

and as the second arrow is infinitesimally étale at `t_x`, to prove that the composite is so at `x`, it suffices to
prove that the first is so at `t_x`. Now thanks to formula (×) above, it is an `S`-homomorphism of localizations, at two
points `x`, `t_x`, of smooth `S`-preschemes `U_t`, `U_{t_x}` of the same relative dimension `d` over `S` at `t`, `t_x`.
This morphism is induced by an `S`-morphism

```text
w : U ⟶ V
```

where `U` is an open neighborhood of `x` in `U_t`, and `V = U_{t_x}` (EGA I 6.5.1). It all reduces to proving that this
morphism is étale at `x`. Moreover, `U` and `V` are equipped with monomorphisms `U → F`, `V → F`, and one sees at once
that, restricting `U` further if necessary, `w` is an `F`-morphism, hence `w` is a monomorphism. It now suffices to
prove the

**Lemma 3.10.** *Let `U`, `V` be two smooth `S`-preschemes, of the same relative dimension `d` over `S`, and `w : U → V`
an `S`-morphism which is a monomorphism; then `w` is an open immersion (and a fortiori is étale).*

<!-- label: III.XI.3.10 -->

By virtue of SGA 1, I 5.7, one is reduced to the case where `S` is the spectrum of a field, which one may suppose
algebraically closed. By virtue of SGA 1, I 5.1, it suffices to prove that `w` is étale, and it suffices to prove this
at the closed points of `U`. Let `x` be such a point, <!-- original page 153 --> `y = w(x)`; then, taking a regular
system of parameters `f_1, …, f_d` of `O_{V, y}`, one sees that `A = O_{U, x}/∑ f_i O_{U, x}` is the trivial extension
of `k = O_{V, y}/∑ f_i O_{V, y}` (for `w` being a monomorphism, so is the structural morphism `Spec(A) → Spec(k)`
deduced from it by base change). As `O_{U, x}` is a regular local ring of dimension `d`, it follows that the `f_i` form
a regular system of parameters of this ring, which immediately implies that `w` is étale at `x` and completes the proof
of 3.10, hence of 3.8.

**Corollary 3.11.** *Under the conditions of 3.8, for every quasi-compact open `U` of `F` separated over `S`, there
exists an `i ∈ I` such that for every `j ⩾ i` the morphism `u_j|U : U → T_j` is an open immersion. In particular, if the
`T_i` are quasi-affine over `S`, then every open `U` of `F` quasi-compact over `S`, i.e. of finite type over `S`, is
quasi-affine over `S`.*

<!-- label: III.XI.3.11 -->

The proof of 3.7 shows that for every `t ∈ F`, there exists an `i ∈ I` such that `u_i : F → T_i` is a local isomorphism
at `t`, and then `u_j` is a local isomorphism at `x` for every `j ⩾ i`. By reason of quasi-compactness, one may choose
`i` independent of `x ∈ U`. It remains to prove that for `i` large, `u_i|U : U → T_i` is a monomorphism. Now as `U → T`
is a monomorphism, one sees that the intersection of the equivalence relations `U ×_{T_i} U ⊂ U ×_S U` is reduced to the
diagonal, and as `U ×_S U` is a noetherian prescheme and the `U ×_{T_i} U` closed subpreschemes, it follows that one of
these `U ×_{T_i} U` is already reduced to the diagonal, i.e. `u_i|U` is a monomorphism. This proves the first assertion
in 3.11, and the second is an immediate consequence of it.

**Proposition 3.12.** *Let `S` be a prescheme, `G` an affine `S`-prescheme in groups.*

<!-- label: III.XI.3.12 -->

<!-- original page 154 -->

*a) Let `F` be the functor `(Sch)°/S → (Ens)` such that, for every `T` over `S`,*

```text
F(T) = set of multiplicative-type subgroups of G_T which are finite over T.
```

*Suppose `S` locally noetherian or `G` of finite presentation over `S`. Then the functor `F` is representable and is
affine over `S`. If `G` is of finite presentation over `S`, then `F` is locally of finite presentation over `S`.*

*b) Let `H` be an `S`-prescheme in groups of multiplicative type, and finite over `S`. Then `Hom_{S-gr.}(H, G)` is
representable. It is affine over `S`, and if `G` is of finite type (resp. of finite presentation) over `S`, the same
holds for `Hom_{S-gr.}(H, G)`.*

**Remark 3.13.** Except for the precision that `Hom_{S-gr.}` is affine, and in the case where `G` is of finite
presentation over `S` (which will suffice for us), 3.12 is an immediate consequence of the theory of Hilbert schemes (A.
Grothendieck, *Techniques de construction et théorèmes d'existence en Géométrie Algébrique: IV Les Schémas de Hilbert*,
Séminaire Bourbaki, May 1961, N° 221). It even suffices that `G` be quasi-projective over `S`; in case a), one may also
represent the larger functor

```text
F′(T) = { set of subpreschemes in groups of G_T,
          flat, proper and of finite presentation over T }
```

(the canonical monomorphism `F → F′` is an "open immersion", as follows from criterion 3.1 and from X 4.7 b), so that
the representability of `F′` entails that `F` is representable by an open of `F′`); in case b), one may restrict to
supposing that `H` is projective and of finite presentation over `S`. In both cases, one obtains a functor locally of
finite presentation over `S`. In the present Exposé, 3.12 is only a technical lemma for proving a key result in the
following N°, so we shall sketch an easy direct proof of 3.12, not using Hilbert schemes.

<!-- label: III.XI.3.13 -->

Let us first prove b). It will suffice to prove that `Hom_S(H, G)` is representable (independently of any group
structure on `H`, `G`), and has the supplementary properties stated for `Hom_{S-gr.}(H, G)`, since using also the same
result for `Hom_S(H ×_S H, G)`, one makes explicit the subfunctor `Hom_{S-gr.}(H, G)` of `Hom_S(H, G)` <!-- original
page 155 --> by a finite projective limit (in fact, with the help of fibered products) involving `G`, `Hom_S(H, G)` and
`Hom_S(H ×_S H, G)`, which we leave to the reader to make explicit. On the other hand, one will have

```text
H = Spec(B),
```

where `B` is a sheaf of algebras over `S` which is locally free as a sheaf of modules (this is the only hypothesis on
`H` that we shall need to retain). As the representability question envisaged is local on `S`, we may suppose `S` affine
with ring `A`. On the other hand, one will have `G = Spec(C)`, where `C` is an `A`-algebra. When `G = S[t] = G_0`, `t`
an indeterminate, the functor `Hom` is none other than

```text
T ↦ Γ(T, B_T),
```

which is representable (`B` being locally free) by the vector bundle `V(B^∨)`, where `B^∨` is the sheaf of modules dual
to `B`. When `G = S[(t_i)]`, with `(t_i)` a (not necessarily finite) family of indeterminates, one will have therefore
`G = G_0^I` (product over `S` of a family of copies of `G_0`), which is representable by the affine scheme

```text
Hom_S(H, G)^I = V(B^∨)^I = V(B^{∨(I)}).
```

In the general case, `G` will be isomorphic to a closed subscheme of a scheme of the form `S[(t_i)]`, i.e. `C` will be a
quotient of an `A`-algebra of the form `A[(t_i)]`. Let `(F_j)` be a system of generators of the ideal by which one
divides. Suppose `B` free of rank `n`, which is permissible by covering `S` by smaller affine opens. Choose a basis
`(e_k)_{1 ⩽ k ⩽ n}` of `B`; then writing the `n` components in this basis of `F_j((x_i))`, for `x_i = ∑ x_{ik} e_k`
(`x_{ik}` indeterminate coefficients, taken in an unspecified algebra `A′` over `A`), one finds, for each `F_j`, `n`
polynomials `F_{j,k}` in the `(x_{i,k})_{i ∈ I, 1 ⩽ k ⩽ n}`, with coefficients in `A`. One verifies at once that
`Hom_S(H, G)` is represented by the spectrum of the quotient of the polynomial ring `A[(x_{i,k})]` by the ideal
generated by the `F_{j,k}`. This proves at once b).

Let us prove a). For every ordinary finite commutative group `M`, let `F_M` be the subfunctor of `F` obtained by
restricting to subgroups of `G_T` which are of multiplicative type <!-- original page 156 --> and of type `M`. One sees
easily, by a gluing argument like the one which served in 3.5 (which we should have stated by unscrewing a bit more!),
that it suffices to verify that the `F_M` are representable; then `F` will be representable by the prescheme sum of the
`F_M`, where `M` runs over the set of classes of finite commutative groups up to isomorphism. (`F` is in fact the sum of
the `F_M` in the category of sheaves…).

From now on we suppose `M` fixed, and we shall write `F` instead of `F_M`. Let `H = D_S(M)`; consider the subfunctor
`F′ = Imm_{S-gr.}(H, G)` of `Hom_{S-gr.}(H, G)` whose value at `T` is the set of homomorphisms of `T`-groups `H_T → G_T`
which are closed immersions. We know already that `Hom_{S-gr.}(H, G)` is representable by an affine `S`-prescheme by
virtue of b), and using IX 6.8, one sees at once that `F′` is representable by an open and closed subprescheme of the
latter, hence it is also affine over `S`. Consider finally the canonical morphism `F′ → F`, which associates to each
monomorphism `H_T → G_T` the image group. One verifies at once, by virtue of the definitions, that in this way `F′`
becomes a principal homogeneous bundle (in the category of fpqc sheaves) over `F`, with group `Γ_F = Γ_S ×_S F`, where
`Γ = Aut_{gr.}(M)`, whence it follows "by descent" that this morphism is representable (i.e. for every morphism `T → F`,
with `T` representable, `T ×_F F′` over `T` is representable — in fact, representable by a principal galois bundle under
`Γ`). Hence by virtue of IV 4.6.6, `F` is representable if and only if the quotient `F′/F″`, where `F″ = F′ ×_F F′`,
exists in `(Sch)` and is universally effective for faithfully flat quasi-compact morphisms, or what amounts to the same,
if and only if the quotient `F′/Γ` exists and is universally effective for the said morphisms. Now as `F′` is affine
over `S`, one has seen in V 4.1 that the condition in question is indeed satisfied. This proves the representability of
`F` in a).

As for the complement, relative to the case where one supposes `G` of finite presentation over `S`, it follows at once
from the preceding proof, taking into account that by virtue of b), `F′` is then locally of finite presentation over
`S`, so that one may apply Exposé V[^N.D.E-XI-3]. <!-- original page 104 -->

## 4. The scheme of multiplicative-type subgroups of a smooth affine group

<!-- original page 157 -->

The principal result of the present Exposé is constituted by

**Theorem 4.1.** *Let `S` be a prescheme, `G` an `S`-prescheme in groups smooth and affine over `S`, `F` the functor
`(Sch)°/S → (Ens)` defined by*

```text
F(T) = set of multiplicative-type subgroups of G_T.
```

*Then the functor `F` is representable, and is smooth and separated over `S`.*

<!-- label: III.XI.4.1 -->

Let us signal at once the following variant:

**Corollary 4.2.** *Let `G`, `H` be two `S`-preschemes in groups, with `G` smooth and affine over `S`, `H` of
multiplicative type and of finite type. Then `Hom_{S-gr.}(H, G)` is representable, and is smooth and separated over
`S`.*

<!-- label: III.XI.4.2 -->

Indeed, when `H` is smooth over `S`, so is `H ×_S G`, and one may apply 4.1 to this latter. By the consideration of
graph subgroups, `Hom_{S-gr.}(H, G)` becomes a subfunctor `F′` of the functor `F` of "multiplicative-type subgroups of
`H ×_S G`", namely `F′(T)` = set of multiplicative-type subgroups `K` of `(H ×_S G)_T = H_T ×_T G_T` such that the
homomorphism induced by the first projection

```text
K ⟶ H_T
```

is an isomorphism. By virtue of IX 2.9, the canonical morphism `F′ → F` is an open immersion, hence `F` being
representable, so is `F′`, which will be representable by an open of `F`; and `F` being separated and smooth over `S`,
so will `F′` be. In the case where `H` is finite over `S`, it suffices to apply 3.12 b) for the representability of
`Hom_{S-gr.}(H, G)`. When `H` is a product `H_1 ×_S H_2`, with `H_1` smooth over `S` and `H_2` finite over `S`, then
`Hom_{T-gr.}(H_T, G_T)` is identified with the subset of `Hom_{T-gr.}((H_1)_T, G_T) × Hom_{T-gr.}((H_2)_T, G_T)` formed
of pairs `(u_1, u_2)` such that `u_1 · u_2 = u_2 · u_1`, whence it follows that `Hom_{S-gr.}(H, G)` is representable by
a closed <!-- original page 158 --> subprescheme of `Hom_{S-gr.}(H_1, G) ×_S Hom_{S-gr.}(H_2, G) = X`, as one sees by
applying VIII 6.5 b), where one takes `Y = H`, `Z = G`, `q_1` and `q_2` being defined respectively by
`(u_1, u_2) ↦ u_1 · u_2` and `(u_1, u_2) ↦ u_2 · u_1`.

In the general case, the question being local on `S` for the Zariski topology, one may suppose that `S` is affine, and
`H` of constant type over `S`. Then `H` being quasi-isotrivial (X 4.5), one can find an étale surjective morphism
`S′ → S`, `S′` affine, that splits `H`, i.e. such that `H′ = H_{S′}` is diagonalizable. Then the preceding result
applies, since a diagonalizable group is the product of a diagonalizable torus by a diagonalizable finite group. It
remains to see that the descent datum obtained on the `S′`-prescheme `Hom_{S′-gr.}(H′, G′) = X′` is effective. This is
seen by the reasoning of X 5.4, noting that in loc. cit., the hypothesis that `X′ → S′` was separated and locally
quasi-finite served only to ensure that every open part of `X′` quasi-compact over `S′` was quasi-affine over `S′`. Now
this property is still verified in the present case, as follows easily from the fact that this is so for the functor `F`
of 4.1 (which will be seen in the course of the proof of 4.1). This (or any other variant of this little unscrewing)
establishes the representability of `Hom_{S-gr.}(H, G)`, and at the same time the fact that it is separated over `S`. It
is locally of finite presentation over `S`, as one sees for example (as was pointed out in 3.2) thanks to the fact that
this functor "commutes with inductive limits of rings". Finally, this functor being formally smooth over `S` (by virtue
of 2.1), it is smooth over `S`.

**Remark 4.3.** We have here deduced 4.2 from 4.1, which is really immediate only when `H` is also smooth over `S`. For
the deduction to be made without contortions for the general case, the representability result 4.1 would have to be
established without supposing `G` smooth over `S`, but only affine of finite presentation over `S`. (Of course, <!--
original page 159 --> then `F` will no longer be smooth in general over `S`!) There is little doubt that 4.1 remains
true under these more general hypotheses, but the proof appears to have to be more delicate (failing the possibility of
invoking 3.8)[^XI-4-1][^N.D.E-XI-4]. Let us point out however that when `G` is a closed subgroup of an affine and smooth
group `G_0` over `S`, then the functor `F` representing the multiplicative-type subgroups of `G` is representable by a
closed subprescheme of the prescheme representing the analogous functor `F_0` for `G_0` (amenable to 4.1), as one sees
easily by applying VIII 6.4. This raises also the question: is an affine `S`-group scheme `G`, which is affine and of
finite presentation over `S`, isomorphic to a subgroup scheme of some `GL(n)_S`, `n` suitable? This is true when `S` is
the spectrum of a field, cf. VI_B 11.11, but unfortunately false in general, even for tori, cf. 4.6. Finally, note that
one could also prove 4.2 directly by exactly the same method as 4.1.

<!-- label: III.XI.4.3 -->

<!-- TRANSLATOR NOTE: In the source, the footnote (∗) is marked at this point of the text; the OCR has fused it with the
N.D.E. (4). They are rendered here as XI-4-1 and N.D.E-XI-4. -->

Let us now prove 4.1. Since the functor `F` is evidently of local nature, one may suppose `S` affine, so that
`S = Spec(A)`, `A` a ring. Considering `A` as the inductive limit of its subrings of finite type over `ℤ`, and noting
that `G` comes from a smooth and affine group over such a subring (EGA IV 8), one is reduced to the case where `S` is
noetherian. For every integer `n > 0`, let `T_n` be the functor defined as `F`, but restricting to subgroups `H` of
multiplicative type of `G_T` such that `n · id_H = 0`, i.e. such that `ₙH = H`. Order the set `I` of integers `> 0` by
the divisibility relation. When `m` is a multiple of `n`, define

```text
p_{n,m} : T_m ⟶ T_n
```

<!-- original page 160 --> by `p_{n,m}(H) = ₙH = Ker(n · id_H)`. In this way the `T_n` form a projective system of

functors over `S`. By virtue of 3.12 a), the functors `T_n` are representable, affine and of finite type over `S`.
Define likewise morphisms

```text
u_n : F ⟶ T_n,
```

by the relation `u_n(H) = ₙH`. In this way, one obtains a morphism

```text
u : F ⟶ T = lim_← T_n,
```

where the `lim_←` is taken in the category of functors over `S`. But let us point out at once that, the `T_n` being
representable and affine over `S`, so is `T` (it will be the spectrum of the inductive limit of the quasi-coherent
algebras on `S` which define the `T_n`). Of course, `T` is not in general of finite type over `S`.

We are going to apply 3.7 and are reduced to verifying conditions a) to d) of 3.7, which will imply that `F` is
representable by a prescheme locally of finite type over `S`. It then follows from 2.1 bis that `F` is even smooth over
`S`, and as `F` is a subfunctor of `T` which is affine over `S`, it follows that `F` is separated over `S` (being
separated over `T`, which is separated over `S`). Let us prove at once the complement invoked above, namely that every
open `U` of `F` quasi-compact over `S` is quasi-affine over `S`: this follows from 3.11 and from the fact that the `T_n`
are affine over `S`.

Let us verify therefore the conditions of 3.7.

a) `F` is a sheaf for the faithfully flat quasi-compact topology, by descent theory SGA 1, VIII, which applies here
since multiplicative-type groups over `T` are affine over `S`. It commutes with inductive limits of rings by the general
carpet [^XI-4-2] EGA IV 8. Let us show that it commutes with adic projective limits of local artinian rings. When
dealing with, instead of the functor `F`, the analogous functor envisaged in 4.2, this property is none other than that
of IX 7.1 in the special case where `A` is a complete noetherian local ring, equipped with an ideal of definition for
its usual topology (N.B. This is exactly where the hypothesis `G` affine intervenes in an essential way). In the present
case, we are reduced to proving the

**Lemma 4.4.** *Let `A` be a complete noetherian local ring, with maximal ideal `m`, `G` a group scheme affine over
`S = Spec(A)`. For every integer `n ⩾ 0`, let `S_n = Spec(A/m^{n+1})`, `G_n = G ×_S S_n`. Let for every `n`, `H_n` be a
subgroup of multiplicative type and of finite type of `G_n`, such that for `m ⩾ n`, `H_n` is deduced from `H_m` by
reduction. Under these conditions, there exists a unique multiplicative-type subgroup `H` in `G` which reduces along the
`H_n`.*

<!-- label: III.XI.4.4 -->

<!-- original page 161 -->

By virtue of X 3.2 there exists a group of multiplicative type `H` over `S`, necessarily of finite type and isotrivial,
determined up to unique isomorphism, equipped with an isomorphism `H ×_S S_0 ≃ H_0` (using the fact that `H_0` is
isotrivial, being of finite type over a field, cf. X 1.4). By virtue of X 2.1, for every `n`, the isomorphism
`H ×_S S_0 ≃ H_0` lifts to a unique isomorphism `H ×_S S_n ≃ H_n`. Having said this, by virtue of IX 7.1 already cited,
the homomorphisms `H_n → G_n` come from a unique homomorphism of `S`-groups `u : H → G`. By virtue of IX 6.6, this last
is a monomorphism since `u_0 : H_0 → G_0` is one. This completes the proof of 4.4.

b) The morphism `u : F → T` is a monomorphism. This follows from the density theorem IX 4.7, in the form of corollary
4.8 b). One will pay attention to the fact that it is essential, for the application we make of it here, to dispose of
this result over a not necessarily noetherian base. (N.B. As the functor `T` does not commute with inductive limits of
rings, it is not possible to reduce to that a priori.)

b′) The morphism `u : F → T` is infinitesimally étale; in other terms one has the

**Lemma 4.5.** *Let `A` be an artinian local ring of residue field `k`, `S = Spec(A)`, `I` an ideal `⊂ rad(A)`,
`S_0 = Spec(A/I)`, `G` an `S`-prescheme in groups smooth over `S`, `G_0 = G ×_S S_0`; let us give ourselves a
multiplicative-type subgroup `H_0` of `G_0` and for every integer `n > 0`, a multiplicative-type subgroup `H(n)` of `G`
such that*

*1°) for every multiple `m` of `n`, `H(n) = ₙH(m)`, and*

*2°) `H(n)_0 = ₙH_0`.*

*Under these conditions, there exists a multiplicative-type subgroup `H` of `G` and one only such that `ₙH = H(n)` for
every `n`.*

<!-- label: III.XI.4.5 -->

Uniqueness is already contained in b). For existence, an immediate recurrence reduces us to the case where `Jm = 0`, `m`
being the maximal ideal of `A`. Let `k = A/m`, `S_0 = Spec(k)`, `G_0 = G ×_S S_0`, `g_0` the Lie algebra of `G_0`, `h_0`
that of `H_0`. One has a canonical isomorphism of groups: <!-- original page 162 -->

```text
g_0 ⊗_k J ≃ Ker(G(S) ⟶ G(S_0)),
```

cf. Exp. III. By virtue of IX 3.6 bis and 3.7, there exists a multiplicative-type subgroup `H` of `G` reducing along
`H_0`, and such an `H` is determined modulo inner automorphism by an element of `N = Ker(G(S) → G(S_0))`. Thus the set
`P` of liftings `H` of `H_0` is a principal homogeneous set under the group `N/M`, where `M` is the group of `g ∈ N`
such that `int(g) · H = H`.

Now one sees easily (Exp. III) that this subgroup is none other than the vector subspace of `g_0 ⊗_k J` formed of the
invariants under `H_0`, when `H_0` operates on `g_0 ⊗_k J` by the representation induced by the adjoint representation
of `G_0`. Likewise, the set `P(n)` of liftings of `H(n)_0 = ₙH_0` is a principal homogeneous set under `N/M(n)`, where
`M(n)` is the vector subspace of `g_0 ⊗_k J = N` formed of the invariants under `ₙH_0`. Using the density theorem Exp.
IX 4.7, one sees easily that for `n` large (in the sense of the order relation put on the set of integers `n > 0`,
namely the divisibility relation) one has `M = M(n)`. Consequently, the natural map `H ↦ ₙH` from `P` to `P(n)`, which
is compatible with the operations of `N` and hence with the homomorphism `N/M → N/M(n)` on the groups of operators, is
bijective for `n` large. The conclusion of 4.5 results from this at once.

To verify c) and d) of 3.7, we use 3.8, which reduces us to verifying c′) and d′) below.

c′) The `T_n` are smooth over `S`, and the transition morphisms `p_{n,m} : T_m → T_n` are smooth.

This is none other than 2.2 bis.

d′) With the notation of 3.8, a point `ξ` of `F` with values in a field `k` over `S` is none other than a
multiplicative-type subgroup `H_0` of `G_0 = G_k`. Taking up again the reasoning of b′) above, one sees that the integer
`d(ξ)` envisaged in 3.8 is none other than the dimension of `g_0/g_0^{H_0}`, <!-- original page 163 --> where `g_0` is
the Lie algebra of `G_0` and `g_0^{H_0}` is the vector subspace of invariants under `H_0`. It is therefore a finite
integer, i.e. condition d′) 1°) of 3.8 is verified. With the notation of d′) 2°), the datum of a morphism `v : X → F`
amounts to the datum of a multiplicative-type subgroup `H` of `G_X`. For `x ∈ X`, the integer `d(ξ_x)` is then none
other than the dimension of `(g ⊗ κ(x))^{H_x}`, where `g` is the sheaf of Lie algebras of `G_X` (which is locally free
of finite type over `X` since `G_X` is smooth over `X`, and `g ⊗ κ(x)` is none other than the Lie algebra of the fiber
`G_x` of `G_X` at `x`), and `H_x` is the fiber of `H` at `x`. Now `g` being a locally free module on `S` on which the
group of multiplicative type `H` operates, one sees at once that the subfunctor `g^H` of invariants under `H` is given
by a locally direct factor subsheaf, hence locally free, of `g`. (By descent, one is reduced to the case where `H` is
diagonalizable, and where one applies Exp. I 4.7.3, noting that the subsheaf of invariants corresponds to the component
of degree zero.) Consequently `d(ξ_x) =` rank at `x` of `g^H`, hence it is a function locally constant in `x`. This
completes the proof of condition d′).

We have thus verified the conditions of 3.7, which completes the proof of 4.1.

**Remark 4.6.** When `G = GL(n)_S`, one can give a noticeably simpler and more explicit direct proof of 4.1, by using I
4.7.3. The proof shows moreover that in this case, the modular scheme is a scheme that is a sum of a family of affine
schemes over `S`. Proceeding as was said in 4.3, one deduces the same result whenever `G` is a closed subgroup of a
group of the form `GL(n)_S`. One should however beware of thinking that the preschemes which represent the functors in
4.1 or 4.2 are always sums of a family of affine schemes over `S`. Let for example `H` be a multiplicative-type group of
finite type over a locally noetherian prescheme `S`; then by virtue of X 5.11, `H` is isotrivial if and only if
`Hom_{S-gr.}(H, G_m)` is a sum of a family of affine preschemes over `S`. Now one has pointed out (X 1.6)
    <!-- original page 164 --> that there can exist tori `H` (of relative dimension `2`) which are not isotrivial; for such
a torus, `Hom_{S-gr.}(H, G_m)` is therefore not a sum of `S`-preschemes affine over `S`, and one sees likewise that the
twisted constant group "dual" `Hom_{S-gr.}(G_m, H)` is not such a sum either (for if two twisted constant commutative
groups of finite presentation `R`, `R′` are dual to each other, `R′ = Hom_{S-gr.}(R, ℤ_S)`, one sees easily that one is
isotrivial if and only if the other is). This last point shows also that such an `H` is not isomorphic to a subgroup of
a group of the form `GL(n)_S`; more precisely, one can show that a multiplicative-type group of finite type over `S`
locally noetherian connected is isomorphic to a subgroup of a group of the form `Aut_{Mod}(E)` (with `E` a locally free
module of finite type over `S`) if and only if it is isotrivial. Finally, taking `G = H × G_m` in the two preceding
examples, one finds an example where the prescheme representing the functor `F` of 4.1 is not a sum of a family of
`S`-preschemes affine over `S` (with `G` a torus of relative dimension `3` if one wishes).

<!-- label: III.XI.4.6 -->

## 5. First corollaries of the representability theorem

Let `H`, `G` be as in 4.2. Set

```text
M = Hom_{S-gr.}(H, G),
```

which is an `S`-prescheme smooth, separated over `S`, by virtue of 4.2. Note that `G` operates on the functor
`M = Hom_{S-gr.}(H, G)` by

```text
(g, u) ↦ int(g) ∘ u,
```

whence a canonical morphism

```text
(×)    G ×_S M ⟶ M ×_S M,
```

<!-- label: eq:III.XI.5-cross -->

whose components are the preceding morphism `G ×_S M → M`, and the second projection `G ×_S M → M`.

**Corollary 5.1.** *The preceding morphism `(×)` is smooth.*

<!-- original page 165 -->

<!-- label: III.XI.5.1 -->

This follows from 4.2 and 2.3. This statement is equivalent to the following:

**Corollary 5.2.** *Let `u_1, u_2 : H ⇉ G` be two homomorphisms of `S`-groups. Then the subfunctor `Transp(u_1, u_2)` of
`G` (cf. 2.4) is representable by a closed subprescheme of `G`, smooth over `S`.*

<!-- label: III.XI.5.2 -->

It remains only to prove that `Transp(u_1, u_2) → G` is indeed a closed immersion, which follows from the fact that it
is the kernel of a pair of morphisms `G ⇉ M` (namely `g ↦ int(g) u_1` and the "constant" morphism `g ↦ u_2`), and from
the fact that `M` is separated over `S`. In particular:

**Corollary 5.3.** *Let `u : H → G` be a morphism of `S`-groups. Then `Centr_G(u) = Transp(u, u)` is representable by a
closed subprescheme in groups of `G`, smooth over `S`. Moreover, `G/Centr_G(u)` is representable by an open subprescheme
of `M`.*

<!-- label: III.XI.5.3 -->

It remains to prove this last point. Now the morphism

```text
g ↦ int(g) ∘ u
```

from `G` to `M` is smooth of finite type by virtue of 5.2; it is therefore an open morphism (EGA IV 6.6), and if `U`
denotes its image, with the structure induced by `M`, the induced morphism `G → U` is smooth, surjective, of finite
type, hence covering for the faithfully flat and quasi-compact topology. Moreover, it is evident that the preceding
morphism `G → M` makes `G` into a formally principal homogeneous sheaf under `Centr_G(u)_M`, which implies that the
sheaf `G/Centr_G(u)` is indeed representable by `U`.

**Corollary 5.4.** *Let `u_1, u_2 : H ⇉ G` be two homomorphisms of `S`-groups. The following conditions are equivalent:*

<!-- label: III.XI.5.4 -->

*(i) `u_1` and `u_2` are conjugate locally for the étale topology.*

<!-- original page 166 -->

*(i bis) `u_1`, `u_2` are conjugate locally in the sense of the faithfully flat quasi-compact topology.*

*(ii) For every `s ∈ S`, denoting by `s̄` the spectrum of an algebraic closure of `κ(s)`, the morphisms
`u_{1, s̄}, u_{2, s̄} : H_{s̄} ⇉ G_{s̄}` are conjugate by an element of `G(κ(s̄))`.*

*(ii bis) The structural morphism `Transp(u_1, u_2) → S` is surjective.*

*(iii) `Transp(u_1, u_2)` is a torsor under the action of the `S`-prescheme in groups smooth of finite type
`Centr_G(u_1)`.*

(i) ⇒ (i bis) and (ii) ⇒ (ii bis) are trivial (the second thanks to the Nullstellensatz); on the other hand (i bis) ⇒
(ii) by the "principle of finite extension" (EGA IV 9). On the other hand (ii bis) ⇒ (iii) thanks to the fact that
`Transp(u_1, u_2)` is smooth over `S` hence flat over `S`, and of finite type hence quasi-compact over `S`; it is
therefore faithfully flat quasi-compact over `S` if and only if its structural morphism is surjective. As, on the other
hand, it is formally principal homogeneous under `Centr_G(u_1)`, which is faithfully flat and quasi-compact over `S`,
one sees that this last condition is equivalent also to saying that `Transp(u_1, u_2)` is a torsor under `Centr_G(u_1)`
(understood: in the sense of the faithfully flat and quasi-compact topology). Finally (iii) ⇒ (i) thanks to the fact
that `Transp(u_1, u_2)` is smooth over `S` and to "Hensel's lemma" in the form 1.10.

**Remark 5.5.** For `u_1 = u : H → G` fixed, the functor `(Sch)°/S → (Ens)` which associates to every `T` over `S` the
set of homomorphisms of `T`-groups `u_2 : H_T → G_T` which are conjugate to `u_T : H_T → G_T` locally for the étale
topology, is precisely representable by the open of `M`, isomorphic to `G/Centr_G(u)`, envisaged in 5.3.

<!-- label: III.XI.5.5 -->

Let us sketch the variants of the preceding results, obtained by application of 4.1 instead of 4.2. Let therefore `G` be
a prescheme in groups smooth and affine over `S`, and let us now denote by `M` the `S`-prescheme smooth, separated over
`S`, <!-- original page 167 --> which represents the functor envisaged in 4.1. One has again operations of `G` on `M`:

```text
(g, H) ⟼ int(g)(H),
```

whence as above a morphism

```text
(× bis)    G ×_S M ⟶ M ×_S M.
```

<!-- label: eq:III.XI.5-cross-bis -->

**Corollary 5.1 bis.** *The preceding morphism is smooth.*

<!-- label: III.XI.5.1bis -->

This follows from 4.1 and 2.3 bis. One concludes again:

**Corollary 5.2 bis.** *Let `H_1, H_2` be two multiplicative-type subgroups of `G`. Then the subfunctor
`Transp_G(H_1, H_2)` of `G` is representable by a closed subprescheme of `G`, smooth over `S`.*

<!-- label: III.XI.5.2bis -->

In particular:

**Corollary 5.3 bis.** *Let `H` be a multiplicative-type subgroup of `G`. Then the subfunctor in groups `Norm_G(H)` of
`G` is representable by a closed subprescheme of `G`, smooth over `S`. Moreover, the quotient `G/Norm_G(H)` is
representable by an open subprescheme of `M`.*

<!-- label: III.XI.5.3bis -->

**Corollary 5.4 bis.** *Let `H_1, H_2` be two multiplicative-type subgroups of `G`. The following conditions are
equivalent:*

<!-- label: III.XI.5.4bis -->

*(i) `H_1` and `H_2` are conjugate locally for the étale topology.*

*(i bis) `H_1` and `H_2` are conjugate locally for the faithfully flat quasi-compact topology.*

*(ii) For every `s ∈ S`, denoting by `s̄` the spectrum of an algebraic closure of `κ(s)`, the subgroups
`H_{1, s̄}, H_{2, s̄}` of `G_{s̄}` are conjugate by an element of `G(κ(s̄))`.*

*(ii bis) The structural morphism `Transp(H_1, H_2) → S` is surjective.* <!-- original page 168 -->

*(iii) `Transp(H_1, H_2)` is a principal homogeneous bundle under the action of the `S`-prescheme in groups smooth of
finite type `Norm_G(H_1)`.*

**Remark 5.5 bis.** Remark 5.5 transposes likewise to the present case.

<!-- label: III.XI.5.5bis -->

**Remark 5.6.** Note that to establish the result 5.2, and consequently also the first assertion in 5.3, as well as 5.4,
the reference to 4.2 can be replaced by a reference to VIII, 6.4, whose proof is much easier. This shows also that the
hypothesis `G` affine over `S` is unnecessary there. Moreover, in N° 6, we shall show how a variant of this method
permits extending these results to the case of certain groups `H` more general than groups of multiplicative type. These
same observations extend to the variants 5.2 bis etc. On the other hand, the result 5.8 that follows uses in an
essential way all the hypotheses made (notably `G` affine and smooth over `S`, `H` of multiplicative type), and the
lecturer knows of no other proof of it than via the representability theorems 4.1 or 4.2[^XI-5-1].

<!-- label: III.XI.5.6 -->

**5.7.** Since the morphism `(×)` resp. `(× bis)` is smooth hence open, its image is open. Let `R` be this image,
equipped with the structure induced by `M ×_S M`; one easily verifies that `R` is an equivalence relation in `M`, which
is none other moreover than the one made explicit in 5.4 resp. 5.4 bis. It would be interesting to know whether the
quotient sheaf `M/R` (which is formally étale over `S`) is representable (it is then representable by a prescheme étale
over `S`); it is so for example when `S` is the spectrum of a field. One will note moreover that `R` may not be closed
in `M ×_S M` (even when `G` is quasi-finite over `S`…), which means (when `M/R` is representable) that `M/R` is then not
separated over `S`.

<!-- label: III.XI.5.7 -->

**Theorem 5.8.** *Let `S` be a prescheme, `G` an `S`-prescheme smooth and affine over `S`, `s ∈ S`. Then:* <!--
original page 169 -->

<!-- label: III.XI.5.8 -->

*a) For every multiplicative-type subgroup `H^0` of `G_s`, there exists an étale morphism `S′ → S`, a point `s′` of `S′`
above `s` such that the residue extension `κ(s′)/κ(s)` be trivial, and a multiplicative-type subgroup `H′` of
`G′ = G ×_S S′`, such that `H′_{s′} = H^0 ⊗_{κ(s)} κ(s′)`.*

*b) For every group homomorphism `u^0 : H_s → G_s`, where `H` is an `S`-prescheme in groups of multiplicative type and
of finite type, there exists an étale morphism `S′ → S`, a point `s′` of `S′` above `s` such that the residue extension
`κ(s′)/κ(s)` be trivial, and a group homomorphism `u′ : H′ → G′`, such that `u′_{s′} : H′_{s′} → G′_{s′}` be equal to
`u^0 ⊗_{κ(s)} κ(s′)`.*

This results from 4.1 resp. 4.2, and from Hensel's lemma in the form 1.10.

**Proposition 5.9.** *Let `S` be a prescheme, `G` an `S`-prescheme smooth and affine over `S`, `H` a multiplicative-type
subgroup of `G`. Consider `Centr_G(H) ↪ Norm_G(H)`, which by 5.3 and 5.3 bis are closed subpreschemes in groups of `G`,
smooth over `S`. Then the first group is an open and closed subprescheme of the second, and the quotient sheaf*

```text
W_G(H) = Norm_G(H)/Centr_G(H)
```

*is representable by an open subprescheme in groups of `Aut_{S-gr.}(H)`; it is therefore an `S`-prescheme in groups
quasi-finite, étale and separated over `S`.*

<!-- label: III.XI.5.9 -->

Consider indeed the evident homomorphism

```text
θ : Norm_G(H) ⟶ Aut_{S-gr.}(H),
```

whose kernel is by definition `Centr_G(H)`. As `Aut_{S-gr.}(H)` is representable by an `S`-prescheme in groups étale and
separated over `S` (X 5.10), its unit section is an open and closed immersion, <!-- original page 170 --> hence its
inverse image under `θ` is an open and closed subgroup of `Norm_G(H)`. I say moreover that `θ` is a smooth morphism:
this indeed results formally from the definitions, and from the fact that `Norm_G(H)` is smooth over `S` and
`Aut_{S-gr.}(H)` is étale over `S`. One concludes as in 5.3 that the image of `θ` is an open `U` of `Aut_{S-gr.}(H)` and
that, equipped with the induced structure, `U` represents the quotient sheaf `Norm_G(H)/Centr_G(H)`. This latter is
therefore étale and separated over `S` since `Aut_{S-gr.}(H)` is, and it is quasi-finite over `S`, being quasi-compact
over `S` as image of `Norm_G(H)` which is. This completes the proof of 5.9.

**Corollary 5.10.** *For every `s ∈ S`, let*

```text
w(s) = rank Norm_{G_s}(H_s)/Centr_{G_s}(H_s)
```

*(which is also the index of `Centr_{G(k̄)}(H(k̄))` in `Norm_{G(k̄)}(H(k̄))`, where `k̄` is an algebraic closure of
`κ(s)`). Then the function `s ↦ w(s)` is lower semicontinuous. For it to be constant in a neighborhood of the point `s`,
it is necessary and sufficient that `W_G(H)` be finite over `S` in a neighborhood of `s`.*

<!-- label: III.XI.5.10 -->

Indeed, for every `S`-prescheme `W` which is étale, of finite type and separated over `S`, it is true that the function
`s ↦ w(s) = rank [W_s : κ(s)]` is lower semicontinuous, and that it is constant in a neighborhood of the point `s` if
and only if `W` is finite over `S` in a neighborhood of `s` (a fact pointed out in SGA 1, I 10.9, and whose proof, which
offers no difficulty, will be found in EGA IV[^XI-5-2]).

**Remark 5.11.**[^N.D.E-XI-5] Let `G` be a prescheme in groups affine and smooth over `S`, `H` a multiplicative-type
subgroup; then 5.3 and 5.3 bis imply that the quotients

```text
G/Centr_G(H) and G/Norm_G(H)
```

are preschemes smooth over `S` and quasi-affine over `S`, since in both cases, the modular prescheme `M` in which the
quotient is embedded is such that every open `U` of `M` quasi-compact over `S` is quasi-affine over `S` (3.11). We shall
see moreover in the following Exposé [^N.D.E-XI-6] that for every `U` as above, the schematic closure `Ū` <!--
original page 171 --> of `U` in `M` is even affine over `S`, which shows that the quotients envisaged are affine over
`S` provided the open `U` in the corresponding modular scheme (of homomorphisms of group from `H` to `G`, resp. of
multiplicative-type subgroups of `G`) is closed in `M`. This is for example the case if `H` is a "maximal torus" in the
second case envisaged, or when `S` is the spectrum of a field, cf. XII.5.4[^N.D.E-XI-7]. I do not know whether the
quotients envisaged are affine over `S` in general.

<!-- label: III.XI.5.11 -->

## 6. On a rigidity property for homomorphisms of certain group schemes, and the representability of certain transporters[^XI-6-0]

**Proposition 6.1.** *Let `S` be a locally noetherian prescheme, `H` a commutative `S`-prescheme in groups, of finite
type over `S`, `E` a set of integers `> 0`, stable under multiplication, and suppose the following conditions
satisfied:*

<!-- label: III.XI.6.1 -->

*a) For every `n ∈ E`, the subgroup `ₙH = Ker(n · id_H)` is finite and flat over `S`.*

*b) For every `s ∈ S`, the family of the `ₙH_s` (`n ∈ E`) is schematically dense in `H`.*

*Let `Y` be a closed subprescheme of `H`. Then the subfunctor `∏_{H/S} Y/H` of `S` (compare VIII, 6) is representable by
a closed subprescheme `T` of `S`, and if `S` is noetherian, there exists an `n ∈ E` such that*

```text
(×)    ∏_{H/S} Y/H = ∏_{ₙH/S} Y ∩ ₙH/S.
```

<!-- label: eq:III.XI.6.1-cross -->

Indeed, by virtue of VIII 6.4, as by condition a) `ₙH` is finite and flat and a fortiori "essentially free" over `S`, it
follows that the second member of `(×)` is representable <!-- original page 172 --> by a closed subprescheme `T_n` of
`T`. Of course, for `n ∈ E`, with `E` ordered by divisibility, the `T_n` form a decreasing family of closed
subpreschemes of `S`, hence if `S` is noetherian (which we may suppose) it is stationary for `n` large. Let `T` be the
value of `T_n` for `n` large; I say that `T` indeed represents the first member of `(×)`, which will complete the proof.
One is reduced to proving that if `S′` is a prescheme over `S` such that `(Y ∩ ₙH)_{S′} = (ₙH)_{S′}` for every `n ∈ E`,
i.e. such that `Y_{S′} ⊃ ₙH_{S′}` for every `n ∈ E`, then `Y_{S′} = H_{S′}`. Now this is indeed the case, for by virtue
of IX 4.4 the family of the `ₙH_{S′}` is schematically dense in `H_{S′}`, taking conditions a) and b) into account.

**Theorem 6.2.** *Let `S` be a prescheme, `H, E` as in 6.1 satisfying conditions a), b), `u : H → G` a homomorphism of
`S`-groups from `H` to an `S`-prescheme in groups locally of finite type over `S`, finally `K` a closed subprescheme in
groups of `H`. Consider the subfunctor `Transp_G(u, K)` of `G` (cf. 2.5). Then this last is representable by a closed
subprescheme of `G`, and if `G` is noetherian (for example `S` noetherian and `G` of finite type over `S`), there exists
an integer `n ∈ E` such that `Transp_G(u, K) = Transp_G(u|_{ₙH}, K)`. If finally `G` is smooth over `S`, and `K` smooth
over `S` or of multiplicative type, and if `H, E` satisfy the following condition stronger than a):*

<!-- label: III.XI.6.2 -->

*a′) For every `n ∈ E`, the subgroup `ₙH` of `H` is of multiplicative type,*

*then `Transp_G(u, K)` is smooth over `S`.*

Consider indeed the `G`-group `H_G = H ×_S G`, which evidently satisfies the conditions of 6.1 (with `S` replaced by
`G`, and `H` by `H_G`), and the closed subprescheme `Y` of `H_G`, inverse image of `K ⊂ G` under

```text
H_G = H ×_S G ⟶ G
```

<!-- original page 173 --> defined by `(h, g) ↦ int(g) · u(h)`. Then `Transp_G(u, K)` is none other than

`∏_{H_G/G} Y/H_G` (compare VIII, examples 6.5 e)). Hence the first assertions result from 6.1, and moreover, one sees
that for every quasi-compact open `U` of `G`, there exists `n ∈ E` such that `Transp_G(u, K)` and `Transp_G(u|_{ₙH}, K)`
have the same trace on `U`. To verify the last assertion of 6.2, one can therefore replace `H` by an `ₙH`, and then it
suffices to apply 2.5, which applies since `ₙH` is supposed of multiplicative type over `S`.

**Remark 6.3.** The preceding proof uses only the very elementary result VIII 6.4, and moreover (for the last part) 2.5,
that is, when `K` is smooth over `S`, the infinitesimal result IX 3.6, hence the vanishing of the cohomology of
multiplicative-type groups. One will note that in the most important cases (cf. 6.7) one can suppose even the `n ∈ E`
prime to the residual characteristics of `S`, i.e. invertible in `O_S`, hence the `ₙH` finite étale over `S`, and then
the cohomological result invoked is practically trivial, so that 6.2 is then independent of the theory of
multiplicative-type groups.

<!-- label: III.XI.6.3 -->

**6.4.** One sees as usual that 6.1 extends to the case where one has an `S`-prescheme `S′` over `S` (not necessarily
locally noetherian), and a closed subprescheme `Y′` of `H′ = H_{S′}`, provided that `Y′ → H′` is of finite presentation
i.e. the ideal defining `Y′` is of finite type: then `∏_{H′/S′} Y′/H′` is representable by a closed subprescheme `T′` of
`S′`, such that `T′ → S′` is of finite presentation, and if `S′` is quasi-compact, there exists `n ∈ E` such that the
relation analogous to `(×)` is valid. It follows also that the first statement in 6.2 is valid without supposing `G`
locally of finite type over `S`, provided that the immersion `K → G` is of finite presentation.

<!-- label: III.XI.6.4 -->

**6.5.** As announced in 5.6, theorem 6.2 permits extending to the preschemes in groups satisfying a′) and b) above,
certain results established by another method and under more restrictive conditions for groups of multiplicative type.
This is the case for results 5.2, for the beginning of 5.3, for 5.4, and for the bis variants of the preceding results
5.9 and 5.10. <!-- original page 174 --> This is also the case for the results of IX, N°s 5 and 6, with the exclusion of
IX 6.8 (already false for a homomorphism of abelian schemes `u : H → G`, over the spectrum `S` of a discrete valuation
ring with residue characteristic `p > 0`: it can happen that `Ker u` have as generic fiber the unit group, and as
special fiber a radicial group not reduced to the unit group).

<!-- label: III.XI.6.5 -->

**6.6.** We have just given an example of a rigidity property for groups of multiplicative type which is not shared by
abelian schemes. Another example, extremely important, is in the fact that the existence theorem of infinitesimal
extensions of homomorphisms IX 3.6 is no longer valid when `H` is an abelian scheme. Thus, an abelian scheme `≠ 0` over
a field admits non-trivial infinitesimal variations, contrary to what occurs for a group of multiplicative type — which
is the infinitesimal aspect of the fact that there exists a "theory of moduli" (moreover far from being completed) for
abelian varieties, while the theory of moduli for groups of multiplicative type is empty. Another "global" aspect of
this infinitesimal difference is that if `H` is an abelian scheme over `S` locally noetherian, and `G` is an
`S`-prescheme in groups commutative locally of finite type over `S`, then one can show that `Hom_{S-gr.}(H, G)` is
representable by a prescheme locally of finite type over `S`, but contrary to what happens for `H` of multiplicative
type, this prescheme is not étale over `S`, but only unramified over `S`. Thus, if `S` is for example the spectrum of a
complete discrete valuation ring, `H` and `G` abelian schemes over `S`, there can exist homomorphisms `H_0 → G_0` on the
special fibers which do not come "by specialization" from a homomorphism on the generic fibers.

<!-- label: III.XI.6.6 -->

**6.7.** Theorem 6.2 applies whenever `H` is an abelian scheme over `S`, or more generally an extension of such a scheme
by a torus. Indeed, the question being local on `S`, one may suppose that there exists a prime number `ℓ` prime to the
residue characteristics of `S`, <!-- original page 175 --> and one sees that it then suffices to take for `E` the set of
powers of `ℓ` to satisfy conditions a′) and b).

<!-- label: III.XI.6.7 -->

A reasoning analogous to that of 6.1 gives us the

**Theorem 6.8.** *Let `X` be a prescheme smooth over `S`, with geometric fibers connected non-empty. Then for every
closed subprescheme `Y` of `X`, the functor `∏_{X/S} Y/X` is representable by a closed subprescheme `T` of `S`. If `Y`
is of finite presentation over `X`, then `T` is of finite presentation over `S`.*

<!-- label: III.XI.6.8 -->

As `f : X → S` is faithfully flat locally of finite presentation, it is covering for the fpqc topology. As on the other
hand `T = ∏_{X/S} Y/X` is evidently a subsheaf of `S` (for the fpqc topology), it follows that the question of
representability of `T` by a closed subprescheme of `S` is of local nature on `S` for the fpqc topology, and the same
holds for the question of deciding whether `T` is of finite presentation over `S`. Doing then the base change `S′ → S`,
with `S′ = X`, one is reduced to the case where `X` admits a section `e` over `S`. One may moreover suppose `S` affine
and a fortiori quasi-compact. One then has:

**Corollary 6.9.** *Under the conditions of 6.8, suppose that `S` be quasi-compact and that `X` admit a section `e` over
`S`. Let, for every integer `n ⩾ 0`, `X_n` be the subprescheme of `X`, infinitesimal neighborhood of order `n` of the
section `e`. Suppose `Y` of finite presentation over `X`. Then there exists an integer `n ⩾ 0` such that one has
`∏_{X/S} Y/X = ∏_{X_n/S} Y_n/X_n` (where `Y_n = Y ∩ X_n`).*

<!-- label: III.XI.6.9 -->

This corollary indeed implies 6.8 when `Y` is of finite presentation over `X`, thanks to VIII 6.4: for, `X` being smooth
over `S`, `X_n` is finite and locally free over `S` and a fortiori is "essentially free" over `S` in the sense of VIII
6.1, hence `∏_{X_n/S} Y_n/X_n` is representable by a closed subprescheme of `S`. Moreover, the proof of loc. cit., or
the reduction to the noetherian case, <!-- original page 176 --> immediately shows us that the said closed subprescheme
of `S` is of finite presentation over `S`.

Let us prove first 6.9, hence 6.8, when `S` is noetherian. Let `T_n = ∏_{X_n/S} Y_n/X_n`. Then the `T_n` form a
decreasing sequence of closed subpreschemes of `S`, and `S` being noetherian, this sequence is stationary. Let
`R = ⋂_{n ⩾ 0} ∏_{X_n/S} Y_n/X_n` their common value for `n` large; one has evidently `T ⊂ R`, and it suffices to
establish that one has `R ⊂ T`. Doing the base change `R → S`, one is reduced to the case where `R = S`, i.e.
`Y_n = X_n` for every `n` i.e. `Y ⊃ X_n` for every `n`, and to prove then `T = S` i.e. `Y = X`. Now `Y ⊃ X_n` for every
`n` implies (thanks to the fact that `X` is locally noetherian) that `Y` is, in a neighborhood of each point of `e(S)`,
an induced open subprescheme of `X`, hence there exists an induced open `U` of `X`, containing `e(S)`, such that
`U ⊂ Y`. By virtue of IX 4.3, the fibers of `X/S` being integral, `U` is schematically dense in `X`, hence (`Y` being a
closed subprescheme majorizing `U`) one has `Y = X`. This proves 6.9, hence 6.8, in this case.

The general case proceeds by reduction to the preceding case. For every `s ∈ S`, there exists an affine open
neighborhood `U` of `s` and an affine open neighborhood `V` of `e(s)` such that `f(V) ⊂ U`. Then `f(V)` is an open
neighborhood of `s` contained in `U`, and if `S_0` is an affine open neighborhood of `s` contained in `e⁻¹(V) ∩ f(V)`,
and `X_0 = V ∩ f⁻¹(S_0)`, then `X_0` and `S_0` are affine opens of `X` resp. `S`, and `X_0/S_0` admits a section.
Because of the local nature of 6.8 and 6.9, one may suppose `S = S_0`. I say that one then has
`∏_{X/S} Y/X = ∏_{X_0/S_0} Y_0/X_0`, where `Y_0 = Y ∩ X_0`; indeed, by virtue of IX 4.6, `X_0` is schematically dense in
`X` (at least when `X` is quasi-separated over `S` so that `X_0` is retrocompact in `X`; but in fact one can show
without difficulty that IX 4.6 remains valid without the retrocompactness hypothesis), and likewise for every base
change `S_1 → S`, `X_0 ×_S S_1` is schematically dense in `X ×_S S_1`, whence at once the announced equality. This
reduces us to the case where `X = X_0`, so one may suppose `S` and `X` affine. <!-- original page 177 --> Moreover, if
`X = Spec(B)` and if `J` is the ideal of `B` which defines `Y`, `J` is the inductive limit of its sub-ideals of finite
type, hence `Y` is the intersection of closed subpreschemes `Y_i` of `X` which are of finite presentation over `S`, and
consequently `∏_{X/S} Y/X = ⋂_i ∏_{X/S} Y_i/X`, which reduces us, to prove 6.8, to the case where `Y` is of finite
presentation over `X`. It then suffices to prove 6.9 with `S` and `X` affine. But then `X` and `Y` over `S` come by base
change `S → S_0` from an analogous situation `X_0` and `Y_0` over `S_0`, with `S_0` noetherian, which reduces us to the
case where `S` is noetherian, which has already been treated. This completes the proof of 6.8 and 6.9.

**Corollary 6.10.** *Let `X` be an `S`-prescheme in groups smooth of finite presentation, with connected fibers, `Y` a
prescheme in groups of finite presentation over `S`, `i : Y → X` a monomorphism of `S`-preschemes in groups, making `Y`
therefore a subgroup of `X`. Then `∏_{X/S} Y/X` is representable by a closed subprescheme of finite presentation of `S`.
If `S` is quasi-compact, denoting for every integer `n ⩾ 0` by `X_n` the infinitesimal neighborhood of order `n` of the
unit section of `X`, and setting `Y_n = X_n ∩ Y`, one has for `n` large enough: `∏_{X/S} Y/X = ∏_{X_n/S} Y_n/X_n`.*

<!-- label: III.XI.6.10 -->

The proof is essentially that of 6.9. Note that the unit sections of `X` and of `Y` induce bijective immersions
`S → X_n` and `S → Y_n`, hence induce isomorphisms of `S_red` with `(X_n)_red` and `(Y_n)_red`, which implies that the
injection `Y_n → X_n` is proper, hence, being a monomorphism of finite presentation, is a closed immersion.
Consequently, by virtue of VIII 6.4 already used, `∏_{X_n/S} Y_n/X_n` is representable by a closed subprescheme of `S`
of finite presentation over `S`, and it remains therefore to prove the last assertion of 6.10 in the case where one
supposes moreover `S` affine. One reduces immediately again to the case where `S` is noetherian, and one is reduced to
proving that one then has `R = T` (with the notation of the proof of 6.9), or again that `Y ⊃ X_n` for every `n` implies
`Y = X`. Now the hypothesis implies that `i : Y → X` is étale at the points of the unit section of `Y` over `S`, hence
`Y` is smooth over `S` at the points of the unit section, whence it follows that the open `Y_0` of points of `Y` at
which `Y` is smooth <!-- original page 178 --> over `S` is an induced open subgroup of `Y`. Then `Y_0 → X` is a
monomorphism étale by virtue of X 3.5, hence an open immersion; now the fibers of `X` being connected and every open
subgroup of an algebraic group being also closed, it follows that this is a surjective open immersion i.e. an
isomorphism. Hence `Y_0 = X` and a fortiori `Y = X`, which completes the proof of 6.10.

Proceeding as in VIII 6.5, one concludes from 6.10:

**Corollary 6.11.** *Let `G` be an `S`-prescheme in groups locally of finite type and quasi-separated over `S`, `H` a
prescheme in groups smooth of finite presentation over `S` with connected fibers, `i : H → G` a monomorphism of
`S`-groups, making `H` therefore a subgroup of `G`. Then:*

<!-- label: III.XI.6.11 -->

*a) `Centr_G(H)` and `Norm_G(H)` are representable by closed subpreschemes of `G` of finite presentation over `G`, and
likewise, for every monomorphism `j : K → G` of finite presentation of `S`-preschemes in groups, `Transp_G(H, K)` is
representable by a closed subprescheme of `G` of finite presentation over `G`.*

*b) If `G` is quasi-compact, in the various cases envisaged in a), there exists an integer `n ⩾ 0` such that (if `H_n`
denotes the infinitesimal neighborhood of order `n` of the unit section of `H`) one has*

```text
Centr_G(H) = Centr_G(H_n)
Norm_G(H) = Norm_G(H_n)
Transp_G(H, K) = Transp_G(H_n, K) = Transp_G(H_n, K_n).
```

One applies 6.10 to the prescheme in groups `X = H_G = H ×_S G` above the base prescheme `G`, and to the subprescheme in
groups `Y` inverse image of the diagonal subgroup of `(G ×_S G)_G` over `G` by a suitable homomorphism of `G`-groups of
`X` into `(G ×_S G)_G` (in the case of `Centr`), resp. the inverse image of `K_G` by a suitable homomorphism of
`G`-groups of `X` into `G_G` (in the case of `Transp`). The case of `Norm` reduces to the transporter by taking `K = H`,
the hypothesis on `G` ensuring that `H → G` is of finite presentation (hence `Y → X` is of finite presentation);
    <!-- original page 179 --> in the case of `Centr`, the hypothesis made on `G` ensures that the diagonal group of
`G ×_S G` is of finite presentation over `G ×_S G`, whence again the fact that `Y` is of finite presentation over `X`.

**Remark 6.12.** One can prove (using rather delicate results of EGA VI[^XI-6-1]) that if `X` is a prescheme flat of
finite presentation over `S`, which is proper over `S` or with non-empty connected geometric fibers, then for every
closed subprescheme `Y` of `X` of finite presentation over `S`, `∏_{X/S} Y/X` is representable by a closed subprescheme
of `S` of finite presentation over `S`. Likewise, if `X` is an `S`-prescheme in groups flat of finite presentation with
connected fibers, and `i : Y → X` a monomorphism of `S`-groups, with `Y` an `S`-prescheme in groups of finite
presentation, then `∏_{X/S} Y/X` is representable by a closed subprescheme of `S` of finite presentation over `S`. In
particular, 6.11 a) remains valid by replacing the hypothesis "`H` smooth over `S`" by "`H` flat over `S`".

<!-- label: III.XI.6.12 -->

<!-- LEDGER DELTA — Exposé XI — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| critère de représentabilité | representability criterion | Per Exposé XI title. |
| formellement lisse / non ramifié / étale | formally smooth / unramified / étale | Standard. |
| infinitésimalement lisse / non ramifié / étale | infinitesimally smooth / unramified / étale | Standard. |
| morphisme net | net morphism | EGA-era replacement for "non ramifié"; rendered "unramified" (current standard) with the source's note that "net" is preferred. |
| de présentation finie | of finite presentation | Per glossary. |
| extension résiduelle | residue field (corrected) | The 2011 re-edition has corrected this from "extension résiduelle"; cf. N.D.E-XI-1. |
| nombres duaux | dual numbers | `D(k) = k[t]/(t²)`. |
| anneau hensélien | henselian ring | Standard. |
| lemme de Hensel | Hensel's lemma | Standard. |
| voisinage infinitésimal d'ordre n | infinitesimal neighborhood of order n | Per Exp. III. |
| de nature locale | of local nature | Sheaf for the Zariski topology. |
| commute aux limites inductives d'anneaux | commutes with inductive limits of rings | The "locally of finite presentation" condition for representable functors. |
| commute aux limites projectives adiques d'anneaux locaux artiniens | commutes with adic projective limits of local artinian rings | The left-exactness condition. |
| ensemblistement surjectif | set-theoretically surjective | Per 3.6. |
| ensemble sous-jacent (ens(F)) | underlying set (set(F)) | Per 3.6. |
| ensemble principal homogène | principal homogeneous set | Standard. |
| fibré principal homogène | principal homogeneous bundle | Standard. |
| (faisceau) formellement principal homogène | formally principal homogeneous (sheaf) | Standard. |
| isomorphisme local | local isomorphism | Standard. |
| isotrivial | isotrivial | Per IX. |
| quasi-isotrivial | quasi-isotrivial | Per IX. |
| sous-groupe de type multiplicatif | multiplicative-type subgroup | Per Exposé XI title. |
| transporteur | transporter | Per glossary. |
| centralisateur | centralizer | American spelling. |
| normalisateur | normalizer | American spelling. |
| schéma modulaire | modular scheme | Standard. |
| préschéma modulaire | modular prescheme | Standard. |
| tapis général | general machinery / "carpet" | Idiom for a body of underlying foundational results in EGA. |
| théorème de densité | density theorem | Per IX 4.7. |
| schématiquement dense | schematically dense | Per IX 4.4. |
| adhérence schématique | schematic closure | `Ū`. |
| sous-préschéma fermé | closed subprescheme | Standard. |
| dimension relative | relative dimension | Standard. |
| algèbre de Lie | Lie algebra | Per glossary. |
| représentation adjointe | adjoint representation | Standard. |
| invariants sous H | invariants under H | Standard. |
| automorphisme intérieur | inner automorphism | `int(g)`. |
| section unité | unit section | Standard. |
| graphe (groupe graphe) | graph (graph subgroup) | Standard. |
| somme amalgamée | amalgamated sum | Standard (= pushout). |
| « par descente » | "by descent" | Keep quotes (translation of guillemets). |
| « lemme de Hensel » | "Hensel's lemma" | Keep quotes for historical name. |
| Schémas de Hilbert | Hilbert schemes | Standard. |
| sans contorsions | without contortions | Standard idiom. |
| ouvert quasi-compact | quasi-compact open | Standard. |
| quasi-affine sur S | quasi-affine over S | Standard. |
| semi-continue inférieurement | lower semicontinuous | Standard. |
| Nullstellensatz | Nullstellensatz | Keep German. |
| conjugué localement | conjugate locally | Standard. |
| extension étale de la base | étale extension of the base | Standard. |
| rétrocompact | retrocompact | Standard. |
| majorer (un sous-préschéma) | majorize (a subprescheme) | Lattice term. |
| « principe de l'extension finie » | "principle of finite extension" | EGA IV 9. |
| rigidité (de morphismes) | rigidity (of morphisms) | Per N° 6 title. |
| théorie des modules | theory of moduli | Standard. |
| variation infinitésimale | infinitesimal variation | Standard. |
| par spécialisation | by specialization | Standard. |
| caractéristique résiduelle | residue characteristic | Standard. |
| anneau de valuation discrète | discrete valuation ring | Standard. |
| fibre générique / spéciale | generic / special fiber | Standard. |
| sous-tore | subtorus | Standard. |
| sous-tore central | central subtorus | Standard. |
| « essentiellement libre » (au sens de VIII 6.1) | "essentially free" (in the sense of VIII 6.1) | Keep quotes — historical SGA 3 coinage. |
| sous-groupe radiciel | radicial subgroup | Per IX. |
| groupe radiciel | radicial group | Per IX. |
| extension triviale (d'un corps) | trivial extension (of a field) | Standard (= the field itself). |
| extension finie séparable | finite separable extension | Standard. |
| groupe d'opérateurs | group of operators | Standard. |
| foncteur à groupe d'opérateurs | functor with group of operators | Standard. |
| morphisme étale surjectif | étale surjective morphism | Standard. |
| splittage (d'un groupe) | splitting (of a group) | Per glossary. |
| « point de F à valeurs dans un corps » | "point of F with values in a field" | Standard. |
| compatible avec les points marqués | compatible with the marked points | Standard. |
| augmentation (D(k) → k) | augmentation | Standard. |
| anneau semi-local régulier | regular semi-local ring | Standard. |
| algèbre de séries formelles | algebra of formal power series | Standard. |
| W_G(H) = Norm_G(H)/Centr_G(H) | W_G(H) | The Weyl-type quotient sheaf. |
| sous-préschéma ouvert | open subprescheme | Standard. |
| sous-préschéma ouvert et fermé | open and closed subprescheme | Standard (clopen). |
-->

[^XI-1-1]: One will now rather say "net" instead of "unramified".

[^N.D.E-XI-1]: *N.D.E.* "Residual extension" has been replaced by "residue field".

[^N.D.E-XI-2]: *N.D.E.* contravariant.

[^N.D.E-XI-3]: *N.D.E.* Reference to verify/make precise.

[^XI-4-1]: It is in fact proved for `G` flat and quasi-affine over `S` with connected fibers, provided one restricts to
    the central subtori of `G` (XV 8.8).

[^N.D.E-XI-4]: *N.D.E.* In the case `H` smooth (not necessarily affine) over a normal locally noetherian base `S`, M.
    Raynaud has shown that the largest representable open of the functor of subtori of `H` is a disjoint sum
    of smooth and affine opens over `S`. This is theorem IX.9.26 in *Faisceaux amples sur les schémas en
    groupes et sur les espaces homogènes*, Lecture Notes Maths. 119 (1970).

[^XI-4-2]: *Translator's note:* the French *tapis* is the standard SGA idiom for an underlying body of foundational
    results that one rolls out; "the general machinery of EGA IV §8" would be an equivalent rendering.

[^XI-5-1]: The situation has changed since the writing of this text, cf. XV and XIX N° 6.

[^XI-5-2]: EGA IV 15.5.1 and 18.10.7.

[^N.D.E-XI-5]: *N.D.E.* For a generalization to the non-affine case, see M. Raynaud, *Faisceaux amples sur les schémas
    en groupes et les espaces homogènes*, Lecture Notes Math. 119 (1970), IX.2.8.

[^N.D.E-XI-6]: *N.D.E.* Cf. remark XII.5.7. Let us mention here the following generalization. Without an affinity
    hypothesis on `G`, if `H` is a torus and `S` is locally noetherian, `U` is affine and smooth by a theorem
    of Raynaud (loc. cit., IX.2.6 and IX.2.8). Indeed, `G/Norm_G(H)` is an open of `M`, and the largest
    representable open of `M` is a disjoint sum of opens smooth and affine over `S`.

[^N.D.E-XI-7]: *N.D.E.* Under the hypothesis that `G` is of locally constant reductive rank.

[^XI-6-0]: The present N° does not use the results of N°s 3, 4, 5; its natural place would be in VI_B.

[^XI-6-1]: Cf. also J.P. Murre, *Representation of unramified functors. Applications*, Sém. Bourbaki N° 294 (May 1965),
    th. 3 (p. 13).
