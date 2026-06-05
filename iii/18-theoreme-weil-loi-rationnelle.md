# Exposé XVIII. Weil's theorem on the construction of a group from a rational law

<!-- label: III.XVIII -->

*by Michael Artin*

## 0. Introduction

<!-- label: III.XVIII.0 -->

<!-- original page 632 -->

This Exposé is devoted to the well-known theorem of Weil [1] which gives the construction of a group variety from a
birational law. It seems that the generalization of this result to the case where the base is the spectrum of a discrete
valuation ring was already known to several people; one may consult, for example, [2]. Here we shall prove the theorem
for a flat group of finite presentation over an arbitrary base prescheme $S$. Since the hypotheses must be made with
somewhat more care, the statement is not in the form given by Weil; but when $S$ is the spectrum of a field, one sees
that the form given here is essentially equivalent to Weil's. We use the following suggestion of Grothendieck: given a
"group germ" $X$ over a prescheme $S$, one is to construct the group as the quotient of $X \times_{S} X$ by a suitable
equivalence relation.

## 1. "Recollections" on rational maps

<!-- label: III.XVIII.1 -->

<!-- original page 633 -->

Let $X/S$ be a relative prescheme and $U \subseteq X$ an open subset. We say that $U$ is *schematically dense in $X$
relatively to $S$*, or that $U \hookrightarrow X$ is *relatively schematically dense*, if for every base change $S' \to
S$ the open subset $U \times_{S} S'$ is schematically dense in $X \times_{S} S'$. For the definition and properties of
this notion we refer to Exp. IX, § 4.[^XVIII-1-1]

**Proposition 1.1.** *(i) A finite intersection, as well as a union of a non-empty family of opens that are
schematically dense relatively to $S$, is schematically dense relatively to $S$.*

<!-- label: III.XVIII.1.1 -->

*(ii) If $U \subseteq X$ is schematically dense relatively to $S$ and if $S \to T$ is a morphism, then $U_{T} \subseteq
X_{T}$ is schematically dense relatively to $T$.*

*(iii) Let $U \subseteq V \subseteq X$ be open immersions. For $U$ to be schematically dense in $X$ relatively to $S$,
it is necessary and sufficient that it be so in $V$ and that $V$ be so in $X$.*

*(iv) If $U \subseteq X$ and $V \subseteq Y$ are relatively schematically dense, then $U \times_{S} V$ is schematically
dense in $X \times_{S} Y$ relatively to $S$.*

In Exp. IX one finds the following criterion:

**Proposition 1.2.** *Let $X/S$ be locally of finite presentation and flat, and let $U$ be an open subset of $X$. If for
each $s \in S$ the fiber $U_{s}$ is schematically dense in $X_{s}$, then $U$ is schematically dense in $X$ relatively to
$S$.*

<!-- label: III.XVIII.1.2 -->

In particular:

**Corollary 1.3.** *If $X/S$ is locally of finite presentation and flat, and if each fiber $X_{s}$ is "without embedded
component", then $U$ is schematically dense in $X$ relatively to $S$ if and only if for each $s \in S$, $U_{s}$ is dense
in $X_{s}$ in the topological sense.*

<!-- label: III.XVIII.1.3 -->

<!-- original page 634 -->

One easily deduces from the definition the following:

**Proposition 1.4.** *Let $U \subseteq X$ be schematically dense relatively to $S$, and let $f, g : X \to Y$ be two
morphisms of functors over $S$, where $Y$ satisfies one of the following conditions:*

<!-- label: III.XVIII.1.4 -->

*(i) $Y$ is a prescheme over $S$ and each fiber $Y_{s}$ is separated.*

*(ii) $Y$ is a presheaf[^N.D.E-XVIII-1] on $S$ such that the diagonal morphism $Y \to Y \times_{S} Y$ is representable
by a closed immersion.[^N.D.E-XVIII-2]*

*Then if $f = g$ on $U$, one has $f = g$.*

*Proof.* In case (i), the standard argument following IX 4.1 shows that $f$ and $g$ are equal on each fiber, so that the
subprescheme $Ker(f, g)$ of $X$ is set-theoretically equal to $X$, hence closed; and since it majorizes $U$, it is equal
to $X$, i.e. $f = g$. Case (ii) is proved as in *loc. cit.*[^N.D.E-XVIII-3]

**Definition 1.5.**[^XVIII-1-2] *Let $X$ be a prescheme over $S$ and $Y$ a presheaf over $S$. By a* rational map $f : X
\dashrightarrow Y$ over $S$ *we mean an equivalence class of morphisms $f : U \to Y$ over $S$, where $U$ is an open of
$X$ that is schematically dense relatively to $S$, and where one sets $(f : U \to Y) \sim (f' : U' \to Y)$ if and only
if there exists an open $U'' \subseteq U' \cap U$, schematically dense relatively to $S$, such that $f = f'$ on `U''`.*

<!-- label: III.XVIII.1.5 -->

This definition is made in such a way that one may define in the obvious way the rational map $f \times_{S} S'$ for any
base change $S' \to S$.

If $U$ is an open of $X$, we say that the rational map $f$ is *defined on $U$* if there exists a morphism representing
$f$ whose set of definition contains $U$.

**Definition 1.5.1.**[^N.D.E-XVIII-4] *If $Y$ satisfies one of the conditions (i), (ii) of 1.4, it is clear that there
exists a largest open $U$ of $X$ on which $f$ is defined, and this $U$ is schematically dense relatively to $S$. It is
called the* domain of definition of $f$ over $S$, *and is denoted $Dom(f)$.*

<!-- label: III.XVIII.1.5.1 -->

This notion does not commute with base change in general, but one has:

**Proposition 1.6.** *Let $X$ be an $S$-prescheme and $Y$ an $S$-functor satisfying one of the hypotheses (i), (ii) of
1.4. Let $f : X \dashrightarrow Y$ be a rational map over $S$, let $S' \to S$ be a flat morphism locally of finite
presentation, and set $f' = f \times_{S} S'$. Then*

<!-- label: III.XVIII.1.6 -->

<!-- original page 635 -->

```text
Dom(f') = Dom(f) ×_S S'.
```

*Proof.* Set $U = Dom(f)$. It is clear that $V' = Dom(f')$ contains $U \times_{S} S'$. Let $V$ be the image of $V'$,
which is an open of $X$ because $X' \to X$ is open. We must show that $V = U$, that is, we must find a morphism $V \to
Y$ that represents $f$. Set $S'' = S' \times_{S} S'$, and

```text
X'' = X ×_S S'',   U'' = U ×_S S'',   V'' = V' ×_V V'.
```

Then `U''` is schematically dense in `X''` relatively to `S''`, hence `U''` is schematically dense in `V''` relatively
to $S$, since $U'' \subseteq V'' \subseteq X''$. The restriction of $f' : V' \to Y'$ to $U'$ is deduced from $f : U \to
Y$ by base change. The two morphisms $V'' \to Y$ deduced from $g$ by base change are equal on `U''`, hence are equal.
Now since $V' \to V$ is flat and locally of finite presentation, it is fppf-covering (Exp. IV 6.3), and one finds the
morphism $V \to Y$ by descent.

We shall make frequent use of the following triviality:

**Proposition 1.7.** *Let $X/S$ be faithfully flat, locally of finite presentation, and let $U \subseteq X$ be a
relatively schematically dense open. Then there exists a base change $S' \to S$ which is fppf-covering, and a section $x
\in X(S')$ which is contained in $U(S')$.*

<!-- label: III.XVIII.1.7 -->

Indeed, $U/S$ is fppf-covering. One takes $S' = U$ and the $S$-graph of the inclusion of $U$ in $X$ as the section.

## 2. Local determination of a group morphism

<!-- label: III.XVIII.2 -->

<!-- original page 636 (preceding) -->

Let $G$ and $H$ be groups and let $U \subseteq G$ be a subset such that $U \cdot U = G$. Then if $f$ and $g$ are
homomorphisms from $G$ to $H$ such that $f = g$ on $U$, one has $f = g$. Similarly:

**Proposition 2.1.** *Let $S$ be a site (cf. Exp. IV[^N.D.E-XVIII-5]), $G$ a sheaf of groups on $S$, and $U \subseteq G$
a subsheaf of sets such that the morphism $U \times U \to G$ induced by multiplication is an epimorphism. Then if $f$
and $g$ are homomorphisms from $G$ to a sheaf of groups $H$ that are equal on $U$, one has $f = g$.*

<!-- label: III.XVIII.2.1 -->

<!-- original page 636 -->

**Corollary 2.2.** *Let $G$ be an $S$-group prescheme locally of finite presentation and flat, let $U \subseteq G$ be an
open that is relatively schematically dense, and let $H$ be a sheaf of groups on $S$ for the fppf topology. Then every
homomorphism $f : G \to H$ is determined by its restriction to $U$.*

<!-- label: III.XVIII.2.2 -->

Indeed, since $G$ is flat over $S$, the composition law on $G$ is a flat morphism (VI_B.9.2.xi), and it follows that $U
\times_{S} U \to G$ is faithfully flat and locally of finite presentation, hence fppf-covering, hence an epimorphism.

**Proposition 2.3.** *Let $G$ be a group prescheme locally of finite presentation and flat over $S$, $U \subseteq G$ a
relatively schematically dense open, and $H$ a sheaf of groups for the fppf topology. Write $m_{G}$ for the
multiplication of $G$ and $m_{H}$ for that of $H$.*

<!-- label: III.XVIII.2.3 -->

*Let $f : U \to H$ be an $S$-morphism and assume that there exists a relatively schematically dense open $V$ of
$m^{-1}_{G}(U) \cap U \times_{S} U$ such that the diagram*

```text
            (f × f)|V
       V ───────────────→ H ×_S H
       │                     │
  m_G  │                     │ m_H
       ▼          f          ▼
       U ───────────────────→ H
```

*is commutative. Then there exists a morphism of $S$-groups $\bar{f} : G \to H$ (necessarily unique) extending $f$, in
each of the following situations:*

*(i) $H$ is representable.*

*(ii) The diagonal morphism $H \to H \times_{S} H$ is representable by a closed immersion.[^N.D.E-XVIII-6]*

*(iii) For each section $a \in U(S)$, the open $pr_{2}((a \times_{S} U) \cap V)$ is relatively schematically dense in
$U$[^XVIII-2-1], and this statement remains true after every base change $S' \to S$.*

*Proof.* Note first that $V$ is relatively schematically dense in $G \times_{S} G$. Indeed, $V$ is relatively
schematically dense in

```text
m_G⁻¹(U) ∩ (U ×_S G) ∩ (G ×_S U),
```

and the three factors are deduced from $U \subseteq G$ by an obvious base change $G \times_{S} G \to G$, which implies
the assertion by 1.1.

To construct a morphism $\bar{f} : G \to H$, it suffices, since $U \times_{S} U \to G$ is fppf-covering, to find a
morphism from $U \times_{S} U$ to $H$ such that the two morphisms induced on $(U \times_{S} U) \times_{G} (U \times_{S}
U)$ are the same.

<!-- original page 637 -->

We take $m_{H} \circ (f \times f) : U \times_{S} U \to H$. We must verify that whenever we have sections $a, b, c, d \in
U(S')$, $S' \to S$ arbitrary, such that $ab = cd$, we also have $f(a)f(b) = f(c)f(d)$. By hypothesis, this is true if
$(a, b)$ and $(c, d)$ are contained in $V(S')$, since in that case $f(a)f(b) = f(ab)$ and $f(c)f(d) = f(cd)$. Therefore
it is true whenever $(a, b, c, d) \in (V \times_{G} V)(S')$.

I claim that $V \times_{G} V$ is an open of $(U \times_{S} U) \times_{G} (U \times_{S} U)$ schematically dense
relatively to $S$. This will complete the proof in cases (i) and (ii) by 1.4, the facts that the morphism $\bar{f}$ so
constructed extends $f$ and that $\bar{f}$ is a homomorphism being evident, again by 1.4.

Indeed, we write

```text
V ×_G V = (V ×_G (G ×_S G)) ∩ ((G ×_S G) ×_G V).
```

By symmetry and 1.1, it suffices to verify that $V \times_{G} (G \times_{S} G)$ is relatively schematically dense in $(G
\times_{S} G) \times_{G} (G \times_{S} G)$. But this last prescheme is $S$-isomorphic to $G \times_{S} G \times_{S} G$,
the morphism being given by $(a, b, c, d) \mapsto (a, b, c)$. Thus what must be shown is that $V \times_{S} G$ is
schematically dense in $G \times_{S} G \times_{S} G$ relatively to $S$, which is a consequence of the fact that $V$ is
relatively schematically dense in $G \times_{S} G$.

It remains to treat case (iii). To prove $f(a)f(b) = f(c)f(d)$, it is permitted to make an fppf-covering base change.
Suppose we have a section $x \in G(S')$, $S' \to S$ fppf-covering, such that $(b, x)$, `(a, bx)`, $(d, x)$, `(c, dx)`
are all in $V$. Then one will have

```text
f(a)f(b)f(x) = f(a)f(bx) = f(abx) = f(cdx) = f(c)f(dx) = f(c)f(d)f(x),
```

whence the desired equality.

[^N.D.E-XVIII-7] To find such an $x$, set, for every $z \in U(S')$,

```text
V_z = pr₂((z ×_{S'} U_{S'}) ∩ V_{S'}).
```

Then the hypotheses on $x$ say that $x \in W$, where

```text
W = V_b(S') ∩ V_d(S') ∩ b⁻¹ V_a(S') ∩ d⁻¹ V_c(S').
```

By (iii), $W$ is relatively schematically dense in $G$. Hence the existence of a section $x$ after an fppf-covering
extension follows from Proposition 1.7.

<!-- original page 638 -->

Let us verify that the morphism so constructed is multiplicative. Let $a, b \in G(S')$, $S' \to S$ arbitrary, and write
$S_{0} = S$. Choose an fppf-covering base change $S' \to S$ and a section $x \in G(S')$ such that $x \in U(S')$ and
$ax^{-1} \in U(S')$, that is, $x \in (a^{-1}U)^{-1}(S')$. Choose moreover another fppf-covering extension $S'' \to S'$
and a section $y \in G(S'')$ such that

```text
y, by⁻¹, aby⁻¹    belong to U(S''),
```

and

```text
by⁻¹ ∈ V_x,   xby⁻¹ ∈ V_{ax⁻¹}.
```

Then by the definition of $\bar{f}$, one has on `S''`

```text
f̄(a) = f(ax⁻¹)f(x),   f̄(b) = f(by⁻¹)f(y),   f̄(ab) = f(aby⁻¹)f(y).
```

Moreover,

$$ \bar{f}(a)\bar{f}(b) = f(ax^{-1})f(x)f(by^{-1})f(y) = f(ax^{-1})f(xby^{-1})f(y) = f(aby^{-1})f(y) = \bar{f}(ab), $$

whence multiplicativity.

The fact that $\bar{f}$ extends $f$ is now easy. Let $a \in U(S')$, write $S_{0} = S$, and choose $S' \to S$
fppf-covering and sections $x, y \in G(S')$ such that $(x, y)$, `(ax, y)`, `(a, xy)` are in $V(S')$. Then

```text
f̄(xy) = f(x)f(y) = f(xy),    f̄(axy) = f(ax)f(y) = f(axy).
```

Hence

```text
f̄(a) = f̄(axy)f̄((xy)⁻¹) = f̄(axy)f̄(xy)⁻¹ = f(axy)f(xy)⁻¹ = f(a).
```

**Remark 2.3.1.** *In many cases hypothesis (iii) is true, for it will even be true if one replaces $U$ by a smaller
open $U^{0}$, still relatively schematically dense in $G$. For example one has:*

<!-- label: III.XVIII.2.3.1 -->

**Proposition 2.4.** *The situation being as in 2.3, suppose that each geometric fiber of $G/S$ is irreducible. Let
$U^{0} = pr_{1} V$ and*

<!-- label: III.XVIII.2.4 -->

```text
V⁰ = V ∩ m_G⁻¹(U⁰) ∩ (U⁰ ×_S U⁰).
```

*Then $U^{0} \subseteq U$ is an open relatively schematically dense of $G$ and the objects $U^{0}$, $f|U^{0}$ and
$V^{0}$ satisfy hypothesis (iii).*

*Proof.* $U^{0}$ is open because $G \times_{S} G \to G$ is flat and locally of finite presentation. All the other
verifications are trivial save hypothesis (iii).

Let $a \in U(S')$, write $S_{0} = S$. To verify that $pr_{2}((a \times_{S} U^{0}) \cap V^{0})$ is relatively
schematically dense in $U^{0}$, it suffices to do so fiber by fiber by Corollary 1.3, that is, it suffices to treat the
case where $S$ is the spectrum of a field, and in that case it suffices to show that $U^{0}$ is non-empty, because $G$
is irreducible and "without embedded components" (cf. VI_A, 1.1.1). Now

```text
pr₂((a ×_S U⁰) ∩ V⁰) = pr₂((a ×_S U⁰) ∩ V) ∩ pr₂((a ×_S U⁰) ∩ m_G⁻¹(U⁰))
```

and the second term of the right-hand side is dense in $G$. Hence it suffices to show that $pr_{2}((a \times_{S} U^{0})
\cap V)$ is dense in $G$, that is, non-empty, which is clear because $a \in U^{0} = pr_{1} V$.

## 3. Construction of a group from a rational law

<!-- label: III.XVIII.3 -->

<!-- original page 639 -->

### 3.0.

<!-- label: III.XVIII.3.0 -->

We are given a prescheme $X/S$ and a rational map $X \times_{S} X \dashrightarrow X$ over $S$, and we seek a group $G/S$
and a birational map relatively to $S$[^N.D.E-XVIII-8]

$$ X \dashrightarrow G $$

that commutes with the composition laws. We treat only the case where $X/S$ satisfies the following hypothesis:

```text
(♦)   X/S is faithfully flat, of finite presentation, and
      with separated fibers "without embedded components".
```

(Note that the latter two hypotheses are properties that hold for a group prescheme.[^N.D.E-XVIII-9])

We shall often suppress the symbol $S$ in fiber products.

Let $X/S$ be a prescheme with the properties `(♦)` above, and let $W$ be a subprescheme of finite presentation of $X
\times X \times X$ having the following property:

```text
(∗)   The three morphisms W → X × X given by the projections of X³ onto X²
      are open immersions, schematically dense relatively to S.
```

**Notations.** We shall use the following terminology. Given sections $a, b, c \in X(S')$, $S' \to S$ arbitrary, such
that $(a, b, c) \in W(S')$, we write:

```text
c = ab,    b = a⁻¹c,    a = cb⁻¹.
```

**Definition 3.0.1.**[^N.D.E-XVIII-10] *We say, given a section $(a, b) \in X^{2}(S')$, that `ab`* is defined *if and
only if there exists a section $c \in X(S')$ such that $(a, b, c) \in W(S')$, i.e. if and only if $(a, b)$ lies in
$pr_{12} W(S')$. Similarly, to say that $a^{-1}b$ or $ab^{-1}$ is defined has the analogous meaning, and one extends
this terminology to products of several factors as well.*

<!-- label: III.XVIII.3.0.1 -->

**Remark 3.0.2.** *Let us note immediately the following fact: by (i), $W$ defines a rational map $X^{2} \dashrightarrow
X$ over $S$ (the one given by $(a, b) \mapsto ab$). It may well happen that this rational map has a domain of definition
larger than $pr_{12} W$. Nevertheless, we say that `ab` is defined only if $(a, b) \in pr_{12} W(S')$.*

<!-- label: III.XVIII.3.0.2 -->

**Definition 3.1.** *A* group germ *is a prescheme $X/S$ having the properties `(♦)` above together with a subprescheme
$W$ of finite presentation of $X \times X \times X$ having the following properties:*

<!-- label: III.XVIII.3.1 -->

<!-- original page 640 -->

*(i) $W$ satisfies the property $(\ast)$ above.*

*(ii) For each section $a \in X(S)$, the sets*

```text
pr_i((a × X × X) ∩ W),    i = 2, 3,
pr_i((X × a × X) ∩ W),    i = 3, 1,
pr_i((X × X × a) ∩ W),    i = 1, 2,
```

*are schematically dense in $X$ relatively to $S$, and this statement remains true after every base change $S' \to S$.
(Hypothesis (i) implies that these sets are opens of $X$.) Intuitively, this says that "`ax` is defined for $x$
sufficiently general", etc.*

*(iii) The law is associative, i.e. if $(a, b, c) \in X^{3}(S')$, $S' \to S$ arbitrary, is such that `(ab)c` and $a(bc)$
are defined, one has $(ab)c = a(bc)$.*

**Remarks.** *(a) In (i), the condition that $W$ be schematically dense in $X^{2}$ relatively to $S$ may be replaced by
the condition that for each $s \in S$ the fiber $W_{s}$ be dense in $X^{2}_{s}$ in the topological sense, thanks to the
hypotheses on $X$ and to 1.2.*

*(b) Condition (iii) is equivalent to the following: let $V_{1}$ (resp. $V_{2}$) be the open of $X^{3}$ where the
rational map $(a, b, c) \mapsto a(bc)$ (resp. $(a, b, c) \mapsto (ab)c$) is defined[^XVIII-3-1]. Then there exists an
open $V \subseteq V_{1} \cap V_{2}$ which is schematically dense in $X^{3}$ relatively to $S$ on which the two preceding
maps coincide. This is a consequence of 1.4 because, of course, $V_{1}$ and $V_{2}$ are schematically dense in $X^{3}$
relatively to $S$.*

*(c) Hypothesis (ii) will serve below to ensure that $X$ will be a subobject of the group prescheme that it defines. In
many cases one may deduce (ii) from (i), provided that one replaces $X$ by an open $X^{0}$ relatively schematically
dense, and $W$ by a relatively schematically dense open of $W \cap X^{03}$. In fact one has:*

**Proposition 3.2.** *Suppose that each geometric fiber of $X/S$ is irreducible, and let $W$ be a subprescheme of
$X^{3}$ satisfying condition (i) of 3.1. Then there exists an open $X^{0}$ of $X$ relatively schematically dense and an
open $W^{0}$ of $W \cap (X^{0} \times X^{0})$ relatively schematically dense such that the pair $(X^{0}, W^{0})$
satisfies conditions (i) and (ii). If (iii) is satisfied for $(X, W)$, it is satisfied for $(X^{0}, W^{0})$.*

<!-- label: III.XVIII.3.2 -->

<!-- original page 641 -->

*Proof.* Set $X^{0} = \bigcap^{3}_{i=1} pr_{i} W$. Each $pr_{i} W$ is open in $X$ because $W \to X^{2}$ is an open
immersion and the projections $X^{2} \to X$ are flat and of finite presentation. Moreover, $pr_{i} W$ is relatively
schematically dense in $X$ because $W$ is so in $X^{2}$ and the projections $X^{2} \to X$ are surjective (it suffices to
check density in the topological sense). Take $W^{0} = W \cap X^{03}$.

To verify that (i) holds, note that

```text
W⁰ = (W ∩ (X⁰ × X⁰ × X)) ∩ (W ∩ (X × X⁰ × X⁰)) ∩ (W ∩ (X⁰ × X × X⁰)).
```

Now $W \cap (X^{0} \times X^{0} \times X) \simeq pr_{12} W \cap (X^{0} \times X^{0})$, hence is relatively schematically
dense in $W$. Similarly, the other terms of the right-hand side are relatively schematically dense in $W$, and
consequently $W^{0}$ is relatively schematically dense in $W$. Hence $pr_{ij} W^{0}$ is relatively schematically dense
in $pr_{ij} W$, hence in $X \times X$, hence in $X^{0} \times X^{0}$.

To verify condition (ii), let $a \in X^{0}(S')$ and write $S_{0} = S$. We must show that, for example, $pr_{2}((a \times
X^{0} \times X^{0}) \cap W^{0})$ is schematically dense in $X^{0}$ relatively to $S$. By 1.3, it suffices to verify this
fiber by fiber, that is, it suffices to treat the case where $S$ is the spectrum of a field, and in that case it
suffices to verify that the open is non-empty, because the fibers of $X/S$ are irreducible and "without embedded
components". Since $pr_{2}((a \times X \times X) \cap W)$ is non-empty (as $a$ is a section of $X^{0}$), this open is
dense in $X$. One has

```text
pr₂((a × X × X) ∩ W) = pr₂((a × X) ∩ pr₁₂ W).
```

Hence,

```text
pr₂((a × X) ∩ pr₁₂ W) ∩ X⁰ = pr₂((a × X⁰) ∩ pr₁₂ W) = pr₂((a × X⁰ × X) ∩ W)
```

is dense in $X$, hence in $X^{0}$.

Similarly, $pr_{3}((a \times X \times X^{0}) \cap W)$ is dense in $X$, hence in $pr_{3}((a \times X \times X) \cap W)$,
i.e. $(a \times X \times X^{0}) \cap W$ is dense in $(a \times X \times X) \cap W$, i.e. $pr_{2}((a \times X \times
X^{0}) \cap W)$ is dense in $pr_{2}((a \times X \times X) \cap W)$, hence dense in $X$, hence dense in $X^{0}$.

Now since

```text
pr₂((a × X⁰ × X⁰) ∩ W⁰) = pr₂((a × X⁰ × X⁰) ∩ W)
                       = pr₂((a × X⁰ × X) ∩ W) ∩ pr₂((a × X × X⁰) ∩ W),
```

it is indeed dense in $X^{0}$, as was to be shown. The other assertions of (ii) follow by symmetry, and the fact that
condition (iii) is preserved is trivial.[^N.D.E-XVIII-11] Proposition 3.2 is proved.

### 3.2.1.

<!-- label: III.XVIII.3.2.1 -->

[^N.D.E-XVIII-12]

<!-- original page 642 -->

Let us now fix a group germ $(X, W)$ over $S$. We must make some preliminary remarks on the situation, which we have
gathered together below. We shall use these rules often without explicit mention in the sequel.

Let $a \in X(S')$, and write $S_{0} = S$. Then one obtains a (bi)rational map $\phi$ over $S$ from $X$ to itself by
associating to a section $x$ the section `ax` if it is defined. By 3.1 (ii), the domain of definition of $\phi$ contains
the relatively schematically dense open $pr_{2}((a \times X \times X) \cap W)$, and $\phi$ defines an isomorphism of
this open onto the open (where $a^{-1}x$ is defined) $pr_{3}((a \times X \times X) \cap W)$. This remark is generalized
in the obvious way in Rule 1.

**Rule 1.** *Let $P = P(x, t_{1}, \cdots, t_{n})$ be a "product" of the symbols $x, t_{1}, \cdots, t_{n}$ obtained
recursively as follows: $P_{0} = x$; $P_{i+1}$ is one of the following expressions:*

```text
P_i t,   t P_i,   P_i⁻¹ t,   t P_i⁻¹,   P_i t⁻¹,   t⁻¹ P_i,
```

*where $t$ is one of the $t_{j}$; $P_{r} = P$. Let $a_{1}, \cdots, a_{n} \in X(S')$. Then there exists a relatively
schematically dense open $U$ of $X_{S'}$ such that the product $P(x, a_{1}, \cdots, a_{n})$ is defined (in the sense of
Remark 3.0.2) for a section $x \in X(S'')$ if and only if $x \in U(S'')$, and the map $x \mapsto P(x, (a))$ gives an
isomorphism of $U$ onto another relatively schematically dense open, denoted $P(U, (a))$, of $X_{S'}$.*

**Rule 2.** *Let $a, b \in X(S')$. Then:*

*If `ab` is defined, so is $a^{-1}(ab)$, and $a^{-1}(ab) = b$.*

*If $a^{-1}b$ is defined, so is $a(a^{-1}b)$, and $a(a^{-1}b) = b$.*

*If $ba^{-1}$ is defined, so is $(ba^{-1})a$, and $(ba^{-1})a = b$.*

**Rule 3.** *Let $a, b, b' \in X(S')$. If $ab = ab'$, if $ba = b'a$, if $a^{-1}b = a^{-1}b'$ or if $ba^{-1} = b'a^{-1}$,
then $b = b'$. Here it is implicit that the equality relation implies that both sides are defined.*

**Rule 4.** *Let $a, b, c \in X(S')$. Then whenever both sides are defined, one has*

```text
a((ba)⁻¹ c) = b⁻¹ c.
```

<!-- original page 643 -->

*Similarly:*

```text
(c(ab)⁻¹) a = cb⁻¹,    a⁻¹(ab⁻¹) c = b⁻¹ c,    (c(b⁻¹ a)⁻¹) a = cb⁻¹.
```

**Rule 5.** *All the following associativity laws are true, whenever both sides are defined:*

```text
(a⁻¹b)c = a⁻¹(bc),    (ab⁻¹)c = a(b⁻¹c),    (ab)c⁻¹ = a(bc⁻¹),
(ab)⁻¹c = b⁻¹(a⁻¹c),  (a⁻¹b)c⁻¹ = a⁻¹(bc⁻¹), (ab⁻¹)c⁻¹ = a(cb)⁻¹.
```

### 3.2.2. Verification of the rules.

<!-- label: III.XVIII.3.2.2 -->

(1) is by an obvious induction on the length $r$ of $P$, the case $r = 1$ being a direct consequence of 3.1 (ii).

(2) Trivial from the definition.

(3) Indeed, by Rule 2, for example in the first case, one has

```text
b = a⁻¹(ab) = a⁻¹(ab') = b'.
```

(4) Let us verify, for example, the first relation. On the right-hand side left multiplication by $b$ is defined and
gives $c$, by Rule 2. Suppose it is also defined on the left-hand side. Then one will have

```text
b(a((ba)⁻¹ c)) = (ba)((ba)⁻¹ c) = c.
```

Indeed `(ba)` is defined by hypothesis because it figures in the expression. Hence the middle member is defined and
equal to $c$ by Rule 2, and equal to the left-hand member by associativity (cf. 3.1 (iii)). Hence Rule 3 implies that
the desired equality is true if this multiplication by $b$ is defined.

Now fix $a$ and $b$. Then Rule 1 implies that $b(a((ba)^{-1} c))$ is well defined for $c$ "in" an open $U$ of $X$
relatively schematically dense; hence on this relatively schematically dense open the two rational maps $c \mapsto
b^{-1} c$ and $c \mapsto a((ba)^{-1} c)$ are equal. By 1.4, they are equal on every common domain of definition, whence
the desired result.

(5) The same kind of argument as the preceding. For example one verifies $(ab^{-1})c^{-1} = a(cb)^{-1}$ as follows. If
right multiplication by $c$ is defined on the right-hand side, one has equality by Rule 4. Since it suffices to verify
such a formula on a relatively schematically dense open, one reduces to the case where this multiplication is well
defined.

<!-- original page 644 -->

### 3.2.3.

<!-- label: III.XVIII.3.2.3 -->

Consider now the relation $R$ on $X \times X$ obtained by setting, for $a, b, a', b' \in X(S')$, $(a, b) \sim (a', b')
mod R(S')$ if and only if there exists $S' \to S$ fppf-covering and a section $x \in X(S')$ such that `(xa)b` and
`(xa')b'` are defined and equal. Then $R$ is an equivalence relation.

Indeed, this relation is evidently symmetric. By Rule 1, the product `(xa)b` is defined if $x$ is "in" a suitable
relatively schematically dense open. Hence 1.7 asserts that there exists $S' \to S$ fppf-covering and an $x \in X(S')$
such that `(xa)b` is defined. The relation is therefore reflexive, and transitivity is a consequence of the following
lemma:

**Lemma 3.3.** *Let `x, y, a, b, a', b'` be sections of $X(S')$ such that `(xa)b`, `(xa')b'`, `(ya)b`, `(ya')b'` are
defined. If $(xa)b = (xa')b'$ then $(ya)b = (ya')b'$.*

<!-- label: III.XVIII.3.3 -->

Indeed, the lemma says that one may test $(a, b) \sim (a', b')$ with any $x \in X(S')$, $S' \to S$ fppf-covering, such
that both products are defined. Given $a, b, a', b', a'', b'' \in X(S)$, one may, by Rule 1, 1.1 and 1.7, find an
fppf-covering extension $S' \to S$ and a section $x \in X(S')$ such that the three products in question are defined,
whence transitivity.

*Proof of the lemma.* Let us write formally to begin with:

```text
(za)b = ((zx⁻¹)x) a b = ((zx⁻¹)(xa)) b = (zx⁻¹)((xa)b),
(za')b' = ((zx⁻¹)x) a' b' = ((zx⁻¹)(xa')) b' = (zx⁻¹)((xa')b').
```

One verifies that these equalities are indeed true if the members are defined, by the appropriate
rules[^N.D.E-XVIII-13]. It follows that $(za)b = (za')b'$ if all these expressions are defined. Moreover, by Rule 1 and
the hypotheses already made, these expressions are well defined if $z \in X(S'')$ is in $V(S'')$, where $V$ is a certain
open of $X$ relatively schematically dense (we have taken $S_{0} = S$). Hence the two rational maps from $X$ to itself
given by $z \mapsto (za)b$ and $z \mapsto (za')b'$ are equal, whence $(ya)b = (ya')b'$.

<!-- original page 645 -->

**Lemma 3.4.** *Consider the rational map $\phi : X^{3} \dashrightarrow X$ over $S$ defined by $(a, b, c) \mapsto
c^{-1}(ab)$. Let $U$ be the domain of definition of $\phi$ and consider the graph $\Gamma$ of the morphism $f : U \to X$
induced by $\phi$, which is a subscheme of $X^{4}$. Then a section $(a, b, c, d) \in X^{4}(S)$ is in $\Gamma(S)$ if and
only if $(a, b) \sim (c, d)$.*

<!-- label: III.XVIII.3.4 -->

*Proof.* Note first that the rational map $\phi$ is the same as the one given by the formula $(a, b, c) \mapsto
(xc)^{-1}((xa)b)$ for an arbitrary section $x \in X(S)$. This is the same as saying that one has $c^{-1}(ab) =
(xc)^{-1}((xa)b)$ whenever both sides are defined. We leave the verification to the reader.

We show then that the map $\phi$ is defined at a section $(a, b, c) \in X^{3}(S)$ if and only if there exists $d$ with
$(a, b) \sim (c, d)$, and that one then has $d = \phi(a, b, c)$. Indeed, suppose that $(a, b) \sim (c, d)$. To verify
that $\phi$ is defined, it is permitted to make an fppf-covering base change (Proposition 1.6), and one may therefore
assume that there exists a section $x \in X(S')$ such that `(xa)b` and `(xc)d` are defined and equal. It follows (Rule
2) that $(xc)^{-1}((xa)b)$ is defined and equal to $d$.

Conversely, suppose $\phi$ is defined at the section $(a, b, c)$ and let $d = \phi(a, b, c)$. Choose $S' \to S$
fppf-covering and a section $x \in X(S')$ such that `(xa)b` and `(xc)d` are defined. We want to show that they are
equal. For this, it suffices to show that the two rational maps over $S$ from $X$ to itself, given by $b \mapsto (xa)b$
and $b \mapsto (xc)\phi(a, b, c)$, are the same, which follows from the remark of the first paragraph.

<!-- original page 646 -->

**Proposition 3.5.** *The equivalence relation $R \Rightarrow X^{2}$ is representable, and it is a flat relation of
finite presentation, that is, the projections of $R$ onto $X^{2}$ are flat morphisms of finite presentation.*

<!-- label: III.XVIII.3.5 -->

*Proof.* We may suppose $S$ affine. Since $(X, W)$ is of finite presentation over $S$, we may descend the whole
situation to an $S$ of finite type over $\operatorname{Spec} \mathbb{Z}$, hence noetherian. We may therefore suppose $S$
noetherian. Then it is trivial that the graph $\Gamma$ of (3.4) is of finite presentation over $X^{2}$. The projection
$pr_{12}|\Gamma$ is flat because $\Gamma \xrightarrow{\sim} pr_{123} \Gamma$, which is an open of $X^{3}$, and the
projection $pr_{12} : X^{3} \to X^{2}$ is flat because $X$ is flat over $S$.

I claim that $\Gamma$ represents $R$. Note that there is something to prove, because the domain of definition of a
rational map does not in general commute with base change. Let $S'' \to S$. What is clear, by (3.4) applied to `S''`, is
that $R(S'') \supset \Gamma(S'')$, because $\phi \times_{S} S''$ is certainly defined on $U \times_{S} S''$. Let then
$(a, b, c, d) \in R(S'')$. We must show that $(a, b, c, d) \in \Gamma(S'')$. The verification of this is done locally
for, say, the étale topology. We may therefore suppose `S''` strictly local, i.e. the spectrum of a henselian ring with
separably closed residue field. Moreover, by applying (1.6) and the usual passage-to-the-limit standard arguments, we
reduce to the case $S$ strictly local and $S'' \to S$ local. Suppose we have a section $x \in X(S)$ such that over `S''`
the products `(xa)b` and `(xc)d` are defined. This will imply that $(xc)^{-1}((xa)b)$ is defined, and equal to $d$. Now
there exists an open $V$ of $X^{3}$ relatively sch. dense such that $(xc)^{-1}((xa)b)$ is defined if and only if $(a, b,
c) \in V(S'')$, and one has $V \subseteq U$. Hence $(a, b, c, d) \in \Gamma(S'')$ if such an $x$ exists. By (1.6) it is
permitted to make a base change $S' \to S$ fppf-covering to find such an $x$. Since $S$ is strictly local, one
can[^XVIII-3-2] find an $S' \to S$ faithfully flat, local, and finite and a section $x \in X(S')$ which "passes through"
an arbitrary closed point of the closed fiber of $X/S$. Now to say that `(xa)b` and `(xc)d` are defined means that over
`S''`, $x$ lies in a certain relatively sch. dense open, which is verified on the closed fiber of $X_{S''}$. Hence it
works.

<!-- original page 647 -->

Let now $G$ be the quotient of $X^{2}$ by $R$ as a sheaf for the fppf topology. We shall define a composition law on $G$
as follows. Let $(g, g') \in G(S')$ be represented by a section `((a, b), (c, d))` of $X^{2} \times X^{2}(S'')$, $S''
\to S'$ fppf-covering. Suppose moreover that $X$ admits a section $x$ over `S''` such that $a(b(cx))$ and $x^{-1}d$ are
defined, which is permitted by Rule 1 and (1.7), and we call `gg'` the class in $G(S')$ represented by the section
$(a(b(cx)), x^{-1}d)$ of $X^{2}(S'')$.

Let us verify that `gg'` does not depend on the choice of the section $x$ and the representative `((a, b), (c, d))`.
Indeed, let $(a', b') \sim (a, b)$, $(c', d') \sim (c, d)$, and $x'$ be such that `a'(b'(c'x'))` and $x'^{-1}d'$ are
defined. We may suppose that all are sections over `S''`. We must show that

```text
(a(b(cx)), x⁻¹d) ∼ (a'(b'(c'x')), x'⁻¹d'),
```

that is, that for a suitable section $z \in X(S''')$, $S''' \to S''$ suitably fppf-covering,

$$ (z(a(b(cx))))(x^{-1}d) = (z(a'(b'(c'x'))))(x'^{-1}d'). $$

Whenever all the products are defined, one has

$$ (z(a(b(cx))))(x^{-1}d) = ((za)(b(cx)))(x^{-1}d) = = (((za)b)(cx))(x^{-1}d) = ((((za)b)c)x)(x^{-1}d) = =
(((za)b)c)(x(x^{-1}d)) = (((za)b)c)d, $$

and the same identities are true with the primes. Now by Rule 1 and (1.7) there exists such a $z$. One must therefore
show that

```text
(((za)b)c)d = (((za')b')c')d'.
```

But $(za)b = (za')b'$ because $(a, b) \sim (a', b')$ (3.3) and one has the desired equality because $(c, d) \sim (c',
d')$.

<!-- original page 648 -->

Consider the natural morphism $i : X \to G$ defined as follows. For $a \in X(S')$, one chooses $S'' \to S'$
fppf-covering and a section $b \in X(S'')$ such that $ab^{-1}$ is defined, and one sets

```text
i(a) = class in G of (ab⁻¹, b).
```

One easily verifies that this class, which is a priori in $G(S'')$, does not depend on the choice of $b$ and so gives a
well-determined element of $G(S')$.

The reader will give himself the pleasure of verifying the following:

**Proposition 3.6.** *The morphism $i$ commutes with the composition laws of $X$ and of $G$, i.e. if $a, b \in X(S')$
are sections such that `ab` is defined, one has $i(a)i(b) = i(ab)$.*

<!-- label: III.XVIII.3.6 -->

The goal of this section is the following theorem:

**Theorem 3.7.**[^N.D.E-XVIII-14] *Let $(X, W)$ be a group germ over $S$, with $X/S$ faithfully flat, of finite
presentation, and with separated fibers without embedded component. Then with the notations above one has*

<!-- label: III.XVIII.3.7 -->

*(i) $G$ is a sheaf of groups.*

*(ii) $i : X \to G$ is representable by an open immersion.*

*(iii) $G$ is representable locally on $S$ for the fppf topology.*

*(iv) If $G/S$ is representable, then it is a flat group of finite presentation, and $i : X \to G$ is schematically
dense relatively to $S$.*

Note that $G$ is evidently characterized by properties (i), …, (iv); one may therefore forget the explicit construction
of $G$.

The proof proceeds in several stages:

**Lemma 3.8.** *(i) Let $c$ be a section of $X(S)$; then the morphism from the prescheme $c \times X$ (which is
$S$-isomorphic to $X$) into $G$ given by $c \times X \hookrightarrow X \times X \to G$ is a monomorphism.*

<!-- label: III.XVIII.3.8 -->

<!-- original page 649 -->

*(ii) Let ${c_{i}}$, $i \in I$, be sections of $X(S)$, let $Z = \sqcup_{i} c_{i} \times X$, and call $R^{0} \Rightarrow
Z$ the equivalence relation induced on $Z$ by the obvious morphism $Z \to X^{2}$. Then $R^{0}$ is a "gluing" of the
$c_{i} \times X \simeq X$.*

*Proof.*

(i) For two sections $(c, a)$ and `(c, a')` of $(c \times X)(S')$ to have the same image in $G$, one must have $(c, a)
\sim (c, a')$, that is, $(xc)a \sim (xc)a'$ for a suitable $x \in X(S'')$, $S'' \to S'$ fppf-covering, whence $a = a'$
by Rule 3.

(ii) Let $c_{i}$, $c_{j}$ be two sections and consider the birational map $\psi_{ji}$ of $X$ to itself over $S$ given by
the formula $x \mapsto c^{-1}_{j}(c_{i} x)$. This is the same map as the one given by $x \mapsto
(yc_{j})^{-1}((yc_{i})x)$, for $y \in X(S)$, as one easily sees. Moreover, one verifies that $\phi_{ji}$ is defined at
$b \in X(S')$ if and only if there exists $b'$ such that $(c_{i}, b) \sim (c_{j}, b')$, and then $b' = \phi_{ji}(b)$.
Let $U_{ji}$ be the domain of definition over $S$ of $\phi_{ji}$. It remains to show that this domain of definition is
universal, i.e. that if $b \in X(S'')$, $S'' \to S$ arbitrary, and if $\phi_{ji}$ is defined at $b$, then $b \in
U_{ji}(S'')$. It comes to the same to show that if $b, b' \in X(S'')$ are such that $(c_{i}, b) \sim (c_{j}, b')$, then
$b \in U_{ji}(S'')$. We leave the verification of this fact, which is analogous to that of (3.5), to the reader.

**Lemma 3.9.** *Suppose that ${c_{i}}$, $i \in I$, are sections of $X(S)$ such that $\sqcup_{i} c_{i} \times X \to G$ is
surjective as a morphism of sheaves. Then $G$ is representable and flat, of finite presentation over $S$, and the
structural morphism $X^{2} \to G$ is flat and of finite presentation.*

<!-- label: III.XVIII.3.9 -->

*Proof.* The fact that $G$ is representable is an immediate consequence of (3.8), and it follows that $\sqcup_{i} c_{i}
\times X \to G$ is an open covering. To show that $X^{2} \to G$ is flat, it suffices to do so locally, hence to show
that the rational map $X^{2} \dashrightarrow c_{i} \times X$ induces a flat morphism on its domain of definition. Now
this rational map is given by $(a, b) \mapsto (c_{i}, ((xc_{i})^{-1}(xa))b)$, $x$ an arbitrary section, and if it is
defined at $(a, b) \in X^{2}(S')$, one can find $S'' \to S'$ fppf-covering and a section $x \in X(S'')$ such that
$((xc_{i})^{-1}(xa))b$ is defined. One sees easily that this is therefore a flat morphism.

<!-- original page 650 -->

It similarly follows that it is locally of finite presentation, hence fppf-covering. Now by construction, the relation
$R$ is effective. Hence by (3.5), the morphism $X^{2} \to G$ becomes of finite presentation after the base change $G
\leftarrow X^{2}$, which is fppf-covering; hence $X^{2} \to G$ is of finite presentation. Let us show that $G \to S$ is
flat and of finite presentation. It is flat and locally of finite presentation since $G$ is covered by the $c_{i} \times
X \simeq X$. Now $X^{2}/S$ is quasi-compact, and $X^{2} \to G$ is surjective. This shows that $G/S$ is quasi-compact. To
show that $G \to S$ is quasi-separated, note that one has the following cartesian diagram

```text
              α
       R ─────────→ X² ×_S X²
       │                │
     γ │                │ β
       ▼      Δ         ▼
       G ──────────→ G ×_S G.
```

One has $\gamma$ surjective and $\alpha, \beta$ quasi-compact, hence $\beta \alpha$ is quasi-compact, hence $\Delta$ is
quasi-compact.[^N.D.E-XVIII-15]

**Lemma 3.10.** *Let ${c_{i}}$, $i \in I$, be sections of $X(S)$. For $\sqcup_{i} c_{i} \times X \to G$ to be surjective
as a morphism of fppf-sheaves, it suffices that the following condition be satisfied:*

<!-- label: III.XVIII.3.10 -->

*For each $S' \to S$ and $(a, b) \in X^{2}(S')$, there exist an open covering ${S'_{\nu}}$, $\nu \in N$, of $S'$ and a
function $N \to I$ ($\nu \mapsto i(\nu)$) such that $(c^{-1}_{i(\nu)} a)b$ is defined on $S'_{\nu}$.*

*Proof.* Let $S'' \to S$ be arbitrary, and $g \in G(S'')$. Choose $S' \to S''$ fppf-covering and a section $(a, b) \in
X^{2}(S')$ representing $g$. Take the open covering ${S'_{\nu}}$ of $S'$ that exists by the hypothesis of the lemma.
Then on each $S'_{\nu}$ one has $(a, b) \sim (c_{i(\nu)}, (c^{-1}_{i(\nu)} a)b)$, hence $g$ is represented by a section
of $[c_{i(\nu)} \times X](S')$ on $S'_{\nu}$, which proves surjectivity, because the family of morphisms ${S'_{\nu} \to
S''}$ is fppf-covering.

**Lemma 3.11.** *Let $Y/S$ be a prescheme of finite presentation, and let ${a_{i}}$, $i \in I$, be sections of $Y(S)$.
Let $s_{0}, s_{1}$ be points of $S$ such that $s_{0}$ is a specialization of $s_{1}$, and $Y_{j}$ the fiber of $Y/S$ at
the point $s_{j}$. Let $C_{j}$ be the closure in $Y_{j}$ of the set of points ${a_{i}(s) \cap Y_{j}}$. Then one has
$\dim C_{1} \geqslant \dim C_{0}$.*

<!-- label: III.XVIII.3.11 -->

<!-- original page 651 -->

*Proof.* It suffices to make the verification after a base change $S' \to S$ with chosen points $s'_{0}$ and $s'_{1}$
such that $s'_{j} \mapsto s_{j}$ and $s'_{0}$ is a specialization of $s'_{1}$. One is

<!-- original page 386 (continuing) -->

therefore (EGA II 7.1.4) reduced to the case where $S$ is the spectrum of a valuation ring $A$, $s_{0}$ the closed point
of $S$, and $s_{1}$ the generic point of $S$. Now let $V$ be the closure of $C_{1}$ in $Y$. It is clear that $C_{0}
\subseteq V$, and so the lemma is a consequence of the "well-known" fact that an irreducible closed subprescheme $V$ of
a prescheme $Y/S$ of finite presentation satisfies $\dim V \times_{S} s_{1} \geqslant \dim V \times_{S} s_{0}$ if $S$ is
the spectrum of a valuation ring and if $V \times_{S} s_{1} \neq \emptyset$ (EGA IV 13.1.6).

**Lemma 3.12.** *Suppose that $S$ is the spectrum of a local ring with closed point $s_{0}$, and let ${c_{i}}$, $i \in
I$, be sections such that the closure $C_{0}$ of the set ${c_{i}(s) \cap X_{0}}$ in the closed fiber $X_{0}$ is of
dimension equal to $\dim X_{0} = n$. Then the condition of Lemma 3.9 is satisfied.*

<!-- label: III.XVIII.3.12 -->

*Proof.* Note first that the fibers of $X/S$ all have the same dimension $n$, which results from EGA IV 12.1.1 (i) and
from the fact that $X$ has a rational composition law. Lemma (3.11) therefore implies that for each morphism $S_{1} \to
S$ with $S_{1}$ the spectrum of a field, the dimension of the closure of the set ${c_{i} \times_{S} S_{1}}$ in
$X_{S_{1}}$ is equal to $n$. Let us verify the condition of (3.10). Let $(a, b) \in X^{2}(S')$. For $(c^{-1}_{i} a)b$ to
be defined, it is necessary and sufficient that $c_{i}$ be contained in a certain open $U \subseteq X_{S'}$ which is
sch. dense relatively to $S'$ (Rule 1). We must show that this is true for a suitable $i$, locally on $S'$. It therefore
suffices to treat the case where $S'$ is the spectrum of a local ring, and then the fact that $c_{i} \in U(S')$ is
verified on the closed fiber. We are thus reduced to the case $S' = \operatorname{Spec} k$, $k$ a field. Now with the
notations above, take $S' = S_{1}$.

<!-- original page 652 -->

One has $\dim C_{1} = \dim X_{S_{1}}$, and $U$ is relatively sch. dense in $X_{S_{1}}$. Hence $U \cap C_{1} \neq
\emptyset$, whence $U \cap {c_{p} \times_{S} S_{1}} \neq \emptyset$, and we are done.

The proof of the theorem is now easy. Note first the following consequence of the finiteness of Lemma (3.9): if
${A_{i}}$ is an inductive system of rings over $S$, if $\tilde{A} = \lim A_{i}$, and if the hypotheses of (3.9) are
satisfied for $S = \operatorname{Spec} \tilde{A}$, then one may descend the object that represents the quotient $G$ of
$R \Rightarrow X^{2}$ to one of $S_{i} = \operatorname{Spec} A_{i}$ with the finiteness and flatness properties stated
in (3.9). This is the usual passage to the limit (EGA IV 8 and 11). It follows that for the proof of (iii) and (iv) of
(3.7), one may restrict to the case $S = \operatorname{Spec} A$, with $A$ a strictly local ring. Let then $x_{0}$ be a
closed point of the closed fiber $X_{0}$ of $X/S$. There exists[^XVIII-3-3] an extension $A'$ of $A$, local, free and
finite, and a section of $X' = X \times_{S} S'$ passing through the unique point $x'_{0}$ of $X'$ above $x_{0}$. Note
that $X'_{0} \to X_{0}$ is radicial since $S$ is strictly local, hence the residue field of $A$ separably closed. It
follows that there exists an inductive system ${A_{i}}$ of local rings, flat and finite over $S$, such that, setting
$\tilde{A} = \lim A_{i}$ and $\tilde{X} = X \times_{S} \operatorname{Spec} \tilde{A}$, $\tilde{X}$ has a set of sections
which induces a dense set on the closed fiber $\tilde{X}_{0}$. For each closed point $x_{0}$ of $X_{0}$ one takes an
extension $A(x_{0})$ such that the corresponding base change of $X$ admits a section "passing through $x_{0}$", and one
takes as inductive system the system of finite tensor products of the $A(x_{0})$. Note that `Ã` is local, being a limit
of local rings. Hence by (3.12) and (3.10) one has the quotient $G$

<!-- original page 653 -->

over $\operatorname{Spec} \tilde{A}$, hence over one of $\operatorname{Spec} A_{i}$ by the remarks above, hence locally
for the fppf topology.

In fact it follows from the constructions that locally for the fppf topology one can find a finite set of sections
${c_{i}}$ ($i = 1, \cdots, r$) such that $G$ is covered by the $c_{i} \times X$. (ii) and (iv) follow easily from this
fact, and we leave the verification of (i) to the reader.

**Corollary 3.13.** *The sheaf of groups $G$ determined by a group germ $(X, W)$ over $S$ is representable in each of
the following situations:*

<!-- label: III.XVIII.3.13 -->

*(i) $S$ is artinian.*

*(ii) For each local scheme $S' \to S$ at a closed point $s$ of $S$, $X_{S'}$ has a set of sections that induces on the
closed fiber a set whose closure is of dimension $\dim X_{s}$.*

*(iii) $S$ is strictly local, and $X/S$ is smooth.*

*(iv) There exists $S' \to S$ fppf-covering such that $G_{S'}$ is representable and affine over $S$.*

Indeed, (ii) is a consequence of (3.10) and (3.12), (iii) follows directly from (ii) and "Hensel's lemma", (iv) from the
descent of affine schemes, and (i) from the descent of group schemes, which is possible here because one knows that
every finite subset of a group over a field is contained in an affine open (Exp. VI).

## Bibliography

[1] Weil, A., *Variétés abéliennes et courbes algébriques*. Hermann, Paris, 1948.

[2] Yanagihara, H., *Reduction of group varieties and transformation spaces*. Journ. Sci. Hiroshima Univ., Ser. A-I,
vol. 27, No. 1, June, 1963.

## Footnotes

<!-- LEDGER DELTA — Exposé XVIII — for consolidation in Phase 3
| French | English | Note |
| ------ | ------- | ---- |
| loi rationnelle | rational law | Per glossary. |
| loi birationnelle | birational law | Standard. |
| germe de groupe | group germ | Grothendieck's term; preserved. |
| application rationnelle | rational map | Standard. |
| application birationnelle | birational map | Standard. |
| schématiquement dense relativement à S | schematically dense relatively to S | Standard. |
| relativement schématiquement dense | relatively schematically dense | Standard. |
| domaine de définition | domain of definition | Standard. |
| fppf-couvrant | fppf-covering | Standard. |
| recollement | gluing | Per VI_A glossary. |
| « sans composantes immergées » | "without embedded components" | Quoted as in source. |
| sections d'un préfaisceau | sections of a presheaf | Standard. |
| sites (au sens de Exp. IV) | sites (in the sense of Exp. IV) | Standard. |
| règle | rule | "Règle 1" → "Rule 1", etc. |
| spécialisation | specialization | American spelling. |
| henselien | henselian | American spelling. |
| strictement local | strictly local | Standard. |
| anneau de valuation | valuation ring | Standard. |
| « bien connu » | "well-known" | Quoted as in source. |
| « passant par x₀ » | "passing through x₀" | Quoted as in source. |
| sorites habituels | usual standard arguments | "Sorites" = a standard chain of small lemmas. |
| `Cb` (OCR) | `Ĉ` | Not encountered in this Exposé; ledger note. |
-->

[^XVIII-1-1]: cf. also EGA IV₃, 11.9 and 11.10 (notably 11.10.8), where one says "universally schematically dense
    relatively to $S$".

[^N.D.E-XVIII-1]: N.D.E.: to be made precise for which topology: a priori (fpqc).

[^N.D.E-XVIII-2]: N.D.E.: We recall here the definition of a closed immersion. A morphism of $S$-functors $F \to G$ is
    *relatively representable* if for every $S$-morphism $T \to G$, where $T$ is an $S$-prescheme, the $T$-functor
    $F_{T} = F \times_{S} T$ is representable by a $T$-prescheme. A morphism of $S$-functors $F \to G$ is an *open*
    (resp. *closed*) *immersion* if it is relatively representable and if for every $S$-morphism $T \to G$, where $T$ is
    an $S$-prescheme, the $T$-morphism $F_{T} \to T$ is an open (resp. closed) immersion.

[^N.D.E-XVIII-3]: N.D.E.: To be made precise…

[^XVIII-1-2]: cf. EGA IV₄, 20.5, where one says "pseudo-morphism of $X$ into $Y$ relatively to $S$", in order not to
    conflict with EGA I, 7.12.

[^N.D.E-XVIII-4]: N.D.E.: The number 1.5.1 has been added.

[^N.D.E-XVIII-5]: N.D.E.: i.e. a category equipped with a topology, cf. IV, § 4.2.

[^N.D.E-XVIII-6]: N.D.E.: See the note at 1.4.

[^XVIII-2-1]: Or in $G$, which amounts to the same by virtue of 1.1 (iv).

[^N.D.E-XVIII-7]: N.D.E.: The beginning of the following sentence has been added.

[^N.D.E-XVIII-8]: N.D.E.: To make explicit the notion of birational map (relatively to $S$), perhaps in an addition
    1.5.2?

[^N.D.E-XVIII-9]: N.D.E.: cf. VI_A, to be made precise…

[^N.D.E-XVIII-10]: N.D.E.: We have introduced the numbering 3.0.1 and 3.0.2.

[^XVIII-3-1]: In the sense explained in 3.0.1; one could also replace these opens by the domains of definition (cf. 1.5)
    of the rational maps in question.

[^N.D.E-XVIII-11]: N.D.E.: The following sentence has been added.

[^N.D.E-XVIII-12]: N.D.E.: We have added the numbering 3.2.1, as well as 3.2.2.

[^N.D.E-XVIII-13]: N.D.E.: to be made precise…

[^XVIII-3-2]: combining Exp. VI_A, 1.1.1 and EGA IV₄, 17.16.2.

[^N.D.E-XVIII-14]: N.D.E.: If $X$ is smooth, separated over $S$, faithfully flat of finite presentation over $S$, then
    $G/S$ is representable by an $S$-group scheme smooth and of finite type over $S$. This is Theorem 6.6.1 of the book
    *Néron models* of Bosch–Lütkebohmert–Raynaud, Springer (1990).

[^N.D.E-XVIII-15]: N.D.E.: Another way to conclude here is by faithfully flat descent (EGA IV₂, 2.7.1), since $\beta$ is
    fppf-covering.

[^XVIII-3-3]: cf. note at the bottom of page 15, Exp. VII.
