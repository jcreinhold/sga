# Exposé VIII. The finiteness theorem

<!-- label: VIII -->

<!-- original page 67 -->

<!-- TRANSLATOR NOTE: per the SGA 2 glossary, the sheafified section functor (underlined `ΓZ` in the source) is
rendered with a script-H in cohomological degrees, so `ℋ^i_Y(F)` denotes the sheafified local-cohomology functor and
`H^i_Y(X, F)` its global version. -->

## 1. A biduality spectral sequence[^VIII-1-1]

<!-- label: VIII.1 -->

Let us state the result we want to reach:

**Proposition.**

<!-- label: VIII.1.1 -->

Let `A` be a noetherian ring and let `I` be an ideal of `A`. Set `X = Spec(A)` and `Y = V(I)`. Let `M` be a finitely
generated `A`-module of finite projective dimension. Let `F = M̃` be the `𝒪_X`-Module associated with `M`.

1. There exists a spectral sequence

```text
E₂^{p,q} = Ext^p_Y(Ext^{-q}(M, A), A) ⇒ H^{p+q}_Y(X, F).
```

2. There exists a spectral sequence

```text
E₂^{p,q} = Ext^p_Y(Ext^{-q}(F, 𝒪_X), 𝒪_X) ⇒ H^{p+q}_Y(X, F).
```


Of course, 2) is deduced from 1) by remarking that, if `M` and `N` are two finitely generated `A`-modules, and if one
sets `F = M̃` and `G = Ñ`, then one has isomorphisms

```text
ℋ^•_Y(F) ≅ H̃^•_Y(X, F),
Ext^•_Y(F, G) ≅ Ẽxt^•_Y(F, G),
Ext^•_{𝒪_X}(F, G) ≅ Ẽxt^•_A(M, N).
```

Let `C` be the category of `A`-modules and `Ab` that of abelian groups. Let `F` be the functor

```text
F : C → Ab    defined by    M ↦ Γ_Y(M̃).
```

We know from Exposé II that there is an isomorphism of `∂`-functors

```text
H^•_Y(X, M̃) ≅ R^• F(M).
```

<!-- original page 68 -->

Furthermore, let `Ext^•_Y` denote the right derived functors in the second argument of

```text
F ∘ Hom : C° × C → Ab.
```

We know from Exposé VI that there is an isomorphism of `∂`-functors

```text
Ext^•_Y(M, N) ≃ Ext^•_Y(M̃, Ñ).
```

Let us finally record the following result from Exposé VI: if `C` is an injective `A`-module and `N` is a finitely
generated `A`-module, then the sheaf `Hom(Ñ, C̃) ≅ Hom(N, C)̃` is flasque, hence

```text
R¹ F(Hom(N, C)) = 0.
```

It remains to prove the following result:

**Lemma.**

<!-- label: VIII.1.2 -->

Let `A` be a noetherian ring and let `C` be the category of `A`-modules. Let `F : C → Ab` be a left exact additive
functor such that, for every finitely generated `A`-module `N` and every injective `A`-module `C`, one has
`R¹ F(Hom(N, C)) = 0`. Let `M` be a finitely generated `A`-module of finite projective dimension. Then there exists a
spectral sequence

```text
E₂^{p,q} = Ext^p_F(Ext^{-q}(M, A), A) ⇒ R^{p+q} F(M),
```

where `Ext^p_F` denotes the `p`-th right derived functor of `F ∘ Hom`.

We shall consider only complexes whose differential has degree `+1`. By the hypothesis on `M`, there exists a projective
resolution of `M` of finite length

```text
u : L^• → M,
```

where, moreover, the `L^p` are finitely generated modules and `L^p = 0` if `p ∉ [−n, 0]`. Let, on the other hand,
`v : M → I^•` be an injective resolution of `M`. We claim that

```text
v ∘ u : L^• → I^•
```

<!-- label: eq:VIII.1.1 -->

is an injective resolution of `L^•`. We must specify what this means.

**Definition.**

<!-- label: VIII.1.3 -->

Let `X^•` be a complex of `A`-modules; by an *injective resolution* of `X^•` one means a homomorphism of complexes

```text
x : X^• → C_X^•,
```

such that `C_X^p` is injective for every `p ∈ ℤ`, and such that `x` induces an isomorphism on homology.

**Proposition.**

<!-- label: VIII.1.4 -->

Every left-bounded complex — i.e. such that there exists `q ∈ ℤ` with `X^p = 0` for `p < q` — admits an injective
resolution. Moreover, if `u : X^• → Y^•` is a homomorphism of complexes (both left-bounded) and if `x : X^• → C_X^•` and
`y : Y^• → C_Y^•` are injective resolutions of `X^•` and `Y^•`, then there exists a homomorphism of complexes

```text
C_u : C_X^• → C_Y^•,
```

<!-- original page 69 -->

unique up to homotopy, such that the diagram

```text
        x
X^•  ────────►  C_X^•
 │                │
 u                C_u
 │                │
 ▼      y         ▼
Y^•  ────────►  C_Y^•
```

is commutative up to homotopy.

The proof is left to the reader.[^VIII-1-2]

Let us recall a notation introduced in Exposé V.

**Notation.**

Let `X^•` and `Y^•` be two complexes. We denote by `Hom^•(X^•, Y^•)` the simple complex whose component of degree `n` is

```text
(Hom^•(X^•, Y^•))^n = ∏_{−p+q=n} Hom(X^p, Y^q),
```

also written `Hom^n(X^•, Y^•)`, and whose differential is given by

```text
∂^n : Hom^n(X^•, Y^•) → Hom^{n+1}(X^•, Y^•),
∂^n = d′ + (−1)^{n+1} d″,
```

where `d′` and `d″` are the differentials (of degree `+1`) induced by those of `X^•` and `Y^•`.

Let then `A^•` be the complex defined by `A^p = 0` if `p ≠ 0` and `A^0 = A`. Let

```text
a : A^• → C_A^•
```

be an injective resolution of `A^•`. Consider the double complex

```text
Q^{p,q} = Hom(Hom(L^{-q}, A), C_A^p).
```

<!-- label: eq:VIII.1.2 -->

The first spectral sequence of the bicomplex `F Q^{••}` will yield the conclusion of Lemma 1.2.

Set

```text
L′^• = Hom^•(L^•, A^•),
```

<!-- label: eq:VIII.1.3 -->

and

```text
P^• = Hom^•(L′^•, C_A^•).
```

<!-- label: eq:VIII.1.4 -->

One sees easily that `P^•` is the simple complex associated with `Q^{••}`. Let us compute the abutment of the spectral
sequence, i.e. the homology of `F P^•`. For this, using the fact that `L^•` is finitely generated projective in every
dimension, one proves that `L^•` is isomorphic to `Hom^•(L′^•, A^•)`. From the homomorphism `a : A^• → C_A^•` one
deduces a homomorphism

```text
b : Hom^•(L′^•, A^•) → Hom^•(L′^•, C_A^•),
```

or equivalently, a homomorphism

```text
c : L^• → P^•.
```

<!-- label: eq:VIII.1.5 -->

<!-- original page 70 -->

This being said, it is easy to see, using the fact that `L′^•` is finitely generated projective in every dimension and
left-bounded, that (1.5) is an injective resolution of `L^•`. Applying Proposition 1.4, one concludes that `P^•` is
homotopy-equivalent to `I^•`, where `I^•` is the injective resolution of `M` introduced earlier (1.1). One
deduces that the abutment of the first spectral sequence of the double complex `F Q^{••}`, which is `H^•(F P^•)`, is
isomorphic to `R^• F(M)`.

The initial term of the first spectral sequence of the bicomplex `F Q^{••}` is

```text
E₂^{p,q} = ′H^p(″H^q(F Q^{••})).
```

For every `p ∈ ℤ`, `C_A^p` is injective. By the hypothesis on `F`, the functor (restricted to the category of finitely
generated modules)

```text
N ↦ F Hom(N, C_A^p)
```

is exact. Hence one deduces isomorphisms

```text
″H^q(F Hom(L′^•, C_A^p)) ≅ F Hom(H^{-q}(L′^•), C_A^p).
```

By the definition of `Ext^•_F` as the derived functor of `F ∘ Hom`, one deduces isomorphisms

```text
E₂^{p,q} ≅ Ext^p_F(H^{-q}(L′^•), A).
```

Now `L′^• = Hom^•(L^•, A^•)`, where `L^•` is a projective resolution of `M`, whence isomorphisms

```text
Ext^{-q}(M, A) ≅ H^{-q}(L′^•),
```

which gives the conclusion. QED.

<!-- TRANSLATOR NOTE: the OCR carries `H^q(L′^•)` and `Ext^q(M, A) ≅ H^q(L′^•)` in this paragraph, with the sign of `q`
flipped relative to the intermediate step `″H^q(F Hom(L′^•, C_A^p)) ≅ F Hom(H^{-q}(L′^•), C_A^p)` (line 184-185 of the
source) and relative to the statement of Proposition 1.1 (whose `Ext^{-q}(M, A)` indexes the spectral sequence the
same way). The sign `−q` is the one consistent with both ends of the proof; this is rendered above with the `−q`
convention. The universal isomorphism `Ext^q(M, A) ≅ H^q(L′^•)` is correct in either sign — the displayed form here is
just the `q ↦ −q` reindexing that aligns with E₂. -->


## 2. The finiteness theorem

<!-- label: VIII.2 -->

**Theorem.**[^N.D.E-VIII-1]

<!-- label: VIII.2.1 -->

Let `X` be a locally noetherian prescheme, `Y` a closed subset of `X`, and `F` a coherent `𝒪_X`-Module. Suppose that `X`
is locally embeddable in a regular prescheme.[^VIII-2-1] Let `i ∈ ℤ`. Suppose that:

a) for every `x ∈ U = X − Y`, one has

```text
H^{i-c(x)}(F_x) = 0,
```

<!-- original page 71 -->

where one has set[^N.D.E-VIII-2]

```text
c(x) = codim({x}̄ ∩ Y, {x}̄).
```

<!-- label: eq:VIII.2.1 -->

Then:

b) `ℋ^i_Y(F)` is coherent.

**Corollary.**[^N.D.E-VIII-3]

<!-- label: VIII.2.2 -->

Under the hypotheses of the preceding theorem, condition a) is equivalent to:

c) for every `x ∈ U` such that `c(x) = 1`, one has `H^{i-1}(F_x) = 0`.

**Corollary.**

<!-- label: VIII.2.3 -->

Let `X` be a locally noetherian prescheme that is locally embeddable in a regular prescheme, let `Y` be a closed subset
of `X`, let `F` be a coherent `𝒪_X`-Module, and let `n` be an integer. The following conditions are equivalent:

(i) for every `x ∈ U`, one has `prof F_x > n − c(x)`;

(ii) for every `x ∈ U` such that `c(x) = 1`, one has `prof F_x ⩾ n`;

(iii) for every `i ∈ ℤ`, `ℋ^i_Y(F)` is coherent if `i ⩽ n`;

(iv) `R^i i_*(F|U)` is coherent for `i < n`.[^N.D.E-VIII-4]

Suppose these results acquired when `X` is the spectrum of a regular noetherian ring `A` and when `F` is the sheaf
associated with an `A`-module of finite projective dimension.

Let us first remark that, if `(X_j)_{j ∈ J}` is an open covering of `X` by opens embeddable in a regular scheme, then
each of the above conditions is equivalent to the conjunction of the analogous conditions obtained by replacing `X` by
`X_j`, `Y` by `Y_j = Y ∩ X_j`, and `F` by `F|X_j`. Indeed, only the conditions involving `c(x)` can present a
difficulty. Let `x ∈ U`. If `x ∈ X_j`, setting

```text
c_j(x) = codim(X_j ∩ {x}̄ ∩ Y, X_j ∩ {x}̄),
```

one has necessarily `c_j(x) ⩾ c(x)`. Let `y ∈ {x}̄ ∩ Y` which "gives the codimension", i.e. such that
`c(x) = dim 𝒪_{{x}̄, y}`, and let `X_j` be an open of the covering such that `y ∈ X_j`; then `x ∈ X_j`, hence
`c_j(x) = c(x)`, which lets us conclude that a) for the `X_j` implies a) for `X`.

<!-- original page 72 -->

At this stage, one has only a partial converse, namely that a) for `X` implies a) for the `X_j` such that
`c(x) = c_j(x)`, which suffices for our purposes.[^N.D.E-VIII-5]

One chooses a covering of `X` by opens embeddable in a regular prescheme. Applying the preceding, one sees that one can
suppose `X` closed in a regular `X′`. The reduction to `X′` is then immediate.

One can therefore suppose `X` regular, and even affine by covering `X` by affine opens. That one can suppose `F = M̃`,
where `M` is of finite projective dimension, will result from the following lemma:

**Lemma.**

<!-- label: VIII.2.4 -->

Let `X` be a regular noetherian prescheme. Let `F` be a coherent `𝒪_X`-Module. The function which to each `x ∈ X`
assigns the projective dimension of `F_x` is upper-bounded.

Indeed, let `x ∈ X` and let `U` be an affine open neighborhood of `x`. Let `L^•` be a projective resolution of the
module `F(U)`, where the `L^i` are finitely generated. By hypothesis, the ring `𝒪_{X,x}` is regular, hence the
projective dimension of `F_x` is finite; let `d` be that integer. Let

```text
K = ker(L^{-d} → L^{-d+1}).
```

The module `K_x` is free, because `d` is the projective dimension of `F_x` ([M], Ch. VI, Prop. 2.1). By
(EGA 0_I 5.4.1 Errata), one deduces that the `𝒪_U`-Module `K̃` is free on a neighborhood `U′` of `x`, with `U′ ⊂ U`.
Choosing `f ∈ 𝒪_X(U)` such that `x ∈ D(f) ⊂ U′`, one therefore has a projective resolution of `M_f` (with `M = F(U)`):

```text
0 → K_f → (L^{d-1})_f → ⋯ → M_f → 0,
```

which proves that the function under study is upper semi-continuous. Now `X` is quasi-compact, whence the conclusion.

We henceforth suppose `X` affine noetherian regular and we suppose that `F = M̃`, where `M` is a finitely generated
`A`-module, necessarily of finite projective dimension. We shall proceed in several steps. First, we find a condition
d), equivalent to a), and prove that it is also equivalent to c). Then, using the spectral sequence of the preceding
number, we prove d) ⇒ b). It then remains to prove that (iii) ⇒ (ii); indeed, (i) ⇔ (ii) ⇒ (iii) follows immediately
from a) ⇔ c) ⇒ b).

Let `x ∈ U`; by hypothesis `𝒪_{X,x}` is a regular local ring. Denoting by `D` the dualizing functor relative to the
local ring `𝒪_{X,x}`, it follows from (V 2.1) that

```text
D H^{i-c(x)}(F_x) ≅ Ext^{d(x)-i}_{𝒪_{X,x}}(F_x, 𝒪_{X,x}),
```

<!-- original page 73 -->

where one has set

```text
d(x) = dim 𝒪_{X,x} + c(x) = dim 𝒪_{X,x} + codim({x}̄ ∩ Y, {x}̄).
```

<!-- label: eq:VIII.2.2 -->

Now `X` is noetherian and `F` is coherent, hence

```text
D H^{i-c(x)}(F_x) ≅ (Ext^{d(x)-i}_{𝒪_X}(F, 𝒪_X))_x.
```

<!-- label: eq:VIII.2.3 -->

Moreover, for a module to be zero, it is necessary and sufficient that its dual be (cf. editor's note (4) on
page 54). For every `q ∈ ℤ`, set

```text
S_q = Supp Ext^q_{𝒪_X}(F, 𝒪_X),
S′_q = S_q ∩ U,    (U = X − Y),
Z_q = S̄′_q ∩ Y.
```

<!-- label: eq:VIII.2.4 -->

From formula (2.3), it follows that a) and c) are respectively equivalent to:

- a′) for every `q ∈ ℤ` and every `x ∈ S′_q`, one has `q + i ≠ d(x)`.
- c′) for every `q ∈ ℤ` and every `x ∈ S′_q`, if `c(x) = 1`, one has `q + i ≠ d(x)`.

Here is the condition d) promised above:

- d) for every `q ∈ ℤ` and every `y ∈ Z_q`, one has `q + i ≠ dim 𝒪_{X,y}`.

These conditions are equivalent:

a′) ⇒ c′) is trivial.

d) ⇒ a′). Indeed, let `q ∈ ℤ` and let `x ∈ S′_q`; let `y ∈ {x}̄ ∩ Y` which[^N.D.E-VIII-6] "gives the codimension", i.e.
such that

```text
dim 𝒪_{{x}̄, y} = codim({x}̄ ∩ Y, {x}̄) = c(x).
```

<!-- label: eq:VIII.2.5 -->

From the fact that `X` is regular at `y`, one deduces

```text
dim 𝒪_{X, y} = d(x)    (cf. (2.2)).
```

<!-- label: eq:VIII.2.6 -->

But `y ∈ {x}̄`, hence `y ∈ Z_q`, whence the conclusion.

c′) ⇒ d). Let `q ∈ ℤ` and let `y ∈ Z_q`. Provisionally admit that there exists `x ∈ S′_q` such that

```text
y ∈ {x}̄    and    dim 𝒪_{{x}̄, y} = 1
```

(one also says that `x` *follows* `y`). It follows that `c(x) = 1`, since `y` "gives the codimension of `{x}̄ ∩ Y` in
`{x}̄`", because `x ∉ Y`. By c′) we extract

```text
q + i ≠ d(x).
```

Whence the conclusion, on noting that `d(x) = dim 𝒪_{X, y}` (2.6). The admitted result is expressed in the following
lemma:

<!-- original page 74 -->

**Lemma.**

<!-- label: VIII.2.5 -->

Let `X` be a locally noetherian prescheme and let `Y` be a closed subset of `X`. Set `U = X − Y` and suppose that `U`
is dense in `X`. For every `y ∈ Y`, there exists `x ∈ U` "which follows it", i.e. such that

```text
y ∈ {x}̄    and    dim 𝒪_{{x}̄, y} = 1.
```

We have applied the lemma taking for `X` the prescheme `S̄′_q` and for `Y` the part `Y ∩ S̄′_q`.

*Proof of 2.5.* — There exists `x ∈ U` such that `y ∈ {x}̄`; let us therefore choose `x ∈ U` such that `y ∈ {x}̄` and
such that `dim 𝒪_{{x}̄, y} = r` be minimal. We must prove that `r = 1`. Since we have chosen `x` so that every
`z ∈ Spec(𝒪_{{x}̄, y})`, `z ≠ x`, lies in `Y`, `{x}` is open in `Spec(𝒪_{{x}̄, y})`. Whence the conclusion.

The second step consists in deducing b) from d).

Set `D(Z_q) = {dim 𝒪_{X,y} | y ∈ Z_q}`. By d), we know that, for every `q ∈ ℤ`, `q + i ∉ D(Z_q)`. One then applies
VII.2.3, and sees that

```text
Ext^{q+i}_Y(Ext^q(F, 𝒪_X), 𝒪_X)    is coherent.
```

The initial term of the spectral sequence of the preceding number is given by

```text
E₂^{p,q} = Ext^p_Y(Ext^{-q}(F, 𝒪_X), 𝒪_X).
```

One deduces that `E₂^{p,q}` is coherent for every `p ∈ ℤ` and every `q ∈ ℤ` such that `p + q = i`. Now there are only
finitely many pairs `(p, q)` with `p + q = i`, and this spectral sequence converges to `H^•_Y(F)`, whence the
conclusion.

It remains to prove that (iii) ⇒ (ii). Let us write

```text
i : U → X
```

for the canonical immersion of `U` in `X`. Taking into account the exact homology sequence of the closed subset `Y`
(I 2.11), one sees that (iii) is equivalent to:

(iv) `R^i i_*(F|U)` is coherent for `i < n`.

Indeed, one has an exact sequence

```text
0 → ℋ^0_Y(F) → F → i_*(F|U) → ℋ^1_Y(F) → 0.
```

Now `ℋ^0_Y(F)` is a quasi-coherent subsheaf of the coherent sheaf `F`, hence is coherent. Therefore `ℋ^1_Y(F)` is
coherent if and only if `i_*(F|U)` is. Moreover, for `p > 0`, the exact cohomology sequence of the closed subset `Y`
reduces to isomorphisms

```text
R^p i_*(F|U) ⥲ ℋ^{p+1}_Y(F).
```

We shall prove that (iv) ⇒ (ii). For this, recall (ii):

(ii) for every `x ∈ U` such that `c(x) = 1`, one has `prof F_x ⩾ n`.

We argue by induction on `n`.

If `n = 0`, the two conditions are empty.

<!-- original page 75 -->

If `n = 1`, one supposes that `i_*(F|U)` is coherent. Argue by contradiction and suppose there exists `x ∈ U` such that
`c(x) = 1` and `prof F_x = 0`, i.e. `x ∈ Ass F_x`. Let `y ∈ {x}̄ ∩ Y` such that `dim 𝒪_{{x}̄, y} = 1`. Set

```text
A = 𝒪_{X, y}    and    X′ = Spec(A).
```

Carry out the base change `v : X′ → X`, which is flat:

```text
            v′
   U′ = X′ ×_X U  ──────►  U
        │                   │
       i′                   i
        │                   │
        ▼          v        ▼
       X′  ──────────────► X.
```

<!-- label: eq:VIII.2.7 -->

The morphism `i` is separated (since it is an immersion), and of finite type (since it is an open immersion and `X` is
locally noetherian); the base change is flat, hence (EGA III 1.4.15) one has an isomorphism

```text
v^*(i_*(F|U)) ≅ i′_*(v′^*(F|U)).
```

<!-- label: eq:VIII.2.8 -->

Let us denote by `𝔵` (resp. `𝔶`) the ideal of `A` corresponding to `x` (resp. `y`). Set `G = v′^*(F|U)`; then `G` is
coherent and `𝔵 ∈ Ass G`, so there exists a monomorphism `𝒪_{{x}̄} → G`, and consequently `i′_*(𝒪_{{x}̄}|U′)` is
coherent. By the choice of `y`, `dim A/𝔵 = 1`, and consequently the support of `𝒪_{{x}̄}` is reduced to
`{x}̄ = {x} ∪ {y}`, since `{x}̄ = Spec(A/𝔵)` as a scheme. It follows that

```text
(𝒪_{{x}̄}|U′)(U′) = Frac(A/𝔵),
```

the field of fractions of `A/𝔵`, and

```text
i′_*(𝒪_{{x}̄}|U′)(X′) = Frac(A/𝔵).
```

But `Frac(A/𝔵)` is not a finitely generated `A`-module, because `𝔵` differs from the maximal ideal of `A`. Whence a
contradiction.

Suppose `n > 1` and that the result is acquired for the `n′ < n`. By the induction hypothesis, for every `x ∈ U` such
that `c(x) = 1`, one has `x ∉ Ass F_x`. Let such an `x`, and let `y ∈ {x}̄ ∩ Y` such that `x` follows `y`, i.e.
`dim 𝒪_{{x}̄, y} = 1`. Carry out the base change `v : Spec(𝒪_{X, y}) → X`, keeping the notation of diagram (2.7). One
finds, applying (EGA III 1.4.15), isomorphisms

```text
v^*(R^p i_*(F|U)) ≃ R^p i′_*(v′^*(F|U)),    p ∈ ℤ.
```

One thus reduces to the case where `X` is the spectrum of a local ring `A` in which `𝔵` is a prime ideal of dimension
`1`, i.e. `dim A/𝔵 = 1`. Then set `F′ = Γ_Y(F)` and `F″ = F/F′`. One sees that `F_x ≃ F″_x` and that `𝔶 ∉ Ass F″`.
Moreover `F′|U = 0`, whence, by the exact sequence of the `R^p i_*`, isomorphisms

```text
R^p i_*(F|U) ≃ R^p i_*(F″|U),    p ∈ ℤ.
```

<!-- original page 76 -->

Since `n > 1`, one deduces that neither `𝔵` nor `𝔶` belongs to `Ass F″`. Now `𝔵, 𝔶` are the only prime ideals of `A`
containing `𝔵`; it follows (III 2.1) that there exists an element `g ∈ 𝔵` which is `M`-regular, where one has set
`F = M̃`, `M = F(X)`. Whence an exact sequence

```text
0 → M ──g·→ M → N → 0,
```

in which `g·` denotes multiplication by `g` in `M`. By the exact homology sequence, one sees that

```text
R^p i_*(Ñ|U)    is coherent for p < n − 1,
```

hence, by the induction hypothesis, `prof(Ñ)_x ⩾ n − 1`, and therefore `prof F_x ⩾ n`. QED.

## 3. Applications

<!-- label: VIII.3 -->

One deduces from these results a coherence condition for the higher direct images of a coherent sheaf under a morphism
that is not proper.

**Theorem.**

<!-- label: VIII.3.1 -->

Let `f : X → Y` be a morphism of preschemes. Suppose that `Y` is locally noetherian and that `f` is proper. Suppose that
`X` is locally embeddable in a regular prescheme. Let `n ∈ ℤ`. Let `U` be an open of `X` and let `F` be a coherent
`𝒪_U`-Module. Suppose that, for every `x ∈ U` such that `codim({x}̄ ∩ (X − U), {x}̄) = 1`, one has `prof F_x ⩾ n`.
Then the `𝒪_Y`-Modules `R^p(f ∘ g)_*(F)` are coherent for `p < n`, where `g` is the canonical immersion of `U` in `X`.

Indeed, there exists a Leray spectral sequence whose abutment is `R^•(f ∘ g)_*(F)` and whose initial term is given by

```text
E₂^{p,q} = R^p f_*(R^q g_*(F)).
```

Moreover, there exists a coherent `𝒪_X`-Module `G` such that `G|U ≃ F` (EGA I 9.4.3). It then follows from the preceding
paragraph that condition (iv) of page 74 is satisfied, i.e. that `R^q g_*(G|U)` is coherent for `q < n`. One then
applies the finiteness theorem of EGA III 3.2.1 to `f` and to the sheaves `R^q g_*(F)`, and finds that `E₂^{p,q}` is
coherent for `q < n`, whence the conclusion.

**Proposition.**

<!-- label: VIII.3.2 -->

Let `X` be a locally noetherian prescheme that is locally embeddable in a regular prescheme. Let `U` be an open of `X`
and let `i : U → X` be the canonical immersion. Let `n ∈ ℤ`. Finally, let `F` be a coherent and Cohen-Macaulay
`𝒪_U`-Module (on `U`!). The following conditions are equivalent:

(a) `R^p i_*(F)` is coherent for `p < n`;

(b) for every irreducible component `S′` of the closure `S̄` of the support `S` of `F`, one has

```text
codim(S′ ∩ (X − U), S′) > n.
```

Let `G` be a coherent `𝒪_X`-Module such that `G|U ≃ F` (EGA I 9.4.3). Applying Corollary 2.3 to `G`, one finds that
condition (a) is equivalent to:

<!-- original page 77 -->

(c) for every `x ∈ S̄`, one has `prof F_x > n − c(x)`, with

```text
c(x) = codim({x}̄ ∩ Y, {x}̄).
```

(a) ⇒ (b). Indeed, let `S′` be an irreducible component of `S̄` and let `s` be its generic point. Since `F` is
Cohen-Macaulay, one has `prof F_s = dim 𝒪_{S̄, s} = 0`. Moreover, `{s}̄ = S′`, whence the conclusion.

(b) ⇒ (a). Let `x ∈ S̄` and let `S′` be an irreducible component of `S̄` such that `x ∈ S′`. Let `s` be the generic point
of `S′`. Since `F` is Cohen-Macaulay, one knows that

```text
prof F_x = dim 𝒪_{{s}̄, x}.
```

If `c(x) = +∞`, there is nothing to prove. Otherwise, there exists `y ∈ Y ∩ {x}̄` such that

```text
c(x) = dim 𝒪_{{x}̄, y}.
```

Now `𝒪_{X, y}` is a quotient of a regular local ring by hypothesis, hence

```text
dim 𝒪_{{s}̄, y} = dim 𝒪_{{s}̄, x} + dim 𝒪_{{x}̄, y} > n.
```

QED.

## Bibliography

1. [M] H. Cartan and S. Eilenberg, *Homological Algebra*, Princeton Math. Series vol. 19, Princeton University Press,
   1956.

[^VIII-1-1]: The reader familiar with the language of Verdier's derived categories will recognize the spectral sequence
    associated with a biduality isomorphism. Cf. SGA 6 I.

[^VIII-1-2]: Cf. also H. Cartan and S. Eilenberg, *Homological Algebra*, Princeton Math. Series, vol. 19, Princeton
    University Press, 1956.

[^VIII-2-1]: This condition can be generalized to the hypothesis of the existence locally on `X` of a "dualizing
    complex", in the sense defined in R. Hartshorne, *Residues and duality* (cited in footnote (*) of Exp. IV
    p. 46).

[^N.D.E-VIII-1]: *N.D.E.* For an analogous statement, but in a somewhat more general situation, see Mme Raynaud
    (Raynaud M., "Théorèmes de Lefschetz en cohomologie des faisceaux cohérents et en cohomologie étale. Application au
    groupe fondamental", *Ann. Sci. Éc. Norm. Sup.* (4) **7** (1974), pp. 29–52, proposition II.2.1).

[^N.D.E-VIII-2]: *N.D.E.* As in Exposé V, `H^•_x(F)` denotes the local cohomology `H^•_{𝔪_x}(F_x)`.

[^N.D.E-VIII-3]: *N.D.E.* Strictly speaking, this is a corollary of the proof that follows and not of the statement.
    The implication c) ⇒ a) is tautological. The other direction is not, but follows from the proof. To be precise: as
    below, one covers `X` by opens embeddable in regular schemes, which allows one, as explained below, to reduce to
    `X = Spec(A)` affine regular and `F = M̃` where `M` is an `A`-module of finite projective dimension. It is shown in
    this case that conditions a) and c) are equivalent to the dual conditions a′) and c′). One then shows that c′)
    implies condition d) (see below) which itself implies a′). See the considerations following 2.4.

[^N.D.E-VIII-4]: *N.D.E.* This condition appeared only in the body of the proof, but not in the statement of the
    corollary; since it is used in §3, we have added it.

[^N.D.E-VIII-5]: *N.D.E.* In fact, a) for `X` implies a) for all the `X_j` as asserted in the original text, but to see
    this one must read the proof that follows in detail. This implication does not seem formal at this stage. Let us
    indeed denote by an index `J` the conjunctions of a property a), b), or c) for the `X_j`. It is proved in the proof
    below that c_J) ⇒ a_J) (this is the chain of implications c′) ⇒ d) ⇒ a′)). Now one has tautologically a) ⇒ c), and
    c) ⇔ c_J), whence a) ⇒ a_J).

[^N.D.E-VIII-6]: *N.D.E.* In all that follows, closures of points are equipped with the reduced structure.

## Translation ledger — Exposé VIII

Terms confirmed or first activated in this Exposé (consult `glossary.md` for the volume-wide list):

| French | English | Note |
| ------ | ------- | ---- |
| suite spectrale de bidualité | biduality spectral sequence | Title-level, §1. |
| théorème de finitude | finiteness theorem | Title of §2 and of Exposé. |
| résolution injective (d'un complexe) | injective resolution (of a complex) | Definition VIII.1.3. |
| complexe limité à gauche | left-bounded complex | Used in Proposition VIII.1.4. |
| double complexe / bicomplexe | double complex / bicomplex | Source uses both interchangeably; preserved. |
| aboutissement | abutment | Standard for spectral sequences. |
| terme initial | initial term | Used for `E₂` page. |
| localement immergeable dans un préschéma régulier | locally embeddable in a regular prescheme | Standing hypothesis of Theorem VIII.2.1. |
| `c(x) = codim({x}̄ ∩ Y, {x}̄)` | `c(x)` as written | Preserved verbatim from (2.1); closures are reduced (cf. N.D.E.). |
| profondeur (`prof F_x`) | depth (`prof F_x`) | Per glossary; the source uses `prof`. |
| « x suit y » | "`x` follows `y`" | Translator keeps quotation marks since the source flags it; Lemma VIII.2.5. |
| sous-faisceau quasi-cohérent | quasi-coherent subsheaf | Standard. |
| de Cohen-Macaulay (sur U !) | Cohen-Macaulay (on `U`!) | Exclamation preserved; the parenthetical insists `F` is Cohen-Macaulay on the open `U`, not on a global ambient. |
| condition (a), (b), (c), (d) | condition (a), (b), (c), (d) | Lowercase Latin letters in this Exposé (not Roman); (i)–(iv) in Corollary 2.3 stay Roman, per the source. |

Note on the `ΓZ`/`ℋ^•_Y` typographic convention: in this Exposé, sheafified local cohomology is rendered `ℋ^i_Y(F)`
(script-H) and global sections with support remain `H^i_Y(X, F)`. The underlined section functor of the source is, when
it appears, written `Γ_Y` in line with the volume-wide convention recorded in the introduction.
