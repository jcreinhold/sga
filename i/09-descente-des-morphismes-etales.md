# Exposé IX. Descent of Étale Morphisms. Application to the Fundamental Group

<!-- label: IX -->

<!-- original page 228 -->

## 1. Reminders on Étale Morphisms

<!-- label: IX.1 -->

We shall review here the properties of étale morphisms, developed in Exposé I, that we shall need, taking the
opportunity to remove the superfluous noetherian hypotheses from the theory. The reader should note that even if one is
interested only in noetherian schemes, descent techniques lead one to introduce non-noetherian schemes, such as
`Spec(Â ⊗_A Â)`, where `A` is a noetherian local ring; and in order to apply the language of fibered categories, it is
important to define notions such as étale morphism, etc., without introducing noetherian restrictions. A reader
reluctant to verify or admit that the statements below are true without noetherian hypotheses may content himself with
admitting them under the noetherian hypotheses of Exposé I, provided that the same noetherian hypotheses are introduced
into the statements of the following numbers, and that Definition IX.1.1 below is used for the non-noetherian schemes
that enter the arguments.

**Definition.**

<!-- label: IX.1.1 -->

Let `f: X → S` be a morphism of preschemes, and let `x` be a point of `X`. We say that `f` is **étale at** `x`, or that
`X` is étale over `S` at `x`, if there exist an affine open neighborhood `U` of `s = f(x)`, an affine open neighborhood
`V` of `x` over `U`, a noetherian affine scheme `U₀`, an affine `U₀`-scheme `V₀` that is étale in the sense of Exposé I,
a morphism `U → U₀`, and a `U`-isomorphism

`V ≃ V₀ ×_U₀ U`.

<!-- original page 229 -->

When `S` is locally noetherian, this terminology agrees with that of loc. cit. Similarly, we shall say that `f` **is
étale**, or that `X` **is étale over** `S`, if `f` is étale at every point `x` of `X`. With these definitions, the
propositions below reduce without difficulty to the noetherian case, where they are proved in I.4, I.5, and I.7. For
details, the reader may consult EGA IV. [Translator note: more precisely, EGA IV 17 and 18.]

**Remarks.**

<!-- label: IX.1.2 -->

If `f` is étale at `x`, then `f` is “**of finite presentation at** `x`” (VIII.3.5), the local ring of `x` in the fiber
`f⁻¹(s)` is a **finite separable extension** of `κ(s)`, and `f` is **flat at** `x`. One can show that the converse is
true; hence Definition IX.1.1 is the same as in the case where `S` is locally noetherian, except that the condition “of
finite type at `x`” must be replaced by “of finite presentation at `x`.” Since this result has a delicate proof, we have
not wanted to take it here as the definition of an étale morphism, as it does not lend itself directly to the proof of
the properties that follow.

First note the trivial fact:

**Proposition.**

<!-- label: IX.1.3 -->

If `f: X → S` is étale, then every morphism `f′: X′ → S′` obtained from it by base change `S′ → S` is also étale.

Thus one can say that étale morphisms form a **fibered subcategory** of the category of arrows in `Sch` (cf. VI VI.11
a). The object of the present exposé is the study of the exactness properties of this fibered category over `Sch`.

**Proposition.**

<!-- label: IX.1.4 -->

Let `f: X → S` be a morphism of preschemes. It is an open immersion if and only if it is étale and radicial.

Cf. I.5.1. It follows that if `X` is étale over `S`, every section of `X` over `S` is an open immersion. Using IX.1.4
once more, one obtains:

**Corollary.**

<!-- label: IX.1.5 -->

Let `X` be an étale `S`-prescheme. Then there is a one-to-one correspondence between the set of sections of `X` over `S`
and the set of open subsets `Γ` of `X` such that the morphism `Γ → S` induced by the structural morphism is **radicial**
and **surjective**.

<!-- original page 230 -->

If moreover `X` is separated over `S`, `Γ` will be a subset of `X` both open and closed, but this is immaterial. Making
the evident base change, one can put IX.1.5 in the following apparently more general form:

**Corollary.**

<!-- label: IX.1.6 -->

Let `X` and `Y` be two `S`-preschemes, with `Y` étale over `S`. Then the map `f ↦ Γ_f` associating to every `S`-morphism
`f` from `X` to `Y` the subset of `X ×_S Y` underlying the graph of `f` is a bijection from `Hom_S(X,Y)` onto the set of
open subsets `Γ` of `X ×_S Y` such that the morphism `Γ → X` induced by `pr₁` is **radicial** and **surjective**.

**Proposition.**

<!-- label: IX.1.7 -->

Let `S₀` be the subprescheme of `S` defined by a quasi-coherent nil-ideal, that is, such that `S₀` has the same
underlying set as `S`. Then the functor `X ↦ X ×_S S₀` from the category of preschemes étale over `S` to the category of
preschemes étale over `S₀` is an equivalence of categories.

The fact that this functor is fully faithful is an immediate consequence of IX.1.6. The fact that it is essentially
surjective is contained in I.8.3. Notice that under the preceding equivalence, `X` is of finite type, that is,
quasi-finite over `S` (respectively finite, that is, an étale covering of `S`), if and only if `X₀` satisfies the
analogous condition over `S₀`; the same remark applies to separatedness. These facts are immediate, and are also
contained in IX.2.4 below.

**Corollary.**

<!-- label: IX.1.8 -->

Let `A` be a complete noetherian local ring with residue field `k`. Then the functor `B ↦ B ⊗_A k` is an equivalence
from the category of finite étale `A`-algebras to the category of finite étale `k`-algebras, that is, finite direct
products of finite separable extensions of `k`.

**Proposition.**

<!-- label: IX.1.9 -->

For `X` to be an **étale covering** of `S`, that is, finite and étale over `S`, it is necessary and sufficient that `X`
be `S`-isomorphic to the spectrum of an Algebra `𝓐` on `S`, which is a locally free Module of finite type, and such that
for every

<!-- original page 231 -->

`s ∈ S`, `𝓐_s ⊗_{𝒪_s} κ(s)` is a separable algebra over `κ(s)`, hence in this case a direct product of finite separable
extensions of `κ(s)`.

Finally, the following result is less elementary in nature, being the conjunction of I.8.4 and the **existence theorem
for sheaves in algebraic geometry** (EGA III 5; cf. also [IX.1], theorem 3).

**Theorem.**

<!-- label: IX.1.10 -->

Let `S` be the spectrum of a complete noetherian local ring, let `X` be a proper `S`-scheme, and let `X₀` be the fiber
of `X` at the closed point of `S`, so that `X₀` is a closed subscheme of `X`. Then the restriction functor
`X′ ↦ X′ ×_X X₀` is an equivalence from the category of étale coverings of `X` to the category of étale coverings of
`X₀`.

## 2. Submersive and Universally Submersive Morphisms

<!-- label: IX.2 -->

**Definition.**

<!-- label: IX.2.1 -->

A morphism `g: S′ → S` of preschemes is called **submersive** if it is surjective and makes `S` a quotient topological
space of `S′`; that is, a subset `U` of `S` whose inverse image `f⁻¹(U)` is open is itself open. One says that `f` is
**universally submersive** if, for every morphism `T → S`, the morphism `f′: T′ = S′ ×_S T → T` deduced from `f` by base
change is submersive.

It is immediate that the composite of two submersive (respectively universally submersive) morphisms is submersive
(respectively universally submersive), and that a base change of a universally submersive morphism is universally
submersive. If `fg` is submersive (respectively universally submersive), then `f` is so.

**Examples.**

<!-- label: IX.2.2 -->

a) A surjective morphism that is open, or closed, is submersive. Hence a surjective universally closed or universally
open morphism is universally submersive. For example, **a proper surjective morphism is universally submersive**. On the
other hand, **a faithfully flat and quasi-compact morphism is universally submersive** (VIII.4.3). These will be the two
most important cases for us.

<!-- original page 232 -->

One can apply to a submersive or universally submersive morphism `g: S′ → S` the arguments of VIII.4.3. In particular
one finds:

**Proposition.**

<!-- label: IX.2.3 -->

Suppose `g: S′ → S` submersive. Then the following diagram of maps is exact:

`Open(S) → Open(S′) ⇉ Open(S″)`,

where `S″ = S′ ×_S S′`, and where `Open(X)` denotes the set of open subsets of the prescheme `X`.

**Proposition.**

<!-- label: IX.2.4 -->

Let `g: S′ → S` be a universally submersive morphism, let `f: X → Y` be an `S`-morphism, and let `f′: X′ → Y′` be the
`S′`-morphism deduced from it by base change. For `f` to be open (respectively closed), it is enough that `f′` be so.
For `f` to be universally open, respectively universally closed, respectively separated, it is necessary and sufficient
that `f′` be so. If in addition `g` is quasi-compact and `f` is locally of finite type, then `f` is proper if and only
if `f′` is proper.

For this last point, note that if `f′` is proper, hence quasi-compact, then `f` is quasi-compact (VIII.3.3), hence of
finite type since it is locally of finite type. On the other hand it is separated and universally closed by what
precedes; therefore it is proper.

**Proposition.**

<!-- label: IX.2.5 -->

Let `S′` be a prescheme of finite type over the spectrum `S` of a complete noetherian local ring. Suppose that the fiber
over the closed point `s` of `S` is finite, so that the local rings in `S′` at the points `s′` of this fiber are finite
over `A = 𝒪_s`. Let `S″` be the sum scheme of the spectra of the `𝒪_{S′,s′}` in question, regarded as a finite
`S`-scheme. Then `g: S′ → S` is universally submersive if and only if the structural morphism `S″ → S′` is surjective.

Since there is a natural `S`-morphism `S″ → S′`, and since a finite surjective morphism is universally submersive by
IX.2.2, the stated condition is sufficient. Conversely, suppose `S″ → S′` is not surjective; we show that `g` is not
universally submersive. Let `t` be a point of `S` not in the image of `S″`. There then exists an `S`-scheme `T`, the
spectrum of a discrete valuation ring, whose image in `S` is `{s,t}`.

<!-- original page 233 -->

Notice that the image of `S″` in `S′` is open, because the morphism `S″ → S′` is a local isomorphism; moreover this
image contains `S′_s` and does not meet `S′_t`. It follows that the inverse image of this open subset in `T′ = S′ ×_S T`
is **open** and identical with the inverse image of the closed point of `T`. This shows that `T′ → T` is not submersive,
and hence `S′ → S` is not universally submersive.

**Remark.**

<!-- label: IX.2.6 -->

Using the criterion IV.6.3 for a constructible subset of a noetherian space to be open, one easily obtains the following
valuative criterion for a morphism `g: S′ → S` **of finite type**, with `S` locally noetherian, to be universally
submersive: it is necessary and sufficient that, for every `S`-scheme `T` that is the spectrum of a discrete valuation
ring, putting `T′ = S′ ×_S T`, the inverse image in `T′` of the closed point of `T` be non-open.

## 3. Descent of Morphisms of Étale Preschemes

<!-- label: IX.3 -->

**Proposition.**

<!-- label: IX.3.1 -->

Let `g: S′ → S` be a **surjective** morphism of preschemes, let `X` and `Y` be two preschemes over `S`, and let `X′`,
`Y′` be their inverse images over `S′`. If `Y` is unramified over `S`, then the canonical map

`Hom_S(X,Y) → Hom_{S′}(X′,Y′)`

is injective.

Indeed, by IX.1.6, an `S`-morphism `f: X → Y` is known once one knows the underlying set of its graph `Γ`, which is a
subset of `Z = X ×_S Y`. Since

`Z′ = Z ×_S S′ = X′ ×_{S′} Y′ → Z`

is surjective (because `S′ → S` is), this subset `Γ` is known once one knows its inverse image in `X′ ×_{S′} Y′`, which
is nothing other than the underlying set of the graph of `f′`. This proves the assertion.

A subset `Γ` of `Z` is the graph of an `S`-morphism `f: X → Y` if and only if it is open and if the morphism induced by
`pr₁` from `Γ` to `X` is radicial

<!-- original page 234 -->

and surjective; cf. IX.1. When the first property is verified, the second is verified if and only if the inverse image
`Γ′` of `Γ` in `Z′` satisfies the same condition, by VIII.3.1. If one finally knows that `Z′ → Z` is submersive, which
will be the case in particular if `S′ → S` is universally submersive, then `Γ` is open if and only if `Γ′` is open.

Thus the set `Hom_S(X,Y)` is then in one-to-one correspondence with the set of open subsets `Γ′` of `Z′` such that the
projection morphism `pr₁: Z′ → X′` is radicial and surjective (that is, corresponding to an `S′`-morphism
`f′: X′ → Y′`), and which are saturated for the equivalence relation defined by `Z′ → Z`; that is, whose two inverse
images in `Z″ = Z′ ×_Z Z′ = Z ×_S S″`, where `S″ = S′ ×_S S′`, by the two projections, are equal. But these latter
subsets are the graphs of the two `S″`-morphisms `X″ → Y″` deduced from `f′` by base change along the two projections
`S″ → S′`. We have therefore obtained:

**Proposition.**

<!-- label: IX.3.2 -->

Let `g: S′ → S` be a **universally submersive** morphism of preschemes, let `S″ = S′ ×_S S′`, let `X` and `Y` be two
`S`-preschemes, let `X′` and `Y′` be their inverse images over `S′`, and let `X″` and `Y″` be their inverse images over
`S″`. If `Y` is étale over `S`, then the following canonical diagram of maps is exact:

`Hom_S(X,Y) → Hom_{S′}(X′,Y′) ⇉ Hom_{S″}(X″,Y″)`.

Taking `X` and `Y` étale over `S`, one obtains the following statement, which moreover gives back IX.3.2, even if one
restricts to `X = S`; indeed in IX.3.2 one can always reduce to that case by the base change `X → S`.

**Corollary.**

<!-- label: IX.3.3 -->

A universally submersive morphism of preschemes is a descent morphism for the fibered category of preschemes étale over
other preschemes.

I do not know, however, whether it is necessarily a morphism of **effective** descent for the fibered category in
question, even under the additional hypotheses that `S` be noetherian and `g` of finite type, and even restricting to
étale coverings. We shall nevertheless give useful criteria of effectivity in the next number.

**Corollary.**

<!-- label: IX.3.4 -->

<!-- original page 235 -->

Let `g: S′ → S` be a universally submersive morphism whose fibers `g⁻¹(s)` are “geometrically connected,” that is, for
every extension `K/κ(s)`, `g⁻¹(s) ⊗_{κ(s)} K` is connected. Then `S′` is connected if `S` is. The functor from the
category of preschemes étale over `S` to the category of preschemes étale over `S′` defined by `g` is fully faithful.

A subset of `S′` that is both open and closed is saturated for the set-theoretic equivalence relation defined by `g`,
since the fibers are connected; it is therefore the inverse image of a subset of `S`, necessarily both open and closed
because `g` is submersive. Thus if `S` is connected, `S′` is connected.

This also implies the following fact: the composite `fg` of two morphisms with universally connected fibers, with `f`
universally submersive, has universally connected fibers; if `S₁′` and `S₂′` over `S` have universally connected fibers,
the same is true of `S₁′ ×_S S₂′`. In particular, under the conditions of IX.3.4, `S″` has universally connected fibers
over `S`.

Let `X` and `Y` be étale over `S`, and let `u′` be an `S′`-morphism from `X′` to `Y′`. We prove that it is compatible
with the descent data, which gives the desired conclusion by IX.3.3. Let `u₁″` and `u₂″` be the two `S″`-morphisms
`X″ → Y″` deduced from `u′`. The subprescheme of `S″` on which `u₁″` and `u₂″` coincide is an induced open subprescheme,
fiberwise closed, as the inverse image of the diagonal prescheme of `Y″` over `S″`. \[Translator note: the source
footnote observes that the fibers of `S′` over `S` are separated.\] It is therefore the inverse image of a subset of
`S`. Since it contains the diagonal in `S″`, it is all of `S″`. Hence `u₁″ = u₂″`, as required.

## 4. Descent of Étale Preschemes: Effectivity Criteria

<!-- label: IX.4 -->

**Proposition.**

<!-- label: IX.4.1 -->

Let `g: S′ → S` be a faithfully flat and quasi-compact morphism. Then `g` is a morphism of effective descent for the
fibered category of preschemes étale, separated, and of finite type over other preschemes.

Indeed, it is a descent morphism for the fibered category in question, by IX.3.3 or by VIII.5.2. It remains to show that
if `X′` is étale, separated, and of finite type over `S′`, and endowed with a descent datum relative to `g: S′ → S`,
then this datum is effective in the fibered category in question. But one sees easily that if `X` is a prescheme over
`S`, then it is étale over `S` if and only if it is étale over `S′`, by Definition IX.1.1 and VIII.3.6. Hence it is
étale, separated, and of finite type over `S` if and only if `X′` is so over `S′`; cf. for example IX.2.4.

<!-- original page 236 -->

It is therefore enough to ensure effectivity of the descent datum on `X` for the fibered category of arrows of `Sch`.
But `X′` is quasi-affine over `S′` by VIII.6.2 and VIII.6.6. One can then conclude using VIII.7.9. Notice that if one
restricts to preschemes étale and **finite** over others, the proof requires less, since one can invoke VIII.2.1
directly.

**Corollary.**

<!-- label: IX.4.2 -->

Let `g: S′ → S` be a universally submersive morphism, let `X′` be an `S′`-prescheme étale, separated, and of finite
type, endowed with a descent datum relative to `g`, and let `S₁ → S` be faithfully flat and quasi-compact. Let `S₁′` and
`X₁′` be deduced from `S′` and `X′` by base change, so that `S₁′ → S₁` is universally submersive and `X₁′` is étale,
separated, and of finite type over `S₁′`, endowed with a descent datum relative to `g₁: S₁′ → S₁`. Then the descent
datum on `X′` is effective if and only if the descent datum on `X₁′` is effective.

This follows from descent theory in categories [IX.D], taking IX.4.1 and IX.3.3 into account.

Similarly one proves:

**Corollary.**

<!-- label: IX.4.3 -->

Let `g: S′ → S` be a universally submersive morphism, let `X′` be an `S′`-prescheme étale and endowed with a descent
datum relative to `g`, and let `(S_i)` be an open covering of `S`. Then the descent datum is effective if and only if,
for every `i`, the corresponding descent datum on `X_i′ = X′ ×_S S_i`, relative to the morphism
`g_i: S_i′ = S′ ×_S S_i → S_i`, is effective.

This last result leads to a local effectivity criterion:

**Proposition.**

<!-- label: IX.4.4 -->

Let `g: S′ → S` be a morphism of finite presentation (VIII.3.6) and universally submersive, let `X′` be a prescheme
étale and of finite presentation over `S′`, endowed with a descent datum relative to `g`, and let `a` be a point of `S`.

<!-- original page 237 -->

Then there exists an open neighborhood `U` of `a` such that the corresponding descent datum on `X_U′ = X′ ×_S U`
relative to

`g_U: S_U′ = S′ ×_S U → S_U = U`

is effective if and only if the corresponding descent datum on `X_a′ = X′ ×_S Spec(𝒪_a)`, relative to

`g_a: S_a′ = S′ ×_S Spec(𝒪_a) → S_a = Spec(𝒪_a)`,

is effective.

Necessity is trivial; let us prove sufficiency. We have an étale prescheme of finite type `X_a` over `S_a`, and an
isomorphism

`(*)  X_a′ ≃ X_a ×_{S_a} S_a′`

compatible with the descent data. By a standard and easy sorites on preschemes defined over an inductive limit of rings
(here the rings `A_f`, where `A` is the ring of an affine open neighborhood of `a`, and `f` runs through the elements of
`A` not in the prime ideal corresponding to `a`), one can find an open neighborhood `U` of `a`, an étale prescheme of
finite type `X_U` over `U = S_U`, and an `S_a`-isomorphism `X_a ≃ X_U ×_{S_U} S_a`. Moreover, after taking `U` small
enough, one may suppose that the isomorphism `(*)` comes from an isomorphism

`X_U′ ≃ X_U ×_{S_U} S_U′`.

The latter might not be compatible with the descent data; however, after shrinking `U`, it will be compatible with them.
This completes the proof.

**Corollary.**

<!-- label: IX.4.5 -->

Under the conditions of IX.4.4, the descent datum on `X′` is effective if and only if, for every `a ∈ S`, the
corresponding descent datum on `X_a′` relative to the morphism `S_a′ = S′ ×_S Spec(𝒪_a) → Spec(𝒪_a)` is effective. When
`S` is locally noetherian and `X′` is separated over `S′`, one may also replace `𝒪_a` by its completion in the preceding
criterion.

<!-- original page 238 -->

The first assertion follows from IX.4.4 and IX.4.3, and the second is then a consequence of IX.4.2. Using IX.4.2 once
more, and the fact that for every noetherian local ring `A` one can find a complete noetherian local ring `B` and a
local homomorphism `A → B` such that `B` is flat over `A` and `B/𝔪B` is any prescribed extension of the residue field
`k = A/𝔪` of `A`, one obtains:

**Corollary.**

<!-- label: IX.4.6 -->

Under the conditions of IX.4.4, suppose in addition that `X′` is separated over `S′` and that `S` is locally noetherian.
Then the descent datum on `X′` is effective if and only if, for every prescheme `S₁` over `S` that is the spectrum of a
complete local ring with algebraically closed residue field, the corresponding descent datum on `X₁′ = X′ ×_S S₁`,
relative to `g₁: S₁′ → S₁`, is effective.

**Theorem.**

<!-- label: IX.4.7 -->

Let `g: S′ → S` be a finite, surjective morphism of finite presentation (the last hypothesis follows from the others if
`S` is locally noetherian). \[Translator note: the source footnote says that in fact it is enough for `g` to be
integral, by a limit argument in the style of EGA IV 8.\] Then `g` is a morphism of effective descent for the fibered
category of preschemes étale, separated, and of finite type over other preschemes.

We must show that if `X′` is étale, separated, and of finite type over `S′`, and endowed with a descent datum relative
to `g`, then this datum is effective. Using IX.4.3, one easily reduces to the case where `S` is noetherian. By IX.4.5,
one may then suppose `S` is the spectrum of a noetherian local ring, hence in particular

`dim S = n < +∞`.

We argue by induction on `dim S = n`, the assertion being trivial for `n < 0`. Suppose therefore `n ≥ 0` and the theorem
proved in dimensions `n′ < n`. By IX.4.6 we are reduced to the case where `S` is the spectrum of a complete local ring;
then `S′` is a finite union of spectra of complete local rings. Hence

`X′ = X₁′ ⨿ X₂′`,

where `X₁′` is **finite** over `S′`, and `X₂′` has no point above any of the closed points

<!-- original page 239 -->

of `S′`. Consider the morphisms

`q₁,q₂: X″ ⇉ X′`

corresponding to the descent datum, compatible with `p₁,p₂: S″ ⇉ S′`. One sees at once that

`X″ = q_i⁻¹(X₁′) ⨿ q_i⁻¹(X₂′)`, `i = 1,2`,

is the analogous canonical decomposition of `X″` over `S″`. This implies `q₁⁻¹(X₁′) = q₂⁻¹(X₁′)`, and consequently `X₁′`
and `X₂′` carry induced descent data.

Let `T` be the open subset of `S` complementary to its closed point. Then `T′ = S′ ×_S T` is the part of `S′`
complementary to the set of closed points, and `X₂′`, which lies entirely over `T′`, is endowed with a descent datum
relative to the morphism `T′ → T` induced by `g`. Since the latter is finite surjective and `dim T < dim S = n`, this
descent datum is effective by the induction hypothesis. Thus it remains only to prove that the descent datum on `X₁′` is
effective; we may therefore suppose from now on that `X′` is étale and **finite** over `S′`. Notice that the induction
argument is unnecessary if one restricts statement IX.4.7 to étale coverings.

Let `S₀` be the spectrum of the residue field of `A`, let `S₀′ = S′ ×_S S₀`, and define `S₀″`, `S₀‴` similarly from the
fiber squares and cubes `S″` and `S‴` of `S′` over `S`. By IX.1.8, the morphisms `S₀ → S`, `S₀′ → S′`, etc. induce
equivalences for the categories of étale coverings of `S` and `S₀`, of `S′` and `S₀′`, etc. From the sorites of descent
theory in categories [IX.D], it follows that `g: S′ → S` is a morphism of effective descent for the fibered category of
étale coverings if and only if the same is true of `g₀: S₀′ → S₀`. But this is indeed the case, for example as a special
case of IX.4.1. This completes the proof.

**Corollary.**

<!-- label: IX.4.8 -->

The conclusion of IX.4.7 remains true if one assumes only that `S′ → S` is universally submersive, of finite type, and
quasi-finite, provided that `S` is locally noetherian.

<!-- original page 240 -->

Indeed, by IX.4.6, one may suppose that `S` is the spectrum of a complete noetherian local ring. Then by IX.2.5, there
exists a finite surjective morphism `S₁ → S` and an `S`-morphism `S₁ → S′`. Since `S₁ → S` is a strict universal descent
morphism for the fibered category under consideration by IX.4.7, and since `S′ → S` is a universal descent morphism for
it, IX.4.8 follows from the general sorites [IX.D].

**Corollary.**

<!-- label: IX.4.9 -->

Let `g: S′ → S` be a morphism of finite type, surjective and universally open, with `S` locally noetherian. Then `g` is
a morphism of effective descent for the fibered category of preschemes étale, separated, and of finite type over other
preschemes.

Proceeding as in IX.4.7, one is reduced to the case where `S` is the spectrum of a complete noetherian local ring `A`.
Let `A₁` be a finite `A`-algebra, with spectrum `S₁`, such that `S₁ → S` is finite and **surjective**, hence a universal
effective descent morphism for the fibered category under consideration by IX.4.7. It follows from the general theorems
[IX.D] that `g` is a morphism of effective descent for that fibered category if and only if the corresponding morphism
`g₁: S₁′ = S′ ×_S S₁ → S₁` is so. Since the latter satisfies the same hypotheses as `g`, we are reduced to proving
IX.4.9 for `S₁` in place of `S`.

Taking first for `A₁` the direct product of the `A/𝔭_i`, for the minimal prime ideals `𝔭_i` of `A`, we are reduced to
the case where `A` is **integral**. One then shows [Translator note: the source refers to EGA IV 14.3.13 and 14.5.4]
that there exists an integral subscheme `S₁` of `S′`, quasi-finite over `S` and dominant over `S`, passing through a
point of the fiber of `S′` over the closed point `y` of `S`. This uses the fact that `S′` is universally open of finite
type over the integral noetherian local `S` and that `S′_y` is nonempty. Since `A` is complete, `S₁` is finite over `S`,
and since it dominates `S`, the morphism `S₁ → S` is surjective. Replacing `S` once more by `S₁`, we are reduced to the
case where `S′` has a section over `S`, where the statement is trivial.

**Theorem.**

<!-- label: IX.4.10 -->

Let `g: S′ → S` be a finite radicial surjective morphism of finite presentation. The last condition is superfluous if
`S` is locally noetherian. \[Translator note: the source footnote says it even suffices that `g` be integral, radicial,
and surjective, by an easy reduction to the case in the text, in the style of EGA IV 8; cf. SGA 4 VIII 1.1.\]

<!-- original page 241 -->

Then the inverse image functor induces an equivalence from the category of preschemes étale over `S` to the category of
preschemes étale over `S′`.

Since the diagonal morphisms from `S′` into `S′ ×_S S′` and `S′ ×_S S′ ×_S S′` are surjective immersions, they induce,
by IX.1.9, equivalences from the categories of preschemes étale over `S′ ×_S S′`, respectively `S′ ×_S S′ ×_S S′`, with
the category of preschemes étale over `S′`. It follows from the descent sorites [IX.D] that every `X′` étale over `S′`
is endowed with one and only one descent datum relative to `g: S′ → S`. Hence IX.3.3 implies that the inverse image
functor by `g`, from preschemes étale over `S` to preschemes étale over `S′`, is **fully faithful**. It remains to show
that it is essentially surjective, that is, that every `X′` étale over `S′` is isomorphic to the inverse image of an `X`
étale over `S`. Since the question is plainly local on `S` **and on** `X′`, one may suppose `S`, `S′`, and `X′` affine.
Then `X′` is separated and of finite type over `S′`, and one can apply the effectivity criterion IX.4.7.

**Corollary.**

<!-- label: IX.4.11 -->

The conclusion of IX.4.9 remains true if the hypothesis on `g` is replaced by: `g` is faithfully flat, quasi-compact,
and radicial.

The proof is the same, invoking IX.4.1 instead of IX.4.7.

Notice that the proof of IX.4.7 is “elementary” in that it does not use the finiteness and comparison theorems for
proper morphisms (EGA III 3, 4, 5). This is no longer true of the following result:

**Theorem.**

<!-- label: IX.4.12 -->

Let `g: S′ → S` be a proper, surjective morphism of finite presentation (the last hypothesis follows from the first if
`S` is locally noetherian). Then `g` is a morphism of effective descent for the fibered category of étale coverings of
preschemes.

By IX.3.3 and IX.2.2, we are reduced to proving that for every étale covering `X′` over `S′`, endowed with a descent
datum relative to `g: S′ → S`, this descent datum is effective. Using IX.4.3, one is easily reduced

<!-- original page 242 -->

to the case where `S` is noetherian; using IX.4.6, one may then suppose that `S` is the spectrum of a **complete**
noetherian local ring `A`. Introduce `S″` and `S‴` as usual, let `S₀` be the spectrum of the residue field of `A`, and
let `S₀′`, `S₀″`, `S₀‴` be deduced from `S′`, `S″`, `S‴` by the base change `S₀ → S`, that is, the fibers of `S′`, `S″`,
`S‴` at the closed point of `S`. By IX.1.10, the morphisms `S₀ → S`, `S₀′ → S′`, etc. induce equivalences from the
category of étale coverings over the target scheme with the category of étale coverings over the source scheme.
Consequently, `g: S′ → S` is a strict descent morphism for the fibered category of étale coverings of preschemes if and
only if `g₀: S₀′ → S₀` is so; this is indeed the case by IX.4.1. This completes the proof of IX.4.12.

In this argument, from IX.1.10 one needed only the fact that the functor considered there is **fully faithful**, which
does **not** use the existence theorem for coherent sheaves in algebraic geometry.

## 5. Translation in Terms of the Fundamental Group

<!-- label: IX.5 -->

Let

`g: S′ → S`

be a **morphism of effective descent** for the fibered category of **étale coverings** of preschemes, for example a
proper, surjective morphism of finite presentation (IX.4.12), or a faithfully flat and quasi-compact morphism.
Introducing as usual `S″` and `S‴`, and denoting by `𝓒`, `𝓒′`, `𝓒″`, `𝓒‴` the categories of étale coverings of `S`,
`S′`, `S″`, `S‴` respectively, one has a 2-exact diagram of categories

`𝓒 → 𝓒′ ⇉ 𝓒″ ⇉⇉ 𝓒‴`

corresponding to the diagram

`S ← S′ ⇐ S″ ⇐⇐ S‴`.

<!-- original page 243 -->

Suppose that the preschemes `S`, `S′`, `S″`, `S‴` are disjoint sums of connected preschemes; this is the case in
particular if they are locally connected, hence a fortiori if they are locally noetherian (for example if `S′` is of
finite type over a locally noetherian `S`). Then the categories `𝓒`, `𝓒′`, ... in the preceding diagram are
multigaloisian categories (V.9), each described by a collection of totally disconnected compact topological groups,
namely the fundamental groups of the connected components of `S`, `S′`, `S″`, `S‴`.

For simplicity we suppose `S` connected, and we shall give a calculation procedure for its fundamental group in terms of
the fibered category formed from `𝓒′`, `𝓒″`, `𝓒‴`, made explicit using the fundamental groups expressing these
categories. The reader should note that the sketched procedure is in fact valid in the general setting of multigaloisian
categories, which need not come from given preschemes `S`, `S′`, `S″`, `S‴`. It is the analogue of the well-known
procedure for calculating the fundamental group of a topological space `S`, a locally finite union of closed subspaces
`S_i` (or an arbitrary union of open subspaces `S_i`), from the fundamental groups of the components of the `S_i` and of
the components of `S_i ∩ S_j`. Of course, the analogous situation for preschemes fits exactly into the general framework
of descent by introducing the prescheme `S′` that is the sum of the `S_i` and the canonical morphism `g: S′ → S`.

Put

`E′ = π₀(S′)`, `E″ = π₀(S″)`, `E‴ = π₀(S‴)`,

where `π₀` denotes the functor “set of connected components.” Since the fiber products of `S′` over `S` form a
simplicial object of `Sch`, applying `π₀` gives a simplicial set whose components in dimensions `0, 1, 2` are `E′`,
`E″`, `E‴`. We shall use the simplicial maps

`q_i = π₀(p_i)`, `i = 1,2`, `q_{ij} = π₀(p_{ij})`, `(i,j) = (2,1),(3,2),(3,1)`.

Objects of `E′` will be denoted with a prime, such as `s′`; objects of `E″` and `E‴` will be denoted with double and
triple primes. The fact that `S` is connected is expressed by `π₀(K) = 0`, where `K` is the simplicial set defined by
`g: S′ → S`; equivalently, the equivalence relation in `E′` generated by the pair of maps `(q₁,q₂)` is transitive.

<!-- original page 244 -->

Choose once and for all an element `s₀′` in `E′`, and for each `s′` in `E′` choose an element `s̄′ ∈ E″` such that
`q₁(s̄′) = s₀′` and `q₂(s̄′) = s′`, thereby displaying the connectedness of `S`. \[Translator note: the source footnote
warns that such an element need not exist in all cases; the stated theorem must then be modified, though the corollaries
remain valid.\] For every `s′ ∈ E′` choose a geometric point underlined `s′` in the connected component `s′` of `S′`;
this point enters in fact through the corresponding fiber functor `F_{s′}′` on the multigaloisian category `𝓒′`. The
automorphism group of this functor, that is, the fundamental group of `S′` at that geometric point, will be denoted
`π_{s′}`. Choose similarly geometric points underlined `s″` and underlined `s‴`, giving fiber functors `F_{s″}″` and
`F_{s‴}‴` and fundamental groups `π_{s″}` and `π_{s‴}`. Thus

`π_{s′}  = π₁(S′, underlined s′)`, `π_{s″}  = π₁(S″, underlined s″)`, `π_{s‴}  = π₁(S‴, underlined s‴)`.

For every `s″ ∈ E″`, `p₁(underlined s″)` lies in the same connected component as underlined `q₁(s″)`, so there is an
isomorphism of fiber functors

`F_{s″}″ ∘ p₁^* ≃ F_{q₁(s″)}′`

that is, a “path class” from `p₁(underlined s″)` to underlined `q₁(s″)`. The same observation applies to `q₂` and to the
`q_{ij}`. Choose all these path classes:

`F_{s″}″ ∘ p_i^* ≃ F_{q_i(s″)}′`, `F_{s‴}‴ ∘ p_{ij}^* ≃ F_{q_{ij}(s‴)}″`,

for `i = 1,2` and `(i,j) = (2,1),(3,2),(3,1)`. They give in particular group homomorphisms

`q_i^{s″}: π_{s″} → π_{q_i(s″)}`, `q_{ij}^{s‴}: π_{s‴} → π_{q_{ij}(s‴)}`.

<!-- original page 245 -->

Finally, recall that the split fibered-category structure with fibers `𝓒′`, `𝓒″`, `𝓒‴` also contains isomorphisms of
functors

`p_{21}^* p_1^* ≃ p_{31}^* p_1^*`, `p_{21}^* p_2^* ≃ p_{32}^* p_1^*`, `p_{31}^* p_2^* ≃ p_{32}^* p_2^*`,

deduced from isomorphisms of the two sides respectively with `u_i^*` (`i = 1,2,3`), where `u_i` are the three
projections from `S‴` to `S′`. Making these data explicit, one finds for every `s‴` a well-determined element

`a_i^{s‴} ∈ π_{v_i(s‴)}`,

where `v_i`, `i = 1,2,3`, are the three maps `E‴ → E′` defined by `v_i = π₀(u_i)`, subject to the compatibility
conditions such as

`q_1^{s_1″} q_{21}^{s‴} = int(a_1^{s‴}) q_1^{s_2″} q_{31}^{s‴}`,

with `s_1″ = q_{21}(s‴)`, `s_2″ = q_{31}(s‴)`, and the two analogous conditions involving `a_2` and `a_3`.

The data just described allow one to reconstruct, up to equivalence of fibered categories, the fibered category with
fibers `𝓒′`, `𝓒″`, `𝓒‴`. Hence in principle they must allow one to reconstruct `𝓒` up to equivalence, and therefore its
fundamental group up to isomorphism. In fact, we shall determine the fundamental group at the geometric point
`p(underlined s₀′)` of `S`, that is, the automorphism group of `F_{s₀′}′ ∘ p^*`.

An object `X′` of `𝓒′` is essentially the same as the data of finite sets `X′_{s′}`, for `s′ ∈ E′`, on which the
`π_{s′}` act continuously.

<!-- original page 246 -->

A gluing datum on such an object is then the giving, for every `s″ ∈ E″`, of a bijection

`φ_{s″}: X′_{q₁(s″)} ≃ X′_{q₂(s″)}`

compatible with the actions of `π_{s″}`, acting on the two sides through the homomorphisms
`q_i^{s″}: π_{s″} → π_{q_i(s″)}`. Taking first the `s″` of the form `s̄′`, one sees that such data define bijections

`ψ_{s′}: X′_{s₀′} = F₀′(X′) → X′_{s′}`,

which allow all the `X′_{s′}` to be identified with the same set `F₀′(X′) = X′_{s₀′}`, on which all the groups `π_{s′}`
will then act. With this understood, the bijections `φ_{s″}` correspond to bijections

`g_{s″}: F₀′(X′) ≃ F₀′(X′)`,

subject first to the commutation relations with `π_{s″}`:

a) `g_{s″} q_1^{s″}(g″) = q_2^{s″}(g″) g_{s″}` for `s″ ∈ E″` and `g″ ∈ π_{s″}`,

and also to the relations

b) `g_{s̄′} = g_{s̄₀′}` for `s′ ∈ E′`,

which express the way in which we identified the `X′_{s′}` with one another. Making explicit the condition that such a
gluing datum is in fact a descent datum gives the relations

c) `a_3^{s‴} g_{q_{31}(s‴)} a_1^{s‴} = g_{q_{32}(s‴)} a_2^{s‴} g_{q_{21}(s‴)}` for `s‴ ∈ E‴`.

This gives an equivalence between the category of objects of `𝓒′` endowed with a descent datum

<!-- original page 247 -->

and the category of finite sets on which the groups `π_{s′}` act continuously, endowed in addition with bijections
`g_{s″}` satisfying relations a), b), c). Let `G` be the group generated by the groups `π_{s′}` and the new generators
`g_{s″}`, subject to relations a), b), c), and let `π` be the inverse limit of the quotients of `G` by subgroups of
finite index whose inverse images in the groups `π_{s′}` are open subgroups. One also says that `π` is the **group of
galoisian type generated by the `π_{s′}` and the `g_{s″}`, subject to relations a), b), c)**. One checks at once that
the category under consideration is also equivalent to the category of finite sets on which the topological group `π`
acts continuously. This proves:

**Theorem.**

<!-- label: IX.5.1 -->

Let `g: S′ → S` be a morphism of preschemes that is a morphism of effective descent for the fibered category of étale
coverings of preschemes (cf. IX.4.9 and IX.4.12). Suppose `S` connected, and suppose `S′`, its fiber square `S″`, and
its fiber cube `S‴` are sums of connected preschemes (for example, this holds if `S′` is of finite type over a locally
noetherian connected `S`). Choose as above: a geometric point in every connected component of `S′`, `S″`, `S‴`; certain
path classes; an `s₀′ ∈ E′`; and for every `s′ ∈ E′` an `s″ ∈ E″` whose two images in `E′` are `s₀′` and `s′`. Here
`E′`, `E″`, `E‴` denote the sets of connected components of `S′`, `S″`, `S‴` respectively. Then the fundamental group of
`S` at the geometric point image of `s₀′` is canonically isomorphic to the group of galoisian type generated by the
`π_{s′} = π₁(S′, underlined s′)`, for `s′ ∈ E′`, and generators `g_{s″}`, for `s″ ∈ E″`, subject to relations a), b), c)
above, involving the elements of the groups `π_{s″} = π₁(S″, underlined s″)` and the elements `a_i^{s‴}`, for
`i = 1,2,3` and `s‴ ∈ E‴`, introduced above.

**Corollary.**

<!-- label: IX.5.2 -->

Suppose `S′` and `S″` have only finitely many connected components, and that the fundamental groups of the connected
components of `S′` are topologically finitely generated. Then the fundamental group of `S` is topologically finitely
generated.

<!-- original page 248 -->

Thus we shall prove later that the fundamental group of a normal projective scheme over an algebraically closed field is
topologically finitely generated. Using Chow’s lemma and normalization of algebraic schemes, it will follow that the
same result is true for every proper scheme over an algebraically closed field.

**Corollary.**

<!-- label: IX.5.3 -->

Suppose `S′`, `S″`, `S‴` have only finitely many connected components, that the fundamental groups of the connected
components of `S′` are topologically **finitely presented**, and that the fundamental groups of the connected components
of `S″` are topologically **finitely generated**. Then the fundamental group of `S` is topologically **finitely
presented**.

One may express IX.4.9 (restricted to étale **coverings**) by saying that **a finite radicial surjective morphism of
noetherian preschemes induces an isomorphism of fundamental groups**. Figuratively, one can therefore say that the
fundamental group is a **topological invariant** for preschemes. More generally, with the help of IX.5.1, one can make
explicit the effect on the fundamental group of operations on preschemes, such as “pinching” a prescheme along a finite
set of points, which have a simple topological meaning. For example:

**Corollary.**

<!-- label: IX.5.4 -->

Let `g: S′ → S` be a finite morphism of finite presentation, and let `T` be a discrete subset of `S`. For every `s ∈ S`,
let `n(s)` be the “geometric number of points” in the fiber `g⁻¹(s)`, which can also be made explicit as the separable
degree of `g⁻¹(s)` over `κ(s)`, the sum of the separable degrees of its residue extensions. Suppose that for `s ∈ S − T`
one has `n(s) = 1`. For every `s ∈ T`, let `K_s` be an algebraically closed extension of `κ(s)`, let `I_s` be the set of
geometric points of `S′` with values in `K_s` (a set with `n(s)` elements), let `I_s′` be the complement of one chosen
point of `I_s`, and let `I′` be the union of the `I_s′`. Suppose `S′` connected. Then the fundamental group of `S` is
isomorphic to the group of galoisian type generated by the fundamental group of `S′` and generators `g_i` for `i ∈ I′`,
subject to no additional relation.

<!-- original page 249 -->

The details of the proof are left to the reader. The statement obtained is only the translation, into the language of
group theory, of the fact that one has an equivalence between the category `𝓒` of étale coverings of `S` and the
category of étale coverings `X′` of `S′` **endowed**, for every `s ∈ T`, with a transitive system of bijections between
the `n(s)` fibers of `X′` at the points of `g⁻¹(s)` with values in `K_s`. In this intrinsic form, of course, it is no
longer necessary to suppose `S′` connected.

**Example.**

<!-- label: IX.5.5 -->

One proves easily that the rational curve `ℙ¹_k` over an algebraically closed field `k` is simply connected.
\[Translator note: the source refers to Exposé XI.1.1.\] Hence the fundamental group of a complete rational curve having
exactly one double point, with `n` analytic branches, is the free group of galoisian type on `n − 1` generators. For
example, in the case of an ordinary double point, one finds the fundamental group `ℤ̂`, as announced in I.11 a). On the
other hand, the existence of a cusp (which is a “geometrically unibranch” point) has no influence on the fundamental
group.

**Corollary.**

<!-- label: IX.5.6 -->

Let `g: S′ → S` be a universally submersive morphism of preschemes, with geometrically connected fibers, `S` being
connected. Then `S′` is connected, and, choosing a geometric point `s′` in `S′` and denoting by `s` its image in `S`,
the homomorphism

`π₁(S′,s′) → π₁(S,s)`

is **surjective**. If `g` is a morphism of effective descent for the fibered category of étale coverings of preschemes
(cf. IX.4.12), introducing the geometric point `s″ = diag(s′)` of `S″ = S′ ×_S S′` and the two homomorphisms

`p_1^*, p_2^*: π₁(S″,s″) → π₁(S′,s′)`

induced by the two projections, `π₁(S,s)` is isomorphic to the cokernel of this pair of morphisms in the category of
groups of galoisian type, that is, to the quotient of `π₁(S′,s′)` by the closed normal subgroup generated by the
elements

<!-- original page 250 -->

`p_1^*(g″) p_2^*(g″)⁻¹`, `g″ ∈ π₁(S″,s″)`.

Indeed, by IX.3.4 the functor `X ↦ X ×_S S′` from étale coverings of `S` to étale coverings of `S′` is fully faithful;
this is equivalent to saying that the homomorphism on fundamental groups is an epimorphism (V.6.9). The last assertion
is an immediate consequence of the description IX.5.1.

**Remark.**

<!-- label: IX.5.7 -->

It is not known at present whether the fundamental group of a proper scheme over an algebraically closed field `k` is
topologically finitely presented. \[Translator note: the source footnote says this seems very unlikely for smooth curves
of genus `g ≥ 2` in characteristic `p > 0`; for the largest prime-to-`p` quotient, however, known techniques seem to
give an affirmative answer, even without properness, and it refers to work in preparation by J.-P. Murre.\] Using
IX.5.3, a well-known technique of hyperplane sections, and desingularization of normal surfaces, one reduces to the case
of a **smooth surface over** `k`. This at least allows one to show, by transcendental methods, that the answer is
affirmative in characteristic `0`, without having to assume triangulability of singular algebraic varieties. In
characteristic `p > 0`, the main difficulty seems to lie in the case of curves, for which one only knows that the
fundamental group is a quotient of the one appearing in the classical case (cf. the next exposé), but the kernel by
which one divides is very poorly known.

**Remark.**

<!-- label: IX.5.8 -->

One could make explicit other special cases besides IX.5.4 and IX.5.6 in which IX.5.1 takes a particularly simple form.
An interesting case is that in which `S` is the quotient of `S′` by a finite group `Γ` of automorphisms. **Then the
category of étale coverings of `S` is equivalent to the category of étale coverings `X′` of `S′` on which `Γ` acts
compatibly with its action on `S′`, in such a way that for every `s′ ∈ S′` and every `g ∈ Γ_{s′}`** (where `Γ_{s′}`
denotes **the inertia group** of `s′` in `Γ`), **`g` acts trivially on the fiber** `X′_{s′}`.

If `S′` is connected, this statement is interpreted as follows. Let `𝓒₀′` be the category of étale coverings of `S′` on
which `Γ` acts compatibly with its action on `S′`, without necessarily satisfying the preceding condition on inertia
groups of points of `S′`. One sees easily that this is a galoisian category (V.5), and that for every geometric point
`a′` of `S′`, the fiber functor `X′ ↦ X′_{a′}` on `𝓒₀′` is a fundamental functor. Let `π₁(S′,Γ;a′) = G` be the
automorphism group of this functor, with its usual topology. Then there is a canonical exact sequence

<!-- original page 251 -->

`e → π₁(S′,a′) → G → Γ → e`.

Moreover, for every geometric point `b′` of `S′`, one has an isomorphism `π₁(S′,Γ;b′) → G = π₁(S′,Γ;a′)`, defined up to
inner automorphism coming from `π₁(S′,a′)`. Since `Γ_{b′}` maps evidently into the first group, one obtains a
homomorphism

`u_{b′}: Γ_{b′} → G`,

defined up to inner automorphism coming from `π₁(S′,a′)`, whose composite with `G → Γ` is the canonical immersion
`Γ_{b′} → Γ`. With this understood, **the fundamental group `π₁(S,a)` is canonically isomorphic to the quotient group of
`G = π₁(S′,Γ;a′)` by the closed normal subgroup generated by the images of the homomorphisms `Γ_{b′} → G`**. In
particular, the image of `π₁(S′,a′)` in `π₁(S,a)` is a normal subgroup, and the corresponding quotient is isomorphic to
a quotient of `Γ`.

One can reduce the number of “relations” introduced as follows. For every `g ∈ Γ`, `g ≠ e`, introduce the subprescheme
`S′_g` where the automorphisms `id_S` and `g` coincide; choose a geometric point `b′_{g,i}` in each connected component
of `S′_g`, then one of the corresponding homomorphisms `π₁(S′,Γ;b′_{g,i}) → G`, giving lifts `ḡ_i` of `g` in `G`. It is
enough to take the quotient of `G` by the closed normal subgroup generated by the `ḡ_i`.

When `a′` is fixed by `Γ`, `Γ` acts naturally on `π₁(S′,a′)`, and `G` identifies with the corresponding semidirect
product. Identifying `Γ` with a subgroup of `G`, one sees that among the relations introduced above, taking `b′ = a′`
gives “`g = e`” for `g` in the inertia group. Therefore **if `S′` has a geometric point `a′` fixed by** `Γ` (that is, a
point `s′` whose inertia group is `Γ`), **then `π₁(S,a)` is a quotient of the quotient group of galoisian type of
`π₁(S′,a′)` obtained by making the actions of `Γ` on `π₁(S′,a′)` trivial**; it is even isomorphic to this latter group
if, for every `g ∈ Γ`, the inertia locus `S′_g` is connected, hence passes through the locality of `a′`.

<!-- original page 252 -->

This last assertion is contained in the second description above of the relations to be introduced in `G`.

This result applies in particular if one takes `S′` to be the cartesian power `Xⁿ` of a connected prescheme over an
algebraically closed field, `Γ` to be the symmetric group `𝔖_n` acting in the usual way, and `S` to be the `n`-th
symmetric power of `X`. Taking `a′` to be a geometric point localized on the diagonal, one is under the preceding
conditions, since all inertia loci `S′_g` contain the diagonal. Using the fact, proved in the next exposé, that if `X`
is proper and connected over `k`, the fundamental group of `Xⁿ` identifies with `π₁(X)^n`, one obtains the following
amusing result: **If `X` is proper and connected over an algebraically closed `k`, the fundamental group of its `n`-th
symmetric power, `n ≥ 2`, is isomorphic to the abelianization of the fundamental group of `X`.** I do not know whether
the analogous fact in algebraic topology is known; it should be provable by the same descent method. Taking for example
`X` to be the rational curve `X = ℙ¹_k`, one obtains yet another proof that `ℙ^r_k` is simply connected, using the fact
that `ℙ¹_k` is. Taking now `X` to be a nonsingular curve over `k`, and `n ≥ 2g − 1`, so that `Symⁿ(X)` is fibered over
the Jacobian `J` with projective-space fibers, and hence, as will be seen using the results of the next two exposés, has
the same fundamental group as `J`, one recovers without dévissage the well-known fact that **the fundamental group of
the Jacobian of `X` is isomorphic to the abelianization of the fundamental group of `X`**.

## 6. A Fundamental Exact Sequence. Descent by Morphisms with Relatively Connected Fibers

<!-- label: IX.6 -->

<!-- original page 253 -->

**Theorem.**

<!-- label: IX.6.1 -->

Let `S` be the spectrum of an artinian ring `A` with residue field `k`, let `k̄` be an algebraic closure of `k`, let `X`
be an `S`-prescheme, `X₀ = X ⊗_A k`, `X̄₀ = X ⊗_A k̄`, let `ā` be a geometric point of `X̄`, let `a` be its image in
`X`, and let `b` be its image in `S`. Suppose `X₀` is quasi-compact and **geometrically connected** over `k`. (If `X` is
proper over `S`, this means that `H⁰(X₀,𝒪_{X₀})` is a **local** artinian ring with residue field **radicial** over `k`.)
Then the sequence of canonical homomorphisms

`e → π₁(X̄₀,ā) → π₁(X,a) → π₁(S,b) → e`

is exact, and one has

`π₁(S,b) ≃ π₁(k,k̄)` = the Galois group of `k̄` over `k`.

Since fundamental groups do not change after killing nilpotents, one may suppose `A = k`, which already makes the last
isomorphism evident. Let `k′` be the separable closure of `k` in `k̄`, and consider `X′ = X ⊗_k k′` and the image `a′`
of `ā` in `X′`. One has a canonical sequence

`e → π₁(X̄₀,ā) → π₁(X′,a′) → π₁(S′,b′) → e`,

where `S′ = Spec(k′)`. There is also a canonical homomorphism from this sequence to the corresponding sequence for
`X/k`, coming from the evident diagram. This homomorphism of sequences is an isomorphism by IX.4.11. We are therefore
reduced to proving that the second sequence is exact, that is, we may suppose `k` **perfect**.

Let `k_i` be the finite Galois subextensions of `k` in `k̄`, put `X_i = X ⊗_k k_i`, and let `a_i` be the image of `ā` in
`X_i`. The reader may verify that the natural homomorphism

`π₁(X̄₀,ā) ≃ lim_i π₁(X_i,a_i)`

is an isomorphism. This simply means that an étale covering of `X̄` comes from an étale covering of some `X_i`, and that
the latter is essentially unique after passing to an `X_j` with `j ≥ i`.

<!-- original page 254 -->

On the other hand, let `π_i` be the Galois group of `k_i` over `k`, that is, the opposite group of the group of
`S`-automorphisms of `S_i = Spec(k_i)`. Since the functor `S′ ↦ X ×_S S′` from étale coverings of `S` to étale coverings
of `X` is fully faithful by IX.3.4, it follows that `π_i` is also isomorphic to the opposite of the group of
`X`-automorphisms of the connected principal covering `X_i` of `X`. Hence by V.6.13 one has an exact sequence

`e → π₁(X_i,a_i) → π₁(X,a) → π_i → e`.

Passing to the inverse limit over `i` in these exact sequences gives an exact sequence, since we are in the category of
groups of galoisian type, and this is precisely the sequence considered in IX.6.1.

The geometric translation of right exactness in IX.6.1 is the following:

**Corollary.**

<!-- label: IX.6.2 -->

With the preceding notation, let `X′` be an étale covering of `X`, and let `X̄₀′` be the corresponding étale covering of
`X̄₀`. The following conditions are equivalent:

1. There exists an `S′` étale over `S` and an `X`-isomorphism `X′ ≃ X ×_S S′`. The `S′` is then determined up to unique
    isomorphism by IX.3.4.
1. `X̄₀′` is completely decomposed over `X̄₀`.

If `X′` is connected, these conditions are also equivalent to:

2 bis. `X̄₀′` has a section over `X̄₀`.

This last supplement is essential: the equivalence of 1 and 2 means only that `π₁(S,b)` is the quotient group of
`π₁(X,a)` by the closed normal subgroup generated by the image of `π₁(X̄₀,ā)`, and not by this image itself. Under the
preceding conditions, we shall say that `X′` is a **geometrically trivial** covering of `X`.

<!-- original page 255 -->

**Remark.**

<!-- label: IX.6.3 -->

In IX.6.1 one cannot replace `k̄` by an arbitrary algebraically closed extension of `k`, even if `k` is already assumed
algebraically closed. In other words, it is not generally true that if `X` is a connected algebraic scheme over an
algebraically closed field `k`, its fundamental group is unchanged after replacing `k` by an algebraically closed
extension. This already fails, for instance, in characteristic `p > 0` for the affine line over `k`, because of “higher
ramification” phenomena at the point at infinity, which imply a “continuous” structure for the fundamental group. We
shall see in the next exposé, however, that such phenomena cannot occur if `X` is **proper** over `k`. We shall also
show by transcendental methods that the same is true if `k` has characteristic zero.

**Corollary.**

<!-- label: IX.6.4 -->

Suppose that `a` is localized at an `x ∈ X` that is rational over `k` (or more generally has residue field radicial over
`k`). Then the exact sequence IX.6.1 is split.

One may suppose `S = Spec(k)`. If `x` is rational over `k`, it corresponds to a section `S → X` of `X` over `S`, sending
`b` to `a` and defining a homomorphism `π₁(S,b) → π₁(X,a)` that is the required splitting. If `κ(x)` is radicial over
`k`, one reduces to the preceding case by the base extension `Spec(κ(x)) → Spec(k)`.

**Theorem.**

<!-- label: IX.6.5 -->

Let `f: X → S` be a proper and surjective morphism of finite presentation, with geometrically connected fibers; let `X′`
be a prescheme of finite presentation and proper over `X`; let `s` be a point of `S`; let `F = X_s` be the fiber of `X`
at `s`; and let `F₁′` be a connected component of the fiber `F′ = X′_s` of `X′` at `s`. There exists an open
neighborhood `X₁′` of `F₁′` in `X′`, an `S`-scheme `S₁′` étale over `S`, and an `X`-isomorphism `X₁′ ≃ S₁′ ×_S X` if and
only if `X′` is étale over `X` at the points of `F₁′` and `F₁′` is a geometrically trivial covering of `F`.

Necessity is trivial, so it remains to prove sufficiency. One reduces easily to the case where `S` is noetherian.
Consider the Stein factorization `X → T → S` of `f`, where `T` is the spectrum of the Algebra `f_*(𝒪_X)` on `S`. Since
the fibers of `X` over `S` are geometrically connected and `f` is surjective, the morphism `T → S` is finite,
surjective, and radicial; hence by IX.4.10 every `T′` étale over `T` comes by inverse image from an `S′` étale over `S`.
This reduces us to proving IX.6.5 with `S` replaced by `T`, that is, to the case where `f_*(𝒪_X) = 𝒪_S`.

Consider then the Stein factorization `X′ → S′ → S` of the proper morphism `h: X′ → S`, where `S′` is the spectrum of
the Algebra `h_*(𝒪_{X′})`. The morphisms `X′ → X` and `X′ → S′` define a canonical morphism

`X′ → X ×_S S′`,

and our assertion is contained in the following:

**Corollary.**

<!-- label: IX.6.6 -->

Let `f: X → S` be a proper morphism of locally noetherian preschemes such that `f_*(𝒪_X) = 𝒪_S`, and let `X′` be a
prescheme proper over `X`. Consider the **Stein** factorization `X′ → S′ → S` for `X′ → S` and the canonical morphism
`X′ → X ×_S S′`. Let `s` be a point of `S`, and let `s′` be a point of `S′` above `s`, corresponding to a connected
component `F₁′` of the fiber `X′_s` of `X′` at `s`. The morphism `X′ → X ×_S S′` is an isomorphism above an open
neighborhood `U′` of `s′` étale over `S` if and only if `X′` is étale over `X` at the points of `F₁′` and `F₁′` is a
geometrically trivial covering of the fiber `F = X_s`.

Necessity is again trivial; it remains to prove sufficiency. The conclusion also says that a) the morphism deduced from
`X′ → X ×_S S′` by base change `Spec(Ô_{s′}) → S′` is an isomorphism, and b) `S′` is étale over `S` at `s′`, that is,
`Ô_{s′}` is étale over `Ô_s`. In this form, the conclusion is invariant under the base change `Spec(Ô_s) → S`. Since the
hypotheses are likewise stable under this base change, one may suppose `S` is the spectrum of a complete noetherian
local ring. One may also plainly suppose `X′` connected, which here implies `S′ = Spec(𝒪_{s′})` and `F′ = F₁′`.

<!-- original page 257 -->

Since the set of points of `X′` at which `X′` is étale over `X` is open and contains the fiber `X′_{s′} = F′`, and since
`X′` is proper over `S`, it follows that `X′` is étale over `X`. Since it induces on `F = X_s` an étale covering
isomorphic to `F ⊗_{κ(s)} L`, where `L` is étale over `κ(s)`, IX.1.10 implies that it is isomorphic to a covering of the
form `X ×_S T`, with `T` étale over `S`. Here again it is enough to use full faithfulness of the functor in IX.1.10,
which follows from the fact that a formal isomorphism of coherent sheaves on `X` comes from an isomorphism of those
sheaves.

Thus, if `T` is defined by the finite `A`-algebra `B`, `X′` identifies with the spectrum of the Algebra `𝒪_X ⊗_A B` over
`X`. Since `f_*(𝒪_X) = 𝒪_S`, it follows at once that `h_*(𝒪_{X′})` is defined by `B`, hence the canonical homomorphism
`X′ → X ×_S S′` is precisely the isomorphism `X′ ≃ X ×_S T` under consideration. This completes the proof.

**Corollary.**

<!-- label: IX.6.7 -->

Under the conditions of IX.6.5, there exists a prescheme `S′` étale over `S` and an `X`-isomorphism `X′ ≃ X ×_S S′` if
and only if `X′` is étale over `X` and for every `s ∈ S`, the fiber `X′_s` is a geometrically trivial covering of `X_s`.

Indeed, if this holds, `X′` is the union of open subsets `X_i′` that are isomorphic to inverse images of `S_i′` étale
over `S`. One then sees easily that these `S_i′` glue to an `S′` étale over `S`, and that one obtains an isomorphism
`X′ ≃ X ×_S S′`. For example, one may say that the `X_i′` carry descent data relative to `X → S`, which necessarily glue
to a descent datum on all of `X′` relative to `X → S`; since this datum is effective on the `X_i′`, it follows easily
(by a sorites omitted in no. IX.4) that it is effective. One can also state IX.6.7 as follows:

**Corollary.**

<!-- label: IX.6.8 -->

Let `f: X → S` be a proper surjective morphism of finite presentation, with geometrically connected fibers. Then `f` is
a morphism of effective descent for the fibered category of preschemes finite étale over other preschemes. The functor
`S′ ↦ X ×_S S′` induces an equivalence from the category of preschemes finite étale over `S` to the category of
preschemes

<!-- original page 258 -->

finite étale over `X` that induce on each fiber `X_s` a geometrically trivial covering.

**Remark.**

<!-- label: IX.6.9 -->

Let `f: X → S` be a proper and surjective morphism, with `S` locally noetherian. Then `f` factors as a morphism `X → S′`
satisfying the hypothesis of IX.6.8 followed by a finite surjective morphism `S′ → S` covered by IX.4.7. Thus `f` is a
composite of two morphisms that are **universal effective descent morphisms** for the fibered category of preschemes
finite étale over other preschemes. It follows that `f` itself is a universal effective descent morphism for the fibered
category in question. This recovers IX.4.12 by a different method.

**Remark.**

<!-- label: IX.6.10 -->

The conclusion of IX.6.7 does not remain valid if the hypothesis that `f` is proper is replaced by: `X` is of finite
type over `S` and admits a section over `S` (so `f` is universally submersive and a descent morphism for the fibered
category of preschemes étale over other preschemes), even when `S` is the spectrum of a discrete valuation ring and `X′`
is an étale covering of `X`. To see this, start with a `Z` proper over `S` whose generic fiber is a nonsingular rational
curve and whose special fiber `Z₀` consists of two intersecting lines. For example, if `t` is a uniformizer of the
valuation ring `A`, take the closed subscheme `Z` of `ℙ²_A` defined by the homogeneous equation `x² + y² + tz² = 0`. Let
`X` be the complement of the singular point `a` of `Z₀` in the union `Z ∪ ℙ²_k`. The fibers of `X` are `ℙ¹_k` and
`ℙ²_k − a`, hence geometrically simply connected, meaning that every étale covering of such a fiber is geometrically
trivial.

<!-- original page 259 -->

However, proceeding as in no. IX.4, one easily constructs étale coverings of `X` that do not come from étale coverings
of `S`, by gluing trivial coverings of `Z − a` and of `ℙ²_k − a`. It is possible, on the other hand, that the conclusion
of IX.6.7 remains true if the properness hypothesis is replaced by the hypothesis that `X` be **universally open** of
finite presentation over `S`. \[Translator note: the source adds that this is now proved, with `g` only universally open
and surjective; cf. SGA 4 XV 1.15.\] This is at least true if the fibers of `X` over `S` are geometrically irreducible,
and not merely geometrically connected. We only point out that in this question one can reduce to the case where `S` is
the spectrum of a complete discrete valuation ring with algebraically closed residue field.

The interpretation of IX.6.7 in terms of the fundamental group is the following:

**Corollary.**

<!-- label: IX.6.11 -->

Let `f: X → S` be a proper surjective morphism of finite presentation, with geometrically connected fibers. Suppose `X`,
hence `S`, connected. Let `a` be a geometric point of `X`, `b` its image in `S`, and for every `s ∈ S` choose an
algebraic closure `κ(s)̄` of `κ(s)`, a geometric point `a_s` of `X_s` with values in this extension, and a path class
from `a_s` to `a`. This gives a homomorphism

`π₁(X̄_s,a_s) → π₁(X,a)`,

where `X̄_s = X_s ⊗_{κ(s)} κ(s)̄`. Then the homomorphism `π₁(X,a) → π₁(S,b)` is surjective, and its kernel is the closed
normal subgroup of `π₁(X,a)` generated by the images of the `π₁(X̄_s,a_s)`.

**Remark.**

<!-- label: IX.6.12 -->

Under the conditions of IX.6.7, assuming `S` noetherian, one sees easily that the set of points `s ∈ S` such that the
corresponding fiber is geometrically trivial over `X_s` is constructible; if `X′` is proper over `X`, it is even open,
as one sees from IX.6.6. Thus, if `S` is a Jacobson prescheme (for example of finite type over a field), or if `X′` is
proper over `X`,

<!-- original page 260 -->

it is enough, in order to verify the conditions of IX.6.7, to restrict to the **closed** points `s` of `S`. Likewise, in
IX.6.11 it is then enough to take the `π₁(X̄_s,a_s)` for the closed points of `S`.

## Bibliography

**[IX.D]** J. Giraud, _Méthode de la descente_, Mémoire no. 2 de la Société Mathématique de France, 1964.

**[IX.1]** A. Grothendieck, _Géométrie algébrique et Géométrie formelle_, Séminaire Bourbaki, vol. 11, 1959, no. 182.
