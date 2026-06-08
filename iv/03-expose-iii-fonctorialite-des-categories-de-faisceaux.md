# SGA 4-I — Expose III: Functoriality of Categories of Sheaves

> Translated from the cleaned OCR transcription of the image-only SGA 4-I scan. The file has been normalized for
> readability. Diagrams and dense formulas remain in fenced text blocks where faithful Markdown transcription is
> uncertain. Consult the PDF for mathematical fidelity.

[PDF p. 280]

# Expose III — Functoriality of Categories of Sheaves

By J.-L. Verdier.

In I 5, the behavior of categories of presheaves with respect to functors between the categories of arguments was
studied.

In this expose, this study is extended to the case of sites and categories of sheaves (§§ 1 and 2). After introducing
the induced topology (§ 3), § 4 takes up the comparison lemma, which will play an important role in Expose IV. In § 5,
for the patient reader, we study certain commutative diagrams connected with localized categories of the type $C/X$.

In Theorem I 5.1, smallness hypotheses are imposed on the categories under consideration. These hypotheses are not, in
general, satisfied by the sites encountered in practice, that is, by $U$-sites. This forces a few contortions (4.2, 4.3,
4.4).

## 1. Continuous Functors

**Definition 1.1.** Let $C$ and $C'$ be two $U$-sites, and let $u : C \to C'$ be a functor between the underlying
categories. We say that $u$ is **continuous** if, for every sheaf of sets $F$ on $C'$, the presheaf $X \mapsto F(u(X))$
on $C$ is a sheaf.

This notion of continuity depends a priori on the universe $U$ for which the two sites are $U$-sites. Proposition 1.5
shows that it does not depend on it.

[PDF p. 281]

**1.1.1.** Denote by $i : \widetilde{C} \to \widehat{C}$ the canonical inclusion functor from sheaves into presheaves,
and by $i' : \widetilde{C'} \to \widehat{C'}$ the analogous functor for $C'$. By Definition 1.1, the functor $u$ is
continuous if and only if there exists a functor $u_s : \widetilde{C'} \to \widetilde{C}$ such that $i u_s = u^* i'$,
where $u^*F = F \circ u$ (I 5.0).

**Proposition 1.2.** Let $C$ be a small site, $C'$ a $U$-site, and $u : C \to C'$ a functor between the underlying
categories. The following properties are equivalent:

1. The functor $u$ is continuous.
2. For every object $X$ of $C$ and every sieve $R \to X$ covering $X$, the morphism $u_!R \to u_!X$ is bicovering in
   $\widehat{C'}$ (II 5.2 and I 5.1). (\*)
3. For every bicovering family $H_i \to K$, $i \in I$, of $\widehat{C}$, the family $u_!H_i \to u_!K$, $i \in I$, is
   bicovering in $\widehat{C'}$.
4. There exists a functor $u^s : \widetilde{C} \to \widetilde{C'}$, commuting with inductive limits and "extending $u$",
   that is, making commutative, up to isomorphism, the canonical diagram between $C$, $C'$, and their categories of
   sheaves.

Moreover, when $C$ is no longer necessarily a small site, but a $U$-site, one still has $1 \Longleftrightarrow 4$. The
functor of 4 is necessarily a left adjoint of the functor $u_s : \widetilde{C'} \to \widetilde{C}$; it is therefore
determined up to unique isomorphism.

(\*) "Covering" instead of "bicovering" does not necessarily suffice; cf. Example 1.9.3 below.

[PDF p. 282]

**Proof.** The proof of $1 \Longleftrightarrow 4$ when $C$ is a $U$-site will be given in 4.2. Suppose $C$ is small. It
is clear that $3 \Rightarrow 2$.

$1 \Rightarrow 3$. Let $H_i \to K$, $i \in I$, be a bicovering family of $\widehat{C}$. For every sheaf $F$ on $C'$, the
presheaf $u^*F$ (I 5.0) is a sheaf on $C$. Therefore, by II 5.3, the canonical map

$$ \operatorname{Hom}(K,u^*F) \to \prod_i \operatorname{Hom}(H_i,u^*F) $$

is bijective. By adjunction (I 5.1), one deduces that the canonical map

$$ \operatorname{Hom}(u_!K,F) \to \prod_i \operatorname{Hom}(u_!H_i,F) $$

is bijective. Consequently, by II 5.3, the family $u_!H_i \to u_!K$, $i \in I$, is bicovering.

$2 \Rightarrow 1$. Let $X$ be an object of $C$, let $R \to X$ be a covering sieve, and let $F$ be a sheaf on $C'$. By II
5.3, the map

$$ \operatorname{Hom}(u_!X,F) \to \operatorname{Hom}(u_!R,F) $$

is bijective. By adjunction (I 5.1), one deduces that the map

$$ \operatorname{Hom}(X,u^*F) \to \operatorname{Hom}(R,u^*F) $$

is bijective. Consequently $u^*F$ is a sheaf.

$1 \Rightarrow 4$. Use the usual notation $a$ and $i$, respectively $a'$ and $i'$, for the "associated sheaf" and
"inclusion into presheaves" functors. For every sheaf $G$ on $C$, put $u^sG = a'u_!iG$. For every sheaf $F$ on $C'$, one
has the sequence of natural isomorphisms

$$
\begin{aligned}
\operatorname{Hom}(G,u_sF)
&= \operatorname{Hom}(iG,iu_sF) \\
&= \operatorname{Hom}(iG,u^*i'F) \\
&= \operatorname{Hom}(u_!iG,i'F) \\
&= \operatorname{Hom}(a'u_!iG,F).
\end{aligned}
$$

[PDF p. 283]

The first isomorphism comes from the fact that $i$ is fully faithful; the second comes from the definition of $u_s$; the
third and fourth are obtained by adjunction. Consequently $u^s$ is left adjoint to $u_s$. In particular, $u^s$ commutes
with inductive limits.

For every presheaf $K$ on $C$ and every sheaf $F$ on $C'$, one has the sequence of natural isomorphisms

$$
\begin{aligned}
\operatorname{Hom}(u^s aK,F)
&= \operatorname{Hom}(aK,u_sF) \\
&= \operatorname{Hom}(K,iu_sF) \\
&= \operatorname{Hom}(K,u^*i'F) \\
&= \operatorname{Hom}(u_!K,i'F) \\
&= \operatorname{Hom}(a'u_!K,F).
\end{aligned}
$$

The third isomorphism comes from the definition of $u_s$; the others are obtained by adjunction. We thus obtain a
functorial isomorphism $u^s aK \simeq a'u_!K$. In particular, when $K$ is representable, taking I 5.4.3 into account,
one obtains a diagram commutative up to isomorphism:

```text
C --u--> C'
|        |
epsilon_C      epsilon_C'
v        v
C~ --u^s--> C'~
```

$4 \Rightarrow 2$. Let $h : C \to \widehat{C}$, respectively $h' : C' \to \widehat{C'}$, be the functor that associates
to an object the presheaf it represents. Consider the canonical diagram corresponding to the functors $u$, $u_!$, $u^s$,
$a$, $a'$, $h$, and $h'$.

[PDF p. 284]

The upper square is commutative (I 5.4.3), and one has $ah = \varepsilon_C$ and $a'h' = \varepsilon_{C'}$. For every
object $K$ of $\widehat{C}$, one has a canonical isomorphism (I 3.4)

$$ \operatorname{colim}_{(h(X)\to K)\in \operatorname{ob}(C/K)} h(X) \to K. $$

Since the functors $u_!$, $u^s$, $a$, and $a'$ commute with inductive limits, one deduces isomorphisms

$$ \operatorname{colim} a'h'u(X) \to u^s aK,\qquad \operatorname{colim} a'u_!h(X) \to a'u_!K. $$

We have $u_!h = h'u$ and, by hypothesis, an isomorphism $a'h'u \simeq u^s ah$. It follows that there is an isomorphism

$$ u^s aK \simeq a'u_!K, $$

functorial in $K$. The diagram is therefore commutative up to isomorphism. Since $ai$ is isomorphic to the identity
functor, one has an isomorphism $u^s \simeq a'u_!i$, whence the uniqueness of $u^s$.

Let $v : H \to K$ be a bicovering morphism of $\widehat{C}$. Then $a(v)$ is an isomorphism (II 5.3), and consequently
$a'u_!(v)$, isomorphic to $u^s a(v)$, is an isomorphism. Thus $u_!(v)$ is transformed by $a'$ into an isomorphism, and
consequently $u_!(v)$ is bicovering (II 5.3). This proves $2$.

[PDF p. 285]

The additional assertion, in the case where $C$ is small, was proved during the proof.

**1.2.1.** The functor $u^s : \widetilde{C} \to \widetilde{C'}$ of 1.2(iv) can often be interpreted as an "inverse
image" functor for a "morphism of topoi" $\widetilde{C'} \to \widetilde{C}$; cf. IV 4.9. Its properties are summarized
in the following proposition.

**Proposition 1.3.** Let $u : C \to C'$ be a continuous functor between a small site $C$ and a $U$-site $C'$.

1. The functor $u^s$ is left adjoint to the functor $u_s$.
2. There is a canonical isomorphism $a'u_!i \simeq u^s$.
3. There is a canonical isomorphism $u^s a \simeq a'u_!$.
4. The functor $u^s$ commutes with inductive limits.
5. When the functor $u_!$ is left exact (cf. I 5.4.4), the functor $u^s$ is left exact as well. More generally, the
   functor $u^s$ commutes with the types of finite projective limits with which the functor $u_!$ commutes.

**Proof.** Assertions 1, 2, 3, and 4 were proved during the proof of 1.2. Assertion 5 follows from the isomorphism 2,
taking into account that $i$ commutes with projective limits and that $a'$ commutes with finite projective limits (II
4.1).

**Remark 1.4.** Combining I 5.4.3 and 1.3.3, one obtains a diagram:

```text
C --u--> C'
|        |
h        h'
v        v
C^ --u_!--> C'^
|          |
a          a'
v          v
C~ --u^s--> C'~
```

[PDF p. 286]

where the upper square is commutative and the lower square is commutative up to isomorphism. But the functors $a$, $a'$,
$u_!$, and $u^s$ are defined only up to isomorphism. The reader may verify that one can choose the functors $a$, $a'$,
and $u^s$ so that:

1. the composite functors $ah$ and $a'h'$ are injective on sets of objects;
2. the diagram indicated in the scan is commutative.

More precisely, one can choose the functors $a$ and $a'$ so as to satisfy condition 1. Once the functors $a$ and $a'$
have been chosen, one can choose the functor $u^s$ so as to satisfy condition 2.

**Proposition 1.5.** Let $U \in V$ be two universes, let $C$ and $C'$ be two $U$-sites, and let $u : C \to C'$ be a
functor between the underlying categories. Then $u$ is continuous relative to $U$ if and only if it is continuous
relative to $V$.

Moreover, when $u$ is continuous, denote by $u^s_U$, respectively $u^s_V$, the functor between categories of
$U$-sheaves, respectively of $V$-sheaves, introduced in 1.2(iv). Then the diagram

```text
C~_U  --u^s_U-->  C'~_U
 |                  |
 v                  v
C~_V  --u^s_V-->  C'~_V
```

[PDF p. 287]

where the vertical functors are the canonical inclusion functors, is commutative up to canonical isomorphism.

**Proof.** We give the proof only in the case where $C$ is $U$-small. The general case will be proved in 4.3. It is
clear that if the functor $u^*$ transforms every $V$-sheaf on $C'$ into a $V$-sheaf on $C$, then it transforms every
$U$-sheaf on $C'$ into a $U$-sheaf on $C$.

Suppose then that $u^*$ transforms every $U$-sheaf on $C'$ into a $U$-sheaf on $C$. Denote by $\widehat{C}_U$,
$\widehat{C'}_U$, respectively $\widehat{C}_V$, $\widehat{C'}_V$, the categories of $U$-presheaves and $V$-presheaves,
and denote by $u_!^U$ and $u_!^V$ the "inverse image" functors for $U$-presheaves and $V$-presheaves respectively. One
has a commutative diagram (cf. the explicit construction of $u_!$ in I 5.1):

```text
C^_U   --u_!^U-->   C'^_U
 |                   |
 v                   v
C^_V   --u_!^V-->   C'^_V
```

The inclusion functors from $U$-presheaves into $V$-presheaves are fully faithful and commute with projective limits. It
then follows from II 5.1(i) that a bicovering morphism of $U$-presheaves is a bicovering morphism of $V$-presheaves.

Let $R \to X$ be a sieve covering an object $X$ of $C$. By 1.2(ii), the morphism $u_!^U R \to u_!^U X$ is bicovering.
Using the commutativity of the preceding diagram and what precedes, one deduces that the morphism $u_!^V R \to u_!^V X$
is bicovering. Consequently, by 1.2, the functor $u^*$ transforms $V$-sheaves on $C'$ into $V$-sheaves on $C$.

The commutativity of the diagram of 1.5 then follows from the commutativity of the preceding diagram, from II 3.6, and
from 1.3.2.

[PDF p. 288]

**Proposition 1.6.** Let $C$ and $C'$ be two $U$-sites, and let $u : C \to C'$ be a functor between the underlying
categories. Consider the following conditions:

1. $u$ is continuous (cf. 1.1 and 1.2).
2. For every covering family $(X_i \to X)$, $i \in I$, of $C$, the family $(uX_i \to uX)$, $i \in I$, of $C'$, is
   covering.

One has the implication $1 \Rightarrow 2$.

Suppose that the topology of $C$ can be defined by a pretopology $T$ (II 1.3) and that the functor $u$ commutes with
fiber products. Then conditions 1 and 2 are equivalent and are equivalent to the following condition:

1. The functor $u$ transforms the covering families of $T$ into covering families of $C'$.

In particular, suppose that, in $C$, fiber products are representable and that the functor $u$ commutes with fiber
products. Then conditions 1 and 2 are equivalent.

Note: it in fact suffices that $u$ commute with the fiber products occurring in base changes for morphisms coming from
covering families for $T$.

**Proof.** We show that $1 \Rightarrow 2$. Let $X_i \to X$, $i \in I$, be a covering family of $C$. For every sheaf $F$
on $C'$, $u^*F$ is a sheaf. Consequently the map

$$ \operatorname{Hom}(X,u^*F) \to \prod_i \operatorname{Hom}(X_i,u^*F) $$

is injective (II 5.1). Hence an injective map

$$ \operatorname{Hom}(uX,F) \to \prod_i \operatorname{Hom}(uX_i,F). $$

Thus the family $uX_i \to uX$, $i \in I$, is covering in $C'$ (II 5.1).

Every covering family of the pretopology $T$ is a covering family of $C$, whence $2 \Rightarrow 3$. We show that $3
\Rightarrow 1$. Let $X$ be an object of $C$ and let $X_i \to X$, $i \in I$, be a covering family of
$\operatorname{Cov}(X)$ (II 1.3).

[PDF p. 289]

The morphisms $X_i \to X$ are squarable, and the functor $u$ commutes with fiber products. Consequently the fiber
products $u(X_i) \times_{u(X)} u(X_j)$ are representable and canonically isomorphic to $u(X_i \times_X X_j)$. Let $F$ be
a sheaf on $C'$. Then the diagram of sets

$$ F(uX) \to \prod_i F(uX_i) \rightrightarrows \prod_{i,j} F(u(X_i \times_X X_j)) $$

is exact (II 2.1, I 3.5 and I 2.12). Consequently the diagram of sets

$$ u^*F(X) \to \prod_i u^*F(X_i) \rightrightarrows \prod_{i,j} u^*F(X_i \times_X X_j) $$

is exact. Thus $u^*F$ is a sheaf (II 2.4), whence 1.

The last assertion of 1.6 follows from what precedes and from the fact that, when fiber products are representable in
$C$, all covering families of $C$ define on $C$ a pretopology whose associated topology is the topology of $C$.

**Proposition 1.7.** Let $C$ be a small site, $C'$ a $U$-site, and $u : C \to C'$ a continuous functor. Let $\gamma$ be
an algebraic structure defined by finite projective limits, such that, in the category of $\gamma$-objects of $U$-Ens,
$U$-inductive limits are representable. We use the notation of Proposition II 6.4.

The functor $u_s$ commutes with projective limits and consequently defines a functor $u_{s,\gamma}$ between the
categories of sheaves with values in $\gamma$-objects. The functor $u_{s,\gamma}$ admits a left adjoint $u^s_\gamma$,
which has the following properties.

Note: the inductive limits are indexed by sets belonging to a suitable universe. One can in fact show that this
condition is always satisfied.

[PDF p. 290]

1. There is a canonical isomorphism $u^s_\gamma \simeq a'_\gamma u_! i_\gamma$, and $u^s_\gamma$ commutes with the
   finite projective limits with which $u_s$ commutes.
2. There is a canonical isomorphism $u^s_\gamma a_\gamma \simeq a'_\gamma u_!$.
3. The functor $u^s_\gamma$ commutes with inductive limits.
4. If $u^s$ is left exact, the diagram below, in the notation of II 6.3.0, is commutative up to isomorphism and the
   functor $u^s_\gamma$ is exact.

    ```text
    C~_gamma --u^s_gamma--> C'~_gamma
     |                       |
    ens                     ens'
     v                       v
    C~        --u^s-->       C'~
    ```

5. Suppose that the functor $\widetilde{\operatorname{ens}}$, respectively $\widetilde{\operatorname{ens}}'$, has a left
   adjoint $\widetilde{\operatorname{Lib}}$, respectively $\widetilde{\operatorname{Lib}}'$ (II 6.5). There is a
   canonical isomorphism

    $$
    u^s_\gamma \widetilde{\operatorname{Lib}} \simeq
    \widetilde{\operatorname{Lib}}' u^s.
    $$

Moreover, when $C$ is not necessarily a small site but a $U$-site, the functor $u_{s,\gamma}$ admits a left adjoint
$u^s_\gamma$. Finally, if $V$ is a universe containing $U$, and if $u^s_{\gamma,U}$, respectively $u^s_{\gamma,V}$,
denotes the left adjoint of $u_{s,\gamma}$ relative to the universe $U$, respectively $V$, the following diagram,
analogous to diagram 1.5.1,

```text
C~_{gamma,U} --u^s_{gamma,U}--> C'~_{gamma,U}
   |                                 |
   v                                 v
C~_{gamma,V} --u^s_{gamma,V}--> C'~_{gamma,V}
```

is commutative up to canonical isomorphism.

**Proof.** The proof, in the case where $C$ is a small site, is left to the reader. It will be completed in 4.3 in the
case where $C$ is a $U$-site.

[PDF p. 291]

**Notation 1.8.** From now on we shall use the notation $u_s$ to denote the functor $u_{s,\gamma}$. This notation risks
no confusion, because the functor $u_s$, defined on sheaves of sets, commutes with finite projective limits.

Similarly, when $u^s$ is left exact, we shall use the notation $u^s$ to denote the functor $u^s_\gamma$. This abuse of
notation is justified by 1.7.4.

**Example 1.9.1.** Let $X$ be a small topological space. Denote by $\operatorname{Ouv}(X)$ the category of opens of $X$:
its objects are the open subsets of $X$, and its morphisms are inclusions. We equip $\operatorname{Ouv}(X)$ with the
canonical topology. A family $(U_i \to U)$, $i \in I$, is covering if and only if the opens $U_i$ cover $U$ (II 2.6).

Sheaves of sets on $\operatorname{Ouv}(X)$ are therefore sheaves of sets in the sense of [TF].

Let $f : X \to Y$ be a continuous map. One deduces a functor $f^{-1} : \operatorname{Ouv}(Y) \to \operatorname{Ouv}(X)$:
for every open $U$ of $Y$, $f^{-1}(U)$ is the inverse image of $U$ by the map $f$. The functor $f^{-1}$ is continuous
(1.6). The functor

$$ f_* : \widetilde{\operatorname{Ouv}(X)} \to \widetilde{\operatorname{Ouv}(Y)} $$

is the direct image functor for sheaves, in the sense of [TF]. The functor

$$ f^* : \widetilde{\operatorname{Ouv}(Y)} \to \widetilde{\operatorname{Ouv}(X)} $$

is the inverse image functor for sheaves, in the sense of [TF]. The functor $(f^{-1})^s$ commutes with finite projective
limits, thanks to 1.3.5.

**Example 1.9.2.** Let $X$ be a topological space and let $Y \to X$ be an open of $X$. Every open of $Y$ is an open of
$X$, whence a functor $j : \operatorname{Ouv}(Y) \to \operatorname{Ouv}(X)$. The functor $j$ is continuous (1.6). The
functor $j_s : \widetilde{\operatorname{Ouv}(X)} \to \widetilde{\operatorname{Ouv}(Y)}$ is the "restriction to $Y$"
functor. The functor $\widetilde{\operatorname{Lib}} : \widetilde{\operatorname{Ouv}(Y)} \to
\widetilde{\operatorname{Ouv}(X)}$ (II 6.3.3, I 1.7) is the "

[PDF p. 292]

extension by zero outside $Y$" functor introduced in [TF].

The functor $j^* : \widetilde{\operatorname{Ouv}(Y)} \to \widetilde{\operatorname{Ouv}(X)}$ (1.3) is analogous to the
"extension by zero" functor: for every sheaf $H$ on $Y$ and every point $y \in Y$, the fiber at $y$ of $j^*H$ is
canonically isomorphic to the fiber at $y$ of $H$; for every point $x \in X$, $x \notin Y$, the fiber at $x$ of $j^*H$
is empty. The functor $j^*$ is called the "extension by the empty object outside $Y$" functor.

The functor $j^*$ commutes with fiber products and finite products over a nonempty set of indices, but it does not
transform the final object of $\widetilde{\operatorname{Ouv}(Y)}$ into the final object of
$\widetilde{\operatorname{Ouv}(X)}$.

**Example 1.9.3.** Let $C$ and $C'$ be two small sites, and let $u : C \to C'$ be a functor between the underlying
categories that transforms every covering family of $C$ into a covering family of $C'$. The functor $u$ is not
continuous in general (cf. however 1.6). Here is a counterexample.

Let $S$ be a set of infinite cardinality in the universe $U$, and let $C$ be the full subcategory of the category of
sets whose objects are the nonempty finite subsets of $S$. We equip $C$ with the canonical topology. The covering
families of $C$ are the surjective families of maps, and covering families are not empty. Moreover, up to isomorphism,
there are only two constant sheaves on $C$: the sheaf with value the empty set and the sheaf with value the one-element
set.

Put $C = C'$ and let $u : C \to C'$ be a constant functor. The functor $u$ transforms covering families of $C$ into
covering families of $C'$. But the functor $u$ is not continuous. Indeed, since the representable presheaves of $C'$ are
sheaves, for every object $X$ of $C'$, there exists a

[PDF p. 293]

sheaf $F$ on $C'$ such that the cardinality of the set $F(X)$ is $\geq 2$, and consequently the presheaf $u^*F$ is not a
sheaf.

## 2. Cocontinuous Functors

**Definition 2.1.** Let $C$ and $C'$ be two $U$-sites, and let $u : C \to C'$ be a functor between the underlying
categories. We say that $u$ is **cocontinuous** if it has the following property:

`(COC)` For every object $Y$ of $C$ and every sieve $R \to u(Y)$ covering $u(Y)$, the sieve of $Y$ generated by the
arrows $Z \to Y$ such that $u(Z) \to u(Y)$ factors through $R$, covers $Y$.

**Proposition 2.2.** Let $C$ be a small site, $C'$ a $U$-site, and $u : C \to C'$ a functor between the underlying
categories. Denote by $u_* : \widehat{C} \to \widehat{C'}$ the functor right adjoint to the functor $F \mapsto F \circ u
= u^*F$ (I 5.1). The functor $u$ is cocontinuous if and only if, for every sheaf $G$ on $C$, $u_*G$ is a sheaf on $C'$.

**Proof.** The condition is sufficient. Suppose that, for every sheaf $G$ on $C$, the presheaf $u_*G$ is a sheaf. Let
$Y$ be an object of $C$ and $R \to u(Y)$ a covering sieve. We have an isomorphism

$$ \operatorname{Hom}(u(Y),u_*G) \to \operatorname{Hom}(R,u_*G). $$

By adjunction (I 5.1), one deduces an isomorphism

$$ \operatorname{Hom}(u^*u(Y),G) \to \operatorname{Hom}(u^*R,G). $$

It follows (II 5.3) that the morphism $u^*R \to u^*u(Y)$ is bicovering. But the functor $u^*$ commutes with projective
limits; consequently the morphism $u^*R \to u^*u(Y)$ is a monomorphism, hence a covering monomorphism. On the other
hand, we have a canonical morphism $Y \to u^*u(Y)$ deduced from the adjunction morphism

[PDF p. 294]

$\operatorname{id} \to u^*u_*$ (I 5.4.3). Make the base change $Y \to u^*u(Y)$. We obtain a sieve covering $Y$:

$$ u^*R \times_{u^*u(Y)} Y \to Y. $$

The arrows $Z \to Y$ that factor through this sieve are exactly those of the sieve described by property `(COC)`.

The condition is necessary. Let $S$ be an object of $C'$ and $R \to S$ a sieve covering $S$. We must prove that, for
every sheaf $G$ on $C$, one has an isomorphism

$$ \operatorname{Hom}(S,u_*G) \to \operatorname{Hom}(R,u_*G). $$

Using Proposition II 5.3 and the adjunction isomorphisms, it suffices to prove that the monomorphism $u^*R \to u^*S$ is
covering. For this, it suffices to prove (II 5.1) that, for every base change $Y \to u^*S$, with $Y$ an object of $C$,
the sieve

$$ u^*R \times_{u^*S} Y \to Y $$

is covering.

By the properties of adjoint functors and I 5.4.3, the morphism $Y \to u^*S$ factors through

$$ Y \to u^*u(Y) \to u^*S. $$

Consequently the sieve $u^*R \times_{u^*S} Y \to Y$ is the transform, by the base change $Y \to u^*u(Y)$, of the
monomorphism

$$ u^*R \times_{u^*S} u^*u(Y) \to u^*u(Y). $$

Now the functor $u^*$ commutes with projective limits; this monomorphism is therefore the transform by $u^*$ of the
sieve $R \times_S u(Y) \to u(Y)$, which is covering. Hypothesis `(COC)` then says that the sieve $u^*R \times_{u^*S} Y
\to Y$ is covering.

**Proposition 2.3.** Let $C$ and $C'$ be two $U$-sites, and let $u : C \to C'$ be a cocontinuous functor. Denote by
$u^* : \widetilde{C'} \to \widetilde{C}$ the functor $u^* = a u^* i'$, where $a$ denotes the "associated sheaf" functor
for $C$, where, in the right-hand member, $u^*$ denotes the functor $F \mapsto F \circ u$, and where $i'$ denotes the

[PDF p. 295]

inclusion functor $\widetilde{C'} \to \widehat{C'}$.

1. The functor $u^*$ commutes with inductive limits and is exact.
2. There is a canonical isomorphism $u^* a' \simeq a u^*$, where $a'$ denotes the "associated sheaf" functor for
   $\widehat{C'}$.
3. The functor $u^*$ admits a right adjoint $u_* : \widetilde{C} \to \widetilde{C'}$. When $C$ is small, the diagram

    ```text
    C~ --u_*--> C'~
    |           |
    i           i'
    v           v
    C^ --u_*--> C'^
    ```

    where the lower functor is right adjoint to the functor $u^*$ (I 5.1), is commutative up to canonical isomorphism.

4. Let $V \supset U$ be a universe. Denote by $u_{*,U}$ (resp. $u_{*,V}$) the right adjoint functor relative to the
   universe $U$ (resp. $V$), whose existence is asserted in 3). The diagram

    ```text
    C~_U --u_{*,U}--> C'~_U
     |                  |
     v                  v
    C~_V --u_{*,V}--> C'~_V
    ```

    is commutative up to isomorphism.

**Proof.** Assertions 1) and 2) follow immediately from II 3.4. Assertion 3), when $C$ is small, follows from 2.2. When
$C$ is a $U$-site, it will be proved in 4.4. Assertion 4), when $C$ is small, follows from the analogous commutativity
assertion when the topologies on $C$ and $C'$ are chaotic, and from I 3.5. When the topologies on $C$ and $C'$ are

[PDF p. 296]

chaotic, the commutativity of (2.3.2) is seen immediately from the explicit description of $u_*$ (I 5.1).

**2.4.** We shall not develop here the considerations concerning $\gamma$-objects of categories of sheaves. It will
suffice to observe that the functors $u^*$ and $u_*$ introduced in this section always commute with finite projective
limits (contrary to what happened in the preceding section for the functor $u_s$). Consequently they extend naturally to
functors defined on $\gamma$-objects, which are adjoint to one another and which commute with the "underlying sheaf of
sets" functors. We shall make the abuses of notation indicated in 1.8, consisting in writing $u^*$ and $u_*$ for the
extensions to $\gamma$-objects.

**Proposition 2.5.** Let $C$ and $C'$ be two $U$-sites, and let $v : C' \to C$ and $u : C \to C'$ be two functors, where
$v$ is left adjoint to $u$. The following properties are equivalent:

1. The functor $u$ is continuous.
2. The functor $v$ is cocontinuous.

Moreover, under these equivalent conditions, one has canonical isomorphisms

$$ v_* \simeq u_s,\qquad v^* \simeq u^s. $$

In particular, the functor $u^s$ commutes with finite projective limits.

**Proof.** The property, for a functor, of being continuous or cocontinuous does not depend on the universe $U$ for
which $C$ and $C'$ are $U$-sites: this is immediate in the case of a cocontinuous functor, and follows from 1.5 in the
case of a continuous functor. We may therefore, after increasing the universe if necessary, suppose that $C$ and $C'$
are small. The proposition then follows from 2.2 and I 5.6.

[PDF p. 297]

**Proposition 2.6.** Let $u : C \to C'$ be a continuous and cocontinuous functor between two $U$-sites. Then the functor
$u^* : \widetilde{C'} \to \widetilde{C}$ (2.3) commutes with $U$-inductive and projective limits. Denote by $u_! :
\widetilde{C} \to \widetilde{C'}$ and $u_* : \widetilde{C} \to \widetilde{C'}$ the functors adjoint to $u^*$ on the left
and on the right respectively. The functor $u_!$ is fully faithful if and only if the functor $u_*$ is fully faithful.
When $u$ is fully faithful, $u_!$ is fully faithful, and the converse is true when the topologies of $C$ and $C'$ are
less fine than the canonical topology.

The functor $u^*$ admits a right adjoint $u_*$ (2.3) and a left adjoint $u_!$ (1.2). The functor $u^*$ therefore
commutes with inductive and projective limits (I 2.11). The fact that $u_!$ is fully faithful if and only if $u_*$ is
fully faithful is a general property of adjoint functors (I 5.7.1).

When $u$ is fully faithful, the functor $u^* : \widehat{C'}_V \to \widehat{C}_V$, relative to $V$-presheaves, for a
sufficiently large universe $V$, is fully faithful (I 5.7). Consequently the functor $u_* : \widetilde{C} \to
\widetilde{C'}$ is fully faithful by virtue of the commutativity of (2.3.1) and (2.3.2), hence $u_!$ is fully faithful
by what precedes. The converse is deduced from the existence of the commutative diagram 1.2 iv), taking into account the
fact that the functors $\varepsilon_C$ and $\varepsilon_{C'}$ are fully faithful when the topologies are less fine than
the canonical topology. QED.

**Example 2.7.** With the notation of 1.9.2, the functor

$$ \varphi : \operatorname{Ouv}(Y) \to \operatorname{Ouv}(X) $$

is continuous (1.9.2) and cocontinuous (2.2). Moreover, let $i : Y \to X$

[PDF p. 298]

be the canonical injection and $i^{-1} : \operatorname{Ouv}(X) \to \operatorname{Ouv}(Y)$ the functor it makes possible
to define (1.9.1). The functor $i$ is right adjoint to the functor $\varphi$. We therefore have a sequence of three
adjoint functors:

$$ \varphi^s,\quad \varphi_s \simeq i^{-1},\quad \varphi_*, $$

and canonical isomorphisms

$$ \varphi^* \simeq (i^{-1})^s,\qquad \varphi_* \simeq i_s^{-1}. $$

## 3. Induced Topology

**3.1.** Let $C'$ be a site, $C$ a category, and $u : C \to C'$ a functor. For every universe $U$ such that $C'$ is a
$U$-site and $C$ is a $U$-small category, denote by $\mathcal{T}_U$ the finest among the topologies $T$ on $C$ that make
$u$ continuous (1.1). Such a topology exists thanks to II 2.2.

The topology $\mathcal{T}_U$ does not depend on the universe $U$. Indeed, if $V \supset U$ is a universe, then
$\mathcal{T}_U = \mathcal{T}_V$ (1.1 and 1.5). The topology $\mathcal{T}_U$ is called the topology induced on $C$ by the
topology of $C'$ by means of the functor $u$.[^induced]

**Proposition 3.2.** Let $C$ be a small category, $C'$ a $U$-site, $u : C \to C'$ a functor, and $\mathcal{T}$ the
topology on $C$ induced by $u$. Let $X$ be an object of $C$ and $R \to X$ a sieve of $X$. The following properties are
equivalent:

1. The sieve $R \to X$ is covering for $\mathcal{T}$.
2. For every base change $Y \to X$, where $Y$ is an object of $C$, the morphism $u_!(R \times_X Y) \to u(Y)$ is
   bicovering in $\widehat{C'}$ (II 5.2).

**Proof.** $i) \Rightarrow ii)$ follows from axiom (T1) for topologies and from 1.2.

$ii) \Rightarrow i)$: For every sheaf $F$ on $C'$, the map

[PDF p. 299]

$$ \operatorname{Hom}(Y,u^*F) \to \operatorname{Hom}(R \times_X Y,u^*F) $$

is isomorphic, by adjunction (I 5.1), to the map

$$ \operatorname{Hom}(u(Y),F) \to \operatorname{Hom}(u_!(R \times_X Y),F), $$

which is bijective (II 5.3). Consequently (II 2.2), the sieve $R \to X$ is covering for $\mathcal{T}$.

**Corollary 3.3.** Let $C'$ be a site, $C$ a category, $u : C \to C'$ a functor, and $\mathcal{T}$ the topology on $C$
induced by the topology of $C'$. Let $(X_i \to X)_{i \in I}$ be a family of squarable morphisms of $C$, and suppose that
$u$ commutes with fiber products.[^fibers] The following properties are equivalent:

1. The family $X_i \to X$, $i \in I$, is covering for $\mathcal{T}$.
2. The family $(u(X_i) \to u(X))$, $i \in I$, is covering.

**Proof.** $i) \Rightarrow ii)$ follows from 1.6.

$ii) \Rightarrow i)$: Let $U$ be a universe such that $C$ is $U$-small and $C'$ is a $U$-site. Let $R \to X$ be the
sieve generated by the $X_i \to X$. The presheaf $R$ is the cokernel of the pair of arrows (I 2.12 and I 3.5)

$$ \coprod_{i,j} X_i \times_X X_j \rightrightarrows \coprod_i X_i $$

where the direct sum is taken here in $\widehat{C}$. Since the functor $u_!$ commutes with inductive limits (I 5.4), the
presheaf $u_!R$ is the cokernel of the pair of arrows

$$ \coprod_{i,j} u(X_i \times_X X_j) \rightrightarrows \coprod_i u(X_i). $$

Since the functor $u$ commutes with fiber products, the presheaf $u_!R$ is the cokernel of the pair of arrows

[PDF p. 300]

$$ \coprod_{i,j} u(X_i) \times_{u(X)} u(X_j) \rightrightarrows \coprod_i u(X_i), $$

and consequently $u_!R \to u(X)$ is a sieve of $u(X)$ generated by the $u(X_i) \to u(X)$, $i \in I$. Again using the
fact that $u$ commutes with fiber products, one shows that, for every base change $Y \to X$, where $Y$ is an object of
$C$, $u_!(R \times_X Y) \to u(Y)$ is a sieve of $u(Y)$ generated by the $u(X_i) \times_{u(X)} u(Y) \to u(Y)$, $i \in I$.
Since the family $u(X_i) \to u(X)$, $i \in I$, is covering, the family $u(X_i) \times_{u(X)} u(Y) \to u(Y)$, $i \in I$,
is covering. Thus $u_!(R \times_X Y) \to u(Y)$ is a covering sieve, and consequently (3.2) $R \to X$ is covering for
$\mathcal{T}$. QED.

**Corollary 3.4.** Let $C'$ be a $U$-site, let $C$ be a full subcategory of $C'$, and let $u : C \to C'$ be the
inclusion functor. Suppose that fiber products are representable in $C$ and that $u$ commutes with fiber products. The
following conditions are equivalent:

1. The following two conditions hold:

    a. For every object $X$ of $C$, every covering family $(Y_j \to X)$,
    $j \in J$, of $C'$ is dominated by a covering family $X_i \to X$,
    $i \in I$, where the $X_i$ are objects of $C$.

    b. There exists a small set $G$ of objects of $C$ such that every object
    of $C$ is the target of a covering family in $C'$ of morphisms whose
    sources lie in $G$.

2. The topology induced by the topology of $C'$ is a $U$-topology (I 3.0.2), and the functor $u$ is continuous and
   cocontinuous for this topology.

**Proof.** This follows immediately from 3.3 and 2.1.

[PDF p. 301]

**Proposition 3.5.** Let $C$ be a $U$-site and let $\varepsilon_C : C \to \widetilde{C}$ be the canonical functor (II
4.4.0). Equip $\widetilde{C}$ with the canonical topology. Then the topology of the site $C$ is the topology induced by
the topology of $\widetilde{C}$.

**Proof.** The covering families of $\widetilde{C}$ for the canonical topology are the universally effective epimorphic
families (II 2.5), that is (II 4.3), the epimorphic families. Let $T$ be the topology of the site $C$ and
$\mathcal{T}_U$ the finest topology among the topologies $T'$ on $C$ such that, for every sheaf $F$ on $\widetilde{C}$,
$F \circ \varepsilon_C$ is a sheaf for $T'$. It suffices to show that $T = \mathcal{T}_U$, because then $\mathcal{T}_U$
is a $U$-topology and consequently $\mathcal{T}_U$ is the induced topology.

**A. The topology $T$ is finer than $\mathcal{T}_U$.** Let $(X_i \to X)_{i \in I}$ be a covering family of
$\mathcal{T}_U$. Then, for every sheaf $F$ on $\widetilde{C}$,

$$ F(\varepsilon_C(X)) \to \prod_i F(\varepsilon_C(X_i)) $$

is injective. Consequently (II 5.2), $(\varepsilon_C(X_i) \to \varepsilon_C(X))_{i \in I}$ is covering for the canonical
topology of $\widetilde{C}$, hence (II 5.2) $(X_i \to X)_{i \in I}$ is covering for $T$.

**B. The topology $T$ is less fine than $\mathcal{T}_U$.** It suffices to show that $\varepsilon_C : C \to
\widetilde{C}$ is continuous (1.1). But it will be proved in IV no. 1 that every sheaf on $\widetilde{C}$ is
representable. Consequently, for every sheaf $F$ on $\widetilde{C}$, $F \circ \varepsilon_C$ is a sheaf on $C$. We shall
not use 3.5 until IV 1.

Let us note two results that will be used in VI 7.

**Proposition 3.6.** Let $(C_i)_{i \in I}$ be a family of sites, $C$ a category, and, for every $i \in I$, a functor
$u_i : C_i \to C$. Let $U$ be a universe such that the categories $C_i$ and $C$ are $U$-small. There exists a topology
$\mathcal{T}_U$ on $C$ which is the least fine of the topologies for which the $u_i$ are continuous. The topology
$\mathcal{T}_U$ does not depend on the universe $U$ for which the categories considered are small.

The last assertion of 3.6 follows from 1.5. Let $T$ be a topology on $C$. Then the functors $u_i$ are continuous if and
only if, for every $i \in I$ and every sieve covering $R \to X$ of an object $X$ of

[PDF p. 302]

$C_i$, the morphism

$$ u_{i!}(R) \to u_i(X) $$

of $\widehat{C}$ is bicovering (1.2 ii). Thus 3.6 is a consequence of Lemma 3.6.1.

**Lemma 3.6.1.** Let $C$ be a small category and let $(u_i : F_i \to G_i)_{i \in I}$ be a family of arrows of
$\widehat{C}$. Then there exists on $C$ a topology least fine among those that make the morphisms $u_i$ covering,
respectively bicovering (II 5.2).

To say that $u : F \to G$ is covering for a given topology $T$ means that, for every arrow $X \to G$, with $X \in
\operatorname{Ob} C$, the corresponding arrow $F \times_G X \to X$ is covering, or equivalently that the family of
arrows $X' \to X$ of $C$ that factor through the preceding arrow is covering. The fact that there exists a least fine
topology among those for which the $u_i : F_i \to G_i$ are covering therefore follows from I 1.1.6; whence the covering
assertion of 3.6.1.

The bicovering assertion is deduced from it by remembering that a morphism $u : F \to G$ is bicovering if and only if
the morphisms $u : F \to G$ and $\operatorname{diag}_u : F \to F \times_G F$ are covering.

**Proposition 3.7.** Let $(C_i)_{i \in I}$ be a family of sites, $C$ a category, and, for every $i \in I$, a functor
$u_i : C_i \to C$. Let $U$ be a universe such that the categories $C_i$ and $C$ are $U$-small. There exists a topology
$\mathcal{T}_U$ which is the finest for which the $u_i$ are cocontinuous. The topology $\mathcal{T}_U$ does not depend
on the universe $U$ for which the categories considered are small.

Let $U$ be a universe for which the categories considered are small. The functors $u_i$ are cocontinuous for a topology
$\mathcal{T}$ of $C$ if and only if, for every $i \in I$ and every sheaf $F$ on $C_i$, the presheaf $u_{i*}F$ is a sheaf
for $\mathcal{T}$ (2.2). It follows that the topology $\mathcal{T}_U$ is the finest topology for which the presheaves
$u_{i*}F$, $i \in I$, $F \in \operatorname{Ob}\widetilde{C_i}$, are sheaves (II 2.2). The last assertion follows from
2.2.

[PDF p. 303]

## 4. Comparison Lemma

**Theorem 4.1 (comparison lemma).** Let $C$ be a small category, let $C'$ be a site whose underlying category is a
$U$-category, and let $u : C \to C'$ be a fully faithful functor. Equip $C$ with the topology induced by $u$ (3.1).
Consider the properties:

1. Every object of $C'$ can be covered by objects coming from $C$.
2. The functor $F \mapsto F \circ u$ induces an equivalence of categories from the category of sheaves on $C'$ to the
   category of sheaves on $C$.

One always has $i) \Rightarrow ii)$. When $C'$ is a $U$-site and when the topology of $C'$ is less fine than the
canonical topology, one has $ii) \Rightarrow i)$.

**4.1.1.** We first prove $i) \Rightarrow ii)$. The proof proceeds in two steps.

**First step.** For every presheaf $H$ of $\widehat{C'}$, the adjunction morphism

$$ \varphi : u_!u^*H \to H $$

(I 5.1) is bicovering (II 5.3), and the functor $u_s : \widetilde{C'} \to \widetilde{C}$ (1.1.1) is fully faithful.

Let $C/H$ be the small category whose objects are the objects $Y$ of $C$ equipped with a morphism $u(Y) \to H$, and
whose morphisms are the commutative diagrams

```text
u(Y) --u(m)--> u(Y')
  \             /
   \           /
        H
```

We have

$$ u^*H = \operatorname{colim}_{Y \in \operatorname{Ob}(C/H)} Y $$

(I 3.4), and consequently (I 5.4)

$$ u_!u^*H = \operatorname{colim}_{Y \in \operatorname{Ob}(C/H)} u(Y). $$

The adjunction morphism is the evident morphism resulting from the description of $u_!u^*H$ as an inductive limit. The
morphism $\varphi$ has the

[PDF p. 304]

following property:

`(*)` For every object $Y$ of $C$, every morphism $m : u(Y) \to H$ factors uniquely as the canonical morphism
$\alpha(m) : u(Y) \to u_!u^*H$ followed by the morphism $\varphi$.

It follows immediately from i) that the morphism $\varphi$ is covering (II 5.1). We show that it is bicovering. Let
$p,q : Z \to u_!u^*H$ be two morphisms from an object $Z$ of $C'$ such that $\varphi p = \varphi q$. For every object
$Y$ of $C$ and every morphism $n : u(Y) \to Z$, we have $\varphi pn = \varphi qn$. Property `(*)` then implies that
$pn = qn$, and since the $u(Y)$ cover $Z$, the kernel of $(p,q)$ is a sieve covering $Z$. The morphism $\varphi$ is
therefore bicovering (II 5.3).

For every sheaf $H$ on $C'$, $u^*H$ is a sheaf on $C$, denoted $u_sH$ (1.1.1). Moreover $u^s u_s H = a' u_!u_sH$ (1.3),
and the adjunction morphism $u^s u_s H \to H$ is obtained by applying the "associated sheaf" functor to the morphism
$\varphi : u_!u^*H \to H$. Consequently (II 5.3), the adjunction morphism $u^s u_s H \to H$ is an isomorphism. Thus
$u_s : \widetilde{C'} \to \widetilde{C}$ is fully faithful.

**Second step.** The functor $u$ is cocontinuous and the functor $u^s : \widetilde{C} \to \widetilde{C'}$ (1.2) is fully
faithful. Consequently $u_s : \widetilde{C'} \to \widetilde{C}$ is an equivalence.

Let $Y$ be an object of $C$ and $i : R \to u(Y)$ a covering sieve. Since the functor $u^*$ commutes with projective
limits (I 5.5), the morphism $u^*(i) : u^*(R) \to u^*u(Y)$ is a monomorphism. Since $u$ is fully faithful, we have
$u^*u(Y) \simeq Y$, whence a sieve of $Y$, $u^*(i) : u^*(R) \to Y$. To show that $u$ is cocontinuous, it suffices to
show that $u^*(i) : u^*(R) \to Y$ is a sieve covering for the induced topology on $C$ (2.1). For this, it suffices to
show (3.2) that, for every base change $m : X \to Y$, the morphism

$$ u_!(u^*(R) \times_Y X) \to u(X) $$

is bicovering. But since $u^*$ commutes

[PDF p. 305]

with projective limits, we have

$$ u^*(R) \times_Y X = u^*(R \times_{u(Y)} u(X)), $$

and $R \times_{u(Y)} u(X)$ is a sieve covering $u(X)$. It therefore suffices to show that, for every object $Y$ of $C$
and every covering sieve $i : R \to u(Y)$, the morphism of $\widehat{C'}$

$$ u_!u^*(R) \to u(Y) $$

is bicovering. But this morphism factors as the adjunction morphism $u_!u^*(R) \to R$, which is bicovering by the first
step, followed by the monomorphism $R \to u(Y)$, which is covering. It is therefore bicovering (II 5.3). This shows that
$u$ is cocontinuous.

Since $u$ is continuous and fully faithful, it follows from 2.6, used in the case where $C$ is small, that $u^s$
(denoted $u_!$ in 2.6) is fully faithful. Since $u^s$ and $u_s$ are adjoint to one another and are fully faithful, they
are quasi-inverse functors, and consequently $u_s$ is an equivalence.

**4.1.2.** We now prove $ii) \Rightarrow i)$. The objects $Y$ of $C$ form a generating family of $\widetilde{C}$ (II
4.10). Consequently, for every object $X$ of $C'$, there exists an epimorphic family in $\widetilde{C}$, $v_i : Y_i \to
u_sX$, $i \in I$. We have $u_su(Y_i) = Y_i$, and, since the functor $u_s$ is an equivalence of categories, we have $v_i
= u_s(w_i)$, where the $w_i : u(Y_i) \to X$ form an epimorphic family of $\widetilde{C'}$. It then follows from II 5.1
that the family $w_i : u(Y_i) \to X$, $i \in I$, is covering.

**4.2. End of the proof of 1.2.** Let $G$ be a full subcategory of $C$ whose objects form a small topologically
generating family of $C$ (II 3.0.1). Equip $G$ with the topology induced by the inclusion functor $i : G \to C$. The
functor $(u \circ i)_s = i_s \circ u_s$ (1.1.1) admits a left adjoint by the first part of the proof of 1.2. Since $i_s$
is an equivalence

[PDF p. 306]

of categories (4.1), the functor $u_s$ admits a left adjoint $u^s$, and one has a functorial isomorphism

$$ u^s \simeq (u \circ i)^s \circ i_s. $$

We show that the diagram

```text
C  --u-->   C'
|          |
epsilon_C        epsilon_C'
v          v
C~ --u^s-> C'~
```

is commutative up to isomorphism. For every sheaf $H$ on $C'$, one has

$$ \operatorname{Hom}_{\widetilde{C'}}(\varepsilon_{C'}uX,H) \simeq u_sH(X) $$

for every $X \in \operatorname{Ob} C$. Moreover one has

$$ \operatorname{Hom}_{\widetilde{C'}}(u^s \varepsilon_C X,H) \simeq \operatorname{Hom}_{\widetilde{C}}(\varepsilon_C
X,u_sH) $$

by adjunction, and then

$$ \operatorname{Hom}_{\widetilde{C}}(\varepsilon_C X,u_sH) \simeq u_sH(X) $$

by definition of $\varepsilon_C$. Hence an isomorphism

$$ \varepsilon_{C'}uX \simeq u^s \varepsilon_C X $$

for every $X \in \operatorname{Ob} C$. This proves $i) \Rightarrow iv)$.

We show that $iv) \Rightarrow i)$. We have a commutative diagram

```text
G --i--> C --u--> C'
|        |        |
epsilon_G      epsilon_C      epsilon_C'
v        v        v
G~--i^s->C~--u^s->C'~
```

and consequently, by the first part of the proof, the functor $u \circ i : G \to C'$ is continuous. It follows at once
from 4.1 and 1.1 that $u$ is continuous, whence $iv) \Rightarrow i)$. One moreover obtains the uniqueness of $u^s$,
knowing, by the first part of the proof, the uniqueness when $C$ is small.

[PDF p. 307]

**4.3. End of the proof of 1.5 and 1.7.** Let $u : C \to C'$ be a functor between two $U$-sites and let $G$ be a full
subcategory of $C$ whose set of objects is a small topologically generating family of $C$ (II 3.0.1). Equip $G$ with the
topology induced by the inclusion functor $i : G \to C$. It follows immediately from 4.1 and 1.1 that $u$ is continuous
if and only if $u \circ i$ is continuous. From this remark and from the first part of the proof of 1.5, the general case
follows. This remark also makes it possible to reduce the proof of 1.7 to the case where the category $C$ is small.

**4.4. End of the proof of 2.3.** Let $u : C \to C'$ be a functor between two $U$-sites, and let $G$ be a full
subcategory of $C$ whose set of objects is a small topologically generating family of $C$ (II 3.0.1), equipped with the
topology induced by the inclusion functor $i : G \to C$. It follows from the proof of 4.1 (4.1.1, second step) that $i$
is cocontinuous.

Consequently, when $u$ is cocontinuous, the functor $u \circ i : G \to C'$ is cocontinuous. Moreover, $i^* :
\widetilde{C} \to \widetilde{G}$ is an equivalence of categories (4.1). Thus the functor $u^* : \widetilde{C'} \to
\widetilde{C}$ admits a right adjoint. This proves 3). To prove 4), it suffices to observe that $(u \circ i)_* \simeq
u_* \circ i_*$ and that $i_*$ is an equivalence (4.1). The commutativity of (2.3.2) then follows from the commutativity
of these diagrams when $C$ is small.

[PDF p. 308]

## 5. Localization

**5.1.** Let now $C$ be a $U$-site and let $X$ be an object of $\widehat{C}$. Unless expressly stated otherwise, the
category $C/X$ will be equipped with the topology $\mathcal{T}$ induced by the functor $j_X : C/X \to C$ (3.1). The
notation $C/X$ will denote the category $C/X$ equipped with the topology $\mathcal{T}$.

Proposition I 5.11 shows that the functor $j_X$ commutes with fiber products and consequently transforms every
monomorphism into a monomorphism. In particular, for every object $(Y \to X)$ of $C/X$, the functor $j_X$ establishes a
one-to-one correspondence between the sieves, in the category $C/X$, of the object $(Y \to X)$ and the sieves, in $C$,
of the object $Y$.

**Proposition 5.2.** Let $C$ be a $U$-site, let $X$ be an object of $\widehat{C}$, and let $j_X : C/X \to C$ be the
corresponding continuous functor.

1. A sieve $R$ of an object $(Z \to X)$ is covering in $C/X$ if and only if the sieve $j_X(R) \to Z$ is covering in $C$.
2. The functor $j_X : C/X \to C$ is cocontinuous and continuous.
3. Let $m : Y \to X$ be a morphism of $\widehat{C}$. We then have the commutative diagram

    ```text
    C/Y --j_m--> C/X
     \           /
    j_Y        j_X
       \       /
           C
    ```

    The topology induced by the functor $j_Y$ on $C/Y$ is equal to the topology induced by $j_m$ on $C/Y$.

4. The topology induced by $j_X : C/X \to C$ is a $U$-topology (II 3.0.2).

[PDF p. 309]

**Proof.**

1. If the sieve $R$ of $(Z \to X)$ is covering, the sieve $j_X(R) \to Z$ is covering (1.6). Conversely, if the sieve
   $j_X(R) \to Z$ is covering in $C$, one sees that the same is true for every sieve obtained by making a base change in
   $C/X$. The sieve $R$ is therefore covering (3.2).
2. This is deduced immediately from 1) by applying 2.1.
3. This is deduced immediately from the description of covering sieves given by 1).
4. Let $(G_i)_{i \in I}$ be a small topologically generating family of $C$. One verifies immediately that the small
   family $(u : G_i \to X)$, where $u \in \bigcup_{i \in I}\operatorname{Hom}_{\widehat{C}}(G_i,X)$, is topologically
   generating in $C/X$.

**Terminology and Notation 5.3.** By the preceding proposition, the functor $j_X$ is both continuous and cocontinuous.
It therefore defines a sequence of three adjoint functors (4.3.2) between the categories of sheaves of sets (1.3 and
2.3):

$$ j_X^s : \widetilde{(C/X)} \to \widetilde{C} $$

$$ j_X^* = j_{X,s} : \widetilde{C} \to \widetilde{(C/X)} $$

$$ j_{X*} : \widetilde{(C/X)} \to \widetilde{C} $$

In the particular situation of Proposition 5.2, we shall use the following terminology and notation:

1. The functor $j_{X*}$ will be called the direct image functor.
2. The functor $j_X^* = j_{X,s}$ will be denoted $j_X^*$ and will be called the restriction functor to $C/X$.

[PDF p. 310]

3. The functor $j_X^s$ on sheaves of sets will be called the extension by the empty object functor to the category
   $\widetilde{C}$, and will be denoted $j_{X!}$ (cf. 2.9.2).

We therefore have a sequence of three adjoint functors between $\widetilde{(C/X)}$ and $\widetilde{C}$:

$$ j_{X!},\qquad j_X^*,\qquad j_{X*}. $$

**Proposition 5.4.** The functor $j_{X!} : \widetilde{(C/X)} \to \widetilde{C}$ factors through the category
$\widetilde{C}/aX$, where $a$ is the "associated sheaf" functor:

```text
(C/X)~ --e_X~--> C~/aX --> C~
```

The functor

$$ \widetilde{e_X} : \widetilde{(C/X)} \to \widetilde{C}/aX $$

is an equivalence of categories. The restriction functor to $C/X$, composed with the equivalence $\widetilde{e_X}$, is
isomorphic to the "base change by $aX \to e$" functor, where $e$ is the final object of $\widetilde{C}$:

$$ F \mapsto (F \times aX \to aX). $$

**Proof.** The image by $j_{X!}$ of the final object of $\widetilde{(C/X)}$ is the object $aX$; hence the factorization.
To show that the functor $\widetilde{e_X}$ is an equivalence, we shall confine ourselves to a few indications. By I
5.11, a presheaf on $C/X$ is defined by a presheaf $F$ on $C$ equipped with a morphism $F \to X$. One then proves that
the following two properties are equivalent:

1. The presheaf on $C/X$ defined by $F \to X$ is a sheaf.

2. The following diagram is cartesian, where $i$ denotes the injection into presheaves and $a$ the associated sheaf
   functor:

    ```text
    F -> iaF
    |    |
    v    v
    X -> iaX
    ```

[PDF p. 311]

One then immediately deduces that $\widetilde{e_X}$ is an equivalence. The last assertion is trivial.

**Proposition 5.5.**

1. Let $C$ be a $U$-site and let $X$ be an object of $\widehat{C}$. The diagram below of categories and functors is
   commutative up to canonical isomorphisms:

    ```text
    Diagram (5.5.1) of the scan: comparison between the categories of
    presheaves/sheaves on C/X and the categories of arrows over X,
    aX, and iaX. The horizontal arrows are h_X, a_X, i_X above,
    then h/X, a/X, i/aX, and pi below; the vertical arrows include
    e_X~ and e~/X.
    ```

    The notation $a_X$ and $i_X$ denotes the "associated sheaf" and "injection into presheaves" functors for the site
    $C/X$. The notation $a/X$ denotes the natural extension of the functor $a$, associated sheaf for the site $C$, to
    the category of arrows with target $X$; similarly for the notation $i/aX$. Finally, the notation $\pi$ denotes the
    base-change functor by the canonical arrow $X \to iaX$.

2. Let moreover $m : Y \to X$ be a morphism of $\widehat{C}$. The diagram below is commutative up to canonical
   isomorphism:

    ```text
    Diagram (5.5.2) of the scan: comparison between C~/aX/aY,
    (C/X)~/a_XY, (C/X/Y)~, C~/aY, and (C/Y)~, with the arrows
    f, g, e_Y~, and e_m~.
    ```

[PDF p. 312]

The arrow $f$ is the natural extension of the equivalence $\widetilde{e}/X$ to the category of arrows with target
$a_XY$, and is therefore an equivalence of categories. The arrow $g$ is none other than the equivalence of 5.4 applied
to the situation $(C/X)/[m]$.

3. Denote by $j_{aX!} : \widetilde{C}/aX \to \widetilde{C}$ the "forget $aX$" functor, and by $j^*_{aX} : \widetilde{C}
   \to \widetilde{C}/aX$ the "product with $aX$" functor. The diagrams below are commutative up to canonical
   isomorphism:

    ```text
    Diagrams (5.5.3) of the scan: compatibility of j_{X!}, j^*_X,
    j_{aX!}, j^*_{aX}, e_X~, and e~/X.
    ```

**Proof.** The proof of these assertions is immediate from the definition of the equivalences $\widetilde{e_X}$ (5.4)
and $\widehat{e_X}$ (I 5.11).

## Bibliography

**[TF]** R. Godement, *Theorie des faisceaux*, Hermann, 1958, Act. Scient. Ind. no. 1252, Paris.

[^induced]: When no confusion results, this topology is called the topology induced on $C$ by the topology of $C'$.

[^fibers]: In fact, it suffices that $u$ commute with fiber products of the form $X_i \times_X X'$.
