# Exposé V. Construction of quotient schemes

<!-- label: III.V -->

*by P. Gabriel*

<!-- original page 251 -->

The aim of this Exposé is to prove the theorems stated in TDTE III.[^N.D.E-V-1] If $X$ and $T$ are two objects of a
category $C$, we write $X(T)$ instead of $\operatorname{Hom}_{C}(T, X)$. Similarly, if $\phi : Y \to X$ is an arrow
(resp. an object $T$) of $C$, then $\phi(T)$ denotes the map $g \mapsto \phi \circ g$ from $Y(T)$ to $X(T)$:

```text
        T
       / \
      g   φ ∘ g
     /     \
    Y ─ φ → X,
```

and $T(\phi)$ denotes the map $g \mapsto g \circ \phi$ from $T(X)$ to $T(Y)$:

```text
    Y ─ φ → X
     \     /
      g ∘ φ   g
       \   /
        T.
```

Finally, if $P$ is a scheme, we write $P$ for the underlying set of $P$.

Exceptionally, in the present Exposé we do not follow the convention stated in IV 4.6.15 on the notation for quotients
(loc. cit., top of page 227 of the original), since we wish to give here a construction of quotients which also applies
to "pre-equivalence relations"[^N.D.E-V-2] that are not equivalence relations.

<!-- original page 252 -->

## 1. $C$-groupoids

<!-- label: III.V.1 -->

**a)** Let $C$ be a category in which products and fiber products exist. Recall first that a diagram

```text
        d₁       p
   X₁ ⇉ X₀ → Y
        d₀
```

in $C$ is said to be *exact* if $p d_{0} = p d_{1}$ and if, for every $T \in C$, $T(p)$ is a bijection of $T(Y)$ onto
the subset of $T(X_{0})$ consisting of arrows $f : X_{0} \to T$ such that $f d_{0} = f d_{1}$. One also says that $(Y,
p)$ is the *cokernel* of $(d_{0}, d_{1})$ and writes

```text
(Y, p) = Coker(d₀, d₁).
```

**b)** Let, for example, $C$ be the category `(Esp.An)` of ringed spaces. In this case, there always exists a cokernel
$(Y, p)$, which can be described as follows: the underlying topological space of $Y$ is obtained from $X_{0}$ by
identifying the points $d_{0}(x)$ and $d_{1}(x)$ and endowing $Y$ with the quotient topology. The canonical map $\pi :
X_{0} \to Y$ together with $d_{0}, d_{1}$ then induces a double arrow of sheaves of rings on $Y$:

```text
                       δ₀
    π_∗(O₀) ⇉ π_∗(d_{0∗} O₁) = π_∗(d_{1∗} O₁),
                       δ₁
```

where $O_{i}$ is the structure sheaf of $X_{i}$. We choose for the sheaf of rings on $Y$ the subsheaf of
$\pi_{\ast}(O_{0})$ whose sections $s$ satisfy $\delta_{0}(s) = \delta_{1}(s)$. The arrow $p$ is defined in the evident
way.

Let[^N.D.E-V-3] `X₁ ⇉ X₀` be a diagram (with arrows $d_{0}, d_{1}$) in `(Esp.An)` and let $(Y, p)$ be its cokernel. We
say that an open set $U$ of $X_{0}$ is *saturated* if $d^{-1}_{0}(U) = d^{-1}_{1}(U)$, which is equivalent to saying
that $U = p^{-1}(p(U))$. In this case, since $Y$ is endowed with the quotient topology, $p(U)$ is an open subset of $Y$.

**Lemma 1.1.** *Let $U$ be a saturated open set of $X$ and $V = p(U)$. If we denote by $U_{1}$ the open set
$d^{-1}_{0}(U) = d^{-1}_{1}(U)$ of $X_{1}$, and by $\tilde{d}_{0}$, $\tilde{d}_{1}$, and $\tilde{p}$ the restrictions of
$d_{0}, d_{1}$ to $U_{1}$, and of $p$ to $U$, then $(V, \tilde{p})$ is a cokernel in `(Esp.An)` of:*[^N.D.E-V-4]

<!-- label: III.V.1.1 -->

```text
         d̃₁      p̃
   U₁ ⇉ U → V.
         d̃₀
```

The verification is straightforward.

**Lemma 1.2.** *Let `X₁ ⇉ X₀` be a diagram in `(Sch)` (with arrows $d_{0}, d_{1}$) and let $(Y, p)$ be its cokernel in
`(Esp.An)`.*

<!-- label: III.V.1.2 -->

*(i) If $Y$ is a scheme and $p$ a morphism of schemes, then $(Y, p)$ is a cokernel of $(d_{0}, d_{1})$ in `(Sch)`.*

*(ii) Suppose that every point of $X_{0}$ possesses a saturated open neighborhood $U$ such that, denoting by
$\tilde{d}_{0}$ and $\tilde{d}_{1}$ the restrictions of $d_{0}$ and $d_{1}$ to $d^{-1}_{0}(U) = d^{-1}_{1}(U)$, and by
$(Q, q)$ the cokernel of $(\tilde{d}_{0}, \tilde{d}_{1})$ in `(Esp.An)`, the space $Q$ is a scheme and $q$ a morphism of
schemes. Then $(Y, p)$ is a cokernel of $(d_{0}, d_{1})$ in `(Sch)`.*

(i) is proved in § 4.c); since the proof is short, let us repeat it here. Let $f : X_{0} \to Z$ be a morphism of schemes
such that $f d_{0} = f d_{1}$. By hypothesis, there is a unique morphism of ringed spaces $r : Y \to Z$ such that $f = r
p$. It remains to show that, for every $y \in Y$, the homomorphism $O_{r(y)} \to O_{y}$ induced by $r$ is local. This
follows from the fact that $p$ is surjective, so that $y$ is of the form $p(x)$, and from the fact that the homomorphism
$O_{f(x)} \to O_{x}$ induced by $f$ is local.

(ii) follows from (i) and the preceding lemma.

<!-- original page 253 -->

**c)** In this Exposé we study the existence of $Coker(d_{0}, d_{1})$ when the double arrow $(d_{0}, d_{1})$ is inserted
in a richer context; more precisely, let $X_{2} = X_{1} \times_{d_{1}, d_{0}} X_{1}$ denote the fiber product of the
diagram

$$ X_{1} \downarrow d_{1} (\ast) X_{0} \uparrow d_{0} X_{1}, $$

and let $d'_{0}$ and $d'_{2}$ be the two canonical projections of $X_{2}$ onto $X_{1}$; one then has by definition a
Cartesian square

```text
                  d′₀
            X₂ ─────→ X₁
            │          │
        d′₂ │          │ d₁
            ↓          ↓
            X₁ ─────→ X₀.
                  d₀
(0)
```

Moreover, let us give ourselves a third arrow $d'_{1} : X_{2} \to X_{1}$; we say that `(d₀, d₁ : X₁ ⇉ X₀, d′₁)` is a
$C$-*groupoid* if for every object $T$ of $C$, $X_{1}(T)$ is the set of arrows of a groupoid $X\ast(T)$ whose set of
objects is $X_{0}(T)$, with source map $d_{1}(T)$, target map $d_{0}(T)$, and composition map $d'_{1}(T)$ (one
identifies, as usual, $(X_{1} \times_{d_{1}, d_{0}} X_{1})(T)$ with $X_{1}(T) \times_{d_{1}(T), d_{0}(T)} X_{1}(T)$; we
also recall that a groupoid is a category in which every arrow is invertible).[^N.D.E-V-5]

If $\phi$ is an arrow of the groupoid $X\ast(T)$, the map $f \mapsto \phi \circ f$ is a bijection from the set of arrows
$f$ whose target coincides with the source of $\phi$ onto the set of arrows having the same target as $\phi$. One sees
easily that this fact can be translated by saying that the square

```text
                  d′₁
            X₂ ─────→ X₁
            │          │
        d′₀ │          │ d₀
            ↓          ↓
            X₁ ─────→ X₀
                  d₀
(1)
```

is Cartesian.

Similarly, the map $g \mapsto g \circ \phi$ is a bijection from the set of arrows $g$ of $X\ast(T)$ having source equal
to the target of $\phi$ onto the set of arrows having the same source as $\phi$. This fact can again be translated by
saying that the square

```text
                  d′₁
            X₂ ─────→ X₁
            │          │
        d′₂ │          │ d₁
            ↓          ↓
            X₁ ─────→ X₀
                  d₁
(2)
```

is Cartesian.

<!-- original page 254 -->

On the other hand, let $s : X_{0} \to X_{1}$ be the unique arrow of $C$ such that, for every $T$, $s(T) : X_{0}(T) \to
X_{1}(T)$ associates to every object of $X\ast(T)$ the identity arrow of that object.[^N.D.E-V-6] The arrow $s$
satisfies the equalities

```text
(3)        d₁ s = id_{X₀},
(3 bis)    d₀ s = id_{X₀}.
```

Finally, the associativity of the composition maps $d'_{1}(T)$ translates into the commutativity of the diagram

```text
                              d′₁ × X₁
   X₁ ×_{d₁, d₀} X₁ ×_{d₁, d₀} X₁ ─────────→ X₁ ×_{d₁, d₀} X₁
            │                                       │
   X₁ × d′₁ │                                       │ d′₁
            ↓                                       ↓
   X₁ ×_{d₁, d₀} X₁ ──────────d′₁──────────────→ X₁.
(4)
```

Conversely, the conditions (1), (2), and (4) together with the existence of an arrow $s$ satisfying (3) imply that
`(X₁ ⇉ X₀, d′₁)` is a $C$-groupoid. The condition (3) is harmless; it merely ensures that the map $d_{1}(T) : X_{1}(T)
\to X_{0}(T)$ is surjective for every $T \in C$. In what follows we shall mostly make use of the Cartesian squares (0),
(1) and (2), which we summarize in the diagram

```text
                  d′₁              d₀
            X₂  ────→  X₁  ──────→  X₀
                  d′₀
        d′₂ │           │ d₁
            ↓           ↓
            X₁  ────→  X₀
                  d₀
(0,1,2)
```

In this diagram the two left-hand squares (i.e. the squares (0) and (2)) are Cartesian; the first row is exact, and
$X_{2}$ is identified with the fiber product $X_{1} \times_{d_{0}, d_{0}} X_{1}$.

We use associativity only indirectly, for instance to ensure the existence of an arrow $s$ satisfying (3) and (3 bis),
or else to ensure the existence of an arrow

```text
(†)   σ : X₁ → X₁    such that    d₀ σ = d₁    and    d₁ σ = d₀
```

(one chooses $\sigma$ so that $\sigma(T) : X_{1}(T) \to X_{1}(T)$ sends every arrow of $X\ast(T)$ to its
inverse).[^N.D.E-V-7]

By abuse of language, we shall sometimes call a $C$-*groupoid* a diagram

```text
        d′₀, d′₁, d′₂      d₀, d₁
   X₂ ⇶ X₁ ⇉ X₀
```

such that (0), (1) and (2) are Cartesian, (4) is commutative, and there exists $s$ satisfying (3). The object $X_{2}$
will therefore be allowed to be "a" fiber product of (∗) without being "the" fiber product of (∗).[^N.D.E-V-8]

**Terminology.** Instead of $C$-groupoid $X\ast$, we shall also speak of the *groupoid $X\ast$ with base $X_{0}$*, or of
the *pre-equivalence relation $X\ast$ in $X_{0}$*.

<!-- original page 255 -->

## 2. Examples of $C$-groupoids

<!-- label: III.V.2 -->

**a)** Let $X$ be an object of $C$ and $G$ a $C$-group acting on the left on $X$. We denote by $d_{0} : G \times X \to
X$ the arrow defining the action of $G$ on $X$, by $d_{1} : G \times X \to X$ the projection of the product onto the
second factor, by $\mu : G \times G \to G$ the arrow defining the $C$-group structure of $G$, and finally by $pr_{2,3}$
the projection of $G \times G \times X = G \times (G \times X)$ onto the second factor. Then

```text
                  pr_{2,3}              d₁
   G × G × X      ⇉      G × X         ⇉   X
                  μ × X                 d₀
                  G × d₀
```

<!-- original page 256 -->

is a $C$-groupoid.

**b)** Let $d_{0}, d_{1} : X_{1} \to X_{0}$ be an *equivalence pair*, i.e., if $d_{0} \boxtimes d_{1} : X_{1} \to X_{0}
\times X_{0}$ is the arrow with components $d_{0}$ and $d_{1}$, we suppose that $(d_{0} \boxtimes d_{1})(T)$ is, for
every object $T$ of $C$, a bijection of $X_{1}(T)$ onto the graph of an equivalence relation on $X_{0}(T)$. The set
$X_{1}(T)$ therefore identifies with the set of pairs $(x, y)$ of elements of $X_{0}(T)$ such that $x \sim y$;
similarly, the set $X_{2}(T) = (X_{1} \times_{d_{1}, d_{0}} X_{1})(T)$ identifies with the set of triples $(x, y, z)$ of
elements of $X_{0}(T)$ such that $x \sim y$ and $y \sim z$. There is therefore one and only one arrow $d'_{1} : X_{2}
\to X_{1}$ making the squares (1) and (2) commute: $d'_{1}(T)$ must send $(x, y, z) \in X_{2}(T)$ to $(x, z) \in
X_{1}(T)$. For this choice of $d'_{1}$, `(d₀, d₁ : X₁ ⇉ X₀, d′₁)` is a $C$-groupoid.

Conversely, consider a $C$-groupoid $X\ast$ such that $d_{0} \boxtimes d_{1} : X_{1} \to X_{0} \times X_{0}$ is a
monomorphism. Then $(d_{0}, d_{1})$ is an equivalence pair and $X\ast$ can be reconstructed from $(d_{0}, d_{1})$ as
explained a few lines above.[^N.D.E-V-9]

**c)** If $p : X \to Y$ is any arrow of $C$ and if $pr_{1}$ and $pr_{2}$ are the two projections of $X \times_{p, p} X$
onto $X$, then `(pr₁, pr₂) : X ×_{p, p} X ⇉ X` is an equivalence pair. One says that $p$ is an *effective epimorphism*
if the diagram

```text
                  pr₁           p
   X ×_{p, p} X  ⇉  X  ────→  Y
                  pr₂
```

is exact, that is, if $(Y, p) = Coker(pr_{1}, pr_{2})$.

Let, for example, $S$ be a Noetherian scheme and let $C$ be the category of schemes finite over $S$. Let us show that an
epimorphism in $C$ is not necessarily effective: take $S$ equal to $\operatorname{Spec} k[T^{3}, T^{5}]$, where $k$ is a
commutative field, $Y$ equal to $S$, and $X$ equal to $\operatorname{Spec} k[T]$. If $i$ is the inclusion of $B =
k[T^{3}, T^{5}]$ into $A = k[T]$, take $p$ equal to $\operatorname{Spec} i$. In this case $X \times_{p, p} X$ identifies
with $\operatorname{Spec}(A \otimes_{B} A)$ and $Coker(pr_{1}, pr_{2})$ with $\operatorname{Spec} B'$, where $B'$ is the
subring of $A$ consisting of $a$ such that $a \otimes_{B} 1 = 1 \otimes_{B} a$. Now

<!-- original page 257 -->

```text
T⁷ ⊗_B 1 = (T² T⁵) ⊗_B 1 = T² ⊗_B T⁵ = T² ⊗_B (T³ T²) = T⁵ ⊗_B T² = 1 ⊗_B T⁷.
```

So $T^{7}$ belongs to $B'$, does not belong to $B$, and $\operatorname{Spec} B'$ is distinct from $\operatorname{Spec}
B$, which yields the counterexample.[^N.D.E-V-10]

## 3. Some sorites on $C$-groupoids

<!-- label: III.V.3 -->

Here, in no particular order, are some remarks used in what follows:

**a)** Let

```text
        d′₀, d′₁, d′₂      d₀, d₁
   X₂ ⇶ X₁ ⇉ X₀
```

be a $C$-groupoid and $f_{0} : Y_{0} \to X_{0}$ an arrow of $C$. We shall define a $C$-groupoid with base $Y_{0}$

```text
        e′₀, e′₁, e′₂      e₀, e₁
   Y₂ ⇶ Y₁ ⇉ Y₀
```

which we shall call *induced by $X\ast$ and $f_{0}$*. One also says that $Y\ast$ is the *inverse image of $X\ast$ under
the base change $f_{0}$*.

We choose for $Y_{1}$ the fiber product of the diagram

```text
                 f₁
   Y₁ ─────────→ X₁
   │              │
   │              │ d₀ ⊠ d₁
   ↓              ↓
   Y₀ × Y₀ ────→ X₀ × X₀,
        f₀ × f₀
```

and for $e_{0}$ and $e_{1}$ the arrows obtained by composing the canonical arrow $Y_{1} \to Y_{0} \times Y_{0}$ with the
first and second projections of $Y_{0} \times Y_{0}$. The morphism $Y_{1} \to Y_{0} \times Y_{0}$ is then $e_{0}
\boxtimes e_{1}$, and one has $f_{0} \circ e_{i} = d_{i} \circ f_{1}$ for $i = 0, 1$, where we have written $f_{1}$ for
the projection of $Y_{1}$ onto $X_{1}$.

<!-- original page 258 -->

We set $Y_{2} = Y_{1} \times_{e_{0}, e_{1}} Y_{1}$, cf. 1.c). One can say that the pair $(e_{0}, e_{1})$ is defined in
such a way that, for every $T \in C$ and every pair $(y, x)$ of elements of $Y_{0}(T)$, there is a certain one-to-one
correspondence $\psi \mapsto {}_{y} \psi_{x}$ between the arrows $\psi$ of $X\ast(T)$ with source $f_{0}(x)$ and target
$f_{0}(y)$ and the arrows ${}_{y} \psi_{x}$ of $Y\ast(T)$ with source $x$ and target $y$. One therefore determines
$e'_{1} : Y_{2} \to Y_{1}$ by defining, for every $T \in C$, the composition of arrows of $Y\ast(T)$ by the formula

```text
   _z ψ_y ∘ _y φ_x = _z (ψ ∘ φ)_x.
```

It is clear that this definition makes each $Y\ast(T)$ into a groupoid.

**b)** Knowing the $C$-groupoid $X\ast$ and the base change $f_{0} : Y_{0} \to X_{0}$, one can reconstruct the pair
`(e₀, e₁) : Y₁ ⇉ Y₀` in another way:[^N.D.E-V-11] construct $Y_{0} \times_{X_{0}} X_{1}$, $pr_{1}$ and $pr_{2}$ so that
the square

```text
                       pr₂
   Y₀ ×_{X₀} X₁ ─────→ X₁
        │              │
    pr₁ │              │ d₀
        ↓              ↓
        Y₀ ──────────→ X₀
                  f₀
```

is Cartesian. One then verifies without difficulty, by reduction to the set-theoretic case, that one has the Cartesian
square

```text
              e₀ ⊠ f₁
   Y₁ ─────────────→ Y₀ ×_{X₀} X₁
   │                       │
e₁ │                       │ d₁ ∘ pr₂
   ↓                       ↓
   Y₀ ────────────────→ X₀,
              f₀
```

where $f_{1}$ denotes the canonical projection of $Y_{1} = (Y_{0} \times Y_{0}) \times_{(X_{0} \times X_{0})} X_{1}$
onto $X_{1}$.

<!-- original page 259 -->

**c)** We shall give two examples of inverse images of a $C$-groupoid. Take $Y_{0}$ equal to $X_{1}$, $f_{0}$ equal to
$d_{0}$. For every object $T$ of $C$, $Y_{1}(T)$ then identifies with the set of diagrams of the form

```text
        φ
   b ────→ d
   ↑        ↑
   f        g
   │        │
   a        c
```

of $X\ast(T)$. The source of such a diagram is the arrow $f$, the target is the arrow $g$. These diagrams compose in the
evident way.

Now put $Y'_{0} = X_{1}$, $f'_{0} = d_{1}$ (we add the primes[^N.D.E-V-12] to avoid any confusion with the preceding
example). In this case, $Y'_{1}(T)$ identifies, for every $T \in C$, with the set of diagrams of the form

```text
   b        d
   ↑        ↑
   f        g
   │   ψ   │
   a ────→ c
```

of the groupoid $X\ast(T)$. The source of such a diagram is $f$, the target is $g$; the composition of these diagrams is
evident.

This being so, it is clear that the identity map of $Y_{0}(T)$ and the map

```text
        φ                       
   b ────→ d           b        d
   ↑        ↑          ↑        ↑
   f        g    ↦     f        g
   │        │          │  g⁻¹φf │
   a        c          a ─────→ c
```

from $Y_{1}(T)$ to $Y'_{1}(T)$ define an isomorphism of the groupoid $Y\ast(T)$ onto $Y'\ast(T)$. Moreover, this
isomorphism depends functorially on $T$, so that the $C$-groupoids $Y\ast$ and $Y'\ast$ are isomorphic.[^N.D.E-V-13]

<!-- original page 260 -->

**d)**

**Proposition 3.1.** *We keep the notations of a) and assume that $f_{0}$ is an effective and universal epimorphism.
Then $Coker(d_{0}, d_{1})$ exists if and only if $Coker(e_{0}, e_{1})$ exists.*[^N.D.E-V-14] *Moreover, in that case,
$f_{0}$ induces an isomorphism*

<!-- label: III.V.3.1 -->

```text
   Coker(d₀, d₁) ⥲ Coker(e₀, e₁).
```

Let us first recall that an epimorphism $f_{0} : Y_{0} \to X_{0}$ is said to be *universal* if, for every Cartesian
square

```text
   Y′ ─────→ Y₀
   │         │
f′ │         │ f₀
   ↓         ↓
   X′ ─────→ X₀,
```

$f'$ is an epimorphism. This being so, let us denote by $C(d_{0}, d_{1})$ the covariant functor from $C$ to sets which
associates to every $T \in C$ the kernel of the pair `T(d₀), T(d₁) : T(X₀) ⇉ T(X₁)`. We define $C(e_{0}, e_{1})$
similarly. For every $T \in C$, one therefore has a commutative diagram

```text
                           T(d₁)
   C(d₀, d₁)(T) ────→ T(X₀) ⇉ T(X₁)
                           T(d₀)
        │                  │           │
   T(f) │           T(f₀) │           │ T(f₁)
        ↓                  ↓           ↓
                           T(e₁)
   C(e₀, e₁)(T) ────→ T(Y₀) ⇉ T(Y₁),
                           T(e₀)
```

where $T(f)$ is the injection induced by the injection $T(f_{0})$. If we show that $T(f)$ is a surjection for every $T$,
we shall have a functorial isomorphism $f : C(d_{0}, d_{1}) \xrightarrow{\sim} C(e_{0}, e_{1})$, so that the
representability of one of these functors will be equivalent to that of the other; this will prove our proposition.

To prove the surjectivity of $T(f)$, consider the diagram

```text
                          f₁
              Y₁ ─────────────→ X₁
            ↗  
        Δ ↗  e₀ │ e₁          d₀ │ d₁
         ↗      ↓                ↓
   Y₀ ×_{X₀} Y₀ ─────→ Y₀ ─────→ X₀,
                   pr₂      f₀
              pr₁
```

<!-- original page 261 -->

where $\Delta$ is the section of $Y_{1} \to Y_{0} \times Y_{0}$ defined by the morphism $s \circ f_{0} \circ pr_{1} :
Y_{0} \times Y_{0} \to X_{1}$, with $s : X_{0} \to X_{1}$ the arrow satisfying equalities (3) and (3 bis) of section 1.

If the arrow $g : Y_{0} \to T$ is such that $g \circ e_{0} = g \circ e_{1}$, then $g \circ e_{0} \circ \Delta = g \circ
e_{1} \circ \Delta$, so $g \circ pr_{1} = g \circ pr_{2}$. Since $f_{0}$ is an effective epimorphism, $g$ factors
through $f_{0}$ and an arrow $h : X_{0} \to T$, that is to say $g = T(f_{0})(h)$. It remains to show that $h$ belongs to
$C(d_{0}, d_{1})(T)$, i.e. satisfies $h d_{0} = h d_{1}$; now one has

```text
   h d₀ f₁ = h f₀ e₀ = g e₀ = g e₁ = h f₀ e₁ = h d₁ f₁,
```

whence the desired equality, since $f_{1}$ is an epimorphism (because $f_{0}$ is a universal epimorphism).

**e)** Consider now a scheme $S$ and choose $C$ equal to $(Sch/S)$. The data of a $C$-groupoid

```text
        d′₀, d′₁, d′₂      d₀, d₁
   X₂ ⇶ X₁ ⇉ X₀
```

allows one to define an equivalence relation on the set $X_{0}$ underlying the scheme $X_{0}$: if $x, y \in X_{0}$, one
writes $x \sim y$ when there exists $z \in X_{1}$ such that $x = d_{1} z$ and $y = d_{0} z$. The reflexivity and
symmetry of this relation are evident;[^N.D.E-V-15] let us prove transitivity: if $x \sim y$ and $y \sim z$, there exist
$u, v \in X_{1}$ with $x = d_{1} u$, $y = d_{0} u$, $y = d_{1} v$, $z = d_{0} v$. It follows that $(v, u)$ belongs to
the set-theoretic fiber product $X_{1} \times_{d_{1}, d_{0}} X_{1}$. Since the canonical map

<!-- original page 262 -->

```text
   X₁ ×_{d₁, d₀} X₁ ⟶ X₁ ×_{d₁, d₀} X₁
```

from the set underlying the fiber product into the fiber product of the underlying sets is surjective, $(v, u)$ is the
image of some $w \in X_{2}$. One then has $x = d_{1} d'_{1} w$ and $z = d_{0} d'_{1} w$, whence $x \sim z$.

**f)** We keep the notations of a) and b), $C$ still being $(Sch/S)$. If `x, y` are points of $Y_{0}$, we shall see that
one has $x \sim y$ if and only if $f_{0}(x) \sim f_{0}(y)$ (the inverse image of the equivalence relation defined by a
groupoid is the equivalence relation defined by the inverse image of the groupoid).

Indeed, suppose $x \sim y$. There exists therefore $z \in Y_{1}$ such that $x = e_{1}(z)$ and $y = e_{0}(z)$. Since
$f_{0} \circ e_{i} = d_{i} \circ f_{1}$ for $i = 0, 1$, one then has $f_{0}(x) = d_{1} f_{1}(z)$ and $f_{0}(y) = d_{0}
f_{1}(z)$, whence $f_{0}(x) \sim f_{0}(y)$.

Conversely, suppose $f_{0}(x) \sim f_{0}(y)$ and let $z \in X_{1}$ be such that $f_{0}(y) = d_{1}(z)$ and $f_{0}(x) =
d_{0}(z)$. Using the construction and notations of b), there is then a point $t$ of $Y_{0} \times_{X_{0}} X_{1}$ such
that $pr_{1}(t) = x$ and $pr_{2}(t) = z$. Similarly, since $f_{0}(y) = d_{1} pr_{2}(t)$, there is $s \in Y_{1}$ such
that $y = e_{1}(s)$ and $(e_{0} \boxtimes f_{1})(s) = t$. One then has $e_{0}(s) = pr_{1}(e_{0} \boxtimes f_{1})(s) =
pr_{1}(t) = x$. Whence $x \sim y$.

<!-- original page 261 -->

## 4. Passage to the quotient by a finite and flat groupoid (proof of a particular case)

<!-- label: III.V.4 -->

**Theorem 4.1.** *Consider a $(Sch/S)$-groupoid*

<!-- label: III.V.4.1 -->

```text
        d′₀, d′₁, d′₂      d₀, d₁
   X₂ ⇶ X₁ ⇉ X₀.
```

*Suppose the following conditions are satisfied:*[^N.D.E-V-16]

<!-- original page 263 -->

*a) $d_{1}$ is finite locally free;*

*b) for every $x \in X_{0}$, the set $d_{0} d^{-1}_{1}(x)$ is contained in an affine open of $X_{0}$.*[^N.D.E-V-17]

*Then:*

*(i) There exists a cokernel $(Y, p)$ of $(d_{0}, d_{1})$ in $(Sch/S)$; moreover, such a $(Y, p)$ is a cokernel of
$(d_{0}, d_{1})$ in the category of all ringed spaces.*

*(ii) $p$ is integral and open, and $Y$ is affine if $X_{0}$ is affine.*[^N.D.E-V-18]

*(iii) The morphism $X_{1} \to X_{0} \times_{Y} X_{0}$ with components $d_{0}$ and $d_{1}$ is surjective.*

*(iv) If $(d_{0}, d_{1})$ is an equivalence pair, then $X_{1} \to X_{0} \times_{Y} X_{0}$ is an
isomorphism*[^N.D.E-V-19] *and $p : X_{0} \to Y$ is finite locally free.*[^N.D.E-V-20] *Moreover, $(Y, p)$ is a cokernel
of $(d_{0}, d_{1})$ in the category of sheaves for the (fppf) topology and, for every base change $Y' \to Y$, $Y'$ is
the cokernel of the groupoid $X\ast \times_{Y} Y'$ obtained from $X\ast$ by the base change $X_{0} \times_{Y} Y' \to
X_{0}$.*

*In particular, for every base change $S' \to S$, $Y' = Y \times_{S} S'$ is the cokernel of the $S'$-groupoid $X'\ast =
X\ast \times_{S} S'$. So, in this case, "the formation of the quotient commutes with base change".*

It evidently follows from (i) that the topological space underlying $Y$ is the quotient of the topological space
underlying $X_{0}$ by the equivalence relation defined by the $(Sch/S)$-groupoid $X\ast$.

We shall first prove this theorem when $X_{0}$ is affine and $d_{1}$ is locally free of constant rank $n$. We shall see
next how to reduce to this particular case.

<!-- original page 262 -->

In the case in which we have placed ourselves, $X_{0}$, $X_{1}$ and $X_{2}$ are affine. We can therefore suppose that

```text
   X_i = Spec A_i,   d_j = Spec δ_j,   d′_k = Spec δ′_k,
```

the $A_{i}$ being commutative rings and the $\delta_{j}$, $\delta'_{k}$ ring homomorphisms. One can then replace the
diagram (0, 1, 2) by the following

```text
                    δ′₁
            A₂ ⇇ A₁ ⇇ A₀
                    δ′₀         δ₀
   (0,1,2)∗   δ′₂        δ₁
                    δ₁
            A₁ ⇇ A₀,
                    δ₀
```

where the two left-hand squares are cocartesian.

Let $B$ denote the subring of $A_{0}$ consisting of those $a \in A_{0}$ such that $\delta_{0}(a) = \delta_{1}(a)$.

<!-- original page 264 -->

**a)** Let us show that $A_{0}$ is integral over $B$. If $a$ belongs to $A_{0}$, let

```text
   P_{δ₁}(T, δ₀(a)) = Tⁿ − σ₁ T^{n−1} + ⋯ + (−1)ⁿ σ_n
```

be the characteristic polynomial of $\delta_{0}(a)$ when $A_{1}$ is regarded as an algebra over $A_{0}$ via the
homomorphism $\delta_{1}$ (cf. Bourbaki, Alg. VIII, § 12 and Alg. comm. II, § 5, exercise 9). Since the left-hand
squares of $(0,1,2)\ast$ are cocartesian, one has

```text
   δ₀(P_{δ₁}(T, δ₀(a))) = P_{δ′₂}(T, δ′₀ δ₀(a))
```

and

```text
   δ₁(P_{δ₁}(T, δ₀(a))) = P_{δ′₂}(T, δ′₁ δ₀(a)).
```

Since $\delta'_{0} \delta_{0} = \delta'_{1} \delta_{0}$, one has

```text
   δ₀(P_{δ₁}(T, δ₀(a))) = δ₁(P_{δ₁}(T, δ₀(a))),
```

that is, $\delta_{0}(\sigma_{i}) = \delta_{1}(\sigma_{i})$ for every $i$. Hamilton–Cayley moreover tells us that

```text
   δ₀(a)ⁿ − δ₁(σ₁) δ₀(a)^{n−1} + ⋯ + (−1)ⁿ δ₁(σ_n) = 0.
```

Since $\delta_{1}(\sigma_{i}) = \delta_{0}(\sigma_{i})$, one also has

```text
   δ₀(a)ⁿ − δ₀(σ₁) δ₀(a)^{n−1} + ⋯ + (−1)ⁿ δ₀(σ_n) = 0,
```

whence

```text
   aⁿ − σ₁ a^{n−1} + ⋯ + (−1)ⁿ σ_n = 0,
```

<!-- original page 265 -->

since there exists a homomorphism $\tau : A_{1} \to A_{0}$ such that $\tau \delta_{0} = id_{A_{0}}$, hence $\delta_{0}$
is injective. It follows that $A_{0}$ is integral over $B$.

**b)** Consider now two prime ideals $x$ and $y$ of $A_{0}$. We shall show that the equality $x \cap B = y \cap B$
entails the existence of a prime ideal $z$ of $A_{1}$ such that $x = d_{0}(z)$ and $y = d_{1}(z)$.

Indeed, if the assertion were not true, $x$ would be distinct from $\delta^{-1}_{0}(t)$ for every prime ideal $t$ of
$A_{1}$ such that $\delta^{-1}_{1}(t) = y$. For such a $t$ one would have $\delta^{-1}_{0}(t) \cap B =
\delta^{-1}_{1}(t) \cap B = y \cap B = x \cap B$, whence by Cohen–Seidenberg (cf. Bourbaki, Alg. comm. V, § 2, cor. 1 of
prop. 1) $x$ would be contained in no $\delta^{-1}_{0}(t)$.[^N.D.E-V-21] Now there are at most $n$ prime ideals $t$ of
$A_{1}$ such that $\delta^{-1}_{1}(t) = y$ (cf. loc. cit., prop. 3), so, by the "Prime Avoidance Lemma" (loc. cit., II,
§ 1, prop. 3), there would exist $a \in x$ belonging to no $\delta^{-1}_{0}(t)$. Consequently, $\delta_{0}(a)$ would
belong to none of these ideals $t$, and so, by the lemma below, the norm $N_{\delta_{1}}(\delta_{0}(a))$ would not
belong to $y$ (one computes this norm by regarding $A_{1}$ as an algebra over $A_{0}$ via the homomorphism $\delta_{1}$;
one has $N_{\delta_{1}}(\delta_{0}(a)) = \sigma_{n}$ with the notations of a)). But, since $(-1)^{n-1} \sigma_{n} =
a^{n} + \sum^{n-1}_{i=1} (-1)^{i} \sigma_{i} a^{n-i}$, this norm belongs to $B \cap x = B \cap y$, whence the
contradiction.

**Lemma 4.1.1.** *Let $A \to A'$ be a morphism of commutative rings making $A'$ into a projective $A$-module of rank
$n$. Let $p \in \operatorname{Spec}(A)$, $q_{1}, \cdots, q_{r}$ the elements of $\operatorname{Spec}(A')$ above $p$, and
$a \in A'$. Then $a$ belongs to $q_{1} \cup \cdots \cup q_{r}$ if and only if its norm $N(a)$ belongs to $p$.*

<!-- label: III.V.4.1.1 -->

Indeed, replacing $A$ and $A'$ by the localizations $A_{p}$ and $A'_{p}$, we reduce to the case where $(A, p)$ is local
and $A'$ is semilocal, with $\operatorname{Spec}(A') = {q_{1}, \cdots, q_{r}}$. In this case, $A'$ is a free $A$-module
of rank $n$ (cf. Bourbaki, Alg. comm. II, § 3.2, cor. 2 of prop. 5), and $N(a)$ is the determinant of the endomorphism
$\ell_{a} : a' \mapsto a a'$ of $A'$, so one has the equivalences

```text
   N(a) ∉ p ⟺ N(a) invertible ⟺ ℓ_a invertible ⟺ a ∉ q₁ ∪ ⋯ ∪ q_r.
```

**c)** Proof of (i):

Set $Y = \operatorname{Spec} B$ and $p = \operatorname{Spec} i$, where $i$ is the inclusion of $B$ into $A_{0}$. By a),
the morphism $p : X_{0} \to Y$ is surjective. Let us first show that $(Y, p)$ is a cokernel of $(d_{0}, d_{1})$ in the
category of all ringed spaces: it follows indeed from b) that the set underlying $\operatorname{Spec} B$ is obtained
from the set underlying $X_{0}$ by identifying the points $x$ and $y$ such that there exists $z \in X_{1}$ with $d_{1} z
= y$, $d_{0} z = x$. Moreover, since $i$ is integral, $p = \operatorname{Spec} i$ is closed, so $Y$ is endowed with the
quotient topology of that of $X_{0}$. It follows that $p$ is open. Indeed, let $U'$ be any open of $X_{0}$; since
$d_{1}$ is surjective and finite locally free, hence faithfully flat and of finite presentation, and therefore open, the
saturation $U = d_{1}(d^{-1}_{0}(U'))$ of $U'$ for the equivalence relation defined by $X\ast$ is open. Then $p(U') =
p(U)$ is open, since $Y$ is endowed with the quotient topology.

It follows finally from the choice of $B$ and from the fact that $p$, $d_{0}$ and $d_{1}$ are affine that the canonical
sequence of sheaves of rings

<!-- original page 266 -->

```text
                       p_∗(δ₁)
   O_Y ────→ p_∗(O_{X₀}) ⇉ p_∗(d_{0∗}(O_{X₁})) = p_∗(d_{1∗}(O_{X₁}))
                       p_∗(δ₀)
```

is exact.

It remains to show that $(Y, p)$ is also the cokernel of $(d_{0}, d_{1})$ in the category of schemes (more generally, in
the category of ringed spaces in local rings). Let then $q : X_{0} \to Z$ be a morphism of schemes such that $q d_{0} =
q d_{1}$. By what precedes, there is a unique morphism of ringed spaces $r : Y \to Z$ such that $q = r p$. It remains to
show that, for every $y \in Y$, the homomorphism $O_{r(y)} \to O_{y}$ induced by $r$ is local. This follows from the
fact that $p$ is surjective, so that $y$ is of the form $p(x)$, and from the fact that the homomorphism $O_{q(x)} \to
O_{x}$ induced by $q$ is local.

**d)** Proof of (ii): Follows from a) and c).

**e)** Proof of (iii):

Recall that one denotes by $P$ the set underlying a scheme $P$, and by $d : P \to Q$ the map induced by a morphism $d :
P \to Q$.

**Lemma 4.1.2.**[^N.D.E-V-22] *Let $(A, m)$ be a local ring, $k$ its residue field, and $K$ an extension of the field
$k$. Then there exists a local and flat $A$-algebra $B$ such that $B/mB$ is $k$-isomorphic to $K$; moreover, one can
choose $B$ finite and free over $A$ if $K$ is of finite degree over $k$.*

<!-- label: III.V.4.1.2 -->

This is proved in EGA 0_III, 10.3.1, where it is moreover shown that one can choose $B$ Noetherian if $A$ is. For the
reader's convenience, let us indicate the proof.

Put $A' = A[T]$, where $T$ is an indeterminate. If $K = k(T)$, let $p = m A'$ and $B = A'_{p}$. Then $B/mB \cong
k[T]_{(0)} = k(T)$, and $B$ is flat over $A'$, which is a free $A$-module, so $B$ is flat over $A$.

If $K = k(t) = k[t]$, where $t$ is algebraic over $k$, set $B = A'/(F)$, where $F \in A'$ is a monic polynomial whose
image in `k[T]` is the minimal polynomial $f$ of $t$ over $k$. Then $B$ is a free $A$-module of finite rank $deg(F) =
deg(f)$. In particular, $B$ is integral over $A$, hence every maximal ideal of $B$ contains $m$. Since $B/mB \cong
k[T]/(f) \cong K$, it follows that $B$ is local, with maximal ideal `mB`. This already shows that if $[K : k] < \infty$,
one can choose $B$ finite and free over $A$.

In the general case, let $(t_{i})_{i \in I}$ be a system of generators of $K$ over $k$, and endow $I$ with a
well-ordering (i.e., a total order $\leqslant$ such that every non-empty subset of $I$ has a least element). For every
$i \in I$, let $k_{i}$ (resp. $k_{<i}$) denote the subfield of $K$ generated by the $t_{j}$ for $j \leqslant i$ (resp.
$j < i$). Adding one element if necessary, we may suppose that $I$ has a greatest element $\xi$, so that $K = k_{\xi}$.
Consider the subset $J$ of $I$ consisting of indices $i$ such that there exists an inductive system $(A_{j})_{j
\leqslant i}$ of local and flat $A$-algebras such that $A_{j}/m A_{j} \cong k_{j}$ and $A_{j}$ is flat over $A_{\ell}$
for every $\ell < j$. Suppose $I - J$ non-empty; let $i$ be its least element and let $A' = \lim_{j < i} A_{j}$. Since
tensor product commutes with direct limits, $A'$ is flat over $A$ and over each $A_{j}$ for $j < i$, and one has $A'/m
A' \cong A' \otimes_{A} (A/m) \cong k_{<i}$. Moreover, $A'$ is local, with maximal ideal $m A'$. Indeed, if $x =
f_{j}(x_{j})$ is non-invertible, then $x_{j}$ is not invertible, hence belongs to the maximal ideal $m A_{j}$ of
$A_{j}$, whence $x \in m A'$. It then follows from the monogenic case treated above that there exists a local and flat
$A'$-algebra $A_{i}$ such that $A_{i}/m A_{i} \cong k_{<i}(t_{i}) = k_{i}$; then $A_{i}$ is flat over each $A_{j}$ for
$j < i$, and so $i \in J$, contrary to hypothesis. This contradiction shows that $J = I$, and so $A_{\xi}$ answers the
question. Lemma 4.1.2 is proved.

<!-- original page 265 -->

Let us now prove 4.1 (iii). Recall that one denotes by $P$ the set underlying a scheme $P$, and by $d : P \to Q$ the map
induced by a morphism $d : P \to Q$. One can then translate b) by saying that the map

```text
   d₀ ⊠ d₁ : X₁ ⟶ X₀ ×_Y X₀
```

with components $d_{0}$ and $d_{1}$ is surjective; now this map factors as follows

```text
   X₁ ──d₀⊠d₁──→ X₀ × X₀ ──q──→ X₀ ×_Y X₀,
                       (set-theoretic Y-product)
```

$q$ being the canonical map; the image of $d_{0} \boxtimes d_{1}$ therefore contains all points $v$ of $X_{0} \times_{Y}
X_{0}$ such that ${v} = q^{-1}(q(v))$. This last condition[^N.D.E-V-23] will be realized in particular if $v$ is
rational over $Y$, that is to say, if the residue field $\kappa(v)$ of $v$ identifies with the residue field $\kappa(w)$
of the image $w$ of $v$ in $Y$.

<!-- original page 267 -->

If $v \in X_{0} \times_{Y} X_{0}$ is not rational over $Y$, let $w$ again be the image of $v$ in $Y$. By lemma 4.1.2,
there exists a local ring $C$ of radical $m$ and a local and flat homomorphism $f : O_{w} \to C$ such that $C/m$ is
isomorphic to $\kappa(v)$ as a $\kappa(w)$-algebra. If one sets $Y' = \operatorname{Spec} C$ and if $\pi : Y' \to Y$ is
the morphism induced by $f$, it is clear that the canonical projection of $(X_{0} \times_{Y} X_{0}) \times_{Y} Y'$ to
$X_{0} \times_{Y} X_{0}$ sends to $v$ a point $v'$ of $(X_{0} \times_{Y} X_{0}) \times_{Y} Y'$ which is rational over
$Y'$. Since

```text
   (X₀ ×_Y X₀) ×_Y Y′ ≅ (X₀ ×_Y Y′) ×_{Y′} (X₀ ×_Y Y′),
```

and since the hypotheses of theorem 4.1 and the previous results, in particular point b), remain valid after the base
change $\pi : Y' \to Y$, then $v'$ is the image of an element $u' \in X_{1} \times_{Y} Y'$ by the morphism deduced from
$d_{0} \boxtimes d_{1}$ by base change. If $u$ is the image of $u'$ in $X_{1}$, one indeed has $v = (d_{0} \boxtimes
d_{1})(u)$.

**f)** Proof of (iv):[^N.D.E-V-24]

**Lemma 4.1.3.** *If a monomorphism of schemes $f : T \to Z$ is a finite morphism, it is a closed immersion.*

<!-- label: III.V.4.1.3 -->

Indeed, covering $Z$ by affine opens $Z_{i}$ and replacing $f$ by the induced morphisms $f^{-1}(Z_{i}) \to Z_{i}$, we
reduce ($f$ being finite, hence affine) to the case where $Z = \operatorname{Spec} B$ and $T = \operatorname{Spec} A$.
Since $f$ is a monomorphism, the diagonal morphism $T \to T \times_{Z} T$ is an isomorphism (EGA I, 5.3.8), i.e., $A
\otimes_{B} A \to A$ is an isomorphism. Consequently, for every maximal ideal $m$ of $B$, one has an isomorphism

```text
   (A/mA) ⊗_k (A/mA) ≅ (A/mA),
```

<!-- original page 266 -->

where we have set $k = B/m$. Since $A$ is finite over $B$, $A/mA$ is a $k$-vector space of finite dimension $d$, and the
above isomorphism entails $d = 0$ or `1`, so that the morphism $k = B/m \to A/mA$ is surjective. Hence, by Nakayama's
lemma ($A$ being finite over $B$), the morphism $B_{m} \to A_{m}$ is surjective. It follows that the morphism of
$B$-modules $B \to A$ is surjective (since its cokernel $C$ satisfies $C_{m} = 0$ for every $m$, so is zero). This
proves the lemma.

Let us now prove (iv). By hypothesis, $X_{0} = \operatorname{Spec} A_{0}$, $X_{1} = \operatorname{Spec} A_{1}$, and, for
$i = 0, 1$, the morphism $\delta_{i} : A_{0} \to A_{1}$ makes $A_{1}$ a finitely generated $A_{0}$-module; thus, a
fortiori, the morphism $A_{0} \otimes_{B} A_{0} \to A_{1}$ is finite.

One assumes in addition that $d = d_{0} \boxtimes d_{1} : X_{1} \to X_{0} \times_{Y} X_{0}$ is a monomorphism; hence, by
the preceding lemma, the morphism $A_{0} \otimes_{B} A_{0} \to A_{1}$ is surjective.

We shall show that it is an isomorphism (we shall prove along the way that $p : X_{0} \to Y$ is finite and locally
free). It suffices to show that, for every prime ideal $p$ of $B$, the homomorphism $(A_{0})_{p} \otimes_{B_{p}}
(A_{0})_{p} \to (A_{1})_{p}$ with components $\delta_{0p}$ and $\delta_{1p}$ is bijective. In other words, one may
suppose $B$ local. It then follows from b) that $(A_{0})_{p}$ is semilocal; indeed, if $m$ is a maximal ideal of
$(A_{0})_{p}$, the other maximal ideals are of the form $\delta^{-1}_{0}(n)$, where $n$ runs over the prime ideals of
$A_{1}$ such that $\delta^{-1}_{1}(n) = m$; the assertion follows from the fact that there are at most $n = [A_{1} :
A_{0}]$ such prime ideals $n$. Possibly performing a faithfully flat base change,[^N.D.E-V-25] one can also suppose that
the residue field of $B$ is infinite, so that one can use the following lemma:

**Lemma 4.2.** *Let $B$ be a local ring with infinite residue field, $A$ a semilocal ring, and $i : B \to A$ a
homomorphism sending the maximal ideal $n$ of $B$ into the radical $r$ of $A$. Let $M$ be a free $A$-module of rank $n$
and $N$ a $B$-submodule of $M$ that generates $M$ as an $A$-module. Then $N$ contains a basis of $M$ over $A$.*

<!-- label: III.V.4.2 -->

<!-- original page 268 -->

Recall indeed that a sequence $m_{1}, \cdots, m_{n}$ of elements of $M$ is an $A$-basis of $M$ if and only if the
canonical images of $m_{1}, \cdots, m_{n}$ in $M/rM$ form a basis of $M/rM$ over $A/r$. One can therefore replace $M$ by
$M/rM$, $N$ by $N/(N \cap rM)$, $A$ by $A/r$ and $B$ by $B/n$. In this case the lemma is easy (if $A$ is a product of
fields $K_{1} \times \cdots \times K_{r}$, one can identify $M$ with the module $K^{n}_{1} \times \cdots \times
K^{n}_{r}$; if $x_{j}$ is then an element of $N$ whose $j$-th component in $K^{n}_{1} \times \cdots \times K^{n}_{r}$ is
non-zero, show that a certain linear combination $x$ of the $x_{j}$ with coefficients in $B$ has all components
non-zero; then replace $M$ by $M/Ax$ and proceed by induction on $n$).

We apply the preceding lemma in the following situation: $B = B$, $A = A_{0}$, $i$ is the inclusion of $B$ in $A_{0}$,
$M = A_{1}$ regarded as an $A_{0}$-module via the homomorphism $\delta_{1}$, $N = \delta_{0}(A_{0})$. Indeed, since
$d_{0} \boxtimes d_{1} : X_{1} \to X_{0} \times_{Y} X_{0}$ is a closed immersion, the homomorphism $A_{0} \otimes_{B}
A_{0} \to A_{1}$ with components $\delta_{0}$ and $\delta_{1}$ is surjective; this means precisely that
$\delta_{0}(A_{0})$ generates the $A_{0}$-module $A_{1}$.

Let then $a_{1}, \cdots, a_{n}$ be elements of $A_{0}$ such that $\delta_{0}(a_{1}), \cdots, \delta_{0}(a_{n})$ form a
basis of $A_{1}$ over $A_{0}$. If we show that $a_{1}, \cdots, a_{n}$ is a basis of $A_{0}$ over $B$, it will follow
that the homomorphism $A_{0} \otimes_{B} A_{0} \to A_{1}$ sends the basis $(1 \otimes a_{i})_{1 \leqslant i \leqslant
n}$ to the basis $(\delta_{0}(a_{i}))_{1 \leqslant i \leqslant n}$, hence is bijective. Consequently, if $\epsilon :
\mathbb{Z}^{n} \to A_{0}$ is the morphism of abelian groups sending the natural basis of $\mathbb{Z}^{n}$ to $a_{1},
\cdots, a_{n}$, it suffices to prove that the map $B \otimes_{\mathbb{Z}} \mathbb{Z}^{n} \to A_{0}$ with components $i$
and $\epsilon$ is bijective.

<!-- original page 269 -->

Now the diagram $(0, 1, 2)\ast$ considered at the beginning of this proof induces the following commutative diagram:

```text
                    δ′₁                       δ₀
            A₂ ⇇ A₁ ⇇ A₀
                    δ′₀
            │       │ ≅           │
         u₂ │    u₁ │           u₀│
            ↓       ↓             ↓
                    δ₁ ⊗ ℤⁿ      i ⊗ ℤⁿ
            A₁ ⊗_ℤ ℤⁿ ⇇ A₀ ⊗_ℤ ℤⁿ ⇇ B ⊗_ℤ ℤⁿ,
                    δ₀ ⊗ ℤⁿ
```

where $u_{0}$, $u_{1}$ and $u_{2}$ have respectively as components $i$ and $\epsilon$, $\delta_{1}$ and $\delta_{0}
\epsilon$, $\delta'_{2}$ and $\delta'_{0} \delta_{0} \epsilon$. We know that $u_{1}$ is an isomorphism. Since the two
left-hand squares of $(0, 1, 2)\ast$ are cocartesian, $u_{2}$ is bijective. But the two horizontal rows of our diagram
are exact, so $u_{0}$ is bijective.[^N.D.E-V-26] This shows that $A_{0}$ is a $B$-module locally free of rank $n$, and,
by the previous reductions, this entails that $\delta_{0} \otimes \delta_{1} : A_{0} \otimes_{B} A_{0} \to A_{1}$ is an
isomorphism. This completes the proof of theorem 4.1 in the particular case considered ($X_{0}$ affine and $d_{1}$
locally free of constant rank $n$).

## 5. Passage to the quotient by a finite and flat groupoid (general case)

<!-- label: III.V.5 -->

**a)** Let $U^{(n)}$ be the largest open subset of $X_{0}$ above which $d_{1}$ is finite locally free of rank $n$. One
knows that $X_{0}$ is the direct sum of the $U^{(n)}$. It follows on the other hand from the two Cartesian squares

```text
              d′₀                              d′₁
   X₂ ────→ X₁          and       X₂ ────→ X₁
   │         │                     │         │
d′₂│         │ d₁                d′₂│         │ d₁
   ↓         ↓                     ↓         ↓
   X₁ ────→ X₀                     X₁ ────→ X₀
        d₀                                d₁
```

that the inverse images of $U^{(n)}$ under $d_{0}$ and $d_{1}$ both coincide with the largest open subset of $X_{1}$
above which $d'_{2}$ is locally free of rank $n$;[^N.D.E-V-27] one therefore has $d^{-1}_{0}(U^{(n)}) =
d^{-1}_{1}(U^{(n)})$, so that the groupoid $X\ast$ is the direct sum of the groupoids $X\ast^{(n)}$ induced by $X\ast$
on the open-and-closed subsets $U^{(n)}$. Consequently, as one sees easily, it suffices to prove theorem 4.1 for each of
the $X\ast^{(n)}$: one is reduced to the case where $d_{1}$ is finite locally free of rank $n$.

**b)** We are now in a position to prove our theorem in the general case.

<!-- original page 270 -->

By a) one may suppose $d_{1}$ locally free of rank $n$. Let then $(Y, p)$ be a cokernel of $(d_{0}, d_{1})$ in the
category of all ringed spaces. The argument at the end of paragraph 4.c) shows that to prove 4.1 (i) it suffices to
prove that $Y$ is a scheme and $p : X_{0} \to Y$ a morphism of schemes. By lemma 1.2, the question is local on $Y$: let
$y \in Y$ and let $x \in X_{0}$ with $p(x) = y$; if $x$ possesses a saturated affine open neighborhood $U$, then $p(U)$
will be an affine open of $Y$ by § 4, and $p|U$ will be a morphism of schemes. It therefore suffices to prove that every
$x \in X_{0}$ possesses a saturated affine open neighborhood $U$. Here is how one proceeds (the proof is taken from SGA
1, VIII, cor. 7.6).

```text
   d₁(d₀⁻¹(x)) ⊂ U = (V_f)′ ⊂ V_f ⊂ V′ ⊂ V ⊂ X₀

      ↑                ↑           ↑
   affine open    special       affine
   special of V   affine open   open
                  of V
                      ↑           ↑
                  largest     largest
                  saturated   saturated
                  open in V_f open in V
```

By condition b) of 4.1, there exists an affine open $V$ of $X_{0}$ containing $d_{1}(d^{-1}_{0}(x))$;[^N.D.E-V-28] if $F
= X_{0} - V$, then $d_{1}(d^{-1}_{0}(F))$ is closed since $d_{1}$ is integral, and $V' = X_{0} - d_{1}(d^{-1}_{0}(F))$
is the largest saturated open contained in $V$. Since $V'$ is a neighborhood of the finite set $d_{1}(d^{-1}_{0}(x))$,
there exists a section $f$ of the structure sheaf of $V$ vanishing on $V - V'$ and such that $d_{1}(d^{-1}_{0}(x))$ is
contained in the open $V_{f}$ of $V$ consisting of points where $f$ does not vanish. We shall show that the largest
saturated open $(V_{f})'$ of $V_{f}$ is affine, and therefore answers the question.

Indeed, let $Z(f) = V' - V_{f}$. Then $d^{-1}_{0}(Z(f))$ is the set of points of $d^{-1}_{0}(V') = d^{-1}_{1}(V')$ where
the image $d^{\ast}_{0}(f)$ of $f$ under the map induced by $d_{0}$ vanishes. On the other hand, since $d_{1}$ induces a
locally free morphism of rank $n$ from $d^{-1}_{0}(V') = d^{-1}_{1}(V')$ onto $V'$,[^N.D.E-V-29] then, by lemma 4.1.1,
$d_{1}(d^{-1}_{0}(Z(f)))$ is the set of points where the norm $N$ of $d^{\ast}_{0}(f)$ for the morphism $d_{1}$
vanishes. It follows that $(V_{f})' = V' - d_{1}(d^{-1}_{0}(Z(f)))$ is the set of points of $V_{f}$ where $N$ does not
vanish; consequently, $(V_{f})'$ is affine.

<!-- original page 271 -->

This proves 4.1 (i); assertions (ii), (iii), and the first part of (iv) are then clear. Let us finally show the
consequences indicated at the end of point (iv) (cf. [Ray67a], th. 1 (iii)).

By hypothesis, the groupoid $X\ast$ comes from an equivalence relation $i : R \to X_{0} \times X_{0}$ ($i$ being
therefore an immersion, cf. N.D.E. 19), and one has established that $R$ is effective (cf. Exp. IV, 3.3.2) and that $p :
X_{0} \to Y = X_{0}/R$ is a surjective and finite locally free morphism, hence in particular faithfully flat and of
finite presentation.

Consequently, denoting by `(M)` the family of faithfully flat morphisms locally of finite presentation, $R$ is
`(M)`-effective. Therefore, by Exp. IV, 6.3.3, $(Y, p)$ represents the quotient sheaf of $X_{0}$ by $R$ for the (fppf)
topology, and the assertions concerning base change follow from IV, 3.4.3.1.

**Remark 5.1.**[^N.D.E-V-30] *We keep the hypotheses and notations of 4.1, and suppose in addition that $S$ is locally
Noetherian and $\pi_{0} : X_{0} \to S$ is quasi-projective. Let us then show that $\pi : Y \to S$ is quasi-projective.*

<!-- label: III.V.5.1 -->

The above hypotheses imply that $Y \to S$ is of finite type, see the proof of 6.1 (ii). Let $A$ be an invertible
$O_{X_{0}}$-module that is ample for $\pi_{0}$. By EGA II, 6.1.12, $p_{\ast}(A)$ is an invertible
$p_{\ast}(O_{X_{0}})$-module. There therefore exists a covering $(V_{i})_{i \in I}$ of $Y$ by affine opens such that $A$
is trivial above each of the saturated affine opens $U_{i} = p^{-1}(V_{i})$.

For each index $i$, write $A_{i,0} = O_{X_{0}}(U_{i})$, $A_{i,1}$ the ring of the affine open $d^{-1}_{0}(U_{i}) =
d^{-1}_{1}(U_{i})$ of $X_{1}$, $\delta_{i,0}$ (resp. $\delta_{i,1}$) the morphism $A_{i,0} \to A_{i,1}$ induced by
$d_{0}$ (resp. $d_{1}$), and $B_{i} = O_{Y}(V_{i}) = {b \in A_{i,0} | \delta_{i,0}(b) = \delta_{i,1}(b)}$.

Following EGA II, § 6.5, consider the invertible $O_{X_{0}}$-module $N_{d_{1}}(d^{\ast}_{0}(A))$, the norm relative to
the finite locally free morphism $d_{1} : X_{1} \to X_{0}$ of the invertible $O_{X_{1}}$-module $d^{\ast}_{0}(A)$. If
$A$ is given, relative to the covering $(U_{i})_{i \in I}$, by transition functions $c_{ij} \in O_{X_{0}}(U_{i} \cap
U_{j})^{\times}$, then $N_{\delta_{1}}(d^{\ast}_{0}(A))$ is given by the transition functions
$N_{d_{1}}(\delta_{0}(c_{ij})) \in O_{X_{0}}(U_{i} \cap U_{j})^{\times}$; since, by paragraph 4.a), these elements
belong to $O_{Y}(V_{i} \cap V_{j})^{\times}$, they define an invertible `O_Y`-module $L$, such that $p^{\ast}(L) =
N_{d_{1}}(d^{\ast}_{0}(A))$. Moreover, note that for every $n \in \mathbb{N}^{\ast}$, one has $p^{\ast}(L^{n}) =
N_{d_{1}}(d^{\ast}_{0}(A^{n}))$, cf. loc. cit., (6.5.2.1).

Let us show that $L$ is ample for the morphism $\pi : Y \to S$. For this, replacing $S$ by an affine open, we may
suppose $S$ affine. Let then $y \in Y$, $x \in X_{0}$ with $p(x) = y$, $V$ an affine open of $Y$ containing $y$, and $U
= p^{-1}(V)$. Since $A$ is $\pi_{0}$-ample, there exists $n \in \mathbb{N}^{\ast}$ and a section $s \in \Gamma(X_{0},
A^{n})$ such that the open $(X_{0})_{s}$ satisfies $x \in (X_{0})_{s} \subset U$. With the preceding notations, $s$ is
given by sections $a_{i} \in A_{i,0} = O_{X_{0}}(U_{i})$ such that $a_{i} = c_{ij} a_{j}$ on $U_{i} \cap U_{j}$, and
$(X_{0})_{s}$ is the union of the opens $U'_{i} = {p \in \operatorname{Spec}(A_{i,0}) | a_{i} \notin p}$.

For each index $i$, put $N(a_{i}) = N_{\delta_{1}}(\delta_{0}(a_{i})) \in B_{i}$. By 4.1 (i) and lemma 4.1.1, one has:

```text
   p(U′_i) = p d₁(d₀⁻¹(U′_i)) = p d₁({q ∈ Spec(A_{i,1}) | δ_{i,0}(a_i) ∉ q})
```

and $d_{1}({q \in \operatorname{Spec}(A_{i,1}) | \delta_{i,0}(a_{i}) \notin q}) = {p \in \operatorname{Spec}(A_{i,0}) |
N_{\delta_{1}}(\delta_{i,0}(a_{i})) \notin p}$, whence

```text
   p(U′_i) = {p ∈ Spec(B_i) | N(a_i) ∉ p}.
```

It follows that $p((X_{0})_{s})$ equals $Y_{N(s)}$, where we have written $N(s)$ for the section of $L^{n}$ over $Y$
defined by the sections $N(a_{i}) \in O_{Y}(V_{i})$. One thus has

```text
(∗)   y ∈ p((X₀)_s) = Y_{N(s)} ⊂ p(U) = V.
```

This shows that $L$ is ample for $\pi : Y \to S$, which finishes showing that $\pi : Y \to S$ is quasi-projective.

<!-- original page 270 -->

## 6. Passage to the quotient when a quasi-section exists

<!-- label: III.V.6 -->

We shall now prove a lemma of technical character which will be useful in the proof of the two theorems we have in view.
Let $S$ be a scheme and

```text
        d′₀, d′₁, d′₂      d₀, d₁
   X₂ ⇶ X₁ ⇉ X₀
```

a $(Sch/S)$-groupoid. We shall call a *quasi-section* of the groupoid $X\ast$ any subscheme $U$ of $X_{0}$ such that (1)
and (2) hold:

(1) The restriction $v$ of $d_{1}$ to $d^{-1}_{0}(U)$ is a finite, locally free, and surjective morphism from
$d^{-1}_{0}(U)$ onto $X_{0}$.

(2) Every subset $E$ of $U$ consisting of points pairwise equivalent for the equivalence relation defined by $X\ast$ (§
3.e)) is contained in an affine open of $U$.[^N.D.E-V-31]

If $U$ is a quasi-section of $X\ast$, the $(Sch/S)$-groupoid

```text
        u′₀, u′₁, u′₂      u₀, u₁
   U₂ ⇶ U₁ ⇉ U
```

<!-- original page 272 -->

induced by $X\ast$ and the inclusion of $U$ into $X_{0}$ (cf. § 3.a)) satisfies the hypotheses of theorem 4.1. Set
indeed $V = d^{-1}_{0}(U)$ and let $u$ and $v$ be the morphisms with source $V$ induced respectively by $d_{0}$ and
$d_{1}$:

```text
   X₀ ←─v── V ──u──→ U.
```

By paragraph 3.b), one has a Cartesian square

```text
                  
   U₁ ──────→ V
   │           │
u₁ │           │ v
   ↓           ↓
   U ─inclusion─→ X₀,
```

so $u_{1}$ is surjective and finite locally free by (1). With (2), condition (1) therefore ensures that the groupoid
$U\ast$ satisfies the hypotheses of theorem 4.1. In particular $Coker(u_{0}, u_{1})$ exists in $(Sch/S)$. Moreover,
$d_{0}$ has a section, so that $u$ is a universal effective epimorphism (cf. III 1.12); it follows, by proposition 3.1,
that $Coker(u_{0}, u_{1})$ coincides with the cokernel $Coker(v_{0}, v_{1})$ of the groupoid $V\ast$:

```text
        v′₀, v′₁, v′₂      v₀, v₁
   V₂ ⇶ V₁ ⇉ V,
```

inverse image of $U\ast$ under the base change $u : V \to U$, that is also the inverse image of $X\ast$ under the base
change:

```text
   V ──inclusion──→ X₁ ──d₀──→ X₀.
```

By paragraph 3.c), $V\ast$ is isomorphic to the groupoid $V'\ast$, the inverse image of $X\ast$ under the base change:

```text
   v :  V ──inclusion──→ X₁ ──d₁──→ X₀,
```

and so $V'\ast$ admits a cokernel in $(Sch/S)$. Now, being flat, surjective and finite, $v : V \to X_{0}$ is faithfully
flat and quasi-compact, hence a universal effective epimorphism by III 6.3.2. Consequently, by proposition 3.1, the
groupoid $X\ast$ admits a cokernel $Coker(d_{0}, d_{1})$ in $(Sch/S)$. We have thus proved the first assertion of point
(i) of the following lemma:[^N.D.E-V-32]

<!-- original page 273 -->

**Lemma 6.1.** *Suppose that the $(Sch/S)$-groupoid $X\ast$ possesses a quasi-section. Then:*

<!-- label: III.V.6.1 -->

*(i) There exists a cokernel $(Y, p)$ of $(d_{0}, d_{1})$ in $(Sch/S)$; moreover, such a $(Y, p)$ is a cokernel of
$(d_{0}, d_{1})$ in the category of all ringed spaces.*

*(i′) $p$ is surjective, and is open (resp. universally closed) if $d_{0}$ is.*

*(ii) Suppose $S$ locally Noetherian and $X_{0}$ locally of finite type (resp. of finite type) over $S$. Then $p$ and $Y
\to S$ are locally of finite presentation (resp. of finite presentation).*

*(iii) The morphism $X_{1} \to X_{0} \times_{Y} X_{0}$ with components $d_{0}$ and $d_{1}$ is surjective.*

*(iv) If $(d_{0}, d_{1})$ is an equivalence pair, then $X_{1} \to X_{0} \times_{Y} X_{0}$ is an isomorphism. Moreover,
if $d_{0} : X_{1} \to X_{0}$ is flat, $p$ is faithfully flat.*

Before proving the second assertion of (i), we shall demonstrate (i′), (ii) and (iii).

**a)** Proof of (i′) and (ii):

We have just seen that $(Y, p)$ identifies with $Coker(v_{0}, v_{1})$ and $Coker(u_{0}, u_{1})$. Let then $q$ and $r$ be
the canonical epimorphisms from $U$ and $V$ into $Y$:

```text
   X₀ ←─v── V ──u──→ U
        ↘        ↙
         r     q
          ↘ ↙
           Y.
```

By hypothesis, $v$ is surjective and finite locally free, hence open. On the other hand, if $d_{0} : X_{1} \to X_{0}$ is
open (resp. universally closed), then $u$, which is obtained from it by base change, is also.

<!-- original page 274 -->

Since, by theorem 4.1, $q$ is surjective, integral, and open, it follows that $r$ is surjective, and open (resp.
universally closed) if $d_{0}$ is. The same therefore holds for $p$, since $v$ is surjective. This proves (i′).

Suppose now $S$ locally Noetherian and $X_{0}$ locally of finite type over $S$, so that $X_{0}$ is locally Noetherian.

Let us show that $Y$ is locally of finite presentation over $S$. Let $S' = \operatorname{Spec} R$ be an affine open of
$S$, $Y' = \operatorname{Spec} B$ an affine open of $Y$ projecting into $S'$, and $U' = \operatorname{Spec} A$ the
inverse image of $Y'$ in $U$. Since $R$ is Noetherian, it suffices to show that $B$ is a finitely generated $R$-algebra;
but, by paragraphs 4 and 5, $B$ is contained in $A$, which is a finitely generated $R$-algebra; the assertion therefore
follows from the fact that $R$ is Noetherian and $A$ is integral over $B$.

Finally, since $X_{0} \to S$ is locally of finite type, so is $p$ (EGA I, 6.6.6), hence $p$ is locally of finite
presentation since $Y$ is locally Noetherian.

It remains to show the last assertion of (ii). Suppose in addition $X_{0}$ of finite type over $S$. Then, since $p$ is
surjective, $Y$ is also quasi-compact over $S$, hence of finite type over $S$. Since $S$ is locally Noetherian, then
$X_{0} \to S$ and $Y \to S$ are of finite presentation, and so $p : X_{0} \to Y$ is also (EGA IV_1, 1.6.2 (v)).

**b)** Proof of (iii):

Since the groupoid $V\ast$ with base $V$ is isomorphic both to the inverse image of $U\ast$ under the base change $u$
and to the inverse image of $X\ast$ under the base change $v$, one has a double Cartesian square

```text
   X₁ ←──── V₁ ─────→ U₁
   │         │          │
d₀⊠d₁│     v₀⊠v₁│    u₀⊠u₁
   ↓         ↓          ↓
   X₀ ×_Y X₀ ←─── V ×_Y V ───→ U ×_Y U.
              v × v        u × u
```

Since $u_{0} \boxtimes u_{1}$ is surjective, so is $v_{0} \boxtimes v_{1}$. Since $v \times v$ is surjective, so is the
composite morphism $V_{1} \to X_{0} \times_{Y} X_{0}$, and therefore so is $d_{0} \boxtimes d_{1}$.

<!-- original page 275 -->

**c)** Proof of (i):

It remains to prove that $(Y, p)$ is a cokernel of $(d_{0}, d_{1})$ in the category of all ringed spaces. We first show
that $Y$ is obtained from $X_{0}$ by identifying the points $x$ and $y$ such that there exists $z \in X_{1}$ with
$d_{0}(z) = x$ and $d_{1}(z) = y$. Indeed, $p$ is surjective and one has $p d_{0} = p d_{1}$; moreover, if $p(x) =
p(y)$, there is a point $z'$ of $X_{0} \times_{Y} X_{0}$ whose first projection is $x$ and second projection is $y$. If
$z$ is a point of $X_{1}$ such that $(d_{0} \boxtimes d_{1})(z) = z'$, one indeed has $d_{0}(z) = x$ and $d_{1}(z) = y$.

On the other hand, if $W$ is a saturated open of $X_{0}$, then $W \cap U$ is a saturated open of $U$; by 4.1, $q(W \cap
U)$ is an open of $Y$. Since $q(W \cap U)$ is none other than $p(W)$, one sees that $Y$ is endowed with the quotient
topology of that of $X_{0}$.

It remains to show that the canonical sequence of sheaves of rings

```text
   O_Y → p_∗(O_{X₀}) ⇉ p_∗ d_{0∗}(O_{X₁}) = p_∗ d_{1∗}(O_{X₁})
```

is exact.

Let then $Y'$ be an open of $Y$ and put $U' = q^{-1}(Y')$, $X'_{0} = p^{-1}(Y')$, etc.[^N.D.E-V-33] Then $U'$ is an open
of $U$ saturated for the equivalence relation defined by the groupoid $U\ast$, and it follows from lemmas 1.1 and 1.2
that $Y'$ is the cokernel, in $(Sch/S)$ and in `(Esp.An)`, of the groupoid induced by $U\ast$ on $U'$. Similarly,
$X'_{0}$ is an open of $X_{0}$ saturated for the equivalence relation defined by $X\ast$, and one has the following
commutative diagram, where the two squares are Cartesian:

```text
              d̃₁                              d̃₀
   X′₀ ←─── V′ = d₀⁻¹(U′) ────→ U′
   │              │                  │
   │              │                  │
   ↓              ↓                  ↓
   X₀ ←──── V = d₀⁻¹(U) ────→ U′.
              d₁                       d₀
```

Then $\tilde{d}_{1}$ is surjective, and finite locally free. On the other hand, let $x \in U'$. Since $U$ is a
quasi-section, the set $E := d_{0} d^{-1}_{1}(x) \cap U$ is finite and contained in an affine open $W$ of $U$. Then $E'
= E \cap U'$ is a finite set, contained in the quasi-affine open $W \cap U'$. Consequently, there exists an affine open
$W'$ of $W \cap U'$ containing $E'$. This shows that $U'$ is a quasi-section of the groupoid $X'\ast$ induced by $X\ast$
on $X'_{0}$. The first assertion of (i), applied to $X'\ast$ and $U'$, then shows that $Y'$ is the cokernel in $(Sch/S)$
of $X'\ast$.

In particular, for every $S$-scheme $T$, one has the exact sequence

```text
                  T(p|_{X′₀})              T(d₁|_{X′₁})
   T(Y′) ────────→ T(X′₀) ⇉ T(X′₁).
                                      T(d₀|_{X′₁})
```

<!-- original page 276 -->

Now, if $T$ is the "affine line" $G_{a,S}$ (I 4.3), this sequence identifies with the sequence

```text
                                          δ₁
   Γ(Y′, O_Y) → Γ(p⁻¹(Y′), O_{X₀}) ⇉ Γ(d₀⁻¹ p⁻¹(Y′), O_{X₁}) = Γ(d₁⁻¹ p⁻¹(Y′), O_{X₁})
                                          δ₀
```

which is therefore exact for every open $Y'$. This completes the proof of 6.1 (i).

**d)** Proof of (iv):

If $(d_{0}, d_{1})$ is an equivalence pair, the same holds for $(u_{0}, u_{1})$. It follows that
$u_{0} \boxtimes u_{1} : U_{1} \to U \times_{Y} U$ is an isomorphism (theorem 4.1), hence so is $v_{0} \boxtimes v_{1}$
(confer the Cartesian squares of b)); since $v \times v$ is faithfully flat and quasi-compact, $d_{0} \boxtimes d_{1}$
is an isomorphism (SGA 1, VIII 5.4).

Moreover, if $d_{0}$ is flat, so is $u$. Now $q$ is flat, by theorem 4.1, so $r$ also is. Since $v$ is faithfully flat,
then $p$ is flat, and therefore faithfully flat since surjective.

## 7. Quotient by a proper and flat groupoid

<!-- label: III.V.7 -->

**Theorem 7.1.**[^N.D.E-V-34] *Let $S$ be a locally Noetherian scheme and*

<!-- label: III.V.7.1 -->

```text
        d′₀, d′₁, d′₂      d₀, d₁
   X₂ ⇶ X₁ ⇉ X₀
```

*a $(Sch/S)$-groupoid such that $d_{1}$ is proper and flat, $X_{0}$ is quasi-projective over $S$,*[^N.D.E-V-35] *and the
morphism $d : X_{1} \to X_{0} \times_{S} X_{0}$ with components $d_{0}$ and $d_{1}$ is quasi-finite. Then:*

*(i) There exists a cokernel $(Y, p)$ of $(d_{0}, d_{1})$ in $(Sch/S)$; moreover, such a $(Y, p)$ is a cokernel of
$(d_{0}, d_{1})$ in the category of all ringed spaces.*

<!-- original page 277 -->

*(ii) $p$ is surjective, open, proper, of finite presentation, and $Y \to S$ is of finite presentation and
separated.*[^N.D.E-V-36]

*(iii) The morphism $X_{1} \to X_{0} \times_{Y} X_{0}$ with components $d_{0}$ and $d_{1}$ is surjective.*

*(iv) If $(d_{0}, d_{1})$ is an equivalence pair, then $X_{1} \to X_{0} \times_{Y} X_{0}$ is an isomorphism and $p$ is
faithfully flat.*[^N.D.E-V-37] *Moreover, $(Y, p)$ is a cokernel of $(d_{0}, d_{1})$ in the category of sheaves for the
(fppf) topology and, for every base change $Y' \to Y$, $Y'$ is the cokernel of the groupoid $X\ast \times_{Y} Y'$
obtained from $X\ast$ by the base change $X_{0} \times_{Y} Y' \to X_{0}$.*

*In particular, for every base change $S' \to S$, $Y' = Y \times_{S} S'$ is the cokernel of the $S'$-groupoid $X'\ast =
X\ast \times_{S} S'$. So, in this case, "the formation of the quotient commutes with base change".*

Let $(Y, p)$ be the cokernel of $(d_{0}, d_{1})$ in the category of all ringed spaces. Lemma 1.2 shows that, to prove
(i), it suffices to show that every point $z$ of $X_{0}$ possesses a saturated open neighborhood $U_{z}$ such that,
denoting by $\tilde{d}_{0}$ and $\tilde{d}_{1}$ the restrictions of $d_{0}$ and $d_{1}$ to $d^{-1}_{0}(U_{z}) =
d^{-1}_{1}(U_{z})$, and by $(Q, q)$ the cokernel of $(\tilde{d}_{0}, \tilde{d}_{1})$ in `(Esp.An)`, $Q$ is a scheme and
$q$ a morphism of schemes.

By lemma 6.1 (i), it therefore suffices to show that every point $z$ of $X_{0}$ possesses a saturated open neighborhood
$U_{z}$ such that the groupoid induced on $U_{z}$ by $X\ast$ possesses a quasi-section. One can even suppose that $z$ is
closed in its fiber over $S$ (we shall say that $z$ is *closed relative to $S$*).[^N.D.E-V-38] The existence of $U_{z}$
then follows from the lemmas below:

<!-- original page 275 -->

**Lemma 7.2.** *Let $T$ be an affine Noetherian scheme, $X$, $Y$, and $Z$ $T$-schemes of finite type, with $X$
quasi-projective over $T$, and*

<!-- label: III.V.7.2 -->

```text
   Y ──u──→ X
   │         ⋮
v  │         ⋮
   ↓         ↓
   Z ⋯⋯⋯⋯→ T
```

*a diagram in $(Sch/T)$. Let $z$ be a point of $v(Y)$ that is closed relative to $T$ and such that $v$ is flat at the
points of $v^{-1}(z)$. Then there exists a closed subscheme $F$ of $X$ such that $u(u^{-1}(F) \cap v^{-1}(z))$ is finite
and non-empty, and such that the restriction of $v$ to $u^{-1}(F)$ is flat at the points of $v^{-1}(z)$.*

Let $T = \operatorname{Spec} A$. One may suppose $X$ of the form $\operatorname{Proj} S$, where $S$ is the symmetric
algebra of a finitely generated $A$-module $E$.

If $u(v^{-1}(z))$ is finite, one can choose $F$ equal to $X$. Otherwise, we denote by $y_{1}, \cdots, y_{n}$

<!-- original page 278 -->

the points of the fiber $v^{-1}(z)$ associated with the structure sheaf $O_{v^{-1}(z)}$ of $v^{-1}(z)$ (the $y_{i}$ are
such that, if $O_{i}$ denotes the local ring of $v^{-1}(z)$ at $y_{i}$, the maximal ideal of $O_{i}$ consists of zero
divisors). If $t$ is the image of $z$ in $T$, $u(v^{-1}(z))$ is an infinite constructible subset of the fiber of $t$ in
$X$. There therefore exists a point $x$ closed in this fiber, belonging to $u(v^{-1} z)$ and distinct from $u(y_{1}),
\cdots, u(y_{n})$. Then $X - {x}$ is an open neighborhood of $u(y_{1}), \cdots, u(y_{n})$, hence contains an open
neighborhood of the form $D_{+}(f)$, where $f$ is a homogeneous element of degree $d$ of $S$ (the notations are those of
EGA II, § 2.3).

Consequently, the closed subscheme $X_{1} = V_{+}(f)$ defined by $f$ contains $x$ and avoids the points $u(y_{1}),
\cdots, u(y_{n})$. It follows of course that the inverse image $Y_{1} = u^{-1}(V_{+}(f))$ of this subscheme is distinct
from $Y$ and meets $v^{-1}(z)$. We shall further show that the restriction $v_{1}$ of $v$ to $Y_{1}$ is flat at the
points of $v^{-1}(z)$; if $u(v^{-1}_{1}(z))$ is finite, we shall therefore only need to choose $F$ equal to $X_{1}$;
otherwise, we shall repeat the argument we have just developed, replacing $Y$ by $Y_{1}$, $v$ by $v_{1}$, $u$ by the
morphism $u_{1}$ induced on $Y_{1}$ by $u$; in this way we shall obtain a decreasing sequence $X, X_{1}, \cdots$ of
closed subschemes of $X$; since such a sequence terminates, $u(u^{-1}(X_{n}) \cap v^{-1}(z))$ will be finite and
non-empty for some $n$, and one will choose $F$ equal to $X_{n}$.

It remains then to show that $v_{1}$ is flat at the points of $v^{-1}(z)$; let $y$ be a point of $Y_{1}$ above $z$,
$O_{y}$ the local ring of $y$ in $Y$, $\bar{O}_{y}$ the local ring of $y$ in $v^{-1}(z)$, $O_{v(y)}$ the local ring of
$v(y)$ in $Z$. If $g \in S_{1}$ is such that $D_{+}(g)$ is a neighborhood of $u(y)$ in $X$, let $\phi$ be the image of
$f/g^{d}$ in $O_{y}$ and $\bar{\phi}$ the image of $f/g^{d}$ in $\bar{O}_{y}$. It then follows from the construction of
$f$ that $\bar{\phi}$ is not a zero divisor in $\bar{O}_{y}$; since

<!-- original page 276 -->

$O_{y}$ is flat over $O_{z}$, $\phi$ is not a zero divisor in $O_{y}$ and $O_{y}/O_{y} \phi$ is flat over $O_{z}$ (SGA
1, IV 5.7). But $O_{y}/O_{y} \phi$ is precisely the local ring of $y$ in $Y_{1}$.

<!-- original page 279 -->

**Lemma 7.3.** *We keep the notations and hypotheses of 7.1. Every point $z$ of $X_{0}$ closed relative to $S$ therefore
possesses a saturated open neighborhood $U_{z}$ such that the groupoid induced by $X\ast$ on $U_{z}$ possesses a
quasi-section.*

<!-- label: III.V.7.3 -->

The statement being local on $S$, one may suppose $S$ affine Noetherian and apply the previous lemma to the diagram

```text
   X₁ ──d₀──→ X₀
   │           ⋮
d₁ │           ⋮
   ↓           ↓
   X₀ ⋯⋯⋯⋯→ S
```

of $(Sch/S)$. Let then $F$ be a closed subscheme of $X_{0}$ such that $d_{0}(d^{-1}_{0}(F) \cap d^{-1}_{1}(z))$ is
finite and non-empty, and such that the restriction of $d_{1}$ to $d^{-1}_{0}(F)$ is flat at the points of
$d^{-1}_{1}(z)$.[^N.D.E-V-39]

Denote by $F_{1}$ and $F_{2}$ the inverse images of $F$ under $d_{0}$ and under $d_{0} d'_{0} = d_{0} d'_{1}$, and
denote by $\tilde{d}_{0}$, $\tilde{d}_{1}$, etc., the morphisms induced by $d_{0}$, $d_{1}$, etc. One thus has a
commutative diagram

```text
                d̃′₁              d̃₀
        F₂ ─────→ F₁ ─────→ F
                d̃′₀                ⋮ q̃
    d̃′₂│         │ d̃₁              ⋮
        ↓         ↓                 ↓
        X₁ ─────→ X₀ ⋯⋯⋯⋯→ S,
                d₁          q
                d₀
```

where the two left-hand squares are Cartesian and the first row is exact (confer (0,1,2), § 1), and where $q$ and
$\tilde{q}$ denote the structure morphisms.

Let us first show that there are only finitely many points of $F_{1}$ above $z$.[^N.D.E-V-39] Indeed, let $s$ be the
image of $z$ in $S$; since $F$ is of finite type over $S$, the fiber $\tilde{q}^{-1}(s)$ is a Noetherian scheme. On the
other hand, since $\tilde{d}_{0}$ is proper, $\tilde{d}_{0}(\tilde{d}^{-1}_{1}(z))$ is a closed subscheme of
$\tilde{q}^{-1}(s)$, consisting of finitely many points. Consequently (cf. EGA I, 6.2.2), the points of this set are
closed in $\tilde{q}^{-1}(s)$, and also (since $F$ is closed in $X_{0}$) in the fiber $q^{-1}(s)$ of $s$ in $X_{0}$. Let
$y$ be one of these points; since the fiber $q^{-1}(s)$ is of finite type over $\kappa(s)$, it contains affine open
neighborhoods $\operatorname{Spec} B$ and $\operatorname{Spec} C$ of $y$ and $z$, respectively, where $B$ and $C$ are
finitely generated $\kappa(s)$-algebras. Then $y$ and $z$ correspond to maximal ideals $p \subset B$ and $q \subset C$,
the fields $B/p$ and $C/q$ are of finite degree over $\kappa(s)$, and so $(B/p) \otimes_{\kappa(s)} (C/q)$ is a
$\kappa(s)$-algebra of finite dimension, whose maximal ideals correspond exactly to the points of $X_{0} \times_{S}
X_{0}$ whose second (resp. first) projection is $z$ (resp. $y$). There are therefore only finitely many points $u$ of
$X_{0} \times_{S} X_{0}$ whose

<!-- original page 280 -->

second projection is $z$ and whose first projection belongs to $\tilde{d}_{0}(\tilde{d}^{-1}_{1}(z))$. Finally, since
$X_{1} \to X_{0} \times_{S} X_{0}$ has finite fibers, such a point $u$ comes from finitely many points of $X_{1}$,
whence the desired assertion.

The morphism $\tilde{d}_{1}$ is therefore quasi-finite and flat at the points of $F_{1}$ above $z$. Since
$\tilde{d}_{1}$ is of finite type, it follows from SGA 1, IV 6.10 and EGA III, 4.4.10,[^N.D.E-V-40] that the set $\Phi$
of points of $F_{1}$ where $\tilde{d}_{1}$ is not simultaneously flat and quasi-finite is closed in $F_{1}$, hence in
$X_{1}$ (since $F_{1}$ is closed in $X_{1}$). Since $d_{1}$ is proper, $\tilde{d}_{1}(\Phi)$ is closed, and does not
contain $z$ by what precedes. Put $W = \tilde{d}_{1}(F_{1}) - \tilde{d}_{1}(\Phi)$. Then the restriction of
$\tilde{d}_{1}$ to $\tilde{d}^{-1}_{1}(W)$ is[^N.D.E-V-41] of finite presentation (in view of the Noetherian
hypotheses), flat, proper and quasi-finite, hence finite, locally free, and open, by EGA III, 4.4.2, and EGA IV_2,
2.1.12 and 2.4.6. Consequently, $\tilde{d}_{1}(F_{1})$ is a neighborhood of $z$, and $W$ is the largest open of $X_{0}$
contained in $\tilde{d}_{1}(F_{1})$ above which $\tilde{d}_{1}$ is simultaneously flat and quasi-finite.

We shall see in lemma 7.4 that the inverse images of $\Phi$ by $\tilde{d}'_{1}$ and $\tilde{d}'_{0}$ both identify with
the set of points of $F_{2}$ where $\tilde{d}'_{2}$ is not simultaneously flat and quasi-finite. It follows that
$d^{-1}_{0}(W) = \tilde{d}'_{2}(F_{2}) - \tilde{d}'_{2}(\tilde{d}'_{0} \Phi)$ coincides with $d^{-1}_{1}(W) =
\tilde{d}'_{2}(F_{2}) - \tilde{d}'_{2}(\tilde{d}'_{1} \Phi)$, that is, $W$ is saturated. Consequently, setting $W_{1} =
\tilde{d}^{-1}_{1}(W)$, the equality $d^{-1}_{0}(W) = d^{-1}_{1}(W)$ entails $\tilde{d}'_{2} \tilde{d}'^{-1}_{0}(W) =
\tilde{d}'_{2} \tilde{d}'^{-1}_{1}(W)$, that is, $\tilde{d}'^{-1}_{0}(W_{1}) = \tilde{d}'^{-1}_{1}(W_{1})$. Since
$\tilde{d}_{0}$ is faithfully flat and quasi-compact (because $d_{0}$ is, like $d_{1}$, surjective, proper and flat),
and the square

```text
              d̃′₁
       F₂ ─────→ F₁
       │          │
   d̃′₀│          │ d̃₀
       ↓          ↓
       F₁ ─────→ F
              d̃₀
```

is Cartesian, it follows that $W_{1}$ is of the form $\tilde{d}^{-1}_{0}(U)$, where $U$ is an open of $F$

<!-- original page 281 -->

(SGA 1, VIII 4.4). This open $U$ of $F$ is a quasi-section for the groupoid with base $W$ induced by $X\ast$. One can
therefore choose $U_{z}$ equal to $W$.

It remains for us therefore to state lemma 7.4, whose proof is classical:

**Lemma 7.4.** *Consider a Cartesian square of schemes*

<!-- label: III.V.7.4 -->

```text
   F₂ ──v──→ F₁
   │           │
d′ │           │ d
   ↓           ↓
   X₁ ──u──→ X₀
```

*and let $x$ be a point of $F_{2}$.*

*(i) If $u$ is flat, $d'$ is flat at $x$ if and only if $d$ is flat at $v(x)$.*

*(ii) If $d$ is locally of finite type, $d'$ is quasi-finite at $x$ if and only if $d$ is quasi-finite at
$v(x)$.*[^N.D.E-V-42]

We have thus proved that there exists a covering of $X_{0}$ by saturated opens $W$ such that the groupoid $W\ast$
induced by $X\ast$ on $W$ possesses a quasi-section.[^N.D.E-V-43]

By lemma 6.1 and the reductions stated after theorem 7.1, this implies assertions (i) and (iii) of theorem 7.1, and the
fact that $p$ is surjective and open, and that $p$ and $Y \to S$ are locally of finite presentation. Moreover, since
$X_{0} \to S$ is quasi-projective, hence separated and of finite type, then $p$ is separated, and the proof of point
(ii) of lemma 6.1 shows that $p$ and $Y \to S$ are of finite presentation.

To show that $p$ is proper, it remains therefore to show that it is universally closed. As the assertion is local on
$Y$, one may place oneself on a saturated open $W$ such that the groupoid $W\ast$ induced by $X\ast$ on $W$ possesses a
quasi-section $U$ (since $X_{0}$ is covered by such opens). Taking up the notations of 6.a), one has a commutative
diagram

```text
   W ←─v── V ──u──→ U
       ↘        ↙
        r     q
         ↘ ↙
          Z,
```

where $Z$ is an open of $Y$, all the arrows are surjective, and $q$ is integral. Moreover, by hypothesis, $d_{0} : X_{1}
\to X_{0}$ is proper, so $u$, obtained from it by base change, is also. Consequently, $r$ is universally closed, and so
is $p$, since $v$ is surjective.

Finally, $p$ being surjective and universally closed, and $X_{0}$ quasi-projective hence separated, the diagonal
$\Delta_{Y/S}(Y)$ is closed in $Y \times_{S} Y$, being the image under $p \times p$ of the diagonal
$\Delta_{X_{0}/S}(X_{0})$. So $Y$ is separated over $S$. This completes the proof of 7.1 (ii).

The assertions to prove in 7.1 (iv) are local on $Y$; since $X_{0}$ is covered by the saturated opens $U_{z}$, it
suffices to verify these assertions by replacing $X$ and $Y$ by $U_{z}$ and $V = p(U_{z})$. As one has already seen at
the beginning of the proof of 7.1, it follows from lemmas 1.1, 1.2, and 6.1 (i), that $(V_{z}, p|_{U_{z}})$ is the
cokernel in `(Sch)` and in `(Esp.An)` of the groupoid induced by $X\ast$ on $U_{z}$. Now the hypothesis that

<!-- original page 282 -->

$d = (d_{0}, d_{1})$ is a monomorphism is preserved by the base change $U_{z} \to X_{0}$. Consequently, the first two
assertions of 7.1 (iv) follow from 6.1 (iv).

Let us finally show the consequences indicated at the end of point (iv) (cf. [Ray67a], th. 1 (iii)). By hypothesis, the
groupoid $X\ast$ comes from an equivalence relation $R \to X_{0} \times X_{0}$, and one has established that $R$ is
effective (cf. Exp. IV, 3.3.2) and that $p : X_{0} \to Y = X_{0}/R$ is faithfully flat and of finite presentation.
Consequently, denoting by `(M)` the family of faithfully flat morphisms locally of finite presentation, $R$ is
`(M)`-effective. Therefore, by Exp. IV, 6.3.3, $(Y, p)$ represents the quotient sheaf of $X_{0}$ by $R$ for the (fppf)
topology, and the assertions concerning base change follow from IV, 3.4.3.1.

## 8. Passage to the quotient by a flat, not necessarily proper, groupoid

<!-- label: III.V.8 -->

**Theorem 8.1.**[^N.D.E-V-44] *Let $S$ be a Noetherian scheme and*

<!-- label: III.V.8.1 -->

```text
        d′₀, d′₁, d′₂      d₀, d₁
   X₂ ⇶ X₁ ⇉ X₀
```

*a $(Sch/S)$-groupoid such that $d_{1}$ is flat and of finite type, $X_{0}$ is of finite type over $S$, and the morphism
$X_{1} \to X_{0} \times_{S} X_{0}$ with components $d_{0}$ and $d_{1}$ is quasi-finite.*

<!-- original page 282 -->

*There then exists an open $W$ of $X_{0}$ which is dense, saturated, and satisfies the following properties:*

*(i) If `W₂ ⇶ W₁ ⇉ W` (with arrows $w'_{i}, w_{j}$) is the groupoid induced by $X\ast$ on $W$, then $(w_{0}, w_{1})$
admits a cokernel $(V, p)$ in $(Sch/S)$; moreover, $(V, p)$ is a cokernel of $(w_{0}, w_{1})$ in the category of all
ringed spaces.*

*(ii) $p$ is surjective and open.*

*(ii′) $p$ and $V \to S$ are of finite presentation.*

*(iii) The morphism $W_{1} \to W \times_{V} W$ with components $w_{0}$ and $w_{1}$ is surjective.*

*(iv) If $(d_{0}, d_{1})$ is an equivalence pair, $W_{1} \to W \times_{V} W$ is an isomorphism and $p$ is faithfully
flat.*

<!-- original page 280 -->

We shall show that one can choose $W$ in such a way that the $(Sch/S)$-groupoid $W\ast$ induced by $X\ast$ possesses a
quasi-section (confer § 7). Theorem 8.1 will then follow from lemma 6.1.

Suppose provisionally that, for every point $z \in X_{0}$ closed relative to $S$ (confer § 7), there exists a saturated
open $W_{z}$ which possesses a quasi-section and meets all the irreducible components of $X_{0}$ passing through $z$.
Then the exterior $X_{0} - W_{z}$ of $W_{z}$ in $X_{0}$ is saturated (since the saturation $d_{1}(d^{-1}_{0}(X_{0} -
W_{z}))$ of this exterior is open and does not meet $W_{z}$). If this exterior is non-empty, one can choose in it a
point $z'$ closed relative to $S$ and associate to $z'$ an open $W_{z'}$ as above; one may moreover suppose $W_{z'}$
contained in $X_{0} - W_{z}$; then $W_{z}$ and $W_{z'}$ are disjoint and the groupoid induced by $X\ast$ on $W_{z} \cup
W_{z'}$ possesses a quasi-section. The process must stop, because $X_{0}$ has only finitely many irreducible components.
It therefore remains to construct $W_{z}$.

For this, one may suppose $S$ affine; in this case, let $y$ be a point of $X_{1}$

<!-- original page 283 -->

such that $d_{1}(y) = z$, $X$ an affine open of $X_{0}$ containing $d_{0}(y)$, $Y$ the inverse image of $X$ in $X_{1}$
under $d_{0}$, and finally $u : Y \to X$ and $v : Y \to X_{0}$ the morphisms induced by $d_{0}$ and $d_{1}$. Since $X$
is affine, hence quasi-projective, one can apply lemma 7.2: there is therefore a closed subscheme $F$ of $X_{0}$ such
that $d^{-1}_{0}(F) \cap d^{-1}_{1}(z)$ is non-empty, $d_{0}(d^{-1}_{0}(F) \cap d^{-1}_{1}(z))$ is finite, and the
restriction of $d_{1}$ to $d^{-1}_{0}(F)$ is flat at the points of $v^{-1}(z)$. This allows us to take up the notations
of lemma 7.3, denoting by $F_{1}$ and $F_{2}$ the inverse images of $F$ in $X_{1}$ and $X_{2}$, etc.

```text
                d̃′₁              d̃₀
        F₂ ─────→ F₁ ─────→ F
                d̃′₀
    d̃′₂│         │ d̃₁
        ↓         ↓
        X₁ ─────→ X₀.
                d₁
                d₀
```

One then shows as in 7.3 that $\tilde{d}_{1}$ is quasi-finite at the points of $\tilde{d}^{-1}_{1}(z)$, so that it is
natural to consider the open $F'_{1}$ of $F_{1}$ consisting of points where $\tilde{d}_{1}$ is simultaneously flat and
quasi-finite. By 7.4, the two inverse images of $F'_{1}$ under $\tilde{d}'_{1}$ and $\tilde{d}'_{0}$ consist of the
points of $F_{2}$ where $\tilde{d}'_{2}$ is flat and quasi-finite, so these two inverse images coincide, and $F'_{1}$ is
of the form $\tilde{d}^{-1}_{0}(F')$, where $F'$ is an open of $F$

(SGA 1, VIII 4.4). Possibly replacing $F$ by $F'$, one may therefore suppose that $\tilde{d}_{1}$ is quasi-finite and
flat. In this case, we denote by $W_{z}$ the largest open of $\tilde{d}_{1}(F_{1})$ above which $\tilde{d}_{1}$ is
finite and flat.

This open $W_{z}$ does not necessarily contain $z$, but it contains the generic points of the irreducible components of
$X_{0}$ passing through $z$.[^N.D.E-V-45] Since $d_{0}$ (resp. $d_{1}$) is faithfully flat and of finite presentation
(hence open), it then follows from SGA 1, VIII 5.7, that $d^{-1}_{0}(W_{z})$ and $d^{-1}_{1}(W_{z})$ both coincide with
the largest open of $\tilde{d}'_{2}(F_{2})$ above which $\tilde{d}'_{2}$ is finite and flat. One sees consequently as in
7.3 that the two inverse images of $\tilde{d}^{-1}_{1}(W_{z})$ under $\tilde{d}'_{0}$ and $\tilde{d}'_{1}$ coincide, so
that $\tilde{d}^{-1}_{1}(W_{z})$ is of the form $\tilde{d}^{-1}_{0}(U)$ where $U$ is an open of $F$ which is a
quasi-section for the groupoid induced by $X\ast$ on $W_{z}$.

## 9. Elimination of the Noetherian hypotheses in theorem 7.1

<!-- label: III.V.9 -->

<!-- original page 284 -->

**a)** We take up the notations and hypotheses of lemma 6.1 and let $\pi : S' \to S$ be an arbitrary base change. Denote
by $f' : X' \to Y'$ the morphism of $S'$-schemes deduced by extension via $\pi$ of the base from a morphism of
$S$-schemes $f : X \to Y$. With this convention, $p' : X'_{0} \to Y'$ is surjective, as is the morphism $X'_{1} \to
X'_{0} \times_{Y'} X'_{0}$ with components $d'_{0}$ and $d'_{1}$. The set underlying $Y'$ therefore identifies with the
quotient of the set underlying $X'_{0}$ by the equivalence relation defined in $X'_{0}$ by the $S'$-groupoid $X'\ast$.
Moreover, $q' : U' \to Y'$ is integral and surjective, so that the topology of $Y'$ is the quotient topology of that of
$U'$, hence also of that of $X'_{0}$ (confer the proof in § 6.c).

On the other hand, it is clear that $U'$ is a quasi-section of the $S'$-groupoid $X'\ast$, to which one can therefore
apply lemma 6.1. In particular, $X'\ast$ possesses a cokernel $(Y_{1}, p_{1})$ and the topological space underlying
`Y_1` is obtained from the topological space underlying $X'_{0}$ by identifying the points equivalent under the relation
defined by $X'\ast$. It follows that the canonical morphism $Y_{1} \to Y'$ is a homeomorphism; I claim that $Y_{1} \to
Y'$ is even a universal homeomorphism: indeed, if $S''$ is above $S'$, let `Y_2` be the cokernel of $(d_{0} \times_{S}
S'', d_{1} \times_{S} S'')$. By what precedes, applied to the base changes $S'' \to S'$ and $S'' \to S$,

```text
   Y_2 ──→ Y_1 ×_{S′} S′′    and    Y_2 ──→ Y ×_S S′′ ≃ Y′ ×_{S′} S′′
```

are homeomorphisms, so the same holds for $Y_{1} \times_{S'} S'' \to Y' \times_{S'} S''$.

**b)** Analogous remarks evidently apply to the case where the groupoid $X\ast$ "locally" possesses quasi-sections
(confer the proof of theorem 7.1).[^N.D.E-V-46] For example, one has the following theorem:

<!-- original page 285 -->

**Theorem 9.0.** *Let $S$ be an arbitrary scheme and `X₂ ⇶ X₁ ⇉ X₀` a $(Sch/S)$-groupoid (with arrows $d'_{i}$ and
$d_{j}$) such that: $X_{0}$ is of finite presentation and quasi-projective over $S$, $d_{1}$ is of finite presentation,
proper and flat, the morphism $d_{0} \boxtimes d_{1} : X_{1} \to X_{0} \times_{S} X_{0}$ is quasi-finite. Then:*

<!-- label: III.V.9.0 -->

*(1) Every point $x$ of $X_{0}$ has an open neighborhood $W$ that is saturated and such that the groupoid induced by
$X\ast$ on $W$ possesses a quasi-section.*

*(2) Let $(Y, p)$ be the cokernel of $(d_{0}, d_{1})$ in the category of all ringed spaces. Then $Y$ is a scheme, $p$ a
morphism of schemes, and $(Y, p)$ is a cokernel of $(d_{0}, d_{1})$ in $(Sch/S)$.*

*(3) $p$ is surjective, open and universally closed.*

*(4) The morphism $d : X_{1} \to X_{0} \times_{Y} X_{0}$ with components $d_{0}$ and $d_{1}$ is surjective.*

*(5) If $(d_{0}, d_{1})$ is an equivalence pair, then:*

*(a) $d : X_{1} \to X_{0} \times_{Y} X_{0}$ is an isomorphism and $p$ is faithfully flat.*

*(b) $p$ and $Y \to S$ are of finite presentation, and $(Y, p)$ is a cokernel of $(d_{0}, d_{1})$ in the category of
sheaves for the (fppf) topology.*

*Proof.* For (1), the question is local on $S$, so one may suppose $S = \operatorname{Spec} B$ affine. There then exists
a ring $A$ of finite type over $\mathbb{Z}$, a morphism $S \to T = \operatorname{Spec} A$ and a $(Sch/T)$-groupoid
$Z\ast$ such that $X\ast$ identifies with $Z\ast \times_{T} S$ (cf. EGA IV_3, 8.8.3, applied to $S_{0} =
\operatorname{Spec} \mathbb{Z}$ and $S_{i} = \operatorname{Spec} A_{i}$, with the $A_{i}$ running over the finitely
generated $\mathbb{Z}$-subalgebras of $B$). Moreover, one may suppose that $Z\ast$ satisfies the hypotheses of theorem
7.1 (cf. EGA IV_3, 8.10.5). Consequently, $Z\ast$ "locally" possesses quasi-sections.

The same therefore holds for $X\ast$, by a), and assertions (2), (3), (4) and (5) (a) follow from 6.1, as in the proof
of 7.1.

**c)** Let us show that $Y \to S$ is of finite presentation.[^N.D.E-V-47] By hypothesis, $(d^{X\ast}_{0},
d^{X\ast}_{1})$ is an equivalence pair, that is, $d^{X\ast} : X_{1} \to X_{0} \times_{S} X_{0}$ is a monomorphism. By
EGA IV_3, 8.10.5, one may suppose, possibly enlarging $A$, that $d^{Z\ast} : Z_{1} \to Z_{0} \times_{T} Z_{0}$ is a
monomorphism. Since $T = \operatorname{Spec} A$, with $A$ Noetherian, it then follows from theorem 7.1 that the groupoid
$Z\ast$ possesses a cokernel $(Q, q)$ in $(Sch/T)$, that $q$ and $Q \to T$ are of finite presentation, and moreover that
$q : Z_{0} \to Q$ is faithfully flat and that $d^{Z\ast}$ induces an isomorphism $Z_{1} \xrightarrow{\sim} Z_{0}
\times_{Q} Z_{0}$. Put $Q_{S} = Q \times_{T} S$.

Since $X_{i} \cong Z_{i} \times_{T} S$, one therefore obtains an isomorphism:

```text
   d^{Z∗} ×_T S : X₁ ⥲ X₀ ×_{Q_S} X₀.
```

Denote its inverse by $\phi$, and let $\pi$ be the canonical morphism

```text
   X₀ ×_Y X₀ ⟶ X₀ ×_{Q_S} X₀.
```

<!-- original page 283 -->

Then $\phi \circ \pi$ is the inverse of $d_{0} \boxtimes d_{1} : X_{1} \xrightarrow{\sim} X_{0} \times_{Y} X_{0}$. It
follows that the equivalence relation defined by $X\ast$, that is, the monomorphism

```text
   X₁ ──d₀⊠d₁ (≅)──→ X₀ ×_Y X₀ ──→ X₀ ×_S X₀,
```

identifies with the equivalence relation $R(q_{S})$ defined by the morphism $q_{S} : X_{0} \to Q_{S}$. Since the latter
is faithfully flat and of finite presentation, hence a universal effective epimorphism, $R(q_{S})$ has quotient `Q_S`
(cf. IV 3.3.2). Consequently, $Y \cong Q \times_{T} S$, so $Y \to S$ and $p$ are of finite presentation. Moreover, by IV
6.3.3, $(Y, p)$ is also a cokernel of $(d_{0}, d_{1})$ in the category of sheaves for the (fppf) topology.

**Proposition 9.1.** *Consider morphisms of schemes*

<!-- label: III.V.9.1 -->

```text
   X₀ ──p──→ Y ──q──→ S
```

*such that `qp` is of finite type (resp. of finite presentation) and $p$ is faithfully flat of finite presentation. Then
$q$ is of finite type (resp. of finite presentation)[^V-9-1].*

Since $p$ is surjective and `qp` quasi-compact, $q$ is quasi-compact. So one may suppose $S$, $Y$ and $X_{0}$ affine,
with rings $A$, $B$, $C$. One has $B = \lim B_{i}$, where the $B_{i}$ run over the finitely generated $A$-subalgebras of
$B$. Since $C$ is of finite presentation over $B$, there exists an index $i_{0}$, a $B_{i_{0}}$-algebra of finite
presentation $C_{i_{0}}$, and an isomorphism $C \simeq C_{i_{0}} \otimes_{B_{i_{0}}} B$; if we put $C_{i} = C_{i_{0}}
\otimes_{B_{i_{0}}} B_{i}$ for $i \geqslant i_{0}$, we therefore have $C \simeq C_{i} \otimes_{B_{i}} B$.

```text
        B ────→ C
        ↑       ↑
        B_i ──→ C_i
        ↑
        A
```

Since $C$ is faithfully flat over $B$, one extracts from EGA IV_3, 11.2.6 and 8.10.5 (vi) the existence of an $i_{1}
\geqslant i_{0}$ such that $C_{i_{1}}$ is faithfully flat over $B_{i_{1}}$; consequently $C_{i}$ is faithfully flat over
$B_{i}$ for $i \geqslant i_{1}$. For $i \geqslant i_{1}$, the canonical map $C_{i} \to C$ is then injective, since
deduced from $B_{i} \to B$ by faithfully flat extension of the base.

<!-- original page 286 -->

If $C$ is of finite type over $A$, it follows that there exists an index $j \geqslant i_{1}$ such that $C_{j} = C$,
whence $B_{j} = B$, since $C_{j}$ is faithfully flat over $B_{j}$. Consequently, $B$ is of finite type over $A$.

Suppose now $C$ of finite presentation over $A$. By what precedes, $B$ is of finite type over $A$, hence of the form
$\bar{B}/I$ where $\bar{B}$ is a polynomial algebra over $A$ in a finite number of indeterminates, and $I$ an ideal of
$\bar{B}$. Then $I$ is the union of its finitely generated subideals $I_{\alpha}$; whence the equality $B = \lim
B_{\alpha}$ with $B_{\alpha} = \bar{B}/I_{\alpha}$. Proceeding as above, there exists an index $\alpha_{0}$, a
$B_{\alpha_{0}}$-algebra of finite presentation $C_{\alpha_{0}}$, and an isomorphism $C \simeq C_{\alpha_{0}}
\otimes_{B_{\alpha_{0}}} B$. For $\alpha \geqslant \alpha_{0}$, one again sets $C_{\alpha} = C_{\alpha_{0}}
\otimes_{B_{\alpha_{0}}} B_{\alpha}$ so that one has $C \simeq C_{\alpha} \otimes_{B_{\alpha}} B$ for $\alpha \geqslant
\alpha_{0}$. Again by EGA IV_3, 11.2.6 and 8.10.5 (vi), one concludes as above that $C_{\alpha}$ is faithfully flat over
$B_{\alpha}$ for $\alpha$ large enough. In this case, the kernel of the map $C_{\alpha} \to C$ (resp. $C_{\alpha} \to
C_{\beta}$ for $\beta \geqslant \alpha$) identifies with $C_{\alpha} \otimes_{B_{\alpha}} (I/I_{\alpha})$ (resp. with
$C_{\alpha} \otimes_{B_{\alpha}} (I_{\beta}/I_{\alpha})$).

Since $C_{\alpha}$ and $C$ are of finite presentation over $A$ and $C_{\alpha} \to C$ is surjective, $C_{\alpha}
\otimes_{B_{\alpha}} (I/I_{\alpha})$ is a finitely generated ideal[^N.D.E-V-48] and is the union of the ideals
$C_{\alpha} \otimes_{B_{\alpha}} (I_{\beta}/I_{\alpha})$. One therefore has $C_{\alpha} \otimes_{B_{\alpha}}
(I_{\beta}/I_{\alpha}) = C_{\alpha} \otimes_{B_{\alpha}} (I/I_{\alpha})$ for $\beta$ large enough, whence also
$I_{\beta} = I$ (since $C_{\alpha}$ is faithfully flat over $B_{\alpha}$); so $B$ is of finite presentation over $A$.

## 10. Complement: quotients by a group scheme

<!-- label: III.V.10 -->

The following §§ 10.2–10.4, written following indications of M. Raynaud, aim to apply the preceding theorems to the case
of an action of a group scheme. For the reader's convenience, we have begun by reproducing, in § 10.1, statements 2.1 to
2.3 of Exp. XVI.

### 10.1. Representability theorems for quotients.

<!-- label: III.V.10.1 -->

"Recall" first the following result:

**Theorem 10.1.1.** *Let $S$ be a scheme, $X$ and $Y$ two $S$-schemes, $f : X \to Y$ an $S$-morphism. Suppose that one
is in one of the following two cases:*

<!-- label: III.V.10.1.1 -->

*α) The morphism $f$ is locally of finite presentation.*

*β) The scheme $S$ is locally Noetherian and $X$ is locally of finite type over $S$.*

*Then the following conditions are equivalent:*

*(i) There exists an $S$-scheme $X'$ and a factorization of $f$:*

```text
   f : X ──f′──→ X′ ──f′′──→ Y,
```

*where $f'$ is a faithfully flat $S$-morphism locally of finite presentation and $f''$ is a monomorphism.*

*(ii) The (first) projection:*

```text
   p_1 : X ×_Y X ⟶ X
```

*is a flat morphism.*

*Moreover, if the preceding conditions are realized, $(X', f')$ is a quotient of $X$ by the equivalence relation defined
by $f$ (for the (fppf) topology), so that the factorization $f = f'' \circ f'$ of i) is unique up to isomorphism.*

The case $Y$ locally Noetherian, $X$ of finite type over $Y$, is treated in [Mur65], cor. 2 of th. 2. We shall see that
one can reduce to this case.

Let us first make a few remarks:

<!-- original page 285 -->

**a)** The implication (i) ⇒ (ii) is trivial. Indeed, the first projection

```text
   p′_1 : X ×_{X′} X ⟶ X
```

factors through $X \times_{Y} X$:

```text
   p′_1 : X ×_{X′} X ──u──→ X ×_Y X ──p_1──→ X.
```

The morphism $u$ is an isomorphism, since $f''$ is a monomorphism, and $p'_{1}$ is flat, since $f'$ is flat, so $p_{1}$
is flat.

**b)** The assertions of 10.1.1 are local on $Y$ (hence local on $S$); they are also local on $X$, as follows easily
from the fact that a flat morphism locally of finite presentation is open (EGA IV_3, 11.3.1).

**c)** Under the hypotheses of 10.1.1 α), in view of what precedes, we are reduced to the case where $X$ and $Y$ are
affine and $f$ of finite presentation. Possibly replacing $S$ by $Y$, one may suppose $X$ and $Y$ of finite presentation
over $S$. One then reduces to the case $S$ Noetherian thanks to EGA IV_3, 11.2.6.

**d)** Under the hypotheses of 10.1.1 β), one may suppose $S$, $X$, $Y$ affine, $S$ Noetherian and $X$ of finite type
over $S$. Consider $Y$ as filtered inverse limit of affine schemes $Y_{i}$ of finite type over $S$. The schemes $X
\times_{Y_{i}} X$ form a filtered decreasing family of closed subschemes of $X \times_{S} X$, whose inverse limit is $X
\times_{Y} X$. Since $X \times_{S} X$ is Noetherian, one has $X \times_{Y_{i}} X = X \times_{Y} X$ for $i$ large enough,
so that $f_{i} : X \to Y \to Y_{i}$ satisfies the hypotheses of 10.1.1 ii) if $f$ does. Since the equivalence relation
defined by $f$ on $X$ coincides with that defined by $f_{i}$, it is clear that it suffices to prove ii) ⇒ i) for
$f_{i}$, which reduces us to the case where $Y$ is of finite type over $S$.

*Application to group schemes.* Let $S$ be a scheme, $G$ an $S$-group scheme locally of finite presentation over $S$,
acting (on the left) on an $S$-scheme $X$. If $X \to S$ possesses a section $\xi$, recall that the stabilizer
$Stab_{G}(\xi)$ is representable by a subgroup scheme of $G$ (cf. I, 2.3.3).

**Theorem 10.1.2.** *Let $S$ be a scheme, $G$ an $S$-group scheme locally of finite presentation over $S$, acting on an
$S$-scheme $X$.*

<!-- label: III.V.10.1.2 -->

*One assumes that $X \to S$ possesses a section $\xi$, such that the stabilizer $H$ of $\xi$ in $G$ is flat over $S$. If
one of the following hypotheses is satisfied:*

*a) $X$ is locally of finite type over $S$,*

*b) $S$ is locally Noetherian,*

*then the quotient (fppf) sheaf $G/H$ is representable by an $S$-scheme, locally of finite presentation over $S$, and
the $S$-morphism:*

```text
   f : G ⟶ X,   g ↦ g · ξ
```

<!-- original page 286 -->

*factors as:*

```text
        G
        │  ↘ f
      p │    ↘
        ↓      ↘
       G/H ──i──→ X,
```

*where $p$ is the canonical projection, which is a faithfully flat morphism locally of finite presentation, and $i$ is a
monomorphism.*

*Proof.* The morphism $f$ makes $G$ an $X$-scheme. By definition of the stabilizer of $\xi$, the morphism:

```text
   G ×_S H ⟶ G ×_X G,   (g, h) ↦ (g, gh)
```

is an isomorphism. Since $H$ is flat over $S$, $G \times_{S} H$ is flat over $G$, so the first projection $p_{1} : G
\times_{S} G \to G$ is a flat morphism. Moreover, if $X$ is locally of finite type over $S$, $f$ is locally of finite
presentation (EGA IV_1, 1.4.3 (v)), and otherwise $S$ is assumed locally Noetherian. It then suffices to apply 10.1.1 to
the morphism $f$. It remains to see that $G/H$ is locally of finite presentation over $S$, but this follows immediately
from 9.1.

**Corollary 10.1.3.** *Let $S$ be a scheme, $u : G \to H$ a morphism of $S$-group schemes. Suppose $G$ locally of finite
presentation over $S$ and that either $H$ is locally of finite type over $S$, or $S$ is locally Noetherian.*

<!-- label: III.V.10.1.3 -->

*Then, if $K = Ker(u)$ is flat over $S$, the quotient group $G/K$ is representable by an $S$-group scheme locally of
finite presentation over $S$, and $u$ factors as:*

```text
        G ──u──→ H
        │       ↗
      p │      ↗
        ↓     ↗ i
       G/K
```

*where $p$ is the canonical projection and $i$ a monomorphism.*

*Proof.* One applies 10.1.2 taking $X = H$ and for $\xi$ the unit section of $H$.

### 10.2. Stabilizer of the diagonal.

<!-- label: III.V.10.2 -->

Let $S$ be a Noetherian scheme, $X$ an $S$-scheme of finite type, and $G$ a flat $S$-group scheme of finite type acting
on the left on $X$, i.e., one has an $S$-action $d_{0} : G \times_{S} X \to X$. Denote by $d_{1} : G \times_{S} X \to X$
the projection onto the second factor. Following § 2.a), one has the groupoid

```text
                  pr_{2,3}              d₁
   G ×_S G ×_S X      ⇉      G ×_S X         ⇉   X
                  μ × X                       d₀
                  G × d₀
```

whose cokernel, if it exists, is denoted $G\backslash X$.

<!-- original page 287 -->

**Definition 10.2.1.** *We denote by $F \subset G \times_{S} X$ the* stabilizer of the diagonal section, *i.e. the
$X$-scheme defined by the Cartesian product*

<!-- label: III.V.10.2.1 -->

```text
   F ─────→ X
   │         │ Δ
   ↓         ↓
   G ×_S X ──(d₀, d₁)──→ X ×_S X.
```

*Then $F$ is an $X$-subgroup scheme of $G \times_{S} X$. Since $G \times_{S} X$ is of finite type over $S$ Noetherian,
hence Noetherian, $F$ is of finite type over $S$ and over $X$ (EGA I, 6.3.5 and 6.3.6). Moreover, if $X \to S$ is
separated, $F$ is a closed $X$-subgroup scheme of $G \times_{S} X$.*

Recall that one says that $G$ *acts freely* on $X$ if the morphism

```text
   G ×_S X ──(d₀, d₁)──→ X ×_S X
```

is a monomorphism (cf. Exp. III, 3.2.1). This amounts to saying that $F$ is the trivial group scheme with base $X$.

### 10.3. Case where $F$ is quasi-finite over $X$.

<!-- label: III.V.10.3 -->

Since $F$ is of finite type over $X$, it is quasi-finite over $X$ if and only if the fixators of the geometric points of
$X$ are finite.

**Theorem 10.3.1.**[^N.D.E-V-49] *Under the hypotheses of 10.2, suppose that $F$ is quasi-finite over $X$. Then there
exists an open $U$ of $X$, dense and $G$-saturated, satisfying the following properties:*

<!-- label: III.V.10.3.1 -->

*(i) In $(Sch/S)$, the cokernel $V = G\backslash U$ exists; moreover, the scheme $V$ is a quotient in the category of
ringed spaces.*

*(ii) $p : U \to V$ is surjective, open, and of finite presentation.*

*(iii) $V$ is of finite presentation over $S$.*

*(iv) The morphism $G \times_{S} U \to U \times_{V} U$, $(g, x) \mapsto (gx, x)$, is surjective.*

*(v) Suppose in addition that $G$ acts freely on $X$. Then $U \to V$ is a (left) $G$-torsor locally trivial for the
(fppf) topology. In particular, $U \to V$ is faithfully flat.*[^N.D.E-V-50]

*Proof.* It is assumed that the morphism $G \times_{S} X \to X \times_{S} X$, $(g, x) \mapsto (gx, x)$, is quasi-finite.
Theorem 8.1 therefore applies to the groupoid defined by $(X, G)$. Thus there exists a dense saturated open $U \subset
X$ such that the quotient $G\backslash U$ exists; it satisfies properties (i), (ii), (iii).

<!-- original page 288 -->

To establish (iv), recall that $G$ acts freely on $X$ if and only if $(d_{0}, d_{1})$ is an equivalence pair (III
3.2.1). In this case, theorem 8.1 (iv) shows that the morphism $G \times_{S} U \to U \times_{V} U$ is an isomorphism and
that $p$ is faithfully flat and of finite presentation. Thus $U$ is a $G$-torsor with base $V$, locally trivial for the
(fppf) topology.

### 10.4. Case where $F$ is flat over $X$.

<!-- label: III.V.10.4 -->

We denote

```text
   d = (d₀, d₁) : G ×_S X ⟶ X ×_S X
```

the morphism $d(g, x) = (gx, x)$. Recall that the sheaf-theoretic graph $\tilde{\Gamma}$ of the equivalence relation
associated with $(X, G)$ is the (fppf) $S$-subsheaf of $X \times_{S} X$ image of $(d_{0}, d_{1})$. It is the (fppf)
sheaf associated to the graph functor:

```text
   T ↦ Γ(T) = {(x₀, x₁) ∈ X(T) × X(T) | x₀ ∈ G(T) x₁}.
```

Set $G_{X} = G \times_{S} X$. For every $S$-scheme $T$, one has a surjective map

```text
   G_X(T) ⟶ Γ(T),   (g, x) ↦ (gx, x),
```

which induces a bijective map

$$ \phi(T) : G_{X}(T)/F(T) \xrightarrow{\sim} \Gamma(T); $$

indeed, if $(g, x), (g', x') \in G_{X}(T)$ satisfy $(gx, x) = (g' x', x')$, then $x' = x$ and $g^{-1} g' x = x$, so
$(g^{-1} g' x, x) \in F(T)$ and $(g, x)$ and $(g', x)$ have the same image in $G_{X}(T)/F_{X}(T)$.

By definition (cf. IV, 4.4.1 (ii) or proof of 5.2.1), the quotient sheaf $G_{X}/F$ is the (fppf) sheaf associated to the
presheaf

$$ T \mapsto G_{X}(T)/F(T) \cong \Gamma(T). $$

One therefore has an isomorphism of sheaves $\phi : G_{X}/F \to \tilde{\Gamma}$.

**Theorem 10.4.1.**[^N.D.E-V-51] *Under the hypotheses of 10.2, one has:*

<!-- label: III.V.10.4.1 -->

*a) $\tilde{\Gamma}$ is representable if and only if $F$ is flat over $X$.*

*b) Suppose $F$ flat over $X$. Then the morphisms induced by $d_{1}$ and $d_{0}$:*

```text
   G_X/F   ⇉   X
        d₀ ↓↑ d₁
```

*are faithfully flat and of finite presentation.*

<!-- original page 289 -->

*Proof of a):* Suppose the (fppf) sheaf $G_{X}/F$ representable by an $X$-scheme $Y$. Then, by IV 6.3.3, $p : G_{X} \to
Y$ is faithfully flat and locally of finite presentation, and the second square of the diagram below is Cartesian:

```text
   F ────→ F ×_X G_X ────→ G_X
   │                            │ p
   ↓                            ↓
   X ──e_X──→ G_X ──────────→ Y,
```

the first square being obtained by base change along the unit section $e_{X} : X \to G_{X}$. Since $p$ is faithfully
flat and locally of finite presentation, so is $F \to X$.

Conversely, suppose $F$ flat over $X$. Put $X_{2} = X \times_{S} X$. The morphism $d : G_{X} \to X_{2}$ allows one to
form the fiber product:

```text
   G_X ×_{X_2} G_X ────→ G_X
        │                 │
        ↓                 ↓
       G_X ────────────→ X_2.
```

Then the morphism $G_{X} \times_{X_{2}} G_{X} \to X_{2}$ is an $F \times_{X} X_{2}$-torsor over `X_2`, and is therefore
flat and of finite type (since $F$ is). By theorem 10.1.1, the morphism $d$ factors uniquely:

```text
   G_X ──ψ──→ Y ──τ──→ X ×_S X,
```

where $\psi$ is faithfully flat (of finite type) and $\tau$ is a monomorphism of schemes.

Consequently, the morphism of sheaves $\psi : G_{X} \to Y$ is therefore $F$-invariant, and there comes a morphism of
sheaves $\bar{\psi} : G_{X}/F \to Y$. Moreover, since $\psi$ is faithfully flat (of finite type), the monomorphism of
sheaves $\tau$ factors through the sheaf image of $d$, that is $\tilde{\Gamma}$. The isomorphism of sheaves $G_{X}/F
\cong \tilde{\Gamma}$ therefore factors through the monomorphism $Y \to \tilde{\Gamma}$. One concludes that $Y$
represents $G_{X}/F$.

*Proof of b):* Suppose $F$ flat over $X$. Then, by a) and its proof, $G_{X}/F$ is representable, and the morphism $p :
G_{X} \to G_{X}/F$ is faithfully flat and of finite presentation. On the other hand, the morphisms $d_{i} : G_{X} \to X$
($i = 0, 1$) are faithfully flat and of finite presentation by hypothesis. Since $d_{i} = \bar{d}_{i} \circ p$, it
follows from EGA IV_2, 2.2.13 (iii) and EGA IV_3, 11.3.16, that $\bar{d}_{i}$ is faithfully flat and of finite
presentation.

**Theorem 10.4.2.**[^N.D.E-V-52] *Under the hypotheses of 10.2, suppose $F$ flat over $X$. Then there exists a dense
saturated open $U$ of $X$ such that the (fppf) quotient $V = G\backslash U$ is an $S$-scheme of finite type and $U \to
V$ is faithfully flat and of finite presentation.*

<!-- label: III.V.10.4.2 -->

<!-- original page 290 -->

*Proof.* Theorem 10.4.1 shows that $G_{X}/F \cong \tilde{\Gamma}$ is representable. Then the (fppf) sheaf $G\backslash
X$ identifies with the quotient sheaf of

```text
                  d̄₁
   G_X/F     ⇉    X.
                  d̄₀
```

By what precedes, $\bar{d}_{i} : G_{X}/F \to X$ is faithfully flat and of finite presentation ($i = 0, 1$), and the
morphism

```text
   G_X/F ──≅──→ Γ̃ ────→ X ×_S X
```

is a monomorphism, that is, $(\bar{d}_{0}, \bar{d}_{1})$ is an equivalence pair. Consequently, theorem 8.1 applies.
There therefore exists an open $U$ of $X$, dense and saturated, such that the (fppf) quotient $V = G\backslash U$ is an
$S$-scheme of finite type, and $U \to V$ is faithfully flat and of finite presentation.

Taking into account the generic flatness theorem (EGA IV_2, 6.9.3), one obtains the

**Corollary 10.4.3.** *Under the hypotheses of 10.2, suppose $X$ reduced. Then there exists a dense saturated open $U$
of $X$ such that the (fppf) quotient $G\backslash U$ is an $S$-scheme of finite type and $U \to G\backslash U$ is
faithfully flat and of finite presentation.*

<!-- label: III.V.10.4.3 -->

## Bibliography

[^N.D.E-V-53]

[AK80] A. B. Altman, S. L. Kleiman, *Compactifying the Picard Scheme*, Adv. Math. **35** (1980), 50–112.

[An73] S. Anantharaman, *Schémas en groupes, espaces homogènes et espaces algébriques sur une base de dimension 1*, Mém.
Soc. Math. France **33** (1973), 5–79.

[BLR90] S. Bosch, W. Lütkebohmert, M. Raynaud, *Néron models*, Springer-Verlag, 1990.

[CTS79] J.-L. Colliot-Thélène, J.-J. Sansuc, *Fibrés quadratiques et composantes connexes réelles*, Math. Ann. **244**
(1979), 105–134.

[DG70] M. Demazure, P. Gabriel, *Groupes algébriques*, Masson & North-Holland, 1970.

[DR81] J. Dixmier, M. Raynaud, *Sur le quotient d'une variété algébrique par un groupe algébrique*, pp. 327–344 in:
*Mathematical Analysis and Applications* (L. Schwartz 65th birthday, ed. L. Nachbin), Adv. Math. Suppl. Stud., Vol. 7A,
1981\.

[Fe03] D. Ferrand, *Conducteur, descente et pincement*, Bull. Soc. Math. France **131** (2003), no. 4, 553–585.

[Hi62] H. Hironaka, *An example of a non-Kählerian complex analytic deformation of Kählerian complex structures*, Ann.
of Math. **75** (1962), no. 1, 190–208.

<!-- original page 291 -->

[KM97] S. Keel, S. Mori, *Quotient by groupoids*, Ann. of Math. **145** (1997), no. 1, 193–213.

[Ko97] J. Kollár, *Quotient spaces modulo algebraic groups*, Ann. of Math. **145** (1997), no. 1, 33–79.

[Ko08] J. Kollár, *Quotients by finite equivalence relations*, arXiv: 0812.3608.

[Mum65] D. Mumford, *Geometric invariant theory*, Springer-Verlag, 1965; 2nd (resp. 3rd) ed. with J. Fogarty (resp. and
F. Kirwan), 1982 (resp. 1994).

[Mur65] J. P. Murre, *Representation of unramified functors. Applications* (according to unpublished results of A.
Grothendieck), Sém. Bourbaki, Vol. 9, Exp. 294 (1965), Soc. Math. France, 1995.

[Ray67a] M. Raynaud, *Passage au quotient par une relation d'équivalence plate*, pp. 78–85 in: *Proc. Conf. Local Fields
(Driebergen)* (ed. T. A. Springer), Springer-Verlag, 1967.

[Ray67b] M. Raynaud, *Sur le passage au quotient par un groupoïde plat*, C. R. Acad. Sci. Paris (Sér. A) **265** (1967),
384–387.

<!-- LEDGER DELTA — Exposé V — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| pré-relation d'équivalence | pre-equivalence relation | Gabriel's coinage; preserve hyphen and the term, since the Exposé constructs quotients for these. |
| couple d'équivalence | equivalence pair | A pair `(d₀, d₁) : X₁ → X₀` whose `d₀ ⊠ d₁` is, on `T`-points, the graph of an equivalence relation on `X₀(T)`. |
| conoyau | cokernel | Standard categorical sense (coequalizer of the double arrow). |
| diagramme exact | exact diagram | For a coequalizer diagram in the sense of §1.a). |
| flèche | arrow | Reserved for category-theoretic morphisms in §1; "morphism" used when the source is a scheme morphism. |
| espace annelé | ringed space | Standard. The category is written `(Esp.An)`. |
| `(Esp.An)` | `(Esp.An)` | Source notation preserved (category of ringed spaces). |
| saturé | saturated | Of an open set, for a given groupoid/equivalence relation. |
| quasi-section | quasi-section | Gabriel's technical term; do not translate. |
| fini localement libre | finite locally free | Of a morphism of schemes. |
| fidèlement plat et quasi-compact | faithfully flat and quasi-compact | Standard. |
| épimorphisme effectif (universel) | (universal) effective epimorphism | Standard. |
| changement de base | base change | Standard. |
| produit fibré | fiber product | American spelling. |
| application source / but / composition | source / target / composition map | Standard groupoid terminology. |
| flèche identique | identity arrow | Standard. |
| relation d'équivalence effective | effective equivalence relation | As in Exp. IV 3.3.2. |
| schéma quasi-projectif | quasi-projective scheme | Standard. |
| morphisme entier | integral morphism | Standard. |
| polynôme caractéristique | characteristic polynomial | Standard. |
| Hamilton-Cayley | Hamilton–Cayley | En-dash between author names. |
| Cohen-Seidenberg | Cohen–Seidenberg | En-dash between author names. |
| Lemme d'évitement des idéaux premiers | Prime Avoidance Lemma | Standard English phrase. |
| « la formation du quotient commute au changement de base » | "the formation of the quotient commutes with base change" | Translate guillemets to quotation marks. |
| fermé relativement à `S` | closed relative to `S` | Gabriel's standing phrase for "closed in its fiber over `S`". |
| anneau semi-local | semilocal ring | One word, American. |
| anneau local artinien | Artinian local ring | Standard. |
| stabilisateur de la section diagonale | stabilizer of the diagonal section | Standard. |
| graphe faisceautique | sheaf-theoretic graph | Per IV. |
| schéma en groupes réductifs | reductive group scheme | Standard. |
| `G`-torseur | `G`-torsor | Standard. |
| linéarisable | linearizable | Standard. |
| théorème de platitude générique | generic flatness theorem | Standard (EGA IV_2 6.9.3). |
| schéma fini | finite scheme | Standard. |
| schéma noethérien | Noetherian scheme | Capital N. |
| « accents » | "accents" | Translator's note on Gabriel's use of primes vs. accents. |
| « pré-relations d'équivalence » | "pre-equivalence relations" | Guillemets in source → English quotation marks; coinage preserved. |
-->

[^N.D.E-V-1]: N.D.E.: namely, theorems 5.1, 5.3, 6.1, 6.2 and 7.2 of TDTE III. The first two (resp. the next two)
    correspond to theorem 4.1 (resp. theorems 7.1 and 8.1) of this Exposé. Theorem 7.2 of TDTE III is proved in Exp.
    VI_A, 3.2 and 3.3.

[^N.D.E-V-2]: N.D.E.: that is, groupoids with base $X$, cf. the terminology at the end of section 1. When $C$ is the
    category of schemes, the quotient $p : X \to Y$ of a groupoid $X\ast$ with base $X$ exists under certain hypotheses
    (cf. 4.1, 6.1, 7.1); if, moreover, $X\ast$ is an equivalence relation, then $p$ is, under the same hypotheses,
    faithfully flat and quasi-compact, hence a universal epimorphism, cf. loc. cit.

[^N.D.E-V-3]: N.D.E.: Lemmas 1.1 and 1.2 have been added; they are used several times in sections 5 to 9.

[^N.D.E-V-4]: N.D.E.: This is not the case in the category of schemes. Take, for example, $S = \operatorname{Spec}(C)$,
    $X_{0} = A^{2}_{S} = \operatorname{Spec}(C[x_{1}, x_{2}])$, let $d_{1} : G_{m,S} \times_{S} A^{2}_{S} \to A^{2}_{S}$
    be the action of $G_{m,S}$ by homotheties on $A^{2}_{S}$, let $d_{0}$ be the projection onto the second factor, and
    $U = A^{2}_{S} - {m}$, where $m$ is the point `(0, 0)`. Then projective space $P^{1}_{S}$ is the cokernel of
    $(\tilde{d}_{0}, \tilde{d}_{1})$ in `(Esp. An)` and in `(Sch)`, and the cokernel $Y$ of $(d_{0}, d_{1})$ in
    `(Esp. An)` is the union of $P^{1}_{S}$ and the point $y_{0} = {p(m)}$; the only open set containing $y_{0}$ is $Y$,
    and one has $\Gamma(Y, O_{Y}) = C$. If $f : A^{2}_{S} \to T$ is a morphism of $S$-schemes such that $f d_{0} = f
    d_{1}$ and if $V = \operatorname{Spec}(A)$ is an affine open of $T$ containing the point $t_{0} = f(y_{0})$, then
    $f^{-1}(V) = A^{2}$ and the ring morphism $A \to C[x_{1}, x_{2}]$ factors through $C$; this shows that $S =
    \operatorname{Spec}(C)$ is the cokernel of $(d_{0}, d_{1})$ in the category $(Sch/S)$.

[^N.D.E-V-5]: N.D.E.: Hence, in this case, $X_{2}(T)$ is the set of pairs $(f_{2}, f_{1})$ of composable arrows, that
    is, such that $d_{0}(f_{1}) = d_{1}(f_{2})$, and $d'_{0}$, $d'_{1}$, $d'_{2}$ send $(f_{2}, f_{1})$ to $f_{2}$,
    $f_{2} \circ f_{1}$, $f_{1}$ respectively.

[^N.D.E-V-6]: N.D.E.: $T \mapsto s(T)$ defines an element of $\operatorname{Hom}(h_{X_{0}}, h_{X_{1}})$, and the latter
    equals $\operatorname{Hom}(X_{0}, X_{1})$ by the Yoneda lemma.

[^N.D.E-V-7]: N.D.E.: It follows from the Yoneda lemma that $\sigma$ is an involutive automorphism of $X_{1}$; this will
    be used, for example, in 3.e) and in theorem 4.1.

[^N.D.E-V-8]: N.D.E.: see example 2.a) below.

[^N.D.E-V-9]: N.D.E.: In particular, if $G$ is a $C$-group acting on the left on an object $X$ of $C$ and if $X\ast$ is
    the $C$-groupoid defined in a), then $(d_{0}, d_{1})$ is an equivalence pair if and only if $G$ acts freely on $X$,
    cf. Exp. III, 3.2.1.

[^N.D.E-V-10]: N.D.E.: The same argument applies for $B = k[T^{3}, T^{4}]$ and $T^{5} \otimes_{B} 1$; more generally,
    for $B = k[T^{n}, T^{n+r}]$ and the element $T^{n+2r} \otimes_{B} 1$, provided that $n$ does not divide `2r`.

[^N.D.E-V-11]: N.D.E.: this second viewpoint will be used in 3.f) and in the proof of 6.1.

[^N.D.E-V-12]: N.D.E.: "accents" in the original.

[^N.D.E-V-13]: N.D.E.: This will play a crucial role in the proof of lemma 6.1.

[^N.D.E-V-14]: N.D.E.: The original has been modified to make explicit the isomorphism below.

[^N.D.E-V-15]: N.D.E.: Reflexivity follows from the existence of $s : X_{0} \to X_{1}$ which is a section of both
    $d_{0}$ and $d_{1}$; symmetry follows from the existence of the involution $\sigma$ of $X_{1}$ which "exchanges
    $d_{0}$ and $d_{1}$", that is, satisfies $d_{0} \sigma = d_{1}$ and $d_{1} \sigma = d_{0}$, cf. § 1, (3), (3 bis)
    and (†).

[^N.D.E-V-16]: N.D.E.: Since $d_{0} = d_{1} \sigma$, where $\sigma$ is an involutive automorphism of $X_{1}$, these two
    conditions are symmetric in $d_{1}$ and $d_{0}$; moreover, one has $d_{0} d^{-1}_{1}(x) = d_{1} d^{-1}_{0}(x)$.

[^N.D.E-V-17]: N.D.E.: One cannot omit hypothesis b). Indeed, H. Hironaka has given an example of an action of the
    finite group $G = \mathbb{Z}/2\mathbb{Z}$ on a proper $C$-variety $X_{0}$ such that the quotient $X_{0}/G$ is an
    algebraic space which is not a scheme ([Hi62], see also [Mum65], Chap. 4, § 3).

[^N.D.E-V-18]: N.D.E.: We have added that $p$ is open, by taking up the analogous proof given in 6.1.

[^N.D.E-V-19]: N.D.E.: Note that, in this case, $X_{1} \to X_{0} \times_{S} X_{0}$ is therefore an immersion (EGA I,
    5.3.10); see also VI_B, 9.2.1. On the other hand, for the existence of the quotient (in the category of schemes or
    that of algebraic spaces) under the weaker hypothesis that $d_{0}$ and $d_{1}$ are finite (but not necessarily
    flat), see [An73], § 1.1, [Fe03], [Ko08]…

[^N.D.E-V-20]: N.D.E.: We have made explicit the consequences which follow; see [Ray67a], th. 1 (iii) and the proof
    given further on, at the end of section 5.

[^N.D.E-V-21]: N.D.E.: We have expanded on the original in what follows; in particular, we have added lemma 4.1.1, taken
    from [DG70], III, § 2.4, Lemma 4.3.

[^N.D.E-V-22]: N.D.E.: We have inserted this lemma, which is used several times in this Exposé and in subsequent Exposés
    (VI_A, VI_B). It appeared as Lemma VI_B, 4.5.1 in the original 1965 edition of SGAD.

[^N.D.E-V-23]: N.D.E.: Note the permutation of pages in Lecture Notes 151; the real order is
    265-266-268-269-267-270-271.

[^N.D.E-V-24]: N.D.E.: We have added the following lemma, taken from [DG70], I, § 5, Prop. 1.5 (see also the proof of
    EGA IV_3, 8.11.5), used implicitly in the original, and explicitly in [DG70], III, § 2, 4.6. It is moreover useful
    in th. 7.1 further on.

[^N.D.E-V-25]: N.D.E.: cf. Lemma 4.1.2.

[^N.D.E-V-26]: N.D.E.: We have added what follows.

[^N.D.E-V-27]: N.D.E.: indeed, since $d_{0}$ (resp. $d_{1}$) is surjective, flat and finite, hence faithfully flat and
    affine, then $d'_{2}$ is of rank $n$ above a neighborhood of a point $x$ of $X_{1}$ if and only if $d_{1}$ is of
    rank $n$ above a neighborhood of $d_{0}(x)$ (resp. $d_{1}(x)$).

[^N.D.E-V-28]: N.D.E.: one has $d_{1}(d^{-1}_{0}(x)) = d_{0}(d^{-1}_{1}(x))$, cf. N.D.E. 16 in theorem 4.1.

[^N.D.E-V-29]: N.D.E.: We have added the reference to lemma 4.1.1, cf. [DG70], III, § 5.2, p. 313.

[^N.D.E-V-30]: N.D.E.: We have added this paragraph.

[^N.D.E-V-31]: N.D.E.: If $x, y \in E$, there exists $z \in X_{1}$ such that $d_{1}(x) = x$ and $d_{0}(z) = y$, that is,
    $z$ belongs to the set $v^{-1}(x)$, which is finite by (1). Hence $E$ is contained in the finite set
    $d_{0}(v^{-1}(x)) = d_{0} d^{-1}_{1}(x) \cap U$.

[^N.D.E-V-32]: N.D.E.: We have slightly modified what follows; in particular, in lemma 6.1, the additional hypothesis
    that $d_{0}$ be flat has been moved to (iv), and (ii) has been separated into (i′) + (ii), and the second assertion
    of (i′) added.

[^N.D.E-V-33]: N.D.E.: We have expanded what follows, in particular the fact that $U'$ is a quasi-section of the
    groupoid induced on $X'_{0}$.

[^N.D.E-V-34]: N.D.E.: Let us mention here the article of S. Keel and S. Mori ([KM97]), where the following theorem is
    established. Let $X$ be an algebraic space of finite type over a locally Noetherian base $S$, and $j : R \to X
    \times_{S} X$ a flat groupoid whose stabilizer $j^{-1}(\Delta_{X})$ is finite over $X$; there then exists an
    algebraic space which is a geometric quotient of $X$ by $R$ and a uniform categorical quotient; moreover, if $j$ is
    separated, this quotient is separated. In particular, if a flat $S$-group scheme $G$ acts properly on $X$, with
    finite stabilizer (i.e., the morphism $G \times_{S} X \to X \times_{S} X$, $(g, x) \mapsto (x, g \cdot x)$, is
    proper and the stabilizer of the diagonal is finite over $X$), then there exists a geometric quotient $X \to X/G$.
    In the case of a reductive $S$-group scheme $G$, this is a result of J. Kollár ([Ko97]).

[^N.D.E-V-35]: N.D.E.: This hypothesis on $X_{0}$ is necessary, cf. N.D.E. 17 in Th. 4.1.

[^N.D.E-V-36]: N.D.E.: In TDTE III, Th. 6.1, it is indicated that $Y \to S$ is quasi-projective if $S$ is Noetherian.
    The editors have not seen how to deduce this from the local existence of quasi-sections.

[^N.D.E-V-37]: N.D.E.: We have made explicit the consequences which follow; see [Ray67a], th. 1 (iii) and the end of the
    proof of the theorem. Let us also mention that another proof of th. 7.1 in the case of an equivalence relation,
    based on the existence of Hilbert schemes, is given in [AK80], Th. 2.9, see also [BLR90], § 8.2, Th. 12; it is
    moreover shown there, in this case, that $Y \to S$ is quasi-projective.

[^N.D.E-V-38]: N.D.E.: Indeed, if one has constructed such an open neighborhood $U_{z}$ for every point $z$ closed
    relative to $S$, then the union of these $U_{z}$ covers $X_{0}$, since each fiber over $S$ of the closed complement
    is a Noetherian scheme without closed points, hence empty.

[^N.D.E-V-39]: N.D.E.: We have added details, and made explicit the role of the hypothesis that $d_{0}$ and $d_{1}$ are
    proper in theorem 7.1. (One can compare with the statement and proof of theorem 8.1, where this properness
    hypothesis is omitted.)

[^N.D.E-V-40]: N.D.E.: If $f : X \to Y$ is a morphism locally of finite type, the set of $x \in X$ isolated in their
    fiber $f^{-1}(f(x))$ is open in $X$: in EGA III, 4.4.10, this is deduced, for $Y$ locally Noetherian, from Zariski's
    "Main Theorem"; on the other hand, for arbitrary $Y$, this follows from Chevalley's semi-continuity theorem (EGA
    IV_3, 13.1.3 and 13.1.4). Consequently, $f$ is quasi-finite at $x$ if and only if $f$ is of finite type at $x$ and
    $x$ is isolated in $f^{-1}(f(x))$; this will be used further on, cf. N.D.E. 42.

[^N.D.E-V-41]: N.D.E.: We have expanded on the original in what follows.

[^N.D.E-V-42]: N.D.E.: The conditions are sufficient, by base change (cf. EGA II, 6.2.4 (iii) and EGA IV_2, 2.1.4).
    Conversely, put $y = d'(x)$ and $z = u(y) = d(v(x))$, and suppose $d'$ flat at $x$ and $u$ (hence also $v$) flat.
    Then $O_{v(x)} \to O_{x}$ is faithfully flat, as is $O_{z} \to O_{y} \to O_{x}$. Consequently, $O_{z} \to O_{v(x)}$
    is faithfully flat (cf. EGA IV_2, 2.2.11 (iv)). Finally, suppose $d$ locally of finite type and $d'$ quasi-finite at
    $x$. Then $v(x)$ is isolated in its fiber $d^{-1}(z)$, since $x$ is in its fiber $d'^{-1}(y) = d^{-1}(z)
    \otimes_{\kappa(z)} \kappa(y)$. Hence, by Chevalley's semi-continuity theorem, there exists an open neighborhood of
    $v(x)$ every point of which is isolated in its fiber (EGA IV_3, 13.1.3 and 13.1.4), so that $d$ is quasi-finite at
    $v(x)$.

[^N.D.E-V-43]: N.D.E.: We have modified the sequel, taking advantage of the additions made in lemma 6.1.

[^N.D.E-V-44]: N.D.E.: There exists a largest open $W$ of $X_{0}$ satisfying the conclusions of the theorem. Indeed, let
    $W$ be an open as in the theorem and $W^{\sharp}$ a dense saturated open contained in $W$. Since $p$ is open,
    $V^{\sharp} = p(W^{\sharp})$ is an open of $V$, and $W^{\sharp} = p^{-1}(V^{\sharp})$, since $W^{\sharp}$ is
    saturated. By lemma 1.1, $V^{\sharp}$ is a cokernel for the groupoid induced on $W^{\sharp}$. Thus one can glue
    along their intersection $W^{\sharp}$ two opens $W$ and $W'$ satisfying the conclusions of the theorem, and the
    conditions (i), (ii), (iii), (iv), as well as the fact that $p$ and $V \to S$ are locally of finite presentation,
    are preserved. The conclusion (ii′) follows, as in the proof of 6.1 (ii), from the hypothesis that $X_{0}$ is of
    finite type over $S$ Noetherian. Moreover, lemmas 1.1 and 1.2 also show that the union of all saturated opens $U$ of
    $X_{0}$ such that the open $p(U)$ of $Y$ is a scheme and $p|_{U} : U \to p(U)$ is a morphism of schemes is the
    largest saturated open $\Omega$ of $X_{0}$ satisfying condition (i) of 8.1. Theorem 8.1 shows that $\Omega$ contains
    a dense open $W$, but it is not immediate that $\Omega$ satisfies properties (ii) to (iv). On this subject, the
    reader may consult [Ray67a], [Ray67b], and Appendix I of [An73], which give more precise results, and study the
    question of the representability of the quotient $S$-sheaf (fppf) $\tilde{X}/R$ (where one has denoted by $R$ the
    groupoid $X\ast$ with base $X = X_{0}$), all this under weaker hypotheses ($S$ an arbitrary scheme, $X$ a scheme
    locally of finite type over $S$, and $R$ an $S$-groupoid with base $X$ such that $d_{0}$ (and therefore $d_{1}$) is
    flat and of finite presentation). Let us mention in particular the following results. If $\tilde{X}/R$ is
    representable by an $S$-scheme $Y$, then $Y$ is also the cokernel in the category `(Esp. An)`. The converse is in
    general false (cf. example 0.4 of [Mum65], Chap. 0, § 3, cited in [Ray67a], Rem. 1), but is true if $d = (d_{0},
    d_{1})$ is an immersion. Under this hypothesis, the morphism $p : \Omega \to Z := \Omega/R_{\Omega}$ is faithfully
    flat and of finite presentation; if moreover $S$ is locally Noetherian, then a point $x$ of codimension 1 in $X$
    belongs to $\Omega$ if and only if the graph of the groupoid induced on $\operatorname{Spec}(O_{X,x})$ is closed.
    For all this, see [Ray67a], Prop. 1, [Ray67b], Prop. 1 and Theorems 2, 1 and 4, and [An73], Theorems 5 and 6 pages
    66–67, and Prop. 3.3.1 page 49. (See also, in the case of an action of an algebraic group on an algebraically closed
    field $k$, the article [DR81].)

[^N.D.E-V-45]: N.D.E.: Indeed, let $\eta$ be such a generic point. The hypotheses imply that $O_{X_{0}, \eta}$ is an
    Artinian local ring, and $O_{F_{1}, \eta}$ a finitely generated $O_{X_{0}, \eta}$-module. Therefore, by SGA 1, VIII
    6.5, there exists an open neighborhood of $\eta$ above which $\tilde{d}_{1}$ is finite.

[^N.D.E-V-46]: N.D.E.: We have expanded what follows, to highlight theorem 9.0 below.

[^N.D.E-V-47]: N.D.E.: The original states that this follows from proposition 9.1 below. We were not able to reconstruct
    that argument. The proof that follows was indicated to us by O. Gabber.

[^V-9-1]: Cf. EGA IV_4, 17.7.5 for a more general result.

[^N.D.E-V-48]: N.D.E.: cf. EGA IV_1, 1.4.4.

[^N.D.E-V-49]: N.D.E.: Here too, there exists a largest open $U$ of $X$ satisfying the conclusions of the theorem, cf.
    N.D.E. 44.

[^N.D.E-V-50]: N.D.E.: If one assumes in addition that $G$ is a reductive $S$-group scheme and that the (free) action of
    $G$ on $X$ is linearizable, then it is known that $G\backslash X$ is representable and that $X \to G\backslash X$ is
    a (left) $G$-torsor. This follows from results of Raynaud and Seshadri and is found in the article [CTS79]
    (proposition 6.11).

[^N.D.E-V-51]: N.D.E.: This is point (2) of theorem 3 of [Ray67b]. In this Note another proof of th. 10.1.1 is sketched.

[^N.D.E-V-52]: N.D.E.: Here too, there exists a largest open $U$ of $X$ satisfying the conclusions of the theorem;
    moreover, a point $x \in X$ of codimension 1 in $X$ belongs to $U$ if and only if the morphism
    `(G_X/F) ×_X Spec(O_{X,x}) → Spec(O_{X,x}) ×_S Spec(O_{X,x})` is a closed immersion, cf. N.D.E. 44.

[^N.D.E-V-53]: N.D.E.: additional references cited in this Exposé.
