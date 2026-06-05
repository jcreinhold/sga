# Exposé VIII. Faithfully Flat Descent

<!-- label: VIII -->

<!-- original page 195 -->

## 1. Descent of Quasi-Coherent Modules

<!-- label: VIII.1 -->

Let `Sch` be the category of preschemes. Proceeding as in VI.11.b, one finds that the category of pairs $(X,F)$, where
$X$ is a prescheme and $F$ is a Module on $X$, with morphisms defined as there by means of the notion of direct image of
a Module by a morphism of ringed spaces, can be regarded as a fibered category over `Sch`. The base-change functor
relative to a morphism $f: X \to Y$ in `Sch` is the inverse-image functor of Modules by $f$. Note that the fiber
category at $X \in Ob(Sch)$ of the preceding fibered category is the category **opposite** to the category of Modules on
$X$.

Since the inverse image of a quasi-coherent Module is quasi-coherent, the full subcategory of the category of pairs
$(X,F)$, formed by the pairs for which $F$ is quasi-coherent, is a fibered subcategory of the preceding fibered
category. By contrast, if no hypotheses are made on $f$, the direct image of a quasi-coherent Module is not in general a
quasi-coherent Module. We shall simply call this fibered category the **fibered category of quasi-coherent Modules on
preschemes**.

Recall, on the other hand, that a morphism $f: X \to Y$ of ringed spaces is said to be **faithfully flat** if it is
**flat**, i.e. for every $x \in X$, $\mathcal{O}_{X,x}$ is a flat module over $\mathcal{O}_{Y,f(x)}$, cf. IV, and
**surjective**. One says that $f$ is a **quasi-compact** morphism if the inverse image by $f$ of every quasi-compact
subset is quasi-compact. When $f$ is a morphism of preschemes, this also means that the inverse image by $f$ of an
affine open subset of $Y$ is a **finite** union of affine open subsets of $X$.

**Theorem.**

<!-- label: VIII.1.1 -->

<!-- original page 196 -->

Let $\mathcal{F}$ be the fibered category of quasi-coherent Modules on preschemes. Let $g: S' \to S$ be a faithfully
flat and quasi-compact morphism of preschemes. Then $g$ is a morphism of effective $\mathcal{F}$-descent.

Recall[^viii-1-1] that this means two things:

**Corollary. Descent of Homomorphisms of Modules.**

<!-- label: VIII.1.2 -->

Let $g: S' \to S$ be a faithfully flat and quasi-compact morphism of preschemes; let $F$ and $G$ be two quasi-coherent
Modules on $S$; let $F'$ and $G'$ be their inverse images on $S'$; and finally let $F''$ and $G''$ be their inverse
images on $S'' = S' \times_{S} S'$. Consider the diagram of maps of sets defined by the base-change functors by $g$,
$p_{1}$, $p_{2}$, where `p₁,p₂: S′ ×_S S′ ⇉ S′` are the two projections:

```text
Hom_S(F,G) → Hom_{S′}(F′,G′) ⇉ Hom_{S″}(F″,G″).
```

This diagram is exact, i.e. it defines a bijection from the first set onto the set of coincidences of the two maps
written from the second set to the third.

In other words, the base-change functor by $g$, $F \mapsto F'$, defines a **fully faithful** functor from the category
of quasi-coherent Modules on $S$ to the category of quasi-coherent Modules on $S'$ endowed with descent data relative to
$g$. Moreover:

**Corollary. Descent of Modules.**

<!-- label: VIII.1.3 -->

For every quasi-coherent Module $F'$ on $S'$, every descent datum on $F'$ relative to $g$ is **effective**, i.e. $F'$,
with its descent datum, is isomorphic to the inverse image by $g$ of a quasi-coherent Module on $S$, determined up to
unique isomorphism by VIII.1.2.

In other words, the preceding fully faithful functor is even an **equivalence**. In practice, this means that giving a
quasi-coherent Module on $S$ is the same as giving a quasi-coherent Module on $S'$ endowed with descent data relative to
$g$.

**Proof of VIII.1.1.** Let first $T$ be an $S$-prescheme that is $S$-isomorphic to the sum of a family of induced open
subsets `Sᵢ` of $S$ covering $S$. Then it is evident that the structural morphism $T \to S$ is a morphism of effective
$\mathcal{F}$-descent. This means precisely that giving a quasi-coherent Module $F$ on $S$ is equivalent to giving
quasi-coherent Modules `Fᵢ` on the `Sᵢ`, together with gluing isomorphisms $\phi_{ji}: F_{i}|S_{i}\cap S_{j} \to
F_{j}|S_{i}\cap S_{j}$ satisfying the familiar cocycle condition. By VII, 8,

<!-- original page 197 -->

it follows that, in order to verify that $g: S' \to S$ is a morphism of effective $\mathcal{F}$-descent, it suffices to
verify it for the morphism $g_{T}: T' = T \times_{S} S' \to T$ deduced from $g$ by the base change $T \to S$. Note that
the hypothesis on $T \to S$ remains stable under arbitrary base change, hence $T \to S$ is in fact a **universal**
morphism of effective $\mathcal{F}$-descent. Taking for the `Sᵢ` affine open subsets covering $S$, we are therefore
reduced to the case where $S$ is affine.

Then $S'$ is a finite union of affine open subsets; taking the $S$-scheme sum of these, one obtains an affine $S$-scheme
$S_{1}$ and an $S$-morphism $S_{1} \to S'$ that is flat and surjective. Thus $S_{1}$ is also faithfully flat over $S$.
If, therefore, one proves that a faithfully flat affine morphism is a morphism of effective $\mathcal{F}$-descent, hence
a strict universal morphism of $\mathcal{F}$-descent, the hypothesis being stable under base change, it follows in
particular that the structural morphism $S_{1} \to S$ is a strict universal morphism of $\mathcal{F}$-descent. Since
there exists an $S$-morphism $S_{1} \to S'$, it will indeed follow, by [VIII.D], that $g: S' \to S$ is a strict morphism
of $\mathcal{F}$-descent.

Thus we are reduced to the case where $g$ is an affine morphism; as we have seen, we may then moreover suppose $S$
affine. Hence **we may suppose $S$ and $S'$ affine**. In this case, VIII.1.2 is equivalent to:

**Lemma.**

<!-- label: VIII.1.4 -->

Let $A$ be a ring, $A'$ a faithfully flat $A$-algebra, $M$ and $N$ two $A$-modules, $M'$ and $N'$ the $A'$-modules
obtained by change of rings $A \to A'$, and $M''$, $N''$ the $A'' = A' \otimes_{A} A'$-modules obtained by change of
rings $A \to A''$. Then the sequence of maps of sets

```text
Hom_A(M,N) → Hom_{A′}(M′,N′) ⇉ Hom_{A″}(M″,N″)
```

is exact.

<!-- original page 198 -->

Since the homomorphism $N \to N'$ is injective, $A'$ being faithfully flat over $A$, the first arrow is injective. It
remains to prove that if an $A'$-homomorphism $u': M' \to N'$ is compatible with the descent data, then it comes from an
$A$-homomorphism $u: M \to N$. But this also simply means that $u'$ maps the subset $M$ of $M'$ into the subset $N$ of
$N'$. The induced map $u: M \to N$ will then automatically be $A$-linear, since $u'$ is $A'$-linear, and one sees
similarly that $u'$ is necessarily equal to $u \otimes_{A} A'$.

Now if $x \in M$, then $u'(x)$ is an element in the kernel of the pair of maps `N′ ⇉ N″`. Thus, in order to prove
VIII.1.4, we are reduced to the following special case, corresponding to the case $M = A$:

**Corollary.**

<!-- label: VIII.1.5 -->

Let $N$ be an $A$-module. Then the sequence of maps of sets

```text
N → N′ ⇉ N″
```

is exact.

Indeed, let $A_{1}$ be a faithfully flat $A$-algebra. To show that the sequence under consideration is exact, it
suffices to prove that the sequence deduced from it by the change of rings $A \to A_{1}$ is exact. But the latter, as
one sees at once, is the sequence relative to the $A_{1}$-module $N_{1} = N \otimes_{A} A_{1}$ and to the
$A_{1}$-algebra $A'_{1} = A_{1} \otimes_{A} A'$. It is therefore enough to find an $A_{1}$ faithfully flat over $A$ such
that $\operatorname{Spec}(A'_{1}) \to \operatorname{Spec}(A_{1})$ is a strict morphism of $\mathcal{F}$-descent. It
indeed suffices to take $A_{1} = A'$, for then the preceding morphism admits a right inverse, hence by [VIII.D] it is a
morphism of effective descent for any fibered category over `Sch`.

It remains finally to show that if $N'$ is an $A'$-module endowed with descent data for $A \to A'$, i.e. endowed with an
isomorphism

$$ \phi: N'_{1} \simeq N'_{2} $$

between the two modules deduced from $N'$ by the changes of rings `A′ ⇉ A′ ⊗_A A′`, then

<!-- original page 199 -->

$N'$ is isomorphic, with its descent datum, to a module $N \otimes_{A} A'$. Taking VIII.1.5 into account, one sees
easily that this statement is equivalent to the following:

**Lemma.**

<!-- label: VIII.1.6 -->

Let $N'$ be an $A'$-module endowed with descent data relative to $A \to A'$, where $A'$ is an $A$-algebra. Let $N$ be
the $A$-submodule of $N'$ formed by the $x$ such that

```text
φ(x ⊗_{A′} 1_{A′}) = 1_{A′} ⊗_{A′} x,
```

and consider the canonical homomorphism

```text
N ⊗_A A′ → N′,
```

which is then compatible with the descent data. If $A'$ is faithfully flat over $A$, this homomorphism is an
isomorphism.

Let us prove this lemma. Let again $A_{1}$ be a faithfully flat $A$-algebra. To show that the morphism under
consideration is an isomorphism, it suffices to prove that it becomes so after the change of rings $A \to A_{1}$. Now,
using the flatness of $A_{1}$ over $A$, one sees that the homomorphism so obtained is none other than the one that would
be obtained directly in terms of the module $N' \otimes_{A} A_{1}$ over $A'_{1} = A' \otimes_{A} A_{1}$, endowed with
the descent datum relative to $A_{1} \to A'_{1}$ canonically deduced by change of rings from the datum given on $N'$.
Thus it suffices to find an $A_{1}$ faithfully flat over $A$ such that $\operatorname{Spec}(A'_{1}) \to
\operatorname{Spec}(A_{1})$ is a morphism of effective $\mathcal{F}$-descent. As above, take $A_{1} = A'$. This finishes
the proof of VIII.1.6, and hence the proof of VIII.1.1.

**Corollary. Descent of Sections of Modules.**

<!-- label: VIII.1.7 -->

Let $g: S' \to S$ be a faithfully flat and quasi-compact morphism of preschemes. For every quasi-coherent Module $G$ on
$S$, let $G'$ and $G''$ be its inverse images on $S'$ and $S'' = S' \times_{S} S'$, and consider the diagram of
homomorphisms of Modules on $S$:

```text
G → g_*(G′) ⇉ h_*(G″),
```

where $h: S'' \to S$ is the structural morphism. This diagram is **exact**.

<!-- original page 200 -->

Indeed, this means that for every open $U$ in $S$, the corresponding diagram formed by the sections over $U$ is exact.
One may evidently suppose $U = S$, and the exactness in question is then a special case of VIII.1.2, obtained by taking
$F = \mathcal{O}_{S}$.

Since the inverse-image functor of Modules is right exact, one concludes formally from VIII.1.1:

**Corollary. Descent of Quotient Modules.**

<!-- label: VIII.1.8 -->

With the notation of VIII.1.7, let moreover $Quot(F)$, for every quasi-coherent Module $F$ on a prescheme, denote the
set of quasi-coherent quotient Modules of $F$. With this convention, the diagram of maps of sets

```text
Quot(G) → Quot(G′) ⇉ Quot(G″)
```

is exact.

One would evidently have the same statement with submodules instead of quotient Modules, since the two correspond
bijectively. Taking in particular $G = \mathcal{O}_{S}$, one obtains:

**Corollary. Descent of Closed Subpreschemes.**

<!-- label: VIII.1.9 -->

For every prescheme $X$, let $H(X)$ be the set of closed subpreschemes of $X$. With this notation, and under the
conditions of VIII.1.7, the following diagram of maps of sets

```text
H(S) → H(S′) ⇉ H(S″)
```

**is exact**.

Theorem VIII.1.1 should be completed by the following result:

**Proposition. Descent of Properties of Modules.**

<!-- label: VIII.1.10 -->

Let $g: S' \to S$ be a faithfully flat and quasi-compact morphism, and let $F$ be a quasi-coherent Module on $S$. In
order that $F$ be of finite type, respectively of finite presentation, respectively locally free and of finite type, it
is necessary and sufficient that its inverse image $F'$ on $S'$ be so.

It remains only to prove the “suffices” direction. One may evidently suppose $S$ affine,

<!-- original page 201 -->

and then, replacing $S'$ by a sum of affine open subsets covering $S'$, one is reduced to the case where $S'$ is also
affine. Then our statement is equivalent to the following:

**Corollary.**

<!-- label: VIII.1.11 -->

Let $A$ be a ring, $A'$ a faithfully flat $A$-algebra, $M$ an $A$-module, and $M'$ the $A'$-module $M \otimes_{A} A'$.
In order that $M$ be of finite type, respectively of finite presentation, respectively locally free of finite type, it
is necessary and sufficient that $M'$ be so.

Indeed, $M = colim_{i} M_{i}$, where the `Mᵢ` are the finite-type submodules of $M$. Hence $M' = colim_{i} M'_{i}$, and
if $M'$ is of finite type, then $M'$ is equal to one of the $M'_{i}$; by faithful flatness, $M$ is equal to `Mᵢ`, hence
$M$ is of finite type. Consequently there exists an exact sequence

$$ 0 \to R \to L \to M \to 0, $$

with $L$ free of finite type, whence an exact sequence

$$ 0 \to R' \to L' \to M' \to 0, $$

with $L'$ free of finite type. Thus if $M'$ is of finite presentation, $R'$ is of finite type, and by what precedes $R$
is of finite type, hence $M$ is of finite presentation. Finally, saying that $M$ is locally free and of finite type
means that it is of finite presentation and flat, cf. IV in the noetherian case; the general case is left to the reader.
Since each of these properties descends, so does their conjunction. This finishes the proof.

**Remark.**

<!-- label: VIII.1.12 -->

The conjunction of VIII.1.1 and VIII.1.10 shows that the statement VIII.1.1 remains valid when one replaces the fibered
category $\mathcal{F}$ by the fibered subcategory formed by quasi-coherent Modules of finite type, respectively of
finite presentation, respectively locally free of finite type, respectively locally free of given rank $n$.

## 2. Descent of Affine Preschemes over Another

<!-- label: VIII.2 -->

<!-- original page 202 -->

Since the inverse-image functor of Modules is compatible with tensor product and other tensor operations, Theorem
VIII.1.1 implies various variants, obtained by considering, instead of a single quasi-coherent Module, a quasi-coherent
Module or a system of quasi-coherent Modules endowed with various additional structures expressed by means of tensor
operations.

For example, the data of three quasi-coherent Modules $F$, $G$, $H$ on $S$ and a pairing

$$ F \otimes G \to H $$

is equivalent to the data of three quasi-coherent Modules $F'$, $G'$, $H'$ on $S'$, endowed with descent data relative
to $g: S' \to S$, and endowed with a pairing

$$ F' \otimes G' \to H' $$

“compatible” with these descent data, in the evident sense. For example, if $F = G = H$, one sees that the data of a
quasi-coherent Module $F$ on $S$ endowed with an algebra law, which for the moment we do not suppose to satisfy any
axiom of associativity, commutativity, or existence of a unit section, is equivalent to the same data on $S'$, endowed
in addition with descent data. Using the results of the preceding number, one checks at once that $F$ satisfies one of
the usual axioms just mentioned if and only if $F'$ does.

For example, the data of a quasi-coherent Algebra $\mathcal{A}$ on $S$, by which from now on we mean associative,
commutative, and with unit section, is equivalent to the data of a quasi-coherent Algebra $\mathcal{A}'$ on $S'$ endowed
with descent data relative to $g: S' \to S$. Recalling the equivalence between the dual category of quasi-coherent
Algebras on $S$ and the category of affine $S$-preschemes over $S$, EGA II, §1, one obtains at once:

**Theorem.**

<!-- label: VIII.2.1 -->

Let $\mathcal{F}'$ be the fibered category of affine morphisms of preschemes $f: X \to S$, regarded as a fibered
subcategory of the fibered category

<!-- original page 203 -->

of arrows in the category `Sch` of preschemes, VI.11.a. Let $g: S' \to S$ be a faithfully flat and quasi-compact
morphism of preschemes. Then $g$ is a morphism of effective $\mathcal{F}'$-descent.

## 3. Descent of Set-Theoretic Properties and Finiteness Properties of Morphisms

<!-- label: VIII.3 -->

_\[Translator’s note: the source section title has a footnote referring to further results of the same kind in EGA IV
2.3, 2.6, and 2.7.\]_

**Proposition.**

<!-- label: VIII.3.1 -->

Let $f: X \to Y$ be an $S$-morphism, let $g: S' \to S$ be a surjective morphism, and let $f': X' = X \times_{S} S' \to
Y' = Y \times_{S} S'$ be the morphism deduced from $f$ by base change using $g: S' \to S$. In order that $f$ be
surjective, respectively radicial, it is necessary and sufficient that $f'$ be so.

Note that $f'$ can also be obtained by the base change $Y' \to Y$, which is also surjective since it is deduced from the
surjective morphism $g: S' \to S$. On the other hand, for every $y \in Y$ and every $y' \in Y'$ lying over $y$, one has
an isomorphism

```text
X′_{y′} ≃ X_y ⊗_{κ(y)} κ(y′),
```

where $X_{y}$ denotes the fiber of $X$ at $y$, and $X'_{y'}$ that of $X'$ at $y'$. It follows that $X_{y}$ is nonempty,
respectively has at most one point and that point corresponds to a radicial residue extension, if and only if $X'_{y'}$
has the same property. This proves VIII.3.1.

**Corollary.**

<!-- label: VIII.3.2 -->

Under the conditions of VIII.3.1, if $f'$ is injective, respectively bijective, then $f$ is likewise.

This comes from the fact that if $X'_{y'}$ has at most one point, respectively exactly one point, then the same is true
of $X_{y}$. This is indeed so, since the morphism $X'_{y'} \to X_{y}$ is surjective, being deduced from
$\operatorname{Spec}(\kappa(y')) \to \operatorname{Spec}(\kappa(y))$, which is surjective.

**Proposition.**

<!-- label: VIII.3.3 -->

With the notation of VIII.3.1, suppose that $g: S' \to S$ is surjective and quasi-compact, respectively faithfully flat
and quasi-compact. In order that $f$ be quasi-compact, respectively of finite type, it is necessary and sufficient that
$f'$ be so.

<!-- original page 204 -->

Only the “suffices” direction has to be proved. One may evidently suppose $S = Y$, since the hypothesis made on $g: S'
\to S$ is preserved for $Y' \to Y$. Moreover, one may suppose $Y$ affine. Then $Y'$ is quasi-compact, hence $X'$ is
quasi-compact, since $f'$ is so by hypothesis. Let $(X_{i})_{i}\in I$ be a family of affine open subsets of $X$ covering
$X$. Then the $X'_{i}$ are open subsets of $X'$ covering $X'$, so a finite subfamily covers $X'$. Since $X' \to X$ is
surjective, it follows that the corresponding `Xᵢ` already cover $X$, and hence $X$ is quasi-compact, i.e. $f$ is
quasi-compact.

Suppose now that $f'$ is of finite type, and prove that $f$ is so, assuming $g$ faithfully flat. Replacing $Y'$ by the
sum of a family of affine open subsets covering it, one may suppose $Y'$ affine. Finally, since $X$ is covered by
finitely many affine open subsets `Xᵢ` by what precedes, it remains to show that they are of finite type over $Y$,
knowing that $X'_{i}$ is of finite type over $Y'$. This reduces us to:

**Corollary.**

<!-- label: VIII.3.4 -->

Let $B$ be an $A$-algebra, $A'$ a faithfully flat $A$-algebra, and $B' = B \otimes_{A} A'$ the $A'$-algebra deduced from
$B$ by change of rings. In order that $B$ be of finite type, it is necessary and sufficient that $B'$ be so.

Only the “suffices” direction has to be proved. We have $B = colim_{i} B_{i}$, where the `Bᵢ` are the finite-type
subalgebras of $B$. Thus $B' = colim_{i} B'_{i}$, and if $B'$ is of finite type over $A'$, then $B'$ is equal to one of
the $B'_{i}$; hence $B$ is equal to `Bᵢ`, and is therefore of finite type.

**Corollary.**

<!-- label: VIII.3.5 -->

Again suppose that the base-change morphism $g: S' \to S$ is faithfully flat and quasi-compact. In order that $f$ be
quasi-finite, it is necessary and sufficient that $f'$ be so.

Indeed, the property “quasi-finite” is by definition the conjunction of “of finite type” and “with finite fibers”; each
descends by $g$, the first by VIII.3.3, the second by the reasoning of VIII.3.1, which uses only the surjectivity of
$g$.

**Remarks.**

<!-- label: VIII.3.6 -->

Let $A$ be a ring and $X$ an $A$-prescheme. One sees easily that the following conditions are equivalent:

1. There exists a noetherian ring $A_{0}$, which one may if desired suppose to be a finite-type subring of $A$, an
   $A_{0}$-prescheme $X_{0}$ of finite type, a homomorphism $A_{0} \to A$, and an $A$-isomorphism $X \simeq X_{0}
   \times_{A_{0}} A$.
1. The diagonal morphism $X \to X \times_{\operatorname{Spec}(A)} X$ is quasi-compact, a void condition if $X$ is
   separated over $A$; $X$ is a finite union of affine open subsets `Xᵢ` whose rings `Bᵢ` are algebras of finite
   presentation over $A$, i.e. quotients of polynomial algebras in finitely many indeterminates by finite-type ideals.

<!-- original page 205 -->

If $X$ itself is affine, with ring $B$, these conditions simply mean that $B$ is an algebra of finite presentation over
$A$.

A morphism $f: X \to Y$ is said to be a **morphism of finite presentation**, and one also says that $X$ is of finite
presentation over $Y$, if $Y$ is a union of affine open subsets `Yᵢ` such that $X|Y_{i}$, as a `Yᵢ`-prescheme, satisfies
the preceding equivalent conditions. The same is then true for $X|Y'$ for **every** affine open subset $Y'$ in $Y$. This
is a property stable under base change, and moreover the composite of two morphisms of finite presentation is of finite
presentation.

With these notions in place, one sees from (2), proceeding as in VIII.1.10, that that statement remains valid when the
words “of finite type” are replaced by “of finite presentation”.

## 4. Descent of Topological Properties

<!-- label: VIII.4 -->

**Theorem.**

<!-- label: VIII.4.1 -->

Let $g: Y' \to Y$ be a morphism, and let $Z$ be a subset of $Y$. Suppose that $g$ is flat, and that there exists a
quasi-compact morphism $f: X \to Y$ such that $Z = f(X)$. N.B. if $Y$ is noetherian, this latter condition is implied by
“$Z$ is constructible”. Then

$$ g^{-1}(closure(Z)) = closure(g^{-1}(Z)). $$

One may suppose $Y$ affine, then $Y'$ affine. Since $Y$ is affine, $X$ is a finite union of affine open subsets `Xᵢ`,
and replacing $X$ by the sum of the `Xᵢ`, one may also suppose $X$ affine. Let $A$, $A'$, $B$ be the rings of $Y$, $Y'$,
$X$, and let $B' = B \otimes_{A} A'$ be the ring of $X' = X \times_{Y} Y'$. Let $I$ be the kernel of $A \to B$, and $I'$
the kernel of $A' \to B'$. Thus the closed subsets of $Y$ and $Y'$ defined by these ideals are respectively the closure
of $Z = f(X)$ and the closure of $Z' = f'(X') = g^{-1}(Z)$. We want to show that the latter is equal to
$g^{-1}(closure(Z))$, which follows from $I' = IA'$, itself a consequence of the flatness of $A'$ over $A$.

<!-- original page 206 -->

**Corollary.**

<!-- label: VIII.4.2 -->

Let $g: Y' \to Y$ be a flat and quasi-compact morphism, and let $Z'$ be a closed subset of $Y'$ saturated for the
set-theoretic equivalence relation defined by $g$. Then

$$ Z' = g^{-1}(closure(g(Z'))). $$

Indeed, $Z' = g^{-1}(Z)$, with $Z = g(Z')$. One may then apply VIII.4.1, noting that the condition imposed on $Z$ in
VIII.4.1 is indeed satisfied by taking for $X$ the prescheme $Z'$ endowed with the reduced structure induced by $Y'$.
The fact that $g$ is quasi-compact then ensures that the induced morphism $f: Z' \to Y$ is quasi-compact.

Statement VIII.4.2 also means that **the topology on $g(Y')$ induced by $Y$ is the quotient of the topology of $Y'$**.
In particular:

**Corollary.**

<!-- label: VIII.4.3 -->

Let $g: Y' \to Y$ be a faithfully flat and quasi-compact morphism. Then $g$ makes $Y$ a quotient topological space of
$Y'$; i.e. for a subset $Z$ of $Y$, $Z$ is closed, respectively open, if and only if $Z' = g^{-1}(Z)$ is so.

Recall now that two elements `a,b` of $Y'$ have the same image in $Y$ if and only if they are of the form $p_{1}(c),
p_{2}(c)$ for a suitable element $c$ in $Y'' = Y' \times_{Y} Y'$. It follows that, if $g$ is surjective, one has an
**exact** diagram of sets

```text
𝒫(Y) → 𝒫(Y′) ⇉ 𝒫(Y″),
```

where for every set $E$, $\mathcal{P}(E)$ denotes the set of its subsets. This being so, VIII.4.3 can also be
interpreted as follows:

**Corollary. Descent of Open, Respectively Closed, Subsets.**

<!-- label: VIII.4.4 -->

<!-- original page 207 -->

Let $g: Y' \to Y$ be as in VIII.4.3. For every prescheme $X$, let $Open(X)$, respectively $Closed(X)$, be the set of its
open subsets, respectively the set of its closed subsets. Then one has exact diagrams of set maps, deduced from $g$ and
the two projections of $Y'' = Y' \times_{Y} Y'$:

```text
Open(Y)   → Open(Y′)   ⇉ Open(Y″),
Closed(Y) → Closed(Y′) ⇉ Closed(Y″).
```

We have the following complement to VIII.4.3:

**Corollary.**

<!-- label: VIII.4.5 -->

Let $g: Y' \to Y$ be as in VIII.4.3, and let $Z$ be a subset of $Y$ such that there exists a quasi-compact morphism $f:
X \to Y$ with image $Z$ (for example, $Z$ constructible and $Y$ noetherian). Then $Z$ is a locally closed subset of $Y$
if and only if $Z' = g^{-1}(Z)$ is a locally closed subset of $Y'$.

It is enough to prove the “if” direction. Let $Y_{1}$ be the closed subprescheme of $Y$, the closure of $Z$ endowed with
the induced reduced structure, and let $Y_{1}' = Y_{1} \times_{Y} Y'$ be the closed subprescheme of $Y'$ inverse image
of $Y_{1}$. Its underlying set is $g^{-1}(Y_{1}) = g^{-1}(cl(Z))$, hence by VIII.4.1 it is equal to $cl(Z')$. Since $Z'$
is locally closed in $Y'$, it is open in $cl(Z')$, hence open in $Y_{1}'$. But $Y_{1}'$ is faithfully flat and
quasi-compact over $Y_{1}$, so by VIII.4.3 it follows that $Z$ is open in $Y_{1}$, that is, in $cl(Z)$; this says
exactly that $Z$ is locally closed.

**Corollary.**

<!-- label: VIII.4.6 -->

Let $g: S' \to S$ be a faithfully flat and quasi-compact morphism, let $f: X \to Y$ be an $S$-morphism, and let $f': X'
\to Y'$ be the $S'$-morphism obtained from it by base change. Suppose that $f'$ is an open map (respectively a closed
map, respectively quasi-compact and a homeomorphism into its image, respectively a homeomorphism onto). Then $f$ has the
same property.

Since $Y'$ is faithfully flat and quasi-compact over $Y$, one may suppose $Y = S$. Let $Q$ be a subset of $X$; then,
denoting by $h$ the projection morphism $X' \to X$, one has

<!-- original page 208 -->

$$ g^{-1}(f(Q)) = f'(h^{-1}(Q)). $$

If $Q$ is open (respectively closed), so is $h^{-1}(Q)$, hence so is $f'(h^{-1}(Q))$ if $f'$ is assumed to be an open
map (respectively a closed map); therefore $f(Q)$ has the same property, by the preceding formula and VIII.4.3. This
proves the first two assertions in VIII.4.6.

It remains to examine the case where $f'$ is a homeomorphism into its image, and then to prove that $f$ is a
homeomorphism into its image. The case of a homeomorphism onto follows from VIII.3.1. By VIII.3.2, $f$ is injective; it
remains to prove that the map $X \to f(X)$ is open. We already know that $f$ is quasi-compact by VIII.3.3. It suffices
to prove that for every closed subset $Z$ of $X$ one has $Z = f^{-1}(cl(f(Z)))$. Since $h: X' \to X$ is surjective, this
is equivalent to the analogous formula after inverse image by $h$, namely

$$ Z' = f'^{-1}(g^{-1}(cl(f(Z)))), $$

where $Z' = h^{-1}(Z)$. By VIII.4.1 applied to the subset $f(Z)$ of $Y$, one has $g^{-1}(cl(f(Z))) = cl(g^{-1}(f(Z)))$,
and the formula to be proved is equivalent to

$$ Z' = f'^{-1}(cl(f'(Z'))), $$

which follows from the hypothesis that $f'$ is a homeomorphism into its image.

N.B. In this last argument, once $f$ is already assumed quasi-compact, we have not used that $g$ is quasi-compact, but
only that $g$ is faithfully flat. Thus under this hypothesis one can descend the property “homeomorphism into its
image,” or “homeomorphism onto,” or again, by the preceding argument, the property “$f'$ is quasi-compact and makes
$f'(X')$ a quotient topological space of $X'$.”

We shall say that a morphism $f: X \to Y$ of preschemes is **universally open** (respectively **universally closed**,
respectively **universally bicontinuous**, etc.) if for every base change $Y' \to Y$, the morphism $f': X' \to Y'$ is
open (respectively closed, respectively a homeomorphism onto its image). We then deduce from VIII.4.6:

**Corollary.**

<!-- label: VIII.4.7 -->

<!-- original page 209 -->

Under the conditions of VIII.4.6, $f$ is universally open (respectively universally closed, respectively a universal
homeomorphism into its image, respectively a universal homeomorphism) if and only if $f'$ is.

**Corollary.**

<!-- label: VIII.4.8 -->

Under the conditions of VIII.4.6, $f$ is separated (respectively proper) if and only if $f'$ is.

To say that $f$ is separated means that the diagonal morphism $X \to X \times_{Y} X$ is closed, or also universally
closed; the first assertion of VIII.4.8 therefore follows from VIII.4.7. To say that $f$ is proper means that $f$
satisfies the conditions: a) $f$ is of finite type, b) $f$ is separated, c) $f$ is universally closed. Condition a)
descends by VIII.3.3; condition b) also descends by what we have just seen; finally condition c) descends by VIII.4.7.

**Remarks.**

<!-- label: VIII.4.9 -->

Recall that when $g: Y' \to Y$ is a flat morphism of finite type, with $Y$ locally noetherian, then $g$ is an open
morphism (VI IV.6.6), which is a sharper result than VIII.4.3. One should note, however, that if $f$ is a faithfully
flat and quasi-compact morphism of noetherian preschemes, then $f$ is not in general an open morphism. For instance, let
$Y$ be an irreducible scheme whose generic point $y$ is not open (for example an algebraic curve), and take $Y'$ to be
the sum scheme $Y \amalg \operatorname{Spec}(\kappa(y))$; then the image, under the structural morphism $Y' \to Y$, of
the open part $\operatorname{Spec}(\kappa(y))$ is not an open subset of $Y$.

The reader should also observe that various statements of the present exposé become false if one drops the hypothesis
that the faithfully flat morphism under consideration is also quasi-compact. The typical counterexample is obtained by
taking $Y'$ to be the sum scheme of the spectra of the local rings of the points of $Y$. For example, again taking $Y$
to be an irreducible algebraic curve and $Z$ to be the subset of $Y$ consisting of the generic point, its inverse image
in $Y'$ is open, while $Z$ is not open.

### 4.10.

<!-- label: VIII.4.10 -->

<!-- original page 210 -->

Various statements of the present exposé remain valid if the hypothesis that $Y'$ be flat over $Y$ is replaced by the
following one: there exists a finite-type Module $F$ on $Y'$, with support $Y'$, flat relative to $Y$. Faithful flatness
is then to be replaced by the preceding hypothesis together with the hypothesis that $Y' \to Y$ is surjective. This
applies to the first two assertions in VIII.1.10, to VIII.3.3, VIII.3.5, VIII.4.1, and consequently to all the results
of the present number.

## 5. Descent of Morphisms of Preschemes

<!-- label: VIII.5 -->

**Proposition.**

<!-- label: VIII.5.1 -->

Let $g: S' \to S$ be a morphism of preschemes.

a) Suppose that $g$ is surjective and that the homomorphism

$$ g*: \mathcal{O}_{S} \to g_{*}(\mathcal{O}_{S}') $$

is injective. Then $g$ is an epimorphism in the category of preschemes, and even in the category of ringed spaces.

b) Suppose that $g$ is surjective and makes $S$ a quotient topological space of $S'$. Let $S'' = S' \times_{S} S'$, let
$h: S'' \to S$ be the structural morphism, and consider the canonical diagram of homomorphisms

```text
𝒪_S → g_*(𝒪_S′) ⇉ h_*(𝒪_S″).
```

Suppose this diagram is **exact**. Then $g$ is an effective epimorphism in the category of preschemes (and also in the
category of ringed spaces), that is, the diagram

$$ S \leftarrow S' \Leftrightarrow S'' $$

is exact.

**Proof.** a) We must show that a morphism of ringed spaces $f: S \to Z$ is known once `fg` is known. Since $g$ is
surjective, the underlying set map $f_{0}$ of $f$ is known; it remains to determine the homomorphism of sheaves of rings
$\mathcal{O}_{Z} \to \mathcal{O}_{S}$, or equivalently the homomorphism

<!-- original page 211 -->

$$ u: f^{-1}_{0}(\mathcal{O}_{Z}) \to \mathcal{O}_{S} $$

defined by $f$. We already know the homomorphism

$$ (fg)^{-1}_{0}(\mathcal{O}_{Z}) = g^{-1}_{0}(f^{-1}_{0}(\mathcal{O}_{Z})) \to \mathcal{O}_{S}' $$

defined by `fg`, or equivalently we have a homomorphism

$$ f^{-1}_{0}(\mathcal{O}_{Z}) \to g_{0}*(\mathcal{O}_{S}') = g_{*}(\mathcal{O}_{S}'). $$

One immediately checks that the latter is none other than the composite of $g*: \mathcal{O}_{S} \to
g_{*}(\mathcal{O}_{S}')$ with $u$; since $g*$ is injective, $u$ is known once $g*u$ is known.

\[
N.B. We have obviously not used the fact that $g: S' \to S$ is a morphism of preschemes; the statement would hold for an
arbitrary morphism of ringed spaces. The same remark applies to b), both in the category of ringed spaces and in the
category of spaces ringed by local rings. Notice also that if $g$ is a morphism of preschemes, not necessarily
surjective, such that $g*: \mathcal{O}_{S} \to g_{*}(\mathcal{O}_{S}')$ is injective, then for two morphisms $f_{1}, f_{2}$ from $S$ to a **scheme** $Z$
such that $f_{1}g = f_{2}g$, one has $f_{1} = f_{2}$. Indeed, if $I$ is the Ideal on $S$ defining the subprescheme of $S$ where $f_{1}$
and $f_{2}$ coincide (the inverse image of the diagonal subprescheme of $Z \times Z$ by $(f_{1},f_{2})$), one sees that $I$ is
contained in $Ker(g*)$.
\]

b) We must show that for every ringed space $Z$, the following diagram of maps is exact,

```text
Hom(S,Z) → Hom(S′,Z) ⇉ Hom(S″,Z),
```

and likewise when $Z$ is a space ringed by local rings and one restricts to homomorphisms of spaces ringed by local
rings. Since by a) we already know that the first map is injective, it remains to see that if $f': S' \to Z$ is a
homomorphism of ringed spaces such that $f'p_{1} = f'p_{2}$, then $f'$ is of the form `fg`, where $f: S \to Z$ is a
homomorphism of ringed spaces.

<!-- original page 212 -->

Since $g$ is surjective, it is then evident that if $f'$ is a morphism of spaces ringed by local rings, the same will be
true for $f$.

The hypothesis on $f'$ implies that the underlying set map $f_{0}'$ is constant on the fibers of the map $g_{0}$. Since
$g_{0}$ is surjective, $f_{0}'$ factors uniquely as $f_{0}' = f_{0}g_{0}$, where $f_{0}: S \to Z$ is a map, necessarily
continuous because $g_{0}$ identifies $S$ with a quotient topological space of $S'$. Now consider the homomorphism

$$ f^{-1}_{0}(\mathcal{O}_{Z}) \to g_{*}(\mathcal{O}_{S}') $$

deduced from the homomorphism $(f_{0}g_{0})^{-1}(\mathcal{O}_{Z}) \to \mathcal{O}_{S}'$ corresponding to $f'$. The
hypothesis $f'p_{1} = f'p_{2}$ is then interpreted as saying that the composites of the preceding homomorphism with the
two homomorphisms

```text
g_*(𝒪_S′) ⇉ h_*(𝒪_S″)
```

are the same. Hence, by hypothesis b), it factors through a morphism

$$ f^{-1}_{0}(\mathcal{O}_{Z}) \to \mathcal{O}_{S}. $$

This latter morphism defines a morphism of ringed spaces $f: S \to Z$, which is the desired morphism.

**Theorem.**

<!-- label: VIII.5.2 -->

Let $\mathcal{F}$ be the fibered category of arrows in the category `Sch` of preschemes (VI VI.11.a). Then every
faithfully flat and quasi-compact morphism $g: S' \to S$ is a morphism of $\mathcal{F}$-descent (or, as one also says, a
descent morphism in `Sch`).

This means the following: let $S'' = S' \times_{S} S'$, and for two preschemes `X,Y` over $S$, consider their inverse
images $X',Y'$ over $S'$ and their inverse images $X'',Y''$ over $S''$; this gives a diagram of maps

```text
Hom_S(X,Y) → Hom_S′(X′,Y′) ⇉ Hom_S″(X″,Y″).
```

In these notations, VIII.5.2 says that this diagram is exact. Notice that it is not true in general that $g$ is a
morphism of effective descent, that is, that for every prescheme $X'$ over $S'$, every descent datum on $X'$ relative to
$g: S' \to S$ is effective. The question of effectivity, often delicate, will be examined in no. VIII.7.

<!-- original page 213 -->

We have seen in [VIII.D], taking into account that fiber products exist in `Sch`, that statement VIII.5.2 is equivalent
to the following:

**Corollary.**

<!-- label: VIII.5.3 -->

A faithfully flat and quasi-compact morphism of preschemes is a universal effective epimorphism.

Since a faithfully flat and quasi-compact morphism remains so after any base extension, we are reduced to proving that
it is an effective epimorphism. We then apply the criterion VIII.5.1 b), which gives the desired result, taking VIII.4.3
and VIII.1.7 into account.

**Corollary.**

<!-- label: VIII.5.4 -->

Let $g: S' \to S$ be a faithfully flat and quasi-compact morphism, let $f: X \to Y$ be an $S$-morphism, and let $f': X'
\to Y'$ be the $S'$-morphism obtained from it by the base change $S' \to S$. Then $f$ is an isomorphism if and only if
$f'$ is an isomorphism.

Indeed, if $f'$ is an isomorphism, it is also an isomorphism for the natural descent structures on $X'$ and $Y'$; and
since the functor $X \mapsto X'$ from $Sch_{/}S$ to the category of objects of $Sch_{/}S'$ with descent data is fully
faithful by VIII.5.2, it follows that $f$ is an isomorphism.

**Corollary.**

<!-- label: VIII.5.5 -->

Under the conditions of VIII.5.4, $f$ is a closed immersion (respectively an open immersion, respectively a
quasi-compact immersion) if and only if $f'$ is.

As usual, one may suppose $Y = S$, and only the “if” direction has to be proved. Notice that the fact that $X'/Y'$ is
endowed with a descent datum relative to $g: Y' \to Y$, and that the structural morphism $f': X' \to Y'$ is an
immersion, hence a monomorphism, implies that the two subobjects of $Y''$ obtained as inverse images of $X'/Y'$ by the
two projections from $S''$ to $S'$ are the same.

<!-- original page 214 -->

If $f'$ is a closed immersion, it follows from VIII.1.9 that there exists a closed subprescheme $X_{1}$ of $Y$ whose
inverse image by $g: Y' \to Y$ is $X'$. Thus, by uniqueness of the solution of a descent problem relative to a morphism
of $\mathcal{F}$-descent, $X_{1}$ is $Y$-isomorphic to $X$, so $f: X \to Y$ is a closed immersion. One proceeds in the
same way for an open immersion, using VIII.4.4. Finally, if $f'$ is a quasi-compact immersion, then $f$ is quasi-compact
by VIII.3.3; therefore one can apply the criterion VIII.4.5 to the subset $f(X)$ of $Y$. This proves that $f(X)$ is
locally closed, since its inverse image $f'(X')$ in $Y'$ is locally closed. Replacing $Y$ by an open subset in which
$f(X)$ is closed, one is reduced to the case where $f'$ is a closed immersion, hence $f$ is one by what precedes.

**Corollary.**

<!-- label: VIII.5.6 -->

Under the conditions of VIII.5.4, $f$ is affine if and only if $f'$ is.

One proceeds as in VIII.5.5, using VIII.2.1. One may also use Serre’s cohomological criterion [EGA II 5.2], which proves
VIII.5.6 without using descent techniques.

**Corollary.**

<!-- label: VIII.5.7 -->

Under the conditions of VIII.5.4, $f$ is integral (respectively finite, respectively finite and locally free) if and
only if $f'$ is.

Only the “if” direction has to be proved, and as usual one may suppose $Y = S$, with $Y$ affine and $Y'$ affine. Since
the hypothesis implies that $f'$ is affine, $f$ is affine as well by VIII.5.6; hence $X$, and consequently $X'$, are
affine. Let $A$, $A'$, $B$, and $B' = B \otimes_{A} A'$ be the rings of $Y$, $Y'$, $X$, and $X'$. One has $B = colim_{i}
B_{i}$, where $B_{i}$ runs through the sub-$A$-algebras of $B$ that are of finite type over $A$; hence $B' = colim_{i}
B_{i}'$, where the $B_{i}'$ are finite-type subalgebras of the $A'$-algebra $B'$. If $B'$ is integral over $A'$, the
$B_{i}'$ are finite-type modules over $A'$; since $A'$ is faithfully flat over $A$, the $B_{i}$ are finite-type modules
over $A$, that is, $B$ is integral over $A$. One sees in the same way that if $B'$ is finite over $A'$, then $B$ is
finite over $A$. The same conclusion holds for “locally free of finite type”; see VIII.1.11.

**Corollary.**

<!-- label: VIII.5.8 -->

<!-- original page 215 -->

Under the conditions of VIII.5.4, suppose $f$ quasi-compact, and let $\mathcal{L}$ be an invertible Module on $X$, with
inverse image $\mathcal{L}'$ on $X'$. Then $\mathcal{L}$ is ample (respectively very ample) relative to $f$ if and only
if $\mathcal{L}'$ is ample (respectively very ample) relative to $f'$.

Only the “if” direction has to be proved. The hypothesis on $\mathcal{L}'$ implies in any case that $f'$ is separated,
hence $f$ is separated by VIII.4.8. Since $f$ is quasi-compact and $g: Y' \to Y$ is flat, the computation of direct
images by affine coverings shows that for every integer $n$ one has isomorphisms

$$ g*(f_{*}(\mathcal{L}^{\otimes }n)) \simeq f'_{*}(\mathcal{L}'^{\otimes }n), $$

and therefore an isomorphism

$$ g*(\mathcal{S}) \simeq \mathcal{S}', $$

where $\mathcal{S}$ (respectively $\mathcal{S}'$) denotes the quasi-coherent graded Algebra on $Y$ (respectively on
$Y'$) given by the direct sum of the $f_{*}(\mathcal{L}^{\otimes }n)$ (respectively of the $f'_{*}(\mathcal{L}'^{\otimes
}n)$) for $n \geq 0$. Notice that, for every $n \geq 0$, the cokernel of the canonical homomorphism
$f'_{*}(\mathcal{S}'_{n}) \to \mathcal{L}'^{\otimes }n$ is the inverse image by $X' \to X$ of the cokernel of
$f_{*}(\mathcal{S}_{n}) \to \mathcal{L}^{\otimes }n$; hence its support $Z'_{n}$ is the inverse image of the support
$Z_{n}$. If $\mathcal{L}'$ is ample, the intersection of the $Z'_{n}$ is empty; since $X' \to X$ is surjective, the
intersection of the $Z_{n}$ is empty, that is, one has a canonical morphism

$$ j: X \to \operatorname{Proj}(\mathcal{S}) $$

(EGA II 3). Moreover, the analogous morphism

$$ j': X' \to \operatorname{Proj}(\mathcal{S}') $$

is none other than the one deduced from the preceding morphism by the base change $Y' \to Y$ (loc. cit.). With this
said, to say that $\mathcal{L}'$ is ample relative to $f'$ means that $j'$ is an immersion, necessarily quasi-compact
since $f'$ is quasi-compact. Thus by VIII.5.5, $j$ is an immersion; that is, $\mathcal{L}$ is ample relative to $f$.

One proceeds in an entirely analogous way in the case of “very ample,” restricting above to $n = 1$ and replacing
$\operatorname{Proj}(\mathcal{S})$ by the projective bundle $\mathcal{P}(\mathcal{S}_{1})$ associated with
$\mathcal{S}_{1}$.

<!-- original page 216 -->

Recall (EGA II 5.1.1) that a quasi-compact morphism $f$ is called **quasi-affine** if, for every affine open $U$ in $Y$,
$f^{-1}(U)$ is a prescheme isomorphic to an open subscheme of an affine scheme. One shows (loc. cit.) that this is
equivalent to saying that $\mathcal{O}_{X}$ is ample (or also very ample) relative to $f$. Thus VIII.5.8 implies:

**Corollary.**

<!-- label: VIII.5.9 -->

Under the conditions of VIII.5.4, and assuming $f$ quasi-compact, $f$ is quasi-affine if and only if $f'$ is.

**Remarks.**

<!-- label: VIII.5.10 -->

Hironaka’s example of a non-projective variety shows that one can have a proper morphism $f: X \to Y$ of nonsingular
algebraic varieties (with $Y$ projective), such that $Y$ is the union of two open subsets $Y_{i}$ for which $X_{i} = X
\times_{Y} Y_{i}$ is projective over $Y_{i}$, while $f$ is not projective. Thus, putting $Y' = Y_{1} \amalg Y_{2}$, $Y'$
is faithfully flat and quasi-compact (and even quasi-finite) over $Y$, and $f': X' \to Y'$ is projective, but $f$ is not
projective. One must therefore be careful: in order to apply VIII.5.8 and deduce from the fact that $f'$ is projective
the same conclusion for $f$, one must already have on $X'$ an invertible Module $\mathcal{L}'$ ample for $f'$, **endowed
with a descent datum relative to** $X' \to X$. This allows $\mathcal{L}'$ to be regarded as the inverse image of an
invertible Module $\mathcal{L}$ on $X$, which will then be ample for $f$ by VIII.5.8. When $g: S' \to S$ is finite and
locally free, however, see VIII.7.7.

## 6. Application to Finite and Quasi-Finite Morphisms

<!-- label: VIII.6 -->

\[
Translator note: the section title contains a footnote in the source: “Cf. EGA IV 18.12 for generalizations to
preschemes not necessarily locally noetherian.”
\]

We shall prove the following two theorems:

**Theorem.**

<!-- label: VIII.6.1 -->

Let $f: X \to Y$ be a morphism **proper with finite fibers**, with $Y$ locally noetherian. Then $f$ is finite.

**Theorem.**

<!-- label: VIII.6.2 -->

Let $f: X \to Y$ be a **quasi-finite** and **separated** morphism, with $Y$ locally noetherian. Then $f$ is
quasi-affine, and a fortiori quasi-projective.

**Remarks.**

<!-- label: VIII.6.3 -->

<!-- original page 217 -->

Theorem VIII.6.1 is well known, and is due to Chevalley in the case of algebraic varieties. One also finds a simple
proof in [EGA III 4], using the “theorem on formal functions.” The proof given here does not use that theorem, but
instead uses descent theory; we give it as a bonus to the reader, since it comes “for free” at the same time as the
proof of VIII.6.2. Recall also ([EGA III 4] or [VIII.1]) that the global form of Zariski’s “Main Theorem,” deduced from
the “theorem on formal functions,” asserts that if $f: X \to Y$ is quasi-finite and **quasi-projective**, with $Y$
noetherian, then $X$ is $Y$-isomorphic to an open subprescheme of a **finite** $Y$-prescheme $Z$. The conjunction of the
“Main Theorem” and VIII.6.2 is therefore:

**Corollary.**

<!-- label: VIII.6.4 -->

Let $f: X \to Y$ be a quasi-finite and separated morphism, with $Y$ noetherian. Then $X$ is $Y$-isomorphic to an open
subprescheme of a finite $Y$-prescheme $Z$.

Another interesting consequence of VIII.6.2 for descent theory will be given with VIII.7.9.

**Proof of VIII.6.1 and VIII.6.2.** We shall admit the following fact, whose proof is easy:

**Lemma.**

<!-- label: VIII.6.5 -->

Let $X$ be a prescheme of finite type over a locally noetherian $Y$, and let $y \in Y$. Then there exists an open
neighborhood $U$ of $y$ such that $X|U$ is finite (respectively quasi-affine, respectively ...) over $U$ if and only if
$X \times_{Y} \operatorname{Spec}(\mathcal{O}_{y})$ is finite (respectively quasi-affine, respectively ...) over
$\operatorname{Spec}(\mathcal{O}_{y})$.

[Translator note: the source footnote refers to EGA IV 8.]

Since, on the other hand, the property for $f: X \to Y$ of being finite, respectively quasi-affine, is local on $Y$, in
order to prove VIII.6.1 and VIII.6.2 we are reduced to the case where $Y$ is the spectrum of a local ring, and hence has
finite dimension. We proceed by induction on

$$ n = \dim(Y), $$

the assertion being trivial for $n < 0$.

<!-- original page 218 -->

We may therefore suppose $n \geq 0$ and the assertion proved in all dimensions $n' < n$. Again one may suppose that $Y$
is the spectrum of a noetherian local ring $A$ of dimension $n$. Notice that the hypotheses made in VIII.6.1 and
VIII.6.2 are stable under base change (we already used this in the initial reduction), and they will remain true after
the base change $\operatorname{Spec}(\hat{A}) \to \operatorname{Spec}(A)$. Since the latter is faithfully flat and
quasi-compact, the statements VIII.5.7 and VIII.5.9 reduce us to the case where $A$ is moreover complete.

Using then the fact that every noetherian local ring $B$ over $A$ that is quasi-finite over $A$ is finite over $A$, and
the fact that $X$ is separated over $Y$ and the fiber over $y$ consists of isolated points, one obtains a decomposition

$$ X = X' \amalg X'', $$

where $X'$ is **finite** over $Y$ and the fiber of $X''$ at $y$ is empty. If $X$ is proper over $Y$, then so is $X''$,
and therefore its image in $Y$ is closed; since it does not contain $y$, it is empty, hence $X'' = \emptyset$ and $X =
X'$. This shows that $X$ is finite over $Y$ and proves VIII.6.1. Notice that the induction hypothesis is not used here.

If $X$ is quasi-finite over $Y$, then $X''$ is also quasi-finite; but $X''$ in fact lies over the open set $Y - {y}$ of
$Y$, **which has dimension** $< n$. By the induction hypothesis, $X''$ is quasi-affine over $Y - {y}$, hence also over
$Y$. Evidently the same is true for $X'$, and hence for their sum $X$. This proves VIII.6.2.

**Remark.**

<!-- label: VIII.6.6 -->

Theorems VIII.6.1 and VIII.6.2 remain valid if $Y$ is no longer assumed locally noetherian, provided one specifies that
$f$ is assumed to be of finite presentation (cf. VIII.3.6). Indeed, one may again suppose $Y$ affine, and then one
verifies without difficulty that the situation $f: X \to Y$ is deduced, by a base change $Y \to Y_{0}$, from a situation
$f_{0}: X_{0} \to Y_{0}$ satisfying the same hypotheses as $f$, with $Y_{0}$ **noetherian**. Thus by VIII.6.1,
respectively VIII.6.2, $f_{0}$ is finite, respectively quasi-affine, and hence the same is true of $f$. This kind of
argument is often useful for getting rid of noetherian hypotheses, which in applications always end up becoming awkward.

<!-- original page 219 -->

## 7. Effectivity Criteria for a Descent Datum

<!-- label: VIII.7 -->

As usual, consider a morphism of preschemes

$$ g: S' \to S $$

and an $S'$-prescheme $X'$. In accordance with the general facts of VII, 9, the giving of a descent datum on $X'$
relative to $g$ is equivalent to the giving of an equivalence pair

```text
q₁,q₂: X″ ⇉ X′
```

such that the structural morphism $X' \to S'$ is compatible with this pair and with the equivalence pair

```text
p₁,p₂: S″ = S′ ×_S S′ ⇉ S′
```

defined by $g$, and such that the two squares (or either one of them, which is the same by symmetry) extracted from the
corresponding diagram

$$ X' \leftarrow X'' \downarrow \downarrow S' \leftarrow S'' $$

using either $p_{1},q_{1}$ or $p_{2},q_{2}$, are **cartesian**. A solution of the descent problem posed by this descent
datum, that is, an object $X$ over $S$ endowed with an isomorphism $X \times_{S} S' \leftarrow X'$ compatible with the
descent data, is equivalent to the giving of a **cartesian** square

$$ X \leftarrow X' \downarrow \downarrow S \leftarrow S' $$

satisfying $hq_{1} = hq_{2}$.

<!-- original page 220 -->

Since the class of faithfully flat and quasi-compact morphisms is stable under base change, and since a faithfully flat
and quasi-compact morphism is an effective epimorphism by VIII.5.3, the general theory [VIII.D] gives:

**Proposition.**

<!-- label: VIII.7.1 -->

Suppose $g: S' \to S$ faithfully flat and quasi-compact. A descent datum on $X'$ relative to $g$ is effective if and
only if the equivalence relation $R = (q_{1},q_{2})$ that it defines is effective (that is, the quotient $X'/R$ exists
and $X''$ becomes the fiber square of $X'$ over $X'/R$), and the canonical morphism $X' \to X'/R$ is faithfully flat and
quasi-compact.

Thus the question of effectivity of a descent datum is a special case of the question of effectivity of an equivalence
graph, and various effectivity criteria given in this number can be obtained in this way. Nevertheless, in the context
of descent one has Theorem VIII.2.1, which implies that **if $X'$ is affine over $S'$, every descent datum on $X'$
relative to $g$ is effective**; this statement has no analogue for passage to the quotient by a general flat equivalence
graph. All the effectivity criteria we give here can also be regarded as consequences of the preceding statement.

Let $U'$ be a subprescheme of $X'$ (or more generally a subobject of $X'$ in the category `Sch`). We say that $U'$ is
**stable under the descent datum** on $X'$ if one can put on $U'$ a descent datum relative to $g$ such that the
immersion $U' \to X'$ is compatible with the descent data. This also means that the inverse images of $U'$ in $X''$ by
$q_{1}$ and $q_{2}$ are the same (or, as one also says, that $U'$ is **stable under the equivalence relation** $R$). Of
course the descent datum in question on $U'$ is then unique, and is called the **induced descent datum** from that of
$X'$. With this understood:

**Proposition.**

<!-- label: VIII.7.2 -->

Let $(X_{i}')$ be a covering of $X'$ by open subsets $X_{i}'$ stable under the descent datum. The descent datum on $X'$
is effective if and only if the induced descent data on the $X_{i}'$ are effective.

<!-- original page 221 -->

This is an easy consequence of VIII.7.1, for example, and the details of the proof are left to the reader.

**Corollary.**

<!-- label: VIII.7.3 -->

Let $(S_{i})$ be an open covering of $S$, and for each $i$ let $S_{i}'$ and $X_{i}'$ be deduced from $S'$ and $X'$ by
the base change $S_{i} \to S$. The descent datum on $X'$ is effective if and only if, for every $i$, the descent datum
on $X_{i}'$ relative to $g_{i}: S_{i}' \to S_{i}$ is effective.

This criterion almost always reduces us to the case where $S$ is affine. In the case where $S'$ is also affine, which is
the most frequent case in applications, one has:

**Corollary.**

<!-- label: VIII.7.4 -->

Suppose $S$ and $S'$ affine. The descent datum on $X'$ is effective if and only if $X'$ is the union of affine open
subsets $X_{i}'$ stable under the descent datum.

Sufficiency follows from VIII.7.2 and from the fact that, if $X_{i}'$ is affine, it is affine over $S'$ and one can
apply VIII.2.1. For necessity, note that if $X'$ comes from $X$, and if $X$ is covered by affine open subsets $X_{i}$,
then the $X_{i}' = X_{i} \times_{S} S'$ are affine open subsets stable under the descent data and covering $X'$.

**Corollary.**

<!-- label: VIII.7.5 -->

Let $g: S' \to S$ be a faithfully flat, quasi-compact, and **radicial** morphism. Then $g$ is a morphism of
**effective** descent; that is, for every $X'$ over $S'$, every descent datum on $X'$ relative to $g: S' \to S$ is
effective.

Indeed, by VIII.7.3 one may suppose $S$ affine. Since $S'$ is radicial over $S$, hence separated, $S'$ is separated.
Moreover, for every $x' \in X'$, the fiber $R(x') = q_{2}(q^{-1}_{1}(x'))$ of the set-theoretic equivalence relation
defined by $R$ is reduced to one point: since $g$ is radicial, the same is true of $p_{1},p_{2}$, which are deduced from
it by the base change $S' \to S$, and hence also of $q_{1},q_{2}$, which are deduced from the preceding ones by the base
change $X' \to S''$.

<!-- original page 222 -->

Thus **every open subset of $X'$ is stable** under the descent datum. Cover $X'$ by affine open subsets $X_{i}'$. These
are affine over $S$ because $S'$ is separated, so the induced descent datum is effective by VIII.2.1. We then conclude
by VIII.7.2.

Notice that VIII.7.5 gives the only known case of an effective descent morphism in the category of preschemes, and
probably the only case indeed, even if one restricts to noetherian schemes or to schemes of finite type over a field.

When $S$ is assumed locally noetherian and $S'$ of finite type over $S$, statement VIII.7.5 is also a special case of
the following one, which generalizes Weil’s Galois descent and Cartier’s inseparable descent:

**Corollary.**

<!-- label: VIII.7.6 -->

Let $g: S' \to S$ be a finite locally free morphism (that is, defined by an Algebra on $S$ that is a locally free module
of finite type) and surjective. Then $g$ is faithfully flat and quasi-compact, hence a descent morphism. Let $X'$ be an
$S'$-prescheme endowed with a descent datum. This datum is effective if and only if, for every $x' \in X'$, the fiber
$R(x') = q_{2}(q^{-1}_{1}(x'))$ is contained in an affine open subset. This condition is automatically satisfied if $X'$
is quasi-projective over $S'$.

The parenthetical assertion comes from the fact that, if $s$ is the point of $S$ below $x'$, then $R(x')$ is finite and
contained in the fiber $X'_{s}$; on the other hand, since $X'$ is quasi-projective over $S'$ and $S'$ is finite over
$S$, $X'$ is quasi-projective over $S$, which implies that a fiber of $X'$ over $S$ is contained in an affine open
subset.

Since every finite subset of an affine scheme has a fundamental system of affine neighborhoods, one does not lose the
hypothesis by restricting over an affine open subset of $S$; by VIII.7.3 this reduces us to the case where $S$ is
affine. By VIII.7.4, we are reduced to showing that $x'$ is contained

<!-- original page 223 -->

in an affine open subset **stable** under the descent datum. Indeed, let $U$ be an affine open subset containing
$R(x')$. Then the saturation

```text
R(X′ − U) = q₂(q₁⁻¹(X′ − U))
```

does not meet $R(x')$; moreover, since $q_{2}$ is finite (because $g$, hence $p_{2}$, is finite), and therefore closed,
the right-hand side is a closed subset of $X'$. Let $U'$ be its complement in $X'$. This is a **saturated** open subset,
and one has

$$ R(x') \subset U' \subset U, $$

with $U$ affine, but $U'$ not a priori affine. Since a finite subset $R(x')$ in an affine scheme $U$ has a fundamental
system of affine neighborhoods of the form $U_{f}$, replacing $f$ by its restriction to $U'$ shows that there exists a
section $f$ of $\mathcal{O}_{U}$ such that

```text
R(x′) ⊂ U′_f,    U′_f is affine.
```

Let $U'' = q^{-1}_{1}(U') = q^{-1}_{2}(U')$, still denoting by $q_{1},q_{2}$ the induced morphisms $U'' \to U'$, and
consider

```text
f′ = Norm_q₂(q₁*(f)),
```

where `Norm_q₂` denotes the **norm** relative to the finite locally free morphism $q_{2}: U'' \to U'$. The compatibility
of the formation of the norm with base change easily implies that $f'$ is an **invariant** section:

$$ q_{1}*(f') = q_{2}*(f'), $$

which implies that ${U'_{f}}'$ is a saturated open subset of $U'$. More precisely, denoting by $Z(f')$ the set of zeros
of a section $f'$, one finds from the properties of norms that

```text
Z(f′) = q₂(Z(q₁*(f))) = q₂(q₁*(Z(f))) = R(U′ − U′_f).
```

<!-- original page 224 -->

This implies that ${U'_{f}}' = U' - Z(f')$ is saturated, contains $R(x')$, and is contained in $U'_{f}$. Since the
latter is affine, it follows that ${U'_{f}}'$ is also affine (being equal to $(U'_{f})_{f}''$, with $f'' = f'$
restricted to ${U'_{f}}'$). It is therefore a saturated affine open subset containing $R(x')$, hence $x'$, which
completes the proof.

Notice that this argument applies whenever one has an equivalence relation (or even only a pre-equivalence relation; see
[VIII.3]) in a prescheme $X'$, finite and locally free; indeed VIII.7.6 is also a special case of the analogous result
for finite locally free pre-equivalences, loc. cit. The same remark applies to VIII.7.7 below.

Once the existence of a saturated quasi-affine open subset $U'$ containing $x'$ has been obtained, one can also appeal
to VIII.7.9 and VIII.7.2, which avoids the use of norms.

Notice moreover that under the conditions of VIII.7.6, if the descent datum on $X'$ is effective, with $X'$ coming from
$X$ over $S$, then the morphism $X' \to X$ is finite, locally free, and surjective, since it is deduced from $g$ by the
base change $X \to S$. It follows (EGA II 6.6.4) that if $X'$ is quasi-projective over $S'$, hence over $S$, then $X$ is
quasi-projective over $S$. A relatively ample invertible sheaf on $X$ is obtained by taking the **norm** of an
invertible sheaf on $X'$ relatively ample over $S$, or over $S'$, which is the same thing. Thus one obtains:

**Corollary.**

<!-- label: VIII.7.7 -->

A finite locally free and surjective morphism $g: S' \to S$ is a morphism of effective descent for the fibered category
of preschemes quasi-projective over other preschemes; that is, for every $X'$ quasi-projective over $S'$, every descent
datum on $X'$ relative to $g$ is effective, and the descended $S$-prescheme $X$ is quasi-projective over $S$.

**Proposition.**

<!-- label: VIII.7.8 -->

Let $g: S' \to S$ be a faithfully flat and quasi-compact morphism. Then $g$ is a morphism of effective descent for the
fibered category of preschemes $Z$ quasi-compact

<!-- original page 225 -->

over a prescheme $T$ and endowed with an invertible sheaf ample relative to $T$. In particular, for every prescheme $X'$
over $S'$, endowed with a descent datum relative to $g: S' \to S$, and every invertible sheaf $\mathcal{L}'$ on $X'$
ample relative to $S'$ and likewise endowed with a descent datum relative to the given one on $X'$ (that is, endowed
with an isomorphism from $q_{1}*(\mathcal{L}')$ to $q_{2}*(\mathcal{L}')$, satisfying the usual transitivity condition),
the descent datum on $X'$ is effective, and the invertible sheaf $\mathcal{L}$ on the descended prescheme $X$, deduced
from $\mathcal{L}'$ by descent, is ample relative to $S$.

The proof is entirely analogous to that of VIII.5.8. One notes that on the quasi-coherent graded Algebra $\mathcal{S}'$
on $S'$ defined by $\mathcal{L}'$ there is a descent datum, allowing one to construct a quasi-coherent graded Algebra
$\mathcal{S}$ on $S$ by VIII.1.1, whence a $P = \operatorname{Proj}(\mathcal{S})$ over $S$ such that $P' =
\operatorname{Proj}(\mathcal{S}')$ is identified, together with its descent datum, with $P \times_{S} S'$. Since by
hypothesis $X'$ is identified with an open subset of $P'$, necessarily stable under the descent datum on $P'$, the
descent datum on $X'$ is also effective, and one obtains the descended prescheme as an open subset of $P$. The details
are left to the reader.

In particular, taking $\mathcal{L}' = \mathcal{O}_{X}'$, one finds:

**Corollary.**

<!-- label: VIII.7.9 -->

Let $g: S' \to S$ be a faithfully flat and quasi-compact morphism, and let $X'$ be a **quasi-affine** prescheme over
$S'$. Then every descent datum on $X'$ relative to $g$ is effective, and the descended prescheme $X$ is quasi-affine
over $S$.

By VIII.6.2, this result applies in particular if $S'$ is locally noetherian and $X'$ is quasi-finite and separated over
$S'$; more generally, if $S'$ is arbitrary and $X'$ is of finite presentation, quasi-finite, and separated over $S'$
(cf. VIII.6.6).

**Remarks.**

<!-- label: VIII.7.10 -->

The results given in this number exhaust the currently known effectivity criteria, and probably even all useful existing
criteria. \[Translator note: the corrected source adds that this opinion turned out to be partly erroneous, referring
for example to J.-P. Murre, Séminaire Bourbaki 294 (Appendix), May 1965, and to special results, notably of Néron and
Raynaud; for descent of group schemes, see M. Raynaud’s 1968 thesis.\] Notice the following counterexamples in support
of this assertion:

<!-- original page 226 -->

1. If $S$ is the spectrum of a field, and $S'$ is the spectrum of a quadratic Galois extension, one can find an $X'$
   over $S'$, proper and smooth over $S'$, of dimension 3, endowed with a descent datum that is not effective (Serre).

1. One can find an $S$ equal to the spectrum of a regular local ring of dimension 3 (if desired, the local ring of an
   algebraic scheme over a field of prescribed characteristic), and a principal covering $T$ of $S$ with group
   $\mathbb{Z}/2\mathbb{Z}$, such that, if $t$ denotes one of the points of $T$ above the closed point $s$ of $S$, and
   $S' = T - s$, one can find an $X'$ **projective** over $S'$, regular, endowed with a descent datum relative to $g: S'
   \to S$, this descent datum not being effective.

For these constructions one uses Hironaka’s example of non-projective varieties. For (i), it is enough to use the fact
that one can find over $k$ a proper and smooth scheme $X_{0}$ of dimension 3, on which $G = \mathbb{Z}/2\mathbb{Z}$ acts
without inertia, and in which there exist two rational points `a,b` congruent under $G$ and not contained in any affine
open subset. One then puts $X' = X_{0} \times_{k} k'$, and lets $G$ act on $X'$ through the actions of $G$ on the two
factors; this gives a descent datum on $X'$ relative to $g: \operatorname{Spec}(k') \to \operatorname{Spec}(k)$. Above
$a$, respectively $b$, there is exactly one point $a'$, respectively $b'$, with quadratic residue extension, and $a'$
and $b'$ are congruent under $G$, since $X' \to X_{0}$ is compatible with the actions of $G$. Then $a'$ and $b'$ cannot
be contained in an affine open subset $U'$, for then $U = X_{0} - Im(X' - U')$ would be an open subset of $X_{0}$
containing $(a,b)$, whose inverse image in $X'$ would be contained in $U'$, hence quasi-affine; therefore $U$ would be
quasi-affine, and consequently $(a,b)$ would have an affine neighborhood in $U$.

For (ii), one uses the fact that in Hironaka’s example, $X_{0}$ is obtained as a prescheme proper over a projective
$k$-scheme $Y$, smooth over $k$. The morphism $f: X_{0} \to Y$ is birational, though this is immaterial. The group $G$
also acts on $Y$ compatibly with its actions on $X_{0}$. Finally, putting $S' = Y - f(b)$ and $X' = X_{0}|S'$, $X'$ is
projective over $S'$.

<!-- original page 227 -->

Then $X_{0}$ is endowed with a natural descent datum relative to the canonical morphism $Y \to S = Y/G$, by means of the
actions of $G$ on $X_{0}$ compatible with its actions on $Y$. This descent datum is not effective, since $(a,b)$ is not
contained in an affine open subset. The induced descent datum on $X'$ relative to $g: S' \to S$ is then not effective,
as is easily verified.

## Bibliography

**[VIII.D]** J. Giraud, _Méthode de la descente_, Mémoire no. 2 de la Société Mathématique de France, 1964.

**[VIII.1]** A. Grothendieck, Séminaire Bourbaki: _Géométrie formelle et Géométrie algébrique_, May 1959, no. 182.

**[VIII.2]** A. Grothendieck, Séminaire Bourbaki: _Technique de descente et Théorèmes d’existence I_, December 1959, no.
190\.

**[VIII.3]** A. Grothendieck, Séminaire Bourbaki: _Technique de descente et Théorèmes d’existence III_, February 1961,
no. 212.

[^viii-1-1]: We admit here the general theory of descent set out in detail in the article of J. Giraud cited in the
    footnote to the Warning, a work that we shall cite as [VIII.D] below. Cf. also [VIII.2] for a succinct account.
