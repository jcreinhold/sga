# Exposé VIII. Faithfully Flat Descent

<!-- label: VIII -->

<!-- original page 195 -->

## 1. Descent of Quasi-Coherent Modules

<!-- label: VIII.1 -->

Let `Sch` be the category of preschemes. Proceeding as in VI.11.b, one finds that the category of pairs `(X,F)`, where
`X` is a prescheme and `F` is a Module on `X`, with morphisms defined as there by means of the notion of direct image of
a Module by a morphism of ringed spaces, can be regarded as a fibered category over `Sch`. The base-change functor
relative to a morphism `f: X → Y` in `Sch` is the inverse-image functor of Modules by `f`. Note that the fiber category
at `X ∈ Ob(Sch)` of the preceding fibered category is the category **opposite** to the category of Modules on `X`.

Since the inverse image of a quasi-coherent Module is quasi-coherent, the full subcategory of the category of pairs
`(X,F)`, formed by the pairs for which `F` is quasi-coherent, is a fibered subcategory of the preceding fibered
category. By contrast, if no hypotheses are made on `f`, the direct image of a quasi-coherent Module is not in general a
quasi-coherent Module. We shall simply call this fibered category the **fibered category of quasi-coherent Modules on
preschemes**.

Recall, on the other hand, that a morphism `f: X → Y` of ringed spaces is said to be **faithfully flat** if it is
**flat**, i.e. for every `x ∈ X`, `𝒪_{X,x}` is a flat module over `𝒪_{Y,f(x)}`, cf. IV, and **surjective**. One says
that `f` is a **quasi-compact** morphism if the inverse image by `f` of every quasi-compact subset is quasi-compact.
When `f` is a morphism of preschemes, this also means that the inverse image by `f` of an affine open subset of `Y` is a
**finite** union of affine open subsets of `X`.

**Theorem.**

<!-- label: VIII.1.1 -->

<!-- original page 196 -->

Let `ℱ` be the fibered category of quasi-coherent Modules on preschemes. Let `g: S′ → S` be a faithfully flat and
quasi-compact morphism of preschemes. Then `g` is a morphism of effective `ℱ`-descent.

Recall[^viii-1-1] that this means two things:

**Corollary. Descent of Homomorphisms of Modules.**

<!-- label: VIII.1.2 -->

Let `g: S′ → S` be a faithfully flat and quasi-compact morphism of preschemes; let `F` and `G` be two quasi-coherent
Modules on `S`; let `F′` and `G′` be their inverse images on `S′`; and finally let `F″` and `G″` be their inverse images
on `S″ = S′ ×_S S′`. Consider the diagram of maps of sets defined by the base-change functors by `g`, `p₁`, `p₂`, where
`p₁,p₂: S′ ×_S S′ ⇉ S′` are the two projections:

```text
Hom_S(F,G) → Hom_{S′}(F′,G′) ⇉ Hom_{S″}(F″,G″).
```

This diagram is exact, i.e. it defines a bijection from the first set onto the set of coincidences of the two maps
written from the second set to the third.

In other words, the base-change functor by `g`, `F ↦ F′`, defines a **fully faithful** functor from the category of
quasi-coherent Modules on `S` to the category of quasi-coherent Modules on `S′` endowed with descent data relative to
`g`. Moreover:

**Corollary. Descent of Modules.**

<!-- label: VIII.1.3 -->

For every quasi-coherent Module `F′` on `S′`, every descent datum on `F′` relative to `g` is **effective**, i.e. `F′`,
with its descent datum, is isomorphic to the inverse image by `g` of a quasi-coherent Module on `S`, determined up to
unique isomorphism by VIII.1.2.

In other words, the preceding fully faithful functor is even an **equivalence**. In practice, this means that giving a
quasi-coherent Module on `S` is the same as giving a quasi-coherent Module on `S′` endowed with descent data relative to
`g`.

**Proof of VIII.1.1.** Let first `T` be an `S`-prescheme that is `S`-isomorphic to the sum of a family of induced open
subsets `Sᵢ` of `S` covering `S`. Then it is evident that the structural morphism `T → S` is a morphism of effective
`ℱ`-descent. This means precisely that giving a quasi-coherent Module `F` on `S` is equivalent to giving quasi-coherent
Modules `Fᵢ` on the `Sᵢ`, together with gluing isomorphisms `φ_{ji}: Fᵢ|Sᵢ∩Sⱼ → Fⱼ|Sᵢ∩Sⱼ` satisfying the familiar
cocycle condition. By VII, 8,

<!-- original page 197 -->

it follows that, in order to verify that `g: S′ → S` is a morphism of effective `ℱ`-descent, it suffices to verify it
for the morphism `g_T: T′ = T ×_S S′ → T` deduced from `g` by the base change `T → S`. Note that the hypothesis on
`T → S` remains stable under arbitrary base change, hence `T → S` is in fact a **universal** morphism of effective
`ℱ`-descent. Taking for the `Sᵢ` affine open subsets covering `S`, we are therefore reduced to the case where `S` is
affine.

Then `S′` is a finite union of affine open subsets; taking the `S`-scheme sum of these, one obtains an affine `S`-scheme
`S₁` and an `S`-morphism `S₁ → S′` that is flat and surjective. Thus `S₁` is also faithfully flat over `S`. If,
therefore, one proves that a faithfully flat affine morphism is a morphism of effective `ℱ`-descent, hence a strict
universal morphism of `ℱ`-descent, the hypothesis being stable under base change, it follows in particular that the
structural morphism `S₁ → S` is a strict universal morphism of `ℱ`-descent. Since there exists an `S`-morphism
`S₁ → S′`, it will indeed follow, by [VIII.D], that `g: S′ → S` is a strict morphism of `ℱ`-descent.

Thus we are reduced to the case where `g` is an affine morphism; as we have seen, we may then moreover suppose `S`
affine. Hence **we may suppose `S` and `S′` affine**. In this case, VIII.1.2 is equivalent to:

**Lemma.**

<!-- label: VIII.1.4 -->

Let `A` be a ring, `A′` a faithfully flat `A`-algebra, `M` and `N` two `A`-modules, `M′` and `N′` the `A′`-modules
obtained by change of rings `A → A′`, and `M″`, `N″` the `A″ = A′ ⊗_A A′`-modules obtained by change of rings `A → A″`.
Then the sequence of maps of sets

```text
Hom_A(M,N) → Hom_{A′}(M′,N′) ⇉ Hom_{A″}(M″,N″)
```

is exact.

<!-- original page 198 -->

Since the homomorphism `N → N′` is injective, `A′` being faithfully flat over `A`, the first arrow is injective. It
remains to prove that if an `A′`-homomorphism `u′: M′ → N′` is compatible with the descent data, then it comes from an
`A`-homomorphism `u: M → N`. But this also simply means that `u′` maps the subset `M` of `M′` into the subset `N` of
`N′`. The induced map `u: M → N` will then automatically be `A`-linear, since `u′` is `A′`-linear, and one sees
similarly that `u′` is necessarily equal to `u ⊗_A A′`.

Now if `x ∈ M`, then `u′(x)` is an element in the kernel of the pair of maps `N′ ⇉ N″`. Thus, in order to prove
VIII.1.4, we are reduced to the following special case, corresponding to the case `M = A`:

**Corollary.**

<!-- label: VIII.1.5 -->

Let `N` be an `A`-module. Then the sequence of maps of sets

```text
N → N′ ⇉ N″
```

is exact.

Indeed, let `A₁` be a faithfully flat `A`-algebra. To show that the sequence under consideration is exact, it suffices
to prove that the sequence deduced from it by the change of rings `A → A₁` is exact. But the latter, as one sees at
once, is the sequence relative to the `A₁`-module `N₁ = N ⊗_A A₁` and to the `A₁`-algebra `A′₁ = A₁ ⊗_A A′`. It is
therefore enough to find an `A₁` faithfully flat over `A` such that `Spec(A′₁) → Spec(A₁)` is a strict morphism of
`ℱ`-descent. It indeed suffices to take `A₁ = A′`, for then the preceding morphism admits a right inverse, hence by
[VIII.D] it is a morphism of effective descent for any fibered category over `Sch`.

It remains finally to show that if `N′` is an `A′`-module endowed with descent data for `A → A′`, i.e. endowed with an
isomorphism

```text
φ: N′₁ ≃ N′₂
```

between the two modules deduced from `N′` by the changes of rings `A′ ⇉ A′ ⊗_A A′`, then

<!-- original page 199 -->

`N′` is isomorphic, with its descent datum, to a module `N ⊗_A A′`. Taking VIII.1.5 into account, one sees easily that
this statement is equivalent to the following:

**Lemma.**

<!-- label: VIII.1.6 -->

Let `N′` be an `A′`-module endowed with descent data relative to `A → A′`, where `A′` is an `A`-algebra. Let `N` be the
`A`-submodule of `N′` formed by the `x` such that

```text
φ(x ⊗_{A′} 1_{A′}) = 1_{A′} ⊗_{A′} x,
```

and consider the canonical homomorphism

```text
N ⊗_A A′ → N′,
```

which is then compatible with the descent data. If `A′` is faithfully flat over `A`, this homomorphism is an
isomorphism.

Let us prove this lemma. Let again `A₁` be a faithfully flat `A`-algebra. To show that the morphism under consideration
is an isomorphism, it suffices to prove that it becomes so after the change of rings `A → A₁`. Now, using the flatness
of `A₁` over `A`, one sees that the homomorphism so obtained is none other than the one that would be obtained directly
in terms of the module `N′ ⊗_A A₁` over `A′₁ = A′ ⊗_A A₁`, endowed with the descent datum relative to `A₁ → A′₁`
canonically deduced by change of rings from the datum given on `N′`. Thus it suffices to find an `A₁` faithfully flat
over `A` such that `Spec(A′₁) → Spec(A₁)` is a morphism of effective `ℱ`-descent. As above, take `A₁ = A′`. This
finishes the proof of VIII.1.6, and hence the proof of VIII.1.1.

**Corollary. Descent of Sections of Modules.**

<!-- label: VIII.1.7 -->

Let `g: S′ → S` be a faithfully flat and quasi-compact morphism of preschemes. For every quasi-coherent Module `G` on
`S`, let `G′` and `G″` be its inverse images on `S′` and `S″ = S′ ×_S S′`, and consider the diagram of homomorphisms of
Modules on `S`:

```text
G → g_*(G′) ⇉ h_*(G″),
```

where `h: S″ → S` is the structural morphism. This diagram is **exact**.

<!-- original page 200 -->

Indeed, this means that for every open `U` in `S`, the corresponding diagram formed by the sections over `U` is exact.
One may evidently suppose `U = S`, and the exactness in question is then a special case of VIII.1.2, obtained by taking
`F = 𝒪_S`.

Since the inverse-image functor of Modules is right exact, one concludes formally from VIII.1.1:

**Corollary. Descent of Quotient Modules.**

<!-- label: VIII.1.8 -->

With the notation of VIII.1.7, let moreover `Quot(F)`, for every quasi-coherent Module `F` on a prescheme, denote the
set of quasi-coherent quotient Modules of `F`. With this convention, the diagram of maps of sets

```text
Quot(G) → Quot(G′) ⇉ Quot(G″)
```

is exact.

One would evidently have the same statement with submodules instead of quotient Modules, since the two correspond
bijectively. Taking in particular `G = 𝒪_S`, one obtains:

**Corollary. Descent of Closed Subpreschemes.**

<!-- label: VIII.1.9 -->

For every prescheme `X`, let `H(X)` be the set of closed subpreschemes of `X`. With this notation, and under the
conditions of VIII.1.7, the following diagram of maps of sets

```text
H(S) → H(S′) ⇉ H(S″)
```

**is exact**.

Theorem VIII.1.1 should be completed by the following result:

**Proposition. Descent of Properties of Modules.**

<!-- label: VIII.1.10 -->

Let `g: S′ → S` be a faithfully flat and quasi-compact morphism, and let `F` be a quasi-coherent Module on `S`. In order
that `F` be of finite type, respectively of finite presentation, respectively locally free and of finite type, it is
necessary and sufficient that its inverse image `F′` on `S′` be so.

It remains only to prove the “suffices” direction. One may evidently suppose `S` affine,

<!-- original page 201 -->

and then, replacing `S′` by a sum of affine open subsets covering `S′`, one is reduced to the case where `S′` is also
affine. Then our statement is equivalent to the following:

**Corollary.**

<!-- label: VIII.1.11 -->

Let `A` be a ring, `A′` a faithfully flat `A`-algebra, `M` an `A`-module, and `M′` the `A′`-module `M ⊗_A A′`. In order
that `M` be of finite type, respectively of finite presentation, respectively locally free of finite type, it is
necessary and sufficient that `M′` be so.

Indeed, `M = colimᵢ Mᵢ`, where the `Mᵢ` are the finite-type submodules of `M`. Hence `M′ = colimᵢ M′ᵢ`, and if `M′` is
of finite type, then `M′` is equal to one of the `M′ᵢ`; by faithful flatness, `M` is equal to `Mᵢ`, hence `M` is of
finite type. Consequently there exists an exact sequence

```text
0 → R → L → M → 0,
```

with `L` free of finite type, whence an exact sequence

```text
0 → R′ → L′ → M′ → 0,
```

with `L′` free of finite type. Thus if `M′` is of finite presentation, `R′` is of finite type, and by what precedes `R`
is of finite type, hence `M` is of finite presentation. Finally, saying that `M` is locally free and of finite type
means that it is of finite presentation and flat, cf. IV in the noetherian case; the general case is left to the reader.
Since each of these properties descends, so does their conjunction. This finishes the proof.

**Remark.**

<!-- label: VIII.1.12 -->

The conjunction of VIII.1.1 and VIII.1.10 shows that the statement VIII.1.1 remains valid when one replaces the fibered
category `ℱ` by the fibered subcategory formed by quasi-coherent Modules of finite type, respectively of finite
presentation, respectively locally free of finite type, respectively locally free of given rank `n`.

## 2. Descent of Affine Preschemes over Another

<!-- label: VIII.2 -->

<!-- original page 202 -->

Since the inverse-image functor of Modules is compatible with tensor product and other tensor operations, Theorem
VIII.1.1 implies various variants, obtained by considering, instead of a single quasi-coherent Module, a quasi-coherent
Module or a system of quasi-coherent Modules endowed with various additional structures expressed by means of tensor
operations.

For example, the data of three quasi-coherent Modules `F`, `G`, `H` on `S` and a pairing

```text
F ⊗ G → H
```

is equivalent to the data of three quasi-coherent Modules `F′`, `G′`, `H′` on `S′`, endowed with descent data relative
to `g: S′ → S`, and endowed with a pairing

```text
F′ ⊗ G′ → H′
```

“compatible” with these descent data, in the evident sense. For example, if `F = G = H`, one sees that the data of a
quasi-coherent Module `F` on `S` endowed with an algebra law, which for the moment we do not suppose to satisfy any
axiom of associativity, commutativity, or existence of a unit section, is equivalent to the same data on `S′`, endowed
in addition with descent data. Using the results of the preceding number, one checks at once that `F` satisfies one of
the usual axioms just mentioned if and only if `F′` does.

For example, the data of a quasi-coherent Algebra `𝒜` on `S`, by which from now on we mean associative, commutative, and
with unit section, is equivalent to the data of a quasi-coherent Algebra `𝒜′` on `S′` endowed with descent data relative
to `g: S′ → S`. Recalling the equivalence between the dual category of quasi-coherent Algebras on `S` and the category
of affine `S`-preschemes over `S`, EGA II, §1, one obtains at once:

**Theorem.**

<!-- label: VIII.2.1 -->

Let `ℱ′` be the fibered category of affine morphisms of preschemes `f: X → S`, regarded as a fibered subcategory of the
fibered category

<!-- original page 203 -->

of arrows in the category `Sch` of preschemes, VI.11.a. Let `g: S′ → S` be a faithfully flat and quasi-compact morphism
of preschemes. Then `g` is a morphism of effective `ℱ′`-descent.

## 3. Descent of Set-Theoretic Properties and Finiteness Properties of Morphisms

<!-- label: VIII.3 -->

_\[Translator’s note: the source section title has a footnote referring to further results of the same kind in EGA IV
2.3, 2.6, and 2.7.\]_

**Proposition.**

<!-- label: VIII.3.1 -->

Let `f: X → Y` be an `S`-morphism, let `g: S′ → S` be a surjective morphism, and let `f′: X′ = X ×_S S′ → Y′ = Y ×_S S′`
be the morphism deduced from `f` by base change using `g: S′ → S`. In order that `f` be surjective, respectively
radicial, it is necessary and sufficient that `f′` be so.

Note that `f′` can also be obtained by the base change `Y′ → Y`, which is also surjective since it is deduced from the
surjective morphism `g: S′ → S`. On the other hand, for every `y ∈ Y` and every `y′ ∈ Y′` lying over `y`, one has an
isomorphism

```text
X′_{y′} ≃ X_y ⊗_{κ(y)} κ(y′),
```

where `X_y` denotes the fiber of `X` at `y`, and `X′_{y′}` that of `X′` at `y′`. It follows that `X_y` is nonempty,
respectively has at most one point and that point corresponds to a radicial residue extension, if and only if `X′_{y′}`
has the same property. This proves VIII.3.1.

**Corollary.**

<!-- label: VIII.3.2 -->

Under the conditions of VIII.3.1, if `f′` is injective, respectively bijective, then `f` is likewise.

This comes from the fact that if `X′_{y′}` has at most one point, respectively exactly one point, then the same is true
of `X_y`. This is indeed so, since the morphism `X′_{y′} → X_y` is surjective, being deduced from
`Spec(κ(y′)) → Spec(κ(y))`, which is surjective.

**Proposition.**

<!-- label: VIII.3.3 -->

With the notation of VIII.3.1, suppose that `g: S′ → S` is surjective and quasi-compact, respectively faithfully flat
and quasi-compact. In order that `f` be quasi-compact, respectively of finite type, it is necessary and sufficient that
`f′` be so.

<!-- original page 204 -->

Only the “suffices” direction has to be proved. One may evidently suppose `S = Y`, since the hypothesis made on
`g: S′ → S` is preserved for `Y′ → Y`. Moreover, one may suppose `Y` affine. Then `Y′` is quasi-compact, hence `X′` is
quasi-compact, since `f′` is so by hypothesis. Let `(Xᵢ)ᵢ∈I` be a family of affine open subsets of `X` covering `X`.
Then the `X′ᵢ` are open subsets of `X′` covering `X′`, so a finite subfamily covers `X′`. Since `X′ → X` is surjective,
it follows that the corresponding `Xᵢ` already cover `X`, and hence `X` is quasi-compact, i.e. `f` is quasi-compact.

Suppose now that `f′` is of finite type, and prove that `f` is so, assuming `g` faithfully flat. Replacing `Y′` by the
sum of a family of affine open subsets covering it, one may suppose `Y′` affine. Finally, since `X` is covered by
finitely many affine open subsets `Xᵢ` by what precedes, it remains to show that they are of finite type over `Y`,
knowing that `X′ᵢ` is of finite type over `Y′`. This reduces us to:

**Corollary.**

<!-- label: VIII.3.4 -->

Let `B` be an `A`-algebra, `A′` a faithfully flat `A`-algebra, and `B′ = B ⊗_A A′` the `A′`-algebra deduced from `B` by
change of rings. In order that `B` be of finite type, it is necessary and sufficient that `B′` be so.

Only the “suffices” direction has to be proved. We have `B = colimᵢ Bᵢ`, where the `Bᵢ` are the finite-type subalgebras
of `B`. Thus `B′ = colimᵢ B′ᵢ`, and if `B′` is of finite type over `A′`, then `B′` is equal to one of the `B′ᵢ`; hence
`B` is equal to `Bᵢ`, and is therefore of finite type.

**Corollary.**

<!-- label: VIII.3.5 -->

Again suppose that the base-change morphism `g: S′ → S` is faithfully flat and quasi-compact. In order that `f` be
quasi-finite, it is necessary and sufficient that `f′` be so.

Indeed, the property “quasi-finite” is by definition the conjunction of “of finite type” and “with finite fibers”; each
descends by `g`, the first by VIII.3.3, the second by the reasoning of VIII.3.1, which uses only the surjectivity of
`g`.

**Remarks.**

<!-- label: VIII.3.6 -->

Let `A` be a ring and `X` an `A`-prescheme. One sees easily that the following conditions are equivalent:

1. There exists a noetherian ring `A₀`, which one may if desired suppose to be a finite-type subring of `A`, an
    `A₀`-prescheme `X₀` of finite type, a homomorphism `A₀ → A`, and an `A`-isomorphism `X ≃ X₀ ×_{A₀} A`.
1. The diagonal morphism `X → X ×_{Spec(A)} X` is quasi-compact, a void condition if `X` is separated over `A`; `X` is a
    finite union of affine open subsets `Xᵢ` whose rings `Bᵢ` are algebras of finite presentation over `A`, i.e.
    quotients of polynomial algebras in finitely many indeterminates by finite-type ideals.

<!-- original page 205 -->

If `X` itself is affine, with ring `B`, these conditions simply mean that `B` is an algebra of finite presentation over
`A`.

A morphism `f: X → Y` is said to be a **morphism of finite presentation**, and one also says that `X` is of finite
presentation over `Y`, if `Y` is a union of affine open subsets `Yᵢ` such that `X|Yᵢ`, as a `Yᵢ`-prescheme, satisfies
the preceding equivalent conditions. The same is then true for `X|Y′` for **every** affine open subset `Y′` in `Y`. This
is a property stable under base change, and moreover the composite of two morphisms of finite presentation is of finite
presentation.

With these notions in place, one sees from (2), proceeding as in VIII.1.10, that that statement remains valid when the
words “of finite type” are replaced by “of finite presentation”.

## 4. Descent of Topological Properties

<!-- label: VIII.4 -->

**Theorem.**

<!-- label: VIII.4.1 -->

Let `g: Y′ → Y` be a morphism, and let `Z` be a subset of `Y`. Suppose that `g` is flat, and that there exists a
quasi-compact morphism `f: X → Y` such that `Z = f(X)`. N.B. if `Y` is noetherian, this latter condition is implied by
“`Z` is constructible”. Then

```text
g⁻¹(closure(Z)) = closure(g⁻¹(Z)).
```

One may suppose `Y` affine, then `Y′` affine. Since `Y` is affine, `X` is a finite union of affine open subsets `Xᵢ`,
and replacing `X` by the sum of the `Xᵢ`, one may also suppose `X` affine. Let `A`, `A′`, `B` be the rings of `Y`, `Y′`,
`X`, and let `B′ = B ⊗_A A′` be the ring of `X′ = X ×_Y Y′`. Let `I` be the kernel of `A → B`, and `I′` the kernel of
`A′ → B′`. Thus the closed subsets of `Y` and `Y′` defined by these ideals are respectively the closure of `Z = f(X)`
and the closure of `Z′ = f′(X′) = g⁻¹(Z)`. We want to show that the latter is equal to `g⁻¹(closure(Z))`, which follows
from `I′ = IA′`, itself a consequence of the flatness of `A′` over `A`.

<!-- original page 206 -->

**Corollary.**

<!-- label: VIII.4.2 -->

Let `g: Y′ → Y` be a flat and quasi-compact morphism, and let `Z′` be a closed subset of `Y′` saturated for the
set-theoretic equivalence relation defined by `g`. Then

```text
Z′ = g⁻¹(closure(g(Z′))).
```

Indeed, `Z′ = g⁻¹(Z)`, with `Z = g(Z′)`. One may then apply VIII.4.1, noting that the condition imposed on `Z` in
VIII.4.1 is indeed satisfied by taking for `X` the prescheme `Z′` endowed with the reduced structure induced by `Y′`.
The fact that `g` is quasi-compact then ensures that the induced morphism `f: Z′ → Y` is quasi-compact.

Statement VIII.4.2 also means that **the topology on `g(Y′)` induced by `Y` is the quotient of the topology of `Y′`**.
In particular:

**Corollary.**

<!-- label: VIII.4.3 -->

Let `g: Y′ → Y` be a faithfully flat and quasi-compact morphism. Then `g` makes `Y` a quotient topological space of
`Y′`; i.e. for a subset `Z` of `Y`, `Z` is closed, respectively open, if and only if `Z′ = g⁻¹(Z)` is so.

Recall now that two elements `a,b` of `Y′` have the same image in `Y` if and only if they are of the form `p₁(c), p₂(c)`
for a suitable element `c` in `Y″ = Y′ ×_Y Y′`. It follows that, if `g` is surjective, one has an **exact** diagram of
sets

```text
𝒫(Y) → 𝒫(Y′) ⇉ 𝒫(Y″),
```

where for every set `E`, `𝒫(E)` denotes the set of its subsets. This being so, VIII.4.3 can also be interpreted as
follows:

**Corollary. Descent of Open, Respectively Closed, Subsets.**

<!-- label: VIII.4.4 -->

<!-- original page 207 -->

Let `g: Y′ → Y` be as in VIII.4.3. For every prescheme `X`, let `Open(X)`, respectively `Closed(X)`, be the set of its
open subsets, respectively the set of its closed subsets. Then one has exact diagrams of set maps, deduced from `g` and
the two projections of `Y″ = Y′ ×_Y Y′`:

```text
Open(Y)   → Open(Y′)   ⇉ Open(Y″),
Closed(Y) → Closed(Y′) ⇉ Closed(Y″).
```

We have the following complement to VIII.4.3:

**Corollary.**

<!-- label: VIII.4.5 -->

Let `g: Y′ → Y` be as in VIII.4.3, and let `Z` be a subset of `Y` such that there exists a quasi-compact morphism
`f: X → Y` with image `Z` (for example, `Z` constructible and `Y` noetherian). Then `Z` is a locally closed subset of
`Y` if and only if `Z′ = g⁻¹(Z)` is a locally closed subset of `Y′`.

It is enough to prove the “if” direction. Let `Y₁` be the closed subprescheme of `Y`, the closure of `Z` endowed with
the induced reduced structure, and let `Y₁′ = Y₁ ×_Y Y′` be the closed subprescheme of `Y′` inverse image of `Y₁`. Its
underlying set is `g⁻¹(Y₁) = g⁻¹(cl(Z))`, hence by VIII.4.1 it is equal to `cl(Z′)`. Since `Z′` is locally closed in
`Y′`, it is open in `cl(Z′)`, hence open in `Y₁′`. But `Y₁′` is faithfully flat and quasi-compact over `Y₁`, so by
VIII.4.3 it follows that `Z` is open in `Y₁`, that is, in `cl(Z)`; this says exactly that `Z` is locally closed.

**Corollary.**

<!-- label: VIII.4.6 -->

Let `g: S′ → S` be a faithfully flat and quasi-compact morphism, let `f: X → Y` be an `S`-morphism, and let
`f′: X′ → Y′` be the `S′`-morphism obtained from it by base change. Suppose that `f′` is an open map (respectively a
closed map, respectively quasi-compact and a homeomorphism into its image, respectively a homeomorphism onto). Then `f`
has the same property.

Since `Y′` is faithfully flat and quasi-compact over `Y`, one may suppose `Y = S`. Let `Q` be a subset of `X`; then,
denoting by `h` the projection morphism `X′ → X`, one has

<!-- original page 208 -->

```text
g⁻¹(f(Q)) = f′(h⁻¹(Q)).
```

If `Q` is open (respectively closed), so is `h⁻¹(Q)`, hence so is `f′(h⁻¹(Q))` if `f′` is assumed to be an open map
(respectively a closed map); therefore `f(Q)` has the same property, by the preceding formula and VIII.4.3. This proves
the first two assertions in VIII.4.6.

It remains to examine the case where `f′` is a homeomorphism into its image, and then to prove that `f` is a
homeomorphism into its image. The case of a homeomorphism onto follows from VIII.3.1. By VIII.3.2, `f` is injective; it
remains to prove that the map `X → f(X)` is open. We already know that `f` is quasi-compact by VIII.3.3. It suffices to
prove that for every closed subset `Z` of `X` one has `Z = f⁻¹(cl(f(Z)))`. Since `h: X′ → X` is surjective, this is
equivalent to the analogous formula after inverse image by `h`, namely

```text
Z′ = f′⁻¹(g⁻¹(cl(f(Z)))),
```

where `Z′ = h⁻¹(Z)`. By VIII.4.1 applied to the subset `f(Z)` of `Y`, one has `g⁻¹(cl(f(Z))) = cl(g⁻¹(f(Z)))`, and the
formula to be proved is equivalent to

```text
Z′ = f′⁻¹(cl(f′(Z′))),
```

which follows from the hypothesis that `f′` is a homeomorphism into its image.

N.B. In this last argument, once `f` is already assumed quasi-compact, we have not used that `g` is quasi-compact, but
only that `g` is faithfully flat. Thus under this hypothesis one can descend the property “homeomorphism into its
image,” or “homeomorphism onto,” or again, by the preceding argument, the property “`f′` is quasi-compact and makes
`f′(X′)` a quotient topological space of `X′`.”

We shall say that a morphism `f: X → Y` of preschemes is **universally open** (respectively **universally closed**,
respectively **universally bicontinuous**, etc.) if for every base change `Y′ → Y`, the morphism `f′: X′ → Y′` is open
(respectively closed, respectively a homeomorphism onto its image). We then deduce from VIII.4.6:

**Corollary.**

<!-- label: VIII.4.7 -->

<!-- original page 209 -->

Under the conditions of VIII.4.6, `f` is universally open (respectively universally closed, respectively a universal
homeomorphism into its image, respectively a universal homeomorphism) if and only if `f′` is.

**Corollary.**

<!-- label: VIII.4.8 -->

Under the conditions of VIII.4.6, `f` is separated (respectively proper) if and only if `f′` is.

To say that `f` is separated means that the diagonal morphism `X → X ×_Y X` is closed, or also universally closed; the
first assertion of VIII.4.8 therefore follows from VIII.4.7. To say that `f` is proper means that `f` satisfies the
conditions: a) `f` is of finite type, b) `f` is separated, c) `f` is universally closed. Condition a) descends by
VIII.3.3; condition b) also descends by what we have just seen; finally condition c) descends by VIII.4.7.

**Remarks.**

<!-- label: VIII.4.9 -->

Recall that when `g: Y′ → Y` is a flat morphism of finite type, with `Y` locally noetherian, then `g` is an open
morphism (VI IV.6.6), which is a sharper result than VIII.4.3. One should note, however, that if `f` is a faithfully
flat and quasi-compact morphism of noetherian preschemes, then `f` is not in general an open morphism. For instance, let
`Y` be an irreducible scheme whose generic point `y` is not open (for example an algebraic curve), and take `Y′` to be
the sum scheme `Y ⨿ Spec(κ(y))`; then the image, under the structural morphism `Y′ → Y`, of the open part `Spec(κ(y))`
is not an open subset of `Y`.

The reader should also observe that various statements of the present exposé become false if one drops the hypothesis
that the faithfully flat morphism under consideration is also quasi-compact. The typical counterexample is obtained by
taking `Y′` to be the sum scheme of the spectra of the local rings of the points of `Y`. For example, again taking `Y`
to be an irreducible algebraic curve and `Z` to be the subset of `Y` consisting of the generic point, its inverse image
in `Y′` is open, while `Z` is not open.

### 4.10.

<!-- label: VIII.4.10 -->

<!-- original page 210 -->

Various statements of the present exposé remain valid if the hypothesis that `Y′` be flat over `Y` is replaced by the
following one: there exists a finite-type Module `F` on `Y′`, with support `Y′`, flat relative to `Y`. Faithful flatness
is then to be replaced by the preceding hypothesis together with the hypothesis that `Y′ → Y` is surjective. This
applies to the first two assertions in VIII.1.10, to VIII.3.3, VIII.3.5, VIII.4.1, and consequently to all the results
of the present number.

## 5. Descent of Morphisms of Preschemes

<!-- label: VIII.5 -->

**Proposition.**

<!-- label: VIII.5.1 -->

Let `g: S′ → S` be a morphism of preschemes.

a) Suppose that `g` is surjective and that the homomorphism

```text
g*: 𝒪_S → g_*(𝒪_S′)
```

is injective. Then `g` is an epimorphism in the category of preschemes, and even in the category of ringed spaces.

b) Suppose that `g` is surjective and makes `S` a quotient topological space of `S′`. Let `S″ = S′ ×_S S′`, let
`h: S″ → S` be the structural morphism, and consider the canonical diagram of homomorphisms

```text
𝒪_S → g_*(𝒪_S′) ⇉ h_*(𝒪_S″).
```

Suppose this diagram is **exact**. Then `g` is an effective epimorphism in the category of preschemes (and also in the
category of ringed spaces), that is, the diagram

```text
S ← S′ ⇔ S″
```

is exact.

**Proof.** a) We must show that a morphism of ringed spaces `f: S → Z` is known once `fg` is known. Since `g` is
surjective, the underlying set map `f₀` of `f` is known; it remains to determine the homomorphism of sheaves of rings
`𝒪_Z → 𝒪_S`, or equivalently the homomorphism

<!-- original page 211 -->

```text
u: f₀⁻¹(𝒪_Z) → 𝒪_S
```

defined by `f`. We already know the homomorphism

```text
(fg)₀⁻¹(𝒪_Z) = g₀⁻¹(f₀⁻¹(𝒪_Z)) → 𝒪_S′
```

defined by `fg`, or equivalently we have a homomorphism

```text
f₀⁻¹(𝒪_Z) → g₀*(𝒪_S′) = g_*(𝒪_S′).
```

One immediately checks that the latter is none other than the composite of `g*: 𝒪_S → g_*(𝒪_S′)` with `u`; since `g*` is
injective, `u` is known once `g*u` is known.

\[
N.B. We have obviously not used the fact that `g: S′ → S` is a morphism of preschemes; the statement would hold for an
arbitrary morphism of ringed spaces. The same remark applies to b), both in the category of ringed spaces and in the
category of spaces ringed by local rings. Notice also that if `g` is a morphism of preschemes, not necessarily
surjective, such that `g*: 𝒪_S → g_*(𝒪_S′)` is injective, then for two morphisms `f₁, f₂` from `S` to a **scheme** `Z`
such that `f₁g = f₂g`, one has `f₁ = f₂`. Indeed, if `I` is the Ideal on `S` defining the subprescheme of `S` where `f₁`
and `f₂` coincide (the inverse image of the diagonal subprescheme of `Z × Z` by `(f₁,f₂)`), one sees that `I` is
contained in `Ker(g*)`.
\]

b) We must show that for every ringed space `Z`, the following diagram of maps is exact,

```text
Hom(S,Z) → Hom(S′,Z) ⇉ Hom(S″,Z),
```

and likewise when `Z` is a space ringed by local rings and one restricts to homomorphisms of spaces ringed by local
rings. Since by a) we already know that the first map is injective, it remains to see that if `f′: S′ → Z` is a
homomorphism of ringed spaces such that `f′p₁ = f′p₂`, then `f′` is of the form `fg`, where `f: S → Z` is a homomorphism
of ringed spaces.

<!-- original page 212 -->

Since `g` is surjective, it is then evident that if `f′` is a morphism of spaces ringed by local rings, the same will be
true for `f`.

The hypothesis on `f′` implies that the underlying set map `f₀′` is constant on the fibers of the map `g₀`. Since `g₀`
is surjective, `f₀′` factors uniquely as `f₀′ = f₀g₀`, where `f₀: S → Z` is a map, necessarily continuous because `g₀`
identifies `S` with a quotient topological space of `S′`. Now consider the homomorphism

```text
f₀⁻¹(𝒪_Z) → g_*(𝒪_S′)
```

deduced from the homomorphism `(f₀g₀)⁻¹(𝒪_Z) → 𝒪_S′` corresponding to `f′`. The hypothesis `f′p₁ = f′p₂` is then
interpreted as saying that the composites of the preceding homomorphism with the two homomorphisms

```text
g_*(𝒪_S′) ⇉ h_*(𝒪_S″)
```

are the same. Hence, by hypothesis b), it factors through a morphism

```text
f₀⁻¹(𝒪_Z) → 𝒪_S.
```

This latter morphism defines a morphism of ringed spaces `f: S → Z`, which is the desired morphism.

**Theorem.**

<!-- label: VIII.5.2 -->

Let `𝓕` be the fibered category of arrows in the category `Sch` of preschemes (VI VI.11.a). Then every faithfully flat
and quasi-compact morphism `g: S′ → S` is a morphism of `𝓕`-descent (or, as one also says, a descent morphism in `Sch`).

This means the following: let `S″ = S′ ×_S S′`, and for two preschemes `X,Y` over `S`, consider their inverse images
`X′,Y′` over `S′` and their inverse images `X″,Y″` over `S″`; this gives a diagram of maps

```text
Hom_S(X,Y) → Hom_S′(X′,Y′) ⇉ Hom_S″(X″,Y″).
```

In these notations, VIII.5.2 says that this diagram is exact. Notice that it is not true in general that `g` is a
morphism of effective descent, that is, that for every prescheme `X′` over `S′`, every descent datum on `X′` relative to
`g: S′ → S` is effective. The question of effectivity, often delicate, will be examined in no. VIII.7.

<!-- original page 213 -->

We have seen in [VIII.D], taking into account that fiber products exist in `Sch`, that statement VIII.5.2 is equivalent
to the following:

**Corollary.**

<!-- label: VIII.5.3 -->

A faithfully flat and quasi-compact morphism of preschemes is a universal effective epimorphism.

Since a faithfully flat and quasi-compact morphism remains so after any base extension, we are reduced to proving that
it is an effective epimorphism. We then apply the criterion VIII.5.1 b), which gives the desired result, taking VIII.4.3
and VIII.1.7 into account.

**Corollary.**

<!-- label: VIII.5.4 -->

Let `g: S′ → S` be a faithfully flat and quasi-compact morphism, let `f: X → Y` be an `S`-morphism, and let
`f′: X′ → Y′` be the `S′`-morphism obtained from it by the base change `S′ → S`. Then `f` is an isomorphism if and only
if `f′` is an isomorphism.

Indeed, if `f′` is an isomorphism, it is also an isomorphism for the natural descent structures on `X′` and `Y′`; and
since the functor `X ↦ X′` from `Sch_/S` to the category of objects of `Sch_/S′` with descent data is fully faithful by
VIII.5.2, it follows that `f` is an isomorphism.

**Corollary.**

<!-- label: VIII.5.5 -->

Under the conditions of VIII.5.4, `f` is a closed immersion (respectively an open immersion, respectively a
quasi-compact immersion) if and only if `f′` is.

As usual, one may suppose `Y = S`, and only the “if” direction has to be proved. Notice that the fact that `X′/Y′` is
endowed with a descent datum relative to `g: Y′ → Y`, and that the structural morphism `f′: X′ → Y′` is an immersion,
hence a monomorphism, implies that the two subobjects of `Y″` obtained as inverse images of `X′/Y′` by the two
projections from `S″` to `S′` are the same.

<!-- original page 214 -->

If `f′` is a closed immersion, it follows from VIII.1.9 that there exists a closed subprescheme `X₁` of `Y` whose
inverse image by `g: Y′ → Y` is `X′`. Thus, by uniqueness of the solution of a descent problem relative to a morphism of
`𝓕`-descent, `X₁` is `Y`-isomorphic to `X`, so `f: X → Y` is a closed immersion. One proceeds in the same way for an
open immersion, using VIII.4.4. Finally, if `f′` is a quasi-compact immersion, then `f` is quasi-compact by VIII.3.3;
therefore one can apply the criterion VIII.4.5 to the subset `f(X)` of `Y`. This proves that `f(X)` is locally closed,
since its inverse image `f′(X′)` in `Y′` is locally closed. Replacing `Y` by an open subset in which `f(X)` is closed,
one is reduced to the case where `f′` is a closed immersion, hence `f` is one by what precedes.

**Corollary.**

<!-- label: VIII.5.6 -->

Under the conditions of VIII.5.4, `f` is affine if and only if `f′` is.

One proceeds as in VIII.5.5, using VIII.2.1. One may also use Serre’s cohomological criterion [EGA II 5.2], which proves
VIII.5.6 without using descent techniques.

**Corollary.**

<!-- label: VIII.5.7 -->

Under the conditions of VIII.5.4, `f` is integral (respectively finite, respectively finite and locally free) if and
only if `f′` is.

Only the “if” direction has to be proved, and as usual one may suppose `Y = S`, with `Y` affine and `Y′` affine. Since
the hypothesis implies that `f′` is affine, `f` is affine as well by VIII.5.6; hence `X`, and consequently `X′`, are
affine. Let `A`, `A′`, `B`, and `B′ = B ⊗_A A′` be the rings of `Y`, `Y′`, `X`, and `X′`. One has `B = colim_i B_i`,
where `B_i` runs through the sub-`A`-algebras of `B` that are of finite type over `A`; hence `B′ = colim_i B_i′`, where
the `B_i′` are finite-type subalgebras of the `A′`-algebra `B′`. If `B′` is integral over `A′`, the `B_i′` are
finite-type modules over `A′`; since `A′` is faithfully flat over `A`, the `B_i` are finite-type modules over `A`, that
is, `B` is integral over `A`. One sees in the same way that if `B′` is finite over `A′`, then `B` is finite over `A`.
The same conclusion holds for “locally free of finite type”; see VIII.1.11.

**Corollary.**

<!-- label: VIII.5.8 -->

<!-- original page 215 -->

Under the conditions of VIII.5.4, suppose `f` quasi-compact, and let `𝓛` be an invertible Module on `X`, with inverse
image `𝓛′` on `X′`. Then `𝓛` is ample (respectively very ample) relative to `f` if and only if `𝓛′` is ample
(respectively very ample) relative to `f′`.

Only the “if” direction has to be proved. The hypothesis on `𝓛′` implies in any case that `f′` is separated, hence `f`
is separated by VIII.4.8. Since `f` is quasi-compact and `g: Y′ → Y` is flat, the computation of direct images by affine
coverings shows that for every integer `n` one has isomorphisms

```text
g*(f_*(𝓛^⊗n)) ≃ f′_*(𝓛′^⊗n),
```

and therefore an isomorphism

```text
g*(𝓢) ≃ 𝓢′,
```

where `𝓢` (respectively `𝓢′`) denotes the quasi-coherent graded Algebra on `Y` (respectively on `Y′`) given by the
direct sum of the `f_*(𝓛^⊗n)` (respectively of the `f′_*(𝓛′^⊗n)`) for `n ≥ 0`. Notice that, for every `n ≥ 0`, the
cokernel of the canonical homomorphism `f′_*(𝓢′_n) → 𝓛′^⊗n` is the inverse image by `X′ → X` of the cokernel of
`f_*(𝓢_n) → 𝓛^⊗n`; hence its support `Z′_n` is the inverse image of the support `Z_n`. If `𝓛′` is ample, the
intersection of the `Z′_n` is empty; since `X′ → X` is surjective, the intersection of the `Z_n` is empty, that is, one
has a canonical morphism

```text
j: X → Proj(𝓢)
```

(EGA II 3). Moreover, the analogous morphism

```text
j′: X′ → Proj(𝓢′)
```

is none other than the one deduced from the preceding morphism by the base change `Y′ → Y` (loc. cit.). With this said,
to say that `𝓛′` is ample relative to `f′` means that `j′` is an immersion, necessarily quasi-compact since `f′` is
quasi-compact. Thus by VIII.5.5, `j` is an immersion; that is, `𝓛` is ample relative to `f`.

One proceeds in an entirely analogous way in the case of “very ample,” restricting above to `n = 1` and replacing
`Proj(𝓢)` by the projective bundle `𝓟(𝓢₁)` associated with `𝓢₁`.

<!-- original page 216 -->

Recall (EGA II 5.1.1) that a quasi-compact morphism `f` is called **quasi-affine** if, for every affine open `U` in `Y`,
`f⁻¹(U)` is a prescheme isomorphic to an open subscheme of an affine scheme. One shows (loc. cit.) that this is
equivalent to saying that `𝒪_X` is ample (or also very ample) relative to `f`. Thus VIII.5.8 implies:

**Corollary.**

<!-- label: VIII.5.9 -->

Under the conditions of VIII.5.4, and assuming `f` quasi-compact, `f` is quasi-affine if and only if `f′` is.

**Remarks.**

<!-- label: VIII.5.10 -->

Hironaka’s example of a non-projective variety shows that one can have a proper morphism `f: X → Y` of nonsingular
algebraic varieties (with `Y` projective), such that `Y` is the union of two open subsets `Y_i` for which
`X_i = X ×_Y Y_i` is projective over `Y_i`, while `f` is not projective. Thus, putting `Y′ = Y₁ ⨿ Y₂`, `Y′` is
faithfully flat and quasi-compact (and even quasi-finite) over `Y`, and `f′: X′ → Y′` is projective, but `f` is not
projective. One must therefore be careful: in order to apply VIII.5.8 and deduce from the fact that `f′` is projective
the same conclusion for `f`, one must already have on `X′` an invertible Module `𝓛′` ample for `f′`, **endowed with a
descent datum relative to** `X′ → X`. This allows `𝓛′` to be regarded as the inverse image of an invertible Module `𝓛`
on `X`, which will then be ample for `f` by VIII.5.8. When `g: S′ → S` is finite and locally free, however, see
VIII.7.7.

## 6. Application to Finite and Quasi-Finite Morphisms

<!-- label: VIII.6 -->

\[
Translator note: the section title contains a footnote in the source: “Cf. EGA IV 18.12 for generalizations to
preschemes not necessarily locally noetherian.”
\]

We shall prove the following two theorems:

**Theorem.**

<!-- label: VIII.6.1 -->

Let `f: X → Y` be a morphism **proper with finite fibers**, with `Y` locally noetherian. Then `f` is finite.

**Theorem.**

<!-- label: VIII.6.2 -->

Let `f: X → Y` be a **quasi-finite** and **separated** morphism, with `Y` locally noetherian. Then `f` is quasi-affine,
and a fortiori quasi-projective.

**Remarks.**

<!-- label: VIII.6.3 -->

<!-- original page 217 -->

Theorem VIII.6.1 is well known, and is due to Chevalley in the case of algebraic varieties. One also finds a simple
proof in [EGA III 4], using the “theorem on formal functions.” The proof given here does not use that theorem, but
instead uses descent theory; we give it as a bonus to the reader, since it comes “for free” at the same time as the
proof of VIII.6.2. Recall also ([EGA III 4] or [VIII.1]) that the global form of Zariski’s “Main Theorem,” deduced from
the “theorem on formal functions,” asserts that if `f: X → Y` is quasi-finite and **quasi-projective**, with `Y`
noetherian, then `X` is `Y`-isomorphic to an open subprescheme of a **finite** `Y`-prescheme `Z`. The conjunction of the
“Main Theorem” and VIII.6.2 is therefore:

**Corollary.**

<!-- label: VIII.6.4 -->

Let `f: X → Y` be a quasi-finite and separated morphism, with `Y` noetherian. Then `X` is `Y`-isomorphic to an open
subprescheme of a finite `Y`-prescheme `Z`.

Another interesting consequence of VIII.6.2 for descent theory will be given with VIII.7.9.

**Proof of VIII.6.1 and VIII.6.2.** We shall admit the following fact, whose proof is easy:

**Lemma.**

<!-- label: VIII.6.5 -->

Let `X` be a prescheme of finite type over a locally noetherian `Y`, and let `y ∈ Y`. Then there exists an open
neighborhood `U` of `y` such that `X|U` is finite (respectively quasi-affine, respectively ...) over `U` if and only if
`X ×_Y Spec(𝒪_y)` is finite (respectively quasi-affine, respectively ...) over `Spec(𝒪_y)`.

[Translator note: the source footnote refers to EGA IV 8.]

Since, on the other hand, the property for `f: X → Y` of being finite, respectively quasi-affine, is local on `Y`, in
order to prove VIII.6.1 and VIII.6.2 we are reduced to the case where `Y` is the spectrum of a local ring, and hence has
finite dimension. We proceed by induction on

```text
n = dim(Y),
```

the assertion being trivial for `n < 0`.

<!-- original page 218 -->

We may therefore suppose `n ≥ 0` and the assertion proved in all dimensions `n′ < n`. Again one may suppose that `Y` is
the spectrum of a noetherian local ring `A` of dimension `n`. Notice that the hypotheses made in VIII.6.1 and VIII.6.2
are stable under base change (we already used this in the initial reduction), and they will remain true after the base
change `Spec(Â) → Spec(A)`. Since the latter is faithfully flat and quasi-compact, the statements VIII.5.7 and VIII.5.9
reduce us to the case where `A` is moreover complete.

Using then the fact that every noetherian local ring `B` over `A` that is quasi-finite over `A` is finite over `A`, and
the fact that `X` is separated over `Y` and the fiber over `y` consists of isolated points, one obtains a decomposition

```text
X = X′ ⨿ X″,
```

where `X′` is **finite** over `Y` and the fiber of `X″` at `y` is empty. If `X` is proper over `Y`, then so is `X″`, and
therefore its image in `Y` is closed; since it does not contain `y`, it is empty, hence `X″ = ∅` and `X = X′`. This
shows that `X` is finite over `Y` and proves VIII.6.1. Notice that the induction hypothesis is not used here.

If `X` is quasi-finite over `Y`, then `X″` is also quasi-finite; but `X″` in fact lies over the open set `Y − {y}` of
`Y`, **which has dimension** `< n`. By the induction hypothesis, `X″` is quasi-affine over `Y − {y}`, hence also over
`Y`. Evidently the same is true for `X′`, and hence for their sum `X`. This proves VIII.6.2.

**Remark.**

<!-- label: VIII.6.6 -->

Theorems VIII.6.1 and VIII.6.2 remain valid if `Y` is no longer assumed locally noetherian, provided one specifies that
`f` is assumed to be of finite presentation (cf. VIII.3.6). Indeed, one may again suppose `Y` affine, and then one
verifies without difficulty that the situation `f: X → Y` is deduced, by a base change `Y → Y₀`, from a situation
`f₀: X₀ → Y₀` satisfying the same hypotheses as `f`, with `Y₀` **noetherian**. Thus by VIII.6.1, respectively VIII.6.2,
`f₀` is finite, respectively quasi-affine, and hence the same is true of `f`. This kind of argument is often useful for
getting rid of noetherian hypotheses, which in applications always end up becoming awkward.

<!-- original page 219 -->

## 7. Effectivity Criteria for a Descent Datum

<!-- label: VIII.7 -->

As usual, consider a morphism of preschemes

```text
g: S′ → S
```

and an `S′`-prescheme `X′`. In accordance with the general facts of VII, 9, the giving of a descent datum on `X′`
relative to `g` is equivalent to the giving of an equivalence pair

```text
q₁,q₂: X″ ⇉ X′
```

such that the structural morphism `X′ → S′` is compatible with this pair and with the equivalence pair

```text
p₁,p₂: S″ = S′ ×_S S′ ⇉ S′
```

defined by `g`, and such that the two squares (or either one of them, which is the same by symmetry) extracted from the
corresponding diagram

```text
X′ ← X″
↓    ↓
S′ ← S″
```

using either `p₁,q₁` or `p₂,q₂`, are **cartesian**. A solution of the descent problem posed by this descent datum, that
is, an object `X` over `S` endowed with an isomorphism `X ×_S S′ ← X′` compatible with the descent data, is equivalent
to the giving of a **cartesian** square

```text
X  ← X′
↓    ↓
S  ← S′
```

satisfying `hq₁ = hq₂`.

<!-- original page 220 -->

Since the class of faithfully flat and quasi-compact morphisms is stable under base change, and since a faithfully flat
and quasi-compact morphism is an effective epimorphism by VIII.5.3, the general theory [VIII.D] gives:

**Proposition.**

<!-- label: VIII.7.1 -->

Suppose `g: S′ → S` faithfully flat and quasi-compact. A descent datum on `X′` relative to `g` is effective if and only
if the equivalence relation `R = (q₁,q₂)` that it defines is effective (that is, the quotient `X′/R` exists and `X″`
becomes the fiber square of `X′` over `X′/R`), and the canonical morphism `X′ → X′/R` is faithfully flat and
quasi-compact.

Thus the question of effectivity of a descent datum is a special case of the question of effectivity of an equivalence
graph, and various effectivity criteria given in this number can be obtained in this way. Nevertheless, in the context
of descent one has Theorem VIII.2.1, which implies that **if `X′` is affine over `S′`, every descent datum on `X′`
relative to `g` is effective**; this statement has no analogue for passage to the quotient by a general flat equivalence
graph. All the effectivity criteria we give here can also be regarded as consequences of the preceding statement.

Let `U′` be a subprescheme of `X′` (or more generally a subobject of `X′` in the category `Sch`). We say that `U′` is
**stable under the descent datum** on `X′` if one can put on `U′` a descent datum relative to `g` such that the
immersion `U′ → X′` is compatible with the descent data. This also means that the inverse images of `U′` in `X″` by `q₁`
and `q₂` are the same (or, as one also says, that `U′` is **stable under the equivalence relation** `R`). Of course the
descent datum in question on `U′` is then unique, and is called the **induced descent datum** from that of `X′`. With
this understood:

**Proposition.**

<!-- label: VIII.7.2 -->

Let `(X_i′)` be a covering of `X′` by open subsets `X_i′` stable under the descent datum. The descent datum on `X′` is
effective if and only if the induced descent data on the `X_i′` are effective.

<!-- original page 221 -->

This is an easy consequence of VIII.7.1, for example, and the details of the proof are left to the reader.

**Corollary.**

<!-- label: VIII.7.3 -->

Let `(S_i)` be an open covering of `S`, and for each `i` let `S_i′` and `X_i′` be deduced from `S′` and `X′` by the base
change `S_i → S`. The descent datum on `X′` is effective if and only if, for every `i`, the descent datum on `X_i′`
relative to `g_i: S_i′ → S_i` is effective.

This criterion almost always reduces us to the case where `S` is affine. In the case where `S′` is also affine, which is
the most frequent case in applications, one has:

**Corollary.**

<!-- label: VIII.7.4 -->

Suppose `S` and `S′` affine. The descent datum on `X′` is effective if and only if `X′` is the union of affine open
subsets `X_i′` stable under the descent datum.

Sufficiency follows from VIII.7.2 and from the fact that, if `X_i′` is affine, it is affine over `S′` and one can apply
VIII.2.1. For necessity, note that if `X′` comes from `X`, and if `X` is covered by affine open subsets `X_i`, then the
`X_i′ = X_i ×_S S′` are affine open subsets stable under the descent data and covering `X′`.

**Corollary.**

<!-- label: VIII.7.5 -->

Let `g: S′ → S` be a faithfully flat, quasi-compact, and **radicial** morphism. Then `g` is a morphism of **effective**
descent; that is, for every `X′` over `S′`, every descent datum on `X′` relative to `g: S′ → S` is effective.

Indeed, by VIII.7.3 one may suppose `S` affine. Since `S′` is radicial over `S`, hence separated, `S′` is separated.
Moreover, for every `x′ ∈ X′`, the fiber `R(x′) = q₂(q₁⁻¹(x′))` of the set-theoretic equivalence relation defined by `R`
is reduced to one point: since `g` is radicial, the same is true of `p₁,p₂`, which are deduced from it by the base
change `S′ → S`, and hence also of `q₁,q₂`, which are deduced from the preceding ones by the base change `X′ → S″`.

<!-- original page 222 -->

Thus **every open subset of `X′` is stable** under the descent datum. Cover `X′` by affine open subsets `X_i′`. These
are affine over `S` because `S′` is separated, so the induced descent datum is effective by VIII.2.1. We then conclude
by VIII.7.2.

Notice that VIII.7.5 gives the only known case of an effective descent morphism in the category of preschemes, and
probably the only case indeed, even if one restricts to noetherian schemes or to schemes of finite type over a field.

When `S` is assumed locally noetherian and `S′` of finite type over `S`, statement VIII.7.5 is also a special case of
the following one, which generalizes Weil’s Galois descent and Cartier’s inseparable descent:

**Corollary.**

<!-- label: VIII.7.6 -->

Let `g: S′ → S` be a finite locally free morphism (that is, defined by an Algebra on `S` that is a locally free module
of finite type) and surjective. Then `g` is faithfully flat and quasi-compact, hence a descent morphism. Let `X′` be an
`S′`-prescheme endowed with a descent datum. This datum is effective if and only if, for every `x′ ∈ X′`, the fiber
`R(x′) = q₂(q₁⁻¹(x′))` is contained in an affine open subset. This condition is automatically satisfied if `X′` is
quasi-projective over `S′`.

The parenthetical assertion comes from the fact that, if `s` is the point of `S` below `x′`, then `R(x′)` is finite and
contained in the fiber `X′_s`; on the other hand, since `X′` is quasi-projective over `S′` and `S′` is finite over `S`,
`X′` is quasi-projective over `S`, which implies that a fiber of `X′` over `S` is contained in an affine open subset.

Since every finite subset of an affine scheme has a fundamental system of affine neighborhoods, one does not lose the
hypothesis by restricting over an affine open subset of `S`; by VIII.7.3 this reduces us to the case where `S` is
affine. By VIII.7.4, we are reduced to showing that `x′` is contained

<!-- original page 223 -->

in an affine open subset **stable** under the descent datum. Indeed, let `U` be an affine open subset containing
`R(x′)`. Then the saturation

```text
R(X′ − U) = q₂(q₁⁻¹(X′ − U))
```

does not meet `R(x′)`; moreover, since `q₂` is finite (because `g`, hence `p₂`, is finite), and therefore closed, the
right-hand side is a closed subset of `X′`. Let `U′` be its complement in `X′`. This is a **saturated** open subset, and
one has

```text
R(x′) ⊂ U′ ⊂ U,
```

with `U` affine, but `U′` not a priori affine. Since a finite subset `R(x′)` in an affine scheme `U` has a fundamental
system of affine neighborhoods of the form `U_f`, replacing `f` by its restriction to `U′` shows that there exists a
section `f` of `𝒪_U` such that

```text
R(x′) ⊂ U′_f,    U′_f is affine.
```

Let `U″ = q₁⁻¹(U′) = q₂⁻¹(U′)`, still denoting by `q₁,q₂` the induced morphisms `U″ → U′`, and consider

```text
f′ = Norm_q₂(q₁*(f)),
```

where `Norm_q₂` denotes the **norm** relative to the finite locally free morphism `q₂: U″ → U′`. The compatibility of
the formation of the norm with base change easily implies that `f′` is an **invariant** section:

```text
q₁*(f′) = q₂*(f′),
```

which implies that `U′_f′` is a saturated open subset of `U′`. More precisely, denoting by `Z(f′)` the set of zeros of a
section `f′`, one finds from the properties of norms that

```text
Z(f′) = q₂(Z(q₁*(f))) = q₂(q₁*(Z(f))) = R(U′ − U′_f).
```

<!-- original page 224 -->

This implies that `U′_f′ = U′ − Z(f′)` is saturated, contains `R(x′)`, and is contained in `U′_f`. Since the latter is
affine, it follows that `U′_f′` is also affine (being equal to `(U′_f)_f″`, with `f″ = f′` restricted to `U′_f′`). It is
therefore a saturated affine open subset containing `R(x′)`, hence `x′`, which completes the proof.

Notice that this argument applies whenever one has an equivalence relation (or even only a pre-equivalence relation; see
[VIII.3]) in a prescheme `X′`, finite and locally free; indeed VIII.7.6 is also a special case of the analogous result
for finite locally free pre-equivalences, loc. cit. The same remark applies to VIII.7.7 below.

Once the existence of a saturated quasi-affine open subset `U′` containing `x′` has been obtained, one can also appeal
to VIII.7.9 and VIII.7.2, which avoids the use of norms.

Notice moreover that under the conditions of VIII.7.6, if the descent datum on `X′` is effective, with `X′` coming from
`X` over `S`, then the morphism `X′ → X` is finite, locally free, and surjective, since it is deduced from `g` by the
base change `X → S`. It follows (EGA II 6.6.4) that if `X′` is quasi-projective over `S′`, hence over `S`, then `X` is
quasi-projective over `S`. A relatively ample invertible sheaf on `X` is obtained by taking the **norm** of an
invertible sheaf on `X′` relatively ample over `S`, or over `S′`, which is the same thing. Thus one obtains:

**Corollary.**

<!-- label: VIII.7.7 -->

A finite locally free and surjective morphism `g: S′ → S` is a morphism of effective descent for the fibered category of
preschemes quasi-projective over other preschemes; that is, for every `X′` quasi-projective over `S′`, every descent
datum on `X′` relative to `g` is effective, and the descended `S`-prescheme `X` is quasi-projective over `S`.

**Proposition.**

<!-- label: VIII.7.8 -->

Let `g: S′ → S` be a faithfully flat and quasi-compact morphism. Then `g` is a morphism of effective descent for the
fibered category of preschemes `Z` quasi-compact

<!-- original page 225 -->

over a prescheme `T` and endowed with an invertible sheaf ample relative to `T`. In particular, for every prescheme `X′`
over `S′`, endowed with a descent datum relative to `g: S′ → S`, and every invertible sheaf `𝓛′` on `X′` ample relative
to `S′` and likewise endowed with a descent datum relative to the given one on `X′` (that is, endowed with an
isomorphism from `q₁*(𝓛′)` to `q₂*(𝓛′)`, satisfying the usual transitivity condition), the descent datum on `X′` is
effective, and the invertible sheaf `𝓛` on the descended prescheme `X`, deduced from `𝓛′` by descent, is ample relative
to `S`.

The proof is entirely analogous to that of VIII.5.8. One notes that on the quasi-coherent graded Algebra `𝓢′` on `S′`
defined by `𝓛′` there is a descent datum, allowing one to construct a quasi-coherent graded Algebra `𝓢` on `S` by
VIII.1.1, whence a `P = Proj(𝓢)` over `S` such that `P′ = Proj(𝓢′)` is identified, together with its descent datum, with
`P ×_S S′`. Since by hypothesis `X′` is identified with an open subset of `P′`, necessarily stable under the descent
datum on `P′`, the descent datum on `X′` is also effective, and one obtains the descended prescheme as an open subset of
`P`. The details are left to the reader.

In particular, taking `𝓛′ = 𝒪_X′`, one finds:

**Corollary.**

<!-- label: VIII.7.9 -->

Let `g: S′ → S` be a faithfully flat and quasi-compact morphism, and let `X′` be a **quasi-affine** prescheme over `S′`.
Then every descent datum on `X′` relative to `g` is effective, and the descended prescheme `X` is quasi-affine over `S`.

By VIII.6.2, this result applies in particular if `S′` is locally noetherian and `X′` is quasi-finite and separated over
`S′`; more generally, if `S′` is arbitrary and `X′` is of finite presentation, quasi-finite, and separated over `S′`
(cf. VIII.6.6).

**Remarks.**

<!-- label: VIII.7.10 -->

The results given in this number exhaust the currently known effectivity criteria, and probably even all useful existing
criteria. \[Translator note: the corrected source adds that this opinion turned out to be partly erroneous, referring
for example to J.-P. Murre, Séminaire Bourbaki 294 (Appendix), May 1965, and to special results, notably of Néron and
Raynaud; for descent of group schemes, see M. Raynaud’s 1968 thesis.\] Notice the following counterexamples in support
of this assertion:

<!-- original page 226 -->

1. If `S` is the spectrum of a field, and `S′` is the spectrum of a quadratic Galois extension, one can find an `X′`
    over `S′`, proper and smooth over `S′`, of dimension 3, endowed with a descent datum that is not effective (Serre).

1. One can find an `S` equal to the spectrum of a regular local ring of dimension 3 (if desired, the local ring of an
    algebraic scheme over a field of prescribed characteristic), and a principal covering `T` of `S` with group `ℤ/2ℤ`,
    such that, if `t` denotes one of the points of `T` above the closed point `s` of `S`, and `S′ = T − s`, one can
    find an `X′` **projective** over `S′`, regular, endowed with a descent datum relative to `g: S′ → S`, this descent
    datum not being effective.

For these constructions one uses Hironaka’s example of non-projective varieties. For (i), it is enough to use the fact
that one can find over `k` a proper and smooth scheme `X₀` of dimension 3, on which `G = ℤ/2ℤ` acts without inertia, and
in which there exist two rational points `a,b` congruent under `G` and not contained in any affine open subset. One then
puts `X′ = X₀ ×_k k′`, and lets `G` act on `X′` through the actions of `G` on the two factors; this gives a descent
datum on `X′` relative to `g: Spec(k′) → Spec(k)`. Above `a`, respectively `b`, there is exactly one point `a′`,
respectively `b′`, with quadratic residue extension, and `a′` and `b′` are congruent under `G`, since `X′ → X₀` is
compatible with the actions of `G`. Then `a′` and `b′` cannot be contained in an affine open subset `U′`, for then
`U = X₀ − Im(X′ − U′)` would be an open subset of `X₀` containing `(a,b)`, whose inverse image in `X′` would be
contained in `U′`, hence quasi-affine; therefore `U` would be quasi-affine, and consequently `(a,b)` would have an
affine neighborhood in `U`.

For (ii), one uses the fact that in Hironaka’s example, `X₀` is obtained as a prescheme proper over a projective
`k`-scheme `Y`, smooth over `k`. The morphism `f: X₀ → Y` is birational, though this is immaterial. The group `G` also
acts on `Y` compatibly with its actions on `X₀`. Finally, putting `S′ = Y − f(b)` and `X′ = X₀|S′`, `X′` is projective
over `S′`.

<!-- original page 227 -->

Then `X₀` is endowed with a natural descent datum relative to the canonical morphism `Y → S = Y/G`, by means of the
actions of `G` on `X₀` compatible with its actions on `Y`. This descent datum is not effective, since `(a,b)` is not
contained in an affine open subset. The induced descent datum on `X′` relative to `g: S′ → S` is then not effective, as
is easily verified.

## Bibliography

**[VIII.D]** J. Giraud, _Méthode de la descente_, Mémoire no. 2 de la Société Mathématique de France, 1964.

**[VIII.1]** A. Grothendieck, Séminaire Bourbaki: _Géométrie formelle et Géométrie algébrique_, May 1959, no. 182.

**[VIII.2]** A. Grothendieck, Séminaire Bourbaki: _Technique de descente et Théorèmes d’existence I_, December 1959, no.
190\.

**[VIII.3]** A. Grothendieck, Séminaire Bourbaki: _Technique de descente et Théorèmes d’existence III_, February 1961,
no. 212.

[^viii-1-1]: We admit here the general theory of descent set out in detail in the article of J. Giraud cited in the
    footnote to the Warning, a work that we shall cite as [VIII.D] below. Cf. also [VIII.2] for a succinct
    account.
