# Exposé IX. Algebraic geometry and formal geometry

<!-- label: IX -->

<!-- original page 99 -->

The goal of this Exposé is to generalize, to the case of a morphism that is not proper, Theorems 3.4.2 and 4.1.5 of EGA
III.

## 1. The comparison theorem

<!-- label: IX.1 -->

Let $f: X \to X'$ be a separated morphism of preschemes of finite type. Suppose that $X$ is locally noetherian. Let $Y'$
be a closed subset of $X'$ and let $Y = f^{-1}(Y')$.

Let $\hat{X}$ and $\hat{X}'$ be the formal completions of $X$ and $X'$ along $Y$ and $Y'$. Let $\hat{f}$ be the morphism
deduced from $f$ by passing to the completions.

```text
    X ◀───── Y               X̂ ──j──▶  X
    │                        │           │
    │ f                      │ f̂         │ f
    ▼                        ▼           ▼
    X′ ◀──── Y′      ,       X̂′ ──i──▶ X′.
```

<!-- label: eq:IX.1.1 -->

<!-- TRANSLATOR NOTE: The source diagram (1.1) places the inclusions `Y → X` and `Y′ → X′` to the left, and the
completion-passing square on the right; the OCR has fractured the layout. The left half merely records the closed
subsets `Y ⊂ X` and `Y′ = f(Y) ⊂ X′`, with `f` restricting to `f: Y → Y′`. The square that matters in what follows is
the one on the right. -->

We denote by $j$ (resp. $i$) the homomorphism from $\hat{X}$ into $X$ (resp. from $\hat{X}'$ into $X'$). It is known
that $i$ and $j$ are flat.

Let $I'$ be an ideal of definition of $Y'$, and let $J = f*(I')\cdot \mathcal{O}_{X}$; this is an ideal of definition of
$Y$. One therefore has:

```text
X̂′ = (Y′, lim_{k ∈ ℕ} 𝒪_{X′}/I′^{k+1}),    X̂ = (Y, lim_{k ∈ ℕ} 𝒪_X/J^{k+1}).
```

<!-- label: eq:IX.1.2 -->

For every $k \in \mathbb{N}$, set:

```text
Y′_k = (Y′, 𝒪_{X′}/I′^{k+1}),    Y_k = (Y, 𝒪_X/J^{k+1}).
```

<!-- label: eq:IX.1.3 -->

Let $F$ be a coherent $\mathcal{O}_{X}$-Module. For every $k \in \mathbb{N}$, we set:

```text
F_k = F/J^{k+1}F,    F̂ = j*(F) ≃ lim_{k} F_k.
```

<!-- label: eq:IX.1.4 -->

<!-- original page 100 -->

If we set:

```text
R^i f_*(F)^∧ = lim_{k ∈ ℕ} (R^i f_*(F) ⊗_{𝒪_{X′}} 𝒪_{Y′_k}),    i ∈ ℤ,
```

<!-- label: eq:IX.1.5 -->

<!-- original page 80 -->

one has a natural homomorphism:

```text
r_i: i*(R^i f_*(F)) → R^i f_*(F)^∧,
```

<!-- label: eq:IX.1.6 -->

which is an isomorphism when $R^{i} f_{*}(F)$ is coherent.

As is explained in
[EGA III 4.1.1](https://jcreinhold.github.io/ega/iii/11-ch3-04-fundamental-theorem-proper-morphisms.html#41-the-fundamental-theorem),
one has a commutative diagram:

```text
                       ρ_i
   i*(R^i f_*(F))  ──────▶  R^i f̂_*(F̂)
        │                       │
     r_i│                       │ψ_i
        ▼          ϕ_i          ▼
   R^i f_*(F)^∧  ──────▶  lim_{k ∈ ℕ} R^i f_*(F_k).
```

<!-- label: eq:IX.1.7 -->

In loc. cit. one finds a commutative diagram, since one knows that $R^{i} f_{*}(F)$ is coherent, and one identifies the
source and target of (1.6). In our case, $R^{i} f_{*}(F)$ will be coherent only for certain values of $i$, for which we
shall study (1.7).

Consider the graded ring

```text
S = ⨁_{k ∈ ℕ} I′^k,
```

<!-- label: eq:IX.1.8 -->

and the graded $S$-Module:

```text
H^i = ⨁_{k ∈ ℕ} R^i f_*(J^k F),    i ∈ ℤ,
```

<!-- label: eq:IX.1.9 -->

whose $S$-Module structure is defined as follows.

<!-- original page 101 -->

The sheaf $R^{i} f_{*}(J^{k} F)$ is associated with the presheaf which, to every affine open $U'$ of $X'$, associates:

```text
H^i(f⁻¹(U′), J^k F | f⁻¹(U′)).
```

<!-- label: eq:IX.1.10 -->

Let $U'$ then be an affine open of $X'$, set

$$ U = f^{-1}(U'), $$

and let $x' \in I'^{m}(U')$. Let $x$ be the image of $x'$ in $J^{m}(U)$. The homothety of ratio $x$ on $F | U$ maps
$J^{k} F | U$ into $J^{k+m} F | U$, whence, by functoriality, a morphism:

```text
μ^i_{x′, k}(U′): H^i(U, J^k F | U) → H^i(U, J^{k+m} F | U),
```

<!-- label: eq:IX.1.11 -->

defined for every $i \in \mathbb{Z}$ and every $k \in \mathbb{N}$, which gives, by passing to the associated sheaf, the
graded $S$-Module structure on $H^{i}$.

**Theorem.**

<!-- label: IX.1.1 -->

Let $n$ be an integer. Suppose that the graded $S$-Module $H^{i}$ is of finite type for $i = n - 1$ and $i = n$. Then:

(0) $r_{n}$ and $r_{n-1}$ are isomorphisms, and $R^{i} \hat{f}_{*}(\hat{F})$ is coherent for $i = n - 1$;

(1) for $i = n - 1$, $\rho_{i}$, $\varphi_{i}$, and $\psi_{i}$ are topological isomorphisms (in particular, the
filtration defined on $R^{n-1} f_{*}(F)$ by the kernels of the homomorphisms

```text
R^{n−1} f_*(F) → R^{n−1} f_*(F_k)
```

<!-- label: eq:IX.1.12 -->

is $I'$-good);

<!-- original page 81 -->

(2) for $i = n$, $\rho_{i}$, $\varphi_{i}$, and $\psi_{i}$ are monomorphisms; furthermore, the filtration on $R^{n}
f_{*}(F)$ is $I'$-good and $\psi_{n}$ is an isomorphism;

(3) the projective system of the $R^{i} f_{*}(F_{k})$ satisfies, for $i = n - 2, n - 1$, the uniform Mittag-Leffler
condition, i.e. there exists a fixed integer $k \geqslant 0$ such that, for every $p \geqslant 0$ and every $p'
\geqslant p + k$, one has:

```text
Im[R^i f_*(F_{p′}) → R^i f_*(F_p)] = Im[R^i f_*(F_{p+k}) → R^i f_*(F_p)].
```

<!-- original page 102 -->

Proceeding as in
[EGA III 4.1.8](https://jcreinhold.github.io/ega/iii/11-ch3-04-fundamental-theorem-proper-morphisms.html#41-the-fundamental-theorem),
it is easy to reduce to the case where $X'$ is the spectrum of a noetherian ring $A$. In this case, one knows that

```text
R^i f_*(F) = H^i(X, F)^~     (cf. 1.10).
```

<!-- label: eq:IX.1.13 -->

Let $I$ be the ideal of $A$ such that $\tilde{I} = I'$, and let

```text
S = ⨁_{k ∈ ℕ} I^k,
```

<!-- label: eq:IX.1.14 -->

```text
H^i = ⨁_{k ∈ ℕ} H^i(X, J^k F),    i ∈ ℤ,
```

<!-- label: eq:IX.1.15 -->

where $H^{i}$ is equipped with the graded $S$-module structure defined by 1.11, where one has taken $U' = X'$.

The proof is modelled on that of
[EGA III 4.1.5](https://jcreinhold.github.io/ega/iii/11-ch3-04-fundamental-theorem-proper-morphisms.html#41-the-fundamental-theorem);
let us give a summary.

We work on $\varphi_{i}$ and $\psi_{i}$, which correspond to homomorphisms of modules:

```text
                              H^i(X̂, F̂)
                                  │
                                  │ψ_i
                  ϕ_i             ▼
   H^i(X, F)^∧  ──────▶  lim_{k} H^i(X, F_k).
```

<!-- label: eq:IX.1.16 -->

<!-- original page 103 -->

(a) We assume only that $H^{i}$ is a graded $S$-module of finite type. We deduce that the filtration defined on
$H^{i}(X, F)$ by the modules:

```text
R^i_k = ker(H^i(X, F) → H^i(X, F_k))
```

<!-- label: eq:IX.1.17 -->

is $I$-good. For this, we use the cohomology exact sequence:

```text
H^i(X, J^{k+1} F) → H^i(X, F) → H^i(X, F_k),
```

<!-- label: eq:IX.1.18 -->

which shows that the graded $S$-module $\bigoplus_{k \in \mathbb{N}} R^{i}_{k}$ is a quotient of the graded
$S$-submodule

```text
⨁_{k ∈ ℕ} H^i(X, J^{k+1} F)
```

of $H^{i}$, hence is of finite type, since $S$ is noetherian. Whence this first point.

Set:

```text
M^i = H^i(X, F),    H^i_k = H^i(X, F_k).
```

<!-- label: eq:IX.1.19 -->

<!-- original page 82 -->

One has a commutative diagram:

```text
                     s_i
   H^i(X, F)^∧  ─────────▶  lim_{k} (M^i / R^i_k)
        \                         │
         \                        │
          \ ϕ_i                   │ t_i
           \                      ▼
            ──────────────▶  lim_{k} H^i_k,
```

<!-- label: eq:IX.1.20 -->

in which $s_{i}$ is an isomorphism; indeed, the filtration of $H^{i}(X, F)$ is $I$-good. Moreover, $t_{i}$ is a
monomorphism; indeed, the functor `lim` is left exact, and, for every $k \geqslant 0$, the natural morphism $M^{i} /
R^{i}_{k} \to H^{i}_{k}$ is a monomorphism, by definition of $R^{i}_{k}$.

To study the surjectivity of $t_{i}$, we introduce:

```text
Q^i_k = coker(H^i(X, F) → H^i(X, F_k)),
```

<!-- label: eq:IX.1.21 -->

<!-- original page 104 -->

whence a projective system of exact sequences:

```text
0 → R^i_k → M^i → H^i_k → Q^i_k → 0.
```

<!-- label: eq:IX.1.22 -->

Using the cohomology exact sequence:

```text
H^i(X, F) → H^i(X, F_k) → H^{i+1}(X, J^{k+1} F),
```

<!-- label: eq:IX.1.23 -->

one sees that the graded $S$-module

```text
Q^i = ⨁_{k ∈ ℕ} Q^i_k
```

<!-- label: eq:IX.1.24 -->

is a graded $S$-submodule of $H^{i+1}$. Moreover, for every $k \geqslant 0$, one has:

$$ I^{k+1} Q^{i}_{k} = 0, $$

<!-- label: eq:IX.1.25 -->

since $Q^{i}_{k}$ is the image of $H^{i}_{k}$.

(b) We assume only that $H^{i+1}$ is of finite type, and we focus on $t_{i}$ (forgetting $s_{i}$). Since $S$ is
noetherian, $Q^{i}$ is of finite type; since $I^{k+1} Q^{i}_{k}$ vanishes, we find that there exist an integer $r
\geqslant 0$ and an integer $k_{0} \geqslant 0$ such that

```text
I^r Q^i_k = 0    for k ⩾ k₀.
```

<!-- label: eq:IX.1.26 -->

It follows that the projective system $(Q^{i}_{k})_{k \in \mathbb{N}}$ is essentially zero, and hence the projective
system $(H^{i}_{k})_{k \in \mathbb{N}}$ satisfies the uniform Mittag-Leffler condition. From the exact sequence (1.22)
one deduces the exact sequence

```text
0 → M^i / R^i_k → H^i_k → Q^i_k → 0,
```

<!-- label: eq:IX.1.27 -->

whence the exact sequence:

```text
0 → lim_{k} M^i / R^i_k  ──t_i──▶  lim_{k} H^i_k → lim_{k} Q^i_k.
```

<!-- label: eq:IX.1.28 -->

<!-- original page 105 -->

Now the projective system $(Q^{i}_{k})_{k \in \mathbb{N}}$ is essentially zero, hence $t_{i}$ is an isomorphism.

(c) Let us prove that, if $H^{i}$ is of finite type, then $\psi_{i}$ is an isomorphism. It suffices to apply [EGA 0_III
13.3.1](https://jcreinhold.github.io/ega/iii/06-ch0-13-projective-limits-homological-algebra.html#133-application-cohomology-of-a-projective-limit-of-sheaves),
taking as a basis of opens of $X$ the affine opens. This is legitimate;

<!-- original page 83 -->

indeed, by (b), the projective system $(H^{i-1}_{k})_{k \in \mathbb{N}}$ satisfies the Mittag-Leffler condition.

The theorem follows formally from (a), (b), and (c). One will note that, in fact, the proof uses, at each step, the
finiteness of $H^{i}$ only for a single value of $i$.

Let us give some examples in which the hypothesis of Theorem 1.1 is satisfied.

**Corollary.**

<!-- label: IX.1.2 -->

Suppose that $I'$ is generated by a section $t'$ of $\mathcal{O}_{X'}$, and denote by $t$ the corresponding section of
$\mathcal{O}_{X}$. Let $F$ be a coherent $\mathcal{O}_{X}$-module and let $n$ be an integer. Suppose that:

(i) $t$ is $F$-regular (i.e. the homothety of ratio $t$ on $F$ is a monomorphism).

(ii) $R^{i} f_{*}(F)$ is coherent for $i = n - 1$ and $i = n$.

Then the hypothesis of Theorem 1.1 is satisfied.

Indeed, one observes that multiplication by $t^{k}$ defines an isomorphism $F \xrightarrow{\sim} J^{k} F$, and one
deduces that

```text
H^i ≃ R^i f_*(F) ⊗_{𝒪_{X′}} 𝒪_{X′}[T],
```

<!-- label: eq:IX.1.29 -->

where $T$ is an indeterminate. Whence the conclusion.

**Corollary.**

<!-- label: IX.1.3 -->

<!-- original page 106 -->

Suppose that $X' = \operatorname{Spec}(A)$, where $A$ is a noetherian ring separated and complete for the $I$-adic
topology. Suppose that the $S$-module $H^{i}$ is of finite type for $i = n - 1$ and $i = n$ (cf. 1.14 and 1.15). Then
the hypotheses of Theorem 1.1 are satisfied, and one finds a commutative diagram of isomorphisms:

```text
                    ρ′_i
   H^i(X, F)  ─────────────▶  H^i(X̂, F̂)
         \                      /
          \                    /
           \ ϕ′_i         ψ_i /
            \                /
             ▼              ▼
              lim_{k} H^i(X, F_k)              for i = n − 1.
```

<!-- label: eq:IX.1.3.1 -->

<!-- TRANSLATOR NOTE: The source labels this diagram "(1.1)" which conflicts with diagram (1.1) above; I label it
eq:IX.1.3.1 to disambiguate, following the SGA 2 numbering convention. -->

[^N.D.E-IX-1]

<!-- original page 84 -->

One simply notes that $H^{i}(X, F)$ is of finite type, hence isomorphic to its completion. One obtains (1.1) by
transcribing the diagram of Modules (1.7) into the category of $A$-modules, and replacing the left vertical by $H^{i}(X,
F)$.

**Proposition.**

<!-- label: IX.1.4 -->

Let $A$ be a noetherian ring. Let $t \in A$ and suppose that $A$ is separated and complete for the `(tA)`-adic topology.
Set:

```text
X′ = Spec(A),    Y′ = V(t),    I = (tA).
```

<!-- label: eq:IX.1.31 -->

Let $T$ be a closed subset of $X'$; set

```text
X = X′ − T,    Y = Y′ ∩ X = Y′ − (Y′ ∩ T).
```

<!-- label: eq:IX.1.32 -->

Let $F$ be a coherent $\mathcal{O}_{X}$-Module. Finally, let

```text
T′ = {x ∈ X′ | codim({x} ∩ T, {x}) = 1}.
```

<!-- label: eq:IX.1.33 -->

Suppose that:

a) $t$ is $F$-regular,

b) $prof_{T'}(F) \geqslant n + 1$,

c) $A$ is a quotient of a regular noetherian ring.

Then, in diagram (1.1), the morphisms $\rho'_{i}$, $\varphi'_{i}$, and $\psi_{i}$ are isomorphisms for $i < n$ and
monomorphisms for $i = n$. Moreover $\psi_{n}$ is an isomorphism.

<!-- original page 107 -->

By virtue of 1.3 and 1.2, it suffices to prove that $R^{i} f_{*}(F)$ is coherent for $i \leqslant n$, which follows from
the finiteness theorem 2.1.[^N.D.E-IX-4]

In particular:

**Example.**

<!-- label: IX.1.5 -->

One will apply 1.4 when $A$ is a local ring and $t$ belongs to the radical $r(A)$ of $A$. One will then take $T =
{r(A)}$. In this case, for $n = 1$, one obtains the following statement:

If $A$ is noetherian, separated and complete for the $t$-adic topology, and a quotient of a regular ring (for example,
if $A$ is complete), if moreover $t$ is $F$-regular and if $prof F_{x} \geqslant 2$ for every $x \in
\operatorname{Spec}(A)$ such that $\dim A/x = 1$, then the natural homomorphism

```text
Γ(X, F) → Γ(X̂, F̂)
```

is an isomorphism.

Indeed, keeping the notation of 1.4, one has $T = {r(A)}$, and formula (1.33) says that

```text
T′ = {x ∈ Spec(A) | dim A/x = 1}.
```

<!-- original page 85 -->

## 2. The existence theorem

<!-- label: IX.2 -->

Let us first state
[EGA III 3.4.2](https://jcreinhold.github.io/ega/iii/10-ch3-03-finiteness-proper-morphisms.html#34-the-finiteness-theorem-case-of-formal-schemes)
in a slightly more general form.

Let $f: X \to X'$ be an adic morphism[^IX-2-star] of formal preschemes, with $X'$ noetherian. Let $I'$ be an ideal of
definition of $X'$; since $f$ is adic, $f*I' = J$ is[^N.D.E-IX-2] an ideal of definition of $X$.

For every $n \in \mathbb{N}$, set

$$ X_{n} = (X, \mathcal{O}_{X}/J^{n+1}); $$

<!-- label: eq:IX.2.1 -->

this is an ordinary prescheme having the same underlying topological space as $X$.

Let $F$ be a coherent $\mathcal{O}_{X}$-Module. For every $k \in \mathbb{N}$, the $\mathcal{O}_{X_{k}}$-Modules

<!-- original page 108 -->

$$ F_{k} = F/J^{k+1} F $$

<!-- label: eq:IX.2.2 -->

are coherent. For every $i$, one has a homomorphism

```text
ψ_i: R^i f_*(F) → lim_{k} R^i f_*(F_k),
```

<!-- label: eq:IX.2.3 -->

deduced by functoriality from the natural homomorphism:

$$ F \to F_{k}. $$

<!-- label: eq:IX.2.4 -->

Set

```text
S = gr_{I′} 𝒪_{X′} = ⨁_{k ∈ ℕ} I′^k / I′^{k+1},
```

<!-- label: eq:IX.2.5 -->

```text
gr_J(F) = ⨁_{k ∈ ℕ} J^k F / J^{k+1} F,
```

<!-- label: eq:IX.2.6 -->

```text
K^i = R^i f_*(gr_J(F)) = ⨁_{k ∈ ℕ} R^i f_*(J^k F / J^{k+1} F).
```

<!-- label: eq:IX.2.7 -->

It is clear that $K^{i}$ is equipped with a graded $S$-Module structure.

**Theorem.**

<!-- label: IX.2.1 -->

Suppose that $K^{i}$ is a graded $S$-Module of finite type for $i = n - 1$, $i = n$, $i = n + 1$. Then:

(i) $R^{n} f_{*}(F)$ is coherent.

(ii) The homomorphism $\psi_{n}$ (2.3) is a topological isomorphism. The natural filtration of the right-hand side of
(2.3) is $I'$-good.

(iii) The projective system of the $R^{n} f_{*}(F_{k})$ satisfies the uniform Mittag-Leffler condition.

<!-- original page 109 -->

The proof is very easy from
[EGA 0_III 13.7.7](https://jcreinhold.github.io/ega/iii/06-ch0-13-projective-limits-homological-algebra.html#137-derived-functors-of-a-projective-limit-of-arguments)
(cf. EGA III 3.4.2), provided one corrects the text on page 78 as indicated in
([EGA III 2](https://jcreinhold.github.io/ega/iii/09-ch3-02-cohomology-projective-morphisms.html#2-cohomological-study-of-projective-morphisms),
Err_III 24).

<!-- original page 86 -->

**Theorem.**

<!-- label: IX.2.2 -->

[^N.D.E-IX-3]

Let $A$ be a noetherian adic ring and let $I$ be an ideal of definition of $A$. Let $T$ be a closed subset of $X' =
\operatorname{Spec}(A)$. Suppose that $I$ is generated by a $t \in A$. Take up the notation 1.31, 1.32, and 1.33. Let
$F$ be a coherent $\mathcal{O}_{\hat{X}}$-Module. Set

$$ F_{0} = F/J F, $$

<!-- label: eq:IX.2.2.1 -->

where $J = t\mathcal{O}_{\hat{X}}$ is an ideal of definition of $\hat{X}$. Suppose that $A$ is a quotient of a regular
noetherian ring and that:

(1) $t$ is $F$-regular,

(2) $prof_{T'} F_{0} \geqslant 2$.

Then there exists a coherent $\mathcal{O}_{X}$-Module $\tilde{F}$ such that $\tilde{F}^{\wedge} \simeq F$.

<!-- TRANSLATOR NOTE: In the source the conclusion is "il existe un O_X-Module cohérent F tel que F̂ ≃ F"; the input
`F` (on `X̂`) and the constructed `F` (on `X`) share the same symbol. To disambiguate the conclusion in English without
altering the mathematics, we write `F̃` for the constructed `𝒪_X`-Module; in the source these are typographically the
same letter. -->

It suffices to prove that $\hat{f}_{*}(F)$ is a coherent $\mathcal{O}_{\hat{X}'}$-Module, where $\hat{f}: \hat{X} \to
\hat{X}'$ is the morphism of formal preschemes deduced from the injection of $X$ into $X'$ by completion with respect to
$t$. Indeed, $A$ is separated and complete for the $t$-adic topology, so there will exist an $A$-module $F'$ whose
completion will be isomorphic to $\hat{f}_{*}(F)$. Since $X$ is an open of $X'$, one will be able to take $\tilde{F} =
\tilde{F}' | X$.

It remains to show that 2.1 is applicable to the morphism of formal preschemes $\hat{f}$ and to $F$. Now, by hypothesis
(1), for every $k \in \mathbb{N}$ one has an isomorphism:

```text
J^k F / J^{k+1} F → F/J F,
```

<!-- original page 110 -->

whence it follows that the hypothesis of 2.1 will be satisfied if one knows that

```text
R^i f_*(F₀) is coherent for i ⩽ 1.
```

Now this follows from (2) and from the finiteness theorem 2.1.[^N.D.E-IX-4] Whence the conclusion.

It remains to specialize this statement by supposing that $A$ is a local ring.

**Corollary.**

<!-- label: IX.2.3 -->

Let $A$ be a noetherian local ring and let $t \in r(A)$ be an element of the radical of $A$. Suppose that $A$ is
separated and complete for the $t$-adic topology and, moreover, a quotient of a regular ring (for example, suppose that
$A$ is a complete noetherian local ring). Set

```text
X′ = Spec A,    T = {r(A)},
```

<!-- label: eq:IX.2.9 -->

<!-- original page 87 -->

and take up the notation (1.31), (1.32), and (1.33). Let $F$ be an $\mathcal{O}_{\hat{X}}$-Module. Suppose that:

(1) $t$ is $F$-regular,

(2) $prof_{T'} F_{0} \geqslant 2$, with $F_{0} = F/J F$ and $J = t\mathcal{O}_{\hat{X}}$.

Then there exists a coherent $\mathcal{O}_{X}$-Module $\tilde{F}$ such that $\tilde{F}^{\wedge} \simeq F$.

Note that here $T'$ is the set of prime ideals $p$ of $A$ such that $\dim A/p = 1$.

<!--
LEDGER DELTA (Exposé IX):

| French | English | Note |
| --- | --- | --- |
| complété formel (de X le long de Y) | formal completion (of X along Y) | Glossary entry. Hat notation `X̂` preserved across OCR breaks. |
| morphisme déduit de f par passage aux complétés | morphism deduced from f by passing to the completions | Standard SGA proof movement. |
| idéal de définition | ideal of definition | Standard. |
| `I′`-bonne (filtration) | `I′`-good (filtration) | Standard EGA terminology for "good filtration"; kept literal. |
| homothétie de rapport t | homothety of ratio t | Standard. |
| F-régulier | F-regular | Per glossary. |
| morphisme adique | adic morphism | Standard EGA term. |
| condition de Mittag-Leffler uniforme | uniform Mittag-Leffler condition | Standard. |
| système projectif essentiellement nul | essentially zero projective system | Standard SGA terminology (cf. Exposé II ledger). |
| théorème de comparaison | comparison theorem | Glossary. |
| théorème d'existence | existence theorem | Glossary. |
| théorème de finitude | finiteness theorem | Glossary; here refers to the Exposé VIII statement (VIII 2.3). |
| anneau noethérien adique | noetherian adic ring | Standard. |
| séparé et complet pour la topologie I-adique | separated and complete for the `I`-adic topology | Standard. |
| préschéma formel | formal prescheme | Standard. |
| Module gradué de type fini | graded Module of finite type | Standard (capital Module preserved per source). |
| anneau gradué associé `gr_I` | associated graded ring `gr_I` | Standard. |
| `S`-Module gradué | graded `S`-Module | Capital preserved per source convention. |
| profondeur (prof_T) | depth (prof_T) | Per SGA 2 glossary entry "profondeur". |
| Or | Now | Pivot conjunction; not "but". |
| À savoir | namely | Standard. |
| D'où la conclusion | Whence the conclusion | Register supports "Whence" in proof closure. |
-->

[^N.D.E-IX-1]: *N.D.E.* In the same vein, see the article by Chow (Chow W.-L., "Formal functions on homogeneous spaces",
    *Invent. Math.* **86** (1986), no. 1, pp. 115–130). The author proves the following result. Let $X$ be an algebraic
    variety over a field, homogeneous under an algebraic group $G$, and let $Z$ be a complete subvariety of $X$ of
    dimension `> 0`. Suppose that $Z$ generates $X$ in the following sense: given $p \in Z$, let $\Gamma_{p}$ be the set
    of elements of $G$ sending $p$ into $Z$. One then says that $Z$ generates if the group generated by the connected
    component of `1` of $\Gamma_{p}$ is the whole of $G$. In this case, every formal rational function on $X$ along $Z$
    is algebraic; compare with the results of Hironaka and Matsumura cited in editor's note (3) p. 138. In the line of
    the techniques introduced by these authors, let us point out the very pretty algebraization result due to Gieseker
    (Gieseker D., "On two theorems of Griffiths about embeddings with ample normal bundle", *Amer. J. Math.* **99**
    (1977), no. 6, pp. 1137–1150, Theorems 4.1 and 4.2). Let $X$ be a connected projective variety of dimension `> 0`,
    locally a complete intersection (over an algebraically closed field). Suppose one has two embeddings of $X$ into
    smooth projective varieties `Y, W`. Then, if the formal completions of $X$ in $Y$ and $W$ are equivalent, there
    exists a scheme $U$ containing $X$ (as a closed subscheme) which embeds into $Y$ and $W$ as an étale neighborhood of
    $X$ in $Y$ and $W$. In other words, formally equivalent entails étale-equivalent. See also the article of Faltings
    (Faltings G., "Formale Geometrie und homogene Räume", *Invent. Math.* **64** (1981), pp. 123–165).

[^N.D.E-IX-4]: *N.D.E.* The "finiteness theorem 2.1" referenced here is the finiteness theorem of Exposé VIII (VIII
    2.3), not the Theorem 2.1 of the present Exposé; the source's local cross-reference is to the
    cohomological finiteness statement on which the existence theorem is built.
        <!-- TRANSLATOR NOTE: The source writes "théorème de
    finitude 2.1" but the only Theorem 2.1 in the present Exposé is the existence theorem itself. The intended
    reference is to the Exposé VIII finiteness theorem, which is the "finiteness theorem" referenced in the
    Introduction and at the head of this Exposé. -->

[^IX-2-star]: This hypothesis is not essential; cf. XII, p. 118.

[^N.D.E-IX-2]: *N.D.E.* By definition itself, cf.
    [EGA I 10.12.1](https://jcreinhold.github.io/ega/i/01-10-formal-schemes.html#1012-adic-morphisms-of-formal-preschemes).

[^N.D.E-IX-3]: *N.D.E.* Numerous algebraization statements have been obtained since, not to mention those cited below;
    cf. the articles of Faltings or of Mme Raynaud cited in editor's notes (22) p. 155 and (7) p. 203 respectively. One
    has in mind in particular the results of Artin (see notably Artin M., "Algebraization of formal moduli. I", in
    *Global Analysis (Papers in Honor of K. Kodaira)*, Univ. Tokyo Press, Tokyo, 1969, pp. 21–71), but also the recent
    algebraicity results for leaves of foliations; see notably Bost J.-B., "Algebraic leaves of algebraic foliations
    over number fields", *Publ. Math. Inst. Hautes Études Sci.* **93** (2001), pp. 161–221, and Chambert-Loir A.,
    "Théorèmes d'algébricité en géométrie diophantienne (d'après J.-B. Bost, Y. André, D. & G. Chudnovsky)", in
    *Séminaire Bourbaki, Vol. 2000/2001*, *Astérisque*, vol. 282, Société mathématique de France, Paris, 2002, Exp. 886,
    pp. 175–209, and the references cited therein. In particular, one will find in these two articles discussions of the
    link between algebraization questions and the theory of diophantine approximation.
