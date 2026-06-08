# Exposé III. Infinitesimal extensions

<!-- label: III.III -->

*by M. Demazure*

<!-- original page 83 -->

[^N.D.E-III-0] In this Exposé, we place ourselves in the following general situation. We have a scheme $S$ and a
coherent nilpotent ideal $I$ on $S$. We denote by $S_{n}$ the closed subscheme of $S$ defined by the ideal $I^{n+1}$ ($n
\geq 0$). In particular $S_{0}$ is defined by $I$. Since $I$ is nilpotent, $S_{n}$ is equal to $S$ for $n$ large enough,
and the `Sᵢ` have the same underlying topological space. A typical example of this situation is the following: $S$ is
the spectrum of a local Artinian ring $A$, $I$ is the ideal defined by the radical of $A$, so that $S_{0}$ is the
spectrum of the residue field of $A$.

In the preceding situation, one is given a certain number of data above $S_{0}$, and one looks above $S$ for data which
lift them, that is to say, which give them back by base change from $S$ to $S_{0}$. This is done step by step, by way of
the $S_{n}$. At each step, we propose to define the obstructions encountered, and to classify, when they exist, the
solutions obtained.

The passage from $S_{n}$ to $S_{n+1}$ can be generalized as follows: one has a scheme $S$, two ideals $I$ and $J$ with
$I \supset J$, and $I \cdot J = 0$ (in the preceding case $S$, $I$ and $J$ are respectively $S_{n+1}$, $I/I^{n+2}$,
$I^{n+1}/I^{n+2}$). We denote by $S_{0}$ (resp. `S_J`) the closed subscheme of $S$ defined by $I$ (resp. $J$), and we
pose a problem of extension from `S_J` to $S$.

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

To simplify the language, we shall call a $Y$-functor, resp. $Y$-scheme, etc., a functor, resp. scheme, etc., equipped
with a morphism into the functor $Y$, thus extending the definitions of Exposé I (which concerned only the case of a
representable $Y$).

## 0. Reminders from SGA 1 III and various remarks

<!-- label: III.III.0 -->

<!-- original page 85 -->

Let us first state a general definition.

**Definition 0.1.** *Let $C$ be a category, $X$ an object of `Ĉ`, $G$ a `Ĉ`-group acting on $X$. We say that $X$ is
**formally principal homogeneous**[^N.D.E-III-3] under $G$ if the following equivalent conditions are satisfied:*

<!-- label: III.III.0.1 -->

*(i) for each object $S$ of $C$, the set $X(S)$ is empty or principal homogeneous under $G(S)$;*

*(ii) the morphism of functors $G \times X \to X \times X$ defined set-theoretically by $(g, x) \mapsto (gx, x)$ is an
isomorphism.*

This being so, we shall put the results of (SGA 1, III, § 5)[^N.D.E-III-4] in the form which will be most useful to us.
We shall employ the following general notations throughout this section. We have a scheme $S$ and on $S$ two
quasi-coherent ideals $I$ and $J$ such that

```text
I ⊃ J   and   I · J = 0.
```

In particular we shall therefore have $J^{2} = 0$. We shall denote by $S_{0}$ (resp. `S_J`) the closed subscheme of $S$
defined by the ideal $I$ (resp. $J$). For every $S$-functor $X$, we shall systematically denote by $X_{0}$ and `X_J` the
functors obtained by base change from $S$ to $S_{0}$ and `S_J`. Same notation for a morphism.

<!-- original page 86 -->

**Definition 0.1.1.**[^N.D.E-III-5] *Let $X$ be an $S$-functor. Define a functor $X^{+}$ above $S$ by the formula:*

<!-- label: III.III.0.1.1 -->

```text
Hom_S(Y, X⁺) = Hom_{S_J}(Y_J, X_J) = Hom_S(Y_J, X)
```

*for a variable $S$-scheme $Y$.* In the notations of (Exp. II, 1), one has

$$ X^{+} \simeq \prod_{S_{J}/S} X_{J} . $$

The identity morphism of `X_J` defines by construction an $S$-morphism

$$ p_{X} : X \to X^{+} . $$

[^N.D.E-III-6] Explicitly, for every $S$-scheme $Y$, the map

```text
p_X(Y) : Hom_S(Y, X) → Hom_S(Y, X⁺) = Hom_S(Y_J, X)
```

is the map induced by the morphism $Y_{J} \to Y$.

**Remark 0.1.2.** *Let us now observe that if $X$ is an $S$-group functor, then `X_J` is an `S_J`-group functor; then
the formula defining $X^{+}$ endows it with a structure of $S$-group functor, and the description of $p_{X}$ above shows
that $p_{X} : X \to X^{+}$ is a morphism of $S$-group functors.*

<!-- label: III.III.0.1.2 -->

**Remark 0.1.3.** *On the other hand, for every $S$-group functor $Y$, one has:*

<!-- label: III.III.0.1.3 -->

```text
Hom_{S-gr.}(Y, X⁺) = Hom_{S_J-gr.}(Y_J, X_J).
```

*Indeed, let $f \in \operatorname{Hom}_{S}(Y, X^{+})$, corresponding to $f_{J} \in \operatorname{Hom}_{S_{J}}(Y_{J},
X_{J})$; the condition that $f \in \operatorname{Hom}_{S-gr.}(Y, X^{+})$ is that, for every $T \to S$ and $y, y' \in
Y(T)$, one has $f(y \cdot y') = f(y) \cdot f(y')$, and this is equivalent to*

```text
f_J(y_J) · f_J(y_J′) = f_J((y · y′)_J);
```

*since $(y \cdot y')_{J} = y_{J} \cdot y_{J}'$ (because $Y(T) \to Y(T_{J}) = Y_{J}(T_{J})$ is a morphism of groups),
this is the condition for $f_{J}$ to be a morphism of groups. Applying this to $Y = X$, we recover that $p_{X}$, which
corresponds to $id_{X_{J}}$, is a morphism of $S$-group functors.*

Let us now return to the general case, but assume that $X$ is an $S$-scheme. Since an $S$-morphism of a variable
$S$-scheme $Y$ into $X^{+}$ is by definition an `S_J`-morphism $g_{J}$ of `Y_J` into `X_J`, we shall define an
$X^{+}$-functor in abelian groups `L_X` as follows.

**Scholie 0.1.4.**[^N.D.E-III-7] *If $\pi : Y \to S$ is a morphism of schemes and $M$ an `O_S`-module, we denote by $M
\otimes_{O_{S}} O_{Y}$ the inverse image $\pi*(M)$. If $J$ is an ideal of `O_S`, we denote by $J \cdot O_{Y}$ the ideal
of `O_Y` image of the morphism*

<!-- label: III.III.0.1.4 -->

```text
π*(J) = J ⊗_{O_S} O_Y → O_Y .
```

Note that, for every morphism of $S$-schemes $f : Z \to Y$, one has an epimorphism of `O_Z`-modules:

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

**Definition 0.1.5.**[^N.D.E-III-8] *Let $X$ be an $S$-scheme. For every $X^{+}$-scheme $Y$, given by a morphism
$g_{J} : Y_{J} \to X_{J}$, we set:*

<!-- label: III.III.0.1.5 -->

```text
Hom_{X⁺}(Y, L_X) = Hom_{O_{Y₀}}(g₀*(Ω¹_{X₀/S₀}), J · O_Y),
```

*where $\Omega^{1}_{X_{0}/S_{0}}$ denotes the module of relative differentials of $X_{0}$ with respect to $S_{0}$ (cf.
SGA 1, I.1 or [EGA IV₄, 16.3](https://jcreinhold.github.io/ega/iv/29-ch4-16-differential-invariants.html#163-fundamental-differential-invariants-of-a-morphism-of-preschemes)), and where $J \cdot O_{Y}$ is regarded as an $O_{Y_{0}}$-module thanks to the fact that it
is annihilated by $I$.*

Then `L_X` is an $X^{+}$-functor in abelian groups.[^N.D.E-III-9] Indeed, for every $X^{+}$-morphism $f : Z \to Y$, the
functor $f_{0}*$ and the morphism $f_{0}*(J \cdot O_{Y}) \to J \cdot O_{Z}$ of (0.1.4) induce a natural morphism of
abelian groups $L_{X}(f)$:

```text
Hom_{O_{Y₀}}(g₀*(Ω¹_{X₀/S₀}), J · O_Y)
        → Hom_{O_{Z₀}}(f₀* g₀*(Ω¹_{X₀/S₀}), f₀*(J · O_Y))
        → Hom_{O_{Z₀}}(f₀* g₀*(Ω¹_{X₀/S₀}), J · O_Z).
```

Let us finally note that $L_{X}(f)$ is described locally as follows. Note first that $Y$ and `Y_J` have the same
underlying topological space, and similarly for $V$ and `V_J` if $V$ is an open subset of $Y$. Let then $U =
\operatorname{Spec}(A)$ be an affine open of $X$ above an affine open $\operatorname{Spec}(\Lambda)$ of $S$, $V =
\operatorname{Spec}(B)$ an affine open of $Y$ such that $g_{J}(V_{J}) \subset U$, and $W = \operatorname{Spec}(C)$ an
affine open of $f^{-1}(V)$. Let $J$ and $I$ be the ideals of $\Lambda$ corresponding to $J$ and $I$. Then $f$ (resp.
$g_{J}$) induces a morphism of $\Lambda$-algebras $\theta : B \to C$ (resp. $\phi : A \to B/JB$), and one obviously has
$\theta(JB) \subset JC$. On the other hand, $m \in \operatorname{Hom}_{O_{Y_{0}}}(g_{0}*(\Omega^{1}_{X/S}), J \cdot
O_{Y})$ induces an element $D$ of

```text
Hom_{O_{V₀}}(g₀*(Ω¹_{U/S}), J · O_V) = Hom_{B/IB}(Ω¹_{A/Λ} ⊗_A B/IB, JB) = Der_Λ(A, JB),
```

and the image of $L_{X}(f)(m)$ in

```text
Hom_{O_{W₀}}(f₀* g₀*(Ω¹_{U/S}), J · O_Z) = Hom_{C/IC}(Ω¹_{A/Λ} ⊗_A C/IC, JC) = Der_Λ(A, JC)
```

is none other than $\theta \circ D$.

<!-- original page 88 -->

**Remark 0.1.6.**[^N.D.E-III-10] *Let $f : X \to W$ be an $S$-morphism. It induces an $S$-morphism $f^{+} : X^{+} \to
W^{+}$ defined as follows: if $g$ is an element of $\operatorname{Hom}_{S}(Y, X^{+})$, corresponding to an $S$-morphism
$g_{J} : Y_{J} \to X$, then $f^{+}(g)$ is the element $f \circ g_{J}$ of $\operatorname{Hom}_{S}(Y, W^{+})$. It is clear
that the following diagram is commutative:*

<!-- label: III.III.0.1.6 -->

```text
        f
   X ─────► W
   │         │
p_X│         │p_W
   ▼   f⁺    ▼
   X⁺ ────► W⁺ .
```

**Reminders 0.1.7.**[^N.D.E-III-11] *In this paragraph, given an $S$-scheme $X$, we "recall" certain functorial
properties of the module of differentials $\Omega^{1}_{X/S}$ and of the first infinitesimal neighborhood of the diagonal
$\Delta^{(1)}_{X/S}$, properties which follow easily from ([EGA IV₄, §§ 16.1–16.4](https://jcreinhold.github.io/ega/iv/29-ch4-16-differential-invariants.html#161-normal-invariants-of-an-immersion)), but which do not figure there
explicitly.*

<!-- label: III.III.0.1.7 -->

**a)** Let us begin by recalling the following facts (cf. [EGA II, §§ 1.2–1.5](https://jcreinhold.github.io/ega/ii/02-01-affine-morphisms.html#12-affine-preschemes-over-a-prescheme)). Let $g : Y \to X$ be a morphism of
schemes, $\pi : X' \to X$ an affine $X$-scheme, $B$ the quasi-coherent `O_X`-algebra $\pi_{*}(O_{X'})$; then the
$Y$-scheme $Y \times_{X} X'$ is affine and corresponds to the quasi-coherent `O_Y`-algebra $g*(B)$, and one has a
commutative diagram of bijections:

```text
Hom_X(Y, X′)            ──∼──►    Hom_Y(Y, Y ×_X X′)
    │                                       │
    ≀                                       ≀
    ▼                                       ▼
Hom_{O_X-alg.}(B, g_*(O_Y))   ──∼──►   Hom_{O_Y-alg.}(g*(B), O_Y).
```

Moreover, these bijections are functorial in the pair $(X, X')$, i.e., if $W'$ is an affine $W$-scheme, corresponding to
the quasi-coherent `O_W`-algebra $A$, if one has a commutative diagram of morphisms of schemes

```text
            X′ ──f′──► W′
          ↗ g′         │
         /             │
        ↗              │
      Y ──g──► X ──f──► W ,
```

and if we denote by $\phi : A \to f_{*}(B)$ and $\phi\sharp : f*(A) \to B$ (resp. $\theta : B \to g_{*}(O_{Y})$ and
$\theta\sharp : g*(B) \to O_{Y}$) the algebra morphisms associated to $f'$ (resp. to a variable $X$-morphism $g' : Y \to
X'$), then one has the following commutative diagram (where $Y$ is viewed as a $W$-scheme via $f \circ g$):

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

**b)** Let now $X$ be an $S$-scheme. Let $\Omega^{1}_{X/S}$ be the module of differentials of $X$ over $S$, and
$\Delta^{(1)}_{X/S}$ the first infinitesimal neighborhood of the diagonal immersion $\delta_{X} : X \to X \times_{S} X$;
it is a subscheme of $X \times_{S} X$, of which the diagonal $\Delta_{X/S}$ is a closed subscheme. We denote by
$pr^{i}_{X}$ ($i = 1, 2$) the two projections $X \times_{S} X \to X$, and by $\pi_{X}$ the restriction of $pr^{1}_{X}$
to $\Delta^{(1)}_{X/S}$.

On the one hand, every morphism $f : X \to W$ of $S$-schemes induces an $S$-morphism $\Delta^{(1)} f :
\Delta^{(1)}_{X/S} \to \Delta^{(1)}_{W/S}$ such that the following diagram is commutative:

```text
       δ_X            pr_X
   X ─────► Δ⁽¹⁾_{X/S} ─────► X ×_S X ─────► X
   │              │               │           │
 f │       Δ⁽¹⁾f │            f×f│         f │
   ▼       δ_W   ▼                ▼   pr_W   ▼
   W ─────► Δ⁽¹⁾_{W/S} ─────► W ×_S W ─────► W .
```

On the other hand, $\Delta^{(1)}_{X/S}$ is, via the projection $\pi_{X}$, an affine $X$-scheme, spectrum of the
augmented quasi-coherent `O_X`-algebra

$$ P^{1}_{X/S} = O_{X} \oplus \Omega^{1}_{X/S}, $$

where $\Omega^{1}_{X/S}$ is an ideal of square zero; the augmentation is the morphism of `O_X`-algebras $\epsilon_{X} :
P^{1}_{X/S} \to O_{X}$ which vanishes on $\Omega^{1}_{X/S}$ and which corresponds to the closed immersion $\delta_{X} :
X \hookrightarrow \Delta^{(1)}_{X/S}$. Then, every morphism of $S$-schemes $f : X \to W$ induces a morphism of augmented
`O_X`-algebras

```text
f*(P¹_{W/S}) = O_X ⊕ f*(Ω¹_{W/S}) → P¹_{X/S} = O_X ⊕ Ω¹_{X/S}
```

that is, equivalently, a morphism of `O_X`-modules

$$ f_{X/W/S} : f*(\Omega^{1}_{W/S}) \to \Omega^{1}_{X/S}, $$

cf. ([EGA IV₄, 16.4.3.6](https://jcreinhold.github.io/ega/iv/29-ch4-16-differential-invariants.html#164-functorial-properties-of-differential-invariants)) (and (16.4.18.2) for the notation $f_{X/W/S}$).

<!-- original page 90 -->

Since $\pi_{X} : \Delta^{(1)}_{X/S} \to X$ is affine, then, by a), $\Delta^{(1)} f$ is entirely determined by
$f_{X/W/S}$ and, for every $X$-scheme $g : Y \to X$, the set

```text
Hom_X(Y, Δ⁽¹⁾_{X/S}) ≃ Hom_{O_Y-alg.}(O_Y ⊕ g*(Ω¹_{X/S}), O_Y)
```

is identified with a subset of $\operatorname{Hom}_{O_{Y}}(g*(\Omega^{1}_{X/S}), O_{Y})$, namely the subset

$$ \tilde{\operatorname{Hom}}_{O_{Y}}(g*(\Omega^{1}_{X/S}), O_{Y}) $$

formed by the `O_Y`-morphisms $\psi : g*(\Omega^{1}_{X/S}) \to O_{Y}$ such that $Im(\psi)$ is an ideal of `O_Y` of
square zero.[^N.D.E-III-12]

Consequently, applying a) to the diagram

```text
              Δ⁽¹⁾ f
   Δ⁽¹⁾_{X/S} ────► Δ⁽¹⁾_{W/S}
       ↗
    g′│
       │
    Y ──g──► X ──f──► W
```

and taking into account that $\Delta^{(1)} f$ is the restriction to $\Delta^{(1)}_{X/S}$ of $f \times f$, one obtains
the following commutative diagram, functorial in the $X$-scheme `Y ──g──► X`:

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
denote by $\tilde{L}_{X}$ the $X$-functor which to every $X$-scheme $g : Y \to X$ associates
$\operatorname{Hom}_{O_{Y}}(g*(\Omega^{1}_{X/S}), O_{Y})$, and $\tilde{L}_{f} : \tilde{L}_{X} \to \tilde{L}_{W}$ the
morphism of functors defined above (which to every $\psi \in \tilde{L}_{X}(Y)$ associates $\psi \circ g*(f_{X/W/S})$),
what precedes shows that we have a commutative diagram of functors:*

<!-- label: III.III.0.1.7.1 -->

```text
X ×̃ X L̃_X  ◄──∼──  Δ⁽¹⁾_{X/S}  ─────► X ×_S X
    │                   │                 │
f ×̃_f│                Δ⁽¹⁾f│           f×f│
    ▼                   ▼                 ▼
W ×̃ W L̃_W  ◄──∼──  Δ⁽¹⁾_{W/S}  ─────► W ×_S W.
```

<!-- original page 91 -->

**Theorem 0.1.8.** *(SGA 1, III 5.1)[^N.D.E-III-13] Let $Y$, $X$ be two $S$-schemes, $J$ a quasi-coherent ideal of `O_Y`
of square zero, `Y_J` the closed subscheme of $Y$ defined by $J$, and $g_{J} : Y_{J} \to X$ an $S$-morphism.*

<!-- label: III.III.0.1.8 -->

*a) The set $P(g_{J})$ of $S$-morphisms $g : Y \to X$ which extend $g_{J}$ is either empty, or principal homogeneous
under the abelian group*

$$ \operatorname{Hom}_{O_{Y_{J}}}(g_{J}*(\Omega^{1}_{X/S}), J). $$

*b) If $i : Y_{0} \hookrightarrow Y_{J}$ is the closed immersion defined by a quasi-coherent ideal $I \supset J$ such
that $I \cdot J = 0$, and if $g_{0} = g_{J} \circ i$, the preceding abelian group is isomorphic to*

$$ \operatorname{Hom}_{O_{Y_{0}}}(g_{0}*(\Omega^{1}_{X/S}), J). $$

*Proof.* (b) follows at once from (a). Indeed, $J$, being annihilated by $I$, can be considered as an
$O_{Y_{0}}$-module, whence, by adjunction:

```text
Hom_{O_{Y_J}}(g_J*(Ω¹_{X/S}), J) = Hom_{O_{Y₀}}(i* g_J*(Ω¹_{X/S}), J).
```

To prove (a), we may assume $P(g_{J}) \neq \emptyset$, i.e. that there exists an $S$-morphism $g : Y \to X$ extending
$g_{J}$. Let us denote by $j$ the immersion $Y_{J} \hookrightarrow Y$. Then $P(g_{J})$ is the set of $S$-morphisms $g' :
Y \to X$ such that $g' \circ j = g_{J}$. The datum of such a $g'$ is equivalent to the datum of an $S$-morphism

```text
h : Y → X ×_S X
```

such that $pr_{1} \circ h = g$ and $h_{J} = \delta \circ g_{J}$, where $h_{J} = h \circ j$ and $\delta$ is the diagonal
immersion $X \hookrightarrow X \times_{S} X$:

```text
                h_J = δ ∘ g_J
   X ×_S X  ◄──────────────── Y_J
    │  ▲ h                    │
pr₁│   ╲                    j │
    ▼    ╲                     ▼
    X  ◄─g───                  Y .
```

Since $h_{J}$ factors through $\delta$ and $Y$ is in the first infinitesimal neighborhood of the immersion $j : Y_{J}
\to Y$ (since $J^{2} = 0$), then, by functoriality (cf. EGA IV₄, 16.2.2 (i)), the $h$'s sought factor uniquely through
$\Delta^{(1)}_{X/S}$ (cf. 0.1.7). Set

```text
Y′ = Δ⁽¹⁾_{X/S} ×_X Y    and    Y_J′ = Y′ ×_Y Y_J = Δ⁽¹⁾_{X/S} ×_X Y_J .
```

Then the $h$'s sought are in bijection with the sections $u$ of $Y' \to Y$ which extend the section $u_{J} = (\delta
\circ g_{J}, id)$ of $Y_{J}' \to Y_{J}$. On the other hand, $Y'$ (resp. $Y_{J}'$) is an affine scheme over $Y$ (resp.
`Y_J`), corresponding to the quasi-coherent algebra

```text
A = O_Y ⊕ g*(Ω¹_{X/S}),    resp.    A_J = A ⊗_{O_Y} O_{Y_J} = O_{Y_J} ⊕ g_J*(Ω¹_{X/S}).
```

Let us denote by $\epsilon : A \to O_{Y}$ the canonical augmentation of $A$ (i.e. the morphism of `O_Y`-algebras $A \to
O_{Y}$ which vanishes on $g*(\Omega^{1}_{X/S})$), and likewise define $\epsilon_{J} : A_{J} \to O_{Y_{J}}$. Then,

```text
Γ(Y′/Y) ≃ Hom_{O_Y-alg.}(A, O_Y),    Γ(Y_J′/Y_J) ≃ Hom_{O_{Y_J}-alg.}(A_J, O_{Y_J})
```

<!-- original page 92 -->

and, via these isomorphisms, the section $u = (\delta \circ g, id)$ (resp. $u_{J}$) corresponds to $\epsilon$ (resp.
$\epsilon_{J}$). Consequently, $P(g_{J})$ is in bijection with the set of algebra morphisms $A \to O_{Y}$ which reduce
to $\epsilon_{J}$, and via this bijection, $g$ corresponds to $\epsilon$.

Set $M = g*(\Omega^{1}_{X/S})$. Then $\operatorname{Hom}_{O_{Y}-alg.}(A, O_{Y})$ is identified with the set of
`O_Y`-morphisms $\psi : M \to O_{Y}$ such that $Im(\psi)$ is an ideal of square zero, and we are interested in those
which induce the null morphism $M \to O_{Y_{J}} = O_{Y}/J$, i.e. which send $M$ into $J$. Conversely, since $J^{2} = 0$,
every `O_Y`-morphism $\phi : M \to J$ comes from a (unique) algebra morphism $A \to O_{Y}$, reducing to $\epsilon_{J}$.
Finally, we have $\operatorname{Hom}_{O_{Y}}(g*(\Omega^{1}_{X/S}), J) =
\operatorname{Hom}_{O_{Y_{J}}}(g_{J}*(\Omega^{1}_{X/S}), J)$ since $J^{2} = 0$ (cf. the proof of (b) already seen). One
thus obtains a bijection

$$ P(g_{J}) \simeq \operatorname{Hom}_{O_{Y_{J}}}(g_{J}*(\Omega^{1}_{X/S}), J) $$

by which $g$ corresponds to the null morphism.

For every $m \in \operatorname{Hom}_{O_{Y_{J}}}(g_{J}*(\Omega^{1}_{X/S}), J)$, denote by $m \cdot g$ the element of
$P(g_{J})$ associated to $g$ and $m$ by the preceding bijection. We have already seen that $0 \cdot g = g$; it remains
to see that

```text
m′ · (m · g) = (m + m′) · g.                            (0.1.8 (∗))
```

This is verified locally.[^N.D.E-III-14] Indeed, the two preceding morphisms $Y \to X$ induce the same continuous map as
$g$ between the underlying topological spaces; it therefore suffices to verify that for every affine open $U =
\operatorname{Spec}(A)$ of $X$ above an affine open $\operatorname{Spec}(\Lambda)$ of $S$, and every affine open $V =
\operatorname{Spec}(B)$ of $g^{-1}(U)$, they induce the same morphism of $\Lambda$-algebras $A \to B$.

Let $J = \Gamma(V, J)$ and let $\phi, \psi$ and $\eta$ be the morphisms $A \to B$ induced by $g$, $m \cdot g$ and
$m' \cdot (m \cdot g)$ respectively; they coincide modulo $J$. One can uniquely write $\psi = \phi + D$ (resp.
$\eta = \psi + D'$), where $D$ (resp. $D'$) is an element of

```text
Der_φ(A, J) = {δ ∈ Hom_Λ(A, J) | δ(ab) = φ(a) δ(b) + φ(b) δ(a)}
```

(resp. $\operatorname{Der}_{\psi}(A, J)$). But $\operatorname{Der}_{\phi}(A, J) = \operatorname{Der}_{\psi}(A, J)$ since
$J^{2} = 0$, and both are identified with

```text
Hom_{B/J}(Ω¹_{A/Λ} ⊗_A B/J, J),
```

and via this identification $D$ corresponds to $m$ and $D'$ to $m'$. Then $\eta = \phi + D + D'$ and $D + D'$
corresponds to $m + m'$, whence the equality (∗).

**Corollary 0.1.9.**[^N.D.E-III-15] *Let $X$ be an $S$-scheme; resume the notations of 0.1.5. Then $X$ is endowed with a
(left) action of the $X^{+}$-abelian group `L_X`, which makes $X$ into a formally principal homogeneous object under
`L_X` above $X^{+}$, i.e. one has an isomorphism of $X^{+}$-functors:*

<!-- label: III.III.0.1.9 -->

```text
L_X × X ──∼──► X × X
       X⁺          X⁺
```

*(defined set-theoretically by $(m, x) \mapsto (x, m \cdot x)$).*

*Proof.* Let $i_{0}$ be the immersion $X_{0} \hookrightarrow X$. Note first that, since $X_{0} = X \times_{S} S_{0}$,
one has $i_{0}*(\Omega^{1}_{X/S}) \simeq \Omega^{1}_{X_{0}/S_{0}}$ (cf. [EGA IV, 16.4.5](https://jcreinhold.github.io/ega/iv/29-ch4-16-differential-invariants.html#164-functorial-properties-of-differential-invariants)).

Let $Y$ be an $X^{+}$-scheme, given by an $S$-morphism $g_{J} : Y_{J} \to X$, and let $g_{0} : Y_{0} \to X_{0}$ be the
morphism obtained by base change. By 0.1.8, if $\operatorname{Hom}_{X^{+}}(Y, X)$ is non-empty, it is a principal
homogeneous set under the group

```text
Hom_{O_{Y₀}}(g₀* i₀*(Ω¹_{X/S}), J · O_Y),
```

which is identified with $\operatorname{Hom}_{O_{Y_{0}}}(g_{0}*(\Omega^{1}_{X_{0}/S_{0}}), J \cdot O_{Y}) = L_{X}(Y)$.
One therefore has a bijection

```text
L_X(Y) × Hom_{X⁺}(Y, X)  ──∼──►  Hom_{X⁺}(Y, X ×_{X⁺} X)
```

given by $(m, g) \mapsto (g, m \cdot g)$. Let us show that this is "functorial in $Y$".

Let $f : Z \to Y$ be a morphism of $S$-schemes. It is a question of showing that the diagram below is commutative:

```text
L_X(Y) × Hom_{X⁺}(Y, X) ──∼──► Hom_{X⁺}(Y, X ×_{X⁺} X)
   │                                       │
L_X(f) × f                             f × f
   ▼                                       ▼
L_X(Z) × Hom_{X⁺}(Z, X) ──∼──► Hom_{X⁺}(Z, X ×_{X⁺} X).
```

If $\operatorname{Hom}_{X^{+}}(Y, X) = \emptyset$, there is nothing to show. It therefore suffices to see that, for
every $S$-morphism $g : Y \to X$ extending $g_{J}$ and every $m \in L_{X}(Y)$, one has:

```text
(m · g) ∘ f = L_X(f)(m) · (g ∘ f).                       (0.1.9 (∗))
```

These two $S$-morphisms $Z \to X$ coincide on `Z_J` with $g_{J} \circ f_{J}$; in particular, they induce the same
continuous map as $g \circ f$ between the underlying topological spaces. Consequently, it suffices to see that, if $z
\in Z$, $y = f(z)$, $x = g(y)$, and if $A$, $B$, $C$ denote respectively the local rings $O_{X,x}$, $O_{Y,y}$,
$O_{Z,z}$, then the morphisms $A \to C$ induced by $(m \cdot g) \circ f$ and $L_{X}(f)(m) \cdot (g \circ f)$ coincide.
Denote by $s$ the image of $x$ in $S$, $\Lambda = O_{S,s}$, $J$ and $I$ the ideals of $\Lambda$ corresponding to $J$ and
$I$, and let $\phi, \psi : A \to B$ and $\theta : B \to C$ be the morphisms of $\Lambda$-algebras induced by $g$, $m
\cdot g$, and $f$. Then $m$ induces an element $D$ of

```text
Hom_{B/IB}(Ω¹_{A/Λ} ⊗_A B/IB, JB) = Der_Λ(A, JB)
```

and one has $\psi = \phi + D$; hence $(m \cdot g) \circ f$ corresponds to $\theta \circ \psi = \theta \circ \phi +
\theta \circ D$. Now, we have seen in 0.1.5 that $\theta \circ D$ is the image of $L_{X}(f)(m)$ in

```text
Hom_{C/IC}(Ω¹_{A/Λ} ⊗_A C/IC, JC) = Der_Λ(A, JC);
```

consequently, $\theta \circ \phi + \theta \circ D$ is the image of $L_{X}(f)(m) \cdot (g \circ f)$. This proves the
equality (0.1.9 (∗)).

**Corollary 0.1.10.**[^N.D.E-III-16] *a) `L_X` depends functorially on $X$: for every $S$-morphism $f : X \to W$, there
exists an $S$-morphism $L_{f} : L_{X} \to L_{W}$ which is a morphism of abelian groups "above $f^{+}$", i.e., the
diagram*

<!-- label: III.III.0.1.10 -->

```text
        L_f
   L_X ────► L_W
   │           │
   ▼   f⁺      ▼
   X⁺ ──────► W⁺
```

*is commutative, and for every $Y \to X^{+}$,*

```text
L_f(Y) : Hom_{X⁺}(Y, L_X) → Hom_{W⁺}(Y, L_W)
```

*(where $Y$ is above $W^{+}$ via $f^{+}$) is a morphism of abelian groups.*

*b) Moreover, the following diagram is commutative:*

```text
L_X × X ─∼─► X ×_{X⁺} X
   │              │
L_f × f        f × f
   ▼              ▼
L_W × W ─∼─► W ×_{W⁺} W .
```

*Proof.* a) $L_{f}$ is induced by the morphism of $O_{X_{0}}$-modules $f_{X_{0}/W_{0}/S_{0}} :
f_{0}*(\Omega^{1}_{W_{0}/S_{0}}) \to \Omega^{1}_{X_{0}/S_{0}}$ (cf. 0.1.7 b)): for every $X^{+}$-scheme $Y$, given by an
$S$-morphism $g_{J} : Y_{J} \to X$, one has a commutative diagram, functorial in $Y$:

```text
                          L_f(Y)
Hom_{O_{Y₀}}(g₀*(Ω¹_{X₀/S₀}), J · O_Y) ───► Hom_{O_{Y₀}}(g₀* f₀*(Ω¹_{W₀/S₀}), J · O_Y)
       │                                                       │
       ▼                                                       ▼
     {g_J}                                                {f_J ∘ g_J}
```

where $L_{f}(Y)$ is the map $\psi \mapsto \psi \circ g_{0}*(f_{X_{0}/W_{0}/S_{0}})$, which is indeed a morphism of
abelian groups.[^N.D.E-III-17]

Let us prove (b). Let $Y$ be an $X^{+}$-scheme; if $\operatorname{Hom}_{X^{+}}(Y, X) = \emptyset$ there is nothing to
show. So let $g \in \operatorname{Hom}_{X^{+}}(Y, X)$; it must be seen that for every $m \in L_{X}(Y)$, one has:

```text
f ∘ (m · g) = L_f(Y)(m) · (f ∘ g).                       (0.1.10 (∗))
```

Now, $g$ being fixed, $\operatorname{Hom}_{X}(Y, X \times_{X^{+}} X)$ is a subset of $\operatorname{Hom}_{X}(Y,
\Delta^{(1)}_{X/S})$ and

```text
L_X(Y) = Hom_{O_{Y₀}}(g₀*(Ω¹_{X₀/S₀}), J · O_Y) = Hom_{O_Y}(g*(Ω¹_{X/S}), J · O_Y)
```

a subset of $\tilde{L}_{X}(Y)$ (cf. 0.1.7); finally, $L_{f}(Y)$ is the restriction to $L_{X}(Y)$ of the map
$\tilde{L}_{f}(Y)$. Moreover, the bijection

```text
L_X(Y) ──∼──► Hom_X(Y, X ×_{X⁺} X),    m ↦ (g, m · g)
```

is (the inverse of) the restriction to $L_{X}(Y) \subset \tilde{L}_{X}(Y)$ of the bijection
`Hom_X(Y, Δ⁽¹⁾_{X/S}) ──∼──► {g} × L̃_X(Y)` considered in 0.1.7.1. Consequently, the equality (0.1.10 (∗)) results from
(0.1.7 (∗)); indeed, if we denote by $g'$ the $X$-morphism $Y \to \Delta^{(1)}_{X/S}$ defined by $(g, m \cdot g)$, then
the element of $\tilde{L}_{W}(Y)$ corresponding to $(f \circ g, f \circ g')$ is $\tilde{L}_{f}(Y)(m) = L_{f}(Y)(m)$,
i.e., one indeed has

```text
L_f(m) · (f ∘ g) = f ∘ (m · g).
```

**Lemma 0.1.11.** *Let $X$, $X'$ be two $S$-schemes. One has a commutative diagram:*

<!-- label: III.III.0.1.11 -->

```text
L_X ×_S L_{X′} ──∼──► L_{X ×_S X′}
       │                  │
       ▼                  ▼
X⁺ ×_S X′⁺  ──∼──► (X ×_S X′)⁺ .
```

[^N.D.E-III-18] *Proof.* First, for every $S$-scheme $Y$, $\operatorname{Hom}_{S}(Y, X^{+} \times_{S} X'^{+})$ equals
$\operatorname{Hom}_{S}(Y, X^{+}) \times \operatorname{Hom}_{S}(Y, X'^{+})$ and this is isomorphic to

```text
Hom_S(Y_J, X) × Hom_S(Y_J, X′) = Hom_S(Y, (X ×_S X′)⁺);
```

this proves that $X^{+} \times_{S} X'^{+} \simeq (X \times_{S} X')^{+}$.

Next, let $Y$ be a scheme above $X^{+} \times_{S} X'^{+}$ via a morphism $h : Y_{J} \to X \times_{S} X'$; set $f = p
\circ h$ and $g = q \circ h$, where we have denoted by `p, q` the projections of $X \times_{S} X'$ to $X$ and $X'$.
Since $\Omega^{1}_{(X_{0} \times_{S_{0}} X'_{0})/S_{0}} \cong p_{0}*(\Omega^{1}_{X_{0}/S_{0}}) \oplus
q_{0}*(\Omega^{1}_{X'_{0}/S_{0}})$ (cf. [EGA IV₄, 16.4.23](https://jcreinhold.github.io/ega/iv/29-ch4-16-differential-invariants.html#164-functorial-properties-of-differential-invariants)), one obtains a natural isomorphism:

```text
Hom_{O_{Y₀}}(f₀*(Ω¹_{X₀/S₀}), J · O_Y) × Hom_{O_{Y₀}}(g₀*(Ω¹_{X′₀/S₀}), J · O_Y)
    ≃ Hom_{O_{Y₀}}(h₀*(Ω¹_{(X₀ ×_{S₀} X′₀)/S₀}), J · O_Y)
```

i.e., $L_{X}(Y) \times L_{X'}(Y) \simeq L_{X \times_{S} X'}(Y)$.

**Remark 0.1.12.**[^N.D.E-III-19] *Let $C$ be a category stable under fibered products, $S$ an object of $C$, $T_{1}$,
$T_{2}$ two objects above $S$ and, for $i = 1, 2$, $L_{i}$ and $X_{i}$ two objects above $T_{i}$:*

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

**Corollary 0.1.13.** *Let `X_1`, `X_2` be two $S$-schemes. One has a commutative diagram of isomorphisms:*

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

**Proposition 0.2.** *For every $S$-scheme $X$, one can define a (left) action of the $X^{+}$-abelian group `L_X` on the
$X^{+}$-object $X$, such that:*

<!-- label: III.III.0.2 -->

*(i) this action makes $X$ into a formally principal homogeneous object under `L_X` above $X^{+}$, i.e. the morphism*

```text
L_X × X ──► X × X
       X⁺          X⁺
```

*is an isomorphism of $X^{+}$-functors;*

*(ii) this action is functorial in the $S$-scheme $X$, i.e., for every $S$-morphism $f : X \to W$, the following diagram
is commutative:*

```text
L_X ×_{X⁺} X ─────► X
     │              │
 L_f × f          f │
     ▼              ▼
L_W ×_{W⁺} W ─────► W ;
```

*(iii) this action "commutes with fibered product", i.e. for all $S$-schemes `X_1` and `X_2`, the following diagram is
commutative:*

```text
L_{X_1 ×_S X_2} ×_{(X_1 ×_S X_2)⁺} (X_1 ×_S X_2)  ──►  X_1 ×_S X_2
        │                                                    ▲
        ≃                                                    │
        ▼                                                    │
(L_{X_1} ×_S L_{X_2}) ×_{(X_1⁺ ×_S X_2⁺)} (X_1 ×_S X_2) ──∼──► (L_{X_1} ×_{X_1⁺} X_1) ×_S (L_{X_2} ×_{X_2⁺} X_2).
```

<!-- original page 89 -->

*Proof.*[^N.D.E-III-20] (i) and (ii) follow respectively from Corollaries 0.1.9 and 0.1.10. To prove (iii), denote $P(X)
= L_{X} \times_{X^{+}} X$, for every $S$-scheme $X$. Then, by (ii) applied to the projections $p_{i} : X_{1} \times_{S}
X_{2} \to X_{i}$, one obtains commutative squares

```text
P(X_1 ×_S X_2)  ─────►  X_1 ×_S X_2
       │                     │
  L_{p_i} × p_i             p_i
       ▼                     ▼
   P(X_i)         ─────►   X_i
```

<!-- original page 90 -->

for $i = 1, 2$, and hence a commutative square:

```text
P(X_1 ×_S X_2)         ─────►   X_1 ×_S X_2
       │                                ║
       ▼                                ▼
P(X_1) ×_S P(X_2)      ─────►   X_1 ×_S X_2 .
```

Combining this with Corollary 0.1.13, one obtains that the vertical arrow is an isomorphism, and that one has the
commutative diagram announced in (iii).

<!-- original page 90 -->

**Remark 0.3.** *Suppose the $X^{+}$-scheme $Y$ flat over $S$ (cf. SGA 1, IV). Then one can write*

<!-- label: III.III.0.3 -->

```text
Hom_{X⁺}(Y, L_X) = Hom_{O_{Y₀}}(g₀*(Ω¹_{X₀/S₀}), J ⊗_{O_{S₀}} O_{Y₀}).
```

**Remark 0.4.** *Denote by $\pi_{0} : X_{0} \to S_{0}$ the structural morphism and suppose there exists an
$O_{S_{0}}$-module $\omega^{1}_{X_{0}/S_{0}}$ such that $\Omega^{1}_{X_{0}/S_{0}} \simeq
\pi_{0}*(\omega^{1}_{X_{0}/S_{0}})$ (the case will arise in particular when $X_{0}$ is an $S_{0}$-group, cf. II, 4.11).
If one defines a functor $L'_{X}$ above $S$ by the formula*

<!-- label: III.III.0.4 -->

```text
Hom_S(Y, L′_X) = Hom_{O_{Y₀}}(ω¹_{X₀/S₀} ⊗_{O_{S₀}} O_{Y₀}, J · O_Y),     (0.4.1)
```

*one then has $\operatorname{Hom}_{X^{+}}(Y, L_{X}) = \operatorname{Hom}_{S}(Y, L'_{X})$ for every $X^{+}$-scheme $Y$,
that is to say*

```text
L_X = L′_X × X⁺ .
              S
```

[^N.D.E-III-21] Then, since $L_{X} \times_{X^{+}} X = L'_{X} \times_{S} X$, the action of `L_X` on $X$ induces an action
of $L'_{X}$ on $X$, and this action respects the morphism $p_{X} : X \to X^{+}$; indeed, if $Y$ is an $S$-scheme, $h : Y
\to X$ an $S$-morphism and $m$ an element of $L'_{X}(Y)$, then $h$ and $m \cdot h$ have the same restriction to `Y_J`,
i.e. $p_{X}(m \cdot h) = p_{X}(h)$.

<!-- original page 91 -->

**Remark 0.5.** *Keep the hypotheses and notations of 0.4 and suppose moreover that $Y$ is an $S$-scheme flat over $S$.
Then we have*

<!-- label: III.III.0.5 -->

```text
Hom_{X⁺}(Y, L_X) = Hom_S(Y, L′_X) = Hom_{S₀}(Y₀, L⁰_X),
```

*where the $S_{0}$-functor in abelian groups $L^{0}_{X}$ is defined by the following identity (with respect to the
variable $S_{0}$-scheme $T$):*

```text
Hom_{S₀}(T, L⁰_X) = Hom_{O_T}(ω¹_{X₀/S₀} ⊗_{O_{S₀}} O_T, J ⊗_{O_{S₀}} O_T).    (0.5.1)
```

*In the notations of (II, 1), we have therefore shown that the functors $L'_{X}$ and $\prod_{S_{0}/S} L^{0}_{X}$ have
the same restriction to the full subcategory of $(Sch)/S$ whose objects are the $S$-schemes $Y$ flat over $S$.*

**Remark 0.6.** *Keep the hypotheses and notations of 0.5[^N.D.E-III-22] and suppose moreover that there exists a
section $\epsilon_{0}$ of $\pi_{0} : X_{0} \to S_{0}$; one then has $\omega^{1}_{X_{0}/S_{0}} \simeq
\epsilon_{0}*(\Omega^{1}_{X_{0}/S_{0}})$.*

<!-- label: III.III.0.6 -->

First, one has (independently of the preceding hypothesis):

```text
Hom_{S₀}(T, L⁰_X) = Γ(T, Hom_{O_T}(ω¹_{X₀/S₀} ⊗_{O_{S₀}} O_T, J ⊗_{O_{S₀}} O_T)).
```

Now suppose that $\omega^{1}_{X_{0}/S_{0}}$ admits a finite presentation (cf. [EGA 0_I, 5.2.5](https://jcreinhold.github.io/ega/i/00-05-quasi-coherent-and-coherent-sheaves.html#52-sheaves-of-finite-type)), which will in particular
be the case if $X_{0}$ is locally of finite presentation over $S_{0}$ (cf. [EGA IV₄, 16.4.22](https://jcreinhold.github.io/ega/iv/29-ch4-16-differential-invariants.html#164-functorial-properties-of-differential-invariants)). Then, if $T$ is flat over
$S_{0}$, it follows from ([EGA 0_I, 6.7.6](https://jcreinhold.github.io/ega/i/00-06-flatness.html#67-flat-morphisms-of-ringed-spaces)) that

```text
Hom_{O_T}(ω¹_{X₀/S₀} ⊗_{O_{S₀}} O_T, J ⊗_{O_{S₀}} O_T) ≃ Hom_{O_{S₀}}(ω¹_{X₀/S₀}, J) ⊗_{O_{S₀}} O_T ,
```

whence

```text
Hom_{S₀}(T, L⁰_X) = Γ(T, Hom_{O_{S₀}}(ω¹_{X₀/S₀}, J) ⊗_{O_{S₀}} O_T).
```

Introducing the notation $W(\cdot)$ of (I, 4.6.1), we have therefore proved that for every $S_{0}$-scheme $T$ flat over
$S_{0}$, one has

```text
Hom_{S₀}(T, L⁰_X) = Hom_{S₀}(T, W(Hom_{O_{S₀}}(ω¹_{X₀/S₀}, J))).
```

<!-- original page 92 -->

In summary, if $\omega^{1}_{X_{0}/S_{0}}$ admits a finite presentation, and if one restricts to the category of
$S$-schemes flat over $S$, one has

```text
L′_X = ∏_{S₀/S} W(Hom_{O_{S₀}}(ω¹_{X₀/S₀}, J)),                  (0.6.1)
```

and $\operatorname{Hom}_{O_{S_{0}}}(\omega^{1}_{X_{0}/S_{0}}, J)$ is a quasi-coherent $O_{S_{0}}$-module, by [EGA I,
9.1.1](https://jcreinhold.github.io/ega/i/01-09-complements-on-quasi-coherent-sheaves.html#91-tensor-product-of-quasi-coherent-sheaves).

Note finally that if $\omega^{1}_{X_{0}/S_{0}}$ is moreover locally free (of finite rank), for example if $X_{0}$ is
smooth over $S_{0}$ (in which case it is automatically locally of finite presentation over $S_{0}$), one has

```text
Hom_{O_{S₀}}(ω¹_{X₀/S₀}, J) ≃ Lie(X₀/S₀) ⊗_{O_{S₀}} J ,           (0.6.2)
```

where, by abuse of language ($X_{0}$ not being necessarily an $S_{0}$-group), we denote by $Lie(X_{0}/S_{0})$ the dual
of the $O_{S_{0}}$-module $\omega^{1}_{X_{0}/S_{0}}$.[^N.D.E-III-23]

Proposition 0.2 (and its proof) has two important corollaries.[^N.D.E-III-24]

**Corollary 0.7.** *Let $X$ be an $S$-scheme.*

<!-- label: III.III.0.7 -->

*a) Every $S$-endomorphism of $X$ inducing the identity on `X_J` is an automorphism.*

*b) One has an exact sequence of groups:*

```text
0 ──► Hom_{O_{X₀}}(Ω¹_{X₀/S₀}, J · O_X) ──i──► Aut_S(X) ──► Aut_{S_J}(X_J) .
```

*c) Moreover, if one makes $\operatorname{Aut}_{S}(X)$ act on the first group by transport of structure, one has, for
all $u \in \operatorname{Aut}_{S}(X)$ and $m \in \operatorname{Hom}_{O_{X_{0}}}(\Omega^{1}_{X_{0}/S_{0}}, J \cdot
O_{X})$:*

```text
i(u · m) = u · i(m) · u⁻¹.
```

<!-- original page 93 -->

*Proof.* By 0.2 (i), $\operatorname{Hom}_{X^{+}}(X, X)$ is a principal homogeneous set under
$\operatorname{Hom}_{X^{+}}(X, L_{X})$, since it is certainly non-empty: it contains a marked point, namely the identity
automorphism of $X$.[^N.D.E-III-25] Consequently, the map $m \mapsto m \cdot id_{X}$ induces a bijection

```text
Hom_{O_{X₀}}(Ω¹_{X₀/S₀}, J · O_X) = L_X(X) ──∼──► Hom_{X⁺}(X, X).
```

Let $m \in L_{X}(X)$ and let $f = m' \cdot id_{X}$ be an element of $\operatorname{Hom}_{X^{+}}(X, X)$. Applying 0.2
(ii) to $f$, one obtains:

```text
f ∘ (m · id_X) = L_f(X)(m) · f = L_f(X)(m) · (m′ · id_X).
```

On the other hand, since $f$ is an $X^{+}$-endomorphism of $X$, one has $f_{J} = id_{X_{J}}$ and therefore $f_{0} =
id_{X_{0}}$; since $L_{f}$ depends only on $f_{0}$ (cf. N.D.E. (17) in 0.1.10), one therefore has $L_{f}(X)(m) = m$.
Consequently, the equality above rewrites as:

```text
(m′ · id_X) ∘ (m · id_X) = m · (m′ · id_X) = (m + m′) · id_X .
```

This shows that the bijection $m \mapsto m \cdot id_{X}$ transforms the group law of $\operatorname{Hom}_{X^{+}}(X,
L_{X})$ into the composition law of $X^{+}$-endomorphisms of $X$.

It follows first that every element of $\operatorname{Hom}_{X^{+}}(X, X)$ is invertible, which is the first assertion of
the statement, and then that one has an exact sequence

```text
0 ──► Hom_{X⁺}(X, L_X) ──i──► Aut_S(X) ──► Aut_{S_J}(X_J) ,
```

which is the second.

Let us now note that the morphism $i$ defined above is functorial in $X$ for isomorphisms, because it is defined in
structural terms from the action of `L_X` on $X$ above $X^{+}$, itself functorial in $X$ by assertion (ii) of
Proposition 0.2.[^N.D.E-III-26] Hence every automorphism $u$ of $X$ above $S$ induces by transport of structure
isomorphisms

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

i.e. such that $f \circ i = i \circ h$. On the other hand, $f$ is given by the commutative diagram

```text
        a
   X ─────► X
   │         │
 u │         │ u
   ▼  f(a)   ▼
   X ─────► X ,
```

that is, $f(a) = u \circ a \circ u^{-1}$ for every $a \in \operatorname{Aut}_{S}(X)$. Writing $i(h(m)) = f(i(m))$, one
finds the desired formula.

**Corollary 0.7.bis.** *Let $X$ be an $S$-scheme such that `X_J` is an `S_J`-monoid. Then `L_X` is endowed with a
structure of $S$-monoid, one has a split exact sequence of $S$-monoids:*

<!-- label: III.III.0.7.bis -->

```text
                i           p
1 ──► L′_X ────► L_X ⇄ ──► X⁺ ──► 1
                     s
```

*and the monoid law induced on $L'_{X}$ coincides with its abelian group structure. In particular, if `X_J` is an
`S_J`-group, then `L_X` is an $S$-group and is the semidirect product of $X^{+}$ and $L'_{X}$.*

*Proof.* Indeed, since `X_J` is an `S_J`-monoid, then $X^{+} = \prod_{S_{J}/S} X_{J}$ is an $S$-monoid (indeed, one has
$X^{+}(Y) = X_{J}(Y_{J})$ for every $Y \to S$). For every $S$-scheme $Y$, denote by $\tilde{Y}_{J}$ the `Y_J`-affine
scheme corresponding to the quasi-coherent $O_{Y_{J}}$-algebra $O_{Y_{J}} \oplus J \cdot O_{Y}$ (i.e. the graded algebra
associated to the filtration $O_{Y} \supset J \cdot O_{Y}$). Then $L_{X}(Y)$ is identified with $X_{J}(\tilde{Y}_{J})$
and $L'_{X}(Y)$ with the kernel of the morphism $p : X_{J}(\tilde{Y}_{J}) \to X_{J}(Y_{J})$ induced by the "zero
section" $Y_{J} \to \tilde{Y}_{J}$ (i.e. by the morphism of $O_{Y_{J}}$-algebras $O_{\tilde{Y}_{J}} \to O_{Y_{J}}$
vanishing on the ideal $J \cdot O_{Y}$). One has therefore, for every $Y \to S$, a split exact sequence of monoids,
functorial in $Y$:

```text
                       i              p
1 ──► L′_X(Y) ──────► L_X(Y) ⇄ ──► X⁺(Y) ──► 1 .
                            s
```

It remains to see that the monoid law induced on $L'_{X}$ coincides with its abelian group structure. Denote by `µ` the
monoid law of `L_X` and $e$ its unit section; one must show that for all $m, m' \in L'_{X}(Y)$, one has

```text
µ(m · e, m′ · e) = (m + m′) · e .
```

This can be seen in either of the following ways. On the one hand, one can revisit the proof of equality (0.1.10 (∗)) by
replacing the morphism $f : X \to W$ appearing there with the morphism `µ : L_X ×_S L_X → L_X`. Identifying $X^{+}(Y) =
X_{J}(Y_{J})$ with its image by $s$ in $L_{X}(Y) = X_{J}(\tilde{Y}_{J})$, one obtains that, for all $g, g' \in
X_{J}(Y_{J})$ and $m, m' \in L'_{X}(Y)$, one has

```text
µ(m · g, m′ · g′) = L_µ^{(g, g′)}(m, m′) · µ(g, g′),                      (⋆)
```

where `L_µ^{(g, g′)}` denotes the morphism derived from `µ` at the point $(g, g')$ (i.e. $\tilde{Y}_{J}$ is above $L_{X}
\times_{S} L_{X}$ via $(g, g')$). In particular, one has `µ(m · e, m′ · e) = L_µ^{(e, e)}(m, m′) · e`; now
`L_µ^{(e, e)}(m, m′) = L_{ℓ_e}(m′) + L_{r_e}(m)`, where $\ell_{e}$ (resp. $r_{e}$) denotes left (resp. right)
translation by $e$, which is the identity map of `X_J`, whence `L_µ^{(e, e)}(m, m′) = m + m′`.

Alternatively, one can proceed as follows (cf. the proof of [DG70], § II.4, Th. 3.5). By Lemma 0.1.11, the formation of
$X^{+}$ and of `L_X` "commutes with products", and hence the same holds for $L'_{X}$; it follows that the morphism
`µ′ : L′_X × L′_X → L′_X` induced by `µ` is a homomorphism for the abelian-group structure. One then deduces from Lemma
3.10 of Exp. II that `µ′` coincides with the abelian-group law.

<!-- original page 95 -->

**0.8.**[^N.D.E-III-27] Let now $X$ be an $S$-scheme such that `X_J` is an `S_J`-group. Suppose there exists an
$S$-morphism

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

is the group law of `X_J`. (An important particular case of the preceding situation will be the case where $X$ is an
$S$-group and one takes for $P$ its group law.) From this one deduces a morphism

```text
L_P : L_X × L_X ≃ L_{X ×_S X} ──► L_X
              S
```

which, in fact, does not depend on $P$, because it is computed by means of the group law `P_J` of `X_J`, as we shall now
see.[^N.D.E-III-28] Indeed, by (ii) and (iii) of 0.2, for every $Y \to S$ and $x, x' \in X(Y)$, $m, m' \in L'_{X}(Y)$,
one has

```text
P(m · x, m′ · x′) = L_P^{(x, x′)}(m, m′) · (x, x′) = L_P^{(x, x′)}(m, m′) · µ(g, g′)
```

where $g$ (resp. $g'$) is the image of $x$ (resp. $x'$) in $X^{+}(Y)$. Moreover (cf. the proof of 0.10), $L^{(x,
x')}_{P}$ equals `L_µ^{(g, g′)}` and, by 0.7.bis (⋆), this is the element of $L'_{X}(Y)$ defined by the following
equality in $L_{X}(Y)$:

```text
L_µ^{(g, g′)}(m, m′) · µ(g, g′) = µ(m · g, m′ · g′),
```

that is, if we denote by $\times$ (instead of `µ`) the group law of `L_X` and `Ad` the "adjoint action" of $X^{+}$ on
$L'_{X}$ (which factors through $X_{0}$ and is induced by the adjoint action of $X_{0}$ on $\omega^{1}_{X_{0}/S_{0}}$),
one obtains that

```text
L_µ^{(g, g′)}(m, m′) × g × g′ = m × g × m′ × g′ = (m × Ad(g)(m′)) × g × g′
```

hence finally $L^{(x, x')}_{P}(m, m') = m \times Ad(g)(m')$. We therefore obtain:

**Proposition 0.8.** *Let $P : X \times_{S} X \to X$ be an $S$-morphism such that `P_J` endows `X_J` with a structure of
`S_J`-group. Denote by $\times$ the group law of $L'_{X}$ and by $(m, x) \mapsto m \cdot x$ the morphism $L'_{X}
\times_{S} X \to X$ defining the action of $L'_{X}$ on $X$, and let $Ad : X^{+} \to \operatorname{Aut}_{S-gr.}(L'_{X})$
be the "adjoint action" of $X^{+}$ on $L'_{X}$ (which is induced by the adjoint action of $X_{0}$ on
$\omega^{1}_{X_{0}/S_{0}}$). Then, for every $S' \to S$ and $x, x' \in X(S')$, $m, m' \in L'_{X}(S')$, one has:*

```text
P(m · x, m′ · x′) = (m × Ad(p_X(x))(m′)) · P(x, x′).        (0.8.1)
```

*If $X$ is an $S$-group, we shall denote by $\ast$ its law, $e$ its unit section, and $i$ the $S$-morphism defined by:*

$$ i(m) = m \cdot e , $$

*for every $S' \to S$ and $m \in L'_{X}(S')$.*

<!-- original page 96 -->

**Corollary 0.9.** *Let $X$ be an $S$-group. Then $X^{+}$ is naturally endowed with a structure of $S$-group, and
$p_{X}$ is a morphism of $S$-groups. Moreover, the $S$-morphism*

<!-- label: III.III.0.9 -->

```text
i : L′_X ──► X,    m ↦ m · e
```

*is an isomorphism of $S$-groups from $L'_{X}$ onto $Ker(p_{X})$, and one has, for all $S' \to S$, $x' \in X(S')$, $m
\in L'_{X}(S')$:*

```text
m · x′ = (m · e) ∗ x′ = i(m) ∗ x′ .                  (0.9.1)
```

The first two assertions have already been proved in 0.1.2. Since $X$ is formally principal homogeneous over $X^{+}$
under $L_{X} = L'_{X} \times_{S} X^{+}$, the morphism $i$ is indeed an isomorphism of $S$-functors from $L'_{X}$ onto
the kernel of $p_{X}$. The fact that $i$ is a morphism of groups and the formula (0.9.1) follow from formula (0.8.1)
applied respectively to $x = x' = e$, and to $x = e$, $m' = 1$.

**Corollary 0.10.** *Let $X$ be an $S$-group. With the preceding notations, for every $S' \to S$ and all $x \in X(S')$
and $m' \in L'_{X}(S')$, one has*

<!-- label: III.III.0.10 -->

```text
x ∗ i(m′) ∗ x⁻¹ = i(Ad(p_X(x))(m′)) .                 (0.10.1)
```

This follows from the equality $i(m') \ast x^{-1} = m' \cdot x^{-1}$ and from (0.8.1) applied to $m = 1$ and $x' =
x^{-1}$.

When $X$ is an $S$-group, we have therefore explicitly determined the kernel of $X \to X^{+}$ and the action of the
inner automorphisms of $X$ on this kernel. We shall now see that one can do the same for certain $S$-group functors not
necessarily representable. One case will be useful to us, namely that of the `Aut` functors (I, 1.7). Let us state at
once:

**Proposition 0.11.** *Let $E$ be an $S$-scheme. Denote $X = \operatorname{Aut}_{S}(E)$. The kernel of the morphism of
$S$-group functors*

<!-- label: III.III.0.11 -->

```text
p_X : X ──► X⁺
```

*is canonically identified with the $S$-functor in commutative groups $L'_{X}$ defined by*

```text
Hom_S(Y, L′_X) = Hom_{O_{E₀ ×_{S₀} Y₀}}(Ω¹_{E₀/S₀} ⊗_{O_{S₀}} O_{Y₀}, J · O_{E ×_S Y}),
```

*where $Y$ denotes a variable $S$-scheme.*

Indeed, if $Y$ is a variable $S$-scheme, one has $\operatorname{Hom}_{S}(Y, X) = \operatorname{Aut}_{Y}(E \times_{S}
Y)$, and

```text
Hom_S(Y, X⁺) = Hom_S(Y_J, X) = Aut_{Y_J}(E ×_S Y_J) = Aut_{Y_J}((E ×_S Y) ×_Y Y_J).
```

<!-- original page 97 -->

Applying 0.7 b) to the $Y$-scheme $E \times_{S} Y$, one obtains an isomorphism of groups:

```text
Hom_S(Y, L′_X) ≃ Ker(Hom_S(Y, X) ──► Hom_S(Y, X⁺)),
```

an isomorphism that one verifies easily to be functorial in the $S$-scheme $Y$. One thus obtains an isomorphism of
$S$-groups

```text
L′_X ≃ Ker(X ──► X⁺),
```

which completes the proof of Proposition 0.11.

**Corollary 0.12.**[^N.D.E-III-29] *We keep the notations of 0.11: $E$ is an $S$-scheme and $X =
\operatorname{Aut}_{S}(E)$. One has a natural action $f$ of $X$ on $L'_{X}$ defined as follows. For every $S$-scheme
$Y$, one has*

<!-- label: III.III.0.12 -->

```text
Hom_S(Y, X) = Aut_Y(E ×_S Y)
and    Hom_S(Y, L′_X) = Hom_{O_{E₀ ×_{S₀} Y₀}}(Ω¹_{E₀ ×_{S₀} Y₀ / Y₀}, J · O_{E ×_S Y})
```

*(N. B. $\Omega^{1}_{E_{0}/S_{0}} \otimes_{S_{0}} O_{Y_{0}} \simeq \Omega^{1}_{E_{0} \times_{S_{0}} Y_{0} / Y_{0}}$, cf.
EGA IV₄, 16.4.5); the first group acts on the second by transport of structure and this action is indeed functorial in
$Y$. One then has the formula:*

```text
x · i(m) · x⁻¹ = i(f(x) m),                              (0.12.1)
```

*for every $Y \to S$ and all $x \in \operatorname{Hom}_{S}(Y, X)$, $m \in \operatorname{Hom}_{S}(Y, L'_{X})$.*

Indeed, this follows from 0.7 c) applied to the $Y$-scheme $E \times_{S} Y$.

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

*if one supposes $f$ (and therefore $f'$) of finite presentation and $g$ (and therefore $g'$) flat, one has for every
quasi-coherent `O_T`-module $F$*

```text
f_*(F) ⊗_{O_S} O_{S′} = f′_*(F ⊗_{O_S} O_{S′}),
```

*where, more elegantly,*

$$ g*(f_{*}(F)) = f'_{*}(g'*(F)). $$

These two facts hold more generally for a quasi-compact and quasi-separated morphism $f$, cf. ([EGA I, 9.2.1](https://jcreinhold.github.io/ega/i/01-09-complements-on-quasi-coherent-sheaves.html#92-direct-image-of-a-quasi-coherent-sheaf)) and ([EGA
III₁, 1.4.15](https://jcreinhold.github.io/ega/iii/08-ch3-01-cohomology-affine-schemes.html#14-application-to-the-cohomology-of-arbitrary-preschemes)) in the quasi-compact separated case (taking into account EGA III₂, Err_III 25) and ([EGA IV₁, 1.7.4](https://jcreinhold.github.io/ega/iv/12-ch4-01-relative-finiteness-conditions.html#17-improvements-of-earlier-results) and
1.7.21).

**Remark 0.14.**[^N.D.E-III-30] *Resume the notations of 0.11: let $E$ be an $S$-scheme, $X = \operatorname{Aut}_{S}(E)$
and $L'_{X}$ the $S$-functor in commutative groups defined by:*

<!-- label: III.III.0.14 -->

```text
L′_X(Y) = Hom_{O_{E₀ ×_{S₀} Y₀}}(Ω¹_{E₀/S₀} ⊗_{O_{S₀}} O_{Y₀}, J · O_{E ×_S Y})
         = Hom_{O_{E ×_S Y}}(Ω¹_{E/S} ⊗_{O_S} O_Y, J · O_{E ×_S Y})
         = Γ(E ×_S Y, Hom_{O_{E ×_S Y}}(Ω¹_{E/S} ⊗_{O_S} O_Y, J · O_{E ×_S Y})).
```

Suppose $Y$ flat over $S$; then one has isomorphisms:

```text
J · O_{E ×_S Y} ←─∼─ (J · O_E) ⊗_{O_S} O_Y ─∼→ (J · O_E) ⊗_{O_{S₀}} O_{Y₀} .
```

Suppose moreover $E$ of finite presentation over $S$; then $\Omega^{1}_{E/S}$ is an `O_E`-module of finite presentation
(cf. EGA IV₄, 16.4.22), and hence, by (EGA 0_I, 6.7.6),

```text
Hom_{O_{E ×_S Y}}(Ω¹_{E/S} ⊗_{O_S} O_Y, (J · O_E) ⊗_{O_S} O_Y) ≃ Hom_{O_E}(Ω¹_{E/S}, J · O_E) ⊗_{O_S} O_Y .
```

Denote by $\pi : E \to S$ and $g : Y \to S$ the structural morphisms; applying 0.13 to the diagram

```text
E ◄────g′──── E ×_S Y
│                 │
π                 π′
▼      g          ▼
S ◄────────────── Y ,
```

and to the `O_E`-module $F = \operatorname{Hom}_{O_{E}}(\Omega^{1}_{E/S}, J \cdot O_{E})$, one obtains

```text
Γ(E ×_S Y, g′*F) = Γ(Y, π′_* g′* F) = Γ(Y, g* π_* F) = W(π_* F)(Y).
```

<!-- original page 99 -->

We have therefore shown that, if $E$ is of finite presentation over $S$, one has

```text
L′_X = W(π_* Hom_{O_E}(Ω¹_{E/S}, J · O_E))                        (0.14.1)
```

on the category of $S$-schemes flat over $S$. Note moreover that the module of which we take the $W$ is quasi-coherent,
by (EGA I, 9.1.1 and 9.2.1).

[^N.D.E-III-31] Denote by $L_{0}$ the $S_{0}$-functor

```text
W(π_{0*} Hom_{O_{E₀}}(Ω¹_{E₀/S₀}, J · O_E)).
```

Then, returning to the definition of $L'_{X}(Y)$ and taking into account the isomorphism

```text
J · O_{E ×_S Y} ≃ (J · O_E) ⊗_{O_{S₀}} O_{Y₀},
```

one obtains, by arguing as above, that

```text
L′_X(Y) = L₀(Y₀) = L₀(Y ×_S S₀) = ∏_{S₀/S} L₀(Y).
```

Hence, on the category of $S$-schemes flat over $S$, one has:

```text
L′_X = ∏_{S₀/S} W(π_{0*} Hom_{O_{E₀}}(Ω¹_{E₀/S₀}, J · O_E)).
```

It is not obvious that the action of $X$ on $L'_{X}$ defined in 0.12 comes from an action of $X_{0} =
\operatorname{Aut}_{S_{0}}(E_{0})$ on $L_{0}$; this is however the case when, moreover, $E$ is flat over $S$.

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

Then, for every $S_{0}$-scheme $T$, one has

```text
L₀(T) ≃ Hom_{O_{E₀ ×_{S₀} T}}(Ω¹_{E₀ ×_{S₀} T / T}, J ⊗_{O_{S₀}} O_{E₀ ×_{S₀} T})
```

and $\operatorname{Hom}_{S_{0}}(T, X_{0}) = \operatorname{Aut}_{T}(E_{0} \times_{S_{0}} T)$ acts by transport of
structure on $L_{0}(T)$, functorially in $T$; finally, for every $S$-scheme $Y$ flat over $S$, the action by transport
of structure of $\operatorname{Hom}_{S}(Y, X) = \operatorname{Aut}_{Y}(E \times_{S} Y)$ on $L'_{X}(Y) = L_{0}(Y_{0})$
factors through $\operatorname{Aut}_{Y_{0}}(E_{0} \times_{S_{0}} Y_{0})$.

Let us finally extract from (SGA 1, III) the following two propositions.

**Proposition 0.15.** *(SGA 1, III, 6.8)[^N.D.E-III-32] For every `S_J`-scheme $Y$ smooth over `S_J` and affine, there
exists an $S$-scheme $X$ smooth over $S$ such that $X \times_{S} S_{J} \simeq Y$, and such an $X$ is unique up to
(non-unique) isomorphism.*

<!-- label: III.III.0.15 -->

**Proposition 0.16.** *(SGA 1, III, 5.5)[^N.D.E-III-33] Let $X$ be an $S$-scheme smooth over $S$. For every affine
$S$-scheme $Y$, the canonical map*

<!-- label: III.III.0.16 -->

```text
p_X(Y) : Hom_S(Y, X) ──► Hom_S(Y, X⁺) = Hom_{S_J}(Y_J, X_J)
```

*is surjective.*

**Corollary 0.17.** *Let $E$ be an $S$-scheme smooth over $S$ and affine; denote $X = \operatorname{Aut}_{S}(E)$. For
every affine $S$-scheme $Y$, the canonical map*

<!-- label: III.III.0.17 -->

```text
Aut_Y(E ×_S Y) = Hom_S(Y, X) ──► Hom_S(Y, X⁺) = Aut_{Y_J}(E_J ×_{S_J} Y_J)
```

*is surjective.*

Indeed, $Y \times_{S} E$ is affine over $Y$, itself affine, so affine. Applying 0.16, one deduces that every
`S_J`-morphism $Y_{J} \times_{S_{J}} E_{J} \to E_{J}$ extends to an $S$-morphism $Y \times_{S} E \to E$. [^N.D.E-III-34]
In other words, every `Y_J`-endomorphism of $Y_{J} \times_{S_{J}} E_{J}$ lifts to a $Y$-endomorphism of $Y \times_{S}
E$. Then, 0.7 a) shows that every `Y_J`-automorphism of $Y_{J} \times_{S_{J}} E_{J}$ lifts to a $Y$-automorphism of $Y
\times_{S} E$, which is the announced property.

## 1. Extensions and cohomology

<!-- label: III.III.1 -->

<!-- original page 101 -->

### 1.1

<!-- label: III.III.1.1 -->

Let $C$ be a category stable under fibered products.[^N.D.E-III-35] Let $S$ be an object of $C$, $G$ an (representable)
$S$-group, and $F$ an $S$-functor in commutative groups on which $G$ acts. We defined in (I, 5.1) the cohomology groups
$H^{n}(G, F)$. Recall that these are the homology groups of a complex denoted $C\ast(G, F)$ where, denoting $(G/S)^{n} =
G \times_{S} \cdot \cdot \cdot \times_{S} G$ ($n$ factors),

```text
Cⁿ(G, F) = Hom_S((G/S)ⁿ, F).
```

Since $G$, and hence the $(G/S)^{n}$, are representable, one has also

$$ C^{n}(G, F) = F((G/S)^{n}); $$

from this, and from the definition of the boundary operator, one sees that the complex $C\ast(G, F)$ depends only on the
restriction of $F$ to the full subcategory of $C/S$ whose objects are the cartesian powers of $G$ over $S$.
Consequently, one has the:

**Lemma 1.1.1.** *Let $C$ be a category stable under fibered products,[^N.D.E-III-35] $S$ an object of $C$, $G$ a
representable $S$-group. Denote by $C(G)$ the full subcategory of $C/S$ whose objects are the cartesian powers of $G$
over $S$. Let $F$ and $F'$ be two $S$-functors in commutative groups on which $G$ acts. If $F$ and $F'$ have the same
restriction to $C(G)$, one has a canonical isomorphism*

<!-- label: III.III.1.1.1 -->

```text
H∗(G, F) ──∼──► H∗(G, F′).
```

### 1.1.2. Cohomology and restriction of scalars

<!-- label: III.III.1.1.2 -->

[^N.D.E-III-36] Let us state another comparison result. Let now $T \to S$ be a morphism in $C$. If $F$ is a $T$-functor
in commutative groups, then the functor obtained by "restriction of scalars" (cf. Exp. II, 1)

$$ F_{1} = \prod_{T/S} F $$

is an $S$-functor in commutative groups and one has a morphism of $S$-group functors

```text
u : ∏_{T/S} Aut_{T-gr.}(F) ──► Aut_{S-gr.}(F₁) .[^N.D.E-III-37]
```

Let now $G$ be an $S$-group functor and let

```text
G_T ──► Aut_{T-gr.}(F)
```

be an action of `G_T` on $F$. By definition of the functor $\prod_{T/S}$, one deduces a morphism of $S$-group functors

```text
G ──► ∏_{T/S} Aut_{T-gr.}(F)
```

whence, by composition with $u$, an action of $G$ on $F_{1} = \prod_{T/S} F$.[^N.D.E-III-38]

<!-- original page 102 -->

**Lemma 1.1.2.** *Under the preceding conditions, one has a canonical isomorphism*

<!-- label: III.III.1.1.2 -->

```text
H∗(G, ∏_{T/S} F) ≃ H∗(G_T, F).
```

Indeed, by the definition of cohomology, the standard complexes are canonically isomorphic.

### 1.2. Lifting of group morphisms

<!-- label: III.III.1.2 -->

[^N.D.E-III-39] Following the general principles, we lay down the following definition:

**Definition 1.2.1.** *Let `1 → M ──u──► E ──v──► G` be a sequence of morphisms of `Ĉ`-groups. We say that it is
**exact** if the following equivalent conditions are verified:*

<!-- label: III.III.1.2.1 -->

*(i) for every $S \in Ob C$, the following sequence of ordinary groups is exact:*

```text
1  ──►  M(S) ──u(S)──► E(S) ──v(S)──► G(S)
```

*(ii) for every object $H$ of `Ĉ`, the following sequence of ordinary groups is exact:*

```text
1  ──►  Hom(H, M) ──u(H)──► Hom(H, E) ──v(H)──► Hom(H, G)
```

Taking in particular $H = G$ in (ii), one sees that the set of sections of $v$ (not respecting *a priori* the group
structures) is empty or principal homogeneous under $\operatorname{Hom}(G, M)$. Suppose it is non-empty; so let

```text
s : G ──► E
```

be a section of $v$. Then for every $S \in Ob C$ and every $x \in G(S)$, the element $s(x)$ of $E(S)$ defines an inner
automorphism of `E_S` which normalizes `M_S` (more correctly, the image of `M_S` by $u_{S}$), hence an automorphism of
`M_S`.

<!-- original page 103 -->

**Scholie 1.2.1.1.**[^N.D.E-III-40] *If $M$ is commutative, one sees "set-theoretically" that this automorphism does not
depend on the chosen section, but only on $x$, and depends multiplicatively on it. In summary, to every exact sequence*

<!-- label: III.III.1.2.1.1 -->

```text
(E)     1  ──►  M  ──u──►  E  ──v──►  G
```

*such that $M$ is commutative and that $v$ admits a section, is associated a morphism of `Ĉ`-groups*

```text
G ──► Aut_{Ĉ-gr.}(M)
```

*which is called the **action of $G$ on $M$ defined by the extension `(E)`**.*

**Definition 1.2.1.2.** *We saw in (I, 2.3.7) that $v$ admits a section which is a morphism of `Ĉ`-groups if and only if
the extension `(E)` is isomorphic ("as an extension") to the semidirect product of $M$ by $G$ relative to the preceding
action. Such a section of $v$ will be called a **section of the extension `(E)`**, or simply a **section of `(E)`**.*

<!-- label: III.III.1.2.1.2 -->

*If $s$ is a section of `(E)` and if $m \in \Gamma(M) \simeq Ker(\Gamma(E) \to \Gamma(G))$ (for the definition of
$\Gamma$, see I, 1.2), then the morphism $G \to E$ defined by[^N.D.E-III-41]*

```text
x ↦ u(m) s(x) u(m)⁻¹
```

*is also a section of `(E)`, said to be **deduced from $s$ by the inner automorphism defined by $m$** (or by $u(m)$).*

**Lemma 1.2.2.** *Let `(E) : 1 → M ──u──► E ──v──► G` be an exact sequence of `Ĉ`-groups such that $M$ is commutative
and $v$ admits a section. Let $G$ act on $M$ in the manner defined by `(E)`.*

<!-- label: III.III.1.2.2 -->

*(i) The extension `(E)` canonically defines a class $c(E) \in H^{2}(G, M)$ whose vanishing is necessary and sufficient
for the existence of a section of `(E)`.*

<!-- original page 104 -->

*(ii) If $c(E) = 0$, the set of sections of `(E)` is principal homogeneous under the group $Z^{1}(G, M)$, and the set of
sections of `(E)` modulo the action of the inner automorphisms defined by the elements of $\Gamma(M)$ is principal
homogeneous under the group $H^{1}(G, M)$.*

*(iii)[^N.D.E-III-42] Let $s$ be a section of `(E)`; the set of conjugates of $s$ by the inner automorphisms defined by
$\Gamma(M)$ is in bijection with $\Gamma(M)/H^{0}(G, M)$.*

*Proof.* It proceeds exactly as in the case of ordinary groups, the fact that one starts from a section of $v$ ensuring
the functoriality of the set-theoretic computations. Let us briefly indicate the principal steps.

**a)** To each section $s$ of $v$, one associates the morphism

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

it suffices to substitute the definition of `Ds` into this formula to find (without using any commutativity) $Ds \in
Z^{2}(G, M)$.

**b)** If $s$ and $s'$ are two sections of $v$, there exists $f : G \to M$ such that $s(x) = f(x) s'(x)$. One then has

```text
Ds′(x, y) = f⁻¹(xy) Ds(x, y) s(x) f(y) s(x)⁻¹ f(x),
          = Ds(x, y) · f⁻¹(xy) · (s(x) f(y) s(x)⁻¹) · f(x),
```

<!-- original page 105 -->

i.e.

$$ Ds' = Ds \cdot \partial^{1} f. $$

[^N.D.E-III-44] This shows that the class of `Ds` in $H^{2}(G, M)$ does not depend on the chosen section $s$ of $v$; it
is the class $c(E)$ of the extension `(E)`.

**c)** Let $s$ and $s'$ be two sections of $v$ and let $m \in \Gamma(M)$. Then, the equality $s(x) = m^{-1} s'(x) m$
(for every $x \in G(S)$, $S \in Ob C$) is equivalent to

```text
s(x) = m⁻¹ s′(x) m s′(x)⁻¹ s′(x),   i.e.   s = ∂⁰ m · s′ .
```

In particular, the stabilizer of $s$ in $\Gamma(M)$ is the subgroup of $m \in \Gamma(M)$ such that $\partial^{0} m =
e_{M}$, i.e. the subgroup $H^{0}(G, M)$. This already proves (iii).

**d)** The reasoning is now habitual.[^N.D.E-III-45] Let $s_{0}$ be an arbitrary section of $v$; there exists a section
$s$, necessarily of the form $s = f \cdot s_{0}$, which is a morphism of groups, i.e. which satisfies $Ds = 0$, if and
only if $(Ds_{0})^{-1} = \partial^{1} f$, i.e., if and only if the class $c(E)$ is zero. This proves (i).

In this case, the set of sections of `(E)` consists of the sections $s' = h \cdot s$, where $h : G \to M$ satisfies
$\partial^{1} h = 0$, i.e. $h \in Z^{1}(G, M)$. Moreover, by point c), two such sections $h_{1} \cdot s$ and $h_{2}
\cdot s$ are conjugate under $\Gamma(M)$ if and only if $h_{1}$ and $h_{2}$ have the same image in $H^{1}(G, M)$. This
proves (ii).

Let still

```text
(E)     1  ──►  M  ──u──►  E  ──v──►  G
```

be an exact sequence of `Ĉ`-groups with $M$ commutative. Let

```text
f : H ──► G
```

be a morphism of `Ĉ`-groups. Consider $E_{f} = H \times_{G} E$; it is a `Ĉ`-group and the projection $v_{f} : E_{f} \to
H$ is a morphism of `Ĉ`-groups. Likewise for $e_{f} : E_{f} \to E$. On the other hand, if one sends $M$ into $E$ via $u$
and into $H$ via the unit morphism, one defines a morphism of `Ĉ`-groups $u_{f} : M \to E_{f}$. We have thus constructed
a commutative diagram of `Ĉ`-groups:

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

**Lemma 1.2.3.** *(i) The sequence $(E_{f})$ is exact.*

<!-- label: III.III.1.2.3 -->

*(ii) The map $s \mapsto e_{f} \circ s = f'$ realizes a bijective correspondence between the morphisms*

```text
s : H ──► E_f
```

*such that $v_{f} \circ s = id$ (that is, the sections of $v_{f}$) and the morphisms*

```text
f′ : H ──► E
```

*such that $v \circ f' = f$ (that is, the morphisms $f'$ "lifting" $f$).*

*(iii) In the preceding correspondence, sections of $(E_{f})$ and morphisms of groups $f'$ lifting $f$ correspond.*

Applying Lemma 1.2.2 to the extension $(E_{f})$ and taking into account 1.2.3, one obtains the following proposition
(which formally contains 1.2.2):

**Proposition 1.2.4.** *Let `(E) : 1 → M → E ──v──► G` be an exact sequence of `Ĉ`-groups with $M$ commutative. Let*

<!-- label: III.III.1.2.4 -->

```text
f : H ──► G
```

*be a morphism of `Ĉ`-groups; suppose it lifts to a morphism (not necessarily of groups) $f' : H \to E$. Let $H$ act on
$M$ by the composite morphism (multiplicative and independent of the choice of $f'$),*

```text
H ──f′──► E ──int──► Aut_{Ĉ-gr.}(M).
```

*(i) The morphism $f$ canonically defines a class $c(f) \in H^{2}(H, M)$ whose vanishing is necessary and sufficient for
the existence of a morphism of `Ĉ`-groups*

```text
f′ : H ──► E
```

*lifting $f$.*

<!-- original page 107 -->

*(ii) If $c(f) = 0$, the set of morphisms of `Ĉ`-groups $f'$ lifting $f$, modulo the action of the inner automorphisms
defined by elements of $\Gamma(M)$ (i.e. by elements $m$ of $\Gamma(E)$ such that $v(m) = e$), is principal homogeneous
under $H^{1}(H, M)$.*

*(iii) If $f' : H \to E$ is a morphism of groups lifting $f$, the set of transforms of $f'$ by the inner automorphisms
defined by the elements of $\Gamma(M)$ is isomorphic to $\Gamma(M)/\Gamma(M^{H}) = \Gamma(M)/H^{0}(H, M)$.*

### 1.3. Extensions of group laws

<!-- label: III.III.1.3 -->

Consider the following situation: one has a morphism of `Ĉ`

```text
(†)     p : X ──► Y
```

and a commutative `Ĉ`-group $M$ acting on $X$, such that $X$ is formally principal homogeneous above $Y$ under `M_Y`.

If $g : Y \to Z$ is an arbitrary morphism of `Ĉ`, then $g \circ p : X \to Z$ is invariant under $M$: for each $S \in Ob
C$, $(g \circ p)(S)$ is invariant under the action of $M(S)$ acting on $X(S)$. Conversely, we shall assume the following
condition verified for $n = 1, 2, 3, 4$.

$(+)_{n}$ : Every morphism from $X^{n}$ to $M$, invariant under the action of $M^{n}$ on $X^{n}$, factors uniquely
through $p^{n} : X^{n} \to Y^{n}$ (where the powers $n$ denote cartesian powers).

**Lemma 1.3.1.** *(i) If $h$ is a morphism from $Y$ to $M$, the automorphism $u_{h}$ of $X$ defined set-theoretically by
$x \mapsto h(p(x)) \cdot x$ preserves the fibers of $p$ and commutes with the actions of $M$ on $X$,[^N.D.E-III-46] i.e.
for all $S \in Ob C$ and $x \in X(S)$, $m \in M(S)$, one has*

<!-- label: III.III.1.3.1 -->

```text
p(h(p(x)) · x) = p(x),     m · (h(p(x)) · x) = h(p(m · x)) · (m · x) .
```

*(ii) This construction realizes a bijective correspondence between morphisms from $Y$ to $M$ and automorphisms of $X$
preserving the fibers of $p$ and commuting with the actions of $M$.*

The first part is clear, since $p(m \cdot x) = p(x)$ and $M$ is commutative.

<!-- original page 108 -->

Conversely, an automorphism $u$ of $X$ preserving the fibers of $p$ is written set-theoretically $x \mapsto g(x) \cdot
x$, where $g$ is some morphism from $X$ to $M$. If $u$ commutes with the actions of $M$, the morphism $g$ is invariant
under $M$[^N.D.E-III-47] and one concludes by condition $(+)_{1}$.

We now suppose given in addition a group law on $Y$ and an action of $Y$ on $M$, that is, a morphism of `Ĉ`-groups:

```text
(‡)     f : Y ──► Aut_{Ĉ-gr.}(M).
```

**Definition 1.3.2.** *A composition law on $X$*

<!-- label: III.III.1.3.2 -->

```text
P : X × X ──► X
```

*is said to be **admissible** if it verifies the following two conditions:*

*(i) $P$ lifts the group law of $Y$, i.e. the diagram*

```text
            P
X × X ─────────► X
(p,p)│           │ p
     ▼           ▼
Y × Y ─────────► Y
```

*is commutative.*

*(ii) For every $S \in Ob C$ and all $x, y \in X(S)$, $m, n \in M(S)$, one has the following relation:*

```text
(++)     P(m · x, n · y) = m · f(p(x))(n) · P(x, y).
```

**Proposition 1.3.3.** *For a group law $\ast$ on $X$ to be admissible, it is necessary and sufficient that the
following four conditions be satisfied:*

<!-- label: III.III.1.3.3 -->

*(i) $p : X \to Y$ is a morphism of groups.*

<!-- original page 109 -->

*(ii) The morphism $i : M \to X$ defined by $i(m) = m \cdot e_{X}$ is an isomorphism of groups from $M$ onto $Ker(p)$,
that is to say: one has set-theoretically $(m \cdot e_{X}) \ast (n \cdot e_{X}) = (mn) \cdot e_{X}$.*

*(iii) One has $m \cdot x = (m \cdot e_{X}) \ast x = i(m) \ast x$ for each $m \in M(S)$, $x \in X(S)$.*

*(iv) The inner automorphisms of $X$ act on $Ker(p)$ by the set-theoretic formula*

```text
x ∗ i(m) ∗ x⁻¹ = i(f(p(x)) m).
```

The proof is immediate.

**Lemma 1.3.4.**[^N.D.E-III-48] *Let $h$ be a morphism $Y \to M$ and $u_{h}$ the automorphism $x \mapsto h(p(x)) \cdot
x$ of $X$ (cf. 1.3.1). Let $P$ be an admissible composition law (resp. an admissible group law) on $X$ and let $P'$ be
the composition law on $X$ deduced from $P$ by means of $u_{h}$, i.e. $P'(x, y) = u^{-1}_{h}(P(u_{h}(x), u_{h}(y)))$.
Then:*

<!-- label: III.III.1.3.4 -->

*(i) $P'$ is an admissible composition law (resp. an admissible group law).*

*(ii) For every $x, y \in X(S)$ ($S \in Ob C$), setting $v = p(x)$ and $w = p(y)$, one has*

```text
P′(x, y) = (h(vw)⁻¹ · h(v) · f(v)(h(w))) · P(x, y) = (∂¹ h)(p(x), p(y)) · P(x, y).
```

*Proof.* One has $u^{-1}_{h} = u_{h^{\vee}}$, where $h^{\vee} : Y \to M$ is defined by $h^{\vee}(y) = h(y)^{-1}$. By
1.3.2 (i) and (ii), one has $P(h(v) \cdot x, h(w) \cdot y) = h(v) \cdot f(v)(h(w)) \cdot P(x, y)$ and $p(P(x, y)) = vw$,
whence

```text
P′(x, y) = (h(vw)⁻¹ · h(v) · f(v)(h(w))) · P(x, y) = (∂¹ h)(p(x), p(y)) · P(x, y).
```

It is then immediate that $P'$ verifies conditions (i) and (ii) of 1.3.2.

**Definition 1.3.5.** *Two admissible composition laws deduced from one another by the procedure of 1.3.4 are said to be
**equivalent**.[^N.D.E-III-49]*

<!-- label: III.III.1.3.5 -->

<!-- original page 110 -->

**Proposition 1.3.6.** *Suppose there exists an admissible composition law on $X$. Then:*

<!-- label: III.III.1.3.6 -->

*(i) There exists a class $c \in H^{3}(Y, M)$ (canonically determined), whose vanishing is necessary and sufficient for
the existence of an admissible **associative** composition law on $X$.*

*(ii) If $c = 0$, the set of admissible and associative composition laws (resp. of equivalence classes of admissible and
associative composition laws) on $X$ is principal homogeneous under $Z^{2}(Y, M)$ (resp. $H^{2}(Y, M)$).*

The proof proceeds in several steps.

**a)** Let $P$ be an admissible composition law on $X$. Since $P$ lifts the composition law of $Y$ which is associative,
there exists a unique morphism $a : X^{3} \to M$ such that

```text
(∗)     P(x, P(y, z)) = a(x, y, z) · P(P(x, y), z).
```

By applying conditions 1.3.2 (i) and (ii), one sees at once that $a$ is invariant under the action of $M^{3}$ on
$X^{3}$,[^N.D.E-III-50] whence, by applying hypothesis $(+)_{3}$, the following result:

**(1)** There exists a unique morphism $DP : Y^{3} \to M$ such that

```text
P(x, P(y, z)) = DP(p(x), p(y), p(z)) · P(P(x, y), z),
```

and $P$ is associative if and only if $DP = 0$.

**b)** Compute step by step $P(P(P(x, y), z), t)$ by means of the preceding formula. Setting $p(x) = u$, $p(y) = v$,
$p(z) = w$, $p(t) = h$, one obtains[^N.D.E-III-51] the following pentagonal diagram, where an arrow `a ──m──► b` means
that $b = m \cdot a$:

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

i.e., $\partial^{3} DP(u, v, w, h) = e_{M}$. As moreover the first member of the preceding formula can be written, by
means of $P$ and $a$, as the expression in $(x, y, z, t)$ of a certain morphism $X^{4} \to M$, it follows from the
uniqueness hypothesis in $(+)_{4}$ that $\partial^{3} DP$ and $e_{M}$, which factor through the same morphism, are
equal, hence

**(2)** `DP` is a cocycle, i.e. one has $DP \in Z^{3}(Y, M)$.

**c)** If $P$ and $P'$ are two admissible composition laws on $X$, there exists a unique morphism

```text
b : X² ──► M
```

such that $P'(x, y) = b(x, y) \cdot P(x, y)$. Applying 1.3.2 (ii) to $P$ and $P'$, one sees that $b$ is invariant under
$M^{2}$, whence, by $(+)_{2}$:

<!-- original page 111 -->

**(3)** For every pair of admissible composition laws $(P, P')$, there exists a unique $d(P, P') : Y^{2} \to M$ such
that

```text
P′(x, y) = d(P, P′)(p(x), p(y)) · P(x, y),
```

and the set of admissible composition laws becomes in this way principal homogeneous under $\operatorname{Hom}(Y^{2}, M)
= C^{2}(Y, M)$.

**d)** Under the preceding conditions, one has the formula:

```text
(4)     DP′ − DP = ∂² d(P, P′).
```

**e)** $P$ and $P'$ are equivalent if and only if there exists a morphism $h \in C^{1}(Y, M) = \operatorname{Hom}(Y, M)$
such that $d(P, P') = \partial^{1} h$; this follows from the definition of equivalence and from 1.3.4 (ii).

**f)** It now only remains to conclude: one seeks a $P'$ that is associative, i.e. such that $DP' = e_{M}$. Now `DP` is
a cocycle whose class in $H^{3}(Y, M)$ does not depend on the chosen admissible composition law $P$ (by (3) and (4)).
This class is the desired obstruction $c$. One will be able to choose a $P'$ answering the conditions if and only if $c
= 0$; indeed, choosing an arbitrary $P$, one will have to solve, by (1):

```text
0 = DP′ = DP + ∂² d(P, P′),
```

which is possible by (3) and (4) if and only if $c = 0$. The set of associative $P'$ is principal homogeneous under
$Z^{2}(Y, M)$, again by (3) and (4). The set of associative $P'$ up to equivalence is principal homogeneous under
$H^{2}(Y, M)$ by (e).

## 2. Infinitesimal extensions of a morphism of group schemes

<!-- label: III.III.2 -->

<!-- original page 112 -->

Resume the notations of § 0. Let $Y$ and $X$ be two $S$-group functors. Let $M$ be the kernel of the morphism of groups
$p_{X} : X \to X^{+}$. One thus has an exact sequence of $S$-group functors

```text
1 ──► M ──► X ──p_X──► X⁺ .
```

By definition of $X^{+}$, one has isomorphisms

```text
Hom_S(Y, X⁺)       ──∼──► Hom_{S_J}(Y_J, X_J)
Hom_{S-gr.}(Y, X⁺) ──∼──► Hom_{S_J-gr.}(Y_J, X_J),
```

and the morphism

```text
Hom_S(Y, p_X) : Hom_S(Y, X) ──► Hom_S(Y, X⁺)
```

associates to an $S$-morphism $f : Y \to X$ the $S$-morphism $f^{+} : Y \to X^{+}$ corresponding by the preceding
isomorphisms to the `S_J`-morphism $f_{J} : Y_{J} \to X_{J}$ obtained by base change from $f$. If $M$ is commutative,
one can apply to this situation Proposition 1.2.4.

### 2.0

<!-- label: III.III.2.0 -->

[^N.D.E-III-52] In what follows, we shall be interested in the following case: $Y$ is flat over $S$, and $X$ is an
$S$-group functor of one of the following two species:

**a)** $X$ is an $S$-group scheme,

**b)** $X = \operatorname{Aut}_{S}(E)$ where $E$ is an $S$-scheme, of finite presentation over $S$.

Denote by $(Flat)/S$ the category of $S$-schemes flat over $S$. In case (a) (resp. (b)), the $S$-group functor $M =
Ker(X \to X^{+})$, its restriction $L$ to $(Flat)/S$, and the actions of the inner automorphisms of $X$ on $M$, have
been computed in 0.9, 0.5, and 0.10 (resp. 0.11, 0.14, and 0.12). That is to say, in case (a), let $L_{0}$ be the
$S_{0}$-functor in commutative groups defined by: for every $S_{0}$-scheme $T_{0}$,

```text
Hom_{S₀}(T₀, L₀) = Hom_{O_{T₀}}(ω¹_{X₀/S₀} ⊗_{O_{S₀}} O_{T₀}, J ⊗_{O_{S₀}} O_{T₀}),
```

on which $X_{0}$ acts via its adjoint representation in $\omega^{1}_{X_{0}/S_{0}}$; then $L = \prod_{S_{0}/S} L_{0}$,
i.e. for every $S$-scheme $T$, one has $L(T) = L_{0}(T \times_{S} S_{0})$.

In case (b), denote by $\pi$ the structural morphism $E \to S$; then $L$ is the functor in abelian groups on $(Flat)/S$
defined by

```text
Hom_S(T, L) = Γ(T, π_*(Hom_{O_E}(Ω¹_{E/S}, J · O_E)) ⊗_{O_S} O_T),
```

on which $X$, considered as a functor on $(Flat)/S$, acts as we saw in 0.12.

Then, one has an exact sequence of functors in groups on $(Flat)/S$:

```text
(E)     1 ──► L ──► X ──► X⁺ .
```

On the other hand, $Y$ being supposed flat over $S$, the groups $H^{i}(Y, M)$ depend, by 1.1.1, only on the restriction
$L$ of $M$ to $(Flat)/S$. Since $L = \prod_{S_{0}/S} L_{0}$ in case (a), then by 1.1.2, one has in this case
isomorphisms $H^{i}(Y, L) \simeq H^{i}(Y_{0}, L_{0})$.

<!-- original page 113 -->

Then, taking the preceding into account, one deduces from Proposition 1.2.4 the:[^N.D.E-III-53]

**Theorem 2.1.** *Let $S$ be a scheme, $I$ and $J$ two quasi-coherent ideals such that $I \supset J$ and $I \cdot J =
0$, defining the closed subschemes $S_{0}$ and `S_J`, and let:*

<!-- label: III.III.2.1 -->

<!-- original page 114 -->

*— $X$ an $S$-group functor of type (a) or (b), and $L_{0}$, $L$ as above;*

*— $Y$ an $S$-group scheme flat over $S$ and $f_{J} : Y_{J} \to X_{J}$ a morphism of `S_J`-groups.*

*Then:*

*(i) For $f_{J}$ to lift to a morphism of $S$-groups $Y \to X$, it is necessary and sufficient that the following two
conditions be satisfied:*

*(i₁) $f_{J}$ lifts to a morphism of $S$-functors $Y \to X$ (by 1.2.4, this defines an action of $Y$ on $L$, which does
not depend on the chosen lift; moreover, in case (a), the action thus obtained of $Y_{0}$ on $L_{0}$ comes from the
morphism $f_{0} : Y_{0} \to X_{0}$ and from "the adjoint action" of $X_{0}$ on $L_{0}$);*

*(i₂) A certain obstruction $c(f_{J})$, defined canonically by $f_{J}$, vanishes, where $c(f_{J})$ is a class in
$H^{2}(Y, L)$ ($\simeq H^{2}(Y_{0}, L_{0})$ in case (a)).*

*(ii) If the conditions of (i) are satisfied, the set $E$ of morphisms of $S$-group functors $Y \to X$ extending $f_{J}$
is principal homogeneous under $Z^{1}(Y, L)$ ($\simeq Z^{1}(Y_{0}, L_{0})$ in case (a)), and $E$ modulo the action of
the inner automorphisms of $X$ defined by the sections of $X$ over $S$ inducing the unit section of `X_J` over `S_J`, is
principal homogeneous under $H^{1}(Y, L)$ ($\simeq H^{1}(Y_{0}, L_{0})$ in case (a)).*

*(iii) If $f : Y \to X$ is a morphism of $S$-group functors extending $f_{J}$, the set of morphisms $Y \to X$ transforms
of $f$ by the inner automorphisms defined by the sections of $X$ over $S$ inducing the unit section of `X_J` over `S_J`
is isomorphic to $\Gamma(L)/H^{0}(Y, L)$ ($\simeq \Gamma(L_{0})/H^{0}(Y_{0}, L_{0})$ in case (a)).*

**Remark 2.1.1.**[^N.D.E-III-54] *If $f, f' : Y \to X$ are morphisms of $S$-group functors extending $f_{J}$, one
therefore obtains a cocycle $d(f, f') \in Z^{1}(Y, L)$ ($\simeq Z^{1}(Y_{0}, L_{0})$ in case (a)), such that*

<!-- label: III.III.2.1.1 -->

```text
(∗)     f′ = d(f, f′) · f .[^N.D.E-III-55]
```

*We shall denote by $\bar{d}(f, f')$ the image of $d(f, f')$ in $H^{1}(Y, L)$ ($\simeq H^{1}(Y_{0}, L_{0})$ in case
(a)).*

<!-- original page 115 -->

**Remark 2.2.** *We keep the preceding notations; in particular, $Y$ is flat over $S$. In case (b), $L$ is, by (0.14.1),
the restriction to $(Flat)/S$ of the functor*

<!-- label: III.III.2.2 -->

$$ W(\pi_{*}(\operatorname{Hom}_{O_{E}}(\Omega^{1}_{E/S}, J \cdot O_{E}))), $$

*where $\pi : E \to S$ is the structural morphism. In case (a), suppose moreover that $X$ is locally of finite
presentation over $S$; then by (0.6.1), $L$ is the restriction to $(Flat)/S$ of the functor*

$$ \prod_{S_{0}/S} W(\operatorname{Hom}_{O_{S_{0}}}(\omega^{1}_{X_{0}/S_{0}}, J)). $$

In both cases, the module of which we take the $W$ is quasi-coherent, by (EGA I, 9.1.1). Suppose moreover $Y$ affine
over $S$.[^N.D.E-III-56] Then, by (I, 5.3), one obtains:

**a)** $H^{i}(Y, L) = H^{i}(Y_{0}, L_{0}) = H^{i}(Y_{0}, \operatorname{Hom}_{O_{S_{0}}}(\omega^{1}_{X_{0}/S_{0}}, J))$,

**b)** $H^{i}(Y, L) = H^{i}(Y, \pi_{*}(\operatorname{Hom}_{O_{E}}(\Omega^{1}_{E/S}, J \cdot O_{E})))$.

<!-- original page 116 -->

**Remark 2.3.** *1) By 0.16 and 0.17, condition $(i_{1})$ is automatically verified when $Y$ is an affine scheme and*

<!-- label: III.III.2.3 -->

```text
(∗)     {  in case (a), X is smooth over S;
           in case (b), E is smooth and affine over S.
```

*2) Moreover, under these conditions ($Y$ always being supposed flat over $S$, cf. 2.0), one can write in case (a), by
2.2 a) and (0.6.2),*

```text
Hⁱ(Y, L) = Hⁱ(Y₀, L₀) = Hⁱ(Y₀, Lie(X₀/S₀) ⊗_{O_{S₀}} J),
```

*[^N.D.E-III-57] and in case (b), by (0.14.2), 1.1.2 and (I, 5.3),*

```text
Hⁱ(Y, L) = Hⁱ(Y₀, π_{0*} Hom_{O_{E₀}}(Ω¹_{E₀/S₀}, J ⊗_{O_{S₀}} O_{E₀})).
```

Let us now state a certain number of corollaries concerning the case where $Y$ is an $S$-diagonalizable group (I, 4.4);
one knows then (loc. cit. 5.3.3) that if $S$ is affine, $H^{n}(Y, F) = 0$ for $n > 0$ and every quasi-coherent
`O_S`-module $F$. First, a particular case:

**Corollary 2.4.** *Let $S$ be a scheme and $S_{0}$ a closed subscheme defined by a nilpotent ideal. Let $Y$ be a
diagonalizable $S$-group and let:*

<!-- label: III.III.2.4 -->

*a) $X$ an $S$-group locally of finite presentation over $S$,*

*b) $X = \operatorname{Aut}_{S}(E)$ where $E$ is an $S$-scheme locally of finite presentation.*

*Let $f : Y \to X$ be a morphism of $S$-groups such that the morphism $f_{0} : Y_{0} \to X_{0}$ obtained by base change
is the unit morphism. Then $f$ is the unit morphism.*

Indeed, the question is local on $S$ and (in (b)) on $E$. We may therefore suppose $S$ affine and (in (b)) $E$ of finite
presentation over $S$. Now introducing the closed subschemes $S_{n}$ of $S$ defined by the powers of the ideal defining
$S_{0}$, one is reduced to the case where $S_{0}$ is defined by an ideal of square zero, and in that case the asserted
statement follows from the theorem, via 2.2.

In the case where one does not necessarily suppose that $f_{0}$ is the unit morphism, one has:

**Corollary 2.5.** *Let $S$ and $S_{0}$ be as in 2.4. Suppose moreover $S$ affine. Let $Y$ be a diagonalizable
$S$-group, $X$ an $S$-group functor, and $f_{0} : Y_{0} \to X_{0}$ a morphism of $S_{0}$-group functors.*

<!-- label: III.III.2.5 -->

*(i)[^N.D.E-III-58]*

<!-- original page 117 -->

*(ii) Suppose that one of the following two properties holds:*

*(a) $X$ is an $S$-group smooth over $S$;*

*(b) $X = \operatorname{Aut}_{S}(E)$ where $E$ is smooth and affine over $S$.*

*Then $f_{0}$ extends to a morphism of $S$-groups $Y \to X$; two such extensions are conjugate by an inner automorphism
of $X$ defined by a section of $X$ over $S$ inducing the unit section of $X_{0}$ over $S_{0}$.*

Introduce the $S_{n}$ as above.[^N.D.E-III-59] For (ii), note first that a scheme smooth over $S$ is necessarily locally
of finite presentation over $S$; hence, in case (b), $E$ being smooth and affine over $S$ is necessarily of finite
presentation over $S$, i.e. we are indeed under hypothesis (b) of 2.0.

Then, under the hypotheses of (ii), condition $(i_{1})$ of 2.1 is automatically verified by 0.16 and 0.17; moreover
every section of $X_{S_{n}}$ over $S_{n}$ lifts to a section of $X_{S_{n+1}}$ over $S_{n+1}$, by the definition of
"smooth over $S$" in case (a), and by 0.17 in case (b). Consequently, if $f$ and $f'$ are two lifts of $f_{0}$, one can
suppose step by step that $f_{n} = f_{n}'$ by lifting the inner automorphism whose existence is asserted by part (ii) of
the theorem, which completes the proof.

By reasoning likewise, taking into account Remark 2.3, one obtains:

**Corollary 2.6.** *Let $S$ be a scheme, $I$ a nilpotent ideal defining the closed subscheme $S_{0}$, $Y$ an $S$-group
flat over $S$ and affine, $X$ an $S$-group smooth over $S$.*

<!-- label: III.III.2.6 -->

*(i) If, for every $n \geq 0$, one has $H^{2}(Y_{0}, Lie(X_{0}/S_{0}) \otimes_{O_{S_{0}}} I^{n+1}/I^{n+2}) = 0$, every
morphism of $S_{0}$-groups $f_{0} : Y_{0} \to X_{0}$ lifts to a morphism of $S$-groups $f : Y \to X$.*

*(ii) If, for every $n \geq 0$, one has $H^{1}(Y_{0}, Lie(X_{0}/S_{0}) \otimes_{O_{S_{0}}} I^{n+1}/I^{n+2}) = 0$, two
such lifts are conjugate by an inner automorphism of $X$ defined by a section of $X$ over $S$ inducing the unit section
of $X_{0}$ over $S_{0}$.*

Now one has the following lemma:

**Lemma 2.7.** *Let $S$ be an affine scheme, $G$ an affine $S$-group, $F$ a quasi-coherent `O_S`-module, $L$ a locally
free `O_S`-module. Suppose one has an action of $G$ on $F$ in the sense of Exposé I, which defines an action of $G$ on
$F \otimes_{O_{S}} L$[^N.D.E-III-60]. Denote by $\Lambda$ the ring of $S$, $L$ the $\Lambda$-module defining $L$ (which
is therefore a projective module). One has a canonical isomorphism*

<!-- label: III.III.2.7 -->

<!-- original page 118 -->

```text
H*(G, F ⊗_{O_S} L) ≃ H*(G, F) ⊗_Λ L.
```

[^N.D.E-III-61] Indeed, denote by $A$ the `O_S`-algebra $A(G)$ and consider the complex $C$ of quasi-coherent
`O_S`-modules:

```text
0 ──► F ──► F ⊗_{O_S} A ──► F ⊗_{O_S} A ⊗_{O_S} A ──► · · ·
```

By (I, 5.3), $H*(G, F)$ (resp. $H*(G, F \otimes_{O_{S}} L)$) is the cohomology of the complex $\Gamma(S, C)$ (resp.
$\Gamma(S, C \otimes_{O_{S}} L)$). Now, since $S$ is affine, one has (cf. [EGA I, 1.3.12](https://jcreinhold.github.io/ega/i/01-01-affine-schemes.html#13-sheaf-associated-to-a-module))

```text
Γ(S, C ⊗_{O_S} L) ≃ Γ(S, C) ⊗_Λ L.
```

Since $L$ is a projective $\Lambda$-module (hence flat), one has also $H*(\Gamma(S, C) \otimes_{\Lambda} L) \simeq
H*(\Gamma(S, C)) \otimes_{\Lambda} L$, whence the announced result.

By using the lemma, one transforms 2.6 into:

**Corollary 2.8.** *Let $S$ be an affine scheme, $I$ a nilpotent ideal on $S$ defining the closed subscheme $S_{0}$.
Suppose the $I^{n+1}/I^{n+2}$ locally free on $S_{0}$. Let $Y$ be an $S$-group flat over $S$ and affine, $X$ an
$S$-group smooth over $S$, and $f_{0} : Y_{0} \to X_{0}$ a morphism of $S$-groups.*

<!-- label: III.III.2.8 -->

*(i) If $H^{2}(Y_{0}, Lie(X_{0}/S_{0})) = 0$, $f_{0}$ lifts to a morphism of $S$-groups $Y \to X$.*

*(ii) If $H^{1}(Y_{0}, Lie(X_{0}/S_{0})) = 0$, two such lifts are conjugate by an inner automorphism of $X$ defined by a
section of $X$ over $S$ inducing the unit section of $X_{0}$ over $S_{0}$.*

In particular, taking $Y = X$:

**Corollary 2.9.** *Let $S$ and $S_{0}$ be as above. Let $X$ be an $S$-group smooth over $S$ and affine.*

<!-- label: III.III.2.9 -->

*(i) If $H^{1}(X_{0}, Lie(X_{0}/S_{0})) = 0$, every endomorphism of $X$ over $S$ inducing the identity on $X_{0}$ is the
inner automorphism defined by a section of $X$ over $S$ inducing the unit section of $X_{0}$ over $S_{0}$.*

<!-- original page 119 -->

*(ii) If $H^{2}(X_{0}, Lie(X_{0}/S_{0})) = 0$, every $S_{0}$-automorphism of $X_{0}$ extends to an $S$-automorphism of
$X$.[^N.D.E-III-62]*

**Remark 2.10.** *The assertions concerning $H^{1}$ have converses by the theorem. Let us signal as an example the
following: if $S = IS_{0}$ is the scheme of dual numbers over $S_{0}$ (II, 2.1) and if $X$ is a flat $S$-group such that
every automorphism of $X$ over $S$ inducing the identity on $S_{0}$ is the inner automorphism defined by a section of
$X$ over $S$ inducing the unit section of $X_{0}$ over $S_{0}$, then $H^{1}(X_{0}, Lie(X_{0}/S_{0})) =
0$.[^N.D.E-III-63]*

<!-- label: III.III.2.10 -->

**Corollary 2.11.** *Let $S$, $I$ and $J$ be as in 2.1. Let $Y$ be an $S$-group scheme flat over $S$, $X$ an $S$-group
scheme, $f : Y \to X$ a morphism of $S$-groups. The set of morphisms from $Y$ to $X$ deduced from $f$ by conjugation by
elements $x \in X(S)$ inducing the unit of $X(S_{J})$ is isomorphic to the quotient*

<!-- label: III.III.2.11 -->

```text
E = Hom_{O_{S₀}}(ω¹_{X₀/S₀}, J) / Hom_{O_{S₀}}(ω¹_{X₀/S₀}, J)^{ad(Y₀)} ,
```

*where the second group consists of the $O_{S_{0}}$-morphisms $\omega^{1}_{X_{0}/S_{0}} \to J$ which by every base
change $S' \to S_{0}$ give morphisms $\omega^{1}_{X_{0}/S_{0}} \otimes_{O_{S_{0}}} O_{S'} \to J \otimes_{O_{S_{0}}}
O_{S'}$ invariant under the action of $Y_{0}(S')$ on the first factor.*

By 2.1 (iii), one knows that the set sought is isomorphic to $\Gamma(L_{0})/H^{0}(Y_{0}, L_{0})$. Now $\Gamma(L_{0}) =
\operatorname{Hom}_{O_{S_{0}}}(\omega^{1}_{X_{0}/S_{0}}, J)$ and $H^{0}(Y_{0}, L_{0})$ is evidently none other than
$\Gamma(L_{0})^{ad(Y_{0})}$ in the sense of the preceding statement.

<!-- original page 120 -->

**Corollary 2.12.** *Under the conditions of 2.11, suppose moreover $\omega^{1}_{X_{0}/S_{0}}$ locally free of finite
rank. Then*

<!-- label: III.III.2.12 -->

```text
E ≃ Γ(S₀, Lie(X₀/S₀) ⊗_{O_{S₀}} J) / H⁰(Y₀, Lie(X₀/S₀) ⊗_{O_{S₀}} J).
```

[^N.D.E-III-64] Indeed, if $\omega^{1}_{X_{0}/S_{0}}$ is locally free of finite rank, one has
$\operatorname{Hom}_{O_{S_{0}}}(\omega^{1}_{X_{0}/S_{0}}, J) \simeq Lie(X_{0}/S_{0}) \otimes_{O_{S_{0}}} J$.

**Corollary 2.13.** *Suppose moreover $Y_{0}$ diagonalizable. Then*

<!-- label: III.III.2.13 -->

```text
E ≃ Γ(S₀, Lie(X₀/S₀) ⊗_{O_{S₀}} J) / Γ(S₀, Lie(X₀/S₀)^{ad(Y₀)} ⊗_{O_{S₀}} J)
```

*where $Lie(X_{0}/S_{0})^{ad(Y_{0})}$ can be constructed as the factor of the decomposition of (I, 4.7.3) corresponding
to the null character of $Y_{0}$.*

Indeed, if $Y_{0} \simeq D_{S_{0}}(M)$, one has by loc. cit. a decomposition into direct sum:

```text
Lie(X₀/S₀) = Lie(X₀/S₀)₀ ⊕ ⨁_{m ∈ M, m ≠ 0} Lie(X₀/S₀)_m .
```

By tensoring with $J$, one finds an analogous decomposition for $Lie(X_{0}/S_{0}) \otimes_{O_{S_{0}}} J$, whence the
relation

```text
H⁰(Y₀, Lie(X₀/S₀) ⊗ J) ≃ Γ(S₀, Lie(X₀/S₀)₀ ⊗_{O_{S₀}} J).
```

**Corollary 2.14.** *Suppose moreover $S_{0}$ affine. Then*

<!-- label: III.III.2.14 -->

```text
E ≃ Γ(S₀, [Lie(X₀/S₀) / Lie(X₀/S₀)^{ad(Y₀)}] ⊗_{O_{S₀}} J).
```

## 3. Infinitesimal extensions of a group scheme

<!-- label: III.III.3 -->

<!-- original page 121 -->

Still in the notation of n° 0 ($S$, $I$, $J$, etc.), let us give ourselves an $S$-scheme $X$ and suppose `X_J` endowed
with a group structure. We propose to find the $S$-group structures on $X$ inducing on `X_J` the given structure.

From now on, we assume $X$ flat over $S$. Let $C$ be the category of $S$-schemes flat over $S$. We have therefore $X \in
Ob C$. We shall denote by $Y$, resp. $M$, the functor on $C$ defined by $X^{+}$, resp. $L'_{X}$. The canonical morphism
$p_{X} : X \to X^{+}$ defines a morphism of `Ĉ`

$$ p : X \longrightarrow Y $$

<!-- original page 122 -->

and the action of $L'_{X}$ on $X$ in $(Sch)/S$ defines an action of $M$ on $X$ in `Ĉ`. One verifies at once that $X$
thus becomes formally principal homogeneous under `M_Y` above $Y$ (cf. 0.2 (i) and 0.4).

The action of $X^{+}$ on $L'_{X}$ defined in 0.8 (denoted `Ad` in loc. cit.) defines an action denoted $f$ of $Y$ on
$M$. One knows, on the other hand (0.5), that

```text
Hom_Ĉ(Z, M) ≃ Hom_{S₀}(Z₀, L₀),     Z ∈ Ob C,
```

where $L_{0}$ is the functor defined in 0.5.

**Lemma 3.1.** *(i) Condition $(+)_{n}$ of 1.3 is satisfied for every positive integer $n$.*

<!-- label: III.III.3.1 -->

*(ii) If one makes the $S_{0}$-group $X_{0}$ act on the $S_{0}$-functor $L_{0}$ through its adjoint representation, one
has a canonical isomorphism*

```text
H*(X₀, L₀) ≃ H*(Y, M),
```

*(the first cohomology being computed in $(Sch)/S_{0}$, the second in $C$).*

Both parts of the lemma follow from the relation:

```text
Hom_Ĉ(Y, M) ≃ Hom_{(Sch)/S₀}(X⁺ ×_S S₀, L₀)
            ≃ Hom_{S₀}(X₀, L₀)
            ≃ Hom_Ĉ(X, M),
```

which arises at once from the definition of $M$ as a $\prod_{S_{0}/S}$. This relation being more generally satisfied on
replacing $X$, $Y$ by $X_{n}$, $Y_{n}$, one deduces that every morphism $X_{n} \to M$ factors in a unique manner through
$Y_{n}$, which entails $(+)_{n}$. One also deduces from it the relation $C*(Y, M) = C*(X_{0}, L_{0})$, which entails
(ii).

We may therefore apply the constructions of 1.3. In particular:

**Lemma 3.2.** *Let $P : X \times_{S} X \to X$ be a morphism. In order for $P$ to induce the group law of `X_J`, it is
necessary and sufficient that $P$ be an admissible composition law (cf. 1.3.2) on $X$.*

<!-- label: III.III.3.2 -->

Indeed, in order for $P$ to induce the group law of `X_J`, it is necessary and sufficient that $P$ lift the group law of
$X^{+}$, or equivalently that of $Y$. It therefore only remains to show that every morphism $P$ lifting the group law of
`X_J` satisfies the identity `(++)` of 1.3.2 (ii), and this is exactly what was seen in 0.8.

**Proposition 3.3.** *Let $S$ be a scheme and $S_{0}$ a closed subscheme defined by a nilpotent ideal. Let $X$ be a flat
$S$-scheme, quasi-compact or locally of finite presentation over $S$. Let $P : X \times_{S} X \to X$ be a composition
law on $X$. In order for $P$ to be a group law, it is necessary and sufficient that the two following conditions be
satisfied:*

<!-- label: III.III.3.3 -->

*(i) $P$ is associative.*

*(ii) $P$ induces on $X_{0} = X \times_{X} S_{0}$ a group law.*

These conditions are obviously necessary. Let us show that they are sufficient. Suppose first that $X \to S$ has a
section. Since $X(S')$ is then non-empty for each $S' \to S$, it suffices[^N.D.E-III-65] to show that, for every $x \in
X(S')$, the left and right translations by $x$ are isomorphisms of $X_{S'}$.[^N.D.E-III-66]

<!-- original page 123 -->

One may evidently suppose $S' = S$; the translation in question $t$ induces on $X_{0}$ a translation $t_{0}$ of $X_{0}$,
which is therefore an automorphism since $X_{0}$ is a group. One concludes by flatness (SGA 1 III 4.2).[^N.D.E-III-67]

No longer supposing now that $X$ has a section over $S$, suppose that there exists an $S' \to S$ such that $X_{S'}$ has
a section over $S'$. Then $X_{S'}$ is an $S'$-group according to what we have just seen; consider its unit section $e'$.
The inverse image of $e'$ by $pr_{i} : S' \times_{S} S' \to S'$ ($i = 1, 2$) is the unit section of $X_{S''}$ for the
group law inverse image of $P_{S'}$ by $pr_{i}$. But since $P$ is "defined over $S$", these two group laws coincide, and
therefore so do their unit sections. One has therefore $pr_{1}*(e') = pr_{2}*(e')$.

If $S' \to S$ is a descent morphism (cf. Exp. IV n° 2), there will exist a section of $X$ giving $e'$ by base extension,
and we shall be done. Since `X_X` has a section over $X$ (the diagonal section), one sees that it now suffices to prove
that $X \to S$ is a descent morphism. Now it is flat and surjective, and quasi-compact or locally of finite
presentation, hence covering for (fpqc), hence a descent morphism (Exp. IV, n° 6).

**Remark.** *In fact the hypothesis $X \to S$ quasi-compact or locally of finite presentation is superfluous, by virtue
of the following result which the reader will prove as an exercise on Exposé IV:*

*Under the conditions of the text on $S$ and $S_{0}$, if $X \to S$ is a flat morphism and $X_{0} \to S_{0}$ a morphism
covering for (fpqc), then $X \to S$ is a descent morphism.*

<!-- original page 124 -->

**Lemma 3.4.** *In order for two admissible composition laws on $X$ to be equivalent (cf. 1.3.5), it is necessary and
sufficient that they be deduced from one another by an automorphism of $X$ over $S$ inducing the identity on `X_J`.*

<!-- label: III.III.3.4 -->

Indeed, the morphisms constructed in 1.3.1 are exactly those of the preceding statement (by 0.7).[^N.D.E-III-68]

Taking all the preceding results into account, Proposition 1.3.6 gives:

**Theorem 3.5.** *Let $S$ be a scheme, $I$ and $J$ two ideals on $S$ such that $I \supset J$, $I \cdot J = 0$, $S_{0}$
and `S_J` the closed subschemes of $S$ which they define. Let $X$ be an $S$-scheme flat over $S$ (and locally of finite
presentation or quasi-compact over $S$), $X_{0}$ and `X_J` the schemes obtained by base change. Suppose `X_J` endowed
with an `S_J`-group structure and denote by $L_{0}$ the $S_{0}$-functor in commutative groups defined by the formula*

<!-- label: III.III.3.5 -->

```text
Hom_{S₀}(T, L₀) = Hom_{O_T}(ω¹_{X₀/S₀} ⊗_{O_{S₀}} O_T, J ⊗_{O_{S₀}} O_T)
```

*on which $X_{0}$ acts through its adjoint representation.*

*(i) For there to exist an $S$-group structure on $X$ inducing the given structure on `X_J`, it is necessary and
sufficient that the following conditions be satisfied:*

*(i₁) There exists a morphism of $S$-schemes $X \times_{S} X \to X$ inducing the group law of `X_J`.*

*(i₂) A certain obstruction class belonging to $H^{3}(X_{0}, L_{0})$ (defined canonically by the data of $X$ and the
group law of `X_J`) is zero.*

*(ii) If the conditions of (i) are satisfied, the set $E$ of group laws on $X$ inducing the given law of `X_J` is a
principal homogeneous set under $Z^{2}(X_{0}, L_{0})$, and $E$ modulo the $S$-automorphisms of $X$ inducing the identity
on `X_J`, is a principal homogeneous set under $H^{2}(X_{0}, L_{0})$.*

<!-- original page 125 -->

[^N.D.E-III-69] Indeed, every morphism of $S$-schemes $f : X \times_{S} X \to X$ inducing the group law of `X_J` is, by
3.2, an admissible composition law on $X$; then, by 1.3.6 (i), the existence of an associative admissible composition
law $P : X \times_{S} X \to X$ is equivalent to the vanishing of a certain class $c(f) \in H^{3}(X_{0}, L_{0})$, and in
this case, by 3.3, $P$ is a group law. This proves (i), and (ii) then follows from 3.3 and 1.3.6 (ii).

**Remark 3.5.1.**[^N.D.E-III-70] *If $\mu$, $\mu'$ are group laws on $X$ inducing the given law of `X_J`, one therefore
obtains a cocycle $\delta(\mu, \mu') \in Z^{2}(X_{0}, L_{0})$, the sign convention chosen being that $\mu' = \delta(\mu,
\mu') \cdot \mu$, that is, for every $S' \to S$ and $x, y \in X(S')$,*

<!-- label: III.III.3.5.1 -->

```text
μ′(x, y) = δ(μ, μ′)(x₀, y₀) · μ(x, y).
```

[^N.D.E-III-71]

We shall denote by $\bar{\delta}(\mu, \mu')$ the image of $\delta(\mu, \mu')$ in $H^{2}(X_{0}, L_{0})$. Finally, if $X$
endowed with the group law $\mu$ (resp. $\mu'$) is designated simply by $X$ (resp. $X'$), one will write $\delta(X, X')$
instead of $\delta(\mu, \mu')$, and likewise for $\bar{\delta}(X, X')$.

**Remark 3.6.** *Let `X_J` be an `S_J`-scheme smooth over `S_J` and affine. By 0.15, there exists up to isomorphism a
unique $S$-scheme $X$, smooth over $S$, reducing to `X_J`. If `X_J` is endowed with an `S_J`-group structure, it follows
from 0.16 that condition (i₁) is automatically satisfied. Moreover, by 0.6 the definition of $L_{0}$ simplifies and one
obtains:*

<!-- label: III.III.3.6 -->

**Corollary 3.7.** *Let $S$, $I$ and $J$ be as in 3.1. Let `X_J` be an `S_J`-group smooth over `S_J` and affine.*

<!-- label: III.III.3.7 -->

*(i) The set of $S$-groups smooth over $S$ and reducing to `X_J`, up to isomorphism (inducing the identity on `X_J`), is
empty or principal homogeneous under the group*

```text
H²(X₀, Lie(X₀/S₀) ⊗_{O_{S₀}} J).
```

*(ii) There exists an $S$-group smooth over $S$ reducing to `X_J` if and only if a certain obstruction in*

```text
H³(X₀, Lie(X₀/S₀) ⊗_{O_{S₀}} J)
```

*is zero.*

One deduces as usual the following corollaries:

**Corollary 3.8.** *Let $S$ be a scheme and $S_{0}$ a closed subscheme defined by a nilpotent ideal $I$. Let $X_{0}$ be
an $S_{0}$-group smooth over $S$ and affine.*

<!-- label: III.III.3.8 -->

*(i) If $H^{2}(X_{0}, Lie(X_{0}/S_{0}) \otimes_{O_{S_{0}}} I^{n+1}/I^{n+2}) = 0$ for every $n \geq 0$, two $S$-groups
smooth over $S$ reducing to $X_{0}$ are isomorphic (by an isomorphism inducing the identity on $X_{0}$).*

<!-- original page 126 -->

*(ii) If $H^{3}(X_{0}, Lie(X_{0}/S_{0}) \otimes_{O_{S_{0}}} I^{n+1}/I^{n+2}) = 0$ for every $n \geq 0$, there exists an
$S$-group smooth over $S$, reducing to $X_{0}$.*

**Corollary 3.9.** *Let $S$ be an affine scheme and $S_{0}$ a closed subscheme defined by a nilpotent ideal $I$. Suppose
the $I^{n+1}/I^{n+2}$ locally free on $S_{0}$. Let $X_{0}$ be an $S_{0}$-group smooth and affine over $S_{0}$.*

<!-- label: III.III.3.9 -->

*(i) If $H^{2}(X_{0}, Lie(X_{0}/S_{0})) = 0$, two $S$-groups smooth over $S$ reducing to $X_{0}$ are isomorphic.*

*(ii) If $H^{3}(X_{0}, Lie(X_{0}/S_{0})) = 0$, there exists an $S$-group smooth over $S$ reducing to $X_{0}$.*

**Corollary 3.10.** *Let $S_{0}$ be a scheme and $S = IS_{0}$ the scheme of dual numbers over $S_{0}$. Let $X_{0}$ be an
$S_{0}$-group smooth over $S_{0}$. In order for every $S$-group $Y$, smooth over $S$, such that $Y_{0}$ be
$S_{0}$-isomorphic to $X_{0}$, to be $S$-isomorphic to $X = X_{0} \times_{S_{0}} S$, it is necessary and sufficient that
$H^{2}(X_{0}, Lie(X_{0}/S_{0})) = 0$.[^N.D.E-III-72]*

<!-- label: III.III.3.10 -->

Indeed, by virtue of 3.5 the set of classes, up to an $S$-group isomorphism "inducing the identity on $X_{0}$", of such
groups $Y$, is in bijection with $H^{2}(X_{0}, Lie(X_{0}/S_{0}))$; hence the set of classes, up to an arbitrary
$S$-group isomorphism, is in bijection with

$$ H^{2}(X_{0}, Lie(X_{0}/S_{0}))/\Gamma_{0}, $$

where

$$ \Gamma_{0} = \operatorname{Aut}_{S_{0}-gr.}(X_{0}) $$

(which acts in the evident manner on the $H^{2}$). The conclusion follows at once.[^N.D.E-III-73]

## 4. Infinitesimal extensions of closed subgroups

<!-- label: III.III.4 -->

<!-- original page 127 -->

Let us first state a result valid in an arbitrary abelian category.

**Lemma 4.1.** *Let $0 \to A' \to^{i} A \to^{p} A'' \to 0$ be an exact sequence, $\phi : A' \to Q$ a morphism and $\pi :
A'' \to P$ an epimorphism with kernel $C$. Let $E$ be the set (up to isomorphism) of quadruples $(B, f, g, h)$ such that
the sequence*

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

*(i) For $E$ to be non-empty, it is necessary and sufficient that the image in $Ext^{1}(C, Q)$ of the element $A$ of
$Ext^{1}(A'', A')$ be zero.*

*(ii) Under these conditions, $E$ is a principal homogeneous set under the abelian group $\operatorname{Hom}(C, Q)$.*

Introduce the amalgamated sum $B' = A \sqcup_{A'} Q$. One then has a commutative diagram with exact rows:[^N.D.E-III-74]

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

and the morphisms $id_{Q}$ and $\pi : A'' \to P$.[^N.D.E-III-75] In this case, the set $E$ is in bijection with the set
of subobjects $N$ of $B'$ such that $B' \to A''$ induces an isomorphism of $N$ with the kernel $C$ of $A'' \to P$, that
is to say, the set of morphisms $e : C \to B'$ lifting the canonical morphism $C \to A''$. The abelian group $G =
\operatorname{Hom}(C, Q)$ acts on $E$ by $g \cdot e = g + e$ (addition in $\operatorname{Hom}(C, B')$), and if $E \neq
\emptyset$ this makes $E$ into a principal homogeneous set under $G$.

One deduces from this:

**Proposition 4.2.**[^N.D.E-III-76] *Let $S$ be a scheme, `S_J` the closed subscheme defined by a quasi-coherent ideal
$J$ of square zero, $X$ an $S$-scheme, $F$ an `O_X`-module, $X_{J} = X \times_{S} S_{J}$, $F_{J} = F \otimes_{O_{S}}
O_{S_{J}}$, and $G_{J} = F_{J} / H_{J}$ a quotient module of `F_J`. Suppose given a morphism of $O_{X_{J}}$-modules*

<!-- label: III.III.4.2 -->

```text
f : J ⊗_{O_{S_J}} G_J ⟶ Q.
```

*Let $E$ be the sheaf of sets on $X$ defined as follows: for every open $U$ of $X$, $E(U)$ is the set of quotient
modules $G$ of $F|_{U}$, such that $G/JG = G_{J}|_{U}$ and there exists an isomorphism*

$$ h : JG \xrightarrow{\sim} Q|_{U} $$

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

*commutative ($h$ is then unique, since $J \otimes_{O_{S_{J}}} (G_{J}|_{U}) \to JG$ is an epimorphism). Then $E$ is a
sheaf formally principal homogeneous under the sheaf in commutative groups*

```text
A = Hom_{O_X}(H_J, Q) = Hom_{O_{X_J}}(H_J, Q).
```

*Proof.* If $E(U) = \emptyset$ there is nothing to prove; one may therefore suppose that $E(U)$ contains an element
$\tilde{G}$. Then, in the diagram below, $h$ is an isomorphism and all the arrows are epimorphisms:

```text
                                          f|_U
J ⊗_{O_{S_J}} (F_J|_U) ─► J ⊗_{O_{S_J}} (G_J|_U) ─────► Q|_U
        │                          │                      ↗
        can.                       can.                 h ≃
        ↓                          ↓                    /
        JF|_U  ──────────────►   JG̃   ──────────────────
```

Therefore, the morphism $J \otimes_{O_{S_{J}}} (F_{J}|_{U}) \to Q|_{U}$ induces an epimorphism (necessarily unique)
$\phi : JF|_{U} \to Q|_{U}$, and if $G$ is an `O_U`-module such that $G/JG = G_{J}|_{U}$ and one has a commutative
diagram with exact rows:

```text
0 ──► JF|_U ─────► F|_U ─────► F_J|_U ──► 0
        │           │            │
        φ           │            π
        ↓     p_J   ↓            ↓
0 ──► Q|_U ─────► G ──────►  G_J|_U ──► 0
```

(where $p_{J}$ is the projection $G \to G/JG = G_{J}|_{U}$, so that $Q|_{U} = Ker(p_{J}) = JG$), then one can identify
$G$ with a quotient module of $F|_{U}$. Consequently, by 4.1 (ii), the set $E(U)$ is principal homogeneous under the
abelian group

```text
Hom_{O_X}(H_J, Q)(U) = Hom_{O_{X_J}}(H_J, Q)(U).
```

**Proposition 4.3.** *(TDTE IV 5.1) Let $S$ be a scheme, `S_J` the closed subscheme defined by a quasi-coherent ideal
$J$ of square zero, $X$ an $S$-scheme, $F$ a quasi-coherent `O_X`-module, $X_{J} = X \times_{S} S_{J}$, $F_{J} = F
\otimes_{O_{S}} O_{S_{J}}$. Let $G_{J} = F_{J} / H_{J}$ be a quasi-coherent quotient module of `F_J`, flat over `S_J`.*

<!-- label: III.III.4.3 -->

*For every open $U$ of $X$, let $E(U)$ be the set of quasi-coherent[^N.D.E-III-77] quotient modules $G$ of $F|_{U}$,
flat over $S$, and such that $G/JG \simeq G_{J}|_{U}$. Then the $E(U)$ form a sheaf of sets $E$ on $X$, which is
formally principal homogeneous under the sheaf in commutative groups*

```text
A = Hom_{O_{X_J}}(H_J, J ⊗_{O_{S_J}} G_J).
```

*Proof.* Denote by $\pi : X \to S$ the structural morphism. Let $U$ be an open of $X$ and $G$ an `O_U`-module flat over
$S$ and such that $G/JG \simeq G_{J}|_{U}$. Then, for every $x \in U$, $G_{x}$ is a flat module over the local ring
$O_{S,s}$ (where $s = \pi(x)$), and therefore the morphism

```text
J_s ⊗_{O_{S,s}} (G/JG)_x = J_s ⊗_{O_{S,s}} G̅_x ⟶ (JG)_x
```

is bijective; one has therefore an exact sequence

```text
0 ⟶ J ⊗_{O_S} (G_J|_U) ⟶ G ⟶ G_J|_U ⟶ 0
```

<!-- original page 130 -->

and since $J \otimes_{O_{S}} (G_{J}|_{U})$ and $G_{J}|_{U}$ are quasi-coherent `O_U`-modules, so is $G$ (cf. [EGA III,
1.4.17](https://jcreinhold.github.io/ega/iii/08-ch3-01-cohomology-affine-schemes.html#14-application-to-the-cohomology-of-arbitrary-preschemes)).

Conversely, since one has supposed `G_J` flat over `S_J`, if $G$ is a quasi-coherent `O_U`-module such that $G/JG \simeq
G_{J}$ and such that the morphism $J \otimes_{O_{S_{J}}} G_{J} \to JG$ is bijective, then $G$ is flat over $S$, by the
"fundamental criterion of flatness" (cf. SGA 1 IV, 5.5[^N.D.E-III-78]).

Consequently, the set $E(U)$ considered here coincides with the set considered in 4.2, taking for $f$ the identity
morphism of $J \otimes_{O_{S_{J}}} G_{J}$, and the conclusion follows therefore from 4.2. QED.

[^N.D.E-III-79] Let us preserve the preceding notation. Let `Y_J` be a closed subscheme of `X_J`, defined by a
quasi-coherent ideal $I_{Y_{J}}$. We assume `Y_J` flat over `S_J`. Then, applying 4.3 to $F = O_{X}$ and $G_{J} =
O_{Y_{J}} = O_{X_{J}}/I_{Y_{J}}$, one obtains the following corollary.

**Corollary 4.3.1.** *Let $S, S_{J}, J, X, X_{J}, Y_{J}$ and $I_{Y_{J}}$ be as above; one assumes `Y_J` flat over `S_J`.
Denote by `A_J` the sheaf in commutative groups*

<!-- label: III.III.4.3.1 -->

```text
Hom_{O_{X_J}}(I_{Y_J}, J ⊗_{O_{S_J}} O_{Y_J})
```

*on `X_J` and $A = i_{*}(A_{J})$, where $i$ is the immersion $X_{J} \hookrightarrow X$.*

*For every open $U$ of $X$, let $E(U)$ be the set of closed subschemes $Y$ of $U$, flat over $S$, such that $Y
\times_{S} S_{J} = Y_{J} \cap U$. Then $E$ is an $A$-pseudo-torsor.*

*If moreover a $Y$ exists locally (that is, if every $x \in X$ has an open neighborhood $U$ such that $E(U) \neq
\emptyset$), then $E$ is an $A$-torsor.* Now one knows (see for example EGA IV₄, 16.5.15) that the $A$-torsors on $X$
are parametrized by the group $H^{1}(X, A) = H^{1}(X_{J}, A_{J})$, and that $E$ has a global section (i.e. $E(X) \neq
\emptyset$) if and only if the cohomology class corresponding to $E$ is zero. One thus obtains:

**Corollary 4.4.** *Let $S, S_{J}, J, X, X_{J}, Y_{J}$ and $I_{Y_{J}}$ be as above; one assumes `Y_J` flat over `S_J`.
Let $E$ be the set of closed subschemes $Y$ of $X$, flat over $S$, such that $Y \times_{S} S_{J} = Y_{J}$.*

<!-- label: III.III.4.4 -->

*(i) The set $E$ is empty or principal homogeneous under the abelian group*

```text
H⁰(X, A) = H⁰(X_J, A_J) = Hom_{O_{X_J}}(I_{Y_J}, J ⊗_{O_{S_J}} O_{Y_J}).
```

<!-- original page 131 -->

*(ii) For $E$ to be non-empty, it is necessary and sufficient that the two following conditions be satisfied:*

*(a) There exists locally on $X$ a solution of the problem.*

*(b) A certain obstruction is zero, lying in*

```text
H¹(X_J, Hom_{O_{X_J}}(I_{Y_J}, J ⊗_{O_{S_J}} O_{Y_J})).
```

**Complement 4.4.1.**[^N.D.E-III-80] *Let us keep the notation of 4.4 and suppose that $E$ contains an element $Y$.
Denote by `I_Y` the ideal of `O_X` defining $Y$, and $I_{Y_{J}}$ its image in $O_{X_{J}}$. Then, as was seen in the
proof of 4.2, one has a commutative diagram*

<!-- label: III.III.4.4.1 -->

```text
J ⊗_{O_{S_J}} O_{X_J} ──► JO_X
         │                  │
         ↓                  ↓
J ⊗_{O_{S_J}} O_{Y_J} ──≃─► JO_Y
```

*hence an epimorphism of `O_X`-modules $\phi : JO_{X} \to J \otimes_{O_{S_{J}}} O_{Y_{J}}$; denote by $K$ its kernel.*
Then, for every element $Y'$ of $E$, the morphism $O_{X} \to O_{Y'}$ factors through $O_{X}/K$ (which is the amalgamated
sum $B'$ of the proof of Lemma 4.1) and, denoting by $I_{Y'}$ the ideal of $Y'$ in `O_X`, one has a commutative diagram:

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

Therefore, replacing $X$ by the closed subscheme defined by $K$, one reduces to $K = 0$. Then, the datum of $Y'$ is
equivalent to that of the sub-`O_X`-module $I_{Y'}$ of `O_X`, sending bijectively onto $I_{Y_{J}}$ by the projection
$p : O_{X} \to O_{X_{J}}$; denote by $f' : I_{Y_{J}} \xrightarrow{\sim} I_{Y'}$ (resp.
$f : I_{Y_{J}} \xrightarrow{\sim} I_{Y}$) the inverse isomorphism. Then $f' - f$ is an element of

```text
Hom_{O_{X_J}}(I_{Y_J}, J ⊗_{O_{S_J}} O_{Y_J}) = Hom_{O_{X_J}}(I_{Y_J}, JO_Y)
```

which we shall denote $d(Y', Y)$. (Note that $d(Y, Y') = -d(Y', Y)$.)

<!-- original page 132 -->

For our fixed $Y$ and variable $Y'$, consider the morphism:

```text
I_{Y′} ⟶ O_X ⟶ O_Y = O_X/I_Y;
```

since the composition with $O_{Y} \to O_{Y_{J}}$ is zero, one knows that it takes values in $JO_{Y} = J
\otimes_{O_{S_{J}}} O_{Y_{J}}$. More precisely, if $V$ is an open of $X$, $x'$ a section of $I_{Y'}$ on $V$ and $x_{J}$
its image in $\Gamma(V, I_{Y_{J}})$, then

```text
x′ = f′(x_J) = f(x_J) + (f′ − f)(x_J) = f(x_J) + d(Y′, Y)(x_J).
```

Consequently: the morphism $I_{Y'} \to JO_{Y}$ is given by $d(Y', Y)$.

**4.5.0.**[^N.D.E-III-81] Let us keep the notation of 4.3.1 and 4.4 and carry out a certain number of transformations:
$I_{Y_{J}}/I^{2}_{Y_{J}}$ is a quasi-coherent $O_{X_{J}}$-module annihilated by $I_{Y_{J}}$, hence is the direct image
of a quasi-coherent $O_{Y_{J}}$-module denoted $N_{Y_{J}/X_{J}}$, called the *conormal sheaf* to `Y_J` in
`X_J`.[^N.D.E-III-82] Since $J \otimes_{O_{S_{J}}} O_{Y_{J}}$ is annihilated by $I_{Y_{J}}$, the sheaf in commutative
groups `A_J` of 4.3.1 identifies with:

```text
Hom_{O_{Y_J}}(I_{Y_J}/I_{Y_J}², J ⊗_{O_{S_J}} O_{Y_J}) = Hom_{O_{Y_J}}(N_{Y_J/X_J}, J ⊗_{O_{S_J}} O_{Y_J}),
```

whence, for every $i \geq 0$:

```text
Hⁱ(X_J, A_J) = Hⁱ(Y_J, Hom_{O_{Y_J}}(N_{Y_J/X_J}, J ⊗_{O_{S_J}} O_{Y_J})).
```

[^N.D.E-III-83] One can then suppress the hypothesis "$Y$ closed", as follows. Let us first note that every open `U_J`
of `X_J` comes by base change from the open subscheme $U$ of $X$ having the same underlying topological space as `U_J`.
Let now `Y_J` be a closed subscheme of `U_J`, flat over `S_J`, and $I_{Y_{J}}$ the quasi-coherent ideal of $O_{U_{J}}$
defining `Y_J`. If `Y_J` lifts to a subscheme $Y$ of $X$, then $Y$, having the same underlying topological space as
`Y_J`, is a closed subscheme of $U$; consequently, the obstruction to lifting `Y_J` to a subscheme, flat over $S$, of
$X$ or of $U$ is "the same", it resides in

```text
H¹(Y_J, Hom_{O_{Y_J}}(N_{Y_J/X_J}, J ⊗_{O_{S_J}} O_{Y_J})).
```

Finally, let us return to the notation of n° 0: let $I$ be a quasi-coherent ideal of `O_S` such that $J \subset I$ and
$IJ = 0$, and let $S_{0}$ be the closed subscheme of `S_J` defined by $I$. For every $S$-scheme $Z$, one denotes $Z_{J}
= Z \times_{S} S_{J}$ and $Z_{0} = Z \times_{S} S_{0}$. Then, since $J$ is annihilated by $I$, one has, with the
notation of 4.4:

```text
J ⊗_{O_{S_J}} O_{Y_J} = J ⊗_{O_{S₀}} O_{Y₀}
Hom_{O_{Y_J}}(N_{Y_J/X_J}, J ⊗_{O_{S_J}} O_{Y_J}) = Hom_{O_{Y₀}}(N_{Y_J/X_J} ⊗_{O_{Y_J}} O_{Y₀}, J ⊗_{O_{S₀}} O_{Y₀}),
```

etc. One thus obtains:

<!-- original page 133 -->

**Proposition 4.5.** *Let $S$ be a scheme, $S_{0}$ and `S_J` the closed subschemes defined by the quasi-coherent ideals
$I$ and $J$, such that $I \supset J$ and $I \cdot J = 0$. Let $X$ be an $S$-scheme and `Y_J` a subscheme of `X_J`, flat
over `S_J`. Let $A_{0}$ be the $O_{Y_{0}}$-module defined by*

<!-- label: III.III.4.5 -->

```text
A₀ = Hom_{O_{Y₀}}(N_{Y_J/X_J} ⊗_{O_{Y_J}} O_{Y₀}, J ⊗_{O_{S₀}} O_{Y₀}).
```

*(i) For there to exist a subscheme $Y$ of $X$, reducing to `Y_J`, flat over $S$, it is necessary and sufficient that
the following conditions be satisfied:*

*(a) Such a $Y$ exists locally on $X$.*

*(b) A certain obstruction in $R^{1}\Gamma(Y_{0}, A_{0})$ is zero.[^N.D.E-III-84]*

*(ii) Under these conditions, the set of $Y$ satisfying the required conditions is principal homogeneous under the
commutative group $\Gamma(Y_{0}, A_{0})$.*

**Remark 4.5.1.**[^N.D.E-III-85] *It follows from 4.5 (ii) that for every pair $(Y, Y')$ of subschemes[^N.D.E-III-86] of
$X$, flat over $S$ and reducing to `Y_J`, one has a "deviation"*

<!-- label: III.III.4.5.1 -->

```text
d(Y′, Y) ∈ Γ(Y₀, A₀) = Hom_{O_{Y₀}}(N_{Y_J/X_J} ⊗_{O_{Y_J}} O_{Y₀}, J ⊗_{O_{S₀}} O_{Y₀});
```

*the sign convention adopted in 4.4.1 being that $d(Y', Y)$ corresponds to the morphism of `O_X`-modules*

$$ I_{Y'} \hookrightarrow O_{X} \longrightarrow O_{Y} $$

*(which takes values in $JO_{Y} \simeq J \otimes_{O_{S_{0}}} O_{Y_{0}}$ and factors through $I_{Y_{J}'} = I_{Y_{J}}$ and
then through $N_{Y_{J}/X_{J}}$).*

**Remark 4.6.**[^N.D.E-III-87] *If $X$ is flat over $S$ and if `Y_J` is locally complete intersection in `X_J`, then
condition (a) is always satisfied and every $Y$ flat over $S$ lifting `Y_J` is then locally complete intersection in
$X$. If moreover $Y_{0}$ is affine, condition (b) is also satisfied.*

<!-- label: III.III.4.6 -->

**Definition 4.6.1.** *(cf. SGA 6, VII 1.1) Let $B$ be a commutative ring, $f : E \to B$ a $B$-linear morphism, where
$E$ is a free $B$-module of finite rank $d$, and $I$ the ideal $f(E)$ (if one chooses a basis of $E$, $f$ is given by a
$d$-tuple $(f_{1}, ..., f_{d})$ of elements of $B$, and $I$ is the ideal generated by the `fᵢ`). The* **Koszul complex**
*$K\bullet(f)$ is the graded $B$-module $\bigwedge\bullet E$, equipped with the differential (of degree $-1$):*

<!-- label: III.III.4.6.1 -->

```text
x₁ ∧ ··· ∧ xᵢ ↦ Σⱼ₌₁ⁱ (−1)ʲ⁻¹ f(xⱼ) x₁ ∧ ··· ∧ x̂ⱼ ∧ ··· ∧ xᵢ.
```

<!-- original page 134 -->

One has therefore an augmented chain complex ($B/I$ being in degree $-1$):

```text
··· ⟶ ⋀² E ⟶ E ──f──► B ⟶ B/I ⟶ 0
```

which by definition is exact in degree `0`, since $I = f(E)$. One says that $f$ is **regular** if $K\bullet(f)$ is
acyclic in degrees `> 0`, that is, if the augmented complex above is a resolution of $C = B/I$.

In this case, the proof of SGA 6, VII 1.2 b) shows that the $C$-modules $I^{n}/I^{n+1}$ ($n \in \mathbb{N}$) are free,
$I/I^{2}$ being of rank $d$.

**Definition 4.6.2.** *(cf. SGA 6, VII 1.4) Let $X$ be a scheme, $Y$ a subscheme, $U$ an open of $X$ such that $Y$ is a
closed subscheme of $U$, defined by the quasi-coherent ideal `I_Y`.*

<!-- label: III.III.4.6.2 -->

*One says that $Y$ is* **locally complete intersection** *in $X$ if $Y \hookrightarrow X$ is a regular immersion in the
sense of SGA 6, VII 1.4, that is, if for every $y \in Y$ there exists an affine open neighborhood $V$ of $y$ in $U$, a
finite free `O_V`-module $E$, and a regular morphism $f : E \to O_{V}$ of image $I_{Y}|_{V}$, i.e. such that
$K\bullet(f)$ be a resolution of $O_{Y \cap V}$.*

This implies that the immersion $Y \hookrightarrow X$ is locally of finite presentation, and, by 4.6.1, that the
conormal sheaf $N_{Y/X} = I_{Y}/I^{2}_{Y}$ is a finite locally free `O_Y`-module.

**Lemma 4.6.3.**[^N.D.E-III-88] *Let $A$ be a ring, $J$ an ideal of $A$ of square zero, $\bar{A} = A/J$, $B$ a flat
$A$-algebra, $E$ a free $B$-module of finite rank, $f : E \to B$ a morphism of $B$-modules. One supposes that the
morphism $\bar{g} : \bar{E} = E \otimes_{A} \bar{A} \to \bar{B} = B \otimes_{A} \bar{A}$ induced by $f$ is regular and
that $\bar{B}/\bar{g}(\bar{E})$ is flat over `Ā`.*

<!-- label: III.III.4.6.3 -->

*Then $f$ is regular and $B/f(E)$ is flat over $A$.*

*Proof.* Set $C = B/f(E)$ and $\bar{C} = C \otimes_{A} \bar{A} = \bar{B}/\bar{g}(\bar{E})$. First, the
$\bigwedge^{i}_{B}(E)$ are free $B$-modules, hence flat $A$-modules, since $B$ is flat over $A$. As
$\bigwedge\bullet_{B} E \otimes_{A} \bar{A} \simeq \bigwedge\bullet_{\bar{B}} \bar{E}$, one obtains therefore an exact
sequence of complexes:

```text
0 ⟶ J ⊗_A ⋀•_B E ⟶ ⋀•_B E ⟶ ⋀•_B̄ Ē ⟶ 0.
```

Moreover, since $J^{2} = 0$, one has $J \otimes_{A} M = J \otimes_{A} \bar{A} \otimes_{A} M$ for every $A$-module $M$.
Denoting by dashed arrows the augmentation morphisms, and by $d$ the rank of $E$, one therefore obtains the bicomplex
that follows, where the rows are exact:

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

Moreover, the right and left columns are exact, since $K\bullet(\bar{g})$ is a resolution of $\bar{C}$ and the latter is
flat over `Ā`. Hence, considering the long exact homology sequence associated with the exact sequence of unaugmented
complexes, one obtains that $K\bullet(f)$ is acyclic in degrees `> 0`, and that one has in degree `0` an exact sequence:

```text
0 ⟶ J ⊗_A C̄ ⟶ C ⟶ C̄ ⟶ 0.
```

Hence $C$ is flat over $A$, by the "fundamental criterion of flatness" (cf. [BAC], § III.5, th. 1).

**Lemma 4.6.4.**[^N.D.E-III-88] *Let $A$ be a commutative ring, $J$ a nilpotent ideal, $N \subset M$ two $A$-modules
such that $M/N$ is flat over $A$. If $x_{1}, ..., x_{n}$ are elements of $N$ whose images generate the image $\bar{N}$
of $N$ in $M/JM$, then they generate $N$.*

<!-- label: III.III.4.6.4 -->

Indeed, denote by $N'$ the submodule of $N$ generated by the `xᵢ`, and $Q = N/N'$. Then the morphism $N' \otimes (A/J)
\to \bar{N}$ is surjective. On the other hand, since $M/N$ is flat over $A$, the morphism $N \otimes (A/J) \to \bar{N}$
is bijective. One thus obtains that $Q \otimes (A/J) = 0$, whence $Q = 0$ by the "nilpotent Nakayama lemma" (one has $Q
= JQ = J^{2}Q = \cdot\cdot\cdot = 0$).

One can now prove:

**Proposition 4.6.5.**[^N.D.E-III-88] *Let `S, I, J` and $X, Y_{J}$ be as in 4.5. Suppose moreover $X$ flat over $S$ and
`Y_J` locally complete intersection in `X_J`.*

<!-- label: III.III.4.6.5 -->

<!-- original page 136 -->

*a) Then condition (a) of 4.5 (i) is satisfied; moreover, every $Y$ flat over $S$ lifting `Y_J` is locally complete
intersection in $X$.*

*b) If moreover $Y_{0}$ is affine, condition (b) of loc. cit. is likewise satisfied.*

*Proof.* The first assertion of (a) follows from Lemma 4.6.3; the second then results from Lemma 4.6.4. On the other
hand, the hypothesis entails (cf. 4.6.2) that $N_{Y_{J}/X_{J}}$ is a finite locally free $O_{Y_{J}}$-module, hence the
$O_{Y_{0}}$-module

```text
A₀ = Hom_{O_{Y₀}}(N_{Y_J/X_J} ⊗_{O_{Y_J}} O_{Y₀}, J ⊗_{O_{S₀}} O_{Y₀}).
```

is quasi-coherent (cf. EGA I, 1.3.12), whence $R^{1}\Gamma(Y_{0}, A_{0}) = 0$ if $Y_{0}$ is affine.

**Remark 4.6.6.**[^N.D.E-III-88] *Let us conclude this paragraph by the following example, which shows that, under the
hypotheses of Lemma 4.6.3, if $(\bar{g}_{1}, \bar{g}_{2})$ is a regular sequence generating the ideal $\bar{I} =
\bar{g}(\bar{E})$, it does not necessarily lift to a regular sequence in $B$.*

<!-- label: III.III.4.6.6 -->

*Let $k$ be a field, $\bar{A} = k[X, Y]$, denote by $k\epsilon$ the `Ā`-module $\bar{A}/(X, Y)$ (i.e. $P \cdot \epsilon
= P(0, 0)\epsilon$ for every $P \in \bar{A}$), and let $A = \bar{A} \oplus k\epsilon$, where $J = k\epsilon$ is an ideal
of square zero. One has $A/J = \bar{A}$.*

*The algebra $B = A \otimes_{k} k[Z, T]$ is free over $A$, hence flat; one has $\bar{B} = k[X, Y, Z, T]$. Set
$\bar{g}_{1} = XZ - YT$ and $\bar{g}_{2} = XZ - 1$. Since the polynomial $\bar{g}_{1}$ is irreducible,
$\bar{B}/(\bar{g}_{1})$ is integral, and therefore $(\bar{g}_{1}, \bar{g}_{2})$ is a regular sequence in $\bar{B}$,
generating the ideal $\bar{I} = (XZ - 1, YT - 1)$. Hence*

```text
C̄ = B̄/Ī = k[X, Y, X⁻¹, Y⁻¹] = Ā[X⁻¹, Y⁻¹]
```

*is a flat `Ā`-algebra (and also a flat $A$-algebra). But every lift in $B$ of $\bar{g}_{1}$ is of the form $XY - ZT +
\lambda \epsilon$, where $\lambda \in k[Z, T]$, hence annihilates $\epsilon$.*

**4.7.** One has suppressed here Remark 4.7, placed in 4.5.1.

**Remark 4.8.0.**[^N.D.E-III-89] *Let $S$ be a scheme, $S'$ a closed subscheme, $X$ an $S$-scheme, $Y$ a sub-$S$-scheme
of $X$, and $X' = X \times_{S} S'$, $Y' = Y \times_{S} S'$. Then, one has a surjective morphism of $O_{Y'}$-modules*

<!-- label: III.III.4.8.0 -->

```text
N_{Y/X} ⊗_{O_Y} O_{Y′} ──surj──► N_{Y′/X′}.
```

Indeed, up to replacing $X$ by a certain open, one may suppose that $Y$ is closed, defined by an ideal `I_Y` of `O_X`;
then the image of `I_Y` in $O_{X'}$ is the ideal $I_{Y'}$ defining $Y'$, and one has a surjective morphism of
$O_{Y'}$-modules

```text
π : (I_Y/I_Y²) ⊗_{O_Y} O_{Y′} ──surj──► I_{Y′}/I_{Y′}².
```

Suppose moreover that $O_{Y} = O_{X}/I_{Y}$ is flat over `O_S`; then the natural morphism

```text
I_Y ⊗_{O_X} O_{X′} ⟶ I_{Y′}
```

<!-- original page 137 -->

is bijective (cf. [EGA IV₂, 2.1.8](https://jcreinhold.github.io/ega/iv/14-ch4-02-base-change-and-flatness.html#21-flat-modules-on-preschemes)). One then has the following commutative diagram with exact rows:

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

**Proposition 4.8.** *Let $S, S_{0}, S_{J}$ and `I, J` be as in 4.5.[^N.D.E-III-91] Let $X$ be an $S$-scheme, $Y$ a
subscheme of $X$, and $i$ the immersion $Y \hookrightarrow X$.*

<!-- label: III.III.4.8 -->

*(i) For every $S$-morphism $f : T \to X$ such that $f_{J} : T_{J} \to X_{J}$ factors through `Y_J`, one can define an
obstruction*

```text
(∗)    c(X, Y, f) ∈ Hom_{O_{T₀}}(f₀*(N_{Y/X} ⊗_{O_Y} O_{Y₀}), JO_T)
```

*whose vanishing is equivalent to the existence of a factorization of $f$ through $Y$.*

*(ii) Let $Y'$ be a second subscheme of $X$. Suppose that $Y_{J}' = Y_{J}$ and that $Y, Y'$ are flat over $S$. One then
has isomorphisms (cf. 4.8.0):*

```text
JO_Y ≃ J ⊗_{O_{S₀}} O_{Y₀} ≃ JO_{Y′}    and    N_{Y/X} ⊗_{O_Y} O_{Y_J} ⥲ N_{Y_J/X_J}
```

*whence an isomorphism:*

```text
u : Hom_{O_{Y₀}}(N_{Y_J/X_J} ⊗_{O_{Y_J}} O_{Y₀}, JO_Y) ⥲ Hom_{O_{Y₀}}(N_{Y/X} ⊗_{O_Y} O_{Y₀}, JO_{Y′}).
```

*Denoting by $i' : Y' \to X$ the canonical immersion and $d(Y, Y')$ the deviation of 4.5.1, one has:[^N.D.E-III-92]*

```text
(∗∗)    c(X, Y, i′) = u(d(Y, Y′)).
```

*(iii) The canonical morphism `N_{Y/X} ──D──► i*(Ω¹_{X/S})` (cf. SGA 1 II, formula 4.3)[^N.D.E-III-93] induces a
morphism:*

```text
D₀ : N_{Y/X} ⊗_{O_Y} O_{Y₀} ⟶ Ω¹_{X₀/S₀} ⊗_{O_{X₀}} O_{Y₀}
```

<!-- original page 138 -->

*and hence, for every $S$-morphism $f : T \to X$ as in (i), a morphism:*

```text
v_{f₀} : Hom_{O_{T₀}}(f₀*(Ω¹_{X₀/S₀}), JO_T) → Hom_{O_{T₀}}(f₀*(N_{Y/X} ⊗_{O_Y} O_{Y₀}), JO_T),
                                       a ↦ a ∘ f₀*(D₀)
```

*where above the first group is $\operatorname{Hom}_{X^{+}}(T, L_{X})$, cf. 0.1.5. For $a \in
\operatorname{Hom}_{X^{+}}(T, L_{X})$, one has:*

```text
(∗∗∗)    c(X, Y, a · f) − c(X, Y, f) = v_{f₀}(a),
```

*where $a \cdot f$ denotes the composite morphism `T ──{a×f}──► L_X ×_{X⁺} X → X`.*

We shall prove part (i) of the proposition, leaving the reader to (not) verify assertions (ii) and (iii); this
verification is done by reduction to the affine case, then by comparison of explicit definitions.[^N.D.E-III-94]

Let us therefore prove (i). The morphism $f : T \to X$ defines a morphism of sheaves of rings $\phi : O_{X} \to
f_{*}(O_{T})$.[^N.D.E-III-95] Let $U$ be an open subscheme of $X$ in which $Y$ is closed; since $T$ (resp. `Y_J`) has
the same underlying space as `T_J` (resp. $Y$), the continuous map underlying $f$ sends $T$ into $U$, and since $U$ is
an open of $X$, $\phi$ induces a morphism of sheaves of rings $O_{U} = O_{X}|_{U} \to f_{*}(O_{T})$, i.e. $f$ factors
through $U$.

Therefore, one may restrict to the case where $Y$ is closed, hence defined by a sheaf of ideals `I_Y`. For $f$ to factor
through $Y$, it is necessary and sufficient that the composite map $I_{Y} \to O_{X} \to f_{*}(O_{T})$ be zero. Since
$f_{J}$ factors through `Y_J`, the composite map $I_{Y_{J}} \to O_{X_{J}} \to f_{*}(O_{T_{J}})$ is zero. Considering the
commutative diagram, where the first row is exact:

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

one deduces that $\phi$ sends `I_Y` into $f_{*}(JO_{T})$.[^N.D.E-III-96] Since $J^{2} = 0$, it follows that
$f_{*}(JO_{T})$, viewed as `O_X`-module via $\phi$, is annihilated by `I_Y`; consequently, $\phi$ induces a morphism of
`O_X`-modules

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

where $iT_{0}$ etc. are the closed immersions deduced by base change from $S_{0} \hookrightarrow S$. Since `JO_T` is a
quasi-coherent `O_T`-module annihilated by $I$, one has an isomorphism

$$ JO_{T} \simeq (\tau_{T_{0}})_{*}\tau_{T_{0}}*(JO_{T}), $$

whence $f_{*}(JO_{T}) \simeq (\tau_{X_{0}})_{*}(f_{0})_{*}\tau_{T_{0}}*(JO_{T})$. Therefore $h$ corresponds, by
adjunction, to a morphism of $O_{T_{0}}$-modules

```text
h₀ : f₀*τ_{X₀}* i_*(N_{Y/X}) ⟶ i_{T₀}*(JO_T).
```

Now, $\tau_{X_{0}}* i_{*}(N_{Y/X}) \simeq (i_{0})_{*}\tau_{Y_{0}}*(N_{Y/X}) = N_{Y/X} \otimes_{O_{Y}} O_{Y_{0}}$. Hence,
returning to the abuse of notation $i_{T_{0}}*(JO_{T}) = JO_{T}$ constantly used, $h_{0}$ identifies with a morphism of
$O_{T_{0}}$-modules

```text
h₀ : f₀*(N_{Y/X} ⊗_{O_Y} O_{Y₀}) ⟶ JO_T
```

which is the obstruction $c(X, Y, f)$ sought. This proves (i).

When $f$ is the immersion $i' : Y' \hookrightarrow X$, one sees that $c(X, Y, i')$ comes from the morphism $I_{Y}
\hookrightarrow O_{X} \to O_{Y'}$ hence corresponds, by 4.4.1 and 4.5.1, to the class $d(Y, Y')$. This proves (ii).

Let us prove (iii). First, $D : N_{Y/X} \to i_{*}(\Omega^{1}_{X/S})$ induces a morphism

```text
D₀ : τ_{Y₀}*(N_{Y/X}) ⟶ τ_{Y₀}* i_*(Ω¹_{X/S}) = i_0* τ_{X₀}*(Ω¹_{X/S})
```

and, since $X_{0} = X \times_{S} S_{0}$, one has $\tau_{X_{0}}*(\Omega^{1}_{X/S}) \simeq \Omega^{1}_{X_{0}/S_{0}}$ (cf.
EGA IV₄, 16.4.5). One thus obtains the announced morphism

```text
D₀ : N_{Y/X} ⊗_{O_Y} O_{Y₀} ⟶ Ω¹_{X₀/S₀} ⊗_{O_{X₀}} O_{Y₀}.
```

Finally, we shall verify equality $(\ast\ast\ast)$ after the remark below.

**Remark 4.9.** *The obstruction $c(X, Y, f)$ is computed locally on $T$. Let $U = \operatorname{Spec}(C)$ be an affine
open of $T$ above an affine open $\operatorname{Spec}(A)$ of $X$, itself above an affine open
$\operatorname{Spec}(\Lambda)$ of $S$; let $J \subset I \subset \Lambda$ (resp. $I_{Y} \subset A$) be the ideals
corresponding to $J \subset I$ (resp. to `I_Y`), let $B = A/I_{Y}$ and let $\phi : A \to C$ be the morphism of
$\Lambda$-algebras corresponding to $f : T \to X$; since $f(T_{J}) \subset Y_{J}$ one has $\phi(I_{Y}) \subset JC$ and
therefore $\phi$ induces a morphism of $\Lambda$-algebras $B \to C/JC \to C_{0} = C/IC$. Then the obstruction $c = c(X,
Y, f)$ is computed by the following commutative diagram:*

<!-- label: III.III.4.9 -->

```text
I_Y ────────────► A ─────φ─────► C
                                  ↑
                                  │c
I_Y/I_Y² ──► I_Y/I_Y² ⊗_B C₀ ────► JC,
```

<!-- original page 140 -->

*that is, it is defined, above the open $U$, as the unique element of*

```text
Hom_{C₀}(I_Y/I_Y² ⊗_B C₀, JC) = Hom_{B₀}(I_Y/I_Y² ⊗_B B₀, JC)
```

*such that, with the evident notation, one has $c(x \otimes_{B} 1) = \phi(x)$, for every $x \in I_{Y}$.*

[^N.D.E-III-97] One can now complete the proof of 4.8 (iii). The equality $(\ast\ast\ast)$ is verified locally on $T$,
so one is reduced to the affine situation described above. Let us denote by $d_{A/\Lambda}$ the differential $A \to
\Omega^{1}_{A/\Lambda}$. Then $a$ corresponds, above $U$, to an element $a_{U}$ of

```text
Hom_{C₀}(Ω¹_{A₀/Λ₀} ⊗_{A₀} C₀, JC) ≃ Hom_{B₀}(Ω¹_{A/Λ} ⊗_A B₀, JC) ≃ Hom_A(Ω¹_{A/Λ}, JC).
```

Then, on the one hand, $v_{f_{0}}(a)$ corresponds above $U$ to the element $a_{U} \circ \bar{D}_{0}$, where
$\bar{D}_{0}$ is the morphism of $B$-modules[^N.D.E-III-98]

```text
I_Y/I_Y² ⟶ Ω¹_{A/Λ} ⊗_A B₀,    x + I_Y² ↦ d_{A/Λ}(x) ⊗ 1.
```

On the other hand (cf. the proofs of 0.1.8 and 0.1.9), the morphism of $\Lambda$-algebras $\phi' : A \to C$
corresponding to $a \cdot f$ differs from $\phi$ by the $\Lambda$-derivation $A \to JC$ associated with $a_{U}$, i.e.
one has:

```text
φ′ = φ + a_U ∘ d_{A/Λ} = φ + a_U ∘ (d_{A/Λ} ⊗ 1).
```

Consequently, denoting $c' = c(X, Y, a \cdot f)$, one has for every $x \in I_{Y}$, denoting by $\bar{x}$ its image in
$I_{Y}/I^{2}_{Y}$:

```text
(c′ − c)(x̄ ⊗ 1) = a_U(d_{A/Λ}(x) ⊗ 1) = (a_U ∘ D̄₀)(x̄) = v_{f₀}(a)(x̄).
```

This shows that $c' - c = v_{f_{0}}(a)$.

**4.10.** One has suppressed Remark 4.10 of the original, made obsolete by the addition of Remark 4.8.0.

**4.11.** We now propose to study the following situation. Let $S, S_{J}$ and $S_{0}$ be as in 4.8; one has three
$S$-schemes $X, X', T$, a subscheme $Y$ of $X$ (resp. $Y'$ of $X'$), and morphisms $f : T \to X'$ and $g : X' \to X$.

<!-- original page 141 -->

```text
                                  Y′         Y
                                  ⊂          ⊂
                                  ↓i′        ↓i
T ──────f────► X′ ──────g────► X.
```

One supposes that by reduction modulo $J$, this diagram completes into a commutative diagram

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

**Lemma 4.12.** *Suppose $Y'$ flat over $S$, so that $J \otimes_{O_{S_{0}}} O_{Y_{0}'} = JO_{Y'}$.*

<!-- label: III.III.4.12 -->

*(i) One has a natural morphism*

```text
b_{f₀} : Hom_{O_{Y₀′}}(i_0′*g_0*(N_{Y/X} ⊗ O_{Y₀}), JO_{Y′}) ⟶ Hom_{O_{T₀}}(f₀*g₀*(N_{Y/X} ⊗ O_{Y₀}), JO_T).
```

*(ii) One has also a natural morphism, functorial in $T$,[^N.D.E-III-100]*

```text
a_{g₀}(f₀) : Hom_{O_{T₀}}(f₀*(N_{Y′/X′} ⊗ O_{Y₀′}), JO_T) ⟶ Hom_{O_{T₀}}(f₀*g₀*(N_{Y/X} ⊗ O_{Y₀}), JO_T).
```

*Proof.*[^N.D.E-III-101] Let us first note that, $X, X', Y, Y'$ being fixed, to give a $T$ as above is equivalent to
giving a morphism $(f, f_{J}) : T \to X' \times_{X'^{+}} Y'^{+}$. Set $Z = X' \times_{X'^{+}} Y'^{+}$ and denote by $M$
and $M'$ the $Z$-functors defined by: for every $f : T \to Z$,

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

and since $Y'$ is flat over $S$, the left arrow is an isomorphism, hence one obtains a morphism of $O_{T_{0}}$-modules
$f_{0}*(JO_{Y'}) \to JO_{T}$. The latter induces a morphism of abelian groups

```text
Hom_{O_{T₀}}(f₀*g₀*(N_{Y/X} ⊗ O_{Y₀}), f₀*(JO_{Y′})) ⟶ M(T)
```

and, composing with the morphism

```text
M(Y′) ⟶ Hom_{O_{T₀}}(f₀*g₀*(N_{Y/X} ⊗ O_{Y₀}), f₀*(JO_{Y′})),
```

induced by $f_{0}*$, one obtains the morphism $b_{f_{0}} : M(Y') \to M(T)$.

Likewise, one has in any case a diagram

```text
g_0*(N_{Y/X} ⊗_{O_Y} O_{Y₀}) ─┄┄┄┄┄─► N_{Y′/X′} ⊗_{O_{Y′}} O_{Y₀′}
              │                                    │
              ↓                                    ↓
g_0*(N_{Y₀/X₀})  ────────────────────► N_{Y₀′/X₀′}
```

and since $Y'$ is flat over $S$, the second vertical arrow is an isomorphism by 4.8.0. One thus obtains an
$O_{Y_{0}'}$-morphism

```text
i_0′*g_0*(N_{Y/X} ⊗_{O_Y} O_{Y₀}) ⟶ N_{Y′/X′} ⊗_{O_{Y′}} O_{Y₀′}
```

which induces a morphism $a_{g_{0}}(id_{Y'}) : M'(Y') \to M(Y')$ and, for every $f : T \to Z$, a morphism
$a_{g_{0}}(f) : M'(T) \to M(T)$ such that one has a commutative diagram

```text
M′(Y′) ──{a_{g₀}(id_{Y₀′})}──► M(Y′)
  │                              │
  b′_{f₀}                        b_{f₀}
  ↓                              ↓
M′(T)  ──{a_{g₀}(f₀)}──────► M(T)
```

(where $b'_{f_{0}}$ is defined like $b_{f_{0}}$). QED.

**Remark 4.12.1.**[^N.D.E-III-103] *Denote by $M_{0}$ and $M_{0}'$ the $Y_{0}'$-functors defined by: for every $f :
T_{0} \to Y_{0}'$,*

<!-- label: III.III.4.12.1 -->

```text
M₀(T) = Hom_{O_{T₀}}(f₀*g₀*(N_{Y/X} ⊗ O_{Y₀}), J ⊗_{O_{S₀}} O_{T₀})
M₀′(T) = Hom_{O_{T₀}}(f₀*(N_{Y′/X′} ⊗ O_{Y₀′}), J ⊗_{O_{S₀}} O_{T₀}).
```

<!-- original page 143 -->

*Note immediately that $Z_{0} = Y_{0}'$ and that on the category of $Z$-schemes $T$ which are flat over $S$, $M$ and
$M'$ coincide, respectively, with the functors $\prod_{S_{0}/S} M_{0}$ and $\prod_{S_{0}/S} M_{0}'$. In this case,
$b_{f_{0}}$ is simply the morphism*

$$ f_{0}* : M_{0}(Y_{0}') \longrightarrow M(T_{0}) $$

*induced by $f_{0}$, and for every morphism $u : U \to T$, setting $h = f \circ u$, one has a commutative diagram*

```text
M₀′(T₀) ──{a_{g₀}(f₀)}──► M₀(T₀)
   │                          │
   u₀*                        u₀*
   ↓                          ↓
M₀′(U₀) ──{a_{g₀}(h₀)}──► M₀(U₀)
```

*i.e. $a_{g_{0}}$ becomes a morphism of functors $\prod_{S_{0}/S} M_{0}' \to \prod_{S_{0}/S} M_{0}$.*

**Proposition 4.13.** *Suppose $Y'$ flat over $S$. One has then the formula:*

<!-- label: III.III.4.13 -->

```text
c(X, Y, g ∘ f) = a_{g₀}(c(X′, Y′, f)) + b_{f₀}(c(X, Y, g ∘ i′)).
```

Since the definition of the different obstructions and of the morphisms $a_{g_{0}}$ and $b_{f_{0}}$ is local, one easily
sees that it suffices to verify the given formula when the different schemes in play are affine. Let us thus denote $S =
\operatorname{Spec}(\Lambda)$, $S_{J} = \operatorname{Spec}(\Lambda/J)$, $S_{0} = \operatorname{Spec}(\Lambda/I)$, $T =
\operatorname{Spec}(C)$, $X = \operatorname{Spec}(A)$, $Y = \operatorname{Spec}(A/I_{Y}) = \operatorname{Spec}(B)$, $X'
= \operatorname{Spec}(A')$, $Y' = \operatorname{Spec}(A'/I_{Y'}) = \operatorname{Spec}(B')$.

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

Let us study the different terms of the formula to be proved. In what follows, if $x \in I_{Y}$ (resp. $u \in I_{Y'}$),
we denote by $\bar{x}$ (resp. `ū`) its image in $I_{Y}/I^{2}_{Y}$ (resp. $I_{Y'}/I^{2}_{Y'}$); on the other hand, if $m$
belongs to a $\Lambda$-module $M$, we denote by $\bar{m}_{0}$ its image in $M_{0} = M/IM$.

One has seen that $c = c(X, Y, g \circ f)$ is the unique $C_{0}$-morphism $I_{Y}/I^{2}_{Y} \otimes_{B} C_{0} \to JC$
such that $c(\bar{x} \otimes 1) = f(g(x))$, for every $x \in I_{Y}$.

<!-- original page 144 -->

Fix $x \in I_{Y}$; one has $g(x) \in I_{Y'} + JA'$ since $g_{J}(Y_{J}') \subset Y_{J}$. Write $g(x) = x' + \Sigma
\lambda_{i} a'_{i}$, with $x' \in I_{Y'}$, $\lambda_{i} \in J$, $a'_{i} \in A'$. One therefore has

```text
(1)    c(X, Y, g ∘ f)(x̄ ⊗ 1) = f(g(x)) = f(x′) + Σ λᵢ f(a′ᵢ).
```

Now consider $a_{g_{0}}(c(X', Y', f))$. According to the definitions laid down, it is defined by the diagram

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

One has therefore $a_{g_{0}}(c(X', Y', f))(\bar{x} \otimes 1) = f(u)$, where $u$ is an element of $I_{Y'}$ whose image
`ū` in $I_{Y_{0}'}/I^{2}_{Y_{0}'}$ satisfies $\bar{u}_{0} \otimes 1 = \bar{g}_{0}(\bar{x}_{0}) \otimes 1 =
\bar{g}_{0}(\bar{x}_{0}) \otimes 1$. One can therefore take $u = x'$ and one finds

```text
(2)    a_{g₀}(c(X′, Y′, f))(x̄ ⊗ 1) = f(x′).
```

Consider finally $b_{f_{0}}(c(X, Y, g \circ i'))$. By hypothesis, the morphism of $\Lambda_{0}$-algebras $f_{0} : A_{0}'
\to C_{0}$ factors through $B_{0}'$, and therefore, since $J \otimes_{\Lambda_{0}} B_{0}' \xrightarrow{\sim} JB'$ ($B'$
being flat over $\Lambda$), one obtains a morphism of $B_{0}'$-modules $\psi : JB' \to JC$ such that one has a
commutative diagram:

```text
J ⊗_{Λ₀} A₀′ ──{id⊗π′}──► J ⊗_{Λ₀} B₀′ ──{id⊗f₀}──► J ⊗_{Λ₀} C₀
       │                          │ ≀
       ↓                          ↓
   JA′  ──────π′──────►       JB′ ──ψ─►       JC.
```

Denote $\phi : JB' \otimes_{B_{0}'} C_{0} \to JC$ the morphism of $C_{0}$-modules deduced from $\psi$; then one has, for
every $a' \in A'$, $\lambda \in J$,

```text
(†)    φ(λπ′(a′) ⊗ 1) = λf(a′).
```

<!-- original page 145 -->

Then, $b_{f_{0}}(c(X, Y, g \circ i'))$ is defined by the commutative diagram:

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

**Corollary 4.14.** *Let $Y, Y'$ be two flat subschemes of $X$, reducing to `Y_J`; suppose $Y_{0}$ locally complete
intersection in $X_{0}$. If $f : T \to X$ is an $S$-morphism such that $f_{J}$ factors through $Y_{J} \to X_{J}$, one
has the formula*

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

one finds $c(X, Y, f) - c(X, Y', f) = b_{f_{0}}(c(X, Y, i'))$. Moreover, by 4.8 (ii), one has $c(X, Y, i') = d(Y, Y')$.

**Proposition 4.15.** *Let $X$ be an $S$-group smooth over $S$ and $Y$ a sub-$S$-group flat and locally of finite
presentation over $S$. Then $Y$ is locally complete intersection (cf. 4.6.2) in $X$.*

<!-- label: III.III.4.15 -->

<!-- original page 146 -->

*Proof.*[^N.D.E-III-105] We shall show that the immersion $Y \to X$ is regular in the sense of [EGA IV₄, 16.9.2](https://jcreinhold.github.io/ega/iv/29-ch4-16-differential-invariants.html#169-regular-and-quasi-regular-immersions), which
implies that it is also regular in the sense of 4.6.2, by [EGA IV₄, 19.5.1](https://jcreinhold.github.io/ega/iv/32-ch4-19-regular-immersions.html#195-m-regularity-criteria) (moreover, by loc. cit., the two definitions
are equivalent if $S$ is locally noetherian). Therefore, in what follows, we take "regular immersion" in the sense of
EGA IV₄, 16.9.2. Since $X$ and $Y$ are flat and locally of finite presentation over $S$, then, by [EGA IV₄, 19.2.4](https://jcreinhold.github.io/ega/iv/32-ch4-19-regular-immersions.html#192-transversally-regular-immersions), it
suffices to show that, for every $s \in S$, $Y_{s} \to X_{s}$ is a regular immersion. By [EGA IV₄, 19.1.5](https://jcreinhold.github.io/ega/iv/32-ch4-19-regular-immersions.html#191-properties-of-regular-immersions) (ii), one is
reduced to verifying the assertion on the geometric fibers of $S$, that is, when $S$ is the spectrum of an algebraically
closed field $k$.

Then, by VI_A, 3.2, the quotient $X/Y$ exists and is smooth, the morphism $\pi : X \to X/Y$ is flat, and one has a
cartesian square

```text
Y ──f──► X
│        │
i        π
↓        ↓
e ────► X/Y
```

(where $e$ is the image in $X/Y$ of the unit point of $X$). Therefore, by flat base change (cf. EGA IV₄, 19.1.5 (ii)),
it suffices to see that $i$ is a regular immersion, which is immediate since the noetherian local ring $O_{X/Y, e}$ is
smooth, hence its maximal ideal is generated by a regular sequence.

**4.16.**[^N.D.E-III-106] Let $X$ be an $S$-group smooth over $S$, denote $\mu : X \times_{S} X \to X$ its group law.
Suppose given a sub-`S_J`-group `Y_J` of `X_J`, flat and locally of finite presentation over `S_J`. By 4.15, `Y_J` is
locally complete intersection in $X$.

Hence, by 4.6.5, every flat $S$-scheme[^N.D.E-III-107] $Y$ lifting `Y_J` is locally complete intersection in $X$. For
such a $Y$ one has, by 4.8.0,

<!-- label: III.III.4.16.1 -->

```text
(4.16.1)    N_{Y/X} ⊗_{O_Y} O_{Y₀} = N_{Y₀/X₀} = N_{Y_J/X_J} ⊗_{O_{Y_J}} O_{Y₀}.
```

On the other hand, denote by $\epsilon_{0} : S_{0} \to Y_{0}$ the unit section of $Y_{0}$ and $n_{Y_{0}/X_{0}}$ the
quasi-coherent $O_{S_{0}}$-module:

$$ n_{Y_{0}/X_{0}} = \epsilon_{0}*(N_{Y_{0}/X_{0}}). $$

Since $Y_{0}$ and $X_{0}$ are $S_{0}$-groups, one sees easily that $N_{Y_{0}/X_{0}}$ is invariant under the (say left)
translations of $Y_{0}$, hence[^N.D.E-III-108] is the inverse image by $Y_{0} \to S_{0}$ of $n_{Y_{0}/X_{0}}$, i.e. one
has

<!-- label: III.III.4.16.2 -->

```text
(4.16.2)    N_{Y₀/X₀} = n_{Y₀/X₀} ⊗_{O_{S₀}} O_{Y₀}.
```

<!-- original page 147 -->

Taking (4.16.1) and (4.16.2) into account, one deduces on the one hand from 4.5 that the set of sub-$S$-schemes $Y$ of
$X$, flat over $S$, lifting `Y_J`, is empty or principal homogeneous under

<!-- label: III.III.4.16.3 -->

```text
(4.16.3)    Hom_{O_{Y₀}}(n_{Y₀/X₀} ⊗_{O_{S₀}} O_{Y₀}, J ⊗_{O_{S₀}} O_{Y₀}),
```

and one deduces on the other hand from 4.8 (i) that, for every such $Y$ and every $S$-morphism $f : T \to X$ such that
$f_{J} : T_{J} \to X_{J}$ factors through `Y_J`, the obstruction $c(X, Y, f)$ to $f$ factoring through $Y$ is an element
of

```text
Hom_{O_{T₀}}(n_{Y₀/X₀} ⊗_{O_{S₀}} O_{T₀}, JO_T);
```

if moreover $T$ is flat over $S$, this last group equals

```text
Hom_{O_{T₀}}(n_{Y₀/X₀} ⊗_{O_{S₀}} O_{T₀}, J ⊗_{O_{S₀}} O_{T₀}).
```

This leads to introducing the group functor $N_{0}$ below:

**Definition 4.16.1.** *Let $N_{0}$ be the $S_{0}$-functor in commutative groups defined by: for every $Z \in Ob
(Sch)/S_{0}$,*

<!-- label: III.III.4.16.1d -->

```text
(∗)    Hom_{S₀}(Z, N₀) = Hom_{O_Z}(n_{Y₀/X₀} ⊗_{O_{S₀}} O_Z, J ⊗_{O_{S₀}} O_Z).
```

*Then, the set of sub-$S$-schemes $Y$ of $X$, flat over $S$, lifting `Y_J`, is empty or principal homogeneous under*

```text
Hom_{S₀}(Y₀, N₀) = C¹(Y₀, N₀).
```

*For each such $Y$, consider the following diagram:*

```text
                Y ×_S Y          Y
                  ⊂              ⊂
                (i,i)            i
                  ↓     μ        ↓
                X ×_S X ────► X
```

*and denote $DY = c(X, Y, \mu \circ (i, i))$ the obstruction to $\mu \circ (i, i)$ factoring through $Y$, i.e. to $Y$
being stable under the group law of $X$; by what precedes, `DY` is an element of*

```text
N₀(Y₀ ×_{S₀} Y₀) = C²(Y₀, N₀).
```

**Lemma 4.17.**[^N.D.E-III-109] *Let $X$ be an $S$-group smooth over $S$ and `Y_J` a sub-`S_J`-group of `X_J`, flat and
locally of finite presentation over `S_J`. For each subscheme $Y$ of $X$, flat over $S$ and lifting `Y_J`, consider the
obstruction defined in 4.16.1:*

<!-- label: III.III.4.17 -->

```text
DY ∈ Hom_{S₀}(Y₀ ×_{S₀} Y₀, N₀) = C²(Y₀, N₀)
```

*(i) For $Y$ to be a sub-$S$-group of $X$, it is necessary and sufficient that $DY = 0$.*

<!-- original page 148 -->

*(ii) If one makes $Y_{0}$ act on $N_{0}$ by functoriality from the inner automorphisms of $Y_{0}$, then $DY \in
Z^{2}(Y_{0}, N_{0})$.*

*(iii) If $Y$ and $Y'$ are two subschemes of $X$, flat over $S$, lifting `Y_J` (so that the deviation $d(Y, Y') \in
C^{1}(Y_{0}, N_{0})$ is defined, cf. 4.5.1), one has $DY' - DY = \partial^{1}d(Y, Y')$.[^N.D.E-III-110]*

Let us successively prove these various assertions.

**4.18.** *Proof of 4.17 (i).* By definition, one has $DY = 0$ if and only if $Y$ is stable under the group law of $X$.
Hence $DY = 0$ if $Y$ is a subgroup of $X$. Conversely, if $DY = 0$, $Y$ is equipped with the induced law $\mu_{Y}$,
which is associative and reduces modulo $J$ to the group law on `X_J`; since $Y$ is flat and locally of finite
presentation over $S$, it follows from 3.3 that $\mu_{Y}$ is a group law.

**4.19.** *Proof of 4.17 (ii).* This is done by comparing the two values of $u = c(X, Y, \mu^{2} \circ (i, i, i))$
computed in the two following diagrams $(D_{j})$, $j = 1, 2$:

```text
                Y ×_S Y ×_S Y     Y ×_S Y     Y
                       ⊂              ⊂        ⊂
(D_j)              (i,i,i)        (i,i)         i
                       │  f_j           μ        ↓
                       ↓                ↓        │
                X ×_S X ×_S X ────► X ×_S X ──► X
```

where $f_{1} = (1, \pi)$, $f_{2} = (\pi, 1)$, and where one denotes by $\mu^{2}$ the morphism

```text
μ ∘ f₁ = μ ∘ f₂ : X ×_S X ×_S X ⟶ X.
```

[^N.D.E-III-111]

Set $\mu_{Y} = \mu \circ (i, i)$, $f_{j,Y} = f_{j} \circ (i, i, i)$ and $\mu_{2,Y} = \mu^{2} \circ (i, i, i)$. For $j =
1, 2$, denote by $a_{j}$ and $b_{j}$ the morphisms

```text
a_j = a_{μ₀}((f_{j,Y})₀)    and    b_j = b_{(f_{j,Y})₀},
```

associated with the pair of morphisms $(f_{j,Y}, \mu)$ by Lemma 4.12; one has therefore:

```text
(†)   Hom_{O_{Y₀³}}((f_{j,Y})₀*(N_{Y₀×Y₀/X₀×X₀}), JO_{Y₀³}) ──{a_j}──► Hom_{O_{Y₀³}}((μ_{2,Y})₀*(N_{Y₀/X₀}), JO_{Y₀³})

      Hom_{O_{Y₀²}}((μ_Y)₀*(N_{Y₀/X₀}), JO_{Y₀²}) ──{b_j}──► Hom_{O_{Y₀³}}((μ_{2,Y})₀*(N_{Y₀/X₀}), JO_{Y₀³}).
```

<!-- original page 149 -->

Since $N_{Y_{0}\times Y_{0}/X_{0}\times X_{0}} \simeq pr_{1}* N_{Y_{0}/X_{0}} \oplus pr_{2}* N_{Y_{0}/X_{0}}$ (since
$X_{0}$ and $Y_{0}$ are flat over $S_{0}$), and $N_{Y_{0}/X_{0}} \simeq n_{Y_{0}/X_{0}} \otimes_{O_{S_{0}}} O_{Y_{0}}$,
then:

```text
(f_{j,Y})₀*(N_{Y₀×Y₀/X₀×X₀}) ≃ (n_{Y₀/X₀} ⊕ n_{Y₀/X₀}) ⊗ O_{Y₀³}
```

and, likewise,

```text
(μ_{2,Y})₀*(N_{Y₀/X₀}) ≃ n_{Y₀/X₀} ⊗ O_{Y₀³}    and    (μ_Y)₀*(N_{Y₀/X₀}) ≃ n_{Y₀/X₀} ⊗ O_{Y₀²}.
```

Moreover, since $Y^{2}_{0}$ and $Y^{3}_{0}$ are flat over $S_{0}$, then `(†)` rewrites in the following form:

```text
(‡)  ⎧ a_j : Hom_{S₀}(Y₀³, N₀ ⊕ N₀) → Hom_{S₀}(Y₀³, N₀)
     ⎩ b_j : Hom_{S₀}(Y₀², N₀) → Hom_{S₀}(Y₀³, N₀).
```

Applying 4.13 twice to $c(X, Y, \mu_{2,Y}) = u$, one obtains:

```text
a₁(c(X², Y², f₁)) + b₁(c(X, Y, μ_Y)) = u = a₂(c(X², Y², f₂)) + b₂(c(X, Y, μ_Y)).
```

Now, $c(X, Y, \mu_{Y}) = DY$ and, since $f_{1} = (1, \mu)$ and $f_{2} = (\mu, 1)$, one has, with evident notations:

```text
c(X², Y², f₁) = (0, DY)    and    c(X², Y², f₂) = (DY, 0).
```

Hence, one obtains:

```text
u = a₁((0, DY)) + b₁(DY) = a₂((DY, 0)) + b₂(DY).
```

The first thing one notes is that $b_{j}$ is nothing other than $\operatorname{Hom}_{S_{0}}((f_{j,Y})_{0}, N_{0})$, that
is to say, the morphism deduced from $(f_{j,Y})_{0}$ by functoriality.

The identity above therefore becomes:

```text
a₁((0, DY)) − Hom((μ, 1), N₀)(DY) + Hom((1, μ), N₀)(DY) − a₂((DY, 0)) = 0.
```

One recognizes the two middle terms: they are the parts "$DY(xy, z)$" and "$DY(x, yz)$" of the 2-coboundary formula. It
only remains, then, to identify the two other terms.

We must first compute the map $a_{j}$. Now it comes, by inverse image by $(f_{j,Y})_{0}$, from the morphism of
$O_{Y^{2}_{0}}$-modules

```text
P : n_{Y₀/X₀} ⊗ O_{Y₀²} ⟶ (n_{Y₀/X₀} ⊕ n_{Y₀/X₀}) ⊗ O_{Y₀²}
```

induced by the product in $Y_{0}$. Now this morphism is described in the following way: consider the vector bundle $V =
V(n_{Y_{0}/X_{0}})$; $P$ gives by duality a morphism

```text
V(P) : V ×_{S₀} V ×_{S₀} Y₀ ×_{S₀} Y₀ ⟶ V ×_{S₀} Y₀ ×_{S₀} Y₀
```

<!-- original page 150 -->

which is expressed set-theoretically by[^N.D.E-III-112]

```text
V(P)(u, v, a, b) = (u + Ad(a)v, ab, b).
```

This is proved exactly like the corresponding fact on Lie algebras, that is, on the module $\omega^{1}_{Y_{0}/S_{0}}$.
One first notes that $V$ is endowed by functoriality in $Y_{0}$ with a group structure in the category of vector bundles
on $S_{0}$; by virtue of the lemma already used for Lie algebras (Exposé II, 3.10), this structure coincides with the
group structure underlying its `O_S`-module structure. One then sees that $V(n_{Y_{0}/X_{0}} \otimes_{O_{S_{0}}}
O_{Y_{0}}) = V(N_{Y_{0}/X_{0}})$ is also endowed with a structure of $S_{0}$-group which is none other than the
semi-direct product of that of $V$ by that of $Y_{0}$. It only remains to identify the operations of $Y_{0}$ on $V$ to
establish the desired formula.

Let us now compute the two remaining terms. Consider first $a_{1}((0, DY))$. One computes it by the diagram (where $n$
denotes $n_{Y_{0}/X_{0}}$):

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

Considering now the vector bundles defined by these different modules as so many schemes over $S_{0}$ and taking points
with values in anything, one has, denoting $(u, x, y, z)$ a point of $V(J) \times Y^{3}_{0}$;

```text
(Ad(x)DY_{y,z}(u), x, yz) ◄──────── (0 + DY_{y,z}(u), x, yz)
              ↑                                  ↑
              │                                  │
              │                            (0 + DY_{y,z}(u), x, y, z)
              │                                  ↑
              │                                  │
(Ad(x)DY_{y,z}(u), x, y, z) ◄──────── (u, x, y, z).
```

One has thus obtained $a_{1}((0, DY))(x, y, z) = Ad(x)DY(y, z)$, which is indeed the first term of the coboundary. One
would have likewise $a_{2}((DY, 0))(x, y, z) = DY(x, y)$, whence[^N.D.E-III-113]

```text
0 = Ad(x)DY(y, z) − DY(xy, z) + DY(x, yz) − DY(x, y) = (∂²DY)(x, y, z).
```

<!-- original page 151 -->

**4.20.** *Proof of 4.17 (iii).*[^N.D.E-III-114] This is done by comparing the two values of $v = c(X, Y, \mu \circ (i',
i'))$ computed in the two following diagrams

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

Denote $f = \mu \circ (i', i')$; then $(\ast)$ gives

```text
(1)    v = DY′ + f₀*(c(X, Y, i′)).
```

Now $Y_{0}' = Y_{0}$ and $f_{0}$ is the multiplication $Y^{2}_{0} \to Y_{0}$; one deduces from this that

```text
(2)    f₀*(c(X, Y, i′))(x₀, y₀) = c(X, Y, i′)(x₀y₀).
```

Set $c = c(X, Y, i')$; via the identification $N_{0}' \simeq N_{0} \oplus N_{0}$, $c(X \times_{S} X, Y \times_{S} Y,
(i', i'))$ identifies with the pair $(c, c)$. Then, denoting $h = (i', i')$, `(†)` gives

```text
(3)    v = h₀*(DY) + a_{μ₀}(c, c).
```

Now $h_{0}$ is the identity map of $Y^{2}_{0}$, whence $h_{0}*(DY) = DY$. Finally, by the computation of $a_{\mu_{0}}$
done previously, one has for every $S' \to S$ and $x_{0}, y_{0} \in Y_{0}(S_{0}')$,

```text
(4)    a_{μ₀}(c, c)(x₀, y₀) = c(x₀) + Ad(x₀)(c(y₀)).
```

One thus obtains:

```text
(DY′ − DY)(x₀, y₀) = Ad(x₀)c(X, Y, i′)(y₀) − c(X, Y, i′)(x₀y₀) + c(X, Y, i′)(x₀)
                    = (∂¹c(X, Y, i′))(x₀, y₀).
```

Since $c(X, Y, i') = d(Y, Y')$ (cf. 4.8 (ii)), this shows that $DY' - DY = \partial^{1}d(Y, Y')$.

**Theorem 4.21.** *Let $S$ be a scheme, $I$ and $J$ two ideals[^N.D.E-III-115] on $S$ such that $I \supset J$ and $I
\cdot J = 0$. Let $X$ be an $S$-group smooth over $S$ and `Y_J` a sub-`S_J`-group of `X_J`, flat and locally of finite
presentation over `S_J`. Consider the $S_{0}$-functor in commutative groups $N_{0}$ defined by*

<!-- label: III.III.4.21 -->

```text
Hom_{S₀}(T, N₀) = Hom_{O_T}(n_{Y₀/X₀} ⊗_{O_{S₀}} O_T, J ⊗_{O_{S₀}} O_T),    T ∈ Ob (Sch)/S₀,
```

*on which $Y_{0}$ acts via the inner automorphisms of $X_{0}$.*

*(i) For there to exist a sub-$S$-group of $X$, flat over $S$, which reduces to `Y_J`, it is necessary and sufficient
that the two following conditions be verified:*

<!-- original page 152 -->

*(i₁) There exists a subscheme $Y$ of $X$, flat over $S$, lifting `Y_J` (condition automatically satisfied if $Y_{0}$ is
affine, cf. 4.6.5).*

*(i₂) A certain canonical obstruction, element of $H^{2}(Y_{0}, N_{0})$, is zero.*

*(ii) If the conditions of (i) are satisfied, the set of sub-$S$-groups $Y$ of $X$, flat over $S$ and reducing to `Y_J`
is a principal homogeneous set under the group $Z^{1}(Y_{0}, N_{0})$.[^N.D.E-III-116]*

Indeed, condition (i₁) is necessary. Suppose it satisfied and let $Y$ be flat over $S$ lifting `Y_J`. We must seek a
$Y'$ flat over $S$ lifting `Y_J` as well such that $DY' = 0$,[^N.D.E-III-117] cf. 4.17 (i). By 4.17 (iii), this amounts
to seeking a $d(Y', Y) \in C^{1}(Y_{0}, N_{0})$ such that $DY = \partial^{1}d(Y', Y)$.[^N.D.E-III-118]

Let $c \in H^{2}(Y_{0}, N_{0})$ be the image class of `DY`, which is a cocycle by 4.17 (ii). It does not depend on the
choice of $Y$ by 4.17 (iii), and its vanishing is necessary and sufficient for the existence of a $d(Y', Y)$ satisfying
the preceding equation. This proves (i).

If one has now chosen $Y$ such that $DY = 0$, the equation to solve becomes $\partial^{1}d(Y', Y) = 0$, which proves
(ii).

**Remark 4.22.** *Let us keep the notation of 4.21. By 4.15, $Y_{0}$ is locally complete intersection in $X_{0}$, hence
$N_{Y_{0}/X_{0}}$ is a finite locally free $O_{Y_{0}}$-module, and consequently $n_{Y_{0}/X_{0}} =
\epsilon_{0}*(N_{Y_{0}/X_{0}})$ is a finite locally free $O_{S_{0}}$-module. Hence, denoting $n^{\vee}_{Y_{0}/X_{0}} =
\operatorname{Hom}_{O_{Y_{0}}}(n_{Y_{0}/X_{0}}, O_{Y_{0}})$, one has*

<!-- label: III.III.4.22 -->

```text
Hom_{O_T}(n_{Y₀/X₀} ⊗_{O_{S₀}} O_T, J ⊗_{O_{S₀}} O_T) ≃ n_{Y₀/X₀}^∨ ⊗_{O_{S₀}} J ⊗_{O_{S₀}} O_T.
```

*for every $T \to S_{0}$.[^N.D.E-III-119] Consequently, the $S_{0}$-functor $N_{0}$ is isomorphic to the functor*

```text
W(n_{Y₀/X₀}^∨ ⊗_{O_{S₀}} J) ≃ W(Hom_{O_{S₀}}(n_{Y₀/X₀}, J)).
```

*It results in isomorphisms:[^N.D.E-III-120]*

```text
H²(Y₀, N₀) ≃ H²(Y₀, Hom_{O_{S₀}}(n_{Y₀/X₀}, J)) ≃ H²(Y₀, n_{Y₀/X₀}^∨ ⊗_{O_{S₀}} J),
Z¹(Y₀, N₀) ≃ Z¹(Y₀, Hom_{O_{S₀}}(n_{Y₀/X₀}, J)) ≃ Z¹(Y₀, n_{Y₀/X₀}^∨ ⊗_{O_{S₀}} J).
```

**4.23.** Still under the hypotheses of 4.21, we are now going to study how the set of $Y$ lifting `Y_J` behaves with
respect to conjugation by sections of $X$. If $x$ is a section of $X$ over $S$ inducing the unit section of `X_J`, the
inner automorphism $Int(x)$ defined by $x$ transforms flat subgroups of $X$ lifting `Y_J` into flat subgroups of $X$
lifting `Y_J`. Now, under the conditions of 4.21 (ii), the set of these subgroups is principal homogeneous under
$Z^{1}(Y_{0}, N_{0})$; we shall see that there then exists a subgroup $\Gamma$ of $B^{1}(Y_{0}, N_{0})$[^N.D.E-III-121]
such that two subgroups of $X$, flat over $S$, and lifting `Y_J`, are conjugate (by $x \in X(S)$ inducing the unit of
$X(S_{J})$) if and only if their "difference" in $Z^{1}(Y_{0}, N_{0})$ is an element of $\Gamma$. In the best cases, we
shall show that $\Gamma$ equals $B^{1}(Y_{0}, N_{0})$, hence that the set of flat subgroups of $X$ lifting `Y_J`, modulo
conjugation by $x \in X(S)$ inducing the unit of $X(S_{J})$, is empty or principal homogeneous under $H^{1}(Y_{0},
N_{0})$ (cf. 4.29 and 4.36).

<!-- original page 153 -->

**4.24.** We keep the notation of 4.21. Let $Y$ be a flat subgroup of $X$, reducing to `Y_J`. Recall that we introduced
in 0.5 the functor $L^{X}_{0}$ (resp. $L^{Y}_{0}$) defined by the identity with respect to the variable $S_{0}$-scheme
$T$:

```text
Hom_{S₀}(T, L₀^X) = Hom_{O_T}(ω¹_{X₀/S₀} ⊗_{O_{S₀}} O_T, J ⊗_{O_{S₀}} O_T)
```

(resp. similarly on replacing $X$ by $Y$), as well as the functor $L'_{X} = \prod_{S_{0}/S} L^{X}_{0}$.

Now one has:

**Lemma 4.25.** *There exists a canonical exact sequence of $Y_{0}$-$O_{S_{0}}$-modules*

<!-- label: III.III.4.25 -->

```text
(+)    n_{Y₀/X₀} ──d──► ω¹_{X₀/S₀} ──► ω¹_{Y₀/S₀} ──► 0
```

*possessing the following properties:*

*(i) By inverse image on $Y_{0}$, $d$ gives the morphism $\bar{D}_{0}$ of 4.8 (iii).*

*(ii) If $X_{0}$ and $Y_{0}$ are smooth over $S_{0}$, then $d$ is injective. Since the two $\omega^{1}$ are then locally
free of finite type, so is $n_{Y_{0}/X_{0}}$ and the sequence is locally split.*

*Proof.*[^N.D.E-III-122] Denote by $\pi_{0}$ the morphism $Y_{0} \to S_{0}$. By SGA 1 II, formula (4.3) (see also [EGA
IV₄, 16.4.21](https://jcreinhold.github.io/ega/iv/29-ch4-16-differential-invariants.html#164-functorial-properties-of-differential-invariants)), one has a canonical exact sequence of $O_{Y_{0}}$-modules

```text
(†)    N_{Y₀/X₀} ──D̄₀──► Ω¹_{X₀/S₀} ⊗_{O_{X₀}} O_{Y₀} ──► Ω¹_{Y₀/S₀} ──► 0.
```

Since this sequence is formed of $(Y_{0} \times_{S} Y_{0})$-equivariant modules and morphisms, its inverse image `(+)`
by $\epsilon_{0}*$ is an exact sequence of $Y_{0}$-$O_{S_{0}}$-modules, and `(†)` is the inverse image of `(+)` by
$\pi_{0}*$ (cf. Exp. I, § 6.8). This proves (i).

<!-- original page 154 -->

Suppose moreover $X_{0}$ and $Y_{0}$ smooth over $S_{0}$. Then, by SGA 1 II 4.10 (see also [EGA IV₄, 17.2.3](https://jcreinhold.github.io/ega/iv/30-ch4-17-smooth-unramified-etale-morphisms.html#172-general-differential-properties) (i) and
17.2.5), $D$ is injective and the sequence `(†)` is formed of $O_{Y_{0}}$-modules locally free of finite type (hence is
locally split). By the equivalence of categories I, 6.8.1, $d$ is also injective, and therefore the sequence `(+)` has
the indicated properties.

**4.26.**[^N.D.E-III-123] For every $S_{0}$-scheme $f : T \to S_{0}$, `(+)` gives an exact sequence of
$Y_{0}(T)$-$O(T)$-modules

```text
0 ⟶ Hom_{O_T}(f*(ω¹_{Y₀/S₀}), f*(J)) ⟶ Hom_{O_T}(f*(ω¹_{X₀/S₀}), f*(J)) ⟶ Hom_{O_T}(f*(n_{Y₀/X₀}), f*(J)),
```

hence one has an exact sequence of $Y_{0}$-$O_{S_{0}}$-modules:

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

Note that $C^{0}(Y_{0}, L^{Y}_{0})$ (resp. $C^{0}(Y_{0}, L^{X}_{0})$) is none other than
$\operatorname{Hom}_{S_{0}}(S_{0}, L^{Y}_{0}) = \operatorname{Hom}_{S}(S, L'_{Y})$ (resp. ···), i.e. (cf. 0.9) the group
of sections of $Y$ (resp. $X$) over $S$ inducing the unit section of `X_J`. Note also that $d^{1}$ is none other than
the morphism $v_{i_{Y_{0}}}$ of 4.8 (iii), where $i_{Y_{0}} : Y_{0} \to X_{0}$ is the canonical
immersion.[^N.D.E-III-124]

**Lemma 4.27.** *Under the conditions of 4.21 for `S, I, J` and $X$, let $Y$ be a subgroup of $X$, flat over $S$ and
lifting `Y_J`. Denote $i : Y \hookrightarrow X$ the canonical immersion.[^N.D.E-III-125]*

<!-- label: III.III.4.27 -->

*(i) Let $i' : Y \to X$ be a morphism of $S$-schemes lifting $i_{0}$ (so that $i'$ is also an immersion), let $Y' =
i'(Y)$ and let $d(i, i')$ be the element of $C^{1}(Y_{0}, L^{X}_{0})$ such that $i' = d(i, i') \cdot i$ (cf. 1.2.4).
Then the deviation $d(Y, Y') \in C^{1}(Y_{0}, N_{0})$ (cf. 4.5.1) is given by the formula:*

```text
d(Y, Y′) = d¹(d(i, i′)).
```

*(ii) Let $x \in C^{0}(Y_{0}, L^{X}_{0})$ be a section of $X$ over $S$ inducing the unit section of `X_J` over `S_J`.
Then the deviation $d(Y, Int(x)Y) \in C^{1}(Y_{0}, N_{0})$ (cf. 4.5.1) is given by the formula:*

<!-- original page 155 -->

```text
−d(Y, Int(x)Y) = d¹∂x = ∂ d⁰x.
```

Indeed, $Y'$ is the image of $Y$ by the composite morphism:[^N.D.E-III-126]

```text
Y ──{(d(i,i′), i)}──► L′_X ×_S X ⟶ X,
```

which is denoted $d(i, i') \cdot i$ in 4.8 (iii); by loc. cit. and the equality $v_{i_{0}} = d^{1}$, one has therefore:

```text
c(X, Y′, d(i, i′) · i) − c(X, Y′, i) = v_{i₀}(d(i, i′)) = d¹(d(i, i′)).
```

But $d(i, i') \cdot i = i'$ factors through $Y'$ by definition, hence the first term is zero; moreover, by 4.8 (ii), one
has $c(X, Y', i) = d(Y', Y) = -d(Y, Y')$. Hence $d(Y, Y') = d^{1}(d(i, i'))$, which proves (i).

Let now $x$ be as in (ii). By the formula

```text
xyx⁻¹ = xyx⁻¹y⁻¹y = (x − Ad(y)x)y = (−∂x)(y) · y,
```

one sees that $Y'$ is the image of $Y$ by the immersion $i' = (-\partial x) \cdot i_{Y}$. Hence, by (i) one obtains

```text
−d(Y, Int(x)Y) = d¹∂x = ∂ d⁰x.
```

**Corollary 4.28.** *For two subgroups $Y$ and $Y'$ of $G$, flat over $S$ and lifting `Y_J`, to be conjugate by a
section of $X$ over $S$ inducing the unit section of `X_J`, it is necessary and sufficient that $d(Y, Y') \in \partial
d^{0} C^{0}(Y_{0}, L^{X}_{0}) \subset \partial C^{0}(Y_{0}, N_{0}) = B^{1}(Y_{0}, N_{0})$.*

<!-- label: III.III.4.28 -->

**Corollary 4.29.** *If $d^{0}$ is surjective, $Y$ and $Y'$ as above are conjugate by a section of $X$ over $S$ inducing
the unit section of `X_J` if and only if $d(Y, Y') \in B^{1}(Y_{0}, N_{0})$.*

<!-- label: III.III.4.29 -->

<!-- original page 156 -->

**Corollary 4.30.** *Let $Y$ be as in 4.27; the set of conjugates of $Y$ by sections of $X$ over $S$ inducing the unit
section of `X_J` is isomorphic to:*

<!-- label: III.III.4.30 -->

```text
d¹∂(C⁰(Y₀, L₀^X)) = C⁰(Y₀, L₀^X) / Ker d¹∂.
```

Note now that $C^{0}(Y_{0}, L^{X}_{0})/Ker d^{1}\partial$ is computed solely with the help of the left square of the
commutative diagram of 4.26. It follows in particular that one can also compute it in any diagram of the same type
having the same left square. Consider in particular the functor $L^{X}_{0}/L^{Y}_{0}$ above $S_{0}$ defined by

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

**Corollary 4.31.** *Let $Y$ be as in 4.27; the set of conjugates of $Y$ by sections of $X$ over $S$ inducing the unit
section of `X_J` is isomorphic to*

<!-- label: III.III.4.31 -->

```text
E = ∂(C⁰(Y₀, L₀^X/L₀^Y)) = C⁰(Y₀, L₀^X/L₀^Y) / H⁰(Y₀, L₀^X/L₀^Y).
```

**Corollary 4.32.** *Suppose moreover $S_{0}$ affine and $\omega^{1}_{Y_{0}/S_{0}}$ finite locally free.[^N.D.E-III-127]
If one denotes $F_{0} = [Lie(X_{0}/S_{0})/Lie(Y_{0}/S_{0})] \otimes_{O_{S_{0}}} J$, one has $E = \Gamma(S_{0},
F_{0})/H^{0}(Y_{0}, F_{0})$.*

<!-- label: III.III.4.32 -->

[^N.D.E-III-128] Indeed, since $\omega^{1}_{Y_{0}/S_{0}}$ is finite locally free, as is $\omega^{1}_{X_{0}/S_{0}}$
(since $X$ is supposed smooth over $S$), one has, by 0.6:

```text
L₀^Y = W(Lie(Y₀/S₀) ⊗_{O_{S₀}} J)    and    L₀^X = W(Lie(X₀/S₀) ⊗_{O_{S₀}} J).
```

On the other hand, by 4.25, one has an exact sequence of $Y_{0}$-$O_{S_{0}}$-modules:

```text
0 ⟶ K ⟶ ω¹_{X₀/S₀} ──φ──► ω¹_{Y₀/S₀} ⟶ 0
```

(where $K = Ker(\phi)$). Since $\omega^{1}_{Y_{0}/S_{0}}$ and $\omega^{1}_{X_{0}/S_{0}}$ are finite locally free, one
has a locally split exact sequence:

```text
0 ⟶ Lie(Y₀/S₀) ⊗_{O_{S₀}} J ⟶ Lie(X₀/S₀) ⊗_{O_{S₀}} J ⟶ F₀ ⟶ 0.
```

<!-- original page 157 -->

It follows that one has an exact sequence of $Y_{0}$-$O_{S_{0}}$-modules:

$$ 0 \longrightarrow L^{Y}_{0} \longrightarrow L^{X}_{0} \longrightarrow W(F_{0}). $$

By the reasoning that served us to prove 4.31, we can compute $E$ as the image of the composite map

```text
C⁰(Y₀, L₀^X) ──π──► C⁰(Y₀, W(F₀)) ──∂──► C¹(Y₀, W(F₀)).
```

Now the map $\pi$ above is the map $\Gamma(S_{0}, Lie(X_{0}/S_{0}) \otimes_{O_{S_{0}}} J) \to \Gamma(S_{0}, F_{0})$.
Hence, $S_{0}$ being affine, $\pi$ is surjective and one finds indeed the announced result.

**Corollary 4.33.** *Let `S, I, J` and $X$ be as in 4.21, and let $Y$ be a diagonalizable subgroup of $X$. Suppose
$\omega^{1}_{Y_{0}/S_{0}}$ finite locally free and $S_{0}$ affine.[^N.D.E-III-129] The set of subgroups of $X$ conjugate
to $Y$ by a section of $X$ over $S$ inducing the unit section of `X_J` is isomorphic to*

<!-- label: III.III.4.33 -->

```text
E = Γ(S₀, [Lie(X₀/S₀) / Lie(X₀/S₀)^{ad(Y₀)}] ⊗_{Γ(S₀, O_{S₀})} Γ(S₀, J))
```

*[^N.D.E-III-130] that is, isomorphic to $L^{X}_{0}(Y_{0})/H^{0}(Y_{0}, L^{X}_{0})$.*

Indeed, one writes by I 4.7.3 (cf. 2.13):

$$ Lie(X_{0}/S_{0}) = Lie(X_{0}/S_{0})^{ad(Y_{0})} \oplus R. $$

Since $Y_{0}$ is commutative one has $Lie(Y_{0}/S_{0}) \subset Lie(X_{0}/S_{0})^{ad(Y_{0})}$, hence

```text
F₀ = [Lie(X₀/S₀)^{ad(Y₀)} / Lie(Y₀/S₀)] ⊗ J ⊕ R ⊗ J,
F₀^{ad(Y₀)} = [Lie(X₀/S₀)^{ad(Y₀)} / Lie(Y₀/S₀)] ⊗ J.
```

<!-- original page 158 -->

By 4.32, one has therefore $E \simeq \Gamma(S_{0}, R \otimes J)$. Returning to the definition of $R$, one is done.

**Corollary 4.34.** *Let `S, I, J` and $X$ be as in 4.21, and let $Y$ be a diagonalizable subgroup of $X$. Suppose
$\omega^{1}_{Y_{0}/S_{0}}$ finite locally free and $S_{0}$ affine.[^N.D.E-III-131] If $x \in X(S)$ induces the unit
section of `X_J` and normalizes $Y$, then it centralizes $Y$.*

<!-- label: III.III.4.34 -->

This results immediately from comparison of the preceding corollary and 2.14. Indeed, 4.33 shows that the elements of
$C^{0}(Y_{0}, L^{X}_{0})$ which globally preserve $Y$ are the elements of $H^{0}(Y_{0}, L^{X}_{0})$, and one has seen in
2.14 that these are precisely those which act trivially on the canonical immersion $Y \to X$.

**4.35.** Let us return to the general situation of 4.21 and suppose `Y_J` smooth over `S_J`. Then, by 4.25 (ii), one
has an exact sequence of $Y_{0}$-$O_{S_{0}}$-modules:

$$ (\ast) 0 \longrightarrow Lie(Y_{0}/S_{0}) \longrightarrow Lie(X_{0}/S_{0}) \longrightarrow n^{\vee}_{Y_{0}/X_{0}}
\longrightarrow 0 $$

and they are finite locally free $O_{S_{0}}$-modules.

On the other hand, by SGA 1, II 4.10, every subscheme $Y$ of $X$ lifting `Y_J` and flat over $S$ will be smooth over
$S$.[^N.D.E-III-132] Suppose moreover $S_{0}$ and `Y_J` affine. Then, since $n^{\vee}_{Y_{0}/X_{0}}$ is a locally free
$O_{S_{0}}$-module, the sequence $(\ast)$ remains exact when one applies $\otimes_{O_{S_{0}}} J$ to it, and then takes
the inverse image on $Y^{n}_{0}$, and as the $Y^{n}_{0}$ are affine, one therefore obtains an exact sequence of
complexes of abelian groups:

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

Let now $Y, Y'$ be two subgroups of $X$ lifting `Y_J` and flat, hence smooth, over $S$. As `Y_J` is affine, then, by
0.15, $Y$ and $Y'$ are isomorphic as schemes extending `Y_J`, i.e. there exists an isomorphism of $S$-schemes

$$ f : Y \xrightarrow{\sim} Y' $$

<!-- original page 159 -->

inducing the identity on `Y_J`. On the one hand, by 1.2.4, $f$ defines an element $a$ of $C^{1}(Y_{0}, L^{X}_{0})$ such
that $f(y) = a(y_{0})y$, for every $y \in Y(S')$, $S' \to S$, and by 4.27 (i), one has

$$ d^{1}(a) = d(Y, Y'). $$

Moreover, since $Y, Y'$ are subgroups of $X$, the above element belongs to $Z^{1}(Y_{0}, N_{0})$ (cf. 4.21). Then
$\partial a$ is an element of $Z^{2}(Y_{0}, L^{Y}_{0})$ whose image $\bar{\partial}a$ in $H^{2}(Y_{0}, L^{Y}_{0})$
depends only on the class $\bar{d}(Y, Y') \in H^{1}(Y_{0}, N_{0})$; this being the definition of the connecting map
$\partial^{1} : H^{1}(Y_{0}, N_{0}) \to H^{2}(Y_{0}, L^{Y}_{0})$, one has therefore:

$$ \partial^{1}(\bar{d}(Y, Y')) = \bar{\partial}a. $$

On the other hand, let us transport by $f$ the group structure of $Y'$ and let $Y_{1}$ be the group obtained (which thus
has $Y$ as underlying scheme), that is, the group law $\mu_{1}$ of $Y_{1}$ is defined by: for every $S' \to S$ and $x, y
\in Y(S')$,

$$ \mu_{1}(x, y) = f^{-1}(f(x)f(y)). $$

By 3.5.1, $Y_{1}$ defines a cocycle $\delta(Y, Y_{1}) \in Z^{2}(Y_{0}, Lie(Y_{0}/S_{0}))$ such that, for every $S' \to
S$ and $x, y \in Y(S')$, one has

```text
δ(Y, Y₁)(x₀, y₀) xy = μ₁(x, y) = f⁻¹(f(x)f(y)).
```

Set $b = \delta(Y, Y_{1})$. For every $S' \to S$ and $x, y \in Y(S')$, one has $(b(x_{0}, y_{0})xy)_{0} = x_{0}y_{0}$
and therefore one obtains that $f(b(x_{0}, y_{0})xy)$ equals, on the one hand, $a(x_{0}y_{0})b(x_{0}, y_{0})xy$ and, on
the other hand,

```text
f(x)f(y) = a(x₀)x a(y₀)y = a(x₀) Ad(x₀)(a(y₀)) xy.
```

Comparing the two expressions, one obtains that $b(x_{0}, y_{0})$ equals

```text
a(x₀y₀)⁻¹ a(x₀) Ad(x₀)(a(y₀)) = Ad(x₀)(a(y₀)) − a(x₀y₀) + a(x₀) = (∂a)(x₀, y₀),
```

i.e. $\delta(Y, Y_{1}) = \partial a$. We have thus obtained:

**Proposition 4.35.1.**[^N.D.E-III-132] *Under the hypotheses of 4.21, suppose moreover $S_{0}$ affine and `Y_J` smooth
over `S_J` and affine. Let $Y, Y'$ be two subgroups of $X$ lifting `Y_J` and flat (hence smooth) over $S$, let $f : Y
\xrightarrow{\sim} Y'$ be an isomorphism of $S$-schemes inducing the identity on `Y_J`, denote by $Y_{1}$ the group
obtained by transporting via $f$ the group structure of $Y'$. Then one has*

<!-- label: III.III.4.35.1 -->

```text
∂¹(d̄(Y, Y′)) = δ(Y, Y₁).
```

**Proposition 4.36.** *Under the hypotheses of 4.21, suppose moreover `Y_J` smooth over `S_J` and $S_{0}$ affine. The
set of sub-$S$-groups $Y$ of $X$ flat (or smooth) over $S$, reducing to `Y_J`, modulo conjugation by sections of $X$
over $S$ inducing the unit section of `X_J`, is either empty, or a principal homogeneous set under the group*

<!-- label: III.III.4.36 -->

```text
H¹(Y₀, [Lie(X₀/S₀)/Lie(Y₀/S₀)] ⊗_{O_{S₀}} J).
```

<!-- original page 160 -->

It suffices for us to verify that Corollary 4.29 applies, that is, that

```text
d⁰ : Hom_{O_{S₀}}(ω¹_{X₀/S₀}, J) ⟶ Hom_{O_{S₀}}(n_{Y₀/X₀}, J)
```

is surjective. Now this follows from the fact that the sequence `(+)` of 4.25 (ii) is split, $S_{0}$ being
affine.[^N.D.E-III-133]

Let us finally state a corollary common to 4.21 and 4.36, which will in fact be the only form under which we shall use
in what follows the general results of this section.[^N.D.E-III-134]

**Corollary 4.37.** *Let $S$ be a scheme and $S_{0}$ the closed subscheme defined by a nilpotent ideal $I$. Let $X$ be
an $S$-group smooth over $S$, and $Y_{0}$ a sub-$S_{0}$-group of $X_{0}$, flat over $S_{0}$.*

<!-- label: III.III.4.37 -->

*(i) If $S_{0}$ is affine, $Y_{0}$ smooth over $S_{0}$, and if*

```text
H¹(Y₀, [Lie(X₀/S₀)/Lie(Y₀/S₀)] ⊗_{O_{S₀}} Iⁿ⁺¹/Iⁿ⁺²) = 0
```

*for every $n \geq 0$, two sub-$S$-groups of $X$, flat (or smooth) over $S$, reducing to $Y_{0}$, are conjugate by a
section of $X$ over $S$ inducing the unit section of $X_{0}$.*

*(ii) If $Y_{0}$ is affine and of finite presentation and if[^N.D.E-III-135]*

```text
H²(Y₀, n_{Y₀/X₀}^∨ ⊗_{O_{S₀}} Iⁿ⁺¹/Iⁿ⁺²) = 0
```

*for every $n \geq 0$, there exists a sub-$S$-group of $X$, flat over $S$, reducing to $Y_{0}$.*

**4.38.** It remains to relate the three constructions which we have made in this Exposé. To avoid inessential
complications, we shall place ourselves in the following situation: $S_{0}$ is the spectrum of a field $k$, $S$ is the
spectrum of the dual numbers $D(k)$, $G$ is an $S$-group smooth over $S$, $K$ a sub-$S$-group, smooth over $S$ and
affine.

<!-- original page 161 -->

[^N.D.E-III-136] Denote $g_{0} = Lie G_{0}$ (which here equals $\Gamma(S_{0}, Lie G_{0}) = Lie(G_{0}/S_{0})(S_{0})$) and
$k_{0} = Lie K_{0}$. One has an exact sequence of $k$-vector spaces[^N.D.E-III-137]:

```text
0 ⟶ k₀ ──i──► g₀ ──d──► n_{K₀/G₀}^∨ ⟶ 0,
```

giving rise to an exact cohomology sequence:

```text
0 ⟶ H⁰(K₀, k₀) ──i⁰──► H⁰(K₀, g₀) ──d⁰──► H⁰(K₀, g₀/k₀)
   ──∂⁰──► H¹(K₀, k₀) ──i¹──► H¹(K₀, g₀) ──d¹──► H¹(K₀, n_{K₀/G₀}^∨) ──∂¹──► H²(K₀, k₀).
```

Now these various groups all have a geometric meaning.

a) $H^{0}(K_{0}, k_{0}) = Lie Centr(K_{0})$[^N.D.E-III-138] by II 5.2.3.

b) $H^{0}(K_{0}, g_{0}) = Lie Centr_{G_{0}}(K_{0})$[^N.D.E-III-138] (idem).

c) $H^{0}(K_{0}, g_{0}/k_{0}) = Lie Norm_{G_{0}}(K_{0})/k_{0}$[^N.D.E-III-138] (idem).

d) $H^{1}(K_{0}, k_{0}) = Lie \operatorname{Aut}_{S_{0}-gr.}(K_{0}) / Im(k_{0})$, where $Im(k_{0})$ denotes the image of
$k_{0}$ by the morphism $Lie(Int_{0})$ deduced from $Int_{0} : K_{0} \to \operatorname{Aut}_{S_{0}-gr.}(K_{0})$. Indeed,
it follows from 2.1 (ii), applied to $Y = X = K$ and $f_{0} = id_{K_{0}}$, that $Z^{1}(K_{0}, k_{0})$ is the group of
infinitesimal automorphisms of the $S_{0}$-group $K_{0}$, and that $H^{1}(K_{0}, k_{0})$ is obtained by quotienting by
inner infinitesimal automorphisms, i.e. by the image of $k_{0}$. Moreover, by II 4.2.2, one also has $Z^{1}(K_{0},
k_{0}) = Lie \operatorname{Aut}_{S_{0}-gr.}(K_{0})$[^N.D.E-III-139].

<!-- original page 162 -->

e) $H^{1}(K_{0}, g_{0})$ is, by 2.1 (ii), the group of deviations between homomorphisms $K \to G$ extending the
canonical immersion $i_{0} : K_{0} \to G_{0}$, modulo the deviations obtained by the action of the inner automorphisms
of $G$ defined by elements of $G(S)$ giving the unit of $G(S_{0})$ (that is, elements of $g_{0}$).

f) $H^{1}(K_{0}, n^{\vee}_{K_{0}/G_{0}})$ is, by 4.36, the group of deviations between subgroups $K'$ of $G$ extending
$K_{0}$ and flat over $S$ (hence smooth over $S$, cf. SGA 1, II 4.10), modulo the deviations obtained by the action of
the inner automorphisms of $G$ constructed as previously.

g) $H^{2}(K_{0}, k_{0})$ is, by 3.5 (ii), the group of deviations between group structures on $K$ extending that of
$K_{0}$, modulo the $S$-automorphisms of $K$ inducing the identity on $K_{0}$.

We now propose to show how one can make explicit the six morphisms of the preceding exact sequence in the geometric
interpretation we have just given.

1. $i^{0}$ and $d^{0}$ are nothing other than the morphisms obtained by passage to the Lie algebra (then by passage to
   the quotient for $d^{0}$), starting from the canonical monomorphisms:

```text
Centr(K₀) ⟶ Centr_{G₀}(K₀) ⟶ Norm_{G₀}(K₀).
```

This indeed results immediately from the definition of the identifications (a), (b), and (c).

1. One constructs $\partial^{0}$ as follows. Let $\bar{x} \in Lie Norm_{G_{0}}(K_{0})/k_{0}$. Lift it to
   `x ∈ Lie Norm_{G₀}(K₀) ⊂ Norm_G(K)(S)`. Then $Int(x)$ defines an automorphism of $K$ inducing the identity on
   $K_{0}$, hence an element of $Lie \operatorname{Aut}_{S_{0}-gr.}(K_{0})$. Denote $Int(\bar{x})$ the image of this
   element in $Lie \operatorname{Aut}_{S_{0}-gr.}(K_{0})/Im(k_{0})$. Then one has:

<!-- original page 163 -->

$$ (\ast) \partial^{0}(\bar{x}) = -Int(\bar{x}) = Int(\bar{x}^{-1}). $$

Indeed, let us compute the element of $Lie \operatorname{Aut}_{S_{0}-gr.}(K_{0})$ defined by $Int(x)$. It will
correspond by definition to an element $a$ of $Z^{1}(K_{0}, k_{0})$ such that

```text
x y x⁻¹ = a(y₀) y,    for every y ∈ K(S′), S′ → S.
```

But this can also be written $a(y_{0}) = xyx^{-1}y^{-1} = x - Ad(y)x = -\partial(x)(y_{0})$, whence $a = -\partial(x)$.

[^N.D.E-III-140] On the other hand, the image of $x \in Lie Norm_{G_{0}}(K_{0}) \subset g_{0}$ by $\partial$ is an
element of $Z^{1}(K_{0}, k_{0})$, whose image $\bar{\partial}(x)$ in $H^{1}(K_{0}, k_{0})$ depends only on $\bar{x}$,
and by definition of the connecting map $\partial^{0}$, one has

$$ \partial^{0}(\bar{x}) = \bar{\partial}(x); $$

combined with the equality $a = -\partial(x)$, this proves $(\ast)$.

3)[^N.D.E-III-141] Denote $i : K \to G$ the canonical immersion. Let `ū` be an element of $H^{1}(K_{0}, k_{0})$, image
of a

```text
u ∈ Lie Aut_{S₀-gr.}(K₀) ⊂ Aut_{S-gr.}(K).
```

Then one has:

```text
(∗∗)    i¹(ū) = d̄(i, i ∘ u),
```

where $\bar{d}(i, i \circ u)$ is the class defined in 2.1.1.

Indeed, $u$ is the image of an element $v \in Z^{1}(K_{0}, k_{0})$ such that $u(y) = v(y_{0})y$, and $i^{1}(\bar{u})$ is
the image in $H^{1}(K_{0}, g_{0})$ of the cocycle $i \circ v \in Z^{1}(K_{0}, g_{0})$.

Now, since $i$ is a morphism of groups, the equality $u(y) = v(y_{0})y$ entails $iu(y) = iv(y_{0})i(y)$. It follows that
$i \circ v = d(i, i \circ u)$, whence $(\ast\ast)$.

1. Let $i' : K \to G$ be a morphism of groups lifting $i_{0}$, let $d(i, i')$ be the class defined in 2.1.1, and let
   $d(K, i'(K)) \in C^{1}(K_{0}, n_{K_{0}/X_{0}})$ be the deviation defined in 4.5.1; by 4.21, $d(K, i'(K))$ belongs to
   $Z^{1}(K_{0}, n_{K_{0}/X_{0}})$. Denote $\bar{d}(K, i'(K))$ its image in $H^{1}(K_{0}, n_{K_{0}/X_{0}})$. Then, by
   4.27 (i), one has:

<!-- original page 164 -->

```text
(†)    d¹(d̄(i, i′)) = d̄(K, i′(K)).
```

1. Finally, let $K'$ be a subgroup of $G$ lifting $K_{0}$ and flat, hence smooth, over $S$. We have supposed that
   $K_{0}$ is affine. Then one knows that $K$ and $K'$ are isomorphic as schemes extending $K_{0}$ (cf. 0.15), hence
   there exists an isomorphism of $S$-schemes

$$ f : K \xrightarrow{\sim} K' $$

inducing the identity on $K_{0}$. Let us transport by $f$ the group structure of $K'$ and let $K_{1}$ be the group
obtained (which thus has $K$ as underlying scheme), that is, the group law $\mu_{1}$ of $K_{1}$ is defined by: for every
$S' \to S$ and $x, y \in K(S')$,

$$ \mu_{1}(x, y) = f^{-1}(f(x)f(y)). $$

[^N.D.E-III-142] By 3.5.1, $K_{1}$ defines a cocycle $\delta(K, K_{1}) \in Z^{2}(K_{0}, k_{0})$ such that, for every $S'
\to S$ and $x, y \in K(S')$, one has

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

[^N.D.E-III-66]: N.D.E.: Let $E$ be a non-empty set equipped with an associative composition law, such that every left
    translation $\ell_{x}$ is bijective; fix $x_{0} \in E$. There exists a unique $e \in E$ such that $x_{0} \cdot e =
    x_{0}$; then $x_{0} \cdot e \cdot x = x_{0} \cdot x$ entails $e \cdot x = x$, for every $x \in E$. On the other
    hand, for every $x$ there exists a unique $x'$ such that $x \cdot x' = e$. Suppose moreover that there exists $b \in
    E$ such that the right translation $r_{b}$ is injective. Then, for every $x$, the equality $x \cdot e \cdot b = x
    \cdot b$ gives $x \cdot e = x$ (i.e. $e$ is a neutral element), and $x \cdot x' \cdot x = x = x \cdot e$ entails $x'
    \cdot x = e$, i.e. $x'$ is the inverse of $x$ from the left and the right, hence $E$ is a group. Note that the
    hypothesis "$r_{b}$ injective" is necessary: on every set $E$ one can define a composition law by $x \cdot y = y$,
    for all $x, y \in E$; then every left translation is the identity (whence the associativity of the law), but for
    every $y$ one has $r_{y}(E) = {y}$, hence $E$ is not a group if $|E| > 1$.

[^N.D.E-III-67]: N.D.E.: Since $X$ and $X_{0}$ have the same underlying topological space and $t_{0}$ is an
    automorphism, $t$ is a homeomorphism, hence an affine morphism, cf. Exp. VI_B, 2.9.1 or [EGA IV₄, 18.12.7.1](https://jcreinhold.github.io/ega/iv/31-ch4-18-complements-etale-morphisms.html#1812-applications-of-étale-localization-to-quasi-finite-morphisms-generalizations-of-earlier-results). It thus
    suffices to see that if $J$ is a nilpotent ideal of a ring $\Lambda$, and $\phi : A \to B$ a morphism of
    $\Lambda$-algebras, with $B$ flat over $\Lambda$, such that $\phi \otimes_{\Lambda} (\Lambda/J)$ is bijective, then
    $\phi$ is bijective. By the "nilpotent Nakayama lemma", $\phi$ is surjective; moreover, $B$ being flat over
    $\Lambda$, one also has $Ker(\phi) \otimes_{\Lambda} (\Lambda/J) = 0$, whence $Ker(\phi) = 0$, hence $\phi$ is
    bijective.

[^N.D.E-III-68]: N.D.E.: Indeed, by the proof of 0.7, the $S$-endomorphisms of $X$ inducing the identity on `X_J` are
    the automorphisms $m \cdot id_{X}$, for $m$ ranging over $M(X) = \operatorname{Hom}_{S}(X, M)$ (for every $S' \to S$
    and $x \in X(S')$, one has $(m \cdot id_{X})(x) = m(x) \cdot x$). Now, by the proof of 3.1, each $m : X \to M$
    factors in a unique manner through a morphism $h$ from $Y = X^{+}$ to $M$, and therefore $m \cdot id_{X}$ is the
    automorphism $u_{h}$ introduced in 1.3.1. The lemma then follows from the definition of equivalence, cf. 1.3.4 and
    1.3.5.

[^N.D.E-III-69]: N.D.E.: We have added what follows.

[^N.D.E-III-70]: N.D.E.: We have added this remark, analogue of 4.5.1, to introduce the notation $\delta(\mu, \mu')$ (or
    $\delta(X, X')$), used in 4.38; consequently, we have also added in 3.5 (ii) above the part concerning $E$ itself.

[^N.D.E-III-71]: N.D.E.: We have conformed to the sign conventions of the original, in order to have in 4.38 (5) the
    equality $\partial^{1}\bar{d}(X, X') = \bar{\delta}(X, X')$ (see also N.D.E. (54)).

[^N.D.E-III-72]: N.D.E.: This is used in XXIV, 1.13.

[^N.D.E-III-73]: N.D.E.: Indeed, $\operatorname{Aut}_{S_{0}-gr.}(X_{0})$ acts by group automorphisms on the abelian
    group $H^{2}(X_{0}, Lie(X_{0}/S_{0}))$, hence the orbit of `0` is the singleton `{0}`; consequently the quotient set
    is a singleton if and only if $H^{2}(X_{0}, Lie(X_{0}/S_{0})) = {0}$.

[^N.D.E-III-74]: N.D.E.: One has $Coker(j) = B' \sqcup_{Q} 0 = A \sqcup_{A'} 0 = A''$, and one sees that $Ker(j) \simeq
    Ker(i) = 0$ by reasoning "as if $C$ were a category of modules"; for a proof solely in terms of arrows, see for
    example [Fr64], Th. 2.5.4 (∗).

[^N.D.E-III-75]: N.D.E.: In what follows, we have replaced $A$ by $B'$ and detailed the end of the argument.

[^N.D.E-III-76]: N.D.E.: We have rewritten the statement to be exactly in the setting of the application made of it in
    4.3; moreover, we have detailed the proof, following the indications given by M. Demazure.

[^N.D.E-III-77]: N.D.E.: To lighten the statement, we have added here the hypothesis that $G$ be quasi-coherent, and
    deferred to the proof the remark that this hypothesis is automatically satisfied; we have detailed the proof
    accordingly.

[^N.D.E-III-78]: N.D.E.: See also [BAC], § III.5, th. 1.

[^N.D.E-III-79]: N.D.E.: We have detailed what follows and added Corollary 4.3.1. Recall that "pseudo-torsor" is
    synonymous with "formally principal homogeneous".

[^N.D.E-III-80]: N.D.E.: We have added this complement, useful to prove point (ii) of Proposition 4.8.

[^N.D.E-III-81]: N.D.E.: We have added the numbering 4.5.0 to mark the return to the original.

[^N.D.E-III-82]: N.D.E.: We have corrected the following sentence.

[^N.D.E-III-83]: N.D.E.: We have detailed what follows.

[^N.D.E-III-84]: N.D.E.: Here, we have denoted $R^{1}\Gamma(Y_{0}, A_{0})$ the "coherent" cohomology group $H^{1}(Y_{0},
    A_{0})$ of the $O_{Y_{0}}$-module $A_{0}$, in order to distinguish it from the "Hochschild" cohomology groups
    $H^{i}(Y_{0}, M_{0})$ ($Y_{0}$ an $S_{0}$-group, $M_{0}$ an $O_{S_{0}}$-module) which will be considered starting
    from 4.16.

[^N.D.E-III-85]: N.D.E.: We have placed here this remark, which replaces Remark 4.7 of the original.

[^N.D.E-III-86]: N.D.E.: We have corrected "closed subschemes" to "subschemes".

[^N.D.E-III-87]: N.D.E.: We have kept, for the record, Remark 4.6 of the original, in which the definition of "locally
    complete intersection" does not appear. We have added next the "good" definition, drawn from SGA 6, VII 1.4 (which
    replaces that of EGA IV₄, 16.9.2), and the proof of the three results stated in the remark.

[^N.D.E-III-88]: N.D.E.: In order to prove the results stated in Remark 4.6, we have added Lemmas 4.6.3, 4.6.4 and
    Proposition 4.6.5, as well as Remark 4.6.6.

[^N.D.E-III-89]: N.D.E.: We have inserted here this remark, used in the following proposition; it appeared in 4.10 of
    the original.

[^N.D.E-III-90]: N.D.E.: In the original, this was indicated in Remark 4.10, under the additional hypothesis that $Y'$
    was locally complete intersection in $X'$. This hypothesis figured also, consequently, in statements 4.12–4.14; it
    seems in fact superfluous, and we have suppressed it from the above-mentioned statements.

[^N.D.E-III-91]: N.D.E.: We have suppressed the hypothesis that $I$ be nilpotent, which appears superfluous (cf. the
    proof).

[^N.D.E-III-92]: N.D.E.: See also 4.27 further on.

[^N.D.E-III-93]: N.D.E.: See also EGA IV₄, 16.4.21. Recall that if $U$ is an affine open of $X$ such that $Y \cap U$ is
    defined by the ideal $I$ of $A = O_{X}(U)$, if one denotes by $d$ the differential $A \to \Gamma(U,
    \Omega^{1}_{X/S})$, and if $x \in I$, then $D(x + I^{2})$ is the element $d(x) \otimes 1$ of $\Gamma(U,
    \Omega^{1}_{X/S}) \otimes_{A} (A/I)$.

[^N.D.E-III-94]: N.D.E.: We have done these verifications below.

[^N.D.E-III-95]: N.D.E.: On the one hand, we have suppressed the hypothesis that $I$ be nilpotent, i.e. that $X_{0}$
    have the same underlying topological space as $X$; on the other hand, we have detailed the following sentence.

[^N.D.E-III-96]: N.D.E.: We have detailed what follows.

[^N.D.E-III-97]: N.D.E.: We have added what follows.

[^N.D.E-III-98]: N.D.E.: Cf. N.D.E. (93).

[^N.D.E-III-99]: N.D.E.: From 4.17 on, we shall apply this to the case where $X$ is an $S$-group, $g : X \times_{S} X
    \to X$ the multiplication, $Y$ a subscheme of $X$ such that `Y_J` is a subgroup of `X_J`, $Y' = Y \times_{S} Y$, and
    to the two morphisms $Y^{3} \to X^{2}$ which send $(y_{1}, y_{2}, y_{3})$ to $(y_{1}y_{2}, y_{3})$, resp. $(y_{1},
    y_{2}y_{3})$. In this case, the comparison of the above obstructions will show that the obstruction to $Y$ being a
    subgroup of $X$ resides in a certain cohomology group (Hochschild) $H^{2}(Y_{0}, N_{0})$.

[^N.D.E-III-100]: N.D.E.: We have suppressed the hypothesis "$Y_{0}'$ locally complete intersection in $X_{0}'$",
    superfluous by 4.8.0; on the other hand, we have added that $a_{g_{0}}(f_{0})$ is "functorial in $T$", this playing
    a crucial role in the proof of 4.17.

[^N.D.E-III-101]: N.D.E.: We have detailed the proof, to make visible the "functoriality in $T$" of $a_{g_{0}}$.

[^N.D.E-III-102]: N.D.E.: The situation will simplify from 4.16 on: one will restrict to schemes flat over $S$, $Y$ will
    be a flat $S$-group and $Y' = Y \times_{S} Y$; one will then obtain $S_{0}$-functors $N_{0}$ and $N_{0}'$.

[^N.D.E-III-103]: N.D.E.: We have added this remark, used in the proof of 4.17.

[^N.D.E-III-104]: N.D.E.: We have kept the notation of the original, denoting $f : A' \to C$ and $g : A \to A'$ the
    morphisms of rings corresponding to $f : T \to X'$ and $g : X' \to X$. This explains the formula $c(X, Y, g \circ
    f)(\bar{x} \otimes 1) = f(g(x))$, for $x \in I_{Y}$.

[^N.D.E-III-105]: N.D.E.: We have added in the statement the hypothesis that $Y$ be locally of finite presentation over
    $S$, and have given the following proof, more direct than the one sketched in the original. To be complete, let us
    also detail the latter. As in the proof given above, one reduces first to the case where $S =
    \operatorname{Spec}(k)$, $k$ being an algebraically closed field. By [EGA IV₄, 16.9.10](https://jcreinhold.github.io/ega/iv/29-ch4-16-differential-invariants.html#169-regular-and-quasi-regular-immersions) and 19.3.2, it suffices to see
    that, for every $y \in Y$, the completion of the local ring $O_{Y,y}$ is the quotient of a complete noetherian local
    ring by a regular sequence. By loc. cit., 19.3.3, the set of $y \in Y$ satisfying this property is an open $U$ of
    $Y$; since $Y$ is of finite type over $k$, it suffices to show that $U$ contains every closed point. Since $Y$ is a
    $k$-group it suffices, by a translation argument, to show that the property is true for the completion of $O_{Y,e}$,
    that is, for the "formal group" `Ŷ` corresponding to $Y$ (cf. Exp. VII_B). Now, since $X$ is smooth, the affine
    algebra $A(\hat{X})$ is an algebra of formal power series $k[[X_{1}, ..., X_{n}]]$, and one concludes with the help
    of the Dieudonné structure theorem which shows that $A(\hat{Y})$ is isomorphic to a quotient $k[[X_{1}, ...,
    X_{r+s}]]/(X^{p^{n_{1}}}_{1}, ..., X^{p^{n_{r}}}_{r})$, where $p$ is the characteristic exponent of $k$ and $r + s
    \leq n$, cf. VII_B, Remark 5.5.2 (b).

[^N.D.E-III-106]: N.D.E.: We have reorganized 4.16 by regrouping there, on the one hand, the hypotheses stated at the
    end of 4.15 and, on the other hand, the definition of the obstruction `DY`.

[^N.D.E-III-107]: N.D.E.: We have corrected the original by adding "flat".

[^N.D.E-III-108]: N.D.E.: See 4.25 further on.

[^N.D.E-III-109]: N.D.E.: We have modified 4.17 and 4.18 taking into account the additions made in 4.16.

[^N.D.E-III-110]: N.D.E.: In the original, one finds $DY' - DY = -\partial d(Y, Y')$, but their $\partial$ is the
    opposite of the differential $\partial^{1}$ defined in I, 5.1.

[^N.D.E-III-111]: N.D.E.: We have slightly modified the notations, and detailed the beginning of the argument.

[^N.D.E-III-112]: N.D.E.: We have replaced `a, b` by `ab, b` to make visible that $V(P)$ comes by inverse image on
    $Y^{2}_{0}$ from the multiplication morphism $V_{Y_{0}} \times_{S_{0}} V_{Y_{0}} \to V_{Y_{0}}$.

[^N.D.E-III-113]: N.D.E.: We have changed the signs to make them compatible with I 5.1.

[^N.D.E-III-114]: N.D.E.: We have detailed the original in what follows.

[^N.D.E-III-115]: N.D.E.: We have suppressed the hypothesis that $I$ be nilpotent, which appears superfluous.

[^N.D.E-III-116]: N.D.E.: The question of whether the preceding set, modulo conjugation by the $x \in X(S)$ inducing the
    unit of $X(S_{J})$, is principal homogeneous under $H^{1}(Y_{0}, N_{0})$, occupies n°s 4.23 to 4.36.

[^N.D.E-III-117]: N.D.E.: We have corrected $\partial DY'$ to $DY'$.

[^N.D.E-III-118]: N.D.E.: Cf. N.D.E. (110).

[^N.D.E-III-119]: N.D.E.: We have detailed what precedes; this shows that the following isomorphism is valid without
    flatness hypothesis; on the other hand, since 4.16, we have restricted ourselves to $S$-schemes $f : T \to S$ flat
    over $S$ to ensure that the group $\operatorname{Hom}_{O_{T}}(n_{Y_{0}/X_{0}} \otimes_{O_{S_{0}}} O_{T_{0}},
    JO_{T})$, in which the obstruction $c(X, Y, f)$ resides, coincides with $N_{0}(T_{0})$ (cf. the end of 4.16).

[^N.D.E-III-120]: N.D.E.: With the notation of I 5.3, assuming $Y_{0}$ affine over $S_{0}$.

[^N.D.E-III-121]: N.D.E.: We have replaced $Z^{1}(Y_{0}, N_{0})$ by $B^{1}(Y_{0}, N_{0})$, since the proof shows that
    $\Gamma$ is a subgroup of $B^{1}(Y_{0}, N_{0})$, cf. 4.27–4.29.

[^N.D.E-III-122]: N.D.E.: We have detailed the proof, taking into account the additions made in Exp. I, § 6.8.

[^N.D.E-III-123]: N.D.E.: We have detailed the original, to make visible that one has an exact sequence of
    $Y_{0}$-$O_{S_{0}}$-modules.

[^N.D.E-III-124]: N.D.E.: This results from the definition of $d : n_{Y_{0}/X_{0}} \to \Omega^{1}_{X_{0}/S_{0}}$ (cf.
    4.25) and from that of $v_{i_{Y_{0}}}$ (cf. 4.8).

[^N.D.E-III-125]: N.D.E.: We have added point (i) below, which will be useful in 4.35.1 and then in 4.38 (4) and (5).

[^N.D.E-III-126]: N.D.E.: Recall that $L'_{X} = \prod_{S_{0}/S} L^{X}_{0}$.

[^N.D.E-III-127]: N.D.E.: We have corrected $Lie(Y_{0}/S_{0})$ to $\omega^{1}_{Y_{0}/S_{0}}$.

[^N.D.E-III-128]: N.D.E.: We have detailed the original in what follows.

[^N.D.E-III-129]: N.D.E.: We have added the hypothesis on $\omega^{1}_{Y_{0}/S_{0}}$ and replaced the hypothesis "$S$
    affine" by "$S_{0}$ affine".

[^N.D.E-III-130]: N.D.E.: We have added what follows, cf. 4.34.

[^N.D.E-III-131]: N.D.E.: Cf. N.D.E. (129).

[^N.D.E-III-132]: N.D.E.: We have added what follows and Proposition 4.35.1, implicit in the original, cf. 4.38 (5).

[^N.D.E-III-133]: N.D.E.: This also follows from the proof of 4.32.

[^N.D.E-III-134]: N.D.E.: For example, 4.37 is used in Exposé IX to prove statements 3.2 bis and 3.6 bis.

[^N.D.E-III-135]: N.D.E.: We have replaced $\operatorname{Hom}_{O_{S_{0}}}(n_{Y_{0}/X_{0}}, I^{n+1}/I^{n+2})$ by
    $n^{\vee}_{Y_{0}/X_{0}} \otimes_{O_{S_{0}}} I^{n+1}/I^{n+2}$, in accordance with Remark 4.22.

[^N.D.E-III-136]: N.D.E.: We have slightly modified the original in what follows. In particular, we have replaced $X$ by
    $G$ and $Y$ by $K$, and we have denoted $g_{0}$ and $k_{0}$ their Lie algebras. On the other hand, we have written
    explicitly $H^{i}(K_{0}, \cdot)$ instead of the abbreviation $H^{i}(\cdot)$ of the original.

[^N.D.E-III-137]: N.D.E.: Equipped with the adjoint action of $K_{0}$.

[^N.D.E-III-138]: N.D.E.: Since the formation of centralizers and normalizers commutes with base change (cf. I 2.3.3.1),
    we have written $Centr(K_{0})$ instead of $Centr(K)_{0}$ in the original, and similarly $Centr_{G_{0}}(K_{0})$ and
    $Norm_{G_{0}}(K_{0})$ instead of $Centr_{G}(K)_{0}$ and $Norm_{G}(K)_{0}$.

[^N.D.E-III-139]: N.D.E.: And this is the Lie algebra $\operatorname{Der}_{k}(k_{0})$ of derivations of $k_{0}$; hence
    $H^{1}(K_{0}, k_{0})$ is the quotient of $\operatorname{Der}_{k}(k_{0})$ by inner derivations (i.e. by the image of
    $ad : k_{0} \to \operatorname{Der}_{k}(k_{0})$).

[^N.D.E-III-140]: N.D.E.: We have added the following sentence.

[^N.D.E-III-141]: N.D.E.: We have detailed the original in what follows, and in $(\ast\ast)$ we have corrected $u \circ
    i$ to $i \circ u$.

[^N.D.E-III-142]: N.D.E.: We have modified the original in what follows, taking into account the additions made in 3.5.1
    and 4.35.1.

[^N.D.E-III-143]: N.D.E.: Additional references cited in this Exposé.
