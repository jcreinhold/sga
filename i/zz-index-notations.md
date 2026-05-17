# Index of notation

<!-- label: I.index-notations -->

A reference index of notation used throughout SGA 1. Locators are given as `<Exposé Roman>.<section>(.<sub>)` or
`<Exposé Roman> (p. <page>)` when known; the source's OCR-extracted index does not carry page locators, so the locator
column reconstructs them from first use in the relevant Exposé. Where the OCR mangled an identifier (most commonly by
dropping the `π` prefix in `π_1(...)` or the script-O / hat over a category), the original symbol is restored and the
restoration noted. Unresolved cases are marked with a translator note rather than silently fixed.

## Sheaves of differentials and infinitesimal neighborhoods (Exposés II–III)

| Notation                                                                                                                                                                      | Where introduced |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `Δ_{X/Y}`, or simply `Δ`                                                                                                                                                      | II.1             |
| `Ω^1_{X/Y}` (sheaf of relative differentials)                                                                                                                                 | II.1             |
| `𝒫^n_{X/Y}` (sheaf of principal parts of order `n`) <!-- TRANSLATOR NOTE: source has the script-O artefact `𝓞P_X/Y^n`; canonical EGA IV notation `𝒫^n_{X/Y}` is restored. --> | II.1             |
| `Δ^n_{X/Y}` (n-th infinitesimal neighborhood of the diagonal)                                                                                                                 | II.1             |
| `𝓂Δ_{X/Y}` (ideal sheaf of the diagonal) <!-- TRANSLATOR NOTE: source `𝔪d_X/Y`; the `d` is a misrendered Δ. -->                                                               | II.1             |
| `d^n_{X/S}` (n-th differential / iterated differential)                                                                                                                       | II               |
| `𝓂g_{X/S}` <!-- TRANSLATOR NOTE: source `𝔪g_X/S`; symbol not fully resolved — `g` likely denotes a generic ideal sheaf or a graded component. -->                             | II               |

## Categories, morphisms, and 2-categorical infrastructure (Exposé VI)

| Notation                                                                                                                                                                                                              | Where introduced |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `C(...)` (a category) <!-- TRANSLATOR NOTE: source `𝓞C( )`; the leading script-O is an OCR artefact attached to the category symbol throughout. -->                                                                   | VI               |
| `Pro-C(...)` (pro-objects of `C`)                                                                                                                                                                                     | VI               |
| `Γ` (sections / global-section functor; context-dependent)                                                                                                                                                            | VI               |
| `(Ens)` (category of sets)                                                                                                                                                                                            | VI               |
| `Cat` (category of categories)                                                                                                                                                                                        | VI               |
| `Ob(C)` (objects of `C`)                                                                                                                                                                                              | VI               |
| `Fl(C)` (arrows / "fleches" of `C`)                                                                                                                                                                                   | VI               |
| `Hom(C, C′)` (functors `C → C′`)                                                                                                                                                                                      | VI               |
| `C^∘` (opposite category)                                                                                                                                                                                             | VI               |
| `Cat_{/E}` (categories over `E` / fibered over `E`)                                                                                                                                                                   | VI               |
| `Hom_{E/-}(F, G)` (cartesian functors over `E`)                                                                                                                                                                       | VI               |
| `v∗u` (vertical composition of 2-cells / Godement product) <!-- TRANSLATOR NOTE: source `v*u`; interpreted as horizontal/vertical composition in the 2-category of fibered categories. -->                            | VI               |
| `F ×_E G` (fibre product of fibered categories) <!-- TRANSLATOR NOTE: source `𝓞F×_𝓞E𝓞G`. -->                                                                                                                          | VI               |
| `f^∗: Cat_{/E} → Cat_{/E′}` (base change of fibered categories) <!-- TRANSLATOR NOTE: source `^*: Cat_/𝓞E→ Cat_/𝓞E'`. -->                                                                                             | VI               |
| `Γ(G/E)`, `Γ̲(G/E)` (sections / sheaf of sections of a fibered category) <!-- TRANSLATOR NOTE: source `Γ (𝓞G/𝓞E) et Γ (𝓞G/𝓞E)`; the two are distinguished by an underline in the original which the OCR collapses. --> | VI               |
| `F_S` (fibre of a fibered category over `S`)                                                                                                                                                                          | VI               |
| `f^∗_F(...)` or `f^∗(...)` (inverse image along `f`)                                                                                                                                                                  | VI               |
| `Γ_f(...)`                                                                                                                                                                                                            | VI               |
| `Hom_•(F, G)` <!-- TRANSLATOR NOTE: source `Hom_ (𝓞F,𝓞G)`; subscript glyph not recovered from OCR. -->                                                                                                                | VI               |
| `Ĉat_{/E}` (a hatted variant — pseudo-functorial 2-category) <!-- TRANSLATOR NOTE: source `Cat^_/𝓞E`; the hat is restored on `Cat`. -->                                                                               | VI               |
| `F/E` (fibered category `F` over `E`)                                                                                                                                                                                 | VI               |
| `f_∗^F` or `~f_∗` (direct image; "tilde" variant)                                                                                                                                                                     | VI               |

## Fundamental group (Exposé V) and étale-topology refinements (Exposé XIII)

| Notation                                                                                                                                                                              | Where introduced |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `π_1(S, a)` (fundamental group at the geometric point `a`) <!-- TRANSLATOR NOTE: source `_1(S,a)`; the OCR systematically drops the `π` prefix on `π_1`. Restored here and below. --> | V                |
| `π_1(S; a, a′)` (set of paths from `a` to `a′`)                                                                                                                                       | V                |
| `π_1(f; a′)` (induced morphism on fundamental groups)                                                                                                                                 | V                |
| `C(S)` (category of finite étale covers of `S`) <!-- TRANSLATOR NOTE: source `𝓞C(S)`; the script-O is artefactual. -->                                                                | V                |
| `Sch` (category of schemes)                                                                                                                                                           | V                |
| `μ_{n, S}` (group scheme of `n`-th roots of unity over `S`)                                                                                                                           | XI               |
| `X^{an}`, `f^{an}` (analytification)                                                                                                                                                  | XII              |
| `SF` or `S(F)` (sheaf associated to a presheaf `F`)                                                                                                                                   | XII              |
| `H^1_t(U, F)` (Čech `H^1` for the topology `t`)                                                                                                                                       | XII              |
| `R^1_t g_∗ F` (higher direct image for the topology `t`)                                                                                                                              | XII              |
| `C_t((U, X)/S)` or `C_t` (category for the topology `t`)                                                                                                                              | XII              |
| `π_1^t((U, X)/S, a)`, `π_1^t(U, a)`, `π_1^t(U)` (fundamental group for `t`) <!-- TRANSLATOR NOTE: source `_1^t(...)`; `π` prefix restored. -->                                        | XIII             |
| `(g_∗^t Φ)_{T′}`                                                                                                                                                                      | XIII             |
| `H^0(V, C_V)^Π`                                                                                                                                                                       | XIII             |
| `π_1^𝐋(U, a)` (fundamental group with prime-to-`𝐋` coefficients) <!-- TRANSLATOR NOTE: `𝐋` denotes a set of prime numbers; source `_1^𝐋 (U,a)`. -->                                   | XIII             |
| `π_1′(X, a)` (a derived / first variant of `π_1`) <!-- TRANSLATOR NOTE: source `_1'(X,a)`. -->                                                                                        | XIII             |
| `π_1^𝐋(X/S, g, s̄)` or `π_1^𝐋(X/S, g)` (fundamental group of a relative scheme) <!-- TRANSLATOR NOTE: source `_1^𝐋 (X/S,g,bar s)`; "bar s" rendered as `s̄`. -->                        | XIII             |
| `π_1^𝐋(X_{s̄}, a)_K` (fundamental group of a geometric fibre, base extension to `K`) <!-- TRANSLATOR NOTE: source `_1^𝐋 (X_bar s,a)_K`. -->                                            | XIII             |
| `𝐙_ℓ[1]` (a Tate-twist–like degree shift)                                                                                                                                             | XIII             |
