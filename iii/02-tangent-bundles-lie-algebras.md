# Exposé II. Tangent bundles, Lie algebras

<!-- label: III.II -->

*by M. Demazure*

<!-- original page 43 -->

[^N.D.E-II-0] We propose in this Exposé to construct the analogue, in the theory of schemes, of the tangent bundles and
Lie algebras of the classical theory. It will however be useful not to restrict ourselves to schemes properly speaking,
but also to consider certain functors on the category of schemes which are not necessarily representable (for example
the functors `Hom`, `Norm`, etc.). As announced in the preceding Exposé (cf. I 1.1), we shall identify a scheme with the
functor associated to it.

On the other hand, the constructions presented below go beyond the framework of the theory of schemes. They are equally
valid, for example, in the theory of analytic spaces with nilpotent elements, modulo a few modifications of detail.

Before beginning this construction, we must lay down a few general definitions that complement those of I 1.7.

## 1. The functors $\operatorname{Hom}_{Z/S}(X, Y)$

<!-- label: III.II.1 -->

Let us resume the notations of I 1.1. We identify the category $C$ with a full subcategory of $\hat{C} =
\operatorname{Hom}(C^{\circ}, (Ens))$ (in particular we suppress the underlines[^N.D.E-II-1] that allowed us to
distinguish graphically an object of `Ĉ` from an object of $C$).

Consider the following situation: four objects of `Ĉ`, denoted `S, X, Y, Z`, the first being in fact an object of $C$,
with $X$ and $Y$ above $Z$, and $Z$ above $S$:

<!-- original page 44 -->

```text
        X                   Y
         ╲                 ╱
       pX ╲               ╱ pY
            ╲           ╱
             ╲         ╱
                Z
                │
                ↓
                S .
```

**Definition 1.1.** *We define an object of $\hat{C}/S$, denoted $\operatorname{Hom}_{Z/S}(X, Y)$, by:*

<!-- label: III.II.1.1 -->

```text
(1)   Hom_{Z/S}(X, Y)(S′) = Hom_{Z_{S′}}(X_{S′}, Y_{S′}) = Hom_Z(X ×_S S′, Y),
```

*for every object $S'$ of $C/S$.* One sees at once that $\operatorname{Hom}_{Z/S}(X, Y)$ is nothing other than the
subobject of $\operatorname{Hom}_{S}(X, Y)$ formed by the morphisms compatible with `pX` and `pY`, that is to say, the
kernel of the pair of morphisms

```text
Hom_S(X, Y) ⇒ Hom_S(X, Z)
```

defined: the first by composition with `pY`; the second as the constant morphism whose "image" is `pX`.

On the other hand, one sees as in I 1.7 that, for every object $T$ of `Ĉ` above $S$, one has a natural
bijection:[^N.D.E-II-2]

```text
(2)   Hom_S(T, Hom_{Z/S}(X, Y)) ≃ Hom_Z(X ×_S T, Y).
```

Moreover, by I 1.7.1, if `E, F` are objects of `Ĉ` above $Z$, one has:

```text
Hom_Z(E, Hom_Z(F, Y)) ≃ Hom_Z(E ×_Z F, Y) ≃ Hom_Z(F, Hom_Z(E, Y)).
```

Applying this with $E = X$ and $F = Z \times_{S} T$, one obtains natural bijections, for every object $T$ of
$\hat{C}/S$:

```text
(3)   Hom_S(T, Hom_{Z/S}(X, Y)) ≃ Hom_Z(X ×_S T, Y) ≃ ⎰ Hom_Z(Z ×_S T, Hom_Z(X, Y))
                                                      ⎱ Hom_Z(X, Hom_Z(Z ×_S T, Y)).
```

Moreover, these bijections are functorial in $T$, so one obtains isomorphisms of $S$-functors:

```text
(4)   Hom_S(T, Hom_{Z/S}(X, Y)) ⥲ Hom_{Z/S}(X, Hom_Z(Z ×_S T, Y))
                                ≃ Hom_{Z/S}(X ×_S T, Y).
```

Let us point out two particular cases of the definition. If $Z = S$, one has:

```text
Hom_{S/S}(X, Y) = Hom_S(X, Y).
```

<!-- original page 45 -->

On the other hand, when $X = Z$, one sets

```text
(5)   ∏_{Z/S} Y = Hom_{Z/S}(Z, Y),
```

so that by definition

```text
(∏_{Z/S} Y)(S′) = Hom_Z(Z ×_S S′, Y) ≃ Γ(Y_{S′}/Z_{S′}).
```

The functor $\prod_{Z/S} : \hat{C}/Z \to \hat{C}/S$ is right adjoint to the base-change functor from $S$ to $Z$: for
every $S$-functor $U$ one has

```text
Hom_S(U, ∏_{Z/S} Y) = Hom_Z(U ×_S Z, Y).
```

(If $C = (Sch)$ and if $Z$ is an $S$-scheme, the functor $\prod_{Z/S}$ is called *"Weil restriction of
scalars"*.)[^N.D.E-II-3] Let us note also that one has an isomorphism:

```text
(6)   Hom_{Z/S}(X, Y) ≃ Hom_{X/S}(X, Y ×_Z X) = ∏_{X/S}(Y ×_Z X),
```

which gives in particular, for $Z = S$, an isomorphism:

```text
(7)   Hom_S(X, Y) ≃ ∏_{X/S} Y_X.
```

**Remark 1.2.** The functor $Y \mapsto \operatorname{Hom}_{Z/S}(X, Y)$ commutes with products in the following sense:
one has a functorial isomorphism

<!-- label: III.II.1.2 -->

```text
(∗)   Hom_{Z/S}(X, Y ×_Z Y′) ≃ Hom_{Z/S}(X, Y) ×_S Hom_{Z/S}(X, Y′).
```

It follows that if $Y$ is a $Z$-group, resp. a $Z$-ring, etc., then $\operatorname{Hom}_{Z/S}(X, Y)$ is an $S$-group,
resp. an $S$-ring, etc.

**Remark 1.3.**[^N.D.E-II-4] Moreover, let $\pi : M \to Y$ be a $Y$-functor of `O_Y`-modules (cf. I, 4.3.3.1). Set $H =
\operatorname{Hom}_{Z/S}(X, Y)$. Then $\operatorname{Hom}_{Z/S}(X, M)$ is equipped with a natural structure of
`O_H`-module; more precisely, for every $H'$ above $H$, $\operatorname{Hom}_{H}(H', \operatorname{Hom}_{Z/S}(X, M))$ is
equipped with a natural structure of $O(H' \times_{S} X)$-module.

<!-- label: III.II.1.3 -->

Indeed, denote by $m : M \times_{Y} M \to M$ and $\lambda : O_{Y} \times_{Y} M \to M$ the morphisms defining the
structures of $Y$-(abelian) group and of `O_Y`-module. Let $H'$ be an $S$-scheme above $H = \operatorname{Hom}_{Z/S}(X,
Y)$, i.e. one has been given a $Z$-morphism $f : X \times_{S} H' \to Y$, which therefore makes $X \times_{S} H'$ a
$Y$-object. Then,

$$ \operatorname{Hom}_{H}(H', \operatorname{Hom}_{Z/S}(X, M)) $$

is the set of $Z$-morphisms $\phi : X \times_{S} H' \to M$ such that $\pi \circ \phi = f$, i.e. of $Y$-morphisms $X
\times_{S} H' \to M$.

<!-- original page 52 -->

If $\phi, \psi$ are two such morphisms, one defines $\phi + \psi$ as the $Y$-morphism composite

```text
X ×_S H′ ──(φ × ψ)──→ M ×_Y M ──m──→ M
```

and one verifies that this equips $\operatorname{Hom}_{Z/S}(X, M)$ with a structure of abelian group above $H =
\operatorname{Hom}_{Z/S}(X, Y)$.[^N.D.E-II-5]

Likewise, if $a$ is an element of $O(X \times_{S} H')$, i.e. an $S$-morphism $a : X \times_{S} H' \to O_{S}$, one
defines $a\phi$ as the composite $\lambda \circ (a \times \phi)$, where $a \times \phi$ denotes the $Y$-morphism from $X
\times_{S} H'$ to $O_{Y} \times_{Y} M \simeq O_{S} \times_{S} M$ with components $a$ and $\phi$; one verifies that this
equips $\operatorname{Hom}_{H}(H', \operatorname{Hom}_{Z/S}(X, M))$ with a structure of $O(X \times_{S} H')$-module,
functorial in the $H$-object $H'$.

## 2. The schemes $I_{S}(M)$

<!-- label: III.II.2 -->

**Definition 2.1.** *Let $S$ be a scheme and $M$ a quasi-coherent `O_S`-module. We denote by $D_{O_{S}}(M)$ the
quasi-coherent `O_S`-algebra $O_{S} \oplus M$ (where $M$ is considered as an ideal of square zero). We denote by
$I_{S}(M)$ the $S$-scheme $\operatorname{Spec} D_{O_{S}}(M)$.*[^N.D.E-II-6]

<!-- label: III.II.2.1 -->

*In particular we set $D_{O_{S}} = D_{O_{S}}(O_{S})$, $I_{S} = I_{S}(O_{S})$, and we call them respectively the algebra
of dual numbers over $S$ and the scheme of dual numbers over $S$.*

Then $M \mapsto I_{S}(M)$ is a contravariant functor from the category of quasi-coherent `O_S`-modules to that of
$S$-schemes. In particular the morphisms $0 \to M$ and $M \to 0$ define respectively the structural morphism $\rho :
I_{S}(M) \to I_{S}(0) = S$ and a section $\epsilon_{M}$ of it, which we call the *zero section*.[^N.D.E-II-7]

<!-- original page 46 -->

**2.1.1.**[^N.D.E-II-8] Since $M \mapsto I_{S}(M)$ is a contravariant functor, every $a \in
\operatorname{End}_{O_{S}}(M)$ defines an $S$-endomorphism $a^{*}$ of $I_{S}(M)$, and one has $1^{*} = id$, $(ab)^{*} =
b^{*} \circ a^{*}$, $0^{*} = \epsilon_{M} \circ \rho$ and $a^{*} \circ \epsilon_{M} = \epsilon_{M}$. Consequently, the
$S$-scheme $I_{S}(M)$ is equipped with a right action of the multiplicative monoid of $\operatorname{End}_{O_{S}}(M)$,
which commutes with the $S$-morphisms $I_{S}(M) \to I_{S}(M')$ arising from morphisms $M' \to M$; in particular, the
operators $a^{*}$ preserve the zero section of $I_{S}(M)$.

For every $a \in \operatorname{End}_{O_{S}}(M)$ and $f : S' \to S$ and $m \in I_{S}(M)(S')$, we shall write $m \cdot a =
a^{*}(m)$; then $m \cdot 1 = m$, $(m \cdot a) \cdot b = m \cdot (ab)$, $m \cdot 0 = \epsilon_{M}(\rho(m))$ and, if $m =
\epsilon_{M}(f)$, then $m \cdot a = m$.[^N.D.E-II-9]

**Remark 2.1.2.** *The formation of the $I_{S}(M)$ commutes with base extension: one has canonical isomorphisms*

<!-- label: III.II.2.1.2 -->

```text
I_S(M)_{S′} ≃ I_{S′}(M ⊗_{O_S} O_{S′}).
```

To simplify, we shall write $I_{S'}(M) = I_{S}(M)_{S'}$; more generally, if $X$ is an $S$-functor (not necessarily
representable), we shall write $I_{X}(M) = I_{S}(M) \times_{S} X$.

**2.1.3.**[^N.D.E-II-10] By what precedes, the multiplicative monoid of $O(S')$ acts on the $S'$-scheme $I_{S'}(M)$,
functorially in $M$, i.e. the $S$-scheme $I_{S}(M)$ is equipped with a structure of object with monoid of operators
`O_S`, this structure being functorial in $M$. One thus has a morphism of $S$-schemes

```text
λ : I_S(M) ×_S O_S ⟶ I_S(M),
```

verifying obvious conditions. For every $S$-functor $X$, one obtains by base change a morphism of $X$-functors:

```text
λ_X : I_X(M) ×_S O_S ⟶ I_X(M)
```

which makes the $S$-functor $I_{X}(M)$ into an object with monoid of operators $O(X)$: every element $a$ of $O(X) =
\operatorname{Hom}_{S}(X, O_{S})$ defines an $X$-endomorphism $a^{*} = \lambda_{X} \circ (id_{I_{X}(M)} \times (a \circ
pr_{X}))$ of $I_{X}(M)$; explicitly, if $x \in X(S')$ and $m \in I_{S}(M)(S') = I_{S'}(M)(S')$, then $a(x) = a \circ x$
belongs to $O(S')$ and one has:

```text
(m, x) · a = (m · a(x), x).
```

This operation is functorial in $M$ and preserves the zero section $\epsilon_{M} : X \to I_{X}(M)$, i.e. $a^{*} \circ
\epsilon_{M} = \epsilon_{M}$ for every $a \in O(X)$.

Moreover, this operation is "functorial in $X$" in the following sense: if $\pi : Y \to X$ is a morphism of $S$-functors
and $u : O(X) \to O(Y)$ the corresponding ring morphism (i.e. $u(a) = a \circ \pi \in O(Y)$ for every $a \in O(X) =
\operatorname{Hom}_{S}(X, O_{S})$), then the following diagram is commutative:

```text
              a^*
   I_X(M) ─────────→ I_X(M)
      ↑                 ↑
      π                 π
              u(a)^*
   I_Y(M) ─────────→ I_Y(M) .
```

**2.2.** Let now $M$ and $N$ be two quasi-coherent `O_S`-modules. The commutative diagram

```text
                M ⊕ N
              ↗   ↑   ↘
            ↗     │     ↘
          M       │       N
            ↘     ↓     ↙
              ↘   │   ↙
                  0
```

<!-- original page 54 -->

defines a commutative diagram of $S$-schemes

```text
                I_S(M ⊕ N)
              ↗     ↑      ↖
            ↗       │        ↖
          ↗       ε_{M⊕N}      ↖
       I_S(M)        │        I_S(N)
(∗)       ↖         │         ↗
            ↖       │       ↗
            ε_M     │     ε_N
                ↘   │   ↙
                    S .
```

**Proposition 2.2.** *For every $S$-scheme $X$, the diagram of functors over $S$ obtained by applying the functor
$\operatorname{Hom}_{S}(-, X)$ to diagram (∗) is cartesian:*

<!-- label: III.II.2.2 -->

<!-- original page 47 -->

```text
                Hom_S(I_S(M ⊕ N), X)
              ↙                      ↘
        Hom_S(I_S(M), X)        Hom_S(I_S(N), X)
              ↘                      ↙
                Hom_S(S, X) = X .
```

It must be verified that for every $S' \to S$, the diagram of sets obtained by taking the value of the functors on $S'$
is cartesian. Since the formation of $I_{S}(P)$ commutes with base extension in the sense explained above, it suffices
to do it for $S' = S$, hence to verify that the following diagram of sets is cartesian:

```text
                X(I_S(M ⊕ N))
              ↙              ↘
        X(I_S(M))       X(I_S(N))
              ↘     X(ε_{M⊕N})↙
              X(ε_M)  ↓  X(ε_N)
                    X(S) .
```

Now, if $x \in X(S)$, it follows from SGA 1, III 5.1[^N.D.E-II-11], that $X(\epsilon_{M})^{-1}(x)$ is isomorphic,
functorially in $M$, to

$$ \operatorname{Hom}_{O_{S}}(x^{*}(\Omega^{1}_{X/S}), M), $$

where $\Omega^{1}_{X/S}$ denotes the sheaf of relative differentials of $X$ with respect to $S$. Now this latter functor
(in $M$) evidently transforms a direct sum of `O_S`-modules into the product of the corresponding sets, whence the
result.

**Corollary 2.2.1.** *Let $X$ be an $S$-scheme and $M$ a free `O_S`-module of finite type. The functor
$\operatorname{Hom}_{S}(I_{S}(M), X)$ is isomorphic (as functor above $X$) to a finite product (above $X$) of copies of
$\operatorname{Hom}_{S}(I_{S}, X)$.*

<!-- label: III.II.2.2.1 -->

<!-- original page 48 -->

**Nota 2.2.2.** *It follows from the proof of the proposition that $\operatorname{Hom}_{S}(I_{S}, X)$ is isomorphic as
$X$-functor to $V(\Omega^{1}_{X/S})$ (I 4.6.1), hence representable by the vector fibration*[^N.D.E-II-12]
*$V(\Omega^{1}_{X/S})$.*

<!-- label: III.II.2.2.2 -->

## 3. The tangent bundle, condition (E)

<!-- label: III.II.3 -->

In this section, unless otherwise stated, the letters $M, M', N$, etc., will always denote free `O_S`-modules of finite
type (that is to say, isomorphic to a finite direct sum of copies of `O_S`).

We shall systematically use the identifications justified in Exposé I; thus we shall say "functor above $S$" to
designate indifferently a functor equipped with a morphism into $S$ (= $h_{S}$) or a functor on the category of objects
above $S$. Likewise we shall say "group-functor above $S$", etc.

**Definition 3.1.** *Let $S$ be a scheme and $M$ a free `O_S`-module of finite type. Let $X$ be a functor above $S$. One
calls* **tangent bundle to $X$ above $S$ relative to the `O_S`-module $M$** *and denotes by $T_{X/S}(M)$ the
$S$-functor*

<!-- label: III.II.3.1 -->

$$ T_{X/S}(M) = \operatorname{Hom}_{S}(I_{S}(M), X). $$

*In particular, one calls* **tangent bundle to $X$ above $S$** *and denotes by $T_{X/S}$ the functor*[^N.D.E-II-13]

```text
T_{X/S} = T_{X/S}(O_S) = Hom_S(I_S, X).
```

Then $M \mapsto T_{X/S}(M)$ is a covariant functor from the category of free `O_S`-modules of finite type to the
category of $S$-functors. In particular the morphisms[^N.D.E-II-14] $M \to 0$ and $0 \to M$ define respectively an
$S$-morphism

<!-- original page 49 -->

```text
π_M : T_{X/S}(M) ⟶ T_{X/S}(0) ≃ X
```

and a section $\tau_{0}$ of it, called the *zero section* (or *null section*).

**Remark 3.1.1.**[^N.D.E-II-15] One should note that the projection $\pi_{M} : T_{X/S}(M) \to X$ is induced by the zero
section $\epsilon_{M} : S \to I_{S}(M)$, while the null section $\tau_{0} : X \to T_{X/S}(M)$ is induced by the
structural morphism $\rho : I_{S}(M) \to S$; i.e., for every point $t \in T_{X/S}(M)(S')$ (resp. $x \in X(S')$),
corresponding to an $S$-morphism $f : S' \times_{S} I_{S}(M) \to X$ (resp. $g : S' \to X$), one has $\pi(t) = f \circ
(id_{S'} \times \epsilon_{M})$ (resp. $\tau_{0}(x) = g \circ (id_{S'} \times \rho)$).

<!-- label: III.II.3.1.1 -->

It follows from 3.1 that $M \mapsto T_{X/S}(M)$ is a covariant functor from the category of free `O_S`-modules of finite
type to that of functors above $X$. In particular $O(S)$ is a monoid of operators of the $X$-functor $T_{X/S}(M)$ which
respects "functoriality in $M$".

**Scholie 3.1.2.**[^N.D.E-II-15] What precedes means, in particular, the following. For every $S$-morphism $\phi : X'
\to X$, set

<!-- label: III.II.3.1.2 -->

```text
Σ(X′, M) = Hom_X(X′, T_{X/S}(M)).
```

One has an action of the multiplicative monoid $\operatorname{End}_{O_{S}}(M)$ on $\Sigma(X', M)$, denoted $(\lambda, x)
\mapsto \lambda \ast x$, such that $\lambda \ast (\mu \ast x) = (\lambda \mu) \ast x$, $1 \ast x = x$, and $0 \ast x =
\tau_{0} \circ \phi$, where $\tau_{0}$ is the null section $X \to T_{X/S}(M)$. One has likewise an action of
$\operatorname{End}_{O_{S}}(M \oplus M)$ on $\Sigma(X', M \oplus M)$.[^N.D.E-II-16]

Moreover, let $m : M \oplus M \to M$ (resp. $\delta : M \to M \oplus M$) be the addition (resp. the diagonal map) of
$M$, and denote by $m_{X'} : \Sigma(X', M \oplus M) \to \Sigma(X', M)$ and $\delta_{X'} : \Sigma(X', M) \to \Sigma(X', M
\oplus M)$ the morphisms induced by $m$ and $\delta$. For $\lambda, \mu \in O(S)$, denote by $\ell_{\lambda}$ (resp.
$\ell_{\lambda,\mu}$) multiplication by $\lambda$ in $M$ (resp. by $(\lambda, \mu)$ in $M \oplus M$). Since $m \circ
\ell_{\lambda,\lambda} = \ell_{\lambda} \circ m$ and $m \circ \ell_{\lambda,\mu} \circ \delta = \ell_{\lambda+\mu}$, one
has, for every $z \in \Sigma(X', M \oplus M)$ and $x \in \Sigma(X', M)$:

```text
(†)   λ ∗ m(z) = m((λ, λ) ∗ z),    m((λ, μ) ∗ δ(x)) = (λ + μ) ∗ x.
```

**Definition 3.2.** *Let $u \in X(S) = \operatorname{Hom}_{S}(S, X) = \Gamma(X/S)$. One calls* **tangent space to $X$
above $S$ at the point $u$ relative to $M$**, *and denotes by $L^{u}_{X/S}(M)$, the $S$-functor obtained from the
$X$-functor $T_{X/S}(M)$ by pullback along the morphism $u : S \to X$:*

<!-- label: III.II.3.2 -->

```text
   L^u_{X/S}(M) ──────→ T_{X/S}(M)
       │                    │
       │                    │ π
       ↓        u           ↓
       S ───────────────→   X .
```

*In particular $L^{u}_{X/S}(O_{S})$ is denoted $L^{u}_{X/S}$. It is the* **tangent space to $X$ above $S$ at the point
$u$**.

**Remark 3.2.1.**[^N.D.E-II-17] It follows from 3.1.1 that, for every $t : S' \to S$, $L^{u}_{X/S}(M)(S')$ is the set of
$S$-morphisms $f : I_{S'}(M) \to X$ such that $f \circ \epsilon_{M} = u \circ t$, where $\epsilon_{M} : S' \to
I_{S'}(M)$ is the zero section.

<!-- label: III.II.3.2.1 -->

Let us note immediately the

**Proposition 3.3.** *If $X$ is representable by an $S$-scheme denoted $\tilde{X}$, then $T_{X/S}(M)$ and
$L^{u}_{X/S}(M)$ are representable. In particular $T_{X/S}$ and $L^{u}_{X/S}$ are representable by vector fibrations on
$\tilde{X}$ and on $S$, which are respectively $V(\Omega^{1}_{\tilde{X}/S})$ and $V(u^{*}(\Omega^{1}_{\tilde{X}/S}))$.*

<!-- label: III.II.3.3 -->

It clearly suffices to prove the proposition for $T_{X/S}(M)$; the analogous results for $L^{u}_{X/S}(M)$ follow by
pullback. By Corollary 2.2.1, it even suffices to do it for $T_{X/S}$, and in that case, the proposition is nothing
other than the remark noted in 2.2.2.

**Remark 3.3.1.** From this proposition follows a particularly simple description of the vector fibration representing
$L^{u}_{X/S}$: the image of the section $u$ of $X$ over $S$ is locally closed[^N.D.E-II-18], hence defined by a
quasi-coherent ideal $m$ of a scheme induced on an open subset of $X$. The quotient $m/m^{2}$ can be considered as a
quasi-coherent module on $S$. It is this module that defines the sought-after vector fibration.

<!-- label: III.II.3.3.1 -->

<!-- original page 50 -->

Take for example $X$ an algebraic scheme over a field $k$ and $u$ a $k$-rational point of $X$. Let $m$ be the maximal
ideal of the local ring $O_{X,u}$ and let $t$ be the $k$-vector space dual to $m/m^{2}$; it is the Zariski tangent space
of $O_{X,u}$ at the point $u$. Then, with the notations of I 4.6.5.1, one has:

$$ L^{u}_{X/k} = V(m/m^{2}) = W(t). $$

Having closed this parenthesis, let us return to the general situation. Let us remark first that $L^{u}_{X/S}(M)$ is a
covariant functor from the category of free `O_S`-modules of finite type to that of functors above $S$. In particular
$O(S)$ is a set of operators of the $S$-functor $L^{u}_{X/S}(M)$ which respects functoriality in $M$.[^N.D.E-II-19]

**Proposition 3.4.** *The formation of $T_{X/S}(M)$ and $L_{X/S}(M)$ commutes with base extension: for every $S$-scheme
$S'$, one has isomorphisms functorial in $M$*

<!-- label: III.II.3.4 -->

```text
T_{X_{S′}/S′}(M ⊗ O_{S′}) ⥲ T_{X/S}(M)_{S′},
L^{u′}_{X_{S′}/S′}(M ⊗ O_{S′}) ⥲ L^u_{X/S}(M)_{S′},   where u′ = u_{S′}.
```

This results immediately from the fact that `Hom` commutes with base extension.

**Corollary 3.4.1.** *The $X$-functor $T_{X/S}(M)$ (resp. the $S$-functor $L^{u}_{X/S}(M)$) is naturally equipped with a
structure of object with operators `O_X` (resp. `O_S`), this structure being functorial in $M$.*

<!-- label: III.II.3.4.1 -->

Let us show this first for $L^{u}_{X/S}(M)$. For each $S'$ above $S$, $O(S')$ acts on $M \otimes O_{S'}$ hence on
$L^{u'}_{X_{S'}/S'}(M \otimes O_{S'}) = L^{u}_{X/S}(M)_{S'}$; now one verifies that this action is functorial in $S'$.
It thus equips $L^{u}_{X/S}(M)$, as announced, with a structure of functor with operators `O_S`.

For $T_{X/S}(M)$ it is a little more complicated. For each $X'$ above $X$, set $T_{X/S}(M)_{X'} = T_{X/S}(M) \times_{X}
X'$; one must equip $T_{X/S}(M)_{X'}(X') = \operatorname{Hom}_{X}(X', T_{X/S}(M))$ with a structure of set with monoid
of operators $O(X')$ in a manner functorial in $X'$. For this one constructs the following diagram, where $X_{X'}$
denotes $X \times_{S} X'$ and $f'$ denotes the section of $X_{X'}$ over $X'$ defined by $f : X' \to X$:

<!-- original page 58 -->

```text
                T_{X_{X′}/X′}(M)
              ↙                ↘
   T_{X/S}(M) ←─────  T_{X/S}(M)_{X′}
       ↓                     ↓
                X_{X′}
              ↙        ↘ f′
            ↙             ↘
   X ←────  f               X′
              ↘            ↙
                  S .
```

[^N.D.E-II-20] This diagram, joined with 3.2.1, shows that $T_{X/S}(M)_{X'}(X')$ is identified with

```text
L^{f′}_{X_{X′}/X′}(M)(X′) = { X′-morphisms ψ : I_{X′}(M) → X_{X′} such that ψ ∘ ε_M = f′ },
```

on which every $a \in O(X')$ acts via its action on $I_{X'}(M)$, i.e., with the notations of 2.1.1, one has: $a\psi =
\psi \circ a^{*}$, i.e. for every $X'' \to X'$ and $x \in I_{X'}(M)(X'')$, $(a\psi)(x) = \psi(x \cdot a)$. One then
verifies easily that this construction is functorial in $X'$.

The isomorphisms of Proposition 3.4 are then, by construction, isomorphisms for the structures of $O_{X_{S'}}$-objects,
resp. $O_{S'}$-objects.

**Remark 3.4.2.**[^N.D.E-II-21] The action of `O_X` on $T_{X/S}(M)$ can be seen, more simply, as follows. For every $f :
X' \to X$, one has

<!-- label: III.II.3.4.2 -->

```text
Hom_X(X′, T_{X/S}(M)) = { φ ∈ Hom_S(I_{X′}(M), X) | φ ∘ ε_M = f },
```

and one saw in 2.1.3 that $I_{X'}(M)$, considered as $S$-functor, is equipped with an action of the monoid $O(X')$ which
preserves the zero section $\epsilon_{M} : X' \to I_{X'}(M)$. Consequently, if one denotes by $a^{*}$ the
$X'$-endomorphism of $I_{X'}(M)$ defined by $a \in O(X')$, one has: $a\phi = \phi \circ a^{*}$, i.e., for every $S' \to
S$ and $(m, x') \in \operatorname{Hom}_{S}(S', I_{S}(M) \times_{S} X')$,

```text
(aφ)(m, x′) = φ(m · a(x′), x′)
```

(note that $a^{*} \circ \epsilon_{M} = \epsilon_{M}$, whence $(a\phi) \circ \epsilon_{M} = \phi \circ \epsilon_{M} =
f$).

Likewise, the action of `O_S` on $L^{u}_{X/S}(M)$ can be described as follows. For every $t : S' \to S$,
$L^{u}_{X/S}(M)(S')$ is the set of $S$-morphisms $\phi : I_{S'}(M) \to X$ such that $\phi \circ \epsilon_{M} = u \circ
t$; for such a $\phi$ and $a \in O(S')$, one has: $a\phi = \phi \circ a^{*}$.

**Remark 3.4.3.**[^N.D.E-II-21] The observations of 3.1.2 hold equally for the action of `O_S` on $L^{u}_{X/S}(M)$ and
that of `O_X` on $T_{X/S}(M)$.

<!-- label: III.II.3.4.3 -->

**Definition 3.5.** *Let $S$ be a scheme and $X$ an $S$-functor. One says that $X$ satisfies* **condition (E)**
*relative to $S$ if, for every $S'$ above $S$ and all free $O_{S'}$-modules $M$ and $N$ of finite type, the diagram of
sets*

<!-- label: III.II.3.5 -->

```text
                X(I_{S′}(M ⊕ N))
              ↙                  ↘
       X(I_{S′}(M))           X(I_{S′}(N))
              ↘                  ↙
                  X(S′) ,
```

*obtained by applying $X$ to the diagram (∗) defined in 2.1, is cartesian.*[^N.D.E-II-22]

<!-- original page 52 -->

**3.5.1.**[^N.D.E-II-23] It comes to the same thing to say that the functor $M \mapsto T_{X/S}(M)$ transforms direct
sums of free `O_S`-modules of finite type into products of $X$-functors; in this case, the same holds for the functor $M
\mapsto L^{u}_{X/S}(M) = S \times_{X} T_{X/S}(M)$, for every $u \in \Gamma(X/S)$.

Proposition 2.2 shows that every representable functor satisfies condition (E).

*Abbreviation:* instead of saying "X satisfies condition (E) with respect to $S$", we shall sometimes say "$X/S$
satisfies condition (E)".

If $X/S$ satisfies condition (E), the functor $M \mapsto T_{X/S}(M)$ commutes with products and therefore transforms
groups into groups. In particular $T_{X/S}(M)$ is a commutative $X$-group. For the same reason, $L^{u}_{X/S}(M)$ is a
commutative $S$-group.

**Proposition 3.6.** *If $X/S$ satisfies (E), the abelian group structure on $T_{X/S}(M)$ (resp. $L^{u}_{X/S}(M)$) and
the action of `O_X` (resp. `O_S`) equip $T_{X/S}(M)$ (resp. $L^{u}_{X/S}(M)$) with a structure of `O_X`-module (resp.
`O_S`-module).*

<!-- label: III.II.3.6 -->

The action of `O_X` (resp. `O_S`) is functorial in $M$; it therefore respects the abelian group structure that is
deduced by functoriality from that of $M$.[^N.D.E-II-24] Indeed, let us resume the notations of 3.1.2. The structure of
(abelian) $X$-group on $T_{X/S}(M)$ is defined by the composite:

```text
T_{X/S}(M) ×_X T_{X/S}(M) ≃ T_{X/S}(M ⊕ M) ──m──→ T_{X/S}(M),
```

and on the other hand the morphism

```text
T_{X/S}(M) ──δ──→ T_{X/S}(M ⊕ M) ≃ T_{X/S}(M) ×_X T_{X/S}(M)
```

is the diagonal morphism. Taking into account Remark 3.4.3, one deduces from the equalities (†) of 3.1.2 that

```text
λ(x + y) = λx + λy,    (λ + μ)x = λx + μx,
```

for every $f : X' \to X$, $x, y \in \operatorname{Hom}_{X}(X', T_{X/S}(M))$ and $\lambda, \mu \in O(X')$.

**Remark 3.6.1.** *If $X$ is representable, in which case it satisfies (E) and $T_{X/S}$ and $L^{u}_{X/S}$ are
representable by vector fibrations, the preceding laws are the same as those deduced from the vector fibration
structures (cf. I 4.6).*[^N.D.E-II-25]

<!-- label: III.II.3.6.1 -->

**Proposition 3.4 bis.** *If $X/S$ satisfies (E), then $X_{S'}/S'$ satisfies (E) and the isomorphisms of 3.4 respect the
structures of $O_{X_{S'}}$-modules, resp. of $O_{S'}$-modules.*

<!-- label: III.II.3.4-bis -->

Without comment.

<!-- original page 53 -->

**Proposition 3.7.** *The functors $T_{X/S}(M)$ and $L^{u}_{X/S}(M)$ are functorial in $X$, i.e., if $f : X \to X'$ is
an $S$-morphism, one has commutative diagrams:*

<!-- label: III.II.3.7 -->

```text
                T(f)                                       L(f)
   T_{X/S}(M) ──────→ T_{X′/S}(M)        L^u_{X/S}(M) ──────→ L^{f∘u}_{X′/S}(M)
        ↓                  ↓                       ↘             ↙
        X  ──────────→     X′  ,                       S .
```

*Moreover,*[^N.D.E-II-26] *if $f$ is a monomorphism, so are $T(f)$ and $L(f)$.*

The existence of $T(f)$ and $L(f)$, as well as the last assertion, follow immediately from the definitions. The
commutativity of the diagrams then follows from the functoriality of these morphisms with respect to $M$ and from the
fact that $T_{X/S}(0) = X$.

**Remark 3.7.1.**[^N.D.E-II-27] Suppose $X$ and $X'$ representable and let $r$ be the rank of the free `O_S`-module $M$.
Then, by 2.2.2, $T_{X/S}(M)$ is isomorphic to the product over $X$ of $r$ copies of $V(\Omega^{1}_{X/S})$, and likewise
for $T_{X'/S}(M)$. Consequently, the above square is cartesian when $f$ is an open immersion, more generally when
$f^{*}(\Omega^{1}_{X'/S}) = \Omega^{1}_{X/S}$, for example if $f$ is étale; under these conditions, one has an
isomorphism of $S$-functors

<!-- label: III.II.3.7.1 -->

$$ L^{u}_{X/S}(M) \xrightarrow{\sim} L^{f\circ u}_{X'/S}(M). $$

In general, the cartesian square of 3.7 defines a morphism of $X$-functors:

```text
T_{X/S}(M) ────────→ T_{X′/S}(M) ×_{X′} X
       ↘                  ↙
              X .
```

**Proposition 3.7 bis.** *Let $f : X \to X'$ be an $S$-morphism; if $X$ and $X'$ satisfy (E) with respect to $S$, then*

<!-- label: III.II.3.7-bis -->

```text
              T(f)                                                L(f)
T_{X/S}(M) ─────────→ T_{X′/S}(M)_X       resp.   L^u_{X/S}(M) ─────────→ L^{f∘u}_{X′/S}(M)
```

*is a morphism of `O_X`-modules (resp. of `O_S`-modules).*

This follows from Proposition 3.7 by functoriality in $M$.

**Proposition 3.8.** *Let $X$ and $Y$ be two functors above $S$. One has isomorphisms functorial in $M$:*

<!-- label: III.II.3.8 -->

```text
(3.8.1)   T_{X/S}(M) ×_S T_{Y/S}(M) ⥲ T_{(X×_S Y)/S}(M),
(3.8.2)   L^u_{X/S}(M) ×_S L^v_{Y/S}(M) ⥲ L^{(u,v)}_{(X×_S Y)/S}(M).
```

[^N.D.E-II-28] The first isomorphism follows from 1.2 (∗); the second is deduced from it by the base change $(u, v) : S
\to X \times_{S} Y$.

**Remark 3.8.0.** Note that (3.8.1) can also be interpreted as an isomorphism of $X \times_{S} Y$-functors

<!-- label: III.II.3.8.0 -->

```text
T_{X/S}(M) ×_X (X ×_S Y) × T_{Y/S}(M) ×_Y (X ×_S Y) ⥲ T_{(X×_S Y)/S}(M).
                            (X×_S Y)
```

**Corollary 3.8.1.** *If $X/S$ is equipped with an algebraic structure defined by finite cartesian products, then
$T_{X/S}(M)$ is equipped with a structure of the same kind and the projection $T_{X/S}(M) \to X$ is a morphism of this
kind of structure.*

<!-- label: III.II.3.8.1 -->

**Proposition 3.8 bis.** *If $X/S$ and $Y/S$ satisfy (E), then $(X \times_{S} Y)/S$ satisfies (E) and (3.8.1) (resp.
(3.8.2)) is an isomorphism of $O_{X\times_{S} Y}$-modules (resp. `O_S`-modules).*

<!-- label: III.II.3.8-bis -->

*Proof.*[^N.D.E-II-29] Suppose that $X/S$ and $Y/S$ satisfy (E). Then, by 3.5.1 and (3.8.1), so does $(X \times_{S}
Y)/S$. Let us show that (3.8.1) is an isomorphism of $O_{X\times_{S} Y}$-modules.

<!-- original page 62 -->

Let $(x, y) : Z \to X \times_{S} Y$ be an $S$-morphism; taking into account 3.4.2, it suffices to see that the map

```text
{ φ ∈ Hom_S(I_Z(M), X) | φ ∘ ε_M = x } × { ψ ∈ Hom_S(I_Z(M), Y) | ψ ∘ ε_M = y }
   ⟶ { θ ∈ Hom_S(I_Z(M), X ×_S Y) | θ ∘ ε_M = (x, y) }
```

which to $(\phi, \psi)$ associates $\phi \times \psi$ is a morphism of $O(Z)$-modules. But this is clear, because if $a
\in O(Z)$ then $a \cdot (\phi, \psi) = (\phi \circ a^{*}, \psi \circ a^{*})$ is sent to

```text
(φ ∘ a^*) × (ψ ∘ a^*) = (φ × ψ) ∘ a^* = a · (φ × ψ).
```

Likewise, using 3.2.1, one shows that (3.8.2) is an isomorphism of `O_S`-modules.

**3.9.0.**[^N.D.E-II-30] If $X$ is an $S$-group and if $e : S \to X$ denotes its unit section, one writes:

$$ Lie(X/S, M) = L^{e}_{X/S}(M), $$

i.e., $Lie(X/S, M)$ is defined by the cartesian square:

```text
                   i
   Lie(X/S, M) ────────→ T_{X/S}(M)
       │                     │
       │                     │ p
       ↓        e            ↓
       S ─────────────────→  X .
```

By Corollary 3.8.1, the projection $p : T_{X/S}(M) \to X$ is a morphism of $S$-groups, and it follows that $Lie(X/S, M)$
is equipped with a structure of $S$-group, and is isomorphic via $i$ to the kernel of $p$.

If, moreover, $X/S$ satisfies condition (E), we shall see in Proposition 3.9 that the $S$-group structure on $Lie(X/S,
M)$, induced by that of $X$, coincides with the abelian group structure induced by functoriality in $M$ (cf. 3.5.1). In
fact, this result is valid under the weaker hypothesis that $X$ be an $S$-functor of monoids or, more generally, an
$S$-functor of $H$-sets (cf. the definition below).

**Definitions 3.9.0.1.** *a) Let us introduce the following terminology:*[^N.D.E-II-31] *an* **$H$-set** *is a set $X$
equipped with a composition law with two-sided unit, denoted $e_{X}$ or simply $e$. If $f : X \to Y$ is a morphism of
$H$-sets, its kernel `Ker f` is $f^{-1}(e_{Y})$; it is a sub-$H$-set of $X$.*

<!-- label: III.II.3.9.0.1 -->

*b) An* **$H$-object** *in a category $C$ is defined in the usual manner: it is therefore an object $X$ of $C$, equipped
with a morphism $X \times X \to X$ such that there exists a section of $X$ (above the final object) possessing the
properties of a two-sided unit. Every $C$-monoid, in particular every $C$-group, is therefore a $C$-$H$-object. In
particular, an $H$-object of the category of functors above the scheme $S$ will be called an* **$S$-$H$-functor**.

*c) If $X$ is an $S$-$H$-functor (for example, an $S$-group), and if $e : S \to X$ denotes the unit section of $X$, one
writes:*

```text
Lie(X/S, M) = L^e_{X/S}(M)    and    Lie(X/S) = Lie(X/S, O_S).
```

Let us make explicit the following particular case of 3.8.1.[^N.D.E-II-32]

**Corollary 3.9.0.2.** *If $X$ is an $S$-$H$-functor (resp. an $S$-group), then $T_{X/S}(M)$ and $Lie(X/S, M)$ are also
$S$-$H$-functors (resp. $S$-groups), and one has morphisms of $S$-$H$-functors (resp. of $S$-groups):*

<!-- label: III.II.3.9.0.2 -->

```text
                   i                p
   Lie(X/S, M) ────────→ T_{X/S}(M) ⇄ X ,
                                     s
```

*where $i$ is an isomorphism of $Lie(X/S)(M)$ onto `Ker p` and $s$ is a section of $p$.*

<!-- original page 55 -->

**Proposition 3.9.** *Let $X$ be an $S$-$H$-functor satisfying (E) with respect to $S$. The $S$-$H$-functor structure of
$Lie(X/S, M)$ coming from that of $X$ coincides with the $S$-group structure defined in 3.5.1.*

<!-- label: III.II.3.9 -->

It follows from what was said above that $Lie(X/S, M)$ is an $H$-object in the category of `O_S`-modules. The
proposition will then follow from the following lemma:[^N.D.E-II-33]

**Lemma 3.10.** *Let $C$ be a category. Let $G$ be an $H$-object in the category of $C$-$H$-objects; $G$ is therefore a
$C$-$H$-object (whose composition law we shall denote $f : G \times G \to G$) equipped with a morphism of
$C$-$H$-objects $h : G \times G \to G$.*[^N.D.E-II-34] *Then $f = h$ and $f$ is commutative.*

<!-- label: III.II.3.10 -->

By taking the values of the functors on a variable argument, one reduces, in the usual manner, to verifying the lemma
when $C$ is the category of sets. One thus has a set $G$ and two maps $f, h : G \times G \to G$ such that

```text
h(f(x, y), f(z, t)) = f(h(x, z), h(y, t)).
```

One has on the other hand two elements of $G$, namely $e$ and $u$, with $f(e, x) = f(x, e) = x$, $h(u, x) = h(x, u) =
x$. One sees first that

```text
h(f(u, y), f(x, u)) = f(x, y) = h(f(x, u), f(u, y)).
```

In particular, for $y = e$, resp. $x = e$, one obtains, respectively,

```text
x = f(x, e) = h(f(u, e), f(x, u)) = h(u, f(x, u)) = f(x, u),
y = f(e, y) = h(f(e, u), f(u, y)) = h(u, f(u, y)) = f(u, y),
```

whence, on substituting in the original equality,

```text
h(y, x) = f(x, y) = h(x, y).
```

This proves the lemma, and thus Proposition 3.9. From 3.9 one then deduces the following corollaries.

**Corollary 3.9.1.** *If $X$ is an $S$-$H$-functor satisfying (E) with respect to $S$, every element of $X(I_{S}(M))$
which projects onto the unit element of $X(S)$ is invertible.*

<!-- label: III.II.3.9.1 -->

**Corollary 3.9.2.** *If $X$ is an $S$-monoid satisfying (E) with respect to $S$, an element of $X(I_{S}(M))$ is
invertible if and only if its image in $X(S)$ is.*

<!-- label: III.II.3.9.2 -->

<!-- original page 56 -->

**Corollary 3.9.3.** *If $X$ is an $S$-group satisfying (E) with respect to $S$, the two $S$-group laws on $Lie(X/S, M)$
coincide.*

<!-- label: III.II.3.9.3 -->

**Corollary 3.9.4.**[^N.D.E-II-35] *Let $G$ be an $S$-group satisfying (E) with respect to $S$. For $n \in \mathbb{Z}$,
let $n_{G} : G \to G$ be the morphism of $S$-functors defined by $g \mapsto g^{n}$. Then the derived morphism
$L(n_{G}) : Lie(G/S) \to Lie(G/S)$ is "multiplication by $n$", i.e. the map that to every $x \in Lie(G/S)(S')$
associates `n x`.*

<!-- label: III.II.3.9.4 -->

Let us first remark that $n_{G}$ is not in general a morphism of groups, but it preserves the unit section $e : S \to
G$, so the derived morphism $L(n_{G})$ indeed sends $Lie(G/S) = L^{e}_{X/S}$ into itself. If one denotes by $i$ the
inclusion $Lie(G/S) \hookrightarrow T_{G/S}$, then $L(n_{G})$ is defined by the equality $i(L(n_{G})(x)) = i(x)^{n}$,
for every $S' \to S$ and $x \in Lie(G/S)(S')$. Now, by 3.9, the two group laws on $Lie(G/S)$ (coming from condition (E)
and coming from the law of $G$) coincide, i.e. one has $i(x)^{n} = i(n x)$, whence $L(n_{G})(x) = n x$.

Before drawing other consequences of Proposition 3.9, let us prove another functoriality result:

**Proposition 3.11.** *In the situation of Section 1, one has an isomorphism functorial in $M$*

<!-- label: III.II.3.11 -->

$$ T_{\operatorname{Hom}_{Z/S}(X,Y)/S}(M) \xrightarrow{\sim} \operatorname{Hom}_{Z/S}(X, T_{Y/Z}(M)). $$

Indeed, by definition (cf. 3.1):

```text
T_{Hom_{Z/S}(X,Y)/S}(M) = Hom_S(I_S(M), Hom_{Z/S}(X, Y)).
```

By the isomorphism (4) of 1.1, applied to $T = I_{S}(M)$, one has:

```text
Hom_S(I_S(M), Hom_{Z/S}(X, Y)) ≃ Hom_{Z/S}(X, Hom_Z(Z ×_S I_S(M), Y)).
```

Taking into account the isomorphism $Z \times_{S} I_{S}(M) \simeq I_{Z}(M)$, this gives

```text
T_{Hom_{Z/S}(X,Y)/S}(M) ≃ Hom_{Z/S}(X, Hom_Z(I_Z(M), Y)) = Hom_{Z/S}(X, T_{Y/Z}(M)).
```

**Corollary 3.11.1.** *If $Y/Z$ satisfies (E), then $\operatorname{Hom}_{Z/S}(X, Y)/S$ satisfies (E) and the isomorphism
of 3.11 respects the $O$-module structures above $\operatorname{Hom}_{Z/S}(X, Y)$.*[^N.D.E-II-36]

<!-- label: III.II.3.11.1 -->

*Proof.* Let `M, N` be two free `O_S`-modules of finite type. If $Y/Z$ satisfies (E), then

```text
T_{Y/Z}(M ⊕ N) ≃ T_{Y/Z}(M) ×_Y T_{Y/Z}(N).
```

The right-hand term is a subfunctor of $T_{Y/Z}(M) \times_{S} T_{Y/Z}(N)$ and via the isomorphism of 1.2 (∗), one
obtains an isomorphism

```text
Hom_{Z/S}(X, T_{Y/Z}(M ⊕ N)) ≃
   Hom_{Z/S}(X, T_{Y/Z}(M)) ×_{Hom_{Z/S}(X,Y)} Hom_{Z/S}(X, T_{Y/Z}(N)).
```

Combined with 3.11, this implies:

```text
T_{Hom_{Z/S}(X,Y)/S}(M ⊕ N) ≃
   T_{Hom_{Z/S}(X,Y)/S}(M) ×_{Hom_{Z/S}(X,Y)} T_{Hom_{Z/S}(X,Y)/S}(N),
```

so $\operatorname{Hom}_{Z/S}(X, Y)$ satisfies (E) with respect to $S$. This proves the first assertion of the corollary.

Let us see the second. Denote by $H = \operatorname{Hom}_{Z/S}(X, Y)$ and give ourselves an $S$-morphism $\Delta : H'
\to \operatorname{Hom}_{Z/S}(X, Y)$, i.e., a $Z$-morphism $\delta : H' \times_{S} X \to Y$, which therefore makes $H'
\times_{S} X$ a $Y$-object.

On the one hand, one has a commutative diagram:

```text
   Hom_H(H′, Hom_{Z/S}(X, T_{Y/Z}(M))) ───→ Hom_S(H′, Hom_{Z/S}(X, T_{Y/Z}(M)))

   Hom_Y(H′ ×_S X, T_{Y/Z}(M)) ──────────→ Hom_Z(H′ ×_S X, T_{Y/Z}(M))

   { ψ ∈ Hom_Z(I_{H′ ×_S X}(M), Y) | ψ ∘ ε_M = δ } ──→ Hom_Z(I_{H′ ×_S X}(M), Y) .
```

By 1.3, the action of $\alpha \in O(H' \times_{S} X)$ on $\Psi \in \operatorname{Hom}_{Y}(H' \times_{S} X, T_{Y/Z}(M))$
is given by: for every $U \to S$ and $(h, x) \in \operatorname{Hom}_{S}(U, H' \times_{S} X)$ ($U$ being then above $Y$
via $\delta \circ (h, x)$),

```text
(αΨ)(h, x) = α(h, x) Ψ(h, x),
```

where $\alpha(h, x) \in O(U)$ acts on $\Psi(h, x) \in T_{Y/Z}(M)(U)$ via the structure of `O_Y`-module of $T_{Y/Z}(M)$.
By 3.4.2, this last is given, via the identification

```text
Hom_Y(H′ ×_S X, T_{Y/Z}(M)) = { ψ ∈ Hom_Z(I_{H′ ×_S X}(M), Y) | ψ ∘ ε_M = δ },
```

by: for every $(m, h, x) \in \operatorname{Hom}_{S}(U, I_{S}(M) \times_{S} H' \times_{S} X)$,

```text
(1)   (αψ)(m, h, x) = ψ(m · α(h, x), h, x).
```

<!-- original page 66 -->

On the other hand, consider the tangent space $T_{H/S}(M) = \operatorname{Hom}_{S}(I_{S}(M), H)$; one has a commutative
diagram:

```text
   Hom_H(H′, T_{H/S}(M)) ──────────→ Hom_S(H′, T_{H/S}(M))

   { Φ ∈ Hom_S(I_{H′}(M), H) | Φ ∘ ε_M = Δ } ────────→ Hom_S(I_{H′}(M), H)
                          (∗)
   { φ ∈ Hom_Z(I_{H′ ×_S X}(M), Y) | φ ∘ ε_M = δ } ────→ Hom_Z(I_{H′ ×_S X}(M), Y) ,
```

where the bijection (∗) is given as follows (cf. 1.1 (2) and I 1.7.1): for every $U \to S$ and $(m, h, x) \in
\operatorname{Hom}_{S}(U, I_{S}(M) \times_{S} H' \times_{S} X)$ (so that $U$ is above $Z$ via $U \xrightarrow{x} X \to
Z$), one has $\Phi(m, h) \in \operatorname{Hom}_{Z}(X \times_{S} U, Y)$ and

```text
(†)   φ(m, h, x) = Φ(m, h) ∘ (x × id_U) ∈ Hom_Z(U, Y).
```

By 3.4.2 (where one replaces $X$ by $\operatorname{Hom}_{Z/S}(X, Y)$ and $X'$ by $H'$), the action of $a \in O(H')$ on
$\Phi \in \operatorname{Hom}_{S}(I_{H'}(M), H)$ is given by: for every $U \to S$ and $(m, h) \in
\operatorname{Hom}_{S}(U, I_{S}(M) \times_{S} H')$,

```text
(aΦ)(m, h) = Φ(m · a(h), h).
```

Consequently, if $\phi$ (resp. $a\phi$) is the element of $\operatorname{Hom}_{Z}(I_{H' \times_{S} X}(M), Y)$ associated
with $\Phi$ (resp. $a\Phi$), one has, by (†),

```text
(2)   (aφ)(m, h, x) = Φ(m · a(h), h) ∘ (x × id_U) = φ(m · a(h), h, x).
```

Combined with (1), this shows that the isomorphism $T_{H/S}(M) \xrightarrow{\sim} \operatorname{Hom}_{Z/S}(X,
T_{Y/Z}(M))$ of 3.11.1 is an isomorphism of $O(H)$-modules; moreover, for every $H' \to H$, the structure of
$O(H')$-module on $\operatorname{Hom}_{H}(H', T_{H/S}(M))$ extends, in a manner functorial in $H'$, to a structure of
$O(H' \times_{S} X)$-module.

In particular, for $Z = S$, one obtains the following corollary.

**Corollary 3.11.2.** *One has an isomorphism functorial in $M$*

<!-- label: III.II.3.11.2 -->

$$ T_{\operatorname{Hom}_{S}(X,Y)/S}(M) \xrightarrow{\sim} \operatorname{Hom}_{S}(X, T_{Y/S}(M)). $$

*Moreover, if $Y/S$ satisfies (E), then $\operatorname{Hom}_{S}(X, Y)/S$ satisfies (E) and the preceding isomorphism
respects the $O$-module structures above $\operatorname{Hom}_{S}(X, Y)$.*

[^N.D.E-II-37] Let $u : X \to Y$ be an $S$-morphism; one identifies it with the constant morphism $u : S \to
\operatorname{Hom}_{S}(X, Y)$ such that $u(f) = u$ for every $f : S' \to S$. One sees at once that the fiber product of
$u$ and of $\operatorname{Hom}_{S}(X, T_{Y/S}(M)) \to \operatorname{Hom}_{S}(X, Y)$ is identified with
$\operatorname{Hom}_{Y/S}(X, T_{Y/S}(M))$, where $X$ is above $Y$ via $u$. Consequently, from the definition of
$L^{u}_{\operatorname{Hom}_{S}(X,Y)/S}(M)$ and the preceding corollary one deduces:

**Corollary 3.11.3.** *Let $u : X \to Y$ be an $S$-morphism. One has an isomorphism functorial in $M$ (where in the
right-hand term $X$ is above $Y$ via $u$):*

<!-- label: III.II.3.11.3 -->

$$ L^{u}_{\operatorname{Hom}_{S}(X,Y)/S}(M) \xrightarrow{\sim} \operatorname{Hom}_{Y/S}(X, T_{Y/S}(M)). $$

[^N.D.E-II-38] *It is an isomorphism of `O_S`-modules if $Y/S$ satisfies (E).*

In particular, for $Y = X$, $\operatorname{End}_{S}(X)$ is an $S$-functor of monoids, hence a fortiori an
$S$-$H$-functor; recalling that $Lie(\operatorname{End}_{S}(X)/S, M)$ denotes $L^{e}_{\operatorname{End}_{S}(X)/S}(M)$,
where $e$ is the unit section (cf. 3.9.0.1), one obtains:

**Corollary 3.11.4.** *One has an isomorphism functorial in $M$*

<!-- label: III.II.3.11.4 -->

<!-- original page 57 -->

```text
Lie(End_S(X)/S, M) ⥲ ∏_{X/S} T_{X/S}(M);
```

[^N.D.E-II-38] *it is an isomorphism of `O_S`-modules if $X/S$ satisfies (E).*

**Remark 3.11.5.**[^N.D.E-II-39] Suppose that $X/S$ satisfies (E). Then $\prod_{X/S} T_{X/S}(M) =
\operatorname{Hom}_{X/S}(X, T_{X/S}(M))$ is equipped with a structure of $(\prod_{X/S} O_{X})$-module, i.e. for every
$S' \to S$,

<!-- label: III.II.3.11.5 -->

```text
Hom_{X/S}(X, T_{X/S}(M))(S′) = { ψ ∈ Hom_X(I_{S′}(M) ×_S X, X) | ψ ∘ (ε_M × id_X) = pr_X }
```

is equipped with a structure of $O(X \times_{S} S')$-module, functorial in $S'$. This follows, at one's choice, from 3.6
and the properties of the functor $\prod_{X/S}$ (cf. 1.2), or from the proof of 3.11.1.

We shall now interpret geometrically the definition of the tangent bundle.

[^N.D.E-II-40] Let $U$ be an $S$-functor; by I 1.7.2, one has isomorphisms functorial in $M$

```text
T_{X/S}(M)(U) = Hom_S(U, Hom_S(I_S(M), X)) ≃ Hom_S(I_S(M), Hom_S(U, X))
              ≃ Hom_{I_S(M)}(U_{I_S(M)}, X_{I_S(M)}).
```

In particular, the morphism $M \to 0$ gives a commutative diagram:

```text
   Hom_S(U, T_{X/S}(M))  ⥲  Hom_{I_S(M)}(U_{I_S(M)}, X_{I_S(M)})
            │                              │
            │ π_M                          │ identity
            ↓                              ↓
   Hom_S(U, X)  ─────────────────────→  Hom_S(U, X) ,
```

where the second vertical arrow is obtained by the base change $\epsilon_{M} : S \to I_{S}(M)$.[^N.D.E-II-41]

In consequence:

**Proposition 3.12.** *Let $h_{0} : U \to X$ be an $S$-morphism. Then $\operatorname{Hom}_{X}(U, T_{X/S}(M))$ is
identified with the set of $I_{S}(M)$-morphisms from $U_{I_{S}(M)}$ to $X_{I_{S}(M)}$ which restrict to $h_{0}$ on $U$
(viewed as a subobject of $U \times_{S} I_{S}(M)$ via $id_{U} \times_{S} \epsilon_{M}$).*

<!-- label: III.II.3.12 -->

[^N.D.E-II-42] In particular, for $U = X$ and $h_{0} = id_{X}$, one obtains the

**Corollary 3.12.1.** *The set $\Gamma(T_{X/S}(M)/X)$ is identified with the set of $I_{S}(M)$-endomorphisms $\phi$ of
$X_{I_{S}(M)}$ which induce the identity on $X$, i.e. such that the following diagram be commutative:*[^N.D.E-II-43]

<!-- label: III.II.3.12.1 -->

```text
                  φ
   I_X(M) ──────────→ I_X(M)
      ↑                   ↑
   ε_M                    ε_M
                id
       X ──────────────→  X .
```

<!-- original page 58 -->

[^N.D.E-II-44] On the other hand, by 3.11.2, $\Gamma(T_{X/S}(M)/X) \simeq Lie(\operatorname{End}_{S}(X)/S, M)(S)$; if
moreover $X/S$ satisfies (E), then $\operatorname{End}_{S}(X)/S$ satisfies (E), so $Lie(\operatorname{End}_{S}(X)/S, M)$
is an `O_S`-module by 3.6 (and in fact a $(\prod_{X/S} O_{X})$-module, by 3.11.5). Applying 3.9, one deduces the

**Proposition 3.13.** *If $X/S$ satisfies (E), the abelian group $\Gamma(T_{X/S}(M)/X)$ is identified with the set of
$I_{S}(M)$-endomorphisms of $X_{I_{S}(M)}$ inducing the identity on $X$. Consequently, every $I_{S}(M)$-endomorphism of
$X_{I_{S}(M)}$ which induces the identity on $X$ is an automorphism.*

<!-- label: III.II.3.13 -->

**Corollary 3.13.1.** *Let $u : X \to Y$ be an $S$-isomorphism, $Y/S$ satisfying (E). Every $I_{S}(M)$-morphism from
$X_{I_{S}(M)}$ into $Y_{I_{S}(M)}$ which extends $u$ is an isomorphism.*

<!-- label: III.II.3.13.1 -->

**Corollary 3.13.2.** *If $Y/S$ satisfies (E), then the monomorphism $Isom_{S}(X, Y) \to \operatorname{Hom}_{S}(X, Y)$
induces, for every $u \in Isom_{S}(X, Y)$, an isomorphism*

<!-- label: III.II.3.13.2 -->

$$ L^{u}_{Isom_{S}(X,Y)/S}(M) \xrightarrow{\sim} L^{u}_{\operatorname{Hom}_{S}(X,Y)/S}(M). $$

*Proof.*[^N.D.E-II-45] One must see that $L^{u}_{Isom_{S}(X,Y)/S}(M)(S') \to
L^{u}_{\operatorname{Hom}_{S}(X,Y)/S}(M)(S')$ is a bijection, for every $S' \to S$. By base change (cf. 3.4), it
suffices to do it for $S' = S$. In this case, $L^{u}_{\operatorname{Hom}_{S}(X,Y)/S}(M)(S)$ (resp.
$L^{u}_{Isom_{S}(X,Y)/S}(M)(S)$) is the set of $I_{S}(M)$-morphisms (resp. automorphisms) $X_{I_{S}(M)} \to
Y_{I_{S}(M)}$ which extend $u$, and one applies the preceding corollary.

<!-- original page 69 -->

**Corollary 3.13.3.** *If $X/S$ satisfies (E), the monomorphism $\operatorname{Aut}_{S}(X) \to
\operatorname{End}_{S}(X)$ induces, for every $u \in \operatorname{Aut}_{S}(X)$, an isomorphism
$L^{u}_{\operatorname{Aut}_{S}(X)/S}(M) \xrightarrow{\sim} L^{u}_{\operatorname{End}_{S}(X)/S}(M)$. In particular, one
has*

<!-- label: III.II.3.13.3 -->

```text
Lie(Aut_S(X)/S, M) ⥲ Lie(End_S(X)/S, M) ⥲ ∏_{X/S} T_{X/S}(M),
```

[^N.D.E-II-46] *so that $Lie(\operatorname{Aut}_{S}(X)/S, M)$ is equipped with a structure of $(\prod_{X/S}
O_{X})$-module.*

**3.14.** Suppose to conclude that $X$ is representable.[^N.D.E-II-47] In this case, one saw in 2.2.2 that the
$X$-functor $T_{X/S}$ is representable by $V(\Omega^{1}_{X/S})$, whence bijections:

```text
Γ(T_{X/S}/X) ≃ Hom_X(Ω¹_{X/S}, O_X) ≃ Dér_{O_S}(O_X).
```

This is also deduced from what precedes, as follows. By 3.13, $\Gamma(T_{X/S}/X)$ is identified with the set of
infinitesimal endomorphisms of $X$ (i.e. of `I_S`-endomorphisms of $X_{I_{S}}$ inducing the identity on $X$). Now $X$
and $X_{I_{S}}$ have the same underlying topological space, the corresponding rings of sheaves being `O_X` and
$D_{O_{X}} = O_{X} \oplus M$, where $M = O_{X}$ is considered as ideal of square zero. Denoting by $\pi : D_{O_{X}} \to
O_{X}$ the morphism of `O_X`-algebras that vanishes on $M$, one deduces that to give an infinitesimal endomorphism of
$X$ is equivalent to giving a morphism of `O_S`-algebras $\phi : O_{X} \to D_{O_{X}}$ such that $\pi \circ \phi =
id_{O_{X}}$, which is equivalent to giving an `O_S`-derivation of the sheaf of rings `O_X`.

Moreover, one sees easily that if $D, D' \in D\acute{e}r_{O_{S}}(O_{X})$ and if one denotes by $\phi_{D}$ the
infinitesimal endomorphism corresponding to $D$, then

$$ \phi_{D+D'} = \phi_{D} \circ \phi_{D'}. $$

This shows that the identification

```text
{ infinitesimal endomorphisms of X } ≃ Dér_{O_S}(O_X)
```

is an isomorphism of abelian groups. Taking into account 3.13 (and 3.11.5), one has therefore constructed an isomorphism
of abelian groups (and even of $O(X)$-modules)

<!-- original page 59 -->

$$ \Gamma(T_{X/S}/X) \xrightarrow{\sim} D\acute{e}r_{O_{S}}(O_{X}), $$

which recovers the classical interpretation of tangent vector fields in terms of derivations of the structure
sheaf.[^N.D.E-II-48] Let us remark in passing that $\Gamma(T_{X/S}/X)$ is equal to $H^{0}(X, g_{X/S})$, where $g_{X/S}$
is the dual of $\Omega^{1}_{X/S}$.

## 4. Tangent space to a group — Lie algebras

<!-- label: III.II.4 -->

**4.1.** Let $G$ be a group-functor above $S$. By 3.9.0.2, $T_{G/S}(M)$ and $Lie(G/S, M)$ are equipped with structures
of groups above $S$ and one has morphisms of groups

```text
                       i                p
   Lie(G/S, M) ────────→ T_{G/S}(M) ⇄ G ;
                                     s
```

by definition $i$ is an isomorphism of $Lie(G/S)(M)$ onto the kernel of $p$ and $s$ is a section of $p$. It then follows
from I 2.3.7 that this sequence of morphisms allows one to identify $T_{G/S}(M)$ with the semi-direct product of $G$ by
$Lie(G/S, M)$.

**Definition 4.1.A.**[^N.D.E-II-49] *The corresponding action of $G$ on $Lie(G/S, M)$ is denoted*

<!-- label: III.II.4.1.A -->

```text
Ad : G ⟶ Aut_{S-gr.}(Lie(G/S, M))
```

*and called the* **adjoint representation** *(relative to $M$) of $G$; one has therefore by definition, for $x \in
G(S')$ and $X \in Lie(G/S, M)(S')$:*

```text
Ad(x) X = i^{-1}(s(x) i(X) s(x)^{-1}).
```

*If $G$ is commutative, then $T_{G/S}(M)$ is also commutative and $Ad(x) X = X$.*

**Definition 4.1.B.**[^N.D.E-II-49] *If $G$ and $H$ are two group-functors above $S$ and if $f : G \to H$ is a morphism
of groups, by functoriality there is deduced a morphism of exact sequences compatible with the canonical sections:*

<!-- label: III.II.4.1.B -->

```text
   1 ─→ Lie(G/S, M) ─→ T_{G/S}(M) ─→ G ─→ 1
            │ L(f)         │ T(f)       │ f
            ↓              ↓            ↓
   1 ─→ Lie(H/S, M) ─→ T_{H/S}(M) ─→ H ─→ 1 ;
```

<!-- original page 60 -->

*$L(f)$, which we shall also write $Lie(f)$, is the* **derived morphism** *of $f$.*[^N.D.E-II-50]

**Remark 4.1.C.**[^N.D.E-II-51] *If $G/S$ and $H/S$ satisfy (E), then $L(f)$ respects the `O_S`-module structures
deduced from "functoriality in $M$" (cf. 3.6).*

<!-- label: III.II.4.1.C -->

**Proposition 4.1.1.** *Let $g \in G(S)$. Then $Ad(g) : Lie(G/S, M) \to Lie(G/S, M)$ is the derived morphism of
$Int(g) : G \to G$.*

<!-- label: III.II.4.1.1 -->

Indeed $Ad(g) X = i^{-1}(Int(g) i(X))$, which is nothing other than $L(Int(g))(X)$ by the very definition of the derived
morphism.

Suppose that $G/S$ satisfies (E). Then, by Proposition 3.9, the group structure on $Lie(G/S, M)$ defined as above is
nothing other than the structure induced by its `O_S`-module structure (defined thanks to (E)). One then deduces from
the preceding proposition and the functoriality of the action of `O_S` (cf. 3.6) the corollary:

**Corollary 4.1.1.1.** *Suppose that $G/S$ satisfies (E). Then `Ad` sends $G$ into the subgroup*

<!-- label: III.II.4.1.1.1 -->

```text
Aut_{O_S-mod.}(Lie(G/S, M))
```

*of $\operatorname{Aut}_{S-gr.}(Lie(G/S, M))$, i.e., for every $g \in G(S')$, $Ad(g)$ respects the $O_{S'}$-module
structure of $Lie(G'/S', M)$ (where $G' = G \times_{S} S'$). In other words, `Ad` is a* **linear representation** *(cf.
I, 3.2) of $G$ in the `O_S`-module $Lie(G/S, M)$.*

**Remarks 4.1.1.2.** *a) For $G/S$ to satisfy (E), it is necessary and sufficient that for every pair $(M, N)$ of free
`O_S`-modules of finite type, the diagram*

<!-- label: III.II.4.1.1.2 -->

```text
                Lie(G/S, M ⊕ N)
              ↙                ↘
        Lie(G/S, M)        Lie(G/S, N)
              ↘                ↙
                Lie(G/S, 0) = S ,
```

*obtained by applying the functor $Lie(G/S, -)$ to the diagram (∗) of 2.1, be cartesian.*

*b) Suppose that $G/S$ satisfies (E). Then the derived morphism of the group law $\pi : G \times_{S} G \to G$ is nothing
other than the addition law in $Lie(G/S, M)$.* (N.B. $\pi$ is not a morphism of groups, but $\pi(e, e) = e$, so the
derived morphism $L(\pi)$ sends $T^{(e,e)}_{(G\times_{S} G)/S}(M) = Lie(G/S, M) \times_{S} Lie(G/S, M)$ into $Lie(G/S,
M)$, cf. 3.7 and 3.8.) For every $n \in \mathbb{Z}$, one shows likewise that if one denotes by $n_{G} : G \to G$ the
morphism of $S$-functors defined by $g \mapsto g^{n}$, then the derived morphism $L(n_{G})$ is multiplication by $n$ on
$Lie(G/S)$, cf. 3.9.4.

<!-- original page 61 -->

**4.1.2.0.**[^N.D.E-II-52] Consider now the $S$-functor $\operatorname{Hom}_{G/S}(G, T_{G/S}(M))$; for every $S' \to S$,
one has $T_{G/S}(M)_{S'} \simeq T_{G_{S'}/S'}(M)$ (cf. 3.4) and therefore:

```text
Hom_{G/S}(G, T_{G/S}(M))(S′) ≃ Hom_{G_{S′}}(G_{S′}, T_{G_{S′}/S′}(M)) = Γ(T_{G_{S′}/S′}(M)/G_{S′}).
```

Note first that one has an isomorphism, functorial in $S'$,

```text
(∗)   Hom_{S′}(G_{S′}, Lie(G_{S′}/S′, M)) ⥲ Γ(T_{G_{S′}/S′}(M)/G_{S′})
```

which to every $f : G_{S'} \to Lie(G_{S'}/S', M)$ associates the section $s_{f} : G_{S'} \to T_{G_{S'}/S'}(M)$ such
that, for every $S'' \to S'$ and $g \in G(S'')$:

$$ s_{f}(g) = i(f(g)) s(g). $$

<!-- original page 72 -->

Let $h$ be an automorphism of the functor $G_{S'}$ above $S'$, not necessarily respecting the group structure. To every
section $\tau$ of $T_{G_{S'}/S'}(M)$, one can associate $h(\tau)$ defined by transport of structure: it is, for example,
the only section of $T_{G_{S'}/S'}(M)$ making commutative the diagram

```text
              τ
   G_{S′} ─────────→ T_{G_{S′}/S′}(M)
       │                        │
       h                       T(h)
       │            h(τ)        │
       ↓                        ↓
   G_{S′} ─────────→ T_{G_{S′}/S′}(M) .
```

In particular, take for $h$ the right translation $t_{x}$ by an element $x$ of $G(S')$, i.e., $h(g) = t_{x}(g) = g \cdot
x$, for every $g \in G(S'')$, $S'' \to S'$. Then one has immediately

$$ t_{x}(s_{f}) = s_{t_{x}(f)} $$

where $t_{x}(f)$ denotes the morphism from $G_{S'}$ into $Lie(G_{S'}/S', M)$ defined by

$$ t_{x}(f)(g) = f(g \cdot x^{-1}), $$

for every $g \in G(S'')$, $S'' \to S'$.

It follows that if one makes $G$ act by right translations on

```text
Hom_{G/S}(G, T_{G/S}(M))    and    Hom_S(G, Lie(G/S, M))
```

in the following way: for every $S' \to S$, $x \in G(S')$, $\sigma \in \Gamma(T_{G_{S'}/S'}(M)/G_{S'})$ and $f \in
\operatorname{Hom}_{S'}(G_{S'}, Lie(G_{S'}/S', M))$,

```text
(σ · x)(g) = σ(g · x^{-1}) · s(x)    and    (f · x)(g) = f(g · x^{-1}),
```

for every $g \in G(S'')$, $S'' \to S'$, then the isomorphism (∗) above respects the actions of $G$.

In particular, by this isomorphism, the elements of $\operatorname{Hom}_{G/S}(G, T_{G/S}(M))^{G}(S')$ correspond to the
constant morphisms from $G_{S'}$ into $Lie(G_{S'}/S', M)$ (i.e. factoring through the projection $G_{S'} \to S'$) or
also to the elements of $Lie(G_{S'}/S', M)(S') = Lie(G/S, M)(S')$.

*Terminology.* The elements of $\operatorname{Hom}_{G/S}(G, T_{G/S}(M))^{G}(S')$ will be called "sections of
$T_{G_{S'}/S'}(M)$ invariant under right translation".

One then obtains the:

**Proposition 4.1.2.**[^II-4-1] *The map $Lie(G/S, M)(S) \to \Gamma(T_{G/S}(M)/G)$ which to $X \in Lie(G/S, M)(S)$
associates the section $x \mapsto X \cdot x$ is a bijection of $Lie(G/S, M)(S)$ onto the part of $\Gamma(T_{G/S}(M)/G)$
formed by the sections invariant under right translation.*

<!-- label: III.II.4.1.2 -->

<!-- original page 73 -->

Likewise, one makes $G$ act on the right on $\operatorname{End}_{I_{S}(M)/S}(G_{I_{S}(M)})$ as follows: for every $S'
\to S$, $x \in G(S')$ and $u \in \operatorname{End}_{I_{S}(M)/S}(G_{I_{S}(M)})(S') =
\operatorname{End}_{I_{S'}(M)}(G_{I_{S'}(M)})$,

```text
(u · x)(g) = u(g · x^{-1}) · x,
```

for every $g \in G(S'')$, $S'' \to I_{S'}(M)$. Then the morphism of 3.12.1

$$ \operatorname{Hom}_{G/S}(G, T_{G/S}(M)) \longrightarrow \operatorname{End}_{I_{S}(M)/S}(G_{I_{S}(M)}) $$

respects the actions of $G$ and therefore induces, for every $S' \to S$, a bijection between
$\Gamma(T_{G_{S'}/S'}(M)/G_{S'})$ and the set of $I_{S'}(M)$-endomorphisms $u$ of $G_{I_{S'}(M)}$ which induce the
identity on $G$ and "commute with right translations", i.e. which verify $u_{S''} \cdot x = u_{S''}$ for every $S'' \to
S'$ and $x \in G(S'')$. One obtains therefore:

**Proposition 4.1.3.**[^II-4-1] *There exists a bijection functorial in $G$ between the set $Lie(G/S, M)(S)$ and the set
of $I_{S}(M)$-endomorphisms of $G_{I_{S}(M)}$ inducing the identity on $G$ and commuting with the right translations of
$G$ (in the sense indicated above).*

<!-- label: III.II.4.1.3 -->

Taking now into account 3.13:

**Theorem 4.1.4.**[^II-4-1] *Let $G$ be an $S$-functor of groups; suppose that $G/S$ satisfies (E). Then the group
$Lie(G/S, M)(S)$ is identified, functorially in $G$, with the group of $I_{S}(M)$-automorphisms of $G_{I_{S}(M)}$
inducing the identity on $G$ and commuting with the right translations of $G$ (in the sense indicated above).*

<!-- label: III.II.4.1.4 -->

One thus recovers (in the case $M = O_{S}$) one of the classical definitions of the Lie algebra of a group.

**4.2.0.**[^N.D.E-II-54] Before going further, let us establish new corollaries of 3.11. Let `X, Y` be above $Z$, with
$Z$ above $S$, as in Section 1. As one saw in 3.11, the isomorphisms 1.1 (4):

```text
(1)   Hom_S(I_S(M), Hom_{Z/S}(X, Y)) ⥲ Hom_{Z/S}(X, Hom_Z(I_Z(M), Y))
                                     ≃ Hom_{Z/S}(X ×_S I_S(M), Y)
```

induce the isomorphism $\theta$ below:

```text
(2)   T_{Hom_{Z/S}(X,Y)}(M) ⥲ Hom_{Z/S}(X, T_{Y/Z}(M))
                            ≃ Hom_{Z/S}(X ×_S I_S(M), Y) .
```

<!-- original page 74 -->

By 1.3, if $Y$ is a $Z$-group, so is $\operatorname{Hom}_{Z}(V, Y)$ for every $V \to Z$ (in particular for $V =
I_{Z}(M)$); explicitly, if $Z'' \to Z' \to Z$ and $\phi, \psi \in \operatorname{Hom}_{Z}(V_{Z'}, Y)$, then $\phi \cdot
\psi$ is defined by $(\phi \cdot \psi)(v) = \phi(v) \psi(v)$, for every $v \in V_{Z'}(Z'')$.

Suppose now that $X$ and $Y$ are $Z$-groups and let us pose the following definition.

**Definition 4.2.0.1.** *Let $\operatorname{Hom}_{(Z/S)-gr.}(X, Y)$ be the subfunctor of $\operatorname{Hom}_{Z/S}(X,
Y)$ defined by: for every $S' \to S$,*

<!-- label: III.II.4.2.0.1 -->

```text
(3)   Hom_{(Z/S)-gr.}(X, Y)(S′) = Hom_{Z_{S′}-gr.}(X_{S′}, Y_{S′}).
```

*This definition applies equally when one replaces $Y$ by the $Z$-group $T_{Y/Z}(M)$.*

One then sees easily that $T_{\operatorname{Hom}_{(Z/S)-gr.}(X,Y)/S}(M)(S')$ corresponds, in the preceding isomorphisms
(2), to the $Z_{S'}$-morphisms

```text
φ : X_{S′} ×_{S′} I_{S′}(M) ⟶ Y_{S′}
```

which are "multiplicative in $X$", i.e. which verify $\phi(x_{1} x_{2}, m) = \phi(x_{1}, m) \phi(x_{2}, m)$, and these
correspond to the morphisms of $Z_{S'}$-groups $X_{S'} \to T_{Y/Z}(M)_{S'}$. One has thus obtained:

**Proposition 4.2.0.2.** *Let `X, Y` be $Z$-groups, with $Z$ above $S$. One has isomorphisms of $S$-functors, functorial
in $M$:*

<!-- label: III.II.4.2.0.2 -->

$$ T_{\operatorname{Hom}_{(Z/S)-gr.}(X,Y)}(M) \xrightarrow{\sim} \operatorname{Hom}_{(Z/S)-gr.}(X, T_{Y/Z}(M)). $$

In particular, for $Z = S$, one obtains the following corollary. Before stating it, let us remark that if $Y$ is a
commutative $S$-group, so is $T_{Y/S}(M)$, then $H = \operatorname{Hom}_{S-gr.}(X, Y)$ and
$\operatorname{Hom}_{S-gr.}(X, T_{Y/S}(M))$, and finally $T_{H/S}(M)$.

**Corollary 4.2.0.3.** *Let `X, Y` be $S$-groups. One has isomorphisms of $S$-functors, functorial in $M$:*

<!-- label: III.II.4.2.0.3 -->

$$ T_{\operatorname{Hom}_{S-gr.}(X,Y)/S}(M) \xrightarrow{\sim} \operatorname{Hom}_{S-gr.}(X, T_{Y/S}(M)). $$

*If $Y$ is commutative, these are moreover isomorphisms of abelian $S$-groups.*

**Definition 4.2.0.4.**[^N.D.E-II-55] *If $Y$ is an `O_S`-module, the functor $T_{Y/S}(M)$ (resp. $Lie(Y/S, M)$) is
equipped with an `O_S`-module structure deduced from that of $Y$. Equipped with this structure, it will be denoted
$T'_{Y/S}(M)$ (resp. $Lie'(Y/S, M)$).*

<!-- label: III.II.4.2.0.4 -->

Consequently, if `X, Y` are `O_S`-modules, then $T'_{Y/S}(M) = \operatorname{Hom}_{S}(I_{S}(M), Y)$ and $H =
\operatorname{Hom}_{O_{S}-mod.}(X, Y)$, then $\operatorname{Hom}_{O_{S}-mod.}(X, T'_{Y/S}(M))$ and $T'_{H/S}(M)$, are
equipped with an `O_S`-module structure, and one obtains the:

<!-- original page 75 -->

**Corollary 4.2.0.5.** *If `X, Y` are `O_S`-modules, one has isomorphisms of `O_S`-modules, functorial in $M$:*

<!-- label: III.II.4.2.0.5 -->

```text
T′_{Hom_{O_S-mod.}(X,Y)/S}(M) ⥲ Hom_{O_S-mod.}(X, T′_{Y/S}(M)).
```

**Definition 4.2.A.**[^N.D.E-II-56] *Let `X, L` be $S$-groups, with $X$ acting on $L$ by group automorphisms (cf. I
2.3.5). One defines the subfunctor $Z^{1}_{S}(X, L)$ of $\operatorname{Hom}_{S}(X, L)$ as follows: for every $S' \to
S$,*

<!-- label: III.II.4.2.A -->

```text
Z¹_S(X, L)(S′) = { φ ∈ Hom_{S′}(X_{S′}, L_{S′}) | φ(x_1 x_2) = φ(x_1) (x_1 · φ(x_2)),
                                                 for all x_1, x_2 ∈ X(S″), S″ → S′ }.
```

*It is called the "functor of* **crossed homomorphisms** *from $X$ to $L$".*

**Remark 4.2.B.**[^N.D.E-II-56] *a) If $L'$ is a second $S$-group on which $X$ acts by group automorphisms, one has*

<!-- label: III.II.4.2.B -->

```text
Z¹_S(X, L ×_S L′) ≃ Z¹_S(X, L) ×_S Z¹_S(X, L′).
```

*b) If $L$ is a $G$-`O_S`-module, $Z^{1}_{S}(X, L)$ coincides with the kernel of the differential $\partial :
\operatorname{Hom}_{S}(X, L) \to \operatorname{Hom}_{S}(X^{2}, L)$ defined in I 5.1; in particular, $Z^{1}_{S}(X, L)$ is
in this case an `O_S`-module.*

**4.2.** Let $u : X \to Y$ be a morphism of $S$-groups; then $L^{u}_{\operatorname{Hom}_{S-gr.}(X,Y)/S}(M)$ is described
as follows. First, one saw in 3.11.3 that one has an isomorphism of $S$-functors, functorial in $M$:

<!-- original page 63 -->

```text
(†)   L^u_{Hom_S(X,Y)/S}(M) ⥲ Hom_{Y/S}(X, T_{Y/S}(M)).
```

On the other hand, since $Y$ is an $S$-group, one has

```text
T_{Y/S}(M) = Lie(Y/S, M) · Y = Lie(Y/S, M)_Y;
```

there follows an isomorphism of $S$-functors, functorial in $M$:

```text
L^u_{Hom_S(X,Y)/S}(M) ⥲ Hom_S(X, Lie(Y/S, M)).
```

For every $S' \to S$, let $u' : X' \to Y'$ denote the morphism deduced from $u$ by base change. Consider the $S$-functor
defined as follows:[^N.D.E-II-57] for every $S' \to S$,

```text
Hom_{(Y/S)-gr.}(X, Lie(Y/S, M) · Y)(S′) = Hom_{Y′-gr.}(X′, (Lie(Y/S, M) · Y)_{S′})
                                        = Hom_{Y′-gr.}(X′, Lie(Y′/S′, M) · Y′).
```

Then one sees easily that the isomorphism (†) induces an isomorphism

```text
(†′)   L^u_{Hom_{S-gr.}(X,Y)/S}(M) ⥲ Hom_{(Y/S)-gr.}(X, Lie(Y/S, M) · Y).
```

On the other hand, the morphism

```text
X ──u──→ Y ──Ad──→ Aut_{S-gr.}(Lie(Y/S, M))
```

<!-- original page 76 -->

defines an action of $X$ on $L = Lie(Y/S, M)$ by group automorphisms.

If $\Phi \in \operatorname{Hom}_{Y/S}(X, Lie(Y/S, M) \cdot Y)$, then, for every $S'' \to S' \to S$ and $x \in X(S'')$,
one can write in a unique manner

```text
Φ(S′)(x) = φ(S′)(x) · u′(x),    where φ(S′)(x) ∈ Lie(Y′/S′, M)(S″);
```

this determines an element $\phi$ of $\operatorname{Hom}_{S}(X, Lie(Y/S, M))$. Then $\Phi(S')$ is a morphism of groups
if, and only if, for all $x_{1}, x_{2} \in X(S'')$ one has:

```text
φ(S′)(x_1 x_2) = φ(S′)(x_1) ( u(x_1) φ(S′)(x_2) u(x_1)^{-1} )
              = φ(S′)(x_1) (x_1 · φ(S′)(x_2)),
```

i.e., if and only if $\phi \in Z^{1}_{S}(X, Lie(Y/S, M))$. One has thus obtained the:

**Proposition 4.2.** *Let $u : X \to Y$ be a morphism of $S$-groups. One has an isomorphism of $S$-functors, functorial
in $M$:*

<!-- label: III.II.4.2 -->

```text
L^u_{Hom_{S-gr.}(X,Y)/S}(M) ⥲ Z¹_S(X, Lie(Y/S, M)).
```

[^N.D.E-II-58] Suppose further that $Y/S$ satisfies (E). Then it follows from 4.2.0.3, exactly as in the proof of
3.11.1, that $\operatorname{Hom}_{S-gr.}(X, Y)/S$ satisfies (E). So one has (cf. 3.5.1):

```text
L^u_{Hom_{S-gr.}(X,Y)/S}(M ⊕ N) ≃ L^u_{Hom_{S-gr.}(X,Y)/S}(M) ×_S L^u_{Hom_{S-gr.}(X,Y)/S}(N).
```

(This also follows from 4.2 and 4.2.B a).) Consequently, $L^{u}_{\operatorname{Hom}_{S-gr.}(X,Y)/S}(M)$ is equipped,
like $Z^{1}_{S}(X, Lie(Y/S, M))$ (cf. 4.2.B b)), with an `O_S`-module structure, deduced from functoriality in $M$. One
deduces that the isomorphism of 4.2 is, in this case, an isomorphism of `O_S`-modules:

**Proposition 4.2 bis.**[^N.D.E-II-58] *Let $u : X \to Y$ be a morphism of $S$-groups; suppose that $Y/S$ satisfies (E).
One has an isomorphism of `O_S`-modules, functorial in $M$:*

<!-- label: III.II.4.2-bis -->

```text
L^u_{Hom_{S-gr.}(X,Y)/S}(M) ⥲ Z¹_S(X, Lie(Y/S, M)).
```

Moreover, when $Y/S$ satisfies (E), one deduces from 3.13.1, exactly as in the proof of 3.13.2, that for every $u \in
Isom_{S-gr.}(X, Y)$ one has an isomorphism functorial in $M$:

$$ (\ast) L^{u}_{Isom_{S-gr.}(X,Y)/S}(M) \xrightarrow{\sim} L^{u}_{\operatorname{Hom}_{S-gr.}(X,Y)/S}(M). $$

One deduces from this the following two corollaries.

**Corollary 4.2.1.** *Let $u : X \to Y$ be a morphism of $S$-groups; if $Y/S$ satisfies (E), one has an isomorphism of
`O_S`-modules, functorial in $M$:*

<!-- label: III.II.4.2.1 -->

```text
L^u_{Isom_{S-gr.}(X,Y)/S}(M) ⥲ Z¹_S(X, Lie(Y/S, M)).
```

<!-- original page 77 -->

**Corollary 4.2.2.** *Let $X$ be an $S$-group; if $X/S$ satisfies (E), one has an isomorphism of `O_S`-modules,
functorial in $M$:*

<!-- label: III.II.4.2.2 -->

```text
Lie(Aut_{S-gr.}(X)/S, M) ⥲ Z¹_S(X, Lie(X/S, M)).
```

[^N.D.E-II-59] Moreover, if $Y$ is commutative, the adjoint action of $Y$ on $L = Lie(X/S, M)$ is trivial, whence
$Z^{1}_{S}(X, L) = \operatorname{Hom}_{S-gr.}(X, L)$. Therefore:

**Corollary 4.2.3.** *Let $Y$ be a commutative $S$-group; one has an isomorphism of $S$-functors, functorial in $M$:*

<!-- label: III.II.4.2.3 -->

```text
L^u_{Hom_{S-gr.}(X,Y)/S}(M) ⥲ Hom_{S-gr.}(X, Lie(Y/S, M)).
```

**4.3.** Consider now the case where $X$ and $Y$ are `O_S`-modules. Recall (cf. 4.2.0.4) that one writes $T'_{Y/S}(M)$
(resp. $Lie'(Y/S, M)$) for the functor $T_{Y/S}(M)$ (resp. $Lie(Y/S, M)$) equipped with the `O_S`-module structure
deduced from that of $Y$.

When $Y/S$ satisfies (E), we shall always write $Lie(Y/S, M)$ for the functor $Lie(Y/S, M)$ equipped with the
`O_S`-module structure defined for every functor satisfying (E). In this case, we know (cf. 3.9) that the abelian-group
structures of $Lie(Y/S, M)$ and $Lie'(Y/S, M)$ coincide, but the same is not a priori true for those of module (see a
counterexample in §6.3). For every $S' \to S$ and $a \in O(S')$, we shall write $a \cdot' m$ (resp. $a \cdot m$) for the
action of $a$ on $m \in Lie'(Y/S, M)(S')$ (resp. on $m \in Lie(Y/S, M)(S')$), and similarly for the action of $a$ on
$T'_{Y/S}(M)$ and $T_{Y/S}(M)$.

One has $T'_{Y/S}(M) \simeq Lie'(Y/S, M) \oplus Y$ as `O_S`-modules; consequently one obtains, exactly as for
Propositions 4.2 and 4.2 bis, the:

**Proposition 4.3.** *Let $u : X \to Y$ be a morphism of `O_S`-modules. One has an isomorphism of $S$-functors,
functorial in $M$:*

<!-- label: III.II.4.3 -->

```text
(∗)   L^u_{Hom_{O_S-mod.}(X,Y)/S}(M) ⥲ Hom_{O_S-mod.}(X, Lie′(Y/S, M)).
```

[^N.D.E-II-60] *If $Y/S$ satisfies (E), then $\operatorname{Hom}_{O_{S}-mod.}(X, Y)/S$ satisfies (E) and (∗) is an
isomorphism of `O_S`-modules when one equips both sides with the `O_S`-module structure deduced from functoriality in
$M$.*[^N.D.E-II-61]

**Remark 4.3 bis.**[^N.D.E-II-62] Let $u : X \to Y$ be a morphism of `O_S`-modules; denote by $\tau_{u}$ the map which
to every morphism of `O_S`-modules $\phi : X \to Lie'(Y/S, M)$ associates the morphism

<!-- label: III.II.4.3-bis -->

```text
u ⊕ φ : X ⟶ T′_{Y/S}(M) = Y ⊕ Lie′(Y/S, M).
```

<!-- original page 78 -->

Then the isomorphism of 4.3 fits into the following commutative diagram, functorial in $M$:

```text
   L^u_{Hom_{O_S-mod.}(X,Y)/S}(M)  ⥲  Hom_{O_S-mod.}(X, Lie′(Y/S, M))
            │                                     │
            ↓                                     ↓ τ_u
   T_{Hom_{O_S-mod.}(X,Y)/S}(M)    ⥲   Hom_{O_S-mod.}(X, T′_{Y/S}(M)).
```

Moreover, when $Y/S$ satisfies (E), one deduces from 3.13.1, exactly as in the proof of 3.13.2, that for every $u \in
Isom_{O_{S}-mod.}(X, Y)$, one has

```text
(∗)   L^u_{Isom_{O_S-mod.}(X,Y)/S}(M) = L^u_{Hom_{O_S-mod.}(X,Y)/S}(M).
```

**Corollary 4.3.1.** *Let $X$ be an `O_S`-module satisfying (E) with respect to $S$. One has an isomorphism functorial
in $M$:*

<!-- label: III.II.4.3.1 -->

```text
Lie(Aut_{O_S-mod.}(X)/S, M) ⥲ Hom_{O_S-mod.}(X, Lie′(X/S, M))
```

*which respects the `O_S`-module structures deduced from functoriality in $M$.*[^N.D.E-II-63] *In particular,
$\operatorname{Aut}_{O_{S}-mod.}(X)/S$ satisfies (E).*

*Proof.* The first assertion follows from (∗) and 4.3; let us prove the second. As $X/S$ satisfies (E), one has
isomorphisms of `O_S`-modules `Lie′(X/S, M ⊕ N) ≃ Lie′(X/S, M) ×_S Lie′(X/S, N)`, and thus:

```text
Lie(Aut_{O_S-mod.}(X)/S, M ⊕ N) ≃
   Lie(Aut_{O_S-mod.}(X)/S, M) ×_S Lie(Aut_{O_S-mod.}(X)/S, N).
```

Taking 4.1.1.2 a) into account, this proves that $\operatorname{Aut}_{O_{S}-mod.}(X)/S$ satisfies (E).

**4.3.2.** Before continuing in this direction, let us examine more closely the relations between $Y$, $Lie(Y/S)$ and
$Lie'(Y/S)$. Let us remark first that

```text
(1)   Lie(O_S/S, M) = Lie′(O_S/S, M) = W(M)
```

(where $W(M)$ is defined in I 4.6) and that one therefore has a canonical isomorphism

$$ (2) d : O_{S} \xrightarrow{\sim} Lie(O_{S}/S). $$

<!-- original page 65 -->

Let now $F$ be an `O_S`-module. For every $S_{2} \to S_{1} \to S$[^N.D.E-II-64], one has a dihomomorphism

```text
(3)   ⎰ F(S_1) → F(S_2)
       ⎱ O(S_1) → O(S_2),
```

whence a morphism of $O(S_{2})$-modules

```text
F(S_1) ⊗_{O(S_1)} O(S_2) ⟶ F(S_2).
```

In particular, setting $S_{1} = S'$ and $S_{2} = I_{S'}(M)$, one deduces morphisms of $O(S')$-modules, functorial in
$M$,

```text
F(S′) ⊗_{O(S′)} T_{O_S/S}(M)(S′) ⟶ T′_{F/S}(M)(S′);
```

letting $S'$ vary, one obtains morphisms of `O_S`-modules, functorial in $M$,

```text
(4)   F ⊗_{O_S} T_{O_S/S}(M) ⟶ T′_{F/S}(M).
```

These morphisms are functorial in $M$, hence compatible with the projections of the tangent bundles onto their bases;
they therefore define morphisms of `O_S`-modules

```text
(5)   F ⊗_{O_S} Lie(O_S/S, M) ⟶ Lie′(F/S, M)
```

such that one has the commutative diagram:

```text
   0 ─→ F ⊗_{O_S} Lie(O_S/S, M) ─→ F ⊗_{O_S} T_{O_S/S}(M) ─→ F ─→ 0
                ↓                              ↓                 ↓
   0 ─────→ Lie′(F/S, M)   ──────→     T′_{F/S}(M)   ────→ F ─→ 0 .
```

One may consider the morphisms (5) as morphisms of abelian $S$-groups

```text
(6)   F ⊗_{O_S} Lie(O_S/S, M) ⟶ Lie(F/S, M);
```

tensoring $F$ with the isomorphism $d : O_{S} \xrightarrow{\sim} Lie(O_{S}/S)$, one deduces (for $M = O_{S}$) a morphism
of abelian $S$-groups

<!-- original page 66 -->

```text
(7)   F ⥲ F ⊗_{O_S} Lie(O_S/S) ⟶ Lie(F/S)
```

also denoted $d : F \to Lie(F/S)$.

**Remark 4.3.3.**[^N.D.E-II-65] When $F/S$ satisfies (E), the morphisms (6) and (7) are not necessarily morphisms of
`O_S`-modules, when one equips both sides with the module structures deduced from that of $M$ thanks to condition (E).

<!-- label: III.II.4.3.3 -->

For example, let $k$ be a field of characteristic $p > 0$, $S = \operatorname{Spec}(k)$, and let $F$ be the `O_S`-module
which to every $S$-scheme $T$ associates $F(T) = \Gamma(T, O_{T})$ equipped with the $O(T)$-module structure obtained by
making scalars act through the $p$-th power, i.e., $r \cdot f = r^{p} f$, for $r \in O(T)$, $f \in F(T)$. As $S$-functor
of groups, $F$ is isomorphic to $G_{a, S}$. Therefore $F$ satisfies (E) and $Lie(F/S)$ is identified with $Lie(G_{a,
S}/S) \cong O_{S}$. Then, the canonical morphism $d : F \to Lie(F/S)$ is, for every $T \to S$, the identity map $F(T)
\to O(T)$: it indeed respects the abelian-group structure but not the `O_S`-module structure.

**Remark 4.3.4.**[^N.D.E-II-66] One can make the morphisms (4) and (5) explicit as follows. The morphism $\Theta : F
\otimes_{O_{S}} T_{O_{S}/S}(M) \to T'_{F/S}(M) = \operatorname{Hom}_{S}(I_{S}(M), F)$ is defined by: for every $S' \to
S$, $\alpha \in O(I_{S'}(M))$, and $f : S' \to F$,

<!-- label: III.II.4.3.4 -->

```text
Θ(f ⊗ α) = α · (τ_0 ∘ f) = α · (f ∘ ρ),
```

where $\tau_{0}$ is the null section $F \to T'_{F/S}(M)$ and $\rho$ the structural morphism $I_{S'}(M) \to S'$. Then
$\Theta$ induces a morphism $\theta : F \otimes_{O_{S}} Lie(O_{S}/S, M) \to Lie'(F/S, M)$; this follows from the
"functoriality in $M$" already mentioned after (4), and can be seen explicitly as follows. On the one hand, one has

```text
Lie′(F/S, M)(S′) = { φ ∈ Hom_S(I_{S′}(M), F) | φ ∘ ε_M = e },
```

where $e$ denotes the unit section $S' \to F$. On the other hand, $Lie(O_{S}/S, M)(S') = \Gamma(S', M)$ is the kernel of
the augmentation $\eta : O(I_{S'}(M)) \to O(S')$, and it is therefore a question of seeing that if $f \in F(S')$ and
$\alpha \in \Gamma(S', M)$, then $\alpha \cdot (f \circ \rho) \circ \epsilon_{M} = e$.

Consider the dihomomorphism (3), in the case where $S_{2} \to S_{1}$ is the $S$-morphism $\epsilon_{M} : S' \to
I_{S'}(M)$; one has then a commutative diagram

```text
                       F(ε_M)
   F(I_{S′}(M)) ─────────────→ F(S′)
        │ α                       │ η(α)
        ↓        F(ε_M)           ↓
   F(I_{S′}(M)) ─────────────→ F(S′) .
```

For every $\phi : I_{S'}(M) \to F$, one therefore has $(\alpha \cdot \phi) \circ \epsilon_{M} = \eta(\alpha) \cdot (\phi
\circ \epsilon_{M})$, whence $(\alpha \cdot \phi) \circ \epsilon_{M} = e$ if $\eta(\alpha) = 0$.

In particular, taking $M = t O_{S}$, one has $Lie(O_{S}/S) = t O_{S}$ and the morphism $F \to Lie'(F/S)$ is given by $f
\mapsto t \cdot (f \circ \rho)$.

**Remark 4.3.5.**[^N.D.E-II-67] Let $F$ be an `O_S`-module, set $E = \operatorname{End}_{O_{S}-mod.}(F)$ and denote by
$d_{F}$ and $d_{E}$ the morphisms of `O_S`-modules given by 4.3.2 (5):

<!-- label: III.II.4.3.5 -->

```text
d_F : F ⊗_{O_S} Lie(O_S/S, M) ⟶ Lie′(F/S, M),
d_E : E ⊗_{O_S} Lie(O_S/S, M) ⟶ Lie′(E/S, M).
```

One deduces from 4.3.4 the following commutative diagram of morphisms of `O_S`-modules:

```text
                                      d_E
   E ⊗_{O_S} Lie(O_S/S, M) ──────────────→ Lie′(E/S, M)
                                                  ↑ ≃ (∗)
                                      d_F
   Hom_{O_S}(F, F ⊗_{O_S} Lie(O_S/S, M)) ─→ Hom_{O_S}(F, Lie′(F/S, M))
```

where the right vertical arrow is the isomorphism (∗) of 4.3. Therefore (loc. cit.), if $F/S$ satisfies (E), then $E/S$
satisfies (E) and (∗) is also an isomorphism of `O_S`-modules when one equips the right-hand terms with the `O_S`-module
structure deduced from (E).

<!-- original page 81 -->

**Remark 4.4.0.**[^N.D.E-II-68] In 4.3.2, the morphisms (4) are isomorphisms if and only if the morphisms (5) are.
Moreover, if these conditions are verified, then $F/S$ satisfies (E). Indeed, it suffices to verify that
`Lie′(F/S, M ⊕ N) ≃ Lie′(F/S, M) ×_S Lie′(F/S, N)`. Now one has the commutative diagram below, where by hypothesis the
horizontal arrows are isomorphisms:

<!-- label: III.II.4.4.0 -->

```text
   F ⊗_{O_S} Lie(O_S/S, M ⊕ N)  ⥲  Lie′(F/S, M ⊕ N)
              │ ≀                          │
              ↓                            ↓
   F ⊗_{O_S} (Lie(O_S/S, M) ×_S Lie(O_S/S, N))  ⥲  Lie′(F/S, M) ×_S Lie′(F/S, N);
```

the second vertical arrow is therefore also an isomorphism, i.e. $F/S$ satisfies (E).

**Definition 4.4.** *One says that $F$ is a* **good `O_S`-module** *if the morphisms*

<!-- label: III.II.4.4 -->

```text
F ⊗_{O_S} T_{O_S/S}(M) ⟶ T_{F/S}(M)
or, equivalently,
F ⊗_{O_S} Lie(O_S/S, M) ⟶ Lie(F/S, M),
```

*are isomorphisms of abelian $S$-groups (so that $F/S$ satisfies (E)) and if moreover they respect the `O_S`-module
structures deduced from condition (E).*

**Corollary 4.4.1.**[^N.D.E-II-69] *Let $F$ be an `O_S`-module. Consider the following conditions:*

<!-- label: III.II.4.4.1 -->

*(i) $F$ is a good `O_S`-module.*

*(ii) $F/S$ satisfies (E) and $d : F \to Lie(F/S)$ is an isomorphism of `O_S`-modules.*

*(iii) $Lie(F/S, M) = Lie'(F/S, M)$.*

*Then one has (i) ⇔ (ii) ⇒ (iii).*

*Proof.* (i) ⇒ (ii) follows from the definition. To prove (ii) ⇒ (i), one must show that the morphisms of abelian
$S$-groups (functorial in $M$)

```text
F ⊗_{O_S} Lie(O_S/S, M) ⥲ Lie(F/S, M)
```

are isomorphisms of `O_S`-modules. Since $F/S$ satisfies (E), both sides transform finite direct sums of copies of `O_S`
into finite products of abelian $S$-groups. This reduces us to the case $M = O_{S}$, which follows from the hypothesis.

Finally, (i) ⇒ (iii) follows from the definition and from the fact that the isomorphisms

```text
F ⊗_{O_S} Lie(O_S/S, M) ⥲ Lie′(F/S, M)
```

of 4.3.2 (5) are morphisms of `O_S`-modules.

**Examples 4.4.2.** *For every quasi-coherent `O_S`-Module $E$, the `O_S`-modules $V(E)$ and $W(E)$ defined in I 4.6 are
good.*

<!-- label: III.II.4.4.2 -->

<!-- original page 67 -->

[^N.D.E-II-70] Indeed, for every $f : S' \to S$, the morphisms

```text
V(E)(S′) ⊗_{O(S′)} O(I_{S′}(M)) ⟶ T_{V(E)/S}(M)(S′)
W(E)(S′) ⊗_{O(S′)} O(I_{S′}(M)) ⟶ T_{W(E)/S}(M)(S′)
```

correspond, respectively, to the morphisms:

```text
Hom_{O_{S′}-mod.}(f^*(E), O_{S′}) ⊗_{O(S′)} Γ(S′, D_{O_{S′}}(M))
   ⟶ Hom_{O_{S′}-mod.}(f^*(E), D_{O_{S′}}(M))
Γ(S′, f^*(E)) ⊗_{O(S′)} Γ(S′, D_{O_{S′}}(M))
   ⟶ Γ(S′, f^*(E) ⊗_{O_{S′}} D_{O_{S′}}(M));
```

these are isomorphisms, since $D_{O_{S'}}(M)$ is isomorphic, as $O_{S'}$-module, to a finite direct sum of copies of
$O_{S'}$.

**Proposition 4.5.** *Let $F$ be a good `O_S`-module. Then:*

<!-- label: III.II.4.5 -->

*(i) $\operatorname{Aut}_{O_{S}-mod.}(F)/S$ satisfies (E) and one has a functorial isomorphism*

```text
Lie(Aut_{O_S-mod.}(F)/S, M) ⥲ Hom_{O_S-mod.}(F, Lie(F/S, M))
```

*which respects the `O_S`-module structures deduced from condition (E). In particular, one has an isomorphism of
`O_S`-modules*

```text
Lie(Aut_{O_S-mod.}(F)/S) ⥲ End_{O_S-mod.}(F).
```

*(ii)*[^N.D.E-II-71] *Moreover, $\operatorname{End}_{O_{S}-mod.}(F)$ is a good `O_S`-module.*

Indeed, by 4.4.1, $F/S$ satisfies (E) and

```text
(1)   Lie(F/S, M) = Lie′(F/S, M) ≃ F ⊗_{O_S} Lie(O_S/S, M).
```

Assertion (i) then follows from 4.3.1. Set $E = \operatorname{End}_{O_{S}-mod.}(F)$. By (1) and Remark 4.3.5, one has
the following commutative diagram of morphisms of abelian $S$-groups:

```text
                                              d_E
   End_{O_S-mod.}(F) ⊗_{O_S} Lie(O_S/S, M) ────→ Lie(End_{O_S-mod.}(F)/S, M)
                                                            ↑ ≃ (∗)
                                              d_F
   Hom_{O_S}(F, F ⊗_{O_S} Lie(O_S/S, M)) ────→ Hom_{O_S}(F, Lie(F/S, M))
```

where $d_{F}$ and (∗) are isomorphisms of `O_S`-modules; consequently, so is $d_{E}$. This proves (ii).

**Scholie 4.5.1.**[^N.D.E-II-72] Set (cf. 2.1) $O_{I_{S}} = O_{S} \oplus t O_{S}$ (with $t^{2} = 0$), and let $F$ be a
good `O_S`-module. Then, for every $S' \to S$, the morphism

<!-- label: III.II.4.5.1 -->

```text
F(S′) ⊕ t F(S′) = F(S′) ⊗_{O(S′)} O(I_{S′}) ⟶ F(I_{S′}) = F(S′) ⊕ Lie(F/S)(S′)
```

<!-- original page 82 -->

(which is the identity on $F(S')$) induces an isomorphism of $O(S')$-modules $t F(S') \simeq Lie(F/S)(S')$. Letting $S'$
vary, one obtains an isomorphism which one may write $Lie(F/S) \simeq t F$.

For every $S' \to S$, one has therefore, by 4.5, a commutative diagram:

```text
   End_{O_{S′}-mod.}(F_{S′}) ⥲ Hom_{O_{S′}-mod.}(F_{S′}, t F_{S′}) ⥲ Lie(Aut_{O_S-mod.}(F)/S)(S′)
              │                            │                                       │
              ↓                            ↓                                       ↓
                       Aut_{O_{I_{S′}}-mod.}(F_{I_{S′}})              T_{Aut_{O_S-mod.}(F)/S}(S′)
```

and one deduces from 4.3 bis that every $X \in \operatorname{End}_{O_{S'}-mod.}(F_{S'})$ corresponds to the element
$id + t X$ of $\operatorname{Aut}_{O_{I_{S'}}-mod.}(F_{I_{S'}})$.

**Definition 4.6.** *One says that the $S$-functor of groups $G$ is* **good** *if $G/S$ satisfies condition (E) and if
$Lie(G/S)$ is a good `O_S`-module.*

<!-- label: III.II.4.6 -->

[^N.D.E-II-73] Note that if $F$ is a good `O_S`-module, it is a good $S$-group; indeed $F/S$ satisfies (E) and $Lie(F/S)
\simeq F$ is a good `O_S`-module.

**Example 4.6.1.** *If $G$ is representable, it is good. Indeed, $G/S$ satisfies (E) and $Lie(G/S)$ is of the form
$V(E)$, hence good, by 4.4.2.*

<!-- label: III.II.4.6.1 -->

**Lemma 4.6.2.**[^N.D.E-II-74] *Let $G$ be an $S$-functor of groups such that $G/S$ satisfies (E), and let $F =
Lie(G/S)$. Then $F$ satisfies (E) and the morphism of abelian groups $d : F \to Lie(F/S)$ respects the `O_S`-module
structures.*

<!-- label: III.II.4.6.2 -->

*Consequently, $G$ is good if and only if $F \to Lie(F/S)$ is bijective.*

*Proof.* Suppose that $G/S$ satisfies (E). Let `M, N` be free `O_S`-modules of finite rank. Write $F(N) = Lie(G/S, N)$
and $e$ the unit section of $G$.

For every $S' \to S$, one has $F(N)(S') = { g \in \operatorname{Hom}_{S}(I_{S'}(N), G) | g \circ \epsilon_{N} = e}$ and
$Lie(F(N)/S, M)(S') = \operatorname{Hom}_{S}(I_{S'}(M), F(N))$ is identified with

```text
{ Φ ∈ Hom_S(I_{S′}(N) ×_{S′} I_{S′}(M), G) |
       Φ ∘ (ε_N × id_{I_{S′}(M)}) = e ∈ G(I_{S′}(M)),
       Φ ∘ (id_{I_{S′}(N)} × ε_M) = e ∈ G(I_{S′}(N)) }.
```

This shows that

```text
(1)   Lie(F(N)/S, M) ≃ Lie(F(M)/S, N).
```

As $G/S$ satisfies (E), one deduces:

```text
Lie(F(N)/S, M_1 ⊕ M_2) ≃ Lie(F(M_1 ⊕ M_2)/S, N)
                       ≃ Lie((F(M_1) ×_S F(M_2))/S, N).
```

By 3.8, the right-hand term is isomorphic to

```text
Lie(F(M_1)/S, N) ×_S Lie(F(M_2)/S, N) ≃ Lie(F(N)/S, M_1) ×_S Lie(F(N)/S, M_2).
```

<!-- original page 84 -->

It follows that

```text
(2)   Lie(F(N)/S, M_1 ⊕ M_2) ≃ Lie(F(N)/S, M_1) ×_S Lie(F(N)/S, M_2),
```

so $F(N)/S$ satisfies (E), by Remark 4.1.1.2 a).

Let us now show that the morphism of abelian groups $d : F(N) \to Lie(F(N)/S)$ respects the `O_S`-module structures.
Consider the free `O_S`-module $M = t O_{S}$, so that

```text
O(I_{S′}(M)) = O(S′)[t]/(t²) = O(S′) ⊕ t O(S′)
```

and $Lie(O_{S}/S) \simeq t O_{S}$. We denote by $\rho_{t}$ the structural morphism $I_{S}(M) \to S$, which corresponds
to the injection $u_{t} : O_{S} \hookrightarrow D_{O_{S}}(M) = O_{S} \oplus t O_{S}$. Recall (cf. 3.4.2) that, for every
$S$-functor $X$, $F(N)(X) = Lie(G/S, N)(X)$ is the set of $S$-morphisms $\phi : I_{X}(N) \to G$ such that $\phi \circ
\epsilon_{N} = e$, and that the action of $a \in O(X)$ is given by $a \cdot \phi = \phi \circ a^{*}$, where $a^{*}$ is
the endomorphism of $I_{X}(N)$ associated with $a$, cf. 2.1.3.

Consequently, by 4.3.4, the morphism $d : F(N) \xrightarrow{\sim} F(N) \otimes_{O_{S}} t O_{S} \to Lie(F(N)/S)$ is given
by: for every $S' \to S$ and $f \in \operatorname{Hom}_{S}(S', F(N))$,

```text
f ↦ f ⊗ t ↦ t · (f ∘ ρ_t) = f ∘ ρ_t ∘ t^*,
```

where, in the last term, $f \circ \rho_{t} \in F(N)(I_{S'}(M))$ is considered as an $S$-morphism $\phi :
I_{I_{S'}(M)}(N) \to G$ (such that $\phi \circ \epsilon_{N} = e$). It is a question of seeing that $d$ is a morphism of
`O_S`-modules, i.e., that $d(a \cdot f) = u_{t}(a) \cdot d(f)$ for every $a \in O(S')$.

Considering $f \in F(N)(S')$ as a morphism $I_{S'}(N) \to G$, one has likewise $a \cdot f = f \circ a^{*}$. On the other
hand, by the functoriality in $X$ of the action of $O(X)$ on $I_{X}(N)$ (cf. 2.1.3), one has the commutative diagram
below:

```text
                          a^*
   I_{S′}(N) ─────────────────→ I_{S′}(N)
       ↑                              ↑
       ρ_t                            ρ_t
                       u_t(a)^*
   I_{I_{S′}(M)}(N) ─────────────→ I_{I_{S′}(M)}(N) .
```

One has therefore

```text
d(a · f) = f ∘ a^* ∘ ρ_t ∘ t^* = f ∘ ρ_t ∘ u_t(a)^* ∘ t^* = f ∘ ρ_t ∘ t^* ∘ u_t(a)^* = u_t(a) · d(f)
```

(the second-to-last equality resulting from the fact that $O$ is commutative). This completes the proof of Lemma 4.6.2.

**Theorem 4.7.** *If $F$ is a good `O_S`-module, the $S$-group $\operatorname{Aut}_{O_{S}-mod.}(F)$ is good.*

<!-- label: III.II.4.7 -->

<!-- original page 68 -->

[^N.D.E-II-75] Indeed, by 4.5, $\operatorname{Aut}_{O_{S}-mod.}(F)/S$ satisfies (E) and
`Lie(Aut_{O_S-mod.}(F)/S) ≃ End_{O_S-mod.}(F)` is a good `O_S`-module.

**4.7.1.**[^N.D.E-II-76] Let now $G$ be an $S$-group and $F$ a good `O_S`-module. Suppose given a linear representation
of $G$ in $F$, that is to say (I 4.7.1), a morphism of $S$-groups

$$ \rho : G \longrightarrow \operatorname{Aut}_{O_{S}-mod.}(F). $$

If $G/S$ satisfies (E), one deduces from 4.1.C and 4.5 a morphism of `O_S`-modules, denoted $\rho'$ or $d\rho$:

```text
Lie(G/S) ⟶ Lie(Aut_{O_S-mod.}(F)/S) ≃ End_{O_S-mod.}(F).
```

[^N.D.E-II-77] Moreover, setting $O_{I_{S}} = O_{S} \oplus t O_{S}$ (with $t^{2} = 0$), one deduces from 4.5.1 that, if
$S' \to S$ and $X \in Lie(G/S)(S') \subset G(I_{S'})$, then one has in
$\operatorname{Aut}_{O_{I_{S'}}-mod.}(F_{I_{S'}})$ the following equality:

```text
(∗)   ρ(X) = id + t ρ′(X),
```

i.e. for every $S'' \to I_{S'}$ and $f \in F(S'')$, one has in $F(S'')$ the equality $\rho(X)(f) = f + t \rho'(X)(f)$.

**Definition 4.7.2.** *Let $G$ be a good $S$-group. Then $Lie(G/S)$ is a good `O_S`-module, and one has a morphism of
$S$-groups `Ad : G → Aut_{O_S-mod.}(Lie(G/S))`. One deduces from 4.7.1 a morphism of `O_S`-modules*

<!-- label: III.II.4.7.2 -->

```text
ad : Lie(G/S) ⟶ End_{O_S-mod.}(Lie(G/S)),
```

*or, what amounts to the same, an `O_S`-bilinear morphism:*

```text
Lie(G/S) ×_S Lie(G/S) ⟶ Lie(G/S),    (x, y) ↦ [x, y] = ad(x) · y
```

*(where $x$ and $y$ denote two arbitrary elements of $Lie(G/S)(S') = Lie(G_{S'}/S')(S')$). If $G$ is commutative, then
$[x, y] = 0$.*

<!-- original page 69 -->

**4.7.3.** One can give an equivalent definition of the bracket as follows: let us remark first that it suffices to do
it for $x, y \in Lie(G/S)(S)$. Let us remark next that there is a canonical isomorphism $I_{S} \times_{S} I_{S} \simeq
I_{I_{S}}$; to avoid confusions, let us denote by $I$ and $I'$ two copies of `I_S` and set $O_{I} = O_{S}[t]$, $O_{I'} =
O_{S}[t']$, where $t^{2} = 0 = t'^{2}$. One has then a commutative diagram

```text
   I × I′ ──→ I′
     │         │
     ↓         ↓
     I  ────→  S ,
```

the two arrows starting from $I \times I'$ identifying it with the scheme of dual numbers over $I$ or over $I'$. There
follows a commutative diagram of groups (where one writes $L = Lie(G/S)$):

```text
                                  1            1
                                  │            │
                                  ↓            ↓
                                L(I) ──────→ L(S) ─→ 1
                                  │            │
   1 ─→ L(I′) ─→ G(I × I′) ─→ G(I′) ─→ 1
(1)            │            │
                                  ↓            ↓
   1 ─→ L(S) ─→ G(I) ─→ G(S) ─→ 1
                                  │            │
                                  ↓            ↓
                                  1            1 .
```

The ninth piece of the puzzle is nothing other than $Lie(L/S)(S)$. If $G$ is good, this is $L(S)$ and one has therefore
the following commutative diagram, where the lines and columns are exact sequences of groups, the five $L(-)$ are
commutative,[^N.D.E-II-78] and where, taking into account the identification $L(I) = L(S) \oplus t L(S)$ (resp. $L(I') =
L(S) \oplus t' L(S)$), the injection $L(S) \hookrightarrow L(I)$ (resp. $L(S) \hookrightarrow L(I')$) is given by $u
\mapsto t u$ (resp. $u \mapsto t' u$):

<!-- original page 86 -->

```text
                          t
   z ∈ L(S) ────────→ L(I) ─────→ L(S) ∋ x
       │ t′                          │
       ↓                             ↓
   L(I′) ────→ G(I × I′) ────→ G(I′)
       │                             │
       ↓                             ↓
   y ∈ L(S) ─────→ G(I) ─────→ G(S) .
```

Now in such a diagram, if one takes two elements $x$ and $y$ as marked, and one lifts arbitrarily $x$ resp. $y$ to an
element $\tilde{x} \in L(I)$ resp. $y' \in L(I')$, the commutator $\tilde{x} y' \tilde{x}^{-1} y'^{-1}$ in $G(I \times
I')$ does not depend on the chosen lifts and is the image of an element $z$ as marked. The reader will verify that one
has $z = [x, y]$.[^N.D.E-II-79]

Indeed, if one still denotes by $x$ the image of $x$ by the canonical section $L(S) \to L(I)$ (and likewise for $y$),
then $\tilde{x} = xu$ and $y' = yv$, with $u, v \in L(S) = L(I) \cap L(I')$, and since $L(I)$ and $L(I')$ are
commutative one has

```text
x̃ y′ x̃^{-1} y′^{-1} = x u y v u^{-1} x^{-1} v^{-1} y^{-1}
                     = x u y u^{-1} v x^{-1} v^{-1} y^{-1}
                     = x y x^{-1} y^{-1}.
```

Moreover, this element is sent to the unit element of $G(I)$ and of $G(I')$, hence comes from a (unique) $z$ as
indicated. Finally, considering $y$ (resp. $x$) as an element of $L_{I'}(I')$ (resp. of $L(S) \subset G(I')$), one has
by 4.7.1 (∗):

```text
x y x^{-1} = Ad(x)(y) = (id + t′ ad(x))(y) = y + t′ [x, y],
```

so the element $x y x^{-1} y^{-1}$ of $L(I')$ is the image of the element $z = [x, y]$ of $L(S)$.

On this construction the following two properties appear:

*(i) the bracket is "functorial in $G$":* precisely, $G \mapsto Lie(G/S)$ is a functor from the category of good
$S$-groups to the category of good `O_S`-modules equipped with an `O_S`-bilinear composition law.

*(ii) One has $[x, y] + [y, x] = 0$:* indeed the diagram is symmetric with respect to the first diagonal.[^N.D.E-II-80]

**Proposition 4.8.** *Let $F$ be a good `O_S`-module. Via the identification*

<!-- label: III.II.4.8 -->

```text
Lie(Aut_{O_S-mod.}(F)/S) = End_{O_S-mod.}(F)
```

*one has*

```text
Ad(g) · Y = g ∘ Y ∘ g^{-1}    and    [X, Y] = X ∘ Y − Y ∘ X,
```

*for every $S' \to S$, $g \in \operatorname{Aut}_{O_{S'}-mod.}(F_{S'})$, and
`X, Y ∈ Lie(Aut_{O_S-mod.}(F)/S)(S′) = End_{O_{S′}-mod.}(F_{S′})`.*

*Proof.*[^N.D.E-II-81] By base change, one reduces to $S' = S$, which permits one to lighten the notation. Set $I =
I_{S}$ and $O_{I} = O_{S}[t]$ (with $t^{2} = 0$). Recall (cf. 4.5.1) that the inclusion
`i : End_{O_S-mod.}(F) ↪ Aut_{O_I-mod.}(F_I)` sends $Y$ to $id + t Y$. Then, by definition of $Ad(g)$ (cf. 4.1.A), one
has:

```text
id + t Ad(g)(Y) = g ∘ (id + t Y) ∘ g^{-1} = id + t (g ∘ Y ∘ g^{-1}),
```

whence $Ad(g)(Y) = g \circ Y \circ g^{-1}$.

Let $I'$ be a second copy of `I_S`, set $O_{I'} = O_{S}[t']$ (with $t'^{2} = 0$). Apply the results of 4.7.3 to $G =
\operatorname{Aut}_{O_{S}-mod.}(F)$ and `L = Lie(G/S) = Aut_{O_S-mod.}(F)`. One identifies $X$ with its image under the
canonical section $L(S) \hookrightarrow L(I)$; its image in $G(I \times I')$ is then $id + t' X$, whose inverse is $id -
t' X$. Likewise, $Y$ lifts to $id + t Y$, whose inverse is $id - t Y$. Then, the commutator

```text
(id + t′ X) ∘ (id + t Y) ∘ (id − t′ X) ∘ (id − t Y) = id + t t′ (X ∘ Y − Y ∘ X)
```

is the image in $G(I \times I')$ of the element $Z = X \circ Y - Y \circ X$ of $L(S)$ (indeed, $Z$ is sent to $t Z \in
L(I)$, then to $id + t' t Z \in G(I \times I')$). By 4.7.3, this shows that $[X, Y] = X \circ Y - Y \circ X$.

<!-- original page 71 -->

**Corollary 4.8.1.** *Let $G$ be a good $S$-group and $x, y, z \in Lie(G/S)(S')$. One has:*

<!-- label: III.II.4.8.1 -->

```text
[x, [y, z]] + [y, [z, x]] + [z, [x, y]] = 0.
```

[^N.D.E-II-82] Indeed, since $G$ is good, $Lie(G/S)$ is a good `O_S`-module and therefore, by 4.7,
$\operatorname{Aut}_{O_{S}-mod.}(Lie(G/S))$ is a good $S$-group. Then, the morphism of $S$-groups

```text
Ad : G ⟶ Aut_{O_S-mod.}(Lie(G/S))
```

gives, by the functoriality 4.7.3 (i): $ad[x, y] = [ad x, ad y]$. Combined with 4.8, this gives:

```text
ad[x, y] = [ad x, ad y] = ad x ∘ ad y − ad y ∘ ad x,
```

which, applied to an element $z$, gives the Jacobi relation.

**Corollary 4.8.2.** *Let $G$ be a good $S$-group acting linearly on a good `O_S`-module $F$ (i.e. let $F$ be a
$G$-`O_S`-module, with $G$ and $F$ good). Then the linear map `ρ′ : Lie(G/S) → End_{O_S-mod.}(F)` is a representation,
i.e. one has*

<!-- label: III.II.4.8.2 -->

```text
ρ′([x, y]) = ρ′(x) ∘ ρ′(y) − ρ′(y) ∘ ρ′(x).
```

**Scholie 4.9.** *To every good $S$-group (for example representable), one has associated a good `O_S`-module $Lie(G/S)$
functorially equipped with a bilinear map satisfying*

<!-- label: III.II.4.9 -->

```text
[x, y] + [y, x] = 0,    [x, [y, z]] + [y, [z, x]] + [z, [x, y]] = 0.
```

*We shall call $Lie(G/S)$ equipped with this structure the "Lie algebra" of $G$ over $S$ (the quotation marks being
justified by the fact that one does not know whether $Lie(G/S)$ is, strictly speaking, an `O_S`-Lie
algebra*[^N.D.E-II-83]*). To every linear representation of $G$ in a good `O_S`-module $F$ is associated a
representation of its "Lie algebra". In particular, to the adjoint representation of $G$ is associated the adjoint
representation of its "Lie algebra".*

**Definition 4.10.** *A group-functor $G$ above $S$ is said to be* **very good** *if it is good and if $Lie(G/S)$ is an
`O_S`-Lie algebra (i.e. if one has identically $[x, x] = 0$).*

<!-- label: III.II.4.10 -->

**Examples 4.10.1.** *The following $S$-groups are very good: $\operatorname{Aut}_{O_{S}-mod.}(F)$ for every good
`O_S`-module $F$ (cf. 4.7 and 4.8), every representable group (see below), every good $S$-group admitting a monomorphism
into a very good $S$-group, for example every good subgroup-functor of a representable group, or every good $S$-group
admitting a faithful linear representation in a good `O_S`-module, for example every good $S$-group such that `Ad` is a
monomorphism . . .*

<!-- label: III.II.4.10.1 -->

<!-- original page 89 -->

**4.11.** Suppose now that $G$ is a group scheme over $S$. By 4.1.4, $Lie(G/S)(S)$ is identified with the group of
infinitesimal automorphisms of $G/S$ right-invariant, that is to say, by 3.14, with the group of derivations of `O_G`
over `O_S` invariant by right translation. Moreover this identification respects the module structure and is
an[^N.D.E-II-84] anti-isomorphism of Lie algebras, as one sees by reasoning as in 4.7.3: set $O_{I} = O_{S}[t]$ and
$O_{I'} = O_{S}[t']$ and let $x \in L(I)$ and $y \in L(I')$. The left translation $\lambda_{x}$ (resp. $\lambda_{y}$) is
an $S$-automorphism of $G_{I\times I'}$ which induces the identity on $G_{I'}$ (resp. `G_I`) and which corresponds to an
`O_S`-automorphism

```text
u = id + t d_x    resp.    v = id + t′ d_y
```

of $O_{G_{I\times I'}} = O_{G}[t, t']/(t^{2}, t'^{2})$, where $d_{x}, d_{y}$ are `O_S`-derivations of `O_G` invariant by
right translation. Since the correspondence between $S$-automorphisms of $G_{I\times I'}$ and `O_S`-automorphisms of
$O_{G_{I\times I'}}$ is contravariant, $\lambda_{x} \lambda_{y} \lambda^{-1}_{x} \lambda^{-1}_{y}$ corresponds to
$v^{-1} u^{-1} v u = id + t t' (d_{y} d_{x} - d_{x} d_{y})$. One deduces, by 4.7.3, that the map $x \mapsto -d_{x}$ is
an isomorphism of Lie algebras (for more details, see [DG70], § II.4, 4.4 and 4.6). What precedes is valid for
$Lie(G/S)(S') = Lie(G_{S'}/S')(S')$ for every $S' \to S$. One thus recovers the classical definition:[^N.D.E-II-85]

**Scholie 4.11.1.** *Via the isomorphism $x \mapsto -d_{x}$, $Lie(G/S)$ is identified with the functor that to every
$S'$ above $S$ associates the $O(S')$-Lie algebra of derivations of $G_{S'}$ with respect to $S'$ invariant by right
translation.*

<!-- label: III.II.4.11.1 -->

Since one knows already, by 4.6.1, that every representable group is good, it follows from what precedes:

**Corollary 4.11.2.** *Every representable group is very good.*

<!-- label: III.II.4.11.2 -->

Let $\epsilon : S \to G$ be the unit section of $G$. Set $\omega^{1}_{G/S} = \epsilon^{*}(\Omega^{1}_{G/S})$ and recall
(cf. 3.3) that $Lie(G/S)$ is representable by the vector fibration $V(\omega^{1}_{G/S})$.

**Scholie 4.11.3.** *One has therefore associated functorially to every $S$-group scheme $G$ a vector fibration
$Lie(G/S) = V(\omega^{1}_{G/S})$ over $S$, which represents the functor $Lie(G/S)$, hence is equipped with a structure
of $S$-scheme of `O_S`-Lie algebras. Moreover (cf. 3.4 and 3.8), this construction commutes with base extension and
finite products.*

<!-- label: III.II.4.11.3 -->

**Remarks 4.11.4.**[^N.D.E-II-86] Denote by $\pi$ the morphism $G \to S$.

<!-- label: III.II.4.11.4 -->

*a)* The `O_G`-module $\Omega^{1}_{G/S}$ is evidently $(G \times_{S} G)$-equivariant (cf. I, § 6) and therefore, by I
6.8.1, one has $\Omega^{1}_{G/S} \simeq \pi^{*}(\omega^{1}_{G/S})$. It follows for example that $\Omega^{1}_{G/S}$ is
locally free (resp. locally free of finite type) if $\omega^{1}_{G/S}$ is, which is in particular the case if $S$ is the
spectrum of a field (resp. if $S$ is the spectrum of a field and $G$ locally of finite type over $S$).

<!-- original page 90 -->

*b)* Moreover, by I 6.8.2, $\omega^{1}_{G/S}$ is equipped with a canonical structure of $G$-`O_S`-module, which induces
on $V(\omega^{1}_{G/S}) = Lie(G/S)$ the adjoint action.[^N.D.E-II-87]

*c)* On the other hand (cf.
[EGA I, 5.3.11](https://jcreinhold.github.io/ega/i/01-05-reduced-preschemes-and-separation.html#53-diagonal-graph-of-a-morphism)
and 5.4.6), $\epsilon$ is an immersion, and is a closed immersion if $G$ is separated over $S$. Therefore
$\omega^{1}_{G/S}$ is identified with $I/I^{2}$, where $I$ is the quasi-coherent ideal defining $\epsilon(S)$ in an open
subset $U$ of $G$ in which $\epsilon(S)$ is closed (if $G \to S$ is separated, one may take $U = G$, and if
$G = \operatorname{Spec} A(G)$ is affine over $S$, $I$ is nothing other than the augmentation ideal of $A(G)$, i.e. the
kernel of $\epsilon^{\natural} : A(G) \to O_{S}$, cf. I 4.2).[^N.D.E-II-88]

**Remark 4.11.5.** One can deduce from the isomorphism $\Omega^{1}_{G/S} \simeq \pi^{*}(\omega^{1}_{G/S})$ that the
`O_S`-module $\omega^{1}_{G/S}$ is identified with the sheaf $\pi_{*}(\Omega^{1}_{G/S})^{G}$ of "differentials of $G$
with respect to $S$ invariant on the right", that is to say, with the sheaf whose sections on an open subset $U$ of $S$
are the sections of $\Omega^{1}_{G/S}$ on $\pi^{-1}(U)$ invariant by right translation (cf. I, 6.8.3, compare also with
VII_A, 2.4).[^N.D.E-II-89]

<!-- label: III.II.4.11.5 -->

<!-- original page 74 -->

**Notation 4.11.6.** *One denotes by $Lie(G/S)$ the sheaf of sections of the vector fibration $Lie(G/S) \to S$; it is
the `O_S`-module $(\omega^{1}_{G/S})^{\vee} = \operatorname{Hom}_{O_{S}}(\omega^{1}_{G/S}, O_{S})$ dual to
$\omega^{1}_{G/S}$ (cf.
[EGA II 1.7.9](https://jcreinhold.github.io/ega/ii/02-01-affine-morphisms.html#17-vector-bundle-associated-to-a-sheaf-of-modules)).
It is equipped with a structure of `O_S`-Lie algebra.*

<!-- label: III.II.4.11.6 -->

*Since this construction does not commute with base extension (in general), the Lie algebra structure on this module
does not allow one to reconstruct the structure of $S$-scheme of `O_S`-Lie algebras on $Lie(G/S)$.*[^N.D.E-II-90]

However one has:

**Lemma 4.11.7.** *Suppose $\omega^{1}_{G/S}$ locally free of finite type (which is the case in particular if $G$ is
smooth over $S$ (cf.
[EGA IV_4, 17.2.4](https://jcreinhold.github.io/ega/iv/30-ch4-17-smooth-unramified-etale-morphisms.html#172-general-differential-properties)),
or if $S$ is the spectrum of a field and $G$ locally of finite type over $S$). Then
$Lie(G/S)^{\vee} \cong (\omega^{1}_{G/S})^{\vee\vee} \cong \omega^{1}_{G/S}$ and therefore*

<!-- label: III.II.4.11.7 -->

```text
Lie(G/S) = V(ω¹_{G/S}) = V(Lie(G/S)^∨) = W(Lie(G/S))
```

*(the last equality following from I 4.6.5.1).*

Finally, let $G \to H$ be a monomorphism of group-functors. Then $Lie(G/S) \to Lie(H/S)$ is also a monomorphism (cf.
3.7). Since every vector monomorphism of vector fibrations is a closed immersion[^N.D.E-II-91] one obtains:

**Corollary 4.11.8.** *Let $G \hookrightarrow H$ be a monomorphism of $S$-group schemes.*

<!-- label: III.II.4.11.8 -->

*(i) $Lie(G/S) \to Lie(H/S)$ is a closed immersion and therefore $\omega^{1}_{H/S} \to \omega^{1}_{G/S}$ is an
epimorphism.*

*(ii) If $\omega^{1}_{G/S}$ is locally free of finite type, then the corresponding morphism $Lie(G/S) \to Lie(H/S)$ is
an isomorphism of $Lie(G/S)$ onto a sub-module of $Lie(H/S)$ locally direct factor.*

## 5. Computation of some Lie algebras

<!-- label: III.II.5 -->

### 5.1. Examples of Lie algebras: diagonalizable groups

<!-- label: III.II.5.1 -->

Let $G = D_{S}(M)$ be a diagonalizable group over $S$ (I 4.4). Since the formation of $Lie(G/S)$ commutes with base
extension, it suffices to make the construction for $G = D(M)$. One has then:

```text
G(I_S) = Hom_{gr.}(M, Γ(I_S, O_{I_S})^×) = Hom_{gr.}(M, Γ(S, D_{O_S})^×).
```

Now one has a split exact sequence

```text
1 ⟶ Γ(S, O_S) ⟶ Γ(S, D_{O_S})^× ⟶ Γ(S, O_S)^× ⟶ 1,
```

which gives that $Lie(G)(S)$ is identified with $\operatorname{Hom}_{gr.}(M, O(S))$ equipped with its obvious
$O(S)$-module structure. One thus obtains, after base change:

<!-- original page 75 -->

**Proposition 5.1.** *One has isomorphisms*

<!-- label: III.II.5.1 -->

```text
Hom_{S-gr.}(M_S, O_S) ⥲ Lie(D_S(M)/S)    and    Hom_{gr.}(M̃_S, O_S) ⥲ Lie(D_S(M)/S),
```

*(where, in the second isomorphism, $\tilde{M}_{S}$ denotes the constant sheaf of groups on $S$ defined by $M$, and
$\operatorname{Hom}_{gr.}$ the sheaf of homomorphisms of sheaves of groups).*

**Corollary 5.1.1.** *If $M$ is free of finite type (or, as we shall say later, if $D_{S}(M)$ is a split torus), then
(see I, 4.6.5 for the definition of $W$)*

<!-- label: III.II.5.1.1 -->

```text
W(Lie(D_S(M)/S)) ⥲ Lie(D_S(M)/S),
M^∨ ⊗_ℤ O_S    ⥲ Lie(D_S(M)/S),
```

*where $M^{\vee}$ denotes the dual of the abelian group $M$. In particular*

```text
O_S ⥲ Lie(G_{m,S}/S)    and    O_S ⥲ Lie(G_{m,S}/S).
```

### 5.2. Normalizers and centralizers

<!-- label: III.II.5.2 -->

Let us first prove a few lemmas. Recall (cf. I 3.1.1) that a sequence $0 \to F' \to F \to F'' \to 0$ of `O_S`-modules is
said to be exact if for every $S' \to S$ the sequence $0 \to F'(S') \to F(S') \to F''(S') \to 0$ of $O(S')$-modules is
exact.

<!-- original page 76 -->

Likewise, a sequence $1 \to G' \to G \to G'' \to 1$ of $S$-groups is said to be exact if for every $S' \to S$ the
sequence of groups $1 \to G'(S') \to G(S') \to G''(S') \to 1$ is exact.

**Lemma 5.2.1.**[^N.D.E-II-92] *Let $1 \to G' \to G \to G'' \to 1$ be an exact sequence of $S$-groups.*

<!-- label: III.II.5.2.1 -->

*(i) The sequences $1 \to T_{G'/S}(M) \to T_{G/S}(M) \to T_{G''/S}(M) \to 1$ and*

```text
1 ⟶ Lie(G′/S, M) ⟶ Lie(G/S, M) ⟶ Lie(G″/S, M) ⟶ 1
```

*are then exact.*

*(ii) Let $1 \to H' \to H \to H'' \to 1$ be a second sequence of groups; it is exact if and only if the sequence below
is exact:*

```text
1 ⟶ G′ ×_S H′ ⟶ G ×_S H ⟶ G″ ×_S H″ ⟶ 1.
```

*(iii) If two of the $S$-groups $G', G, G''$ satisfy (E), the third also satisfies (E).*

*(iv) If $0 \to F' \to F \to F'' \to 0$ is an exact sequence of `O_S`-modules and if two of the modules $F', F, F''$ are
good, the third is also.*

*(v) If two of the $S$-groups $G', G, G''$ are good, the third is also.*

[^N.D.E-II-93] The first part of (i) is immediate, and the second part follows. Likewise, (ii) is immediate. Let us
prove (iii). To abbreviate, write $L(M) = Lie(G, M)$, $L'(M) = Lie(G', M)$, etc. Then one has the following commutative
diagram

```text
   1 ─→ L′(M ⊕ N) ─→ L(M ⊕ N) ─→ L″(M ⊕ N) ─→ 1
              │              │             │
              ↓              ↓             ↓
   1 ─→ L′(M) ×_S L′(N) ─→ L(M) ×_S L(N) ─→ L″(M) ×_S L″(N) ─→ 1
```

in which the first (resp. the second) row is exact by (i) (resp. (i) and (ii)). Assertion (iii) follows.

Let us prove (iv). One has a commutative diagram

```text
   0 ─→ F′ ⊗_{O_S} T_{O_S/S}(M) ─→ F ⊗_{O_S} T_{O_S/S}(M) ─→ F″ ⊗_{O_S} T_{O_S/S}(M) ─→ 0
              │                          │                           │
              ↓                          ↓                           ↓
   0 ─────→ T_{F′/S}(M) ─────────→ T_{F/S}(M) ─────────→ T_{F″/S}(M) ─────→ 0
```

with exact rows (the first, because $T_{O_{S}/S}(M)$ is a free `O_S`-module hence flat, the second by (i)). It follows
that if two of the modules $F', F, F''$ are good, the third is also. Finally, (v) follows from (iii) and (iv).

**Lemma 5.2.2.** *Let $G$ be an $S$-group, `E, H` two $G$-objects, $F$ a $G$-`O_S`-module.*

<!-- label: III.II.5.2.2 -->

*(i) The canonical homomorphism $E^{G} \times_{S} H^{G} \to (E \times_{S} H)^{G}$ is an isomorphism.*

*(ii) If $F$ is a good `O_S`-module, so is $F^{G}$.*

<!-- original page 92 -->

[^N.D.E-II-94] The first assertion is immediate; let us prove the second. For every $S' \to S$, one has a commutative
diagram

```text
   F^G(I_{S′}(M)) ─────────────→ F(I_{S′}(M))
              ↑ φ                       ↑ ≃ φ_1
   F^G(S′) ⊗_{O(S′)} O(I_{S′}(M)) ─→ F(S′) ⊗_{O(S′)} O(I_{S′}(M))
```

and one must show that $\phi$ is bijective; now it is evidently injective; let us show that it is surjective. Let
$(t_{0}, \cdots, t_{n})$ be a basis of the free $O(S')$-module $O(I_{S'}(M))$ and let

```text
u = Σ_{i=0}^n f_i ⊗ t_i
```

be an element of $F(S') \otimes_{O(S')} O(I_{S'}(M))$ such that $\phi_{1}(u)$ belongs to $F^{G}(I_{S'}(M))$. Let us show
that the $f_{i}$ belong to $F^{G}(S')$.

Let $S'' \to S'$; one can consider $S''$ as above $I_{S'}(M)$ via the zero section $\epsilon_{M}$. Then, for every $g
\in G(S'')$, one has:

```text
u_{S″} = g · u_{S″} = Σ_{i=0}^n g · (f_i)_{S″} ⊗ (t_i)_{S″}.
```

Since the $(t_{i})_{S''}$ form a basis of $O(I_{S''}(M)) \simeq O(I_{S'}(M)) \otimes_{O(S')} O(S'')$ over $O(S'')$, it
follows that $g \cdot (f_{i})_{S''} = (f_{i})_{S''}$, whence $f_{i} \in F^{G}(S')$ for every $i$.

*Notations.*[^N.D.E-II-95] If $E$ is an $S$-group and $F$ a sub-$S$-group of $E$, one denotes by $E/F$ the $S$-functor
that to every $S' \to S$ associates the set $E(S')/F(S')$ of classes $\bar{x} = x F(S')$, $x \in E(S')$. If $E$ is a
commutative $S$-group then $E/F$ is a commutative $S$-group.

Let now $G$ be an $S$-group and $K$ a sub-$S$-group of $G$; set $E = Lie(G/S, M)$ and $F = Lie(K/S, M)$. The adjoint
action of $K$ on $E$ stabilizes $F$, hence induces an action of $K$ on the $S$-functor $E/F$. Then, for every $S' \to
S$, one has:

```text
(E/F)^K(S′) = { x̄ ∈ E(S′)/F(S′) | for every f : S″ → S′ and k ∈ K(S″),
                                   f^*(x̄^{-1}) Ad(k)(f^*(x̄)) ∈ F(S″) },
```

where $f^{*}(\bar{x})$ denotes the image of $\bar{x}$ in $E(S'')$.

**Theorem 5.2.3.** *Let $G$ be an $S$-group, $K$ a sub-$S$-group of $G$. Write (I 2.3.3)*

<!-- label: III.II.5.2.3 -->

<!-- original page 77 -->

```text
N = Norm_G(K),    Z = Centr_G(K).
```

*Make $K$ act on $Lie(G/S, M)$ through the adjoint representation of $G$.*

*(i) If the group law of $Lie(G/S, M)$ is commutative*[^II-5-1] [^N.D.E-II-96]*, then*

```text
Lie(N/S, M) / Lie(K/S, M) = ( Lie(G/S, M) / Lie(K/S, M) )^K.
```

*(ii) If the group law of $Lie(G/S, M)$ is commutative*[^II-5-1]*, then*

```text
Lie(Z/S, M) = Lie(G/S, M)^K.
```

*(iii) If $G$ satisfies (E) (resp. if $G$ and $K$ satisfy (E)), then $Z$ satisfies (E) (resp. $N$ satisfies (E)).*

*(iv) Suppose $G$ is good; then $Z$ is good; if moreover $G$ is very good, then $Z$ is very good.*

*(v) Suppose $G$ and $K$ are good; then $N$ is good; if moreover $G$ is very good, then $N$ is very good.*

To prove (i) and (ii)[^N.D.E-II-97] we shall use the following lemma, which follows from the diagram of exact sequences
considered in 4.1.B (with $G$ and $H$ interchanged).

**Lemma 5.2.3.0.** *Let $G$ be an $S$-group, $H$ a sub-$S$-group of $G$, and $M$ a free `O_S`-module of finite type.
Then $T_{H/S}(M)$ and $Lie(G/S, M)$ are sub-$S$-groups of $T_{G/S}(M)$ and one has:*

<!-- label: III.II.5.2.3.0 -->

```text
T_{H/S}(M) ∩_T Lie(G/S, M) = Lie(H/S, M),
```

*where one has set `T_{H/S}(M) ∩_T Lie(G/S, M) :=def T_{H/S}(M) ×_{T_{G/S}(M)} Lie(G/S, M)`.*

Since the functors considered in (i) and (ii) commute with base extension, it suffices to show the equalities of
$S$-points.

Set $H = N$ (resp. $= Z$) and let $\alpha = \pm 1$. By the preceding lemma and the definition of $N$ and $Z$ (cf. I
2.3.3), one has: $Lie(H/S, M)(S) =$

```text
{ X ∈ Lie(G/S, M)(S) ⊂ G(I_S(M)) |
       for every f : S′ → I_S(M) and u ∈ K(S′),
            f^*(X^α) · u · f^*(X^{-α}) · u^{-1} ∈ K(S′),
       resp. f^*(X) · u · f^*(X^{-1}) · u^{-1} = 1   (∗) },
```

where $f^{*}(X)$ denotes the image of $X$ in $G(S')$.

To simplify the writing, let us write

```text
g = Lie(G/S, M),    k = Lie(K/S, M),    n = Lie(N/S, M),    z = Lie(Z/S, M).
```

If $X \in Lie(H/S, M)(S)$, the equalities (∗) are valid for every $f : S' \to S$, since $f = \rho \circ \epsilon_{M}
\circ f$ factors through $I_{S}(M)$ (where $\rho : I_{S}(M) \to S$ is the structural morphism and $\epsilon_{M} : S \to
I_{S}(M)$ the zero section). One deduces that

```text
n(S)/k(S) ⊂ (g/k)^K(S)    and    z(S) ⊂ g^K(S).
```

<!-- original page 95 -->

To prove the reverse inclusions, suppose henceforth $g = Lie(G/S, M)$ commutative; then $g^{K}$ and $(g/k)^{K}$ are
commutative $S$-groups. Let $X \in g(S)$ and $\bar{X}$ its image in $(g/k)(S)$, suppose that $\bar{X} \in (g/k)^{K}(S)$
(resp. $X \in g^{K}(S)$) and let us show that $X \in n(S)$ (resp. $X \in z(S)$).

Let $f : S' \to I_{S}(M)$; let us show that the preceding condition (∗) is verified for every $u \in K(S')$. Consider
the cartesian square

```text
                p
   I_{S′}(M) ──────→ I_S(M)
       │ ρ′            │ ρ
       ↓     ρ ∘ f     ↓
       S′ ──────→     S
```

and let $h$ be the section of $\rho'$ defined by $f$. It suffices to show that, for every $v \in K(I_{S'}(M))$, one has

```text
(∗∗)   p^*(X^α) · v · p^*(X^{-α}) · v^{-1} ∈ K(I_{S′}(M)),
       resp. p^*(X) · v · p^*(X^{-1}) · v^{-1} = 1.
```

Indeed, taking $v = \rho'^{*}(u)$ and applying $h^{*}$ to (∗∗), one obtains (∗), since $\rho' \circ h = id_{S'}$ and $p
\circ h = f$.

Let us now show (∗∗); for simplicity, we shall write $X$ instead of $p^{*}(X)$. Every $v \in K(I_{S'}(M))$ is written in
a unique manner $Y \cdot k$ where $Y \in Lie(K/S, M)(S')$ and $k \in K(S')$. The expression $X^{\alpha} \cdot u \cdot
X^{-\alpha} \cdot u^{-1}$ then becomes $X^{\alpha} \cdot Y \cdot (k \cdot X^{-\alpha} \cdot k^{-1}) \cdot Y^{-1}$ which,
since $Lie(G/S, M)$ is commutative, is written $X^{\alpha} Ad(k)(X^{-\alpha})$. Now this is a priori in $Lie(G/S,
M)(S')$; taking into account Lemma 5.2.3.0, the condition (∗∗) for $X$ therefore becomes: for every $k \in K(S')$,

```text
⎰ Ad(k)(X) = X,                                if H = Z;
⎱ X^α Ad(k)(X^{-α}) ∈ Lie(K/S, M)(S′),         if H = N.
```

When $H = Z$, this condition is indeed a consequence of the hypothesis $X \in g^{K}(S)$. When $H = N$, the condition is
also written:

```text
(∗′)   Ad(k)(X) = X    and    Ad(k)(X^{-1}) = X^{-1},
```

now the second condition of (∗′) is a consequence of the first, since the action of $K$ on $g/k$ respects the group
structure of this latter. Therefore, when $H = N$, the condition (∗∗) for $X$ is indeed a consequence of the hypothesis
$\bar{X} \in (g/k)^{K}(S)$. This proves (i) and (ii).

To prove (iii)–(v), let us write $g(M) = Lie(G/S, M)$ and define similarly $k(M)$, $z(M)$ and $n(M)$. If $G/S$ satisfies
(E), then $g(M \oplus N) \simeq g(M) \times_{S} g(N)$ and therefore, by 5.2.2 (i),

```text
g(M ⊕ N)^K ≃ g(M)^K ×_S g(N)^K,
```

<!-- original page 96 -->

whence $z(M \oplus N) \simeq z(M) \times_{S} z(N)$, so $Z$ satisfies (E). If moreover $K/S$ satisfies (E), one obtains
successively isomorphisms:

```text
(g/k)(M ⊕ N) ≃ (g/k)(M) ×_S (g/k)(N),
(g/k)^K(M ⊕ N) ≃ (g/k)(M)^K ×_S (g/k)(N)^K,
```

then a commutative diagram:

```text
   0 ─→ k(M ⊕ N) ─→ n(M ⊕ N) ─→ (n/k)(M ⊕ N) ─→ 0
            ≀ │              │                ≀ │
              ↓              ↓                  ↓
   0 ─→ k(M) ×_S k(N) ─→ n(M) ×_S n(N) ─→ (n/k)(M) ×_S (n/k)(N) ─→ 0
```

from which it follows that $n(M \oplus N) \simeq n(M) \times_{S} n(N)$, so $N$ satisfies (E).

Henceforth, write $g = g(O_{S}) = Lie(G/S)$ and define similarly `k, z, n`. If $G$ is good, $g$ is a good `O_S`-module
so, by 5.2.2 (ii), $z \simeq g^{K}$ is also, so $Z$ (which satisfies (E) by (iii)) is good. If moreover $K$ is good,
then $k$ is a good `O_S`-module so, by 5.2.1 (iv) and 5.2.2 (ii), so are $g/k$ and $(g/k)^{K}$. Taking into account the
exact sequence

$$ 0 \longrightarrow k \longrightarrow n \longrightarrow (g/k)^{K} \longrightarrow 0, $$

one obtains, by 5.2.1 (iv) again, that $n$ is good. Finally, if in addition to the preceding conditions, $G$ is very
good, i.e., if one has identically $[x, x] = 0$ for every $x \in g$, it is clear that $Z$ and $N$ are very good. This
proves (iii), (iv) and (v).

**Corollary 5.2.3.1.** *One has `Lie(Centr(G)/S) = Lie(G/S)^G` if the group law of $Lie(G/S)$ is commutative.*

<!-- label: III.II.5.2.3.1 -->

**Corollary 5.2.3.2.** *If the group law of $Lie(G/S)$ is commutative and if $K$ is a normal subgroup of $G$, then*

<!-- label: III.II.5.2.3.2 -->

```text
( Lie(G/S) / Lie(K/S) )^K = Lie(G/S) / Lie(K/S).
```

### 5.3. Linear representations

<!-- label: III.II.5.3 -->

<!-- original page 79 -->

Let $G$ be a good $S$-group acting linearly on a good `O_S`-module $F$ via

$$ \rho : G \longrightarrow \operatorname{Aut}_{O_{S}-mod.}(F). $$

One has defined (4.7.1 and 4.8.2) a corresponding linear representation

```text
ρ′ : Lie(G/S) ⟶ End_{O_S-mod.}(F).
```

The sub-$S$-groups $Norm_{G}(E)$ and $Centr_{G}(E)$ are defined for every part $E$ of $F$, for example for every
sub-`O_S`-module $E$ of $F$.

<!-- original page 97 -->

**Definition 5.3.0.** *One will pose analogously: for every $S' \to S$,*

<!-- label: III.II.5.3.0 -->

```text
Norm_{Lie(G/S)}(E)(S′) = { X ∈ Lie(G/S)(S′) | ρ′(X) E_{S′} ⊂ E_{S′} };
Centr_{Lie(G/S)}(E)(S′) = { X ∈ Lie(G/S)(S′) | ρ′(X) E_{S′} = 0 }.
```

*(Note that this construction can be made for any linear representation of an `O_S`-"Lie algebra" (in the sense of 4.9)
and that the two subobjects constructed are sub-`O_S`-modules stable under the bracket.)*

**Theorem 5.3.1.** *Let $G$ be a good $S$-group acting linearly on a good `O_S`-module $F$ and let $E$ be a
sub-`O_S`-module of $F$.*

<!-- label: III.II.5.3.1 -->

*(i) One has `Lie(Centr_G(E)/S) = Centr_{Lie(G/S)}(E)` and $Centr_{G}(E)$ is a good $S$-group; it is very good if $G$
is.*

*(ii) Suppose that $E$ is a good `O_S`-module. Then*[^N.D.E-II-98] *`Lie(Norm_G(E)/S) = Norm_{Lie(G/S)}(E)` and
$Norm_{G}(E)$ is a good $S$-group; it is very good if $G$ is.*

The proof is left to the reader.

**5.3.2.** Let $G$ be a good $S$-group; what precedes applies in particular to the case where one takes for $\rho$ the
adjoint representation of $G$. Let $E$ be a good[^N.D.E-II-99] sub-module of $Lie(G/S)$; to it one therefore associates
two subgroups of $G$, its centralizer and its normalizer. By 5.3.1, their Lie algebras are respectively the centralizer
and the normalizer of $E$ in $Lie(G/S)$ computed as usual by means of the bracket:

```text
Centr_{Lie(G/S)}(E)(S′) = { X ∈ Lie(G/S)(S′) | [X, E_{S′}] = 0 },
Norm_{Lie(G/S)}(E)(S′)  = { X ∈ Lie(G/S)(S′) | [X, E_{S′}] ⊂ E_{S′} }.
```

**5.3.3.** Let $K$ be a sub-$S$-group of $G$, then $Lie(K/S)$ is a sub-`O_S`-module of $Lie(G/S)$; suppose that
$Lie(K/S)$ is a good `O_S`-module[^N.D.E-II-99] (which is the case if $K$ is a good $S$-group). One evidently has

```text
Centr_G(K) ⊂ Centr_G(Lie(K/S)),
Norm_G(K) ⊂ Norm_G(Lie(K/S)),
```

whence, by 5.3.1,

```text
Lie(Centr_G(K)/S) ⊂ Centr_{Lie(G/S)}(Lie(K/S)),
Lie(Norm_G(K)/S) ⊂ Norm_{Lie(G/S)}(Lie(K/S)),
```

but none of these four inclusions is a priori an equality; we shall see by the sequel many examples.

It follows in particular from these inclusions that if $K$ is a normal subgroup of $G$, then $Lie(K/S)$ is an ideal of
$Lie(G/S)$.

## 6. Miscellaneous remarks

<!-- label: III.II.6 -->

<!-- original page 98 -->

**6.1.** One can define the bracket of two infinitesimal automorphisms for an $S$-functor $X$ which is not necessarily a
group. It suffices to apply the results of this Exposé to the group $\operatorname{Aut}_{S}(X)$. To arrive at an
agreeable formalism, one is led to suppose $X$ good, i.e. to suppose that the `O_X`-module $T_{X/S}$ is good (if $X$ is
an $S$-group, this definition evidently coincides with Definition 4.6).

**6.2.** There exist functors possessing infinitesimal endomorphisms that are not automorphisms, hence a fortiori not
satisfying condition (E).[^N.D.E-II-100] For every pointed set $(E, x_{0})$, let $MA(E)$ be the free abelian monoid
generated by $E$ and let $MAP(E, x_{0})$ be the abelian monoid obtained by quotienting $MA(E)$ by the equivalence
relation generated by the relation $m \sim x_{0} + m$. Then $(E, x_{0}) \mapsto MAP(E, x_{0})$ is the left adjoint of
the forgetful functor from the category of abelian monoids to that of pointed sets; one will say that $MAP(E, x_{0})$ is
the "free abelian monoid on the pointed set $(E, x_{0})$".

Take then for $X$ the functor that to every scheme $S$ associates the free abelian monoid on the set $O(S)$, pointed by
the zero element. Every morphism $f : S \to I_{\mathbb{Z}} = \operatorname{Spec}(\mathbb{Z}[\epsilon])$ corresponds to
an element of square zero $u_{f}$ of $O(S)$, and hence defines an endomorphism of $X(S)$ by $x \mapsto x + u_{f}$ (sum
in $MAP(O(S), 0)$). One thus obtains an endomorphism $\phi$ of $X_{I_{\mathbb{Z}}} = X \times_{\mathbb{Z}}
I_{\mathbb{Z}}$, defined as follows. For every $f \in I_{\mathbb{Z}}(S)$ and $x \in X(S)$,

```text
φ((x, f)) = (x + u_f, f).
```

If $f_{0} : S \to I_{\mathbb{Z}}$ is the composite of the structural morphism $S \to \operatorname{Spec}(\mathbb{Z})$
and the zero section of $I_{\mathbb{Z}}$, the corresponding element is $u_{f_{0}} = 0$, and so $\phi((x, f_{0})) = (x,
f_{0})$, since $x + 0 = x$ in $MAP(O(S), 0)$. This shows that $\phi$ induces the identity on $X$; it is therefore an
infinitesimal endomorphism of $X$ which is evidently not an automorphism.

**6.3.** There exist modules that are not good. On the one hand, one can modify the preceding counterexample
slightly:[^N.D.E-II-101] take for $F(S)$ the free $O(S)$-module with basis the elements of $O(S)$; then $F$ does not
satisfy condition (E) with respect to $\operatorname{Spec}(\mathbb{Z})$; moreover, let $G$ be the $\mathbb{Z}$-group
defined by $G(S) = GL_{n}(R(S))$, where $n \geqslant 2$ and $R(S)$ is the $O(S)$-algebra of the abelian group $O(S)$;
then the $\mathbb{Z}$-group $Lie(G/\mathbb{Z})$ is not commutative.

[^N.D.E-II-102] On the other hand, one can give the following counterexamples. Let $S = \operatorname{Spec}(k)$, with
$k$ a field of characteristic $p > 0$.

*a)* Let $F$ be the `O_S`-module which to every $S$-scheme $T$ associates $F(T) = \Gamma(T, O_{T})$ equipped with the
$O(T)$-module structure obtained by making scalars act through the $p$-th power, that is to say, $r \cdot f = r^{p} f$,
for $r \in O(T)$, $f \in F(T)$. As $S$-functor of groups, $F$ is isomorphic to $G_{a, S}$. Therefore $F/S$ satisfies (E)
and $Lie(F/S)$ is identified with $Lie(G_{a, S}/S) \cong O_{S}$. Then, the canonical morphism $F \to Lie(F/S)$ is,

<!-- original page 99 -->

for every $T \to S$, the identity map $F(T) \to O(T)$: it respects the abelian-group structure but not the module
structure. Therefore $F$ is not good (cf. 4.4.1).

*b)* Let $\alpha_{p,k}$ be the $k$-functor of groups which to every $S$-scheme $T$ associates

```text
α_{p,k}(T) = { x ∈ O(T) | x^p = 0 };
```

it is represented by $\operatorname{Spec}(k[X]/(X^{p}))$ so it is a very good $S$-group; it is also equipped with an
`O_S`-module structure, but it is not a good `O_S`-module, because the canonical morphism $\alpha_{p,k} \to
Lie(\alpha_{p,k}/k) = G_{a,k}$ is not bijective.

**6.4.** Let $G$ be a group-functor on $S$. One has by definition the following implications

<!-- original page 82 -->

```text
(G/S satisfies (E)) ⇐ (G is good) ⇐ (G is very good).
```

[^N.D.E-II-103] It would be interesting to prove or counter-exemplify the implications in the reverse direction.

**6.5.**[^N.D.E-II-104] Let `Nil` be the $\mathbb{Z}$-functor of groups defined as follows: for every scheme $S$,
$Nil(S)$ is the ideal of $O(S)$ formed by the nilpotent elements, i.e.

```text
Nil(S) = { x ∈ O(S) | there exists n ∈ ℕ such that x^n = 0 }.
```

(`Nil` is very good but is not representable.) Let $Nil^{2}$, $O_{r\acute{e}d}$ and $F$ be the $\mathbb{Z}$-functors of
groups that to every scheme $S$ associate, respectively, the ideal $Nil(S)^{2}$ and

```text
O_{réd}(S) = O(S) / Nil(S),    F(S) = O(S) / Nil(S)².
```

One sees easily that $Lie(O_{r\acute{e}d}/\mathbb{Z}) = 0$, so the $O_{\mathbb{Z}}$-module $O_{r\acute{e}d}$ is not good
(although it is a good $\mathbb{Z}$-group). If `M, N` are $\mathbb{Z}$-modules free of finite rank, one has

```text
Nil²(I_S(M ⊕ N)) ≃ Nil²(S) ⊕ Nil(S) ⊗_ℤ M ⊕ Nil(S) ⊗_ℤ N
```

and therefore

```text
F(I_S(M ⊕ N)) ≃ F(S) ⊕ O_{réd}(S) ⊗_ℤ M ⊕ O_{réd}(S) ⊗_ℤ N.
```

One deduces, on the one hand, that the $\mathbb{Z}$-functor of groups $F$ satisfies condition (E) and, on the other
hand, that $Lie(F/\mathbb{Z}) = O_{r\acute{e}d}$; since this latter is not a good $O_{\mathbb{Z}}$-module, this shows
that $F$ is an example of a $\mathbb{Z}$-group that satisfies (E) but is not good.

**6.5.1.** Let us also give the counterexamples mentioned in 5.3.1–5.3.3. Let $S$ be a scheme, $F$ the good `O_S`-module
$O^{\oplus 2}_{S}$ equipped with the natural action of the good $S$-group $G = GL_{2,S}$, and $E$ the sub-`O_S`-module
of $F$ formed by the pairs $(x_{1}, x_{2})$ such that $x_{2}$ is nilpotent. Set $N = Norm_{G}(E)$. Then $Lie(N/S) =
Lie(G/S)$ while, for every $S' \to S$, one has

```text
Norm_{Lie(G/S)}(E)(S′) = { ⎡a b⎤ | a, b, c, x ∈ O(S′), x nilpotent },
                          ⎣x c⎦
```

so `Lie(Norm_G(E)/S) ≠ Norm_{Lie(G/S)}(E)`.

<!-- original page 100 -->

By considering the semi-direct product $G_{1} = F \cdot G$, one obtains an analogous counterexample where $E$ is a
sub-`O_S`-module of $Lie(G_{1}/S)$; moreover, with the notations introduced above, $E = Lie(K/S)$ where $K$ is the
subgroup $O_{S} \oplus Nil^{2}$ of $F$ (i.e., for every $S' \to S$, $K(S')$ is formed by the pairs $(x_{1}, x_{2})$ such
that $x_{2} \in Nil(S')^{2}$).

## Bibliography

[^N.D.E-II-105]

[DG70] M. Demazure, P. Gabriel, *Groupes Algébriques*, Masson & North-Holland, 1970.

[HM69] G. Hochschild, G. D. Mostow, Automorphisms of affine algebraic groups, *J. Algebra* **13** (1969), 535–543.

[MO67] H. Matsumura, F. Oort, Representability of group functors and automorphisms of algebraic schemes, *Invent. math.*
**4** (1967), 1–25.

## Footnotes

<!-- LEDGER DELTA — Exposé II — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| fibré tangent | tangent bundle | Title and throughout; context here is consistently the geometric/functorial object T_{X/S}, not the tangent sheaf. |
| fibré tangent à `X` au-dessus de `S` relativement au `O_S`-module `M` | tangent bundle to `X` above `S` relative to the `O_S`-module `M` | Definition 3.1. |
| espace tangent (au point `u`) | tangent space (at the point `u`) | Definition 3.2, `L^u_{X/S}(M)`. |
| section zéro / section nulle | zero section / null section | `ε_M` is "zero section"; `τ_0` is "null section" (used in 3.1, 3.1.1). |
| nombres duaux | dual numbers | `D_{O_S}`, `I_S`; algèbre des / schéma des. |
| algèbre de Lie | Lie algebra | Standard; `Lie(G/S)` notation preserved. |
| algèbre enveloppante | enveloping algebra | Glossary term (not actually appearing in II). |
| `p`-algèbre de Lie | `p`-Lie algebra | Glossary term (not used in II body, but kept consistent with introduction). |
| crochet | bracket | 4.7.2, 4.7.3, 4.8, etc. |
| structure de crochet | bracket structure | Used incidentally. |
| dérivation | derivation | 3.14, 4.11. |
| dérivation invariante par translation à droite | derivation invariant by right translation | 4.11. |
| automorphisme infinitésimal | infinitesimal automorphism | 4.1.4, 4.11, 6.1. |
| endomorphisme infinitésimal | infinitesimal endomorphism | 3.12.1, 3.13, 3.14, 6.1, 6.2. |
| condition (E) | condition (E) | Definition 3.5; kept literally. |
| `S`-foncteur | `S`-functor | Per Tome-I glossary. |
| `S`-H-foncteur | `S`-`H`-functor | Coined here in 3.9.0.1; we render the H literally. |
| H-ensemble / H-objet | `H`-set / `H`-object | "H-set" / "H-object" with H italics inappropriate in code; rendered as `H` in backticks where used inline. |
| foncteur en groupes | group-functor | Used for "S-foncteur en groupes" when emphasis is on the functor structure; else "S-functor of groups". |
| bon `O_S`-module / bon `S`-groupe | good `O_S`-module / good `S`-group | Definitions 4.4, 4.6. |
| très bon | very good | Definition 4.10. |
| morphisme dérivé | derived morphism | 4.1.B. |
| représentation adjointe | adjoint representation | 4.1.A. |
| représentation linéaire | linear representation | 4.1.1.1, 4.7.1, 5.3. |
| homomorphisme croisé | crossed homomorphism | Definition 4.2.A; `Z¹_S(X, L)`. |
| restriction des scalaires à la Weil | Weil restriction of scalars | 1.1 (5); kept in quotation marks per source convention. |
| fibration vectorielle | vector fibration | Per Exposé I convention. |
| section unité | unit section | Standard. |
| centralisateur / normalisateur | centralizer / normalizer | American spelling. |
| sous-groupe distingué | normal subgroup | English does not distinguish. |
| très bon / bon | very good / good | Translations of *bon* / *très bon* used only in the technical sense of Demazure here. |
| différentielles invariantes à droite | right-invariant differentials | 4.11.5. |
| relèvement | lift | 4.7.3. |
| transport de structure | transport of structure | 4.1.2.0. |
-->

[^N.D.E-II-0]: Version of 14/10/2024.

[^N.D.E-II-1]: Rendered in this edition by boldface characters `F, G, V, W`, cf. Exposé I. However, for functors such as
    `Norm` and `Centr` (cf. 5.2) the underlines have been kept in the original, and they have been added for the functor
    `Lie`, this to distinguish the functor $Lie(G/S)$ from the $\Gamma(S, O_{S})$-Lie algebra $Lie(G/S) = Lie(G/S)(S)$,
    used for example in Exposé VII_A.

[^N.D.E-II-2]: One has detailed the points (2), (3), (4); in particular, (4) will be used in 3.11.

[^N.D.E-II-3]: One has added the two preceding sentences.

[^N.D.E-II-4]: One has added this remark, useful for Corollary 3.11.1.

[^N.D.E-II-5]: Of course, if $M$ is a $Y$-group (not necessarily abelian) and if one sets $\phi \cdot \psi = m \circ
    (\phi \times \psi)$, this makes $\operatorname{Hom}_{Z/S}(X, M)$ a group above $\operatorname{Hom}_{Z/S}(X, Y)$.

[^N.D.E-II-6]: Note that $I_{S}(M)$ has the same underlying space as $S$.

[^N.D.E-II-7]: Compare with 3.1.1.

[^N.D.E-II-8]: One has detailed the original in what follows, and one has added the numbering 2.1.1 to 2.1.3.

[^N.D.E-II-9]: In the sequel, one will be principally interested in the case where $a \in O(S)$, acting by homotheties
    on $M$. For example, if $M$ is a free `O_S`-module of rank $r$, then, for every $S' \to S$,
    $\operatorname{Hom}_{S}(S', I_{S}(M))$ is identified with the set of $r$-tuples $(\epsilon_{1}, \cdots,
    \epsilon_{r}) \in O(S')$ such that $\epsilon_{i} \epsilon_{j} = 0$ for all `i, j`, and one has $(\epsilon_{1},
    \cdots, \epsilon_{r}) \cdot a = (a \epsilon_{1}, \cdots, a \epsilon_{r})$ for every $a \in O(S)$.

[^N.D.E-II-10]: One has added this paragraph, which will be useful in 3.4.2 and 4.6.2.

[^N.D.E-II-11]: See also the addition 0.1.8 in Exp. III.

[^N.D.E-II-12]: Cf. N.D.E. (33) of Exp. I.

[^N.D.E-II-13]: When $S = \operatorname{Spec}(k)$ and $X$ is a $k$-scheme, one has $T_{X/S}(S') =
    \operatorname{Hom}_{S}(S' \otimes_{k} k[\epsilon], X) = X(S' \otimes_{k} k[\epsilon])$; one thus recovers one of the
    usual definitions of the tangent bundle.

[^N.D.E-II-14]: One has corrected "$0 \to M$ and $M \to 0$" to: "$M \to 0$ and $0 \to M$".

[^N.D.E-II-15]: One has added the paragraphs 3.1.1 and 3.1.2.

[^N.D.E-II-16]: In fact, one is interested only in the action of $O(S)$ (resp. $O(S) \times O(S)$) on $\Sigma(X', M)$
    (resp. $\Sigma(X', M \oplus M)$), cf. below and the proof of 3.6.

[^N.D.E-II-17]: One has added this remark.

[^N.D.E-II-18]: Cf. EGA I, 5.3.11.

[^N.D.E-II-19]: Cf. 3.1.2.

[^N.D.E-II-20]: One has detailed the original in what follows.

[^N.D.E-II-21]: One has added Remarks 3.4.2 and 3.4.3.

[^N.D.E-II-22]: For examples of $S$-functors and $S$-groups not satisfying (E), see 6.2 and 6.3.

[^N.D.E-II-23]: One has added what follows.

[^N.D.E-II-24]: One has detailed what follows.

[^N.D.E-II-25]: I.e., for every $S$-morphism $f : X' \to X$, the action of $O(X')$ on $\operatorname{Hom}_{X}(X',
    T_{X/S}(M))$ corresponds, via the identification $\operatorname{Hom}_{X}(X', T_{X/S}(M)) \simeq
    \operatorname{Hom}_{O_{X'}}(f^{*}(\Omega^{1}_{X/S}), M \otimes_{O_{S}} O_{X'})$, to the natural action of $O(X')$ on
    the right-hand term; this follows from the proof of SGA 1, III 5.1 (see also the addition 0.1.8 in Exp. III).

[^N.D.E-II-26]: One has added the sentence that follows.

[^N.D.E-II-27]: One has added the hypothesis that $X$ and $X'$ be representable, and one has detailed what follows.

[^N.D.E-II-28]: One has detailed what follows.

[^N.D.E-II-29]: One has added this proof.

[^N.D.E-II-30]: One has added this paragraph, in order to explain the introduction of the notion of $S$-$H$-functor.

[^N.D.E-II-31]: This is inspired by the notion of $H$-space in topology.

[^N.D.E-II-32]: One has added Corollary 3.9.0.2, which will be useful in 4.1.

[^N.D.E-II-33]: Inspired by the standard proof showing that the fundamental group of an $H$-space is abelian.

[^N.D.E-II-34]: $G \times G$ is equipped with the law $(G \times G) \times (G \times G) \to G \times G$, $((x, z), (y,
    t)) \mapsto (f(x, y), f(z, t))$.

[^N.D.E-II-35]: One has added this corollary, which amplifies Remark 4.1.1.2 below.

[^N.D.E-II-36]: Setting $H = \operatorname{Hom}_{Z/S}(X, Y)$, this implies in particular that $T_{H/S}(M)$ is equipped
    with a natural structure of module over $\prod_{X \times_{S} H/H} O_{H}$. This result has seemed somewhat surprising
    to the editors; for this reason one has detailed the proof.

[^N.D.E-II-37]: One has added the sentences that follow.

[^N.D.E-II-38]: One has added the sentence that follows.

[^N.D.E-II-39]: One has added this remark.

[^N.D.E-II-40]: One has simplified the original in what follows.

[^N.D.E-II-41]: Via the isomorphism $\operatorname{Hom}_{I_{S}(M)}(U_{I_{S}(M)}, X_{I_{S}(M)}) \simeq
    \operatorname{Hom}_{S}(U \times_{S} I_{S}(M), X)$, this is equivalent to Remark 3.1.1. Likewise, 3.12 is equivalent
    to the first part of Remark 3.4.2.

[^N.D.E-II-42]: One has detailed the original in what follows.

[^N.D.E-II-43]: When $M = O_{X}$, these are called "infinitesimal endomorphisms" of $X$; see 6.2 at the end of this
    Exposé.

[^N.D.E-II-44]: One has detailed the original in what follows.

[^N.D.E-II-45]: One has added the proof that follows.

[^N.D.E-II-46]: One has added what follows.

[^N.D.E-II-47]: One has added the reminder of 2.2.2, and detailed the sequel.

[^N.D.E-II-48]: Moreover, this isomorphism is functorial in $S$: if $S' \to S$, setting $X' = X_{S'}$, one has
    $Lie(\operatorname{Aut}_{S}(X)/S)(S') \simeq \Gamma(T_{X'/S'}/X') \simeq D\acute{e}r_{O_{S'}}(O_{X'})$.

[^N.D.E-II-49]: One has added the numbering 4.1.A and 4.1.B to highlight these definitions.

[^N.D.E-II-50]: If $f$ is a monomorphism, so are $L(f)$ and $T(f)$, cf. 3.7.

[^N.D.E-II-51]: One has added this remark.

[^N.D.E-II-52]: One has detailed the original in what follows, in order to show the action of $G$ on the functors
    $\operatorname{Hom}_{G/S}(G, T_{G/S}(M))$ and $\operatorname{Hom}_{S}(G, Lie(G/S, M))$.

[^II-4-1]: The statements 4.1.2, 4.1.3 and 4.1.4 are obtained more simply by remarking that the automorphisms of $G$
    invariant by right translations are the left translations.[^N.D.E-II-53]

[^N.D.E-II-54]: One has added paragraph 4.2.0, whose results are used implicitly in 4.2 and 4.7 of the original.

[^N.D.E-II-55]: One has inserted here this definition, which in the original appeared in 4.3.

[^N.D.E-II-56]: One has detailed the original in what follows; in particular, one has added Definition 4.2.A and Remark
    4.2.B.

[^N.D.E-II-57]: This is Definition 4.2.0.1 applied to $Z = Y$ and to the $Y$-groups $u : X \to Y$ and $T_{Y/S}(M)$.

[^N.D.E-II-58]: One has added the sentences that follow and Proposition 4.2 bis, implicit in the original.

[^N.D.E-II-59]: One has added the sentence that follows.

[^N.D.E-II-60]: One has added the sentence that follows.

[^N.D.E-II-61]: Note that on the right-hand term, this is the structure defined by $(a\phi)(x) = a \cdot \phi(x)$, where
    $a \cdot \phi(x)$ denotes the action of $a$ on $\phi(x) \in Lie(Y/S, M)$. This differs from the action $(a \cdot'
    \phi)(x) = a \cdot' \phi(x) = \phi(ax)$, but coincides with it if $Lie(Y/S, M) = Lie'(Y/S, M)$.

[^N.D.E-II-62]: One has added this remark, which will be useful in 4.5.1.

[^N.D.E-II-63]: Cf. N.D.E. (61). Moreover, one has added the sentence that follows, as well as its proof.

[^N.D.E-II-64]: One has changed $S' \to S$ to $S_{2} \to S_{1} \to S$, because one must let `S_2` and `S_1` vary (cf.
    below). Moreover, one has detailed the original in what follows.

[^N.D.E-II-65]: One found in the original the assertion that when $F/S$ satisfies (E), the morphisms (6) (and hence (7))
    are morphisms of `O_S`-modules, assertion contradicted by a counterexample given in 6.3. One has deleted this
    assertion, inserted here the example just mentioned, and modified Definition 4.4 accordingly. This is without
    consequence for the sequel.

[^N.D.E-II-66]: One has added this remark, which will be useful in 4.6.2.

[^N.D.E-II-67]: One has added this remark, which will be useful in 4.5 and 4.7.

[^N.D.E-II-68]: Taking into account the modifications in Definition 4.4 (cf. N.D.E. (65)), one has inserted here this
    remark, which in the original figured in the proof of 4.4.1.

[^N.D.E-II-69]: The original showed that (i) implies (ii) and (iii); one has added the implication (ii) ⇒ (i).

[^N.D.E-II-70]: One has added what follows.

[^N.D.E-II-71]: One has added the point (ii), immediate consequence of what precedes.

[^N.D.E-II-72]: One has added this scholie, implicit in the original, which will be useful in 4.7.1. (Here and in the
    sequel, one writes $t, t'$, etc. for variables of square zero, the letter $\epsilon$ being reserved for the unit
    section of groups.)

[^N.D.E-II-73]: One has added the sentence that follows.

[^N.D.E-II-74]: One has added this lemma.

[^N.D.E-II-75]: One has simplified the original, using the additions made in 4.3.1 and 4.5.

[^N.D.E-II-76]: One has added the numbering 4.7.1, 4.7.2, 4.7.3.

[^N.D.E-II-77]: One has added the sentence that follows.

[^N.D.E-II-78]: One has detailed the original in what follows.

[^N.D.E-II-79]: The original indicated in a footnote: "(∗) The author acknowledges, at Gabriel's request, that the
    exercise is not immediate; this is moreover the reason why it is not in the text". One has given the details, taking
    into account the addition made in 4.7.1; see also [DG70], § II.4, 4.2.

[^N.D.E-II-80]: I.e. $x$ and $y$ play symmetric roles: the image in $G(I \times I')$ of `[y, x]` equals the commutator
    $y' \tilde{x} y'^{-1} \tilde{x}^{-1}$, which is the inverse of $\tilde{x} y' \tilde{x}^{-1} y'^{-1} = [x, y]$. On
    the other hand (cf. 4.10 below), one does not know whether one necessarily has $[x, x] = 0$: if one considers $x$ as
    an element $\tilde{x} \in L(I)$ (resp. $x' \in L(I')$) it is not a priori clear that $\tilde{x}$ and $x'$ commute. .
    .

[^N.D.E-II-81]: One has detailed and simplified the original in what follows.

[^N.D.E-II-82]: One has detailed the original in what follows.

[^N.D.E-II-83]: Because one does not know whether $[x, x] = 0$, see 4.10 which follows.

[^N.D.E-II-84]: One has corrected a sign error in the original, cf. [DG70], § II.4, 4.4 and 4.6.

[^N.D.E-II-85]: One has detailed the original in what follows; in particular, one has added, for later references, the
    numbering 4.11.1 to 4.11.8.

[^N.D.E-II-86]: One has detailed what follows, taking into account the additions made in Exp. I, § 6.8.

[^N.D.E-II-87]: For this reason, the linear action of $G$ on $\omega^{1}_{G/S}$ could be called the "pre-adjoint
    action"; in fact, by abuse of language, one will still speak of "the adjoint action" on $\omega^{1}_{G/S}$. Let us
    point out here a slightly more general construction, which will be used in Exp. III (cf. in particular III 0.8).
    Suppose given, for every $Y \to S$, an `O_Y`-module $N(Y)$, and for every $S$-morphism $\phi : Z \to Y$, a morphism
    of `O_Z`-modules $N(\phi) : \phi^{*} N(Y) \to N(Z)$, which is functorial in $\phi$ (this is the case, for example,
    if $J$ is a quasi-coherent ideal of `O_S` and if one sets $N(Y) = J O_{Y}$, cf. Exp. III); then the action of $G$ on
    $\omega^{1}_{G/S}$ induces a (generalized) "adjoint action" of $G$ on the $S$-functor of abelian groups that to
    every $f : Y \to S$ associates $\operatorname{Hom}_{O_{Y}}(f^{*}(\omega^{1}_{G/S}), N(Y))$.

[^N.D.E-II-88]: One has added the preceding description of $\omega^{1}_{G/S}$, which will be useful later (for example,
    in VII_A, 5.5).

[^N.D.E-II-89]: This description of $\omega^{1}_{G/S}$ in terms of invariant differentials will not be used in the
    sequel.

[^N.D.E-II-90]: Because $Lie(G/S) \cong (\omega^{1}_{G/S})^{\vee}$ does not necessarily determine $\omega^{1}_{G/S}$.
    For example, if $S = \mathbb{A}^{1}_{k}$ ($k$ a field) and if $G$ is the $S$-group whose fiber at $s = 0$ is
    $G_{a,k}$ and the other fibers are the unit group, then $Lie(G/S) = 0$ but $Lie(G_{s}/k)(k) = k$.

[^N.D.E-II-91]: Let $f : M \to N$ be a morphism of `O_S`-modules and $P = Coker(f)$. If $V(N) \to V(M)$ is a
    monomorphism, the surjective morphism $Sym(N) \to Sym(P)$ factors through `O_S`, so $P = 0$.

[^N.D.E-II-92]: One has detailed the statement of the lemma (and its proof); this will be useful in 5.3.1.

[^N.D.E-II-93]: One has added the proof of points (iii) and (v).

[^N.D.E-II-94]: One has detailed the original in what follows.

[^N.D.E-II-95]: One has detailed these notations.

[^II-5-1]: Condition automatically verified if $G$ satisfies (E) (cf. 3.9), for example if $G$ is representable.

[^N.D.E-II-96]: For an example where the $S$-group $Lie(G/S)$ is not commutative, see 6.3.

[^N.D.E-II-97]: One has detailed the proof, adding in particular Lemma 5.2.3.0, implicit in the original.

[^N.D.E-II-98]: One has corrected the original, which stated the equality that follows without hypotheses on $E$; see
    6.5.1 for counterexamples.

[^N.D.E-II-99]: One has added this hypothesis; cf. 6.5.1.

[^N.D.E-II-100]: One has detailed the original in what follows. In particular, the correct definition of the "free
    abelian monoid on a pointed set" was pointed out to us by O. Gabber.

[^N.D.E-II-101]: One has added what follows.

[^N.D.E-II-102]: In what follows, one has detailed example a) and added example b).

[^N.D.E-II-103]: And $G$ is very good if it is representable (4.11). For representability criteria, see for example
    [MO67]. On the other hand, for the automorphisms of an affine algebraic group (over an algebraically closed field of
    characteristic 0), let us cite [HM69].

[^N.D.E-II-104]: One has added this paragraph.

[^N.D.E-II-105]: Additional references cited in this Exposé.

[^N.D.E-II-53]: See for example the proof of Propositions 4.6 and 2.5 of [DG70], § II.4.
