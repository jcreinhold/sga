# Exposé III. Infinitesimal extensions

<!-- label: III.III -->

*by M. Demazure*

<!-- original page 83 -->

[^N.D.E-III-0] In this Exposé, we place ourselves in the following general situation. We have a scheme `S` and a
coherent nilpotent ideal `I` on `S`. We denote by `Sₙ` the closed subscheme of `S` defined by the ideal `Iⁿ⁺¹`
(`n ≥ 0`). In particular `S₀` is defined by `I`. Since `I` is nilpotent, `Sₙ` is equal to `S` for `n` large enough, and
the `Sᵢ` have the same underlying topological space. A typical example of this situation is the following: `S` is the
spectrum of a local Artinian ring `A`, `I` is the ideal defined by the radical of `A`, so that `S₀` is the spectrum of
the residue field of `A`.

In the preceding situation, one is given a certain number of data above `S₀`, and one looks above `S` for data which
lift them, that is to say, which give them back by base change from `S` to `S₀`. This is done step by step, by way of
the `Sₙ`. At each step, we propose to define the obstructions encountered, and to classify, when they exist, the
solutions obtained.

The passage from `Sₙ` to `Sₙ₊₁` can be generalized as follows: one has a scheme `S`, two ideals `I` and `J` with
`I ⊃ J`, and `I · J = 0` (in the preceding case `S`, `I` and `J` are respectively `Sₙ₊₁`, `I/Iⁿ⁺²`, `Iⁿ⁺¹/Iⁿ⁺²`). We
denote by `S₀` (resp. `S_J`) the closed subscheme of `S` defined by `I` (resp. `J`), and we pose a problem of extension
from `S_J` to `S`.

<!-- original page 84 -->

In (SGA 1, III), problems of extension of morphisms of schemes and of extension of schemes were treated. We pose here
the problems of extension of morphisms of groups, of extension of group structures, and of extension of subgroups.

We have gathered in a § 0 the results of (SGA 1, III) which will be useful to us, in order to put them in the most
convenient form for our purpose, and to spare the reader from having to refer constantly to (SGA 1, III).[^N.D.E-III-1]
§ 1 collects some computations of group cohomology which will be useful in what follows and which have nothing to do
with scheme theory. §§ 2 and 3 treat respectively of the extension of group morphisms and the extension of group
structures. In § 4, we have briefly recalled the proof of a result stated in (TDTE IV) concerning the extension of
subschemes, and applied this result to the problem of extension of subgroups. For the rest of the Seminar, only the
result of § 2, concerning the extension of morphisms of groups, will be indispensable.[^N.D.E-III-2]

The idea of reducing infinitesimal extension problems to the usual computations of cohomology in extensions of groups
was suggested by J. Giraud at the oral exposé (whose computations were notably more complicated and less transparent).
Unfortunately, it seems that this method only applies well to the first two problems studied, and we have been unable to
escape rather painful computations in the case of extensions of subgroups.

To simplify the language, we shall call a `Y`-functor, resp. `Y`-scheme, etc., a functor, resp. scheme, etc., equipped
with a morphism into the functor `Y`, thus extending the definitions of Exposé I (which concerned only the case of a
representable `Y`).

## 0. Reminders from SGA 1 III and various remarks

<!-- label: III.III.0 -->

<!-- original page 85 -->

Let us first state a general definition.

**Definition 0.1.** *Let `C` be a category, `X` an object of `Ĉ`, `G` a `Ĉ`-group acting on `X`. We say that `X` is
**formally principal homogeneous**[^N.D.E-III-3] under `G` if the following equivalent conditions are satisfied:*

<!-- label: III.III.0.1 -->

*(i) for each object `S` of `C`, the set `X(S)` is empty or principal homogeneous under `G(S)`;*

*(ii) the morphism of functors `G × X → X × X` defined set-theoretically by `(g, x) ↦ (gx, x)` is an isomorphism.*

This being so, we shall put the results of (SGA 1, III, § 5)[^N.D.E-III-4] in the form which will be most useful to us.
We shall employ the following general notations throughout this section. We have a scheme `S` and on `S` two
quasi-coherent ideals `I` and `J` such that

```text
I ⊃ J   and   I · J = 0.
```

In particular we shall therefore have `J² = 0`. We shall denote by `S₀` (resp. `S_J`) the closed subscheme of `S`
defined by the ideal `I` (resp. `J`). For every `S`-functor `X`, we shall systematically denote by `X₀` and `X_J` the
functors obtained by base change from `S` to `S₀` and `S_J`. Same notation for a morphism.

<!-- original page 86 -->

**Definition 0.1.1.**[^N.D.E-III-5] *Let `X` be an `S`-functor. Define a functor `X⁺` above `S` by the formula:*

<!-- label: III.III.0.1.1 -->

```text
Hom_S(Y, X⁺) = Hom_{S_J}(Y_J, X_J) = Hom_S(Y_J, X)
```

*for a variable `S`-scheme `Y`.* In the notations of (Exp. II, 1), one has

```text
X⁺ ≃ ∏_{S_J/S} X_J .
```

The identity morphism of `X_J` defines by construction an `S`-morphism

```text
p_X : X → X⁺ .
```

[^N.D.E-III-6] Explicitly, for every `S`-scheme `Y`, the map

```text
p_X(Y) : Hom_S(Y, X) → Hom_S(Y, X⁺) = Hom_S(Y_J, X)
```

is the map induced by the morphism `Y_J → Y`.

**Remark 0.1.2.** *Let us now observe that if `X` is an `S`-group functor, then `X_J` is an `S_J`-group functor; then
the formula defining `X⁺` endows it with a structure of `S`-group functor, and the description of `p_X` above shows that
`p_X : X → X⁺` is a morphism of `S`-group functors.*

<!-- label: III.III.0.1.2 -->

**Remark 0.1.3.** *On the other hand, for every `S`-group functor `Y`, one has:*

<!-- label: III.III.0.1.3 -->

```text
Hom_{S-gr.}(Y, X⁺) = Hom_{S_J-gr.}(Y_J, X_J).
```

*Indeed, let `f ∈ Hom_S(Y, X⁺)`, corresponding to `f_J ∈ Hom_{S_J}(Y_J, X_J)`; the condition that
`f ∈ Hom_{S-gr.}(Y, X⁺)` is that, for every `T → S` and `y, y′ ∈ Y(T)`, one has `f(y · y′) = f(y) · f(y′)`, and this is
equivalent to*

```text
f_J(y_J) · f_J(y_J′) = f_J((y · y′)_J);
```

*since `(y · y′)_J = y_J · y_J′` (because `Y(T) → Y(T_J) = Y_J(T_J)` is a morphism of groups), this is the condition for
`f_J` to be a morphism of groups. Applying this to `Y = X`, we recover that `p_X`, which corresponds to `id_{X_J}`, is a
morphism of `S`-group functors.*

Let us now return to the general case, but assume that `X` is an `S`-scheme. Since an `S`-morphism of a variable
`S`-scheme `Y` into `X⁺` is by definition an `S_J`-morphism `g_J` of `Y_J` into `X_J`, we shall define an `X⁺`-functor
in abelian groups `L_X` as follows.

**Scholie 0.1.4.**[^N.D.E-III-7] *If `π : Y → S` is a morphism of schemes and `M` an `O_S`-module, we denote by
`M ⊗_{O_S} O_Y` the inverse image `π*(M)`. If `J` is an ideal of `O_S`, we denote by `J · O_Y` the ideal of `O_Y` image
of the morphism*

<!-- label: III.III.0.1.4 -->

```text
π*(J) = J ⊗_{O_S} O_Y → O_Y .
```

Note that, for every morphism of `S`-schemes `f : Z → Y`, one has an epimorphism of `O_Z`-modules:

```text
f*(J · O_Y) → J · O_Z ,                              (0.1.4)
```

as follows from the commutative diagram below:

```text
J ⊗_{O_S} O_Y ⊗_{O_Y} O_Z   ─────►   J ⊗_{O_S} O_Z
            │                                │
            ▼                                ▼
f*(J · O_Y) = (J · O_Y) ⊗_{O_Y} O_Z   ───►   J · O_Z .
```

<!-- original page 87 -->

**Definition 0.1.5.**[^N.D.E-III-8] *Let `X` be an `S`-scheme. For every `X⁺`-scheme `Y`, given by a morphism
`g_J : Y_J → X_J`, we set:*

<!-- label: III.III.0.1.5 -->

```text
Hom_{X⁺}(Y, L_X) = Hom_{O_{Y₀}}(g₀*(Ω¹_{X₀/S₀}), J · O_Y),
```

*where `Ω¹_{X₀/S₀}` denotes the module of relative differentials of `X₀` with respect to `S₀` (cf. SGA 1, I.1 or EGA
IV₄, 16.3), and where `J · O_Y` is regarded as an `O_{Y₀}`-module thanks to the fact that it is annihilated by `I`.*

Then `L_X` is an `X⁺`-functor in abelian groups.[^N.D.E-III-9] Indeed, for every `X⁺`-morphism `f : Z → Y`, the functor
`f₀*` and the morphism `f₀*(J · O_Y) → J · O_Z` of (0.1.4) induce a natural morphism of abelian groups `L_X(f)`:

```text
Hom_{O_{Y₀}}(g₀*(Ω¹_{X₀/S₀}), J · O_Y)
        → Hom_{O_{Z₀}}(f₀* g₀*(Ω¹_{X₀/S₀}), f₀*(J · O_Y))
        → Hom_{O_{Z₀}}(f₀* g₀*(Ω¹_{X₀/S₀}), J · O_Z).
```

Let us finally note that `L_X(f)` is described locally as follows. Note first that `Y` and `Y_J` have the same
underlying topological space, and similarly for `V` and `V_J` if `V` is an open subset of `Y`. Let then `U = Spec(A)` be
an affine open of `X` above an affine open `Spec(Λ)` of `S`, `V = Spec(B)` an affine open of `Y` such that
`g_J(V_J) ⊂ U`, and `W = Spec(C)` an affine open of `f⁻¹(V)`. Let `J` and `I` be the ideals of `Λ` corresponding to `J`
and `I`. Then `f` (resp. `g_J`) induces a morphism of `Λ`-algebras `θ : B → C` (resp. `φ : A → B/JB`), and one obviously
has `θ(JB) ⊂ JC`. On the other hand, `m ∈ Hom_{O_{Y₀}}(g₀*(Ω¹_{X/S}), J · O_Y)` induces an element `D` of

```text
Hom_{O_{V₀}}(g₀*(Ω¹_{U/S}), J · O_V) = Hom_{B/IB}(Ω¹_{A/Λ} ⊗_A B/IB, JB) = Der_Λ(A, JB),
```

and the image of `L_X(f)(m)` in

```text
Hom_{O_{W₀}}(f₀* g₀*(Ω¹_{U/S}), J · O_Z) = Hom_{C/IC}(Ω¹_{A/Λ} ⊗_A C/IC, JC) = Der_Λ(A, JC)
```

is none other than `θ ∘ D`.

<!-- original page 88 -->

**Remark 0.1.6.**[^N.D.E-III-10] *Let `f : X → W` be an `S`-morphism. It induces an `S`-morphism `f⁺ : X⁺ → W⁺` defined
as follows: if `g` is an element of `Hom_S(Y, X⁺)`, corresponding to an `S`-morphism `g_J : Y_J → X`, then `f⁺(g)` is
the element `f ∘ g_J` of `Hom_S(Y, W⁺)`. It is clear that the following diagram is commutative:*

<!-- label: III.III.0.1.6 -->

```text
        f
   X ─────► W
   │         │
p_X│         │p_W
   ▼   f⁺    ▼
   X⁺ ────► W⁺ .
```

**Reminders 0.1.7.**[^N.D.E-III-11] *In this paragraph, given an `S`-scheme `X`, we "recall" certain functorial
properties of the module of differentials `Ω¹_{X/S}` and of the first infinitesimal neighborhood of the diagonal
`Δ⁽¹⁾_{X/S}`, properties which follow easily from (EGA IV₄, §§ 16.1–16.4), but which do not figure there explicitly.*

<!-- label: III.III.0.1.7 -->

**a)** Let us begin by recalling the following facts (cf. EGA II, §§ 1.2–1.5). Let `g : Y → X` be a morphism of schemes,
`π : X′ → X` an affine `X`-scheme, `B` the quasi-coherent `O_X`-algebra `π_*(O_{X′})`; then the `Y`-scheme `Y ×_X X′` is
affine and corresponds to the quasi-coherent `O_Y`-algebra `g*(B)`, and one has a commutative diagram of bijections:

```text
Hom_X(Y, X′)            ──∼──►    Hom_Y(Y, Y ×_X X′)
    │                                       │
    ≀                                       ≀
    ▼                                       ▼
Hom_{O_X-alg.}(B, g_*(O_Y))   ──∼──►   Hom_{O_Y-alg.}(g*(B), O_Y).
```

Moreover, these bijections are functorial in the pair `(X, X′)`, i.e., if `W′` is an affine `W`-scheme, corresponding to
the quasi-coherent `O_W`-algebra `A`, if one has a commutative diagram of morphisms of schemes

```text
            X′ ──f′──► W′
          ↗ g′         │
         /             │
        ↗              │
      Y ──g──► X ──f──► W ,
```

and if we denote by `φ : A → f_*(B)` and `φ♯ : f*(A) → B` (resp. `θ : B → g_*(O_Y)` and `θ♯ : g*(B) → O_Y`) the algebra
morphisms associated to `f′` (resp. to a variable `X`-morphism `g′ : Y → X′`), then one has the following commutative
diagram (where `Y` is viewed as a `W`-scheme via `f ∘ g`):

<!-- original page 89 (cont.) -->

```text
                         g′ ↦ f′ ∘ g′
Hom_X(Y, X′) ──────────────────────► Hom_W(Y, W′)
                                          │
                                          ≃
                                          ▼
                                Hom_{O_W-alg.}(A, f_* g_*(O_Y))
                                          │
                                          ≃
       θ ↦ θ ∘ φ♯                         ▼
Hom_{O_X-alg.}(B, g_*(O_Y)) ──────► Hom_{O_X-alg.}(f*(A), g_*(O_Y))
       │                                  │
       ≀                                  ≀
       ▼   ψ ↦ ψ ∘ g*(φ♯)                 ▼
Hom_{O_Y-alg.}(g*(B), O_Y) ──────► Hom_{O_Y-alg.}(g* f*(A), O_Y).
```

**b)** Let now `X` be an `S`-scheme. Let `Ω¹_{X/S}` be the module of differentials of `X` over `S`, and `Δ⁽¹⁾_{X/S}` the
first infinitesimal neighborhood of the diagonal immersion `δ_X : X → X ×_S X`; it is a subscheme of `X ×_S X`, of which
the diagonal `Δ_{X/S}` is a closed subscheme. We denote by `pr_X^i` (`i = 1, 2`) the two projections `X ×_S X → X`, and
by `π_X` the restriction of `pr_X^1` to `Δ⁽¹⁾_{X/S}`.

On the one hand, every morphism `f : X → W` of `S`-schemes induces an `S`-morphism `Δ⁽¹⁾ f : Δ⁽¹⁾_{X/S} → Δ⁽¹⁾_{W/S}`
such that the following diagram is commutative:

```text
       δ_X            pr_X
   X ─────► Δ⁽¹⁾_{X/S} ─────► X ×_S X ─────► X
   │              │               │           │
 f │       Δ⁽¹⁾f │            f×f│         f │
   ▼       δ_W   ▼                ▼   pr_W   ▼
   W ─────► Δ⁽¹⁾_{W/S} ─────► W ×_S W ─────► W .
```

On the other hand, `Δ⁽¹⁾_{X/S}` is, via the projection `π_X`, an affine `X`-scheme, spectrum of the augmented
quasi-coherent `O_X`-algebra

```text
P¹_{X/S} = O_X ⊕ Ω¹_{X/S},
```

where `Ω¹_{X/S}` is an ideal of square zero; the augmentation is the morphism of `O_X`-algebras `ε_X : P¹_{X/S} → O_X`
which vanishes on `Ω¹_{X/S}` and which corresponds to the closed immersion `δ_X : X ↪ Δ⁽¹⁾_{X/S}`. Then, every morphism
of `S`-schemes `f : X → W` induces a morphism of augmented `O_X`-algebras

```text
f*(P¹_{W/S}) = O_X ⊕ f*(Ω¹_{W/S}) → P¹_{X/S} = O_X ⊕ Ω¹_{X/S}
```

that is, equivalently, a morphism of `O_X`-modules

```text
f_{X/W/S} : f*(Ω¹_{W/S}) → Ω¹_{X/S},
```

cf. (EGA IV₄, 16.4.3.6) (and (16.4.18.2) for the notation `f_{X/W/S}`).

<!-- original page 90 -->

Since `π_X : Δ⁽¹⁾_{X/S} → X` is affine, then, by a), `Δ⁽¹⁾ f` is entirely determined by `f_{X/W/S}` and, for every
`X`-scheme `g : Y → X`, the set

```text
Hom_X(Y, Δ⁽¹⁾_{X/S}) ≃ Hom_{O_Y-alg.}(O_Y ⊕ g*(Ω¹_{X/S}), O_Y)
```

is identified with a subset of `Hom_{O_Y}(g*(Ω¹_{X/S}), O_Y)`, namely the subset

```text
Hom̃_{O_Y}(g*(Ω¹_{X/S}), O_Y)
```

formed by the `O_Y`-morphisms `ψ : g*(Ω¹_{X/S}) → O_Y` such that `Im(ψ)` is an ideal of `O_Y` of square
zero.[^N.D.E-III-12]

Consequently, applying a) to the diagram

```text
              Δ⁽¹⁾ f
   Δ⁽¹⁾_{X/S} ────► Δ⁽¹⁾_{W/S}
       ↗
    g′│
       │
    Y ──g──► X ──f──► W
```

and taking into account that `Δ⁽¹⁾ f` is the restriction to `Δ⁽¹⁾_{X/S}` of `f × f`, one obtains the following
commutative diagram, functorial in the `X`-scheme `Y ──g──► X`:

```text
                              (g, g′) ↦ (f∘g, f∘g′)
Hom_X(Y, X ×_S X) ──────────────────────────────► Hom_W(Y, Δ⁽¹⁾_{W/S})
       ↑                                                  ↑
       │                                                  │
       │                              g′ ↦ Δ⁽¹⁾f ∘ g′
Hom_X(Y, Δ⁽¹⁾_{X/S}) ────────────────────────► Hom_W(Y, Δ⁽¹⁾_{W/S})       (0.1.7 (∗))
       │                                                  │
       ≃                                                  ≃
       ▼            ψ ↦ ψ ∘ g*(f_{X/W/S})                  ▼
Hom̃_{O_Y}(g*(Ω¹_{X/S}), O_Y) ──────────────► Hom̃_{O_Y}(g* f*(Ω¹_{W/S}), O_Y).
```

**Remark 0.1.7.1.** *Let us end this paragraph with the following remark, which will be useful later (cf. 0.1.10). If we
denote by `L̃_X` the `X`-functor which to every `X`-scheme `g : Y → X` associates `Hom_{O_Y}(g*(Ω¹_{X/S}), O_Y)`, and
`L̃_f : L̃_X → L̃_W` the morphism of functors defined above (which to every `ψ ∈ L̃_X(Y)` associates
`ψ ∘ g*(f_{X/W/S})`), what precedes shows that we have a commutative diagram of functors:*

<!-- label: III.III.0.1.7.1 -->

```text
X ×̃ X L̃_X  ◄──∼──  Δ⁽¹⁾_{X/S}  ─────► X ×_S X
    │                   │                 │
f ×̃_f│                Δ⁽¹⁾f│           f×f│
    ▼                   ▼                 ▼
W ×̃ W L̃_W  ◄──∼──  Δ⁽¹⁾_{W/S}  ─────► W ×_S W.
```

<!-- original page 91 -->

**Theorem 0.1.8.** *(SGA 1, III 5.1)[^N.D.E-III-13] Let `Y`, `X` be two `S`-schemes, `J` a quasi-coherent ideal of `O_Y`
of square zero, `Y_J` the closed subscheme of `Y` defined by `J`, and `g_J : Y_J → X` an `S`-morphism.*

<!-- label: III.III.0.1.8 -->

*a) The set `P(g_J)` of `S`-morphisms `g : Y → X` which extend `g_J` is either empty, or principal homogeneous under the
abelian group*

```text
Hom_{O_{Y_J}}(g_J*(Ω¹_{X/S}), J).
```

*b) If `i : Y₀ ↪ Y_J` is the closed immersion defined by a quasi-coherent ideal `I ⊃ J` such that `I · J = 0`, and if
`g₀ = g_J ∘ i`, the preceding abelian group is isomorphic to*

```text
Hom_{O_{Y₀}}(g₀*(Ω¹_{X/S}), J).
```

*Proof.* (b) follows at once from (a). Indeed, `J`, being annihilated by `I`, can be considered as an `O_{Y₀}`-module,
whence, by adjunction:

```text
Hom_{O_{Y_J}}(g_J*(Ω¹_{X/S}), J) = Hom_{O_{Y₀}}(i* g_J*(Ω¹_{X/S}), J).
```

To prove (a), we may assume `P(g_J) ≠ ∅`, i.e. that there exists an `S`-morphism `g : Y → X` extending `g_J`. Let us
denote by `j` the immersion `Y_J ↪ Y`. Then `P(g_J)` is the set of `S`-morphisms `g′ : Y → X` such that `g′ ∘ j = g_J`.
The datum of such a `g′` is equivalent to the datum of an `S`-morphism

```text
h : Y → X ×_S X
```

such that `pr₁ ∘ h = g` and `h_J = δ ∘ g_J`, where `h_J = h ∘ j` and `δ` is the diagonal immersion `X ↪ X ×_S X`:

```text
                h_J = δ ∘ g_J
   X ×_S X  ◄──────────────── Y_J
    │  ▲ h                    │
pr₁│   ╲                    j │
    ▼    ╲                     ▼
    X  ◄─g───                  Y .
```

Since `h_J` factors through `δ` and `Y` is in the first infinitesimal neighborhood of the immersion `j : Y_J → Y` (since
`J² = 0`), then, by functoriality (cf. EGA IV₄, 16.2.2 (i)), the `h`'s sought factor uniquely through `Δ⁽¹⁾_{X/S}` (cf.
0.1.7). Set

```text
Y′ = Δ⁽¹⁾_{X/S} ×_X Y    and    Y_J′ = Y′ ×_Y Y_J = Δ⁽¹⁾_{X/S} ×_X Y_J .
```

Then the `h`'s sought are in bijection with the sections `u` of `Y′ → Y` which extend the section `u_J = (δ ∘ g_J, id)`
of `Y_J′ → Y_J`. On the other hand, `Y′` (resp. `Y_J′`) is an affine scheme over `Y` (resp. `Y_J`), corresponding to the
quasi-coherent algebra

```text
A = O_Y ⊕ g*(Ω¹_{X/S}),    resp.    A_J = A ⊗_{O_Y} O_{Y_J} = O_{Y_J} ⊕ g_J*(Ω¹_{X/S}).
```

Let us denote by `ε : A → O_Y` the canonical augmentation of `A` (i.e. the morphism of `O_Y`-algebras `A → O_Y` which
vanishes on `g*(Ω¹_{X/S})`), and likewise define `ε_J : A_J → O_{Y_J}`. Then,

```text
Γ(Y′/Y) ≃ Hom_{O_Y-alg.}(A, O_Y),    Γ(Y_J′/Y_J) ≃ Hom_{O_{Y_J}-alg.}(A_J, O_{Y_J})
```

<!-- original page 92 -->

and, via these isomorphisms, the section `u = (δ ∘ g, id)` (resp. `u_J`) corresponds to `ε` (resp. `ε_J`). Consequently,
`P(g_J)` is in bijection with the set of algebra morphisms `A → O_Y` which reduce to `ε_J`, and via this bijection, `g`
corresponds to `ε`.

Set `M = g*(Ω¹_{X/S})`. Then `Hom_{O_Y-alg.}(A, O_Y)` is identified with the set of `O_Y`-morphisms `ψ : M → O_Y` such
that `Im(ψ)` is an ideal of square zero, and we are interested in those which induce the null morphism
`M → O_{Y_J} = O_Y/J`, i.e. which send `M` into `J`. Conversely, since `J² = 0`, every `O_Y`-morphism `φ : M → J` comes
from a (unique) algebra morphism `A → O_Y`, reducing to `ε_J`. Finally, we have
`Hom_{O_Y}(g*(Ω¹_{X/S}), J) = Hom_{O_{Y_J}}(g_J*(Ω¹_{X/S}), J)` since `J² = 0` (cf. the proof of (b) already seen). One
thus obtains a bijection

```text
P(g_J) ≃ Hom_{O_{Y_J}}(g_J*(Ω¹_{X/S}), J)
```

by which `g` corresponds to the null morphism.

For every `m ∈ Hom_{O_{Y_J}}(g_J*(Ω¹_{X/S}), J)`, denote by `m · g` the element of `P(g_J)` associated to `g` and `m` by
the preceding bijection. We have already seen that `0 · g = g`; it remains to see that

```text
m′ · (m · g) = (m + m′) · g.                            (0.1.8 (∗))
```

This is verified locally.[^N.D.E-III-14] Indeed, the two preceding morphisms `Y → X` induce the same continuous map as
`g` between the underlying topological spaces; it therefore suffices to verify that for every affine open `U = Spec(A)`
of `X` above an affine open `Spec(Λ)` of `S`, and every affine open `V = Spec(B)` of `g⁻¹(U)`, they induce the same
morphism of `Λ`-algebras `A → B`.

Let `J = Γ(V, J)` and let `φ, ψ` and `η` be the morphisms `A → B` induced by `g`, `m · g` and `m′ · (m · g)`
respectively; they coincide modulo `J`. One can uniquely write `ψ = φ + D` (resp. `η = ψ + D′`), where `D` (resp. `D′`)
is an element of

```text
Der_φ(A, J) = {δ ∈ Hom_Λ(A, J) | δ(ab) = φ(a) δ(b) + φ(b) δ(a)}
```

(resp. `Der_ψ(A, J)`). But `Der_φ(A, J) = Der_ψ(A, J)` since `J² = 0`, and both are identified with

```text
Hom_{B/J}(Ω¹_{A/Λ} ⊗_A B/J, J),
```

and via this identification `D` corresponds to `m` and `D′` to `m′`. Then `η = φ + D + D′` and `D + D′` corresponds to
`m + m′`, whence the equality (∗).

**Corollary 0.1.9.**[^N.D.E-III-15] *Let `X` be an `S`-scheme; resume the notations of 0.1.5. Then `X` is endowed with a
(left) action of the `X⁺`-abelian group `L_X`, which makes `X` into a formally principal homogeneous object under `L_X`
above `X⁺`, i.e. one has an isomorphism of `X⁺`-functors:*

<!-- label: III.III.0.1.9 -->

```text
L_X × X ──∼──► X × X
       X⁺          X⁺
```

*(defined set-theoretically by `(m, x) ↦ (x, m · x)`).*

*Proof.* Let `i₀` be the immersion `X₀ ↪ X`. Note first that, since `X₀ = X ×_S S₀`, one has
`i₀*(Ω¹_{X/S}) ≃ Ω¹_{X₀/S₀}` (cf. EGA IV, 16.4.5).

Let `Y` be an `X⁺`-scheme, given by an `S`-morphism `g_J : Y_J → X`, and let `g₀ : Y₀ → X₀` be the morphism obtained by
base change. By 0.1.8, if `Hom_{X⁺}(Y, X)` is non-empty, it is a principal homogeneous set under the group

```text
Hom_{O_{Y₀}}(g₀* i₀*(Ω¹_{X/S}), J · O_Y),
```

which is identified with `Hom_{O_{Y₀}}(g₀*(Ω¹_{X₀/S₀}), J · O_Y) = L_X(Y)`. One therefore has a bijection

```text
L_X(Y) × Hom_{X⁺}(Y, X)  ──∼──►  Hom_{X⁺}(Y, X ×_{X⁺} X)
```

given by `(m, g) ↦ (g, m · g)`. Let us show that this is "functorial in `Y`".

Let `f : Z → Y` be a morphism of `S`-schemes. It is a question of showing that the diagram below is commutative:

```text
L_X(Y) × Hom_{X⁺}(Y, X) ──∼──► Hom_{X⁺}(Y, X ×_{X⁺} X)
   │                                       │
L_X(f) × f                             f × f
   ▼                                       ▼
L_X(Z) × Hom_{X⁺}(Z, X) ──∼──► Hom_{X⁺}(Z, X ×_{X⁺} X).
```

If `Hom_{X⁺}(Y, X) = ∅`, there is nothing to show. It therefore suffices to see that, for every `S`-morphism `g : Y → X`
extending `g_J` and every `m ∈ L_X(Y)`, one has:

```text
(m · g) ∘ f = L_X(f)(m) · (g ∘ f).                       (0.1.9 (∗))
```

These two `S`-morphisms `Z → X` coincide on `Z_J` with `g_J ∘ f_J`; in particular, they induce the same continuous map
as `g ∘ f` between the underlying topological spaces. Consequently, it suffices to see that, if `z ∈ Z`, `y = f(z)`,
`x = g(y)`, and if `A`, `B`, `C` denote respectively the local rings `O_{X,x}`, `O_{Y,y}`, `O_{Z,z}`, then the morphisms
`A → C` induced by `(m · g) ∘ f` and `L_X(f)(m) · (g ∘ f)` coincide. Denote by `s` the image of `x` in `S`,
`Λ = O_{S,s}`, `J` and `I` the ideals of `Λ` corresponding to `J` and `I`, and let `φ, ψ : A → B` and `θ : B → C` be the
morphisms of `Λ`-algebras induced by `g`, `m · g`, and `f`. Then `m` induces an element `D` of

```text
Hom_{B/IB}(Ω¹_{A/Λ} ⊗_A B/IB, JB) = Der_Λ(A, JB)
```

and one has `ψ = φ + D`; hence `(m · g) ∘ f` corresponds to `θ ∘ ψ = θ ∘ φ + θ ∘ D`. Now, we have seen in 0.1.5 that
`θ ∘ D` is the image of `L_X(f)(m)` in

```text
Hom_{C/IC}(Ω¹_{A/Λ} ⊗_A C/IC, JC) = Der_Λ(A, JC);
```

consequently, `θ ∘ φ + θ ∘ D` is the image of `L_X(f)(m) · (g ∘ f)`. This proves the equality (0.1.9 (∗)).

**Corollary 0.1.10.**[^N.D.E-III-16] *a) `L_X` depends functorially on `X`: for every `S`-morphism `f : X → W`, there
exists an `S`-morphism `L_f : L_X → L_W` which is a morphism of abelian groups "above `f⁺`", i.e., the diagram*

<!-- label: III.III.0.1.10 -->

```text
        L_f
   L_X ────► L_W
   │           │
   ▼   f⁺      ▼
   X⁺ ──────► W⁺
```

*is commutative, and for every `Y → X⁺`,*

```text
L_f(Y) : Hom_{X⁺}(Y, L_X) → Hom_{W⁺}(Y, L_W)
```

*(where `Y` is above `W⁺` via `f⁺`) is a morphism of abelian groups.*

*b) Moreover, the following diagram is commutative:*

```text
L_X × X ─∼─► X ×_{X⁺} X
   │              │
L_f × f        f × f
   ▼              ▼
L_W × W ─∼─► W ×_{W⁺} W .
```

*Proof.* a) `L_f` is induced by the morphism of `O_{X₀}`-modules `f_{X₀/W₀/S₀} : f₀*(Ω¹_{W₀/S₀}) → Ω¹_{X₀/S₀}` (cf.
0.1.7 b)): for every `X⁺`-scheme `Y`, given by an `S`-morphism `g_J : Y_J → X`, one has a commutative diagram,
functorial in `Y`:

```text
                          L_f(Y)
Hom_{O_{Y₀}}(g₀*(Ω¹_{X₀/S₀}), J · O_Y) ───► Hom_{O_{Y₀}}(g₀* f₀*(Ω¹_{W₀/S₀}), J · O_Y)
       │                                                       │
       ▼                                                       ▼
     {g_J}                                                {f_J ∘ g_J}
```

where `L_f(Y)` is the map `ψ ↦ ψ ∘ g₀*(f_{X₀/W₀/S₀})`, which is indeed a morphism of abelian groups.[^N.D.E-III-17]

Let us prove (b). Let `Y` be an `X⁺`-scheme; if `Hom_{X⁺}(Y, X) = ∅` there is nothing to show. So let
`g ∈ Hom_{X⁺}(Y, X)`; it must be seen that for every `m ∈ L_X(Y)`, one has:

```text
f ∘ (m · g) = L_f(Y)(m) · (f ∘ g).                       (0.1.10 (∗))
```

Now, `g` being fixed, `Hom_X(Y, X ×_{X⁺} X)` is a subset of `Hom_X(Y, Δ⁽¹⁾_{X/S})` and

```text
L_X(Y) = Hom_{O_{Y₀}}(g₀*(Ω¹_{X₀/S₀}), J · O_Y) = Hom_{O_Y}(g*(Ω¹_{X/S}), J · O_Y)
```

a subset of `L̃_X(Y)` (cf. 0.1.7); finally, `L_f(Y)` is the restriction to `L_X(Y)` of the map `L̃_f(Y)`. Moreover, the
bijection

```text
L_X(Y) ──∼──► Hom_X(Y, X ×_{X⁺} X),    m ↦ (g, m · g)
```

is (the inverse of) the restriction to `L_X(Y) ⊂ L̃_X(Y)` of the bijection `Hom_X(Y, Δ⁽¹⁾_{X/S}) ──∼──► {g} × L̃_X(Y)`
considered in 0.1.7.1. Consequently, the equality (0.1.10 (∗)) results from (0.1.7 (∗)); indeed, if we denote by `g′`
the `X`-morphism `Y → Δ⁽¹⁾_{X/S}` defined by `(g, m · g)`, then the element of `L̃_W(Y)` corresponding to
`(f ∘ g, f ∘ g′)` is `L̃_f(Y)(m) = L_f(Y)(m)`, i.e., one indeed has

```text
L_f(m) · (f ∘ g) = f ∘ (m · g).
```

**Lemma 0.1.11.** *Let `X`, `X′` be two `S`-schemes. One has a commutative diagram:*

<!-- label: III.III.0.1.11 -->

```text
L_X ×_S L_{X′} ──∼──► L_{X ×_S X′}
       │                  │
       ▼                  ▼
X⁺ ×_S X′⁺  ──∼──► (X ×_S X′)⁺ .
```

[^N.D.E-III-18] *Proof.* First, for every `S`-scheme `Y`, `Hom_S(Y, X⁺ ×_S X′⁺)` equals `Hom_S(Y, X⁺) × Hom_S(Y, X′⁺)`
and this is isomorphic to

```text
Hom_S(Y_J, X) × Hom_S(Y_J, X′) = Hom_S(Y, (X ×_S X′)⁺);
```

this proves that `X⁺ ×_S X′⁺ ≃ (X ×_S X′)⁺`.

Next, let `Y` be a scheme above `X⁺ ×_S X′⁺` via a morphism `h : Y_J → X ×_S X′`; set `f = p ∘ h` and `g = q ∘ h`, where
we have denoted by `p, q` the projections of `X ×_S X′` to `X` and `X′`. Since
`Ω¹_{(X₀ ×_{S₀} X′₀)/S₀} ≅ p₀*(Ω¹_{X₀/S₀}) ⊕ q₀*(Ω¹_{X′₀/S₀})` (cf. EGA IV₄, 16.4.23), one obtains a natural
isomorphism:

```text
Hom_{O_{Y₀}}(f₀*(Ω¹_{X₀/S₀}), J · O_Y) × Hom_{O_{Y₀}}(g₀*(Ω¹_{X′₀/S₀}), J · O_Y)
    ≃ Hom_{O_{Y₀}}(h₀*(Ω¹_{(X₀ ×_{S₀} X′₀)/S₀}), J · O_Y)
```

i.e., `L_X(Y) × L_{X′}(Y) ≃ L_{X ×_S X′}(Y)`.

**Remark 0.1.12.**[^N.D.E-III-19] *Let `C` be a category stable under fibered products, `S` an object of `C`, `T₁`, `T₂`
two objects above `S` and, for `i = 1, 2`, `L_i` and `X_i` two objects above `T_i`:*

<!-- label: III.III.0.1.12 -->

```text
L_1 ──► T_1 ◄── X_1        L_2 ──► T_2 ◄── X_2
              ╲                    ╱
                ╲                ╱
                  ▼            ▼
                       S                  .
```

*Then one has a natural isomorphism:*

```text
(L_1 ×_{T_1} X_1) ×_S (L_2 ×_{T_2} X_2) ≃ (L_1 ×_S L_2) ×_{T_1 ×_S T_2} (X_1 ×_S X_2).
```

Consequently, from the preceding lemma one deduces the:

**Corollary 0.1.13.** *Let `X_1`, `X_2` be two `S`-schemes. One has a commutative diagram of isomorphisms:*

<!-- label: III.III.0.1.13 -->

```text
        L_{X_1 ×_S X_2} ×_{(X_1 ×_S X_2)⁺} (X_1 ×_S X_2)
              │                                ╲
   (0.1.11) ≃ ▼                                  ≃
        (L_{X_1} ×_S L_{X_2}) ×_{(X_1⁺ ×_S X_2⁺)} (X_1 ×_S X_2)
                              ──∼──►
        (L_{X_1} ×_{X_1⁺} X_1) ×_S (L_{X_2} ×_{X_2⁺} X_2) .
                                                (0.1.12)
```

We can now state:

<!-- original page 88 (cont.) -->

**Proposition 0.2.** *For every `S`-scheme `X`, one can define a (left) action of the `X⁺`-abelian group `L_X` on the
`X⁺`-object `X`, such that:*

<!-- label: III.III.0.2 -->

*(i) this action makes `X` into a formally principal homogeneous object under `L_X` above `X⁺`, i.e. the morphism*

```text
L_X × X ──► X × X
       X⁺          X⁺
```

*is an isomorphism of `X⁺`-functors;*

*(ii) this action is functorial in the `S`-scheme `X`, i.e., for every `S`-morphism `f : X → W`, the following diagram
is commutative:*

```text
L_X ×_{X⁺} X ─────► X
     │              │
 L_f × f          f │
     ▼              ▼
L_W ×_{W⁺} W ─────► W ;
```

*(iii) this action "commutes with fibered product", i.e. for all `S`-schemes `X_1` and `X_2`, the following diagram is
commutative:*

```text
L_{X_1 ×_S X_2} ×_{(X_1 ×_S X_2)⁺} (X_1 ×_S X_2)  ──►  X_1 ×_S X_2
        │                                                    ▲
        ≃                                                    │
        ▼                                                    │
(L_{X_1} ×_S L_{X_2}) ×_{(X_1⁺ ×_S X_2⁺)} (X_1 ×_S X_2) ──∼──► (L_{X_1} ×_{X_1⁺} X_1) ×_S (L_{X_2} ×_{X_2⁺} X_2).
```

<!-- original page 89 -->

*Proof.*[^N.D.E-III-20] (i) and (ii) follow respectively from Corollaries 0.1.9 and 0.1.10. To prove (iii), denote
`P(X) = L_X ×_{X⁺} X`, for every `S`-scheme `X`. Then, by (ii) applied to the projections `p_i : X_1 ×_S X_2 → X_i`, one
obtains commutative squares

```text
P(X_1 ×_S X_2)  ─────►  X_1 ×_S X_2
       │                     │
  L_{p_i} × p_i             p_i
       ▼                     ▼
   P(X_i)         ─────►   X_i
```

<!-- original page 90 -->

for `i = 1, 2`, and hence a commutative square:

```text
P(X_1 ×_S X_2)         ─────►   X_1 ×_S X_2
       │                                ║
       ▼                                ▼
P(X_1) ×_S P(X_2)      ─────►   X_1 ×_S X_2 .
```

Combining this with Corollary 0.1.13, one obtains that the vertical arrow is an isomorphism, and that one has the
commutative diagram announced in (iii).

<!-- original page 90 -->

**Remark 0.3.** *Suppose the `X⁺`-scheme `Y` flat over `S` (cf. SGA 1, IV). Then one can write*

<!-- label: III.III.0.3 -->

```text
Hom_{X⁺}(Y, L_X) = Hom_{O_{Y₀}}(g₀*(Ω¹_{X₀/S₀}), J ⊗_{O_{S₀}} O_{Y₀}).
```

**Remark 0.4.** *Denote by `π₀ : X₀ → S₀` the structural morphism and suppose there exists an `O_{S₀}`-module
`ω¹_{X₀/S₀}` such that `Ω¹_{X₀/S₀} ≃ π₀*(ω¹_{X₀/S₀})` (the case will arise in particular when `X₀` is an `S₀`-group, cf.
II, 4.11). If one defines a functor `L′_X` above `S` by the formula*

<!-- label: III.III.0.4 -->

```text
Hom_S(Y, L′_X) = Hom_{O_{Y₀}}(ω¹_{X₀/S₀} ⊗_{O_{S₀}} O_{Y₀}, J · O_Y),     (0.4.1)
```

*one then has `Hom_{X⁺}(Y, L_X) = Hom_S(Y, L′_X)` for every `X⁺`-scheme `Y`, that is to say*

```text
L_X = L′_X × X⁺ .
              S
```

[^N.D.E-III-21] Then, since `L_X ×_{X⁺} X = L′_X ×_S X`, the action of `L_X` on `X` induces an action of `L′_X` on `X`,
and this action respects the morphism `p_X : X → X⁺`; indeed, if `Y` is an `S`-scheme, `h : Y → X` an `S`-morphism and
`m` an element of `L′_X(Y)`, then `h` and `m · h` have the same restriction to `Y_J`, i.e. `p_X(m · h) = p_X(h)`.

<!-- original page 91 -->

**Remark 0.5.** *Keep the hypotheses and notations of 0.4 and suppose moreover that `Y` is an `S`-scheme flat over `S`.
Then we have*

<!-- label: III.III.0.5 -->

```text
Hom_{X⁺}(Y, L_X) = Hom_S(Y, L′_X) = Hom_{S₀}(Y₀, L⁰_X),
```

*where the `S₀`-functor in abelian groups `L⁰_X` is defined by the following identity (with respect to the variable
`S₀`-scheme `T`):*

```text
Hom_{S₀}(T, L⁰_X) = Hom_{O_T}(ω¹_{X₀/S₀} ⊗_{O_{S₀}} O_T, J ⊗_{O_{S₀}} O_T).    (0.5.1)
```

*In the notations of (II, 1), we have therefore shown that the functors `L′_X` and `∏_{S₀/S} L⁰_X` have the same
restriction to the full subcategory of `(Sch)/S` whose objects are the `S`-schemes `Y` flat over `S`.*

**Remark 0.6.** *Keep the hypotheses and notations of 0.5[^N.D.E-III-22] and suppose moreover that there exists a
section `ε₀` of `π₀ : X₀ → S₀`; one then has `ω¹_{X₀/S₀} ≃ ε₀*(Ω¹_{X₀/S₀})`.*

<!-- label: III.III.0.6 -->

First, one has (independently of the preceding hypothesis):

```text
Hom_{S₀}(T, L⁰_X) = Γ(T, Hom_{O_T}(ω¹_{X₀/S₀} ⊗_{O_{S₀}} O_T, J ⊗_{O_{S₀}} O_T)).
```

Now suppose that `ω¹_{X₀/S₀}` admits a finite presentation (cf. EGA 0_I, 5.2.5), which will in particular be the case if
`X₀` is locally of finite presentation over `S₀` (cf. EGA IV₄, 16.4.22). Then, if `T` is flat over `S₀`, it follows from
(EGA 0_I, 6.7.6) that

```text
Hom_{O_T}(ω¹_{X₀/S₀} ⊗_{O_{S₀}} O_T, J ⊗_{O_{S₀}} O_T) ≃ Hom_{O_{S₀}}(ω¹_{X₀/S₀}, J) ⊗_{O_{S₀}} O_T ,
```

whence

```text
Hom_{S₀}(T, L⁰_X) = Γ(T, Hom_{O_{S₀}}(ω¹_{X₀/S₀}, J) ⊗_{O_{S₀}} O_T).
```

Introducing the notation `W(·)` of (I, 4.6.1), we have therefore proved that for every `S₀`-scheme `T` flat over `S₀`,
one has

```text
Hom_{S₀}(T, L⁰_X) = Hom_{S₀}(T, W(Hom_{O_{S₀}}(ω¹_{X₀/S₀}, J))).
```

<!-- original page 92 -->

In summary, if `ω¹_{X₀/S₀}` admits a finite presentation, and if one restricts to the category of `S`-schemes flat over
`S`, one has

```text
L′_X = ∏_{S₀/S} W(Hom_{O_{S₀}}(ω¹_{X₀/S₀}, J)),                  (0.6.1)
```

and `Hom_{O_{S₀}}(ω¹_{X₀/S₀}, J)` is a quasi-coherent `O_{S₀}`-module, by EGA I, 9.1.1.

Note finally that if `ω¹_{X₀/S₀}` is moreover locally free (of finite rank), for example if `X₀` is smooth over `S₀` (in
which case it is automatically locally of finite presentation over `S₀`), one has

```text
Hom_{O_{S₀}}(ω¹_{X₀/S₀}, J) ≃ Lie(X₀/S₀) ⊗_{O_{S₀}} J ,           (0.6.2)
```

where, by abuse of language (`X₀` not being necessarily an `S₀`-group), we denote by `Lie(X₀/S₀)` the dual of the
`O_{S₀}`-module `ω¹_{X₀/S₀}`.[^N.D.E-III-23]

Proposition 0.2 (and its proof) has two important corollaries.[^N.D.E-III-24]

**Corollary 0.7.** *Let `X` be an `S`-scheme.*

<!-- label: III.III.0.7 -->

*a) Every `S`-endomorphism of `X` inducing the identity on `X_J` is an automorphism.*

*b) One has an exact sequence of groups:*

```text
0 ──► Hom_{O_{X₀}}(Ω¹_{X₀/S₀}, J · O_X) ──i──► Aut_S(X) ──► Aut_{S_J}(X_J) .
```

*c) Moreover, if one makes `Aut_S(X)` act on the first group by transport of structure, one has, for all `u ∈ Aut_S(X)`
and `m ∈ Hom_{O_{X₀}}(Ω¹_{X₀/S₀}, J · O_X)`:*

```text
i(u · m) = u · i(m) · u⁻¹.
```

<!-- original page 93 -->

*Proof.* By 0.2 (i), `Hom_{X⁺}(X, X)` is a principal homogeneous set under `Hom_{X⁺}(X, L_X)`, since it is certainly
non-empty: it contains a marked point, namely the identity automorphism of `X`.[^N.D.E-III-25] Consequently, the map
`m ↦ m · id_X` induces a bijection

```text
Hom_{O_{X₀}}(Ω¹_{X₀/S₀}, J · O_X) = L_X(X) ──∼──► Hom_{X⁺}(X, X).
```

Let `m ∈ L_X(X)` and let `f = m′ · id_X` be an element of `Hom_{X⁺}(X, X)`. Applying 0.2 (ii) to `f`, one obtains:

```text
f ∘ (m · id_X) = L_f(X)(m) · f = L_f(X)(m) · (m′ · id_X).
```

On the other hand, since `f` is an `X⁺`-endomorphism of `X`, one has `f_J = id_{X_J}` and therefore `f₀ = id_{X₀}`;
since `L_f` depends only on `f₀` (cf. N.D.E. (17) in 0.1.10), one therefore has `L_f(X)(m) = m`. Consequently, the
equality above rewrites as:

```text
(m′ · id_X) ∘ (m · id_X) = m · (m′ · id_X) = (m + m′) · id_X .
```

This shows that the bijection `m ↦ m · id_X` transforms the group law of `Hom_{X⁺}(X, L_X)` into the composition law of
`X⁺`-endomorphisms of `X`.

It follows first that every element of `Hom_{X⁺}(X, X)` is invertible, which is the first assertion of the statement,
and then that one has an exact sequence

```text
0 ──► Hom_{X⁺}(X, L_X) ──i──► Aut_S(X) ──► Aut_{S_J}(X_J) ,
```

which is the second.

Let us now note that the morphism `i` defined above is functorial in `X` for isomorphisms, because it is defined in
structural terms from the action of `L_X` on `X` above `X⁺`, itself functorial in `X` by assertion (ii) of Proposition
0.2.[^N.D.E-III-26] Hence every automorphism `u` of `X` above `S` induces by transport of structure isomorphisms

```text
h : Hom_{X⁺}(X, L_X) ──∼──► Hom_{X⁺}(X, L_X)
```

and `f : Aut_S(X) ──∼──► Aut_S(X)` such that the following diagram is commutative:

```text
            i
Hom_{X⁺}(X, L_X) ────► Aut_S(X)
      │                    │
      h                    f
      ▼     i              ▼
Hom_{X⁺}(X, L_X) ────► Aut_S(X)
```

<!-- original page 94 -->

i.e. such that `f ∘ i = i ∘ h`. On the other hand, `f` is given by the commutative diagram

```text
        a
   X ─────► X
   │         │
 u │         │ u
   ▼  f(a)   ▼
   X ─────► X ,
```

that is, `f(a) = u ∘ a ∘ u⁻¹` for every `a ∈ Aut_S(X)`. Writing `i(h(m)) = f(i(m))`, one finds the desired formula.

**Corollary 0.7.bis.** *Let `X` be an `S`-scheme such that `X_J` is an `S_J`-monoid. Then `L_X` is endowed with a
structure of `S`-monoid, one has a split exact sequence of `S`-monoids:*

<!-- label: III.III.0.7.bis -->

```text
                i           p
1 ──► L′_X ────► L_X ⇄ ──► X⁺ ──► 1
                     s
```

*and the monoid law induced on `L′_X` coincides with its abelian group structure. In particular, if `X_J` is an
`S_J`-group, then `L_X` is an `S`-group and is the semidirect product of `X⁺` and `L′_X`.*

*Proof.* Indeed, since `X_J` is an `S_J`-monoid, then `X⁺ = ∏_{S_J/S} X_J` is an `S`-monoid (indeed, one has
`X⁺(Y) = X_J(Y_J)` for every `Y → S`). For every `S`-scheme `Y`, denote by `Ỹ_J` the `Y_J`-affine scheme corresponding
to the quasi-coherent `O_{Y_J}`-algebra `O_{Y_J} ⊕ J · O_Y` (i.e. the graded algebra associated to the filtration
`O_Y ⊃ J · O_Y`). Then `L_X(Y)` is identified with `X_J(Ỹ_J)` and `L′_X(Y)` with the kernel of the morphism
`p : X_J(Ỹ_J) → X_J(Y_J)` induced by the "zero section" `Y_J → Ỹ_J` (i.e. by the morphism of `O_{Y_J}`-algebras
`O_{Ỹ_J} → O_{Y_J}` vanishing on the ideal `J · O_Y`). One has therefore, for every `Y → S`, a split exact sequence of
monoids, functorial in `Y`:

```text
                       i              p
1 ──► L′_X(Y) ──────► L_X(Y) ⇄ ──► X⁺(Y) ──► 1 .
                            s
```

It remains to see that the monoid law induced on `L′_X` coincides with its abelian group structure. Denote by `µ` the
monoid law of `L_X` and `e` its unit section; one must show that for all `m, m′ ∈ L′_X(Y)`, one has

```text
µ(m · e, m′ · e) = (m + m′) · e .
```

This can be seen in either of the following ways. On the one hand, one can revisit the proof of equality (0.1.10 (∗)) by
replacing the morphism `f : X → W` appearing there with the morphism `µ : L_X ×_S L_X → L_X`. Identifying
`X⁺(Y) = X_J(Y_J)` with its image by `s` in `L_X(Y) = X_J(Ỹ_J)`, one obtains that, for all `g, g′ ∈ X_J(Y_J)` and
`m, m′ ∈ L′_X(Y)`, one has

```text
µ(m · g, m′ · g′) = L_µ^{(g, g′)}(m, m′) · µ(g, g′),                      (⋆)
```

where `L_µ^{(g, g′)}` denotes the morphism derived from `µ` at the point `(g, g′)` (i.e. `Ỹ_J` is above `L_X ×_S L_X`
via `(g, g′)`). In particular, one has `µ(m · e, m′ · e) = L_µ^{(e, e)}(m, m′) · e`; now
`L_µ^{(e, e)}(m, m′) = L_{ℓ_e}(m′) + L_{r_e}(m)`, where `ℓ_e` (resp. `r_e`) denotes left (resp. right) translation by
`e`, which is the identity map of `X_J`, whence `L_µ^{(e, e)}(m, m′) = m + m′`.

Alternatively, one can proceed as follows (cf. the proof of [DG70], § II.4, Th. 3.5). By Lemma 0.1.11, the formation of
`X⁺` and of `L_X` "commutes with products", and hence the same holds for `L′_X`; it follows that the morphism
`µ′ : L′_X × L′_X → L′_X` induced by `µ` is a homomorphism for the abelian-group structure. One then deduces from Lemma
3.10 of Exp. II that `µ′` coincides with the abelian-group law.

<!-- original page 95 -->

**0.8.**[^N.D.E-III-27] Let now `X` be an `S`-scheme such that `X_J` is an `S_J`-group. Suppose there exists an
`S`-morphism

<!-- label: III.III.0.8 -->

```text
P : X × X ──► X
        S
```

such that the morphism obtained by base change

```text
P_J : X_J × X_J ──► X_J
            S_J
```

is the group law of `X_J`. (An important particular case of the preceding situation will be the case where `X` is an
`S`-group and one takes for `P` its group law.) From this one deduces a morphism

```text
L_P : L_X × L_X ≃ L_{X ×_S X} ──► L_X
              S
```

which, in fact, does not depend on `P`, because it is computed by means of the group law `P_J` of `X_J`, as we shall now
see.[^N.D.E-III-28] Indeed, by (ii) and (iii) of 0.2, for every `Y → S` and `x, x′ ∈ X(Y)`, `m, m′ ∈ L′_X(Y)`, one has

```text
P(m · x, m′ · x′) = L_P^{(x, x′)}(m, m′) · (x, x′) = L_P^{(x, x′)}(m, m′) · µ(g, g′)
```

where `g` (resp. `g′`) is the image of `x` (resp. `x′`) in `X⁺(Y)`. Moreover (cf. the proof of 0.10), `L_P^{(x, x′)}`
equals `L_µ^{(g, g′)}` and, by 0.7.bis (⋆), this is the element of `L′_X(Y)` defined by the following equality in
`L_X(Y)`:

```text
L_µ^{(g, g′)}(m, m′) · µ(g, g′) = µ(m · g, m′ · g′),
```

that is, if we denote by `×` (instead of `µ`) the group law of `L_X` and `Ad` the "adjoint action" of `X⁺` on `L′_X`
(which factors through `X₀` and is induced by the adjoint action of `X₀` on `ω¹_{X₀/S₀}`), one obtains that

```text
L_µ^{(g, g′)}(m, m′) × g × g′ = m × g × m′ × g′ = (m × Ad(g)(m′)) × g × g′
```

hence finally `L_P^{(x, x′)}(m, m′) = m × Ad(g)(m′)`. We therefore obtain:

**Proposition 0.8.** *Let `P : X ×_S X → X` be an `S`-morphism such that `P_J` endows `X_J` with a structure of
`S_J`-group. Denote by `×` the group law of `L′_X` and by `(m, x) ↦ m · x` the morphism `L′_X ×_S X → X` defining the
action of `L′_X` on `X`, and let `Ad : X⁺ → Aut_{S-gr.}(L′_X)` be the "adjoint action" of `X⁺` on `L′_X` (which is
induced by the adjoint action of `X₀` on `ω¹_{X₀/S₀}`). Then, for every `S′ → S` and `x, x′ ∈ X(S′)`,
`m, m′ ∈ L′_X(S′)`, one has:*

```text
P(m · x, m′ · x′) = (m × Ad(p_X(x))(m′)) · P(x, x′).        (0.8.1)
```

*If `X` is an `S`-group, we shall denote by `∗` its law, `e` its unit section, and `i` the `S`-morphism defined by:*

```text
i(m) = m · e ,
```

*for every `S′ → S` and `m ∈ L′_X(S′)`.*

<!-- original page 96 -->

**Corollary 0.9.** *Let `X` be an `S`-group. Then `X⁺` is naturally endowed with a structure of `S`-group, and `p_X` is
a morphism of `S`-groups. Moreover, the `S`-morphism*

<!-- label: III.III.0.9 -->

```text
i : L′_X ──► X,    m ↦ m · e
```

*is an isomorphism of `S`-groups from `L′_X` onto `Ker(p_X)`, and one has, for all `S′ → S`, `x′ ∈ X(S′)`,
`m ∈ L′_X(S′)`:*

```text
m · x′ = (m · e) ∗ x′ = i(m) ∗ x′ .                  (0.9.1)
```

The first two assertions have already been proved in 0.1.2. Since `X` is formally principal homogeneous over `X⁺` under
`L_X = L′_X ×_S X⁺`, the morphism `i` is indeed an isomorphism of `S`-functors from `L′_X` onto the kernel of `p_X`. The
fact that `i` is a morphism of groups and the formula (0.9.1) follow from formula (0.8.1) applied respectively to
`x = x′ = e`, and to `x = e`, `m′ = 1`.

**Corollary 0.10.** *Let `X` be an `S`-group. With the preceding notations, for every `S′ → S` and all `x ∈ X(S′)` and
`m′ ∈ L′_X(S′)`, one has*

<!-- label: III.III.0.10 -->

```text
x ∗ i(m′) ∗ x⁻¹ = i(Ad(p_X(x))(m′)) .                 (0.10.1)
```

This follows from the equality `i(m′) ∗ x⁻¹ = m′ · x⁻¹` and from (0.8.1) applied to `m = 1` and `x′ = x⁻¹`.

When `X` is an `S`-group, we have therefore explicitly determined the kernel of `X → X⁺` and the action of the inner
automorphisms of `X` on this kernel. We shall now see that one can do the same for certain `S`-group functors not
necessarily representable. One case will be useful to us, namely that of the `Aut` functors (I, 1.7). Let us state at
once:

**Proposition 0.11.** *Let `E` be an `S`-scheme. Denote `X = Aut_S(E)`. The kernel of the morphism of `S`-group
functors*

<!-- label: III.III.0.11 -->

```text
p_X : X ──► X⁺
```

*is canonically identified with the `S`-functor in commutative groups `L′_X` defined by*

```text
Hom_S(Y, L′_X) = Hom_{O_{E₀ ×_{S₀} Y₀}}(Ω¹_{E₀/S₀} ⊗_{O_{S₀}} O_{Y₀}, J · O_{E ×_S Y}),
```

*where `Y` denotes a variable `S`-scheme.*

Indeed, if `Y` is a variable `S`-scheme, one has `Hom_S(Y, X) = Aut_Y(E ×_S Y)`, and

```text
Hom_S(Y, X⁺) = Hom_S(Y_J, X) = Aut_{Y_J}(E ×_S Y_J) = Aut_{Y_J}((E ×_S Y) ×_Y Y_J).
```

<!-- original page 97 -->

Applying 0.7 b) to the `Y`-scheme `E ×_S Y`, one obtains an isomorphism of groups:

```text
Hom_S(Y, L′_X) ≃ Ker(Hom_S(Y, X) ──► Hom_S(Y, X⁺)),
```

an isomorphism that one verifies easily to be functorial in the `S`-scheme `Y`. One thus obtains an isomorphism of
`S`-groups

```text
L′_X ≃ Ker(X ──► X⁺),
```

which completes the proof of Proposition 0.11.

**Corollary 0.12.**[^N.D.E-III-29] *We keep the notations of 0.11: `E` is an `S`-scheme and `X = Aut_S(E)`. One has a
natural action `f` of `X` on `L′_X` defined as follows. For every `S`-scheme `Y`, one has*

<!-- label: III.III.0.12 -->

```text
Hom_S(Y, X) = Aut_Y(E ×_S Y)
and    Hom_S(Y, L′_X) = Hom_{O_{E₀ ×_{S₀} Y₀}}(Ω¹_{E₀ ×_{S₀} Y₀ / Y₀}, J · O_{E ×_S Y})
```

*(N. B. `Ω¹_{E₀/S₀} ⊗_{S₀} O_{Y₀} ≃ Ω¹_{E₀ ×_{S₀} Y₀ / Y₀}`, cf. EGA IV₄, 16.4.5); the first group acts on the second by
transport of structure and this action is indeed functorial in `Y`. One then has the formula:*

```text
x · i(m) · x⁻¹ = i(f(x) m),                              (0.12.1)
```

*for every `Y → S` and all `x ∈ Hom_S(Y, X)`, `m ∈ Hom_S(Y, L′_X)`.*

Indeed, this follows from 0.7 c) applied to the `Y`-scheme `E ×_S Y`.

**Reminder 0.13.** *The direct image of a quasi-coherent module by a morphism of finite presentation is quasi-coherent.
Under the same conditions, the formation of the direct image commutes with flat base change: in the situation*

<!-- label: III.III.0.13 -->

```text
T ◄────g′──── T′ = T ×_S S′
│                  │
f                  f′
▼      g           ▼
S ◄──────────── S′ ,
```

<!-- original page 98 -->

*if one supposes `f` (and therefore `f′`) of finite presentation and `g` (and therefore `g′`) flat, one has for every
quasi-coherent `O_T`-module `F`*

```text
f_*(F) ⊗_{O_S} O_{S′} = f′_*(F ⊗_{O_S} O_{S′}),
```

*where, more elegantly,*

```text
g*(f_*(F)) = f′_*(g′*(F)).
```

These two facts hold more generally for a quasi-compact and quasi-separated morphism `f`, cf. (EGA I, 9.2.1) and (EGA
III₁, 1.4.15) in the quasi-compact separated case (taking into account EGA III₂, Err_III 25) and (EGA IV₁, 1.7.4 and
1.7.21).

**Remark 0.14.**[^N.D.E-III-30] *Resume the notations of 0.11: let `E` be an `S`-scheme, `X = Aut_S(E)` and `L′_X` the
`S`-functor in commutative groups defined by:*

<!-- label: III.III.0.14 -->

```text
L′_X(Y) = Hom_{O_{E₀ ×_{S₀} Y₀}}(Ω¹_{E₀/S₀} ⊗_{O_{S₀}} O_{Y₀}, J · O_{E ×_S Y})
         = Hom_{O_{E ×_S Y}}(Ω¹_{E/S} ⊗_{O_S} O_Y, J · O_{E ×_S Y})
         = Γ(E ×_S Y, Hom_{O_{E ×_S Y}}(Ω¹_{E/S} ⊗_{O_S} O_Y, J · O_{E ×_S Y})).
```

Suppose `Y` flat over `S`; then one has isomorphisms:

```text
J · O_{E ×_S Y} ←─∼─ (J · O_E) ⊗_{O_S} O_Y ─∼→ (J · O_E) ⊗_{O_{S₀}} O_{Y₀} .
```

Suppose moreover `E` of finite presentation over `S`; then `Ω¹_{E/S}` is an `O_E`-module of finite presentation (cf. EGA
IV₄, 16.4.22), and hence, by (EGA 0_I, 6.7.6),

```text
Hom_{O_{E ×_S Y}}(Ω¹_{E/S} ⊗_{O_S} O_Y, (J · O_E) ⊗_{O_S} O_Y) ≃ Hom_{O_E}(Ω¹_{E/S}, J · O_E) ⊗_{O_S} O_Y .
```

Denote by `π : E → S` and `g : Y → S` the structural morphisms; applying 0.13 to the diagram

```text
E ◄────g′──── E ×_S Y
│                 │
π                 π′
▼      g          ▼
S ◄────────────── Y ,
```

and to the `O_E`-module `F = Hom_{O_E}(Ω¹_{E/S}, J · O_E)`, one obtains

```text
Γ(E ×_S Y, g′*F) = Γ(Y, π′_* g′* F) = Γ(Y, g* π_* F) = W(π_* F)(Y).
```

<!-- original page 99 -->

We have therefore shown that, if `E` is of finite presentation over `S`, one has

```text
L′_X = W(π_* Hom_{O_E}(Ω¹_{E/S}, J · O_E))                        (0.14.1)
```

on the category of `S`-schemes flat over `S`. Note moreover that the module of which we take the `W` is quasi-coherent,
by (EGA I, 9.1.1 and 9.2.1).

[^N.D.E-III-31] Denote by `L₀` the `S₀`-functor

```text
W(π_{0*} Hom_{O_{E₀}}(Ω¹_{E₀/S₀}, J · O_E)).
```

Then, returning to the definition of `L′_X(Y)` and taking into account the isomorphism

```text
J · O_{E ×_S Y} ≃ (J · O_E) ⊗_{O_{S₀}} O_{Y₀},
```

one obtains, by arguing as above, that

```text
L′_X(Y) = L₀(Y₀) = L₀(Y ×_S S₀) = ∏_{S₀/S} L₀(Y).
```

Hence, on the category of `S`-schemes flat over `S`, one has:

```text
L′_X = ∏_{S₀/S} W(π_{0*} Hom_{O_{E₀}}(Ω¹_{E₀/S₀}, J · O_E)).
```

It is not obvious that the action of `X` on `L′_X` defined in 0.12 comes from an action of `X₀ = Aut_{S₀}(E₀)` on `L₀`;
this is however the case when, moreover, `E` is flat over `S`.

<!-- original page 100 -->

Indeed, in this case one has canonical isomorphisms:

```text
J · O_E ≃ J ⊗_{O_S} O_E ≃ J ⊗_{O_{S₀}} O_{E₀}.
```

```text
L₀ ≃ W(π_{0*} Hom_{O_{E₀}}(Ω¹_{E₀/S₀}, J ⊗_{O_{S₀}} O_{E₀})),
```

```text
L′_X = ∏_{S₀/S} W(π_{0*} Hom_{O_{E₀}}(Ω¹_{E₀/S₀}, J ⊗_{O_{S₀}} O_{E₀})).        (0.14.2)
```

Then, for every `S₀`-scheme `T`, one has

```text
L₀(T) ≃ Hom_{O_{E₀ ×_{S₀} T}}(Ω¹_{E₀ ×_{S₀} T / T}, J ⊗_{O_{S₀}} O_{E₀ ×_{S₀} T})
```

and `Hom_{S₀}(T, X₀) = Aut_T(E₀ ×_{S₀} T)` acts by transport of structure on `L₀(T)`, functorially in `T`; finally, for
every `S`-scheme `Y` flat over `S`, the action by transport of structure of `Hom_S(Y, X) = Aut_Y(E ×_S Y)` on
`L′_X(Y) = L₀(Y₀)` factors through `Aut_{Y₀}(E₀ ×_{S₀} Y₀)`.

Let us finally extract from (SGA 1, III) the following two propositions.

**Proposition 0.15.** *(SGA 1, III, 6.8)[^N.D.E-III-32] For every `S_J`-scheme `Y` smooth over `S_J` and affine, there
exists an `S`-scheme `X` smooth over `S` such that `X ×_S S_J ≃ Y`, and such an `X` is unique up to (non-unique)
isomorphism.*

<!-- label: III.III.0.15 -->

**Proposition 0.16.** *(SGA 1, III, 5.5)[^N.D.E-III-33] Let `X` be an `S`-scheme smooth over `S`. For every affine
`S`-scheme `Y`, the canonical map*

<!-- label: III.III.0.16 -->

```text
p_X(Y) : Hom_S(Y, X) ──► Hom_S(Y, X⁺) = Hom_{S_J}(Y_J, X_J)
```

*is surjective.*

**Corollary 0.17.** *Let `E` be an `S`-scheme smooth over `S` and affine; denote `X = Aut_S(E)`. For every affine
`S`-scheme `Y`, the canonical map*

<!-- label: III.III.0.17 -->

```text
Aut_Y(E ×_S Y) = Hom_S(Y, X) ──► Hom_S(Y, X⁺) = Aut_{Y_J}(E_J ×_{S_J} Y_J)
```

*is surjective.*

Indeed, `Y ×_S E` is affine over `Y`, itself affine, so affine. Applying 0.16, one deduces that every `S_J`-morphism
`Y_J ×_{S_J} E_J → E_J` extends to an `S`-morphism `Y ×_S E → E`. [^N.D.E-III-34] In other words, every
`Y_J`-endomorphism of `Y_J ×_{S_J} E_J` lifts to a `Y`-endomorphism of `Y ×_S E`. Then, 0.7 a) shows that every
`Y_J`-automorphism of `Y_J ×_{S_J} E_J` lifts to a `Y`-automorphism of `Y ×_S E`, which is the announced property.

## 1. Extensions and cohomology

<!-- label: III.III.1 -->

<!-- original page 101 -->

### 1.1.

<!-- label: III.III.1.1 -->

Let `C` be a category stable under fibered products.[^N.D.E-III-35] Let `S` be an object of `C`, `G` an (representable)
`S`-group, and `F` an `S`-functor in commutative groups on which `G` acts. We defined in (I, 5.1) the cohomology groups
`Hⁿ(G, F)`. Recall that these are the homology groups of a complex denoted `C∗(G, F)` where, denoting
`(G/S)ⁿ = G ×_S · · · ×_S G` (`n` factors),

```text
Cⁿ(G, F) = Hom_S((G/S)ⁿ, F).
```

Since `G`, and hence the `(G/S)ⁿ`, are representable, one has also

```text
Cⁿ(G, F) = F((G/S)ⁿ);
```

from this, and from the definition of the boundary operator, one sees that the complex `C∗(G, F)` depends only on the
restriction of `F` to the full subcategory of `C/S` whose objects are the cartesian powers of `G` over `S`.
Consequently, one has the:

**Lemma 1.1.1.** *Let `C` be a category stable under fibered products,[^N.D.E-III-35] `S` an object of `C`, `G` a
representable `S`-group. Denote by `C(G)` the full subcategory of `C/S` whose objects are the cartesian powers of `G`
over `S`. Let `F` and `F′` be two `S`-functors in commutative groups on which `G` acts. If `F` and `F′` have the same
restriction to `C(G)`, one has a canonical isomorphism*

<!-- label: III.III.1.1.1 -->

```text
H∗(G, F) ──∼──► H∗(G, F′).
```

### 1.1.2. Cohomology and restriction of scalars.

<!-- label: III.III.1.1.2 -->

[^N.D.E-III-36] Let us state another comparison result. Let now `T → S` be a morphism in `C`. If `F` is a `T`-functor in
commutative groups, then the functor obtained by "restriction of scalars" (cf. Exp. II, 1)

```text
F₁ = ∏_{T/S} F
```

is an `S`-functor in commutative groups and one has a morphism of `S`-group functors

```text
u : ∏_{T/S} Aut_{T-gr.}(F) ──► Aut_{S-gr.}(F₁) .[^N.D.E-III-37]
```

Let now `G` be an `S`-group functor and let

```text
G_T ──► Aut_{T-gr.}(F)
```

be an action of `G_T` on `F`. By definition of the functor `∏_{T/S}`, one deduces a morphism of `S`-group functors

```text
G ──► ∏_{T/S} Aut_{T-gr.}(F)
```

whence, by composition with `u`, an action of `G` on `F₁ = ∏_{T/S} F`.[^N.D.E-III-38]

<!-- original page 102 -->

**Lemma 1.1.2.** *Under the preceding conditions, one has a canonical isomorphism*

<!-- label: III.III.1.1.2 -->

```text
H∗(G, ∏_{T/S} F) ≃ H∗(G_T, F).
```

Indeed, by the definition of cohomology, the standard complexes are canonically isomorphic.

### 1.2. Lifting of group morphisms.

<!-- label: III.III.1.2 -->

[^N.D.E-III-39] Following the general principles, we lay down the following definition:

**Definition 1.2.1.** *Let `1 → M ──u──► E ──v──► G` be a sequence of morphisms of `Ĉ`-groups. We say that it is
**exact** if the following equivalent conditions are verified:*

<!-- label: III.III.1.2.1 -->

*(i) for every `S ∈ Ob C`, the following sequence of ordinary groups is exact:*

```text
1  ──►  M(S) ──u(S)──► E(S) ──v(S)──► G(S)
```

*(ii) for every object `H` of `Ĉ`, the following sequence of ordinary groups is exact:*

```text
1  ──►  Hom(H, M) ──u(H)──► Hom(H, E) ──v(H)──► Hom(H, G)
```

Taking in particular `H = G` in (ii), one sees that the set of sections of `v` (not respecting *a priori* the group
structures) is empty or principal homogeneous under `Hom(G, M)`. Suppose it is non-empty; so let

```text
s : G ──► E
```

be a section of `v`. Then for every `S ∈ Ob C` and every `x ∈ G(S)`, the element `s(x)` of `E(S)` defines an inner
automorphism of `E_S` which normalizes `M_S` (more correctly, the image of `M_S` by `u_S`), hence an automorphism of
`M_S`.

<!-- original page 103 -->

**Scholie 1.2.1.1.**[^N.D.E-III-40] *If `M` is commutative, one sees "set-theoretically" that this automorphism does not
depend on the chosen section, but only on `x`, and depends multiplicatively on it. In summary, to every exact sequence*

<!-- label: III.III.1.2.1.1 -->

```text
(E)     1  ──►  M  ──u──►  E  ──v──►  G
```

*such that `M` is commutative and that `v` admits a section, is associated a morphism of `Ĉ`-groups*

```text
G ──► Aut_{Ĉ-gr.}(M)
```

*which is called the **action of `G` on `M` defined by the extension `(E)`**.*

**Definition 1.2.1.2.** *We saw in (I, 2.3.7) that `v` admits a section which is a morphism of `Ĉ`-groups if and only if
the extension `(E)` is isomorphic ("as an extension") to the semidirect product of `M` by `G` relative to the preceding
action. Such a section of `v` will be called a **section of the extension `(E)`**, or simply a **section of `(E)`**.*

<!-- label: III.III.1.2.1.2 -->

*If `s` is a section of `(E)` and if `m ∈ Γ(M) ≃ Ker(Γ(E) → Γ(G))` (for the definition of `Γ`, see I, 1.2), then the
morphism `G → E` defined by[^N.D.E-III-41]*

```text
x ↦ u(m) s(x) u(m)⁻¹
```

*is also a section of `(E)`, said to be **deduced from `s` by the inner automorphism defined by `m`** (or by `u(m)`).*

**Lemma 1.2.2.** *Let `(E) : 1 → M ──u──► E ──v──► G` be an exact sequence of `Ĉ`-groups such that `M` is commutative
and `v` admits a section. Let `G` act on `M` in the manner defined by `(E)`.*

<!-- label: III.III.1.2.2 -->

*(i) The extension `(E)` canonically defines a class `c(E) ∈ H²(G, M)` whose vanishing is necessary and sufficient for
the existence of a section of `(E)`.*

<!-- original page 104 -->

*(ii) If `c(E) = 0`, the set of sections of `(E)` is principal homogeneous under the group `Z¹(G, M)`, and the set of
sections of `(E)` modulo the action of the inner automorphisms defined by the elements of `Γ(M)` is principal
homogeneous under the group `H¹(G, M)`.*

*(iii)[^N.D.E-III-42] Let `s` be a section of `(E)`; the set of conjugates of `s` by the inner automorphisms defined by
`Γ(M)` is in bijection with `Γ(M)/H⁰(G, M)`.*

*Proof.* It proceeds exactly as in the case of ordinary groups, the fact that one starts from a section of `v` ensuring
the functoriality of the set-theoretic computations. Let us briefly indicate the principal steps.

**a)** To each section `s` of `v`, one associates the morphism

```text
Ds : G × G ──► M,
```

defined set-theoretically by

```text
u(Ds(x, y)) = s(xy) s(y)⁻¹ s(x)⁻¹.
```

One shows that `Ds` is a 2-cocycle by the following computation.[^N.D.E-III-43] By the definition of the differential of
the standard complex (I, 5.1), one has:

```text
(∂² Ds)(x, y, z) = (s(x) Ds(y, z) s(x)⁻¹) · Ds(x, y)⁻¹ · Ds(xy, z)⁻¹ · Ds(x, yz);
```

it suffices to substitute the definition of `Ds` into this formula to find (without using any commutativity)
`Ds ∈ Z²(G, M)`.

**b)** If `s` and `s′` are two sections of `v`, there exists `f : G → M` such that `s(x) = f(x) s′(x)`. One then has

```text
Ds′(x, y) = f⁻¹(xy) Ds(x, y) s(x) f(y) s(x)⁻¹ f(x),
          = Ds(x, y) · f⁻¹(xy) · (s(x) f(y) s(x)⁻¹) · f(x),
```

<!-- original page 105 -->

i.e.

```text
Ds′ = Ds · ∂¹ f.
```

[^N.D.E-III-44] This shows that the class of `Ds` in `H²(G, M)` does not depend on the chosen section `s` of `v`; it is
the class `c(E)` of the extension `(E)`.

**c)** Let `s` and `s′` be two sections of `v` and let `m ∈ Γ(M)`. Then, the equality `s(x) = m⁻¹ s′(x) m` (for every
`x ∈ G(S)`, `S ∈ Ob C`) is equivalent to

```text
s(x) = m⁻¹ s′(x) m s′(x)⁻¹ s′(x),   i.e.   s = ∂⁰ m · s′ .
```

In particular, the stabilizer of `s` in `Γ(M)` is the subgroup of `m ∈ Γ(M)` such that `∂⁰ m = e_M`, i.e. the subgroup
`H⁰(G, M)`. This already proves (iii).

**d)** The reasoning is now habitual.[^N.D.E-III-45] Let `s₀` be an arbitrary section of `v`; there exists a section
`s`, necessarily of the form `s = f · s₀`, which is a morphism of groups, i.e. which satisfies `Ds = 0`, if and only if
`(Ds₀)⁻¹ = ∂¹ f`, i.e., if and only if the class `c(E)` is zero. This proves (i).

In this case, the set of sections of `(E)` consists of the sections `s′ = h · s`, where `h : G → M` satisfies
`∂¹ h = 0`, i.e. `h ∈ Z¹(G, M)`. Moreover, by point c), two such sections `h₁ · s` and `h₂ · s` are conjugate under
`Γ(M)` if and only if `h₁` and `h₂` have the same image in `H¹(G, M)`. This proves (ii).

Let still

```text
(E)     1  ──►  M  ──u──►  E  ──v──►  G
```

be an exact sequence of `Ĉ`-groups with `M` commutative. Let

```text
f : H ──► G
```

be a morphism of `Ĉ`-groups. Consider `E_f = H ×_G E`; it is a `Ĉ`-group and the projection `v_f : E_f → H` is a
morphism of `Ĉ`-groups. Likewise for `e_f : E_f → E`. On the other hand, if one sends `M` into `E` via `u` and into `H`
via the unit morphism, one defines a morphism of `Ĉ`-groups `u_f : M → E_f`. We have thus constructed a commutative
diagram of `Ĉ`-groups:

```text
(E)     1  ──►  M  ──u──►  E   ──v──►  G
                ║          ▲           ▲
                id        e_f          f
                           │           │
                          u_f          v_f
(E_f)   1  ──►  M  ─────►  E_f  ─────► H .
```

One has immediately:

<!-- original page 106 -->

**Lemma 1.2.3.** *(i) The sequence `(E_f)` is exact.*

<!-- label: III.III.1.2.3 -->

*(ii) The map `s ↦ e_f ∘ s = f′` realizes a bijective correspondence between the morphisms*

```text
s : H ──► E_f
```

*such that `v_f ∘ s = id` (that is, the sections of `v_f`) and the morphisms*

```text
f′ : H ──► E
```

*such that `v ∘ f′ = f` (that is, the morphisms `f′` "lifting" `f`).*

*(iii) In the preceding correspondence, sections of `(E_f)` and morphisms of groups `f′` lifting `f` correspond.*

Applying Lemma 1.2.2 to the extension `(E_f)` and taking into account 1.2.3, one obtains the following proposition
(which formally contains 1.2.2):

**Proposition 1.2.4.** *Let `(E) : 1 → M → E ──v──► G` be an exact sequence of `Ĉ`-groups with `M` commutative. Let*

<!-- label: III.III.1.2.4 -->

```text
f : H ──► G
```

*be a morphism of `Ĉ`-groups; suppose it lifts to a morphism (not necessarily of groups) `f′ : H → E`. Let `H` act on
`M` by the composite morphism (multiplicative and independent of the choice of `f′`),*

```text
H ──f′──► E ──int──► Aut_{Ĉ-gr.}(M).
```

*(i) The morphism `f` canonically defines a class `c(f) ∈ H²(H, M)` whose vanishing is necessary and sufficient for the
existence of a morphism of `Ĉ`-groups*

```text
f′ : H ──► E
```

*lifting `f`.*

<!-- original page 107 -->

*(ii) If `c(f) = 0`, the set of morphisms of `Ĉ`-groups `f′` lifting `f`, modulo the action of the inner automorphisms
defined by elements of `Γ(M)` (i.e. by elements `m` of `Γ(E)` such that `v(m) = e`), is principal homogeneous under
`H¹(H, M)`.*

*(iii) If `f′ : H → E` is a morphism of groups lifting `f`, the set of transforms of `f′` by the inner automorphisms
defined by the elements of `Γ(M)` is isomorphic to `Γ(M)/Γ(M^H) = Γ(M)/H⁰(H, M)`.*

### 1.3. Extensions of group laws.

<!-- label: III.III.1.3 -->

Consider the following situation: one has a morphism of `Ĉ`

```text
(†)     p : X ──► Y
```

and a commutative `Ĉ`-group `M` acting on `X`, such that `X` is formally principal homogeneous above `Y` under `M_Y`.

If `g : Y → Z` is an arbitrary morphism of `Ĉ`, then `g ∘ p : X → Z` is invariant under `M`: for each `S ∈ Ob C`,
`(g ∘ p)(S)` is invariant under the action of `M(S)` acting on `X(S)`. Conversely, we shall assume the following
condition verified for `n = 1, 2, 3, 4`.

`(+)_n` : Every morphism from `Xⁿ` to `M`, invariant under the action of `Mⁿ` on `Xⁿ`, factors uniquely through
`pⁿ : Xⁿ → Yⁿ` (where the powers `n` denote cartesian powers).

**Lemma 1.3.1.** *(i) If `h` is a morphism from `Y` to `M`, the automorphism `u_h` of `X` defined set-theoretically by
`x ↦ h(p(x)) · x` preserves the fibers of `p` and commutes with the actions of `M` on `X`,[^N.D.E-III-46] i.e. for all
`S ∈ Ob C` and `x ∈ X(S)`, `m ∈ M(S)`, one has*

<!-- label: III.III.1.3.1 -->

```text
p(h(p(x)) · x) = p(x),     m · (h(p(x)) · x) = h(p(m · x)) · (m · x) .
```

*(ii) This construction realizes a bijective correspondence between morphisms from `Y` to `M` and automorphisms of `X`
preserving the fibers of `p` and commuting with the actions of `M`.*

The first part is clear, since `p(m · x) = p(x)` and `M` is commutative.

<!-- original page 108 -->

Conversely, an automorphism `u` of `X` preserving the fibers of `p` is written set-theoretically `x ↦ g(x) · x`, where
`g` is some morphism from `X` to `M`. If `u` commutes with the actions of `M`, the morphism `g` is invariant under
`M`[^N.D.E-III-47] and one concludes by condition `(+)_1`.

We now suppose given in addition a group law on `Y` and an action of `Y` on `M`, that is, a morphism of `Ĉ`-groups:

```text
(‡)     f : Y ──► Aut_{Ĉ-gr.}(M).
```

**Definition 1.3.2.** *A composition law on `X`*

<!-- label: III.III.1.3.2 -->

```text
P : X × X ──► X
```

*is said to be **admissible** if it verifies the following two conditions:*

*(i) `P` lifts the group law of `Y`, i.e. the diagram*

```text
            P
X × X ─────────► X
(p,p)│           │ p
     ▼           ▼
Y × Y ─────────► Y
```

*is commutative.*

*(ii) For every `S ∈ Ob C` and all `x, y ∈ X(S)`, `m, n ∈ M(S)`, one has the following relation:*

```text
(++)     P(m · x, n · y) = m · f(p(x))(n) · P(x, y).
```

**Proposition 1.3.3.** *For a group law `∗` on `X` to be admissible, it is necessary and sufficient that the following
four conditions be satisfied:*

<!-- label: III.III.1.3.3 -->

*(i) `p : X → Y` is a morphism of groups.*

<!-- original page 109 -->

*(ii) The morphism `i : M → X` defined by `i(m) = m · e_X` is an isomorphism of groups from `M` onto `Ker(p)`, that is
to say: one has set-theoretically `(m · e_X) ∗ (n · e_X) = (mn) · e_X`.*

*(iii) One has `m · x = (m · e_X) ∗ x = i(m) ∗ x` for each `m ∈ M(S)`, `x ∈ X(S)`.*

*(iv) The inner automorphisms of `X` act on `Ker(p)` by the set-theoretic formula*

```text
x ∗ i(m) ∗ x⁻¹ = i(f(p(x)) m).
```

The proof is immediate.

**Lemma 1.3.4.**[^N.D.E-III-48] *Let `h` be a morphism `Y → M` and `u_h` the automorphism `x ↦ h(p(x)) · x` of `X` (cf.
1.3.1). Let `P` be an admissible composition law (resp. an admissible group law) on `X` and let `P′` be the composition
law on `X` deduced from `P` by means of `u_h`, i.e. `P′(x, y) = u_h⁻¹(P(u_h(x), u_h(y)))`. Then:*

<!-- label: III.III.1.3.4 -->

*(i) `P′` is an admissible composition law (resp. an admissible group law).*

*(ii) For every `x, y ∈ X(S)` (`S ∈ Ob C`), setting `v = p(x)` and `w = p(y)`, one has*

```text
P′(x, y) = (h(vw)⁻¹ · h(v) · f(v)(h(w))) · P(x, y) = (∂¹ h)(p(x), p(y)) · P(x, y).
```

*Proof.* One has `u_h⁻¹ = u_{h^∨}`, where `h^∨ : Y → M` is defined by `h^∨(y) = h(y)⁻¹`. By 1.3.2 (i) and (ii), one has
`P(h(v) · x, h(w) · y) = h(v) · f(v)(h(w)) · P(x, y)` and `p(P(x, y)) = vw`, whence

```text
P′(x, y) = (h(vw)⁻¹ · h(v) · f(v)(h(w))) · P(x, y) = (∂¹ h)(p(x), p(y)) · P(x, y).
```

It is then immediate that `P′` verifies conditions (i) and (ii) of 1.3.2.

**Definition 1.3.5.** *Two admissible composition laws deduced from one another by the procedure of 1.3.4 are said to be
**equivalent**.[^N.D.E-III-49]*

<!-- label: III.III.1.3.5 -->

<!-- original page 110 -->

**Proposition 1.3.6.** *Suppose there exists an admissible composition law on `X`. Then:*

<!-- label: III.III.1.3.6 -->

*(i) There exists a class `c ∈ H³(Y, M)` (canonically determined), whose vanishing is necessary and sufficient for the
existence of an admissible **associative** composition law on `X`.*

*(ii) If `c = 0`, the set of admissible and associative composition laws (resp. of equivalence classes of admissible and
associative composition laws) on `X` is principal homogeneous under `Z²(Y, M)` (resp. `H²(Y, M)`).*

The proof proceeds in several steps.

**a)** Let `P` be an admissible composition law on `X`. Since `P` lifts the composition law of `Y` which is associative,
there exists a unique morphism `a : X³ → M` such that

```text
(∗)     P(x, P(y, z)) = a(x, y, z) · P(P(x, y), z).
```

By applying conditions 1.3.2 (i) and (ii), one sees at once that `a` is invariant under the action of `M³` on
`X³`,[^N.D.E-III-50] whence, by applying hypothesis `(+)_3`, the following result:

**(1)** There exists a unique morphism `DP : Y³ → M` such that

```text
P(x, P(y, z)) = DP(p(x), p(y), p(z)) · P(P(x, y), z),
```

and `P` is associative if and only if `DP = 0`.

**b)** Compute step by step `P(P(P(x, y), z), t)` by means of the preceding formula. Setting `p(x) = u`, `p(y) = v`,
`p(z) = w`, `p(t) = h`, one obtains[^N.D.E-III-51] the following pentagonal diagram, where an arrow `a ──m──► b` means
that `b = m · a`:

```text
                       P(x, P(y, P(z, t)))
       DP(u,v,wh) ↙                      ↘ f(u)(DP(v,w,h))
                ↙                          ↘
P(P(x, y), P(z, t))                    P(x, P(P(y, z), t))
       │                                       │
   DP(uv,w,h)                             DP(u,vw,h)
       ▼            DP(u,v,w)                  ▼
P(P(P(x, y), z), t) ◄──────────────── P(P(x, P(y, z)), t)
```

so one finds

```text
DP(u, v, w) · DP(u, vw, h) · f(u)(DP(v, w, h)) · DP(u, v, wh)⁻¹ · DP(uv, w, h)⁻¹ = e_M
```

i.e., `∂³ DP(u, v, w, h) = e_M`. As moreover the first member of the preceding formula can be written, by means of `P`
and `a`, as the expression in `(x, y, z, t)` of a certain morphism `X⁴ → M`, it follows from the uniqueness hypothesis
in `(+)_4` that `∂³ DP` and `e_M`, which factor through the same morphism, are equal, hence

**(2)** `DP` is a cocycle, i.e. one has `DP ∈ Z³(Y, M)`.

**c)** If `P` and `P′` are two admissible composition laws on `X`, there exists a unique morphism

```text
b : X² ──► M
```

such that `P′(x, y) = b(x, y) · P(x, y)`. Applying 1.3.2 (ii) to `P` and `P′`, one sees that `b` is invariant under
`M²`, whence, by `(+)_2`:

<!-- original page 111 -->

**(3)** For every pair of admissible composition laws `(P, P′)`, there exists a unique `d(P, P′) : Y² → M` such that

```text
P′(x, y) = d(P, P′)(p(x), p(y)) · P(x, y),
```

and the set of admissible composition laws becomes in this way principal homogeneous under `Hom(Y², M) = C²(Y, M)`.

**d)** Under the preceding conditions, one has the formula:

```text
(4)     DP′ − DP = ∂² d(P, P′).
```

**e)** `P` and `P′` are equivalent if and only if there exists a morphism `h ∈ C¹(Y, M) = Hom(Y, M)` such that
`d(P, P′) = ∂¹ h`; this follows from the definition of equivalence and from 1.3.4 (ii).

**f)** It now only remains to conclude: one seeks a `P′` that is associative, i.e. such that `DP′ = e_M`. Now `DP` is a
cocycle whose class in `H³(Y, M)` does not depend on the chosen admissible composition law `P` (by (3) and (4)). This
class is the desired obstruction `c`. One will be able to choose a `P′` answering the conditions if and only if `c = 0`;
indeed, choosing an arbitrary `P`, one will have to solve, by (1):

```text
0 = DP′ = DP + ∂² d(P, P′),
```

which is possible by (3) and (4) if and only if `c = 0`. The set of associative `P′` is principal homogeneous under
`Z²(Y, M)`, again by (3) and (4). The set of associative `P′` up to equivalence is principal homogeneous under
`H²(Y, M)` by (e).

## 2. Infinitesimal extensions of a morphism of group schemes

<!-- label: III.III.2 -->

<!-- original page 112 -->

Resume the notations of § 0. Let `Y` and `X` be two `S`-group functors. Let `M` be the kernel of the morphism of groups
`p_X : X → X⁺`. One thus has an exact sequence of `S`-group functors

```text
1 ──► M ──► X ──p_X──► X⁺ .
```

By definition of `X⁺`, one has isomorphisms

```text
Hom_S(Y, X⁺)       ──∼──► Hom_{S_J}(Y_J, X_J)
Hom_{S-gr.}(Y, X⁺) ──∼──► Hom_{S_J-gr.}(Y_J, X_J),
```

and the morphism

```text
Hom_S(Y, p_X) : Hom_S(Y, X) ──► Hom_S(Y, X⁺)
```

associates to an `S`-morphism `f : Y → X` the `S`-morphism `f⁺ : Y → X⁺` corresponding by the preceding isomorphisms to
the `S_J`-morphism `f_J : Y_J → X_J` obtained by base change from `f`. If `M` is commutative, one can apply to this
situation Proposition 1.2.4.

### 2.0.

<!-- label: III.III.2.0 -->

[^N.D.E-III-52] In what follows, we shall be interested in the following case: `Y` is flat over `S`, and `X` is an
`S`-group functor of one of the following two species:

**a)** `X` is an `S`-group scheme,

**b)** `X = Aut_S(E)` where `E` is an `S`-scheme, of finite presentation over `S`.

Denote by `(Flat)/S` the category of `S`-schemes flat over `S`. In case (a) (resp. (b)), the `S`-group functor
`M = Ker(X → X⁺)`, its restriction `L` to `(Flat)/S`, and the actions of the inner automorphisms of `X` on `M`, have
been computed in 0.9, 0.5, and 0.10 (resp. 0.11, 0.14, and 0.12). That is to say, in case (a), let `L₀` be the
`S₀`-functor in commutative groups defined by: for every `S₀`-scheme `T₀`,

```text
Hom_{S₀}(T₀, L₀) = Hom_{O_{T₀}}(ω¹_{X₀/S₀} ⊗_{O_{S₀}} O_{T₀}, J ⊗_{O_{S₀}} O_{T₀}),
```

on which `X₀` acts via its adjoint representation in `ω¹_{X₀/S₀}`; then `L = ∏_{S₀/S} L₀`, i.e. for every `S`-scheme
`T`, one has `L(T) = L₀(T ×_S S₀)`.

In case (b), denote by `π` the structural morphism `E → S`; then `L` is the functor in abelian groups on `(Flat)/S`
defined by

```text
Hom_S(T, L) = Γ(T, π_*(Hom_{O_E}(Ω¹_{E/S}, J · O_E)) ⊗_{O_S} O_T),
```

on which `X`, considered as a functor on `(Flat)/S`, acts as we saw in 0.12.

Then, one has an exact sequence of functors in groups on `(Flat)/S`:

```text
(E)     1 ──► L ──► X ──► X⁺ .
```

On the other hand, `Y` being supposed flat over `S`, the groups `Hⁱ(Y, M)` depend, by 1.1.1, only on the restriction `L`
of `M` to `(Flat)/S`. Since `L = ∏_{S₀/S} L₀` in case (a), then by 1.1.2, one has in this case isomorphisms
`Hⁱ(Y, L) ≃ Hⁱ(Y₀, L₀)`.

<!-- original page 113 -->

Then, taking the preceding into account, one deduces from Proposition 1.2.4 the:[^N.D.E-III-53]

**Theorem 2.1.** *Let `S` be a scheme, `I` and `J` two quasi-coherent ideals such that `I ⊃ J` and `I · J = 0`, defining
the closed subschemes `S₀` and `S_J`, and let:*

<!-- label: III.III.2.1 -->

<!-- original page 114 -->

*— `X` an `S`-group functor of type (a) or (b), and `L₀`, `L` as above;*

*— `Y` an `S`-group scheme flat over `S` and `f_J : Y_J → X_J` a morphism of `S_J`-groups.*

*Then:*

*(i) For `f_J` to lift to a morphism of `S`-groups `Y → X`, it is necessary and sufficient that the following two
conditions be satisfied:*

*(i₁) `f_J` lifts to a morphism of `S`-functors `Y → X` (by 1.2.4, this defines an action of `Y` on `L`, which does not
depend on the chosen lift; moreover, in case (a), the action thus obtained of `Y₀` on `L₀` comes from the morphism
`f₀ : Y₀ → X₀` and from "the adjoint action" of `X₀` on `L₀`);*

*(i₂) A certain obstruction `c(f_J)`, defined canonically by `f_J`, vanishes, where `c(f_J)` is a class in `H²(Y, L)`
(`≃ H²(Y₀, L₀)` in case (a)).*

*(ii) If the conditions of (i) are satisfied, the set `E` of morphisms of `S`-group functors `Y → X` extending `f_J` is
principal homogeneous under `Z¹(Y, L)` (`≃ Z¹(Y₀, L₀)` in case (a)), and `E` modulo the action of the inner
automorphisms of `X` defined by the sections of `X` over `S` inducing the unit section of `X_J` over `S_J`, is principal
homogeneous under `H¹(Y, L)` (`≃ H¹(Y₀, L₀)` in case (a)).*

*(iii) If `f : Y → X` is a morphism of `S`-group functors extending `f_J`, the set of morphisms `Y → X` transforms of
`f` by the inner automorphisms defined by the sections of `X` over `S` inducing the unit section of `X_J` over `S_J` is
isomorphic to `Γ(L)/H⁰(Y, L)` (`≃ Γ(L₀)/H⁰(Y₀, L₀)` in case (a)).*

**Remark 2.1.1.**[^N.D.E-III-54] *If `f, f′ : Y → X` are morphisms of `S`-group functors extending `f_J`, one therefore
obtains a cocycle `d(f, f′) ∈ Z¹(Y, L)` (`≃ Z¹(Y₀, L₀)` in case (a)), such that*

<!-- label: III.III.2.1.1 -->

```text
(∗)     f′ = d(f, f′) · f .[^N.D.E-III-55]
```

*We shall denote by `d̄(f, f′)` the image of `d(f, f′)` in `H¹(Y, L)` (`≃ H¹(Y₀, L₀)` in case (a)).*

<!-- original page 115 -->

**Remark 2.2.** *We keep the preceding notations; in particular, `Y` is flat over `S`. In case (b), `L` is, by (0.14.1),
the restriction to `(Flat)/S` of the functor*

<!-- label: III.III.2.2 -->

```text
W(π_*(Hom_{O_E}(Ω¹_{E/S}, J · O_E))),
```

*where `π : E → S` is the structural morphism. In case (a), suppose moreover that `X` is locally of finite presentation
over `S`; then by (0.6.1), `L` is the restriction to `(Flat)/S` of the functor*

```text
∏_{S₀/S} W(Hom_{O_{S₀}}(ω¹_{X₀/S₀}, J)).
```

In both cases, the module of which we take the `W` is quasi-coherent, by (EGA I, 9.1.1). Suppose moreover `Y` affine
over `S`.[^N.D.E-III-56] Then, by (I, 5.3), one obtains:

**a)** `Hⁱ(Y, L) = Hⁱ(Y₀, L₀) = Hⁱ(Y₀, Hom_{O_{S₀}}(ω¹_{X₀/S₀}, J))`,

**b)** `Hⁱ(Y, L) = Hⁱ(Y, π_*(Hom_{O_E}(Ω¹_{E/S}, J · O_E)))`.

<!-- original page 116 -->

**Remark 2.3.** *1) By 0.16 and 0.17, condition `(i₁)` is automatically verified when `Y` is an affine scheme and*

<!-- label: III.III.2.3 -->

```text
(∗)     {  in case (a), X is smooth over S;
           in case (b), E is smooth and affine over S.
```

*2) Moreover, under these conditions (`Y` always being supposed flat over `S`, cf. 2.0), one can write in case (a), by
2.2 a) and (0.6.2),*

```text
Hⁱ(Y, L) = Hⁱ(Y₀, L₀) = Hⁱ(Y₀, Lie(X₀/S₀) ⊗_{O_{S₀}} J),
```

*[^N.D.E-III-57] and in case (b), by (0.14.2), 1.1.2 and (I, 5.3),*

```text
Hⁱ(Y, L) = Hⁱ(Y₀, π_{0*} Hom_{O_{E₀}}(Ω¹_{E₀/S₀}, J ⊗_{O_{S₀}} O_{E₀})).
```

Let us now state a certain number of corollaries concerning the case where `Y` is an `S`-diagonalizable group (I, 4.4);
one knows then (loc. cit. 5.3.3) that if `S` is affine, `Hⁿ(Y, F) = 0` for `n > 0` and every quasi-coherent `O_S`-module
`F`. First, a particular case:

**Corollary 2.4.** *Let `S` be a scheme and `S₀` a closed subscheme defined by a nilpotent ideal. Let `Y` be a
diagonalizable `S`-group and let:*

<!-- label: III.III.2.4 -->

*a) `X` an `S`-group locally of finite presentation over `S`,*

*b) `X = Aut_S(E)` where `E` is an `S`-scheme locally of finite presentation.*

*Let `f : Y → X` be a morphism of `S`-groups such that the morphism `f₀ : Y₀ → X₀` obtained by base change is the unit
morphism. Then `f` is the unit morphism.*

Indeed, the question is local on `S` and (in (b)) on `E`. We may therefore suppose `S` affine and (in (b)) `E` of finite
presentation over `S`. Now introducing the closed subschemes `Sₙ` of `S` defined by the powers of the ideal defining
`S₀`, one is reduced to the case where `S₀` is defined by an ideal of square zero, and in that case the asserted
statement follows from the theorem, via 2.2.

In the case where one does not necessarily suppose that `f₀` is the unit morphism, one has:

**Corollary 2.5.** *Let `S` and `S₀` be as in 2.4. Suppose moreover `S` affine. Let `Y` be a diagonalizable `S`-group,
`X` an `S`-group functor, and `f₀ : Y₀ → X₀` a morphism of `S₀`-group functors.*

<!-- label: III.III.2.5 -->

*(i)[^N.D.E-III-58]*

<!-- original page 117 -->

*(ii) Suppose that one of the following two properties holds:*

*(a) `X` is an `S`-group smooth over `S`;*

*(b) `X = Aut_S(E)` where `E` is smooth and affine over `S`.*

*Then `f₀` extends to a morphism of `S`-groups `Y → X`; two such extensions are conjugate by an inner automorphism of
`X` defined by a section of `X` over `S` inducing the unit section of `X₀` over `S₀`.*

Introduce the `Sₙ` as above.[^N.D.E-III-59] For (ii), note first that a scheme smooth over `S` is necessarily locally of
finite presentation over `S`; hence, in case (b), `E` being smooth and affine over `S` is necessarily of finite
presentation over `S`, i.e. we are indeed under hypothesis (b) of 2.0.

Then, under the hypotheses of (ii), condition `(i₁)` of 2.1 is automatically verified by 0.16 and 0.17; moreover every
section of `X_{Sₙ}` over `Sₙ` lifts to a section of `X_{Sₙ₊₁}` over `Sₙ₊₁`, by the definition of "smooth over `S`" in
case (a), and by 0.17 in case (b). Consequently, if `f` and `f′` are two lifts of `f₀`, one can suppose step by step
that `fₙ = fₙ′` by lifting the inner automorphism whose existence is asserted by part (ii) of the theorem, which
completes the proof.

By reasoning likewise, taking into account Remark 2.3, one obtains:

**Corollary 2.6.** *Let `S` be a scheme, `I` a nilpotent ideal defining the closed subscheme `S₀`, `Y` an `S`-group flat
over `S` and affine, `X` an `S`-group smooth over `S`.*

<!-- label: III.III.2.6 -->

*(i) If, for every `n ≥ 0`, one has `H²(Y₀, Lie(X₀/S₀) ⊗_{O_{S₀}} Iⁿ⁺¹/Iⁿ⁺²) = 0`, every morphism of `S₀`-groups
`f₀ : Y₀ → X₀` lifts to a morphism of `S`-groups `f : Y → X`.*

*(ii) If, for every `n ≥ 0`, one has `H¹(Y₀, Lie(X₀/S₀) ⊗_{O_{S₀}} Iⁿ⁺¹/Iⁿ⁺²) = 0`, two such lifts are conjugate by an
inner automorphism of `X` defined by a section of `X` over `S` inducing the unit section of `X₀` over `S₀`.*

Now one has the following lemma:

**Lemma 2.7.** *Let `S` be an affine scheme, `G` an affine `S`-group, `F` a quasi-coherent `O_S`-module, `L` a locally
free `O_S`-module. Suppose one has an action of `G` on `F` in the sense of Exposé I, which defines an action of `G` on
`F ⊗_{O_S} L`[^N.D.E-III-60]. Denote by `Λ` the ring of `S`, `L` the `Λ`-module defining `L` (which is therefore a
projective module). One has a canonical isomorphism*

<!-- label: III.III.2.7 -->

<!-- original page 118 -->

```text
H*(G, F ⊗_{O_S} L) ≃ H*(G, F) ⊗_Λ L.
```

[^N.D.E-III-61] Indeed, denote by `A` the `O_S`-algebra `A(G)` and consider the complex `C` of quasi-coherent
`O_S`-modules:

```text
0 ──► F ──► F ⊗_{O_S} A ──► F ⊗_{O_S} A ⊗_{O_S} A ──► · · ·
```

By (I, 5.3), `H*(G, F)` (resp. `H*(G, F ⊗_{O_S} L)`) is the cohomology of the complex `Γ(S, C)` (resp.
`Γ(S, C ⊗_{O_S} L)`). Now, since `S` is affine, one has (cf. EGA I, 1.3.12)

```text
Γ(S, C ⊗_{O_S} L) ≃ Γ(S, C) ⊗_Λ L.
```

Since `L` is a projective `Λ`-module (hence flat), one has also `H*(Γ(S, C) ⊗_Λ L) ≃ H*(Γ(S, C)) ⊗_Λ L`, whence the
announced result.

By using the lemma, one transforms 2.6 into:

**Corollary 2.8.** *Let `S` be an affine scheme, `I` a nilpotent ideal on `S` defining the closed subscheme `S₀`.
Suppose the `Iⁿ⁺¹/Iⁿ⁺²` locally free on `S₀`. Let `Y` be an `S`-group flat over `S` and affine, `X` an `S`-group smooth
over `S`, and `f₀ : Y₀ → X₀` a morphism of `S`-groups.*

<!-- label: III.III.2.8 -->

*(i) If `H²(Y₀, Lie(X₀/S₀)) = 0`, `f₀` lifts to a morphism of `S`-groups `Y → X`.*

*(ii) If `H¹(Y₀, Lie(X₀/S₀)) = 0`, two such lifts are conjugate by an inner automorphism of `X` defined by a section of
`X` over `S` inducing the unit section of `X₀` over `S₀`.*

In particular, taking `Y = X`:

**Corollary 2.9.** *Let `S` and `S₀` be as above. Let `X` be an `S`-group smooth over `S` and affine.*

<!-- label: III.III.2.9 -->

*(i) If `H¹(X₀, Lie(X₀/S₀)) = 0`, every endomorphism of `X` over `S` inducing the identity on `X₀` is the inner
automorphism defined by a section of `X` over `S` inducing the unit section of `X₀` over `S₀`.*

<!-- original page 119 -->

*(ii) If `H²(X₀, Lie(X₀/S₀)) = 0`, every `S₀`-automorphism of `X₀` extends to an `S`-automorphism of
`X`.[^N.D.E-III-62]*

**Remark 2.10.** *The assertions concerning `H¹` have converses by the theorem. Let us signal as an example the
following: if `S = IS₀` is the scheme of dual numbers over `S₀` (II, 2.1) and if `X` is a flat `S`-group such that every
automorphism of `X` over `S` inducing the identity on `S₀` is the inner automorphism defined by a section of `X` over
`S` inducing the unit section of `X₀` over `S₀`, then `H¹(X₀, Lie(X₀/S₀)) = 0`.[^N.D.E-III-63]*

<!-- label: III.III.2.10 -->

**Corollary 2.11.** *Let `S`, `I` and `J` be as in 2.1. Let `Y` be an `S`-group scheme flat over `S`, `X` an `S`-group
scheme, `f : Y → X` a morphism of `S`-groups. The set of morphisms from `Y` to `X` deduced from `f` by conjugation by
elements `x ∈ X(S)` inducing the unit of `X(S_J)` is isomorphic to the quotient*

<!-- label: III.III.2.11 -->

```text
E = Hom_{O_{S₀}}(ω¹_{X₀/S₀}, J) / Hom_{O_{S₀}}(ω¹_{X₀/S₀}, J)^{ad(Y₀)} ,
```

*where the second group consists of the `O_{S₀}`-morphisms `ω¹_{X₀/S₀} → J` which by every base change `S′ → S₀` give
morphisms `ω¹_{X₀/S₀} ⊗_{O_{S₀}} O_{S′} → J ⊗_{O_{S₀}} O_{S′}` invariant under the action of `Y₀(S′)` on the first
factor.*

By 2.1 (iii), one knows that the set sought is isomorphic to `Γ(L₀)/H⁰(Y₀, L₀)`. Now
`Γ(L₀) = Hom_{O_{S₀}}(ω¹_{X₀/S₀}, J)` and `H⁰(Y₀, L₀)` is evidently none other than `Γ(L₀)^{ad(Y₀)}` in the sense of the
preceding statement.

<!-- original page 120 -->

**Corollary 2.12.** *Under the conditions of 2.11, suppose moreover `ω¹_{X₀/S₀}` locally free of finite rank. Then*

<!-- label: III.III.2.12 -->

```text
E ≃ Γ(S₀, Lie(X₀/S₀) ⊗_{O_{S₀}} J) / H⁰(Y₀, Lie(X₀/S₀) ⊗_{O_{S₀}} J).
```

[^N.D.E-III-64] Indeed, if `ω¹_{X₀/S₀}` is locally free of finite rank, one has
`Hom_{O_{S₀}}(ω¹_{X₀/S₀}, J) ≃ Lie(X₀/S₀) ⊗_{O_{S₀}} J`.

**Corollary 2.13.** *Suppose moreover `Y₀` diagonalizable. Then*

<!-- label: III.III.2.13 -->

```text
E ≃ Γ(S₀, Lie(X₀/S₀) ⊗_{O_{S₀}} J) / Γ(S₀, Lie(X₀/S₀)^{ad(Y₀)} ⊗_{O_{S₀}} J)
```

*where `Lie(X₀/S₀)^{ad(Y₀)}` can be constructed as the factor of the decomposition of (I, 4.7.3) corresponding to the
null character of `Y₀`.*

Indeed, if `Y₀ ≃ D_{S₀}(M)`, one has by loc. cit. a decomposition into direct sum:

```text
Lie(X₀/S₀) = Lie(X₀/S₀)₀ ⊕ ⨁_{m ∈ M, m ≠ 0} Lie(X₀/S₀)_m .
```

By tensoring with `J`, one finds an analogous decomposition for `Lie(X₀/S₀) ⊗_{O_{S₀}} J`, whence the relation

```text
H⁰(Y₀, Lie(X₀/S₀) ⊗ J) ≃ Γ(S₀, Lie(X₀/S₀)₀ ⊗_{O_{S₀}} J).
```

**Corollary 2.14.** *Suppose moreover `S₀` affine. Then*

<!-- label: III.III.2.14 -->

```text
E ≃ Γ(S₀, [Lie(X₀/S₀) / Lie(X₀/S₀)^{ad(Y₀)}] ⊗_{O_{S₀}} J).
```

## 3. Infinitesimal extensions of a group scheme

<!-- label: III.III.3 -->

<!-- original page 121 -->

Still in the notation of n° 0 (`S`, `I`, `J`, etc.), let us give ourselves an `S`-scheme `X` and suppose `X_J` endowed
with a group structure. We propose to find the `S`-group structures on `X` inducing on `X_J` the given structure.

From now on, we assume `X` flat over `S`. Let `C` be the category of `S`-schemes flat over `S`. We have therefore
`X ∈ Ob C`. We shall denote by `Y`, resp. `M`, the functor on `C` defined by `X⁺`, resp. `L′_X`. The canonical morphism
`p_X : X → X⁺` defines a morphism of `Ĉ`

```text
p : X ⟶ Y
```

<!-- original page 122 -->

and the action of `L′_X` on `X` in `(Sch)/S` defines an action of `M` on `X` in `Ĉ`. One verifies at once that `X` thus
becomes formally principal homogeneous under `M_Y` above `Y` (cf. 0.2 (i) and 0.4).

The action of `X⁺` on `L′_X` defined in 0.8 (denoted `Ad` in loc. cit.) defines an action denoted `f` of `Y` on `M`. One
knows, on the other hand (0.5), that

```text
Hom_Ĉ(Z, M) ≃ Hom_{S₀}(Z₀, L₀),     Z ∈ Ob C,
```

where `L₀` is the functor defined in 0.5.

**Lemma 3.1.** *(i) Condition `(+)_n` of 1.3 is satisfied for every positive integer `n`.*

<!-- label: III.III.3.1 -->

*(ii) If one makes the `S₀`-group `X₀` act on the `S₀`-functor `L₀` through its adjoint representation, one has a
canonical isomorphism*

```text
H*(X₀, L₀) ≃ H*(Y, M),
```

*(the first cohomology being computed in `(Sch)/S₀`, the second in `C`).*

Both parts of the lemma follow from the relation:

```text
Hom_Ĉ(Y, M) ≃ Hom_{(Sch)/S₀}(X⁺ ×_S S₀, L₀)
            ≃ Hom_{S₀}(X₀, L₀)
            ≃ Hom_Ĉ(X, M),
```

which arises at once from the definition of `M` as a `∏_{S₀/S}`. This relation being more generally satisfied on
replacing `X`, `Y` by `Xₙ`, `Yₙ`, one deduces that every morphism `Xₙ → M` factors in a unique manner through `Yₙ`,
which entails `(+)_n`. One also deduces from it the relation `C*(Y, M) = C*(X₀, L₀)`, which entails (ii).

We may therefore apply the constructions of 1.3. In particular:

**Lemma 3.2.** *Let `P : X ×_S X → X` be a morphism. In order for `P` to induce the group law of `X_J`, it is necessary
and sufficient that `P` be an admissible composition law (cf. 1.3.2) on `X`.*

<!-- label: III.III.3.2 -->

Indeed, in order for `P` to induce the group law of `X_J`, it is necessary and sufficient that `P` lift the group law of
`X⁺`, or equivalently that of `Y`. It therefore only remains to show that every morphism `P` lifting the group law of
`X_J` satisfies the identity `(++)` of 1.3.2 (ii), and this is exactly what was seen in 0.8.

**Proposition 3.3.** *Let `S` be a scheme and `S₀` a closed subscheme defined by a nilpotent ideal. Let `X` be a flat
`S`-scheme, quasi-compact or locally of finite presentation over `S`. Let `P : X ×_S X → X` be a composition law on `X`.
In order for `P` to be a group law, it is necessary and sufficient that the two following conditions be satisfied:*

<!-- label: III.III.3.3 -->

*(i) `P` is associative.*

*(ii) `P` induces on `X₀ = X ×_X S₀` a group law.*

These conditions are obviously necessary. Let us show that they are sufficient. Suppose first that `X → S` has a
section. Since `X(S′)` is then non-empty for each `S′ → S`, it suffices[^N.D.E-III-65] to show that, for every
`x ∈ X(S′)`, the left and right translations by `x` are isomorphisms of `X_{S′}`.[^N.D.E-III-66]

<!-- original page 123 -->

One may evidently suppose `S′ = S`; the translation in question `t` induces on `X₀` a translation `t₀` of `X₀`, which is
therefore an automorphism since `X₀` is a group. One concludes by flatness (SGA 1 III 4.2).[^N.D.E-III-67]

No longer supposing now that `X` has a section over `S`, suppose that there exists an `S′ → S` such that `X_{S′}` has a
section over `S′`. Then `X_{S′}` is an `S′`-group according to what we have just seen; consider its unit section `e′`.
The inverse image of `e′` by `pr_i : S′ ×_S S′ → S′` (`i = 1, 2`) is the unit section of `X_{S′′}` for the group law
inverse image of `P_{S′}` by `pr_i`. But since `P` is "defined over `S`", these two group laws coincide, and therefore
so do their unit sections. One has therefore `pr_1*(e′) = pr_2*(e′)`.

If `S′ → S` is a descent morphism (cf. Exp. IV n° 2), there will exist a section of `X` giving `e′` by base extension,
and we shall be done. Since `X_X` has a section over `X` (the diagonal section), one sees that it now suffices to prove
that `X → S` is a descent morphism. Now it is flat and surjective, and quasi-compact or locally of finite presentation,
hence covering for (fpqc), hence a descent morphism (Exp. IV, n° 6).

**Remark.** *In fact the hypothesis `X → S` quasi-compact or locally of finite presentation is superfluous, by virtue of
the following result which the reader will prove as an exercise on Exposé IV:*

*Under the conditions of the text on `S` and `S₀`, if `X → S` is a flat morphism and `X₀ → S₀` a morphism covering for
(fpqc), then `X → S` is a descent morphism.*

<!-- original page 124 -->

**Lemma 3.4.** *In order for two admissible composition laws on `X` to be equivalent (cf. 1.3.5), it is necessary and
sufficient that they be deduced from one another by an automorphism of `X` over `S` inducing the identity on `X_J`.*

<!-- label: III.III.3.4 -->

Indeed, the morphisms constructed in 1.3.1 are exactly those of the preceding statement (by 0.7).[^N.D.E-III-68]

Taking all the preceding results into account, Proposition 1.3.6 gives:

**Theorem 3.5.** *Let `S` be a scheme, `I` and `J` two ideals on `S` such that `I ⊃ J`, `I · J = 0`, `S₀` and `S_J` the
closed subschemes of `S` which they define. Let `X` be an `S`-scheme flat over `S` (and locally of finite presentation
or quasi-compact over `S`), `X₀` and `X_J` the schemes obtained by base change. Suppose `X_J` endowed with an
`S_J`-group structure and denote by `L₀` the `S₀`-functor in commutative groups defined by the formula*

<!-- label: III.III.3.5 -->

```text
Hom_{S₀}(T, L₀) = Hom_{O_T}(ω¹_{X₀/S₀} ⊗_{O_{S₀}} O_T, J ⊗_{O_{S₀}} O_T)
```

*on which `X₀` acts through its adjoint representation.*

*(i) For there to exist an `S`-group structure on `X` inducing the given structure on `X_J`, it is necessary and
sufficient that the following conditions be satisfied:*

*(i₁) There exists a morphism of `S`-schemes `X ×_S X → X` inducing the group law of `X_J`.*

*(i₂) A certain obstruction class belonging to `H³(X₀, L₀)` (defined canonically by the data of `X` and the group law of
`X_J`) is zero.*

*(ii) If the conditions of (i) are satisfied, the set `E` of group laws on `X` inducing the given law of `X_J` is a
principal homogeneous set under `Z²(X₀, L₀)`, and `E` modulo the `S`-automorphisms of `X` inducing the identity on
`X_J`, is a principal homogeneous set under `H²(X₀, L₀)`.*

<!-- original page 125 -->

[^N.D.E-III-69] Indeed, every morphism of `S`-schemes `f : X ×_S X → X` inducing the group law of `X_J` is, by 3.2, an
admissible composition law on `X`; then, by 1.3.6 (i), the existence of an associative admissible composition law
`P : X ×_S X → X` is equivalent to the vanishing of a certain class `c(f) ∈ H³(X₀, L₀)`, and in this case, by 3.3, `P`
is a group law. This proves (i), and (ii) then follows from 3.3 and 1.3.6 (ii).

**Remark 3.5.1.**[^N.D.E-III-70] *If `μ`, `μ′` are group laws on `X` inducing the given law of `X_J`, one therefore
obtains a cocycle `δ(μ, μ′) ∈ Z²(X₀, L₀)`, the sign convention chosen being that `μ′ = δ(μ, μ′) · μ`, that is, for every
`S′ → S` and `x, y ∈ X(S′)`,*

<!-- label: III.III.3.5.1 -->

```text
μ′(x, y) = δ(μ, μ′)(x₀, y₀) · μ(x, y).
```

[^N.D.E-III-71]

We shall denote by `δ̄(μ, μ′)` the image of `δ(μ, μ′)` in `H²(X₀, L₀)`. Finally, if `X` endowed with the group law `μ`
(resp. `μ′`) is designated simply by `X` (resp. `X′`), one will write `δ(X, X′)` instead of `δ(μ, μ′)`, and likewise for
`δ̄(X, X′)`.

**Remark 3.6.** *Let `X_J` be an `S_J`-scheme smooth over `S_J` and affine. By 0.15, there exists up to isomorphism a
unique `S`-scheme `X`, smooth over `S`, reducing to `X_J`. If `X_J` is endowed with an `S_J`-group structure, it follows
from 0.16 that condition (i₁) is automatically satisfied. Moreover, by 0.6 the definition of `L₀` simplifies and one
obtains:*

<!-- label: III.III.3.6 -->

**Corollary 3.7.** *Let `S`, `I` and `J` be as in 3.1. Let `X_J` be an `S_J`-group smooth over `S_J` and affine.*

<!-- label: III.III.3.7 -->

*(i) The set of `S`-groups smooth over `S` and reducing to `X_J`, up to isomorphism (inducing the identity on `X_J`), is
empty or principal homogeneous under the group*

```text
H²(X₀, Lie(X₀/S₀) ⊗_{O_{S₀}} J).
```

*(ii) There exists an `S`-group smooth over `S` reducing to `X_J` if and only if a certain obstruction in*

```text
H³(X₀, Lie(X₀/S₀) ⊗_{O_{S₀}} J)
```

*is zero.*

One deduces as usual the following corollaries:

**Corollary 3.8.** *Let `S` be a scheme and `S₀` a closed subscheme defined by a nilpotent ideal `I`. Let `X₀` be an
`S₀`-group smooth over `S` and affine.*

<!-- label: III.III.3.8 -->

*(i) If `H²(X₀, Lie(X₀/S₀) ⊗_{O_{S₀}} Iⁿ⁺¹/Iⁿ⁺²) = 0` for every `n ≥ 0`, two `S`-groups smooth over `S` reducing to `X₀`
are isomorphic (by an isomorphism inducing the identity on `X₀`).*

<!-- original page 126 -->

*(ii) If `H³(X₀, Lie(X₀/S₀) ⊗_{O_{S₀}} Iⁿ⁺¹/Iⁿ⁺²) = 0` for every `n ≥ 0`, there exists an `S`-group smooth over `S`,
reducing to `X₀`.*

**Corollary 3.9.** *Let `S` be an affine scheme and `S₀` a closed subscheme defined by a nilpotent ideal `I`. Suppose
the `Iⁿ⁺¹/Iⁿ⁺²` locally free on `S₀`. Let `X₀` be an `S₀`-group smooth and affine over `S₀`.*

<!-- label: III.III.3.9 -->

*(i) If `H²(X₀, Lie(X₀/S₀)) = 0`, two `S`-groups smooth over `S` reducing to `X₀` are isomorphic.*

*(ii) If `H³(X₀, Lie(X₀/S₀)) = 0`, there exists an `S`-group smooth over `S` reducing to `X₀`.*

**Corollary 3.10.** *Let `S₀` be a scheme and `S = IS₀` the scheme of dual numbers over `S₀`. Let `X₀` be an `S₀`-group
smooth over `S₀`. In order for every `S`-group `Y`, smooth over `S`, such that `Y₀` be `S₀`-isomorphic to `X₀`, to be
`S`-isomorphic to `X = X₀ ×_{S₀} S`, it is necessary and sufficient that `H²(X₀, Lie(X₀/S₀)) = 0`.[^N.D.E-III-72]*

<!-- label: III.III.3.10 -->

Indeed, by virtue of 3.5 the set of classes, up to an `S`-group isomorphism "inducing the identity on `X₀`", of such
groups `Y`, is in bijection with `H²(X₀, Lie(X₀/S₀))`; hence the set of classes, up to an arbitrary `S`-group
isomorphism, is in bijection with

```text
H²(X₀, Lie(X₀/S₀))/Γ₀,
```

where

```text
Γ₀ = Aut_{S₀-gr.}(X₀)
```

(which acts in the evident manner on the `H²`). The conclusion follows at once.[^N.D.E-III-73]

## 4. Infinitesimal extensions of closed subgroups

<!-- label: III.III.4 -->

<!-- original page 127 -->

Let us first state a result valid in an arbitrary abelian category.

**Lemma 4.1.** *Let `0 → A′ →^i A →^p A′′ → 0` be an exact sequence, `φ : A′ → Q` a morphism and `π : A′′ → P` an
epimorphism with kernel `C`. Let `E` be the set (up to isomorphism) of quadruples `(B, f, g, h)` such that the sequence*

<!-- label: III.III.4.1 -->

```text
0 ──► Q ──f──► B ──g──► P ──► 0
```

*be exact and the diagram below commutative:*

```text
0 ──► A′ ──i──► A ──p──► A′′ ──► 0
       │        │         │
       φ        h         π
       ↓        ↓         ↓
0 ──► Q ──f──► B ──g──► P  ──► 0.
```

*(i) For `E` to be non-empty, it is necessary and sufficient that the image in `Ext¹(C, Q)` of the element `A` of
`Ext¹(A′′, A′)` be zero.*

*(ii) Under these conditions, `E` is a principal homogeneous set under the abelian group `Hom(C, Q)`.*

Introduce the amalgamated sum `B′ = A ⊔_{A′} Q`. One then has a commutative diagram with exact rows:[^N.D.E-III-74]

```text
0 ──► A′ ──i──► A ──p──► A′′ ──► 0
       │       j│         ║
       φ        ↓         ║
0 ──►  Q  ───► B′ ──────► A′′ ──► 0,
```

<!-- original page 128 -->

and it is clear that the category of solutions of the problem posed is canonically isomorphic to the category of
solutions of the corresponding problem for the sequence

```text
0 ──► Q ──► B′ ──► A′′ ──► 0
```

and the morphisms `id_Q` and `π : A′′ → P`.[^N.D.E-III-75] In this case, the set `E` is in bijection with the set of
subobjects `N` of `B′` such that `B′ → A′′` induces an isomorphism of `N` with the kernel `C` of `A′′ → P`, that is to
say, the set of morphisms `e : C → B′` lifting the canonical morphism `C → A′′`. The abelian group `G = Hom(C, Q)` acts
on `E` by `g · e = g + e` (addition in `Hom(C, B′)`), and if `E ≠ ∅` this makes `E` into a principal homogeneous set
under `G`.

One deduces from this:

**Proposition 4.2.**[^N.D.E-III-76] *Let `S` be a scheme, `S_J` the closed subscheme defined by a quasi-coherent ideal
`J` of square zero, `X` an `S`-scheme, `F` an `O_X`-module, `X_J = X ×_S S_J`, `F_J = F ⊗_{O_S} O_{S_J}`, and
`G_J = F_J / H_J` a quotient module of `F_J`. Suppose given a morphism of `O_{X_J}`-modules*

<!-- label: III.III.4.2 -->

```text
f : J ⊗_{O_{S_J}} G_J ⟶ Q.
```

*Let `E` be the sheaf of sets on `X` defined as follows: for every open `U` of `X`, `E(U)` is the set of quotient
modules `G` of `F|_U`, such that `G/JG = G_J|_U` and there exists an isomorphism*

```text
h : JG ⥲ Q|_U
```

*making the diagram*

```text
                      f|_U
J ⊗_{O_{S_J}} (G_J|_U) ────► Q|_U
       │                    ↗
       can.                h ≃
       ↓                  /
       JG ──────────────
```

<!-- original page 129 -->

*commutative (`h` is then unique, since `J ⊗_{O_{S_J}} (G_J|_U) → JG` is an epimorphism). Then `E` is a sheaf formally
principal homogeneous under the sheaf in commutative groups*

```text
A = Hom_{O_X}(H_J, Q) = Hom_{O_{X_J}}(H_J, Q).
```

*Proof.* If `E(U) = ∅` there is nothing to prove; one may therefore suppose that `E(U)` contains an element `G̃`. Then,
in the diagram below, `h` is an isomorphism and all the arrows are epimorphisms:

```text
                                          f|_U
J ⊗_{O_{S_J}} (F_J|_U) ─► J ⊗_{O_{S_J}} (G_J|_U) ─────► Q|_U
        │                          │                      ↗
        can.                       can.                 h ≃
        ↓                          ↓                    /
        JF|_U  ──────────────►   JG̃   ──────────────────
```

Therefore, the morphism `J ⊗_{O_{S_J}} (F_J|_U) → Q|_U` induces an epimorphism (necessarily unique) `φ : JF|_U → Q|_U`,
and if `G` is an `O_U`-module such that `G/JG = G_J|_U` and one has a commutative diagram with exact rows:

```text
0 ──► JF|_U ─────► F|_U ─────► F_J|_U ──► 0
        │           │            │
        φ           │            π
        ↓     p_J   ↓            ↓
0 ──► Q|_U ─────► G ──────►  G_J|_U ──► 0
```

(where `p_J` is the projection `G → G/JG = G_J|_U`, so that `Q|_U = Ker(p_J) = JG`), then one can identify `G` with a
quotient module of `F|_U`. Consequently, by 4.1 (ii), the set `E(U)` is principal homogeneous under the abelian group

```text
Hom_{O_X}(H_J, Q)(U) = Hom_{O_{X_J}}(H_J, Q)(U).
```

**Proposition 4.3.** *(TDTE IV 5.1) Let `S` be a scheme, `S_J` the closed subscheme defined by a quasi-coherent ideal
`J` of square zero, `X` an `S`-scheme, `F` a quasi-coherent `O_X`-module, `X_J = X ×_S S_J`, `F_J = F ⊗_{O_S} O_{S_J}`.
Let `G_J = F_J / H_J` be a quasi-coherent quotient module of `F_J`, flat over `S_J`.*

<!-- label: III.III.4.3 -->

*For every open `U` of `X`, let `E(U)` be the set of quasi-coherent[^N.D.E-III-77] quotient modules `G` of `F|_U`, flat
over `S`, and such that `G/JG ≃ G_J|_U`. Then the `E(U)` form a sheaf of sets `E` on `X`, which is formally principal
homogeneous under the sheaf in commutative groups*

```text
A = Hom_{O_{X_J}}(H_J, J ⊗_{O_{S_J}} G_J).
```

*Proof.* Denote by `π : X → S` the structural morphism. Let `U` be an open of `X` and `G` an `O_U`-module flat over `S`
and such that `G/JG ≃ G_J|_U`. Then, for every `x ∈ U`, `G_x` is a flat module over the local ring `O_{S,s}` (where
`s = π(x)`), and therefore the morphism

```text
J_s ⊗_{O_{S,s}} (G/JG)_x = J_s ⊗_{O_{S,s}} G̅_x ⟶ (JG)_x
```

is bijective; one has therefore an exact sequence

```text
0 ⟶ J ⊗_{O_S} (G_J|_U) ⟶ G ⟶ G_J|_U ⟶ 0
```

<!-- original page 130 -->

and since `J ⊗_{O_S} (G_J|_U)` and `G_J|_U` are quasi-coherent `O_U`-modules, so is `G` (cf. EGA III, 1.4.17).

Conversely, since one has supposed `G_J` flat over `S_J`, if `G` is a quasi-coherent `O_U`-module such that `G/JG ≃ G_J`
and such that the morphism `J ⊗_{O_{S_J}} G_J → JG` is bijective, then `G` is flat over `S`, by the "fundamental
criterion of flatness" (cf. SGA 1 IV, 5.5[^N.D.E-III-78]).

Consequently, the set `E(U)` considered here coincides with the set considered in 4.2, taking for `f` the identity
morphism of `J ⊗_{O_{S_J}} G_J`, and the conclusion follows therefore from 4.2. QED.

[^N.D.E-III-79] Let us preserve the preceding notation. Let `Y_J` be a closed subscheme of `X_J`, defined by a
quasi-coherent ideal `I_{Y_J}`. We assume `Y_J` flat over `S_J`. Then, applying 4.3 to `F = O_X` and
`G_J = O_{Y_J} = O_{X_J}/I_{Y_J}`, one obtains the following corollary.

**Corollary 4.3.1.** *Let `S, S_J, J, X, X_J, Y_J` and `I_{Y_J}` be as above; one assumes `Y_J` flat over `S_J`. Denote
by `A_J` the sheaf in commutative groups*

<!-- label: III.III.4.3.1 -->

```text
Hom_{O_{X_J}}(I_{Y_J}, J ⊗_{O_{S_J}} O_{Y_J})
```

*on `X_J` and `A = i_*(A_J)`, where `i` is the immersion `X_J ↪ X`.*

*For every open `U` of `X`, let `E(U)` be the set of closed subschemes `Y` of `U`, flat over `S`, such that
`Y ×_S S_J = Y_J ∩ U`. Then `E` is an `A`-pseudo-torsor.*

*If moreover a `Y` exists locally (that is, if every `x ∈ X` has an open neighborhood `U` such that `E(U) ≠ ∅`), then
`E` is an `A`-torsor.* Now one knows (see for example EGA IV₄, 16.5.15) that the `A`-torsors on `X` are parametrized by
the group `H¹(X, A) = H¹(X_J, A_J)`, and that `E` has a global section (i.e. `E(X) ≠ ∅`) if and only if the cohomology
class corresponding to `E` is zero. One thus obtains:

**Corollary 4.4.** *Let `S, S_J, J, X, X_J, Y_J` and `I_{Y_J}` be as above; one assumes `Y_J` flat over `S_J`. Let `E`
be the set of closed subschemes `Y` of `X`, flat over `S`, such that `Y ×_S S_J = Y_J`.*

<!-- label: III.III.4.4 -->

*(i) The set `E` is empty or principal homogeneous under the abelian group*

```text
H⁰(X, A) = H⁰(X_J, A_J) = Hom_{O_{X_J}}(I_{Y_J}, J ⊗_{O_{S_J}} O_{Y_J}).
```

<!-- original page 131 -->

*(ii) For `E` to be non-empty, it is necessary and sufficient that the two following conditions be satisfied:*

*(a) There exists locally on `X` a solution of the problem.*

*(b) A certain obstruction is zero, lying in*

```text
H¹(X_J, Hom_{O_{X_J}}(I_{Y_J}, J ⊗_{O_{S_J}} O_{Y_J})).
```

**Complement 4.4.1.**[^N.D.E-III-80] *Let us keep the notation of 4.4 and suppose that `E` contains an element `Y`.
Denote by `I_Y` the ideal of `O_X` defining `Y`, and `I_{Y_J}` its image in `O_{X_J}`. Then, as was seen in the proof of
4.2, one has a commutative diagram*

<!-- label: III.III.4.4.1 -->

```text
J ⊗_{O_{S_J}} O_{X_J} ──► JO_X
         │                  │
         ↓                  ↓
J ⊗_{O_{S_J}} O_{Y_J} ──≃─► JO_Y
```

*hence an epimorphism of `O_X`-modules `φ : JO_X → J ⊗_{O_{S_J}} O_{Y_J}`; denote by `K` its kernel.* Then, for every
element `Y′` of `E`, the morphism `O_X → O_{Y′}` factors through `O_X/K` (which is the amalgamated sum `B′` of the proof
of Lemma 4.1) and, denoting by `I_{Y′}` the ideal of `Y′` in `O_X`, one has a commutative diagram:

```text
                       0          0
                       │          │
                       ↓          ↓
                  I_{Y′}/K  ──≃──► I_{Y_J}
                       │            │
                       ↓            ↓
0 ──► (JO_X)/K ──► O_X/K ──► O_{X_J} ──► 0
        │            │ ≀         │
        ↓            ↓           ↓
0 ──► J ⊗_{O_{S_J}} O_{Y_J} ──► O_{Y′} ──► O_{Y_J} ──► 0
                       │            │
                       ↓            ↓
                       0            0.
```

Therefore, replacing `X` by the closed subscheme defined by `K`, one reduces to `K = 0`. Then, the datum of `Y′` is
equivalent to that of the sub-`O_X`-module `I_{Y′}` of `O_X`, sending bijectively onto `I_{Y_J}` by the projection
`p : O_X → O_{X_J}`; denote by `f′ : I_{Y_J} ⥲ I_{Y′}` (resp. `f : I_{Y_J} ⥲ I_Y`) the inverse isomorphism. Then
`f′ − f` is an element of

```text
Hom_{O_{X_J}}(I_{Y_J}, J ⊗_{O_{S_J}} O_{Y_J}) = Hom_{O_{X_J}}(I_{Y_J}, JO_Y)
```

which we shall denote `d(Y′, Y)`. (Note that `d(Y, Y′) = −d(Y′, Y)`.)

<!-- original page 132 -->

For our fixed `Y` and variable `Y′`, consider the morphism:

```text
I_{Y′} ⟶ O_X ⟶ O_Y = O_X/I_Y;
```

since the composition with `O_Y → O_{Y_J}` is zero, one knows that it takes values in `JO_Y = J ⊗_{O_{S_J}} O_{Y_J}`.
More precisely, if `V` is an open of `X`, `x′` a section of `I_{Y′}` on `V` and `x_J` its image in `Γ(V, I_{Y_J})`, then

```text
x′ = f′(x_J) = f(x_J) + (f′ − f)(x_J) = f(x_J) + d(Y′, Y)(x_J).
```

Consequently: the morphism `I_{Y′} → JO_Y` is given by `d(Y′, Y)`.

**4.5.0.**[^N.D.E-III-81] Let us keep the notation of 4.3.1 and 4.4 and carry out a certain number of transformations:
`I_{Y_J}/I_{Y_J}²` is a quasi-coherent `O_{X_J}`-module annihilated by `I_{Y_J}`, hence is the direct image of a
quasi-coherent `O_{Y_J}`-module denoted `N_{Y_J/X_J}`, called the *conormal sheaf* to `Y_J` in `X_J`.[^N.D.E-III-82]
Since `J ⊗_{O_{S_J}} O_{Y_J}` is annihilated by `I_{Y_J}`, the sheaf in commutative groups `A_J` of 4.3.1 identifies
with:

```text
Hom_{O_{Y_J}}(I_{Y_J}/I_{Y_J}², J ⊗_{O_{S_J}} O_{Y_J}) = Hom_{O_{Y_J}}(N_{Y_J/X_J}, J ⊗_{O_{S_J}} O_{Y_J}),
```

whence, for every `i ≥ 0`:

```text
Hⁱ(X_J, A_J) = Hⁱ(Y_J, Hom_{O_{Y_J}}(N_{Y_J/X_J}, J ⊗_{O_{S_J}} O_{Y_J})).
```

[^N.D.E-III-83] One can then suppress the hypothesis "`Y` closed", as follows. Let us first note that every open `U_J`
of `X_J` comes by base change from the open subscheme `U` of `X` having the same underlying topological space as `U_J`.
Let now `Y_J` be a closed subscheme of `U_J`, flat over `S_J`, and `I_{Y_J}` the quasi-coherent ideal of `O_{U_J}`
defining `Y_J`. If `Y_J` lifts to a subscheme `Y` of `X`, then `Y`, having the same underlying topological space as
`Y_J`, is a closed subscheme of `U`; consequently, the obstruction to lifting `Y_J` to a subscheme, flat over `S`, of
`X` or of `U` is "the same", it resides in

```text
H¹(Y_J, Hom_{O_{Y_J}}(N_{Y_J/X_J}, J ⊗_{O_{S_J}} O_{Y_J})).
```

Finally, let us return to the notation of n° 0: let `I` be a quasi-coherent ideal of `O_S` such that `J ⊂ I` and
`IJ = 0`, and let `S₀` be the closed subscheme of `S_J` defined by `I`. For every `S`-scheme `Z`, one denotes
`Z_J = Z ×_S S_J` and `Z₀ = Z ×_S S₀`. Then, since `J` is annihilated by `I`, one has, with the notation of 4.4:

```text
J ⊗_{O_{S_J}} O_{Y_J} = J ⊗_{O_{S₀}} O_{Y₀}
Hom_{O_{Y_J}}(N_{Y_J/X_J}, J ⊗_{O_{S_J}} O_{Y_J}) = Hom_{O_{Y₀}}(N_{Y_J/X_J} ⊗_{O_{Y_J}} O_{Y₀}, J ⊗_{O_{S₀}} O_{Y₀}),
```

etc. One thus obtains:

<!-- original page 133 -->

**Proposition 4.5.** *Let `S` be a scheme, `S₀` and `S_J` the closed subschemes defined by the quasi-coherent ideals `I`
and `J`, such that `I ⊃ J` and `I · J = 0`. Let `X` be an `S`-scheme and `Y_J` a subscheme of `X_J`, flat over `S_J`.
Let `A₀` be the `O_{Y₀}`-module defined by*

<!-- label: III.III.4.5 -->

```text
A₀ = Hom_{O_{Y₀}}(N_{Y_J/X_J} ⊗_{O_{Y_J}} O_{Y₀}, J ⊗_{O_{S₀}} O_{Y₀}).
```

*(i) For there to exist a subscheme `Y` of `X`, reducing to `Y_J`, flat over `S`, it is necessary and sufficient that
the following conditions be satisfied:*

*(a) Such a `Y` exists locally on `X`.*

*(b) A certain obstruction in `R¹Γ(Y₀, A₀)` is zero.[^N.D.E-III-84]*

*(ii) Under these conditions, the set of `Y` satisfying the required conditions is principal homogeneous under the
commutative group `Γ(Y₀, A₀)`.*

**Remark 4.5.1.**[^N.D.E-III-85] *It follows from 4.5 (ii) that for every pair `(Y, Y′)` of subschemes[^N.D.E-III-86] of
`X`, flat over `S` and reducing to `Y_J`, one has a "deviation"*

<!-- label: III.III.4.5.1 -->

```text
d(Y′, Y) ∈ Γ(Y₀, A₀) = Hom_{O_{Y₀}}(N_{Y_J/X_J} ⊗_{O_{Y_J}} O_{Y₀}, J ⊗_{O_{S₀}} O_{Y₀});
```

*the sign convention adopted in 4.4.1 being that `d(Y′, Y)` corresponds to the morphism of `O_X`-modules*

```text
I_{Y′} ↪ O_X ⟶ O_Y
```

*(which takes values in `JO_Y ≃ J ⊗_{O_{S₀}} O_{Y₀}` and factors through `I_{Y_J′} = I_{Y_J}` and then through
`N_{Y_J/X_J}`).*

**Remark 4.6.**[^N.D.E-III-87] *If `X` is flat over `S` and if `Y_J` is locally complete intersection in `X_J`, then
condition (a) is always satisfied and every `Y` flat over `S` lifting `Y_J` is then locally complete intersection in
`X`. If moreover `Y₀` is affine, condition (b) is also satisfied.*

<!-- label: III.III.4.6 -->

**Definition 4.6.1.** *(cf. SGA 6, VII 1.1) Let `B` be a commutative ring, `f : E → B` a `B`-linear morphism, where `E`
is a free `B`-module of finite rank `d`, and `I` the ideal `f(E)` (if one chooses a basis of `E`, `f` is given by a
`d`-tuple `(f₁, ..., f_d)` of elements of `B`, and `I` is the ideal generated by the `fᵢ`). The* **Koszul complex**
*`K•(f)` is the graded `B`-module `⋀• E`, equipped with the differential (of degree `−1`):*

<!-- label: III.III.4.6.1 -->

```text
x₁ ∧ ··· ∧ xᵢ ↦ Σⱼ₌₁ⁱ (−1)ʲ⁻¹ f(xⱼ) x₁ ∧ ··· ∧ x̂ⱼ ∧ ··· ∧ xᵢ.
```

<!-- original page 134 -->

One has therefore an augmented chain complex (`B/I` being in degree `−1`):

```text
··· ⟶ ⋀² E ⟶ E ──f──► B ⟶ B/I ⟶ 0
```

which by definition is exact in degree `0`, since `I = f(E)`. One says that `f` is **regular** if `K•(f)` is acyclic in
degrees `> 0`, that is, if the augmented complex above is a resolution of `C = B/I`.

In this case, the proof of SGA 6, VII 1.2 b) shows that the `C`-modules `Iⁿ/Iⁿ⁺¹` (`n ∈ ℕ`) are free, `I/I²` being of
rank `d`.

**Definition 4.6.2.** *(cf. SGA 6, VII 1.4) Let `X` be a scheme, `Y` a subscheme, `U` an open of `X` such that `Y` is a
closed subscheme of `U`, defined by the quasi-coherent ideal `I_Y`.*

<!-- label: III.III.4.6.2 -->

*One says that `Y` is* **locally complete intersection** *in `X` if `Y ↪ X` is a regular immersion in the sense of SGA
6, VII 1.4, that is, if for every `y ∈ Y` there exists an affine open neighborhood `V` of `y` in `U`, a finite free
`O_V`-module `E`, and a regular morphism `f : E → O_V` of image `I_Y|_V`, i.e. such that `K•(f)` be a resolution of
`O_{Y ∩ V}`.*

This implies that the immersion `Y ↪ X` is locally of finite presentation, and, by 4.6.1, that the conormal sheaf
`N_{Y/X} = I_Y/I_Y²` is a finite locally free `O_Y`-module.

**Lemma 4.6.3.**[^N.D.E-III-88] *Let `A` be a ring, `J` an ideal of `A` of square zero, `Ā = A/J`, `B` a flat
`A`-algebra, `E` a free `B`-module of finite rank, `f : E → B` a morphism of `B`-modules. One supposes that the morphism
`ḡ : Ē = E ⊗_A Ā → B̄ = B ⊗_A Ā` induced by `f` is regular and that `B̄/ḡ(Ē)` is flat over `Ā`.*

<!-- label: III.III.4.6.3 -->

*Then `f` is regular and `B/f(E)` is flat over `A`.*

*Proof.* Set `C = B/f(E)` and `C̄ = C ⊗_A Ā = B̄/ḡ(Ē)`. First, the `⋀ⁱ_B(E)` are free `B`-modules, hence flat
`A`-modules, since `B` is flat over `A`. As `⋀•_B E ⊗_A Ā ≃ ⋀•_B̄ Ē`, one obtains therefore an exact sequence of
complexes:

```text
0 ⟶ J ⊗_A ⋀•_B E ⟶ ⋀•_B E ⟶ ⋀•_B̄ Ē ⟶ 0.
```

Moreover, since `J² = 0`, one has `J ⊗_A M = J ⊗_A Ā ⊗_A M` for every `A`-module `M`. Denoting by dashed arrows the
augmentation morphisms, and by `d` the rank of `E`, one therefore obtains the bicomplex that follows, where the rows are
exact:

<!-- original page 135 -->

```text
                 0              0              0
                 ↓              ↓              ↓
0 ──► J ⊗_A ⋀ᵈ_B̄ Ē ──► ⋀ᵈ_B E ──► ⋀ᵈ_B̄ Ē ──► 0
                 ↓              ↓              ↓
                ⋮              ⋮              ⋮
                 ↓              ↓              ↓
0 ──► J ⊗_A Ē  ──────► E   ──────► Ē  ─────► 0
        │id⊗ḡ           │f             │ḡ
        ↓               ↓              ↓
0 ──► J ⊗_A B̄  ──────► B   ──────► B̄  ─────► 0
        ⤍              ⤍              ⤍
        J ⊗_A C̄  ──────► C   ──────► C̄  ─────► 0
        ↓               ↓              ↓
        0               0              0
```

Moreover, the right and left columns are exact, since `K•(ḡ)` is a resolution of `C̄` and the latter is flat over `Ā`.
Hence, considering the long exact homology sequence associated with the exact sequence of unaugmented complexes, one
obtains that `K•(f)` is acyclic in degrees `> 0`, and that one has in degree `0` an exact sequence:

```text
0 ⟶ J ⊗_A C̄ ⟶ C ⟶ C̄ ⟶ 0.
```

Hence `C` is flat over `A`, by the "fundamental criterion of flatness" (cf. [BAC], § III.5, th. 1).

**Lemma 4.6.4.**[^N.D.E-III-88] *Let `A` be a commutative ring, `J` a nilpotent ideal, `N ⊂ M` two `A`-modules such that
`M/N` is flat over `A`. If `x₁, ..., x_n` are elements of `N` whose images generate the image `N̄` of `N` in `M/JM`,
then they generate `N`.*

<!-- label: III.III.4.6.4 -->

Indeed, denote by `N′` the submodule of `N` generated by the `xᵢ`, and `Q = N/N′`. Then the morphism `N′ ⊗ (A/J) → N̄`
is surjective. On the other hand, since `M/N` is flat over `A`, the morphism `N ⊗ (A/J) → N̄` is bijective. One thus
obtains that `Q ⊗ (A/J) = 0`, whence `Q = 0` by the "nilpotent Nakayama lemma" (one has `Q = JQ = J²Q = ··· = 0`).

One can now prove:

**Proposition 4.6.5.**[^N.D.E-III-88] *Let `S, I, J` and `X, Y_J` be as in 4.5. Suppose moreover `X` flat over `S` and
`Y_J` locally complete intersection in `X_J`.*

<!-- label: III.III.4.6.5 -->

<!-- original page 136 -->

*a) Then condition (a) of 4.5 (i) is satisfied; moreover, every `Y` flat over `S` lifting `Y_J` is locally complete
intersection in `X`.*

*b) If moreover `Y₀` is affine, condition (b) of loc. cit. is likewise satisfied.*

*Proof.* The first assertion of (a) follows from Lemma 4.6.3; the second then results from Lemma 4.6.4. On the other
hand, the hypothesis entails (cf. 4.6.2) that `N_{Y_J/X_J}` is a finite locally free `O_{Y_J}`-module, hence the
`O_{Y₀}`-module

```text
A₀ = Hom_{O_{Y₀}}(N_{Y_J/X_J} ⊗_{O_{Y_J}} O_{Y₀}, J ⊗_{O_{S₀}} O_{Y₀}).
```

is quasi-coherent (cf. EGA I, 1.3.12), whence `R¹Γ(Y₀, A₀) = 0` if `Y₀` is affine.

**Remark 4.6.6.**[^N.D.E-III-88] *Let us conclude this paragraph by the following example, which shows that, under the
hypotheses of Lemma 4.6.3, if `(ḡ₁, ḡ₂)` is a regular sequence generating the ideal `Ī = ḡ(Ē)`, it does not necessarily
lift to a regular sequence in `B`.*

<!-- label: III.III.4.6.6 -->

*Let `k` be a field, `Ā = k[X, Y]`, denote by `kε` the `Ā`-module `Ā/(X, Y)` (i.e. `P · ε = P(0, 0)ε` for every
`P ∈ Ā`), and let `A = Ā ⊕ kε`, where `J = kε` is an ideal of square zero. One has `A/J = Ā`.*

*The algebra `B = A ⊗_k k[Z, T]` is free over `A`, hence flat; one has `B̄ = k[X, Y, Z, T]`. Set `ḡ₁ = XZ − YT` and
`ḡ₂ = XZ − 1`. Since the polynomial `ḡ₁` is irreducible, `B̄/(ḡ₁)` is integral, and therefore `(ḡ₁, ḡ₂)` is a regular
sequence in `B̄`, generating the ideal `Ī = (XZ − 1, YT − 1)`. Hence*

```text
C̄ = B̄/Ī = k[X, Y, X⁻¹, Y⁻¹] = Ā[X⁻¹, Y⁻¹]
```

*is a flat `Ā`-algebra (and also a flat `A`-algebra). But every lift in `B` of `ḡ₁` is of the form `XY − ZT + λε`, where
`λ ∈ k[Z, T]`, hence annihilates `ε`.*

**4.7.** One has suppressed here Remark 4.7, placed in 4.5.1.

**Remark 4.8.0.**[^N.D.E-III-89] *Let `S` be a scheme, `S′` a closed subscheme, `X` an `S`-scheme, `Y` a sub-`S`-scheme
of `X`, and `X′ = X ×_S S′`, `Y′ = Y ×_S S′`. Then, one has a surjective morphism of `O_{Y′}`-modules*

<!-- label: III.III.4.8.0 -->

```text
N_{Y/X} ⊗_{O_Y} O_{Y′} ──surj──► N_{Y′/X′}.
```

Indeed, up to replacing `X` by a certain open, one may suppose that `Y` is closed, defined by an ideal `I_Y` of `O_X`;
then the image of `I_Y` in `O_{X′}` is the ideal `I_{Y′}` defining `Y′`, and one has a surjective morphism of
`O_{Y′}`-modules

```text
π : (I_Y/I_Y²) ⊗_{O_Y} O_{Y′} ──surj──► I_{Y′}/I_{Y′}².
```

Suppose moreover that `O_Y = O_X/I_Y` is flat over `O_S`; then the natural morphism

```text
I_Y ⊗_{O_X} O_{X′} ⟶ I_{Y′}
```

<!-- original page 137 -->

is bijective (cf. EGA IV₂, 2.1.8). One then has the following commutative diagram with exact rows:

```text
I_Y² ⊗_{O_X} O_{X′} ──► I_Y ⊗_{O_X} O_{X′} ──► (I_Y/I_Y²) ⊗_{O_Y} O_{Y′} ──► 0
       │                       │ ≀                       │ π surj.
       surj.                   ↓                         ↓
0 ──► I_{Y′}² ──────────► I_{Y′} ──────────► I_{Y′}/I_{Y′}² ────────────► 0
```

whence one deduces, by the snake lemma:[^N.D.E-III-90]

```text
N_{Y/X} ⊗_{O_Y} O_{Y′} ⥲ N_{Y′/X′}     if Y is flat over S.        (4.8.0)
```

**Proposition 4.8.** *Let `S, S₀, S_J` and `I, J` be as in 4.5.[^N.D.E-III-91] Let `X` be an `S`-scheme, `Y` a subscheme
of `X`, and `i` the immersion `Y ↪ X`.*

<!-- label: III.III.4.8 -->

*(i) For every `S`-morphism `f : T → X` such that `f_J : T_J → X_J` factors through `Y_J`, one can define an
obstruction*

```text
(∗)    c(X, Y, f) ∈ Hom_{O_{T₀}}(f₀*(N_{Y/X} ⊗_{O_Y} O_{Y₀}), JO_T)
```

*whose vanishing is equivalent to the existence of a factorization of `f` through `Y`.*

*(ii) Let `Y′` be a second subscheme of `X`. Suppose that `Y_J′ = Y_J` and that `Y, Y′` are flat over `S`. One then has
isomorphisms (cf. 4.8.0):*

```text
JO_Y ≃ J ⊗_{O_{S₀}} O_{Y₀} ≃ JO_{Y′}    and    N_{Y/X} ⊗_{O_Y} O_{Y_J} ⥲ N_{Y_J/X_J}
```

*whence an isomorphism:*

```text
u : Hom_{O_{Y₀}}(N_{Y_J/X_J} ⊗_{O_{Y_J}} O_{Y₀}, JO_Y) ⥲ Hom_{O_{Y₀}}(N_{Y/X} ⊗_{O_Y} O_{Y₀}, JO_{Y′}).
```

*Denoting by `i′ : Y′ → X` the canonical immersion and `d(Y, Y′)` the deviation of 4.5.1, one has:[^N.D.E-III-92]*

```text
(∗∗)    c(X, Y, i′) = u(d(Y, Y′)).
```

*(iii) The canonical morphism `N_{Y/X} ──D──► i*(Ω¹_{X/S})` (cf. SGA 1 II, formula 4.3)[^N.D.E-III-93] induces a
morphism:*

```text
D₀ : N_{Y/X} ⊗_{O_Y} O_{Y₀} ⟶ Ω¹_{X₀/S₀} ⊗_{O_{X₀}} O_{Y₀}
```

<!-- original page 138 -->

*and hence, for every `S`-morphism `f : T → X` as in (i), a morphism:*

```text
v_{f₀} : Hom_{O_{T₀}}(f₀*(Ω¹_{X₀/S₀}), JO_T) → Hom_{O_{T₀}}(f₀*(N_{Y/X} ⊗_{O_Y} O_{Y₀}), JO_T),
                                       a ↦ a ∘ f₀*(D₀)
```

*where above the first group is `Hom_{X⁺}(T, L_X)`, cf. 0.1.5. For `a ∈ Hom_{X⁺}(T, L_X)`, one has:*

```text
(∗∗∗)    c(X, Y, a · f) − c(X, Y, f) = v_{f₀}(a),
```

*where `a · f` denotes the composite morphism `T ──{a×f}──► L_X ×_{X⁺} X → X`.*

We shall prove part (i) of the proposition, leaving the reader to (not) verify assertions (ii) and (iii); this
verification is done by reduction to the affine case, then by comparison of explicit definitions.[^N.D.E-III-94]

Let us therefore prove (i). The morphism `f : T → X` defines a morphism of sheaves of rings
`φ : O_X → f_*(O_T)`.[^N.D.E-III-95] Let `U` be an open subscheme of `X` in which `Y` is closed; since `T` (resp. `Y_J`)
has the same underlying space as `T_J` (resp. `Y`), the continuous map underlying `f` sends `T` into `U`, and since `U`
is an open of `X`, `φ` induces a morphism of sheaves of rings `O_U = O_X|_U → f_*(O_T)`, i.e. `f` factors through `U`.

Therefore, one may restrict to the case where `Y` is closed, hence defined by a sheaf of ideals `I_Y`. For `f` to factor
through `Y`, it is necessary and sufficient that the composite map `I_Y → O_X → f_*(O_T)` be zero. Since `f_J` factors
through `Y_J`, the composite map `I_{Y_J} → O_{X_J} → f_*(O_{T_J})` is zero. Considering the commutative diagram, where
the first row is exact:

```text
0 ──► f_*(JO_T) ──────► f_*(O_T) ─────► f_*(O_{T_J})
            ↖              ↑                 ↑
              ↖           φ                 φ_J
                ↖          │                  │
                  ↖       O_X ────────────► O_{X_J}
              φ      ↖    ↑                   ↑
                       ↖  I_Y ────────────► I_{Y_J}
```

<!-- original page 139 -->

one deduces that `φ` sends `I_Y` into `f_*(JO_T)`.[^N.D.E-III-96] Since `J² = 0`, it follows that `f_*(JO_T)`, viewed as
`O_X`-module via `φ`, is annihilated by `I_Y`; consequently, `φ` induces a morphism of `O_X`-modules

```text
h : i_*(N_{Y/X}) = I_Y/I_Y² ⟶ f_*(JO_T).
```

On the other hand, one has cartesian squares:

```text
T₀ ──f₀──► X₀ ◄──i₀── Y₀
│τ_{T₀}    │τ_{X₀}    │τ_{Y₀}
↓          ↓          ↓
T ──f───► X ◄──i──── Y.
```

where `iT₀` etc. are the closed immersions deduced by base change from `S₀ ↪ S`. Since `JO_T` is a quasi-coherent
`O_T`-module annihilated by `I`, one has an isomorphism

```text
JO_T ≃ (τ_{T₀})_*τ_{T₀}*(JO_T),
```

whence `f_*(JO_T) ≃ (τ_{X₀})_*(f₀)_*τ_{T₀}*(JO_T)`. Therefore `h` corresponds, by adjunction, to a morphism of
`O_{T₀}`-modules

```text
h₀ : f₀*τ_{X₀}* i_*(N_{Y/X}) ⟶ i_{T₀}*(JO_T).
```

Now, `τ_{X₀}* i_*(N_{Y/X}) ≃ (i₀)_*τ_{Y₀}*(N_{Y/X}) = N_{Y/X} ⊗_{O_Y} O_{Y₀}`. Hence, returning to the abuse of notation
`i_{T₀}*(JO_T) = JO_T` constantly used, `h₀` identifies with a morphism of `O_{T₀}`-modules

```text
h₀ : f₀*(N_{Y/X} ⊗_{O_Y} O_{Y₀}) ⟶ JO_T
```

which is the obstruction `c(X, Y, f)` sought. This proves (i).

When `f` is the immersion `i′ : Y′ ↪ X`, one sees that `c(X, Y, i′)` comes from the morphism `I_Y ↪ O_X → O_{Y′}` hence
corresponds, by 4.4.1 and 4.5.1, to the class `d(Y, Y′)`. This proves (ii).

Let us prove (iii). First, `D : N_{Y/X} → i_*(Ω¹_{X/S})` induces a morphism

```text
D₀ : τ_{Y₀}*(N_{Y/X}) ⟶ τ_{Y₀}* i_*(Ω¹_{X/S}) = i_0* τ_{X₀}*(Ω¹_{X/S})
```

and, since `X₀ = X ×_S S₀`, one has `τ_{X₀}*(Ω¹_{X/S}) ≃ Ω¹_{X₀/S₀}` (cf. EGA IV₄, 16.4.5). One thus obtains the
announced morphism

```text
D₀ : N_{Y/X} ⊗_{O_Y} O_{Y₀} ⟶ Ω¹_{X₀/S₀} ⊗_{O_{X₀}} O_{Y₀}.
```

Finally, we shall verify equality `(∗∗∗)` after the remark below.

**Remark 4.9.** *The obstruction `c(X, Y, f)` is computed locally on `T`. Let `U = Spec(C)` be an affine open of `T`
above an affine open `Spec(A)` of `X`, itself above an affine open `Spec(Λ)` of `S`; let `J ⊂ I ⊂ Λ` (resp. `I_Y ⊂ A`)
be the ideals corresponding to `J ⊂ I` (resp. to `I_Y`), let `B = A/I_Y` and let `φ : A → C` be the morphism of
`Λ`-algebras corresponding to `f : T → X`; since `f(T_J) ⊂ Y_J` one has `φ(I_Y) ⊂ JC` and therefore `φ` induces a
morphism of `Λ`-algebras `B → C/JC → C₀ = C/IC`. Then the obstruction `c = c(X, Y, f)` is computed by the following
commutative diagram:*

<!-- label: III.III.4.9 -->

```text
I_Y ────────────► A ─────φ─────► C
                                  ↑
                                  │c
I_Y/I_Y² ──► I_Y/I_Y² ⊗_B C₀ ────► JC,
```

<!-- original page 140 -->

*that is, it is defined, above the open `U`, as the unique element of*

```text
Hom_{C₀}(I_Y/I_Y² ⊗_B C₀, JC) = Hom_{B₀}(I_Y/I_Y² ⊗_B B₀, JC)
```

*such that, with the evident notation, one has `c(x ⊗_B 1) = φ(x)`, for every `x ∈ I_Y`.*

[^N.D.E-III-97] One can now complete the proof of 4.8 (iii). The equality `(∗∗∗)` is verified locally on `T`, so one is
reduced to the affine situation described above. Let us denote by `d_{A/Λ}` the differential `A → Ω¹_{A/Λ}`. Then `a`
corresponds, above `U`, to an element `a_U` of

```text
Hom_{C₀}(Ω¹_{A₀/Λ₀} ⊗_{A₀} C₀, JC) ≃ Hom_{B₀}(Ω¹_{A/Λ} ⊗_A B₀, JC) ≃ Hom_A(Ω¹_{A/Λ}, JC).
```

Then, on the one hand, `v_{f₀}(a)` corresponds above `U` to the element `a_U ∘ D̄₀`, where `D̄₀` is the morphism of
`B`-modules[^N.D.E-III-98]

```text
I_Y/I_Y² ⟶ Ω¹_{A/Λ} ⊗_A B₀,    x + I_Y² ↦ d_{A/Λ}(x) ⊗ 1.
```

On the other hand (cf. the proofs of 0.1.8 and 0.1.9), the morphism of `Λ`-algebras `φ′ : A → C` corresponding to
`a · f` differs from `φ` by the `Λ`-derivation `A → JC` associated with `a_U`, i.e. one has:

```text
φ′ = φ + a_U ∘ d_{A/Λ} = φ + a_U ∘ (d_{A/Λ} ⊗ 1).
```

Consequently, denoting `c′ = c(X, Y, a · f)`, one has for every `x ∈ I_Y`, denoting by `x̄` its image in `I_Y/I_Y²`:

```text
(c′ − c)(x̄ ⊗ 1) = a_U(d_{A/Λ}(x) ⊗ 1) = (a_U ∘ D̄₀)(x̄) = v_{f₀}(a)(x̄).
```

This shows that `c′ − c = v_{f₀}(a)`.

**4.10.** One has suppressed Remark 4.10 of the original, made obsolete by the addition of Remark 4.8.0.

**4.11.** We now propose to study the following situation. Let `S, S_J` and `S₀` be as in 4.8; one has three `S`-schemes
`X, X′, T`, a subscheme `Y` of `X` (resp. `Y′` of `X′`), and morphisms `f : T → X′` and `g : X′ → X`.

<!-- original page 141 -->

```text
                                  Y′         Y
                                  ⊂          ⊂
                                  ↓i′        ↓i
T ──────f────► X′ ──────g────► X.
```

One supposes that by reduction modulo `J`, this diagram completes into a commutative diagram

```text
                                    Y_J′ ──┄──► Y_J
                                    ⊂            ⊂
                                  ↗ i_J′         ↓i_J
                                ↗
T_J ──────f_J────► X_J′ ──────g_J────► X_J.
```

One has therefore by 4.8 obstructions:

```text
c(X, Y, g ∘ i′) ∈ Hom_{O_{Y₀′}}(i_0′*g_0*(N_{Y/X} ⊗_{O_Y} O_{Y₀}), JO_{Y′}),
c(X′, Y′, f) ∈ Hom_{O_{T₀}}(f₀*(N_{Y′/X′} ⊗_{O_{Y′}} O_{Y₀′}), JO_T),
c(X, Y, g ∘ f) ∈ Hom_{O_{T₀}}(f₀*g₀*(N_{Y/X} ⊗_{O_Y} O_{Y₀}), JO_T),
```

whose relations one seeks to compute.[^N.D.E-III-99]

**Lemma 4.12.** *Suppose `Y′` flat over `S`, so that `J ⊗_{O_{S₀}} O_{Y₀′} = JO_{Y′}`.*

<!-- label: III.III.4.12 -->

*(i) One has a natural morphism*

```text
b_{f₀} : Hom_{O_{Y₀′}}(i_0′*g_0*(N_{Y/X} ⊗ O_{Y₀}), JO_{Y′}) ⟶ Hom_{O_{T₀}}(f₀*g₀*(N_{Y/X} ⊗ O_{Y₀}), JO_T).
```

*(ii) One has also a natural morphism, functorial in `T`,[^N.D.E-III-100]*

```text
a_{g₀}(f₀) : Hom_{O_{T₀}}(f₀*(N_{Y′/X′} ⊗ O_{Y₀′}), JO_T) ⟶ Hom_{O_{T₀}}(f₀*g₀*(N_{Y/X} ⊗ O_{Y₀}), JO_T).
```

*Proof.*[^N.D.E-III-101] Let us first note that, `X, X′, Y, Y′` being fixed, to give a `T` as above is equivalent to
giving a morphism `(f, f_J) : T → X′ ×_{X′⁺} Y′⁺`. Set `Z = X′ ×_{X′⁺} Y′⁺` and denote by `M` and `M′` the `Z`-functors
defined by: for every `f : T → Z`,

```text
M(T) = Hom_{O_{T₀}}(f₀*g₀*(N_{Y/X} ⊗ O_{Y₀}), JO_T)
M′(T) = Hom_{O_{T₀}}(f₀*(N_{Y′/X′} ⊗ O_{Y₀′}), JO_T).
```

[^N.D.E-III-102]

One has in any case a commutative diagram:

```text
f₀*(J ⊗_{O_{S₀}} O_{Y₀′}) ──── J ⊗_{O_{S₀}} O_{T₀}
        │                              │
        ↓                              ↓
f₀*(JO_{Y′})       ─┄┄┄┄─►          JO_T
```

<!-- original page 142 -->

and since `Y′` is flat over `S`, the left arrow is an isomorphism, hence one obtains a morphism of `O_{T₀}`-modules
`f₀*(JO_{Y′}) → JO_T`. The latter induces a morphism of abelian groups

```text
Hom_{O_{T₀}}(f₀*g₀*(N_{Y/X} ⊗ O_{Y₀}), f₀*(JO_{Y′})) ⟶ M(T)
```

and, composing with the morphism

```text
M(Y′) ⟶ Hom_{O_{T₀}}(f₀*g₀*(N_{Y/X} ⊗ O_{Y₀}), f₀*(JO_{Y′})),
```

induced by `f₀*`, one obtains the morphism `b_{f₀} : M(Y′) → M(T)`.

Likewise, one has in any case a diagram

```text
g_0*(N_{Y/X} ⊗_{O_Y} O_{Y₀}) ─┄┄┄┄┄─► N_{Y′/X′} ⊗_{O_{Y′}} O_{Y₀′}
              │                                    │
              ↓                                    ↓
g_0*(N_{Y₀/X₀})  ────────────────────► N_{Y₀′/X₀′}
```

and since `Y′` is flat over `S`, the second vertical arrow is an isomorphism by 4.8.0. One thus obtains an
`O_{Y₀′}`-morphism

```text
i_0′*g_0*(N_{Y/X} ⊗_{O_Y} O_{Y₀}) ⟶ N_{Y′/X′} ⊗_{O_{Y′}} O_{Y₀′}
```

which induces a morphism `a_{g₀}(id_{Y′}) : M′(Y′) → M(Y′)` and, for every `f : T → Z`, a morphism
`a_{g₀}(f) : M′(T) → M(T)` such that one has a commutative diagram

```text
M′(Y′) ──{a_{g₀}(id_{Y₀′})}──► M(Y′)
  │                              │
  b′_{f₀}                        b_{f₀}
  ↓                              ↓
M′(T)  ──{a_{g₀}(f₀)}──────► M(T)
```

(where `b′_{f₀}` is defined like `b_{f₀}`). QED.

**Remark 4.12.1.**[^N.D.E-III-103] *Denote by `M₀` and `M₀′` the `Y₀′`-functors defined by: for every `f : T₀ → Y₀′`,*

<!-- label: III.III.4.12.1 -->

```text
M₀(T) = Hom_{O_{T₀}}(f₀*g₀*(N_{Y/X} ⊗ O_{Y₀}), J ⊗_{O_{S₀}} O_{T₀})
M₀′(T) = Hom_{O_{T₀}}(f₀*(N_{Y′/X′} ⊗ O_{Y₀′}), J ⊗_{O_{S₀}} O_{T₀}).
```

<!-- original page 143 -->

*Note immediately that `Z₀ = Y₀′` and that on the category of `Z`-schemes `T` which are flat over `S`, `M` and `M′`
coincide, respectively, with the functors `∏_{S₀/S} M₀` and `∏_{S₀/S} M₀′`. In this case, `b_{f₀}` is simply the
morphism*

```text
f₀* : M₀(Y₀′) ⟶ M(T₀)
```

*induced by `f₀`, and for every morphism `u : U → T`, setting `h = f ∘ u`, one has a commutative diagram*

```text
M₀′(T₀) ──{a_{g₀}(f₀)}──► M₀(T₀)
   │                          │
   u₀*                        u₀*
   ↓                          ↓
M₀′(U₀) ──{a_{g₀}(h₀)}──► M₀(U₀)
```

*i.e. `a_{g₀}` becomes a morphism of functors `∏_{S₀/S} M₀′ → ∏_{S₀/S} M₀`.*

**Proposition 4.13.** *Suppose `Y′` flat over `S`. One has then the formula:*

<!-- label: III.III.4.13 -->

```text
c(X, Y, g ∘ f) = a_{g₀}(c(X′, Y′, f)) + b_{f₀}(c(X, Y, g ∘ i′)).
```

Since the definition of the different obstructions and of the morphisms `a_{g₀}` and `b_{f₀}` is local, one easily sees
that it suffices to verify the given formula when the different schemes in play are affine. Let us thus denote
`S = Spec(Λ)`, `S_J = Spec(Λ/J)`, `S₀ = Spec(Λ/I)`, `T = Spec(C)`, `X = Spec(A)`, `Y = Spec(A/I_Y) = Spec(B)`,
`X′ = Spec(A′)`, `Y′ = Spec(A′/I_{Y′}) = Spec(B′)`.

One has therefore a diagram of rings and ideals[^N.D.E-III-104]

```text
                                B′         B
                                ↑          ↑
                                π′         π
                                │          │
                C ◄──f── A′ ◄──g── A
                                ↑          ↑
                                │          │
                            I_{Y′}      I_Y.
```

Let us study the different terms of the formula to be proved. In what follows, if `x ∈ I_Y` (resp. `u ∈ I_{Y′}`), we
denote by `x̄` (resp. `ū`) its image in `I_Y/I_Y²` (resp. `I_{Y′}/I_{Y′}²`); on the other hand, if `m` belongs to a
`Λ`-module `M`, we denote by `m̄₀` its image in `M₀ = M/IM`.

One has seen that `c = c(X, Y, g ∘ f)` is the unique `C₀`-morphism `I_Y/I_Y² ⊗_B C₀ → JC` such that
`c(x̄ ⊗ 1) = f(g(x))`, for every `x ∈ I_Y`.

<!-- original page 144 -->

Fix `x ∈ I_Y`; one has `g(x) ∈ I_{Y′} + JA′` since `g_J(Y_J′) ⊂ Y_J`. Write `g(x) = x′ + Σ λᵢ a′ᵢ`, with `x′ ∈ I_{Y′}`,
`λᵢ ∈ J`, `a′ᵢ ∈ A′`. One therefore has

```text
(1)    c(X, Y, g ∘ f)(x̄ ⊗ 1) = f(g(x)) = f(x′) + Σ λᵢ f(a′ᵢ).
```

Now consider `a_{g₀}(c(X′, Y′, f))`. According to the definitions laid down, it is defined by the diagram

```text
                                       f
                          I_{Y′} ─────────────► C
                                                ↑
                                                │c(X′,Y′,f)
                                  ≃            │
I_{Y₀′}/I_{Y₀′}² ⊗_{B₀′} C₀ ◄── I_{Y′}/I_{Y′}² ⊗_{B′} C₀ ────► JC
        ↑                                                ↗
        │g₀                                            ↗
        │                                            ↗ a_{g₀}(c(X′,Y′,f))
I_{Y₀}/I_{Y₀}² ⊗_{B₀} C₀ ◄── I_Y/I_Y² ⊗_B C₀
```

One has therefore `a_{g₀}(c(X′, Y′, f))(x̄ ⊗ 1) = f(u)`, where `u` is an element of `I_{Y′}` whose image `ū` in
`I_{Y₀′}/I_{Y₀′}²` satisfies `ū₀ ⊗ 1 = ḡ₀(x̄₀) ⊗ 1 = g̅₀(x̄₀) ⊗ 1`. One can therefore take `u = x′` and one finds

```text
(2)    a_{g₀}(c(X′, Y′, f))(x̄ ⊗ 1) = f(x′).
```

Consider finally `b_{f₀}(c(X, Y, g ∘ i′))`. By hypothesis, the morphism of `Λ₀`-algebras `f₀ : A₀′ → C₀` factors through
`B₀′`, and therefore, since `J ⊗_{Λ₀} B₀′ ⥲ JB′` (`B′` being flat over `Λ`), one obtains a morphism of `B₀′`-modules
`ψ : JB′ → JC` such that one has a commutative diagram:

```text
J ⊗_{Λ₀} A₀′ ──{id⊗π′}──► J ⊗_{Λ₀} B₀′ ──{id⊗f₀}──► J ⊗_{Λ₀} C₀
       │                          │ ≀
       ↓                          ↓
   JA′  ──────π′──────►       JB′ ──ψ─►       JC.
```

Denote `φ : JB′ ⊗_{B₀′} C₀ → JC` the morphism of `C₀`-modules deduced from `ψ`; then one has, for every `a′ ∈ A′`,
`λ ∈ J`,

```text
(†)    φ(λπ′(a′) ⊗ 1) = λf(a′).
```

<!-- original page 145 -->

Then, `b_{f₀}(c(X, Y, g ∘ i′))` is defined by the commutative diagram:

```text
                              π′ ∘ g
              I_Y  ──────────────────────► B′
                                            ↑
                                            │c(X,Y,g∘i′)
                                            │
              I_Y/I_Y² ⊗_B B₀′ ────────► JB′
                          │                    │
                          ↓                    ↓
              I_Y/I_Y² ⊗_B C₀ ────────► JB′ ⊗_{B₀′} C₀
                              ↘                      ↘ φ
                                ↘                      ↘
                                  ↘ b_{f₀}(c(X,Y,g∘i′))   ↘
                                    ↘                       ↘
                                                               JC.
```

One has therefore at once

```text
(3)    b_{f₀}(c(X, Y, g ∘ i′))(x̄ ⊗ 1) = φ(Σ λᵢ π′(a′ᵢ) ⊗ 1) = Σ λᵢ f(a′ᵢ),
```

the last equality following from `(†)` above. The comparison of the three explicit results (1), (2), (3) gives the
formula sought.

**Corollary 4.14.** *Let `Y, Y′` be two flat subschemes of `X`, reducing to `Y_J`; suppose `Y₀` locally complete
intersection in `X₀`. If `f : T → X` is an `S`-morphism such that `f_J` factors through `Y_J → X_J`, one has the
formula*

<!-- label: III.III.4.14 -->

```text
c(X, Y, f) − c(X, Y′, f) = b_{f₀}(d(Y, Y′)).
```

Indeed, applying the preceding formula to the diagram

```text
                                 Y′           Y
                                 ⊂            ⊂
                                 ↓i′          ↓i
                       T ─f──► X ──id──► X
```

one finds `c(X, Y, f) − c(X, Y′, f) = b_{f₀}(c(X, Y, i′))`. Moreover, by 4.8 (ii), one has `c(X, Y, i′) = d(Y, Y′)`.

**Proposition 4.15.** *Let `X` be an `S`-group smooth over `S` and `Y` a sub-`S`-group flat and locally of finite
presentation over `S`. Then `Y` is locally complete intersection (cf. 4.6.2) in `X`.*

<!-- label: III.III.4.15 -->

<!-- original page 146 -->

*Proof.*[^N.D.E-III-105] We shall show that the immersion `Y → X` is regular in the sense of EGA IV₄, 16.9.2, which
implies that it is also regular in the sense of 4.6.2, by EGA IV₄, 19.5.1 (moreover, by loc. cit., the two definitions
are equivalent if `S` is locally noetherian). Therefore, in what follows, we take "regular immersion" in the sense of
EGA IV₄, 16.9.2. Since `X` and `Y` are flat and locally of finite presentation over `S`, then, by EGA IV₄, 19.2.4, it
suffices to show that, for every `s ∈ S`, `Y_s → X_s` is a regular immersion. By EGA IV₄, 19.1.5 (ii), one is reduced to
verifying the assertion on the geometric fibers of `S`, that is, when `S` is the spectrum of an algebraically closed
field `k`.

Then, by VI_A, 3.2, the quotient `X/Y` exists and is smooth, the morphism `π : X → X/Y` is flat, and one has a cartesian
square

```text
Y ──f──► X
│        │
i        π
↓        ↓
e ────► X/Y
```

(where `e` is the image in `X/Y` of the unit point of `X`). Therefore, by flat base change (cf. EGA IV₄, 19.1.5 (ii)),
it suffices to see that `i` is a regular immersion, which is immediate since the noetherian local ring `O_{X/Y, e}` is
smooth, hence its maximal ideal is generated by a regular sequence.

**4.16.**[^N.D.E-III-106] Let `X` be an `S`-group smooth over `S`, denote `μ : X ×_S X → X` its group law. Suppose given
a sub-`S_J`-group `Y_J` of `X_J`, flat and locally of finite presentation over `S_J`. By 4.15, `Y_J` is locally complete
intersection in `X`.

Hence, by 4.6.5, every flat `S`-scheme[^N.D.E-III-107] `Y` lifting `Y_J` is locally complete intersection in `X`. For
such a `Y` one has, by 4.8.0,

<!-- label: III.III.4.16.1 -->

```text
(4.16.1)    N_{Y/X} ⊗_{O_Y} O_{Y₀} = N_{Y₀/X₀} = N_{Y_J/X_J} ⊗_{O_{Y_J}} O_{Y₀}.
```

On the other hand, denote by `ε₀ : S₀ → Y₀` the unit section of `Y₀` and `n_{Y₀/X₀}` the quasi-coherent `O_{S₀}`-module:

```text
n_{Y₀/X₀} = ε₀*(N_{Y₀/X₀}).
```

Since `Y₀` and `X₀` are `S₀`-groups, one sees easily that `N_{Y₀/X₀}` is invariant under the (say left) translations of
`Y₀`, hence[^N.D.E-III-108] is the inverse image by `Y₀ → S₀` of `n_{Y₀/X₀}`, i.e. one has

<!-- label: III.III.4.16.2 -->

```text
(4.16.2)    N_{Y₀/X₀} = n_{Y₀/X₀} ⊗_{O_{S₀}} O_{Y₀}.
```

<!-- original page 147 -->

Taking (4.16.1) and (4.16.2) into account, one deduces on the one hand from 4.5 that the set of sub-`S`-schemes `Y` of
`X`, flat over `S`, lifting `Y_J`, is empty or principal homogeneous under

<!-- label: III.III.4.16.3 -->

```text
(4.16.3)    Hom_{O_{Y₀}}(n_{Y₀/X₀} ⊗_{O_{S₀}} O_{Y₀}, J ⊗_{O_{S₀}} O_{Y₀}),
```

and one deduces on the other hand from 4.8 (i) that, for every such `Y` and every `S`-morphism `f : T → X` such that
`f_J : T_J → X_J` factors through `Y_J`, the obstruction `c(X, Y, f)` to `f` factoring through `Y` is an element of

```text
Hom_{O_{T₀}}(n_{Y₀/X₀} ⊗_{O_{S₀}} O_{T₀}, JO_T);
```

if moreover `T` is flat over `S`, this last group equals

```text
Hom_{O_{T₀}}(n_{Y₀/X₀} ⊗_{O_{S₀}} O_{T₀}, J ⊗_{O_{S₀}} O_{T₀}).
```

This leads to introducing the group functor `N₀` below:

**Definition 4.16.1.** *Let `N₀` be the `S₀`-functor in commutative groups defined by: for every `Z ∈ Ob (Sch)/S₀`,*

<!-- label: III.III.4.16.1d -->

```text
(∗)    Hom_{S₀}(Z, N₀) = Hom_{O_Z}(n_{Y₀/X₀} ⊗_{O_{S₀}} O_Z, J ⊗_{O_{S₀}} O_Z).
```

*Then, the set of sub-`S`-schemes `Y` of `X`, flat over `S`, lifting `Y_J`, is empty or principal homogeneous under*

```text
Hom_{S₀}(Y₀, N₀) = C¹(Y₀, N₀).
```

*For each such `Y`, consider the following diagram:*

```text
                Y ×_S Y          Y
                  ⊂              ⊂
                (i,i)            i
                  ↓     μ        ↓
                X ×_S X ────► X
```

*and denote `DY = c(X, Y, μ ∘ (i, i))` the obstruction to `μ ∘ (i, i)` factoring through `Y`, i.e. to `Y` being stable
under the group law of `X`; by what precedes, `DY` is an element of*

```text
N₀(Y₀ ×_{S₀} Y₀) = C²(Y₀, N₀).
```

**Lemma 4.17.**[^N.D.E-III-109] *Let `X` be an `S`-group smooth over `S` and `Y_J` a sub-`S_J`-group of `X_J`, flat and
locally of finite presentation over `S_J`. For each subscheme `Y` of `X`, flat over `S` and lifting `Y_J`, consider the
obstruction defined in 4.16.1:*

<!-- label: III.III.4.17 -->

```text
DY ∈ Hom_{S₀}(Y₀ ×_{S₀} Y₀, N₀) = C²(Y₀, N₀)
```

*(i) For `Y` to be a sub-`S`-group of `X`, it is necessary and sufficient that `DY = 0`.*

<!-- original page 148 -->

*(ii) If one makes `Y₀` act on `N₀` by functoriality from the inner automorphisms of `Y₀`, then `DY ∈ Z²(Y₀, N₀)`.*

*(iii) If `Y` and `Y′` are two subschemes of `X`, flat over `S`, lifting `Y_J` (so that the deviation
`d(Y, Y′) ∈ C¹(Y₀, N₀)` is defined, cf. 4.5.1), one has `DY′ − DY = ∂¹d(Y, Y′)`.[^N.D.E-III-110]*

Let us successively prove these various assertions.

**4.18.** *Proof of 4.17 (i).* By definition, one has `DY = 0` if and only if `Y` is stable under the group law of `X`.
Hence `DY = 0` if `Y` is a subgroup of `X`. Conversely, if `DY = 0`, `Y` is equipped with the induced law `μ_Y`, which
is associative and reduces modulo `J` to the group law on `X_J`; since `Y` is flat and locally of finite presentation
over `S`, it follows from 3.3 that `μ_Y` is a group law.

**4.19.** *Proof of 4.17 (ii).* This is done by comparing the two values of `u = c(X, Y, μ² ∘ (i, i, i))` computed in
the two following diagrams `(D_j)`, `j = 1, 2`:

```text
                Y ×_S Y ×_S Y     Y ×_S Y     Y
                       ⊂              ⊂        ⊂
(D_j)              (i,i,i)        (i,i)         i
                       │  f_j           μ        ↓
                       ↓                ↓        │
                X ×_S X ×_S X ────► X ×_S X ──► X
```

where `f₁ = (1, π)`, `f₂ = (π, 1)`, and where one denotes by `μ²` the morphism

```text
μ ∘ f₁ = μ ∘ f₂ : X ×_S X ×_S X ⟶ X.
```

[^N.D.E-III-111]

Set `μ_Y = μ ∘ (i, i)`, `f_{j,Y} = f_j ∘ (i, i, i)` and `μ_{2,Y} = μ² ∘ (i, i, i)`. For `j = 1, 2`, denote by `a_j` and
`b_j` the morphisms

```text
a_j = a_{μ₀}((f_{j,Y})₀)    and    b_j = b_{(f_{j,Y})₀},
```

associated with the pair of morphisms `(f_{j,Y}, μ)` by Lemma 4.12; one has therefore:

```text
(†)   Hom_{O_{Y₀³}}((f_{j,Y})₀*(N_{Y₀×Y₀/X₀×X₀}), JO_{Y₀³}) ──{a_j}──► Hom_{O_{Y₀³}}((μ_{2,Y})₀*(N_{Y₀/X₀}), JO_{Y₀³})

      Hom_{O_{Y₀²}}((μ_Y)₀*(N_{Y₀/X₀}), JO_{Y₀²}) ──{b_j}──► Hom_{O_{Y₀³}}((μ_{2,Y})₀*(N_{Y₀/X₀}), JO_{Y₀³}).
```

<!-- original page 149 -->

Since `N_{Y₀×Y₀/X₀×X₀} ≃ pr₁* N_{Y₀/X₀} ⊕ pr₂* N_{Y₀/X₀}` (since `X₀` and `Y₀` are flat over `S₀`), and
`N_{Y₀/X₀} ≃ n_{Y₀/X₀} ⊗_{O_{S₀}} O_{Y₀}`, then:

```text
(f_{j,Y})₀*(N_{Y₀×Y₀/X₀×X₀}) ≃ (n_{Y₀/X₀} ⊕ n_{Y₀/X₀}) ⊗ O_{Y₀³}
```

and, likewise,

```text
(μ_{2,Y})₀*(N_{Y₀/X₀}) ≃ n_{Y₀/X₀} ⊗ O_{Y₀³}    and    (μ_Y)₀*(N_{Y₀/X₀}) ≃ n_{Y₀/X₀} ⊗ O_{Y₀²}.
```

Moreover, since `Y₀²` and `Y₀³` are flat over `S₀`, then `(†)` rewrites in the following form:

```text
(‡)  ⎧ a_j : Hom_{S₀}(Y₀³, N₀ ⊕ N₀) → Hom_{S₀}(Y₀³, N₀)
     ⎩ b_j : Hom_{S₀}(Y₀², N₀) → Hom_{S₀}(Y₀³, N₀).
```

Applying 4.13 twice to `c(X, Y, μ_{2,Y}) = u`, one obtains:

```text
a₁(c(X², Y², f₁)) + b₁(c(X, Y, μ_Y)) = u = a₂(c(X², Y², f₂)) + b₂(c(X, Y, μ_Y)).
```

Now, `c(X, Y, μ_Y) = DY` and, since `f₁ = (1, μ)` and `f₂ = (μ, 1)`, one has, with evident notations:

```text
c(X², Y², f₁) = (0, DY)    and    c(X², Y², f₂) = (DY, 0).
```

Hence, one obtains:

```text
u = a₁((0, DY)) + b₁(DY) = a₂((DY, 0)) + b₂(DY).
```

The first thing one notes is that `b_j` is nothing other than `Hom_{S₀}((f_{j,Y})₀, N₀)`, that is to say, the morphism
deduced from `(f_{j,Y})₀` by functoriality.

The identity above therefore becomes:

```text
a₁((0, DY)) − Hom((μ, 1), N₀)(DY) + Hom((1, μ), N₀)(DY) − a₂((DY, 0)) = 0.
```

One recognizes the two middle terms: they are the parts "`DY(xy, z)`" and "`DY(x, yz)`" of the 2-coboundary formula. It
only remains, then, to identify the two other terms.

We must first compute the map `a_j`. Now it comes, by inverse image by `(f_{j,Y})₀`, from the morphism of
`O_{Y₀²}`-modules

```text
P : n_{Y₀/X₀} ⊗ O_{Y₀²} ⟶ (n_{Y₀/X₀} ⊕ n_{Y₀/X₀}) ⊗ O_{Y₀²}
```

induced by the product in `Y₀`. Now this morphism is described in the following way: consider the vector bundle
`V = V(n_{Y₀/X₀})`; `P` gives by duality a morphism

```text
V(P) : V ×_{S₀} V ×_{S₀} Y₀ ×_{S₀} Y₀ ⟶ V ×_{S₀} Y₀ ×_{S₀} Y₀
```

<!-- original page 150 -->

which is expressed set-theoretically by[^N.D.E-III-112]

```text
V(P)(u, v, a, b) = (u + Ad(a)v, ab, b).
```

This is proved exactly like the corresponding fact on Lie algebras, that is, on the module `ω¹_{Y₀/S₀}`. One first notes
that `V` is endowed by functoriality in `Y₀` with a group structure in the category of vector bundles on `S₀`; by virtue
of the lemma already used for Lie algebras (Exposé II, 3.10), this structure coincides with the group structure
underlying its `O_S`-module structure. One then sees that `V(n_{Y₀/X₀} ⊗_{O_{S₀}} O_{Y₀}) = V(N_{Y₀/X₀})` is also
endowed with a structure of `S₀`-group which is none other than the semi-direct product of that of `V` by that of `Y₀`.
It only remains to identify the operations of `Y₀` on `V` to establish the desired formula.

Let us now compute the two remaining terms. Consider first `a₁((0, DY))`. One computes it by the diagram (where `n`
denotes `n_{Y₀/X₀}`):

```text
n ⊗ O_{Y₀²} ──P──► (n + n) ⊗ O_{Y₀²}
    │                      │
    (f₁,Y)₀*               (f₁,Y)₀*
    ↓                      ↓
n ⊗ O_{Y₀³}        (n + n) ⊗ O_{Y₀³}
       ↘                     │
         ↘                   (0, DY)
           ↘ a₁((0,DY))      ↓
             ↘             J ⊗ O_{Y₀³}.
```

Considering now the vector bundles defined by these different modules as so many schemes over `S₀` and taking points
with values in anything, one has, denoting `(u, x, y, z)` a point of `V(J) × Y₀³`;

```text
(Ad(x)DY_{y,z}(u), x, yz) ◄──────── (0 + DY_{y,z}(u), x, yz)
              ↑                                  ↑
              │                                  │
              │                            (0 + DY_{y,z}(u), x, y, z)
              │                                  ↑
              │                                  │
(Ad(x)DY_{y,z}(u), x, y, z) ◄──────── (u, x, y, z).
```

One has thus obtained `a₁((0, DY))(x, y, z) = Ad(x)DY(y, z)`, which is indeed the first term of the coboundary. One
would have likewise `a₂((DY, 0))(x, y, z) = DY(x, y)`, whence[^N.D.E-III-113]

```text
0 = Ad(x)DY(y, z) − DY(xy, z) + DY(x, yz) − DY(x, y) = (∂²DY)(x, y, z).
```

<!-- original page 151 -->

**4.20.** *Proof of 4.17 (iii).*[^N.D.E-III-114] This is done by comparing the two values of `v = c(X, Y, μ ∘ (i′, i′))`
computed in the two following diagrams

```text
                                      Y′       Y
                                       ⊂        ⊂
(∗)                                    i′       i
                                       │  μ∘(i′,i′)    │
            Y′ ×_S Y′ ────────────────► X       X
```

```text
                                      Y ×_S Y    Y
                                          ⊂        ⊂
(†)                                    (i,i)       i
                          (i′,i′)         μ        ↓
            Y′ ×_S Y′ ──────────► X ×_S X ──────► X.
```

Denote `f = μ ∘ (i′, i′)`; then `(∗)` gives

```text
(1)    v = DY′ + f₀*(c(X, Y, i′)).
```

Now `Y₀′ = Y₀` and `f₀` is the multiplication `Y₀² → Y₀`; one deduces from this that

```text
(2)    f₀*(c(X, Y, i′))(x₀, y₀) = c(X, Y, i′)(x₀y₀).
```

Set `c = c(X, Y, i′)`; via the identification `N₀′ ≃ N₀ ⊕ N₀`, `c(X ×_S X, Y ×_S Y, (i′, i′))` identifies with the pair
`(c, c)`. Then, denoting `h = (i′, i′)`, `(†)` gives

```text
(3)    v = h₀*(DY) + a_{μ₀}(c, c).
```

Now `h₀` is the identity map of `Y₀²`, whence `h₀*(DY) = DY`. Finally, by the computation of `a_{μ₀}` done previously,
one has for every `S′ → S` and `x₀, y₀ ∈ Y₀(S₀′)`,

```text
(4)    a_{μ₀}(c, c)(x₀, y₀) = c(x₀) + Ad(x₀)(c(y₀)).
```

One thus obtains:

```text
(DY′ − DY)(x₀, y₀) = Ad(x₀)c(X, Y, i′)(y₀) − c(X, Y, i′)(x₀y₀) + c(X, Y, i′)(x₀)
                    = (∂¹c(X, Y, i′))(x₀, y₀).
```

Since `c(X, Y, i′) = d(Y, Y′)` (cf. 4.8 (ii)), this shows that `DY′ − DY = ∂¹d(Y, Y′)`.

**Theorem 4.21.** *Let `S` be a scheme, `I` and `J` two ideals[^N.D.E-III-115] on `S` such that `I ⊃ J` and `I · J = 0`.
Let `X` be an `S`-group smooth over `S` and `Y_J` a sub-`S_J`-group of `X_J`, flat and locally of finite presentation
over `S_J`. Consider the `S₀`-functor in commutative groups `N₀` defined by*

<!-- label: III.III.4.21 -->

```text
Hom_{S₀}(T, N₀) = Hom_{O_T}(n_{Y₀/X₀} ⊗_{O_{S₀}} O_T, J ⊗_{O_{S₀}} O_T),    T ∈ Ob (Sch)/S₀,
```

*on which `Y₀` acts via the inner automorphisms of `X₀`.*

*(i) For there to exist a sub-`S`-group of `X`, flat over `S`, which reduces to `Y_J`, it is necessary and sufficient
that the two following conditions be verified:*

<!-- original page 152 -->

*(i₁) There exists a subscheme `Y` of `X`, flat over `S`, lifting `Y_J` (condition automatically satisfied if `Y₀` is
affine, cf. 4.6.5).*

*(i₂) A certain canonical obstruction, element of `H²(Y₀, N₀)`, is zero.*

*(ii) If the conditions of (i) are satisfied, the set of sub-`S`-groups `Y` of `X`, flat over `S` and reducing to `Y_J`
is a principal homogeneous set under the group `Z¹(Y₀, N₀)`.[^N.D.E-III-116]*

Indeed, condition (i₁) is necessary. Suppose it satisfied and let `Y` be flat over `S` lifting `Y_J`. We must seek a
`Y′` flat over `S` lifting `Y_J` as well such that `DY′ = 0`,[^N.D.E-III-117] cf. 4.17 (i). By 4.17 (iii), this amounts
to seeking a `d(Y′, Y) ∈ C¹(Y₀, N₀)` such that `DY = ∂¹d(Y′, Y)`.[^N.D.E-III-118]

Let `c ∈ H²(Y₀, N₀)` be the image class of `DY`, which is a cocycle by 4.17 (ii). It does not depend on the choice of
`Y` by 4.17 (iii), and its vanishing is necessary and sufficient for the existence of a `d(Y′, Y)` satisfying the
preceding equation. This proves (i).

If one has now chosen `Y` such that `DY = 0`, the equation to solve becomes `∂¹d(Y′, Y) = 0`, which proves (ii).

**Remark 4.22.** *Let us keep the notation of 4.21. By 4.15, `Y₀` is locally complete intersection in `X₀`, hence
`N_{Y₀/X₀}` is a finite locally free `O_{Y₀}`-module, and consequently `n_{Y₀/X₀} = ε₀*(N_{Y₀/X₀})` is a finite locally
free `O_{S₀}`-module. Hence, denoting `n_{Y₀/X₀}^∨ = Hom_{O_{Y₀}}(n_{Y₀/X₀}, O_{Y₀})`, one has*

<!-- label: III.III.4.22 -->

```text
Hom_{O_T}(n_{Y₀/X₀} ⊗_{O_{S₀}} O_T, J ⊗_{O_{S₀}} O_T) ≃ n_{Y₀/X₀}^∨ ⊗_{O_{S₀}} J ⊗_{O_{S₀}} O_T.
```

*for every `T → S₀`.[^N.D.E-III-119] Consequently, the `S₀`-functor `N₀` is isomorphic to the functor*

```text
W(n_{Y₀/X₀}^∨ ⊗_{O_{S₀}} J) ≃ W(Hom_{O_{S₀}}(n_{Y₀/X₀}, J)).
```

*It results in isomorphisms:[^N.D.E-III-120]*

```text
H²(Y₀, N₀) ≃ H²(Y₀, Hom_{O_{S₀}}(n_{Y₀/X₀}, J)) ≃ H²(Y₀, n_{Y₀/X₀}^∨ ⊗_{O_{S₀}} J),
Z¹(Y₀, N₀) ≃ Z¹(Y₀, Hom_{O_{S₀}}(n_{Y₀/X₀}, J)) ≃ Z¹(Y₀, n_{Y₀/X₀}^∨ ⊗_{O_{S₀}} J).
```

**4.23.** Still under the hypotheses of 4.21, we are now going to study how the set of `Y` lifting `Y_J` behaves with
respect to conjugation by sections of `X`. If `x` is a section of `X` over `S` inducing the unit section of `X_J`, the
inner automorphism `Int(x)` defined by `x` transforms flat subgroups of `X` lifting `Y_J` into flat subgroups of `X`
lifting `Y_J`. Now, under the conditions of 4.21 (ii), the set of these subgroups is principal homogeneous under
`Z¹(Y₀, N₀)`; we shall see that there then exists a subgroup `Γ` of `B¹(Y₀, N₀)`[^N.D.E-III-121] such that two subgroups
of `X`, flat over `S`, and lifting `Y_J`, are conjugate (by `x ∈ X(S)` inducing the unit of `X(S_J)`) if and only if
their "difference" in `Z¹(Y₀, N₀)` is an element of `Γ`. In the best cases, we shall show that `Γ` equals `B¹(Y₀, N₀)`,
hence that the set of flat subgroups of `X` lifting `Y_J`, modulo conjugation by `x ∈ X(S)` inducing the unit of
`X(S_J)`, is empty or principal homogeneous under `H¹(Y₀, N₀)` (cf. 4.29 and 4.36).

<!-- original page 153 -->

**4.24.** We keep the notation of 4.21. Let `Y` be a flat subgroup of `X`, reducing to `Y_J`. Recall that we introduced
in 0.5 the functor `L₀^X` (resp. `L₀^Y`) defined by the identity with respect to the variable `S₀`-scheme `T`:

```text
Hom_{S₀}(T, L₀^X) = Hom_{O_T}(ω¹_{X₀/S₀} ⊗_{O_{S₀}} O_T, J ⊗_{O_{S₀}} O_T)
```

(resp. similarly on replacing `X` by `Y`), as well as the functor `L′_X = ∏_{S₀/S} L₀^X`.

Now one has:

**Lemma 4.25.** *There exists a canonical exact sequence of `Y₀`-`O_{S₀}`-modules*

<!-- label: III.III.4.25 -->

```text
(+)    n_{Y₀/X₀} ──d──► ω¹_{X₀/S₀} ──► ω¹_{Y₀/S₀} ──► 0
```

*possessing the following properties:*

*(i) By inverse image on `Y₀`, `d` gives the morphism `D̄₀` of 4.8 (iii).*

*(ii) If `X₀` and `Y₀` are smooth over `S₀`, then `d` is injective. Since the two `ω¹` are then locally free of finite
type, so is `n_{Y₀/X₀}` and the sequence is locally split.*

*Proof.*[^N.D.E-III-122] Denote by `π₀` the morphism `Y₀ → S₀`. By SGA 1 II, formula (4.3) (see also EGA IV₄, 16.4.21),
one has a canonical exact sequence of `O_{Y₀}`-modules

```text
(†)    N_{Y₀/X₀} ──D̄₀──► Ω¹_{X₀/S₀} ⊗_{O_{X₀}} O_{Y₀} ──► Ω¹_{Y₀/S₀} ──► 0.
```

Since this sequence is formed of `(Y₀ ×_S Y₀)`-equivariant modules and morphisms, its inverse image `(+)` by `ε₀*` is an
exact sequence of `Y₀`-`O_{S₀}`-modules, and `(†)` is the inverse image of `(+)` by `π₀*` (cf. Exp. I, § 6.8). This
proves (i).

<!-- original page 154 -->

Suppose moreover `X₀` and `Y₀` smooth over `S₀`. Then, by SGA 1 II 4.10 (see also EGA IV₄, 17.2.3 (i) and 17.2.5), `D`
is injective and the sequence `(†)` is formed of `O_{Y₀}`-modules locally free of finite type (hence is locally split).
By the equivalence of categories I, 6.8.1, `d` is also injective, and therefore the sequence `(+)` has the indicated
properties.

**4.26.**[^N.D.E-III-123] For every `S₀`-scheme `f : T → S₀`, `(+)` gives an exact sequence of `Y₀(T)`-`O(T)`-modules

```text
0 ⟶ Hom_{O_T}(f*(ω¹_{Y₀/S₀}), f*(J)) ⟶ Hom_{O_T}(f*(ω¹_{X₀/S₀}), f*(J)) ⟶ Hom_{O_T}(f*(n_{Y₀/X₀}), f*(J)),
```

hence one has an exact sequence of `Y₀`-`O_{S₀}`-modules:

<!-- label: III.III.4.26.1 -->

```text
(4.26.1)    0 ⟶ L₀^Y ⟶ L₀^X ──d──► N₀.
```

From this one deduces an exact sequence of complexes of abelian groups:

```text
0 ⟶ C*(Y₀, L₀^Y) ⟶ C*(Y₀, L₀^X) ──d*──► C*(Y₀, N₀),
```

and in particular, a commutative diagram with exact rows

```text
0 ⟶ C⁰(Y₀, L₀^Y) ⟶ C⁰(Y₀, L₀^X) ──d⁰──► C⁰(Y₀, N₀)
        │ ∂              │ ∂                │ ∂
        ↓                ↓                  ↓
0 ⟶ C¹(Y₀, L₀^Y) ⟶ C¹(Y₀, L₀^X) ──d¹──► C¹(Y₀, N₀).
```

Note that `C⁰(Y₀, L₀^Y)` (resp. `C⁰(Y₀, L₀^X)`) is none other than `Hom_{S₀}(S₀, L₀^Y) = Hom_S(S, L′_Y)` (resp. ···),
i.e. (cf. 0.9) the group of sections of `Y` (resp. `X`) over `S` inducing the unit section of `X_J`. Note also that `d¹`
is none other than the morphism `v_{i_{Y₀}}` of 4.8 (iii), where `i_{Y₀} : Y₀ → X₀` is the canonical
immersion.[^N.D.E-III-124]

**Lemma 4.27.** *Under the conditions of 4.21 for `S, I, J` and `X`, let `Y` be a subgroup of `X`, flat over `S` and
lifting `Y_J`. Denote `i : Y ↪ X` the canonical immersion.[^N.D.E-III-125]*

<!-- label: III.III.4.27 -->

*(i) Let `i′ : Y → X` be a morphism of `S`-schemes lifting `i₀` (so that `i′` is also an immersion), let `Y′ = i′(Y)`
and let `d(i, i′)` be the element of `C¹(Y₀, L₀^X)` such that `i′ = d(i, i′) · i` (cf. 1.2.4). Then the deviation
`d(Y, Y′) ∈ C¹(Y₀, N₀)` (cf. 4.5.1) is given by the formula:*

```text
d(Y, Y′) = d¹(d(i, i′)).
```

*(ii) Let `x ∈ C⁰(Y₀, L₀^X)` be a section of `X` over `S` inducing the unit section of `X_J` over `S_J`. Then the
deviation `d(Y, Int(x)Y) ∈ C¹(Y₀, N₀)` (cf. 4.5.1) is given by the formula:*

<!-- original page 155 -->

```text
−d(Y, Int(x)Y) = d¹∂x = ∂ d⁰x.
```

Indeed, `Y′` is the image of `Y` by the composite morphism:[^N.D.E-III-126]

```text
Y ──{(d(i,i′), i)}──► L′_X ×_S X ⟶ X,
```

which is denoted `d(i, i′) · i` in 4.8 (iii); by loc. cit. and the equality `v_{i₀} = d¹`, one has therefore:

```text
c(X, Y′, d(i, i′) · i) − c(X, Y′, i) = v_{i₀}(d(i, i′)) = d¹(d(i, i′)).
```

But `d(i, i′) · i = i′` factors through `Y′` by definition, hence the first term is zero; moreover, by 4.8 (ii), one has
`c(X, Y′, i) = d(Y′, Y) = −d(Y, Y′)`. Hence `d(Y, Y′) = d¹(d(i, i′))`, which proves (i).

Let now `x` be as in (ii). By the formula

```text
xyx⁻¹ = xyx⁻¹y⁻¹y = (x − Ad(y)x)y = (−∂x)(y) · y,
```

one sees that `Y′` is the image of `Y` by the immersion `i′ = (−∂x) · i_Y`. Hence, by (i) one obtains

```text
−d(Y, Int(x)Y) = d¹∂x = ∂ d⁰x.
```

**Corollary 4.28.** *For two subgroups `Y` and `Y′` of `G`, flat over `S` and lifting `Y_J`, to be conjugate by a
section of `X` over `S` inducing the unit section of `X_J`, it is necessary and sufficient that
`d(Y, Y′) ∈ ∂ d⁰ C⁰(Y₀, L₀^X) ⊂ ∂C⁰(Y₀, N₀) = B¹(Y₀, N₀)`.*

<!-- label: III.III.4.28 -->

**Corollary 4.29.** *If `d⁰` is surjective, `Y` and `Y′` as above are conjugate by a section of `X` over `S` inducing
the unit section of `X_J` if and only if `d(Y, Y′) ∈ B¹(Y₀, N₀)`.*

<!-- label: III.III.4.29 -->

<!-- original page 156 -->

**Corollary 4.30.** *Let `Y` be as in 4.27; the set of conjugates of `Y` by sections of `X` over `S` inducing the unit
section of `X_J` is isomorphic to:*

<!-- label: III.III.4.30 -->

```text
d¹∂(C⁰(Y₀, L₀^X)) = C⁰(Y₀, L₀^X) / Ker d¹∂.
```

Note now that `C⁰(Y₀, L₀^X)/Ker d¹∂` is computed solely with the help of the left square of the commutative diagram of
4.26. It follows in particular that one can also compute it in any diagram of the same type having the same left square.
Consider in particular the functor `L₀^X/L₀^Y` above `S₀` defined by

```text
Hom_{S₀}(T, L₀^X/L₀^Y) = Hom_{S₀}(T, L₀^X) / Hom_{S₀}(T, L₀^Y).
```

One has a commutative diagram

```text
0 ⟶ C⁰(Y₀, L₀^Y) ⟶ C⁰(Y₀, L₀^X) ⟶ C⁰(Y₀, L₀^X/L₀^Y) ⟶ 0
        │ ∂              │ ∂                  │ ∂
        ↓                ↓                    ↓
0 ⟶ C¹(Y₀, L₀^Y) ⟶ C¹(Y₀, L₀^X) ⟶ C¹(Y₀, L₀^X/L₀^Y) ⟶ 0,
```

whence by the preceding remark:

**Corollary 4.31.** *Let `Y` be as in 4.27; the set of conjugates of `Y` by sections of `X` over `S` inducing the unit
section of `X_J` is isomorphic to*

<!-- label: III.III.4.31 -->

```text
E = ∂(C⁰(Y₀, L₀^X/L₀^Y)) = C⁰(Y₀, L₀^X/L₀^Y) / H⁰(Y₀, L₀^X/L₀^Y).
```

**Corollary 4.32.** *Suppose moreover `S₀` affine and `ω¹_{Y₀/S₀}` finite locally free.[^N.D.E-III-127] If one denotes
`F₀ = [Lie(X₀/S₀)/Lie(Y₀/S₀)] ⊗_{O_{S₀}} J`, one has `E = Γ(S₀, F₀)/H⁰(Y₀, F₀)`.*

<!-- label: III.III.4.32 -->

[^N.D.E-III-128] Indeed, since `ω¹_{Y₀/S₀}` is finite locally free, as is `ω¹_{X₀/S₀}` (since `X` is supposed smooth
over `S`), one has, by 0.6:

```text
L₀^Y = W(Lie(Y₀/S₀) ⊗_{O_{S₀}} J)    and    L₀^X = W(Lie(X₀/S₀) ⊗_{O_{S₀}} J).
```

On the other hand, by 4.25, one has an exact sequence of `Y₀`-`O_{S₀}`-modules:

```text
0 ⟶ K ⟶ ω¹_{X₀/S₀} ──φ──► ω¹_{Y₀/S₀} ⟶ 0
```

(where `K = Ker(φ)`). Since `ω¹_{Y₀/S₀}` and `ω¹_{X₀/S₀}` are finite locally free, one has a locally split exact
sequence:

```text
0 ⟶ Lie(Y₀/S₀) ⊗_{O_{S₀}} J ⟶ Lie(X₀/S₀) ⊗_{O_{S₀}} J ⟶ F₀ ⟶ 0.
```

<!-- original page 157 -->

It follows that one has an exact sequence of `Y₀`-`O_{S₀}`-modules:

```text
0 ⟶ L₀^Y ⟶ L₀^X ⟶ W(F₀).
```

By the reasoning that served us to prove 4.31, we can compute `E` as the image of the composite map

```text
C⁰(Y₀, L₀^X) ──π──► C⁰(Y₀, W(F₀)) ──∂──► C¹(Y₀, W(F₀)).
```

Now the map `π` above is the map `Γ(S₀, Lie(X₀/S₀) ⊗_{O_{S₀}} J) → Γ(S₀, F₀)`. Hence, `S₀` being affine, `π` is
surjective and one finds indeed the announced result.

**Corollary 4.33.** *Let `S, I, J` and `X` be as in 4.21, and let `Y` be a diagonalizable subgroup of `X`. Suppose
`ω¹_{Y₀/S₀}` finite locally free and `S₀` affine.[^N.D.E-III-129] The set of subgroups of `X` conjugate to `Y` by a
section of `X` over `S` inducing the unit section of `X_J` is isomorphic to*

<!-- label: III.III.4.33 -->

```text
E = Γ(S₀, [Lie(X₀/S₀) / Lie(X₀/S₀)^{ad(Y₀)}] ⊗_{Γ(S₀, O_{S₀})} Γ(S₀, J))
```

*[^N.D.E-III-130] that is, isomorphic to `L₀^X(Y₀)/H⁰(Y₀, L₀^X)`.*

Indeed, one writes by I 4.7.3 (cf. 2.13):

```text
Lie(X₀/S₀) = Lie(X₀/S₀)^{ad(Y₀)} ⊕ R.
```

Since `Y₀` is commutative one has `Lie(Y₀/S₀) ⊂ Lie(X₀/S₀)^{ad(Y₀)}`, hence

```text
F₀ = [Lie(X₀/S₀)^{ad(Y₀)} / Lie(Y₀/S₀)] ⊗ J ⊕ R ⊗ J,
F₀^{ad(Y₀)} = [Lie(X₀/S₀)^{ad(Y₀)} / Lie(Y₀/S₀)] ⊗ J.
```

<!-- original page 158 -->

By 4.32, one has therefore `E ≃ Γ(S₀, R ⊗ J)`. Returning to the definition of `R`, one is done.

**Corollary 4.34.** *Let `S, I, J` and `X` be as in 4.21, and let `Y` be a diagonalizable subgroup of `X`. Suppose
`ω¹_{Y₀/S₀}` finite locally free and `S₀` affine.[^N.D.E-III-131] If `x ∈ X(S)` induces the unit section of `X_J` and
normalizes `Y`, then it centralizes `Y`.*

<!-- label: III.III.4.34 -->

This results immediately from comparison of the preceding corollary and 2.14. Indeed, 4.33 shows that the elements of
`C⁰(Y₀, L₀^X)` which globally preserve `Y` are the elements of `H⁰(Y₀, L₀^X)`, and one has seen in 2.14 that these are
precisely those which act trivially on the canonical immersion `Y → X`.

**4.35.** Let us return to the general situation of 4.21 and suppose `Y_J` smooth over `S_J`. Then, by 4.25 (ii), one
has an exact sequence of `Y₀`-`O_{S₀}`-modules:

```text
(∗)    0 ⟶ Lie(Y₀/S₀) ⟶ Lie(X₀/S₀) ⟶ n_{Y₀/X₀}^∨ ⟶ 0
```

and they are finite locally free `O_{S₀}`-modules.

On the other hand, by SGA 1, II 4.10, every subscheme `Y` of `X` lifting `Y_J` and flat over `S` will be smooth over
`S`.[^N.D.E-III-132] Suppose moreover `S₀` and `Y_J` affine. Then, since `n_{Y₀/X₀}^∨` is a locally free
`O_{S₀}`-module, the sequence `(∗)` remains exact when one applies `⊗_{O_{S₀}} J` to it, and then takes the inverse
image on `Y₀ⁿ`, and as the `Y₀ⁿ` are affine, one therefore obtains an exact sequence of complexes of abelian groups:

```text
0 ⟶ C*(Y₀, L₀^Y) ⟶ C*(Y₀, L₀^X) ──d*──► C*(Y₀, N₀) ⟶ 0
```

and in particular, a commutative diagram with exact rows

```text
0 ⟶ C¹(Y₀, L₀^Y) ⟶ C¹(Y₀, L₀^X) ──d¹──► C¹(Y₀, N₀) ⟶ 0
        │ ∂                │ ∂                │ ∂
        ↓                  ↓                  ↓
0 ⟶ C²(Y₀, L₀^Y) ⟶ C²(Y₀, L₀^X) ──d²──► C²(Y₀, N₀) ⟶ 0.
```

Let now `Y, Y′` be two subgroups of `X` lifting `Y_J` and flat, hence smooth, over `S`. As `Y_J` is affine, then, by
0.15, `Y` and `Y′` are isomorphic as schemes extending `Y_J`, i.e. there exists an isomorphism of `S`-schemes

```text
f : Y ⥲ Y′
```

<!-- original page 159 -->

inducing the identity on `Y_J`. On the one hand, by 1.2.4, `f` defines an element `a` of `C¹(Y₀, L₀^X)` such that
`f(y) = a(y₀)y`, for every `y ∈ Y(S′)`, `S′ → S`, and by 4.27 (i), one has

```text
d¹(a) = d(Y, Y′).
```

Moreover, since `Y, Y′` are subgroups of `X`, the above element belongs to `Z¹(Y₀, N₀)` (cf. 4.21). Then `∂a` is an
element of `Z²(Y₀, L₀^Y)` whose image `∂̄a` in `H²(Y₀, L₀^Y)` depends only on the class `d̄(Y, Y′) ∈ H¹(Y₀, N₀)`; this
being the definition of the connecting map `∂¹ : H¹(Y₀, N₀) → H²(Y₀, L₀^Y)`, one has therefore:

```text
∂¹(d̄(Y, Y′)) = ∂̄a.
```

On the other hand, let us transport by `f` the group structure of `Y′` and let `Y₁` be the group obtained (which thus
has `Y` as underlying scheme), that is, the group law `μ₁` of `Y₁` is defined by: for every `S′ → S` and `x, y ∈ Y(S′)`,

```text
μ₁(x, y) = f⁻¹(f(x)f(y)).
```

By 3.5.1, `Y₁` defines a cocycle `δ(Y, Y₁) ∈ Z²(Y₀, Lie(Y₀/S₀))` such that, for every `S′ → S` and `x, y ∈ Y(S′)`, one
has

```text
δ(Y, Y₁)(x₀, y₀) xy = μ₁(x, y) = f⁻¹(f(x)f(y)).
```

Set `b = δ(Y, Y₁)`. For every `S′ → S` and `x, y ∈ Y(S′)`, one has `(b(x₀, y₀)xy)₀ = x₀y₀` and therefore one obtains
that `f(b(x₀, y₀)xy)` equals, on the one hand, `a(x₀y₀)b(x₀, y₀)xy` and, on the other hand,

```text
f(x)f(y) = a(x₀)x a(y₀)y = a(x₀) Ad(x₀)(a(y₀)) xy.
```

Comparing the two expressions, one obtains that `b(x₀, y₀)` equals

```text
a(x₀y₀)⁻¹ a(x₀) Ad(x₀)(a(y₀)) = Ad(x₀)(a(y₀)) − a(x₀y₀) + a(x₀) = (∂a)(x₀, y₀),
```

i.e. `δ(Y, Y₁) = ∂a`. We have thus obtained:

**Proposition 4.35.1.**[^N.D.E-III-132] *Under the hypotheses of 4.21, suppose moreover `S₀` affine and `Y_J` smooth
over `S_J` and affine. Let `Y, Y′` be two subgroups of `X` lifting `Y_J` and flat (hence smooth) over `S`, let
`f : Y ⥲ Y′` be an isomorphism of `S`-schemes inducing the identity on `Y_J`, denote by `Y₁` the group obtained by
transporting via `f` the group structure of `Y′`. Then one has*

<!-- label: III.III.4.35.1 -->

```text
∂¹(d̄(Y, Y′)) = δ(Y, Y₁).
```

**Proposition 4.36.** *Under the hypotheses of 4.21, suppose moreover `Y_J` smooth over `S_J` and `S₀` affine. The set
of sub-`S`-groups `Y` of `X` flat (or smooth) over `S`, reducing to `Y_J`, modulo conjugation by sections of `X` over
`S` inducing the unit section of `X_J`, is either empty, or a principal homogeneous set under the group*

<!-- label: III.III.4.36 -->

```text
H¹(Y₀, [Lie(X₀/S₀)/Lie(Y₀/S₀)] ⊗_{O_{S₀}} J).
```

<!-- original page 160 -->

It suffices for us to verify that Corollary 4.29 applies, that is, that

```text
d⁰ : Hom_{O_{S₀}}(ω¹_{X₀/S₀}, J) ⟶ Hom_{O_{S₀}}(n_{Y₀/X₀}, J)
```

is surjective. Now this follows from the fact that the sequence `(+)` of 4.25 (ii) is split, `S₀` being
affine.[^N.D.E-III-133]

Let us finally state a corollary common to 4.21 and 4.36, which will in fact be the only form under which we shall use
in what follows the general results of this section.[^N.D.E-III-134]

**Corollary 4.37.** *Let `S` be a scheme and `S₀` the closed subscheme defined by a nilpotent ideal `I`. Let `X` be an
`S`-group smooth over `S`, and `Y₀` a sub-`S₀`-group of `X₀`, flat over `S₀`.*

<!-- label: III.III.4.37 -->

*(i) If `S₀` is affine, `Y₀` smooth over `S₀`, and if*

```text
H¹(Y₀, [Lie(X₀/S₀)/Lie(Y₀/S₀)] ⊗_{O_{S₀}} Iⁿ⁺¹/Iⁿ⁺²) = 0
```

*for every `n ≥ 0`, two sub-`S`-groups of `X`, flat (or smooth) over `S`, reducing to `Y₀`, are conjugate by a section
of `X` over `S` inducing the unit section of `X₀`.*

*(ii) If `Y₀` is affine and of finite presentation and if[^N.D.E-III-135]*

```text
H²(Y₀, n_{Y₀/X₀}^∨ ⊗_{O_{S₀}} Iⁿ⁺¹/Iⁿ⁺²) = 0
```

*for every `n ≥ 0`, there exists a sub-`S`-group of `X`, flat over `S`, reducing to `Y₀`.*

**4.38.** It remains to relate the three constructions which we have made in this Exposé. To avoid inessential
complications, we shall place ourselves in the following situation: `S₀` is the spectrum of a field `k`, `S` is the
spectrum of the dual numbers `D(k)`, `G` is an `S`-group smooth over `S`, `K` a sub-`S`-group, smooth over `S` and
affine.

<!-- original page 161 -->

[^N.D.E-III-136] Denote `g₀ = Lie G₀` (which here equals `Γ(S₀, Lie G₀) = Lie(G₀/S₀)(S₀)`) and `k₀ = Lie K₀`. One has an
exact sequence of `k`-vector spaces[^N.D.E-III-137]:

```text
0 ⟶ k₀ ──i──► g₀ ──d──► n_{K₀/G₀}^∨ ⟶ 0,
```

giving rise to an exact cohomology sequence:

```text
0 ⟶ H⁰(K₀, k₀) ──i⁰──► H⁰(K₀, g₀) ──d⁰──► H⁰(K₀, g₀/k₀)
   ──∂⁰──► H¹(K₀, k₀) ──i¹──► H¹(K₀, g₀) ──d¹──► H¹(K₀, n_{K₀/G₀}^∨) ──∂¹──► H²(K₀, k₀).
```

Now these various groups all have a geometric meaning.

a) `H⁰(K₀, k₀) = Lie Centr(K₀)`[^N.D.E-III-138] by II 5.2.3.

b) `H⁰(K₀, g₀) = Lie Centr_{G₀}(K₀)`[^N.D.E-III-138] (idem).

c) `H⁰(K₀, g₀/k₀) = Lie Norm_{G₀}(K₀)/k₀`[^N.D.E-III-138] (idem).

d) `H¹(K₀, k₀) = Lie Aut_{S₀-gr.}(K₀) / Im(k₀)`, where `Im(k₀)` denotes the image of `k₀` by the morphism `Lie(Int₀)`
deduced from `Int₀ : K₀ → Aut_{S₀-gr.}(K₀)`. Indeed, it follows from 2.1 (ii), applied to `Y = X = K` and
`f₀ = id_{K₀}`, that `Z¹(K₀, k₀)` is the group of infinitesimal automorphisms of the `S₀`-group `K₀`, and that
`H¹(K₀, k₀)` is obtained by quotienting by inner infinitesimal automorphisms, i.e. by the image of `k₀`. Moreover, by II
4.2.2, one also has `Z¹(K₀, k₀) = Lie Aut_{S₀-gr.}(K₀)`[^N.D.E-III-139].

<!-- original page 162 -->

e) `H¹(K₀, g₀)` is, by 2.1 (ii), the group of deviations between homomorphisms `K → G` extending the canonical immersion
`i₀ : K₀ → G₀`, modulo the deviations obtained by the action of the inner automorphisms of `G` defined by elements of
`G(S)` giving the unit of `G(S₀)` (that is, elements of `g₀`).

f) `H¹(K₀, n_{K₀/G₀}^∨)` is, by 4.36, the group of deviations between subgroups `K′` of `G` extending `K₀` and flat over
`S` (hence smooth over `S`, cf. SGA 1, II 4.10), modulo the deviations obtained by the action of the inner automorphisms
of `G` constructed as previously.

g) `H²(K₀, k₀)` is, by 3.5 (ii), the group of deviations between group structures on `K` extending that of `K₀`, modulo
the `S`-automorphisms of `K` inducing the identity on `K₀`.

We now propose to show how one can make explicit the six morphisms of the preceding exact sequence in the geometric
interpretation we have just given.

1. `i⁰` and `d⁰` are nothing other than the morphisms obtained by passage to the Lie algebra (then by passage to the
    quotient for `d⁰`), starting from the canonical monomorphisms:

```text
Centr(K₀) ⟶ Centr_{G₀}(K₀) ⟶ Norm_{G₀}(K₀).
```

This indeed results immediately from the definition of the identifications (a), (b), and (c).

1. One constructs `∂⁰` as follows. Let `x̄ ∈ Lie Norm_{G₀}(K₀)/k₀`. Lift it to `x ∈ Lie Norm_{G₀}(K₀) ⊂ Norm_G(K)(S)`.
    Then `Int(x)` defines an automorphism of `K` inducing the identity on `K₀`, hence an element of
    `Lie Aut_{S₀-gr.}(K₀)`. Denote `Int(x̄)` the image of this element in `Lie Aut_{S₀-gr.}(K₀)/Im(k₀)`. Then one has:

<!-- original page 163 -->

```text
(∗)    ∂⁰(x̄) = −Int(x̄) = Int(x̄⁻¹).
```

Indeed, let us compute the element of `Lie Aut_{S₀-gr.}(K₀)` defined by `Int(x)`. It will correspond by definition to an
element `a` of `Z¹(K₀, k₀)` such that

```text
x y x⁻¹ = a(y₀) y,    for every y ∈ K(S′), S′ → S.
```

But this can also be written `a(y₀) = xyx⁻¹y⁻¹ = x − Ad(y)x = −∂(x)(y₀)`, whence `a = −∂(x)`.

[^N.D.E-III-140] On the other hand, the image of `x ∈ Lie Norm_{G₀}(K₀) ⊂ g₀` by `∂` is an element of `Z¹(K₀, k₀)`,
whose image `∂̄(x)` in `H¹(K₀, k₀)` depends only on `x̄`, and by definition of the connecting map `∂⁰`, one has

```text
∂⁰(x̄) = ∂̄(x);
```

combined with the equality `a = −∂(x)`, this proves `(∗)`.

3)[^N.D.E-III-141] Denote `i : K → G` the canonical immersion. Let `ū` be an element of `H¹(K₀, k₀)`, image of a

```text
u ∈ Lie Aut_{S₀-gr.}(K₀) ⊂ Aut_{S-gr.}(K).
```

Then one has:

```text
(∗∗)    i¹(ū) = d̄(i, i ∘ u),
```

where `d̄(i, i ∘ u)` is the class defined in 2.1.1.

Indeed, `u` is the image of an element `v ∈ Z¹(K₀, k₀)` such that `u(y) = v(y₀)y`, and `i¹(ū)` is the image in
`H¹(K₀, g₀)` of the cocycle `i ∘ v ∈ Z¹(K₀, g₀)`.

Now, since `i` is a morphism of groups, the equality `u(y) = v(y₀)y` entails `iu(y) = iv(y₀)i(y)`. It follows that
`i ∘ v = d(i, i ∘ u)`, whence `(∗∗)`.

1. Let `i′ : K → G` be a morphism of groups lifting `i₀`, let `d(i, i′)` be the class defined in 2.1.1, and let
    `d(K, i′(K)) ∈ C¹(K₀, n_{K₀/X₀})` be the deviation defined in 4.5.1; by 4.21, `d(K, i′(K))` belongs to
    `Z¹(K₀, n_{K₀/X₀})`. Denote `d̄(K, i′(K))` its image in `H¹(K₀, n_{K₀/X₀})`. Then, by 4.27 (i), one has:

<!-- original page 164 -->

```text
(†)    d¹(d̄(i, i′)) = d̄(K, i′(K)).
```

1. Finally, let `K′` be a subgroup of `G` lifting `K₀` and flat, hence smooth, over `S`. We have supposed that `K₀` is
    affine. Then one knows that `K` and `K′` are isomorphic as schemes extending `K₀` (cf. 0.15), hence there exists an
    isomorphism of `S`-schemes

```text
f : K ⥲ K′
```

inducing the identity on `K₀`. Let us transport by `f` the group structure of `K′` and let `K₁` be the group obtained
(which thus has `K` as underlying scheme), that is, the group law `μ₁` of `K₁` is defined by: for every `S′ → S` and
`x, y ∈ K(S′)`,

```text
μ₁(x, y) = f⁻¹(f(x)f(y)).
```

[^N.D.E-III-142] By 3.5.1, `K₁` defines a cocycle `δ(K, K₁) ∈ Z²(K₀, k₀)` such that, for every `S′ → S` and
`x, y ∈ K(S′)`, one has

```text
δ(K, K₁)(x₀, y₀) xy = μ₁(x, y) = f⁻¹(f(x)f(y)).
```

Then, by 4.35.1, one has:

```text
(‡)    ∂¹(d̄(K, K′)) = δ̄(K, K₁).
```

## Bibliography

[^N.D.E-III-143]

[BAlg] N. Bourbaki, *Algèbre*, Chap. I–III, Hermann, 1970.

[BAC] N. Bourbaki, *Algèbre commutative*, Chap. I–IV, Masson, 1985.

[DG70] M. Demazure, P. Gabriel, *Groupes algébriques*, Masson & North-Holland, 1970.

[Fr64] P. Freyd, *Abelian categories*, Harper and Row, 1964.

<!-- TRANSLATOR NOTE: The footnote bodies for N.D.E-III-65 through N.D.E-III-143 follow the same numbering scheme as the original; they record editorial additions, corrections, and clarifications. They are listed below for reference. -->

<!-- LEDGER DELTA — Exposé III — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| extension infinitésimale | infinitesimal extension | Title term. |
| déformation infinitésimale | infinitesimal deformation | Standard. |
| déviation | deviation | The `d(Y, Y′)` / `d(μ, μ′)` element measuring difference of two liftings; preserve. |
| obstruction | obstruction | Standard. |
| classe d'obstruction | obstruction class | Standard. |
| formellement principal homogène | formally principal homogeneous | Standard for pseudo-torsors. |
| pseudo-torseur | pseudo-torsor | Synonym of "formally principal homogeneous"; preserve loanword. |
| somme amalgamée | amalgamated sum | Standard category-theoretic pushout under a span. |
| faisceau conormal | conormal sheaf | `N_{Y/X} = I_Y/I_Y²`. |
| nY₀/X₀ | nY₀/X₀ | The pulled-back conormal at the unit section, `ε₀*(N_{Y₀/X₀})`. |
| localement intersection complète | locally complete intersection | Per SGA 6, VII 1.4. |
| immersion régulière | regular immersion | Per SGA 6, VII / EGA IV₄. |
| complexe de Koszul | Koszul complex | Standard. |
| morphisme régulier | regular morphism | Of a Koszul map; standard. |
| critère fondamental de platitude | fundamental criterion of flatness | Per [BAC], § III.5, th. 1 / SGA 1 IV 5.5. |
| lemme de Nakayama nilpotent | nilpotent Nakayama lemma | Standard. |
| loi de composition admissible | admissible composition law | Per § 1.3.2. |
| loi de composition associative | associative composition law | Standard. |
| loi de groupe | group law | Standard. |
| morphisme de descente | descent morphism | Per Exp. IV. |
| couvrant pour (fpqc) | covering for (fpqc) | Standard. |
| section unité | unit section | Standard. |
| translation à gauche / droite | left / right translation | Standard. |
| automorphisme intérieur | inner automorphism | Standard. |
| représentation adjointe | adjoint representation | Standard. |
| schéma des nombres duaux | scheme of dual numbers | Per Exp. II 2.1; `D(k)`. |
| cohomologie de Hochschild | Hochschild cohomology | Per § 1 / 4.5 N.D.E.; distinguished from coherent cohomology `R¹Γ`. |
| différentielle | differential | Standard (of a complex or of an algebra). |
| application bord | connecting map | For long exact cohomology sequences. |
| transporter (la structure) | transport (the structure) | As in transport-by-isomorphism. |
| centralisateur / normalisateur | centralizer / normalizer | American spelling. |
| algèbre de Lie | Lie algebra | Standard. |
| algébriquement clos | algebraically closed | Standard. |
| de présentation finie | of finite presentation | Per intro § 6; preserve. |
| Bible | Bible | Chevalley Seminar 1956/58; italicise. |
-->

[^N.D.E-III-65]: N.D.E.: We have corrected the original by suppressing the inadequate reference to an exercise of
    Bourbaki on semigroups (cf. [BAlg], § I.2, Exercises 9–13) and by indicating the role of left and right
    translations; see the following N.D.E.

[^N.D.E-III-66]: N.D.E.: Let `E` be a non-empty set equipped with an associative composition law, such that every left
    translation `ℓ_x` is bijective; fix `x₀ ∈ E`. There exists a unique `e ∈ E` such that `x₀ · e = x₀`;
    then `x₀ · e · x = x₀ · x` entails `e · x = x`, for every `x ∈ E`. On the other hand, for every `x`
    there exists a unique `x′` such that `x · x′ = e`. Suppose moreover that there exists `b ∈ E` such that
    the right translation `r_b` is injective. Then, for every `x`, the equality `x · e · b = x · b` gives
    `x · e = x` (i.e. `e` is a neutral element), and `x · x′ · x = x = x · e` entails `x′ · x = e`, i.e.
    `x′` is the inverse of `x` from the left and the right, hence `E` is a group. Note that the hypothesis
    "`r_b` injective" is necessary: on every set `E` one can define a composition law by `x · y = y`, for
    all `x, y ∈ E`; then every left translation is the identity (whence the associativity of the law), but
    for every `y` one has `r_y(E) = {y}`, hence `E` is not a group if `|E| > 1`.

[^N.D.E-III-67]: N.D.E.: Since `X` and `X₀` have the same underlying topological space and `t₀` is an automorphism, `t`
    is a homeomorphism, hence an affine morphism, cf. Exp. VI_B, 2.9.1 or EGA IV₄, 18.12.7.1. It thus
    suffices to see that if `J` is a nilpotent ideal of a ring `Λ`, and `φ : A → B` a morphism of
    `Λ`-algebras, with `B` flat over `Λ`, such that `φ ⊗_Λ (Λ/J)` is bijective, then `φ` is bijective. By
    the "nilpotent Nakayama lemma", `φ` is surjective; moreover, `B` being flat over `Λ`, one also has
    `Ker(φ) ⊗_Λ (Λ/J) = 0`, whence `Ker(φ) = 0`, hence `φ` is bijective.

[^N.D.E-III-68]: N.D.E.: Indeed, by the proof of 0.7, the `S`-endomorphisms of `X` inducing the identity on `X_J` are
    the automorphisms `m · id_X`, for `m` ranging over `M(X) = Hom_S(X, M)` (for every `S′ → S` and
    `x ∈ X(S′)`, one has `(m · id_X)(x) = m(x) · x`). Now, by the proof of 3.1, each `m : X → M` factors in
    a unique manner through a morphism `h` from `Y = X⁺` to `M`, and therefore `m · id_X` is the
    automorphism `u_h` introduced in 1.3.1. The lemma then follows from the definition of equivalence, cf.
    1.3.4 and 1.3.5.

[^N.D.E-III-69]: N.D.E.: We have added what follows.

[^N.D.E-III-70]: N.D.E.: We have added this remark, analogue of 4.5.1, to introduce the notation `δ(μ, μ′)` (or
    `δ(X, X′)`), used in 4.38; consequently, we have also added in 3.5 (ii) above the part concerning `E`
    itself.

[^N.D.E-III-71]: N.D.E.: We have conformed to the sign conventions of the original, in order to have in 4.38 (5) the
    equality `∂¹d̄(X, X′) = δ̄(X, X′)` (see also N.D.E. (54)).

[^N.D.E-III-72]: N.D.E.: This is used in XXIV, 1.13.

[^N.D.E-III-73]: N.D.E.: Indeed, `Aut_{S₀-gr.}(X₀)` acts by group automorphisms on the abelian group
    `H²(X₀, Lie(X₀/S₀))`, hence the orbit of `0` is the singleton `{0}`; consequently the quotient set is a
    singleton if and only if `H²(X₀, Lie(X₀/S₀)) = {0}`.

[^N.D.E-III-74]: N.D.E.: One has `Coker(j) = B′ ⊔_Q 0 = A ⊔_{A′} 0 = A′′`, and one sees that `Ker(j) ≃ Ker(i) = 0` by
    reasoning "as if `C` were a category of modules"; for a proof solely in terms of arrows, see for
    example [Fr64], Th. 2.5.4 (∗).

[^N.D.E-III-75]: N.D.E.: In what follows, we have replaced `A` by `B′` and detailed the end of the argument.

[^N.D.E-III-76]: N.D.E.: We have rewritten the statement to be exactly in the setting of the application made of it in
    4.3; moreover, we have detailed the proof, following the indications given by M. Demazure.

[^N.D.E-III-77]: N.D.E.: To lighten the statement, we have added here the hypothesis that `G` be quasi-coherent, and
    deferred to the proof the remark that this hypothesis is automatically satisfied; we have detailed the
    proof accordingly.

[^N.D.E-III-78]: N.D.E.: See also [BAC], § III.5, th. 1.

[^N.D.E-III-79]: N.D.E.: We have detailed what follows and added Corollary 4.3.1. Recall that "pseudo-torsor" is
    synonymous with "formally principal homogeneous".

[^N.D.E-III-80]: N.D.E.: We have added this complement, useful to prove point (ii) of Proposition 4.8.

[^N.D.E-III-81]: N.D.E.: We have added the numbering 4.5.0 to mark the return to the original.

[^N.D.E-III-82]: N.D.E.: We have corrected the following sentence.

[^N.D.E-III-83]: N.D.E.: We have detailed what follows.

[^N.D.E-III-84]: N.D.E.: Here, we have denoted `R¹Γ(Y₀, A₀)` the "coherent" cohomology group `H¹(Y₀, A₀)` of the
    `O_{Y₀}`-module `A₀`, in order to distinguish it from the "Hochschild" cohomology groups `Hⁱ(Y₀, M₀)`
    (`Y₀` an `S₀`-group, `M₀` an `O_{S₀}`-module) which will be considered starting from 4.16.

[^N.D.E-III-85]: N.D.E.: We have placed here this remark, which replaces Remark 4.7 of the original.

[^N.D.E-III-86]: N.D.E.: We have corrected "closed subschemes" to "subschemes".

[^N.D.E-III-87]: N.D.E.: We have kept, for the record, Remark 4.6 of the original, in which the definition of "locally
    complete intersection" does not appear. We have added next the "good" definition, drawn from SGA 6, VII
    1.4 (which replaces that of EGA IV₄, 16.9.2), and the proof of the three results stated in the remark.

[^N.D.E-III-88]: N.D.E.: In order to prove the results stated in Remark 4.6, we have added Lemmas 4.6.3, 4.6.4 and
    Proposition 4.6.5, as well as Remark 4.6.6.

[^N.D.E-III-89]: N.D.E.: We have inserted here this remark, used in the following proposition; it appeared in 4.10 of
    the original.

[^N.D.E-III-90]: N.D.E.: In the original, this was indicated in Remark 4.10, under the additional hypothesis that `Y′`
    was locally complete intersection in `X′`. This hypothesis figured also, consequently, in statements
    4.12–4.14; it seems in fact superfluous, and we have suppressed it from the above-mentioned statements.

[^N.D.E-III-91]: N.D.E.: We have suppressed the hypothesis that `I` be nilpotent, which appears superfluous (cf. the
    proof).

[^N.D.E-III-92]: N.D.E.: See also 4.27 further on.

[^N.D.E-III-93]: N.D.E.: See also EGA IV₄, 16.4.21. Recall that if `U` is an affine open of `X` such that `Y ∩ U` is
    defined by the ideal `I` of `A = O_X(U)`, if one denotes by `d` the differential `A → Γ(U, Ω¹_{X/S})`,
    and if `x ∈ I`, then `D(x + I²)` is the element `d(x) ⊗ 1` of `Γ(U, Ω¹_{X/S}) ⊗_A (A/I)`.

[^N.D.E-III-94]: N.D.E.: We have done these verifications below.

[^N.D.E-III-95]: N.D.E.: On the one hand, we have suppressed the hypothesis that `I` be nilpotent, i.e. that `X₀` have
    the same underlying topological space as `X`; on the other hand, we have detailed the following
    sentence.

[^N.D.E-III-96]: N.D.E.: We have detailed what follows.

[^N.D.E-III-97]: N.D.E.: We have added what follows.

[^N.D.E-III-98]: N.D.E.: Cf. N.D.E. (93).

[^N.D.E-III-99]: N.D.E.: From 4.17 on, we shall apply this to the case where `X` is an `S`-group, `g : X ×_S X → X` the
    multiplication, `Y` a subscheme of `X` such that `Y_J` is a subgroup of `X_J`, `Y′ = Y ×_S Y`, and to
    the two morphisms `Y³ → X²` which send `(y₁, y₂, y₃)` to `(y₁y₂, y₃)`, resp. `(y₁, y₂y₃)`. In this
    case, the comparison of the above obstructions will show that the obstruction to `Y` being a subgroup
    of `X` resides in a certain cohomology group (Hochschild) `H²(Y₀, N₀)`.

[^N.D.E-III-100]: N.D.E.: We have suppressed the hypothesis "`Y₀′` locally complete intersection in `X₀′`", superfluous
    by 4.8.0; on the other hand, we have added that `a_{g₀}(f₀)` is "functorial in `T`", this playing a
    crucial role in the proof of 4.17.

[^N.D.E-III-101]: N.D.E.: We have detailed the proof, to make visible the "functoriality in `T`" of `a_{g₀}`.

[^N.D.E-III-102]: N.D.E.: The situation will simplify from 4.16 on: one will restrict to schemes flat over `S`, `Y` will
    be a flat `S`-group and `Y′ = Y ×_S Y`; one will then obtain `S₀`-functors `N₀` and `N₀′`.

[^N.D.E-III-103]: N.D.E.: We have added this remark, used in the proof of 4.17.

[^N.D.E-III-104]: N.D.E.: We have kept the notation of the original, denoting `f : A′ → C` and `g : A → A′` the
    morphisms of rings corresponding to `f : T → X′` and `g : X′ → X`. This explains the formula
    `c(X, Y, g ∘ f)(x̄ ⊗ 1) = f(g(x))`, for `x ∈ I_Y`.

[^N.D.E-III-105]: N.D.E.: We have added in the statement the hypothesis that `Y` be locally of finite presentation over
    `S`, and have given the following proof, more direct than the one sketched in the original. To be
    complete, let us also detail the latter. As in the proof given above, one reduces first to the case
    where `S = Spec(k)`, `k` being an algebraically closed field. By EGA IV₄, 16.9.10 and 19.3.2, it
    suffices to see that, for every `y ∈ Y`, the completion of the local ring `O_{Y,y}` is the quotient of
    a complete noetherian local ring by a regular sequence. By loc. cit., 19.3.3, the set of `y ∈ Y`
    satisfying this property is an open `U` of `Y`; since `Y` is of finite type over `k`, it suffices to
    show that `U` contains every closed point. Since `Y` is a `k`-group it suffices, by a translation
    argument, to show that the property is true for the completion of `O_{Y,e}`, that is, for the "formal
    group" `Ŷ` corresponding to `Y` (cf. Exp. VII_B). Now, since `X` is smooth, the affine algebra `A(X̂)`
    is an algebra of formal power series `k[[X₁, ..., X_n]]`, and one concludes with the help of the
    Dieudonné structure theorem which shows that `A(Ŷ)` is isomorphic to a quotient
    `k[[X₁, ..., X_{r+s}]]/(X₁^{p^{n₁}}, ..., X_r^{p^{n_r}})`, where `p` is the characteristic exponent of
    `k` and `r + s ≤ n`, cf. VII_B, Remark 5.5.2 (b).

[^N.D.E-III-106]: N.D.E.: We have reorganized 4.16 by regrouping there, on the one hand, the hypotheses stated at the
    end of 4.15 and, on the other hand, the definition of the obstruction `DY`.

[^N.D.E-III-107]: N.D.E.: We have corrected the original by adding "flat".

[^N.D.E-III-108]: N.D.E.: See 4.25 further on.

[^N.D.E-III-109]: N.D.E.: We have modified 4.17 and 4.18 taking into account the additions made in 4.16.

[^N.D.E-III-110]: N.D.E.: In the original, one finds `DY′ − DY = −∂d(Y, Y′)`, but their `∂` is the opposite of the
    differential `∂¹` defined in I, 5.1.

[^N.D.E-III-111]: N.D.E.: We have slightly modified the notations, and detailed the beginning of the argument.

[^N.D.E-III-112]: N.D.E.: We have replaced `a, b` by `ab, b` to make visible that `V(P)` comes by inverse image on `Y₀²`
    from the multiplication morphism `V_{Y₀} ×_{S₀} V_{Y₀} → V_{Y₀}`.

[^N.D.E-III-113]: N.D.E.: We have changed the signs to make them compatible with I 5.1.

[^N.D.E-III-114]: N.D.E.: We have detailed the original in what follows.

[^N.D.E-III-115]: N.D.E.: We have suppressed the hypothesis that `I` be nilpotent, which appears superfluous.

[^N.D.E-III-116]: N.D.E.: The question of whether the preceding set, modulo conjugation by the `x ∈ X(S)` inducing the
    unit of `X(S_J)`, is principal homogeneous under `H¹(Y₀, N₀)`, occupies n°s 4.23 to 4.36.

[^N.D.E-III-117]: N.D.E.: We have corrected `∂DY′` to `DY′`.

[^N.D.E-III-118]: N.D.E.: Cf. N.D.E. (110).

[^N.D.E-III-119]: N.D.E.: We have detailed what precedes; this shows that the following isomorphism is valid without
    flatness hypothesis; on the other hand, since 4.16, we have restricted ourselves to `S`-schemes
    `f : T → S` flat over `S` to ensure that the group `Hom_{O_T}(n_{Y₀/X₀} ⊗_{O_{S₀}} O_{T₀}, JO_T)`, in
    which the obstruction `c(X, Y, f)` resides, coincides with `N₀(T₀)` (cf. the end of 4.16).

[^N.D.E-III-120]: N.D.E.: With the notation of I 5.3, assuming `Y₀` affine over `S₀`.

[^N.D.E-III-121]: N.D.E.: We have replaced `Z¹(Y₀, N₀)` by `B¹(Y₀, N₀)`, since the proof shows that `Γ` is a subgroup of
    `B¹(Y₀, N₀)`, cf. 4.27–4.29.

[^N.D.E-III-122]: N.D.E.: We have detailed the proof, taking into account the additions made in Exp. I, § 6.8.

[^N.D.E-III-123]: N.D.E.: We have detailed the original, to make visible that one has an exact sequence of
    `Y₀`-`O_{S₀}`-modules.

[^N.D.E-III-124]: N.D.E.: This results from the definition of `d : n_{Y₀/X₀} → Ω¹_{X₀/S₀}` (cf. 4.25) and from that of
    `v_{i_{Y₀}}` (cf. 4.8).

[^N.D.E-III-125]: N.D.E.: We have added point (i) below, which will be useful in 4.35.1 and then in 4.38 (4) and (5).

[^N.D.E-III-126]: N.D.E.: Recall that `L′_X = ∏_{S₀/S} L₀^X`.

[^N.D.E-III-127]: N.D.E.: We have corrected `Lie(Y₀/S₀)` to `ω¹_{Y₀/S₀}`.

[^N.D.E-III-128]: N.D.E.: We have detailed the original in what follows.

[^N.D.E-III-129]: N.D.E.: We have added the hypothesis on `ω¹_{Y₀/S₀}` and replaced the hypothesis "`S` affine" by "`S₀`
    affine".

[^N.D.E-III-130]: N.D.E.: We have added what follows, cf. 4.34.

[^N.D.E-III-131]: N.D.E.: Cf. N.D.E. (129).

[^N.D.E-III-132]: N.D.E.: We have added what follows and Proposition 4.35.1, implicit in the original, cf. 4.38 (5).

[^N.D.E-III-133]: N.D.E.: This also follows from the proof of 4.32.

[^N.D.E-III-134]: N.D.E.: For example, 4.37 is used in Exposé IX to prove statements 3.2 bis and 3.6 bis.

[^N.D.E-III-135]: N.D.E.: We have replaced `Hom_{O_{S₀}}(n_{Y₀/X₀}, Iⁿ⁺¹/Iⁿ⁺²)` by `n_{Y₀/X₀}^∨ ⊗_{O_{S₀}} Iⁿ⁺¹/Iⁿ⁺²`,
    in accordance with Remark 4.22.

[^N.D.E-III-136]: N.D.E.: We have slightly modified the original in what follows. In particular, we have replaced `X` by
    `G` and `Y` by `K`, and we have denoted `g₀` and `k₀` their Lie algebras. On the other hand, we have
    written explicitly `Hⁱ(K₀, ·)` instead of the abbreviation `Hⁱ(·)` of the original.

[^N.D.E-III-137]: N.D.E.: Equipped with the adjoint action of `K₀`.

[^N.D.E-III-138]: N.D.E.: Since the formation of centralizers and normalizers commutes with base change (cf. I 2.3.3.1),
    we have written `Centr(K₀)` instead of `Centr(K)₀` in the original, and similarly `Centr_{G₀}(K₀)` and
    `Norm_{G₀}(K₀)` instead of `Centr_G(K)₀` and `Norm_G(K)₀`.

[^N.D.E-III-139]: N.D.E.: And this is the Lie algebra `Der_k(k₀)` of derivations of `k₀`; hence `H¹(K₀, k₀)` is the
    quotient of `Der_k(k₀)` by inner derivations (i.e. by the image of `ad : k₀ → Der_k(k₀)`).

[^N.D.E-III-140]: N.D.E.: We have added the following sentence.

[^N.D.E-III-141]: N.D.E.: We have detailed the original in what follows, and in `(∗∗)` we have corrected `u ∘ i` to
    `i ∘ u`.

[^N.D.E-III-142]: N.D.E.: We have modified the original in what follows, taking into account the additions made in 3.5.1
    and 4.35.1.

[^N.D.E-III-143]: N.D.E.: Additional references cited in this Exposé.
