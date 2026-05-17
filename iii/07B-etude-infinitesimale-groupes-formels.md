# Exposé VII_B. Infinitesimal study: formal groups

<!-- label: III.VII_B -->

*by P. Gabriel*

## B) Formal groups

<!-- original page 477 -->

[^N.D.E-VII_B-0]

The study of formal groups is usually of extreme simplicity. If this does not appear clearly in the pages that follow,
the responsibility lies with an arithmetician who claims to know formal groups over "something other than
fields".[^N.D.E-VII_B-1] We have therefore unrolled, for formal groups "locally free over inverse limits of artinian
rings", the generalities one ordinarily states for formal groups defined over a field. For a more detailed study of the
latter, we refer the reader to the 1964/65 algebraic geometry seminar of Heidelberg–Strasbourg.[^N.D.E-VII_B-2]

## 0. Reminders on pseudocompact rings and modules

<!-- label: III.VII_B.0 -->

This paragraph contains a few technical preliminaries; we recall and complete in it some results from [CA] (*Des
catégories abéliennes*, Bull. Soc. Math. France 90, 1962).

### 0.1.

<!-- label: III.VII_B.0.1 -->

A *left pseudocompact ring* is a topological ring with unit element, separated and complete, which possesses a basis of
neighborhoods of `0` consisting of left ideals `𝓁` of finite colength (i.e. `length_A(A/𝓁) < +∞`). We shall assume here
that `A` is commutative, <!-- original page 478 --> so that there is no need to distinguish "between left and right".

In particular, the quotients `A/𝓁` are artinian rings and `A` is identified with the topological inverse limit of these
rings, each endowed with the discrete topology.

A complete noetherian local ring `(A, 𝔪)` is obviously pseudocompact.[^N.D.E-VII_B-3]

#### 0.1.1.

<!-- label: III.VII_B.0.1.1 -->

Every closed ideal `I` of `A` is the intersection of the open ideals containing it.[^N.D.E-VII_B-4] Every closed maximal
ideal is therefore open. Moreover, if `𝓁` is an open ideal of `A`, the maximal ideals of `A/𝓁` are in bijective
correspondence with the maximal ideals `𝔪` of `A` containing `𝓁`; these are therefore both open and closed.
Consequently, every closed maximal ideal is an open (and hence closed) maximal ideal; the converse being evident. We
denote by `Υ(A)` the set of these ideals.

If `𝓁` is an open ideal of `A` and if `𝔪 ∈ Υ(A)`, the localization `(A/𝓁)_𝔪` is therefore a local ring if `𝔪` contains
`𝓁` and zero otherwise. Since the ring `A/𝓁` is artinian, it is a direct product of finitely many local rings, which one
can write

```text
A/𝓁 ≃ ∏_{𝔪 ∈ Υ(A)} (A/𝓁)_𝔪.
```

From this one deduces "canonical" isomorphisms

```text
A ≃ lim_𝓁 (A/𝓁) ≃ lim_𝓁 ∏_𝔪 (A/𝓁)_𝔪 ≃ ∏_𝔪 lim_𝓁 (A/𝓁)_𝔪 ≃ ∏_𝔪 A_𝔪,
```

where one has set

```text
A_𝔪 = lim_𝓁 (A/𝓁)_𝔪.
```

This local component `A_𝔪` is a filtered inverse limit of artinian local rings, endowed with the discrete topology; it
is therefore a local ring which is pseudocompact for the inverse-limit topology.[^N.D.E-VII_B-5]

<!-- original page 479 -->

#### 0.1.2.

<!-- label: III.VII_B.0.1.2 -->

Let `r(A)` be the intersection of the open maximal ideals of `A`, that is, the cartesian product of the ideals `𝔪 A_𝔪`
when one identifies `A` with `∏_𝔪 A_𝔪`. For every open ideal `𝓁` of `A`, the image of `r(A)` in `A/𝓁` is contained in
the radical of `A/𝓁`. Some power of this image is therefore zero, so that `r(A)^n` is contained in `𝓁` when `n` is large
enough. The sequence of `r(A)^n` therefore tends to `0`.

The same holds for the sequence of `x^n`, when `x` belongs to `r(A)`. In other words, every element of `r(A)` is
topologically nilpotent and the converse is clear. It follows that the sequence with general term `1 + x + ⋯ + x^n` is
convergent and converges to `1/(1 − x)` when `x ∈ r(A)`. This shows that `r(A)` is the Jacobson radical of `A`, i.e.,
the intersection of all maximal ideals of `A` (cf. Bourbaki, *Algèbre*, Chap. 8, § 6, th. 1).[^N.D.E-VII_B-6]

**Remarks.**[^N.D.E-VII_B-7] a) If `𝔭` is an open prime ideal of `A`, then since `A/𝔭` is artinian, `𝔭` is a maximal
ideal. Consequently, `Υ(A)` equals the set of open prime ideals of `A`.

b) Each `𝔪 A_𝔪` is an ideal of definition of `A_𝔪`, i.e. an open ideal `I` such that the sequence of `I^n` tends to `0`
(cf. EGA 0_I, 7.1.2). Consequently, `Spec(A_𝔪 / 𝔪 A_𝔪)`, endowed with the topological ring `A_𝔪`, is an affine formal
scheme in the sense of (EGA I, 10.1.2).

c) The topological ring `A` is *admissible* in the sense of (EGA 0_I, 7.1.2) if and only if `r(A)` is open (hence an
ideal of definition), and this is the case if and only if `Υ(A)` is finite. In this case, the affine formal scheme
`Spf(A) = Spec(A / r(A))` (cf. EGA I, 10.1.2) has `Υ(A)`, endowed with the discrete topology, as underlying space, and
its structure sheaf has as ring of sections on a subset `E` of `Υ(A)` the product `∏_{𝔪 ∈ E} A_𝔪`.

d) Let `A` be an arbitrary pseudocompact ring. In 1.1 below, the space `Υ(A)` is endowed with the discrete topology and
with the sheaf of rings whose ring of sections on any subset `E` is `∏_{𝔪 ∈ E} A_𝔪`. By b), every point then admits an
open neighborhood which is an affine formal scheme, so this defines a formal scheme (EGA I, 10.4.2), which we shall
denote `Spf(A)`. (For this formal scheme to be affine, it must be quasi-compact, hence `Υ(A)` must be finite; in this
case, `Spf(A)` coincides with the definition of (EGA I, 10.1.2)).

#### 0.1.3.

<!-- label: III.VII_B.0.1.3 -->

If `A` and `B` are two pseudocompact rings, a *homomorphism* from `A` to `B` is, by definition, a continuous map
compatible with addition, multiplication, and the unit elements. Such a homomorphism sends a topologically nilpotent
element of `A` to a topologically nilpotent element of `B`; it therefore maps the radical `r(A)` of `A` into the radical
`r(B)` of `B`.

### 0.2.

<!-- label: III.VII_B.0.2 -->

Let `A` be a (commutative) pseudocompact ring. A *pseudocompact `A`-module* `M` is a topological `A`-module, separated
and complete, which possesses a basis of neighborhoods of `0` consisting of submodules `M'` such that `M/M'` is of
finite length over `A`.

If `M` and `N` are two pseudocompact `A`-modules, a *morphism* from `M` to `N` is by definition a continuous `A`-linear
map. We shall denote by `Hom_c(M, N)` the group of these morphisms.

<!-- original page 480 -->

**Proposition 0.2.B.**[^N.D.E-VII_B-8] *(i) The pseudocompact `A`-modules form an abelian category, which we shall
denote `PC(A)`. (In particular, for every morphism `f : M → N`, `Im(f)` is a complete submodule, hence closed in `N`).*

*(ii) The pseudocompact `A`-modules of finite length (whose topology is therefore discrete) form a system of
cogenerators of `PC(A)`.*

*(iii) Infinite products and filtered inverse limits are exact, i.e., `PC(A)` satisfies axiom `(AB5*)`.*[^N.D.E-VII_B-9]

<!-- label: III.VII_B.0.2.B -->

For the convenience of the reader, let us briefly indicate the steps of the proof. First, one has the following lemma
([CA] § IV.3, Lemma 1; for the proof, see [BEns], III, § 7.4, th. 1 and example 2):

**Lemma 0.2.C.** *Let `B` be a ring, `I` a filtered ordered set, `(M_i)` and `(N_i)` two inverse systems of left
`B`-modules indexed by `I`. Let `(s_i)` be a morphism of inverse systems `(M_i) → (N_i)`, such that `s_i` is surjective
with artinian kernel for every `i`. Then the map*

```text
lim s_i : lim M_i ⟶ lim N_i
```

*is surjective.*

<!-- label: III.VII_B.0.2.C -->

**Corollary 0.2.D** *([CA] § IV.3, Prop. 10 & 11). Let `M` be a pseudocompact `A`-module.*

*(i) Let `K` be a closed submodule of `M`. Then `M/K`, endowed with the quotient topology, is a pseudocompact
`A`-module.*

*(ii) Let `(M_i)` be a filtered decreasing family of closed submodules of `M`.*

*(a) The canonical map `M → lim M/M_i` is surjective and has kernel `⋂_i M_i`.*

*(b) For every closed submodule `N` of `M`, one has `N + ⋂_i M_i = ⋂_i (N + M_i)`.*

<!-- label: III.VII_B.0.2.D -->

*Proof.* Let `(L_j)` be the filtered decreasing family of open submodules of `M`. We endow `M/K` with the quotient
topology, i.e. a basis of neighborhoods of `0` is formed by the open submodules `(K + L_j)/K`. Since `K` is closed, it
equals the intersection of the `K + L_j`, so the map

```text
τ : M/K ⟶ lim_j M/(K + L_j)
```

is injective. It is also open, the right-hand side being the inverse limit of the discrete modules `M/(K + L_j)`.
Moreover, for each `j`, the map `t_j : M/L_j → M/(K + L_j)` is surjective with artinian kernel, so by the preceding
lemma, the map `t` in the commutative diagram below is surjective:

```text
M ─p─⥲→ lim_j M/L_j
│           │ t
│τ          ↓
M/K ─⥲→ lim_j M/(K + L_j).
```

Since `p` is an isomorphism because `M` is complete, it follows that `τ` is surjective, hence is an isomorphism. This
proves (i).

<!-- original page 507 -->

Let us prove (ii)(a). By what precedes, one has for every `i` an isomorphism `M/M_i ⥲ lim_j M/(M_i + L_j)`, and so the
two horizontal arrows in the commutative diagram below are isomorphisms:

```text
M ─p─⥲→ lim_j M/L_j
│           │ s
│g          ↓
lim_i M/M_i ─⥲→ lim_{i,j} M/(M_i + L_j).
```

Moreover, for each `j`, the family of submodules `(M_i + L_j)/L_j` admits a smallest element, since `M/L_j` is artinian,
so the morphism `s_j : M/L_j → lim_i M/(L_j + M_i)` is surjective; therefore, by the preceding lemma, `s` is surjective.
It follows that `g` is surjective. Finally, the kernel of `g` is the inverse limit of the `M_i`, i.e. their
intersection. This proves part (a).

Let us deduce part (b) from it. Since `N` is a closed submodule (hence separated and complete), it is a pseudocompact
module for the topology induced by that of `M`. Therefore, by (a), the morphisms `f` and `g` in the commutative exact
diagram below are surjective:

```text
0 ─→ N ───────→ M ───────→ M/N ─→ 0
     │f         │g         │h
     ↓          ↓          ↓
0 ─→ lim_i N/(N ∩ M_i) ─→ lim_i M/M_i ─→ lim_i M/(N + M_i).
```

Then, by the "snake lemma", the sequence `0 → Ker f → Ker g → Ker h → 0` is exact, and the equality
`N + ⋂_i M_i = ⋂_i (N + M_i)` follows.

We can now prove Proposition 0.2.B. Let `f : M → N` be a morphism of pseudocompact `A`-modules. Then `K = Ker(f)` is a
closed submodule of `M`, hence separated and complete, so `K` is a pseudocompact module for the topology induced by that
of `M`. By 0.2.D (i), `M/K` endowed with the quotient topology is pseudocompact.

Let us show that the continuous bijective morphism `M/K → Im(f)` is bicontinuous. Identifying `M/K` with `Im(f)`, it
suffices to show that the quotient topology `Q` is finer than the topology `T` induced by that of `N`. Let `(L_j)`
(resp. `(N_i)`) be the filtered decreasing family of open submodules of `M` (resp. `N`) and set `N'_i = N_i ∩ Im(f)`.
Let `P = (K + L_j)/K` be a submodule of `M/K` open for `Q`. Since `M/(K + L_j)` is artinian, the family `N'_i + P` has a
smallest element `N'_{i₀} + P`. Since the `N'_i` are open, hence closed, for `T` and hence also for `Q`, it follows from
0.2.D (ii) (b) that

```text
N'_{i₀} + P = ⋂_i (N'_i + P) = P + ⋂_i N'_i = P,
```

whence `N'_{i₀} ⊂ P`. This shows that `P` is open for `T`, and `M/K → Im(f)` is therefore an isomorphism of
pseudocompact modules.

In particular, `Im(f)` is complete for `T`, hence closed in `N`. Then, by 0.2.D (i) again, `Coker(f)` endowed with the
quotient topology is pseudocompact. This proves that `PC(A)` is an abelian category.

On the other hand, arbitrary inverse limits exist in `PC(A)`: if `(M_i)` is an inverse system of pseudocompact modules,
the inverse limit of the `M_i` has as underlying module the inverse limit of the underlying modules, with the
inverse-limit topology. Moreover, if one has a family of exact sequences in `PC(A)`:

```text
0 ⟶ K_i ⟶ M_i ⟶ Q_i ⟶ 0,
```

<!-- original page 508 -->

then the sequence `0 → ∏_i K_i → ∏_i M_i → ∏_i Q_i → 0` is exact. Point (iii) of 0.2.B follows, since in any abelian
category where arbitrary products exist, conditions (a) and (b) of 0.2.D are equivalent and equivalent to the exactness
of filtered inverse limits (cf. [Mi65], III 1.2–1.9 or [Po73], Chap. 2, Th. 8.6).

Finally, every pseudocompact module `M` is a submodule of the product `∏_L M/L`, where `L` ranges over the open
submodules of `M`, so the objects of finite length form a system of cogenerators of `PC(A)`. (Moreover, every object of
length `n` is isomorphic to a quotient `A^n / L`, where `L` is an open submodule of `A^n` of colength `n`; these
quotients therefore form a *set* of cogenerators.) This completes the proof of 0.2.B.

[^N.D.E-VII_B-10] Let `(Ab)` be the category of abelian groups and `LF(A)` the full subcategory of `PC(A)` formed by the
objects of finite length. For every object `M` of `PC(A)`, denote by `h^M_c` the functor:

```text
LF(A) ⟶ (Ab),     N ↦ Hom_c(M, N).
```

By [CA], § II.4, th. 1, Lemma 4 and Cor. 1, one has the following results.[^N.D.E-VII_B-11]

**Proposition 0.2.E.** *The functor `M ↦ h^M_c` is an anti-equivalence of `PC(A)` onto the category `Lex(LF(A), (Ab))`
of left-exact functors `LF(A) → (Ab)`.*

<!-- label: III.VII_B.0.2.E -->

**Corollary 0.2.F.** *(i) An object `P` of `PC(A)` is projective if and only if the functor `h^P_c` is exact (i.e., if
and only if the functor `Hom_c(P, −)` is exact on `LF(A)`).*

*(ii) Let `(M_i)` be a filtered inverse system[^N.D.E-VII_B-12] of objects of `PC(A)`. For every object `N` of `LF(A)`,
one has a functorial isomorphism in `N`:*

```text
Hom_c(lim M_i, N) ≃ colim Hom_c(M_i, N).
```

*(iii) Every filtered inverse limit and every product[^N.D.E-VII_B-12] of projective objects of `PC(A)` is a projective
object of `PC(A)`.*

<!-- label: III.VII_B.0.2.F -->

Finally, one deduces from 0.2.F the

**Corollary 0.2.G.** *Let `(M_i)_{i ∈ I}` be a family of objects of `PC(A)`. Then `∏_{i ∈ I} M_i` is projective if and
only if each `M_i` is.*

<!-- label: III.VII_B.0.2.G -->

<!-- original page 509 -->

Indeed, for every `N ∈ Ob LF(A)`, one has `Hom_c(∏_i M_i, N) ≃ ⨁_i Hom_c(M_i, N)`.

#### 0.2.1.

<!-- label: III.VII_B.0.2.1 -->

Each local component `A_𝔪` of `A` is a direct factor of `A`, hence a projective object of `PC(A)` (`A` is manifestly
projective). Moreover, `A_𝔪` has `S_𝔪 = A_𝔪 / 𝔪 A_𝔪` as its unique simple quotient, hence is indecomposable. On the
other hand, every simple object of `PC(A)` is isomorphic to a unique `S_𝔪`. By [CA], IV § 3, Cor. 1 of th.
3,[^N.D.E-VII_B-13] one therefore has:

**Proposition.** *(i) Every projective object of `PC(A)` is a direct product of indecomposable projective objects,
uniquely determined (up to isomorphism).*

*(ii) Every indecomposable projective object is isomorphic to a unique `A_𝔪` (`𝔪 ∈ Υ(A)`).*

**Definition.** *A pseudocompact `A`-module `M` is said to be* topologically free *if it is isomorphic to the product of
a family `(A_i)` of copies of `A`.*

*In this case, a family `(m_i)` of elements of `M` is called a* pseudobasis *of `M` if the `A`-linear maps from `A_i`
into `M` sending the unit element of `A_i` to `m_i` extend to an isomorphism of `∏_i A_i` onto `M`.*

#### 0.2.2.

<!-- label: III.VII_B.0.2.2 -->

[^N.D.E-VII_B-14] If `M` is a pseudocompact `A`-module, we shall denote by `M^†` the `A`-module (without topology)
`Hom_c(M, A)`.

Conversely, if `N` is an `A`-module, we denote by `N^* = Hom_A(N, A)` its dual, endowed with the topology of pointwise
convergence, i.e., a basis of neighborhoods of `0` in `N^*` is formed by the following submodules, where `x ∈ N` and `𝓁`
is an open ideal of `A`:

```text
V(x, 𝓁) = {f ∈ N^* | f(x) ∈ 𝓁}.
```

This makes `N^*` a pseudocompact `A`-module. Indeed, one sees first that if `N = A`, then `N^* = A`, endowed with its
topology of pseudocompact ring, and if `N` is a free module `A^{(I)}`, then `N^*` is the product `A^I`, endowed with the
product topology. On the other hand, for every morphism `φ : N_1 → N_2`, the transposed morphism `^t φ : N_2^* → N_1^*`
is continuous, since the inverse image under `^t φ` of a submodule `V(x_1, 𝓁)` of `N_1^*` is nothing but the submodule
`V(φ(x_1), 𝓁)` of `N_2^*`. Then, for arbitrary `N`, taking a presentation

```text
A^{(J)} ─φ→ A^{(I)} ─π→ N → 0,
```

one sees that `N^*` is the kernel of the continuous morphism `^t φ : A^I → A^J`, so `N^*` is pseudocompact.

When `A` is artinian (in which case one can take `𝓁 = 0` above), one deduces from 0.2.F:

<!-- original page 481 -->

**Proposition.** *When `A` is artinian, the functors*

```text
P ↦ P^†       and       Q ↦ Q^*,
```

*where `P` (resp. `Q`) is a projective object of `PC(A)` (resp. a projective `A`-module), establish an anti-equivalence
between the category of projective pseudocompact `A`-modules and that of projective `A`-modules.*[^N.D.E-VII_B-15]

In particular, when `A` is a field `k`, `P ↦ P^†` is an anti-equivalence between the category of all pseudocompact
`k`-modules (one also speaks of *linearly compact `k`-vector spaces*) and that of `k`-vector spaces.[^N.D.E-VII_B-16]

### 0.3.

<!-- label: III.VII_B.0.3 -->

[^N.D.E-VII_B-17] Let `L` and `M` be two pseudocompact `A`-modules. The functor

```text
LF(A) ⟶ (Ab),     N ↦ Bil_c(L × M, N),
```

where `Bil_c(L × M, N)` denotes the abelian group of continuous `A`-bilinear maps from `L × M` into `N`, is left exact.

By 0.2.E, there therefore exists a pseudocompact `A`-module `L ⊗̂_A M`, unique up to unique isomorphism, which
represents this functor, i.e. such that one has a functorial isomorphism, for every object `N` of `LF(A)`:

```text
Hom_c(L ⊗̂_A M, N) ≃ Bil_c(L × M, N).
```

<!-- original page 482 -->

Moreover, `L ⊗̂_A M` is identified with the inverse limit `P` of the (discrete) `A`-modules `(L/L') ⊗_A (M/M')`, where
`L'` and `M'` range respectively over the open submodules of `L` and `M`.

Indeed, let `φ : L × M → N` be a continuous bilinear map of `L × M` into an `A`-module (discrete) of finite length `N`.
By Lemma 0.3.1 below, there exist open submodules `L'` and `M'` of `L` and `M` such that `φ(L' × M) = φ(L × M') = {0}`.
This means that the map `φ̄ : L ⊗_A M → N`, which is induced by `φ`, is of the form `φ' ∘ p`, where `p` is the canonical
projection of `L ⊗_A M` onto `(L/L') ⊗_A (M/M')`. If one denotes by `φ̂` the composite:

```text
P ⟶ (L/L') ⊗_A (M/M') ─φ'→ N,
```

one sees that the map `φ ↦ φ̂` is a functorial bijection of `Bil_c(L × M, N)` onto `Hom_c(P, N)`, whence `P ≃ L ⊗̂_A M`.

The pseudocompact module `L ⊗̂_A M` is therefore the separated completion of `L ⊗_A M` for the linear topology defined
by the kernels of the canonical projections of `L ⊗_A M` onto `(L/L') ⊗_A (M/M')`, and it will be called the *completed
tensor product* of `L` and `M`.

If `x` and `y` belong to `L` and `M`, the image of `x ⊗_A y` in `L ⊗̂_A M` will be denoted `x ⊗̂_A y`.

#### 0.3.1.

<!-- label: III.VII_B.0.3.1 -->

**Lemma 0.3.1.** *Let `L`, `M` and `N` be pseudocompact `A`-modules, `N` of finite length. If `φ : L × M → N` is a
continuous `A`-bilinear map, there exist open submodules `L'` and `M'` of `L` and `M` such that
`φ(L' × M) = φ(L × M') = {0}`.*

<!-- label: III.VII_B.0.3.1.statement -->

Indeed, `φ^{-1}(0)` is an open neighborhood of `(0, 0)`, hence contains an open of the form `L_1 × M_1`, where `L_1` and
`M_1` are open submodules of `L` and `M`. Since `L/L_1` is of finite length, there exist elements `x_1, …, x_r` of `L`
such that `L_1 + A x_1 + ⋯ + A x_r = L`. If `M' ⊂ M_1` is "small enough", one also has `φ(x_i, M') = 0` for every `i`,
because the map `y ↦ φ(x_i, y)` is continuous; from this one deduces `φ(L, M') = {0}`; likewise, `φ(L', M) = {0}` if
`L'` is small enough.

**Corollary 0.3.1.1.**[^N.D.E-VII_B-18] *Let `M` be a pseudocompact `A`-module.*

*(i) For every open submodule `M'`, there exists an open ideal `𝓁` of `A` such that `𝓁 M ⊂ M'`.*

*(ii) Consequently, `M ≃ lim_𝓁 M / 𝓁 M`, where `𝓁` ranges over the filtered inverse system of open ideals of `A` and
each `M / 𝓁 M` is endowed with the quotient topology (which makes it a pseudocompact module, cf. 0.2.D).*

<!-- label: III.VII_B.0.3.1.1 -->

Indeed, consider the map `φ : A × M → M/M'`, `(a, m) ↦ am + M'`; by 0.3.1 there exists an open ideal `𝓁` of `A` such
that `𝓁 M ⊂ M'`, and since `M'` is also closed, it contains also `𝓁 M`. Since the intersection of the open submodules of
`M` is zero, one therefore has `⋂_𝓁 𝓁 M = (0)`. On the other hand, by 0.2.D, the map `φ : M → lim_𝓁 M / 𝓁 M` is
surjective; by (the proof of) 0.2.B, `φ` therefore induces an isomorphism `M / Ker(φ) ⥲ lim_𝓁 M / 𝓁 M`, but we have just
seen that `Ker(φ) = ⋂_𝓁 𝓁 M` is zero.

**Remark 0.3.1.2.**[^N.D.E-VII_B-19] *The completed tensor product satisfies the usual associativity condition: if `L`,
`M`, `P` are pseudocompact `A`-modules, one has a canonical isomorphism*

```text
(L ⊗̂ M) ⊗̂ P ≃ L ⊗̂ (M ⊗̂ P);
```

*indeed, these two objects represent the functor that associates to every object `N` of `LF(A)` the abelian group of
continuous `A`-trilinear maps from `L × M × P` into `N`.*

<!-- label: III.VII_B.0.3.1.2 -->

#### 0.3.2.

<!-- label: III.VII_B.0.3.2 -->

Let `L' ─f→ L ─g→ L'' → 0` be an exact sequence and `M` an object of `PC(A)`. It is clear that for every object `N` of
`LF(A)`, the induced sequences:

```text
0 → Bil_c(L'' × M, N) → Bil_c(L × M, N) → Bil_c(L' × M, N)

0 → Hom_c(L'' ⊗̂_A M, N) → Hom_c(L ⊗̂_A M, N) → Hom_c(L' ⊗̂_A M, N)
```

<!-- original page 483 -->

are exact. By 0.2.E, this is equivalent to saying that the sequence

```text
(∗)              L' ⊗̂_A M ─f ⊗̂ M→ L ⊗̂_A M ─g ⊗̂ M→ L'' ⊗̂_A M → 0
```

is exact. Hence:

**Corollary.** *For every pseudocompact `A`-module `M`, the functor `− ⊗̂_A M` is right exact.*

In particular, take for `L` the ring `A`, for `f` the inclusion of a closed ideal `𝔞` in `A`, and for `g` the canonical
projection of `A` onto `A/𝔞`. One can then identify `A ⊗̂_A M` with `M` by means of the map `x ⊗̂_A m ↦ x m`. Since the
image of `𝔞 ⊗̂_A M` is closed in `M` (cf. 0.2.B) and the image of `𝔞 ⊗_A M` is everywhere dense in `𝔞 ⊗̂_A M`, the image
of `f ⊗̂_A M` is nothing but the closure `𝔞̄ M` of `𝔞 M` in `M`. The exact sequence (∗) therefore yields the
isomorphism:

```text
(A/𝔞) ⊗̂_A M ⥲ M / 𝔞̄ M.
```

#### 0.3.3.

<!-- label: III.VII_B.0.3.3 -->

**Lemma 0.3.3 (Nakayama's Lemma).** *Let `A` be a pseudocompact ring, `M` a pseudocompact `A`-module, and `𝔞` an ideal
of `A` contained in the radical `r(A)`. The equality `𝔞̄ M = M` then implies `M = 0`.*

<!-- label: III.VII_B.0.3.3 -->

Indeed, suppose `𝔞̄ M = M`.[^N.D.E-VII_B-20] Let `M'` be an open submodule of `M` and `M'' = M/M'`. Since `M''` is
discrete, `𝔞 M''` is closed in `M''`, hence equal to `𝔞̄ M''`. By 0.3.2, the canonical map of `M/𝔞̄ M` to `M''/𝔞̄ M''`
is surjective, so one has `𝔞 M'' = 𝔞̄ M'' = M''`. Since `M''` is a finitely generated `A`-module and `𝔞 ⊂ r(A)`, this
implies `M'' = 0` by the usual Nakayama's Lemma. Consequently, every open submodule `M'` of `M` equals `M`, and so `M`
is zero.[^N.D.E-VII_B-21]

#### 0.3.4.

<!-- label: III.VII_B.0.3.4 -->

From Nakayama's Lemma one draws the usual consequences:

**Corollary.** *Let `𝔞` be a closed ideal contained in `r(A)` and `f : M → N` a morphism of pseudocompact `A`-modules.*

*(i) `f` is surjective if the induced map `f' : M/𝔞 M → N/𝔞 N` is.*[^N.D.E-VII_B-22]

*(ii) If `N` is projective, `f` is invertible if `f'` is.*

<!-- original page 484 -->

Indeed, (i) follows from Lemma 0.3.3 applied to `Coker f`. For (ii), suppose `f'` invertible. Then by (i), `f` is
surjective, hence has a section; one then applies 0.3.3 to `Ker f`.

When `A` is local with maximal ideal `𝔪`, one can also deduce from 0.3.3 the following exchange theorem:

**Theorem.** *Let `A` be a local pseudocompact ring, `𝔪` its maximal ideal, `M` a topologically free `A`-module with
pseudobasis `(m_i)_{i ∈ I}` (0.2.1), and `N` a (closed) direct factor of `M`. There exists a pseudobasis of `M` formed
of elements of `N` and of certain `m_i`.*

Indeed, this is clear when `A` is a field (one then uses the duality of 0.2.2 and applies the usual exchange theorem);
consequently, `N/𝔪 N`[^N.D.E-VII_B-23] has as a supplement a topologically free module over `A/𝔪` with pseudobasis
`(m̄_i)_{i ∈ J}`, where `m̄_i` is the image of `m_i` in `M / 𝔪 M` and `J` is a subset of `I`. If `P` denotes the direct
product `∏_{i ∈ J} A m_i`, the canonical map of `N ⊕ P` to `M` is "bijective modulo `𝔪`"; it is therefore bijective by
what precedes (for another proof see [CA], § IV.2, Prop. 8).

#### 0.3.5.

<!-- label: III.VII_B.0.3.5 -->

<!-- original page 485 -->

Consider now three pseudocompact `A`-modules `L`, `M` and `N`, where `N` is of finite length. Endowing the `A`-module
`Hom_c(M, N)` with the discrete topology, every element `ψ` of `Hom_c(L, Hom_c(M, N))` defines a continuous bilinear map
`ψ' : (𝓁, m) ↦ ψ(𝓁)(m)` from `L × M` to `N`. One thus obtains a natural isomorphism

```text
(1)             Hom_c(L, Hom_c(M, N)) ⥲ Hom_c(L ⊗̂_A M, N),
```

hence another characterization of `Hom_c(L ⊗̂_A M, N)`, which we shall use when `M` is the inverse limit of a filtered
inverse system of pseudocompact `A`-modules `M_i`. Then, by (1) and 0.2.F (ii), one has natural isomorphisms:

```text
(2)   Hom_c(L ⊗̂_A lim M_i, N) ≃ Hom_c(L, Hom_c(lim M_i, N))
                              ≃ Hom_c(L, colim Hom_c(M_i, N)).
```

Moreover, since the module `colim Hom_c(M_i, N)` is discrete, every continuous map with source `L` factors through a
finite-length quotient of `L`. Consequently, the natural map below is an isomorphism:

```text
(3)   colim Hom_c(L, Hom_c(M_i, N)) ⟶ Hom_c(L, colim Hom_c(M_i, N)).
```

Finally, by (1) and 0.2.F (ii) again, one has natural isomorphisms:

```text
(4)   colim Hom_c(L, Hom_c(M_i, N)) ≃ colim Hom_c(L ⊗̂_A M_i, N)
                                     ≃ Hom_c(lim (L ⊗̂_A M_i), N).
```

Combining isomorphisms (2), (3), (4), one obtains:

**Proposition.** *Let `(M_i)` be a filtered inverse system of objects of `PC(A)`, and let `L` (resp. `N`) be an object
of `PC(A)` (resp. `LF(A)`). One has a functorial isomorphism in `N`:*

```text
Hom_c(L ⊗̂_A lim M_i, N) ≃ Hom_c(lim (L ⊗̂_A M_i), N),
```

*and hence an isomorphism:*

```text
L ⊗̂_A lim M_i ≃ lim (L ⊗̂_A M_i).
```

*The completed tensor product therefore commutes with filtered inverse limits.*[^N.D.E-VII_B-24]

#### 0.3.6.

<!-- label: III.VII_B.0.3.6 -->

In particular,[^N.D.E-VII_B-25] the completed tensor product commutes with infinite products. For example, since the
ring `A` is the product of its local components `A_𝔪` (0.1.1), every pseudocompact `A`-module `M` (`≃ A ⊗̂_A M`) is
identified with the product of the modules `M_𝔪 = A_𝔪 ⊗̂_A M` (the local components of `M`).

<!-- original page 514 -->

Likewise, let `M` and `N` be two pseudocompact `A`-modules. Recall (cf. 0.2.2) that `M^†` denotes `Hom_c(M, A)`.
Consider the map

```text
φ : M^† ⊗_A N^† ⟶ (M ⊗̂_A N)^†
```

which associates to an element `f ⊗ g` of `M^† ⊗_A N^†` the map `m ⊗̂ n ↦ f(m) g(n)` from `M ⊗̂_A N` to `A`. This map
`φ` is bijective when `M` is isomorphic to `A`.

**Corollary.** *When `A` is artinian, `φ` is an isomorphism whenever `M` is topologically free (or more generally
projective).*

Indeed, for `N` fixed, the functor `M ↦ (M ⊗̂_A N)^†` (resp. `M ↦ M^† ⊗_A N^†`) transforms every direct product into a
direct sum, by what precedes and 0.2.F.

**Remark 0.3.6.A.**[^N.D.E-VII_B-26] *Using 0.2.F in a similar way, one also obtains the following result: Let `A` be an
artinian ring, `M`, `Q` objects of `PC(A)`, and `N` an object of `LF(A)`. Suppose `Q` projective; then one has natural
isomorphisms:*

```text
Hom_c(M, Q) ⥲ Hom_A(Q^†, M^†)         and        Q^† ⊗_A N ⥲ Hom_c(Q, N).
```

<!-- label: III.VII_B.0.3.6.A -->

#### 0.3.7.

<!-- label: III.VII_B.0.3.7 -->

For every `𝔪 ∈ Υ(A)`, the functor `M ↦ A_𝔪 ⊗̂_A M` is evidently exact. <!-- original page 486 --> Since every projective
pseudocompact `A`-module `P` is a product of modules of the form `A_𝔪`, it follows that the functor `M ↦ P ⊗̂_A M` is
exact when `P` is projective. The converse is true:

**Proposition.** *Let `A` be a pseudocompact ring, `P` a pseudocompact `A`-module. The following conditions are
equivalent:*

*(i) `P` is a projective object of `PC(A)`.*

*(ii) Each local component `P_𝔪` is a topologically free `A_𝔪`-module.*

*(iii) The functor `M ↦ P ⊗̂_A M` is exact.*

Indeed, the equivalence of (i) and (ii) follows from 0.2.F (iii) and 0.2.1, and we have just seen that (ii) ⇒ (iii).
Suppose the functor `M ↦ P ⊗̂_A M` is exact. Since `P ⊗̂_A M` is the product of its local components:

```text
(P ⊗̂_A M)_𝔪 ≃ P_𝔪 ⊗̂_{A_𝔪} M_𝔪,
```

one is reduced to the case where the ring `A` is local. We then prove that `P` is topologically free.

Let `𝔪` be the maximal ideal of `A`; then `P / 𝔪̄ P` is a linearly compact vector space over `A/𝔪`, hence a product of
copies of `A/𝔪` (cf. 0.2.2). There is therefore a family `(A_i)_{i ∈ I}` of copies of `A` and an isomorphism
`φ : ∏_{i ∈ I} (A_i / 𝔪) ⥲ P / 𝔪̄ P`. Since `∏_{i ∈ I} A_i` is projective, there is a commutative square

```text
∏ A_i ─ψ→ P
│         │
│p        │q
↓         ↓
∏ (A_i/𝔪) ─φ→ P/𝔪̄ P,
```

<!-- original page 515 -->

where `p` and `q` denote the canonical projections. Applying Nakayama's Lemma to `Coker ψ` and noting that
`(A/𝔪) ⊗̂_A ψ` is nothing but `φ`, one sees that `ψ` is surjective.[^N.D.E-VII_B-27]

Setting then `B = ∏_{i ∈ I} A_i` and `N = Ker ψ`, one has the following commutative and exact diagram:

```text
        𝔪 ⊗̂_A N ────→ 𝔪 ⊗̂_A B ────→ 𝔪 ⊗̂_A P ─→ 0
            ↓             ↓             ↓
        A ⊗̂_A N ────→ A ⊗̂_A B ──ψ→ A ⊗̂_A P ─→ 0
            ↓             ↓             ↓
        (A/𝔪) ⊗̂_A N → (A/𝔪) ⊗̂_A B ─φ→ (A/𝔪) ⊗̂_A P → 0.
```

The "snake lemma" applied to the first two rows then shows that, in the bottom row, the morphism
`(A/𝔪) ⊗̂_A N → (A/𝔪) ⊗̂_A B` is a monomorphism. But then, since `φ` is an isomorphism, `(A/𝔪) ⊗̂_A N` is zero; whence
`N = 0` (0.3.3) and `ψ` is an isomorphism.[^N.D.E-VII_B-28]

<!-- original page 487 -->

#### 0.3.8.

<!-- label: III.VII_B.0.3.8 -->

**Corollary 0.3.8.** *Let `A` be a complete noetherian local ring and `P` a pseudocompact `A`-module. Then `P` is
topologically free if and only if `P` is flat over `A`.*

Indeed, the canonical map of `M ⊗_A P` into `M ⊗̂_A P` is bijective when `M` equals `A`, hence also when `M` is
noetherian (take a finite presentation of `M` and use the right exactness of the tensor product and of the completed
tensor product).

Now `P` is flat if and only if the functor `M ↦ M ⊗_A P` is exact when `M` ranges over the noetherian modules. Likewise,
we saw in the proof of Proposition 0.3.7 that `P` is topologically free if the sequence

```text
0 ⟶ 𝔪 ⊗̂_A P ⟶ A ⊗̂_A P ⟶ (A/𝔪) ⊗̂_A P ⟶ 0
```

<!-- original page 488 -->

is exact. So `P` is topologically free if and only if the functor `M ↦ M ⊗̂_A P` is exact when `M` ranges over the
noetherian modules. The corollary therefore follows from the equality `M ⊗_A P = M ⊗̂_A P` established above.

### 0.4.

<!-- label: III.VII_B.0.4 -->

Let `k` be a pseudocompact ring; a *topological `k`-algebra* is a (commutative) topological ring `A`, equipped with a
morphism of topological rings `k → A`. One says that `A` is a *profinite `k`-algebra* if the underlying topological
`k`-module is pseudocompact.

In this case, let `𝓁` be an open `k`-submodule of `A`. The composite map

```text
φ : A × A ─mult→ A ─can→ A/𝓁
```

is continuous, hence by Lemma 0.3.1, there exists an open `k`-submodule `𝔫` of `A` such that `φ(A × 𝔫) = 0`. This means
that `𝓁` contains the open ideal `A𝔫` and implies that `A` is a pseudocompact ring.

Likewise, let `M` be a topological `A`-module whose underlying `k`-module is pseudocompact. If `M'` is an open
`k`-submodule of `M`, Lemma 0.3.1 applied to the map

```text
A × M ─mult→ M ─can→ M/M'
```

shows that `M'` contains an open `A`-submodule, so that `M` is also a pseudocompact `A`-module.[^N.D.E-VII_B-29]
Conversely:

**Lemma.** *Let `A` be a profinite `k`-algebra and `M` a pseudocompact `A`-module. Then the `k`-module `M|_k` obtained
by restriction of scalars is pseudocompact.*

Indeed, every pseudocompact `A`-module of finite length is isomorphic to a quotient `A^n / L` (where `L` is an open
submodule of `A^n`), hence is a pseudocompact `k`-module. Since `M|_k` is an inverse limit of such modules, it is a
pseudocompact `k`-module.

#### 0.4.1.

<!-- label: III.VII_B.0.4.1 -->

If `A` and `B` are two profinite `k`-algebras, a *morphism* from `A` to `B` is, by definition, a continuous homomorphism
of `k`-algebras. We shall denote by `Alp/k` the category of profinite `k`-algebras.

It evidently possesses inverse limits: the algebra underlying an inverse limit is the inverse limit of the underlying
algebras; the topology is that of the inverse limit. <!-- original page 489 -->

It also possesses finite direct limits[^N.D.E-VII_B-30]: for example, if `f : A → B` and `g : A → C` are two morphisms
of profinite `k`-algebras, the amalgamated sum of `B` and `C` over `A` has `B ⊗̂_A C` as underlying topological
`A`-module (by 0.4, `f` and `g` endow `B` and `C` with pseudocompact `A`-module structures); the multiplication of
`B ⊗̂_A C` is obviously such that `(b ⊗̂ c)(b' ⊗̂ c') = (bb') ⊗̂ (cc')` if `b, b' ∈ B` and `c, c' ∈ C`.

#### 0.4.2.

<!-- label: III.VII_B.0.4.2 -->

**Definition 0.4.2.** *A profinite `k`-algebra `C` is said to be of* finite length *if the underlying `k`-module is of
finite length (hence discrete); we denote by `Alf/k` the full subcategory of `Alp/k` formed by `k`-algebras of finite
length.*[^N.D.E-VII_B-31]

<!-- label: III.VII_B.0.4.2 -->

For every profinite `k`-algebra `A`, we denote by `h_A` the functor:

```text
Alf/k ⟶ (Sets),     C ↦ Hom_{Alp/k}(A, C).
```

It is clear that `h_A` is a left-exact functor[^N.D.E-VII_B-32]. Moreover, the canonical projections `A → A/𝓁` (where
`𝓁` ranges over the open ideals of `A`) induce, for every object `C` of `Alf/k`, a canonical isomorphism

```text
colim_𝓁 Hom_{Alf/k}(A/𝓁, C) ⥲ Hom_{Alp/k}(A, C),
```

functorial in `C`. This means that `h_A` is the direct limit of the representable functors `h_{A/𝓁}`, i.e.,

```text
(∗)     h_A ≃ colim_𝓁 h_{A/𝓁}.
```

If `B` is another profinite `k`-algebra, the general properties of the bifunctor `Hom` and the isomorphism
`Hom(h_C, h_B) = h_B(C)` for `C` of finite length give isomorphisms:

```text
Hom_{Alp/k}(B, A) ≃ lim Hom_{Alp/k}(B, A/𝓁)
                  ≃ lim Hom(h_{A/𝓁}, h_B)
                  ≃ Hom(colim_𝓁 h_{A/𝓁}, h_B);
```

combined with (∗), this shows that the contravariant functor `A ↦ h_A` is fully faithful. In fact:

<!-- original page 490 -->

**Proposition.** *The functor `A ↦ h_A` is an anti-equivalence of `Alp/k` onto the category of left-exact functors from
`Alf/k` to `(Sets)`.*

Indeed, by what precedes, it suffices to show that every left-exact functor `F : Alf/k → (Sets)` is isomorphic to a
functor of the type `h_A`; for this, one can construct `A` as follows (cf. TDTE II, § 3).

Since `F` is left-exact, for every `k`-algebra of finite length `C` and every element `ξ` of `F(C)`, there is a smallest
subalgebra `C'` of `C` such that `ξ` belongs to the image of `F(C')` in `F(C)`. If one has `C' = C`, one says that the
pair `(C, ξ)` is *minimal*.

The minimal pairs form a category if one takes for morphisms from `(C, ξ)` to `(D, η)` the homomorphisms `φ` from `C` to
`D` such that `(Fφ)(ξ) = η`; it is clear that such a `φ` is a surjection and that the category of minimal pairs is "left
filtered". Moreover, one can restrict to pairs `(C, ξ)` such that `C` belongs to a set containing `k`-algebras of finite
length of each isomorphism type[^N.D.E-VII_B-33]. Hence, the functor `(C, ξ) ↦ C`, with source category that of minimal
pairs and target category that of profinite `k`-algebras, possesses an inverse limit; one takes for `A` this inverse
limit.

**Corollary.** *The category `Alp/k` possesses infinite direct limits.*

Indeed, the category of left-exact functors from `Alf/k` to `(Sets)` possesses inverse limits, which are defined
"argument by argument", i.e., if `(F_i)` is an inverse system of such functors, one has, for every object `C` of
`Alf/k`:

```text
(lim F_i)(C) = lim F_i(C).
```

[^N.D.E-VII_B-34]

### 0.5.

<!-- label: III.VII_B.0.5 -->

[^N.D.E-VII_B-35] Let `φ : k → ℓ` be a homomorphism of pseudocompact rings (cf. 0.1.3). One can generalize the
construction of 0.3 as follows.

<!-- original page 491 -->

**Definition 0.5.A.** *For every object `M` of `PC(k)` (resp. `N` of `PC(ℓ)`), we shall denote by `M ⊗̂_k N` the
separated completion of `M ⊗_k N` for the linear topology defined by the kernels of the projections:*

```text
M ⊗_k ℓ ⟶ (M/M') ⊗_k (N/N'),
```

*where `M'` (resp. `N'`) is an open submodule of `M` (resp. of `N`). Then `M ⊗̂_k N` is a pseudocompact `ℓ`-module. If
`m ∈ M` and `x ∈ N`, we shall denote by `m ⊗̂_k x` the canonical image of `m ⊗_k x` in `M ⊗̂_k N`.*

<!-- label: III.VII_B.0.5.A -->

*This applies in particular when `N = ℓ`, in which case we shall say that `M ⊗̂_k ℓ` is the pseudocompact `ℓ`-module
deduced from `M` by the base change `k → ℓ`.*

**Remarks 0.5.B.** *(i) When one considers such a base change, `ℓ` will not in general be a profinite `k`-algebra: a
typical example is the case where `k` is a field and `ℓ` is an arbitrary extension `K` of `k`.*

*(ii) However, if the `k`-module underlying `N` is pseudocompact (for example if `ℓ` is a profinite `k`-algebra) then,
by 0.4, every open `k`-submodule of `N` contains an open `ℓ`-submodule of `N`; consequently, `M ⊗̂_k N` coincides in
this case with the completed tensor product (cf. 0.3) of the pseudocompact `k`-modules `M` and `N`, and the notation
therefore does not present any ambiguity.*

<!-- label: III.VII_B.0.5.B -->

The `k`-module `N|_k` obtained by restriction of scalars is in any case a topological `k`-module, i.e. the map
`k × N → N`, `(t, n) ↦ φ(t) n` is continuous. We denote by `Hom_c(M, N|_k)` the abelian group of continuous `k`-module
homomorphisms of `M` into `N|_k`.

**Proposition 0.5.C.** *For every `M ∈ Ob PC(k)` and `N ∈ Ob PC(ℓ)`, one has a functorial isomorphism*

```text
Hom_{PC(ℓ)}(M ⊗̂_k ℓ, N) ≃ Hom_c(M, N|_k).
```

<!-- label: III.VII_B.0.5.C -->

[^N.D.E-VII_B-36]

Indeed, let `φ` be a continuous homomorphism `M → N|_k`; then the map `φ' : M × ℓ → N`, `(m, λ) ↦ λ φ(m)` is continuous
and "bilinear" (i.e., `k`-linear in the first factor and `ℓ`-linear in the second). If `N'` is an open `ℓ`-submodule of
`N`, one shows as in Lemma 0.3.1 that there exist an open submodule `M'` of `M` and an open ideal `ℓ'` of `ℓ` such that
`φ'(M' × ℓ)` and `φ'(M × ℓ')` are contained in `N'`. It follows that `φ` induces a continuous homomorphism of
`ℓ`-modules `Φ : M ⊗̂_k ℓ → N`, such that `Φ(m ⊗̂ λ) = λ φ(m)`, for every `m ∈ M` and `λ ∈ ℓ`.

Conversely, to every morphism `f : M ⊗̂_k ℓ → N` one associates the morphism `f' : m ↦ f(m ⊗̂_k 1)` from `M` to `N|_k`.

One then obtains, as in 0.3.2, 0.3.5, and 0.3.1.2, the:

**Corollary 0.5.D.** *The functor `PC(k) → PC(ℓ)`, `M ↦ M ⊗̂_k ℓ` is right exact and commutes with filtered inverse
limits, i.e., if `(M_i)` is a filtered inverse system of objects of `PC(k)`, one has a canonical isomorphism:*

```text
(lim M_i) ⊗̂_k ℓ ≃ lim (M_i ⊗̂_k ℓ).
```

*Moreover, if `M`, `N` are pseudocompact `k`-modules, one has a canonical isomorphism:*

```text
(M ⊗̂_k N) ⊗̂_k ℓ ≃ (M ⊗̂_k ℓ) ⊗̂_ℓ (N ⊗̂_k ℓ).
```

<!-- label: III.VII_B.0.5.D -->

**Definition 0.5.E.** *Finally, if `A` is a profinite `k`-algebra, there is on `A ⊗̂_k ℓ` one and only one structure of
profinite `ℓ`-algebra such that, if `a, b ∈ A` and `λ, μ ∈ ℓ`,*

```text
(a ⊗̂_k λ)(b ⊗̂_k μ) = (ab) ⊗̂_k (λμ).
```

*One says that `A ⊗̂_k ℓ` is the profinite `ℓ`-algebra deduced from `A` by the extension of scalars (or "base change")
`k → ℓ`.*

<!-- label: III.VII_B.0.5.E -->

## 1. Formal varieties over a pseudocompact ring

<!-- label: III.VII_B.1 -->

<!-- original page 492 -->

### 1.1.

<!-- label: III.VII_B.1.1 -->

One can associate to every pseudocompact ring `A` a formal scheme (EGA I, 10.4.2) by proceeding as follows: the
underlying topological space is the set `Υ(A)` of open (hence maximal) prime ideals of `A`, endowed with the discrete
topology; the structure sheaf has the cartesian product `∏_{𝔪 ∈ E} A_𝔪` as space of sections on a subset `E` of `Υ(A)`.
The formal scheme thus obtained is denoted `Spf(A)` (the *formal spectrum* of `A`).[^N.D.E-VII_B-37]

If `A` and `B` are two pseudocompact rings, a morphism from `Spf(B)` to `Spf(A)` consists of the datum of a map `f` from
`Υ(B)` to `Υ(A)` and of a family of continuous homomorphisms `f_y^♮ : A_{f(y)} → B_y`, for `y ∈ Υ(B)`. Such a morphism
induces a continuous homomorphism `f^♮` from `A = ∏_{x ∈ Υ(A)} A_x` to `B = ∏_{y ∈ Υ(B)} B_y`. The converse is true:

<!-- original page 520 -->

**Proposition.** *The contravariant functor `A ↦ Spf(A)` is fully faithful.*

Indeed, if `φ : A → B` is a continuous algebra homomorphism, the inverse image `φ^{-1}(𝔫)` of an open maximal ideal of
`B` is an open prime ideal of `A`, hence maximal in `A`. One thus obtains a map `𝔫 ↦ φ^{-1}(𝔫)` from `Υ(B)` to `Υ(A)`,
and `φ` induces a continuous homomorphism `A_{φ^{-1}(𝔫)} → B_𝔫`. So `φ` induces a morphism of formal schemes
`Spf(φ) : Spf(B) → Spf(A)`. One verifies easily that `Spf(φ)^♮ = φ`, and that `Spf(f^♮) = f` for every morphism
`f : Spf(B) → Spf(A)`, whence the proposition.

Although we shall here speak only of formal schemes of the form `Spf(A)`, we shall use the language of formal schemes
rather than that of pseudocompact rings, in order to base our assertions on a geometric intuition.

### 1.2.

<!-- label: III.VII_B.1.2 -->

Let `k` be a pseudocompact ring.

<!-- original page 493 -->

**Definition 1.2.A.**[^N.D.E-VII_B-38] *We shall call a* formal variety over `k` *any formal scheme `X` over `Spf(k)`
which is isomorphic to a formal `k`-scheme `Spf(A)` for some profinite `k`-algebra `A`. The algebra `A` is then
isomorphic to the* affine algebra *of `X`, that is, to the algebra of sections of the structure sheaf `O_X` of `X`.*

*We denote by `Vaf/k` the full subcategory of the category of formal schemes over `Spf(k)` whose objects are the formal
`k`-varieties.*[^N.D.E-VII_B-39]

<!-- label: III.VII_B.1.2.A -->

By 1.1, the functor `A ↦ Spf(A)` is an anti-equivalence of `Alp/k` (0.4.1) onto `Vaf/k`. So, by the corollary of 0.4.2:

**Proposition 1.2.B.** *The category `Vaf/k` possesses inverse and direct limits.*[^N.D.E-VII_B-40]

<!-- label: III.VII_B.1.2.B -->

For example, let `X ∈ Ob Vaf/k` and `f : Y → X` and `g : Z → X` be two formal `k`-varieties over `X` and let `A`, `B`,
`C` be the affine algebras of `X`, `Y`, `Z`; by 0.4.1, the affine algebra of the fiber product `Y ×_X Z` is identified
with `B ⊗̂_A C`,[^N.D.E-VII_B-41] so that the inclusion of `Vaf/k` in the category of all formal `k`-schemes commutes
with finite inverse limits (cf. EGA I, 10.7).

The direct limits of formal `k`-varieties correspond to inverse limits of their affine algebras.

**Example 1.2.C (Cokernels).** Let, for example, `d, e : X ⇒ Y` be a double arrow of `Vaf/k`; the affine algebra of
`Coker(d, e)` is isomorphic to the kernel of the homomorphisms induced on the affine algebras of `X` and `Y`, but one
can also give the following construction of `Coker(d, e)`: the topological space underlying `Coker(d, e)` is the
cokernel of the underlying spaces;[^N.D.E-VII_B-42] if `p` is the canonical projection of the set underlying `Y` onto
the cokernel and if `z` belongs to the cokernel, the local algebra of `Coker(d, e)` at `z` is the kernel of the double
arrow

```text
d^♮, e^♮ : ∏_{p(y) = z} O_{Y, y} ⇒ ∏_{q(x) = z} O_{X, x},
```

where one has set `q = p ∘ d = p ∘ e` and where `d^♮` and `e^♮` are induced by the homomorphisms `d_x^♮` and `e_x^♮`
(notations of 1.1).

<!-- original page 494 -->

**Definition 1.2.D.** *If `φ : k → ℓ` is a homomorphism of pseudocompact rings and `X` is a formal `k`-variety with
affine algebra `A`, the formal scheme `X ×_{Spf(k)} Spf(ℓ)`, obtained by base change, is a formal `ℓ`-variety, which we
shall also denote `X ⊗̂_k ℓ` and which has as affine algebra the completed tensor product `A ⊗̂_k ℓ` (cf. 0.5 and EGA I,
§ 10).*

<!-- label: III.VII_B.1.2.D -->

**Remark 1.2.E.** *Since every formal variety over `k` decomposes into formal varieties over the local components of
`k`, we shall assume in some proofs that `k` is a local pseudocompact ring.*

<!-- label: III.VII_B.1.2.E -->

We now give some examples while fixing our terminology.

#### 1.2.1.

<!-- label: III.VII_B.1.2.1 -->

A `k`-*functor* will be, by definition, a covariant functor from `Alf/k` to `(Sets)`. By 1.1 and 0.4.2, one can identify
`Vaf/k ≃ (Alp/k)°` with a full subcategory of the category of `k`-functors, by associating to every formal `k`-variety
`X` the functor:

```text
Alf/k ⟶ (Sets),     C ↦ X(C) = Hom_{Vaf/k}(Spf(C), X).
```

We shall encounter later `k`-functors `F` that associate to every object `C` of `Alf/k` a module `F(C)` over `C` and to
every morphism `φ : C → D` of `Alf/k` a `k`-linear map `F(φ) : F(C) → F(D)` such that, if `x ∈ F(C)` and `λ ∈ C`:

```text
F(φ)(λ x) = φ(λ) F(φ)(x).
```

By Exposé I, 3.1, such an `F` is equipped with a structure of `O_k`-module, if one denotes by `O_k` the `k`-functor in
rings that associates to every object `C` of `Alf/k` the ring underlying `C`.

<!-- original page 495 -->

**Definitions.** *(i) An `O_k`-module `F` will be said to be* admissible *if every morphism `φ : C → D` of `Alf/k`
induces a bijection of `D ⊗_C F(C)` onto `F(D)`.*[^N.D.E-VII_B-43]

*(ii) One says that `F` is* flat *if it is admissible and if, for every object `C` of `Alf/k`, `F(C)` is a flat
`C`-module.*[^N.D.E-VII_B-44]

For example, if `M` is a `k`-module (not necessarily pseudocompact), we shall denote (as in Exposé I, 4.6.1) by `W(M)`
the `O_k`-module `C ↦ C ⊗_k M`; then `W(M)` is flat when `M` is flat over `k`.

Moreover, the functor `M ↦ W(M)` has as right adjoint the functor that associates to every `O_k`-module `F` the
`k`-module `lim_𝓁 F(k/𝓁)`, where `𝓁` ranges over the open ideals of `k`.

#### 1.2.2.

<!-- label: III.VII_B.1.2.2 -->

In what follows, an `O_k`-module will always be denoted by a boldface letter such as `**F**`; when `k` is artinian, we
shall then write simply `F` instead of `**F**(k)`. In this case, it goes without saying that the functor `**F** ↦ F`
induces an equivalence of the category of flat `O_k`-modules onto that of flat `k`-modules! The terminology we have
adopted has therefore only the goal of allowing us to reason "as if `k` were always artinian".

In accordance with Exposé I § 3.1, we shall use analogous conventions for other algebraic structures: thus, an
`O_k`-*algebra* (resp. an `O_k`-coalgebra, resp. an `O_k`-Lie algebra, resp. an `O_k`-`p`-Lie algebra) will consist of
the datum of an `O_k`-module `**M**` and, for every object `C` of `Alf/k`, of a structure of `C`-algebra (resp.
`C`-coalgebra, resp. `C`-Lie algebra, resp. `C`-`p`-Lie algebra) on `**M**(C)`; one assumes moreover that, for every
morphism `φ : C → D` of `Alf/k`, the map from `D ⊗_C **M**(C)` to `**M**(D)` induced by `**M**(φ)` is a homomorphism of
`D`-algebras (resp. `D`-coalgebras, etc.).

Note finally that, if `**F**` and `**G**` are two `O_k`-modules, `**F** ⊗_k **G**` will denote the `O_k`-module
`C ↦ **F**(C) ⊗_C **G**(C)`.

#### 1.2.3.

<!-- label: III.VII_B.1.2.3 -->

[^N.D.E-VII_B-45] We begin with the following lemma.

<!-- original page 523 -->

**Lemma 1.2.3.A.** *Let `k → K` be a morphism of pseudocompact rings, `B` a pseudocompact `K`-module, and `M` a
(topology-free) projective `k`-module. One has a canonical isomorphism of pseudocompact `K`-modules*

```text
(2)     θ : Hom_k(M, k) ⊗̂_k B ⥲ Hom_k(M, B).
```

<!-- label: III.VII_B.1.2.3.A -->

Here, `M^* = Hom_k(M, k)` is endowed with the topology defined in 0.2.2, which makes it a pseudocompact `k`-module, and
the topology of `Hom_k(M, B)` is defined analogously: a basis of neighborhoods of `0` is formed by the following
`K`-submodules, where `x ∈ M` and `B'` is an open `K`-submodule of `B`:

```text
ℋ(x, B') = {f ∈ Hom_k(M, B) | f(x) ∈ B'}.
```

Finally, `M^* ⊗̂_k B` is the pseudocompact `K`-module deduced from `M^*` by base change, cf. 0.5.A.

This being so, `θ` is evidently an isomorphism when `M = k`; moreover, both sides of (2), considered as functors in `M`,
transform direct sums into products (in particular, commute with finite direct sums). One thus obtains that (2) is an
isomorphism when `M` is a free `k`-module, and then when `M` is projective.

<!-- original page 496 -->

**Definition 1.2.3.B.** *Let `N` be a pseudocompact `k`-module. We denote by `**V_k^f**(N)` or
`**N**^†`[^N.D.E-VII_B-46] the `O_k`-module that associates to every `C ∈ Ob Alf/k` the `C`-module `(C ⊗̂_k N)^†` dual
of `C ⊗̂_k N` (0.2.2), i.e. the `C`-module*

```text
Hom_c(C ⊗̂_k N, C) ≃ Hom_c(N, C|_k),
```

*where `C|_k` denotes the `k`-module `C` obtained by restriction of scalars. This `O_k`-module `**V_k^f**(N)` will be
called the* dual *of `N`.*

<!-- label: III.VII_B.1.2.3.B -->

If `k_𝔪` is a local component of `k`, then for every object `C` of `Alf/k`,

```text
Hom_c(k_𝔪, C|_k) = C_𝔪 = C ⊗_k k_𝔪
```

is a projective `C`-module, and moreover one has `D ⊗_C C_𝔪 = D_𝔪` for every morphism `C → D` of `Alf/k`; so
`**V_k^f**(k_𝔪)` is a flat `O_k`-module (cf. 1.2.1). Since every projective pseudocompact `k`-module is a product of
modules `k_𝔪` (cf. Prop. 0.2.1), one deduces from Corollary 0.2.F the:

**Corollary 1.2.3.C.** *`**V_k^f**(N)` is a flat `O_k`-module when `N` is a projective pseudocompact `k`-module.*

<!-- label: III.VII_B.1.2.3.C -->

**Definition 1.2.3.D.** *Conversely, if `**M**` is an admissible `O_k`-module (cf. 1.2.1),*[^N.D.E-VII_B-47] *we call*
dual *of `**M**` and denote by `Γ^*(**M**)` the pseudocompact `k`-module defined as follows. As `𝓁` ranges over the open
ideals of `k`, we endow each `k/𝓁`-module*

```text
**M**(k/𝓁)^* = Hom_{k/𝓁}(**M**(k/𝓁), k/𝓁)
```

*with the topology described in 0.2.2, which makes it a pseudocompact `k`-module. Since
`**M**(k/𝓁) ≃ **M**(k/𝓁') ⊗ (k/𝓁)` for `𝓁 ⊃ 𝓁'`, one has transition morphisms:*

```text
Hom_{k/𝓁'}(**M**(k/𝓁'), k/𝓁') ⟶ Hom_{k/𝓁'}(**M**(k/𝓁'), k/𝓁) = Hom_{k/𝓁}(**M**(k/𝓁), k/𝓁),
```

*and by definition `Γ^*(**M**)` is the inverse limit of this filtered inverse system of pseudocompact `k`-modules.*

<!-- label: III.VII_B.1.2.3.D -->

<!-- original page 524 -->

From now on, suppose moreover that `**M**` is a flat `O_k`-module (cf. 1.2.1); then each `**M**(k/𝓁')` is a projective
`(k/𝓁')`-module, so the transition morphisms above are surjective, and hence so are the projections
`Γ^*(**M**) → **M**(k/𝓁)^*`, since in `PC(k)` filtered inverse limits are exact.

If `τ : k → K` is a morphism of pseudocompact rings, we shall denote by `**M** ⊗_k K` or simply `**M_K**` the
`O_K`-functor defined as follows. If `C` is a `K`-algebra of finite length, then the kernel of `k → C` is an open ideal
`𝓁`, and one sets `**M_K**(C) = **M**(k/𝓁) ⊗_k C`; one then has `**M_K**(C) = **M**(k/𝓁') ⊗_k C` for every open ideal
`𝓁'` contained in `𝓁`. One then defines `Γ^*_K(**M_K**)` as the inverse limit, for `I` ranging over the open ideals of
`K`, of the pseudocompact `K`-modules:

```text
Hom_{K/I}(**M_K**(K/I), K/I) = Hom_{k/𝓁}(**M**(k/𝓁), K/I),
```

where in the right-hand term `𝓁` is any open ideal of `k` such that `τ(𝓁) ⊂ I`. Moreover, by 1.2.3.A, the right-hand
side is identified with `**M**(k/𝓁)^* ⊗̂_k (K/I)`. Since the projections `Γ^*(**M**) → **M**(k/𝓁)^*` are surjective, one
sees that the inverse limit of `**M**(k/𝓁)^* ⊗̂_k (K/I)` is nothing but the pseudocompact `K`-module `Γ^*(**M**) ⊗̂_k K`
(cf. 0.5.A). One has thus obtained that, for every flat `O_k`-module `**M**`, the formation of `Γ^*(**M**)` commutes
with extension of the base, i.e. one has

```text
(⋆)     Γ^*_K(**M** ⊗_k K) ≃ Γ^*(**M**) ⊗̂_k K.
```

**Proposition 1.2.3.E.** *(i) The functors `N ↦ **V_k^f**(N)` and `**M** ↦ Γ^*(**M**)` define an anti-equivalence
between the category of projective pseudocompact `k`-modules and that of flat `O_k`-modules.*[^N.D.E-VII_B-48]

*(ii) Moreover, if `k → K` is a morphism of pseudocompact rings, then the previous anti-equivalence "commutes with base
change" in the following sense: if `N ≃ Γ^*(**M**)`, then `N ⊗̂_k K ≃ Γ^*_K(**M** ⊗_k K)`.*

<!-- label: III.VII_B.1.2.3.E -->

*Proof.* On the one hand, one has a natural transformation `φ_N : N → Γ^*(**V_k^f**(N))`. Since the functor
`Γ^* ∘ **V_k^f**` commutes with products, by 0.3.5 and 0.2.F, it suffices to verify that `φ_N` is an isomorphism when
`N` is a local component `k_𝔪` of `k`. In this case, for every open ideal `𝓁` of `k` contained in `𝔪`, the natural
morphism

```text
(k/𝓁)_𝔪 ⟶ Hom_{k/𝓁}(Hom_c(k_𝔪 ⊗̂ k/𝓁, k/𝓁), k/𝓁)
```

is an isomorphism, whence the result.

<!-- original page 525 -->

On the other hand, let `**M**` be a flat `O_k`-module. Let us show that `Γ^*(**M**) = lim **M**(k/𝓁)^*` is a projective
object of `PC(k)`. Let `N → N'` be a surjective morphism between objects of `LF(k)`. By 0.2.F (i) and (ii), it suffices
to show that the natural map

```text
colim Hom_c(**M**(k/𝓁)^*, N) ⟶ colim Hom_c(**M**(k/𝓁)^*, N')
```

is surjective. But this is clear, because `N` and `N'` are `k/𝓁_0`-modules for some open ideal `𝓁_0`; so if `𝓁 ⊂ 𝓁_0`,
every morphism `**M**(k/𝓁)^* → N'` lifts to a morphism `**M**(k/𝓁)^* → N`, since `**M**(k/𝓁)^*` is a projective object
of `PC(k/𝓁)`.

One has a morphism `ψ : **M** → **V_k^f**(Γ^*(**M**))` of functors from `Alf/k` to `(Sets)`. Let `B` be an object of
`Alf/k`; let us show that

```text
(1)     ψ(B) : **M**(B) ⟶ **V_k^f**(Γ^*(**M**))(B) = Hom_c(lim_𝓁 **M**(k/𝓁)^* ⊗̂_k B, B)
```

is a bijection (in the equality above, we have used the fact that `⊗̂` commutes with filtered inverse limits). Let `𝓁_0`
be an open ideal of `k` contained in the kernel of `k → B`. By Lemma 1.2.3.A, for every `𝓁 ⊂ 𝓁_0`, one has a canonical
isomorphism of pseudocompact `B`-modules:

```text
**M**(k/𝓁)^* ⊗̂_k B ⥲ Hom_{k/𝓁}(**M**(k/𝓁), B)
```

and, since `**M**(B) = **M**(k/𝓁) ⊗_{k/𝓁} B`, the right-hand side equals `Hom_B(**M**(B), B)`. So the inverse system in
(1) is constant for `𝓁 ⊂ 𝓁_0`, and (1) reduces to the canonical morphism

```text
**M**(B) ⟶ Hom_c(Hom_B(**M**(B), B), B),
```

which is an isomorphism by 0.2.2, since `B` is artinian and `**M**(B)` a projective `B`-module. This proves point (i) of
the proposition, and point (ii) follows from the isomorphism (⋆) established above.

**Remark 1.2.3.F.** *Let us return to the statement of the proposition, and suppose moreover that `N` is a topologically
free pseudocompact `k`-module. In this case, one can choose "coherently" bases for the `C`-modules `**V_k^f**(N)(C)`.*

<!-- label: III.VII_B.1.2.3.F -->

Indeed, let `(n_i)` be a pseudobasis of `N` (0.2.1) and `n^C_i` the canonical image of `n_i` in `C ⊗̂_k N`, for
`C ∈ Alf/k`. If one defines the element `δ^C_i` of `(C ⊗̂_k N)^†` by the equalities `δ^C_i(n^C_i) = 1` and
`δ^C_i(n^C_j) = 0` for `i ≠ j`, the family `(δ^C_i)` is a basis of `**V_k^f**(N)(C)`; moreover, for every morphism
`φ : C → D` of `Alf/k`, `**V_k^f**(N)(φ)` sends `δ^C_i` to `δ^D_i`.

#### 1.2.4.

<!-- label: III.VII_B.1.2.4 -->

[^N.D.E-VII_B-49] For every pseudocompact `k`-module `E`, let `Ŝ_k(E)` be the *completed symmetric algebra* of `E`,
defined as follows. Let `T_k(E)` be the direct sum of the pseudocompact `k`-modules:

```text
⊗̂^n_k E = E ⊗̂_k ⋯ ⊗̂_k E   (n ⩾ 0; if n = 0, ⊗̂^0_k E = k);
```

one makes `T_k(E)` into a graded `k`-algebra by defining the multiplication in the usual way; <!-- original page 497 -->
let `S_k(E)` be the quotient of `T_k(E)` by the homogeneous ideal whose `n`-th component is the closed `k`-submodule of
`⊗̂^n_k E` generated by the elements:

```text
x_1 ⊗̂ ⋯ ⊗̂ x_i ⊗̂ x_{i+1} ⊗̂ ⋯ ⊗̂ x_n − x_1 ⊗̂ ⋯ ⊗̂ x_{i+1} ⊗̂ x_i ⊗̂ ⋯ ⊗̂ x_n.
```

If one denotes by `S^n_k(E)` this quotient, `S_k(E)` is obviously a graded `k`-algebra with `n`-th component `S^n_k(E)`.

One endows `S_k(E)` with the linear topology defined by the set `Υ` of ideals `𝓁` such that `S_k(E)/𝓁` is a `k`-module
of finite length and that `S^n_k(E) ∩ 𝓁` is an open submodule of `S^n_k(E)` for every `n`. Then the profinite algebra
`Ŝ_k(E)` is the separated completion of `S_k(E)` for this topology.[^N.D.E-VII_B-50]

We denote by `**V^f_k**(E)` the formal `k`-variety `Spf(Ŝ_k(E))`. It represents the `k`-functor `**V_k^f**(E)`, i.e.,
for every object `C` of `Alf/k`, one has a canonical isomorphism:

```text
**V_k^f**(E)(C) = Hom_c(E, C|_k) ⥲ Hom_{Alp/k}(Ŝ_k(E), C) = Hom_{Vaf/k}(Spf(C), **V^f_k**(E)).
```

In all the sequel, we identify `**V^f_k**(E)` with the `k`-functor `**V_k^f**(E)`.

#### 1.2.5.

<!-- label: III.VII_B.1.2.5 -->

By 1.2.4, the zero morphism from `E` to `k` is associated with a morphism of profinite algebras `π : Ŝ_k(E) → k`; this
morphism `π` induces the zero map on `S^n_k(E)` for `n ⩾ 1` and defines a section of the structure morphism
`**V^f_k**(E) → Spf(k)`.

We shall denote by `**V^{f,0}_k**(E)` the formal variety which has as points the images of the points of `Spf(k)` under
the section `Spf(π)` and which has the same local algebras as `**V^f_k**(E)` at these points.[^N.D.E-VII_B-51]

Then, the affine algebra of `**V^{f,0}_k**(E)` is the separated completion of `S_k(E)` for the topology defined by the
ideals `𝓁 ∈ Υ` (cf. 1.2.4) that contain `S^n_k(E)` for `n` large enough. One deduces that it is the infinite product:

```text
k[[E]] = k × E × S^2_k(E) × S^3_k(E) × ⋯
```

On the other hand, let `C` be an object of `Alf/k`, `u` an element of `**V^f_k**(C) = Hom_c(E, C)`, and `φ : Ŝ_k(E) → C`
the corresponding morphism of profinite `k`-algebras. Then `Ker(φ)` is an open ideal (i.e. `φ` belongs to
`**V^{f,0}_k**(C)`) if and only if `Ker(φ)` contains `S^n_k(E)` for `n` large enough, i.e., if and only if `u(E)` is
contained in the radical `r(C)` of `C`. Therefore: for every object `C` of `Alf/k`, one has canonical isomorphisms:

<!-- original page 498 -->

```text
**V^{f,0}_k**(E)(C) ≃ Hom_{Alp/k}(k[[E]], C) ≃ Hom_c(E, r(C)).
```

#### 1.2.6.

<!-- label: III.VII_B.1.2.6 -->

A formal `k`-variety `V` is said to be *of finite length* if its affine algebra is. Likewise, if `S` is a scheme, an
`S`-scheme `X` is said to be of *finite length* if `X` is finite over `S` and if the direct image of `O_X` on `S` is an
`O_S`-module of finite length.[^N.D.E-VII_B-52] So, to give an `S`-scheme of finite length `X` is "the same thing" as to
give a finite set `{s_1, …, s_n}` of closed points of `S`, and at each of these points, an `O_{S, s_i}`-algebra of
finite length.

One sees therefore that the `S`-schemes of finite length identify with the formal varieties of finite length over the
formal scheme `Ŝ` that follows. The topological space underlying `Ŝ` is the set of closed points of `S` endowed with the
discrete topology; if `s` is such a closed point, the structure sheaf `O_{Ŝ}` has as stalk `O_{Ŝ, s}` at `s` the
separated completion `Ô_{S, s}` of `O_{S, s}` for the linear topology defined by the ideals of finite colength; one
therefore has `Ŝ = Spf 𝓐(Ŝ)`, where `𝓐(Ŝ)` is the product of the `Ô_{S, s}`, for `s` ranging over the closed points of
`S`, endowed with the product topology.

**Definition.** *If `X` is an `S`-scheme, we denote by `X̂/Ŝ` the formal variety over `k = 𝓐(Ŝ)` defined as follows. The
underlying topological space is formed by the points `x ∈ X` such that `[κ(x) : κ(s)] < ∞`, where `s` is the image of
`x` in `S`; the local ring `O_{X̂/Ŝ, x}` is the separated completion of `O_{X, x}` for the linear topology defined by
the ideals `I` of `O_{X, x}` such that `O_{X, x}/I` is of finite length as an `O_{S, s}`-module (N.B. since
`[κ(x) : κ(s)] < ∞`, this is equivalent to saying that `O_{X, x}/I` is of finite length as an `O_{X, x}`-module).*

Let `Vafℓf/Ŝ` be the category of formal varieties of finite length over `Ŝ` (identified with that of `S`-schemes of
finite length). By 1.1 and 1.2.1, the category `Vaf/Ŝ` of formal varieties over `Ŝ` is equivalent to that of left-exact
contravariant functors from `Vafℓf/Ŝ` to `(Sets)`. In particular, for every `S`-scheme `X`, the functor
`T ↦ Hom_{(Sch/S)}(T, X)`, from `Vafℓf/Ŝ` to `(Sets)`, is such a left-exact functor, hence corresponds to a formal
variety over `Ŝ`. The latter is nothing but `X̂/Ŝ`:[^N.D.E-VII_B-53]

**Proposition.** *For every `S`-scheme `X`, the functors*

```text
Hom_{Vaf/Ŝ}(−, X̂/Ŝ)     and     Hom_{(Sch/S)}(−, X)
```

*have the same restriction to `Vafℓf/Ŝ`. One thus obtains a functor `X ↦ X̂/Ŝ` from `(Sch/S)` to `Vaf/Ŝ` which commutes
with finite inverse limits.*

<!-- original page 528 -->

Indeed, one sees easily that the formal variety `X̂/Ŝ` has the required property, and that the correspondence `X ↦ X̂/Ŝ`
is functorial. Let us prove the second assertion.

Set `**S** = (Sch/S)` and `**V** = Vaf/Ŝ`, and write `X̂` instead of `X̂/Ŝ`. We know (1.2.B) that `**V**` possesses
arbitrary inverse limits. Let `(X_i)_{i ∈ I}` be an inverse system in `**S**` and suppose that `X = lim X_i` exists in
`**S**` (which is the case if `I` is finite). Since the functor that associates to every object `Y` of `**S**` (resp.
`V` of `**V**`) the functor `h^Y = Hom_{**S**}(−, Y)` (resp. `h^V = Hom_{**V**}(−, V)`) commutes with inverse limits,
one has, for every `S`-scheme `T` of finite length, functorial isomorphisms:

```text
Hom_{**S**}(T, X) ≃ lim Hom_{**S**}(T, X_i) ≃ lim Hom_{**V**}(T, X̂_i) ≃ Hom_{**V**}(T, lim X̂_i).
```

Consequently, the functor `X ↦ X̂/Ŝ` commutes with inverse limits when they exist in `(Sch/S)`; in particular, it
commutes with finite inverse limits.

### 1.3.

<!-- label: III.VII_B.1.3 -->

<!-- original page 499 -->

**Proposition 1.3.** *Let `f : X → Y` be a morphism of formal varieties over `k`, `A` and `B` the affine algebras of `X`
and `Y`, `g : B → A` the morphism induced by `f`. Then `f` is a monomorphism of `Vaf/k` if and only if `g` is a
surjection.*

<!-- label: III.VII_B.1.3 -->

[^N.D.E-VII_B-54] By 1.1, `A ↦ Spf(A)` is an anti-equivalence of `Alp/k` onto `Vaf/k`, so `f` is a monomorphism if and
only if `g` is an epimorphism, and this is the case if `g` is surjective.

Conversely, suppose that `g` is an epimorphism and let us show that it is surjective. For every `𝔫 ∈ Υ(B)`, set
`A_𝔫 = A ⊗̂_B B_𝔫`; by 0.4, `A` is a pseudocompact `B`-module, hence is the product of the `A_𝔫` (cf. 0.3.6). Then `g`
is the product of the morphisms `g_𝔫 : B_𝔫 → A_𝔫` deduced from `g` by base change. These are still epimorphisms, which
reduces us to proving the result when `B` is local with maximal ideal `𝔫`. Set `K = B/𝔫`.

By Nakayama's Lemma 0.3.3, it suffices to show that the morphism `g ⊗̂_B K` is surjective; it is deduced from `g` by
base change, so is an epimorphism of `Alp/K`. One can therefore assume that `B = K` is a field. Now `f` is a
monomorphism if and only if the diagonal morphism `X → X ×_Y X` is an isomorphism, that is, if the homomorphism
`x ⊗̂_K x' ↦ x x'` is an isomorphism of `A ⊗̂_K A` onto `A`. Since `K` is a field, this implies `A = K`.

**Remark.**[^N.D.E-VII_B-55] *It follows from the proposition that every monomorphism `f : X → Y` of formal varieties is
an isomorphism of `X` onto a (necessarily closed!) formal subvariety of `Y`.*

#### 1.3.1.

<!-- label: III.VII_B.1.3.1 -->

The preceding proposition implies in particular that every monomorphism `f : X → Y` of `Vaf/k` is effective (cf. IV
1.3).[^N.D.E-VII_B-56] It is not the same for epimorphisms, as one easily sees by slightly modifying the counterexample
of Exposé V, § 2.c);[^N.D.E-VII_B-57] this is why we shall consider a sympathetic class of effective epimorphisms.

<!-- original page 529 -->

**Lemma.**[^N.D.E-VII_B-58] *Let `f : X → Y` be a morphism of formal `k`-varieties and let `A`, `B` be the affine
algebras of `X`, `Y` and `f^♮ : B → A` the morphism induced by `f`. The following conditions are equivalent:*

*(i) For every `x ∈ X`, the homomorphism `f^♮_x : O_{Y, f(x)} → O_{X, x}` makes `O_{X, x}` a topologically free
pseudocompact `O_{Y, f(x)}`-module.*

*(ii) For every `y ∈ Y`, the local component `A_y = ∏_{f(x) = y} O_{X, x}` is a topologically free pseudocompact
`B_y`-module.*

*(iii) `f^♮ : B → A` makes `A` a projective pseudocompact `B`-module.*

*(iv) The functor `PC(B) → PC(A)`, `M ↦ M ⊗̂_B A`, is exact.*

*If these conditions are satisfied, one says that `f` is* topologically flat.

The implications (i) ⇒ (ii) ⇔ (iii) ⇔ (iv) follow from 0.2.F (iii) and 0.3.7. Conversely, assume (ii) holds and let
`x ∈ X` and `y = f(x)`. Since `O_{X, x}` is a direct factor of `A_y`, it is a projective pseudocompact `B_y`-module,
hence topologically free by 0.2.1 (since `B_y` is local).

On the other hand, a morphism `f : X → Y` of formal `k`-varieties is said to be *surjective* if it induces a surjection
of the underlying sets.

<!-- original page 500 -->

**Proposition.** *Let `f : X → Y` be a surjective and topologically flat morphism of formal `k`-varieties. Then `f` is
an effective epimorphism (cf. IV 1.3).*

Indeed, let `A`, `B` be the affine algebras of `X`, `Y` and `g : B → A` the morphism induced by `f`. We must show that
`Y` is identified with the cokernel of `X ×_Y X ⇒ X`, i.e., that for every `𝔫 ∈ Υ(B)`, `B_𝔫` is identified with the
subring of `A_𝔫 = A ⊗̂_B B_𝔫` formed by the `a` such that `a ⊗̂ 1 = 1 ⊗̂ a`.

We can therefore assume `B` local, with maximal ideal `𝔫`. Our hypothesis then means that `g` makes `A` a topologically
free and nonzero `B`-module. By Nakayama's Lemma 0.3.3, `A / 𝔫 A` is not zero, so the morphism `g' : B/𝔫 → A/𝔫 A`
deduced from `g` is injective. By Lemma 1.3.2 below, `B` is a direct factor of `A` as a `B`-module, say `A = B ⊕ A'`; it
follows that `B` is identified with the part of `A` formed by the `a` such that `a ⊗̂_B 1 = 1 ⊗̂_B a`.

#### 1.3.2.

<!-- label: III.VII_B.1.3.2 -->

**Lemma 1.3.2.** *Let `B` be a local pseudocompact ring, `𝔫` its maximal ideal, `M` and `N` two projective pseudocompact
`B`-modules, and `g` a morphism `M → N`. If `(B/𝔫) ⊗̂_B g` is injective, `g` is an isomorphism of `M` onto a direct
factor of `N`.*

<!-- label: III.VII_B.1.3.2 -->

Indeed, suppose `g' = (B/𝔫) ⊗̂_B g` is injective. Since `B/𝔫` is a field, `g'` then has a retraction `r'`. Let `p` and
`q` be the canonical projections of `M` and `N` onto `M/𝔫 M` and `N/𝔫 N`; since `N` is projective, there exists a
morphism `r : N → M` such that `p ∘ r = r' ∘ q`; consequently, `r'` is deduced from `r` by passage to the quotient.
Then, since `r' ∘ g'` is an isomorphism, so is `r ∘ g`, by 0.3.4 (since `M` is projective). Let `s` be the inverse
isomorphism of `r ∘ g`; then `s ∘ r` is a retraction of `g`.

#### 1.3.3.

<!-- label: III.VII_B.1.3.3 -->

**Proposition 1.3.3.** *Let `f : X → Y` and `g : Y → Z` be morphisms of formal `k`-varieties.*

*(i) If `f` and `g` are topologically flat, so is `g ∘ f`.*

*(ii) If `f` and `g ∘ f` are topologically flat and if `f` is surjective, `g` is topologically flat.*

*(iii) If `f` is topologically flat, so is `f ×_Y Y'` for every base change `Y' → Y`.*

<!-- label: III.VII_B.1.3.3 -->

<!-- original page 501 -->

Assertions (i) and (iii) are clear. To prove (ii), let `A`, `B`, `C` be the affine algebras of `X`, `Y`, `Z`, and
`f' : B → A` and `g' : C → B` the morphisms induced by `f` and `g`. Since `g ∘ f` is topologically flat, `f' ∘ g'` makes
`A` a projective pseudocompact `C`-module; likewise, `f'` makes `A` a projective pseudocompact `B`-module that is also
faithful. As `P` ranges over the pseudocompact `C`-modules and `N` over the pseudocompact `B`-modules, the functors
`P ↦ P ⊗̂_C A` and `N ↦ N ⊗̂_B A` are therefore exact; since the second is moreover faithful, the functor `P ↦ P ⊗̂_C B`
is exact; by 0.3.7, `B` is therefore a projective pseudocompact `C`-module.

#### 1.3.4.

<!-- label: III.VII_B.1.3.4 -->

**Proposition 1.3.4.** *Let `S` be a scheme, `Y` a locally noetherian `S`-scheme, and `f : X → Y` an `S`-morphism
locally of finite type and faithfully flat, so that `f` is an effective epimorphism, i.e., the sequence below is exact
(cf. IV 6.3.1 (iv) and IV 1.3):*

```text
(∗)      X ×_Y X ⇒ X ─f→ Y.
```

*Then the morphism of formal `Ŝ`-varieties `f̂ : X̂/Ŝ → Ŷ/Ŝ` (cf. 1.2.6) is surjective and topologically flat, and the
sequence below, deduced from (∗), is exact:*

```text
(∗̂)      X̂ ×_{Ŷ} X̂/Ŝ ⇒ X̂/Ŝ ─f̂→ Ŷ/Ŝ.
```

<!-- label: III.VII_B.1.3.4 -->

Indeed, let `y` be a point of `Y` with projection `s` on `S` and such that `κ(y)` is a finite extension of the residue
field `κ(s)` of `s`. Since `f` is surjective and locally of finite type, `f^{-1}(y)` is non-empty and locally of finite
type over `κ(y)`; the closed points of `f^{-1}(y)` are then the points of `X̂/Ŝ` projecting onto `y`. This shows that
`f̂` is surjective.

<!-- original page 531 -->

[^N.D.E-VII_B-59] Let `x` be a closed point of `f^{-1}(y)`. Since `Y` is locally noetherian and `f` locally of finite
type, the local ring `O_{Y, y}` (resp. `O_{X, x}`) is noetherian, so the powers of the maximal ideal are of finite
colength, so that the local ring of `Ŷ/Ŝ` at `y` (resp. of `X̂/Ŝ` at `x`) is the completion `Ô_{Y, y}` of `O_{Y, y}`
(resp. `Ô_{X, x}` of `O_{X, x}`) for the `𝔪`-adic topology. Then, since `f` is flat, `Ô_{X, x}` is flat over `Ô_{Y, y}`,
by (SGA 1, IV 5.8). Hence, by 0.3.8, `Ô_{X, x}` is a topologically free `Ô_{Y, y}`-module. This shows that `f̂` is
topologically flat.

So, by Proposition 1.3.1, `f̂` is an effective epimorphism, i.e., the sequence below (where one has written `X̂` instead
of `X̂/Ŝ`) is exact:

```text
X̂ ×_{Ŷ} X̂ ⇒ X̂ ─f̂→ Ŷ.
```

Moreover, by 1.2.6, one has a natural isomorphism (which in particular commutes with the projections on `X̂`):

```text
X̂ ×_Y X ≃ X̂ ×_{Ŷ} X̂.
```

Consequently, the sequence `(∗̂)` is exact.

#### 1.3.5.

<!-- label: III.VII_B.1.3.5 -->

Let `k` be a pseudocompact ring. A formal variety `X` over `k` is said to be *topologically flat* if its affine algebra
`A` is a projective pseudocompact `k`-module, i.e., if the structure morphism `X → Spf(k)` is topologically flat.

[^N.D.E-VII_B-60] Let us first note that 0.2.2 and 0.3.6 imply the following result (analogous to VII_A, 3.1.1).

**Lemma 1.3.5.A.** *Suppose `k` artinian. The functors `A ↦ A^† = Hom_c(A, k)` and `C ↦ C^* = Hom_k(C, k)` define an
anti-equivalence between the category of topologically flat profinite `k`-algebras, and that of flat `k`-coalgebras.*

<!-- label: III.VII_B.1.3.5.A -->

Indeed, if `A` is a topologically flat profinite `k`-algebra, then by 0.3.6, one has an isomorphism of `k`-modules:

```text
A^† ⊗_k A^† ⥲ (A ⊗̂ A)^†,
```

so that the multiplication `A ⊗̂ A → A` induces by duality a `k`-coalgebra structure on `A^†`. The rest then follows
from Proposition 0.2.2.

Let us return to the case of an arbitrary pseudocompact ring `k`.

**Definition 1.3.5.B.** *To every formal `k`-variety `X` whose affine ring `A` is a projective pseudocompact `k`-module,
one associates a flat `O_k`-coalgebra `**H**(X)`, defined as follows.*

<!-- label: III.VII_B.1.3.5.B -->

Denote by `**H**(X)` the `O_k`-module `**V_k^f**(A)`, "*dual of `A`*"; it is a flat `O_k`-module, since the
pseudocompact `k`-module underlying `A` is projective (cf. 1.2.3.C). Moreover, by 0.3.6, one has:

<!-- original page 503 -->

```text
**V_k^f**(A ⊗̂ A) ≃ **V_k^f**(A) ⊗ **V_k^f**(A),
```

and so the multiplication of `A` induces by transposition a diagonal morphism:

```text
**H**(X) = **V_k^f**(A) ⟶ **V_k^f**(A ⊗̂ A) = **H**(X) ⊗ **H**(X),
```

which makes `**H**(X)` a flat `O_k`-coalgebra. We shall say that `**H**(X)` is the *coalgebra of `X` over `O_k`*.

**Definition 1.3.5.C.** *Conversely, to every `O_k`-coalgebra `**C**` one can associate a `k`-functor (cf. 1.2.1)
`Spf^*(**C**)`, defined as follows. For every object `B` of `Alf/k`, one sets (with the notations of VII_A 3.1):*

```text
(1)   Spf^*(**C**)(B) = Hom_{B-coalg.}(B, **C**(B))
                       = {x ∈ **C**(B) | ε_{**C**(B)}(x) = 1 and Δ_{**C**(B)}(x) = x ⊗ x}.
```

<!-- label: III.VII_B.1.3.5.C -->

[^N.D.E-VII_B-61] Assume moreover that the `O_k`-module underlying `**C**` is admissible (cf. 1.2.1), and set

```text
(2)   A = Γ^*(**C**) = lim_𝓁 **C**(k/𝓁)^*.
```

Then the algebra structures on each `**C**(k/𝓁)^*` endow `A` with a structure of profinite `k`-algebra. For every object
`B` of `Alf/k`, one has:

```text
(3)   Hom_{Vaf/k}(Spf(B), Spf(A)) = Hom_{Alp/k}(A, B) = Hom_{Alp/B}(A ⊗̂ B, B).
```

Assume finally that `**C**` is a flat `O_k`-module. Then, by 1.2.3.E, `A = Γ^*(**C**)` is a projective pseudocompact
`k`-module. Moreover, we saw in the proof of *loc. cit.* that, if `𝓁_0` is an open ideal of `k` contained in the kernel
of `k → B`, one has isomorphisms

```text
(4)   A ⊗̂ B = lim_𝓁 **C**(k/𝓁)^* ⊗̂_k B ≃ Hom_{k/𝓁_0}(**C**(k/𝓁_0), B) ≃ Hom_B(**C**(B), B),
```

and we shall denote by `**C**(B)^*` the right-hand term. Finally, by Lemma 1.3.5.A applied to the artinian ring `B`, one
has a natural isomorphism

```text
(5)   Hom_{B-coalg.}(B, **C**(B)) ⥲ Hom_{Alp/B}(**C**(B)^*, B).
```

Then, combining (1), (5), (4), (3) and (2), one obtains, when `**C**` is a flat `O_k`-coalgebra, an isomorphism of
functors:

```text
(⋆)   Spf^*(**C**) ≃ Spf(A) = Spf(Γ^*(**C**)).
```

Consequently, if one denotes by `𝓐(X)` the affine algebra of a formal `k`-variety `X`, one obtains, taking 1.2.3.E into
account:

**Proposition 1.3.5.D.** *(i) The functors `X ↦ **H**(X) = **V_k^f**(𝓐(X))` and `**C** ↦ Spf^*(**C**) = Spf(Γ^*(**C**))`
define an equivalence between the category of topologically flat formal `k`-varieties and that of flat
`O_k`-coalgebras.*

*(ii) Moreover, this equivalence "commutes with base change": if `k → K` is a morphism of pseudocompact rings, then
`X ⊗̂_k K` corresponds to `**H**(X) ⊗_k K`.*

<!-- label: III.VII_B.1.3.5.D -->

#### 1.3.6.

<!-- label: III.VII_B.1.3.6 -->

<!-- original page 533 -->

In the rest of this Exposé, we shall several times define a topologically flat formal `k`-variety `X` by exhibiting the
coalgebra `**H**(X)`. We shall then need to interpret by means of `**H**(X)` certain geometric properties of `X`. We
give here an example of this situation: suppose given a section `σ` of the structure morphism `X → Spf(k)` and ask
ourselves under what condition `σ` induces an isomorphism on the underlying topological spaces.[^N.D.E-VII_B-62]

To begin, suppose `k` artinian. Let `(H, Δ, ε)` be a flat `k`-coalgebra, `H^+ = Ker(ε)` and `A = H^*` the profinite
`k`-algebra dual to `H`. Suppose given a morphism of `k`-coalgebras `k → H`, i.e., an element `φ` of `H` such that
`ε(φ) = 1` and `Δ(φ) = φ ⊗ φ`. On the one hand, `φ` defines a continuous algebra morphism `Φ : A → k`, and hence a
section `σ : Spf(k) → Spf(A)` of the projection `Spf(A) → Spf(k)`.

<!-- original page 504 -->

On the other hand, one defines `k`-submodules of `H` by setting `H_0 = k φ` and, for `n ⩾ 1`,

```text
H_n = {x ∈ H | Δ(x) − x ⊗ φ ∈ H_{n-1} ⊗ H^+};
```

this is also valid for `n = 0` if one sets `H_{-1} = (0)`. One sees, by induction on `n`, that `H_{n-1} ⊂ H_n`. We say
that `H_0 ⊂ H_1 ⊂ ⋯` is the *filtration of `H` defined by `φ`*.

**Remark.** *Since `Δ(H_n) ⊂ H_n ⊗ H_0 ⊕ H_{n-1} ⊗ H^+`, one has `Δ(H_n) ⊂ H_n ⊗ H`. Since `Δ` is cocommutative (i.e.
`σ ∘ Δ = Δ`, where `σ(a ⊗ b) = b ⊗ a`), one also has `Δ(H_n) ⊂ H ⊗ H_n`. When `H/H_n` is flat over `k`, it follows that
`H_n` is a sub-coalgebra of `H` (see also 1.3.6.A (iii) below). But in general, `Δ : H_n → H_n ⊗ H` does not factor
through `H_n ⊗ H_n`.*[^N.D.E-VII_B-63]

**Lemma 1.3.6.A.** *Let `k` be an artinian ring, `H` a flat `k`-coalgebra, `A = H^*` the dual profinite `k`-algebra, `φ`
an element of `H` such that `ε(φ) = 1` and `Δ(φ) = φ ⊗ φ`. Let `Φ : A → k` be the continuous algebra morphism,
`σ : Spf(k) → Spf(A)` the section of `Spf(A) → Spf(k)`, and `(H_n)` the filtration of `H` defined by `φ`. Set
`I = Ker Φ`.*

*(i) For every `n ⩾ 1`, `H_{n-1}` is the orthogonal in `H` of the closure `Ī^n` of `I^n`.*

*(ii) Consequently, `σ` induces a bijection of the underlying sets if and only if `H = ⋃_n H_n`.*[^N.D.E-VII_B-64]

*(iii) If moreover each `H/H_n` is flat over `k`, then for every `n ⩾ 0`,*

```text
(∗)     Δ(H_n) ⊂ ∑_{i=0}^n H_i ⊗ H_{n-i};
```

*in particular, each `H_n` is then a sub-coalgebra of `H`.*

<!-- label: III.VII_B.1.3.6.A -->

*Proof.* Note that, for every `x ∈ H`, the map `A → k`, `f ↦ f(x)` is continuous, so if `I^n` is annihilated by `x`, so
is its closure `Ī^n`. We set then, for every `n ⩾ 1`,

```text
(I^n)^⊥ = {x ∈ H | f(x) = 0, for every f ∈ I^n}.
```

Suppose that `σ : 𝔪 ↦ Φ^{-1}(𝔪)` is a bijection of `Spf(k)` onto `Spf(A)`. Since `I` is contained in the intersection of
the `Φ^{-1}(𝔪)`, it follows from 0.1.2 that the sequence of ideals `(Ī^n)` tends to `0`. Let then `x ∈ H`; since
`J(x) = {f ∈ A | f(x) = 0}` is an open and closed `k`-submodule of `A`, it contains `Ī^n` for `n` large enough; in other
words, `x ∈ (I^n)^⊥` for `n` large enough.

Conversely, suppose that `H = ⋃_n (I^n)^⊥`. Let `𝔭` be an open prime ideal of `A`; by the definition of the topology of
`A` (0.2.2), `𝔭` contains an open `k`-submodule of the form

```text
V(x_1, …, x_s) = {f ∈ A | f(x_1) = ⋯ = f(x_s) = 0}.
```

By hypothesis, there exists an integer `n` such that `x_1, …, x_s ∈ (I^n)^⊥`, and so `Ī^n ⊂ 𝔭`. Moreover, since `k` is
artinian, `Spf(k)` is a finite set `{𝔪_1, …, 𝔪_r}` and there exists an integer `t ⩾ 1` such that `(∏_i 𝔪_i)^t = 0`,
whence

```text
∏_i Φ^{-1}(𝔪_i)^t ⊂ I.
```

So `𝔭` contains the product of the `Φ^{-1}(𝔪_i)^{tn}`; since `𝔭` is prime, it follows that `𝔭` contains, hence equals,
one of the `Φ^{-1}(𝔪_i)`. One has thus shown that:

```text
σ is a bijection ⟺ H = ⋃_n (I^n)^⊥.
```

[^N.D.E-VII_B-65]

<!-- original page 535 -->

On the other hand, one has `H = k φ ⊕ H^+`; denote by `π` the projection `H → H^+` of kernel `k φ`. For every `n ⩾ 0`,
let `Δ^n` be the "iterated" comultiplication `H → H^{⊗(n+1)}`, `Δ̄^n` the composite of `Δ^n` with the projection
`π^{⊗(n+1)} : H^{⊗(n+1)} → (H^+)^{⊗(n+1)}`, and

```text
H'_n = Ker(Δ̄^n) = {x ∈ H | Δ^n(x) ∈ ∑_{i=0}^n H^{⊗(n-i)} ⊗ H_0 ⊗ H^{⊗i}}.
```

(One sets `Δ̄^0 = id_H`, whence `H'_0 = H_0`.) One sees easily, by induction on `n`, that

```text
(∗)     H_n ⊂ H'_n ⊂ (I^{(n+1)})^⊥.
```

Up to this point, one has not used the hypothesis that `H` is flat over `k`. Suppose now `H` flat, hence projective over
`k`, so that `A^† = H` by 0.2.2, and let us show that `H_n = (I^{(n+1)})^⊥`. This is clear for `n = 0`. Assume it
verified for `n < r`. Then `H_{r-1}` is the kernel of the morphism `H → (I^r)^†`, and so, since `H^+` is flat, the
morphism

```text
(H/H_{r-1}) ⊗ H^+ ⟶ (I^r)^† ⊗ H^+
```

is injective. On the other hand, the hypothesis implies that `I` is a projective pseudocompact `k`-module (since a
direct factor of `A = H^*`), whence, by 0.3.6,

```text
(I^r ⊗̂ I)^† ≃ (I^r)^† ⊗ I^† = (I^r)^† ⊗ H^+.
```

Then the exact sequence

```text
I^r ⊗̂ I ⟶ A ⟶ A/I^{r+1} ⟶ 0
```

<!-- original page 505 -->

gives by duality the exact sequence:

```text
(1)     (I^r)^† ⊗ H^+ ←δ─ H ←─ (A/I^{r+1})^† ←─ 0,
```

where `δ` is obtained by composing `Δ_H` with the projection:

```text
(2)     H ⊗ H ⟶ H ⊗ H^+ ⟶ (H/H_{r-1}) ⊗ H^+ ↪ (I^r)^† ⊗ H^+.
```

Now, for every `u ∈ H`, the projection of `Δ(u)` onto `H ⊗ H^+` is `Δ(u) − u ⊗ φ`. Then (1) and (2) show that if `u`
belongs to `(A/I^{r+1})^† = (I^{r+1})^⊥`, then `Δ(u) − u ⊗ φ` belongs to the kernel of the map
`H ⊗ H^+ → (H/H_{r-1}) ⊗ H^+`, that is, to `H_{r-1} ⊗ H^+`, so `u ∈ H_r`. This completes the proof of points (i) and
(ii), and also shows that `H_n = Ker(Δ̄^n)`.

Let us prove (iii). For every `i ⩾ 0`, set `H^+_i = H_i ∩ H^+`. Let `n ⩾ 1`. For every `x ∈ H^+_n`, `x̄ = x − ε(x) φ`
belongs to `H^+_n` and one has:

```text
Δ(x) = ε(x) φ ⊗ φ + x ⊗ φ + φ ⊗ x + Δ̄(x).
```

So it suffices to show that:

```text
Δ̄(H^+_n) ⊂ ∑_{i=1}^{n-1} H^+_i ⊗ H^+_{n-i}.
```

For every `i = 0, …, n - 1`, `Δ̄^n` factors as:

```text
                Δ̄                       Δ̄^i ⊗ Δ̄^{n-i-1}
H^+ ─────────→ H^+ ⊗ H^+ ──────────────────→ (H^+)^{⊗(i+1)} ⊗ (H^+)^{⊗(n-i)}
                ↓                                                  ↑ g
              H^+/H^+_i ⊗ H^+/H^+_{n-i-1} ────f─→ H^+ ⊗ (H^+)^{⊗(n-i)} / H^+_i.
```

Moreover, since `H^+/H^+_i` and `(H^+)^{⊗(n-i)}` are flat, the maps `f` and `g` above are injective. It follows that
`Δ̄(H^+_n)` is contained in `H^+_i ⊗ H^+ + H^+ ⊗ H^+_{n-i-1}`, for every `i = 0, …, n - 1`. Point (iii) then follows
from the lemma below, applied to `M = H^+` and `E_i = H^+_{i-1}`.

**Lemma 1.3.6.B.** *Let `k` be a ring, `0 = E_0 ⊂ E_1 ⊂ ⋯ ⊂ E_n ⊂ M` `k`-modules. Suppose `M/E_i` flat for every `i`.
Then one has the equality:*

```text
⋂_{i=0}^n (E_i ⊗ M + M ⊗ E_i) = ∑_{i=1}^n E_i ⊗ E_{n-i+1}.
```

<!-- label: III.VII_B.1.3.6.B -->

<!-- original page 536 -->

Denote by `K` (resp. `S`) the left-hand (resp. right-hand) term. One easily sees that `S ⊂ K`; let us show the converse.
For `i = 0, …, n`, set `K_i = K ∩ (E_i ⊗ M)`. For every `i = 1, …, n`, since `M/E_{n-i+1}` and `E_i/E_{i-1}` are flat,
the map `τ_i` below is injective, and the composite map:

```text
(E_i/E_{i-1}) ⊗ M ⟶ (E_i/E_{i-1}) ⊗ (M/E_{n-i+1}) ─τ_i→ (M/E_{i-1}) ⊗ (M/E_{n-i+1})
```

has kernel `(E_i/E_{i-1}) ⊗ E_{n-i+1}`. Since the image of `K_i` in `(E_i ⊗ M)/(E_{i-1} ⊗ M)` is contained in, and
contains, this kernel, one deduces that

```text
K_i = K_{i-1} + E_i ⊗ E_{n-i+1},
```

whence the lemma.

[^N.D.E-VII_B-66] To finish this paragraph, let us return to an arbitrary pseudocompact ring `k`. Let `(**H**, Δ, ε)` be
a flat `O_k`-coalgebra, `**H**^+ = Ker(ε)`, `A = Γ^*(**H**)` the dual profinite `k`-algebra, `X = Spf(A)`, so that
`**H** = **H**(X)` (cf. 1.3.5). Suppose given a morphism of `O_k`-coalgebras `φ : O_k → **H**`; it defines a continuous
morphism of `k`-algebras `A → k`, and hence a section `σ` of the structure morphism `X → Spf(k)`.

For every object `B` of `Alf/k`, denote `**H**_0(B) = φ(B) = B φ_B`, where `φ_B` is the element `φ(1_B)` of `**H**(B)`,
and one defines sub-`O_k`-modules `**H**_n` of `**H**`, by setting, for `n ⩾ 1`,

```text
**H**_n(B) = {u ∈ **H**(B) | Δ(u) − u ⊗ φ_B ∈ **H**_{n-1}(B) ⊗ **H**^+(B)}.
```

One thus obtains a filtration `**H**_0 ⊂ **H**_1 ⊂ ⋯` of `**H**(X)`. By what precedes, one has:

**Proposition.** *In order for `σ` to induce an isomorphism on the underlying topological spaces, it is necessary and
sufficient that `**H**(X)` be the union of the `**H**_n`.*

### 1.4. Theorem.

<!-- label: III.VII_B.1.4 -->

**Theorem 1.4.** *Let `k` be a pseudocompact ring and `d₀, d₁ : X₁ ⇒ X` an equivalence couple in `Vaf_/k` (cf. Exp. V, §
2.b) such that `d₁` is topologically flat.*

*(i) The canonical projection of `X` onto `X/X₁` (`= Coker(d₀, d₁)`) is surjective and topologically flat, and the
morphism `X₁ → X ×_{X/X₁} X` with components `d₀` and `d₁` is an isomorphism.*

*(ii) If `X` is topologically flat over `k`, then so is `X/X₁`.*

<!-- label: III.VII_B.1.4.thm -->

Let us first note that (ii) follows from (i), by 1.3.3 (ii). The proof of (i) occupies paragraphs 1.4.1, 1.4.2 and
1.4.3.

#### 1.4.1.

<!-- label: III.VII_B.1.4.1 -->

Let us first show that one may reduce to the case where `X` has a single point. Since we are dealing with an equivalence
couple, one sees as in Exp. V, § 3.e), that one defines <!-- original page 506 --> an equivalence relation on the
underlying set of `X` by declaring two points `x, y` to be equivalent if there exists a point `z` of `X₁` such that
`d₀(z) = y` and `d₁(z) = x`. One may evidently suppose without loss of generality that `X` contains a single equivalence
class for this relation, in other words that `X/X₁` has a single point (see the construction of `X/X₁` given in 1.2).

In this case, let `x` be an arbitrary point of `X` and `U` the formal variety which has `x` as its only point and the
same local ring as `X` at `x`. One sees then as in Exp. V, § 6, that the equivalence relation induced by `(d₀, d₁)` on
`U` again satisfies the hypotheses of the theorem and that it suffices to give the proof for the latter equivalence
relation (`U` is a "quasi-section").

Let us briefly recall the principle of the proof given in Exp. V, § 6. Set `V = d₀⁻¹(U) = U ×_{i,d₀} X₁`, where `i` is
the inclusion of `U` in `X`; let `u` and `v` be the morphisms with source `V` induced respectively by `d₀` and `d₁`:

```text
                v          u
   X ←─────── V ─────────→ U.
```

It is clear that `u` and `v` are topologically flat and that `u` is surjective; since `X` contains a single equivalence
class, `v` is surjective. If `(v₀, v₁)` is the inverse image of the equivalence couple `(d₀, d₁)` under `v` (cf. V,
3.a)), it follows from V, 3.c) and 3.d) that `X/X₁` and the quotient of `U` by the equivalence relation induced by
`(d₀, d₁)` are both identified with `Coker(v₀, v₁)`. One sees then, as in the proof of V, 6.1, that if the conclusion of
Theorem 1.4 is verified for `U`, it is also verified for `X`.

#### 1.4.2.

<!-- label: III.VII_B.1.4.2 -->

We are thus reduced to the case where `X` has a single point.[^N.D.E-VII_B-67] Consider then the following commutative
diagram (cf. V, § 1, (0,1,2)):

```text
            d'₁           d₀
   X₂ ───────── X₁ ─────────→ X
            d'₀
                            
   d'₂         d₁         
                          
            d₁                
   X₁ ─────────→ X ─────────→ X/X₁
            d₀
```

where `X₂` is the fiber product `X₁ ×_{d₁,d₀} X₁`, and where `d'₀`, `d'₁` and `d'₂` are respectively
    <!-- original page 507 --> the morphisms "`(x, y, z) ↦ (x, y)`", "`(x, y, z) ↦ (x, z)`", and
"`(x, y, z) ↦ (y, z)`".[^N.D.E-VII_B-68]

If `B`, `A`, `A₁` and `A₂` denote respectively the affine algebras of `X/X₁`, `X`, `X₁` and `X₂`, the preceding diagram
induces a commutative diagram:

```text
                 j₁           i₀
       A₂ ←───────── A₁ ←───────── A
                 j₀
                                    
    j₂           i₁           i      
                                     
                 i₁           i        
       A₁ ←───────── A  ←──────── B
                 i₀
```

in which the two rows are exact and the squares determined by `(i₀, j₀)` and `(i₁, j₁)` are cocartesian. Since the
morphism `X₁ → X × X` with components `d₀` and `d₁` is a monomorphism by hypothesis, the morphism `A ⨶_k A → A₁` with
components `i₀` and `i₁` is surjective, by Proposition 1.3.

This means that `i₁` makes `A₁` into a pseudocompact `A`-module (assumed topologically free), generated by `i₀(A)`.
Since `A` is local, Lemma 1.4.3 below yields the existence of a topologically free `k`-module `V` and a morphism of
pseudocompact `k`-modules `f : V → A` such that the morphism

```text
   α₁ : A ⨶_k V ─→ A₁,    a ⨶ v ↦ i₁(a) · i₀(f(v))
```

<!-- original page 508 --> is invertible. Let `α : B ⨶_k V → A` and `α₂ : A₁ ⨶_k V → A₂` be the morphisms:

```text
   b ⨶ v ↦ i(b) · f(v)    and    a₁ ⨶ v ↦ j₂(a₁) · j₀ i₀(f(v)).
```

In the following commutative diagram, the two rows are therefore exact and the two left-hand squares are cocartesian.
Since `α₁` is invertible, the same holds for `α₂`, hence for `α`.

```text
                 j₁                  i₀
        A₂ ←──────────── A₁ ←──────────── A
                 j₀

    α₂              α₁                α

                i₁ ⨶ V             i ⨶ V
       A₁ ⨶_k V ←─── A ⨶_k V ←─── B ⨶_k V.
                i₀ ⨶ V
```

This shows on the one hand that `A` is topologically free over `B`, with pseudobasis `f(V)` (cf. 0.2.1), and that one
obtains a pseudobasis of `A₁` over `A` (where `A₁` is considered as an `A`-module via `i₁`) by taking the image under
`i₀` of `f(V)`; this entails that the morphism `A ⨶_B A → A₁` with components `i₁` and `i₀` is invertible:

```text
   A ⨶_B A ≃ A ⨶_B B ⨶_k V ≃ A ⨶_k V ≃ A₁.
```

This proves Theorem 1.4, modulo Lemma 1.4.3 which follows.

#### 1.4.3. Lemma.

<!-- label: III.VII_B.1.4.3 -->

**Lemma 1.4.3.** *Let `k` be a pseudocompact ring, `A` a local profinite `k`-algebra, `A₁` a topologically free
`A`-module and `i₀ : M → A₁` a morphism of pseudocompact `k`-modules. Suppose that the map*

```text
   A ⨶_k M ─→ A₁,    a ⨶ m ↦ a · i₀(m)
```

*is surjective. Then there exist a topologically free `k`-module `V` and a morphism of pseudocompact `k`-modules
`f : V → M` such that the map*

```text
   A ⨶_k V ─→ A₁,    a ⨶ v ↦ a · i₀(f(v))
```

*is bijective.*

Since every pseudocompact `k`-module is the quotient of a topologically free `k`-module (cf. N.D.E. (27)), one may
suppose without loss of generality that `M` is <!-- original page 509 --> topologically free; so let us take for `M` the
direct product of a family `(M_i)_{i ∈ I}` of copies of `k`. In this case, `A ⨶_k M` is none other than the product
`∏_{i ∈ I} A ⨶_k M_i`. Since the map `a ⨶ m ↦ a · i₀(m)` is surjective and `A₁` is projective, the kernel of this map is
a direct factor of `A ⨶_k M`; since `A` is local, it follows from the exchange theorem (0.3.4) that this kernel has as
supplement a partial product `∏_{i ∈ J} A ⨶_k M_i`, where `J` denotes some subset of `I`. One may therefore take
`V = ∏_{i ∈ J} M_i`.

### 1.5.

<!-- label: III.VII_B.1.5 -->

Let `k` be a pseudocompact ring.

**Definition 1.5.** *We shall say that a family of morphisms `f_i : X_i → X` of `Vaf_/k` is a topologically flat
surjective family if the morphism `∐_i X_i → X` induced by the `f_i` is surjective and topologically flat; this means
that each `f_i` is topologically flat and that every point of `X` belongs to the image of at least one of the `X_i`.*

<!-- label: III.VII_B.1.5.def -->

It follows from 1.3.3 that the topologically flat surjective families define a pretopology on `Vaf_/k` (IV 4.2.5); the
corresponding topology will be called the *flat topology* on `Vaf_/k`.

By IV, 4.3.5, a functor `F : (Vaf_/k)° → (Ens)` is a sheaf for the flat topology if and only if `F` transforms every
direct sum into a direct product and the sequence

```text
              F(f)              F(pr₁)
   F(Y) ─────────→ F(X) ──────────────⇉ F(X ×_Y X)
                                F(pr₂)
```

is exact for every topologically flat surjective morphism `f : X → Y`.

By IV, 4.5, Proposition 1.3.1 implies that the flat topology is <!-- original page 510 --> less fine than the canonical
topology, i.e., for every object `X` of `Vaf_/k`, the functor `h_X : T ↦ Hom_{Vaf_/k}(T, X)` is a sheaf for the flat
topology. (In what follows, one will identify, as usual (cf. Exp. I), `X` with `h_X`.)

By IV, 4.6.5, one may reformulate Theorem 1.4 as follows.

**Theorem 1.5.** *Let `k` be a pseudocompact ring, `d₀, d₁ : X₁ ⇒ X` an equivalence couple in `Vaf_/k`, and `X/X₁` the
formal quotient variety (i.e., `Coker(d₀, d₁)`, cf. 1.2). If `d₁` is topologically flat, then `X/X₁` represents the
quotient sheaf for the flat topology.*

<!-- label: III.VII_B.1.5.thm -->

### 1.6.

<!-- label: III.VII_B.1.6 -->

To complete these generalities on formal varieties, it remains to define briefly the étale formal varieties over
`k`.[^N.D.E-VII_B-70]

**Recollections 1.6.A.** *(i)* Let us first recall (cf. EGA 0\_{IV}, 19.10.2) that a topological `k`-algebra `A` is said
to be *formally étale* over `k` (for the topologies given on `k` and `A`, resp. for the discrete topologies) if, for
every discrete topological `k`-algebra `C` (not necessarily artinian), and every nilpotent ideal `J` of `C`, every
continuous morphism of `k`-algebras `A → C/J` lifts in a unique way to a continuous morphism `A → C` (`A` being endowed
with the given topology, resp. with the discrete topology). One sees at once that this property is preserved by base
change, i.e., for every morphism `k → k'` of pseudocompact rings, `A ⨶_k k'` is then formally étale over `k'`. On the
other hand, one sees easily that it suffices to verify the lifting condition for every ideal `J` of square zero, cf. EGA
IV_4, 17.1.2 (ii). One says that `A` is *étale* over `k` if it is formally étale over `k` for the discrete topologies,
and if moreover `A` is a `k`-algebra of finite presentation (cf. EGA IV_4, 17.3.2 (ii)). In what follows, `k` being a
pseudocompact ring and `A` a profinite `k`-algebra, one will use "formally étale" in the sense of the given topologies
(unless otherwise stated).

<!-- label: III.VII_B.1.6.A -->

*(ii)* Recall also that if `F ∈ k[T]` is a monic polynomial of degree `d ⩾ 1`, separable (i.e., such that the ideal
generated by `F` and its derivative polynomial `F'` is `k[T]`), then the `k`-algebra `B = k[T]/(F)` (which is free of
rank `d` over `k`, and endowed with the product topology) is formally étale over `k`. Indeed, let `C` be a discrete
`k`-algebra (so that the kernel of `k → C` is an open ideal `l` of `k`), `J` an ideal of `C` of square zero, and
`φ : B → C/J` a continuous morphism of `k`-algebras. Note that, `B` being a `k`-module free of finite rank, `lB` is an
open ideal of `B`, hence every lifting `Φ : B → C` of `φ` is automatically continuous. Let `t` be the image of `T` in
`B` and `u₀` an arbitrary lifting of `φ(t)` in `C`; then `F(u₀) ∈ J` (since `φ(t)` is a root of `F`); on the other hand
there exist `G, H ∈ k[T]` such that `GF + HF' = 1`, hence `H(u₀)F'(u₀) = 1 − G(u₀)F(u₀)`, and the right-hand term is
invertible, since `F(u₀)` is of square zero, hence `F'(u₀)` is invertible. Let us seek `h ∈ J` such that `x = u₀ + h` be
a root of `F`; this amounts to `0 = F(u) = F(u₀) + F'(u₀)h`, and as `F'(u₀)` is invertible, this has the unique solution
`h = −F'(u₀)⁻¹ F(u₀) ∈ J`. Of course, the same proof (without making continuity hypotheses on the morphisms `k → C`, `φ`
and `Φ`) shows that `B` is also an étale `k`-algebra.

*(iii)* Recall finally that if `A` is a finite product `A₁ × ⋯ × A_n`, then `A` is formally étale over `k` if and only
if the `A_i` are.[^N.D.E-VII_B-71] Indeed, it suffices to see this for `n = 2`, in which case let `e = 1_{A₁}` be the
idempotent such that `A₁ = Ae` and `A₂ = A(1 − e)`, and suppose given a continuous morphism `A → C/J`, where `J` is an
ideal of square zero. Since the polynomial `F = X² − X` is separable (one has `F' = 2X − 1` and `(F')² − 4F = 1`), the
idempotent `φ(e)` of `C/J` lifts in a unique way to an idempotent `f` of `C`, whence `C = Cf ⊕ C(1 − f)`, and then to
give a lifting of `Φ` amounts to giving two morphisms `Φ₁ : A₁ → Cf` and `Φ₂ : A₂ → C(1 − f)`, lifting the restrictions
of `φ` to `A₁` and `A₂`. The same argument shows that if `e` is an idempotent of `k` such that `A = Ae`, then `A` is
formally étale over `k` if and only if it is so over the localization `k_e` (which is identified with `ke`).

Let now `X` be a `k`-formal variety and `A` its affine algebra. If `x` is a point of `X` (i.e., a maximal open ideal `m`
of `A`), with image `s` in `Spf(k)`, one will denote by `k_m` or `k_s` the local component of `k` corresponding to `s`.

**Definition 1.6.B.** *The following conditions are equivalent:*

*(a) `A` is formally étale over `k`.*

*(b) For every `m ∈ Υ(A)`, `A_m` is formally étale over `k` (or over `k_m`).*

*(c) For every open ideal `l` of `k`, `A ⨶_k (k/l) = A/Al` is formally étale over `k/l`.*

*(d) For every `m ∈ Υ(A)` and every open ideal `l` of `k_m`, `A_m/A_m l` is formally étale over `k_m/l`.*

<!-- label: III.VII_B.1.6.B -->

We shall say that `X` is *étale over `k`* if it satisfies these conditions, and one denotes by `Vaf^ét_/k` the full
subcategory of `Vaf_/k` formed by the formal varieties étale over `k`.[^N.D.E-VII_B-72]

Note that if `φ : A → C/J` is a continuous morphism of `k`-algebras, where `C` is a discrete `k`-algebra and `J` an
ideal of square zero, then `I = Ker(φ)` is an open ideal of `A`, hence `A/I` is artinian, hence `I` is contained in only
a finite number of maximal open ideals `m₁, …, m_r`, hence contains the product of the components `A_m` for `m ≠ m_i`,
which equals `A(1 − e)` where `e` denotes the idempotent of `A` such that `Ae = ∏_{i=1}^r A_{m_i}`. Thus
`φ(e) = 1_{C/J}` and it amounts to the same to give a continuous lifting of `φ` or of the morphism from
`Ae ≃ A/A(1 − e)` to `C/J`, induced by `φ`.

On the other hand, one knows (cf. N.D.E. (24)) that `A ≃ lim_l A/Al`. Taking these remarks and the preceding
recollections into account, one easily obtains the equivalence of the indicated conditions.

**Definitions 1.6.C.** *Set `κ(k) = ∏_{s ∈ Spf(k)} κ(s)`, endowed with the product topology, i.e., the formal variety
`Spf(κ(k))` is the direct sum of the `Spec κ(s)`, for `s ∈ Spf(k)`. On the other hand, one denotes by `S_{κ(k)}` the
scheme direct sum of the `Spec κ(s)`, for `s ∈ Spf(k)`.*

<!-- label: III.VII_B.1.6.C -->

*For every formal variety `X` over `k`, one denotes by `X_κ = X ⨶_k κ(k)` the formal variety over `κ(k)` obtained by
base change, i.e., `X_κ` has the same points as `X` and for every `x ∈ X`, of projection `s` on `Spf(k)`, one has
`O_{X_κ, x} = O_{X, x} ⨶_k κ(s)`. This base change functor `Vaf_/k → Vaf_/κ(k)` sends `Vaf^ét_/k` into `Vaf^ét_/κ(k)`
(cf. 1.6.A (i)).*

One then has (cf. SGA 1, I 6.2):

**Lemma 1.6.D.** *For every `Y ∈ Ob Vaf^ét_/k` and `X ∈ Ob Vaf_/k`, the canonical map*

```text
   Hom_{Vaf_/k}(X, Y) ─→ Hom_{Vaf_/κ(k)}(X_κ, Y_κ)
```

*is bijective. In particular, the functor `Vaf^ét_/k → Vaf^ét_/κ(k)` is fully faithful (and one will see below that it
is an equivalence).*

<!-- label: III.VII_B.1.6.D -->

Indeed, let `A` (resp. `B`) be the affine algebra of `X` (resp. `Y`) and `r` the radical of `k`, and suppose given a
morphism `B ⨶_k κ(k) → A ⨶_k κ(k)` or, what amounts to the same, a morphism `φ : B → A/rA`.

For every open ideal `l` of `k`, there exists `n ∈ ℕ*` such that `r^n ⊂ l`, whence `(rA)^n ⊂ lA ⊂ lA`, and since the
multiplication map `m^{n-1} : A^n → A` is continuous, one also has `(rA)^n ⊂ lA`, i.e., `rA/lA` is a nilpotent ideal of
`A/lA`. Consequently, `φ` lifts in a unique way to a morphism `φ_l : B → A/lA`. By uniqueness, these morphisms form a
projective system, hence give a continuous morphism `Φ : B → lim_l A/lA = A`. Moreover, `Φ` is unique since if `Φ'` is a
second lifting of `φ`, then `Φ'` and `Φ` coincide modulo `lA` for every `l`, hence are equal.

**Proposition 1.6.E.** *(a) Let `X` be a formal variety over `k` and `A` its affine algebra. The following conditions
are equivalent:*

*(i) `X` is étale over `k`.*

*(ii) `X` is topologically flat over `k` and the diagonal morphism `∆ : X → X × X` is a local isomorphism, i.e., `∆_X`
induces an isomorphism `O_{X×X, ∆(x)} ⥲ O_{X, x}` for every point `x` of `X`.*

*(iii) For every `x ∈ X`, of projection `s` on `Spf(k)`, `O_{X, x}` is isomorphic to `k_s[T]/(F)`, where `F ∈ k_s[T]` is
a monic separable polynomial (cf. 1.6.A (ii)).*

*(iv) `X` is topologically flat over `k`, and, for every point `x ∈ X`, of projection `s` on `Spf(k)`,
`O_{X, x} ⨶_k κ(s)` is a finite separable extension of `κ(s)`.*

*(v) For every open ideal `l` of `k`, each local component of `A ⨶_k (k/l)` is a finite étale algebra over the artinian
ring `k/l`.*

*(b) `Vaf^ét_/κ(k)` is identified with the category of étale schemes over `S_{κ(k)}` (cf. 1.6.C), and the functor
`X ↦ X_κ` induces an equivalence of categories `Vaf^ét_/k ⥲ Vaf^ét_/κ(k)` (cf. SGA 1, I 6.1).*

<!-- label: III.VII_B.1.6.E -->

*Proof.* (a) Let `I` denote the kernel of the multiplication morphism `m : A ⨶_k A → A`. Suppose `X` étale over `k`,
i.e., `A` formally étale over `k`. Then, by EGA 0\_{IV}, 20.7.4, the Hausdorff completion of `I/I²`, for the quotient
topology of that of `I`, is zero, i.e., one has `I = I²`. Now, for every `x ∈ X`, `I` is contained in the maximal ideal
`m_{∆(x)}` of `A ⨶_k A`, hence the localization `I_{m_{∆(x)}}` is contained in the maximal ideal of `O_{X×X, ∆(x)}`, and
so, by Nakayama's lemma 0.3, one has `I_{m_{∆(x)}} = 0`, and hence `∆ : X → X × X` is a local isomorphism.

Suppose now that `∆` is a local isomorphism and that `k` is a field `κ`, and let us show that each `O_{X, x}` is a
finite-dimensional étale `κ`-algebra. Replacing `X` by `Spf(O_{X, x})`, one may suppose that `A = O_{X, x}` is local.
One proceeds then as in the proof of EGA IV_4, 17.4.1, (b) ⇒ (d''). Let `K` be a finite normal extension of `κ`
containing the residue field `κ(x)`, and let `B = A ⨶_κ K = A ⨶_κ K` (since `[K : κ] < ∞`, then `−⨶_κ K` and `− ⨶_κ K`
coincide) and `X_K = Spf(B) = X ⨶_κ K`. Then `∆_K : X_K → X_K ⨶_K X_K` is again a local isomorphism, so for every
`y ∈ X_K`, the multiplication `B_y ⨶_K B_y → B_y` induces an isomorphism `(B_y ⨶_K B_y)_{m_{∆_K(y)}} ⥲ B_y`. Now, since
the residue field of `B_y` is `K` (cf. for example VI_A, 1.1.1, N.D.E. (11)), `C = B_y ⨶_K B_y` is already a local ring
(indeed, `n = m_y ⨶_K B_y + B_y ⨶_K m_y` consists of topologically nilpotent elements, hence is contained in the radical
of `C`, and `C/n = K ⨶_K K = K` is a field), hence one obtains that the multiplication morphism `B_y ⨶_K B_y → B_y` is
an isomorphism. Taking a pseudobasis of `B_y` over `K` containing the unit element `1`, one deduces that `B_y = K`.
Since moreover `B` is finite over `A`, `X_K` is a finite set, hence `B = A ⨶_κ K` is the product of a finite number of
copies of `K`, and this entails that `A` is a finite étale `κ`-algebra.

One thus obtains that, if `κ` is a field, every profinite `κ`-algebra `A` étale over `κ` is the product of finite
separable extensions `K_i` of `κ`, endowed with the product topology, hence the formal variety `Spf(A)` is the direct
sum of the `Spf(K_i) = Spec(K_i)`, and one deduces that `Vaf^ét_/κ` is identified with the category of étale
`κ`-schemes.

What precedes shows the implication (ii) ⇒ (iv) (since `O_{X, x} ⨶_k κ(s)` is formally étale over `κ(s)`), and entails
point (b) of 1.6.E. Indeed, let `k` be again an arbitrary pseudocompact ring. By what precedes, `Vaf^ét_/κ(k)` is
identified with the category of étale schemes over `S_{κ(k)}`. Let us show that `X ↦ X_κ` induces an equivalence
`Vaf^ét_/k ⥲ Vaf^ét_/κ(k)`. Taking 1.6.D into account, it suffices to show that for every `s ∈ Spf(k)` and every finite
separable extension `K` of `κ(s)`, there exists an étale `k_s`-algebra `A` such that `A ⨶_k κ(s) ≃ K`. Let `ξ` be a
primitive element of the extension `K/κ(s)`, `n` its degree, and `F ∈ k_s[T]` a monic polynomial of degree `n` whose
image `F̄` in `κ(s)[T]` is the minimal polynomial of `ξ`. Since `F̄'` is invertible in `κ(s)[T]/(F̄)`, it follows from
Nakayama's lemma that `F'` is invertible in `k_s[T]/(F)`, hence `F` is a separable polynomial and hence, by 1.6.A (ii),
`A = k_s[T]/(F)` is an étale `k_s`-algebra such that `A ⨶_k κ(s) ≃ K`. One thus obtains that every local profinite étale
`k_s`-algebra is free of finite rank over `k_s` (hence a fortiori topologically free over `k`), and hence every
profinite étale `k`-algebra is topologically free over `k`.

On the other hand, condition (v) implies condition (d) of 1.6.B, hence implies (i). One has thus obtained that (i),
(iii) and (v) are equivalent, and imply (ii), which implies (iv). Finally, let `A` be a profinite `k`-algebra satisfying
(iv); let us show that `A` is formally étale over `k`. For this, one may suppose `A` and `k` local; denote by `κ` the
residue field of `k`. By hypothesis, `K = A ⨶_k κ` is a finite separable extension of `κ`, say of degree `n`. By what we
have seen above (and taking Lemma 1.6.D into account), there exists then a `k`-algebra `B` free of rank `n`, formally
étale over `k`, and a continuous morphism `φ : B → A` such that `φ ⨶_k κ` is an isomorphism. Since `A` is topologically
flat over `k`, this entails that `Coker(φ) ⨶_k κ = 0` and also `Ker(φ) ⨶_k κ = 0`; by Nakayama's lemma 0.3, one
therefore has `Coker(φ) = 0 = Ker(φ)`, hence `φ` is an isomorphism (cf. the proof of 0.2.B). This completes the proof of
1.6.E.

Let `X` be a formal variety over `k`. For every `x ∈ X`, of projection `s` on `Spf(k)`, the residue field `κ(x)` is a
finite extension of `κ(s)` and one denotes by `κ_e(x)` the separable closure of `κ(s)` in `κ(x)`.

**Proposition 1.6.F.** *(i) The inclusion of `Vaf^ét_/k` in `Vaf_/k` has a left adjoint `X ↦ X_e`: the variety `X_e` has
the same points as `X`, and for every `x ∈ X`, of projection `s` on `Spf(k)`, let `ξ` be a primitive element of
`κ_e(x)`, `n` its degree, `u` an arbitrary lifting <!-- original page 511 --> of `ξ` in `O_{X, x}`, and `F ∈ k[T]` monic
of degree `n` annihilating `u`; one sets `O_{X_e, x} = k[T]/(F)`. Then for every `Y ∈ Ob Vaf^ét_/k`, the canonical maps
below are bijective:*

```text
   Hom_{Vaf_/k}(X, Y) ────⥲────→ Hom_{Vaf_/κ(k)}(X_κ, Y_κ)
                                          ↑
                                          ≀
   Hom_{Vaf_/k}(X_e, Y) ────⥲───→ Hom_{Vaf_/κ(k)}((X_e)_κ, Y_κ),
```

*the vertical arrow being induced by the inclusions `κ_e(x) ↪ κ(x)` for every `x ∈ X`. This defines, in particular, a
morphism `p : X → X_e`, and every morphism of `k`-formal varieties `φ : X → Y`, with `Y` étale over `k`, factors
uniquely through `p`.*

*(ii) The functor `X ↦ X_e` commutes with finite products.*

<!-- label: III.VII_B.1.6.F -->

Indeed, (i) follows from 1.6.E (b) and 1.6.D. Let us prove (ii). Taking the equivalence of categories 1.6.E (b) into
account, one may suppose that `k` is a field. In this case, one sees easily that if `X` is a semi-local `k`-formal
variety, i.e., one whose affine algebra `A` is semi-local, then the affine algebra of `X_e` is the largest subalgebra of
`A` which is étale over `k`; let us denote it by `A_e`. One thus reduces to seeing that if `K, L` are two finite-degree
extensions of `k`, then the inclusion `K_e ⨶ L_e ⊂ (K ⨶ L)_e` is an equality. Let `p` be the characteristic exponent of
`k` (i.e., `p = 1` if `char(k) = 0` and `p = char(k)` otherwise), then for every `x ∈ K ⨶ L`, there exists `n ∈ ℕ*` such
that `x^{p^n} ∈ K_e ⨶ L_e`, hence every subalgebra `B` of `K ⨶ L` is radicial over `K_e ⨶ L_e`, and it follows that
`K_e ⨶ L_e = (K ⨶ L)_e`.

Note, keeping the preceding notations, that `O_{X_e, x}` is not necessarily a subalgebra of `O_{X, x}`, but this is the
case when `X` is topologically flat over `k`, by the following proposition.

#### 1.6.1.

<!-- label: III.VII_B.1.6.1 -->

Let `Y` be an étale `k`-formal variety and `f : X → Y` a morphism of `Vaf_/k`. Then one has the cartesian square below,
where `Γ_f` is the graph morphism `X → X × Y`, with components `id_X` and `f`,

```text
            Γ_f
       X ───────→ X × Y
                       
       f          f ⊠ id_Y
                       
            ∆_Y       
       Y ───────→ Y × Y.
```

It follows that `Γ_f` is a local isomorphism, hence that `f = pr_Y ∘ Γ_f` is topologically flat if `pr_Y` is, for
example if `X` is topologically flat over `k`.

Conversely, since `Y → k` is topologically flat, `X → k` will be as well if `f` is so (cf. 1.3.3). Taking in particular
`f` to be the canonical morphism `p : X → X_e` of 1.6, one obtains:

**Proposition 1.6.1.** *Let `X` be a formal variety over `k`. The morphism `X → X_e` is topologically flat if and only
if `X` is topologically flat over `k`.*

<!-- label: III.VII_B.1.6.1.prop -->

**Remark 1.6.2.**[^N.D.E-VII_B-74] When `k` is a perfect field, the functor `X ↦ X_e` is also right adjoint to the
inclusion `Vaf^ét_/k ↪ Vaf_/k`. Indeed, in this case one has `O_{X_e, x} = κ(x)` for every `x ∈ X`, and the canonical
projections `O_{X, x} → κ(x)` define a morphism `s : X_e → X`, which is a section of `p : X → X_e`. For every morphism
`f : X → Y` the diagrams below are commutative:

```text
                              f
   O_{Y, f(x)} ─→ O_{X, x}       X ──────→ Y
                                 ↑          ↑
                                 s_X        s_Y
                                       f_e
   κ(f(x)) ────→ κ(x)            X_e ────→ Y_e
```

hence `s` is functorial in `X`, and it follows that `X ↦ X_e` is right adjoint to the inclusion `Vaf^ét_/k ↪ Vaf_/k`.
Hence, being a right adjoint, `X ↦ X_e` commutes with inverse limits when they exist in `Vaf^ét_/k`,[^N.D.E-VII_B-75]
hence in particular with finite products. (This can also be verified directly: for every `k`-formal variety `X`, of
affine algebra `A`, `X_e` has as affine algebra the quotient of `A` by its radical `r(A)`, and since `k` is perfect, the
quotient of `O_{X, x} ⨶ O_{Y, y}` by its radical is the algebra `κ(x) ⨶_k κ(y)`, since the latter is semi-simple.)

<!-- label: III.VII_B.1.6.2 -->

## 2. Generalities on formal groups

<!-- label: III.VII_B.2 -->

<!-- original page 512 -->

### 2.1.

<!-- label: III.VII_B.2.1 -->

Let `k` be a pseudocompact ring and `G` a `k`-formal group, that is, a group of the category `Vaf_/k` of formal
varieties over `k`. Let `A` be the affine algebra of `G`. The composition law of `G` evidently defines a diagonal
morphism, that is, a homomorphism of profinite `k`-algebras `∆_A : A → A ⨶_k A`; this homomorphism satisfies the
following conditions:

(i) the diagram

```text
                       ∆_A
            A ───────────────→ A ⨶_k A

         ∆_A                   ∆_A ⨶ id_A
                                
                   id_A ⨶ ∆_A
            A ⨶_k A ────────→ A ⨶_k A ⨶_k A
```

is commutative.

(ii) there exists an augmentation (necessarily unique), that is, a homomorphism of profinite `k`-algebras `ε_A : A → k`
such that the composite maps

```text
              ∆_A          ε_A ⨶ id_A
         A ───────→ A ⨶_k A ───────────→ k ⨶_k A ≃ A

   and    A ───────→ A ⨶_k A ───────────→ A ⨶_k k ≃ A
              ∆_A          id_A ⨶ ε_A
```

are the identity maps of `A`.

(iii) there exists an antipodism (necessarily unique), that is, a homomorphism of profinite `k`-algebras `c_A : A → A`
such that the composite map

```text
         ∆_A         c_A ⨶ id_A        m_A
   A ───────→ A ⨶_k A ─────────────→ A ⨶_k A ──────→ A
```

is equal to `η_A ∘ ε_A`, where `m_A` denotes the linear map sending `a ⨶ b` to `ab` and `η_A` the map `λ ↦ λ · 1_A` from
`k` into `A`.

<!-- original page 513 -->

Conversely, the data of `(∆_A, ε_A, c_A)` satisfying (i)–(iii) endows `G` with a structure of `k`-formal
group.[^N.D.E-VII_B-76] Explicitly, for every profinite `k`-algebra `B`, the set `Hom_c(A, B)` of continuous morphisms
of `k`-modules `φ : A → B` is endowed with a group structure, functorial in `B`, defined by

```text
   φ · φ' = m_B ∘ (φ ⨶ φ') ∘ ∆_A,
```

the neutral element being `η_B ∘ ε_A` (where `m_B` is the multiplication of `B` and `η_B` the map `λ ↦ λ · 1_B` from `k`
into `B`), and `φ ∘ c_A` being the inverse of `φ`; and the set `Hom_{Alp/k}(A, B)` of continuous morphisms of
`k`-algebras `A → B` is a subgroup of it (since the algebra `B` is commutative).

**Definition 2.1.** *A morphism of `k`-formal groups `θ : K → G` is, by definition, a morphism of `k`-formal varieties
which respects the group structures.* If `B` (resp. `A`) is the affine algebra of `K` (resp. `G`) and if `f : A → B` is
the morphism corresponding to `θ`, this amounts to saying that `f` is compatible with the comultiplications, i.e.,

```text
   (f ⨶ f) ∘ ∆_A = ∆_B ∘ f
```

(the conditions `ε_B ∘ f = ε_A` and `c_B ∘ f = f ∘ c_A` being then automatically satisfied). One will denote by `Grf_/k`
the category of `k`-formal groups.

<!-- label: III.VII_B.2.1.def -->

**Notations.** *In what follows, we shall call augmentation ideal of `A` the ideal `I_A = Ker(ε_A)`, and we shall denote
by `ω_{G/k}` the pseudocompact `k`-module `I_A/I_A²`, that is, the quotient of `I_A` by the closed ideal generated by
the products `xy`, for `x, y ∈ I_A`.*

### 2.2.

<!-- label: III.VII_B.2.2 -->

Let `H` be a group of the category of coalgebras over `O_k`, i.e., for every object `C` of `Alf_/k`, `H(C)` is endowed
with a structure of `C`-coalgebra in groups (cf. VII_A 3.2; following Manin, we shall say *bialgebra*[^N.D.E-VII_B-77]
instead of *coalgebra in groups*); moreover, if `φ : C → D` is a morphism of `Alf_/k`, the map `D ⨶_C H(C) → H(D)` is a
homomorphism of `D`-bialgebras.

**Definition 2.2.** *We shall summarize the above properties by saying that `H` is a* bialgebra over `O_k`.

<!-- label: III.VII_B.2.2.def -->

It is clear that the functor `H ↦ Spf*(H)` of 1.3.5 commutes with finite products. It therefore transforms a bialgebra
over `O_k` into a `k`-group functor, that is, a (covariant) functor from `Alf_/k` to the category of groups.

And indeed, for every `k`-algebra `C` of finite length, the elements of

```text
   Spf*(H)(C) = Spf*(H(C)) = {x ∈ H(C) | ε(x) = 1 and ∆(x) = x ⊗ x}
```

form a group for the multiplication of the algebra `H(C)` (cf. VII_A 3.2.2). Note moreover that the condition
`∆(x) = x ⊗ x` entails the equality `ε(x) = ε(x)²`, hence also `ε(x) = 1` if `C` is local and `x ≠ 0`.[^N.D.E-VII_B-78]

#### 2.2.1.

<!-- label: III.VII_B.2.2.1 -->

A bialgebra `H` over `O_k` is said to be *flat* if the underlying module is flat (cf. 1.2.1).[^N.D.E-VII_B-79]
    <!-- original page 514 --> If `H` is flat then, by 1.3.5, `A = Γ*(H)` is a topologically flat profinite `k`-algebra, and
`Spf*(H)` is isomorphic, as a functor from `(Alf_/k)° = Vaf_/k` to `(Ens)`, to the functor

```text
   Spf(A) : C ↦ Hom_{Vaf_/k}(Spf(C), Spf(A)).
```

The group structure of `Spf*(H)` thus endows `𝒢(H) = Spf(A)` with a structure of formal group, which is described
explicitly as follows.

For every object `C` of `Alf_/k`, since the `C`-module underlying `H(C)` is projective, one deduces from Lemma 1.2.3.A,
by induction on `n`, natural isomorphisms:

```text
   H(C)*^⨶(n+1) ≃ Hom_C(H(C), (H(C)*)^⨶ n)
               ≃ Hom_C(H(C), (H(C)^⨶ n)*) ≃ (H(C)^⨶(n+1))*.
```

One deduces from this (for `n = 1, 2`) that the `C`-algebra structure of `H(C)` endows `H(C)*` with a diagonal map
satisfying conditions 2.1 (i)–(iii), all of this functorially in `C`.

Consequently, `A = Γ*(H) = lim H(k/l)*` is endowed with a structure of cogroup in `Alp/k`, which defines on `𝒢(H)` the
announced formal group structure.

Conversely, let `G` be a topologically flat `k`-formal group, of affine algebra `A`, and denote by `H(G)` the
`O_k`-coalgebra `V_kf(A)` (cf. 1.2.3). The diagonal morphism `∆_A : A → A ⨶_k A` then induces, for every `k`-algebra `C`
of finite length, a `C`-linear map

```text
   V_kf(A)(C) ⊗_C V_kf(A)(C) ─→ V_kf(A)(C)
```

which makes the coalgebra `V_kf(A)(C)` into a `C`-bialgebra. One says that `H(G)` is the *covariant bialgebra* of the
formal group `G`.[^N.D.E-VII_B-80] Therefore, by Proposition 1.3.5.D:

**Proposition 2.2.1.** *(i) The functors `G ↦ H(G)` and `H ↦ 𝒢(H)` define an equivalence between the category of
topologically flat `k`-formal groups and that of flat `O_k`-bialgebras.*[^N.D.E-VII_B-81]

*(ii) This equivalence "commutes with base change": if `k → K` is a morphism of pseudocompact rings, then
`H(G ⨶_k K) = H(G) ⨶_k K` and `𝒢(H ⨶_k K) = 𝒢(H) ⨶_k K`.*

<!-- label: III.VII_B.2.2.1.prop -->

When `k` is an artinian ring and `G` a topologically flat `k`-formal group, the functor `H(G)` is evidently determined
by its value `H(G) = H(G)(k)` at `k`. One will also say that `H(G)` is the (covariant) *bialgebra* of
`G`.[^N.D.E-VII_B-82] Consequently, denoting by `H_k` the category of `k`-Hopf algebras and `H^cocom_{flat/k}` the full
subcategory formed by `k`-Hopf algebras flat over `k` and cocommutative, one obtains:

**Corollary 2.2.1.** *Let `k` be an artinian ring.*

*(i) The functors `G ↦ H(G)` and `H ↦ 𝒢(H) = Spf* H(G)` define an equivalence between the category of topologically flat
`k`-formal groups and `H^cocom_{flat/k}`.*

*(ii) This equivalence "commutes with base change": if `k → K` is a morphism of artinian rings, then
`H(G ⨶_k K) = H(G) ⨶_k K` and `𝒢(H ⨶_k K) = 𝒢(H) ⨶_k K`.*

<!-- label: III.VII_B.2.2.1.cor -->

On the other hand, let us denote `H^com_{flat/k}` the full subcategory of `H_k` formed by the `k`-Hopf algebras flat
over `k` and commutative, and recall that the functor `K ↦ O(K)` is an anti-equivalence of the category of affine
`k`-group schemes onto `H^com_{flat/k}`.

#### 2.2.2.

<!-- label: III.VII_B.2.2.2 -->

<!-- original page 515 -->

Let us suppose for simplicity that `k` is artinian and let `G` be a topologically flat `k`-formal
group.[^N.D.E-VII_B-83] Then `G` is commutative if and only if its affine algebra `𝒜(G)` has a cocommutative
comultiplication, which is equivalent to saying that the bialgebra `H(G)` has a commutative multiplication. In this
case, `H(G)` is a commutative and cocommutative Hopf algebra, flat over `k`; if one sets `D'(G) = Spec H(G)`, then
`D'(G)` is a commutative `k`-group scheme, affine and flat over `k`. Conversely, if `T` is such a `k`-group scheme, its
affine algebra `O(T)` is a commutative group in the category of cocommutative `k`-coalgebras flat over `k` and hence, by
1.3.5.C, one obtains a topologically flat `k`-formal group `D(T)` by setting:

```text
   D(T) = Spf* O(T) = Spf(𝒜),    where 𝒜 = O(T)*.
```

As, by 1.3.5.D, one has canonical isomorphisms `G = Spf* H(G)` and `H(D(T)) = O(T)`, one obtains canonical isomorphisms:

```text
   D(D'(G)) = Spf* O(D'(G)) = Spf* H(G) = G,
   D'(D(T)) = Spec H(D(T)) = Spec O(T) = T.
```

Moreover, denoting by `k`-Gr. the category of `k`-group schemes, one has, by Corollary 2.2.1, functorial isomorphisms:

```text
   Hom_{Grf/k}(G, D(T)) ≃ Hom_{H_k}(H(G), O(T)) ≃ Hom_{k-Gr.}(T, D'(G)),
```

One thus obtains:

**Proposition (Cartier duality) 2.2.2.** *Let `k` be an artinian ring.*

*(i) The functors `G ↦ D'(G) = Spec H(G)` and `T ↦ D(T) = Spf* O(T)` induce an anti-equivalence between the category
`ℱ𝒞_k` of commutative topologically flat `k`-formal groups and the category `𝒜𝒞_k` of commutative `k`-group schemes,
affine and flat, i.e., `G` and `D'(G)` (resp. `T` and `D(T)`) are related by the equalities:[^N.D.E-VII_B-84]*

```text
   H(G) = O(D'(G))    and    O(T) = H(D(T)).
```

*(ii) This anti-equivalence "commutes with base change": if `k → K` is a morphism of artinian rings, then
`D'(G ⨶_k K) = D'(G) ⨶_k K` and `D(T ⨶_k K) = D(T) ⨶_k K`.*

*(iii) In particular, if `k` is a field, one obtains an anti-equivalence between the category of commutative `k`-formal
groups and that of commutative affine `k`-group schemes, which commutes with extension of the base field.*

<!-- label: III.VII_B.2.2.2.prop -->

### 2.3.

<!-- label: III.VII_B.2.3 -->

Let us now consider an arbitrary `k`-formal group[^N.D.E-VII_B-85] `G`, of affine algebra `A`. Let us still denote by
`H(G)` the `O_k`-module `V_kf(A)` dual to `A` and let `ϕ_G` denote the functorial homomorphism

```text
   ϕ_G : H(G) ⨶_k H(G) ─→ H(G × G)
```

induced by the natural map (0.3.6), for every object `C` of `Alf_/k`:

```text
   (A ⨶_k C)† ⊗_C (A ⨶_k C)† ─→ ((A ⨶_k C) ⨶_C (A ⨶_k C))†.
```

If `m : G × G → G` is the multiplication of `G`, the composite map

```text
                  ϕ_G              H(m)
   H(G) ⨶_k H(G) ────→ H(G × G) ────────→ H(G)
```

makes `H(G)` into an algebra over `O_k`; for every `C ∈ Alf_/k`, the unit element of `H(G)(C) = (A ⨶_k C)†` is the
augmentation of `A ⨶_k C` (cf. 2.1).[^N.D.E-VII_B-86] If `G` is not topologically flat over `k`, `ϕ_G` is not
necessarily an isomorphism, and hence the morphism `δ_G : H(G) → H(G × G)` induced by the diagonal morphism
"`x ↦ (x, x)`" from `G` into `G × G` does not necessarily factor through `H(G) ⨶_k H(G)`, i.e., `H(G)` is not
necessarily an `O_k`-bialgebra.

For this reason we shall simply say, in the general case, that `H(G)` is the <!-- original page 516 --> "*covariant
algebra*" of the formal group `G`.

Of course, when `G` is topologically flat over `k`, `ϕ_G` is an isomorphism, and one recovers the structure of
`O_k`-bialgebra on `H(G)` defined in 2.2.1.

#### 2.3.1. Proposition.

<!-- label: III.VII_B.2.3.1 -->

**Proposition 2.3.1.** *Let `K` and `G` be two `k`-formal groups, of affine algebras `B` and `A`. Assume `K`
topologically flat over `k`. Then there exists a canonical bijection from `Hom_{Grf/k}(K, G)` onto the set of
homomorphisms of unital `O_k`-algebras `h : H(K) → H(G)` such that the diagram*

```text
                          h ⨶ h
        H(K) ⨶_k H(K) ──────────→ H(G) ⨶_k H(G)
              ↑                              \
                                              \ ϕ_G
                                               \
   (∗)   ∆_{H(K)}                                H(G × G)
                                               /
                                              /
                                             / δ_G
              h
        H(K) ────────────────────→ H(G)
```

*is commutative.*

Since `K` is topologically flat, `H(K)` is endowed with a structure of bialgebra (cf. 2.2) and `∆_{H(K)}` is its
diagonal morphism; in other words, with the notations of 2.3, one has `∆_{H(K)} = ϕ_K⁻¹ ∘ δ_K`. When `G` is also
topologically flat over `k`, our proposition follows from the equivalence of categories established in 2.2.1.

<!-- original page 517 -->

In the general case, one may suppose `k` artinian and argue on the algebras `H(K) = B†` and `H(G) = A†`. Let
`Hom_c(A, B)` be the set of continuous `k`-linear maps from `A` into `B` and `Hom_k(B†, A†)` the set of `k`-linear maps
from `B†` into `A†`.

By 0.3.6.A, one knows that if `M, P` are pseudocompact `k`-modules and `P` is projective, the canonical map

```text
   Hom_c(M, P) ─→ Hom_k(P†, M†),    f ↦ ᵗf
```

(where `ᵗf` denotes the transpose of `f`) is bijective. (One will apply this to `M = A ⨶ A` and `P = B`, or `M = A` and
`P = B ⨶ B`.)

Let `f ∈ Hom_c(A, B)`. Consider the diagrams below, where the squares (0) are commutative, and where the two unnamed
vertical arrows are `ᵗ(f ⨶ f)`.

```text
                m_A          ∆_A
   A ⨶ A ────────→ A ────────→ A ⨶ A

  f ⨶ f    (1)    f    (2)    f ⨶ f

                m_B          ∆_B
   B ⨶ B ────────→ B ────────→ B ⨶ B
```

```text
                       ᵗm_A=δ_G                ᵗ∆_A=ϕ_G
   A† ⊗ A† ─→ (A ⨶ A)† ←────── A† ────── (A ⨶ A)† ←── A† ⊗ A†
       ↑                ↑                 ↑                 ↑
                                                            
   ᵗf⊗ᵗf  (0)             (1')    ᵗf    (2')               ᵗf⊗ᵗf
                                                            
   B† ⊗ B† ─→ (B ⨶ B)† ←────── B† ────── (B ⨶ B)† ←── B† ⊗ B†
                       ᵗm_B=δ_K                ᵗ∆_B=ϕ_K
```

If `f : A → B` corresponds to a morphism of formal groups `K → G`, then squares (1) and (2) are commutative, and
`ε_B ∘ f = ε_A`; consequently, squares (1') and (2') are commutative and `ᵗf` sends the unit of `B† = H(K)` to that of
`A† = H(G)`, i.e., `ᵗf` is a morphism of unital `k`-algebras `H(K) → H(G)` such that the diagram `(∗)` of the
proposition is commutative.

Conversely, if `ᵗf` satisfies these conditions, then `ε_B ∘ f = ε_A` and the squares (1') and (2') are commutative.
Since, for `M = A ⨶ A` and `P = B` (resp. `M = A` and `P = B ⨶ B`), the map `g ↦ ᵗg` is injective, one deduces that
squares (1) and (2) are commutative, hence `f` is compatible with the multiplications and the diagonal morphisms of `A`
and `B`. It remains to see that `f(1_A) = 1_B`. But it follows from what precedes that `ε_B f(1) = 1`,
`∆_B f(1) = f(1) ⨶ f(1)` and `f(1) · f(1) = f(1)`. The first two conditions entail, by 2.1 (iii), that `f(1)` admits
`c_B f(1)` as inverse in `B`; consequently `f(1) · f(1) = f(1)` entails `f(1) = 1`. So `f : A → B` is a morphism of
`Alp/k`, compatible with the comultiplications of `A` and `B`.

#### 2.3.2.

<!-- label: III.VII_B.2.3.2 -->

<!-- original page 518 -->

Let us suppose now, for simplicity, that the ring `k` is artinian. When `G` is topologically flat over `k`, the algebra
`H(G) = H(G)(k)` may be characterized by a universal property (due to Cartier). Recall (cf. 1.2.1) that if `U` is a
`k`-module, one denotes by `W(U)` the functor which to every `k`-algebra `C` of finite length associates the `C`-module
`U ⊗_k C`.[^N.D.E-VII_B-88] If `U` is a `k`-algebra (associative, with unit element), so is `U ⊗_k C`; we shall denote
by `W(U)×` the `k`-group functor which to every `C ∈ Ob Alf_/k` associates the multiplicative group of the invertible
elements of the algebra `U ⊗_k C`:

```text
   W(U)×(C) = (U ⊗_k C)×.
```

Moreover, let us identify `G` with the `k`-group functor `C ↦ Hom_{Vaf_/k}(Spf(C), G)` and denote by
`Hom_{k-Gr.}(G, W(U)×)` the set of homomorphisms of `k`-group functors from `G` into `W(U)×`. One has the

**Proposition 2.3.2.** *Let `k` be an artinian ring. For every formal group `G` topologically flat over `k` and for
every `k`-algebra `U`, there is a canonical isomorphism*

```text
   Hom_{k-Gr.}(G, W(U)×) ⥲ Hom_{k-Alg.}(H(G), U).
```

<!-- label: III.VII_B.2.3.2.prop -->

Let us denote by `A` the affine algebra of `G`; by hypothesis it is a projective object of `PC(k)`, and `H(G) = A†`. For
every object `P` of `PC(k)`, let us denote by `U ⨶_k P` the projective limit of the `k`-modules `U ⊗_k (P/N)`, where `N`
ranges over the open submodules of `P`. One has linear maps

```text
   U ⊗_k (P/N) ─→ Hom_k((P/N)*, U)
```

sending `u ⊗ x` to the `k`-linear map `f ↦ f(x) u`, and forming a filtered projective system. One obtains therefore, by
passage to the projective limit, a morphism

```text
                       ψ_P
(1)    U ⨶_k P ─────────────→ Hom_k(P†, U) .
```

<!-- original page 519 -->

When `P = k`, `ψ_k` is evidently an isomorphism; moreover, the two sides of (1), considered as functors in `P`, commute
with infinite products (every product being a filtered projective limit of finite products). One obtains therefore that
(1) is an isomorphism when `P` is a product of copies of `k`, then when `P` is a projective object of `PC(k)` (the two
sides of (1) commuting with finite direct sums).

Let us now denote by `Hom_F(G, W(U))` the set of morphisms of `k`-functors from `G` into `W(U)`. Since
`G = Spf(A) = lim Spf(A/l)`, where `l` ranges over the open ideals of `A`, one has canonical isomorphisms

```text
   Hom_F(G, W(U)) = lim Hom_F(Spf(A/l), W(U)) = lim U ⊗_k (A/l) = U ⨶_k A.
```

By what precedes, one obtains therefore a canonical isomorphism:

```text
                                              ψ_A
(2)   Hom_F(G, W(U)) = U ⨶_k A ──────────────→ Hom_k(H(G), U).
```

For every `k`-algebra `C` of finite length, the multiplication makes `U ⊗_k C` into a monoid with unit, and every
morphism of monoids with unit `G(C) → U ⊗_k C` is necessarily a morphism of groups `G(C) → (U ⊗_k C)×`. Consequently,
one obtains that `Hom_{k-Gr.}(G, W(U)×)` is the part of `Hom_F(G, W(U))` formed by the morphisms of `k`-functors into
monoids with unit element.

It remains to see that these morphisms correspond to the `k`-linear maps from `H(G)` into `U` which preserve
multiplication and the unit elements.[^N.D.E-VII_B-89] To simplify the writing, `H(G) = A†` will be denoted `H` and one
will write `⨶` instead of `⨶_k`. Let `∆_A, m_A` and `ε_A` (resp. `∆_H, m_H` and `ε_H`) denote the comultiplication,
multiplication and augmentation of `A` (resp. `H`). Let `θ ∈ Hom_F(G, W(U))`, denote by `γ` its image in `U ⨶ A` and
`φ : H → U` the associated `k`-linear map. Then `θ` sends the unit section `s ∈ G(k)` onto an element `u` of `U`, and
since `s` corresponds to the augmentation `ε : A → k`, which is the unit element `1_H` of `H`, one sees that
`θ(s) = 1_U` if and only if `φ(1_H) = 1_U`.

Moreover, the morphism `θ ∘ m_G : G × G → W(U)` corresponds to the element `(id_U ⨶ ∆_A)(γ)`, and this corresponds, by
duality, to the map `φ ∘ m_H : H ⊗ H → U`.

On the other hand, the morphism `θ ∘ pr_1 : G × G → W(U)` corresponds to the element `γ ⨶ 1_A` of `U ⨶ A ⨶ A`, which
corresponds by duality to `φ ∘ (id_H ⊗ ε) : H ⊗ H → U`. Similarly, `θ ∘ pr_2` corresponds to the element `τ(γ ⨶ 1_A)` of
`U ⨶ A ⨶ A` (where `τ(u ⨶ a ⨶ b) = u ⨶ b ⨶ a`), which corresponds by duality to `φ ∘ (ε ⊗ id_H) : H ⊗ H → U`. Finally,
the multiplication map `μ = m_{U ⨶ A ⨶ A}` below:

```text
   (U ⨶ A ⨶ A) × (U ⨶ A ⨶ A),  (u ⨶ a₁ ⨶ a₂, u' ⨶ a₃ ⨶ a₄) ↦ uu' ⨶ a₁a₃ ⨶ a₂a₄
```

can be seen as the composite of the endomorphism `σ_{23}` of `(U ⊗ U) ⨶ A^{⨶ 4}` which "exchanges the factors `a₂` and
`a₃`", and the map

```text
                                m_U ⨶ m_A ⨶ m_A
   (U ⊗ U) ⨶ A^{⨶ 2} ⨶ A^{⨶ 2} ──────────────────→ U ⨶ A ⨶ A.
```

One deduces that the map `μ ∘ (φ ∘ pr_1, φ ∘ pr_2) : G × G → W(U)` corresponds to the composite map `β` below:

```text
                                  β
                H ⊗ H ─────────────────→ U
                  ↑                       ↑
   id_H ∘ σ_{23} ∘ id_H                   m_U
                                          
   H ⊗ H ⊗ H ⊗ H            U ⊗ U
                                          
   (id_H ⊗ ε_H) ⊗ (ε_H ⊗ id_H)   φ ⊗ φ
                                          
                H ⊗ H ────────────────────.
```

Finally, `θ` is compatible with the laws of `G` and of `W(U)×` if and only if `θ ∘ m_G` equals
`μ ∘ (φ ∘ pr_1, φ ∘ pr_2)` which is equivalent, by what precedes, to `φ ∘ m_H = β`. Now it is clear that
`(φ ∘ m_H)(x ⊗ y) = φ(xy)`, and one sees easily that `β(x ⊗ y) = φ(x) φ(y)`.

### 2.4.

<!-- label: III.VII_B.2.4 -->

Let us now return to an arbitrary pseudocompact ring `k` in order to apply to formal groups the results of 1.4–1.5 on
passage to the quotient by a topologically flat equivalence relation.[^N.D.E-VII_B-90]

Let `u : H → G` be a monomorphism of `k`-formal groups, `μ : G × G → G` the "multiplication" morphism of `G`, and `λ`
the composite morphism <!-- original page 520 -->

```text
                  id_G × u           μ
   λ :   G × H ────────────→ G × G ──────→ G.
```

Since `u` is a monomorphism, the couple

```text
              pr_1
              ────→
   G × H              G
              ────→
               λ
```

is an equivalence couple in `Vaf_/k` (cf. V, 2.b)). Recall (cf. 1.2.C) that the cokernel `G/H` of this couple is defined
as follows.

Let `O(G)` and `O(H)` be the affine algebras of `G` and `H`, `∆ : O(G) → O(G) ⨶_k O(G)` the diagonal morphism of `O(G)`,
and `I` the kernel of the morphism `u^♮ : O(G) → O(H)`. (One knows, by Proposition 1.3, that `u^♮` induces an
isomorphism `O(G)/I ⥲ O(H)`.) Then the affine algebra `O(G/H)` of `G/H` is the kernel of the couple of morphisms:

```text
                    τ_1
                    ───→
        O(G)                O(G) ⨶_k O(H),
                    ───→
              (id ⨶ u^♮)∆
```

where `τ_1(x) = x ⨶ 1`, i.e.,

```text
   O(G/H) = {x ∈ O(G) | ∆(x) − x ⨶ 1 ∈ O(G) ⨶ I}.
```

If, moreover, `H` is topologically flat over `k`, then `pr_1` is topologically flat and one deduces from Theorem 1.4 the
following theorem.

**Theorem 2.4.** *Let `u : H → G` be a monomorphism of `k`-formal groups. Assume `H` topologically flat over `k`. Then
the projection `p : G → G/H` is surjective and topologically flat, one has an isomorphism*

```text
(∗)                G × H ⥲ G ×_{G/H} G
```

*and `G/H` represents the quotient-sheaf for the flat topology.*

*Consequently, `G/H` is endowed with a canonical structure of object with group of operators `G`, such that
`p : G → G/H` is a morphism of objects with operators. If moreover `u` identifies `H` with an invariant subgroup of `G`,
then `G/H` is endowed with a canonical structure of `k`-formal group, such that `p : G → G/H` is a morphism of
`k`-formal groups, and `H` is the kernel of `p`.*

<!-- label: III.VII_B.2.4.thm -->

Indeed, the first assertion follows from 1.4; the other two from IV, Corollaries 5.2.2 and 5.2.4.

**Corollary 2.4.**[^N.D.E-VII_B-91] *Let `G` be a `k`-formal group, `H` a formal subgroup of `G`, `A` (resp. `A/J`, `B`)
the affine algebra of `G` (resp. `H`, `G/H`), `I_A` the augmentation ideal of `A`, and `I_B = B ∩ I_A`. Assume `H`
topologically flat over `k`. Then `J` equals `AI_B`, the closed ideal generated by `I_B`.*

<!-- label: III.VII_B.2.4.cor -->

Indeed, the projection `B → B/I_B` corresponds to the "unit section" `e : Spf(k) → G/H` of `G/H`. By `(∗)`, `H` is
identified with the fiber product `Spf(k) ×_{G/H} G`, and hence its affine algebra `A/J` is identified with
`(B/I_B) ⨶_B A ≃ A/AI_B`.

#### 2.4.A.

<!-- label: III.VII_B.2.4.A -->

Let `G, Q` be topologically flat `k`-formal groups; assume that there exist homomorphisms `σ : Q → G` and `π : G → Q`
such that `π ∘ σ = id_Q`. In particular, `σ` is a monomorphism, so `Q` is a formal subgroup of `G` (cf. Remark 1.3). Let
`N = Ker(π)` and `σ'` the inclusion `N ↪ G`. Then `G` is the semi-direct product of `N` by `Q` (cf. I, 2.3.8), i.e., for
every `B ∈ Ob Alf_/k`, identifying `N(B)` and `Q(B)` with their images in `G(B)` via `σ'` and `σ`, `N(B)` is an
invariant subgroup of `G(B)` and the map

```text
(1)    μ : N(B) × Q(B) ─→ G(B),    (x, q) ↦ xq
```

is bijective. Then the morphism of `k`-formal varieties

```text
(2)    θ : G(B) ─→ N(B),    g ↦ g · σπ(g⁻¹)
```

is a retraction of `σ'`, the inverse of `μ` is the map

```text
(3)    g ↦ (θ(g), π(g))
```

and `θ ∘ σ' : N → G/Q` is an isomorphism of `k`-formal varieties. In particular, `N` is topologically flat over `k`, by
1.4 (ii). Denote by `α` (resp. `β`) the map from `Q × N` (resp. `G × N = N × Q × N`) to `N` defined setwise by
`α(q, y) = qyq⁻¹` (resp. `β(x, q, y) = x α(q, y)`). Then one has the following commutative diagram:

```text
              id × θ          θ × id
   G × G ───────────→ G × N ──────────→ N × N
                                       
   m_G                  β                m_N
                                       
              θ
   G ────────────────→ N.
```

This may be expressed as follows in terms of the affine algebras `A`, `A₀` and `A'` of `G`, `Q` and `N` (cf. 5.1.3
below). Let `ρ' : A → A'`, `ρ : A → A₀` and `τ : A₀ → A` be the homomorphisms of `k`-bialgebras corresponding to `σ'`,
`σ` and `π`, and let `I = Ker(ρ)`. Then, by the preceding Corollary, `A'` is identified with `A/Aτ(J₀)`, where `J₀`
denotes the augmentation ideal of `A₀`.

On the other hand, let `B` be the affine algebra of `G/Q`; it is the kernel of the couple of morphisms

```text
                  τ_1
                  ────→
     A                       A ⨶_k A₀,
                  ────→
            (id ⨶ ρ)∆_A
```

i.e., `B = {x ∈ A | ∆_A(x) − x ⨶ 1 ∈ A ⨶ I}`. Denote by `γ` the continuous morphism of `k`-algebras `θ^♮ : A' → A`; it
is a section of `ρ'` and an isomorphism of profinite `k`-algebras from `A'` onto `B`. On the other hand, `τ = π^♮`
identifies `A₀` with a sub-bialgebra of `A`, which is none other than the affine algebra of the quotient `N \ G`. One
deduces from (1) and (3) that one has an isomorphism of profinite `k`-algebras

```text
(∗)    A' ⨶_k A₀ ⥲ A,    a' ⨶ a₀ ↦ γ(a') τ(a₀),
```

whose inverse is the map `a ↦ (ρ' ⨶ ρ)∆_A(a)`.

Finally, let us identify `A'` with its image in `A` via `γ`, so that the projection `A → A'` is then `γρ'`. Denoting by
`∆_{A'}` the comultiplication of `A'`, one deduces from (4) that `∆_A(A') ⊂ A ⨶ A'` and that the following diagram is
commutative:

```text
              ∆_A
        A' ────────→ A ⨶ A'
                          γρ' ⨶ id
                          
              ∆_{A'}
        A' ────────→ A' ⨶ A'
```

(one also has therefore `γρ' ∘ c_A = c_{A'}`, where `c_A` (resp. `c_{A'}`) is the antipode of `A` (resp. `A'`)). On the
other hand, denoting by `m_A` the multiplication of `A`, one deduces from (2) that, for every `a ∈ A`,

```text
   γρ'(a) = (m_A ∘ (id ⊗ τρ c_A) ∘ ∆_A)(a).
```

#### 2.4.B.

<!-- label: III.VII_B.2.4.B -->

Let us suppose, for simplicity, `k` artinian. Then what precedes is expressed more simply in terms of the covariant
bialgebras of `G, Q, N`. Indeed, since `G = N × Q` as `k`-formal varieties, then `H(G) = H(N) ⨶_k H(Q)` as
`k`-coalgebras. Moreover, since the multiplication of `G` is given by

```text
   (x, q) · (x', q') = (x α(q, x'), qq'),    where α(q, x') = qx'q⁻¹,
```

the multiplication of `H(G)` is given as follows: for every `x ∈ H(N), q ∈ H(Q)`,

```text
   (x ⊗ q) · (x' ⊗ q') = x φ(q, x') ⊗ qq',
```

where `φ : H(Q) ⨶_k H(N)` is the morphism of `k`-coalgebras induced by `α`. Since `α` is the composite morphism below
(where `δ_G` (resp. `m_G`) is the diagonal morphism (resp. multiplication) of `G`, `c_Q` the inversion morphism of `Q`,
and `v(q ⨶ q' ⨶ x) = q ⨶ x ⨶ q'`):

```text
              v ∘ (δ_G × id)              id × id × c_Q             m_G
   Q × N ────────────────────→ Q × N × Q ─────────────────→ Q × N × Q ──────→ G,
```

one obtains, denoting still by `c_Q` the antipode of `H(Q)`, that

```text
(⋆)    φ(q ⊗ x') = Σ_i q_i x' c_Q(q'_i)    if ∆_{H(Q)}(q) = Σ_i q_i ⊗ q'_i.
```

In particular, if `M` is an abstract group and if `H(Q)` is the group algebra `kM` (i.e., `Q = Spf* kM` is the constant
`k`-formal group `M_k`), then for every `γ ∈ M` and `x' ∈ H(N)` one has `φ(γ ⊗ x') = γ x' γ⁻¹`, and this defines an
action of `M` on `H(N)` by Hopf algebra automorphisms.

#### 2.4.1. Proposition.

<!-- label: III.VII_B.2.4.1 -->

**Proposition 2.4.1.** *Let `f : G → K` be a morphism of `k`-formal groups. If `H = Ker(f)` is topologically flat over
`k`, the homomorphism `f' : G/H → K` <!-- original page 521 --> induced by `f` is a monomorphism.*

<!-- label: III.VII_B.2.4.1.prop -->

This is a consequence of the results of Exposé IV;[^N.D.E-VII_B-93] we nonetheless give a direct proof. Let `T` be a
formal variety of finite length over `k` and `t` an element of `(G/H)(T)` such that `f' ∘ t` is the unit element of
`K(T)`. We must show that `t` is the unit element of `(G/H)(T)`. Denote by `p` the projection `G → G/H` and by `X` the
fiber product `T ×_{G/H} G`.

By 2.4, `p` is surjective and topologically flat, hence so is the morphism `pr_1 : X → T`, hence `pr_1` is an
epimorphism by Proposition 1.3.1, hence it suffices to show that `t ∘ pr_1` is the unit element of `(G/H)(X)`. Denote by
`pr_2` the projection `X → G`; one has `t ∘ pr_1 = p ∘ pr_2`, whence the equality
`1 = f' ∘ t ∘ pr_1 = f' ∘ p ∘ pr_2 = f ∘ pr_2`. Then the exact sequence

```text
                              f
   1 ─────→ H ──────→ G ──────→ K
```

shows that `pr_2` factors through `H`, hence `p ∘ pr_2` is the zero morphism. Since `p ∘ pr_2 = t ∘ pr_1`, this proves
the proposition.

One deduces from the proposition the following corollary. Let `O(G), O(K)` and `O(G/H)` denote the affine algebras of
`G`, `K` and `G/H`; one has seen (2.4) that `p` induces an injection of `O(G/H)` into `O(G)`. Moreover, by Proposition
1.3, since `f' : G/H → K` is a monomorphism, the morphism `O(K) → O(G/H)` is surjective, whence:

**Corollary 2.4.1.** *Let `f : G → K` be a morphism of `k`-formal groups and `H = Ker(f)`. If `H` is topologically flat
over `k`, then `O(G/H)` is the image of `O(K)` in `O(G)`.*

<!-- label: III.VII_B.2.4.1.cor -->

#### 2.4.2.

<!-- label: III.VII_B.2.4.2 -->

Let us keep the preceding notations and assume `H` and `G` topologically flat over `k`. Then `G` is topologically flat
over `k` and over `G/H`, hence, by 1.3.3, `G/H` is topologically flat over `k`. Consequently, by 2.4, the canonical
projection `q` from `K` onto `Coker(f')` is topologically flat and `f'` is an isomorphism from `G/H` onto `Ker(q)`. It
is clear on the other hand that one has `Coker(f) = Coker(f')`. Hence, under the hypothesis that `G` and `H = Ker(f)`
are topologically flat over `k`, one has obtained an isomorphism between `Ker(q)`, the image of `f`, and `G/Ker(f)`, the
coimage of `f`. This entails the theorem below.

**Theorem 2.4.2.** *Let `k` be a field. The commutative `k`-formal groups form an abelian category.*
    <!-- original page 522 -->

<!-- label: III.VII_B.2.4.2.thm -->

**Corollary 2.4.2.** *Let `k` be a field. The commutative affine `k`-group schemes form an abelian
category.*[^N.D.E-VII_B-94]

<!-- label: III.VII_B.2.4.2.cor -->

This follows from the theorem and the equivalence of categories 2.2.2.

### 2.5.

<!-- label: III.VII_B.2.5 -->

A `k`-formal group is said to be *étale* if the underlying formal variety is étale (cf. 1.6); these formal groups have a
very simple structure. Indeed, suppose `k` local; let `κ` be the residue field of `k`, `κ_s` a separable closure of `κ`,
and `Γ` the topological Galois group of `κ_s` over `κ`. Let us call a *`Γ`-set* the datum of a set `E` and a continuous
operation of `Γ` on `E` (i.e., the isotropy group of every element `x ∈ E` is an open subgroup of `Γ`).

For every `k`-formal variety `X`, one sets:

```text
   X(κ_s) = lim X(ℓ),
            ──→
              ℓ
```

where `ℓ` ranges over the finite extensions of `κ` contained in `κ_s`.[^N.D.E-VII_B-95] Then `Γ` operates continuously
on each `X(ℓ)`, hence also on `X(κ_s)`. Moreover, let `X_κ = X ⨶_k κ` (cf. 1.6.C); for every `ℓ` one has
`X(ℓ) = X_κ(ℓ)`, whence `X(κ_s) = X_κ(κ_s)`.

Suppose now `X` étale over `k`; then `X_κ` is the `κ`-formal variety direct sum of the `Spec κ(x)`, for `x ∈ X`, and if
one denotes by `X'_κ` the `κ`-scheme direct sum of the `Spec κ(x)`, one sees that `X_κ(κ_s)` is none other than
`X'_κ(κ_s) = Hom_{(Sch/κ)}(Spec κ_s, X'_κ)`.

Let us denote `𝒞 = (Sch^ét_/κ)` the full subcategory of `(Sch_/κ)` formed by the étale `κ`-schemes. One knows that the
functor `X' ↦ X'(κ_s)` is an equivalence of `𝒞` onto the category `𝒞'` of `Γ`-sets (cf. SGA 1, V §§ 7–8 or [DG70], § I.4
6.4); it therefore induces an equivalence between the category of `𝒞`-groups and that of `𝒞'`-groups; now one sees at
once that a `𝒞'`-group is the same thing as an abstract group `G` endowed with a continuous operation of `Γ` by group
automorphisms (one will then say that `G` is a *`Γ`-group*).

Taking into account the equivalences `Vaf^ét_/k ⥲ Vaf^ét_/κ ⥲ (Sch^ét_/κ)` of 1.6.E, one therefore obtains:

**Proposition 2.5.** *Let `k` be a local pseudocompact ring, `κ` its residue field, `κ_s` a separable closure of `κ`,
and `Γ = Gal(κ_s/κ)`.*

*(i) The functor `X ↦ X(κ_s)` is an equivalence of the category of étale `k`-formal varieties onto that of `Γ`-sets.*

*(ii) It induces an equivalence of the category of étale `k`-formal groups onto that of `Γ`-groups.*

<!-- label: III.VII_B.2.5.prop -->

**Remark 2.5.A.**[^N.D.E-VII_B-96] Let `k` be a field, `k_s` a separable closure of `k`, `G` an étale `k`-formal group
and `M` the abstract group `G(k_s)`. Let us denote by `X` a set of representatives of the orbits of `Γ = Gal(k_s/k)` in
`M`, and for every `x ∈ X` let `Γ_x` be its stabilizer, which is a subgroup of `Γ` of finite index, and
`L_x = k_s^{Γ_x}`, which is an extension of `k` of degree `[Γ : Γ_x]` (see, for example, [BAlg], V § 10.10). Then, by
the equivalence of categories above, the affine algebra `𝒜(G)` of `G` is the product of the `L_x`, endowed with the
product topology, and hence the `L_x` are precisely the simple quotients `𝒜(G)/m`, where `m` is a maximal open ideal of
`𝒜(G)`. Since these correspond by duality to the subcoalgebras of `H(G)`, one obtains that `H(G)` is pointed (i.e.,
`dim_k(C) = 1` for every simple subcoalgebra `C`) if and only if `L_x = k` for every `x`, and in this case `𝒜(G)` is the
topological algebra `k^M`, hence `H(G)` is the group algebra `kM`, and one has

```text
   M = {x ∈ H(G) | ε(x) = 1 and ∆(x) = x ⊗ x} = G(k).
```

<!-- label: III.VII_B.2.5.A -->

#### 2.5.1.

<!-- label: III.VII_B.2.5.1 -->

Let us now suppose `k` an arbitrary pseudocompact ring. Since the functor <!-- original page 523 --> `X ↦ X_e` of 1.6.F
commutes with finite products, it transforms every formal group `G` into an étale formal group `G_e`, and since the
morphism `p : X → X_e` of loc. cit. is functorial in `X`, then `p : G → G_e` is in this case a morphism of formal
groups.

Consider the kernel `Ker(p)`;[^N.D.E-VII_B-97] it is the fiber product of the diagram:

```text
                       G
                          p
                  ε       
                          
       Spf(k) ──────→ G_e
```

where `ε` is the unit section of `G_e`. Since `p` induces a bijection on the underlying sets, one deduces (cf. 1.2,
N.D.E. (41)) that `Ker(p)` has as underlying set the image of `Spf(k)` under `ε` and that for every point `s` of
`Spf(k)`, the local algebra of `Ker(p)` at the point `ε(s)` is `O_{G, ε(s)} ⨶_{O_{G_e, ε(s)}} k_s`. Moreover, at each
point `ε(s)`, the residue field of `O_{G, ε(s)}` is `κ(s)`, and hence `O_{G_e, ε(s)} = k_s`, whence
`O_{Ker(p), ε(s)} = O_{G, ε(s)}`. For these reasons we shall say that `Ker(p)` is the *infinitesimal neighborhood of the
origin* of `G` and we shall write `Ker(p) = G⁰`, thereby obtaining an exact sequence:

```text
                       incl.        p
   1 ──────→ G⁰ ─────────────→ G ──────→ G_e.
```

In what follows, we shall say that `G` is *infinitesimal* if `G = G⁰`.[^N.D.E-VII_B-98] This is equivalent to saying
that for every `s ∈ Spf(k)`, or also for every continuous morphism `k → κ`, where `κ` is a field endowed with the
discrete topology, the unit element is the unique element of `G(κ(s))` resp. of `G(κ)`.

Suppose furthermore that `G` is topologically flat over `k`.[^N.D.E-VII_B-99] Then, by 1.6.1, the morphism `p : G → G_e`
is topologically flat, and since it is bijective, it is therefore an effective epimorphism by Proposition 1.3.1.
Consequently, `G_e` is identified with the quotient `G/G⁰`. One has therefore obtained:

**Corollary 2.5.1.** *Let `G` be a formal group topologically flat over `k`. Then `G_e` is identified with the quotient
`G/G⁰`; i.e., one has an exact sequence of formal groups:*

```text
                              incl.       p
   1 ──────→ G⁰ ─────────────→ G ──────→ G_e ──────→ 1.
```

<!-- label: III.VII_B.2.5.1.cor -->

#### 2.5.2.

<!-- label: III.VII_B.2.5.2 -->

Suppose `k` is a perfect field. In this case, one has seen (cf. 1.6.2) that the morphism `p : X ↦ X_e` admits a section
`s : X_e → X` which depends functorially <!-- original page 524 --> on `X`; this section is therefore a morphism of
formal groups when `X` is a formal group. One obtains thus:

**Proposition 2.5.2.** *When `k` is a perfect field, every `k`-formal group `G` is canonically isomorphic to the
semi-direct product of an infinitesimal group `G⁰` and an étale group `G_e` operating on `G⁰`.*[^N.D.E-VII_B-100]

*If, moreover, `G` is commutative, then `G` is the product of `G⁰` and of `G_e`. By 2.2.2, this canonical decomposition
of commutative `k`-formal groups corresponds to an analogous decomposition of affine commutative `k`-group schemes; see
paragraph 2.5.3 below.*

<!-- label: III.VII_B.2.5.2.prop -->

**Remark 2.5.2.A.**[^N.D.E-VII_B-101] The exact sequence `1 → G⁰ → G → G_e → 1` is not necessarily split when `k` is not
perfect: let us give the following example, taken from [DG70], § III.6, 8.6. Let `k` be a non-perfect field of
characteristic `p > 0`. Let `λ ∈ k − k^p`, let `L_λ` be the abelian `p`-Lie algebra with basis `(x, y)`, the *symbolic
`p`-th power* (cf. VII_A, 5.2) being given by `x^{(p)} = x` and `y^{(p)} = λx`, let
`U_p(L_λ) = k[x, y]/(x^p − x, y^p − λx)` be the restricted enveloping algebra of `L_λ` (cf. VII_A, 5.3), and let `G_λ`
be the commutative `k`-formal group with affine algebra `U_p(L_λ)`. Then `G_λ` is a non-split extension of the étale
constant `k`-group `(ℤ/pℤ)_k` by the infinitesimal `k`-group `α_{p,k} = Spf k[x]/(x^p − x)`, i.e., one has a non-split
exact sequence of commutative `k`-formal groups:[^N.D.E-VII_B-102]

```text
   0 ─────→ α_{p,k} ─────→ G_λ ─────→ (ℤ/pℤ)_k ─────→ 0.
```

It corresponds by duality to a non-split exact sequence of commutative `k`-algebraic groups:

```text
   0 ─────→ μ_{p,k} ─────→ D'(G_λ) ─────→ α_{p,k} ─────→ 0,
```

where `μ_{p,k} = Spec k[t]/(t^p − 1)` (and one obtains thus all extensions of `α_{p,k}` by `μ_{p,k}`, cf. [DG70], §
III.6, 8.6).

<!-- label: III.VII_B.2.5.2.A -->

#### 2.5.3.

<!-- label: III.VII_B.2.5.3 -->

Let `k` be a field.

**Definition 2.5.3.A.** *One says that a commutative `k`-group scheme is* unipotent *if it is isomorphic to `Spec H(G)`,
where `G` is an infinitesimal commutative `k`-formal group.*[^N.D.E-VII_B-104]

<!-- label: III.VII_B.2.5.3.A -->

On the other hand, following Exp. IX, Definition 1.1, one says that a `k`-group scheme `H` is *of multiplicative type*
if there exists a scheme `S`, faithfully flat and quasi-compact over `Spec k`, such that `H_S` is a diagonalizable
`S`-group, i.e., is isomorphic to `D_S(M)` for some "abstract" abelian group `M`.[^N.D.E-VII_B-105] By (fpqc) descent,
this implies that `H` is affine and commutative. On the other hand, since one may replace `S` by the residue field of
one of its points, one sees that `H` is of multiplicative type if and only if there exists an extension `K` of `k` such
that `H_K` is a diagonalizable `K`-group.

**Proposition 2.5.3.B.** *Let `T` be an affine commutative `k`-group scheme and let `k_s` be a separable closure of
`k`.*

*(i) For `T` to be of multiplicative type, it is necessary and sufficient that its dual `D(T)` be an étale commutative
`k`-formal group.*

*(ii) Consequently, `T` is of multiplicative type if and only if `T ⨶_k k_s` is diagonalizable.*

<!-- label: III.VII_B.2.5.3.B -->

*Proof.* Let `A` denote the affine algebra of `D(T)` and `A₀` its local component at the neutral element; then `D(T)` is
étale over `k` if and only if `A₀ = k`. If `K` is an extension of `k`, then the algebra `A₀ ⨶_k K` is local (since it is
a projective limit of local artinian rings), so it coincides with the local component `(A ⨶_k K)₀`; moreover, since the
formation of `D(T)` commutes with base change (cf. 2.2.2), one also has `A ⨶_k K ≃ D(T_K)`.

Suppose `T` of multiplicative type; then there exists an extension `K` of `k` such that `O(T) ⨶_k K` is isomorphic, as a
`K`-Hopf algebra, to the group algebra `KM`, for some abelian group `M`. Then `A ⨶_k K` is isomorphic to the algebra
`K^M`, endowed with the product topology, hence one has `K = (A ⨶_k K)₀ = A₀ ⨶_k K` and this entails that `A₀ = k`, so
`D(T)` is étale.

Conversely, suppose `D(T)` étale. Then `D(T) ⨶_k k_s = D(T_{k_s})` is a `k_s`-constant group `M`, so its covariant
bigèbre is the group algebra `k_s M` (cf. Remark 2.5.A), so `O(T) ⨶_k k_s = k_s M`, which proves that `T` is of
multiplicative type, and split by the extension `k → k_s`. The proposition follows.

By 2.2.2, 2.5.1, and 2.5, one obtains:

**Corollary 2.5.3.C.** *Let `k` be a field and `G` an affine commutative `k`-group scheme.*

*(i) `G` contains a subgroup of multiplicative type `G_m` such that `G/G_m` is unipotent.*

*(ii) When `k` is perfect, there exists furthermore a canonical retraction of `G` onto `G_m`, so that `G` is the product
of a unipotent group and a group of multiplicative type.*

*(iii)*[^N.D.E-VII_B-106] *Let `k_s` be a separable closure of `k` and `Γ = Gal(k_s/k)`. The category of `k`-group
schemes of multiplicative type is anti-equivalent to the category of continuous `Γ`-modules.*

<!-- label: III.VII_B.2.5.3.C -->

### 2.6.

<!-- label: III.VII_B.2.6 -->

We shall now study infinitesimal formal groups, to which the following paragraphs are devoted. In this study, Lie
algebras play a primordial role.

Suppose first that the base ring `k` is artinian and let `G` be a formal group over `k`. One can give three different
interpretations of the Lie algebra of `G`, all of which we shall use:

a) Let `D` be the algebra `k[d]/(d²)` of dual numbers over `k` and `δ` the homomorphism <!-- original page 525 --> from
`D` to `k` which annihilates `d`. For every formal group `G` over `k`, `Lie(G)` is the kernel of `G(δ)`, so that by
definition one has an exact sequence of groups

```text
   1 ────→ Lie(G) ────→ G(D) ──G(δ)──→ G(k) ────→ 1.
```

b) Let `A` be the affine algebra of `G` and `I_A = Ker ε_A` its augmentation ideal. The group `G(D)` has as elements the
morphisms of profinite `k`-algebras `f : A → D`. The condition `G(δ)(f) = 1` is equivalent to `δ ∘ f = ε_A`. Since
`x − ε_A(x) · 1_A ∈ I_A` for every `x ∈ A`, this is equivalent to `f(I_A) ⊂ k · d`, hence `Ker(f)` contains `I_A²` and
therefore also `Ī_A²` (the closure), so `f` induces a continuous linear map `f' : I_A / I_A² = ω_{G/k} → k` such that,
for every `x ∈ A`, one has the equality

```text
   f(x) = ε_A(x) · 1_D + f'(x̄) · d,
```

where `x̄` designates the image of `x − ε_A(x) · 1_A` in `I_A/I_A²`. One sees then that the map `f ↦ f'` defines a
bijection of `Lie(G)` onto the topological dual `ω_{G/k}†` of `ω_{G/k}` (cf. 0.2.2).

This bijection respects the group structures. Indeed, let `f` and `g` be two elements of `Lie(G)`; their product `f · g`
is the composite map `h ∘ ∆_A`, where `h : A ⨶ A → D` is such that `h(b ⨶ b') = f(b) g(b')`. Now if `a ∈ I_A` one has,
by 2.1 (ii), `∆_A(a) − a ⨶ 1 − 1 ⨶ a ∈ I_A ⨶ I_A`, whence `(f · g)(a) = f(a) + g(a)` (cf. also II 3.10).

In what follows, we identify `Lie(G)` with `ω_{G/k}†` by means of the bijection `f ↦ f'` described above. The group
`Lie(G)` is thus endowed with a structure of `k`-module.

<!-- original page 526 -->

c) Let `A†` and `D†` be the `k`-modules dual to `A` and `D`, `{1_D†, d†}` the dual basis of the basis `{1_D, d}` of `D`
over `k` (one has `1_D† = δ`). Since `D` is free of finite rank over `k`, the canonical map

```text
   Hom_c(A, D) ─→ Hom_k(D†, A†),    f ↦ ᵗf
```

is bijective. On the other hand, `f` is determined by the values `ᵗf(1_D*)` and `ᵗf(d*) = x`.

The condition `G(δ)(f) = 1` is equivalent to the equality `ᵗf(1_D*) = ε_A`. One sees easily on the other hand that `f`
is compatible with multiplication if and only if one has (cf. 2.3):

```text
(∗)    δ_G(x) = ϕ_G(x ⊗ 1 + 1 ⊗ x).
```

Finally, it is clear that a continuous linear map `f : A → D` which is compatible with multiplication and such that
`δ ∘ f = ε_A` sends the unit element of `A` to that of `D`.[^N.D.E-VII_B-107] The map `f ↦ x` thus permits us to
identify `Lie(G)` with the set of "primitive elements" of `H(G)` (i.e., the `x ∈ H(G)` satisfying relation `(∗)`). If
`x` and `y` are two such elements, one has

```text
   δ_G(xy) = δ_G(x) δ_G(y) = ϕ_G(x ⊗ 1 + 1 ⊗ x)(y ⊗ 1 + 1 ⊗ y)
          = ϕ_G(xy ⊗ 1 + x ⊗ y + y ⊗ x + 1 ⊗ xy),
```

whence `δ_G(xy − yx) = ϕ_G((xy − yx) ⊗ 1 + 1 ⊗ (xy − yx))`.

This shows that the `k`-module `Lie(G)` is identified with a Lie subalgebra of `H(G)`: we shall say that `Lie(G)` is the
*Lie algebra* of `G`.[^N.D.E-VII_B-108]

#### 2.6.1.

<!-- label: III.VII_B.2.6.1 -->

<!-- original page 527 -->

When `k` is an arbitrary pseudocompact ring and `G` a formal group over `k`, we call *`O_k`-Lie algebra of `G`* the
functor `Lie(G)` which associates to every object `C` of `Alf_/k` the `C`-Lie algebra of the `C`-formal group
`G' = G ⨶_k C`:[^N.D.E-VII_B-109] set `A' = A ⨶_k C`, since `I_A` is a direct factor of `A`, then `I_{A'}` equals
`I_A ⨶_k C = I_A ⨶_A A'`, and since `ω_{G/k} = I_A ⨶_A k` and similarly `ω_{G'/C} = I_{A'} ⨶_{A'} C`, one obtains that
`ω_{G'/C} = ω_{G/k} ⨶_A C` and hence

```text
   Lie(G)(C) = Hom_c(ω_{G/k} ⨶_A C, C)    i.e.    Lie(G) = V_kf(ω_{G/k})
```

(with the notations of 1.2.3.B). Therefore, by Proposition 1.2.3.E, `Lie(G)` is flat over `O_k` if and only if `ω_{G/k}`
is a projective pseudocompact `k`-module.

#### 2.6.2.

<!-- label: III.VII_B.2.6.2 -->

Conversely, every Lie algebra `L` over `O_k` defines a `k`-group functor. Indeed, let us denote by `U(L)` the functor
which associates to every object `C` of `Alf_/k` the enveloping algebra `U(L(C))` of the `C`-Lie algebra `L(C)`. By
VII_A, 3.2.2, `U(L)` is a bialgebra over `O_k` and therefore determines, by 2.2, a `k`-group functor `Spf* U(L)` which
we shall henceforth denote `𝒢(L)`. Thus, `𝒢(L)(C)` is the group of elements `z ∈ U(L(C))` of augmentation `1` and such
that `∆_{U(L(C))}(z) = z ⊗ z`.

Moreover, when `L` is flat over `O_k`, one has the following proposition.

**Proposition 2.6.2.**[^N.D.E-VII_B-110] *Let `L` be a flat `O_k`-Lie algebra.*

*(i) `𝒢(L)` is a formal group topologically flat over `k`, having `U(L)` as `O_k`-bialgebra.*

*(ii) `𝒢(L)` is infinitesimal.*

*(iii) For every object `C` of `Alf_/k`, `Lie(𝒢(L))(C)` is identified with the set*

```text
   Prim U(L(C)) = {x ∈ U(L(C)) | ε(x) = 0 and ∆(x) = x ⊗ 1 + 1 ⊗ x}
```

*of primitive elements of `U(L(C))`. In particular, one has a natural morphism of `O_k`-Lie algebras
`τ_L : L → Lie(𝒢(L))`.*

<!-- label: III.VII_B.2.6.2.prop -->

Indeed, the hypothesis that `L` be flat over `O_k` means that for every morphism `C → D` of `Alf_/k`, one has
`L(D) = L(C) ⊗_C D`, and that for each local component `C'` of `C`, `L(C')` is a free `C'`-module. The first condition
entails that `U(L(D)) = U(L(C)) ⊗ D` (by the universal property of the tensor product and that of the functor
`L ↦ U(L)`), and the second condition entails, by the Poincaré–Birkhoff–Witt theorem (cf. Bourbaki, *Groupes et algèbres
de Lie*, I 2.7), that `U(L(C'))` is a free `C'`-module. Therefore the bialgebra `U(L)` is flat over `O_k`.

To prove (ii) and (iii), one may suppose `k` artinian. Set then `L = L(k)`, `U = U(L)`, `U_0 = k · 1_U` and let `U⁺` be
the two-sided ideal of `U` generated by the image of `L`. Set in addition, for every `n ⩾ 1`,

```text
   U_n = {u ∈ U | ∆_U(u) − u ⊗ 1 ∈ U_{n−1} ⊗ U⁺}.
```

By 1.3.6, it suffices to show that `U` is the union of the `U_n`. Now, if one identifies `L` with its
    <!-- original page 528 --> canonical image in `U`, `L` is evidently contained in `U_1`. If `x_1, …, x_n` are elements of
`L`, one has `∆_U(x_1 ⋯ x_n) = (x_1 ⊗ 1 + 1 ⊗ x_1) ⋯ (x_n ⊗ 1 + 1 ⊗ x_n)`, which shows, by induction on `n`, that the
product `x_1 ⋯ x_n` belongs to `U_n`, hence that `U = ∪_n U_n`. This proves (ii).

On the other hand, let `D = k[d]/(d²)` be the algebra of dual numbers over `k`. By hypothesis one has `L(D) ≃ L ⊗ D`,
whence `U(L(D)) ≃ U ⊗ D`, by the universal properties of the tensor product and of the enveloping algebra. It follows
that `Lie(𝒢(L))(k)` is identified with the set of elements `z = 1 + xd` of `U ⊕ Ud` (where `x ∈ U`) such that `ε(z) = 1`
and `∆(z) = z ⊗ z`, which is equivalent to `ε(x) = 0` and `∆(x) = x ⊗ 1 + 1 ⊗ x`, i.e., to `x ∈ Prim U`. In particular,
the map `τ_L : x ↦ 1 + dx` is a morphism of `O_k`-Lie algebras, from `L` to `Lie(𝒢(L))`.

#### 2.6.3.

<!-- label: III.VII_B.2.6.3 -->

If `L` is a Lie algebra flat over `O_k`, the formal group `𝒢(L)` may be characterized by a universal
property.[^N.D.E-VII_B-111] Indeed, every morphism `φ` from `𝒢(L)` into a formal group `G` induces a morphism
`Lie(φ) : Lie(𝒢(L)) → Lie(G)`; composing it with the morphism `τ_L : L → Lie(𝒢(L))` (cf. 2.6.2), one obtains a morphism
`φ' : L → Lie(G)`, and one has:

**Proposition 2.6.3.** *If `G` is a `k`-formal group and `L` a flat `O_k`-Lie algebra, the map `φ ↦ φ'` defined above is
a bijection*

```text
   Hom_{Grf/k}(𝒢(L), G) ⥲ Hom_{Lie}(L, Lie(G))
```

*where the right-hand term designates the set of morphisms of `O_k`-Lie algebras from `L` to `Lie(G)`.*

<!-- label: III.VII_B.2.6.3.prop -->

One reduces at once to the case where `k` is artinian. Set `L = L(k)`. By 2.3.1, `Hom_{Grf/k}(𝒢(L), G)` is in bijection
with the set of unital algebra morphisms `φ : U(L) → H(G)` such that the following diagram is commutative:

```text
                  h
        U(L) ────────→ H(G)
          ↑                \
                            \ δ_G
                             \
      ∆_{U(L)}                H(G × G)
                             /
                            /
                           / ϕ_G
                  h ⊗ h    
        U(L) ⊗ U(L) ─→ H(G) ⊗ H(G)
```

<!-- original page 529 -->

Now `h` is determined by its restriction to `L`, which is a morphism of Lie algebras from `L` to the Lie algebra
underlying `H(G)`, and the commutativity of the diagram means that `h` sends `L` into the part of `H(G)` formed by the
`x` such that `δ_G(x) = ϕ_G(x ⊗ 1 + 1 ⊗ x)`, which is none other than `Lie(G)`, cf. 2.6 c).

### 2.7.

<!-- label: III.VII_B.2.7 -->

We end these generalities with a statement which goes back to S. Lie and which will serve us in paragraph 5.1. A *formal
monoid* over `k` is by definition a couple `(M, m)` consisting of a formal variety `M` and a morphism `m : M × M → M`
such that `m(C)` makes `M(C)` into a monoid for every object `C` of `Alf_/k`.[^N.D.E-VII_B-112] In particular, the "unit
section", which associates to every object `C` the unit element of `M(C)`, defines <!-- original page 565 --> a section
`ε_M` of the canonical projection `M → Spf(k)`. We shall say that the formal monoid `M` is *infinitesimal* if `ε_M`
induces a bijection of the underlying sets.

**Proposition 2.7.** *Every topologically flat infinitesimal `k`-formal monoid `M` is a `k`-formal
group.*[^N.D.E-VII_B-113]

<!-- label: III.VII_B.2.7.prop -->

We must show that `M(C)` is a group for every object `C` of `Alf_/k`. One reduces immediately to the case where `k` is
artinian. Let then `U = H(M)` be the coalgebra of `M` (1.3.5); the multiplication `m : M × M → M` induces a morphism of
coalgebras `m_U : U ⊗ U → U`, which makes `U` into an associative algebra over `k`; this algebra has as unit element the
image of the unit element of `k` by the map from `k` into `U` <!-- original page 530 --> induced by the unit section
`ε_M` of `M`. Similarly, the projection `M → Spf(k)` induces a homomorphism `ε_U` from `U` to `k`; we shall denote `U⁺`
the kernel of `ε_U`.

We must show that there exists an antipodism, that is, a morphism of coalgebras `c_U : U → U` such that, for every
`u ∈ U`,

```text
(∗)    (m_U ∘ (c_U ⊗ id_U) ∘ ∆_U)(x) = ε_U(u) · 1_U.
```

Let `(U_n)` be the filtration of `U` defined in 1.3.6, set `U⁺_n = U⁺ ∩ U_n`. Since `M` is infinitesimal, `U⁺` is the
union of the submodules `U⁺_n`.[^N.D.E-VII_B-114] One sets `c_0(1) = 1` and `c_1(x) = −x` if `x ∈ U⁺_1`, i.e., if `x` is
a primitive element. Suppose `c_{n−1} : U_{n−1} → U` constructed so as to satisfy `(∗)` for every `x ∈ U_{n−1}`, and let
`x ∈ U⁺_n`. By the proof of Lemma 1.3.6.A, one has `∆_U(x) − x ⊗ 1 ∈ U_{n−1} ⊗ U⁺` (this is where the hypothesis that
`U` be flat over `k` intervenes), so one may write `∆_U(x) = x ⊗ 1 + Σ_i y_i ⊗ z_i`, with `y_i ∈ U_{n−1}`; one then sets
`c_n(x) = −Σ_i c_{n−1}(y_i) z_i`. One obtains thus a `k`-linear map `c : U → U`, which is the left inverse of `id_U` for
the monoid law on `End_k(U)`, defined by `f · g = m_U ∘ (f ⊗ g) ∘ ∆_U` (the unit element being the map
`η : u ↦ ε(u) · 1_U`). It follows that `c` is uniquely determined, and is also the right inverse of `id_U`, i.e., one
also has `m_U ∘ (c_U ⊗ id_U) ∘ ∆_U = η` (without supposing `U` cocommutative).

### 2.8. Unipotent group schemes over a field.

<!-- label: III.VII_B.2.8 -->

Let `k` be a field. "Recall" that a `k`-group scheme `G` is said to be *unipotent* if it satisfies the following two
conditions (cf. [DG70], § IV.2, Prop. 2.5):

(a) `G` is affine.

(b) Every simple `O(G)`-comodule is trivial, i.e., if `ρ : V → V ⊗_k O(G)` is an `O(G)`-comodule structure on a
`k`-vector space `V ≠ 0`, and if there exists no nonzero subspace `W ≠ V` such that `ρ(W) ⊂ W ⊗_k O(G)`, then `V` is
one-dimensional and `ρ(v) = v ⊗ 1` for every `v ∈ V`.

By loc. cit., when `G` is of finite type over `k`, this is equivalent to the definition given in Exp. XVII, § 1, namely
that `G` possesses a finite composition series whose successive quotients are isomorphic to `k`-subgroups of `𝔾_{a,k}`.

Now, for every affine `k`-group scheme `G`, the comultiplication of `O(G)` endows the pseudocompact `k`-module
`A = O(G)*` with a structure of profinite `k`-algebra, not necessarily commutative, the unit element `1_A` being the
augmentation `ε : O(G) → k`. On the other hand, let `I = {f ∈ A | f(1_{O(G)}) = 0}`; this is a two-sided ideal of `A`,
and one has `A = k · 1_A ⊕ I`, cf. 1.3.6.

Let `V` be a subspace of `A` of finite codimension, consider the continuous `k`-bilinear map `ϕ : A × A → A/V`,
`(a, b) ↦ ab + V`; by Lemma 0.3.1, there exist two subspaces `L_1, L_2` of finite codimension in `A` such that `V`
contains `AL_2` and `L_1 A`; then `L = L_1 ∩ L_2` is a subspace of `A` of finite codimension, and `V` contains the
two-sided ideal `ALA`, which is of finite codimension. This shows that the two-sided ideals of finite codimension form a
basis of neighborhoods of `0`. One deduces that an `O(G)`-comodule "is the same thing" as a continuous `A`-module, i.e.,
an `A`-module `V` such that the map `A × V → V` is continuous, `V` being endowed with the discrete topology. Such a
module is evidently the union of submodules `V_i` of finite dimension over `k`, each of which is a module over a
`k`-algebra quotient `A_i` of `A`, of finite dimension over `k`. It follows that if `M` is a simple continuous module,
it is of finite dimension over `k`, and is a faithful simple module over the finite-dimensional `k`-algebra `A/Ann(M)`;
the latter is therefore a finite-dimensional simple `k`-algebra, i.e., `Ann(M)` is a maximal open ideal of `A`.
Conversely, let `P` be an open prime ideal[^N.D.E-VII_B-116] of `A`; then `A/P` is a finite-dimensional `k`-algebra in
which the ideal `(0)` is prime, hence it is a finite-dimensional simple `k`-algebra, so there exists, up to isomorphism,
a unique simple continuous `A`-module whose annihilator is `P`. It follows that the map `M ↦ Ann(M)` defines a bijection
between the isomorphism classes of simple continuous `A`-modules and the open prime ideals of `A`. In particular, the
`A`-module `A/I`, which is one-dimensional over `k`, is called the "trivial module"; it corresponds to the
one-dimensional `O(G)`-comodule `V` which is trivial, i.e., such that `ρ(v) = v ⊗ 1_{O(G)}` for every `v ∈ V`. One thus
obtains the following proposition:

**Proposition 2.8.1.** *Let `k` be a field, `G` an affine `k`-group scheme and `A = O(G)*`.*

*(i) Then `G` is unipotent if and only if `I` is the unique open prime ideal of `A`.*[^N.D.E-VII_B-117]

*(ii) In particular, if `G` is commutative, so that `O(G) = H(D(G))`, where `D(G) = Spf(A)` designates the Cartier dual
of `G`, then `G` is unipotent if and only if `D(G)` is infinitesimal.*

<!-- label: III.VII_B.2.8.1 -->

### 2.9. Pointed cocommutative Hopf algebras over a field.

<!-- label: III.VII_B.2.9 -->

Let `k` be a field, `C` a `k`-coalgebra, `A` the algebra `C*` endowed with the structure of profinite `k`-algebra (not
necessarily commutative) described in 2.8; by 0.2.2, one has `C = A† = Hom_c(A, k)`. One deduces that the map
`D ↦ D⊥ = {f ∈ A | f(D) = 0}` is a bijection from the set of subcoalgebras of `C` onto that of closed two-sided ideals
(in the sequel, one will simply say "ideals") of `A`; the inverse bijection being given by
`I ↦ I⊥ = {x ∈ C = A† | x(I) = 0}`. Since every maximal closed ideal is a maximal open ideal (cf. 0.2.1), every
subcoalgebra therefore contains a simple subcoalgebra, necessarily of finite dimension.

Recall that a subcoalgebra `D` of `C` is called *irreducible* if it contains only one simple subcoalgebra `S_0`, which
is equivalent to saying that `m_0 = S_0⊥` is the unique maximal open ideal containing `D⊥`, i.e., `D⊥ + m = A` for every
maximal open ideal `m ≠ m_0`. This is in particular the case if `D = S_0`. Then the sum `Σ_0` of all the irreducible
subcoalgebras `C_i` containing `S_0` is evidently a subcoalgebra, and it is irreducible because, for every `m ≠ m_0`,
one has, by 0.2.D:

```text
   m + ∩_i C_i⊥ = ∩_i (m + C_i⊥) = A.
```

One says that `Σ_0` is the *irreducible component of `C` corresponding to `C_0`*.

Moreover, one says that `C` is *pointed* if every simple `k`-subcoalgebra of `C` is one-dimensional; this is equivalent
to saying that for every maximal open ideal `m` of `A`, one has `A/m = k`. Recall also that `C` is said to be
*connected* if it is irreducible and pointed. (Let us note in passing that if `C` is a bialgebra, it is connected if and
only if it is irreducible, since `k · 1_C` is a simple subcoalgebra.)

Suppose henceforth that `C` is cocommutative. Then `A` is commutative and is therefore the product of its local
components `A_m`, for `m ∈ Υ(A)` (cf. 0.1.1); denote by `S_m` the simple subcoalgebra `m⊥ ≃ (A/m)*` and by `Σ_m` its
irreducible component. One may describe `Σ_m` as follows. Denote by `J_m` the kernel of the projection `A → A_m`; it is
contained in `m` and is the smallest closed ideal `I` of `m` such that `I + m' = A` for every `m' ≠ m`. Indeed, if `I`
has this property, then `I` contains `A_{m'}` for every `m' ≠ m`, so contains `J_m`. Since `A = J_m ⊕ A_m`, it follows
that `Σ_m = J_m⊥` is identified with `A_m†`. One can now prove the:

**Proposition 2.9.1.** *Let `k` be a field.*

*(i) Let `G` be a `k`-formal group such that all the residue fields of `G` equal `k`. Then `G_e` is the constant
`k`-group `M_k`, where `M = G(k) = {x ∈ H(G) | ε(x) = 1 and ∆(x) = x ⊗ x}`, and `H(G)` is the semi-direct product of
`H(G⁰)` by `kM` (cf. 2.4.B).*

*(ii) Equivalently: let `H` be a cocommutative pointed `k`-Hopf algebra. Then `H` is the semi-direct product of the
irreducible component `H_0` of the unit element `1_H` by `kM`, where `M = {x ∈ H | ε(x) = 1 and ∆(x) = x ⊗ x}`.*

<!-- label: III.VII_B.2.9.1 -->

Let us prove (i). Since all the residue fields of `G` equal `k`, the projection `π : G → G_e` admits the section
`s : G_e → G` defined by `O_{G,g} → κ(g) = k`, for every `g ∈ G`; moreover, for every `g, h ∈ G`, `O_{G,g} ⨶_k O_{G,h}`
is local with residue field `k`, and one therefore obtains that `s × s` is a section of the projection
`π × π : G × G → (G × G)_e = G_e × G_e`. Since `π` is a group morphism, it follows that
`π ∘ m_G ∘ (s × s) = m_{G_e} = π ∘ s ∘ m_{G_e}`, and since `π` is an epimorphism this entails that `s` is a group
morphism. One obtains therefore that `G = G⁰ ⋊ G_e`, and hence `H(G)` is the semi-direct product of `H(G⁰)` by `H(G_e)`.
Moreover, since all the residue fields of `G` equal `k`, then `H(G_e)` is the group algebra `kM`, where `M = G_e(k)`
(cf. 2.5.A). Finally, since `G⁰` is infinitesimal, the morphism `G(k) → G_e(k)` is injective; it is therefore bijective
(since it admits a section), so `M = G(k)`. Point (i) follows.

To prove (ii), it remains only to see that `H_0` equals `H(G⁰)`. Now the unit element `1_H` of `H` is none other than
the augmentation `ε_A : A → k`, which is the unit section of `G(k)`, so the local component of `𝒜(G)` corresponding to
`H_0` is none other than `𝒜(G⁰)` and therefore, by what was seen above, one has `H_0 = 𝒜(G⁰)† = H(G⁰)`. This proves the
proposition.

**Remarks 2.9.2.** *(a) The proposition above, contained implicitly in 2.5.2, has been obtained independently by B.
Kostant (cf. [Sw69], Preface). Combined with Cartier's Theorem 3.3 below (cf. [Ca62], § 12, Th. 3), also obtained by
Kostant (cf. [Sw69], loc. cit.), this result is often called the "Cartier–Gabriel–Kostant theorem".*

*(b) In the form (ii), 2.9.1 has been extended by R. G. Heyneman and M. E. Sweedler to the case where one assumes that
`H` is pointed and a direct sum of its irreducible components (but not necessarily cocommutative), cf. [HS69], Th.
3.5.8.*

<!-- label: III.VII_B.2.9.2 -->

## 3. Phenomena specific to characteristic 0

<!-- label: III.VII_B.3 -->

<!-- original page 531 -->

Throughout Section 3, we assume that the pseudocompact ring `k` contains the field of rational numbers `ℚ`.

### 3.1. Lemma.

<!-- label: III.VII_B.3.1 -->

**Lemma 3.1.** *Let `C` be a commutative unital `ℚ`-algebra, `L` a Lie algebra over `C` whose underlying `C`-module is
free. Then the canonical map `L → U(L)` is an isomorphism of `L` onto the set of primitive elements of `U(L)`.*

<!-- label: III.VII_B.3.1.lem -->

Indeed, let us identify `L` with its canonical image in `U(L)`; let `I` be a totally ordered set and `(x_i)_{i ∈ I}` a
basis of `L` indexed by `I`; let us denote by `ℕ^{(I)}` the set of <!-- original page 569 --> families
`n = (n_i)_{i ∈ I}` of natural integers such that `n_i` is zero except perhaps for a finite number of indices
`i_1 < i_2 < ⋯ < i_s` (these indices depend on `n`); set finally

```text
   x^n = x_{i_1}^{n_{i_1}} x_{i_2}^{n_{i_2}} ⋯ x_{i_s}^{n_{i_s}}    and    n! = (n_{i_1}!)(n_{i_2}!) ⋯ (n_{i_s}!).
```

One knows then that the `x^n` form a basis of `U(L)` (Poincaré–Birkhoff–Witt theorem) and one sees easily that one has

```text
                                  x^n          x^m       x^{n−m}
(∗)              ∆_{U(L)}(─────) = Σ  ─── ⊗ ────────,
                                  n!           m!        (n − m)!
```

the sum being extended over all elements `m` of `ℕ^{(I)}` such that `0 ⩽ m ⩽ n` (i.e., such that `0 ⩽ m_i ⩽ n_i` for
every `i`). It evidently follows that one has `∆_{U(L)}(u) = u ⊗ 1 + 1 ⊗ u` if and only if `u` is a linear combination
of the `x_i`.

### 3.2.

<!-- label: III.VII_B.3.2 -->

Suppose now `C` artinian, of radical `r`. For every `C`-algebra `U` <!-- original page 532 --> (associative, unital),
the ideal `rU` therefore consists of nilpotent elements; if `x` belongs to `rU`, we shall set

```text
                                  x²
   exp_U x = 1 + x + ─── + ⋯
                                  2!
```

[^N.D.E-VII_B-119]

One thus obtains a bijection of `rU` onto `1 + rU`; the inverse bijection sends an element `1 + y` of `1 + rU` to

```text
                                                y²        y³
   log_U(1 + y) = y − ─── + ─── − ⋯
                                                 2          3
```

Moreover, it is clear that the map `exp_U` is functorial in `U`.[^N.D.E-VII_B-120]

The ring `C` still being artinian, suppose `U` endowed with a structure of bialgebra over `C` (cf. 2.2). For every
primitive element `x` of `rU` (cf. VII_A 3.2.3), one has then

```text
   ∆_U(exp_U x) = exp_{U⊗U}(∆_U(x))
                 = exp_{U⊗U}(x ⊗ 1 + 1 ⊗ x)
                 = exp_{U⊗U}(x ⊗ 1) · exp_{U⊗U}(1 ⊗ x)
                 = ((exp_U x) ⊗ 1) · (1 ⊗ (exp_U x))
                 = (exp_U x) ⊗ (exp_U x).
```

One thus sees that the bijection `exp_U` transforms a primitive element of `rU` into an element `z` of `1 + rU` such
that `∆_U(z) = z ⊗ z`. Conversely, if `z` satisfies these conditions then, setting `x = log_U(z)`, the preceding
computation shows that `exp_{U⊗U}(x ⊗ 1 + 1 ⊗ x)` equals `z ⊗ z = ∆(exp_U x) = exp_{U⊗U}(∆_U(x))`, whence
`x ⊗ 1 + 1 ⊗ x = ∆_U(x)`.[^N.D.E-VII_B-121] Let us moreover note that if `z ∈ 1 + rU` satisfies `∆_U(z) = z ⊗ z`, then
`ε_U(z)² = ε_U(z)`, and since `ε_U(z)` is invertible (since `z` is, `r` being nilpotent), it follows that `ε_U(z) = 1`.

Consider in particular a Lie algebra `L` flat over `C`, take for `U` the enveloping algebra `U(L)` of `L` over `C`, and
identify `L` with its canonical image in `U`. By Lemma 3.1, `L` is therefore the set of primitive elements of `U`
(indeed `L` is a product of free modules over the local components of `C`). Consider then <!-- original page 533 --> the
`C`-formal group `𝒢(L) = Spf* U(L)`, which has `U = U(L)` as covariant bialgebra (cf. 2.6.2). Let `m` be a maximal ideal
of `C` and `C̄ = C/m`. Since `𝒢(L)` is infinitesimal (loc. cit.), the unit element of `Ū = U ⊗_C C̄` is the only element
`z` of `Ū` such that[^N.D.E-VII_B-122] `ε_Ū(z) = 1` and `∆_Ū(z) = z ⊗ z`. It follows that the elements `z` of `U` such
that `ε_U(z) = 1` and `∆_U(z) = z ⊗ z` necessarily belong to `1 + rU`.

Finally, since `L ∩ rU` is identified with `rL = L ⊗_C r`, one sees finally that: `exp_U` defines a bijection of
`L ⊗_C r` onto the group `𝒢(L)(C)`. We summarize:

**Proposition 3.2.** *Let `k` be a pseudocompact ring containing `ℚ` and `L` a flat `O_k`-Lie algebra.*

*(i) For every object `C` of `Alf_/k`, denote by `r(C)` its radical; then the map*

```text
   exp_{U(L(C))} :    L(C) ⊗_C r(C) ─→ 𝒢(L)(C)
```

*is bijective and functorial in `C` and `L`.*

*(ii) The natural morphism `L → Lie(𝒢(L))` (cf. 2.6.2) is an isomorphism of `O_k`-Lie algebras.*[^N.D.E-VII_B-123]

<!-- label: III.VII_B.3.2.prop -->

#### 3.2.1.

<!-- label: III.VII_B.3.2.1 -->

The bijection `exp_{U(L(C))}` permits one to define by transport of structure a group law on the set `L(C) ⊗_C r(C)`
(which one identifies with a part of `U(L(C))` as in 3.2). If `x` and `y` are two elements of `L(C) ⊗_C r(C)`, this law
is such that

```text
                                                            x^p y^q
   x · y = log((exp x)(exp y)) = log(1 + Σ_{p+q > 0} ─────────)
                                                            p! q!
                                                                                                       
                                  (−1)^{m−1}  x^{p_1} y^{q_1}    x^{p_m} y^{q_m}    
            = Σ_{m ⩾ 1} Σ_{p_i + q_i > 0} ──────── ───────────── ⋯ ────────────────  = Σ_{ℓ ⩾ 1} P_ℓ(x, y)
                                  m              p_1! q_1!              p_m! q_m!     
```

<!-- original page 534 -->

where `P_ℓ(x, y)` designates the sum of the monomials of total degree `ℓ` in `x` and `y`. One has for example:

```text
   P_1(x, y) = x + y

                x²              y²    1
   P_2(x, y) = ─── + xy + ─── − ─── (x² + xy + yx + y²)
                2               2     2
                                                                              1                  1
                  (terms with m=1)              (terms with m=2)            = ─── (xy − yx) = ─── [x, y]
                                                                              2                  2
```

and `P_3(x, y)` is the sum of the three terms below:

```text
   x³   x²y   xy²   y³    1                              1
   ─── + ──── + ──── + ─── − ─── (x³ + x²y + yx² + xyx + yxy + y²x + xy² + y³)
    6    2     2      6     2                              2
                              (m=1)                                (m=2)

                                            1
                                        + ─── (x³ + x²y + yx² + xyx + yxy + y²x + xy² + y³)
                                            3
                                                                  (m=3)
```

whence

```text
                  1                                         1
   P_3(x, y) = ──── (x²y + yx² − 2 xyx − 2 yxy + y²x + xy²) = ──── ([y, x], x] + [y, [y, x]]).
                12                                          12
```

One can show more generally that one has the Campbell–Hausdorff formula:[^N.D.E-VII_B-124]

```text
              ℓ                                        m−1
              Σ  (−1)^{m−1}                          ┌──┐ (ad x)^{p_i} (ad y)^{q_i}      (ad x)^{p_m}
   P_ℓ(x,y)= ─── ─────────── Σ_{p_1,…,p_m, q_1,…,q_{m−1}} │  │  ───────────────────────── · ──────────── (y)
              m=1   m · ℓ                            └──┘       p_i!   q_i!                p_m!
                                                     i=1
              ℓ                                        m−1
              Σ  (−1)^{m−1}                          ┌──┐ (ad x)^{p_i} (ad y)^{q_i}
            +  ─── ─────────── Σ_{p_1,…,p_{m−1}, q_1,…,q_{m−1}} │  │  ───────────────────────── (x)
              m=1   m · ℓ                            └──┘       p_i!   q_i!
                                                     i=1
```

where the `p_j, q_i ∈ ℕ` verify `p_i + q_i ⩾ 1` for `i = 1, …, m − 1` and `p_m + Σ_{i=1}^{m−1}(p_i + q_i) = ℓ − 1`
(i.e., in the sums above, each non-zero "Lie monomial" is of total degree `ℓ`); for a proof, see N. Jacobson, *Lie
Algebras* (Interscience, 1962), § V.5, or [BLie], II § 6.4, Th. 2.

### 3.3.

<!-- label: III.VII_B.3.3 -->

If `G` is a `k`-formal group of affine algebra `A`, recall that one denotes by `I_A` the augmentation ideal of `A` and
by `ω_{G/k}` the pseudocompact `k`-module `I_A / I_A² ≃ I_A ⨶_A k`.

**Theorem 3.3 (Cartier).** *Let `k` be a pseudocompact ring[^N.D.E-VII_B-125] containing `ℚ` and `G` a
    <!-- original page 535 --> `k`-formal group. The following assertions are equivalent:*

*(i) There exists a flat `O_k`-Lie algebra `L` such that `G` is isomorphic to `𝒢(L)` (and in this case `L = Lie(G)` by
3.2).*

*(ii) There exists a projective pseudocompact `k`-module `ω` such that the formal variety underlying `G` is isomorphic
to the formal variety `V_k^{f,0}(ω)` (cf. 1.2.5) of affine algebra `k[[ω]]` (and in this case `ω ≃ ω_{G/k}`).*

*(iii) `G` is infinitesimal and `ω_{G/k}` is a projective pseudocompact `k`-module.*

*(iv) `G` is infinitesimal and topologically flat over `k`.*

<!-- label: III.VII_B.3.3.thm -->

*(i) ⇒ (ii):* Let `ω = Γ*(L)` be the pseudocompact `k`-module dual to `L` (cf. 1.2.3.D). For every object `C` of
`Alf_/k`, we must exhibit an isomorphism from `V_k^{f,0}(ω)(C)` onto `𝒢(L)(C)` which is functorial in `C`. By 1.2.5,
`V_k^{f,0}(ω)(C)` is identified with the set `Hom_c(ω, r(C))` of continuous `k`-linear maps from `ω` into the radical of
`C`. This set is naturally isomorphic to the set `Hom_c(ω ⨶_k C, r(C))` of continuous `C`-linear maps from `ω ⨶_k C`
into `r(C)`; finally, since `ω ⨶_k C` is a projective pseudocompact `C`-module, the canonical map

```text
   (ω ⨶_k C)† ⊗_C r(C) ─→ Hom_c(ω ⨶_k C, r(C))
```

is bijective (cf. 0.3.6.A). Since, by 1.2.3.E, `L(C)` is identified with `V_kf(Γ*(L))(C) = (ω ⨶_k C)†`, one obtains that
`V_k^{f,0}(ω)(C)` is canonically isomorphic to `L(C) ⊗_C r(C)`, which is canonically isomorphic to `𝒢(L)(C)` by
Proposition 3.2. This proves <!-- original page 536 --> implication (i) ⇒ (ii).

*(ii) ⇒ (iii):* Let `ω` be a projective object of `PC(k)` and `h` an isomorphism from `k[[ω]]` onto the affine algebra
`A` of `G`. Composing `h` with the augmentation `ε_A : A → k`, one obtains a homomorphism `ε_A ∘ h : k[[ω]] → k`, which
is determined by its restriction `λ` to `ω`; the latter sends `ω` into the radical `r` of `k`. Therefore, the map
`x ↦ x − λ(x)`, from `ω` into the radical of `k[[ω]]`, extends by the universal property of `k[[ω]]` (cf. 1.2.5) to an
endomorphism `ℓ_λ` of `k[[ω]]`. The equalities `ℓ_λ ∘ ℓ_{−λ} = ℓ_{−λ} ∘ ℓ_λ = id` show that `ℓ_λ` is an automorphism of
`k[[ω]]`. Consequently, `h ∘ ℓ_λ` is, like `h`, an isomorphism from `k[[ω]]` onto `A`, and moreover `ε_A ∘ h ∘ ℓ_λ`
sends `ω` to `0`. Replacing `h` by `h ∘ ℓ_λ` if necessary, one may therefore suppose that `ε_A ∘ h` vanishes on the
closed ideal `I` of `k[[ω]]` generated by `ω`. In this case, `h` induces an isomorphism from `I/I²` onto `I_A/I_A²`;
since `I/I² ≃ ω`, it follows that `ω_{G/k} = I_A/I_A²` is isomorphic to `ω`, hence projective. It is clear on the other
hand that `V_k^{f,0}(ω)` is infinitesimal, as is `G`.

*(iii) ⇒ (i):* Suppose that `G` is infinitesimal and that `ω_{G/k}` is projective. Let `L` be the `O_k`-Lie algebra of
`G`; the underlying `O_k`-module is `V_kf(ω_{G/k})`, by 2.6.1. Consequently, `L` is flat over `O_k`, and
`Γ*(L) ≃ ω_{G/k}`, by Proposition 1.2.3.E. Hence, by the proof of (i) ⇒ (ii), the affine algebra of the `k`-formal group
`𝒢(L)` is identified with `k[[ω_{G/k}]]`. On the other hand, by 2.6.3, the identity morphism of `L` is canonically
associated with a morphism of formal groups `𝒢(L) → G`, hence with a continuous morphism of `k`-algebras

```text
   φ : A ─→ k[[ω_{G/k}]].
```

Let `I` be the closed ideal of `k[[ω_{G/k}]]` generated by `ω_{G/k}`; let us filter `k[[ω_{G/k}]]` (resp. `A`) by the
closures of the ideals `I^n` (resp. `I_A^n`). We have to show that `φ`, which by definition induces the identity on
`ω_{G/k} = I_A/I_A² = I/I²`, is an isomorphism.

<!-- original page 537 -->

Since `ω_{G/k}` is a projective object of `PC(k)`, there exists a section `τ` of the canonical projection
`I_A → ω_{G/k}`. By the universal property of `k[[ω_{G/k}]]` (cf. 1.2.5), `τ` defines a continuous morphism of algebras

```text
   ψ : k[[ω_{G/k}]] ─→ A
```

and `φ ∘ ψ` induces the identity map on `ω_{G/k}`, hence also on the associated graded of `k[[ω_{G/k}]]`. It follows
that `φ ∘ ψ` is an isomorphism, by [CA], § V.7, Lemma 1.[^N.D.E-VII_B-126]

Moreover, `ψ` induces an isomorphism from `I/I²` onto `I_A/I_A²`, hence a surjection of the associated gradeds of
`k[[ω_{G/k}]]` and `A`. On the other hand, since `G` is radicial, `I_A` is contained in the radical of `A`, so that the
intersection of the `I_A^n` is zero. Therefore, by loc. cit., `ψ` is surjective. Then, since `φ ∘ ψ` is an isomorphism
and `ψ` a surjection, `ψ` and `φ` are isomorphisms. This proves (iii) ⇒ (i).

Let us note finally that it is clear that (i) or (ii) entail (iv), so that it remains to prove the implication (iv) ⇒
(ii). For this, one may suppose `k` local, with residue field `k_0`. Set then `G_0 = G ⨶_k k_0`, `ω = ω_{G/k}`,
`ω_0 = ω ⨶_k k_0`, etc.[^N.D.E-VII_B-127] Since `k_0` is a field, the pseudocompact `k_0`-module `ω_0` has a pseudobasis
`(y_λ)_{λ ∈ Λ}`; denoting `ω'` the topologically free `k`-module product of copies `k_λ` of `k`, for `λ ∈ Λ`, and
lifting each `y_λ` to an element `x_λ` of `ω`, one obtains a continuous `k`-linear map `f : ω' → ω` such that
`f_0 = f ⨶_k k_0` is invertible.[^N.D.E-VII_B-128] Since `ω'` is a projective pseudocompact `k`-module, `f` lifts to a
continuous `k`-linear map `g : ω' → I_A` such that `π ∘ g = f`, where `π` is the projection `I_A → ω`. By the universal
property of `k[[ω']]` (cf. 1.2.5), `g` induces a morphism of topological algebras `φ : k[[ω']] → A`.

<!-- original page 538 -->

Now `ω' ⨶_k k_0` is identified with `ω ⨶_k k_0 = ω_{G_0/k_0}` and hence `k[[ω']] ⨶_k k_0` is identified with
`k_0[[ω_{G_0/k_0}]]`. Since hypotheses (iii) are satisfied for `k_0` and `G_0`, the proof of (iii) ⇒ (i) shows that
`φ_0 = φ ⨶_k k_0` is invertible. Since, on the other hand, `k[[ω']]` and `A` are projective pseudocompact `k`-modules,
`φ` is invertible by 0.3.4. (In particular, denoting `I` the augmentation ideal of `k[[ω']]`, `φ` induces an isomorphism
from `ω' = I/I²` onto `I_A/I_A² = ω`.)

#### 3.3.1.

<!-- label: III.VII_B.3.3.1 -->

**Corollary 3.3.1.** *Let `S` be a locally noetherian scheme over `ℚ` and `G` an `S`-group scheme that is flat and
locally of finite type.[^N.D.E-VII_B-C-11] If `ω_{G/S}` is a locally free `O_S`-module, `G` is smooth over `S` at every
point of the unit section.*

<!-- label: III.VII_B.3.3.1 -->

Indeed, let `x` be a point of the unit section, `s` its image in `S`, `O_x` and `O_s` the local algebras of `x` and
`s`.[^N.D.E-VII_B-C-12] Since, by hypothesis, `O_s` and `O_x` are noetherian local rings, the `𝔪`-adic topology on each
of these rings coincides with the "pseudocompact" topology defined by the ideals of finite codimension. Denote then by
`Ô_x` and `Ô_s` the completions for this topology. By (EGA IV₄, 17.5.3), `G` is smooth over `S` at the point `x` if and
only if `Ô_x` is formally smooth over `Ô_s`, these two algebras being endowed with the `𝔪`-adic topology; it therefore
suffices to show this latter property. Now `Ô_x` and `Ô_s` are the local rings of `x` and `s` in the formal varieties
`Ĝ/Ŝ` and `Ŝ` defined in 1.2.6. Set `k = Ô_s` and `H = Spf(Ô_x)`; then `H` is a `k`-formal variety that is infinitesimal
and, since the formation of `Ĝ/Ŝ` commutes with products (loc. cit.), `H` is an infinitesimal `k`-formal group. Denote
by `I` the augmentation ideal of `O_x`. By hypothesis, `ω_{G/S, x} = I/I²` is a locally free `O_s`-module of finite rank
`n`. Since `O_s` is noetherian, it follows that `ω_{H/k}`, which is the completion of `ω_{G/S, x}`, is identified with
`ω_{G/S} ⊗_{O_S} Ô_s`, hence is a topologically free `k`-module of rank `n`. Hence, by the implication (iv) ⇒ (ii) of
3.3, `Ô_x` is isomorphic to `k[[ω_{H/k}]]`, i.e., to a formal power series algebra `k[[t₁, …, t_n]]`. Finally, this last
is formally smooth over `k`, by (EGA 0_IV, 19.3.3). This proves the corollary.

We thus recover a result obtained otherwise for group schemes locally of finite presentation over an arbitrary scheme
`S`, cf. VI_B, 1.6.

#### 3.3.2.

<!-- label: III.VII_B.3.3.2 -->

<!-- original page 574 -->

**Corollary 3.3.2.** *Let `k` be a field of characteristic 0. The functor `L ↦ **G**(L)` is an equivalence from the
category of `k`-Lie algebras onto that of infinitesimal `k`-formal groups.*[^N.D.E-VII_B-C-13]

<!-- label: III.VII_B.3.3.2 -->

<!-- original page 574, marginal 539 -->

Indeed, when `G` runs through the infinitesimal `k`-formal groups, the functor `G ↦ **G**(Lie G)` is isomorphic, by
Theorem 3.3, to the identity functor of the category of infinitesimal `k`-groups. Likewise, by 3.2 (ii), the functor
`L ↦ Lie(**G**(L)) = Prim(U(L))` is isomorphic to the identity functor of the category of `k`-Lie algebras.

#### 3.3.3.

<!-- label: III.VII_B.3.3.3 -->

Suppose still that `k` is a field of characteristic 0. Let `k̄` be an algebraic closure of `k` and `Γ` the topological
Galois group of `k̄` over `k`.

For every `k`-formal group `G`, we denote by `**Aut**_k(G)` the `k`-group functor that associates to every commutative
`k`-algebra `C` of finite dimension the group of automorphisms of the `C`-formal group `G ⊗̂_k C`.[^N.D.E-VII_B-C-14]
Since `G` is topologically flat over `k` (since `k` is a field), i.e., its affine algebra `A = **A**(G)` is
topologically flat over `k`, or, equivalently, its covariant bialgebra `H = **H**(G)` is flat over `k`, this `k`-functor
is a `k`-formal group. Indeed, since `**Aut**_k(G)` is identified with the fibered product of the following diagram (cf.
Exp. I, 1.7.3):

```text
                                  **End**_k(G) × **End**_k(G)
                                           ↓
Spf(k)  ⟶  **End**_k(G) × **End**_k(G)
```

where the vertical (resp. horizontal) arrow is given by `(φ, ψ) ↦ (φ ∘ ψ, ψ ∘ φ)` (resp. is the unit section), it
suffices to check that the `k`-functor `**End**_k(G)` is represented by an element of `Vaf/k`, that is (cf. 1.1 and
0.4.2), that it is left exact, i.e., commutes with fibered products of `k`-algebras. Now to give an element of
`**End**_k(G)(C)` is equivalent to giving, say, a morphism of `k`-algebras `φ : H → H ⊗_k C` that also respects the
coalgebra structure, i.e., such that the well-known diagrams are commutative; since `H` is flat over `k`, the functor
`H ⊗_k −` commutes with fibered products of `k`-algebras, and one deduces that the `k`-functor `**End**_k(G)` is left
exact, so we can treat it as a `k`-formal group.

<!-- original page 575 -->

If `L` is a `k`-Lie algebra and `G` the formal group `**G**(L)`, Theorem 3.3 shows that `**Aut**_k(G)` is isomorphic to
the `k`-group functor `**Aut**_k(L)` which associates to a finite-dimensional `k`-algebra `C` the group of automorphisms
of the `C`-Lie algebra `C ⊗_k L`.

If `G` is an arbitrary `k`-formal group, we saw in 2.5.2 that `G` decomposes canonically into a semi-direct product of
an étale formal group `G_e` and an infinitesimal formal group `G^0`. This semi-direct product is determined by the data
of `L = Lie(G) = Lie(G^0)`, of the `Γ`-group `M = G_e(k̄) = G(k̄)`, and of a morphism of `k`-formal groups

```text
Φ : G_e ⟶ **Aut**_k(G^0) ≃ **Aut**_k(L).
```

Such a morphism sends `G_e` into the "étale part" `**Aut**_k(L)_e` of `**Aut**_k(L)`, cf. 2.5.1. It is therefore
determined by the data of a morphism of `Γ`-groups:

```text
φ = Φ(k̄) :    M ⟶ (**Aut**_k L)(k̄) = **Aut**_{k̄}(L ⊗_k k̄).
```

<!-- original page 575, marginal 540 -->

If we let `Γ` act on `L ⊗_k k̄` by the formula `γ(ℓ ⊗ t) = ℓ ⊗ γ(t)`, then `φ` makes `M` act on `L ⊗_k k̄` by
automorphisms of `k̄`-Lie algebra in such a way that one has `φ(γ(m)) = γ ∘ φ(m) ∘ γ^{−1}`, i.e.:

```text
γ(m)(ℓ ⊗ t) = γ(m(ℓ ⊗ γ^{−1}(t)))
```

for every `m ∈ M`, `γ ∈ Γ` and `ℓ ⊗ t ∈ L ⊗_k k̄`. We express this last condition by saying that `M` acts on `L ⊗_k k̄`
*compatibly with `Γ`*.

One can summarize the situation by means of a "highbrow" statement: let us call *`Γ`-Lie algebra over `k`* the data of a
triple `(L, M, φ)` formed by a `k`-Lie algebra `L`, a `Γ`-group `M`, and an action `φ` of `M` on `L ⊗_k k̄` that is
"compatible with the action of `Γ` on `M` and on `L ⊗_k k̄`".

If `(L, M, φ)` and `(L′, M′, φ′)` are two such `Γ`-Lie algebras, a morphism of the first into the second is a pair
`(f, θ)` formed by a morphism `f : L → L′` of `k`-Lie algebras and a morphism `θ : M → M′` of `Γ`-groups such that

```text
(f ⊗ 1)(m · x) = θ(m) · (f ⊗ 1)(x)
```

for every `x ∈ L ⊗_k k̄` and `m ∈ M`. One then obtains:

**Theorem.** *Let `k` be a field of characteristic 0. Then the functor that associates to `G` the triple
`(Lie(G), G(k̄), Φ(k̄))` is an equivalence of the category of `k`-formal groups onto that of `Γ`-Lie
algebras.*[^N.D.E-VII_B-C-15]

## 4. Phenomena specific to characteristic `p > 0`

<!-- label: III.VII_B.4 -->

<!-- original page 575, marginal 541 -->

Throughout Section 4, we denote by `p` a prime number, by `k` a pseudocompact ring of characteristic `p`, and by `π` the
continuous endomorphism `x ↦ x^p` of `k`.

### 4.1.

<!-- label: III.VII_B.4.1 -->

<!-- original page 576 -->

Let `X` be a `k`-formal variety with affine algebra `A`; one denotes by `X^{(p/k)}` or `X^{(p)}` the `k`-formal variety
`X ⊗̂_π k` obtained by the base change `π : k → k` (cf. 1.2.D); it has as affine algebra the completed tensor product
`A ⊗̂_π k`. Then, the continuous morphism `A ⊗̂_π k → A` which sends `a ⊗̂_π λ` onto `a^p λ` induces a morphism of
`k`-formal varieties

```text
Fr(X/k) : X ⟶ X^{(p/k)}.
```

In what follows, we shall say that `Fr(X/k)` is the *Frobenius morphism of `X` relative to `k`* and we shall often write
`Fr` instead of `Fr(X/k)`.

#### 4.1.1.

<!-- label: III.VII_B.4.1.1 -->

[^N.D.E-VII_B-C-16] Consider now a scheme `S` over the prime field `𝔽_p` and an `S`-scheme `η : X → S`; let `fr(S)` be
the "absolute" Frobenius morphism of `S` (it induces the identity on the underlying topological space and sends every
section `f` of the structure sheaf onto `f^p`; cf. VII_A 4.1) and let `X^{(p)}` be the `S`-scheme `X ×_{fr(S)} S`
(VII_A, loc. cit.), i.e., the structure morphism `X^{(p)} → S` is `fr(S) ∘ η`.

Let `Ŝ` be the formal scheme whose underlying topological space is the set of closed points of `S`, endowed with the
discrete topology, the local ring `Ô_{S, s}` at such a closed point `s` being the separated completion `Ô_{S, s}` of
`O_{S, s}` for the linear topology defined by the ideals of finite colength (cf. 1.2.6); its affine algebra
`k = **A**(Ŝ)` is therefore the product of the `Ô_{S, s}`, as `s` runs through the closed points of `S`. Recall (loc.
cit.) that one denotes by `X̂/Ŝ` the `k`-formal variety formed by the points `x ∈ X` such that `[κ(x) : κ(s)] < ∞`,
where `s` is the image of `x` in `S`, the local ring `O_{X̂/Ŝ, x}` being the separated completion `Ô_{X, x}` of
`O_{X, x}` for the linear topology defined by the ideals `I` such that `O_{X, x}/I` is of finite length as
`O_{X, x}`-module (and therefore also as `O_{S, s}`-module). One can therefore form, by base change, the `k`-formal
variety `(X̂/Ŝ)^{(p)} = (X̂/Ŝ) ⊗̂_π k`.

One can also consider the `k`-formal variety `X̂^{(p)}/Ŝ`: the underlying set is formed by the `x ∈ X^{(p)} = X` such
that, denoting by `s` the image of `x` in `S`, the morphism

```text
κ(s) ─fr→ κ(s) ─η^♯→ κ(x)
```

makes `κ(x)` an extension of finite degree of `κ(s)`; in this case, the same holds for `η^♯ : κ(s) → κ(x)`, i.e., `x` is
a point of `X̂/Ŝ`, and one then has

```text
O_{X̂^{(p)}/Ŝ, x} = Ô_{X, x} ⊗̂_π Ô_{S, s} = Ô_{X^{(p)}, x}
```

<!-- original page 576, marginal 542 -->

(the second equality since `X ↦ X̂/Ŝ` commutes with products, cf. 1.2.6). One therefore sees that: `X̂^{(p)}/Ŝ` is
identified with a formal subvariety of `(X̂/Ŝ)^{(p)}`. Moreover, equality holds if and only if for every closed point
`s` of `S`, `κ(s)` is of finite degree over `κ(s)^p`, which is the case for example if `S` is a scheme locally of finite
type over a field `κ` such that `[κ : κ^p] < +∞`.

#### 4.1.2.

<!-- label: III.VII_B.4.1.2 -->

<!-- original page 577 -->

Let `G` be a `k`-formal group. Since the functor `X ↦ X^{(p)} = X ⊗̂_π k` commutes with finite products, it transforms a
`k`-formal group into a `k`-formal group. Moreover, since `Fr(X/k)` is functorial in `X`, the morphism

```text
Fr : G ⟶ G^{(p)}
```

is a homomorphism of `k`-formal groups. If one sets `G^{(p^{n+1})} = (G^{(p^n)})^{(p)}`, the same holds for the
composite morphism

```text
Fr^n = Fr^n(G/k) :   G ─Fr→ G^{(p)} ─Fr→ G^{(p²)} ─Fr→ ⋯ ─Fr→ G^{(p^n)}.
```

Denote by `A` the affine algebra of `G` and by `I_A` its augmentation ideal.

**Definitions.** *(a) The kernel of `Fr^n` will be denoted `Fr_n G`. It follows directly from the definitions that
`Fr_n G` is infinitesimal and has as affine algebra the quotient `A / I_A^{\{p^n\}}`, where `I_A^{\{p^n\}}` denotes the
closed ideal of `A` generated by the `p^n`-th powers of the elements of `I_A`.*

*(b) One says that `G` is of height `⩽ n` if `I_A^{\{p^n\}} = 0`, that is to say if one has `Fr_n G = G`.*

### 4.2.

<!-- label: III.VII_B.4.2 -->

<!-- original page 577, marginal 543 -->

It is clear that the Lie algebra `Lie(G)` of a `k`-formal group `G` is a `p`-Lie subalgebra of the algebra `**H**(G)`
(cf. 2.3). Indeed, one reduces immediately to the case where `k` is artinian; in this case, `Lie(G)` is the part of
`**H**(G)` formed by the elements `x` such that `φ_G(x ⊗ 1 + 1 ⊗ x) = Δ_G(x)` with the notations of 2.3 and 2.6 (c). One
then has

```text
φ_G(x^p ⊗ 1 + 1 ⊗ x^p) = φ_G((x ⊗ 1 + 1 ⊗ x))^p
                       = (φ_G(x ⊗ 1 + 1 ⊗ x))^p = Δ_G(x)^p = Δ_G(x^p).
```

#### 4.2.1.

<!-- label: III.VII_B.4.2.1 -->

Conversely, every `p`-Lie algebra `L` over `O_k` defines a `k`-group functor. Denote indeed by `U_p(L)` the functor that
associates to every object `C` of `Alf/k` the restricted enveloping algebra `U_p(L(C))` of the `p`-Lie algebra `L(C)`
over `C` (VII_A 5.3). By VII_A 5.4, `U_p(L)` is an `O_k`-bialgebra and therefore determines, by 2.2, a `k`-group functor
`Spf^*(U_p(L))` that we shall henceforth denote `**G**_p(L)`.

Thus, `**G**_p(L)(C)` is the group of elements `z ∈ U_p(L(C))` of augmentation `1` and such that
`Δ_{U_p(L(C))}(z) = z ⊗ z`.

#### 4.2.2.

<!-- label: III.VII_B.4.2.2 -->

Suppose `L` is a `p`-Lie algebra that is flat over `O_k`. Then, taking account of VII_A 5.3.3, one shows as in point (i)
of Proposition 2.6.2 that `U_p(L)` is flat over `O_k`; hence `**G**_p(L)` is a topologically flat `k`-formal group which
has `U_p(L)` as covariant `O_k`-bialgebra.

[^N.D.E-VII_B-C-17] By the proof of 2.6.2 (iii), for every `k`-algebra `C` of finite length, `Lie(**G**_p(L))(C)` is the
set of primitive elements of `U_p(L)(C) = U_p(L(C))` (see also VII_A 3.2.3); moreover, by VII_A 5.5.3, the canonical
morphism `L → U_p(L)` induces an isomorphism of `p`-Lie algebras

```text
τ_{p, L} : L ⥲ Lie(**G**_p(L))
```

(compare with 3.1 in characteristic 0).

The formal group `**G**_p(L)` can be characterized by a universal property. Indeed, every morphism `h` of `**G**_p(L)`
into a formal group `G` induces a morphism `Lie(h) : Lie(**G**_p(L)) → Lie(G)`. Composing this with the isomorphism
`τ_{p, L}`, one obtains a morphism `h′ : L → Lie(G)`.

<!-- original page 577, marginal 544 -->

**Proposition.** *If `k` is a pseudocompact ring of characteristic `p > 0`, `G` a `k`-formal group, and `L` a `p`-Lie
algebra that is flat over `O_k`, the map `h ↦ h′` defined above is a bijection*

```text
Hom_{Grf/k}(**G**_p(L), G) ⥲ Hom_{p-Lie}(L, Lie(G))
```

*where the right-hand term denotes the set of morphisms of `p`-Lie algebras from `L` into `Lie(G)`.*

[^N.D.E-VII_B-C-18] One reduces indeed immediately to the case where `k` is artinian. Set `L = L(k)`. By 2.3.1,
`Hom_{Grf/k}(**G**_p(L), G)` is in bijection with the set of morphisms of unitary algebras `h : U_p(L) → **H**(G)` such
that the following diagram is commutative:

```text
U_p(L) ────h──── **H**(G) ────δ_G──── **H**(G × G)
   │                                       ↑
Δ_{U_p(L)}                                 φ_G
   ↓                                       │
U_p(L) ⊗ U_p(L) ────h⊗h──── **H**(G) ⊗ **H**(G)
```

Now `h` is determined by its restriction to `L`, which is a morphism of `p`-Lie algebras from `L` into the `p`-Lie
algebra underlying `**H**(G)`, and the commutativity of the diagram means that `h` sends `L` into the part of `**H**(G)`
formed by the `x` such that `δ_G(x) = φ_G(x ⊗ 1 + 1 ⊗ x)`, which is none other than `Lie(G)`, cf. 2.6 (c).

### 4.3.

<!-- label: III.VII_B.4.3 -->

We now propose to study in greater detail the `k`-formal group `**G**_p(L)` when `L` is a `p`-Lie algebra that is flat
over `O_k`.

<!-- original page 577, marginal 545 -->

For this, we first consider a ring `C` of characteristic `p` and a `p`-Lie algebra `L` over `C` whose underlying module
is free with basis `(x_i)_{i ∈ I}`. Denote moreover by `P` the set of families `n = (n_i)_{i ∈ I}` of natural integers
such that `0 ⩽ n_i < p` and that the `n_i` are zero except possibly a finite number of them. If we endow `I` with a
total order and if we call `i₁, i₂, …, i_r` (`i₁ < i₂ < ⋯ < i_r`) the indices `i` such that `n_i ≠ 0`, we can therefore
set `|n| = n_{i₁} + ⋯ + n_{i_r}` and

```text
x^n = x_{i₁}^{n_{i₁}} · x_{i₂}^{n_{i₂}} ⋯ x_{i_r}^{n_{i_r}},    n! = (n_{i₁}!) ⋯ (n_{i_r}!).
```

It is known that the monomials `x^n/n!` form a basis of `U_p(L)` (VII_A 5.3.3) and it is clear that one has

```text
(∗)    Δ(x^n/n!) = ∑_{m ⩽ n} (x^m/m!) ⊗ (x^{n−m}/(n − m)!)
```

<!-- original page 578 -->

the sum being extended to all `m ∈ P` such that `m ⩽ n` (i.e., `m_i ⩽ n_i` for all `i ∈ I`).

Formula `(∗)` allows an easy determination of the natural filtration of `U_p(L)` (cf. 1.3.6). Set `U = U_p(L)`, let
`U^+` be the two-sided ideal generated by `L`, and let `U_0 = C · 1_U`. As in 1.3.6, one defines a filtration of `U` (by
`C`-subcoalgebras) by setting, for `n ⩾ 1`:

```text
U_n = {u ∈ U | Δ_U(u) − u ⊗ 1 ∈ U_{n−1} ⊗ U^+}.
```

Formula `(∗)` then entails that `U_n` is the free `C`-module having as basis the monomials `x^m` such that `|m| ⩽ n`.

#### 4.3.1.

<!-- label: III.VII_B.4.3.1 -->

<!-- original page 578, marginal 546 -->

With the notations of 4.3, let us determine the elements `ξ` of `U = U_p(L)` such that `ε_U(ξ) = 1` and
`Δ_U(ξ) = ξ ⊗ ξ`. Every element `ξ` of `U` is written `ξ = ∑_{n ∈ P} ξ_n (x^n/n!)`, with `ξ_n ∈ C`. The condition
`ε_U(ξ) = 1` entails the equality `ξ_0 = 1`, where `0` denotes the element of `P` all of whose components are zero. The
condition `Δ_{U_p(L)}(ξ) = ξ ⊗ ξ` entails:

```text
∑_{m ⩽ n} ξ_n (x^m/m!) ⊗ (x^{n−m}/(n − m)!) = ∑_{q, r} ξ_q ξ_r (x^q/q!) ⊗ (x^r/r!)
```

that is to say,

```text
ξ_{q+r} = ξ_q ξ_r    if q_i + r_i < p,    and    ξ_q ξ_r = 0    otherwise.
```

If one denotes by `ξ_i` the value of `ξ_n` when `n_i = 1` and `n_j = 0` for `j ≠ i`, these conditions mean that one has

```text
ξ_n = ∏_i ξ_i^{n_i}    if n ∈ P,    and    ξ_i^p = 0    ∀ i ∈ I.
```

One deduces from this:

**Proposition.** *Let `k` be a local pseudocompact ring[^N.D.E-VII_B-C-19] of characteristic `p > 0`, `L` a `p`-Lie
algebra that is flat over `O_k`, `C` an object of `Alf/k`, and `^p√0_C` the ideal of `C` formed by the elements `x` such
that `x^p = 0`. There exists a bijection "functorial in `C`":*

```text
L(C) ⊗_C ^p√0_C ⥲ **G**_p(L)(C).
```

<!-- label: III.VII_B.4.3.1 -->

<!-- original page 578, marginal 547 -->

By Remark 1.2.3.F, one can indeed choose a basis `(^C x_i)_{i ∈ I}` of `L(C)` over `C` in such a way that, for every
morphism `φ : C → D` of `Alf/k`, `L(φ)` sends `^C x_i` onto `^D x_i`. By what precedes, the map

```text
∑_i (^C x_i) ⊗ ξ_i ↦ ∑_{n ∈ P} (∏_i ξ_i^{n_i}) · ((^C x)^n / n!)
```

is a functorial bijection from `L(C) ⊗_C ^p√0_C` onto `**G**_p(L)(C)`.

#### 4.3.2.

<!-- label: III.VII_B.4.3.2 -->

<!-- original page 579 -->

"There is no Campbell–Hausdorff formula in characteristic `p > 0`". Let us explain ourselves: the functorial isomorphism
of 4.3.1 depends on the choice of the bases `(^C x_i)_{i ∈ I}`. Unlike what happens in 3.2 (case of characteristic 0),
there is no, in general, bijection from `L(C) ⊗_C ^p√0_C` onto `**G**_p(L)(C)` that is "functorial both in `C` and in
`L`". The argument that follows shows for example that such an isomorphism does not exist when `k` is a field containing
the `(p² − 1)`-th roots of unity.

Choose `L` indeed in such a way that, for every `C ∈ Alf/k`, `L(C)` is the abelian `p`-Lie algebra over `C` generated by
an element `x` subject to the relation `x^{(p²)} = 0`. One has therefore

```text
L(C) = Cx ⊕ Cx^{(p)},    U_p(L(C)) ≅ k[x]/(x^{p²}).
```

We shall show that the only functorial morphism

```text
χ_C : L(C) ⊗_C ^p√0_C ⟶ U_p(L(C))
```

that is compatible with the endomorphisms of `L` and that sends `L(C) ⊗_C ^p√0_C` into `**G**_p(L)(C)` is the constant
morphism of value `1`.

<!-- original page 579, marginal 548 -->

Indeed, let `ψ_C` be the bijection from `L(C) ⊗_C ^p√0_C` onto `**G**_p(L)(C) = Prim(U_p(L(C)))` given by 4.3.1, i.e.,

```text
x ⊗ a + x^{(p)} ⊗ b ↦ ∑_{0 ⩽ i, j < p} a^i b^j x^{i + pj}.
```

Composing `χ_C` with `ψ_C^{−1}`, one obtains a functorial morphism (in `C`):

```text
θ_C :  L(C) ⊗_C ^p√0_C → L(C) ⊗_C ^p√0_C
        x ⊗ a + x^{(p)} ⊗ b ↦ x ⊗ P(a, b) + x^{(p)} ⊗ Q(a, b).
```

Functoriality in `C` implies that `P(a, b)` and `Q(a, b)` are the values at `(a, b)` of two polynomials `P, Q ∈ k[X, Y]`
that one can assume of degree `< p` in `X` as well as in `Y`.[^N.D.E-VII_B-C-20] Let `α` be an element of `k` and `ℓ_α`
the `p`-Lie algebra endomorphism of `L` that sends `x` onto `α x` (and therefore `x^{(p)}` onto `α^p x^{(p)}`). Then
`U_p(ℓ_α)` is the algebra endomorphism that sends `x` onto `α x` (and therefore each `x^i` onto `α^i x^i`, for
`i < p²`), and one sees easily that the square below

```text
L(C) ⊗_C ^p√0_C ──ψ_C──→ U_p(L(C))
       │                       │
ℓ_α(C) ⊗_C id            U_p(ℓ_α)(C)
       ↓                       ↓
L(C) ⊗_C ^p√0_C ──ψ_C──→ U_p(L(C))
```

is commutative. The hypothesis `χ_C ∘ (ℓ_α(C) ⊗ id) = U_p(ℓ_α)(C) ∘ χ_C` then entails the equalities:

```text
P(α a, α^p b) = α P(a, b)    and    Q(α a, α^p b) = α^p Q(a, b).
```

Writing `P = ∑_{i, j < p} λ_{ij} X^i Y^j` and `Q = ∑_{i, j < p} μ_{ij} X^i Y^j`, and taking for `C` the algebra
`k[X, Y]/(X^p, Y^p)`, one deduces that if `λ_{ij} ≠ 0` (resp. `μ_{ij} ≠ 0`) then `α^{i − 1 + pj} = 1`

<!-- original page 580 -->

(resp. `α^{i + p(j − 1)} = 1`). Hence, taking for `α` a primitive root of unity of order `p² − 1`, one deduces that
`P = λ X` and `Q = μ Y`, with `λ, μ ∈ k`. Consequently, one has:

```text
χ_C(x ⊗ a + x^{(p)} ⊗ b) = ∑_{0 ⩽ i, j < p} (λ a)^i (μ b)^j x^{i + pj}.
```

[^N.D.E-VII_B-C-20] Finally, consider the endomorphism `f` of `L` that sends `x` onto `x + x^{(p)}`; taking
`C = k[a]/(a³)` and comparing the coefficients of `x^p` and `x^{p+1}` in `(χ_C ∘ f(C))(x ⊗ a)` and in
`(U_p(f)(C) ∘ χ_C)(x ⊗ a)`, one obtains that `λ = μ` and `λ² a² = 0`, whence `λ = μ = 0`.

### 4.4.

<!-- label: III.VII_B.4.4 -->

<!-- original page 580, marginal 549 -->

**Theorem 4.4.** *Let `k` be a pseudocompact ring of characteristic `p > 0` and `G` a `k`-formal group. The following
assertions are equivalent:*

<!-- label: III.VII_B.4.4 -->

*(i) There exists a `p`-Lie algebra `L` that is flat over `O_k` such that `G` is isomorphic to `**G**_p(L)` (and in this
case `L = Lie(G)` by 4.2.2).*

*(ii) There exists a projective pseudocompact `k`-module `ω` such that the affine algebra of `G` is isomorphic to the
quotient of `k[[ω]]` by the closed ideal generated by the `x^p`, for `x ∈ ω` (and in this case `ω ≃ ω_{G/k}`).*

*(iii) `G` is of height `⩽ 1` and `ω_{G/k}` is a projective pseudocompact `k`-module.*

*(iv) `G` is of height `⩽ 1` and is topologically flat over `k`.*

(i) ⇒ (ii): Let `ω = Γ_*(L)` (cf. 1.2.3.D) and `A` the quotient of `k[[ω]]` by the closed ideal generated by the `x^p`,
for `x ∈ ω`. Every continuous morphism `h : A → C`, where `C` is an object of `Alf/k`, is determined by its restriction
`h′` to `ω`; this restriction `h′` sends `ω` into `^p√0_C`. One thus obtains a canonical bijection from
`Hom_{Alp/k}(A, C)` onto the set `Hom_c(ω, ^p√0_C)` of continuous `k`-linear maps from `ω` into `^p√0_C`. This last set
is canonically isomorphic to `L(C) ⊗_C ^p√0_C` (see the proof of 3.3). The implication (i) ⇒ (ii) thus follows from the
functorial bijection `L(C) ⊗_C ^p√0_C ⥲ **G**_p(L)(C)` established in 4.3.1.

For the other implications, consult the proofs of Theorems 3.3 and VII_A 7.4.1, which are analogous.

**Remark 4.4.A.**[^N.D.E-VII_B-C-21] *Let `G` be an infinitesimal `k`-formal group, with affine algebra `A`, such that
`ω_{G/k} = I_A / I_A²` is a projective pseudocompact `k`-module. Then there exists a section `τ : ω_{G/k} → I_A` of the
projection `I_A → ω_{G/k}`, and `τ` induces a continuous morphism of algebras `ψ : k[[ω_{G/k}]] → A` that is surjective,
cf. the proof of the implication (iii) ⇒ (i) in 3.3.*

#### 4.4.1.

<!-- label: III.VII_B.4.4.1 -->

**Corollary 4.4.1.** *If `k` is a field of characteristic `p > 0`, the functor `L ↦ **G**_p(L)` is an equivalence of the
category of `p`-Lie algebras over `k` onto that of `k`-formal groups of height `⩽ 1`.*

<!-- label: III.VII_B.4.4.1 -->

<!-- original page 580, marginal 550 -->

Indeed, when `G` runs through the formal groups of height `⩽ 1`, the functor `G ↦ **G**_p(Lie G)` is isomorphic to the
identity functor by Theorem 4.4; likewise, we saw in 4.2.2 that the functor `L ↦ Lie **G**_p(L)` is isomorphic to the
identity functor (see also VII_A, 5.5.3).[^N.D.E-VII_B-C-22]

#### 4.4.2.

<!-- label: III.VII_B.4.4.2 -->

<!-- original page 581 -->

Take still `k` to be a field of characteristic `p`. Let `G` be an infinitesimal `k`-formal group, with affine algebra
`A`. Since `G` is infinitesimal, every open ideal of `A` contains `I_A^{\{p^n\}}` for `n` large enough, hence `G` is the
inverse limit of the affine algebras `A / I_A^{\{p^n\}}` of the groups `Fr_n G` (cf. 4.1.2). Every infinitesimal
`k`-formal group is therefore a direct limit of `k`-formal groups of finite height.

Suppose `G` is of height `⩽ n` and write `H = G / Fr G`.[^N.D.E-VII_B-C-23] By 2.4 and 2.4.1, `Fr : G → G^{(p)}`
factorizes through an epimorphism `π : G → H` followed by a monomorphism `i : H → G^{(p)}`. One has then the following
commutative diagram:

```text
G ──π──→ H ──Fr^{n−1}──→ H^{(p^{n−1})}
│                            │
Fr                         i^{(p^{n−1})}
↓                            ↓
G^{(p)} ──Fr^{n−1}──→ G^{(p^n)}
```

and since the functor `X ↦ X^{(p)}` commutes with fibered products, `i^{(p^{n−1})}` is still a monomorphism. Since
`Fr^n(G/k)` is zero and `π` is an epimorphism, then `Fr^{n−1}(G^{(p)}/k) ∘ i = i^{(p^{n−1})} ∘ Fr^{n−1}(H/k)` is zero,
and hence, `i^{(p^{n−1})}` being a monomorphism, `Fr^{n−1}(H/k)` is zero, so `H` is of height `⩽ n − 1`. One therefore
sees that: *every `k`-formal group of finite height possesses a composition series whose quotients are of height `⩽ 1`,
hence can be described by `p`-Lie algebras over `k`*.

Finally, the affine algebra `A` of `G` is a quotient of `k[[ω_{G/k}]]`, cf. 4.4.A; hence if `ω_{G/k}` is of finite
dimension over `k`, then all the algebras `A / I_A^{\{p^n\}}` are `k`-vector spaces of finite dimension. One therefore
sees that: *every infinitesimal formal group `G` over a field of characteristic `p > 0`, such that `ω_{G/k}` is of
finite dimension over `k`, is a direct limit of finite formal groups (i.e., of finite length, cf. 1.2.6)*.

## 5. Homogeneous spaces of infinitesimal formal groups over a field

<!-- label: III.VII_B.5 -->

### 5.0.

<!-- label: III.VII_B.5.0 -->

<!-- original page 581, marginal 551 -->

[^N.D.E-VII_B-C-24] Assume, for simplicity, that `k` is a field. Let `G` be a `k`-formal group with affine algebra
`A = **A**(G)`. Let `A^+` be the augmentation ideal of `A`; for every `a ∈ A` we shall denote by `ā = a − ε_A(a) 1_A`
its projection onto `A^+`. Let `F` be a formal subgroup

<!-- original page 582 -->

of `G`, defined by the closed ideal `J` of `A`, and let `π` (resp. `π̄`) be the projection `A → A/J` (resp. the
composition of the projections `A → A^+ → A^+/J`). Note that, for every `a ∈ A`, the projection of `Δ_A(a)` onto
`A ⊗̂ A^+` is `Δ_A(a) − a ⊗̂ 1`.

By Theorem 2.4, one can form the quotient `k`-formal variety `X = G/F`, its affine algebra `B` is

```text
                                τ₁
B = Ker( A ⇒ A ⊗̂_k (A/J) )
            (id_A ⊗̂ π) Δ_A

  = { a ∈ A | (id_A ⊗̂ π) Δ_A(a) = a ⊗̂ π(1) }

  = Ker( (id_A ⊗̂ π̄) Δ_A ).
```

It is also the subalgebra of `A` formed by the elements `φ` such that, for every `C ∈ Ob Alf/k` and `g ∈ G(C)`,
`h ∈ F(C)`, one has `φ(gh) = φ(g)`. For every `g, g′ ∈ G(C)` and `h ∈ F(C)`, one has `φ(g g′ h) = φ(g g′)`, hence `Δ(φ)`
belongs to the kernel of `id_A ⊗̂_k (id_A ⊗̂ π) Δ_A`, which equals `A ⊗̂_k B` since `A` is topologically flat over `k`.
One has therefore `Δ_A(B) ⊂ A ⊗̂_k B`, i.e., the closed subalgebra `B` is also a left coideal.

On the other hand, `B` determines `F` since, by Corollary 2.4.1, one has `J = A B^+`, i.e., `J` is the closed ideal
generated by `B^+ = B ∩ A^+`. One thus obtains an injective map `Q` from the set `**F**` of formal subgroups of `G` into
the set `**B**` of closed subalgebras `B` of `A` that are left coideals. The question then arises of determining the
image of this map, and Proposition 5.1 below shows that `Q` is bijective when `G` is infinitesimal. In fact, this is
true for every `k`-formal group `G`.

Indeed, recall (cf. 2.2.1) that the functor `G ↦ **H**(G)` is an equivalence between the category of `k`-formal groups
and that of cocommutative `k`-Hopf algebras; if `F` is a formal subgroup of `G`, defined by the closed ideal `J` of `A`,
then the Hopf subalgebra `**H**(F)` of `H = **H**(G)` is the orthogonal of `J` for the duality between `A = H^*` and
`H = A^†` (cf. 0.2.2). On the other hand, if `B` is a closed subalgebra of `A` that is also a left coideal, then its
orthogonal `I = B^⊥` is a coideal of `H` (i.e., `Δ_H(I) ⊂ I ⊗ H + H ⊗ I` and `ε_H(I) = 0`) and a left ideal. Denote by
`**H**` (resp. `**I**`) the set of Hopf subalgebras (resp. left ideals that are coideals) of `H`. For every `I ∈ **I**`,
one will denote by `π_I` (resp. `π̄_I`) the projection `H → H/I` (resp. the composition of the projections
`H → H^+ → H^+/I`), where `H^+` is the augmentation ideal of `H`.

Let `K` be a Hopf subalgebra of `H` and `K^+ = K ∩ H^+`. If `F` is the formal subgroup corresponding to `K`, then
`J = K^⊥` and `A^+/J` is identified with the dual of `K^+`, and since `B = Q(F)` is the kernel of the map

```text
A ──Δ_A──→ A ⊗̂_k A ──id ⊗̂ π̄──→ A ⊗̂_k (A^+/J)
```

one obtains that `Q` corresponds by duality to the map `Φ` which to `K` associates the image of

```text
H ←──m_H── H ⊗_k H ←──id ⊗̂ can.── H ⊗_k K^+
```

i.e., the left ideal `H K^+`, which is also a coideal. One sees similarly that the map which to `B ∈ **B**` associates
`A B^+` corresponds by duality to the map `Ψ` which to every `I ∈ **I**`

<!-- original page 584 -->

associates the kernel of `(id ⊗_k π̄_I) ∘ Δ_H`, i.e., one has

```text
Ψ(I) = { x ∈ H | (id ⊗_k π_I) Δ_H(x) = x ⊗ π_I(1) }.
```

One then has the following theorem:

**Theorem 5.0.1.** *Let `k` be a field and `H` a cocommutative Hopf algebra. Then the maps `Φ` and `Ψ` above are inverse
bijections between the set of Hopf subalgebras of `H` and that of left ideals that are coideals.*

<!-- label: III.VII_B.5.0.1 -->

This theorem was first proved by K. Newman, cf. [Ne75], Th. 4.1 (where the word "cocommutative" was forgotten). Its
proof uses "the Cartier–Gabriel–Kostant theorem" (cf. 2.9) to reduce to the case where `H` is connected, then the
existence in that case of a "Sweedler basis" (cf. [Sw67], Th. 3), a result dual to the Dieudonné–Cartier theorem 5.2.2
below. Another proof, shorter, was given by H. J. Schneider [Sch90], Th. 4.15. A generalization was then obtained by A.
Masuoka when one assumes only that the coradical `H_0` of `H` (i.e., the sum of the simple subcoalgebras) is commutative
[Ma91], Th. 1.3 (3).

Let us point out finally that for a commutative `k`-Hopf algebra, corresponding therefore to an affine `k`-group scheme
`G`, one cannot expect an analogue of 5.0.1 without additional hypotheses, since for a `k`-subgroup `F` of `G`, the
quotient `G/F` is not necessarily affine. But M. Takeuchi established in [Tak72], Th. 4.3 (resp. [Tak79], Th. 3), an
analogous bijection between the set of `k`-subgroups `F` of `G` which are invariant (resp. such that `G/F` is affine),
and that of subalgebras `B` of `O(G)` such that `Δ(B) ⊂ A ⊗ B` and which are stable under the antipode (resp. and such
that `B → A` is faithfully flat).

### 5.1.

<!-- label: III.VII_B.5.1 -->

Let `k` be a pseudocompact ring.[^N.D.E-VII_B-C-25] Let `G` be a topologically flat infinitesimal `k`-formal group, `A`
its affine algebra, `B` a closed subalgebra of `A`, `X = Spf(B)`, and `r : G → X` the epimorphism induced by the
inclusion of `B` into `A`. One proposes to see under what condition `r` makes `X` the right quotient of `G` by a
subgroup `H` (cf. 2.4).[^N.D.E-VII_B-C-26]

**Proposition.** *Let `G` be a topologically flat infinitesimal `k`-formal group, `A` its affine algebra, `I_A` the
augmentation ideal of `A`, `B` a closed subalgebra of `A`, and `J_B = A I_B`, where `I_B = B ∩ I_A`. Assume that `A` is
topologically flat over `k`, as well as `J_B^n / J_B^{n+1}` for every `n ⩾ 0`. Then the following two assertions are
equivalent:*

*(i) For every `x ∈ B`, `Δ_A(x) − x ⊗̂ 1` belongs to `A ⊗̂_k J_B`.*

<!-- original page 584 -->

*(ii) The sequence below (where `τ₁(a) = a ⊗̂ 1` and `π` is the projection `A → A/J_B`) is exact:*

```text
                                τ₁
(∗)    B ⟶ A ⇒ A ⊗̂_k (A/J_B)
                          (π ⊗̂ id_A) Δ_A
```

*that is, `B` is the set of all `x ∈ A` such that `Δ_A(x) − x ⊗̂ 1` belongs to `A ⊗̂_k J_B`.*

*In this case, `H = Spf(A/J_B)` is a formal subgroup of `G`, and the sequence below (where `λ` is the restriction to
`G × H` of the multiplication of `G`) is exact:*

```text
                                pr₁
(∗∗)    G × H ⇒ G ⟶ Spf(B)
                          λ
```

*that is, `Spf(B)` is isomorphic to `G/H`.*

Set `Ā = A/J_B` and `H = Spf(Ā)`; then `H` is a formal subvariety of `G`. Since `J_B ⊂ I_A`, the augmentation `ε_A`
induces a continuous morphism of `k`-algebras `ε̄ : Ā → k`.

If (i) is satisfied, then `Δ_A(I_B) ⊂ I_B ⊗̂ 1 + A ⊗̂ J_B`, and hence `Δ_A` induces by passage to the quotient a
diagonal morphism `Δ̄`. Then `Δ̄` and `ε̄` endow `H` with a structure of formal submonoid of `G`. Since `G` is
infinitesimal, so is `H`; hence, by Proposition 2.7, `H` is a formal subgroup of `G`. It then follows from the
definition of `G/H` (cf. 2.4) that (ii) entails the last assertion of the proposition.

On the other hand, it is clear that (ii) implies (i). The proof of the converse occupies paragraphs 5.1.1 to 5.1.5.

#### 5.1.1.

<!-- label: III.VII_B.5.1.1 -->

<!-- original page 584, marginal 552 -->

Let us first consider the following category `**C**`: an object of `**C**` is a pair `(A, J)` formed by a profinite
`k`-algebra `A` and a closed ideal `J` of `A`; a morphism `ψ : (A, J) → (A′, J′)` of `**C**` is a continuous
homomorphism of `k`-algebras `A → A′` that sends `J` into `J′`. If one associates to `(A, J)` the pair
`(Spf(A/J), Spf(A))`, one obtains evidently an anti-equivalence of `**C**` onto the category of pairs `(Z, Y)` formed by
a `k`-formal variety `Y` and a formal subvariety `Z`, a morphism `φ : (Z, Y) → (Z′, Y′)` being a morphism of `k`-formal
varieties `Y → Y′` that sends `Z` into `Z′`.

A *cogroup structure* on an object `(A, J)` of `**C**` consists of the data of a structure of formal group on `Spf(A)`
such that the following conditions are realized (notations of 2.1):

(1) `Δ_A(J) ⊂ J ⊗̂_k A + A ⊗̂_k J`;

(2) `ε_A(J) = 0`;

(3) `c_A(J) ⊂ J`.

These conditions also mean that `H = Spf(A/J)` is a formal subgroup of `G = Spf(A)`.[^N.D.E-VII_B-C-27]

<!-- original page 585 -->

Suppose moreover that `A` is local, i.e., that `Spf(A)` is an infinitesimal formal group. Then, if `J ≠ A`, conditions
(2) and (3) are consequences of (1). Indeed, if `J` is a closed ideal distinct from `A`, it is contained in the
augmentation ideal `I_A`, hence (2) is verified, and `M = Spf(A/J)` is a formal submonoid of `G`. Since `G` is
infinitesimal, it follows from 2.7 that `M` is a formal subgroup of `G`, i.e., condition (3) is verified.

#### 5.1.2.

<!-- label: III.VII_B.5.1.2 -->

<!-- original page 585, marginal 553 -->

Denote by `Alpg/k` the category of *graded profinite `k`-algebras*: an object of this category consists of the data of a
sequence `A_0, A_1, …, A_n, …` of pseudocompact `k`-modules and of a profinite algebra structure on the product
`∏_{n ⩾ 0} A_n` such that one has `A_n · A_m ⊂ A_{m+n}` (`A_n` being identified with a part of `∏_{i ⩾ 0} A_i` by means
of the canonical injection); a morphism `ψ : (A_n) → (B_n)` is a sequence of continuous linear maps `ψ_n : A_n → B_n`
such that one has `ψ_{m+n}(a · a′) = ψ_m(a) · ψ_n(a′)` if `a ∈ A_m` and `a′ ∈ A_n`.

**Definitions.** *It is clear that two graded profinite `k`-algebras `(A_n)` and `(B_n)` have a
coproduct[^N.D.E-VII_B-C-28] in `Alpg/k`, which has as `n`-th component the product `∏_{i=0}^n A_i ⊗̂_k B_{n−i}` of the
pseudocompact `k`-modules `A_i ⊗̂_k B_{n−i}`. This coproduct will be denoted `(A_n) ⊗̂_k (B_n)`.*

*Then, a cogroup structure on an object `(A_n)` of `Alpg/k` is the data of continuous `k`-linear maps
`Δ_n : A_n → ∏_{i=0}^n A_i ⊗̂_k A_{n−i}` and `ε : A_0 → k`, which induce on `∏_{n ⩾ 0} A_n` (setting `ε(A_i) = 0` for
`i ⩾ 1`) a cogroup structure in `Alp/k`.*

*Finally, for every object `(A, J)` of `**C**`, one denotes by `Gr_J(A)` the graded profinite algebra associated with
the filtration of `A` by the closures `J^n` of the powers of `J`; one has therefore `Gr_J(A)_n = J^n/J^{n+1}` and the
multiplication of `Gr_J(A)` is induced by that of `A`.*

**Lemma.**[^N.D.E-VII_B-C-29] *Let `U, V` be two pseudocompact `k`-modules, with `U` topologically flat, and let
`U = U_0 ⊃ U_1 ⊃ ⋯` and `V = V_0 ⊃ V_1 ⊃ ⋯` be two decreasing sequences of closed `k`-submodules. Filter the completed
tensor product `W = U ⊗̂_k V` by means of the closed submodules*

```text
W_n = U_n ⊗̂_k V_0 + U_{n−1} ⊗̂_k V_1 + ⋯ + U_0 ⊗̂_k V_n.
```

*Suppose that each `U_i/U_{i+1}` is topologically flat over `k` (so that `U/U_n` and hence `U_n` are also so, for every
`n`). Then, for every `n`, one has an isomorphism*

```text
W_n / W_{n+1} ≃ ⨁_{i + j = n} (U_i/U_{i+1}) ⊗̂_k (V_j/V_{j+1}).
```

<!-- original page 585, marginal 554 -->

*Proof.* Set `W_{i, j} = U_i ⊗̂ V_j` and `W̄_{i, j} = (U_i/U_{i+1}) ⊗̂_k (V_j/V_{j+1})`, for every `i, j ⩾ 0`. Let us
show by induction on `n` that the natural map

```text
π_n : W_n ⟶ ⨁_{i + j = n} W̄_{i, j}
```

is surjective and that the inclusion `W_{n+1} ⊂ Ker(π_n)` is an equality. For `n = 0`, the projection

```text
π_0 : U_0 ⊗̂_k V_0 ⟶ (U_0/U_1) ⊗̂_k (V_0/V_1)
```

is surjective and, since `U_0`, `U_0/U_1` and hence `U_1` are topologically flat over `k`, one sees that
`Ker(π_0) = U_0 ⊗̂_k V_1 + U_1 ⊗̂_k V_0` and that, moreover, `U_0 ⊗̂_k V_1 ∩ U_1 ⊗̂_k V_0 = U_1 ⊗̂_k V_1`.

Suppose then `n > 0` and the result established for `n − 1`. Set `M_0 = U_0 ⊗̂_k V_n` and
`S_0 = ∑_{i=1}^n U_i ⊗̂_k V_{n−i}`. One has `S_0 ⊂ U_1 ⊗̂_k V_0` and hence, by what precedes applied to `V_0 ⊃ V_n`
instead of `V_0 ⊃ V_1`, one has

```text
M_0 ∩ S_0 ⊂ U_0 ⊗̂_k V_n ∩ U_1 ⊗̂_k V = U_1 ⊗̂_k V_n
```

from which one deduces that `M_0 ∩ S_0 = U_1 ⊗̂_k V_n`. Since `W_n = M_0 + S_0`, one obtains a commutative diagram with
exact rows, where one has set `U′_i = U_{i+1}` and `W′_{i, n−1−i} = W_{i+1, n−1−i}` for `i = 0, …, n − 1`:

```text
0 ⟶ S_0 ⟶ W_n ⟶ (U_0/U_1) ⊗̂_k V_n ⟶ 0
        │π′_{n−1}    │π_n                │p
        ↓            ↓                   ↓
0 ⟶ ⨁_{i=0}^{n−1} W̄′_{i, n−1−i} ⟶ ⨁_{i=0}^n W̄_{i, n−1} ⟶ W̄_{0, n} ⟶ 0.
```

Then `p` is surjective, with kernel `(U_0/U_1) ⊗̂_k V_{n+1}`. Moreover, by the induction hypothesis applied to the
sequence `(U′_i)`, `π′_{n−1}` is surjective, with kernel equal to `W′_n = ∑_{i=1}^n W_{i, n+1−i}`. It follows that `π_n`
is surjective, and that the inclusion `W_{n+1} ⊂ Ker(π_n)` is an equality. This proves the lemma.

Let us return to an object `(A, J)` of `**C**` and note that, by 0.2.G, the hypothesis that each `J^n/J^{n+1}` is
topologically flat over `k` is equivalent to saying that `Gr_J(A)` is topologically flat over `k`.

**Corollary.** *Let `**P**` be the full subcategory of `**C**` formed by the objects `(A, J)` such that `A` and
`Gr_J(A)` are topologically flat over `k`. Then the functor `**P** → Alpg/k`, `(A, J) ↦ Gr_J(A)`, commutes with finite
coproducts, hence transforms a cogroup of `**P**` into a cogroup of `Alpg/k`.*

*In particular, if `k` is a field then, for every cogroup `(A, J)` of `**C**`, `Gr_J(A)` is a cogroup of
`Alpg/k`.*[^N.D.E-VII_B-C-30]

#### 5.1.3.

<!-- label: III.VII_B.5.1.3 -->

<!-- original page 587 -->

Identify every profinite `k`-algebra `Γ` with the graded profinite `k`-algebra `(Γ_n)_{n ⩾ 0}` such that `Γ_0 = Γ` and
`Γ_n = 0` if `n > 0`. In particular, if `(A_n)_{n ⩾ 0}` is a graded profinite `k`-algebra, we shall consider `A_0`
indifferently as a profinite `k`-algebra or as a graded profinite `k`-algebra. We shall then denote by `ρ : (A_n) → A_0`
the morphism of `Alpg/k` such that `ρ_0 = id_{A_0}` and `ρ_n = 0` if `n > 0`. Similarly, `τ : A_0 → (A_n)` will denote
the section of `ρ` such that `τ_0 = id_{A_0}` and `τ_n = 0` if `n > 0`.

Every cogroup structure on `(A_n)_{n ∈ ℕ}` induces a cogroup structure on `A_0` such that `ρ` and `τ` are homomorphisms
of cogroups. In this case, denote by `I_0` the augmentation ideal of `A_0` and set `A′_n = A_n / I_0 A_n` for every
`n ⩾ 0` (so that `A′_0 = k`).

Then, `(A′_n)_{n ∈ ℕ}` is a cogroup in `Alpg/k` (note that, since `A_0 = I_0 ⊕ k · 1`, then `I_0 ⊗̂_k A_n ≃ I_0 A_n` is
a direct factor of `A_n`, for every `n`). Since `τ` is a section of `ρ`, then, by 2.4.A, the cogroup `(A_n)_{n ∈ ℕ}` is
the "semi-direct coproduct" of `A_0` and of the cogroup `(A′_n)_{n ∈ ℕ}`. More precisely, `(A′_n)_{n ∈ ℕ}` is
isomorphic, as an object of `Alpg/k`, to the kernel of the pair:

```text
                              τ₁
(A_n) ⇒ (A_n) ⊗̂_k A_0
                          (id ⊗̂ ρ) Δ
```

(where `Δ : (A_n) → (A_n) ⊗̂ (A_n)` is the comultiplication of `(A_n)` and `τ₁(x) = x ⊗̂ 1`), and, identifying `A′_n`
with its image in `A_n`, the map

```text
(A′_n ⊗̂_k A_0) ⟶ (A_n),    a′_n ⊗̂ a_0 ↦ a′_n a_0
```

is an isomorphism in `Alpg/k`. (N.B. This is not an isomorphism of cogroups, but `Δ(A′) ⊂ A ⊗̂ A′` and
`(γ_ρ′ ⊗̂ id) ∘ Δ|_{A′} = Δ′`, where `Δ′` is the comultiplication of `A′` and `γ_ρ′` the projection `A′ → A′`, cf.
2.4.A.)

#### 5.1.4.

<!-- label: III.VII_B.5.1.4 -->

<!-- original page 587, marginal 555 -->

Let `(A, J)` be an object of `**C**` and `(A_n) = Gr_J(A)` the object of `Alpg/k` associated, i.e., `A_n = J^n/J^{n+1}`
for every `n ⩾ 0`. It is clear that the algebra `**A** = ∏_{n ⩾ 0} A_n` is generated by `A_0` and `A_1`, that is to say
that, for `n ⩾ 1`, the map

```text
(1)    A_1 ⊗̂_{A_0} A_1 ⊗̂_{A_0} ⋯ ⊗̂_{A_0} A_1 ⟶ A_n
```

defined by multiplication is surjective.

Suppose moreover that `(A, J)` is a cogroup of `**C**` and that `A` and the quotients `J^n/J^{n+1}` are flat over `k`.
Then, by Corollary 5.1.2, `Gr_J(A)` is a cogroup of `Alpg/k`. Therefore, by 5.1.3, if one sets

```text
(2)    A′_n = { x ∈ J^n/J^{n+1} | Δ(x) − x ⊗̂ 1 ∈ ⨁_{i=1}^n (J^{n−i}/J^{n−i+1}) ⊗̂ (J^i/J^{i+1}) },
```

then the map `(A′_n ⊗̂ A_0) → (A_n)`, `a′_n ⊗̂ a_0 ↦ a′_n a_0`, is an isomorphism in `Alpg/k`.[^N.D.E-VII_B-C-31]

<!-- original page 588 -->

Denoting by `I_0` the augmentation ideal of `A_0`, one deduces from (1) and the commutative diagram below, where
`A′_1 ⊗̂^n` denotes `A′_1 ⊗̂_k ⋯ ⊗̂_k A′_1` (`n` factors):

```text
A_1 ⊗̂_{A_0} ⋯ ⊗̂_{A_0} A_1  ⥲  A′_1 ⊗̂^n ⊗̂_k A_0  ⥲  (A′_1 ⊗̂^n ⊗̂_k I_0) ⊕ A′_1 ⊗̂^n
      │m                              │m′ ⊗̂ id              │m′ ⊗̂ id ⊕ m′
      ↓                                ↓                     ↓
A_n  ⥲  A′_n ⊗̂_k A_0  ⥲  (A′_n ⊗̂_k I_0) ⊕ A′_n
```

that the map

```text
(3)    m′ : A′_1 ⊗̂_k ⋯ ⊗̂_k A′_1 ⟶ A′_n
```

induced by multiplication is surjective; in other words, the profinite `k`-algebra `**A**′ = ∏_{n ⩾ 0} A′_n` is
generated by its terms of degree 1.

[^N.D.E-VII_B-C-32] Let us now return to the hypothesis (i) of Proposition 5.1: let `G` be a topologically flat
infinitesimal `k`-formal group, `A` its affine algebra, `I_A` the augmentation ideal of `A`, `B` a closed subalgebra of
`A`, and `J = A I_B`, where `I_B = B ∩ I_A`. Denote by `H` the formal subgroup `Spf(A/J)` and `π` the projection
`A → A/J`. Suppose that `A/J^n` is topologically flat over `k`, for every `n ⩾ 1`, and that `B` is contained in the
kernel `B̃` of the pair:

```text
                              τ₁
A ⇒ A ⊗̂_k (A/J).
                        (id_A ⊗̂_k π) Δ_A
```

Let `(A_n) = Gr_J(A)`, let `I_0 = I_A/J` be the augmentation ideal of `A_0 = A/J`, and define `(A′_n)_{n ∈ ℕ}` as in (2)
above. Denote by `(B_n)_{n ∈ ℕ}` (resp. `(B̃_n)_{n ∈ ℕ}`) the object of `Alpg/k` associated to the filtration of `B`
(resp. `B̃`) induced by that of `A`, i.e., defined by the ideals `B ∩ J^n` (resp. `B̃ ∩ J^n`). Then, it is clear that
`B_n ⊂ B̃_n ⊂ A′_n` for every `n`, and that

```text
**B** = ∏_{n ⩾ 0} B_n ⊂ **B̃** = ∏_{n ⩾ 0} B̃_n
```

are subalgebras of `**A**′ = ∏_{n ⩾ 0} A′_n`.

On the other hand, `J` (resp. `J²`) is the image in `A` of `I_B ⊗̂_k A` (resp. of `I_B² ⊗̂_k A`). Consequently, the map

```text
(I_B/I_B²) ⊗̂_k A ⟶ J/J² = A_1 ≃ A′_1 ⊗̂_k A_0
```

<!-- original page 589 -->

is surjective, and it factors through `(I_B/I_B²) ⊗̂_k A_0`. Since `A_0 = k · 1 ⊕ I_0`, one deduces from the commutative
and exact diagram:

```text
(I_B/I_B²) ⊗̂_k A_0  ⥲  ((I_B/I_B²) ⊗̂_k I_0) ⊕ (I_B/I_B²)
        ↓                          ↓
J/J²  ⥲  (A′_1 ⊗̂_k I_0) ⊕ A′_1
        ↓                          ↓
        0                          0
```

that `A′_1` is the image of `I_B/I_B²`, so that one has `B_1 = A′_1`. Since `**A**′` is generated by `A′_1`, it follows
that, for every `n ⩾ 1`, one has

```text
A′_n ⊂ B_n ⊂ B̃_n ⊂ A′_n,
```

<!-- original page 589, marginal 556 -->

whence `B_n = B̃_n = A′_n`.[^N.D.E-VII_B-C-33]

Finally, since the formal group `G` is infinitesimal, one has `𝔯(A) = I_A` and hence the ideals `I_A^n` tend to `0` (cf.
0.1.2); a fortiori, the ideals `J^n` tend to `0`, and hence the induced filtrations on `B̃` and `B` are separated.
Moreover, since `B` is a closed subalgebra of `A`, it is complete for the topology defined by the ideals `B ∩ J^n`.
Consequently, it follows from [CA], § V.7, Lemma 1 (see also 5.1.5 below) that `B = B̃`. This completes the proof of
Proposition 5.1.

One has moreover the following supplement. For every `n`, `J^n = A I_B^n` is the image in `A` of `A ⊗̂_B I_B^n` and also
of `A ⊗̂_B (B ∩ J^n)`. Now, by hypothesis, the affine algebra `A/J` of the formal subgroup `H` is topologically flat
over `k`. Hence, by Theorem 2.4, the morphism `G = Spf(A) → G/H = Spf(B)` is surjective and topologically flat; one has
therefore

```text
A ⊗̂_B I_B^n = J^n = A ⊗̂_B (B ∩ J^n),
```

and this entails that `I_B^n = B ∩ J^n` for every `n`. This also follows from the fact that the maps

```text
I_B^n / I_B^{n+1} ⟶ A′_i = (B ∩ J^n)/(B ∩ J^{n+1})
```

are surjective, and from 5.1.5 (ii) below, applied to `B′_n = I_B^n` and `B_n = B ∩ J^n`.

#### 5.1.5.

<!-- label: III.VII_B.5.1.5 -->

**Lemma 5.1.5.**[^N.D.E-VII_B-C-34] *(i) Let `M` and `N` be two abelian groups filtered by decreasing sequences of
subgroups `(M_n)_{n ∈ ℤ}` and `(N_n)_{n ∈ ℤ}`. Suppose that the union of the `M_n` (resp. `N_n`) equals `M` (resp. `N`),
that the intersection of the `M_n` (resp. `N_n`) is zero, and that `M` is complete for the topology defined by the
`M_n`. Let `f : M → N` be a morphism of filtered groups.*

<!-- label: III.VII_B.5.1.5 -->

<!-- original page 590 -->

*a) If `f` induces a surjection of the associated graded modules, then `f` is a surjection and `N` is complete for the
topology defined by the `N_n`.*

*b) If `f` induces an injection of the associated graded modules, then `f` is an injection.*

*(ii) Let `B` be an abelian group, `B = B′_0 ⊃ B′_1 ⊃ ⋯` and `B = B_0 ⊃ B_1 ⊃ ⋯` two separated filtrations of `B` by
subgroups such that `B′_n ⊂ B_n` for every `n`. Suppose `B` is complete for the topology defined by the filtration
`(B′_n)`.*

*If the map `B′_i/B′_{i+1} → B_i/B_{i+1}` is surjective for every `i`, then `B′_n = B_n` for every `n`.*

Indeed, (i) is Lemma 1 of [CA], § V.7 (see also [BAC], III, § 2.8), and (ii) follows from it by taking
`M = B′_n ⊃ B′_{n+1} ⊃ ⋯` and `N = B_n ⊃ B_{n+1} ⊃ ⋯`.

### 5.2.

<!-- label: III.VII_B.5.2 -->

In all the rest of Section 5, `k` denotes a perfect field of characteristic `p > 0`.

We set `**N̄** = ℕ ∪ {∞}`. If `B` is a profinite `k`-algebra and `r ∈ **N̄**`, we denote by `((x^{p^r}))_{x ∈ 𝔯(B)}` the
closed ideal of `B` generated by the elements `x^{p^r}`, where `x` runs through the radical `𝔯(B)` of `B`. If `r = ∞`,
we use the same notation, with the convention that `((x^{p^∞}))_{x ∈ 𝔯(B)}` is the zero ideal. In both cases, `B_r`
denotes the quotient `B / ((x^{p^r}))_{x ∈ 𝔯(B)}`.

We say that `B` is *of height `⩽ r`* if `((x^{p^r}))_{x ∈ 𝔯(B)}` is the zero ideal; if this holds and `r` is finite, we
say that `B` is *of finite height*.

Consider in particular the case where `B` is of the form `k[[ω]]`, `ω` being a pseudocompact `k`-vector space (cf.
1.2.5).[^N.D.E-VII_B-C-35] We then say that `B` is a *formal power series algebra* and that `B_r` is a *truncated formal
power series algebra* (`r ∈ **N̄**`; we therefore agree to say that `B = B_∞` is also "truncated"). If `B = k[[ω]]`, we
also write `((x^{p^r}))_{x ∈ ω}` instead of `((x^{p^r}))_{x ∈ 𝔯(B)}`.

<!-- original page 590, marginal 557 -->

**Notations.** *Let `ω` be a pseudocompact `k`-vector space filtered by an increasing sequence of closed vector
subspaces*

```text
0 = ω_0 ⊂ ω_1 ⊂ ω_2 ⊂ ω_3 ⊂ ⋯
```

*(a) The closed ideal of `k[[ω]]` generated by the elements `x^{p^r}`, where `r` runs through `ℕ` and `x` runs through
`ω_r`, will be denoted `((x^{p^r}))_{r ∈ ω_r}`.*

*(b) On the other hand, we shall denote by `^r ω` the filtered pseudocompact vector space such that*

```text
^r ω_i = ω_i    if i < r    and    ^r ω_i = ω    if i ⩾ r.
```

**Theorem (Dieudonné–Cartier).** *Let `H → G` be a monomorphism of infinitesimal formal groups over a perfect field `k`
of characteristic `p > 0`. Let `B` be the affine algebra of the homogeneous space `G/H` and suppose one of the following
three conditions verified:*[^N.D.E-VII_B-C-36]

<!-- label: III.VII_B.5.2 -->

<!-- original page 591 -->

*(i) `B` is of finite height (this is the case in particular if `G` is of finite height).*

*(ii) `B` is a complete noetherian local ring.*

*(iii) `B` is a reduced ring.*

*Then `B` is isomorphic to the completed tensor product of a finite family of truncated formal power series algebras.*

<!-- original page 591, marginal 558 -->

The proof of this theorem occupies paragraphs 5.2.1 to 5.2.5.

#### 5.2.1.

<!-- label: III.VII_B.5.2.1 -->

Let `A` be the affine algebra of `G`, `I_A` its augmentation ideal, and `I = B ∩ I_A`. By 2.4, one has `H = Spf(A/AI)`
and `B = { x ∈ A | Δ(x) − 1 ⊗̂ x ∈ A ⊗̂ AI }`. Set `ω = I/I²`. One denotes by `I_r` the closed sub-ideal of `I` formed
by the `x` such that `x^{p^r} = 0`, and by `ω_r` the canonical image of `I_r` in `ω`. We shall prove:

**Proposition.** *If there exists a continuous section `σ : ω → I` of the projection `I → I/I²`, such that
`σ(ω_r) ⊂ I_r` for every `r`, then `B` is isomorphic to `k[[ω]] / ((x^{p^r}))_{x ∈ ω_r}`.*

<!-- label: III.VII_B.5.2.1 -->

Such a section indeed extends into a continuous morphism `k[[ω]] → B`, which factors through
`B′ = k[[ω]] / ((x^{p^r}))_{x ∈ ω_r}`. We prove from 5.2.2 to 5.2.5 that the morphism

```text
φ : B′ = k[[ω]] / ((x^{p^r}))_{x ∈ ω_r} ⟶ B
```

thus obtained is an isomorphism.

##### 5.2.1.A.

<!-- label: III.VII_B.5.2.1.A -->

[^N.D.E-VII_B-C-37] For each `r ∈ ℕ`, set `I̅_r = I² + I_r`, so that `I̅_r/I² ≃ ω_r`; one then has a commutative diagram
with exact rows:

```text
0 ⟶ I̅_{r−1} ⟶ I̅_r ⟶ I̅_r/I̅_{r−1} ⟶ 0
                                ≀
                                ↓
0 ⟶ ω_{r−1} ⟶ ω_r ⟶ ω_r/ω_{r−1} ⟶ 0
```

and since `k` is a field, the rows are split: one can complete a pseudobasis `B_{r−1}` of `I̅_{r−1}` into a pseudobasis
`B_{r−1} ∪ B′_r` of `I̅_r`, and then the closed subspace `S_r` with pseudobasis `B′_r` is a supplement of `I̅_{r−1}` in
`I̅_r`, and the projection `π : I → ω` induces an isomorphism of `S_r` onto a supplement `ω′_r` of `ω_{r−1}` in `ω_r`.
Denote by `I_∞` the closed ideal `⋃_r I̅_r`; it admits similarly a supplement `S_∞` in `I`, and `π` induces an
isomorphism of `I_∞/I²` (resp. of `S_∞`) onto the closure `ω_∞` of the union of the `ω_r` (resp. onto a supplement
`ω′_∞` of `ω_∞` in `ω`). Denote by `η` the isomorphism `S_∞ ⥲ ω′_∞`. One then obtains continuous linear maps:

```text
I² × S_∞ × ⨁^c_r S_r ──φ──→ I
              │
              η × θ
              ↓
              ω = ω′_∞ × ω_∞
```

<!-- original page 592, marginal 559 -->

where `⨁^c_r S_r` is the direct sum of the `S_r` in `PC(k)`, i.e., `(∏_r S_r^†)^*` (cf. N.D.E. (16) of 0.2.2) and where
`θ : ⨁^c_r S_r → ω_∞` is induced by the maps `S_r ⥲ ω′_r ↪ ω_∞`. One therefore sees that a sufficient condition (but not
necessary, see below) to obtain a section `σ : ω → I` as desired is that `θ` be an isomorphism. By duality (cf. 0.2.2),
this amounts to saying that the linear map `ω_∞^† → ∏_r S_r^†` is bijective.

##### 5.2.1.B.

<!-- label: III.VII_B.5.2.1.B -->

Denote, as before, `ω_∞ = ⋃_{n ∈ ℕ} ω_n`. A second case in which a section `σ : ω → I` as desired exists is the case
where `ω_∞` possesses a pseudobasis `**B**_∞` that is a union of pseudobases of the `ω_n/ω_{n−1}`, for `n ∈ ℕ^*` (one
can then complete it by a pseudobasis `**B**′_∞` of `ω/ω_∞` to obtain a pseudobasis of `ω` compatible with the
filtration). Setting `V = ω_∞^†` and denoting by `V_n` the orthogonal in `V` of `ω_n`, this amounts to saying that, in
the category of "ordinary" `k`-vector spaces, the decreasing separated filtration

```text
V = V_0 ⊃ V_1 ⊃ V_2 ⊃ ⋯
```

is split, i.e., that `V` is the direct sum, for `n ∈ ℕ`, of subspaces `F_n` such that `F_n ≃ V_n/V_{n+1}`. This is not
necessarily the case: for example, if `V` is the space `S = k^ℕ` of sequences of elements of `k` and `S_n` the subspace
of sequences `(u_i)` such that `u_i = 0` for `i < n`, so that `dim S_n/S_{n+1} = 1`, then `S` is not isomorphic to the
direct sum of the `S_n/S_{n+1}` since `S` is not of countable dimension (on the other hand, `S` is here the product of
the `S_n/S_{n+1}`, cf. 5.2.1.A). It is however the case if `V` is of countable dimension.[^N.D.E-VII_B-C-38] Indeed, let
`(e_n)_{n ∈ ℕ}` be a basis of `V`; we shall construct by induction on `n` an increasing function `g : ℕ → ℕ` and
subspaces `F_i`, for `i = 0, …, g(n)`, such that `F_i ≃ V_i/V_{i+1}` and that `F_{⩽ g(n)} = ⨁_{i=0}^{g(n)} F_i` is a
supplement of `V_{g(n)+1}` containing `e_0, …, e_n`; one will then have `V = ⨁_{i ⩾ 0} F_i`. Let `n + 1 ∈ ℕ`; we may
assume the assertion established for `n` (the assertion being vacuous for `n = −1`). If `e_{n+1} ∈ F_{⩽ g(n)}`, set
`g(n + 1) = g(n)`; otherwise write `e_{n+1} = f + x` with `f ∈ F_{⩽ g(n)}` and `x ∈ V_{g(n)+1}` nonzero. Let then `j` be
the smallest integer such that `x ∈ V_j − V_{j+1}`; for `i = g(n) + 1, …, j`, choose a supplement `F_i` of `V_{i+1}` in
`V_i`, so that `e_{n+1} ∈ F_j`; one then sets `g(n + 1) = j`.

##### 5.2.1.C.

<!-- label: III.VII_B.5.2.1.C -->

[^N.D.E-VII_B-C-39] In particular, the two preceding conditions (5.2.1.A and B) are verified when the filtration of `ω`
is stationary, i.e., when there exists an integer `n_0` such that `ω_n = ω_{n_0}` for `n_0 ⩽ n < +∞`. In this case, one
obtains an isomorphism of `k[[ω]] / ((x^{p^r}))_{x ∈ ω_r}` onto the completed tensor product:

```text
( k[[ω_1]] / ((x^p))_{x ∈ ω_1} ) ⊗̂ ( k[[ω′_2]] / ((x^{p²}))_{x ∈ ω′_2} ) ⊗̂ ⋯ ⊗̂ ( k[[ω′_{n_0}]] / ((x^{p^{n_0}}))_{x ∈ ω′_{n_0}} ) ⊗̂ k[[ω′_∞]]
```

where `ω′_n` (resp. `ω′_∞`) is a supplement of `ω_{n−1}` in `ω_n` (resp. of `ω_∞ = ω_{n_0}` in `ω`). The filtration of
`ω` is obviously stationary in case (i), i.e., if `ω_r = ω` for `r` large enough, and in case (ii), i.e., if `ω` is of
finite dimension, and also in case (iii), i.e., if `I_r = 0` for every `r` (and in this case `B` will be isomorphic to
the formal power series algebra

<!-- original page 593 -->

`k[[ω]]`). The remarks above therefore imply our theorem, modulo points 5.2.2–5.2.5 below.

#### 5.2.2.

<!-- label: III.VII_B.5.2.2 -->

<!-- original page 593, marginal 559 -->

Suppose first that `B` is of height `⩽ 1`, that is to say that `x^p = 0` if `x ∈ I`. By 5.1.4, the graded ring `Gr_I(B)`
associated with `B` for the filtration `I ⊃ I² ⊃ I³ ⊃ ⋯` is endowed with a cogroup structure in the category `Alpg/k`,
i.e., the profinite algebra `**C** = ∏_{n ⩾ 0} Gr_I(B)_n` is the affine algebra of a `k`-formal group `N`. It is clear
that one has `ω_{N/k} = I/I²` and that `N` is infinitesimal of height `⩽ 1`. By 4.4, the identity map of `ω_{N/k}`
therefore induces an isomorphism of `B′ = k[[ω_{N/k}]] / ((x^p))_{x ∈ ω_{N/k}}` onto `**C**`. This implies in particular
that the map `φ` of 5.2.1 induces an isomorphism of the associated graded rings of `B′` and `B` when one filters `B′`
and `B` by the powers of the augmentation ideal. Hence `φ` is an isomorphism, by [CA], § V.7, Lemma 1 (see also 5.1.5).

#### 5.2.3.

<!-- label: III.VII_B.5.2.3 -->

Suppose now `B` of finite height `⩽ r`. Let `π` be the isomorphism `x ↦ x^p` of `k` onto `k`. The linear map of
`B ⊗̂_π k` into `B` which sends `b ⊗̂_π x` onto `b^p x = (b x^{1/p})^p` has a closed image which is none other than the
closed subalgebra `B^p = { b^p | b ∈ B }` of `B`. Set `J = B^p ∩ I = B^p ∩ I_A`.

[^N.D.E-VII_B-C-40] Denote by `G_1` the kernel of the Frobenius morphism `Fr : G → G^{(p)}` and by `H G_1` the formal
subgroup of `G` inverse image of the formal subgroup `H^{(p)}` of `G^{(p)}`. Then `H G_1` is defined by the closed ideal
generated by the `p`-th powers of elements of `AI`, which equals `AJ`. On the other hand, since the formation of `G/H`
commutes with base change (since `G/H` represents the sheaf-quotient for the flat topology, cf. 2.4), then
`(G/H)^{(p)} = G^{(p)}/H^{(p)}`, and one therefore has commutative diagrams:

```text
G ──Fr──→ G^{(p)}              A ←──a ⊗̂ 1 ↦ a^p──── A ⊗̂_π k
↓                  ↓               ↑                       ↑
G/H ──Fr──→ G^{(p)}/H^{(p)}      B ←──b ⊗̂ 1 ↦ b^p──── B ⊗̂_π k
```

from which one deduces that `B^p` is the affine algebra of the quotient `G/H G_1`.[^N.D.E-VII_B-C-41] Denote
provisionally by `**C**` the affine algebra of the quotient `H G_1 / H`. Since the formation of `G/H` commutes with base
change, one has a cartesian square:

```text
H G_1 ⟶ G
  ↓        ↓
H G_1/H ⟶ G/H
```

whence an isomorphism `A ⊗̂_B **C** ≃ A/AJ = A ⊗̂_B (B/BJ)`, and since `A` is topologically free over `B` (by 2.4, since
`A` and `B` are local), it follows that the natural morphism `B/BJ → **C**` is an isomorphism, hence `B/BJ` is the
affine algebra of `H G_1 / H`,[^N.D.E-VII_B-C-41] and of course `B/BJ = B_1` is of height `⩽ 1` since
`J = ((x^p))_{x ∈ 𝔯(B)}`.

<!-- original page 594 -->

Let `B′ = k[[ω]] / ((x^{p^r}))_{x ∈ ω_r}`, `φ : B′ → B` the morphism introduced in 5.2.1, `B′^p` the subalgebra
`{ x^p | x ∈ B′ }`, and `J′` the augmentation ideal of `B′^p`. Then, one has a commutative diagram:

```text
B′ ──φ──→ B
↓                ↓
B′_1 = B′/B′J′ ⟶ B_1 = B/BJ
```

and, by 5.2.2, `φ_1` is an isomorphism.

<!-- original page 594, marginal 560 -->

On the other hand, by 2.4, `A` is topologically flat over `B = **A**(G/H)` and over `B^p = **A**(G/H G_1)`; hence, by
1.3.3, `B` is topologically flat over `B^p`. Moreover, by 5.2.4 below, the morphism `B′^p → B^p` induced by `φ` is an
isomorphism. One can then apply 0.3.4 to the pseudocompact ring `B′^p = B^p` and to the pseudocompact `B^p`-modules
`M = B′`, `N = B`: by what precedes, `φ_1 = φ ⊗̂_{B^p} k` is an isomorphism, and it follows that `φ` is an isomorphism.
This proves 5.2 when `B` is of finite height, modulo point 5.2.4 below.

#### 5.2.4.

<!-- label: III.VII_B.5.2.4 -->

For every pseudocompact vector space `V` over `k`, we denote by `^π V` the space `V ⊗̂_π k` deduced from `V` by the
extension `x ↦ x^p` of the field of scalars.[^N.D.E-VII_B-C-42] One then has a commutative diagram with exact rows

```text
0 ⟶ ^π I² ──α──→ ^π I ──β──→ ^π ω ⟶ 0
        │u            │v          │w
        ↓             ↓           ↓
0 ⟶ J² ──γ──→ J ──δ──→ ω̄ ⟶ 0
```

where one has set `ω̄ = J/J²` and where the maps `u, v, w` are induced by the linear map `x ⊗̂ a ↦ x^p a` from `^π B`
into `B^p`. Since `u` and `v` are surjections, `w` is a surjection and has as kernel the image `^π ω_1` of
`^π I_1 = Ker(v)`.

Then, setting `J_n = { x ∈ J | x^{p^n} = 0 }` and `ω̄_n = δ(I_n)`, one has `J_n = v(^π I_{n+1})` and
`ω̄_n = w(^π ω_{n+1})`, for every `n ⩾ 0`. The section `^π σ : ^π ω → ^π I`, which is induced by the section `σ` of
5.2.1, therefore defines by passage to the quotient a section `τ : ω̄ → J` that is compatible with the filtrations of
`J` and `ω̄`. Since `B^p` is of height `⩽ r − 1`, this section induces, by induction hypothesis, an isomorphism

```text
ψ : B′′ = k[[ω̄]] / ((x^{p^n}))_{x ∈ ω̄_n} ⥲ B^p.
```

Now `B′′` is identified with `B′^p` and `ψ` with the morphism `B′^p → B^p` induced by `φ`, hence our

<!-- original page 595, marginal 561 -->

theorem is proved when `B` is of finite height.

**Remark 5.2.4.A.**[^N.D.E-VII_B-C-43] *Suppose `B` of height `⩽ r + 1` (with `r ∈ ℕ^*`). Then `I_{r+1} = I` and one has
an isomorphism*

<!-- label: III.VII_B.5.2.4.A -->

```text
(1)    B ≃ (k[[S_1]]/((x_1^p))_{x_1 ∈ S_1}) ⊗̂_k ⋯ ⊗̂_k (k[[S_r]]/((x_r^{p^r}))_{x_r ∈ S_r}) ⊗̂_k (k[[S_{r+1}]]/((x_{r+1}^{p^{r+1}}))_{x_{r+1} ∈ S_{r+1}})
```

*where each `S_n` is a supplement of `I² + I_{n−1}` in `I² + I_n`. Then `ω = I/I²` is identified with
`∏_{i=1}^{r+1} S_i`, and one sees easily that, for `n = 1, …, r + 1`, the image `ω_n` of `I_n` in `ω` is identified with
`∏_{i=1}^n S_i`.*

This has the following consequence. Let `B_r = B/J̌_r`, where `J̌_r = ((x^{p^r}))_{x ∈ 𝔯(B)}`, and let `𝔪 = I/J̌_r` be
the augmentation ideal of `B_r`; since `J̌_r ⊂ I²`, then `ω(r) = 𝔪/𝔪²` is identified with `ω`. For `n = 1, …, r`, denote
by `ω(r)_n` the image in `ω(r)` of `𝔪^n`; it is also the image in `ω` of `{ x ∈ I | x^{p^n} ∈ J̌_r }`, hence `ω(r)_n`
contains `ω_n`. On the other hand, it follows from isomorphism (1) that one has
`J̌_r = ((x_{r+1}^{p^r}))_{x_{r+1} ∈ S_{r+1}}`, whence

```text
(2)    B_r ≃ (k[[S_1]]/((x_1^p))_{x_1 ∈ S_1}) ⊗̂_k ⋯ ⊗̂_k (k[[S_r]]/((x_r^{p^r}))_{x_r ∈ S_r}) ⊗̂_k (k[[S_{r+1}]]/((x_{r+1}^{p^r}))_{x_{r+1} ∈ S_{r+1}})
```

and therefore, by what precedes, `ω(r)_n` is identified with `∏_{i=1}^n S_i` for `n = 1, …, r − 1`. One thus obtains
that the inclusion `ω_n ⊂ ω(r)_n` is an equality, for `n = 1, …, r − 1`.

#### 5.2.5.

<!-- label: III.VII_B.5.2.5 -->

It remains to consider the case where `B` is of infinite height, and where the projection `I → ω` possesses a section
`σ` compatible with the filtrations of `ω` and `I`. Consider the morphism

```text
φ : B′ = k[[ω]] / ((x^{p^n}))_{x ∈ ω_n} ⟶ B
```

induced by `σ`; it suffices to show that for every `r ∈ ℕ`, the map `φ_r : B′_r → B_r` induced by `φ` is
invertible.[^N.D.E-VII_B-C-44]

For every `r ∈ ℕ^*`, denote by `G_r` the kernel of the iterated Frobenius morphism `G → G^{(p^r)}` and by `H G_r` the
formal subgroup of `G` inverse image of the formal subgroup `H^{(p^r)}` of `G^{(p^r)}`, so that `H G_r` is defined by
the closed ideal generated by the `p^r`-th powers of elements of `AI`, which equals `AJ̌_r`, where
`J̌_r = { x^{p^r} | x ∈ I }`. One obtains then, exactly as in 5.2.3, that `B_r = B/B J̌_r` is the affine algebra of
`H G_r / H` (and is of course of height `⩽ r`).

Denote by `𝔪(r) = I/B J̌_r` the augmentation ideal of `B_r`; the canonical projection of `B` onto `B_r` obviously
induces an isomorphism of `ω = I/I²` onto `ω(r) = 𝔪(r)/𝔪(r)²`, which allows us to identify these two spaces. Let
`ω(r)_n` be the image in `ω(r)` of the closed ideal `𝔪(r)_n = { y ∈ 𝔪(r) | y^{p^n} = 0 }`; it is also the image in `ω`
of the closed ideal

<!-- original page 596 -->

`I(r)_n = { x ∈ I | x^{p^n} ∈ B J̌_r }`.[^N.D.E-VII_B-C-45] It is clear that `ω_n(r) = ω` if `n ⩾ r`; let us show that
`ω_n(r) = ω_n` if `n < r`. For every `r, n`, the sequence below is exact:

```text
0 ⟶ I(r)_n ∩ I² ⟶ I(r)_n ⟶ ω(r)_n ⟶ 0.
```

Moreover, for `n` fixed, one has `⋂_r I(r)_n = I_n`, since `⋂_r B J̌_r = 0`. Since in `PC(k)` filtered inverse limits
are exact (cf. 0.2), it follows that, for every `n`, one has

```text
(∗)    ω_n = ⋂_r ω(r)_n.
```

On the other hand, by Remark 5.2.4.A, one has `ω(r)_n = ω(r + 1)_n` if `n < r`. Combined with `(∗)`, this entails that
`ω(r)_n = ω_n` if `n < r`.

<!-- original page 596, marginal 562 -->

Consequently, the vector space `ω` filtered by the subspaces `(ω(r)_n)_{n ⩾ 0}` is none other than `^r ω` (Notations
5.2). A fortiori, the map `σ(r)` composed of `σ : ω → I` and of the projection `I → 𝔪(r)` is compatible with the
filtrations `(ω(r)_n)` and `(𝔪(r)_n)` of `ω` and `𝔪(r)`. Since `k[[^r ω]] / ((x^{p^n}))_{x ∈ ^r ω_n}` is none other than
`B′_r` and `φ_r : B′_r → B_r` is the morphism induced by `σ(r)`, the result already established for algebras of finite
height shows that `φ_r` is an isomorphism.

#### 5.2.6.

<!-- label: III.VII_B.5.2.6 -->

**Definition 5.2.6.**[^N.D.E-VII_B-C-46] *Let `(A_λ)_{λ ∈ Λ}` be a family of profinite `k`-algebras, each endowed with
an augmentation `ε_λ : A_λ → k` (this is the case in particular if each `A_λ` is local with residue field `k`). One
defines then the infinite completed tensor product*

```text
**A** = ⊗̂^c_{λ ∈ Λ} A_λ
```

*as the inverse limit in `Alp/k` of the `**A**_F = ⊗̂^c_{λ ∈ F} A_λ`, for `F` running through the finite subsets of `Λ`,
the transition morphisms `**A**_{F′} → **A**_F`, for `F′ = F ∪ {λ}`, being `id ⊗̂ ε_λ`.*

<!-- label: III.VII_B.5.2.6 -->

In particular, if `Λ = ℕ^*` and if one denotes by `X_n` the `k`-formal variety `Spf(A_n)`, then `Spf(**A**)` represents
the functor that to every `C ∈ Alf/k` associates the set of "finite" sequences of elements of `∏_{n ⩾ 1} X_n(C)`, i.e.,
sequences

```text
(x_1, x_2, …) ∈ ∏_{n ⩾ 1} X_n(C)
```

such that `x_n = ε_n` for `n` large enough, where `ε_n` denotes, by abuse of notation, the composite of `ε_n : A_n → k`
and of the structure morphism `k → C`. (If moreover each `A_n` is a quotient of an algebra `k[[ω′_n]]`, one can denote
by `0` the unique morphism `A_n → C` that vanishes on `ω′_n`, and one therefore obtains the set of sequences such that
"`x_n = 0`" for `n` large enough.)

### 5.3.

<!-- label: III.VII_B.5.3 -->

**Remarks.** *(a) Let us call **stationary** every profinite `k`-algebra that is the completed tensor product of a
family of truncated formal power series algebras.*[^N.D.E-VII_B-C-47]

<!-- original page 597 -->

If `G` is an infinitesimal `k`-formal group and `B` the affine algebra of a homogeneous space of `G`, it follows from
Theorem 5.2 that the algebra `B / ((x^{p^r}))_{x ∈ 𝔯(B)}` is stationary for every integer `r ∈ ℕ`. This implies in
particular that `B` is an inverse limit of stationary algebras.[^N.D.E-VII_B-C-48]

*(b) I do not know if, with the notations of 5.2.1, one can choose `A` and `B` in such a way that there exists no
section `σ : ω → I` compatible with the filtrations.*[^N.D.E-VII_B-C-49] *One will however note that one can have for
`ω` any pseudocompact vector space filtered by an increasing sequence of closed subspaces. Indeed, if
`ω_1 ⊂ ω_2 ⊂ ⋯ ⊂ ω` is such a filtered space, one can define in the algebra `B = A = k[[ω]] / ((x^{p^r}))_{x ∈ ω_r}` a
diagonal morphism `Δ_A : A → A ⊗̂_k A` satisfying conditions (i), (ii), (iii) of 2.1; it suffices to set
`Δ_A(y) = y ⊗̂ 1 + 1 ⊗̂ y` when `y` is the image in `A` of an element of `ω`.*

### 5.4.

<!-- label: III.VII_B.5.4 -->

<!-- original page 597, marginal 563 -->

**Corollary 5.4.** *Let `G` be an algebraic group over a perfect field `k` of characteristic `p > 0`, `H` an algebraic
subgroup of `G`, `e` the image of the neutral element of `G` in `G/H`, and `A` the local algebra of `G/H` at `e`. Then
`Â` is isomorphic to an algebra of the form*

```text
k[[X_1, …, X_r, … X_s]] / (X_1^{p^{n_1}}, …, X_r^{p^{n_r}}).
```

<!-- label: III.VII_B.5.4 -->

Indeed, consider the infinitesimal formal groups `Ĝ = Spf(Ô_{G, e})` and `Ĥ = Spf(Ô_{H, e})`; by 1.3.4, the completion
`Â` of `A = O_{G/H, e}` is isomorphic to `**A**(Ĝ/Ĥ)`, and the corollary therefore follows from Theorem 5.2
(ii).[^N.D.E-VII_B-C-50]

### 5.5. Complements.

<!-- label: III.VII_B.5.5 -->

[^N.D.E-VII_B-C-51] Recall the following definitions. On the one hand, one says that a noetherian local ring `A` is a
*complete intersection* if the completion `Â` is a quotient of a complete regular noetherian local ring `B` by an ideal
`I` generated by a regular sequence of elements of `B` (cf. EGA IV₄, 19.3.1). On the other hand, let `τ : Y ↪ X` be a
closed immersion of schemes. If `y ∈ Y`, one says that `τ` is a *regular immersion at the point `y`* if the kernel of
`O_{X, y} → O_{Y, y}` is generated by a regular sequence; if moreover `X` is locally noetherian and if `τ` is a regular
immersion at every point, one says that `τ` is a regular immersion (cf. loc. cit., Prop. 16.9.10 and Déf. 16.9.2).

<!-- original page 599 -->

**Corollary 5.5.1.** *If `G` is an algebraic group over a field `k`, the local ring `O_{G, e}` is a complete
intersection.*

<!-- label: III.VII_B.5.5.1 -->

Indeed, by EGA IV₄, 19.3.4, one can assume `k` algebraically closed. If `car(k) = 0`, we already know that `G` is smooth
(cf. 3.3.1 or VI_B, 1.6.1) and hence `O_{G, e}` is a `k`-algebra of formal power series, by EGA IV₄, 17.5.3 (d′′). If
`car(k) = p > 0`, it follows from 5.4, applied to `H = {e}`, that `O_{G, e}` is a complete intersection.

**Remarks 5.5.2.** *Let `k` be a field, `G` a smooth `k`-algebraic group, and `H` a closed subgroup of `G`.*

<!-- label: III.VII_B.5.5.2 -->

*a) We saw in Exp. III, 4.15, that the immersion `H ↪ G` is regular; this can also be deduced from 5.4, as follows.* As
in loc. cit., one can assume `k` algebraically closed, and it suffices to show that the kernel `I` of
`O_{G, e} → O_{H, e}` is generated by a regular sequence. Set `A = O_{G, e}`, `Ĝ = Spf(Â)` and `Ĥ = Spf(Ô_{H, e})`.
Since `A` is noetherian, one has an exact sequence

```text
0 ⟶ I ⊗_A Â ⟶ Â ──π──→ **A**(Ĥ) → 0
```

and `Â` is faithfully flat over `A`. Hence, by EGA IV₄, 16.9.10 (ii) and 19.1.5 (ii), it suffices to show that the
kernel `Î = I ⊗_A Â` of `π` is generated by a regular sequence of elements of `Â`.

Now, since `G` is smooth, `Â` is reduced; by 5.4, the subalgebra `B = **A**(Ĝ/Ĥ)` is therefore isomorphic to a formal
power series algebra `k[[x_1, …, x_n]]`, and hence the unit section of `Ĝ/Ĥ` is defined in `B` by the regular sequence
`(x_1, …, x_n)`. Since `Â` is noetherian, the ideal `J` of `Â` generated by `x_1, …, x_n` is closed, hence equal to `Î`,
by Corollary 1.4. Moreover, since `Â` is topologically flat, hence flat over `B` (cf. 0.3.8), then `(x_1, …, x_n)` is a
regular sequence in `Â`, by EGA IV₄, 19.1.5 (ii).

*b) One can also deduce from 5.2 (ii) the following more precise result.* Suppose `k` perfect. By 5.2 (ii) applied to
the algebra `C = **A**(H)`, there exists a basis `(y_1, …, y_{r+s})` of `ω_H` and integers `1 ⩽ n_1 ⩽ ⋯ ⩽ n_r` such that
`**A**(H)` is isomorphic to the quotient of `k[[y_1, …, y_{r+s}]]` by the ideal generated by the `y_i^{p^{n_i}}` for
`i = 1, …, r`. Lift the `y_i` to elements `x_i` of `ω_G` and complete `(x_1, …, x_{r+s})` into a basis `(x_1, …, x_n)`
of `ω_G`. Since `**A**(G)` is reduced, the morphism `k[[x_1, …, x_n]] → **A**(G)` is an isomorphism, by 5.2 (iii). One
thus obtains: *there exists a "system of coordinates" `(x_1, …, x_n)` of `G` (i.e., an isomorphism
`**A**(G) ≃ k[[x_1, …, x_n]]`) such that `H` is defined by the equations `x_i^{p^{n_i}} = 0` for `i = 1, …, r` and
`x_i = 0` for `i > r + s`* ("Dieudonné's theorem", compare with [Di55], § 19, Th. 6 and [Di73], II § 3.2, Prop. 3 and
what precedes it).

## Bibliography

<!-- label: III.VII_B.Bibliography -->

[CA] P. Gabriel, *Des catégories abéliennes*, Bull. Soc. Math. France **90** (1962), 323–448.[^N.D.E-VII_B-C-52]

<!-- original page 600 -->

[Ab80] E. Abe, *Hopf algebras*, Cambridge Univ. Press, 1980.

[Br00] C. Breuil, *Groupes `p`-divisibles, groupes finis et modules filtrés*, Ann. of Math. **152** (2000), no. 2,
489–549.

[BAlg] N. Bourbaki, *Algèbre*, Chap. I–III et IV–VII, Hermann, 1970, et Masson, 1981.

[BAC] N. Bourbaki, *Algèbre commutative*, Chap. I–IV, Masson, 1985.

[BEns] N. Bourbaki, *Théorie des ensembles*, Chap. I–IV, Hermann, 1970.

[BLie] N. Bourbaki, *Groupes et algèbres de Lie*, Chap. II–III, Hermann, 1970.

[Ca62] P. Cartier, *Groupes algébriques et groupes formels*, pp. 87–111 in: *Colloque sur la théorie des groupes
algébriques* (Bruxelles, 1962), Gauthier-Villars, 1962.

[DG70] M. Demazure, P. Gabriel, *Groupes algébriques*, Masson & North-Holland, 1970.

[De72] M. Demazure, *Lectures on `p`-divisible groups*, Lect. Notes Math. **302**, Springer-Verlag, 1972.

[Di55] J. Dieudonné, *Groupes de Lie et hyperalgèbres de Lie sur un corps de caractéristique `p > 0`*, Comm. Math. Helv.
**28** (1955), 87–118.

[Di73] J. Dieudonné, *Introduction to the theory of formal groups*, Marcel Dekker, 1973.

[Fo77] J.-M. Fontaine, *Groupes `p`-divisibles sur les corps locaux*, Astérisque **47–48**, Soc. Math. France, 1977.

[Gr57] A. Grothendieck, *Sur quelques points d'algèbre homologique*, Tôhoku Math. J. **9** (1957), 119–221.

[Gr74] A. Grothendieck, *Groupes de Barsotti–Tate et cristaux de Dieudonné*, Presses Univ. Montréal, 1974.

[HS69] R. G. Heyneman, M. E. Sweedler, *Affine Hopf Algebras I*, J. Algebra **13** (1969), 194–241.

[Il85] L. Illusie, *Déformations de groupes de Barsotti–Tate, d'après A. Grothendieck*, pp. 151–198 in: *Séminaire sur
les pinceaux arithmétiques: la conjecture de Mordell*, Astérisque **127**, Soc. Math. France, 1985.

[Ja65] I. M. James, review of [MM65] in *Math. Reviews*, MR0174052.

[La75] M. Lazard, *Commutative formal groups*, Lect. Notes Math. **443**, Springer-Verlag, 1975.

[LT65] J. Lubin, J. Tate, *Formal complex multiplication in local fields*, Ann. of Math. **81** (1965), 380–387.

[LT66] J. Lubin, J. Tate, *Formal moduli for one-parameter formal Lie groups*, Bull. Soc. Math. France **94** (1966),
49–60.

[Ma91] A. Masuoka, *On Hopf algebras with cocommutative coradicals*, J. Algebra **144** (1991), 451–466.

[Me72] W. Messing, *The crystals associated with Barsotti–Tate Groups: with applications to abelian schemes*, Lect.
Notes Math. **264**, Springer-Verlag, 1972.

[MM65] J. W. Milnor, J. C. Moore, *On the structure of Hopf algebras*, Ann. of Math. **81** (1965), 211–264.

[Mi65] B. Mitchell, *Theory of categories*, Academic Press, 1965.

<!-- original page 601 -->

[Ne75] K. Newman, *A correspondence between bi-ideals and sub-Hopf algebras in cocommutative Hopf algebras*, J. Algebra
**36** (1975), 1–15.

[Po73] N. Popescu, *Abelian categories with applications to rings and modules*, Academic Press, 1973.

[Sch90] H. J. Schneider, *Principal homogeneous spaces for arbitrary Hopf algebras*, Israel J. Math. **72** (1990), nos.
1–2, 167–195.

[Sw67] M. Sweedler, *Hopf algebras with one grouplike element*, Trans. Amer. Math. Soc. **127** (1967), no. 3, 515–526.

[Sw69] M. Sweedler, *Hopf algebras*, Benjamin, 1969.

[Tak72] M. Takeuchi, *A correspondence between Hopf ideals and sub-Hopf algebras*, Manuscripta Math. **7** (1972),
251–270.

[Tak79] M. Takeuchi, *Relative Hopf modules—Equivalence and freeness criteria*, J. Algebra **60** (1979), 452–471.

[Ta67] J. Tate, *`p`-divisible groups*, pp. 158–183 in: *Proc. Conf. Local Fields* (Driebergen, 1966) (ed. T. A.
Springer), Springer-Verlag, 1967.

[We95] C. A. Weibel, *An introduction to homological algebra*, Cambridge Univ. Press, 1995.

<!-- LEDGER DELTA — Exposé VII_B — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| morphisme de Frobenius | Frobenius morphism | Chunk-C uses `Fr(X/k)` (and `Fr^n`, `Fr_n G`) per source; "absolute Frobenius" = `fr(S)`. |
| groupe formel de hauteur ⩽ n | formal group of height ⩽ n | Per 4.1.2 (b). |
| algèbre enveloppante restreinte | restricted enveloping algebra | `U_p(L)`; for `p`-Lie algebras. |
| formule de Campbell-Hausdorff | Campbell–Hausdorff formula | En-dash between names. |
| Γ-algèbre de Lie | `Γ`-Lie algebra | Triple `(L, M, φ)` with Galois action; new in §3.3.3. |
| théorème de Cartier-Gabriel-Kostant | Cartier–Gabriel–Kostant theorem | En-dashes throughout; cf. 2.9.2, 3.3.3. |
| théorème de Cartier-Kostant-Milnor-Moore | Cartier–Kostant–Milnor–Moore theorem | En-dashes; cf. N.D.E. 3.3.2. |
| théorème de Dieudonné-Cartier | Dieudonné–Cartier theorem | En-dash; §5.2 main theorem. |
| algèbre profinie graduée | graded profinite algebra | Per 5.1.2; category `Alpg/k`. |
| cogroupe | cogroup | Object of `**C**` with compatible formal group structure on `Spf(A)`; cf. 5.1.1. |
| coproduit (au lieu de "somme directe") | coproduct | Per N.D.E. in 5.1.2; replacing the original "somme directe". |
| produit semi-direct (de cogroupes) | semi-direct coproduct | Per 5.1.3; structural decomposition of graded cogroups. |
| complété formel `Ĝ_H` le long de `H` | formal completion `Ĝ_H` along `H` | Per N.D.E. in 5.1.2. |
| algèbre de séries formelles tronquée | truncated formal power series algebra | Per 5.2; `B_r = k[[ω]]/((x^{p^r}))`. |
| espace vectoriel pseudocompact | pseudocompact vector space | Replaces the source's "linearly compact" per N.D.E. 5.2; for consistency. |
| pseudobase | pseudobasis | Basis in `PC(k)`; standard chunk-A usage retained. |
| stationnaire (algèbre) | stationary (algebra) | Per 5.3; N.D.E. flags that "stable" would be preferable. |
| intersection complète | complete intersection | Per 5.5.1, EGA IV₄ 19.3.1. |
| immersion régulière | regular immersion | Per 5.5; cf. EGA IV₄ 16.9.10. |
| « théorème de Dieudonné » | "Dieudonné's theorem" | Per 5.5.2 b); compare with [Di55] § 19. |
| `^p√0_C` | `^p√0_C` | Ideal of `p`-nilpotent elements; per 4.3.1. |
| ((x^{p^r}))_{x ∈ r(B)} | `((x^{p^r}))_{x ∈ 𝔯(B)}` | Closed ideal generated by `p^r`-th powers of radical elements; per 5.2. |
| Alpg/k | `Alpg/k` | Category of graded profinite `k`-algebras; per 5.1.2. |
| Fr_n G | `Fr_n G` | Kernel of iterated Frobenius; per 4.1.2 (a). |
| « hauteur infinie » | infinite height | Per 5.2.5. |
| catégorie `**C**` (algèbre profinie + idéal fermé) | category `**C**` (profinite algebra + closed ideal) | Per 5.1.1. |
| HG_1 | `H G_1` | Inverse image of `H^{(p)}` under Frobenius; per 5.2.3. |
-->

[^N.D.E-VII_B-0]: N.D.E.: Version of 13/10/2024.

[^N.D.E-VII_B-1]: N.D.E.: The interest of formal groups over a complete noetherian local ring appears, for example, in
    the work of Lubin and Tate (cf. [LT65]). The study of formal groups over an arbitrary base, and
    questions of lifting and deformation, in particular for Barsotti–Tate groups ("`p`-divisible groups"),
    has given rise to an abundant literature; cf. for example \[LT66, Ta67, Gr74, Me72, La75, Fo77, Il85,
    Br00\]. In particular, the results of the present Exposé are largely taken up again in Chapter I of
    [Fo77].

[^N.D.E-VII_B-2]: N.D.E.: The editors have found only such a seminar dated 1965/66, entitled "Linear algebraic groups",
    in which the notion of formal group does not appear; see instead [De72].

[^N.D.E-VII_B-3]: N.D.E.: (when endowed with the `𝔪`-adic topology).

[^N.D.E-VII_B-4]: N.D.E.: Indeed, if `x ∉ I`, there exists an open ideal `𝓁` such that `(x + 𝓁) ∩ I = ∅`, and then
    `I + 𝓁` is an open ideal not containing `x`. On the other hand, in what follows, we have made explicit
    the fact that every "closed maximal" ideal is maximal and open.

[^N.D.E-VII_B-5]: N.D.E.: We note that `A_𝔪` is the localization of `A` at the maximal ideal `𝔪`. Indeed, the unit
    element `e_𝔪` of `A_𝔪` is an idempotent of `A` not belonging to `𝔪`, and since `A = A_𝔪 × B`, where
    `B = A(1 − e_𝔪)`, then `A_𝔪` is identified with the localization `A_{e_𝔪}` and thus also with the
    localization `S^{-1} A`, where `S = A − 𝔪`. On the other hand, since `e_𝔪(1 − e_𝔪) = 0`, then `𝔪`
    contains `1 − e_𝔪` and hence also `B`, and so `𝔪` is identified with `𝔪 A_𝔪 × B`.

[^N.D.E-VII_B-6]: N.D.E.: Indeed, let `x ∈ r(A)`; if `𝔪` is a maximal ideal not containing `x`, there exists `y ∈ A`
    such that `1 − xy ∈ 𝔪`, and since `xy ∈ r(A)`, `1 − xy` is invertible, whence a contradiction. We note
    the following consequence: if `Υ(A)` is a finite set `{𝔪₁, …, 𝔪_r}`, the `𝔪_i` are all the maximal
    ideals of `A`.

[^N.D.E-VII_B-7]: N.D.E.: We have added these remarks, in order to be able to compare the definition of the formal
    spectrum `Spf(A)` given in 1.1 with those of (EGA I, 10.1.2) and (EGA I, 10.4.2).

[^N.D.E-VII_B-8]: N.D.E.: We have brought out the results of this paragraph in the proposition that follows, and have
    indicated below the steps of the proof; cf. [CA], § IV.3 or [DG70], § V.2.

[^N.D.E-VII_B-9]: N.D.E.: cf. [Gr57], I § 1.5 and Prop. 1.8; one may also consult, for example, [Po73], § 2.8 or [We95],
    Append. A.4.

[^N.D.E-VII_B-10]: N.D.E.: We have inserted into this paragraph Proposition 0.2.E and Corollary 0.2.F, which will be
    useful in 0.2.2. (In the original, these results appeared in 0.3.)

[^N.D.E-VII_B-11]: N.D.E.: Indeed, `PC(A)` has a set of artinian cogenerators, filtered inverse limits in it are exact,
    and `LF(A)` is the subcategory of artinian objects. The dual category `PC(A)°` therefore has a set of
    noetherian generators, and filtered direct limits in it are exact. By the proof of [CA] § II.4, th.
    1, the functor `M ↦ Hom_c(M, −)` is an anti-equivalence of `PC(A)` with `Lex(LF(A), (Ab))`. Likewise,
    Lemma 4 and Cor. 1 of *loc. cit.* state results "dual" to those of Corollary 0.2.F. For a "direct"
    proof, see [DG70], § V.2, th. 3.1, Lemma 3.5, Cor. 3.3 & 3.4.

[^N.D.E-VII_B-12]: N.D.E.: As every infinite product is a filtered inverse limit of finite products, every additive
    functor that commutes with filtered inverse limits also commutes with infinite products.

[^N.D.E-VII_B-13]: N.D.E.: This refers to the "dual" statements established in *loc. cit.*, § 2, Th. 2 and § 1, Prop. 2;
    for a "direct" proof, see [DG70], V, § 2, Th. 4.5 and Example 4.6 b).

[^N.D.E-VII_B-14]: N.D.E.: We have detailed the results of this paragraph, which play an important role in what follows
    (cf. 1.2.3, 1.3.5, 2.2.1, etc.).

[^N.D.E-VII_B-15]: N.D.E.: Recall on the other hand that, over an artinian ring, a module is projective if and only if
    it is flat; see for example (VI_B, N.D.E. (54)) or 0.3.7 below.

[^N.D.E-VII_B-16]: N.D.E.: One will note that the direct sum in `PC(k)` of a family `(V_i)_{i ∈ I}` of linearly compact
    `k`-vector spaces is `(∏_{i ∈ I} V_i^†)^*`.

[^N.D.E-VII_B-17]: N.D.E.: We have modified this paragraph, taking into account the additions made in 0.2.

[^N.D.E-VII_B-18]: N.D.E.: We have added this corollary.

[^N.D.E-VII_B-19]: N.D.E.: We have added this remark.

[^N.D.E-VII_B-20]: N.D.E.: Up to replacing `𝔞` by its closure, one can assume `𝔞` closed.

[^N.D.E-VII_B-21]: N.D.E.: since equal to the inverse limit of the `M/M' = 0`.

[^N.D.E-VII_B-22]: N.D.E.: Consequently, every pseudocompact `A`-module is a quotient of a topologically free `A`-module
    (one first reduces to the case where `A` is local), cf. the proof of 0.3.7.

[^N.D.E-VII_B-23]: N.D.E.: We have corrected `N/𝔪 N` to `N / 𝔪̄ N`, and likewise for `M/𝔪 M` below.

[^N.D.E-VII_B-24]: N.D.E.: One thus recovers 0.3.1.1: `L = L ⊗̂_A A = L ⊗̂_A lim_𝓁 (A/𝓁) ≃ lim_𝓁 L/𝓁 L`, where `𝓁`
    ranges over the open ideals of `A`.

[^N.D.E-VII_B-25]: N.D.E.: cf. N.D.E. (12).

[^N.D.E-VII_B-26]: N.D.E.: We have added this remark, which will be useful in 2.3.1.

[^N.D.E-VII_B-27]: N.D.E.: This shows the result announced in N.D.E. (22): every pseudocompact `A`-module `M` is a
    quotient of a topologically free `A`-module. (Since products are exact in `PC(A)`, one reduces to the
    case where `A` is local, treated above.)

[^N.D.E-VII_B-28]: N.D.E.: A fully analogous proof, using "nilpotent Nakayama's Lemma", shows that if `A` is artinian
    and `P` is a flat `A`-module, then each local component of `P` is a free `A`-module (cf. [BAC], II §
    3.2, cor. 2 of prop. 5).

[^N.D.E-VII_B-29]: N.D.E.: We have added the following lemma, cf. N.D.E. (36) in Proposition 0.5.

[^N.D.E-VII_B-30]: N.D.E.: We will see in 0.4.2 that it possesses arbitrary direct limits.

[^N.D.E-VII_B-31]: N.D.E.: Caution: `k` is an object of `Alf/k` only if `k` is artinian, cf. 1.2.2 below.

[^N.D.E-VII_B-32]: N.D.E.: i.e., which commutes with finite inverse limits.

[^N.D.E-VII_B-33]: N.D.E.: Indeed, every discrete `k`-module of length `n` is isomorphic to `k^n / L`, where `L` is an
    open submodule of `k^n` of colength `n`. One can then consider the set of (isomorphism classes of)
    profinite `k`-algebra structures on each such module.

[^N.D.E-VII_B-34]: N.D.E.: If `(A_i)_{i ∈ I}` is a direct system in `Alp/k`, its direct limit in `Alp/k` is the
    separated completion of the `k`-algebra `B`, direct limit of the underlying `k`-algebras, for the
    topology defined by the ideals `I` such that `I ∩ A_i` is an open ideal of `A_i` for every `i`, and
    `length_k(B/I) < ∞`. Note that if, for example, `K/k` is an algebraic extension of fields, of
    infinite degree, and if `(k_i)` denotes the filtered direct system of subextensions of finite degree,
    then the direct limit of the system `(k_i)` in `Alp/k` is the zero ring!

[^N.D.E-VII_B-35]: N.D.E.: We have detailed this paragraph.

[^N.D.E-VII_B-36]: N.D.E.: Consequently, if `ℓ` is a profinite `k`-algebra, the functor `M ↦ M ⊗̂_k ℓ` is left adjoint
    to the restriction-of-scalars functor.

[^N.D.E-VII_B-37]: N.D.E.: cf. Remarks 0.1.2.

[^N.D.E-VII_B-38]: N.D.E.: We have added the numbering 1.2.A to 1.2.E, for later references.

[^N.D.E-VII_B-39]: N.D.E.: We note that, by the definition of morphisms (1.1), every `X ∈ Ob Vaf/k` is the direct sum in
    `Vaf/k` of the pointwise formal varieties `Spf(O_{X,x})`, for `x ∈ X`.

[^N.D.E-VII_B-40]: N.D.E.: In particular, cokernels exist in `Vaf/k`, see below. We note moreover that a filtered
    inverse limit in `Vaf/k`, all of whose transition morphisms are surjective, can be empty, cf. N.D.E.
    (34).

[^N.D.E-VII_B-41]: N.D.E.: We note that `Y ×_X Z` is the direct sum, for `x ∈ X`, of the formal varieties
    `B_x ⊗̂_{O_{X,x}} C_x`, where `B_x` is the product of the `O_{Y,y}` for `y ∈ Y` such that `f(y) = x`,
    and `C_x` is defined analogously. This will be used in 2.5.1.

[^N.D.E-VII_B-42]: N.D.E.: i.e., the quotient set of `Y` by the identifications `d(x) = e(x)`, for every `x ∈ X`,
    endowed with the quotient topology, which is here the discrete topology.

[^N.D.E-VII_B-43]: N.D.E.: We have introduced this terminology, cf. N.D.E. (47) in 1.2.3.

[^N.D.E-VII_B-44]: N.D.E.: and hence projective, since `C` is artinian.

[^N.D.E-VII_B-45]: N.D.E.: We have added the lemma that follows and have introduced the numbering 1.2.3.A to 1.2.3.F,
    for later references.

[^N.D.E-VII_B-46]: N.D.E.: In fact, we shall not use this second notation, see N.D.E. (47).

[^N.D.E-VII_B-47]: N.D.E.: The editors do not understand the following definition if `**M**` is not assumed admissible,
    whence the addition of this hypothesis. On the other hand, we have written `Γ^*(**M**)` instead of
    `**M**^*`, in order to avoid confusions between `M^*`, the dual module of the functor `**M**`, and
    `**N**^†`, the dual functor of the module `N`, cf. N.D.E. (46). Finally, we have detailed the
    construction of `Γ^*(**M**)`.

[^N.D.E-VII_B-48]: N.D.E.: We have added point (ii) below, as well as the proof that follows. The original stated: "If
    `**M**` is a flat `O_k`-module, it is clear that `**M**` is nothing other than the dual of `**M**^*`,
    so the functors `N ↦ **N**^*` and `**M** ↦ **M**^*` define an anti-equivalence…"

[^N.D.E-VII_B-49]: N.D.E.: In this paragraph, we have modified the order, by first defining `Ŝ_k(E)` and then stating
    that `**V^f_k**(E)` represents `**V_k^f**(E)`.

[^N.D.E-VII_B-50]: N.D.E.: For example, let `k` be a field, `E` a pseudocompact `k`-vector space, `V = Hom_c(E, k)`; one
    has `E ≃ V^*` (cf. 0.2.2). For every finite-dimensional subspace `W` of `V`, let `F(W)` be the set of
    closed points of the `k`-scheme `V(W) = Spec S_k(W^*)`. Denote by `F(V)` the direct limit of the
    `F(W)`. Then `Ŝ_k(E)` is the product, for `x ∈ F(V)`, of the pseudocompact `k`-algebras
    `Ŝ_k(E)_x = lim_W Ô_{W, x}`, where `W` ranges over the finite-dimensional subspaces of `V` such that
    `x ∈ F(W)`, and `Ô_{W, x}` denotes the separated completion of the local ring `O_{V(W), x}` for the
    topology defined by the ideals of finite codimension (which here coincides with the `𝔪`-adic
    topology). If `k` is algebraically closed and `(v_i)_{i ∈ I}` a basis of `V`, so that `E` possesses a
    pseudobasis `(e_i)_{i ∈ I}`, then each local component `Ŝ_k(E)_x` is isomorphic to the ring of formal
    series `k[[e_i, i ∈ I]]`, endowed with the topology defined by the ideals of finite codimension.

[^N.D.E-VII_B-51]: N.D.E.: We have detailed the rest of this paragraph.

[^N.D.E-VII_B-52]: N.D.E.: We have added the following sentence.

[^N.D.E-VII_B-53]: N.D.E.: We have amplified the following proposition by inserting in it the fact that the functor
    `X ↦ X̂/Ŝ` commutes with finite inverse limits (in the original, this appeared in the proof of 1.3.4
    — the proof given here is more direct than the original). Moreover, this result will be useful in
    Section 2 and in 3.3.1.

[^N.D.E-VII_B-54]: N.D.E.: We have detailed the beginning of the proof.

[^N.D.E-VII_B-55]: N.D.E.: We have added this remark.

[^N.D.E-VII_B-56]: N.D.E.: i.e., in the opposite category `(Vaf/k)° = Alp/k`, the morphism `g : B → A` corresponding to
    `f` is an effective epimorphism. This is the case, because `g` is surjective, hence induces (cf. the
    proof of 0.2.B) an isomorphism of profinite `k`-algebras `B/I ⥲ A`, where `I = Ker g`. Consequently,
    every morphism `φ : B → C` of `Alp/k` that is zero on `I` descends to a morphism `φ̄ : A → C` such
    that `φ = φ̄ ∘ g`.

[^N.D.E-VII_B-57]: N.D.E.: i.e., let `k` be a field, `X = Spf(k[[T]])` and `Y = Spf(B)`, where `B` is the `k`-subalgebra
    of `A = k[[T]]` generated topologically by `T^3` and `T^4` (i.e., `B` is formed by the formal series
    `∑ a_n T^n` such that `a_n = 0` for `n = 1, 2, 5`). Then `X → Y` is an epimorphism that is not
    effective; indeed, the cokernel of `X ×_Y X ⇒ X` is `Spf(B')`, where `B'` is the subalgebra of `A`
    formed by the `a` such that `a ⊗̂ 1 = 1 ⊗̂ a`, and `B'` contains `T^5`.

[^N.D.E-VII_B-58]: N.D.E.: We have added this lemma, which explains the terminology "topologically flat".

[^N.D.E-VII_B-59]: N.D.E.: We have detailed what follows; then we have taken advantage of the addition made in 1.2.6.

[^N.D.E-VII_B-60]: N.D.E.: We have added the following lemma, used implicitly in the original; on the other hand, we
    have introduced the numbering 1.3.5.A to 1.3.5.D, for later references.

[^N.D.E-VII_B-61]: N.D.E.: We have detailed what follows.

[^N.D.E-VII_B-62]: N.D.E.: In Lemma 1.3.6.A that follows, we have detailed the proof of points (i) and (ii), and have
    added point (iii).

[^N.D.E-VII_B-63]: N.D.E.: For example, let `k_0` be a field, `k = k_0[T]/(T^n)`, where `n ⩾ 4`, `H = k φ ⊕ k x`, with
    `ε(x) = 0` and `Δ(x) = x ⊗ φ + φ ⊗ x + t x ⊗ x`, where `t` is the image of `T` in `k`. Then
    `H_i = k φ ⊕ t^{n-i} x` for `i = 0, …, n`, but for `2 ⩽ i ⩽ n - 2`, `Δ(t^{n-i} x)` does not belong to
    the image of `H_i ⊗ H_i` in `H ⊗ H`.

[^N.D.E-VII_B-64]: N.D.E.: In this case, one says that the coalgebra `H` is *connected*, cf. the addition 2.9.

[^N.D.E-VII_B-65]: N.D.E.: This also holds without assuming `H` cocommutative (`k` remaining a commutative artinian
    ring): in this case, a basis of neighborhoods of `0` in `A = H^*` is given by the two-sided ideals
    `J` such that `A/J` is of finite length over `k`, and the preceding proof shows that
    `H = ⋃_n (I^n)^⊥` if and only if the `Φ^{-1}(𝔪_i)` are the only open prime ideals of `A`.

[^N.D.E-VII_B-66]: The following has been added; the original was limited to the case where `k` is artinian.

[^N.D.E-VII_B-67]: One may therefore suppose `k` local.

[^N.D.E-VII_B-68]: cf. Exp. V, § 2.b).

[^N.D.E-VII_B-70]: The original continued thus: "A formal variety `X` over `k` is said to be étale if the diagonal
    morphism `∆_X : X → X × X` is a local isomorphism, that is, if `∆_X` induces an isomorphism of
    `O_{X×X, ∆_X(x)}` onto `O_{X,x}` for every point `x` of `X`. One sees easily with the aid of SGA I
    that this formulation is equivalent to the following two: the formal variety `X` is topologically
    flat, and, for every point `x ∈ X`, of projection `s ∈ Spf(k)`, `O_{X,x} ⨶_k κ(s)` is a finite
    separable extension of the residue field `κ(s)` of `s`; or also, if `A` denotes the affine algebra of
    `X`, the local components (0.1) of `A ⨶_k (k/l)` are finite étale algebras over `k/l`, for every open
    ideal `l` of `k`." In what follows, we have rectified the omission of the flatness hypothesis in the
    first condition above, and detailed the equivalence of the said conditions.

[^N.D.E-VII_B-71]: Let us point out in passing that the proof given in EGA 0\_{IV}, 19.3.5 (v) is erroneous.

[^N.D.E-VII_B-72]: Note that `Vaf^ét_/k` is stable under finite inverse limits.

[^N.D.E-VII_B-74]: We have inserted this remark here, which in the original appeared in 2.5.2.

[^N.D.E-VII_B-75]: This is the case for finite inverse limits.

[^N.D.E-VII_B-76]: One will also say that `A` is a *cogroup* in the category of profinite `k`-algebras. On the other
    hand, we have detailed what follows; in particular, we have made explicit what a morphism of formal
    groups `K → G` is, cf. Proposition 2.3.1.

[^N.D.E-VII_B-77]: One also says *bigèbre* (cf. [BAlg], III § 11.4); recall (cf. VII_A, 3.1, N.D.E. (26)) that all the
    "bialgebras" considered here are assumed cocommutative and equipped with an antipode, i.e., they are
    in fact cocommutative Hopf algebras.

[^N.D.E-VII_B-78]: Since `∆(x) = x ⊗ x` one has `x = ε(x)x`, hence `ε(x) = 0` can occur only if `x = 0`.

[^N.D.E-VII_B-79]: We have detailed the original in what follows.

[^N.D.E-VII_B-80]: We have added the adjective "covariant" to make it visible that the functor `G ↦ H(G)` is covariant;
    this terminology is used in [Di73], I § 2.14.

[^N.D.E-VII_B-81]: Recall that in this Exposé, "bialgebra" means "cocommutative Hopf algebra".

[^N.D.E-VII_B-82]: We have introduced here the notation `H^cocom_{flat/k}`, which will be useful below.

[^N.D.E-VII_B-83]: We have detailed the original in what follows, in order to introduce the notations `D'(G)` and
    `D(K)`, cf. [Ca62], § 14.

[^N.D.E-VII_B-84]: If one denotes by `ℱ𝒞^f_k` (resp. `𝒜𝒞^f_k`) the full subcategory of `ℱ𝒞_k` (resp. `𝒜𝒞_k`) formed by
    the objects `G` (resp. `T`) such that `H(G)` (resp. `O(T)`) is a finite `k`-module (and hence finite
    locally free), then `ℱ𝒞^f_k` and `𝒜𝒞^f_k` both have the same objects as the category `𝒞` of
    commutative and cocommutative Hopf `k`-algebras, finite and flat over `k`, the correspondence
    `G ↦ H(G)` (resp. `T ↦ O(T)`) being covariant (resp. contravariant), and one thus recovers the
    "Cartier duality" of the category `𝒜𝒞_k`, already seen in VII_A, 3.3.1.

[^N.D.E-VII_B-85]: That is, not necessarily topologically flat over `k`.

[^N.D.E-VII_B-86]: We have modified the order of the sentences in what follows.

[^N.D.E-VII_B-88]: We have added the preceding sentence, and in what follows we have denoted `W(U)×` instead of `U_m`.
    Recall on the other hand (cf. 1.2.1) that one calls "`k`-functor" a covariant functor
    `Alf_/k → (Ens)`.

[^N.D.E-VII_B-89]: The original indicated: "(this) follows from the functorial character of `ψ_A`". We have detailed
    this in what follows.

[^N.D.E-VII_B-90]: We have detailed the original in what follows.

[^N.D.E-VII_B-91]: We have made this corollary explicit, since it is used, for example, in 5.2.1/5.2.3.

[^N.D.E-VII_B-93]: cf. IV, 5.2.6.

[^N.D.E-VII_B-94]: See also the remarks following VI_A, 5.4.3.

[^N.D.E-VII_B-95]: Note that if `[κ_s : κ] = ∞`, `κ_s` is not a profinite `κ`-algebra, so the preceding notation is an
    abuse of notation. On the other hand, we have detailed the original in what follows.

[^N.D.E-VII_B-96]: We have added this remark.

[^N.D.E-VII_B-97]: We have detailed the original in what follows.

[^N.D.E-VII_B-98]: We have added the following sentence.

[^N.D.E-VII_B-99]: We have detailed what follows.

[^N.D.E-VII_B-100]: The same argument shows also that, for an arbitrary field `k`, if all the residue fields of `G`
    equal `k`, then `G_e` is the constant `k`-group `(M)_k`, where `M = G(k) = Spf* H(G)`, and `H(G)` is
    the semi-direct product of `H(G⁰)` by the group algebra `kM`, cf. the addition 2.9 further below.

[^N.D.E-VII_B-101]: We have added this remark.

[^N.D.E-VII_B-102]: `α_{p,k}`, `(ℤ/pℤ)_k` and `G_λ` are also `k`-algebraic groups, finite and flat over `k`, cf. N.D.E.
    (84) in 2.2.2.

[^N.D.E-VII_B-104]: This coincides with the "usual" notion of unipotent `k`-group scheme, cf. the addition 2.8 at the
    end of Section 2.

[^N.D.E-VII_B-105]: The original indicated: "let us say that a commutative `k`-group scheme is of multiplicative type if
    it is isomorphic to `Spec H(G)`, where `G` is an étale commutative `k`-formal group." We have given
    here the "usual" definition, drawn from Exp. IX, 1.1, and we have shown its equivalence with the
    preceding condition; see also [DG70], § IV.1, Th. 2.2.

[^N.D.E-VII_B-106]: We have added point (iii), a consequence of Proposition 2.5.

[^N.D.E-VII_B-107]: Indeed, `δ ∘ f = ε_A` entails `f(1) = 1 + λd`, with `λ ∈ k`, and then `f(1) = f(1)² = 1 + 2λd` gives
    `λ = 0`.

[^N.D.E-VII_B-108]: Comparing with VII_A 2.5, one sees that if `K` is a `k`-group scheme of finite type and if `G` is
    the formal completion of `K` at the origin (i.e., `𝒜(G)` is the completion of the local ring
    `O_{K,e}` for the `m`-adic topology, where `m` is the kernel of the augmentation `ε : O_{K,e} → k`),
    then `H(G)` is identified with the algebra of distributions `U(K)`, and `Lie(G)` with `Lie(K)`. (The
    condition that `K` be of finite type over `k` is used to ensure that `m/m²` is a `k`-module of
    finite length, hence discrete, so that its topological dual coincides with its ordinary dual.) In
    particular, when `G` is a finite `k`-formal group (i.e., such that `𝒜(G)` is a finite `k`-module),
    in which case `G` may also be considered as the `k`-group scheme `Spec 𝒜(G)`, the two definitions of
    `Lie(G)` coincide.

[^N.D.E-VII_B-109]: We have detailed the original in what follows.

[^N.D.E-VII_B-110]: We have highlighted points (i) and (ii), and added point (iii), which will be useful in 2.6.3 and
    3.3.2.

[^N.D.E-VII_B-111]: We have modified what follows, taking advantage of the addition made in 2.6.2.

[^N.D.E-VII_B-112]: Here and in what follows, we have written "monoid" instead of "monoid with unit element" (recall
    that a monoid is by definition a set endowed with an associative composition law and possessing a
    unit element).

[^N.D.E-VII_B-113]: By the equivalence of categories 1.3.5.D, a monoid in the category of topologically flat `k`-formal
    varieties "is the same thing" as a monoid in the category of cocommutative flat `O_k`-coalgebras,
    i.e., a cocommutative `O_k`-bialgebra (in the usual sense, i.e., not necessarily equipped with an
    antipode). Moreover, by 1.3.6, the hypothesis that `M` be infinitesimal is equivalent to saying that
    the corresponding bialgebra is connected. So, if `k` is an artinian ring, the proposition is
    equivalent to saying that: every cocommutative connected `k`-bialgebra, flat over `k`, is a `k`-Hopf
    algebra, i.e., possesses an antipode (and the cocommutativity hypothesis is in fact superfluous, cf.
    the proof).

[^N.D.E-VII_B-114]: The original continued thus: "one shows then easily, by induction on `n`, that there exists one and
    only one linear map `c_n : U_n → U_n` such that the composite map
    `m_U ∘ (c_n ⊗ id_U) ∘ ∆_U : U⁺_n → U` be zero"; we have detailed the proof, which rests on that of
    Lemma 1.3.6.A.

[^N.D.E-VII_B-116]: Recall that a two-sided ideal `P` of a ring `A` is called *prime* if in `A/P` the product of two
    nonzero two-sided ideals is nonzero.

[^N.D.E-VII_B-117]: This is also equivalent to saying that `k · 1_{O(G)}` is the unique simple `k`-subcoalgebra of
    `O(G)`; see for example [Ab80], 3.1.4. Let us point out in passing a misprint in loc. cit., p. 130,
    line 4: `M ≃ C*/ann M` is to be replaced by `C*/ann M ≃ End_k(M)`.

[^N.D.E-VII_B-119]: If `x, x' ∈ rU` commute, one has therefore `exp_U(x + x') = (exp_U x)(exp_U x')`.

[^N.D.E-VII_B-120]: That is, for every morphism `φ : U → V` of `C`-algebras, one has `φ(exp_U(x)) = exp_V φ(x)`.

[^N.D.E-VII_B-121]: We have detailed what precedes and added the following sentence.

[^N.D.E-VII_B-122]: We have added the condition `ε_U(z) = 1`, omitted in the original.

[^N.D.E-VII_B-123]: We have added point (ii), an immediate consequence of 3.1.

[^N.D.E-VII_B-124]: We have corrected the formula given, which was erroneous, and added the reference [BLie].

[^N.D.E-VII_B-125]: We have removed the hypothesis that `k` be local (the proof reduces to this case).

[^N.D.E-VII_B-126]: cf. 5.1.5 further below; see also [BAC], III, § 2.8, Th. 1 and corollaries. On the other hand, we
    have detailed the original in what follows.

[^N.D.E-VII_B-127]: We have detailed the original in what follows.

[^N.D.E-VII_B-128]: We do not know a priori that `ω` is a projective pseudocompact `k`-module, but this will follow from
    what follows: compare with the proof of (iv) ⇒ (iii) in VII_A, 7.4.

[^N.D.E-VII_B-C-11]: N.D.E.: We have added the flatness hypothesis, omitted in the original.

[^N.D.E-VII_B-C-12]: N.D.E.: We have detailed the original in what follows.

[^N.D.E-VII_B-C-13]: N.D.E.: Since, by 2.7, 2.2.1 and 1.3.6, an infinitesimal `k`-formal group `G` is "the same thing"
    as a connected cocommutative `k`-bialgebra `H` (cf. 2.9), this statement is equivalent to the
    theorem below, obtained independently by Kostant (cf. 2.9.2). This theorem had been obtained
    earlier by J. W. Milnor and J. C. Moore ([MM65]), under the additional hypothesis that `H` is
    generated as an algebra by its primitive elements (although published in 1965, this text had
    circulated before 1960, cf. the review [Ja65]), so that it is often called the
    "Cartier–Kostant–Milnor–Moore theorem".

    **Theorem (Cartier–Kostant–Milnor–Moore).** *Let `k` be a field of characteristic 0. The functors `L ↦ U(L)` and
    `H ↦ Prim(H)` define an equivalence between the category of `k`-Lie algebras and that of connected cocommutative
    `k`-bialgebras.*

    On the other hand, if `k` is an artinian ring containing `ℚ`, then 3.2 (ii) and 3.3 (combined with 2.7, 2.2.1 and
    1.3.6) similarly show that the functor `L ↦ **G**(L)` (resp. `L ↦ U(L)`) is an equivalence of the category of flat
    `k`-Lie algebras onto that of infinitesimal `k`-formal groups topologically flat (resp. onto that of connected
    cocommutative `k`-bialgebras that are flat).

[^N.D.E-VII_B-C-14]: N.D.E.: The original stated: "This `k`-functor is manifestly left exact (`H` is topologically flat
    over `k`!)". We have detailed this in what follows.

[^N.D.E-VII_B-C-15]: N.D.E.: In particular, when `k̄ = k`, one thus recovers the "Cartier–Gabriel–Kostant theorem"
    mentioned in 2.9.2.

[^N.D.E-VII_B-C-16]: N.D.E.: We have corrected the original, which gave the inclusion `(X̂/Ŝ)^{(p)} ⊂ X̂^{(p)}/Ŝ`
    instead of the opposite inclusion. Let us point out moreover that this paragraph is not used in the
    sequel.

[^N.D.E-VII_B-C-17]: N.D.E.: We have detailed what follows.

[^N.D.E-VII_B-C-18]: N.D.E.: The proof is identical to that of 2.6.3.

[^N.D.E-VII_B-C-19]: N.D.E.: We have added the hypothesis that `k` be local, so that every topologically flat
    pseudocompact `k`-module be topologically free; cf. the proof.

[^N.D.E-VII_B-C-20]: N.D.E.: We have detailed the original in what follows.

[^N.D.E-VII_B-C-21]: N.D.E.: We have added this remark, used in 4.4.2.

[^N.D.E-VII_B-C-22]: N.D.E.: If `k` is an artinian ring of characteristic `p > 0`, the same proof gives an equivalence
    between the category of `p`-Lie algebras that are flat over `k` and that of `k`-formal groups of
    height `⩽ 1`, topologically flat over `k`.

[^N.D.E-VII_B-C-23]: N.D.E.: We have detailed the original in what follows.

[^N.D.E-VII_B-C-24]: N.D.E.: We have added subsection 5.0, in order to express in the language of cocommutative Hopf
    algebras the proposition 5.1 that follows, and to cite the results obtained since in this
    direction.

[^N.D.E-VII_B-C-25]: N.D.E.: In the original, it is supposed in 5.1 that `k` is a field. In fact, this hypothesis can be
    replaced by flatness hypotheses; we have modified accordingly nos. 5.1 to 5.1.5.

[^N.D.E-VII_B-C-26]: N.D.E.: We have replaced "left" by "right" and have modified the statement of Proposition 5.1, in
    order to bring out more clearly, on the one hand, the equivalent conditions (i), (ii), and, on the
    other hand, the conclusion `Spf(B) ≃ G/H`.

[^N.D.E-VII_B-C-27]: N.D.E.: Note that if `(A′, J′)` is a second cogroup of `**C**`, corresponding to a pair `H′ ⊂ G′`
    of `k`-formal groups, then to give a morphism of cogroups `(A′, J′) → (A, J)` amounts to giving a
    morphism of `k`-formal groups `G → G′` that sends `H` into `H′`.

[^N.D.E-VII_B-C-28]: N.D.E.: We have replaced "direct sum" by "coproduct".

[^N.D.E-VII_B-C-29]: N.D.E.: In the original, the lemma is stated when `k` is a field, the proof in this case being left
    to the reader.

[^N.D.E-VII_B-C-30]: N.D.E.: To a pair `H ⊂ G` of `k`-formal groups, one therefore associates the "formal completion
    `Ĝ_H` of `G` along `H`", which is a `k`-formal group; moreover, one shall see in 5.1.3–5.1.4 that
    the inclusion `σ : H ↪ Ĝ_H` admits a retraction `π : Ĝ_H → H` and that the `k`-formal group
    `N = Ker(π)` is identified, as a formal variety, with the completion of the homogeneous space `G/H`
    along the unit section. This will be useful in 5.2.2.

[^N.D.E-VII_B-C-31]: N.D.E.: Let `G, H` and `Ĝ_H` be the `k`-formal groups corresponding to `A`, `A_0 = A/J` and
    `Gr_J(A)`; then `τ : A_0 ↪ Gr_J(A)` corresponds to a retraction `π : Ĝ_H → H` of the inclusion
    `H ↪ Ĝ_H`, and what precedes means that `Ĝ_H` is the semi-direct product of `N = Ker(π)` by `H`.

[^N.D.E-VII_B-C-32]: N.D.E.: We have detailed the original in what follows, and we have put at the end the "supplement"
    `I_B^n = B ∩ J^n` (which is not necessary to establish Proposition 5.1).

[^N.D.E-VII_B-C-33]: N.D.E.: With the notations of N.D.E. [^N.D.E-VII_B-C-31], this entails that the formal completion
    of `G/H` along the unit section (which has `∏_n B_n` as affine algebra) is isomorphic, as a formal
    variety, to the `k`-formal group `N`.

[^N.D.E-VII_B-C-34]: N.D.E.: The original stated only point (ii); for the reader's convenience, we have stated in (i)
    Lemma 1 of [CA], § V.7.

[^N.D.E-VII_B-C-35]: N.D.E.: In the original, the author uses "linearly compact vector space", which is equivalent to
    "pseudocompact vector space" (cf. [BAC], § III.2, Exercises 15 a), 19 a), and 20 d)). We have
    preferred to keep the terminology "pseudocompact" used so far.

[^N.D.E-VII_B-C-36]: N.D.E.: On the one hand, we have replaced `H\G` by `G/H`, and likewise in the proof; on the other
    hand, we have added condition (iii).

[^N.D.E-VII_B-C-37]: N.D.E.: We have added paragraphs 5.2.1.A and 5.2.1.B.

[^N.D.E-VII_B-C-38]: N.D.E.: This paragraph is the fruit of discussions with J.-M. Fontaine and E. Bouscaren; in
    particular Bouscaren indicated to us the proof that follows.

[^N.D.E-VII_B-C-39]: N.D.E.: We return here to the original, which we have shortened taking account of the preceding
    additions.

[^N.D.E-VII_B-C-40]: N.D.E.: We have added what follows.

[^N.D.E-VII_B-C-41]: N.D.E.: As indicated in the original, this also follows from Proposition 5.1, but we have preferred
    to indicate the argument above, which does not use the implication (i) ⇒ (ii) of loc. cit.

[^N.D.E-VII_B-C-42]: N.D.E.: Since `k` is perfect, one can identify `^π V` with the abelian group `V` on which `k` acts
    by `λ · v = λ^{1/p} v`.

[^N.D.E-VII_B-C-43]: N.D.E.: We have added this remark, used in 5.2.5.

[^N.D.E-VII_B-C-44]: N.D.E.: Indeed, `B′` (resp. `B`) is the inverse limit of the `B′_r` (resp. `B_r`). On the other
    hand, we have modified the original in what follows, taking account of the addition made in 5.2.3.

[^N.D.E-VII_B-C-45]: N.D.E.: We have detailed the original in what follows.

[^N.D.E-VII_B-C-46]: N.D.E.: We have added this number, in order to define the infinite tensor products used in 5.3 (a).

[^N.D.E-VII_B-C-47]: N.D.E.: The author no doubt had in mind a tensor product
    `**A** = ⊗̂^c_{n ∈ ℕ^*} k[[ω′_n]] / ((x^{p^n}))_{x ∈ ω′_n}`, where the `ω′_n` are arbitrary
    pseudocompact `k`-vector spaces. In this case, one sees without difficulty that `ω = ω_{**A**/k}`
    is identified with the product of the `ω′_n`, and the filtration `(ω_n)_{n ∈ ℕ^*}` is given by
    `ω_n = ∏_{i=1}^n ω′_i`, i.e., one is in case 5.2.1.B. For this reason, it would be preferable to
    name these algebras **stable** (rather than "stationary"), cf. [Di73], II § 2.9, p. 75. If for
    example `dim ω′_n = 1` for every `n ∈ ℕ^*`, then `**A**` represents the functor that to every
    `C ∈ Alf/k` associates the set of sequences `(x_n)_{n ∈ ℕ^*}` of elements of `C` such that
    `x_n^{p^n} = 0`, and `x_n = 0` for `n` large enough. Let us note finally that this case (i.e., the
    case where `ω = ∏_{n ∈ ℕ^*} ω′_n`) corresponds to the case studied, in the dual situation of
    connected cocommutative Hopf algebras, by M. E. Sweedler, cf. [Sw67], Th. 3.

[^N.D.E-VII_B-C-48]: N.D.E.: But such an inverse limit is not necessarily a stable profinite `k`-algebra (in the sense
    of the previous N.D.E.). For example, let `S` be the "ordinary" `k`-vector space of sequences
    `(u_1, u_2, …)` of elements of `k` and let `ω = S^*`; then `ω` is the direct sum in `PC(k)` of
    copies `k_n` of `k`, for `n ∈ ℕ^*`, i.e., one is in case 5.2.1.A. If one denotes by `x_n` the
    element of `ω` defined by `x_n(u) = u_n`, for every sequence `u = (u_i)_{i ∈ ℕ^*}`, then the
    `k`-algebra `**A** = k[[ω]] / ((x_n^{p^n}))_{n ∈ ℕ^*}` is such that `ω_{**A**/k} = ω` and
    `ω_n = ∏_{i=1}^n k x_i`, but is not stable: `Spf(**A**)` represents the functor that to every
    `C ∈ Alf/k` associates the set of "infinite" sequences `(x_n)_{n ∈ ℕ^*}` of elements of `C` such
    that `x_n^{p^n} = 0` for every `n ∈ ℕ^*`.

[^N.D.E-VII_B-C-49]: N.D.E.: The editors do not know either, outside the cases considered in 5.2.1.A and B.

[^N.D.E-VII_B-C-50]: N.D.E.: See also [DG70], § III.3, Th. 6.1.

[^N.D.E-VII_B-C-51]: N.D.E.: We have added this subsection, in order to give some consequences of 5.4, mentioned in
    Exposés III and VI_A.

[^N.D.E-VII_B-C-52]: N.D.E.: We have added to this reference, which appeared in the original, the references which
    follow.
