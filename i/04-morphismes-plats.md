# Exposé IV. Flat Morphisms

<!-- label: IV -->

<!-- original page 87 -->

Here we give above all the flatness properties that were used in the preceding exposés. A more detailed study will be
found in Chapter IV of the Éléments de Géométrie Algébrique in preparation,[^iv-0-1] where the following situation is
studied systematically: $X$ locally of finite type over locally noetherian $Y$, and $\mathcal{F}$ coherent on $X$ and
$Y$-flat; one seeks relations among the properties of $Y$, those of $\mathcal{F}$, and those of the coherent sheaves
induced by $\mathcal{F}$ on the fibers of $X \to Y$, especially from the viewpoints of dimension, cohomological
dimension, depth, etc. There is in particular a systematic way of obtaining theorems of **Seidenberg** or **Bertini**
type, for hyperplane sections. The essential result for applying flatness methods in this context is the following,
proved below: if $Y$ is integral, $X$ of finite type over $Y$, and $\mathcal{F}$ coherent on $X$, then there exists a
nonempty open $U$ of $Y$ such that $\mathcal{F}$ is $Y$-flat at the points of $X$ lying over $U$. A second, no doubt
still more important, way in which flatness enters algebraic geometry is **descent theory**: see, for example,
Grothendieck's two exposés on the subject in the Bourbaki seminar,[^iv-0-2] and Exposés VIII and IX below. Flatness thus
seems to be one of the central technical notions in algebraic geometry.

Recall that the notion of flatness and faithful flatness was introduced by Serre in GAGA. An exposition of the following
numbers IV.1 and IV.2 is also found in Bourbaki's _Algèbre Commutative_, which of course, as the title of the book
indicates, is not restricted to commutative base rings.[^iv-0-3]

Contrary to the preceding exposés, we do not suppose that the rings under consideration are necessarily noetherian.

## 1. Sorites on Flat Modules

<!-- label: IV.1 -->

A module $M$ over a ring $A$ is said to be **flat**, or $A$-flat if one wants to specify $A$, if the functor

```text
T_M: N ↦ M ⊗_A N
```

which is in any case right exact, is **exact**, i.e. transforms monomorphisms into monomorphisms. Equivalently, the
first right-derived functor, or all the right-derived functors, vanish; that is, one has

```text
Tor^A_1(M,N) = 0     for all N,
```

respectively

```text
Tor^A_i(M,N) = 0     for i > 0 and all N.
```

Since the $Tor_{i}$ commute with inductive limits, it is enough to verify these conditions for $N$ of finite type;
indeed, taking then a composition series of $N$ with monogenic quotients, it is enough to have

$$ Tor^{A}_{1}(M,N) = 0 $$

for $N$ monogenic, i.e. of the form $A/I$, where $I$ is an ideal of $A$. Note moreover that

```text
Tor^A_1(M,A/I) = 0  ⇔  I ⊗_A M → M = A ⊗_A M is injective,
```

as one sees from the exact sequence of Tor, taking into account that $Tor^{A}_{1}(M,A) = 0$. Thus $M$ flat is equivalent
to saying that for every ideal $I$, the natural homomorphism

```text
I ⊗_A M → IM
```

is an isomorphism. It is enough to verify this for $I$ of finite type; a fortiori it is enough to verify that the
functor $M \otimes -$ is exact on **modules of finite type**.

As always when one has an exact functor $T$, if for a subobject $N'$ of $N$ one identifies $T(N')$ with a subobject of
$T(N)$, then for two subobjects $N'$, $N''$ of $N$ one has

```text
T(N′ ∩ N″) = T(N′) ∩ T(N″),
T(N′ + N″) = T(N′) + T(N″).
```

A direct sum of flat modules, and a direct factor of a flat module, is flat. In particular, since $A$ is flat, a
**free** module, hence also a **projective** module, is flat. The tensor product of two flat modules is flat; and if $M$
is flat over $A$, then $M \otimes_{A} B$ is flat over $B$ for every base change $A \to B$, by associativity of the
tensor product and the fact that a composite of exact functors is exact. If $M$ is flat over $B$, and $B$ flat over $A$,
then $M$ is flat over $A$, for the same reason.

The exact sequence of Tor, plus the “commutativity” of Tor, gives:

**Proposition.**

<!-- label: IV.1.1 -->

Let

$$ 0 \to M' \to M \to M'' \to 0 $$

be an exact sequence of $A$-modules, with $M''$ flat. Then:

1. This sequence remains exact after tensoring by any $A$-module $N$.
1. $M$ is flat if and only if $M'$ is flat.

Thus one may say that, from the point of view of behavior under tensor products, flat modules are “as good” as free or
projective modules; in particular, the exact sequence of IV.1.1 is “as good” as if it split.

Let $S$ be a multiplicatively stable subset of $A$. Then $S^{-1}A$ is flat over $A$, because $S^{-1}A \otimes N =
S^{-1}N$ is an exact functor in $N$. If $M$ is $A$-flat, then $S^{-1}M = S^{-1}A \otimes M$ is $S^{-1}A$-flat; the
converse is true if $M \to S^{-1}M$ is an isomorphism, i.e. if the $s \in S$ are bijective on $M$, by transitivity of
flatness, since $S^{-1}A$ is flat over $A$. More generally, the case of a morphism of preschemes $X \to Y$ and a
quasi-coherent sheaf $\mathcal{F}$ on $X$ whose flatness relative to $Y$ one wants to study leads to the situation with
two rings.

**Proposition.**

<!-- label: IV.1.2 -->

Let $A \to B$ be a homomorphism of rings, let $M$ be a $B$-module, and let $T$ be a multiplicatively stable subset of
$B$.

1. If $M$ is $A$-flat, then $T^{-1}M$ is $A$-flat, hence also $S^{-1}A$-flat for every multiplicatively stable subset
   $S$ of $A$ mapping into $T$.
1. Conversely, if $M_{\mathfrak{n}}$ is flat over $A_{\mathfrak{n}}$ for every maximal ideal $\mathfrak{n}$ of $B$,
   equivalently over $A_{\mathfrak{m}}$ where $\mathfrak{m}$ is the prime ideal of $A$ inverse image of $\mathfrak{n}$,
   then $M$ is $A$-flat.

Indeed, there is the formula, functorial in the $A$-module $N$:

```text
T⁻¹M ⊗_A N = T⁻¹(M ⊗_A N),
```

for the two sides are functorially isomorphic to $T^{-1}B \otimes_{B} M \otimes_{B} N_{(B)}$, with $N_{(B)} = N
\otimes_{A} B$, by the associativity formulas for $\otimes$. It follows at once that if $M \otimes_{A} N$ is exact in
$N$, then the same is true of $T^{-1}M \otimes_{A} N$, as a composite of two exact functors; this gives (i). And (ii)
follows in the same way, since to verify exactness of a sequence of $B$-modules it is enough to verify exactness of the
localizations at all maximal ideals of $B$.

**Proposition.**

<!-- label: IV.1.3 -->

1. Let $M$ be a flat $A$-module. If $x \in A$ is not a zero-divisor in $A$, then it is not a zero-divisor in $M$. In
   particular, if $A$ is integral, $M$ is torsion-free.
1. Suppose $A$ is integral and that for every maximal ideal $\mathfrak{m}$ of $A$, $A_{\mathfrak{m}}$ is principal, for
   example $A$ is a Dedekind ring, or even a principal ideal domain. In order that the $A$-module $M$ be flat, it is
   necessary and sufficient that it be torsion-free.

For (i), note that homothety by $x$ on $M$ is obtained by tensoring homothety by $x$ on $A$ with $M$. For (ii), by
IV.1.2 (ii) one may already suppose $A$ principal. One must show that if $M$ is torsion-free, then for every ideal $I$
of $A$, the injection $I \to A$, tensored by $M$, is an injection. This means that the generator $x$ of $I$ is not a
zero-divisor in $M$, as required.

## 2. Faithfully Flat Modules

<!-- label: IV.2 -->

A functor $F$ from one category to another is said to be **faithful** if, for all $X$ and $Y$, the map
$\operatorname{Hom}(X,Y) \to \operatorname{Hom}(F(X),F(Y))$ is injective. If $F$ is an additive functor between additive
categories, this is equivalent to saying that $F(u) = 0$ implies $u = 0$, and this implies that $F(X) = 0$ implies $X =
0$. For $F$ to be **faithful and exact**, it is necessary and sufficient that the following condition hold: for every
sequence $M' \to M \to M''$ of morphisms in $\mathcal{C}$, the transformed sequence $F(M') \to F(M) \to F(M'')$ is exact
**if and only if** the original one is exact. Or again: $F$ is exact, and $F(X) = 0$ implies $X = 0$. To speak of
exactness, of course, the categories involved must be **abelian**.

Suppose one has a family $(M_{i})$ of nonzero objects of $\mathcal{C}$ such that every nonzero object of $\mathcal{C}$
has a subobject admitting a quotient isomorphic to some $M_{i}$. Then $F$ is faithful and exact if and only if $F$ is
exact and $F(M_{i}) \neq 0$ for all $i$. If $\mathcal{C}$ is the category of modules over a ring $A$, one may take for
$(M_{i})$, for example, the family of $A/\mathfrak{m}$, with $\mathfrak{m}$ running through the maximal ideals of $A$.
Indeed, every nonzero module admits a nonzero monogenic submodule, hence one isomorphic to $A/I$, with $I$ an ideal
$\neq A$, which by Krull admits a quotient $A/\mathfrak{m}$. From these sorites one deduces in particular:

**Proposition.**

<!-- label: IV.2.1 -->

Let $M$ be an $A$-module. The following conditions are equivalent:

1. The functor $M \otimes_{A} -$ is faithful and exact.
1. $M$ is flat, and $M \otimes_{A} N = 0$ implies $N = 0$.
1. $M$ is flat, and $M \otimes A/\mathfrak{m} \neq 0$ for every maximal ideal $\mathfrak{m}$ of $A$.
1. For every sequence of homomorphisms $N' \to N \to N''$, the sequence tensored by $M$ is exact if and only if the
   initial sequence is exact.

One then says that $M$ is a **faithfully flat** $A$-module. In particular, if $M$ is faithfully flat, then $N \to N'$ is
a monomorphism, epimorphism, or isomorphism if and only if the homomorphism obtained by tensoring by $M$ is one. A
faithfully flat module is **faithful**, since homothety by $f$ on $M$ is obtained by tensoring homothety by $f$ on $A$
with $M$.

As in IV.1, one sees the usual transitivity properties: the tensor product of two faithfully flat modules is faithfully
flat; if $M$ is faithfully flat over $A$, then $M \otimes_{A} B$ is faithfully flat over $B$ for every extension of the
base $A \to B$; if $B$ is an $A$-algebra faithfully flat over $A$ and $M$ is a faithfully flat $B$-module, then $M$ is a
faithfully flat $A$-module.

**Corollary.**

<!-- label: IV.2.2 -->

Let $A \to B$ be a local homomorphism of local rings, and let $M$ be a $B$-module of finite type. In order that $M$ be
faithfully flat over $A$, it is necessary and sufficient that it be flat over $A$ and nonzero.

This follows from criterion (i ter) and Nakayama. In particular, **for $B$ to be $A$-flat, it is necessary and
sufficient that it be faithfully $A$-flat**.

**Proposition.**

<!-- label: IV.2.3 -->

Let $A \to B$ be a homomorphism of rings, and let $M$ be a $B$-module faithfully flat over $A$. For every prime ideal
$\mathfrak{p}$ of $A$, there exists a prime ideal $\mathfrak{q}$ of $B$ inducing it.

Dividing by $\mathfrak{p}$, we are reduced to the case $\mathfrak{p} = 0$. Localizing at the prime ideal `0`, we are
reduced to the case where $A$ is a field. But $M$, being faithfully flat over $A$, is nonzero; a fortiori $B \neq 0$,
hence $B$ has a prime ideal, which can only induce the unique prime ideal of $A$. Geometrically, one may say that the
existence of a quasi-coherent sheaf $\mathcal{F}$ on $X = \operatorname{Spec}(B)$ that is “faithfully flat” relative to
$A$ implies that $X \to Y = \operatorname{Spec}(A)$ is **surjective**.

**Corollary.**

<!-- label: IV.2.4 -->

Suppose $M$ is flat over $A$, of finite type over $B$, and $Supp M = \operatorname{Spec}(B)$, i.e. $M_{\mathfrak{q}}
\neq 0$ for every prime ideal $\mathfrak{q}$ of $B$. Then the prime ideals $\mathfrak{q}$ of $B$ containing
$\mathfrak{p}B$ and minimal among such ideals induce $\mathfrak{p}$.

<!-- original page 92 -->

We are again reduced to the case $\mathfrak{p} = 0$, since all the hypotheses are preserved by dividing, hence $A$ is
integral. We are reduced to the following statement.

**Corollary.**

<!-- label: IV.2.5 -->

With $M$ as above, every minimal prime ideal $\mathfrak{q}$ of $B$ induces a prime ideal $\mathfrak{p}$ of $A$ that is
minimal.

Indeed, localizing at $\mathfrak{p}$ and $\mathfrak{q}$, we are reduced to proving that if $A$ and $B$ are local, $A \to
B$ is local, $M$ is a nonzero $B$-module flat over $A$, and $B$ has dimension `0`, then $A$ has dimension `0`. By IV.2.2
and IV.2.3, every prime ideal of $A$ is induced by a prime ideal of $B$, hence by the maximal ideal of $B$, and
therefore is the maximal ideal, as required. Geometrically, IV.2.5 means that every irreducible component of $X =
\operatorname{Spec}(B)$ dominates some irreducible component of $Y = \operatorname{Spec}(A)$, provided there exists a
quasi-coherent sheaf of finite type on $X$, with support $X$, and flat relative to $Y$.

Note that in IV.2.4 we did not have to suppose $M$ faithfully flat over $A$, but then nothing guarantees the existence
of a prime ideal containing $\mathfrak{p}B$, and hence of a minimal one among such ideals.

**Proposition.**

<!-- label: IV.2.6 -->

Let $i: A \to B$ be a homomorphism of rings. The following conditions are equivalent:

1. $B$ is a faithfully flat $A$-module.
1. $B$ is flat over $A$, and $\operatorname{Spec}(B) \to \operatorname{Spec}(A)$ is surjective.
1. $B$ is flat over $A$, and every maximal ideal is induced by an ideal of $B$.
1. $i$ is injective and `Coker i` is a flat $A$-module.
1. The functor $M_{(B)} = M \otimes_{A} B$ in the $A$-module $M$ is exact, and the canonical functorial homomorphism $M
   \to M_{(B)}$ is injective.
1. For every ideal $I$ of $A$, $I \otimes_{A} B \to IB$ is an isomorphism, and the inverse image of `IB` in $A$ is equal
   to $I$.

We have (i) ⇒ (ii) by IV.2.3; (ii) ⇒ (ii bis) is trivial; (ii bis) ⇒ (i) by criterion (i ter) of IV.2.1. We have (iii) ⇒
(iv) by IV.1.1; (iv) ⇒ (iv bis) trivially, taking $M = A/I$ in the second condition (iv bis); and (iv bis) ⇒ (i) by the
flatness criterion by ideals seen at the beginning of IV.1 and by criterion IV.2.1 (i ter). Finally, (iv) ⇒ (iii) by an
easy converse of IV.1.1, and (i) ⇒ (iv), because if $N$ is the kernel of $M \to M \otimes_{A} B = T(M)$, then, since $T$
is exact, $N \to T(N)$ is zero; hence $T(N) = N \otimes_{A} B = 0$, whence $N = 0$.

## 3. Relations with Completion

<!-- label: IV.3 -->

Let $A$ be a noetherian ring, let $I$ be an ideal in $A$, let `Â` be the separated completion of $A$ for the $I$-preadic
topology, and for every $A$-module $M$, let $\hat{M}$ be its completion for the $I$-preadic topology. This is an
`Â`-module, whence a canonical homomorphism

```text
M ⊗_A Â → M̂.
```

When $M$ ranges over **modules of finite type**, the functor $M \mapsto \hat{M}$ is exact, as follows easily from
**Krull's theorem: if $N \subset M$, then the topology of $N$ is the one induced by the topology of $M$**. Since $M
\otimes_{A} \hat{A}$ is right exact, one easily concludes, by resolving $M$ by $L \to L' \to M$ with $L$ and $L'$ free
of finite type, that the functorial homomorphism above is an **isomorphism**, since $\hat{M}$ is also right exact, and
consequently that $M \otimes_{A} \hat{A}$ is also an **exact** functor in $M$. Therefore:

**Proposition.**

<!-- label: IV.3.1 -->

Let $A$ be a noetherian ring and $I$ an ideal of $A$. Then the separated completion `Â` of $A$, for the $I$-preadic
topology, is **flat** over $A$.

**Corollary.**

<!-- label: IV.3.2 -->

In order that `Â` be faithfully flat over $A$, it is necessary and sufficient that $I$ be contained in the radical of
$A$.

Indeed, it suffices to apply criterion IV.2.1 (i ter).

These results summarize all that can be said, from the viewpoint of linear algebra, about the relations between $A$ and
`Â`. Corollary IV.3.2 is used especially when $A$ is a noetherian local ring and $I$ is contained in the maximal ideal
$\mathfrak{m}$, and most often is equal to it.

## 4. Relations with Free Modules

<!-- label: IV.4 -->

**Proposition.**

<!-- label: IV.4.1 -->

Let $A$ be a ring, let $I$ be an ideal of $A$, and let $M$ be an $A$-module. Suppose one is under one or the other of
the following hypotheses:

1. $I$ is nilpotent.
1. $A$ is noetherian, $I$ lies in the radical of $A$, and $M$ is of finite type.

In order that $M$ be free over $A$, it is necessary and sufficient that $M \otimes A/I$ be free over $A/I$ and that
$Tor^{A}_{1}(M,A/I) = 0$.

This is necessary. We prove the sufficiency. Let $(e_{i})$ be a family of elements of $M$ whose image in $M \otimes A/I
= M/IM$ defines a basis there over $A/I$; it is a finite family in case (b). Let $L$ be the free $A$-module constructed
on the same index set. Thus there is a homomorphism $L \to M$ such that tensoring $T$ by $A/I$ induces an isomorphism
$T(L) \to T(M)$. If $Q$ is the cokernel of $L \to M$, then $T(Q) = 0$, whence $Q = 0$ by Nakayama, valid under either
condition (a) or (b). Thus $L \to M$ is surjective. Let $R$ be its kernel. We then have an exact sequence

$$ 0 \to R \to L \to M \to 0, $$

whence, since $Tor^{A}_{1}(M,A/I) = 0$, an exact sequence $0 \to T(R) \to T(L) \to T(M) \to 0$, whence $T(R) = 0$, and
hence $R = 0$ again by Nakayama, taking into account that in case (b), $R$ is of finite type because $A$ was assumed
noetherian.

**Corollary.**

<!-- label: IV.4.2 -->

One may replace the condition $Tor^{A}_{1}(M,A/I) = 0$ by: the canonical surjective homomorphism

```text
gr_I^0(M) ⊗_{A/I} gr_I(A) → gr_I(M)
```

<!-- label: eq:IV.2.* -->

is an isomorphism.

Indeed, if $M$ is free, this is certainly verified. Thus one must prove that if $M \otimes A/I$ is free over $A/I$ and
the condition on the associated graded objects is verified, then $M$ is free. Resume the proof above by constructing $L
\to M$. The hypothesis implies that this homomorphism induces an isomorphism on associated graded objects; hence its
kernel is contained in the intersection of the $I^{nL}$, and so is zero, trivially in (a), and by a well-known fact in
(b). This proves the assertion.

**Corollary.**

<!-- label: IV.4.3 -->

Suppose $A/I$ is a field. Then the following conditions on $M$ are equivalent:

1. $M$ is free.
1. $M$ is projective.
1. $M$ is flat.
1. $Tor^{A}_{1}(M,A/I) = 0$.
1. The canonical homomorphism IV.4.2 is bijective.

Indeed, in the case considered, $M \otimes A/I$ is automatically free.

The preceding result is valid in the following two cases:

1. $M$ is an **arbitrary** module over a local ring $A$ whose maximal ideal $I$ is **nilpotent**, for example an
   artinian local ring.
1. $M$ is a module **of finite type** over a **noetherian local** ring.

Recall, for reference:

**Corollary.**

<!-- label: IV.4.4 -->

<!-- original page 95 -->

Suppose $A$ is a **noetherian local integral** ring with maximal ideal $\mathfrak{m} = I$, residue field $k = A/I$, and
field of fractions $K$. Let $M$ be a module of finite type over $A$. Then the preceding equivalent conditions (i) to (v)
are also equivalent to:

1. $M \otimes_{A} K$ and $M \otimes_{A} k$ are vector spaces of the same dimension, i.e. the rank of $M$ over $A$ is
   equal to the minimum number of generators of the $A$-module $M$.

The proof is immediate. We leave it to the reader to generalize to the case where $A$ is only assumed to have no
nilpotent elements; one must then require that the ranks of $M$ at the minimal prime ideals of $A$ be equal to the
dimension of the vector space $M \otimes_{A} k$.

## 5. Local Flatness Criteria

<!-- label: IV.5 -->

**Proposition.**

<!-- label: IV.5.1 -->

Let $A$ be a ring equipped with an ideal $I$, and let $M$ be an $A$-module. Suppose

$$ Tor^{A}_{1}(M,A/I^{n}) = 0 for n > 0. $$

Then the canonical surjective homomorphism

```text
gr_I^0(M) ⊗_{A/I} gr_I(A) → gr_I(M)
```

<!-- label: eq:IV.5.1.* -->

is an isomorphism. The converse is true if $I$ is nilpotent.

The hypothesis means that the homomorphisms

```text
I^n ⊗_A M → I^nM
```

are isomorphisms, whence at once the fact that the homomorphisms

```text
I^n/I^{n+1} ⊗_A M → I^nM/I^{n+1}M
```

are isomorphisms. Conversely, suppose this condition holds and $I$ is nilpotent. We prove $Tor^{A}_{1}(M,A/I^{n}) = 0$
for every $n$. This is true for large $n$, so proceed by descending induction on $n$, supposing it proved for $n + 1$.
We have a commutative diagram

```text
        M ⊗ I^{n+1}  →  M ⊗ I^n  →  M ⊗ (I^n/I^{n+1})  →  0
              ↓              ↓                 ↓
0  →       MI^{n+1}  →      MI^n  →       MI^n/MI^{n+1} →  0
```

whose rows are exact. By hypothesis, the last vertical arrow is an isomorphism, and the induction hypothesis also means
that the first vertical arrow is one. The same is therefore true of the middle vertical arrow, which completes the
proof.

The following proposition was isolated by Serre at the time of the Seminar; it allows substantial simplifications in the
present number.

**Proposition.**

<!-- label: IV.5.2 -->

Let $A \to B$ be a homomorphism of rings, and let $M$ be an $A$-module. The following conditions are equivalent:

1. For every $B$-module $N$, one has $Tor^{A}_{1}(M,N) = 0$.
1. $Tor^{A}_{1}(M,B) = 0$, and $M_{(B)} = M \otimes_{A} B$ is $B$-flat.

There is a functorial isomorphism

```text
M ⊗_A N = (M ⊗_A B) ⊗_B N,
```

which expresses the left-hand side, regarded as a functor in $M$, as a composite of two functors $M \mapsto M
\otimes_{A} B$ and $P \mapsto P \otimes_{B} N$. Since the first sends free $A$-modules to free $B$-modules, hence
projectives to projectives, one has the spectral sequence for composite functors

```text
Tor^A_n(M,N) ⇐ Tor^B_p(Tor^A_q(M,B),N),
```

whence an exact sequence in low degrees

```text
0 ← Tor^B_1(M ⊗_A B,N) ← Tor^A_1(M,N) ← Tor^A_1(M,B) ⊗_A N.
```

If (i) holds, then from this exact sequence one concludes $Tor^{B}_{1}(M \otimes_{A} B,N) = 0$ for every $N$, i.e. $M
\otimes_{A} B$ is $B$-flat, hence (ii). Conversely, if (ii) holds, then in the exact sequence the terms surrounding
$Tor^{A}_{1}(M,N)$ are zero, hence (i) holds.

**Corollary.**

<!-- label: IV.5.3 -->

Suppose $B = A/I$. Then the preceding conditions are equivalent to:

1. $Tor^{A}_{1}(M,N) = 0$ for every $A$-module $N$ annihilated by a power of $I$.

Indeed, (i) means that this holds if $N$ is annihilated by $I$. One deduces (iii) by applying the hypothesis to the
$I^{nN}/I^{n+1}N$.

**Corollary.**

<!-- label: IV.5.4 -->

Under the conditions of IV.5.3, the conditions under consideration imply that the functorial homomorphism

```text
gr_I^0(M) ⊗_{A/I} gr_I(A) → gr_I(M)
```

<!-- label: eq:IV.5.* -->

is an isomorphism, and that $M \otimes_{A} A/I$ is flat over $A/I$.

It suffices to apply (iii) and IV.5.1. Using the converse of IV.5.1 when $I$ is nilpotent, one finds:

**Corollary.**

<!-- label: IV.5.5 -->

Let $A$ be a ring equipped with a nilpotent ideal $I$, and let $M$ be an $A$-module. The following conditions are
equivalent:

1. $M$ is $A$-flat.
1. $M \otimes_{A} A/I$ is $A/I$-flat, and $Tor^{A}_{1}(M,A/I) = 0$.
1. $M \otimes_{A} A/I$ is $A/I$-flat, and the canonical homomorphism $IV.5.*$ on associated graded objects is an
   isomorphism.

Indeed, these are respectively the preceding conditions (iii) and (ii), and those of Corollary IV.5.4.

No longer suppose $I$ nilpotent. Then in IV.5.5 one will only have a priori the implications (i) ⇒ (ii) ⇒ (iii). On the
other hand, since condition (iii) remains stable after dividing by a power of $I$, one sees by IV.5.5 that it implies:

1. **For every integer $n$, $M \otimes A/I^{n}$ is flat over $A/I^{n}$.**

We propose to give conditions under which one can conclude (i), i.e. that $M$ is $A$-flat. I say that it suffices for
this that $A$ be noetherian and that $M$ satisfy the following finiteness condition: **for every module $N$ of finite
type over $A$, $M \otimes_{A} N$ is separated for the $I$-preadic topology**. It would suffice to verify this when $N$
is an ideal of finite type in $A$. Indeed, let us prove that under these conditions, if $N' \to N$ is a monomorphism of
finite-type modules, then $M \otimes_{A} N' \to M \otimes_{A} N$ is a monomorphism. It is enough to show that the kernel
is contained in the

```text
I^n(M ⊗_A N′) = Im(M ⊗_A I^nN′ → M ⊗_A N′),
```

or again in the

```text
Im(M ⊗_A V′_n → M ⊗_A N′) = Ker(M ⊗_A N′ → M ⊗_A (N′/V′_n)),
```

where $V'_{n}$ runs through a countable fundamental system of neighborhoods of `0` in $N'$, endowed with its $I$-adic
topology. By Krull's theorem, the $I$-adic topology of $N'$ is induced by that of $N$, so one may take $V'_{n} = N' \cap
I^{nN}$. Consider then the commutative diagram

```text
M ⊗_A N′          →  M ⊗_A (N′/V′_n)
↓                    ↓
M ⊗_A N           →  M ⊗_A (N/I^nN).
```

<!-- original page 98 -->

Since $N'/V'_{n}$ and $N/I^{nN}$ are annihilated by $I^{n}$, the second vertical homomorphism identifies with the one
obtained from the **injective** homomorphism $N'/V'_{n} \to N/I^{nN}$ by tensoring over $A/I^{n}$ with the **flat**
$A/I^{n}$-module $M \otimes_{A} A/I^{n}$; it is therefore **injective**. Consequently, the kernel of $M \otimes_{A} N'
\to M \otimes_{A} N$ is contained in the kernel of $M \otimes_{A} N' \to M \otimes_{A} (N'/V'_{n})$, which is what was
required.

The “finiteness” condition considered for $M$ is satisfied in particular if $M$ is a module of finite type over a
noetherian $A$-algebra $B$ such that `IB` is contained in the radical of $B$: indeed, then $M \otimes_{A} N$ is a module
of finite type over $B$ for every module $N$ of finite type over $A$, hence is separated by Krull for the $I$-adic
topology, which is its `IB`-adic topology. Thus one obtains:

**Theorem.**

<!-- label: IV.5.6 -->

Let $A \to B$ be a homomorphism of noetherian rings, let $I$ be an ideal of $A$ such that `IB` is contained in the
radical of $B$, and let $M$ be a $B$-module of finite type. The following conditions are equivalent:

1. $M$ is $A$-flat.
1. $M \otimes_{A} A/I$ is $A/I$-flat, and $Tor^{A}_{1}(M,A/I) = 0$.
1. $M \otimes_{A} A/I$ is $A/I$-flat, and the canonical homomorphism

```text
gr_I^0(M) ⊗_{A/I} gr_I(A) → gr_I(M)
```

is an isomorphism. 4. For every integer $n$, $M \otimes_{A} A/I^{n}$ is flat over $A/I^{n}$.

This result applies especially when $A$ and $B$ are **local** noetherian rings, $A \to B$ a local homomorphism, and $I$
an ideal of $A$ contained in its maximal ideal; and one can immediately reduce IV.5.6 to this case. An interesting case
is that where $A/I$ is a field, i.e. $I$ is maximal; then the condition that $M \otimes_{A} A/I$ be flat over $A/I$
becomes superfluous. Moreover, since the $A/I^{n}$ are artinian local rings, condition (iv) means that the $M
\otimes_{A} A/I^{n}$ are **free** over the $A/I^{n}$.

**Corollary.**

<!-- label: IV.5.7 -->

Let $A \to B$ be a local homomorphism of noetherian local rings, and let $u: M' \to M$ be a homomorphism of $B$-modules
of finite type. Suppose $M$ is flat over $A$. Then the following conditions are equivalent:

1. $u$ is injective, and `Coker u` is flat over $A$.
1. $u \otimes_{A} k: M' \otimes_{A} k \to M \otimes_{A} k$ is injective,

where $k$ denotes the residue field of $A$.

(i) ⇒ (ii) by IV.1.1. We prove the converse. First, $u$ is injective, for it suffices to verify this on associated
graded objects, where it follows from a commutative square that the reader will write. Let $M''$ be its cokernel. We
then have an exact sequence

$$ 0 \to M' \to M \to M'' \to 0. $$

By the exact sequence of Tor, taking into account hypothesis (ii) and $Tor^{A}_{1}(M,k) = 0$, we get $Tor^{A}_{1}(M'',k)
= 0$; hence $M''$ is flat over $A$ by Theorem IV.5.6.

**Corollary.**

<!-- label: IV.5.8 -->

Under the conditions of IV.5.6, let $J$ be an ideal of $B$ containing `IB` and contained in the radical. Let `Â` be the
$I$-adic completion of $A$, and let $\hat{B}$ and $\hat{M}$ be the $J$-adic completions of $B$ and $M$. In order that
$M$ be $A$-flat, it is necessary and sufficient that $M$ be `Â`-flat.

The sufficiency would already follow easily from IV.3.2. One uses criterion (iii) of IV.5.6 in the situation $(A,B,I,M)$
and in the situation $(\hat{A},\hat{B},I\hat{A},\hat{M})$. One observes that the conditions obtained in the two cases
are equivalent by IV.3.2.

**Corollary.**

<!-- label: IV.5.9 -->

Let $A \to B \to C$ be local homomorphisms of noetherian local rings, and let $M$ be a $C$-module of finite type. Here
$C$ occurs only so that a finiteness condition can be placed on $M$. Suppose $B$ is flat over $A$. Let $k$ be the
residue field of $A$. The following conditions are equivalent:

1. $M$ is flat over $B$.
1. $M$ is flat over $A$, and $M \otimes_{A} k$ is flat over $B \otimes_{A} k$.

The implication (i) ⇒ (ii) is trivial. We prove (ii) ⇒ (i). Apply criterion (iii) of IV.5.6 to $(B,C,\mathfrak{m}B =
I,M)$. Since

```text
M ⊗_B (B/I) = M ⊗_B (B ⊗_A k) = M ⊗_A k,
```

the first condition of this criterion says precisely that $M \otimes_{A} k$ is flat over $B \otimes_{A} k$. The second
condition of the criterion is satisfied because $M$ is flat over $A$ and $B$ is flat over $A$, by an associativity
formula for the tensor product. Of course, referring to IV.5.5 instead of IV.5.6, one obtains an analogous statement
without noetherian and finiteness assumptions, when one supposes instead that the ideal $\mathfrak{m}$ of $A$ is
nilpotent. The fact that $\mathfrak{m}$ was taken maximal did not enter; but in a sense the case “$\mathfrak{m}$
maximal” is “the best possible”.

## 6. Flat Morphisms and Open Sets

<!-- label: IV.6 -->

Recall first some results on constructible sets, which are proved in circulating notes from the Dieudonné-Rosenlicht
Seminar on Schemes.[^iv-6-0-1]

Let $X$ be a topological space. Following Chevalley, a subset of $X$ is called **constructible** if it is a finite union
of locally closed subsets.

**Lemma.**

<!-- label: IV.6.1 -->

Let $X$ be a noetherian topological space, and let $Z$ be a subset of $X$. In order that $Z$ be constructible, it is
necessary and sufficient that for every irreducible closed subset $Y$ of $X$, $Z \cap Y$ is nondense in $Y$ or contains
a nonempty open subset of the space $Y$.

One deduces from this, using a well-known lemma of commutative algebra:

**Lemma (Chevalley).**

<!-- label: IV.6.2 -->

Let $f: X \to Y$ be a morphism of finite type of preschemes, with $Y$ noetherian. Then $f(X)$ is constructible.

**Lemma.**

<!-- label: IV.6.3 -->

Let $X$ be a noetherian topological space in which every irreducible closed subset admits a generic point, let $U$ be a
constructible subset of $X$, and let $x \in X$. In order that $U$ be a neighborhood of $x$, it is necessary and
sufficient that every generization $y$ of $x$, i.e. every $y \in X$ such that $x \in closure(y)$, belongs to $U$.

In particular:

**Corollary.**

<!-- label: IV.6.4 -->

Let $X$ be a noetherian topological space in which every irreducible closed subset admits a generic point, and let $U$
be a subset of $X$. In order that $U$ be open, it is necessary and sufficient that it satisfy the following two
conditions:

1. $U$ contains every generization of each of its points.
1. If $x \in U$, then $U \cap closure(x)$ contains a nonempty open subset of the space $closure(x)$.

Indeed, $U$ is necessarily constructible by IV.6.1, and one applies criterion IV.6.2, which proves that $U$ is a
neighborhood of each of its points.

**Corollary.**

<!-- label: IV.6.5 -->

Let $f: X \to Y$ be a morphism of finite type of preschemes, with $Y$ locally noetherian, let $x$ be a point of $X$, and
let $y = f(x)$. In order that $f$ transform every neighborhood of $x$ into a neighborhood of $y$, it is necessary and
sufficient that for every generization $y'$ of $y$, there exist a generization $x'$ of $x$ such that $f(x') = y'$.

We may evidently suppose $X$ and $Y$ affine, hence noetherian. The condition is sufficient, for it is enough to prove
that $f(X)$ is a neighborhood of $y$; but $f(X)$ is constructible by IV.6.1, and it suffices to apply criterion IV.6.3.
The condition is necessary: let $Y' = closure(y')$, and let $F$ be the union of the irreducible components of
$f^{-1}(Y')$ that do not contain $x$. Then $X - F$ is an open neighborhood of $x$, so its image is a neighborhood of
$y$, and a fortiori contains $y'$. Thus there exists $x'_{1} \in X - F$ such that $f(x'_{1}) = y'$. Consider an
irreducible component of $f^{-1}(Y')$ containing $x'_{1}$; it necessarily contains $x$

otherwise it would be contained in $F$. Let $x'$ be its generic point. This is a generization of $x$, and $f(x')$ is a
generization of $f(x'_{1}) = y'$ contained in $Y'$, hence is equal to $y'$, as required.

**Theorem.**

<!-- label: IV.6.6 -->

Let $f: X \to Y$ be a morphism locally of finite type, with $Y$ locally noetherian, and let $F$ be a coherent sheaf on
$X$ with support $X$, flat relative to $Y$. Then $f$ is an open morphism, i.e. transforms open sets into open sets.

It suffices to prove criterion IV.6.5 for every point $x \in X$. The generizations $x'$ of $x$ correspond to the prime
ideals of $\mathcal{O}_{x}$, those $y'$ of $y$ correspond to the prime ideals of $\mathcal{O}_{y}$, and therefore one
must verify that every prime ideal of $\mathcal{O}_{y}$ is induced by a prime ideal of $\mathcal{O}_{x}$. But $F_{x}$ is
a nonzero $\mathcal{O}_{x}$-module, flat over $\mathcal{O}_{y}$, hence faithfully flat over $\mathcal{O}_{y}$ by IV.2.2.
We may therefore apply IV.2.3, which completes the proof.

**Remarks.** Since flatness is preserved under extension of the base, one sees that under the conditions of IV.6.5, $f$
is even **universally open**. I do not know, however, when $Y$ is integral and $X$ is of finite type over $Y$, whether
$f$ induces on every component $X_{i}$ of $X$ an open morphism, or even only an equidimensional one,[^iv-6-6-1] i.e. one
whose fiber components all have the same dimension; one only knows that $X_{i}$ **dominates** $Y$. The question is
related to the following one: let $A \to B$ be a local homomorphism of noetherian local rings, such that $B$ is flat
over $A$ and $\mathfrak{m}B$ is an ideal of definition of $B$, which implies moreover $\dim B = \dim A$. Is it true that
for every minimal prime ideal $\mathfrak{p}_{i}$ of $B$ one has $\dim B/\mathfrak{p}_{i} = \dim B$? Let us only point
out that the answer to the first question is negative if one replaces the flatness hypothesis of IV.6.5 by the sole
hypothesis that $f$ is universally open.

**Lemma.**

<!-- label: IV.6.7 -->

Let $A$ be a noetherian integral ring, let $B$ be an $A$-algebra of finite type, and let $M$ be a $B$-module of finite
type. Then there exists a nonzero element $f$ of $A$ such that $M_{f}$ is a free, a fortiori flat, module over $A_{f}$.

Let $K$ be the field of fractions of $A$. Then $B \otimes_{A} K$ is an algebra of finite type over $K$, and $M
\otimes_{A} K$ is a module of finite type over it. Let $n$ be the dimension of the support of this module; we argue by
induction on $n$. If $n < 0$, i.e. if $M \otimes_{A} K = 0$, then taking a finite set of generators of $M$ over $B$, one
sees that there exists $f \in A$ annihilating these generators, hence annihilating $M$; thus $M_{f} = 0$, and we are
done. Suppose $n \geq 0$. We know that the $B$-module $M$ admits a composition series whose successive quotients are
isomorphic to modules $B/\mathfrak{p}_{i}$, with $\mathfrak{p}_{i}$ prime ideals of $B$. Since an extension of free
modules is free, we are reduced to the case where $M$ itself is of the form $B/\mathfrak{p}$, or again identical with
$B$, with $B$ an **integral** $A$-algebra. Applying Noether's normalization lemma to the $K$-algebra $B \otimes_{A} K$,
one sees easily that there exists a nonzero element $f$ of $A$ such that $B_{f}$ is integral over the subring
$A_{f}[t_{1},...,t_{n}]$, where the $t_{i}$ are indeterminates. Thus we may already suppose $B$ is integral over $C =
A[t_{1},...,t_{n}]$; it is then a finite torsion-free $C$-module. Let $m$ be its rank. There is therefore an exact
sequence of $C$-modules

$$ 0 \to C^{m} \to B \to M' \to 0 $$

where $M'$ is a torsion $C$-module. It follows that the Krull dimension of the $C \otimes_{A} K$-module $M' \otimes_{A}
K$ is strictly less than the dimension $n$ of $C \otimes_{A} K$. By the induction hypothesis, after localizing with
respect to a suitable nonzero $f$ of $A$, we may suppose that $M'$ is a free $A$-module. On the other hand, $C^{m}$ is a
free $A$-module. Hence $B$ is then a free $A$-module, and we are done.

**Lemma.**

<!-- label: IV.6.8 -->

Let $A$ be a noetherian ring, $B$ an algebra of finite type over $A$, $M$ a $B$-module of finite type, $\mathfrak{p}$ a
prime ideal of $B$, and $\mathfrak{q}$ the prime ideal it induces on $A$. Suppose $M_{\mathfrak{p}}$ is flat over
$A_{\mathfrak{q}}$, equivalently over $A$. Then there exists $g \in B - \mathfrak{p}$ such that:

1. $(M/\mathfrak{q}M)_{g}$ is flat over $A/\mathfrak{q}$.
1. $Tor^{A}_{1}(M,A/\mathfrak{q})_{g} = 0$.

Indeed, applying IV.6.7 to $(A/\mathfrak{q}, B/\mathfrak{q}B, M/\mathfrak{q}M)$, one first sees that there exists $f$ in
$A - \mathfrak{q}$ such that $(M/\mathfrak{q}M)_{f}$ is flat over $A/\mathfrak{q}$. On the other hand, since
$M_{\mathfrak{p}}$ is flat over $A$, we have

$$ Tor^{A}_{1}(M,A/\mathfrak{q})_{\mathfrak{p}} = Tor^{A}_{1}(M_{\mathfrak{p}},A/\mathfrak{q}) = 0. $$

Since $Tor^{A}_{1}(M,A/\mathfrak{q})$ is a $B$-module of finite type, there exists $g \in B - \mathfrak{p}$ such that
(b) holds. Replacing $g$ by `gf`, we may then suppose that (a) also holds, which proves the corollary.

**Corollary.**

<!-- label: IV.6.9 -->

With the notation of IV.6.8, for every prime ideal $\mathfrak{p}'$ of $B$ containing $\mathfrak{p}$ and not containing
$g$, $M_{\mathfrak{p}'}$ is flat over $A$, equivalently over $A_{\mathfrak{q}'}$, where $\mathfrak{q}'$ is the prime
ideal of $A$ induced by $\mathfrak{p}'$.

It suffices to apply criterion IV.5.6 (ii) to the system $(A, B_{\mathfrak{q}'}, \mathfrak{q}, M_{\mathfrak{q}'})$,
using localization of Tor.

**Theorem.**

<!-- label: IV.6.10 -->

Let $f: X \to Y$ be a morphism of finite type, with $Y$ locally noetherian, and let $F$ be a coherent sheaf on $X$. Let
$U$ be the set of points $x \in X$ such that $F_{x}$ is flat over $\mathcal{O}_{f(x)}$. Then $U$ is an **open** set.

**Proof.** We may suppose $X$ and $Y$ affine, with rings $B$ and $A$, so $F$ is defined by a $B$-module $M$ of finite
type. We apply criterion IV.6.4. Condition (a) is trivially verified by IV.1.2 (i); it remains to verify condition (b)
of IV.6.4. This is what was done in Lemma IV.6.8 and Corollary IV.6.9.

In many questions, the following weaker form of Theorem IV.6.10 is sufficient; it already follows from Lemma IV.6.7, and
therefore requires neither the technique of constructible sets nor Theorem IV.5.6.

**Corollary.**

<!-- label: IV.6.11 -->

Under the conditions of IV.6.10, if one supposes $Y$ integral, then there exists a nonempty open $V$ in $Y$ such that
$F$ is flat relative to $Y$ at all points of $f^{-1}(V)$.

Indeed, the open set $U$ contains the fiber of the generic point of $Y$, since the local ring of this point is a field;
hence it contains an open set of the form $f^{-1}(V)$, since $X$ is of finite type over $Y$. From IV.6.11 one also
easily concludes the following result, where $Y$ is supposed noetherian but not necessarily integral: there exists a
partition of $Y$ into locally closed subsets $Y_{i}$ such that, giving $Y_{i}$ the induced reduced structure, $F$
induces on each $X_{i} = X \times_{Y} Y_{i}$ a sheaf flat relative to $Y_{i}$.

<!-- end of Exposé IV source block: next chapter begins at smf_doc-math_3_01.tex line 7383 -->

[^iv-0-1]: Cf. EGA IV 11 and 12.

[^iv-0-2]: And, for a more detailed exposition, Exposés VIII and IX below.

[^iv-0-3]: N. Bourbaki, _Algèbre Commutative_, Chap. I, Modules plats, Act. Sci. Ind. 1290, Paris, Hermann, 1961.

[^iv-6-0-1]: Cf. EGA 0_III 9, EGA IV 1.8 and 1.10.

[^iv-6-6-1]: The answer to the second question is affirmative, and to the first negative even if $f$ is étale; cf. EGA
    IV 12.1.1.5 and EGA Err_IV 33.
