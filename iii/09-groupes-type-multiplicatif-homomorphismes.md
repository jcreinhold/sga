# Exposé IX. Groups of multiplicative type: homomorphisms into a group scheme

<!-- label: III.IX -->

*by A. Grothendieck*

> Version 1.0 of 8 November 2009: additions in proof of 3.6 bis, 4.4–7, 5.0–6, 6.1, 7.1, 8.2. 8.1 and 4.5 to be
> revised.[^IX-0-0]

## 1. Definitions

<!-- original page 37 -->

**Definition 1.1.** *Let `S` be a prescheme and `G` an `S`-prescheme in groups. One says that `G` is a* group of
multiplicative type *if `G` is locally diagonalizable in the sense of the faithfully flat quasi-compact topology (cf. IV
6.3), i.e. if for every `s ∈ S`, there exist an open neighborhood `U` of `s` and a faithfully flat quasi-compact
morphism `S′ → U` such that `G′ = G ×_S S′` is a diagonalizable `S′`-group (I 4.4 and VIII 1.1).*

<!-- label: III.IX.1.1 -->

— *One says that `G` is* of quasi-isotrivial multiplicative type *if it is even locally diagonalizable in the sense of
the étale topology (IV 6.3), i.e. if in the preceding definition one can even take `S′ → U` étale surjective, or again
(which amounts to the same, as one sees by taking the disjoint-sum scheme of the various `S′` attached to the various
`s ∈ S`) if there exists `S′ → S` étale and surjective such that `G′ = G ×_S S′` is a locally diagonalizable
`S′`-group.*

— *If one can even choose `S′ → S` étale surjective and finite, one says that `G` is* of isotrivial multiplicative type.

— *Finally, one says that `G` is a* group of locally trivial *(resp.* locally isotrivial\*) multiplicative type if every
`s ∈ S` admits an open neighborhood `U` such that `G ×_S U` is a diagonalizable `U`-group (resp. a group of isotrivial
multiplicative type, i.e. there exists an étale surjective finite morphism `S′ → U` such that `G ×_S S′` is a
diagonalizable `S′`-group).\*

**Comments 1.2.** One will note that the five preceding notions all derive from the notion of diagonalizable group by
the process of localization, in the sense of five different "topologies" associated with `(Sch)`.

<!-- label: III.IX.1.2 -->

We agree, generally, that when the word "locally" is not made explicit <!-- original page 38 --> by specifying the
topology envisaged, the Zariski topology is meant, in accordance with received terminology. In the terminology
introduced here, "of locally trivial multiplicative type" is equivalent to "locally diagonalizable" of VIII 1.1, and
likewise "trivial" translates as "diagonalizable". Among the five notions introduced, one has the following diagram of
implications, which results from the corresponding relations between the topologies in play:

```text
                 multiplicative type (general)
                            ⇑
                      quasi-isotrivial
                            ⇑
            locally isotrivial ⇐ isotrivial
                  ⇑                   ⇑
            locally trivial ⇐    trivial
```

<!-- TRANSLATOR NOTE: original diagram is degraded by OCR; the implications are reconstructed from the surrounding text
and from the standard implications between the five notions. -->

From the practical point of view, let us point out at once that all the groups of multiplicative type we shall encounter
will be quasi-isotrivial; thus, we shall see in the following Exposé (X 4.5) that when `G` is of finite type over `S`,
then `G` is automatically quasi-isotrivial, but we shall give examples where it is not locally isotrivial. We shall
likewise see there that `G` may be locally trivial without being isotrivial nor, a fortiori, trivial (which easily
implies that the inclusions of the preceding diagram are strict).

On the other hand, we shall also see there (X 5.16) that when `S` is locally noetherian and normal (more generally
geometrically unibranch), every group of multiplicative type of finite type over `S` is necessarily isotrivial, and
moreover trivial as soon as it is locally trivial (or even merely trivial on a dense open). This explains that most
groups of multiplicative type one will encounter in practice will doubtless be isotrivial, all the more so since we
shall see later that the maximal tori of semisimple group schemes are automatically isotrivial.

**Definition 1.3.** *Let `S`, `G` be as in 1.1. One says that `G` is a* torus *if it is locally isomorphic, in the sense
of the faithfully flat quasi-compact topology, to a group of the form `G_m^r` (where `r` is an integer `⩾ 0`).*

<!-- original page 39 -->

<!-- label: III.IX.1.3 -->

With the notation of 1.1, this means therefore that one can choose `S′` such that `G′` be isomorphic to a group of the
form `(G_{m,S′})^r`. One will note that the integer `r` depends on `s ∈ S`: it is the dimension of the fiber
`G_s = G ⊗_S κ(s)`. It is a locally constant function of `s`, as one verifies at once. There is occasion to generalize
this remark:

**Definition 1.4.** *Let `G` be a diagonalizable group scheme over a field `k`, so that `G` is isomorphic to a group
`D_k(M)`, where `M` is an ordinary commutative group, defined up to isomorphism by this condition — more precisely
`M ≃ Hom_{k-gr.}(G, G_{m,k})` (VIII 1.3). The isomorphism class of `M` is called the* type *of the diagonalizable group
`G`; it is evidently invariant under extension of the base field.*

<!-- label: III.IX.1.4 -->

*If now `G` is a group scheme of multiplicative type over an arbitrary prescheme `S`, then for every `s ∈ S`, there
exists an extension `k` of `κ(s)` such that `G ×_S Spec(k)` is a diagonalizable `k`-group;*[^N.D.E-IX-1] *its type is
then independent of the chosen extension by the preceding remark, and will be called the* type of `G` at `s`, *or* type
of `G_s`. *In particular, if `G` itself is diagonalizable, hence isomorphic to a group of the form `D_S(M)`, then for
every `s ∈ S`, the type of `G` at `s` equals the class of the group `M`.*

*In general, if `G` is a group of multiplicative type over `S` and `M` an ordinary commutative group, one will say that
`G` is* of type `M` *if it is of type `M` at every point `s ∈ S`, in other words if `G` is locally isomorphic to
`D_S(M)` in the sense of the faithfully flat quasi-compact topology.*

**Remark 1.4.1.**[^N.D.E-IX-2] *a) One sees immediately that for a given group of multiplicative type `G` over `S`, the
function `s ↦ type of G_s` is locally constant on `S`: indeed, with the notation of 1.1, if `G′` is of type `M`, then
`G` is of type `M` on the neighborhood `U` of `s`. It follows that one has a canonical partition of `S` into a disjoint
sum of preschemes `S_i`,* <!-- original page 40 --> *such that for every `i`, `G_{S_i}` is of type `M_i`, where the
`M_i` are pairwise non-isomorphic commutative groups.*

<!-- label: III.IX.1.4.1 -->

*b) In particular, if `S` is connected, the type of the fibers of `G` is constant, i.e. there exists a commutative group
`M` such that `G` is of type `M`. Finally, if `G` is a torus, the type of `G` at `s` is characterized by the integer
`dim G_s` (indeed, `G_s` is of type `ℤ^n`, where `n = dim G_s`).*

**Remark 1.5.** *a) It is trivial on definitions 1.1 and 1.3 that these are "compatible with base extension". Thus, if
`G` is a prescheme in groups over `S`, and `S′ → S` is a base-change morphism, then if `G` is of multiplicative type
(resp. of isotrivial multiplicative type, etc.), the same holds for `G′`.*

<!-- label: III.IX.1.5 -->

*b) When moreover `S′ → S` is faithfully flat and quasi-compact, then if `G′` is of multiplicative type, resp. a torus,
the same holds for `G`. If moreover `S′ → S` is étale (resp. finite étale), and `G′` quasi-isotrivial (resp.
isotrivial), the same holds for `G`.*

*c) Finally, returning to an arbitrary base-change morphism `f : S′ → S`, if `s′ ∈ S′` and `s = f(s′)`, then the type of
`G′` at `s′` is equal to that of `G` at `s`, since `G′_{s′} = G_s ⊗_{κ(s)} κ(s′)`.*

## 2. Extension of certain properties of diagonalizable groups to groups of multiplicative type

The extensions in question are essentially trivial consequences of the results of the preceding Exposé, given
Definitions 1.1 and the "local" nature (in the sense of the faithfully flat quasi-compact topology) of the results
concerned.

**Definition 2.0.**[^N.D.E-IX-3] *We denote by `M` the set of faithfully flat quasi-compact morphisms.*

<!-- label: III.IX.2.0 -->

**Proposition 2.1.** *Let `G` be a group of multiplicative type over a prescheme `S`. One has the following:*

<!-- label: III.IX.2.1 -->

*a) `G` is faithfully flat over `S`, and affine over `S` (a fortiori quasi-compact over `S`).*

<!-- original page 41 -->

*b) `G` of finite type over `S` `⇔` `G` of finite presentation over `S` `⇔` for every `s ∈ S`, the type of `G` at `s` is
given by a commutative group of finite type.*

*c) `G` finite over `S` `⇔` for every `s ∈ S`, the type of `G` at `s` is given by a finite commutative group `⇔` (if `S`
quasi-compact) `G` is of finite type over `S` and is annihilated by an integer `n > 0`.*

*c′) `G` integral over `S` `⇔` for every `s ∈ S`, the type of `G` at `s` is given by a torsion commutative group.*

*d) `G` is the unit group `⇔` for every `s ∈ S`, the type of `G` at `s` is given by the zero commutative group.*

*e) `G` is smooth over `S` `⇔` for every `s ∈ S`, the type of `G` at `s` is given by a commutative group of finite type
whose torsion subgroup is of order prime to the characteristic of `κ(s)`.*

These statements follow from VIII 2.1, taking into account that the properties in question descend along faithfully flat
quasi-compact morphisms (cf. SGA 1, VIII or EGA IV₂, § 2).

Using VIII 3.5, one obtains likewise:

**Proposition 2.2.** *Let `G` be a group of multiplicative type and of finite type over `S`; then for every integer
`n ≠ 0`, the kernel `_nG` of `n · id_G` is a group of multiplicative type, finite over `S`.*

<!-- label: III.IX.2.2 -->

**Proposition 2.3.** *Let `G` be a group of multiplicative type over the prescheme `S`, operating freely on the right on
the `S`-prescheme `X` affine over `S`. Then:*

<!-- label: III.IX.2.3 -->

*a) The equivalence relation defined by `G` in `X` is `M`-effective (IV 3.4), and `Y = X/G` is affine over `S`.*

*b) If moreover `X` is of finite presentation (resp. of finite type) over `S`, the same holds for `Y`.*

The first assertion follows from VIII 5.1, which treats the case where `G` is diagonalizable, <!-- original page 42 -->
and from IV 3.5.2, which allows one to reduce to that case, given that faithfully flat quasi-compact morphisms `S′ → S`
are morphisms of effective descent for the fibered category of affine schemes over others, i.e. for every `Y′` affine
over `S′` endowed with a descent datum relative to `S′ → S`, this descent datum is effective, i.e. `Y′` comes from a `Y`
affine over `S` (cf. SGA 1, VIII 2.1).

For the second assertion one is likewise reduced to the diagonalizable case VIII 5.8, since the finiteness conditions
envisaged descend along faithfully flat quasi-compact morphisms (SGA 1, VIII 3.3 and 3.6[^N.D.E-IX-4]). Proceeding as in
VIII, Corollaries 5.5 to 5.7, one deduces from 2.3:

**Corollary 2.4.** *Under the conditions of 2.3, the graph morphism*

<!-- label: III.IX.2.4 -->

```text
X ×_S G ⟶ X ×_S X
```

*is a closed immersion. For every section `σ` of `X` over `S`, the corresponding morphism `G → X`, `g ↦ σ · g` is a
closed immersion.*

In particular:

**Corollary 2.5.** *Let `u : G → H` be a monomorphism of `S`-preschemes in groups, with `G` of multiplicative type and
`H` affine over `S`. Then `u` is a closed immersion, `H/G = Y` exists and is affine over `S`, and finally `H` is a
principal homogeneous bundle over `Y` with group `G_Y`.*

<!-- label: III.IX.2.5 -->

**Remark 2.6.** *Let `u : G → H` be a monomorphism of `S`-preschemes in groups, with `G` of multiplicative type and of
finite type over `S`, `H` of finite presentation over `S` and separated over `S`. Then one can show that `u` is a closed
immersion, using VIII 7.12 (see remark VIII 7.13 b)).*

<!-- label: III.IX.2.6 -->

**Proposition 2.7.** *Let `u : G → H` be a homomorphism of `S`-groups of multiplicative type, with `H` of finite type
over `S`.* <!-- original page 43 --> *Then:*

<!-- label: III.IX.2.7 -->

*(i) `G_0 = Ker u` is an `S`-group of multiplicative type, the equivalence relation defined by `G_0` in `G` is
`M`-effective, hence (IV 3.4) `u` factors as*

```text
G ⟶ G/G_0 = I ⟶ H,
```

*where `I → H` is a monomorphism*[^N.D.E-IX-5] *of `S`-groups; `I` is of multiplicative type, the equivalence relation
in `H` defined by `I` is `M`-effective, consequently `H_0 = H/I` exists, and moreover `H_0` is of multiplicative type.*

*(ii) `H_0` and `I` are of finite type, and the same holds for `G_0` if `G` is.*

*Proof.* Proceeding as for 2.3, one is reduced to the case where `G` and `H` are diagonalizable, and then 2.7 reduces to
VIII 3.4.

Let us note the following corollaries:

**Corollary 2.8.** *a) Let `S` be a prescheme. Then the category of `S`-groups of multiplicative type and of finite type
is an abelian category.*

<!-- label: III.IX.2.8 -->

*b) Let `u : G → H` be a homomorphism in this category; for it to be a monomorphism (resp. an epimorphism, resp. an
isomorphism) in this category, it is necessary and sufficient that `u` be a monomorphism of preschemes (resp. that `u`
be faithfully flat, resp. that `u` be an isomorphism of preschemes).*

It suffices to note that the product of two `S`-groups of multiplicative type is again of multiplicative type (which is
immediate), and evidently of finite type over `S` if both factors are. The rest of 2.8 follows immediately from 2.7; the
detail is left to the reader.

**Corollary 2.9.** *Let `u : G → H` be a homomorphism of `S`-groups of multiplicative type and of finite type. Let `U`
be the set of points `s ∈ S` such that `u_s : G_s → H_s` is a monomorphism (resp. faithfully flat, resp. an
isomorphism). Then `U` is both open and closed,* <!-- original page 44 --> *and the induced homomorphism
`u_U : G_U → H_U` is a monomorphism (resp. faithfully flat, resp. an isomorphism).*

<!-- label: III.IX.2.9 -->

Let `P` (resp. `Q`) be the kernel (resp. cokernel) of `u`. By 2.7, `Q` exists and `P` and `Q` are of multiplicative
type; moreover the formation of `P` and of `Q` commutes with every base change `S′ → S`, in particular with the
formation of fibers. On the other hand, `u` is a monomorphism (resp. faithfully flat, resp. an isomorphism) if and only
if `P = 0` (resp. `Q = 0`, resp. `P = Q = 0`). Thanks to these remarks, one is therefore reduced to verifying the
following: if `R` is an `S`-group of multiplicative type, then the set `U` of `s ∈ S` such that `R_s = 0` is open and
closed, and `R_U = 0`. But this is contained in Remark 1.4.1 a).

**Corollary 2.10.** *Let `G` be an `S`-group of multiplicative type and of finite type, and `H`, `H′` two subgroups of
multiplicative type.*

<!-- label: III.IX.2.10 -->

*a) `H″ = H ∩ H′` is a subgroup of multiplicative type of `G`.*

*b) Let `U` be the set of `s ∈ S` such that `H_s ⊆ H′_s` (resp. `H_s = H′_s`). Then `U` is open and closed, and
`H_U ⊆ H′_U` (resp. `H_U = H′_U`).*

Of course the intersection sign in `H ∩ H′` denotes the intersection in the functorial sense, i.e. `H ×_G H′`, which is
evidently an `S`-subgroup of `G`; likewise the inclusion sign (resp. equality sign) denotes the order relation (resp.
the equality) between subfunctors of `H` (and not inclusion (resp. equality) of underlying sets).

Applying first 2.7 to the inclusion morphism `H → G`, one finds that `H` is of finite type; likewise `H′` is of finite
type. It then follows from 2.8 that `H ∩ H′` is of multiplicative type and of finite type (one will note that the
canonical functor from the category envisaged in 2.8 to the category `(Sch)/S` commutes with finite projective limits).

The formation of `H ∩ H′` commutes with base extension, in particular with the formation of fibers. On the other hand,
`H ⊆ H′` (resp. `H = H′`) is equivalent to `H″ = H` (resp. `H″ = H` and `H″ = H′`). Consider then the canonical
homomorphisms `H″ → H` and `H″ → H′`; then `U` is the set of `s ∈ S` such that the induced homomorphism `H″_s → H_s` is
an isomorphism (resp. such that `H″_s → H_s` and `H″_s → H′_s` are isomorphisms). <!-- original page 45 --> By 2.9, it
follows that `U` is open and closed, and that `H″_U → H_U` (resp. `H″_U → H_U` and `H″_U → H′_U`) are isomorphisms.
Hence the desired conclusion.

**Proposition 2.11.** *Let `S` be a prescheme, `G` an `S`-group of multiplicative type and of finite type over `S`, `H`
a subgroup of multiplicative type of `G`, and `K = G/H` (which is a group of multiplicative type, quotient of `G`).*

<!-- label: III.IX.2.11 -->

*(i) Suppose `G` is trivial, i.e. diagonalizable. Then there exists a partition of `S` into open-and-closed parts `S_i`,
such that for every `i`, `H_{S_i}` and `K_{S_i}` are diagonalizable. In particular, if `S` is connected, `H` and `K` are
diagonalizable.*

*(ii) Same statement as in (i), replacing "diagonalizable" by "isotrivial", provided that `S` is connected, or locally
connected, or quasi-compact.*

*(iii) Suppose `G` is locally trivial (resp. locally isotrivial, resp. quasi-isotrivial); then the same holds for `K`
and `H`.*

*Proof.* (i) By hypothesis `G = D_S(M)`, where `M` is a commutative group of finite type. For every quotient group `M_i`
of `M`, let `H_i = D_S(M_i)` be the corresponding diagonalizable subgroup of `G` (VIII 3.1). Let `S_i` be the set of
`s ∈ S` such that `H_s = (H_i)_s`; by 2.10, `S_i` is open and closed, and one has `H_{S_i} = (H_i)_{S_i}`, hence
`H_{S_i}` is diagonalizable, hence so is `K_{S_i}` (VIII 3.1). Evidently the `S_i` are pairwise disjoint; we claim that
they cover `S`. This follows from the fact that for every `s`, `H_s` is diagonalizable, as a subgroup of the
diagonalizable group `G_s` (cf. 8.1 below[^N.D.E-IX-6]); hence `H_s` is of the form `D_{κ(s)}(M_i)`, by VIII, 1.5 and
3.2 b). Restricting to the family of non-empty `S_i`, the conclusion (i) appears.

(ii) By hypothesis, there exists `S′ → S` étale finite surjective such that `G_{S′}` is diagonalizable. Hence every
point of `S′` has an open-and-closed neighborhood `U′` such that `H_{U′}` and `K_{U′}` are diagonalizable. Then the
image `U` of `U′` in `S` is open and closed, and `S′ → S` still induces an étale finite surjective morphism `U′ → U`;
hence one sees that every <!-- original page 46 --> point `s` of `S` has an open-and-closed neighborhood `U` such that
`H_U` and `K_U` are isotrivial. The conclusion (ii) follows at once.

(iii) Follows at once from (i) and (ii) and the definitions. Note moreover that the "quasi-isotrivial" case will also
follow from the more general fact that "finite type ⇒ quasi-isotrivial", announced in 1.2 (cf. X 4.5).

## 3. Infinitesimal properties: lifting and conjugation theorems

The fundamental infinitesimal properties of groups of multiplicative type follow from the following theorem:

**Theorem 3.1.** *Let `S` be an affine scheme, `H` an `S`-group of multiplicative type, `F` a quasi-coherent sheaf on
`S` on which `H` operates (I 4.7). Then one has*

<!-- label: III.IX.3.1 -->

```text
H^i(H, F) = 0    for    i > 0,
```

*where `H^i` is the Hochschild cohomology studied in Exp. I, § 5.*

Indeed, by loc. cit., 5.3, the Hochschild cohomology is described, in terms of the affine rings `A` of `S` and `B` of
`G`, and the module `M` over `A` defining `F`, as the cohomology of a complex of `A`-modules `C^•(H, M)`, the formation
of which commutes with every base change `A → A′`. Consequently, for a base change `A → A′` with `A′` flat over `A`, one
has

```text
H^i(H′, F′) = H^i(H, F) ⊗_A A′,
```

and consequently, if one supposes even `A′` faithfully flat over `A`, in order to prove that `H^i(H, F)` is zero, it
suffices to prove that the same holds for `H^i(H′, F′)`. This remark reduces us to verifying 3.1 in the case where `G`
is diagonalizable; in that case this was proved in I 5.3.3.

<!-- original page 47 -->

Using the results of Exposé III, we shall deduce from 3.1 various consequences of geometric nature:

**Theorem 3.2.** *Let `S` be an affine scheme, `S_0` an affine subscheme defined by an ideal `J`, `H` a group of
multiplicative type over `S`, `G` an arbitrary prescheme in groups over `S`, `u, v : H → G` two homomorphisms of groups,
`u_0, v_0 : H_0 → G_0` the homomorphisms deduced from `u, v` by the base change `S_0 → S`. If `J^2 = 0` and `u_0 = v_0`,
then there exists a `g ∈ G(S)` such that `v = int(g) ∘ u` and `g_0 = e`.*

<!-- label: III.IX.3.2 -->

This follows from III 2.1 (ii), and from 3.1 (vanishing of `H^1`).

**Corollary 3.3.** *Under the preliminary conditions of 3.2, suppose moreover `G` smooth over `S`, but assume only `J`
nilpotent (not necessarily of square zero). If there exists `g_0 ∈ G_0(S_0)` such that `v_0 = int(g_0) ∘ u_0`, then
`g_0` lifts to a `g ∈ G(S)` such that `v = int(g) ∘ u`.*

<!-- label: III.IX.3.3 -->

By induction on the integer `n` such that `J^n = 0`, one is reduced to the case where `J` is of square zero. Moreover,
`G` being smooth over `S`, one can lift `g_0` to an element `g′` of `G(S)`. Replacing `v` by `v′ = int(g′) ∘ u`, one is
then reduced to the situation of 3.2.

**Corollary 3.4.** *Under the preliminary conditions of 3.2, with `J` nilpotent, suppose moreover `u` is central (for
example `G` commutative). Then `u_0 = v_0` implies `u = v`.*

<!-- label: III.IX.3.4 -->

Indeed, the reduction to the case where `J` has square zero is again immediate, and then it suffices to apply 3.2. In
particular:

**Corollary 3.5.** *Let `S`, `S_0`, `H`, `G` be as in 3.2, with `J` nilpotent. Let `u : H → G` be a homomorphism of
`S`-groups such that `u_0 : H_0 → G_0` is the unit homomorphism. Then `u` is the unit homomorphism.*

<!-- label: III.IX.3.5 -->

<!-- original page 48 -->

**Theorem 3.6.** *Let `S` be an affine scheme, `S_0` a subscheme defined by a nilpotent ideal `J`, `H` a group of
multiplicative type over `S`, `G` a prescheme in groups smooth over `S`, `u_0 : H_0 → G_0` a homomorphism of the
`S_0`-groups deduced by the base change `S_0 → S`.*

<!-- label: III.IX.3.6 -->

*Then there exists a homomorphism `u : H → G` of `S`-groups which lifts `u_0` (and by 3.3 any two such liftings `u, u′`
are conjugate by an element of `G(S)` reducing along the unit element of `G(S_0)`).*

This follows from III 2.1 and 2.3, and from 3.1 (vanishing of `H^2` for the existence of the lift of `u_0`, vanishing of
`H^1` for the uniqueness up to conjugation).

One can prove in the same way the following variants of 3.2 to 3.6 (which in fact entail the preceding statements, by
applying them to the graph subgroups of the homomorphisms envisaged in 3.2 to 3.6):

**Theorem 3.2 bis.** *Let `S` be an affine scheme, `S_0` a subscheme defined by an ideal `J`, `G` an `S`-prescheme in
groups, `H, H′` subpreschemes in groups, of multiplicative type, `G_0, H_0, H′_0` the groups over `S_0` deduced by the
base change `S_0 → S`. If `J^2 = 0` and `H_0 = H′_0`, then there exists `g ∈ G(S)` such that `H′ = int(g)(H)` and
`g_0 = e`.*

<!-- label: III.IX.3.2bis -->

**Corollary 3.3 bis.** *Under the preliminary conditions of 3.2 bis, suppose moreover `G` smooth over `S`, and `J`
nilpotent (not necessarily of square zero). Let `g_0 ∈ G_0(S_0)` be such that `H′_0 = int(g_0)(H_0)`; then `g_0` lifts
to `g ∈ G(S)` such that `H′ = int(g)(H)`.*

<!-- label: III.IX.3.3bis -->

**Corollary 3.4 bis.** *Under the preliminary conditions of 3.2 bis, suppose `J` nilpotent, `H` central (for example `G`
commutative). Then `H_0 = H′_0` implies `H = H′`.*

<!-- label: III.IX.3.4bis -->

**Theorem 3.6 bis.** *Let `S` be an affine scheme, `S_0` a subscheme defined by a nilpotent ideal `J`,* <!-- original
page 49 --> *`G` an `S`-prescheme in groups smooth over `S`, `H_0` a subprescheme in groups of `G_0 = G ×_S S_0`, of
multiplicative type. Then:*

<!-- label: III.IX.3.6bis -->

*(a) There exists a subprescheme in groups `H` of `G`, flat over `S`, such that `H ×_S S_0 = H_0`.*

*(b) Such an `H` is necessarily of multiplicative type.*

*(c) Finally, by 3.2 bis, any two such liftings `H, H′` of `H_0` are conjugate by an element `g ∈ G(S)` reducing along
the unit element of `G(S_0)`.*

Let us show how one may prove 3.2 bis (of which 3.3 bis and 3.4 bis are an immediate consequence) and assertion (a) of
3.6 bis. The latter follows from 3.1 (vanishing of `H^2`) and from III 4.37 (ii). Similarly 3.2 bis follows from 3.1
(vanishing of `H^1`) and from III 4.37 (i), at least when `G` and `H` are smooth over `S`.

But using the results of the following Exposé, one can very simply deduce 3.2 bis and 3.6 bis, in the general form
stated here, from 3.2 resp. 3.6. For 3.2 bis, it suffices indeed to note that by X 2.1, `H` and `H′` are isomorphic,
which reduces us to 3.2.

For 3.6 bis, one notes that `H_0` is necessarily of finite type over `S_0`:[^N.D.E-IX-7] indeed, as a subprescheme of
`G_0`, which is smooth over `S_0`, `H_0` is locally of finite type over `S_0`; but, by 2.1 a), `H_0` is affine over
`S_0`, hence is of finite type over `S_0`. Then, by X 4.5, `H_0` is quasi-isotrivial, hence comes, by X 2.1, from a
group of multiplicative type `H` over `S`.[^N.D.E-IX-8] Then, by 3.6, there exists a homomorphism of `S`-groups
`u : H → G` which lifts the immersion `H_0 ↪ G_0`; since `H` and `H_0` (resp. `G` and `G_0`) have the same underlying
topological space, and since, for every `h ∈ H`, the morphism <!-- original page 50 --> `O_{G,u(h)} → O_{H,h}` is
surjective (since it is so after reduction modulo `J`, which is nilpotent), `u` is also an immersion (cf. EGA I, 4.2.2).

Finally, for every lifting `H` of `H_0` to a flat subgroup of `G`, `H` is necessarily of multiplicative type by X
2.3,[^N.D.E-IX-9] which also proves assertion (b) of 3.6 bis. (The reader will verify that the results 3.2 bis to 3.6
bis are not used in Exposé X, hence that there is no vicious circle!)

**Proposition 3.8.**[^N.D.E-IX-10] *Let `S` be a prescheme, `S_0` a closed subprescheme defined by a locally nilpotent
ideal `J`, `G` an `S`-group of multiplicative type, `X` an `S`-prescheme locally of finite presentation. Suppose that
`G` operates on `X`, in such a way that `G_0 = G ×_S S_0` operates trivially on `X_0 = X ×_S S_0`. Under these
conditions, `G` operates trivially on `X`.*

<!-- label: III.IX.3.8 -->

The proof is that of III 2.4 b); one can also reduce to loc. cit. by noting that 3.8 reduces at once to the case where
`G` is diagonalizable, which is the case envisaged in loc. cit.

**Corollary 3.9.** *Let `S, S_0` be as above, and `u : G → H` a homomorphism of `S`-groups, with `G` of multiplicative
type and `H` locally of finite presentation over `S`. Suppose that the homomorphism `u_0 : G_0 → H_0` deduced by base
change `S_0 → S` is central. Then `u` is central.*

<!-- label: III.IX.3.9 -->

Indeed, it suffices to apply 3.8 by taking `X = H` and making `G` operate on `H` by
`(g, h) ↦ int(u(g)) · h = u(g) h u(g)^{-1}`.

## 4. The density theorem

This theorem (cf. 4.7 below)[^IX-4-1], together with the theorem[^N.D.E-IX-11] of N° 7, will be the essential tool in
the present Exposé and the two following, for passing from the infinitesimal properties of groups of multiplicative
type, which have just been developed, to the "finite" properties.

**Definition 4.1.** *Let `X` be a prescheme. A family `(Z_i)_{i ∈ I}` of subpreschemes of `X` is said to be*
schematically dense *if for every open `U` of `X`, and every closed subprescheme `U_0` of `U` which majorizes the
`Z_i ∩ U`, one has `U_0 = U`.*

<!-- label: III.IX.4.1 -->

*One says that a subprescheme `Z` of `X` is* schematically dense in `X` *if such is the case of the family reduced to
`Z`.*

One sees immediately (cf. EGA IV₃, 11.10.1) that the definition is equivalent to saying that for every open `U` of `X`,
every section `f` of `O_U` which is zero on the `Z_i ∩ U` is zero, which also means that the intersection of the kernels
of the canonical homomorphisms

```text
u_i : O_X ⟶ (v_i)_*(O_{Z_i})
```

is zero, where `v_i : Z_i → X` is the canonical immersion.[^N.D.E-IX-12] When `X` lies over a prescheme `S`, this is
again equivalent to saying that for every open `U` of `X` and every pair `(u, v)` of morphisms from `U` into an
`S`-prescheme `Y` separated over `S` that coincide on the `Z_i ∩ U`, one has `u = v`. (Indeed, the relation `u = v` is
equivalent to `U_0 = U`, where `U_0` is the inverse image of the diagonal of `Y ×_S Y` by the `S`-morphism `X → Y ×_S Y`
defined by `(u, v)`; <!-- original page 51 --> this diagonal is a closed subprescheme of `Y ×_S Y`, hence `U_0` is a
closed subprescheme of `U`, majorizing the `Z_i ∩ U` by the hypothesis on `(u, v)`; hence if the family `(Z_i)` is
schematically dense, one will have `U_0 = U`, hence `u = v`; the converse implication is seen by simply taking
`Y = Spec O_S[T]`.)

With the terminology introduced in EGA I, end of N° 9.5, to say that the subprescheme `Z` of `X` is schematically dense
also means that `X` is identical to the adherence subprescheme of `Z` in `X`.

**Lemma 4.2.** *Let `X` be a flat `S`-prescheme, `(Z_i)_{i ∈ I}` a family of subpreschemes of `X` flat over `S`. Let
`S_0` be a subprescheme of `S`, defined by a nilpotent ideal `J`; suppose the modules `J^n/J^{n+1}` locally free over
`S_0`.*

<!-- label: III.IX.4.2 -->

*Let `X_0, Z'_i` be deduced from `X, Z_i` by the base change `S_0 → S`. Then, if the family `(Z'_i)_{i ∈ I}` is
schematically dense in `X_0`, the family `(Z_i)_{i ∈ I}` is so in `X`.*

Suppose `J^{n+1} = 0` (where `n ⩾ 0`); let us argue by induction on `n`, the assertion being trivial for `n = 0`.
Defining `S_m, X_m, Z^i_m` by reduction modulo `J^{m+1}` as is customary, the induction hypothesis already implies that
`(Z^i_{n-1})_{i ∈ I}` is schematically dense in `X_{n-1}`. Replacing `X` by an induced open if necessary, we are reduced
to proving that every section `f` of `O_X` which vanishes on the `Z_i` is zero.

Now the section `f_{n-1}` of `O_{X_{n-1}} = O_X/J^n O_X` defined by `f` vanishes on the `Z^i_{n-1}`, hence is zero,
hence `f` is a section of `J^n O_X`. Since `X` is flat over `S`, one has

```text
J^n O_X ⥲ E ⊗_{O_{S_0}} O_{X_0},          where E = J^n = J^n/J^{n+1}.
```

Likewise, since each `Z_i` is flat over `S`, the restriction `f_i` of `f` to `Z_i` may be regarded as a section of:

```text
J^n O_{Z_i} ⥲ E ⊗_{O_{S_0}} O_{Z'_i}.
```

By hypothesis, the `f_i` are zero. Now `E` is locally free by hypothesis, hence so is `F = E ⊗_{O_{S_0}} O_{X_0}`.

<!-- original page 52 --> Hence `f` is a section of the locally free module `F` over `X_0`, such that for every `i` its

restriction to `Z'_i` is zero. Since `(Z'_i)_{i ∈ I}` is schematically dense in `X_0`, it follows at once that `f` is
zero. QED.

**Corollary 4.3.** *Let `X` be a locally noetherian `S`-prescheme flat over `S`, `(Z_i)_{i ∈ I}` a family of
subpreschemes of `X` flat over `S`. Suppose that for every `s ∈ S`, the family `(Z_{i,s})_{i ∈ I}` of fibers at `s` is
schematically dense in `X_s`. Then the family `(Z_i)_{i ∈ I}` is schematically dense in `X`.*

<!-- label: III.IX.4.3 -->

Replacing `X` by an induced open if necessary, one is reduced to proving that every section `f` of `O_X` whose
restrictions to the `Z_i` are zero is itself zero.[^N.D.E-IX-13] For this, it suffices to prove that for every `x ∈ X`,
the image of `f` in `O_{X,x}` is zero. Denote by `m_x` the maximal ideal of `O_{X,x}`, and by `m_s` that of `O_{S,s}`,
where `s` is the image of `x` in `S`. Since `O_{X,x}` is noetherian, one has `⋂_{n ∈ ℕ} m_x^n = 0`, hence a fortiori
`⋂_{n ∈ ℕ} O_{X,x} m_s^n = 0`.

So it suffices to show that, for every integer `n`, the section induced by `f` on `X ×_S Spec(O_{S,s}/m_s^{n+1})` is
zero. By hypothesis, the family of fibers `Z_{i,s} = Z_i ⊗_{O_{S,s}} κ(s)` is schematically dense in the fiber
`X_s = X ⊗_{O_{S,s}} κ(s)`. This reduces us to the case where `S` is the spectrum of a local ring whose maximal ideal
`J` is nilpotent, `S_0 = Spec κ(s)`, and the hypotheses of 4.2 are satisfied; hence the conclusion.

**Lemma 4.4.** *Let `S` be a locally noetherian prescheme, `X` a locally noetherian `S`-prescheme flat over `S`,
`(Z_i)_{i ∈ I}` a family of subpreschemes of `X` flat over `S`. Suppose that for every `s ∈ S`, the family
`(Z_{i,s})_{i ∈ I}` of fibers at `s` is schematically dense in `X_s`.*

<!-- label: III.IX.4.4 -->

*Then, for every base change `S′ → S` (`S′` not necessarily locally noetherian), the family `(Z'_i)_{i ∈ I}` is
schematically dense in `X′` (i.e. the family `(Z_i)_{i ∈ I}` is universally schematically dense in `X` relative to `S`,
cf. EGA IV₃, Def. 11.10.8).*

*Proof.*[^N.D.E-IX-14] Let `f′` be a section of `O_{X′}` over an open `U′` of `X′`, vanishing on the `Z'_i`; we must
show that `f′` is zero. Let `s′ ∈ S′`; it suffices to prove that `f′` is zero at every point of `U′` above `s′`. Let `s`
be the image of `s′` in `S`; replacing `S, S′` by the spectra of the local rings at `s, s′` if necessary, one may
suppose `S, S′` <!-- original page 53 --> local with `s, s′` as closed points. One may moreover suppose `X` affine,
hence

```text
S = Spec(A),    S′ = Spec(A′),    X = Spec(B),    X′ = Spec(B′),    B′ = B ⊗_A A′
```

where `A, A′` are local, `A → A′` is a local homomorphism, and `A, B` are noetherian. One may also suppose `U′` affine,
of the form `X′_{g′}`, with `g′ ∈ B′`.

For every sub-`A`-algebra `A″` of `A′`, consider `S″ = Spec(A″)` and `X″, Z^i_{n″}` deduced from `X, Z_i` by the base
change `S″ → S`, giving the diagram:

```text
Z_i ←  Z^i_{n″} ← Z'_i
 ↓        ↓        ↓
 X  ←   X″   ←   X′
 ↓        ↓        ↓
 S  ←   S″   ←   S′.
```

We restrict in what follows to those `A″` which are localizations of finite-type sub-`A`-algebras `A″_1` of `A′` at
`m′ ∩ A″_1` (where `m′` is the maximal ideal of `A′`), so that the homomorphisms `A → A″ → A′` are local. Note that
these `A″` form an increasing filtered family of subalgebras whose union is `A′`, hence their direct limit is also `A′`.
One has therefore likewise `B′ = lim_{A″} B ⊗_A A″`. Hence there exist an `A″` and an element `g″ ∈ B″ = B ⊗_A A″` whose
image in `B′` is `g′`.

[^N.D.E-IX-15] By Lemma 4.5 below, the property that the family of fibers `(Z_{i,s})_{i ∈ I}` be schematically dense in
`X_s` is preserved by every base change `S″ → S`; consequently, since each `S″` is locally noetherian, if one replaces
`S` by an appropriate `S″`, and `X, Z_i` by `X″, Z″_i`, the hypotheses of 4.4 will be preserved.

Hence, replacing `S` by `S″` (and `X, Z_i` by `X″, Z″_i`) if necessary, one may suppose that `g′` comes from `g ∈ B`.
Replacing `X` by the open `X_g = U` if necessary, one may therefore suppose `U′ = X′`. One sees likewise that one may
suppose that `f′` comes from a section `f` of `O_X` over `X`.

Let `Y = V(f)` be the subscheme of `X` defined by `f`, and `Y_i = Z_i ×_X Y` its intersection with `Z_i`, which is a
closed subscheme of `Z_i`, equal to `V(f_i)`, where `f_i` is the section of `O_{Z_i}` induced by `f`. Denoting by
`Y′, Y'_i` the `S′`-schemes deduced from the preceding by base change, one will again have

```text
Y′ = V(f′),    Y'_i = Z'_i ×_{X′} Y′ = V(f'_i),
```

and one has the analogous relations for `Y″, Y″_i`. The hypothesis that `f′` vanishes on the `Z'_i` is expressed by the
relations `Y'_i = Z'_i` for every `i`.[^N.D.E-IX-16]

Let `m` be the maximal ideal of `A`. For every integer `n ⩾ 0`, introduce the subscheme `S_n = Spec(A/m^{n+1})` of `S`,
and the schemes `X_n, Y_n, Z^i_n, Y^i_n` deduced from `X, Y, Z_i, Y_i` by the base change `S_n → S`. In general, for
every `S`-prescheme `P`, we shall set `P_n = P ×_S S_n`.

<!-- original page 54 -->

For every `n`, and `i ∈ I`, consider the functor

```text
F^i_n = ∏_{Z^i_n/S_n} Y^i_n/Z^i_n : (Sch)°/S_n ⟶ (Ens)
```

defined by (cf. VIII, 6.4): for every `P` over `S_n`,

```text
F^i_n(P) = Γ((Y^i_n)_P / (Z^i_n)_P) =  ∅       if (Y^i_n)_P ≠ (Z^i_n)_P;
                                       {id}    if (Y^i_n)_P = (Z^i_n)_P.
```

Since `S_n` is local artinian, and `Z^i_n` flat hence essentially free over `S_n`, then, by VIII, 6.4, each `F^i_n` is
representable by a closed subprescheme `T^i_n` of `S_n`.

[^N.D.E-IX-17] The completion `Â` of the local ring `A` is noetherian since `A` is, and it is the projective limit of
the `A_n`. Denote by `K^i_n` the ideal of `A_n = A/m^{n+1}` defining `T^i_n` and `K^i` the projective limit of the
`K^i_n`; it is an ideal of `Â`.

For `i` fixed, `m ⩾ n` and every `S_n`-prescheme `P`, one has

```text
(Y^i_n)_P = Y_i ×_S S_n ×_{S_n} P = Y_i ×_S P = (Y^i_m)_P,
```

and likewise `(Z^i_n)_P = (Z^i_m)_P`; it follows that `F^i_n` is the restriction `F^i_m ×_{S_m} S_n` of `F^i_m` to
`(Sch)/S_n`, whence `T^i_n = T^i_m ×_{S_m} S_n`. One therefore has a commutative diagram with exact rows:

```text
0 → K^i_m → A_m → O(T^i_m) → 0
        ↓     ↓        ↓
0 → K^i_n → A_n → O(T^i_n) → 0
```

where all the vertical arrows are surjective. This has the following consequences: on the one hand, the projective
system `(K^i_n)_{n ∈ ℕ}` satisfies the Mittag-Leffler condition, hence the projective limit of the `O(T^i_n)` identifies
with the topological ring quotient `Â/K^i` (cf. EGA 0_III, § 13.2). On the other hand, the map `K^i → K^i_n` is
surjective (cf. [BEns], III, § 7.4, Prop. 5), whence it follows that `K^i_n ≃ (K^i + m^{n+1} Â)/m^{n+1} Â` and
`O(T^i_n) ≃ (Â/K^i) ⊗_A (A/m^{n+1})`.

In other words, `(T^i_n)_n` is an inductive system of affine artinian schemes, and the inductive limit
`T^i = lim_n T^i_n` is a closed formal subscheme of the formal scheme `Ŝ = Spf(Â)` (cf. EGA I, § 10), whose reduction
modulo `m^{n+1}` is `T^i_n`.

Let `T` be the closed formal subscheme of `Ŝ` intersection of the `T^i`, that is, defined by `K = ∑_i K^i`. Since `Â` is
noetherian, there exists a finite part `J` of `I` such that one has `K = ∑_{i ∈ J} K^i` (i.e. `T = ⋂_{i ∈ J} T^i`). Note
then that for every `n`, one has `K_n = ∑_{i ∈ J} K^i_n` where `K_n` denotes the image of `K` in `A_n`.

Recall that `f_i` denotes the image of `f ∈ B = O(X)` in `O(Z_i)`, and `f'_i` its image in `O(Z'_i) = O(Z_i) ⊗_A A′`;
the hypothesis `Y'_i = Z'_i` is equivalent to the vanishing of `f'_i`. Since `O(Z_i) ⊗_A A′` is the inductive limit of
the subalgebras `O(Z_i) ⊗_A A″` (where `A″` satisfies the conditions made explicit above), there exists therefore an
`A″` such that `Y″_i = Z″_i`. A priori, `A″` depends on `i`, but one can find an `A″` that works for all `i ∈ J`, since
`J` is finite. Set `S″ = Spec(A″)` and `S″_{(n)} = S″ ×_S S_n`.[^N.D.E-IX-18]

Since `Y″_i ×_{S″} S″_{(n)} = (Y^i_n)_{S″_{(n)}}` equals `Z″_i ×_{S″} S″_{(n)} = (Z^i_n)_{S″_{(n)}}` for every `i ∈ J`,
it follows from the definition of the `T^i_n` that `S″_{(n)} → S_n` factors through `T^i_n` for every `i ∈ J`, hence
also through `T_n = ⋂_{i ∈ J} T^i_n`, hence also through `T^i_n` for every `i ∈ I`. Denoting by `f″` the image of `f` in
`B″ = B ⊗_A A″`, and `f″_{(n)}` its image in `B″_{(n)} = B″/m^{n+1} B″`, this means that for every `n`, `f″_{(n)}`
vanishes on the `Z_i ×_S S″_{(n)}`.

Since the morphisms `A → A″ → A′` are local, the image `s″` of `s′` in `S″` is the closed point of `S″`, corresponding
to the maximal ideal `m″` of `B″`, and the image of `s″` in `S` is `s`. Fix `n` and denote now by `S″_n` the `n`-th
infinitesimal neighborhood of `s″` in `S″`, that is, `Spec(A″/m″^{n+1})`. Set `B″_n = B″/m″^{n+1} B″` and
`Z″_{n,i} = Z_i ×_S S″_n = Spec(B″_n)`. Then the image `f″_n` of `f″_{(n)}` in `B″_n` vanishes on `Z″_{n,i}`, for every
`i`. Now, by Lemma 4.5 below, the family of fibers

```text
Z_i''' = Z″_{n,i} ×_{S″_n} κ(s″) = Z_{i,s} ×_{κ(s)} κ(s″)
```

is schematically dense in the fiber `X_0''' = X″_n ×_{S″_n} κ(s″) = X_s ×_{κ(s)} κ(s″)`. Hence
`S″_n, X″_n, (Z″_{n,i})_{i ∈ I}`, and `S_0''' = Spec κ(s″)` satisfy the hypotheses of Lemma 4.2; it follows therefore
that `f″_n = 0`, i.e. `f″ ∈ m″^{n+1} B″`, for every `n`.

Since `B` is noetherian and `B″ = B ⊗_A A″` is a localization of a finite-type `B`-algebra, `B″` is noetherian, hence
its local rings are separated for their usual topology. It follows that `f″` is zero at the points `x″` of `X″` such
that `m″ B″` is contained in the maximal ideal of `O_{X″,x″}`, i.e. at the points of `X″` above `s″`. A fortiori, `f′`
is zero at the points `x′` of `X′` above `s′`. QED.

**Lemma 4.5.0.**[^N.D.E-IX-19] *Let `X` be an `S`-prescheme, `(Z_i)_{i ∈ I}` a family of subpreschemes of `X`, and
`S′ → S` a faithfully flat morphism. If the family `(Z'_i)_{i ∈ I}` is schematically dense in `X′`, then `(Z_i)_{i ∈ I}`
is schematically dense in `X`.*

<!-- label: III.IX.4.5.0 -->

This follows from EGA IV₃, 11.10.5 (i) and 11.9.10 (i). It remains to give the proof of:

**Lemma 4.5.** *Let `X` be a locally noetherian prescheme*[^N.D.E-IX-20] *over a field `k`, `(Z_i)_{i ∈ I}` a family of
subpreschemes of `X`, `k′` an extension of `k`, `X′` and `Z'_i` the preschemes deduced from `X` and `Z_i` by the base
change `k′/k`. For `(Z_i)_{i ∈ I}` to be schematically dense in `X`, it is necessary and sufficient that
`(Z'_i)_{i ∈ I}` be so in `X′`.*

<!-- label: III.IX.4.5 -->

The "if" follows from 4.5.0; let us prove the "only if".[^N.D.E-IX-21] First, one may suppose `X = Spec(B)` affine. For
every `i`, let `(Z_{ij})_{j ∈ J_i}` be a covering of `Z_i` by affine opens; replacing `(Z_i)_{i ∈ I}` by the family
`(Z_{ij})_{(i,j) ∈ J}`, where `J = ∐_{i ∈ I} J_i`, one may also suppose the `Z_i` affine.

Let `g ∈ B′ = B ⊗_k k′` and `t′ ∈ B'_g` be a section of `O_{X′}` on the affine open `U′ = X'_g`, vanishing on the
`Z'_i ∩ U′`, i.e. whose image in each `(O(Z_i) ⊗_k k′)_g` is zero. There exists a finite-type sub-`k`-algebra `A` of
`k′` such that `g ∈ B_A = B ⊗_k A` <!-- original page 55 --> and `t′ ∈ (B_A)_g`. The map `O(Z_i) ⊗_k A → O(Z_i) ⊗_k k′`
being injective, so is the map

```text
(O(Z_i) ⊗_k A)_g ⟶ (O(Z_i) ⊗_k k′)_g;
```

given the hypothesis, this implies that the image of `t′` in each `(O(Z_i) ⊗_k A)_g` is zero. This reduces us to showing
that the family `(Z_{iA})_{i ∈ I}` is schematically dense in `X_A`,[^N.D.E-IX-22] which follows from EGA IV₃, 11.9.10
b).

Let us note in passing the following result, which will serve in a later Exposé:[^N.D.E-IX-23]

**Corollary 4.6.** *Let `X` be a flat `S`-prescheme, `U` an open subset of `X`. Suppose that for every `s ∈ S`, `U_s` is
schematically dense in `X_s`, and that `X` is locally noetherian, or locally of finite presentation over `S`. Then `U`
is schematically dense in `X`.*

<!-- label: III.IX.4.6 -->

<!-- original page 56 -->

Suppose for simplicity `U` retrocompact in `X` (cf. EGA IV₃, 11.10.10 and 11.9.17 for the general case). The case `X`
locally noetherian is included only for memory; it is contained in 4.3.

In the second case envisaged, one may evidently suppose `S` and `X` affine; then `X` and `U` are of finite presentation
over `S = Spec(A)`. The ring `A` is the inductive limit of its finite-type sub-`ℤ`-algebras `A_i`. The "patented
procedure" already used (cf. EGA IV₃, 8.8.2 and 8.10.5 (iii)) shows that there exist an `i`, an affine scheme `X_i` over
`S_i = Spec(A_i)` and an open `U_i` in `X_i`, from which `X, U` are deduced by base change `S → S_i`. Let `E_i` be the
part of `S_i` consisting of `s ∈ S_i` such that `(U_i)_s` is schematically dense in `(X_i)_s`.

[^N.D.E-IX-24] By EGA IV₂, 5.9.9 and 5.10.2, `E_i` is the set of `s ∈ S_i` such that `(U_i)_s` contains the set
`Ass O(X_i)_s` of points "associated" with the structure sheaf of `(X_i)_s`, and by EGA IV₃, 11.9.17.1 this condition is
of constructible nature, i.e. `E_i` is a constructible part of `S_i`.

[^N.D.E-IX-24] By 4.5, the inverse image of `E_i` by `S_j → S_i` (resp. by `S → S_i`) is `E_j` (resp. the set `E` of
`s ∈ S` such that `U_s` is schematically dense in `X_s`). Moreover, by hypothesis, `E = S`, which is also the inverse
image by each `S → S_i` of `S_i`. By EGA IV₃, 8.3.11, this implies that there exists `j ⩾ i` such that `E_j = S_j`, i.e.
such that for every `s ∈ S_j`, `(U_j)_s` is schematically dense in `(X_j)_s`.

Then, by 4.4 applied to `(S_j, X_j, U_j)` and to the base change `S → S_j`, it follows that `U` is schematically dense
in `X`. One will note moreover that we use 4.4 here only in the case of a family with finite index set (in fact, reduced
to one element), in which case the proof of 4.4 simplifies considerably, as the reader will check.

**Theorem 4.7.** *Let `S` be a prescheme, `G` a group of multiplicative type and of finite type over `S`. For every
integer `n > 0`, let `_nG` be the kernel of `n · id_G`. Then the family of subpreschemes `(_nG)_{n > 0}` of `G` is
schematically dense (Def. 4.1).*

<!-- label: III.IX.4.7 -->

We distinguish two cases.

a) Case `S` locally noetherian. Then by 4.3 one is reduced to the case where `S` is the spectrum of a field `k`. By
4.5.0, one may suppose `k` algebraically closed and `G` diagonalizable, i.e. of the form `D_k(M)`, where `M` is a
commutative group of finite type. Then `M` is of the form `Γ × ℤ^r`, with `Γ` finite, hence `G` is of the form
`G_1 × G_2`, <!-- original page 57 --> with `G_1 = D(Γ)` and `G_2 = G_m^r`; and for `n` large multiplicatively (namely
`n` a multiple of the order of `Γ`) one will have `_nG = G_1 × _nG_2` since one will have `_nG_1 = G_1`.

Applying again 4.3 to the projection `G → G_1`, one is reduced to the case of `G_2`, i.e. to the case where `G = G_m^r`.
Since `G` is then reduced, it amounts to the same to say that `(_nG)_{n > 0}` is schematically dense in `G`, or that the
union of the `_nG` is dense in `G` for the ordinary topology. Since `_nG = (_nG_m)^r`, one is reduced to the case of
`G = G_m`, hence `G` irreducible of dimension `1`. Then this follows from the fact that the union of the `_nG` (equal to
the set of roots of unity in `k`) is infinite.

b) General case. For every point `s` of `S`, there exist an open neighborhood `U` of `s` and a faithfully flat
quasi-compact morphism `S′ → U` such that `G′ = G_{S′}` is diagonalizable, i.e. of the form `D_{S′}(M)`. By 4.5.0 again,
one may reduce to the case of `G′`, so one may suppose `G` diagonalizable; hence it comes from the absolute group
`H = D_ℤ(M)` over `Spec(ℤ)` by base change `S → Spec(ℤ)`. By the proof of a), for every `s ∈ Spec(ℤ)`, the family
`(_nH_s)_{n > 0}` is schematically dense in `H`; it now suffices to apply 4.4.[^N.D.E-IX-25]

**Corollary 4.8.** *a) Let `u, v : H → G` be two homomorphisms of `S`-preschemes in groups, with `H` of multiplicative
type and*[^N.D.E-IX-26] *of finite type, and suppose that for every integer `n > 0`, the restrictions of `u` and `v` to
`_nH` are identical. Then `u = v`.*

<!-- label: III.IX.4.8 -->

*b) Let `H_1, H_2` be two subgroups of multiplicative type and of finite type of a prescheme in groups `G`, and suppose
that for every integer `n > 0`, one has `_nH_1 = _nH_2`; then `H_1 = H_2`.*

The first assertion follows from the second, by consideration of the subgroups `H_1` and `H_2` of `H × G`, graphs of `u`
and `v`. To prove b), let `H = H_1 ∩ H_2`; this is a subprescheme in groups of `H_i` (`i = 1, 2`); one must show that it
is identical to `H_i`. Now the hypothesis means that it majorizes the `_nH_i`. One is therefore reduced to proving the:

**Corollary 4.9.** *Let `G` be an `S`-group of multiplicative type and of finite type, and `H` a subprescheme in groups
which majorizes the `_nG`, `n > 0`. Then `H = G`.*

<!-- label: III.IX.4.9 -->

By 4.7, one is reduced to proving that the subprescheme `H` is closed, or again that it equals `G` set-theoretically.
This reduces us to the case where `S` is the spectrum <!-- original page 58 --> of a field; but then every subprescheme
in groups of `G` is closed (VI_B 1.4.2), whence the conclusion.

**Remark 4.10.** *Under the conditions of 4.7, let `m` be an integer `> 0` having the following properties: for every
`s ∈ S`, `m` is not a power of the characteristic of `κ(s)`, and if `G_s` is of type `M`, the prime divisors of the
torsion of `M` divide `m`. (N.B. This second condition is always satisfied if `G` is a torus.) Then the proof given
shows that in the statement of 4.7 and the Corollaries 4.8 and 4.9, one may restrict attention to subgroups of the form
`_{(m^r)}G`, with `r > 0`.*

<!-- label: III.IX.4.10 -->

Moreover, one sees at once that when `G` is smooth over `S`, then for every point `s ∈ S`, there exist an open
neighborhood `U` of `s` and an integer `m > 0`, prime to all the residual characteristics of `U`, satisfying the
preceding conditions for `G_U`. (Take for example for `m` the order of the torsion of the type of `G` at `s`, cf. 1.4.1
a) and 2.1 e).) Under these conditions, one finds `_{(m^r)}G` that are finite and étale over `S`, and whose family is
schematically dense, provided one restricts to over `U`. This remark allows, in certain cases (notably those involving
the theorems 3.2 and 3.2 bis, cf. XI 6, but not those involving the theorems 3.6 and 3.6 bis), to dispense with the
theorem 3.1, which involves Hochschild cohomology.

## 5. Central homomorphisms of groups of multiplicative type

**Lemma 5.0.**[^N.D.E-IX-27] *Let `(A, m)` be a noetherian local ring, `S = Spec(A)`, and `H` a finite scheme over `S`,
so `H = Spec(B)`, where `B` is finite over `A`. Let `K` be a subscheme of `H`, such that by reduction modulo `m^{n+1}`
one has `K_n = H_n` for every `n`. Then `K = H`.*

<!-- label: III.IX.5.0 -->

Let `s` be the closed point of `S`. Note first that `K` is a closed subscheme of `H`. Indeed, it is a priori a closed
subscheme of an open `U` of `H`. But `K`, hence `U`, contains the fiber `K_s = H_s`; since the morphism `H → S` is
finite, hence closed, it follows that the complement of `U` is empty, i.e. `U = H`. Hence `K` is defined by an ideal `I`
of `B`. The hypothesis entails that `I` is contained in `m^n B` for every `n`; since `B` is a finite `A`-module, it is
separated for the `m`-adic topology, whence `I = 0`.

**Theorem 5.1.** *Let `u, v : H → G` be two homomorphisms of `S`-preschemes in groups, with `H` of multiplicative type
and of finite type, and `S` locally noetherian or `G` of finite presentation over `S`. Let `s ∈ S` be such that
`u_s = v_s`, and suppose `u_s` central. Then there exists an open neighborhood `U` of `s` such that `u_U = v_U`.*

<!-- label: III.IX.5.1 -->

<!-- original page 59 -->

We distinguish the two cases:

a) `S` locally noetherian.[^N.D.E-IX-28] Let `K = Ker(u, v)` be the inverse image of the diagonal of `G ×_S G` by the
morphism `(u, v)`; this is a subprescheme in groups of `H`. We wish to find `U` such that `K_U = H_U`. Note that, since
`S` is locally noetherian and `H` of finite type over `S`, `H` is locally noetherian, hence the immersion `K ↪ H` is of
finite type (cf. EGA I, 6.3.5). Hence `K` is of finite type over `S`, hence of finite presentation over `S`, since `S`
is locally noetherian. Consequently, by EGA IV₃, 8.8.2.4, to show that there exists an open neighborhood `U` of `s` such
that `K_U = H_U`, it suffices to show that `K_{S_0} = H_{S_0}`, where `S_0` is the spectrum of `A = O_{S,s}`. One may
therefore suppose `S` local with closed point `s`. Replacing the noetherian local ring `A` by its completion `Â` if
necessary, which introduces a base change `Ŝ → S` faithfully flat and quasi-compact, one may even, if one wishes,
suppose[^N.D.E-IX-29] `A` complete.

By 3.4 one has `u_n = v_n` for every `n`, where as usual the index `n` indicates reduction modulo `m^{n+1}` (`m` being
the maximal ideal of `A`). For every integer `m > 0`, denoting by `_mu, _mv` the homomorphisms `_mH → G` induced by
`u, v`, one therefore also has `(_mu)_n = (_mv)_n`. This being true for every `n`, and `_mH` being finite over `S` by
2.2, it follows that `_mu = _mv` by 5.0. This being true for every `m`, one has therefore `u = v` by 4.7.

b) `G` of finite presentation.[^N.D.E-IX-30] Since `H` is also of finite presentation over `S`, then, by EGA IV₃, 8.8.2,
we may again suppose `S` local with closed point `s` and prove that then `u = v`. If `f : S′ → S` is a faithfully flat
quasi-compact morphism, and if one denotes by `f_H` the morphism `H′ → H` and `u′, v′ : H′ → G′` the morphisms deduced
from `u, v`, then the equality `u′ = v′` entails `u′ ∘ f_H = v′ ∘ f_H`, hence `u = v`, since `f_H` is an epimorphism.
Hence, by making a faithfully flat quasi-compact extension of the base, one may suppose moreover `H` diagonalizable,
hence of the form `D_S(M)`, with `M` a commutative group of finite type.

Introduce, as in the proof of 4.6, the increasing filtered family of finite-type sub-`ℤ`-algebras `A_i` of
`A = O_{S,s}`, and `S_i = Spec(A_i)`.[^N.D.E-IX-30] Note that `H = D_S(M)` comes, for every `i`, from the diagonalizable
group `H_i = D_{S_i}(M)`. Since `G` is of finite presentation over `S`, then, by EGA IV₃, 8.8.2 (see also VI_B, 10.2 and
10.3), there exist an index `i`, a prescheme in groups `G_i` of finite presentation over `S_i`, and morphisms of
`S_i`-groups `u_i, v_i : H_i → G_i` from which `u, v` come by base change. Let `s_i` be the image of `s` in `S_i` and
let `ρ_i : H_i ×_{S_i} G_i → G_i` be the morphism of `S_i`-preschemes defined by `ρ_i(h, g) = u_i(h) g u_i(h)^{-1}`.
Then, since `u_s` is central, `ρ_s = ρ_i ×_{κ(s_i)} κ(s)` equals the second projection; so the same holds for `ρ_i`
(since `κ(s_i) → κ(s)` is faithfully flat and quasi-compact), i.e. `(u_i)_{s_i}` is central. Similarly, since
`u_s = v_s` one has `(u_i)_{s_i} = (v_i)_{s_i}`. One can then apply a) to the situation over `S_i`, whence the announced
conclusion.

**Corollary 5.2.** *Let `u : H → G` be a homomorphism of `S`-preschemes in groups, with `H` of multiplicative type and
of finite type, and `S` locally noetherian or `G` of finite presentation over `S`. Let `s ∈ S` and suppose that `u_s` is
the unit homomorphism. Then there exists an open neighborhood `U` of `s` such that `u_U` is the unit homomorphism.*

<!-- label: III.IX.5.2 -->

**Corollary 5.3.** *Let `u, H, G` be as in 5.2, suppose moreover `G` separated over `S`.* <!-- original page 60 --> *Let
`U` be the set of `s ∈ S` such that `u_s` is the unit homomorphism. Then `U` is an open-and-closed part of `S`, and
`u_U : H_U → G_U` is the unit homomorphism.*

<!-- label: III.IX.5.3 -->

It remains only to prove that `U` is closed. Now let `K = Ker(u)`; since `G` is separated over `S`, `K` is a closed
subprescheme of `H`, and `U` is the set of `s ∈ S` such that `K_s = H_s`. One then sees easily that `U` is closed, for
example as an application of VIII 6.4 (`H` being essentially free over `S` by VIII 6.3), or by noting that one may
suppose `S` reduced and `U` dense in `S`, hence schematically dense in `S`, which implies `H_U` schematically dense in
`H` since `H` is flat over `S`,[^N.D.E-IX-31] and since `u` and the unit homomorphism coincide on `H_U`, they coincide
on `H`.

**Corollary 5.4.** *Let `S` be a prescheme, `H` and `G` two `S`-groups, with `H` of multiplicative type and of finite
type and `G` separated and of finite presentation over `S`, `π : S′ → S` a*[^N.D.E-IX-32] *universal effective
epimorphism (for example, a faithfully flat quasi-compact morphism, or a morphism admitting a section, cf. IV 1.12) with
geometrically connected fibers.*[^N.D.E-IX-33]

<!-- label: III.IX.5.4 -->

*Let `u′ : H′ → G′` be a central homomorphism of the `S′`-groups deduced from `H, G` by the base change `S′ → S`. Then
there exists a unique homomorphism `u : H → G` of `S`-groups such that `u ×_S S′ = u′`. When `S′/S` admits a section
`g`, then `u` is the morphism deduced from `u′` by the base change `g : S → S′`.*

Since `π` is a universal effective epimorphism, so is `H′ → H`, whence the uniqueness of `u`, cf. the beginning of the
proof of 5.1 b). If `π` admits a section `g`, then `u′ = π^*(u)` entails `u = g^* π^*(u) = g^*(u′)`.

For the existence of `u`, one is reduced, by IV 2.3, to showing that the two homomorphisms `u″_1, u″_2 : H″ → G″` of
`S″`-groups deduced from `u′` by the two base changes `pr_1, pr_2 : S″ = S′ ×_S S′ → S′`, are identical. Now they
coincide on the diagonal of `S″`; more precisely the inverse images of `u″_1` and `u″_2` by the diagonal morphism
`S′ → S″` are identical (since both equal `u′`).[^N.D.E-IX-34] Since `u″_1` and `u″_2` are central, one may apply 5.3 to
the morphism `u″_1 (u″_2)^{-1}`. There exists therefore an open-and-closed part `U` of `S″`, <!-- original page 61 -->
containing the diagonal of `S″`, such that `u″_1` and `u″_2` coincide above `U`.

Now the fibers of `S′/S` being geometrically connected, the same holds for those of `S″/S`, which are therefore a
fortiori connected; whence it follows that `U` (containing the diagonals of the said fibers) contains the said fibers,
hence is equal to `S″`, which completes the proof.

**Corollary 5.5.** *Let `S` be a prescheme, `K` an `S`-prescheme in groups locally of finite type*[^N.D.E-IX-35] *and
with connected fibers, `H` a subgroup of multiplicative type and of finite type, invariant in `K`. Then `H` is a central
subgroup of `K`.*

<!-- label: III.IX.5.5 -->

[^N.D.E-IX-36] Note first that `π : K → S` has geometrically connected fibers, since for a group scheme locally of
finite type over a field, connected implies geometrically connected (cf. VI_A 2.4). One can then apply 5.4 by taking
`G = H` and `S′ = K`, to the homomorphism of `K`-groups `u′ : H_K → H_K` defined set-theoretically by
`(h, k) ↦ (k h k^{-1}, k)`, which is central since `H` is commutative. The inverse image of `u′` by the unit section
`ε : S → K` is the identity homomorphism of `K`, hence by 5.4 the same holds for `H_K → H_K`; hence `H` is central in
`K`.

Let us state the variants of the preceding results for central subgroups of multiplicative type. One obtains, by
proceeding as for the preceding results (and using 3.2 bis):

**Theorem 5.1 bis.** *Let `G` be an `S`-prescheme in groups, `H_1` and `H_2` two subpreschemes in groups of
multiplicative type and of finite type, with `(H_1)_s` central. Suppose `S` locally noetherian or `G` of finite
presentation over `S`. Then for every `s ∈ S` such that `(H_1)_s = (H_2)_s`, there exists an open neighborhood `U` of
`s` such that `H_1|U = H_2|U`.*

<!-- label: III.IX.5.1bis -->

**Corollary 5.3 bis.** *Under the preceding conditions, suppose moreover `G` separated over `S`. Let `U` be the set of
`s ∈ S` such that `(H_1)_s = (H_2)_s`. Then `U` is an open-and-closed part of `S`, and `H_1|U = H_2|U`.*

<!-- label: III.IX.5.3bis -->

**Corollary 5.4 bis.** *Let `S` be a prescheme, `G` a prescheme in groups separated and of finite presentation over
`S`,* <!-- original page 62 --> *`S′ → S` a covering morphism for the faithfully flat quasi-compact topology, with
geometrically connected fibers, `H′` a subgroup of multiplicative type and of finite type of `G′ = G ×_S S′`.*

<!-- label: III.IX.5.4bis -->

*Then there exists a unique subgroup `H` of `G` such that `H′ = H ×_S S′`, and `H` is of multiplicative type and of
finite type over `S`, by 1.1 and 2.1 b). If `S′ → S` admits a section `g`, then `H` is the inverse image of the subgroup
`H′` of `G′` by `g : S → S′`.*

**Theorem 5.6.** *Let `S` be a prescheme, `u : H → G` a homomorphism of `S`-preschemes in groups, with `H` of
multiplicative type and of finite type, `G` of finite presentation over `S`.*

<!-- label: III.IX.5.6 -->

*a) Suppose `G` has connected fibers, and let `s ∈ S` be such that `u_s : H_s → G_s` is a central homomorphism. Then
there exists an open neighborhood `U` of `s` such that the homomorphism `H|U → G|U` induced by `u` is central.*

*b) Suppose that for every `s ∈ S`, `u_s : H_s → G_s` is central. Then `u` is central.*

[^N.D.E-IX-37] Let us prove (a). Proceeding exactly as in the proof of 5.1 (b), one may suppose `S` local with closed
point `s`, then `H = D_S(M)` diagonalizable, then that there exist a finite-type sub-`ℤ`-algebra `A_i` of `A = O_{S,s}`
and a morphism `u_i : D_{S_i}(M) → G_i` such that `u_{s_i}` is central (where `s_i` is the image of `s` in `S_i`) and
from which `u` comes by base change. This reduces us to the case where `S` is local noetherian with closed point `s`,
and one must then prove that `u` is central.

Let `K` be the subprescheme `Ker(v, w)`, where `v, w : H ×_S G ⇒ G` are defined by

```text
v(h, g) = g,      w(h, g) = int(u(h)) · g = u(h) g u(h)^{-1}.
```

Then `K` is a sub-`G`-group of the `G`-group `H_G = H ×_S G`; we wish to show that it is equal to `H_G` itself. By 4.9,
one is reduced to proving that it majorizes the `_m(H_G) = (_mH) ×_S G` for every integer `m > 0`, which reduces us to
the case where `H = _mH`, hence `H` finite over `S`.

Let `e` be the unit element of the fiber `G_s`; then `S^0 = Spec(O_{G,e})` is a local noetherian scheme (`G` being of
finite presentation over `S` noetherian); set `S^0_n = S^0 ×_S S_n`, where `S_n = Spec(A/m^{n+1})`. Then
`K_{S^0} = K ×_G S^0` is a subprescheme of `H_{S^0} = H ×_S S^0`, and, <!-- original page 63 --> by 3.9, one has
`K_{S^0_n} = H_{S^0_n}` for every `n`.[^N.D.E-IX-38] Since `H_{S^0}` is finite over `S^0`, one concludes from 5.0
(applied to the noetherian local ring `B`) that `K_{S^0} = H_{S^0}`.

On the other hand, since `H ×_S G` is noetherian (being of finite presentation over `S` noetherian), the immersion
`K ↪ H ×_S G` is of finite type (cf. EGA I, 6.3.5), so that `K` is of finite type, hence of finite presentation over
`G`. Then the equality `K_{S^0} = H_G ×_G S^0` entails, by EGA IV₃, 8.8.2.4, that there exists an open neighborhood `W`
of `e` in `G` such that `K ×_G W = H_G ×_G W = H ×_S W`. Hence `K` majorizes the open neighborhood `V = H ×_S W` of the
unit section of `G_H` over `H`.

For every `t ∈ H`, the fiber `G_t` (being a `κ(t)`-algebraic group) is Cohen–Macaulay (VI_A, 1.1.1), hence without
embedded components; as it is moreover connected, hence irreducible (VI_A, 2.4), it has its generic point as unique
associated point. Hence, by EGA IV₂, 3.1.8, the open `V_t` is schematically dense in `G_t`. By 4.3, `V` is therefore
schematically dense in `G_H`. Moreover, since `K` is a sub-`H`-group of `G_H`, it induces on each fiber `G_h` a subgroup
`K_h`, and since the latter majorizes an open neighborhood of the unit element and `G_h` is connected, it follows that
`K_h = G_h`, hence `K = G_H` set-theoretically. Thus `K` is a closed subprescheme of `G_H` which majorizes the
schematically dense subprescheme `V`, hence `K = G_H`, which proves a).

Finally, b) is a direct consequence of 3.9, given that to verify that a subprescheme `K` of `P = G ×_S H` is identical
to `P`, it suffices to verify that for every base change `S′ → S`, where `S′` is an artinian quotient of a local ring of
`S`, one has `K′ = P′`.

## 6. Monomorphisms of groups of multiplicative type, and canonical factorization of a homomorphism of such a group

**Lemma 6.1.** *Let `S` be a quasi-compact prescheme, `G` an `S`-prescheme in commutative groups, of finite presentation
and quasi-finite over `S`. Then there exists an integer `n > 0` such that `n · id_G = 0`, i.e. `G = _nG`.*

<!-- label: III.IX.6.1 -->

<!-- original page 64 -->

If `S` is the spectrum of a field `k`, then `G` is finite over `k`, and by VII_A 8.5, it suffices to take
`n = deg(G/k)`. Suppose now `S = Spec(A)` local artinian; let `k` be the residue field of `A`, `G_0 = G ⊗_A k`, and
`n_0 = deg(G_0/k)`. Distinguish two cases.

a) `k` is of characteristic zero. Then `G_0` is separable over `k`, hence `G` is unramified over `S`. Then the unit
section of `G` is an open immersion, hence `_nG = Ker(n · id_G)` is an open subscheme of `G`; therefore in order that it
be equal to `G`, it suffices that it be so set-theoretically; one may then take `n = n_0`.

b) `k` is of characteristic `p > 0`. Denote by `m` the maximal ideal of `A` and `S_r = Spec(A/m^{r+1})` for every `r`.
Let `m` be an integer such that `m^{m+1} = 0`; we claim that one may take `n = p^m n_0`. Indeed, proceeding by induction
on `m`, and setting `n′ = p^{m-1} n_0`, one may suppose that `n′ · id_G` induces the zero endomorphism in
`G_{m-1} = G ×_S S_{m-1}`.

[^N.D.E-IX-39] Denote by `E` the set of endomorphisms `u` of `G` having this property and `K` the kernel of the morphism
of functors in groups `G → ∏_{S_{m-1}/S} G` (cf. III 0.1.2). Then `E` identifies with `Hom_{S-gr.}(G, K)`; in particular
the abelian group law on `E` is induced by that of `K`. Now, by III 0.9, `K` is the `S`-functor in groups which to every
`g : T → S` associates the `k`-vector space

```text
Hom_{O_{T_0}}(g_0^*(Ω^1_{G_0/S_0}), m^m O_T);
```

one has therefore `pu = 0` for every `u ∈ E`. Hence one has `pn′ · id_G = 0`, i.e. `p^m n_0 · id_G = 0`.

Suppose now `S` noetherian (one reduces to this in 6.1 by the customary reduction to the noetherian case[^N.D.E-IX-40]).
It then suffices to combine the foregoing with the

**Lemma 6.2.** *Let `X` be a quasi-finite prescheme over `S` noetherian, and consider an increasing filtered family of
subpreschemes `(X_i)_{i ∈ I}` having the following property:*

<!-- label: III.IX.6.2 -->

```text
for every s ∈ S and n ⩾ 0, setting S_{s,n} = Spec(O_{S,s}/m^{n+1}), there exists an i ∈ I
such that X_i ×_S S_{s,n} = X ×_S S_{s,n}.
```

*Under these conditions, there exists an `i ∈ I` such that `X_i = X`.*

Since `S` is noetherian, there exists a maximal open `U` such that one has `X|U = X_i|U` <!-- original page 65 --> for
`i` large; we shall show that `U = S`. In other words, we shall show that if `U ≠ S`, one can find a `U_1` strictly
larger than `U`, and an `i` such that `X|U_1 = X_i|U_1`. Localizing at a maximal point `s` of `S − U`, one is reduced to
the case where `S` is local with closed point `s`, and `U = S − {s}`. (Indeed, if one writes `S^0 = Spec(O_{S,s})` and
if there exists `i` such that `X ×_S S^0 = X_i ×_S S^0` then,[^N.D.E-IX-41] there exists an open neighborhood `V` of `s`
such that `X|V = X_i|V`; hence taking `i` large enough so that `X_i|U = X|U`, one will have `X|W = X_i|W`, where
`W = U ∪ V.`)

Then, for `i` large, since `X|U = X_i|U`, one sees that `X_i` is a closed subprescheme of `X` defined by an ideal
`I^{(i)}` of support contained in `X_s = X_0 = X ×_S S_0` (where `S_n = Spec(A/m^{n+1})`, `S = Spec(A)`). Since `X_0` is
quasi-finite over `S_0`, `X_0` is a finite closed part of `X` noetherian, hence `I^{(i)}` is a module of finite length.
It follows that there exists an integer `n ⩾ 0` such that `I^{(i)} ∩ m^{n+1} O_X = 0`. On the other hand, by the
hypothesis in 6.2, one may suppose (by enlarging `i` if necessary) that the image of `I^{(i)}` in
`O_{X_n} = O_X/m^{n+1} O_X` is zero. This implies `I^{(i)} = 0`, hence `X_i = X`. QED.

**Lemma 6.3.** *Let `S` be a prescheme, `K` a prescheme in groups over `S`, locally of finite presentation, `s ∈ S` such
that `K_s` is quasi-finite (resp. unramified) over `κ(s)` at the unit element. Then there exists an open neighborhood
`U` of `s` such that `K|U` is locally quasi-finite (resp. unramified) over `U`.*[^IX-6-1]

<!-- label: III.IX.6.3 -->

Let `V` be the set of points `x` of `K` such that, denoting by `t` the image of `x` in `S`, the fiber `K_t` is
quasi-finite (resp. unramified) over `κ(t)` at `x`, i.e. such that `x` is isolated in `K_t` (resp. and its local ring in
`K_t` is a separable extension of `κ(t)`). One knows that `V` is open since `K` is locally of finite presentation over
`S`,[^N.D.E-IX-42] hence if `ε` denotes the unit section of `K`, `ε^{-1}(V)` is open. By hypothesis it contains `s`,
hence is an open neighborhood `U` of `s`. The latter does the trick; in other words, `t ∈ U` implies that `K_t` is
locally quasi-finite (resp. unramified) over `κ(t)`: indeed, <!-- original page 66 --> since `K_t` is a group locally of
finite type over `κ(t)`, this follows from the fact that it is quasi-finite (resp. unramified) over `κ(t)` at the point
`ε(t)`, cf. VI_B 1.3.

Combining 6.1 and 6.3, one finds the

**Theorem 6.4.** *Let `S` be a prescheme, `H` an `S`-group of multiplicative type and of finite type, `K` a closed
subprescheme in groups, of finite presentation over `S`. Let `s ∈ S` be such that `K_s` is finite.*

<!-- label: III.IX.6.4 -->

*Then there exists an open neighborhood `U` of `s` such that `K|U` is contained in `_nH|U` for some `n`, and a fortiori
(`_nH` being finite over `S`) such that `K|U` is finite over `U`.*

Using Nakayama's lemma, one deduces:

**Corollary 6.5.** *With the preceding notation, suppose that `K_s` is the unit group. Then there exists an open
neighborhood `U` of `s` such that `K|U` is the unit group.*

<!-- label: III.IX.6.5 -->

**Corollary 6.6.** *Let `u : H → G` be a homomorphism of `S`-preschemes in groups, with `H` of multiplicative type and
of finite type, and `G` separated over `S`. Suppose moreover `S` locally noetherian, or `G` locally of finite
presentation*[^N.D.E-IX-43] *over `S`.*

<!-- label: III.IX.6.6 -->

*Let `s ∈ S` be such that `u_s : H_s → G_s` is a monomorphism; then there exists an open neighborhood `U` of `s` such
that `u` induces a monomorphism `H|U → G|U`.*

Indeed, let `K = Ker(u)`; the hypothesis on `u_s` means that `K_s` is the unit group, the conclusion that `K|U` is the
unit group, for a suitable `U`. Now `G` being separated over `S`, `K` is a closed subgroup of `H`; and in the case where
one does not suppose `S` locally noetherian but rather `G` locally of finite presentation over `S`, `K` is locally of
finite presentation over `S`,[^N.D.E-IX-43] hence of finite presentation over `S` since it is separated over `S` (`H`
being so) and quasi-compact over `S` (being closed in `H` which is quasi-compact over `S`). One may therefore apply 6.5,
whence 6.6.

**Remark 6.6.1.**[^N.D.E-IX-44] *Under the hypotheses of 6.6, one will note that when moreover `G` is affine over `S`
(resp. of finite presentation over `S`), `H|U → G|U` is even a closed immersion, as was pointed out in 2.5 (resp. 2.6).*

<!-- label: III.IX.6.6.1 -->

**Corollary 6.7.** *Let `u : H → G` be a homomorphism of `S`-preschemes in groups,* <!-- original page 67 --> *with `H`
of multiplicative type and of finite type; suppose `S` locally noetherian or `G` locally of finite presentation over
`S`.*

<!-- label: III.IX.6.7 -->

*If all the homomorphisms induced on the fibers `u_s : H_s → G_s` are monomorphisms, then `u` is a monomorphism.*

The reasoning is the same as in 6.6; the hypothesis that `G` be separated over `S` is here unnecessary to ensure that
`K` is closed in `H`, since the hypothesis that the `u_s` be monomorphisms implies that `K` reduces set-theoretically to
the unit section of `G`.

**Theorem 6.8.** *Let `u : H → G` be a homomorphism of `S`-preschemes in groups, with `H` of multiplicative type and of
finite type, and `G` separated over `S`. Suppose moreover `S` locally noetherian or `G` of finite presentation over
`S`.*

<!-- label: III.IX.6.8 -->

*Then `K = Ker(u)` is a subgroup of multiplicative type and of finite type of `H`, and `u` factors as*

```text
H ─u'→ H/K ─u''→ G,
```

*where `H/K` is of multiplicative type and of finite type, `u'` is the canonical homomorphism and is faithfully flat
(and affine), and `u''` is a monomorphism.*

(N.B. As remarked in 6.6.1, `u''` is a closed immersion if `G` is affine over `S` or of finite presentation over `S`.)
It suffices to prove that `K` is of multiplicative type, the rest of the proposition then following from 2.7 and IV
5.2.6.

Suppose first `G` of finite presentation over `S`. This hypothesis being stable under base change, one is reduced, to
prove that `K` is of multiplicative type, to the case where `H` is diagonalizable, i.e. `H = D_S(M)`, where `M` is a
commutative group of finite type. Let `s ∈ S`; then `K_s` is a closed subgroup of `H_s = D_{κ(s)}(M)`, hence

<!-- original page 68 --> by 8.1[^N.D.E-IX-45] is of the form `D_{κ(s)}(N)`, where `N` is a quotient group of `M`. Set

`K′ = D_S(N)`; then `K′` is a subgroup of multiplicative type of `H`. Let `v′ : K′ → G` be induced by `u`.[^N.D.E-IX-46]
Then `v′_s` is the unit homomorphism by construction, hence by 5.2 there exists an open neighborhood `U` of `s` such
that `v′|U : K′|U → G|U` is the unit homomorphism. Hence, replacing `S` by `U` if necessary, one may suppose that `v′`
is the unit homomorphism, hence that `u` factors as

```text
H ─u'→ H/K′ ─u''→ G.
```

Now, since `u''_s` is deduced from `u_s` by factoring through `H_s → H_s/Ker(u_s)`, then `u''_s` is a monomorphism (IV
5.2.6), hence by 6.6 there exists an open neighborhood `U` of `s` such that `u''|U : (H/K′)|U → G|U` is a monomorphism.
Hence, restricting `S` if necessary, one sees that `u''` is a monomorphism, hence `Ker(u) = Ker(u') = K′`, which proves
that `Ker u` is of multiplicative type.

The same proof is valid if, instead of supposing `G` of finite presentation over `S`, one supposes `S` locally
noetherian — at least in the case where `H` is diagonalizable. In the case where one does not make this hypothesis on
`H`, one must show that one can find a covering base change `S′ → S`, with `S′` locally noetherian, that trivializes
`H`. This will indeed be seen in the following Exposé (X 4.6).

## 7. Algebraicity of formal homomorphisms into an affine group

**Theorem 7.1.** *Let `A` be a noetherian ring equipped with an ideal `I` such that `A` is separated and complete for
the `I`-adic topology, `S = Spec(A)`, `S_n = Spec(A/I^{n+1})`, `H, G` `S`-preschemes in groups, with `H` of isotrivial
multiplicative type, and `G` affine.*

<!-- label: III.IX.7.1 -->

*Then the canonical map*

```text
(*)    θ : Hom_{S-gr.}(H, G) ⟶ lim_n Hom_{S_n-gr.}(H_n, G_n)
```

<!-- label: eq:III.IX.7.1-star -->

*is bijective (where `H_n, G_n` are the `S_n`-groups deduced from `H, G` by the base change `S_n → S`).*

<!-- original page 69 -->

Suppose first `H` diagonalizable, hence of the form

```text
H = Spec A^{(M)},
```

where `B = A^{(M)}` is the algebra of the commutative group `M` with coefficients in `A`. One also has `G = Spec(C)`,
where `C` is an `A`-algebra equipped with a diagonal map (satisfying the well-known axioms). Then the homomorphisms of
`S`-groups `H → G` correspond bijectively to the homomorphisms of `A`-algebras `ϕ : C → B` compatible with the diagonal
maps, i.e. such that, for every `f ∈ C`,

```text
Δ_H(ϕ(f)) = (ϕ ⊗ ϕ)(Δ_G(f))
```

where `Δ_H` and `Δ_G` are the diagonal maps. One has an analogous description for the homomorphisms of `S_n`-groups
`H_n → G_n`, defined by certain homomorphisms of `A_n`-algebras `ϕ_n : C_n → B_n` (where one sets `A_n = A/I^{n+1}`,
`B_n = B ⊗_A A_n`, `C_n = C ⊗_A A_n`). Set

```text
B̂ = lim_n B_n    and    Ĉ = lim_n C_n;
```

then `B̂ = lim_n A_n^{(M)}` identifies with a submodule of the product `A^M` (namely, that formed by the families
`(a_m)_{m ∈ M}` of elements of `A` which tend to `0` (for the `I`-adic topology) along the filter of complements of
finite parts of `M`). This already implies that the canonical homomorphism `B → B̂` is injective,[^N.D.E-IX-47] since
the projective system `θ(ϕ) = (ϕ_n)_{n ⩾ 0}` defines a homomorphism `ϕ̂ : Ĉ → B̂` such that the diagram below is
commutative:

```text
C ─ϕ→ B
↓     ↓
Ĉ ─ϕ̂→ B̂.
```

Let us prove that `θ` is surjective: take a projective system `(ϕ_n)_{n ⩾ 0}` and let us prove that it comes by
reduction from a `ϕ` of the first member. A priori, `(ϕ_n)` defines a homomorphism on the completed algebras

```text
ϕ̂ : Ĉ ⟶ B̂,
```

and all that remains is to see that its composite `Φ : C → Ĉ →^{ϕ̂} B̂` with the canonical homomorphism `C → Ĉ` sends
`C` into `B`. Indeed, if this is the case, one finds a homomorphism <!-- original page 70 --> of `A`-algebras
`ϕ : C → B`, reducing along the `ϕ_n`, from which one concludes at once that it is compatible with the diagonal maps
(since the `ϕ_n` are, and `B ⊗_A B → B̂ ⊗̂_A B` is injective, as one sees, as above, by replacing `M` by `M × M`).

Note that the diagonal homomorphism `Δ_H` of `H` defines, on passing to the completions, a homomorphism

```text
Δ̂_H : B̂ ⟶ B̂ ⊗̂_A B,
```

and one has a commutative diagram (deduced by passage to the projective limit from the analogous diagrams defined by the
`ϕ_n`):

```text
       Φ
C ────────→ B̂
↓Δ_G         ↓Δ̂_H
C ⊗_A C ─Ψ→ B̂ ⊗̂_A B,
```

where `Ψ` is the composite

```text
C ⊗_A C ─Φ⊗Φ→ B̂ ⊗_A B̂ ⟶ B̂ ⊗̂_A B
```

(the last arrow being the obvious canonical homomorphism). It follows that for every `f ∈ C`, `Φ(f)` is an element of
`B̂` whose image under `Δ̂_H` is a "decomposable" element of `B̂ ⊗̂_A B`, i.e. is in the image of `B̂ ⊗_A B̂`.

Denote by `(e_m)_{m ∈ M}` the canonical basis of `A^{(M)}` and `(e_{m,m'})` that of `A^{(M × M)} = A^{(M)} ⊗_A A^{(M)}`.
Since `Δ_H(e_m) = e_m ⊗ e_m = e_{m,m}` for every `m`, it suffices now to apply the

**Lemma 7.2.** *Let `A` be a noetherian ring, `M` a set, `(a_{m,m'})` a family of elements of `A` indexed by `M × M`,
such that*

<!-- label: III.IX.7.2 -->

*(i) `a_{m,m'} = 0` if `m ≠ m'` (i.e. the support of the family is contained in the diagonal of `M × M`),*

*(ii) One has*

```text
a_{m,m'} = ∑_i b^i_m c^i_{m'}
```

*where the `b^i, c^i` are finitely many elements of `A^M` (i.e. `(a_{m,m'})` belongs to the image of the canonical
homomorphism `A^M ⊗_A A^M → A^{M × M}`).*

*Under these conditions, the support of the family `(a_{m,m'})` is finite.*

<!-- original page 71 -->

By (i), the family `(a_{m,m'})` is determined by knowledge of the `a_m = a_{m,m}`. Set, for every
`x = (x_n)_{n ∈ M} ∈ A^{(M)}`:

```text
(u · x)_m = ∑_{m'} a_{m,m'} x_{m'},
```

i.e. interpret `(a_{m,m'})` as the matrix of a homomorphism `u : A^{(M)} → A^M`. Then by (i) one has simply

```text
(u · x)_m = a_m x_m.
```

On the other hand, by (ii) one has

```text
u · x ∈ ∑_i A · b^i,
```

hence `u(A^{(M)})` remains in a finitely generated `A`-module. Consequently, denoting by `(e_m)_{m ∈ M}` the canonical
basis of `A^{(M)} ⊂ A^M`, the `a_m e_m` remain in a finitely generated `A`-module. Since `A` is noetherian, the module
they generate is itself of finite type, which implies (since the `e_m` are linearly independent) that all but finitely
many of the `a_m` are zero. This proves 7.2 and consequently 7.1 in the case where `H` is diagonalizable.

Let us now prove the general case of 7.1, where one supposes only `H` isotrivial, i.e. there exists a finite étale
surjective morphism `S′ → S` such that `H′ = H ×_S S′` is diagonalizable. We shall use only the fact that `S′ → S` is
finite and covering (for the faithfully flat quasi-compact topology, or simply for the canonical topology of `(Sch)`) —
thus the "étale" hypothesis could be replaced by "flat".

<!-- original page 72 -->

Let `S″ = S′ ×_S S′`; introduce likewise `S'_n` and `S″_n = S″ ×_S S_n = S'_n ×_{S_n} S'_n`, and
`H′, G′, H″, G″, H'_n, G'_n, H″_n, G″_n` deduced from `H` and `G` by the base changes one guesses. Note that `H′` and
`H″` are now diagonalizable. Note also that `S′` hence `S″` is affine, and that if `S′ = Spec(A′)`, `S″ = Spec(A″)`,
then `A′` and `A″` are separated and complete for the topology defined by `IA′` resp. by `IA″` (since `A′` and `A″` are
finite over `A`). Since `S′ → S` and `S'_n → S_n` are covering, one obtains a commutative diagram of maps of sets whose
two rows are exact:

```text
Hom_{S-gr.}(H, G) ──→ Hom_{S′-gr.}(H′, G′) ⇉ Hom_{S″-gr.}(H″, G″)
       ↓u                       ↓u'                    ↓u''
lim_n Hom_{S_n-gr.}(H_n, G_n) → lim_n Hom_{S'_n-gr.}(H'_n, G'_n) ⇉ lim_n Hom_{S″_n-gr.}(H″_n, G″_n).
```

(N.B. The second row is exact as a projective limit of exact diagrams, relative to the various `S'_n → S_n`.) By what
has already been proved (the diagonalizable case), `u'` and `u''` are bijective. The same therefore holds for `u`, which
completes the proof of 7.1.

**Corollary 7.3.** *Under the conditions of 7.1, suppose moreover `G` smooth over `S`, and let `u_0 : H_0 → G_0` be a
homomorphism of `S_0`-groups. Then there exists a homomorphism of `S`-groups `u : H → G` which lifts `u_0`. Any two such
liftings `u, u′` are conjugate by an element `g` of `G(S)` reducing along the unit element of `G_0(S_0)`.*

<!-- label: III.IX.7.3 -->

Follows from the conjunction of 3.6 and 7.1. To construct a `u`, one constructs step by step `u_n`, which is possible by
3.6, and by 7.1 the system `(u_n)` comes from a `u`. Given two liftings `u` and `u′`, to construct `g` such that
`u′ = int(g) u`, `g_0 = 1`, <!-- original page 73 --> one constructs step by step `g_n`, such that `g_0 = 1`, `g_n` is
deduced from `g_{n+1}` by reduction, `u′_n = int(g_n) u_n`; this is possible thanks to 3.6. Since `A` is separated and
complete, the `g_n` come from a `g ∈ G(S)`; and to prove that `u′ = int(g) u`, it suffices to use the injectivity in
assertion 7.1.

**Remark 7.4.** *One will compare 7.1 with EGA III 5.4.1, which implies that the statement 7.1 is valid if, instead of
supposing `H` of multiplicative type and `G` affine, one supposes `H` proper over `S`, and `G` separated and locally of
finite type over `S`. Having a statement like 7.1 without a properness hypothesis is rather exceptional, and must here
be interpreted as one of the aspects of the great "rigidity" of the structure of a group of multiplicative type. The
analogous statement with `G = H = G_a` (additive group) is false in general, as one sees by taking `A` of characteristic
`p > 0`, and defining the `u_n` by reduction mod `I^{n+1}` from an additive formal series*

<!-- label: III.IX.7.4 -->

```text
u(T) = ∑_{n ⩾ 0} a_n T^{p^n},
```

*where the `a_n` are elements of `A` that tend to `0` for the `I`-adic topology, but not for the discrete topology.
Statement 7.1 also becomes false if one suppresses the hypothesis `G` affine, even for `H = G_m` (multiplicative group);
one sees an example of this (with `A` a complete discrete valuation ring) by starting from an elliptic curve over the
field of fractions `K` of `A`, which reduces (in the Néron–Kodaira reduction theory, say) along the group `G_m` over the
residue field `k`:*[^N.D.E-IX-48] *one will thus have a commutative smooth group scheme `G` over `S`, whose special
fiber is `G_{m,k}` (which, thanks to 3.6, allows one to define a projective system of isomorphisms* *`u_n : H_n ⥲ G_n`,
where `H = G_{m,A}`), but whose generic fiber is an abelian variety, so that there exists no homomorphism of `S`-groups
`H → G` other than `0`.*

## 8. Subgroups, quotient groups, and extensions of groups of multiplicative type over a field[^IX-8-1]

**Scholium 8.0.**[^N.D.E-IX-49] *Let `k` be a field, `H` an affine `k`-group scheme. Denote by `k[H]` its affine algebra
and `X(H) = Hom_{k-gr.}(H, G_{m,k})` the group of characters of `H`. By the lemma of independence of characters, `X(H)`
is a free part of `k[H]`. It follows that `H` is diagonalizable if and only if `X(H)` generates `k[H]` as a `k`-vector
space.*

<!-- label: III.IX.8.0 -->

<!-- original page 74 -->

**Proposition 8.1.** *Let `G` be a diagonalizable group scheme (resp. of multiplicative type) over a field
`k`.*[^N.D.E-IX-50] *Then for every subgroup scheme `H` of `G`, `H` and `G/H` are diagonalizable (resp. of
multiplicative type).*

<!-- label: III.IX.8.1 -->

Definition 1.1 reduces us at once to the non-resp. case. An easy passage to the limit, using VI_B 11.13 and VIII 3.1,
reduces us to the case where `G` is of finite type over `k`.[^N.D.E-IX-51] By VI_B 11.16,[^N.D.E-IX-52] one can find a
finite family of non-zero elements

```text
f_i = ∑ a_{im} m,    a_{im} ∈ k                                                 (8.1.1)
```

<!-- label: eq:III.IX.8.1.1 -->

of the affine ring `k^{(M)}` of `G = D_k(M)`, such that the points of `H` (with values in an arbitrary `k`-algebra `k′`)
are the points `g ∈ G(k′)` such that one has

```text
τ_g f_i = λ_i(g) f_i,    with λ_i(g) ∈ k′,                                       (8.1.2)
```

<!-- label: eq:III.IX.8.1.2 -->

where `τ_g` denotes the translation by `g`. Now one has

```text
τ_g f_i = ∑ a_{im} χ_m(g) m,                                                    (8.1.3)
```

<!-- label: eq:III.IX.8.1.3 -->

where `χ_m : G → G_{m,k}` is the character associated with `m`, so that (8.1.2) is equivalent to the relation

```text
χ_m(g) = χ_{m'}(g)    if m, m′ ∈ Z_i,                                            (8.1.4)
```

<!-- label: eq:III.IX.8.1.4 -->

`Z_i` denoting the set of `m ∈ M` such that `a_{im} ≠ 0`. This relation may also be written

```text
χ_{m' - m}(g) = 1    if m, m′ ∈ Z_i.
```

<!-- original page 75 -->

Denoting by `N` the subgroup of `M` generated by all the `m′ - m` (`i` varying, and `m, m′ ∈ Z_i`), one deduces from the
definition of `D_k(M)` (`≃ G`) that `H` identifies with `D_k(M/N)`. It then follows from VIII 3.1 that `G/H` identifies
with `D_k(N)`. QED.

**Proposition 8.2.**[^N.D.E-IX-53] *Let `k` be a field, `H, K` `k`-group schemes of multiplicative type and of finite
type, and `G` a `k`-group scheme such that one has an exact sequence*

<!-- label: III.IX.8.2 -->

```text
1 ⟶ H ⟶ G ⟶ K ⟶ 1
```

*(which entails that `G` is of finite type over `k`).*

*(i) If one supposes `G` commutative or `K` connected, then `G` is of multiplicative type.*

*(ii) If `K` and `H` are diagonalizable, with `K` a torus, then `G` is diagonalizable.*

For the proof of (i), the reader is referred to XVII 7.1.1, of which 8.2 (i) is a special case; the case of a field is
treated in part (i) of the proof of XVII 7.1.1 (not using the results of the following Exposés).

(ii) Suppose now `K` and `H` diagonalizable:

```text
K ≃ D_k(M)    and    H ≃ D_k(N).
```

[^N.D.E-IX-53] Suppose `G` of multiplicative type (which is the case by (i) if `K` is a torus). Then, by X 1.4, `G` is
isotrivial over `k`, i.e. there exists a finite separable extension `k′/k` such that `G′ = G ×_k k′` is diagonalizable,
so `G′ = D_{k′}(E)` for some commutative group `E`, and one has an exact sequence

```text
0 ⟶ D_{k′}(N) ⟶ D_{k′}(E) ⟶ D_{k′}(M) ⟶ 0.                                          (1)
```

<!-- label: eq:III.IX.8.2.1 -->

Hence, by VIII, 3.1 and 3.2, `M` is a subgroup of `E` and one has an exact sequence

```text
0 ⟶ M ⟶ E ⟶ N ⟶ 0.                                                                  (2)
```

<!-- label: eq:III.IX.8.2.2 -->

For a given extension `E_0` of `N` by `M`, consider the diagonalizable `k`-group `G_0 = D_k(E_0)`; then the `k`-functor
in groups `A` of automorphisms of the extension

```text
1 ⟶ H ⟶ G_0 ⟶ K ⟶ 1,                                                                (3)
```

<!-- label: eq:III.IX.8.2.3 -->

i.e. the sub-functor in groups of `Aut_{k-gr.}(G_0)` whose points on a `k`-prescheme `T` are the `φ ∈ Aut_{T-gr.}(G_T)`
inducing the identity on `H_T` and on `K_T`, identifies with `Hom_{k-gr.}(K, H)`, which is, by VIII 1.5, the constant
`k`-group of value `L = Hom_{gr.}(N, M)`.

One sees therefore that the classification of extensions `G` of `K` by `H` which, over a separable closure `k_s` of `k`,
become isomorphic to the extension (3), is the same as that of the <!-- original page 76 --> `k`-torsors for the étale
topology under the constant group `L_k`. Denoting `Γ = Gal(k_s/k)`, these are classified by the Galois cohomology group
(`L` being a trivial `Γ`-module):

```text
H^1_ét(k, L_k) = H^1(Γ, L) = Hom_{gr. top.}(Γ, L).
```

If moreover `K` is a torus, `M` is torsion-free, hence so is `L`, whence `Hom_{gr. top.}(Γ, L) = 0`; it follows that
every extension of `K` by `H` is already diagonalizable.

**Remark 8.3.** *As already pointed out in the proof of 8.2, the first assertion is stated and proved over an arbitrary
base in XVII 7.1.1. On the other hand, the second assertion generalizes, with essentially the same proof, to the case of
an integral normal base scheme (or more generally, geometrically unibranch), using X 5.13 below.*

<!-- label: III.IX.8.3 -->

*Finally, one can also consider 8.1 as a corollary of the (markedly less trivial) result 6.8, also valid over an
arbitrary base scheme.*[^N.D.E-IX-54]

## Bibliography

[^N.D.E-IX-55]

[BEns] N. Bourbaki, *Théorie des ensembles*, Chap. I–IV, Hermann, 1970.

<!-- LEDGER DELTA — Exposé IX — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| groupe de type multiplicatif | group of multiplicative type | Per Exposé IX–X titles. |
| de type multiplicatif quasi-isotrivial | of quasi-isotrivial multiplicative type | New term in Exposé IX. |
| de type multiplicatif isotrivial | of isotrivial multiplicative type | New term in Exposé IX. |
| de type multiplicatif localement trivial | of locally trivial multiplicative type | New term in Exposé IX. |
| localement isotrivial | locally isotrivial | New term in Exposé IX. |
| type de G en s | type of G at s | Standard. |
| schématiquement dense | schematically dense | Standard (EGA IV₃, 11.10). |
| famille schématiquement dense | schematically dense family | Standard. |
| schématiquement dense dans X | schematically dense in X | Standard. |
| universellement schématiquement dense | universally schematically dense | Per EGA IV₃, Def. 11.10.8. |
| rétrocompact | retrocompact | Standard. |
| majorer (un sous-préschéma) | majorize (a subprescheme) | Lattice-of-subpreschemes term. |
| sous-préschéma adhérence | adherence subprescheme | Per EGA I, end of N° 9.5. |
| voisinage infinitésimal | infinitesimal neighborhood | Standard. |
| cohomologie de Hochschild | Hochschild cohomology | Standard. |
| théorème de relèvement | lifting theorem | Section 3 title. |
| théorème de conjugaison | conjugation theorem | Section 3 title. |
| relèvement | lifting / lift | Choose by part of speech. |
| relever | lift | Standard. |
| théorème de densité | density theorem | Section 4 title. |
| homomorphisme central | central homomorphism | Standard. |
| sous-groupe central | central subgroup | Standard. |
| sous-groupe invariant | invariant subgroup | "Normal" in modern usage; keep "invariant" here. |
| factorisation canonique | canonical factorization | Standard. |
| algébricité | algebraicity | Section 7 title; technical loanword. |
| algébricité des homomorphismes formels | algebraicity of formal homomorphisms | Section 7 title. |
| application diagonale | diagonal map | For Hopf algebras: comultiplication, but keep literal here. |
| M-effectif | M-effective | Standard (per Exp. IV 3.4). |
| morphisme de descente effective | morphism of effective descent | Standard. |
| épimorphisme effectif universel | universal effective epimorphism | Standard. |
| morphisme couvrant | covering morphism | Standard. |
| extension radicielle | radicial extension | Loanword (purely inseparable). |
| géométriquement unibranche | geometrically unibranch | Standard. |
| géométriquement connexe | geometrically connected | Standard. |
| réduction de Néron-Kodaira | Néron–Kodaira reduction | En-dash. |
| courbe elliptique | elliptic curve | Standard. |
| variété abélienne | abelian variety | Standard. |
| clôture séparable | separable closure | Standard. |
| cohomologie galoisienne | Galois cohomology | Standard. |
| points associés | associated points | Per EGA IV₂. |
| corps fini / extension finie séparable | finite field / finite separable extension | Standard. |
| anneau de valuation discrète complet | complete discrete valuation ring | Standard. |
| Mittag-Leffler (condition de) | Mittag-Leffler condition | Standard. |
-->

[^IX-0-0]: Version 1.0 of 8 November 2009: additions in proof of 3.6 bis, 4.4–7, 5.0–6, 6.1, 7.1, 8.2. 8.1 and 4.5 to be
    revised.

[^N.D.E-IX-1]: *N.D.E.* Indeed, there exists by hypothesis an open neighborhood `U` of `s` and a faithfully flat
    quasi-compact morphism `S′ → U` such that `G_{S′}` is diagonalizable; then for every `s′ ∈ S′` above `s`,
    `κ(s′)` is an extension of `κ(s)` and `G_{s′} = G ×_S Spec(κ(s′))` is diagonalizable.

[^N.D.E-IX-2]: *N.D.E.* The number 1.4.1 has been added to the remarks that follow, for later references.

[^N.D.E-IX-3]: *N.D.E.* This definition has been added, since it appears in propositions 2.3 and 2.7.

[^N.D.E-IX-4]: *N.D.E.* Cf. also V, 9.1 or EGA IV₂, 2.7.1.

[^N.D.E-IX-5]: *N.D.E.* and even a closed immersion.

[^N.D.E-IX-6]: *N.D.E.* The erroneous reference to IV 4.7.5 has been corrected. Note that N° 8 of the present Exposé is
    independent of N°s 3 to 7.

[^N.D.E-IX-7]: *N.D.E.* The original indicated: "by 2.1 b), since its fibers are so". The editors did not understand
    this argument, and substituted the one that follows.

[^N.D.E-IX-8]: *N.D.E.* The following sentence has been spelled out.

[^N.D.E-IX-9]: *N.D.E.* Note that X 2.3 depends in an essential way on Theorem 3.6 of the present Exposé.

[^N.D.E-IX-10]: *N.D.E.* The numbering of the original has been preserved: there is no N° 3.7.

[^IX-4-1]: All the results from 4.1 to 4.6 are contained in EGA IV₃, 11.10, to which we refer the reader for an
    exposition in form of the notion of schematic density.

[^N.D.E-IX-11]: *N.D.E.* The "algebraicity" theorem 7.1.

[^N.D.E-IX-12]: *N.D.E.* All the results on schematic density stated in EGA IV₃, § 11.10 follow from the results on
    "separating families of homomorphisms" proved in loc. cit., § 11.9, to which we shall refer in certain
    *N.D.E.* that follow.

[^N.D.E-IX-13]: *N.D.E.* The original has been spelled out in what follows.

[^N.D.E-IX-14]: *N.D.E.* For another proof, using a reduction to the case where `S′` is locally noetherian (and 4.3 and
    4.5 as here), see EGA IV₃, 11.9.16 and 11.9.12 (N.B. in the last line of the proof of 11.9.16, replace
    11.9.5 by 11.9.12).

[^N.D.E-IX-15]: *N.D.E.* The following sentence has been added, and the original spelled out in what follows.

[^N.D.E-IX-16]: *N.D.E.* The original added: "at least at every point `x′` of `X′` above `s′`", but this restriction
    seems unnecessary.

[^N.D.E-IX-17]: *N.D.E.* The original has been spelled out and corrected, to show that the projective limit of the rings
    `O(T^i_n)` defines a closed formal subscheme of the formal scheme `Spf(Â)`.

[^N.D.E-IX-18]: *N.D.E.* The original has been spelled out and corrected, distinguishing between `S″_{(n)}` and the
    subscheme `S″_n = S″_n(s″)` introduced below.

[^N.D.E-IX-19]: *N.D.E.* This lemma has been inserted here, since it is used in the proof of 4.5 and 4.7.

[^N.D.E-IX-20]: *N.D.E.* This hypothesis is in fact superfluous, cf. EGA IV₃, 11.10.6 and 11.9.13.

[^N.D.E-IX-21]: *N.D.E.* The original has been spelled out in what follows.

[^N.D.E-IX-22]: *N.D.E.* The original continued with: "Using 4.3 for the `X_{A'}`, where `A′` is a quotient of `A` by a
    power of a maximal ideal, and Hilbert's Nullstellensatz, one is reduced to the case where `k′` is a
    finite extension of `k`". One could spell out this reduction, and pursue this approach, since the case
    of a finite extension `k′/k` is somewhat simpler than the more general case treated in EGA IV₃, 11.9.10
    b).

[^N.D.E-IX-23]: *N.D.E.* Specify this …

[^N.D.E-IX-24]: *N.D.E.* The original has been spelled out in what follows.

[^N.D.E-IX-25]: *N.D.E.* One will need in X 4.3 this result for `S` non locally noetherian (namely, `S = Spec(Â ⊗_A Â)`,
    where `Â` is the completion of the noetherian local ring `A`).

[^N.D.E-IX-26]: *N.D.E.* "Diagonalizable" has been replaced by "of multiplicative type".

[^N.D.E-IX-27]: *N.D.E.* This lemma has been made explicit, since it is used several times in the sequel (implicitly in
    the original).

[^N.D.E-IX-28]: *N.D.E.* The original has been spelled out in what follows.

[^N.D.E-IX-29]: *N.D.E.* Because `K = H` if `K_Ŝ = H_Ŝ`, cf. SGA 1, VIII 5.4; but the sequel does not use the hypothesis
    "`A` complete".

[^N.D.E-IX-30]: *N.D.E.* The original has been spelled out in what follows.

[^N.D.E-IX-31]: *N.D.E.* And of finite presentation over `S`, cf. EGA IV₃, 11.10.5 (ii) and 11.9.10 (ii).

[^N.D.E-IX-32]: *N.D.E.* "Morphism covering for the faithfully flat quasi-compact topology" has been replaced by
    "universal effective epimorphism", so as to be able to apply this to the morphism `K → S` of 5.5; the
    beginning of the proof has been modified accordingly.

[^N.D.E-IX-33]: *N.D.E.* This is the case, for example, if `S = Spec k` and `S′ = Spec k′`, where `k` is a field and
    `k′` a radicial extension of `k`, cf. X, Prop. 1.4.

[^N.D.E-IX-34]: *N.D.E.* The following sentence has been added.

[^N.D.E-IX-35]: *N.D.E.* The hypothesis "locally of finite type" has been added to agree with the reference VI_A, 2.4.
    In fact, one can show that over a field, every connected group scheme is geometrically connected.

[^N.D.E-IX-36]: *N.D.E.* The original has been spelled out in what follows.

[^N.D.E-IX-37]: *N.D.E.* The original has been spelled out in the proof of a).

[^N.D.E-IX-38]: *N.D.E.* The original has been spelled out and corrected, by replacing "unit section of `(G_H)_n` over
    `H_n`" by `H_{S^0_n}`.

[^N.D.E-IX-39]: *N.D.E.* The original has been spelled out in what follows, by making explicit the results of Exp. III
    that are used.

[^N.D.E-IX-40]: *N.D.E.* Since `S` is quasi-compact, it is covered by a finite number of affine opens, hence one is
    reduced to the case where `S = Spec(A)`. Then, since `G` is of finite presentation over `S`, one can
    apply EGA IV₃, 8.8.2.

[^N.D.E-IX-41]: *N.D.E.* Above, `X − {s}` has been corrected to `S − {s}`. Recall on the other hand that a quasi-finite
    morphism is supposed to be of finite type, cf. EGA II, 6.2.3 (and EGA III₂, Err_III 20 for the
    definition of "locally quasi-finite"). Hence here (`S` being noetherian), `X` is of finite presentation
    over `S`, each immersion `X_i ↪ X` is of finite type (by EGA I, 6.3.5), hence `X_i` is of finite
    presentation over `S`, and one may apply EGA IV₃, 8.8.2.

[^IX-6-1]: Cf. VI_B 2.5 (ii) for a more general statement.

[^N.D.E-IX-42]: *N.D.E.* Cf. EGA IV₃, 13.1.4, and EGA IV₄, 17.4.1. Moreover, `t` (instead of `s`) has been used to
    denote the image of `x`.

[^N.D.E-IX-43]: *N.D.E.* It in fact suffices to suppose `G` locally of finite type over `S`; by EGA IV₄, 1.4.3 (v), this
    entails (`H → S` being of finite presentation) that `H → G` is locally of finite presentation, hence so
    is `K → S`, which is deduced from it by base change.

[^N.D.E-IX-44]: *N.D.E.* The numbering 6.6.1 has been added, for later references.

[^N.D.E-IX-46]: *N.D.E.* "Induced by `G`" has been corrected to "induced by `u`".

[^N.D.E-IX-47]: *N.D.E.* What follows has been spelled out.

[^N.D.E-IX-48]: *N.D.E.* One could spell out such an example …

[^IX-8-1]: Added in July 1969. This regretful section is independent of N°s 3 to 7.

[^N.D.E-IX-49]: *N.D.E.* This scholium has been added.

[^N.D.E-IX-50]: *N.D.E.* "Over a field `k`" has been added, being implicit in the original; on the other hand,
    "algebraic group" has been replaced by "group scheme", since `G` is not supposed to be of finite type.

[^N.D.E-IX-51]: *N.D.E.* Spell out this "passage to the limit": this uses 8.0 and also the equality
    `G/H = lim_i G_i/H_i`, cf. VI_B, proof of 11.17. To see that `H = lim_i (H ∩ G_i)`, does one use the
    fact that `H` is closed in `G`? Using this, one can give a direct proof …

[^N.D.E-IX-52]: *N.D.E.* It would doubtless be necessary to rewrite VI_B 11.16 in the usual, more pleasant form. In
    particular, a single `f_i` suffices below …

[^N.D.E-IX-53]: *N.D.E.* The statement, as well as its proof, has been spelled out.

[^N.D.E-IX-54]: *N.D.E.* Note however that the proof of 6.8 uses 8.1!

[^N.D.E-IX-55]: *N.D.E.* Additional references cited in this Exposé.
