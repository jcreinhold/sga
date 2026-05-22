# Index of notation

<!-- label: I.index-notations -->

A reference index of notation used throughout SGA 1. Locators are given as `<Exposé Roman>.<section>(.<sub>)` or
$<Expos\acute{e} Roman> (p. <page>)$ when known; the source's OCR-extracted index does not carry page locators, so the
locator column reconstructs them from first use in the relevant Exposé. Where the OCR mangled an identifier (most
commonly by dropping the $\pi$ prefix in $\pi_{1}(...)$ or the script-O / hat over a category), the original symbol is
restored and the restoration noted. Unresolved cases are marked with a translator note rather than silently fixed.

## Sheaves of differentials and infinitesimal neighborhoods (Exposés II–III)

| Notation                                                                                                                                                                                  | Where introduced |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| $\Delta_{X/Y}$, or simply $\Delta$                                                                                                                                                        | II.1             |
| $\Omega^{1}_{X/Y}$ (sheaf of relative differentials)                                                                                                                                      | II.1             |
| $\mathcal{P}^{n}_{X/Y}$ (sheaf of principal parts of order $n$) <!-- TRANSLATOR NOTE: source has the script-O artefact `𝓞P_X/Y^n`; canonical EGA IV notation `𝒫^n_{X/Y}` is restored. --> | II.1             |
| $\Delta^{n}_{X/Y}$ (n-th infinitesimal neighborhood of the diagonal)                                                                                                                      | II.1             |
| $\mathcal{m}\Delta_{X/Y}$ (ideal sheaf of the diagonal) <!-- TRANSLATOR NOTE: source `𝔪d_X/Y`; the `d` is a misrendered Δ. -->                                                            | II.1             |
| $d^{n}_{X/S}$ (n-th differential / iterated differential)                                                                                                                                 | II               |
| $\mathcal{m}g_{X/S}$ <!-- TRANSLATOR NOTE: source `𝔪g_X/S`; symbol not fully resolved — `g` likely denotes a generic ideal sheaf or a graded component. -->                               | II               |

## Categories, morphisms, and 2-categorical infrastructure (Exposé VI)

| Notation                                                                                                                                                                                                                   | Where introduced |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `C(...)` (a category) <!-- TRANSLATOR NOTE: source `𝓞C( )`; the leading script-O is an OCR artefact attached to the category symbol throughout. -->                                                                        | VI               |
| `Pro-C(...)` (pro-objects of $C$)                                                                                                                                                                                          | VI               |
| $\Gamma$ (sections / global-section functor; context-dependent)                                                                                                                                                            | VI               |
| `(Ens)` (category of sets)                                                                                                                                                                                                 | VI               |
| `Cat` (category of categories)                                                                                                                                                                                             | VI               |
| $Ob(C)$ (objects of $C$)                                                                                                                                                                                                   | VI               |
| $Fl(C)$ (arrows / "fleches" of $C$)                                                                                                                                                                                        | VI               |
| $\operatorname{Hom}(C, C')$ (functors $C \to C'$)                                                                                                                                                                          | VI               |
| $C^{\circ}$ (opposite category)                                                                                                                                                                                            | VI               |
| $Cat_{/E}$ (categories over $E$ / fibered over $E$)                                                                                                                                                                        | VI               |
| $\operatorname{Hom}_{E/-}(F, G)$ (cartesian functors over $E$)                                                                                                                                                             | VI               |
| $v\ast u$ (vertical composition of 2-cells / Godement product) <!-- TRANSLATOR NOTE: source `v*u`; interpreted as horizontal/vertical composition in the 2-category of fibered categories. -->                             | VI               |
| $F \times_{E} G$ (fibre product of fibered categories) <!-- TRANSLATOR NOTE: source `𝓞F×_𝓞E𝓞G`. -->                                                                                                                        | VI               |
| $f^{\ast}: Cat_{/E} \to Cat_{/E'}$ (base change of fibered categories) <!-- TRANSLATOR NOTE: source `^*: Cat_/𝓞E→ Cat_/𝓞E'`. -->                                                                                           | VI               |
| $\Gamma(G/E)$, `Γ̲(G/E)` (sections / sheaf of sections of a fibered category) <!-- TRANSLATOR NOTE: source `Γ (𝓞G/𝓞E) et Γ (𝓞G/𝓞E)`; the two are distinguished by an underline in the original which the OCR collapses. --> | VI               |
| `F_S` (fibre of a fibered category over $S$)                                                                                                                                                                               | VI               |
| $f^{\ast}_{F}(...)$ or $f^{\ast}(...)$ (inverse image along $f$)                                                                                                                                                           | VI               |
| $\Gamma_{f}(...)$                                                                                                                                                                                                          | VI               |
| $\operatorname{Hom}_{\bullet}(F, G)$ <!-- TRANSLATOR NOTE: source `Hom_ (𝓞F,𝓞G)`; subscript glyph not recovered from OCR. -->                                                                                              | VI               |
| $\hat{C}at_{/E}$ (a hatted variant — pseudo-functorial 2-category) <!-- TRANSLATOR NOTE: source `Cat^_/𝓞E`; the hat is restored on `Cat`. -->                                                                              | VI               |
| $F/E$ (fibered category $F$ over $E$)                                                                                                                                                                                      | VI               |
| $f^{F}_{\ast}$ or $~f_{\ast}$ (direct image; "tilde" variant)                                                                                                                                                              | VI               |

## Fundamental group (Exposé V) and étale-topology refinements (Exposé XIII)

| Notation                                                                                                                                                                                           | Where introduced |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| $\pi_{1}(S, a)$ (fundamental group at the geometric point $a$) <!-- TRANSLATOR NOTE: source `_1(S,a)`; the OCR systematically drops the `π` prefix on `π_1`. Restored here and below. -->          | V                |
| $\pi_{1}(S; a, a')$ (set of paths from $a$ to $a'$)                                                                                                                                                | V                |
| $\pi_{1}(f; a')$ (induced morphism on fundamental groups)                                                                                                                                          | V                |
| $C(S)$ (category of finite étale covers of $S$) <!-- TRANSLATOR NOTE: source `𝓞C(S)`; the script-O is artefactual. -->                                                                             | V                |
| `Sch` (category of schemes)                                                                                                                                                                        | V                |
| $\mu_{n, S}$ (group scheme of $n$-th roots of unity over $S$)                                                                                                                                      | XI               |
| $X^{an}$, $f^{an}$ (analytification)                                                                                                                                                               | XII              |
| `SF` or $S(F)$ (sheaf associated to a presheaf $F$)                                                                                                                                                | XII              |
| $H^{1}_{t}(U, F)$ (Čech $H^{1}$ for the topology $t$)                                                                                                                                              | XII              |
| $R^{1}_{t} g_{\ast} F$ (higher direct image for the topology $t$)                                                                                                                                  | XII              |
| $C_{t}((U, X)/S)$ or $C_{t}$ (category for the topology $t$)                                                                                                                                       | XII              |
| $\pi^{t}_{1}((U, X)/S, a)$, $\pi^{t}_{1}(U, a)$, $\pi^{t}_{1}(U)$ (fundamental group for $t$) <!-- TRANSLATOR NOTE: source `_1^t(...)`; `π` prefix restored. -->                                   | XIII             |
| $(g^{t}_{\ast} \Phi)_{T'}$                                                                                                                                                                         | XIII             |
| $H^{0}(V, C_{V})^{\Pi}$                                                                                                                                                                            | XIII             |
| $\pi^{\mathbf{L}}_{1}(U, a)$ (fundamental group with prime-to-$\mathbf{L}$ coefficients) <!-- TRANSLATOR NOTE: `𝐋` denotes a set of prime numbers; source `_1^𝐋 (U,a)`. -->                        | XIII             |
| $\pi_{1}'(X, a)$ (a derived / first variant of $\pi_{1}$) <!-- TRANSLATOR NOTE: source `_1'(X,a)`. -->                                                                                             | XIII             |
| $\pi^{\mathbf{L}}_{1}(X/S, g, \bar{s})$ or $\pi^{\mathbf{L}}_{1}(X/S, g)$ (fundamental group of a relative scheme) <!-- TRANSLATOR NOTE: source `_1^𝐋 (X/S,g,bar s)`; "bar s" rendered as `s̄`. --> | XIII             |
| $\pi^{\mathbf{L}}_{1}(X_{\bar{s}}, a)_{K}$ (fundamental group of a geometric fibre, base extension to $K$) <!-- TRANSLATOR NOTE: source `_1^𝐋 (X_bar s,a)_K`. -->                                  | XIII             |
| $\mathbf{Z}_{\ell}[1]$ (a Tate-twist–like degree shift)                                                                                                                                            | XIII             |
