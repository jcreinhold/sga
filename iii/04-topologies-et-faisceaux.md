# Exposé IV. Topologies and sheaves

<!-- label: III.IV -->

*by M. Demazure*[^IV-0-1]

<!-- original page 160 -->

[^N.D.E-IV-0]

This Exposé is intended to acquaint the reader with the essentials of the language of topologies and sheaves (without
cohomology), particularly convenient in questions of passage to the quotient (among others).

The first three sections develop the language of passage to the quotient. The fourth, which is the central part, is the
exposition of the theory of sheaves, oriented principally towards the application to questions of quotients; the fifth
is an application to passage to the quotient in groups and to principal homogeneous fibered objects. The last section
concerns more specifically the category of schemes, and defines various useful topologies on this category.

The reader will profitably refer to [AS], [MA], [D], and SGA 4; [D] in particular as regards the applications of
topologies to the theory of descent, and SGA 4 for questions of universes (particularly mistreated in this Exposé).

## 1. Universal effective epimorphisms

<!-- original page 161 -->

In what follows in this Exposé, we suppose fixed a category `C`.

**Definition 1.1.** *A morphism `u : T → S` is called an* epimorphism *if, for every object `X`, the corresponding map*

```text
X(S) = Hom(S, X) ⟶ X(T) = Hom(T, X)
```

*is injective.*[^IV-1-1] *One says that `u` is a* universal epimorphism *if for every morphism `S′ → S`, the fiber
product `T′ = T ×_S S′` exists, and `u′ : T′ → S′` is an epimorphism.*

<!-- label: III.IV.1.1 -->

<!-- original page 178 -->

**Definition 1.2.** *A diagram*

```text
A —u→ B ⇉_{v₁,v₂} C
```

*of maps of sets is said to be* exact *if `u` is injective and if its image is formed by the elements `b` of `B` such
that `v₁(b) = v₂(b)`. A diagram of the same type in `C` is said to be* exact *if for every object `X` of `C`, the
corresponding diagram of sets*

```text
A(X) → B(X) ⇉ C(X)
```

*is exact; one then also says that `u` makes `A` into a* kernel *of the pair of arrows `(v₁, v₂)`. Dually, a diagram*

```text
C ⇉_{v₁,v₂} B —u→ A
```

*in `C` is said to be exact if it is exact as a diagram in the opposite category `C°`, i.e. if for every object `X` of
`C`, the corresponding diagram of sets*

```text
X(A) → X(B) ⇉ X(C)
```

<!-- original page 162 -->

*is exact.*[^N.D.E-IV-2] *One also says that `u` makes `A` into a* cokernel *of the pair of arrows `(v₁, v₂)`.*

<!-- label: III.IV.1.2 -->

**Definition 1.3.** *A morphism `u : T → S` is called an* effective epimorphism *if the fiber square `T ×_S T` exists,
and if the diagram*

```text
T ×_S T ⇉_{pr₁,pr₂} T —u→ S
```

*is exact, i.e. if `u` makes `S` into a cokernel of `(pr₁, pr₂)`. One says that `u` is a* universal effective
epimorphism *if for every morphism `S′ → S`, the fiber product `T′ = T ×_S S′` exists, and the morphism
`u′ : T′ → S′` is an effective epimorphism.*

<!-- label: III.IV.1.3 -->

One evidently has the implications:

```text
universal effective epimorphism  ⟹  effective epimorphism
            ⇓                                ⇓
universal epimorphism            ⟹  epimorphism,
```

but in general no other implication holds.[^N.D.E-IV-3]

**Definition 1.4.0.**[^N.D.E-IV-4] *We "recall" that a morphism `u : T → S` is said to be* squarable *if for every
morphism `S′ → S`, the fiber product `T ×_S S′` exists.*

<!-- label: III.IV.1.4.0 -->

**Lemma 1.4.** *Consider morphisms `U —v→ T —u→ S`. Then*

*a) `u, v` epimorphisms `⟹ uv` epimorphism `⟹ u` epimorphism,*

*b) `u, v` universal epimorphisms `⟹ uv` universal epimorphism, and `u` squarable `⟹ u` universal epimorphism.*

<!-- label: III.IV.1.4 -->

Lemma 1.4 is trivial from the definitions. From it we conclude:

**Corollary 1.5.** *Let `u : X → Y` and `u′ : X′ → Y′` be universal epimorphisms, such that `Y × Y′` exists; then
`X × X′` exists and `u × u′ : X × X′ → Y × Y′` is a universal epimorphism.*

<!-- label: III.IV.1.5 -->

Let us also note:

<!-- original page 163 -->

**Definition 1.6.0.**[^N.D.E-IV-5] *One says that an object `S` of `C` is* squarable *if its product with every object of
`C` exists. (If `C` has a final object `e`, this is equivalent to saying that the morphism `S → e` is squarable, cf.
1.4.0.)*

<!-- label: III.IV.1.6.0 -->

**Lemma 1.6.** *Let `u : X → Y` be a morphism in `C/S`; for it to be an epimorphism (resp. universal epimorphism, resp.
effective epimorphism, resp. universal effective epimorphism), it suffices that the corresponding morphism in `C` be
such, and this is also necessary if one supposes that `S` is a squarable object of `C`.*

<!-- label: III.IV.1.6 -->

Immediate proof left to the reader. One uses the hypothesis "`S` squarable" in order to interpret the `C`-morphisms from
an object `Y` of `C/S` into an object `Z` of `C` as the `C/S`-morphisms from `Y` into `Z × S`.

**Lemma 1.7.** *With the notation of 1.4: `u, v` effective epimorphisms and `v` universal epimorphism `⟹ uv` effective
epimorphism.*

<!-- label: III.IV.1.7 -->

To see this, one considers the diagram

```text
S ⇇ T ⇇ T ×_S T
  ↑   ↑v   ↑v×_S v
    U ⇇ U ×_S U
        ↖
       U ×_T U
```

<!-- original page 164 -->

One notes that by hypothesis, row 1 and column 1 are exact, and that by virtue of 1.5 and 1.6, `v ×_S v` is an
epimorphism (`v` being a universal epimorphism). The conclusion follows by an evident diagram-chase: if an element of
`X(U)` has the same images in `X(U ×_S U)`, it has *a fortiori* the same images in `X(U ×_T U)`, hence comes from an
element of `X(T)` since column 1 is exact. As row 1 is exact, it suffices to verify that the element under consideration
has the same images in `X(T ×_S T)`, and since `v ×_S v` is an epimorphism, it suffices to verify that the images in
`X(U ×_S U)` are the same, which is indeed the case.

**Proposition 1.8.** *Consider morphisms `U —v→ T —u→ S`. Then `u, v` universal effective epimorphisms `⟹ uv` universal
effective epimorphism, and `u` squarable `⟹ u` universal effective epimorphism.*

<!-- label: III.IV.1.8 -->

The first implication follows at once from 1.7. For the second, one looks at the diagram (of "bisimplicial" type):

```text
S ⇇ T ⇇ T ×_S T
↑uv  ↑   ↑
U ⇇ U ×_S T ⇇ U ×_S T ×_S T
↑    ↑           ↑
U ×_S U ⇇ U ×_S U ×_S T ⇇ U ×_S U ×_S T ×_S T.
```

Columns 1, 2, 3 are exact by virtue of the hypothesis "`uv` universal effective epimorphism", row 2 is exact, since
`U ×_S T → U` is an effective epimorphism (because it has a section over `U`), and the same holds for row 3 (same
reason). An evident diagram-chase then shows that row 1 is exact, i.e. `u` is an effective epimorphism. As the
hypotheses made are invariant under any change of base `S′ → S`, it follows that `u` is in fact a universal effective
epimorphism.

**Corollary 1.9.** *Let `u : X → Y` and `u′ : X′ → Y′` be universal effective epimorphisms, such that `Y × Y′` exists;
then `X × X′` exists and `u × u′ : X × X′ → Y × Y′` is a universal effective epimorphism.*

<!-- label: III.IV.1.9 -->

Proof as for 1.5 by the diagram

```text
Y′ ⇇ X′
↑    ↑u′
X ⇇ X × Y′ ⇇ X × X′
↑u             ↘ u×u′
Y ⇇ Y × Y′.
```

<!-- original page 165 -->

**Corollary 1.10.** *Consider a squarable morphism `u : T → S`, and a change-of-base morphism `S′ → S` which is a
universal effective epimorphism. For `u` to be a universal effective epimorphism, it is necessary and sufficient that
`u′ : T′ = T ×_S S′ → S′` be one:*

```text
T ⇇v′ T′
↓u    ↓u′
S ⇇v  S′.
```

<!-- label: III.IV.1.10 -->

<!-- original page 181 -->

Only the "it suffices" requires a proof. Now if `u′` is a universal effective epimorphism, so is `vu′` by 1.8, and since
`vu′ = uv′`, one concludes by 1.8 that `u` is a universal effective epimorphism.

**Remark 1.11.** *The same reasoning shows that in 1.10 one can replace "universal effective epimorphism" by "universal
epimorphism" or "universal and effective epimorphism", or simply by "epimorphism" (and in this last case, the hypothesis
"`u` squarable" is evidently unnecessary).*

<!-- label: III.IV.1.11 -->

In the proof of 1.8 we used the following result, which deserves to be made explicit:

**Proposition 1.12.** *Let `u : T → S` be a morphism that admits a section. Then `u` is an epimorphism, and if
`T ×_S T` exists, it is an effective epimorphism, and a universal effective epimorphism if moreover `u` is squarable.*

<!-- label: III.IV.1.12 -->

The first assertion is contained in 1.4 a), and the third will follow at once from the second, which it will therefore
suffice to establish. In fact we have a stronger conclusion: for every functor `F : C° → (Ens)` (not necessarily
representable), the diagram of sets

```text
F(S) → F(T) ⇉ F(T ×_S T)
```

is exact. This may be considered as a particular case of the formalism of Čech cohomology (in dimension 0!), which we
content ourselves with recalling here. Suppose simply that `T ×_S T` exists; one then sets

```text
Ȟ⁰(T/S, F) = Ker(F(T) ⇉ F(T ×_S T)).
```

<!-- original page 166 -->

One may evidently regard `Ȟ⁰(T/S, F)` as a contravariant functor in the argument `T` varying in `C/S`, every
`S`-morphism `T′ → T` defining a map

```text
(+)    Ȟ⁰(T/S, F) → Ȟ⁰(T′/S, F).
```

Fix `T` and `T′` in `C/S`. A well-known calculation shows that if there exists an `S`-morphism from `T′` into `T`, the
corresponding map (+) is in fact independent of the choice of this morphism,[^N.D.E-IV-6] so that `Ȟ⁰(T/S, F)` may be
regarded as a functor on the category associated to the set `Ob C/S` preordered by the relation of "domination" (`T′`
dominates `T` if there exists an `S`-morphism from `T′` into `T`). In particular, if `T` and `T′` are isomorphic in this
latter category, i.e. if each dominates the other, then (+) is an isomorphism of sets. This applies in particular to the
case where `T′` is the final object of `C/S`, i.e. essentially `S` itself; in any case `T` dominates `T′ = S`, and the
converse is true precisely if `T/S` has a section. This establishes 1.12 in the strengthened form announced.

**Remark 1.13.** *For various applications, the notions introduced in the present Exposé, and the results stated, must
be developed more generally relative to a family of morphisms `uᵢ : Tᵢ → S` with the same target (instead of a single
morphism `u : T → S`). Thus, such a family will be said to be* epimorphic *if for every object `X` of `C`, the
corresponding map*

```text
X(S) → ∏ᵢ X(Tᵢ)
```

*is injective, and one introduces in the same way the notion of an* effective epimorphic *family and the "universal"
variants of these notions. We shall admit, if need be, in what follows, that the results of the present Exposé extend to
this more general situation.*

<!-- label: III.IV.1.13 -->

**Remark 1.14.** *Every morphism that is at once a monomorphism and an effective epimorphism is an isomorphism.*

<!-- label: III.IV.1.14 -->

<!-- original page 167 -->

Indeed, in the notation of 1.3, the fact that `T → S` be a monomorphism entails that the two morphisms

```text
pr₁, pr₂ : T ×_S T ⇉ T
```

are equal (and are isomorphisms). Now a diagram

```text
C ⇉_{v,v} B —u→ A
```

is exact only if `u` is an isomorphism, as follows immediately from the definition.[^N.D.E-IV-7]

## 2. Descent morphisms

Let us recall the following definitions:

**Definition 2.1.** *Let `f : S′ → S` be a morphism such that `S″ = S′ ×_S S′` exists, and let `u′ : X′ → S′` be an
object over `S′`. One calls* gluing datum *on `X′/S′`, relative to `f`, an `S″`-isomorphism*

```text
c : X″₁ ⥲ X″₂
```

*where `X″ᵢ` (`i = 1, 2`) denotes the inverse image (supposed to exist) of `X′/S′` under the projection
`prᵢ : S″ → S′`. One says that the gluing datum `c` is a* descent datum *if it satisfies the "cocycle condition"*

```text
pr*₃,₁(c) = pr*₃,₂(c) pr*₂,₁(c)
```

<!-- label: III.IV.2.1 -->

<!-- original page 168 -->

*where `prᵢ,ⱼ` (`1 ≤ j < i ≤ 3`) are the canonical projections from `S‴ = S′ ×_S S′ ×_S S′` into `S″` (N.B. one now
supposes that `S‴` also exists), where `pr*ᵢ,ⱼ(c)` is the inverse image of `c`, considered as an `S‴`-morphism from
`X‴ⱼ` into `X‴ᵢ`, and where for every integer `k` between 1 and 3, `X‴_k` denotes the inverse image (supposed to exist)
of `X′/S′` under the projection of index `k`, `qₖ : S‴ → S′`.*

In the second part of the definition, we have therefore used identifications and abuses of writing in current
use,[^N.D.E-IV-8] which experience proves to be harmless, but which it is evidently fitting to avoid in a rigorous
exposition of the theory of descent (which must precisely justify to a certain extent these common abuses of language).
Such a formal exposition ([D]) has been written by Giraud (with the aim of justifying and making precise SGA 1, VII,
which was never written). For a detailed exposition of the results of faithfully flat descent of which constant use will
be made in the present Séminaire, one may consult SGA 1, VIII.

Let `f : S′ → S` still be a morphism such that `S″ = S′ ×_S S′` exists, and let `X` be an object over `S` such that
`X′ = X ×_S S′` and `X″ = X ×_S S″` exist; then the inverse images of `X′` under `prᵢ` (`i = 1, 2`) exist and are
canonically isomorphic, and consequently `X′/S′` is endowed with a canonical gluing datum relative to `f`. When `S‴`
and `X‴ = X ×_S S‴` exist, this is even a descent datum. If `Y` is another object over `S`, satisfying the same
conditions as `X/S`, then for every `S`-morphism `X → Y`, the corresponding `S′`-morphism `X′ → Y′` is "compatible with
the canonical gluing data" on `X′, Y′`. If in particular `S′ → S` is a squarable morphism, then

```text
X ⟼ X′ = X ×_S S′
```

is a functor from the category `C/S` into the "category of objects over `S′` equipped with a descent datum relative to
`f`" — a category whose definition is left to the reader, and which is a full subcategory of the "category of objects
over `S′` equipped with a gluing datum relative to `f`".

This being so:

**Definition 2.2.** *One says that a morphism `f : S′ → S` is a* descent morphism *(resp. an* effective descent
morphism*) if `f` is squarable (i.e. for every `X → S`, the fiber product `X ×_S S′` exists), and if the preceding
functor `X ⟼ X′ = X ×_S S′` from the category `C/S` of objects over `S`, into the category of objects over `S′` equipped
with a descent datum relative to `f`, is fully faithful (resp. an equivalence of categories).*

<!-- label: III.IV.2.2 -->

<!-- original page 169 -->

One notes that the first of these two notions can be expressed using only the notion of gluing datum (hence without
involving the triple fiber product `S‴`), `f` being a descent morphism if `f` is squarable and `X ⟼ X′` is a fully
faithful functor from the category `C/S` into the category of objects over `S′` equipped with a gluing datum relative
to `f`. When one makes this definition explicit, one finds that it means that for two objects `X, Y` over `S`, the
following diagram of sets

```text
(×)    Hom_S(X, Y) → Hom_{S′}(X′, Y′) ⇉_{p₁, p₂} Hom_{S″}(X″, Y″)
```

<!-- original page 170 -->

is exact, where `pᵢ(u′)` denotes the inverse image of `u′ ∈ Hom_{S′}(X′, Y′)` under the projection `prᵢ : S″ → S′`, for
`i = 1, 2`; indeed, the kernel of the pair `(p₁, p₂)` is by definition none other than the set of `S′`-morphisms
`X′ → Y′` compatible with the canonical gluing data.

Note that, by definition of the inverse images `Y′, Y″`, one has canonical bijections

```text
Hom_{S′}(X′, Y′) ≃ Hom_S(X′, Y)    and    Hom_{S″}(X″, Y″) ≃ Hom_S(X″, Y),
```

so that the exactness of the diagram (×) is equivalent to that of

```text
(××)    Hom_S(X, Y) → Hom_S(X′, Y) ⇉ Hom_S(X″, Y),
```

obtained by applying `Hom_S(−, Y)` to the diagram in `C/S`:

```text
(×××)   X″ ⇉ X′ → X
```

which is deduced from

```text
S″ ⇉ S′ → S
```

by the base change `X → S`. This proves, taking account of 1.6, the first part of the following proposition:

**Proposition 2.3.** *Let `f : S′ → S` be a morphism. If it is a universal effective epimorphism, it is a descent
morphism, and the converse is true if `S` is a squarable object of `C` (i.e. its product with every object of `C`
exists).*

<!-- label: III.IV.2.3 -->

It remains to prove that if `f` is a descent morphism, it is a universal effective epimorphism, that is, that for every
morphism `X → S`, the diagram (×××) is exact, i.e. for every object `Z` of `C`, the transform of this diagram by
`Hom(−, Z)` is an exact diagram of sets. Now by hypothesis `Z × S` exists; let `Y` be the object of `C/S` that it
defines; then the transform of (×××) by `Hom(−, Z)` is isomorphic to the transform by `Hom_S(−, Y)`, and this last is
exact by the hypothesis on `f`.

One may therefore apply to universal effective epimorphisms the results on descent morphisms, such as the following:

**Proposition 2.4.** *Let `f : S′ → S` be a descent morphism (for example a universal effective epimorphism). Then:*

*a) For every `S`-morphism `u : X → Y`, `u` is an isomorphism (resp. a monomorphism) if and only if `u′ : X′ → Y′` is.*

*b) Let `X, Y` be two subobjects of `S`, `X′` and `Y′` the subobjects of `S′` inverse images of the preceding ones. For
`X` to be contained in `Y` (resp. to be equal to `Y`), it is necessary and sufficient that the same hold for `X′, Y′`.*

<!-- label: III.IV.2.4 -->

<!-- original page 185 -->

For (a), it follows from the definition that if `u′` is an isomorphism in the category of objects with gluing datum,
then `u` is an isomorphism; now one notes at once that every isomorphism of objects over `S′` compatible with gluing
data is an isomorphism of objects with gluing datum, i.e. its inverse is also compatible with the gluing data. For b),
one is reduced to proving that if `X′` is contained in `Y′`, i.e. if there exists an `S′`-morphism `X′ → Y′`, then the
same holds for `X, Y` over `S`. Now since `Y′ → S′`, and hence also `Y″ → S″`, is a monomorphism, one sees that
`X′ → Y′` is automatically compatible with the gluing data, hence comes from an `S`-morphism `X → Y`. Note that the
proof holds more generally when one has two objects `X, Y` over `S`, with `Y → S` a monomorphism, and one asks whether
the morphism `X → S` factors through `Y`: it suffices that `X′ → S′` factor through `Y′`.

**Corollary 2.5.** *Let `f : S′ → S` be a universal effective epimorphism and `g : S → T` a morphism such that
`S ×_T S` exists. Suppose that `S″ = S′ ×_S S′` is also a fiber product of `S′` with itself over `T`, i.e.
`S′ ×_S S′ ⥲ S′ ×_T S′`. Then `g : S → T` is a monomorphism (and conversely, of course).*

<!-- label: III.IV.2.5 -->

Indeed, consider the cartesian diagram

```text
S′ ×_S S′ ⥲ S′ ×_T S′
    ↓             ↓ f
    S    →    S ×_T S,
```

where the second horizontal arrow is the diagonal morphism. By virtue of 1.9 the second vertical arrow `f` is a
universal effective epimorphism, by hypothesis the first horizontal arrow is an isomorphism, hence by virtue of 2.4 a)
or b) at one's choice,[^N.D.E-IV-9] the same holds for `S → S ×_T S`, which means precisely that `g : S → T` is a
monomorphism.

**Remark 2.6.** *The notions introduced in 2.1, in terms of morphisms between certain inverse limits, become explicit in
an obvious way in terms of the contravariant functors defined by the objects `S, S′, X′` under consideration: subject to
the existence of the fiber products envisaged in 2.1, there is a one-to-one correspondence between gluing data (resp.
descent data) on `X′/S′` relative to `S′ → S`, and gluing data (resp. descent data) for the corresponding objects in
`Ĉ = Hom(C°, (Ens))`. This allows one, if one wishes, to extend these notions to the case where one makes no hypothesis
of existence of fiber products in `C`.*

<!-- label: III.IV.2.6 -->

<!-- original page 172 -->

**Remark 2.7.** *The notions introduced in this number generalize to the case of families of morphisms. They can on the
other hand be presented in a more intrinsic manner using the notion of sieve (4.1). For these questions, the reader is
referred to [D].*

<!-- label: III.IV.2.7 -->

## 3. Universal effective equivalence relations

### 3.1. Equivalence relations: definitions

**Definition 3.1.1.** *One calls a* `C`-equivalence relation *in `X ∈ Ob C` a representable subfunctor `R` of the
functor `X × X`, such that for every `S ∈ Ob C`, `R(S)` is the graph of an equivalence relation in `X(S)`.*

<!-- label: III.IV.3.1.1 -->

This definition applies in particular to the category `Ĉ`. If one considers `X` as an object of `Ĉ`, one then sees that
a `Ĉ`-equivalence relation in `X` is nothing other than a subfunctor `R` of `X × X` such that `R(S)` is the graph of an
equivalence relation in `X(S)` for every object `S` of `C`.[^N.D.E-IV-10]

If `R` is a `C`-equivalence relation in `X`, one denotes by `pᵢ` the morphism from `R` into `X` induced by the
projection `prᵢ : X × X → X`. One thus has a diagram

```text
p₁, p₂ : R ⇉ X.
```

<!-- original page 173 -->

**Definition 3.1.2.** *A morphism `u : X → Z` is said to be* compatible *with `R` if `up₁ = up₂`. An object of `C` that
is a cokernel of the pair `(p₁, p₂)` is also called a* quotient object *of `X` by `R` and denoted `X/R`.*

<!-- label: III.IV.3.1.2 -->

One thus has an exact diagram

```text
R ⇉_{p₁, p₂} X —p→ X/R
```

and `X/R` represents the covariant functor

```text
Hom_C(X/R, Z) = {morphisms from X into Z compatible with R}.
```

Since quotient objects have been chosen in `C`, the quotient `X/R` is unique (when it exists).

These definitions generalize at once to the case of a `Ĉ`-equivalence relation in `X`, but one will notice that the
identification of objects of `C` with their images in `Ĉ` does not commute with the formation of quotients, that is, the
quotient `X/R` of `X` by `R` in `C` is not *a priori* a quotient of `X` by `R` in `Ĉ`. One should therefore guard
against rashly identifying `C` with its image in `Ĉ` in questions involving passages to the quotient.[^N.D.E-IV-11]

In what follows, we shall say simply *equivalence relation* for *`Ĉ`-equivalence relation*; we shall specify, when
appropriate, whether we are dealing with `C`-equivalence relations.[^N.D.E-IV-12]

**Definition 3.1.3.** *If `X` is an object of `C` over `S`, one calls an* equivalence relation in `X` over `S` *an
equivalence relation `R` in `X` such that the structural morphism `X → S` is compatible with `R`.*

<!-- label: III.IV.3.1.3 -->

The canonical monomorphism `R → X × X` then factors through the monomorphism

```text
X ×_S X ⟶ X × X
```

and defines an equivalence relation in the object `X → S` of `C/S`. When the quotient `X/R` exists, it is endowed with
a canonical morphism into `S` and the corresponding object of `C/S` is a quotient of `X ∈ Ob C/S` by the preceding
equivalence relation.

<!-- original page 174 -->

Conversely, if `S` is a squarable object of `C` and if `Y → S` is a quotient of `X` by this equivalence relation (in
`C/S`), then `Y` is a quotient of `X` by `R` in `C`. In any case, we shall never have to consider quotients in `C/S`
that are not already quotients in `C`.

**Definition 3.1.4.** *If `X` (resp. `X′`) is an object of `C` equipped with an equivalence relation `R` (resp. `R′`), a
morphism*

```text
u : X → X′
```

*is said to be* compatible with `R` and `R′` *if the following equivalent conditions are satisfied:*

*(i) for every `S ∈ Ob C`, two points of `X(S)` congruent modulo `R(S)` are transformed by `u` into two points of `X′(S)`
congruent modulo `R′(S)`;*

*(ii) there exists a morphism `R → R′` (necessarily unique) making commutative the diagram*

```text
R   →   R′
↓        ↓
X × X → X′ × X′.
        (u × u)
```

<!-- label: III.IV.3.1.4 -->

By the universal property of `X/R`, there then exists (when the quotients `X/R` and `X′/R′` exist) a unique morphism `v`
making commutative the diagram

```text
X   —p→  X/R
↓u         ↓v
X′  —p′→ X′/R′.
```

<!-- original page 175 -->

**Definition 3.1.5.** *A subobject (= a representable subfunctor) `Y` of `X` is said to be* stable under the equivalence
relation `R` *if the following equivalent conditions are satisfied:*

*(i) For every `S ∈ Ob C`, the subset `Y(S)` of `X(S)` is stable under `R(S)`.*

*(ii) The two subobjects of `R` inverse images of `Y` under `p₁` and `p₂` are identical.*

<!-- label: III.IV.3.1.5 -->

An important particular case of stable subobject of `X` is the following: the quotient `X/R` exists and `Y` is the
inverse image on `X` of a subobject of `X/R`.

**Definition 3.1.6.** *Let `R` be an equivalence relation in `X` and `X′ → X` a morphism. The equivalence relation `R′`
in `X′` obtained by the cartesian diagram*

```text
R′      →    R
↓             ↓
X′ × X′ →  X × X
```

*is said to be the equivalence relation in `X′`* inverse image *of the equivalence relation `R` in `X`. In particular,
if `X′` is a subobject of `X`, one says it is the equivalence relation* induced in `X′` by `R`, *and one denotes it
`R_{X′}`.*

<!-- label: III.IV.3.1.6 -->

The morphism `X′ → X` is compatible with `R′` and `R`; one thus has, when the quotients exist, a morphism `X′/R′ → X/R`
(3.1.4). If `X′` is a subobject of `X`, we shall see later that in certain cases one can prove that `X′/R′ → X/R` is a
monomorphism, hence identifies `X′/R′` with a subobject of `X/R`. When this is so, the inverse image of this subobject
in `X` will be a subobject of `X` containing `X′` and stable under `R`: the *saturation* of `X′` for the equivalence
relation `R`.

<!-- original page 176 -->

**Proposition 3.1.7.** *If the subobject `Y` of `X` is stable under `R`, one has two cartesian squares, for `i = 1, 2`:*

```text
R_Y   →  R
↓ pᵢ     ↓ pᵢ
Y     →  X.
```

<!-- label: III.IV.3.1.7 -->

Immediate proof.

### 3.2. Equivalence relation defined by a group acting freely

**Definition 3.2.1.** *Let `X` be an object of `C` and `H` a `C`-group acting on `X` (that is, equipped with a morphism
of `Ĉ`-groups*

```text
H ⟶ Aut(X)).
```

*One says that `H` acts* freely *on `X` if the following equivalent conditions are satisfied:*

*(i) For every `S ∈ Ob C`, the group `H(S)` acts freely on `X(S)`;*

*(ii) The morphism of functors*

```text
H × X ⟶ X × X
```

*defined set-theoretically by `(h, x) ⟼ (hx, x)` is a monomorphism.*

<!-- label: III.IV.3.2.1 -->

(In the preceding definition, one supposed that the group `H` acted "on the left" on `X`. One evidently has an analogous
notion in the case where the group acts "on the right", that is, when one is given a morphism of groups from the group
`H°` opposite to `H` into `Aut(X)`).

If `H` acts freely on `X`, the image of `H × X` under the morphism of (ii) is an equivalence relation in `X` called the
*equivalence relation defined by the action of `H` on `X`*. When the quotient of `X` by this equivalence relation
exists, it is denoted `H\X`

<!-- original page 177 -->

(`X/H` when `H` acts on the right). It represents the following covariant functor: if `Z` is an object of `C`, one has

```text
Hom(H\X, Z) = {morphisms from X into Z invariant under H}
```

where the morphism `f : X → Z` is said to be *invariant under `H`* if for every `S ∈ Ob C`, the corresponding morphism
`X(S) → Z(S)` is invariant under the group `H(S)`.

**Lemma 3.2.2.** *Under the conditions of 3.2.1, let `Y` be a subobject of `X`. The following conditions are
equivalent:*

*(i) `Y` is stable under the equivalence relation defined by `H` (3.1.5);*

*(ii) For every `S ∈ Ob C`, the subset `Y(S)` of `X(S)` is stable under `H(S)`;*

*(iii) There exists a morphism `f`, necessarily unique, making commutative the diagram*

```text
H × Y  —f→  Y
↓             ↓
H × X   →   X.
```

*Under these conditions, `f` defines a morphism of `Ĉ`-groups*

```text
H ⟶ Aut(Y)
```

*and the equivalence relation defined in `Y` by this action of `H` is none other than the equivalence relation induced
in `Y` by the equivalence relation defined in `X` by the action of `H`.*

<!-- label: III.IV.3.2.2 -->

Immediate proof. One evidently has an analogous statement for a "right action". The action of `H` on `Y` defined above
will be called the *action induced in `Y` by the given action of `H` on `X`*.

<!-- original page 178 -->

Let us now consider the following situation: `H` and `G` are two `C`-groups and one is given a morphism of groups

```text
u : H ⟶ G.
```

Then `H` acts on `G` by translations (one sets set-theoretically `hg = u(h)g`) and acts freely there if and only if `u`
is a monomorphism. The quotient of `G` by this action of `H` is denoted, when it exists, `H\G`. One defines similarly a
right action of `H` on `G` and a quotient `G/H`. These quotients are functorial with respect to the groups in question;
more precisely, one has the following lemma, stated for right quotients:

**Lemma 3.2.3.** *Let `u : H → G` and `u′ : H′ → G′` be two monomorphisms of `C`-groups. Suppose given a morphism of
`C`-groups*

```text
f : G ⟶ G′.
```

*The following conditions are equivalent:*

*(i) `f` is compatible with the equivalence relations defined in `G` and `G′` by `H` and `H′`.*

*(ii) For every `S ∈ Ob C`, one has `f u(H(S)) ⊂ u′(H′(S))`.*

*(iii) There exists a morphism `g : H → H′`, necessarily unique and multiplicative, such that the following diagram is
commutative*

```text
H  —g→  H′
↓u        ↓u′
G  —f→  G′.
```

*Under these conditions, if the quotients `G/H` and `G′/H′` exist, there exists a unique morphism `f̄` making commutative
the diagram*

```text
G   —f→   G′
↓p          ↓p′
G/H —f̄→  G′/H′.
```

<!-- label: III.IV.3.2.3 -->

<!-- original page 179 -->

The first part is proved by reduction to the set-theoretic case. The second follows at once from (i).

One could translate to the present situation the notions introduced above for general equivalence relations. Let us
simply signal the following lemma, whose proof is immediate by reduction to the set-theoretic case:

**Lemma 3.2.4.** *Let `u : H → G` be a monomorphism of `C`-groups and `G′` a sub-`C`-group of `G`. For the subobject `G′`
of `G` to be stable under the equivalence relation defined by `H`, it is necessary and sufficient that `u` factor
through the canonical monomorphism `G′ → G`, and under this condition the action of `H` on `G′` induced by the action of
`H` on `G` defined by `u` is none other than the action deduced from the monomorphism `H → G′` that factors `u`.*

<!-- label: III.IV.3.2.4 -->

### 3.3. Universal effective equivalence relations

**Definition 3.3.1.** *Let `f : X → Y` be a morphism. One calls the* equivalence relation defined by `f` in `X`, *and
denotes by `R(f)`, the `Ĉ`-equivalence relation in `X` image of the canonical monomorphism*

```text
X ×_Y X → X × X.
```

<!-- label: III.IV.3.3.1 -->

**Definition 3.3.2.** *Let `R` be an equivalence relation in `X`. One says that `R` is* effective *if*

*(i) `R` is representable (i.e. is a `C`-equivalence relation);*

*(ii) the quotient `Y = X/R` exists in `C`;*[^N.D.E-IV-13]

*(iii) the diagram*

<!-- original page 180 -->

```text
R ⇉_{p₁, p₂} X —p→ Y
```

*makes `R` the fiber square of `X` over `Y`, that is, `R` is the equivalence relation defined by `p`.*

<!-- label: III.IV.3.3.2 -->

**Scholie 3.3.2.1.**[^N.D.E-IV-14] *If `R` is an effective equivalence relation in `X`, then `p` is an effective
epimorphism (1.3). If `f : X → Y` is an effective epimorphism, then `R(f)` is an effective equivalence relation in `X` a
quotient of which is `Y`. There is therefore a "Galois" one-to-one correspondence between effective equivalence
relations in `X` and effective quotients of `X` (i.e. equivalence classes of effective epimorphisms with source `X`).*

<!-- label: III.IV.3.3.2.1 -->

**Definition 3.3.3.** *One says that the equivalence relation `R` in `X` is* universally effective *if the quotient
`Y = X/R` exists, and if, for every `Y′ → Y`, the fiber products `X′ = X ×_Y Y′` and `R′ = R ×_Y Y′` exist and `R′` is a
fiber square of `X′` over `Y′`. It amounts to the same to say that `R` is effective and that `p : X → X/R` is a
universal effective epimorphism.*

<!-- label: III.IV.3.3.3 -->

**Scholie 3.3.3.1.**[^N.D.E-IV-14] *There is therefore, as above, a one-to-one correspondence between universal
effective equivalence relations in `X` and universal effective quotients of `X`.*

<!-- label: III.IV.3.3.3.1 -->

**Remark 3.3.3.2.**[^N.D.E-IV-14] *Suppose that `C` is the category of `S`-schemes and let `𝔸¹` denote the affine space
of dimension 1 over `S`. Let `R ⊂ X ×_S X` be a universal effective equivalence relation and `p : X → Y` the quotient.
Then, for every open `U` of `Y`, `O(U) = Hom_S(U, 𝔸¹_S)` is the set of elements `φ` of `O(p⁻¹(U)) = Hom_S(p⁻¹(U), 𝔸¹_S)`
such that `φ ∘ pr₁ = φ ∘ pr₂`. In particular, if `R` is given by the action of a group `H` acting freely on the right on
`X` (cf. 3.2.1), then `O(U)` is the set of `φ ∈ O(p⁻¹(U))` such that `φ(xh) = φ(x)`, for every `S′ → S` and
`x ∈ X(S′)`, `h ∈ H(S′)`.*

<!-- label: III.IV.3.3.3.2 -->

**Proposition 3.3.4.** *Let `R` be a universal effective equivalence relation in `X`. Let `f : X → Z` be a morphism
compatible with `R`, hence factoring through `g : X/R → Z`. The following conditions are equivalent:*

*(i) `g` is a monomorphism;*

*(ii) `R` is the equivalence relation defined by `f`.*

<!-- label: III.IV.3.3.4 -->

Indeed, (i) trivially entails (ii); the converse is none other than 2.5.

<!-- original page 181 -->

**Definition 3.3.5.** *Let `H` be a `C`-group acting freely on `X`. One says that `H` acts* effectively, *or that the
action of `H` on `X` is* effective *(resp.* universally effective*), if the equivalence relation defined in `X` by the
action of `H` is effective (resp. universally effective).*

<!-- label: III.IV.3.3.5 -->

### 3.4. (M)-effectivity

In practice, it is most often difficult to characterize universal effective epimorphisms. One often disposes,
nevertheless, of a certain number of morphisms of this type, for example in scheme theory, of faithfully flat
quasi-compact morphisms. This leads to the developments below.

**3.4.1.** Let us first state a certain number of conditions bearing on a family `(M)` of morphisms of `C`:

(a) `(M)` is stable under extension of the base, i.e., every `u : T → S` element of `(M)` is squarable (cf. 1.4.0) and
for every `S′ → S`, `u′ : T ×_S S′ → S′` is an element of `(M)`.

(b) The composite of two elements of `(M)` is in `(M)`.

(c) Every isomorphism is an element of `(M)`.

(d) Every element of `(M)` is an effective epimorphism.

Note that (a) and (b) entail:

(a′) The cartesian product of two elements of `(M)` is in `(M)`: let `u : X → Y` and `u′ : X′ → Y′` be two `S`-morphisms,
elements of `(M)`. If `Y ×_S Y′` exists, then `X ×_S X′` exists and `u ×_S u′` is an element of `(M)`.

<!-- original page 182 -->

This follows from the diagram

```text
Y′    ⇇    X′
↑           ↑u′
X  ⇇  X ×_S Y′  ⇇  X ×_S X′
↑u                   ↘ u×_S u′
Y  ⇇  Y ×_S Y′.
```

Likewise (a) and (d) entail:

(d′) Every element of `(M)` is a universal effective epimorphism.

**3.4.2.** The family `(M₀)` of universal effective epimorphisms satisfies the conditions (a) through (d) of 3.4.1.
Indeed, (a), (c) and (d) are satisfied by definition, (b) follows from 1.8. In what follows, we shall suppose given a
family `(M)` of morphisms of `C` satisfying these conditions: our results will therefore apply in particular to the
family `(M₀)`.

**Definition 3.4.3.** *One says that the equivalence relation `R` in `X` is of* type `(M)` *if it is representable and
if `p₁ ∈ (M)` (which by (b) and (c) entails that `p₂ ∈ (M)`).*

*One says that `R` is* `(M)`-effective *if it is effective and if the canonical morphism `X → X/R` is an element of
`(M)`.*

*One says that the quotient `Y` of `X` is* `(M)`-effective *if the canonical morphism `X → Y` is an element of `(M)`.*

<!-- label: III.IV.3.4.3 -->

The following consequences result from this definition:[^N.D.E-IV-15]

**Proposition 3.4.3.1.** *(i) An `(M)`-effective equivalence relation is of type `(M)` and universally effective.*

*(ii) An `(M)`-effective quotient is universally effective (cf. 3.3.3).*

*(iii) The maps `R ⟼ X/R` and `p ⟼ R(p)` realize a one-to-one correspondence between `(M)`-effective equivalence
relations in `X` and `(M)`-effective quotients of `X`.*

*(iv) `(M₀)`-effective is equivalent to universally effective.*

<!-- label: III.IV.3.4.3.1 -->

Let us prove point (i). Since `R` is `(M)`-effective, one has a cartesian square

```text
R   —p₂→  X
↓p₁          ↓p
X   —p→   X/R,
```

<!-- original page 194 -->

and `p ∈ (M)`. Then, by 3.4.1 (a), `p₁` and `p₂` belong to `(M)`, hence `R` is of type `(M)`.

Set `Y = X/R` and let `Y′ → Y` be an arbitrary morphism. By 3.4.1 (a), the fiber products `X′ = X ×_Y Y′` and
`R′ = R ×_Y Y′` exist and the morphisms `X′ → Y′` and `p′ᵢ : R′ → X′` belong to `(M)`. Finally, since `R = X ×_Y X`, one
obtains, by associativity of the fiber product:

```text
R′ = X ×_Y X ×_Y Y′ = X′ ×_{Y′} X′.
```

This shows that `R′` is `(M)`-effective; hence in particular, `R` is universally effective. This proves (i), and also
(iv). Points (ii) and (iii) follow from this, taking account of Definition 3.3.2.

<!-- original page 183 -->

**3.4.4.** Let `H` be an `S`-group whose structural morphism is an element of `(M)`. Then if `H` acts freely on the
`S`-object `X`, it defines an equivalence relation of type `(M)`. Indeed, by (a) the fiber product `H ×_S X` exists and
`pr₂ : H ×_S X → X` is an element of `(M)`. One says that the action of `H` is `(M)`-effective if the equivalence
relation defined in `X` by this action is `(M)`-effective.

**Proposition 3.4.5 ((M)-effectivity and base change).** *Let `R` be an `(M)`-effective equivalence relation in `X` over
`S`. Set `Y = X/R`. Let `S′ → S` be a change of base such that `Y′ = Y ×_S S′` exists. Then `X′ = X ×_S S′` exists,
`R′ = R ×_S S′` is an `(M)`-effective equivalence relation in `X′` over `S′` and `X′/R′ ≃ (X/R)′`.*

<!-- label: III.IV.3.4.5 -->

Indeed, the canonical morphisms `X → Y` and `R → Y` are elements of `(M)`, hence by (a′) `X′` and `R′` are representable.
By associativity of the product, `R′` is the equivalence relation defined in `X′` by the canonical morphism `X′ → Y′`
which is an element of `(M)`, whence the conclusion.

**Proposition 3.4.6 ((M)-effectivity and cartesian products).** *Let `R` (resp. `R′`) be an `(M)`-effective equivalence
relation in `X` (resp. `X′`) over `S`. If `(X/R) ×_S (X′/R′)` exists, then `X ×_S X′` exists, `R ×_S R′` is an
`(M)`-effective equivalence relation in `X ×_S X′` over `S` and*

```text
(X ×_S X′)/(R ×_S R′) ≃ (X/R) ×_S (X′/R′).
```

<!-- label: III.IV.3.4.6 -->

Set `Y = X/R`, `Y′ = X′/R′`. By (a′), the fiber product `X ×_S X′` exists and the canonical morphism

```text
q : X ×_S X′ → Y ×_S Y′
```

is an element of `(M)`. Now the formula

```text
(X ×_S X′) ×_{(Y ×_S Y′)} (X ×_S X′) ≃ (X ×_Y X) ×_S (X′ ×_{Y′} X′)
```

<!-- original page 184 -->

(all products without subscript are taken over `S`) shows that `R ×_S R′` is the equivalence relation defined by `q` in
`X ×_S X′`, which completes the proof.

**3.4.7.**[^N.D.E-IV-16] Suppose that `C` has a final object `e` and let `f : G → G′` be a morphism of `C`-groups, such
that `f ∈ (M)`. Then, by 3.4.1 (a), the kernel `Ker(f)` is representable by `e ×_{G′} G`, and the morphism
`Ker(f) → e` belongs to `(M)`.

On the other hand, the equivalence relation defined by `f` is the same as that defined by the action of `Ker(f)` (say,
on the right) on `G`, i.e., it is the image of the morphism `G × Ker(f) → G × G`, defined set-theoretically by
`(g, h) ⟼ (g, gh)`. Consequently, one deduces from 3.3.2.1 the following corollary:

**Corollary 3.4.7.1.** *Suppose that `C` has a final object `e` and let `f : G → G′` be a morphism of `C`-groups, such
that `f ∈ (M)`. Then the action of `Ker(f)` on `G` is `(M)`-effective and `G′` is the quotient `G/Ker(f)`.*

<!-- label: III.IV.3.4.7.1 -->

### 3.5. Construction of quotients by descent

It frequently happens that one does not know how to construct a quotient directly, but that one does know how to do so
after a suitable change of base. The present number gives a criterion useful in this situation.

We have seen in §2.1 the definition of a descent datum on an object `X′` over `S′` relative to a morphism `S′ → S`.

**Definition 3.5.1.** *One says that a descent datum on `X′` relative to `S′ → S` is* effective *if `X′` equipped with
this descent datum is isomorphic to the inverse image on `S′` of an object `X` over `S`, equipped with its canonical
descent datum.*

<!-- label: III.IV.3.5.1 -->

If `S′ → S` is a descent morphism (2.2), then the `X` of the definition is unique up to unique isomorphism. To say that
`S′ → S` is an effective descent morphism (2.2), is to say that it is a descent morphism and that every descent datum
relative to this morphism is effective.

Consider now an equivalence relation `R` in an object `X` over `S`. Let `X′` (resp. `X″`, resp. `X‴`) be the inverse
images of `X` on `S′`, `S″ = S′ ×_S S′` and `S‴ = S′ ×_S S′ ×_S S′` and let `R′, R″, R‴` be the equivalence relations
deduced from `R` by inverse image. Suppose that the equivalence relation `R′` in `X′` is `(M)`-effective, and consider
the quotient `Y′ = X′/R′`, which is an object over `S′`. Its two inverse images on `S″` are isomorphic to `X″/R″` by
3.4.5. The `S′`-object `Y′` is therefore endowed with a canonical gluing datum. Using likewise the uniqueness of
`X‴/R‴`, one sees that this is even a descent datum. (Remark: it has been implicitly supposed in this proof that all the
fiber products written existed, which is the case in particular if `S′ → S` is squarable, for example a descent
morphism).

<!-- original page 185 -->

**Proposition 3.5.2.** *Let `R` be an equivalence relation in the object `X` over `S`. Let `S′ → S` be a universal
effective epimorphism. Suppose that every `S`-morphism whose inverse image on `S′` is in `(M)` is itself in `(M)`. The
following conditions are equivalent:*

*(i) `R` is `(M)`-effective in `X`;*

<!-- original page 196 -->

*(ii) `R′` is `(M)`-effective in `X′` and the canonical descent datum on `X′/R′` is effective.*

*If this is so, the "descended" object of `X′/R′` is canonically isomorphic to `X/R`.*

<!-- label: III.IV.3.5.2 -->

The fact that (i) entails (ii) is none other than the translation, in the language of descent, of 3.4.4. If one shows
the converse, the last assertion of the proposition will be a consequence of the fact that a universal effective
epimorphism is a descent morphism (2.3), hence that the "descended object" is unique (up to unique isomorphism).

So let us prove (ii) ⇒ (i). Let `Y′` be the quotient `X′/R′` and `Y` the descended object. As the canonical morphism
`p′ : X′ → X′/R′ = Y′` is by construction compatible with the descent data (its inverse images on `S″` coincide with the
canonical morphism `X″ → X″/R″`), it comes by inverse image on `S′` from an `S`-morphism `p : X → Y`. Since `p′` is an
element of `(M)`, it follows from the hypothesis made on the morphism `S′ → S` that `p` is also an element of `(M)`. As
`p′` is compatible with the equivalence relation `R′`, `p` is compatible with `R`, again because a universal effective
epimorphism is a descent morphism. One thus has a morphism

```text
R ⟶ X ×_Y X.
```

To prove that `R` is `(M)`-effective and that `Y` is isomorphic to `X/R`, it suffices to prove that this morphism is an
isomorphism. Now it becomes one by extension of the base from `S` to `S′`, since `R′` is effective; it is therefore an
isomorphism for the same reason as before (2.4).

<!-- original page 186 -->

Note that the hypothesis of the text is satisfied if one takes for `(M)` the family `(M₀)` of universal effective
epimorphisms and if `C` has fiber products (1.10). One deduces the

**Corollary 3.5.3.** *Suppose that `C` has fiber products (over `S` would suffice). Let `R` be an equivalence relation in
`X` over `S` and `S′ → S` a universal effective epimorphism. The following conditions are equivalent:*

*(i) `R` is universally effective in `X`,*

*(ii) `R′` is universally effective in `X′` and the canonical descent datum on `X′/R′` is effective.*

*If this is so, the "descended" object of `X′/R′` is canonically isomorphic to `X/R`.*

<!-- label: III.IV.3.5.3 -->

## 4. Topologies and sheaves

The notion of sieve, and the presentation of the notion of topology (4.2.1) adopted here (more intrinsic and in many
respects more convenient than the one by covering families of [MA]), are due to J. Giraud [AS].

### 4.1. Sieves

**Definition 4.1.1.** *One calls a* sieve *of the category `C` a subfunctor `C` of the final functor `e : C° → (Ens)`.*

<!-- label: III.IV.4.1.1 -->

<!-- original page 197 -->

To every sieve `C` of `C` one associates the set `E(C)` of objects `X` of `C` such that `C(X) ≠ ∅`, that is, such that
the structural morphism `X → e` factors through `C`. One thus has the equivalences

```text
(+)   X ∈ E(C) ⟺ C(X) = e(X) = {∅}.
      X ∉ E(C) ⟺ C(X) = ∅.
```

<!-- original page 187 -->

The set `E = E(C)` enjoys the following property:

```text
(++)   If X ∈ E and if Hom(Y, X) ≠ ∅, then Y ∈ E.
```

(Note that if one equips the set `Ob C` with its natural preorder structure (`Y` dominating `X` if there exists an arrow
from `Y` into `X`), the sets `E` satisfying (++) are the subsets of `Ob C` that contain every dominator[^N.D.E-IV-17] of
one of their elements.)

Conversely, if `E` is a subset of `Ob C` enjoying property (++), then `E` is written in a unique way in the form `E(C)`
and `C` is defined by the formulas (+). There is therefore a one-to-one correspondence between sieves of `C` and subsets
of `Ob C` satisfying condition (++). By abuse of language, we shall sometimes say that the set `E(C)` is a sieve of `C`.

[^N.D.E-IV-18] Let `C` and `C′` be two sieves of `C`; since they are two subfunctors of the final functor `e`, it amounts
to the same to say that `C` dominates `C′` (for the relation of domination in `Ob Ĉ`), or that `C` is a subfunctor of
`C′`, or yet that `E(C) ⊂ E(C′)`; one then says that `C` is *finer* than `C′`. One sees that this gives an order
structure on the set of sieves of `C`. Furthermore, one has `E(C) ∩ E(C′) = E(C × C′)` and therefore the set of sieves
of `C` is filtered for the order relation "being finer".

Every subset `E` of `Ob Ĉ`, for example a subset of `Ob C`, defines a sieve `C(E)`: the set of `X ∈ Ob C` such that
`F(X) ≠ ∅` for at least one `F ∈ E` satisfies condition (++) and defines the sought sieve.

This sieve can also be defined as the image of the family of morphisms `{F → e, F ∈ E}` in the sense of the following
definition:

**Definition 4.1.2.** *Let `{Fᵢ → F}` be a family of morphisms of `Ĉ` with the same target `F`. One calls* image *of
this family the subfunctor of `F` defined by*

```text
S ⟼ ⋃ᵢ Im Fᵢ(S) ⊂ F(S).
```

<!-- label: III.IV.4.1.2 -->

**Proposition 4.1.3.** *The formation of the image commutes with base extension: in the preceding notation, denote by
`I` the image of the family `{Fᵢ → F}`; for every*

<!-- original page 198 -->

*morphism `G → F` of `Ĉ`, the image of the family of morphisms `{Fᵢ ×_F G → G}` is the subfunctor `I ×_F G` of `G`.*

<!-- label: III.IV.4.1.3 -->

**Definition 4.1.4.0.**[^N.D.E-IV-19] *Let `C` be a sieve of `C`. If `E` is a subset of `Ob C` such that `C(E) = C`, one
says that `E` is a* base *of `C`. Every sieve `C` has a base, for example the set `E(C)`.*

<!-- label: III.IV.4.1.4.0 -->

We propose to describe the set `Hom(C, F)`, where `C` is a sieve of `C` and `F` an object of `Ĉ`, using a base `{Sᵢ}` of
`C`. For each pair `(i, j)`, one has a diagram in `Ĉ`:

```text
Sᵢ × Sⱼ → Sᵢ
↓           ↓
Sⱼ      →  e,
```

whence a diagram of sets

```text
Γ(F) = Hom(e, F) —σ→ ∏ᵢ Hom(Sᵢ, F) ⇉_{τ₁, τ₂} ∏_{i,j} Hom(Sᵢ × Sⱼ, F)
```

such that `τ₁σ = τ₂σ`. One thus has a morphism

```text
Hom(e, F) ⟶ Ker(∏ᵢ Hom(Sᵢ, F) ⇉ ∏_{i,j} Hom(Sᵢ × Sⱼ, F)).
```

One verifies immediately:

**Proposition 4.1.4.** *One has an isomorphism, functorial in `F`,*

```text
Hom(C, F) ⥲ Ker(∏ᵢ Hom(Sᵢ, F) ⇉ ∏_{i,j} Hom(Sᵢ × Sⱼ, F)),
```

*such that the diagram*

```text
Hom(e, F) → Ker(∏ᵢ Hom(Sᵢ, F) ⇉ ∏_{i,j} Hom(Sᵢ × Sⱼ, F))
                        ↑ ≀
Hom(e, F) →            Hom(C, F),
```

*where the last line is induced by the canonical morphism `C → e`, is commutative.*

<!-- label: III.IV.4.1.4 -->

<!-- original page 189 -->

**Corollary 4.1.5.** *Suppose that the fiber products `Sᵢ × Sⱼ` are representable, for example*

<!-- original page 199 -->

*that the `Sᵢ` are squarable. One then has, for every `F ∈ Ob Ĉ`, an isomorphism*

```text
Hom(C, F) ⥲ Ker(∏ᵢ F(Sᵢ) ⇉ ∏_{i,j} F(Sᵢ × Sⱼ)).
```

<!-- label: III.IV.4.1.5 -->

**Remark 4.1.6.** *Let `R` be a sieve of `C`; denote by `R̄` the full subcategory of `C` whose set of objects is `E(R)`
and by*

```text
i_R : R̄ ⟶ C
```

*the inclusion functor. One has an isomorphism, functorial in `F ∈ Ob Ĉ`,*

```text
Hom(R, F) ⥲ Γ(F ∘ i_R)
```

*such that the diagram*

```text
Hom(e, F)  →  Hom(R, F)
   ↕ ≀          ↕ ≀
   Γ(F)    →  Γ(F ∘ i_R),
```

*where the second line is induced by the functor `i_R`, is commutative.*

<!-- label: III.IV.4.1.6 -->

**Definition 4.1.7.** *Let `C` be a category. One calls a* sieve of the object `S` of `C` *a sieve of the category `C/S`.*

<!-- label: III.IV.4.1.7 -->

A sieve of `S` is therefore a sub-`Ĉ`-object of `S`. To it corresponds canonically a subset of `Ob C/S` containing the
source of every arrow whose target it contains. By abuse of language, such a set will also be called a sieve of `S`.

### 4.2. Topologies: definitions

**Definition 4.2.1.** *Let `C` be a category. One calls a* topology *on `C` the datum, for each `S` of `C`, of a set
`J(S)` of sieves of `S`, called* covering sieves *or* refinements *of `S`,*

<!-- original page 190 -->

*the datum satisfying the following axioms:*

*(T 1) For every refinement `R` of `S` and every morphism `T → S`, the sieve `R ×_S T` of `T` is covering ("stability
under base change").*

*(T 2) If `R, C` are two sieves of `S`, if `R` is covering, and if for every `T ∈ Ob C` and every morphism `T → R`, the
sieve `C ×_S T` of `T` is covering, then `C` is a refinement of `S`.*[^N.D.E-IV-20]

*(T 3) If `C ⊃ R` are two sieves of `S` and if `R` is covering, then `C` is covering.*

*(T 4) For every `S`, `S` is a refinement of `S`.*

<!-- label: III.IV.4.2.1 -->

One can reformulate these axioms in the following way. Suppose given a topology `S ⟼ J(S)` on `C` and, for every object
`F` of `Ĉ`, denote by `J(F)` the set of subfunctors `R` of `F` such that for every morphism `T → F` of `Ĉ` where `T` is
representable, `R ×_F T`, which is a sieve of `T`, is covering. By virtue of (T 1), this notation is compatible with the
preceding one. One will also say that `R ∈ J(F)` is a *refinement* of `F`. One verifies immediately that the preceding
axioms entail the following properties:

(T′ 0) If `F ⊃ G` are two objects of `Ĉ`, and if for every `S ∈ Ob C` and every morphism `S → F`, `G ×_F S ∈ J(S)`, then
`G ∈ J(F)`.

(T′ 1) If `G ∈ J(F)`, and if `H → F` is a morphism of `Ĉ`, then `G ×_F H ∈ J(H)`.

(T′ 2) If `F ⊃ G ⊃ H` are three objects of `Ĉ`, if `G ∈ J(F)` and `H ∈ J(G)`, then `H ∈ J(F)`.

(T′ 3) If `F ⊃ G ⊃ H` are three objects of `Ĉ` and if `H ∈ J(F)`, then `G ∈ J(F)`.

(T′ 4) For every `F ∈ Ob Ĉ`, `F ∈ J(F)`.

<!-- original page 191 -->

Conversely, if one gives oneself, for every `F ∈ Ob Ĉ`, a set `J(F)` of subobjects of `F` satisfying the properties
(T′ 0) through (T′ 4), the map `S ⟼ J(S)` defines a topology on `C` and the two preceding constructions are inverse to
each other.

From (T′ 1), (T′ 2) and (T′ 3)[^N.D.E-IV-21] results the following property:

(T′ 5) If `G` and `H` are two subobjects of `F` and if `G, H ∈ J(F)`, then `G ∩ H ∈ J(F)`.

The set `J(F)`, ordered by the relation `⊃`, is therefore filtered; this remark will be useful later.

**4.2.2.** One says that the topology defined by `J` is *finer* than the topology defined by `J′` if for every
`S ∈ Ob C`, `J(S) ⊃ J′(S)` (it amounts to the same to say that for every `F ∈ Ob Ĉ`, `J(F) ⊃ J′(F)`).

Every set of topologies on `C` has a greatest lower bound: let `I` be an indexing set, and for each `i ∈ I`, let
`S ⟼ Jᵢ(S)` be a topology on `C`. Set `J(S) = ⋂_{i∈I} Jᵢ(S)`; it is immediate that one has thus defined a topology on
`C`, and that this is indeed the greatest lower bound of the given set.

In particular, let us give ourselves, for each `S ∈ Ob C`, a set `E(S)` of sieves of `S`. One calls the *topology
generated by these sets* the least fine topology for which the elements of `E(S)` are refinements of `S` for every `S`.

**Definition 4.2.3.** *Let `{Fᵢ → F}` be a family of morphisms of `Ĉ`. Let `G ⊂ F` be the image (4.1.2) of this family.
The family is said to be* covering *if `G ∈ J(F)`. A morphism is said to be covering if the family reduced to this
morphism is covering.*

<!-- label: III.IV.4.2.3 -->

This definition applies in particular to an inclusion: a sieve `C` of `S` is covering if and only if the canonical
morphism `C → S` is covering.

<!-- original page 192 -->

The axioms (T′ 0) through (T′ 5) entail for covering families the following properties:

(C 0) Let `{Fᵢ → F}` be a family of morphisms of `Ĉ`. If for every representable base change `S → F`, the family
`{Fᵢ ×_F S → S}` is covering, then so is the initial family.

(C 1) For every covering family `{Fᵢ → F}` and every morphism `G → F`, the family `{Fᵢ ×_F G → G}` is covering
("stability under base change").

(C 2) If `{Fᵢ → F}` is a covering family and if, for each `i`, `{F_{ij} → Fᵢ}` is a covering family, then the composite
family `{F_{ij} → F}` is covering ("stability under composition").

(C 3) If `{Gⱼ → F}` is a covering family, and if `{Fᵢ → F}` is a family of morphisms with target `F` such that for each
`j` there exists an `i` such that `Gⱼ → F` factors through `Fᵢ → F`, then `{Fᵢ → F}` is covering ("saturation").

(C 4) Every family reduced to an isomorphism is covering.

Note that (C 2) and (C 3) also entail:

(C 5) If `{Fᵢ → F}` is a family of morphisms with target `F` such that there exists a covering family `{Gⱼ → F}` such
that for every `j` the family `{Fᵢ ×_F Gⱼ → Gⱼ}` is covering, then the family `{Fᵢ → F}` is covering ("a locally covering
family is covering").

**4.2.4.** Conversely, let `C` be a category having fiber products and let us give ourselves, for each `S ∈ Ob C`, a set
of families of morphisms of `C` with target `S`, said to be *covering families*, the datum satisfying axioms (C 1)
through (C 4) (hence also (C 5) which is a consequence). For every `S ∈ Ob C`, let `J(S)` be the set

<!-- original page 193 -->

of sieves of `S` having a covering base (or, what amounts to the same by (C 3), all of whose bases are covering). Then
`S ⟼ J(S)` defines a topology on `C`. The two preceding constructions are inverse to each other.

In fact, in applications, it is impractical to consider all covering families, since one sometimes has fairly simple
descriptions of a "sufficient" number of such families. This leads to posing the following definitions.

**Definition 4.2.5.0.**[^N.D.E-IV-22] *Let `C` be a category. Suppose given, for each `S ∈ Ob C`, a set `P(S)` of
families of morphisms of `C` with target `S`. One calls the* topology generated by `P` *the least fine topology for
which the given families are covering.*

<!-- label: III.IV.4.2.5.0 -->

**Definition 4.2.5.** *Let `C` be a category. One calls a* pretopology *on `C` the datum for each `S ∈ Ob C` of a set
`R(S)` of families of morphisms `{Sᵢ → S}` with target `S`, said to be* covering for the pretopology under consideration,
*satisfying the following axioms:*

*(P 1) For every family `{Sᵢ → S} ∈ R(S)` and every morphism `T → S`, the fiber products `Sᵢ ×_S T` exist and
`{Sᵢ ×_S T → T} ∈ R(T)`.*

<!-- original page 202 -->

*(P 2) If `{Sᵢ → S} ∈ R(S)` and if for each `i`, `{T_{ij} → Sᵢ} ∈ R(Sᵢ)`, then the composite family `{T_{ij} → S}`
belongs to `R(S)`.*

*(P 3) Every family reduced to an isomorphism is covering.*

<!-- label: III.IV.4.2.5 -->

**Proposition 4.2.6.** *For every `S`, let `J(S)` be the set of sieves of `S` covering for the topology generated by the
pretopology `R`. Let `J_R(S)` be the part of `J(S)` formed by the sieves defined by the families of `R(S)`. Then
`J_R(S)` is cofinal in `J(S)`: every refinement of `S` contains a sieve defined by a family of `R(S)`.*

<!-- label: III.IV.4.2.6 -->

<!-- original page 194 -->

For every `S`, let `J′(S)` be the set of sieves of `S` containing a sieve of `J_R(S)`. One evidently has
`J′(S) ⊂ J(S)`. To show that `J(S) = J′(S)`, it suffices to show that the `J′(S)` make a topology on `C`, that is, that
they satisfy axioms (T 1) through (T 4). Now (T 1), (T 3), (T 4) are evidently satisfied. It remains to verify
(T 2).[^N.D.E-IV-23]

So let `U` be an element of `J′(S)` and `C` a sieve of `S`; one supposes that for every `T → U`, the sieve `C ×_S T` is
in `J′(T)` and one must prove that `C ∈ J′(S)`. By definition of `J′`, `U` contains a refinement `U′` defined by a family
`{Sᵢ → S} ∈ R(S)`. Since one has verified (T 3), it suffices to prove that `U′ ∩ C ∈ J′(S)`, so one may suppose that
`U = U′`. By hypothesis, for every `i`, `C ×_S Sᵢ ∈ J′(Sᵢ)`; there therefore exists, for each `i`, a covering family
`{T_{ij} → Sᵢ} ∈ R(Sᵢ)` such that `T_{ij} → Sᵢ` factors through `C ×_S Sᵢ → Sᵢ`. The morphism `T_{ij} → S` therefore
factors through `C → S`, which shows that `C` contains the sieve defined by the composite family `{T_{ij} → S}`, and one
has finished by (P 2).

The axioms (P 1) through (P 3) are those of [MA]. Given the practical interest of pretopologies, we shall interpret each
important result with the aid of a pretopology defining the given topology.

**Remark 4.2.7.** *One can introduce a somewhat more general notion: one gives, for each `S`, a set of covering families
satisfying (P 1), (P 3) and Proposition 4.2.6. This presents itself in particular when the given families satisfy
(P 1), (P 3) and (C 5). The reader may consult [D].*

<!-- label: III.IV.4.2.7 -->

**Definition 4.2.8.** *Let `C` be equipped with a topology, and let `S` be an object of `C`. Let `P(S′)` be a relation
involving an argument `S′ ∈ Ob C/S`. Suppose that `Hom(S″, S′) ≠ ∅` entails `P(S′) ⇒ P(S″)`. One says that `P` is true*
locally on `S` *for the topology under consideration, if the following equivalent conditions are satisfied:*

*(i) The set of `S′ → S` such that `P(S′)` is true is a refinement of `S`.*

*(ii) There exists a refinement of `S` such that `P(S′)` is true for every `S′` of this refinement.*

<!-- original page 195 -->

*(iii) (If the given topology is defined by a pretopology). There exists a covering family for this pretopology such
that `P(S′)` is true for every `S′` of this family.*

<!-- label: III.IV.4.2.8 -->

**Example 4.2.9.** *Let `f : X → Y` be an `S`-morphism. One will say that `f` is* locally an isomorphism *if there exists
a covering family `{Sᵢ → S}` such that for every `i`, `f ×_S Sᵢ`*

<!-- original page 203 -->

*is an isomorphism. It amounts to the same to require that there exist a refinement `R` of `S` such that for every
`T → R`, `X(T) → Y(T)` is an isomorphism.*

<!-- label: III.IV.4.2.9 -->

One will see in the sequel many other examples of "local" language.

### 4.3. Presheaves, sheaves, sheaf associated to a presheaf

**Definition 4.3.1.** *Let `C` be a category. One calls a* presheaf of sets *on `C` any contravariant functor from `C`
into the category of sets. The category `Ĉ = Hom(C°, (Ens))` is called the* category of presheaves *on `C`. If `C` is
equipped with a topology, one says that the presheaf `P` is* separated *(resp.* is a sheaf*) if for every `S ∈ Ob C` and
every `R ∈ J(S)`, the canonical map*

```text
(+)    P(S) = Hom(S, P) ⟶ Hom(R, P)
```

*is injective (resp. bijective). One calls* category of sheaves, *and denotes by `C̃`, the full subcategory of `Ĉ` whose
objects are the sheaves.*[^N.D.E-IV-24]

<!-- label: III.IV.4.3.1 -->

**Proposition 4.3.2.** *Let `P` be a separated presheaf (resp. a sheaf). For every functor `H ∈ Ob Ĉ` and every
`R ∈ J(H)`, the canonical map*

```text
(+)    Hom(H, P) ⟶ Hom(R, P)
```

*is injective (resp. bijective).*

<!-- label: III.IV.4.3.2 -->

Indeed, let `P` be a separated presheaf, `H` a presheaf, `R ∈ J(H)`, and `u, v : H → P` such that `uj = vj`. For every
`f : S → H`, `S ∈ Ob C`, `R ×_H S` is a refinement of `S` and `uf j_S = vf j_S`:

<!-- original page 196 -->

```text
R ×_H S —j_S→ S
   ↓f_R         ↓f
   R    —j→   H   ⇉_{u, v} P.
```

Since `P` is separated, one deduces `uf = vf`. This being true for every representable `S`, one has `u = v`.

Suppose now that `P` is a sheaf. Let `g : R → P`; let us show that it factors through `H`. For every `f : S → H`,
`S ∈ Ob C`, `g ∘ f_R : R ×_H S → P` factors

<!-- original page 204 -->

in a unique way through `S`, hence defines a morphism `h : S → P`, which is evidently functorial in `f`, by uniqueness:

```text
R ×_H S —f_R→ R —g→ P
   ↓j_S          ↓j   ↗h
   S      —f→   H.
```

One has thus defined for every `S` a map from `H(S)` into `P(S)` functorial in `S`, hence a morphism from `H` into `P`
that answers the required conditions.

**Corollary 4.3.2.1.**[^N.D.E-IV-25] *Let `R, F` be two sheaves. If `R` is a refinement of `F`, then `R = F`.*

<!-- label: III.IV.4.3.2.1 -->

Indeed, suppose that `R` is a refinement of `F` and denote by `j` the inclusion `R ↪ F`. By 4.3.2, one has
`Hom(F, R) = End(R)`, hence there exists `π : F → R` such that `π ∘ j = id_R`. One has likewise `End(F) = Hom(R, F)`,
and the equality `j ∘ π ∘ j = j` entails `j ∘ π = id_F`, hence `j` is an isomorphism.

**Proposition 4.3.3 ([AS], 1.3).** *Let `C` be a category. Let `P` be a presheaf on `C`; for every `S ∈ Ob C`, denote by
`J(S)` the set of sieves `R` of `S` such that for every `T → S`, the map*

```text
(+)    Hom(T, P) ⟶ Hom(R ×_S T, P)
```

*is injective (resp. bijective). Then the `J(S)` define a topology on `C`, i.e. satisfy axioms (T 1) through (T 4).*

<!-- label: III.IV.4.3.3 -->

**Corollary 4.3.4.** *Let, for every `S ∈ Ob C`, `K(S)` be a family of sieves satisfying (T 1). Let `P` be a presheaf on
`C`. For it to be separated (resp. a sheaf) for the topology generated by the `K(S)`, it is necessary and sufficient
that for every `S ∈ Ob C` and every `R ∈ K(S)`, the canonical map*

```text
(+)    Hom(S, P) ⟶ Hom(R, P)
```

*be injective (resp. bijective).*

<!-- label: III.IV.4.3.4 -->

<!-- original page 197 -->

**Corollary 4.3.5.** *Let, for each `S ∈ Ob C`, `R(S)` be a set of families of morphisms of `C` with target `S`,
satisfying (P 1) (for example defining a pretopology). Let `P` be a presheaf on `C`. For `P` to be separated (resp. a
sheaf) for the topology generated by `R`, it is necessary and sufficient that for every `S ∈ Ob C` and every family
`{Sᵢ → S} ∈ R(S)`, the map*

```text
P(S) ⟶ ∏ᵢ P(Sᵢ)
```

*be injective, (resp. the diagram*

```text
P(S) ⟶ ∏ᵢ P(Sᵢ) ⇉ ∏_{i,j} P(Sᵢ ×_S Sⱼ)
```

*be exact).*

<!-- label: III.IV.4.3.5 -->

**Definition 4.3.6.** *Let `C` be a category. One calls the* canonical topology *on `C` the finest topology for which
all representable functors are sheaves.*

<!-- label: III.IV.4.3.6 -->

**Corollary 4.3.7.** *For a sieve `R` of `S` to be a refinement for the canonical topology, it is necessary and
sufficient that for every morphism `T → S` of `C` and every `X ∈ Ob C`, the canonical map*

```text
Hom(T, X) ⟶ Hom(R ×_S T, X)
```

*be bijective.*

<!-- label: III.IV.4.3.7 -->

**Definition 4.3.8.** *A sieve covering for the canonical topology will be called a* universal effective epimorphic sieve.

<!-- label: III.IV.4.3.8 -->

**Corollary 4.3.9.** *A universal effective epimorphic family defines a universal effective epimorphic sieve. Conversely,
every squarable family defining a universal effective epimorphic sieve is universal effective epimorphic.*

<!-- label: III.IV.4.3.9 -->

Let us return to the case where `C` is equipped with an arbitrary topology and pass to the construction of the sheaf
associated to a presheaf `P`. Let `S` be an object of `C`. If `R ⊃ R′` are

<!-- original page 198 -->

two refinements of `S`, one has a diagram

```text
Hom(S, P) ⟶ Hom(R, P)
                 ↘
              Hom(R′, P).
```

The ordered set `J(S)` is filtered, as has already been remarked. Since `S` is an element of `J(S)`, one has an evident
morphism

```text
Hom(S, P) ⟶ lim→_{R ∈ J(S)} Hom(R, P).
```

<!-- original page 206 -->

**Definition 4.3.10.0.**[^N.D.E-IV-26] *One sets `Ȟ⁰(S, P) = lim→_{R ∈ J(S)} Hom(R, P)`. One verifies that `Ȟ⁰(S, P)`
depends functorially on `S`, hence defines a functor `LP` by*

```text
(++)   Hom(S, LP) = Ȟ⁰(S, P) = lim→_{R ∈ J(S)} Hom(R, P).
```

<!-- label: III.IV.4.3.10.0 -->

One has by construction morphisms

```text
ℓ_P : P ⟶ LP
z_R : Hom(R, P) → Hom(S, LP).
```

**Lemma 4.3.10.** *(i) For every refinement `R` of `S` and every `u : R → P`, the diagram*

```text
P  —ℓ_P→  LP
↑u           ↑z_R(u)
R  —i_R→  S
```

*is commutative.*

*(ii) For every morphism `v : S → LP`, there exists a refinement `R` of `S` and a morphism `u : R → P` with
`v = z_R(u)`.*

<!-- original page 199 -->

*(iii) Let `Q` be a functor and `u, v : Q → P` such that `ℓ_P u = ℓ_P v`. Then the kernel of the pair `(u, v)` is a
refinement of `Q`.*

*(iv) Let `u : R → P` and `u′ : R′ → P`; for `z_R(u) = z_{R′}(u′)`, it is necessary and sufficient that there exist a
refinement `R″ ⊂ R ∩ R′` of `S` such that `u` and `u′` coincide on `R″`.*

<!-- label: III.IV.4.3.10 -->

*Proof.* (i): One must verify that `z_R(u) i_R = ℓ_P u`. For this, it suffices to verify that the composites of these
two morphisms with every morphism `g : T → R`, where `T` is representable, are equal. Now consider `f = i_R g` and the
fiber product `R′ = R ×_S T`:[^N.D.E-IV-27]

```text
P  —ℓ_P→  LP
↑u           ↑z_R(u)
R  —i_R→  S
↑p           ↑f
R′  —∼→   T (via i_{R′}, g)
```

By definition of `ℓ_P`, `ℓ_P u g = z_R(u) f` (this is the particular case of what one is trying to prove in which `i_R`
is an isomorphism), and now `z_R(u) f = z_R(u) i_R g`.

(ii) and (iv) merely translate the definition of `Hom(S, LP)` as a direct limit.

(iii): If `K` denotes the kernel of the pair `(u, v)`, then for each morphism `f : S → Q` where `S` is representable,
`K ×_Q S` is a subfunctor of the kernel of the pair of arrows `uf, vf : S → P`. One is therefore reduced, by (T′ 0), to
proving the assertion in the case where `Q = S` is representable. But in this case, it follows from (ii) and (iv) that
`K` contains a refinement of `S` hence is a refinement of `S`.

One verifies finally that `P ⟼ LP` defines a functor

<!-- original page 200 -->

```text
L : Ĉ ⟶ Ĉ
```

and `P ⟼ ℓ_P` a morphism of functors

```text
ℓ : Id_Ĉ ⟶ L.
```

Let us now state the essential result:

**Proposition 4.3.11.** *(i) If `P` is any presheaf, `LP` is separated and `ℓ_P : P → LP` is covering (4.2.3).*

*(ii) If `P` is a sheaf, `P → LP` is an isomorphism.*

*(iii) For every presheaf `P` and every separated presheaf (resp. sheaf) `F`, the map*

```text
Hom(ℓ_P, F) : Hom(LP, F) → Hom(P, F)
```

*is injective (resp. bijective).*

*(iv) If `P` is separated, `ℓ_P : P → LP` is a covering monomorphism (hence `P` is a refinement of `LP`), and `LP` is a
sheaf.*

<!-- label: III.IV.4.3.11 -->

*Proof.* (i) First, `P → LP` is covering; indeed, for every morphism `v : S → LP`, there exists, by 4.3.10 (i) and (ii),
a refinement `R` of `S` such that one has a commutative diagram

```text
P  —ℓ_P→  LP
↑v′          ↑v
P ×_{LP} S  ←  S
↑                  ↑i_R
R
```

hence `P ×_{LP} S → S` is covering. It follows, by (C 0), that `P → LP` is covering.

If on the other hand two morphisms `v₁, v₂ : S → LP` induce the same morphism on a refinement `R` of `S`, let us show
that they are equal. There exist refinements `Rᵢ`, `i = 1, 2`, and morphisms `uᵢ : Rᵢ → P` such that `z_{Rᵢ}(uᵢ) = vᵢ`.
Taking `R` small enough, one may suppose `R₁ = R₂ = R`. It then follows from the commutative diagram of 4.3.10

<!-- original page 201 -->

(i) that `ℓ_P u₁ = ℓ_P u₂`. By loc. cit. (iii), `u₁` and `u₂` therefore coincide on a refinement of `R`, hence a
refinement of `S`, which entails that `z_R(u₁) = z_R(u₂)`, by loc. cit. (iv).

(ii) is clear, for if `P` is a sheaf, `Hom(S, P) → Hom(R, P)` is already an isomorphism for every refinement `R` of `S`.

(iii) Let `u` and `v` be two morphisms `LP → F` such that `uℓ_P = vℓ_P`. To show that `u = v`, it suffices to see that
`uf = vf` for every `f : S → LP` where `S` is representable. Now there exists a refinement `R` of `S` and a morphism
`g : R → P` with `f = z_R(g)`. Then `uf` and `vf` coincide on `R` with `uℓ_P g = vℓ_P g`, hence coincide on `R`. If `F`
is separated, one therefore has `uf = vf`. Suppose now that `F` is a sheaf; one then has the commutative diagram

```text
P  —ℓ_P→  LP
↘             ↓
   F   →    LF
```

which shows that `Hom(ℓ_P, F)` is surjective.

(iv) Let us show that if `P` is separated, `P → LP` is a monomorphism. For this, it suffices to see that for every pair
of morphisms `u, v : S → P` (where `S` is representable) such that `ℓ_P u = ℓ_P v` one has `u = v`. Now loc. cit. (iii)
shows that `u` and `v` coincide on a refinement of `S`, hence coincide because `P` is separated. This shows that
`P → LP` is a monomorphism; as it is covering by (i), one obtains that `P` is a refinement of `LP`.

Let us finally show that `LP` is a sheaf. As we already know by (i) that it is a separated presheaf, it suffices to see
that for every `S ∈ Ob C`, every refinement `R` of `S` and every morphism `h : R → LP`, there exists a morphism
`u : S → LP` with `u i_R = h`. Now `R′ = P ×_{LP} R` is a refinement of `R`, since `P` is a refinement of `LP`, hence
`R′` is

<!-- original page 202 -->

a refinement of `S`. Set `u = z_{R′}(h′)`:

```text
P  —ℓ_P→  LP
↑h′           ↑u (via h)
R′  —j→   R   —i_R→  S.
```

One has `u i_{R′} = ℓ_P h′ = hj`, whence `u i_R j = hj`. Since `R′` is a refinement of `R` and since `LP` is separated,
4.3.2 shows that `u i_R = h`.

**Corollary 4.3.12.**[^N.D.E-IV-28] *Let `F` be a sheaf and `R` a sub-`Ĉ`-object of `F`. Then `R` is a separated
presheaf, `ℓ_R : R → LR` is a covering monomorphism, and one has a commutative diagram*

```text
R  —i→  F
↘         ↗ j
   LR.
↑ℓ_R
```

*Consequently, `R` is a refinement of `F` if and only if `j` is an isomorphism.*

<!-- label: III.IV.4.3.12 -->

We have already noted that `R` is separated and that `j` is a monomorphism, cf. N.D.E. (24) and (26). By 4.3.11 (iv),
`ℓ_R` is a covering monomorphism. Therefore, if `j` is an isomorphism, `R` is a refinement of `F`. Conversely, if `i` is
covering, so is `j`, hence it is an isomorphism by 4.3.2.1.

**Remark 4.3.13.** *If `J′(S)` is a cofinal subset of `J(S)`, one has*

```text
Hom(S, LP) = lim→_{R ∈ J′(S)} Hom(R, P).
```

*In particular, let `S ⟼ R(S)` be a pretopology generating the given topology. The functor `L` can be described using
the covering families that are elements of `R(S)`. Making the formula above explicit, one recovers the construction of
[MA].*

<!-- label: III.IV.4.3.13 -->

Denote by `i` the inclusion functor `C̃ → Ĉ`. From Proposition 4.3.11 results the following theorem:

**Theorem 4.3.14.** *There exists a unique functor `a : Ĉ → C̃` such that the following diagram is commutative*

```text
Ĉ  —L→  Ĉ
↓a         ↓L
C̃  —i→  Ĉ,
```

<!-- original page 210 -->

*i.e., for every presheaf `P`, `L(L(P))` is a sheaf. The functors `i` and `a` are adjoint to one another: for every
presheaf `P` and every sheaf `F` one has an isomorphism, functorial in `P` and `F`,*

```text
Hom_Ĉ(P, i(F)) ≃ Hom_C̃(a(P), F),
```

<!-- original page 203 -->

*that is,*

```text
Hom(P, F) ≃ Hom(a(P), F).
```

<!-- label: III.IV.4.3.14 -->

**Definition 4.3.15.** *The sheaf `a(P)` is said to be* associated *to the presheaf `P`.*

<!-- label: III.IV.4.3.15 -->

**Remark 4.3.16.** *As the functor `L` is constructed using inverse limits and filtered direct limits, it commutes with
finite inverse limits.*[^N.D.E-IV-29]

*Moreover, if one identifies `L(P × P)` with `LP × LP`, the morphism `ℓ_{P×P}` is identified with `ℓ_P × ℓ_P`. It follows
for example that if `P` is a presheaf of groups, `LP` is also canonically equipped with a structure of presheaf of
groups and the canonical morphism `P → LP` is a morphism of groups. The same holds for the functor `a`, which shows that
if `P` is a presheaf of groups and `F` a sheaf of groups, one has an isomorphism*

```text
Hom_{Ĉ-gr.}(P, i(F)) ≃ Hom_{C̃-gr.}(a(P), F).
```

*See [D] for more details.*

<!-- label: III.IV.4.3.16 -->

**4.3.17.** If `V` is any category, one calls a *presheaf on `C` with values in `V`* a contravariant functor from `C`
into `V`. To define sheaves with values in `V`, we must first recall the definition of the inverse limit of a functor.
If `R` and `V` are two categories, and

```text
F : R° ⟶ V
```

a contravariant functor from `R` to `V`, one denotes by `lim← F` the object of `V̂` defined as follows:

```text
lim← F(X) = Hom_V̂(X, lim← F) = lim←_{U ∈ Ob R} Hom_V(F(U), X) = Hom(c_X, F),
```

<!-- original page 204 -->

where `X` is a variable object of `V`, where `c_X` denotes the contravariant functor from `R` to `V` that sends each
object of `R` to `X` and each arrow of `R` to `id_X`, and where the last Hom is taken in the category `Hom(R°, V)`. If
`R` has a final object `e_R`, one has `lim← F = F(e_R)`. If `V` is the category of sets, the functor `lim←` is
identified with the functor `Γ`.

If `S` is an object of `C` and `R` a sieve of `S`, denote by `R̄` the full subcategory of `C/S` whose set of objects is
`E(R)` and `i_R : R̄ → C/S` the canonical functor. If `P` is a presheaf on `C` with values in `V`, it defines by
restriction a functor `P_S : (C/S)° → V`. The functor `i_R` induces a morphism of `V̂`:

```text
P(S) = P_S(S) = lim← P_S ⟶ lim←(P_S ∘ i_R).
```

<!-- original page 211 -->

One denotes by `lim←_R P` the object `lim←(P_S ∘ i_R)` of `V̂`. By virtue of 4.1.6, Definition 4.3.1 generalizes to the

**Definition 4.3.18.** *The presheaf `P` on `C` with values in `V` is said to be* separated *(resp.* a sheaf*), if for
every `S ∈ Ob C` and every `R ∈ J(S)`, the canonical morphism of `V̂`*

```text
P(S) ⟶ lim←_R P
```

*is a monomorphism (resp. an isomorphism).*

<!-- label: III.IV.4.3.18 -->

In the case where `V` is the category `(Gr.)` of groups (or any other category of sets equipped with algebraic
structures defined by finite inverse limits), one can see (cf. [D]) that there is equivalence between the following
notions: a presheaf on `C` with values in `(Gr.)` whose underlying presheaf of sets is a sheaf, and a group in the
category of sheaves of sets. Taking account of these identifications, we shall always consider sheaves with values in a
category of sets equipped with algebraic structures defined by finite inverse limits

<!-- original page 205 -->

as sheaves of sets, equipped in the category `C̃` with the corresponding algebraic structure.

### 4.4. Exactness properties of the category of sheaves

**Theorem 4.4.1.** *(i) Arbitrary inverse limits exist in `C̃`; "they are computed in `Ĉ`", i.e. the inclusion functor
`i : C̃ → Ĉ` commutes with inverse limits: if `(X_α)` is an inverse system of sheaves, the presheaf*

```text
lim← i(X_α) : S ⟼ lim← X_α(S)
```

*is a sheaf and one has `i(lim← X_α) = lim← i(X_α)`.*

*(ii) Arbitrary direct limits exist in `C̃`: if `(X_α)` is a direct system of sheaves, one has*

```text
lim→ X_α = a(lim→ i(X_α))
```

*where `lim→ i(X_α)` is the presheaf direct limit of the `i(X_α)`:*

```text
lim→ i(X_α) : S ⟼ lim→ X_α(S).
```

*(iii) The functor `a : Ĉ → C̃` commutes with arbitrary direct limits and with finite inverse limits.*

<!-- label: III.IV.4.4.1 -->

Assertions (i) and (ii) follow formally from the adjunction formula (4.3.14), and[^N.D.E-IV-30] the first assertion of
(iii) follows from (ii). Finally, the second assertion of (iii) has already been pointed out in 4.3.16.

**Scholie 4.4.2.** *This theorem allows one to use the following method to prove in `C̃` an assertion bearing
simultaneously on arbitrary direct limits and finite inverse limits (for example: "every epimorphism is universally
effective", cf. below). One begins by proving the corresponding assertion in the category of sets, then one extends it
"argument by argument" to the category*

<!-- original page 206 -->

*of presheaves. Next, one uses the preceding theorem to pass from the category of presheaves to the category of sheaves.
One will see in the sequel many examples of this method (4.4.3, 4.4.6, 4.4.9, etc.).*

<!-- label: III.IV.4.4.2 -->

<!-- original page 212 -->

Let us finally remark that the assertions relative to the category of presheaves are formally corollaries of the
assertions relative to the category of sheaves. It suffices in fact to take as topology the least fine topology
("chaotic"), that is, the topology defined by `J(S) = {S}` for every `S ∈ Ob C`; every functor is indeed a sheaf for
this topology.

**Proposition 4.4.3.** *Let `F = {Fᵢ → F}` be a family of morphisms of sheaves. The following conditions are
equivalent:*

*(i) `F` is an epimorphic family.*

*(ii) `F` is a universal effective epimorphic family (1.13).*

*(iii) `F` is covering (4.2.3).*

*(iv) The sheaf image of `F` (that is, the sheaf associated to the presheaf image of `F` (4.1.2)) is `F`.*

<!-- label: III.IV.4.4.3 -->

The equivalence of (iii) and (iv) follows from 4.3.12. The other equivalences will follow from the following lemmas.

**Lemma 4.4.4.** *Let `f : X → Y` be a monomorphism of sheaves which is an epimorphism. Then `f` is an isomorphism.*

<!-- label: III.IV.4.4.4 -->

The lemma is first clear in the category of sets. Let us prove it next in the category of presheaves. Consider the
presheaf

```text
V : S ⟼ Y(S) ∐_{X(S)} Y(S);
```

<!-- original page 207 -->

it is the amalgamated sum of `Y` and `Y` under `X` in the category of presheaves.[^N.D.E-IV-31] Denote by `i₁` and `i₂`
the two "coordinate" morphisms `Y → V`. If `X → Y` is an epimorphism in the category of presheaves, then `i₁ = i₂`. In
this case, for each `S`, the map `X(S) → Y(S)` is surjective; as it is also injective, it is a bijection, and therefore
`X → Y` is an isomorphism.

Let us place ourselves finally in the category `C̃` of sheaves. By 4.4.1 (ii), the amalgamated sum in `C̃` of the sheaves
`Y` and `Y` under `X` is the sheaf `Z` associated to the presheaf `V`. Consider the diagram of morphisms:

```text
X —f→ Y ⇉_{i₁, i₂} V —τ→ Z = a(V).
```

One has `i₁ f = i₂ f`, whence `τ i₁ f = τ i₂ f`, and therefore `τ i₁ = τ i₂`, since `f` is an epimorphism in `C̃`. By
point (iii) of the lemma below, the presheaf `V` is separated, hence `τ` is a monomorphism (4.3.11 (iv)). Therefore
`i₁ = i₂`, and we have seen above that this

<!-- original page 213 -->

entails that `f : X → Y` is an isomorphism. This proves Lemma 4.4.4, once one has verified that `V` is separated.

[^N.D.E-IV-32] Let `R_∅` be the presheaf that to every `S ∈ Ob C` associates the empty set; it is an initial object of
`Ĉ`.

**Lemma 4.4.5.** *(i) Suppose that `R_∅ ∉ J(S)`, for every `S ∈ Ob C`. If `(Xᵢ)` is a family of separated presheaves, the
direct sum presheaf `∐ᵢ Xᵢ` is separated.*[^N.D.E-IV-33]

*(ii) Consider an equivalence relation in the category of presheaves:*

```text
X ⇉_{u, v} Y
```

*and let `w : Y → Z` be the quotient. If `X` is a sheaf and `Y` separated, then `Z` is separated.*

*(iii) Consider an amalgamated sum in the category of presheaves, where `u` and `u′` are monomorphisms:*

```text
X  —u→   Y
↓u′         ↘
Y′    →    V.
```

*If `Y` and `Y′` are separated, and `X` a sheaf, then `V` is separated.*

<!-- label: III.IV.4.4.5 -->

(i) Set `X = ∐ᵢ Xᵢ`. Let `S ∈ Ob C` and `τ : R ↪ S` a refinement of `S`, and let `x₁, x₂` be two elements of `X(S)` such
that `x₁ ∘ τ = x₂ ∘ τ`; there exist indices `i, j` such that `x₁ ∈ Xᵢ(S)` and `x₂ ∈ Xⱼ(S)`. Since `R ≠ R_∅`, there
exists a morphism `φ : T → R`, with `T ∈ Ob C`. Then, `x₁ ∘ τ ∘ φ = x₂ ∘ τ ∘ φ`, and since `X(T)` is the disjoint union
of the `X_k(T)`, this entails `i = j`. Then, since `Xᵢ` is separated and a subobject of `X`, the map
`Xᵢ(S) → Xᵢ(R) → X(R)` is injective, and therefore `x₁ = x₂`. This proves that `X` is separated.

Let us prove (iii). Consider the morphisms `i : Y → V` and `j : Y′ → V`, and let `K` be the kernel of:

```text
Y × Y′ ⇉_{p, q} V,
```

where `p = i ∘ pr₁` and `q = j ∘ pr₂`.

Let `S ∈ Ob(C)`. Since `u` and `u′` are monomorphisms, one can identify `X(S)` with its image in `Y(S)` (resp. `Y′(S)`);
denote by `Z(S)` (resp. `Z′(S)`) the complement. Then

<!-- original page 214 -->

`V(S)` is identified with the disjoint union of `Z(S)`, `Z′(S)` and `X(S)`, and one easily sees that the maps
`i(S) : Y(S) → V(S)` and `j(S) : Y′(S) → V(S)` are injective, and that the map

```text
(u × u′)(S) : X(S) ⟶ K(S)
```

is bijective. Consequently, `i` and `j` are monomorphisms, and `u × u′ : X → K` is an isomorphism.

Set `U = Y ∐ Y′`, and let `τ : R ↪ S` be a refinement of `S`; one has a commutative diagram:

```text
U(S)  —U(τ)→  U(R)
↓                  ↓
V(S)  —V(τ)→  V(R).
```

Let `v₁, v₂ ∈ V(S)` whose images in `V(R)` coincide. By the definition of `V`, `v₁, v₂` lift to elements `y₁, y₂` of
`U(S)`; denote by `z₁, z₂` their images in `U(R)`. Then `z₁, z₂` have the same image in `V(R)`.

Since `i : Y → V` and `j : Y′ → V` are monomorphisms, the maps `Y(R) → V(R)` and `Y′(R) → V(R)` are injective. Therefore,
since `Y` and `Y′` are separated, if `y₁` and `y₂` both belong to `Y(S)` or to `Y′(S)`, then `y₁ = y₂`. Otherwise, one
may suppose that `y₁ ∈ Y(S)` and `y₂ ∈ Y′(S)`, whence `z₁ ∈ Y(R)` and `z₂ ∈ Y′(R)`. But then, since `i ∘ z₁ = j ∘ z₂`,
the morphism `z₁ ⊠ z₂ : R → Y × Y′` factors through `K = X`. Moreover, since `X(R) = X(S)` (because `X` is a sheaf),
there exists `x ∈ X(S)` such that `u(x) ∘ τ = z₁ = y₁ ∘ τ` and `u′(x) ∘ τ = z₂ = y₂ ∘ τ`, whence, since `Y` and `Y′` are
separated, `u(x) = y₁` and `u′(x) = y₂`, and therefore `v₁ = v₂`. This proves that `V` is separated.

Let us prove (ii). Let us first remark that the morphism of presheaves

```text
X —u⊠v→ K,
```

where `K` denotes the kernel of the pair of morphisms `w ∘ prᵢ : Y × Y → Z`, is an isomorphism. Indeed, for every
`T ∈ Ob C`, `X(T)` is an equivalence relation in `Y(T)`, so that the diagram

```text
X(T) —u⊠v→ Y(T) × Y(T) ⇉_{w∘pr₁, w∘pr₂} Z(T)
```

is exact in the category of sets.

Let now `S ∈ Ob C` and `g₁, g₂ : S → Z` be two morphisms that coincide on a refinement `τ : R ↪ S` of `S`. Since
`S ∈ Ob C`, one has `Z(S) = Y(S)/X(S)`,

<!-- original page 208 -->

by construction of `Z`, and therefore there exist morphisms `f₁, f₂ : S → Y` such that `w fᵢ = gᵢ`.

Then, `w f₁ τ = w f₂ τ` and therefore, by what precedes, there exists a morphism `φ : R → X` such that `u φ = f₁ τ` and
`v φ = f₂ τ`. Since `X` is a sheaf, there exists `ψ : S → X` such that `φ = ψ τ`, and therefore one has in `Y(R)` the
equalities:

```text
u ψ τ = f₁ τ ,    v ψ τ = f₂ τ.
```

<!-- original page 215 -->

Since `Y(S) → Y(R)` is injective (`Y` being separated), this entails `u ψ = f₁` and `v ψ = f₂`, whence it follows that
`g₁ = g₂`. This proves that `Z` is separated.

**Lemma 4.4.6.**[^N.D.E-IV-34] *(i) Let `{Fᵢ —fᵢ→ F}` be a family of morphisms of presheaves, and let `G ⊂ F` be the
presheaf image. Then the following diagram in `Ĉ` is exact:*

```text
∐ᵢ Fᵢ ×_G ∐ⱼ Fⱼ ⇉_{pr₁, pr₂} ∐ᵢ Fᵢ ⟶ G
```

*i.e., for every presheaf `H`, the following diagram of sets is exact:*

```text
(∗)    Hom(G, H) ⟶ ∏ᵢ Hom(Fᵢ, H) ⇉_{p, q} ∏_{i,j} Hom(Fᵢ ×_G Fⱼ, H).
```

*(ii) Every covering family of morphisms of sheaves is universally effective epimorphic.*

<!-- label: III.IV.4.4.6 -->

(i) Let `H` be a presheaf. The map `f*` which to a morphism `φ : G → H` associates the family of morphisms
`φ ∘ fᵢ : Fᵢ → H` is injective, since for every `S ∈ Ob C`, `φ(S)` is determined by the `(φ ∘ fᵢ)(S)`, since the family
`fᵢ(S) : Fᵢ(S) → G(S)` is surjective. It is clear that the image of `f*` is contained in `Ker(p, q)`. Conversely, let
`φᵢ : Fᵢ → H` be a family of morphisms such that, for every `i, j`, the diagram below is commutative:

```text
Fᵢ ×_G Fⱼ → Fⱼ
↓             ↓ φⱼ
Fᵢ   —φᵢ→  H.
```

Then, for every `S`, the map `∐ᵢ Fᵢ(S) → H(S)` factors uniquely as a map `φ(S) : G(S) → H(S)`, and this defines a
morphism `φ : G → H` such that `f*(φ) = (φᵢ)`. This proves the exactness of the sequence (∗), and point (i).

Let us prove (ii). Since the notion of covering family is stable under base extension, it suffices to show that every
covering family is effective epimorphic. So let `{Fᵢ → F}` be a covering family of morphisms of sheaves, and let `G` be
the presheaf image of this family. Since the family is covering, so is the monomorphism `G ↪ F`, hence, by 4.3.12, one
has `a(G) = F`.

On the other hand, since `G ↪ F` is a monomorphism, the fiber products `Fᵢ ×_G Fⱼ` and `Fᵢ ×_F Fⱼ` are the same. Hence,
by (i), the following diagram of sets is exact, for every presheaf `H`:

```text
(∗∗)   Hom(G, H) ⟶ ∏ᵢ Hom(Fᵢ, H) ⇉_{p, q} ∏_{i,j} Hom(Fᵢ ×_F Fⱼ, H).
```

If moreover `H` is a sheaf, one has

```text
Hom(G, H) = Hom(a(G), H) = Hom(F, H),
```

<!-- original page 216 -->

and then (∗∗) shows that `{Fᵢ → F}` is indeed an effective epimorphic family in the category `C̃` of sheaves.

**Lemma 4.4.7.** *Every family of morphisms of sheaves `{Fᵢ → F}` factors as a covering family `{Fᵢ → G}` and a
monomorphism `G → F`.*

<!-- label: III.IV.4.4.7 -->

It suffices in fact to take for `G` the sheaf image of the given family.

<!-- original page 209 -->

*Proof of Proposition 4.4.3:* one has seen in 4.4.6 that (iii) ⇒ (ii), and one evidently has (ii) ⇒ (i). Let finally
`{Fᵢ → F}` be an epimorphic family; by Lemma 4.4.7, it factors as a covering family followed by a monomorphism. But the
latter, being dominated[^N.D.E-IV-35] by an epimorphic family, is an epimorphism, hence an isomorphism by 4.4.4.

**Remark 4.4.8.**[^N.D.E-IV-36] *As the presheaf image of the family `F` is separated, the construction of the
associated sheaf shows that the conditions of Proposition 4.4.3 are also equivalent to the following:*

*(v) For every `S ∈ Ob C`, every `f ∈ F(S)` is locally in the image of `F`, that is:*

*(vi) For every `S ∈ Ob C` and every `f ∈ F(S)`, the set of `S′ → S` such that the image of `f` in `F(S′)` is in the
image of one of the `Fᵢ(S′)` is a refinement of `S`.*

*(vii) (If the topology is defined by a pretopology `R`). For every `S ∈ Ob C` and every `f ∈ F(S)`, there exists a
family `{Sⱼ → S} ∈ R(S)` such that for every `j` the image `fⱼ` of `f` in `F(Sⱼ)` is in the image of one of the
`Fᵢ(Sⱼ)`.*

<!-- label: III.IV.4.4.8 -->

**Remark 4.4.8.bis.** *If the sheaf `F` is representable, the preceding conditions are also equivalent to:*

*(viii) The set of `T → F` (`T ∈ Ob C`), such that there exist an `i` and a commutative diagram*

```text
Fᵢ → F
↑   ↗
T
```

*is a refinement of `F`.*

<!-- label: III.IV.4.4.8.bis -->

<!-- original page 210 -->

Indeed, if (viii) is satisfied, the presheaf image of the `Fᵢ` is dominated by[^N.D.E-IV-37] a refinement of `F`, which
entails that the family is covering. Conversely, one applies (vi) to `id_F ∈ F(F)`.

This condition is expressed in pictorial language in the following way: *locally on `F`, there exists an `i` such that
`Fᵢ → F` has a section*. In particular, a morphism

<!-- original page 217 -->

`G → F`, where `G` is a sheaf and `F` a representable sheaf, will be covering if and only if it has *locally (on `F`) a
section*.

[^N.D.E-IV-38] The following lemmas will be useful in VI_B, 8.1 and 8.2.

**Lemma 4.4.8.1.** *Let `Q ⊂ P` be presheaves of groups on `C`, `Q` being normal in `P`. Suppose that `P` is separated,
and that `Q` is a sheaf. Then the presheaf of groups `P/Q` is separated. Consequently, one has*

```text
a(P/Q) = L(P/Q) = lim→_{R ∈ J(S)} (P/Q)(R).
```

<!-- label: III.IV.4.4.8.1 -->

It suffices to show the first assertion, since the second follows from it, by 4.3.11 (iv) and (ii). Let `S ∈ Ob C` and
`R` a sieve of `S`, and let `y ∈ P(S)/Q(S)` whose image in `(P/Q)(R)` is the identity. One must show that `y = 1`. Now,
by hypothesis, the morphism `P(S) → P(R)` (resp. `Q(S) → Q(R)`) is injective (resp. an isomorphism), and in the
commutative diagram below, the top row is exact:

```text
1 → Q(S) → P(S) → P(S)/Q(S) → 1
    ↓ ≀    ↓        ↓
1 → Q(R) → P(R) → (P/Q)(R).
```

The result will follow from this, if one shows that the bottom row is exact. Let `f : R → P` whose image in `(P/Q)(R)`
is the identity, and let `φ : T → R` with `T ∈ Ob C`. Then `f ∘ φ` is the identity of `(P/Q)(T) = P(T)/Q(T)`, i.e.
`f ∘ φ ∈ Q(T)`. Therefore, `φ ⟼ f ∘ φ` is a functorial map `R(T) → Q(T)`, hence defines a morphism of functors
`π : R → Q` such that `π(id_R) = f`, whence `f ∈ Q(R)`. This proves the exactness of the bottom row, and the lemma is
proved.

**Lemma 4.4.8.2.** *Let `H ⊂ G` be presheaves of groups on `C`.*

*(i) If `H` is normal in `G`, then `L(H)` is normal in `L(G)`.*

*(ii) If `H` is central in `G`, then `L(H)` is central in `L(G)`.*

<!-- label: III.IV.4.4.8.2 -->

Let `S ∈ Ob C`; it must be shown (cf. I 2.3.6) that `L(H)(S)` is normal (resp. central) in `L(G)(S)`. Let
`h ∈ L(H)(S)` and `g ∈ L(G)(S)`; there exist a sieve `R` of `S` and elements `h′ ∈ H(R)`, `g′ ∈ G(R)`, such that
`h = z_R(h′)` and `g = z_R(g′)` (notation of 4.3.10). Since `z_R` is a morphism of groups, one has
`g h g⁻¹ h⁻¹ = z_R(g′ h′ g′⁻¹ h′⁻¹)`.

In case (i), one has `g′ h′ g′⁻¹ h′⁻¹ ∈ H(R)`, whence `g h g⁻¹ h⁻¹ ∈ LH(S)`; in case (ii),
`g′ h′ g′⁻¹ h′⁻¹ = 1` and therefore `g h g⁻¹ h⁻¹ = 1`.

<!-- original page 218 -->

**Proposition 4.4.9.** *Every equivalence relation in `C̃` is universally effective (3.3.3): let `R` be a `C̃`-equivalence
relation in the sheaf `X`; then the sheaf associated to the separated presheaf*

```text
i(X)/i(R) : S ⟼ X(S)/R(S)
```

*is a universal effective quotient of `X` by `R`.*

<!-- label: III.IV.4.4.9 -->

Let `X/R` be the sheaf quotient of `X` by `R`, which exists by 4.4.1 (ii): `X/R = a(i(X)/i(R))`. We must show that
`X → X/R` is a universal effective epimorphism, and that the morphism `f : R → X ×_{X/R} X` is an isomorphism. The first
assertion has already been proved (4.4.3). As for `f`, it comes by application of the functor `a` from the morphism
`i(R) → i(X) ×_{i(X/R)} i(X)` or, since `i(X)/i(R)` is separated (4.4.5 (ii)) so that `i(X)/i(R) → i(X/R)` is a
monomorphism, from the canonical morphism `i(R) → i(X) ×_{i(X)/i(R)} i(X)`.

One is therefore reduced to proving the same assertion in the category of presheaves. But `i(X)/i(R)` is the presheaf
`S ⟼ X(S)/R(S)` and one is reduced to proving the analogous assertion in the category of sets, where it is immediate.

**Proposition 4.4.10.** *Under the conditions of 4.4.9, let `Y` be a subsheaf of `X`. Denote by `R_Y` the equivalence
relation induced in `Y` by `R`. Then the canonical morphism (3.1.6)*

<!-- original page 211 -->

```text
Y/R_Y ⟶ X/R
```

*is a monomorphism: it identifies `Y/R_Y` with a subsheaf of `X/R`, which is the* sheaf image *of the composite
morphism*

```text
Y ⟶ X ⟶ X/R.
```

<!-- label: III.IV.4.4.10 -->

The morphism of presheaves

```text
i(Y)/i(R_Y) = i(Y)/i(R)_{i(Y)} ⟶ i(X)/i(R)
```

is a monomorphism. Since the functor `a` is left exact (4.3.16), it transforms monomorphisms into monomorphisms, and
therefore

```text
Y/R_Y ⟶ X/R
```

is a monomorphism. The last assertion follows from the commutative diagram

```text
Y     →   X
↓           ↓
Y/R_Y → X/R,
```

and the fact that `Y → Y/R_Y` is covering.

By virtue of this proposition, we shall always identify `Y/R_Y` with a subsheaf of `X/R`.

<!-- original page 219 -->

**Proposition 4.4.11.** *Let `R` be a `C̃`-equivalence relation in the sheaf `X`. For every subsheaf `Y` of `X` stable
under `R`, denote by `Y′` the quotient `Y/R_Y` considered as a subsheaf of `X′ = X/R`. Then `Y = Y′ ×_{X′} X`, and the
maps `Y ⟼ Y/R_Y` and `Y′ ⟼ Y′ ×_{X′} X` realize a bijective correspondence between the set of subsheaves `Y` of `X`
stable under `R` and the set of subsheaves `Y′` of `X′`.*

<!-- label: III.IV.4.4.11 -->

If `Y′` is a subsheaf of `X′`, then `Y′ ×_{X′} X` is a subsheaf of `X` stable

<!-- original page 212 -->

under `R`.[^N.D.E-IV-39] If `Y′` is obtained by passage to the quotient from a subsheaf `Y` of `X`, then `Y` is a
subobject of `Y′ ×_{X′} X`. It therefore suffices to show that if one has two subsheaves `Y` and `Y₁` of `X`, stable
under `R`, `Y₁` containing `Y`, and if the quotients `Y/R_Y` and `Y₁/R_{Y₁}` are identical, then `Y = Y₁`. One is
evidently reduced to proving the same assertion in the case where `Y₁ = X`. Denoting then by `P` (resp. `Q`) the
presheaf `i(X)/i(R)` (resp. `i(Y)/i(R_Y)`), the diagram

```text
X  →  P
↑       ↑
Y  →  Q
```

is cartesian. Since one has a commutative diagram

```text
P  →  a(P)
↑       ↑
Q  →  a(Q),
```

and since `Q ↪ a(Q)` is covering (4.3.11), the monomorphism `Q ↪ P` is covering, hence `Q` is a refinement of `P`. By
base change, `Y` is a refinement of `X`. Since `X` and `Y` are sheaves, this entails (4.3.12) `Y = X`.

**4.4.12.** In particular, if `Y` is a subsheaf of `X`, and if `Y′ = Y/R_Y`, then the preceding correspondence defines a
subsheaf `Ȳ` of `X`, stable under `R`, containing `Y` and minimum for these properties, which one calls the *saturation*
of `Y` for the equivalence relation `R`.

## Footnotes (chunk-A)

[^IV-0-1]: This text develops the substance of two oral expositions of A. Grothendieck, completing the latter on
several important points which had been passed over in silence or scarcely touched on.

[^N.D.E-IV-0]: N.D.E.: Version of 13/10/2024.

[^IV-1-1]: N.D.E.: that is, if `u` is right-cancellable.

[^N.D.E-IV-2]: N.D.E.: This implies, in particular, that `u` be an epimorphism.

[^N.D.E-IV-3]: N.D.E.: For example, if `C = (Sch)` is the category of schemes, one sees easily that every universal
epimorphism is surjective. Let `T = ∐_{p prime} Spec(F_p)` and `S = Spec(Z)`; then the morphism `u : T → S` is an
epimorphism that is not universal. On the other hand, one sees that `T ×_S T` is identified with `T`, so that the two
projections `T ×_S T ⇉ T` coincide; since `id_T` does not descend to a morphism `S → T`, this shows that `u` is not an
effective epimorphism.

[^N.D.E-IV-4]: N.D.E.: The numbering 1.4.0 has been added for later references.

[^N.D.E-IV-5]: N.D.E.: The numbering 1.6.0 has been added for later references.

[^N.D.E-IV-6]: N.D.E.: This is the following argument, communicated by M. Demazure. Let `f, g : T′ → T`, and let
`φ : T′ → T ×_S T` be the morphism with components `f` and `g`, whence `p₁ ∘ φ = f` and `p₂ ∘ φ = g`. Then
`F(φ) : F(T ×_S T) → F(T′)` satisfies `F(φ) ∘ F(p₁) = F(f)` and `F(φ) ∘ F(p₂) = F(g)`. Now, for every
`x ∈ Ȟ⁰(T/S, F)`, one has `F(p₁)(x) = F(p₂)(x)`. Hence, applying `F(φ)` to both sides, one obtains
`F(f)(x) = F(g)(x)`, which shows that `f` and `g` induce the same morphism.

[^N.D.E-IV-7]: N.D.E.: One will note that a monomorphism which is an epimorphism is not necessarily an isomorphism.
For example, in `C = (Sch)`, the morphism `Spec(F_p) ∐ Spec(Z[1/p]) → Spec(Z)` is a monomorphism and a surjective
epimorphism, but is not an isomorphism.

[^N.D.E-IV-8]: N.D.E.: for example, one has identified, on the one hand, `pr*₂,₁(X″₁) = pr*₃,₁(X″₁)` and, on the other
hand, `pr*₂,₁(X″₂) = pr*₃,₂(X″₂)`.

[^N.D.E-IV-9]: N.D.E.: applied to `f : S′ ×_T S′ → S ×_T S = Y`.

[^N.D.E-IV-10]: N.D.E.: The condition is evidently necessary. Conversely, if for every `S ∈ Ob C`, `R(S)` is the graph
of an equivalence relation, then this equivalence relation extends to `R(F)` for every `F ∈ Ob Ĉ`, by declaring that
two morphisms `φ, ψ : F → R` are equivalent if, for every `S ∈ Ob C` and `x ∈ F(S)`, `φ(x)` and `ψ(x)` are equivalent
in `X(S)`.

[^N.D.E-IV-11]: N.D.E.: Let us illustrate this by giving an outline of the sequel of this Exposé. Let `G` be a
`C`-group, `H` a sub-`C`-group, `R` the equivalence relation in `G` defined by `G × H → G × G`, `(g, h) ⟼ (g, gh)`
(cf. 3.2). The functor `Q` defined by `Q(S) = G(S)/H(S)` is a quotient in `Ĉ` (according to 4.4.9 applied to the least
fine topology, cf. 4.4.2), but it is not in general the quotient that one wishes. For example, for `C = (Sch)`, one
has an exact sequence of (affine) group schemes:

    ```text
    1 ⟶ μ₂ ⟶ G_m —p→ G_m ⟶ 1
    ```

    which identifies `G_m` with the quotient `G_m/μ₂`. Moreover, since `p` is a finite and locally free morphism, then
    `G_m` is the sheaf-quotient of `G_m` by `μ₂` in the larger category of sheaves for the (fppf) topology, cf. 4.6.6
    (ii) and 6.3.2. By contrast, the quotient `Q` in `Ĉ` is not isomorphic to `G_m` since, for example, `Q(Z) = {1}`
    while `G_m(Z) = {±1}`. Hence `Q` is not an (fppf) sheaf, and *a fortiori* `Q` is not representable.

[^N.D.E-IV-12]: N.D.E.: Note that, even for a `Ĉ`-equivalence relation in `X`, one is interested in the existence of a
quotient in `C`.

[^N.D.E-IV-13]: N.D.E.: "in `C`" has been added.

[^N.D.E-IV-14]: N.D.E.: The numbering 3.3.2.1 (resp. 3.3.3.1) has been added for later references. On the other hand,
Remark 3.3.3.2 has been added.

[^N.D.E-IV-15]: N.D.E.: The numbering 3.4.3.1 has been added for later references, and the proof of point (i) has been
detailed.

[^N.D.E-IV-16]: N.D.E.: This paragraph has been added.

[^N.D.E-IV-17]: N.D.E.: Here, "dominator" is taken in the sense of the preorder relation mentioned above, i.e., `Y`
dominates `X` if there exists an arrow `Y → X`. On the other hand, if `X, Y` are two subobjects of an object `Z`, one
says (cf. 2.4) that `Y` contains `X` if `X ⊂ Y`. To avoid any ambiguity between these two terminologies, "majorant"
has been replaced in the sequel by "dominating" in the first case, and by "containing", in the second.

[^N.D.E-IV-18]: N.D.E.: The sentence that follows has been detailed.

[^N.D.E-IV-19]: N.D.E.: The numbering 4.1.4.0 has been added in order to highlight this definition.

[^N.D.E-IV-20]: N.D.E.: that is: if `C` is covering "locally with respect to the covering sieve `R`", then `C` is
covering.

[^N.D.E-IV-21]: N.D.E.: (T′ 1) and (T′ 2) suffice: `G ∩ H = G ×_F H` belongs to `J(H)`, by (T′ 1), hence to `J(F)`, by
(T′ 2).

[^N.D.E-IV-22]: N.D.E.: This definition has been placed here (placed in the original after 4.2.5), since it will be
used in 6.2.1 in a slightly more general setting than that of 4.2.5.

[^N.D.E-IV-23]: N.D.E.: in what follows, typographical errors of the original have been corrected.

[^N.D.E-IV-24]: N.D.E.: One will note that if `Q` is a subpresheaf of a separated presheaf `P`, then `Q` is separated.
Indeed, for every sieve `R` of `S`, the composite map `Q(S) ↪ P(S) ↪ P(R)` is injective and factors through
`Q(S) → Q(R)`.

[^N.D.E-IV-25]: N.D.E.: This corollary has been added.

[^N.D.E-IV-26]: N.D.E.: The numbering 4.3.10.0 has been added for later references. On the other hand, it follows
from the definition that if `Q → P` is a monomorphism, the same holds for `LP → LQ`; hence `L` "preserves
monomorphisms" (see also 4.3.16 for a more general result: `L` "commutes with finite inverse limits").

[^N.D.E-IV-27]: N.D.E.: Denote by `p` the projection `R′ → R`. Since `i_R` is a monomorphism, one has `p = g i_{R′}`.
Let `g′` be the section of `i_{R′}` defined by `g`; then `p g′ = g` and therefore `p g′ i_{R′} = g i_{R′} = p`; this
entails `g′ i_{R′} = id_{R′}` and therefore `i_{R′} : R′ → T` is an isomorphism, with inverse `g′`.

[^N.D.E-IV-28]: N.D.E.: The statement of the corollary and its proof have been detailed.

[^N.D.E-IV-29]: N.D.E.: In particular, if `K` is the kernel of a pair of morphisms of presheaves `u, v : Q ⇉ P`, then
`LK` is the kernel of `Lu, Lv : LQ ⇉ LP` (this will be used in 4.4.5).

[^N.D.E-IV-30]: N.D.E.: The original has been modified here.

[^N.D.E-IV-31]: N.D.E.: The continuation of the proof has been slightly modified.

[^N.D.E-IV-32]: N.D.E.: Point (i) of Lemma 4.4.5 has been corrected, and the proof of the three points detailed.

[^N.D.E-IV-33]: N.D.E.: In general, the direct sum of two sheaves `F, G` is not a sheaf. Indeed, let
`S₁, S₂ ∈ Ob C`; suppose that the direct sum `S = S₁ ∐ S₂` exists in `C` and that the fiber product `S₁ ×_S S₂` is an
initial object `∅` of `C` (cf. I, 1.8). Let `R` be the sieve of `S` with base `{S₁, S₂}`; then `(F ∐ G)(R)` is the
disjoint union of `F(S) ∐ G(S)` and of `F(Sᵢ) × G(Sⱼ)` for `i ≠ j`, hence `F ∐ G` is not a sheaf in general. On the
other hand, if `C` is the category with a single object `S` and `id_S` as sole morphism, equipped with the topology
defined by `J(S) = {R_∅, S}`, then the only separated presheaves are `R_∅` and `X = h_S` (which is a sheaf), and
`X ∐ X` is not separated.

[^N.D.E-IV-34]: N.D.E.: The statement of the lemma and its proof have been detailed.

[^N.D.E-IV-35]: N.D.E.: Recall (cf. N.D.E. (17)) that one says that a morphism `g : G → H` is *dominated* by a family
of morphisms `Fᵢ → H` if this family factors through `g`.

[^N.D.E-IV-36]: N.D.E.: In order to be in accord with later references, the numbering of the original, which contained
two nos. 4.4.7, has been corrected.

[^N.D.E-IV-37]: N.D.E.: "contains" has been replaced by: "is dominated by", cf. N.D.E. (17).

[^N.D.E-IV-38]: N.D.E.: Lemmas 4.4.8.1 and 4.4.8.2 have been added.

[^N.D.E-IV-39]: N.D.E.: and one has `(Y′ ×_{X′} X)/R = Y′`.

### 4.5. The case of a topology coarser than the canonical topology

By 4.3.6 and 4.3.8, the following conditions are equivalent for a topology `T` on `C`:

(i) `T` is coarser than the canonical topology of `C`.

<!-- original page 219 -->

(ii) Every representable presheaf is a sheaf for `T`.

(iii) Every covering sieve for `T` is universal effective epimorphic.

If `T` is defined by a pretopology `S ↦ R(S)`, these conditions are further equivalent to

(iv) Every family belonging to `R(S)` is universal effective epimorphic.

In the case where these conditions are satisfied, the canonical functor `C → Ĉ` factors through a functor `j_C = j : C → C̃` (we shall also write `j(S) = S̃`[^N.D.E-IV-40]).

**Proposition 4.5.1.** *The functor `j : C → C̃` is fully faithful and commutes with arbitrary inverse limits. It is in particular left exact and therefore preserves the algebraic structures defined by finite inverse limits.*

<!-- label: III.IV.4.5.1 -->

This follows at once from consideration of the commutative diagram

```text
        C
       ╱ ╲
    j ╱   ╲ (canonical)
     ↙     ↘
    C̃  ─── i ───→  Ĉ
```

and from 4.4.1 (i).

Before exhibiting other properties of the functor `j`, we need to define the topology induced on a category `C/S`. No longer assuming the given topology necessarily coarser than the canonical one, this is done as follows: if `C` is a sieve of `T` in `C` and one has a morphism `T → S`, then `C` defines naturally a sieve of `T` in `C/S`, denoted `J(T)` (since the definition of a sieve of `T` depends only on the category `C/T = (C/S)/T`). If, for example, `C` is defined by the family `{T_i → T}`, then its image in `C/S` is defined by the same family considered as a family of morphisms of `C/S`. This being said, the map `T ↦ J(T)` defines a topology on `C/S` called the *topology induced* by the given topology. With the definitions of [AS], 2.3, it is the coarsest of the topologies on `C/S` for which the canonical functor

```text
i_S : C/S ⟶ C
```

<!-- original page 214 -->

is a comorphism[^N.D.E-IV-41]. One will note that the identifications

```text
(C/S)/T = C/T
```

respect the topologies by definition.

**Proposition 4.5.2.** *Let `S` be a representable sheaf on `C` and `F → S` a morphism of `Ĉ`. In order for `S′ ↦ Hom_S(S′, F)` to be a separated presheaf (resp. a sheaf) on `C/S`, it is necessary and sufficient that `F` be a separated presheaf (resp. a sheaf) on `C`.*

<!-- label: III.IV.4.5.2 -->

For every functor `P`, one has (I 1.4.1)

```text
Hom(P, F) = ⨆_{f ∈ Hom(P, S)} Hom_f(P, F).
```

[^N.D.E-IV-42]

<!-- original page 221 -->

Let `S′ ∈ Ob C` and `η : C′ → S′` a covering sieve. As `S` is a sheaf, the map `f ↦ f ∘ η` establishes a bijection `Hom(S′, S) ⥲ Hom(C′, S)`. Consequently, the map

```text
Hom_Ĉ(S′, F) ⟶ Hom_Ĉ(C′, F)
```

decomposes as a "disjoint union" of the maps

```text
Hom_f(S′, F) ⟶ Hom_{f ∘ η}(C′, F).
```

The proposition follows.

**Corollary 4.5.3.** *The topology induced on `C/S` by a topology on `C` coarser than the canonical topology of `C`, is coarser than the canonical topology of `C/S`.*

<!-- label: III.IV.4.5.3 -->

**Corollary 4.5.4.** *Suppose the given topology on `C` is coarser than the canonical topology. For every `S ∈ Ob C`, one has an equivalence of categories*

```text
C̃/S̃ ⥲ C̃/S.
```

*The following diagrams are commutative up to isomorphism (all unlabelled arrows being equivalences):*

```text
              (j_C)/S                (i_C)/S̃                (a_C)/Ŝ
    C/S ─────────────→  C̃/S̃ ───────────────→  Ĉ/Ŝ ────────────────→  C̃/S̃
      ║                  ≀                     ≀                       ≀
      ║       j_{C/S}            i_{C/S}                 a_{C/S}
    C/S ──────────────→  C̃/S ───────────────→  Ĉ/S ────────────────→  C̃/S
```

```text
        T̃
       ╱ ╲
      ╱   ╲
   ╱        ↘
  C̃/S̃     C̃/S / T̃
   ↘ ≃   ↗
      ╲ ╱
      C̃/T̃ ─→ C̃/T
```

<!-- original page 215 -->

The commutativity of the first two squares results from the definition of the equivalence `C̃/S̃ → C̃/S`. To prove the commutativity of the last, one must see that the following square is commutative:

```text
       L′
Ĉ/Ŝ ────→  Ĉ/Ŝ
  │           │
  │           │
  ↓    L″     ↓
Ĉ/S ────→  Ĉ/S ,
```

where `L′` is the restriction of the functor `L_C` to `Ĉ/Ŝ` and `L″` the functor `L_{C/S}`; this is easily seen by going back to the definition of the functors `L` (given after 4.3.9). As for the second diagram, this is none other than the restriction to the sheaf categories of the corresponding diagram on the categories of presheaves (Exposé I, n° 1), which is commutative.

**Scholie 4.5.5.** *The various assertions of this number show that, in the case where the given topology is coarser than the canonical topology, one may identify `C` with a full subcategory of `C̃`, itself a full subcategory of `Ĉ`, and that under this identification one may indulge in the usual abuses of language regarding `C → Ĉ`, justified by the commutativities above. Let us explicitly remark that the first diagram of 4.5.4 shows that one may use the functor `a` without special precaution.*

<!-- label: III.IV.4.5.5 -->

<!-- original page 216 -->

We shall see in the next number that the identification of `C` with a full subcategory of `C̃` (contrary to what was the case for `Ĉ`) commutes with the formation of certain direct limits, and we shall then say how to use this fact.

From now on, and unless explicitly stated otherwise, we shall assume the given topology coarser than the canonical topology and we shall systematically make the identifications described above.

**Proposition 4.5.6.** *Let `F` and `G` be two sheaves over `S` and `f : F → G` an `S`-morphism. The following conditions on `f` are equivalent:*

<!-- label: III.IV.4.5.6 -->

*(i) `f` is a monomorphism (resp. an epimorphism, resp. an isomorphism) in `C̃`.*

*(ii) `f` is a monomorphism (resp. an epimorphism, resp. an isomorphism) in `C̃/S = C̃/S`.*

For monomorphism and isomorphism, this is evident (it is a question of presheaves). For epimorphism, it follows from the description of epimorphisms as covering morphisms (4.4.3) and from the fact that, by definition of the induced topology, these are the same in `C̃` and `C̃/S`.

**Proposition 4.5.7.** *Let `f : F → G` be a morphism of sheaves. The following conditions are equivalent:*

<!-- label: III.IV.4.5.7 -->

*(i) `f` is a monomorphism (resp. an epimorphism, resp. an isomorphism).*

<!-- original page 217 -->

*(ii) For each `S ∈ Ob C`, `f_S : F_S → G_S` is locally a monomorphism (resp. an epimorphism, resp. an isomorphism), that is:*

*(iii) For each `S ∈ Ob C`, the set of `T → S` such that `F_T → G_T` is a monomorphism (resp. an epimorphism, resp. an isomorphism) is a refinement of `S`.*

*If the given topology is defined by a pretopology `R`, these conditions are further equivalent to the following:*

*(iv) For each `S ∈ Ob C`, there exists a covering family `{S_i → S} ∈ R(S)` such that for every `i`, `F_{S_i} → G_{S_i}` is a monomorphism (resp. an epimorphism, resp. an isomorphism).*

*If the category `C` has a final object `e`, one may content oneself with taking `S = e` in conditions (ii), (iii), and (iv).*

One obviously has (ii) ⇔ (iii) ⇔ (iv). To prove the equivalence of (i) and (ii) as well as the supplement concerning the final object, one must show that (ii) ⇒ (i) and that the notions in question are stable under base extension. Let us first prove this last point. For monomorphism and isomorphism, this is evident (it is a question of presheaves). For epimorphism, it follows from the fact that every epimorphism of sheaves is universal (4.4.3).

Let us finally show that (ii) entails (i). Suppose first that `f_S : F_S → G_S` is locally a monomorphism (resp. an isomorphism). There then exists a covering sieve `C` of `S` such that for every `T → C`, `f_T` is a monomorphism (resp. an isomorphism). As an inverse limit of monomorphisms (resp. isomorphisms) is one, `Hom(C, f)` will be a monomorphism (resp. an isomorphism) (cf. 4.1.4). The commutative diagram

```text
            Hom(C, f)
Hom(C, F) ────────────→ Hom(C, G)
   ↑                       ↑
   ≀                       ≀
            f(S)
   F(S) ─────────────→ G(S)
```

<!-- original page 218 -->

then shows that `f(S)` is injective (resp. bijective). Suppose finally that `f : F → G` is locally an epimorphism and let `H ⊂ G` be its image. For each `S → G`, `H ×_G S` is the image of `f ×_G S : F ×_G S → S`. To show that `f` is an epimorphism, one must show that `H` is a refinement of `G`, that is, that `H ×_G S` is a refinement of `S` for each `S`. But since this is so after every base change `T → S` of a refinement of `S` (since `f ×_G S` is locally covering), `H ×_G S` is indeed a refinement of `S` (Axiom (T 2)).

**Corollary 4.5.8.** *Let `F` and `G` be two sheaves over `S` and `f : F → G` an `S`-morphism. In order for `f` to be a monomorphism, resp. an epimorphism, resp. an isomorphism, it is necessary and sufficient that it be so locally on `S`.*

<!-- label: III.IV.4.5.8 -->

**Remark 4.5.9.** *The proof of the proposition shows that it remains valid, for the part concerning monomorphisms (resp. isomorphisms), when one only assumes that `F` is a separated presheaf (resp. a sheaf) and `G` an arbitrary presheaf (resp. a separated presheaf).*

<!-- label: III.IV.4.5.9 -->

Let us provisionally return to the case of an arbitrary topology and lay down a definition.

**Definition 4.5.10.** *Let `G → F` be a morphism of `Ĉ`. We say that `G` is a* relative sheaf above `F` *if for every `F`-functor `H` and every refinement `R` of `H`, the canonical map*

<!-- label: III.IV.4.5.10 -->

```text
(+)    Hom_F(H, G) ⥲ Hom_F(R, G)
```

*is bijective.*

<!-- original page 224 -->

Proposition 4.5.2 immediately generalizes:

**Proposition 4.5.11.** *If `F` is a sheaf, `G` is a relative sheaf above `F` if and only if it is a sheaf.*

<!-- label: III.IV.4.5.11 -->

**Lemma 4.5.12.** *In the situation `X → T → S` (where `X, T, S` are three objects of `Ĉ`), if `X` is a relative sheaf above `T`, then `U = ∏_{T/S} X` is a relative sheaf above `S`.*

<!-- label: III.IV.4.5.12 -->

<!-- original page 219 -->

Indeed, one has for every `S`-functor `Y`

```text
Hom_S(Y, U) = Hom_T(T ×_S Y, X).
```

If `C` is a sieve of `Y`, then `T ×_S C` is a sieve of `T ×_S Y`; one concludes at once.

**Corollary 4.5.13.** *The presheaves `Hom_{T/S}(X, Y)`, `Isom_S(X, Y)`, etc., are sheaves when the arguments appearing in them are also.*

<!-- label: III.IV.4.5.13 -->

Indeed, all these presheaves are constructed by means of fibered products and presheaves `∏_{T/S} X` (I 1.7 and II 1). It therefore suffices to verify the result for a presheaf `∏_{T/S} X`; in this case, the assertion follows from 4.5.11 and 4.5.12.

### 4.6. Description of the quotient of a sheaf by an equivalence relation

Recall that we are assuming the topology `T` given to be coarser than the canonical topology.

**Proposition 4.6.1.** *Let `R ⇒ X` (with morphisms `p_1, p_2`) be a `C̃`-equivalence relation in the sheaf `X`. Let `F ∈ Ob Ĉ` be defined as follows: for each `S` of `C`,*

<!-- label: III.IV.4.6.1 -->

```text
F(S) = { sub-S-sheaves Z of X_S stable under R × S[^N.D.E-IV-43], whose quotient by R_Z is S,
         i.e. such that the diagram R_Z ⇒ Z → S is exact }.
```

*Then for every sheaf `Y`, `Hom(Y, F)` is identified with the set:*

```text
{ sub-Y-sheaves of X × Y stable under R × Y and whose quotient is Y }.
```

*In particular the sub-sheaf `R` of `X × X` corresponds to an element `p` of `Hom(X, F)` and the diagram*

```text
R ⇒ X →^p F
```

*is exact, hence identifies `F` with the sheaf-quotient `X/R`.*

<!-- original page 220 -->

Indeed, set `Q = X/R`. For every sheaf `Y` and every morphism `f ∈ Hom(Y, Q)` corresponding to a section `s : Y ↪ Q × Y`, consider the diagram

```text
R × Y ⇒ X × Y ──→ Q × Y
                    ↑     ↑
(∗)                 │     │ s
                    │     │
                    Z ──→ Y
```

<!-- original page 225 -->

where the square is cartesian. It is immediate by 4.4.11 that `Z` is a sub-`Y`-sheaf of `X × Y`, stable under `R × Y`, whose quotient is `Y`, and that, conversely, every `Z` of this type comes from a unique section of `Q × Y` over `Y`. Taking first `Y` representable, one extracts an isomorphism `Q ≃ F`. Taking next `Y` arbitrary, one extracts the announced form of `Hom(Y, F)`. Considering finally the canonical morphism `X → Q`, one sees at once that it corresponds to the sub-`X`-sheaf `R` of `X × X`, which completes the proof.

**Corollary 4.6.2.** *Let `G` be an arbitrary subfunctor of `F` such that `Hom(X, G) ⊂ Hom(X, F)` contains `R`. Then the canonical morphism `p : X → F` factors through `G`.*

<!-- label: III.IV.4.6.2 -->

Since `p` is covering (4.4.9 and 4.4.3), it follows that `G` is a refinement of `F`. In particular, every sub-sheaf `G` of `F` satisfying the preceding condition is equal to `F` (4.3.12).

**4.6.3.** We are now going to interest ourselves in the case where `X` and `R` are representable. Let us first introduce some terminology. Besides the conditions (a) to (d) introduced in 3.4.1, we shall use other conditions on a family `(M)` of morphisms of `C`, which we state below, recalling the conditions (a) to (c) already given, for completeness.

<!-- label: III.IV.4.6.3 -->

(a) `(M)` is stable under base extension.

(b) The composite of two elements of `(M)` is in `(M)`.

(c) Every isomorphism is an element of `(M)`.

(d_T) Every element of `(M)` is covering.[^N.D.E-IV-44]

(e_T) Let `f : X → Y` be a morphism of `C`. If there exists a refinement `R` of `Y` such that for every `Y′ → R`, `X ×_Y Y′ → Y′` is an element of `(M)`, then `f` is an element of `(M)`.

<!-- original page 221 -->

Recall that (a) and (b) entail

(a′) The cartesian product of two elements of `(M)` is an element of `(M)`.

On the other hand, (a) and (d_T) entail by 4.3.9:

(d′) Every element of `(M)` is a universal effective epimorphism.

**4.6.4.** The preceding conditions are verified by the family of covering morphisms, denoted `(M_T)`, when `C` has fibered products. Indeed (cf. 4.2.3), (a) follows from (C 1), (b) from (C 2), (c) from (C 4), (d_T) from the definition, (e_T) from (C 5). The results we shall establish for a family satisfying these conditions will apply in particular to the family `(M_T)`. In particular, one may take for `T` the canonical topology and for `(M)` the family of universal effective epimorphisms.

**Lemma 4.6.5.** *Let `(M)` be a family of morphisms satisfying the properties (a) to (e_T) above. Let `R` be a `C`-equivalence relation in `X ∈ Ob C`, of type `(M)`. Let `X̃` be the sheaf defined by `X`, `R̃` the `C̃`-equivalence relation in `X̃` defined by `R` and `X̃/R̃` the sheaf-quotient. In order for `R` to be `(M)`-effective, it is necessary and sufficient that `X̃/R̃` be representable. If this is so, `X̃/R̃` is represented by the quotient `X/R`.*

<!-- label: III.IV.4.6.5 -->

Suppose first that `R` is `(M)`-effective and denote `Y = X/R`. The canonical morphism `p : X → Y` is an element of `(M)`, hence covering by (d_T). The corresponding morphism

```text
p̃ : X̃ ⟶ X̃/R̃
```

is therefore a universal effective epimorphism of `C̃` (4.4.3), hence identifies `X̃/R̃` with the quotient of `X̃` by the equivalence relation `R′` defined in `X̃` by `p̃`. As the canonical functor `C → C̃` commutes with fibered products, `R′` is none other than `R̃`, since `R` is the equivalence relation defined by `p`.

<!-- original page 222 -->

Conversely, suppose `X̃/R̃` representable by an object `Y` of `C`. Let `p : X → Y` be the morphism deduced from the canonical morphism `X̃ → X̃/R̃`; it is a covering morphism by 4.4.3. It is clear as before that `R` is the equivalence relation defined by `p`. It only remains to show that `p ∈ (M)`. Now the cartesian square

```text
R ⥲ X ×_Y X ──→ X
           │      │
        pr_2     p
           ↓      ↓
           X ───→ Y
```

shows that `p` becomes `p_2`, which is an element of `(M)`, after base change by the covering morphism `p`. One concludes by (e_T).

**Corollary 4.6.5.1.**[^N.D.E-IV-45] *Let `(M)` satisfy the properties (a) to (e_T) above and let `f : G → G′` be a morphism of `C`-groups, such that `f ∈ (M)`. Suppose `Ker(f)` representable (which is the case if `C` has a final object `e`). Then the equivalence relation in `G` defined by `H = Ker(f)` is `(M)`-effective and `G′` represents the sheaf-quotient `G̃/H̃` for the topology `T`.*

<!-- label: III.IV.4.6.5.1 -->

This follows from 4.6.5 and 3.4.7.1.

We are now in a position to state the main result of this number.

**Theorem 4.6.6.** *Let `(M)` be a family of morphisms verifying the axioms (a) to (e_T) of 4.6.3. Let `R` be a `C`-equivalence relation of type `(M)` (cf. 3.4.3) in the object `X` of `C`. Consider the functor `F ∈ Ob Ĉ` defined as follows:*

<!-- label: III.IV.4.6.6 -->

```text
F(S) = { sub-S-sheaves Z of X_S stable under R × S whose quotient by R_Z is S }.
```

*Let `F_0` be the subfunctor of `F` defined as follows: `F_0(S)` consists of the `Z ∈ F(S)` that are representable, that is:*

```text
F_0(S) = { sub-C/S-objects Z of X_S stable under R × S, such that
           R_Z is (M)-effective and has quotient S (i.e. such that
           Z → S belongs to (M) and R_Z ≃ Z ×_S Z) }.
```

*Then:*

<!-- original page 227 -->

*(i) The morphism `p ∈ Hom(X, F) = F(X)` defined by the sub-object `R` of `X × X` identifies `F` with the sheaf-quotient of `X` by `R`.*

*(ii) The following conditions are equivalent:*
- *a) `F` is representable.*
- *b) `F_0` is representable.*
- *c) `R` is `(M)`-effective.*

<!-- original page 223 -->

*Under these conditions, `F = F_0 = X/R`.*

*(iii) Let `(N)` be a family of morphisms stable under base change, such that for every covering family `{S_i → S}` and every family `{T_i → S_i}` of morphisms of `(N)`, every descent datum on the `T_i` relative to `{S_i → S}` is effective. Suppose `X` squarable (cf. 1.6.0) and the morphism `R → X × X` an element of `(N)`. Then `F_0 = F`.*

*Proof.* (i) has already been proved (4.6.1).

(ii) We have seen the equivalence of a) and c) as well as the equality `F = X/R`. It remains to prove that b) or c) implies `F_0 = F`. Let us first remark, as is moreover affirmed in the statement, that `F_0` is indeed a subfunctor of `F`; for every `S ∈ Ob C` and every `Z ∈ F_0(S)`, the morphism `Z → S` is squarable, hence `Z ×_S S′` is an element of `F_0(S′)` for every `S′ → S`. As `R ∈ F(X)` belongs to `F_0(X)`, 4.6.2 shows that b) implies `F_0 = F`.

Now suppose c) verified and let `Q` be an object of `C` representing `X/R`. Then the morphism `X → Q` is an element of `(M)` and, for every `S ∈ Ob C` and every `Z ∈ F(S)`, the diagram (∗) of 4.6.1 shows that `Z = S ×_{Q × S} X × S` is representable, and `Z → S` belongs to `(M)`, hence `Z ∈ F_0(S)`.

(iii) Let `f ∈ Hom(S, F)` correspond to `Z ∈ F(S)`. We must show that `f` factors through `F_0`, that is, that `Z` is representable. This is clear first if `f` factors through `X`, by virtue of:

**Lemma 4.6.7.** *Let `x_0 ∈ X(S)`. The image of `x_0` in `F(S)` corresponds to the sub-sheaf `Z` of `X_S` defined by the two cartesian squares*

<!-- label: III.IV.4.6.7 -->

```text
              id_{X_S} × x_0
   X_S ─────────────────→ X_S ×_S X_S ──→ X × X
    ↑                          ↑              ↑
    │                          │              │
    Z ──────────────────→     R_S ─────────→ R
```

<!-- original page 224 -->

This lemma follows at once from the description of the morphism `X → F`.

Let us return to the proof of the theorem. If `f` factors through `X`, then `Z` is representable and, as `R → X × X` is an element of `(N)`, the same holds for `Z → X_S`.

In general, `f` does not necessarily factor through `X`; but since `X → F` is covering (4.4.3), there exists by 4.4.8 (vii) a covering family `{S_i → S}` and for each `i` a morphism `S_i → X` making commutative the diagram

```text
X ────→ F
↑       ↑
│       │ f
S_i ──→ S .
```

<!-- original page 228 -->

By what precedes, the morphism `f_i : S_i → F` defined by the preceding diagram belongs to `Hom(S_i, F_0)` and corresponds to the sub-sheaf `Z ×_S S_i` of `X_{S_i}`. The morphism `Z ×_S S_i → X_{S_i}` is an element of `(N)` and the family `X_{S_i} → X_S` covering. It therefore only remains to establish:

**Proposition 4.6.8.** *Let `{S_i → S}` be a covering family and `Z` a sheaf above `S`. Suppose that for each `i`, the `S_i`-functor `Z ×_S S_i` is representable by an object `T_i`. Then the family of `T_i` is equipped with a canonical descent datum relative to `S_i → S`. In order for `Z` to be representable, it is necessary and sufficient that this datum be effective; if this is so, the "descended" object represents `Z`.*

<!-- label: III.IV.4.6.8 -->

Let us first remark that by 4.4.3, `{S_i → S}` is a universal effective epimorphic family in `C̃`, hence a descent family in `C̃` (2.3). If `Z` is representable by the object `T`, then `T ×_S S_i` (considered as a sheaf) is isomorphic to `Z ×_S S_i`, hence the descent datum on the `T_i` is effective and the (unique) descended object is isomorphic to `Z`. Conversely, suppose that the canonical descent datum on the `T_i` is effective and let `T` be the descended object. Since the family `{S_i → S}` is a descent family in `C̃`, there exists an `S`-morphism `T → Z` which by base extension to each `S_i` recovers the canonical morphism `T_i → Z ×_S S_i`. This morphism is locally an isomorphism; as `T` and `Z` are sheaves, it follows from 4.5.8 that it is an isomorphism.

<!-- original page 225 -->

**Corollary 4.6.9.** *Let `R` be an `(M)`-effective equivalence relation in `X`. For every sheaf `F`, the map*

<!-- label: III.IV.4.6.9 -->

```text
Hom(X/R, F) ⟶ Hom(X, F)
```

*identifies the first set with the part of the second consisting of the morphisms compatible with `R`.*

**Corollary 4.6.10.** *Let `T ′` be a topology coarser than `T`, for which the morphisms of `(M)` are covering. Under the conditions of 4.6.6 (iii), `X/R` is also the sheaf-quotient of `X` by `R` in every intermediate topology between `T ′` and the canonical topology.*

<!-- label: III.IV.4.6.10 -->

**Remark 4.6.11.** *If in the statement of 4.6.6 (iii), one furthermore assumes that, under the hypotheses of the text, if one denotes `T` the descended object, the morphism `T → S` is an element of `(N)`, then the inclusion morphisms `Z ↪ X_S` are also elements of `(N)`, as follows at once from the construction of `Z` by descent.*

<!-- label: III.IV.4.6.11 -->

**Remark 4.6.12.** *The implications c) ⇒ b) ⇒ a) and c) ⇒ [F_0 = F = X/R] have been established without recourse to the "if" part of Lemma 4.6.5, which is the only place where condition (e_T) is used. They therefore remain valid if `(M)` satisfies only conditions (a) to (d_T). An example of such a family `(M)` is that of squarable covering morphisms (compare with 4.6.4). In the case of the canonical topology, these are none other than the universal effective epimorphisms. One therefore has:*

<!-- label: III.IV.4.6.12 -->

<!-- original page 226 -->

<!-- original page 229 -->

**Corollary 4.6.13.** *Let `R` be a universal effective equivalence relation in `X`. Then the object `X/R` of `C` is the sheaf-quotient of `X` by `R` for the canonical topology. It represents the following functor: `(X/R)(S)` is the set of sub-`C/S`-objects `Z` of `X_S` stable under `R × S` and such that the induced equivalence relation is universal effective and has `S` as quotient.*

<!-- label: III.IV.4.6.13 -->

Similarly, for an arbitrary topology:

**Corollary 4.6.14.** *Let `(M)` be the family of squarable covering morphisms. If `R` is an `(M)`-effective equivalence relation in `X`, then the object `X/R` of `C` is the sheaf-quotient of `X` by `R` and represents the functor `F_0` of 4.6.6.*

<!-- label: III.IV.4.6.14 -->

**Scholie 4.6.15.** *We can now bring the following precisions to 4.5.5.* Whereas in questions involving exclusively inverse limits (fibered products, algebraic structures, etc.), one may, by the results of Exposé I and 4.5.5, identify `C` indifferently with a full subcategory of `C̃` or of `Ĉ`, it is not the same in those that mix inverse and direct limits. In all questions involving both inverse and direct limits, in particular passages to the quotient (example: group structure on the quotient of a group by an invariant subgroup), we shall consider the given category as embedded in the category of sheaves; thus if `R` is a `C`-equivalence relation in the object `X` of `C`, `X/R` will denote the sheaf-quotient of `X` by `R` (previously denoted `j(X)/j(R)`), hence in the case where this sheaf is representable, the object it represents. The preceding results show that in the most important cases, a quotient in `C` will also be a quotient in the category of sheaves; in any case, we forbid ourselves the use of the notation `X/R` for a quotient in `C` that does not coincide with the quotient in `C̃` (for example one that is not universal), thus modifying the definitions of n° 3.

<!-- label: III.IV.4.6.15 -->

<!-- original page 227 -->

To study a problem of the type above, one therefore places oneself first in the category of sheaves, where all the usual results are valid (cf. n° 4.4), then one specializes the results obtained to the original category, using the results of the present number and, when one has them, descent effectivity criteria. We shall see examples of this method in the following numbers.

### 4.7. Use of effectivity criteria: isomorphism theorem

In this number, we give an example of the use of effectivity criteria. The data of departure are a topology `T` on `C` (always coarser than the canonical topology), a family `(M)` of morphisms of `C` verifying the axioms (a) to (e_T) of 4.6.3, and a family `(N)` of morphisms of `C` liable to verify the following axioms:

(a) `(N)` is stable under base extension.

(f_T) "the morphisms of `(N)` descend by the given topology"; that is: for every `S ∈ Ob C`, every covering family `{S_i → S}` and every family `{T_i → S_i}` of morphisms of `(N)`, every descent datum on the `T_i` relative to `{S_i → S}` is effective, and if one denotes `T` the descended object, the morphism `T → S` is an element of `(N)`.

<!-- original page 230 -->

Since every element of `(M)` is covering (condition 4.6.3 (d_T)), (f_T) entails the following axiom:[^N.D.E-IV-46]

(f_M) If `Y → X` is an element of `(N)` and `X → X_1` an element of `(M)`, every descent datum on `Y` relative to `X → X_1` is effective; if one denotes `Y_1` the descended object, `Y_1 → X_1` is an element of `(N)`.

Let us at once signal an example of this situation, which will be treated later: `C` is the category of schemes, `T` the faithfully flat quasi-compact topology; `(M)` the family of faithfully flat quasi-compact morphisms, `(N)` the family of closed immersions, or that of quasi-compact immersions.[^N.D.E-IV-47]

Let us recall the principal result of 4.6.6 (taking into account 4.6.11):

**Proposition 4.7.1.** *If `X` is a squarable object of `C`, `R` an equivalence relation of type `(M)` in `X`, such that `R → X × X` is an element of `(N)`, with `(N)` verifying (a) and (f_T), then the sheaf-quotient `X/R` is defined by*

<!-- label: III.IV.4.7.1 -->

<!-- original page 228 -->

```text
(X/R)(S) = { sub-S-objects Z of X_S, stable under R × S, such that Z → X_S
             belongs to (N), Z → S is covering (or an element of (M)),
             and R_Z ≃ Z ×_S Z }.
```

Moreover, one has:

**Proposition 4.7.2.** *Let `X ∈ Ob C` and `R` an `(M)`-effective equivalence relation in `X`. Let `(N)` be a family of morphisms verifying (a) and (f_M).*

<!-- label: III.IV.4.7.2 -->

<!-- original page 229 -->

*For every sub-object `Y` of `X`, stable under `R` and such that `Y → X` belongs to `(N)`, the equivalence relation induced in `Y` by `R` is `(M)`-effective and the quotient `Y/R_Y = Y′` is a sub-object of `X′ = X/R` such that `Y′ → X′` belongs to `(N)`.*

*The map `Y ↦ Y′` is a bijection between the set of sub-objects `Y` of `X`, stable under `R`, such that `Y → X` belongs to `(N)`, and the set of sub-objects `Y′` of `X′` such that `Y′ → X′` belongs to `(N)`. The inverse map is `Y′ ↦ Y′ ×_{X′} X`.*

*Proof.* As `R` is `(M)`-effective, the morphism `X → X′` belongs to `(M)`. Let `Y′` be a sub-object of `X′` such that the canonical morphism `Y′ → X′` belongs to `(N)`. Then, the sub-object `Y = Y′ ×_{X′} X` of `X` is stable under `R`, and the morphism `Y → X` (resp. `Y → Y′`) belongs to `(N)` (resp. `(M)`) since `(N)` and `(M)` are stable under base change. Let `R_Y` denote the equivalence relation induced in `Y` by `R`. By 4.4.11, the sheaf quotient `Y/R_Y` is represented by `Y′` and therefore, by 4.6.5, `R_Y` is `(M)`-effective.

Conversely, let us show that every sub-object `Y` of `X`, stable under `R`, such that the structural morphism `Y → X` belongs to `(N)`, is obtained in this way. Indeed, if `Y` is stable under `R`, its two images in `R = X ×_{X′} X` are identical and `Y` is equipped with a descent datum relative to `X → X′`; the desired result follows, since the family `(N)` verifies the axiom (f_M).

<!-- original page 231 -->

**Corollary 4.7.3.** *Let `X ∈ Ob C` and `R` an `(M)`-effective equivalence relation in `X`; assume moreover that `R → X × X` belongs to `(N)`, where `(N)` verifies (a) and (f_T). Then, for every `Y` as in 4.7.2, `R_Y → Y × Y` also belongs to `(N)` and therefore, by 4.7.1, one has:*

<!-- label: III.IV.4.7.3 -->

```text
(Y/R_Y)(S) = { sub-S-objects Z of Y_S, stable under R_Y × S, such that Z → Y_S
               belongs to (N) (then Z → X_S also belongs to it), Z → S is covering,
               and R_Z ≃ Z ×_S Z }.
```

## 5. Passage to the quotient and algebraic structures

<!-- label: III.IV.5 -->

### 5.1. Principal homogeneous bundles

**Definition 5.1.0.**[^N.D.E-IV-48] *We recall (III 0.1) that an object `X` with (right) operator group `H` is said to be* formally principal homogeneous[^N.D.E-IV-49] *under `H` if the canonical morphism (of functors)*

<!-- label: III.IV.5.1.0 -->

```text
X × H ⟶ X × X
```

*defined by `(x, h) ↦ (x, xh)` is an isomorphism. It amounts to the same thing to say (cf. loc. cit.) that for every `S ∈ Ob C`, `X(S)` is formally principal homogeneous under `H(S)`, that is, empty or principal homogeneous under `H(S)`. In particular, if `H` is made to operate on itself by (right) translations, `H` becomes formally principal homogeneous under itself.*

<!-- original page 230 -->

**Definition 5.1.1.** *The object `X` with operator group `H` is said to be* trivial *if it is isomorphic (as object with operator group `H`) to `H` on which `H` operates by translations.*

<!-- label: III.IV.5.1.1 -->

**Proposition 5.1.2.** *Let `X` be formally principal homogeneous under `H`. One has an isomorphism*

<!-- label: III.IV.5.1.2 -->

```text
Γ(X) ⥲ Isom_{H-obj.}(H, X)
```

*of principal homogeneous sets under `Γ(H)`.*

To every section `x` of `X` one associates the morphism from `H` to `X` defined setwise by `h ↦ xh`. The stated assertion is immediate, by reduction to the set-theoretic case.

**Corollary 5.1.3.** *One has an isomorphism of objects with operators `H`*

<!-- label: III.IV.5.1.3 -->

```text
X ⥲ Isom_{H-obj.}(H, X).
```

**Corollary 5.1.4.** *In order for an object with operator group to be trivial, it is necessary and sufficient that it be formally principal homogeneous and possess a section.*

<!-- label: III.IV.5.1.4 -->

<!-- original page 232 -->

**Definition 5.1.5.** *Let `C` be a category equipped with a topology. We say that the `S`-object `X` with `S`-operator group `H` is a* principal homogeneous bundle under `H` *if it is locally trivial, that is, if the following equivalent conditions are satisfied:[^N.D.E-IV-50]*

<!-- label: III.IV.5.1.5 -->

*(i) The set of `T → S` such that (the functor) `X ×_S T` is trivial under `H ×_S T` is a refinement of `S`.*

<!-- original page 231 -->

*(ii) There exists a covering family (for a pretopology defining the given topology) `{S_i → S}` such that for each `i`, the `S_i`-functor `X ×_S S_i` with `S_i`-functor-group of operators `H ×_S S_i` is trivial (= has a section over `S_i`).*

**Proposition 5.1.6.** *Let `C` be a category equipped with a topology `T`. Let `(M)` be a family of morphisms of `C` verifying the axioms (a) to (e_T) of 4.6.3. Let `H` be an `S`-group such that the structural morphism `H → S` is an element of `(M)` and `P` an `S`-object with `S`-operator group `H`. The following conditions are equivalent:*

<!-- label: III.IV.5.1.6 -->

*(i) `P` is a principal homogeneous bundle under `H` (Definition 5.1.5).*

*(ii) `P` is formally principal homogeneous under `H` and the structural morphism `P → S` is an element of `(M)`.*

*(iii) There exists a morphism `S′ → S` element of `(M)` such that by base extension from `S` to `S′`, `P` becomes trivial, that is, `P ×_S S′` is trivial under `H ×_S S′`.*

*(iv) `H` operates freely on `P`, in an `(M)`-effective manner, and the quotient `P/H` is isomorphic to `S`.*

Let us first remark that (ii) and (iv) are equivalent, taking into account that, in either case, `P → S` is an element of `(M)`, hence squarable, which ensures the representability of the fibered products `H ×_S P` and `P ×_S P`. It is clear that (ii) entails (iii), as one can take `P` itself as `S′`, the hypothesis that `P` is formally principal homogeneous entailing that `P ×_S P` is trivial under `H ×_S P` (5.1.4), since it has a section (the diagonal section). It is clear that (iii) entails (i), since `{S′ → S}` is a covering family, by axiom (d_T). It therefore remains to show that (i) entails (ii). The morphism of sheaves `P ×_S H → P ×_S P` is locally an isomorphism, hence an isomorphism (4.5.8); `P` is therefore formally principal homogeneous. The structural morphism `P → S` is locally isomorphic to the structural morphism `H → S` which is an element of `(M)`. It is therefore itself an element of `(M)` by (e_T).

<!-- original page 232 -->

The equivalence between (i) and (iv) generalizes:

**Proposition 5.1.7.** *Under the same hypotheses on `C` and `(M)`, let `H` be an `S`-group and `X` an `S`-object on which `H` operates (on the right). Suppose the structural morphism `H → S` is an element of `(M)`. The following conditions are equivalent:*

<!-- label: III.IV.5.1.7 -->

*(i) `H` operates freely on `X` and in an `(M)`-effective manner.*

*(ii) There exists an `S`-morphism `p : X → Y` compatible with the equivalence relation defined in `X` by the action of `H` and such that the operation of `H ×_S Y` on `X` above `Y` thus deduced makes `X` a principal homogeneous bundle under `H_Y` above `Y`.*

*Under these conditions `p` identifies `Y` with the quotient `X/H`.*

<!-- original page 233 -->

If `p : X → Y` is a morphism compatible with the action of `H`, then the operation of `H ×_S Y` on `X` above `Y` thus deduced defines in `X` the same equivalence relation as the action of `H`, by virtue of the formula

```text
H_Y ×_Y X ⥲ H ×_S X.
```

The proposition follows from this remark and from the equivalence (iv) ⇔ (i) above.

**Corollary 5.1.7.1.**[^N.D.E-IV-51] *Let `C` be a category having a final object, stable under fibered products, and equipped with a topology `T` coarser than the canonical topology. Let `f : G → H` be a morphism of `C`-groups, and `K = Ker(f)`. Assume `f` covering for the topology `T`.*

<!-- label: III.IV.5.1.7.1 -->

*Then `H` represents the sheaf quotient `G/K`, and `f` is a `K_H`-torsor. (N.B. One will also say that: "`G` is a `K`-torsor above `H`".)*

Indeed, as `f` is covering, it is a universal effective epimorphism (4.4.3), hence by 3.3.3.1, `H` is the quotient of `G` by the equivalence relation `R(f) = G ×_H G`. On the other hand, the morphism `G × K → G ×_H G`, `(g, k) ↦ (g, gk)` is an isomorphism of objects with operator group `K_G = G ×_H K_H` (its inverse being given by `(g, g′) ↦ (g, g⁻¹ g′)`). Hence, on the one hand, `R(f)` is the equivalence relation defined by `K`; on the other hand, since the morphism `f : G → H` is covering, `f` is a `K_H`-torsor, by 5.1.6 (ii) (or directly by definition 5.1.5 (ii)).

We can now make Theorem 4.6.6 more precise in the case of passage to the quotient by an operator group:

**Proposition 5.1.8.** *Under the hypotheses of 5.1.7, let `F_0` denote the functor over `S` defined as follows: for each `S′ → S`, `F_0(S′)` is the set of representable sub-`S′`-functors `Z` of `X ×_S S′`, stable under `H ×_S S′` and being principal homogeneous bundles under this `S′`-group for the induced action (3.2.2).*

<!-- label: III.IV.5.1.8 -->

*(i) The following conditions are equivalent:*

<!-- original page 233 -->

- *a) The operation of `H` on `X` is `(M)`-effective and free.[^N.D.E-IV-52]*
- *b) `F_0` is representable.*

*Under these conditions, one has `F_0 = X/H`.*

*(ii) Let `(N)` be a family of morphisms, stable under base change, such that for every covering family `{S′_i → S′}` and every family `{T_i → S′_i}` of morphisms of `(N)`, every descent datum on the `T_i` relative to `{S′_i → S′}` is effective. Assume the morphism `X ×_S H → X ×_S X` is an element of `(N)` and `X` squarable. Then the element `p` of `Hom(X, F_0)` corresponding to the sub-object `X ×_S H` of `X ×_S X` identifies `F_0` with the sheaf-quotient `X/H`.*

<!-- original page 234 -->

### 5.2. Group structures and passage to the quotient

In this number we interest ourselves in the algebraic structures one can place on the quotient `G/H` of a group by a subgroup. We shall first place ourselves in the category of sheaves on `C` for an arbitrary topology. By taking the canonical topology and using 4.5.12, we shall obtain results for the universal effective passage to the quotient in `C`.

**Proposition 5.2.1.** *Let `u : H → G` be a monomorphism of sheaves of groups. There exists on the sheaf-quotient `G/H` a unique structure of object with operator group `G` such that the canonical morphism*

<!-- label: III.IV.5.2.1 -->

```text
p : G ⟶ G/H
```

*is a morphism of objects with operator group `G`. This structure is functorial with respect to the pair `(G, H)`: if one has a commutative diagram*

```text
H ──→ G
│      │
│      │ f
↓      ↓
H′ ──→ G′ ,
```

*the morphism `f : G/H → G′/H′` (3.2.3) is compatible with the morphism `f` on the operator groups.*

Indeed, the sheaf `G/H` is the sheaf associated with the presheaf

```text
i(G)/i(H) : S ↦ G(S)/H(S);
```

as the functor `a` is left exact, it transforms objects with operator groups into objects with operator group. As the presheaf `i(G)/i(H)` is equipped with a structure of object with operator groups `i(G)`, then `G/H = a(i(G)/i(H))` is equipped with a structure of object with operators `a(i(G)) = G`. This structure obviously enjoys all the stated properties.

**Corollary 5.2.2.** *Let `u : H → G` be a monomorphism of `C`-groups. Suppose that the operation of `H` on `G` is universal effective. There exists on the object-quotient `G/H ∈ Ob C` a unique structure of object with operator group `G` such that `p : G → G/H` is a morphism of objects with operators. This structure is functorial in the pair `(H, G)` (with `H` operating in a universal effective manner in `G`), in the preceding sense.*

<!-- label: III.IV.5.2.2 -->

**Proposition 5.2.3.** *Let `u : H → G` be a monomorphism of sheaves of groups identifying `H` with an invariant sub-sheaf of groups of `G`. There exists on the sheaf-quotient `G/H` a unique structure of sheaf of groups such that the canonical morphism `p : G → G/H` is a morphism of groups. This structure is functorial in the pair `(H, G)` (with `H` invariant).*

<!-- label: III.IV.5.2.3 -->

The proof is similar to that of 5.2.1.

**Corollary 5.2.4.** *Let `u : H → G` be a monomorphism of `C`-groups identifying `H` with an invariant subgroup of `G`. Suppose that the action of `H` on `G` is universal effective. There exists on the object-quotient `G/H ∈ Ob C` a unique group structure*

<!-- label: III.IV.5.2.4 -->

<!-- original page 235 -->

*such that the canonical morphism `G → G/H` is a morphism of groups. This structure is functorial with respect to the pair `(H, G)` (`H` invariant, `H` operating in a universal effective manner).*

One can characterize the group structure of `G/H` in a more telling manner:

**Proposition 5.2.5.** *Under the conditions of 5.2.4, let `K` be a `C`-group and `f : G → K` a morphism. The following conditions are equivalent:*

<!-- label: III.IV.5.2.5 -->

*(i) `f` is a morphism of groups compatible with the equivalence relation defined by `H`.*

*(ii) `f` is a morphism of groups inducing the trivial morphism `H → K`.*

*(iii) `f` factors as a morphism of groups `G/H → K`.*

*In particular, one has an isomorphism, functorial in the group `K`*

```text
Hom_{C-gr.}(G/H, K) ⥲ {f ∈ Hom_{C-gr.}(G, K) | f ∘ u = e}.
```

The equivalence of (i) and (ii) is proved set-theoretically. One obviously has (iii) ⇒ (ii). The equivalence of (iii) and (ii) follows from the formula

```text
Hom(G/H, K) ≃ Hom(i(G)/i(H), K)
```

and from the definition of the group structure of `G/H`.

**Remark 5.2.6.** *In the preceding situation, if the kernel of `f` is exactly `H`, the morphism `G/H → K` that factors `f` is a monomorphism. This follows at once from 3.3.4.*

<!-- label: III.IV.5.2.6 -->

In the case of sheaves of groups, one can make 4.4.11 more precise by means of the

**Proposition 5.2.7.** *Let `G` be a sheaf of groups, `H` an invariant sub-sheaf of groups. For every sub-sheaf of groups `K` of `G` containing `H`, let `K′` be the quotient group `K/H` considered as a subgroup of `G′ = G/H`.*

<!-- label: III.IV.5.2.7 -->

<!-- original page 236 -->

*One has `K = K′ ×_{G′} G`, and the maps `K ↦ K/H` and `K′ ↦ K′ ×_{G′} G` realize a bijection between the set of sub-sheaves of groups of `G` containing `H` and the set of sub-sheaves of groups of `G′`. In this correspondence, the invariant sub-sheaves of groups of `G` and of `G′` correspond.*

The first part follows easily from 4.4.11 and 3.2.4. It remains to see that `K` is invariant in `G` if and only if `K′` is invariant in `G′`. If `K` is invariant in `G`, then the presheaf `i(K)/i(H)` is invariant in `i(G)/i(H)`. The same holds for the associated sheaves, by virtue of the usual argument. If conversely `K′` is invariant in `G′`, then the fibered product `K ×_{G′} G` is invariant in `G`, as one sees immediately.

If now `L` is an arbitrary sub-sheaf of groups of `G`, let `L̄` be the saturation of `L` for the equivalence relation defined by `H`; we shall also write `L̄ = L · H`.

**Proposition 5.2.8.** *Under the preceding conditions, `L · H` is a sub-sheaf of groups of `G` containing `H` and the image of `L` in `G/H` is identified with*

<!-- label: III.IV.5.2.8 -->

```text
(L · H)/H ≃ L/(H ∩ L).
```

Indeed, let `L′` denote the sheaf image of `L` in `G/H`. It is a sub-sheaf of groups of `G/H` corresponding to `L · H` in the correspondence of the preceding proposition. As the morphism `L → L′` is covering, hence a universal effective epimorphism of sheaves, it follows from 4.4.9 that `L′` is identified with the quotient of `L` by the kernel of `L → L′` which is obviously none other than `H ∩ L`.

Let us finally consider the following situation: we have a sheaf of groups `G`, a sub-sheaf of groups `K` and a sub-sheaf of groups `H` of `K`, invariant in `K`. Let us first define a (right) operation of the sheaf of groups `H\K` (= `K/H`) on `G/H`. The group `K` operates by right translations on `G`. As `H` is invariant in `K`, this operation is compatible with the equivalence relation defined by the action of `H` and therefore defines an operation of `K` on `G/H`, that is, a morphism from the opposite group `K°` to `K` into `Aut(G/H)`. As the latter is a sheaf (4.5.13) and this morphism is trivial on `H`, it factors through `K/H` and defines the sought operation. As the right and left operations of `G` on itself commute, the operations of `G` and `K/H` on `G/H` commute.

<!-- original page 237 -->

**Proposition 5.2.9.** *Under the preceding conditions, `K/H` operates freely (on the right) on `G/H` and one has a canonical isomorphism of sheaves with operator group `G`*

<!-- label: III.IV.5.2.9 -->

```text
(G/H)/(K/H) ≃ G/K.
```

*When `K` is invariant in `G`, in which case `K/H` is invariant in `G/H` (5.2.7), this isomorphism respects the group structures of the two sides.*

One has an isomorphism of presheaves

```text
(i(G)/i(H)) / (i(K)/i(H)) ⥲ i(G)/i(K),
```

which respects the structures of objects with operator group `i(G)`. The announced result is obtained by applying the functor `a` to this relation.

**Corollary 5.2.10.** *Let `G` be a `C`-group, `K` a sub-`C`-group of `G`, `H` an invariant sub-`C`-group of `K`. Let `(M)` be a family of morphisms of `C` verifying the axioms (a) to (e_T). Suppose the operation of `H` on `G` (resp. `K`) on the right is `(M)`-effective. Then `K/H` operates in a natural manner freely on the right on `G/H`; this operation commutes with that of `G`. The following conditions are equivalent:*

<!-- label: III.IV.5.2.10 -->

<!-- original page 238 -->

*(i) The operation of `K` on `G` is `(M)`-effective.*

*(ii) The operation of `K/H` on `G/H` is `(M)`-effective.*

*Under these conditions, one has an isomorphism of objects[^N.D.E-IV-53] with operator group `G`:*

```text
(G/H)/(K/H) ≃ G/K.
```

### 5.3. Use of effectivity criteria: Noether's theorem[^N.D.E-IV-54]

Let `C`, `T` and `(M)` be as usual. Let `(N)` be a family of morphisms verifying the axioms (a) and (f_M) of 4.7. Putting together 5.2.7 and 4.7.2, one obtains:

**Proposition 5.3.1.** *Let `G` be a `C`-group. Let `H` be a sub-`C`-group of `G`, invariant and operating in an `(M)`-effective manner in `G`.*

<!-- label: III.IV.5.3.1 -->

*For every sub-`C`-group `K` of `G` containing `H` and such that the morphism `K → G` belongs to `(N)`, `H` operates in `K` in an `(M)`-effective manner and the quotient `K/H = K′` is a sub-`C`-group of `G/H = G′` such that the morphism `K′ → G′` belongs to `(N)`.*

*The map `K ↦ K′` is a bijection between the set of sub-`C`-groups `K` of `G`, containing `H` and such that `K → G` belongs to `(N)`, and the set of sub-`C`-groups `K′` of `G′` such that `K′ → G′` belongs to `(N)`. The inverse map is `K′ ↦ K ×_{G′} G`. In this correspondence, the invariant subgroups of `G` and `G′` correspond.*

**Corollary 5.3.2.** *If `H → G` is an element of `(N)`, then `C` has a final object `e` and the unit section `e → G/H` is an element of `(N)`.[^N.D.E-IV-55]*

<!-- label: III.IV.5.3.2 -->

## 6. Topologies in the category of schemes

<!-- label: III.IV.6 -->

<!-- original page 239 -->

### 6.1. The Zariski topology

This is the topology generated by the following pretopology: a family of morphisms `{S_i → S}` is covering if each morphism is an open immersion and the union of the images of the `S_i` is all of `S`. It is denoted (Zar).

**Definition 6.1.1.** *A sheaf for the Zariski topology is also called* a functor of local nature*: it is a contravariant functor from `(Sch)` to `(Ens)` such that for every scheme `S` and every covering of `S` by opens `S_i`, one has an exact diagram:*

<!-- label: III.IV.6.1.1 -->

```text
F(S) → ∏_i F(S_i) ⇒ ∏_{i,j} F(S_i ∩ S_j).
```

In particular, a functor of local nature transforms direct sums into products. As every representable functor is a sheaf, this topology is coarser than the canonical topology.

From the terminological point of view, whenever we say "local", "locally", without precision, it will be with reference to the Zariski topology, hence in the usual sense.

### 6.2. A procedure for constructing topologies

**Proposition 6.2.1.** *Let `C` be a category, `C ′` a full subcategory, `P` a set of families of morphisms of `C` with the same target, stable under base change and under composition (i.e. verifying the axioms (P 1) and (P 2) of 4.2.5), `P′` a set of families of morphisms of `C ′` containing the families reduced to an identity isomorphism. Equip `C` with the topology generated by `P` and `P′` (cf. 4.2.5.0) and suppose the three conditions below are verified:*

<!-- label: III.IV.6.2.1 -->

*(a) If `{S_i → S} ∈ P′` (hence `S_i, S ∈ Ob C ′`) and if `T → S` is a morphism of `C ′`, then the fibered products `S_i ×_S T` (in `C`) exist and the family `{S_i ×_S T → T}` belongs to `P′` (hence `S_i ×_S T ∈ Ob C ′`). (Remark: this condition entails that `P′` is stable under base change in `C ′`, but is not equivalent to it, since it further supposes that the inclusion functor from `C ′` to `C` commutes with certain fibered products).*

<!-- original page 240 -->

*(b) For every `S ∈ Ob C`, there exists `{S_i → S} ∈ P` with `S_i ∈ Ob C ′` for each `i`.*

*(c) In the following situation:*

```text
              S_{ijk}
                │ (P′)
                ↓
        (P)  S_{ij}
   S_i ←──── │
        (P′) │
             ↓
             S ,
```

*where `S, S_i, S_{ij}, S_{ijk} ∈ Ob C ′`; `{S_i → S} ∈ P′`; `{S_{ij} → S_i} ∈ P` for each `i`; `{S_{ijk} → S_{ij}} ∈ P′` for each `ij`, there exists a family `{T_n → S} ∈ P′` and for each `n` a multi-index `(ijk)` and a commutative diagram*

```text
S_{ijk} ←──── T_n
       ╲     ╱
        ╲   ╱
         ╲ ╱
          S .
```

*Then, in order for a sieve `R` of `S ∈ Ob C` to be covering, it is necessary and sufficient that there exist a composite family*

```text
R ←┄┄┄ S_{ij}
        │ (P′)
        ↓
   S ←─ S_i
        (P)
```

*where `S_i, S_{ij} ∈ Ob C ′`, `{S_i → S} ∈ P`, `{S_{ij} → S_i} ∈ P′` for each `i`, and the morphisms `S_{ij} → S` so obtained factor through `R` (in other words, the sieve generated by this composite family is contained in `R`).*

<!-- original page 239 -->

*Proof.* As the families elements of `P` and of `P′` are covering, a family composed of such families will be also (C 2), hence a sieve of the indicated form will be covering, since it contains a covering sieve.

<!-- original page 241 -->

Conversely, it suffices to see that the sieves of this form do indeed form a topology, i.e. it suffices to verify the axioms (T 1) to (T 4) of 4.2.1.

*Axiom (T 4).* Let `S ∈ Ob C`. There exists by (b) a family `{S_i → S} ∈ P` with `S_i ∈ Ob C ′`. The families `{S_i →^{id_{S_i}} S_i}` are elements of `P′` by hypothesis. The sieve `S` of `S` is therefore of the desired form:

```text
S_i ───→ S
 │  (P′) id    id_S
 ↓  (P)    
S_i ───→ S .
```

*Axiom (T 3).* Evident.

*Axiom (T 2).* Let `R` be a sieve of `S` of the desired form and let `C` be a sieve[^N.D.E-IV-56] of `S` such that, for every `T ∈ Ob C` and every morphism `T → S` factoring through `R`, the sieve `C ×_S T` of `T` is of the desired form. Then, as `S_{ij} → S` factors through `R`, the sieve `C_{ij} = C ×_S S_{ij}` of `S_{ij}`:

```text
        S_{ij} ←─── C_{ij}
       ╱  (P′)
      ╱
    S_i
     │ (P)
     ↓
     S ←──── C
     ↑
     R
```

is of the desired form; hence, for each `ij`, one has a diagram of the form:

```text
S_{ijkl}
   │ (P′)
   ↓
S_{ijk}
   │
   │ (P)
   ↓
S_{ij} ←──── C_{ij} .
```

One has therefore proved that there exists a composite family

```text
S_{ijkl} ──(P′)─→ S_{ijk} ──(P)─→ S_{ij} ──(P′)─→ S_i ──(P)─→ S
```

<!-- original page 240 -->

belonging to `P ∘ P′ ∘ P ∘ P′`, factoring through `C`, and where all objects other than `S` are in `C ′`. Applying condition (c) to each family `{S_{ijkl} → S_i}`, one deduces that for each `i` there exists a family `{T_{in} → S_i} ∈ P′`, such that `T_{in} → S` factors through one of the `S_{ijkl}`, hence through `C`:

<!-- original page 242 -->

```text
T_{in} ──→ S_{ijkl}
   │ (P′)
   ↓
   S_i
   │ (P)
   ↓
   S ←──── C .
```

The sieve `C` of `S` is therefore of the desired form, which completes the verification.

*Axiom (T 1).* Let `R` be a sieve of `S` of the given form and let `T → S` be a morphism of `C`. Let us show that the sieve `R ×_S T` of `T` is of the desired form.

```text
       S_{ij} ←──────── U_{ikj}
          │ (P′)              (P′)
          ↓                   ↓
   S_i ←─────────── T_i ←─(P)── U_{ik}
          │                       ╱
          │ (P)            (P)   ╱ (P)
          ↓                     ╱
   R ──→ S ←──────── T ←───────
```

Let `T_i = S_i ×_S T`. The family `{T_i → T}` belongs to `P` (by (P 1)). Applying (b), one constructs `{U_{ik} → T_i} ∈ P`, with the `U_{ik} ∈ Ob C ′`. By hypothesis (condition (P 2) on `P`), one has `{U_{ik} → T} ∈ P`. By (a), `U_{ik} ×_{S_i} S_{ij} = U_{ikj}` is an object of `C ′` and for each `ik`, `{U_{ikj} → U_{ik}} ∈ P′`. Then, the commutative diagram below

```text
R ←──────── U_{ikj}
              │ (P′)
              ↓
              U_{ik}
              │ (P)
              ↓
S ←──── T ←── 
```

shows that the morphisms `U_{ijk} → T` factor through the sieve `T ×_S R` of `T`, which is therefore of the desired form, which completes the proof.

**Corollary 6.2.2.** *If `S ∈ Ob C ′` and if `R` is a sieve of `S`, `R` is covering if and only if there exists a family `{T_i → S} ∈ P′`, factoring through `R`.*

<!-- label: III.IV.6.2.2 -->

<!-- original page 243 -->

Indeed, such a sieve is covering. On the other hand, it suffices to apply (c) by taking the family `{S_i → S}` reduced to the identity isomorphism of `S` to deduce from the proposition that a covering sieve is of the indicated form.

**Corollary 6.2.3.** *In order for a presheaf `F` on `C` to be separated (resp. a sheaf), it is necessary and sufficient that the morphism*

<!-- label: III.IV.6.2.3 -->

```text
F(S) ⟶ ∏_i F(S_i)
```

*be injective (resp. that the diagram*

```text
F(S) ⟶ ∏_i F(S_i) ⇒ ∏_{i,j} F(S_i ×_S S_j)
```

*be exact) in the two following cases:*

*(i) `{S_i → S} ∈ P`,*

*(ii) `S, S_i ∈ Ob C ′`;  `{S_i → S} ∈ P′`.*

Indeed, the conditions are necessary, since the families in question are covering. If `C` is the sieve of `S` image of a family of morphisms `{S_{ij} →^{(P′)} S_i →^{(P)} S}`, a straightforward diagram chase shows that the conditions of the corollary entail that `Hom(S, F) →^g Hom(C, F)` is injective (resp. bijective). But every refinement `R` of `S` contains a sieve `C` of the above type and one has a commutative diagram

```text
                f
Hom(S, F) ───────────→ Hom(R, F)
       ╲                  ╱
        ╲ g           h ╱
         ╲             ╱
          ↘           ↙
           Hom(C, F) .
```

One knows that `g` is injective, hence so is `f`. Therefore `F` is separated. But `R` is a refinement of `C`, hence `h` is also injective. If `g` is bijective, then `f` is also, hence `F` is a sheaf.

<!-- original page 244 -->

**Remark 6.2.4.** *The preceding corollary does not follow from 4.3.5, because `P′` is not stable under base extension.*

<!-- label: III.IV.6.2.4 -->

**Remark 6.2.5.** *Condition (c) is verified in particular in the case where*

<!-- label: III.IV.6.2.5 -->

*(i) `P′` is stable under composition.*

*(ii) If `{S_j → S}` is a family of morphisms of `C ′`, element of `P`, there exists a subfamily element of `P′`.*

### 6.3. Application to the category of schemes

One takes for `C` the category of schemes, for `C ′` the full subcategory formed by affine schemes, for `P` the set of surjective families of open immersions. One will consider several sets `P′`:

`P′_1` : finite surjective families, composed of flat morphisms.

<!-- original page 242 -->

`P′_2` : finite surjective families, composed of flat morphisms of finite presentation and quasi-finite.[^N.D.E-IV-57]

`P′_3` : finite surjective families, composed of étale morphisms.

`P′_4` : finite surjective families, composed of étale and finite morphisms.

For each of these sets `P′_i`, except `P′_4`, the conditions of Proposition 6.2.1 are verified ((c) thanks to 6.2.5, since an affine scheme being quasi-compact, every family of morphisms of `C ′`, element of `P`, contains a finite subfamily that is also in `P`, hence in `P′_i` for `i = 1, 2, 3`). The topology `T_i` generated by `P` and `P′_i` is denoted and called in the following way:

<!-- original page 245 -->

```text
T_1 = (fpqc) = faithfully flat quasi-compact topology.
T_2 = (fppf) = faithfully flat (locally) of finite presentation topology.
T_3 = (ét)  = étale topology.
T_4 = (étf) = étale finite topology.
```

As `P′_1 ⊃ P′_2 ⊃ P′_3 ⊃ P′_4`, one has

```text
(fpqc) ≥ (fppf) ≥ (ét) ≥ (étf) ≥ (Zar).
```

**Proposition 6.3.1.** *(i) In order for the sieve `R` of `S` to be covering for `T_i`, `1 ≤ i ≤ 3`, it is necessary and sufficient that there exist a covering `(S_p)` of `S` by affine opens and for each `p` a family `{S_{pq} → S_p}` element of `P′_i`, the `S_{pq}` being affine, such that each morphism `{S_{pq} → S}` factors through `R`.[^N.D.E-IV-58]*

<!-- label: III.IV.6.3.1 -->

*(ii) In order for a presheaf `F` on `(Sch)` to be a sheaf for (fpqc) (resp. (fppf), (ét), (étf)), it is necessary and sufficient that*

- *a) `F` be a sheaf for (Zar), i.e. a functor of local nature.*
- *b) For every faithfully flat (resp. faithfully flat of finite presentation and quasi-finite, resp. surjective étale, resp. surjective étale finite) morphism `T → S`, where `T` and `S` are affine, one has an exact diagram:*

```text
F(S) ⟶ F(T) ⇒ F(T ×_S T).
```

*(iii) The topologies `T_i`, `i = 1, 2, 3, 4`, are coarser than the canonical topology.*

<!-- original page 246 -->

*(iv) Every surjective family formed of flat and open morphisms (resp. flat and locally of finite presentation, resp. étale, resp. étale and finite) is covering for (fpqc) (resp. (fppf), resp. (ét), resp. (étf)).*

*(v) Every finite surjective family formed of flat and quasi-compact morphisms is covering for (fpqc). In particular, every faithfully flat and quasi-compact morphism is covering for (fpqc).*

*Proof.* (i) follows from 6.2.1, (ii) from 6.2.3, taking into account the fact that a sheaf for the Zariski topology transforms direct sums into products. Every representable functor being a sheaf for (Zar) and verifying condition (b) of (ii) by SGA 1, VIII 5.3, `T_1` is coarser than the canonical topology, which proves (iii).

Let us prove (iv). Let `{S_i → S}` be a family of morphisms as in the statement. Considering a covering of `S` by affine opens, one reduces immediately to the case where `S` is affine.[^N.D.E-IV-59]

Let us first treat the case where the morphisms `S_i → S` are flat and open (resp. étale). Let `S_{ij}` be a covering of `S_i` by affine opens. As the morphisms in question are open, the images `T_{ij}` of the `S_{ij}` form an open covering of `S`. As `S` is affine, hence quasi-compact, it is covered by a finite number of opens `T_{ij}`, for `(i, j)` running through a finite set `F`. Then `S′ = ⨆_F S_{ij}` is affine, and the morphism `S′ → S` belongs to `P′_1`, resp. `P′_3`, hence is covering. As it factors through the given family, the latter is covering.

In the case (étf), each `S_i` is finite over `S` hence is affine; in the preceding argument, one can then take the covering `{S_i}` of `S_i`, and one obtains that `S′ → S` belongs to `P′_4`.

Let us now consider the case where the morphisms `f_i : S_i → S` are flat and locally of finite presentation. For every `s ∈ S`, there exists, by (the proof of) EGA IV_4, 17.16.2, an affine subscheme `X(s)` of a certain `S_i`, such that `s ∈ f_i(X(s))` and that the morphism `g_i : X(s) → S`, restriction of `f_i`, is flat, of finite presentation, and quasi-finite. Then, `g_i(X(s))` is an open neighborhood `U(s)` of `s` (EGA IV_2, 2.4.6), and, `S` being affine, it is covered by a finite number of such opens `U(s_j)`, `j = 1, ..., n`. Consequently, `X′ = ⨆_j X(s_j)` is affine, and the morphism `X′ → S` is surjective, flat, of finite presentation, and quasi-finite, hence belongs to `P′_2`.[^N.D.E-IV-60] This completes the proof of (iv).

Let us prove (v). Let `{S_i → S}` be a finite faithfully flat and quasi-compact family. Let `T_j` be a covering of `S` by affine opens. The `S_{ij} = T_j ×_S S_i` are quasi-compact and therefore have finite affine open coverings `T_{ijk}`. Each morphism `T_{ijk} → T_j` is flat, and the family `{T_{ijk} → T_j}` is finite and surjective, hence covering for `T_1`. The family `{T_{ijk} → S}` is therefore also, by composition. It factors through the given family which is therefore also:

<!-- original page 247 -->

```text
S_i ←──── S_{ij} ←──── T_{ijk}
                          ╱
                         ╱
                        ╱
S ←──── T_j ←─────────
```

**Corollary 6.3.2.** *Let `(M_i)` be the following family of morphisms:*

<!-- label: III.IV.6.3.2 -->

- *(M_1) : faithfully flat and quasi-compact morphisms.*
- *(M_2) : faithfully flat morphisms locally of finite presentation.*
- *(M_3) : surjective étale morphisms.*
- *(M_4) : surjective étale finite morphisms.[^N.D.E-IV-61]*

*The family `(M_i)` verifies the axioms (a), (b), (c), (d_{T_i}) and (e_{T_i}) of 4.6.3.*

Indeed, for (a), (b), (c), it is classical (EGA and SGA 1, passim.).[^N.D.E-IV-62] By 6.3.1, (iv) and (v), `(M_i)` verifies (d_{T_i}). It remains to see that `(M_i)` verifies (e_{T_i}); for this, it suffices to see that `(M_i)` verifies (e_{T_1}), which entails the others. This follows from SGA 1, VIII (nos 4 and 5).

**Corollary 6.3.3.** *If `X` is a scheme and `R` an equivalence relation in `X` of type `(M_i)`, `R` is `(M_i)`-effective if and only if the sheaf-quotient of `X` by `R` for `T_i` is representable and in this case it is represented by the quotient `X/R`.*

<!-- label: III.IV.6.3.3 -->

Indeed, this is 4.6.5.

<!-- original page 248 -->

### 6.4. Effectivity conditions

We now seek families `(N)` of morphisms verifying axiom (f_T) of 4.7. Let us first remark that (f_{T_1}) entails (f_{T_i}), so that we may restrict ourselves to the case of the topology (fpqc).

**Lemma 6.4.1.** *The following families of morphisms verify axiom (f_{T_1}) of 4.7, that is, "descend by (fpqc)":*

<!-- label: III.IV.6.4.1 -->

- *(N) : open immersions.*
- *(N′) : closed immersions.*
- *(N″) : quasi-compact immersions.*

By virtue of 6.3.1 (ii), it suffices to verify that the given families descend by the Zariski topology and by a faithfully flat quasi-compact morphism. The first assertion is clear; let us verify the second. For (N), this is SGA 1, VIII 4.4; for (N′), this is loc. cit., 1.9. For (N″) one argues as in loc. cit., 5.5, using the two preceding results.

<!-- original page 245 -->

**Corollary 6.4.2.** *The same result holds for quasi-compact open immersions.*

<!-- label: III.IV.6.4.2 -->

These results allow one to apply to the present situation the general results of 4.7.1, 4.7.2, 5.1.8, 5.3.1, etc. Let us state one as an example, the first.

**Corollary 6.4.3.** *(= 4.7.1 + 4.6.10).* *Let `X` be a scheme and `R` an equivalence relation in `X`. Suppose that `R → X` is faithfully flat and quasi-compact and that `R → X × X` is a closed immersion (resp. open, resp. quasi-compact, resp. quasi-compact open). Then the sheaf-quotient `X/R` is the same for the topology (fpqc) and for the canonical topology, and for each scheme `S`, one has*

<!-- label: III.IV.6.4.3 -->

<!-- original page 249 -->

```text
(X/R)(S) = { closed (resp. open, resp. retrocompact[^N.D.E-IV-63], resp. open retrocompact)
             subschemes Z of X_S, stable under R × S, such that Z → S is
             faithfully flat quasi-compact and the diagram R_Z ⇒ Z → S is exact }.
```

### 6.5. Principal homogeneous bundles

Let us simply indicate the terminology:

```text
   topology     principal homogeneous bundles
   (fpqc)       "         "         "             (tout court)
   (ét)         "         "         "             quasi-isotrivial
   (étf)        "         "         "             locally isotrivial
   (Zar)        "         "         "             locally trivial.
```

### 6.6. Other topologies

One sometimes uses other topologies on the category of schemes. Let us indicate one: the *global étale finite* topology (étfg), generated by the pretopology whose covering families are the surjective families formed of étale finite morphisms. It is not finer than the Zariski topology. The corresponding principal homogeneous bundles are called "isotrivial".

<!-- original page 246 -->

```text
                     (canonical)
                         │
                       (fpqc)
                         │
                       (fppf)
                         │
                        (ét)
                         │
                       (étf)
                       ╱    ╲
                      ╱      ╲
                  (Zar)    (étfg)
                      ╲      ╱
                       ╲    ╱
                    (chaotic)[^N.D.E-IV-64]
```

### 6.7. Homogeneous spaces[^N.D.E-IV-65]

Let `G` be an `S`-group scheme, `X` an `S`-scheme with (left) operator group `G`, and

```text
Φ : G ×_S X ⟶ X ×_S X
```

the morphism of `S`-schemes defined setwise by `(g, x) ↦ (gx, x)`. Let us recall (cf. 5.1.0 and III.0.1) that one says that `X` is a *formally principal homogeneous space* under `G` if the following equivalent conditions are satisfied:

(i) for every `T → S`, the set `X(T)` is empty or principal homogeneous under `G(T)`,

(ii) `Φ` is an isomorphism of `S`-functors,

(iii) `Φ` is an isomorphism of `S`-schemes.

(The equivalence (i) ⇔ (ii) is clear, and one has (ii) ⇔ (iii) since `C = (Sch/S)` is a full subcategory of `Ĉ`.)

The definition of formally homogeneous space (not necessarily principal homogeneous) is obtained by requiring that `Φ` be an epimorphism in the category of sheaves for an appropriate topology `T`. Indeed, the condition that `Φ` be an epimorphism of `S`-functors amounts to the requirement that, for every `T → S`, the set `X(T)` be empty or homogeneous (not necessarily principal homogeneous) under `G(T)`, but this condition is too restrictive, as the following simple example shows. Let `S = Spec R`, `G = G_{m,R}` and `X = G_{m,R}` on which `G` acts via `t · x = t² x`. Then the morphism `Φ` is étale, finite, and surjective, hence an epimorphism in the category of sheaves for the topology (étf) (a fortiori, an epimorphism of `S`-schemes); on the other hand, the points `1` and `−1` of `X(R)` are not conjugate by an element of `G(R)`, so that the morphism `G(R) × X(R) → X(R) × X(R)` is not surjective.[^N.D.E-IV-66] One is therefore led to lay down the following definition:

<!-- original page 247 -->

**Definition 6.7.1.** *Let `G` be an `S`-group, `X` an `S`-scheme with operator group `G`, and `T` a topology on `(Sch/S)`, coarser than the canonical topology. We say that `X` is a* formally homogeneous space under `G` (relative to the topology `T`) *if the following equivalent conditions are satisfied:*

<!-- label: III.IV.6.7.1 -->

*(i) the morphism `Φ : G ×_S X → X ×_S X` is an epimorphism in the category of sheaves for the topology `T`,*

*(ii) for every `T → S`, and `x, y ∈ X(T)`, there exists a morphism `T′ → T` covering for the topology `T`, and `g ∈ G(T′)`, such that `y_{T′} = g · x_{T′}`.*

**Remark 6.7.2.** *Condition (i) implies, in particular, that `Φ` is a universal effective epimorphism in `(Sch/S)` (cf. 4.4.3). This entails, as one easily sees, that `Φ` is surjective (cf. 1.3, N.D.E. (3)).*

<!-- label: III.IV.6.7.2 -->

**Proposition and Definition 6.7.3.**[^N.D.E-IV-67] *Let `G` be an `S`-group, `X` an `S`-scheme with operator group `G`, and `T` a topology on `(Sch/S)`, coarser than the canonical topology. The following conditions are equivalent:*

<!-- label: III.IV.6.7.3 -->

*(i) `X` verifies the two hypotheses below:*

- *(1) the morphism `Φ : G ×_S X → X ×_S X` is covering, i.e. `X` is a `G`-formally homogeneous space,*
- *(2) the morphism `X → S` is also covering, i.e. locally for the topology `T`, it has a section (cf. RefIV.4.4.8bis.bis).*

*(ii) "Locally on `S` for the topology `T`", `X` is isomorphic, as a scheme with operator group `G`, to the sheaf quotient (for `T`) of `G` by a sub-group-scheme `H`, i.e. there exists a covering family `{S_i → S}` such that each `X ×_S S_i` represents the sheaf quotient of `G ×_S S_i` by a certain sub-group-scheme `H_i`.*

*Under these conditions, one says that `X` is a `G`-*homogeneous space* (relative to the topology `T`).*

*Proof.* Suppose (ii) is verified. Set `G_i = G ×_S S_i` and `X_i = X ×_S S_i`. Then, `X_i` has a section over `S_i`, namely the composite of the unit section `ε_i : S_i → G_i` and the projection `π_i : G_i → X_i = G_i/H_i`. Hence `X → S` is covering.

<!-- original page 248 -->

On the other hand, `π_i` is covering, hence `π_i × π_i` is also (cf. 4.2.3 (C 1) and (C 2)), and one has a commutative diagram:

```text
                 Φ_i
G_i ×_{S_i} X_i ────→ G_i ×_{S_i} X_i
       ↑                       ↑
  id × π_i                   π_i × π_i
       │                       │
                 Ψ_i
G_i ×_{S_i} G_i ────→ G_i ×_{S_i} G_i
                  ∼
```

where `Φ_i` is deduced from `Φ` by the base change `S_i → S` and `Ψ_i` is the isomorphism defined setwise by `(g, g′) ↦ (gg′, g)`. Then `(π_i × π_i) ∘ Ψ_i` is covering, hence `Φ_i` is also (4.2.3 (C 3)). This shows that `Φ` is "locally covering", hence is covering (4.2.3 (C 5)). This proves that (ii) ⇒ (i).

Conversely, suppose (i) is verified, and suppose moreover that the structural morphism `X → S` has a section `σ`. By EGA I, 5.3.13, `σ` is an immersion. Let us define `H = G ×_X S` by the diagram below, in which the two squares are cartesian:

```text
H ──→ G ──id_G ⊠ σ──→ G ×_S X
│      │                 │
│      π                 Φ
↓ σ    ↓    id_X ⊠ σ     ↓
S ──→ X ──────────────→ X ×_S X
```

where `π`, `id_G ⊠ σ` and `id_X ⊠ σ` denote the morphisms defined setwise, for `T → S` and `g ∈ G(T)`, `x ∈ X(T)`, by:

```text
π(g) = g · σ_T,    (id_G ⊠ σ)(g) = (g, σ_T),    (id_X ⊠ σ)(x) = (x, σ_T).
```

Then, `π` is covering, and `H` is a sub-group-scheme of `G`, representing the stabilizer `Stab_G(σ)` of `σ` (cf. I, 2.3.3), i.e., for every `T → S`, one has:

```text
H(T) = { g ∈ G(T) | g · σ_T = σ_T }.
```

Let us denote `G/H` the presheaf `T ↦ G(T)/H(T)`, and `a(G/H)` the associated sheaf, for the topology `T`. By what precedes, one obtains a commutative diagram of morphisms of presheaves with operator group `G`:

```text
G ──π──→ X
 ╲       ↗
  ╲     ╱ π̄
   ↘   ╱
   G/H
```

where `π̄` is a monomorphism. As `π` is covering, `π̄` is also and therefore, by 4.3.12, `π̄` induces an isomorphism `a(G/H) ⥲ X`. One has therefore proved that: if `X` is a `G`-homogeneous space such that `X → S` admits a section `σ`, then `X` represents the sheaf quotient `G/H`, where `H = G ×_X S` is the stabilizer of `σ`.

In the general case, there exists by hypothesis a covering family `{S_i → S}` such that each morphism `X_i = X ×_S S_i → S_i` has a section `σ_i`. Set `G_i = G ×_S S_i`; then the morphism `Φ_i : G_i ×_{S_i} X_i → X_i ×_{S_i} X_i` deduced from `Φ` by the base change `S_i → S` is again covering. Hence, by what precedes, `X_i ≅ G_i/H_i`, where `H_i` is the stabilizer in `G_i` of `σ_i`. This completes the proof of the implication (i) ⇒ (ii).

<!-- original page 249 -->

## Bibliography

<!-- original page 250 -->

- [AS] *Analysis Situs*, by J. Giraud, Sém. Bourbaki, Exp. 256, May 1963.
- [D] *Méthode de la descente*, by J. Giraud, Mém. Soc. Math. France, t. 2 (1964), p. iii–viii + 1–150.
- [MA] *Grothendieck Topologies*, by M. Artin, mimeographed notes, Harvard, 1962.
- [SGA 1] *Séminaire de Géométrie Algébrique du Bois-Marie 1960–61, Revêtements étales et groupe fondamental*, Lecture Notes in Maths. 224 (1971), revised and annotated edition, Documents Math. 3, Soc. Math. France, 2003.
- [SGA 4] *Séminaire de Géométrie Algébrique du Bois-Marie 1963–1964, Théorie des topos et cohomologie étale des schémas*, t. I, II, III, Lecture Notes in Maths. 269, 270 (1972), 305 (1973).
- [TDTE I] *Techniques de descente et théorèmes d'existence en géométrie algébrique I. Généralités. Descente par morphismes fidèlement plats*, by A. Grothendieck, Sém. Bourbaki, Exp. 190, Dec. 1959.
- [Ray70][^N.D.E-IV-68] M. Raynaud, *Faisceaux amples sur les schémas en groupes et les espaces homogènes*, Lect. Notes Math. 119, Springer-Verlag, 1970.

## Footnotes

[^N.D.E-IV-40]: N.D.E.: and we shall also write `h_S = Ŝ`, cf. the first commutative diagram of 4.5.4.

[^N.D.E-IV-41]: N.D.E.: i.e., such that for every object `T → S` of `C/S`, every covering sieve `R′` of `i_S(T → S) = T`, considered as a sieve of `(T → S) ∈ Ob C/S`, is covering.

[^N.D.E-IV-42]: N.D.E.: We have expanded the original in what follows.

[^N.D.E-IV-43]: N.D.E.: `R × S` denotes the equivalence relation in `X × S` defined by `R × S_{diagonal} ⊂ X × X × S × S`, and `R_Z` is the equivalence relation it induces in `Z` (cf. 3.1.6).

[^N.D.E-IV-44]: N.D.E.: Recall that `T` denotes the given topology on `C`, coarser than the canonical topology.

[^N.D.E-IV-45]: N.D.E.: We have added this corollary.

[^N.D.E-IV-46]: N.D.E.: We have placed the axiom (f_M) here (which figured before Proposition 4.7.2).

[^N.D.E-IV-47]: N.D.E.: cf. § 6.4, see also VI_A, 5.3.1.

[^N.D.E-IV-48]: N.D.E.: We have introduced the numbering 5.1.0, to refer to it later.

[^N.D.E-IV-49]: N.D.E.: One also says "pseudo-torsor", cf. EGA IV_4, 16.5.15. On the other hand, the more general notion of formally homogeneous object (not necessarily principal homogeneous), is defined in the addendum 6.7.1 at the end of this Exposé.

[^N.D.E-IV-50]: N.D.E.: In this case, one also says that `X` is an `H`-torsor.

[^N.D.E-IV-51]: N.D.E.: We have added this particular case as a corollary, which will be used several times in the following Exposés.

[^N.D.E-IV-52]: N.D.E.: We have added "and free".

[^N.D.E-IV-53]: N.D.E.: of `C`.

[^N.D.E-IV-54]: N.D.E.: In fact, the isomorphisms established in 5.2.8 to 5.2.10 would deserve to be called "Noether isomorphism theorems".

[^N.D.E-IV-55]: N.D.E.: This follows from the proposition applied to `K = H`.

[^N.D.E-IV-56]: N.D.E.: We have corrected the original here.

[^N.D.E-IV-57]: N.D.E.: Let `P″_2` denote the set of finite surjective families, composed of flat morphisms of `C ′` of finite presentation. According to Proposition 6.3.1 below, the topology `T_2` generated by `P` and `P′_2` coincides with the topology generated by `P` and `P″_2`. This follows from the results of EGA IV_4, § 17.16 on quasi-sections; see the proof of 6.3.1. Let us cite here the following particular case of EGA IV_4, 17.16.2: let `S` be affine and `f : X → S` a surjective flat morphism locally of finite presentation; then there exists a morphism `S′ → S` faithfully flat, of finite presentation, quasi-finite, with `S′` affine, and an `S`-morphism `S′ → X`.

[^N.D.E-IV-58]: N.D.E.: By hypothesis, each family `{S_{pq} → S} ∈ P′_i` is finite, hence `S′_p = ⨆_q S_{pq}` is affine and the family can therefore be replaced by the morphism `S′_p → S_p`, which still belongs to `P′_i`.

[^N.D.E-IV-59]: N.D.E.: We have simplified what follows, taking advantage of the fact that `S` is henceforth assumed affine.

[^N.D.E-IV-60]: N.D.E.: This shows that, if one denotes `P″_2` the set of finite surjective families of morphisms of `C ′` flat of finite presentation, the topology generated by `P` and `P″_2` equals `T_2`. On the other hand, with the notations at the start of the proof of (iv), if one takes a covering of `S_i` by affine opens, of finite presentation over `S`, one obtains that `S′ → S` belongs to `P″_2`.

[^N.D.E-IV-61]: N.D.E.: We have corrected the original by adding the surjectivity hypothesis for `(M_3)` and `(M_4)`, which is automatically satisfied in the other cases.

[^N.D.E-IV-62]: N.D.E.: cf. EGA I, 6.6.4 for "quasi-compact", EGA II, 6.1.5 for "finite", EGA IV_1, 1.6.2 for "locally of finite presentation", EGA IV_2, 2.2.13 for "faithfully flat", and EGA IV_4, 17.3.3 for "étale".

[^N.D.E-IV-63]: N.D.E.: Recall that a subscheme `Z` of a scheme `T` is said to be *retrocompact* if the immersion `Z ↪ T` is quasi-compact, cf. EGA 0_III, 9.1.1.

[^N.D.E-IV-64]: N.D.E.: Recall (cf. 4.4.2) that the chaotic topology is the coarsest topology, defined by `J(S) = {S}` for every `S ∈ Ob C`.

[^N.D.E-IV-65]: N.D.E.: We have added the numbers that follow.

[^N.D.E-IV-66]: N.D.E.: Evidently, this difficulty arises from the fact that if `C ′` is a full subcategory of `Ĉ` containing `C`, for example, the category `C̃_T` of sheaves on `C` for a topology `T` coarser than the canonical topology, and if `f : X → Y` is a morphism in `C`, then the implications:
    ```text
    f epimorphism of Ĉ ⇒ f epimorphism of C ′ ⇒ f epimorphism of C
    ```
    are in general strict.

[^N.D.E-IV-67]: N.D.E.: cf. [Ray70], Def. VI.1.1.

[^N.D.E-IV-68]: N.D.E.: We have added this reference.

<!-- LEDGER DELTA — Exposé IV — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| topologie moins fine | coarser topology | "Moins fine" means having fewer covering sieves; preserve the comparative idiom. |
| raffinement | refinement | Standard in topos theory; sieve-theoretic sense. |
| crible couvrant | covering sieve | Standard. |
| faisceau relatif | relative sheaf | Per Definition 4.5.10. |
| sous-faisceau | sub-sheaf | Hyphenated to match SGA 1/2. |
| sous-S-faisceau | sub-`S`-sheaf | Preserve hyphenation around the base. |
| quarrable | squarable | Historical SGA term; mathlib usage. Modern English often: "with representable diagonal" / "with squarable structural morphism". |
| (M)-effective | (M)-effective | Preserve the parenthesized family-name as in source. |
| relation d'équivalence (M)-effective | (M)-effective equivalence relation | Standard. |
| extension de la base | base extension | Sometimes "base change" — used both. |
| changement de base | base change | Standard. |
| stable par changement de base | stable under base change | Standard. |
| descente | descent | Standard. |
| donnée de descente | descent datum | Plural: descent data. |
| descend par la topologie | descends by the topology | Preserve the source's metaphor. |
| descendu (objet) | descended (object) | Standard. |
| morphisme couvrant | covering morphism | Standard. |
| famille couvrante | covering family | Standard. |
| morphisme effectif universel | universal effective morphism | Standard. |
| épimorphisme effectif universel | universal effective epimorphism | Standard. |
| sous-foncteur représentable | representable subfunctor | Standard. |
| objet quarrable | squarable object | See above. |
| ⨆ (somme directe) | ⨆ / disjoint union / direct sum | Source uses `⨆` for `∐`; rendered as `⨆`. |
| espace formellement principal homogène | formally principal homogeneous space | Per 6.7. |
| espace formellement homogène | formally homogeneous space | Per 6.7. |
| espace homogène | homogeneous space | Per 6.7. |
| fibré principal homogène | principal homogeneous bundle | Per 5.1.5. "Torsor" is the modern term and appears in N.D.E. (50). |
| pseudo-torseur | pseudo-torsor | Per N.D.E. (49). |
| torseur | torsor | Modern term used in N.D.E. (50). |
| H-torseur | H-torsor | Standard. |
| quasi-isotrivial / localement isotrivial / isotrivial | quasi-isotrivial / locally isotrivial / isotrivial | Per 6.5 and 6.6. Preserve the "iso-" prefix. |
| localement trivial | locally trivial | Standard. |
| trivial (à groupe d'opérateurs) | trivial (with operator group) | Per 5.1.1. |
| objet à groupe d'opérateurs | object with operator group | Standard. |
| objet à opérateurs | object with operators | Standard. |
| à droite / à gauche | on the right / on the left | Preserve the side. |
| sous-schéma rétrocompact | retrocompact subscheme | Per N.D.E. (63); historical term from EGA. |
| immersion quasi-compacte | quasi-compact immersion | Standard. |
| immersion ouverte | open immersion | Standard. |
| immersion fermée | closed immersion | Standard. |
| morphisme fidèlement plat | faithfully flat morphism | Standard. |
| morphisme quasi-compact | quasi-compact morphism | Standard. |
| morphisme de présentation finie | morphism of finite presentation | Per SGA 3 Introduction §6. |
| localement de présentation finie | locally of finite presentation | Standard. |
| morphisme quasi-fini | quasi-finite morphism | Standard. |
| morphisme étale | étale morphism | Standard. |
| morphisme étale fini | étale finite morphism | Standard. |
| topologie fidèlement plate quasi-compacte | faithfully flat quasi-compact topology | Acronym (fpqc). |
| topologie fidèlement plate de présentation finie | faithfully flat of finite presentation topology | Acronym (fppf). |
| topologie étale | étale topology | Acronym (ét). |
| topologie étale finie | étale finite topology | Acronym (étf). |
| topologie étale finie globale | global étale finite topology | Acronym (étfg). Per 6.6. |
| topologie chaotique | chaotic topology | Per N.D.E. (64). |
| foncteur de nature locale | functor of local nature | Per 6.1.1. |
| translation à droite / à gauche | right / left translation | Standard. |
| saturé (d'un sous-objet) | saturation (of a sub-object) | Per 4.4.12 and 5.2.8. |
| sous-groupe invariant | invariant subgroup | SGA convention; English "normal subgroup" would be modernizing. |
| théorème de Noether | Noether's theorem | Per 5.3 title and N.D.E. (54). |
| sommes amalgamée | amalgamated sum | Standard. |
| passage au quotient | passage to the quotient | Standard. |
| objet final | final object | Standard. |
| section unité | unit section | Standard. |
| stabilisateur | stabilizer | American spelling. |
-->



