# Exposé XIV. Regular elements (continuation). Applications to algebraic groups

<!-- label: III.XIV -->

*by A. Grothendieck, with an Appendix by J.-P. Serre*

## 1. Construction of Cartan subgroups and of maximal tori for a smooth algebraic group

<!-- label: III.XIV.1 -->

<!-- original page 296 -->

**Theorem 1.1.** *Let `G` be a smooth algebraic group over a field `k`. Then `G` admits a maximal torus `T`, hence
a Cartan subgroup `C = Centr_G(T)`.*

<!-- label: III.XIV.1.1 -->

By virtue of (XII 3.2), it amounts to the same to find a maximal torus `T` of `G` or a Cartan subgroup `C` of `G`.
Moreover, since the maximal tori of `G` are those of `G⁰`, we may assume `G` connected. We distinguish two cases:

1°) *The field `k` is finite.* Let `T` be the scheme of maximal tori of `G` (Exp XII 1.10), which is a smooth scheme over
`k`. Note that `G` operates on `T` via inner automorphisms, and by virtue of the conjugation theorem (XII 6.6 a)), two
points of `T_{k̄}` rational over `k̄` are congruent under `G_{k̄}(k̄)`. Taking into account that `T` is smooth over `k`,
hence `T_{k̄}` smooth over `k̄`, it follows that `T_{k̄}` is isomorphic to `G_{k̄}/N`, where `N` is the stabilizer of an
element of `T_{k̄}(k̄)`, i.e. the normalizer of a maximal torus `T` of `G_{k̄}`. Consequently, `T` is a "homogeneous space"
under the action of the group `G`. A well-known theorem of Lang (Amer. J. Math. 78, 1956, pp. 555–563) tells us that
every homogeneous space under a smooth connected algebraic group over a finite field `k` admits a rational point. In
particular, `T` admits a rational point, i.e. `G` admits a maximal torus `T`. *QED*.

2°) *The field `k` is infinite.* We shall use the <!-- original page 297 -->

**Lemma 1.2.** *Let `G` be a smooth algebraic group over a field `k`. Then `G` admits a subgroup of type (C) (XIII 6.2).*

<!-- label: III.XIV.1.2 -->

By virtue of (XIII 6.3), this amounts to saying that `𝔤` contains a Cartan subalgebra `𝔡`. This is trivial if `k` is
infinite, for then `𝔤` contains a regular element `a`, and one takes `𝔡 = Nil(a, 𝔤)`. The case of finite `k` is handled
exactly as in the proof of 1°) above, but requires the prior construction of the scheme `𝒟` of Cartan subalgebras of
`𝔤` and the fact that this scheme is smooth over `k`, which will be carried out below (2.16).

To establish 1.1 in case 2°), where we have placed ourselves, it suffices in any event to know 1.2 for `k` infinite.
Let us also record for the record:

**Lemma 1.3.** *Let `G` be a smooth, connected, affine algebraic group whose reductive center (XII 4.1 and 4.4) is
reduced to the unit group. Then `G` is nilpotent if (and only if) its Lie algebra `𝔤` is nilpotent.*

<!-- label: III.XIV.1.3 -->

This is contained in (XII 4.9).

We can now give a procedure for constructing Cartan subgroups of `G` (also valid when `k` is finite, granting 1.2 in
that case). Suppose first that `G` is affine. We proceed by induction on `n = dim G`, the assertion being trivial if
`n = 0`. So suppose `n > 0` and the assertion proved for dimensions `n′ < n`. Let `Z` be the reductive center of `G`,
and let

```text
u : G ⟶ G′ = G/Z
```

be the canonical homomorphism. By virtue of (XII 4.7 c)), one has a bijective correspondence `C′ ↦ C = u⁻¹(C′)` between
Cartan subgroups of `G′` and Cartan subgroups of `G`. So, replacing `G` by `G′` if necessary, we may suppose that the
reductive center `Z` of `G` is reduced to the unit element (since this is the case for that of `G′` by XII 4.7 b)).
<!-- original page 298 --> By virtue of 1.3, `G` admits a subgroup `D` of type (C). We know that over the algebraic
closure `k̄` of `k`, `D_{k̄}` contains a Cartan subgroup of `G_{k̄}` (XIII 6.6 b)), hence every Cartan subgroup of `D` is a
Cartan subgroup of `G` (XIII 2.8 a)). So we are reduced to finding a Cartan subgroup of `D`. If `dim D = dim G`, i.e.
`D = G`, then the Lie algebra of `G` is a Cartan subalgebra of itself, hence is nilpotent, hence by 1.3 `G` is
nilpotent, hence is a Cartan subgroup of itself. If `dim D < dim G`, then by the induction hypothesis there exists a
Cartan subgroup of `D`, which is therefore a Cartan subgroup of `G`, which completes the proof in the case where `G` is
affine. In the general case, let `Z` be the center of `G`; then `G/Z = G′` is affine (XII 6.1) and for every Cartan
subgroup `C′` of `G′`, its inverse image `C` in `G` is a Cartan subgroup of `G` (XII 6.6 e)). One is reduced to finding
a Cartan subgroup of the smooth affine algebraic group `G′`, a case already treated.

**Corollary 1.4.** *Let `G` be a smooth group scheme of finite type over an artinian scheme `S`. Then `G` admits a
maximal torus `T`, hence a Cartan subgroup `C = Centr_G(T)`. Every torus `S` in `G` is contained in a maximal torus.*

<!-- label: III.XIV.1.4 -->

One may indeed suppose `S` local of residue field `k`; then by virtue of 1.1, `G₀ = G ×_S Spec(k)` admits a maximal
torus `T₀`, and by virtue of (IX 3.6 bis) and (X 2.3), `T₀` comes from a torus `T` of `G`, which is evidently a maximal
torus. The last statement follows from this, applying the preceding result to the centralizer of `S`, which is indeed
smooth over `k` (XI 2.4).

**Remarks 1.5.** a) We shall give below (3.20, 3.21 and XV) variants of 1.4 in the case where `S` is not assumed
artinian.

<!-- label: III.XIV.1.5 -->

b) I do not know whether every algebraic group `G` (not necessarily smooth) over a field `k` admits a maximal torus.
The question only arises in characteristic `p > 0`, and <!-- original page 299 --> using 1.1 for a smooth quotient group
of the form `G′ = G/I`, where `I` is a suitable radicial subgroup of `G` (for example, the kernel of a sufficiently
high power of the Frobenius homomorphism), one is reduced, by taking the inverse image in `G` of a maximal torus of
`G′`, to the case where `(G_{k̄})_red` is a torus (`k̄` always denoting the algebraic closure of `k`). It is easy to see
that the answer is affirmative when `G` is commutative (or more generally nilpotent): then `G` admits a unique maximal
torus, which one may construct for example by descent from the maximal torus of `G_{k̄}` [^XIV-1-1].

c) In the case where `G` is affine, and `k` is perfect or `G` solvable, 1.1 is known and due to Rosenlicht; his proof is
very different from the one given here.

d) When `k` is infinite, 1.1 is a consequence of the much more precise result that the scheme `T` of maximal tori of `G`
is a rational variety, proved below (6.1). The method is essentially a combination of the proof of 1.1 and of the
explicit description of the structure of the scheme `𝒟` of Cartan subalgebras of `𝔤`. To reach the desired result, we
must first generalize to the case of an arbitrary base prescheme certain results from (XIII 4 to 6) (this is the goal
of the next two sections), and refine the previous construction proving 1.1, by using the fact that every Cartan
subgroup of `G` is contained in one and only one subgroup of type (C) of `G` (Nos 4, 5).

[^XIV-1-1]: M. Raynaud gave a negative answer to the question raised here, cf. (XVII Example 5.9.c)).

## 2. Lie algebras over an arbitrary prescheme: regular sections and Cartan subalgebras

<!-- label: III.XIV.2 -->

**Lemma 2.1.** *Let `A` be a ring, `𝔡` a Lie algebra over `A`, and for every `s ∈ Spec(A)`, let `𝔡(s) = 𝔡 ⊗_A k(s)` be
the corresponding Lie algebra over the residue field `k(s)`. Suppose the `A`-module `𝔡` is of finite presentation. The
following conditions are equivalent:*

<!-- label: III.XIV.2.1 -->

- *(i) For every `s ∈ Spec(A)`, `𝔡(s)` is nilpotent.*
- *(ii) For every `x ∈ 𝔡`, `ad(x)` is nilpotent.*
- *(iii) There exists an integer `N ⩾ 0` such that for every sequence `x₁, …, x_N` of elements of `𝔡`, one has*

<!-- original page 300 -->

```text
ad(x₁) ad(x₂) … ad(x_N) = 0.
```

When `A` is a field, the equivalence of (i) and (iii) is the definition of "nilpotent", that of (ii) and (iii) is a
well-known consequence of Engel's theorem (Bourbaki, *Groupes et algèbres de Lie*, Chap. I, § 4, N° 2). In the general
case, one has trivially (iii) ⇒ (ii), and (ii) ⇒ (i) thanks to the preceding result and to the fact that (ii) is stable
by passage to quotients and by localization. It remains to prove (i) ⇒ (iii). When `A` is local artinian with maximal
ideal `𝔪`, let `n > 0` be an integer such that `𝔪ⁿ = 0`, let `N` be an integer such that condition (iii) is satisfied
for `𝔡(s) = 𝔡 ⊗_A A/𝔪`, and take `N′ = nN`; one sees at once that this integer satisfies (iii). When `A` is noetherian,
there exist finitely many elements `s_i ∈ Spec(A)` and ideals of definition `𝔮_i ⊂ A_{s_i}` such that the natural map

```text
𝔡 ⟶ ∏_i 𝔡 ⊗_A A_i,    where A_i = A_{s_i}/𝔮_i,
```

is injective; then by what precedes there exists for every `i` an integer `N_i` satisfying (iii) for the Lie algebra
`𝔡 ⊗_A A_i`, and taking `N` to be the largest of the `N_i`, one satisfies (iii) for `𝔡`. Finally, the general case
reduces to the noetherian case by the usual procedure explained in (EGA IV 8).

**Definition 2.2.** *Let `S` be a prescheme, `𝔡` a quasi-coherent Lie algebra over `S` that is a module of finite
presentation. One says that `𝔡` is locally nilpotent if for every `s ∈ S`, the Lie algebra `𝔡(s)` over `k(s)` is
nilpotent. One says that `𝔡` is strictly locally nilpotent if it is locally free, and if on every open `U` of `S` on
which it is of constant rank `r`, its Killing polynomial reduces to `P_𝔡(t) = tʳ`.*

<!-- label: III.XIV.2.2 -->

Of course, if `𝔡` is a locally free Lie algebra (as a module) over `S`, one defines its Killing polynomial as a
polynomial

```text
P_𝔡 ∈ A[t],    where A = Γ(Sym_{𝒪_S}(𝔡)) ≃ Γ(W(𝔡))
```

<!-- original page 301 -->

is the ring of sections of the structure sheaf of the vector bundle `W(𝔡)` defined by `𝔡`.

It is evident that the two notions just introduced in 2.2 are stable by base change, and of local nature for the fpqc
topology. Let us note:

**Proposition 2.3.** *If `𝔡` is strictly locally nilpotent, it is locally nilpotent. The converse is true when `𝔡` is
locally free and `S` is reduced.*

<!-- label: III.XIV.2.3 -->

The proof is immediate.

**Definition 2.4.** *Let `S` be a prescheme, `𝔤` a Lie algebra over `S` that is a locally free module of finite type.
Let `𝔡` be a Lie subalgebra of `𝔤`; one says that it is a Cartan subalgebra if it satisfies the following conditions:*

<!-- label: III.XIV.2.4 -->

- *(i) `𝔡` is a locally direct factor submodule (hence also locally free of finite type).*
- *(ii) For every `s ∈ S`, `𝔡(s)` is a Cartan subalgebra of `𝔤(s)`.*

**Definition 2.5.** *Let `S`, `𝔤` be as in 2.4. A section `a` of `𝔤` is called quasi-regular if for every `s ∈ S`,
`a(s) ∈ 𝔤(s)` is a regular element of the Lie algebra `𝔤(s)` over `k(s)`. One says that `a` is a regular section if it
is quasi-regular and contained in a Cartan subalgebra of `𝔤`.*

<!-- label: III.XIV.2.5 -->

Notions 2.4 and 2.5 are again stable by base change, and of local nature for the fpqc topology. Only the last assertion,
and only for the notion "regular section", requires a proof, and follows from the fact that the Cartan subalgebra
containing a given regular section is uniquely determined. More precisely:

<!-- original page 302 -->

**Proposition 2.6.** *Let `S`, `𝔤` be as in 2.4 and let `a` be a quasi-regular section of `𝔤`. Then there exists at most
one Cartan subalgebra of `𝔤` containing `a`. For one to exist, i.e. for `a` to be a regular section, it is necessary
and sufficient that `a` satisfy the following condition: `𝔡 = Nil(a, 𝔤)` is a locally direct factor submodule of `𝔤`,
and `ad(a)` induces an automorphism of `𝔤/𝔡`. In this case, `𝔡` is the unique Cartan subalgebra of `𝔤` containing `a`.*

<!-- label: III.XIV.2.6 -->

Suppose indeed that `a` is contained in the Cartan subalgebra `𝔡` of `𝔤`. Then `ad(a)_{𝔤/𝔡}` is bijective on each fiber,
hence (since `𝔤/𝔡` is locally free of finite type) it is an automorphism of `𝔤/𝔡`; on the other hand by virtue of 2.1
`ad(a)_𝔡` is locally nilpotent, hence `𝔡 = Nil(a, 𝔤)`, which proves the uniqueness of `𝔡`, and the necessity of the
stated regularity criterion. For sufficiency, note that the hypothesis made on `a` implies that the formation of
`Nil(a, 𝔤)` commutes with base extension and in particular with passage to fibers, which shows in particular that the
fibers `𝔡(s)` of `𝔡 = Nil(a, 𝔤)` are Cartan subalgebras of the `𝔤(s)`; moreover `𝔡` is a Lie subalgebra of `𝔤` by virtue
of (XIII 4.1), hence it is a Cartan subalgebra.

**Corollary 2.7.** *Under the conditions of 2.4, let `𝔡` be a Cartan subalgebra of `𝔤`, `a` a section of `𝔡` that is
regular in `𝔤`, `u` an automorphism of `𝔤`. In order for `u` to preserve `𝔡`, it is necessary and sufficient that `u(a)`
be a section of `𝔡`.*

<!-- label: III.XIV.2.7 -->

Indeed, by transport of structure `u(a)` is then a regular section of `𝔤`, contained in the two Cartan subalgebras `𝔡`
and `u(𝔡)`, which are therefore identical.

**Corollary 2.8.** *Under the conditions of 2.4, let `𝔡` be a Cartan subalgebra of `𝔤`. Then for every `s ∈ S` such that
`k(s)` is infinite, there exists an open neighborhood `V` of `s` and a regular section `a` of `𝔤` over `V` such that
`𝔡 = Nil(a, 𝔤|V)` (i.e. such that `a` is a section of `𝔡|V`).*

<!-- label: III.XIV.2.8 -->

Indeed, the fact that `k(s)` is infinite ensures the existence of a regular element `a₀` of <!-- original page 303 -->
`𝔤(s)` contained in `𝔡(s)`; one can extend it to a section `a` of `𝔡` on an open neighborhood `U` of `s`, and since
`ad(a)_{𝔤/𝔡}` induces an automorphism of `𝔤(s)/𝔡(s)`, it follows that, on restricting `V`, `ad(a)_{𝔤/𝔡}` is an
automorphism, which implies that `a` is a quasi-regular section of `𝔤|V` satisfying the desired condition.

Let `𝔤` be as in 2.4; then examination of its Killing polynomial implies at once that the function

```text
s ↦ nilpotent rank of 𝔤(s)
```

on `S` is upper semi-continuous. We are above all interested in the case when this function is in fact continuous, i.e.
locally constant. Here are some variants of this property:

**Proposition 2.9.** *Let `S`, `𝔤` be as in 2.4. Consider the following conditions:*

<!-- label: III.XIV.2.9 -->

- *(C₀) The nilpotent rank of the `𝔤(s)` (`s ∈ S`) is a locally constant function of `s`.*
- *(C₁) There locally exists, for the fpqc topology, a Cartan subalgebra of `𝔤`.*
- *(C₁′) Like (C₁), with "fpqc topology" replaced by "étale topology".*
- *(C₂) Condition (C₀) is satisfied, and for every `S′` over `S`, every quasi-regular section of `𝔤_{S′} = 𝔤 ⊗_S S′` is
  regular.*
- *(C₃) Every `s ∈ S` has an open neighborhood `V` on which the Killing polynomial of `𝔤` is of the form*

```text
tʳ(tⁿ⁻ʳ + c₁ tⁿ⁻ʳ⁻¹ + ⋯ + c_{n−r})
```

*where for every `s ∈ V`, `c_{n−r}(s) ∈ Sym(𝔤(s)^∨)` is non-zero.*

*With these notations, one has the implications*

```text
(C₃) ⇒ (C₂) ⇒ (C₁′) ⇒ (C₁) ⇒ (C₀),
```

<!-- original page 304 -->

*and when `S` is reduced, the five conditions considered are equivalent.*

Let us also note that the conditions considered are manifestly stable by base change, and of local nature for the fpqc
topology.

The implications (C₁′) ⇒ (C₁) ⇒ (C₀) are trivial, the implication (C₀) ⇒ (C₃) when `S` is reduced is immediate. Note
moreover:

**Corollary 2.10.** *Suppose condition (C₀) satisfied. Let `U` be the set of elements of `W(𝔤)` that are regular in
their fiber. Then `U` is open; in particular, for every section `a` of `𝔤` over `S`, the set `V` of `s ∈ S` such that
`a(s) ∈ 𝔤(s)` is regular, is open.*

<!-- label: III.XIV.2.10 -->

Indeed, the first assertion follows from the second (applied to `𝔤_{S′}` for every base change `S′` over `S`). For the
second, since one may suppose here `S` reduced, hence (C₃) verified, it suffices to examine the Killing polynomial of
`a` in `𝔤`.

The implication (C₂) ⇒ (C₁′) now follows easily from b) in the more precise statement that follows:

**Corollary 2.11.** *Suppose condition (C₂) satisfied. Then:*

<!-- label: III.XIV.2.11 -->

*a) For every `s ∈ S` and every Cartan subalgebra `𝔡₀` of `𝔤(s)` such that `𝔡₀` contains a regular element of `𝔤(s)`
(condition automatically satisfied if `k(s)` is infinite), there exists an open neighborhood `V` of `s` and a
subalgebra `𝔡` of `𝔤|V` whose fiber at `s` is `𝔡₀`. If `S₁` is a subprescheme of `S` containing `s`, and if one has
already extended `𝔡₀` to a Cartan subalgebra `𝔡₁` of `𝔤 ⊗_S S₁`, then one can find an open neighborhood `V` of `s` in
`S` and a Cartan subalgebra `𝔡` of `𝔤|V` such that `𝔡 ⊗_V (S₁ ∩ V)` is equal to `𝔡₁|(S₁ ∩ V)`.*

*b) For every `s ∈ S` such that `𝔤(s)` contains a regular element (condition automatically satisfied if `k(s)` is
infinite), <!-- original page 305 --> there exists an open neighborhood `V` of `s` and a Cartan subalgebra `𝔡` of `𝔤|V`.*

Statement b) follows from a) by taking `𝔡₀ = Nil(a₀, 𝔤(s))`, `a₀` being a regular element of `𝔤(s)`. To prove a), let us
say the second formulation, one considers a regular element `a₀` of `𝔤(s)` contained in `𝔡₀`, one extends it to a
neighborhood of `s` in `S₁` as a section of `𝔡₁`, and one extends this last to a section of `𝔤` in a neighborhood of
`s`. By virtue of 2.10, this section is quasi-regular in an open neighborhood `V` of `s`, hence regular by virtue of
(C₂), hence by virtue of 2.6 `𝔡 = Nil(a, 𝔤|V)` satisfies the required conditions.

**Remark 2.12.** I do not know if statement 2.11 a) and b) is valid without the hypothesis of existence of regular
points (when `k(s)` is finite).

<!-- label: III.XIV.2.12 -->

It remains to prove the implication (C₃) ⇒ (C₂). Let us also note the following equivalent form of (C₃):

- (C₃′) One has (C₀), i.e. the nilpotent rank of the `𝔤(s)` (`s ∈ S`) is locally constant, and on every open `V` of `S`
  where this rank has value `r`, the Killing polynomial of `𝔤|V` is divisible by `tʳ`.

It is necessary to show that this condition implies that every quasi-regular section `a` of `𝔤` is regular. Taking 2.6
into account, this is contained in the following lemma (applied to the endomorphism `ad(a)` of `𝔤`), (iv) ⇒ (iii):

**Lemma 2.13.** *Let `A` be a ring, `M` a projective `A`-module of finite type, `u` an endomorphism of `M`. The
following conditions are equivalent:*

<!-- label: III.XIV.2.13 -->

- *(i) `M` is the direct sum of two stable submodules `M′`, `M″` such that `u|M′` is nilpotent and `u|M″` is an
  automorphism of `M″`.*
- *(ii) There exists an integer `n > 0` such that `Im uⁿ + Ker uⁿ = M`.*
- *(iii) The nil-space `Nil(u) = ⋃_{n>0} Ker uⁿ` is a direct factor in `M`, and `M = Nil(u) + u(M)`.*

*These conditions are implied by the following (and are equivalent to it when `A` is reduced):* <!-- original page 306 -->

- *(iv) Locally on `Spec(A)` (for the Zariski topology) the characteristic polynomial `P_u(t)` of `u` can be put in the
  form*

```text
tʳ(tⁿ⁻ʳ + c₁ tⁿ⁻ʳ⁻¹ + ⋯ + c_{n−r}),
```

*where `c_{n−r}` is invertible.*

The equivalence of (i) (ii) (iii) is immediate and is recorded for the record. The fact that (i) implies (iv) when `A`
is reduced follows from the fact that in this case a nilpotent endomorphism of a projective module of rank `r` has
characteristic polynomial `tʳ`, while in any case the characteristic polynomial of an automorphism of a projective
module of finite type has as constant term the determinant of `u` up to sign (locally on `Spec(A)`), hence an
invertible element of `A`. Finally, to prove (iv) ⇒ (i), one notes that `M` is a module over the polynomial ring
`A[t]`, by letting `t` act as `u`, and the well-known identity

```text
P(u) = 0
```

shows that `M` is annihilated by `P A[t]`, hence can be considered as a module over `A[t]/P A[t]`. Now writing
`P = tʳ Q`, where the constant term of `Q` is invertible, one sees at once that

```text
P A[t] = tʳ A[t] ∩ Q A[t],
```

hence `A[t]/P A[t]` decomposes into the product of the rings `A[t]/tʳ A[t]` and `A[t]/Q A[t]`, whence a corresponding
decomposition of `M` as a sum of two `A[t]`-modules, i.e. as a sum of two `A`-submodules `M′` and `M″` stable under
`u`; this is the decomposition envisaged in (i).

This completes the proof of 2.13, hence of 2.9.

<!-- original page 307 -->

**Corollary 2.14.** *When condition (C₃) of 2.9 is satisfied, the Cartan subalgebras of `𝔤` are strictly nilpotent
(2.2).*

<!-- label: III.XIV.2.14 -->

The proof is immediate.

**Remark 2.15.** a) Let us point out that one can prove a converse of 2.14: (C₃) is equivalent to the fact that for
every `S′` over `S`, every quasi-regular section of `𝔤_{S′}` is regular and every Cartan subalgebra of `𝔤_{S′}` is
strictly nilpotent, or again, every quasi-regular section of `𝔤_{S′}` is contained in a strictly nilpotent Cartan
subalgebra of `𝔤_{S′}`.

<!-- label: III.XIV.2.15 -->

b) Contrary to the other conditions (C₀) to (C₂), condition (C₃) is of "infinitesimal nature". More precisely, when `S`
is locally noetherian, `𝔤` satisfies condition (C₃) if and only if for every base change `S′ → S` with `S′` local
artinian (if one wishes, `S′` the spectrum of an artinian quotient of a local ring of `S`), `𝔤_{S′}` satisfies the same
condition. Similarly, when (C₀) is satisfied, the condition for a section of `𝔤` to be regular is of infinitesimal
nature.

c) When `𝔤` is the Lie algebra of a smooth prescheme in groups of finite presentation over `S`, then we shall see that
conditions (C₀), (C₁), (C₁′), (C₂) on `𝔤` are equivalent (5.2 a)); I do not know what is the case in general (except
that, even for `S` local artinian, (C₀) does not imply (C₁)). However, even in the case where `𝔤` comes from a `G`,
and `S` being local artinian, it is not true in general that (C₂) implies (C₃), since `𝔤` can be nilpotent without
being strictly nilpotent. One obtains an example of this fact starting from a smooth affine group scheme `G` over the
spectrum `S` of a discrete valuation ring such that the Lie algebra of the generic fiber is non-nilpotent (for example
the generic fiber is an adjoint semisimple group), and that of the special fiber is nilpotent (for example, the special
fiber being a vector group): then for `n` large enough, the Lie algebra of `G_n = G ×_S S_n` is not strictly nilpotent,
however it is nilpotent.

<!-- original page 308 -->

Let us still place ourselves under the conditions of 2.4, and let

```text
𝒟 : (Sch)°/S ⟶ (Ens)
```

be the functor defined by

```text
𝒟(S′) = set of Cartan subalgebras of 𝔤_{S′}.
```

Let us also introduce the functor

```text
X(S′) = set of pairs (𝔡, a), where 𝔡 is a Cartan subalgebra of 𝔤_{S′} and a a section of 𝔡.
```

One thus has two projections `(𝔡, a) ↦ 𝔡` and `(𝔡, a) ↦ a`:

```text
p : X ⟶ 𝒟    and    ψ : X ⟶ W(𝔤).
```

When (C₀) is satisfied, we also consider the open `U` of regular points of `W(𝔤)` (cf. 2.10) and condition (C₂) is then
expressed by the fact that the morphism

```text
ψ⁻¹(U) ⟶ U
```

induced by `ψ` is an isomorphism (a priori, it is a monomorphism thanks to 2.6). Note that it is trivial that the
morphism `p : X → 𝒟` is representable by a projection of vector bundles (i.e. for every `S`-morphism `S′ → 𝒟`,
corresponding to a Cartan subalgebra `𝔡` of `𝔤_{S′}`, `X ×_𝒟 S′` is representable by a vector bundle over `S′`,
namely `W(𝔡)`); so if `𝒟` is representable, the same is true of `X`. Now one has:

**Theorem 2.16.** *Let `S` be a prescheme, `𝔤` a Lie algebra over `S` that is a locally free `𝒪_S`-module of finite
type; suppose condition (C₀) of 2.9 is satisfied.*

<!-- label: III.XIV.2.16 -->

*a) The functor `𝒟` of Cartan subalgebras of `𝔤` defined above is representable by a quasi-projective prescheme of
finite presentation over `S`. The same is true of the functor `X` defined above.* <!-- original page 309 -->

*b) When condition (C₂) of 2.9 is satisfied, `𝒟` and `X` are smooth over `S`, and the morphism `ψ⁻¹(U) → U` induced by
`ψ` is an isomorphism.*

*c) Still assuming condition (C₂) satisfied, let `s ∈ S`, `𝔡₀` a Cartan subalgebra of `𝔤(s)`, corresponding to a point
`d` of `𝒟` rational over `k(s)`. Suppose that `𝔡₀` contains a regular point of `𝔤(s)` (condition automatically
satisfied if `k(s)` is infinite). Let `r` be the infinitesimal rank of `𝔤(s)`, `n` its rank over `k(s)`; then there
exists an open neighborhood `V` of `d` in `𝒟` that is `S`-isomorphic to an open `V′` of `S[t₁, …, t_{n−r}]`.*

*Proof.* One may suppose `𝔤` of constant rank `n` and of constant nilpotent rank `r`. The assertions made about `X` in
a) and b) follow at once from the assertions made about `𝒟` and from the fact that `X` is a vector bundle over `𝒟`
defined by a locally free module, and are stated only for the record.

a) The functor `𝒟` is a subfunctor of the functor `Grass_{n−r}(𝔤)` whose value at `S′` is the set of locally free
quotient modules of rank `n − r` of `𝔤_{S′}`, and it is well known that this latter functor is representable by a
projective prescheme smooth over `S` (cf. for example Séminaire Cartan 1960/61, Exp. 12, Nos 2 and 3, whose
constructions transpose as they stand to the case of preschemes) [^XIV-2-1] [^N.D.E-XIV-1]. So one is reduced to a
relative problem, namely the following: given a locally free quotient module of rank `n − r` of `𝔤`, or equivalently, a
locally free submodule `𝔡` of rank `r` that is locally a direct factor, represent the following functor: `F(S′) = ∅` if
`𝔡` is not a Cartan subalgebra of `𝔤_{S′}`, `F(S′) = {∅}` otherwise. In fact, we shall see that `F` is representable by
a subprescheme of finite presentation of `S` (which will show that `𝒟 → Grass` is representable by an immersion of
finite presentation, and will finish proving a)). One begins by expressing the condition that `𝔡_{S′}` is a Lie
subalgebra of `𝔤_{S′}`; one sees at once that this is expressed by the fact that `S′ → S` factors through a certain
closed subprescheme `S₁` of `S`, of <!-- original page 310 --> finite presentation over `S` (whose local equations on
`S` can be written immediately using a basis of `𝔤` adapted to the submodule `𝔡`). One may therefore suppose that one
has already `S = S₁`. One must then express that `𝔡_{S′}` contains locally for fpqc a quasi-regular section of `𝔤_{S′}`,
and for this one considers `V = W(𝔡) ∩ U`, where `U` is the open of regular points of `W(𝔤)` (2.10); then the structure
morphism `V → S` being smooth and quasi-compact, its image `S₁` is an open part of `S` and the immersion morphism
`S₁ → S` is quasi-compact i.e. of finite presentation. The condition envisaged on `S′` is then expressed by saying that
`S′ → S` factors through `S₁`. So one is reduced to the case where `S = S₁`, and using the theory of descent, to the
case where `𝔡` admits a section `a` that is a quasi-regular section of `𝔤`. It remains finally to express that the
section `a_{S′}` of `𝔤_{S′}` deduced from `a` satisfies `ad(a_{S′})_{𝔤_{S′}/𝔡_{S′}}` bijective, which amounts again to
saying that `S′ → S` factors through a certain open subprescheme of finite presentation of `S`, namely `S_D`, where `D`
is the determinant of `ad(a)_{𝔤/𝔡}`. But then one sees at once that `𝔡|S_D` is a Cartan subalgebra of `𝔤|S_D`, hence
`S_D` represents the functor `F`, which proves a).

b) Is immediate thanks to 2.11 a) and (XI 1.5). Of course b) is also a consequence of the more precise statement c).

c) Let `a₀` be a regular point of `𝔤(s)` contained in `𝔡₀`; extend it to a section `a` of `𝔤` on an open neighborhood
`V` of `s`; one may evidently suppose `V = S`. On the other hand let `M₀` be a complement of the vector space `𝔡₀` in
`𝔤(s)`; then in an open neighborhood `V` of `S` there exists a submodule `M` of `𝔤`, a direct factor of `𝔤|V`, such
that `M(s) = M₀`, and one may again suppose `V = S`. Let now `𝒱` be the subfunctor of `𝒟` such that `𝒱(S′)` is the set
of Cartan subalgebras `𝔡′` of `𝔤_{S′}` satisfying the two following conditions:

- 1°) `𝔡′` is a complement of `M_{S′}`, and
- 2°) the unique section of `(a_{S′} + M_{S′}) ∩ 𝔡′` is a regular section of `𝔤_{S′}`.

<!-- original page 311 -->

Condition 1°) corresponds to an open `V₁` of `𝒟` (induced by the open of `Grass_{n−r}(𝔤)` defined by the same condition
1°)); the conjunction of 1°) and 2°) corresponds to an open of `V₁` by virtue of 2.10 and (C₂). Hence `𝒱` is
represented by an open subprescheme `V` of `𝒟`, evidently containing `d`.

On the other hand let `𝒱′` be the subfunctor of `W(M)` defined by

`𝒱′(S′) = set of sections u′ of M_{S′}` such that:

- (i) `a_{S′} + u′` is a regular section of `𝔤_{S′}`, and
- (ii) the unique Cartan subalgebra `𝔡′` of `𝔤_{S′}` containing `a_{S′} + u′` is a complement of `M_{S′}`.

Then condition 1°) corresponds to an open subprescheme `V₁′` of `W(M)`, namely the inverse image of the open `U` of
regular points of `W(𝔤)` (cf. 2.10) by the translation morphism `m ↦ a + m`. The conjunction of (i) and (ii) corresponds
to an open `V′` of `V₁′`, namely the inverse image of `V` by the obvious morphism `V₁′ → 𝒟` (associating to `u′` the
unique Cartan subalgebra `𝔡′` of `𝔤_{S′}` containing `a_{S′} + u′`). The restriction of this last morphism to `V′` is a
morphism

```text
V′ ⟶ V,
```

which is evidently an isomorphism. This proves c).

**Corollary 2.17.** *Let `𝔤` be a finite-dimensional Lie algebra over a field `k`. Then the scheme `𝒟` of Cartan
subalgebras of `𝔤` (2.16 a)) is quasi-projective, smooth and irreducible. When `𝔤` contains a regular element (for
example when `k` is infinite), `𝒟` is a rational variety, i.e. its function field is a pure extension of `k`.*

<!-- label: III.XIV.2.17 -->

The fact that `𝒟` is irreducible follows from the fact that one has a surjective morphism `ψ⁻¹(U) → 𝒟`, and `ψ⁻¹(U)` is
irreducible, being isomorphic to the open `U` of `W(𝔤)`. The assertion on the function field is an immediate
consequence of c).

**Remark 2.18.** I do not know if this conclusion remains valid if `k` is finite, without supposing that `𝔤` contains a
regular point; compare 2.12. One can prove that this is the case when `𝔤` is the Lie algebra of an algebraic group `G`
smooth over `k`, at least when <!-- original page 312 --> `G/radical` is an "adjoint" semisimple group, by using a
result of Chevalley pointed out below (cf. Appendix). It is plausible that this result remains valid without
restriction on `G`; it would suffice for this that the cited result of Chevalley be proved for every (not necessarily
adjoint) semisimple algebraic group.

<!-- label: III.XIV.2.18 -->

[^XIV-2-1]: Cf. also EGA I, 2nd edition (to appear in North Holland Publishing Co.).

[^N.D.E-XIV-1]: See § I.1.3 of M. Demazure and P. Gabriel, *Groupes algébriques*, Masson (1970).

## 3. Subgroups of type (C) of group preschemes over an arbitrary prescheme

<!-- label: III.XIV.3 -->

**Theorem 3.1.** *Let `S` be a prescheme, `G` a smooth `S`-prescheme in groups, `𝔤` its Lie algebra (which is a locally
free module of finite type over `S`), `𝔥` a Lie subalgebra of `𝔤` that is (as a module) a locally direct factor in `𝔤`,
and such that for every `s ∈ S`, the geometric fiber `𝔥_s` contains a Cartan subalgebra of `𝔤_s`. Let `a` be a
quasi-regular section of `𝔤` (2.5). Then*

```text
M_a = Transp_G(a, 𝔥)
```

*(subfunctor of `G` whose `S′`-valued points are the `g ∈ G(S′)` such that `ad(g) · a_{S′} ∈ Γ(S′, 𝔥_{S′})`) is
representable by a closed subprescheme [^N.D.E-XIV-2] of `G` smooth over `S`, whose structure morphism to `S` is
surjective.*

<!-- label: III.XIV.3.1 -->

Consider the canonical morphism

```text
ϕ : G ×_S W(𝔥) ⟶ W(𝔤)
```

given by `(g, x) ↦ ad(g) · x`; then `M_a` is `S`-isomorphic to `ϕ⁻¹(a)`, the inverse image of `a` (considered as a
section of `W(𝔤)` over `S`) by `ϕ`. It will suffice for the smoothness of `M_a` to show that `ϕ` is smooth at points of
`G ×_S W(𝔥)` lying over `Im(a)`; more generally `ϕ` is smooth at every point lying over a point of `W(𝔤)` that is
regular in its fiber `W(𝔤(s))` over `S`. To see this, since the source and target of `ϕ` are smooth, hence flat locally
of finite presentation over `S`, one is reduced to making the verification fiber by fiber, which reduces us to the case
where `S` is the spectrum of an algebraically closed field, `G` thus being a locally algebraic group over `k`, `𝔥` a
Lie subalgebra of its Lie algebra `𝔤`, containing a Cartan subalgebra of `𝔤`, and `a` a regular point <!-- original page
313 --> of `𝔤`. One may evidently suppose (taking into account that `ϕ` is a `G`-morphism) that the point of `G × W(𝔥)`
envisaged is of the form `(e, a)`. One may evidently suppose `G` connected, hence of finite type over `k`, but then our
assertion is none other than (XIII 5.4). Moreover, the fact that `M_a` is a closed subprescheme of `G` (of finite
presentation over `S`) is trivial, since `M_a` is the inverse image of `W(𝔥)` by the morphism `g ↦ ad(g) · a` of `G`
into `W(𝔤)`. The surjectivity of the structure morphism `M_a → S` also reduces to the case of an algebraically closed
base field, but then `𝔥` contains a Cartan subalgebra `𝔡` by hypothesis, which is therefore conjugate to the Cartan
subalgebra `𝔡 = Nil(a, 𝔤)` by the conjugation theorem (XIII 6.1 a)), hence `𝔥` contains a conjugate of `a`. This
completes the proof of 3.1.

**Corollary 3.2.** *Let `G`, `𝔤` be as in 3.1, with `G` of finite type over `S`; let `𝔨` and `𝔥` be two Lie subalgebras
of `𝔤`, locally direct factors (as modules); suppose that one is under one of the two following hypotheses:*

<!-- label: III.XIV.3.2 -->

*a) For every `s ∈ S`, the geometric fiber `𝔨_s` is nilpotent and contains a regular element of `𝔤_s`; the geometric
fiber `𝔥_s` contains a Cartan subalgebra of `𝔤_s`.*

*b) `𝔨` is a Cartan subalgebra of `𝔤`.*

*Then `Transp_G(𝔨, 𝔥)` is a closed subprescheme of `G` smooth over `S`; moreover, in case a), its structure morphism to
`S` is surjective.*

The fact that the transporter is representable by a closed subprescheme of finite presentation of `G` is immediate, and
left to the reader. Let us first prove smoothness in case a). Suppose first that there exists a section `a` of `𝔨` that
is quasi-regular in `𝔤`. Then it suffices to apply 3.1 and the

**Lemma 3.3.** *Under the conditions of 3.2 a), if `a` is a section of `𝔨` quasi-regular in `𝔤`, then one has*

<!-- label: III.XIV.3.3 -->

```text
Transp_G(𝔨, 𝔥) = Transp_G(a, 𝔥).
```

<!-- original page 314 -->

Indeed, taking the definitions into account, this amounts to showing that if `a` is moreover a section of `𝔥`, then one
has `𝔨 ⊂ 𝔥`. Now since by hypothesis `𝔨` is locally nilpotent, it follows from 2.1 that `𝔨 ⊂ Nil(a, 𝔤)`; on the other
hand `Nil(a, 𝔤) ⊂ 𝔥` because `ad(a)_{𝔤/𝔥}` is injective (being so fiber by fiber by virtue of (XIII 4.8 b))). Whence the
conclusion. In the general case, one reduces to the case where `S` is affine noetherian by the standard procedure, then
to the case where `S` is local artinian (smoothness being a property of infinitesimal nature), and by flat descent to
the case where its residue field is infinite, hence the fiber `K₀` admits an element that is regular in `𝔤₀`. One lifts
this element to an element of `K = Γ(𝔨)`, which reduces us to the preceding case. Thus, in case a) we have proved the
smoothness of the transporter; as for the fact that its structure morphism is surjective, it reduces to the case where
`S` is the spectrum of an algebraically closed field, hence where `K` contains a regular point of `𝔤`, and one applies
3.3 and 3.1.

To prove b), one is reduced by the definition of smoothness (XI 1.1) to proving that if `S` is affine, `S₀` a subscheme
defined by a quasi-coherent nilpotent ideal `J`, `g₀` an element of `G(S₀)` that transports `𝔨₀` into `𝔤₀`, then `g₀`
lifts to an element `g` of `G(S)` that transports `𝔨` into `𝔤`. Now the hypothesis on `g₀` implies that one is under
the conditions of a), already treated. This completes the proof.

Of course, when in 3.2 b) `𝔥` satisfies the stronger hypothesis of 3.1, then (and only then) the structure morphism
`Transp_G(𝔡, 𝔥) → S` is surjective. Using Hensel's lemma (XI 1.10), one concludes from 3.1 and 3.2:

**Corollary 3.4.** *Under the conditions of 3.1 for `G` and `𝔥`, and supposing `G` of finite type over `S`:*

<!-- label: III.XIV.3.4 -->

*a) For every quasi-regular section `a` of `𝔤`, there locally exists for the étale topology a conjugate of `a` that is
a section of `𝔥`.*

*b) For every Cartan subalgebra `𝔡` of `𝔤`, `𝔡` is locally for the étale topology conjugate to a subalgebra of `𝔥`.*

In particular, when `𝔥` is itself a Cartan subalgebra of `𝔤`, one finds: <!-- original page 315 -->

**Corollary 3.5.** *Let `G` be a smooth `S`-prescheme in groups of finite type, `𝔤` its Lie algebra, `𝔡` and `𝔡′` two
Cartan subalgebras of `𝔤`. Then `Transp_G(𝔡, 𝔡′)` is identical to the strict transporter of `𝔡` into `𝔡′`, and is a
closed subprescheme of `G` smooth over `S`, with surjective structure morphism. Locally for the étale topology, `𝔡` and
`𝔡′` are conjugate.*

<!-- label: III.XIV.3.5 -->

The fact that the transporter is identical here to the strict transporter follows trivially from the fact that `𝔡` and
`𝔡′` are locally direct factors in `𝔤` and have the same rank at every point. Hence 3.5 is a particular case of 3.4. In
particular, if `𝔡 = 𝔡′`:

**Corollary 3.6.** *Let `G` be as in 3.5, and let `𝔡` be a Cartan subalgebra of `𝔤`. Then `Norm_G(𝔡)` is a closed
subprescheme in groups of `G` smooth over `S`, whose Lie algebra is identical to `𝔡`.*

<!-- label: III.XIV.3.6 -->

Indeed, this last assertion amounts to saying that `𝔡` is its own normalizer in `𝔡`, which follows at once from the
fact that this is true fiber by fiber.

**Corollary 3.7.** *Let `G`, `𝔤` be as in 3.5. Then conditions (C₂), (C₁′), (C₁) of 2.9 are equivalent; in other words,
if `𝔤` admits locally for the fpqc topology a Cartan subalgebra, then every quasi-regular section of `𝔤` is regular.*

<!-- label: III.XIV.3.7 -->

Indeed, let `a` be a quasi-regular section; let us prove that it is regular. The question being local for the fpqc
topology, one may suppose that `𝔤` admits a Cartan subalgebra `𝔡`. By virtue of 3.4 a), `a` is then locally for the
étale topology conjugate to a section of `𝔡`, which reduces us to the case where `a` is a section of `𝔡`, where the
conclusion is trivial from the definition.

**Definition 3.8.** *Let `G` be a smooth prescheme in groups over a prescheme `S`. One calls a subgroup of type (C) of
`G` a subprescheme in groups `D` of `G`, smooth over `S`, with connected fibers, such that `𝔡 = Lie(D)` is a Cartan
subalgebra (2.4) of `𝔤 = Lie(G)`, i.e. such that for every `s ∈ S`, `D_s` is a subgroup of type (C) of the algebraic
group `G_s` (XIII 6.2).*

<!-- label: III.XIV.3.8 -->

<!-- original page 316 -->

**Theorem 3.9.** *Let `G` be a smooth `S`-prescheme in groups of finite presentation, `𝔤` its Lie algebra. Then:*

<!-- label: III.XIV.3.9 -->

*a) The map*

```text
D ↦ 𝔡 = Lie(D)
```

*establishes a bijective correspondence between subgroups of type (C) of `G` and Cartan subalgebras of `𝔤`.*

*b) If `D` and `𝔡` correspond, one has*

```text
Norm_G(D) = Norm_G(𝔡),
```

*it is a closed subprescheme of `G` smooth over `S`, and one has*

```text
D = Norm_G(D)⁰ = Norm_G(𝔡)⁰.
```

*c) Two subgroups of type (C) `D` and `D′` of `G` are conjugate locally for the étale topology.*

*Proof.* Let `D` be a subgroup of type (C) of `G`, and `𝔡` its Lie algebra; then `D ⊂ Norm_G(𝔡)`, and by virtue of
Definition 3.8 and 3.6 this is an inclusion of preschemes in groups smooth over `S`, inducing an isomorphism on the
Lie algebras. Since `D` has connected fibers, one therefore has `D = Norm_G(𝔡)⁰`. Hence the map envisaged in a) is
injective; let us prove that it is surjective. So let `𝔡` be a Cartan subalgebra of `𝔤`; then by virtue of 3.6
`Norm_G(𝔡) = N` is a closed subprescheme in groups of `G` smooth over `S`, admitting `𝔡` as Lie algebra. Since `G` is of
finite presentation over `S`, the same is true of `N`, hence (as was pointed out in XII after 7.3) the union of the
connected components of the fibers of `N` is the underlying set of an open subprescheme in groups `N°` of `N`, which is
evidently a subgroup of type (C) of `G` having Lie algebra `𝔡`. This proves a); the first assertion of b) follows from
it at once; <!-- original page 317 --> and the formula `D = Norm_G(𝔡)⁰` has already been proved. Finally, c) follows
from a) and 3.5.

**Corollary 3.10.** *Suppose that `𝔤` admits locally for the fpqc topology a Cartan subalgebra (or equivalently, by
virtue of 3.9 a), that `G` admits locally for the fpqc topology a subgroup of type (C)). Consider the functor
`𝒟 : (Sch)°/S → (Ens)` defined by `𝒟(S′) = ` set of subgroups of type (C) of `G_{S′}`. Then this functor is
representable by a quasi-projective and smooth prescheme over `S`, with connected geometric fibers. When `S` is the
spectrum of a field `k`, hence `G` a smooth algebraic group over `k`, and `𝔤` admits a regular point (condition
automatically satisfied if `k` is infinite), then `𝒟` is a rational variety over `k`.*

<!-- label: III.XIV.3.10 -->

Indeed, by virtue of 3.9 a), the functor `𝒟` is canonically isomorphic to the functor envisaged in 2.16; on the other
hand by virtue of 3.7 condition (C₂) is satisfied. Hence 3.10 follows from 2.16 and 2.17.

**Corollary 3.11.** *Let `D` be a subgroup of type (C) of `G`, and let `N` be its normalizer in `G`. Then the quotient
sheaf `G/N` is canonically isomorphic to the functor `𝒟` of 3.10, hence representable by a quasi-projective and smooth
prescheme over `S`, with connected geometric fibers.*

<!-- label: III.XIV.3.11 -->

**Proposition 3.12.** *Let `G` be a smooth `S`-prescheme in groups of finite presentation over `S`, `H`, `K` two
subpreschemes in groups, smooth of finite presentation over `S`, with `K` having connected fibers; `𝔤`, `𝔨`, `𝔥` the
corresponding Lie algebras. Suppose that one of the two following conditions is realized for the geometric fibers of
these latter:*

<!-- label: III.XIV.3.12 -->

<!-- original page 318 -->

*a) For every `s ∈ S`, `𝔨_s` contains a regular element of `𝔤_s`, and `𝔥_s` contains a Cartan subalgebra of `𝔤_s`.*

*b) For every `s ∈ S`, `𝔨_s` contains a Cartan subalgebra of `𝔤_s`.*

*Under these conditions, in order to have `H ⊃ K`, it is necessary and sufficient that one have `𝔥 ⊃ 𝔨`.*

Of course, we need only prove that if `𝔥 ⊃ 𝔨`, then `H ⊃ K`. In case b), the inclusion `𝔥 ⊃ 𝔨` shows that one is in fact
under the conditions of a), so it suffices to prove a). Proceeding as in 3.2 a) by reduction to the case `S` local
artinian, one is reduced to the case where there exists a section `a` of `𝔨` that is quasi-regular in `𝔤`. In this case,
proceeding as in (XIII 5.5), one is reduced to the following statement:

**Corollary 3.13.** *Let `G` be a smooth `S`-prescheme in groups of finite presentation over `S`, `H` a subprescheme in
groups of `G` smooth of finite presentation over `S`, `𝔤` and `𝔥` the Lie algebras, `a` a section of `𝔥` that is
quasi-regular in `𝔤`. Suppose that for every `s ∈ S`, the geometric fiber `𝔥_s` contains a Cartan subalgebra of `𝔤_s`.
Let*

<!-- label: III.XIV.3.13 -->

```text
M_a = Transp_G(a, 𝔥),
```

*which is a closed subprescheme of `G` smooth over `S` (cf. 3.1), so that `M_a⁰` (union of the connected components of
the identity element in the fibers of `M_a`) is an open part of `M_a`, which we shall endow with the structure induced
by `M_a`. One then has `H⁰ = M_a⁰`.*

Evidently one has `H ⊂ M_a`, whence `H⁰ ⊂ M_a⁰`. Since this is an inclusion of preschemes smooth over `S`, to prove that
it is an equality, one is reduced to verifying it on the fibers, which reduces us to the case where `S` is the spectrum
of an algebraically closed field, a case treated in (XIII 5.4).

**Corollary 3.14.** *Let `G` be a smooth `S`-prescheme in groups of finite presentation, `D` a subgroup of type (C) of
`G`, `H` a subprescheme in groups of `G` smooth over `S` and of finite presentation over `S`, <!-- original page 319 -->
`𝔡` and `𝔥` their Lie algebras. Then one has*

<!-- label: III.XIV.3.14 -->

```text
Transp_G(D, H) = Transp_G(𝔡, 𝔥),
```

*and this functor is representable by a closed subprescheme of `G` smooth over `S`.*

Indeed, the identity between the two transporters follows from 3.12 b), which allows one to apply 3.2.

**Corollary 3.15.** *Let `G`, `H` be as in 3.14 and suppose that for every `s ∈ S`, the geometric fiber `𝔥_s` contains a
Cartan subalgebra of `𝔤_s`. Suppose moreover that `𝔤` admits locally for the fpqc topology a Cartan subalgebra. Then
locally for the étale topology, `H` contains a subgroup of type (C) of `G`.*

<!-- label: III.XIV.3.15 -->

By virtue of 3.7 and 3.9 a), `G` admits locally for the étale topology a subgroup of type (C), so one may suppose that
`G` admits such a subgroup, say `D`. Then the hypothesis on `𝔥` means also that the structure morphism of the
transporter considered in 3.14 is surjective (taking into account the conjugation theorem XIII 6.1 a)). One concludes
by Hensel's lemma (XI 1.10).

**Corollary 3.16.** *Let `G`, `H`, `K` be as in 3.12 a); suppose moreover that for every `s ∈ S`, the geometric fiber
`𝔨_s` is nilpotent (i.e. `𝔨` is locally nilpotent). Then one has*

<!-- label: III.XIV.3.16 -->

```text
Transp_G(K, H) = Transp_G(𝔨, 𝔥),
```

*and this functor is representable by a closed subprescheme of `G` smooth over `S`, whose structure morphism to `S` is
surjective. `H` contains locally for the étale topology a subgroup conjugate to `K`.*

<!-- original page 320 -->

The identity of the two transporters is again contained in 3.12 a), the assertion on its structure is then none other
than 3.2 a), and the last assertion of 3.16 is then a consequence of Hensel's lemma.

**Remarks 3.17.** a) In 3.12 and 3.16, one may replace the hypothesis that `K` is smooth over `S` by the following
weaker hypothesis: the sheaf `e_K*(Ω¹_{K/S}) = ω¹_K` of relative 1-differentials along the unit section is locally free.
In this way, 3.12 contains (XIII 5.5).

<!-- label: III.XIV.3.17 -->

b) Let `G`, `𝔤`, `𝔥` be as in 3.1, with `G` of finite presentation over `S`. Then `N = Norm_G(𝔥)` is not necessarily
smooth over `S` along the unit section, or equivalently, there does not necessarily exist a subprescheme in groups `H`
of `S` smooth over `S` whose Lie algebra is `𝔥`, even if `S` is the spectrum of a field. When such an `H` exists, so
that one has (taking `H` with connected fibers) `N = Norm_G(H)`, I do not know whether `N` is smooth over `S`. In this
question, one may evidently reduce to the case where `S` is local artinian.

To conclude this section, let us examine the case where `G` is "semisimple" over `S`:

**Theorem 3.18.** *Let `S` be a prescheme, `G` a smooth `S`-prescheme in groups over `S`, whose geometric fibers are
"adjoint" semisimple groups, i.e. semisimple with reductive center (XII 4.1 and 4.4) reduced to the unit group. Then the
subgroups of type (C) of `G` are identical with its maximal tori, hence also with its Cartan subgroups (XII 3.1).*

<!-- label: III.XIV.3.18 -->

Taking definitions into account, one is reduced to the case where `S` is the spectrum of an algebraically closed field,
and to proving then that for a maximal torus `T` of `G`, the Lie algebra `𝔱` of `T` is a Cartan subalgebra of `𝔤`, that
is to say (taking into account the inequality `nilpotent rank of 𝔤 ⩾ nilpotent rank of G = dim T = rank 𝔱 = r`) that
there exists `x ∈ 𝔱` with `dim Nil(x, 𝔤) = r`. Since `𝔱` is abelian and *a fortiori* nilpotent, it amounts to the same
to say that there exists `a ∈ 𝔱` such that `ad(a)_{𝔤/𝔱}` is injective <!-- original page 321 --> (XIII 5.7 a)). Now
consider the characters `α` of `T` that intervene in the representation of `T` induced by the adjoint representation
of `G`. The structure theory of the semisimple group `G` (*Bible*, 13 th. 1 a) and th. 3, cor. 2), more precisely the
"big cell" of `G`, semidirect product of `T` and subgroups `P_α` isomorphic to the additive group `G_a`, preserved by
`T` and corresponding to the "root" characters of `G` for the torus `T`, shows that the eigenspace of `𝔤` relative to
the trivial character is none other than `𝔱`, and the other eigenspaces are of dimension 1, the characters `α`
associated being none other than the roots of `G` for `T`. By virtue of the computation of the reductive center of `G`
as the intersection of the kernels of the characters of `T` that intervene in the adjoint representation of `G` (XII
4.8), one sees that the fact that `G` is adjoint is interpreted as saying that the roots generate the lattice
`M = Hom(T, G_m)`. Now a well-known lemma of the theory of roots tells us that every root is part of a system of simple
roots, hence of a basis of the group generated by the roots, and consequently of a basis of the dual `M` of `T`
[^N.D.E-XIV-3]. We conclude:

**Corollary 3.19.** *If `G` is an adjoint semisimple algebraic group over an algebraically closed field `k`, `T` a
maximal torus of `G`, then for every root `α` of `G` with respect to `T`, `α : T → G_m`, the corresponding homomorphism
`α′ : 𝔱 → k` is non-zero.*

<!-- label: III.XIV.3.19 -->

This result is essentially equivalent to Theorem 3.18, for given `t ∈ 𝔱`, `ad(t)` is semisimple and its eigenvalues in
`𝔤/𝔱` are none other than the `α′(t)`, hence `ad(t)_{𝔤/𝔱}` is injective if and only if the `α′(t)` are `≠ 0`, and there
exists `t ∈ 𝔱` having this property if and only if all the `α′` are `≠ 0`.

**Corollary 3.20.** *Let `S` be a prescheme, `G` an `S`-prescheme in groups, smooth, of finite presentation over `S`,
whose geometric fibers are connected reductive algebraic groups (i.e. extensions of a semisimple group by a torus).
Then for every `s ∈ S` there exists an open neighborhood `U` of `s` such that `G|U` admits a maximal torus.* [^XIV-3-1]

<!-- label: III.XIV.3.20 -->

We shall see indeed in XVI that the hypothesis just made on `G` implies <!-- original page 322 --> that `G` is affine
over `S` and of locally constant reductive rank; hence (XII 4.7 c)) `G` admits a reductive center `Z`, `G′ = G/Z` is a
smooth and affine group over `S` whose reductive center is reduced to the unit group, and finally the maximal tori of
`G` and of `G′` are in bijective correspondence. Moreover, one sees at once that the geometric fibers of `G′` are
connected semisimple groups, and moreover adjoint by definition (their reductive center being trivial). So it suffices
to limit oneself to the case where `G` is semisimple and adjoint, and by virtue of 3.18 one is reduced to finding an
open neighborhood `U` of `s` and a subgroup of type (C) of `G|U`, or equivalently (3.9 a)) a Cartan subalgebra of `𝔤|U`.
Now this is possible if `k(s)` is infinite, since by virtue of 3.7 `𝔤` satisfies condition (C₂) of 2.9, hence one may
apply 2.11 b). In fact, statement 3.20 remains valid without supposing `k(s)` infinite. Indeed, by the preceding
argument, it suffices to know that for every adjoint semisimple group `G` over a finite field `k`, the Lie algebra `𝔤`
of `G` contains a regular element. Now this statement has been proved by Chevalley (using the properties of the
Coxeter element of the Weyl group...), cf. the Appendix below by J.-P. Serre.

**Remarks 3.21.** a) Statement 3.20 remains valid, with essentially the same proof, replacing `G` by a closed
subprescheme in groups `H` smooth over `S`, having everywhere the same rank as `G` (for example a "parabolic subgroup"
of `G`), provided that `k(s)` is infinite. I do not know if here again the hypothesis that `k(s)` is infinite is
superfluous. One can show that this is the case at least if `H` is parabolic, thanks to the construction of the radical
`U` of `H` and of the quotient `H/U`, which reduces us to the semisimple case. Unfortunately, the method of regular
elements seems here powerless, since one easily constructs examples (for example with the projective group and its
"standard" Borel subgroup) where the Lie algebra `𝔥` of `H` does not contain any regular element.

<!-- label: III.XIV.3.21 -->

<!-- original page 323 -->

b) The proof of 3.20 in fact shows a more precise result (by invoking 3.9 b)) in the case where `k(s)` is infinite,
namely that every maximal torus `T₀` of `G_s` comes from a maximal torus `T` on an open neighborhood of `s`. I do not
know if this statement remains valid when `k(s)` is no longer supposed infinite; the difficulty obviously coming from
the fact that the Lie algebra `𝔱₀` of `T₀` does not in general contain a regular element of the Lie algebra `𝔤₀` of the
fiber `G_s`. An affirmative answer to this problem would imply the following statement (which is proved only in the
case of an infinite residue field or when `A` is separated and complete): Let `A` be a local ring, with residue field
`k`, `M` an "Azumaya algebra" over `A`, i.e. an algebra such that `M` is a free module of finite type over `A`, and
`M₀ = M ⊗_A k` a central simple algebra over `k`, `D₀` a commutative subalgebra of `M₀` separable over `k`, such that
`[M₀ : k] = ([D₀ : k])²`; then there exists a commutative subalgebra `D` of `M`, which is a direct factor module in
`M` and such that `D ⊗_A k = D₀` (?). (Note that the datum of `M` is equivalent to the datum of a principal homogeneous
bundle under the projective group `PGL(n)_A`, whence an "inner" twisted form `G` of `PGL(n)`, and the maximal tori of
`G` correspond bijectively to the commutative subalgebras `D` of `M` étale over `A` of rank `n` over `A`.)

c) Applying 3.20 to the centralizer of a subtorus `Q` of `G` (`G` a reductive `S`-prescheme in groups), one deduces that
every such `Q` is contained, locally for the Zariski topology, in a maximal torus of `G`.

[^N.D.E-XIV-2]: One has written `Transp_G(a, 𝔥)`.

[^N.D.E-XIV-3]: One has replaced `T̂` by `T`.

[^XIV-3-1]: This result, as well as 2.11 on which it rests, generalizes immediately to the case where `s` is replaced by a finite part of `S` contained in an affine open.

## 4. A digression on Borel subgroups

<!-- label: III.XIV.4 -->

**Definition 4.1.** *Let `G` be a smooth algebraic group over an algebraically closed field. One calls a Borel subgroup
of `G` a smooth, solvable, connected algebraic subgroup that is maximal for these properties.*

<!-- label: III.XIV.4.1 -->

When `G` is affine, one thus recovers the terminology of (*Bible* 6 def. 1). Let us note at once that if `Z` is a
connected and smooth subgroup of `G` contained in the center <!-- original page 324 --> (or more generally, solvable and
invariant), then for every Borel subgroup `B` of `G`, the image `BZ` of `B × Z` by the morphism `(b, z) ↦ bz` of
`B × Z` into `G` is a smooth, solvable, connected subgroup of `G` containing `B`, hence identical to `B`, hence `B`
contains `Z`, hence `B` is the inverse image of an algebraic subgroup `B′` of `G′ = G/Z`, and it is immediate that `B′`
is a Borel subgroup of `G′`. Taking `Z = Centr(G⁰)°_{red}`, `G′ = G/Z` is affine (XII 6.1), hence the Borel subgroups of
`G′` are conjugate and for such a `B′`, `G′/B′` is a projective variety (*Bible* 6 th. 4). Consequently:

**Proposition 4.2.** *Let `G` be as in 4.1. Then the Borel subgroups of `G` are conjugate. If `B` is a Borel subgroup,
then `G/B` is a projective variety. The maximal tori of `B` (resp. the Cartan subgroups of `B`, `G` being connected)
are maximal tori of `G` (resp. Cartan subgroups of `G`).*

<!-- label: III.XIV.4.2 -->

It remains to prove the last assertion, and one may evidently suppose `G = G⁰`. For the Cartan subgroups, it follows
from the analogous assertion in `G′` (*Bible* 6 th. 4 cor. 4) and from (XII 6.6 e)). For the maximal tori, it follows
from the preceding, since by (XII 6.6 c)) the maximal tori of a smooth algebraic group are the maximal tori of its
Cartan subgroups.

**Corollary 4.3.** *Suppose `G` connected. Then every element of `G` is contained in a Borel subgroup of `G`.*

<!-- label: III.XIV.4.3 -->

One is reduced to the same statement in `G′`, which is well known (*Bible* 6 th. 5 d)).

**Corollary 4.4.** *Let `B` be a Borel subgroup of `G`, `C` a Cartan subgroup of `B`, `N` its normalizer in `G`; then
`N ∩ B = C`.*

<!-- label: III.XIV.4.4 -->

Indeed, `N ∩ B = Norm_B(C)`, so one is reduced to showing that when `G` is connected and solvable, a Cartan subgroup
`C` is its own connected <!-- original page 325 --> normalizer. Now with the preceding notations, `C` is the inverse
image of a Cartan subgroup `C′` of `G′`, so one is reduced to the case where `G` is affine. Since one knows that the
normalizer of a Cartan subgroup is smooth (`C` being its own connected normalizer, cf. for example XII 6.6 c)), it
suffices to see that `C` and `N` have the same `k`-valued points, which is none other than (*Bible* th. 6 d)).

**Definition 4.5.** *Let `G` be a smooth prescheme in groups of finite presentation over a prescheme `S`. One calls a
Borel subgroup of `G` any subprescheme in groups `B` of `G`, smooth of finite presentation, such that for every
`s ∈ S`, the geometric fiber `B_s` is a Borel subgroup of `G_s`.*

<!-- label: III.XIV.4.5 -->

This is therefore, as one verifies at once, a notion stable by base change and of local nature for the fpqc topology
(for if `k′` is an algebraically closed extension of an algebraically closed field `k`, then an algebraic subgroup `B`
of the smooth algebraic group `G` over `k` is a Borel subgroup of `G` if and only if `B_{k′}` is one of `G_{k′}`). It
follows from this definition that if `G` is a smooth algebraic group over an arbitrary field `k`, `B` a Borel subgroup
of `G`, then `G/B` is a projective variety, every maximal torus `T` of `B` is a maximal torus of `G`, its normalizer
in `B` is identical to its centralizer `C`, and is a Cartan subgroup of `G` when `G` is connected.

**Remarks 4.6.** Unfortunately, it is no longer true in general (even if `G` is affine over `S` and `S` is the spectrum
of the algebra of dual numbers over an algebraically closed field `k`) that two Borel subgroups of `G` are conjugate
locally for the fpqc topology. As a consequence of this regrettable fact, let us point out that if `G` is a smooth,
affine, connected algebraic group over a non-perfect field `k`, it is not possible in general to define in a natural
way a homogeneous space `𝒟` under `G`, playing the role of a flag variety, i.e. of the variety of Borel subgroups of
`G` (which, over the algebraic closure `k̄` of `k`, would therefore be isomorphic to `G_{k̄}/B`, where `B` is a Borel
subgroup of `G_{k̄}`). Indeed, when the quotient of `G_{k̄}` by its radical `R` is an adjoint semisimple group, then the
kernel of `G_{k̄} → Aut_{k̄}(𝒟)` is the radical of <!-- original page 326 --> `G_{k̄}`, hence if `𝒟` came from a
homogeneous space `D` under `G`, the radical `R` would come from a subgroup `R` of `G`. Now one easily constructs
examples where `G_{k̄}/R` is adjoint but `R` is not "defined over `k`". It is easy to see that under these conditions,
the functor `𝔅 : (Sch)°/S → (Ens)` such that `𝔅(S′) = ` set of Borel subgroups of `G_{S′}` is not representable by a
smooth `S`-prescheme. From the infinitesimal point of view (III § 3), the non-validity of the conjugation theorem is
expressed by the fact that if `B` is a Borel subgroup of the smooth algebraic group `G`, the cohomology group
`H¹(B, 𝔤/𝔟)` [^N.D.E-XIV-4] can be different from zero.

<!-- label: III.XIV.4.6 -->

We shall see on the other hand in a later exposé that when `G` is semisimple, or more generally reductive, such
unpleasant phenomena do not occur. It is these phenomena no doubt, as well as the absence of good existence theorems,
that explain why Borel subgroups play only a relatively effaced role in the study of general group schemes from the
scheme-theoretic point of view, while they will dominate the theory of semisimple group schemes in the later exposés.

**Proposition 4.8.** [^N.D.E-XIV-5] *Let `G` be a smooth `S`-prescheme in groups of finite presentation with connected
fibers, `B` a Borel subgroup of `G`; then `B` is identical to its own normalizer, and is a closed subprescheme of `G`.*

<!-- label: III.XIV.4.8 -->

Indeed, by virtue of (XII 7.10), one is reduced to proving that over an algebraically closed field `k`, every element
of `G(k)` that normalizes `B` is in `B(k)`, which for `G` affine is a fundamental result of Chevalley (*Bible* 9 th. 1);
the general case reduces to it at once by the reduction already used in 4.2.

**Remark 4.8.1.** One can generalize Definition 4.5 by also introducing the notion of parabolic subgroup of `G`: one
calls thus a subprescheme in groups `P` of `G`, smooth and of finite presentation over `S`, such that for every
`s ∈ S`, the geometric fiber `P_s` is a parabolic subgroup of `G_s`, i.e. contains a Borel subgroup of `G_s`. <!--
original page 327 --> Proposition 4.8 extends (with the same reduction proof to the "set-theoretic" statement, which is
known) to the case of a parabolic subgroup `P` of `G`. Let us note the following consequence of this result (cf. XVI).
If `P` is a parabolic subgroup of `G`, then `G/P` is representable by a quasi-projective prescheme of finite
presentation over `S` (N.B. one assumes `G` to have connected fibers). Moreover `G/P` is evidently smooth over `S`, and
moreover with connected and proper geometric fibers, whence one can conclude easily, using (EGA III 5.5.1), that
`D = G/P` is in fact proper, hence projective, over `S`. Moreover, if its relative dimension is `n`, it is known that
the invertible sheaf `Ωⁿ_{D/S}` is such that its inverse induces on the geometric fibers of `D/S` ample sheaves, hence
(EGA III 4.7.1) `(Ωⁿ_{D/S})⁻¹` is ample on `D` relative to `S`.

<!-- label: III.XIV.4.8.1 -->

One sees easily, by reduction to the affine case and to the case of an algebraically closed base field, that if
`u : G → G′` is an epimorphism of smooth algebraic groups, then for every Borel subgroup `B` of `G`, `u(B) = B′` is a
Borel subgroup of `G′`. We are interested in the case where one obtains in this way a bijective correspondence between
Borel subgroups of `G` and of `G′`:

**Proposition 4.9.** *Let `G`, `G′` be two smooth `S`-preschemes in groups of finite presentation with connected fibers,
`u : G → G′` a faithfully flat (i.e. surjective) homomorphism of groups [^N.D.E-XIV-6]. Suppose one is in one of the
following two cases (where one has set `N = Ker u`):*

<!-- label: III.XIV.4.9 -->

*a) `N` is central in `G`.*

*b) `S` is the spectrum of a field `k`, and if `k̄` denotes an algebraic closure of it, `N_{k̄} = Ker u_{k̄}` is contained
in the radical of `G_{k̄}`, i.e. in the largest smooth connected solvable invariant subgroup of `G_{k̄}`.*

*Then the map `B′ ↦ u⁻¹(B′)` induces a bijection of the set of Borel subgroups of `G′` with the analogous set for `G`.*

Case b) follows at once from the correspondence between algebraic subgroups of `G′` and algebraic subgroups of `G`
containing `N`, and from the fact that when `k` is <!-- original page 328 --> algebraically closed, the Borel subgroups
of `G` contain the radical of `G` (which is immediate by the reasoning preceding 4.2).

Let us prove case a). By virtue of (XII 7.12), the map `H′ ↦ H = u⁻¹(H′)` establishes a bijective correspondence
between subpreschemes in groups `H′` of `G′` that are smooth of finite presentation over `S`, with connected fibers,
and that have at every `s ∈ S` the same reductive rank and the same nilpotent rank as `G′`, and the subpreschemes in
groups `H` of `G` having the analogous properties. Now Borel subgroups (of `G′`, or of `G`) have the properties in
question. It remains to prove that if `H′`, `H` correspond, then `H′` is a Borel subgroup of `G′` if and only if `H` is
one of `G`. By definition, this question reduces to the case where `S` is the spectrum of an algebraically closed
field. Now since `N` is central in `G` hence in `H`, it follows that `H` is solvable if and only if `H′` is. Finally,
taking the correspondence between algebraic subgroups of `G′` and algebraic subgroups of `G` containing `N` into
account, one sees at once that `H′` has the maximal character of Definition 4.1 if and only if `H` does, which
completes the proof.

**Corollary 4.10.** *With the notations of 4.7, if `B′` and `B` are Borel subgroups of `G′` and `G` which correspond,
one has*

<!-- label: III.XIV.4.10 -->

```text
𝔟 = Lie(u)⁻¹(𝔟′)
```

*where `𝔤`, `𝔤′`, `𝔟`, `𝔟′` are the Lie algebras of `G`, `G′`, `B`, `B′`, and where `Lie(u) : 𝔤 → 𝔤′` is the
homomorphism deduced from `u`.*

This statement follows trivially from the definitions and from the relation `u⁻¹(B′) = B`.

We can now prove the principal result of the present section:

**Theorem 4.11.** *Let `G` be a smooth algebraic group over an algebraically closed field `k`, `𝔤` its Lie algebra. Then
`𝔤` is equal to the union of the Lie algebras `𝔟` of the Borel subgroups `B` of `G`.*

<!-- label: III.XIV.4.11 -->

<!-- original page 329 -->

One may evidently suppose `G` connected. Let `R` be the radical of `G` and let `G′ = G/R`. Then 4.9 b) and 4.10 reduce
us to proving Theorem 4.11 for `G′` instead of `G`, i.e. one may suppose `G` semisimple. Let then `Z` be the center of
`G`, identical to the reductive center, and let `G′ = G/Z`. The same reasoning (now using 4.9 a)) reduces us to proving
the theorem for `G′`, i.e. one may suppose `G` semisimple adjoint. Let `B` be a Borel of `G`, `T` a maximal torus of
`B` hence of `G`, and let `𝔟` and `𝔱` be the Lie algebras. By virtue of 3.18, `T` is a subgroup of type (C) of `G`,
i.e. `𝔱` is a Cartan subalgebra of `𝔤`, hence the union of the conjugates of `𝔱` is dense in `𝔤` (XIII 5.1 (i) ⇒ (vii)).
*A fortiori* the union of the conjugates of `𝔟` is dense in `𝔤`. Now let `X` be the closed subscheme of `G/B × W(𝔤)`
whose `k`-valued points are the `(g′, x)` such that `x ∈ Ad(g) · 𝔟` (cf. XIII 1). Then the morphism `ψ : X → W(𝔤)`
induced by the second projection is proper since `G/B` is proper over `k`; on the other hand we have just seen that it
is dominant, hence it is surjective, which proves 4.11.

The only result of the present section that we shall use in the rest of this exposé is the following corollary:

**Corollary 4.12.** *Let `k` be an infinite field, `G` a smooth algebraic group over `k`, `T` a maximal torus of `G`,
`𝔤` and `𝔱` the Lie algebras, `u : G → GL(V)` a linear representation (`V` a finite-dimensional vector space over `k`),
whence a representation of Lie algebras `u′ : 𝔤 → 𝔤𝔩(V)`, making `V` into a `𝔤`-module. Then the minimum of the nullity
of `u′(x)` (`x ∈ 𝔤`) is attained for an element `x ∈ 𝔱`.*

<!-- label: III.XIV.4.12 -->

One is reduced at once to the case where `k` is algebraically closed. One may evidently suppose `G` connected, and
replacing `G` by `G/(Ker u)_{red}` if necessary, one may suppose `G` affine. Using 4.11 and the conjugation theorem of
maximal tori of `G`, one is reduced to the case where `G` is moreover solvable. Then `G` is a semidirect product
`T · V`, where `V` is the "unipotent part" of `G`, which is a smooth connected unipotent group (*Bible* 6 th. 3). Hence
`𝔤` is the direct sum (as a vector space) of the Lie subalgebras `𝔱` and `𝔳 = Lie(V)`. <!-- original page 330 --> By
virtue of the Lie-Kolchin theorem (*Bible* 6 th. 1), `𝔳` admits a composition series by stable subspaces `𝔳_i` such that
`𝔳_i/𝔳_{i+1} = w_i` is of dimension 1. Then for each `i`, one has an induced representation `u_i : G → GL(w_i) = G_m`
and the corresponding homomorphism of Lie algebras `u′_i : 𝔤 → k`, so that for every `x ∈ 𝔤`, the nullity of `u′(x)` is
equal to the number of `i` such that `u′_i(x) = 0`. Since `V` is unipotent, the `u_i` are trivial on `V`, hence the
`u′_i` are trivial on `𝔳`, which proves that if `x = t + v` (`t ∈ 𝔱`, `v ∈ 𝔳`), then `u′_i(x) = u′_i(t)` for all `i`,
hence the nullity of `u′(x)` is equal to that of `u′(t)`. Assertion 4.12 follows at once.

[^N.D.E-XIV-4]: Where `𝔟` is the Lie algebra of `B`.

[^N.D.E-XIV-5]: There is no number 4.7.

[^N.D.E-XIV-6]: Add a reference here?

## 5. Relations between Cartan subgroups and Cartan subalgebras

<!-- label: III.XIV.5 -->

Applying 4.12 to the adjoint representation of `G`, one finds:

**Theorem 5.1.** *Let `G` be a smooth algebraic group over an infinite field, `T` a maximal torus of `G`, `𝔤 ⊃ 𝔱` the
Lie algebras; then `𝔱` contains a regular element of `𝔤`.*

<!-- label: III.XIV.5.1 -->

**Corollary 5.2.** *Let `G` be a smooth `S`-prescheme in groups of finite presentation, `𝔤` its Lie algebra.*

<!-- label: III.XIV.5.2 -->

*a) Conditions (C₀) to (C₂) of 2.9 on `𝔤` are equivalent; in particular, if the infinitesimal rank of the fibers of `𝔤`
at the points of `S` is locally constant, then `𝔤` admits locally for the étale topology a Cartan subalgebra, hence
(by 3.9 a)) `G` admits locally for the étale topology a subgroup of type (C).*

*b) Let `H` be a subprescheme in groups of `G` smooth of finite presentation over `S`, with connected fibers having the
same reductive rank as `G` at each `s ∈ S` (for example, `H` is a maximal torus or a Cartan subgroup of `G`); let `D`
be a subgroup of type (C) of `G`; then one has `H ⊂ D` if and only if one has `𝔥 ⊂ 𝔡`.*

*c) Suppose condition (C₀) is satisfied, i.e. the infinitesimal rank of `G` is locally constant. Let `H` be a
subprescheme in groups of `G` smooth of finite presentation over `S`, with connected nilpotent fibers having the same
reductive rank as `G` at each point (for example, `H` is a maximal torus or a Cartan subgroup of `G`). Then `H` is
contained in one and only one subgroup `D` of type (C) of `G`.*

*d) Suppose that `G` admits locally for fpqc a Cartan subgroup; then the same is true of every subgroup `D` of type (C)
of `G`.*

<!-- original page 331 -->

*Proof.* a) Suppose condition (C₀) is satisfied, and let us prove that the same is true of (C₂), i.e. that every
quasi-regular section `a` of `𝔤` is regular. One reduces as usual to the case `S` affine noetherian, then, the question
being "infinitesimal" (2.15 b)), to the case where `S` is local artinian (in which case (C₀) is moreover trivially
satisfied). One may suppose moreover that the residue field `k` of `S` is infinite. Note that by virtue of 3.7 it
suffices to establish that `𝔤` admits a Cartan subalgebra. Let `T` be a maximal torus of `G`; by virtue of 5.1 there
exists a quasi-regular element `t` contained in the Lie algebra `𝔱` of `T`; let us prove that it is regular, which will
complete the proof. Consider the linear representation of `T` in `𝔤` induced by the adjoint representation of `G`; there
exists therefore a finite set `(u_i)_{i ∈ I}` of characters of `T`, such that `𝔤` decomposes as a direct sum of
submodules `𝔤_i` stable under `T`, `T` operating on `𝔤_i` by `u_i` (cf. I § 4.7.3). Let `u′_i : 𝔱 → A` be the homomorphism
of Lie algebras deduced from `u_i : T → G_m` (N.B. `A` denotes the ring of `S`). Consider the homomorphisms `u_{i0}`
and `u′_{i0}` deduced from the preceding by passage to the fibers, i.e. by the base change `A → k`. Let `I′` be the set
of `i ∈ I` such that `u′_{i0} ≠ 0`, and let `I″ = I − I′`. The fact that `t` is regular is expressed by the condition
`u′_{i0}(t₀) ≠ 0` for all `i ∈ I′`, hence `u′_i(t)` invertible for `i ∈ I′`. The Cartan subalgebra of `𝔤₀` defined by
`t`, i.e. the kernel subspace of the semisimple endomorphism `ad(t₀)` of `𝔤₀`, is `∑_{i ∈ I″} (𝔤_i)₀`. Consider

```text
𝔡 = ∑_{i ∈ I″} 𝔤_i;
```

then `ad(t)` is nilpotent in `𝔡`; on the other hand it is an automorphism of `𝔤/𝔡 ≃ ∑_{i ∈ I′} 𝔤_i`. <!-- original page
332 --> By virtue of 2.6, `t` is therefore regular.

b) Follows from 3.12 a), `H` satisfying the hypothesis that every geometric fiber of `𝔥` contains a regular element of
that of `𝔤`, thanks to 5.1.

c) By virtue of b), one is reduced to proving that `𝔥` is contained in one and only one Cartan subalgebra of `𝔡`. By
virtue of a) we know moreover that `𝔤` satisfies (C₂). One is thus reduced to the:

**Lemma 5.3.** *Let `𝔤` be a Lie algebra over `S` that is a locally free module of finite type and satisfies condition
(C₂) of 2.9. Let `𝔥` be a Lie subalgebra of `𝔤` satisfying the following conditions: it is a locally direct factor
module, it is locally nilpotent, and for every `s ∈ S`, the geometric fiber `𝔥_s` contains a regular element of `𝔤_s`.
Then `𝔥` is contained in one and only one Cartan subalgebra of `𝔤`.*

<!-- label: III.XIV.5.3 -->

(N.B. in the case of interest to us, `𝔥` satisfies the stated conditions: it is locally nilpotent because `H` has
nilpotent fibers, and the condition on regular elements follows from 5.1.) Since 5.3 is local for the fpqc topology, it
suffices to prove that at a point `s ∈ S` such that `κ(s)` is infinite, there exists an open neighborhood `U` of `s`
such that existence and uniqueness hold for every base change `S′ → S` factoring through `U`. Take a regular element of
`𝔤 ⊗ κ(s)` contained in `𝔥 ⊗ κ(s)`, extend it to a section `a` of `𝔥` on an open neighborhood `U` of `s`; thanks to (C₂)
one may suppose this section is regular (2.10). One may suppose `U = S`. A Cartan subalgebra of `𝔤` containing `𝔥`
contains `a`, hence is identical to `𝔡 = Nil(a, 𝔤)` (2.6), whence uniqueness. Moreover since `𝔥` is locally nilpotent,
one indeed has `𝔥 ⊂ 𝔡`, which proves existence.

d) Is a particular case of (XII 7.9 d)).

<!-- original page 333 -->

**Corollary 5.4.** *Let `G` be a smooth and connected algebraic group over an algebraically closed field `k`, `H` a
connected algebraic subgroup such that `𝔥` contains a Cartan subalgebra of `𝔤`, i.e. such that `H` contains a subgroup
of type (C) of `G`. Then the number of conjugates of `H` containing a regular element of `G(k)` is equal to the number
of conjugates of `𝔥` containing a regular element of `𝔤`.*

<!-- label: III.XIV.5.4 -->

Indeed, let `g` be a regular element of `G(k)`, `C` the unique Cartan subgroup of `G` containing `g` (XIII 2); then the
conjugates of `H` containing `g` are those containing `C` (XIII 2.8 b)). Similarly, let `x` be a regular element of
`𝔤`; then if a conjugate `𝔥′` of `𝔥` contains `x`, then `ad(x)_{𝔤/𝔥′}` is injective (XIII 5.4), hence `𝔥′` contains
`Nil(x, 𝔤) = 𝔡`, hence the number of conjugates of `𝔥` containing `x` is equal to the number of conjugates containing
the Cartan subalgebra `𝔡`. Moreover `𝔡` is the Lie algebra of a subgroup `D` of type (C) of `G`. One may evidently
suppose `C ⊂ D`, and assertion 5.4 will follow from this: in order for `H` to contain `C`, it is necessary and
sufficient that `𝔥` contain `𝔡`. Indeed, by virtue of (XIII 5.5) the relation `𝔥 ⊃ 𝔡` implies `H ⊃ D` and *a fortiori*
`H ⊃ C`. Conversely, by 5.1 `𝔱` contains a regular element `x` of `𝔤`; then `H ⊃ C` implies `𝔥 ∋ x`, hence as already
pointed out, this implies `𝔥 ⊃ 𝔡`. This completes the proof.

Let `G` be as in 5.2 and suppose that the infinitesimal rank of the fibers of `G` remains locally constant (condition
(C₀)). Then thanks to 5.2 c), one finds a homomorphism of functors on `(Sch)°/S`:

```text
𝒞 ⟶ 𝒟
```

where

```text
𝒞(S′) = set of Cartan subgroups of G_{S′}
𝒟(S′) = set of subgroups of type (C) of G_{S′}.
```

<!-- original page 334 -->

By virtue of 3.10 and 5.2 a), `𝒟` is representable by a smooth and quasi-projective prescheme over `S`. Consider the
subgroup `D` of type (C) of `G_𝒟` playing the universal role with respect to `G/S`; one may then consider the functor
`𝒞_D : (Sch)°/𝒟 → (Ens)` defined in terms of the `𝒟`-group `D` as `𝒞` in terms of the `S`-group `G`. One then has the
following result:

**Proposition 5.5.** *Under the preceding conditions, considering `𝒞` as a functor over the prescheme `𝒟`, then `𝒞` is
`𝒟`-isomorphic to the functor `𝒞_D` "of Cartan subgroups of `D`".*

<!-- label: III.XIV.5.5 -->

This follows at once from the:

**Corollary 5.6.** *Let `G` be a smooth `S`-prescheme in groups of finite presentation, `D` a subgroup of type (C) of
`G`. Then there is a bijective correspondence between Cartan subgroups of `G` contained in `D`, and Cartan subgroups
of `D` (more precisely, for a subgroup `H` of `G`, `H` is a Cartan subgroup of `G` if and only if it is a Cartan
subgroup of `D`).*

<!-- label: III.XIV.5.6 -->

Indeed, this is a particular case of (XII 7.9 c)), taking into account that over an algebraically closed field, a
subgroup of type (C) of `G` contains a Cartan subgroup of `G`.

For the following section, the main result obtained here is 5.2 c) for `H` a Cartan subgroup of `G`, which permits
stating 5.5 and thus furnishes a useful "dévissage" of `𝒞`.

## 6. Applications to the structure of algebraic groups

<!-- label: III.XIV.6 -->

**Theorem 6.1.** *Let `G` be a smooth algebraic group over a field `k`. Consider the scheme `𝒯` of maximal tori of `G`,
isomorphic to the scheme `𝒞` of Cartan subgroups of `G`, which is a homogeneous space under `G⁰`, and a smooth affine
connected algebraic scheme (XII 7.1 d)). Then `𝒞` is a rational variety, i.e. the field of rational functions of `𝒞` is
a pure extension of `k`.*

<!-- label: III.XIV.6.1 -->

We shall first give the proof in the case where `k` is infinite. One may evidently <!-- original page 335 --> suppose
`G` connected, since `𝒯` hence `𝒞` does not change on replacing `G` by `G⁰`. Moreover, by virtue of (XII 7.6), `𝒞` does
not change on dividing `G` by a central subgroup. This allows us, first dividing by the center of `G`, to suppose `G`
affine (XII 6.1), then, dividing by its reductive center (XII 4.1 and 4.4), to suppose that the reductive center of
`G` is trivial (XII 4.7 b)). Moreover we proceed by induction on `n = dim G`, supposing the theorem proved for
dimensions `n′ < n`. If `G` is nilpotent, then `𝒞` is reduced to a single point rational over `k`, and 6.1 is trivial.
In the contrary case, the Lie algebra of `G` is non-nilpotent (1.3), hence the Cartan subalgebras of `𝔤` are of
dimension `n′ < n`, hence the subgroups of type (C) of `G` are of dimension `n′ < n`. Consider then the morphism

```text
𝒞 ⟶ 𝒟
```

envisaged in 5.5. We know by 3.10 (`k` being an infinite field, hence `𝔤` containing a regular element) that `𝒟` is a
rational variety, i.e. the field `K` of rational functions on `𝒟` is a pure extension of `k`. Consider the fiber of `𝒞`
over the generic point `x` of `𝒟`; by virtue of 5.5 this is the scheme of Cartan subgroups of a certain smooth and
connected algebraic group `D_x` over `K = κ(x)` (namely `D_x = ` "the generic subgroup of type (C) of `G`"). The field
`L` of rational functions on `𝒞` is therefore isomorphic to the field of rational functions on `𝒞_{D_x}`, which by the
induction hypothesis (since `dim D_x = n′ < n`) is a pure extension of `K`. So by transitivity `L` is a pure extension
of `k`.

When `k` is finite, a different proof is needed. One may still suppose `G` is affine and connected. Note that `k` is
perfect; it follows at once that the radical `R` of `G_{k̄}` is "defined over `k`", i.e. comes from a subgroup `R` of
`G`. Suppose first `R ≠ G`, i.e. `G` non-solvable, and let

```text
u : G ⟶ G′ = G/R
```

<!-- original page 336 -->

be the canonical morphism. Consider the corresponding morphism `C ↦ u(C)`

```text
v : 𝒞_G ⟶ 𝒞_{G′}
```

(whose definition is immediate by virtue of (XII 7.1 e))). Let `x` be the generic point of `𝒞_{G′}`; then the fiber
`v⁻¹(x)` is identified with the scheme of Cartan subgroups of `G_K` (where `K = κ(x)`) whose image in `G′_K` is a
certain Cartan subgroup `C′_x` (namely, "the generic Cartan subgroup of `G′`"). It is therefore also the scheme of
Cartan subgroups of `H = u⁻¹_K(C′)` (XII 7.9 c)), and since `K` is here an infinite extension of `k`, it follows from
the already proved part of 7.1 that the field `L` of rational functions of `𝒞_G`, equal to that of `𝒞_H`, is a pure
transcendental extension of `K`. To prove that it is a pure transcendental extension of `k`, it therefore suffices to
prove that this is the case of `K`, i.e. one is reduced to the case where `G` is semisimple. One may moreover suppose
that `G` is adjoint (dividing `G` by its reductive center if necessary). But then by virtue of 3.18 one has
`𝒞_G ≃ 𝒟_G`, and by virtue of 3.10 it suffices to prove that `𝔤` admits a regular point, which (as was pointed out in
3.20) is an unpublished result of Chevalley [^N.D.E-XIV-7].

It only remains to treat the case where `k` is finite, `G` connected affine solvable. One in fact has a more general
result:

**Corollary 6.2.** *Let `G` be a smooth solvable algebraic group over a field `k`; then the variety `𝒞` of Cartan
subgroups of `G` is isomorphic to an affine space `Spec k[t₁, …, t_N]`.*

<!-- label: III.XIV.6.2 -->

One may still suppose `G` connected and affine. Let `G_∞` be the smallest of the groups appearing in the descending
central series of `G` (by `G_i` such that `G_{i+1} = [G, G_i]`); it is thus the smallest invariant algebraic subgroup
of `G` such that `G/G_∞` is nilpotent. Let `C` be a Cartan subgroup of `G` (it exists by virtue of 1.1); then the image
of `C` in `G/G_∞` is a Cartan subgroup of it, hence is equal to `G/G_∞`, consequently the morphism `g ↦ Ad(g) · C` of
`G_∞` into `𝒞` is an epimorphism, and identifies <!-- original page 337 --> `𝒞` with the homogeneous space
`G_∞/N ∩ G_∞`, where `N` is the normalizer of `C` in `G` (moreover equal to `C` as we recalled in 4.4, but this is of
little importance here). Note that `U = G_∞` is evidently a smooth connected "unipotent" algebraic group (since over
the algebraic closure of `k`, it is contained in the unipotent part of `G`, by virtue of the known structure of smooth
affine solvable groups, *Bible* 6 th. 3). When `k` is perfect (the only case needed to establish 6.1), it follows very
easily that `U` is even `k`-unipotent, i.e. admits a composition series by algebraic subgroups `U_i` such that
`U_i/U_{i+1}` is isomorphic to `G_a`. In fact, Rosenlicht has proved that this result remains valid for a group of the
form `G_∞` as above, without restriction on `k` (M. Rosenlicht, *Questions of rationality for solvable algebraic groups
over non perfect fields*, Annali di Matematica 1963, pp. 97–120, theorem 4 cor. 2), a result clearly more delicate which
we shall admit here. It now suffices to apply the following lemma, doubtless well known to specialists:

**Lemma 6.3.** *Let `U` be a smooth connected algebraic group over a field `k`, `X = U/V` a homogeneous space under `U`
having a rational point over `k`. Suppose `U` is `k`-unipotent. Then as a `k`-scheme, `X` is isomorphic to an affine
space `Spec k[t₁, …, t_N]`.*

<!-- label: III.XIV.6.3 -->

Indeed, let `(U_i)_{0 ⩽ i ⩽ n}` be a composition series of `U` by smooth connected subgroups, with `U_n = (e)`,
`U_0 = U`, `U_i/U_{i+1} ≃ G_a`, the `U_i` invariant in `U`. Then the `K_i = U_i V` are algebraic subgroups of `U` (not
necessarily smooth nor connected if `V` is not, but no matter), and `K_{i+1}` is invariant in `K_i`. One has a canonical
morphism `U_i/U_{i+1} → K_i/K_{i+1}` that is an epimorphism, which proves that `K_i/K_{i+1}` is either reduced to the
unit group, or isomorphic to `G_a/H_i`, where `H_i` is a finite subgroup of `G_a`, which by virtue of Rosenlicht (loc.
cit., th. 2) implies that `K_i/K_{i+1} ≃ G_a` (a result moreover immediate if `k` is perfect). Set now `X_i = U/K_i`;
let us prove by induction on `i` that `X_i` is isomorphic to an affine space. Indeed, if this is so for `X_i`, let us
prove that the same is true of `X_{i+1}`. If `K_i/K_{i+1} = e` one has `X_i = X_{i+1}` and this is trivial. Otherwise,
`X_{i+1}` is a principal bundle with base `X_i` and structure group `G_a ≃ K_i/K_{i+1}`. <!-- original page 338 --> So,
`X_i` being affine, `X_{i+1}` is a trivial bundle, hence is isomorphic to `X_i × G_a`, which again proves that
`X_{i+1}` is isomorphic to an affine space. This proves 6.2 and consequently completes the proof of 6.1.

**Corollary 6.4.** *Let `G` be a smooth algebraic group over an infinite field `k`. Then the set of `k`-rational points
of `𝒞` (notations of 6.1) is dense for the Zariski topology. The union of the Cartan subgroups of `G` is dense in `G`.*

<!-- label: III.XIV.6.4 -->

The first assertion is valid for any unirational variety over an infinite field, and is moreover the most important
"arithmetic" consequence of the unirationality results for us here. The second assertion follows from the first and
from the density theorem (XIII 2.1).

**Corollary 6.5.** *Let `G` be a smooth connected algebraic group over `k`. Then the variety `Z` of regular semisimple
points of `G` (XIII 3.5) is a unirational variety. In particular, if `k` is infinite, the set of `k`-rational points of
`Z` is dense in `Z`.*

<!-- label: III.XIV.6.5 -->

Indeed, `Z` is an open of a torus over `𝒞`, hence its function field `L` is the function field of a torus defined over
the function field `K` of `𝒞` (namely the "generic maximal torus" of `G`); it is therefore a unirational extension of
`K` (XIII 3.4), and since `K` is a pure extension of `k` by virtue of 6.1, `L` is a unirational extension of `k`.

**Corollary 6.6.** *Let `G` be a smooth connected algebraic group over `k`, and let `H` be the subgroup of `G`
generated by the subvariety `Z` of regular semisimple points, i.e. (XII 8.2) the smallest invariant algebraic subgroup
of `G` such that `G/H` has reductive rank zero (i.e. is, over the algebraic closure of `k`, an extension of an abelian
variety by a smooth connected unipotent group). Then `H` is a unirational variety. In particular, if `G = H`, i.e.
(XII 8.4) if `G` is affine and if over the algebraic closure `k̄`, <!-- original page 339 --> there exists no non-trivial
homomorphism of `G_{k̄}` to `G_a`, then `G` is a unirational variety, hence if `k` is infinite, the set of its
`k`-rational points is dense.*

<!-- label: III.XIV.6.6 -->

This follows at once from 6.5, for it is immediate that if one has smooth connected `k`-preschemes `Z_i` that are
unirational varieties and morphisms `u_i : Z_i → G`, then the algebraic subgroup of `G` generated by the `u_i` (VI_B
7.1) is a unirational variety.

As an interesting particular case of 6.5 or 6.6 (whichever one chooses), let us note:

**Corollary 6.7.** *Let `G` be a smooth connected affine algebraic group of unipotent rank zero; then `G` is a
unirational variety.*

<!-- label: III.XIV.6.7 -->

One can refine 6.4 as follows:

**Corollary 6.8.** *Let `G` be a smooth connected algebraic group over the infinite field `k`, and let `C` be a Cartan
subgroup of `G`. Then the union of the conjugates of `C` by regular semisimple elements of `G(k)` is dense in `G`.*

<!-- label: III.XIV.6.8 -->

This follows at once from 6.4 and from (XIII 3.6), which says that the morphism `ϕ : Z × C → G` defined by
`ϕ(t, c) = ad(t)c` is dominant. This result also implies (without supposing `k` infinite):

**Corollary 6.9.** *Let `G` be a smooth connected algebraic group over `k`, `H` a smooth connected algebraic subgroup
of `G` such that `H` has the same reductive rank and the same nilpotent rank as `G` (i.e. over the algebraic closure
`k̄` of `k`, `H_{k̄}` contains a Cartan subgroup of `G_{k̄}`). If `H` is a unirational variety, the same is true of `G`.
If `H(k)` is dense in `H`, `G(k)` is dense in `G`.*

<!-- label: III.XIV.6.9 -->

Indeed, the morphism `ϕ : Z × H → G` defined by `ϕ(t, h) = ad(t)h` is dominant. Now by virtue of 6.5, `Z` is a
unirational variety, and by hypothesis the same is true of `H`, hence of `Z × H`, whence the first result. The second
is proved analogously.

We now recover the following well-known result (due to Chevalley, in characteristic 0, to Rosenlicht in characteristic
`p > 0`):

<!-- original page 340 -->

**Corollary 6.10.** *Let `G` be a smooth connected affine algebraic group over a perfect field `k`. Then `G` is a
unirational variety, hence if `k` is moreover infinite, `G(k)` is dense in `G`.*

<!-- label: III.XIV.6.10 -->

Indeed, by virtue of 1.1, `G` admits a Cartan subgroup `C`. By virtue of 6.9 it suffices to prove that this latter is a
unirational variety. Now `k` being perfect, one sees at once by Galois descent from the case `k` algebraically closed
(*Bible* 6 th. 2) that one has `C = T × C_u`, where `T` is the maximal torus of `C` and `C_u` a smooth connected
unipotent group. One already knows that `T` is a unirational variety (XIII 3.4); it remains to see that the same is
true of `C_u`. Now `k` being perfect, `C_u` is even `k`-unipotent, and one may apply 6.3.

**Remarks 6.11.** a) One knows (Rosenlicht) examples of twisted forms of `G_a` over a non-perfect field that have only
finitely many rational points, hence *a fortiori* are not unirational varieties. On the other hand, Chevalley has given
an example of a torus over a field of characteristic zero that is not a rational variety. By contrast, it follows from
Chevalley's theory of semisimple groups that over an algebraically closed field, every smooth connected affine
algebraic group is a rational variety. Let us note moreover that the question of unirationality only arises in any
event for affine algebraic groups, a unirational algebraic group being necessarily affine by Chevalley's structure
theorem.

<!-- label: III.XIV.6.11 -->

b) With the notations of 6.6, it is tempting to try to give a unirationality condition on `G` in terms of the group
`G/H` (which is unipotent if `G` is supposed affine). It is evidently necessary that this latter be unirational; is
this condition also sufficient? Note that an example of Rosenlicht (loc. cit.) shows that a smooth connected unipotent
algebraic group `U` may be a rational variety without being `k`-unipotent.

c) It would be interesting to study, over a finite field `k`, questions of the "density" type, such as the following
(raised by Rosenlicht): Let `G` be a smooth and connected algebraic group <!-- original page 341 --> over `k`; is `G`
generated by its Cartan subgroups? [^XIV-6-1] [^N.D.E-XIV-8]

In this question, one can reduce to the case `G` affine, by dividing by the center. The answer would be affirmative in
the semisimple case, if one could refine the existence result for regular points of Chevalley pointed out in 3.20, so
as to obtain a regular element of `𝔤` that does not belong to `𝔥 = Lie(H)`, where `H` is a smooth algebraic subgroup of
`G` and `≠ G` given in advance (`G` an adjoint semisimple group over the finite field `k`).

[^N.D.E-XIV-7]: Cf. the Appendix, by J.-P. Serre.

[^XIV-6-1]: This question has since been resolved affirmatively by Steinberg.

[^N.D.E-XIV-8]: Not having identified this result in the *Collected Papers* of R. Steinberg, we give a proof based on
the Bruhat decomposition. Let `G/k` be a semisimple group defined over the finite field `k`. The point is to show that
`G` is generated by its `k`-Cartan subgroups. This question is stable by central isogeny and by restriction of scalars;
one is therefore reduced to the case where `G` is geometrically simple (in the same way as in Lemma 1 of the appendix
below). Denote by `G♯` the subgroup of `G` generated by its `k`-subtori. The group `G` is quasi-split (Lang) and
therefore admits a Killing couple `(T, B)`. By definition, one has `T ⊂ G♯`; in particular `T` normalizes `G♯`. The big
cell `R_u(B⁻) T R_u(B)` of `G` indicates that it suffices to verify that `R_u(B) ⊂ G♯`. Let `S` be the maximal split
`k`-torus of `T`. One considers the relative root system `Φ(G, S)` and a basis `Δ_k`. Given `α ∈ Φ(G, S)`, denote by
`U_(α)` the unipotent subgroup associated to `α` (cf. A. Borel, *Linear Algebraic Groups*, second edition (1991),
Springer, Prop. 21.9). Since the `k`-group `R_u(B)` is generated by the `k`-unipotent groups `U_(α)` (`α ∈ Δ_k`), one
is reduced to verifying that `U_(α) ⊂ G♯`. A glance at the classification shows that there exists a semisimple group
`G_α` of quasi-split type `A₁`, `²A₁`, `³A₁` or `²A₂` such that `U_(α) ⊂ G_α ⊂ G`. It is therefore permissible to
suppose that `G = PGL₂` or `G = SU₃(K)`, where `K` denotes the unique quadratic extension field of `k`. The group
`PGL₂^♯` containing the standard split torus `T`, the possibilities up to conjugation under `G(k)` are the following:
`PGL₂^♯ = T`, `PGL₂^♯ = B`, or `PGL₂^♯ = PGL₂`. The case `PGL₂^♯ = T` is excluded since `PGL₂^♯` contains the `k`-torus
`R_{K/k}(G_m)/G_m`. The preceding discussion indicates that if `PGL₂^♯ = B`, then `PGL₂^♯ = PGL₂`. Hence
`PGL₂^♯ = PGL₂`. If `G = SU₃(K)`, `Δ_k = {α}` and the possibilities for `G♯` (up to conjugation) are the following:
`G♯ = T`, `G♯ = B`, `G♯ = U_(2α) ⋊ T`, `G♯ = ⟨U_(2α), U_(−2α), T⟩ = SL₂ · T`, or `G♯ = G`. The case `G♯ = B` is excluded
as for `PGL₂`. The case `SL₂ · T` is excluded because `G♯` contains the `k`-torus `R¹_{K/k}(R¹_{K₃/K}(G_m))`, `K₃/K`
denoting the extension of degree 3 of `K`, and the isogeny class of this torus is irreducible. Moreover, this torus
also excludes the cases `G♯ = T` and `G♯ = U_(2α) ⋊ T`. One concludes that `G♯ = G`.

## Appendix. Existence of regular elements over finite fields

<!-- label: III.XIV.7 -->

*by J.-P. Serre*

<!-- original page 342 -->

In all that follows, `k` denotes a finite field, and `k̄` its algebraic closure; the Galois group of `k̄/k` is denoted
`𝒢`; one recalls that, if `q = Card(k)`, `𝒢` is topologically generated by the "Frobenius" element `F : x ↦ x^q`.

We propose to prove the following theorem [^XIV-A-1]:

**Theorem.** *Let `G` be an adjoint semisimple group defined over `k`, and let `𝔤` be its Lie algebra. The `k`-Lie
algebra `𝔤(k)` contains a regular element.*

<!-- label: III.XIV.7.theorem -->

**Remarks.** (1) It is well to recall that "adjoint" means that the center of `G` is trivial (as a subgroup scheme of
`G`). In view of the Chevalley seminar, this also means that, if `T` is a maximal torus of `G`, the group `X(T)` of
characters of `T` (defined over `k̄`) is generated by the set `R` of roots. It follows in particular that the rank of
the Lie algebra `𝔤` is equal to the dimension of `T` (i.e. to the rank of `G`).

(2) The editor does not know whether the hypothesis that `G` is adjoint is indispensable.

**Lemma 1.** *It suffices to prove the theorem when `G` is geometrically simple.*

<!-- label: III.XIV.7.lemma-1 -->

(One says that `G` is geometrically simple if `G ⊗ k̄` does not contain any normal subgroup scheme smooth over `k̄`,
apart from `G` and `{e}`; an equivalent condition: the associated root system `R` is irreducible.)

One may first suppose `G` indecomposable over `k`. The group `G ⊗ k̄` is then a <!-- original page 343 --> product of
geometrically simple components `S` that are permuted transitively by the Galois group `𝒢`. If `H` is the subgroup of
`𝒢` fixing one of these components `S`, this component is defined over the field `K` corresponding to `H` (i.e. comes
by extension of scalars from a subscheme of `G ⊗ K`), and a standard argument shows that `G = ∏_{K/k}(S)` (i.e.
`R_{K/k}(S)`, for readers used to the notation of Weil). Likewise, the Lie algebra `𝔤` of `G` is identified with
`∏_{K/k} 𝔰`, where `𝔰` is the Lie algebra of `S`. If the theorem is true for `S`, there exists `x ∈ 𝔰(K) = 𝔤(k)` that
is regular in `𝔰`; one then verifies easily that it is regular in `𝔤`. *QED*.

From now on, one supposes `G` geometrically simple and one chooses a maximal torus `T` of `G` (one knows this is
possible). One denotes by `X` the group of characters of `T ⊗ k̄`, `R` its root system, `W` its Weyl group, and `E` the
group of automorphisms of `X` preserving `R`. The group `W` is a normal subgroup of `E`.

If `T′` is another torus of `G`, one denotes by `X′`, `R′`, `W′`, `E′` the group of characters, root system, …,
corresponding. If one chooses `y ∈ G(k̄)` such that `y · (T ⊗ k̄) · y⁻¹ = T′ ⊗ k̄`, one can identify `X′`, `R′`, `W′`,
`E′` with `X`, `R`, `W`, `E` thanks to `int(y)`. Changing `y` modifies this identification by an automorphism of `X`
corresponding to an element of `W`.

The canonical generator `x ↦ x^q` of `𝒢` operates on `X′` while preserving `R′`; it therefore defines an element
`f_{T′}` of `E′`. In particular one sets `f = f_T`. When one identifies `E′` with `E` as just stated, the element
`f_{T′}` is transformed into an element `f′` of `E`, defined up to replacement by `wf′w⁻¹` with `w ∈ W`. We are going
to compare this element to `f`:

**Lemma 2.** *One has `f′ ≡ f mod W`; conversely, every `f′ ∈ E` satisfying this condition can be obtained from a
maximal torus `T′` of `G`.*

<!-- label: III.XIV.7.lemma-2 -->

Set `T̄ = T ⊗ k̄`, `T̄′ = T′ ⊗ k̄`, and let `y ∈ G(k̄)` be such that `yT̄y⁻¹ = T̄′`; since `y^q T̄ y^{-q} = T̄′`, <!-- original
page 344 --> one concludes that `n = y⁻¹ y^q` belongs to the normalizer `N(T)` of `T`. The effect of `f′` on the points
of `T̄(k̄)` is then the following:

```text
f′(t) = y⁻¹(yty⁻¹)^q y = y⁻¹ y^q t^q y^{-q} y = n t^q n⁻¹.
```

If `w ∈ W` is the element defined by `n`, this shows that `f′` and `f ∘ w` have the same effect on the points of `T̄`,
hence also on its characters, and one has `f′ = f ∘ w`, whence `f′ ≡ f mod W`. Conversely, if `w ∈ W` is given, one
represents it by an element `n ∈ N(T)(k̄)`; thanks to a classical theorem of Lang, one can write `n` in the form
`n = y⁻¹ y^q`, with `y ∈ G(k̄)`; the torus `T̄′ = yT̄y⁻¹` is then defined over `k`, and the preceding calculation shows
that the corresponding `f′` is equal to `f ∘ w`.

**Lemma 3.** *Let `X`, `R`, `W`, `E` be as above (`R` being irreducible), and let `ϕ ∈ E/W`. Then there exists an
element `f ∈ E` representing `ϕ`, and a family `θ₁, …, θ_n` of roots enjoying the two following properties:*

<!-- label: III.XIV.7.lemma-3 -->

*(1) `(θ₁, …, θ_n)` is a basis of `X`.*

*(2) `R` is the union of the orbits of the `θ_i` under the powers of `f` (i.e. every `a ∈ R` can be written
`a = f^m θ_i`, with suitable `m` and `i`).*

The proof will be given a little further on.

Here now is a lemma of linear algebra:

**Lemma 4.** *Let `V` be a vector space over `k`, and let `(θ₁, …, θ_n)` be a basis of the dual of `V ⊗ k̄`. There
exists `x ∈ V` such that `θ_i(x) ≠ 0` for all `i`.*

<!-- label: III.XIV.7.lemma-4 -->

Let `V*` be the dual of `V`, and let `W_i` be the subspace of `V* ⊗ k̄` generated by the conjugates of `θ_i`; this
subspace is defined over `k`, i.e. of the form `W_i ⊗ k̄`. The obvious application `W_1 ⊗ ⋯ ⊗ W_n → ∧ⁿ V*` is not zero
(otherwise its extension to `k̄` would be also, which is absurd since `θ_i ∈ W_i` and `θ_1 ∧ … ∧ θ_n ≠ 0`). There exists
therefore a basis of `V*` formed of elements `u_i ∈ W_i`. Let `x ∈ V` be such that `u_i(x) ≠ 0` for all `i` (for
example `u_i(x) = 1`). The element `x` answers the question, for if one had `θ_i(x) = 0`, the conjugates of `θ_i` would
also vanish at `x`, and the same would be true of `u_i`, which is not the case.

<!-- original page 345 -->

**End of the proof of the theorem.**

By combining Lemmas 2 and 3, one can choose a torus `T` whose element `f` satisfies the properties of Lemma 3. If `Y`
is the dual of `X`, the Lie algebra `𝔱(k̄)` of `T` [^N.D.E-XIV-9] is canonically identified with `Y ⊗ k̄`, and this
operation is compatible with the action of the Galois group (the latter operating on `Y ⊗ k̄` thanks to its action on
`Y` and on `k̄`). Let `V = 𝔱(k)` be the Lie algebra of `T` over `k`. An element `x ∈ V` is regular if and only if it is
not annihilated by any root `α ∈ R`, or rather by any of the linear forms `α ∈ V* ⊗ k̄` defined canonically by the
`α ∈ R`. By Lemma 4, one can find such an `x` not annihilated by any of the roots `θ_i`; but every root is conjugate to
a `θ_i` (this is what condition (2) of Lemma 3 expresses); it follows that `x` is not annihilated by any root, and it
is indeed a regular element.

**Proof of Lemma 3.**

It relies on properties of Coxeter transformations. Let us briefly recall what this involves:

Let `a_1, …, a_n` be a simple root system of `R`, and, for every `i`, let `r_i` be the symmetry corresponding to `a_i`.
Set:

```text
c = r_1 ⋯ r_n.
```

One has `c ∈ W`; of course the element `c` depends on the choice of the simple system `(a_1, …, a_n)` as well as on the
order of the `a_i`; however one shows that its conjugacy class does not depend on any of these choices. One calls `c`
the *Coxeter element* of the system considered. One shows (we shall admit it) that `c` does not have 1 as an
eigenvalue.

**Lemma 5.** *Set `θ_i = r_n ⋯ r_{i+1}(a_i)`. Then:*

<!-- label: III.XIV.7.lemma-5 -->

*(a) The `θ_i` form a basis of the group `X` generated by the roots.*

*(b) One has `θ_i > 0` and `c(θ_i) < 0` for all `i`* [^XIV-A-2].

*(c) Every root `a ∈ R` such that `a > 0` and `c(a) < 0` is equal to one of the `θ_i`.*

<!-- original page 346 -->

*(d) `R` is the union of the orbits of the `θ_i` under the powers of `c`.*

It is clear that `θ_i` is of the form `a_i + ∑_{j > i} m_{ij} a_j`, with `m_{ij} ∈ ℤ`, which proves (a). Assertions (b)
and (c) are consequences of the following remark: the symmetry `r_i` preserves the sign of every root distinct from
`±a_i`, and changes the sign of `±a_i`.

Finally, for (d) one remarks that an orbit of `c` cannot be entirely formed of positive (resp. negative) roots, since,
taking the sum of these roots one would find a non-zero element of `X` invariant under `c`, and we have admitted that
`c` does not have 1 as an eigenvalue. There is therefore necessarily in every orbit an element `a > 0` such that
`c(a) < 0`, and one applies (c).

**Remark.** We have sketched the preceding proof only to facilitate the reader's task; one could have limited oneself
to referring to the canonical texts on Coxeter (cf. for example Koszul, Séminaire Bourbaki, 1959/1960, exposé 191).
Said texts contain other results: the orbits of `c` all have the same number `h` of elements, and each contains only one
`θ_i`. In particular `h = Card(R)/n`.

Let us now return to the proof of Lemma 3. Distinguish three cases:

(1) *The element `ϕ ∈ E/W` given is equal to the identity element.*

One must then take `f ∈ W`; one chooses `f = c`; it works by Lemma 5.

(2) *The system `R` is of type `A_n`, with `n` even `⩾ 2`, and `ϕ` is the unique non-trivial element of `E/W`.*

One knows that `−1 ∉ W`; one then takes `f = −c`. A simple calculation shows that `c` is of order `h = n + 1`; hence its
order is odd. If `a ∈ R` is any root, <!-- original page 347 --> one has `a = c^m θ_i` for a pair `(m, i)`, cf. Lemma 5;
by adding `h` to `m` if necessary, one may suppose `m` even, and one sees that one has then `a = (−c)^m θ_i = f^m θ_i`.
The orbits of the `θ_i` therefore indeed fill `R`.

(3) *The element `ϕ ∈ E/W` is non-trivial, and `R` is of one of the following types:*

- `A_n`, `n` odd `≥ 3`
- `D_4`
- `D_n`, `n ≥ 5`
- `E_6`.

(A glance at the classification shows that these are indeed all the cases (with `A_n`, `n` even) where `E/W` is
non-trivial.)

Let `S` be a simple root system, which we shall not number for the moment. One knows that `E` is the semidirect product
of `W` and the group `Ψ` of permutations of `S` that leave invariant the Cartan matrix (or the Dynkin diagram, it is
the same thing). The group `E/W` is thereby identified with `Ψ`, and in particular `ϕ` corresponds to an element
`ψ ∈ Ψ`. One observes by inspection of the Dynkin diagrams (cf. figures above) that every orbit of `ψ` in `S` is formed
of roots that are pairwise orthogonal (i.e. not linked in the diagram). [Note that this would not be the case for `A_n`
(`n` even), which obliged us to treat this case separately.] If `σ` is such an orbit, the symmetries `r_a`, `a ∈ σ`,
commute with each other; their product will be denoted `ρ_σ`. It is clear that `ρ_σ` commutes with `ψ`.

This being so, let us choose on `S` a total order such that every orbit is a segment for this order relation; this
amounts to numbering the elements of `S`: `S = {a_1, …, a_n}`. Let `θ_1, …, θ_n` be the roots defined above, and
`c = r_1 ⋯ r_n` the corresponding Coxeter element. The element `c` is the product of the `ρ_σ`, the `σ` being arranged
in a certain order; it follows that it commutes with `ψ`. One then sets `f = cψ`. One further remarks that `ψ`
permutes the `θ_i` among themselves. Indeed, one has `ψ(θ_i) > 0` since `θ_i > 0` and `c(ψ(θ_i)) = ψ(c(θ_{i′})) < 0`,
hence (Lemma 5, (c)), `ψ(θ_i)` is equal to some `θ_j`. It is now immediate <!-- original page 348 --> that `f = cψ`
answers the question. Indeed, if `a ∈ R`, one has `a = c^m θ_i` for a pair `(m, i)`, whence `a = f^m (ψ^{−m} θ_i) =
f^m θ_j` for some `j`. *QED*.

**Remark.** One can prove that, except in case (2), every orbit of `f` has exactly `h = Card(R)/n` elements and contains
one and only one `θ_i`. In case (2), some of the `θ_i` are superfluous.

[^XIV-A-1]: This theorem is due to Chevalley. The editor wishes to express his gratitude to American Express which, by
misplacing a trunk of Chevalley manuscripts, obliged him to reconstruct the proof.

[^N.D.E-XIV-9]: One has changed `T̄` to `T`.

[^XIV-A-2]: For the order relation defined by `(a_1, …, a_n)`.

<!-- LEDGER DELTA — Exposé XIV — for consolidation in Phase 3
| French                                              | English                                             | Note                                                                                          |
| --------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| schéma des tores maximaux                           | scheme of maximal tori                              | Matches glossary "variété des tores maximaux"; here Grothendieck uses *schéma*.               |
| variété des sous-groupes de Cartan                  | variety of Cartan subgroups                         | Parallel to "variety of maximal tori".                                                        |
| sous-groupe de type (C)                             | subgroup of type (C)                                | Per Exposé XIII 6.2; preserved verbatim.                                                      |
| « espace homogène »                                 | "homogeneous space"                                 | Author quotes; preserve quotation marks.                                                      |
| section quasi-régulière / régulière                 | quasi-regular / regular section                     | Distinct technical notions (Def. 2.5).                                                        |
| algèbre de Lie localement nilpotente                | locally nilpotent Lie algebra                       | Def. 2.2.                                                                                     |
| strictement localement nilpotente                   | strictly locally nilpotent                          | Def. 2.2.                                                                                     |
| polynôme de Killing                                 | Killing polynomial                                  | Standard.                                                                                     |
| rang nilpotent / rang infinitésimal / rang réductif | nilpotent rank / infinitesimal rank / reductive rank | All preserved verbatim; standard.                                                              |
| « grosse cellule »                                  | "big cell"                                          | Author quotes; preserve.                                                                      |
| sous-groupe de Borel                                | Borel subgroup                                      | Standard.                                                                                     |
| sous-groupe parabolique                             | parabolic subgroup                                  | Standard.                                                                                     |
| « partie unipotente »                               | "unipotent part"                                    | Author quotes; preserve.                                                                      |
| « défini sur k »                                    | "defined over k"                                    | Author quotes; preserve.                                                                      |
| variété rationnelle                                 | rational variety                                    | Function field is a pure extension.                                                           |
| variété unirationnelle                              | unirational variety                                 | Standard.                                                                                     |
| corps parfait / non parfait                         | perfect / non-perfect field                         | Per task brief.                                                                               |
| descente non galoisienne                            | non-Galois descent                                  | Per task brief (not used explicitly in this Exposé; kept for ledger).                          |
| groupe k-unipotent                                  | `k`-unipotent group                                 | i.e. successive `G_a`-extensions over `k`.                                                    |
| dévissage                                           | dévissage                                           | Keep technical loanword (5.6 ff.).                                                            |
| forme tordue « intérieure »                         | "inner" twisted form                                | Author quotes; preserve.                                                                      |
| « algèbre d'Azumaya »                               | "Azumaya algebra"                                   | Author quotes; preserve.                                                                      |
| élément de Coxeter                                  | Coxeter element                                     | Standard.                                                                                     |
| nullité (d'un endomorphisme)                        | nullity (of an endomorphism)                        | dim ker.                                                                                      |
| Bible                                               | *Bible*                                             | The Chevalley Seminar 1956–58; italicised, per glossary.                                       |
| TranspG / NormG / CentrG                            | Transp_G / Norm_G / Centr_G                         | Notation preserved.                                                                           |
| sous-groupe de Cartan                               | Cartan subgroup                                     | Per glossary.                                                                                 |
| centre réductif                                     | reductive center                                    | Per glossary.                                                                                 |
| Killing couple (T, B)                               | Killing couple `(T, B)`                             | Used in N.D.E. footnote; loanword preserved.                                                  |
-->






