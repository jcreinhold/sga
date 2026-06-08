# Exposé XXIII. Reductive groups: uniqueness of pinned groups

<!-- label: III.XXIII -->

*by M. Demazure*

<!-- original page 263 -->

[^N.D.E-XXIII-0]

The aim of this Exposé is the proof of the uniqueness theorem (Theorem 4.1). This was proved by Chevalley in the case of
an algebraically closed field; the method of reduction to rank two used here is also due to Chevalley (see *Bible*, Exp.
23 and 24). Along the way, we obtain an explicit description of reductive groups by generators and relations (3.5).

## 1. Pinnings

<!-- label: III.XXIII.1 -->

**Definition 1.1.** *Let $S$ be a scheme and $(G, T, M, R)$ an $S$-split group (XXII, 1.13). One calls*
pinning[^N.D.E-XXIII-butterfly] *of this split group the datum of a system $\Delta$ of simple roots of $R$ and, for each
$\alpha \in \Delta$, a section $X_{\alpha} \in \Gamma(S, g_{\alpha})^{\times}$.*[^N.D.E-XXIII-butterfly-anchor]

<!-- label: III.XXIII.1.1 -->

In other words, a pinning of the reductive group $G$ over the nonempty scheme $S$ is the datum of:

(i) a maximal torus $T$,

(ii) an abelian group $M$ and an isomorphism $T \simeq D_{S}(M)$,

(iii) a system of roots $R$ of $G$ with respect to $T$,

(iv) a system of simple roots $\Delta$ of $R$,

(v) an $X_{\alpha} \in \Gamma(S, g_{\alpha})^{\times}$ for every $\alpha \in \Delta$, that is, of a

```text
u_α = exp_α(X_α) ∈ U_α^×(S)    for every α ∈ Δ,
```

<!-- original page 264 -->

satisfying condition (D 1) of Exp. XXII, 1.13 (indeed condition (D 2) of *loc. cit.* is automatically
satisfied[^N.D.E-XXIII-1]).

Every split group admits a pinning; in particular, every reductive group is locally pinnable for the étale topology.

### 1.2

<!-- label: III.XXIII.1.2 -->

If $G$ is a pinned $S$-group — that is, an $S$-split group equipped with a pinning — it is canonically endowed with the
system of positive roots $R^{+}$ defined by $\Delta$, the corresponding Borel subgroup $B = B_{R^{+}}$, the opposite
Borel subgroup $B^{-} = B_{R^{-}}$, the unipotent groups $U = B_{u}$, $U^{-} = (B^{-})_{u}$, the open set $U^{-} \cdot T
\cdot U$, etc. Likewise, for each $\alpha \in \Delta$, one has a canonical isomorphism of vector groups

```text
p_α : G_{a, S} ⥲ U_α,    x ↦ exp_α(x X_α) = u_α^x,
```

normalized by $T$ with multiplier $\alpha$, and whose datum is equivalent to that of $X_{\alpha}$ (Exp. XXII, 1.1).

By duality, one deduces an $X_{-\alpha} \in \Gamma(S, g_{-\alpha})^{\times}$ and an isomorphism

```text
p_{-α} : G_{a, S} ⥲ U_{-α}
```

which is the contragredient of the preceding one (Exp. XXII, 1.3). We shall set (Exp. XX, 3.1)

```text
w_α = w_α(X_α) = p_α(1) p_{-α}(-1) p_α(1) = p_{-α}(-1) p_α(1) p_{-α}(-1).
```

One then has (*loc. cit.* 3.1, 3.7)

```text
w_α^2 = α^*(-1),    int(w_α) t = s_α(t) = t · α^*(α(t)^{-1}),
```

```text
int(w_α) p_α(x) = p_{-α}(-x) = p_{-α}(x)^{-1},
Ad(w_α) X_α = -X_{-α},
```

```text
int(w_α) p_{-α}(x) = p_α(-x) = p_α(x)^{-1},
Ad(w_α) X_{-α} = -X_α.
```

<!-- original page 265 -->

We shall use the preceding notation systematically in what follows.

**Definition 1.3.** *Let $S$ be a scheme and $(G, T, M, R, \Delta, (X_{\alpha}))$ and $(G', T', M', \cdots)$ two pinned
$S$-groups. One says that the morphism of split groups (Exp. XXII, 4.2.1)*

$$ f : G \to G' $$

*is* compatible with the pinnings, *or that it defines a* morphism of pinned groups, *if the bijection $d : R \to R'$
associated with it (cf. loc. cit.) satisfies $d(\Delta) = \Delta'$ and if, for every $\alpha \in \Delta$, one has*

```text
f(exp_α(X_α)) = exp_{d(α)}(X'_{d(α)}),    i.e.    f(u_α) = u'_{d(α)}.
```

[^N.D.E-XXIII-2]

<!-- label: III.XXIII.1.3 -->

<!-- original page 178 source / page 179 source — heading transition -->

### 1.4

<!-- label: III.XXIII.1.4 -->

If we denote by $q(\alpha)$ the integer of *loc. cit.*, we therefore have

```text
f(p_α(x)) = p'_{d(α)}(x^{q(α)})    for    α ∈ Δ,
```

and consequently

```text
f(p_{-α}(x)) = p'_{-d(α)}(x^{q(α)}),    f(w_α) = w'_{d(α)}.
```

Recall (Exp. XXII, 4.2) that, for every $\alpha \in R$ and all $z \in G_{m}(S')$, $t \in T(S')$,

```text
f(α^*(z)) = d(α)^*(z)^{q(α)} = d(α)^*(z^{q(α)}),    d(α)(f(t)) = α(t)^{q(α)}.
```

### 1.5

<!-- label: III.XXIII.1.5 -->

<!-- original page 266 -->

We shall call a *pinned root datum* a root datum endowed with a system of simple roots, and a *$p$-morphism of pinned
root data* a $p$-morphism of root data (Exp. XXI, 6.8) sending simple roots to simple roots.

If $G$ is a pinned $S$-group, we denote by $R(G)$ the corresponding pinned root datum (this is the root datum of Exp.
XXII, 1.14 equipped with $\Delta$). Let $p$ be the integer defined in Exp. XXII, 4.2.2. One then has:

**Scholium 1.6.** *The correspondence $G \mapsto R(G)$ defines a functor from the category of pinned reductive
$S$-groups to that of pinned root data (with $p$-morphisms as morphisms).*

<!-- label: III.XXIII.1.6 -->

### 1.7. The pinned groups $Z_{\Delta_{1}}$

<!-- label: III.XXIII.1.7 -->

Let $\Delta_{1}$ be a subset of the system of simple roots $\Delta$ of the pinned group $G$. Let $T_{\Delta_{1}}$ be the
maximal torus of $\bigcap_{\alpha \in \Delta_{1}} Ker(\alpha)$; set

$$ Z_{\Delta_{1}} = Centr_{G}(T_{\Delta_{1}}). $$

Set $R' = \mathbb{Z} \cdot \Delta_{1} \cap R$; one knows (Exp. XXII, 5.10.7) that $Z_{\Delta_{1}}$ is a reductive
$S$-group with radical $T_{\Delta_{1}}$, that `(T, M, R')` is a splitting of it, and $\Delta_{1}$ a system of simple
roots. It follows that $(Z_{\Delta_{1}}, T, M, R', \Delta_{1}, (X_{\alpha})_{\alpha \in \Delta_{1}})$ is a pinned
$S$-group. We shall always equip $Z_{\Delta_{1}}$ with this pinning. In particular, we shall consider the groups

```text
Z_α = Z_{{α}},    Z_{αβ} = Z_{{α, β}}.
```

We denote by $B_{\Delta_{1}} = B \cap Z_{\Delta_{1}}$; one knows (*loc. cit.*) that this is the canonical Borel
subgroup[^N.D.E-XXIII-3] of $Z_{\Delta_{1}}$, and that its unipotent part is $U_{\Delta_{1}} = U \cap Z_{\Delta_{1}}$.
In particular,

$$ B_{\alpha} = T \cdot U_{\alpha}. $$

<!-- original page 267 -->

We shall denote

```text
U_{αβ} = U_{{α, β}} = U ∩ Z_{αβ} = ∏_{γ ∈ R^+_{αβ}} U_γ,
```

where $R^{+}_{\alpha \beta}$ denotes the set of positive roots that are linear combinations of $\alpha$ and $\beta$.

Now let $f : G \to G'$ be a morphism of pinned $S$-groups. If $d : R \to R'$ is the corresponding bijection and if
$\Delta_{1}$ is a subset of $\Delta$, then $d(\Delta_{1}) = \Delta'_{1}$ is a subset of $\Delta'$, and it is clear that
$f$ sends $T_{\Delta_{1}}$ into $T'_{\Delta'_{1}}$, hence $Z_{\Delta_{1}}$ into $Z'_{\Delta'_{1}}$. The corresponding
$S$-morphism

$$ f_{\Delta_{1}} : Z_{\Delta_{1}} \to Z'_{d(\Delta'_{1})} $$

is compatible with the canonical pinnings; it defines a morphism of pinned root data

```text
R(f_{Δ_1}) : R(Z_{Δ_1}, T, M, …) → R(Z_{Δ'_1}, T', M', …)
```

and the underlying morphisms $M' \to M$ of $R(f)$ and $R(f_{\Delta_{1}})$ coincide.

### 1.8. Study of the group $Norm_{G}(T)$

<!-- label: III.XXIII.1.8 -->

For each pair $(\alpha, \beta)$ of simple roots, denote by $n_{\alpha \beta}$ the order of the element $s_{\alpha}
s_{\beta}$ of the Weyl group $W$. In particular, $n_{\alpha \alpha} = 1$. One has therefore $(w_{\alpha}
w_{\beta})^{n_{\alpha \beta}} \in T(S)$.

**Definition 1.8.1.** *For every $(\alpha, \beta) \in \Delta \times \Delta$, one sets*

```text
t_{αβ} = (w_α w_β)^{n_{αβ}} ∈ T(S).
```

*Moreover, one sets (Exp. XX, 3.1)*

```text
t_α = t_{αα} = w_α^2 = α^*(-1) ∈ T(S).
```

<!-- label: III.XXIII.1.8.1 -->

<!-- original page 268 -->

**Proposition 1.8.2.** *Let $H$ be an $S$-functor in groups transforming direct sums of schemes into products (for
example a sheaf for the Zariski topology). Let*

$$ f_{T} : T \to H $$

*be a morphism of groups and $h_{\alpha} (\alpha \in \Delta)$ elements of $H(S)$. In order that there exist a morphism
of groups (necessarily unique)*

$$ f_{N} : Norm_{G}(T) \to H $$

*inducing $f_{T}$ on $T$ and such that $f(w_{\alpha}) = h_{\alpha}$ for $\alpha \in \Delta$, it is necessary and
sufficient that the following two conditions be satisfied:*

*(i) For every $\alpha \in \Delta$,*

```text
f_T(s_α(t)) = h_α f_T(t) h_α^{-1}
```

*for every $t \in T(S')$, $S' \to S$ (i.e. $f_{T} \circ s_{\alpha} = int(h_{\alpha}) \circ f_{T}$).*

*(ii) For every $(\alpha, \beta) \in \Delta \times \Delta$,*

$$ f_{T}(t_{\alpha \beta}) = (h_{\alpha} h_{\beta})^{n_{\alpha \beta}}. $$

<!-- label: III.XXIII.1.8.2 -->

*Proof.* Indeed, equip `(Sch)` with the topology $\mathcal{T}$ generated by the pretopology whose covering families are
the direct sums; the hypothesis of the statement says that $H$ is a $\mathcal{T}$-sheaf. Let $L$ be the free group with
generators $(m_{\alpha})_{\alpha \in R}$ and `L_1` the invariant subgroup generated by the elements $(m_{\alpha}
m_{\beta})^{n_{\alpha \beta}}$, $(\alpha, \beta) \in \Delta \times \Delta$. Let $g : L \to W$ be the morphism defined by
$g(m_{\alpha}) = s_{\alpha}$; one knows (Exp. XXI, 5.1) that $g$ induces an isomorphism `ḡ` of $L/L_{1}$ onto $W$. Make
$L$ act on $T$ through $g$ (or, equivalently, by $m_{\alpha} \cdot t = s_{\alpha}(t)$). Let `L_S` be the constant group
defined by $L$; consider the semidirect product $T \cdot L_{S} = N$ for the preceding operation. One has a morphism of
$S$-groups

```text
h : T · L_S = N → Norm_G(T)
```

unique such that $h(m_{\alpha}) = w_{\alpha}$, $h(t) = t$ for every $t \in T(S')$, $S' \to S$. Let `N_1` be the
invariant subsheaf of groups of $N$ generated by the

<!-- original page 269 -->

```text
t_{αβ}^{-1} · (m_α m_β)^{n_{αβ}},    (α, β) ∈ Δ × Δ.
```

One evidently has $N_{1} \subset Ker h$; consider the induced morphism

$$ h_{1} : N/N_{1} \to Norm_{G}(T). $$

Let us prove that $h_{1}$ is an isomorphism. Since $h$ induces on $T$ the canonical immersion, which is a monomorphism,
the canonical morphism

$$ T \to N/N_{1} $$

is also a monomorphism, hence induces an isomorphism of $T$ onto $TN_{1}/N_{1}$. For the same reason, $h_{1}$ induces an
isomorphism of $TN_{1}/N_{1}$ onto $T$; to prove that $h_{1}$ is an isomorphism, it therefore suffices to verify that
the corresponding morphism

$$ h_{2} : N/TN_{1} \to Norm_{G}(T)/T $$

is an isomorphism. Now `TN_1` is the invariant $\mathcal{T}$-subsheaf of groups of $N$ generated by $T$ and the
$(m_{\alpha} m_{\beta})^{n_{\alpha \beta}}$, that is, the $\mathcal{T}$-subsheaf generated by $T$ and `L_1`, that is, $T
\cdot (L_{1})_{S}$. The morphism $h_{2}$ is therefore identified with the morphism

$$ \bar{g} : L_{S}/(L_{1})_{S} \to W_{S} $$

which is an isomorphism by construction.

The proof of 1.8.2 is now easy; the conditions are evidently necessary. Let us prove that they are sufficient. Condition
(i) shows that there exists a morphism

$$ u : N \to H $$

such that $u(m_{\alpha}) = h_{\alpha}$ for $\alpha \in \Delta$, and $u|_{T} = f_{T}$. Condition (ii) says that $u$
vanishes on `N_1`, which yields the result at once.

### 1.9. Faithfulness of the functor $R$

<!-- label: III.XXIII.1.9 -->

<!-- original page 270 -->

**Proposition 1.9.1.** *The functor $R$ of 1.6 is faithful: if*

```text
f, g : G ⇒ G'
```

*are two morphisms of pinned groups such that $R(f) = R(g)$, then $f = g$.*

<!-- label: III.XXIII.1.9.1 -->

Indeed, $f$ and $g$ coincide on $T$, $U_{\alpha} (\alpha \in \Delta)$ and $U_{-\alpha} (\alpha \in \Delta)$; it
therefore suffices to apply:

**Lemma 1.9.2.** *Let $S$ be a scheme, $G$ a pinned reductive $S$-group, $H$ an $S$-presheaf in groups, separated for
(fppf). Let*

```text
f, g : G ⇒ H
```

*be two morphisms of $S$-groups. The following conditions are equivalent:*

*(i) $f = g$.*

*(ii) $f$ and $g$ coincide on $T$, on each $U_{\alpha} (\alpha \in \Delta)$, on each $U_{-\alpha} (\alpha \in \Delta)$.*

*(iii) $f$ and $g$ coincide on $T$, on each $U_{\alpha} (\alpha \in \Delta)$, and $f(w_{\alpha}) = g(w_{\alpha})$ for
each $\alpha \in \Delta$.*

<!-- label: III.XXIII.1.9.2 -->

Indeed, (i) ⇒ (ii) is trivial, (ii) ⇒ (iii) follows at once from the definition of $w_{\alpha}$ (1.2). It remains to
prove (iii) ⇒ (i). If $\alpha \in R$, there exists a sequence ${\alpha_{i}} \subset \Delta$ with $\alpha =
s_{\alpha_{1}} s_{\alpha_{2}} \cdots s_{\alpha_{n}}(\alpha_{n+1})$, hence

```text
U_α = int(w_{α_1} ⋯ w_{α_n}) U_{α_{n+1}},
```

which shows that $f$ and $g$ coincide on each $U_{\alpha}$. It follows that $f$ and $g$ coincide on $\Omega$, hence
coincide (Exp. XXII, 4.1.11).

**Remark 1.9.3.** *If $G$ is semisimple, one may, in (ii) and (iii), drop the hypothesis that $f$ and $g$ coincide on
$T$. Indeed, $G$ is generated as an (fppf) sheaf by the $U_{\alpha}$, $\alpha \in R$ (Exp. XXII, 6.2.2 (a)).*

<!-- label: III.XXIII.1.9.3 -->

## 2. Generators and relations for a pinned group

<!-- label: III.XXIII.2 -->

<!-- original page 271 -->

In this section, we fix a pinned $S$-group $G$. If $\alpha, \beta \in \Delta$, we shall use the notation $Z_{\alpha}$,
$Z_{\alpha \beta}$, $U_{\alpha \beta}$, $R^{+}_{\alpha \beta}$ of 1.7.

**Theorem 2.1.** *Let $S$ be a scheme, $G$ a pinned $S$-group, $H$ an $S$-sheaf in groups for (fppf). Let*

```text
f_N : Norm_G(T) → H,    f_α : U_α → H,    α ∈ R,
```

*be morphisms of groups. In order that there exist a morphism of groups (necessarily unique)*

$$ f : G \to H $$

*extending $f_{N}$ and the $f_{\alpha} (\alpha \in R)$, it is necessary and sufficient that the following conditions be
satisfied:*

*(i) For every $\alpha \in \Delta$ and every $\beta \in R$,*

```text
int(f_N(w_α)) ∘ f_β = f_{s_α(β)} ∘ int(w_α).
```

*(ii) For every $\alpha \in \Delta$, there exists a morphism of groups*

$$ F_{\alpha} : Z_{\alpha} \to H $$

*extending $f_{\alpha}$, $f_{-\alpha}$ and $f_{N}|_{Norm_{Z_{\alpha}}(T)}$.*

*(iii) For every pair $(\alpha, \beta) \in \Delta \times \Delta$, there exists a morphism of groups $U_{\alpha \beta}
\to H$ inducing $f_{\gamma}$ on $U_{\gamma}$ for every $\gamma \in R^{+}_{\alpha \beta}$ (i.e. $U_{\gamma} \subset
U_{\alpha \beta}$).*

<!-- label: III.XXIII.2.1 -->

### 2.1.1. Proof

<!-- label: III.XXIII.2.1.1 -->

The conditions of the statement are evidently necessary. Choose on the other hand a structure of totally ordered group
on $\Gamma_{0}(R)$ such that the roots `> 0` are the elements of $R^{+}$ (Exp. XXI, 3.5.6); every product indexed by a
subset of $R$ will be taken relative to this order.

<!-- original page 272 -->

Denote by $f_{T}$ the restriction of $f_{N}$ to $T$, and consider the morphism

$$ f : \Omega \to H $$

defined set-theoretically by

```text
f(∏_{α ∈ R^-} y_α · t · ∏_{α ∈ R^+} x_α) = ∏ f_α(y_α) · f_T(t) · ∏ f_α(x_α).
```

Any morphism satisfying the conditions of the statement must extend $f$; on the other hand any morphism of groups $f : G
\to H$ extending $f$ also extends $f_{N}$: indeed, extending $f_{\alpha}$ and $f_{-\alpha}$, it satisfies $f(w_{\alpha})
= F_{\alpha}(w_{\alpha}) = f_{N}(w_{\alpha})$, and it extends $f_{T}$ by hypothesis. By Exp. XXII, 4.1.11 (ii), one is
therefore reduced to proving:

**Proposition 2.1.2.** *The morphism $f : \Omega \to H$ defined above is "generically multiplicative"; more precisely,
for every $S' \to S$ and all $x, y \in \Omega(S')$ such that $xy \in \Omega(S')$, one has $f(xy) = f(x) f(y)$.*

<!-- label: III.XXIII.2.1.2 -->

**Lemma 2.1.3.** *Let $n \in Norm_{G}(T)(S')$, $S' \to S$, and let $\alpha, \beta \in R$ be such that $int(n) U_{\alpha}
= U_{\beta}$ (i.e. $n(\alpha) = \beta$); then*

```text
int(f_N(n)) ∘ f_α = f_β ∘ int(n).
```

<!-- label: III.XXIII.2.1.3 -->

Indeed, it suffices to verify the formula for a system of generators of the sheaf $Norm_{G}(T)$; it is true for each
$w_{\alpha}$, $\alpha \in \Delta$ (by 2.1 (i)), so it suffices to do it for $n \in T(S')$. This is trivial by 2.1 (ii)
if $\alpha$ is simple; otherwise, one takes a $w \in W$ such that $w^{-1}(\alpha) \in \Delta$; writing $w$ as a product
of simple reflections,[^N.D.E-XXIII-4] one is reduced to proving that if the formula is true for $\alpha$ and for every
$n$, it is also true for $w_{\alpha_{0}}(\alpha)$ and $t \in T(S')$, where $\alpha_{0} \in \Delta$. Now, by 2.1 (i),

```text
int(f_N(t)) ∘ f_{w_{α_0}(α)} = int(f_N(t w_{α_0})) ∘ f_α ∘ int(w_{α_0}^{-1})
                             = f_{w_{α_0}(α)} ∘ int(t w_{α_0}) ∘ int(w_{α_0}^{-1}).
```

**Lemma 2.1.4.** *The restriction of $f$ to $U$ (resp. $U^{-}$) is a morphism of groups. In particular, this restriction
is independent of the order chosen on the roots.*

<!-- label: III.XXIII.2.1.4 -->

<!-- original page 273 -->

It suffices to give the proof for $U$. By virtue of Exp. XXII, 5.5.8, it suffices to verify that for every pair $\alpha
< \beta$ of positive roots, one has for all $x_{\alpha} \in U_{\alpha}(S')$, $x_{\beta} \in U_{\beta}(S')$, $S' \to S$,

```text
f_β(x_β) f_α(x_α) f_β(x_β^{-1}) = f(x_β x_α x_β^{-1}).
```

By Exp. XXII, 5.5.2, there exist $x_{\gamma} \in U_{\gamma}(S')$ ($\gamma = i\alpha + j\beta \in R$, $i > 0$, $j
\geqslant 0$[^N.D.E-XXIII-5]) such that

```text
x_β x_α x_β^{-1} = ∏_γ x_γ,
```

and we must therefore verify the relation

```text
f_β(x_β) f_α(x_α) f_β(x_β^{-1}) = ∏_{γ = iα + jβ, i > 0, j ⩾ 0} f_γ(x_γ).
```

By Exp. XXI, 3.5.4, there exists $w \in W$ such that $w(\alpha) = \alpha_{0} \in \Delta$, $w(\beta) \in A_{\alpha_{0}
\beta_{0}}$ (notation of 1.7), where $\beta_{0} \in \Delta$. Lifting $w$ to an $n \in Norm_{G}(T)(S)$ (by Exp. XXII,
3.8), it suffices to verify the preceding relation after conjugation by $f_{N}(n)$. By 2.1.3, one is therefore reduced
to the case $\alpha, \beta \in R^{+}_{\alpha_{0} \beta_{0}}$, a case in which we conclude by condition 2.1 (iii).

**Lemma 2.1.5.** *Let $n \in Norm_{G}(T)(S)$ be such that $int(n) U = U^{-}$ (i.e. $n$ is the symmetry of the Weyl
group[^N.D.E-XXIII-6] (Exp. XXI, 3.6.14)). For every $u \in U(S')$, $S' \to S$ (resp. $u \in U^{-}(S')$, $S' \to S$),
one has*

```text
f(n u n^{-1}) = f_N(n) f(u) f_N(n^{-1}).
```

<!-- label: III.XXIII.2.1.5 -->

Immediate by 2.1.3 and 2.1.4.

<!-- original page 274 -->

**Lemma 2.1.6.** *Let $u \in B(S')$, $v \in B^{-}(S')$, $g \in \Omega(S')$, $S' \to S$. Then*

```text
f(v g u) = f(v) f(g) f(u).
```

<!-- label: III.XXIII.2.1.6 -->

Indeed, set $v = v_{1} t_{1}$, $g = v_{2} t_{2} u_{2}$, $u = t_{3} u_{3}$, with $v_{i} \in U^{-}(S')$, $t_{i} \in
T(S')$, $u_{i} \in U(S')$. One has

```text
f(v) f(g) f(u) = f(v_1) f_T(t_1) f(v_2) f_T(t_2) f(u_2) f_T(t_3) f(u_3),
```

on the one hand, and

```text
f(v g u) = f(v_1 t_1 v_2 t_1^{-1} t_1 t_2 t_3 t_3^{-1} u_2 t_3 u_3)
         = f(v_1 · t_1 v_2 t_1^{-1}) f_T(t_1 t_2 t_3) f(t_3^{-1} u_2 t_3 · u_3).
```

Using 2.1.4 to decompose the two extreme terms of this last expression, one obtains

```text
f(v g u) = f(v_1) f(t_1 v_2 t_1^{-1}) f_T(t_1 t_2 t_3) f(t_3^{-1} u_2 t_3) f(u_3).
```

One is then reduced to the obvious formulas

```text
f(t_1 v_2 t_1^{-1}) = f_T(t_1) f(v_2) f_T(t_1)^{-1},    f(t_3^{-1} u_2 t_3) = f_T(t_3)^{-1} f(u_2) f_T(t_3),
```

which follow from the definition of $f$ and from 2.1.3.

**Lemma 2.1.7.** *Let $\alpha \in \Delta$ and $g \in \Omega(S') \cap int(w_{\alpha})^{-1} \Omega(S')$, $S' \to S$. Then*

```text
f(w_α g w_α^{-1}) = f_N(w_α) f(g) f_N(w_α)^{-1}.
```

<!-- label: III.XXIII.2.1.7 -->

Indeed, let $g \in \Omega(S')$, $S' \to S$. Write, by Exp. XXII, 5.6.8,

```text
g = a x_{-α} t x_α b,
```

<!-- original page 275 -->

with $a \in U^{-}_{-\hat{\alpha}}(S')$, $x_{-\alpha} \in U_{-\alpha}(S')$, $t \in T(S')$, $x_{\alpha} \in
U_{\alpha}(S')$, $b \in U_{\hat{\alpha}}(S')$. By 2.1.3, 2.1.4 and the fact that $s_{\alpha}$ permutes the positive
roots $\neq \alpha$ (cf. Exp. XXI, 3.3.2), one has

```text
int(w_α) a ∈ U_{-α̂}^-(S'),    int(w_α) b ∈ U_{α̂}(S')
```

and the formula to be proved is true for $g = a$ or $g = b$. By 2.1.6, one is therefore reduced to proving the asserted
formula when $g = x_{-\alpha} t x_{\alpha} \in Z_{\alpha}(S')$. But then "everything happens in $Z_{\alpha}$", and one
concludes by condition (ii) of 2.1.

**Lemma 2.1.8.** *Let $n \in Norm_{G}(T)(S)$. For every $S' \to S$ and every $g \in \Omega(S')$ such that $int(n) g \in
\Omega(S')$, one has*

```text
f(n g n^{-1}) = f_N(n) f(g) f_N(n)^{-1}.
```

<!-- label: III.XXIII.2.1.8 -->

This is trivial if $n \in T(S)$ (by 2.1.3). The two sides of the preceding formula define morphisms of $\Omega \cap
int(n)^{-1} \Omega$ into $H$; to verify that they coincide, it suffices to verify that there exists an open $V_{n}$ of
$\Omega$ containing the unit section such that $int(n) V_{n} \subset \Omega$, and that $f \circ int(n)$ and
$int(f_{N}(n)) \circ f$ coincide on $V_{n}$. By virtue of the structure of $Norm_{G}(T)$, it suffices to prove that if
the preceding assertion is true for an $n' \in Norm_{G}(T)(S)$ and if $\alpha \in \Delta$, it is true for $n = n'
w_{\alpha}$. Set

```text
V_n = Ω ∩ int(w_α)^{-1} V_{n'}.
```

One has $int(n) V_{n} \subset int(n') V_{n'} \subset \Omega$. If $g \in V_{n}(S')$, then

```text
int(n) g = int(n') int(w_α) g.
```

Now $int(w_{\alpha}) g \in V_{n'}(S')$, hence by hypothesis

```text
f(int(n') int(w_α) g) = int(f_N(n')) f(int(w_α) g);
```

since $int(w_{\alpha}) g \in \Omega(S')$, one may apply 2.1.7, which gives

```text
f(int(w_α) g) = int(f_N(w_α)) f(g),
```

and one concludes at once.

<!-- original page 276 -->

Let us now prove 2.1.2. Let $x, x' \in \Omega(S')$; write as usual

```text
x = v t u,    x' = v' t' u',
```

whence

```text
x x' = v t (u v') t' u'.
```

By 2.1.6 and the relation $U^{-}(S') \Omega(S') U(S') = \Omega(S')$, one is reduced to proving that if $u v' \in
\Omega(S')$, then $f(u v') = f(u) f(v')$. Let $n \in Norm_{G}(T)(S')$ be as in 2.1.5 (ii). One has

```text
f(u) = f_N(n)^{-1} f(n u n^{-1}) f_N(n),    f(v') = f_N(n)^{-1} f(n v' n^{-1}) f_N(n),
```

by *loc. cit.*, whence

```text
f(u) f(v') = f_N(n)^{-1} f(n u n^{-1}) f(n v' n^{-1}) f_N(n).
```

But $n u n^{-1} \in U^{-}(S')$, $n v' n^{-1} \in U(S')$, so that

```text
f(n u n^{-1}) f(n v' n^{-1}) = f((n u n^{-1})(n v' n^{-1})) = f(n u v' n^{-1}),
```

which gives

```text
f(u) f(v') = f_N(n)^{-1} f(n u v' n^{-1}) f_N(n).
```

If $u v' \in \Omega(S')$, one may apply 2.1.8 and one is done.

**Remark 2.2.** *Instead of giving oneself $f_{N}$, one may give oneself a morphism of groups $f_{T} : T \to H$ and
sections $h_{\alpha} \in H(S) (\alpha \in \Delta)$ satisfying the conditions of 1.8.2. One must then replace condition
(ii) of the theorem by:*

*(ii') There exists a morphism of groups $F_{\alpha} : Z_{\alpha} \to H$ extending*

```text
f_α,    f_{-α},    f_T    and satisfying    F_α(w_α) = h_α.
```

<!-- label: III.XXIII.2.2 -->

<!-- original page 277 -->

We shall now give the preceding theorem a more explicit form. Keep the preceding notation.

**Theorem 2.3.** *Let $S$ be a scheme, $G$ a pinned $S$-group. Let $H$ be an $S$-sheaf in groups for (fppf),*

```text
f_T : T → H,    f_α : U_α → H,    α ∈ Δ,
```

*morphisms of groups, and*

```text
h_α ∈ H(S),    (α ∈ Δ),
```

*sections of $H$. In order that there exist a morphism of groups*

$$ f : G \to H $$

*(necessarily unique) inducing $f_{T}$ and the $f_{\alpha} (\alpha \in \Delta)$ and satisfying $f(w_{\alpha}) =
h_{\alpha}$ for every $\alpha \in \Delta$, it is necessary and sufficient that the following conditions be satisfied:*

*(i) For every $S' \to S$, every $t \in T(S')$, every $\alpha \in \Delta$ and every $x \in U_{\alpha}(S')$,*

```text
f_T(t) f_α(x) f_T(t)^{-1} = f_α(int(t) x).            (1)
```

*(ii) For every $\alpha \in \Delta$, every $S' \to S$, every $t \in T(S')$,*

```text
h_α f_T(t) h_α^{-1} = f_T(s_α(t)) = f_T(t · α^* α(t)^{-1}).            (2)
```

*(iii) For every $(\alpha, \beta) \in \Delta \times \Delta$,*

$$ (h_{\alpha} h_{\beta})^{n_{\alpha \beta}} = f_{T}(t_{\alpha \beta}). (3) $$

<!-- original page 278 -->

*(iv) For every $\alpha \in \Delta$, (recall that we write $u_{\alpha} = \exp_{\alpha}(X_{\alpha})$)*

$$ (h_{\alpha} f_{\alpha}(u_{\alpha}))^{3} = e. (4) $$

*(v) For every $(\alpha, \beta) \in \Delta \times \Delta$, $\alpha \neq \beta$, there exists a morphism of groups*

$$ f_{\alpha \beta} : U_{\alpha \beta} \to H $$

*satisfying the two following conditions:*

*a) One has*

```text
f_{αβ}|_{U_α} = f_α,    f_{αβ}|_{U_β} = f_β,            (5)
```

*b) For every $\gamma \in R^{+}_{\alpha \beta}$, $\gamma \neq \alpha$ (resp. $\gamma \neq \beta$), and every $x \in
U_{\gamma}(S')$, $S' \to S$,*

```text
int(h_α) f_{αβ}(x) = f_{αβ}(int(w_α) x),                                       (6)
(resp. int(h_β) f_{αβ}(x) = f_{αβ}(int(w_α) x)).
```

<!-- label: III.XXIII.2.3 -->

*Proof.* The uniqueness is clear by 1.9.2. Let us prove existence.

**Lemma 2.3.1.** *There exists a morphism of groups*

$$ f_{N} : Norm_{G}(T) \to H $$

*extending $f_{T}$ and satisfying $f_{N}(w_{\alpha}) = h_{\alpha}$.*

<!-- label: III.XXIII.2.3.1 -->

This is precisely what is asserted by 1.8.2, taking into account conditions (2) and (3).

<!-- original page 279 -->

**Lemma 2.3.2.** *There exists a morphism of groups*

```text
F_α : Z_α → H,    α ∈ Δ,
```

*extending $f_{T}$, $f_{\alpha}$ and satisfying $F_{\alpha}(w_{\alpha}) = h_{\alpha}$, hence extending
$f_{N}|_{Norm_{Z_{\alpha}}(T)}$.*

<!-- label: III.XXIII.2.3.2 -->

This is clear from Exp. XX, 6.2 and conditions (1), (3) and (4).

**Lemma 2.3.3.** *For every $(\alpha, \beta) \in \Delta \times \Delta$, $\alpha \neq \beta$, every $n \in
Norm_{Z_{\alpha \beta}}(T)(S)$ such that $n(\alpha) = \alpha$ (resp. $n(\alpha) = \beta$), i.e. $int(n) U_{\alpha} =
U_{\alpha}$ (resp. $int(n) U_{\alpha} = U_{\beta}$), every $S' \to S$ and every $x \in U_{\alpha}(S')$,*

```text
int(f_N(n)) f_α(x) = f_α(int(n) x)
```

*(resp.*

```text
int(f_N(n)) f_α(x) = f_β(int(n) x)).
```

<!-- label: III.XXIII.2.3.3 -->

Indeed, there exist a $t \in T(S)$ and a sequence ${\alpha_{i}} \subset {\alpha, \beta}$ such that $n = t w_{\alpha_{k}}
\cdots w_{\alpha_{1}}$. The condition is satisfied for $n = t$ by condition (1). One may therefore suppose $n =
w_{\alpha_{k}} \cdots w_{\alpha_{1}}$. We proceed by induction on $k$, i.e. we suppose the assertion proved for every
$n$ which can be written as a product of fewer than $k - 1$ simple reflections (and satisfies the hypotheses of the
lemma). Consider the roots

$$ \gamma_{i} = s_{\alpha_{i}} \cdots s_{\alpha_{1}}(\alpha). $$

If all the $\gamma_{i}$ are positive, i.e. belong to $R^{+}_{\alpha \beta}$, one may apply condition (v) of 2.3; using
the notation of 2.3 (v), one concludes at once by induction that

```text
int(f_N(w_{α_i} ⋯ w_{α_1})) f_α(x) = f_{αβ}(int(w_{α_i} ⋯ w_{α_1}) x),
```

which for $i = k$ is the desired property. If not all the $\gamma_{i}$ are positive, there exists an index $j < k$ such
that

```text
γ_j ∈ R^+,    γ_{j+1} ∉ R^+.
```

<!-- original page 280 -->

Since $\gamma_{j+1} = s_{\alpha_{j}}(\gamma_{j})$, it follows at once that $\gamma_{j} = \alpha_{j}$, by Exp. XXI,
3.3.2, hence that $\gamma_{j}$ is $\alpha$ or $\beta$, and one may decompose $n$ as

$$ n = n' \cdot n'', n' = w_{\alpha_{k}} \cdots w_{\alpha_{j+1}}, n'' = w_{\alpha_{j}} \cdots w_{\alpha_{1}}, $$

$n'$ and `n''` satisfying the hypotheses of the lemma and being a product of fewer than $k - 1$ reflections, hence
satisfying by the induction hypothesis the conclusion of the lemma.

**Lemma 2.3.4.** *Let $\alpha \in R$. If $n, n' \in Norm_{G}(T)(S)$ and $\beta, \beta' \in \Delta$ satisfy $n(\alpha) =
\beta$ and $n'(\alpha) = \beta'$, one has*

```text
int(f_T(n)^{-1}) f_β(n x n^{-1}) = int(f_T(n')^{-1}) f_{β'}(n' x n'^{-1}),
```

*for every $x \in U_{\alpha}(S')$, $S' \to S$.*

<!-- label: III.XXIII.2.3.4 -->

It suffices to verify that if $n(\alpha) = \beta$, $\alpha, \beta \in \Delta$, then $int(f_{T}(n)) \circ f_{\alpha} =
f_{\beta} \circ int(n)$. Now, by Tits's lemma (Exp. XXI, 5.6), there exists a sequence of simple roots $\alpha_{0} =
\alpha, \alpha_{1}, \cdots, \alpha_{m} = \beta$, and a sequence of elements $w_{i} \in W$, $i = 0, 1, \cdots, m - 1$,
with

```text
n = w_{m-1} ⋯ w_0,
w_i(α_i) = α_{i+1},    i = 0, 1, …, m - 1,
```

<!-- original page 281 -->

the following condition being moreover satisfied: for every $i = 0, 1, \cdots, m - 1$, there exists a simple root
$\beta_{i}$ such that

```text
w_i ∈ W_{α_i β_i},    α_{i+1} = α_i    or    β_i.
```

One is then reduced by induction to the case treated in the preceding lemma.

**Lemma 2.3.5.** *There exists a family of morphisms of groups $f'_{\gamma} : U_{\gamma} \to H$, $\gamma \in R$,
satisfying*

*(i) For $\alpha \in \Delta$, $f'_{\alpha} = f_{\alpha}$ and $f'_{-\alpha} = F_{\alpha}|_{U_{-\alpha}}$, where
$F_{\alpha}$ is defined in 2.3.2.*

*(ii) For $\alpha, \beta \in \Delta$ and $\gamma \in R^{+}_{\alpha \beta}$, $f'_{\gamma} = f_{\alpha
\beta}|_{U_{\gamma}}$.*

*(iii) For every $n \in Norm_{G}(T)(S)$ and $\alpha, \beta \in R$ such that $n(\alpha) = \beta$,*

```text
int(f_N(n)) f'_α(x) = f'_β(int(n) x)
```

*for every $x \in U_{\alpha}(S')$, $S' \to S$.*

<!-- label: III.XXIII.2.3.5 -->

For every root $\alpha \in R$, there exists an $n \in Norm_{G}(T)(S)$ such that $n(\alpha) \in \Delta$. Then define
$f'_{\alpha}(x)$ as the expression of 2.3.4. This is independent of the choice of $n$, and $f'_{\alpha}$ is indeed a
morphism of groups. Property (iii) is satisfied by construction. The first assertion of (i) is clear (take $n = e$), the
second too (take $n = w_{\alpha}$ and apply 2.3.2); if $\gamma \in R^{+}_{\alpha \beta}$ ($\alpha, \beta \in \Delta$),
there exists $n \in Norm_{Z_{\alpha \beta}}(T)(S)$ such that $n(t) = \alpha$ or $\beta$; one then applies (iii) and
conditions (5) and (6) and has proved (ii).

### 2.3.6

<!-- label: III.XXIII.2.3.6 -->

<!-- original page 282 -->

Let us now prove the theorem by showing that the conditions of 2.1 are satisfied, for the morphisms $f_{N}$ and
$f'_{\alpha}$, $\alpha \in R$.

- 2.1 (i) follows from 2.3.5 (iii),
- 2.1 (ii) follows from 2.3.5 (i) and 2.3.2,
- 2.1 (iii) follows from 2.3.5 (ii) and from the fact that $f_{\alpha \beta}$ is a morphism of groups.

An obvious corollary is:

**Corollary 2.4.** *Let $S$ be a scheme, $G$ a pinned $S$-group of semisimple rank $\geqslant 1$, $H$ an (fppf)
$S$-sheaf in groups. For each $(\alpha, \beta) \in \Delta \times \Delta$, let*

$$ F_{\alpha \beta} : Z_{\alpha \beta} \to H $$

*be a morphism of groups. In order that there exist a morphism of groups*

$$ f : G \to H $$

*inducing the $F_{\alpha \beta}$, it is necessary and sufficient that for every $(\alpha, \beta) \in \Delta \times
\Delta$,*

$$ F_{\alpha \beta}|_{Z_{\alpha}} = F_{\alpha \alpha}. $$

<!-- label: III.XXIII.2.4 -->

The condition is evidently necessary. Suppose it satisfied. Set $f_{T} = F_{\alpha \alpha}|_{T}$ (which does not depend
on $\alpha$, since $F_{\alpha \alpha}|_{T} = F_{\alpha \beta}|_{T} = F_{\beta \beta}|_{T}$). Set

```text
p_α = F_{αα}|_{U_α},    h_α = F_{αα}(w_α),    f_{αβ} = F_{αβ}|_{U_{αβ}}.
```

The conditions of 2.3 are evidently satisfied: (1), (2), (4) "are verified" in $Z_{\alpha}$, (3), (5) and (6) in
$Z_{\alpha \beta}$. There therefore exists a morphism $f : G \to H$ extending $f_{T}$, the $f_{\alpha} (\alpha \in
\Delta)$ and satisfying $f(w_{\alpha}) = h_{\alpha}$; it coincides with $F_{\alpha \beta}$ on generators of $Z_{\alpha
\beta}$, hence satisfies $f|_{Z_{\alpha \beta}} = F_{\alpha \beta}$.

One also has the following technical corollary.

<!-- original page 283 -->

**Corollary 2.5.** *Let $S$ be a scheme, $G$ and $G'$ two pinned $S$-groups of semisimple rank 2, $q$ an integer `> 0`
such that $x \mapsto x^{q}$ is an endomorphism of $G_{a, S}$, $h : R(G') \to R(G)$ a $q$-morphism of pinned root data.
Choose for each $\alpha \in R^{+}$ an $X_{\alpha} \in \Gamma(S, g_{\alpha})^{\times}$ and an $X'_{d(\alpha)} \in
\Gamma(S, g'_{d(\alpha)})^{\times}$ (extending the canonical choices for $\alpha \in \Delta$). Suppose the following
conditions are realized:*

*(i) If $\Delta = {\alpha, \beta}$, then $D_{S}(h)(t_{\alpha \beta}) = t'_{d(\alpha) d(\beta)}$.*

*(ii) For every $\alpha \in \Delta$ and every $\beta \in R^{+}$, $\beta \neq \alpha$ (whence $s_{\alpha}(\beta) \in
R^{+}$), if $z \in G_{m}(S)$ is defined by*

```text
Ad(w_α) X_β = z X_{s_α(β)},
```

*one has also*

```text
Ad(w'_{d(α)}) X'_{d(β)} = z^{q(β)} X'_{d(s_α(β))}.
```

*(iii) There exists a morphism of groups $f : U \to U'$ such that for every $\alpha \in R^{+}$,*

```text
f(exp(x X_α)) = exp(x^{q(α)} X'_{d(α)})
```

*for every $x \in G_{a}(S')$, $S' \to S$.*

*Then there exists a morphism of pinned groups $g : G \to G'$ such that $R(g) = h$.*

<!-- label: III.XXIII.2.5 -->

Indeed, one defines $f_{\alpha} : U_{\alpha} \to G'$ by

```text
f_α(exp(x X_α)) = exp(x^{q(α)} X'_{d(α)});
```

one sets $f_{T} = D_{S}(h)$, $h_{\alpha} = w'_{d(\alpha)}$. The conditions of 2.3 are satisfied (note that
$q(s_{\alpha}(\beta)) = q(\beta)$ (Exp. XXI, 6.8.4) and that one always has $D_{S}(h)(t_{\alpha}) = t'_{d(\alpha)}$),
and one concludes at once.

**Remark 2.6.** *One may make condition (v) of 2.3 more precise as follows. One must first verify:*

*(a) For every word in $w_{\alpha}$ and $w_{\beta}$ such that the corresponding word transforms $\alpha$ or $\beta$ into
$\alpha$ or $\beta$, the relation of type 2.3.3 corresponding is satisfied. In fact the proof of 2.3.3 shows that it
suffices to verify it for the words in $w_{\alpha}$ and $w_{\beta}$ that are minimal (in the sense that any nontrivial
initial sub-word does not satisfy the imposed conditions).*

<!-- original page 284 -->

*If condition (a) is satisfied, one may now define for each $\gamma \in R^{+}_{\alpha \beta}$ an $f_{\gamma} :
U_{\gamma} \to H$ as in 2.3.5; one must then write:*

*(b) The morphism defined by the $f_{\gamma}$*

```text
U_{αβ} = ∏_{γ ∈ R^+_{αβ}} U_γ → H
```

*is a morphism of groups. By Exp. XXII, 5.5.8, (b) is entailed by:*

*(b') The preceding morphism respects the commutation relations between $U_{\gamma}$ and $U_{\delta}$ for $\gamma,
\delta \in R^{+}_{\alpha \beta}$, $\gamma > \delta$ (i.e. the relations in $C_{i, j, \gamma, \delta}$ of Exp. XII,
5.5.2).*

<!-- label: III.XXIII.2.6 -->

It is clear that conversely the set of conditions (a) and (b') is equivalent to (v).

One may even reduce the preceding conditions to conditions bearing only on the elements $h_{\alpha}$, $h_{\beta}$,
$f_{\alpha}(u_{\alpha})$, $f_{\beta}(u_{\beta})$ of $H$. A condition of type (a) will be written for example, if
$s_{\alpha} s_{\beta} s_{\alpha}(\beta) = \alpha$:

```text
int(h_α h_β h_α) f_β(x) = f_α(int(w_α w_β w_α) x);            (1)
```

for every $x \in U_{\alpha}(S')$, $S' \to S$. In particular, for $x = u_{\beta}$, one has $int(w_{\alpha} w_{\beta}
w_{\alpha}) u_{\beta} = u^{z}_{\alpha}$ for a certain section $z$ of $G_{m}(S)$, and the preceding relation will give

```text
int(h_α h_β h_α) f_β(u_β) = f_α(u_α)^z.            (1')
```

<!-- original page 285 -->

Let us show that, conversely, taking into account conditions (i) to (iv) of 2.3, (1') entails (1). If $t \in T(S')$, $S'
\to S$, make $int(t)$ act on (1'); taking into account conditions (i) and (ii), one obtains (1) for $x = int(t)
u_{\beta} = u^{\beta(t)}_{\beta}$. It suffices to remark now that $\beta : T \to G_{m, S}$ is faithfully flat, hence
that condition (1) is certainly true for $x \in U_{\alpha}(S')^{\times}$, $S' \to S$. Since it is additive in $x$, and
every section of $U_{\alpha}$ can be locally written as a sum of two sections of $U^{\times}_{\alpha}$, one concludes
that (1') + (i) + (ii) ⇒ (1).

One reasons similarly with conditions of type (b). It is then necessary to use the fact that if $\gamma$ and $\gamma'$
are two distinct (hence linearly independent over $\mathbb{Q}$) positive roots, the morphism $T \to G^{2}_{m, S}$ of
components $\gamma$ and $\gamma'$ is faithfully flat. We leave the details of this transposition to the reader.

## 3. Groups of semisimple rank 2

<!-- label: III.XXIII.3 -->

### 3.1. Generalities

<!-- label: III.XXIII.3.1 -->

**Lemma 3.1.1.** *Let $S$ be a scheme, $G$ a pinned $S$-group, $\alpha$ and $\beta$ two roots of $G$, with $\alpha +
\beta \neq 0$.*

*(i) If $\alpha + \beta \notin R$, then*

```text
exp(X_α) exp(X_β) = exp(X_β) exp(X_α)
```

*for all $X_{\alpha} \in W(g_{\alpha})(S')$, $X_{\beta} \in W(g_{\beta})(S')$, $S' \to S$.*

*(ii) If $\alpha + \beta$ and $\alpha - \beta$ are not roots, then*

```text
w_α(z_α) exp(X_β) w_α(z_α)^{-1} = exp(X_β)
```

<!-- original page 286 -->

*for all $X_{\beta} \in W(g_{\beta})(S')$, $z_{\alpha} \in W(g_{\alpha})^{\times}(S')$, $S' \to S$, and*

```text
w_α(z_α) w_β(z_β) = w_β(z_β) w_α(z_α)
```

*for all $z_{\alpha} \in W(g_{\alpha})^{\times}(S')$ and $z_{\beta} \in W(g_{\beta})^{\times}(S')$, $S' \to S$.*

*(iii) Let $X_{\alpha} \in W(g_{\alpha})^{\times}(S')$, $X_{\beta} \in W(g_{\beta})^{\times}(S')$, and $w \in
Norm_{G}(T)(S')$ such that $w(\alpha) = \beta$; define $z \in G_{m}(S')$ by*

```text
Ad(w) X_α = z X_β.
```

*Then*

```text
int(w) exp(x X_α) = exp(x z X_β),
int(w) exp(y X_α^{-1}) = exp(y z^{-1} X_β^{-1}),
int(w) w_α(X_α) = β^*(z) w_β(X_β).
```

*In particular, if $z = \pm 1$, then*

$$ int(w) w_{\alpha}(X_{\alpha}) = w_{\beta}(X_{\beta})^{z}. $$

*(iv) If one sets $t_{\alpha} = \alpha^{*}(-1)$, $t_{\beta} = \beta^{*}(-1)$, then*

```text
s_α(t_β) = t_β t_α^{(β^*, α)},    β(t_α) = (-1)^{(α^*, β)}.
```

<!-- label: III.XXIII.3.1.1 -->

*Proof.* (i) follows at once from Exp. XXII, 5.5.2; (ii) from Exp. XX, 3.1 and from (i) applied to $(\beta, \alpha)$,
$(\beta, -\alpha)$, $(-\beta, \alpha)$, $(-\beta, -\alpha)$; (iii) is evident from the definitions. For the last
assertion of (iii), note that $\beta^{*}(-1) = w_{\beta}(X_{\beta})^{-2}$. Finally, (iv) is trivial.

**Proposition 3.1.2 (Groups of type $A_{1} \times A_{1}$).** *Let $S$ be a scheme, $G$ a pinned $S$-group of type $A_{1}
\times A_{1}$, and denote $\Delta = R^{+} = {\alpha, \beta}$.*

*(i) One has*

<!-- original page 287 -->

```text
t_{αβ} = (w_α w_β)^2 = t_α t_β = (w_β w_α)^2 = t_{βα}.
```

*(ii) One has*

```text
Ad(w_α) X_β = X_β,    Ad(w_β) X_α = X_α.
```

*(iii) $U_{\alpha}$ and $U_{\beta}$ commute (i.e. $U$ is commutative).*

<!-- label: III.XXIII.3.1.2 -->

Indeed, by assertion (ii) of the lemma, $w_{\alpha} w_{\beta} = w_{\beta} w_{\alpha}$, whence $(w_{\alpha}
w_{\beta})^{2} = w^{2}_{\alpha} w^{2}_{\beta} = t_{\alpha} t_{\beta}$, which is (i). By assertion (ii) of the lemma, one
has also (ii); finally, (iii) is assertion (i) of the lemma.

### 3.1.3

<!-- label: III.XXIII.3.1.3 -->

Let us make condition (v) of 2.3 explicit here. Using the method exposed in 2.6, one obtains the two following groups of
conditions, setting $v_{\alpha} = f_{\alpha}(u_{\alpha})$ for $\alpha \in \Delta$:

```text
(A)   h_α v_β h_α^{-1} = v_β,           (B)   v_α v_β = v_β v_α.
      h_β v_α h_β^{-1} = v_α
```

### 3.2. Groups of type `A_2`

<!-- label: III.XXIII.3.2 -->

**Proposition 3.2.1.** *Let $S$ be a scheme, $G$ a pinned $S$-group of type `A_2`, and denote $\Delta = {\alpha,
\beta}$, $R^{+} = {\alpha, \beta, \alpha + \beta}$.*

<!-- original page 288 -->

*(i) One has*

```text
t_{αβ} = (w_α w_β)^3 = e = (w_β w_α)^3 = t_{βα}.
```

*(ii) Set $Ad(w_{\beta}) X_{\alpha} = X_{\alpha + \beta}$. Then*

```text
Ad(w_α) X_β = -X_{α + β},    Ad(w_α) X_{α + β} = X_β,    Ad(w_β) X_{α + β} = -X_α.
```

*(iii) Set $p_{\alpha + \beta}(x) = \exp(x X_{\alpha + \beta}) = int(w_{\beta}) p_{\alpha}(x)$. Then*

```text
p_β(y) p_α(x) = p_α(x) p_β(y) p_{α + β}(x y).
```

<!-- label: III.XXIII.3.2.1 -->

### 3.2.2

<!-- label: III.XXIII.3.2.2 -->

The proof occupies Nos. 3.2.2 to 3.2.7. First, $(\beta^{*}, \alpha) = (\alpha^{*}, \beta) = -1$, whence
$\alpha(t_{\beta}) = \beta(t_{\alpha}) = -1$.

Set $Ad(w_{\beta}) X_{\alpha} = X_{\alpha + \beta}$; one has at once

```text
Ad(w_β) X_{α + β} = α(t_β) X_α = -X_α.
```

Set

```text
Ad(w_α) X_β = z X_{α + β},    z ∈ G_m(S),
```

whence

```text
Ad(w_α) X_{α + β} = β(t_α) z^{-1} X_β = -z^{-1} X_β.
```

We know (Exp. XXII, 5.5.2) that there exists a unique section $A \in G_{a}(S)$ such that

```text
p_β(y) p_α(x) = p_α(x) p_β(y) p_{α + β}(A x y).            (+)
```

To prove (ii) and (iii), it therefore remains to show that $A = -z = 1$.

<!-- original page 289 -->

### 3.2.3

<!-- label: III.XXIII.3.2.3 -->

Make $int(w_{\beta})$ act on the preceding formula (+); one obtains:

```text
p_{-β}(-y) p_{α + β}(x) = p_{α + β}(x) p_{-β}(-y) p_α(-A x y).            (++)
```

### 3.2.4

<!-- label: III.XXIII.3.2.4 -->

By definition of $p_{\alpha + \beta}$,

```text
w_β p_α(x) w_β^{-1} = p_{α + β}(x),
```

which is written

```text
p_β(1) p_{-β}(-1) p_β(1) p_α(x) p_β(-1) p_{-β}(1) p_β(-1) = p_{α + β}(x).
```

Since $p_{\beta}$ and $p_{\alpha + \beta}$ commute, $\alpha + 2\beta$ not being a root, this is also written

```text
p_β(1) p_α(x) p_β(-1) = p_{-β}(1) p_{α + β}(x) p_{-β}(-1).
```

Using now (+) in the left member and (++) in the right, one obtains:

```text
p_α(x) p_β(1) p_{α + β}(A x) p_β(-1) = p_{α + β}(x) p_{-β}(1) p_α(A x) p_{-β}(-1).
```

Since $\alpha + 2\beta$ (resp. $\alpha - \beta$) is not a root, the left (resp. right) member is written

```text
p_α(x) p_{α + β}(A x)    resp. p_{α + β}(x) p_α(A x)
```

and the right-hand term equals $p_{\alpha}(A x) p_{\alpha + \beta}(x)$, since $2\alpha + \beta$ is not a root. Therefore

```text
p_α(x) p_{α + β}(A x) = p_α(A x) p_{α + β}(x),
```

which gives (by XXII 4.1.3) $A = 1$.

### 3.2.5

<!-- label: III.XXIII.3.2.5 -->

Now make $int(w_{\alpha})$ act on formula (+); using the fact that $A = 1$, one finds

```text
p_{α + β}(z y) p_{-α}(-x) = p_{-α}(-x) p_{α + β}(z y) p_β(-z^{-1} x y).            (+++)
```

### 3.2.6

<!-- label: III.XXIII.3.2.6 -->

<!-- original page 290 -->

Write now, as a moment ago,

```text
w_α p_β(y) w_α^{-1} = p_{α + β}(z y),
```

whence, since $p_{\alpha}$ and $p_{\alpha + \beta}$ commute,

```text
p_α(1) p_β(y) p_α(-1) = p_{-α}(1) p_{α + β}(z y) p_{-α}(-1).
```

Using now (+) and (+++), this is also written

```text
p_β(y) p_{α + β}(-y) = p_{α + β}(z y) p_β(-z^{-1} y),
```

and since $p_{\beta}$ and $p_{\alpha + \beta}$ commute, this gives $z = -1$.

### 3.2.7

<!-- label: III.XXIII.3.2.7 -->

We have therefore proved (ii) and (iii). Let us prove (i). One has

```text
w_α w_β w_α = w_α w_β w_α^{-1} w_α^2 = w_{α + β}^{-1} t_α,
```

whence

```text
w_β w_α w_β w_α w_β = w_β w_{α + β}^{-1} t_α w_β = w_β w_{α + β}^{-1} w_β^{-1} · s_β(t_α) · t_β
                    = w_α · t_α t_β · t_β = w_α t_α = w_α^{-1},
```

which gives

```text
(w_α w_β)^3 = (w_β w_α)^3 = e,
```

which completes the proof.

**Remark 3.2.8.** *Condition (v) of 2.3 translates here as (setting $v_{\alpha} = f_{\alpha}(u_{\alpha})$):*

```text
(A)   int(h_α h_β h_α) v_β = vβ → h_α v_β h_α^{-1} = h_β v_α h_β^{-1}      (B)
      int(h_β h_α h_β) v_α = vα                                                  v_β v_α = v_α v_β · h_β v_α h_β^{-1},
                                                                                 v_β · h_β v_α h_β^{-1} = h_β v_α h_β^{-1} · v_β,
                                                                                 v_α · h_β v_α h_β^{-1} = h_β v_α h_β^{-1} · v_α.
```

<!-- label: III.XXIII.3.2.8 -->

<!-- original page 291 -->

Setting $v_{\alpha + \beta} = int(h_{\beta}) v_{\alpha}$, the three last conditions are also written

```text
(B)   v_β v_α = v_α v_β v_{α + β},
      v_α v_{α + β} = v_{α + β} v_α,
      v_β v_{α + β} = v_{α + β} v_β.
```

### 3.3. Groups of type `B_2`

<!-- label: III.XXIII.3.3 -->

**Proposition 3.3.1.** *Let $S$ be a scheme, $G$ a pinned $S$-group of type `B_2`, and denote $\Delta = {\alpha,
\beta}$, $R^{+} = {\alpha, \beta, \alpha + \beta, 2\alpha + \beta}$.*

*(i) One has*

```text
t_{αβ} = (w_α w_β)^4 = t_α = (w_β w_α)^4 = t_{βα}.
```

<!-- original page 194 source / 294 reedition — heading transition -->

*(ii) If one sets*

```text
Ad(w_β) X_α = X_{α + β},    Ad(w_α) X_β = X_{2α + β},
```

*one has:*

```text
Ad(w_α) X_{α + β} = -X_{α + β},
Ad(w_α) X_{2α + β} = X_β,
Ad(w_β) X_{α + β} = -X_α,
Ad(w_β) X_{2α + β} = X_{2α + β}.
```

*(iii) Set*

```text
p_{α + β}(x) = exp(x X_{α + β}) = int(w_β) p_α(x),
p_{2α + β}(x) = exp(x X_{2α + β}) = int(w_α) p_β(x).
```

*Then:*

```text
p_β(y) p_α(x) = p_α(x) p_β(y) p_{α + β}(x y) p_{2α + β}(x^2 y),
p_{α + β}(y) p_α(x) = p_α(x) p_{α + β}(y) p_{2α + β}(2 x y).
```

<!-- label: III.XXIII.3.3.1 -->

### 3.3.2

<!-- label: III.XXIII.3.3.2 -->

The proof occupies Nos. 3.3.2 to 3.3.6. One has $(\beta^{*}, \alpha) = -1$, $(\alpha^{*}, \beta) = -2$, whence
$\alpha(t_{\beta}) = -1$, $\beta(t_{\alpha}) = 1$.

<!-- original page 292 -->

Note in passing that $\beta(t_{\alpha}) = \alpha(t_{\alpha}) = 1$, which shows that $t_{\alpha}$ is a section of
$Centr(G)$. Set

```text
Ad(w_β) X_α = X_{α + β},    Ad(w_α) X_β = X_{2α + β}.
```

One has at once

```text
Ad(w_β) X_{α + β} = α(t_β) X_α = -X_α,
Ad(w_α) X_{2α + β} = β(t_α) X_β = X_β.
```

Since $(2\alpha + \beta) + \beta$ and $(2\alpha + \beta) - \beta$ are not roots,

```text
Ad(w_β) X_{2α + β} = X_{2α + β}.
```

There exists a scalar $k \in G_{m}(S)$ such that

```text
Ad(w_α) X_{α + β} = k X_{α + β}.
```

On the other hand, by Exp. XXII, 5.5.2, there exist sections $A, B, C \in G_{a}(S)$ such that

```text
p_β(y) p_α(x) = p_α(x) p_β(y) p_{α + β}(A x y) p_{2α + β}(B x^2 y),       (1)
p_{α + β}(y) p_α(x) = p_α(x) p_{α + β}(y) p_{2α + β}(C x y).               (2)
```

It is therefore necessary, in (ii) and (iii), to prove that $A = B = 1$, $C = 2$, $k = -1$.

### 3.3.3

<!-- label: III.XXIII.3.3.3 -->

Make $int(w_{\alpha})$ act on formula (2). One finds

```text
p_{2α + β}(y) p_{-α}(-x) = p_{-α}(-x) p_{2α + β}(y) p_{α + β}(A k x y) p_β(B x^2 y).       (3)
```

Transforming (2) likewise, one obtains

```text
p_{α + β}(k y) p_{-α}(-x) = p_{-α}(-x) p_{α + β}(k y) p_β(C x y).       (4)
```

<!-- original page 293 -->

Transforming (1) by $int(w_{\beta})$,

```text
p_{-β}(-y) p_{α + β}(x) = p_{α + β}(x) p_{-β}(-y) p_α(-A x y) p_{2α + β}(B x^2 y).       (5)
```

### 3.3.4

<!-- label: III.XXIII.3.3.4 -->

Write

```text
w_β p_α(x) w_β^{-1} = p_{α + β}(x).
```

Since $\alpha + 2\beta$ is not a root, this gives

```text
p_β(1) p_α(x) p_β(-1) = p_{-β}(1) p_{α + β}(x) p_{-β}(-1).
```

Using (1) in the left member and (5) in the right, one obtains

```text
p_α(x) p_β(1) p_{α + β}(A x) p_{2α + β}(B x^2) p_β(-1) =
    p_{α + β}(x) p_{-β}(1) p_α(A x) p_{2α + β}(-B x^2) p_{-β}(-1).
```

Since $p_{\beta}$ commutes with $p_{\alpha + \beta}$ and $p_{2\alpha + \beta}$ on the one hand, and $p_{-\beta}$
commutes with $p_{\alpha}$ and $p_{2\alpha + \beta}$ on the other hand, this is written

```text
p_α(x) p_{α + β}(A x) p_{2α + β}(B x^2) = p_{α + β}(x) p_α(A x) p_{2α + β}(-B x^2).
```

Transforming the right member by (2), one obtains

```text
p_α(x) p_{α + β}(A x) p_{2α + β}(B x^2) = p_α(A x) p_{α + β}(x) p_{2α + β}((A C - B) x^2),
```

which gives

```text
A = 1,    C = 2 B.
```

### 3.3.5

<!-- label: III.XXIII.3.3.5 -->

Write now

```text
w_α p_β(y) w_α^{-1} = p_{2α + β}(y).
```

Since $3\alpha + \beta$ is not a root, this gives

```text
p_α(1) p_β(y) p_α(-1) = p_{-α}(1) p_{2α + β}(y) p_{-α}(-1).
```

<!-- original page 294 -->

Using (1) in the left member, (3) in the right, one obtains

```text
p_β(y) p_{α + β}(-A y) p_{2α + β}(B y) = p_{2α + β}(y) p_{α + β}(A k y) p_β(B y).
```

Since $p_{\alpha + \beta}$, $p_{2\alpha + \beta}$ and $p_{\beta}$ commute, this gives at once

```text
B = 1,    -A = A k,
```

whence finally

```text
A = 1,    B = 1,    C = 2,    k = -1.
```

### 3.3.6

<!-- label: III.XXIII.3.3.6 -->

We have therefore proved (ii) and (iii). Let us prove (i). Taking into account the equality $s_{\beta}(t_{\alpha}) =
t_{\alpha} t^{(\alpha^{*}, \beta)}_{\beta} = t_{\alpha}$ (since $(\alpha^{*}, \beta) = 2$),[^XXIII-3-1] one has
successively:

```text
w_α w_β w_α = w_α w_β w_α^{-1} t_α = w_{2α + β} t_α,
w_β w_α w_β w_α w_β = w_β w_{2α + β} w_β^{-1} · s_β(t_α) · t_β = w_{2α + β} t_α t_β,
w_α w_β w_α w_β w_α w_β w_α = w_α w_{2α + β} w_α^{-1} · s_α(t_α t_β) · t_α = w_β · t_α · t_β t_α · t_α
                            = w_β^{-1} t_α,
```

whence

$$ (w_{\beta} w_{\alpha})^{4} = t_{\alpha}, $$

and

```text
(w_α w_β)^4 = s_β(t_α) = t_α,
```

which completes the proof.

**Remark 3.3.7.** *Condition (v) of 2.3 translates here as follows, setting $v_{\alpha + \beta} = int(h_{\beta})
v_{\alpha}$ and $v_{2\alpha + \beta} = int(h_{\alpha}) v_{\beta}$:*

<!-- original page 295 -->

```text
(A)   int(h_α h_β h_α) v_β = v_β,        (B)   v_β v_α = v_α v_β v_{α + β} v_{2α + β},
      int(h_β h_α h_β) v_α = v_α,              v_{α + β} v_α = v_α v_{α + β} v_{2α + β}^2,
                                               v_{α + β} v_β = v_β v_{α + β},
                                               v_{2α + β} v_α = v_α v_{2α + β},
                                               v_{2α + β} v_β = v_β v_{2α + β},
                                               v_{2α + β} v_{α + β} = v_{α + β} v_{2α + β}.
```

<!-- label: III.XXIII.3.3.7 -->

### 3.4. Groups of type `G_2`

<!-- label: III.XXIII.3.4 -->

**Proposition 3.4.1.** *Let $S$ be a scheme, $G$ a pinned $S$-group of type `G_2`, and denote $\Delta = {\alpha,
\beta}$, $R^{+} = {\alpha, \beta, \alpha + \beta, 2\alpha + \beta, 3\alpha + \beta, 3\alpha + 2\beta}$.*

*(i) One has*

```text
t_{αβ} = (w_α w_β)^6 = e = (w_β w_α)^6 = t_{βα}.
```

*(ii) If one sets*

```text
Ad(w_β) X_α = X_{α + β},    Ad(w_α) X_{α + β} = X_{2α + β},
Ad(w_α) X_β = -X_{3α + β},    Ad(w_β) X_{3α + β} = X_{3α + 2β},
```

*one has:*

```text
Ad(w_α) X_{2α + β} = -X_{α + β},    Ad(w_α) X_{3α + β} = X_β,
Ad(w_α) X_{3α + 2β} = X_{3α + 2β},    Ad(w_β) X_{α + β} = -X_α,
Ad(w_β) X_{2α + β} = X_{2α + β},    Ad(w_β) X_{3α + 2β} = -X_{3α + β}.
```

*(iii) If one sets*

```text
p_{α + β}(x) = exp(x X_{α + β}) = int(w_β) p_α(x),
p_{2α + β}(x) = exp(x X_{2α + β}) = int(w_α w_β) p_α(x),
p_{3α + β}(x) = exp(x X_{3α + β}) = int(w_α) p_β(-x),
p_{3α + 2β}(x) = exp(x X_{3α + 2β}) = int(w_β w_α) p_β(-x),
```

<!-- original page 296 -->

*one has:*

```text
p_β(y) p_α(x) = p_α(x) p_β(y) p_{α + β}(x y) p_{2α + β}(x^2 y) p_{3α + β}(x^3 y) p_{3α + 2β}(x^3 y^2),
p_{α + β}(y) p_α(x) = p_α(x) p_{α + β}(y) p_{2α + β}(2 x y) p_{3α + β}(3 x^2 y) p_{3α + 2β}(3 x y^2),
p_{2α + β}(y) p_α(x) = p_α(x) p_{2α + β}(y) p_{3α + β}(3 x y),
p_{3α + β}(y) p_β(x) = p_β(x) p_{3α + β}(y) p_{3α + 2β}(-x y),
p_{2α + β}(y) p_{α + β}(x) = p_{α + β}(x) p_{2α + β}(y) p_{3α + 2β}(3 x y).
```

<!-- label: III.XXIII.3.4.1 -->

### 3.4.2

<!-- label: III.XXIII.3.4.2 -->

The proof occupies Nos. 3.4.2 to 3.4.9. One has $(\beta^{*}, \alpha) = -1$, $(\alpha^{*}, \beta) = -3$, whence
$\beta(t_{\alpha}) = \alpha(t_{\beta}) = -1$. Define $X_{\alpha + \beta}$, $X_{2\alpha + \beta}$, $X_{3\alpha + \beta}$
and $X_{3\alpha + 2\beta}$ as in (ii). One has at once

```text
Ad(w_β) X_{α + β} = α(t_β) X_α = -X_α,
Ad(w_α) X_{2α + β} = α(t_α) β(t_α) X_{α + β} = -X_{α + β},
Ad(w_α) X_{3α + β} = -β(t_α) X_β = X_β,
Ad(w_β) X_{3α + 2β} = α(t_β)^3 β(t_β) X_{3α + β} = -X_{3α + β}.
```

Finally, since $(3\alpha + 2\beta) \pm \alpha$ and $(2\alpha + \beta) \pm \beta$ are not roots,

```text
Ad(w_α) X_{3α + 2β} = X_{3α + 2β},    Ad(w_β) X_{2α + β} = X_{2α + β},
```

which completes the proof of (ii).

### 3.4.3

<!-- label: III.XXIII.3.4.3 -->

<!-- original page 297 -->

By virtue of Exp. XXII, 5.5.2, there exist scalars[^N.D.E-XXIII-7]

```text
A, B, C, D, E, F, G, H, J ∈ G_a(S),
```

such that

```text
p_β(y) p_α(x) = p_α(x) p_β(y) p_{α + β}(A x y) p_{2α + β}(B x^2 y) p_{3α + β}(C x^3 y) p_{3α + 2β}(D x^3 y^2),   (1)
p_{α + β}(y) p_α(x) = p_α(x) p_{α + β}(y) p_{2α + β}(E x y) p_{3α + β}(F x^2 y) p_{3α + 2β}(G x y^2),           (2)
p_{2α + β}(y) p_α(x) = p_α(x) p_{2α + β}(y) p_{3α + β}(H x y),                                                  (3)
p_{3α + β}(y) p_β(x) = p_β(x) p_{3α + β}(y) p_{3α + 2β}(J x y).                                                 (4)
```

### 3.4.4

<!-- label: III.XXIII.3.4.4 -->

Make $int(w_{\beta})$ act on (1), (3) and (4):

```text
p_{-β}(-y) p_{α + β}(x) =
    p_{α + β}(x) p_{-β}(-y) p_α(-A x y) p_{2α + β}(B x^2 y) p_{3α + 2β}(C x^3 y) p_{3α + β}(-D x^3 y^2),       (5)
p_{2α + β}(y) p_{α + β}(x) = p_{α + β}(x) p_{2α + β}(y) p_{3α + 2β}(H x y),                                    (6)
p_{3α + 2β}(y) p_{-β}(-x) = p_{-β}(-x) p_{3α + 2β}(y) p_{3α + β}(-J x y).                                       (7)
```

Making $int(w_{\alpha})$ act on (1), one finds

```text
p_{3α + β}(-y) p_{-α}(-x) =
    p_{-α}(-x) p_{3α + β}(-y) p_{2α + β}(A x y) p_{α + β}(-B x^2 y) p_β(C x^3 y) p_{3α + β}(D x^3 y^2).        (8)
```

### 3.4.5

<!-- label: III.XXIII.3.4.5 -->

Write

```text
w_β p_α(x) w_β^{-1} = p_{α + β}(x),
```

that is, $\alpha + 2\beta$ not being a root,

<!-- original page 298 -->

```text
p_β(1) p_α(x) p_α(-1) = p_{-β}(1) p_{α + β}(x) p_{-β}(-1).            (9)
```

Transforming the left member of (9) by (1), then (4), one obtains:

```text
p_β(1) p_α(x) p_β(-1)
   = p_α(x) p_β(1) p_{α + β}(A x) p_{2α + β}(B x^2) p_{3α + β}(C x^3) p_{3α + 2β}(D x^3) p_β(-1)
   = p_α(x) p_β(1) p_{α + β}(A x) p_{2α + β}(B x^2) p_β(-1) p_{3α + β}(C x^3) p_{3α + 2β}((D - C J) x^3)
   = p_α(x) p_{α + β}(A x) p_{2α + β}(B x^2) p_{3α + β}(C x^3) p_{3α + 2β}((D - C J) x^3).            (10)
```

Transforming the right member of (9) by (5), then (7):

```text
p_{-β}(1) p_{α + β}(x) p_{-β}(-1)
   = p_{α + β}(x) p_{-β}(1) p_α(A x) p_{2α + β}(-B x^2) p_{3α + 2β}(-C x^3) p_{3α + β}(-D x^3) p_{-β}(-1)
   = p_{α + β}(x) p_α(A x) p_{2α + β}(-B x^2) p_{3α + 2β}(-C x^3) p_{3α + β}((C J - D) x^3).            (11)
```

Using now (2), this right member becomes

```text
p_α(A x) p_{α + β}(x) p_{2α + β}(A E x^2) p_{3α + β}(A^2 F x^3) p_{3α + 2β}(A G x^3) ×
    p_{2α + β}(-B x^2) p_{3α + 2β}(-C x^3) p_{3α + β}((C J - D) x^3)
= p_α(A x) p_{α + β}(x) p_{2α + β}((A E - B) x^2) p_{3α + β}((A^2 F + C J - D) x^3) p_{3α + 2β}((A G - C) x^3). (12)
```

So (9) rewrites:

```text
p_α(x) p_{α + β}(A x) p_{2α + β}(B x^2) p_{3α + β}(C x^3) p_{3α + 2β}((D - C J) x^3) =
   p_α(A x) p_{α + β}(x) p_{2α + β}((A E - B) x^2) p_{3α + β}((A^2 F + C J - D) x^3) p_{3α + 2β}((A G - C) x^3),
```

which gives

```text
A = 1,    E = 2 B,    C + D = F + C J,    F = G.
```

### 3.4.6

<!-- label: III.XXIII.3.4.6 -->

Write now

```text
w_α p_β(y) w_α^{-1} = p_{3α + β}(-y),
```

<!-- original page 299 -->

that is, $4\alpha + \beta$ not being a root,

```text
p_α(1) p_β(y) p_α(-1) = p_{-α}(1) p_{3α + β}(-y) p_{-α}(-1).            (13)
```

Transform the left member by (1):

```text
p_α(1) p_β(y) p_α(-1) = p_β(y) p_{α + β}(-A y) p_{2α + β}(B y) p_{3α + β}(-C y) p_{3α + 2β}(-D y^2).
```

Transform the right member of (13) successively by (8), (6) and (4):

```text
p_{-α}(1) p_{3α + β}(-y) p_{-α}(-1)
   = p_{3α + β}(-y) p_{2α + β}(A y) p_{α + β}(-B y) p_β(C y) p_{3α + 2β}(D y^2)
   = p_{3α + β}(-y) p_{α + β}(-B y) p_{2α + β}(A y) p_{3α + 2β}(-A B H y^2) p_β(C y) p_{3α + 2β}(D y^2)
   = p_β(C y) p_{3α + β}(-y) p_{α + β}(-B y) p_{2α + β}(A y) p_{3α + 2β}((D - C J - A B H) y^2)
   = p_β(C y) p_{α + β}(-B y) p_{2α + β}(A y) p_{3α + β}(-y) p_{3α + 2β}((D - C J - A B H) y^2).
```

So (13) rewrites:

```text
p_β(C y) p_{α + β}(-B y) p_{2α + β}(A y) p_{3α + β}(-y) p_{3α + 2β}((D - C J - A B H) y^2) =
   p_β(y) p_{α + β}(-A y) p_{2α + β}(B y) p_{3α + β}(-C y) p_{3α + 2β}(-D y^2),
```

whence

```text
C = 1,    A = B,    D - C J - A B H = -D.
```

Taking into account the results already obtained:

```text
A = B = C = 1,    E = 2,    F = G,    D + 1 = F + J,    2 D = H + J.
```

### 3.4.7

<!-- label: III.XXIII.3.4.7 -->

Write

```text
w_β p_{3α + β}(x) w_β^{-1} = p_{3α + 2β}(x),
```

that is,

```text
p_β(1) p_{3α + β}(x) p_β(-1) = p_{-β}(1) p_{3α + 2β}(x) p_{-β}(-1).
```

Transforming the left member by (4), the right by (7), one obtains:

<!-- original page 300 -->

```text
p_{3α + β}(x) p_{3α + 2β}(-J x) = p_{3α + 2β}(x) p_{3α + β}(-J x),
```

so $J = -1$.

### 3.4.8

<!-- label: III.XXIII.3.4.8 -->

Write finally

```text
w_α p_{α + β}(y) w_α^{-1} = p_{2α + β}(y),
```

that is,

```text
p_α(1) p_{α + β}(y) p_α(-1) = p_{-α}(1) p_α(-1) p_{2α + β}(y) p_α(1) p_{-α}(-1).
```

Transforming the left member by (2), the right by (3), one obtains:

```text
p_{α + β}(y) p_{2α + β}(-E y) p_{3α + β}(F y) p_{3α + 2β}(-G y^2) =
    p_{-α}(1) p_{2α + β}(y) p_{3α + β}(H y) p_{-α}(-1).
```

It is immediate to see that, if one makes $p_{-\alpha}(-1)$ commute with $p_{3\alpha + \beta}(H y)$, then $p_{2\alpha +
\beta}(y)$, one does not introduce in the right member any new terms in $p_{3\alpha + \beta}$. The latter therefore
writes, denoting by empty parentheses quantities whose exact value does not matter to us:

```text
p_{α + β}( ) p_{2α + β}( ) p_β( ) p_{3α + β}(H y) p_{3α + 2β}( ).
```

Comparing with the left member, one has at once $F = H$, whence by the previous results $2 D = D + 1$, so $D = 1$, and
finally $F = G = H = 2 D - J = 3$, which completes the determination of the coefficients $A, \cdots, J$ and the proof of
(iii).

### 3.4.9

<!-- label: III.XXIII.3.4.9 -->

Let us prove (i) finally, in the usual manner. One has successively:

```text
w_α w_β w_α = w_α w_β w_α^{-1} t_α = w_{3α + β}^{-1} · t_α,
w_β (w_α w_β)^2 = w_β w_{3α + β}^{-1} w_β^{-1} · s_β(t_α) · t_β = w_{3α + 2β}^{-1} · t_α t_β · t_β = w_{3α + 2β}^{-1} · t_α,
w_α (w_β w_α)^3 = w_α w_{3α + 2β}^{-1} w_α^{-1} = w_{3α + 2β}^{-1},
w_β (w_α w_β)^4 = w_β w_{3α + 2β}^{-1} w_β^{-1} · t_β = w_{3α + β} · t_β,
w_α (w_β w_α)^5 = w_α w_{3α + β} w_α^{-1} · s_α(t_β) · t_β = w_β · t_β t_α · t_α = w_β^{-1}.
```

<!-- original page 301 -->

Whence

```text
(w_α w_β)^6 = (w_β w_α)^6 = e.
```

**Remark 3.4.10.** *Condition (v) of 2.4 is composed of*

```text
(A)   int(h_α h_β h_α h_β h_α) v_β = v_β,
      int(h_β h_α h_β h_α h_β) v_α = v_α,
```

*and, setting*

```text
v_{α + β} = int(h_β) v_α,    v_{2α + β} = int(h_α h_β) v_α,
v_{3α + β} = int(h_α) v_β^{-1},    v_{3α + 2β} = int(h_β h_α) v_β^{-1},
```

<!-- original page 302 -->

*the commutation relations:*

```text
(B)   v_β v_α = v_α v_β v_{α + β} v_{2α + β} v_{3α + β} v_{3α + 2β},
      v_{α + β} v_α = v_α v_{α + β} v_{2α + β}^2 v_{3α + β}^3 v_{3α + 2β}^3,
      v_{2α + β} v_α = v_α v_{2α + β} v_{3α + β}^3,
      v_{3α + β} v_α = v_α v_{3α + β},
      v_{3α + 2β} v_α = v_α v_{3α + 2β},
      v_{α + β} v_β = v_β v_{α + β},
      v_{2α + β} v_β = v_β v_{2α + β},
      v_{3α + β} v_β = v_β v_{3α + β} v_{3α + 2β}^{-1},
      v_{3α + 2β} v_β = v_β v_{3α + 2β},
      v_{2α + β} v_{α + β} = v_{α + β} v_{2α + β} v_{3α + 2β}^3,
      v_{3α + β} v_{α + β} = v_{α + β} v_{3α + β},
      v_{3α + 2β} v_{α + β} = v_{α + β} v_{3α + 2β},
      v_{3α + β} v_{2α + β} = v_{2α + β} v_{3α + β},
      v_{3α + 2β} v_{2α + β} = v_{2α + β} v_{3α + 2β},
      v_{3α + 2β} v_{3α + β} = v_{3α + β} v_{3α + 2β}.
```

<!-- label: III.XXIII.3.4.10 -->

### 3.5. Explicit form of the generators-and-relations theorem

<!-- label: III.XXIII.3.5 -->

**Theorem 3.5.1.** *Let $S$ be a scheme, $G$ a pinned $S$-group, $T$ its maximal torus, $\Delta$ its system of simple
roots, $u_{\alpha} \in U_{\alpha}(S)^{\times}$ and $w_{\alpha} \in Norm_{G}(T)(S)$ the elements defined by the pinning
($\alpha \in \Delta$). Let*

```text
f_T : T → H,    f_α : U_α → H,    α ∈ Δ
```

<!-- original page 303 -->

*be morphisms of groups, $H$ being an $S$-sheaf in groups for (fppf); let $h_{\alpha} \in H(S)$, ($\alpha \in \Delta$)
be sections of $H$, and set $v_{\alpha} = f_{\alpha}(u_{\alpha})$, $\alpha \in \Delta$. In order that there exist a
morphism of groups*

$$ f : G \to H $$

*extending $f_{T}$, $f_{\alpha} (\alpha \in \Delta)$ and satisfying $f(w_{\alpha}) = h_{\alpha}$ ($\alpha \in \Delta$)
(and then necessarily unique), it is necessary and sufficient that the following conditions be satisfied:*

*(i) For every $S' \to S$, every $\alpha \in \Delta$, every $t \in T(S')$ and every $x \in U_{\alpha}(S')$,*

```text
int(f_T(t)) f_α(x) = f_α(int(t) x) = f_α(x^{α(t)}).            (1)
```

*(ii) For every $\alpha \in \Delta$, every $S' \to S$ and every $t \in T(S')$,*

```text
int(h_α) f_T(t) = f_T(s_α(t)) = f_T(t · α^* α(t)^{-1}).            (2)
```

*(iii) For every $\alpha \in \Delta$,[^N.D.E-XXIII-8]*

$$ h^{2}_{\alpha} = f_{T}(\alpha^{*}(-1)), (3_{1}) (h_{\alpha} v_{\alpha})^{3} = e. (4) $$

*(iv) For all $\alpha, \beta \in \Delta$, $\alpha \neq \beta$, such that $(\alpha^{*}, \beta) = 0$ (resp. $(\alpha^{*},
\beta) = -1$, resp. $(\alpha^{*}, \beta) = -2$, resp. $(\alpha^{*}, \beta) = -3$):*

<!-- original page 304 -->

*(a) the relation*

```text
(h_α h_β)^2 = f_T(α^*(-1) β^*(-1))     if (α^*, β) = 0;
(h_α h_β)^3 = e,                       if (α^*, β) = -1;        (3₂)
(h_α h_β)^4 = f_T(α^*(-1)),            if (α^*, β) = -2;
(h_α h_β)^6 = e,                       if (α^*, β) = -3.
```

*(b) The relations (A) and (B) of 3.1.3 (resp. 3.2.8, resp. 3.3.7, resp. 3.4.10).*

<!-- label: III.XXIII.3.5.1 -->

This follows at once from 2.3, 2.6 and the calculations done in each particular case.

**Remark 3.5.2.** *One may present the preceding results in a slightly different way: one gives oneself morphisms, for
$\alpha \in \Delta$,*

```text
a_α : T · U_α → H,    b_α : Norm_{Z_α}(T) → H,
```

*and one sets*

```text
h_α = b_α(w_α),    v_α = a_α(u_α);
```

*then the conditions to be verified are the following:*

*(1) all the $a_{\alpha} (\alpha \in \Delta)$ and all the $b_{\alpha} (\alpha \in \Delta)$ have the same restriction to
$T$;*

*(2) conditions (4) and (iv) of 3.5.1 above are satisfied.*

<!-- label: III.XXIII.3.5.2 -->

### 3.5.3

<!-- label: III.XXIII.3.5.3 -->

<!-- original page 305 -->

Various applications of this theorem will be given in the following Exposé. Let us mention one here: Theorem 3.5.1 gives
a description by generators and relations of $G$ in the category of $S$-sheaves for (fppf); in other words, consider for
each $S' \to S$ the group $H(S')$ generated by $T(S')$, $U_{\alpha}(S')$, $\alpha \in R$, and $w_{\alpha}$, $\alpha \in
R$, subjected to relations analogous to (1), (2), (3₁), (4), (3₂), (A), (B); then $G$ is none other than the sheaf
associated with the presheaf $S' \mapsto H(S')$.

In particular, if $S'$ is the spectrum of an algebraically closed field $k$, one has $G(S') = H(S')$ (an immediate
consequence of the Nullstellensatz in the form: "a sieve over an algebraically closed field, covering for (fppf), is
trivial"), so that 3.5.1 yields at once an explicit description by generators and relations of the "abstract" group
$G(k)$.[^N.D.E-XXIII-9]

## 4. Uniqueness of pinned groups: fundamental theorem

<!-- label: III.XXIII.4 -->

**Theorem 4.1.** *Let $S$ be a nonempty scheme. The functor $R$ of 1.6 is fully faithful: let $G$ and $G'$ be two pinned
$S$-groups, $p$[^N.D.E-XXIII-10] an integer `> 0` such that $x \mapsto x^{p}$ is an endomorphism of $G_{a, S}$, and $h :
R(G') \to R(G)$ a $p$-morphism of pinned root data. There exists a unique morphism of pinned groups*

$$ f : G \to G' $$

*such that $R(f) = h$.*

<!-- label: III.XXIII.4.1 -->

The uniqueness is proved in 1.9. It suffices to prove existence. By hypothesis, one has a bijection $d : R
\xrightarrow{\sim} R'$ and a map $q : R \to {p^{n} | n \in \mathbb{N}}$ such that

```text
h(d(α)) = q(α) α    and    ^t h(α^*) = q(α) d(α)^*
```

<!-- original page 306 -->

for every $\alpha \in R$. In particular, the semisimple ranks of $G$ and $G'$ coincide.

### 4.1.1

<!-- label: III.XXIII.4.1.1 -->

Suppose $rg_{ss}(G) = rg_{ss}(G') = 0$. Then $G$ and $G'$ are tori: one has $G = T = D_{S}(M)$, $G' = T' = D_{S}(M')$
and $h$ is simply a morphism of ordinary groups $h : M' \to M$. One then takes $f = D_{S}(h)$.

### 4.1.2

<!-- label: III.XXIII.4.1.2 -->

Suppose $rg_{ss}(G) = rg_{ss}(G') = 1$. Consider then

```text
f_T = D_S(h) : T → T'.
```

By hypothesis, one has a commutative diagram, where $\alpha' = d(\alpha)$:

```text
G_{m, S} ──α^*──→ T ──α──→ G_{m, S}
   │              │            │
 q(α)            f_T          q(α)
   │              │            │
   ↓              ↓            ↓
G_{m, S} ──α'^*──→ T' ──α'──→ G_{m, S}.
```

One then applies Exp. XX, 4.1.

### 4.1.3

<!-- label: III.XXIII.4.1.3 -->

Suppose $rg_{ss}(G) = rg_{ss}(G') = 2$. Then, by Exp. XXI, 7.5.3, one knows all the possibilities for $h : R(G') \to
R(G)$. Let us examine them successively, verifying each time the conditions of 2.5.

Denote $\Delta = {\alpha, \beta}$, $\Delta' = {\alpha', \beta'}$ in such a way that $d(\alpha) = \alpha'$, $d(\beta) =
\beta'$.

### 4.1.4. $G$ and $G'$ of type $A_{1} \times A_{1}$

<!-- label: III.XXIII.4.1.4 -->

One has

```text
h(α') = q α,    h(β') = q_1 β.
```

Let us show that the conditions of 2.5 are satisfied: (ii) and (iii) follow from 3.1.2 (ii) and (iii); let us prove (i).

<!-- original page 307 -->

One has[^N.D.E-XXIII-11]

```text
D_S(h) t_{αβ} = D_S(h)(t_α t_β) = ^t h(α^*)(-1) · ^t h(β^*)(-1) = α'^*((-1)^q) · β'^*((-1)^{q_1}).
```

Now, the hypothesis that $x \mapsto x^{p}$ is an endomorphism of $G_{a, S}$ (and $S \neq \emptyset$) entails that $p =
1$ or that $S$ is of characteristic $p$; in all cases $(-1)^{q} = -1$ (if $q$ is even, $p = 2$ and `1 = -1`).
Consequently,

```text
D_S(h) t_{αβ} = α'^*(-1) · β'^*(-1) = t'_{α' β'}.
```

This shows that condition 2.5 (i) is satisfied.

### 4.1.5. $G$ and $G'$ of type `A_2`

<!-- label: III.XXIII.4.1.5 -->

One has

```text
h(α') = q α,    h(β') = q β.
```

Set $X_{\alpha + \beta} = Ad(w_{\beta}) X_{\alpha}$ and $X'_{\alpha' + \beta'} = Ad(w_{\beta'}) X_{\alpha'}$. Let us
verify the conditions of 2.5. For (i), one reasons as above, using 3.2.1 (i); for (ii), it is immediate by 3.2.1 (ii);
it remains to verify (iii). We must check that

```text
p_α(x) p_β(y) p_{α + β}(z) ↦ p'_{α'}(x^q) p'_{β'}(y^q) p'_{α' + β'}(z^q)
```

is a morphism of groups. The only nontrivial commutation relation is that of 3.2.1 (iii), which is written

```text
p_β(y) p_α(x) = p_α(x) p_β(y) p_{α + β}(x y),
p'_{β'}(y^q) p'_{α'}(x^q) = p'_{α'}(x^q) p'_{β'}(y^q) p'_{α' + β'}(x^q y^q).
```

### 4.1.6

<!-- label: III.XXIII.4.1.6 -->

One reasons similarly for $G$ and $G'$ of type `B_2` (resp. `G_2`), when the radicial exponents are equal, using 3.3.1
(resp. 3.4.1); it remains, therefore, to treat — in order to complete the case of groups of rank 2 — the two exceptional
cases of Exp. XXI, 7.5.3.

### 4.1.7. $G$ and $G'$ of type `B_2`, $S$ of characteristic 2, $q(\alpha) = 2q$, $q(\beta) = q$

<!-- label: III.XXIII.4.1.7 -->

<!-- original page 308 -->

The positive roots are ${\alpha, \beta, \alpha + \beta, 2\alpha + \beta}$ and ${\alpha', \beta', \alpha' + \beta',
\alpha' + 2\beta'}$ (note that the "short" simple roots are $\alpha$ and $\beta'$). One has

```text
h(α') = 2 q α,    h(β') = q β,    h(α' + β') = q(2α + β),    h(α' + 2β') = 2 q(α + β),
```

which gives

```text
d(α + β) = α' + 2β',    q(α + β) = 2 q,
d(2α + β) = α' + β',    q(2α + β) = q.
```

Set

```text
X_{α + β} = Ad(w_β) X_α,    X_{2α + β} = Ad(w_α) X_β,
X'_{α' + β'} = Ad(w'_{α'}) X'_{β'},    X'_{α' + 2β'} = Ad(w'_{β'}) X'_{α'}.
```

Let us now verify the conditions of 2.5.

(i) Since $S$ is of characteristic 2, one has `-1 = 1` on $S$, hence $t_{\alpha \beta} = t_{\alpha} = \alpha^{*}(-1) = e
= \beta'^{*}(-1) = t'_{\beta'} = t'_{\alpha' \beta'}$ (cf. 3.3.1 (i)).

(ii) One has by construction

```text
Ad(w_α) X_β = X_{2α + β},    Ad(w'_{α'}) X'_{β'} = X'_{α' + β'} = X'_{d(2α + β)};
Ad(w_β) X_α = X_{α + β},    Ad(w'_{β'}) X'_{α'} = X'_{α' + 2β'} = X'_{d(α + β)}.
```

By 3.3.1 (ii) and the fact that `-1 = 1` on $S$, one has on each side

```text
Ad(w_α) X_{α + β} = X_{α + β},    Ad(w'_{α'}) X'_{d(α + β)} = Ad(w'_{α'}) X'_{α' + 2β'} = X'_{α' + 2β'} = X'_{d(α + β)};
Ad(w_α) X_{2α + β} = X_β,    Ad(w'_{α'}) X'_{d(2α + β)} = Ad(w'_{α'}) X'_{α' + β'} = X'_{β'} = X'_{d(β)};
Ad(w_β) X_{α + β} = X_α,    Ad(w'_{β'}) X'_{d(α + β)} = Ad(w'_{β'}) X'_{α' + 2β'} = X'_{α'} = X'_{d(α)};
Ad(w_β) X_{2α + β} = X_{2α + β},    Ad(w'_{β'}) X'_{d(2α + β)} = Ad(w'_{β'}) X'_{α' + β'} = X'_{α' + β'} = X'_{d(2α + β)}.
```

<!-- original page 309 -->

(iii) By 3.3.1 (iii), one sees that the only nontrivial commutation relation in $U$ (resp. $U'$) is

```text
p_β(y) p_α(x) = p_α(x) p_β(y) p_{α + β}(x y) p_{2α + β}(x^2 y),
```

resp.

```text
p'_{α'}(y') p'_{β'}(x') = p'_{β'}(x') p'_{α'}(y') p'_{α' + β'}(x' y') p'_{α' + 2β'}(x' y'^2).
```

We must verify that the morphism

```text
p_α(x) p_β(y) p_{α + β}(z) p_{2α + β}(t) ↦ p'_{α'}(x^{2q}) p'_{β'}(y^q) p'_{α' + 2β'}(z^{2q}) p'_{α' + β'}(t^q)
```

is a morphism of groups; one sees at once that this amounts to seeing that

```text
p'_{β'}(y^q) p'_{α'}(x^{2q}) = p'_{α'}(x^{2q}) p'_{β'}(y^q) p'_{α' + 2β'}((x y)^{2q}) p'_{α' + β'}((x^2 y)^q),
```

which is none other than the second relation above (setting $y' = x^{2q}$, $x' = y^{q}$).

### 4.1.8. $G$ and $G'$ of type `G_2`, $S$ of characteristic 3, $q(\alpha) = 3q$, $q(\beta) = q$

<!-- label: III.XXIII.4.1.8 -->

<!-- original page 310 -->

The positive roots are ${\alpha, \beta, \alpha + \beta, 2\alpha + \beta, 3\alpha + \beta, 3\alpha + 2\beta}$ on the one
hand, ${\alpha', \beta', \alpha' + \beta', \alpha' + 2\beta', \alpha' + 3\beta', 2\alpha' + 3\beta'}$ on the other (as
in the preceding case, the short simple roots are $\alpha$ and $\beta'$). One has

```text
h(α') = 3 q α,    h(β') = q β,    h(α' + β') = q(3α + β),
h(α' + 2β') = q(3α + 2β),    h(α' + 3β') = 3 q(α + β),
h(2α' + 3β') = 3 q(2α + β),
```

which gives

```text
d(α + β) = α' + 3β',    q(α + β) = 3 q,
d(2α + β) = 2α' + 3β',    q(2α + β) = 3 q,
d(3α + β) = α' + β',    q(3α + β) = q,
d(3α + 2β) = α' + 2β',    q(3α + 2β) = q.
```

Set

```text
X_{α + β} = Ad(w_β) X_α,    X_{2α + β} = Ad(w_α) X_{α + β},
X_{3α + β} = -Ad(w_α) X_β,    X_{3α + 2β} = Ad(w_β) X_{3α + β};
X'_{α' + β'} = -Ad(w'_{α'}) X'_{β'},    X'_{α' + 2β'} = Ad(w'_{β'}) X'_{α' + β'},
X'_{α' + 3β'} = Ad(w'_{β'}) X'_{α'},    X'_{2α' + 3β'} = Ad(w'_{α'}) X'_{α' + 3β'}.
```

Let us now verify the conditions of 2.5.

(i) $t_{\alpha \beta} = e$ and $t'_{\alpha' \beta'} = e$ by 3.4.1 (i).

(ii) One has by construction

```text
Ad(w_β) X_α = X_{α + β},    Ad(w'_{β'}) X'_{α'} = X'_{α' + 3β'} = X'_{d(α + β)};
Ad(w_α) X_β = -X_{3α + β},    Ad(w'_{α'}) X'_{β'} = -X'_{α' + β'} = -X'_{d(3α + β)};
Ad(w_β) X_{3α + β} = X_{3α + 2β},    Ad(w'_{β'}) X'_{d(3α + β)} = Ad(w'_{β'}) X'_{α' + β'} = X'_{α' + 2β'} = X'_{d(3α + 2β)};
Ad(w_α) X_{α + β} = X_{2α + β},    Ad(w'_{α'}) X'_{d(α + β)} = Ad(w'_{α'}) X'_{α' + 3β'} = X'_{2α' + 3β'} = X'_{d(2α + β)}.
```

<!-- original page 311 -->

By 3.4.1 (ii), one has on each side:

```text
Ad(w_α) X_{2α + β} = -X_{α + β},    Ad(w'_{α'}) X'_{d(2α + β)} = Ad(w'_{α'}) X'_{2α' + 3β'} = -X'_{α' + 3β'} = -X'_{d(α + β)};
       …                                          …
Ad(w_β) X_{3α + 2β} = -X_{3α + β},    Ad(w'_{β'}) X'_{d(3α + 2β)} = Ad(w'_{β'}) X'_{α' + 2β'} = -X'_{α' + β'} = -X'_{d(3α + β)}.
```

(The dots replace four verifications of the same kind.)

(iii) The only nontrivial commutation relations in $U$ and $U'$ are, by 3.4.1 (iii) (and taking into account `3 = 0` on
$S$):

```text
p_β(y) p_α(x) = p_α(x) p_β(y) p_{α + β}(x y) p_{2α + β}(x^2 y) p_{3α + β}(x^3 y) p_{3α + 2β}(x^3 y^2),
p_{α + β}(y) p_α(x) = p_α(x) p_{α + β}(y) p_{2α + β}(-x y),
p_{3α + β}(y) p_β(x) = p_β(x) p_{3α + β}(y) p_{3α + 2β}(-x y);

p'_{α'}(y') p'_{β'}(x') =
    p'_{β'}(x') p'_{α'}(y') p'_{α' + β'}(-x' y') p'_{α' + 2β'}(-x'^2 y') p'_{α' + 3β'}(-x'^3 y') p'_{2α' + 3β'}(-x'^3 y'^2),
p'_{α' + β'}(y') p'_{β'}(x') = p'_{β'}(x') p'_{α' + β'}(y') p'_{α' + 2β'}(x' y'),
p'_{α' + 3β'}(y') p'_{α'}(x') = p'_{α'}(x') p'_{α' + 3β'}(y') p'_{2α' + 3β'}(x' y').
```

<!-- original page 312 -->

We must verify that the morphism $\phi : U \to U'$ defined by

```text
φ(p_α(x) p_β(y) p_{α + β}(t) p_{2α + β}(u) p_{3α + β}(v) p_{3α + 2β}(w))
  = p'_{α'}(x^{3q}) p'_{β'}(y^q) p'_{α' + 3β'}(t^{3q}) p'_{2α' + 3β'}(u^{3q}) p'_{α' + β'}(v^q) p'_{α' + 2β'}(w^q)
```

is a morphism of groups. Now one verifies immediately that the three last commutation relations are also written

```text
p'_{β'}(y^q) p'_{α'}(x^{3q}) =
    p'_{α'}(x^{3q}) p'_{β'}(y^q) p'_{α' + 3β'}((x y)^{3q}) p'_{2α' + 3β'}((x^2 y)^{3q}) p'_{α' + β'}((x^3 y)^q) p'_{α' + 2β'}((x^3 y^2)^q),
p'_{α' + 3β'}(y^{3q}) p'_{α'}(x^{3q}) = p'_{α'}(x^{3q}) p'_{α' + 3β'}(y^{3q}) p'_{2α' + 3β'}(-(x y)^{3q}),
p'_{α' + β'}(y^q) p'_{β'}(x^q) = p'_{β'}(x^q) p'_{α' + β'}(y^q) p'_{α' + 2β'}(-(x y)^q);
```

which shows that $\phi$ is indeed a morphism of groups and completes the proof of 4.1.7.

### 4.1.9. Case where $G$ and $G'$ are of semisimple rank `> 2`

<!-- label: III.XXIII.4.1.9 -->

For each root $\alpha \in \Delta$, denote $\alpha' = d(\alpha) \in \Delta' = d(\Delta)$. For each $(\alpha, \beta) \in
\Delta \times \Delta$, consider the pinned groups of semisimple rank $\leqslant 2$, $Z_{\alpha \beta}$ and $Z'_{\alpha'
\beta'}$. The morphism of groups $M' \to M$ underlying $h$ defines a $p$-morphism of root data

```text
h_{αβ} : R(Z_{αβ}) → R(Z'_{α' β'}).
```

By virtue of the preceding results, there exists therefore a morphism of pinned groups

```text
f_{αβ} : Z_{αβ} → Z'_{α' β'}
```

<!-- original page 313 -->

such that $R(f_{\alpha \beta}) = h_{\alpha \beta}$. Let us prove that the $f_{\alpha \beta}$ satisfy the gluing
condition of 2.5; indeed $f_{\alpha \beta}|_{Z_{\alpha}}$ and $f_{\alpha \alpha}$ are two morphisms of pinned groups

$$ Z_{\alpha} \to Z'_{\alpha'} $$

corresponding to the same morphism of pinned root data, and therefore coincide by the uniqueness result already proved.
By 2.5 there exists therefore a morphism of groups

$$ f : G \to G' $$

extending the $f_{\alpha \beta}$. This is evidently a morphism of pinned groups such that $R(f) = h$, which completes
the proof of Theorem 4.1.

## 5. Corollaries of the fundamental theorem

<!-- label: III.XXIII.5 -->

The most important is:

**Corollary 5.1.** *Let $S$ be a nonempty scheme, $G$ and $G'$ two pinned $S$-groups, $h$ an isomorphism of pinned root
data*

$$ h : R(G') \xrightarrow{\sim} R(G). $$

*There exists a unique isomorphism of pinned $S$-groups*

$$ f : G \xrightarrow{\sim} G' $$

*such that $R(f) = h$.*

<!-- label: III.XXIII.5.1 -->

Note that 5.1 also follows from 3.5.1 (the relations of 3.5.1 may be written using only the datum of $R(G)$); note also
that 5.1 follows from the most elementary part of the proof of 4.1 (one does not need to consider the "exceptional
isogenies" of 4.1.7 and 4.1.8).

<!-- original page 314 -->

**Corollary 5.2 ("Uniqueness theorem").** *Let $S$ be a scheme, $G$ and $G'$ two splittable $S$-groups (Exp. XXII,
1.13). If $G$ and $G'$ are of the same type (Exp. XXII, 2.6), they are isomorphic.*

<!-- label: III.XXIII.5.2 -->

**Corollary 5.3.** *Let $S$ be a scheme, $G$ and $G'$ two splittable $S$-groups. The following conditions are
equivalent:*

*(i) $G$ and $G'$ are isomorphic.*

*(ii) $G$ and $G'$ are isomorphic locally for the (fpqc) topology.*

*(iii) There exists an $s \in S$ such that the $s$-groups $G_{s}$ and $G'_{s}$ are of the same type.*

<!-- label: III.XXIII.5.3 -->

Indeed, one evidently has (i) ⇒ (ii) ⇒ (iii). On the other hand, (iii) entails that $R(G) = R(G_{s}) = R(G'_{s}) =
R(G')$, hence that $G$ and $G'$ satisfy the condition of 5.2.

**Corollary 5.4 ("Uniqueness of the Chevalley schemes").** *Let $G$ and $G'$ be two reductive groups over $\mathbb{Z}$
possessing split maximal tori.*[^XXIII-5-1] *The following conditions are equivalent:*

*(i) $G$ and $G'$ are isomorphic.*

*(ii) There exists $s \in \operatorname{Spec}(\mathbb{Z})$ such that $G_{s}$ and $G'_{s}$ are of the same type.*

*(iii) $G_{\mathbb{C}}$ and $G'_{\mathbb{C}}$ are of the same type.*

<!-- label: III.XXIII.5.4 -->

Indeed, $G$ and $G'$ are splittable by Exp. XXII, 2.2.

**Corollary 5.5 ("Existence of outer automorphisms").** *Let $S$ be a scheme, $G$ a pinned $S$-group, $h$ an
automorphism of the pinned root datum $R(G)$. There exists a unique automorphism $u$ of $G$ respecting its pinning and
such that $R(u) = h$.*

<!-- label: III.XXIII.5.5 -->

Let us make the preceding corollary explicit.

**Corollary 5.5.bis.** *Let $S$ be a scheme, $G$ a split reductive $S$-group, $R^{+}$ a system of positive roots of
$G$.*

<!-- original page 315 -->

*Choose for each simple root $\alpha$ an isomorphism of vector groups $p_{\alpha} : G_{a, S} \xrightarrow{\sim}
U_{\alpha}$. Let $h$ be an automorphism of $M$ permuting the positive roots and the corresponding coroots: if $\alpha
\in R^{+}$, $h(\alpha) \in R^{+}$ and $h^{\vee}(\alpha^{*}) = h(\alpha)^{*}$. There exists a unique automorphism $u$ of
$G$ inducing $D_{S}(h)$ on $T$ and such that $u \circ p_{\alpha} = p_{h(\alpha)}$ for every simple root $\alpha$.*

<!-- label: III.XXIII.5.5.bis -->

**Corollary 5.6.** *Let $G$ and $G'$ be two reductive $S$-groups. The following conditions are equivalent:*

*(i) $G$ and $G'$ are isomorphic locally for the (fpqc) topology.*

*(i bis) $G$ and $G'$ are isomorphic locally for the étale topology.*

*(ii) For every $s \in S$, $G_{s}$ and $G'_{s}$ are isomorphic.*

*(iii) The functions $s \mapsto$ type of $G_{s}$ and $s \mapsto$ type of $G'_{s}$ are equal.*

<!-- label: III.XXIII.5.6 -->

<!-- original page 208 source -->

Indeed (i bis) ⇒ (i) trivially, (i) ⇒ (ii) by the principle of finite extension ([EGA IV₃, 9.1.4](https://jcreinhold.github.io/ega/iv/22-ch4-09-constructible-properties.html#91-the-principle-of-finite-extension)), (ii) ⇒ (iii)
trivially; it remains to prove (iii) ⇒ (i bis). Now one may suppose $G$ and $G'$ splittable (Exp. XXII, 2.3), in which
case the assertion follows from 5.3.

**Corollary 5.7.** *Let $S$ be a scheme, $G$ a reductive $S$-group, $G'$ an $S$-group that is affine, smooth, and with
connected fibers. Let $s \in S$ be such that $G_{s}$ and $G'_{s}$ are isomorphic; there exists then an étale $S' \to S$
covering $s$ such that $G_{S'}$ and $G'_{S'}$ are isomorphic.*

<!-- label: III.XXIII.5.7 -->

Indeed, by Exp. XIX 2.5 and Exp. XXII 2.1, one may suppose $G$ and $G'$ reductive splittable and one is reduced to 5.3.

In the case where $S$ is the spectrum of a field, one deduces from 5.6 and 5.7:

<!-- original page 316 -->

**Corollary 5.8.** *Let $k$ be a field and $G$ and $G'$ two reductive $k$-groups. The following conditions are
equivalent:*[^N.D.E-XXIII-12]

*(i) $G$ and $G'$ are of the same type.*

*(ii) $G \otimes_{k} \bar{k}$ and $G' \otimes_{k} \bar{k}$ are isomorphic.*

*(iii) There exists a finite separable extension $K$ of $k$ such that $G \otimes_{k} K$ and $G' \otimes_{k} K$ are
isomorphic.*

<!-- label: III.XXIII.5.8 -->

**Corollary 5.9.** *Let $S$ be a nonempty scheme and $R$ a root datum. The following conditions are
equivalent:*[^N.D.E-XXIII-13]

*(i) There exists a pinned $S$-group of type $R$.*

*(ii) There exists an $S$-group of type $R$.*

*(iii) There exists locally for (fpqc) a reductive $S$-group of type $R$.*

<!-- label: III.XXIII.5.9 -->

It is evidently a matter of proving (iii) ⇒ (i). To simplify the proof, suppose that there exist a faithfully flat
quasi-compact morphism $S' \to S$ and a reductive $S'$-group $G'$ of type $R$. One may suppose $G'$ splittable; fix a
pinning $E'$ of $G'$; denote $R = R(G', E')$. The two pullbacks of `(G', E')` to $S'' = S' \times_{S} S'$ are pinned
groups $(G''_{1}, E''_{1})$, $(G''_{2}, E''_{2})$; one has canonical isomorphisms $p_{i} : R(G''_{i}, E''_{i})
\xrightarrow{\sim} R$, whence an isomorphism

```text
p = p_2^{-1} ∘ p_1 : R(G''_1, E''_1) → R(G''_2, E''_2).
```

By the uniqueness theorem, there exists a unique isomorphism

```text
f : (G''_1, E''_1) ⥲ (G''_2, E''_2)
```

such that $R(f) = p$. One has therefore on $G'$ a gluing datum; this is a descent datum.

<!-- original page 317 -->

Indeed, one must verify a compatibility condition between the pullbacks of $f$ on `S'''`, but it suffices to make this
verification on the transforms of these arrows by the functor $R$, since the latter is fully faithful. Now $p$ is indeed
a descent datum, by construction, which shows that $f$ is one too. Since $G'$ is affine, this descent datum is
effective; since the pinning of $G'$ is stable under the descent datum, one verifies easily that there exists a pinned
$S$-group $(G, E)$ which gives `(G', E')` by base extension and which is therefore of type $R$.

*N.B.* Naturally, in the language of fibered categories, the preceding proof simplifies (and becomes intelligible).

**Corollary 5.10.** *Let $S$ be a nonempty scheme. Let $R$ be a pinned root datum such that there exists a reductive
$S$-group of type $R$. Then there exists a pinned $S$-group of type $R$, unique up to a unique isomorphism.*

<!-- label: III.XXIII.5.10 -->

**Definition 5.11.** *Under the preceding conditions, we shall denote by $\acute{E}p_{S}(R)$ the unique pinned $S$-group
of type $R$, by $T_{S}(R)$ its canonical maximal torus, by $B_{S}(R)$ its canonical Borel subgroup, etc.*

<!-- label: III.XXIII.5.11 -->

If one has a morphism $S' \to S$ ($S'$ nonempty), one may identify $\acute{E}p_{S'}(R)$ with $\acute{E}p_{S}(R)
\times_{S} S'$, etc. In particular, if $\acute{E}p_{\operatorname{Spec}(\mathbb{Z})}(R)$ exists (we shall see that this
is always the case), one denotes it $\acute{E}p(R)$, and one has

```text
Ép_S(R) = Ép(R) ×_{Spec(ℤ)} S.
```

One says that $\acute{E}p(R)$ is the *Chevalley group scheme of type $R$*.

### 5.12

<!-- label: III.XXIII.5.12 -->

It therefore comes to the same thing to say that the $S$-sheaf in groups $G$ is a reductive $S$-group of type $R$, or to
say that it is locally isomorphic (for the étale or (fpqc) topology) to $\acute{E}p_{S}(R)$. Likewise, by virtue of the
conjugation theorems, it comes to the same thing to say that $(G, T)$ is a reductive $S$-group of type $R$ equipped with
a maximal torus, or to say that it is locally isomorphic to $(\acute{E}p_{S}(R), T_{S}(R))$; likewise with Borel
subgroups or Killing couples.

## 6. Chevalley systems

<!-- label: III.XXIII.6 -->

<!-- original page 318 -->

The explicit calculations of No. 3 have important numerical consequences. We first lay down the following definition.

**Definition 6.1.** *Let $S$ be a scheme, $(G, T, M, R)$ a split $S$-group. One calls* Chevalley system of $G$ *a family
$(X_{\alpha})_{\alpha \in R}$ of elements*

$$ X_{\alpha} \in \Gamma(S, g_{\alpha})^{\times} $$

<!-- original page 210 source -->

*satisfying the following condition:*

*(SC) for every pair $\alpha, \beta \in R$,*

$$ Ad(w_{\alpha}(X_{\alpha})) X_{\beta} = \pm X_{s_{\alpha}(\beta)}. $$

<!-- label: III.XXIII.6.1 -->

Recall (Exp. XX, 3.1) that

```text
w_α(X_α) = exp(X_α) exp(-X_α^{-1}) exp(X_α).
```

Note that (SC) entails in particular $X_{-\alpha} = \pm X_{\alpha}$ for $\alpha \in R$, by virtue of the relation (Exp.
XX, 3.7) $Ad(w_{\alpha}(X_{\alpha})) X_{\alpha} = -X^{-1}_{\alpha}$.

**Proposition 6.2.** *Every split group admits a Chevalley system. More precisely, let $(\Delta, (X'_{\alpha})_{\alpha
\in \Delta})$ be a pinning (1.1) of the split group $(G, T, M, R)$; there exists then a Chevalley system
$(X_{\alpha})_{\alpha \in R}$ of $G$ such that $X_{\alpha} = X'_{\alpha}$ for $\alpha \in \Delta$.*

<!-- label: III.XXIII.6.2 -->

Let us first show that it suffices to verify condition (SC) for $\alpha \in \Delta$; for every $\alpha \in R$, there
exists a sequence ${\alpha_{i}} \subset \Delta$ such that $\alpha = s_{\alpha_{1}} \cdots s_{\alpha_{n}}(\alpha_{n+1})$,
whence, applying condition (SC) for each of the $\alpha_{i}$,

```text
X_α = ± Ad(w_{α_1}(X_{α_1}) ⋯ w_{α_n}(X_{α_n})) X_{α_{n+1}}.
```

<!-- original page 319 -->

By 3.1.1 (iii),

```text
w_{α_1}(X_{α_1}) ⋯ w_{α_n}(X_{α_n}) w_{α_{n+1}}(X_{α_{n+1}}) w_{α_n}(X_{α_n})^{-1} ⋯ w_{α_1}(X_{α_1})^{-1}
    = α^*(±1) w_α(X_α).
```

Now, it suffices to note that $w_{\alpha_{i}}(X_{\alpha_{i}})^{-1} = \alpha^{*}_{i}(-1) w_{\alpha_{i}}(X_{\alpha_{i}})$
and that for every pair of roots $(\beta, \gamma)$, $\beta(\gamma^{*}(-1)) = (-1)^{(\gamma^{*}, \beta)} = \pm 1$, which
entails that if (SC) is satisfied for the pairs $(\alpha_{i}, \gamma)$ ($\gamma \in R$), it is so for every pair
$(\alpha, \beta)$, ($\beta \in R$).

Let us now construct a system $(X_{\alpha})_{\alpha \in R}$ in the following manner. For every $\alpha \in R$, choose a
sequence ${\alpha_{i}} \subset \Delta$ as above, and define $X_{\alpha}$ by

```text
X_α = Ad(w_{α_i}(X_{α_1}) ⋯ w_{α_n}(X_{α_n})) X'_{α_{n+1}}.
```

To verify (SC), it suffices to prove:

**Lemma 6.3.** *Let $(G, T, M, R, \Delta, (X_{\alpha})_{\alpha \in \Delta})$ be a pinned $S$-group; let $\alpha_{i} (0
\leqslant i \leqslant n + 1)$ be a sequence of simple roots such that*

$$ int(s_{\alpha_{1}} \cdots s_{\alpha_{n}})(\alpha_{n+1}) = \alpha_{0}. $$

*Then*

```text
Ad(w_{α_1} ⋯ w_{α_n}) X_{α_{n+1}} = ± X_{α_0}.
```

<!-- label: III.XXIII.6.3 -->

Reasoning as in 2.3.4 with the help of Tits's lemma (Exp. XXI 5.6), one is reduced to verifying lemma 6.3 in the two
following cases:

a) $G$ is of semisimple rank at most 2, or b) $w_{\alpha_{1}} \cdots w_{\alpha_{n}}$ is a section of $T$.

In case a), note that 6.3 is a consequence of 6.2 and that 6.2 has been verified in part (i) of 3.1.2 (resp. 3.2.1,
resp. 3.3.1, resp. 3.4.1).

<!-- original page 320 -->

It therefore remains to prove 6.3 in case b), or, what amounts to the same thing, that if ${\alpha_{i}}$ is a sequence
of simple roots such that $s_{\alpha_{1}} \cdots s_{\alpha_{n}} = id$, then $t = w_{\alpha_{1}} \cdots w_{\alpha_{n}}$
satisfies $\alpha(t) = \pm 1$ for every root $\alpha \in R$. By virtue of the structure of the Weyl group (Exp. XXI,
5.1), the word $s_{\alpha_{1}} \cdots s_{\alpha_{n}}$ in the free group generated by the $s_{\alpha}$, $\alpha \in
\Delta$, is in the invariant subgroup generated by the $(s_{\alpha} s_{\beta})^{n_{\alpha \beta}}$, $(\alpha, \beta) \in
\Delta \times \Delta$. One is therefore reduced to the case where $s_{\alpha_{1}} \cdots s_{\alpha_{n}}$ is of the form

```text
s_{α_1} ⋯ s_{α_i} (s_{α_{i+1}} s_{α_{i+2}})^{n_{α_{i+1} α_{i+2}}} s_{α_i} ⋯ s_{α_1}.
```

Then

```text
t = s_{α_1} ⋯ s_{α_i}(t_{α_{i+1} α_{i+2}}),
```

and one is reduced to verifying that for every pair of simple roots $(\alpha_{1}, \alpha_{2})$ and every root $\beta \in
R$, $\beta(t_{\alpha_{1} \alpha_{2}}) = \pm 1$, which is trivial, in view of the values of $t_{\alpha_{1} \alpha_{2}}$
calculated in No. 3 (part (i) of 3.1.2, 3.2.1, 3.3.1, 3.4.1).

**Proposition 6.4.** *Let $(G, T, M, R)$ be a split $S$-group, $(X_{\alpha})_{\alpha \in R}$ a Chevalley system of $G$.
Let $\alpha$ and $\beta$ be two non-proportional roots; suppose*

```text
long(α) ⩽ long(β),    i.e.    |(β^*, α)| ⩽ |(α^*, β)|.
```

*Let $q$ and $p - 1$ be the integers $\geqslant 0$ such that the set of roots of the form $\beta + k \alpha$, $k \in
\mathbb{Z}$, is*

```text
{β - (p - 1) α, …, β, …, β + q α}.
```

*(cf. Exp. XXI, 2.3.5; by loc. cit., one has therefore $-(\alpha^{*}, \beta) = q - p + 1$). Then the commutation
relation between $U_{\alpha}$ and $U_{\beta}$ is given by the following table (which exhausts the possible cases, since
the length of the preceding root chain is $p + q - 1 \leqslant 3$),*

<!-- original page 321 -->

*where, for each $\gamma \in R$, one writes $p_{\gamma}(x) = \exp(x X_{\gamma})$:*

```text
(p, q)    p_β(y) p_α(x) p_β(-y) p_α(-x)
(-, 0)     = e
(1, 1)     = p_{α + β}(± x y)
(1, 2)     = p_{α + β}(± x y) p_{2α + β}(± x^2 y)
(1, 3)     = p_{α + β}(± x y) p_{2α + β}(± x^2 y) p_{3α + β}(± x^3 y) p_{3α + 2β}(± x^3 y^2)
(2, 1)     = p_{α + β}(± 2 x y)
(2, 2)     = p_{α + β}(± 2 x y) p_{2α + β}(± 3 x^2 y) p_{α + 2β}(± 3 x y^2)
(3, 1)     = p_{α + β}(± 3 x y).
```

<!-- label: III.XXIII.6.4 -->

*Proof.* By virtue of Exp. XXI, 3.5.4, there exists a system of simple roots $\Delta$ of $R$ satisfying: $\alpha \in
\Delta$, and there exist $\alpha' \in \Delta$ and $a, b \in \mathbb{Q}_{+}$ such that $\beta = a \alpha + b \alpha'$.
Consider the pinning $(\Delta, (X_{\alpha})_{\alpha \in \Delta})$ of $G$. The commutation relation to be verified is a
relation between elements of $U_{\alpha \alpha'}$; one is therefore reduced to the explicit calculations of No. 3, and
one concludes at once by condition (SC).

**Corollary 6.5 (Chevalley's rule).** *Let $S$ be a scheme, $(X_{\alpha})_{\alpha \in R}$ a Chevalley system of the
split $S$-group $G$. If $\alpha, \beta, \alpha + \beta \in R$, then*

```text
[X_α, X_β] = ± p X_{α + β},
```

*where $p$ is the smallest integer `> 0` such that $\beta - p \alpha$ is not a root.*

<!-- label: III.XXIII.6.5 -->

<!-- original page 322 -->

Indeed, since the assertion is symmetric in $\alpha$ and $\beta$, one may suppose $long(\alpha) \leqslant long(\beta)$,
and one is reduced to 6.4.

**Corollary 6.6.** *Let $S$ be a scheme such that $6 \cdot 1_{S} \neq 0$ and $(G, T, M, R)$ a split $S$-group. If $R'$
is a subset of $R$ such that*

```text
g_{R'} = t ⊕ ⨁_{α ∈ R'} g_α            (*)
```

*is a Lie subalgebra of $g$, then $R'$ is a closed subset of $R$ (Exp. XXI, 3.1.4).*

<!-- label: III.XXIII.6.6 -->

[^N.D.E-XXIII-15] Indeed, let $(X_{\gamma})_{\gamma \in R^{+}}$ be a Chevalley system of $g$, and let $\alpha, \beta \in
R'$ be such that $\alpha + \beta \in R$. By 6.5 and 6.4,

```text
[X_α, X_β] = ± p X_{α + β},    with p ∈ {1, 2, 3}
```

and since neither 2 nor 3 are zero on $S$, this entails, by (\*), that $g_{R'}$ contains $g_{\alpha + \beta}$, hence
$\alpha + \beta \in R'$.[^N.D.E-XXIII-16]

### 6.7

<!-- label: III.XXIII.6.7 -->

It is possible to make explicit the exact value of the various $\pm$ of this section, thanks to the study of the group
$Norm_{G}(T)$, and more precisely of the "extended Weyl group":

```text
W^* = N(ℤ),    where N = Norm_{Ép_ℤ(R)}(T_ℤ(R))
```

(cf. 5.11), which is an extension of $W(R)$ by an abelian group of type $(2, 2, \cdots, 2)$, which is "responsible for
the signs".[^XXIII-6-1] [^N.D.E-XXIII-17]

**Remark 6.7.1.**[^N.D.E-XXIII-18] *Note that, by point (i) of 3.1.2 and 3.n.1 ($n = 2, 3, 4$), the elements
$w_{\alpha}$ and $w_{\beta}$ of $N(\mathbb{Z})$ satisfy the "braid relations":*

```text
w_α w_β ⋯ = w_β w_α ⋯    (n_{αβ} factors in each term).
```

<!-- label: III.XXIII.6.7.1 -->

(See also [Ti66], [BLie], § IX.4, Ex. 12, and [Sp98], 9.3.2.)

## Bibliography

[^N.D.E-XXIII-19]

[BLie] N. Bourbaki, *Groupes et algèbres de Lie*, Chap. IX, Masson, 1982.

[Ja87] J. C. Jantzen, *Representations of algebraic groups*, Academic Press, 1987; 2nd ed., Amer. Math. Soc., 2003.

[Sp98] T. A. Springer, *Linear algebraic groups*, 2nd ed., Birkhäuser, 1998.

[St62] R. Steinberg, *Générateurs, relations et revêtements de groupes algébriques*, Colloque sur la théorie des groupes
algébriques (Bruxelles 1962), Univ. Louvain & Gauthier-Villars, 1962 (pp. 133–147 in *R. Steinberg Collected Papers*,
Amer. Math. Soc., 1997).

[St67] R. Steinberg, *Lectures on Chevalley groups*, Yale University (1967).

[Ta83] M. Takeuchi, *A hyperalgebraic proof of the isomorphism and isogeny theorems for reductive groups*, J. Algebra
**85** (1983), 179–196.

[Ti66] J. Tits, *Normalisateurs de tores I. Groupes de Coxeter étendus*, J. Algebra **4** (1969), 96–116.

<!-- LEDGER DELTA — Exposé XXIII — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| groupe épinglé | pinned group | Per glossary; Exposé title. |
| épinglage | pinning | Per glossary. |
| groupe déployé | split group | Per glossary. |
| groupe déployable | splittable group | Per glossary. |
| donnée radicielle épinglée | pinned root datum | Pinned = endowed with simple roots; introduced 1.5. |
| `p`-morphisme de données radicielles épinglées | `p`-morphism of pinned root data | Source uses `p`-morphism for `q`-morphism modulo a power of `p`. |
| racines simples | simple roots | Standard. |
| réflexions simples | simple reflections | N.D.E. replaces older "symétries fondamentales". |
| sous-groupe de Borel canonique | canonical Borel subgroup | The Borel attached to the chosen positive system. |
| longueur (d'une racine) | length (of a root) | Notation `long(α)`; preserve abbreviation. |
| ÉpS(R), Ép(R) | Ép_S(R), Ép(R) | Notation preserved; `Ép` short for *épinglé*. |
| schéma en groupes de Chevalley | Chevalley group scheme | Standard. |
| système de Chevalley | Chevalley system | Per 6.1. |
| Règle de Chevalley | Chevalley's rule | Per 6.5. |
| relations de tresses | braid relations | Standard. |
| groupe de Weyl étendu | extended Weyl group | Per 6.7. |
| rang semi-simple | semisimple rank | Abbreviation `rg_{ss}` preserved. |
| isogénies exceptionnelles | exceptional isogenies | Per 5.1; standard. |
| BIBLE | *Bible* | Italicised per glossary. |
| données de recollement / descente | gluing / descent datum | Standard. |
| transformer (sommes en produits) | transform / send | Used for functors taking direct sums to products. |
| « se vérifient » | "are verified" | Quotation marks preserved; signals informal verification. |
| « tout se passe dans Zα » | "everything happens in `Z_α`" | Standard quasi-quote, preserved. |
| « papillon » (folklore image) | butterfly (folklore image) | Per N.D.E. XXIII-1.1; pinning = "pinning the butterfly". |
| Cb | Ĉ | OCR repair; not needed in this Exposé but noted. |
-->

[^N.D.E-XXIII-0]: N.D.E.: Version of 13/10/2024.

[^N.D.E-XXIII-1]: N.D.E.: It is implied by condition (v), i.e. the existence of a section $X_{\alpha} \in \Gamma(S,
    g_{\alpha})^{\times}$.

[^N.D.E-XXIII-2]: N.D.E.: We have denoted by $d$ the bijection $R \xrightarrow{\sim} R'$ (instead of $u$), in order to
    avoid the notation $u'_{u(\alpha)}$.

[^N.D.E-XXIII-3]: N.D.E.: i.e., the Borel subgroup of $Z_{\Delta_{1}}$ corresponding to $R'_{+} = R' \cap R_{+}$.

[^N.D.E-XXIII-4]: N.D.E.: We have replaced "fundamental symmetries" by "simple reflections".

[^N.D.E-XXIII-5]: N.D.E.: We have corrected $i, j > 0$ to $i > 0$, $j \geqslant 0$ (since $x_{\alpha}$ appears in the
    product on the right).

[^N.D.E-XXIII-6]: N.D.E.: relative to $\Delta$.

[^XXIII-3-1]: In the source: "since $(\alpha^{*}, \beta) = 2$". The correct expression $(\alpha^{*}, \beta) = -2$ was
    used in the previous section; here Demazure exploits the resulting formula $s_{\beta}(t_{\alpha}) = t_{\alpha}
    t^{-2}_{\beta} = t_{\alpha}$ (using $t^{2}_{\beta} = e$, which holds in `B_2`).

    <!-- TRANSLATOR NOTE: the source displays "(α^*, β) = 2"; this is a sign-convention discrepancy that does not
    affect the conclusion `s_β(t_α) = t_α` since `t_β^{(α^*, β)}` is computed via the involution `t_β^2 = e`. -->

[^N.D.E-XXIII-7]: N.D.E.: We introduce here absolute constants $A, B, \cdots, J$. These constants will be determined in
    the pages that follow; their values are $A = B = C = D = 1$, $E = 2$, $J = -1$, $F = G = H = 3$, cf. 3.4.8.

[^N.D.E-XXIII-8]: N.D.E.: The relations (3₁) and (3₂) form the description of the normalizer of the torus, (3₁) being,
    like (4), in a group of rank 1, while (3₂) is in a group of rank 2.

[^N.D.E-XXIII-9]: N.D.E.: For an arbitrary field $k$ and $G$ simply connected, R. Steinberg gave a presentation of the
    group $G(k)$ in [St62], Th. 3.2, see also [St67], § 6, Th. 8.

[^N.D.E-XXIII-10]: N.D.E.: To avoid a notational problem later on, we have replaced $q$ by $p$, so that in what follows,
    $q$ (resp. $q_{1}$) is an arbitrary power of $p$.

[^N.D.E-XXIII-11]: N.D.E.: We have spelled out what follows.

[^XXIII-5-1]: In fact, one may prove that every $\mathbb{Z}$-torus is split.[^N.D.E-XXIII-14]

[^N.D.E-XXIII-12]: N.D.E.: Another proof of this corollary, not using the reduction to the case of groups of rank 2, was
    given by M. Takeuchi ([Ta83], Th. 4.6); see also [Ja87], II 1.14.

[^N.D.E-XXIII-13]: N.D.E.: This corollary is rendered superfluous by Exp. XXV, which shows the existence of a split
    group of type $R$ over $\operatorname{Spec}(\mathbb{Z})$, hence over any base $S$. (In fact, after XXV 1.3 one finds
    a reference to the present corollary to ensure that the reductive $\mathbb{Z}$-group obtained is split, but this
    already follows from XXII 2.2; cf. N.D.E. (3) of XXV.)

[^N.D.E-XXIII-15]: N.D.E.: We have added the following proof. Note that it suffices that 2 and 3 be nonzero on $S$; for
    example the result is valid for $S = \operatorname{Spec}(\mathbb{Z}/6\mathbb{Z})$.

[^N.D.E-XXIII-16]: N.D.E.: On the other hand, let us point out that if `2 = 0` on $S$ and $R$ is of type $C_{n}$, then
    the set $R'$ of short roots (which is a root system of type $D_{n}$) is not closed in $R$, but is a part of type (R)
    of $R$, symmetric (cf. XXII 5.4.2 and 5.4.10), i.e. it corresponds to a subgroup $H_{R'}$ of type (R) of $G$ with
    reductive fibers: this is in particular the case for the natural embedding (in characteristic 2) of $SO(2n)$ into
    $Sp(2n)$. Likewise, if `2 = 0` on $S$ and $R$ is of type `F_4` (resp. if `3 = 0` on $S$ and $R$ is of type `G_2`),
    the set $R'$ of short roots (which is a root system of type `D_4` (resp. `A_2`)) is not closed in $R$, but
    corresponds to a subgroup $H_{R'}$ of type (R) of $G$, with reductive fibers.

[^XXIII-6-1]: Cf. J. Tits, *Sur les constantes de structure et le théorème d'existence des algèbres de Lie
    semi-simples*, Publ. Math. I.H.É.S. **31** (1966), 21–58.

[^N.D.E-XXIII-17]: N.D.E.: see also [Ti66].

[^N.D.E-XXIII-18]: N.D.E.: We have added this remark.

[^N.D.E-XXIII-19]: N.D.E.: additional references cited in this Exposé.

[^N.D.E-XXIII-14]: N.D.E.: this follows from the fact that every $\mathbb{Z}$-torus is isotrivial (Exp. X, 5.16) and
    from the fact that every étale covering of $\operatorname{Spec}(\mathbb{Z})$ is trivial.
