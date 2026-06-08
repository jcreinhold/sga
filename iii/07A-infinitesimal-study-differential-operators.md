# Exposé VII_A. Infinitesimal study: differential operators and restricted $p$-Lie algebras

<!-- label: III.VII_A -->

*by P. Gabriel*

<!-- original page 412 -->

In Exposé II we restricted ourselves to the study of first-order differential invariants and did not address certain
phenomena specific to characteristic $p > 0$ or to characteristic 0. Our object in part A of this Exposé is to fill in
this gap.

Moreover, the infinitesimal study of arbitrary order of a group scheme is related to that of the associated formal
group; the object of the second part of this Exposé is to present the first definitions and properties concerning formal
groups.

## A) Differential operators and restricted $p$-Lie algebras[^VII_A-A-1]

## 1. Differential operators

<!-- label: III.VII_A.1 -->

In this section, as well as in sections 2 and 3, $S$ denotes a fixed scheme and the products considered are cartesian
products in the category of $S$-schemes.[^N.D.E-VII_A-1] If $X$ is an $S$-scheme, we write $p_{X/S}$, $p_{X}$ or simply
$p$ for the structural morphism of $X$ into $S$.

### 1.1

<!-- label: III.VII_A.1.1 -->

Let $u : Y \to X$ be a morphism of $S$-schemes and endow the direct image $u_{*}(O_{Y})$ of the structure sheaf of $Y$
with the `O_X`-module structure induced by $u$. The sheaf $H = \operatorname{Hom}_{p^{-1}_{X}(O_{S})}(O_{X},
u_{*}(O_{Y}))$ of $p^{-1}_{X}(O_{S})$-module homomorphisms <!-- original page 413 --> from `O_X` into $u_{*}(O_{Y})$ is
therefore naturally equipped with a structure of `O_X`-bimodule: if $U$ is an open of $X$, $f$ and $d$ sections of `O_X`
and $H$ on $U$, then `fd` and `df` are respectively the morphisms $g \mapsto f d(g)$ and $g \mapsto d(fg)$ from `O_X`
into $u_{*}(O_{Y})$. We shall henceforth write `(ad f)(d)` in place of $fd - df$.

**Definition 1.1.1.** *An $S$-deviation of order $\leqslant n$ is by definition a pair $D = (u, d)$ consisting of a
morphism of $S$-schemes $u : Y \to X$ and a morphism of $p^{-1}_{X}(O_{S})$-modules $d : O_{X} \to u_{*}(O_{Y})$ such
that, for every open $U$ of $X$ and every sequence of $n + 1$ sections $f_{0}, \cdots, f_{n} \in O_{X}(U)$, one has in
$\operatorname{Hom}_{p^{-1}_{U}(O_{S})}(O_{U}, u_{*}(O_{Y})|_{U})$ the equality:*

<!-- label: III.VII_A.1.1.1 -->

```text
(∗_n)                    (ad f₀)(ad f₁) ··· (ad f_n)(d) = 0.
```

[^N.D.E-VII_A-2]

In this case, we shall also say that $d$ is an $S$-deviation of $u$ of order $\leqslant n$. In particular, an
$S$-deviation of $u$ of order $\leqslant 0$ is a morphism of `O_X`-modules from `O_X` into $u_{*}(O_{Y})$, i.e., an
element of $\Gamma(Y, O_{Y})$.

**Definition 1.1.2.** *A morphism of $p^{-1}_{X}(O_{S})$-modules $d : O_{X} \to u_{*}(O_{Y})$ is an $S$-deviation of $u$
if, for every point $y$ of $Y$, there exist an open neighborhood $U$ of $u(y)$ in $X$ and an open neighborhood $V$ of
$y$ in $Y$ satisfying the following conditions:*

*a) $u(V) \subset U$;*

*b) if $v : V \to U$ is the morphism induced by $u$, there is an integer $n$ such that the morphism $O_{U} \to
v_{*}(O_{V})$ induced by $d$ is an $S$-deviation of $v$ of order $\leqslant n$.*[^N.D.E-VII_A-3]

<!-- label: III.VII_A.1.1.2 -->

If $d$ is an $S$-deviation of $u$, we also say that the pair $D = (u, d)$ is an $S$-deviation and it will happen that we
write $Y \xrightarrow{D} X$ or $Y \xrightarrow{d} X$ (over $u$).

When $d$ is the algebra homomorphism $u^{\natural} : O_{X} \to u_{*}(O_{Y})$ corresponding to the morphism $u : Y \to
X$, we shall also write $u$ in place of $D$.

**Remarks 1.1.3.**[^N.D.E-VII_A-4] Let $D\acute{e}v(u)$ (resp. $D\acute{e}v_{\leqslant n}(u)$) be the set of
$S$-deviations of $u$ (resp. $S$-deviations of $u$ of order $\leqslant n$). It is equipped with a natural structure of
$O_{Y}(Y)$-module: if $\lambda \in O_{Y}(Y)$, $\lambda d$ is the deviation sending $f$ to $\lambda d(f)$, for every
section $f$ of `O_X` on an open $U$.

<!-- label: III.VII_A.1.1.3 -->

For every open $V$ of $Y$, set $\mathcal{D}\acute{e}v(u)(V) = D\acute{e}v(u|_{V})$, i.e., $\mathcal{D}\acute{e}v(u)(V)$
is the set of

```text
d_V ∈ Hom_{p_X^{-1}(O_S)}(O_X, (u|_V)_*(O_V)) ≃ Hom_{p_Y^{-1}(O_S)}((u|_V)^{-1} O_X, O_V)
                                              ≃ Hom_{p_Y^{-1}(O_S)}(u^{-1} O_X, O_Y)(V)
```

<!-- original page 444 -->

such that, for every open $U$ of $X$, the map $d_{V}(U) : O_{X}(U) \to O_{Y}(u^{-1}(U) \cap V)$ satisfies $(\ast_{n})$.
This defines a presheaf of `O_Y`-modules on $Y$, and one sees easily that it is a sheaf (more precisely, a subsheaf of
$\operatorname{Hom}_{p^{-1}_{Y}(O_{S})}(u^{-1} O_{X}, O_{Y})$).

### 1.2

<!-- label: III.VII_A.1.2 -->

Consider now two $S$-deviations $D = (u, d)$ and $E = (v, e)$:

```text
Z ─v,e→ Y ─u,d→ X.
```

When $U$ ranges over the opens of $X$, the composed maps

```text
Γ(U, O_X) ─d(U)→ Γ(u^{-1} U, O_Y) ─e(u^{-1} U)→ Γ(v^{-1} u^{-1} U, O_Z)
```

define an $S$-deviation of `uv` which we shall denote `de`; <!-- original page 414 --> when $d$ is of order $\leqslant
m$ and $e$ of order $\leqslant n$, `de` is of order $\leqslant m + n$. We shall also write

```text
(†)                              D ∘ E = (uv, de)
```

[^N.D.E-VII_A-5]

and we shall say that $D \circ E$ or `DE` is the *composed $S$-deviation*. When $d = u^{\natural}$ (i.e., $D = u$ with
the convention of 1.1), one also says that `DE` is the *image of $E$ by $u$*.

The map $(D, E) \mapsto D \circ E$ we have just defined will henceforth allow us to speak of the *category of
$S$-deviations*, whose objects are the $S$-schemes and whose morphisms are the $S$-deviations.[^N.D.E-VII_A-6]

**Definition 1.2.0.**[^N.D.E-VII_A-7] *Let $w : Z \to X$ be an $S$-morphism. An $S$-derivation of $w$, or $S$-derivation
of `O_X` into $w_{*}(O_{Z})$, is a morphism of $p^{-1}(O_{S})$-modules $d : O_{X} \to w_{*}(O_{Z})$ such that, for every
open $U$ of $X$ and $f, g \in O_{X}(U)$,*

<!-- label: III.VII_A.1.2.0 -->

```text
d(fg) = w^♮(f) d(g) + w^♮(g) d(f).
```

*Then $d$ is a deviation of $w$ of order $\leqslant 1$ which vanishes on the unit section of `O_X`. We denote by
$D\acute{e}r_{S}(w)$ the set of $S$-derivations of $w$; it is an $O(Z)$-module.*

With the notations of 1.2, take $Y$ equal to $I_{Z} = \operatorname{Spec} O_{Z}[t]$, where $t^{2} = 0$, and $v$ equal to
the zero section $\tau : Z \to I_{Z}$, defined by the morphism of `O_Z`-algebras $O_{Z}[t] \to O_{Z}$ sending $t$ to
`0`, and take $e$ equal to the morphism of `O_Z`-modules $\sigma : O_{Z}[t] \to O_{Z}$ defined by $\sigma(1) = 0$ and
$\sigma(t) = 1$,[^N.D.E-VII_A-8] which it is convenient to denote $\partial_{t}$.

If $u : I_{Z} \to X$ is a morphism satisfying $w = u \circ \tau$, then $\sigma \circ u^{\natural}$ is an $S$-derivation
of `O_X` into $w_{*}(O_{Z})$. Conversely, to every $S$-derivation $d$ we associate the morphism $u : I_{Z} \to X$ such
that $u = w$ on the underlying spaces, and

```text
u^♮(f) = w^♮(f) + d(f) t,
```

<!-- original page 446 -->

for every section $f$ of `O_X` on an open $U$. One thus obtains:

**Lemma 1.2.1.** *Let $E = (\tau, \partial_{t})$ be the deviation of $\tau : Z \to I_{Z}$ defined above. For every
$S$-morphism $w : Z \to X$, the map $u \mapsto u \circ E$ is a bijection between the $S$-morphisms $u : I_{Z} \to X$
such that $u \circ \tau = w$, and the $S$-derivations of $w$.*

<!-- label: III.VII_A.1.2.1 -->

### 1.2.2

<!-- label: III.VII_A.1.2.2 -->

Let $d$ be an $S$-deviation of $u : Y \to X$. On the one hand, $d$ is obviously an $S'$-deviation of $u$ for every
morphism $s : S \to S'$.

On the other hand, let $t : T \to S$ be a morphism with target $S$, and let $u_{T} : Y_{T} \to X_{T}$ be the morphism
deduced from $u$ by base change, and $t_{Y} : Y_{T} \to Y$ and $t_{X} : X_{T} \to X$ the canonical projections. Then
there exists one and only one $T$-deviation of $u_{T}$, which we shall denote $d_{T}$ or $d \times T$, satisfying the
equality $t_{X} d_{T} = d t_{Y}$, in the sense of `(†)` above, i.e., for every open $U$ of $X$, one has a commutative
diagram:[^N.D.E-VII_A-9]

```text
                 t_X^♮
   O(U)  ─────────────────→  O(U × T)

  d(U)                              d_T(U × T)

                 t_Y^♮
   O(u^{-1} U)  ────────→  O(u^{-1} U × T).
```

If one sets $D = (u, d)$, one will also write $D_{T} = (u_{T}, d_{T})$ and we shall say that $d_{T}$ and `D_T` are
deduced from $d$ and $D$ by base change.

### 1.2.3

<!-- label: III.VII_A.1.2.3 -->

<!-- original page 415 -->

For example, let $u : Y \to X$ and $v : Z \to T$ be two $S$-morphisms, $d$ and $e$ $S$-deviations of $u$ and $v$. One
has a commutative diagram

```text
            u_T
X × T  ←─────────  Y × T
  ↑                  ↑
v_X │  u×v        v_Y │
  │                  │
            u_Z
X × Z  ←─────────  Y × Z
```

and we shall denote by $d \times e$ (the *product* of $d$ and $e$) the $S$-deviation of $u \times v$ equal to $d_{T}
e_{Y} = e_{X} d_{Z}$ (with the convention `(†)` above), i.e., for every open $U$ of $X \times T$, if we denote

<!-- original page 447 --> by `W` the open `v_Y^{-1} u_T^{-1} U = u_Z^{-1} v_X^{-1} U`, one has a commutative diagram:

```text
                       d_T(U)
       O(U)  ──────────────────→  O(u_T^{-1} U)
         ╲                              ↑
   e_X(U) ╲    (d × e)(U)               │ e_Y(u_T^{-1} U)
           ╲                            │
                d_Z(v_X^{-1} U)
       O(v_X^{-1} U)  ────────────→  O(W).
```

If one sets $D = (u, d)$ and $E = (v, e)$, we shall also write $D \times E = (u \times v, d \times e)$.

### 1.3

<!-- label: III.VII_A.1.3 -->

[^N.D.E-VII_A-10] Let $u : Y \to X$ be a morphism of $S$-schemes. Recall that the adjunction isomorphism

```text
Hom_{p_X^{-1}(O_S)}(O_X, u_*(O_Y)) ⥲ Hom_{p_Y^{-1}(O_S)}(u^{-1}(O_X), O_Y)
```

associates with every morphism of $p^{-1}(O_{S})$-modules $d : O_{X} \to u_{*}(O_{Y})$ the morphism $d' = \epsilon \circ
u^{-1}(d)$, where $\epsilon$ is the canonical morphism $u^{-1} u_{*}(O_{Y}) \to O_{Y}$.

Let us write $J_{u}$ (resp. $I_{u}$) for the kernel of the algebra homomorphism $u^{\natural} : O_{X} \to u_{*}(O_{Y})$
(resp. $u^{\natural'} : u^{-1}(O_{X}) \to O_{Y}$), and let $d : O_{X} \to u_{*}(O_{Y})$ be a morphism of
$p^{-1}(O_{S})$-modules. If $U$ is an open of $X$ and $f_{0}, \cdots, f_{n}, g \in O_{X}(U)$, one sees easily by
induction on $n$ that the condition $(\ast_{n})$ is equivalent to the following equality (cf.
[EGA IV₄, 16.8.8.2](https://jcreinhold.github.io/ega/iv/29-ch4-16-differential-invariants.html#168-differential-operators1)):

<!-- label: III.VII_A.1.3.1 -->

```text
(∗∗_n)                     0 = ∑_{I ⊂ ⟦0,n⟧} (−1)^{|I|} u^♮(f_{⟦0,n⟧ − I}) d(f_I g),
```

where $f_{I}$ denotes the product of the $f_{i}$, for $i \in I$. It follows that if $d$ satisfies $(\ast_{n})$, then $d$
vanishes on the ideal $J^{n+1}_{u}$.

Suppose now $Y$ equal to $S$; then $u : S \to X$ is a section of $p : X \to S$, hence is an immersion (cf. [EGA I,
5.3.13](https://jcreinhold.github.io/ega/i/01-05-reduced-preschemes-and-separation.html#53-diagonal-graph-of-a-morphism)). Then, on the one hand, $\epsilon : u^{-1} u_{*} O_{S} \to O_{S}$ is an isomorphism, so that $u^{-1}(J_{u}) =
I_{u}$. On the other hand, one has an isomorphism:

$$ (\star) u^{-1}(O_{X}) \simeq O_{S} \oplus I_{u}. $$

Suppose that $d$ vanishes on $J^{n+1}_{u}$. Then $d' = \epsilon \circ u^{-1}(d)$ vanishes on $I^{n+1}_{u}$ and hence
$d'$ satisfies the analogues $(\ast\ast'_{n})$ and $(\ast'_{n})$ of $(\ast\ast_{n})$ and $(\ast_{n})$, when $f_{0},
\cdots, f_{n} \in I_{u}(u^{-1}(U))$. Moreover, since $(ad a)(\phi) = 0$ for every $a \in O_{S}(u^{-1}(U))$ and every
morphism of $O_{u^{-1}(U)}$-modules $\phi : u^{-1}(O_{U}) \to O_{u^{-1}(U)}$, one deduces from $(\star)$ that $d'$
satisfies the analogue $(\ast'_{n})$ of $(\ast_{n})$. It follows that $d$ satisfies $(\ast_{n})$. Consequently, one has
obtained:

**Lemma.** *If $u : S \to X$ is a section of $p : X \to S$, then $d$ is an $S$-deviation of $u$ of order $\leqslant n$
if and only if $d'$ vanishes on $I^{n+1}_{u}$.*

This interpretation may be generalized as follows. Let $u : Y \to X$ be an arbitrary $S$-morphism and $\Gamma_{u}$ the
graph of $u$, i.e., the morphism $Y \to Y \times X$ <!-- original page 448 --> with components $id_{Y}$ and $u$. For
every $S$-deviation $d$ of $u$ of order $\leqslant n$, one obtains by composition

```text
Y ──diag.→ Y × Y ──d_Y→ Y × X (over u_Y)
```

a $Y$-deviation of $\Gamma_{u}$ of order $\leqslant n$ which we shall denote $\Gamma_{d}$ (the graph of $d$).

Conversely, to every $Y$-deviation $e$ of $\Gamma_{u}$ one associates the composed $S$-deviation $e_{X} = pr_{2} \circ
e$:

```text
Y ──e→ Y × X ──pr₂→ X (over Γ_u).
```

One sees at once that $(\Gamma_{d})_{X} = d$, and the equality $\Gamma_{e_{X}} = e$ follows from the fact that $e$ is
`O_Y`- linear.[^N.D.E-VII_A-11] One thus obtains an isomorphism of $O_{Y}(Y)$-modules:

```text
{ S-deviations of u of order ⩽ n }  ⥲  { Y-deviations of Γ_u of order ⩽ n }
                                 d ↦ Γ_d.
```

Moreover, one sees easily that $d$ is an $S$-derivation of $u$ if and only if $\Gamma_{d}$ is a $Y$-derivation of
$\Gamma_{u}$.

<!-- original page 416 -->

Let us call $I_{\Gamma_{u}}$ the kernel of the algebra homomorphism $(\Gamma_{u})^{-1}(O_{Y \times X}) \to O_{Y}$
corresponding to $\Gamma_{u}$. Taking into account the preceding lemma, one has obtained:

**Proposition.** *Let $u : Y \to X$ be an $S$-morphism and $\Gamma_{u} : Y \to Y \times X$ its graph. The $S$-deviations
of $u$ of order $\leqslant n$ are identified with the $Y$-deviations of $\Gamma_{u}$ of order $\leqslant n$, which are
in bijection with*

```text
Hom_{O_Y}((Γ_u)^{-1}(O_{Y × X}) / I_{Γ_u}^{n+1}, O_Y).
```

### 1.3.1

<!-- label: III.VII_A.1.3.1 -->

[^N.D.E-VII_A-12] Let us return to the case where $u : S \to X$ is a section of $p : X \to S$. Then the homomorphism
$\phi : u^{-1}(O_{X}) \to O_{S}$ admits a section, which we shall denote simply $g \mapsto g \cdot 1$, so that, with the
notations of 1.3, one has an isomorphism of `O_S`-modules:

$$ (\star) u^{-1}(O_{X}) \simeq O_{S} \oplus I_{u}, $$

and for every section $f$ of $u^{-1}(O_{X})$, $f - \phi(f) \cdot 1$ is a section of $I_{u}$.

Let $d$ be an $S$-deviation of $u$ of order $\leqslant 1$, and $d'$ the `O_S`-morphism $u^{-1}(O_{X}) \to O_{S}$
corresponding to $d$. If `a, b` are sections of $u^{-1}(O_{X})$, one has:

```text
0 = d'((a − φ(a) · 1)(b − φ(b) · 1)) = d'(ab) − φ(a) d'(b) − φ(b) d'(a) + φ(ab) d'(1).
```

Consequently, one sees that $d$ is an $S$-derivation of $u$ (cf. 1.2.1 and N.D.E. (2)) if and only if $d'(1) = 0$. One
thus obtains:

<!-- original page 449 -->

**Lemma.** *The $S$-derivations of $u$ are exactly the $S$-deviations of $u$ of order `1` which vanish on the unit
section of `O_X`; they correspond to the $O_{S}(S)$-module*

$$ \operatorname{Hom}_{O_{S}}(I_{u} / I^{2}_{u}, O_{S}), $$

*and one has an isomorphism of $O_{S}(S)$-modules $D\acute{e}v_{\leqslant 1}(u) \simeq O_{S}(S) \oplus
D\acute{e}r_{S}(u)$.*

Returning to the general case, one deduces, with the notations of 1.3,

**Corollary.** *Let $u : Y \to X$ be an $S$-morphism and $\Gamma_{u} : Y \to Y \times X$ its graph. One has a canonical
isomorphism of $O_{Y}(Y)$-modules*

```text
Dér_S(u) ≃ Dér_Y(Γ_u) ≃ Hom_{O_Y}(I_{Γ_u} / I_{Γ_u}², O_Y).
```

### Definition 1.4

<!-- label: III.VII_A.1.4 -->

*Let $X$ be an $S$-scheme. We call $S$-differential operator (resp. $S$-differential operator of order $\leqslant n$) on
$X$ any $S$-deviation (resp. any $S$-deviation of order $\leqslant n$) of the identity morphism of $X$.*

According to 1.1, an $S$-differential operator of order $\leqslant n$ is therefore an endomorphism of
$p^{-1}(O_{S})$-module of `O_X` which satisfies the equalities $(\ast_{n})$ of 1.1. We shall denote by $Dif^{n}_{X/S}$
the $\Gamma(O_{S})$-module [^N.D.E-VII_A-13] formed by the $S$-differential operators of order $\leqslant n$, and by
$Dif_{X/S}$ that formed by all the $S$-differential operators.

As we saw in 1.2, one can compose $S$-deviations of $id_{X}$, which equips $Dif_{X/S}$ with a structure of
$\Gamma(O_{S})$-algebra; we shall say that this is the *algebra of differential operators of $X / S$*.

Similarly, for every open $V$ of $X$, set $\mathcal{D}if_{X/S}(V) = Dif_{V/S} = D\acute{e}v(id_{V})$; according to
1.1.3, this defines a sheaf of `O_X`-modules, called the *sheaf of $S$-differential operators on $X$*.[^N.D.E-VII_A-14]

### 1.4.1

<!-- label: III.VII_A.1.4.1 -->

As we saw in 1.3, one can interpret the differential operators of $X / S$ by means of the graph of the identity morphism
of $X$, i.e., of the diagonal morphism `∆ = ∆_{X/S}` of $X$ into $X \times X$. Let us translate into the present context
the statements of 1.3.

Endow $O_{X \times X}$ with the $pr^{-1}_{1}(O_{X})$-algebra structure defined by $pr_{1}$, so that `∆^{-1}(O_{X × X})`
is equipped with a structure of algebra over `O_X = ∆^{-1} pr₁^{-1}(O_X)`. Let $I_{X/S}$ be the kernel of the
homomorphism

```text
∆^{-1}(O_{X × X}) ──m→ O_X
```

adjoint to the homomorphism `O_{X × X} → ∆_*(O_X)`, and let $P^{m}_{X/S}$ be the `O_X`-algebra

```text
∆^{-1}(O_{X × X}) / I_{X/S}^{m+1}.
```

If $V$ is an affine open of $S$ and $U$ an affine open of $X$ above $V$, and if one sets

<!-- original page 417 --> `k = Γ(V, O_S)` and `A = Γ(U, O_X)`, one has therefore:

```text
Γ(U, P^m_{X/S}) = (A ⊗_k A) / I^{m+1},
```

<!-- original page 450 -->

where $I$ is the ideal generated by the elements $a \otimes 1 - 1 \otimes a$, for $a \in A$. This being so, one has
according to 1.3 an isomorphism of $O_{X}(X)$-modules:

```text
j_X : Dif^m_{X/S} ⥲ Hom_{O_X}(P^m_{X/S}, O_X)
```

which one can define as follows: if $d$ belongs to $Dif^{m}_{X/S}$ and if $c$ is a section of $P^{m}_{X/S}$ on $U$ of
the form $a \otimes b + I^{m+1}$, one has $j_{X}(d)(c) = a \cdot d(b)$.[^N.D.E-VII_A-15]

### 1.4.2

<!-- label: III.VII_A.1.4.2 -->

Let $d$ be a differential operator and $u$ a section of $X$ over $S$. We call *value of $d$ at $u$* the composed
$S$-deviation

```text
S ──u→ X ──d→ X (over id_X).
```

According to 1.3 and 1.4.1, if $d$ is a differential operator of order $\leqslant m$, then `du` (resp. $d$) is
canonically associated with a morphism of `O_S`-modules $d' : u^{-1}(O_{X}) / I^{m+1}_{u} \to O_{S}$ (resp. a morphism
of `O_X`-modules $d'' : P^{m}_{X/S} \to O_{X}$).

It is clear that one can construct $d'$ from `d''` as follows: the square

```text
                 u × X
   X ≃ S ×_X X  ──────→  X × X
       │                   │
       p                   pr₁
       │           u       │
       ▼                   ▼
       S          ───────→ X
```

is cartesian, which allows us to identify $X$ with $S \times_{X} (X \times X)$, $u$ with `S ×_X ∆`, hence
$u^{*}(P^{m}_{X/S})$ with $u^{-1}(O_{X}) / I^{m+1}_{u}$. One thus identifies $u^{*}(d'')$ with a morphism $u^{-1}(O_{X})
/ I^{m+1}_{u} \to O_{S}$, which is none other than $d'$.

### 1.5

<!-- label: III.VII_A.1.5 -->

<!-- original page 418 -->

Set as usual $I_{S} = \operatorname{Spec} O_{S}[T] / (T^{2})$. Let $\tau : S \to I_{S}$ be the zero section and $\sigma$
the canonical deviation of $\tau$ which we defined in 1.2.0, i.e. the homomorphism of `O_S`-modules which vanishes on
the unit section of $O_{S}[T]/(T^{2})$ and which sends the class $t$ of $T$ modulo $T^{2}$ to the unit section of `O_S`.

Let $X$ be an $S$-scheme. To every `I_S`-automorphism $u$ of $I_{S} \times X$ inducing the identity on $X$ there is
associated by composition a differential operator $D_{u}$ of $X$:

```text
X ≃ S × X ──σ × X→ I_S × X ──u→ I_S × X ──pr₂→ X.
```

According to II, 3.14, the map $u \mapsto D_{u}$ is an isomorphism of the $\Gamma(O_{S})$-Lie algebra

```text
Lie(Aut X) := Lie(Aut X)(S)
```

onto the $\Gamma(O_{S})$-Lie algebra of $p^{-1}(O_{S})$-derivations of `O_X`. The inverse isomorphism associates with
every derivation $D$ the automorphism of $I_{S} \times X$ corresponding to the automorphism $a + bt \mapsto a + (Da +
b)t$ of $O_{X}[T]/(T^{2})$.

## 2. Invariant differential operators on group schemes

<!-- label: III.VII_A.2 -->

### 2.1

<!-- label: III.VII_A.2.1 -->

<!-- original page 419 -->

Let $G$ be an $S$-group scheme; we denote by $\epsilon$ or $\epsilon_{G} : S \to G$ the unit section of $G$.

**Definition.** *Let $U(G)$ be the $\Gamma(O_{S})$-module of $S$-deviations of $\epsilon_{G}$ (or $S$-deviations of the
origin) (cf. 1.1).*

*If $d$ and $e$ are two elements of $U(G)$, $d \times e$ is an $S$-deviation of $\epsilon \times \epsilon : S \simeq S
\times S \to G \times G$. The image of $d \times e$ by the multiplication morphism $m : G \times G \to G$ (cf. 1.2) will
be called the product of $d$ and $e$ and will be denoted $d \cdot e$.*

*The $\Gamma(O_{S})$-module $U(G)$ is thus equipped with a structure of associative $\Gamma(O_{S})$-algebra having
$\epsilon_{G}$ as unit element (1.1). We shall say that $U(G)$ is the* infinitesimal algebra *of $G$.*[^N.D.E-VII_A-16]

When $T$ ranges over the schemes above $S$, the infinitesimal algebra $U(G_{T})$ of the $T$-group $G \times T$ obviously
varies contravariantly in $T$, so that we may speak of the *infinitesimal algebra functor*.

When $T$ ranges over the opens of $S$, one therefore obtains a presheaf $T \mapsto U(G_{T})$ of `O_S`-algebras;
moreover, according to 1.1.3, this is a sheaf. We shall denote it $\mathcal{U}(G)$ and we shall call it the *sheaf of
infinitesimal algebras of $G$*.

The algebra $U(G)$ is also a covariant functor in $G$. Indeed, if $u : G \to H$ is a homomorphism of $S$-groups and $d$
an $S$-deviation of $\epsilon_{G}$, the image of $d$ by $u$ is an element $U(u)(d) = ud$ of $U(H)$. The map $U(u) : U(G)
\to U(H)$ thus defined is obviously a homomorphism of $\Gamma(O_{S})$-algebras. One defines similarly a homomorphism
$\mathcal{U}(u)$ from $\mathcal{U}(G)$ to $\mathcal{U}(H)$.

### 2.2

<!-- label: III.VII_A.2.2 -->

Let $d$ be an element of $U(G)$, i.e., an $S$-deviation of the origin of $G$. Consider the $S$-deviation $d \times G$ of
$\epsilon \times G : G \simeq S \times G \to G \times G$ obtained from $d$ by base change (1.2.2); the image of $d
\times G$ by the multiplication morphism $m : G \times G \to G$ is an $S$-deviation of $m \circ (\epsilon \times id_{G})
= id_{G}$, i.e., an element of $Dif_{G/S}$, which we shall denote $d_{G}$.

The map $d \mapsto d_{G}$ is obviously $\Gamma(O_{S})$-linear and the "commutative" diagram below shows that one has $(e
\cdot d)_{G} = d_{G} \cdot e_{G}$:[^N.D.E-VII_A-17] <!-- original page 420 -->

```text
                                 m × G
   G × G × G  ─────────────────────────────→  G × G
       △                                       △
       │ G × d × G                              │ G × m
       │ ε × G × G                              │

  G × G                              G × G                     m
   △  △                              △  △
   │  │ e × G   m                   │  │ d × G   m
   │  │ ε × G                       │  │ ε × G
   │                                │
   │           e_G                  │           d_G
   G  ─────────────→  G  ─────────────→  G       (over id_G everywhere).
```

The commutativity of the two bottom triangles follows from the definition of $d_{G}$ and $e_{G}$; on the other hand, the
composed $S$-deviation of $e \times G$ and $G \times d \times G$ is $(e \times d) \times G$ (cf. 1.2.2), its image by $m
\times G$ is $(e \cdot d) \times G$, and the image of the latter by $m$ is therefore equal to $(e \cdot d)_{G}$.

One thus obtains an anti-homomorphism $U(G) \to Dif_{G/S}$ of $\Gamma(O_{S})$-algebras, called *right
translation*.[^N.D.E-VII_A-18]

If $\mathcal{D}if_{G/S}$ denotes the sheaf of $S$-differential operators on $G$ (cf. 1.4) and $p$ the structural
morphism $G \to S$, one defines similarly a "right translation": $\mathcal{U}(G) \to p_{*}(\mathcal{D}if_{G/S})$.

### 2.3

<!-- label: III.VII_A.2.3 -->

We shall now characterize the differential operators of $G$ over $S$ of the form $d_{G}$. Let $g : S \to G$ be a section
of the structural morphism of $G$ and $g_{G}$ the right translation of $G$ by $g$, i.e., the composed morphism:

```text
g_G : G ≃ G × S ──G × g→ G × G ──m→ G.
```

For every differential operator $D$ of $G$ over $S$, the composition $g^{-1}_{G} D g_{G}$ (cf. 1.2) is again an
$S$-deviation of $id_{G}$, i.e., an element of $Dif_{X/S}$; we shall denote:

```text
D^g = g_G^{-1} D g_G.
```

We shall say that $D$ is *right-invariant* if, for every base change $t : T \to S$ and every section $g : T \to G \times
T$, one has $(D_{T})^{g} = D_{T}$.

**Lemma.** *For every differential operator $D$ of $G$ over $S$, the following assertions are equivalent (where $m$ is
the multiplication morphism of $G$):*

<!-- original page 421 -->

*(i) $D$ is right-invariant.*

*(ii) The two following deviations of $m$ are equal: $D m = m(D \times G)$.*

(ii) ⇒ (i): since the condition (ii) is stable under base change, it suffices to show that (ii) entails the equality
$D^{g} = D$ for every section $g : S \to G$. Let $h$ be the morphism $G \times g : G \simeq G \times S \to G \times G$,
so that $m \circ h$ is the right translation $g_{G}$. The equality $D^{g} = D$ is equivalent to the equality $g_{G}
\circ D = D \circ g_{G}$, and this follows from the commutative diagram:

```text
                    m                     h
       G  ←──────────  G × G  ←──────────  G

   D, id_G        D × G, id_{G × G}      D, id_G

                    m                     h
       G  ←──────────  G × G  ←──────────  G.
```

(i) ⇒ (ii): take indeed for $t : T \to S$ the structural morphism $p : G \to S$, for section $g : T \to G \times T$ the
diagonal morphism `∆ : G → G × G`. The right translation

```text
∆_{G × G} : G × G  ⟶  G × G
```

is then the morphism from $G \times G$ into $G \times G$ with components $m$ and $pr_{2}$. The equality `(D_G)^∆ = D_G`
is then equivalent to the commutativity of the first square of the following diagram:

```text
                  ∆_{G × G}                  pr₁
       G × G  ──────────────→  G × G  ──────────→  G

   D_G, id_{G × G}          D_G, id_{G × G}    D, id_G

                  ∆_{G × G}                  pr₁
       G × G  ──────────────→  G × G  ──────────→  G.
```

The equality (ii) thus follows from the fact that `m = pr₁ ∘ ∆_{G × G}`.

<!-- original page 422 -->

Consider for example an element $d$ of the infinitesimal algebra $U(G)$. The squares of the diagram

```text
                          d × G × G                            m × G
       G × G  ←────  S × G × G  ──────────────→  G × G × G  ──────────→  G × G
                          ε × G × G

         m                    S × m                  G × m                  m

                          d × G                                m
         G  ←────  S × G  ──────────────→  G × G  ──────────→  G
                          ε × G
```

are then commutative. Since one has

```text
m ∘ (d × G) = d_G    and    (m × G) ∘ (d × G × G) = d_G × G,
```

one also has $d_{G} \circ m = m \circ (d_{G} \times G)$. Therefore: *for every $S$-deviation $d$ of the origin, $d_{G}$
is a right-invariant differential operator*.

### 2.4. Theorem

<!-- label: III.VII_A.2.4 -->

*(i) The map $d \mapsto d_{G}$ is an anti-isomorphism[^N.D.E-VII_A-19] of the infinitesimal algebra $U(G)$ onto the
subalgebra $Dif^{G}_{G/S}$ of $Dif_{G/S}$ formed by the right-invariant differential operators.*

*(ii) Similarly, the map $d \mapsto {}_{G} d$ is an isomorphism of $U(G)$ onto the subalgebra of $Dif_{G/S}$ formed by
the left-invariant differential operators.*

Let in fact $D$ be an arbitrary differential operator of $G$ over $S$ and let us denote by `D_0` its value at the
origin, i.e., the composed deviation $S \xrightarrow{\epsilon} G \xrightarrow{D} G$ (over $id_{G}$). The right-invariant
differential operator $(D_{0})_{G}$ is then obtained by composition:

```text
G ≃ S × G ──ε × G→ G × G ──D × G→ G × G ──m→ G (over id_{G × G}).
```

If $D$ is right-invariant, one has $D m = m(D \times G)$, whence

```text
D = D m(ε × G) = m(D × G)(ε × G) = (D_0)_G.
```

In particular, the map $d \mapsto d_{G}$ is surjective.

Conversely, let $d$ be an $S$-deviation of the origin. One then has a commutative square

```text
                          d × G
       G × G  ←──────────  G
         △                  △
   G × ε │                  │ ε
                       d
       G × S ≃ G  ←──────  S
```

<!-- original page 423 -->

whence it follows that $d = m(G \times \epsilon) d = m(d \times G) \epsilon = (d_{G})_{0}$. *A fortiori*, the map $d
\mapsto d_{G}$ is injective. This proves the theorem.

When $S$ varies, Theorem 2.4 obviously implies that the right translation $\mathcal{U}(G) \to
p_{*}(\mathcal{D}if_{G/S})$ is an anti-isomorphism of `O_S`-algebras of $\mathcal{U}(G)$ onto the sheaf of
`O_S`-algebras $p_{*}(\mathcal{D}if_{G/S})^{G}$, which to every open $U$ of $S$ associates $Dif^{G_{U}}_{G_{U} / U}$.

### 2.4.1. Remark

<!-- label: III.VII_A.2.4.1 -->

Consider the commutative diagram

```text
                       η
        G  ←──────────  G × G
        △               △    △
     p  │   ε        pr₁ │    │ ∆
        │       p        │
        S  ←──────────  G,
```

where $\eta$ denotes the morphism "$(x, y) \mapsto y x^{-1}$".[^N.D.E-VII_A-20] The latter induces morphisms

```text
η' : η^{-1}(O_G) ⟶ O_{G × G}    and    ∆^{-1}(η') : p^{-1} ε^{-1}(O_G) ⟶ ∆^{-1}(O_{G × G}).
```

For every integer $n \geqslant 1$, set $p^{n}_{G/S} = \epsilon^{-1}(O_{G}) / I^{n+1}_{\epsilon}$ (cf. 1.3 and 1.4 for
the notations).[^N.D.E-VII_A-21] Since the square formed by the morphisms $\epsilon$, $\eta$, `∆` and $p$ is cartesian,
`∆^{-1}(η')` induces an isomorphism of `O_G`-modules:

$$ p^{*}(p^{n}_{G/S}) \xrightarrow{\sim} P^{n}_{G/S}. $$

The differential operators of $G$ over $S$ of order $\leqslant n$ therefore correspond bijectively to the morphisms of
`O_G`-modules $p^{*}(p^{n}_{G/S}) \longrightarrow O_{G}$, i.e., to the morphisms <!-- original page 424 --> of
`O_S`-modules

$$ p^{n}_{G/S} \longrightarrow p_{*}(O_{G}). $$

In this bijection, the right-invariant differential operators correspond to the composed arrows

```text
p^n_{G/S} ──→ O_S ──can.→ p_*(O_G).
```

One thus recovers the isomorphism of Theorem 2.4.

### 2.5

<!-- label: III.VII_A.2.5 -->

[^N.D.E-VII_A-22] Let $Lie(G)$ be the Lie algebra of $G$;[^N.D.E-VII_A-23] we shall define a morphism of
$\Gamma(O_{S})$-Lie algebras $\alpha : Lie(G) \to U(G)$.

Let $s : S \to I_{S}$ be the zero section of $I_{S} \to S$ and $\sigma$ the deviation of $s$ defined in 1.2.0. Recall
(cf. II, 4.1) that $Lie(G)$ is the set of morphisms $x : I_{S} \to G$ such that $x \circ s = \epsilon_{G}$. Then the
composition

```text
S ──σ→ I_S ──x→ G (over s)
```

is an $S$-deviation of $\epsilon_{G}$, i.e., an element of $U(G)$; with the notations of 1.2 `(†)`, it is denoted
$\sigma x$. Moreover, according to 1.2.1, the map $\alpha : x \mapsto \sigma x$ is an isomorphism of $O_{S}(S)$-modules
from $Lie(G)$ onto the submodule $D\acute{e}r(\epsilon_{G})$ of $U(G)$ formed by the $S$-derivations of $\epsilon_{G}$.
We shall see that $\alpha$ is a morphism of Lie algebras.[^N.D.E-VII_A-24] Let

$$ \rho' : U(G) \longrightarrow Dif_{G/S} $$

be the algebra morphism which to an $S$-deviation $d$ of $\epsilon_{G}$ associates the left-invariant differential
operator ${}_{G} d \in Dif_{G/S}$, cf. 2.2, N.D.E. (17).

Let $\rho : G \to \operatorname{Aut}_{S}(G)$ be the homomorphism of group functors which to an $S$-morphism $g : T \to
G$ associates the right translation of `G_T` by $g$, i.e. the morphism:

```text
G_T ≃ T ×_T G_T ──G_T × g→ G_T ×_T G_T ──m_T→ G_T.
```

Recall also (cf. 1.5 and II, 3.14) that `Lie(Aut G) = Lie(Aut_S(G)/S)(S)` is identified with the infinitesimal
automorphisms of $G$, i.e., with the automorphisms of $I_{S} \times G$ inducing the identity on $G$.

<!-- original page 456 -->

Since $\rho$ is a monomorphism, the same holds for the morphism `Lie(ρ) : Lie(G/S) → Lie(Aut_S(G)/S)` (see, for example,
Exp. II, N.D.E. (50)), hence `Lie(ρ) : Lie(G) → Lie(Aut G)` is injective.

On the other hand, according to 1.5, the map $\beta$ which to every infinitesimal automorphism $u$ of $G$ associates the
differential operator $D_{u}$ of $G$:

```text
G ≃ S × G ──σ × G→ I_S × G ──u→ I_S × G ──pr₂→ G
```

is an isomorphism of $Lie(\operatorname{Aut} G)$ onto the Lie subalgebra of $Dif_{G/S}$ formed by the
$p^{-1}(O_{S})$-derivations of `O_G`.

For every $x \in Lie(G)$, one has the commutative square below which determines the image of $x$ by $Lie(\rho)$:

```text
                       Lie(ρ)(x)
       I_S × G  ───────────────→  I_S × G

   x × G                                pr₂
                          m
       G × G  ──────────────────→  G.
```

<!-- original page 425 -->

Taking this diagram into account, the image of $Lie(\rho)(x)$ by $\beta$ is the composed deviation

```text
G ≃ S × G ──σ × G→ I_S × G ──G × x→ G × G ──m→ G (over s × G)
```

which, according to 2.2 N.D.E. (17), is none other than ${}_{G}(\sigma x) = \rho'(\alpha(x))$. One thus obtains a
commutative diagram:

```text
                       Lie(ρ)
       Lie(G)  ─────────────────→  Lie(Aut G)
          │                              │
        α │                              │ β
          │              ρ'              │
          ▼                              ▼
       U(G)  ──────────────────────────→  Dif_{G/S}
```

where $Lie(\rho)$, $\beta$ and $\rho'$ are morphisms of Lie algebras. Since $\rho'$ is injective, it follows that
$\alpha$ is also a morphism of Lie algebras. Consequently, one has obtained:

**Proposition.** *$\alpha$ is an isomorphism of $O_{S}(S)$-Lie algebras, from $Lie(G)$ into the Lie algebra of
$S$-derivations of $\epsilon_{G}$, itself isomorphic via $Lie(\rho)$ to the Lie algebra of $S$-derivations of $G$
invariant under left translation.*[^N.D.E-VII_A-25]

## 3. Coalgebras and Cartier duality

<!-- label: III.VII_A.3 -->

### 3.1

<!-- label: III.VII_A.3.1 -->

<!-- original page 426 -->

Let $S$ be a scheme (or, more generally, a ringed space). An *`O_S`-coalgebra*[^N.D.E-VII_A-26] is a pair `(𝒰, ∆_𝒰)`
consisting of an `O_S`-module $\mathcal{U}$ and a morphism of `O_S`-modules `∆_𝒰 : 𝒰 → 𝒰 ⊗_{O_S} 𝒰` (called the
*diagonal morphism* or *comultiplication*) such that:

(i) `σ ∘ ∆_𝒰 = ∆_𝒰`, where $\sigma(a \otimes b) = b \otimes a$.

(ii) The square

```text
                              ∆_𝒰
       𝒰  ──────────────────────→  𝒰 ⊗_{O_S} 𝒰

   ∆_𝒰                                    id_𝒰 ⊗ ∆_𝒰

                          ∆_𝒰 ⊗ id_𝒰
       𝒰 ⊗_{O_S} 𝒰  ──────────────────→  𝒰 ⊗_{O_S} 𝒰 ⊗_{O_S} 𝒰
```

is commutative.

(iii) There exists a morphism of `O_S`-modules $\epsilon_{\mathcal{U}} : \mathcal{U} \to O_{S}$, called the
*augmentation*, such that the composed morphisms

```text
𝒰 ──∆_𝒰→ 𝒰 ⊗_{O_S} 𝒰 ──id_𝒰 ⊗ ε_𝒰→ 𝒰 ⊗_{O_S} O_S ≃ 𝒰
𝒰 ──∆_𝒰→ 𝒰 ⊗_{O_S} 𝒰 ──ε_𝒰 ⊗ id_𝒰→ O_S ⊗_{O_S} 𝒰 ≃ 𝒰
```

are the identity morphism of $\mathcal{U}$.

If $\epsilon_{\mathcal{U}}$ and $\epsilon'_{\mathcal{U}}$ are two augmentations, one has
`ε_𝒰 = (ε_𝒰 ⊗ ε'_𝒰) ∘ ∆_𝒰 = ε'_𝒰`; the augmentation is therefore uniquely determined by (iii).

If `(𝒰, ∆_𝒰)` and `(𝒱, ∆_𝒱)` are two `O_S`-coalgebras, a *morphism* from the first into the second is a morphism of
`O_S`-modules $f : \mathcal{U} \to \mathcal{V}$ such that the diagrams

```text
        f                              f
   𝒰  ────→  𝒱                    𝒰  ────→  𝒱
   │          │                    │          │
 ∆_𝒰         ∆_𝒱      and        ε_𝒰        ε_𝒱
   ▼          ▼                    │          │
                                   ▼          ▼
   𝒰 ⊗ 𝒰  ─f ⊗ f→  𝒱 ⊗ 𝒱                  O_S
```

are commutative. Morphisms of coalgebras compose like morphisms of `O_S`-modules, so that we shall be able to speak of
the *category of `O_S`-coalgebras*.

<!-- original page 427 -->

### 3.1.0

<!-- label: III.VII_A.3.1.0 -->

[^N.D.E-VII_A-27] This category has finite products: the final object is the `O_S`-module `O_S`, the comultiplication
being the identity; the product of two coalgebras `(𝒰, ∆_𝒰)` and `(𝒱, ∆_𝒱)` is the tensor product $\mathcal{U}
\otimes_{O_{S}} \mathcal{V}$, the comultiplication being the composed morphism

```text
𝒰 ⊗ 𝒱 ──∆_𝒰 ⊗ ∆_𝒱→ 𝒰 ⊗ 𝒰 ⊗ 𝒱 ⊗ 𝒱 ──id_𝒰 ⊗ σ ⊗ id_𝒱→ 𝒰 ⊗ 𝒱 ⊗ 𝒰 ⊗ 𝒱
```

where $\sigma(a \otimes b) = b \otimes a$; the canonical projections of $\mathcal{U} \otimes \mathcal{V}$ onto the
factors $\mathcal{U}$ and $\mathcal{V}$ are the morphisms $id_{\mathcal{U}} \otimes \epsilon_{\mathcal{V}}$ and
$\epsilon_{\mathcal{U}} \otimes id_{\mathcal{V}}$,[^N.D.E-VII_A-28] and the "diagonal morphism" $\mathcal{U} \to
\mathcal{U} \otimes \mathcal{U}$ (corresponding to the pair of morphisms $(id_{\mathcal{U}}, id_{\mathcal{U}})$) is none
other than the comultiplication `∆_𝒰`.

### 3.1.1

<!-- label: III.VII_A.3.1.1 -->

Let $\mathcal{A}$ be a commutative `O_S`-algebra, locally free and of finite type as an `O_S`-module. If we set

$$ \mathcal{A}^{*} = \operatorname{Hom}_{O_{S}-Mod.}(\mathcal{A}, O_{S}), $$

the canonical morphism $\phi$ from $\mathcal{A}^{*} \otimes_{O_{S}} \mathcal{A}^{*}$ into $(\mathcal{A} \otimes_{O_{S}}
\mathcal{A})^{*}$ is invertible. If $m : \mathcal{A} \otimes \mathcal{A} \to \mathcal{A}$ is the morphism defining the
multiplication of $\mathcal{A}$, one obtains by composition a diagonal morphism

```text
∆_{𝒜^*} : 𝒜^* ──m^*→ (𝒜 ⊗ 𝒜)^* ──φ^{-1}→ 𝒜^* ⊗ 𝒜^*.
```

This diagonal morphism obviously makes $\mathcal{A}^{*}$ an `O_S`-coalgebra whose augmentation is the

<!-- original page 428 --> transpose morphism of the morphism `O_S → 𝒜` defined by the unit section of `𝒜`. Moreover,

it is clear that:

*The functor $\mathcal{A} \mapsto \mathcal{A}^{*}$ is an anti-equivalence of the category of `O_S`-algebras which are
locally free and of finite type as `O_S`-modules, onto the category of `O_S`-coalgebras locally free and of finite type
as `O_S`-modules.*

### 3.1.2

<!-- label: III.VII_A.3.1.2 -->

To every `O_S`-coalgebra $\mathcal{U}$ is canonically associated an $S$-functor

```text
Spec^* 𝒰 : (Sch/S)° ⟶ (Ens).
```

Note indeed that, for every $S$-scheme $q : T \to S$, $q^{*}(\mathcal{U} \otimes_{O_{S}} \mathcal{U})$ is identified
with $q^{*}(\mathcal{U}) \otimes_{O_{T}} q^{*}(\mathcal{U})$, so that `q^*(∆_𝒰)` makes $\mathcal{U}_{T} =
q^{*}(\mathcal{U})$ into an `O_T`-coalgebra; we can therefore set by definition and with an obvious abuse of
notation:[^N.D.E-VII_A-29]

```text
(Spec^* 𝒰)(T) = { x ∈ Γ(T, 𝒰_T) | ε_{𝒰_T}(x) = 1 and ∆_{𝒰_T}(x) = x ⊗ x }.
```

<!-- original page 458 -->

The sections $x$ of $\mathcal{U}_{T}$ obviously correspond to the morphisms of `O_T`-modules $\xi : O_{T} \to
\mathcal{U}_{T}$; the conditions $\epsilon(x) = 1$ and `∆(x) = x ⊗ x` simply express that $\xi$ is a morphism of
coalgebras. One therefore also has:

```text
(Spec^* 𝒰)(T) = Hom_{O_T-coalg.}(O_T, 𝒰_T).
```

In particular, one has the following proposition:[^N.D.E-VII_A-30]

**Proposition 3.1.2.1.** *Let $\mathcal{A}$ be a commutative `O_S`-algebra which is locally free of finite type as an
`O_S`-module. Then the $S$-functor $\operatorname{Spec}^{*} \mathcal{A}^{*}$ is represented by $\operatorname{Spec}
\mathcal{A}$.*

<!-- label: III.VII_A.3.1.2.1 -->

Indeed, for every $S$-scheme $T$, one has canonical isomorphisms:

```text
(Spec^* 𝒜^*)(T) = Hom_{O_T-coalg.}(O_T, 𝒜_T^*) ≃ Hom_{O_T-alg.}(𝒜_T, O_T) ≃ (Spec 𝒜)(T).
```

### 3.2

<!-- label: III.VII_A.3.2 -->

An `O_S`-*coalgebra in groups* (i.e., a group in the category of `O_S`-coalgebras) consists of the data of an
`O_S`-coalgebra `(𝒰, ∆_𝒰)` and three morphisms of `O_S`-coalgebras $m_{\mathcal{U}} : \mathcal{U} \otimes \mathcal{U}
\to \mathcal{U}$, $\eta_{\mathcal{U}} : O_{S} \to \mathcal{U}$ and $c_{\mathcal{U}} : \mathcal{U} \to \mathcal{U}$
satisfying the conditions (ii)*, (iii)* and (vi) below; on the other hand, the fact that $m_{\mathcal{U}}$ is a morphism
of cogebras translates into the commutativity of diagrams (iv) and (v)

<!-- original page 429 --> below:

```text
                              m_𝒰
       𝒰 ⊗ 𝒰  ────────────────────→  𝒰

   ∆_𝒰 ⊗ ∆_𝒰
       │
(iv)   ▼                                  ∆_𝒰
   𝒰 ⊗ 𝒰 ⊗ 𝒰 ⊗ 𝒰

   id_𝒰 ⊗ σ ⊗ id_𝒰
                              m_𝒰 ⊗ m_𝒰
   𝒰 ⊗ 𝒰 ⊗ 𝒰 ⊗ 𝒰  ──────────────────→  𝒰 ⊗ 𝒰
```

```text
                              m_𝒰
       𝒰 ⊗ 𝒰  ────────────────────→  𝒰
              ╲                    ╱
(v)            ╲                  ╱
        ε_𝒰 ⊗ ε_𝒰              ε_𝒰
                  ╲          ╱
                       O_S
```

(ii)\* The square

```text
                              id_𝒰 ⊗ m_𝒰
       𝒰 ⊗ 𝒰 ⊗ 𝒰  ──────────────────→  𝒰 ⊗ 𝒰

   m_𝒰 ⊗ id_𝒰                                 m_𝒰

                              m_𝒰
       𝒰 ⊗ 𝒰  ────────────────────→  𝒰
```

is commutative.

(iii)\* The two compositions below equal the identity morphism of $\mathcal{U}$:

```text
𝒰 ≃ 𝒰 ⊗ O_S ──id_𝒰 ⊗ η_𝒰→ 𝒰 ⊗ 𝒰 ──m_𝒰→ 𝒰
𝒰 ≃ O_S ⊗ 𝒰 ──η_𝒰 ⊗ id_𝒰→ 𝒰 ⊗ 𝒰 ──m_𝒰→ 𝒰.
```

(vi) The composed morphism below is equal to $\eta_{\mathcal{U}} \circ \epsilon_{\mathcal{U}}$:

<!-- original page 430 -->

```text
𝒰 ──∆_𝒰→ 𝒰 ⊗ 𝒰 ──c_𝒰 ⊗ id_𝒰→ 𝒰 ⊗ 𝒰 ──m_𝒰→ 𝒰.
```

### 3.2.1

<!-- label: III.VII_A.3.2.1 -->

The morphisms $\eta_{\mathcal{U}}$ and $c_{\mathcal{U}}$ are uniquely determined by $m_{\mathcal{U}}$. On the other
hand, conditions (ii)\* and (iii)\* simply express that $m_{\mathcal{U}}$ makes $\mathcal{U}$ an `O_S`-algebra having as
unit section the image by $\eta_{\mathcal{U}}$ of the unit section of `O_S`. Condition (iv) also expresses that the
diagonal morphism `∆_𝒰` is compatible with multiplication; and indeed, `∆_𝒰 : 𝒰 → 𝒰 ⊗ 𝒰` must be a homomorphism of group
coalgebras, which also entails the commutativity of the triangle

```text
                       O_S
                  ╱         ╲
             η_𝒰              η_𝒰 ⊗ η_𝒰
(v)*            ╱               ╲
              ╱                   ╲
       𝒰  ───────────────────→  𝒰 ⊗ 𝒰.
                       ∆_𝒰
```

On the other hand, as in every category, the *antipode* $c_{\mathcal{U}}$ is an isomorphism of $\mathcal{U}$ onto the
"opposite" group object;[^N.D.E-VII_A-31] in particular, $c_{\mathcal{U}}$ induces an algebra isomorphism of
$\mathcal{U}$ onto the opposite algebra $\mathcal{U}^{\circ}$.

### 3.2.2

<!-- label: III.VII_A.3.2.2 -->

Since the functor $\mathcal{U} \mapsto \operatorname{Spec}^{*} \mathcal{U}$ commutes with finite products, it transforms
a group coalgebra into a group $S$-functor; and indeed, for every $S$-scheme $T$, the elements $x \in \Gamma(T,
\mathcal{U}_{T})$ belonging to $(\operatorname{Spec}^{*} \mathcal{U})(T)$ form a group under the multiplication of the
algebra $\Gamma(T, \mathcal{U}_{T})$; the inverse of $x$ is none other than $c_{\mathcal{U}}(x)$. According to 3.1.2.1,
one has:

**Scholium 3.2.2.1.**[^N.D.E-VII_A-32] *Let $\mathcal{U}$ be an `O_S`-coalgebra in groups, finite and locally free as an
`O_S`-module. Then the group $S$-functor $\operatorname{Spec}^{*} \mathcal{U}$ is represented by the $S$-group, finite
and locally free, $\operatorname{Spec} \mathcal{U}^{*}$.*

<!-- label: III.VII_A.3.2.2.1 -->

**Remark 3.2.2.2.** *Let $\mathcal{L}$ be an `O_S`-Lie algebra and $\mathcal{U}(\mathcal{L})$ the enveloping algebra of
$\mathcal{L}$, i.e., the sheaf on $S$ associated with the presheaf which to every open $V$ assigns the enveloping
algebra $U(\Gamma(V, \mathcal{L}))$ of the Lie algebra $\Gamma(V, \mathcal{L})$.*

<!-- label: III.VII_A.3.2.2.2 -->

Every homomorphism from $\mathcal{L}$ into the Lie algebra underlying an associative `O_S`-algebra factors in one and
only one way through the canonical morphism <!-- original page 431 --> from $\mathcal{L}$ into
$\mathcal{U}(\mathcal{L})$; moreover, this universal property entails, besides the functoriality of
$\mathcal{U}(\mathcal{L})$ in $\mathcal{L}$, that the enveloping algebra of a product of Lie algebras is identified with
the tensor product of the enveloping algebras.

In particular, the diagonal morphism $\delta : \mathcal{L} \to \mathcal{L} \times \mathcal{L}$ induces an algebra
homomorphism `∆ : 𝒰(ℒ) → 𝒰(ℒ × ℒ) ≃ 𝒰(ℒ) ⊗ 𝒰(ℒ)`. The zero morphism $\mathcal{L} \to 0$ induces a homomorphism
$\epsilon : \mathcal{U}(\mathcal{L}) \to \mathcal{U}(0) \simeq O_{S}$. The isomorphism $x \mapsto -x$ of $\mathcal{L}$
onto the opposite Lie algebra $\mathcal{L}^{\circ}$ induces an anti-isomorphism $c$ of the algebra
$\mathcal{U}(\mathcal{L})$. One then verifies easily that the multiplication $m$ of the algebra
$\mathcal{U}(\mathcal{L})$ makes `(𝒰(ℒ), ∆)` an `O_S`-coalgebra in groups with $\epsilon$ as augmentation and $c$ as
antipode.[^N.D.E-VII_A-33]

### 3.2.3

<!-- label: III.VII_A.3.2.3 -->

[^N.D.E-VII_A-34] Let $\mathcal{U}$ be an `O_S`-coalgebra in groups. We shall see that the group $S$-functor $G =
\operatorname{Spec}^{*} \mathcal{U}$ is *very good*, in the sense of II, 4.6 and 4.10.

Let $M$ be a free `O_S`-module of rank $r$, and let $T \to S$ be an $S$-scheme. Since $I_{T}(M) =
\operatorname{Spec}(O_{T} \oplus M_{T})$, so that $\pi : I_{T}(M) \to T$ is affine, one has

```text
π_*(𝒰_{I_T(M)}) = 𝒰_T ⊗_{O_T} π_*(O_{I_T(M)}) = 𝒰_T ⊗_{O_T} (O_T ⊕ M_T),
```

and so

```text
(1)    Γ(I_T(M), 𝒰_{I_T(M)}) ≃ Γ(T, 𝒰_T) ⊗_{O(T)} (O(T) ⊕ Γ(T, M_T)).
```

Let $(d_{1}, \cdots, d_{r})$ be a basis of $M$. Then an element $u_{0} + \sum_{i} u_{i} d_{i}$ of $\Gamma(I_{T}(M),
\mathcal{U}_{I_{T}(M)})$ belongs to $G(I_{T}(M))$ if and only if one has:

```text
1 = ε(u_0 + ∑_i u_i d_i) = ε(u_0) + ∑_i ε(u_i) d_i,
```

and

```text
(u_0 + ∑_i u_i d_i) ⊗ (u_0 + ∑_i u_i d_i) = ∆(u_0 + ∑_i u_i d_i) = ∆(u_0) + ∑_i ∆(u_i) d_i,
```

that is to say:

```text
(2)    { ε(u_0) = 1,  ∆ u_0 = u_0 ⊗ u_0,    (i.e. u_0 ∈ G(T))
       { ε(u_i) = 0,  ∆(u_i) = u_i ⊗ u_0 + u_0 ⊗ u_i,  for i = 1, …, r.
```

Moreover, the morphism $G(I_{T}(M)) \to G(T)$ corresponding to the zero section of $I_{T}(M) \to T$ is given by $u_{0} +
\sum_{i} u_{i} d_{i} \mapsto u_{0}$. From this, combined with (1) and (2), one deduces that, if $N$ is a second free
`O_S`-module of finite rank, the diagram of sets

```text
       G(I_T(M ⊕ N))          ─────→  G(I_T(N))
           │                              │
           ▼                              ▼
       G(I_T(M))               ─────→  G(T)
```

is cartesian, i.e. $G$ satisfies condition (E) of II, 3.5.

<!-- original page 462 -->

Let us denote by $Prim \Gamma(T, \mathcal{U}_{T})$ the sub-$O(T)$-module of $\Gamma(T, \mathcal{U}_{T})$ formed by the
*primitive elements*, i.e., the elements $u$ which satisfy (with the abuse of notation signaled in 3.1.2):

```text
∆u = u ⊗ 1 + 1 ⊗ u,    ε(u) = 0.
```

[^N.D.E-VII_A-35]

Since `(Lie G)(T)` is the set of elements $u_{0} + u d \in G(I_{T})$ above the unit element $u_{0} = 1$ of $G(T)$, one
obtains an isomorphism of $O(T)$-modules, functorial in $T$:[^N.D.E-VII_A-36]

```text
(Lie G)(T) ≃ Prim Γ(T, 𝒰_T).
```

On the other hand, one deduces from (1) that

```text
Prim Γ(I_T(M), 𝒰_{I_T(M)}) ≃ Prim Γ(T, 𝒰_T) ⊗_{O(T)} O(I_T(M)),
```

and it follows that the natural morphism of $O(I_{T}(M))$-modules:

```text
(Lie G)(T) ⊗_{O(T)} O(I_T(M)) ⟶ (Lie G)(I_T(M))
```

is an isomorphism, i.e. `Lie G` is a *good `O_S`-module* (cf. II, Déf. 4.4).

So $G$ is a good group $S$-functor (cf. II, Déf. 4.6), and according to II, 4.7.2, `Lie G` is equipped with an
`O_S`-bilinear "Lie bracket" satisfying the Jacobi identity. It remains to show that $G$ is very good, i.e., that the
"bracket" on `(Lie G)(T)` satisfies $[u, u] = 0$ for every $u \in (Lie G)(T)$ (cf. II, 4.10).

Let `u, v` be two elements of `(Lie G)(T)`, i.e., two primitive elements of $\Gamma(T, \mathcal{U}_{T})$. Set $I =
\operatorname{Spec} O_{S}[d]/(d^{2})$ and $I' = \operatorname{Spec} O_{S}[d']/(d'^{2})$. Since the composition law of
$G(I \times I')$ is induced by the multiplication of the algebra $\mathcal{U}_{I \times I'}$, one has in $G(I \times
I')$ the equality:

```text
(1 + ud)(1 + vd')(1 + ud)^{-1}(1 + vd')^{-1} = (1 + ud)(1 + vd')(1 − ud)(1 − vd')
                                              = 1 + (uv − vu) dd'
```

<!-- original page 432 -->

According to the description of the bracket `[u, v]` given before Prop. 4.8 of Exp. II, one obtains that

```text
[u, v] = uv − vu,
```

where the right-hand term is the commutator of $u$ and $v$ in the algebra $\Gamma(T, \mathcal{U}_{T})$, whence $[u, u] =
0$. One has thus obtained the following proposition:[^N.D.E-VII_A-37]

**Proposition.** *Let $\mathcal{U}$ be an `O_S`-coalgebra in groups. The group $S$-functor $G = \operatorname{Spec}^{*}
\mathcal{U}$ is very good, and one has an isomorphism $Lie G \simeq Prim \mathcal{W}(\mathcal{U})$ of `O_S`-Lie
algebras, where $Prim \mathcal{W}(\mathcal{U})$ denotes the functor which to every $T \to S$ associates the $O(T)$-Lie
algebra formed by the primitive elements of $\mathcal{W}(\mathcal{U})(T) = \Gamma(T, \mathcal{U}_{T})$.*

### 3.3

<!-- label: III.VII_A.3.3 -->

Suppose finally that $\mathcal{U}$ is a commutative group coalgebra, i.e., the triangle

```text
                              σ
       𝒰 ⊗ 𝒰  ────────────────────→  𝒰 ⊗ 𝒰
              ╲                    ╱
(i)*           ╲                  ╱
              m_𝒰              m_𝒰
                  ╲          ╱
                       𝒰
```

is commutative, or in other words that $m_{\mathcal{U}}$ makes $\mathcal{U}$ a commutative `O_S`-algebra. Conditions
(i), (ii), (iii), (iv), (v), (vi), (i)*, (ii)*, (iii)\* and (v)\* then also signify that $\mathcal{U}$ is a cogroup in
the category of commutative `O_S`-algebras. Therefore, if moreover $\mathcal{U}$ is a quasi-coherent `O_S`-module, then
the affine $S$-scheme $\operatorname{Spec} \mathcal{U}$ is a commutative $S$-group scheme.

In this case, since the diagonal morphism `∆'` of $O_{S}[T, T^{-1}]$ sends $T$ to $T \otimes T$, the morphisms of
$S$-groups from $\operatorname{Spec} \mathcal{U}$ into $\mathbb{G}_{m, S}$ (I 4.3.2) correspond bijectively to the
morphisms of unital `O_S`-algebras

```text
φ : O_S[T, T^{-1}] ⟶ 𝒰
```

such that `(φ ⊗ φ) ∘ ∆' = ∆_𝒰 ∘ φ` (in this case, $\epsilon_{\mathcal{U}} \circ \phi$ is the neutral element of
$\mathbb{G}_{m, S}(S)$, i.e., the augmentation $\epsilon'$). Such a morphism $\phi$ is determined by the image
$\phi(T)$, which must be an invertible element $x$ of $\mathcal{U}$ satisfying `∆_𝒰 x = x ⊗ x` and
$\epsilon_{\mathcal{U}}(x) = \epsilon'(T) = 1$. One therefore has:

```text
Hom_{S-gr.}(Spec 𝒰, 𝔾_{m, S}) ≃ (Spec^* 𝒰)(S)
```

and since this formula remains valid after any base change, this gives: <!-- original page 433 -->

```text
Spec^* 𝒰 ≃ Hom_{S-gr.}(Spec 𝒰, 𝔾_{m, S}).
```

One has therefore obtained the

**Proposition 3.3.0.** *If $\mathcal{U}$ is an `O_S`-coalgebra in commutative groups, quasi-coherent as an `O_S`-module,
then the affine $S$-scheme $G = \operatorname{Spec} \mathcal{U}$ is a commutative $S$-group scheme, and one has an
isomorphism of group $S$-functors*

<!-- label: III.VII_A.3.3.0 -->

```text
Spec^* 𝒰 ≃ Hom_{S-gr.}(G, 𝔾_{m, S}).
```

If one supposes moreover that $\mathcal{U}$ is a locally free `O_S`-module of finite type, then, according to 3.1.2.1,
the group $S$-functor $\operatorname{Spec}^{*} \mathcal{U}$ is represented by $\operatorname{Spec} \mathcal{U}^{*}$. One
thus obtains the

**Proposition 3.3.1 (Cartier duality).** *The functor*

<!-- label: III.VII_A.3.3.1 -->

```text
𝒜(G) ↦ 𝒜(G)^* = Hom_{O_S-Mod.}(𝒜(G), O_S)
```

*induces a duality $(\ast)$ of the category of commutative, finite and locally free $S$-group schemes; it associates
with $G$ the $S$-group $\operatorname{Hom}_{S-gr.}(G, \mathbb{G}_{m, S})$.*

## 4. "Frobeniuseries"

<!-- label: III.VII_A.4 -->

<!-- original page 434 -->

Let $p$ be a fixed prime number and $(Sch/\mathbb{F}_{p})$ the category of schemes of characteristic $p$, i.e., of
schemes above the prime field $\mathbb{F}_{p}$. Following the general conventions of this Seminar, we identify
$(Sch/\mathbb{F}_{p})$ with a subcategory of $(Sch/\mathbb{F}_{p})^{\wedge}$ by means of the functor $h$ of I 1.1. We
likewise take advantage of the isomorphism from $\operatorname{Hom}(h_{X}, F)$ onto $F(X)$ defined in I 1.1 to identify
these two sets whenever $X$ is an $\mathbb{F}_{p}$-scheme and $F$ an object of $(Sch/\mathbb{F}_{p})^{\wedge}$.

**Notations 4.0.**[^N.D.E-VII_A-39] *If $T$ is an $\mathbb{F}_{p}$-scheme, a $T$-functor is a morphism $q : F \to T$ of
$(Sch/\mathbb{F}_{p})^{\wedge}$ having $T$ as target; for every $T$-scheme $r : X \to T$, the set of $T$-morphisms $X
\to F$, i.e., of $\mathbb{F}_{p}$-morphisms $s : X \to F$ such that $q \circ s = r$, will then be denoted $q(r)$,
$q(X/T)$, $F(r)$ or $F(X/T)$ (or even $F(X)$ when no confusion will be possible with $\operatorname{Hom}(h_{X}, F)$).*

<!-- label: III.VII_A.4.0 -->

### 4.1

<!-- label: III.VII_A.4.1 -->

For every scheme $S$ of characteristic $p$, we denote by $fr(S)$, or simply `fr`, the endomorphism of $S$ which induces
the identity on the underlying topological space of $S$ and which associates $x^{p}$ with a section $x$ of `O_S` on an
open $U$.

Then the map $fr : S \mapsto fr(S)$ is an endomorphism of the identity functor of
$(Sch/\mathbb{F}_{p})$,[^N.D.E-VII_A-40] which implies the following results. Let $E$ be an $\mathbb{F}_{p}$-functor,
i.e., an object of $(Sch/\mathbb{F}_{p})^{\wedge}$; the map which to every $\mathbb{F}_{p}$-scheme $S$ associates the
endomorphism $E(fr(S))$ of $E(S)$ is a functorial endomorphism of $E$ which we shall denote $fr(E)$ or `fr`; this
notation is compatible with the identification of $(Sch/\mathbb{F}_{p})$ with a subcategory of
$(Sch/\mathbb{F}_{p})^{\wedge}$. Moreover, the map $E \mapsto fr(E)$ is an endomorphism of the identity functor of
$(Sch/\mathbb{F}_{p})^{\wedge}$ (which we shall again denote `fr`).[^N.D.E-VII_A-41]

For every $\mathbb{F}_{p}$-scheme $S$ and every $S$-functor $q : X \to S$, we denote by $X^{(p/S)}$ or $X^{(p)}$ the
inverse image of $X$ by the base change $fr(S)$:

```text
                  pr_X
       X^{(p/S)}  ──────→  X
           │                  │ q
           ▼                  ▼
                fr(S)
            S  ──────────→  S.
```

<!-- original page 465 -->

The commutative square

```text
                       fr(X)
              X  ──────────→  X
              │                  │
            q │                  │ q
              ▼       fr(S)       ▼
              S  ──────────→  S
```

induces an $S$-morphism, denoted $Fr(X/S)$ (or simply `Fr`), from $X$ into $X^{(p/S)}$ such that $fr(X) = pr_{X} \circ
Fr(X/S)$:

```text
              X
              │ ╲
              │  ╲  Fr(X/S)
              │   ╲
              │    ╲             fr(X)
              │     X^{(p/S)}  ──pr_X→  X
              │       │                  │
            q │       │ q^{(p/S)}        │ q
              ▼       ▼       fr(S)       ▼
              S       S       ─────→     S.
```

We shall say that $Fr(X/S)$ is the *Frobenius morphism of $X$ relative to $S$*; it is clear that the map $Fr : X \mapsto
Fr(X/S)$ is a functorial homomorphism.

[^N.D.E-VII_A-42] Let $r : T \to S$ be an $S$-scheme. For every $\phi \in X(r) = \operatorname{Hom}_{S}(T, X)$ (cf.
4.0), one has a commutative diagram:

```text
                  Fr(X/S)              pr_X
       X  ──────────────→  X^{(p/S)}  ──────→  X
        ╲                         │                  │
         ╲ φ                      │ q^{(p/S)}        │ q
       r  ╲                       │                  │
            ╲                     ▼      fr(S)       ▼
              T  ──────────────→  S  ──────────→  S.
```

According to the definition of $X^{(p/S)}$ as fibered product, $pr_{X}$ induces a bijection:

```text
X^{(p/S)}(r) = Hom_S(T, X^{(p/S)})  ⥲  Hom_S(T, X) = X(fr(S) ∘ r).
```

On the other hand, $r \circ fr(T) = fr(S) \circ r$, since `fr` is an endomorphism of the identity functor. It follows
that the map $Fr(X/S)(r) : X(r) \to X^{(p/S)}(r)$ can be characterized by the commutativity of the following square:

```text
                  Fr(X/S)(r)
       X(r)  ────────────────→  X^{(p/S)}(r)

(†)   X(fr(T))                       ≀
                                          
       X(r ∘ fr(T))           X(fr(S) ∘ r).
```

<!-- original page 466 -->

For example, if $X$ is the subscheme of $S$ defined by a quasi-coherent ideal $\mathcal{I}$, then $X^{(p)}$ is the
subscheme of $S$ defined by the ideal $\mathcal{I}^{{p}}$ generated by the $p$-th powers of the sections of
$\mathcal{I}$; moreover, $Fr(X/S)$ is then the canonical immersion of $\operatorname{Spec}(O_{X} / \mathcal{I})$ into
$\operatorname{Spec}(O / \mathcal{I}^{{p}})$.

### 4.1.1

<!-- label: III.VII_A.4.1.1 -->

[^N.D.E-VII_A-43] Let $t : T \to S$ be a base change and $X_{T} = X \times_{q, t} T$. Consider the inverse image of
`X_T` by $fr(T)$:

```text
       (X_T)^{(p/T)}  ────→  X_T  ─────→  X
                                              │ q
                  fr(T)              t
              T  ──────→  T  ──→  S.
```

<!-- original page 436 -->

Since $t \circ fr(T) = fr(S) \circ t$, then $(X_{T})^{(p/T)}$ is identified with the inverse image of $X^{(p/S)}$ by
$t$; in other words, one has a canonical isomorphism:

$$ X^{(p/T)}_{T} \xrightarrow{\sim} (X^{(p/S)})_{T}. $$

It is clear that, in this identification, $Fr(X_{T} / T)$ is identified with the inverse image $Fr(X/S)_{T}$ of
$Fr(X/S)$.

#### 4.1.1.1

<!-- label: III.VII_A.4.1.1.1 -->

In particular, if $S$ is the spectrum of the prime field $\mathbb{F}_{p}$, $X^{(p/S)}$ is equal to $X$ and $Fr(X/S)$ to
$fr(X)$. Consequently, $X^{(p/T)}_{T}$ is identified with `X_T` and $Fr(X_{T} / T)$ with $fr(X)_{T}$.

For example, if $E$ is a set and `E_T` the constant $T$-scheme of type $E$, one has $E^{(p/T)}_{T} \simeq E_{T}$ and
$Fr(E_{T} / T) \simeq id_{E_{T}}$.

### 4.1.2

<!-- label: III.VII_A.4.1.2 -->

The functor $X \mapsto X^{(p/S)}$ obviously commutes with products; it therefore transforms an $S$-group $G$ into an
$S$-group $G^{(p/S)}$; moreover, since `Fr` is a functorial homomorphism, then

$$ Fr(G/S) : G \longrightarrow G^{(p/S)} $$

is a homomorphism of $S$-groups. We shall denote `Fr G` its kernel.

If $r : T \to S$ is a scheme above $S$, it follows from the diagram `(†)` of 4.1 that the value of `Fr G` at $r$ is the
kernel of the homomorphism

```text
G(fr(T)) : G(r) ⟶ G(r ∘ fr(T)).
```

Now, when $T$ is the scheme `I_R` of dual numbers over an $S$-scheme $R$, $fr(I_{R})$ factors as follows:

```text
I_R  ──can.→  R  ──fr(R)→  R  ──s→  I_R,
```

where $s$ is the zero section. It follows that $(Fr G)(I_{R})$ contains the kernel $Lie(G/S)(R)$ of the morphism $G(s) :
G(I_{R}) \to G(R)$, and that one therefore has: $Lie(G/S) = Lie(Fr G / S)$.

### 4.1.3

<!-- label: III.VII_A.4.1.3 -->

<!-- original page 437 -->

More generally, for every $S$-functor $X$, we define the $S$-functor $X^{(p^{n})}$ by recursion on $n$ by means of the
formulas:

```text
X^{(p)} = X^{(p/S)}    and    X^{(p^n)} = (X^{(p^{n-1})})^{(p)}.
```

Similarly, $Fr^{n}(X/S)$ or $Fr^{n}$ denote the composed functorial homomorphism

```text
X ──Fr(X/S)→ X^{(p)} ──Fr(X^{(p)}/S)→ X^{(p²)} ──→ ··· ──→ X^{(p^{n-1})} ──Fr(X^{(p^{n-1})}/S)→ X^{(p^n)}.
```

One will note that, according to 4.1.1, $Fr(X^{(p)}/S)$ coincides with $Fr(X/S)^{(p)}$, i.e., the following diagram is
commutative:

```text
       X^{(p)}  ────→  X

   Fr(X^{(p)}/S)         Fr(X/S)

       X^{(p²)}  ────→  X^{(p)}.
```

If $G$ is a group $S$-functor, $G^{(p^{n})}$ is also one and $Fr^{n}(G/S)$ is a homomorphism of group $S$-functors.

**Definition.** *We shall denote by $Fr^{n} G$ the kernel of $Fr^{n}(G/S)$ and we shall say that $G$ is of height
$\leqslant n$ if $Fr^{n}(G/S)$ is zero, i.e., if $Fr^{n} G = G$.*

**Lemma.** *The group subfunctor $Fr^{n} G$ of $G$ is characteristic, i.e., for every $S$-scheme $T$, every endomorphism
$\phi$ of the group $T$-functor `G_T` induces an endomorphism of $(Fr^{n} G)_{T}$.*

Indeed, since the construction of $G^{(p^{n})}$ and of $Fr^{n}(G/S)$ commutes with base changes according to 4.1.1, one
may suppose $T = S$; in this case, the assertion follows from the fact that $Fr^{n}(G/S)$ is a functorial homomorphism.

### 4.1.4. Examples

<!-- label: III.VII_A.4.1.4 -->

a) Consider first an "abstract" abelian group $M$ and the diagonalizable group $G = D_{S}(M)$ of type $M$ (I 4.4): for
every $S$-scheme $T$, $G(T)$ is therefore the abelian group $\operatorname{Hom}_{(Ab)}(M, \Gamma(T, O_{T})^{\times})$.
Since $G$ is the inverse image of the diagonalizable group $D(M)$ over $\mathbb{F}_{p}$, $G^{(p)}$ is identified with
$G$ and $Fr(G/S)(T)$ is identified with the endomorphism $x \mapsto x^{p}$ of $G(T)$ (4.1.1). In particular, when $M$ is
equal to $\mathbb{Z}$, one has $D_{S}(M) = \mathbb{G}_{m, S}$, so that:

> $Fr \mathbb{G}_{m, S}$ is the $S$-group $\mu_{p, S}$ which to every $S$-scheme $T$ associates the group of $p$-th
> roots of unity in $\Gamma(T, O_{T})^{*}$.

b) Consider now a scheme $S$ of characteristic $p$ and a sheaf of modules $\mathcal{E}$ on $S$. According to I 4.6.2,
one has a canonical isomorphism

$$ \mathcal{W}(\mathcal{E})^{(p)} \simeq \mathcal{W}(\mathcal{E}^{(p)}), $$

where $\mathcal{E}^{(p)}$ is the inverse image of $\mathcal{E}$ by $fr(S)$. For every $S$-scheme $\pi : T \to S$, the
map <!-- original page 438 --> $Fr(\mathcal{W}(\mathcal{E}))(\pi)$ is determined, according to 4.1 `(†)`, by the
commutative triangle

```text
       Γ(T, π^* fr(S)^* ℰ)  ──can.~→  Γ(T, fr(T)^* π^* ℰ)
              ╲                                    ╱
               ╲                                  ╱
        Fr(𝒲(ℰ)/S)(π)                          f'
                  ╲                          ╱
                    Γ(T, π^* ℰ),
```

where $f'$ is the map induced by $fr(T)$.

In particular, if $\mathcal{E}$ is equal to `O_S`, $\mathcal{W}(\mathcal{E})$ is identified with the additive group
$\mathbb{G}_{a, S}$. In this case, one has $\mathcal{E}^{(p)} = \mathcal{E} = O_{S}$ and the Frobenius morphism
$Fr(\mathbb{G}_{a, S}/S)$ sends $x \in \Gamma(T, O_{T})$ to $x^{p}$. So:

> $Fr \mathbb{G}_{a, S}$ is the $S$-group $\alpha_{p, S}$ which to every $S$-scheme $T$ associates the group: ${ x \in
> \Gamma(T, O_{T}) | x^{p} = 0}$.

c) One would see similarly that, for every quasi-coherent `O_S`-algebra $\mathcal{A}$, $(\operatorname{Spec}
\mathcal{A})^{(p)}$ is identified with the spectrum $\operatorname{Spec} \mathcal{A}^{(p)}$ of the inverse image of
$\mathcal{A}$ by $fr(S)$. If $\pi$ denotes the endomorphism $x \mapsto x^{p}$ of the sheaf of rings `O_S`, one has
therefore[^N.D.E-VII_A-44]

```text
𝒜^{(p)} = 𝒜 ⊗_π O_S
```

and $Fr((\operatorname{Spec} \mathcal{A})/S)$ is induced by the morphism of `O_S`-algebras $\mathcal{A} \otimes_{\pi}
O_{S} \to \mathcal{A}$ defined by $a \otimes_{\pi} x \mapsto a^{p} x$.

For every quasi-coherent `O_S`-module $\mathcal{E}$, finally, one has canonical isomorphisms

```text
𝒱(ℰ)^{(p)} ≃ 𝒱(ℰ^{(p)})    and    𝒮(ℰ)^{(p)} ≃ 𝒮(ℰ^{(p)}),
```

where $\mathcal{S}(\mathcal{E})$ denotes the symmetric algebra of the `O_S`-module $\mathcal{E}$.

<!-- original page 439 -->

d) Let $\mathcal{U}$ be an `O_S`-coalgebra (3.1) and $T$ a scheme of characteristic $p$. If $\mathcal{U}^{(p/S)}$ or
$\mathcal{U}^{(p)}$ denote the inverse image of the coalgebra $\mathcal{U}$ by $fr(S)$, one has as in b) a canonical
isomorphism:

```text
(Spec^* 𝒰)^{(p)} ≃ Spec^* 𝒰^{(p)}.
```

If $\mathcal{U}$ is a coalgebra in groups, the value of $Fr(\operatorname{Spec}^{*} \mathcal{U})$, i.e., of the kernel
of the Frobenius morphism $\operatorname{Spec}^{*} \mathcal{U} \to (\operatorname{Spec}^{*} \mathcal{U})^{(p)}$, for an
$S$-scheme $T$ is therefore the set of elements $\gamma$ of

```text
(Spec^* 𝒰)(T) = { x ∈ Γ(T, 𝒰_T) | ε_{𝒰_T}(x) = 1, ∆_{𝒰_T} x = x ⊗ x }
```

such that the image in $\Gamma(T, \mathcal{U}_{T} \otimes_{fr(T)} O_{T})$ of the element $\gamma \otimes_{fr(T)} 1$ of
$\Gamma(T, \mathcal{U}_{T}) \otimes_{fr(T)} O(T)$ is equal to `1`.

### 4.2

<!-- label: III.VII_A.4.2 -->

<!-- original page 440 -->

[^N.D.E-VII_A-45] We shall now occupy ourselves with a construction close to the preceding one: let $S$ be a scheme of
characteristic $p$, $X$ an $S$-scheme and $X^{p_{S}}$ the product in the category $(Sch/S)$ of $p$ copies of $X$.

We then denote by $U_{p}(X)$ the open subscheme of $X^{p_{S}}$ which is the union of the products $U^{p_{S}}$, when $U$
ranges over the affine opens of $X$. A point $x$ of $X^{p_{S}}$ therefore belongs to $U_{p}(X)$ if and only if the
projections $pr_{i} x$ of $x$ onto the factors of $X^{p_{S}}$ belong to a common affine open of $X$. For example, if
every finite part of $X$ is contained in an affine open, one has $U_{p}(X) = X^{p_{S}}$.

The symmetric group $\mathfrak{S}_{p}$ of order $p$ operates on $X^{p_{S}}$ by permutation of factors and leaves stable
the open $U_{p}(X)$. We shall call the *$p$-fold symmetric product of $X$* and we shall denote $\Sigma^{p} X$ the
quotient of $X^{p_{S}}$ by $\mathfrak{S}_{p}$ in the category of ringed spaces. Let $q(X)$, or simply $q$, be the
canonical projection $X^{p_{S}} \to \Sigma^{p} X$.

Then $q$ maps $U_{p}(X)$ onto an open $V_{p}(X)$ of the symmetric product, which one may describe as follows (cf. V
4.1). The structure sheaf of $\Sigma^{p} X$ induces on $V_{p}(X)$ a scheme structure; the morphism
$q'(X) : U_{p}(X) \to V_{p}(X)$ induced by $q(X)$ is affine and even integral; when $U$ ranges over the affine opens of
$X$ which project into an affine open $V$ of $S$ varying, the $\Sigma^{p} U$ form an affine covering of $V_{p}(X)$; if
$R$ <!-- original page 441 --> denotes the affine algebra of $V$ and $A$ that of $U$, $\Sigma^{p} U$ has as affine
algebra the subalgebra $\Sigma^{p} A$ of $\bigotimes^{p}_{R} A$ formed by the symmetric tensors.

Consider now the diagonal morphism $\delta$ of $X$ into $U_{p}(X)$. If $V = \operatorname{Spec} R$ is an affine open of
$S$ and $U = \operatorname{Spec} A$ an affine open of $X$ above $V$, the restriction of $\delta$ to $U$ is defined by
the algebra morphism

```text
η : ⨂^p_R A ⟶ A,    a_1 ⊗ ··· ⊗ a_p ↦ a_1 a_2 ··· a_p.
```

One therefore has, if $N$ is the symmetrization operator:

```text
η(N(a_1 ⊗ ··· ⊗ a_p)) = η(∑_{σ ∈ 𝔖_p} a_{σ(1)} ⊗ ··· ⊗ a_{σ(p)}) = p! a_1 ··· a_p = 0.
```

In other words, $\eta$ vanishes on the subspace $N(\bigotimes^{p}_{R} A)$ of $\Sigma^{p} A$ formed by the symmetrized
tensors. Moreover, if $f$ is a symmetric tensor, one has obviously $N(f a) = f N(a)$, which shows that
$N(\bigotimes^{p}_{R} A)$ is an ideal of $\Sigma^{p} A$. We shall henceforth denote

```text
U^{[p/S]} = Spec(Σ^p A / N(⨂^p_R A));
```

it is a closed subscheme of $\Sigma^{p}(U) = V_{p}(U)$. The union of the $U^{[p/S]}$, when $U$ ranges over the affine
opens of $X$ which project into a varying affine open $V$ of $S$, is a closed subscheme of $V_{p}(X)$, denoted
$X^{[p/S]}$.

Moreover, if $i(X)$ denotes the inclusion of $X^{[p/S]}$ into $V_{p}(X)$, we have just seen that $q'(X) \circ \delta$
factors through $X^{[p/S]}$, whence a morphism $F^{[p]}(X/S) : X \to X^{[p/S]}$:[^N.D.E-VII_A-46]

<!-- original page 470 -->

```text
                                   δ(X)
       X^{p_S}  ⊃  U_p(X)  ←──────────  X

   q(X)             q'(X)            F^{[p]}(X/S)

                                   i(X)
       Σ^p(X)  ⊃  V_p(X)  ←──────────  X^{[p/S]}.
```

It is clear that $X^{[p/S]}$ is functorial in $X$ and that the map $F^{[p]} : X \mapsto F^{[p]}(X/S)$ is a functorial
homomorphism.

### 4.2.1

<!-- label: III.VII_A.4.2.1 -->

The schemes $X^{[p/S]}$ and $X^{(p/S)}$ are obviously related: let $V$ be an affine open of $S$ with affine ring $R$ and
$U$ an affine open of $X$ above $V$; let $A$ be the affine algebra of $U$. If $\pi$ denotes the endomorphism $x \mapsto
x^{p}$ of $R$, then $U^{(p/S)}$ has $A \otimes_{\pi} R$ as affine algebra. One verifies moreover that the map

```text
a ⊗_π λ ↦ (λ a ⊗ ··· ⊗ a    mod    N(⨂^p_R A))
```

defines a morphism of $R$-algebras from $A \otimes_{\pi} R$ into $\Sigma^{p} A / N(\bigotimes^{p}_{R} A)$, and the
latter induces a morphism $\phi(U) : U^{[p/S]} \to U^{(p/S)}$ such that $\phi(U) \circ F^{[p]}(U/S) = Fr(U/S)$.

"Gluing the pieces", one then obtains a commutative triangle

```text
                              X
                       ╱           ╲
              F^{[p]}(X/S)         Fr(X/S)
                  ╱                   ╲
                ╱                       ╲
              X^{[p/S]}  ──────φ(X)────→  X^{(p/S)}.
```

For example, if $X$ is the subscheme of $S$ defined by a quasi-coherent ideal $\mathcal{I}$, $F^{[p]}(X/S)$ is
identified with the identity morphism of $X$, so that $\phi(X)$ is the canonical immersion of $\operatorname{Spec}(O_{S}
/ \mathcal{I})$ into $\operatorname{Spec}(O_{S} / \mathcal{I}^{{p}})$. One thus sees that $\phi(X)$ is not an
isomorphism in general.

However, when $M$ is a free $R$-module, it is clear that the map

```text
M ⊗_π R ⟶ Σ^p M / N(⨂^p_R M),    m ⊗_π λ ↦ (λ m ⊗ ··· ⊗ m    mod    N(⨂^p_R M))
```

is bijective; this map therefore remains bijective when $M$ is $R$-flat, because every flat module is a filtered direct
limit of free modules (Lazard[^VII_A-4-1] [^N.D.E-VII_A-47]). It follows that

> $\phi(X) : X^{[p/S]} \to X^{(p/S)}$ is an isomorphism if $X$ is a flat $S$-scheme.

### 4.3

<!-- label: III.VII_A.4.3 -->

<!-- original page 471 -->

Consider finally an $S$-group scheme $G$ in abelian groups. Then the composed morphism $\mu(G) : U_{p}(G)
\hookrightarrow G^{p_{S}} \to G$, which is defined by the multiplication, factors through $V_{p}(G)$, i.e., there exists
a morphism $\nu(G) : V_{p}(G) \to G$ such that $\nu(G) \circ q'(G) = \mu(G)$, so that one has the following commutative
diagram:

```text
                          μ(G)                δ(G)
       G  ←──────────  U_p(G)  ←──────────  G
        ╲                  │                  │
         ╲ ν(G)             │                  │ F^{[p]}(G/S)
          ╲                 │ q'(G)            │
                            ▼                  ▼
                          V_p(G)  ←──────  G^{[p/S]}
                                  i(G)
        Ver(G/S)                                Fr(G/S)
                                          ╲       ╱
                                            φ(G)
                                              ▼
                                          G^{(p/S)}.
```

<!-- original page 442 -->

When $G$ is $S$-flat, $\phi(G)$ is an isomorphism and one can define a morphism (called the *Verschiebung*)

$$ Ver(G/S) : G^{(p/S)} \longrightarrow G $$

by means of the formula $Ver(G/S) = \nu(G) \circ i(G) \circ \phi(G)^{-1}$. When $G$ ranges over $S$-flat group schemes
in abelian groups, the map $Ver : G \mapsto Ver(G/S)$ is obviously a functorial homomorphism; consequently, $Ver(G/S)$
is a group homomorphism. For every $S$-scheme $T$ finally, the composed map

```text
G(T) ──δ(G)(T)→ U_p(G)(T) ──μ(G)(T)→ G(T)
```

sends $x \in G(T)$ to $p \cdot x$. We may write $p \cdot id_{G}$ instead of $\mu(G) \circ \delta(G)$, thus obtaining the
classical formula:

```text
(∗)                       Ver(G/S) ∘ Fr(G/S) = p · id_G.
```

**Examples 4.3.1.**

<!-- label: III.VII_A.4.3.1 -->

(a) When $G$ is a constant $S$-scheme in abelian groups, we know that $Fr(G/S)$ is identified with the identity morphism
of $G$ (cf. 4.1.1.1). One therefore has $Ver(G/S) = p id_{G}$.

(b) When $G$ is the diagonalizable $S$-group of type $M$, $Fr(G/S)$ is equal to $p id_{G}$ according to 4.1.4 (a); one
then sees easily that $Ver(G/S)$ is the identity morphism of $G$.

(c) When $\mathcal{E}$ is a flat `O_S`-module and $G$ is the $S$-group $\mathcal{V}(\mathcal{E})$, the morphism
$Ver(G/S)$ is zero, as is $p \cdot id_{G}$. One will see in Exposé VII_B that a commutative algebraic group $G$ over a
field $k$ is "unipotent" if and only if the composed homomorphism

```text
G^{(p^n)} ──Ver(G^{(p^{n-1})}/S)→ G^{(p^{n-1})} ──→ ··· ──→ G^{(p)} ──Ver(G/S)→ G
```

<!-- original page 443 -->

is zero for some $n$ (one has set $G^{(p^{n})} = (G^{(p^{n-1})})^{(p)}$, cf. 4.1.3).[^N.D.E-VII_A-48]

### 4.3.2

<!-- label: III.VII_A.4.3.2 -->

Since the map $Ver : G \mapsto Ver(G/S)$ is a functorial homomorphism when $G$ ranges over $S$-flat group schemes in
commutative groups, the square

```text
                          Ver(G/S)
       G^{(p)}  ──────────────────→  G

   Fr(G/S)^{(p)}                            Fr(G/S)
                                
                       Ver(G^{(p)}/S)
       G^{(p²)}  ──────────────────→  G^{(p)}
```

is commutative, where $Fr(G/S)^{(p)}$ denotes the inverse image of $Fr(G/S)$ by the base change $fr(S)$. According to
4.1.1, one has $Fr(G/S)^{(p)} = Fr(G^{(p)}/S)$, so, according to 4.3 $(\ast)$ applied to $G^{(p)}$, one obtains:

```text
(∗∗)        Fr(G/S) ∘ Ver(G/S) = Ver(G^{(p)}/S) ∘ Fr(G^{(p)}/S) = p · id_{G^{(p)}}.
```

### 4.3.3

<!-- label: III.VII_A.4.3.3 -->

<!-- original page 444 -->

Suppose finally that $G$ is a commutative, finite and locally free $S$-group; let $\mathcal{A}$ be the `O_S`-affine
algebra of $G$ and $\pi$ the endomorphism of the sheaf of rings `O_S` which sends a section $x$ of `O_S` to
$x^{p}$.[^N.D.E-VII_A-49] We denote by $\Sigma^{p} \mathcal{A}$ the subalgebra of $\bigotimes^{p}_{O_{S}} \mathcal{A}$
formed by the sections invariant under the action of the symmetric group, by $i(\mathcal{A})$ the inclusion of
$\Sigma^{p} \mathcal{A}$ into the tensor product. Let `∆_p(𝒜) : 𝒜 → ⨂^p_{O_S} 𝒜` be the morphism obtained by iterating
the diagonal morphism of the coalgebra $\mathcal{A}$ (it corresponds to the morphism of multiplication $U_{p}(G) =
G^{p_{S}} \to G$); according to the beginning of paragraph 4.3, `∆_p(𝒜)` factors through $\Sigma^{p} \mathcal{A}$, i.e.,
it induces a morphism

```text
a(𝒜) : 𝒜 ⟶ Σ^p 𝒜
```

such that `i(𝒜) ∘ a(𝒜) = ∆_p(𝒜)`.

On the other hand, let $S^{p}(\mathcal{A})$ be the degree-$p$ component of the symmetric algebra of $\mathcal{A}$ and
$q(\mathcal{A}) : \bigotimes^{p}_{O_{S}} \mathcal{A} \to S^{p}(\mathcal{A})$ the canonical projection. The
multiplication $m_{p}(\mathcal{A}) : \bigotimes^{p}_{O_{S}} \mathcal{A} \to \mathcal{A}$ factors through
$S^{p}(\mathcal{A})$, i.e., it induces a map

$$ b(\mathcal{A}) : S^{p}(\mathcal{A}) \longrightarrow \mathcal{A} $$

such that $b(\mathcal{A}) \circ q(\mathcal{A}) = m_{p}(\mathcal{A})$.

Since $\Sigma^{p} \mathcal{A}$ is the affine algebra of $V_{p}(\mathcal{A})$, then, according to the beginning of 4.3
again, the composed morphism $i(G) \circ \phi(G)^{-1}$ induces an algebra homomorphism

```text
r(𝒜) : Σ^p 𝒜 ⟶ 𝒜 ⊗_π O_S;
```

this homomorphism vanishes on the sections of the form

```text
∑_{σ ∈ 𝔖_p} a_{σ(1)} ⊗ ··· ⊗ a_{σ(p)}
```

<!-- original page 473 -->

and sends $a \otimes \cdot\cdot\cdot \otimes a$ to $a \otimes_{\pi} 1$. Similarly, $j(\mathcal{A})$ is the morphism of
`O_S`-modules $a \otimes_{\pi} 1 \mapsto q(a \otimes \cdot\cdot\cdot \otimes a)$. One thus obtains the commutative
diagram:

```text
                       ∆_p(𝒜)                       m_p(𝒜)
       𝒜  ────────────→  ⨂^p_{O_S} 𝒜  ──────────────→  𝒜
        ╲                  ▲     │                       ▲
         ╲ a(𝒜)      i(𝒜) │     │ q(𝒜)         b(𝒜) ╱
          ╲                │     ▼                     ╱
(𝒜)        Σ^p 𝒜                  S^p(𝒜)
              ╲                                       ╱
               ╲ r(𝒜)                          j(𝒜) ╱
                ╲                                  ╱
                   𝒜 ⊗_π O_S.
```

The composition $r(\mathcal{A}) \circ a(\mathcal{A})$ is associated with the Verschiebung morphism $Ver(G/S)$, while
$b(\mathcal{A}) \circ j(\mathcal{A})$ is associated with the Frobenius morphism $Fr(G/S)$.

The commutative diagram $(\mathcal{A})$ above is self-dual; let $D$ indeed be the functor which to every `O_S`-module
$\mathcal{M}$ associates the dual `O_S`-module $\operatorname{Hom}_{O_{S}}(\mathcal{M}, O_{S})$; it is clear that the
image of the diagram $(\mathcal{A})$ by the functor $D$ is none other than the diagram $(D\mathcal{A})$, the morphisms
$Dr(\mathcal{A})$, $Da(\mathcal{A})$, $Dj(\mathcal{A})$ and $Db(\mathcal{A})$ being identified respectively with
$j(D\mathcal{A})$, $b(D\mathcal{A})$, $r(D\mathcal{A})$ and $a(D\mathcal{A})$. According to 3.3.1, one therefore sees
that:

> In the category of commutative, finite and locally free $S$-groups, Cartier duality interchanges the Frobenius
> morphism and the Verschiebung.[^N.D.E-VII_A-50]

## 5. Restricted $p$-Lie algebras

<!-- label: III.VII_A.5 -->

<!-- original page 445 -->

Let us first recall some results from the *Séminaire Sophus Lie*.[^N.D.E-VII_A-51]

### 5.1

<!-- label: III.VII_A.5.1 -->

Let $p$ be a prime number, $R$ a commutative ring of characteristic $p$ and $A$ an associative $R$-algebra, but not
necessarily commutative. If $a$ and $b$ are two elements of $A$, we set $[a, b] = ab - ba$ and $a \cdot b = L_{a}(b) =
R_{b}(a)$. One then has:

```text
(ad x^p)(y) = [x^p, y] = (L_x^p − R_x^p)(y) = (L_x − R_x)^p(y) = (ad x)^p(y)
```

whence Jacobson's first formula:

```text
(i)                        ad(x^p) = (ad x)^p.
```

If $a_{1}, \cdots, a_{p}$ are $p$ arbitrary elements of $A$, then, denoting by $N$ the symmetrization operator (cf.
4.2), one has the equalities:

```text
(∗)    N(a_1 ⊗ ··· ⊗ a_p) = ∑_σ a_{σ(1)} ··· a_{σ(p)} = ∑_τ [a_{τ(1)} [a_{τ(2)} [··· [a_{τ(p-1)}, a_p] ···]]]
```

<!-- original page 474 -->

where $\sigma$ ranges over the permutations of $p$ letters and $\tau$ over those of $(p - 1)$ letters. Indeed, the last
term equals

```text
∑_τ ∑_{r=0}^{p-1} ∑_{i_1 < ··· < i_r} (−1)^s a_{τ(i_1)} a_{τ(i_2)} ··· a_{τ(i_r)} a_p a_{τ(j_s)} ··· a_{τ(j_1)}
```

where $\tau$ ranges over the permutations of $p - 1$ letters, $i_{1}, \cdots, i_{r}$ the strictly increasing sequences
of integers of the interval $[1, p - 1]$ and where $j_{1}, \cdots, j_{s}$ denotes the strictly increasing sequence whose
values are the integers of $[1, p - 1]$ different from $i_{1}, \cdots, i_{r}$. For a fixed value of $r$, the sum of the
terms $(-1)^{s} a_{\tau(i_{1})} \cdot\cdot\cdot a_{\tau(i_{r})} a_{p} a_{\tau(j_{s})} \cdot\cdot\cdot a_{\tau(j_{1})}$
obviously equals

```text
(−1)^s (p−1 choose s) ∑_ρ a_{ρ(1)} ··· a_{ρ(r)} a_p a_{ρ(r+1)} ··· a_{ρ(p−1)}
```

<!-- original page 446 -->

where $\rho$ ranges over the permutations of $p - 1$ letters. Now $(-1)^{s} (p-1 choose s) = 1$ in $\mathbb{F}_{p}$,
since in $\mathbb{F}_{p}[x]$ ($x$ an indeterminate) one has: $(x - 1)^{p} = x^{p} - 1 = (x - 1)(x^{p-1} +
\cdot\cdot\cdot + 1)$ and therefore $(x - 1)^{p-1} = x^{p-1} + \cdot\cdot\cdot + 1$. This proves $(\ast)$.

On the other hand, if $x_{0}$ and $x_{1}$ are two elements of $A$, one has

```text
(x_0 + x_1)^p = x_0^p + x_1^p + ∑ x_{z(1)} x_{z(2)} ··· x_{z(p)},
```

where $z$ ranges over the non-constant maps from `[1, p]` into `{0, 1}`. One deduces

```text
(x_0 + x_1)^p = x_0^p + x_1^p + ∑_{0 < r < p} 1/(r!(p−r)!) N(x_0, …, x_0, x_1, …, x_1)
```

(with $r$ factors $x_{0}$ and $p-r$ factors $x_{1}$).[^N.D.E-VII_A-52] Now, according to $(\ast)$, one has:

```text
N(x_0, …, x_0, x_1, …, x_1) = r! (p − 1 − r)! ∑_t [x_{t(1)} x_{t(2)} ··· x_{t(p−1)}, x_1] ···
```

(with $r$ factors $x_{0}$ and $p-r$ factors $x_{1}$), where $t$ ranges over the maps $[1, p-1] \to {0, 1}$ taking the
value `0` exactly $r$ times. From this one deduces Jacobson's second formula:

```text
(ii)    (x_0 + x_1)^p = x_0^p + x_1^p − ∑_{0 < r < p} ∑_t (1/r) [x_{t(1)} x_{t(2)} ··· x_{t(p−1)}, x_1] ···
```

where $t$ ranges over the maps $[1, p-1] \to {0, 1}$ taking the value `0` exactly $r$ times.

### 5.2

<!-- label: III.VII_A.5.2 -->

Let now $\mathfrak{g}$ be an $R$-Lie algebra. One says that a map $x \mapsto x^{(p)}$ from $\mathfrak{g}$ into
$\mathfrak{g}$ makes $\mathfrak{g}$ a *restricted $p$-Lie algebra* over $R$ if the following conditions are satisfied:

(0) $(\lambda x)^{(p)} = \lambda^{p} \cdot x^{(p)}$, for $\lambda \in R$, $x \in \mathfrak{g}$

(i) $ad x^{(p)} = (ad x)^{p}$, for $x \in \mathfrak{g}$

(ii) $(x_{0} + x_{1})^{(p)} = x^{(p)}_{0} + x^{(p)}_{1} - \sum_{0 < r < p} \sum_{t} (1/r) [x_{t(1)} x_{t(2)}
\cdot\cdot\cdot x_{t(p-1)}, x_{1}] \cdot\cdot\cdot$

<!-- original page 447 -->

where $t$ ranges over the maps $[1, p-1] \to {0, 1}$ taking the value `0` exactly $r$ times ($x_{0}, x_{1} \in
\mathfrak{g}$). The map $x \mapsto x^{(p)}$ will then be called the "*symbolic $p$-th power*".

For example, if $A$ is an associative $R$-algebra, we saw in 5.1 that one obtains a $p$-Lie algebra, which we shall
denote $A_{Lie}$, by taking the $R$-module underlying $A$ and setting, for $x, y \in A$,

```text
[x, y] = xy − yx    and    x^{(p)} = x^p.
```

We shall say that $A_{Lie}$ is the $p$-Lie algebra underlying $A$.

In what follows we shall consider mostly sub-$p$-Lie algebras of $p$-algebras of the form $A_{Lie}$; here is an example:
let $S$ be a scheme of characteristic $p > 0$ and $X$ an $S$-scheme. Recall that a derivation of $X$ over $S$ is an
endomorphism $D$ of the sheaf of abelian groups `O_X` such that

```text
D(λ · s) = λ · D(s)    and    D(st) = (Ds) t + s (Dt)
```

when $\lambda$ and `s, t` range over the sections of `O_S` and of `O_X` on opens such that the formulas make sense.
Leibniz's formula

```text
D^n(st) = ∑_{i=0}^n (n choose i) (D^i s)(D^{n−i} t)
```

shows that $D^{p}$ is again a derivation of $X$ over $S$, taking into account the equality $(p choose i) \equiv 0 (mod
p)$ for $i \neq 0, p$. It follows that:

> The algebra $D\acute{e}r_{X/S}$ of derivations of $X$ over $S$ is a sub-$p$-Lie algebra of the $\Gamma(S,
> O_{S})$-algebra of differential operators of $X$ over $S$.

#### 5.2.1

<!-- label: III.VII_A.5.2.1 -->

If $\mathfrak{g}$ and $\mathfrak{h}$ are two $p$-Lie algebras, a *homomorphism* $h : \mathfrak{g} \to \mathfrak{h}$ is
an $R$-linear map from $\mathfrak{g}$ into $\mathfrak{h}$ such that $h([x, y]) = [h(x), h(y)]$ and $h(x^{(p)}) =
h(x)^{(p)}$ if $x, y \in \mathfrak{g}$. The composition of two homomorphisms is again a homomorphism, so that we may
speak of the *category of $p$-Lie algebras* over $R$.

If $(X, R)$ is a ringed space, we shall say that an $R$-module $\mathfrak{g}$ is equipped with a structure of $p$-Lie
algebra over $R$ if, for every open $U$, $\Gamma(U, \mathfrak{g})$ is equipped with a structure of $p$-Lie algebra over
$\Gamma(U, R)$ <!-- original page 448 --> and if the restrictions are homomorphisms.

### 5.3

<!-- label: III.VII_A.5.3 -->

We are now interested in the left adjoint functor to the functor $A \mapsto A_{Lie}$ of 5.2. Let $\mathfrak{g}$ be a
$p$-Lie algebra over the ring $R$ of characteristic $p$, $U(\mathfrak{g})$ the enveloping algebra of the Lie algebra
underlying $\mathfrak{g}$ (cf. [BLie], I § 2.1) and $i_{\mathfrak{g}}$ (or simply $i$) the canonical map $\mathfrak{g}
\to U(\mathfrak{g})$.

Let $A$ be a unital associative $R$-algebra. One knows that, for every Lie algebra homomorphism $\phi : \mathfrak{g} \to
A_{Lie}$ there exists a unique homomorphism of unital $R$-algebras $\psi : U(\mathfrak{g}) \to A$ such that $\psi \circ
i = \phi$. Moreover, $\phi$ is a $p$-Lie algebra homomorphism if and only if $\psi$ vanishes on the elements $i(x)^{p} -
i(x^{(p)})$, when $x$ ranges over $\mathfrak{g}$.

**Definition.** *One denotes by $U^{R}_{p}(\mathfrak{g})$ or simply $U_{p}(\mathfrak{g})$ the quotient of
$U(\mathfrak{g})$ by the two-sided ideal generated by the elements $i(x)^{p} - i(x^{(p)})$, and $j_{\mathfrak{g}}$ (or
simply $j$) the map $\mathfrak{g} \to U_{p}(\mathfrak{g})$ composed of $i : \mathfrak{g} \to U(\mathfrak{g})$ and the
canonical map $U(\mathfrak{g}) \to U_{p}(\mathfrak{g})$. One says that $U_{p}(\mathfrak{g})$ is the* restricted
enveloping algebra *of $\mathfrak{g}$.*

According to what precedes, one has the

**Proposition.** *For every unital associative $R$-algebra and every $p$-Lie algebra morphism $\phi : \mathfrak{g} \to
A_{Lie}$, there exists a unique homomorphism of unital algebras $\psi : U_{p}(\mathfrak{g}) \to A$ such that $\psi \circ
j = \phi$. In other words, the functor $\mathfrak{g} \mapsto U_{p}(\mathfrak{g})$ is left adjoint to the forgetful
functor $A \mapsto A_{Lie}$.*

#### 5.3.1

<!-- label: III.VII_A.5.3.1 -->

With the notations of 5.3, set now $\beta(x) = i(x)^{p} - i(x^{(p)})$. For every element $y$ of $\mathfrak{g}$, one has,
according to 5.1 (i) and 5.2 (i):

```text
β(x) i(y) = i(y) β(x) + [β(x), i(y)]
          = i(y) β(x) + (ad i(x))^p i(y) − i((ad x)^p y)
          = i(y) β(x),
```

<!-- original page 449 -->

so $\beta(x)$ belongs to the center of $U(\mathfrak{g})$; in particular, the left ideal generated by the elements
$\beta(x)$ is already two-sided.

On the other hand, it is clear that $\beta(\lambda x) = \lambda^{p} \beta(x)$, for $\lambda \in R$, and it follows from
5.1 (ii) and 5.2 (ii) that, for $x, y \in \mathfrak{g}$,

```text
β(x + y) = β(x) + β(y).
```

In particular, if $(x_{\alpha})$ is a family of generators of the $R$-module $\mathfrak{g}$, the left ideal generated by
the elements $\beta(x)$ is already generated by the $\beta(x_{\alpha})$.

#### 5.3.2. Proposition

<!-- label: III.VII_A.5.3.2 -->

[^N.D.E-VII_A-53] *Let $\mathfrak{g}$ be an $R$-Lie algebra whose underlying $R$-module is free with basis
$(x_{\alpha})$. Then the structures of $p$-Lie algebra on $\mathfrak{g}$ correspond bijectively to the families
$(y_{\alpha})$ of $\mathfrak{g}$ such that $ad y_{\alpha} = (ad x_{\alpha})^{p}$.*

Indeed, if $\mathfrak{g}$ is equipped with a structure of $p$-Lie algebra $x \mapsto x^{(p)}$, then according to 5.2 (i)
and (0), (ii), the $y_{\alpha} = x^{(p)}_{\alpha}$ satisfy $ad y_{\alpha} = (ad x_{\alpha})^{p}$, and determine the
$p$-Lie algebra structure.

Let us prove the converse. Since $\mathfrak{g}$ is a free $R$-module, the canonical map $i : \mathfrak{g} \to
U(\mathfrak{g})$ is injective, according to the Poincaré–Birkhoff–Witt theorem (cf. [BLie], I § 2.7), so one can
identify $\mathfrak{g}$ with an $R$-submodule of $U(\mathfrak{g})$. Suppose that $(y_{\alpha})$ is a family of elements
of $\mathfrak{g}$ such that $ad y_{\alpha} = (ad x_{\alpha})^{p}$. Let $\pi$ be the map $r \mapsto r^{p}$ from $R$ into
$R$, and let $\mathfrak{g} \otimes_{\pi} R$ be the $R$-Lie algebra obtained by extension of scalars $\pi : R \to
R$.[^N.D.E-VII_A-54]

There then exists an $R$-linear map $\gamma$ from $\mathfrak{g} \otimes_{\pi} R$ into $U(\mathfrak{g})$ which sends
$x_{\alpha} \otimes_{\pi} 1$ to $x^{p}_{\alpha} - y_{\alpha}$; moreover, since one has, for every $x \in \mathfrak{g}$,

```text
(ad x_α^p)(x) = (ad x_α)^p(x) = (ad y_α)(x),
```

$\gamma$ maps $\mathfrak{g} \otimes_{\pi} R$ into the center of $U(\mathfrak{g})$. Set, for every $x \in \mathfrak{g}$:

```text
x^{(p)} = x^p − γ(x ⊗_π 1).
```

Then, for every $\alpha$, one has $x^{(p)}_{\alpha} = y_{\alpha}$. If $x = \sum \lambda_{\alpha} x_{\alpha}$, one
deduces from 5.1 (ii) (by induction on the number of indices $\alpha$ such that $\lambda_{\alpha} \neq 0$), that

<!-- original page 477 -->

```text
x^p − ∑_α λ_α^p x_α^p ∈ 𝔤;
```

denoting this element by $z$, one then has $x^{(p)} = \sum \lambda^{p}_{\alpha} y_{\alpha} + z$ and therefore $x^{(p)}
\in \mathfrak{g}$.

It is clear that the map $x \mapsto x^{(p)}$ satisfies $(\lambda x)^{(p)} = \lambda^{p} x^{(p)}$. Moreover, since
$\gamma(x \otimes_{\pi} 1)$ is central, then $ad x^{(p)} = ad x^{p}$ and therefore, according to Jacobson's first
formula (5.1 (i)), one has

```text
ad x^{(p)} = (ad x)^p.
```

Finally, according to Jacobson's second formula (5.1 (ii)), the map $x \mapsto x^{(p)}$ satisfies condition (ii) of 5.2.
It therefore makes $\mathfrak{g}$ a $p$-Lie algebra. This proves the proposition.

#### 5.3.3. Proposition

<!-- label: III.VII_A.5.3.3 -->

*Let $\mathfrak{g}$ be a $p$-Lie algebra over $R$ whose underlying module is free with basis $(x_{\alpha})$. Then the
map $j : \mathfrak{g} \to U_{p}(\mathfrak{g})$ is injective and, if one sets $z_{\alpha} = j(x_{\alpha})$, then
$U_{p}(\mathfrak{g})$ has as basis the monomials*

```text
∏_α z_α^{n_α}    where    0 ⩽ n_α < p,
```

*(the $n_{\alpha}$ are assumed to be zero except for a finite number of them; one assumes the basis to be totally
ordered and the products to be performed in increasing order).*

Indeed, identify $\mathfrak{g}$ with a submodule of the enveloping algebra $U(\mathfrak{g})$ by means of the canonical
map $i$. For every family $n = (n_{\alpha})$ of natural integers, zero except for a finite number of them, set

```text
|n| = ∑_α n_α    and    x^n = ∏_α x_α^{n_α}.
```

<!-- original page 450 -->

Writing $n_{\alpha} = m_{\alpha} + p \ell_{\alpha}$, with $0 \leqslant m_{\alpha} < p$, set also

```text
T_n = ∏_α x_α^{m_α} β(x_α)^{ℓ_α}
```

where $\beta(x) = x^{p} - x^{(p)}$ is the map $\mathfrak{g} \to U(\mathfrak{g})$ defined in 5.3.1.

For every $r \in \mathbb{N}$, denote by $U_{r}$ the sub-$R$-module of $U(\mathfrak{g})$ generated by the $x^{n}$ such
that $|n| \leqslant r$. Since the graded ring $\bigoplus_{r} U_{r} / U_{r-1}$ is commutative (cf. [BLie], I § 2.6), one
sees that, for every $n$:

```text
T_n − ∏_α x_α^{n_α} ∈ U_{|n| − 1}.
```

For every $s \in \mathbb{N}$, the $x^{n}$ such that $|n| = s$ form, according to the Poincaré–Birkhoff–Witt theorem
(loc. cit., § 2.7), a basis of $U_{s} / U_{s-1}$, and therefore the same holds for the $T_{n}$ such that $|n| = s$.

Therefore, when $s = |n|$ varies, the $T_{n}$ form a basis of $U(\mathfrak{g})$. Now the kernel $J$ of the canonical map
$U(\mathfrak{g}) \to U_{p}(\mathfrak{g})$ is the left ideal of $U(\mathfrak{g})$ generated by the central elements $\beta(x_{\alpha})$ (5.3.1). Consequently, the $T_{n}$
such that $\ell = (\ell_{\alpha}) \neq 0$ <!-- original page 478 --> form a basis of $J$, and the $T_{n}$ such that $n_{\alpha} < p$ for every
$\alpha$, form a basis of $U_{p}(\mathfrak{g}) = U(\mathfrak{g}) / J$.

#### 5.3.3 bis

<!-- label: III.VII_A.5.3.3-bis -->

Let $\mathfrak{g}$ be a $p$-Lie algebra over $R$ and $f : R \to R'$ an extension of the base ring. I claim that there
exists on the $R'$-module $R' \otimes_{R} \mathfrak{g}$ a $p$-Lie algebra structure and only one such that

```text
(∗)    [λ ⊗ x, μ ⊗ y] = λμ ⊗ [x, y]    and    (λ ⊗ x)^{(p)} = λ^p ⊗ x^{(p)}.
```

It will follow, in particular, that the functor $\mathfrak{g} \mapsto R' \otimes_{R} \mathfrak{g}$ is left adjoint to
the functor "restriction of scalars from $R'$ to $R$".

The uniqueness of the $p$-Lie algebra structure defined by $(\ast)$ being clear, let us prove existence. When
$\mathfrak{g}$ is free with basis $(x_{\alpha})$ there exists, according to 5.3.2, one and only one $p$-Lie algebra
structure on the Lie algebra $R' \otimes_{R} \mathfrak{g}$ such that

$$ (1 \otimes x_{\alpha})^{(p)} = 1 \otimes x^{(p)}_{\alpha}; $$

this structure is the one we seek.

When $\mathfrak{g}$ is an arbitrary $p$-Lie algebra, there exists a $p$-Lie algebra `L_0` free (as an $R$-module) and a
surjective homomorphism $q_{0} : L_{0} \to \mathfrak{g}$; it suffices for example to take for `L_0` the $p$-Lie algebra
$R \otimes_{\mathbb{F}_{p}} \mathfrak{g}$, where $\mathbb{F}_{p}$ denotes the prime field <!-- original page 451 --> of
characteristic $p$, and for $q_{0}$ the homomorphism $\lambda \otimes x \mapsto \lambda x$ ($\mathfrak{g}$ is free over
$\mathbb{F}_{p}$!). The kernel of $q_{0}$ is then a $p$-ideal of `L_0`, i.e., an ideal of the Lie algebra `L_0` which is
stable under the endomorphism $x \mapsto x^{(p)}$; there is therefore also a $p$-Lie algebra `L_1` free (as an
$R$-module) and a homomorphism $q_{1} : L_{1} \to L_{0}$ whose image is $Ker q_{0}$, whence the exact sequence:

```text
L_1 ──q_1→ L_0 ──q_0→ 𝔤 ──→ 0.
```

One deduces from this an exact sequence of $R'$-Lie algebras

```text
R' ⊗_R L_1 ──R' ⊗_R q_1→ R' ⊗_R L_0 ──R' ⊗_R q_0→ R' ⊗_R 𝔤 ──→ 0.
```

Since $R' \otimes_{R} q_{1}$ is manifestly a homomorphism of $p$-Lie algebras, the kernel of $R' \otimes_{R} q_{0}$ is a
$p$-ideal, so that the symbolic $p$-th power operation of $R' \otimes_{R} L_{0}$ induces by passage to the quotient a
map from $R' \otimes_{R} \mathfrak{g}$ into $R' \otimes_{R} \mathfrak{g}$ (use formula (ii) of 5.2); this last one
equips $R' \otimes_{R} \mathfrak{g}$ with the $p$-Lie algebra structure sought.

### 5.3.4

<!-- label: III.VII_A.5.3.4 -->

The canonical map $j_{\mathfrak{g}} : \mathfrak{g} \to U_{p}(\mathfrak{g})$ induces, for every extension $R \to R'$ of
the base ring, a homomorphism

```text
R' ⊗_R j_𝔤 : R' ⊗_R 𝔤 ⟶ R' ⊗_R U_p(𝔤),
```

whence a homomorphism

```text
h : U_p(R' ⊗_R 𝔤) ⟶ R' ⊗_R U_p(𝔤)
```

such that $h \circ j_{R' \otimes \mathfrak{g}} = R' \otimes_{R} j_{\mathfrak{g}}$. It obviously follows from the
universal properties of $R' \otimes_{R} \mathfrak{g}$ and the restricted enveloping algebra that $h$ is an isomorphism,
which will allow us to identify $U_{p}(R' \otimes_{R} \mathfrak{g})$ with $R' \otimes_{R} U_{p}(\mathfrak{g})$.

In particular, if $r$ is an element of $R$ and if $R'$ is the localized ring $R_{r}$, one sees that
$\mathfrak{g}_{r} = R_{r} \otimes_{R} \mathfrak{g}$ is equipped canonically with a structure of $p$-Lie algebra over
$R_{r}$, <!-- original page 452 --> so that the sheaf $\tilde{\mathfrak{g}}$ on $\operatorname{Spec} R$ is a
quasi-coherent $p$-Lie algebra on $\operatorname{Spec} R$. Moreover, the restricted enveloping algebra
$U^{R_{r}}_{p}(\mathfrak{g}_{r})$ is identified with $U^{R}_{p}(\mathfrak{g})_{r}$, so that the sheaf associated with
the presheaf $V \mapsto U_{p}(\Gamma(V, \tilde{\mathfrak{g}}))$ is quasi-coherent.

**Definition.** *More generally, if $S$ is a scheme of characteristic $p$ and $\mathcal{G}$ a quasi-coherent $p$-Lie
algebra on `O_S`, the sheaf associated with the presheaf $V \mapsto U_{p}(\Gamma(V, \mathcal{G}))$ is quasi-coherent; it
will be denoted $\mathcal{U}_{p}(\mathcal{G})$ and called the* restricted enveloping algebra *of $\mathcal{G}$. If $V$
is affine, $U_{p}(\Gamma(V, \mathcal{G}))$ is identified with $\Gamma(V, \mathcal{U}_{p}(\mathcal{G}))$.*

### 5.4

<!-- label: III.VII_A.5.4 -->

The universal character of $U_{p}(\mathfrak{g})$ entails that $U_{p}(\mathfrak{g})$ is functorial in $\mathfrak{g}$:
every homomorphism of $p$-Lie algebras $\phi : \mathfrak{g} \to \mathfrak{h}$ induces a homomorphism of unital algebras
$U_{p}(\phi)$ and only one such that $j_{\mathfrak{h}} \circ \phi = U_{p}(\phi) \circ j_{\mathfrak{g}}$. Here are some
examples:

a) If $\mathfrak{h} = 0$, $U_{p}(\mathfrak{h})$ is identified with the base ring and $U_{p}(\phi)$ is an algebra
homomorphism $\epsilon_{\mathfrak{g}} : U_{p}(\mathfrak{g}) \to R$ called the *augmentation*.

b) Now take for $\mathfrak{h}$ the algebra $\mathfrak{g}^{\circ}$ opposite to $\mathfrak{g}$, i.e.,
$\mathfrak{g}^{\circ}$ has the same underlying module as $\mathfrak{g}$, the same symbolic $p$-th power, the bracket of
two elements in $\mathfrak{g}^{\circ}$ being the opposite of the bracket in $\mathfrak{g}$. It is clear that we can
identify $U_{p}(\mathfrak{g}^{\circ})$ with the algebra opposite to $U_{p}(\mathfrak{g})$. Moreover, the isomorphism $x
\mapsto -x$ of $\mathfrak{g}$ onto $\mathfrak{g}^{\circ}$ induces an isomorphism $c_{\mathfrak{g}}$ of
$U_{p}(\mathfrak{g})$ onto $U_{p}(\mathfrak{g}^{\circ}) \simeq U_{p}(\mathfrak{g})^{\circ}$. One says that
$c_{\mathfrak{g}}$ is the *antipode* of $U_{p}(\mathfrak{g})$.

c) Let finally $\mathfrak{f}$ and $\mathfrak{g}$ be two $p$-Lie algebras and $\mathfrak{h}$ the $p$-Lie algebra product
$\mathfrak{f} \times \mathfrak{g}$ which has as underlying $R$-module the direct product $\mathfrak{f} \times
\mathfrak{g}$, the bracket and the symbolic $p$-th power being defined by the formulas

```text
[(x, y), (x', y')] = ([x, x'], [y, y'])    and    (x, y)^{(p)} = (x^{(p)}, y^{(p)}).
```

If $h_{1} : \mathfrak{f} \to \mathfrak{k}$ and $h_{2} : \mathfrak{g} \to \mathfrak{k}$ are two $p$-Lie algebra
homomorphisms <!-- original page 453 --> such that $[h_{1}(x), h_{2}(y)] = 0$ for every $x$ of $\mathfrak{f}$ and every
$y$ of $\mathfrak{g}$, the map $h_{1} + h_{2} : (x, y) \to h_{1}(x) + h_{2}(y)$ is a $p$-Lie algebra homomorphism;
conversely, every homomorphism from $\mathfrak{f} \times \mathfrak{g}$ into $\mathfrak{k}$ is of this type, which allows
us to characterize $\mathfrak{f} \times \mathfrak{g}$ as the solution of a universal problem. For example, the maps

```text
h_1 : x ↦ i_𝔣(x) ⊗ 1    and    h_2 : y ↦ 1 ⊗ i_𝔤(y)
```

induce a homomorphism $h_{1} + h_{2}$ from $\mathfrak{f} \times \mathfrak{g}$ into the $p$-Lie algebra underlying
$U_{p}(\mathfrak{f}) \otimes U_{p}(\mathfrak{g})$. It follows from the universal characters of $\mathfrak{f} \times
\mathfrak{g}$ and of the restricted enveloping algebras that $h_{1} + h_{2}$ extends to an isomorphism:

```text
φ : U_p(𝔣 × 𝔤) ⥲ U_p(𝔣) ⊗ U_p(𝔤).
```

**Definition.** *If $\mathfrak{f} = \mathfrak{g}$, the diagonal map $\delta : x \mapsto (x, x)$ of $\mathfrak{g}$ into
$\mathfrak{g} \times \mathfrak{g}$ induces a homomorphism of $U_{p}(\mathfrak{g})$ into $U_{p}(\mathfrak{g} \times
\mathfrak{g})$. We shall denote by `∆_𝔤` the composition of this homomorphism with the isomorphism $\phi :
U_{p}(\mathfrak{g} \times \mathfrak{g}) \xrightarrow{\sim} U_{p}(\mathfrak{g}) \otimes
U_{p}(\mathfrak{g})$.*[^N.D.E-VII_A-55]

One then sees easily that `∆_𝔤` and the multiplication of the algebra $U_{p}(\mathfrak{g})$ make $U_{p}(\mathfrak{g})$
an $R$-coalgebra in groups (cf. 3.2) which has $\epsilon_{\mathfrak{g}}$ as augmentation and $c_{\mathfrak{g}}$ as
antipode.

### 5.5

<!-- label: III.VII_A.5.5 -->

[^N.D.E-VII_A-56] Let now $S$ be a scheme of characteristic $p$. First, if $\mathcal{U}$ is an `O_S`-coalgebra in groups
and $G$ the group $S$-functor $\operatorname{Spec}^{*} \mathcal{U}$, we saw (3.2.3) that, for every $T \to S$,
`(Lie G)(T)` is the Lie subalgebra of $\Gamma(T, \mathcal{U}_{T})$ formed by the primitive elements. Now, if $x$ is such
an element, one has `∆(x^p) = x^p ⊗ 1 + 1 ⊗ x^p` (since $(p choose i) = 0 mod p$ for $0 < i < p$), i.e. $x^{p}$ is again
a primitive element. It follows, according to 5.1 and 5.2, that the map $x \mapsto x^{p}$ equips `(Lie G)(T)` with a
structure of $O(T)$-$p$-Lie algebra.

Let now $\mathcal{L}$ be an `O_S`-$p$-Lie algebra, quasi-coherent on `O_S`. When $V$ ranges over the opens of $S$, the
structures of group coalgebras previously defined on the sets $U_{p}(\Gamma(V, \mathcal{L}))$ induce on the associated
sheaf, i.e., on the restricted enveloping algebra $\mathcal{U}_{p}(\mathcal{L})$, a structure of `O_S`-coalgebra in
groups. Moreover, <!-- original page 480 --> for every $S$-scheme $T$, one has an isomorphism
$\mathcal{U}_{p}(\mathcal{L}_{T}) \xrightarrow{\sim} \mathcal{U}_{p}(\mathcal{L})_{T}$.

Denote by $Prim \mathcal{U}_{p}(\mathcal{L})$ the subpresheaf of $\mathcal{U}_{p}(\mathcal{L})$ associating with every
open $V$ the set of primitive elements of $\mathcal{U}_{p}(\mathcal{L})(V)$; one sees easily that this is a sheaf. When
$V$ ranges over the opens of $S$, the composed maps

```text
Γ(V, ℒ) ──j→ Prim U_p(Γ(V, ℒ)) ──→ Prim 𝒰_p(ℒ)(V)
```

define a morphism $\mathcal{L} \to Prim \mathcal{U}_{p}(\mathcal{L})$, which we shall again denote $j$ or
$j_{\mathcal{L}}$, and this defines further a morphism of `O_S`-$p$-Lie algebras $\mathcal{W}(\mathcal{L}) \to Prim
\mathcal{W}(\mathcal{U}_{p}(\mathcal{L}))$ (cf. 3.2.3).

**Proposition 5.5.1.** *Let $\mathcal{L}$ be an `O_S`-$p$-Lie algebra, locally free as an `O_S`-module. Then
$j_{\mathcal{L}}$ induces an isomorphism of `O_S`-$p$-Lie algebras:*

<!-- label: III.VII_A.5.5.1 -->

$$ \mathcal{W}(\mathcal{L}) \xrightarrow{\sim} Prim \mathcal{W}(\mathcal{U}_{p}(\mathcal{L})). $$

*Proof.* Let $T$ be an $S$-scheme; taking into account the identification $\mathcal{U}_{p}(\mathcal{L}_{T}) =
\mathcal{U}_{p}(\mathcal{L})_{T}$, the task is to show that the map $\Gamma(T, \mathcal{L}_{T}) \to Prim \Gamma(T,
\mathcal{U}_{p}(\mathcal{L}_{T}))$ is bijective. Replacing $S$ by $T$, one is reduced to the case where $T = S$, and it
then suffices to show that the morphism of sheaves $j_{\mathcal{L}} : \mathcal{L} \to Prim \mathcal{U}_{p}(\mathcal{L})$
is an isomorphism. This question being local on $S$, we may suppose that $S$ is affine with ring $R$ and that
$\mathcal{L}$ is the sheaf associated with an $R$-$p$-Lie algebra $L$ with basis $(x_{\alpha})$. As in 5.3.3, denote by
$z_{\alpha}$ the image of $x_{\alpha}$ in $U = U_{p}(L)$ and, for every family $n = (n_{\alpha})$ of integers between
`0` and $p - 1$, zero except for a finite number of them, denote $z^{(n)}$ the product

$$ \prod_{\alpha} z^{n_{\alpha}}_{\alpha} / n_{\alpha}! $$

<!-- original page 481 -->

(one supposes the basis $(x_{\alpha})$ totally ordered and the products performed in increasing order).

Since `∆(z_α) = z_α ⊗ 1 + 1 ⊗ z_α`, one sees easily that

```text
∆(z^{(n)}) = ∑_r z^{(n−r)} ⊗ z^{(r)}
```

the sum being taken over the (finite!) set of $r$ such that $0 \leqslant r_{\alpha} \leqslant n_{\alpha}$ for every
$\alpha$. Since the $z^{(n)}$ (resp. the $z^{(n)} \otimes z^{(m)}$) form a basis of $U$ (resp. of $U \otimes U$), one
deduces that an element $u$ of $U$ satisfies `∆(u) = u ⊗ 1 + 1 ⊗ u` if and only if $u$ is a linear combination of the
$z_{\alpha}$. This proves 5.5.1.

**Remark 5.5.2.** *Recall (cf. 3.2.2 and 3.2.3), that the group $S$-functor $G = \operatorname{Spec}^{*}
\mathcal{U}_{p}(\mathcal{L})$ is very good and that $Lie(G) = Prim \mathcal{W}(\mathcal{U}_{p}(\mathcal{L}))$. The
preceding proposition therefore signifies that $j_{\mathcal{L}}$ induces an isomorphism $\mathcal{W}(\mathcal{L})
\xrightarrow{\sim} Lie(G)$.*

<!-- label: III.VII_A.5.5.2 -->

If one supposes moreover that $\mathcal{L}$ is a locally free `O_S`-module of finite rank, then
$\mathcal{U}_{p}(\mathcal{L})$ is finite locally free over `O_S`, according to 5.3.3, so $\operatorname{Spec}^{*}
\mathcal{U}_{p}(\mathcal{L})$ is represented by the $S$-group $\mathfrak{G}_{p}(\mathcal{L}) = \operatorname{Spec}
\mathcal{U}_{p}(\mathcal{L})^{*}$ (cf. 3.2.2.1), and one obtains the following more precise proposition:

**Proposition 5.5.3.** *Let $\mathcal{L}$ be an `O_S`-$p$-Lie algebra, locally free of finite rank as an `O_S`-module,
let $\mathcal{A} = \mathcal{U}_{p}(\mathcal{L})^{*}$ and let $G = \mathfrak{G}_{p}(\mathcal{L})$ be the affine $S$-group
$\operatorname{Spec} \mathcal{A}$.*

<!-- label: III.VII_A.5.5.3 -->

*(i) $j_{\mathcal{L}}$ induces an isomorphism $\mathcal{W}(\mathcal{L}) \xrightarrow{\sim} Lie(G)$ of `O_S`-$p$-Lie
algebras.*

*(ii) Let $\mathcal{I}$ be the augmentation ideal of $\mathcal{A}$ and $\omega_{G} = \mathcal{I} / \mathcal{I}^{2}$ (cf.
II, 4.11.4). Then $\omega_{G}$ is identified with $\mathcal{L}^{*} = \operatorname{Hom}_{O_{S}}(\mathcal{L}, O_{S})$,
hence is a locally free `O_S`-module of finite rank (and one has $\omega^{*}_{G/S} = \mathcal{L}$).*

*Proof.* (i) following from 5.5.2, let us prove (ii). Denote by $\eta_{\mathcal{U}}$ and $\epsilon_{\mathcal{U}}$ the
unit section and the augmentation of $\mathcal{U} = \mathcal{U}_{p}(\mathcal{L})$, by $\eta_{\mathcal{A}}$ and
$\epsilon_{\mathcal{A}}$ those of $\mathcal{A}$, and $\mathcal{J} = Ker \epsilon_{\mathcal{U}}$. Then one has:

$$ (1) \mathcal{U} = \eta_{\mathcal{U}}(O_{S}) \oplus \mathcal{J}. $$

Let $\delta$ be the morphism defined by the diagram below, where $\tau$ and $\pi$ denote the inclusion and the
projection deduced from the decomposition (1):

```text
       𝒥  ──────────δ─────────→  𝒥 ⊗ 𝒥
       │                           ▲
     τ │                           │ π
       ▼            ∆               │
       𝒰  ──────────────────────→  𝒰 ⊗ 𝒰
```

then one has an exact sequence:

```text
(∗)        0  ──→  ℒ^*  ──j_ℒ→  𝒥  ──δ→  𝒥 ⊗ 𝒥.
```

Moreover, according to 5.3.3, the `O_S`-module $\mathcal{J} / \mathcal{L}$ is locally free and, according to 5.5.1, the
sequence $(\ast)$ remains exact after every base change. So, according to [BAC], II § 3, <!-- original page 482 -->
prop. 6, $\delta$ induces an isomorphism of $\mathcal{J} / \mathcal{L}$ onto a submodule $Q$ locally direct factor of
$\mathcal{J} \otimes \mathcal{J}$. It follows that $(\ast)$ gives by duality the exact sequence:

```text
(∗∗)        0  ←──  ℒ  ←──ᵗj_ℒ──  ℐ  ←──ᵗδ──  ℐ ⊗ ℐ.
```

Now the decomposition (1) corresponds by duality to the decomposition:

$$ (2) \mathcal{A} = \eta_{\mathcal{A}}(O_{S}) \oplus \mathcal{I} $$

and the transpose of `∆` is the multiplication $m_{\mathcal{A}} : \mathcal{A} \otimes \mathcal{A} \to \mathcal{A}$.
Since $\mathcal{I}$ is an ideal of $\mathcal{A}$, $m_{\mathcal{A}}$ sends $\mathcal{I} \otimes \mathcal{I}$ into
$\mathcal{I}$; more precisely, taking into account decomposition (2), one has a commutative square

```text
                            m'
       ℐ  ←──────────  ℐ ⊗ ℐ
       │                  │
     ᵗτ                  ᵗπ
       ▼            m_𝒜    ▼
       𝒜  ←──────────  𝒜 ⊗ 𝒜
```

which shows that the restriction $m'$ of $m_{\mathcal{A}}$ to $\mathcal{I} \otimes \mathcal{I}$ is the transpose of
$\delta$. The exact sequence $(\ast\ast)$ then gives $\mathcal{I} / \mathcal{I}^{2} \simeq \mathcal{L}^{*}$, and the
proposition follows.

## 6. $p$-Lie algebra of an $S$-group scheme

<!-- label: III.VII_A.6 -->

<!-- original page 454 -->

Let $S$ be a scheme of characteristic $p > 0$. In paragraph 5.5 we associated with every quasi-coherent `O_S`-$p$-Lie
algebra $\mathcal{L}$ a group $S$-functor $\mathfrak{G}_{p}(\mathcal{L}) = \operatorname{Spec}^{*}
\mathcal{U}_{p}(\mathcal{L})$. We shall now see that, for every $S$-group scheme $G$, the `O_S`-Lie algebra $Lie(G/S)$
defined in II 4.11 is naturally equipped with a structure of `O_S`-$p$-Lie algebra.

### 6.1

<!-- label: III.VII_A.6.1 -->

Let us first identify $Lie(G/S)(S)$ and $Lie(\operatorname{Aut} G/S)(S)$ respectively with Lie subalgebras of $U(G)$ and
$Dif_{G/S}$ by means of the injections $\alpha$ and $\beta$ of 2.5; $Lie(\operatorname{Aut} G/S)(S)$ is therefore
identified with the $\Gamma(O_{S})$-Lie algebra of $S$-derivations of `O_G`. According to 5.2, this latter is a
sub-$p$-Lie algebra of $Dif_{G/S}$.

On the other hand, the image of $L = Lie(G/S)(S)$ by the injective algebra morphism $\ell : U(G) \to Dif_{G/S}$, $d
\mapsto {}_{G} d$, is formed by the left-invariant derivations (cf. 2.2, N.D.E. (17), 2.4 and 2.5). If $x$ belongs to
$L$, $\ell(x)^{p}$ is none other than $\ell(x^{p})$, according to loc. cit. Since $\ell(x)^{p}$ is again a derivation,
one sees that $x^{p}$ belongs to $Lie(G/S)(S)$. Therefore:[^N.D.E-VII_A-57]

> $Lie(G/S)(S)$ is a sub-$p$-Lie algebra of the infinitesimal algebra $U(G)$.

#### 6.1.1

<!-- label: III.VII_A.6.1.1 -->

Let $\phi : G \to H$ be a homomorphism of $S$-group schemes. It is clear that the homomorphisms $Lie(\phi/S)(S)$ and
$U(\phi)$ are compatible with the identifications of $Lie(G/S)(S)$ and $Lie(H/S)(S)$ with sub-$p$-Lie algebras of $U(G)$
and $U(H)$. Since $U(\phi)$ is an algebra homomorphism, one sees therefore that $Lie(\phi/S)(S)$ is a homomorphism of
$p$-Lie algebras.

Similarly, if $s : T \to S$ is a base change, the map from $Lie(G/S)(S)$ into $Lie(G/S)(T)$, which is induced by $s$, is
a homomorphism of $p$-Lie algebras. One can translate this by saying that the functor $Lie(G/S)$ is equipped with a
structure of `O_S`-$p$-Lie algebra. In particular, when $T$ ranges over the opens of $S$, one sees that

<!-- original page 455 --> the sheaf `Lie(G/S)` is equipped with a structure of `O_S`-`p`-Lie algebra.

### 6.2

<!-- label: III.VII_A.6.2 -->

Following an idea of Demazure, we shall now generalize what precedes to certain group $S$-functors not necessarily
representable. For this, we shall first give another definition of the symbolic $p$-th power in the Lie algebra of an
$S$-group scheme $G$.

Let $D$ be a derivation of $G$ at the origin;[^N.D.E-VII_A-58] according to 1.2.1, $D$ is the composition of the
$S$-derivation $\delta = (\tau, \partial_{t})$ of the zero section $\tau : S \to I_{S}$, and a morphism $x : I_{S} \to
G$ such that $x \circ \tau = \epsilon$ (i.e. $x \in Lie(G/S)(S)$). According to the definition we gave in 2.1, $D^{p}$
is the following composed deviation:

```text
S ≃ S × S × ··· × S ──δ × ··· × δ→ I_S × ··· × I_S ──x × ··· × x→ G × ··· × G ──m^{(p)}→ G
```

($p$ copies), where $m^{(p)}$ is the morphism induced by the multiplication $m : G \times G \to G$. Since $I_{S} \times
\cdot\cdot\cdot \times I_{S}$ is affine over $S$ and has as affine algebra $B = O_{S}[d_{1}, \cdots, d_{p}] /
(d^{2}_{1}, \cdots, d^{2}_{p})$, the deviation $\delta \times \cdot\cdot\cdot \times \delta$ is defined by the morphism
of `O_S`-modules

$$ \phi : B \longrightarrow O_{S} $$

which sends to `1` the monomial $d_{1} d_{2} \cdot\cdot\cdot d_{p}$, and to `0` the other monomials $d_{i_{1}}
\cdot\cdot\cdot d_{i_{r}}$, for $0 \leqslant r < p$. On the other hand, if $pr_{i}$ denotes the projection of
$I^{p}_{S}$ onto the $i$-th factor and if $x_{i}$ is the image in $G(I^{p}_{S})$ of $x$ by $G(pr_{i})$, then the
composed morphism $m^{(p)} \circ (x \times \cdot\cdot\cdot \times x)$ is none other than the product $x_{1} x_{2}
\cdot\cdot\cdot x_{p}$. Consequently, $D^{p}$ is also the following composed deviation:

```text
S ──δ × ··· × δ→ I_S × ··· × I_S ──x_1 x_2 ··· x_p→ G.
```

This description allows us to re-prove that $D^{p}$ is a derivation of $G$ at the origin. <!-- original page 456 -->
Indeed, since $G$ is a very good group (II 4.11), the images $G(pr_{1})(x)$ and $G(pr_{2})(x)$ of $x$ in $G(I_{S} \times
I_{S})$ commute with each other. It follows that the elements $x_{i}$ of $G(I^{p}_{S})$ commute pairwise and therefore,
for every permutation $\gamma$ of the factors of $I^{p}_{S}$, one has $(x_{1} \cdot\cdot\cdot x_{p}) \circ \gamma =
x_{1} \cdot\cdot\cdot x_{p}$; it follows that $x_{1} \cdot\cdot\cdot x_{p}$ factors through the canonical projection of
$I^{p}_{S}$ into the symmetric product $\Sigma^{p} I_{S}$ (cf. 4.2).

The symmetric product $\Sigma^{p} I_{S}$ has as affine algebra the subalgebra $A$ of $B$ which has as basis over `O_S`
the elementary symmetric functions $1 = \sigma_{0}, \sigma_{1}, \cdots, \sigma_{p}$ of $d_{1}, \cdots, d_{p}$. Denote by
$\kappa$ the inclusion $A \hookrightarrow B$ and $\pi$ the morphism of `O_S`-algebras $A \to O_{S}[t]/(t^{2})$ which
annihilates $\sigma_{1}, \cdots, \sigma_{p-1}$ and sends $\sigma_{p}$ to $t$; then one has $\phi \circ \kappa =
\partial_{t} \circ \pi$ (recall that $\partial_{t} : O_{S}[t]/(t^{2}) \to O_{S}$ is the morphism of `O_S`-modules which
annihilates `1` and sends $t$ to `1`). Consequently, denoting by $i$ the closed immersion $I_{S} \hookrightarrow
\Sigma^{p} I_{S}$ defined by $\pi$, one has a commutative diagram:

```text
                              D^p
       S  ──δ × ··· × δ→  I_S^p  ──x_1 ··· x_p→  G

   δ                              can.
              i                            y
       I_S  ──────────→  Σ^p I_S  ──────────→  G
```

which shows that $D^{p}$ is of the form $y \circ \delta$, so is indeed a derivation of $G$ at the origin.

### 6.3

<!-- label: III.VII_A.6.3 -->

Let $\mathfrak{S}_{p}$ be the symmetric group of order $p$ and $I^{p}_{S} \times \mathfrak{S}_{p}$ the direct sum of a
family of copies of $I^{p}_{S}$ indexed by $\mathfrak{S}_{p}$. We denote by $\pi : I^{p}_{S} \times \mathfrak{S}_{p} \to
I^{p}_{S}$ the canonical projection and

```text
μ : I_S^p × 𝔖_p ⟶ I_S^p
```

the morphism defining the action of $\mathfrak{S}_{p}$ on $I^{p}_{S}$ (i.e., if $\tau$ is an element of
$\mathfrak{S}_{p}$, the restriction of $\mu$ to $I^{p}_{S} \times \tau$ has $pr_{\tau(j)}$ as $j$-th component). This
being so, we lay down the following definition:

<!-- original page 457 -->

**Definition.** *A functor $X : (Sch/S)^{\circ} \to (Ens)$ satisfies condition* (F) *if:*

*a) $X$ transforms finite direct sums into direct products,*

*b) for every $S$-scheme $T$, the following sequence is exact:*

```text
X(T × Σ^p I_S)  ⟶  X(T × I_S^p)  ⇉  X(T × I_S^p × 𝔖_p),
                          (the two parallel arrows being X(id_T × π) and X(id_T × μ)).
```

Every $S$-scheme satisfies (F); if $\mathcal{F}$ is an `O_S`-module, $\mathcal{W}(\mathcal{F})$ satisfies (F); every
projective limit of functors satisfying (F) also satisfies (F); if $Y$ satisfies (F) and if $X$ is an arbitrary
$S$-functor, $\operatorname{Hom}_{S}(X, Y)$ satisfies (F).

Let $X$ be a very good group (II 4.10) satisfying condition (F). Denoting by $x : I_{S} \to X$ a morphism which extends
the unit section of $X$ and resuming the notations of 6.2, one sees as above that $x_{1} \cdot\cdot\cdot x_{p} :
I^{p}_{S} \to X$ factors through $\Sigma^{p} I_{S}$:

```text
       I_S^p  ──x_1 ··· x_p→  X
           ╲                  ╱
         can. ╲              ╱ Σ^p(x)
                ╲          ╱
                   Σ^p I_S
```

and defines by composition a morphism

```text
x^{(p)} : I_S ──i→ Σ^p I_S ──Σ^p(x)→ X
```

which we shall call the *symbolic $p$-th power* of $x$.

<!-- original page 485 -->

The endomorphism $x \mapsto x^{(p)}$ of $Lie(G/S)(S)$ is obviously compatible with base changes and is functorial in
$G$. It would be interesting to know for which $G$ this endomorphism makes $Lie(G/S)(S)$ a $p$-Lie algebra.

### 6.4

<!-- label: III.VII_A.6.4 -->

<!-- original page 458 -->

The last definition of the symbolic $p$-th power, which we have just given, is particularly well-suited to computation.
Here are some examples:

#### 6.4.1

<!-- label: III.VII_A.6.4.1 -->

Let $M$ be an "abstract" abelian group and $D_{S}(M)$ the diagonalizable $S$-group of type $M$ (I 4.4.2). For every
$S$-scheme $T$, one has therefore

$$ D_{S}(M)(T) = \operatorname{Hom}_{(Ab)}(M, O(T)^{\times}). $$

Let $x$ be an element of $Lie(D_{S}(M)/S)(S)$, i.e., a homomorphism of abelian groups

```text
M ──x→ Γ(S, O_S + d O_S)^×
```

of the form $m \mapsto 1 + d \xi(m)$, where $\xi \in \operatorname{Hom}_{(Ab)}(M, O(S))$. With the notations of 6.2 and
6.3, the product $x_{1} \cdot\cdot\cdot x_{p}$ associates with an element $m$ of $M$ the expression

```text
(1 + d_1 ξ(m)) ··· (1 + d_p ξ(m))
```

i.e. $1 + \sigma_{1} \xi(m) + \sigma_{2} \xi(m)^{2} + \cdot\cdot\cdot + \sigma_{p} \xi(m)^{p}$.

This expression indeed belongs to $O(\Sigma^{p} I_{S})$. Projecting this into $O(S)[d]/(d^{2})$ by annihilating
$\sigma_{1}, \cdots, \sigma_{p-1}$ and sending $\sigma_{p}$ to $d$, one sees that $x^{(p)}$ is the following
homomorphism from $M$ into $\Gamma(S, O_{S} + d O_{S})^{\times}$:

$$ m \mapsto 1 + d \xi(m)^{p}. $$

In summary, if one identifies $Lie(D_{S}(M)/S)(S)$ with $\operatorname{Hom}_{(Ab)}(M, O(S))$ as in II 5.1, the symbolic
$p$-th power associates with $\xi$ the homomorphism $\xi^{(p)} : m \mapsto \xi(m)^{p}$.

#### 6.4.2

<!-- label: III.VII_A.6.4.2 -->

<!-- original page 459 -->

Let $\mathcal{F}$ be an `O_S`-module and $G$ the group $S$-functor in abelian groups $\mathcal{W}(\mathcal{F})$ (cf. I,
4.6). Let $y$ be an element of $\mathcal{W}(\mathcal{F})(S) = \Gamma(S, \mathcal{F})$ and $y'$ its image in
$\mathcal{W}(\mathcal{F})(I_{S})$ by $\mathcal{W}(\mathcal{F})(I_{S} \to S)$.

One knows (cf. II, 4.4.2 and 4.5.1) that the map $y \mapsto d y'$ is an isomorphism of $O(S)$-modules from
$\mathcal{W}(\mathcal{F})(S)$ onto $Lie(\mathcal{W}(\mathcal{F})/S)(S)$. If one sets $x = d y'$, the quantity $x_{i}$ of
6.2 is none other than $d_{i} y''$, where `y''` denotes the canonical image of $y'$[^N.D.E-VII_A-59] in
$\mathcal{W}(\mathcal{F})(I^{p}_{S})$. Consequently, the product $x_{1} \cdot\cdot\cdot x_{p}$ is equal here to

```text
x_1 + ··· + x_p = (d_1 + ··· + d_p) y'' = σ_1 y''
```

and belongs to $\mathcal{W}(\mathcal{F})(\Sigma^{p} I_{S})$. Since the homomorphism $O(\Sigma^{p} I_{S}) \to O(I_{S})$,
which defines the morphism $i$ of 6.1, annihilates $\sigma_{1}$, one sees that $x^{(p)}$ is zero. Therefore:

> For every `O_S`-module $\mathcal{F}$, the operation $x \mapsto x^{(p)}$ in $Lie \mathcal{W}(\mathcal{F})$ is zero.

#### 6.4.3

<!-- label: III.VII_A.6.4.3 -->

Let $X$ be an $S$-scheme, $G$ the group $S$-functor $\operatorname{Aut}_{S} X$ and $D$ an $S$-derivation of the
structure sheaf `O_X`. According to 1.5, $D$ can be identified with an `I_S`-automorphism $x$ of $X_{I_{S}}$, inducing
the identity on $X$, which one can describe as follows. If $f$ is a section of $O_{S}[d]/(d^{2})$ of the form $a + bd$,
set $D_{I_{S}} f = D a + (D b) d$; in other words, $D_{I_{S}}$ is deduced from $D$ by the base change $I_{S} \to S$;
then the automorphism in question of $X_{I_{S}}$ is associated with the endomorphism
$f \mapsto f + (D_{I_{S}} f) d = a + (D(a) + b) d$ of $O_{S}[d]/(d^{2})$.

Similarly, let $D_{I^{p}_{S}}$ be the differential operator of $X_{I^{p}_{S}}$ deduced from $D$ by the base change
$I^{p}_{S} \to S$. With the notations of 6.2, the automorphism $x_{i}$ of $X_{I^{p}_{S}}$ is then associated with the
endomorphism $f \mapsto f + (D_{I^{p}_{S}} f) d_{i}$ of $O_{S}[d_{1}, \cdots, d_{p}] / (d^{2}_{1}, \cdots, d^{2}_{p})$.
The product $x_{1} \cdot\cdot\cdot x_{p}$ is therefore associated with the endomorphism

```text
(1 + d_1 D_{I_S^p})(1 + d_2 D_{I_S^p}) ··· (1 + d_p D_{I_S^p})
```

<!-- original page 460 -->

i.e., $1 + \sigma_{1} D_{I^{p}_{S}} + \sigma_{2} D^{2}_{I^{p}_{S}} + \cdot\cdot\cdot + \sigma_{p} D^{p}_{I^{p}_{S}}$.

The coefficient of $\sigma_{p}$ is $D^{p}_{I^{p}_{S}}$, which means that the Lie algebra isomorphism

```text
Dér_S(O_X) ⥲ Lie(Aut_S X),    D ↦ x
```

(cf. 1.5), is also an isomorphism of $p$-Lie algebras.

#### 6.4.4

<!-- label: III.VII_A.6.4.4 -->

Using the same method, one sees that, for every `O_S`-module $\mathcal{F}$, the Lie algebra isomorphism

```text
Lie(Aut_{O_S-mod.} 𝒲(ℱ) / S)(S) ⥲ (End_{O_S-mod.} 𝒲(ℱ))(S).
```

(cf. II 4.8) is also an isomorphism of $p$-Lie algebras.

#### 6.4.5

<!-- label: III.VII_A.6.4.5 -->

[^N.D.E-VII_A-60] Let $\mathcal{U}$ be an `O_S`-coalgebra in groups and $G$ the group $S$-functor
$\operatorname{Spec}^{*} \mathcal{U}$; suppose that $G$ is representable. In this case, for every $T \to S$, one has
defined in 5.5 and 6.1.1 two structures of $p$-Lie algebra on $L(T) = Lie(G)(T)$. Since one has a commutative diagram

```text
                              τ
       L(T)  ─────────────────→  Γ(T, 𝒰_T)
          │ ╲                      ▲
          │   ╲ i                  │ ψ
        α │     ╲                  │
          │       ╲                │
          ▼          ▼              │
       U(G_T)  ←─────────────  U(L(T))
                       φ
```

where $U(L(T))$ is the enveloping algebra of $L(T)$ and $\phi$, $\psi$ the algebra morphisms induced by $\alpha$,
$\tau$, one sees that the two $p$-Lie algebra structures coincide: if one identifies $x \in L(T)$ with its image in
$U(G_{T})$ (resp. $\Gamma(T, \mathcal{U}_{T})$), then $x^{(p)}$ is the image of the element $x^{p}$ of $U(L(T))$ by
$\phi$ (resp. $\psi$).

## 7. Radicial groups of height 1

<!-- label: III.VII_A.7 -->

<!-- original page 461 -->

[^N.D.E-VII_A-61] Let $S$ be a scheme of characteristic $p > 0$. We shall say that an `O_S`-algebra $\mathcal{A}$ (resp.
an `O_S`-$p$-Lie algebra $\mathcal{L}$) is *finite locally free* if the `O_S`-module underlying $\mathcal{A}$ (resp.
$\mathcal{L}$) is locally free and of finite type. If $\mathcal{L}$ is a finite locally free `O_S`-$p$-Lie algebra, we
know (cf. 5.5.2) that the group $S$-functor $\operatorname{Spec}^{*} \mathcal{U}_{p}(\mathcal{L})$ is represented by an
$S$-group scheme $\mathfrak{G}_{p}(\mathcal{L})$, finite and locally free. We shall see that this $S$-group scheme is
the solution of a universal problem (7.2) and we shall characterize the $S$-group schemes of the form
$\mathfrak{G}_{p}(\mathcal{L})$ (7.4).

### Definition 7.0

<!-- label: III.VII_A.7.0 -->

[^N.D.E-VII_A-62] *Let $H = \operatorname{Spec} \mathcal{A}$ be a finite locally free $S$-group scheme. We say that $H$
is* infinitesimal *if the unit section $\epsilon_{H} : S \to H$ is a homeomorphism, which is equivalent to saying that
the augmentation ideal of $\mathcal{A}$ is locally nilpotent.*

### 7.1

<!-- label: III.VII_A.7.1 -->

[^N.D.E-VII_A-63] Let $\mathcal{L}$ be a finite locally free `O_S`-$p$-Lie algebra and let
$\mathfrak{G}_{p}(\mathcal{L})$ be the affine $S$-group $\operatorname{Spec} \mathcal{U}_{p}(\mathcal{L})$. According to
5.5, one knows that $\mathcal{L}$ is identified with $Lie \mathfrak{G}_{p}(\mathcal{L})$.

Consider now a very good group $S$-functor $G$ satisfying condition (F) of 6.3 and let $\phi :
\mathfrak{G}_{p}(\mathcal{L}) \to G$ be a morphism of group $S$-functors. According to 6.3, the morphism of `O_S`-Lie
algebras `Lie φ : Lie 𝔊_p(ℒ) → Lie G` is compatible with the symbolic $p$-th power. If we denote by
$\operatorname{Hom}_{p}(\mathcal{L}, Lie G)$ the set of `O_S`-Lie algebra morphisms which are compatible with the
symbolic $p$-th power, one therefore has a map <!-- original page 462 -->

```text
Lie : Hom_{S-Gr.}(𝔊_p(ℒ), G) ⟶ Hom_p(ℒ, Lie G),    φ ↦ Lie φ.
```

### 7.2. Theorem

<!-- label: III.VII_A.7.2 -->

*If $\mathcal{L}$ is a finite locally free `O_S`-$p$-Lie algebra, the map*

```text
Hom_{S-gr.}(𝔊_p(ℒ), G) ⟶ Hom_p(ℒ, Lie G)
```

*is bijective in each of the following cases:*

*(i) $G$ is an $S$-group scheme;*

*(ii) $G$ is of the form $\operatorname{Aut}_{S} X$, where $X$ is an $S$-scheme;*

*(iii) $G$ is of one of the forms $\mathcal{W}(\mathcal{F})$ or $\operatorname{Aut}_{O_{S}-mod}
\mathcal{W}(\mathcal{F})$, where $\mathcal{F}$ denotes a quasi-coherent `O_S`-module.*

The proof of the theorem rests on the following lemma:

**Lemma.** *If $\mathcal{L}$ is a finite locally free `O_S`-$p$-Lie algebra, the $S$-group $G =
\mathfrak{G}_{p}(\mathcal{L})$ is annihilated by the Frobenius morphism $Fr : G \to G^{(p)}$. In particular, $G$ is
infinitesimal.*

[^N.D.E-VII_A-64] Let in fact $\mathcal{U}$ be the restricted enveloping algebra of $\mathcal{L}$, $\mathcal{A} =
\mathcal{U}^{*}$ the affine algebra of $G$, and $\mathcal{I} = Ker \epsilon_{\mathcal{A}}$ the augmentation ideal of
$\mathcal{A}$. One has

$$ (1) \mathcal{A} = \mathcal{I} \oplus \eta_{\mathcal{A}}(O_{S}), $$

where $\eta_{\mathcal{A}}$ denotes the unit section of $\mathcal{A}$, and since $\epsilon_{\mathcal{A}}$ (resp.
$\eta_{\mathcal{A}}$) is the transpose of $\eta_{\mathcal{U}}$ (resp. $\epsilon_{\mathcal{U}}$), this decomposition
corresponds by duality to the decomposition

$$ (2) \mathcal{U} = \mathcal{J} \oplus \eta_{\mathcal{U}}(O_{S}), $$

where $\mathcal{J}$ is the augmentation ideal of $\mathcal{U}$; one therefore has $\mathcal{J} = \mathcal{I}^{*}$.

Let $\pi$ denote the endomorphism $x \mapsto x^{p}$ of `O_S`. We must show that the morphism $Fr : G \to G^{(p)}$
factors through the unit section of $G^{(p)}$, which is equivalent to saying (cf. 4.1.4 (c)) that the morphism $\Phi : a
\otimes_{\pi} x \mapsto a^{p} x$ from $\mathcal{I} \otimes_{\pi} O_{S}$ into $\mathcal{A}$ is zero. Since $\mathcal{A}$
is finite locally free over `O_S`, it suffices to see that the transposed morphism ${}^{t} \Phi$ is zero.

Now $\Phi$ is none other than the following composition

```text
ℐ ⊗_π O_S ──τ→ 𝒜 ⊗_π O_S ──j(𝒜)→ S^p 𝒜 ──b(𝒜)→ 𝒜,
```

where $\tau$ is deduced from the inclusion $\mathcal{I} \hookrightarrow \mathcal{A}$, and $b(\mathcal{A})$ and
$j(\mathcal{A})$ are defined as in 4.3.3 (i.e. $b(\mathcal{A})$ is induced by the multiplication of $\mathcal{A}$ and
$j(\mathcal{A})$ sends $a \otimes_{\pi} 1$ to the image of $a \otimes \cdot\cdot\cdot \otimes a$ in $S^{p}
\mathcal{A}$). Since the `O_S`-dual module of $S^{p} \mathcal{A}$ is none other than the submodule $\Sigma^{p}
\mathcal{U}$ of $\bigotimes^{p} \mathcal{U}$ formed by the sections invariant under the action of the symmetric group of
order $p$, one sees that ${}^{t} \Phi$ is the following composed morphism:

<!-- original page 463 -->

```text
𝒰 ──a(𝒰)→ Σ^p 𝒰 ──r(𝒰)→ 𝒰 ⊗_π O_S ──q→ 𝒥 ⊗_π O_S,
```

where $q$ is deduced from the projection $\mathcal{U} \to \mathcal{J}$ of kernel $\eta_{\mathcal{U}}(O_{S})$,
$a(\mathcal{U})$ is induced by the comultiplication of $\mathcal{U}$ and $r(\mathcal{U})$ vanishes on the symmetrized
tensors and sends a section $x \otimes \cdot\cdot\cdot \otimes x$ to $x \otimes_{\pi} 1$ (confer 4.3.3).

It is clear that ${}^{t} \Phi \circ \eta_{\mathcal{U}} = 0$ and therefore, according to (2), it remains to see that
${}^{t} \Phi$ annihilates the augmentation ideal $\mathcal{J}$. Since ${}^{t} \Phi$ is an algebra morphism and since the
ideal $\mathcal{J}$ is generated by $\mathcal{L}$ (identified with its image in $\mathcal{U}$), it suffices to see that
${}^{t} \Phi(x) = 0$ for every section $x$ of $\mathcal{L}$. Now $-a(\mathcal{U})(x) = (p - 1)! a(\mathcal{U})(x)$ is
the symmetrization of $x \otimes 1 \otimes \cdot\cdot\cdot \otimes 1$, so its image by $r(\mathcal{U})$ is zero. This
proves the first assertion of the lemma.

The second follows. Indeed, since every local section of $\mathcal{I}$ has $p$-th power zero and since $\mathcal{I}$ is
an `O_S`-module of finite type, $\mathcal{I}$ is locally nilpotent (explicitly, if $V$ is an affine open of $S$ such
that $I = \Gamma(V, \mathcal{I})$ is generated by $r$ elements, then $I^{r(p-1)+1} = 0$), whence $G_{red} = S_{red}$ and
therefore the unit section $\epsilon_{G} : S \to G$ is a homeomorphism.

#### 7.2.1

<!-- label: III.VII_A.7.2.1 -->

[^N.D.E-VII_A-65] We shall first prove assertion (ii) of Theorem 7.2. Let $\pi : X \to S$ be an $S$-scheme. Consider
first an arbitrary infinitesimal $S$-group $H$. The <!-- original page 489 --> morphisms $\phi$ from $H$ into
$\operatorname{Aut} X$ correspond bijectively to left actions $\mu : H \times X \to X$ of $H$ on $X$. For such an
action, if $\epsilon$ is the unit section of $H$, the composed morphism

```text
X ≃ S × X ──ε × X→ H × X ──μ→ X
```

must be the identity. Since $(H \times X)_{red}$ is identified with $X_{red}$, one sees that $\mu$ must induce the
identity on the associated reduced schemes. In particular, $\mu$ induces an action of $H$ on each open of $X$, and one
therefore obtains, for every open $U$ of $X$, affine over $S$, a morphism of unital associative algebras:

$$ \mathcal{A}(U) \longrightarrow \mathcal{A}(H) \otimes \mathcal{A}(U) $$

making $\mathcal{A}(U)$ an $\mathcal{A}(H)$-comodule on the left, in such a way that the restriction maps
$\mathcal{A}(U) \to \mathcal{A}(U')$, for $U' \subset U$, are comodule morphisms. Conversely, every datum of this type
comes from a unique left action $\mu : H \times X \to X$. On the other hand, one has the following lemma:

**Lemma.** *Let $X = \operatorname{Spec} \mathcal{C}$ be an affine $S$-scheme, $H = \operatorname{Spec} \mathcal{A}$ an
infinitesimal $S$-group,*

<!-- original page 464 -->

*and $\mathcal{U} = \mathcal{A}^{*} = \operatorname{Hom}_{O_{S}}(\mathcal{A}, O_{S})$. The left actions of $H$ on $X$
correspond bijectively to the representations of the algebra $\mathcal{U}$ in the `O_S`-module $\mathcal{C}$ such that
one has:*

```text
(a)    u(1_𝒞) = ε(u) · 1_𝒞
(b)    u(xy) = ∑_i v_i(x) w_i(y)    if    ∆u = ∑_i v_i ⊗ w_i.
```

*(In the formulas above, $u$ denotes an arbitrary section of $\mathcal{U}$ on an affine open $V$ of $S$, $x$ and $y$
sections of $\mathcal{C}$ on $V$; one denotes by $1_{\mathcal{C}}$ the unit section of $\mathcal{C}$, by $\epsilon$ and
`∆` the augmentation and the diagonal morphism of $\mathcal{U}$.)*

Indeed, a left action $\mu$ of $H$ on $X$ is defined by a morphism of unital associative algebras:

```text
λ : 𝒞 ⟶ 𝒜 ⊗ 𝒞
```

making $\mathcal{C}$ an $\mathcal{A}$-comodule on the left. We shall denote by $\alpha$ the composed morphism

```text
𝒰 ⊗_{O_S} 𝒞 ──𝒰 ⊗ λ→ 𝒰 ⊗_{O_S} 𝒜 ⊗_{O_S} 𝒞 ──γ ⊗ 𝒞→ O_S ⊗_{O_S} 𝒞 ≃ 𝒞
```

where $\gamma$ is the "contraction" of $\mathcal{A}^{*} \otimes_{O_{S}} \mathcal{A}$ into `O_S`. Since $\mathcal{A}$ is
finite locally free over `O_S`, one knows that the map $\lambda \mapsto (\gamma \otimes \mathcal{C})(\mathcal{U} \otimes
\lambda)$ is a bijection from $\operatorname{Hom}_{O_{S}}(\mathcal{C}, \mathcal{A} \otimes \mathcal{C})$ onto
$\operatorname{Hom}_{O_{S}}(\mathcal{U} \otimes \mathcal{C}, \mathcal{C})$. Moreover, one sees easily that the condition
that $\lambda$ define a structure of $\mathcal{A}$-comodule on the left (resp. be a morphism of unital associative
algebras) is equivalent, by duality, to the condition that $\alpha$ be a representation of $\mathcal{U}$ in
$\mathcal{C}$ (resp. that $\alpha$ satisfy conditions (a) and (b)). This proves the lemma.

Moreover, it is clear that, for every representation of $\mathcal{U}$ in the `O_S`-module $\mathcal{C}$, the sections
$u$ of $\mathcal{U}$ which satisfy conditions (a) and (b) of the lemma form a subalgebra of $\mathcal{U}$.

In the particular case $H = \mathfrak{G}_{p}(\mathcal{L})$ of interest to us, these conditions will therefore be satisfied for all sections $u$
of $\mathcal{U} = \mathcal{U}_{p}(\mathcal{L})$, if they are true for the <!-- original page 490 --> sections $u$ of $\mathcal{L}$ (by identifying $\mathcal{L}$ with its
image in $\mathcal{U}_{p}(\mathcal{L})$). Now, if $u$ is a section of $\mathcal{L}$, conditions (a) and (b) simply mean that $u(1_{\mathcal{C}}) = 0$ and that
$u(xy) = u(x) y + x u(y)$, i.e. that $\alpha(u)$ is an `O_S`-derivation of $\mathcal{C} = \mathcal{A}(X)$. Assertion (ii)

<!-- original page 465 --> of 7.2 follows. Indeed, every morphism `φ` from `𝔊_p = 𝔊_p(ℒ)` into `Aut X` defines a

homomorphism of $p$-Lie algebras $Lie \phi$ from $\mathcal{L} = Lie \mathfrak{G}_{p}$ into $\pi_{*}(D\acute{e}r_{O_{S}}
O_{X})$, and conversely every datum of this type comes, according to what precedes, from a unique action $\mu : G \times
X \to X$.

#### 7.2.2

<!-- label: III.VII_A.7.2.2 -->

Let us now show how assertion (i) of Theorem 7.2 follows from (ii). Let $G$ be an $S$-group scheme. If $T$ is an
$S$-scheme and $x$ an element of $G(T)$, we denote by $\ell^{T}_{x}$ (resp. $r^{T}_{x}$) the left translation (resp.
right translation) of `G_T` defined by $x$. The maps $\ell^{T} : x \mapsto \ell^{T}_{x}$ therefore determine a
homomorphism $\ell$ from $G$ into $\operatorname{Aut} G$. On the other hand, let $f$ be a $T$-automorphism of `G_T`; one
then defines ${}^{x} f$ as being equal to $(r^{T}_{x})^{-1} f r^{T}_{x}$, i.e. for every $T' \to T$ and $g \in G(T')$,
$({}^{x} f)(g) = f(g x) x^{-1}$. In this way $G$ acts on the left on the group $S$-functor $\operatorname{Aut} G$, hence
also on the functors $T \mapsto \operatorname{Hom}_{T-Gr.}(\mathfrak{G}_{p}(\mathcal{L}_{T}), \operatorname{Aut} G_{T})$
and `T ↦ Hom_p(ℒ_T, Lie(Aut G_T / T))`. On the other hand, the morphism $\ell^{T} : G_{T} \to \operatorname{Aut} G_{T}$
identifies `G_T` with the group of automorphisms of the $T$-scheme `G_T` commuting with right translations, and the
derived morphism $Lie(\ell^{T})$ identifies $Lie G_{T}$ with the $p$-Lie algebra of `O_T`-derivations of $O_{G_{T}}$
commuting with right translations (cf. II, 4.11.1); they therefore induce commutative squares

```text
                                          Lie
       Hom_{T-Gr.}(𝔊_p(ℒ_T), G_T)  ───────────→  Hom_p(ℒ_T, Lie(G_T / T))

             ℓ^T                                       Lie ℓ^T

                                          Lie
       Hom_{T-Gr.}(𝔊_p(ℒ_T), Aut G_T)  ─────→  Hom_p(ℒ_T, Lie(Aut G_T / T)).
```

The images of the two vertical arrows are the subfunctors formed by the invariants under the action of the $S$-group
$G$. Since the bottom horizontal arrow is invertible according to 7.2.1 and is compatible with the action of $G$, the
top horizontal arrow is also invertible. This proves 7.2 (i).

#### 7.2.3

<!-- label: III.VII_A.7.2.3 -->

<!-- original page 466 -->

Consider now the case where $G = \operatorname{Aut}_{O_{S}-mod.} \mathcal{W}(\mathcal{F})$.[^N.D.E-VII_A-66] Set
$\mathcal{U} = \mathcal{U}_{p}(\mathcal{L})$, $\mathcal{A} = \mathcal{U}^{*}$ and $H = \mathfrak{G}_{p}(\mathcal{L}) =
\operatorname{Spec} \mathcal{A}$. Since $H$ is affine over $S$ then, according to VI_B 11.6.1, a morphism of $S$-groups
from $H$ into $\operatorname{Aut}_{O_{S}-mod.} \mathcal{W}(\mathcal{F})$ is the same thing as a structure of
$\mathcal{A}$-comodule on the right

```text
μ : ℱ ⟶ ℱ ⊗ 𝒜.
```

Moreover, since $\mathcal{A}$ is finite locally free over `O_S`, this is equivalent to the datum of a representation

$$ \alpha : \mathcal{U} \longrightarrow \operatorname{End}_{O_{S}}(\mathcal{F}) $$

of $\mathcal{U}$ in $\mathcal{F}$. Finally, according to the universal property of $\mathcal{U} =
\mathcal{U}_{p}(\mathcal{L})$, to give such a morphism $\alpha$ is equivalent to giving its restriction $\rho$ to
$\mathcal{L}$ (identified with its image in $\mathcal{U}$), which is a $p$-Lie algebra morphism from $\mathcal{L}$ into
$\operatorname{End}_{O_{S}}(\mathcal{F})$.

[^N.D.E-VII_A-67] Finally, consider the case where $G = \mathcal{W}(\mathcal{F})$, keeping the preceding notations.
First, to give a morphism of $S$-functors $\phi : H \to \mathcal{W}(\mathcal{F})$ is equivalent to giving an element
$\theta$ of $\Gamma(H, \mathcal{F} \otimes O_{H})$, and since $H$ is finite locally free over $S$, one has:

```text
Γ(H, ℱ ⊗ O_H) = Γ(S, ℱ ⊗ 𝒜) = Hom_{O_S}(𝒰, ℱ).
```

The condition that $\phi$ be a group morphism then translates into the fact that $\theta$, considered as morphism of
`O_S`-modules $\mathcal{U} \to \mathcal{F}$, vanishes on $1_{\mathcal{U}}$ and on $\mathcal{J}^{2} / \mathcal{J}$, where
$\mathcal{J}$ is the augmentation ideal of $\mathcal{U}$, whence

```text
(1)                  Hom_{S-gr.}(H, 𝒲(ℱ)) = Hom_{O_S}(𝒥 / 𝒥², ℱ).
```

On the other hand, consider the quasi-coherent sheaf $[\mathcal{L}, \mathcal{L}]$, image of the morphism $\mathcal{L}
\otimes \mathcal{L} \to \mathcal{L}$, $x \otimes y \mapsto [x, y]$; for every affine open $V$ of $S$, one has
$[\mathcal{L}, \mathcal{L}](V) = [\mathcal{L}(V), \mathcal{L}(V)]$. Then one has an exact sequence

```text
(†)        0  ⟶  [ℒ, ℒ]  ⟶  ℒ  ──π→  𝒥 / 𝒥²  ⟶  0,
```

where $\pi$ is the composition of the inclusion $\mathcal{L} \hookrightarrow \mathcal{J}$ and the projection
$\mathcal{J} \to \mathcal{J} / \mathcal{J}^{2}$.

Indeed, the question being local on $S$, we may suppose that $S$ is affine with ring $R$ and that $L = \mathcal{L}(S)$
is free with basis $(x_{1}, \cdots, x_{r})$. Identifying $L$ with its image in $U = U_{p}(L)$, let $K$ be the
sub-$R$-module of $U$ direct sum of `[L, L]` and the submodule with basis the monomials $x^{n_{1}}_{1} \cdot\cdot\cdot
x^{n_{r}}_{r}$ such that $n_{1} + \cdot\cdot\cdot + n_{r} \geqslant 2$; one then verifies that $K$ is a two-sided ideal
of $U$. Since $K$ is contained in $J^{2}$ (where $J$ is the augmentation ideal of $U$) and contains all the products
$x_{i} x_{j}$ (which generate $J^{2}$), one deduces that $K = J^{2}$, whence $J^{2} \cap L = [L, L]$ and one has the
exact sequence `(†)`.

On the other hand, one knows from 6.4.2 that $Lie \mathcal{W}(\mathcal{F})$ is none other than
$\mathcal{W}(\mathcal{F})$, the Lie bracket and the symbolic $p$-th power being zero. From this and from what precedes
one deduces that

```text
(2)        Hom_p(ℒ, ℱ) = Hom_{O_S}(ℒ / [ℒ, ℒ], ℱ) = Hom_{O_S}(𝒥 / 𝒥², ℱ)
```

and this, combined with (1), completes the proof of Theorem 7.2.

### 7.3. Lemma

<!-- label: III.VII_A.7.3 -->

*If $\mathcal{L}$ is a finite locally free `O_S`-$p$-Lie algebra, the morphism $j_{\mathcal{L}} : \mathcal{L} \to Lie
\mathfrak{G}_{p}(\mathcal{L})$ of 5.5 is invertible.*

<!-- original page 467 -->

[^N.D.E-VII_A-68] For the proof, see 5.5.1.

### 7.4

<!-- label: III.VII_A.7.4 -->

To end this section, we shall give a characterization of the $S$-group schemes of the form
$\mathfrak{G}_{p}(\mathcal{L})$, where $\mathcal{L}$ is a finite locally free `O_S`-$p$-Lie algebra.

Let $G$ be an $S$-group scheme, $\epsilon_{G}$ the unit section and $\mathcal{I}'$ the kernel of the morphism
$\epsilon^{-1}_{G}(O_{G}) \to O_{S}$ corresponding to $\epsilon_{G}$. The image of $Lie(G/S)(S)$ in $U(G)$ is
identified, according to 2.5 and 1.3.1, with the morphisms of `O_S`-modules from $\epsilon^{-1}_{G}(O_{G})$ into `O_S`
which vanish on the unit section of $\epsilon^{-1}_{G}(O_{G})$ and on $\mathcal{I}'^{2}$. One thus recovers the
canonical isomorphism of $Lie(G/S)(S)$ onto $\operatorname{Hom}_{O_{S}}(\mathcal{I}' / \mathcal{I}'^{2}, O_{S})$ of II,
3.3 and 4.11.4.[^N.D.E-VII_A-69] We shall set $\omega_{G/S} = \mathcal{I}' / \mathcal{I}'^{2}$ as in loc. cit., so that
the sheaf $Lie(G/S)$ is identified with $\omega^{*}_{G/S} = \operatorname{Hom}_{O_{S}}(\omega_{G/S},
O_{S})$.[^N.D.E-VII_A-70] Moreover, if $G = \mathfrak{G}_{p}(\mathcal{L})$, where $\mathcal{L}$ is a finite locally free
`O_S`-$p$-Lie algebra, one saw in 5.5.3 that $\omega_{G/S} = \mathcal{L}^{*}$.

**Theorem.** *If $G$ is a group scheme over a scheme $S$ of characteristic $p > 0$, the following assertions are
equivalent:*

*(i) There exists a finite locally free `O_S`-$p$-Lie algebra $\mathcal{L}$ such that $G \simeq
\mathfrak{G}_{p}(\mathcal{L})$.*

*(i') The `O_S`-$p$-Lie algebra $Lie(G)$ is finite locally free and $G \simeq \mathfrak{G}_{p}(Lie(G))$.*

*(ii) $G$ is affine over $S$, $\omega_{G/S}$ is a locally free `O_S`-module of finite type and the affine algebra of $G$
is locally isomorphic to the quotient of the symmetric algebra $S_{O_{S}}(\omega_{G/S})$ by the ideal generated by the
$p$-th powers of the sections of $\omega_{G/S}$.*

*(iii) $G$ is locally of finite presentation over $S$, of height $\leqslant 1$, and $\omega_{G/S}$ is locally free.*

*(iii') $G$ is locally of finite type over $S$, of height $\leqslant 1$, and $\omega_{G/S}$ is locally free.*

*(iv) $G$ is locally of finite presentation and flat over $S$, of height $\leqslant 1$.*[^N.D.E-VII_A-71]

#### 7.4.1

<!-- label: III.VII_A.7.4.1 -->

<!-- original page 468 -->

The equivalence (i) ⇔ (i') follows from 5.5.3 (i), the implications (ii) ⇒ (iii) ⇒ (iii') are clear, and one has (i) ⇒
(iv) since $\mathfrak{G}_{p}(\mathcal{L})$ is finite locally free and of height $\leqslant 1$, according to 5.5.2 and
Lemma 7.2. Let us show that (i) entails (ii). Denote by $\mathcal{I}$ the augmentation ideal of $\mathcal{A} =
\mathcal{U}_{p}(\mathcal{L})^{*}$. One has already seen in 5.5.3 (ii) that $\omega_{G/S} = \mathcal{I} /
\mathcal{I}^{2}$ is identified with $\mathcal{L}^{*}$, hence is finite locally free.

Now suppose $S$ affine. There is then a section $\sigma : \omega_{G/S} \to \mathcal{I}$ of the projection $\mathcal{I}
\to \mathcal{I} / \mathcal{I}^{2}$; it induces an algebra morphism $\sigma' : S_{O_{S}}(\omega_{G/S}) \to \mathcal{A}$
and, according to Lemma 7.2, $\sigma'$ factors into a morphism

```text
φ : S_{O_S}(ω_{G/S}) / K ⟶ 𝒜,
```

where $K$ denotes the ideal generated by the $p$-th powers of sections of $\omega_{G/S}$. If one filters $\mathcal{A}$
(resp. $S_{O_{S}}(\omega_{G/S}) / K$) by the powers of $\mathcal{I}$ (resp. of the ideal generated by $\omega_{G/S}$),
it is clear that $\phi$ induces an epimorphism of the associated graded modules. So $\phi$ is an epimorphism of locally
free `O_S`-modules of the same rank (cf. 5.3.3); so $\phi$ is an isomorphism. This proves that (i) ⇒ (ii).

#### 7.4.2

<!-- label: III.VII_A.7.4.2 -->

Suppose now $G$ of height $\leqslant 1$ and locally of finite presentation <!-- original page 469 --> over
$S$.[^N.D.E-VII_A-72] Since the Frobenius morphism $Fr : G \to G^{(p)}$ is integral and factors through the unit section
of $G^{(p)}$, then $G$ is integral (hence affine) over $S$. Let then $\mathcal{A} = \mathcal{A}(G)$; since $G$ is
supposed locally of finite presentation over $S$, it follows that $G$ is finite and of finite presentation over $S$,
hence $\mathcal{A}(G)$ is an `O_S`-module of finite presentation (cf. [EGA IV₁, 1.4.7](https://jcreinhold.github.io/ega/iv/12-ch4-01-relative-finiteness-conditions.html#14-morphisms-locally-of-finite-presentation)). Let $\mathcal{I}$ be the
augmentation ideal of $\mathcal{A}$; since $\mathcal{A} = \eta_{\mathcal{A}}(O_{S}) \oplus \mathcal{I}$ (where
$\eta_{\mathcal{A}}$ is the unit section of $\mathcal{A}$), $\mathcal{I}$ is an `O_S`-module of finite presentation, and
so is $\omega_{G} = \mathcal{I} / \mathcal{I}^{2}$. When one supposes $G$ of height $\leqslant 1$ and locally of finite
type over $S$, one obtains similarly that $\mathcal{A}(G)$, $\mathcal{I}$ and $\omega_{G} = \mathcal{I} /
\mathcal{I}^{2}$ are `O_S`-modules of finite type.

So, under hypothesis (iii'), one obtains that $\omega_{G/S}$ is finite locally free over `O_S`, as is $\mathcal{L} =
Lie(G/S) = \omega^{*}_{G/S}$. Let then $\mathcal{B} = \mathcal{U}_{p}(\mathcal{L})^{*}$ and $H =
\mathfrak{G}_{p}(\mathcal{L}) = \operatorname{Spec} \mathcal{B}$. According to Theorem 7.2, the identity map of
$\mathcal{L}$ corresponds to a group morphism from $H = \mathfrak{G}_{p}(\mathcal{L})$ to $G$, hence to a morphism of
`O_S`-algebras $\theta : \mathcal{A} \to \mathcal{B}$. The task is to show that $\theta$, which induces by definition an
isomorphism of $\omega_{G/S}$ onto $\omega_{H/S}$, is an isomorphism.

For this, one may restrict to the case where $S$ is affine. There is then a section $\tau$ of the projection
$\mathcal{I} \to \omega_{G/S}$; it induces an algebra morphism $\tau' : S_{O_{S}}(\omega_{G/S}) \to \mathcal{A}$ and
since every local section of $\mathcal{I}$ has $p$-th power zero (since $Fr : G \to G^{(p)}$ factors through the unit
section of $G^{(p)}$), $\tau'$ induces a morphism of `O_S`-algebras $\psi$ which fits in the commutative diagram below:

```text
                                          ψ
              S_{O_S}(ω_{G/S}) / K  ──────→  𝒜
                       ╲                        │
                         ╲                      │ θ
                         φ ╲                    │
                              ╲                 ▼
                                                ℬ
```

where $K$ is the ideal generated by the $p$-th powers of sections of $\omega_{G/S}$. On the one hand, one shows as in
7.4.1 that $\psi$ is an epimorphism of `O_S`-modules. On the other hand, we saw in 7.4.1 that $\phi = \theta \circ \psi$
is an isomorphism. The same therefore holds for $\theta$. This proves that (iii') ⇒ (i).

#### 7.4.3

<!-- label: III.VII_A.7.4.3 -->

[^N.D.E-VII_A-73] Let us finally show that (iv) entails (iii). It suffices to show that $\omega_{G/S}$ is locally free,
so one may suppose $S$ affine with ring $R$. As remarked at the beginning of 7.4.2, hypothesis (iv) then entails that $G
= \operatorname{Spec} A$, for an $R$-algebra $A$ which is an $R$-module of finite presentation, as is $\omega_{G/A} = I
/ I^{2}$ (where $I$ is the augmentation ideal of $A$). Since one supposes moreover that $G$ is flat over $S$, then $A$
is a finite locally free $R$-module (cf. [BAC] II, § 5.2, Th. 1 and cor. 2) and, according to loc. cit., to show that
$\omega_{G/A}$ is locally free of finite rank, it suffices to show that $(\omega_{G/A})_{\mathfrak{m}}$ is flat for
every maximal ideal $\mathfrak{m}$ of $R$. So one may suppose $R$ local <!-- original page 494 --> and $A$ free of rank
$n + 1$, hence $I$ free of rank $n$. Let $\mathfrak{m}$ be the maximal ideal of $R$ and $k = R / \mathfrak{m}$.

Denote by $I_{k}$ the augmentation ideal of $A_{k}$ and $r$ the dimension of $\omega_{G_{k} / k} = I_{k} / I^{2}_{k}$.
Let $(e_{1}, \cdots, e_{n})$ be a basis of $I_{k}$ such that $(e_{r+1}, \cdots, e_{n})$ is a basis of $I^{2}_{k}$, and
let $x_{1}, \cdots, x_{n}$ be elements of $I$ lifting the $e_{i}$. According to Nakayama's lemma, $(x_{1}, \cdots,
x_{n})$ is a basis of $I$ over $R$. Let $N$ be the sub-$R$-module of $I$ with basis $(x_{1}, \cdots, x_{r})$ and let $B$
be the quotient of the symmetric algebra of $N$ by the ideal generated by the elements $x^{p}$, for $x \in N$. Since
every element of $I$ has $p$-th power zero, one obtains a morphism of $R$-algebras

$$ \psi : B \longrightarrow A. $$

According to 7.4.2, $\psi \otimes k$ is an isomorphism. It follows that $Coker \psi = 0$ and that, denoting $K = Ker
\psi$, the morphism $\tau : K \otimes k \to B \otimes k$ is zero. But since $\psi$ is surjective and $A$ is flat over
$R$, then $\tau$ is also injective, whence $K \otimes k = 0$. On the other hand, since $A$ is an $R$-module of finite
presentation, $K$ is an $R$-module of finite type (cf. [BAC] I, § 2.8, Lemma 9), whence $K = 0$ by Nakayama. So $\psi$
is an isomorphism of $R$-algebras, and since $\psi^{-1}(I)$ contains the augmentation ideal $J$ of $B$, it follows that
$\psi^{-1}(I) = J$, and therefore $\psi^{-1}$ induces an isomorphism of $R$-modules from $I / I^{2}$ onto $J / J^{2} =
N$. This proves that $\omega_{G/S}$ is finite locally free, whence the implication (iv) ⇒ (iii). This completes the
proof of Theorem 7.4.

### Remark 7.5

<!-- label: III.VII_A.7.5 -->

[^N.D.E-VII_A-74] It obviously follows from Theorems 7.2 and 7.4 that the functors $G \mapsto Lie(G)$ and $\mathcal{L}
\mapsto \mathfrak{G}_{p}(\mathcal{L})$ induce equivalences, quasi-inverses of each other, between the category of
$S$-groups locally of finite presentation and flat, of height $\leqslant 1$, and the full subcategory of that of
`O_S`-$p$-Lie algebras formed by the finite locally free `O_S`-$p$-Lie algebras.

## 8. The case of a base field

<!-- label: III.VII_A.8 -->

<!-- original page 470 -->

### 8.1

<!-- label: III.VII_A.8.1 -->

Let us now summarize the results obtained in the case where $S$ is the spectrum of a field $k$ of characteristic $p >
0$. Let us then say that a $k$-group scheme is *algebraic* if the underlying scheme is of finite type over $k$. In this
case, according to Theorem 7.2, one obtains:[^N.D.E-VII_A-75]

#### Theorem 8.1.1

<!-- label: III.VII_A.8.1.1 -->

*The functor $\mathfrak{G}_{p}$, which to every $p$-Lie algebra $\mathcal{L}$ of finite dimension over $k$ associates
the $k$-group $\mathfrak{G}_{p}(\mathcal{L})$, is left adjoint to the functor which to every algebraic $k$-group $G$
associates $Lie(G)$.*

Combining this with Theorem 7.4, one obtains:

#### Theorem 8.1.2

<!-- label: III.VII_A.8.1.2 -->

*The functors $\mathfrak{G}_{p} : \mathcal{L} \mapsto \mathfrak{G}_{p}(\mathcal{L})$ and $G \mapsto Lie(G)$ induce
equivalences, quasi-inverses of each other, between the category of $p$-Lie algebras of finite dimension over $k$, and
that of algebraic $k$-groups of height $\leqslant 1$.*

Then, since $\mathfrak{G}_{p}$ is a left adjoint functor, it commutes with inductive limits,[^N.D.E-VII_A-76] hence in
particular with the formation of cokernels. On the other hand, if one has two morphisms $\phi : G \to H$ and $\phi' : G'
\to H$ between algebraic $k$-groups of height $\leqslant 1$, then the fibered product $G \times_{H} G'$ is again an
algebraic $k$-group of height $\leqslant 1$ (since the morphism $Fr : G \to G^{(p)}$ commutes with fibered products). So
the inclusion of the category of algebraic $k$-groups of height $\leqslant 1$ into that of all algebraic $k$-groups
commutes with fibered products, hence in particular with the formation of kernels. From this one deduces the:

#### Corollary 8.1.3

<!-- label: III.VII_A.8.1.3 -->

*The functor $\mathfrak{G}_{p}$ is exact, in the following sense. If $\pi : \mathcal{L}_{1} \to \mathcal{L}_{2}$ is a
surjective morphism between $p$-Lie algebras of finite dimension over $k$ and if $i$ is the inclusion of
$\mathcal{L}_{0} = Ker \pi$ in $\mathcal{L}_{1}$, one has an exact sequence of algebraic $k$-groups:*

```text
1  ⟶  𝔊_p(ℒ_0)  ──𝔊_p(i)→  𝔊_p(ℒ_1)  ──𝔊_p(π)→  𝔊_p(ℒ_2)  ⟶  1.
```

[^N.D.E-VII_A-77]

Indeed, according to what precedes, $\mathfrak{G}_{p}(i)$ induces an isomorphism of $\mathfrak{G}_{p}(\mathcal{L}_{0})$
onto $Ker(\mathfrak{G}_{p}(\pi))$ (this kernel being the same in the category of all algebraic $k$-groups $H$ or in that
of $H$ of height $\leqslant 1$), and $\mathfrak{G}_{p}(\pi) : \mathfrak{G}_{p}(\mathcal{L}_{1}) \to
\mathfrak{G}_{p}(\mathcal{L}_{2})$ identifies $\mathfrak{G}_{p}(\mathcal{L}_{2})$ with the quotient of
$\mathfrak{G}_{p}(\mathcal{L}_{1})$ by $\mathfrak{G}_{p}(\mathcal{L}_{0})$ in the category of algebraic $k$-groups.

#### Remark 8.1.4

<!-- label: III.VII_A.8.1.4 -->

[^N.D.E-VII_A-78] Let $\phi : G \to H$ be a morphism of $k$-groups and $K = Ker(\phi)$. Suppose $\phi$ covering for the
(fpqc) topology (this will be the case, in particular, if $\phi$ is covering for a less fine topology, for example the
(fppf) topology). Then, on the one hand, $\phi$ is a $K$-torsor above $H$ (cf. IV 5.1.7.1). On the other hand, (cf. IV
6.3.1) there exists a covering of $H$ by affine opens $S_{i}$, and for each $i$ an affine faithfully flat morphism
$T_{i} \to S_{i}$ factoring through $\phi$. Then $G \times_{H} T_{i}$ is $T_{i}$-isomorphic to $K \times T_{i}$, hence
faithfully flat over $T_{i}$, and therefore, by (fpqc) descent, $G \times_{H} S_{i} \to S_{i}$ is faithfully flat, so
that $\phi$ is faithfully flat.

Conversely, if $\phi$ is faithfully flat and quasi-compact (resp. and locally of finite presentation), it is covering
for the (fpqc) topology (resp. (fppf)), cf. IV 6.3.1. Recall finally that a morphism of sheaves is covering if and only
if it is an epimorphism, cf. IV 4.4.3. One therefore obtains, in particular, that a quasi-compact morphism of $k$-groups
is faithfully flat if and only if it is an epimorphism of (fpqc) sheaves.

### 8.2. Proposition

<!-- label: III.VII_A.8.2 -->

*Consider an exact sequence*[^N.D.E-VII_A-79] *of algebraic groups over a field $k$ of characteristic $p > 0$*

```text
1  ⟶  G'  ──τ→  G  ──π→  G''  ⟶  1
```

<!-- original page 496 -->

*and the following assertions:*

*(i) The morphism $\pi$ is smooth.*

*(ii) $G'$ is smooth.*

*(iii) For every integer $n > 0$, the following sequence, induced by $\tau$ and $\pi$, is exact:*

<!-- original page 471 -->

```text
1 ⟶ Fr^n G' ⟶ Fr^n G ⟶ Fr^n G'' ⟶ 1.
```

*(iv) The morphism $Fr \pi : Fr G \to Fr G''$ is an epimorphism of (fppf) sheaves.*

*(v) The morphism `Lie(π) : Lie(G) → Lie(G'')` is surjective.*

*Then one has the implications (i) ⇔ (ii) ⇒ (iii) ⇒ (iv) ⇔ (v) and all the assertions are equivalent when $G$ is smooth
over $k$.*

Indeed, (i) is equivalent to (ii) according to VI_B 9.2 (vii), and it is clear that (iii) implies (iv). On the other
hand, the equivalence of (iv) and (v) follows from 8.1.3.

The implication (ii) ⇒ (iii) follows from the diagram:

```text
       1  ⟶  G'  ──τ→  G  ──π→  G''  ⟶  1

          Fr^n(G'/k)     Fr^n(G/k)     Fr^n(G''/k)
                                                              
       1  ⟶  G'^{(p^n)}  ──τ^{(p^n)}→  G^{(p^n)}  ──π^{(p^n)}→  G''^{(p^n)}  ⟶  1
```

whose two rows are exact: since $Fr^{n}(G'/k)$ is an epimorphism of (fppf) sheaves according to Corollary 8.3.1 below,
$\pi$ induces an epimorphism of $Fr^{n} G$ onto $Fr^{n} G''$ (generalize the snake lemma to sheaves of groups not
necessarily commutative).

Similarly, when $G$ is smooth over $k$, $Fr(G/k)$ is an epimorphism, so if moreover $Fr \pi$ is an epimorphism, the same
snake lemma applied to the diagram above for $n = 1$ shows that $Fr(G'/k)$ is an epimorphism, so $G'$ is smooth over
$k$, according to 8.3.1 below.

### 8.3. Proposition

<!-- label: III.VII_A.8.3 -->

*If $G$ is a group locally of finite type*[^N.D.E-VII_A-80] *over a field $k$ of characteristic $p > 0$, there exists an
integer $n_{0}$ such that $G / (Fr^{n} G)$ is smooth over $k$ for $n \geqslant n_{0}$.*

<!-- original page 472 -->

Since the construction of $G / (Fr^{n} G)$ commutes with extension of the base field (4.1.1 and VI_A, 3.3.2), we may
suppose $k$ perfect. In this case, $G_{red}$ is a $k$-group locally of finite type (cf. VI_A 0.2) and one has the
following commutative and exact diagram, where one has denoted by $H$ the $k$-scheme $G_{red} \ G$:

$$ 1 \longrightarrow G_{red} \longrightarrow G \longrightarrow H

              Fr^{n}(G_{red}/k)    Fr^{n}(G/k)     Fr^{n}(H/k)
                                                              
       1  \longrightarrow  G^{(p^{n})}_{red}  \longrightarrow  G^{(p^{n})}  \longrightarrow  H^{(p^{n})}.
$$

Now $H$ is the spectrum of a finite local $k$-algebra with residue field $k$ (cf. VI_A, 5.6.1). Consequently, there
exists an integer $n_{0}$ such that, for every $n \geqslant n_{0}$, $Fr^{n}(H/k)$ factors through the "unit" section of
$H^{(p^{n})}$. It follows that, for $n \geqslant n_{0}$, $Fr^{n}(G/k)$ factors through $G^{(p^{n})}_{red}$ and
therefore, according to VI_A, 5.4.1, one has a commutative diagram

```text
                              Fr^n(G/k)
              G  ───────────────────→  G_{red}^{(p^n)}
                ╲                              ▲
              π  ╲                              │ i
                  ╲                              │
                   ╲                              │
                G / (Fr^n G)
```

where $i$ is a closed immersion (and $\pi$ is the canonical projection). Since moreover $i$ induces a homeomorphism of
the underlying topological spaces, it is therefore an isomorphism. Since $k$ is perfect, $G^{(p^{n})}_{red}$ is smooth
over $k$ (VI_A, 1.3.1), and therefore $G / (Fr^{n} G)$ is smooth over $k$, for every $n \geqslant n_{0}$.

#### 8.3.1. Corollary

<!-- label: III.VII_A.8.3.1 -->

*Let $G$ be a group locally of finite type over a field $k$ of characteristic $p > 0$ and let $n$ be an integer
$\geqslant 1$.*[^N.D.E-VII_A-81] *The following conditions are equivalent:*

*(i) $G$ is smooth over $k$.*

*(ii) $Fr^{n}(G/k) : G \to G^{(p^{n})}$ is an epimorphism of (fppf) sheaves.*

*(iii) $Fr^{n}(G/k) : G \to G^{(p^{n})}$ is faithfully flat.*

First, since $G$ is locally of finite type over $k$, $Fr^{n}(G/k)$ is of finite presentation, so the equivalence of (ii)
and (iii) follows from 8.1.4. Suppose $G$ smooth over $k$, hence $G$ reduced. Then, since $Fr^{n}(G/k)$ is surjective,
it is faithfully flat (cf. VI_A, 6.2 or VI_B, 1.3).

Conversely, suppose $Fr^{n}(G/k)$ faithfully flat. Since $Fr^{n}(G^{(p^{n})}/k)$ is deduced from $Fr^{n}(G/k)$ by base
change (cf. 4.1.3), it is therefore also faithfully flat, as is the composition:

```text
Fr^{2n}(G/k) : G ⟶ G^{(p^n)} ⟶ G^{(p^{2n})}.
```

One thus obtains that, for every $m \in \mathbb{N}$, $Fr^{mn}(G/k) : G \to G^{(p^{mn})}$ is faithfully flat, hence
induces an isomorphism $G / (Fr^{mn} G) \simeq G^{(p^{mn})}$ (cf. VI_A, 5.4.1). Now, according to Proposition 8.3,
$G^{(p^{mn})}$ is smooth over $k$ for $m$ large, so $G$ is also, by (fpqc) descent (cf.
[EGA IV₄, 17.7.1](https://jcreinhold.github.io/ega/iv/30-ch4-17-smooth-unramified-etale-morphisms.html#177-descent-properties-passage-to-the-limit-and-constructibility)).

### 8.4

<!-- label: III.VII_A.8.4 -->

<!-- original page 498 -->

In the two statements which end this Exposé, we return to the case of a field $k$ of arbitrary characteristic.

When $k$ is of characteristic 0 (resp. $p > 0$), let $n$ be an integer $\geqslant 1$ (resp. an integer $\geqslant 1$ and
coprime to $p$); in both cases, we say simply that $n$ is *coprime to the characteristic of $k$*. Moreover, if $G$ is a
group scheme over $k$, we denote by $n_{G} : G \to G$ the morphism of $k$-schemes <!-- original page 473 --> which sends
an element $x$ of $G(T)$ to $x^{n} \in G(T)$, when $T$ is a $k$-scheme.

**Proposition.** *Let $G$ be an algebraic group over a field $k$ and $n$ an integer coprime to the characteristic of
$k$. Then $n_{G} : G \to G$ is an étale morphism.*

[^N.D.E-VII_A-82] According to VI_B 1.3, it suffices to show that $n_{G}$ is étale at the origin. Let $A$ be the local
ring of $G$ at the origin and $I$ the maximal ideal of $A$. According to II 3.9.4, the map `Lie(n_G) : Lie(G) → Lie(G)`,
which is induced by $n_{G}$, is the homothety of ratio $n$. It is therefore an isomorphism, as is the endomorphism
induced by $n_{G}$ on $I / I^{2} = Lie(G)^{*}$. If $k$ is of characteristic 0, $G$ is smooth over $k$ (VI_B 1.6.1, see
also VII_B 3.3.1), so the canonical morphism $S(I / I^{2}) \to gr_{I}(A)$ is an isomorphism, where $gr_{I}(A)$ denotes
the graded module associated with the $I$-adic filtration. It follows that $n_{G}$ induces an automorphism of
$gr_{I}(A)$, hence also of the completion `Â` of $A$, hence $n_{G}$ is étale at the origin (cf.
[EGA IV₄, 17.6.3](https://jcreinhold.github.io/ega/iv/30-ch4-17-smooth-unramified-etale-morphisms.html#176-characterizations-of-étale-morphisms)).

If the characteristic is $p > 0$ and if $G$ is of height $\leqslant 1$, then $A$ is isomorphic to the quotient of the
symmetric algebra of $\omega_{G/k} = I / I^{2}$ by the ideal generated by the $p$-th powers of the elements of
$\omega_{G/k}$ (cf. 7.4); one may then apply the "same" reasoning as in characteristic 0, and one obtains that $n_{G}$
induces an automorphism of $A$.

If $G$ is of height $\leqslant r$ and if we suppose our assertion proved for groups of height $\leqslant r - 1$, denote
by $B$, $A$ and $A'$ the affine algebras of `Fr G`, $G$ and `G' = Fr G \ G`, and $n_{B}$, $n_{A}$ and $n_{A'}$ the
endomorphisms of $B$, $A$ and $A'$ which are induced by $n_{Fr G}$, $n_{G}$ and $n_{G'}$.[^N.D.E-VII_A-83] Let $I' = I
\cap A'$ be the maximal ideal of $A'$, since one has a cartesian square

```text
              Fr G  ────────→  G
                                          
                                          
                e ─────────→  G'
```

one has $B = A / I' A$. Observe that $n_{A'}$ (resp. $n_{B}$) is none other than the endomorphism induced by $n_{A}$ on
$A'$ (resp. on $B$). According to VI_A 3.2, $A$ is a faithfully flat $A'$-module, and since $A'$ is an Artinian local
ring ($G'$ being an algebraic $k$-group of height $\leqslant r - 1$), it follows that $A$ is a free $A'$-module. Since
the restriction of $n_{A}$ to $A'$ is $n_{A'}$, which is an isomorphism according to the inductive hypothesis, it
follows from Nakayama's lemma that $n_{A}$ will be an automorphism if the endomorphism it induces on $A / I' A$ is one.

<!-- original page 499 --> Now this endomorphism is none other than `n_B`, which is an automorphism since `B` is of

height $\leqslant 1$. So $n_{A}$ is an automorphism.

Finally, when $G$ is an arbitrary algebraic group over a field of characteristic $p > 0$, what precedes shows that
$n_{G}$ induces automorphisms of the $k$-schemes $Fr^{r} G$; these schemes are affine over $k$ and have as algebras the
quotients of the local algebra $A$ by the ideal $I^{{p^{r}}}$ generated by the $p^{r}$-th powers of the elements of $I$.
Since <!-- original page 474 --> $n_{G}$ defines automorphisms of the algebras $A / I^{{p^{r}}}$, one sees by passage to
the projective limit that $n_{G}$ induces an automorphism of `Â`, hence $n_{G}$ is étale at the origin (EGA IV₄,
17.6.3).

### 8.5. Proposition

<!-- label: III.VII_A.8.5 -->

*Let $G$ be a finite algebraic group, of rank $n$ over the field $k$. Then $n_{G} : G \to G$ is the zero morphism of
$G$.*

Let us point out at once the following corollary, obtained by combining 8.4 and 8.5:[^N.D.E-VII_A-84]

#### Corollary 8.5.1

<!-- label: III.VII_A.8.5.1 -->

*Let $G$ be a finite algebraic group, of rank $n$ over the field $k$. If $n$ is coprime to the characteristic of $k$,
then $G$ is étale over $k$.*

Let us now prove 8.5. Let $H$ be a normal subgroup of $G$ of rank $m$ over $k$. Denote by $\lambda : H \times G \to G$
the morphism induced by the multiplication of $G$. Then, with the notations of VI_A 3.2, one has a cartesian square:

```text
              H × G  ──λ→  G
              pr_2          π
                              
                              
                G  ───→  H \ G.
```

Since $\pi : G \to H \ G$ is faithfully flat, quasi-compact (VI_A 3.2), and since $pr_{2}$ is locally free of rank $m$,
it follows from
[EGA IV₂, 2.5.2](https://jcreinhold.github.io/ega/iv/14-ch4-02-base-change-and-flatness.html#25-permanence-of-properties-of-modules-under-faithfully-flat-descent),
that $G \to H \ G$ is locally free of rank $m$. Denoting $r = rg_{k}(H \ G)$, one therefore has $n = rg_{k}(G) = r m$.

On the other hand, one has an exact sequence of "abstract" groups

```text
1 ⟶ H(T) ⟶ G(T) ⟶ (H \ G)(T)
```

for every $k$-scheme $T$; it is therefore clear that $n_{G}$ is zero if $m_{H}$ and $r_{H \ G}$ are. If one takes for
$H$ the neutral component `G_0` of $G$, then $G_{0} \ G$ is étale (cf. VI_A 5.5.1), so that one may suppose $G$ étale
over $k$ or else infinitesimal (cf. 7.0).

If $G$ is étale, one reduces, by extension of the base field, to the case where $k$ is algebraically closed. In this
case, $G$ is a constant group (cf. I 4.1), and the statement is classical.

If $G$ is infinitesimal and non-zero, $k$ is necessarily of characteristic $p > 0$ (cf. VI_B 1.6.1 or VII_B 3.3.1); the
subgroups $Fr^{n} G$ then form a composition series of $G$, whose quotients are of height $\leqslant 1$.
    <!-- original page 475 -->

This reduces us to the case where $G$ is of height $\leqslant 1$. Let then $A$ (resp. $L$) be the affine algebra (resp.
the Lie algebra) of $G$ and $U = U_{p}(L)$. According to 7.4, one has $G = \mathfrak{G}_{p}(L)$ whence $A = U^{*}$; so
if $\dim_{k} L = r$, the rank of $G$ over $k$ is $p^{r}$ (cf. 5.3.3). We shall therefore study the morphism $p_{G} : G
\to G$ defined by raising to the $p$-th power; it induces an endomorphism $p_{A}$ of $A$ and, by duality, an
endomorphism $p_{U}$ of $U$.

Let $I$ be the augmentation ideal of $A$; we shall show that $p_{A}(I) \subset I^{p}$. Supposing this established, one
will therefore have $p^{r}_{A}(I) \subset I^{p^{r}}$. On the other hand, one knows that $I^{r(p-1)+1} = 0$ (since $I$ is
generated by $r$ elements of $p$-th power zero). Since $p^{r} > r(p - 1)$, it follows that $p^{r}_{A}(I) = 0$, so
$p^{r}_{G}$ is the zero morphism. It therefore remains to show the assertion:

$$ (\ast) p_{A}(I) \subset I^{p}. $$

For every integer $s \geqslant 1$, we shall denote $m^{s-1}_{A} : A^{\otimes s} \to A$ (resp. `∆_U^{s-1} : U → U^{⊗s}`)
the map induced by the multiplication $m_{A}$ of $A$ (resp. the comultiplication `∆_U` of $U$). Then $p_{A}$ is equal to
the following composition:

```text
A ──∆_A^{p-1}→ A^{⊗p} ──m_A^{p-1}→ A,
```

and since the transpose of $m_{A}$ (resp. `∆_A`) is `∆_U` (resp. $m_{U}$), the endomorphism $p_{U} = {}^{t}p_{A}$ of $U$
is the following composition:

```text
U ──∆_U^{p-1}→ U^{⊗p} ──m_U^{p-1}→ U.
```

[^N.D.E-VII_A-85] Let $J$ be the augmentation ideal of $U$; one has $U = k 1_{U} \oplus J$ and one will denote by $\pi$
the projection $U \to J$ of kernel $k 1_{U}$. For every integer $s \geqslant 1$, denote $(I^{s})^{\perp}$ the orthogonal
of $I^{s}$ in $A^{*} = U$, i.e., $(I^{s})^{\perp}$ is the set of $u \in U$ such that the composition below is zero:

```text
I^{⊗s} ──m_A^{s-1}→ I ──u→ k.
```

Since the transpose of $m_{A}$ is `∆_U`, one sees that $(I^{s})^{\perp}$ is the vector subspace $P_{s-1}$ formed by the
$u \in U$ such that `∆_U^{s-1}(u)` vanishes on $I^{\otimes s}$, i.e., denoting by `∆̄_U^{s-1}` the composition of
`∆_U^{s-1}` and the projection $\pi^{\otimes s} : U^{\otimes s} \to J^{\otimes s}$, one obtains that

```text
(I^s)^⊥ = P_{s-1} = Ker ∆̄_U^{s-1}
```

(see also VII_B, 1.3.6). So, to prove assertion $(\ast)$, one must show that the transpose map $p_{U} = {}^{t}p_{A}$
sends $P_{p-1}$ into $I^{\perp} = k 1_{U}$. Since $p_{U}(1_{U}) = 1_{U}$, it suffices to show the assertion below, where
$P^{+}_{p-1}$ denotes $J \cap P_{p-1}$:

$$ (\ast\ast) p_{U}(P^{+}_{p-1}) = 0. $$

On the other hand, one shows easily, by induction on $s$, that $P^{+}_{s-1}$ is the vector subspace of $U$ generated by
the products $x_{1} \cdot\cdot\cdot x_{t}$, with $1 \leqslant t \leqslant s - 1$ and $x_{i} \in L$ (cf. VII_B <!-- original page 501 --> 4.3). Now, if
$x_{1}, x_{2}, \cdots, x_{t}$ are elements of $L$, one has:

```text
p_U(x_1 x_2 ··· x_t) = m_U^{p-1}( ∏_{j=1}^t ∑_{i=1}^p 1 ⊗ ··· ⊗ x_j ⊗ ··· ⊗ 1 )    (x_j in position i)
```

It is clear that the expression $\prod_{j} \sum_{i} 1 \otimes \cdot\cdot\cdot \otimes x_{j} \otimes \cdot\cdot\cdot
\otimes 1$ is a sum of $p^{t}$ terms $x_{h}$ indexed by the maps $h$ from ${1, \cdots, t}$ into ${1, \cdots,
p}$.[^N.D.E-VII_A-86] Such a map $h$ defines an ordered partition $p_{h}$ of ${1, \cdots, t}$ into at most $p$ parts.
Indeed, denote $i_{1} < \cdot\cdot\cdot < i_{r}$ the elements of the image of $h$ and, for $s = 1, \cdots, r$, set
$I_{s} = h^{-1}(i_{s})$ and $x_{I_{s}} = \prod_{j \in I_{s}} x_{j}$, the product being taken in increasing order. Then
$h$ corresponds to the $p$-tensor

$$ 1 \otimes \cdot\cdot\cdot \otimes x_{I_{1}} \otimes \cdot\cdot\cdot \otimes x_{I_{r}} \otimes \cdot\cdot\cdot \otimes
1 $$

(where each $x_{I_{s}}$ is in position $i_{s}$), and its image by $m^{p}_{U}$ is the product:

$$ x_{I_{1}} \otimes \cdot\cdot\cdot \otimes x_{I_{r}} $$

which depends only on the ordered partition $p = (I_{1}, \cdots, I_{r})$, and which one will denote $x_{p}$. For $p$
fixed, $x_{p}$ is obtained for all choices of $i_{1} < \cdot\cdot\cdot < i_{r}$ in ${1, \cdots, p}$, and one therefore
obtains the equality

```text
p_U(x_1 x_2 ··· x_t) = ∑_p (p choose n(p)) x_p,
```

where $p$ ranges over the set of ordered partitions of ${1, \cdots, t}$ into at most $p$ parts, and where $n(p)$ denotes
the number of parts of $p$. (One has $1 \leqslant n(p) \leqslant \min(t, p)$.)

When $t < p$, all the terms `(p choose n(p))` are therefore zero, so that $p_{U}(x_{1} \cdot\cdot\cdot x_{t}) = 0$.
    <!-- original page 476 --> So $p_{U}$ vanishes on $P^{+}_{p-1}$, which proves assertion $(\ast\ast)$, and hence $(\ast)$, and
completes the proof of 8.5.

#### Corollary 8.5.2

<!-- label: III.VII_A.8.5.2 -->

[^N.D.E-VII_A-87] *Let $S$ be a reduced scheme and $G$ a finite locally free $S$-group of rank $n$. Then $n_{G} : G \to
G$ is the zero morphism of $G$.*

Indeed, let $S'$ be the sum of the $\operatorname{Spec} O_{S, \eta}$, for $\eta$ ranging over the maximal points of $S$.
Since $S$ is reduced, the morphism $S' \to S$ is schematically dominant, and the same holds for the morphism $f : G_{S'}
\to G$, since $G$ is finite locally free over $S$ (cf. EGA IV₃, 11.10.5). Since $G \to S$ is affine, hence separated,
the locus of coincidence of $n_{G}$ and the zero morphism is a closed subscheme of $G$, and it majorizes $f$ according
to 8.5, hence equals $G$, i.e. $n_{G}$ is the zero morphism.

#### Remark 8.5.3

<!-- label: III.VII_A.8.5.3 -->

Let us also point out that, according to a theorem of P. Deligne (see [TO70], p. 4), if $G$ is a commutative finite
locally free $S$-group of rank $n$ over an arbitrary base $S$, then $n_{G} = 0$.

## Bibliography

- [BAlg] N. Bourbaki, *Algèbre*, Chap. I–III, Hermann, 1974, Chap. X, Masson, 1980.
- [BAC] N. Bourbaki, *Algèbre commutative*, Chap. I–IV, Masson, 1985.
- [BLie] N. Bourbaki, *Groupes et algèbres de Lie*, Chap. I, Hermann, 1971.
- [DG70] M. Demazure, P. Gabriel, *Groupes algébriques*, Masson & North-Holland, 1970.
- [Ja03] J. C. Jantzen, *Representations of algebraic groups*, Academic Press 1987; 2nd edition, Amer. Math. Soc., 2003.
- [TO70] J. Tate, F. Oort, *Groups schemes of prime order*, Ann. scient. Éc. Norm. Sup. 3 (1970), 1–21.

<!-- LEDGER DELTA — Exposé VII_A — for consolidation in Phase 3

| French | English | Note |
| ------ | ------- | ---- |
| déviation | deviation | Used both for `S`-deviation (composed pair `(u, d)`) and order-`n` deviation. Kept literal. |
| `S`-déviation d'ordre `⩽ n` | `S`-deviation of order `⩽ n` | Standard. |
| `S`-dérivation | `S`-derivation | Distinct from deviation; satisfies Leibniz rule. |
| algèbre infinitésimale | infinitesimal algebra | Per VII_A 2.1; modern usage: algebra of distributions (cf. [DG70]). |
| opérateur différentiel invariant à droite / à gauche | right-invariant / left-invariant differential operator | Standard. |
| translation à droite / à gauche | right / left translation | Standard. |
| coalgèbre / cogèbre | coalgebra | Bourbaki's *cogèbre* is rendered "cogebra" in N.D.E. quotations; main text uses "coalgebra". |
| coalgèbre en groupes | coalgebra in groups | Group object in the category of coalgebras. |
| comultiplication / morphisme diagonal | comultiplication / diagonal morphism | Both terms preserved. |
| antipodisme | antipode | Standard modern term. |
| élément primitif | primitive element | `∆u = u ⊗ 1 + 1 ⊗ u`. |
| dualité de Cartier | Cartier duality | Standard. |
| morphisme de Frobenius absolu / relatif | absolute / relative Frobenius morphism | Per VII_A 4.1 N.D.E. (41). |
| Verschiebung | Verschiebung | Loanword preserved per modern English usage. |
| `p`-algèbre de Lie (restreinte) | restricted `p`-Lie algebra | Title preference; modern English: restricted Lie algebra. First gloss provided. |
| puissance `p`-ième symbolique | symbolic `p`-th power | The operation `x ↦ x^{(p)}`. |
| algèbre enveloppante restreinte | restricted enveloping algebra | `U_p(𝔤)`. |
| très bon groupe / bon foncteur | very good group / good functor | Per II 4.4, 4.6, 4.10. |
| groupe radiciel de hauteur 1 | radicial group of height 1 | Section 7 title. *Radiciel* = purely inseparable per glossary. |
| hauteur ⩽ n | height ⩽ n | `Fr^n(G/S) = 0`. |
| produit symétrique p-uple | `p`-fold symmetric product | `Σ^p X`. |
| tenseur symétrisé | symmetrized tensor | Image of `N` operator. |
| Frobeniuseries | "Frobeniuseries" | Gabriel's coinage; kept with quotation marks as in source. |
| recouvrement (fpqc, fppf) | covering (for the (fpqc), (fppf) topology) | Per glossary. |
| schématiquement dominant | schematically dominant | Per EGA IV. |
| groupe infinitésimal | infinitesimal group | Per Definition 7.0. |
-->

[^VII_A-A-1]: Part A of the present Exposé had not been treated seriously in the oral seminars.

[^N.D.E-VII_A-1]: In particular, if $X$ and $Y$ are two $S$-schemes, $X \times_{S} Y$ is denoted simply $X \times Y$.
    Moreover, let us point out that for the content of sections 1 and 2, one may also consult [DG70], § II.4, nos 5–6;
    see also [Ja03], § I.7.

[^N.D.E-VII_A-2]: One sees easily that this is equivalent to saying that, for every $x \in X$ and $f_{0}, \cdots, f_{n},
    g \in O_{X,x}$, one has $(ad f_{0})(ad f_{1}) \cdot\cdot\cdot (ad f_{n})(d_{x})(g) = 0$. On the other hand, recall
    that the adjunction isomorphism

    ```text
    θ : Hom_{p_X^{-1}(O_S)}(O_X, u_*(O_Y)) ⥲ Hom_{p_Y^{-1}(O_S)}(u^{-1}(O_X), O_Y)
    ```

    associates with every morphism of $p^{-1}_{X}(O_{S})$-modules $d : O_{X} \to u_{*}(O_{Y})$ the morphism $d' = \epsilon \circ u^{-1}(d)$,
    where $\epsilon$ is the canonical morphism $u^{-1} u_{*}(O_{Y}) \to O_{Y}$. Conversely, for every $p^{-1}_{Y}(O_{S})$-morphism
    $d' : u^{-1}(O_{X}) \to O_{Y}$, one has $\theta^{-1}(d') = u_{*}(d') \circ \eta$, where $\eta$ is the canonical morphism
    $O_{X} \to u_{*} u^{-1}(O_{X})$. It follows that $d$ satisfies $(\ast_{n})$ if and only if $d'$ satisfies:

    ```text
    (∗'_n)                  (ad f₀) ··· (ad f_n)(d')(g) = 0
    ```

    for every open $V$ of $Y$ and $f_{0}, \cdots, f_{n}, g \in u^{-1}(O_{X})(V)$.

[^N.D.E-VII_A-3]: If $X$ and $u$ are quasi-compact, every $S$-deviation of $u$ is therefore of order $\leqslant n$, for
    some integer $n$.

[^N.D.E-VII_A-4]: These remarks have been added, as they will be useful in 1.3, 1.4 and 2.1.

[^N.D.E-VII_A-5]: One will note that with this notation, `de` denotes the composition "$d$ followed by $e$".

[^N.D.E-VII_A-6]: Often, one considers only the $S$-deviations of the morphism $id_{X}$, which form the algebra of
    $S$-differential operators of $X$, cf. 1.4 below. However, the more general framework of $S$-deviations provides a
    convenient "functorial" language for proving statements such as: "if $G$ is an $S$-group, the algebra of
    $S$-differential operators on $G$ invariant under left translation is isomorphic to the algebra of $S$-deviations of
    the unit section $\epsilon : S \to G$, cf. 2.1 and 2.4 below."

[^N.D.E-VII_A-7]: This paragraph has been expanded, with the number 1.2.0 (resp. 1.2.1) being assigned to this
    definition (resp. to the lemma which follows).

[^N.D.E-VII_A-8]: The following has been added, i.e. the notation $\partial_{t}$ has been introduced.

[^N.D.E-VII_A-9]: Explicitly, if $V$ is an affine open of $S$ and $U$ (resp. $U'$) an affine open of $X$ (resp. $T$)
    above $V$, so that $O_{X \times T}(U \times U') = O_{X}(U) \otimes_{O_{S}(V)} O_{T}(U')$, then $d_{T}(U \times U')$
    is the composition:

    ```text
    O_X(U) ⊗_{O_S(V)} O_T(U') ──d(U) ⊗ id→ O_Y(u^{-1} U) ⊗_{O_S(V)} O_T(U') ──→ O_{Y × T}(u^{-1} U × U').
    ```

    The author left to the reader the verification that $d_{T}$ is well-defined, and the editors do the same.

[^N.D.E-VII_A-10]: This paragraph has been expanded with respect to the original; see also N.D.E. (2) in 1.1.1.

[^N.D.E-VII_A-11]: If $\lambda, f$ are local sections of `O_Y` and `O_X`, one has $(\Gamma_{e_{X}})(\lambda \otimes f) =
    \lambda \cdot e(1 \otimes g)$, and this equals $e(\lambda \otimes g)$ since $e$ is `O_Y`-linear.

[^N.D.E-VII_A-12]: This paragraph has been added.

[^N.D.E-VII_A-13]: In this Exposé, the ring $\Gamma(S, O_{S}) = O_{S}(S)$ is denoted $\Gamma(O_{S})$.

[^N.D.E-VII_A-14]: We have modified the original here, which mentioned the sheaf $U \mapsto Dif_{X_{U} / U}$, where $U$
    ranges over the opens of $S$; this is the direct image of $\mathcal{D}if_{X/S}$ by the morphism $p_{X} : X \to S$.

[^N.D.E-VII_A-15]: Via this isomorphism, the $X$-derivations of `∆_{X/S}` correspond, according to 1.3.1, to the
    $S$-derivations of $id_{X}$, i.e., to the $p^{-1}(O_{S})$-derivations of `O_X`.

[^N.D.E-VII_A-16]: One now says "the algebra of distributions" (at the origin) of $G$, cf. [DG70], § II.4, 6.1 and
    [Ja03], I 7.7.

[^N.D.E-VII_A-17]: We have corrected the original, replacing in the diagram $d \times G \times G$ by $G \times d \times
    G$, so that the composition on the left side of the triangle is $(e \times d) \times G$, and so that the map $d
    \mapsto d_{G}$ is an anti-isomorphism of $U(G)$ onto the right-invariant differential operators (cf. 2.3, 2.4
    below); on the other hand, by defining ${}_{G} d$ as the image under $m$ of $G \times d$, one would obtain similarly
    an isomorphism of $U(G)$ onto the left-invariant differential operators (cf. [DG70], § II.4, Th. 6.5). We have
    corrected 2.4 and 2.5 accordingly.

[^N.D.E-VII_A-18]: It would be preferable to call this a *left action*. Indeed, let for example $d$ be an $S$-derivation
    of the origin; according to 1.2.1, $d$ is the composition of the $S$-derivation $(\tau, \partial_{t}) : S \to I_{S}$
    and a morphism $x : I_{S} \to G$ such that $x \circ \tau = \epsilon$ (i.e. $x \in Lie(G/S)(S)$), and then $d_{G}$ is
    the derivation of `O_G` which sends a local section $\phi$ to the section $g \mapsto \partial_{t} \phi(xg)$.
    Moreover, with this terminology, one could say: "the left action commutes with right translations".

[^N.D.E-VII_A-19]: We have corrected "isomorphism" to "anti-isomorphism", and added assertion (ii), cf. N.D.E. (17).

[^N.D.E-VII_A-20]: i.e., $G$ acts on itself on the left by right translations.

[^N.D.E-VII_A-21]: In what follows, we have corrected the original, which referred to the square formed by the morphisms
    $p$, $p$, $\eta$, and $pr_{1}$, instead of $\epsilon$, $\eta$, `∆` and $p$.

[^N.D.E-VII_A-22]: In this paragraph, we have modified the order, beginning by defining the map $\alpha : Lie(G) \to
    U(G)$, and we have corrected the original as indicated in N.D.E. (17).

[^N.D.E-VII_A-23]: In this Exposé, if $G$ (resp. $X$) is an $S$-group scheme (resp. an $S$-scheme), the "Lie algebra"
    $Lie(G)$ (resp. $Lie(\operatorname{Aut} X)$) denotes, with the notations of Exposé II, $Lie(G/S)(S)$ (resp.
    $Lie(\operatorname{Aut}_{S}(X)/S)(S)$); it is a $\Gamma(O_{S})$-Lie algebra, according to II, 4.11 and 3.14.

[^N.D.E-VII_A-24]: See also II, 4.11.

[^N.D.E-VII_A-25]: There are examples of Lie algebras $\mathfrak{g}$ over a ring $A$, such that the map $\mathfrak{g}
    \to U(\mathfrak{g})$ is not injective, cf. [BLie], § I.2, Ex. 9. The above result shows (since $\alpha$ factors
    through $Lie(G) \to U(Lie(G)) \to U(G)$) that this cannot happen for "algebraic" Lie algebras, i.e., of the form
    $Lie(G)$, where $G$ is an $A$-group scheme.

[^N.D.E-VII_A-26]: One also says "cogebra", cf. [BAlg], III § 11.1. On the other hand, one will note that in this Exposé
    (as well as in VII_B), we place ourselves in the category of cocommutative coalgebras (i.e., those satisfying
    condition (i)), which is crucial for defining the product and the notion of group coalgebra (cf. 3.1.0 and 3.2).

[^N.D.E-VII_A-27]: We have added the numbering 3.1.0, for later references.

[^N.D.E-VII_A-28]: The following has been added. Let us also recall that, to show that $\mathcal{U} \otimes \mathcal{V}$
    is indeed the product of $\mathcal{U}$ and $\mathcal{V}$ in the category of cocommutative `O_S`-cogebras, one
    verifies that if one has an arbitrary `O_S`-cogebra $\mathcal{E}$ and morphisms of cogebras $f : \mathcal{E} \to
    \mathcal{U}$ and $g : \mathcal{E} \to \mathcal{V}$, then every morphism of cogebras $\phi : \mathcal{E} \to
    \mathcal{U} \otimes \mathcal{V}$ such that $pr_{\mathcal{U}} \circ \phi = f$ and $pr_{\mathcal{V}} \circ \phi = g$
    is necessarily equal to `(f ⊗ g) ∘ ∆_ℰ`, and this is a morphism of cogebras if and only if it equals
    `(g ⊗ f) ∘ ∆_ℰ`.

[^N.D.E-VII_A-29]: For every $x \otimes y \in \Gamma(T, \mathcal{U}_{T}) \otimes_{O(T)} \Gamma(T, \mathcal{U}_{T})$, its
    image in $\Gamma(T, \mathcal{U}_{T} \otimes_{O_{T}} \mathcal{U}_{T})$ is again denoted $x \otimes y$.

[^N.D.E-VII_A-30]: We have added the numbering 3.1.2.1, for later references. Note moreover that the $S$-functor
    $\operatorname{Spec}^{*} \mathcal{U}$ is a sheaf for the Zariski topology (and even for the (fpqc) topology if
    $\mathcal{U}$ is a quasi-coherent `O_S`-module).

[^N.D.E-VII_A-31]: i.e. endowed with the multiplication $m'_{\mathcal{U}} = m_{\mathcal{U}} \circ \sigma$.

[^N.D.E-VII_A-32]: We have added this scholium, implicit in the original.

[^N.D.E-VII_A-33]: The group $S$-functor $\operatorname{Spec}^{*} \mathcal{U}(\mathcal{L})$ is not representable in
    general, but one will see later (5.5) that if $S$ is a scheme of characteristic $p$, if $\mathcal{L}$ is finite
    locally free over `O_S` and if $\mathcal{U}_{p}(\mathcal{L})$ is its restricted enveloping algebra (cf. 5.3), then
    $\operatorname{Spec}^{*} \mathcal{U}_{p}(\mathcal{L})$ is represented by a finite and locally free $S$-group.

[^N.D.E-VII_A-34]: We have expanded this paragraph.

[^N.D.E-VII_A-35]: Note that the second condition is a consequence of the first, since the first entails that
    `u = (id ⊗ ε) ∆(u) = u + ε(u)`, whence $\epsilon(u) = 0$.

[^N.D.E-VII_A-36]: The structure of `O_S`-module on `Lie G` is defined in II, Prop. 3.6.

[^N.D.E-VII_A-37]: We have added this proposition, which summarizes the preceding discussion.

[^N.D.E-VII_A-39]: We have added the numbering 4.0, for later references.

[^N.D.E-VII_A-40]: i.e. for every morphism of $\mathbb{F}_{p}$-schemes $f : Y \to X$, the diagram below is commutative:

    ```text
                       f
              Y  ────────→  X
       fr(Y)                fr(X)
                       f
              Y  ────────→  X.
    ```

[^N.D.E-VII_A-41]: One says that $fr(X)$ is the "absolute" Frobenius morphism of $X$, to distinguish it from the
    "relative" Frobenius morphism $Fr(X/S)$ introduced below.

[^N.D.E-VII_A-42]: We have expanded the original in what follows.

[^N.D.E-VII_A-43]: We have expanded the original in what follows.

[^N.D.E-VII_A-45]: For the content of nos 4.2 and 4.3, one may also consult [DG70], § IV.3, nos 4–6.

[^N.D.E-VII_A-46]: In the original, this morphism (resp. the relative Frobenius morphism) was denoted $F'$ (resp. $F$).

[^VII_A-4-1]: D. Lazard, C. R. Acad. Sc. Paris 258, 1964, p. 6313–6316.

[^N.D.E-VII_A-47]: See also: D. Lazard, Bull. Soc. Math. France 97 (1969), 81–128, or: [BAlg], X § 1.6, Th. 1.

[^N.D.E-VII_A-48]: Since this does not appear explicitly in VII_B, one refers to [DG70], § IV.3, Prop. 4.11.

[^N.D.E-VII_A-49]: We have modified the order, by first introducing the objects appearing in the diagram that follows.

[^N.D.E-VII_A-50]: See also [DG70], § IV.3, 4.9.

[^N.D.E-VII_A-51]: cf. P. Cartier, Exemples d'hyperalgèbres, Sém. Sophus Lie 1955/56, Exp. 3 (accessible on the Numdam
    site: <http://www.numdam.org>).

[^N.D.E-VII_A-52]: We have inserted the explanation that follows, taken from [DG70], § II.7, 3.2.

[^N.D.E-VII_A-53]: In this paragraph, we have modified the order, first stating the result, then detailing the proof.

[^N.D.E-VII_A-54]: i.e., $x r \otimes_{\pi} 1 = x \otimes_{\pi} r^{p}$ and $r \cdot (x \otimes_{\pi} 1) = x
    \otimes_{\pi} r$, for $x \in \mathfrak{g}$, $r \in R$.

[^N.D.E-VII_A-55]: i.e. `∆_𝔤(x) = x ⊗ 1 + 1 ⊗ x` for every $x \in \mathfrak{g}$; in particular, the comultiplication
    `∆_𝔤` is indeed cocommutative …

[^N.D.E-VII_A-56]: We have transformed § 5.4.1 of the original into this § 5.5: on the one hand, Proposition 5.5.1
    combines the results of Section 5 and Proposition 3.2.3 and contains Lemma 7.3 of the original; on the other hand,
    the proof of 5.5.3 (ii) takes up, in expanded form, that of the implication (i) ⇒ (ii) in Theorem 7.4 below.

[^N.D.E-VII_A-57]: One can also show directly (without the intermediary of $Dif_{G/S}$) that the Lie algebra of
    derivations of $G$ at the origin (isomorphic to $Lie(G/S)(S)$ according to 2.5) is stable under raising to the
    $p$-th power in $U(G)$: this is done in 6.2 below.

[^N.D.E-VII_A-58]: We have expanded the original in what follows.

[^N.D.E-VII_A-59]: We have corrected $x$ to $y'$.

[^N.D.E-VII_A-60]: We have added the numbering 6.4.5, and expanded the original.

[^N.D.E-VII_A-61]: For the results of this section, one may also consult [DG70], § II.7, nos 3-4.

[^N.D.E-VII_A-62]: We have added this definition (cf. [DG70], § II.4, 7.1), which will be used in 7.2.1.

[^N.D.E-VII_A-63]: We have simplified the original, taking into account the additions made in 5.5.

[^N.D.E-VII_A-64]: We have expanded the original in what follows. For another proof, see [DG70], § II.7, 3.9.

[^N.D.E-VII_A-65]: We have expanded the original in what follows.

[^N.D.E-VII_A-66]: In what follows, we have expanded (and simplified) the original, taking into account VI_B, 11.6.1.

[^N.D.E-VII_A-67]: We have added the following. (The original indicated "the case of $\mathcal{W}(\mathcal{F})$ is
    analogous").

[^N.D.E-VII_A-68]: In order not to modify the numbering, the statement 7.3 has been preserved, although it has been
    included, with its proof, in 5.5.1.

[^N.D.E-VII_A-69]: If $G$ is affine over $S$ and if $\mathcal{I}$ denotes the augmentation ideal of $\mathcal{A}(G)$,
    then $\mathcal{I}' / \mathcal{I}'^{2}$ is identified with $\epsilon^{*}_{G}(\mathcal{I} / \mathcal{I}^{2})$, cf.
    loc. cit.

[^N.D.E-VII_A-70]: We have added the following sentence.

[^N.D.E-VII_A-71]: We have added, on the one hand, assertion (i'), implicit in the original, and on the other hand,
    assertions (iii') and (iv), pointed out by O. Gabber; assertion (iv) takes up a footnote of the original, which
    indicated: "The condition on $\omega_{G/S}$ is in fact useless, as one sees easily by reducing to the case where $S$
    is local with residue field $k$, and applying the theorem to the case of the group $G_{k}$". As pointed out by
    Gabber, this is inaccurate without a flatness hypothesis: if $A$ is an Artinian local ring of characteristic $p > 0$
    and $J$ a proper non-zero ideal of $A$, let $H$ be the subgroup $\operatorname{Spec} A[x] / (x^{p}, J x)$ of
    $\alpha_{p, A}$ (i.e. for every $A$-algebra $R$, $H(R) = { x \in R | x^{p} = 0 and J x = 0}$), then $H$ is not flat
    over $A$ so is not of the form $\mathfrak{G}_{p}(\mathcal{L})$, where $\mathcal{L}$ is a free $p$-Lie algebra of
    finite rank over $A$.

[^N.D.E-VII_A-72]: We have expanded (and simplified) the original in what follows.

[^N.D.E-VII_A-73]: We have added this paragraph to prove that (iv) ⇒ (iii), cf. N.D.E. (71).

[^N.D.E-VII_A-74]: We have added this remark.

[^N.D.E-VII_A-75]: We have added the numbering 8.1.1 to 8.1.3, to highlight the results stated there.

[^N.D.E-VII_A-76]: We have expanded what follows, as well as the proof of the corollary below.

[^N.D.E-VII_A-77]: Moreover, according to VI_A, 3.2, $\mathfrak{G}_{p}(\mathcal{L}_{2})$ represents the (fppf) sheaf
    quotient of $\mathfrak{G}_{p}(\mathcal{L}_{1})$ by $\mathfrak{G}_{p}(\mathcal{L}_{0})$.

[^N.D.E-VII_A-78]: We have added this remark, pointed out by O. Gabber, which will be useful in 8.3.1.

[^N.D.E-VII_A-79]: i.e. $\pi$ is faithfully flat and $i$ is an isomorphism of $G'$ onto $Ker \pi$, so that `G''`
    represents the (fppf) sheaf quotient of $G$ by $G'$, cf. VI_A, 3.2 and 5.2.

[^N.D.E-VII_A-80]: We have replaced "algebraic" by "locally of finite type".

[^N.D.E-VII_A-81]: We have made explicit the equivalence between (ii) and (iii) and we have expanded the proof.

[^N.D.E-VII_A-82]: We have changed in the statement "étale at the origin" to "étale", and we have added the following
    sentence.

[^N.D.E-VII_A-83]: We have expanded the original in what follows.

[^N.D.E-VII_A-84]: We have added this corollary, indicated implicitly in the original by: "(confer 8.4)". For another
    proof of the corollary, not using 8.5, see for example [TO70], Lemma 5.

[^N.D.E-VII_A-85]: We have expanded the original in the paragraph that follows.

[^N.D.E-VII_A-86]: We have expanded the original in what follows, replacing the notion of preorder by the equivalent
    notion of ordered partition.

[^N.D.E-VII_A-87]: We have added this corollary, signaled in Exp. VIII, Remark 7.3.1.

[^N.D.E-VII_A-44]: $\mathcal{A} \otimes_{\pi} O_{S}$ denotes the `O_S`-algebra obtained by extension of scalars $\pi :
    O_{S} \to O_{S}$, i.e., one has: $ax \otimes_{\pi} 1 = a \otimes_{\pi} x^{p}$, and $x \cdot (a \otimes_{\pi} 1) = a
    \otimes_{\pi} x$.
