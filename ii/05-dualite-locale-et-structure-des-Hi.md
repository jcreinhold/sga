# Exposé V. Local duality and the structure of the H^i(M)

<!-- label: V -->

<!-- original page 47 -->

## 1. Complexes of homomorphisms

<!-- label: V.1 -->

**1.1.** Let $F\bullet$ and $G\bullet$ be two graded modules; then one writes

$$
\operatorname{Hom}\bullet(F\bullet, G\bullet)
$$

<!-- label: eq:V.1.1 -->

for the graded module of homomorphisms of graded modules from $F\bullet$ into $G\bullet$. Thus one has

```text
Homˢ(F•, G•) = ∏ₖ Hom(Fₖ, Gₖ₊ₛ).
```

<!-- label: eq:V.1.2 -->

Let $F\bullet$ (resp. $G\bullet$) be a complex, and let $d_{1}$ (resp. $d_{2}$) be its differential; then for
$h \in \operatorname{Hom}^{s}(F\bullet, G\bullet)$ one sets[^V-1-1]

```text
d(h) = h ∘ d₁ + (−1)^{s+1} d₂ ∘ h.
```

<!-- label: eq:V.1.3 -->

One verifies trivially that $d \circ d = 0$, hence that $\operatorname{Hom}\bullet(F\bullet, G\bullet)$ equipped with
$d$ is a complex. The cohomology group of this complex is written

$$
H\bullet(F\bullet, G\bullet).
$$

<!-- label: eq:V.1.4 -->

If $G\bullet$ is injective in each degree, then

$$
F\bullet \mapsto H\bullet(F\bullet, G\bullet)
$$

is an exact ∂-functor. Likewise, for arbitrary $F\bullet$,

$$
G\bullet \mapsto H\bullet(F\bullet, G\bullet)
$$

is an exact δ-functor on the category of complexes $G\bullet$ that are injective in each degree.

<!-- original page 48 -->

**Remark 1.2.**

<!-- label: V.1.2 -->

The cycles of $\operatorname{Hom}\bullet(F\bullet, G\bullet)$ are the homomorphisms from $F\bullet$ into $G\bullet$ that
commute or anticommute with the differentials, according to degree. The boundaries of
$\operatorname{Hom}\bullet(F\bullet, G\bullet)$ are the homomorphisms from $F\bullet$ into $G\bullet$ that are homotopic
to zero.

Let $A$ be a ring, let $M$ (resp. $N$) be an $A$-module, and let $R(M)$ (resp. $R(N)$) be an injective resolution of $M$
(resp. $N$). Then there exists a canonical isomorphism[^V-1-2]

```text
Hˢ(R(M), R(N)) ≅ Extˢ(M, N).
```

<!-- label: eq:V.1.3-iso -->

Indeed, let $i: M \to R(M)$ be the canonical augmentation, and let $h \in \operatorname{Hom}^{s}(R(M), R(N))$; one
writes $t_{s}$ for the map

$$
h \mapsto h^{0} \circ i
$$

from $\operatorname{Hom}^{s}(R(M), R(N))$ into $\operatorname{Hom}(M, R(N)^{s})$. The family $(t_{s})_{s\geqslant 0}$
defines a homomorphism of (ordinary) complexes[^V-1-3]

```text
t: Hom•(R(M), R(N)) → Hom•(M, R(N)),
```

i.e. one has $(dh)^{0} \circ i = d_{2} \circ h^{0} \circ i$.

One verifies easily that, upon passing to cohomology, $t$ gives an isomorphism. In particular, it follows that

$$
H\bullet(R(M), R(N))
$$

does not "depend" on the chosen injective resolution $R(M)$ (resp. $R(N)$) of $M$ (resp. $N$).

To every exact sequence of $A$-modules

$$
0 \to M' \to M \to M'' \to 0
$$

<!-- label: eq:V.1.5 -->

one associates an exact sequence of injective resolutions

$$
0 \to R(M') \to R(M) \to R(M'') \to 0.
$$

<!-- label: eq:V.1.6 -->

One verifies that the isomorphism (1.3) commutes with the homomorphisms

```text
Hˢ(R(M′), R(N)) → Hˢ⁺¹(R(M″), R(N)),
```

<!-- label: eq:V.1.8 -->

```text
Extˢ(R(M′), R(N)) → Extˢ⁺¹(R(M″), R(N)),
```

<!-- label: eq:V.1.9 -->

deduced from (6) and (5).

<!-- original page 49 -->

Let $P$ be a third $A$-module, and let $R(P)$ be an injective resolution of $P$; then composition of graded morphisms
gives a pairing

```text
Homⁱ(R(N), R(M)) × Homʲ(R(M), R(P)) → Homⁱ⁺ʲ(R(N), R(P)),
```

<!-- label: eq:V.1.10 -->

which defines a pairing

```text
Hⁱ(R(N), R(M)) × Hʲ(R(M), R(P)) → Hⁱ⁺ʲ(R(N), R(P)),
```

<!-- label: eq:V.1.11 -->

hence a homomorphism of functors in $M$:

```text
Hⁱ(R(N), R(M)) → Hom(Hʲ(R(M), R(P)), Hⁱ⁺ʲ(R(N), R(P))).
```

<!-- label: eq:V.1.4-hom -->

We shall see that (1.4) is a homomorphism of δ-functors in $M$. The exact sequences (5) and (6) give a commutative
diagram:

```text
Homⁱ(R(N), R(M′))   ──→   Hom(Homʲ(R(M′), R(P)), Homⁱ⁺ʲ(R(N), R(P)))
       │                                       ↑
       │                                  Hom(q, id)
       ↓                                       │
Homⁱ(R(N), R(M))    ──→   Hom(Homʲ(R(M), R(P)), Homⁱ⁺ʲ(R(N), R(P)))
       │
       │ p
       ↓                                       │
Homⁱ(R(N), R(M″))   ──→   Hom(Homʲ(R(M″), R(P)), Homⁱ⁺ʲ(R(N), R(P))).
```

Let $h \in \operatorname{Hom}^{i}(R(N), R(M''))$ (resp. $g \in \operatorname{Hom}^{j}(R(M'), R(P))$) be a cycle, and let
$h' \in \operatorname{Hom}^{i}(R(N), R(M))$ (resp. $g' \in \operatorname{Hom}^{j}(R(M), R(P))$) be such that $p(h') = h$
(resp. $q(g') = g$); then to say that (1.4) is a homomorphism of δ-functors in $M$ is to say that

```text
g ∘ dh′ − dg′ ∘ h
```

<!-- label: eq:V.1.12 -->

is a coboundary in $\operatorname{Hom}\bullet(R(N), R(P))$.

Now one has

```text
dh′ = h′ ∘ d₁ + (−1)^{i+1} d₂ ∘ h′,
dg′ = g′ ∘ d₂ + (−1)^{j+1} d₃ ∘ g′,
```

with the obvious notations. Hence (12) is written

```text
g ∘ h′ ∘ d₁ + (−1)^{i+1} g ∘ d₂ ∘ h′ − g′ ∘ d₂ ∘ h − (−1)^{j+1} d₃ ∘ g′ ∘ h.
```

<!-- original page 50 -->

On the other hand, since $h$ and $g$ are cycles, one has

```text
g ∘ d₂ = (−1)ʲ d₃ ∘ g,
d₂ ∘ h = (−1)ⁱ h ∘ d₁,
```

hence, finally, (12) is written

```text
d(g ∘ h′ + (−1)^{i+1} g′ ∘ h),
```

which completes the proof.

Thus (1.3) and (1.4) give a homomorphism of δ-functors in $M$:

```text
Extⁱ(N, M) → Hom(Extʲ(M, P), Extⁱ⁺ʲ(N, P)).
```

<!-- label: eq:V.1.5-final -->

## 2. The local duality theorem for a regular local ring

<!-- label: V.2 -->

Let $A$ be a regular local ring of dimension $r$, let $\mathfrak{m}$ be the maximal ideal of $A$, and let $M$ be a
finitely generated $A$-module. One sets $H^{i}(M) = H^{i}_{\mathfrak{m}}(M)$ (hence
$H^{i}(M) = \lim\to Ext^{i}(A/\mathfrak{m}^{k}, M)$). One has seen (IV 5.4) that $I = H^{r}(A)$ is a dualizing module
for $A$; denote by $D$ the associated dualizing functor. In (1.5) setting $N = A/\mathfrak{m}^{k}$, $P = A$, one obtains
a homomorphism of δ-functors in $M$

```text
φₖ: Extⁱ(A/𝔪ᵏ, M) → Hom(Extʳ⁻ⁱ(M, A), Extʳ(A/𝔪ᵏ, A)).
```

<!-- label: eq:V.2.13 -->

Passing to the direct limit over $k$, one finds a homomorphism of δ-functors

```text
φ: Hⁱ(M) → D(Extʳ⁻ⁱ(M, A)).
```

<!-- label: eq:V.2.14 -->

**Theorem 2.1** (Local duality theorem)**.**

<!-- label: V.2.1 -->

The functorial homomorphism $\phi$ above is an isomorphism.

*Proof.* If $i > r$, the right-hand side of (14) is trivially zero, and the left-hand side is zero because
$H^{i}(M) = \lim\to_{k} Ext^{i}(A/\mathfrak{m}^{k}, M)$, and this holds for each $Ext^{i}(A/\mathfrak{m}^{k}, M)$
(syzygy theorem).

If $i = r$, by what precedes, the two functors in $M$, $H^{r}(M)$ and $D(\operatorname{Hom}(M, A))$, are right exact;
since $A$ is noetherian and $M$ is finitely generated, it suffices to verify the isomorphism for $M = A$, which is
immediate.

<!-- original page 51 -->

To show that $\phi$ is a functorial isomorphism, it now suffices, proceeding by descending induction on $i$, to remark
that every finitely generated module admits a finite presentation, and that for $i < r$ the two sides of (14) are zero
when $M$ is finitely generated free. This is evident for the right-hand side, and since $H^{i}$ commutes with finite
sums it suffices, as for the left-hand side, to show that $H^{i}(A) = 0$ for $i < r$. But this follows, since
$prof(A) = r$, from (III 3.4).

## 3. Application to the structure of the H^i(M)

<!-- label: V.3 -->

**Theorem 3.1.**

<!-- label: V.3.1 -->

Let $A$ be a noetherian local ring, $D$ a dualizing functor for $A$, and $M$ a finitely generated $A$-module with
$M \neq 0$, of dimension $n$. Then one has:

(i) $H^{i}(M) = 0$ if $i < 0$ or if $i > n$.

(ii) `D(Hⁱ(M))^` is a finitely generated module over `Â`, of dimension $\leqslant i$.

(iii) $H^{n}(M) \neq 0$, and if $A$ is complete, $D(H^{n}(M))$ is of dimension $n$ and

```text
Ass(D(Hⁿ(M))) = {𝔭 ∈ Ass(M) | dim A/𝔭 = n}.
```

*Proof.* Let $I$ be the dualizing module associated to $D$. One knows that `Î` is a dualizing module for `Â`. On the
other hand, one has

```text
Hⁱ(M)^ = Hⁱ(M̂),
D(Hⁱ(M))^ = Hom(Hⁱ(M̂), Î), and
dim M̂ = dim M;
```

hence one may suppose $A$ complete. Now, by a theorem of Cohen, every complete local ring is a quotient of a regular
local ring. To reduce to that case, one needs the following lemma:

<!-- original page 52 -->

**Lemma 3.2.**

<!-- label: V.3.2 -->

Let $X$ (resp. $Y$) be a ringed space, let $X'$ (resp. $Y'$) be a closed subspace of $X$ (resp. $Y$), and let
$f: X \to Y$ be a morphism of ringed spaces such that $f^{-1}(Y') = X'$. Let $F$ be an $\mathcal{O}_{X}$-Module, and
denote by $A$ (resp. $B$) the ring $\Gamma(\mathcal{O}_{X})$ (resp. $\Gamma(\mathcal{O}_{Y})$), and by $f: B \to A$ the
ring homomorphism corresponding to $f$. There exists a spectral sequence of $B$-modules, with initial term

$$
E^{p,q}_{2} = H^{p}_{Y'}(Y, R^{g}f_{*}(F)),
$$

<!-- label: eq:V.3.15 -->

abutting to the $B$-module $H\bullet_{X'}(X, F)_{f}$.

*Proof.* Let $\mathcal{O}_{Y,Y'}$ be the sheaf $\mathcal{O}_{Y}|Y'$ extended by `0` outside $Y'$ (see Exp. I). One has
an isomorphism of $B$-modules:

```text
Hom(𝒪_{Y,Y′}, f_*(F)) ≅ Hom(f*(𝒪_{Y,Y′}), F)_[f].
```

<!-- label: eq:V.3.16 -->

Now one has

$$
f*(\mathcal{O}_{Y,Y'}) = \mathcal{O}_{X,X'},
$$

<!-- label: eq:V.3.17 -->

and moreover if $G$ is an injective $\mathcal{O}_{X}$-Module, then $f_{*}(G)$ is an injective $\mathcal{O}_{Y}$-Module,
at least if $f$ is flat — a case to which one easily reduces by replacing $\mathcal{O}_{X}$, etc., by the constant
sheaves of rings $\mathbb{Z}$. Hence the spectral sequence of the composite functor

$$
F \mapsto \operatorname{Hom}(\mathcal{O}_{Y,Y'}, f_{*}(F)),
$$

with initial term

```text
E₂^{p,q} = Extᵖ(Y; 𝒪_{Y,Y′}, Rᵍf_*(F)),
```

abuts, taking into account (16) and (17), to

$$
Ext\bullet(X; \mathcal{O}_{X,X'}, F)_{f}.
$$

The lemma then follows from (I 13 bis). QED

<!-- original page 53 -->

Let now $f: B \to A$ be a surjective homomorphism of local rings. Let

$$
f: \operatorname{Spec}(A) \to \operatorname{Spec}(B)
$$

be the corresponding morphism of affine schemes. Set $X = \operatorname{Spec}(A)$ (resp. $X' = {\mathfrak{m}_{A}}$),
$Y = \operatorname{Spec}(B)$ (resp. $Y' = {\mathfrak{m}_{B}}$), and let $M$ be an $A$-module and $\tilde{M}$ the
corresponding $\mathcal{O}_{X}$-Module. Since $R^{g}f_{*}(\tilde{M}) = 0$ for $q > 0$, the spectral sequence (15)
degenerates, and by (3.2) one obtains an isomorphism of $B$-modules:

```text
Hⁿ_{{𝔪_B}}(Y, f_*(M̃)) ≅ Hⁿ_{{𝔪_A}}(X, M̃)_[f],
```

<!-- label: eq:V.3.18 -->

hence an isomorphism of $B$-modules:

$$
H^{n}_{\mathfrak{m}_{B}}(M_{f}) \cong H^{n}_{\mathfrak{m}_{A}}(M)_{f}.
$$

<!-- label: eq:V.3.19 -->

On the other hand, if `D_A` (resp. `D_B`) is the dualizing functor for $A$ (resp. $B$), one has

$$
D_{A}(M)_{f} \cong D_{B}(M_{f}).
$$

<!-- label: eq:V.3.20 -->

Finally, since one has a ring isomorphism

```text
B/Ann M_[f] ≅ A/Ann M,
```

<!-- label: eq:V.3.21 -->

one sees that the change of base rings under consideration changes nothing. So suppose $A$ is regular of dimension $r$.

By (2.1) one has

$$
D(H^{i}(M)) = Ext^{r-i}(M, A).
$$

<!-- label: eq:V.3.22 -->

We shall prove the equivalence of the following properties:

(a) $\dim Ext^{j}(M, A) \leqslant r - j$;

(b) for every $\mathfrak{p} \in X = \operatorname{Spec}(A)$ such that $\dim A_{\mathfrak{p}} < j$, one has
$Ext^{j}(M, A)_{\mathfrak{p}} = 0$;

(c) $codim(Supp(Ext^{j}(M, A)), X) \geqslant j$.

To prove (a) ⇒ (b), let $\mathfrak{p} \in X$ with $\dim A_{\mathfrak{p}} < j$; then $\dim A/\mathfrak{p} > r - j$, hence
by (a) $Ann(Ext^{j}(M, A)) \nsubset \mathfrak{p}$, which entails $Ext^{j}(M, A)_{\mathfrak{p}} = 0$. Let
$\mathfrak{p} \in Supp(Ext^{j}(M, A))$; then $Ext^{j}(M, A)_{\mathfrak{p}} \neq 0$, so by (b)
$\dim A_{\mathfrak{p}} \geqslant j$. Hence `codim(Supp(Extʲ(M, A)), X) = inf{dim A_𝔭 | 𝔭 ∈ Supp(Extʲ(M, A))} ⩾ j`, that
is, (b) ⇒ (c). Finally (c) implies (a) trivially.

Let us now prove the theorem.

(i) Let $x = (x_{1}, \cdots, x_{r})$ be a system of parameters for $A$ such that $x_{i} \in Ann M$ for
$i = 1, \cdots, r - n$. Let $K\bullet((x^{k}), M)$ be the Koszul complex. One sees easily that the map
$K^{i}((x^{k}), M) \to K^{i}((x^{k}'), M)$ for $k < k'$ is zero, if $i > n$. It follows that
$H^{i}(M) = \lim\to H^{i}((x^{k}), M) = 0$ if $i > n$. On the other hand, it is trivial that $H^{i}(M) = 0$ if $i < 0$,
so (i) is proved.

(ii) Since $A$ is regular, $\dim A_{\mathfrak{p}} < j$ entails that the global homological dimension of
$A_{\mathfrak{p}}$ is strictly less than $j$, and hence
$Ext^{j}(M, A)_{\mathfrak{p}} = Ext^{j}_{A_{\mathfrak{p}}}(M_{\mathfrak{p}}, A_{\mathfrak{p}}) = 0$; so one has proved
(b) and consequently (a). (ii) then follows from (22) and from (a).

(iii) There exists a $\mathfrak{p} \in Supp(M)$ such that $\dim A_{\mathfrak{p}} = r - n$ and such that
$Supp(M_{\mathfrak{p}}) = {\mathfrak{m}_{A_{\mathfrak{p}}}}$. Since $A_{\mathfrak{p}}$ is regular if $A$ is, one finds
$prof A_{\mathfrak{p}} = r - n$, hence

```text
Extʳ⁻ⁿ_A(M, A)_𝔭 = Extʳ⁻ⁿ_{A_𝔭}(M_𝔭, A_𝔭) ≠ 0.
```

<!-- label: eq:V.3.23 -->

<!-- original page 54 -->

This implies, taking (22) into account, that on the one hand

$$
H^{n}(M) \neq 0,
$$

and on the other hand

$$
\dim D(H^{n}(M)) \geqslant n,
$$

hence by (ii)

$$
\dim D(H^{n}(M)) = n.
$$

Let now $Y = Supp(M)$. By (i) one knows that $D(H^{n}(M')) = Ext^{r-n}(M', A)$ is a functor in $M'$, left exact, on the
category $(\mathcal{C}_{Y})^{\circ}$. Hence there exists an $A$-module $H$ and an isomorphism of functors in $M'$:

```text
Extʳ⁻ⁿ(M′, A) = Hom(M′, H).
```

Let `Yᵢ`, $i = 1, \cdots, k$, be the irreducible components of $Y$ of maximum dimension. We shall see that the assertion
$Ext^{r-n}(M', A) \neq 0$ is equivalent to the assertion: there exists an $i$ such that $Supp M' \supset Y_{i}$. Indeed,
if $Supp M' \supset Y_{i}$, then $\dim(M') = n$, hence $Ext^{r-n}(M', A) \neq 0$.

If $Supp M' \nsupset Y_{i}$ for every $i = 1, \cdots, k$, then $\dim M' < n$ and

$$
D(H^{n}(M')) = Ext^{r-n}(M', A) = 0.
$$

Since `Ass(Extʳ⁻ⁿ(M, A)) = Supp M ∩ Ass(H)`, one sees that the last assertion of (iii) follows from the following lemma:

**Lemma 3.3.**

<!-- label: V.3.3 -->

Let $X = \operatorname{Spec}(A)$, let $Y$ be a closed subset of $X$, let $T: (\mathcal{C}_{Y})^{\circ} \to Ab$ be a left
exact functor, and let `Yᵢ`, $i = 1, \cdots, k$, be a family of irreducible components of $Y$ such that the assertion:
$T(M) = 0$ is equivalent to the assertion: $\forall i, Supp M \nsupset Y_{i}$. Then $T$ is representable by a module $H$
such that $Ass(H) = \bigcup^{k}_{i=1} {y_{i}}$, where `yᵢ` is the generic point of `Yᵢ`, $i = 1, \cdots, k$.

*Proof.* Let $y \in Y$; one constructs an $A$-module $M(y)$ such that $Supp(M(y)) = {y}$. Suppose that $y \neq y_{i}$
for every $i = 1, \cdots, k$; then $Y_{i} \nsubset Supp(M(y))$ for every $i = 1, \cdots, k$, so $T(M(y)) = 0$. It
follows that

```text
Ass(T(M(y))) = Supp(M(y)) ∩ Ass(H) = ∅,
```

hence $y \notin Ass(H)$. If $y = y_{i}$, then $Y_{i} \subset Supp(M(y))$, so $T(M(y)) \neq 0$, whence

```text
Ass(T(M(y))) = Supp(M(y)) ∩ Ass(H) ≠ ∅.
```

By the first part of the proof, this implies $y \in Ass(H)$, whence the lemma. QED

**Example 3.4.**

<!-- label: V.3.4 -->

Let $A$ be a noetherian ring, let $X = \operatorname{Spec}(A)$, and let $Y$ be a closed subset of $X$ such that $X - Y$
is affine; then for every irreducible component $Y_{\alpha}$ of $Y$ one has $codim(Y_{\alpha}, X) \leqslant 1$.

Indeed, consider $X$ as a prescheme over $X$. Let $y_{\alpha} \in Y_{\alpha}$ be a generic point, and consider the
morphism $\operatorname{Spec}(\mathcal{O}_{X,y_{\alpha}}) \to X$. The affine scheme obtained by base extension of $X$ to
$\operatorname{Spec}(\mathcal{O}_{X,y_{\alpha}})$ is canonically isomorphic to
$\operatorname{Spec}(\mathcal{O}_{X,y_{\alpha}})$.

By (EGA I 3.2.7) one sees that if $y_{0}$ is the unique closed point of
$Y_{0} = \operatorname{Spec}(\mathcal{O}_{X,y_{\alpha}})$, then $Y_{0} - y_{0}$ is affine. By (EGA III 1.3.1) one finds

```text
Hⁱ(Y₀ − y₀, 𝒪_{Y₀}) = 0   if i > 0,
```

<!-- original page 55 -->

hence by (I 2.9)

```text
Hⁱ⁻¹(𝒪_{X,y_α}) = Hⁱ_{{y₀}}(Y₀, 𝒪_{Y₀}) = 0   if i ⩾ 2.
```

Taking 3.1 (iii) into account, it follows that

$$
\dim \mathcal{O}_{X,y_{\alpha}} \leqslant 1,
$$

hence `codim(Y_α, X) = inf_{y ∈ Y_α} dim 𝒪_{X,y} ⩽ 1`. QED

Let $A$ be a noetherian local ring, $\mathfrak{m}$ its maximal ideal, and $M$ a finitely generated $A$-module. Suppose
that $A$ is a quotient of a regular local ring. Set $X = \operatorname{Spec}(A)$, and for every $x \in X$,
$\mathfrak{m}_{x} = \mathfrak{m}A_{x}$.

**Proposition 3.5.**

<!-- label: V.3.5 -->

The following two conditions are equivalent:

a) $H^{i}(M)$ is of finite length;

b) $\forall x \in X - {\mathfrak{m}}, H^{i-dim} {x}_{\mathfrak{m}_{x}}(M_{x}) = 0$.

*Proof.* Taking (3.2) into account, we may suppose $A$ regular. By (2.1) we have

$$
H^{i}(M) = D(Ext^{r-i}(M, A)),
$$

where $r = \dim A$. By (IV 4.7), a) is equivalent[^V-3-4] to

```text
Extʳ⁻ⁱ(M, A) is of finite length.
```

<!-- label: eq:V.3.24 -->

Now (24) is equivalent to

```text
∀ x ∈ X − {𝔪}, one has Extʳ⁻ⁱ(M, A)_x = 0.
```

<!-- label: eq:V.3.25 -->

On the other hand $A_{x}$ is regular of dimension $r - \dim {x}$, so by (2.1)

```text
Hⁱ⁻ᵈⁱᵐ {x}_{𝔪_x}(M_x) = D(Ext^{(r − dim {x}) − (i − dim {x})}_{A_x}(M_x, A_x)) = D(Extʳ⁻ⁱ_{A_x}(M_x, A_x)).
```

<!-- label: eq:V.3.26 -->

Since $M$ is finitely generated, one has

```text
Extʳ⁻ⁱ_A(M, A)_x = Extʳ⁻ⁱ_{A_x}(M_x, A_x),
```

whence the proposition.

**Corollary 3.6.**

<!-- label: V.3.6 -->

In order that $H^{i}(M)$ be of finite length for $i \leqslant n$, it is necessary and sufficient that

```text
prof(M_x) > n − dim {x}
```

for every $x \in X - {\mathfrak{m}}$.

*Proof.* Follows from (3.5) and (III 3.1).

<!--
LEDGER DELTA (Exposé V):
| French | English | Note |
| --- | --- | --- |
| Complexes d'homomorphismes | Complexes of homomorphisms | Section title; preserves the `Hom•` dot notation in body. |
| modules gradués | graded modules | Standard. |
| ∂-foncteur / δ-foncteur | ∂-functor / δ-functor | Preserve Grothendieck's distinction between `∂` and `δ`. |
| résolution injective | injective resolution | Standard. |
| augmentation canonique | canonical augmentation | Standard. |
| homomorphes à zéro | homotopic to zero | Standard. |
| accouplement | pairing | Standard category-theoretic term. |
| anneau local régulier | regular local ring | Per glossary. |
| Théorème des syzygies | syzygy theorem | Hilbert's syzygy theorem; the source uses singular "théorème", rendered as English "syzygy theorem". |
| module dualisant | dualizing module | Per glossary. |
| foncteur dualisant | dualizing functor | Per glossary. |
| limite inductive | direct limit | Per glossary; rendered "direct limit" (modern English) here. |
| espace annelé | ringed space | Per glossary. |
| `𝒪_X`-Module | `𝒪_X`-Module | Capital "Module" preserved (sheaf-of-modules) per SGA convention. |
| suite spectrale | spectral sequence | Per glossary. |
| terme initial | initial term | Per glossary. |
| aboutissement / aboutit à | abutment / abuts to | Per glossary. |
| changement d'anneaux de base | change of base rings | Standard. |
| `M`-[f] (extension of scalars) | `M_[f]` | The bracketed `[f]` denotes restriction/extension of scalars along `f`; preserved as `_[f]`. |
| Théorème de Cohen | theorem of Cohen | Cohen's structure theorem for complete local rings. |
| anneau noethérien | noetherian ring | Standard. |
| de type fini | finitely generated (for modules) | Per glossary; "of finite type" not used here since context is module-level. |
| dimension homologique globale | global homological dimension | Standard. |
| système de paramètres | system of parameters | Standard. |
| complexe de Koszul | Koszul complex | Standard. |
| composantes irréductibles | irreducible components | Standard. |
| point générique | generic point | Standard. |
| partie fermée | closed subset | Standard. |
| `(𝒞_Y)°` | `(𝒞_Y)°` | Opposite category of coherent sheaves with support in `Y`; preserved. |
| Ass | Ass | Associated primes; preserved as Ass. |
| prof | prof | Depth functor; preserved as `prof` (matches source). |
| section hyperplane | n/a | Not used in this Exposé. |
| extension du schéma de base | base extension | Standard. |
| C.Q.F.D. / Q.E.D. | QED | Preserved as English "QED" per glossary. |
| `[f]` (restriction-of-scalars subscript) | `_[f]` | The source brackets `[f]` indicate restriction of scalars; rendered as a subscript `_[f]`. |
| `^` (hat / formal completion) | `Â`, `M̂`, `Î` | Hat indicates formal completion / `m`-adic completion; rendered with Unicode combining hat. |
-->

[^V-1-1]: *N.D.E.* The original sign convention was different; but it is not compatible with the convention of Exposé
    VIII, which seems more reasonable, since in that case the cohomology in degree `0` is the set of homotopy classes of
    morphisms from $F\bullet$ into $G\bullet$. The calculations have been modified accordingly in what follows.

[^V-1-2]: *N.D.E.* The strange original numbering has been preserved.

[^V-1-3]: *N.D.E.* We still write $M$ for the complex `M[0]` consisting of $M$ placed in degree `0`.

[^V-3-4]: *N.D.E.* Indeed, the point is to show that, $E$ being a finitely generated $A$-module, if $D(E)$ is of finite
    length then $E$ is of finite length. Let $K$ (resp. $Q$) be the kernel (resp. cokernel) of the canonical morphism
    $\epsilon: E \to DD(E)$. The composition of $D(\epsilon)$ and the canonical morphism $\gamma: D(E) \to DDD(E)$ is
    the identity of $D(E)$. Since $D(E)$ is of finite length, $\gamma$ is an isomorphism, and hence so is $D(\epsilon)$.
    Since $D$ is exact, it follows that $D(K)$ and $D(Q)$ are zero. It suffices to prove that if $M$ is an $A$-module
    with zero dual, then $M$ is zero, for one will then have $E = DD(E)$ of finite length, just like $D(E)$. Indeed, let
    $M_{0}$ be a finitely generated submodule of $M$. Since $D$ is exact, $D(M_{0})$ is a quotient of $D(M)$, which is
    zero. Again by the exactness of $D$, one has $D(M_{0}/\mathfrak{m}_{A} M_{0}) = 0$, and hence, by biduality, the
    finite-length module $M_{0}/\mathfrak{m}_{A} M_{0}$ is zero. Nakayama's lemma then ensures the vanishing of $M_{0}$,
    and finally one obtains that of $M$.
