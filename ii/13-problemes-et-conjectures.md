# Exposé XIII. Problems and conjectures

<!-- label: XIII -->

<!-- original page 135 -->

## 1. Relations between global and local results. Affine problems related to duality

<!-- label: XIII.1 -->

<!-- original page 172 -->

It is well known that many statements concerning a projective scheme `X` can be formulated in terms of statements
concerning a certain graded ring, or better a complete local ring, namely the homogeneous coordinate ring of `X` (i.e.
the affine ring of the projecting cone `X̃` of `X`), or its completion (i.e. the completion of the local ring of the
vertex of `X̃`). The interest of this reformulation is that it often allows one, starting from known global results, to
conjecture, and even to prove, analogous results for complete noetherian local rings more general than those which
really appear in the global statement, for instance for local rings that are not necessarily of equal characteristic.
Thus, Serre's duality theorem for projective space (XII 1.1) suggested the useful local duality theorem (V 2.1). Serre's
fundamental theorem on the cohomology of coherent Modules on projective space (finiteness, asymptotic behavior for large
`n` of `Hⁱ(X, F(n))`, cf. EGA III 2.2.1) generalizes to a structure theorem for the local invariants `Hⁱ_𝔪(M)`, see V 3.
Likewise, the Lefschetz theorems for the fundamental group, and for the Picard group ("equivalence criteria"), well
familiar in the classical case and subsequently extended to an arbitrary base field, suggested the "local" Lefschetz
theorems of Exposés X and XI. Of course, the local theorems are in turn precious tools for obtaining global statements.
For example, local duality permits one to formulate a global asymptotic property (XII 1.3 (i)) by the vanishing of
certain local invariants `Hⁱ(Fₓ)`. More substantially, the local Lefschetz theorems, implying for instance the "purity"
or the parafactoriality of certain local rings that are complete intersections (X 3.4 and XI 3.13), allow one, in the
global Lefschetz theorems, to dispose of certain non-singularity hypotheses, as in X 3.5, 3.6, 3.7.

<!-- original page 173 -->

Another useful generalization of the theorems concerning projective schemes over a field `k` consists in replacing `k`
by a general base scheme. Thus, the sequel of EGA III will give[^N.D.E-XIII-1] a generalization in this direction of
Serre duality[^XIII-1-1]; the theorems on finiteness and asymptotic behavior of the `Hⁱ(X, F(n))` were stated in EGA III
2.2.1 over a general base scheme, and finally the Lefschetz theorems can equally be developed for a projective morphism,
as we saw in XII 4.9, thanks to the local theorem XII 4.7. Of course, working over a general base scheme also leads to
essentially new statements, such as the "comparison theorem" EGA III 4.15 and the existence theorem for sheaves EGA III
5.1.4 (which, as we saw moreover in IX, derive from the same key cohomological theorems as the Lefschetz theorems for
`π₁` and `Pic`).

It then becomes necessary to extract theorems that simultaneously encompass the two generalizations we have just
indicated of statements concerning projective schemes over a field. The natural objects for such a common generalization
are noetherian rings that are separated and complete for an `I`-adic topology. Their study, from this point of view, has
not yet been seriously addressed, and seems to me at the present time the most interesting subject in the local theory
of coherent sheaves. Here is a typical problem in this direction:

**Conjecture 1.1** ("Second affine finiteness theorem"[^XIII-1-2][^N.D.E-XIII-2]).

<!-- label: XIII.1.1 -->

Let `M` be a finitely generated module over a noetherian ring `A` (which one will, if necessary, assume to be a quotient
of a regular ring), and let `J` be an ideal of `A`. Prove that the modules `Hⁱ_J(M)` are

<!-- original page 174 -->

"`J`-cofinite", i.e. that the modules

```text
Hom_A(A/J, Hⁱ_J(M))
```

are finitely generated.

Recall that `Hⁱ_J(M)` denotes the module `Hⁱ_Y(X, M̃)` (where `X = Spec(A)`, `Y = V(J)`) of Exposé I, interpreted in II
in terms of a direct limit of cohomologies of Koszul complexes, or again for `i ⩾ 2` the module `Hⁱ⁻¹(X − Y, M̃)`.
Actually, 1.1 should be a consequence of a more precise statement, implying that the `Hⁱ_J(M)` lie in a suitable abelian
subcategory `𝒟_J` of the category `𝒞_J` of `A`-modules of support `⊂ Y = V(J)`, such that `H ∈ Ob 𝒟_J` implies that `H`
is `J`-cofinite. (N.B. The category of modules `H` of support contained in `V(J)` that are `J`-cofinite is unfortunately
not stable under passage to a quotient!). The essential problem would then consist in defining `𝒟_J`. More precisely,
the solution of problem 1.1 should follow (at least if `A` is a quotient of a regular ring) from a duality theory,
generalizing both local duality and the duality theory of projective morphisms to which we alluded above, and which
would be of the following kind:

**Conjecture 1.2** ("Affine duality"[^XIII-1-3]).

<!-- label: XIII.1.2 -->

Suppose `A` is regular, separated and complete for the `J`-adic topology. Let `C•(A)` be an injective resolution of `A`.

(i) Prove that the functor

```text
D_J : L• ↦ Hom_J(L•, C•(A))
```

from the category of complexes of `A`-modules that are free of finite type in each dimension and bounded above in degree
(where morphisms are homomorphisms of complexes up to homotopy) into the category of complexes of `A`-modules `K•` that
are injective in each dimension and bounded above in degree (where the morphisms are defined similarly) is fully
faithful.

(ii) Prove that for every `K•` of the form `D_J(L•)`, the `Hⁱ(K•) (= Extⁱ_Y(X; L•, 𝒪_X))` are `J`-cofinite.

(iii) More precisely, prove that the `K•` that are homotopic to a complex of the form `D_J(L•)` can be characterized by
finiteness properties of the `Hⁱ(K•)`, stronger than the one envisaged in (ii), for example by the property
`Hⁱ(K•) ∈ Ob 𝒟_J`,

<!-- original page 175 -->

where `𝒟_J` is a suitable abelian category, as envisaged above.

Note that the problem is resolved in the affirmative when `A` is local and `J` is an ideal of definition of it (cf. Exp.
IV), and also when `J` is the zero ideal. In these two cases, exceptionally, one can confine oneself to taking for `𝒟_J`
the category of Modules with support `V(J)` that are `J`-cofinite, (which in the second case signifies simply that one
takes the category of finitely generated Modules over `A`). An affirmative solution of

<!-- original page 138 -->

conjecture 1.2 in general would give one for 1.1, by taking for `L•` the dual of a free finitely generated resolution of
`M`. On the other hand, an affirmative solution of 1.1 would give an affirmative answer to the first part of the
following conjecture, which we formulate in "global" form:

**Conjecture 1.3.**

<!-- label: XIII.1.3 -->

Let `X ⊂ 𝐏^r_k` be a closed subscheme of standard projective space that is locally a complete intersection and every
irreducible component of which is of codimension `⩾ s`. Let `U = 𝐏^r_k − X`.

(i) Prove that for every coherent Module `F` on `U`, one has

```text
dim Hⁱ(U, F) < +∞   for i ⩾ s.
```

[^XIII-1-4]

(ii) Give an example, with `X` connected and regular, where one has

```text
Hˢ(U, F) ≠ 0.
```

To see that (i) is a particular case of 1.1, one considers

```text
Hⁱ(U, F(·)) = ⊕_n Hⁱ(U, F(n)) = Hⁱ(𝐄^{r+1} − X̃, F̃)
```

as a module over the affine ring `k[t₀, …, t_r]` of the projecting cone `𝐄^{r+1}` of `𝐏^r`. This module is none other
than `Hⁱ⁺¹_J(M)`, where `J` is the ideal of the projecting cone `X̃` of `X` in `𝐄^{r+1}`.

<!-- original page 176 -->

On the other hand, from the hypothesis made on `X`, which implies that `X̃` is also a complete intersection of
codimension `⩾ s` at every point of `𝐄^{r+1}` distinct from the origin, it follows that `Hⁱ⁺¹_J(M)` is zero outside the
origin for `i ⩾ s`. If it is therefore `J`-cofinite as 1.1 demands, it is *a fortiori* `𝔪`-cofinite, which easily
implies that it is finite-dimensional in each degree[^N.D.E-XIII-3]. Note moreover that conjecture 1.3 is already posed
for a non-singular irreducible curve `X` in `𝐏³`; one does not know in this case whether the `H²(𝐏³ − X, 𝒪_X(n))` are
finite-dimensional, or whether they are necessarily zero[^XIII-1-5]. One does not even know whether there exists an
irreducible curve in `𝐏³` that is not set-theoretically the intersection of two hypersurfaces[^N.D.E-XIII-4].

**Problem 1.4.**

<!-- label: XIII.1.4 -->

Give an affine variant of the "comparison theorem" EGA III 4.1.5 as a theorem of commutation of the functors `Hⁱ_J` with
certain inverse limits.

Finally, in the present order of ideas, I had posed the following problem: let `A` be a complete regular noetherian
local ring, `K` its fraction field; prove that `Extⁱ_A(K, A) = 0` for every `i`. An affirmative answer was given on the
spot by M. Auslander: the regularity hypothesis can be replaced by the assumption that `A` is integral, and in fact it
is true that `Extⁱ_A(K, M) = 0` for every `i`, as soon as `M` is finitely generated over `A`. This follows immediately
from the following statement, due to Auslander: if `A` is a complete noetherian local ring, then for every finitely
generated module `M` over `A`, the functors `Extⁱ_A(·, M)` transform direct limits into inverse limits[^N.D.E-XIII-5].

## 2. Problems related to `π₀`: local Bertini theorems

<!-- label: XIII.2 -->

Let `A` be a complete noetherian local ring, `f` an element of its maximal ideal, `X = Spec(A)`, `Y = Spec(A/fA)`. The
use of the local "Lefschetz" technique allows one to give criteria for `Y' = X' ∩ Y` (where `X' = X − {𝔪}`) to be
connected, in terms of hypotheses on `X'`. Thus, it suffices that one have: a) `X'` connected, b) `prof 𝒪_{X',x} ⩾ 2`

<!-- original page 177 -->

for every closed point `x` of `X'`, c) `f` is `A`-regular. One notes however that hypotheses b) and c) are not of purely
topological nature; for instance, they are not invariant under replacing `X` by `X_red`. In the analogous situation for
a projective scheme `X'` over a field and a hyperplane section `Y'` of `X'`, the use of "Bertini's theorem" and
Zariski's "connection theorem" allows one in fact to obtain results of distinctly more satisfactory appearance, which
had led me in the oral seminar to state a conjecture, which I have since resolved in the affirmative. Let us therefore
state here:

**Theorem 2.1.**

<!-- label: XIII.2.1 -->

Let `A` be a complete noetherian local ring, `X` its spectrum, `a` the closed point of `X`, `X' = X − {a}`. Suppose that
`X` satisfies the conditions (where `k` denotes an integer `⩾ 1`):

`a_k`) The irreducible components of `X'` are of dimension `⩾ k + 1`.

<!-- original page 140 -->

`b_k`) `X'` is connected in dimension `⩾ k`, i.e. one cannot disconnect `X'` by a closed part of dimension `< k` (cf.
III 3.8).

Let `m` be an integer, `0 ⩽ m ⩽ k`, and let `f₁, …, f_m ∈ 𝔯(A)`; set `B = A / ∑ᵢ fᵢA`,
`Y = Spec(B) = V(f₁) ∩ ⋯ ∩ V(f_m)`, `Y' = X' ∩ Y = Y − {a}`. Then `Y` satisfies the conditions `a_{k−m}`), `b_{k−m}`).
In particular, for every sequence of `m ⩽ k` elements `f₁, …, f_m` of `𝔯(A)`, `Y' = X' ∩ V(f₁) ∩ ⋯ ∩ V(f_m)` is
connected.

It is moreover easy to see that if the last conclusion holds (it evidently suffices to take `m = k` there), and
excluding the case where `X` would be irreducible of dimension 0 or 1, it follows that the irreducible components of
`X'` are of dimension `⩾ k + 1`, and `X'` is connected in dimension `⩾ k`, so that in a sense, 2.1 is a "best possible"
result.

Let us give the principle of the proof of 2.1. Only condition `b_{k−m}`) for `Y` poses a problem. One reduces easily,
for given `k`, to the case where `X` is integral, and even (by passing to the normalization, which is finite over `X`)

<!-- original page 178 -->

to the case where `X` is normal. If `k = 1`, hence `dim X' ⩾ 2`, then `X'` is of depth `⩾ 2` at its closed points, and
one can apply the result recalled at the beginning of the section, which shows that `Y' = X' ∩ V(f)` is connected. In
the case `k ⩾ 1`, one supposes the theorem proved for `k' < k`. By induction on `m`, one is reduced to the case where
`m = 1`, i.e. to verifying that for `f₁ ∈ 𝔯(A)`, `X' ∩ V(f₁)` is connected in dimension `⩾ k − 1`. If it were not, i.e.
if it were disconnected by a `Z'` of dimension `< k − 1`, there would exist a sequence `f₂, …, f_k` such that
`X' ∩ V(f₁) ∩ ⋯ ∩ V(f_k)` is disconnected, and in this sequence one can choose `f₂ ∈ 𝔯(A)` arbitrarily, subject to the
sole condition of not vanishing at any point of a certain finite part `F` of `X'` (namely the set of maximal points of
`Z'`). Moreover, one verifies easily, using the fact that `X'` is normal, hence satisfies Serre's condition
(`S₂`)[^XIII-2-1], that there exists a finite part `F'` of `X'` such that `f ∈ 𝔯(A)`, `V(f) ∩ F' = ∅` implies that
`V(f) ∩ X'` also satisfies condition (`S₂`). One can then choose `f₂` in such a way that `f₂` vanishes neither on `F`
nor on `F'`, hence such that `X' ∩ V(f₂)` satisfies (`S₂`). But then, by virtue of Hartshorne's theorem III 3.6,
`X' ∩ V(f₂)` is connected in codimension 1, hence (since every component of `X' ∩ V(f₂)` is of dimension `⩾ k`) it is
connected in dimension `⩾ k − 1`. Applying the induction hypothesis to `V(f₂) = Spec(A/f₂A)`, it follows that
`X' ∩ V(f₂) ∩ V(f₁) ∩ V(f₃) ∩ ⋯ ∩ V(f_k)` is connected, whereas it had been constructed disconnected — absurd.

Let us point out some interesting corollaries:

**Corollary 2.2.**

<!-- label: XIII.2.2 -->

Let `f : X → Y` be a proper morphism of locally noetherian preschemes, with `Y` integral, `y₀ ∈ Y`, `y₁` the generic
point of `Y`. Suppose

a) `Y` is unibranch at `y₀`, and every irreducible component of `X` dominates `Y`.

<!-- original page 141 -->

b) The irreducible components of `X_{y₁}` are of dimension `⩾ k + 1`, and `X_{y₁}` is connected in dimension `⩾ k`.

<!-- original page 179 -->

Then the irreducible components of `X_{y₀}` are of dimension `⩾ k + 1`, and `X_{y₀}` is connected in dimension `⩾ k`.

Indeed, Zariski's connection theorem (cf. EGA III 4.3.1) implies that `X_{y₀}` is connected; to show that it is not
disconnected by a closed part of dimension `< k`, one is reduced to showing that the local rings at points `x ∈ X_{y₀}`
such that `dim x < k` have a spectrum not disconnected by `x`. Now this is true without assuming either `f` proper, or
`Y` unibranch at `y₀`. One reduces, to see this, to the case where `X` is integral dominating `Y`, and if one wishes `Y`
affine of finite type over `ℤ`, so that one is under the conditions of the dimension formula for `𝒪_{X,x}` over
`𝒪_{Y,y₀}`. Using in this case the finiteness of the normal closure, one can even suppose `X` normal, hence by virtue of
a theorem of Nagata[^XIII-2-2], the completion of a local ring `𝒪_{X,x}` of `X'` is again normal; hence (if `𝒪_{X,x}` is
of dimension `N`) `Spec(𝒪̂_{X,x})` is connected in dimension `⩾ N − 1`. Let `n = dim 𝒪_{Y,y₀}`; then
`deg tr k(x)/k(y) < k` implies `dim 𝒪_{X,x} > n + (k + 1) − k = n + 1`, taking into account `dim X_{y₁} ⩾ k + 1`, and
taking a system `f₁, …, f_n` of parameters of `𝒪_{Y,y₀}` which one lifts to elements of `𝒪_{X,x}`, one sees by 2.1 that
`Spec(𝒪̂_{X,x} / ∑ fᵢ 𝒪̂_{X,x})` is connected in dimension `⩾ 1`, i.e. is not disconnected by its closed point, or
equivalently, `Spec(𝒪̂_{X_{y₀},x})` is not disconnected by its closed point; *a fortiori* the same holds for
`Spec(𝒪_{X_{y₀},x})`.

As in the case of the ordinary connection theorem, one can vary 2.2 by taking geometric fibers (over the algebraic
closures of the residue fields), provided one supposes `Y` geometrically unibranch at `y₀`, or (without other hypothesis
than `Y` noetherian) that `f` is universally open. Applying this to the case where `Y` is the dual scheme of a
projective scheme `𝐏^r_k` over a field, one recovers a strengthened form of the global result that had inspired 2.1,
namely:

**Corollary 2.3**[^N.D.E-XIII-6].

<!-- label: XIII.2.3 -->

Let `X` be a closed subscheme of `𝐏^r_k` (`k` a field); suppose the irreducible components of `X` are of dimension
`⩾ l + 1`, and `X` geometrically connected in dimension `⩾ l`.

<!-- original page 180 -->

Then for every sequence `H₁, …, H_m` of `m` hyperplanes of `𝐏^r_k` (`0 ⩽ m ⩽ l − 1`), `X ∩ H₁ ∩ ⋯ ∩ H_m` satisfies the
same condition with `l − m`, in particular is geometrically connected in dimension `⩾ l − 1`.

One can moreover modify this statement in an obvious way for the case where one is given a proper morphism `X → 𝐏^r_k`,
which is not necessarily an immersion; an analogous extension is possible for 2.1 (by considering a proper scheme over
`X'`).

<!-- original page 142 -->

These statements are moreover formally deduced from the statements given here, taking into account the ordinary
connection theorem which reduces us to the case of a finite morphism.

**Corollary 2.4.**

<!-- label: XIII.2.4 -->

Let `A` be a complete noetherian normal local ring of dimension `⩾ k + 2`. Let `X = Spec(A)`, `X' = X − {a}`, and
`f₁, …, f_k` elements of `𝔯(A)`; then `Y' = X' ∩ V(f₁) ∩ ⋯ ∩ V(f_k)` is connected, and `π₁(Y') → π₁(X')` is surjective.

One proceeds as in SGA 1 X 2.11.

In all this, only questions of connectedness were at issue. Now in the global case, well-known theorems assert that for
an irreducible projective variety `X ⊂ 𝐏^r_k`, `k` algebraically closed, its intersection with a sufficiently "general"
hyperplane `H` is irreducible (and not merely connected): this is Bertini's theorem, proved by Zariski, which in turn
implies, by Zariski's connection theorem, that for every `H`, `H ∩ X` is connected (although not necessarily
irreducible). One can moreover proceed in the reverse direction, proving this latter result by a Lefschetz-type
technique, and deducing Bertini's theorem, reducing to the case where `X` is normal, and using the following result: for
`H` "sufficiently general", `X ∩ H` is also normal. This suggests:

**Conjecture 2.5**[^N.D.E-XIII-7].

<!-- label: XIII.2.5 -->

<!-- original page 181 -->

Let `A` be a complete noetherian normal local ring. Show that there exists a nonzero `f ∈ 𝔯(A)` such that
`Y' = X' ∩ V(f) = Y − {a}` (where `Y = Spec(A/fA)`) is normal (hence irreducible by 2.1 if `dim A ⩾ 3`).

To do things properly, one would have to show that, in a suitable sense, there exist even "many" elements `f` having the
property in question, for example that one can choose `f` in an arbitrary power of the maximal ideal. Using Serre's
normality criterion and the remark made above for Serre's property (`S₂`), one sees that one would have an affirmative
answer to 2.5 if one had one to:

**Conjecture 2.6**[^N.D.E-XIII-8].

<!-- label: XIII.2.6 -->

Let `A` be a complete noetherian local ring, `U` an open part of its spectrum `X`, `F` a finite part of `X' = X − {a}`.
Suppose `U` is regular. Prove that there exists `f ∈ 𝔯(A)` such that `V(f) ∩ U` is regular, and `V(f) ∩ F = ∅`.

For a "local Bertini"-type result, see Chow [2].

## 3. Problems related to `π₁`

<!-- label: XIII.3 -->

Here again, one has numerous questions, suggested by the global results or by the transcendental results.

**Conjecture 3.1**[^N.D.E-XIII-9].

<!-- label: XIII.3.1 -->

Let `A` be a complete noetherian local ring with algebraically closed residue field, `X = Spec(A)`, `X' = X − {a}`, `a`
the closed point. Suppose the irreducible components of `X` are of dimension `⩾ 2`, and `X'` connected.

(i) Prove that `π₁(X')` is topologically finitely generated.

(ii) If `p` is the characteristic exponent of the residue field `k` of `A`, prove that the largest topological quotient
group of `π₁(X')` that is "of order prime to `p`" is finitely presented.

<!-- original page 182 -->

For part (i), using the theory of descent SGA 1 IX 5.2 and theorem 2.4, one is reduced to the case where `A` is normal
of dimension 2. In this case, a systematic method for studying the fundamental group of `X'`, inaugurated by Mumford [5]
in the transcendental setting, consists in desingularizing `X`, i.e. in considering a projective birational morphism
`Z → X`, with `Z` integral regular, inducing an isomorphism `Z' = Z|_{X'} → X'`; it is plausible that such a `Z` always
exists, this is in any case what Abhyankar's method [1] demonstrates in the case of "equal characteristics"[^XIII-3-1].
Let `C` be the fiber of the closed point of `X` by `Z → X`; it is an algebraic curve over the residue field `k`,
connected by virtue of the connection theorem. The solution of 3.1 then seems linked to:

**Problem 3.2.**

<!-- label: XIII.3.2 -->

With the preceding notation, put `π₁(X')` in relation with the topological invariants of `C`, in particular its
fundamental group, (in order to bring out the topological finite generation of `π₁(X')`, by using for instance SGA 1,
theorem X 2.6).

Another method would be to consider `A` as a finite algebra over a complete regular local ring `B` of dimension 2,
ramified along a curve `C` contained in `Spec(B) = Y`. One is thus led to:

**Problem 3.3.**

<!-- label: XIII.3.3 -->

Let `A` be a complete regular local ring of dimension 2, with algebraically closed residue field `k`, `X` its spectrum,
`C` a closed part of `X` of dimension 1. Define local invariants of the embedded curve `C`, having a sense independent
of the residual characteristic, and the knowledge of which permits one to calculate the

<!-- original page 144 -->

fundamental group of `X − C` by generators and relations when `k` is of characteristic zero. Prove that when `k` is of
characteristic `p > 0`, the "tame" fundamental group of `X − C` is a quotient of the preceding one, and that the two
fundamental groups (in characteristic 0, and in characteristic `p > 0`) have the same maximal quotient of order prime to
`p`.

Of course, 3.3 shows us that in 3.1, there is also occasion to replace `X'` by a scheme of the form `X − Y`, where `Y`
is a closed part of `X` that is of codimension `⩾ 2` in every component of `X` containing it.

<!-- original page 183 -->

When one abandons this restriction on `Y`, there must still exist an analogous finiteness result, on condition of
imposing "tame"-type restrictions on the ramification at the maximal points of the irreducible components of `Y` that
are of codimension 1.

**Problem 3.4.**

<!-- label: XIII.3.4 -->

Let `A` be a complete noetherian local ring of dimension 2, with algebraically closed residue field. Let again
`X = Spec(A)`, `X' = X − {a}`. Find particular structural properties of `π₁(X')` in the case where `A` is a complete
intersection.

A satisfactory solution of this problem would perhaps permit one to resolve the following old problem:

**Conjecture 3.5**[^N.D.E-XIII-10].

<!-- label: XIII.3.5 -->

Find an irreducible curve in `𝐏³_k` (`k` algebraically closed field), preferably non-singular, that is not
set-theoretically the intersection of two hypersurfaces.

(Kneser [4] shows that one can always obtain it as the intersection of three hypersurfaces).

## 4. Problems related to higher `πᵢ`: local and global Lefschetz theorems for complex analytic spaces[^N.D.E-XIII-11]

<!-- label: XIII.4 -->

Let `X` be a scheme locally of finite type over the field of complex numbers `ℂ`; one can associate to it an analytic
space `X_h` over `ℂ`, whence homotopy and homology invariants `πᵢ(X_h)`, `Hᵢ(X_h)`, `Hⁱ(X_h)` etc. One knows moreover
that `X` is connected if and only if `X_h` is, hence one has a bijection

```text
π₀(X_h) → π₀(X).
```

Likewise, since every étale covering `X'` of `X` defines an étale covering `X'_h`

<!-- original page 184 -->

of `X_h`, one has a canonical homomorphism

```text
π₁(X_h) → π₁(X),
```

which one knows, using a theorem of Grauert-Remmert, identifies the second group with the completion of the first for
the topology of subgroups of finite index (which simply expresses the fact that `X' ↦ X'_h` is an equivalence of the
category of étale coverings of `X` with the category of finite étale coverings of `X_h`). It follows that the results of
this seminar (by purely algebraic means) on `π₀(X)` and `π₁(X)` imply results for `π₀(X_h)` and `π₁(X_h)` (which are of
transcendental nature). Moreover, if `X` is proper, the well-known exact sequence `0 → ℤ → ℂ → ℂ* → 0` allows one to
show that the Néron-Severi group of `X` (the quotient of its Picard group by the connected component of the identity) is
isomorphic to a subgroup of `H²(X_h, ℤ)`; in the non-singular Kähler case, it is the subgroup denoted
`H^{(1,1)}(X_h, ℤ)` (classes of type `(1, 1)`):

```text
Pic(X) / Pic⁰(X) ⊂ H²(X, ℤ).
```

Consequently, the information we have obtained on Picard groups implies information, very partial it is true, about the
groups `H²(X_h, ℤ)`. It is tempting to complete all these fragmentary results by conjectures.

Very precise indications, going in the same direction as those just mentioned, are furnished by a classical theorem of
Lefschetz [7]. It asserts that if `X` is a non-singular irreducible projective analytic space of dimension `n`, and if
`Y` is a non-singular hyperplane section, then the injection

```text
Y_{n−1} → X_n
```

induces a homomorphism

<!-- original page 185 -->

```text
πᵢ(Y_{n−1}) → πᵢ(X_n)
```

which is an isomorphism for `i ⩽ n − 2`, an epimorphism for `i = n − 1`. The analogous statement follows for the
homomorphisms

```text
Hᵢ(Y_{n−1}) → Hᵢ(X_n)
```

on homology (integral, to fix ideas), while in cohomology,

```text
Hⁱ(X_n) → Hⁱ(Y_{n−1})
```

is an isomorphism in dimension `i ⩽ n − 2`, a monomorphism in dimension `i = n − 1`. We have obtained variants of these
results in the framework of schemes, for `π₀`, `π₁`, `Pic`, valid moreover without non-singularity hypotheses to a large
extent, cf. Exp. XII. Moreover, in the elimination of non-singularity hypotheses, we have used in an essential way
"local" variants of these global Lefschetz theorems. All this suggests the following problems, which doubtless will have
to be attacked simultaneously[^XIII-4-1].

**Problem 4.1.**

<!-- label: XIII.4.1 -->

Let `X` be an analytic space, `Y` a closed analytic part of `X` (or simply a closed part?[^N.D.E-XIII-12]) such that for
every `x ∈ Y`, the local ring `𝒪_{X,x}` is a complete intersection. Let `n` be the complex codimension of `Y` in `X`. Is
the canonical homomorphism

```text
πᵢ(X − Y) → πᵢ(X)
```

<!-- original page 146 -->

an isomorphism for `i ⩽ n − 2`, and an epimorphism for `i = n − 1`?

In this problem and the following ones, one supposes evidently implicitly a base-point chosen to define the homotopy
groups. To state the next problem, one must define, for an analytic space `X` (more generally, for a locally
path-connected space) and `x ∈ X`, local invariants `Π^x_i(X)`[^XIII-4-2].

<!-- original page 186 -->

To do this, one chooses a non-constant map `f` from the interval `[0, 1]` into `X`, such that `f(0) = x` and `f(t) ≠ x`
for `t ≠ 0` (such maps exist if `x` is not an isolated point). Then for every neighborhood `U` of `x`, there exists an
`ε > 0` such that `0 < t < ε` implies `f(t) ∈ U`, and the homotopy groups `πᵢ(U − x, f(t))` are essentially independent
of `t` (they are, for varying `t`, related by a transitive system of isomorphisms); one can denote them `πᵢ(U − x, f)`.
One then sets

```text
Π^x_i(X) = lim_{← U} πᵢ₋₁(U − x, f),
```

the inverse limit being taken over the system of open neighborhoods `U` of `x`. Strictly speaking, this limit depends on
`f`, and should be denoted `Π^x_i(X, f)`, but one verifies that for varying `f`, these groups are isomorphic to each
other[^XIII-4-3]; more precisely, they form a local system on the space of paths of the type envisaged issuing from `x`.
These invariants are the homotopical version of the local cohomology invariants `H^x_i(F)` for a sheaf `F` on `X`,
introduced in I, and should play the role of relative local homotopy groups of `X` modulo `X − x`. Their vanishing for
`i ⩽ n` and for every `x ∈ Y`, where `Y` is a closed part of `X` of topological dimension `⩽ d`, should entail that the
homomorphisms

```text
πᵢ(X − Y) → πᵢ(X)
```

are bijective for `i < n − d`, and surjective for `i = n − d`[^XIII-4-4]. From this point of view, 4.1 would imply (for
`Y` reduced to a point) a conjecture of purely local nature, expressing itself by

```text
Π^x_i(X) = 0   for i ⩽ n − 1
```

when `X` is a complete intersection of dimension `n` at `x`.

<!-- original page 147 -->

As an example of local invariants `Π^x_i(X)`, note that if `x` is a non-singular point of `X` of complex dimension `n`,
then

<!-- original page 187 -->

```text
Π^x_i(X) = πᵢ₋₁(S^{2n−1}),
```

where `S^{2n−1}` denotes the sphere of dimension `2n − 1`. In particular in this case `Π^x_i(X) = 0` for `i ⩽ 2n − 1`,
which corresponds to the fact that if from a topological manifold `X` one removes a closed part `Y` of codimension
`⩾ m`, then `πᵢ(X − Y) → πᵢ(X)` is an isomorphism for `i ⩽ m − 2` and an epimorphism for `i = m − 1`.

This being said:

**Problem 4.2.**

<!-- label: XIII.4.2 -->

Let `X` be an analytic space, `x ∈ X`, `t` a section of `𝒪_X` vanishing at `x`, `Y` the set of zeros of `t`. Suppose the
following conditions satisfied:

a) `t` is regular at `x` (i.e. not a zero-divisor at `x`, a hypothesis perhaps superfluous, moreover).

b) At the points `x'` of `X − Y` near `x`, `𝒪_{X,x'}` is a complete intersection (a hypothesis which should be
replaceable by the following more general one if 4.1 is true: for `x'` as above, `Π^{x'}_i(X) = 0` for `i ⩽ n − 1`).

c) At the points `y` of `Y − {x}` near `x`, one has

```text
prof 𝒪_{X,y} ⩾ n
```

(it suffices for example that one have `prof 𝒪_{X,x} ⩾ n`).

Under these conditions, is the canonical homomorphism

```text
Π^x_i(Y) → Π^x_i(X)
```

an isomorphism for `i ⩽ n − 2`, an epimorphism for `i = n − 1`?

Here finally is a global variant of 4.2, which should be deduced from it by consideration of the projecting cone at its
origin, and which would generalize the classical Lefschetz theorems:

**Problem 4.3.**

<!-- label: XIII.4.3 -->

<!-- original page 188 -->

Let `X` be a projective analytic space, equipped with an ample invertible Module `L`, `t` a section of `L`, `Y` the set
of zeros of `t`. Suppose:

a) `t` is a regular section (hypothesis perhaps superfluous).

b) For every `x ∈ X − Y`, `𝒪_{X,x}` is a complete intersection (should be replaceable by `Π^x_i(X) = 0` for
`i ⩽ n − 1`).

c) For every `x ∈ Y`, `prof 𝒪_{X,x} ⩾ n`.

Under these conditions, is the homomorphism

```text
πᵢ(Y) → πᵢ(X)
```

an isomorphism for `i ⩽ n − 2`, an epimorphism for `i = n − 1`?

<!-- original page 148 -->

We shall leave it to the reader to state analogous conjectures of cohomological nature[^XIII-4-5], the hypotheses and
conclusions then bearing on local cohomological invariants (with coefficients in a given group). In any case, the key
result seems bound to be 4.2, when hypothesis b) there is taken in the form just discussed, — whether one places oneself
from the point of view of homology, or of homotopy.

We have stated these conjectures in the transcendental setting, in the hope of interesting topologists in them and
convincing them that "Lefschetz"-type questions are far from being closed. Of course, now that we are about to dispose
of a good theory of cohomology of schemes (with finite coefficients), thanks to the recent work of M. Artin, the same
questions arise in the framework of schemes, and it is difficult to doubt that they will not receive a positive answer,
in the near future[^XIII-4-6].

## 5. Problems related to local Picard groups

<!-- label: XIII.5 -->

<!-- original page 189 -->

A first fundamental problem, signaled for the first time by Mumford [5] in a particular case, is the following. Let `A`
be a complete local ring with residue field `k`, `X = Spec(A)`, `U = Spec(A) − {a}`, where `a` is the maximal ideal of
`A`, i.e. the closed point of `Spec(A)`. One proposes to construct a strict projective system `G` of locally algebraic
groups `Gᵢ` over `k`, and a natural isomorphism

```text
Pic(U) ≃ G(k)
```

<!-- label: eq:XIII.5.plus -->

where one of course sets `G(k) = lim_{← } Gᵢ(k)`. Heuristically, one proposes to "put an algebraic group structure" (or,
at least, pro-algebraic, in a suitable sense) on the group `Pic(U)`.

It is evident that as it stands, the problem is not precise enough, for the datum of an isomorphism (+) is far from
characterizing the pro-object `G`. If `A` contains a subfield, still denoted `k`, that is a field of representatives,
one can make the problem precise by requiring that for a variable extension `k'` of `k`, one have an isomorphism,
functorial in `k'`:

```text
Pic(U') ≃ G(k')
```

<!-- label: eq:XIII.5.plus-prime -->

where `U'` is the open part analogous to `U` in `Spec(A')`, `A' = A ⊗̂_k k'`. One can proceed in an analogous way even
if `A` has no field of representatives, provided that `k` is perfect, which then permits one to construct functorially
an `A'` "by residual extension `k'/k`". Moreover, when `A` admits a field of representatives, the algebraic structure
that one will find on `Pic(U)` will depend essentially on the choice of this field of representatives (as one sees
already on the projecting cone of an elliptic curve); it seems therefore that one must start from a "pro-algebraic ring
over `k`" in the sense of Greenberg [3], in order to arrive at

<!-- original page 149 -->

defining the pro-object `G`. It is moreover conceivable that in the case where there is no given field of
representatives, one finds only a projective system of quasi-algebraic groups in the sense of Serre, or rather
quasi-locally-algebraic groups

<!-- original page 190 -->

(the groups `Gᵢ` obtained will not in general be of finite type over `k`, but only locally of finite type over `k`). It
is even possible that one will find in general only a still weaker structure on `Pic(U)`, of the kind encountered by
Néron [6] in his theory of degeneration of abelian varieties defined over local fields.

A method for attacking the problem, also introduced by Mumford, consists in desingularizing `X`, i.e. in considering a
projective birational morphism `Y → X` with `Y` regular. When `U` is regular (i.e. `a` is an isolated singular point),
one can often find `Y` in such a way that `Y|_U = V → U` is an isomorphism. In this case, one will therefore have

```text
Pic(U) ≃ Pic(V) ≃ Pic(Y) / Im ℤ^I,
```

where `I` is the set of irreducible components of the fiber `Y_a` (each of these defining an element of `Pic(Y)`, being
a locally principal divisor, thanks to `Y` regular). On the other hand, using the technique of formal geometry EGA III 4
and 5, notably the existence theorem, one finds

```text
Pic(Y) ≃ lim_{← } Pic(Y_n),
```

where `Y_n = Y ⊗_A A_n`, `A_n = A/𝔪^{n+1}`. When `A` admits a field of representatives `k`, one has at one's disposal
the theory of Picard schemes of the projective schemes `Y_n` over `k`, hence one has

```text
Pic(Y_n) ≃ Pic_{Y_n/k}(k).
```

This therefore furnishes a construction of a projective system of locally algebraic groups `Pic_{Y_n/k} / Im ℤ^I`, which
is the desired system[^N.D.E-XIII-13]. In the case envisaged here, one can moreover see (using that `a` is an isolated
singular point) that the connected components of the universal-image subgroups in this projective system form an
essentially constant projective system, so that in this case one finds a locally algebraic group `G` as solution of the
problem. If one supposes furthermore `A` normal of dimension 2, then a remark of Mumford (stating that the intersection
matrix of the components of `Y_a` in `X` is negative definite[^N.D.E-XIII-14]) implies that `G` is even

<!-- original page 191 -->

<!-- original page 150 -->

an algebraic group, i.e. of finite type over `k` (the number of its connected components being moreover equal to the
determinant of the intersection matrix envisaged a moment ago).

If on the contrary `a` is not an isolated singularity, one convinces oneself by examples (with `A` of dimension 2) that
one finds a projective system of algebraic groups, not reducing to a single algebraic group.

Once one had at one's disposal a good notion of "local Picard scheme", there would be occasion to strengthen the notion
of parafactoriality, by saying that `A` is "geometrically parafactorial" when not only `A` and even `Â` are
parafactorial, but the local Picard scheme `G(Â)` is the trivial group (which is stronger, when the residue field is not
algebraically closed, than saying that `G` has no other rational point over `k` than the unit). One realizes the
necessity of a strengthened notion of parafactoriality by recalling that there exist complete normal local rings of
dimension 2 that are factorial, but that admit finite étale algebras that are not[^N.D.E-XIII-15]. A "geometrically
factorial" local ring would then be a normal ring `A` such that all the localizations of dimension `⩾ 2` are
geometrically parafactorial, or better, such that the localizations of `Â` are parafactorial[^XIII-5-1]. Of course, it
would be interesting to find a "good" definition of these notions, independent of the theory, still to be done, of local
Picard schemes[^N.D.E-XIII-16].

It is in any case plausible that one will need these notions if one wishes to obtain statements of the following type:
Let `A` be a "good ring" (for example, an algebra of finite type over `ℤ`, or over a complete local ring, for example
over a field). Let `U` be the set of `x ∈ X = Spec(A)` such that `𝒪_{X,x}` is "geometrically factorial"; is `U` open? Or
again: Let `f : X → Y` be a flat morphism of finite type with `Y` locally noetherian, let `U` be the set of `x ∈ X` such
that `𝒪_{X_{f(x)},x}` is "geometrically factorial"; is `U` open, at least under sympathetic supplementary conditions on
`f`? I doubt that with the usual notion of factorial ring, there exist true statements of this type.

<!-- original page 192 -->

We have raised here, in a particular case, the question of the study of geometric properties of "variable" local rings,
for example the `𝒪_{X,x}` as `x` ranges over a prescheme `X`. When `X` is a scheme of finite type over a field, for
example, one knows[^N.D.E-XIII-17] that there exists on `X` a projective system of finite algebras `P_n^{X/k}` (obtained
by completing `X ×_k X` along the diagonal), whose fiber at every point `x ∈ X` rational over `k` is isomorphic to the
projective system of `𝒪_{X,x}/𝔪_X^{n+1}`. It is then natural to relate the study of the completions of the local rings
`𝒪_{X,x}`, for varying `x`, to that of the "algebraic family of complete local rings" given by the `P_n`, by noting that
for every `x ∈ X` (rational over `k` or not), one obtains a complete local ring

```text
P_∞(x) = lim_{← } P_n(x)
```

(where `P_n(x)` = reduced fiber `P_n ⊗_{𝒪_{X,x}} k(x)`). A particular interest will attach for example to the complete
ring thus associated to the generic point, and one will expect that its algebraic-geometric properties (expressing
themselves for instance by its local Picard groups, or homotopy groups, or homology groups), will be essentially those
of the completions `𝒪̂_{X,x}` for `x` in a suitable dense open `U`.

One can, in general, propose to make the simultaneous study of the complete local rings obtained in this way from an
adic projective system `(P_n)` of finite algebras over a given scheme `X`. It is plausible that one will find, subject
to certain regularity conditions (such as the flatness of the `P_n`), that the local homotopy groups arise from a
projective system of finite group schemes over `X`,

<!-- original page 193 -->

and that one will have analogous results for the local Picard groups. As regards the latter, a first interesting case
that deserves to be investigated is that where one starts from an algebraic surface `X` having singular curves, and one
proposes to study the local Picard schemes at variable points on them, in terms of a suitable pro-group scheme defined
on the singular locus.

## 6. Comments[^XIII-6-1]

<!-- label: XIII.6 -->

<!-- original page 194 -->

The point of view of "étale cohomology" of schemes and recent progress in this theory lead us to make precise and at the
same time to broaden certain of the problems posed. For the notion of "topology" and of "étale topology of a scheme", I
refer to M. Artin, *Grothendieck Topologies*, Harvard University 1962 (mimeographed notes)[^XIII-6-2].

This theory, by a finer notion of localization than that furnished by the traditional "Zariski topology", leads one to
attach a particular interest to *strictly local rings*, i.e. henselian local rings with separably closed residue field.
For every local ring `A` with residue field `k`, and every separable closure `k'` of `k`, one can find a local
homomorphism of `A` into a strictly local ring `A'`, the strictly local closure of `A`, with residue field `k'`, having
an obvious universal property. `A'` is henselian, flat over `A`, and `A' ⊗_A k ≃ k'`; it is noetherian if and only if
`A` is. (Cf. loc. cit. Chap. III, section 4)[^XIII-6-3].

<!-- original page 152 -->

If `X` is a prescheme, and `x` a point of `X`, `x'` a point above `x`, the spectrum of a separable closure `k'` of
`k = k(x)`, one is led to define the *strictly local ring of `X` at `x'`*, `𝒪'_{X,x'}`, as the strictly local closure of
the usual local ring `𝒪_{X,x}`, relatively to the residual extension `k'/k`. It is the strictly local rings at the
"geometric" points of `X` that, from the point of view of the étale topology, are supposed to reflect the local
properties of the prescheme `X`. They also play, in many respects, the role that one used to assign to the completions
of the local rings of `X` (say, at the points with algebraically closed residue field), while remaining "closer" to `X`
and permitting an easier passage to "neighboring points".

It is then in order to take up again a good number of questions, that one generally poses for complete local rings
(eventually restricted to having an algebraically closed residue field), for noetherian henselian local rings (resp.

<!-- original page 195 -->

noetherian strictly local rings). Thus the topological problems raised in nos 2 and 3 are posed more generally for
strictly local rings. One can moreover state conjecturally, for "good" strictly local rings, certain properties of
simple connectedness and acyclicity for the geometric fibers of the canonical morphism `Spec(Â) → Spec(A)`, which would
show that for many "topological"-nature properties, it amounts to the same to prove them for the ring `A`, or for its
completion `Â`. Certain results already obtained in this direction[^XIII-6-4] allow one to hope that one will soon have
at one's disposal complete results in this direction.

The notion of étale localization furnishes a definition that seems reasonable of the notion of "geometrically
parafactorial" or "geometrically factorial" local ring (the need for which was indicated in no 5, p. 150): one will call
thus a local ring whose strictly local closure is parafactorial, resp. factorial. Hypotheses of this nature introduce
themselves effectively in a natural way in the study of the étale cohomology of preschemes[^N.D.E-XIII-18]. Thus, if `X`
is a locally noetherian prescheme whose strictly local rings are factorial (i.e. whose ordinary local rings are
"geometrically factorial"), one shows that the `Hⁱ(X_ét, 𝐆_m)`

<!-- original page 153 -->

are torsion groups for `i ⩾ 2` (which allows one sometimes to express these groups in terms of cohomology groups with
coefficients in the groups `μ_n` of `n`-th roots of unity), and if `X` is integral with fraction field `K`, the natural
homomorphism `H²(X_ét, 𝐆_m) → H²(K, 𝐆_m) = Br(K)` is injective[^N.D.E-XIII-19]; examples show that these conclusions can
fail, even for `X` local, if one supposes only `X` factorial instead of geometrically factorial[^XIII-6-5].

Concerning the problems of local and global Lefschetz type raised in 3.4[^TRANSLATOR-NOTE-XIII-1], and their analogues
in scheme theory, the homological version of these questions has been considerably clarified, all resulting formally
from three general theorems: one concerning the cohomological dimension of certain affine schemes (resp. of Stein
spaces), such as affine schemes `X` of finite type over an algebraically closed field: their cohomological dimension is
`⩽ dim X` ("affine Lefschetz theorem")[^XIII-6-6];

<!-- original page 196 -->

the other being a duality theorem for the cohomology (with discrete coefficients) of a projective morphism[^XIII-6-7],
and finally the last a local duality theorem of analogous nature[^XIII-6-8]. In Algebraic Geometry, only this last is
not proved at the time of writing these lines (it is however proved in characteristic 0, using Hironaka's resolution of
singularities). Moreover, in the transcendental setting, one disposes from now on of global and local duality, recently
demonstrated by Verdier[^N.D.E-XIII-20]. Let us limit ourselves to indicating that in the statement of the homological
versions of problems 4.2 and 4.3 (which from now on deserve the name of conjectures), the conditions a) and c) "at
infinity" are certainly superfluous; only the local cohomological structure of `X − Y` is important, which one will
suppose for example locally a complete intersection of dimension `⩾ n`. Moreover, in 4.3 say, the fact that `Y` is a
hyperplane section should not play a role, and should be replaceable by the sole hypothesis that `X` is compact and
`X − Y` is Stein (i.e. in the case of Algebraic Geometry, `X` is proper over `k` and `X − Y` affine; as we said, the
homological version of this conjecture is demonstrated for algebraic spaces over the field `ℂ`)[^XIII-6-9].

<!-- TRANSLATOR NOTE: The source says "3.4" but the problems referenced are those of section 4 (4.2, 4.3). The reading
"section 4" (or "no 4") is consistent with the surrounding discussion of Lefschetz-type problems and the conjectures
A–D below; we have kept the source's "3.4" literally and flagged it. -->

In the definition (p. 146) of the `Π^x_i(X)`, one must suppose `i ⩾ 2`. For `i = 0, 1`, there is no reasonable
definition of the `Π^x_i(X)`; one should replace them by `H^x_0(X)` and `H^x_1(X)`, defined respectively as the cokernel
and the kernel in the natural homomorphism

```text
lim_{← } H⁰(U − {x}, ℤ) → lim_{← } H⁰(U, ℤ).
```

At a pinch, and for convenience of formulation, one can set `Π^x_i(X) = H^x_i(X)` for `i ⩽ 1`; otherwise one must
complete the subsequent assertions concerning the `Π^x_i` by the corresponding assertions for `H^x_0`, `H^x_1`. If `x`
is an isolated point of `X`, it is appropriate to set `Π^x_i(X) = 0` for `i ≠ 0`, `Π^x_0(X) = H^x_0(X) = ℤ`.

<!-- original page 197 -->

The assertion that the `Π^x_i(U, f)` be isomorphic to each other is true only when `X` is not disconnected by `x` in a
neighborhood of `x`, i.e. if `Π^x_i(X) = 0` for `i = 0, 1`. In the general case `Π^x_i(X)` can designate only a family
of groups, not necessarily isomorphic to each other; however the expression `Π^x_i(X) = 0` retains an obvious sense.

Page 146, where I predict that the vanishing of the local homotopy invariants `Π^x_i(X)` for `x ∈ Y`, `i ⩽ n`, should
entail the bijectivity of `πᵢ(X − Y) → πᵢ(X)` for `i < n − d`, the surjectivity for `i = n − d`, it is appropriate to be
cautious, failing to be able to dispose in the present context (as in Algebraic Geometry) of "general" points at which
the local conditions will also have to apply. It will doubtless be necessary, for this reason, to call upon *relative
local homotopy invariants*

```text
Π^Y_i(X, f) = Π^Y_i(X, x) = lim_{← U} πᵢ₋₁(U − U ∩ Y, f(t))   for i ⩾ 2,
```

(and an *ad hoc* definition as above for `i = 0, 1`), where `Y` is a closed part of `X`; or to make up for the absence
of general points by expressing the hypotheses on `X` in terms of properties of topological nature (for the étale
topology) of the spectra of the local rings of `X`, which allows one to recover general points. The same reservation
applies to the generalization of conjectures 4.2 and 4.3 to the case where `X − Y` is not assumed locally a complete
intersection, a generalization suggested in the statement of conditions b) of these conjectures.

To formulate the expurgated versions of conjectures 4.2 and 4.3 suggested by the results to which we alluded above, it
is appropriate to pose:

<!-- original page 155 -->

**Definition 1.**

<!-- label: XIII.6.def1 -->

Let `X` be a topological space, `Y` a locally closed part of `X`, and `n` an integer. One says that `X` is of
*homotopical depth `⩾ n` along `Y`*, and one writes `prof htp_Y(X) ⩾ n`, if for every `x ∈ Y`, one has `Π^Y_i(X, x) = 0`
for `i < n`.

<!-- original page 198 -->

It should be equivalent to say that for every open `X'` of `X`, and every `x ∈ X' ∩ U = U'` (where `U = X − Y`), the
canonical homomorphism

```text
πᵢ(U', x) → πᵢ(X', x)
```

is an isomorphism for `i < n − 1`, a monomorphism for `i = n − 1`[^N.D.E-XIII-21].

**Definition 2.**

<!-- label: XIII.6.def2 -->

Let `X` be a complex analytic space, `n` an integer; one says that the *rectified homotopical depth of `X`* is
`n`[^XIII-6-10], if for every locally closed analytic part `Y` of `X`, one has

```text
prof htp_Y(X) ⩾ n − dim Y
```

<!-- label: eq:XIII.6.x -->

(where, of course, `dim Y` denotes the complex dimension of `Y`).

It should be equivalent to say that for every irreducible analytic part `Y` locally closed in `X`, there exists a closed
analytic part `Z` of `Y`, of dimension `< dim Y`, such that the relation (x) is valid for `Y − Z` in place of `Y`. This
would permit one for example in definition 2 to confine oneself to the case where `Y` is non-singular[^N.D.E-XIII-22].

The following conjecture, of purely topological nature, is in the nature of a "local Hurewicz theorem".

**Conjecture A** ("local Hurewicz theorem"[^N.D.E-XIII-23]).

<!-- label: XIII.6.A -->

Let `X` be a topological space, `Y` a locally closed part, subject if necessary to "smoothness"-type conditions such as
local triangulability of the pair `(X, Y)`, `n` an integer `⩾ 3`. For one to have `prof htp_Y(X) ⩾ n`, it is necessary
and sufficient that one have

<!-- original page 199 -->

```text
H^Y_i(ℤ_X) = 0   for i < n
```

<!-- original page 156 -->

(one then says that `X` is of *cohomological depth `⩾ n` along `Y`*), and that the local fundamental groups

```text
Π^Y_2(X, x) = lim_{← U ∋ x} π₁(U − U ∩ Y)
```

be zero (one then says that `X` is "pure along `Y`").

One notes that if `X` is an analytic space, `Y` an analytic subspace, and if `X` is pure along `Y`, then for every
`x ∈ Y`, the local ring `𝒪_{X,x}`, as well as its localizations with respect to prime ideals containing the ideal
defining the germ `Y` at `x` (i.e. in the inverse image `Y_x` of `Y` by `Spec(𝒪_{X,x}) = X_x → X`), are pure in the
sense of Exp. X; it seems plausible that the converse is also true. Analogous remarks hold for cohomological depth, it
being understood that one works with the étale topology on the `Spec(𝒪_{X,x})`.

Conjecture 4.1 then generalizes to:

**Conjecture B** ("Purity"[^N.D.E-XIII-24]).

<!-- label: XIII.6.B -->

Let `E` be an analytic space, `X` an analytic part of `E`. Suppose that `E` is non-singular of dimension `N` at `x ∈ X`,
and that `X` can be described by `p` analytic equations in a neighborhood of every point. Then the rectified homotopical
depth of `X` is `⩾ N − p`.

In particular, a local complete intersection of dimension `n` at every point would be of rectified homotopical depth
`⩾ n`, which is none other than conjecture 4.1.

Conjectures 4.2 and 4.3 generalize respectively to:

**Conjecture C** ("Local Lefschetz"[^N.D.E-XIII-25]).

<!-- label: XIII.6.C -->

Let `X` be an analytic space, `Y` a closed analytic part, `x` a point of `Y`; suppose that `X − Y` is Stein in a
neighborhood of `x` (for example `Y` defined by an equation at `x`), and that `X − Y` is of rectified homotopical depth
`⩾ n` in a neighborhood of `x` (for example, is at every point of `X − Y` near `x` a complete intersection of dimension
`⩾ n`, cf. conjecture B). Then the canonical homomorphism

```text
Π^x_i(Y) → Π^x_i(X)
```

is an isomorphism for `i < n − 1`, an epimorphism for `i = n − 1`.

<!-- original page 200 -->

**Conjecture D** ("Global Lefschetz"[^N.D.E-XIII-26]).

<!-- label: XIII.6.D -->

Let `X` be a compact analytic space, `Y` an analytic subspace of `X` such that `U = X − Y` is Stein, and is of

<!-- original page 157 -->

rectified homotopical depth `⩾ n` (for example a complete intersection of dimension `⩾ n` at every point). Then the
canonical homomorphism

```text
πᵢ(Y) → πᵢ(X)
```

is an isomorphism for `i < n − 1`, an epimorphism for `i = n − 1`.

**Remark.**

<!-- label: XIII.6.remark -->

When, in statements C and D, one replaces the hypothesis that `X − Y` is Stein by the hypothesis that `X − Y` is the
union of `c + 1` Stein opens (which will play the role of a hypothesis of topological "concavity"), the conclusions must
be modified simply by replacing `n` there by `n − c`[^N.D.E-XIII-27].

Let us make explicit, finally, in the "global case" D, the conjecture concerning the fundamental group (obtained by
taking `n = 3`):

**Conjecture D'** (Global Lefschetz for the fundamental group[^N.D.E-XIII-29]).

<!-- label: XIII.6.D-prime -->

Let `X` be a compact analytic space over the field of complex numbers, `Y` a closed analytic part such that `U = X − Y`
is Stein. Suppose moreover the following conditions satisfied:

(i) For every `x ∈ U`, the local fundamental group `Π^x_2(X, x)` is zero (i.e. `X` is "pure at `x`"), or only the local
ring `𝒪_{X,x}` is pure.

(ii) The local rings of points of `U` are "connected in dimension `⩾ 2`".

(iii) The local rings of points of `U` are of dimension `⩾ 3`.

Under these conditions, for every `x ∈ Y`, the homomorphism

```text
π₁(Y, x) → π₁(X, x)
```

<!-- original page 201 -->

is an isomorphism (and `π₂(Y, x) → π₂(X, x)` an epimorphism).

One notes that the local conditions (i) (ii) (iii) on `U` are satisfied if `U` is locally a complete intersection of
dimension `⩾ 3`. From the point of view of Algebraic Geometry, (when `U` comes from a scheme, still denoted `U`), the
conditions (i) to (iii) correspond to hypotheses on the local invariants `Π^x_i(U)`, namely `Π^x_i(U) = 0` for
`i < 3 − deg tr k(x)/k`, for points `x` such that one has respectively `deg tr k(x)/k = 0, 1, 2`. The global condition
on `U` (`U` Stein) will be satisfied if `X` is projective and `Y` a hyperplane section.

<!-- original page 158 -->

## Bibliography

<!-- label: XIII.bibliography -->

<!-- original page 202 -->

1. S. Abhyankar — "Local uniformisation on algebraic surfaces over ground fields of characteristics `p ≠ 0`", *Annals of
    Math.* **63** (1956), p. 491–526.
1. W.L. Chow — "On the theorem of Bertini for local domains", *Proc. Nat. Acad. Sci. U.S.A.* **44** (1958), p. 580–584.
1. M. Greenberg — "Schemata over local rings", *Annals of Math.* **73** (1961), p. 624–648.
1. M. Kneser — "Über die Darstellung algebraischer Raumkurven als Durchschnitte von Flächen", *Archiv der Math.* **XI**
    (1960), p. 157–158.
1. D. Mumford — "The topology of normal singularities of an algebraic surface, and a criterion for simplicity", *Publ.
    Math. Inst. Hautes Études Sci.* **9** (1961), p. 5–22.
1. A. Néron — "Modèles minimaux des variétés abéliennes sur les corps locaux et globaux", *Publ. Math. Inst. Hautes
    Études Sci.* **21** (1964), p. 5–128.
1. A.H. Wallace — *Homology Theory of algebraic Varieties*, Pergamon Press, 1958.
1. S. Abhyankar — "Resolution of singularities of arithmetical surfaces", in *Arithmetical Algebraic Geometry*, Harper
    and Row, New York, 1965, p. 111–152.
1. [HL] H.A. Hamm & Lê Dũng Tráng — "Rectified homotopical depth and Grothendieck conjectures", in *The Grothendieck
    Festschrift, Vol. II*, Progr. Math., vol. **87**, Birkhäuser Boston, 1990, p. 311–351.

## Footnotes

## Translation ledger delta

| French                                               | English                                        | Note                                                                                                                                            |
| ---------------------------------------------------- | ---------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| problèmes et conjectures                             | problems and conjectures                       | Title-level. Per task spec.                                                                                                                     |
| relations entre résultats globaux et locaux          | relations between global and local results     | Section 1 title.                                                                                                                                |
| problèmes affines liés à la dualité                  | affine problems related to duality             | Section 1 title.                                                                                                                                |
| théorèmes de Bertini locaux                          | local Bertini theorems                         | Per task spec.                                                                                                                                  |
| théorèmes de Lefschetz cohomologiques / homotopiques | cohomological / homotopical Lefschetz theorems | Per task spec.                                                                                                                                  |
| théorèmes de Lefschetz locaux et globaux             | local and global Lefschetz theorems            | Section 4 title.                                                                                                                                |
| espaces analytiques complexes                        | complex analytic spaces                        | Per task spec.                                                                                                                                  |
| groupes de Picard locaux                             | local Picard groups                            | Per task spec.                                                                                                                                  |
| groupes d'homotopie locale                           | local homotopy groups                          | Per source index; notation `Π^x_i(X)`.                                                                                                          |
| `πix`, `πi^x`                                        | `Π^x_i`                                        | The "local πᵢ at x" of the source — rendered with capital pi-superscript to disambiguate from the ordinary πᵢ.                                  |
| profondeur homotopique                               | homotopical depth                              | Per glossary.                                                                                                                                   |
| profondeur homotopique rectifiée                     | rectified homotopical depth                    | Per glossary.                                                                                                                                   |
| profondeur cohomologique                             | cohomological depth                            | Per glossary.                                                                                                                                   |
| géométriquement factoriel / parafactoriel            | geometrically factorial / parafactorial        | Per task spec.                                                                                                                                  |
| anneau strictement local                             | strictly local ring                            | Per task spec.                                                                                                                                  |
| clôture strictement locale                           | strictly local closure                         | Standard.                                                                                                                                       |
| hensélisé strict                                     | strict henselization                           | Modern English for the strictly local closure in N.D.E. footnotes.                                                                              |
| corps de représentants                               | field of representatives                       | Standard for Cohen-structure-theory phrase.                                                                                                     |
| théorème de connexion (de Zariski)                   | (Zariski's) connection theorem                 | Standard.                                                                                                                                       |
| `J`-cofini                                           | `J`-cofinite                                   | Per Hartshorne usage cited in N.D.E.                                                                                                            |
| dualité affine                                       | affine duality                                 | Title of Conjecture 1.2.                                                                                                                        |
| « bon anneau »                                       | "good ring"                                    | Kept the scare quotes as in source.                                                                                                             |
| courbe immergée                                      | embedded curve                                 | Standard.                                                                                                                                       |
| « tame » (groupe fondamental)                        | "tame" (fundamental group)                     | Kept the English loanword in scare quotes as in source.                                                                                         |
| anneaux locaux variables                             | "variable" local rings                         | Kept scare quotes.                                                                                                                              |
| sous-schéma fermé                                    | closed subscheme                               | Standard.                                                                                                                                       |
| section hyperplane                                   | hyperplane section                             | Per glossary.                                                                                                                                   |
| schéma dual                                          | dual scheme                                    | Standard.                                                                                                                                       |
| fibre géométrique                                    | geometric fiber                                | Standard.                                                                                                                                       |
| `Spec(Â)` / complété                                 | `Spec(Â)` / completion                         | Standard, hat preserved.                                                                                                                        |
| `prof htp_Y(X)`                                      | `prof htp_Y(X)`                                | Symbol preserved verbatim per source.                                                                                                           |
| « théorème de Hurewicz local »                       | "local Hurewicz theorem"                       | Kept scare quotes; per source.                                                                                                                  |
| Stein                                                | Stein                                          | Standard analytic-geometry term, kept.                                                                                                          |
| « concavité » topologique                            | topological "concavity"                        | Kept scare quotes.                                                                                                                              |
| pur le long de `Y`                                   | pure along `Y`                                 | Per Exp. X usage.                                                                                                                               |
| connexe en dimension `⩾ k`                           | connected in dimension `⩾ k`                   | Standard.                                                                                                                                       |
| théorème de Bertini                                  | Bertini's theorem                              | Standard.                                                                                                                                       |
| anneau gradué / cône projetant                       | graded ring / projecting cone                  | Standard.                                                                                                                                       |
| anneau de coordonnées homogènes                      | homogeneous coordinate ring                    | Standard.                                                                                                                                       |
| schéma de Picard local                               | local Picard scheme                            | Per Boutot-era usage.                                                                                                                           |
| groupe pro-algébrique / quasi-algébrique             | pro-algebraic / quasi-algebraic group          | Standard.                                                                                                                                       |
| matrice d'intersection                               | intersection matrix                            | Standard.                                                                                                                                       |
| il y a tout lieu de penser                           | there is every reason to think                 | Per task modality table; not used in this Exposé (the surrounding modality leans on *il semble*, *plausible*, *on s'attend*, *il est tentant*). |
| il est tentant de                                    | it is tempting to                              | Translation of *il est tentant de*; preserves the speculative register.                                                                         |
| plausible                                            | plausible                                      | Kept as cognate; the source uses *il est plausible que* / *plausible que*. Preserves modality.                                                  |
| on s'attendra à ce que                               | one will expect that                           | Future-modal; preserves the projection of expectation forward.                                                                                  |
| il semble                                            | it seems                                       | Per modality table.                                                                                                                             |
| il doit être équivalent de dire                      | it should be equivalent to say                 | Preserves the projected-but-unproven equivalence.                                                                                               |
| doit pouvoir se remplacer                            | should be replaceable                          | Preserves the conditional / projected feasibility.                                                                                              |
| sans doute                                           | doubtless                                      | Per modality table.                                                                                                                             |
| il est difficile de douter que                       | it is difficult to doubt that                  | Litotes preserved.                                                                                                                              |
| à vrai dire                                          | actually                                       | Idiomatic English equivalent.                                                                                                                   |
| il est tentant de compléter                          | it is tempting to complete                     | Preserves speculative register.                                                                                                                 |
| N.D.E.                                               | *N.D.E.*                                       | Editor's note, italicized abbreviation per glossary.                                                                                            |
| `7→`, `−→`, `∼=`                                     | `↦`, `→`, `≅`                                  | OCR repair, per glossary.                                                                                                                       |
| `π1`, `π0`, `πi`                                     | `π₁`, `π₀`, `πᵢ`                               | Unicode subscripts in backticks, per task spec.                                                                                                 |

[^N.D.E-XIII-1]: *N.D.E.* In fact, this generalization is not to be found there; see note below, and the editor's note
    (4) on page 2.

[^XIII-1-1]: Cf. *Séminaire Hartshorne*, cited at the end of Exp. IV.

[^XIII-1-2]: This conjecture, and conjecture 1.2 below, are false, as R. Hartshorne has shown, "Affine duality and
    cofinite modules", *Invent. Math.* **9** (1969/70), p. 145–164, section 3.

[^N.D.E-XIII-2]: *N.D.E.* However, if `A` is complete local (resp. regular of positive characteristic) and `J` is the
    maximal ideal, the statement is true for `M` finitely generated (resp. `M = A`), cf. (Hartshorne R.,
    "Affine duality and cofinite modules", *Invent. Math.* **9** (1969/70), p. 145–164, corollary 1.4)
    (resp. (Huneke C. & Sharp R., "Bass numbers of local cohomology modules", *Trans. Amer. Math. Soc.*
    **339** (1993), no. 2, p. 765–779), which moreover contains far stronger results). For completely
    different methods (`𝒟`-modules) allowing one to approach characteristic zero, see (Lyubeznik G.,
    "Finiteness properties of local cohomology modules (an application of `𝒟`-modules to commutative
    algebra)", *Invent. Math.* **113** (1993), no. 1, p. 41–55); see also by the same author "Finiteness
    properties of local cohomology modules for regular local rings of mixed characteristic: the unramified
    case", *Comm. Algebra* **28** (2000), no. 12, p. 5867–5882, Special issue in honor of Robin Hartshorne,
    and "Finiteness properties of local cohomology modules: a characteristic-free approach", *J. Pure Appl.
    Algebra* **151** (2000), no. 1, p. 43–50. The notion of cofinite module has evolved since under
    Hartshorne's aegis. One says that `M` is *`J`-cofinite* if its support is contained in `V(J)` and if
    all `Extⁱ_A(A/J, Hⁱ_J(M))` are finitely generated. On this subject, see for example (Delfino D. &
    Marley Th., "Cofinite modules and local cohomology", *J. Pure Appl. Algebra* **121** (1997), no. 1, p.
    45–52).

[^XIII-1-3]: This conjecture, false as it stands, has nonetheless been established in a rather close form by R.
    Hartshorne, "Affine duality and cofinite modules", *Invent. Math.* **9** (1969/70), p. 145–164.

[^XIII-1-4]: Part (i) of this conjecture is proved by R. Hartshorne when `X` is smooth; cf. *Ample subvarieties of
    algebraic varieties*, Notes written in collaboration with C. Musili, Lect. Notes in Math., vol. 156,
    Springer-Verlag, Berlin–New York, 1970, theorem III.5.2. The same author also found an example for (ii),
    cf. R. Hartshorne, "Cohomological dimension of algebraic varieties", *Ann. of Math. (2)* **88** (1968), p.
    403–450, example page 449.

[^N.D.E-XIII-3]: *N.D.E.* Hartshorne has proved (Hartshorne R., "Cohomological dimension of algebraic varieties", *Ann.
    of Math. (2)* **88** (1968), p. 403–450) that the cohomology `H^{n−1}(𝐏^n_k − X, F)` is zero for `F`
    coherent and `X` of positive dimension (`k` algebraically closed). In fact, thanks essentially to Serre
    duality and to Lichtenbaum's theorem — vanishing of the cohomology of coherent sheaves in maximal
    dimension of irreducible non-complete quasi-projective varieties — one reduces to proving that the
    formal completion `𝐏̂^n_k` and `X` have the same field of rational functions. This is the difficult
    point (theorem 7.2 of *loc. cit.*); in other words, `𝐏^n_k` is *G3* in the terminology of (Hironaka H.
    & Matsumura H., "Formal functions and formal embeddings", *J. Math. Soc. Japan* **20** (1968), p.
    52–82). These authors proved independently the preceding results, and in fact much better ones. They
    proved that `X` is universally *G3* and computed the field of rational functions of the formal
    completion of an abelian variety along a subvariety of positive dimension. It is in this article that
    the conditions *G1*, *G2*, *G3*, now classical, appear for the first time.

[^XIII-1-5]: The question has just been resolved in the affirmative by R. Hartshorne (Hartshorne R., "Ample vector
    bundles", *Publ. Math. Inst. Hautes Études Sci.* **29** (1966), p. 63–94, theorem 8.1) and H. Hironaka.

[^N.D.E-XIII-4]: *N.D.E.* See conjecture 3.5 and the corresponding note.

[^N.D.E-XIII-5]: *N.D.E.* Write `K = lim_{a ≠ 0} A[1/a]` and observe that `a ≠ 0` is `A`-regular.

[^XIII-2-1]: Cf. EGA IV 5.7.2.

[^XIII-2-2]: Cf. EGA IV 7.8.3 (i) (ii) (v).

[^N.D.E-XIII-6]: *N.D.E.* For a very beautiful direct proof, see (Fulton W. & Lazarsfeld R., "Connectivity and its
    applications in algebraic geometry", in *Algebraic geometry (Chicago, Ill., 1980)*, Lect. Notes in
    Math., vol. 862, Springer, Berlin–New York, 1981, p. 26–92, theorem 2.1). Cf. also [HL], cited in the
    editor's note (22) page 155.

[^N.D.E-XIII-7]: *N.D.E.* See the following editor's note.

[^N.D.E-XIII-8]: *N.D.E.* One now finds a proof of this conjecture in the literature, and so the preceding one must also
    be considered as proved as indicated above. One can also find two attempts at proofs, published earlier
    but alas unsuccessful, by Flenner and Trivedi. See Trivedi V., "Erratum: 'A local Bertini theorem in
    mixed characteristic'", *Comm. Algebra* **25** (1997), no. 5, p. 1685–1686. However, the editor has not
    verified that the proof is by now complete.

[^N.D.E-XIII-9]: *N.D.E.* The analogous statement is true for (connected) schemes `X` of finite type over a separably
    closed field `k` under the hypothesis of strong desingularization for all `k`-schemes (of finite type),
    in particular if `k` is of characteristic zero or `X` of dimension `⩽ 2`. To this end one reduces to
    the case of quasi-projective surfaces by Lefschetz-type techniques developed by Mme Raynaud, cf. notes
    *supra*; see SGA 7.I, theorem II.2.3.1.

[^XIII-3-1]: The possibility of "resolving" `A` is proved now in full generality by Abhyankar [8].

[^N.D.E-XIII-10]: *N.D.E.* This problem is, as of autumn 2004, still open.

[^N.D.E-XIII-11]: *N.D.E.* The statements are made precise in the Comments (section 6). The conjectures that appear
    there have become theorems, cf. the footnotes of section 6.

[^XIII-4-1]: The formulations 4.1 to 4.3 that follow are provisional. See conjectures A to D below, in "comments on Exp.
    XIII", for more satisfactory formulations, as well as Exp. XIV.

[^N.D.E-XIII-12]: *N.D.E.* The meaning of this question is not clear; indeed, the very statement of the problem does not
    seem to have a sense in this case, since the codimension of `Y` in `X` is not defined when `Y` is no
    longer assumed analytic.

[^XIII-4-2]: If `i ⩾ 2`. For the case `i ⩽ 1`, cf. Comments in no 6 below, page 154.

[^XIII-4-3]: At least if `x` does not disconnect `X` in a neighborhood of `x`, cf. Comments below, page 154.

[^XIII-4-4]: For a corrected formulation, cf. Comments below, page 154.

[^XIII-4-5]: Cf. Exp. XIV for the corresponding results in scheme theory.

[^XIII-4-6]: See previous note.

[^N.D.E-XIII-13]: *N.D.E.* The question has been greatly clarified by the results of Boutot (Boutot J.-F., *Schéma de
    Picard local*, Lect. Notes in Math., vol. 632, Springer, Berlin, 1978). In particular, if `A` is a
    complete (noetherian) local `k`-algebra of depth `⩾ 2` such that `H²_𝔪(A)` is finite-dimensional over
    `k`, the local Picard group is a group scheme locally of finite type over `k`, with tangent space at
    the origin `H²_𝔪(A)`. If `A` is moreover normal of dimension `⩾ 3`, Serre's normality criterion XI
    3.11 together with corollary V 3.6 ensure the required finiteness and, hence, the existence of the
    local Picard scheme. See also (Lipman J., "The Picard group of a scheme over an Artin ring", *Publ.
    Math. Inst. Hautes Études Sci.* **46** (1976), p. 15–86) for an approach closer to that of
    Grothendieck sketched above.

[^N.D.E-XIII-14]: *N.D.E.* Mumford D., "The topology of normal singularities of an algebraic surface and a criterion for
    simplicity", *Publ. Math. Inst. Hautes Études Sci.* **9** (1961), p. 5–22.

[^N.D.E-XIII-15]: *N.D.E.* Factorial rings with non-factorial henselization arise naturally when one studies moduli
    spaces of vector bundles. See for example (Drézet J.-M., "Groupe de Picard des variétés de modules de
    faisceaux semi-stables sur `𝐏²`", in *Singularities, representation of algebras, and vector bundles
    (Lambrecht, 1985)*, Lect. Notes in Math., vol. 1273, Springer, Berlin, 1987, p. 337–362). Strictly
    speaking, Drézet shows that the completion is not factorial, but in fact the proof gives the result
    for the henselization: the point is that Luna's étale slice theorem (Luna D., "Slices étales", in *Sur
    les groupes algébriques*, Mém. Soc. math. France, vol. 33, Société mathématique de France, Paris,
    1973, p. 81–105) describes the local ring of a quotient in the sense of invariant geometry near a
    semi-stable point locally for the étale topology.

[^XIII-5-1]: For a more flexible notion of "geometrically factorial" local ring, cf. Comments, page 152.

[^N.D.E-XIII-16]: *N.D.E.* See page 152: a local ring is geometrically factorial (resp. parafactorial) if its strict
    henselization is factorial (resp. parafactorial).

[^N.D.E-XIII-17]: *N.D.E.* See EGA IV.16.

[^XIII-6-1]: Written in March 1963.

[^XIII-6-2]: Or, preferably, SGA 4.

[^XIII-6-3]: Or EGA IV 18.8.

[^XIII-6-4]: Cf. M. Artin in SGA 4 XIX.

[^N.D.E-XIII-18]: *N.D.E.* See for example (Strano R., "The Brauer group of a scheme", *Ann. Mat. Pura Appl. (4)*
    **121** (1979), p. 157–169) where the hypothesis of geometric parafactoriality of the local rings of a
    scheme `X` sometimes allows one to show the coincidence of the Brauer groups of `X` (computed in terms
    of Azumaya algebras) and of the cohomological Brauer group of `X`.

[^N.D.E-XIII-19]: *N.D.E.* The link between Brauer group and Picard group is intimate. Let us cite in this connection
    the following results of Saito (Saito S., "Arithmetic on two-dimensional local rings", *Invent. Math.*
    **85** (1986), no. 2, p. 379–414) in the case of surfaces, the first being local, the other global.
    Let `A` be an excellent local ring of dimension 2, normal and henselian with finite residue field, and
    `X` the complement of the closed point in `Spec(A)`. Then one has a perfect duality of torsion groups
    `Pic(X) × Br(X) → ℚ/ℤ` — by Brauer group of `X`, one means cohomological Brauer group
    `Br(X) = H²_ét(X, 𝐆_m)`. In the global case, one has the following generalization of a result of
    Lichtenbaum (Lichtenbaum S., "Duality theorems for curves over `p`-adic fields", *Invent. Math.* **7**
    (1969), p. 120–136): let `k` be the field of fractions of a complete discrete valuation ring `𝒪` with
    finite residue field and `X` a projective, smooth and geometrically complete curve over `k`. The group
    `Pic⁰(X)` is equipped with the topology induced from the adic topology of `k`, and `Pic(X)` is the
    topological group that makes `Pic⁰(X)` an open subgroup. Then one has a perfect duality of topological
    groups `Pic(X) × Br(X) → ℚ/ℤ`. Note that this statement, which concerns curves, is of course proved by
    considering a regular (proper and flat) model of `X` over `𝒪`: it is a result about surfaces.

[^XIII-6-5]: Cf. A. Grothendieck, *Le groupe de Brauer II* (Séminaire Bourbaki no 297, Nov. 1965), notably 1.8 and 1.11
    b.

[^XIII-6-6]: Cf. SGA 4 XIV.

[^XIII-6-7]: Cf. SGA 4 XVIII.

[^XIII-6-8]: Cf. SGA 5 I.

[^N.D.E-XIII-20]: *N.D.E.* See Verdier J.-L., "Dualité dans la cohomologie des espaces localement compacts", in
    *Séminaire Bourbaki, vol. 9*, Société mathématique de France, Paris, 1995, Exp. 300, p. 337–349.

[^XIII-6-9]: Cf. Exp. XIV.

[^N.D.E-XIII-21]: *N.D.E.* When the pair `(X, Y)` is moreover polyhedral, this equivalence is true; cf. (Eyral C.,
    "Profondeur homotopique et conjecture de Grothendieck", *Ann. Sci. Éc. Norm. Sup. (4)* **33** (2000),
    no. 6, p. 823–836).

[^XIII-6-10]: In the first edition of these notes, we had employed the term "true homotopical depth". In the present
    version, we follow EGA IV 10.8.1.

[^N.D.E-XIII-22]: *N.D.E.* All the conjectures that follow, suitably rectified if I dare say so, have become theorems
    thanks to the work of Hamm and Lê Dũng Tráng (Hamm H.A. & Lê Dũng Tráng, "Rectified homotopical depth
    and Grothendieck conjectures", in *The Grothendieck Festschrift, Vol. II*, Progr. Math., vol. 87,
    Birkhäuser, Boston, 1990, p. 311–351), cited [HL] in what follows. As regards the two conjecturally
    equivalent definitions of rectified depth, they are even equivalent to a third, expressing itself in
    terms of Whitney stratification (cf. *loc. cit.*, theorem 1.4).

[^N.D.E-XIII-23]: *N.D.E.* As observed in [HL], example 3.1.3, this conjecture is false already for
    `X = {z ∈ ℂⁿ ∣ z₁² + z₂³ + ⋯ + zₙ³ = 0}`, `n ⩾ 4` and `Y` reduced to the origin. But, suitably
    modified, it is true (theorem 3.1.4 of *loc. cit.*).

[^N.D.E-XIII-24]: *N.D.E.* This conjecture is proved, even in the case where `E` is singular, in \[HL\]: it is theorem
    3.2.1.

[^N.D.E-XIII-25]: *N.D.E.* This conjecture is proved in [HL], even in its strong form of the remark that follows, cf.
    theorem 3.3.1 of *loc. cit.*

[^N.D.E-XIII-26]: *N.D.E.* This conjecture is again proved in [HL], even in its strong form of the remark that follows,
    cf. theorem 3.4.1 of *loc. cit.*

[^N.D.E-XIII-27]: *N.D.E.* Let us finally signal the following result of Fulton, to be compared with the Fulton-Hansen
    result cited in editor's note (4) page 127: let `X` and `H` be closed subschemes of `𝐏^m_ℂ`, `n` the
    dimension of `X` and `d` the codimension of `H`. Then the map

    ```text
    πᵢ(X, X ∩ H) → πᵢ(𝐏^n_ℂ, H)
    ```

    is an isomorphism if `i ⩽ n − d` and is surjective if `i = n − d − 1`; see (Fulton W., "Connectivity and its
    applications in algebraic geometry", in *Algebraic geometry (Chicago, Ill., 1980)*, Lect. Notes in Math., vol. 862,
    Springer, Berlin–New York, 1981, p. 26–92).

[^N.D.E-XIII-29]: *N.D.E.* This conjecture is demonstrated in [HL], cf. theorem 3.5.1 of *loc. cit.*
