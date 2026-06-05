# Exposé VI. The functors $Ext^{\bullet}_{Z}(X; F, G)$ and $\mathcal{E}xt^{\bullet}_{Z}(F, G)$

<!-- label: VI -->

<!-- original page 72 -->

<!-- TRANSLATOR NOTE: Throughout this Exposé we write `ℰxt^i_Z(F, G)` (script `ℰ`)
for the sheafified version of `Ext` (the variant underlined in the original source)
and `Ext^i_Z(X; F, G)` for the global one. Wherever the OCR shows two parallel
forms `ExtiZ (X; F, G)` and `ExtiZ (F, G)` for the same derived functor, the second
one is the sheafified version, and is rendered `ℰxt^i_Z(F, G)`. -->

## 1. Generalities

<!-- label: VI.1 -->

### 1.1.

<!-- label: VI.1.1 -->

Let $(X, \mathcal{O}_{X})$ be a ringed space and let $Z$ be a locally closed subset of $X$. Let $F$ and $G$ be
$\mathcal{O}_{X}$-Modules; we denote by $Ext^{i}_{Z}(X; F, G)$ (resp. $\mathcal{E}xt^{i}_{Z}(F, G)$) the $i$-th derived
functor of the functor $G \mapsto \Gamma_{Z}(\operatorname{Hom}_{\mathcal{O}_{X}}(F, G))$ (resp. $G \mapsto \Gamma
Z(\mathcal{H}om_{\mathcal{O}_{X}}(F, G))$, where $\Gamma Z$ denotes the sheafified sections-with-support functor and
$\mathcal{H}om_{\mathcal{O}_{X}}$ the sheafified `Hom`).

**Lemma.**

<!-- label: VI.1.2 -->

The sheaf $\mathcal{E}xt^{i}_{Z}(F, G)$ is canonically isomorphic to the sheaf associated with the presheaf $U \mapsto
Ext^{i}_{Z \cap U}(U; F|U, G|U)$.

This follows from (*Tôhoku*, 3.7.2) together with the fact that $\Gamma(U; \Gamma Z(\mathcal{H}om_{\mathcal{O}_{X}}(F,
G)))$ is canonically isomorphic to $\Gamma_{Z \cap U}(\operatorname{Hom}_{\mathcal{O}_{X}|U}(F|U, G|U))$.

**Theorem (Excision theorem).**

<!-- label: VI.1.3 -->

Let $V$ be an open subset of $X$ containing $Z$. Then one has an isomorphism of cohomological functors

```text
Ext^•_X(X; F, G) ≃ Ext^•_V(V; F|V, G|V).
```

<!-- label: eq:VI.1.3.1 -->

Indeed, if $G^{\bullet}$ is an injective resolution of $G$, then $G^{\bullet}|V$ is an injective resolution of $G|V$.
The theorem follows immediately.

### 1.4.

<!-- label: VI.1.4 -->

Let $\mathcal{O}_{X,Z}$ be the $\mathcal{O}_{X}$-Module defined by the following conditions ([Godement], 2.9.2):
$\mathcal{O}_{X,Z}|_{X - Z} = 0$ and $\mathcal{O}_{X,Z}|_{Z} = \mathcal{O}_{X}|_{Z}$. We have seen that for every
$\mathcal{O}_{X}$-Module $H$ there is a functorial isomorphism $\Gamma_{Z}(H) \simeq
\operatorname{Hom}_{\mathcal{O}_{X}}(\mathcal{O}_{X,Z}, H)$. From this we deduce functorial isomorphisms in $F$ and $G$:

```text
Γ_Z(Hom_{𝒪_X}(F, G)) ≃ Hom_{𝒪_X}(𝒪_{X,Z}, Hom_{𝒪_X}(F, G)),
```

<!-- label: eq:VI.1.4.1 -->

```text
Γ_Z(Hom_{𝒪_X}(F, G)) ≃ Hom_{𝒪_X}(𝒪_{X,Z} ⊗_{𝒪_X} F, G),
```

<!-- label: eq:VI.1.4.2 -->

```text
Γ_Z(Hom_{𝒪_X}(F, G)) ≃ Hom_{𝒪_X}(F, Hom_{𝒪_X}(𝒪_{X,Z}, G)) = Hom_{𝒪_X}(F, Γ_Z(G)).
```

<!-- label: eq:VI.1.4.3 -->

<!-- original page 73 -->

It follows in particular from (1.4.2) that there is a $\partial$-functorial isomorphism in $F$ and $G$

```text
θ: Ext^i_{𝒪_X}(𝒪_{X,Z} ⊗_{𝒪_X} F, G) ⥲ Ext^i_Z(X; F, G).
```

<!-- original page 74 -->

<!-- TRANSLATOR NOTE: the source paginates the displayed θ-isomorphism at the
foot of page 73 and the section heading 1.5 at the top of page 74; the running
header on page 74 is the Exposé title, which we omit. -->

### 1.5.

<!-- label: VI.1.5 -->

By definition, the functor $G \mapsto \Gamma_{Z}(\operatorname{Hom}_{\mathcal{O}_{X}}(F, G))$ is the composite of the
functor $G \mapsto \operatorname{Hom}_{\mathcal{O}_{X}}(F, G)$ and the functor $\Gamma_{Z}$. Since $\Gamma_{Z}$ is left
exact (I 1.9), since $\operatorname{Hom}_{\mathcal{O}_{X}}(F, G)$ is flasque whenever $G$ is injective, and since
$\Gamma_{Z}$ is exact on flasque sheaves (I 2.12), it follows from (*Tôhoku*, 2.4.1) that there is a spectral functor
abutting to $Ext^{\bullet}_{Z}(X; F, G)$ whose initial term is $H^{p}_{Z}(X, \mathcal{E}xt^{q}_{\mathcal{O}_{X}}(F,
G))$.

On the other hand, it follows from (1.4.3) that $\Gamma_{Z}(\operatorname{Hom}_{\mathcal{O}_{X}}(F, G))$ is the
composite of $\Gamma_{Z}$ and the functor $H \mapsto \operatorname{Hom}_{\mathcal{O}_{X}}(F, H)$.

Since the functor $\Gamma_{Z}$ takes injectives to injectives (I 1.4), it follows from (*Tôhoku*, 2.4.1) that there is a
spectral functor abutting to $Ext^{\bullet}_{Z}(X; F, G)$ whose initial term is $Ext^{p}_{\mathcal{O}_{X}}(X; F,
\mathcal{H}^{q}_{Z}(G))$.

It follows finally, from (1.4.2) and the spectral sequence for `Ext`, that there is a spectral functor abutting to
$Ext^{\bullet}_{Z}(X; F, G)$ whose initial term is $H^{p}(X; \mathcal{E}xt^{q}_{Z}(F, G))$. Whence the

**Theorem.**

<!-- label: VI.1.6 -->

There exist three spectral functors abutting to $Ext^{\bullet}_{Z}(X; F, G)$ whose initial terms are respectively

$$ H^{p}_{Z}(X, \mathcal{E}xt^{q}_{\mathcal{O}_{X}}(F, G)) $$

<!-- label: eq:VI.1.6.1 -->

$$ H^{p}(X, \mathcal{E}xt^{q}_{Z}(F, G)) $$

<!-- label: eq:VI.1.6.2 -->

$$ Ext^{p}_{\mathcal{O}_{X}}(X; F, \mathcal{H}^{q}_{Z}(G)). $$

<!-- label: eq:VI.1.6.3 -->

### 1.7.

<!-- label: VI.1.7 -->

Let now $Z'$ be a closed subset of $Z$ and let $Z'' = Z - Z'$. We have an exact sequence

$$ 0 \to \mathcal{O}_{X,Z''} \to \mathcal{O}_{X,Z} \to \mathcal{O}_{X,Z'} \to 0 $$

<!-- label: eq:VI.1.7.1 -->

which generalizes the exact sequence of ([Godement], 2.9.3). This exact sequence splits locally; hence for every
$\mathcal{O}_{X}$-Module $F$ we have a further exact sequence:

```text
0 → F ⊗_{𝒪_X} 𝒪_{X,Z″} → F ⊗_{𝒪_X} 𝒪_{X,Z} → F ⊗_{𝒪_X} 𝒪_{X,Z′} → 0.
```

<!-- label: eq:VI.1.7.2 -->

Let now $G$ be an $\mathcal{O}_{X}$-Module; applying the functor $\operatorname{Hom}_{\mathcal{O}_{X}}(\bullet, G)$ to
the exact sequence (1.7.2), one deduces from (1.4.2) and the long exact sequence for `Ext` the following theorem:

**Theorem.**

<!-- label: VI.1.8 -->

Let $Z$ be a locally closed subset of $X$, let $Z'$ be a closed subset of $Z$, and let $Z'' = Z - Z'$. Then there is an
exact sequence, functorial in $F$ and $G$:

```text
0 → Hom_{Z′}(F, G) → Hom_Z(F, G) → Hom_{Z″}(F, G) → Ext^1_{Z′}(F, G) → ⋯
    ⋯ → Ext^i_Z(F, G) → Ext^i_{Z″}(F, G) → Ext^{i+1}_{Z′}(F, G) → ⋯
```

**Corollary.**

<!-- label: VI.1.9 -->

Let $Y$ be a closed subset of $X$ and let $U = X - Y$. Then there is an exact sequence, functorial in $F$ and $G$:

```text
0 → Hom_Y(F, G) → Hom_{𝒪_X}(F, G) → Hom_{𝒪_X|U}(F|U, G|U) → Ext^1_Y(F, G) → ⋯
    ⋯ → Ext^i_{𝒪_X}(F, G) → Ext^i_{𝒪_X|U}(F|U, G|U) → Ext^{i+1}_Y(F, G) → ⋯
```

This corollary is an immediate consequence of theorem (1.3) and theorem (1.8).

<!-- original page 75 -->

## 2. Applications to quasi-coherent sheaves on preschemes

<!-- label: VI.2 -->

**Proposition.**

<!-- label: VI.2.1 -->

Let $X$ be a locally noetherian prescheme. For every locally closed subset $Z$ of $X$, every coherent Module $F$, and
every quasi-coherent Module $G$ on $X$, the sheaves $\mathcal{E}xt^{i}_{Z}(F, G)$ are quasi-coherent.

One shows, as in (1.6.3), that the Modules $\mathcal{E}xt^{i}_{Z}(F, G)$ are the abutment of a spectral sequence with
initial term $\mathcal{E}xt^{p}_{\mathcal{O}_{X}}(F, \mathcal{H}^{q}_{Z}(G))$. By (II, cor. 3) the
$\mathcal{H}^{q}_{Z}(G)$ are quasi-coherent, and so are the $\mathcal{E}xt^{p}_{\mathcal{O}_{X}}(F,
\mathcal{H}^{q}_{Z}(G))$, since $F$ is coherent. The proposition follows immediately.

### 2.2.

<!-- label: VI.2.2 -->

Let now $Y$ be a closed subprescheme of $X$ and let $\mathcal{I}$ be a defining ideal of $Y$. Let $m$ and $n$ be
integers with $m \geqslant n \geqslant 0$; we denote by $i_{n,m}$ the canonical map $\mathcal{O}_{Y_{m}} =
\mathcal{O}_{X}/\mathcal{I}^{m+1} \to \mathcal{O}_{X}/\mathcal{I}^{n+1} = \mathcal{O}_{Y_{n}}$ and by $j_{n}$ the map
$\mathcal{O}_{X,Y} \to \mathcal{O}_{Y_{n}}$. The system $(\mathcal{O}_{Y_{n}}, i_{n,m})$ forms a projective system, and
the maps $j_{n}$ are compatible with the $i_{n,m}$.

Applying the functor $Ext^{i}_{\mathcal{O}_{X}}(F \otimes \bullet, G)$, one deduces a morphism

```text
φ′: lim_{→ n} Ext^i_{𝒪_X}(X; F ⊗ 𝒪_{Y_n}, G) → Ext^i_{𝒪_X}(X; F ⊗ 𝒪_{X,Y}, G);
```

this is a morphism of cohomological functors in $G$. The morphism

```text
φ: lim_{→ n} Ext^i_{𝒪_X}(X; F ⊗ 𝒪_{Y_n}, G) → Ext^i_Y(X; F, G)
```

obtained as the composite of $\phi'$ with $\theta$ (cf. 1.4) is therefore likewise a morphism of cohomological functors
in $G$.

One defines in the same way

```text
φ̲: lim_{→ n} ℰxt^i_{𝒪_X}(F ⊗ 𝒪_{Y_n}, G) → ℰxt^i_Y(F, G).
```

<!-- TRANSLATOR NOTE: in the source both arrows are called `ϕ`; here `φ̲`
(underlined `φ`) denotes the sheafified variant, to match the global/sheafified
split used elsewhere in this Exposé. -->

**Theorem.**

<!-- label: VI.2.3 -->

<!-- original page 76 -->

Let $X$ be a locally noetherian prescheme, let $Y$ be a closed subset of $X$ defined by a coherent ideal $\mathcal{I}$,
let $F$ be a coherent Module and let $G$ be a quasi-coherent Module. Then:

a) `φ̲` is an isomorphism.

b) If $X$ is noetherian, $\phi$ is an isomorphism.

The proof of b) being almost word for word that of (II 6 b)), thanks to the spectral sequence 1.6.2, we shall not
reproduce it.

For the proof of a), one may, by (2.1), assume $X$ affine with ring $A$, $F$ (resp. $G$) defined by an $A$-module $M$
(resp. $N$), and $\mathcal{I}$ by an ideal $I$. It suffices to prove that the homomorphism

```text
lim_{→ n} Ext^i_A(M/I^n M, N) → Ext^i_Y(X, F, G)
```

<!-- label: eq:VI.2.3.1 -->

deduced from `φ̲` is an isomorphism.

Indeed, for $i = 0$, one can canonically identify both sides of (2.3.1) with the submodule of $\operatorname{Hom}_{A}(M,
N)$ consisting of those elements of $\operatorname{Hom}_{A}(M, N)$ annihilated by some power of $I$. One then sees that
the homomorphism (2.3.1) is none other than the identity map.

The functor $N \mapsto \lim_{\to n} Ext^{\bullet}_{A}(M/I^{n} M, N)$ is a universal $\partial$-functor. We shall show
that the same holds for the functor $N \mapsto Ext^{\bullet}_{Y}(M, N)$. Indeed, if $N$ is an injective module, by (9
and 11), $\mathcal{H}^{q}_{Y}(N) = 0$ for $q \neq 0$; and by (IV.2.2), $\mathcal{H}^{0}_{Y}(N)$ is injective.

<!-- TRANSLATOR NOTE: the citations "(9 and 11)" in the source most plausibly
refer to results from the present section's preceding Exposés (likely I 1.4 and
the depth/injectivity material of IV); they are kept verbatim, as in the
French. -->

It follows then that $Ext^{p}_{\mathcal{O}_{X}}(X; M, \mathcal{H}^{q}_{Y}(N)) = 0$ for $p + q \neq 0$; hence, by
(1.6.3), $Ext^{i}_{Y}(M, N) = 0$ for $i \neq 0$ and $N$ injective. This completes the proof.

## Bibliography

Same references as those listed at the end of Exp. I, cited respectively \[*T\hat{o}hoku*\] and [Godement].

<!-- ────────────────────────────────────────────────────────────────────── -->

<!-- Ledger delta — Exposé VI                                                -->

<!-- ────────────────────────────────────────────────────────────────────── -->

<!--
The following terminological choices were fixed in the present Exposé. They
extend the entries already recorded in `glossary.md`; merge into the master
glossary on the next consolidation pass.

| French                                          | English                                            | Note                                                                                  |
| ----------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------------------------------------- |
| `Ext^i_Z(X; F, G)`                              | `Ext^i_Z(X; F, G)`                                 | Global Ext with support in `Z`. Non-sheafified.                                       |
| `Ext^i_Z(F, G)` (underlined in source)          | `ℰxt^i_Z(F, G)`                                    | Sheafified Ext with support in `Z`. Script `ℰ` marks the underline in the source.     |
| `ϕ` (global) vs. `ϕ` underlined (sheafified)    | `φ` vs. `φ̲`                                       | The sheafified comparison morphism is rendered with combining low line; parallel to `ΓZ` / `Γ_Z`. |
| `Théorème d'excision`                           | excision theorem                                   | Per source. Attribution kept on the theorem statement (Theorem 1.3).                  |
| `aboutissant à`                                 | abutting to                                        | Standard spectral-sequence term.                                                      |
| `foncteur spectral`                             | spectral functor                                   | SGA usage; the modern phrasing would be "spectral sequence functor".                  |
| `terme initial`                                 | initial term                                       | `E_2`-term in modern parlance; the source says *terme initial* throughout.            |
| `idéal de définition`                           | defining ideal                                     | Of a closed subprescheme.                                                             |
| `presque mot à mot`                             | almost word for word                               | Proof-movement idiom; kept literal.                                                   |

Unresolved / flagged:

- The citation "(9 and 11)" in the proof of Theorem 2.3 is opaque in the source.
  It almost certainly refers to numbered items inside SGA 2 (Exposé I, no. 1.4
  for the injectivity-preservation of `Γ_Z`, and Exposé IV for the depth
  vanishing); the bare "(9 and 11)" reading is preserved with a translator note,
  pending a cross-reference pass against the renumbered statements.
- The morphism called `ϕ` twice in the source — once globally, once sheafified —
  has been disambiguated as `φ` / `φ̲` to mirror the `Γ_Z` / `ΓZ` convention
  pinned at first use in this Exposé.
-->
