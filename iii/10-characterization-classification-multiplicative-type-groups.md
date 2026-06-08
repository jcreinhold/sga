# Exposé X. Characterization and classification of groups of multiplicative type

<!-- label: III.X -->

*by A. Grothendieck*

> Version xy of 6 November 2009: Addenda placed in Section 9, reviewed through 8.8.[^X-0-0]

## 1. Classification of isotrivial groups. Case of a base field

<!-- original page 77 -->

Recall (IX 1.1) that the group of multiplicative type $H$ over the prescheme $S$ is said to be *isotrivial* if there
exists an étale, finite, surjective morphism $S' \to S$ such that $H' = H \times_{S} S'$ is diagonalizable. When $S$ is
connected, $S'$ decomposes as a finite sum of connected components $S'_{i}$, and one can therefore (possibly by
replacing $S'$ by one of the $S'_{i}$) assume $S'$ connected. Finally, one knows that $S'$ can be dominated by an
$S'_{1}$ finite, étale and connected, which is Galois, i.e. a principal homogeneous bundle over $S$ with group
$\Gamma_{S}$, where $\Gamma$ is an ordinary finite group (cf. SGA 1, V N°s 7 & 3 when $S$ is locally noetherian, and
[EGA IV₄, 18.2.9](https://jcreinhold.github.io/ega/iv/31-ch4-18-complements-etale-morphisms.html#182-étale-covers) in
the general case).[^N.D.E-X-1] We assume $S'$ chosen in this way, and we propose to determine the groups of
multiplicative type $H$ over $S$ which are "trivialized" by $S'$, i.e. such that $H' = H \times_{S} S'$ is
diagonalizable.[^N.D.E-X-2] By descent theory (cf. SGA 1, VIII 5.4), the category of these $H$ is equivalent to the
category of diagonalizable groups $H'$ over $S'$, equipped with operations of $\Gamma$ on $H'$ compatible with the
operations of $\Gamma$ on $S'$. (N.B. As the groups under consideration are affine over the base, the question of
effectivity of a descent datum is answered in the affirmative, cf. SGA 1, VIII 2.1.) Now $S'$ being connected, the
contravariant functor

$$ M \mapsto D_{S'}(M) $$

is an anti-equivalence of the category of ordinary commutative groups with the category <!-- original page 78 --> of
diagonalizable groups over $S'$ (cf. VIII 1.6), a quasi-inverse functor being $H \mapsto \operatorname{Hom}_{S'-gr.}(H,
G_{m,S'})$.[^N.D.E-X-3]

**Proposition 1.1.** *Let $S$ be a connected prescheme, $S'$ a connected principal cover of $S$ with group $\Gamma$
(finite). Then the category of groups of multiplicative type over $S$ split[^N.D.E-X-4] by $S'$ is anti-equivalent to
the category of $\Gamma$-modules, i.e. of ordinary commutative groups $M$ equipped with a homomorphism $\Gamma \to
\operatorname{Aut}_{gr.}(M)$.*

<!-- label: III.X.1.1 -->

One concludes from this in a standard manner:

**Corollary 1.2.** *Let $S$ be a connected prescheme, $\xi : \operatorname{Spec}(\Omega) \to S$ a "geometric point" of
$S$, i.e. a homomorphism into $S$ of the spectrum of an algebraically closed field $\Omega$; consider the fundamental
group of $S$ at $\xi$ (cf. SGA 1 V, N° 7):*

<!-- label: III.X.1.2 -->

$$ \pi = \pi_{1}(S, \xi). $$

*Then the category of isotrivial groups of multiplicative type $H$ over $S$ is anti-equivalent to the category of
"Galois modules" under $\pi$, i.e. of $\pi$-modules $M$ such that the stabilizer in $\pi$ of every point of $M$ is an
open subgroup.*

*In this correspondence, to the isotrivial group of multiplicative type $H$ is associated the group $M =
\operatorname{Hom}_{\Omega-gr.}(H_{\xi}, G_{m,\Omega})$, where $H_{\xi}$ is the fiber of $H$ at $\xi$; this group is
naturally equipped with operations of $\pi_{1}(S, \xi)$.*

**Remark 1.3.** We shall see below (cf. 5.16) that if $S$ is normal, or more generally geometrically unibranch, then
every group of multiplicative type and of finite type over $S$ is necessarily isotrivial, so that the classification
principle 1.2 is applicable to groups of multiplicative type and of finite type over $S$, which correspond to <!--
original page 79 --> Galois $\pi$-modules that are of finite type over $\mathbb{Z}$. For the moment, let us confine
ourselves to the following result:

<!-- label: III.X.1.3 -->

**Proposition 1.4.** *Let $k$ be a field, $H$ a group of multiplicative type and of finite type over $k$; then $H$ is
isotrivial, i.e. there exists a finite separable extension $k'$ of $k$ which splits $H$.*

<!-- label: III.X.1.4 -->

*Consequently, by 1.2, if $\pi$ is the topological Galois group of an algebraic closure $\Omega$ of $k$, the category of
groups of multiplicative type and of finite type $H$ over $k$ is anti-equivalent to the category of Galois modules $M$
under $\pi$ that are of finite type as $\mathbb{Z}$-modules.*

It follows first from the fact that $H$ is of finite type over $k$ and from the "principle of the finite extension" (cf.
[EGA IV₃, 9.1.4](https://jcreinhold.github.io/ega/iv/22-ch4-09-constructible-properties.html#91-the-principle-of-finite-extension))
that there exists a finite extension $k'$ of $k$ which splits $H$. Let us recall the principle of the proof: by
hypothesis there exist a diagonalizable group of finite type $G$ over $k$, a faithfully flat $S'$ over $S =
\operatorname{Spec}(k)$, and an isomorphism of $S'$-groups $H_{S'} \simeq G_{S'}$. Possibly replacing $S'$ by the
residue field of a point of $S'$, we may suppose that $S'$ is the spectrum of an extension $K$ of $k$. The latter is the
inductive limit of its finitely generated subalgebras $A_{i}$, from which it readily follows (cf.
[EGA IV₃, 8.8.2.4](https://jcreinhold.github.io/ega/iv/21-ch4-08-projective-limits.html#88-preschemes-of-finite-presentation-over-a-projective-limit-of-preschemes))
that $u$ comes from an $A_{i}$-isomorphism $u_{i} : H_{A_{i}} \simeq G_{A_{i}}$ for $i$ large enough. By the
Nullstellensatz, there exists a quotient ring $k'$ of $A_{i}$ which is a finite extension of $k$. The latter therefore
splits $H$.

<!-- original page 65 -->

Then $k'$ is a radicial extension of a separable extension $k'_{s}$ of $k$. By IX 5.4, the isomorphism $u' : H_{k'}
\simeq G_{k'}$ comes from an isomorphism $H_{k'_{s}} \simeq G_{k'_{s}}$, which proves that $k'_{s}$ splits $H$ and
establishes 1.4.

**Remark 1.5.** Statement 1.2 yields in particular a characterization of isotrivial tori over $S$ of relative dimension
$n$: setting $\pi = \pi_{1}(S, \xi)$, they correspond to classes (up to "equivalence") of representations $\pi \to GL(n,
\mathbb{Z})$ with kernel an open subgroup of $\pi$.

<!-- label: III.X.1.5 -->

**1.6.** Even when $S$ is an algebraic curve, there can exist over $S$ tori (of relative dimension `2`) that are not
locally isotrivial (and *a fortiori* not isotrivial); <!-- original page 80 --> there can also exist locally trivial
tori that are not isotrivial. (Note however that such phenomena can present themselves only if $S$ is not normal, as
already signalled in 1.3.) Let for example $S$ be an irreducible algebraic curve (over an algebraically closed field to
fix ideas) having an ordinary double point $a$, let $S'$ be its normalization, and $b$ and $c$ the two points of $S'$
above $a$. One then constructs a principal homogeneous bundle $P$ over $S$, with structural group $\mathbb{Z}$,
connected, by attaching together an infinity of copies of $S'$ along the diagram

<!-- label: III.X.1.6 -->

```text
······         b            b           b            b   ······
                       c            c           c
```

(N.B. This is a principal bundle in the sense of the étale topology.) Now one has a homomorphism

```text
                                     ⎛ 1  n ⎞
φ : ℤ ⟶ GL(2, ℤ),       φ(n) =       ⎝ 0  1 ⎠,
```

which permits the construction of a torus $T$ over $S$, of relative dimension `2`, from the trivial torus $G^{2}_{m}$
over $P$ and from the descent datum on the latter deduced from $\phi$. (N.B. one will note that the projection $P \to S$
is covering for the étale topology and *a fortiori* for the canonical topology of `(Sch)`, and that the descent datum
under consideration is necessarily effective, since $G^{2}_{m,P}$ is affine over $P$.) It is not difficult to prove that
$T$ is not isotrivial in a neighborhood of $a$[^N.D.E-X-5] (it is however trivial on $S - {a}$).

One finds a variant of this construction by taking for $S$ a curve having two irreducible components `S_1` and `S_2`
intersecting in two points $a'$ and $a''$, which permits the construction of a principal homogeneous bundle $P$ over $S$
with group $\mathbb{Z}_{S}$, connected and locally trivial, hence an associated torus $T$ which is locally trivial, but
not isotrivial.

## 2. Infinitesimal variations of structure

<!-- original page 81 -->

[^N.D.E-X-6] Let us begin by recalling the following result (cf. SGA 1, I 8.3 in the case $S$ locally noetherian, [EGA
IV₄,
18.1.2](https://jcreinhold.github.io/ega/iv/31-ch4-18-complements-etale-morphisms.html#181-a-remarkable-equivalence-of-categories)
in general):

<!-- original page 66 -->

**Recall 2.0.** *Let $S$ be a prescheme, `S_0` a sub-prescheme having the same underlying set. Then the functor*

<!-- label: III.X.2.0 -->

```text
X ↦ X_0 = X ×_S S_0
```

*is an equivalence between the category of étale preschemes over $S$ and the analogous category over `S_0`.*

**Proposition 2.1.** *Let $S$ be a prescheme, `S_0` a sub-prescheme having the same underlying set (i.e. defined by a
nilideal $I$). Then the functor*

<!-- label: III.X.2.1 -->

```text
H ↦ H_0 = H ×_S S_0
```

*from the category of preschemes in groups of multiplicative type over $S$ to the analogous category over `S_0`, is
fully faithful.*

*Moreover, it induces an equivalence between the category of quasi-isotrivial groups of multiplicative type over $S$ and
the analogous category over `S_0`.*

Let us first prove the full faithfulness, i.e. that if $H$, $G$ over $S$ are of multiplicative type, then

```text
Hom_{S-gr.}(H, G) ⟶ Hom_{S_0-gr.}(H_0, G_0)
```

is bijective. The question being local on $S$, we may suppose $S$ affine; there then exists a faithfully flat
quasi-compact morphism $S' \to S$ which splits $H$ and $G$. Let $S'' = S' \times_{S} S'$; denote by $H', G'$ resp. $H'',
G''$ the groups deduced from `H, G` by the base change $S' \to S$ resp. $S'' \to S$; define $S'_{0}$ and $S''_{0}$
similarly, the latter being also isomorphic to $S'_{0} \times_{S_{0}} S'_{0}$. One then finds a commutative diagram with
exact rows:

```text
Hom_{S-gr.}(H, G)      ⟶  Hom_{S′-gr.}(H′, G′)      ⇉  Hom_{S″-gr.}(H″, G″)
        ↓ u                       ↓ u′                       ↓ u″
Hom_{S_0-gr.}(H_0, G_0) ⟶ Hom_{S′_0-gr.}(H′_0, G′_0) ⇉  Hom_{S″_0-gr.}(H″_0, G″_0),
```

so to prove that $u$ is bijective, it suffices to prove that $u'$ and $u''$ are, which reduces us to the case where $H$
and $G$ are diagonalizable, hence of the form $D_{S}(M)$ and <!-- original page 82 --> $D_{S}(N)$, where $M$ and $N$ are
ordinary commutative groups. One will therefore have likewise $H_{0} = D_{S_{0}}(M)$, $G_{0} = D_{S_{0}}(N)$. One then
has a commutative diagram[^N.D.E-X-7]

```text
Hom_{S-gr.}(N_S, M_S)       ⥲  Hom_{S-gr.}(D_S(M), D_S(N))
        ↓                                  ↓
Hom_{S_0-gr.}(N_{S_0}, M_{S_0}) ⥲ Hom_{S_0-gr.}(D_{S_0}(M), D_{S_0}(N)),
```

<!-- original page 67 -->

where the horizontal arrows are isomorphisms by VIII 1.4, so we are reduced to proving that the homomorphism

```text
(×)     Hom_{S-gr.}(N_S, M_S) ⟶ Hom_{S_0-gr.}(N_{S_0}, M_{S_0})
```

is bijective, i.e. to proving that the functor $M_{S} \mapsto M_{S_{0}}$, from preschemes in constant commutative groups
over $S$ to preschemes in constant commutative groups over `S_0`, is fully faithful. Now $(\times)$ identifies also with
the natural map

```text
Hom_{gr.}(N, Γ(M_S)) ⟶ Hom_{gr.}(N, Γ(M_{S_0}))
```

deduced from $\Gamma(M_{S}) \to \Gamma(M_{S_{0}})$; this latter map is obviously bijective (since $\Gamma(M_{S})$ = set
of locally constant maps from $S$ to $M$, depends only on the topological space underlying $S$), whence the desired
conclusion.

To prove the second assertion of 2.1, it remains to see that every group `H_0` of multiplicative type over `S_0` which
is quasi-isotrivial comes from a quasi-isotrivial group of multiplicative type $H$ over $S$. To see this, let $S'_{0}
\to S_{0}$ be an étale surjective morphism which splits `H_0`.

One knows (cf. 2.0) that there exists an étale morphism $S' \to S$ and an `S_0`-isomorphism $S' \times_{S} S_{0} \simeq
S'_{0}$, so that one may suppose that $S'_{0}$ comes from $S'$ by reduction. Since <!-- original page 83 --> $H'_{0}$ is
diagonalizable, one sees at once that it is isomorphic to the group deduced by base change $S'_{0} \to S'$ from a
diagonalizable group $H'$ over $S'$ (N.B. if $H'_{0} = D_{S'_{0}}(M)$, one takes $H' = D_{S'}(M)$). Set as usual $S'' =
S' \times_{S} S'$, $S''' = S' \times_{S} S' \times_{S} S'$, and define $S''_{0}$, $S'''_{0}$ similarly, deduced from the
preceding by the base change $S_{0} \to S$ and isomorphic also to the fibered square resp. cube of $S'_{0}$ over `S_0`.
Using the full faithfulness already proved, in the cases $(S'', S''_{0})$ and $(S''', S'''_{0})$, one sees that the
natural descent datum on $H'_{0}$ relative to $S'_{0} \to S_{0}$ (cf. IV 2.1) comes from a well-determined descent datum
on $H'$ relative to $S' \to S$. This descent datum is effective since $H'$ is affine over $S'$ (SGA 1, VIII 2.1), so
there exists an $S$-group $H$ such that $H \times_{S} S' = H' = D_{S'}(M)$, and $H$ is therefore of quasi-isotrivial
multiplicative type.

One then verifies easily, using now the full-faithfulness result for $(S', S'_{0})$, that the given isomorphism between
$H'_{0}$ and $H' \times_{S'} S'_{0}$ comes from an isomorphism between `H_0` and $H \times_{S} S_{0}$. (For a more
formal exposition of results of this kind, see Giraud's article in preparation[^X-2-1] on descent theory.)

**Corollary 2.2.** *Let $H$ be an $S$-group of multiplicative type, and $H_{0} = H \times_{S} S_{0}$. For $H$ to be
quasi-isotrivial (resp. locally isotrivial, resp. isotrivial, resp. locally trivial, resp. trivial), it is necessary and
sufficient that `H_0` be so.*

<!-- label: III.X.2.2 -->

The "only if" is trivial; the "if" has already been seen in the quasi-isotrivial case, since thanks to the full
faithfulness, it suffices to know that every quasi-isotrivial group over `S_0` lifts to a quasi-isotrivial group over
$S$. The same argument works for "trivial". For the case "isotrivial", one takes up the reasoning establishing the
second assertion of 2.1, but taking $S'_{0} \to S_{0}$ étale surjective and finite. The cases "locally isotrivial" and
"locally trivial" follow at once from the cases "isotrivial" and "trivial".

One can generalize 2.2 somewhat when $I$ is nilpotent, without supposing *a priori* $H$ of multiplicative
type:[^N.D.E-X-8]

<!-- original page 84 -->

<!-- original page 68 -->

**Corollary 2.3.** *Suppose the ideal $I$ defining `S_0` locally nilpotent. Let $H$ be a prescheme in groups over $S$,
flat over $S$, and $H_{0} = H \times_{S} S_{0}$. For $H$ to be of quasi-isotrivial multiplicative type, it is necessary
and sufficient that `H_0` be so.*

<!-- label: III.X.2.3 -->

Indeed, suppose `H_0` is of quasi-isotrivial multiplicative type; let us prove that $H$ is so. The question being local
for the étale topology, and the category of étale preschemes over $S$ being equivalent to the category of étale
preschemes over `S_0` by the functor $S' \mapsto S' \times_{S} S_{0}$ (cf. 2.0), one is at once reduced to the case
where `H_0` is diagonalizable, hence isomorphic to a group $D_{S_{0}}(M)$. Let $G = D_{S}(M)$; one then has an
isomorphism $u_{0} : H_{0} \xrightarrow{\sim} G_{0}$; I claim it comes from a unique homomorphism $u : H \to G$, which
will therefore be an isomorphism since $u_{0}$ is one ($H$ and $G$ being flat over $S$, and $I$ locally
nilpotent[^N.D.E-X-9]); this will establish 2.3. Now one has (cf. VIII 1 (xxx))

```text
Hom_{S-gr.}(H, G) ≃ Hom_{S-gr.}(M_S, Hom_{S-gr.}(H, G_{m,S})),
```

and the second member identifies also with

$$ \operatorname{Hom}_{gr.}(M, \operatorname{Hom}_{S-gr.}(H, G_{m,S})), $$

so the homomorphism

```text
(×)     Hom_{S-gr.}(H, G) ⟶ Hom_{S_0-gr.}(H_0, G_0)
```

is isomorphic to the homomorphism

```text
Hom_{gr.}(M, Hom_{S-gr.}(H, G_{m,S})) ⟶ Hom_{gr.}(M, Hom_{S_0-gr.}(H_0, G_{m,S_0}))
```

deduced from the restriction homomorphism

```text
(××)    Hom_{S-gr.}(H, G_{m,S}) ⟶ Hom_{S_0-gr.}(H_0, G_{m,S_0});
```

<!-- original page 85 -->

so to prove that $(\times)$ is bijective, it suffices to prove that $(\times\times)$ is. The question is local on $S$;
we may therefore suppose $S$ affine. Now $G_{m,S}$ being commutative and smooth over $S$, the situation is governed by
IX 3.6, which completes the proof.

**Corollary 2.4.** *Let $A$ be an artinian local ring with residue field $k$, $S = \operatorname{Spec}(A)$, $S_{0} =
\operatorname{Spec}(k)$.*

<!-- label: III.X.2.4 -->

*(i)[^N.D.E-X-10] Let $H$ be an $S$-prescheme in groups, flat and locally of finite type, such that $H_{0} = H
\times_{S} S_{0}$ is of multiplicative type. Then $H$ is of multiplicative type, of finite type and isotrivial. In
particular, every $S$-prescheme in groups $H$ of multiplicative type and of finite type is isotrivial.*

*(ii) The functor $H \mapsto H_{0}$ is an equivalence between the category of groups of multiplicative type of finite
type over $A$ and the analogous category over $k$.*

Indeed, let $H$ be as in (i). Then `H_0` is of multiplicative type and locally of finite type, hence of finite type,
hence isotrivial by 1.4. Therefore, by 2.3 and 2.2, $H$ is of multiplicative type (hence of finite type) and isotrivial.
Assertion (ii) then follows from 2.1.

**Corollary 2.5.** *Let $S' \to S$ be a faithfully flat and radicial morphism.*

<!-- label: III.X.2.5 -->

*(i) The functor $H \mapsto H' = H \times_{S} S'$, from the category of groups of multiplicative type over $S$ to the
analogous category over $S'$, is fully faithful.*

*Moreover, it induces an equivalence between the subcategories formed by the quasi-isotrivial groups of multiplicative
type.*

*(ii) If $H$ is of multiplicative type, for it to be quasi-isotrivial (resp. locally isotrivial, resp. isotrivial, resp.
locally trivial, resp. trivial) it is necessary and sufficient that $H'$ be so.*

Indeed, let $S'' = S' \times_{S} S'$ and $S''' = S' \times_{S} S' \times_{S} S'$; then the hypothesis that $S' \to S$ is
radicial implies that the diagonal immersions $S' \to S''$ and $S' \to S'''$ are surjective, so the base change by
either of these immersions is governed by 2.1 and 2.2. Taking into account that $S' \to S$ is a morphism of effective
descent for the fibered category of groups of multiplicative type over preschemes (since it is faithfully flat and
quasi-compact[^N.D.E-X-11]), our assertion follows formally from 2.1 and 2.2 (cf. for a formal argument the
already-cited Giraud article).

## 3. Finite variations of structure: complete base ring

<!-- original page 86 -->

**Lemma 3.1.** *Let $A$ be a noetherian ring, equipped with an ideal $I$ such that $A$ is separated and complete for the
$I$-adic topology, $S = \operatorname{Spec}(A)$, $S_{0} = \operatorname{Spec}(A/I)$, $G$ and $H$ two $S$-group schemes,
with $G$ of multiplicative type and isotrivial, $H$ affine over $S$, flat over $S$ at the points of $H_{0} = H
\times_{S} S_{0}$, `H_0` of quasi-isotrivial multiplicative type. Then the natural map*

<!-- label: III.X.3.1 -->

```text
Hom_{S-gr.}(G, H) ⟶ Hom_{S_0-gr.}(G_0, H_0)
```

*is bijective.*

For every integer $n \geqslant 0$, let $S_{n} = \operatorname{Spec}(A/I^{n+1})$, and let $G_{n}$, $H_{n}$ be the groups
deduced from $G$, $H$ by the base change $S_{n} \to S$. Since $G/S$ is of isotrivial multiplicative type and $H$ affine
over $S$, then, by IX 7.1, the natural homomorphism

```text
Hom_{S-gr.}(G, H) ⟶ lim_n Hom_{S_n-gr.}(G_n, H_n)
```

is bijective. On the other hand, by 2.3, the $H_{n}$ are of quasi-isotrivial multiplicative type, and by 2.1, the
transition homomorphisms in the projective system $(\operatorname{Hom}_{S_{n}-gr.}(G_{n}, H_{n}))_{n}$ are isomorphisms,
whence 3.1 at once.

**Theorem 3.2.** *Let $A$ be a noetherian ring equipped with an ideal $I$ such that $A$ is separated and complete for
the $I$-adic topology, $S = \operatorname{Spec}(A)$, $S_{0} = \operatorname{Spec}(A/I)$. Then:*

<!-- label: III.X.3.2 -->

<!-- original page 70 -->

*(i) The functor*

```text
H ↦ H_0 = H ×_S S_0
```

*is an equivalence between the category of isotrivial groups of multiplicative type over $S$ and the analogous category
over `S_0`.*

<!-- original page 87 -->

*(ii) Let $H$ be an $S$-group of multiplicative type and of finite type; for $H$ to be isotrivial, it is necessary and
sufficient that `H_0` be so.*

*Proof.* For (i) one can either take up the proof of 2.1, or use 1.2, in either case using the fact that the functor

```text
S′ ↦ S′_0 = S′ ×_S S_0
```

from the category of finite étale schemes over $S$ to the category of finite étale schemes over `S_0` is an equivalence
(SGA 1, I 8.4), which one can also state (reducing to the case $S$ connected, i.e. `S_0` connected), by choosing a
geometric point $\xi$ of `S_0`, by saying that the canonical homomorphism

```text
π₁(S_0, ξ) ⟶ π₁(S, ξ)
```

is an isomorphism.

Let us prove (ii), i.e. that if `H_0` is isotrivial, then $H$ is so. By (i), there exists an isotrivial group of
multiplicative type $G$ over $S$ and an `S_0`-isomorphism

$$ u_{0} : G_{0} \xrightarrow{\sim} H_{0}. $$

[^N.D.E-X-12] Since $H$ is of finite type, so are `H_0` and `G_0`; therefore, by IX 2.1 b), the type of $G$ at each
point of $S$ is an abelian group of finite type, and so $G$ is of finite type over $S$. On the other hand, by 3.1,
$u_{0}$ comes from a homomorphism of $S$-groups

$$ u : G \longrightarrow H. $$

Finally, since $G$, $H$ are of multiplicative type and of finite type over $S$, and since $u_{0}$ is an isomorphism,
then, by IX 2.9, $u$ is an isomorphism (taking into account that every neighborhood of `S_0` in $S$ equals $S$).

**Corollary 3.3.** *Let $A$ be a complete noetherian local ring with residue field $k$.*

<!-- label: III.X.3.3 -->

<!-- original page 88 -->

*(i) Every group of multiplicative type and of finite type over $A$ is isotrivial.*

*(ii) The functor $H \mapsto H \otimes_{A} k = H_{0}$ is an equivalence between the categories of groups of
multiplicative type and of finite type over $A$ and over $k$.*

[^N.D.E-X-12] First, (i) follows from 3.2 (ii) and 1.4; then (ii) follows from 3.2 (i), taking into account the fact
that $H$ is of finite type if and only if `H_0` is (cf. the proof of 3.2 (ii)).

**Remark 3.3.1.** One will note that 3.3 yields, by 1.4, a complete classification of groups of multiplicative type and
of finite type over $A$ in terms of the topological Galois group of an algebraic closure $\Omega$ of $k$.

<!-- label: III.X.3.3.1 -->

**Remarks 3.4.** Under the hypotheses of 3.2 (i.e. $A$ noetherian, separated and complete for the $I$-adic topology, but
without further hypothesis on $A/I$), it will follow from N° 5 that the functor $H \mapsto H_{0}$, from the category of
groups of multiplicative type and of finite type over $S$ to the analogous category over `S_0`, is again fully faithful
(without hypotheses of isotriviality).[^N.D.E-X-13]

<!-- label: III.X.3.4 -->

However, it is not in general essentially surjective; in fact, there can exist an `S_0`-group `H_0` of multiplicative
type and of finite type, locally trivial if one wishes (but not isotrivial), which does not come by reduction from a
group of multiplicative type $H$ over $S$.

To see this, let us take up either of the examples 1.6 of a non-isotrivial group of multiplicative type over a
non-normal curve. One may obviously take this curve affine, say `S_0`, and assume that it is embedded in the affine
space of dimension 2, hence defined by an ideal $J$ in `k[X, Y]`. We shall take for $A$ the completion of this ring for
the $J$-preadic topology, so that $A$ is a regular ring of dimension 2, *a fortiori* normal. We shall see in 5.16 that
it follows that every group of multiplicative type and of finite type over $S = \operatorname{Spec}(A)$ is isotrivial;
therefore `H_0`, which is of finite type and not isotrivial, does not come from a group of multiplicative type $H$ over
$S$ (since $H$ would necessarily be of finite type, hence isotrivial).

**Lemma 3.5.**[^X-3-1] *Let $S$ be a prescheme, $u : G \to H$ a homomorphism of $S$-preschemes in groups, locally of
finite presentation and flat over $S$, $U$ the set of $s \in S$ such that the induced homomorphism on fibers $u_{s} :
G_{s} \to H_{s}$ is flat (resp. smooth, resp. unramified, resp. étale, resp. quasi-finite).*

<!-- label: III.X.3.5 -->

<!-- original page 89 -->

*Then $U$ is open, and the restriction $u|U : G|U \to H|U$ is a flat (resp. smooth, resp. unramified, resp. étale, resp.
quasi-finite) morphism.*

Indeed, let $V$ be the set of points at which $u$ is flat (resp. …). One knows that $V$ is open (cf. SGA 1, I to IV in
the locally noetherian case, EGA IV in general[^N.D.E-X-14]), and that for $x \in G$ above $s \in S$, one has $x \in V$
if and only if $u_{s} : G_{s} \to H_{s}$ is flat (resp. …) at $x$ (same reference; in the flat, smooth, étale cases, one
uses here the flatness of $G$ and $H$ over $S$). Since $u_{s}$ is a homomorphism of locally algebraic groups, this also
means that $u_{s}$ is flat (resp. …) everywhere (Exp. VI_B, 1.3), i.e. $s \in U$. Therefore $U$ is the inverse image of
the open set $V$ by the unit section of $G$, hence open, and $V = G|U$, so $G|U \to H|U$ is flat (resp. …), which
completes the proof. (N.B. In the "unramified" or "quasi-finite" case, the flatness hypothesis on $G$ and $H$ is
unnecessary.)

**Lemma 3.6.** *Let $H$ be a commutative algebraic group over a field $k$, admitting an open subgroup $G$ of
multiplicative type. Then the family of subschemes ${}_{n} H$ ($n > 0$) of $H$ is schematically dense; in particular, if
one has ${}_{n} H = {}_{n} G$ for every $n > 0$, then $H = G$.*

<!-- label: III.X.3.6 -->

Here ${}_{n} H$ denotes the kernel of $n \cdot id_{H}$.[^N.D.E-X-15] Let $\bar{k}$ be an algebraic closure of $k$; it
suffices to show that the family $({}_{n} H_{\bar{k}})_{n > 0}$ is schematically dense in $H_{\bar{k}}$, for then the
family $({}_{n} H)_{n > 0}$ will be so in $H$ (cf. IX 4.5). Thus, one may suppose $k$ algebraically closed, hence $G$ of
the form $D_{k}(M)$, $M$ a finitely generated ordinary commutative group.

<!-- original page 72 -->

Let $M_{0} = M/Torsion(M)$; then $T = D_{k}(M_{0})$ is the largest torus contained in $G$, and $H/T$ is finite, so
$H(k)/T(k)$ is annihilated by an integer $\nu > 0$. One can find a finite number of elements $g_{i} \in H(k)$ such that

```text
H = ∐_i g_i · G,
```

and one will have $g^{\nu}_{i} \in T(k)$. Since $k$ is algebraically closed, $\nu \cdot id_{T}$ is surjective on $T(k)
\simeq k^{\ast d}$, so up to replacing the $g_{i}$ by $g_{i} t^{-1}_{i}$, where $t_{i} \in T(k)$ is such that
$t^{\nu}_{i} = g^{\nu}_{i}$, <!-- original page 90 --> one may suppose that $g^{\nu}_{i} = 1$. If then $n$ is a multiple
of $\nu$, one will have

```text
_n H ⊇ g_i · _n G,
```

and since (for $n > 0$ variable) the family of ${}_{n} G$ is schematically dense in $G$ by IX 4.7, conclusion 3.6
follows.

**Theorem 3.7.** *Let $A$ be a noetherian ring equipped with an ideal $I$ such that $A$ is separated and complete for
the $I$-adic topology, $S = \operatorname{Spec}(A)$, $S_{0} = \operatorname{Spec}(A/I)$, and let $H$ be an affine
$S$-group scheme of finite type, flat over $S$ at the points of `H_0`, such that $H_{0} = H \times_{S} S_{0}$ is of
multiplicative type and isotrivial.*

<!-- label: III.X.3.7 -->

*Then there exists an open and closed subgroup $G$ of $H$, of isotrivial multiplicative type (and of finite type), such
that $G_{0} = H_{0}$.*

By 3.2 (i), there exists an isotrivial group of multiplicative type $G$ over $S$ and an isomorphism

$$ u_{0} : G_{0} \xrightarrow{\sim} H_{0}. $$

By 3.1, $u_{0}$ comes from a unique homomorphism of $S$-groups

$$ u : G \longrightarrow H. $$

Using IX 6.6, one sees that $u$ is a monomorphism (since if $U$ is the set of $s \in S$ such that $u_{s} : G_{s} \to
H_{s}$ is a monomorphism, then $U$ is an open neighborhood of `S_0` hence identical to $S$, and $G|U \to H|U$ is a
monomorphism). By IX 2.5, $u$ is even a closed immersion.

[^N.D.E-X-16] Therefore $G$ is of finite type, hence of finite presentation over $S$. Then, by lemma 3.5 in the "étale"
case, one sees that there exists an open set $U$ neighborhood of `S_0`, hence identical to $S$, such that $G|U \to H|U$
is étale, so $u$ is étale, hence an open immersion (since it is an étale monomorphism[^N.D.E-X-17]), which completes the
proof.

**Corollary 3.8.** *Let $A$ be a noetherian ring equipped with an ideal $I$ such that $A$ is separated and complete for
the $I$-adic topology, $S = \operatorname{Spec}(A)$, $S_{0} = \operatorname{Spec}(A/I)$, and let $H$ be an $S$-prescheme
in groups of finite type, affine and flat over $S$.*

<!-- label: III.X.3.8 -->

<!-- original page 91 -->

*For $H$ to be of multiplicative type and isotrivial, it is necessary and sufficient that `H_0` be so, and that $H$
satisfy one of the following conditions a) and b) (which are therefore equivalent given the preceding conditions):*

*a) The fibers of $H$ are of multiplicative type, and of constant type on each connected component of $S$.*

*b) $H$ is commutative and the ${}_{n} H$ ($n > 0$) are finite over $S$.*

*These last conditions are also implied by the following:*

*c) The fibers of $H$ are connected.*

Of course, if $H$ is of multiplicative type (and isotrivial), conditions a) and b) are verified by IX 1.4.1 a) and 2.1
c), so only the "if" requires proof. We shall use the subgroup $G$ indicated in 3.7. When condition c) is satisfied, one
obviously has $G = H$ and we are done.

In case b), one notes that the immersion $u : G \to H$ induces an open immersion

```text
_n u : _n G ⟶ _n H
```

which induces an isomorphism $({}_{n} G)_{0} \xrightarrow{\sim} ({}_{n} H)_{0}$; since ${}_{n} H$ is finite over $S$,
this implies at once that ${}_{n} u$ is an isomorphism (the complement of its image is finite over $S$ and reduces to
$\emptyset$). By 3.6 it follows that the morphisms induced on fibers $u_{s} : G_{s} \to H_{s}$ are isomorphisms, so $u$
is surjective, hence an isomorphism.

Finally, in case a), one may assume $S$ connected,[^N.D.E-X-18] and it follows that for every $s \in S$, $u_{s} : G_{s}
\to H_{s}$ is a monomorphism of algebraic groups of multiplicative type and of the same type over
$\kappa(s)$.[^N.D.E-X-19] I claim that such a homomorphism is necessarily an isomorphism (which will again complete the
proof[^N.D.E-X-20]). Indeed, one may suppose, possibly extending the base field, that the two groups over $\kappa(s)$
are diagonalizable, and then this follows from VIII 3.2 b) and from the fact that a surjective homomorphism of
isomorphic finitely generated $\mathbb{Z}$-modules $M \to N$ is necessarily bijective.

**Corollary 3.9.** *Let $A$ be a noetherian ring equipped with an ideal $I$ such that $A$ is separated and complete for
the $I$-adic topology, and let $H$ be an $S$-prescheme in groups of finite type, affine and flat over $S$, with
connected fibers.*

<!-- label: III.X.3.9 -->

<!-- original page 92 -->

*For $H$ to be an isotrivial torus, it is necessary and sufficient that `H_0` be so.*

## 4. Case of an arbitrary base. Quasi-isotriviality theorem

Let $A$ be a local ring. Recall that one says, after Nagata, that $A$ is *henselian* if every algebra $B$ finite over
$A$ is a product of local algebras $B_{i}$ finite over $A$.

**Recall 4.0.**[^N.D.E-X-21] *Let $A$ be a henselian local ring, $k$ its residue field, $S = \operatorname{Spec}(A)$,
$S_{0} = \operatorname{Spec}(k)$, and $\xi$ a geometric point of `S_0`. Then, the functor*

<!-- label: III.X.4.0 -->

```text
X ↦ X_0 = X ×_S S_0
```

*is an equivalence between the category of étale covers of $S$ and the analogous category over `S_0` (cf. [EGA IV₄, §
18.5](https://jcreinhold.github.io/ega/iv/31-ch4-18-complements-etale-morphisms.html#185-henselian-local-rings1)).
Consequently (cf. SGA 1, V), one has $\pi_{1}(S_{0}, \xi) = \pi_{1}(S, \xi)$.*

Suppose moreover $A$ noetherian and denote by $A'$ its completion, $S' = \operatorname{Spec}(A')$. Then $A'$ is a
complete noetherian local ring, hence henselian (loc. cit., 18.5.14), and the functor

```text
X ↦ X′ = X ×_S S′,
```

from the category of étale covers of $S$ to the analogous category over $S'$, fits into a commutative diagram

```text
                Rev.ét.(S)  ⟶  Rev.ét.(S′)
                       ↘        ↙
                      ≃   ↘   ↙  ≃
                            Rev.ét.(S_0)
```

so is also an equivalence of categories, whence $\pi_{1}(S_{0}, \xi) = \pi_{1}(S', \xi)$.

**Remark 4.0.1.** Since $S$ is connected ($A$ being local), it follows from 1.2 that the category of isotrivial groups
of multiplicative type over $S$ is equivalent to the analogous category over `S_0` (and also over $S'$ if moreover $A$
is noetherian).

<!-- label: III.X.4.0.1 -->

**Lemma 4.1.** *Let $A$ be a henselian local ring with residue field $k$, $S = \operatorname{Spec}(A)$, $S_{0} =
\operatorname{Spec}(k)$.*

<!-- label: III.X.4.1 -->

*(i) The functor*

```text
H ↦ H_0 = H ×_S S_0
```

*is an equivalence between the category of finite groups of multiplicative type over $S$ and* <!-- original page 93 -->
*the analogous category over `S_0`.*

*(ii) If moreover $A$ is noetherian, denoting by $A'$ its completion and $S' = \operatorname{Spec}(A')$, the functor*

```text
H ↦ H′ = H ×_S S′
```

*is an equivalence between the category of finite groups of multiplicative type over $S$ and the analogous category over
$S'$.*

As in 4.0, the second assertion is a consequence of the first; let us prove the latter. One already knows that the
functor under consideration is essentially surjective, since every group of multiplicative type `H_0` over $S_{0} =
\operatorname{Spec}(k)$, finite hence of finite type over $k$, is isotrivial by 1.4, hence comes from an isotrivial
group of multiplicative type over $S$ by 4.0.1.

It remains to prove full faithfulness, i.e. that for two finite groups $G$, $H$ of multiplicative type over $S$, the map
below is bijective:

```text
Hom_{S-gr.}(G, H) ⟶ Hom_{S_0-gr.}(G_0, H_0),
```

i.e.,[^N.D.E-X-22] denoting by $F$ the $S$-functor $\operatorname{Hom}_{S-gr.}(G, H)$, that the natural map

```text
Hom_S(S, F) ⟶ Hom_{S_0}(S_0, F_0)
```

induced by the base change $S_{0} \to S$ is bijective. For this, given recall 4.0, it suffices to prove:

**Lemma 4.2.** *Let $G$, $H$ be two finite groups of multiplicative type over a prescheme $S$. Then $F =
\operatorname{Hom}_{S-gr.}(G, H)$ is representable by a finite étale scheme over $S$.*

<!-- label: III.X.4.2 -->

[^N.D.E-X-23] Let $f : S' \to S$ be a faithfully flat quasi-compact morphism such that $G'$ and $H'$ are diagonalizable.
It suffices to show that $F_{S'}$ is representable by a preschem $X'$ étale and finite (hence affine) over $S'$, since
the descent datum on $X'$ relative to $f$ (cf. VIII 1.7.2) will then be effective (by SGA 1 VIII, 2.1), whence the
existence of an $S$-prescheme $X$ such that $X \times_{S} S' = X'$, which represents $F$, and is étale and finite over
$S$ (cf. SGA 1, V 5.7 and
[EGA IV₄, 17.7.3](https://jcreinhold.github.io/ega/iv/30-ch4-17-smooth-unramified-etale-morphisms.html#177-descent-properties-passage-to-the-limit-and-constructibility)
(ii)).

One may therefore suppose that $G = D_{S}(M)$ and $H = D_{S}(N)$, where $M$ and $N$ are finite commutative groups (cf.
VIII 2.1 c)). Then, <!-- original page 94 --> $K = \operatorname{Hom}_{gr.}(N, M)$ is a finite abelian group and, by
VIII 1.5, one has an isomorphism

$$ \operatorname{Hom}_{S-gr.}(G, H) \simeq K_{S}, $$

which completes the proof of 4.2 and hence of 4.1.

**Proposition 4.3.0.**[^N.D.E-X-24] *Let $S$ be a henselian local scheme, $s$ its closed point, $g : X \to S$ a morphism
locally of finite type, $x$ an isolated point of the fiber $X_{s}$.*

<!-- label: III.X.4.3.0 -->

*(i) Then $O_{X,x}$ is finite over $O_{S,s}$. (In particular, if the residue extension $\kappa(x)/\kappa(s)$ is trivial,
then $O_{S,s} \to O_{X,x}$ is surjective, by Nakayama's lemma.)*

*(ii) If moreover $g$ is separated, then $X' = \operatorname{Spec}(O_{X,x})$ is an open and closed subscheme of $X$,
i.e. one has a decomposition as a disjoint sum $X = X' \sqcup X''$.*

*Proof.* By the local form of Zariski's main theorem given in [Pes66], or [Ray70, Ch. IV, Th. 1], $x$ has an affine open
neighborhood $U = \operatorname{Spec}(B)$ of finite type and quasi-finite over $A = O_{S,s}$, and there exists an open
immersion $U \hookrightarrow Y = \operatorname{Spec}(C)$, where $C$ is a finite $A$-algebra. (N.B. to reach this
conclusion, one may also use Chevalley's semi-continuity theorem
([EGA IV₃, 13.1.4](https://jcreinhold.github.io/ega/iv/25-ch4-13-equidimensional-morphisms.html#131-chevalleys-semi-continuity-theorem)),
then the form of Zariski's main theorem given in loc. cit., 8.12.8.)

Since $A$ is henselian, $Y$ is the disjoint sum of local schemes $Y_{1}, \cdots, Y_{n}$, each finite over $S$, and the
points of $Y$ above $s$ are the closed points $y_{1}, \cdots, y_{n}$. Therefore $x = y_{i}$ for some $i$, and $O_{X,x} =
O_{U,x} = C_{i}$ is finite over $A$. Moreover, $X' = C_{i}$ is an open subscheme of $U$ hence of $X$.

Suppose moreover $g$ separated. Then, since the morphism $X' \to S$ is finite ($C_{i}$ being finite over $A$), so is the
immersion $X' \to X$ (cf.
[EGA II, 6.1.5](https://jcreinhold.github.io/ega/ii/02-06-integral-finite-morphisms.html#61-preschemes-integral-over-another)
(v)), so $X'$ is also closed in $X$.

**Lemma 4.3.** *Let $A$ be a noetherian henselian local ring, $A'$ its completion, $S = \operatorname{Spec}(A)$, $S' =
\operatorname{Spec}(A')$, $s$ the closed point of $S$, $G$ and $H$ two $S$-preschemes in groups, with $G$ of
multiplicative type and of finite type over $S$, $H$ locally of finite type and separated over $S$, $H_{s}$ of
multiplicative type, and $H$ flat over $S$ at the points of $H_{s}$.*

<!-- label: III.X.4.3 -->

*Let $G'$, $H'$ be deduced from $G$, $H$ by the base change $S' \to S$. Then the natural map below is bijective:*

```text
Hom_{S-gr.}(G, H) ⥲ Hom_{S′-gr.}(G′, H′).
```

Since $S'$ is faithfully flat and quasi-compact over $S$, one knows by SGA 1, VIII 5.2 that this map is a bijection of
the first member onto the part of the second formed by the $u' : G' \to H'$ such that the two inverse images $u''_{1}$,
$u''_{2} : G'' \to H''$ of $u'$ on $S'' = S' \times_{S} S'$ (by the projections $pr_{1}$, $pr_{2}$ of $S''$ onto $S'$)
are equal.

Therefore everything reduces to proving that for every homomorphism of $S'$-groups $u' : G' \to H'$, one has $u''_{1} =
u''_{2}$. By the density theorem IX 4.8 it suffices to prove that $u''_{1}$ and $u''_{2}$ coincide on ${}_{n} G''$ for
every integer $n > 0$. (N.B. one needs here in an essential way the density theorem in a case where the base prescheme,
here $S''$, is not locally noetherian.)

This reduces us, replacing $G$ by ${}_{n} G$, to the case where there exists an integer $n > 0$ such that $n \cdot
id_{G} = 0$, hence where $G$ is finite over $S$. Let likewise ${}_{n} H$ be the kernel of the $n$-th power morphism
$\phi_{n}$ in $H$. (N.B. we have not assumed $H$ commutative, so $\phi_{n}$ (resp. ${}_{n} H$) is not necessarily a
homomorphism of groups (resp. a subgroup of $H$).) Since ${}_{n} H$ is defined as the fibered product of $\phi_{n} : H
\to H$ <!-- original page 95 --> and the unit section $\epsilon : S \to H$, its formation commutes with every base
change $T \to S$, i.e. one has $({}_{n} H)_{T} = {}_{n} (H_{T})$.

[^N.D.E-X-25] We denote by an index $m$ on the right the reductions modulo $m^{m+1}$, where $m$ is the maximal ideal of
$A$. Then $H_{m}$ is flat over $S_{m}$ (since $H$ is so over $S$ at the points of `H_0`); therefore, by 2.4, since `H_0`
is of multiplicative type and of finite type, so is $H_{m}$. Therefore each $({}_{n} H)_{m} = {}_{n} (H_{m})$ is a
subgroup of $H_{m}$, of multiplicative type, finite and flat over $S_{m}$.

In particular, $({}_{n} H)_{0} = {}_{n} (H_{0})$ is finite over `S_0`; since $S$ is henselian local and ${}_{n} H$ is
(like $H$) locally of finite type and separated over $S$, then, by 4.3.0, <!-- original page 77 --> the local rings of
${}_{n} H$ at the points of $({}_{n} H)_{0}$ are finite over $S$ and one has a decomposition as a disjoint sum of open
sets

```text
(∗)    _n H = _n H⁺ ⊔ _n H⁻,
```

where $Z = {}_{n} H^{+}$ is finite over $S$, and ${}_{n} H^{-}$ lies above $S - {s}$.

Note that, for every finite $S$-scheme $Y$ (such as $G$), every $S$-morphism $Y \to {}_{n} H$ factors through $Z$, and
that the formation of the decomposition $(\ast)$ commutes with the base change $S' \to S$ (where $S' =
\operatorname{Spec}(A')$, $A'$ the completion of $A$).

Then $Z' = Z \times_{S} S'$ is a finite scheme over $S'$, as is $P' = Z' \times_{S'} Z'$. Denote by $\nu$ the
restriction to $P'$ of the multiplication of $H'$ and by $\sigma$ the automorphism of $P'$ which exchanges the two
factors. Since $P'$ is finite over $S'$ and $H'$ separated and locally of finite type over $S'$, then, by [EGA II 5.4.3](https://jcreinhold.github.io/ega/ii/02-05-quasi-affine-quasi-projective-morphisms.html#54-proper-morphisms-and-universally-closed-morphisms)
and IV₁ 1.1.3, $Y = \nu(P')$ is a closed subscheme of $H'$, universally closed and quasi-compact, hence of finite type,
hence proper over $S'$. Moreover, $Y \to S'$ has finite fibers (since $P' \to S'$ does). Therefore, since $S'$ is
noetherian, the morphism $Y \to S'$ is finite (cf. [EGA III, 4.4.2](https://jcreinhold.github.io/ega/iii/11-ch3-04-fundamental-theorem-proper-morphisms.html#44-zariskis-main-theorem)). Since $Z' \subseteq Y$ and $Z'_{m} = Y'_{m}$ for
every $m$, then $Z' = Y$, by lemma IX 5.0, so $Z'$ is a subgroup of $H'$. Likewise, the kernel $K = Ker(\nu, \nu \circ
\sigma)$ is a closed subscheme of $P'$, such that $K_{m} = P'_{m}$ for every $m$ (since $Z'_{m} = {}_{n} H_{m}$ is
commutative), so $K = P'$, i.e. $Z'$ is a commutative subgroup of $H'$.

On the other hand, since each reduction $Z'_{m} = {}_{n} H_{m}$ is flat over $S_{m}$, then, by the "local criterion of
flatness" (cf. [EGA 0_III, 10.2.2](https://jcreinhold.github.io/ega/iii/03-ch0-10-complements-flat-modules.html#102-local-criteria-of-flatness) or [BAC], III § 5, Example 1 and Th. 1), $Z'$ is flat over $S'$. Since moreover $Z'_{0}
= {}_{n} H_{0}$ is a finite group of multiplicative type over `S_0`, hence isotrivial by 1.4, then $Z'$ is of
multiplicative type (and isotrivial) over $S'$, by 3.8 b). Since $S' \to S$ is faithfully flat and quasi-compact, one
deduces that the multiplication $Z \times_{S} Z \to H$ factors through $Z$ and makes $Z$ a subgroup of $H$, finite over
$S$ and of multiplicative type (since $Z'$ is).

Finally, by the remarks made above on decomposition $(\ast)$, $Z'$ is the "finite part" of ${}_{n} H'$, and so the
morphism $u' : G' \to {}_{n} H'$ takes its values in $Z'$. Since $Z$ is of multiplicative type and finite over $S$, as
is $G = {}_{n} G$, then, by 4.1, $u'$ comes from a $u : G \to Z$, and therefore $u''_{1} = u''_{2}$. This completes the
proof of 4.3.

**Lemma 4.4.0.**[^N.D.E-X-26] *Let $A$ be a ring, $S = \operatorname{Spec}(A)$, $H$ an $S$-group scheme of
multiplicative type and of finite type, quasi-isotrivial (resp. isotrivial), $(A_{i})$ a filtered family of subrings of
$A$ of which $A$ is the inductive limit, $S_{i} = \operatorname{Spec}(A_{i})$.*

<!-- label: III.X.4.4.0 -->

*Then there exist an index $i$ and an $S_{i}$-group scheme $H_{i}$ of multiplicative type and of finite type,
quasi-isotrivial (resp. isotrivial), such that $H = H_{i} \times_{S_{i}} S$.*

**Theorem 4.4.** *Let $S$ be a prescheme, $H$ an $S$-prescheme in groups affine and of finite presentation over $S$, and
$s \in S$. Assume:*

<!-- label: III.X.4.4 -->

*α) $H$ is flat over $S$ at the points of $H_{s}$.*

*β) $H_{s}$ is of multiplicative type.*

*Then there exist an étale morphism $S' \to S$, a point $s'$ of $S'$ above $s$ such that the extension $\kappa(s')/\kappa(s)$ is
trivial, and an open and closed subgroup $G'$ of $H' = H \times_{S} S'$,* <!-- original page 96 --> *of multiplicative type and
of finite type, isotrivial, such that $G'_{s'} = H'_{s'}$.*

[^N.D.E-X-27] **a)** Let us provisionally denote $T = \operatorname{Spec}(O_{S,s})$ and show that, by "descent of
conclusions", one can reduce to the case where $S = T$. Indeed, suppose we have found an étale morphism $g : T' \to T$,
a point $s' \in T'$ and a subgroup $G'$ of $H' = H_{T'}$ satisfying the conditions of the statement; replacing $T'$ by
an affine open neighborhood of $s'$, one may suppose $T'$ of finite presentation over $T$.

Since $G'$ is isotrivial, there exists an étale finite surjective morphism $f : \tilde{T} \to T'$ such that $\tilde{G} =
G' \times_{T'} \tilde{T}$ is isomorphic to $D_{\tilde{T}}(M)$, where $M$ is a finitely generated abelian group. Since
$T'$, $H$, and $\tilde{T}$, $G'$ are of finite presentation over $T = \operatorname{Spec}(O_{S,s})$, and $O_{S,s}$ is
the inductive limit of the subalgebras $A_{i} = O_{S}(S_{i})$, where $S_{i}$ runs through the affine open neighborhoods
of $s$ in $S$, then, by
[EGA IV₃, 8.8.2](https://jcreinhold.github.io/ega/iv/21-ch4-08-projective-limits.html#88-preschemes-of-finite-presentation-over-a-projective-limit-of-preschemes)
(and Exp. VI_B, 10.2 and 10.3), there exist an index $i$, $S_{i}$-preschemes (resp. an $S_{i}$-prescheme in groups) of
finite presentation $S'_{i}$ and $\tilde{T}_{i}$ (resp. $G'_{i}$), and morphisms $g_{i} : S'_{i} \to S_{i}$ and
$f_{i} : \tilde{T}_{i} \to S'_{i}$ (resp. a morphism of $S_{i}$-preschemes in groups
$u_{i} : G'_{i} \to H \times_{S} S'_{i}$), from which $f$ and $g$ (resp. $u : G' \to H'$) come by the base change
$T' \to S_{i}$. Moreover, taking $i$ large enough, $g_{i}$ will be étale, $f_{i}$ étale finite surjective, and $u_{i}$
an open and closed immersion (cf.
[EGA IV, 8.10.5](https://jcreinhold.github.io/ega/iv/21-ch4-08-projective-limits.html#810-permanence-properties-of-morphisms-under-projective-passage-to-the-limit)
and 17.7.8).

Then, $\tilde{G}$ comes from the groups $\tilde{G}_{i} = G_{i} \times_{S_{i}} \tilde{T}_{i}$ and $D_{\tilde{T}_{i}}(M)$;
therefore, by EGA IV₃, 8.8.2 (i) (and VI_B, 10.2), there exists an index $j \geqslant i$ such that $\tilde{G}_{j} \simeq
D_{\tilde{T}_{j}}(M)$, so $G_{j}$ is of isotrivial multiplicative type. Denote by $s'_{j}$ the image of $s'$ in
$S'_{j}$. Then the étale morphism $S'_{j} \to S_{j} \hookrightarrow S$, the point $s'_{j}$ and the open and closed
subgroup $G'_{j}$ of $H \times_{S} S'_{j}$, verify the conditions of the statement. This shows that one may suppose $S =
\operatorname{Spec}(A)$ local, with closed point $s$.

**b)** Then, $A$ is the inductive limit of local rings $A_{i}$ which are localizations of $\mathbb{Z}$-algebras of
finite type; denote $S_{i} = \operatorname{Spec}(A_{i})$. Let us show that the hypotheses α) and β) "descend" to some
$A_{i}$. Since $H \to S$ is of finite presentation, the set of $x \in H$ such that $H$ is flat over $S$ at $x$ is an
open set $W$, which contains $H_{s}$ by hypothesis, hence contains a quasi-compact open set $V$ containing $H_{s}$
(since $H_{s}$ being affine, one can cover it by a finite number of affine open sets contained in $W$). Then the open
immersion $\tau : V \hookrightarrow H$ is of finite presentation, so $V \to S$ is too.

Therefore, by EGA IV₃, 8.8.2 (and Exp. VI_B, 10.2 and 10.3), there exist an index $i$, an $S_{i}$-prescheme $V_{i}$
(resp. an $S_{i}$-prescheme in groups $H_{i}$) of finite presentation over $S_{i}$, and an $S_{i}$-morphism $\tau_{i} :
V_{i} \to H_{i}$ from which $V$, $H$ and $\tau$ come by base change $S \to S_{i}$; moreover, taking $i$ large enough,
$\tau_{i}$ will be an open immersion and $V_{i}$ will be flat over $S_{i}$, by EGA IV₃, 8.10.5 and 11.2.6. Denote by
$s_{i}$ the image of $s$ in $S_{i}$; since the open immersion $(V_{i})_{s_{i}} \hookrightarrow (H_{i})_{s_{i}}$ gives,
by the base change $\kappa(s_{i}) \to \kappa(s)$, the equality $V_{s} = H_{s}$, one already has $(V_{i})_{s_{i}} =
(H_{i})_{s_{i}}$, i.e. $(H_{i})_{s_{i}} \subseteq V_{i}$, so $H_{i}$ is flat over $S_{i}$ at the points of
$(H_{i})_{s_{i}}$. Finally, $(H_{i})_{s_{i}}$ is of multiplicative type, since $H_{s} = (H_{i})_{s_{i}}
\otimes_{\kappa(s_{i})} \kappa(s)$ is. Therefore the triple $(S_{i}, H_{i}, s_{i})$ verifies the hypotheses of 4.4, and
if the desired assertion is verified for this triple, it will also be verified, by base change, for $(S, H, s)$. This
reduces us to the case where $A$ is local and noetherian. Let us now distinguish two cases.

**1°)** $A$ *is local noetherian and henselian.* <!-- original page 79 --> Let `Â` be its completion, $\hat{S} =
\operatorname{Spec}(\hat{A})$, and $\hat{H} = H \times_{S} \hat{S}$. Applying theorem 3.7, one finds an `Ŝ`-group `Ĝ` of
multiplicative type, isotrivial and of finite type, and a homomorphism of `Ŝ`-groups

$$ \hat{u} : \hat{G} \longrightarrow \hat{H} $$

which is an open immersion and a closed immersion, such that `û` induces an isomorphism $\hat{u}_{0} : \hat{G}_{0}
\xrightarrow{\sim} \hat{H}_{0}$.

By remark 4.0.1, the base change functor by $\hat{S} \to S$ induces an equivalence between the category of isotrivial
groups of multiplicative type over $S$, and over `Ŝ`; in particular `Ĝ` "comes from" an $S$-group of multiplicative type
$G$, isotrivial and of finite type. By 4.3, `û` comes from a homomorphism

$$ u : G \longrightarrow H; $$

moreover $u$ is an open and closed immersion and induces an isomorphism $u_{0} : G_{0} \to H_{0}$, since this is so
after the faithfully flat quasi-compact base change $\hat{S} \to S$. This therefore proves 4.4 in this case (taking of
course, in the conclusion of 4.4, $S' = S$ and $s' = s$).

**2°)** $A$ *is local noetherian.* The reduction to case 1°) is immediate, by applying 1°) to the "henselized" ring
$A^{h}$ of $A$. More precisely, one sees easily (using SGA 1, I § 5[^X-4-1]) that the local rings $O_{S',s'}$ of the
$S$-preschemes étale $S'$ equipped with a point $s'$ above $s$ such that $\kappa(s')/\kappa(s)$ is trivial, form a
filtered inductive system, whose inductive limit is a noetherian henselian local ring $A^{h}$ (called the "henselized"
ring of $A$); for details of this construction (due to Nagata in the normal case), cf. SGA 4, VIII § 4[^X-4-1]. The
sorites of
[EGA IV₃ § 8](https://jcreinhold.github.io/ega/iv/21-ch4-08-projective-limits.html#8-projective-limits-of-preschemes)
then allow, <!-- original page 97 --> as in part a) of the proof, to deduce from a known result on the inductive limit
$A^{h}$ of the $O_{S',s'}$, an analogous result on one of the $(S', s')$, which proves 4.4.

**Corollary 4.5.** *Let $S$ be a prescheme, $H$ an $S$-prescheme in groups of multiplicative type and of finite type.
Then $H$ is quasi-isotrivial, i.e. is split by an étale surjective morphism $S' \to S$.*

<!-- label: III.X.4.5 -->

Indeed, let $s \in S$. By 4.4, there exist an étale morphism $S' \to S$, an $s' \in S'$ above $s$ such that $\kappa(s) =
\kappa(s')$, and a subgroup $G'$ of $H'$, of isotrivial multiplicative type and of finite type, such that $G'_{s'} =
H'_{s'}$. Since $G'$ and $H'$ are of multiplicative type and of finite type, then, by IX 2.9, there exists an open
neighborhood $U'$ of $s'$ such that $G'|U' = H'|U'$.

[^N.D.E-X-28] Suppose moreover $S$ local henselian, with closed point $s$; then, by [EGA IV₄, 18.5.11](https://jcreinhold.github.io/ega/iv/31-ch4-18-complements-etale-morphisms.html#185-henselian-local-rings1) b), there exists a
section $\sigma$ of $S' \to S$ such that $\sigma(s) = s'$. (N.B. one can see directly that $B = O_{S',s'}$ equals $A =
O_{S,s}$ as follows: by 4.3.0 (i), one has $B \simeq A/I$, and since $B$ is a finitely presented and flat $A$-algebra,
$I$ is a finitely generated ideal <!-- original page 80 --> (cf. [EGA IV₁, 1.4.7](https://jcreinhold.github.io/ega/iv/12-ch4-01-relative-finiteness-conditions.html#14-morphisms-locally-of-finite-presentation)), and $I = I m$ (where $m$ is the
maximal ideal of $A$), whence $I = 0$.) Therefore $H$ is already isotrivial. One thus obtains:

**Corollary 4.6.** *Let $A$ be a henselian local ring, $k$ its residue field, and $\pi$ the topological Galois group of
an algebraic closure of $k$.*

<!-- label: III.X.4.6 -->

*(i) Every group of multiplicative type and of finite type over $S = \operatorname{Spec}(A)$ is isotrivial.*

*(ii) The category of these groups over $S$ is equivalent (via the functor $H \mapsto H \otimes_{A} k$) to the analogous
category over $S_{0} = \operatorname{Spec}(k)$; it is therefore anti-equivalent, by 1.4, to the category of Galois
modules under $\pi$ which are of finite type as $\mathbb{Z}$-modules.*

**Corollary 4.7.** *Under the conditions of 4.4 suppose moreover that one of the following conditions is verified:*

<!-- label: III.X.4.7 -->

*a) For every generization $t$ of $s$, $H_{t}$ is of multiplicative type and of the same type as $H_{s}$.*

*b) $H$ is commutative and the ${}_{n} H$ ($n > 0$) are finite over $S$ in a neighborhood of $s$.*

*c) For every generization $t$ of $s$, the fiber $H_{t}$ is connected.*

*Then there exists an open neighborhood $U$ of $s$ such that $H|U$ is of multiplicative type.*

<!-- original page 98 -->

Taking into account that an étale morphism is open, one is reduced to proving that there exists (with the notations of
the conclusion of 4.4) an open neighborhood $U'$ of $s'$ such that $G'|U' = H'|U'$. Set $S'' =
\operatorname{Spec}(O_{S',s'})$; since $G'$ and $H'$ are of finite presentation over $S'$, it suffices to show, by EGA
IV₃, 8.8.2, that $G'' = H''$. We may therefore suppose $S = S''$, and then hypotheses (a), (b), (c) become those of the
lemma below, whose proof is the same as that of 3.8:

**Lemma 4.7.1.** *Let $S$ be a local scheme, $s$ its closed point, $H$ an $S$-group scheme of finite type, $G$ an open
and closed subgroup of $H$, of multiplicative type, such that $G_{s} = H_{s}$. Suppose moreover one of the following
conditions verified:*

<!-- label: III.X.4.7.1 -->

*a) The fibers of $H$ are of multiplicative type and of the same type as $H_{s}$.*

*b) $H$ is commutative and the ${}_{n} H$ ($n > 0$) are finite over $S$.*

*c) The fibers of $H$ are connected.*

*Then $G = H$.*

**Corollary 4.8.** *Let $S$ be a prescheme, $H$ an $S$-prescheme in groups affine, flat and of finite presentation over
$S$, with fibers of multiplicative type.*

<!-- label: III.X.4.8 -->

*For $H$ to be of multiplicative type, it is necessary and sufficient that it satisfy one of the two following
conditions (equivalent given the preceding conditions):*

*a) The type of $H_{s}$ (cf. IX 1.4) is a locally constant function of $s \in S$.*

*b) $H$ is commutative, and the ${}_{n} H$ ($n > 0$) are finite over $S$.*

*Moreover, these conditions a), b) are implied by the following:*

*c) The fibers of $H$ are connected.*

In particular, one finds:

**Corollary 4.9.** *Let $S$ be a prescheme, $H$ an $S$-prescheme in groups flat and of finite presentation over $S$.
Suppose moreover $H$ affine over $S$ and with connected fibers.[^N.D.E-X-29] If $s \in S$ is such that $H_{s}$ is a
torus, there exists an open neighborhood $U$ of $s$ such that $H|U$ is a torus.*

<!-- label: III.X.4.9 -->

<!-- original page 81 -->

*In particular, if all the fibers of $H$ are tori, $H$ is a torus.*

## 5. Scheme of homomorphisms from one group of multiplicative type to another. Twisted constant groups and groups of multiplicative type

**Definition 5.1.** *a) Let $S$ be a prescheme, $R$ a prescheme in groups over $S$. One says that $R$ is a* twisted
constant group *over $S$ if it is locally isomorphic, in the sense of the faithfully flat quasi-compact topology, to a
constant group scheme, i.e. of the form `M_S` with $M$ an ordinary group.*

<!-- label: III.X.5.1 -->

<!-- original page 99 -->

*b) One says that the twisted constant group $R$ over $S$ is* quasi-isotrivial, resp. isotrivial, resp. locally
isotrivial, resp. locally trivial, resp. trivial, *if in the definition above one can replace the faithfully flat
quasi-compact topology by the étale topology, resp. the global finite étale topology, resp. the finite étale topology,
resp. the Zariski topology, resp. the coarsest (or "chaotic") topology, cf. IX 1.1 and 1.2, and IV 6.6.*

*To say that $R$ is quasi-isotrivial (resp. isotrivial) thus means that there exists an étale surjective (resp. and
finite) morphism $S' \to S$ such that $R' = R \times_{S} S'$ is a constant group over $S$; to say that it is trivial
means that $R$ is a constant group.*

*c) One defines as in VIII 1.4 the* type *of a twisted constant group $R$ over $S$ at an $s \in S$; it is a class of
ordinary groups up to isomorphism, which for variable $s$ is a locally constant function of $s$, hence constant if $S$
is connected. One will also say that $R$ is "of type $M$" if all the fibers of $R$ are of type $M$.*

*Beware that $R$ is quasi-compact over $S$ only if it is finite over $S$, i.e. if its type at every $s \in S$ is a
finite group.*[^N.D.E-X-30]

*d) The case most interesting for us is that where $R$ is commutative. We shall then say that $R$ is "*finitely
generated*" if its type at each point $s \in S$ is given by a finitely generated $\mathbb{Z}$-module, a notion which
should not be confused with the schematic notion "$R$ of finite type over $S$" (cf. above).*

**Remark 5.2.** We shall also have to consider $S$-preschemes $X$ which are locally isomorphic (for the faithfully flat
quasi-compact topology) to constant preschemes, independently of any group structure. We shall then say that $X$ is a
*twisted constant bundle* over $S$, and we extend to these preschemes the terminology introduced in 5.1. Of course one
will note that when $X$ is endowed with an $S$-group structure, the meaning of the expressions "twisted constant",
"isotrivial" etc. changes, depending on whether one takes into account or not the group structure over $S$. The same
holds if one considers <!-- original page 100 --> on $X$ any other species of algebraic structure (for example that of
Galois principal bundle that will be considered in the following number).

<!-- label: III.X.5.2 -->

**Proposition 5.3.** *Let $R$ be a commutative twisted constant group over $S$.*

<!-- label: III.X.5.3 -->

*(i) The functor $H = D_{S}(R)$ (cf. VIII 1) is representable and is a group of multiplicative type over $S$.*

*(ii) For every $s \in S$, the type of $R$ at $s$ equals that of $H$ at $s$.*

*(iii) For $R$ to be quasi-isotrivial (resp. isotrivial, resp. trivial, resp. locally isotrivial, resp. locally
trivial), it is necessary and sufficient that $H$ be so.*

**Remark 5.3.1.**[^N.D.E-X-31] One may worry about seeing in 5.3 the term "type" used in two different senses depending
on whether we speak of $R$ or $H$; fortunately, when an $S$-prescheme in groups $G$ is at the same time a twisted
constant group and of multiplicative type, its type in either sense is the same, thanks to the fact that a finite
ordinary commutative group is isomorphic to its dual!

<!-- label: III.X.5.3.1 -->

*Proof.* Since the families covering for the faithfully flat quasi-compact topology are families of effective descent
for the fibered category of affine preschemes in groups over variable base preschemes (SGA 1, VIII 2.1), one sees that
$H$ is representable (and is affine over $S$), since it is so "locally"[^N.D.E-X-32] (because it is so when $R$ is
constant, and then $H$ is a diagonalizable group).

The fact that $H$ is of multiplicative type is then evident by definition, as is the fact that the type of $R$ and $H$
at $s \in S$ is the same. Finally, since $H_{S'} = D_{S'}(R_{S'})$, the last assertion is reduced to the "trivial" case,
i.e. to verifying that $R$ is trivial if and only if $H$ is, which follows at once from the biduality theorem VIII 1.2.

To finish making precise the correspondence between twisted constant groups and groups of multiplicative type, one must
start from a group of multiplicative type $H$, and study $R = D_{S}(H)$. If the latter is representable, it is obviously
a twisted constant group, and one will have $H \simeq D_{S}(R)$. In other words:

**Scholie 5.4.0.** *The functor $R \mapsto D_{S}(R)$ is an anti-equivalence[^N.D.E-X-33] between the category of twisted
constant groups over $S$ and that of groups of multiplicative type $H$ over $S$ such that $D_{S}(H)$ is representable.*

<!-- label: III.X.5.4.0 -->

<!-- original page 101 -->

I do not know whether this condition on $H$ is always satisfied; we shall see however that it is satisfied when $H$ is
quasi-isotrivial, in particular when $H$ is of finite type.

**Lemma 5.4.** *Let $S' \to S$ be a faithfully flat morphism locally of finite presentation, $X'$ an $S'$-prescheme
separated, locally of finite presentation and locally quasi-finite over $S'$.*

<!-- label: III.X.5.4 -->

*Then every descent datum on $X'$ relative to $S' \to S$ is effective, i.e. there exists an $S$-prescheme $X$, and an
$S'$-isomorphism $X \times_{S} S' \simeq X'$ compatible with the descent datum.*

We have already noted that the hypothesis on $S' \to S$ implies that it is a morphism covering for the faithfully flat
quasi-compact topology (IV 6.3.1 (iv)), *a fortiori* a morphism of effective descent.

When $X' \to S'$ is quasi-compact, hence of finite presentation and quasi-finite, then it is a quasi-affine morphism
(cf. SGA 1, VIII 6.2[^N.D.E-X-34]), and effectivity follows in this case from SGA 1, VIII 7.9. In the general case, one
reduces at once to the case where $S$ and $S'$ are affine. One covers $X'$ by affine open sets $U'_{i}$; let $V'_{i}$ be
the saturation of $U'_{i}$ for the equivalence relation in $X'$ defined by the descent datum, i.e. $V'_{i} =
q_{2}(q^{-1}_{1}(U'_{i}))$, where $q_{1}$, $q_{2}$ are the two projections of $X''_{1} = X' \times_{S'} (S'', p_{1})$
onto $X'$ ($q_{1} = pr_{1}$, and $q_{2}$ is deduced from the first projection of $X''_{2} = X' \times_{S'} (S'', p_{2})$
thanks to the given descent isomorphism $X''_{1} \simeq X''_{2}$). Since $S' \to S$ is faithfully flat quasi-compact
locally of finite presentation, the same holds for $p_{1} : S'' = S' \times_{S} S' \to S'$, hence also for $q_{1}$ and
$q_{2}$, which are consequently open morphisms (SGA 1 IV 6.6[^N.D.E-X-35]). Consequently, $V'_{i}$ is an open and
quasi-compact part of $X'$. By what we have already seen, the descent data induced on the $V'_{i}$ are effective, whence
it follows that the descent datum on $X'$ is so (SGA 1, VIII 7.2).

**Corollary 5.5.** *A faithfully flat morphism of finite presentation $S' \to S$ is a morphism of effective descent for
the fibered category of twisted constant groups (over variable base preschemes).*

<!-- label: III.X.5.5 -->

<!-- original page 102 -->

Indeed, this amounts to asserting the effectivity of a descent datum under the conditions of 5.4, when $X'$ is a
constant $S'$-prescheme.

**Theorem 5.6.** *Let $S$ be a prescheme, $G$ and $H$ two $S$-preschemes in groups of quasi-isotrivial multiplicative
type, with $G$[^N.D.E-X-36] of finite type.*

<!-- label: III.X.5.6 -->

*Then $\operatorname{Hom}_{S-gr.}(H, G)$ is representable by, and is a quasi-isotrivial twisted constant group over
$S$;*[^N.D.E-X-37] *for every $s \in S$, if the type at $s$ of $G$ (resp. $H$) is $M$ (resp. $N$), that of
$\operatorname{Hom}_{S-gr.}(H, G)$ is $\operatorname{Hom}_{gr.}(M, N)$.*

One proceeds as in 4.2, using the fact that the assertion is established (VIII 1.5) when $G$ and $H$ are trivial. The
necessary effectivity criterion is furnished by 5.5 (in the case of an étale surjective morphism $S' \to S$).

In particular, taking $G = G_{m,S}$, one finds:

**Corollary 5.7.** *(i) Let $H$ be a quasi-isotrivial $S$-group of multiplicative type; then the $S$-group $D_{S}(H)$ is
representable and is a quasi-isotrivial twisted constant group over $S$.*

<!-- label: III.X.5.7 -->

*(ii) The functors $R \mapsto D_{S}(R)$ and $H \mapsto D_{S}(H)$ are anti-equivalences, quasi-inverse to one another,
between the category of quasi-isotrivial twisted constant $S$-groups and that of quasi-isotrivial $S$-groups of
multiplicative type.*

*(iii) These functors induce anti-equivalences between the subcategories formed by the isotrivial, resp. locally
isotrivial, resp. locally trivial, resp. trivial groups.*

The last assertion is included only for the record, being already contained in 5.3.

Moreover, since every $S$-group of multiplicative type and of finite type is quasi-isotrivial by 4.5, one deduces from
5.6:

**Corollary 5.8.** *Let $S$ be a prescheme, $G$ and $H$ two $S$-preschemes in groups of multiplicative type and of
finite type. Then $\operatorname{Hom}_{S-gr.}(H, G)$ is representable and is a finitely generated quasi-isotrivial
twisted constant $S$-group.*

<!-- label: III.X.5.8 -->

Let us note also that in 5.3, $R$ is finitely generated if and only if $H = D_{S}(R)$ is of finite type (IX 2.1 b)). By
4.5, $H$ is then quasi-isotrivial, hence $R$ is quasi-isotrivial. One thus finds:

<!-- original page 103 -->

**Corollary 5.9.** *The functors of 5.7 induce anti-equivalences quasi-inverse to one another between the category of
$S$-groups $H$ of multiplicative type of finite type, and that of finitely generated twisted constant $S$-groups $R$;
moreover, every such group $R$ is quasi-isotrivial.*

<!-- label: III.X.5.9 -->

**Corollary 5.10.** *Let $H$, $G$ be two $S$-preschemes in groups of multiplicative type and of finite type.*

<!-- label: III.X.5.10 -->

*(i) Then $Isom_{S-gr.}(H, G)$ is representable by an open and closed subprescheme of $\operatorname{Hom}_{S-gr.}(H,
G)$, and it is a twisted constant $S$-prescheme.*

*(ii) In particular, $\operatorname{Aut}_{S-gr.}(H)$ is representable and is a twisted constant $S$-group (in general
non-commutative).*

This follows from 5.8 and from VIII 1.6.[^N.D.E-X-38]

**Recall 5.11.0.**[^N.D.E-X-39] Recall that if $X$ is a locally noetherian prescheme, its connected components (which
are always closed) are open. Indeed, let $C$ be a connected component of $X$, $x \in C$ and $U$ a noetherian open
neighborhood of $x$; then $U$ has only a finite number of connected components, hence the connected component $U_{x}$ of
$x$ in $U$ is open in $U$ hence in $X$; since $U_{x} \subseteq C$, this shows that $C$ is open in $X$.

<!-- label: III.X.5.11.0 -->

**Proposition 5.11.** *Let $S$ be a prescheme, $R$ a commutative twisted constant group over $S$, $H = D_{S}(R)$ the
group of multiplicative type that it defines. Consider the following conditions:*

<!-- label: III.X.5.11 -->

*(i) $H$ is isotrivial (i.e. $R$ is isotrivial).*

*(ii) $R$ is the union of subpreschemes both open and closed $R_{i}$, which are quasi-compact over $S$ (and then
necessarily finite over $S$).*

*(iii) The connected components of $R$ are finite over $S$.*

*a) Then (i) ⇒ (ii) ⇒ (iii).*[^N.D.E-X-40]

*b) One has (i) ⇔ (ii) ⇔ (iii) if $S$ is locally noetherian.*

*c) Finally, (i) ⇔ (ii) if $R$ is finitely generated (i.e. if $H$ is of finite type over $S$), at least if $S$ is
quasi-compact or if its connected components are open.*

Decomposing first $S$ into a prescheme sum of preschemes $S_{i}$ on each of which $H$ is of constant type (cf. IX
1.4.1), we are reduced to the case where $H$ hence $R$ is of constant type $M$. We shall need:

**Lemma 5.12.** *Let $S$ be a prescheme, $R$ a twisted constant prescheme over $S$. Then every closed subprescheme $Z$
of $R$ which is quasi-compact over $S$ is finite over $S$.*

<!-- label: III.X.5.12 -->

Indeed, one reduces to the case where $R$ is constant, hence of the form `I_S`, where $I$ is a set, <!-- original page
104 --> hence the filtered increasing union of the `J_S`, where $J$ runs through the finite subsets of $I$. One may
moreover suppose $S$ affine; then $Z$ is quasi-compact, hence contained in one of the `J_S`. Since `J_S` is finite over
$S$, the same holds for $Z$.

Lemma 5.12 already establishes the parenthesized assertion in 5.11 (ii).[^N.D.E-X-41] The implication (ii) ⇒ (iii) is
then clear, since the connected components of $R$ are closed; by 5.11.0 they are open and closed if $S$ is locally
noetherian ($R$ being étale, hence locally of finite type over $S$), whence (iii) ⇒ (ii) in this case.

Let us prove that (i) ⇒ (ii). For this, let $S' \to S$ be an étale finite surjective morphism splitting $H$ hence $R$
(cf. 5.3), so that $R'$ is isomorphic to $M_{S'} = \coprod_{m \in M} R'_{m}$, where the $R'_{m}$ are disjoint open sets
of $R'$, $S'$-isomorphic to $S'$. Let $g : R' \to R$ be the projection, which is a finite étale surjective morphism,
hence an open and closed morphism; then the $R_{m} = g(R'_{m})$ are open and closed parts of $R$, and obviously
quasi-compact over $S$ since the $R'_{m}$ are so.

Finally, suppose $H$ of finite type over $S$, and let us prove (ii) ⇒ (i). The case where the connected components of
$S$ are open reduces at once to the case where $S$ is connected, so we may suppose $S$ quasi-compact or connected. Since
$M$ is finitely generated, one can write $M = \mathbb{Z}^{r} \times N$, where $r$ is an integer $\geqslant 0$ and $N$ a
finite abelian group. Let $G = D_{S}(M)$; consider the preschemes

```text
P = Isom_{S-gr.}(H, G) ⊂ Hom_{S-gr.}(H, G) = Q
```

(cf. 5.8 and 5.10). One has isomorphisms

```text
Q ≃ Hom_{S-gr.}(M_S, R) ≃ Hom_{S-gr.}(ℤ^r_S, R) × Hom_{S-gr.}(N_S, R) ≃ R^r × E,
```

where $E = \operatorname{Hom}_{S-gr.}(N_{S}, R)$ is finite over $S$[^N.D.E-X-42]. It follows that $Q$ is the union of subpreschemes both
open and closed $Q_{i}$ finite over $S$. Therefore $P$ is the union of the subpreschemes both open and closed
$P_{i} = P \cap Q_{i}$, finite over $S$. Since they are étale over $S$, their images in $S$ are parts $S_{i}$ both open and
closed, and they cover $S$. If $S$ is connected or quasi-compact, there therefore exists a finite set <!-- original
page 105 --> of indices $i$ such that the $S_{i}$ cover $S$; let $S'$ be the union of the corresponding $P_{i}$. Then
$S' \to S$ is finite étale surjective, and setting $P' = P \times_{S} S' = Isom_{S'-gr.}(H', G')$, one sees that $P'$ has a
section over $S'$, hence there exists an isomorphism of $S'$-groups

```text
H′ = H ×_S S′ ⥲ G′ = G ×_S S′ = D_{S′}(M),
```

which proves that $S'$ splits $H$. This completes the proof of 5.11.[^N.D.E-X-43]

**Remark 5.11 bis.** Let us note moreover that one can, when $H$ is of finite type over $S$ and of constant type, give
the following isotriviality criterion (in which it is no longer necessary to make any restriction on $S$): $H =
D_{S}(R)$ is isotrivial if and only if $R$ is the union of a sequence of parts both open and closed finite over
$S$.[^N.D.E-X-44]

<!-- label: III.X.5.11bis -->

**Lemma 5.13.** *Let $S$ be a locally noetherian and connected prescheme, $P$ a quasi-isotrivial twisted constant
$S$-prescheme, $Z$ a part both open and closed of $P$, such that there exists an $s \in S$ with $Z_{s}$ finite. Then $Z$
is finite over $S$.*

<!-- label: III.X.5.13 -->

Let us first not suppose $S$ connected: let $U$ be the set of $s \in S$ such that $Z_{s}$ is finite; we shall prove that
$U$ is both open and closed, and that $Z|U$ is finite over $U$. This is a statement essentially equivalent to 5.13 but
has the advantage of being "of local nature" on $S$ for the étale topology (say), which reduces us to the case where $P$
is constant, i.e. of the form `I_S`, where $I$ is a set. (N.B. the locally noetherian hypothesis is not lost by an étale
base change; this is where we use the quasi-isotriviality of $P$ over $S$.)

One may moreover suppose $S$ connected, since its connected components are open ($S$ being locally noetherian). But then
one necessarily has $Z = J_{S}$, where $J$ is a part of $I$, and one therefore has $U = \emptyset$ or $U = S$, depending
on whether $J$ is infinite or finite, which gives the desired conclusion.

**Recalls 5.14.0.**[^N.D.E-X-45] Let $S$ be a locally noetherian prescheme, and let $\tilde{S}$ be the normalization of
$S_{red}$ (cf.
[EGA II, 6.3.8](https://jcreinhold.github.io/ega/ii/02-06-integral-finite-morphisms.html#63-integral-closure-of-a-prescheme)).
Recall that $S$ is said to be *geometrically unibranch* (cf.
[EGA 0_IV, § 23.2](https://jcreinhold.github.io/ega/iv/10-ch0-23-japanese-rings.html#232-integral-closure-of-an-integral-noetherian-local-ring)
and IV₂, § 6.15) if the canonical morphism $\tilde{S} \to S$ is radicial (and hence a universal homeomorphism); in
particular, the connected components of $S$ are irreducible.

<!-- label: III.X.5.14.0 -->

Suppose then $S$ connected, hence irreducible, let $\eta$ be its generic point and let $f : P \to S$ be a flat and
locally quasi-finite morphism. Let $P_{i}$ be the irreducible components of $P$, and $\xi_{i}$ the generic point of
$P_{i}$. Since $P$ is flat over $S$, each $\xi_{i}$ <!-- original page 106 --> lies above $\eta$ (cf.
[EGA IV₂, 2.3.4](https://jcreinhold.github.io/ega/iv/14-ch4-02-base-change-and-flatness.html#23-topological-properties-of-flat-morphisms)),
and so $(P_{i})_{\eta} = P_{i} \cap P_{\eta}$ is the closure of $\xi_{i}$ in $P_{\eta}$. Since the fiber $P_{\eta}$ is
discrete, one therefore has $(P_{i})_{\eta} = {\xi_{i}}$. This applies in particular when $f$ is étale; in this case,
$P$ is also locally noetherian and geometrically unibranch (cf.
[EGA IV₄, 17.5.7](https://jcreinhold.github.io/ega/iv/30-ch4-17-smooth-unramified-etale-morphisms.html#175-characterizations-of-smooth-morphisms)),
so its irreducible components are its connected components and are open (and closed).

**Corollary 5.14.** *Let $S$ be a locally noetherian and geometrically unibranch prescheme, $P$ a quasi-isotrivial
twisted constant $S$-prescheme. Then the connected components of $P$ are finite over $S$.*

<!-- label: III.X.5.14 -->

One may obviously suppose $S$ connected hence irreducible, and let $\eta$ be its generic point. By what precedes, each
connected component $P_{i}$ of $P$ is open and closed, and meets the fiber $P_{\eta}$ at a single point. Therefore 5.13
applies and shows that each $P_{i}$ is finite over $S$.

**Theorem 5.16.**[^N.D.E-X-46] *Let $S$ be a locally noetherian and geometrically unibranch prescheme. Then every
$S$-group of multiplicative type and of finite type is isotrivial.*

<!-- label: III.X.5.16 -->

One may indeed suppose $S$ connected, hence $H$ of constant type $M$. It suffices to apply 5.14 to $P = Isom_{S-gr.}(H,
G)$, where $G = D_{S}(M)$, then to argue as in the proof of 5.11 (ii) ⇒ (i). One may also apply 5.14 to $P = R =
D_{S}(H)$ (cf. 5.9), then use 5.11.

## 6. Infinite Galois principal covers and the enlarged fundamental group

(The results of the present N° and of the following will no longer be used in the sequel of this Seminar.)

Let $S$ be a prescheme; we propose to determine the principal homogeneous bundles $P$ over $S$ with structural group of
the form `G_S`, the constant $S$-group defined by an ordinary group $G$ (not necessarily finite), which we shall also
call *Galois principal bundles over $S$ with group $G$*. <!-- original page 107 --> We take "principal bundle" in the
sense of the faithfully flat quasi-compact topology (cf. Exp. IV, Def. 5.1.5), but we shall note that for such a $P$,
the structural morphism $P \to S$ is necessarily étale and surjective, hence covering for the étale topology;
consequently $P$ is also locally trivial for the étale topology (cf. IV, Prop. 5.1.6).[^N.D.E-X-47]

We shall assume that $S$ is a sum of connected preschemes, i.e. that its connected components are open, which reduces us
at once to the case where $S$ is connected. We shall then choose a "geometric point" $\xi$ of $S$, i.e. an $S$-scheme
$\xi$ which is the spectrum of an algebraically closed field $\Omega = \kappa(\xi)$. Then for every Galois principal
bundle $P$ over $S$ with group $G$, $P_{\xi}$ is a Galois principal bundle over the algebraically closed field
$\kappa(\xi)$, hence is trivial. We shall therefore make the initial problem precise by proposing to determine the
category of Galois principal bundles over $S$ *pointed* above $\xi$, i.e. endowed with an $S$-homomorphism $\xi \to P$,
i.e. with a trivialization of $P_{\xi}$. For fixed $G$, the set of classes of such bundles, up to an isomorphism
respecting the base point, will be denoted by $\bar{\pi}^{1}(S, \xi; G)$. Then the set $\bar{\pi}^{1}(S; G)$ of
isomorphism classes of Galois principal bundles over $S$ with group $G$ (without a specified base point) is isomorphic
to the set of orbits of $G$ in $\bar{\pi}^{1}(S, \xi; G)$ (taking into account the natural operations of $G$ on this
set, corresponding to translation by $G$ of the marked point in a pointed Galois principal bundle $P$):

```text
π̄¹(S; G) = π̄¹(S, ξ; G)/G.
```

For every morphism $S' \to S$ which is a morphism of universal effective descent for the fibered category of twisted
constant preschemes over a variable base (for example $S' \to S$ faithfully flat and locally of finite presentation, cf.
5.4; for other examples cf. SGA 1 IX), we propose to determine the subsets of the preceding sets, denoted
$\bar{\pi}^{1}(S'/S, \xi; G)$ and <!-- original page 108 --> $\bar{\pi}^{1}(S'/S; G)$, formed by the Galois principal
bundles over $S$ which become trivial on $S'$ (or, as one says, are "split" by $S'$). One will in fact determine the
category of Galois principal bundles $P$ over $S$ which are split by $S'$. Of course, one will then have

```text
π̄¹(S, ξ; G) = lim_{S′} π̄¹(S′/S, ξ; G),
```

where in the second member, $S'$ runs over a cofinal system in the set of $S'/S$ covering for the étale topology (for
example, when $S$ is quasi-compact, the set of $S'$ over $S$ which are quasi-compact and with étale and surjective
structural morphism). Likewise, the category of Galois principal bundles over $S$ will be the inductive limit of the
subcategories defined by the $S'$ (formed of the bundles which are split over $S'$).

Thanks to the hypothesis made on $S'/S$, the category of Galois principal bundles over $S$ split by $S'$ is equivalent
to the category of trivial Galois principal bundles over $S'$ (hence of the form $G_{S'}$, where $G$ acts by right
translations), endowed with a descent datum relative to $S' \to S$. The datum of a base point on a Galois principal
bundle $P$ over $S$ split by $S'$ amounts, in terms of the corresponding trivial bundle $P'$ over $S'$ and its descent
datum, to the datum of a trivialization of $P' \times_{S'} S'_{\xi}$ compatible with the induced descent datum, relative
to $S'_{\xi} \to \xi$ (N.B. we have set $S'_{\xi} = S' \times_{S} \xi$), i.e. a section $\sigma$ of $P'_{\xi}$ over
$S'_{\xi}$ compatible with the descent datum. There is then advantage, for an arbitrary $S$-prescheme $S'$ (for which
one no longer supposes that $S' \to S$ is a morphism of universal effective descent for the fibered category of twisted
constant bundles…), in defining $\bar{\pi}^{1}(S'/S; G)$ and $\bar{\pi}^{1}(S'/S, \xi; G)$ as the set of classes, up to
isomorphism, of the structures with descent data just specified. One then obtains, for these functors in $G$, a very
simple simplicial description, in terms of the fibered square and cube $S''$ and $S'''$ of $S'$ over $S$, which we shall
sketch below (cf. 6.3).

<!-- original page 109 -->

The important conclusion to retain will be the following:

**Proposition 6.1.** *Suppose that the connected components of $S'$ and $S''$ are open, and, for example, that the
quotient set of $\pi_{0}(S')$ by the equivalence relation induced by the two projections $\pi_{0}(S'') \to \pi_{0}(S')$
is a single point.*[^N.D.E-X-48]

<!-- label: III.X.6.1 -->

*(i) The functor $G \mapsto \bar{\pi}^{1}(S'/S, \xi; G)$, from the category of groups to the category of sets, is
representable by a group, denoted $\pi_{1}(S'/S, \xi)$ and called the* fundamental group of $S$ at $\xi$ relative to $S'
\to S$. *One thus has a functorial bijection:*

```text
π̄¹(S′/S, ξ; G) ≃ Hom_{gr.}(π_1(S′/S, ξ), G).
```

*(ii) This group has a set of generators in bijection with $\pi_{0}(S'')$, and is described in terms of these generators
by relations in bijection with the elements of $\pi_{0}(S''')$.[^N.D.E-X-49] In particular, $\pi_{1}(S'/S, \xi)$ is
finitely generated (resp. of finite presentation) if $\pi_{0}(S'')$ (resp. as well as $\pi_{0}(S''')$) is finite.*

*(iii) The category of Galois principal bundles over $S$ split by $S'$, with base point above $\xi$, is equivalent to
the category of ordinary groups $G$, endowed with a homomorphism of $\pi_{1}(S'/S, \xi)$ into $G$.*

The proof is given below, cf. ….

**6.2.** When $S$ is a connected locally noetherian prescheme, which implies that every étale prescheme $S'$ over $S$ is
locally noetherian hence has its connected components open, one concludes from what precedes[^N.D.E-X-50] that the
functor $G \mapsto \bar{\pi}^{1}(S, \xi; G)$, from the category of ordinary groups to the category of sets, is strictly
pro-representable (cf. *Séminaire Bourbaki*, February 1960, N° 195, §§ A.2 and A.3), i.e. there exists a projective
system

<!-- label: III.X.6.2 -->

```text
Π = Π_1(S; ξ) = (π_i)_{i ∈ I}
```

of ordinary groups over a filtered increasing index set $I$, which is "strict" <!-- original page 110 --> (i.e. with
surjective transition morphisms $\pi_{j} \to \pi_{i}$), and an isomorphism of functors in $G$

```text
π̄¹(S, ξ; G) ≃ lim_i Hom_{gr.}(π_i, G).
```

The second member is also simply denoted $\operatorname{Hom}_{pro-gr.}(\Pi, G)$ (cf. loc. cit.).

In the case where the projective limit $\pi = \lim \pi_{i}$ is "sufficiently large", more precisely when the canonical
homomorphisms $\Pi \to \Pi_{i}$ are surjective, it is appropriate to endow $\Pi$ with the projective limit topology of
the discrete topologies of the $\Pi_{i}$, and the preceding isomorphism is also written:

```text
π̄¹(S, ξ; G) ≃ Hom_{gr. top.}(π, G),
```

where the second member denotes the set of homomorphisms of topological groups, it being understood that $G$ is endowed
with the discrete topology.

The hypothesis just formulated on the projective system $\Pi$ is verified, as is well known, when the $\pi_{i}$ are
finite groups (cf. [BEns], III § 7.4, Th. 1). This last condition obviously also means that every Galois principal
bundle over $S$ is isotrivial, i.e. is split by an étale surjective finite morphism. This is the case when $S$ is
geometrically unibranch (for example normal), as follows at once from 5.14.[^N.D.E-X-51] In the case where the $\pi_{i}$
are finite, the group $\pi$ coincides also with the fundamental group $\pi_{1}(S, \xi)$ introduced in SGA 1, V.

Also, in the favorable case ($\pi \to \pi_{i}$ surjective) one could call $\pi$ the *enlarged fundamental group of $S$
at $\xi$*. Outside of this favorable case, $\pi$ itself is hardly of interest, and the role of the usual fundamental
group is played by the projective system $\Pi$ itself, which one will call the *enlarged fundamental pro-group of $S$ at
$\xi$*. (Any terminological suggestion better than "enlarged" is welcome![^N.D.E-X-52]). One will note that knowledge of
this pro-group is more precise than that of the usual fundamental group $\pi_{1}(S, \xi)$ of SGA 1 V; more precisely,
the latter is the projective limit of the projective system formed by the finite quotients of the $\pi_{i}$.

**6.3.** Let us indicate rapidly the "computation" of $\pi_{1}(S'/S, \xi)$. Let $S_{i}$ be the $(i + 1)$-th fibered
power of $S'$ over $S$ (i.e. $S_{0} = S'$, $S_{1} = S''$, etc.). One has between the $S_{i}$ obvious simplicial
operations, which make $(S_{i})_{i \in \mathbb{N}}$ a simplicial object of $(Sch)/S$.

<!-- label: III.X.6.3 -->

<!-- original page 111 -->

Transforming this simplicial object by the functor "set of connected components"

$$ \pi_{0} : (Sch)/S \longrightarrow (Ens), $$

one finds a simplicial set $K_{\bullet} = (K_{i})_{i \in \mathbb{N}}$, with $K_{i} = \pi_{0}(S_{i})$.

Likewise, the $S_{i,\xi}$ (= $(i + 1)$-th fibered power of $S'_{\xi}$ over $\xi$) form a simplicial object of
$(Sch)/\xi$ hence of $(Sch)/S$, moreover endowed with a natural homomorphism of simplicial objects into $(S_{i})_{i \in
\mathbb{N}}$, whence a simplicial set $k_{\bullet}$ (with $k_{i} = \pi_{0}(S_{i,\xi})$) and a canonical homomorphism

$$ k_{\bullet} \longrightarrow K_{\bullet}. $$

We can form a new simplicial set by taking the cone of this morphism (cf. 9.5.1):

$$ \tilde{K}_{\bullet} = Cone(k_{\bullet} \longrightarrow K_{\bullet}). $$

[^N.D.E-X-53] In this way, one obtains a "pointed simplicial set" $\tilde{K}_{\bullet}$ (i.e. a simplicial set endowed
with a homomorphism $\tilde{\xi} : \tilde{e}_{\bullet} \to \tilde{K}_{\bullet}$, where $\tilde{e}_{\bullet}$ is the
final simplicial set). We can construct its well-known combinatorial invariants $\pi_{0}(\tilde{K}_{\bullet},
\tilde{\xi})$ and $\pi_{1}(\tilde{K}_{\bullet}, \tilde{\xi})$, whose construction involves only the components of degree
$\leqslant 1$ resp. of degree $\leqslant 2$. These invariants are defined without restriction on $S$ or $S'$. One then
verifies without difficulty, when the connected components of `S_0` and `S_1` are open and $\tilde{K}_{\bullet}$ is
connected,[^N.D.E-X-54] that $\pi_{1}(\tilde{K}_{\bullet}, \tilde{\xi})$ represents the functor $G \mapsto
\bar{\pi}^{1}(S'/S, \xi; G)$, i.e. one has:

```text
π_1(S′/S; ξ) ≃ π_1(K̃_•, ξ̃).
```

Let us also signal that when the morphism $S' \to S$ is "universally submersive" (cf. SGA 1, IV 2.1), and the connected
components of $S'$ are open, then[^N.D.E-X-55] <!-- original page 112 --> the simplicial set $K_{\bullet}$, hence also
$\tilde{K}_{\bullet}$, is connected.

**Examples 6.4.** It remains to give examples of enlarged fundamental groups. Let us take up the examples of 1.6, i.e.
let $k$ be an algebraically closed field, `C_1` a complete rational curve over $k$, having exactly one singular point,
this point being an ordinary double point, and `C_2` a curve which is the union of two irreducible components,
isomorphic to $P^{1}_{k}$ and meeting at exactly two points, which are ordinary double points of `C_2`. In either case,
the enlarged fundamental group of the curve is isomorphic to $\mathbb{Z}$.[^N.D.E-X-56]

<!-- label: III.X.6.4 -->

In general, there would be reason to take up (simplifying and rectifying them) the results of SGA 1 IX 5, in the
framework of the enlarged fundamental group. The examples of loc. cit., 5.5 would give as many examples of enlarged
fundamental pro-groups which are not profinite. Thus, if instead of an ordinary double point, one took in the first
example a double point with $n$ distinct branches,[^N.D.E-X-57] one would find as enlarged fundamental group the free
(discrete!) group on $n - 1$ generators.

## 7. Classification of twisted constant preschemes and of groups of multiplicative type of finite type in terms of the enlarged fundamental group

**7.0.** Let $S$ be a prescheme, which we still assume locally noetherian, to ensure that $S$ and certain preschemes
over $S$ that we shall consider <!-- original page 113 --> (notably those étale over $S$, more generally those locally
of finite type over $S$) are locally connected.

**Proposition 7.0.1.** *Every twisted constant prescheme $X$ over $S$ which is locally trivial for the (fppf) topology
(i.e. which is split by a faithfully flat morphism locally of finite presentation $S' \to S$) is quasi-isotrivial (i.e.
one can even choose $S' \to S$ étale surjective).*

<!-- label: III.X.7.0.1 -->

Indeed, one may suppose $S$ connected, hence $X$ of type $I$, where $I$ is a fixed set. Therefore $X' = X \times_{S} S'$
is isomorphic to $I_{S'}$, hence $I_{S'}$ is endowed with a descent datum relative to $S' \to S$, i.e. one has an
isomorphism $I_{S''} \xrightarrow{\sim} I_{S''}$ satisfying the usual transitivity condition. Now, $S'' = S' \times_{S}
S'$ is locally noetherian hence locally connected, whence it follows that the automorphisms of $I_{S''}$ correspond to
the sections of $G_{S''}$, where $G = \operatorname{Aut}(I)$ is the group of permutations of $I$.

In this way, one obtains a descent datum on $G_{S'}$ (considered as a trivial Galois principal bundle) relative to $S'
\to S$. By 5.4 this descent datum is effective, whence a Galois principal bundle $P$ over $S$, with group $G$. By
construction, it represents the functor $Isom_{S}(I_{S}, X)$ in the category of preschemes over $S$ which are locally
noetherian. Consequently, the étale surjective base change $P \to S$ splits $X$, so $X$ is indeed quasi-isotrivial.

**Remark 7.0.2.** Beware that even if $S$ is the spectrum of a field, it is not true in general that every twisted
constant bundle over $S$ is quasi-isotrivial. It suffices for example to take for $X$ the scheme sum of a sequence of
schemes of the form $\operatorname{Spec}(k_{i})$, where the $k_{i}$ are separable extensions of $k$ of strictly
increasing degrees.

<!-- label: III.X.7.0.2 -->

The proof given above shows at the same time that the classification of twisted constant bundles $X$ over $S$,
quasi-isotrivial and of type $I$, is equivalent to that of Galois principal bundles over $S$ with group $G =
\operatorname{Aut}(I)$. It is even an equivalence of categories.

It can be put in a more convenient form as in SGA 1 V. For this, <!-- original page 114 --> suppose $S$ connected and
equipped with a geometric point $\xi$. Consequently the enlarged fundamental pro-group $\Pi = \Pi_{1}(S, \xi)$ is
defined. Moreover, for every quasi-isotrivial twisted constant bundle $X$ over $S$, let $I = X(\xi)$ be its
set-theoretic fiber at $\xi$. Therefore $X$ is of type $I$, and consequently associated as we have just said with a
Galois principal bundle $P = Isom_{S}(I_{S}, X)$ over $S$, with group $G = \operatorname{Aut}(I)$.

By the definition of $\Pi$, one therefore obtains a canonical homomorphism of $\Pi$ into $G$, i.e. of one of the
$\Pi_{i}$ into $G$. Since $G$ is the group of permutations of $I = X(\xi)$, this means that $\Pi$ "acts continuously on
$I = X(\xi)$", it being understood that the $\pi_{i}$ ($i$ large) act on $I$, in a way compatible with the transition
morphisms.

We leave to the reader the verification that every $S$-morphism $X \to Y$ between quasi-isotrivial twisted constant
bundles over $S$ induces a map $X(\xi) \to Y(\xi)$ compatible with the operations of $\Pi$, and that the functor thus
obtained is an equivalence of categories:

**Proposition 7.0.3.** *Let $S$ be a locally noetherian connected prescheme, $\xi$ a geometric point of $S$, $\Pi =
\Pi_{1}(S, \xi)$ the enlarged fundamental pro-group of $S$ at $\xi$. Then the functor*

<!-- label: III.X.7.0.3 -->

$$ X \mapsto X(\xi) $$

*is an equivalence between the category of quasi-isotrivial twisted constant bundles over $S$ and the category of sets
on which $\Pi$ acts continuously.*

This functor is compatible with the operations of finite sums and finite inverse limits. It follows for example that the
twisted constant groups (or rings etc.) quasi-isotrivial over $S$ correspond to the ordinary groups (resp. rings etc.)
on which the pro-group $\Pi$ acts continuously. In particular:

**Corollary 7.0.4.** *The category of commutative twisted constant groups quasi-isotrivial over $S$ is equivalent to the
category of "$\Pi$-modules", i.e. of commutative groups $M$ on which $\Pi$ acts continuously.*

<!-- label: III.X.7.0.4 -->

Using now 5.7 one concludes the:

**Theorem 7.1.** *Let $S$ be a locally noetherian connected prescheme, $\xi$ a geometric point of $S$, $\Pi = \Pi_{1}(S,
\xi)$ the enlarged fundamental pro-group of $S$ at $\xi$. Then the functor*

<!-- label: III.X.7.1 -->

$$ G \mapsto \operatorname{Hom}_{\kappa(\xi)-gr.}(G_{\xi}, G_{m,\xi}) $$

*induces an anti-equivalence of the category of quasi-isotrivial groups of multiplicative type over $S$* <!-- original
page 115 --> *with the category of $\Pi$-modules.*

Using 4.5 one concludes:

**Corollary 7.2.** *The preceding functor induces an anti-equivalence of the category of groups of multiplicative type
and of finite type over $S$ with the category of $\Pi$-modules which are of finite type over $\mathbb{Z}$.*

<!-- label: III.X.7.2 -->

**Example 7.3.** Take for example for $S$ a complete rational curve over an algebraically closed field, having exactly
one multiple point with $n + 1$ distinct branches. By 6.4, the enlarged fundamental group $\Pi(S, \xi)$ is a free group
on $n$ generators. Therefore, by 7.2, the classification of tori of relative dimension $m$ over $S$ is equivalent to the
classification of systems of $n$ endomorphisms $A_{1}, \cdots, A_{n}$ of the $\mathbb{Z}$-module $\mathbb{Z}^{m}$, up to
automorphism of $\mathbb{Z}^{m}$. Except for $n \leqslant 1$ or $m \leqslant 1$, an explicit classification of such
systems seems hopeless. One can at least define a multitude of non-trivial invariants for such a system, such as the
characteristic polynomials of the $A_{i}$.[^N.D.E-X-58]

<!-- label: III.X.7.3 -->

**Remark 7.4.** If one makes no hypothesis on $S$, it remains true that for a given ordinary commutative group $M$ of
finite type over $\mathbb{Z}$, the category of groups of multiplicative type of type $M$ over $S$ is anti-equivalent to
the category of Galois principal bundles over $S$ with group $G = \operatorname{Aut}_{gr.}(M)$. This follows easily from
5.9 and 5.10.

<!-- label: III.X.7.4 -->

**Remark 7.5.** The theory of the fundamental pro-group that we have sketched in the present two numbers will be written
more advantageously in the framework of general sites. In this form, it applies equally well, for example, to ordinary
topological spaces, and gives a satisfactory theory at least for a locally connected topological space (not necessarily
locally simply connected). In this case too it seems that one cannot be content with defining a fundamental group, and
that a pro-group is needed. Finally, let us note that, once one has available the language of topologies and descent
(which is really at the bottom of these questions), the exposition sketched here is also technically simpler than that
of SGA 1 V, and should therefore in principle replace it.

<!-- label: III.X.7.5 -->

## 8. Appendix: Elimination of certain affineness hypotheses

<!-- original page 116 -->

Our aim is to prove the following generalization of 4.9.

**Theorem 8.1.** *Let $S$ be a prescheme, $H$ an $S$-prescheme in groups flat and of finite presentation, with connected
and affine fibers.[^N.D.E-X-59] Let $s \in S$; suppose that $H_{s}$ is a torus. Then there exists an open neighborhood
$U$ of $s$ such that $H|U$ is a torus.*

<!-- label: III.X.8.1 -->

One concludes immediately:

**Corollary 8.2.** *Let $H$ be an $S$-prescheme in groups, flat and of finite presentation over $S$. For $H$ to be a
torus, it is necessary and sufficient that its fibers be tori.*

<!-- label: III.X.8.2 -->

**Remark 8.3.** Even when $S$ is the spectrum of a discrete valuation ring, one cannot abandon in 8.1 the hypothesis
that the fibers of $H$ (here the generic fiber) be affine, since there are examples of smooth groups over $S$ whose
generic fiber is an elliptic curve, and whose special fiber is $G_{m}$.

<!-- label: III.X.8.3 -->

*Proof of 8.1.* One may obviously suppose $S = \operatorname{Spec}(A)$ affine, which reduces us by the standard
procedure (cf. EGA IV₂, 8.8.2) to the case where $S$ is moreover noetherian. We begin by proving 8.2 in this case.

By 4.9 we are reduced to proving that $H$ is affine over $S$. We may therefore suppose[^N.D.E-X-60] $A$ noetherian
local, and since the completion `Â` is faithfully flat over $A$, we are reduced by descent to the case where $A$ is a
complete noetherian local ring. Let $S'$ be the normalization of $S_{red}$; one knows by Nagata that it is finite over
$S$ ([EGA 0_IV, 23.1.5](https://jcreinhold.github.io/ega/iv/10-ch0-23-japanese-rings.html#231-japanese-rings)); moreover
$S' \to S$ is surjective, so $H' = H \times_{S} S' \to H$ is finite and surjective, so to prove that $H$ is affine, it
suffices to show that $H'$ is so
([EGA II, 6.7.1](https://jcreinhold.github.io/ega/ii/02-06-integral-finite-morphisms.html#67-chevalleys-theorem)).

<!-- original page 95 -->

[^N.D.E-X-61] Replacing $S$ by a connected component of $S'$, this reduces us to the case where $A$ is a noetherian
(semi-local) normal and integral ring. Moreover, possibly replacing $A$ by its normalization in a finite separable
extension of its field of fractions, <!-- original page 117 --> one may suppose that the generic fiber $H_{\eta}$ of $H$
is diagonalizable, i.e. that one has an isomorphism

$$ u_{\eta} : H_{\eta} \xrightarrow{\sim} T_{\eta}, $$

where $T = G^{r}_{m,S}$. Now we have:

**Lemma 8.4.** *Let $S$ be a locally noetherian normal and irreducible prescheme, with generic point $\eta$, $H$ a
prescheme in groups over $S$ smooth and with connected fibers, $T$ a prescheme in groups of multiplicative type and of
finite type over $S$, $u_{\eta} : H_{\eta} \to T_{\eta}$ a homomorphism of algebraic groups over $\kappa(\eta)$.*

<!-- label: III.X.8.4 -->

*Then $u_{\eta}$ extends to a homomorphism of groups $u : H \to T$.*

Possibly replacing $S$ by its normalization in a finite separable extension of its function field, one may suppose $T$
diagonalizable (which is moreover the case in the application we have in view). Then $T$ is a closed subgroup of a group
of the form $G^{r}_{m,S}$, which reduces us to the case where $T = G_{m,S}$.

It all amounts to proving that $u_{\eta}$, considered as a rational map of $H$ into $T = G_{m,S}$, is everywhere defined
(since the morphism $u : H \to T$ extending it is then necessarily a homomorphism of groups). One may consider
$u_{\eta}$ as an invertible section $f$ of the structural sheaf of $H_{\eta}$, and one must show that it extends to an
invertible section of the structural sheaf of $H$. Now $H$, being smooth over the normal $S$, is normal (SGA 1, II 3.1),
so it suffices to find a closed part $Z$ of $H$ of codimension $\geqslant 2$ such that $f$ extends to an invertible
section of the structural sheaf of $H - Z$. This reduces us at once to the case where $S$ is the spectrum of a discrete
valuation ring $A$ (by localizing at points of codimension 1 of $S$).

Let $t$ be a uniformizer of $A$, $t'$ the section of `O_H` that it defines, so that the special fiber `H_0` is equal to
$V(t')$. By hypothesis `H_0` is smooth over the residue field $k$, and connected. Then $f$ is a rational function on $H$
which has neither zeros nor poles in $H - H_{0}$; since $H_{0} = V(t')$ is an irreducible divisor, there exists an integer
$n \in \mathbb{Z}$ such that $t'^{n} f = t^{n} f$ has neither zeros nor poles, i.e. is an invertible section of `O_H`. <!-- original
page 118 --> It therefore defines a morphism $v : H \to G_{m,S}$, and since $v_{\eta} = t'^{n} u_{\eta}$ and $u_{\eta}$ is a homomorphism
of groups, $v$ transforms the unit section of $H$ into a section of $G_{m,S}$ whose value at the generic point of $S$ is
$t^{n}$; since it is a question of a section of $G_{m,S}$, $t^{n}$ must be a unit, i.e. $n = 0$, so $v$ extends $u_{\eta}$, which
completes the proof of 8.4.

Applying this lemma to the present case, one finds a homomorphism of groups

```text
u : H ⟶ T = G^r_{m,S}
```

which induces on the generic fibers an isomorphism. Let us prove that $u$ is an isomorphism.

**Lemma 8.5.** *For every integer $n > 0$ prime to the residual characteristic of $A$, ${}_{n} H = Ker(n \cdot id_{H})$
is finite over $S$.*

<!-- label: III.X.8.5 -->

If $n$ is prime to the residual characteristic of $A$, it is prime to all the residual characteristics of points of $S$.
Therefore $n \cdot id_{H}$ induces on every fiber of $H$ an étale morphism; consequently $n \cdot id_{H}$ is étale (SGA
1, I 5.9), so its kernel ${}_{n} H$ is étale over $S$. On the other hand, ${}_{n} H$ is separated over $S$ since $H$
is.[^X-8-1] [^N.D.E-X-62] Moreover, all its fibers have the same rank $n^{r}$, since the fibers of $H$ are tori, all of
the same dimension $r$ ($H$ being smooth over $S$). One concludes that ${}_{n} H$ is finite over $S$ (SGA 1, I 10.9 or
EGA IV₄, 18.2.9).

Therefore, by the preceding lemma, $u({}_{n} H)$ is a closed part of $T$. Since on the generic fiber $T_{\eta}$, this
part is identical to ${}_{n}(T_{\eta})$, it follows that it contains the closure of this part, namely ${}_{n} T$. Now
for every $s \in S$, the ${}_{n}(T_{s})$ are dense in $T_{s}$; since $u_{s}(H_{s})$ is a closed part (VI_B 1.4.2)
containing them, one sees that $u_{s}(H_{s}) = T_{s}$, so $u$ is surjective. Since a surjective homomorphism of tori of
the same dimension over a field is flat,[^N.D.E-X-63] it follows that $u$ induces on each fiber a flat morphism, so $u$
is flat (SGA 1 I 5.9). Consequently, $K = Ker(u)$ is flat over $S$,[^N.D.E-X-64] hence equal to the closure of its
generic fiber $K_{\eta}$. Now $K_{\eta}$ is the unit group by construction, and since $K$ is separated over $S$ (since
$H$ is), its unit section is closed, whence it follows that $K$ is the unit group. <!-- original page 119 --> Therefore
$u$ is a monomorphism; since we have seen that it is faithfully flat, it is therefore an isomorphism (cf. SGA 1, I 5.1
or
[EGA IV₄, 17.9.1](https://jcreinhold.github.io/ega/iv/30-ch4-17-smooth-unramified-etale-morphisms.html#179-étale-morphisms-and-open-immersions)).
This proves that $H$ is a torus, hence completes the proof of 8.2.[^N.D.E-X-65]

**Remark 8.5.1.** Instead of invoking 8.5 one can also invoke Zariski's "Main Theorem", which directly implies that $u$
is an open immersion, hence an isomorphism.[^N.D.E-X-66]

<!-- label: III.X.8.5.1 -->

To prove 8.1, we are reduced, thanks to the quasi-isotriviality theorem, to the case where $S$ is local, $s$ its closed
point,[^N.D.E-X-67] and to proving that, with the hypotheses made elsewhere, $H$ is then a torus. By 8.2 already proved,
we are reduced to proving that the fibers of $H$ are tori. One may suppose $S$ the spectrum of a complete noetherian
local ring $A$. By 3.3 there exists for every $n > 0$ a group of multiplicative type $T_{n}$ finite over $S$, and an
isomorphism $(T_{n})_{s} \simeq {}_{n}(H_{s})$, where $s$ is the closed point of $S$. Proceeding as in 3.1 and using the
fact that $T_{n}$ is finite over $S$,[^N.D.E-X-68] one sees that the preceding isomorphism comes from a homomorphism
$u_{n} : T_{n} \to H$, moreover uniquely determined. (Pass to the limit over the artinian quotients of $A$.)

Moreover, by uniqueness properties, $u_{n} : T_{n} \to H$ is deduced from $u_{m} : T_{m} \to H$ by restriction to
${}_{n}(T_{m}) \simeq T_{n}$ when $m$ is a multiple of $n$. It follows from IX 6.6 that the $u_{n}$ are monomorphisms,
so the $T_{n}$ are subgroups of $H$, and for $m$ a multiple of $n$, one has $T_{n} = {}_{n}(T_{m})$.

Therefore for every $t \in S$, the $(T_{n})_{t}$ are subgroups of $H_{t}$, of type $(\mathbb{Z}/n\mathbb{Z})^{r}$ (where
$r = \dim H_{s} = \dim H_{t}$), such that for $m$ a multiple of $n$, one has $(T_{n})_{t} = {}_{n}(T_{m})_{t}$. The fact
that $H_{t}$ is a torus now follows from:

**Lemma 8.6.** *Let $H$ be a smooth affine algebraic group over an algebraically closed field $k$, $(T_{n})_{n > 0}$ a
family of subgroups of multiplicative type of $H$, such that for every integer $n > 0$, $T_{n}$ is of type
$(\mathbb{Z}/n\mathbb{Z})^{r}$, and for every multiple $m$ of $n$, one has $T_{n} = {}_{n}(T_{m})$.*

<!-- label: III.X.8.6 -->

*Under these conditions, $H$ contains a torus of dimension $\geqslant r$ containing the $T_{n}$,* <!-- original page 120 --> *so
if $H$ is connected of dimension $\leqslant r$, $H$ is a torus of dimension $r$.*

This is an exercise on affine algebraic groups, which we shall treat by reference to *Bible*. We confine ourselves to
considering the $T_{n}$ for $n$ prime to the characteristic. Let $K$ be the closure of the union of the $T_{n}$ in $H$,
endowed with the induced reduced structure; then standard arguments show that $K$ is a commutative algebraic subgroup of
$H$. By *Bible*, § 4.5, Th. 4, $K$ is therefore isomorphic to a product $K_{u} \times K_{s}$, with $K_{u}$ "unipotent"
and $K_{s}$ diagonalizable. Every diagonalizable subgroup of $K$ is contained in $K_{s}$, so the $T_{n}$ are subgroups
of $K_{s}$, hence $K = K_{s}$. Write $K = D(M)$, with $M$ an ordinary commutative group of finite type over
$\mathbb{Z}$; then $T_{n} \subseteq K$ means that $M$ admits a quotient group isomorphic to
$(\mathbb{Z}/n\mathbb{Z})^{r}$. Since this is true for every integer $n$ prime to the characteristic of $k$ (it would
suffice for powers of a fixed prime number), it follows that $M$ is of rank $\geqslant r$, so $K$ contains a torus of
dimension $r$, say $T$. When $H$ is connected of dimension $r$, it follows that $T = H$, which completes the proof of
8.6. Thus 8.1 is proved.

**Remarks 8.7.** Using 8.1, it should not be difficult to give analogous generalizations of 4.7 and 4.8. A more
interesting study would be that of the situation in 8.1 where one abandons the hypothesis that the fibers of $H$ be
affine. One can show that there then exists an open neighborhood $U$ of $s$ such that $H|U$ is commutative and that for
every $t \in U$, the geometric fiber $H_{t}$ is an extension of an abelian variety by a torus.[^N.D.E-X-69] Of course,
in questions of this kind, one may restrict oneself to the case where $S$ is the spectrum of a discrete valuation ring,
$s$ its closed point, $t$ its generic point.

<!-- label: III.X.8.7 -->

One can generalize this result as follows. For every algebraic group $G$ connected smooth over an algebraically closed
field $k$, a well-known theorem of Chevalley <!-- original page 121 --> tells us that $G$ is (in a unique way) an
extension of an abelian variety $A$ by a smooth connected affine group $V$. Let us denote by *abelian rank* (resp.
*reductive rank*, resp. *nilpotent rank*, resp. *semisimple dimension*) of $G$, and denote by $\rho_{ab}(G)$ (resp.
$\rho_{r}(G)$, resp. $\rho_{n}(G)$, resp. $d_{s}(G)$), the dimension of $A$, resp. the dimension of the maximal tori of
$G$, resp. the dimension of the Cartan subgroups[^N.D.E-X-70] of $G$, resp. the dimension of the quotient of $G$ (or
also of $V$) by its radical (cf. *Bible* for all these notions). Let us also introduce the *unipotent rank* $\rho_{u}(G)
= \rho_{u}(V) = \rho_{n}(G) - \rho_{r}(G) - \rho_{ab}(G)$. When $G$ is not over an algebraically closed field, we still
denote by the same names and the same notations the corresponding invariants for $G_{\bar{k}}$, where $\bar{k}$ is the
algebraic closure of $k$.

This being so, let $G$ be a smooth group scheme over the spectrum $S$ of a discrete valuation ring; let $\rho_{ab}$ etc.
(resp. $\rho'_{ab}$ etc.) be the invariants associated with the special fiber (resp. with the generic fiber); then one
has the inequalities:

```text
⎧ ρ_{ab} ⩽ ρ′_{ab}             ⎧ ρ_n ⩾ ρ′_n
⎨ ρ_r + ρ_{ab} ⩽ ρ′_r + ρ′_{ab}⎨
⎩ d_s ⩽ d′_s                   ⎩ ρ_u ⩾ ρ′_u.
```

It amounts to the same to say that if $G$ is smooth of finite type over an arbitrary base $S$, the functions $s \mapsto
\rho_{ab}(s)$, $\rho_{ab}(s) + \rho_{r}(s)$, $d_{s}(s)$ are lower semi-continuous, and the functions $s \mapsto
\rho_{n}(s)$, $\rho_{u}(s)$ are upper semi-continuous.[^N.D.E-X-71]

The same results probably remain valid without supposing $G$ smooth over $S$, but simply flat of finite presentation
over $S$, by agreeing to denote, for an algebraic group $G$ over an algebraically closed field $k$, by $\rho_{ab}(G)$
etc. the corresponding invariants of $G^{0}_{red}$.

In this Seminar, we present some results of this kind for $G$ affine over $S$, or more generally with affine fibers:

<!-- original page 122 --> in this case, we shall verify the semi-continuity properties for `ρ_r`, `ρ_n` hence for

$\rho_{u} = \rho_{n} - \rho_{r}$, and the continuity of $\rho_{s}$ in a neighborhood of a point $s$ whose fiber is a
reductive group.[^N.D.E-X-71]

One can generalize 8.2 when one supposes already $G$ commutative, as follows:

**Theorem 8.8.**[^N.D.E-X-72] *Let $G$ be an $S$-prescheme in commutative groups which is flat and of finite
presentation over $S$, with affine connected fibers. Let $s \in S$, and suppose that*

<!-- label: III.X.8.8 -->

*a) if $\bar{k}$ denotes an algebraic closure of $\kappa(s)$, $(G_{\bar{k}})_{red}$ is a torus.*

*b) There exists a generization $t$ of $s$ such that $G_{t}$ is smooth over $\kappa(t)$.*

*Under these conditions, there exists an open neighborhood $U$ of $s$ such that $G|U$ is a torus.*

*(Note moreover that if one supposes only that for every generization $t$ of $s$, $G_{t}$ is affine resp. connected, one
easily derives that the same conclusion is valid for $t$ in an open neighborhood of $s$).*

*Proof of 8.8.* It suffices to prove that $G_{s}$ is smooth over $\kappa(s)$. Indeed, since $G$ is flat of finite
presentation over $S$, it then follows that $G$ is smooth over $S$ above a neighborhood of $s$ (cf. 3.5), but then one
is under the conditions of 8.1.

To prove that $G_{s}$ is smooth over $\kappa(s)$, the usual procedure reduces us to the case where $S$ is affine
noetherian. Choosing a homomorphism $S' \to S$ from a spectrum of a discrete valuation ring $S'$ into $S$, sending the
closed point to $s$ and the generic point $\eta$ to $t$, we are reduced to the case where $S$ is itself the spectrum of
a discrete valuation ring, which may be assumed moreover complete with algebraically closed residue field, and where $s$
and $t = \eta$ are respectively the closed point and the generic point of $S$.

Therefore $G$ is flat, separated, of finite type over $S$, the generic fiber $G_{\eta}$ is smooth and connected, <!--
original page 123 --> and the special fiber `G_0` is such that $T_{0} = (G_{0})_{red}$ is a torus. Let $m$ be an integer
`> 0` prime to the residual characteristic at $s$, hence also to that at $\eta$; one knows then that $m \cdot id_{G}$ is
a fiber-by-fiber étale morphism (VII_A 8.4), hence an étale morphism since $G$ is flat over $S$ (SGA 1 I 5.9), so its
kernel ${}_{m} G$ is étale over $S$, and since $G$ is separated[^X-8-2] [^N.D.E-X-73] of finite type over $S$, so is
${}_{m} G$. Since $({}_{m} G)_{0} = {}_{m}(T_{0})$, its degree is $m^{r}$, where `r = dim T_0 = dim G_0 = dim G`. It
follows that the rank of $({}_{m} G)_{\eta} = {}_{m}(G_{\eta})$ is $\geqslant m^{r}$, which proves already (using 8.6)
that $G_{\eta}$ is a torus of dimension $r$, since the two fibers of ${}_{m} G$ have the same rank, hence as in 8.5 that
${}_{m} G$ is finite over $S$.[^N.D.E-X-74]

Note that since $S$ is complete with algebraically closed residue field, the finite étale cover ${}_{m} G$ decomposes
completely, so through every point of ${}_{m} G_{0}$ passes a section of $G$ over $S$; in particular, the set of points
of `G_0` through which passes a section of $G$ over $S$ is everywhere dense. Now we have this:

**Lemma 8.9.** *Let $S$ be a locally noetherian regular prescheme of dimension 1, $G$ an $S$-prescheme in groups flat
and locally of finite type, such that $G_{\eta}$ is smooth over $\kappa(\eta)$ for every maximal point $\eta$ of $S$
(which implies that $G$ is reduced). Suppose that the normalized scheme $X$ of $G$ is finite over $G$ (this is the case,
by Nagata, if $S$ is the spectrum of a complete discrete valuation ring, cf.
[EGA IV₂, 7.7.4](https://jcreinhold.github.io/ega/iv/19-ch4-07-noetherian-completion.html#77-applications-ii-universally-japanese-rings)),
and let $G'$ be the open set of $X$ formed by the points at which $X$ is smooth over $S$. With these notations:*

<!-- label: III.X.8.9 -->

*a) If the projection $G' \to S$ is surjective, then there exists on $G'$ a unique structure of $S$-prescheme in groups
such that the canonical morphism $G' \to G$ is a homomorphism of groups.*

*b) Suppose that for every closed point $s$ of $S$, the set of points of $G^{0}_{s}$ through which passes an étale
quasi-section is dense in $G^{0}_{s}$ for the Zariski topology. Then $X$ is regular, one is under the conditions of a),
and the map $\Gamma(G'/S) \to \Gamma(G/S)$ is bijective.*

<!-- original page 124 -->

In the case of interest to us, this lemma applies and gives us a homomorphism of groups $u : G' \to G$, where $G'$ is
smooth over $S$, and $u_{\eta}$ is an isomorphism $G'_{\eta} \xrightarrow{\sim} G_{\eta}$. Possibly replacing $G'$ by an
open subgroup, one may suppose that $G'_{0}$ is connected, and since $u_{0} : G'_{0} \to G_{0}$ induces a surjective
morphism $G'_{0} \to T_{0}$, where `T_0` is a torus of the same dimension as $G'_{0}$, one easily concludes that
$G'_{0}$ is a torus (for example using 8.6, or by referring to *Bible*, § 7.3, Th. 3 a)). Consequently, by 8.2 $G'$ is a
torus, but then by IX 6.8, `Ker u` is a subgroup of multiplicative type of $G'$, and since its generic fiber is reduced
to the unit group, it is the unit group, hence $u$ is a monomorphism. Using now VIII 7.9 it follows that $u$ is an
immersion. Being surjective, and $G$ being reduced, it follows that $u$ is an isomorphism, which completes the proof of
8.8.

It remains to prove 8.9. To prove a), note that the uniqueness of the group law on $G'$ making $u : G' \to G$ a
homomorphism of groups is clear, since one knows the group law of $G'$ on the generic fiber (supposing $S$ irreducible,
which is permissible). For existence, one reduces easily to the case where $S$ is local, the spectrum of a discrete
valuation ring $A$, and thanks to uniqueness, and to the fact that the operation of integral closure commutes with an
étale base extension, one can make étale base extensions on $S$, which reduces us to the case where $A$ is "strictly
local" i.e. henselian with separably closed residue field. The same reduction applies for b), but under the hypothesis
made in b), one can now replace "étale quasi-section" by "section".

Note that $G'$ being smooth over $S$ and $X$ normal, $G' \times_{S} X$ is normal (since smooth over $X$ which is
normal), so the composite morphism $G' \times_{S} X \to G \times_{S} G \to G$ factors as

```text
p : G′ ×_S X ⟶ X.
```

<!-- original page 125 -->

Let us prove that this last morphism induces on the open set $G' \times_{S} G'$ of $G' \times_{S} X$ a morphism

```text
G′ ×_S G′ ⟶ G′.
```

One must therefore show that $G'_{0} \times_{k} G'_{0}$ is mapped into the open set $G'_{0}$ of `X_0`; it suffices to
see that for every point $g'_{0}$ of $G'_{0}$ with values in $k$, the morphism

$$ (\times) h'_{0} \mapsto p_{0}(g'_{0}, h'_{0}) $$

from $G'_{0}$ into `X_0` takes its values in $G'_{0}$. Now since $G'$ is smooth over $S$ and $S$ is henselian, every
$g'_{0}$ as above is induced by a section $g'$ of $G'$ over $S$, and one sees at once that the morphism $(\times)$ above
is then induced by the morphism $h' \mapsto p(g', h')$ of $G'$ into $X$, itself deduced by transport of structure from
the automorphism $h \mapsto g \cdot h$ of $G$, left translation by the section $g$ of $G$ image of $g'$. So $h' \mapsto
p(g', h')$ is itself an automorphism of $X$, hence maps $G'$ into $G'$, which proves our assertion.

It remains to prove that the composition law thus obtained on $G'$ is a group law. Associativity follows at once from
the associativity of the generic fiber (isomorphic to that of $G$). On the other hand, the symmetry automorphism of the
$S$-prescheme $G$ induces an automorphism of $X$, which therefore leaves $G'$ stable and induces an automorphism
$\sigma$ of $G'$. One then verifies that the latter has the properties of an inverse for the composition law on $G'$,
since this again reduces to verifying the commutativity of certain diagrams involving fibered powers of $G'$ over $S$,
and the latter being smooth over $S$, it suffices to verify the commutativity on the generic fiber, which is clear. This
proves part a) of 8.9.

Let us prove b). Let $Z'$ be the set of $x \in X$ such that $O_{X,x}$ is non-regular; it is a closed part by a theorem
of Nagata ([EGA IV₂, 6.12.6](https://jcreinhold.github.io/ega/iv/18-ch4-06-flat-morphisms.html#612-nagatas-criteria-for-regx-to-be-open)), <!-- original page 126 --> obviously contained in `X_0`; let $Z$ be its image in $G$, which
is therefore a closed part of `G_0`. Then $Z$ is a rare part of `G_0`, i.e. contains no maximal point $y$ of `G_0`.
Indeed, since `G_0` is defined in $G$ by an equation $t = 0$ (where $t$ is a uniformizer of the discrete valuation ring
$A$), $O_{G,y}$ is of dimension 1 by the Hauptidealsatz, so for every $x$ of $X$ above $y$, $O_{X,x}$ is of dimension 1,
hence a discrete valuation ring since $X$ is normal hence regular in codimension 1. On the other hand, it is evident
that for every section $g$ of $G$ over $S$, $Z'$ is stable under the automorphism of $X$ defined by transport of
structure from the left translation by $g$ in $G$, so $Z$ is stable under the left translation in `G_0` defined by
$g_{0}$. Now by hypothesis the set of such $g_{0}$ is dense in $G^{0}_{0}$. Since $Z$ is stable under translation by
these $g_{0}$, and is a rare closed set, it follows at once that $Z = \emptyset$, whence $Z' = \emptyset$, so $X$ is
regular. Consequently, $X$ is smooth over $S$ at every point through which passes a section. Now every section of $G$
over $S$ lifts in a unique way to a section of $X$ over $S$ hence of $G'$ over $S$. This is so in particular for the
unit section, which proves that the image of $G'$ in $S$ is $S$, i.e. that one is under the conditions of (a). This
completes the proof of 8.9 and hence of 8.8.

## 9. Addenda

[^N.D.E-X-75]

### 9.1. Simplicial sets, topoi, groupoids, and topological spaces

**Notations 9.1.1.**[^X-9-1] *Let $E$ be a simplicial set. One can associate with it the following objects:*

<!-- label: III.X.9.1.1 -->

*(2) a topos $T = E^{\sim}$, obtained from the topoi naturally associated with the sets $E_{i}$, by the procedure
described in [Del74], 6.3.1 (see also [Ill72], VI.5.2 and SGA 4 VI.7);*

*(3) a groupoid $G = \Pi(E)$, whose objects are the elements of `E_0` (the "vertices"), and whose arrows are defined in
[GZ67], II.7;*

*(4) a topological space $X = |E|$ (a cellular complex), called the "geometric realization" (or "topological") (cf. loc.
cit., III.1).*

Let us note that a sheaf on $T$ is nothing other than a simplicial set over $E$.

<!-- original page 102 -->

### 9.2. Locally constant sheaves; descent data

**Definitions 9.2.1.** *One calls a* locally constant sheaf *on:*

<!-- label: III.X.9.2.1 -->

*(1) a simplicial set $E$, every morphism of simplicial sets $E' \to E$ such that for every $i \in \mathbb{N}$ and every
$e \in E_{i}$, the face operators $d$ induce isomorphisms $E'_{e} \xrightarrow{\sim} E'_{d(e)}$ between the fibers (cf.
[AM69], § 10);*

*(2) a topos $T$, every object $F$ of $T$ such that there exists an epimorphism $U \to 1$ and an isomorphism $F \times U
\simeq f^{\ast} I \times U$, where $I$ is a set and $f : T \to Ens$ is the final morphism (cf. SGA 4, IX.2);*

*(3) a groupoid $G$, every presheaf on $G$, that is, every contravariant functor from $G$ into the category of sets (cf.
[GZ67], append. I.1.2);*

*(4) a topological space $X$, every sheaf of sets on $X$, locally constant in the usual sense.*

*Finally:*

*(5) one calls a* descent datum *on a simplicial set $E$ the datum of a sheaf $F$ on $E^{\sim}_{0}$ (that is, a
set-valued function on `E_0`) and of an isomorphism $\alpha : p^{\ast}_{1} F \xrightarrow{\sim} p^{\ast}_{2} F$, where
$p_{1}, p_{2} : E^{\sim}_{1} \to E^{\sim}_{0}$ are the morphisms (deduced from the) faces, satisfying the usual cocycle
relation (cf. Exp. IV, 2.1 (1) and infra).*

The morphisms between these five types of objects, as well as the associated inverse-image functors, are defined in an
obvious manner.

### 9.3. Some equivalences of categories

Let $E$ be a simplicial set and let $T$, $G$ and $X$ be the associated topos, groupoid and topological space.

**Proposition 9.3.1.** *The categories of locally constant sheaves on $E$, $T$, $G$, $X$ as well as the category of
descent data on $E$ are equivalent.*

<!-- label: III.X.9.3.1 -->

*Sketch of proof.* Let us denote by (1) through (5) the categories of objects defined in the preceding paragraph.

– (1) ⇔ (5). This is a particular case of [AM69], 10.6 (see also [GZ67], append. I.2.3, [Fri82], ?.5.6, or [Ill72],
VI.8.1.6). An equivalence of categories is given by the functor associating with the object $(E' \to E)$ the pair
$(E'_{0}, \alpha)$ where $E'_{0}$ is considered as a sheaf on `E_0` and where $\alpha$ is the unique isomorphism
$p^{\ast}_{1} E'_{0} \xrightarrow{\sim} p^{\ast}_{2} E'_{0}$ whose fiber at each $y \in E_{1}$ — with images denoted
$x_{1}$ and $x_{2}$ by the two projections — is given by the isomorphisms $(E'_{0})_{x_{1}} \leftarrow (E'_{1})_{y} \to
(E'_{0})_{x_{2}}$.

– (5) ⇔ (3). Evident: one of the two relations defining the morphisms in the groupoid $G$ associated with $E$ is a
cocycle relation.

– (1) ⇔ (4). Cf. [GZ67], append. I.3.2.1.

– (1) ⇔ (2). One must show that an object over $E$ is a locally constant sheaf in the simplicial sense if and only if it
is so as a sheaf on $T = E^{\sim}$. This follows from the fact that the locally constant sheaves $F_{\bullet}$ on $T$
are nothing other than the cartesian sheaves, that is, those for which the arrows $([n] \to [m])^{\ast} F_{m} \to F_{n}$
are isomorphisms. This last point is a particular case of a general fact on simplicial topoi <!-- original page 103 -->
together with the fact that every sheaf on $E^{\sim}_{0}$ is locally constant. (See also [Ill72], VI.8.1.6.) QED.

For every group $H$, the equivalences of categories above induce equivalences between the categories of $H$-torsors,
these being locally constant sheaves equipped with an action of $H$, with fibers isomorphic to $H$ acting on itself by
translation.

### 9.4. Fundamental groups and groupoids

It follows from the preceding equivalences of categories that for every group $H$ and every simplicial set $E$, the sets
of isomorphism classes of $H$-torsors $H^{1}(E, H)$, $H^{1}(E^{\sim}, H)$, $\pi_{0}(\operatorname{Hom}(\Pi(E), BH))$ and
$H^{1}(|E|, H)$ are naturally in bijection. Recall that one denotes by `BH` the punctual groupoid associated with $H$
and by $\pi_{0}$ the functor associating with a category the set of isomorphism classes of its objects.

Likewise, if $e$ is a point of $E$, the preceding equivalences induce bijections between the sets of isomorphism classes
of $H$-torsors trivialized over $e$, denoted respectively $H^{1}(E rel e, H)$, $H^{1}(E^{\sim} rel e^{\sim}, H)$,
$\operatorname{Hom}(\pi_{1}(\Pi(E), e), H)$ and $H^{1}(|E| rel |e|, H)$. Recall that one denotes by $\pi_{1}(\Pi(E), e)$
the group $Isom_{\Pi(E)}(e, e)$. For variable $H$, these functors are represented, in the connected case, by a group
which one denotes by $\pi_{1}(E, e)$. The group $\pi_{1}(E, e)$ is isomorphic to $\pi_{1}(\Pi(E), e)$ and $\pi_{1}(|E|,
|e|)$, hence also to the fundamental group of a simplicial set as defined by Kan (cf. e.g. [May67], 16.1 or [Ill72],
I.2.1.1). (Recall that the set $H^{1}(E, H)$ is in turn isomorphic to the set $H^{1}(\pi_{1}(E, e), H)$ of morphisms to
$H$ modulo conjugation, also denoted $\operatorname{Hom} ext(\pi_{1}(E, e), H)$.)

### 9.5. Cones

**Definitions 9.5.1.** *(1) Let $f : E' \to E$ be a morphism of simplicial sets. Recall (cf. for example [Del74], 6.3.1)
that one denotes by $C(f)$ the pointed simplicial set whose underlying set in degree $n \geqslant 0$ is*

<!-- label: III.X.9.5.1 -->

```text
E_n ∐ (∐_{i < n} E′_i) ∐ ⋆,
```

*where $\star$ is a singleton. We leave to the reader the task of defining the simplicial maps, the definition of the
faces in rank less than or equal to two being recalled below. (See also [GZ67], VI.2 for a pointed variant.) The
category of locally constant sheaves on $C(f)$ is equivalent to the category of locally constant sheaves on $E$ equipped
with a trivialization of the inverse image on $E'$. The simplicial set $C(f)$ is naturally pointed by $\star \to C(f)$.*

*(2) Let $f : T' \to T$ be a morphism of topoi. Denote by $C(f)$ the topos whose objects are quintuples* $(F, F', A,
\alpha : f^{\ast} F \to F', \beta : A \to \Gamma(T', F'))$, *where $F$ (resp. $F'$) is an object of $T$ (resp. $T'$),
$A$ is a set, and $\alpha$ (resp. $\beta$) is a morphism in $T'$ (resp. Ens). (See also [Del80], 4.3.4 and [Ill72],
III.4 for a variant of this construction.) The category of locally constant sheaves on $C(f)$ is equivalent to the
category of locally constant sheaves on $T$ equipped with a trivialization of* <!-- original page 104 --> *the inverse
image on $T'$. The topos $C(f)$ is naturally pointed by the fiber functor sending the quintuple $(F, F', A, \alpha :
f^{\ast} F \to F', \beta : A \to \Gamma(T', F'))$ to the set $A$.*

*(3) Let $f : G' \to G$ be a morphism of groupoids. Denote by $C(f)$ the colimit of the diagram*

$$ G \leftarrow G' \to B_{1} $$

*where `B_1` is the punctual category (one object, one arrow). The category of locally constant sheaves on $C(f)$ is
equivalent to the category of locally constant sheaves on $G$ equipped with a trivialization of the inverse image on
$G'$.*

*(4) Let $f : X' \to X$ be a morphism of topological spaces. Denote by $C(f)$ the colimit of the diagram*

```text
⋆ ← X′ × {0} → X′ × [0, 1] ← X′ × {1} → X.
```

*The category of locally constant sheaves on $C(f)$ is equivalent to the category of locally constant sheaves on $X$
equipped with a trivialization of the inverse image on $X'$. The topological space $C(f)$ is naturally pointed by $\star
\to C(f)$.*

#### 9.5.2. Descent data on the cone of a simplicial map

Let $f : E' \to E$ be a morphism of simplicial sets and $C(f)$ its cone (cf. supra, (1)). Let us use the letter $p$
(resp. $q$, $r$) to denote the face maps of $E'$ (resp. $E$, $C(f)$). Before stating the proposition below, let us
explicit the faces $r$ in degree less than or equal to two in terms of $p$ and $q$. By convention, $p_{ij}$ (resp.
$p_{i}$) is the face map $E'_{2} = E'_{\{1,2,3\}} \to E'_{1} = E'_{\{1,2\}}$ (resp. $E'_{1} = E'_{\{1,2\}} \to E'_{0} =
E'_{\{1\}}$) corresponding to the increasing map $\{1, 2\} \to \{1, 2, 3\}$ (resp. $\{1\} \to \{1, 2\}$) of image
`\{i, j\}` (resp. `\{i\}`)[^X-9-2]. The same convention is adopted for the faces of $E$ and $C(f)$.

The morphism

```text
r_1 : C(f)_1 = E_1 ∐ E′_0 ∐ ⋆ → C(f)_0 = E_0 ∐ ⋆
```

(resp. $r_{2}$) is:

– $q_{1} : E_{1} \to E_{0}$ (resp. $q_{2} : E_{1} \to E_{0}$) on `E_1`;

– $E'_{0} \to \star$ (resp. $f_{0} : E'_{0} \to E_{0}$) on $E'_{0}$;

– $\star \to \star$ on $\star$.

Likewise the morphism

```text
r_{21} : C(f)_2 = E_2 ∐ E′_1 ∐ E′_0 ∐ ⋆ → C(f)_1 = E_1 ∐ E′_0 ∐ ⋆
```

(resp. $r_{32}$, $r_{31}$) is:

– $q_{21} : E_{2} \to E_{1}$ (resp. $q_{32}$, $q_{31}$) on `E_2`;

– $p_{1} : E'_{1} \to E'_{0}$ (resp. $f_{1} : E'_{1} \to E_{1}$, $p_{2} : E'_{1} \to E'_{0}$) on $E'_{1}$;

– $E'_{0} \to \star$ (resp. $Id : E'_{0} \to E'_{0}$, $Id : E'_{0} \to E'_{0}$) on $E'_{0}$.

Let $H$ be a descent datum on $C(f)$, that is, a sheaf `H_0` on $C(f)_{0} = E_{0} \coprod \star$ equipped with an
isomorphism $\gamma : r^{\ast}_{1} H_{0} \xrightarrow{\sim} r^{\ast}_{2} H_{0}$ between its inverse images on $C(f)_{1}
= E_{1} \coprod E'_{0} \coprod \star$ satisfying the cocycle relation $r^{\ast}_{31} \gamma = r^{\ast}_{32} \gamma \circ
r^{\ast}_{21} \gamma$.

<!-- original page 105 -->

The restriction of the isomorphism $\gamma$ to `E_1` (resp. $E'_{0}$) is a descent datum $\beta : q^{\ast}_{1} G_{0}
\xrightarrow{\sim} q^{\ast}_{2} G_{0}$ where `G_0` is the restriction of `H_0` to `E_0` (resp. a trivialization $t :
H_{0}(\star) \xrightarrow{\sim} f^{\ast} G_{0} =: F_{0}$ where $H_{0}(\star)$ is the constant sheaf with stalk
$H_{0}(\star)$). The restriction of the cocycle relation satisfied by $\gamma$ to `E_2` (resp. $E'_{1}$) is the cocycle
relation for $\beta$ (resp. $p^{\ast}_{2}(t) = f^{\ast}_{1}(\beta) \circ p^{\ast}_{1}(t)$). This latter relation means
that the trivialization $t$ is compatible with the descent datum $f^{\ast}_{1}(\beta)$ induced by $\beta$ on `F_0`. From
this it follows:

**Proposition 9.5.3.** *Let $f : E' \to E$ be a morphism of simplicial sets and $C(f)$ its cone, pointed by $\star$. The
category of descent data on $C(f)$ trivialized over $\star$ is equivalent to the category of descent data on $E$
equipped with a trivialization of the descent datum induced on $E'$.*

<!-- label: III.X.9.5.3 -->

### 9.6. Representability of the functor π̄¹(S′/S, ξ; −)

The notations are those of page 90 and from now on we suppose the connected components of $S_{0} = S'$ and $S_{1} = S'
\times_{S} S'$ open. Under this hypothesis, one has the following explicit combinatorial description, which follows
immediately from the recalls above.

**Proposition 9.6.1.** *For every group $G$, the set $\bar{\pi}^{1}(S'/S, \xi; G)$ of isomorphism classes of descent
data equipped with a trivialization above $\xi$ is in natural bijection with the relative non-abelian cohomology set*

<!-- label: III.X.9.6.1 -->

```text
H^1(K rel k, G) := H^1(K̃ rel ⋆, G).
```

It follows that this functor is representable by a group, denoted $\pi_{1}(K, k)$ (the "*relative fundamental group*"),
as soon as the simplicial set $\tilde{K} = C(k \to K)$ is connected. One verifies immediately that this is so if and
only if the map $\pi_{0}(k) \to \pi_{0}(K)$ is surjective. It suffices in particular that the simplicial set $K$ be
connected. As indicated in the text, this is the case if the scheme $S$ is connected and the morphism $S' \to S$ is
universally submersive.

### 9.7. Contractibility of k, counter-example to the injectivity of k\_• → K\_•

The two following propositions make the N.D.E. (53) more precise.

**Proposition 9.7.1.** *Let $\kappa$ be an algebraically closed field, and $X$ a connected $\kappa$-scheme. For every
integer $i \geqslant 0$, denote by $X_{i}$ the $(i + 1)$-th fibered power of $X$ over $\kappa$. For every integer $i
\geqslant 0$, the canonical map*

<!-- label: III.X.9.7.1 -->

$$ \pi_{0}(X_{i}) \to \pi_{0}(X)^{i+1} $$

*is a bijection. In particular, the simplicial set $\pi_{0}(X_{\bullet})$ is contractible.*

It suffices to prove the following lemma, which follows by passage to the limit from the Künneth formula. [Spell out?]

**Lemma 9.7.2.** *Let $\kappa$ be an algebraically closed field and $X$, $Y$ two connected $\kappa$-schemes. Then the
fibered product $X \times_{\kappa} Y$ is connected.*

<!-- label: III.X.9.7.2 -->

**Proposition 9.7.3.** *Let $X$ be a connected scheme, $X' \to X$ a finite étale morphism, and $x$ a geometric point of
$X$ localized at a point $x$. The canonical morphism $\pi_{0}(X'_{x}) \to \pi_{0}(X')$ is surjective.*

<!-- label: III.X.9.7.3 -->

<!-- original page 106 -->

Indeed, every connected component of $X'$ has image an open-closed of $X$ hence meets the fiber $X'_{x}$. The morphism
$\pi_{0}(X'_{x}) \to \pi_{0}(X')$ is therefore surjective, as is the morphism $\pi_{0}(X^{'}_{x}) \to \pi_{0}(X'_{x})$.

## Bibliography

[^X-biblio]

- **[BAC]** N. Bourbaki, *Algèbre commutative*, Chap. I–IV, Hermann, 1961, Masson, 1985, Springer-Verlag, 2006.
- **[BEns]** N. Bourbaki, *Théorie des ensembles*, Chap. I–IV, Hermann, 1970.
- **[Pes66]** C. Peskine, *Une généralisation du « Main Theorem » de Zariski*, Bull. Sci. Math. **90** (1966), 119–127.
- **[PY06]** G. Prasad, J.-K. Yu, *On quasi-reductive group schemes*, J. Alg. Geom. **15** (2006), 507–549.
- **[Ray70]** M. Raynaud, *Anneaux locaux henséliens*, Lect. Notes Maths. **169**, Springer-Verlag, 1970.
- **[AM69]** M. Artin & B. Mazur, *Etale homotopy*, Lect. Notes Maths **100**, Springer, 1969.
- **[Del74]** P. Deligne, *Théorie de Hodge III*, Publ. Math. IHÉS **44** (1974), 5–77.
- **[Del80]** P. Deligne, *La conjecture de Weil II*, Publ. Math. IHÉS **52** (1980), 137–252.
- **[Fri82]** E. M. Friedlander, *Etale homotopy of simplicial schemes*, Princeton Univ. Press, 1982.
- **[GZ67]** P. Gabriel & M. Zisman, *Calculus of fractions and homotopy theory*, Springer, 1967.
- **[Ill72]** L. Illusie, *Complexe cotangent et déformations I & II*, Lect. Notes Maths **239** & **283**, Springer,
  1971 & 1972.
- **[Kan58]** D. Kan, *A combinatorial definition of homotopy groups*, Ann. of Math. **67** (1958), 282–312.
- **[May67]** J. P. May, *Simplicial objects in algebraic topology*, Univ. of Chicago Press, 1967.

<!-- LEDGER DELTA — Exposé X — for consolidation in Phase 3

| French                                     | English                                          | Note                                                                                                                                                                  |
| ------------------------------------------ | ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| revêtement principal                       | principal cover                                  | When `Γ`-Galois cover of a connected base; matches SGA 1, V.                                                                                                          |
| déployé / déploie                          | split / splits                                   | Per N.D.E. (4), the editors replaced "splitté" with "déployé"; we render uniformly as "split".                                                                        |
| à engendrement fini                        | finitely generated                               | Used for a twisted constant commutative group whose type at every point is a finitely generated `ℤ`-module. Not the same as the schematic "of finite type".           |
| fibré principal galoisien                  | Galois principal bundle                          | Principal homogeneous bundle with constant `G_S` structural group.                                                                                                    |
| groupe fondamental élargi                  | enlarged fundamental group                       | Grothendieck's term for the group attached to the full pro-system, not just its finite quotients.                                                                     |
| pro-groupe fondamental élargi              | enlarged fundamental pro-group                   | The projective system `Π = (π_i)_{i ∈ I}` itself.                                                                                                                     |
| anneau hensélisé                           | henselized ring                                  | `A^h`, the inductive limit of étale local neighborhoods of `s` with trivial residue extension.                                                                        |
| critère local de platitude                 | local criterion of flatness                      | Standard EGA terminology.                                                                                                                                             |
| point géométrique                          | geometric point                                  | Spectrum of an algebraically closed field, with a chosen map into `S`.                                                                                                |
| rang abélien / réductif / nilpotent / unipotent | abelian / reductive / nilpotent / unipotent rank | The four numerical invariants of a smooth algebraic group introduced in 8.7.                                                                                          |
| dimension semi-simple                      | semisimple dimension                             | The dimension of `G / radical`, denoted `d_s(G)`.                                                                                                                     |
| théorème principal de Zariski              | Zariski's main theorem                           | Standard. Also rendered "Main Theorem" when the original used English quotes.                                                                                         |
| théorème de quasi-isotrivialité            | quasi-isotriviality theorem                      | The principal theorem of §4 (Theorem 4.4 and Corollary 4.5).                                                                                                          |
| ensemble simplicial pointé                 | pointed simplicial set                           | Per §9.1–9.5.                                                                                                                                                         |
| topos simplicial                           | simplicial topos                                 | Per §9.1.                                                                                                                                                             |
| réalisation géométrique                    | geometric realization                            | Standard.                                                                                                                                                             |
| groupoïde ponctuel                         | punctual groupoid                                | A groupoid with one object and one automorphism group `H`; `BH` notation.                                                                                             |
| cocycle                                    | cocycle                                          | In descent data.                                                                                                                                                      |
| données de descente                        | descent data                                     | Standard.                                                                                                                                                             |
| morphisme universellement submersif         | universally submersive morphism                  | Per SGA 1, IV 2.1.                                                                                                                                                    |
| données de descente effective              | effective descent datum                          | Standard.                                                                                                                                                             |
| « partie finie »                            | "finite part"                                    | Per the decomposition `(∗)` in the proof of 4.3.                                                                                                                      |
| caractérisation                            | characterization                                 | Per Exposé title.                                                                                                                                                     |
| classification                             | classification                                   | Per Exposé title.                                                                                                                                                     |
-->

[^X-0-0]: Version xy of 6 November 2009: Addenda placed in Section 9, reviewed through 8.8.

[^N.D.E-X-1]: *N.D.E.* More precisely, this follows from the "axiomatic conditions of a Galois theory", cf. SGA 1, V N°
    4 g); when $S$ is locally noetherian, the verification of the axioms is done in *loc. cit.*, N°s 7 & 3, in
    particular 3.7, which rests on SGA 1, I 10.9. This last result is proved, without noetherian hypotheses, in EGA IV₄,
    18.2.9.

[^N.D.E-X-2]: *N.D.E.* In the sequel, one will say that an $S$-group of multiplicative type is "split" if it is
    "trivial" in the sense of IX 1.2, i.e., if it is a diagonalizable $S$-group.

[^N.D.E-X-3]: *N.D.E.* One has corrected $S$ to $S'$.

[^N.D.E-X-4]: *N.D.E.* One has replaced, here and in the sequel, "splittés" by "déployés", "splitte" by "déploie", etc.
    (In English: "split".)

[^N.D.E-X-5]: *N.D.E.* See 7.3 below.

[^N.D.E-X-6]: *N.D.E.* One has added this "recall", for later references.

[^N.D.E-X-7]: *N.D.E.* One has corrected the original by exchanging $M$ and $N$ in the right-hand terms.

[^X-2-1]: Cf. J. Giraud, *Méthode de la descente*, Bull. Soc. Math. France, Mémoire 2 (1964).

[^N.D.E-X-8]: *N.D.E.* One recalls that 2.3 is used to prove Theorem IX 3.6 bis.

[^N.D.E-X-9]: *N.D.E.* Since $u_{0}$ is an isomorphism, it suffices to see that for every $h \in H$, the morphism
    $\phi : O_{G,u(h)} \to O_{H,h}$ is bijective. It is so by reduction modulo $I = I_{s}$ (where $s$ is the image of
    $h$ in $S$), so its cokernel $C$ verifies $C = IC$, whence $C = 0$ since $I$ is nilpotent. Then, since $O_{H,h}$ is
    flat over $O_{S,s}$, the kernel $K$ of $\phi$ also verifies $K = IK$, whence $K = 0$.

[^N.D.E-X-10]: *N.D.E.* One has rewritten the statement keeping only the non-trivial implication, to bring it into
    focus.

[^N.D.E-X-11]: *N.D.E.* Spell out this point ….

[^N.D.E-X-12]: *N.D.E.* One has spelled out the original in what follows.

[^N.D.E-X-13]: *N.D.E.* Specify this reference, possibly adding a corollary in N° 5 ….

[^X-3-1]: Cf. also VI_B 2.5 for more systematic developments of this nature.

[^N.D.E-X-14]: *N.D.E.* Specify these references: Since $G$, $H$ are locally of finite presentation, $u$ is locally of
    finite presentation (IV₁, 1.4.3 (v)); next one applies IV₃, 11.3.10 and 13.1.4 for flat and quasi-finite, IV₄,
    17.4.1, 17.5.1 and 17.6.1 for unramified, smooth and étale; compare with VI_B 2.5.

[^N.D.E-X-15]: *N.D.E.* One has added the following sentence.

[^N.D.E-X-16]: *N.D.E.* One has added the following sentence.

[^N.D.E-X-17]: *N.D.E.* Cf. EGA IV₄, 17.9.1.

[^N.D.E-X-18]: *N.D.E.* The original indicated: "i.e. `S_0` connected". Note that, since $A$ is separated for the
    $I$-adic topology, `S_0` meets every connected component of $S$ (and since $A$ is complete, the connected components
    of `S_0` and $S$ are in bijection).

[^N.D.E-X-19]: *N.D.E.* since $G_{s}$ and $H_{s}$ are of the same type for every $s \in S_{0}$, hence for every $s$.

[^N.D.E-X-20]: *N.D.E.* because $u$ will once again be a surjective open immersion.

[^N.D.E-X-21]: *N.D.E.* One has spelled out this recall, and added remark 4.0.1.

[^N.D.E-X-22]: *N.D.E.* One has added what follows.

[^N.D.E-X-23]: *N.D.E.* One has spelled out the original in what follows.

[^N.D.E-X-24]: *N.D.E.* One has added this recall, used in the proof of 4.3 (the reference to EGA IV₄ 18.5.11 not being
    fully satisfactory).

[^N.D.E-X-25]: *N.D.E.* One has spelled out the original in what follows, on the basis of indications by M. Raynaud.

[^N.D.E-X-26]: *N.D.E.* One has added this lemma, used several times in the sequel.

[^N.D.E-X-27]: *N.D.E.* One has spelled out the reductions that follow (the original indicated: "One reduces at once to
    the case where $S$ is the spectrum of a noetherian local ring $A$, and where $s$ is the closed point of $S$.").

[^X-4-1]: Or
    [EGA IV₄, § 18.6](https://jcreinhold.github.io/ega/iv/31-ch4-18-complements-etale-morphisms.html#186-henselization).

[^N.D.E-X-28]: *N.D.E.* One has spelled out the original in what precedes and what follows.

[^N.D.E-X-29]: *N.D.E.* This result is generalized in 8.1: it suffices in fact to suppose that the fibers of $H$ are
    affine and connected.

[^N.D.E-X-30]: *N.D.E.* See lemma 5.12 below.

[^N.D.E-X-31]: *N.D.E.* One has moved this remark here, appearing in the original after the proof.

[^N.D.E-X-32]: *N.D.E.* cf. VIII § 1.7.

[^N.D.E-X-33]: *N.D.E.* One has corrected "equivalence" to "anti-equivalence".

[^N.D.E-X-34]: *N.D.E.* (when $S'$ is locally noetherian, and
    [EGA IV₃, 8.11.2](https://jcreinhold.github.io/ega/iv/21-ch4-08-projective-limits.html#811-application-to-quasi-finite-morphisms)
    in general).

[^N.D.E-X-35]: *N.D.E.* (when $S'$ is locally noetherian, and
    [EGA IV₂, 2.4.6](https://jcreinhold.github.io/ega/iv/14-ch4-02-base-change-and-flatness.html#24-universally-open-morphisms-and-flat-morphisms)
    in general).

[^N.D.E-X-36]: *N.D.E.* One has corrected $H$ to $G$.

[^N.D.E-X-37]: *N.D.E.* One has added what follows.

[^N.D.E-X-38]: *N.D.E.* Correct this reference by treating the case of the functor $Isom_{S-gr.}(H, G)$ in an addition
    1.5.1 in VIII ….

[^N.D.E-X-39]: *N.D.E.* One has added this recall, used several times in the sequel. (See also
    [EGA I, 6.1.9](https://jcreinhold.github.io/ega/i/01-06-finiteness-conditions.html#61-noetherian-and-locally-noetherian-preschemes);
    note however that the proof of *loc. cit.* seems unnecessarily complicated.)

[^N.D.E-X-40]: *N.D.E.* Compare with the examples of 1.6 ….

[^N.D.E-X-41]: *N.D.E.* One has spelled out the original in what follows.

[^N.D.E-X-42]: *N.D.E.* because it is a twisted constant group of type $\operatorname{End}_{gr.}(N)$ (cf. 5.6 and 5.8).

[^N.D.E-X-43]: *N.D.E.* modulo the verification that (ii) ⇒ (i) when $S$ is locally noetherian and $R$ is not finitely
    generated ….

[^N.D.E-X-44]: *N.D.E.* Spell out this point: $M$ being a finitely generated $\mathbb{Z}$-module, it is countable, and
    the proof of 5.11 (i) ⇒ (ii) shows that $R$ is the union of a countable family of open and closed parts, finite over
    $S$. One would need to see the converse ….

[^N.D.E-X-45]: *N.D.E.* The original treated in 5.14 the case where $S$ is locally noetherian and normal, and signalled
    in Remark 5.15 that the reasoning applies, more generally, if one supposes only $S$ geometrically unibranch instead
    of normal. One has modified the statement of 5.14 (and also 5.16) accordingly, and one has added these "recalls",
    drawn from
    [EGA IV₄, 18.10.6](https://jcreinhold.github.io/ega/iv/31-ch4-18-complements-etale-morphisms.html#1810-étale-preschemes-over-a-geometrically-unibranch-or-normal-prescheme)
    and 18.10.7, which show that the proof of 5.14 applies verbatim to the geometrically unibranch case.

[^N.D.E-X-46]: *N.D.E.* One has removed remark 5.15, rendered obsolete by the addition of 5.14.0 (cf. the preceding
    N.D.E.), and in 5.16 one has replaced "normal" by "geometrically unibranch".

[^N.D.E-X-47]: *N.D.E.* Note that $P$ is supposed to be a prescheme — in the *a priori* more general case of a sheaf
    (fpqc) $P$ which is a `G_S`-torsor, is $P$ necessarily representable?

[^N.D.E-X-48]: *N.D.E.* One has added the hypothesis that the connected components of $S'$ be open, as well as the
    second hypothesis. This latter means that the simplicial set $K_{\bullet} = \pi_{0}(S_{\bullet})$ defined in 6.3 is
    connected; in fact a weaker hypothesis suffices, namely that the cone $\tilde{K}_{\bullet}$ of a certain morphism of
    simplicial sets $k_{\bullet} \to K_{\bullet}$ be connected (cf. *loc. cit.*).

[^N.D.E-X-49]: *N.D.E.* One has suppressed the superfluous hypothesis that the connected components of $S'''$ be open.
    On the other hand, the description given later (cf. …) gives as the natural set of generators the set $\pi_{0}(S'')
    \coprod \pi_{0}(S'_{\xi})$; one then reduces to $\pi_{0}(S'')$ by means of the relations between these generators
    arising from the 2-cells. See for example [Kan58], § 19 for a finer description.

[^N.D.E-X-50]: *N.D.E.* One could spell out this deduction; $I$ is in bijection with a cofinal set of morphisms $S' \to
    S$ covering for the étale topology ….

[^N.D.E-X-51]: *N.D.E.* One has corrected 5.13 to 5.14.

[^N.D.E-X-52]: *N.D.E.* Some authors speak of the "true" fundamental group.

[^N.D.E-X-53]: *N.D.E.* One has corrected the original, which considers $\tilde{K}_{\bullet} = K_{\bullet}/k_{\bullet}$
    whereas on the one hand $k_{\bullet}$ is already contractible (cf. 9.7.1) and on the other hand the morphism
    $k_{\bullet} \to K_{\bullet}$ is not in general injective. It is an epimorphism if $S'/S$ is étale finite (cf.
    9.7.3).

[^N.D.E-X-54]: *N.D.E.* One has added the hypothesis that $\tilde{K}_{\bullet}$ be connected; for the proof, see the
    addendum below (Section 9).

[^N.D.E-X-55]: *N.D.E.* One has modified the sequel, taking into account the correction made above, cf. N.D.E. (53).
    (The original was: "$\pi_{0}(\tilde{K}_{\bullet}, \tilde{\xi})$ is also canonically isomorphic to the set
    $\pi_{0}(S, \xi)$ of connected components of $S$, pointed by the connected component of $\xi$ in $S$".)

[^N.D.E-X-56]: *N.D.E.* One could spell this out: first, taking into account 5.14, the enlarged fundamental group of the
    projective line $P^{1}_{k}$ is zero, i.e. $P^{1}_{k}$ is "truly" simply connected. Next, one would have to extend to
    the case of the enlarged fundamental group and the category of principal bundles (not necessarily finite), Corollary
    5.4 of SGA 1 IX and the discussion that follows. (Let $\Gamma_{1}$ and $\Gamma_{2}$ be two copies of $P^{1}_{k}$,
    $a_{i}$, $b_{i}$ two distinct points of $\Gamma_{i}$, $C''_{2}$ the disjoint union of $\Gamma_{1}$ and $\Gamma_{2}$,
    $C'_{2}$ the curve obtained by identifying $a_{1}$ with $a_{2}$; then `C_2` is obtained from $C'_{2}$ by
    additionally identifying $b_{1}$ with $b_{2}$. The discussion following *loc. cit.*, extended to the enlarged case,
    then shows that the enlarged fundamental group of $C'_{2}$ (resp. `C_2`) is zero (resp. $\mathbb{Z}$).

[^N.D.E-X-57]: *N.D.E.* This is an $n$-fold point with $n$ distinct tangents, for example the curve $X^{n} - Y^{n} =
    X^{n+1}$.

[^N.D.E-X-58]: *N.D.E.* In particular, this shows that the tori of relative dimension 2 considered in 1.6 are not
    isotrivial.

[^N.D.E-X-59]: *N.D.E.* Note that the hypotheses entail that $H$ is separated over $S$, by VI_B, Th. 5.3 or Cor. 5.5.

[^N.D.E-X-60]: *N.D.E.* by EGA IV₂, 8.8.2 again.

[^N.D.E-X-61]: *N.D.E.* One has spelled out the original in what follows.

[^X-8-1]: By Raynaud's theorem VI_B 5.3.

[^N.D.E-X-62]: *N.D.E.* Spell out this point, in connection with the modifications in VI_B § 5.

[^N.D.E-X-63]: *N.D.E.* This follows, for example, from VIII 3.2 a); more generally, if $f : G \to H$ is a surjective
    morphism of algebraic groups over a field $k$ and if $H$ is reduced, then $f$ is flat (cf. VI_B 1.3).

[^N.D.E-X-64]: *N.D.E.* One has spelled out the original in what follows.

[^N.D.E-X-65]: *N.D.E.* At least in the case envisaged so far, namely $S$ locally noetherian.

[^N.D.E-X-66]: *N.D.E.* The editors did not understand this remark, not understanding why $u$ would *a priori* have
    finite fibers and be surjective ….

[^N.D.E-X-67]: *N.D.E.* Spell out this reduction ….

[^N.D.E-X-68]: *N.D.E.* Spell out this point ….

[^N.D.E-X-69]: *N.D.E.* Give a reference here?

[^N.D.E-X-70]: *N.D.E.* Recall the definition of "Cartan subgroup" ….

[^N.D.E-X-71]: *N.D.E.* Give a reference for these results?

[^N.D.E-X-72]: *N.D.E.* G. Prasad and J.-K. Yu have generalized (subject to some additional hypotheses) this result
    without supposing $G$ commutative and replacing in hypothesis a) and the conclusion "torus" by "reductive group",
    cf. [PY06], Th. 6.2.

[^X-8-2]: By Raynaud's theorem VI_B 5.3.

[^N.D.E-X-73]: *N.D.E.* cf. N.D.E. (62) in 8.5.

[^N.D.E-X-74]: *N.D.E.* revise the preceding sentence ….

[^N.D.E-X-75]: *N.D.E.* This additional section was written by Fabrice Orgogozo (following indications by Ofer Gabber).

[^X-9-1]: PP: I have replaced "FGA, *Technique de descente* I, 1.6" by "Exp. IV, 2.1".

[^X-9-2]: This convention departs from the current simplicial norm but is closer to the notations used by Grothendieck
    in his theory of descent.

[^X-biblio]: *N.D.E.* additional references cited in this Exposé; the references [AM69] and following concern the
    Addenda.
